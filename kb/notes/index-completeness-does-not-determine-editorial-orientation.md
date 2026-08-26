---
description: "Complete generated listings establish membership, but their inputs do not determine topic-specific grouping, role phrases, or reading order without editorial judgment"
type: ./types/structured-claim.md
traits: [title-as-claim]
tags: [kb-maintenance]
---

# Index completeness does not determine editorial orientation

A complete generated index answers which notes belong to a tag. Commonplace's deterministic build-time generator derives that membership and reproduces each note's title and description. Those inputs do not select topic-specific groupings, priorities, tensions, or reading paths. A person, agent, or model can propose that structure, but the proposal becomes durable orientation only through an editorial decision or a separately encoded rule that can be reviewed. Generated enumeration and curated orientation are therefore complementary layers, not a division between machine-written and human-written text.

## Evidence

**The generated-tail index design embeds this distinction architecturally.** ADR [004-replace-areas-with-tags](../reference/adr/004-replace-areas-with-tags.md) split index pages into two layers: a curated section above the `<!-- generated -->` marker and a generated section below. The curated section is selective and editorial; the generated section is exhaustive and mechanical. The generated layer can be rebuilt from tag membership, while the curated layer preserves choices that membership does not contain.

**Context phrases record topic-relative roles.** The [COLLECTION.md](./COLLECTION.md) convention requires curated entries to have context phrases — "a bare link list is an address book, not a map." A note's description states its contribution in isolation; a context phrase states its role at one destination. The same note can be foundational in one topic and a counterargument in another, so neither membership nor the note's single description determines which role a particular index should foreground.

**Stale curation is costly when it closes discovery.** [Indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md): an apparently complete curated view can make a reader stop before a more complete search. Curated sections can fall behind as new notes arrive, but generated-tail indexes mitigate this by keeping the generated section always complete. A reader who doesn't find what they need in the curated section can fall back to the generated listing. The staleness risk applies to the curated section, not the index as a whole.

**One tested auto-aggregation design lost editorial context.** The [OpenViking review](../agent-memory-systems/reviews/openviking.md) considered borrowing bottom-up summary aggregation for indexes, but noted that "our index entries carry editorial context phrases that auto-aggregation would lose." This shows that the proposed aggregation method did not preserve the editorial layer. It does not establish a capability limit for every LLM- or graph-based generator.

## Reasoning

Membership is a mechanically checkable relation between a tag and a set of notes. Orientation is a purpose-relative relation among those notes: which items to foreground, how to group them, which tensions to expose, and what sequence helps a particular reader. The same complete set admits several useful maps because different tasks make different relationships salient.

Titles, typed links, graph structure, and embeddings can constrain a candidate map, and a generator can turn those inputs into candidate groupings or role phrases. Determinism can verify that the build followed its algorithm; it cannot by itself verify that the resulting emphasis is the right editorial judgment for the index's readers. If canonical roles or reading order are encoded as authoritative input, a deterministic generator can reproduce them, but the curation has moved upstream rather than disappeared.

[Title-as-claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) is a partial counterpoint: claim titles expose more structure than topic titles even in a generated listing. Typed links can likewise make some inter-note relations explicit. These inputs reduce the editorial work, but they do not choose which valid relationships should organize a purpose-specific map.

Additional orientation has diminishing returns on small collections and increasing returns on large ones. Below roughly five notes, a reader can often scan the complete listing without needing another layer. Above that threshold, the listing becomes a wall of entries and the curated section becomes the primary navigation surface. This matches the COLLECTION.md lifecycle guidance: "Create when 5+ related notes accumulate under a tag. Curate when the generated listing alone isn't enough." The threshold concerns the value of curation, not whether membership logically entails orientation.

## Caveats

- The 5-note threshold is a rough heuristic, not a bright line. Some topics with 3 notes benefit from curation if the relationships are non-obvious; some with 10 need no curation because the titles alone are clear.
- This claim does not require a human to draft the curated layer. An LLM or graph algorithm can propose it; editorial review is what turns a proposal into accepted orientation.
- A schema can make roles, groups, or reading order mechanically reproducible. In that case the encoded fields, rather than index completeness, are the source of the orientation.
- Curation cost is non-trivial. Each curated entry requires reading the note, understanding its role in the topic, and writing a context phrase. The [maintain-curated-indexes](../instructions/maintain-curated-indexes.md) instruction exists because this is ongoing maintenance, not a one-time cost.
- This argument does not claim curation is always worth the cost. For tags with high note churn, maintenance cost may exceed orientation benefit. The generated section alone may suffice for volatile topics.

---

Relevant Notes:

- [Indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — foundation: establishes the fallback-suppression risk that curated sections must manage
- [title-as-claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — extends: claim titles add orientation even in generated listings, but curation adds relational structure that titles alone cannot carry
- [two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — foundation: the index boundary defines the regime where curated orientation becomes operationally necessary
- [004-replace-areas-with-tags](../reference/adr/004-replace-areas-with-tags.md) — evidenced-by: the generated-tail design architecturally separates the two kinds of index value this note distinguishes
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — extends: quality scores address which notes to connect, while curation addresses how to present connected notes for navigation
