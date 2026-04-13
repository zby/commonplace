---
description: Where commonplace stores data — authored markdown under kb/, derived indexes rebuilt from those files, and the review subsystem's local SQLite database
type: note
tags: []
status: current
---

# Storage

Commonplace stores data in three layers: authored markdown files under `kb/`, derived indexes rebuilt from those files, and a local SQLite database scoped to the review subsystem.

## Authored markdown

All authored content lives as markdown with YAML frontmatter under `kb/`, tracked in git. Every file is readable and editable without tooling beyond an editor and `grep`.

| Directory | Contents |
|---|---|
| `kb/notes/` | Transferable claims and theory |
| `kb/reference/` | Shipped-system reference docs and ADRs |
| `kb/sources/` | Ingested external sources |
| `kb/tasks/` | Task lifecycle documents |
| `kb/work/` | Workshop artifacts |
| `kb/instructions/` | Skills and procedural guidance |
| `kb/types/`, `kb/*/types/` | Global and collection-scoped type definitions |

Document type is declared by `type:` in frontmatter and validated against the matching schema in the owning collection's `types/` directory. See [available-types.md](./available-types.md) and [type-loading.md](./type-loading.md).

## Derived indexes

Each index below is regenerable from the authored markdown. Losing an index is a rebuild, not a data loss.

| Index | What it covers | Rebuild command |
|---|---|---|
| Directory listing pages (`kb/notes/dir-index.md`, `kb/sources/dir-index.md`) | Title, description, and type of every note in the directory | `commonplace-generate-notes-index <dir>` |
| Tag-index generated tails (`kb/notes/tags-index.md` and subordinate tag pages) | Notes grouped by tag below the `<!-- generated -->` marker | `commonplace-sync-generated-index` |
| All of the above at once | — | `commonplace-refresh-indexes` |
| qmd semantic search index | Every collection listed in `qmd-collections.yml` | External `qmd` CLI |
| MkDocs static site | Entire `kb/` tree, configured by `mkdocs.yml` | `mkdocs build` |

The `redirect_maps` block in `mkdocs.yml` preserves external URLs across note renames.

## Review state (SQLite)

Review state is the one subsystem that is not file-backed. The review database stores:

| Table | Contents |
|---|---|
| `review_runs` | One row per review invocation on a note |
| `review_run_gates` | Gate set captured at run start, with per-gate SHAs |
| `gate_reviews` | Append-only per-gate review history |
| `acceptance_events` | Append-only per-gate acceptance history |

Acceptance is keyed by `(note_path, gate_id, model_id)`. Current acceptance for any key is the latest `acceptance_events` row, exposed via the `current_gate_acceptances` view. Selector logic reads current note and gate SHAs from files and compares them against accepted SHAs from the database.

Notes, gates, instructions, and source material remain file-backed. See [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md) for the rationale.

## See also

- [architecture.md](./architecture.md) — installed project layout and surface-by-role
- [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md) — decision: SQLite for review state
- [ADR-007](./adr/007-reports-directory-for-generated-snapshots.md) — decision: `kb/reports/` for generated operational artifacts
