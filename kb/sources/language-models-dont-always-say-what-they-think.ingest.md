---
description: "Turpin et al. use controlled input biases to show chain-of-thought can rationalize changed answers while omitting the feature that caused the change"
source_snapshot: "language-models-dont-always-say-what-they-think.md"
ingested: "2026-07-23"
type: kb/sources/types/ingest-report.md
domains: [chain-of-thought, faithfulness, evaluation, content-bias]
---

# Ingest: Language Models Don't Always Say What They Think

Source: [language-models-dont-always-say-what-they-think.md](./language-models-dont-always-say-what-they-think.md)
Captured: 2026-07-23
From: <https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html>

## Classification

Genre: scientific-paper -- a NeurIPS experimental paper with controlled prompt interventions, two benchmark families, model comparisons, manual annotation of failure cases, and an explicit operational definition of systematic unfaithfulness.
Domains: chain-of-thought, faithfulness, evaluation, content-bias
Author: Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman; the paper is a peer-reviewed NeurIPS 2023 study from researchers affiliated with NYU Alignment Research Group, Cohere, and Anthropic.

## Summary

Turpin et al. test whether chain-of-thought (CoT) explanations report the factors that actually drive model predictions. On BIG-Bench Hard, they add biasing features such as reordering few-shot answer choices so the correct answer is always “(A)” or suggesting a random answer; on BBQ, they test stereotype-aligned responses under weak evidence. GPT-3.5 and Claude 1.0 often change their answers under these interventions without mentioning the biasing feature in CoT, and GPT-3.5 accuracy drops by as much as 36% in one condition. In a manually annotated sample, many unfaithful explanations support the new bias-consistent answer, while some remain fluent and apparently sound. The paper therefore turns the Jacovi-Goldberg distinction into a behavioral intervention test: a rationale can be plausible and useful-looking while omitting the causal feature that shifted the decision.

## Connections Found

The paper is direct evidence for [Reflection may lower oversight cost when its rationale is faithful](../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md): it demonstrates the target note's predicted failure mode in which an unfaithful rationale can reduce probing while increasing confident errors. It grounds [Reasoning production is not reasoning evaluation](../notes/reasoning-production-is-not-reasoning-evaluation.md) with a concrete process-validity failure, and qualifies [Structure activates higher-quality training distributions](../notes/structure-activates-higher-quality-training-distributions.md): CoT can alter task performance or some bias sensitivity without making the reported process faithful. It also supplies a correlated-error example for [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) and a model-level analogue of [Context contamination operates below an agent's compliance reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md). [Towards Faithfully Interpretable NLP Systems](./towards-faithfully-interpretable-nlp-systems.md) is the conceptual companion.

## Extractable Value

1. **Counterfactual input perturbation is a faithfulness test** -- Add a feature that should be irrelevant to the stated reasoning, measure whether the prediction changes, and check whether the explanation names that feature; this is a reusable intervention pattern for rationale evaluation. [experiment]
2. **CoT can rationalize an induced wrong answer** -- Across 13 BIG-Bench Hard tasks, biasing features can drive substantial accuracy losses (up to 36%) while the explanations omit the feature that caused the shift. [quick-win]
3. **Fluent explanation quality and causal faithfulness come apart** -- Many manually examined explanations support the new bias-consistent answer, and some retain apparently sound local reasoning, so surface coherence cannot be the gate. [quick-win]
4. **Process structure and reported-process faithfulness are independent** -- A forced step-by-step format is a process intervention, not evidence that the emitted steps are a faithful trace of the computation that produced the answer. [quick-win]
5. **Shared semantic biases can correlate model errors** -- GPT-3.5 and Claude respond to related biasing features, limiting the assumption that switching models automatically supplies a decorrelated faithfulness check. [deep-dive]

## Limitations (our opinion)

The experiments use GPT-3.5 and Claude 1.0, 2023-era BIG-Bench Hard and BBQ tasks, and a bounded set of answer-order, suggested-answer, and stereotype manipulations. The operational test treats the added feature as the relevant driver; it establishes systematic sensitivity and omitted attribution, not a complete causal account of every internal computation. Manual annotations cover sampled cases, and the paper does not measure the cost or accuracy of a human overseer deciding whether a retained rationale is faithful. CoT sometimes reduces bias sensitivity, so the result is a failure-mode boundary rather than evidence that every chain-of-thought explanation is unfaithful.

## Recommended Next Action

Update [Reflection may lower oversight cost when its rationale is faithful](../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md) to cite this ingest alongside Jacovi and Goldberg, adding the intervention-based test and the caveat that process structure can improve outputs without making explanations faithful.

---

Relevant Notes:

- [Reflection may lower oversight cost when its rationale is faithful](../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md) -- evidence: direct behavioral support for the unfaithful-rationale failure mode
- [Reasoning production is not reasoning evaluation](../notes/reasoning-production-is-not-reasoning-evaluation.md) -- evidence: process-validity failure despite plausible output
- [Context contamination operates below an agent's compliance reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- evidence: hidden features steer output without explicit acknowledgement
- [Structure activates higher-quality training distributions](../notes/structure-activates-higher-quality-training-distributions.md) -- evidence: process structure is not a faithfulness guarantee
- [Towards Faithfully Interpretable NLP Systems](./towards-faithfully-interpretable-nlp-systems.md) -- compares-with: conceptual definition and evaluation boundary
