---
description: Tags are semantic membership predicates over KB artifacts; tag heads define those predicates and provide bounded-context routing over their members
type: kb/types/note.md
tags: [tags]
---

# Tags are semantic membership predicates with canonical routing heads

A tag represents a reusable semantic predicate over ordinary KB artifacts.

For a KB root \(K\), projection \(P\), and tag \(t\), let

\[
M_{K,P}(t)
\]

be the artifacts in the resolved projection that satisfy the predicate represented by \(t\).

Tagging an artifact with `t` asserts that the artifact belongs to this set. A tag is therefore stronger than a search keyword: it is a maintained semantic claim that this artifact is a plausible direct candidate when retrieving knowledge about the concept represented by the tag.

A useful operational test is:

> Would an agent asking a recurring question represented by this tag plausibly want this artifact among its direct retrieval candidates?

Mentioning a concept is not sufficient for membership.

## Tag names have KB-wide meaning

Within one KB root, the same tag name has one canonical meaning.

Collections may contribute different members to the tag, but they do not redefine it. Membership is therefore projection-relative while meaning is KB-wide.

This lets an installed or partial projection contain fewer members without changing what the tag means.

## Tag heads define and route the predicate

Every stable tag may have one canonical tag head. Whether a head is required from the first stable use, or only after the tag needs curated navigation, remains an open design question.

A tag head serves two related purposes:

1. **Definition** — state what membership in the tag means and distinguish it from nearby predicates.
2. **Routing** — help a bounded-context reader choose which members or narrower routes to inspect.

The tag head is metadata about the class represented by the tag. It is not itself a member of that class.

Consequently, relationships among tags should not be expressed by putting those tags in the tag head's `tags:` field. They belong in explicit routing links or tag-relation metadata.

## Tag heads have a common routing prefix

A tag head should make the following information cheap to recover:

- **Meaning** — what predicate the tag represents.
- **Use when** — the recurring retrieval question for which this tag is a useful candidate set.
- **Boundary** — important nearby concepts that do not imply membership.
- **Route** — the best first reads or narrower routes.
- **Stopping rule** — whether the head is selective, complete, or covered by narrower routes.

The remainder of the head may take whatever form best represents the area: a flat map, hierarchical router, comparative survey, or compact synthesis.

Uniform routing does not require uniform exposition.

## Completeness licenses skipping search

By default a tag head is selective. An agent requiring exhaustive membership must fall back to the shared tag-membership resolver.

`complete: true` asserts:

\[
M_{K,P}(t) \subseteq links(head(t))
\]

for the projection against which the head is being consumed.

This is an operational claim, not editorial prose: it licenses the reader to skip fallback membership search. It therefore must be mechanically checked wherever it is relied upon.

Without an enforced completeness mark, omission from a tag head does not imply non-membership.

## Coverage is a routing relation, not necessarily a taxonomy

A head may declare that its members are covered by narrower tag routes.

For tag \(t\) and routes \(C\):

\[
covered\_by(t,C)
\iff
M_{K,P}(t) \subseteq \bigcup_{c \in C} M_{K,P}(c)
\]

This licenses descent through those routes instead of enumerating the parent.

It does not by itself assert that every child is a semantic subtype of the parent. A true subtag relation additionally requires:

\[
M_{K,P}(c) \subseteq M_{K,P}(t)
\]

Tag hierarchy should therefore be introduced only when it improves a recurring routing decision, not merely because concepts can be arranged taxonomically.

Tags may overlap freely.

## Stable vocabulary is controlled but extensible

Writers should reuse an existing canonical tag when its predicate fits.

A new stable tag should have:

- a recurring retrieval question;
- a distinguishable semantic predicate;
- a name with one load-bearing sense in the KB;
- a boundary against the nearest existing alternatives.

Exploratory work may use provisional vocabulary before these conditions are met. Promotion into the participating library should resolve provisional tags into the stable vocabulary or establish them as new canonical tags.

The goal is not to minimize the number of tags. It is to avoid multiple names for the same retrieval predicate, multiple meanings for one name, and tags that do not materially improve retrieval.

## Machine consumers share the predicate

A tag may also drive deterministic machinery when the machine predicate and the navigation predicate are genuinely the same.

For example, if `trace-learning` is used both to retrieve systems that learn from traces and to populate a comparison matrix, both uses should derive from the same membership predicate.

A machine-specific classification that only partially overlaps a navigation concept should instead have its own typed field or an explicitly defined derived relation.

A tag must not silently acquire a second meaning merely because code consumes it.

## Search is the recovery layer

Curated tag navigation optimizes common retrieval paths; it does not replace search.

The shared membership resolver remains authoritative for recovering the eligible members of a tag in a projection.

Failure or staleness of a curated route should therefore cost an additional search, not make eligible knowledge unreachable.

This gives tag heads a bounded role: they are precomputed semantic routing surfaces over a recoverable underlying membership relation.
