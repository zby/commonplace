---
description: An agent trusts an index as exhaustive — a missing entry doesn't trigger search, it makes the note invisible
type: note
traits: []
areas: [links]
status: current
---

# Stale indexes are worse than no indexes

When an agent has no index for a topic, she falls back to search — and search accesses current content. She might find what she needs. But when an index exists and is incomplete, the agent reads it, feels oriented, and stops looking. The index *satisfies* the navigation need. Notes missing from the index become invisible not because they're hard to find, but because nobody looks for them.

This is the core asymmetry: **absence of an index degrades to search; presence of a stale index suppresses search entirely.**

## The critical moment is note creation

The most common staleness is a new note that doesn't get added to a relevant index. This happens when the agent creating the note doesn't know which indexes exist, or misjudges which ones apply.

The `areas:` frontmatter field is the first defense — it declares index membership at creation time. But `areas:` requires the agent to know what indexes are available. Without that knowledge, the field stays empty or incomplete, and everything downstream (Topics footer, index listing) inherits the gap.

## Defenses

**At creation time:** The agent needs to see the list of available indexes. `docs/indexes.md` serves this purpose — a single file listing all indexes with descriptions. The agent reads it and asks "does this note belong in any of these?"

**At connection time:** The /connect skill's Phase 5 reads `docs/indexes.md` and checks each index against the note. This is a second pass that catches what creation missed.

**Deterministic check:** For every note with `areas: [X]`, verify it appears in the X index. This catches the case where `areas:` is correct but the index wasn't updated. This check is automatable.

**What remains unjudgeable:** Whether a note *should* belong to an index it doesn't claim membership in. This is semantic judgment that only the agent reading both the note and the index description can make. The index-of-indexes approach keeps this judgment feasible by presenting the full list.

## Sourcing

This observation draws on arscontexta methodology research ("stale navigation actively misleads because agents trust curated maps completely"), adapted to our specific system where `areas:` frontmatter and `docs/indexes.md` provide the defense mechanisms.

Topics:
- [links](./links.md)
