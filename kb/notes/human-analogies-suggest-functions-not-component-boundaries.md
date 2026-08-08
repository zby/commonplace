---
description: "Separates functions and failure modes suggested by human cognition from the unsupported inference that an engineered agent should bundle the responsible roles along human boundaries."
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model]
---

# Human analogies can motivate functions without determining component boundaries

Humans are a familiar example of systems that remember, interpret, act, and adapt over time. Analogies to human cognition can therefore expose a function an agent may need or a failure it may need to prevent. They have outsized architectural influence because these functions appear unified in one person: the analogy often supplies a decomposition before the designer has compared alternatives.

The useful inference and the architectural inference are different. A human analogy may suggest that user-specific intent must persist, relevant experience must affect current action, or an identity must remain coherent. It does not by itself show that persistence, activation, interpretation, and action should occur in one engineered component. The fact that these functions arrive bundled in one organism is a fact about the source of the analogy, not an inherited constraint of an LLM agent system.

Personalization makes the distinction visible. A human editor can remember a writer's aims and interpret a terse new request. An agent system can reproduce that behavior through several allocations: a model can interpret the request; live context or a retained artifact can carry the aims; a context engine can activate the relevant record; an authority policy or the user can resolve whether it still applies. Some of this could instead be learned into model weights. The user-visible function is similar, but the alternatives differ in provenance, correction cost, portability across models, and failure attribution. This is why [memory-backed personalization can look like model improvement](./memory-backed-personalization-can-look-like-model-improvement.md).

Three questions should not collapse: does the target system need the function or share the failure mode, does the human causal mechanism transfer, and where should the responsible roles be allocated? Restate a surviving function as causal obligations and derive an allocation from the engineered system's own consumer, substrate, domain, and machinery commitments. Comparing this map with the analogy-supplied allocation preserves useful insight while exposing borrowed seams. If the function survives but the boundary moves, the function has support and the allocation remains a design choice.

This second step matters even when the borrowed category sounds technically natural. “Memory,” for example, crosses storage, contextual activation, learning, and action; [agent memory is a crosscutting concern rather than a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md). Treating the human word as one component can hide both the relevant design space and the distinct causes of failure.

None of this makes separation automatically better. Coupling can reduce latency and interface cost, preserve a shared representation, or enable joint optimization; separation can improve provenance, replaceability, and controlled evaluation while adding coordination and consistency costs. A human-like component boundary may be the best design, but resemblance alone does not establish it.

---

Relevant Notes:

- [Psychology-to-agent transfer needs per-principle failure-mode testing](./psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — foundation: supplies the first transfer test, whether the target system shares the human failure mode
- [First-principles analysis maps a design space before selecting within it](./first-principles-analysis-maps-design-space-before-selection.md) — mechanism: supplies the rival-decomposition test for the proposed component boundary
- [Human-LLM differences are load-bearing for knowledge-system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — context: explains why neither wholesale adoption nor wholesale rejection of human conventions works
- [LLM learning phases fall between human learning modes rather than mapping onto them](./llm-learning-phases-fall-between-human-learning-modes.md) — exemplifies: human learning categories fail to preserve their boundaries across LLM training and context use
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — exemplifies: one familiar label decomposes into roles distributed across an engineered agent system
