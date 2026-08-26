---
description: "Proposal: define tags as KB-wide semantic membership predicates and tag heads as canonical definition and bounded-context routing surfaces"
type: kb/reference/types/design-proposal.md
tags: [tags]
traits: [has-external-sources]
---

# Semantic contract for tags and tag heads

Commonplace has machinery for tag membership and routing, but no single
semantic contract that tells writers what assigning a tag asserts, how a tag
keeps its meaning across projections, or when deterministic consumers may use
the same classification. This proposal isolates that contract from the wider
tag-scope and migration design. It leaves the remaining policy choices explicit
rather than presenting the contract as shipped behavior.

## Current state (as of 2026-08-27)

The shared `tags` field accepts free-form strings. [ADR 026](../adr/026-tag-readme-type-with-completeness-and-coverage-marks.md)
defines curated tag heads and the `complete` and `covered_by` marks, but it
deliberately leaves tag selection out of the write path. Membership checks are
collection-scoped, and no binding surface defines tag membership as a semantic
predicate or prevents one string from acquiring several senses.

The sibling [tag-scope proposal](./tag-scope-is-declared-where-membership-claims-are-made.md)
would add KB-root ownership, projection-relative membership, canonical head
paths, and a shared resolver. This proposal states the semantic contract that
those mechanisms would implement. Neither proposal describes the current
system.

Recent grounded navigation work now supplies a bounded evidence boundary for
the routing half of the design. [Pirolli's information-foraging
account](../../sources/pirolli-proximal-information-scent-distal-content.ingest.md)
models selection of unseen content from proximal cues; [Teevan and
colleagues](../../sources/teevan-perfect-search-engine-orienteering.ingest.md)
observed human searchers combining contextual local steps with direct jumps;
and [Tombros and
Sanderson](../../sources/tombros-sanderson-query-biased-summaries.ingest.md)
found better human relevance judgments from query-biased summaries than from a
static surrogate. These sources distinguish navigation problems and motivate
agent-side tests. They do not establish LLM-agent behavior or choose a tag
interface.

## Forces

- A tag must be precise enough that writers, readers, and deterministic
  consumers classify the same artifacts alike.
- The same KB can appear through several projections, so membership can vary
  without letting a tag's meaning vary.
- Curated routing must save bounded-context work without becoming the only way
  to recover membership.
- Exact tag membership, contextual head traversal, and task-level search answer
  different questions; a guarantee about one must not silently authorize
  stopping another.
- A retained head supplies stable and authored cues, while a query-time result
  can condition its cue on the current task. The design must preserve both
  options without making an untested agent-performance claim.
- Stable vocabulary needs a discoverable boundary and reuse rule, but
  exploratory work must be able to try provisional classifications cheaply.
- Tag relationships may improve routing without constituting a taxonomy.

## Proposed semantic contract

Under this candidate contract, a tag represents a reusable semantic predicate
over ordinary KB artifacts.

For a KB root \(K\), projection \(P\), and tag \(t\), let

\[
M_{K,P}(t)
\]

be the artifacts in the resolved projection that satisfy the predicate represented by \(t\).

Tagging an artifact with `t` asserts that the artifact belongs to this set. A
tag is therefore stronger than a search keyword: it is a maintained semantic
claim that the artifact is a plausible candidate for at least one recurring
information need represented by the tag. Membership does not assert that every
query about the tag should load every member.

A useful operational test is:

> Would an agent pursuing at least one recurring information need named by this
> tag plausibly need this artifact considered before route- or query-specific
> selection?

Mentioning a concept is not sufficient for membership.

### Tag names have KB-wide meaning

Within one KB root, the same tag name has one canonical meaning.

Collections may contribute different members to the tag, but they do not redefine it. Membership is therefore projection-relative while meaning is KB-wide.

This lets an installed or partial projection contain fewer members without changing what the tag means.

### Tag heads define and route the predicate

Every stable tag may have one canonical tag head. Whether a head is required from the first stable use, or only after the tag needs curated navigation, remains an open design question.

A tag head serves two related purposes:

1. **Definition** — state what membership in the tag means and distinguish it from nearby predicates.
2. **Routing** — help a bounded-context reader choose which members or narrower routes to inspect.

The tag head is metadata about the class represented by the tag. It is not itself a member of that class.

Consequently, relationships among tags should not be expressed by putting those tags in the tag head's `tags:` field. They belong in explicit routing links or tag-relation metadata.

### Tag heads have a common routing prefix

A tag head should make the following information cheap to recover:

- **Meaning** — what predicate the tag represents.
- **Use when** — the recurring retrieval question for which this tag is a useful candidate set.
- **Boundary** — important nearby concepts that do not imply membership.
- **Route** — the best first reads or narrower routes.
- **Stopping rule** — whether the head is selective, complete, or covered by narrower routes.

The remainder of the head may take whatever form best represents the area: a flat map, hierarchical router, comparative survey, or compact synthesis.

Uniform routing does not require uniform exposition.

The prefix is a stable pointer, not a relevance oracle. The [proximal-cue
account](../../notes/agents-navigate-by-deciding-what-to-read-next.md) explains
why meaning, use conditions, boundaries, and context phrases can help a reader
judge unseen destinations. Their usefulness remains relative to a task and
consumer, and structural validation cannot establish their editorial quality.

### Completeness licenses skipping membership resolution

By default a tag head is selective. An agent requiring exhaustive membership must fall back to the shared tag-membership resolver.

`complete: true` asserts:

\[
M_{K,P}(t) \subseteq links(head(t))
\]

for the projection against which the head is being consumed.

This is an operational claim, not editorial prose: it licenses the reader to
skip fallback resolution of `M_{K,P}(t)`. It therefore must be mechanically
checked wherever it is relied upon.

Without an enforced completeness mark, omission from a tag head does not imply non-membership.

Even a valid mark says nothing about artifacts outside the tag that may matter
to the current task. It cannot license stopping task-level search or establish
that the tag's predicate captures the whole information need.

### Coverage is a routing relation, not necessarily a taxonomy

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

### Stable vocabulary is controlled but extensible

Writers should reuse an existing canonical tag when its predicate fits.

A new stable tag should have:

- a recurring retrieval question;
- a distinguishable semantic predicate;
- a name with one load-bearing sense in the KB;
- a boundary against the nearest existing alternatives.

Exploratory work may use provisional vocabulary before these conditions are met. Promotion into the participating library should resolve provisional tags into the stable vocabulary or establish them as new canonical tags.

The goal is not to minimize the number of tags. It is to avoid multiple names for the same retrieval predicate, multiple meanings for one name, and tags that do not materially improve retrieval.

### Machine consumers share the predicate

A tag may also drive deterministic machinery when the machine predicate and the navigation predicate are genuinely the same.

For example, if `trace-learning` is used both to retrieve systems that learn from traces and to populate a comparison matrix, both uses should derive from the same membership predicate.

A machine-specific classification that only partially overlaps a navigation concept should instead have its own typed field or an explicitly defined derived relation.

A tag must not silently acquire a second meaning merely because code consumes it.

### Membership recovery, head traversal, and search remain distinct

The shared membership resolver is authoritative for recovering the eligible
members of a tag in a projection. It answers an exact classification question,
not which artifacts best answer the current task.

A tag head is a contextual local-navigation surface over that recoverable set.
Its groupings and context phrases can support a sequence of informed next-read
decisions. [Teevan and colleagues' human study](../../sources/teevan-perfect-search-engine-orienteering.ingest.md)
shows that contextual local steps and direct jumps can serve different
information-seeking paths, while withholding any claim that LLM agents prefer
the same strategy.

Task-level search is the complementary long-range route. It may recover
relevant artifacts outside one tag or rank members for a narrower query.
[Tombros and Sanderson's human experiment](../../sources/tombros-sanderson-query-biased-summaries.ingest.md)
supports testing query-conditioned result pointers rather than assuming that a
fixed head or description is sufficient. It does not warrant a required
agent-facing summarizer.

Failure or staleness of a curated head must therefore leave exact membership
recoverable through the resolver. Task discovery may still require search even
when the head is complete. The [end-to-end access
account](../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md)
also prevents successful membership recovery from standing in for useful
selection, loading, uptake, or task success.

## Free choices

- **When a head becomes mandatory.** A stable tag could require a canonical
  head from its first participating-library use, making heads the registry, or
  remain headless until curated navigation repays the extra artifact. The
  contract must choose one rule; the current 5+ member convention and a
  first-use requirement are different designs.
- **Where provisional vocabulary is allowed.** Provisional tags could be
  limited to non-participating workshop and capture surfaces, or admitted into
  participating collections with an explicit provisional marker and promotion
  path. Silent headless vocabulary in a supposedly stable namespace is not a
  third option.
- **How semantic reuse is checked.** Writer discipline, a write-path lookup,
  semantic review, and a validator-backed registry impose different costs and
  guarantees. Structural validation can check identity and existence; it
  cannot decide unaided whether two natural-language predicates mean the same
  thing.
- **How tag relations are represented.** `covered_by` supplies one routing
  relation. Additional subtype or overlap metadata should be introduced only
  if a recurring consumer needs it.
- **How resolver results are presented.** Exact membership is fixed by the
  resolver, but its agent-facing view may expose path/title/description records
  or add query-conditioned ranking and summaries. The human evidence motivates
  preserving this comparison; an agent trial, not the source analogy, must
  choose between presentations.

## Operativity

- Root authoring instructions and the shared `tags` schema guidance would tell
  writers that assignment asserts semantic membership, that mention is
  insufficient, and that one string has one sense within a KB root.
- The tag-head collection contract and `tag-readme` type would own the common
  routing prefix and the meanings of `complete` and `covered_by`.
- The shared resolver, validator, and documentation build would compute one
  projection-relative membership relation and enforce every claim that licenses
  skipping membership resolution.
- The write path would consult the stable vocabulary when assigning tags and
  route new stable predicates through the chosen head or registry policy.
- Type-local validators and deterministic consumers would enforce parity when
  a tag also drives a machine classification.

No single consumer implements this contract today. Adoption must change these
surfaces together or clearly stage them without letting proposed semantics read
as current guarantees.

## Adoption criteria

- Every binding surface gives `tags` the same KB-wide predicate meaning and
  names the projection boundary of membership claims.
- All membership enumeration, mark validation, published augmentation, and
  skip rules consume the same resolver.
- The mandatory-head choice, provisional-vocabulary boundary, and semantic
  reuse check are decided and enforced consistently.
- Tag heads expose meaning, use condition, boundary, route, and stopping rule
  cheaply enough for the write and read paths to use them.
- Every stopping shortcut is limited to exact tag-membership recovery; no mark
  is presented as evidence that task-level discovery is complete.
- Resolver output keeps exact membership separate from any fixed or
  query-conditioned presentation so those pointer strategies can be evaluated
  without changing tag semantics.
- Every deterministic consumer either uses exactly the navigation predicate or
  moves its classification to a typed field or explicit derived relation.
- Existing tag uses are audited against the adopted predicates, including
  headless and machine-consumed tags.
- The adopted design is reconciled with the tag-scope proposal so the two
  artifacts do not define competing membership or head contracts.

## Alternatives considered

1. **Treat tags as search keywords.** Rejected as the stable contract because
   occurrence and relevance are different predicates; mentioning a concept
   does not make an artifact a useful direct retrieval candidate.
2. **Give a tag collection-local meaning.** Rejected because moving or
   projecting an artifact would change the interpretation of the same
   frontmatter value, and cross-collection routing could not rely on it.
3. **Reserve tags for navigation and always duplicate machine
   classifications.** Rejected when both consumers genuinely use the same
   predicate; duplicate authored state can drift. A typed field remains the
   alternative when the predicates differ.
4. **Treat `covered_by` as a subtype declaration.** Rejected because coverage
   licenses a routing descent without proving that each child predicate is a
   semantic subset of the parent.

## Related design work

- [Tag scope is declared where membership claims are made](./tag-scope-is-declared-where-membership-claims-are-made.md) — part-of: owns the KB-root, projection, resolver, canonical-path, and migration machinery this semantic contract assumes
- [Write-time vocabulary collision controls](./write-time-vocabulary-collision-controls.md) — see-also: supplies candidate registry and write-time mechanisms for enforcing one-string-one-sense
- [Link-following and search impose different metadata requirements](../../notes/link-following-and-search-impose-different-metadata-requirements.md) — rests-on: distinguishes contextual local navigation from long-range selection without treating the tool invoked as the strategy
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — rests-on: separates fixed, query-time, and authored pointers by specificity, cost, availability, and accuracy
- [An enforced tag-README combines a MOC pattern with checked membership](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) — rests-on: separates editorial mapping from the exact checked relation that authorizes a membership shortcut
