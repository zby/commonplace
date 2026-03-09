---
description: Structured templates like Evidence/Reasoning sections steer autoregressive generation toward higher-quality training data (scientific papers, legal analyses) rather than unstructured web text — the structure acts as a distribution selector
type: note
traits: [has-external-sources]
areas: [type-system]
status: seedling
---

# Structure activates higher-quality training distributions

LLMs are autoregressive — they produce text that continues the pattern in context. When the context contains sections like `## Evidence` and `## Reasoning`, the model's output will resemble the training data that had similar structure: scientific papers, legal analyses, peer-reviewed arguments. These documents are, on average, higher quality for reasoning purposes than the bulk of internet text.

The structure acts as a distribution selector. A free-form prompt might draw from blog posts, forum comments, or opinion pieces. A Toulmin-shaped template steers the model toward the subset of its training data where authors were already doing rigorous argumentation. We assume — reasonably — that scientific papers and formal arguments have better epistemic value for our purposes than unstructured web text.

This argument is independent of [failure-mode transfer](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md). Even if LLMs had no human-like failure modes at all, the distribution-selection effect would still apply: structured context activates structured training data, which tends to be higher quality. And it's independent of [readability for humans](./structured-output-is-easier-for-humans-to-review.md) — the quality improvement happens in the generation process itself, before any human reads the output.

The epiplexity framework ([Finzi et al., 2026](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md)) provides formal grounding. Epiplexity measures structurally learnable content within computational bounds, and one of its core results is that data ordering affects learning — the same data presented in different arrangements exposes different extractable structure to a bounded learner. Structured templates work by the same mechanism: they reorder and partition the generation task so that at each point, the model's bounded computation can extract more structure from its training distribution. The distribution-selection metaphor is what epiplexity formalises.

**Status note:** This stays seedling deliberately. The distribution-selection mechanism is partially supported but not confirmed. [Ugare & Chandra (2026)](../sources/agentic-code-reasoning.ingest.md) show that semi-formal reasoning templates yield 5-12pp accuracy gains on code verification tasks — direct evidence that structured templates improve output quality beyond what unconstrained reasoning achieves. However, the same paper shows Sonnet gains nothing from templates on code QA (84.8% vs 85.3%), and past experience with `structured-claim` type showed that imposing structure can degrade quality.

[Lampinen et al. (2024)](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) add evidence from a different domain: LLMs exhibit human-like content effects on reasoning tasks (performing better when semantic content supports the correct inference), and chain-of-thought prompting partially restores content-independent reasoning — improving performance on abstract/unfamiliar conditions without degrading familiar ones. This is the distribution-selection effect observed directly: structured prompting shifts generation away from the content-biased default toward content-independent logical reasoning. Crucially, content effects survive both scaling (larger models are more accurate but equally content-biased) and instruction tuning (Flan-PaLM 2, GPT-3.5), which strengthens the case that structural intervention is permanent architecture rather than a stopgap pending better models.

The epiplexity connection is suggestive but doesn't confirm the causal claim that the mechanism is distribution selection rather than simply constraining output format. The evidence supports "structure helps, and the need for it doesn't dissolve with scale" but not the stronger thesis that it works specifically via activating higher-quality training subsets.

---

Sources:
- Finzi et al. (2026). [From entropy to epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md) — formalises why data ordering and structure affect extractable information for bounded learners.
- Ugare & Chandra (2026). [Agentic Code Reasoning](../sources/agentic-code-reasoning.ingest.md) — semi-formal templates yield 5-12pp gains on code verification; partial empirical support for the distribution-selection thesis, with a boundary condition (Sonnet non-improvement on code QA).
- Lampinen et al. (2024). [Content Effects on Reasoning Tasks](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) — CoT reduces content bias on abstract/unfamiliar conditions without degrading familiar ones; content effects survive scaling and instruction tuning, evidencing that structural intervention is a permanent need.

Relevant Notes:

- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — complementary: a first independent argument for structured types (failure-mode transfer rather than distribution selection)
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — complementary: a third independent argument (readability, not LLM-specific)
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — example: the Toulmin structure is one template that activates the distribution-selection effect
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview that links all three arguments as supporting the quality role of types
- [agentic code reasoning](../sources/agentic-code-reasoning.ingest.md) — grounds: 5-12pp gains from semi-formal templates provide partial empirical support; Sonnet's non-improvement on code QA surfaces a boundary condition
- [content effects on reasoning tasks](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) — grounds: CoT reduces content bias without degrading familiar performance; content effects survive scaling and instruction tuning, supporting structural intervention as permanent architecture
- [process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md) — refines: the distribution-selection effect applies differently to process constraints (activating rigorous reasoning) and output constraints (activating formally structured training data)
- [Toulmin Argument (Purdue OWL)](../sources/purdue-owl-toulmin-argument.md) — source: the canonical argumentation framework behind the "Toulmin-shaped template" referenced here

Topics:

- [type-system](./type-system.md)
