# Napkin analysis and trace audit

## Identity and status

Retained on 2026-10-11 from the audit in the commissioning conversation. This
working report consolidates the returned findings and trace anchors; it is not
a new audit or a verbatim session transcript. Severity and recommendations are
the auditors' judgments, not adopted method decisions.

```yaml
run-id: AAS-2026-10-10-napkin-b831630d0978-01
method-commit: 6ff7c828e94dd66abdf5af00c89db6420bc6a1ad
source-revision: 7582d6a46f5a11995956e60a59c41a5b242109f1
worker-profile: pi-sol
audit-date: 2026-10-11
```

Local worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/napkin-b831630d0978`.
Local session trace:
`/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-10T22-10-09-558Z_01a127dd-cc16-745a-b8d3-80ae1386ab9d.jsonl`.
Original worker messages are embedded in subagent tool-result
`details.results[].messages` arrays, not separate worker session files.

Path abbreviations below are relative to that worktree:

- `A/`: `kb/agentic-system-analyses/retained/napkin/`.
- `S/`: `related-systems/Michaelliv--napkin/`.
- Attempt IDs refer to this run's `state/handouts/` directories.

## Outcome and limits

The central characterization survived the audit: file-backed retention,
caller-requested retrieval, instruction-mediated curation, and no demonstrated
learning benefit. Three medium-severity gaps and three narrower qualifications
were identified. No high-severity finding overturned that account.

Two independent reviewers inspected correctness against the frozen source;
the coordinator spot-checked principal findings. A separate reviewer inspected
all 13 original workers' embedded traces. This was static inspection, not target
or benchmark execution. Publication-byte integrity was not independently
audited. No analysis, method, run state, or integration was changed.

The original audit recommended a corrected run before integration. That remains
a local recommendation, not an authorized run or evidence that a general method
change is needed. All findings below come from one run.

## Correctness findings

### N1 — Medium: Distillation instructions conflict with path semantics

The skill's creation example at `S/skills/distill/SKILL.md:86` supplies a title
and `--path "<folder>"`. But `S/src/core/crud.ts:46–53` treats the path as the
complete target filename and ignores the title when a path is supplied.
A title of `Connection Pooling` and path of `guides` targets `guides.md`, not
`guides/Connection Pooling.md`. CLI forwarding is at `S/src/main.ts:230–241`.

The skilled retention account in `A/runtime.md:35,107` and
`A/synthesis.md:16–18` omits this constraint. Literal adherence is insufficient;
the agent must correct the path. A related basename rewrite example at
`S/skills/distill/SKILL.md:79–80` can target a root-level file instead of an
existing nested note because creation does not use read-style resolution.
No actual distillation failure was executed or observed.

### N2 — Medium: Saved files inherit a consumer established only for in-memory results

`A/memory-profile.md:613–624` assigns wired knowledge authority at benchmark
aggregation/reporting to the retained benchmark-results object.
`A/memory.md:180` identifies JSONL/JSON files, while `A/epistemic.md:307`
describes aggregation as later read-back.

The inspected drivers add result objects to an array and separately save them:
`S/bench/longmemeval-eval.ts:628–632` and
`S/bench/locomo-eval.ts:439–445`. Aggregation consumes `allResults`, not a reload
of those files (`661–694` and `454–495`, respectively). The analysis record
contract excludes ordinary current-run state from read-back.

Separate storage from current-run aggregation. Retained-file consumption
remains unresolved unless a concrete reload path is identified. This does not
establish that no external consumer exists.

### N3 — Medium: Documented automatic delivery is treated as wholly indeterminate

`A/memory-profile.md:915–975` withholds a positive automatic-delivery finding;
`A/profile-verification.md:24–25` endorses it. Yet `S/docs/distill.md:11–24`
describes a timer, a new-entry check, and prompt assembly from `NAPKIN.md` and
templates. Lines `44,75,79–82` describe background operation, template selection,
and supplying that retained context to the model.

This supports a documented claim of automatic delivery, not implementation or
deployment verification. Missing implementation should not erase the claimed
mechanism. Add the source facts to the underlying records before changing the
profile; the profile should not invent facts absent from those records.

### N4 — Low: Search withdrawal needs a default-search qualification

`A/memory.md:75,310`, `A/synthesis.md:18`, and
`A/memory-profile.md:808–819` describe withdrawal of soft-deleted content from
ordinary search, with explicit reads remaining possible. Folder-scoped search
can also discover deleted Markdown files: `S/src/core/search.ts:53,234` passes
the search folder into enumeration, while `S/src/utils/files.ts:28–54` skips
encountered hidden directories but not a directly selected starting folder.

Thus `--path .trash` can search deleted notes. The supported statement is
withdrawal from default vault-wide discovery, not all search. The analysis
already rejects secure-deletion guarantees; this is a missing condition.

### N5 — Low: Empty context creation is conditional

`A/runtime.md:18` says discovery creates an empty `NAPKIN.md`.
`S/src/utils/vault.ts:91–94` writes it only if absent. Existing populated context
is preserved. The broader finding that discovery can mutate state still holds.

### N6 — Low: Benchmark averages exclude failed questions

`A/epistemic.md:82` says error/null results withhold measurement but does not
explain the changed denominator. Only non-null results enter `allResults`;
means and confidence intervals use those surviving results:
`S/bench/longmemeval-eval.ts:628–632,661–694` and
`S/bench/locomo-eval.ts:439–445,483–495`.

These are successful-run-conditional metrics. Correlation between failure and
difficulty could make aggregates optimistic. Whether any published score was
affected is unknown; the analysis already withholds verification of headline
accuracy.

## Trace findings

Trace anchors use 1-based JSONL line numbers (`L`) and 0-based indices in each
worker's embedded messages array (`m`). A parallel result number distinguishes
the two workers on L26. These locators refer to the session file above.

### T1 — A substantive analytical error was caught and repaired

The initial `000008-epistemic` treated the auxiliary exposure-measurement script
as an operative evaluation route despite an incompatible corpus-loader call.

- `000014-reconciliation`, L30 m40: retained the conflict.
- `000017-report-verification`, L34 m63: made correction a publication blocker.
- `000019-epistemic`, L38 m41: made nine coordinated replacements.
- `000026-report-verification`, L46 m67: independently accepted the repair.

This is successful semantic review after content validation, not an outstanding
error. The incompatibility was established statically, not by executing the
script. It should count as evidence that the correction loop worked, alongside
its cost.

### T2 — Shell success masked a failed operation

`000005-runtime`, L22 m16–17, requested nonexistent `src/utils/file.ts` with
`wc`. The output reported failure, but a final successful `printf` made the tool
call succeed. At m23 the worker read the correct `src/utils/files.ts`.
The source-access need was recovered, although the inventory command was not
rerun successfully.

Other compound commands did not preserve individual statuses: L26 memory m21
and m49, and L26 epistemic m23. No underlying failure was demonstrated for those
commands. The worker rules already require status preservation, so recurrence
could reflect noncompliance rather than a missing rule.

### T3 — Three validation failures were repaired

- `000003-boundary`, L18 m93: quotation-attribution errors; repaired at m98 and
  validation passed at m101.
- `000008-epistemic`, L26 result 1 m64: quotation-attribution errors; repaired
  at m65.
- Same worker, m68: a quote occurred three times; m69 supplied the disambiguating
  source range and m72 passed validation.

These repairs added attribution or disambiguation. No claim withdrawal or
narrowing was identified in these validation repairs.

### T4 — Actual output truncation was recovered

`000007-memory`, L26 result 0 m50, retained lines 110–584 of a search result,
dropping 109 lines. The narrower search at m51–52 recovered the omitted SDK
matches. No unrecovered substantive content was identified.

Some required reads advertised a remaining line that proved to be empty EOF
content. Two verification workers deferred or omitted such continuations. This
is a procedural imperfection, not evidence of a substantive reading gap.
Scoped source reads were allowed and were not classified as failures merely
because more source lines existed.

### T5 — Read logs record requested rather than actual ranges

`000026-report-verification` logs ranges such as search lines 160–339, overview
lines 985–1084, and the distill skill lines 1–180, although the corresponding
files have 252, 1033, and 136 lines. Reads are at L46 m49 and m54; the authored
log is at m67. `000017-report-verification` has similar ranges.

The tools returned through EOF. This does not establish fabricated content or
insufficient reading, but the retained logs are not exact coverage records.

### T6 — No unauthorized mutation observed

Inspection found no explicit worker writes outside assigned outputs, identities,
or scratch paths; no target execution, network use, nested delegation, or
prior-review exposure was observed. The correcting epistemic worker copied its
supplied previous report into its own output before editing. The memory-profile
worker executed an authorized scratch generator and revalidated semantic
self-revisions after an earlier validation pass. Neither was an unauthorized
repair.

## Coverage and cost

| Attempt | Session anchor | Tool calls |
|---|---|---:|
| `000003-boundary` | L18 | 77 |
| `000005-runtime` | L22 | 42 |
| `000007-memory` | L26 result 0 | 57 |
| `000008-epistemic` | L26 result 1 | 45 |
| `000014-reconciliation` | L30 | 23 |
| `000017-report-verification` | L34 | 42 |
| `000019-epistemic` | L38 | 27 |
| `000023-reconciliation` | L42 | 23 |
| `000026-report-verification` | L46 | 44 |
| `000028-memory-profile` | L50 | 29 |
| `000030-profile-verification` | L54 | 30 |
| `000032-synthesis` | L60 | 34 |
| `000034-synthesis-verification` | L64 | 32 |

Total: 13 workers, 836 embedded messages, 505 tool calls (419 reads, 47 bash,
33 writes, 6 edits). Seventeen validation invocations produced 14 passes and
three failures; every worker eventually obtained a pass. All enclosing worker
results reported exit code 0, empty stderr, and normal stop.

Harness-reported usage: 305 model turns; 991,770 input tokens; 12,145,408
cache-read tokens; 93,797 output tokens; $4.1360508 reported cost; 2,420.02 summed
worker-seconds. Summed time is not wall-clock time because workers overlapped.
These figures cover the original analysis workers, not this audit.

Repeated independent reads were partly required by the method. Avoidable
retries and successful semantic review should not be collapsed into one waste
measure. Missing host implementation, target-run evidence, datasets, and raw
benchmark traces remain evidence limits, not execution failures established by
this audit.

## Improvement candidates, not adopted changes

The audit proposed checking skill examples against APIs, requiring concrete
reload consumers for retained-memory claims, preserving documentation-backed
mechanisms at their actual evidence strength, inspecting benchmark denominators,
reporting recovered failures, and making consequential profile verification
selectively source-facing. It also proposed better shell-status handling and
accurate source-read ranges.

These are hypotheses for comparison with other reports. N1–N6 could be local
output mistakes; T1 shows an existing safeguard working; T2 concerns an already
stated rule. No candidate has cross-run support established here. The workshop's
multi-report decision boundary supersedes treating this list as a method-edit
backlog.
