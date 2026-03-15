---
description: Existing links already encode dependency information; comparing note and target timestamps flags notes that may be stale without any new annotation, analogous to make's file-based rebuild logic.
type: note
traits: []
tags: [kb-maintenance]
status: seedling
---

# Link graph plus timestamps enables make-like staleness detection

Notes that reference current design state go stale when that state changes. A note proposing changes to WRITING.md becomes misleading once WRITING.md adopts those changes. Currently there is no mechanism to detect this — staleness is discovered only when someone happens to re-read the note.

## The make analogy

`make` solves a structurally similar problem: source files change, and downstream targets need rebuilding. It tracks dependencies between files and compares timestamps. If a source is newer than its target, the target is rebuilt.

A KB note that links to another file is making a claim about that file's state. If the target changes, the claim may be stale. The link graph already encodes the dependency; git provides the timestamps. No new annotation is needed.

## Mechanism

1. Walk the link graph to extract each note's outbound links.
2. For each link target, compare the note's last-modified time (git log) against the target's last-modified time.
3. If any target is newer than the note, flag the note for review.

The "rebuild" is not automatic rewriting — it's a review prompt. A human or agent checks whether the change to the target invalidates what the note says about it. This is analogous to `make` invoking a recipe, except the recipe is "re-read and decide."

## False positives and filtering

Not every change to a target invalidates the linking note. WRITING.md might get a typo fix that doesn't affect any note referencing it. This is the same tradeoff `make` accepts — it rebuilds targets that may not need rebuilding because the cost of a redundant rebuild is lower than the cost of a missed one.

For a KB, the cost of a false positive is "agent re-reads a note unnecessarily." That's cheap. The cost of a false negative is a stale note misleading future traversal — which is the core problem [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) identifies.

Possible filters to reduce noise:
- Only flag notes whose targets changed substantively (exclude commits that only touch whitespace or frontmatter).
- Only flag notes that link to targets with specific relationship types (e.g. "proposes changes to" is high-risk for staleness; "foundation" is low-risk).
- Weight by note centrality — high-centrality stale notes are higher priority.

## Scope

This works for intra-KB links where both files are in git. It does not cover external references (URLs, API docs) — those need a different mechanism (periodic link checking, `last-checked` fields as [related-systems reviews](./related-systems/README.md) already use).

## Relationship to existing staleness work

The KB already has staleness concepts:
- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) identifies the high cost of stale navigation.
- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) proposes note-age-vs-connection-count as a staleness proxy.
- Related-system reviews use `last-checked` for external sources.

This note adds a dependency-aware mechanism that is more precise than age-based heuristics: a note modified yesterday can be stale if its target was modified today.

## What would defeat this claim?

If most staleness comes from notes whose claims drift due to accumulated context changes across many files (rather than specific target changes), then pairwise timestamp comparison would miss the important cases. The mechanism assumes staleness is traceable to specific linked targets. [High-reach revisions](./brainstorming-how-reach-informs-kb-design.md) are the specific mechanism that produces this failure mode — revising a foundational principle may touch few files directly while silently invalidating downstream reasoning across many notes.

---

Relevant Notes:

- [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — foundation: the high cost of stale navigation that motivates detection
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — extends: adds dependency-aware detection alongside age-based heuristics
- [mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — motivates: its proposal-pruning pattern is a concrete use case for this detection
- [traversal improves the graph](./traversal-improves-the-graph.md) — mechanism: traversal is when staleness gets noticed today; this note proposes detecting it before traversal
- [links](./links-index.md) — foundation: the link graph that provides the dependency structure
