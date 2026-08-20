---
description: "Distinguishes functions and failure modes suggested by human cognition from the unsupported inference that an engineered agent should bundle the responsible roles along human boundaries."
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model]
---

# Human analogies can motivate functions without determining component boundaries

Humans are a familiar example of systems that remember, interpret, act, and adapt over time. Analogies to human cognition can therefore suggest a function an agent may need or a failure it may need to prevent. Because those functions appear unified in one person, however, the analogy can also lead designers to inherit a component decomposition before comparing alternatives.

The functional inference and the architectural inference are different. A human analogy may suggest that user-specific intent must persist, relevant experience must affect current action, or identity must remain coherent. Resemblance alone does not show that persistence, activation, interpretation, and action should occur in one engineered component. Their bundling in humans constrains the target architecture only when the target shares the causal dependencies that make such coupling useful. Familiar labels can conceal this distinction. “Memory,” for example, spans storage, contextual activation, learning, and action because [agent memory is a crosscutting concern rather than a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md).

Personalization makes the distinction visible. A human editor can remember a writer's aims and use them to interpret a terse new request. An agent system can reproduce similar behavior through several allocations. A model may interpret the request from live context or a retained artifact that carries the aims. A context engine may activate the relevant record, while a separate policy—or the user—decides which source may govern current behavior. Alternatively, user-specific aims or response patterns may be learned into model weights. Each allocation is a hypothesis about how to preserve the required capacity and must be tested. The options differ in provenance, correction cost, portability across models, and ease of attributing failures. Behavior alone may not reveal which allocation produced it because [memory-backed personalization can look like model improvement](./memory-backed-personalization-can-look-like-model-improvement.md).

Three questions should remain distinct even when their answers interact: Does the target need the function or share the failure mode? Does the human causal mechanism transfer? Where should the responsible roles be allocated? When a transferable mechanism depends on shared state, recurrence, or joint adaptation, those dependencies constrain the third answer. Restate any surviving function as the behavior and dependencies an implementation must preserve. Then compare candidate allocations against the needs of the target's consumers, feasible media such as context, artifacts, or model weights, domain constraints, and available orchestration machinery. These considerations can narrow the choice without determining it. Finally, compare this map with the allocation implied by the analogy. If the function survives but the boundary moves, the function has support while the inherited allocation remains a design choice.

Nor is separation always better. Coupling can reduce latency and interface costs, preserve shared representations, or enable joint optimization. Separation can improve provenance, replaceability, and controlled evaluation, but it adds coordination and consistency costs. A human analogy can support coupling when structural comparison shows that the target shares the relevant causal dependencies. Resemblance alone cannot establish the boundary.

---

Relevant Notes:

- [Psychology-to-agent transfer needs per-principle failure-mode testing](./psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — grounds: supplies the first transfer test, whether the target system shares the human failure mode
- [First-principles analysis maps a design space before selecting within it](./first-principles-analysis-maps-design-space-before-selection.md) — mechanism: supplies the rival-decomposition test for the proposed component boundary
- [Human-LLM differences are load-bearing for knowledge-system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — grounds: explains why neither wholesale adoption nor wholesale rejection of human conventions works
- [LLM learning phases fall between human learning modes rather than mapping onto them](./llm-learning-phases-fall-between-human-learning-modes.md) — evidenced-by: human learning categories fail to preserve their boundaries across LLM training and context use
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md) — grounds: states when an inherited boundary carries conditional warrant into a target domain
