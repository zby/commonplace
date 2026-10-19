import assert from "node:assert/strict";
import { EventEmitter } from "node:events";
import fs from "node:fs";
import { createRequire, syncBuiltinESMExports } from "node:module";
import os from "node:os";
import path from "node:path";
import { PassThrough } from "node:stream";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

// Use the same dependencies as the installed Pi; no child agents or model calls.
const packageDir = process.env.PI_PACKAGE_DIR;
assert.ok(packageDir, "Set PI_PACKAGE_DIR to the installed pi-coding-agent directory");
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
childProcess.spawn = (command, args, options) => {
  // Capture prompt files while they exist; the extension removes them on exit.
  const promptIndex = args.indexOf("--append-system-prompt");
  const systemPrompt = promptIndex < 0 ? undefined : fs.readFileSync(args[promptIndex + 1], "utf8");
  launches.push({ command, args, options, systemPrompt });
  const proc = new EventEmitter();
  proc.stdout = new PassThrough();
  proc.stderr = new PassThrough();
  proc.kill = () => true;
  process.nextTick(() => {
    proc.stdout.write(JSON.stringify({ type: "message_end", message: {
      role: "assistant", content: [{ type: "text", text: "OK" }], stopReason: "stop",
    } }) + "\n");
    proc.emit("close", 0);
  });
  return proc;
};
syncBuiltinESMExports();

const root = fs.mkdtempSync(path.join(os.tmpdir(), "subagent-test-"));
fs.mkdirSync(path.join(root, ".pi", "agents"), { recursive: true });
for (const [name, model] of [["inherited", ""], ["pinned", "model: pinned-model\n"]]) {
  fs.writeFileSync(path.join(root, ".pi", "agents", `${name}.md`),
    `---\nname: ${name}\ndescription: Test agent\n${model}---\n`);
}
const delegatorBody = "Delegate the commissioned work.";
for (const [name, tools, body] of [
  ["worker", "read, bash, edit, write", "Do the assigned job."],
  ["delegator", "read, bash, edit, write, subagent", delegatorBody],
]) {
  fs.writeFileSync(path.join(root, ".pi", "agents", `${name}.md`),
    `---\nname: ${name}\ndescription: Test agent\ntools: ${tools}\n---\n\n${body}\n`);
}
let tool;
try {
  const extension = await jiti.import(fileURLToPath(new URL("../index.ts", import.meta.url)), { default: true });
  extension({ registerTool: registered => { tool = registered; }, on() {} });
} catch (error) {
  childProcess.spawn = originalSpawn;
  syncBuiltinESMExports();
  fs.rmSync(root, { recursive: true, force: true });
  throw error;
}
const ctx = { cwd: root, model: { provider: "test", id: "parent" }, thinkingLevel: "medium", hasUI: false };
const launch = async params => {
  launches.length = 0;
  const result = await tool.execute("test", { agentScope: "project", ...params }, undefined, undefined, ctx);
  assert.equal(result.isError, undefined);
  return result;
};
const flag = (index, name) => {
  const args = launches[index].args;
  const position = args.indexOf(name);
  return position < 0 ? undefined : args[position + 1];
};

test("launch overrides and inheritance", async t => {
  try {
    await t.test("schema exposes both overrides in every mode", () => {
      for (const schema of [tool.parameters, tool.parameters.properties.tasks.items]) {
        assert.ok(schema.properties.model);
        assert.equal(schema.properties.model.minLength, 1);
        assert.deepEqual(schema.properties.thinkingLevel.enum, ["off", "minimal", "low", "medium", "high", "xhigh", "max"]);
      }
    });
    await t.test("destination approval parameter is absent", () => {
      assert.equal(tool.parameters.properties.confirmProjectAgents, undefined);
    });
    await t.test("chain is absent and rejected rather than silently ignored", async () => {
      assert.equal(tool.parameters.properties.chain, undefined);
      await assert.rejects(launch({ agent: "inherited", task: "test", chain: [] }), /Chain mode/);
      assert.equal(launches.length, 0);
    });
    await t.test("omitted fields preserve parent inheritance", async () => {
      const result = await launch({ agent: "inherited", task: "test" });
      assert.equal(flag(0, "--model"), "test/parent");
      assert.equal(flag(0, "--thinking"), "medium");
      assert.equal(result.details.results[0].thinkingLevel, "medium");
      assert.ok(launches[0].args.includes("--no-session"));
    });
    await t.test("a definition can select delegation without exposing it to ordinary workers", async () => {
      for (const [agent, tools] of [
        ["worker", "read,bash,edit,write"],
        ["delegator", "read,bash,edit,write,subagent"],
      ]) {
        await launch({ agent, task: "test", model: "openai/gpt-6.1-sol", thinkingLevel: "medium", cwd: root });
        assert.equal(flag(0, "--tools"), tools);
        assert.equal(flag(0, "--model"), "openai/gpt-6.1-sol");
        assert.equal(flag(0, "--thinking"), "medium");
        assert.equal(launches[0].options.cwd, root);
        assert.ok(launches[0].args.includes("--no-session"));
      }
    });
    await t.test("launch transports the definition body without commission help", async () => {
      const task = "Coordinate the commissioned work.";
      await launch({ agent: "delegator", task, cwd: root });
      assert.equal(launches.length, 1);
      assert.ok(flag(0, "--append-system-prompt"));
      assert.equal(launches[0].systemPrompt.trim(), delegatorBody);
      assert.equal(launches[0].args.at(-1), `Task: ${task}`);
      assert.equal(launches[0].options.cwd, root);
    });
    await t.test("destination definitions and tools are selected without an approval gate", async () => {
      const destination = path.join(root, "destination");
      const definitions = path.join(destination, ".pi", "agents");
      fs.mkdirSync(definitions, { recursive: true });
      fs.writeFileSync(path.join(definitions, "inherited.md"), "---\nname: inherited\ndescription: Destination\ntools: [read]\n---\nDESTINATION PROMPT\n");
      await launch({ agent: "inherited", task: "test", cwd: destination });
      assert.equal(launches.length, 1);
      assert.equal(flag(0, "--tools"), "read");
      assert.match(launches[0].systemPrompt, /DESTINATION PROMPT/);
      launches.length = 0;
      const result = await tool.execute("test", { agentScope: "project", agent: "inherited", task: "test", cwd: destination }, undefined, undefined,
        { ...ctx, hasUI: true, isProjectTrusted: () => false, ui: { confirm: () => { assert.fail("No destination approval dialog"); } } });
      assert.equal(result.isError, undefined);
      assert.equal(launches.length, 1);
      assert.equal(flag(0, "--tools"), "read");
      assert.match(launches[0].systemPrompt, /DESTINATION PROMPT/);
      await launch({ tasks: [
        { agent: "inherited", task: "parent" }, { agent: "inherited", task: "child", cwd: destination },
      ] });
      const child = launches.find(l => l.options.cwd === destination);
      assert.match(child.systemPrompt, /DESTINATION PROMPT/);
      assert.equal(launches.find(l => l.options.cwd === root).systemPrompt, undefined);
    });
    await t.test("invalid tool lists fail closed without breaking unrelated definitions", async () => {
      const file = path.join(root, ".pi", "agents", "bad.md");
      for (const tools of ["[]", "''", "null", "42", "{read: true}", "[read, 42]", "'read,,bash'"]) {
        fs.writeFileSync(file, `---\nname: bad\ndescription: Invalid\ntools: ${tools}\n---\n`);
        await assert.rejects(launch({ agent: "bad", task: "test" }), /tools must be/);
        assert.equal(launches.length, 0);
        await launch({ agent: "inherited", task: "still valid" });
      }
      fs.unlinkSync(file);
    });
    await t.test("pinned model preserves original thinking default", async () => {
      await launch({ agent: "pinned", task: "test" });
      assert.equal(flag(0, "--model"), "pinned-model");
      assert.equal(flag(0, "--thinking"), undefined);
    });
    await t.test("explicit settings override agent and parent", async () => {
      const result = await launch({ agent: "pinned", task: "test", model: "chosen", thinkingLevel: "off" });
      assert.equal(flag(0, "--model"), "chosen");
      assert.equal(flag(0, "--thinking"), "off");
      assert.equal(result.details.results[0].model, "chosen");
      assert.equal(result.details.results[0].thinkingLevel, "off");
    });
    await t.test("thinking-only override keeps pinned model", async () => {
      await launch({ agent: "pinned", task: "test", thinkingLevel: "high" });
      assert.equal(flag(0, "--model"), "pinned-model");
      assert.equal(flag(0, "--thinking"), "high");
    });
    await t.test("model-only override inherits parent effort", async () => {
      await launch({ agent: "pinned", task: "test", model: "chosen" });
      assert.equal(flag(0, "--thinking"), "medium");
    });
    for (const mode of ["tasks"]) {
      await t.test(`${mode}: item overrides are independent and beat call-wide values`, async () => {
        await launch({ model: "call-model", thinkingLevel: "low", [mode]: [
          { agent: "pinned", task: "one", model: "item-model" },
          { agent: "inherited", task: "two", thinkingLevel: "off" },
        ] });
        assert.equal(flag(0, "--model"), "item-model");
        assert.equal(flag(0, "--thinking"), "low");
        assert.equal(flag(1, "--model"), "call-model");
        assert.equal(flag(1, "--thinking"), "off");
      });
    }
  } finally {
    childProcess.spawn = originalSpawn;
    syncBuiltinESMExports();
    fs.rmSync(root, { recursive: true, force: true });
  }
});
