---
description: "Distinguishes functions and failure modes suggested by human cognition from the unsupported inference that an engineered agent should bundle the responsible roles along human boundaries."
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model]
---

# Human analogies can motivate functions without determining component boundaries

Humans are a familiar example of systems that remember, interpret, act, and adapt over time. Analogies to human cognition can therefore reveal a function an agent may need or a failure it may need to prevent. But because these functions appear unified in one person, the analogy can also lead designers to inherit a component decomposition before comparing alternatives.

The functional inference and the architectural inference are different. A human analogy may suggest that user-specific intent must persist, relevant experience must affect current action, or identity must remain coherent. Resemblance alone does not show that persistence, activation, interpretation, and action should occur in one engineered component. Their bundling in the human source constrains the target only when the target shares the causal dependencies that make the bundling effective.

Personalization makes this distinction visible. A human editor can remember a writer's aims and use them to interpret a terse new request. An agent system can reproduce similar behavior through several allocations. A model can interpret the request while live context or a retained artifact carries the aims. A context engine can activate the relevant record, while an authority policy or the user determines whether it still applies. User-specific aims or response patterns could instead be learned into model weights. Each option is an allocation hypothesis whose ability to preserve the required capacity must be tested. They differ in provenance, correction cost, portability across models, and ease of attributing failures. The resulting behavior may not reveal which allocation produced it; [memory-backed personalization can look like model improvement](./memory-backed-personalization-can-look-like-model-improvement.md).

Three questions should remain distinct even when their answers interact: Does the target need the function or share the failure mode? Does the human causal mechanism transfer? Where should the responsible roles be allocated? A mechanism that depends on shared state, recurrence, or joint adaptation constrains the answer to the third question. Restate any surviving function as the behavior and dependencies an implementation must preserve. Then compare candidate allocations against the target's consumer needs, available substrates, domain constraints, and machinery. These considerations narrow the choice without mechanically determining it. Comparing the resulting map with the allocation implied by the analogy preserves the functional hypothesis while exposing boundaries that still need warrant. If the function survives but the boundary moves, the function has support while the allocation remains a design choice.

Reopening allocation matters even when the borrowed category sounds technically natural. “Memory,” for example, spans storage, contextual activation, learning, and action; [agent memory is a crosscutting concern rather than a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md). Treating the human category as a single component can hide both the available design space and the distinct causes of failure.

This does not make separation automatically better. Coupling can reduce latency and interface costs, preserve shared representations, or enable joint optimization. Separation can improve provenance, replaceability, and controlled evaluation, but it adds coordination and consistency costs. A structurally grounded human analogy can support coupling when the target shares the relevant causal dependencies. Resemblance alone cannot establish the boundary.

---

Relevant Notes:

- [Psychology-to-agent transfer needs per-principle failure-mode testing](./psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — foundation: supplies the first transfer test, whether the target system shares the human failure mode
- [First-principles analysis maps a design space before selecting within it](./first-principles-analysis-maps-design-space-before-selection.md) — mechanism: supplies the rival-decomposition test for the proposed component boundary
- [Human-LLM differences are load-bearing for knowledge-system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — context: explains why neither wholesale adoption nor wholesale rejection of human conventions works
- [LLM learning phases fall between human learning modes rather than mapping onto them](./llm-learning-phases-fall-between-human-learning-modes.md) — exemplifies: human learning categories fail to preserve their boundaries across LLM training and context use
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) — grounds: states when an inherited boundary carries conditional warrant into a target domain
