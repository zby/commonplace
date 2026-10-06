---
description: "Job of an analyse-agentic-system run: the memory analyst, first round or correction round"
type: types/instruction.md
---

# Analyse memory and context as the memory analyst

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first` or `correction`. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `runtime` | Absolute path of the runtime report. | `first` |
| `previous-report` | Absolute path of your report as the record verifier judged it. | `correction` |
| `requests` | Absolute path of the blockers addressed to your report, with the current declarations of the records they cite from other reports. | `correction` |
| `answers` | Absolute path where you write your answers to those blockers. | `correction` |

## Situation

The runtime analyst has written `runtime`, a provisional account of how
`system` runs, with its routes as `RT-` records. The epistemic analyst works
in parallel with you and does not see your report. A reconciler will connect
your records to the others', and an independent verifier will judge them
against the frozen source.

## Mission

Write the memory report to `output` under the supplied memory type: a
source-grounded account of `system`'s memory and context mechanisms in
source-native terms, covering every included part along the record
contract's coverage dimensions, not only a primary store or the
best-understood route. Choose the memory scope from the runtime routes and
state its inclusions and exclusions. Declare new records with `MEM-`; annotate
supplied `RT-` records rather than redeclaring them, and record each overlap
disposition, each correction to a supplied fact and each unresolved question
under Integration issues, so the reconciler and verifier can act on them.

Treat the runtime report as a starting account, not the inspection limit:
check the frozen source's CLI dispatch, hooks, registered tools and exposed
library or service operations against its routes, and trace memory
operations, including evaluation, cleanup, rejection and withdrawal, through
retained results to their later consumers. Challenge strong source claims,
misleading labels and partial ontology mappings. A thin memory boundary
warrants short sections with explicit limits.

## Boundaries

Describe mechanisms; do not map them to controlled comparison values, which
the profile job assigns later, and do not compare the system with others or
with Commonplace. Cite `runtime`, the Source register of `boundary`, your own
declarations and, in a correction round, any record `requests` supplies; the
output is refused with unresolved IDs otherwise.

When `round = correction`, follow **Correct a report after verification** in
the supplied worker rules; this instruction still governs the report's
content.

Run the acceptance check before submitting; a check result and the
conclusions it prevents belong under Limitations and checks.
