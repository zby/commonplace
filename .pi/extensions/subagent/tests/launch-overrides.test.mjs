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
// Exercise the shipped definitions, not a duplicate tools fixture.
for (const name of ["commonplace-worker", "commonplace-coordinator"]) {
  fs.copyFileSync(fileURLToPath(new URL(`../../../agents/${name}.md`, import.meta.url)),
    path.join(root, ".pi", "agents", `${name}.md`));
}
const coordinatorBody = fs.readFileSync(
  path.join(root, ".pi", "agents", "commonplace-coordinator.md"), "utf8",
).replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "").trim();
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
      for (const schema of [tool.parameters, tool.parameters.properties.tasks.items, tool.parameters.properties.chain.items]) {
        assert.ok(schema.properties.model);
        assert.equal(schema.properties.model.minLength, 1);
        assert.deepEqual(schema.properties.thinkingLevel.enum, ["off", "minimal", "low", "medium", "high", "xhigh", "max"]);
      }
    });
    await t.test("omitted fields preserve coordinator inheritance", async () => {
      const result = await launch({ agent: "inherited", task: "test" });
      assert.equal(flag(0, "--model"), "test/parent");
      assert.equal(flag(0, "--thinking"), "medium");
      assert.equal(result.details.results[0].thinkingLevel, "medium");
      assert.ok(launches[0].args.includes("--no-session"));
    });
    await t.test("coordinator can select delegation without exposing it to ordinary workers", async () => {
      for (const [agent, tools] of [
        ["commonplace-worker", "read,bash,edit,write"],
        ["commonplace-coordinator", "read,bash,edit,write,subagent"],
      ]) {
        await launch({ agent, task: "test", model: "openai/gpt-6.1-sol", thinkingLevel: "medium", cwd: root });
        assert.equal(flag(0, "--tools"), tools);
        assert.equal(flag(0, "--model"), "openai/gpt-6.1-sol");
        assert.equal(flag(0, "--thinking"), "medium");
        assert.equal(launches[0].options.cwd, root);
        assert.ok(launches[0].args.includes("--no-session"));
      }
    });
    await t.test("shipped coordinator explicitly loads the canonical contract and fails closed", () => {
      const body = coordinatorBody.replace(/\s+/g, " ");
      assert.match(body, /Before any delegation or opening a workflow, read the complete `\.pi\/APPEND_SYSTEM\.md`/);
      assert.match(body, /from the repository root of your current worktree and follow it as the canonical Pi delegation contract/);
      assert.match(body, /Do not assume it was inherited from the parent or loaded at startup/);
      assert.match(body, /If it is absent or unreadable, stop and report the exact path and read failure; do not guess the launch contract/);
      // Launch details belong in APPEND_SYSTEM.md, not a second contract here.
      assert.doesNotMatch(body, /agentScope|COMMONPLACE_WORKER_OK/);
    });
    await t.test("coordinator launch transports the full contract-loading instruction without commission help", async () => {
      const task = "Coordinate the commissioned workflow.";
      await launch({ agent: "commonplace-coordinator", task, cwd: root });
      assert.equal(launches.length, 1);
      assert.ok(flag(0, "--append-system-prompt"));
      assert.equal(launches[0].systemPrompt.trim(), coordinatorBody);
      assert.equal(launches[0].args.at(-1), `Task: ${task}`);
      assert.equal(launches[0].options.cwd, root);
    });
    await t.test("pinned model preserves original thinking default", async () => {
      await launch({ agent: "pinned", task: "test" });
      assert.equal(flag(0, "--model"), "pinned-model");
      assert.equal(flag(0, "--thinking"), undefined);
    });
    await t.test("explicit settings override agent and coordinator", async () => {
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
    await t.test("model-only override inherits coordinator effort", async () => {
      await launch({ agent: "pinned", task: "test", model: "chosen" });
      assert.equal(flag(0, "--thinking"), "medium");
    });
    for (const mode of ["tasks", "chain"]) {
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
