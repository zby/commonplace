import assert from "node:assert/strict";
import { createRequire } from "node:module";
import path from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const requirePi = createRequire(path.join(process.env.PI_PACKAGE_DIR, "package.json"));
const { createJiti } = requirePi("jiti");
const { readLimits, grant } = await createJiti(import.meta.url).import(fileURLToPath(new URL("../budgets.ts", import.meta.url)));

test("budget validation and static partitions", () => {
  assert.deepEqual(readLimits({}), { depth: null, workers: 4 });
  assert.deepEqual(grant(readLimits({}), {}), { maxDepth: 0, maxWorkers: 0 });
  for (const value of ["", "-1", "1.5", "NaN", "Infinity", " 1", "1e2", "9007199254740992"]) {
    const limits = readLimits({ PI_SUBAGENT_DEPTH: value, PI_SUBAGENT_WORKERS: "1" });
    assert.ok(limits.error, value);
    assert.throws(() => grant(limits, {}), /invalid inherited budget/);
  }
  assert.ok(readLimits({ PI_SUBAGENT_DEPTH: "1", PI_SUBAGENT_WORKERS: "5" }).error);
  assert.ok(readLimits({ PI_SUBAGENT_DEPTH: "1" }).error);
  for (const value of [-1, 1.5, Infinity, NaN, "1", Number.MAX_SAFE_INTEGER + 1]) {
    for (const name of ["maxDepth", "maxWorkers"]) assert.throws(() => grant(readLimits({}), { [name]: value }), /safe integer/);
  }
  for (let depth = 1; depth < 5; depth++) for (let workers = 1; workers <= 4; workers++) {
    const granted = grant({ depth, workers }, { maxDepth: 100, maxWorkers: 100 });
    assert.equal(granted.maxDepth, depth - 1);
    assert.equal(1 + granted.maxWorkers, workers, "a child and its entire partition fit inside the caller's pool");
  }
});
