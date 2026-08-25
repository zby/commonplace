---
description: Empirical demonstration that LLMs mirror human content effects on reasoning (syllogisms, NLI, Wason) — content bias survives scaling and instruction tuning but chain-of-thought partially restores content-independent reasoning
source: https://academic.oup.com/pnasnexus/article/3/7/pgae233/7712372
captured: "2026-03-08"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: cfd34d847c87ad80812295940b4ea41c8a5c49f1b09ba25c1edaf69ce09e9faa
ingested: "2026-03-09"
type: kb/sources/types/ingest-report.md
domains: [cognitive-science, llm-reasoning, human-ai-comparison, dual-process-theory]
---

# Ingest: Language Models, Like Humans, Show Content Effects on Reasoning Tasks

## Classification
Peer-reviewed in PNAS Nexus, systematic experiments across three reasoning tasks with statistical analyses, human participant studies, and multiple model evaluations.
Author: Andrew K Lampinen (DeepMind) et al., including James L McClelland (Stanford) — strong credentials in both computational cognitive science and deep learning. McClelland is a foundational figure in connectionist/PDP models of cognition.

## Summary

Lampinen et al. systematically test whether large language models exhibit the same "content effects" as humans on logical reasoning tasks — the tendency to reason more accurately when semantic content supports the correct logical inference. Across three tasks (natural language inference, syllogisms, Wason selection task), LMs mirror human accuracy patterns: both perform better on familiar/believable content and worse on abstract or belief-violating content. Model confidence correlates negatively with human response times on the same problems, even after controlling for task variables and accuracy. The key divergence is the Wason selection task, where LMs generally outperform humans and show a different error distribution (fewer matching-bias errors, more antecedent-false errors). Chain-of-thought prompting can partially restore content-independent reasoning in strong models by improving performance on abstract/unfamiliar conditions without degrading familiar ones. The authors argue these findings show dual-system-like behavior can emerge from a single system without explicit symbolic reasoning, and that content effects may arise from training on human-generated text reflecting real-world statistical regularities. Content effects survive instruction tuning (Flan-PaLM 2) and scale (larger models are more accurate but not less content-biased).

## Quotes

- **Source extract (verbatim):** We explored this question across three logical reasoning tasks: natural language inference, judging the logical validity of syllogisms, and the Wason selection task. We evaluate state of the art LMs, as well as humans, and find that the LMs reflect many of the same qualitative human patterns on these tasks—like humans, models answer more accurately when the semantic content of a task supports the logical inferences. These parallels are reflected in accuracy patterns, and in some lower-level features like the relationship between LM confidence over possible answers and human response times. However, in some cases the humans and models behave differently—particularly on the Wason task, where humans perform much worse than large models, and exhibit a distinct error pattern.
  - **Source location:** Abstract.
- **Source extract (verbatim):** In each task, humans and models show similar levels of accuracy across conditions. In keeping with our hypothesis, humans and models show similar content effects on each task, which we measure as the advantage when reasoning about logical situations that are consistent with real-world relationships or rules. - In the simplest NLI task, humans and all models show high accuracy and relatively minor effects of content. - When judging the validity of syllogisms, both humans and models show more moderate accuracy, and significant advantages when content supports the logical inference. - On the Wason selection task, humans and models show even lower accuracy, and again substantial content effects.
  - **Source location:** “Content effects in humans and language models,” primary-results summary; list whitespace normalized.
- **Source extract (verbatim):** For each task, the model is presented with brief instructions approximating the human instructions, then the question ending with "Answer:", and model scoring uses the DC-PMI correction (change in likelihood of each answer relative to a baseline context) to reduce sensitivity to answer phrasing.
  - **Source location:** Methods summary, “Models & evaluation.”
- **Source extract (verbatim):** We also find that chain-of-thought techniques (loosely giving the models time to "think") can improve the performance of strong models on the Arbitrary and Nonsense conditions of the Wason task.
  - **Source location:** Results, The Wason selection task.
- **Source extract (verbatim):** Chain-of-thought prompting can, in some cases, push large models to rely more on logical strategies, thereby reducing content effects through improving performance on less familiar or conflicting situations—particularly if those examples demonstrate precisely the type of reasoning that's required.
  - **Source location:** Results, Chain-of-thought can sometimes push large models to rely more on logic.
- **Source extract (verbatim):** We generally find similar content effects across the various models we evaluate. Larger models tend to be more accurate overall. Instruction-tuned models (Flan-PaLM 2 and GPT-3.5) do not show consistent differences in overall accuracy or content effects compared to base language models. We also tested several newer Gemini models and observed similar effects, showing that these phenomena still hold with more recent models.
  - **Source location:** Results, Variability across different language models.

## Connections Found

The `/connect` discovery identified four genuine connections in the KB — three previously established and one new:

1. **[human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md)** — grounds: This paper provides direct empirical evidence for the note's central claim that LLMs exhibit human-like failure modes. Content effects across three reasoning tasks, with quantifiable confidence/RT correlations, move the claim from speculative toward empirically supported. The Wason divergence marks a concrete boundary where the overlap breaks down.

2. **[human-llm-differences-are-load-bearing-for-knowledge-system-design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)** — exemplifies: The paper is a worked example of the per-convention evaluation methodology the note advocates. Syllogisms and NLI show shared failure modes (convention transfers); the Wason task shows divergent error patterns (convention may not transfer). This is exactly the granular, convention-by-convention analysis the note calls for.

3. **[first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)** — extends: Content effects are the empirical manifestation of adaptive fit dominating explanatory reach in reasoning. Chain-of-thought partially restoring content-independent reasoning suggests a concrete mechanism for moving from adaptive to explanatory reasoning.

4. **[Structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md)** — evidenced-by: The chain-of-thought result shows a behavior change under a structural intervention, but the experiment does not distinguish training-distribution selection from extra computation, task decomposition, or a learned procedure. Persistence across tested scaling and tuning conditions bounds those experiments; it does not establish permanent necessity.

Two synthesis opportunities were flagged by `/connect`:
- **Content-bias decorrelation**: Content effects are shared across architecturally different models (Chinchilla, PaLM 2, GPT-3.5), implying model diversity alone is insufficient for decorrelating reasoning errors. Decorrelation strategies need to vary semantic framing (e.g., metamorphic checks that rephrase content), not just the model. This connects to [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md).
- **Scaling vs structured intervention**: Content effects surviving scaling and instruction tuning means structural interventions (templates, Toulmin sections) are not a temporary measure — they are permanent architecture because content bias does not dissolve with scale.

## Extractable Value

1. **Confidence-RT correlation as a transfer diagnostic**: LM confidence on reasoning problems correlates with human response times even after controlling for task variables and accuracy. This could serve as a quantitative test for whether a specific cognitive convention transfers to LLMs — if difficulty profiles align, the convention likely transfers. [experiment]

2. **Chain-of-thought as a causal-identification case**: CoT reduces content bias by improving performance on abstract or belief-violating conditions without degrading familiar ones. The result evidences that structure can change behavior, while [structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) explains why it does not identify a higher-quality training subset as the cause. [quick-win]

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

The completed update to [Structured-prompt gains do not establish training-distribution selection](../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) uses this paper as evidence that a structural intervention can change reasoning behavior while preserving the causal limit: neither the chain-of-thought result nor persistence across tested models identifies a higher-quality training subset or permanent necessity.
