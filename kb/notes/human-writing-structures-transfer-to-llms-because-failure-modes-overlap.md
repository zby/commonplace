---
description: Human writing genres evolved to prevent specific reasoning failures; the same structures help LLMs because LLMs exhibit surprisingly human-like failure modes (conflating evidence with opinion, skipping qualifications) — suggesting per-structure transfer evaluation rather than wholesale analogy
type: note
areas: [document-system]
status: seedling
---

# Human writing structures transfer to LLMs because failure modes overlap

Human writing genres — Toulmin argumentation, scientific paper structure, legal brief format — evolved under selection pressure. They exist because they help humans avoid specific reasoning failures. The Toulmin scaffold, for instance, forces the writer to separate evidence from reasoning and to surface assumptions.

The naive transfer argument ("it helps humans, so it helps LLMs") is weak because LLMs are not humans. But it becomes stronger when we observe that LLMs exhibit surprisingly human-like failure modes: they get distracted by irrelevant context, they conflate evidence with opinion, they skip qualifications when the argument feels strong. These failures are "un-machine-like" — you wouldn't expect a computational system to get distracted — but they happen.

This overlap suggests a methodology: rather than assuming wholesale transfer, **evaluate the specific arguments for why a structure helps humans, and check whether each argument applies to LLMs.** For Toulmin, the argument is "separating evidence from warrant prevents conflation" — and LLMs do conflate evidence with warrant. For scientific paper structure, the argument is "methods sections enable reproducibility" — which may be less relevant for LLMs.

This is still speculative and would require empirical verification, but it's more principled than blind analogy. The methodology applies beyond Toulmin: any human writing convention proposed for LLM use should be evaluated by asking "what specific failure does this prevent, and does the LLM exhibit that failure?"

---

Relevant Notes:
- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — foundation: the specific Toulmin structure this note argues transfers to LLMs
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — extends: adds a new category of transfer — not just programming practices but writing genre conventions
- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — complementary: a second independent argument for structured types with LLMs (distribution selection rather than failure-mode transfer)
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — complementary: a third independent argument (readability, not LLM-specific at all)
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview that links all three arguments as supporting the quality role of types

Topics:
- [document-system](./document-system.md)
