---
description: Techniques from cludebot worth borrowing — what we already cover, what to adopt now, and what to watch for as the KB grows
areas: [claw-design]
status: current
---

# What cludebot teaches us

[Cludebot](https://github.com/sebbsssss/cludebot) is a "molecular memory" system for AI agents — typed relations, decay-based retention, dream-cycle consolidation, hybrid retrieval. It's designed for large-scale agent memory (thousands of memories, multiple users, Supabase + pgvector backend). Our KB is ~200 markdown notes on a local filesystem with qmd for search. Most of cludebot's infrastructure is overkill at our scale, but several of its ideas are worth borrowing — and some may become relevant as the KB grows.

## What we already have

Cludebot's best ideas overlap significantly with patterns we've already adopted:

**Typed link semantics.** Cludebot uses `supports`, `contradicts`, `elaborates`, `causes`, `follows`. We use `extends`, `foundation`, `contradicts`, `enables`, `example`. Same principle — relations carry more information than raw similarity. Our link semantics are documented in CLAUDE.md and used in prose links throughout the KB.

**Progressive disclosure.** Cludebot's `recallSummaries()` → `hydrate()` pattern returns lightweight summaries first, full content on demand. We do the same with `description` frontmatter: scan titles and descriptions via `rg`, then `Read` the full note. Same cognitive benefit, zero infrastructure.

**Hybrid retrieval.** Cludebot combines keyword matching, vector similarity, tag overlap, and graph traversal. We combine `rg` (structured/exact queries on frontmatter) with `qmd query` (BM25 + vector + reranking). Both systems recognize that neither keyword nor semantic search alone is sufficient.

**Evidence linkage.** Cludebot ties synthesized statements to source memory IDs. We do this with inline markdown links — every claim links to upstream notes. Less structured but equally traceable.

## Worth adopting now

These techniques would improve the KB without adding infrastructure:

**Active contradiction surfacing.** We have `contradicts` as a link semantic, but we don't actively look for contradictions. Cludebot treats contradiction as a retrieval mode, not just a label. Concretely: when `/connect` finds a candidate link, it should ask "does this *contradict* the new note?" not just "is this related?" A KB that only surfaces agreement becomes quietly overconfident. This is a prompt change, not an architecture change.

**Explicit staleness decay.** Cludebot assigns different decay rates to different memory types (episodic fades at 7%/day, semantic at 2%/day, self-model at 1%/day). We have `status: current | outdated | speculative` but no systematic way to flag notes for review based on age. A lightweight version: during `/review`, prioritize notes whose linked code or ADRs have changed since the note was last updated. The [three-space model](./three-space-agent-memory-maps-to-tulving-taxonomy.md) already predicts that operational notes should churn faster than knowledge notes — decay rates would formalize that intuition. The [note quality scores](./notes-need-quality-scores-to-scale-curation.md) note proposes type-dependent recency decay as one scoring dimension, formalizing this intuition.

**Consolidation passes.** Cludebot's "dream cycles" periodically synthesize clusters of related memories into higher-level insights with evidence links. We have `/review` but no consolidation step that asks: "these 5 notes about the same topic — can they be merged into one stronger note?" As the KB grows past 300-400 notes, this becomes important to prevent fragmentation.

## Watch for as the KB grows

These are premature now but worth revisiting at scale:

**Graph-based retrieval.** Cludebot traverses typed bonds between memories (O(k) where k ≈ 3-5 hops) instead of scanning all memories (O(n)). At 200 notes, `qmd query` returns results in under a second — graph traversal would add complexity for no speed gain. But if the KB reaches 1000+ notes with dense cross-linking, navigating via link graph could outperform flat search for "find everything connected to this cluster."

**Co-retrieval reinforcement.** Cludebot strengthens links between memories that are frequently retrieved together (Hebbian learning). We'd need retrieval logging to implement this. Interesting signal — notes that consistently co-appear in search results probably should be linked — but not worth building until we have enough query volume to make the signal meaningful.

**Compaction.** Cludebot summarizes old, low-importance, faded memories into consolidated group summaries with evidence links to originals. If our operational notes accumulate faster than we archive them, a periodic pass that merges or summarizes stale clusters could keep the KB navigable. The [three-space model](./three-space-agent-memory-maps-to-tulving-taxonomy.md)'s notion of "graduation from operational to knowledge space" is essentially manual compaction.

## What to skip

**The molecular metaphor.** Atoms, bonds, molecules, stability scores. The metaphor is evocative but the value comes from the concrete mechanics underneath (typed relations, evidence links, decay rates). We already have those mechanics in simpler form.

**Supabase/pgvector/Solana infrastructure.** Cludebot runs on a database stack with vector indexes. We run on markdown files with qmd and rg — and [files beat a database for agent knowledge bases](./files-not-database.md) because they preserve the universal interface (Read/Write/Grep), get versioning for free via git, and require zero infrastructure. Migrating to a database would add operational complexity without clear benefit at our scale.

**Automated importance scoring.** Cludebot uses LLM calls to score memory importance 1-10. At our scale, the human decides what's worth writing down. That implicit filter is more reliable than automated scoring.

Topics:
- [claw-design](./claw-design.md)
