---
description: Empirical demonstration that LLMs mirror human content effects on reasoning (syllogisms, NLI, Wason) — content bias survives scaling and instruction tuning but chain-of-thought partially restores content-independent reasoning
source_snapshot: language-models-like-humans-show-content-effects-on-reasoning-tasks.md
ingested: 2026-03-09
type: scientific-paper
domains: [cognitive-science, llm-reasoning, human-ai-comparison, dual-process-theory]
---

# Ingest: Language Models, Like Humans, Show Content Effects on Reasoning Tasks

Source: language-models-like-humans-show-content-effects-on-reasoning-tasks.md
Captured: 2026-03-08
From: https://academic.oup.com/pnasnexus/article/3/7/pgae233/7712372

## Classification
Type: scientific-paper — peer-reviewed in PNAS Nexus, systematic experiments across three reasoning tasks with statistical analyses, human participant studies, and multiple model evaluations.
Domains: cognitive-science, llm-reasoning, human-ai-comparison, dual-process-theory
Author: Andrew K Lampinen (DeepMind) et al., including James L McClelland (Stanford) — strong credentials in both computational cognitive science and deep learning. McClelland is a foundational figure in connectionist/PDP models of cognition.

## Summary

Lampinen et al. systematically test whether large language models exhibit the same "content effects" as humans on logical reasoning tasks — the tendency to reason more accurately when semantic content supports the correct logical inference. Across three tasks (natural language inference, syllogisms, Wason selection task), LMs mirror human accuracy patterns: both perform better on familiar/believable content and worse on abstract or belief-violating content. Model confidence correlates negatively with human response times on the same problems, even after controlling for task variables and accuracy. The key divergence is the Wason selection task, where LMs generally outperform humans and show a different error distribution (fewer matching-bias errors, more antecedent-false errors). Chain-of-thought prompting can partially restore content-independent reasoning in strong models by improving performance on abstract/unfamiliar conditions without degrading familiar ones. The authors argue these findings show dual-system-like behavior can emerge from a single system without explicit symbolic reasoning, and that content effects may arise from training on human-generated text reflecting real-world statistical regularities. Content effects survive instruction tuning (Flan-PaLM 2) and scale (larger models are more accurate but not less content-biased).

## Connections Found

The `/connect` discovery identified four genuine connections in the KB — three previously established and one new:

1. **[human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md)** — grounds: This paper provides direct empirical evidence for the note's central claim that LLMs exhibit human-like failure modes. Content effects across three reasoning tasks, with quantifiable confidence/RT correlations, move the claim from speculative toward empirically supported. The Wason divergence marks a concrete boundary where the overlap breaks down.

2. **[human-llm-differences-are-load-bearing-for-knowledge-system-design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)** — exemplifies: The paper is a worked example of the per-convention evaluation methodology the note advocates. Syllogisms and NLI show shared failure modes (convention transfers); the Wason task shows divergent error patterns (convention may not transfer). This is exactly the granular, convention-by-convention analysis the note calls for.

3. **[first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md)** — extends: Content effects are the empirical manifestation of adaptive fit dominating explanatory reach in reasoning. Chain-of-thought partially restoring content-independent reasoning suggests a concrete mechanism for moving from adaptive to explanatory reasoning.

4. **[structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md)** — grounds (new connection): The paper's chain-of-thought finding directly evidences the distribution-selection thesis. CoT reduces content bias by improving performance on abstract/unfamiliar conditions without degrading familiar ones — structured reasoning context shifts the model away from its content-biased default distribution toward content-independent logical reasoning. The finding that content effects survive both scaling and instruction tuning strengthens the argument that distribution selection via structural intervention is a permanent architectural need, not a stopgap pending better models.

Two synthesis opportunities were flagged by `/connect`:
- **Content-bias decorrelation**: Content effects are shared across architecturally different models (Chinchilla, PaLM 2, GPT-3.5), implying model diversity alone is insufficient for decorrelating reasoning errors. Decorrelation strategies need to vary semantic framing (e.g., metamorphic checks that rephrase content), not just the model. This connects to [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md).
- **Scaling vs structured intervention**: Content effects surviving scaling and instruction tuning means structural interventions (templates, Toulmin sections) are not a temporary measure — they are permanent architecture because content bias does not dissolve with scale.

## Extractable Value

1. **Confidence-RT correlation as a transfer diagnostic**: LM confidence on reasoning problems correlates with human response times even after controlling for task variables and accuracy. This could serve as a quantitative test for whether a specific cognitive convention transfers to LLMs — if difficulty profiles align, the convention likely transfers. [experiment]

2. **Chain-of-thought as distribution-selection evidence**: CoT reduces content bias by improving performance on abstract/belief-violating conditions without degrading familiar ones. This is the strongest empirical support yet for [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md) — structured prompting shifts the model's generation distribution rather than just constraining output format. [quick-win]

3. **Content effects shared across model families as a decorrelation constraint**: Chinchilla, PaLM 2, and GPT-3.5 all show the same content biases despite different architectures and training data. For [error correction](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), this means model diversity alone cannot decorrelate reasoning errors. Decorrelation requires varying the semantic framing of the check, not just the checker. [experiment]

4. **Wason divergence as a transfer boundary marker**: Humans show matching bias on the Wason task; LMs show a qualitatively different error pattern (antecedent-false errors). A concrete example where a human cognitive convention does NOT transfer — useful as a worked counterexample for the per-convention transfer methodology. [just-a-reference]

5. **Single-system dual-process behavior**: A single transformer exhibits both "fast" (content-biased) and "slow" (content-independent with CoT) reasoning without an explicit symbolic System 2. Challenges the common claim that LLMs are "System 1 only" and need external symbolic augmentation. [deep-dive]

6. **Content effects survive instruction tuning and scaling**: Flan-PaLM 2 and GPT-3.5 show the same content effects as base models. Larger models are more accurate overall but not less content-biased. This means RLHF and scale do not address content bias — structured prompting is required. [quick-win]

7. **Two hypotheses for content effect origins**: (a) Direct imitation of human error patterns from training data, or (b) convergent evolution from shared statistical structure of experience. These map onto different predictions about whether novel structured formats (not in training data) can escape content bias. [deep-dive]

## Limitations (our opinion)

**What was not tested:**

- **No metamorphic or rephrasing-based interventions**: The paper tests chain-of-thought but not other structured interventions (Toulmin templates, evidence/reasoning separation, rephrased checks). Given the KB's interest in distribution selection via structural templates, the CoT finding is suggestive but does not directly test whether domain-specific structured formats (as opposed to generic "think step by step") produce the same content-bias reduction.

- **Models tested are now two generations old**: Chinchilla, PaLM 2, and GPT-3.5 were state-of-the-art in 2023-2024. The authors tested "several newer Gemini models" and found similar effects, but the paper does not evaluate models with substantially different training regimes (e.g., models trained with extended reasoning, process reward models, or models like o1/o3 that use internal chain-of-thought). Whether content effects persist in these architectures is an open question.

- **Only three reasoning tasks, all deductive**: NLI, syllogisms, and Wason are all formal deductive logic problems. The paper acknowledges this limitation. Content effects are documented in humans across inductive, probabilistic, and causal reasoning as well — the paper's finding may understate the breadth of the phenomenon.

- **No investigation of content effect magnitude by domain**: The paper varies content (believable vs unbelievable vs nonsense) but does not examine whether some semantic domains produce stronger content effects than others. For KB design, knowing which domains are most susceptible to content bias would be more actionable than knowing that content bias exists.

- **Human sample is UK-only, crowd-sourced, with low Wason performance**: Participants were UK-based, recruited via a crowd-sourcing platform, with no control for logical training. The human baseline on the Wason task (not significantly above chance) is lower than some prior studies, making the human-model comparison on that task hard to interpret. The paper does not examine individual differences in logical education, which past work shows strongly affects Wason performance.

- **The "imitation vs convergence" question is left open**: The two hypotheses for why content effects arise (copying human errors from training data vs convergent evolution from shared statistical regularities) are stated but not tested. This is the most important mechanistic question — if content effects are convergent, novel structured formats should still be subject to them; if they are imitative, novel formats might escape them.

## Recommended Next Action

Update [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md): add this paper as a third empirical source. The CoT finding (structured prompting reduces content bias by improving abstract/unfamiliar performance without degrading familiar performance) is direct evidence for the distribution-selection mechanism, and the scaling/instruction-tuning robustness finding (content effects survive both) strengthens the argument that distribution selection is a permanent architectural need. This would move the note's status question forward — it currently stays "seedling" due to limited evidence, and this paper adds a meaningful data point from a different domain (reasoning tasks vs code verification).
