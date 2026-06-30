---
description: Where Commonplace stores data — authored markdown under kb/, derived indexes rebuilt from those files, and the review subsystem's local SQLite database
type: kb/types/note.md
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

Document type is declared by `type:` in frontmatter and validated against the matching schema, resolved from the owning collection's `types/` directory with fallback to global `kb/types/`. See [available-types.md](./available-types.md) and [type-loading.md](./type-loading.md).

## Derived indexes

Each surface below is derived from the authored markdown; none of it is committed. Complete generated listings exist only in the built site (ADR 025).

| Surface | What it covers | Where it is produced |
|---|---|---|
| Directory listing pages (per-collection `dir-index.md`) | Title, description, and type of every note in the directory | mkdocs hook, build time only |
| Per-tag generated listings (below each curated tag index) | Notes grouped by tag, minus already-curated entries | mkdocs hook, build time only |
| MkDocs static site | Entire `kb/` tree, configured by `mkdocs.yml` | `mkdocs build` |

Agents enumerate the same information on demand with the scoped `rg` recipes in [navigation.md](./navigation.md).

The `redirect_maps` block in `mkdocs.yml` preserves external URLs across note renames.

## Generated reports

Generated reports record operational work products rather than curated library knowledge. Connect reports under `kb/reports/connect/` are discovery artifacts produced by `/cp-skill-connect` and consumed by downstream workflows such as ingestion. They are intentionally gitignored because they are regenerable from the source artifact and current KB state; their absence from `git status` is expected.

## Review state (SQLite)

Review state is the one subsystem that is not file-backed. The review database stores:

| Table | Contents |
|---|---|
| `review_jobs` | One row per review invocation/prompt, with freshness `model_partition`, nullable runner provenance, `queued`/`running`/`completed`/`failed` status, created/started/completed timing, and prompt/output artifact paths |
| `review_pairs` | One row per requested `(note_path, gate_path)` pair inside a job; model partition is derived through the parent job |
| `acceptance_events` | Append-only per-gate acceptance history |

Acceptance is keyed by `(note_path, gate_path, model_partition)`. Current acceptance for any key is the latest `acceptance_events` row, exposed via the `current_gate_acceptances` view. Selector logic reads current note and gate content from files and compares their hashes against accepted DB-owned snapshots.

Notes, gates, instructions, and source material remain file-backed. See [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md), [ADR-032](./adr/032-review-freshness-uses-db-snapshots-not-git.md), [ADR-033](./adr/033-honest-review-run-state.md), and [ADR-034](./adr/034-queued-review-jobs-and-execution-provenance.md) for the rationale.

## See also

- [documentation-site.md](./documentation-site.md) — how the MkDocs site renders these files, the README-vs-index rule, and the reader landing-page inventory
- [architecture.md](./architecture.md) — installed project layout and surface-by-role
- [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — decision: SQLite for review state
- [ADR-007](./adr/007-reports-directory-for-generated-snapshots.md) — decision: `kb/reports/` for generated operational artifacts
