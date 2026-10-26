import assert from "node:assert/strict";
import { EventEmitter } from "node:events";
import fs from "node:fs";
import { createRequire, syncBuiltinESMExports } from "node:module";
import os from "node:os";
import path from "node:path";
import { PassThrough } from "node:stream";
import { test } from "node:test";
import { fileURLToPath } from "node:url";
import { sessionFixture } from "./session-fixture.mjs";

const packageDir = process.env.PI_PACKAGE_DIR;
assert.ok(packageDir, "Set PI_PACKAGE_DIR");
const requirePi = createRequire(path.join(packageDir, "package.json"));
const { createJiti } = requirePi("jiti");
const aliases = Object.fromEntries([
  "@earendil-works/pi-agent-core", "@earendil-works/pi-ai",
  "@earendil-works/pi-coding-agent", "@earendil-works/pi-tui", "typebox",
].map(name => [name, name.startsWith("@earendil-works/")
  ? path.join(path.dirname(packageDir), name.split("/")[1], "dist", "index.js")
  : requirePi.resolve(name)]));
const jiti = createJiti(import.meta.url, { alias: aliases, moduleCache: true });
const childProcess = createRequire(import.meta.url)("node:child_process");
const originalSpawn = childProcess.spawn;
const launches = [];
let throwSpawn = false;
const mockSpawn = (command, args, options) => {
  if (throwSpawn) throw new Error("mock spawn failure");
  const proc = new EventEmitter();
  proc.stdout = new PassThrough();
  proc.stderr = new PassThrough();
  proc.signals = [];
  let announced = false;
  const announce = () => {
    if (announced) return;
    announced = true;
    const info = sessionFixture(args, options.cwd, path.join(root, "sessions"));
    proc.sessionFile = JSON.parse(info.slice(info.indexOf("{"))).sessionFile;
    proc.stderr.write(info);
  };
  process.nextTick(announce);
  proc.kill = signal => {
    announce();
    proc.signals.push(signal);
    // Deliberately use killed=true on TERM: escalation must not rely on it.
    proc.killed = true;
    if (!proc.ignoreTerm || signal === "SIGKILL") queueMicrotask(() => proc.emit("close", null, signal));
    return true;
  };
  proc.respond = (text, stopReason, errorMessage) => {
    announce();
    proc.stdout.write(JSON.stringify({ type: "message_end", message: {
      role: "assistant", content: [{ type: "text", text }], stopReason,
      ...(errorMessage === undefined ? {} : { errorMessage }),
    } }) + "\n");
  };
  proc.finish = (text = "OK", code = 0, stopReason = "stop", errorMessage) => {
    proc.respond(text, stopReason, errorMessage);
    proc.emit("close", code);
  };
  launches.push({ proc, args, options });
  return proc;
};
const root = fs.mkdtempSync(path.join(os.tmpdir(), "subagent-async-test-"));
fs.mkdirSync(path.join(root, ".pi", "agents"), { recursive: true });
fs.writeFileSync(path.join(root, ".pi", "agents", "worker.md"), "---\nname: worker\ndescription: Test\n---\nTest prompt\n");
let tool;
const events = {};
const extension = await jiti.import(fileURLToPath(new URL("../index.ts", import.meta.url)), { default: true });
childProcess.spawn = mockSpawn;
syncBuiltinESMExports();
function install(depth, workers) {
  const oldDepth = process.env.PI_SUBAGENT_DEPTH, oldWorkers = process.env.PI_SUBAGENT_WORKERS;
  try {
    if (depth === undefined) delete process.env.PI_SUBAGENT_DEPTH; else process.env.PI_SUBAGENT_DEPTH = depth;
    if (workers === undefined) delete process.env.PI_SUBAGENT_WORKERS; else process.env.PI_SUBAGENT_WORKERS = workers;
    extension({ registerTool(value) { tool = value; }, on(name, fn) { events[name] = fn; } });
  } finally {
    if (oldDepth === undefined) delete process.env.PI_SUBAGENT_DEPTH; else process.env.PI_SUBAGENT_DEPTH = oldDepth;
    if (oldWorkers === undefined) delete process.env.PI_SUBAGENT_WORKERS; else process.env.PI_SUBAGENT_WORKERS = oldWorkers;
  }
}
install();
const ctx = { cwd: root, model: { provider: "test", id: "parent" }, thinkingLevel: "medium", hasUI: false,
  sessionManager: { getSessionId: () => "parent-session", getSessionFile: () => path.join(root, "parent.jsonl") } };
const call = (params, signal, context = ctx) => tool.execute("test", params, signal, undefined, context);
const start = (params = {}, signal, context) => call({ action: "start", agent: "worker", task: "test", agentScope: "project", ...params }, signal, context);
const handle = result => result.details.jobs[0].handle;
const spawned = async count => {
  for (let i = 0; i < 200 && launches.length < count; i++) await new Promise(resolve => setTimeout(resolve, 5));
  assert.equal(launches.length, count);
};
const wait = handles => call({ action: "wait", handles });
const reset = async () => { await events.session_shutdown(); await events.session_start(); launches.length = 0; };

test("asynchronous subagent lifecycle (mock processes only)", async t => {
  try {
    await t.test("depth zero and invalid inherited budgets refuse launches but retain control operations", async () => {
      for (const [depth, workers, message] of [["0", "2", /remaining depth is 0/], ["2", "0", /worker capacity is 0/],
        ["bad", "2", /invalid inherited budget/], [undefined, "2", /invalid inherited budget/]]) {
        await events.session_shutdown(); install(depth, workers);
        await assert.rejects(start({ maxDepth: 999, maxWorkers: 999 }), message);
        await assert.rejects(call({ agent: "worker", task: "blocking", agentScope: "project" }), message);
        assert.equal(launches.length, 0);
        assert.deepEqual((await call({ action: "status" })).details.jobs, []);
        assert.match(tool.description, /Remaining depth: 0|worker capacity: 0/);
      }
      await events.session_shutdown(); install();
    });
    await t.test("child grants decrement depth and cap its reserved worker slots", async () => {
      await events.session_shutdown(); install("2", "2");
      try {
        assert.match(tool.description, /Remaining depth: 2; worker capacity: 2/);
        const h = handle(await start({ maxDepth: 99, maxWorkers: 99 })); await spawned(1);
        assert.equal(launches[0].options.env.PI_SUBAGENT_DEPTH, "1");
        assert.equal(launches[0].options.env.PI_SUBAGENT_WORKERS, "1");
        assert.equal((await call({ action: "status" })).details.jobs[0].slots, 2);
        await assert.rejects(start(), /Worker capacity exhausted/);
        launches[0].proc.finish();
        const result = (await wait([h])).details.jobs[0].result;
        assert.equal(result.maxDepth, 1); assert.equal(result.maxWorkers, 1);
      } finally { await events.session_shutdown(); install(); launches.length = 0; }
    });
    await t.test("reserved slots block siblings and queued calls until success, failure or cancellation settles", async () => {
      for (const outcome of ["success", "failure", "cancel"]) {
        const h = handle(await start({ maxDepth: 2, maxWorkers: 3 })); await spawned(1);
        assert.equal((await call({ action: "status" })).details.jobs[0].slots, 4);
        await assert.rejects(start(), /Worker capacity exhausted/);
        const pending = call({ agent: "worker", task: "queued", agentScope: "project" });
        await new Promise(resolve => setTimeout(resolve, 20));
        assert.equal(launches.length, 1);
        if (outcome === "cancel") {
          launches[0].proc.kill = signal => { launches[0].proc.signals.push(signal); return true; };
          await call({ action: "cancel", handles: [h] });
          assert.equal((await call({ action: "status" })).details.jobs[0].state, "cancelling");
          await assert.rejects(start(), /Worker capacity exhausted/);
        }
        launches[0].proc.finish(outcome, outcome === "failure" ? 1 : 0);
        await spawned(2);
        launches[1].proc.finish();
        assert.equal((await pending).isError, undefined);
        await wait([h]); await reset();
      }
    });
    await t.test("four-job rolling window returns first finish and refills without a barrier", async () => {
      const handles = [];
      for (let i = 0; i < 4; i++) handles.push(handle(await start({ model: "chosen", thinkingLevel: "off", cwd: root })));
      await spawned(4);
      await assert.rejects(start(), /Worker capacity exhausted/);
      for (const launch of launches) {
        assert.ok(!launch.args.includes("--no-session"));
        assert.equal(launch.args[launch.args.indexOf("--model") + 1], "chosen");
        assert.equal(launch.args[launch.args.indexOf("--thinking") + 1], "off");
        assert.equal(launch.options.cwd, root);
      }
      const pending = wait(handles);
      launches[2].proc.finish("third finishes first");
      const first = await pending;
      assert.equal(handle(first), handles[2]);
      assert.equal(first.details.jobs[0].state, "completed");
      assert.match(first.content[0].text, /third finishes first/);
      const replacement = handle(await start());
      await spawned(5);
      const states = (await call({ action: "status" })).details.jobs;
      assert.equal(states.filter(j => j.state === "running").length, 4);
      assert.equal(states.find(j => j.handle === handles[0]).state, "running");
      assert.equal(states.find(j => j.handle === replacement).state, "running");
      // Completed results are repeatable, not implicitly consumed.
      assert.equal(handle(await wait(handles)), handles[2]);
      await call({ action: "forget", handles: [handles[2]] });
      await assert.rejects(wait([handles[2]]), /Unknown subagent handle/);
      await reset();
    });
    await t.test("wait interruption leaves workers running; duplicate/unknown/mixed inputs fail", async () => {
      const h = handle(await start());
      await spawned(1);
      const controller = new AbortController();
      const pending = call({ action: "wait", handles: [h] }, controller.signal);
      controller.abort();
      await assert.rejects(pending, /jobs continue running/);
      assert.deepEqual(launches[0].proc.signals, []);
      await assert.rejects(call({ action: "wait", handles: [h, "bad"] }), /Unknown/);
      await assert.rejects(wait([h, h]), /distinct/);
      await assert.rejects(call({ action: "forget", handles: [h] }), /active/);
      await assert.rejects(call({ action: "status", task: "ignored?" }), /only action/);
      await assert.rejects(start({ tasks: [] }), /requires agent/);
      const cancel = await call({ action: "cancel", handles: [h] });
      assert.equal(cancel.details.jobs[0].state, "cancelling");
      assert.equal((await wait([h])).details.jobs[0].state, "cancelled");
      await reset();
    });
    await t.test("async destination launches do not ask for approval", async () => {
      const destination = path.join(root, "destination");
      fs.mkdirSync(path.join(destination, ".pi", "agents"), { recursive: true });
      fs.copyFileSync(path.join(root, ".pi", "agents", "worker.md"), path.join(destination, ".pi", "agents", "worker.md"));
      for (const context of [ctx, { ...ctx, hasUI: true, isProjectTrusted: () => false,
        ui: { confirm: () => { assert.fail("No destination approval dialog"); }, notify() {} },
      }]) {
        const h = handle(await start({ cwd: destination }, undefined, context));
        await spawned(1);
        assert.equal(launches[0].options.cwd, destination);
        launches[0].proc.finish();
        assert.equal((await wait([h])).details.jobs[0].state, "completed");
        await reset();
      }
    });
    await t.test("already aborted starts never spawn", async () => {
      const controller = new AbortController(); controller.abort();
      await assert.rejects(start({}, controller.signal), /start aborted/);
      assert.equal(launches.length, 0);
    });
    await t.test("unknown agent and setup/spawn rejection become retained failures", async () => {
      const unknown = handle(await start({ agent: "missing" }));
      const result = await wait([unknown]);
      assert.equal(result.isError, true);
      assert.match(result.content[0].text, /Unknown agent: "missing"/);
      throwSpawn = true;
      const h = handle(await start());
      assert.match((await wait([h])).content[0].text, /mock spawn failure/);
      throwSpawn = false;
      await reset();
    });
    await t.test("process error, signal exit and model error are failures, not successful progress", async () => {
      for (const mode of ["error", "signal", "model", "empty"])  {
        const h = handle(await start()); await spawned(1);
        const proc = launches.at(-1).proc;
        if (mode === "error") { proc.emit("error", new Error("ENOENT mock")); proc.emit("close", -2); }
        if (mode === "signal") proc.emit("close", null, "SIGTERM");
        if (mode === "model") proc.finish("model failed", 0, "error");
        if (mode === "empty") proc.emit("close", 0);
        assert.equal((await wait([h])).isError, true);
        await reset();
      }
    });
    await t.test("recovered assistant errors do not fail async or blocking workers", async () => {
      const transient = "OpenAI Responses stream ended before a terminal response event";
      for (const mode of ["async", "blocking"]) {
        const pending = mode === "async"
          ? wait([handle(await start())])
          : call({ agent: "worker", task: "blocking", agentScope: "project" });
        await spawned(1);
        const proc = launches[0].proc;
        proc.respond("", "error", transient);
        assert.equal((await call({ action: "status" })).details.jobs[0].state, "running");
        proc.finish("Recovered final result");
        const result = await pending;
        assert.notEqual(result.isError, true);
        const worker = mode === "async" ? result.details.jobs[0].result : result.details.results[0];
        assert.equal(worker.exitCode, 0);
        assert.equal(worker.stopReason, "stop");
        assert.equal(worker.errorMessage, undefined);
        assert.equal(worker.messages[0].errorMessage, transient, "retain the intermediate error as evidence");
        assert.match(result.content[0].text, /Recovered final result/);
        await reset();
      }
    });
    await t.test("audit evidence survives recovered failures, forget and reload; sessions cannot run concurrently", async () => {
      const h = handle(await start()); await spawned(1);
      const proc = launches[0].proc;
      proc.stdout.write(JSON.stringify({ type: "auto_retry_start", attempt: 1 }) + "\n");
      proc.respond("", "error", "Hidden transient failure");
      proc.stderr.write("Diagnostic before recovery\n");
      proc.finish("Recovered result");
      const first = (await wait([h])).details.jobs[0].result;
      const eventsFile = path.join(first.executionDir, "events.jsonl");
      assert.match(fs.readFileSync(eventsFile, "utf8"), /Hidden transient failure/);
      assert.match(fs.readFileSync(eventsFile, "utf8"), /auto_retry_start/);
      assert.match(fs.readFileSync(path.join(first.executionDir, "stderr.log"), "utf8"), /Diagnostic before recovery/);
      await call({ action: "forget", handles: [h] });
      await reset();
      assert.ok(fs.existsSync(first.sessionFile));
      assert.ok(fs.existsSync(eventsFile));
      const resumedHandle = handle(await start({ sessionFile: first.sessionFile }));
      await spawned(1);
      const duplicate = await call({ agentScope: "project", agent: "worker", task: "competing", sessionFile: first.sessionFile });
      assert.equal(duplicate.isError, true);
      assert.match(duplicate.content[0].text, /active or has a stale lock/);
      assert.equal(launches.length, 1);
      await call({ action: "cancel", handles: [resumedHandle] });
      const cancelled = (await wait([resumedHandle])).details.jobs[0].result;
      assert.equal(cancelled.sessionId, first.sessionId);
      assert.notEqual(cancelled.executionDir, first.executionDir);
      assert.equal(JSON.parse(fs.readFileSync(path.join(cancelled.executionDir, "execution.json"), "utf8")).stopReason, "aborted");
      assert.ok(!fs.existsSync(first.sessionFile + ".subagent/active"));
      await reset();
      assert.ok(fs.existsSync(cancelled.executionDir));
    });
    await t.test("a recording failure aborts the worker and cannot report success", async () => {
      const h = handle(await start()); await spawned(1);
      const proc = launches[0].proc;
      // Force announcement before damaging the active execution's event file.
      proc.respond("interim", "toolUse");
      const dir = proc.sessionFile + ".subagent";
      const execution = fs.readdirSync(dir, { withFileTypes: true }).find(entry => entry.isDirectory() && entry.name !== "active").name;
      const eventsFile = path.join(dir, execution, "events.jsonl");
      fs.unlinkSync(eventsFile); fs.mkdirSync(eventsFile);
      proc.respond("would otherwise look successful", "stop");
      const response = await wait([h]);
      assert.equal(response.isError, true);
      assert.match(response.details.jobs[0].result.errorMessage, /Session recording failed/);
      assert.ok(proc.signals.includes("SIGTERM"));
      assert.ok(!fs.existsSync(path.join(dir, "active")));
      await reset();
    });
    await t.test("finalization failures keep the session reference and are recorded as failures", async () => {
      const h = handle(await start()); await spawned(1);
      const proc = launches[0].proc;
      proc.respond("interim", "toolUse");
      fs.rmSync(proc.sessionFile + ".subagent/active", { recursive: true });
      proc.finish("Otherwise successful");
      const response = await wait([h]);
      const result = response.details.jobs[0].result;
      assert.equal(response.isError, true);
      assert.equal(result.sessionFile, proc.sessionFile);
      assert.match(result.errorMessage, /Session finalization failed/);
      assert.match(JSON.parse(fs.readFileSync(path.join(result.executionDir, "execution.json"), "utf8")).errorMessage, /Session finalization failed/);
      await reset();
    });
    await t.test("terminal errors replace earlier error text and remain failures", async () => {
      for (const finalError of ["Final provider failure", undefined]) {
        const h = handle(await start()); await spawned(1);
        const proc = launches[0].proc;
        proc.respond("", "error", "Earlier transient failure");
        proc.respond("Continue with tools", "toolUse");
        proc.finish("Final error response", 0, "error", finalError);
        const result = await wait([h]);
        const worker = result.details.jobs[0].result;
        assert.equal(result.isError, true);
        assert.equal(worker.stopReason, "error");
        assert.equal(worker.errorMessage, finalError);
        assert.equal(worker.messages[0].errorMessage, "Earlier transient failure");
        assert.doesNotMatch(result.content[0].text, /Earlier transient failure/);
        assert.match(result.content[0].text, /Final/);
        await reset();
      }
    });
    await t.test("recovery does not hide nonzero process exit or a terminal abort", async () => {
      for (const [code, stopReason] of [[7, "stop"], [0, "aborted"]]) {
        const h = handle(await start()); await spawned(1);
        const proc = launches[0].proc;
        proc.respond("", "error", "Earlier transient failure");
        proc.stderr.write("Retained diagnostic\n");
        proc.finish("Final response", code, stopReason);
        const result = await wait([h]);
        const worker = result.details.jobs[0].result;
        assert.equal(result.isError, true);
        assert.equal(worker.exitCode, code);
        assert.equal(worker.stopReason, stopReason);
        assert.equal(worker.errorMessage, undefined);
        assert.match(worker.stderr, /Retained diagnostic/);
        await reset();
      }
    });
    await t.test("shutdown cancels, waits for close, cleans prompts, invalidates handles and is idempotent", async () => {
      const h = handle(await start()); await spawned(1);
      const prompt = launches[0].args[launches[0].args.indexOf("--append-system-prompt") + 1];
      assert.ok(fs.existsSync(prompt));
      const pending = wait([h]);
      await events.session_shutdown();
      assert.equal((await pending).details.jobs[0].state, "cancelled");
      assert.ok(!fs.existsSync(prompt));
      await events.session_shutdown();
      await assert.rejects(wait([h]), /Unknown/);
      await assert.rejects(start(), /shutting down/);
      await events.session_start(); launches.length = 0;
    });
    await t.test("session replacement cancels old ownership and completion is visible", async () => {
      const notifications = [];
      const h = handle(await start({}, undefined, { ...ctx, hasUI: true,
        isProjectTrusted: () => true,
        ui: { notify: (...args) => notifications.push(args) },
      }));
      await spawned(1);
      assert.match((await call({ action: "status" })).details.jobs[0].label, /worker @/);
      await events.session_start();
      assert.deepEqual(launches[0].proc.signals, ["SIGTERM"]);
      assert.match(notifications[0][0], /cancelled/);
      await assert.rejects(wait([h]), /Unknown/);
      launches.length = 0;
    });
    await t.test("POSIX root cancellation targets the group; nested launches inherit it", async () => {
      if (process.platform === "win32") return;
      const originalKill = process.kill;
      const originalGroup = process.env.PI_SUBAGENT_PROCESS_GROUP;
      const signals = [];
      try {
        delete process.env.PI_SUBAGENT_PROCESS_GROUP;
        const h = handle(await start()); await spawned(1);
        launches[0].proc.pid = 123456;
        process.kill = (pid, signal) => {
          signals.push([pid, signal]);
          if (signal === "SIGTERM") queueMicrotask(() => launches[0].proc.emit("close", null, signal));
          return true;
        };
        assert.equal(launches[0].options.detached, true);
        assert.equal(launches[0].options.env.PI_SUBAGENT_PROCESS_GROUP, "1");
        await call({ action: "cancel", handles: [h] });
        await wait([h]);
        assert.deepEqual(signals, [[-123456, "SIGTERM"], [-123456, "SIGKILL"]]);
        await reset();
        process.env.PI_SUBAGENT_PROCESS_GROUP = "1";
        const nested = handle(await start()); await spawned(1);
        assert.equal(launches[0].options.detached, false);
        launches[0].proc.finish(); await wait([nested]);
        await reset();
      } finally {
        process.kill = originalKill;
        if (originalGroup === undefined) delete process.env.PI_SUBAGENT_PROCESS_GROUP;
        else process.env.PI_SUBAGENT_PROCESS_GROUP = originalGroup;
      }
    });
    await t.test("streaming a synchronous parallel task does not mark it complete", async () => {
      const updates = [];
      const pending = tool.execute("parallel", { agentScope: "project", tasks: [
        { agent: "worker", task: "one" }, { agent: "worker", task: "two" },
      ] }, undefined, result => updates.push(result), ctx);
      await spawned(2);
      launches[0].proc.stdout.write(JSON.stringify({ type: "message_end", message: {
        role: "assistant", content: [{ type: "text", text: "interim" }],
      } }) + "\n");
      assert.match(updates.at(-1).content[0].text, /0\/2 done/);
      launches.forEach(launch => launch.proc.finish());
      await pending;
      launches.length = 0;
    });
    await t.test("retained handle bound requires explicit forget; settled jobs free active slots", async () => {
      const { Jobs } = await jiti.import(fileURLToPath(new URL("../jobs.ts", import.meta.url)));
      const registry = new Jobs();
      for (let i = 0; i < 128; i++) {
        const job = registry.start(async () => "ok", () => false);
        await job.done;
      }
      assert.throws(() => registry.start(async () => "ok", () => false), /128 retained/);
      registry.forget(registry.select());
      const job = registry.start(() => { throw new Error("sync exception"); }, () => false);
      await job.done;
      assert.equal(job.state, "failed");
      await registry.shutdown();
    });
    await t.test("blocking calls share capacity with async jobs and wait without oversubscription", async () => {
      const handles = [];
      for (let i = 0; i < 4; i++) handles.push(handle(await start()));
      await spawned(4);
      const blocking = call({ agent: "worker", task: "blocking", agentScope: "project" });
      await new Promise(resolve => setTimeout(resolve, 20));
      assert.equal(launches.length, 4);
      launches[0].proc.finish();
      await spawned(5);
      await assert.rejects(start(), /Worker capacity exhausted/);
      launches[4].proc.finish();
      assert.equal((await blocking).isError, undefined);
      assert.equal((await call({ action: "status" })).details.jobs.length, 4, "blocking handle auto-released");
      await reset();
    });
    await t.test("interrupting a blocking call cancels its child and releases ownership", async () => {
      const controller = new AbortController();
      const pending = call({ agent: "worker", task: "blocking", agentScope: "project" }, controller.signal);
      await spawned(1);
      controller.abort();
      assert.equal((await pending).isError, true);
      assert.deepEqual(launches[0].proc.signals, ["SIGTERM"]);
      assert.deepEqual((await call({ action: "status" })).details.jobs, []);
      await reset();
    });
    await t.test("shutdown owns blocking children and prevents queued spawns", async () => {
      const pending = call({ agentScope: "project", tasks: Array.from({ length: 8 }, () => ({ agent: "worker", task: "work" })) });
      await spawned(4);
      await events.session_shutdown();
      assert.equal((await pending).isError, true);
      assert.equal(launches.length, 4);
      assert.ok(launches.every(l => l.proc.signals.includes("SIGTERM")));
      await reset();
    });
    await t.test("cancel escalates even after TERM was delivered", async () => {
      const h = handle(await start()); await spawned(1);
      launches[0].proc.ignoreTerm = true;
      await call({ action: "cancel", handles: [h] });
      await wait([h]);
      assert.deepEqual(launches[0].proc.signals, ["SIGTERM", "SIGKILL"]);
      await reset();
    });
  } finally {
    throwSpawn = false;
    await events.session_shutdown();
    childProcess.spawn = originalSpawn;
    syncBuiltinESMExports();
    fs.rmSync(root, { recursive: true, force: true });
  }
});
