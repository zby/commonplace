---
description: "Use with every analysis model hand-out for input reading, write authority, frozen sources, correction answers and content checks"
type: types/instruction.md
---

# Follow the engine analysis worker rules

Produce one assigned analysis output from its pinned inputs without changing the target, evidence boundary or coordinator-owned state.

These rules serve every new-engine model role: boundary, the three analysts,
reconciliation, record verification, profile, profile verification, synthesis
and synthesis verification. The coordinator owns
scheduling, acceptance, integration and recovery; this hand-out grants neither
delegation nor publication authority.

## Read the hand-out

Read the invocation prompt completely, recovering every truncated part. Read
the named instruction first, then every Input reading batch in printed order.
Use supplied paths unchanged. Complete a batch before beginning the next;
read oversized files in the printed bounded ranges until their end. Read
source files and searches in bounded ranges too.

Inspect the complete tool result, including status, errors and truncation.
Recover a truncated read with a smaller range; a larger inner token limit
cannot fix outer delivery truncation. A running command has no final status
until it completes. Use the available read tool for files when the runtime
requires it. Group reads only when that tool supports complete batch delivery.

| Name | Meaning |
|---|---|
| `system`, `run-id` | Fixed target name and exact run identity |
| `job`, `attempt` | Assigned job and open attempt |
| Named inputs | Absolute paths; `absent` means the optional input is missing |
| `opening` | Pinned opening JSON, including the prepared `command-path` and source identity |
| `refusal` | Optional refusal report: refused version, identity, scope and findings |
| `previous-boundary`, `previous-report`, `previous-reconciliation`, `previous-profile`, `previous-synthesis`, `previous-verification`, `previous-answers` | Prior completed outputs by identity, when supplied; not current inputs |
| `validation-set`, `validation-member` | Intended set directory and member slot for content validation |
| `output`, `output-answers`, `problem` | Primary result, declared correction answers when supplied, or inability report |
| `workspace`, `scratch` | Per-attempt workspace and intermediate-file directory |

The supplied contracts give the operative definitions for this job. Linked
background definitions are not extra mandatory inputs. An unavailable
required input, needed target or source-identity change, or consequential
scope decision not authorized by the instruction requires `problem`. An
uncertainty that only limits a conclusion stays beside that conclusion in
`output`; do not discard supported findings to make coverage uniform.

## Stay within authority

Write only the supplied output paths (`output` and `output-answers` when
present), `problem`, `worker-model` and intermediate files under `scratch`. The
boundary instruction separately permits immutable captures or bundles under
`capture-directory` in `opening`, including creation of that directory. Do not
modify existing captures. Closed hand-out workspaces are disposable; captures
must survive them. All supplied inputs, previous output and source checkouts
are read-only.
Do not create other workspace files, edit the working set or another job's
workspace, or alter attempts, versions, judgments or run metadata. The layout
is authority, not a filesystem sandbox.

Do not publish, stage, commit, delegate or invoke a worker. Read engine state
only through this prompt's supplied inputs and previous output; do not inspect
other attempts or reconstruct run-state paths. Code materializes accepted
members; writing a candidate does not install it.

If refusal findings are supplied, repair those defects and their consequences
against the frozen source, preserving unrelated work. Use the supplied
previous output as the baseline, not a mutable member copy. Do not repeat the
whole analysis. The engine's max attempts do not reset after acceptance.

## Answer correction obligations

For every role supplied `output-answers`, write an empty file when there are
no blockers. This includes the analysts, profile, synthesis and the profile
and synthesis verifiers. Boundary, reconciliation and record verification
repair refusal findings in their primary output without an auxiliary answer.
For roles with `output-answers`, on a retry repair Findings in `refusal` and
answer every entry under its `## Blockers`, in order, using
the record contract's `- corrected: ...` or `- declined: ...` grammar.
`none` means no blockers. Unstructured operator findings constitute one
blocker. For analysts, the feedback's Cited records from other reports supplies
peer fragments; do not reconstruct whole peer-report paths. A structural repair
can retain earlier semantic blockers: answer those too, not just the latest
format findings. Analysts preserve the accepted predecessor's record IDs and
referents; other roles preserve unrelated supported findings and carried limits without
inventing records. The engine records the delivered primary previous output
and `previous-answers` in the producer attempt. Code tests a `corrected` answer
against that delivered primary output, not a member acceptance has since replaced.

Recheck each blocker against frozen evidence. Correct the finding and every
dependent field, table, ledger row and conclusion where it holds. Otherwise
keep the finding and explain the evidence for declining. Preserve unrelated
work. A `corrected` answer requires a changed primary output. When all answers are
`declined`, the primary output may remain byte-identical if the answers change; this
completes an attempt, not a semantic acceptance or override of the verifier.
Repeating both the primary output and answers fails and counts toward max attempts.

When fixing a structurally refused attempt, use the role's supplied previous
primary output as the edit baseline and `previous-answers` to preserve relevant
answers. For analysts, the unchanged accepted predecessor still governs record
preservation. Do not make artificial primary-output changes merely to bypass
an unchanged-result failure. Return both output paths when both were written.

## Inspect sources, not target execution

Analyse source text and evidence within the assigned frozen boundary. Do not
execute the target, tests or examples, call its model providers or services,
install dependencies or create runtime fixtures. Source reading, quotation,
source capture authorized by the boundary instruction, and Commonplace
validation remain in scope. Missing execution evidence limits conclusions;
it does not authorize setting up a runtime check.

For Git, read and search the files at the registered commit under its frozen
`path`. Initially inspected paths are coverage, not an allowlist. Inspecting
another file at that commit does not expand the source boundary. An excluded
path may be inspected for relevance, not silently included. A material
shipped responsibility outside the selected functional boundary requires
`problem` with its path, responsibility and prevented conclusion. Treat the
checkout as read-only. For a capture, read only its frozen contents.

## Check content and quotation

Read `opening` for `command-path`, the prepared worktree's command directory.
If it is missing or the command is unavailable, write `problem`; do not use
a shared installation as a substitute. Run:

```text
<command-path>/commonplace-validate <output> --set <validation-set> --member <validation-member>
```

Use each supplied value unchanged. Run commands separately and inspect every
exit status, or chain dependent commands with `&&`. Pipelines require
`set -o pipefail`. Retain stderr as well as stdout. Repair findings and rerun
until the content check passes; do not report a check you did not execute.
Validation is read-only and reports this slot's content and relation findings.
A content pass establishes form and quotation occurrence, not claim support,
analytical correctness or job acceptance. Code also checks invocation-specific
identity and source conditions.

Use the source contract's quotation form; do not calculate attribution ranges
or revisions. Resolve ambiguity by printed context or a longer quote. For a
missing quote, reread the source and recheck the claim. Narrow or withdraw a
finding only when the evidence cannot support it, never merely to pass a check.
Record each finding narrowed or withdrawn during check repair, with its
reason, in `scratch/check-repairs.md`.

## Avoid prior-analysis exposure

Do not call agent listings or read style exemplars, prior reviews or audits,
`kb/agent-memory-systems/`, `kb/agentic-systems/reviews/`,
`kb/agentic-systems/reviews-archive/`, `kb/agentic-systems/reports/`,
`kb/agentic-system-analyses/retained/`,
`kb/agentic-system-analyses/retained-archive/`,
`kb/work/analyse-agentic-system/`, other runs under
`kb/agentic-system-analyses/state/`, surveys or comparison outputs. A path
filter does not make an agent listing safe. If any tool exposes prior-review
prose or audit findings, stop and write `problem` saying so; this run cannot
use your work.

When finished, reply in one line naming the file written, without summarizing
it. Follow higher-priority runtime requirements for progress messages.
