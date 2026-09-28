---
description: "Use in a fresh worker commissioned by analyse-agentic-system to analyse memory and context routes from frozen inputs and return a typed report."
type: types/instruction.md
---

# Analyse agent memory

Goal: a source-grounded account of the system's memory mechanisms and their
proposed comparison classifications, returned as one typed report the parent
can integrate into the main agentic-system analysis.

## Commission and boundary

Run as a fresh specialist under `analyse-agentic-system`. Require the parent
run ID, frozen `memory-input.md`, report destination, and permitted source
access. The input supplies the subject, source register with full revision or
capture digest and access root, relevant canonical records, requested memory
scope and depth, exclusions, and any specific question. Its records are
provisional findings to check against sources, not accepted conclusions.

Write only the commissioned `memory-report.md` under the
[`agent-memory-analysis-report`](../types/agent-memory-analysis-report.md)
type. Read that contract, including its Memory comparison fields, and the
set-wide conventions of the
[overview type](../types/agentic-system-analysis-overview.md#the-set):
canonical identity, the declaration and annotation grammar, status fields
and the Source register's quotation contract. Together they fix every
section, field and controlled value the report uses. The parent finalizes
your report as the set's memory member, `memory.md`: it maps your proposal
IDs to canonical IDs by exact token, turns a seeded record you re-declared
into an `On <ID>` annotation, and appends amendments; your report stays in
the run directory as provenance, pinned by the member's `finalized-from`.
Write it so those mechanical edits are the only ones needed.
Do not load the legacy review type, prior system reviews, surveys, matrix
outputs, or style exemplars. The parent owns canonical IDs, integration,
publication and completion. Do not publish, modify the parent's input or
set, delegate, or stage and commit.

Do not call agent listings for status: their payloads may include prior
analyses, even with a path filter. Return through the final report and
completion event. If a notification fails, do not assume it arrived; include
that failure in the final response and end the turn so the supervisor can
relay the report path, hash and status. Prior-analysis exposure blocks this
worker's handoff; report it and stop for a fresh source-only replacement.

Hash the input and this instruction before analysis. Report those identities
and your actual model identity; state `unknown` if the runtime does not expose
it. Verify input and method hashes again before returning. Changed input
requires a new handoff from the parent, not silent reconciliation in the
worker.

## Inspect and explain

Use the frozen primary sources. For Git, inspect commit-addressed blobs
through `git --no-replace-objects -C <source-root> show <full-commit>:<path>`
and scoped `grep` or `ls-tree`; the worktree and current HEAD are not
evidence. For captures, verify the supplied digest before reading. Select
paths and ranges before reading; truncated output supplies no evidence until
the needed range is delivered in a bounded read. Budget combined tool output
as well as individual reads, inspect the delivered output for truncation, and
reread omitted spans before citing them. A missing source or needed scope
expansion returns a blocked report with the conclusion it prevents.

Work through the report's sections in order: core ideas, shared records,
write side, read-back, then a curiosity pass that challenges strong source
claims, misleading labels and partial ontology mappings, recording its
corrections under Core ideas and its open questions under Integration
issues. Keep each finding
source-native before giving a Commonplace classification. Do not turn source
claims into implemented or observed behavior. Keep current Commonplace
recommendations outside the report; no comparison to other systems is
needed. A thin memory boundary warrants short sections with explicit limits.

For each load-bearing finding, generate the quote block the overview's
Source register requires with
[`commonplace-quote`](../reference/commands.md#commonplace-quote):
`commonplace-quote <sibling-run-state-path> --source-path <commit-relative-path>
--text-file <selection-file>`, omitting `--source-path` for the frozen
capture, or `--selections <json-file>` to resolve many selections across
files in one call. Choose the occurrence whose context supports the finding
and insert its citation unchanged. Request discontiguous passages separately. A failed
lookup requires rereading the source and revising the selection; never format
a citation, strip source characters, or calculate a range by hand. Assess
semantic support yourself; publication validates the assembled bundle, so run
no separate quote check.

## Classify and hand back

You own the proposed classifications in `memory-comparison` as well as their
supporting analysis, under the report type's per-value evidence contract. Do
not weaken a wired value because another value is
merely afforded. Distinguish missing evidence from a negative finding. Every record the
profile cites is declared or annotated (`On <ID>`) in your report; annotate
any seeded record the profile cites. Use
local proposal IDs where the parent has not yet registered a discovered
object or route; the parent maps exact tokens.

Record corrections, proposed records, unresolved questions and limitations
inside the report. Validate it with `commonplace-validate --full
<report-path>` and correct structural errors. Inspect exit status and stderr,
not only stdout. Run dependent commands separately or with `&&` (and
`set -o pipefail` for pipelines); later validation or hashing cannot clear an
earlier failure. Rehash only the final corrected report.

Return the report path, SHA-256, status and a short summary of integration
issues. Progress and urgent scope or access requests may be sent separately,
but every substantive finding or unresolved issue must be in the final
report.
