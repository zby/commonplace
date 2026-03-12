# Connection Report: AI Components for a Deterministic System (An Example)

**Source:** [eric-evans-ai-components-deterministic-system](kb/sources/eric-evans-ai-components-deterministic-system.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — scanned all 149 entries. Flagged candidates:
  - [constraining](kb/notes/constraining.md) — Evans' "freeze the schema" is constraining
  - [codification](kb/notes/codification.md) — moving from natural language categories to frozen taxonomy is a form of codification
  - [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) — already links to the Evans analysis note
  - [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) — extracting deterministic verifiers from stochastic behavior
  - [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) — Evans' "use established standards for generic domains" raises bitter lesson questions
  - [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operationalizes the codify/relax cycle Evans implicitly describes
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — Evans' core problem is underspecification
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — the verifiability gradient
  - [document-classification](kb/notes/document-classification.md) — rejected: this is about document types in the KB, not classification as Evans means it
  - [sift-kg](kb/notes/related-systems/sift-kg.md) — schema discovery from sources is the same modeling/classification separation
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — the constraining gradient applies to Evans' technique
  - [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) — existing analysis note of the same article

**Topic indexes:**
- Read [learning-theory](kb/notes/learning-theory.md) implicitly via candidates — all core connections are in the learning-theory area

**Semantic search:** (via qmd)
- query "separating modeling from classification tasks freezing schema deterministic AI output" --collection notes:
  - [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) (93%) — the existing analysis note; strong match, same article
  - [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) (56%) — already references Evans; mechanism overlap
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) (42%) — foundational framework Evans' problem maps to
  - [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) (38%) — skip, connection is too generic (both involve structuring AI work)
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) (37%) — the gradient parallels Evans' approach
  - [title-as-claim-enables-traversal-as-reasoning](kb/notes/title-as-claim-enables-traversal-as-reasoning.md) (35%) — skip, no genuine connection
  - [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) (33%) — Evans' key insight about when to use established standards maps to this
  - [scenario-decomposition-drives-architecture](kb/notes/scenario-decomposition-drives-architecture.md) (33%) — skip, surface vocabulary overlap only
  - [decomposition-rules-for-bounded-context-scheduling](kb/notes/decomposition-rules-for-bounded-context-scheduling.md) (33%) — skip, different domain
- query "separating modeling from classification tasks freezing schema deterministic AI output" --collection sources:
  - (self) (93%) — the source being connected
  - [koylanai-personal-brain-os-ingest](kb/sources/koylanai-personal-brain-os-ingest.md) (51%) — skip, surface similarity only (both about file-based systems)
  - [towards-a-science-of-ai-agent-reliability](kb/sources/towards-a-science-of-ai-agent-reliability.ingest.md) (34%) — consistency dimension is what Evans achieves
- query "using established standards published taxonomies instead of custom AI generated categories" --collection notes:
  - [siftly](kb/notes/related-systems/siftly.md) (92%) — high score but misleading; Siftly uses predefined categories, which parallels Evans, but connection is thin
  - [sift-kg](kb/notes/related-systems/sift-kg.md) (38%) — schema discovery mirrors Evans' modeling/classification split
  - [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) (35%) — already captured
  - [design-methodology-borrow-widely-filter-by-first-principles](kb/notes/design-methodology-borrow-widely-filter-by-first-principles.md) (34%) — skip, connection is thematic but not specific enough

**Keyword search:**
- rg "evans|modeling.*classification|taxonomy.*freeze" kb/ — found: [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md), [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) (both already in candidates)
- rg "separate.*modeling|freeze.*taxonomy|freeze.*schema|canonical.*categories|published.*standards" kb/ — found: [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md), [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) (no new candidates)

**Link following:**
- From [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md): links to [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md), [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md), [research/adaptation-agentic-ai-analysis](kb/notes/research/adaptation-agentic-ai-analysis.md)
- From [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md): links to [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md), [constraining](kb/notes/constraining.md), [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — the existing Evans reference is here, as a specific instance of the "constrain the generator" strategy

## Connections Found

The source snapshot is a raw capture of Evans' article. There is already an existing **analysis note** at `kb/notes/related_works/evans-ai-components-deterministic-system.md` that connects deeply to the KB's learning theory. The connections below are for the source snapshot itself; most would be mediated through the analysis note rather than linking directly.

- [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) — **extends**: the analysis note is a direct KB interpretation of this source; the source grounds everything the analysis note claims about Evans' framework. This is the primary connection — the source-to-analysis link.

- [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) — **exemplifies**: Evans' "freeze the taxonomy then classify" is the specific instance already cited in this note's "constrain the generator" strategy (Strategy 1). The source provides the concrete case study (OpenEMR domain classification) behind the reference.

- [constraining](kb/notes/constraining.md) — **exemplifies**: Evans' entire approach is constraining — constraining the interpretation space by freezing a taxonomy before classification. The "modeling phase" admits many valid schemas; freezing one is committing to a single interpretation. This maps to the constraining spectrum: from underspecified "create a classification" to committed "apply these specific categories."

- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — **exemplifies**: Evans demonstrates the two phenomena. Asking "what domain does this code address?" is semantically underspecified (admits multiple valid category schemes). Running the same prompt multiple times shows execution indeterminism (inconsistent formats). His solution — separate modeling from classification — is narrowing the interpretation space for the classification step by pre-resolving the modeling ambiguity.

- [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) — **exemplifies**: Evans' iterative refinement phase (sampling, critic models, judge models) is spec mining — observing LLM behavior, identifying patterns, extracting them into a frozen schema. The frozen NAICS taxonomy is the extreme case: someone else already mined the spec, so you skip the observation step entirely.

- [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) — **grounds**: Evans' key insight — "Creating a classification system is a modeling task, which is much harder than the classification task itself" — maps to the arithmetic/vision-feature distinction. Classification against a frozen schema is in the arithmetic regime (spec IS the problem). Creating the schema is in the vision-feature regime (spec is a theory about what categories are useful). Evans' recommendation to use NAICS is an arithmetic-regime choice: adopt a spec that already exists rather than trying to create one.

- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — **exemplifies**: Evans' approach is codification in the blurry zone. His "incremental updates" pattern (check new code against existing categories, add genuinely new ones) is the relax/re-codify cycle operating on a taxonomy rather than on code.

**Bidirectional candidates** (reverse link also worth adding):
- [related_works/evans-ai-components-deterministic-system](kb/notes/related_works/evans-ai-components-deterministic-system.md) <-> source — **grounds/extends**: the source grounds the analysis; the analysis extends the source into KB vocabulary. Both directions are useful for navigation.

## Rejected Candidates

- [document-classification](kb/notes/document-classification.md) — despite sharing the word "classification," Evans' article is about domain classification of code, not document type taxonomies. The KB note is about the internal type system. No genuine conceptual overlap beyond vocabulary.
- [siftly](kb/notes/related-systems/siftly.md) — Siftly uses predefined categories with AI-readable descriptions, which superficially parallels Evans' "use published standards." But the connection is too thin: Siftly's categories are hand-coded application features, not a response to the modeling-vs-classification problem Evans identifies.
- [sift-kg](kb/notes/related-systems/sift-kg.md) — sift-kg's schema discovery (sampling documents, asking LLM to design entity types, then caching the schema) is structurally similar to Evans' modeling/classification separation. However, sift-kg discovers the schema automatically from the corpus, while Evans argues for human-driven or published schemas. The parallel is suggestive but the relationship is shallow — both separate schema creation from schema application, but they draw opposite conclusions about who should create the schema.
- [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) — both involve structuring AI work, but the connection is too generic to be useful.
- [towards-a-science-of-ai-agent-reliability](kb/sources/towards-a-science-of-ai-agent-reliability.ingest.md) — Evans achieves consistency (one of Rabanser's four dimensions) through schema freezing. But the connection is indirect — Evans' technique is one instance of many constraining techniques that improve consistency, and the reliability paper provides the vocabulary rather than the technique. Not specific enough to link directly from the source.
- [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — the constraining gradient is relevant, but the connection runs through [constraining](kb/notes/constraining.md) rather than directly from Evans' source. Adding a direct link would bypass the abstraction.

## Index Membership

- [learning-theory](kb/notes/learning-theory.md) — the source exemplifies constraining and codification concepts. The analysis note at `related_works/` already carries this area membership implicitly through its links.
- The source itself (in `kb/sources/`) is listed in the auto-generated [sources/index.md](kb/sources/index.md).

## Synthesis Opportunities

None detected. The existing analysis note at `kb/notes/related_works/evans-ai-components-deterministic-system.md` already performs the synthesis work — mapping Evans' framework to the KB's vocabulary (constraining, codification, underspecification, bitter lesson boundary). The source snapshot adds no new synthesis opportunities beyond what the analysis note captures.

## Flags

- **Legacy directory:** The analysis note lives in `kb/notes/related_works/` (underscore naming). The log already flags this: "kb/notes/related_works/: legacy directory with underscore naming; remaining files need triage." This source snapshot connects primarily through that analysis note, so its connection quality depends on whether the analysis note migrates to a proper location.
- **Source has no ingest file.** The source at `kb/sources/eric-evans-ai-components-deterministic-system.md` is a raw web-fetch capture without a corresponding `.ingest.md` analysis. The analysis work was done in `kb/notes/related_works/` instead, which pre-dates the ingest workflow. Running `/ingest` on this source would formalize the connection analysis.
