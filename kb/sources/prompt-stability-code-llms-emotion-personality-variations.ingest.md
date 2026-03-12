---
description: Empirical study measuring code LLM stability under emotion/personality prompt variations — finds performance and stability are decoupled objectives, smaller models can be more stable, and emotional prompting reveals confidence miscalibration invisible to standard benchmarks
source_snapshot: prompt-stability-code-llms-emotion-personality-variations.md
ingested: 2026-03-12
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

Ma et al. introduce PromptSE, a framework for measuring how sensitive code generation models are to semantically equivalent prompts that vary in emotional tone (frustrated, anxious, focused, etc.) and personality style (algorithm expert, pragmatic engineer, etc.). Using psychologically grounded templates at three controlled perturbation distances (d=0.1 light lexical, d=0.2 moderate style, d=0.3 substantial transformation), they generate 14,760 variants of HumanEval prompts and evaluate 14 models across three architecture families (Llama, Qwen, DeepSeek). The core finding is that performance (Pass@1) and stability (AUC-E, their proposed area-under-curve metric) are statistically uncorrelated (Spearman rho = -0.433, p = 0.122), meaning these are decoupled optimization objectives. Additional findings: smaller models can outperform larger ones on stability (Qwen-1.5B achieves AUC-E 0.646, highest in the study), stability does not scale monotonically with model size, and high-arousal negative-valence prompts induce confidence miscalibration (ECE ranging from 0.055 to 0.622 across model-emotion combinations) not visible in standard benchmarks.

## Connections Found

The `/connect` discovery identified 11 connections (4 strong, 7 moderate), mapping cleanly into the KB's three-phenomena taxonomy, reliability/oracle framework, and bitter lesson boundary.

**Strong connections:**

- [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: holding functional requirements constant while varying emotional/stylistic expression produces up to 40% performance swings, providing the strongest empirical evidence in the KB that semantic underspecification (not execution noise) drives meaningful output variation. The performance-stability decoupling directly confirms that underspecification and execution quality are independent axes. **Gap: this note does not yet cite the source.**

- [llm-interpretation-errors](../notes/llm-interpretation-errors.md) — **grounds**: the paper empirically separates all three phenomena in the taxonomy: temperature+sampling measures indeterminism within each variant, cross-variant comparison measures underspecification, and systematic degradation under emotional prompts reveals interpretation bias. AUC-E quantifies underspecification; no model achieves AUC-E near 1.0 (max 0.646), confirming it is a permanent property of the language. **Bidirectional: already established.**

- [execution-indeterminism-is-a-property-of-the-sampling-process](../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **grounds**: the methodology provides the cleanest empirical separation of indeterminism from underspecification in the KB's source collection. Temperature=0.2 with 16 samples per prompt measures indeterminism within each variant; comparing across variants measures underspecification. **Gap: this note has no sources section at all.**

- [operational-signals-that-a-component-is-a-relaxing-candidate](../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **refines**: PromptSE's emotion/personality templates provide a richer operationalization of Signal 1 (paraphrase brittleness) than simple rephrasings — three calibrated perturbation distances across 14,760 variants. The non-monotonic scaling finding supports the note's interpretation that brittleness detects badly-fitting theories rather than capacity limitations. **Bidirectional: already established.**

**Moderate connections:**

- [reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — **extends**: AUC-E is a concrete operationalization of the Robustness dimension (R_Rob), and the calibration analysis (ECE) maps to Predictability. The decoupling finding independently confirms that capability and reliability are independent optimization axes. **Gap: note does not yet cite this source.**

- [writing-styles-are-strategies-for-managing-underspecification](../notes/writing-styles-are-strategies-for-managing-underspecification.md) — **complements**: complementary taxonomy viewed from opposite directions. The writing-styles note focuses on instruction-author strategies for narrowing the interpretation space; this paper demonstrates that user-side expression variation also functionally alters model behavior even when functional requirements are held constant. Both show stylistic register is functionally consequential, not cosmetic.

- [structure-activates-higher-quality-training-distributions](../notes/structure-activates-higher-quality-training-distributions.md) — **grounds from opposite direction**: the paper demonstrates the distribution-selection mechanism in reverse — emotional coloring (frustrated, anxious) activates different training distributions, some with miscalibrated confidence properties (ECE ranging 0.055 to 0.622). Where the structure-activates note argues structured templates steer toward higher-quality distributions, this paper shows emotional framing steers toward different-quality distributions. Same mechanism, opposite valence.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **enables**: the emotion/personality templates provide a structured methodology for the "vary the prompt" decorrelation strategy. The perturbation distance control (d=0.1, 0.2, 0.3) provides calibrated decorrelation strength.

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — **extends**: the ECE analysis provides additional evidence for the calibration-vs-discrimination distinction. Model-specific ECE shifts under emotional prompting demonstrate that calibration properties are fragile under surface-level perturbations — even calibration improvements from Rabanser et al. may be brittle under realistic usage conditions.

- [bitter-lesson-boundary](../notes/bitter-lesson-boundary.md) — **extends**: the non-monotonic scaling finding (smaller Qwen-1.5B more stable than larger models) provides evidence for the core distinction. Stability may not follow the same scaling patterns as performance, suggesting it is closer to requiring explicit optimization rather than emerging from scale.

- [prompt-ablation-converts-human-insight-to-deployable-framing](../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — **complements methodology**: both involve controlled prompt variation with fixed inputs. The ablation note varies framing to find which cognitive moves agents can execute reliably; this paper varies emotional/personality framing to measure stability. Methodological parallel: controlled variation as a diagnostic technique.

**Synthesis opportunities flagged:**

1. "Performance and stability are decoupled optimization objectives" — recommended as a new note. Contributing notes: agentic-systems-interpret-underspecified-instructions, reliability-dimensions-map-to-oracle-hardening-stages, the-augmentation-automation-boundary-is-discrimination-not-accuracy.
2. Systematic prompt variation as dual-purpose methodology — simultaneously a verification technique (decorrelating oracle checks) and a diagnostic technique (measuring brittleness to identify relaxing candidates).

## Extractable Value

1. **Performance-stability decoupling evidence** — Spearman rho = -0.433, p = 0.122 across 14 models. The four-quadrant distribution (3/4/4/3 models in high/low performance x high/low stability) is the strongest empirical evidence in the KB's sources that capability and reliability are independent optimization axes. [quick-win]

2. **Non-monotonic scaling of stability** — smaller models (Qwen-1.5B) achieving the highest AUC-E challenges the assumption that scale improves all properties. Connects to the bitter lesson boundary — if stability doesn't scale, it may require explicit optimization (theory, not specification). [experiment]

3. **Controlled perturbation distance methodology** — three calibrated distances (d=0.1, 0.2, 0.3) from light lexical changes through substantial transformation while preserving semantics. Directly usable as a protocol for metamorphic testing in our own systems. The finding that d=0.1 "often preserves performance" while d=0.3 "reveals model-specific vulnerabilities" gives a practical gradient. [experiment]

4. **Emotion-as-probe for confidence miscalibration** — high-arousal negative-valence prompts induce ECE shifts in specific model families (particularly Qwen). Novel diagnostic: emotional coloring as a stress test revealing calibration failures invisible to standard benchmarks. The mechanism (emotional language correlating with different code quality distributions in training data) is a concrete instance of the distribution-selection hypothesis. [deep-dive]

5. **AUC-E as a concrete metric for quantifying underspecification** — provides an operational definition (area under the elasticity curve across perturbation distances) that maps to our theoretical concept of "how much underspecification the spec language introduces." [just-a-reference]

6. **SoftExec as probability-aware evaluation** — weights correctness by generation probability, distinguishing high-confidence correct solutions from lucky guesses. Addresses a real limitation of Pass@k. [just-a-reference]

## Curiosity Gate

**What is most surprising?** The non-monotonic scaling of stability is the standout finding. That Qwen-1.5B (a tiny, distilled model) achieves the highest stability score across all 14 models — including models 20x its size — is genuinely unexpected. The paper speculates about "simpler decision boundaries" but a simpler account may be more informative: distilled models learn a narrower repertoire of solutions, so there is less variation to express. If the model only knows one way to solve a problem regardless of how you ask, it looks "stable" without actually being robust in any deep sense. This reframes the finding: stability-through-simplicity is not the same as stability-through-understanding. The practical consequence is that a small stable model may fail catastrophically on tasks outside its narrow repertoire, while a large unstable model may succeed on a wider range of tasks despite being sensitive to phrasing. This tension is not explored in the paper.

**What's the simpler account?** For the headline claim (performance-stability decoupling): the simpler explanation is that these are just different properties being measured by different instruments, and there is no theoretical reason they should correlate in the first place. Performance measures how well the model solves problems at its best; stability measures how much phrasing variation affects performance. A model that has learned robust functional mappings but weak surface-form invariance would score high on performance and low on stability — which is exactly what Qwen2.5-Coder-7b does (Pass@1 0.820, AUC-E 0.403). The "decoupling" is better understood as "these were never the same thing" rather than "these used to be coupled and now we've discovered they're not." This doesn't reduce the practical value of measuring both, but it deflates the theoretical novelty.

## Limitations (our opinion)

**Narrow evaluation domain.** The study uses only HumanEval (164 problems, Python only). HumanEval problems have unambiguous functional specifications with test suites — the least underspecified type of coding task. The paper's findings about "prompt sensitivity" may understate the effect for more realistic, genuinely underspecified tasks (e.g., "refactor for readability" as discussed in [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)). The paper measures sensitivity to emotional/stylistic variation on tasks where the functional specification is precise; real-world underspecification involves ambiguity in what the task even IS.

**Template generation introduces its own bias.** Variants are generated by DeepSeek-Chat using structured templates. This means "stylistic variation" is filtered through one LLM's interpretation of what frustrated/anxious/focused writing looks like. The paper acknowledges this but does not test whether human-written emotional variants produce the same sensitivity patterns. The perturbation distances (0.1, 0.2, 0.3) are defined by template instructions, not measured against any ground truth of linguistic distance.

**Statistical power for the headline claim.** The performance-stability correlation (rho = -0.433, p = 0.122) is presented as "no statistically significant negative correlation" — but with only 14 models, the study is underpowered to detect moderate effects. The confidence interval [-0.875, 0.249] spans a wide range including strong negative correlation. The claim that performance and stability are "decoupled" is consistent with the data but not strongly supported by it; a larger model sample could reveal a relationship the current study lacks power to detect.

**Missing baselines.** The paper does not compare PromptSE against simpler stability measures — e.g., variance of Pass@k across random prompt rephrasings without the emotion/personality structure, or stability under purely syntactic transformations (reordering clauses, adding whitespace). Without these baselines, it's unclear how much value the psychologically grounded templates add over random paraphrasing — the approach Rabanser et al. already used in [towards-a-science-of-ai-agent-reliability](towards-a-science-of-ai-agent-reliability.md).

**No causal mechanism for the non-monotonic scaling finding.** The observation that smaller models can be more stable is interesting but unexplained. The paper speculates about "simpler decision boundaries" but provides no evidence for this mechanism. Alternative explanations (distillation artifacts in the Qwen-1.5B model, limited solution diversity in small models that happens to look like stability) are not ruled out.

**Single evaluation metric design choices.** AUC-E uses Simpson's rule across three points with equal weighting — but the choice of three distances, their specific values, and equal weighting are all design decisions that could produce different rankings under different choices. The paper does not perform sensitivity analysis on these meta-parameters.

## Recommended Next Action

Write a note titled "Performance and stability are decoupled optimization objectives" connecting to [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) and [reliability-dimensions-map-to-oracle-hardening-stages](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — it would argue that empirical evidence from prompt sensitivity studies (this paper's four-quadrant distribution and Rabanser et al.'s R_prompt findings) confirms the KB's theoretical prediction that capability and reliability are independent axes, with practical implications for model selection in agent architectures. The note should also address the deflationary interpretation from the Curiosity Gate: the decoupling may be less surprising than it appears, since performance and stability measure fundamentally different properties.
