---
description: Capability artifacts should be placed by autonomy readiness so AGENTS.md stays free of inventories and only routes or constrains behavior
type: note
traits: []
areas: [kb-design]
status: current
---

# Capability placement should follow autonomy readiness

Capability placement is a separate decision from AGENTS.md control-plane design. The organizing variable is **autonomy readiness**: how safely and reliably the agent can execute a capability without human steering.

## Decision rule

- **Ready for autonomous use** -> promote to **skills** (harness-discovered/injected).
- **Reusable but not autonomous-ready** -> keep as **instruction** (`kb/instructions/`) invoked explicitly by user direction.
- **Exploratory or unstable** -> keep as **methodology/operations notes** while patterns are still forming.

## Consequence for AGENTS.md

AGENTS.md should not carry capability inventories. If a capability is autonomy-ready, the harness exposes it through skills. If it is not autonomy-ready, AGENTS.md should not advertise it as if it were routine runtime machinery.

AGENTS.md may still contain minimal routing pointers ("for X, read Y") when omission would create high-cost failure, but not catalogues of what the system can do.

## Migration path

1. Capture an operation in notes/catalogues during exploration.
2. Distill stable procedure into `kb/instructions/`.
3. Promote to skill only after repeated successful autonomous execution.
4. Remove obsolete pointers once harness discovery is sufficient.

This sequence prevents premature automation while avoiding AGENTS.md bloat.

---

Relevant Notes:

- [agents-md-should-be-organized-as-a-control-plane](./agents-md-should-be-organized-as-a-control-plane.md) — parent framing: AGENTS.md is control-plane runtime context, not capability catalog space
- [instructions-are-skills-without-automatic-routing](./instructions-are-skills-without-automatic-routing.md) — defines the intermediate form between notes and skills
- [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — concrete staging area for operations before they are distilled
- [skills-derive-from-methodology-through-distillation](./skills-derive-from-methodology-through-distillation.md) — theoretical basis for promotion from reasoning artifacts to execution artifacts

Topics:

- [kb-design](./kb-design.md)
