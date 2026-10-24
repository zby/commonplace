import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const packageDir = process.env.PI_PACKAGE_DIR;
assert.ok(packageDir, "Set PI_PACKAGE_DIR");
const recorder = fileURLToPath(new URL("../session-info.ts", import.meta.url));

test("native Pi selects storage and reports it without any model request", { timeout: 60000 }, () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "pi-native-sessions-"));
  const agentDir = path.join(root, "agent");
  const projects = [path.join(root, "project"), path.join(root, "worktree")];
  for (const cwd of projects) fs.mkdirSync(cwd);
  const run = (cwd, extra = {}) => {
    const env = { ...process.env, PI_CODING_AGENT_DIR: agentDir, PI_OFFLINE: "1" };
    delete env.PI_CODING_AGENT_SESSION_DIR;
    Object.assign(env, extra);
    const result = spawnSync(process.execPath, [path.join(packageDir, "dist/cli.js"),
      "--mode", "json", "-p", "--no-extensions", "--extension", recorder,
      "--no-skills", "--no-tools", "--offline"], { cwd, env, input: "", encoding: "utf8", timeout: 15000 });
    assert.equal(result.status, 0, result.stderr);
    const info = result.stderr.split("\n").find(line => line.startsWith("PI_SUBAGENT_SESSION "));
    assert.ok(info, result.stderr);
    const reference = JSON.parse(info.slice("PI_SUBAGENT_SESSION ".length));
    const header = JSON.parse(result.stdout.trim());
    assert.equal(header.type, "session");
    assert.equal(reference.sessionId, header.id);
    assert.equal(reference.cwd, cwd);
    return reference;
  };
  try {
    const first = run(projects[0]);
    const second = run(projects[0]);
    const worktree = run(projects[1]);
    assert.notEqual(first.sessionId, second.sessionId);
    assert.equal(path.dirname(first.sessionFile), path.dirname(second.sessionFile));
    assert.notEqual(path.dirname(first.sessionFile), path.dirname(worktree.sessionFile));
    assert.ok(first.sessionFile.startsWith(path.join(agentDir, "sessions") + path.sep));
    fs.mkdirSync(path.join(projects[0], ".pi"));
    const configured = path.join(root, "configured");
    fs.writeFileSync(path.join(projects[0], ".pi/settings.json"), JSON.stringify({ sessionDir: configured }));
    assert.equal(path.dirname(run(projects[0]).sessionFile), configured);
    const overridden = path.join(root, "override");
    assert.equal(path.dirname(run(projects[0], { PI_CODING_AGENT_SESSION_DIR: overridden }).sessionFile), overridden);
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});
