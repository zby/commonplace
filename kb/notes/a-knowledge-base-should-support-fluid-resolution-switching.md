---
description: Good thinking requires moving between abstraction levels — broad for context, narrow for mechanism, back out for pattern. A KB's quality should be measured by how fluidly it supports this resolution-switching, not just retrieval accuracy.
type: note
traits: [has-external-sources]
areas: [claw-design]
status: seedling
---

# A knowledge base should support fluid resolution-switching

Good thinking is not staying at one level of abstraction — it is constantly moving between levels. Start broad to see the landscape, narrow in when something is interesting, zoom back out to check bearings, dive deep into the load-bearing detail, then abstract up to see the pattern. A knowledge base that supports good thinking must support this motion fluidly.

The commonplace KB already has several mechanisms that serve resolution-switching, but they aren't usually described under that framing:

**Titles vs bodies are a resolution pair.** Claim titles give the zoomed-out view — the principle, the assertion. The note body gives the zoomed-in view — the mechanism, the evidence, the specifics. Scanning a list of titles is surveying the landscape; opening a note is examining the territory. Since [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md), following links between claim titles reads as a chain of reasoning at the abstract level — without requiring the reader to descend into any specific note.

**Indexes and notes operate at different resolutions.** An area index like `claw-design.md` is the broad view — it shows what topics exist and how they relate. Following a link from the index zooms in. Returning to the index zooms out to check bearings. This is the [two kinds of navigation](./two-kinds-of-navigation.md) distinction: local link-following is narrow and contextual; search and index browsing are broad and orienting.

**Link semantics encode zoom direction.** "Since [X]" zooms into a foundation — following it takes you deeper, toward the grounds of the current argument. "This extends [Y]" zooms out toward a generalization. "Contradicts [Z]" shifts laterally to a competing view at the same level. The relationship words in [link strength](./link-strength-is-encoded-in-position-and-prose.md) aren't just categorization — they tell the reader which direction in abstraction space they're moving.

**Progressive disclosure is a resolution gradient.** The [context loading strategy](./context-loading-strategy.md) layers information from always-loaded (CLAUDE.md — broadest, least specific) through on-demand descriptions (medium) to full note bodies (narrowest, most specific). An agent traversing this hierarchy is adjusting resolution.

## The evaluative criterion

This framing suggests a quality criterion for knowledge bases that complements retrieval accuracy: **resolution-switching fluidity**. A good KB lets you move between abstraction levels with low friction. A bad one traps you — either stuck in abstractions (indexes that link to indexes, never reaching specifics) or stuck in details (dense notes with no outward links to broader context).

Concrete symptoms of poor resolution-switching:
- Notes with no outbound links — you can zoom in but can't zoom back out
- Indexes with bare links (no context phrases) — the broad view has no resolution; everything looks the same
- Topic-titled notes — titles don't carry the abstract-level argument, so you must open every note to learn anything
- Missing relationship articulation — links exist but don't tell you which direction you're moving

## Connection to discovery

The [discovery note](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) describes three depths of abstraction in connection: shared feature, shared structure, and shared generative model. Resolution-switching is the navigation skill that makes discovery possible — you can only see the particular as an instance of the general if you can move between the two levels. A KB that traps you at one level suppresses discovery.

## Open questions

- Can resolution-switching fluidity be measured? Candidate signal: for a random note, how many clicks to reach an index (zoom out) and how many from an index to reach a specific mechanism (zoom in)?
- Does the KB have resolution dead-ends — areas where you can zoom in but not out, or vice versa?
- Is there a sweet spot for note granularity that maximises resolution-switching? Too fine-grained and zooming out requires too many hops; too coarse and zooming in means reading irrelevant material.

---

Relevant Notes:
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — enables: claim titles are the zoomed-out resolution layer; they carry the argument without requiring descent into the note body
- [two kinds of navigation](./two-kinds-of-navigation.md) — grounds: local link-following (narrow) vs search/index browsing (broad) are the two primary resolution-switching modes
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — operationalises: every read/skip decision is a resolution-switching decision — follow to zoom in, skip to stay broad
- [context loading strategy](./context-loading-strategy.md) — exemplifies: the loading hierarchy is a resolution gradient from always-loaded broad context to on-demand narrow detail
- [link strength is encoded in position and prose](./link-strength-is-encoded-in-position-and-prose.md) — extends: link semantics encode zoom direction — "since" zooms into foundations, "extends" zooms out to generalizations
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — grounds: resolution-switching is the navigation skill that makes discovery possible; three abstraction depths define how deep the zoom goes

Source:
- Adapted from a social media post on "The Art of Good Thinking: Moving Between Levels" — the core insight about resolution-switching applied to KB design

Topics:
- [claw-design](./claw-design.md)
