# Connection Report: Prompt Stability in Code LLMs: Measuring Sensitivity across Emotion- and Personality-Driven Variations

**Source:** [prompt-stability-code-llms-emotion-personality-variations](kb/sources/prompt-stability-code-llms-emotion-personality-variations.md)
**Date:** 2026-03-11
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — scanned all 145 entries. Flagged candidates:
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — underspecification theory directly tested by this paper
  - [prompt-underspecification-is-a-property-of-the-specification-language](kb/notes/prompt-underspecification-is-a-property-of-the-specification-language.md) — the exact property this paper measures
  - [execution-indeterminism-is-a-property-of-the-sampling-process](kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — paper's methodology controls for this
  - [interpretation-errors-are-failures-of-the-interpreter-not-the-spec](kb/notes/interpretation-errors-are-failures-of-the-interpreter-not-the-spec.md) — miscalibration findings may reveal interpreter failures
  - [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — paraphrase brittleness signal
  - [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — robustness/predictability dimensions
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — AUC-E as oracle manufacturing
  - [constraining](kb/notes/constraining.md) — prompt standardization as constraining
  - [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) — style variation taxonomy
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — prompt variation as decorrelation
  - [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) — emotion templates as distribution selectors
  - [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — performance vs stability decoupling
  - [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — performance/stability as generality/reliability trade-off

**Topic indexes:**
- Read [llm-interpretation-errors](kb/notes/llm-interpretation-errors.md) — confirmed three-phenomena taxonomy is the primary framework; additional candidate: [synthesis-is-not-error-correction](kb/notes/synthesis-is-not-error-correction.md) (rejected — no substantive connection to prompt stability)
- Read [learning-theory](kb/notes/learning-theory.md) — no additional candidates beyond those already flagged

**Semantic search:** (via qmd)
- Query 1: "prompt sensitivity stability semantically equivalent phrasing variations emotion personality code generation"
  - notes collection top hits:
    - [commonplace-installation-architecture](kb/notes/commonplace-installation-architecture.md) (88%) — false positive, no semantic connection
    - [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) (50%) — evaluated, too generic
    - [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) (45%) — evaluated, connection too thin
    - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) (33%) — already flagged from index
    - [execution-indeterminism-is-a-property-of-the-sampling-process](kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) (33%) — already flagged
    - [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) (32%) — already flagged
    - [prompt-underspecification-is-a-property-of-the-specification-language](kb/notes/prompt-underspecification-is-a-property-of-the-specification-language.md) (32%) — already flagged
  - sources collection top hits:
    - [towards-a-science-of-ai-agent-reliability](kb/sources/towards-a-science-of-ai-agent-reliability.md) (42%) — already flagged from index scan

- Query 2: "performance stability decoupled optimization objectives robustness evaluation metrics calibration confidence"
  - [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) (88%) — already flagged
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) (50%) — already flagged
  - [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) (40%) — already flagged
  - [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) (29%) — already flagged

**Keyword search:**
- grep "paraphrase|prompt robustness|prompt sensitivity" — found 15 files; all relevant ones already in candidate set from index and semantic search
- grep "stability.*performance|decoupled.*objective" — only the target source itself (no existing KB note discusses this specific decoupling)
- grep "non-monotonic.*scal" — only the target source itself

**Link following:**
- From [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md): already references Rabanser et al.'s R_prompt metric as the paraphrase brittleness signal; no new candidates
- From [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md): links to oracle spectrum and spec mining; no new candidates
- From [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md): the "vary the prompt" decorrelation strategy is directly relevant; no new candidates beyond those already flagged

## Connections Found

- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: the paper empirically demonstrates the two-phenomena model at scale — 14 models, 14,760 prompt variants show that semantically equivalent instructions yield up to 40% performance swings, confirming that underspecification, not execution noise, drives the meaningful variation. The finding that performance and stability are statistically uncorrelated (Spearman rho = -0.433, p = 0.122) provides direct empirical evidence that semantic underspecification and execution quality are independent axes.

- [prompt-underspecification-is-a-property-of-the-specification-language](kb/notes/prompt-underspecification-is-a-property-of-the-specification-language.md) — **grounds** (target is seedling): the paper's core design holds functional requirements constant while varying only emotional/stylistic expression, measuring how much the specification language's underspecification affects output even when semantics are preserved. AUC-E quantifies this: it is a metric for how much underspecification the spec language introduces for a given model. The finding that no model achieves AUC-E near 1.0 (max is 0.646) confirms that underspecification is a permanent property of the language, not eliminable by better models.

- [execution-indeterminism-is-a-property-of-the-sampling-process](kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **grounds** (target is seedling): the paper's methodology explicitly separates the two phenomena. Temperature=0.2 with 16 samples per prompt measures indeterminism within each variant; comparing across variants measures underspecification. The SoftExec metric weights by generation probability, isolating the probability-level signal from binary pass/fail noise. This is the cleanest empirical separation of the two phenomena in the KB's source collection.

- [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **grounds** (target is seedling): the paper's emotion/personality templates are systematic metamorphic tests for paraphrase brittleness (Signal 1). PromptSE operationalizes this signal as a quantitative metric with controlled perturbation distances. The finding that smaller models (Qwen-1.5B) achieve superior stability (AUC-E 0.646) while larger models show greater variance directly supports the note's prediction that brittleness signals detect badly-fitting theories — larger models may encode more theories about prompt format rather than more robust specifications of meaning.

- [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — **extends** (target is seedling): AUC-E maps to the Robustness dimension (R_Rob), specifically prompt robustness. The paper's calibration analysis (ECE ranging from 0.055 to 0.622 across model-emotion combinations) maps to the Predictability dimension. The paper provides richer perturbation structure than Rabanser et al.'s simple paraphrases — controlled emotion/personality templates at three distance levels — which could refine R_prompt measurement. The decoupling finding (performance and stability uncorrelated) independently confirms the reliability study's core principle that capability and reliability are independent.

- [towards-a-science-of-ai-agent-reliability](kb/sources/towards-a-science-of-ai-agent-reliability.md) — **extends**: both papers study LLM robustness to input variation using 14 models, but PromptSE provides a richer perturbation framework — psychologically grounded emotion/personality templates at controlled distances versus simple instruction paraphrases. PromptSE's AUC-E metric offers a continuous stability measure complementary to Rabanser's discrete R_prompt. The PromptSE finding about non-monotonic scaling (smaller models more stable) adds a dimension Rabanser's study noted but didn't systematically characterize (their observation that larger models are less consistent because they have more solution strategies).

- [error-correction-works-above-chance-oracles-and-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **exemplifies**: the paper's emotion templates are a structured methodology for generating the "vary the prompt" decorrelation strategy the error correction note recommends. The paper empirically demonstrates that prompt variation produces different failure modes across models and emotions — exactly the decorrelation signal needed for oracle amplification. The perturbation distance control (d=0.1, 0.2, 0.3) provides a way to tune the strength of decorrelation.

- [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) — **extends** (target is seedling): the paper's emotion/personality templates are a complementary taxonomy of how natural language variation affects LLM interpretation. The writing-styles note focuses on instruction-author strategies (prescriptive, prohibitive, etc.); the paper focuses on user-side expression variation (emotion, personality). Both demonstrate that stylistic/emotional register is not cosmetic but functionally consequential for LLM output quality. The paper provides quantitative evidence (up to 40% performance swings) for the mechanism the writing-styles note describes theoretically.

- [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) — **extends** (target is seedling): the paper's emotion templates empirically demonstrate the distribution-selection mechanism from the opposite direction. While the structure note argues that formal structure activates high-quality distributions, the PromptSE paper shows that emotional coloring (frustrated, anxious, stressed) activates DIFFERENT distributions — some associated with lower-quality or miscalibrated outputs. The confidence miscalibration finding (high-arousal negative-valence prompts induce ECE shifts) is direct evidence that stylistic framing selects training distributions with different calibration properties.

**Bidirectional candidates** (reverse link also worth adding):
- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) <-> source — the source provides the strongest empirical grounding for the two-phenomena model in the KB
- [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) <-> source — the source operationalizes Signal 1 (paraphrase brittleness) with a richer quantitative framework than the Rabanser study already cited

## Rejected Candidates

- [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) — too generic. The connection would be "this paper tests prompts, and the note says testing applies to prompting." No specific insight gained by linking.
- [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) — the paper doesn't address output storage as a strategy. The connection would have to route through constraining theory, which is too indirect.
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — the paper's four-quadrant framework maps loosely to the generality/reliability trade-off, but the note discusses learning mechanisms, not evaluation metrics. The connection would be forced.
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — initially considered: high-performance-low-stability models exemplify the augmentation/automation distinction. But the paper doesn't discuss augmentation or automation, and the connection relies on us importing concepts the paper doesn't use. Weak.
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — AUC-E is tangentially related as "oracle manufacturing" but the paper doesn't frame itself in oracle terms and the connection would require more interpretation than substance.
- [constraining](kb/notes/constraining.md) — the paper's recommendation for prompt standardization maps to constraining, but the connection is through vocabulary translation, not through a specific insight one provides the other.
- [commonplace-installation-architecture](kb/notes/commonplace-installation-architecture.md) — false positive from qmd (88% score!); no semantic connection whatsoever. The high score likely reflects shared structural patterns in YAML frontmatter.
- [synthesis-is-not-error-correction](kb/notes/synthesis-is-not-error-correction.md) — the paper uses multi-sample generation and averaging, but it's an evaluation methodology, not an agent aggregation architecture. No genuine connection.
- [interpretation-errors-are-failures-of-the-interpreter-not-the-spec](kb/notes/interpretation-errors-are-failures-of-the-interpreter-not-the-spec.md) — initially flagged because miscalibration could indicate interpreter failures. But the paper doesn't distinguish between the LLM choosing an unexpected valid interpretation and the LLM producing an invalid output. The connection would require imposing a taxonomy the paper doesn't use. Dropped to avoid forcing it.

## Index Membership

- [llm-interpretation-errors](kb/notes/llm-interpretation-errors.md) — the paper provides empirical grounding for the three-phenomena taxonomy, particularly the underspecification and indeterminism phenomena; could be listed under "Related notes in other areas" or as a source reference
- [learning-theory](kb/notes/learning-theory.md) — the paper's findings about stability as distinct from performance contribute to the understanding of what learning mechanisms (constraining) need to address; weaker fit than llm-interpretation-errors

## Synthesis Opportunities

**Prompt variation as a dual-purpose methodology.** Three notes converge on the idea that varying prompts serves two distinct purposes simultaneously: (1) as a decorrelation strategy for error correction ([error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)), and (2) as a diagnostic for model robustness ([operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md)). The PromptSE paper provides a systematic framework (controlled emotion/personality templates at graded distances) that could serve both purposes. A synthesis note could argue: "systematic prompt variation is simultaneously a verification technique (decorrelating checks to amplify oracle strength) and a diagnostic technique (measuring brittleness to identify relaxing candidates) — the same methodology serves error correction and architecture evaluation."

## Flags

- **qmd false positive**: commonplace-installation-architecture scored 88% on the first semantic search — the highest score — despite having zero semantic relevance to prompt stability. This suggests qmd's ranking may be overweighting structural/format similarity (both files have YAML frontmatter with similar fields) over semantic content.
- **No existing ingest**: the source has no `.ingest.md` file yet. An ingest would formalize the connections found here and extract additional value (the non-monotonic scaling finding, the four-quadrant framework for model selection, the perturbation distance methodology).
