---
description: Empirical study measuring code LLM stability under emotion/personality prompt variations — finds performance and stability are decoupled objectives, smaller models can be more stable, and emotional prompting reveals confidence miscalibration invisible to standard benchmarks
source_snapshot: prompt-stability-code-llms-emotion-personality-variations.md
ingested: 2026-03-11
type: scientific-paper
domains: [prompt-sensitivity, llm-evaluation, code-generation, reliability]
---

# Ingest: Prompt Stability in Code LLMs: Measuring Sensitivity across Emotion- and Personality-Driven Variations

Source: prompt-stability-code-llms-emotion-personality-variations.md
Captured: 2026-03-11
From: https://arxiv.org/pdf/2509.13680

## Classification

Type: scientific-paper — peer-reviewed preprint with controlled experiments across 14 models, 14,760 prompt variants, statistical analysis with FDR correction and bootstrap confidence intervals.

Domains: prompt-sensitivity, llm-evaluation, code-generation, reliability

Author: Wei Ma et al. (five authors). Academic team studying software engineering and LLM reliability. The paper introduces a novel framework (PromptSE) rather than reporting on production deployment experience. Credibility rests on experimental methodology rather than practitioner authority.

## Summary

The paper introduces PromptSE, a framework for measuring how sensitive code generation models are to semantically equivalent prompts that vary in emotional tone (frustrated, anxious, focused, etc.) and personality style. Using psychologically grounded templates at three controlled perturbation distances, they generate 14,760 variants of HumanEval prompts and evaluate 14 models across three architecture families (Llama, Qwen, DeepSeek). The core finding is that performance (Pass@1) and stability (AUC-E, their proposed area-under-curve metric) are statistically uncorrelated (Spearman rho = -0.433, p = 0.122), meaning these are decoupled optimization objectives. Additional findings: smaller models can outperform larger ones on stability (Qwen-1.5B achieves AUC-E 0.646, highest in the study), stability does not scale monotonically with model size, and high-arousal negative-valence prompts induce confidence miscalibration (ECE ranging from 0.055 to 0.622 across model-emotion combinations) not visible in standard benchmarks.

## Connections Found

The `/connect` discovery identified nine connections, four strong and five moderate, mapping cleanly into the KB's three-phenomena taxonomy and reliability/oracle framework.

**Strong connections:**

- [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — the paper **grounds** the two-phenomena model at scale. Holding functional requirements constant while varying emotional/stylistic expression produces up to 40% performance swings, confirming that semantic underspecification (not execution noise) drives the meaningful variation. The performance-stability decoupling provides direct empirical evidence that underspecification and execution quality are independent axes.

- [LLM interpretation errors](../notes/llm-interpretation-errors.md) — the paper empirically separates all three phenomena in the taxonomy: temperature+sampling measures indeterminism within each variant, cross-variant comparison measures underspecification, and systematic performance degradation under emotional prompts reveals bias (interpretation error). AUC-E quantifies underspecification; no model achieves AUC-E near 1.0 (max 0.646), confirming it is a permanent property of the language.

- [execution-indeterminism-is-a-property-of-the-sampling-process](../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — the paper's methodology cleanly separates the two phenomena. Temperature=0.2 with 16 samples per prompt measures indeterminism within each variant; comparing across variants measures underspecification. This is the cleanest empirical separation of the two phenomena in the KB's source collection.

- [operational-signals-that-a-component-is-a-softening-candidate](../notes/operational-signals-that-a-component-is-a-softening-candidate.md) — PromptSE's emotion/personality templates are systematic metamorphic tests for paraphrase brittleness (Signal 1). The finding that smaller models achieve superior stability while larger models show greater variance supports the note's prediction that brittleness signals detect badly-fitting theories — larger models may encode more theories about prompt format rather than more robust specifications of meaning.

**Moderate connections:**

- [reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — AUC-E maps to the Robustness dimension (R_Rob), and the calibration analysis (ECE) maps to Predictability. The decoupling finding independently confirms that capability and reliability are independent.

- [towards-a-science-of-ai-agent-reliability](towards-a-science-of-ai-agent-reliability.md) — PromptSE extends Rabanser et al.'s R_prompt with a richer perturbation framework: psychologically grounded templates at controlled distances versus simple instruction paraphrases.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — emotion templates are a structured methodology for the "vary the prompt" decorrelation strategy. The perturbation distance control (d=0.1, 0.2, 0.3) provides a way to tune decorrelation strength.

- [writing-styles-are-strategies-for-managing-underspecification](../notes/writing-styles-are-strategies-for-managing-underspecification.md) — complementary taxonomy: the writing-styles note focuses on instruction-author strategies; this paper focuses on user-side expression variation. Both show stylistic register is functionally consequential, not cosmetic.

- [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md) — the paper demonstrates the distribution-selection mechanism from the opposite direction: emotional coloring (frustrated, anxious) activates different training distributions, some associated with miscalibrated outputs. Direct evidence that stylistic framing selects training distributions with different calibration properties.

**Synthesis opportunity flagged:** Systematic prompt variation as a dual-purpose methodology — simultaneously a verification technique (decorrelating checks for oracle amplification) and a diagnostic technique (measuring brittleness to identify softening candidates). The PromptSE framework with controlled perturbation distances could serve both purposes.

## Extractable Value

1. **AUC-E as a concrete metric for quantifying underspecification** — the paper provides an operational definition (area under the elasticity curve across perturbation distances) that maps directly to our theoretical concept of "how much underspecification the spec language introduces." Could be referenced when the seedling notes on underspecification and indeterminism are matured. [just-a-reference]

2. **Performance-stability decoupling evidence** — Spearman rho = -0.433, p = 0.122 across 14 models. The four-quadrant distribution (high/low performance x high/low stability with 3/4/4/3 models) is the strongest empirical evidence in the KB's sources that capability and reliability are independent optimization axes. Directly supports the reliability-dimensions framework. [quick-win]

3. **Non-monotonic scaling of stability** — smaller models (Qwen-1.5B) achieving the highest AUC-E challenges the assumption that scale improves all properties. The paper suggests simpler decision boundaries or reduced overfitting to training prompt distributions as mechanisms. This connects to the bitter lesson boundary — if stability doesn't scale, it may be a property that requires explicit optimization (theory, not specification). [experiment]

4. **Controlled perturbation distance methodology** — three calibrated distances (d=0.1, 0.2, 0.3) with light lexical changes through substantial transformation while preserving semantics. This is directly usable as a protocol for metamorphic testing in our own systems. The finding that d=0.1 "often preserves performance" while d=0.3 "reveals model-specific vulnerabilities" gives a practical gradient. [experiment]

5. **Emotion-as-probe for confidence miscalibration** — high-arousal negative-valence prompts induce ECE shifts in specific model families (particularly Qwen). This is a novel diagnostic: emotional coloring as a stress test that reveals calibration failures invisible to standard benchmarks. The mechanism (emotional language correlating with different code quality distributions in training data) is a concrete instance of the distribution-selection hypothesis. [deep-dive]

6. **SoftExec as probability-aware evaluation** — weights correctness by generation probability, distinguishing high-confidence correct solutions from lucky guesses. This addresses a real limitation of Pass@k and could be relevant if we develop evaluation methodology for our own agent outputs. [just-a-reference]

## Limitations (our opinion)

**Narrow evaluation domain.** The study uses only HumanEval (164 problems, Python only). HumanEval problems have unambiguous functional specifications with test suites — the least underspecified type of coding task. The paper's findings about "prompt sensitivity" may understate the effect for more realistic, genuinely underspecified tasks (e.g., "refactor for readability" as discussed in [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)). The paper measures sensitivity to emotional/stylistic variation on tasks where the functional specification is precise; real-world underspecification involves ambiguity in what the task even IS.

**Template generation introduces its own bias.** Variants are generated by DeepSeek-Chat using structured templates. This means "stylistic variation" is filtered through one LLM's interpretation of what frustrated/anxious/focused writing looks like. The paper acknowledges this but does not test whether human-written emotional variants produce the same sensitivity patterns. The perturbation distances (0.1, 0.2, 0.3) are defined by template instructions, not measured against any ground truth of linguistic distance.

**Statistical power for the headline claim.** The performance-stability correlation (rho = -0.433, p = 0.122) is presented as "no statistically significant negative correlation" — but with only 14 models, the study is underpowered to detect moderate effects. The confidence interval [-0.875, 0.249] spans a wide range including strong negative correlation. The claim that performance and stability are "decoupled" is consistent with the data but not strongly supported by it; a larger model sample could reveal a relationship the current study lacks power to detect.

**Missing baselines.** The paper does not compare PromptSE against simpler stability measures — e.g., variance of Pass@k across random prompt rephrasings without the emotion/personality structure, or stability under purely syntactic transformations (reordering clauses, adding whitespace). Without these baselines, it's unclear how much value the psychologically grounded templates add over random paraphrasing — the very approach Rabanser et al. already used.

**No causal mechanism for the non-monotonic scaling finding.** The observation that smaller models can be more stable is interesting but unexplained. The paper speculates about "simpler decision boundaries" but provides no evidence for this mechanism. Alternative explanations (distillation artifacts in the Qwen-1.5B model, limited solution diversity in small models that happens to look like stability) are not ruled out.

**Single evaluation metric design choices.** AUC-E uses Simpson's rule across three points with equal weighting — but the choice of three distances, their specific values, and equal weighting are all design decisions that could produce different rankings under different choices. The paper does not perform sensitivity analysis on these meta-parameters.

## Recommended Next Action

Write a note titled "Performance and stability are decoupled optimization objectives" connecting to [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) and [reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — it would argue that empirical evidence from prompt sensitivity studies (this paper's four-quadrant distribution and Rabanser et al.'s R_prompt findings) confirms the KB's theoretical prediction that capability and reliability are independent axes, with practical implications for model selection in agent architectures (optimizing for reliability may require different model choices than optimizing for capability, and the two can sometimes be jointly achieved).
