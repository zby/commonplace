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
const jiti = createJiti(import.meta.url, { alias: aliases, moduleCache: false });
const childProcess = createRequire(import.meta.url)("node:child_process");
const originalSpawn = childProcess.spawn;
const launches = [];
childProcess.spawn = (command, args, options) => {
  launches.push({ command, args, options });
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
let tool;
try {
  const extension = await jiti.import(fileURLToPath(new URL("../index.ts", import.meta.url)), { default: true });
  extension({ registerTool: registered => { tool = registered; } });
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
