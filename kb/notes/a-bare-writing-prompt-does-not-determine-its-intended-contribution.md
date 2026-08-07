---
description: "Separates the contribution a bare writing prompt leaves underdetermined from empirical claims about how experts and LLMs supply the missing purpose."
type: kb/types/note.md
traits: [title-as-claim]
tags: [llm-reliability, computational-model]
---

# A bare writing prompt does not determine its intended contribution

“Write an article about X” specifies a topic and output form, but not an angle, thesis, audience, or contribution. Because mutually incompatible articles satisfy the instruction, the prompt alone cannot determine which contribution is intended. Choosing one requires information or priors beyond its literal content.

A commissioned expert also brings their knowledge and agenda, and may read the commission as a request to exercise that judgment. An LLM brings different priors and may instead generate generic topical prose. Identical prompt text can therefore induce different effective tasks.

## Empirical Question

Experiments should test how reliably experts and LLMs infer the richer commission, and how explicit purpose, expert-persona prompting, retrieval, or additional inference effort affects the result.

---

Relevant Notes:

- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — exemplifies: a bare writing prompt admits many valid contributions and therefore cannot identify one without additional context
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — contrasts: activating relevant facts is distinct from constructing the purpose that selects and organizes them

Operationalized into:

- [cp-skill-write](../instructions/cp-skill-write/SKILL.md) — requires an artifact-specific contribution to be determined before ordinary drafting
- [cp-skill-write-multistage](../instructions/cp-skill-write-multistage/SKILL.md) — makes unresolved intent a brief-stage blocker rather than a choice for reconstruction
