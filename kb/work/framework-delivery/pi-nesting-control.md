# pi worker nesting: checkout verification

Dated evidence for [sub-agent requirements](./sub-agent-requirements.md) S8/S9.
This records the 2026-10-26 implementation; the remaining acceptance is loading
the INSTALL.md user-level copy in an installed project.

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
