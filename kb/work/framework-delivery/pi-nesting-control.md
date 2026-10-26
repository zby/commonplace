# Bounded nesting for the pi subagent extension

Analysis written 2026-10-26 for a pi session that will implement it. The
operator's direction: replace the bans on worker nesting with a control, and do
it in this checkout's `.pi/extensions/subagent` first. Requirements S8 and S9 in
[sub-agent-requirements.md](./sub-agent-requirements.md) state the target.

## What the extension does today

Read from `index.ts`, `launcher.ts`, `jobs.ts`, `process.ts`, `sessions.ts`
at commit `d57f5c824`.

- **Depth.** Nothing limits it. A child is a separate `pi --mode json -p`
  process that inherits the parent's environment and loads the same user and
  (under trust) project extensions, so it has `subagent` unless its agent
  definition's `tools` list leaves it out. `commonplace-worker` leaves it out;
  that is the ban. The README says "there is no explicit nesting limit".
- **Capacity.** `Jobs` allows four active jobs and 128 retained handles per
  extension instance, so per session. A child that has `subagent` owns a
  separate pool of four; a tree can run 4 + 4·4 + … workers. Blocking calls
  queue on the local pool; async `start` rejects when it is full.
- **Tree awareness that exists.** `process.ts` puts nested workers in the root
  coordinator's process group through `PI_SUBAGENT_PROCESS_GROUP`, so cancel
  reaches descendants. This is the precedent for passing control down the
  tree by environment variable.
- **Audit.** Each execution writes `execution.json`, `events.jsonl` and
  `stderr.log` under `<child session file>.subagent/<uuid>/`. The metadata
  names the parent process pid but not the parent session, so the tree can be
  walked downward from tool results but not upward from a child's record.

## What to build

1. **Depth budget per launch.** A `maxDepth` field on a single call and on each
   parallel task: how many further levels the child may delegate. Default 0.
   Pass it to the child as an environment variable (`PI_SUBAGENT_DEPTH`, name
   open) on spawn; the child's extension reads it at load. A session with no
   variable is a root and has no limit of its own. A launch requires the
   caller's remaining depth to be above 0, and the child's budget is capped at
   the caller's remaining depth minus one. Resumed sessions take the budget
   from the resuming call, not from the recorded one.
2. **Refusal at zero.** Keep registering the tool, but refuse every launch with
   a clear message when the remaining depth is 0, and state the remaining
   depth in the tool description so the model does not try. Registering rather
   than hiding keeps the attempt in the audit. `commonplace-worker` can then
   list `subagent` again; its prose rule becomes the default budget.
3. **Capacity as a budget, not a shared counter.** A `maxWorkers` field beside
   `maxDepth`: slots the child may use, carved from the caller's own four. The
   caller counts the child's job plus its reserved slots against its pool while
   the child runs, and passes the number down the same way. Default 0, which
   with depth 0 changes nothing. This is static partitioning: deterministic,
   no cross-process locks, testable with the existing mocks. The cost is idle
   reserved slots; a shared slot directory under the root session's audit
   directory with pid-checked locks would avoid that, and is the alternative if
   partitioning proves too tight. Choose partitioning first.
4. **Lineage in the audit.** Record the parent's session id and file in the
   child's `execution.json` (the parent knows its own from the session manager)
   and in the result details, so a tree is walkable upward as well as downward.
   Include the granted `maxDepth` and `maxWorkers`.
5. **Tests.** In `launch-overrides`: the spawn environment carries the budget
   variables, decremented and capped. In `async`: a call at depth 0 is refused;
   a child's reserved slots count against the parent's pool and are released
   when the child ends. A real-process test with a harmless Node child that
   prints its environment, as `process.test.mjs` does. Run with
   `PI_PACKAGE_DIR=… node --test .pi/extensions/subagent/tests/*.test.mjs`.
6. **Docs.** `.pi/README.md` Limits and Launch configuration sections, the tool
   description string, and `.pi/agents/commonplace-worker.md`. Afterwards,
   update the pi column of S8 and S9 in the requirements file.

Out of scope here: changing the skills' handoffs to state budgets, and the
other harnesses. `cp-skill-health-check` Step 3 may later read the depth
variable as the exposed remaining depth it now reports as unknown.

## Prompt for the pi session

```text
Implement bounded nesting in .pi/extensions/subagent as analysed in
kb/work/framework-delivery/pi-nesting-control.md. Read that file, then the
extension's six source files and its tests, and .pi/README.md, before
changing anything. Build items 1–6 in that order; choose the variable names
and keep the partitioning design for capacity. Run the extension tests with
the installed pi package, then exercise it live: from this checkout launch
commonplace-worker with maxDepth 1 and have it launch one child that returns
a token; then launch it with the default budget and confirm the nested launch
is refused with the message. Use /reload after editing. Commit the extension,
its tests and docs in one commit with trailers
"Workshop: kb/work/framework-delivery" and "Model: <your model id>"; stage
explicit files. Report what the live runs showed and anything in the analysis
that turned out wrong.
```

## Implementation and verification

Implemented in this checkout on 2026-10-26. The environment variables are
`PI_SUBAGENT_DEPTH` and `PI_SUBAGENT_WORKERS`. Both budgets default to zero for
each launch, including resume. The child receives at most the caller's depth
minus one and its worker capacity minus one. Root capacity is four worker
slots; the coordinator itself is not counted. Each job reserves one slot plus
its granted child pool until execution settles. A reservation is not reduced
because siblings are busy: blocking calls wait; async starts reject.

The tool remains registered at depth zero. Its description exposes its limits,
and launch attempts fail before spawning. Invalid or incomplete inherited
budgets fail closed. Control operations remain available. `execution.json` and
result details retain the parent session ID/file and both granted budgets.
The generic worker now includes `subagent`; its runtime budgets replace its
nesting prohibition. Skills' handoffs and other harnesses are unchanged.

Verification passed: 52 extension tests, including the real Node environment
probe and process cancellation tests; 84 general tests; Ruff; and deterministic
validation of both edited workshop documents. The extension tests also cover
weighted capacity through success, failure and cancellation, capped inherited
grants, invalid budgets, default-zero resume grants and parent lineage. This
was not a full repository test run or a live concurrency stress test.

The live probes used a fresh Pi 1.3.0 RPC coordinator in this checkout, with
`openai/gpt-6.1-sol` and requested low thinking. Before either probe, a probe-only extension
command invoked `ctx.reload()`, the runtime reload action. This did not reload
the implementing conversation's attached tool schema; that still requires an
operator `/reload` with no jobs active.

- With `maxDepth: 1, maxWorkers: 1`, the worker launched exactly one leaf. The
  leaf returned `NESTING_LEAF_20261026` without tools. Its granted budgets were
  zero, and both parent session links matched the actual native sessions.
- With both budgets omitted, the worker attempted exactly one nested tool call.
  That call was an error with `Subagent launch refused: remaining depth is 0`.
  The worker then reported the refusal successfully; no leaf was launched.
- Raw tool events and audit metadata, not just the model's reports, establish
  these outcomes. No extra tools were used, and all worker ownership locks
  were released.

The native root session is
`~/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-26T08-49-32-713Z_01a17766-9028-72cd-a2da-8370cd8fcd96.jsonl`.
Its `.nesting-probe/` sidecar retains `events.jsonl`, `stderr.log`, `run.json`,
`driver.mjs`, `reload.ts` and `acceptance.json`. The last file records the child
session/execution paths, lineage checks and source SHA256 values for the uncommitted implementation
used in the probes, on base `5b02c4720c833296b969249a9e2c755b9dcbbf00`.
These are local operational records, not installed-project delivery acceptance.

Corrections to the analysis and proposed probe:

- Depth alone does not permit the positive probe. Because `maxWorkers` defaults
  to zero, that probe also needs `maxWorkers: 1`.
- The existing process-group control places descendants in the first worker's
  group for that branch, not in the root coordinator's own process group.
- The prompt's six-file source count was stale. The extension now has eight
  TypeScript source files, including the new `budgets.ts`.
