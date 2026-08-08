---
description: "Separates the contribution a bare writing prompt leaves underdetermined from empirical claims about how experts and LLMs supply the missing purpose."
type: kb/types/note.md
traits: [title-as-claim]
tags: [llm-reliability, computational-model]
---

# A bare writing prompt does not determine its intended contribution

“Write an article about X” specifies a topic and output form, but not an angle, thesis, audience, or contribution. Because mutually incompatible articles satisfy the instruction, the prompt alone cannot determine which contribution is intended. Identifying the intended one requires information beyond its literal content.

A commissioned expert also brings their knowledge and agenda, and may read the commission as a request to exercise that judgment. An LLM brings different priors and may instead generate generic topical prose. Identical prompt text can therefore induce different effective tasks.

Past interaction can also supply the missing information. If a system retrieves it, the combined input may determine a commission even though the bare prompt does not. [Memory-backed personalization can look like model improvement](./memory-backed-personalization-can-look-like-model-improvement.md) develops that separate architectural consequence.

## Empirical Question

Experiments should test how reliably experts and LLMs infer the richer commission, and how explicit purpose, expert-persona prompting, retrieved memory, or additional inference effort affects the result.

---

Relevant Notes:

- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — exemplifies: a bare writing prompt admits many valid contributions and therefore cannot identify one without additional context
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — mechanism: retained intent can complete a bare commission only when the memory path activates it for the write
- [LLM output deviation has three sources with non-substitutable remedies](./llm-output-deviation-has-three-sources-with-non-substitutable.md) — extends: model improvement repairs interpreter failure, not information missing from the available specification and context

Operationalized into:

- [cp-skill-write](../instructions/cp-skill-write/SKILL.md) — requires an artifact-specific contribution to be determined before ordinary drafting
- [cp-skill-write-multistage](../instructions/cp-skill-write-multistage/SKILL.md) — makes unresolved intent a brief-stage blocker rather than a choice for reconstruction
- [Run a full improvement pass on one note](../instructions/run-full-improvement-pass-on-note.md) — treats an unresolved contribution as a specification gap and leaves the note unchanged
