---
description: "Job of an analyse-agentic-system run: the epistemic analyst, written as the set's epistemic member"
type: types/instruction.md
---

# Trace the epistemic routes

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
`system` runs, with its routes as `RT-` records. The memory analyst works in
parallel with you and does not see your report. A reconciler will connect
your records to the others', and an independent verifier will judge them
against the frozen source.

## Mission

Write the epistemic report to `output` under the supplied epistemic type. It
answers whether and how `system` acquires or produces truth-apt content,
checks it, grants or withholds reliance, and lets it affect later behavior.
The type fixes the blocks, which routes are material, the empty-ledger form
for a system that only stores or serves content, the content and update
relations, the ledger and its controlled values, and the assessment limits;
follow its checking order and record `not determinable` where the
accessible evidence cannot individuate truth-apt content. Declare new records with `EPI-`; keep supplied `RT-` IDs
when assessing the same referents, and flag a needed supersession or a
defective supplied fact beside the finding it affects, with evidence.

Treat the runtime report as a starting account: check CLI dispatch, hooks,
registered tools and exposed operations against it, and trace material
evaluation, cleanup, rejection and withdrawal through their results and
consequential consumers, including operations the runtime omitted. Name a
target and its domain before judging its evaluator. For a deterministic text
transformation, trace a concrete input through the inspected code; the
finding rests on the `implementation` evidence layer as a deduction from
inspected code and needs no target execution.

## Boundaries

Cite your own declarations, `runtime` records, the Source register of
`boundary` and, in a correction round, any record `requests` supplies; the
output is refused with unresolved IDs otherwise. Assess distributed-parametric
state only from accessible sources and supplied execution evidence.

When `round = correction`, follow **Correct a report after verification** in
the supplied worker rules; this instruction still governs the report's
content.

Run the acceptance check before submitting.
