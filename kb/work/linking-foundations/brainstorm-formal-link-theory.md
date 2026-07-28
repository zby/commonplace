---
description: "Use when brainstorming what formal links do and how collection-shaped link vocabularies should emerge from observed linking practice"
type: kb/types/instruction.md
---

# Brainstorm formal-link theory from observed practice

Develop candidate explanations for how formal links work in Commonplace and how their vocabularies should arise. Keep established observations separate from conclusions generated during the brainstorm. The purpose is to open the design space without adopting a model, vocabulary, migration, or implementation.

## Grounding

- Commonplace currently has two authored link surfaces. Inline links receive their meaning from surrounding prose. Footer links use a collection-authorized identifier plus a context phrase in a stable form that can also be found mechanically, including with `rg`.
- The same relationship may matter to prose readers and to consumers of the normalized footer surface. Whether this warrants deliberate inline/footer duplication remains unresolved; no rule for or against duplication has been established.
- The source collection governs outbound destinations and authorized labels. Every directional identifier must complete `source <label> target`.
- [ADR 009](../../reference/adr/009-link-relationship-semantics.md) borrowed Ars Contexta's propositional-link vocabulary for Commonplace's theory notes. Ars Contexta argues that articulated inline links retain more relationship detail than untyped metadata, while a constrained relation vocabulary makes recurring distinctions queryable and forces the author to say more than “related.” It also recognizes that prose can express relationships a small vocabulary cannot.
- Ars Contexta supplies reasons to formalize recurring relations, but not a generative process for deriving a suitable vocabulary for a new collection.
- The borrowed vocabulary worked substantially better for claim-titled theory notes than for the reference collection. Reference artifacts needed structural, implementation, versioning, and theory-dependence relations that the theory-note vocabulary did not express well. Commonplace consequently moved authorization into collection contracts and accumulated additional relation families.
- The evidence, rationale, and grounds reviews found that one inherited label often covered several source-to-target assertions. Corpus classification had to precede renaming; grammatical direction alone did not settle semantics.
- The unresolved mechanism cases show another observed limit: artifact endpoints can stand for documents, expressed claims, or described systems and processes. A plausible label can remain ambiguous about which of those the relation connects.
- Formalization may affect note writing as well as retrieval: selecting a specific relation requires an author to articulate how a note fits existing knowledge. Whether that pressure improves note boundaries, reduces unnecessary notes, increases fragmentation, or merely produces ritual classification has not been established.

## Brainstorming task

Explore explanations that account for all of the grounding above. In particular, consider what value is unique to the normalized footer surface, how it relates to richer inline assertions, and how repeated useful relationships can inform a collection's formal vocabulary without assuming that one vocabulary fits every collection.

Use concrete Commonplace cases, especially the contrast between theory and reference links and the current mechanism ambiguity. Distinguish throughout between:

- what current files and completed migrations demonstrate;
- what Ars Contexta actually argues;
- candidate explanations inferred from those observations;
- proposals that would still require testing.

Do not treat an attractive decomposition, schema, ontology, promotion procedure, or duplication policy as an established result. Do not change collection contracts or migrate live labels as part of this brainstorm.

## Useful output

Return a small number of competing high-level models, the observations each explains, the important cases each fails or leaves open, and the next evidence that would discriminate among them. Preserve unresolved tensions rather than filling them with invented detail.
