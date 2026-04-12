---
description: Files beat a database early on — a schema commits to access patterns before you know them, and files let you constrain incrementally while getting free browsing, versioning, and agent access from day one
type: note
traits: []
tags: [architecture]
status: current
---

# Files beat a database for agent-operated knowledge bases

The temptation as a KB grows is to move to a database. But a database migration doesn't just change storage — it replaces the entire tool chain:

- **Versioning**: Git gives branching, diffing, and history for free. Database versioning is either "diffs in a table" (fragile, no branching) or "shell out to git" (then why move?).
- **Browsing**: Files render in any editor or on GitHub with zero setup. A database needs a viewing layer built for it — a whole application to build and maintain.
- **Agent access**: Agents use Read/Write/Grep — tools they already have. A database requires an API layer or DB client on every interaction.
- **Infrastructure**: Files need nothing. A database needs hosting, backups, migrations, and someone to maintain it.

[Koylanai's Personal Brain OS](../sources/koylanai-personal-brain-os.ingest.md) arrived at the same conclusion independently: 80+ files in markdown, YAML, and JSONL, no database, no API keys, no build step.

## Premature schema commitment

The practical arguments above are real, but there's a deeper reason: a database schema is a commitment to access patterns you don't yet understand. When a project is young, you don't know what queries matter, what relationships will emerge, or how knowledge will be organized six months from now. A schema encodes those assumptions in DDL — and every reorganization becomes a migration.

Files let you defer that commitment and [constrain incrementally](./definitions/constraining.md) as you learn. Raw markdown first, then frontmatter conventions, then grep-based queries, then derived indexes (semantic search, quality scores). Each step adds structure only after the access pattern has been observed in practice. This is the [constrain/relax cycle](./agentic-systems-interpret-underspecified-instructions.md) applied to storage architecture — stay at the least constrained medium until you've seen enough to know what to commit to.

This isn't a files-forever position. Once access patterns stabilize, a database may earn its place — either as a replacement or, more likely, as a derived layer alongside files. The point is that starting with a database front-loads a commitment you're not yet equipped to make. Files buy time to learn what the right schema would be. The browsing cost compounds this: early on, when the methodology is still forming, having to build a viewing layer before anyone can browse the knowledge is a real barrier. Files give a usable system from day one.

## What actually breaks at scale

The failure modes files hit at scale are all addressable without abandoning the substrate:

1. **Finding things** — solved by semantic search indexes derived from the files
2. **Too many files per directory** — solved by subdirectories
3. **Structured queries with scoring** — the real gap, but solvable with [note quality scores](./notes-need-quality-scores-to-scale-curation.md)

The pattern is: files as source of truth, derived indexes for capabilities files alone can't provide. Each index is a build artifact rebuildable from files at any time. [Cludebot's database stack](../agent-memory-systems/reviews/cludebot.md) (Supabase, pgvector) provides a useful counterpoint: the techniques worth borrowing from it (typed link semantics, contradiction surfacing, staleness decay) can all be implemented over files.

## Where the trade-off tips: Graphiti

[Graphiti](../sources/graphiti-temporal-knowledge-graph.ingest.md) is the strongest counterexample to the files-first position. Its graph database dependency is not incidental — it requires capabilities that files genuinely cannot replicate:

- **Bi-temporal edge invalidation** — every relationship carries valid_at/invalid_at timestamps, enabling point-in-time queries ("what was true on date X?") and contradiction resolution through temporal supersession rather than overwriting. Git history tracks *when a file changed*, not *when the fact it describes became true or false*.
- **Community detection** — label propagation over entity nodes discovers clusters automatically. Files have no native graph traversal; link-based clustering requires building an explicit graph representation first.
- **Hybrid graph+semantic retrieval** — combining graph traversal with embedding similarity in a single query requires both representations co-located in a queryable store.

The lesson is not that files are wrong for authored, agent-navigated knowledge where versioning, inspectability, and zero infrastructure matter most. The lesson is that the files-first argument has a boundary: systems that need temporal invalidation, automated graph analytics, or hybrid traversal+semantic queries have legitimate reasons to pay the database cost. Graphiti's use case (continuously streaming conversational data with contradictions over time) is genuinely different from authored-notes use cases (documents with explicit status transitions), and the architectural difference follows from the use case difference.

A second kind of boundary shows up inside a mostly files-first system: a specific subsystem can outgrow the authored-document shape even when the rest of the KB stays file-backed. Once an artifact leaves git and the system mostly wants indexed state transitions over it, a local database is simpler than pretending the files are still the primary representation. That scoped exception is compatible with the files-first position, not a refutation of it.

---

Relevant Notes:

- [storage-architecture](../reference/storage-architecture.md) — current-state: how commonplace instantiates this argument today, including the derived-index layer and the scoped SQLite review-state exception
- [cludebot](../agent-memory-systems/reviews/cludebot.md) — evaluates a database-backed agent memory system and concludes the valuable techniques transfer to files without the infrastructure cost
- [Koylanai Personal Brain OS](../sources/koylanai-personal-brain-os.ingest.md) — independent practitioner report validating the same architectural choice at 80+ file scale
- [Fintool: Lessons from Financial Services](../sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.ingest.md) — validates at commercial scale: S3 as source of truth with Lambda-synced PostgreSQL as derived index, paying users, 11-nines durability; strongest production evidence for files-first with derived indexes
- [Coding Agents are Effective Long-Context Processors](../sources/coding-agents-are-effective-long-context-processors.ingest.md) — extends: benchmark evidence that exposing corpora as navigable files changes agent strategy (coordinate-based read/slice beats monolithic scans), suggesting part of files' value is operational, not just storage ergonomics
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — addresses the "structured queries" gap with composite note scores; derived indexes keep files as source of truth
- [Graphiti](../sources/graphiti-temporal-knowledge-graph.ingest.md) — contradicts: the strongest counterexample — bi-temporal queries, edge invalidation, and community detection genuinely require database infrastructure
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — extends: files are one important choice for the runtime's execution substrate
- [Tracecraft](../agent-memory-systems/reviews/tracecraft.md) — tests: applies the files-over-database bet to ephemeral coordination state (write-heavy, latency-sensitive, disposable) rather than durable knowledge, where the access patterns differ significantly
