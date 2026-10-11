# Letta analysis and trace audit

## Judgment and identity

Trust this run as a supported **blocked boundary result**, not as an analysis
of Letta's runtime or memory. The frozen repository is a landing page; the
worker did not substitute the linked implementation or historical branch.
No substantive correction to the boundary is indicated by this audit.
The coordinator's final answer correctly distinguished local completion from
publication, but did not explain the practical reason for the block.

```yaml
run-id: AAS-2026-10-11-letta-d460b458ddad-01
method-commit: 6ff7c828e94dd66abdf5af00c89db6420bc6a1ad
source-revision: 5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a
audit-date: 2026-10-11
worker-profile: pi-sol
worker-runtime: {harness: pi, model: openai/gpt-6.1-sol, reasoning-effort: medium}
reporter-profile: {harness: pi, model: openai/gpt-6-astra, reasoning-effort: medium}
```

Reporter identity comes from `PI_PROVIDER`, `PI_MODEL` and
`PI_REASONING_LEVEL`. The session changed model before this audit. This is
an audit in the original coordinator session, not an independent blind review.

## Evidence and scope

Local locators, not alternative run identities:

- `W`: `/home/zby/llm/commonplace/.commonplace/worktrees/letta-d460b458ddad`.
- `R`: `W/kb/agentic-system-analyses/state/AAS-2026-10-11-letta-d460b458ddad-01`.
- `S`: `W/related-systems/letta-ai--letta`.
- `T`: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T06-44-36-040Z_01a129b4-c847-711e-8a12-57e9467dd961.jsonl`.

`T L<n>` names a one-based JSONL line. `B m<n>` names a zero-based message
in `T L23.message.details.results[0].messages`, the boundary worker transcript.
All 42 embedded messages were covered for tool actions and results; this audit
does not reproduce private reasoning. There were 23 tool results: 14 reads,
six shell commands, two writes and one edit. The original handout workspace
is no longer present; its prompt, input reads and candidate edits survive in
this embedded transcript. Separate child-session archives were not sought.

Inspected evidence includes both local artifact members, all six attempt
records, both judgments, acquisition metadata, the publication receipt, the
worker prompt and contracts captured in the trace, coordinator actions through
the final report, the frozen README and recursive Git tree, and the local
publication handler's non-complete branch. No target execution or new network
acquisition was performed. Prior audits below supply comparison evidence;
their underlying traces were not re-audited here.

## Findings

### L1 — Supported stop; no source substitution

`S/README.md:5` identifies `letta-ai/letta-code` as the current source, while
its Historical source section locates the retired V1 server on `archive`.
The audit's `git ls-tree -r --name-only HEAD` confirmed twelve tracked files:
three under `.github/`, plus `AGENTS.md`, `AI_POLICY.md`, `CITATION.cff`,
`CONTRIBUTING.md`, `LICENSE`, `PRIVACY.md`, `README.md`, `SECURITY.md` and
`TERMS.md`. HEAD matched the source revision above, and source status was clean.
The worker inspected the issue workflow in full (`B m23`); it performs issue
compliance checks and GitHub API actions, not model-dependent agent execution.

This independently supports the absence of the advertised implementation
from this pin. `R/artifact/boundary.md` properly limits its claim to that
revision and makes no runtime or effectiveness finding. Its source register
labels the workflow as repository administration rather than agent behavior.
The source's `AGENTS.md` contains strong instructions against historical use
(`B m21`), but the stop does not need those instructions as authority: the
tracked tree and Commonplace's fixed-source contract independently suffice.
The trace shows neither an archive checkout nor a redirected acquisition.

Disposition: retain the boundary result. A current implementation analysis
would need a separate commission naming the implementation repository; a
historical analysis would need an explicit historical revision and scope.
Neither was launched by this audit.

### L2 — Deterministic quotation repair succeeded; failures were visible

The first validator invocation rejected both quote attributions (`B m31–32`):
`SRC-1,` followed by a bare backticked path did not match the accepted syntax.
The worker searched the parser, read its relevant implementation, added the
frozen revision to both attributions, and reran validation successfully
(`B m33–40`). No claim was narrowed or withdrawn, so the rule requiring a
scratch record for narrowed or withdrawn findings was not triggered.

An earlier guessed `find letta` path also failed (`B m14–15`). The worker
recovered by reading the README and inventorying the whole tracked tree
(`B m16–19`), rather than treating the missing guessed directory as sufficient
proof of an absent implementation.

Both failures reached the harness as `isError: true` with exit code 1. The
successful validation exposed exit code 0. This is a counterexample to masked
shell failures reported in the other audits, not evidence that masking is
fixed generally. The worker's final one-line file response followed its prompt;
it was not required to narrate repaired failures there.

### L3 — Coordinator publication instructions were loaded late

The coordinator read `publish-analysis.md` at `T L28–29`, after the final
advance at `L24–25` had completed the publication job. The skill requires that
read before publication. The local-only branch meant no retained publication
occurred, so this is a prerequisite-order deviation without demonstrated
public artifact damage. It still shows that waiting for an explicit
publication hand-out is unsafe: advance can reach the code job automatically.

The worker profile was read before preparation (`T L10–11`), and the actual
launch explicitly selected `gpt-6.1-sol` and medium effort (`L22`). Worker
runtime identity agreed (`B m12–13`, attempt record). No profile mismatch or
worker-isolation failure was observed. The dirty-origin stop was also respected:
the coordinator waited for permission before using `--allow-dirty-origin`
(`T L13–17`).

### L4 — Correct status report, incomplete operator explanation

`T L30` reports blocked local completion and includes the inspect JSON
unchanged, but never states that the supplied repository is now a landing
page. The generated overview similarly directs the reader to the boundary
rather than carrying the stopping reason. The result is accurate status with
poor guidance about what the operator must decide next.

The coordinator was explicitly forbidden to inspect worker outputs while
driving the run. Its omission should therefore not be classified as a simple
failure to read more. The reporting surface exposed the disposition but not
its reason. Whether to expose a bounded stopping reason through inspection is
a design question for separate consideration, not an adopted change here.

### L5 — Local completion and exact member bytes agree

`R/state/attempts/000006-publish.json` points to receipt version
`3ed71dd9c6a601350e2abeabf84828532256f8e702f22a1762d0e681f6bba710`, which
contains `{"published": false}`. The method's
`src/commonplace/lib/agentic_analysis/publication.py:253–278` returns this
receipt for non-complete artifacts without retained or archive output.
Only the acquisition effect journal is present. This agrees with the
original inspection's `completion: local` and `result-disposition: blocked`.

Independent byte checks matched each local artifact to its accepted version:

| Member | SHA-256 |
|---|---|
| boundary | `ab74780436ff63ceb7ac39599a369877cd0cc7ec513a2fc76702451dddbacc33` |
| overview | `4f6fef2eaed69ba2f9d52f2a7b920751400e3a770c1fb9d496a537ffc22942e1` |

Both recorded judgments accepted their subjects without findings or overrides.
No semantic verifier ran: the workflow ended at the boundary. These checks
establish local byte correspondence and a consistent no-publication record,
not a historical filesystem audit of every retained destination.

## Timing and cost comparison

Coordinator timestamps in `T` give the following intervals:

| Interval | Elapsed time | Boundary |
|---|---:|---|
| Authorized retry through completion-producing advance | 177.145 s | L16 to L25; includes preparation, acquisition, worker and coordinator gaps |
| Acquisition advance | 14.412 s | L20 to L21; includes engine work, not just network transfer |
| One boundary worker call | 136.303 s | L22 to L23; launch-to-return envelope |
| Waiting for dirty-origin authorization | 2,210.645 s | L14 to L15; operator latency, not compute |

The sole worker's embedded timestamps span about 129.9 seconds from its system
message to final message. There is no worker overlap. The 136.3-second call
envelope includes launch/return overhead; neither interval is a provider-billed
compute measure. The failed-validator call through successful-validator result
spans about 35.2 seconds (`B m31–40`), including diagnosis and repair, not just
validator runtime.

Harness-reported worker usage: 17 model turns, 46,281 input tokens, 3,594 output
tokens, 230,272 cache-read tokens and 0.1515292 reported cost units. These exclude
coordinator, diagnostic, preparation and audit usage and are not an invoice.

For comparison, the [Graphiti 85a21a06d35c audit](./graphiti-85a21a06d35c-analysis-and-trace-audit.md#coverage-and-cost)
reports about 38½ minutes from preparation to publication-producing advance,
ten workers, 264 turns and cost 3.9385776. The
[Napkin audit](./napkin-analysis-and-trace-audit.md) reports 13 workers,
305 turns, cost 4.1360508 and 2,420.02 summed worker-seconds, explicitly not
wall time because workers overlapped. Both use the same method commit and
`pi-sol` profile as Letta. Their scope is full analysis with downstream
verification, unlike this single-boundary stop. Graphiti and Napkin permit
parallel analyst work; this run had only one worker. These differences prevent
speedup or performance-trend claims. The clearest cost driver here is avoided
downstream work after a valid early stop. Counting the operator wait as model
latency would invert that interpretation.

## Cross-run interpretation and disposition

| Mechanism | Evidence across distinct runs | Present disposition |
|---|---|---|
| Quotation-attribution repair | L2; Graphiti 85a21a06d35c T3; Napkin Recovered failures | Recurring repair cost at the same method/profile, with successful validation safeguards. Syntax ambiguity and variable model compliance remain plausible; do not infer a general analytical defect. |
| Late coordinator prerequisite | L3; Graphiti 85a21a06d35c T1 | Recurring ordering error, but Letta had no retained publication. Apply the existing prerequisite before advance; no extra gate adopted. |
| Masked command failures | Letta L2 exposes both failures correctly; Graphiti and Napkin reports contain masked failures | Counterexample retained. Six Letta shell calls are too few, and too narrow, to estimate reliability. |
| Blocked reason absent from operator report | L4 only | Accumulate evidence; do not generalize from one blocked case. |

A bounded future comparison could test whether a valid attribution example
reduces repair time without weakening quotation checks. Its benefit would be
fewer diagnosis reads; its costs would be prompt length and evaluation work.
No reduction in repair frequency, or worse grounding, would count against it.
For the reporting gap, exposing a reason would help the next source-selection
decision but adds a field and risks flattening nuanced limits; other blocked
runs are needed before recommending that change.

No method, retained analysis or run state was edited. No integration, rerun,
source migration or worktree disposal was performed. The worktree and session
trace remain necessary evidence. The practical next decision belongs to the
operator: analyse the redirected current implementation, specify a historical
revision, or keep this supported stop as the final result.
