---
description: "Job of an analyse-agentic-system run: the memory specialist, first pass or correction round"
type: types/instruction.md
---

# Analyse memory and context as the specialist

Follow [Analyse agent memory](../../analyse-agent-memory.md) with the run's frozen `memory-input.md`. Your report goes to the output path your prompt names, not to `memory-report.md`; code copies the last accepted round there. The parent it names is this run's reconciliation.

In a correction round your prompt names the previous report and the reconciliation that returned findings to you. Answer each returned finding from the sources: correct the report where the finding holds, and keep your finding with its evidence where it does not. Write the whole report again; the round's report replaces the previous one.
