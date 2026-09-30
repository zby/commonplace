---
description: "Job of an analyse-agentic-system run: the memory analyst, first round or correction round"
type: types/instruction.md
---

# Analyse memory and context as the memory analyst

Read every file under `read-first` in your invocation before any other step.

## Parameters

| Name | Meaning | Present |
|---|---|---|
| `system` | The source-native system name. | Always |
| `run-state` | Absolute path passed to `commonplace-quote`; not an evidence input. | Always |
| `output` | Absolute path of your result. | Always |
| `problem` | Absolute path for the reason you cannot finish. | Always |
| `scratch` | Absolute directory for intermediate files. | Always |
| `round` | `first` or `correction`. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `runtime` | Absolute path of the runtime member. | Always |
| `previous-memory` | Absolute path of the previous memory report. | `correction` |
| `returned-findings` | Absolute path of the reconciliation requesting this correction. | `correction` |
| `epistemic` | Absolute path of the epistemic member. | `correction` |

Use the supplied paths unchanged. If a required parameter is missing, write `problem`; do not reconstruct it. Retry refusal feedback applies to the same job and does not change its analytical round.

## Task

Produce a source-grounded account of `system`'s memory mechanisms and comparison classifications as one typed report at `output`. Code copies the accepted report unchanged into the set's memory member. The reconciliation owns integration and records its corrections as amendments in the overview.

Work from `boundary` and `runtime`. Treat the runtime member's records as provisional findings to check against sources. Choose the memory scope from those routes and state its inclusions and exclusions in the profile's `scope` and the report's Boundary and evidence. The [memory report type](../../../types/agent-memory-analysis-report.md) fixes the sections, fields and controlled values; the overview type fixes the set-wide conventions.

## Inspect and explain

Work through the report's sections in the order the memory report type gives. Trace the distinguishing mechanisms on the write side and read-back side, then challenge strong source claims, misleading labels and partial ontology mappings. Record corrections to supplied facts and unresolved questions under Integration issues; explain distinguishing mechanisms under Core ideas. Keep current Commonplace recommendations outside the report; no comparison to other systems is needed. A thin memory boundary warrants short sections with explicit limits.

A justified unknown or an access gap that only limits a conclusion belongs in a complete report, with the prevented conclusion named. If missing source access or an unresolved scope decision prevents completing the assigned analysis, write `problem` instead of a blocked report at `output`. Needed expansion beyond the frozen boundary is such a scope decision; do not expand it yourself.

## Classify and record

You own `memory-comparison` and its supporting analysis under the report type's per-value evidence contract. Do not weaken a wired value because another value is merely afforded. Distinguish missing evidence from a negative finding.

Declare each record you establish under a `MEM-` ID, such as `MEM-RTE-1`, under the six kind headings the memory report type lists. Put memory-specific fields on a record declared elsewhere under `## Annotations`, as `#### On <ID> — Label`, with the fields the type authorizes. Every record the comparison profile cites must be declared or annotated in this report itself. Other prose may cite records declared by `runtime` or the Source register in `boundary`; when `round = correction`, it may also cite records declared by `epistemic`. The output is refused if it is not a valid member or its citations do not resolve against those inputs and its own declarations.

Record every correction, possible duplicate, unresolved question and limitation inside the report. Under Integration issues, identify any record of yours that may duplicate a record declared elsewhere, with its evidence and the affected full IDs.

## Correct returned findings

When `round = first`, write the initial report. When `round = correction`, read `previous-memory`, `returned-findings`, and `epistemic`. Answer each returned finding from the sources: correct the report where the finding holds, and keep your finding with its evidence where it does not. Write the whole report again; it replaces the previous report.

A surviving record keeps its ID and referent. A new record gets a new number; never reuse a number from a dropped record. No withdrawal marker is needed for a dropped record: only the accepted report enters the set. The returned findings still refer to the previous report's IDs.

## Check

Validate `output` with `commonplace-validate --full <output>` and correct structural errors. Publication checks the assembled set's quotations; run no separate quote check. Retain the validation result and prevented conclusions under Limitations and checks.
