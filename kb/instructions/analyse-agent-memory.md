---
description: "Use in the memory job of an analyse-agentic-system run to analyse memory and context routes from the frozen boundary and write the set's memory member."
type: types/instruction.md
---

# Analyse agent memory

Goal: a source-grounded account of the system's memory mechanisms and their
comparison classifications, returned as one typed report that becomes the
memory member of the main agentic-system analysis.

## Inputs and boundary

Run as the memory job of an `analyse-agentic-system` run. Your prompt names
the run, the system and the report's output path. Work from `boundary.md`,
which gives the frozen source with its full revision or capture digest and
access root, the boundary and the source register, and from
`output/runtime.md`, the runtime member. The runtime member's records are
provisional findings to check against sources, not accepted conclusions.
Choose the memory scope from the runtime member's routes and state it, with
its exclusions, in the profile's `scope` and the report's Boundary and
evidence.

Write only the report under the
[`agent-memory-analysis-report`](../types/agent-memory-analysis-report.md)
type. Read that contract, including its Memory comparison fields, and the
set-wide conventions of the
[overview type](../types/agentic-system-analysis-overview.md#the-set):
canonical identity, the declaration and annotation grammar, status fields
and the Source register's quotation contract. Together they fix every
section, field and controlled value the report uses. The run's last
accepted report becomes the set's memory member, `memory.md`, byte for
byte: nothing is mapped, merged or appended afterwards, and the reconciliation's
corrections to your records are amendments in the overview. Write it as
the member.
Do not read prior analyses (the worker rules list where they are) or style
exemplars. The runtime analyst owns the unprefixed IDs; the
reconciliation owns integration. Do not call agent listings for status: their
payloads may include prior analyses, even with a path filter.

## Inspect and explain

Use the frozen primary sources. For Git, read and grep the files of the
checkout at `source.path`, which the boundary job checked out at the
recorded commit with an empty `git status`; do not modify it. For captures, verify the supplied digest before reading. Select
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
semantic support yourself; publication validates the assembled set, so run
no separate quote check.

## Classify and check

You own the proposed classifications in `memory-comparison` as well as their
supporting analysis, under the report type's per-value evidence contract. Do
not weaken a wired value because another value is
merely afforded. Distinguish missing evidence from a negative finding. Every record the
profile cites is declared or annotated (`On <ID>`) in your report; annotate
any runtime record the profile cites. Declare each object, route or other
record you establish under a `MEM-` ID, such as `MEM-RTE-1`; the ID is
final. Annotate a runtime record rather than re-declaring it, and name a
record of yours that may duplicate a runtime record under Integration issues.

Record corrections, possible duplicates, unresolved questions and
limitations inside the report; every substantive finding or unresolved issue
is in the report. Validate it with `commonplace-validate --full
<report-path>` and correct structural errors, inspecting exit status and
stderr, not only stdout.
