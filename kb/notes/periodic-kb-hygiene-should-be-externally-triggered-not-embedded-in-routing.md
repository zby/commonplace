---
description: Periodic hygiene checks belong in externally triggered operations (user request, scheduler, CI), not in always-loaded routing instructions
type: note
traits: []
areas: [kb-design]
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
- [context-loading-strategy](./context-loading-strategy.md) — extends this by applying always-loaded vs on-demand loading to maintenance operations
- [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — operationalizes this by collecting periodic checks and their distillation status
- [instructions-are-skills-without-automatic-routing](./instructions-are-skills-without-automatic-routing.md) — defines the target artifact for procedures that mature beyond note-level catalogues

Topics:
- [kb-design](./kb-design.md)
