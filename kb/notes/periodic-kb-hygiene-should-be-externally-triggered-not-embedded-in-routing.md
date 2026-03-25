---
description: Routing instructions load every session for high-frequency decisions; periodic hygiene adds noise on every session while helping only occasionally, blurring routing and operations
type: note
traits: []
tags: [kb-maintenance]
status: current
---

# Periodic KB hygiene should be externally triggered, not embedded in routing

Routing instructions are loaded every session, so they should optimize for high-frequency decisions: where content goes, which type to use, and which docs to open next. Periodic hygiene checks are different. They are low-frequency operational maintenance and are typically triggered by something external: a user request, a heartbeat job, or CI.

Placing periodic operations inside always-loaded routing instructions adds instruction noise on every session while helping only occasionally. It also blurs two responsibilities:

- Routing: "what to do now for this task"
- Operations: "what to audit from time to time"

The separation keeps the default path lightweight without losing the maintenance playbook. The playbook itself lives in [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md), which is the staging ground for operations before promotion into `kb/instructions/`.

---

Relevant Notes:

- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — extends this by applying always-loaded vs on-demand loading to maintenance operations
- [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — operationalizes this by collecting periodic checks and their distillation status
- [skills are instructions plus routing and execution policy](./skills-are-instructions-plus-routing-and-execution-policy.md) — defines the target artifact for procedures that mature beyond note-level catalogues
