---
description: Files with git beat a database for agent-operated knowledge bases — universal interface, free versioning, no infrastructure to maintain
type: note
traits: []
areas: [kb-design]
status: current
---

# Files beat a database for agent-operated knowledge bases

The temptation as a KB grows is to move to a database. But files are the universal interface — agents read/write them directly with tools they already have (Read, Write, Grep), git gives versioning and diffing for free, grep searches thousands of files in milliseconds, and markdown renders everywhere (GitHub, editors, browsers). [Koylanai's Personal Brain OS](../sources/koylanai-personal-brain-os.ingest.md) arrived at the same conclusion independently: 80+ files in markdown, YAML, and JSONL, no database, no API keys, no build step — and the system works because the file formats are the interface.

A database migration doesn't just change storage — it replaces the entire tool chain:

- **Versioning**: You'd reimplement git, badly. Database versioning is either "diffs in a table" (fragile, no branching) or "shell out to git" (then why move?).
- **Browsing**: Files render in any editor or on GitHub with zero setup. A database needs a web UI — a whole application to build and maintain.
- **Agent access**: Agents currently use Read/Write/Grep — tools they already have. A database requires an API layer or DB client on every interaction.
- **Infrastructure**: Files need nothing. A database needs hosting, backups, migrations, and someone to maintain it.

## What actually breaks at scale

1. **Finding things** — solved by semantic search indexes (qmd)
2. **Too many files per directory** — solved by subdirectories
3. **Structured queries with scoring** — the real gap, but solvable with [note quality scores](./notes-need-quality-scores-to-scale-curation.md)

The pattern is: files as source of truth, derived indexes for capabilities files alone can't provide. Each index (semantic, structured, scoring) is a build artifact that can be rebuilt from files at any time.

This is the same pattern qmd already uses for semantic search — it indexes files, it doesn't replace them. The [patterns proven in practice](./what-works.md) confirm this works: frontmatter makes files queryable via grep, qmd adds semantic search, and progressive disclosure keeps token costs low — all without leaving the filesystem.

[Cludebot's database stack](./what-cludebot-teaches-us.md) (Supabase, pgvector) provides a useful counterpoint: the techniques worth borrowing from it (typed link semantics, contradiction surfacing, staleness decay) can all be implemented over files without the infrastructure overhead.

## Where the trade-off tips: Graphiti

[Graphiti](../sources/graphiti-temporal-knowledge-graph.ingest.md) is the strongest counterexample to the files-first position. Its graph database dependency is not incidental — it requires capabilities that files genuinely cannot replicate:

- **Bi-temporal edge invalidation** — every relationship carries valid_at/invalid_at timestamps, enabling point-in-time queries ("what was true on date X?") and contradiction resolution through temporal supersession rather than overwriting. Git history tracks *when a file changed*, not *when the fact it describes became true or false*.
- **Community detection** — label propagation over entity nodes discovers clusters automatically. Files have no native graph traversal; link-based clustering requires building an explicit graph representation first.
- **Hybrid graph+semantic retrieval** — combining graph traversal with embedding similarity in a single query requires both representations co-located in a queryable store.

The lesson is not that files are wrong for our KB — they remain the right choice for authored, agent-navigated knowledge where versioning, inspectability, and zero infrastructure matter most. The lesson is that the files-first argument has a boundary: systems that need temporal invalidation, automated graph analytics, or hybrid traversal+semantic queries have legitimate reasons to pay the database cost. Graphiti's use case (continuously streaming conversational data with contradictions over time) is genuinely different from ours (authored notes with explicit status transitions), and the architectural difference follows from the use case difference.

---

Relevant Notes:

- [what works](./what-works.md) — provides the evidence base: frontmatter queries, semantic search via qmd, and progressive disclosure all work within the file-based architecture
- [what cludebot teaches us](./what-cludebot-teaches-us.md) — evaluates a database-backed agent memory system and concludes the valuable techniques transfer to files without the infrastructure cost
- [Koylanai Personal Brain OS](../sources/koylanai-personal-brain-os.ingest.md) — independent practitioner report validating the same architectural choice at 80+ file scale
- [Fintool: Lessons from Financial Services](../sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.ingest.md) — validates at commercial scale: S3 as source of truth with Lambda-synced PostgreSQL as derived index, paying users, 11-nines durability; strongest production evidence for files-first with derived indexes
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — addresses the "structured queries" gap with composite note scores; derived indexes keep files as source of truth
- [Graphiti](../sources/graphiti-temporal-knowledge-graph.ingest.md) — contradicts: the strongest counterexample — bi-temporal queries, edge invalidation, and community detection genuinely require database infrastructure

Topics:

- [kb-design](./kb-design.md)
