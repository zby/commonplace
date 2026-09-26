---
description: "Curated head for the document-system tag — how KB documents are typed, written, structured, tested, and retained: type contracts, writing conventions, text testing and validation, documentation retention, and claim repair"
type: types/tag-readme.md
---

# Document system

This tag gathers how KB documents are typed, written, structured, and checked: document types and type contracts, writing conventions such as claim titles, testing and validating text, how directories and taxonomies organize a KB, what documentation to retain and how to segment it, and how defeated claims get repaired. No single defining note anchors it; [human-LLM differences are load-bearing](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) states the dual-audience premise most members build on. Members are mostly notes, plus a reference definition and a reference proposal. Nearby but different: [artifact-analysis](./artifact-analysis-README.md) classifies any retained artifact by substrate, form, lineage, and authority; a note belongs here when its question is how a document is written, structured, or checked.

For how the live Commonplace system uses global and collection-local type contracts, see [collections and types](../reference/collections-and-types.md).

## Foundations

- [note base type](../types/note.md) — the base structured type: required path-valued type and description, optional traits and tags, and optional committed human verification
- [text root type](../types/text.md) — the empty root type: no frontmatter, always valid
- [human-llm-differences-are-load-bearing-for-knowledge-system-design](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — knowledge systems produce dual-audience documents (human + LLM), making cognitive differences a first-class design concern for type and convention design
- [design-for-the-first-time-human-except-on-access-cost](../notes/design-for-the-first-time-human-except-on-access-cost.md) — refines the dual-audience heuristic: design for newcomer-human ergonomics except where agent access mode makes whole-artifact reads expensive
- [opposed recompute factors do not decide documentation segmentation](../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) — crossed savings and recurrence rankings need measured magnitudes even to order cache value, while segmentation also depends on whether specialization repays another maintained content layer
- [addressability grain, not compression ratio, sets a matched selective-read floor](../notes/addressability-grain-sets-a-matched-selective-read-floor.md) — for a known question with one discriminating unit on each path, the smaller addressed unit sets the retrieval floor; opposite Commonplace cases show why whole-artifact compression does not decide it
- [why-directories-despite-their-costs](../notes/why-directories-despite-their-costs.md) — directories buy one-two orders of magnitude of navigable scale but each new directory taxes routing, search config, and cross-directory linking
- [a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults](../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — type and label taxonomies are open local choices, while the former register taxonomy became clone-once collection prototypes; the fixed points are stipulated answerability and enforced contract declaration, not certified universals
- [A framework rule with a boundary-preserving rival is not an inherited constraint](../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) — the complement: a one-way demotion test — a rule whose rival preserves the boundary invariants (consumer, substrate, domain, machinery) is a design choice; a rule with no rival found is only undemoted, not certified

## Writing Conventions

- [title-as-claim-enables-traversal-as-reasoning](../notes/title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link traversal read as reasoning chains; topical titles break this, and multi-claim documents get different title conventions

## Testing

- [automated-tests-for-text](../notes/automated-tests-for-text.md) — text artifacts can be tested with the same pyramid as software: deterministic checks, LLM rubrics, corpus compatibility
- [text-testing-framework](../notes/text-testing-framework.md) — reference framework: contracts per document type, test pyramid (deterministic/LLM rubric/corpus), production workflow
- [deterministic-validation-should-be-a-script](../notes/deterministic-validation-should-be-a-script.md) — hard-oracle checks (enums, link resolution, frontmatter structure) belong in a script, not an LLM skill; the argument behind what is now `commonplace-validate`
- [unit-testing-llm-instructions-requires-mocking-the-tool-boundary](../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) — skills are programs whose I/O boundary is tool calls; mocking that boundary enables instruction-level testing that complements text artifact testing

## Claim Quality and Repair

- [generality bought to avoid counterexamples is paid for in precision](../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — widening a claim's vocabulary to survive counterexamples keeps content flat; unreadability is the symptom
- [narrowing bought to survive review is paid for in content](../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — shrinking a defeated claim's subject can end in an analytic title that passes every gate and says nothing
- [domain-pricing-routes-an-exception-to-idealization-assessment](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) — the workflow shape for defeated-but-retainable claims: domain pricing opens an idealization assessment, adequacy evidence decides it, and pricing-gated acceptance is an immunizing slot

## Decisions

- [084-kind rules live in type specs and operations in instructions](../reference/adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) — where a document kind's rules are stated and where its procedures live; the collection contracts (`COLLECTION.md`) replaced the old writing guide

## Related Tags

- [type-system](./type-system-README.md) — sub-area: why documents have types, their roles, and how structured writing improves quality
- [architecture](./architecture-README.md) — storage substrate and layout decisions that depend on document structure
- [links](./links-README.md) — [title-as-claim](../notes/title-as-claim-enables-traversal-as-reasoning.md) bridges both areas: it's a writing convention that enables link semantics
- [learning-theory](./learning-theory-README.md) — the type ladder instantiates the constraining gradient for documents
