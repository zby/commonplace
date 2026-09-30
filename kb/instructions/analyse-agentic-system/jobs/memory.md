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

Follow [Analyse agent memory](../../analyse-agent-memory.md) with `boundary` and `runtime`. Your report goes to `output`; code copies the round the reconciliation accepts to `output/memory.md` byte for byte, as the set's memory member. The parent it names is this run's reconciliation. Your output is refused while it is not a valid member or cites a record that neither it, `runtime` nor the Source register declares; a correction round may also cite records `epistemic` declares.

When `round = correction`, read `previous-memory`, `returned-findings`, and `epistemic`. Answer each returned finding from the sources: correct the report where the finding holds, and keep your finding with its evidence where it does not. Write the whole report again; the round's report replaces the previous one.
