---
description: "Code-LLM study finds performance and prompt stability are distinct, smaller models may be steadier, and emotional/personality variants expose confidence miscalibration missed by standard benchmarks"
source: https://arxiv.org/pdf/2509.13680
captured: "2026-03-11"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc
ingested: "2026-03-12"
type: types/ingest-report.md
domains: [prompt-sensitivity, llm-evaluation, code-generation, reliability]
---

# Ingest: Prompt Stability in Code LLMs

## Classification

Peer-reviewed preprint with controlled experiments across 14 models, 14,760 prompt variants, statistical analysis with FDR correction and bootstrap confidence intervals.

Author: Wei Ma et al. (five authors). Academic team studying software engineering and LLM reliability. The paper introduces a novel framework (PromptSE) rather than reporting on production deployment experience. Credibility rests on experimental methodology rather than practitioner authority.

## Summary

Ma et al. introduce PromptSE, a framework for measuring how sensitive code generation models are to prompts intended to preserve meaning while varying emotional tone (frustrated, anxious, focused, etc.) and personality style (algorithm expert, pragmatic engineer, etc.). Using psychologically grounded templates at three template-specified rewriting levels (d=0.1 light lexical, d=0.2 moderate style, d=0.3 substantial transformation), they generate 14,760 variants of HumanEval prompts and evaluate 14 models across three architecture families (Llama, Qwen, DeepSeek). The model-level correlation between performance (Pass@1) and stability (AUC-E, their proposed area-under-curve metric) did not reach statistical significance in this 14-model sample (Spearman rho = -0.433, p = 0.122; 95% CI [-0.875, 0.249]). This does not establish independence or decoupled optimization objectives. Additional findings: smaller models can outperform larger ones on stability (Qwen-1.5B achieves AUC-E 0.646, highest in the study), stability does not scale monotonically with model size, and high-arousal negative-valence prompts induce confidence miscalibration (ECE ranging from 0.055 to 0.622 across model-emotion combinations) not visible in standard benchmarks.

## Quotes

> Our approach generates semantically equivalent prompt variants through emotion and personality templates, then evaluates model sensitivity using probability-aware continuous scoring (PromptSE) or binary evaluation (PromptSELight) depending on model accessibility. The framework operates under strict semantic and interface invariance constraints, ensuring that all variants preserve computational requirements (e.g., preserving input-output constraints, and complexity bounds) and functional specifications.
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §2, “PromptSE: Proposed Prompt Sensitivity Evaluation Framework”

> We apply a uniform decoding policy with temperature 0.2 and draw 16 independent samples per prompt at each distance level.
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §3.2, “Models and Decoding Settings”

> We compute model-level rank correlation, obtaining Spearman ρ = −0.433 (p = 0.122; 95% CI [−0.875, 0.249]), which does not reach statistical significance in the current sample, suggesting no unified negative correlation trend.
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §4.1, “RQ1: Joint Structure of Performance and Prompt Stability”

> We evaluate 14 models across three architecture families (Llama, Qwen, DeepSeek) using HumanEval with semantically equivalent variants (14,760 in total). Each variant prompt generates 16 samples under uniform decoding, with statistical analysis employing robust methods including correlation tests, confidence intervals (CI), and false discovery rate (FDR) correction.
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §1, “Introduction”

> For each prompt p and distance d, compute individual elasticity using the formulations from Equations 4 and 5. For PromptSE mode, average across all prompts to obtain the elasticity curve E(d). Second, average across all prompts for PromptSELight mode.
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §2.3, “AUC-E: Area Under Curve of Elasticity,” Elasticity Curve Construction

> We adopt model-level Pass@1 as the performance indicator and quantify prompt stability through AUC-E.
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §4.1, “RQ1: Joint Structure of Performance and Prompt Stability”

> Under valence×arousal conditions, performance–sensitivity coupling and confidence patterns show cross-model differences. For some models, emotional prompting mildly reshapes correctness and calibration, but effects vary by model and family. Probability-layer diagnostics (ECE, bias, and elasticity) complement discrete indicators, helping make "calibration-aware" model selections. High-arousal negative-valence prompts inducing confidence miscalibration in certain models (particularly the Qwen family) suggest that emotional coloring can serve as a practical probe for model brittleness. Model × emotion ECE ranges from approximately 0.055 (Qwen-1.5B) to 0.622 (DS-Coder-6.7B).
> --- `kb/sources/.snapshots/prompt-stability-code-llms-emotion-personality-variations.md` @ `sha256:d29f22a52f74d5469e11d11c2ed3e446b60190ee2f7d4fe94116a03521e016fc` — §4.4, “RQ4: Effects of Valence×Arousal on Correctness and Calibration”

## Connections Found

The `/connect` discovery identified 11 candidate connections (4 strong, 7 moderate). PromptSE directly measures prompt sensitivity under intended meaning-preserving variants; the three-phenomena taxonomy, reliability/oracle framework, and bitter lesson boundary require separate interpretation.

**Strong connections:**

- [prompting-changes-failure-diagnosis-with-the-semantic-reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — **grounds**: the authors aim to hold functional requirements constant while varying emotional/stylistic expression. Conditional on preserved public meaning, performance differences show interpreter sensitivity to framing, not semantic underspecification; repeated sampling is aggregated into the reported stability measure. The 40% performance swing mentioned in the introduction is attributed to prior work, not this experiment. The nonsignificant model-level correlation does not establish independent axes. **Gap: this note does not yet cite the source.**

- [LLM output deviation requires three-way diagnosis](../theory/llm-output-deviation-requires-three-way-diagnosis.md) — **grounds**: the paper varies emotional/personality framing while intending to preserve task meaning and uses repeated samples under fixed decoding. Its reported AUC-E aggregates sample-based correctness into cross-variant sensitivity, without separately identifying within-prompt sampling dispersion. Conditional on meaning preservation, this does not test underspecification. The observed AUC-E range describes this setup, not a permanent property of language. **Bidirectional: already established.**

- [execution-indeterminism-is-a-property-of-the-sampling-process](../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **grounds**: the uniform temperature of 0.2 and 16 samples per prompt permit repeated evaluation, but the reported aggregate does not isolate within-prompt dispersion. Cross-variant comparison probes framing sensitivity under intended meaning preservation, not underspecification. **Gap: this note has no sources section at all.**

- [operational-signals-that-a-component-is-a-relaxing-candidate](../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **refines**: PromptSE's emotion/personality templates provide a structured test of prompt brittleness across three template-specified rewriting levels and 14,760 variants. Non-monotonic stability across the evaluated models does not distinguish a badly-fitting theory from limited capacity, training, distillation, or architecture effects. **The note now cites this ingest for its prompt-variation method.**

**Moderate connections:**

- [reliability-dimensions-map-to-oracle-hardening-stages](../theory/reliability-dimensions-map-to-oracle-hardening-stages.md) — **extends**: AUC-E is a concrete operationalization of the Robustness dimension (R_Rob), and the calibration analysis (ECE) maps to Predictability. The study did not find a statistically significant model-level correlation between Pass@1 and AUC-E in its sample; that result does not establish independent optimization axes. **The note now cites this ingest for its AUC-E measurement.**

- [writing-styles-are-strategies-for-managing-underspecification](../theory/writing-styles-are-strategies-for-managing-underspecification.md) — **complements**: complementary taxonomy viewed from opposite directions. The writing-styles note focuses on instruction-author strategies for narrowing the interpretation space; this paper demonstrates that user-side expression variation also functionally alters model behavior even when functional requirements are held constant. Both show stylistic register is functionally consequential, not cosmetic.

- [Structured-prompt gains do not establish training-distribution selection](../theory/structured-prompt-gains-do-not-establish-distribution-selection.md) — **evidenced-by**: Emotional framing changes accuracy and calibration, but the experiment does not distinguish training-distribution activation from instruction salience, assistant-persona effects, or tuning. It is another case where prompt movement alone cannot identify the mechanism.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **enables**: the emotion/personality templates offer candidate framing probes for a future decorrelation test. This study does not measure decorrelation between judges or calibrate its three rewriting levels as decorrelation strength.

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — **extends**: the ECE analysis provides additional evidence for the calibration-vs-discrimination distinction. Model-specific ECE shifts under emotional prompting demonstrate that calibration properties are fragile under surface-level perturbations — even calibration improvements from Rabanser et al. may be brittle under realistic usage conditions.

- [bitter-lesson-boundary](../theory/exact-implementation-does-not-validate-a-requirement.md) — **extends**: the non-monotonic scaling finding (smaller Qwen-1.5B more stable than larger models) raises a question for the fixed-artifact distinction, but does not test it. The observed ranking does not identify whether scale, training, architecture, or distillation explains the differences; explicit optimization remains a hypothesis.

- [prompt-ablation-converts-human-insight-to-deployable-framing](../theory/prompt-ablation-converts-human-insight-to-deployable-framing.md) — **complements methodology**: both involve controlled prompt variation with fixed inputs. The ablation note varies framing to find which cognitive moves agents can execute reliably; this paper varies emotional/personality framing to measure stability. Methodological parallel: controlled variation as a diagnostic technique.

**Synthesis opportunities flagged:**

1. Whether performance and stability require different optimization objectives remains open; the nonsignificant correlation in this sample does not decide it. Previously recommended as a new note. Contributing notes: prompting-changes-failure-diagnosis-with-the-semantic-reference, reliability-dimensions-map-to-oracle-hardening-stages, the-augmentation-automation-boundary-is-discrimination-not-accuracy.
2. Systematic prompt variation as dual-purpose methodology — simultaneously a verification technique (decorrelating oracle checks) and a diagnostic technique (measuring brittleness to identify relaxing candidates).

## Extractable Value

1. **Performance-stability relationship remains unresolved** — Spearman rho = -0.433, p = 0.122 across 14 models, with a 95% CI of [-0.875, 0.249]. The study did not find a significant model-level correlation in this sample; it cannot establish independence or distinct optimization objectives. [quick-win]

2. **Non-monotonic scaling of stability** — smaller models (Qwen-1.5B) achieving the highest AUC-E shows that the largest model was not the most stable in this evaluation. This bounded ranking does not establish a scaling law or distinguish capacity limits from a badly-fitting theory; explicit optimization is a hypothesis to test. [experiment]

3. **Controlled perturbation distance methodology** — three template-specified rewriting levels (d=0.1, 0.2, 0.3) from light lexical changes through substantial transformation, with semantic preservation as a generation and validation aim. The levels suggest a candidate metamorphic-test design, not a calibrated distance scale or a transferable guarantee; a new application must check semantic invariance and sensitivity for itself. [experiment]

4. **Emotion-as-probe for confidence miscalibration** — high-arousal negative-valence prompts induce ECE shifts in specific model families (particularly Qwen). Novel diagnostic: emotional coloring as a stress test revealing calibration failures invisible to standard benchmarks. A training-distribution explanation is a conjecture; the experiment does not distinguish it from other causes of framing sensitivity. [deep-dive]

5. **AUC-E as a metric for prompt stability in this setup** — aggregates correctness-score differences across intended meaning-preserving variants and three selected rewriting levels. It does not quantify how much underspecification the specification introduces. [just-a-reference]

6. **SoftExec as probability-aware evaluation** — weights correctness by generation probability, distinguishing high-confidence correct solutions from lucky guesses. Addresses a real limitation of Pass@k. [just-a-reference]

## Curiosity Gate

**What is most surprising?** The non-monotonic scaling of stability is the standout finding. That Qwen-1.5B (a tiny, distilled model) achieves the highest stability score across all 14 models — including models 20x its size — is genuinely unexpected. The paper speculates about "simpler decision boundaries." An alternative conjecture is that distillation narrows the solution repertoire and thereby reduces measured variation without improving general robustness. Neither mechanism is tested here; out-of-domain success is not measured.

**What's the simpler account?** For the proposed performance-stability distinction: one possible explanation is that these are different properties measured by different instruments; the sample does not establish whether they correlate. Pass@1 measures success under the evaluated prompts and decoding policy; AUC-E measures aggregated sensitivity to the selected variants. Qwen2.5-Coder-7b scores high on Pass@1 (0.820) and lower on AUC-E (0.403), but the scores do not identify why. This example motivates measuring both properties, but it does not establish that they are statistically independent or require separate optimization.

## Limitations (our opinion)

**Narrow evaluation domain.** The study uses only HumanEval (164 problems, Python only). The benchmark supplies test suites for functional correctness, but these do not prove that all generated variants preserve public meaning or resolve every ambiguity in the task. The study measures sensitivity to intended meaning-preserving emotional/stylistic variation; it does not test the wider permitted-output space of an underspecified request (e.g., "refactor for readability" as discussed in [prompting-changes-failure-diagnosis-with-the-semantic-reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md)).

**Template generation introduces its own bias.** Variants are generated by DeepSeek-Chat using structured templates. This means "stylistic variation" is filtered through one LLM's interpretation of what frustrated/anxious/focused writing looks like. The paper acknowledges this but does not test whether human-written emotional variants produce the same sensitivity patterns. The perturbation distances (0.1, 0.2, 0.3) are defined by template instructions, not measured against any ground truth of linguistic distance.

**Statistical power for the headline claim.** The performance-stability correlation (rho = -0.433, p = 0.122) is presented as "no statistically significant negative correlation" — but with only 14 models, the study is underpowered to detect moderate effects. The confidence interval [-0.875, 0.249] spans a wide range including strong negative correlation. The interval does not rule out a substantial negative relationship; a larger model sample could reveal one that this study did not detect.

**Missing baselines.** The paper does not compare PromptSE against simpler stability measures — e.g., variance of Pass@k across random prompt rephrasings without the emotion/personality structure, or stability under purely syntactic transformations (reordering clauses, adding whitespace). Without these baselines, it's unclear how much value the psychologically grounded templates add over random paraphrasing — the approach Rabanser et al. already used in [towards-a-science-of-ai-agent-reliability](https://arxiv.org/pdf/2602.16666).

**No causal mechanism for the non-monotonic scaling finding.** The observation that smaller models can be more stable is interesting but unexplained. The paper speculates about "simpler decision boundaries" but provides no evidence for this mechanism. Alternative explanations (distillation artifacts in the Qwen-1.5B model, limited solution diversity in small models that happens to look like stability) are not ruled out.

**Single evaluation metric design choices.** AUC-E uses Simpson's rule across three points with equal weighting — but the choice of three distances, their specific values, and equal weighting are all design decisions that could produce different rankings under different choices. The paper does not perform sensitivity analysis on these meta-parameters.

## Recommended Next Action

Do not promote the proposed note "Performance and stability are decoupled optimization objectives" on the strength of this correlation result. A future study of the performance-stability relationship would need enough precision to distinguish a meaningful correlation from independence before making that claim; the current sample does not do so.
