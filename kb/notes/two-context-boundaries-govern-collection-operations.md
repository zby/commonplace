---
description: Any note collection faces two context boundaries — a full-text boundary where all bodies can be loaded together, and an index boundary where all titles+descriptions fit — creating three operational regimes that govern areas, /connect, and whole-KB operations differently
type: note
areas: [kb-design]
status: seedling
---

# Two context boundaries govern collection operations

[Areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) identifies two operations that justify areas — orientation (reconstructing what is known about a topic) and comparative reading (detecting redundancy, contradiction, tension, and gaps across notes). It treats both as sharing one constraint: context is finite. But the two operations have different minimum resolution requirements. Comparative reading needs full note bodies — you can't detect redundancy between two notes from their descriptions alone. Orientation can work at either resolution — full text or descriptions. This means the two operations hit different context limits, which creates distinct operational regimes.

## The two boundaries

**The full-text boundary** is the point where all note bodies in a collection can be loaded together alongside instructions and reasoning space. WRITING.md sets this at ~40 notes, though the actual threshold depends on note length, instruction overhead, and how much reasoning space the operation needs.

**The index boundary** is the point where all titles and descriptions in a collection can be loaded together. Because a title+description pair is much smaller than a full note body, this boundary is substantially higher than the full-text boundary. How much higher depends on description length, context window size, and what else competes for the window — but the gap is structural, not marginal. A collection can be well past the full-text boundary and still have a scannable index.

As context windows grow, the index boundary moves upward — but the full-text boundary may not, because [complexity costs](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) limit how many note bodies an agent can usefully reason about simultaneously, regardless of whether they fit. The gap between the two boundaries may widen over time.

## Three operational regimes

The two boundaries create three regimes for any collection:

**Below the full-text boundary:** Both operations work at full power. Comparative reading loads all bodies. Orientation can use either the index or full text. This is where areas are most productive — the [virtuous cycle](./areas-exist-because-useful-operations-require-reading-notes-together.md) between orientation and comparative reading runs without friction.

**Between the two boundaries:** Orientation still works — the index fits in context, and good descriptions let the agent build a mental model without loading every body. Comparative reading must be partitioned into sub-passes. The agent can use the index to choose sub-passes intelligently (load notes that are likely to tension against each other), but can't do a single exhaustive comparison across the whole set. This is a degraded-but-functional regime: one operation works natively, the other requires planning.

**Above the index boundary:** Even the index stops fitting productively. Orientation requires search or hierarchical navigation through sub-indexes. The collection has exceeded the point where it functions as a coherent unit for either operation.

## Consequences

### Descriptions become load-bearing in the middle regime

Below the full-text boundary, description quality matters for retrieval but isn't critical for orientation — the agent can just read the notes. Once a collection crosses the full-text boundary, descriptions become **the only content that participates in index-level operations** — orientation, candidate discovery, sub-pass planning.

This reframes the WRITING.md guidance that descriptions are "retrieval filters, not summaries." In the middle regime, they also serve as the compressed representation through which the agent orients and plans. A note with a bad description isn't just hard to find — it's invisible to every operation that works at index resolution.

### Parent/child area relationships are operationally distinct layers

The [areas note](./areas-exist-because-useful-operations-require-reading-notes-together.md) identifies a tension in index design: orientation benefits from synthesis and editorial structure, while comparative reading benefits from flat loadable lists. The two-boundary model separates these demands by scale rather than trying to serve both in one artifact:

- **Parent areas operate at index resolution** — orientation, routing, candidate discovery. They serve collections in the middle regime.
- **Child areas operate at full-text resolution** — comparative reading, integration. Splitting restores the ability to load all bodies together within each sub-collection.

The parent index is not a taxonomic convenience — it's a distinct operational layer serving a different resolution.

### Library/workshop separation is an operational necessity

The [connect skill's discovery strategy](./adr/003-connect-skill-discovery-strategy.md) is built on the index boundary: `/connect` works by reading the full `index.md` in one pass, scanning all titles and descriptions to find candidates. ADR 003 explicitly identifies this as a scaling constraint — it works while `index.md` is small enough to scan in one read, and proposes portioned loading when it isn't.

The [quality scores note](./notes-need-quality-scores-to-scale-curation.md) identifies the same threshold from the other direction: `/connect` stops scaling without filtering once the candidate list exceeds what an agent can evaluate in context.

ADR 003's scaling strategy is implicitly a response to the index boundary:
- **Keep the main collection below the index boundary** by curating what goes in `kb/notes/` — workshop artifacts and machine-generated notes go elsewhere
- **Use semantic search as backup** for what the index scan can't reach (sources, which have no curated index)
- **Load the index in portions** as a degraded-but-functional fallback

This means the library/workshop separation from [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) isn't just about curation quality — it's an operational necessity to keep the main collection below the index boundary where `/connect`'s full-scan approach works.

## Open questions

- Should the KB proactively structure for the index boundary (hierarchical indexes now), or treat it as a future problem and keep the current flat index until it breaks?
- Does this model predict that very large KBs need three levels (namespace > area > sub-area) rather than two?
- Can `/connect` be redesigned to work above the index boundary without losing cross-domain discovery? The quality-scores approach (filter before scanning) is one path; hierarchical indexes are another.

---

Relevant Notes:

- [areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — extends: adds the two-boundary model to the single-constraint analysis; separates the orientation/comparative-reading tension by scale
- [003-connect-skill-discovery-strategy](./adr/003-connect-skill-discovery-strategy.md) — grounds: the connect skill's index-first approach is built on the index boundary; its scaling concerns are exactly what happens when a collection crosses that boundary
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — extends: quality scores are a response to the index boundary — filtering candidates when the full index exceeds productive scanning
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: context scarcity is why the boundaries exist; the volume/complexity distinction explains why the full-text boundary may not move with growing windows
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: the two boundaries define two resolution levels (index and full-text) between which the KB must support fluid switching
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — enables: library/workshop separation keeps the main collection below the index boundary where /connect works
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — parallel: the loading hierarchy (always-loaded > on-demand > full-text) mirrors the resolution gradient described here

Topics:

- [kb-design](./kb-design.md)
