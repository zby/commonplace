---
description: "Job of an analyse-agentic-system run: trace and challenge the runtime baseline and write the set's runtime member"
type: types/instruction.md
---

# Trace and challenge the runtime baseline

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first` or `correction`. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `previous-report` | Absolute path of your report as the record verifier judged it. | `correction` |
| `requests` | Absolute path of the blockers addressed to your report, with the current declarations of the records they cite from other reports. | `correction` |
| `answers` | Absolute path where you write your answers to those blockers. | `correction` |

## Situation

An analysis run of `system` has frozen its evidence boundary in `boundary`.
Nothing has yet been established about how the system runs. The memory and
epistemic analysts will start from your report, and a reconciler and an
independent verifier will read it against the frozen source.

## Mission

Write the runtime report to `output` under the supplied runtime type, within
`boundary`, so that the later analysts have a source-grounded account of the
consequential claimed work, the shipped entry paths, one ordinary invocation
traced end to end, the material routes, the load-bearing guarantees and their
enforcement points, the distributed-parametric components, and the mechanisms
that admit changes to the product, retained knowledge, capabilities or
production machinery. Declare runtime records with `RT-` under the shared
record contract; the type fixes the fields each kind of record carries.

A guarantee covers only the paths its enforcement point covers, so judge it
after enumerating the materially equivalent alternate paths: direct model
calls, provider-native tools, host callbacks, shell access, extension code,
subprocesses or remote workers, manual graph control, and durable variants.
Inspect the smallest warranted set of forcing cases, ordinarily two to four
for a full code-grounded analysis, and state what remains unobserved.
Distinguish the capability surface, the current grant set and the deployed
isolation envelope. Leave memory revisions to the memory analyst.

## Boundaries

Cite your own declarations, the Source register of `boundary` and, in a
correction round, any record `requests` supplies; the output is refused with
unresolved IDs otherwise. Read evidence only from the frozen source.

When `round = correction`, follow **Correct a report after verification** in
the supplied worker rules; this instruction still governs the report's
content.

Run the acceptance check before submitting.
