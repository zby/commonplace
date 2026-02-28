---
description: Structured templates like Evidence/Reasoning sections steer autoregressive generation toward higher-quality training data (scientific papers, legal analyses) rather than unstructured web text — the structure acts as a distribution selector
type: note
areas: [document-system]
status: seedling
---

# Structure activates higher-quality training distributions

LLMs are autoregressive — they produce text that continues the pattern in context. When the context contains sections like `## Evidence` and `## Reasoning`, the model's output will resemble the training data that had similar structure: scientific papers, legal analyses, peer-reviewed arguments. These documents are, on average, higher quality for reasoning purposes than the bulk of internet text.

The structure acts as a distribution selector. A free-form prompt might draw from blog posts, forum comments, or opinion pieces. A Toulmin-shaped template steers the model toward the subset of its training data where authors were already doing rigorous argumentation. We assume — reasonably — that scientific papers and formal arguments have better epistemic value for our purposes than unstructured web text.

This argument is independent of [failure-mode transfer](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md). Even if LLMs had no human-like failure modes at all, the distribution-selection effect would still apply: structured context activates structured training data, which tends to be higher quality. And it's independent of [readability for humans](./structured-output-is-easier-for-humans-to-review.md) — the quality improvement happens in the generation process itself, before any human reads the output.

---

Relevant Notes:
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](./human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — complementary: a first independent argument for structured types (failure-mode transfer rather than distribution selection)
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — complementary: a third independent argument (readability, not LLM-specific)
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — example: the Toulmin structure is one template that activates the distribution-selection effect
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview that links all three arguments as supporting the quality role of types

Topics:
- [document-system](./document-system.md)
