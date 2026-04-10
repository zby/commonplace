---
description: Commonplace's current storage architecture — markdown files as source of truth, qmd and generated listings as derived indexes, SQLite as a scoped exception for review-state operational data
type: note
tags: [architecture]
status: current
---

# Storage architecture

Commonplace's storage boundary as it exists today. This is a current-state description: what is file-backed, what is a derived index, and which subsystem crosses into SQLite and why. For the general argument that files beat a database for agent-operated knowledge bases, see [files-not-database](../notes/files-not-database.md).

## Primary substrate: markdown files under git

All authored library content lives as markdown under `kb/`:

- `kb/notes/` — transferable claims and theory
- `kb/reference/` — current-state descriptions of the commonplace system and ADR decision history (this collection)
- `kb/sources/` — ingested external sources
- `kb/tasks/` — task lifecycle documents
- `kb/work/` — workshop artifacts
- `kb/instructions/` — skills and procedural guidance

Each document is a markdown file with YAML frontmatter. Types are identified by `type:` in frontmatter and validated by schemas declared in the collection's `types/` directory. Nothing about authored content requires tooling beyond an editor, grep, and git — agents read these files with the same Read/Grep tools they use for source code.

## Derived indexes

Capabilities that files alone can't provide are added as derived layers. Each index is a build artifact rebuildable from the files at any time:

- **qmd** — semantic search index over all collections, configured via `qmd-collections.yml`. Rebuilt from markdown source, answers retrieval queries the `rg`+frontmatter layer can't handle economically.
- **Generated listing indexes** — `kb/notes/index.md`, `kb/sources/index.md`, and similar files are produced by `commonplace-generate-notes-index`. They exist to give agents a scannable table of contents without having to list a directory.
- **Tag indexes** — curated editorial pages (`kb/notes/tags-index.md` and subordinate tag pages) with auto-generated sections appended by `commonplace-sync-generated-index`.
- **MkDocs site** — the whole KB is rendered to static HTML via `mkdocs.yml`, with a `redirect_maps` block that preserves external URLs across renames. The site is a derived view, not a source of truth.

None of these indexes are authored directly; they are all regenerable. Losing an index is a rebuild, not a data loss.

## Scoped exception: SQLite for review state

Review state is the one subsystem that is not file-backed. Per [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md), review runs, gate reviews, acceptance events, and their provenance live in a local SQLite database keyed by `(note_path, gate_id, model_id)`.

The exception is justified by two shifts that moved review artifacts out of the authored-library shape:

1. Per-gate review artifacts were removed from git because they produced too much churn. Once they stopped participating in git history and diffs, the main file advantage weakened.
2. To preserve selector and ack behavior outside git, each review had to carry operational metadata (accepted SHAs, gate fingerprints, acceptance timestamps, model partitions). The subsystem was no longer primarily reading prose — it was querying current state and mutating acceptance rows.

At that point the read/write pattern had shifted from "load document, render prose" to "query state, transition state," which is exactly what a small local database is for. Notes, gates, instructions, and source material remain file-backed because they are still authored, human-reviewable, and versioned. Review state isn't any of those things anymore.

The boundary: **files remain the right default for authored knowledge under git. Once a specific artifact leaves git and the system mostly wants indexed state transitions over it, SQLite is the simpler representation.** The boundary is narrow and keyed to the review subsystem; no other commonplace subsystem currently sits on the operational-state side of it.

---

Relevant Notes:

- [files-not-database](../notes/files-not-database.md) — theory: the general argument that files beat a database early, and why a scoped database exception does not refute the files-first position
- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md) — decision: the full rationale and consequences of the SQLite boundary for review state
- [007-reports-directory-for-generated-snapshots](./adr/007-reports-directory-for-generated-snapshots.md) — related: the move of review artifacts to `kb/reports/` preceded and enabled the SQLite transition
- [architecture](./architecture.md) — current-state: how the storage substrate sits inside the broader repo layout
