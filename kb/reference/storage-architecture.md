---
description: Where Commonplace stores data — authored markdown under kb/, derived indexes rebuilt from those files, and the review subsystem's local SQLite database
type: kb/types/note.md
tags: []
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
| `review_jobs` | One row per review invocation/prompt, with freshness `model_partition`, nullable finalization-time runner provenance, `queued`/`completed`/`failed` status, created/completed timing, and grouping |
| `review_pairs` | One row per requested `(note_path, criterion_path)` pair inside a job, with persisted `result_kind`, nullable outcome, `completed_at`, and reviewed snapshot IDs; model partition is derived through the parent job |
| `freshness_baselines` | Current snapshot-pinned freshness baseline per `(note_path, criterion_path, model_partition)` |

Prompt, job-output, manifest, and per-pair result paths are derived from the review job id, grouping, and pair set. A freshness baseline is keyed by `(note_path, criterion_path, model_partition)` and stored as one current row per key; it means the evidence is fresh, not that the note is globally approved. `current_freshness_baselines` enriches those rows with evidence-pair results and baseline snapshot content. Selector logic compares current note and criterion hashes against those snapshots; malformed baselines raise integrity errors. Successful supersede prunes obsolete review rows, unreferenced snapshots, and whole obsolete job artifact directories inline; there is no separate prune command.

Notes, criteria, instructions, and source material remain file-backed. The operational schema and commands name the generic assay axis `criterion`; `gate` names only closed-ended, verdict-kind criteria and their catalog. See [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md), [ADR-032](./adr/032-review-freshness-uses-db-snapshots-not-git.md), [ADR-033](./adr/033-honest-review-run-state.md), [ADR-034](./adr/034-queued-review-jobs-and-execution-provenance.md), [ADR-035](./adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md), and [ADR-036](./adr/036-review-acceptance-is-current-state-not-append-only-history.md) for the rationale.

## See also

- [documentation-site.md](./documentation-site.md) — how the MkDocs site renders these files, the README-vs-index rule, and the reader landing-page inventory
- [architecture.md](./architecture.md) — installed project layout and surface-by-role
- [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — outcome: SQLite for review state
- [ADR-007](./adr/007-reports-directory-for-generated-snapshots.md) — outcome: `kb/reports/` for generated operational artifacts
