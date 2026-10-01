# Three Instinctual Memory runs: results and trace audit

Recorded 2026-10-01 at the operator's request to compare three analyses,
inspect their traces for hidden failures, and identify fixes. This is an
audit of completed or blocked work, not a resumption or correction of it.
The generated reviews and retained members were left unchanged.

## Comparison boundary

The three runs use the same repository,
`https://github.com/jasonkneen/instinctual-memory`, source commit
`6acb13dc35765bf5ccfc87e445dd09c480f1c28a`, and method commit
`2ad1816a79e0e5d9b1e178a109d3615fdfab61e5`. Their opening records all name
the same initially absent review destination. They ran concurrently.

**These are three repetitions of Sol medium, not the planned model
comparison.** Every parent and all 26 worker sessions record
`model: gpt-6.1-sol`, `effort: medium` in their turn contexts. None of the
worker launch calls supplies a model or effort override. The invocation
messages specify the pinned source but no model. The skill's `model: opus`
frontmatter did not determine the recorded Codex model.

| Run suffix | Actual model and effort | Parent elapsed time | Worker jobs | Memory returns | Final-set words | Matching quotes | Outcome |
|---|---|---:|---:|---:|---:|---:|---|
| 05 | gpt-6.1-sol medium | 52.9 min | 10 | 1 | 20,289 | 52 | Synthesis accepted; publication blocked |
| 06 | gpt-6.1-sol medium | 42.4 min | 8 | 0 | 22,547 | 50 | Synthesis accepted; publication blocked |
| 07 | gpt-6.1-sol medium | 39.6 min | 8 | 0 | 20,050 | 43 | Published and complete |

Elapsed time runs from the first recorded parent timestamp to its final
handoff or block report. It includes coordination and stopping overhead,
and is not a controlled latency benchmark. Word counts include YAML,
quoted code, verification and reconciliation, using whitespace splitting.
All ten axes are marked `known` in every final memory profile.

Local evidence is under
`kb/reports/state/agentic-system-analysis/AAS-2026-10-01-instinctual-memory-05/`,
and the corresponding `-06/` and `-07/` directories. Only 07 has a set under
`kb/reports/retained/agentic-system-analysis/` and a published review at
`kb/agentic-systems/reviews/instinctual-memory.md`.

The parent trace IDs are:

| Run | Parent thread ID |
|---|---|
| 05 | `01a0f7be-8c29-73a3-85f3-7d9d98496c4c` |
| 06 | `01a0f7be-6994-72a1-a70e-bbfbee19ef0a` |
| 07 | `01a0f7be-029d-7020-a8c9-0af752fb481c` |

Trace files are local JSONL under `/home/zby/.codex/sessions/2026/10/01/`.
Workers are associated through their `parent_thread_id` and `agent_path`.
The audit inspected tool inputs, returned statuses and delivered text,
worker launch settings and completion events; private reasoning and
encrypted handout contents are not retained here. Event numbers below
are zero-based JSONL line indices in the named worker session.

## What worked

All three analyses reached record verification, synthesis and synthesis
verification. Every handed-out job was accepted on its first workflow
attempt. Run 05's extra memory and reconciliation jobs were an analytical
return about ranking, not a malformed-output retry. Run 06 repaired a
local validation failure before returning its memory report.

All sets agree on the useful operational account: session/file acquisition,
durable source events, rules/model extraction, versioned facts, requested
recall, host callbacks, exported instructions, maintenance and evaluation.
All distinguish implementation evidence from actual host activation,
passing tests and improved performance. All identify two concrete semantic
risks in the target: preference extraction loses negative qualifiers, and
duplicate comparison drops negation/modal words. Their withdrawal accounts
also distinguish query search, direct reads, exports, source journals and
external copies.

The audit independently reran member validation and pinned-source quote
matching for all 15 members. **All 145 quote blocks match; every member
passes its type checks.** All three manifests match their member hashes.
The retained 07 set is byte-identical to its run output. The published
review, retained manifest and completed run state also pass
`commonplace-validate`. These checks establish form, occurrence and
integrity; they do not establish semantic accuracy.

The tool traces show source inspection, quotation and Commonplace checks,
with no observed target execution, dependency installation, provider call
or source refresh. Missing execution evidence is correctly retained as a
limitation. The previous quote-generation failure did not recur.

## Findings and fixes

### F1 — Shared publication destination invalidated two tests

Run 07 published first. Runs 06 and 05 then stopped at publication with
`ValueError: publication destination changed since inspection`. Their
`workflow-state/workflow/block-1.md` files and parent final reports give
that reason. Both have accepted overview members and review candidates.
Neither is an analyst failure.

The expected-incumbent check protected the first publication. Weakening
that check would permit a later test to overwrite it. For another
concurrent trial, supply a different `review-path` for each invocation,
directly under `kb/agentic-systems/reviews/`. This option already exists;
the test instructions need to name the distinct paths. No new publication
mode is needed to address this collision.

Both blocked runs still have `run-status: running`, null artifact and
failure fields, while their effect records say publication started and
their workflow reports retain an operator stop. A consumer of run-state
alone cannot distinguish active work from this stopped run. Expose the
workflow block/stop in the handoff or status command, or represent that
state explicitly. Do not infer analytical failure from the publication
block.

### F2 — Accepted complete profiles disagree semantically

Seven of the ten axis value sets agree. Three differ:

| Axis | 05 | 06 | 07 |
|---|---|---|---|
| behavioral_authority | knowledge, instruction, enforcement, routing, validation, ranking | knowledge, instruction, enforcement, ranking, routing | enforcement, instruction, knowledge |
| curation_operations | consolidate, dedup, evolve, invalidate, decay | dedup, evolve, invalidate, decay | consolidate, dedup, evolve, invalidate, decay |
| trace_source | session-logs | session-logs, event-streams | session-logs |

The field definitions and retained records reveal different kinds of issue.

**07's ranking exclusion is too narrow.** Its profile and reconciliation
exclude ranking because the scoring policy is fixed or model-based rather
than learned retained policy. The registered
[behavioral authority definition](../../notes/definitions/behavioral-authority.md)
includes selection or ranking influence. Retained statements, titles and
aliases feed tokenization and corpus-dependent scores in
`src/search/lexical.rs:121-165`; they need not rewrite the ranking algorithm
to influence ranking. Run 05's returned finding and corrected memory
annotation establish this distinction. Run 07's verifier accepts the narrower
definition without addressing it.

**06 omits consolidation despite describing its mechanism.** The
[memory type](../../types/agent-memory-analysis-report.md) defines
`consolidate` as reducing retained content without new claims. The same
run describes journal windows becoming selected durable facts, and its
reconciliation correctly says an accidental polarity defect is not a new
curation operation. Its exclusion nevertheless rests on the command name
and uncertain model semantics instead of the supported reduction route.
At minimum the rules route needs assessment against that positive
definition. Source uncertainty should not erase an independently supported
operation. The record verifier repeats the four retained values and passes
the omission.

**The trace-source difference exposes an underspecified boundary.** Run 06
correctly notices that calendar summaries and voice cues become `Role::Note`
in `src/ingest.rs` and enter the model branch in `src/consolidate.rs:634-646`.
Runs 05 and 07 reserve trace-source classification for session messages.
The controlled value `event-streams` does not define whether external
calendar/voice content counts as an agent learning trace. Source occurrence
cannot settle that taxonomy. Treat this as a contract decision, rather than
declaring either value set correct by majority vote.

The distinction between enforcement, validation and routing is also thin:
05 counts blocked-ID admission checks as validation; 06 treats checkpoint
progress as routing; 07 reports only three authority values. Define the
positive consumption witness for the categories the comparison actually
needs. The existing
[analyst instruction audit](./analyst-instruction-audit.md) already records
this vocabulary gap. A short definition and example belongs beside each
controlled value. Another general instruction to “check all axes” adds
little: every verifier already says it did so.

### F3 — Bounded-read rules still fail in actual tool use

The three runs contain 19 tool deliveries explicitly marked
`Warning: truncated output`: five in 05, eight in 06, six in 07, counting
parents and workers. Many were repaired by smaller reads. Recovery is real,
so the raw count must not be presented as 19 unresolved failures.

Examples of repaired reads include 05 reconciliation's epistemic member,
06 synthesis's memory/epistemic members, and 07 runtime's theory-builder
definition. Several searches or reads remain incomplete:

- 06 memory worker `01a0f7cb-2fc3-77e3-ba08-e974bf8516c4`, event 94:
  ten source ranges returned in one outer call lose 1,762 tokens spanning
  task operations and other files. Subsequent calls 110 and 119 recover
  some search/operation context but do not repeat all lost ranges.
- 06 runtime worker `01a0f7c1-6e9b-7391-bb17-389bdd9fa22f`, event 39:
  a large cross-file symbol search loses 4,186 tokens. Later focused reads
  inspect important mechanisms, but do not recover the whole search.
- 07 epistemic worker `01a0f7ca-235f-7002-be3b-398e8f5e2fb8`, event 67:
  a multi-file dispatch search loses 1,367 tokens. Later source slices
  cover selected branches, without a complete repeated search.

These gaps limit coverage confidence. They do not prove a particular
conclusion false. The worker rule already explains outer truncation and
requires rereading the lost range; repeating that explanation is unlikely
to solve it. Use separate bounded deliveries, with a bounded search result
or a saved result read in chunks. The existing
[role-specific packet proposal](./role-specific-packets-and-code-owned-form.md)
also reduces the contract volume workers must recover. Keep acceptance
focused on useful evidence rather than adding dynamic target checks.

Two workers also returned only stdout during their initial combined contract
read: 05 reconciliation round 1, event 23, and 06 record verification,
event 22, use `text(r.output)`. This discards the command's exit status and
stderr wrapper. Both reread contracts afterward, and no actual hidden
command failure is established in those calls. They are failures of status
preservation, not evidence of a failed analytical result.

### F4 — Repaired errors must be separated from hidden failures

Observed nonzero commands include guessed absent paths (`src/erase.rs`,
`src/evaluate.rs`, and a framework quote-command path), a multi-file search
including absent source files, and a parent's guessed checkout directory.
Workers found the actual implementation paths or inspected available
sources afterward. The 06 memory worker's validator initially rejected an
unresolved lineage reference; it added an `On RTE-12` annotation and reran
validation successfully. These errors consumed work but did not survive as
structural defects in the final members.

Use source file inventories before naming implementation files. Preserve
the existing local repair and deterministic quote acceptance behavior.
The workflow's zero rejected attempts does not mean every worker command
succeeded: internal repairs happened before handoff.

Earlier run directories 02–04 contain opening blocks for uncommitted
workshop changes (`kb/work/README.md` and the localization plan). They
never acquired a boundary or produced analyst results, and are excluded
from the three-run comparison. The clean-worktree prerequisite detected
that setup problem before analysis began.

### F5 — Reconciliation and verification work, but do not settle taxonomy

All runs carry actual amendments rather than only agreement prose. 05
repairs ranking through a memory return. 06 corrects the model input scope
and the difference between exact reads and query search. 07 explicitly
corrects the runtime's task-write claim from atomic replacement to locked
truncate/write/sync, matching `src/ops.rs:716-730`. Public synthesis respects
these amendments. Tidy and evaluation are present in all three, so the
older omission of the maintenance route is not reproduced.

The verifier revision permits useful bounded conclusions and these runs
confirm that synthesis can follow record verification. However, all
verifiers accept `known` profiles with the semantic differences above.
The quotation check does not address that failure. Clarify the disputed
classification witnesses first, then rerun the record check against them.

A related architectural risk remains: `systems_matrix.py` exports raw
memory-profile values and assessments, without applying reconciliation
amendments or unresolved-conflict qualifications. No unresolved-conflict
case exercised that path in these three runs. Before accepting a profile
defect only as a public limitation, ensure downstream comparisons can
represent that qualification. This is an unexercised risk, not an observed
matrix failure here.

## Recommended order

1. Specify the actual worker model/effort and a distinct review path per
   test. Check launch metadata before spending a full run. These three
   repetitions cannot answer Luna medium versus Luna xhigh versus Sol
   medium.
2. Resolve the consolidation and authority interpretation errors, and
   settle the event-stream boundary in the comparison contract. Use brief
   positive examples; avoid another blanket verification checklist.
3. Reduce contract delivery to the needed role sections and use bounded
   tool deliveries. The present 20,000–22,500-word sets create substantial
   rereading work; much of the extra overview volume is verification
   accounting rather than public synthesis, which is 791–997 words.
4. Make publication blocks/stops visible in run status and handoff. Keep
   the expected-incumbent protection.
5. Reuse the three settled record sets for a focused profile-verifier test
   before commissioning another whole-system analysis. Then run the
   intended model comparison with the same source and method pins.

07 is the most compact set and the fastest observed repetition, but its
authority-profile issue prevents treating it as a clean semantic reference.
06 offers useful additional acquisition detail while retaining the most
profile uncertainty. 05 demonstrates a successful correction path at the
cost of two extra jobs. The evidence supports these specific differences,
not a statistical model ranking.

## Definition repair — 2026-10-01

The operator authorized fixing the definitions after this audit. The
[memory report type](../../types/agent-memory-analysis-report.md) now
defines every authority value by its consumed retained part and effect.
Ranking includes retained content scored by a fixed algorithm; checkpoint
input selection is routing; an admission blocklist can supply both
validation and enforcement. Learning input includes updates to durable
guidance as well as parameters. This clarification may expose additional
omissions in the old profiles.

Consolidation explicitly includes reducing retained session content to
standing facts while keeping the source messages. Trace-source values
classify original activity records rather than their journal wrapper or
adapter role. Environmental calendar entries and timestamped voice cues
count as event streams when used in a qualifying durable-memory write.
Imported static instructions alone remain outside trace-source classification.

The memory, reconciliation and record-verification jobs already require
this type as a dependency. They receive one definition set; no duplicate
definitions or new verification phase were added. Existing run artifacts
retain their original method-bound results. A fresh semantic verification
under the revised definitions remains a separate test.
