---
description: "HBR trendslop article: LLM strategy advice follows fashionable management discourse despite prompt and context variation."
source_snapshot: "researchers-asked-llms-strategic-advice-trendslop.md"
ingested: "2026-04-21"
type: kb/sources/types/ingest-report.md
domains: [llm-reasoning, prompt-sensitivity, strategy, evaluation]
---

# Ingest: Researchers Asked LLMs for Strategic Advice. They Got "Trendslop" in Return.

Source: researchers-asked-llms-strategic-advice-trendslop.md
Captured: 2026-04-21
From: https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return

## Classification

Type: conceptual-essay -- HBR article by academic researchers that names a framing ("strategy trendslop"), reports high-level experimental findings, and turns them into management guidance; it is not the primary paper/preprint.
Domains: llm-reasoning, prompt-sensitivity, strategy, evaluation
Author: Angelo Romasanta, Llewellyn D.W. Thomas, and Natalia Levina are business-school academics working on innovation, ecosystems, generative AI evaluation, and technology use in organizations.

## Summary

Romasanta, Thomas, and Levina argue that LLMs are risky strategic advisors because they tend to recommend fashionable, high-valence management options rather than context-specific strategic trade-offs. They report simulations across seven binary strategy tensions and several leading models, finding strong defaults toward options such as differentiation, augmentation, collaboration, decentralization, and long-termism. Prompt manipulations and richer organizational contexts shifted some results but did not remove the bias; option order itself produced large movement, suggesting sensitivity rather than deeper reasoning. The article names this failure mode "strategy trendslop" and recommends using LLMs for option expansion, counterargument generation, and risk surfacing while keeping final strategic choice with humans.

## Connections Found

The connect pass saved [researchers-asked-llms-strategic-advice-trendslop.connect.md](../reports/connect/sources/researchers-asked-llms-strategic-advice-trendslop.connect.md). It found six direct connections. The strongest is [First-principles reasoning selects for explanatory reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md): the source is a concrete case of adaptive cultural fit dominating explanatory reach in LLM advice. It also extends [Structure activates higher-quality training distributions](../notes/structure-activates-higher-quality-training-distributions.md) by showing the negative case, where domain prompts activate polished business discourse rather than better reasoning. It extends [Human writing structures transfer to LLMs because failure modes overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) and the [content-effects ingest](language-models-like-humans-show-content-effects-on-reasoning.ingest.md) by moving content effects from formal reasoning tasks into strategic choice. Finally, it exemplifies [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), extends [Agentic systems interpret underspecified instructions](../notes/agentic-systems-interpret-underspecified-instructions.md), and qualifies [Prompt ablation converts human insight into deployable agent framing](../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md).

## Extractable Value

1. **LLM advice can follow discourse priors before task logic** -- High-reach mechanism: where a domain has fashionable vocabulary with positive affect, the model may optimize for culturally plausible discourse rather than the decision criterion. This is a cleaner phrase for the KB than "trendslop" because it connects to adaptive fit and distribution selection. [deep-dive]

2. **Distribution selection has negative cases** -- [Structure activates higher-quality training distributions](../notes/structure-activates-higher-quality-training-distributions.md) currently emphasizes structured templates selecting better reasoning distributions. This source adds the boundary: domain language can select a fluent but low-reach discourse distribution, especially in advice-heavy domains. [quick-win]

3. **Prompt movement is not bias removal** -- The reported option-order effect is valuable because it separates "the output changed" from "the model reasoned better." This sharpens the evaluation meaning of prompt variation and belongs near [systematic-prompt-variation](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md). [quick-win]

4. **Context can make a biased answer sound tailored** -- Richer business context reportedly tempered but did not eliminate the default preferences. For KB methodology, this warns that adding context can improve surface fit without changing the underlying projection policy. [experiment]

5. **Use LLMs for option expansion, not consequential selection** -- The practical rule transfers beyond corporate strategy: ask the model to generate alternatives, risks, opposing cases, and stakeholder perspectives, but do not let it collapse the final trade-off when the verifier is weak. [quick-win]

6. **Bias ledgers may be needed for repeated model use** -- The article's recommendation to record model versions and query outputs is a concrete operational pattern: for high-stakes repeated use, track stable priors as part of the evaluation surface because model upgrades can shift them silently. [experiment]

## Limitations (our opinion)

The main limitation is source form: this is an HBR article summarizing "recent research," not the primary paper. It gives headline model names, broad task categories, and selected effect sizes, but not enough detail to evaluate prompts, sampling settings, statistical tests, dataset construction, or exact model versions. The empirical claims should be treated as useful directional evidence until the underlying study is available.

The binary strategy tensions are also theory-laden. Framing choices as forced pairs can make LLM hedging look like strategic confusion even when hybrid strategy would be legitimate under a more precise decomposition. The article invokes established strategy theory, but does not show outcome validation: we do not know whether the supposedly biased answers would underperform in real strategic contexts.

The causal story is plausible but not fully hard to vary. "LLMs learned fashionable management discourse from internet text" is a simpler mechanism than "LLMs have a worldview," but the article does not test training-data attribution directly. It also does not separate content-valence bias from option-order bias, safety/helpfulness tuning, RLHF preferences for balanced advice, or the possibility that models avoid recommending harsh options such as automation because of assistant-persona constraints.

For KB use, the strongest transferable claim is not that LLMs are bad at strategy. It is that domain-specific context and better prompting can fail to dislodge a learned prior while making the output look more situated. That claim fits existing KB theory, but it needs primary-method evidence before it should become a load-bearing empirical source.

## Recommended Next Action

Write a note titled "LLM advice follows discourse priors before task logic" connecting to [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md), [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md), and [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing](../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md). It would argue that in advice-heavy domains, LLM outputs often select the socially fluent distribution before they evaluate the task logic; prompt and context variation should therefore be treated as diagnosis unless tied to an external verifier.
