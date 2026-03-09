---
description: Human writing genres evolved to prevent specific reasoning failures; the same structures help LLMs because LLMs exhibit empirically demonstrated human-like failure modes (content effects on reasoning) — per-convention transfer evaluation, not wholesale analogy
type: note
traits: [has-external-sources]
areas: [type-system]
status: current
---

# Human writing structures transfer to LLMs because failure modes overlap

Human writing genres — Toulmin argumentation, scientific paper structure, legal brief format — evolved under selection pressure. They exist because they help humans avoid specific reasoning failures. The Toulmin scaffold, for instance, forces the writer to separate evidence from reasoning and to surface assumptions.

The naive transfer argument ("it helps humans, so it helps LLMs") is weak because LLMs are not humans. But it becomes stronger when we observe that LLMs exhibit surprisingly human-like failure modes: they get distracted by irrelevant context, they conflate evidence with opinion, they skip qualifications when the argument feels strong. These failures are "un-machine-like" — you wouldn't expect a computational system to get distracted — but they happen.

This overlap suggests a methodology: rather than assuming wholesale transfer, **evaluate the specific arguments for why a structure helps humans, and check whether each argument applies to LLMs.** For Toulmin, the argument is "separating evidence from warrant prevents conflation" — and LLMs do conflate evidence with warrant. For scientific paper structure, the argument is "methods sections enable reproducibility" — which may be less relevant for LLMs.

Empirical evidence supports this overlap. [Lampinen et al. (2024)](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md) tested LLMs on three reasoning tasks (syllogisms, the Linda problem, the Wason selection task) and found that LLMs mirror human accuracy patterns — both perform better on familiar/believable content and worse on abstract or belief-violating content. LLM confidence even correlates with human response times on the same problems. The overlap is real but not universal: on the Wason selection task, LLMs show qualitatively different error patterns (antecedent-false errors rather than matching bias), marking a concrete boundary where human conventions may not transfer.

Chain-of-thought prompting reduces content bias by improving performance on abstract/unfamiliar conditions without degrading familiar ones — suggesting that structured prompting pushes toward content-independent reasoning. This is directly relevant: the structured templates in this KB (Toulmin sections, Evidence/Reasoning/Caveats) may work by a similar mechanism, forcing the model past content-biased defaults.

The methodology applies beyond Toulmin: any human writing convention proposed for LLM use should be evaluated by asking "what specific failure does this prevent, and does the LLM exhibit that failure?" The Lampinen results show this must be done per-convention — syllogisms and NLI show shared failure modes (convention transfers), while the Wason task shows divergence (convention may not transfer).

---

Relevant Notes:

- [claim notes should use Toulmin-derived sections](./claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md) — foundation: the specific Toulmin structure this note argues transfers to LLMs
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — extends: adds a new category of transfer — not just programming practices but writing genre conventions
- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — complementary: a second independent argument for structured types with LLMs (distribution selection rather than failure-mode transfer)
- [structured-output-is-easier-for-humans-to-review](./structured-output-is-easier-for-humans-to-review.md) — complementary: a third independent argument (readability, not LLM-specific at all)
- [why-notes-have-types](./why-notes-have-types.md) — context: the overview that links all three arguments as supporting the quality role of types
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md) — evidence: empirical demonstration of human-like content effects across three reasoning tasks, with Wason divergence as a transfer boundary
- [Toulmin Argument (Purdue OWL)](../sources/purdue-owl-toulmin-argument.md) — source: the formal argumentation model used as the primary running example throughout this note

Topics:

- [type-system](./type-system.md)
