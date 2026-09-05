---
name: analyse-agent-memory
description: "Analyse memory and context routes as a specialist invoked by analyse-agentic-system, returning a typed report for integration into the main result."
type: kb/types/instruction.md
user-invocable: false
allowed-tools: Read, Write, Grep, Glob, Bash
context: fork
argument-hint: "parent run, frozen memory-input.md, and memory-report.md destination"
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

Write only the commissioned `memory-report.md` using
`kb/reports/types/agent-memory-analysis-report.md`. Read that contract and the
Memory comparison fields and Status fields sections of
`kb/types/agentic-system-analysis-result.md`. Do not load the legacy review
type, prior system reviews, surveys, matrix outputs, or style exemplars.
The parent owns canonical IDs, integration, publication and completion. Do not
publish, modify the parent's input/result, delegate, or stage and commit.

Hash the input and this skill before analysis. Report those identities and
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

Follow the old memory review's analytical progression: core mechanisms,
operative artifacts, write side, read-back, then a curiosity pass. Keep each
finding source-native before giving a Commonplace classification. A thin
memory boundary warrants short sections with explicit limits.

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
known value its supporting records and inference. A complete set covers all
scoped alternatives; use explicit uncertainty when an included branch remains
opaque or uninspected. A Session identifier alone supplies no task horizon.
Distinguish missing evidence from a negative finding. Use local proposal IDs
where the parent has not yet registered a discovered object or route.

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

Return the report path, SHA-256, status and a short summary of integration
issues. Progress and urgent scope/access requests may be sent separately, but
every substantive finding or unresolved issue must be in the final report.
