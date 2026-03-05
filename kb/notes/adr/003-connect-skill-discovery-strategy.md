---
description: Design options and scaling strategy for how the connect skill discovers candidate connections — index-first with semantic search backup, and what changes when the KB grows
type: adr
areas: [claw-design]
status: accepted
---

# 003-connect-skill-discovery-strategy

**Status:** accepted
**Date:** 2026-03-05

## Context

The connect skill finds connections between a note and the rest of the KB. The original design used dual discovery in parallel: topic index exploration and semantic search (qmd). This missed cross-domain connections because semantic search is biased toward the source document's vocabulary — a paper about "behavioral contracts" didn't find a note about "legal drafting" despite both addressing specification and enforcement.

The root cause: semantic search queries stay within the source's vocabulary. A note using programming terms won't match notes using legal terms, even when the underlying concepts are identical.

## Decision

**Primary discovery: read `kb/notes/index.md` first.** The directory index lists every note with its description. Scanning the full list catches cross-domain connections that vocabulary-biased search misses. This works because:

- Descriptions are written as retrieval filters (KB convention)
- The agent evaluates conceptual overlap, not keyword overlap
- One file read gives complete coverage of the main collection

**Semantic search (qmd) as secondary.** Still run on both notes and sources. The index scan sees descriptions only; semantic search reaches inside note bodies — finding connections in sections, examples, or open questions that descriptions don't capture.

**Topic indexes as optional enrichment.** When the index scan identifies relevant areas, read the topic index for curated structure (groupings, tensions, gaps) that the flat listing lacks.

## Scaling strategy

The index-first approach works while index.md is small enough to scan in one read. Current size: ~120 lines. This scales to several hundred notes without issue.

**When the main collection grows too large:**

- Load index.md in portions rather than switching away from index-first discovery
- The main collection should stay curated — keep it feasible to connect against the whole index
- If we add automated/generated notes, they should NOT go in the main index. Options:
  - Workshop artifacts stay in `kb/work/` (already the case)
  - Machine-generated notes could live in a separate collection with its own index
  - The main `kb/notes/` collection remains human-curated and connectable in full

**The principle:** the main collection is the "library" — everything in it is worth connecting against. If something doesn't meet that bar, it belongs in workshops or a separate collection. This keeps index-first discovery viable indefinitely.

**Semantic search remains necessary for sources.** Sources don't have a curated index with descriptions. They also accumulate faster than notes and are less curated. qmd is the right tool here.

## Consequences

**Easier:**
- Cross-domain connections are found reliably (index scan doesn't have vocabulary bias)
- Discovery is debuggable (the trace shows what the agent saw in the index)
- No dependency on qmd availability for the primary discovery path

**Harder:**
- Requires index.md to be kept up to date (agents must add entries when creating notes; `scripts/generate_notes_index.py` as fallback)
- Description quality becomes load-bearing — a bad description hides a note from the primary discovery mechanism
- Main collection size becomes a design constraint — can't just dump everything in `kb/notes/`

---

Relevant Notes:
- [context efficiency is the central design concern in agent systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: reading one index file vs multiple search queries is a context efficiency win
- [notes need quality scores to scale curation](../notes-need-quality-scores-to-scale-curation.md) — extends: description quality is now load-bearing for discovery, not just nice-to-have
- [a functioning KB needs a workshop layer not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — supports: the library/workshop separation is what keeps the main index scannable

Topics:
- [kb-design](../kb-design.md)
