---
description: "A Commonplace tag-README can inherit Milo's contextual mapping pattern while validation checks only its declared membership relations, not editorial quality."
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [kb-maintenance, document-system]
---

# An enforced tag-README combines a MOC pattern with checked membership

Within Commonplace, an **enforced tag-README** is a tag-README carrying at least
one validator-enforced membership mark. It combines two distinct layers. Its
curated orientation inherits Nick Milo's MOC pattern of contextual mapping. Its
declared `complete` or `covered_by` relation adds a separate membership contract
whose truth the validator re-derives and whose success authorizes a bounded
stopping shortcut. This is a local design synthesis and a component-level
analogy, not a genealogy, an exact equivalence between tag-READMEs and MOCs, or
a machine judgment about editorial quality.

## The inherited mapping pattern

In [Milo's account](../sources/nick-milo-mocs-definition.ingest.md), an MOC is a
cluster of information that maps things in context with other things, and a
note whose links are clustered into groups is one example. The definition
supplies the comparison criterion, and the example shows one possible
realization. Neither establishes grouping, annotation, or selectivity as a
necessary property of every MOC, nor do they characterize LYT practice as a
whole.

Under Commonplace's [tag-README contract](../types/tag-readme.md), a tag's
curated head gives a short orientation. Its groupings and topic-relative
context phrases explain why destinations matter in this map. Those choices
relate the destinations rather than merely enumerate them. A bare membership
list would not provide the same orientation, so the tag-README realizes Milo's
contextual-map pattern without being asserted to be identical to every MOC.

## The checked membership contract

Selection is the default. `complete: true` asserts that the README links every
note carrying its tag. `covered_by: [children]` asserts that every note carrying
the parent tag also carries at least one listed child tag, so the parent's
membership is contained in the union of the children's memberships. The
validator re-derives each relation, and the [local
contract](../types/tag-readme.md) permits completeness or child coverage to be
claimed only through its corresponding enforced mark. These exact assertions
are the machine-checked addition; they are not part of the inherited MOC
premise.

[Exact membership does not determine editorial
orientation](./index-completeness-does-not-determine-editorial-orientation.md).
It does not choose the groups, priorities, tensions, role phrases, or reading
order that make the page useful for a particular topic and task. Enumeration
answers which items are members; orientation answers how a reader should
approach and relate them. Validation checks the first answer and therefore does
not certify the relevance or quality of the second.

A valid `complete` mark permits a consumer to skip the by-tag membership sweep,
while a valid `covered_by` mark permits trusting the declared child routing.
Without the relevant mark, the scoped membership query remains the fallback.
The marks are therefore [non-load-bearing validated
copies](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
that authorize particular shortcuts rather than replace canonical membership.
A false trusted copy can hide missing members when it [suppresses the retrieval
that would expose
them](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md);
checking the exact relation on which stopping depends turns such drift into a
visible failure. This is a conditional control-flow mechanism, not evidence
that every agent needs these marks or that consumers always stop at an index.

## Scope

The [Luhmann
Archive](../sources/luhmann-archive-schlagwortregister.ingest.md) separately
reports that Luhmann's own keyword registers made no claim to completeness
concerning the locations of the respective terms and instead named only the
relevant entry points into the collection. This is a bounded analogue for
useful selective navigation, which Commonplace contrasts with its optional
checked completeness or coverage claims. It does not identify the registers as
MOCs, establish lineage between Luhmann and Milo, or characterize Zettelkasten
or PKM practice generally. The commissioned evidence also does not answer
whether other MOC practitioners state completeness or canonical-entry-point
policies.
