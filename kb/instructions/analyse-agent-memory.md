---
description: "Use in a fresh worker commissioned by analyse-agentic-system to analyse memory and context routes from frozen inputs and return a typed report."
type: types/instruction.md
---

# Analyse agent memory

Establish the system's memory mechanisms and their supported comparison
classifications for integration into the main agentic-system analysis.

## Commission and boundary

Run as a fresh specialist under `analyse-agentic-system`. Require the parent
run ID, frozen `memory-input.md`, report destination, and permitted source
access. The input supplies the subject, source register with full revision or
capture digest and access root, relevant canonical records, requested memory
scope and depth, exclusions, and any specific question. Its records are
provisional findings to check against sources, not accepted conclusions.

Write only the commissioned `memory-report.md` using the global
[`agent-memory-analysis-report`](../types/agent-memory-analysis-report.md) type. Read that contract and the
Memory comparison fields, Status fields, and Source register sections of
[`agentic-system-analysis-result`](../types/agentic-system-analysis-result.md). Do not load the legacy review
type, prior system reviews, surveys, matrix outputs, or style exemplars.
The parent owns canonical IDs, integration, publication and completion. Do not
publish, modify the parent's input/result, delegate, or stage and commit.

Do not call agent listings for status: their payloads may include prior
analyses, even with a path filter. Return through the final report and completion
event. If a notification fails, do not assume it arrived; include that failure
in the final response and end the turn so the supervisor can relay the report
path, hash and status. Prior-analysis exposure blocks this worker's handoff;
report it and stop for a fresh source-only replacement.

Hash the input and this instruction before analysis. Report those identities and
your actual model identity; state `unknown` if the runtime does not expose it.
Verify input and method hashes again before returning. Changed input requires
a new handoff from the parent, not silent reconciliation in the worker.

## Inspect and explain

Use the frozen primary sources. For Git, inspect commit-addressed blobs through
`git --no-replace-objects -C <source-root> show <full-commit>:<path>` and scoped
`grep` or `ls-tree`; the worktree and current HEAD are not evidence. For
captures, verify the supplied digest before reading. Select paths and ranges
before reading; truncated output supplies no evidence until the needed range
is delivered in a bounded read. A missing source or needed scope expansion
returns a blocked report with the conclusion it prevents.
Budget combined tool output as well as individual reads. Inspect the delivered
output for truncation and reread omitted spans before citing them.

Follow the old memory review's analytical progression: core mechanisms,
operative artifacts, write side, read-back, then a curiosity pass. Keep each
finding source-native before giving a Commonplace classification. Retain the
minimum supporting code or prose for each load-bearing finding. Write the text
to locate into a UTF-8 selection file and run
`commonplace-quote <sibling-run-state-path> --source-path <commit-relative-path>
--text-file <selection-file>`. Omit `--source-path` for the frozen capture.
One occurrence returns only the Markdown citation. Two to ten occurrences return
JSON entries containing complete `citation` strings and selection metadata.
More than ten occurrences returns an error: select a longer quote and retry.
The tool includes additional source context
when needed to distinguish occurrences on the same line. Choose the occurrence
whose context supports the finding and insert its citation unchanged.

Request discontiguous passages separately. A failed lookup requires rereading
the source and revising the selection. Do not format citations, strip source
characters, or calculate endpoints yourself. For ordinary source references,
use the full path without a range, or reuse a generated location. Follow the
main-result Source register contract. Do not run a separate quote check after
insertion; publication uses the regular validator on the assembled bundle.
Assess semantic support yourself, and let the parent retain the chosen quote
once on the canonical record. A thin memory boundary warrants short sections
with explicit limits.

- **Core mechanisms:** explain what retained material can change in later
  work. Account for context volume and selection complexity, provenance and
  trust controls, and human editing/adoption surfaces where material.
- **Artifacts:** distinguish raw traces from derived memory, content from
  access metadata, and opaque payloads from their readable display summaries.
  Record storage, representational form, derivation, and authority at the
  actual consumer. Reuse canonical IDs with a short description; propose
  missing records as `MEM-OBJ-1`, `MEM-RTE-1`, and analogous local IDs.
- **Write side:** identify producer, input, trigger, persistence, rejection,
  maintenance and withdrawal. Separate manual authoring, automatic acquisition,
  and automatic operations over already retained material. Examine every
  trace-fed transformation, including compaction, for a later consuming route.
  For each derived behavior-shaping artifact, state whether it retains the
  reason for what it prescribes and whether any later route reads that reason;
  the parent records this on the theory route, where a rationale a later
  route reads can guide diagnosis.
- **Read-back:** trace retained material through selection and delivery to a
  named later consumer. Separate availability, delivery, activation and
  demonstrated benefit. For pull, identify the requesting consumer role and
  supported interface; an API with an unspecified hypothetical caller is only
  a storage capability. A documented external consumer role may establish an
  afforded route without deployed wiring. Push requires an automatic selector;
  name its trigger, inputs, selected parts, budget and consumption channel.
- **Curiosity:** challenge strong source claims, misleading labels and partial
  ontology mappings. Keep current Commonplace recommendations outside this
  report. No comparison to other systems is needed.

## Classify and hand back

Fill all fourteen comparison axes in the report's `memory-comparison`, using
the main-result contract's assessments, bases and controlled values. You own
the proposed classifications as well as their supporting analysis. Give each
value its own evidence basis, supporting records and inference. Do not weaken
a wired value because another value is merely afforded. A known set covers all
scoped alternatives; use partial coverage to retain supported positives when an
included branch remains opaque or uninspected. A Session identifier alone supplies no task horizon.
Distinguish missing evidence from a negative finding. Use local proposal IDs
where the parent has not yet registered a discovered object or route. Write
every identifier in full, including lists: `MEM-OBJ-1, MEM-OBJ-2`. Never use
abbreviations such as `MEM-OBJ-1/O2` or ranges. The parent maps exact tokens.

Use curation terms consistently: `consolidate` reduces retained content without
new claims; `dedup` merges near duplicates; `evolve` revises an existing entry;
`synthesize` creates a claim absent from the inputs; `invalidate` withdraws
current reliance while retaining history; `decay` forgets or downweights;
`promote` raises tier or salience. Index rebuilds and acquisition alone do not
establish these operations. Trace-learning scope, timing and form must cover
the same qualifying routes.

Record corrections, proposed records, unresolved questions and limitations
inside the report. Questions that prevent integration set `report-status:
blocked`; justified unknown classifications do not by themselves block a
complete report. Validate the report with `commonplace-validate --full
<report-path>` and correct structural errors. This is specialist analysis,
not independent semantic clearance of the main result.

Inspect exit status and stderr, not only stdout. Run dependent commands
separately or with `&&`
(and `set -o pipefail` for pipelines); later validation or hashing cannot clear
an earlier failure. Rehash only the final corrected report.

Return the report path, SHA-256, status and a short summary of integration
issues. Progress and urgent scope/access requests may be sent separately, but
every substantive finding or unresolved issue must be in the final report.
