---
description: When write invariants are unsettled, canonical files let systems add constraints gradually and rebuild read views; database authority becomes warranted when correctness depends on write-time invariants or unowned mutable state
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [architecture]
---

# Incrementally constrained files defer centralized schema commitment until write invariants stabilize

Keeping authored files canonical does not eliminate schema. Filenames, directories, frontmatter, link labels, and validators still constrain the data. The advantage is narrower: a file-backed system can defer when those commitments become binding. While write-side invariants are unsettled, constraints can remain close to the authored documents and comparatively easy to revise rather than being enforced centrally on every write.

This advantage holds when three conditions are met:

- agents already share file and Git tools;
- canonical writes do not yet require transactions, uniqueness, per-record authorization, or similar invariants; and
- missing read capabilities can be rebuilt from the authored documents.

Under these conditions, files provide a usable authoring surface immediately. Git records diffs, branches, and document history. Editors and repository browsers render the content without a purpose-built viewer. Agents can use ordinary read, write, and search tools without a storage-specific API. These are contingent tool-chain savings, not benefits that every environment grants files for free.

## Files still accumulate schema

A file-backed KB does not choose between schema and no schema. It chooses weaker, distributed conventions before stronger centralized enforcement. Changing a frontmatter field across thousands of notes or repairing links after a path convention changes is still a data migration.

The useful difference is the sequence in which commitments become binding. Files can [add constraints only after repeated use exposes a stable pattern](./progressive-constraining-commits-only-after-patterns-stabilize.md): raw Markdown can acquire frontmatter, typed links, validators, and derived indexes one observed need at a time. Each addition should make an actual access pattern cheaper or a known invalid state impossible.

This is [incremental constraining](./definitions/constraining.md): postpone enforcement whose requirements are unknown, but do not postpone information that later enforcement will need. Stable identities and provenance needed later should be captured from the first record; write invariants already known should be enforced from the outset. A database can also defer normalization, for example through a document table with flexible metadata. The file choice is therefore warranted by the available authoring and inspection tools, not by a claim that databases are inherently rigid.

## The boundary is derived views versus authoritative state

Once a system needs capabilities beyond direct file access, the decisive question is whether the supporting structure is rebuildable or authoritative. Read-side capabilities can remain derived when the canonical documents contain everything needed to reconstruct them. Semantic search, retrieval ranking, quality scores, and a traversable link graph can fit this pattern. A derived copy is safe only when it is [checked against its recomputable source or omitted](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md); otherwise the convenience layer quietly becomes a second, stale source of truth.

A database earns authority when an invariant must hold at write time or when mutable state cannot be assigned safely to a single document. Examples include concurrent uniqueness, transactional updates, per-record access control, fact-validity intervals, and mutable state on an ownerless many-to-many relation. The important question is not file count. It is whether the database can be discarded and rebuilt from the authored documents without losing information or violating correctness.

[Graphiti](https://github.com/getzep/graphiti) illustrates the authoritative class. Its design puts bitemporal relationship validity and graph operations in a graph database. A file-backed system could retain source facts and build graph or temporal indexes from them. But if correctness depends on the database updating validity as facts change, that temporal state is not a disposable view. Commonplace reaches the same boundary at a smaller scale: documents remain Markdown, while churning review freshness on `(note, criterion)` edges lives in SQLite because [no single document owns that mutable relation](./many-to-many-edge-state-is-where-files-yield-to-a-database.md).

The decision rule is therefore conditional. Prefer incrementally constrained files when shared file tooling makes authored documents cheap to inspect and revise, canonical writes can tolerate weak enforcement, and added capabilities remain rebuildable. Prefer database authority when its infrastructure is already the cheaper shared substrate or when correctness requires stable write-time invariants. A mixed system often follows: files own authored knowledge, while databases serve either as disposable read views or as authoritative stores for scoped operational state. Whether the database can be rebuilt distinguishes those roles.

---

Relevant Notes:

- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — mechanism: generalizes the timing rule behind adding storage constraints only after their need is observed
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: supplies the safety condition for file-backed indexes and views
- [Current-task fit alone does not warrant costly structural entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — contrasts: distinguishes unknown future requirements from overcommitting to today's known queries
- [Storage architecture](../reference/storage-architecture.md) — evidenced-by: shows the mixed file-and-SQLite boundary in the shipped Commonplace system
- [Churning state on a many-to-many edge is where files yield to a database](./many-to-many-edge-state-is-where-files-yield-to-a-database.md) — extends: names one structural trigger for scoped database authority
- [Lessons from Building AI Agents for Financial Services](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) — evidenced-by: reports canonical object storage with PostgreSQL as a derived query index in a production workload
- [What the matrix shows across 148 agent memory systems](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — evidenced-by: file-backed systems are common in the reviewed corpus, while substrate alone predicts little about activation or verification
- [The GitHub for Context Doesn't Exist Yet](../sources/the-github-for-context-doesn-t-exist-yet-2077772169455530152.ingest.md) — evidenced-by: qualifies Git history by showing that it does not supply semantic dependency or governance information
