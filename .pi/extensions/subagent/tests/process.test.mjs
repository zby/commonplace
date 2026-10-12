import assert from "node:assert/strict";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

// Real Node subprocesses only: never launches Pi or makes model calls.
const requirePi = createRequire(path.join(process.env.PI_PACKAGE_DIR, "package.json"));
const { createJiti } = requirePi("jiti");
const jiti = createJiti(import.meta.url);
const { runProcess } = await jiti.import(fileURLToPath(new URL("../process.ts", import.meta.url)));
const { Jobs } = await jiti.import(fileURLToPath(new URL("../jobs.ts", import.meta.url)));

function child(source, signal) {
  let ready;
  const started = new Promise(resolve => { ready = resolve; });
  let stdout = "", stderr = "";
  const done = runProcess(process.execPath, ["-e", source], process.cwd(), signal, text => {
    stdout += text;
    if (stdout.includes("READY\n")) ready();
  }, text => { stderr += text; });
  return { started, done, stdout: () => stdout, stderr: () => stderr };
}

const idle = "console.log('READY'); setInterval(() => {}, 1000);";
test("real child cancellation and session ownership", { timeout: 20000 }, async t => {
  const inherited = process.env.PI_SUBAGENT_PROCESS_GROUP;
  delete process.env.PI_SUBAGENT_PROCESS_GROUP;
  try {
    await t.test("normal exit drains output and preserves exit status", async () => {
      const c = child("console.log('READY'); console.error('diagnostic'); process.exitCode = 7;");
      const result = await c.done;
      assert.equal(result.exitCode, 7);
      assert.equal(result.aborted, false);
      assert.match(c.stdout(), /READY/);
      assert.match(c.stderr(), /diagnostic/);
    });
    await t.test("blocking job shutdown waits for real process close", async () => {
      const jobs = new Jobs();
      let c;
      const pending = jobs.execute(signal => { c = child(idle, signal); return c.done; }, r => r.exitCode !== 0, "real child");
      // execute reserves synchronously, then starts in a microtask.
      await Promise.resolve();
      await c.started;
      await jobs.shutdown();
      assert.equal((await pending).aborted, true);
      assert.deepEqual(jobs.select(), []);
    });
    await t.test("TERM-resistant child escalates to KILL", { skip: process.platform === "win32" }, async () => {
      const controller = new AbortController();
      const c = child("process.on('SIGTERM', () => {});" + idle, controller.signal);
      try {
        await c.started;
        controller.abort();
        assert.equal((await c.done).aborted, true);
        assert.match(c.stderr(), /SIGKILL/);
      } finally { controller.abort(); await c.done; }
    });
    await t.test("root cancellation terminates a real descendant in its group", { skip: process.platform !== "linux" }, async () => {
      const controller = new AbortController();
      const c = child(`const { spawn } = require('node:child_process');
        const grandchild = spawn(process.execPath, ['-e', ${JSON.stringify("process.on('SIGTERM', () => {});" + idle)}], {stdio: ['ignore', 'pipe', 'inherit']});
        grandchild.stdout.on('data', () => { console.log('PID=' + grandchild.pid); console.log('READY'); });
        setInterval(() => {}, 1000);`, controller.signal);
      let pid;
      try {
        await c.started;
        pid = Number(c.stdout().match(/PID=(\d+)/)[1]);
        controller.abort();
        assert.equal((await c.done).aborted, true);
        // A killed orphan may briefly remain a zombie until the OS reaps it.
        const stopped = () => {
          try { return /\) [ZX] /.test(fs.readFileSync(`/proc/${pid}/stat`, 'utf8')); }
          catch (e) { if (e.code === 'ENOENT') return true; throw e; }
        };
        for (let i = 0; i < 100 && !stopped(); i++) await new Promise(resolve => setTimeout(resolve, 10));
        assert.equal(stopped(), true, 'descendant must no longer execute');
      } finally {
        controller.abort();
        if (pid) try { process.kill(pid, 'SIGKILL'); } catch (e) { if (e.code !== 'ESRCH') throw e; }
        await c.done;
      }
    });
  } finally {
    if (inherited === undefined) delete process.env.PI_SUBAGENT_PROCESS_GROUP;
    else process.env.PI_SUBAGENT_PROCESS_GROUP = inherited;
  }
});
