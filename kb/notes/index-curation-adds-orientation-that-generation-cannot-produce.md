---
description: "Generated indexes guarantee completeness but not orientation — curation adds editorial grouping and context phrases that turn a listing into a navigable map"
type: ./types/structured-claim.md
traits: [title-as-claim]
tags: [kb-maintenance]
status: seedling
---

# Index curation adds orientation that generation cannot produce

A generated index is complete: every note carrying a tag appears in the listing, rebuilt deterministically by `commonplace-sync-generated-index`. But completeness is not orientation. A reader scanning 30 generated entries sees an alphabetized address book — titles and descriptions in sequence, with no signal about which notes are foundational, which are in tension, or where the interesting clusters lie. The reader must open notes to discover structure.

Curation adds editorial information that generation cannot: groupings that reflect conceptual clusters, context phrases that explain *why* a note matters to a topic (not just *that* it exists), and cross-links to related indexes that reveal how topics connect. This is orientation — it tells the reader where they are in a landscape before they start walking.

## Evidence

**The generated-tail index design embeds this distinction architecturally.** ADR [004-replace-areas-with-tags](../reference/adr/004-replace-areas-with-tags.md) split index pages into two layers: a curated section above the `<!-- generated -->` marker and a generated section below. The curated section is selective and editorial; the generated section is exhaustive and mechanical. The design treats them as complementary — the same note can appear in both without redundancy, because the curated entry carries context the generated entry lacks.

**Context phrases are the atomic unit of curation value.** The [COLLECTION.md](./COLLECTION.md) convention requires curated entries to have context phrases — "a bare link list is an address book, not a map." Curation adds the *relationship between note and topic*, stated in a phrase. A generated entry can reproduce a note's description, but it cannot say "defines the concept" or "the main counterargument" or "foundational for everything below" — those are editorial judgments about role.

**Stale curation is costly, but the alternative is worse.** [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) shows that a stale index suppresses search entirely — the agent trusts the map and stops exploring. Curated sections can fall behind as new notes arrive, but generated-tail indexes mitigate this by keeping the generated section always complete. A reader who doesn't find what they need in the curated section can fall back to the generated listing. The staleness risk applies to the curated section, not the index as a whole.

**Auto-aggregation loses editorial context.** The [OpenViking review](../agent-memory-systems/reviews/openviking.md) considered borrowing bottom-up summary aggregation for indexes, but noted that "our index entries carry editorial context phrases that auto-aggregation would lose." Orientation resists automation: it requires judgment about what matters, not summarization of what exists.

## Reasoning

Orientation requires a model of *relevance structure* — which items are central, which peripheral, how they cluster, what tensions exist. A generated listing has one ordering principle (alphabetical, or by title) and one metadata dimension (the note's own description). Curation adds a second dimension: the note's role within the topic.

[Title-as-claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) is a partial counterpoint: claim titles carry more orientation than topic titles even in generated listings, because they expose what the note commits to. But even claim titles cannot express relationships *between* items. "These three notes tension against each other" or "start here, then read these" are relational judgments that only the curated section can carry.

Curation has diminishing returns on small collections and increasing returns on large ones. Below roughly five notes, a generated listing *is* the orientation — the reader can scan everything. Above that threshold, the listing becomes a wall of entries and the curated section becomes the primary navigation surface. This matches the COLLECTION.md lifecycle guidance: "Create when 5+ related notes accumulate under a tag. Curate when the generated listing alone isn't enough."

## Caveats

- The 5-note threshold is a rough heuristic, not a bright line. Some topics with 3 notes benefit from curation if the relationships are non-obvious; some with 10 need no curation because the titles alone are clear.
- Curation cost is non-trivial. Each curated entry requires reading the note, understanding its role in the topic, and writing a context phrase. The [maintain-curated-indexes](../instructions/maintain-curated-indexes.md) instruction exists because this is ongoing maintenance, not a one-time cost.
- This argument does not claim curation is always worth the cost. For tags with high note churn, maintenance cost may exceed orientation benefit. The generated section alone may suffice for volatile topics.

---

Relevant Notes:

- [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — foundation: establishes the cost of index staleness that curated sections must manage
- [title-as-claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — extends: claim titles add orientation even in generated listings, but curation adds relational structure that titles alone cannot carry
- [two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — foundation: the index boundary defines the regime where curated orientation becomes operationally necessary
- [004-replace-areas-with-tags](../reference/adr/004-replace-areas-with-tags.md) — evidence: the generated-tail design architecturally separates the two kinds of index value this note distinguishes
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — extends: quality scores address which notes to connect, while curation addresses how to present connected notes for navigation
