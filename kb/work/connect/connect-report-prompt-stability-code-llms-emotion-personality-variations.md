# Connection Report: Prompt Stability in Code LLMs: Measuring Sensitivity across Emotion- and Personality-Driven Variations

**Source:** [prompt-stability-code-llms-emotion-personality-variations.md](kb/sources/prompt-stability-code-llms-emotion-personality-variations.md)
**Ingest:** [prompt-stability-code-llms-emotion-personality-variations.ingest.md](kb/sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md)
**Date:** 2026-03-12
**Depth:** standard

## Note Summary

Ma et al. introduce PromptSE, a framework for measuring code generation model stability under semantically equivalent prompt variations driven by emotion and personality templates. Key findings across 14 models and 14,760 variants: (1) performance (Pass@1) and stability (AUC-E) are statistically uncorrelated (Spearman rho = -0.433, p = 0.122), making them decoupled optimization objectives; (2) stability does not scale monotonically with model size (Qwen-1.5B achieves highest AUC-E); (3) emotional prompting reveals confidence miscalibration (ECE) invisible to standard benchmarks; (4) PromptSELight approximates PromptSE for closed-source screening (Pearson ~0.72).

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (full 158-entry scan). Flagged candidates by description relevance:
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — core framework: two-phenomena model directly tested
  - [execution-indeterminism-is-a-property-of-the-sampling-process](kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — paper's methodology cleanly separates this from underspecification
  - [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — paraphrase brittleness is Signal 1; already references this source
  - [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — AUC-E maps to robustness dimension
  - [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — calibration vs discrimination distinction, same Rabanser backdrop
  - [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) — complementary taxonomy: author-side vs user-side stylistic variation
  - [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) — distribution selection from opposite direction
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — emotion templates as decorrelation strategy
  - [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) — non-monotonic scaling of stability
  - [prompt-ablation-converts-human-insight-to-deployable-framing](kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — controlled prompt variation methodology
  - [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — stability as property requiring explicit optimization

**Topic indexes:**
- Read [llm-interpretation-errors](kb/notes/llm-interpretation-errors-index.md) — already cites this source in the introduction paragraph; connection to all three phenomena established. Additional candidates from index: oracle-strength-spectrum, synthesis-is-not-error-correction (rejected -- no substantive connection).
- Read [learning-theory](kb/notes/learning-theory-index.md) — constraining section confirms operational-signals and bitter-lesson-boundary connections. No additional candidates beyond index scan.

**Semantic search (via qmd):**
- query "prompt sensitivity stability robustness model evaluation reliability" --collection notes -n 15:
  - llm-context-is-composed-without-scoping (88%) — high score due to "stability" vocabulary, but no genuine content connection to prompt sensitivity. Rejected.
  - operational-signals-that-a-component-is-a-relaxing-candidate (56%) — confirmed candidate
  - oracle-strength-spectrum (39%) — indirect connection via reliability-dimensions; not strong enough standalone
  - prompt-ablation-converts-human-insight-to-deployable-framing (34%) — confirmed candidate
  - programming-practices-apply-to-prompting (32%) — checked; testing section relevant but connection is thin
- query "prompt sensitivity stability robustness model evaluation reliability" --collection sources -n 10:
  - self-match (93%) — expected
  - towards-a-science-of-ai-agent-reliability.ingest (46%) — confirmed companion source
  - agent-behavioral-contracts (36%) — already referenced by reliability-dimensions note; no direct link needed
- query "underspecification interpretation variation phrasing semantically equivalent" --collection notes -n 15:
  - execution-indeterminism (93%) — confirmed candidate
  - agentic-systems-interpret-underspecified-instructions (56%) — confirmed candidate
  - llm-interpretation-errors (47%) — confirmed (index already references source)
  - storing-llm-outputs-is-constraining (46%) — checked; not a direct connection to this paper
  - writing-styles-are-strategies-for-managing-underspecification (41%) — confirmed candidate
- query "scaling model size bitter lesson stability non-monotonic" --collection notes -n 10:
  - bitter-lesson-boundary (41%) — confirmed candidate
  - codification-and-relaxing-navigate-the-bitter-lesson-boundary (42%) — checked; indirect via bitter-lesson
- query "testing metamorphic invariance evaluation metric" --collection notes -n 10:
  - quality-signals-for-kb-evaluation (91%) — metamorphic testing connection; checked but the connection to this paper specifically is weak (metamorphic concept is general)
- query "emotion personality style calibration confidence" --collection notes -n 10:
  - operational-signals-that-a-component-is-a-relaxing-candidate (91%) — already confirmed
  - the-augmentation-automation-boundary-is-discrimination-not-accuracy (50%) — confirmed candidate

**Keyword search:**
- grep "prompt stability|prompt sensitivity|prompt robustness|AUC-E|PromptSE" in kb/notes/:
  - operational-signals-that-a-component-is-a-relaxing-candidate.md — already references this source
  - interpretation-errors-are-failures-of-the-interpreter.md — checked but no substantive connection beyond shared domain
  - llm-interpretation-errors-index.md — already cites this source
  - reliability-dimensions-map-to-oracle-hardening-stages.md — confirmed
- grep "paraphrase|brittleness|perturbation|sensitivity" in kb/notes/:
  - 17 files found; most already captured. New: spec-mining-as-codification.md (mentions perturbation in passing); not a direct connection.

**Link following:**
- From operational-signals: followed links to bitter-lesson-boundary, oracle-strength-spectrum, error-correction, codification-and-relaxing. Cluster confirmed: the bitter-lesson / oracle / relaxing-signals constellation is the primary neighborhood.
- From llm-interpretation-errors: this source is already referenced as the primary empirical evidence for the three-phenomena separation. No new connections discovered via link following.
- From reliability-dimensions: followed to the-augmentation-automation-boundary, which deepens the calibration-vs-discrimination distinction. The paper's ECE analysis (confidence miscalibration) is evidence for the same phenomenon.

## Connections Found

### Strong connections (source already referenced by target or strong mutual grounding)

- [llm-interpretation-errors](kb/notes/llm-interpretation-errors-index.md) — **grounds**: the paper empirically separates all three phenomena in the taxonomy: temperature+sampling within each variant isolates indeterminism, cross-variant comparison isolates underspecification, and systematic degradation under emotional prompts reveals interpretation bias. The llm-interpretation-errors index already cites this source with a paragraph summarizing the separation. **Bidirectional: already established.**

- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: holding functional requirements constant while varying only emotional/stylistic expression produces up to 40% performance swings across 14 models, providing the strongest empirical evidence in the KB that semantic underspecification (not execution noise) drives meaningful output variation. The performance-stability decoupling (rho = -0.433) directly confirms that underspecification and execution quality are independent axes. The agentic-systems note does not currently cite this source.

- [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **refines**: PromptSE's emotion/personality templates provide a richer operationalization of Signal 1 (paraphrase brittleness) than simple rephrasings -- three calibrated perturbation distances (d=0.1 light lexical, d=0.2 moderate style, d=0.3 substantial transformation) across 14,760 variants. The non-monotonic scaling finding (smaller models more stable) supports the note's interpretation that brittleness detects badly-fitting theories rather than capacity limitations. **Bidirectional: already established** (note already references this source).

- [execution-indeterminism-is-a-property-of-the-sampling-process](kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **grounds**: the paper's methodology provides the cleanest empirical separation of indeterminism from underspecification in the KB's source collection. Temperature=0.2 with 16 samples per prompt measures indeterminism within each variant; comparing across semantically equivalent variants measures underspecification. This is exactly the distinction the note argues is conceptually important but often confused.

### Moderate connections

- [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — **extends**: AUC-E is a concrete operationalization of robustness oracle hardening (R_Rob from Rabanser et al.). The calibration analysis (ECE) maps to predictability. The performance-stability decoupling independently confirms the note's claim that capability and reliability are independent optimization axes. The note does not currently cite this source.

- [writing-styles-are-strategies-for-managing-underspecification](kb/notes/writing-styles-are-strategies-for-managing-underspecification.md) — **complements**: the writing-styles note taxonomizes instruction-author strategies for narrowing the interpretation space; this paper empirically demonstrates that user-side expression variation (emotional tone, personality style) also functionally alters model behavior even when functional requirements are held constant. Both show that stylistic register is functionally consequential, not cosmetic. The distinction is direction: the writing-styles note looks at how authors write instructions; this paper looks at how users write requests.

- [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) — **grounds from opposite direction**: the paper demonstrates the distribution-selection mechanism in reverse -- emotional coloring (frustrated, anxious) activates different training distributions, some with miscalibrated confidence properties (ECE ranging 0.055 to 0.622). Where the structure-activates note argues that structured templates steer toward higher-quality distributions, this paper shows that emotional framing steers toward different-quality distributions. Same mechanism, opposite valence.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **enables**: the paper's emotion/personality templates provide a structured methodology for the "vary the prompt" decorrelation strategy described in the error-correction note. The perturbation distance control (d=0.1, 0.2, 0.3) provides calibrated decorrelation strength. The note already lists prompt variation as a decorrelation strategy; this paper provides the most structured implementation of it in the KB's source collection.

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — **extends**: the paper's ECE analysis provides additional evidence for the calibration-vs-discrimination distinction. Model-specific ECE shifts under emotional prompting (particularly Qwen family) demonstrate that calibration properties are fragile under surface-level perturbations -- extending the Rabanser et al. finding that the note builds on. The paper does not test discrimination directly, but the calibration fragility it reveals adds a further complication: even the calibration improvements Rabanser et al. found may be brittle under realistic usage conditions.

- [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) — **extends**: the non-monotonic scaling finding (smaller Qwen-1.5B more stable than larger models) provides evidence for the note's core distinction. Stability appears to be a property that does not follow the same scaling patterns as performance -- suggesting it may be closer to the "vision feature" side of the boundary, requiring explicit optimization rather than emerging from scale. The mechanism is speculative but aligns with the note's prediction.

- [prompt-ablation-converts-human-insight-to-deployable-framing](kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — **complements methodology**: both involve controlled prompt variation with fixed inputs. The ablation note varies framing to find which cognitive moves agents can execute reliably; this paper varies emotional/personality framing to measure stability. The methodological parallel is: controlled variation as a diagnostic technique. The connection is methodological, not conceptual -- both use the same experimental structure for different purposes.

**Bidirectional candidates** (reverse link also worth adding):
- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) <-> source — **grounds**: the source provides the strongest empirical evidence for the two-phenomena separation; the note currently has no source reference to this paper.
- [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md) <-> source — **extends**: AUC-E as concrete robustness metric.

## Rejected Candidates

- **llm-context-is-composed-without-scoping** — ranked 88% in semantic search due to vocabulary overlap ("stability," "sensitivity") but the note is about context window scoping, not prompt stability. No genuine conceptual connection.
- **oracle-strength-spectrum** — indirect connection via reliability-dimensions; the paper doesn't directly address oracle strength concepts. The connection is real but mediated entirely through reliability-dimensions, making a direct link redundant.
- **programming-practices-apply-to-prompting** — the testing section is tangentially relevant (testing under variation) but the connection is too generic to be useful. An agent following this link would gain nothing specific.
- **quality-signals-for-kb-evaluation** — metamorphic testing is mentioned in both, but the shared concept is too generic (metamorphic testing as a technique). The paper's domain (code generation evaluation) is disjoint from KB evaluation.
- **automated-tests-for-text** / **text-testing-framework** — testing frameworks with metamorphic testing mention, but the connection is again the generic testing concept, not the specific findings about prompt stability.
- **storing-llm-outputs-is-constraining** — qmd ranked it at 46% via underspecification vocabulary, but the paper's contribution is about measuring sensitivity, not about constraining strategies. The connection would be "constraining reduces sensitivity" but that is implicit rather than articulated in either note.
- **codification-and-relaxing-navigate-the-bitter-lesson-boundary** — the non-monotonic scaling finding is relevant but the connection is already captured through bitter-lesson-boundary. Direct link would be redundant.

## Index Membership

- [llm-interpretation-errors](kb/notes/llm-interpretation-errors-index.md) — already listed in Sources section as primary empirical evidence for three-phenomena separation
- [learning-theory](kb/notes/learning-theory-index.md) — not a direct member, but the paper's findings are evidence for constraining theory (operational-signals) and the bitter lesson boundary. Connection is indirect through member notes.

## Synthesis Opportunities

1. **"Performance and stability are decoupled optimization objectives"** — the ingest report already recommends this note. It would argue that empirical evidence from this paper (four-quadrant distribution, rho = -0.433) and Rabanser et al. (capability gains outpacing reliability) confirms the KB's theoretical prediction that capability and reliability are independent axes. Contributing notes: [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md), [reliability-dimensions-map-to-oracle-hardening-stages](kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [the-augmentation-automation-boundary-is-discrimination-not-accuracy](kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), plus this source and the Rabanser et al. source.

2. **Systematic prompt variation as dual-purpose methodology** — PromptSE's controlled perturbation framework simultaneously serves as (a) a verification technique for decorrelating oracle checks (error-correction note) and (b) a diagnostic technique for detecting relaxing candidates (operational-signals note). The ingest report flagged this. Contributing notes: [error-correction-works-above-chance-oracles-with-decorrelated-checks](kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), [prompt-ablation-converts-human-insight-to-deployable-framing](kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md).

## Flags

- **Already well-connected:** The ingest report already identified the nine core connections, and the llm-interpretation-errors index already cites this source. The primary gaps are: (a) agentic-systems-interpret-underspecified-instructions does not yet cite this source despite being the foundational note it grounds, (b) reliability-dimensions note does not yet cite this source despite direct AUC-E/robustness mapping.
- **Ingest quality:** The ingest report is unusually thorough -- it identified all connections this discovery phase found, plus accurately assessed limitations. The recommended synthesis note ("Performance and stability are decoupled optimization objectives") remains unwritten.
