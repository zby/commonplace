---
description: "Distinguishes the body-loading boundary from the later title-and-description index boundary, yielding three size regimes for any note set an agent reads as a unit, with consequences for areas, connect, and whole-KB work"
type: types/note.md
traits: [title-as-claim]
tags: []
---

# Two context boundaries govern operations on read-together note sets

[Areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) identifies two operations that justify areas (read-together note sets): orientation (reconstructing what is known about a topic) and comparative reading (detecting redundancy, contradiction, tension, and gaps across notes). It also observes that comparative reading usually needs more of each note than orientation does, so the two operations need different representations. This note develops that difference into its consequence for context limits. Comparative reading needs full note bodies — you can't reliably detect redundancy between two notes from their descriptions alone. Orientation can work at either resolution — full text or descriptions. This means the two operations hit different context limits, which creates distinct operational regimes.

The model applies to knowledge bases in general. Its subject is any bounded subset of a knowledge base that an agent reads as a unit: an area, a directory, a tag slice, a query result, or a whole small knowledge base. This note calls such a subset a collection, in the ordinary sense of the word. [Commonplace's collections](../reference/definitions/collection.md) are one application; the argument does not use their subtree or text-contract properties.

## The two boundaries

**The full-text boundary** is the point where all note bodies in a collection can be loaded together alongside instructions and reasoning space. Commonplace's former writing guide, `WRITING.md` (since replaced by per-collection contracts), used ~40 notes as its split heuristic, though the actual threshold depends on note length, instruction overhead, and how much reasoning space the operation needs.

**The index boundary** is the point where all titles and descriptions in a collection can be loaded together. Because a title+description pair is much smaller than a full note body, this boundary is substantially higher than the full-text boundary. How much higher depends on description length, context window size, and what else competes for the window — but the gap is structural, not marginal. A collection can be well past the full-text boundary and still have a scannable index.

As context windows grow, the index boundary moves upward. The full-text boundary may not, because [per-window degradation](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) caps how many note bodies an agent can usefully reason about at once, even when they all fit. The gap between the two boundaries may widen over time.

## Three operational regimes

The two boundaries create three regimes for any collection:

**Below the full-text boundary:** Neither operation needs partitioning. Comparative reading loads all bodies. Orientation can use either the index or full text. This is where areas are most productive. The [virtuous cycle](./areas-exist-because-useful-operations-require-reading-notes-together.md) between orientation and comparative reading runs without sub-passes: orientation focuses the next comparative pass, and that pass makes later orientation cheaper.

**Between the two boundaries:** Orientation still works — the index fits in context, and good descriptions let the agent form an overview of the collection without loading every body. Comparative reading must be partitioned into sub-passes. The agent can use the index to choose sub-passes intelligently (load notes that are likely to tension against each other), but can't do a single exhaustive comparison across the whole set. This is a degraded-but-functional regime: one operation works natively, the other requires planning.

**Above the index boundary:** Even the index stops fitting productively. Orientation requires search or hierarchical navigation through sub-indexes. The collection has exceeded the point where it functions as a coherent unit for either operation.

## Consequences

### Descriptions become load-bearing in the middle regime

Below the full-text boundary, description quality matters for retrieval but isn't critical for orientation — the agent can just read the notes. Once a collection crosses the full-text boundary, orientation, sub-pass planning, and index-scan candidate discovery must run at index resolution, so titles and descriptions become **the only content those operations see**.

This reframes the Commonplace convention, now stated in the [note type](../types/note.md), that descriptions are "retrieval filters, not summaries." In the middle regime, they also serve as the compressed representation through which the agent orients and plans, so a note with a poor description is effectively lost to operations that work at index resolution and can be reached only through body-level search.

### Parent/child area relationships are operationally distinct layers

The [areas note](./areas-exist-because-useful-operations-require-reading-notes-together.md) identifies a tension in index design: orientation benefits from synthesis and editorial structure, while comparative reading benefits from flat loadable lists. The two-boundary model separates these demands by scale rather than trying to serve both in one artifact:

- **Parent areas operate at index resolution** — orientation, routing, candidate discovery. They serve collections in the middle regime.
- **Child areas operate at full-text resolution** — comparative reading, integration. Splitting restores the ability to load all bodies together within each sub-collection.

### Library/workshop separation keeps index-scan discovery viable

In a knowledge base, the library is the curated main collection, where everything is worth connecting against. The [workshop](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) holds in-flight working material that is consumed rather than accumulated. For a system whose candidate discovery scans the whole library index, separating the two has an operational role. It keeps the library below the index boundary, where a single-pass scan works; portioned loading is the degraded fallback. Commonplace's ADR 003 is the historical case this consequence was abstracted from.

ADR 003 is the architecture decision record for the [connect skill's discovery strategy](../reference/adr/003-connect-skill-discovery-strategy.md) (dated 2026-03-05, since superseded by [ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md)). The connect skill (`/connect`) finds existing notes that a given note should link to. ADR 003 built it on the index boundary: `/connect` read the full directory index (`kb/notes/dir-index.md`) in one pass, scanning all titles and descriptions to find candidates. ADR 003 explicitly identified this as a scaling constraint — it worked only while the index was small enough to scan in one read — and proposed portioned loading as the fallback for when the index outgrew that size. ADR 025 later removed complete-index reads from the agent discovery path because that read had become the dominant per-fork cost.

The [quality scores note](./notes-need-quality-scores-to-scale-curation.md) identifies a related limit from the candidate-evaluation side: `/connect` stops scaling without filtering once its candidate list exceeds what an agent can evaluate in context. That list is keyword-search results, or a complete titles listing that stays loadable whole only while the corpus is small.

ADR 003's scaling strategy is implicitly a response to the index boundary:
- **Keep the main collection below the index boundary** by curating what goes in it (then `kb/notes/`) — workshop artifacts (in-flight working material that is consumed rather than accumulated) and machine-generated notes go elsewhere
- **Use semantic search as backup** for what the index scan can't reach (sources, which have no curated index)
- **Load the index in portions** as a degraded-but-functional fallback

The separation itself is drawn in [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md), which grounds it in value trajectory and lifecycle rather than in context limits.

## Scope

- Boundary positions are not fixed numbers. The full-text boundary shifts with note length, instruction overhead, and the reasoning space an operation needs; a note count such as the ~40-note heuristic above is a local planning figure. The index boundary shifts with description length, context window size, and what else competes for the window.
- The middle regime assumes orientation can work from titles and descriptions, which holds only as far as the descriptions are good.
- The claim that the gap between the boundaries may widen as windows grow is a prediction, not an observation. It depends on a criterion this note leaves open: the full-text boundary must be set by productive use while the index boundary tracks fit, or index scanning must degrade less than full-body comparison. If both boundaries measure fit, or both measure productive use, the prediction needs separate support.

## Open questions

- Should a knowledge base structure for the index boundary early (hierarchical indexes before they are needed), or keep a flat index until index-resolution operations degrade?
- Does this model predict that very large KBs need three levels (namespace > area > sub-area) rather than two?
- Can whole-collection candidate discovery work above the index boundary without losing cross-domain discovery? Filtering before scanning (the quality-scores approach) is one path; hierarchical indexes are another. Commonplace's `/connect` under ADR 003 was one instance of this operation.
- Which criterion sets each boundary: raw fit in the window, or productive use? If the index boundary tracks window size while the full-text boundary does not, what makes index scanning degrade less than full-body comparison as the window fills?

---

Relevant Notes:

- [areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — extends: develops the areas note's resolution difference between orientation and comparative reading into the two-boundary model; separates the orientation/comparative-reading tension by scale
- [003-connect-skill-discovery-strategy](../reference/adr/003-connect-skill-discovery-strategy.md) — abstracted-from: the historical connect design (superseded by ADR 025) whose index-first discovery and scaling concerns this note's index-boundary consequence was built from
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — extends: quality scores address a related limit — ranking candidates when keyword results or the complete titles listing exceed what an agent can evaluate in context
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: context scarcity is why the boundaries exist; its feasibility face — soft degradation as the window fills, before the hard cap — explains why the full-text boundary may not move with growing windows
- [a knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — extends: the two boundaries define two resolution levels (index and full-text) between which the KB must support fluid switching
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — enables: library/workshop separation keeps the main collection below the index boundary where index-scan discovery works
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — contrasts: its loading hierarchy (always-loaded router → on-demand skill bodies → task docs read when needed) orders instructions by loading frequency, a neighbouring shape to the index/full-text resolution gradient described here
