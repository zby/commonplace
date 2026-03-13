# Connection Report: Language Models, Like Humans, Show Content Effects on Reasoning Tasks

**Source:** [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — scanned all 145 entries. Flagged candidates:
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — description explicitly mentions "content effects on reasoning" and cites this paper
  - [human-llm-differences-are-load-bearing-for-knowledge-system-design](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — per-convention evaluation of human/LLM cognitive differences
  - [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) — structured templates and training data distribution selection
  - [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — adaptive fit vs explanatory reach maps to content effects
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — content effects as a source of correlated oracle errors
  - [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — content-dependent reasoning as a "vision feature" vs content-independent reasoning as "arithmetic"
  - [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — content effects as a mechanism shaping underspecification resolution
  - [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — distribution sensitivity signal

**Topic indexes:**
- Read [learning-theory](../../notes/learning-theory-index.md) — no additional candidates beyond index scan

**Semantic search:** (via qmd)
- query "content effects reasoning LLM human belief bias prior knowledge logical inference" in notes — top hits:
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) (93%) — direct citation, already flagged
  - [backlinks](../../notes/backlinks.md) (50%) — surface match on "reasoning", no semantic connection
  - [human-llm-differences-are-load-bearing-for-knowledge-system-design](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) (38%) — already flagged
  - [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) (34%) — already flagged
  - Remaining hits (33% and below): claim-notes-should-use-toulmin, skills-derive-from-methodology, context-efficiency, learning-is-not-only-about-generality — all surface vocabulary overlap, no genuine mechanism connection
- query in sources — self-match (93%), agentic-code-reasoning (50%, unrelated domain), ingest file (43%, companion file not a connection target)

**Keyword search:**
- grep "content effect|belief bias|dual.system|chain.of.thought" — found references only in human-writing-structures note and agent-skills-for-context-engineering (chain-of-thought mention, but in a different context — reliability improvement, not content bias reduction)
- grep "prior.*(knowledge|expectation|belief)|training.*(data|distribution).*reason" — found human-llm-differences and structure-activates-higher-quality (both already flagged)
- grep "distribution.sensitivity" — found only relaxing-signals note (already flagged and evaluated)

**Link following:**
- From human-writing-structures-transfer: followed to claim-notes-should-use-toulmin, programming-practices-apply-to-prompting, structured-output-is-easier-for-humans-to-review, why-notes-have-types — none connect to the Lampinen paper specifically
- From structure-activates-higher-quality: followed to epiplexity source — the distribution-selection mechanism is independent from content effects; the paper is more relevant as evidence for the note's mechanism than a parallel

## Connections Found

**Already connected (confirmed existing links via ingest file):**
- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — **grounds**: direct empirical evidence for the note's central claim that LLMs exhibit human-like failure modes; the note already cites this source
- [human-llm-differences-are-load-bearing-for-knowledge-system-design](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **exemplifies**: the paper is a worked example of the per-convention evaluation methodology the note advocates (syllogisms transfer, Wason diverges); already connected via ingest
- [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — **extends**: content effects are the empirical manifestation of adaptive fit dominating explanatory reach; chain-of-thought as a mechanism for shifting toward explanatory reasoning; already connected via ingest

**New connection:**
- [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) — **grounds**: The Lampinen paper shows that chain-of-thought prompting reduces content bias by improving performance on abstract/unfamiliar conditions without degrading performance on familiar ones (section: "Chain-of-thought can sometimes push large models to rely more on logic"). This is direct empirical evidence that structured prompting shifts LLM output from content-biased (drawing from training data reflecting real-world statistical regularities) toward content-independent logical reasoning. The structure-activates note claims structured templates work by selecting higher-quality training distributions; the CoT finding demonstrates the mechanism — structured reasoning context does shift the model away from its default content-biased distribution. The Lampinen paper also shows this effect survives instruction tuning and scaling (Flan-PaLM 2 and GPT-3.5 show same content effects), meaning the distribution-selection effect cannot be achieved through scale alone — it requires explicit structural intervention.

**Bidirectional candidates** (reverse link also worth adding):
- [structure-activates-higher-quality-training-distributions](../../notes/structure-activates-higher-quality-training-distributions.md) <-> source — **grounds**: the source provides empirical evidence (CoT reducing content bias) that strengthens the distribution-selection thesis; the note provides a theoretical mechanism (distribution selection) that explains why the CoT effect in the source works

## Rejected Candidates

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — The paper shows content effects are shared across different models (Chinchilla, PaLM 2, GPT-3.5), which is relevant to the decorrelation requirement. However, the connection is indirect: the paper doesn't discuss error correction or voting, and the error-correction note doesn't address content bias. The implication (model diversity may not decorrelate content-bias errors) is a reasonable inference but requires a synthesis step neither artifact performs. Better as a synthesis opportunity than a direct link.
- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — Content-dependent reasoning could be framed as "vision features" (learned heuristics about the world) vs content-independent reasoning as "arithmetic" (pure logical rules). But the paper doesn't address scaling in the way the bitter lesson note does — it compares models of different sizes and finds "larger models tend to be more accurate overall" but "not less content-biased." This is potentially interesting evidence about the boundary, but the paper frames it as a robustness finding, not a scaling argument. The connection requires reframing the paper's claims beyond what it argues.
- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — Two steps removed: bitter lesson boundary is already indirect, and this note operationalizes a different aspect (the codify/relax cycle). No direct mechanism shared.
- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — Content effects could be seen as a mechanism by which LLMs resolve underspecified instructions (prior expectations from training shape the projection). But the underspecification note operates at a different level of analysis — it's about the semantics of natural language specs, not about reasoning biases. Connecting them would require a bridging argument ("content effects explain why particular interpretations are selected") that neither artifact makes. The overlap is conceptual, not operational.
- [operational-signals-that-a-component-is-a-relaxing-candidate](../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — Signal 5 (distribution sensitivity) superficially maps to content effects. But the note's distribution sensitivity refers to degradation when a deployed component encounters shifted input distributions, while the paper's content effects refer to reasoning performance varying by semantic content of the task. Different phenomena sharing vocabulary.
- [writing-styles-are-strategies-for-managing-underspecification](../../notes/writing-styles-are-strategies-for-managing-underspecification.md) — No genuine connection. The note is about how instruction styles narrow interpretation spaces. The paper is about reasoning biases. Surface vocabulary overlap only ("interpretation," "reasoning").

## Index Membership

- The source is a scientific paper in kb/sources/ — it belongs in the sources index (already listed in kb/sources/index.md).
- No note-level index membership applicable (this is a source, not a note). The ingest file already routes connections to relevant area indexes via the connected notes.

## Synthesis Opportunities

1. **Content-bias decorrelation as an error-correction constraint**: The Lampinen paper shows content effects are shared across architecturally different models (Chinchilla, PaLM 2, GPT-3.5) trained on different data. Combined with the error-correction note's requirement for decorrelated checks, this implies: model diversity alone is insufficient for decorrelating reasoning errors, because all models trained on human-generated text inherit the same content biases. Decorrelation strategies would need to vary the semantic framing (e.g., metamorphic checks that rephrase the content) rather than just the model. This is not stated in either artifact but follows from combining them.

2. **Scaling vs structured intervention for reasoning quality**: The paper shows content effects survive scaling (larger models are not less content-biased) and instruction tuning (Flan-PaLM 2 shows same effects as base PaLM 2). The structure-activates note argues structured templates shift the distribution. Combined: for reasoning quality in KB operations, structural interventions (templates, Toulmin sections) are not a temporary measure pending better models — they're a permanent architectural feature because the underlying content bias doesn't dissolve with scale. This strengthens the KB's bet on structured types beyond what either artifact argues alone.

## Flags

- No split candidates.
- No tensions detected.
- The ingest file (../../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) already performed a thorough connection analysis that identified the same three main connections. The one new connection found here (structure-activates-higher-quality-training-distributions) was not in the ingest file's analysis but is a genuine extension.
