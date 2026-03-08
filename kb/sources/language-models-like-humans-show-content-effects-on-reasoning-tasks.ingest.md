---
source_snapshot: language-models-like-humans-show-content-effects-on-reasoning-tasks.md
ingested: 2026-03-08
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

Lampinen et al. systematically test whether large language models exhibit the same "content effects" as humans on logical reasoning tasks — the tendency to reason more accurately when semantic content supports the correct logical inference. Across three tasks (natural language inference, syllogisms, Wason selection task), LMs mirror human accuracy patterns: both perform better on familiar/believable content and worse on abstract or belief-violating content. Model confidence even correlates negatively with human response times on the same problems. The key divergence is the Wason selection task, where LMs generally outperform humans and show different error distributions (fewer matching-bias errors, more antecedent-false errors). Chain-of-thought prompting can partially restore content-independent reasoning in strong models, paralleling the effect of deliberative "slow" thinking in humans. The authors argue these findings show dual-system-like behavior can emerge from a single system without explicit symbolic reasoning, and that content effects may arise from training on human-generated text that reflects real-world statistical regularities.

## Connections Found

The /connect discovery identified three genuine connections in the KB:

1. **[human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md)** — grounds: This paper provides direct empirical evidence for the note's central (self-described "speculative") claim that LLMs exhibit human-like failure modes. Content effects across three reasoning tasks, with quantifiable confidence/RT correlations, move the claim from speculative toward empirically supported.

2. **[human-llm-differences-are-load-bearing-for-knowledge-system-design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)** — grounds: The paper is a worked example of the per-convention evaluation methodology the note advocates. Syllogisms and NLI show shared failure modes (convention transfers); the Wason task shows divergent error patterns (convention may not transfer). This is exactly the granular, convention-by-convention analysis the note calls for.

3. **[first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md)** — extends: Content effects are the empirical manifestation of adaptive fit dominating explanatory reach in reasoning. Chain-of-thought partially restoring content-independent reasoning suggests a concrete mechanism for moving from adaptive to explanatory reasoning.

Eight candidates were rejected with specific mechanistic justifications (surface vocabulary overlap without shared mechanism). A synthesis opportunity was flagged: combining the failure-mode overlap note, the human-LLM differences note, and this source could produce an empirically grounded transfer methodology.

## Extractable Value

1. **Confidence-RT correlation as a transfer diagnostic**: LM confidence on reasoning problems correlates with human response times even after controlling for task variables and accuracy. This could serve as a quantitative test for whether a specific cognitive convention transfers to LLMs — if the difficulty profiles align, the convention likely transfers. [experiment]

2. **Chain-of-thought as adaptive-to-explanatory shift**: CoT prompting reduces content bias specifically by improving performance on abstract/belief-violating conditions, not by degrading performance on familiar ones. This is a directional finding: structured prompting pushes toward content-independent reasoning without sacrificing content-supported reasoning. Relevant to how we design structured templates in the KB. [quick-win]

3. **Wason divergence as a transfer boundary marker**: Humans show matching bias on the Wason task; LMs show a qualitatively different error pattern (antecedent-false errors). This is a concrete example where a human cognitive convention does NOT transfer — useful as a worked counterexample for the transfer methodology. [just-a-reference]

4. **Single-system dual-process behavior**: A single transformer can exhibit both "fast" (content-biased) and "slow" (content-independent with CoT) reasoning without an explicit symbolic System 2. This challenges the common claim that LLMs are "System 1 only" and need external symbolic augmentation. [deep-dive]

5. **Content effects survive instruction tuning and scaling**: Flan-PaLM 2 and GPT-3.5 show the same content effects as base models. Larger models are more accurate overall but not less content-biased. This means structured prompting (not just scale or RLHF) is needed to address content bias. [quick-win]

6. **Two hypotheses for content effect origins**: (a) direct imitation of human error patterns from training data, or (b) convergent evolution from shared statistical structure of experience. These map onto different predictions about whether novel structured formats (not in training data) can escape content bias. [deep-dive]

## Recommended Next Action

Update [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md): add a section citing this paper as empirical evidence that the failure-mode overlap is not speculative but demonstrated across three reasoning tasks, with the Wason task divergence as a concrete boundary case where the overlap breaks down. This strengthens the note's central claim and adds the nuance that overlap is real but not universal — exactly the per-convention evaluation the methodology requires.
