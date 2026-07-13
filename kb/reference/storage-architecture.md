---
description: Where Commonplace stores data — authored markdown under kb/, derived indexes rebuilt from those files, and the review subsystem's local SQLite database
type: kb/types/note.md
tags: []
---

# Storage

Commonplace stores data in three layers: authored markdown files under `kb/`, derived indexes rebuilt from those files, and a local SQLite operational store for review execution and artifact freshness.

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

Full-pass packets are the scoped exception to report statelessness. A pending or resolved `full-pass-report.md` owns non-regenerable disposition state plus immutable start-state captures, so resolution-aware cleanup retains the packet as one unit while that state remains actionable ([ADR 051](./adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md)). The packet remains local and gitignored; portability across clones or machines is not promised.

## Operational store (SQLite)

The operational store (`kb/reports/commonplace-store.sqlite`; override `COMMONPLACE_STORE`) is the one subsystem that is not file-backed. It holds general artifact freshness and review execution in one database ([ADR 052](./adr/052-general-freshness-store-review-first-migration.md)). The retained `kb/reports/review-store.sqlite` is the schema-v7 backup; migrate before relying on the new default.

| Table | Contents |
|---|---|
| `artifact_snapshots` | Path-keyed `file-text` versions with mandatory stored text |
| `freshness_baselines` | Current accepted baseline per `(target_kind, target_key_json)` with monotonic `revision` |
| `freshness_inputs` | Accepted input roles pointing at snapshot ids |
| `review_freshness_evidence` | Review-only bridge from a `review-pair` target to its evidence pair |
| `review_jobs` | One row per review invocation/prompt, with `model_partition`, nullable runner provenance, status, timing, grouping |
| `review_pairs` | One row per requested `(note_path, criterion_path)` pair, with result protocol, reviewed snapshot ids, and queued-job `expected_baseline_revision` |

Prompt, job-output, manifest, and per-pair result paths remain derived from review job state. Review freshness baselines are `review-pair` targets over `note` and `criterion` `file-text` inputs; `current_review_freshness_baselines` is the review-shaped adapter view. `commonplace-freshness-status` reports all registered targets; `commonplace-review-target-selector` keeps applicable-pair discovery including `missing-baseline`. Malformed baselines raise store integrity errors. Successful supersede prunes obsolete review rows, unreferenced snapshots, and whole obsolete job artifact directories inline.

Notes, criteria, instructions, and source material remain file-backed. See [freshness architecture](./freshness-architecture.md), [review architecture](./review-architecture.md), [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md), [ADR-032](./adr/032-review-freshness-uses-db-snapshots-not-git.md), and [ADR-052](./adr/052-general-freshness-store-review-first-migration.md).

## See also

- [documentation-site.md](./documentation-site.md) — how the MkDocs site renders these files, the README-vs-index rule, and the reader landing-page inventory
- [architecture.md](./architecture.md) — installed project layout and surface-by-role
- [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — outcome: SQLite for review state
- [ADR-007](./adr/007-reports-directory-for-generated-snapshots.md) — outcome: `kb/reports/` for generated operational artifacts
- [ADR 051](./adr/051-full-pass-packets-own-guarded-captures-and-resolutions.md) — outcome: full-pass packets are a stateful, resolution-aware report exception
- [freshness-architecture.md](./freshness-architecture.md) — general freshness substrate and review adapter
- [ADR 052](./adr/052-general-freshness-store-review-first-migration.md) — outcome: commonplace-store replaces review-only freshness tables
