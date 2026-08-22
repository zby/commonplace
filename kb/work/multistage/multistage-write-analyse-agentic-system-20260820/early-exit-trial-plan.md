# Early-exit trial plan

Closes the coverage gap recorded in `trial-evaluation.md`: the first four trials all returned both
lenses `applicable`, so the `inapplicable` branch, the early-exit record shape, and the
prevented-conclusion discipline on a non-run were never exercised.

## Target

**`sequentialthinking` MCP server** — the subtree `src/sequentialthinking` of
`github.com/modelcontextprotocol/servers`.

- Local checkout: `/home/zby/llm/servers/src/sequentialthinking/` (clean tree, no network needed)
- Pinned commit: `2ecb382a02d7921511180dfbadcef24eb66a052f`
- Whole system is roughly 200 lines: `index.ts`, `README.md`, `package.json`

## Why this target

Selected from a scouting pass over the local pool. `related-systems/` turned out useless for this
purpose by construction — it is a 178-entry agent-*memory* corpus, so persistence is the selection
criterion and the memory trigger fires on essentially every entry. The trigger-poor entries there are
documents rather than systems, which would exercise the step-1 out-of-scope exit instead.

`sequentialthinking` fails the memory trigger for a *structural* reason that can be cited in three
lines, while the epistemic lens survives:

- **Memory expected `inapplicable`.** State exists but provably does not return.
  `index.ts:26-27` holds `thoughtHistory` and `branches` as plain instance fields; the tool response
  (`index.ts:106-117`) returns only `thoughtNumber`, `totalThoughts`, `nextThoughtNeeded`, the branch
  *keys*, and a history *length* — accumulated thought content is never read back. Prior thoughts go
  to stderr (`index.ts:104`), out of the loop entirely. No filesystem, database, or network use
  anywhere. This is ordinary current-run state, which the trigger explicitly excludes.
- **Epistemic expected `applicable`, and instructively so.** The shipped tool description claims
  hypothesis generation and verification (`index.ts:154-155, 166-167, 184-187`; `README.md:12`),
  while the implementation performs only shape validation (`validateThoughtData`, `index.ts:29-56`) —
  which is not truth checking. The entire epistemic route is therefore doctrine-only, which
  stress-tests the architectural-status distinction rather than merely repeating the earlier trials.
- **In scope.** A reasoning scaffold exposed as a tool into an agent's loop is an agent
  operating-layer component, not a bare utility.

Small enough to analyse exhaustively, so the result should carry no "unassessed route families"
hedging — which makes any `absent` conclusion in it unusually well-grounded.

## Sequencing

Run against the **post-fix candidate**, not the version the first four trials used. Several of the
twelve fixes bear directly on this run: the absence namespace (an `inapplicable` memory disposition
is itself an evidenced absence), the scope-test restructure (this target sits nearer the
tool-versus-system line than any prior trial), and the behavioral-authority/`horizon`
self-containment. Testing the artifact that would actually be promoted also gives a partial
re-validation of the fixes.

## Backups

- `time` MCP server (same repo/commit, `/home/zby/llm/servers/src/time/`) — cleaner memory verdict,
  muddier epistemic one, and closer to the out-of-scope line.
- If a **both**-lens exit is wanted later, fetch `sparfenyuk/mcp-proxy` (a stdio↔SSE transport
  bridge: pure passthrough, arguably in scope as agent transport infrastructure) rather than settling
  for a context-preparation CLI such as `simonw/files-to-prompt`, which would exit at step 1 before
  either lens is reached.
