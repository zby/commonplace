---
description: "Explains how Commonplace combines Milo's grouped-link MOC pattern with validator-enforced completeness while treating Luhmann's non-exhaustive registers as a separate bounded analogue"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [kb-maintenance, document-system]
---

# An enforced tag-README is a MOC with a machine-checked contract

A tag-README is a Map of Content wearing a validator. In Nick Milo's stated sense, a MOC maps things in context and can take the form of a note whose links are clustered into groups. A Commonplace tag-README fits that positive description: its groupings and context phrases orient a reader through a topic. The `complete` and `covered_by` marks add machine-checked membership and coverage claims. The result is an inherited grouped-link map plus a local contract, not a claim that every MOC has the same structure or maintenance policy.

The mark contract lives in the [`tag-readme` type spec](../types/tag-readme.md). `complete: true` says the curated README links every note carrying the tag. `covered_by` says every note carrying the parent tag also carries at least one listed child tag. Both are recomputable claims about membership. Neither says that the grouping, ordering, or explanation is editorially adequate.

## The sources establish two bounded historical comparisons

[Milo defines a MOC](../sources/nick-milo-mocs-definition.ingest.md) as a cluster that maps things in context, helps gather, develop, and navigate ideas, and may be a digital note whose links are clustered into groups. This supports the grouped-link orientation half of the comparison. It does not establish that every MOC is annotated or selective, that a tag-README is exactly equivalent to every MOC, or that MOC practitioners never promise completeness.

The [Niklas Luhmann Archive](../sources/luhmann-archive-schlagwortregister.ingest.md) describes Luhmann's own keyword registers separately. It says those registers made no claim to complete term locations and named only the relevant entry points into the collection. This is evidence about Luhmann's registers, not evidence that the registers were MOCs or that all Zettelkasten and PKM practice rejects completeness claims.

These sources therefore do not support the stronger historical story that human PKM lacked completeness contracts because readers never needed them or maintainers could never afford them. The defensible inheritance claim is positive and narrower: Milo supplies a grouped-link mapping pattern, while Luhmann supplies a distinct example of non-exhaustive entry-point navigation.

## Commonplace adds a useful and enforceable stopping rule

The machine-checked delta follows from Commonplace's own routing semantics. An LLM reader may use `complete: true` as a stopping rule and skip a fallback by-tag search. [Indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md), so that shortcut is safe only while the membership claim remains true. Without the mark, the reader cannot treat the curated head as exhaustive.

The same system can recheck the claim mechanically. Validation compares the README's links with current tag membership and rejects a stale mark. Since [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), this enforced-or-omitted design avoids asking a model to trust an unchecked completeness claim.

Both parts matter to this local design. A cheap check without a consumer-visible stopping rule guards a promise nobody uses. A useful stopping rule without enforcement creates a stale trusted cache. This joint-necessity argument explains why Commonplace adds the marks; it does not claim that the same need or enforcement cost holds for every human knowledge system.

## The contract stops at membership

The validator checks set membership and child coverage. It cannot establish which topics deserve emphasis, which notes should be read first, or whether a context phrase explains a note's role well. Those remain editorial judgments. Milo's MOC definition supplies a useful model for grouped-link orientation, while Commonplace's marks constrain only the recomputable dimension beside it.

An enforced tag-README is therefore a MOC with a machine-checked contract in this precise sense: the artifact combines a grouped contextual map with explicit, validated membership claims. The sources identify the inherited patterns. The local argument identifies the added contract and its consumer.

## Scope

- The MOC comparison uses Milo's positive definition; it is not a survey of MOC practice.
- Luhmann's registers are a separate analogue and are not identified as MOCs.
- The evidence does not establish how often human-maintained maps promise completeness or why a particular tradition did or did not do so.

## Open Questions

- Do other MOC practitioners state explicit completeness or canonical-entry-point policies?
- Does the same map-plus-contract split apply to backlink pages, tag hierarchies, or folgezettel sequences?

---

Relevant Notes:

- [Human–LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — exemplifies: the general claim this note applies by separating a human-oriented mapping pattern from the contract used by an LLM reader
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the enforce-or-omit rule for the recomputable completeness claim
- [Indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — grounds: the fallback-suppression mechanism that makes a false completeness signal harmful
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: the economics under which a checked cached mark can serve a model reader
- [Index completeness does not determine editorial orientation](./index-completeness-does-not-determine-editorial-orientation.md) — extends: separates mechanically complete membership from the editorial value of grouping and context phrases
- [Soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — exemplifies: a human knowledge-organization pattern is transferred into agent context with the source-side pattern and local delta kept separate
- [tag-readme type spec](../types/tag-readme.md) — evidenced-by: the shipped `complete` and `covered_by` semantics that constitute the machine-checked contract
- [MOCs (defn)](../sources/nick-milo-mocs-definition.ingest.md) — evidenced-by: Milo defines MOCs as contextual maps and gives a grouped-link note as one form
- [Schlagwortregister](../sources/luhmann-archive-schlagwortregister.ingest.md) — evidenced-by: the Archive describes Luhmann's keyword registers as non-exhaustive lists of relevant entry points, not as MOCs
