---
description: Routing instructions serve the current task; periodic hygiene is triggered externally (user, heartbeat, CI), so embedding it in always-loaded routing blurs two responsibilities and adds session noise
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance]
---

# Periodic KB hygiene should be externally triggered, not embedded in routing

Routing and periodic hygiene answer to different triggers. Routing serves the current task — where content goes, which type to use, which docs to open next — so it is keyed to what the agent is doing now. Periodic hygiene is triggered by something outside the task entirely: a user request, a heartbeat job, or CI. Even a hygiene check that were always relevant would not belong in routing, because nothing in the current task calls for it.

That trigger mismatch is the reason to keep periodic operations out of always-loaded routing instructions. The two carry distinct responsibilities:

- Routing: "what to do now for this task"
- Operations: "what to audit from time to time"

Embedding operations in routing also collides with loading frequency — always-loaded context competes for attention every session (see [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md)), so a low-frequency check pays a per-session cost while helping only occasionally.

Separating them keeps the default path lightweight without losing the maintenance playbook. The playbook itself lives in [maintenance-operations-catalogue-should-stage-stable-procedures](./maintenance-operations-catalogue-should-stage-stable-procedures.md), the staging ground for operations before they are worked into `kb/instructions/` — compressed into a use-shaped instruction.

---

Relevant Notes:

- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — the general principle this note applies: the trigger-source argument compounds the loading-frequency cost of always-loaded context
- [maintenance-operations-catalogue-should-stage-stable-procedures](./maintenance-operations-catalogue-should-stage-stable-procedures.md) — operationalizes this by collecting periodic checks and tracking which ones are ready to become instructions
- [skills are instructions plus routing and execution policy](./skills-are-instructions-plus-routing-and-execution-policy.md) — defines the target artifact for procedures that mature beyond note-level catalogues
