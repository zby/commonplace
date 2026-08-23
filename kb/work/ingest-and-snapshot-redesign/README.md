# Minimal ingest and source-snapshot migration

**State:** active. The sole progress authority is [state.md](./state.md).

## Goal

Ship the smallest version of the ingest change already selected in discussion:

- The tracked ingest carries the durable source identity, capture metadata,
  primary-snapshot checksum, and KB analysis.
- Source content is materialized locally when it must be read; it is not
  tracked as the ingest's authority.
- An ingest has one URL-backed primary source and zero or more secondary
  sources. V1 accepts only commit-pinned `implementation` secondaries.
- The current ingest body format stays in place. A migration removes only body
  information that merely repeats a new field.

V1 does not introduce directory primaries. The two existing irregular
`source_snapshot` values receive explicit migration dispositions; they do not
define another supported input shape.

## What closes the workshop

- The exact v1 fields, checksum semantics, and local materialization path are
  specified with one ordinary and one code-grounded example.
- Types, schemas, instructions, capture commands, source URL extraction, and
  tests implement those examples.
- Existing tracked ingests carry their durable source and capture fields plus
  the exact primary-snapshot checksum, and retain their analytical body except
  for direct field duplication.
- Existing source material is preserved locally before tracked copies retire.
- Durable-library links that depended on retiring snapshots have valid
  replacement targets. Peer workshops and frozen workflow fixtures remain
  outside the corpus migration's authority and retain their working-history
  paths until their owners revise or close them.
- The full relevant test and validation suite passes.
- One ADR records the shipped choice. Its `Postponed` section is the only
  retained list of extensions not implemented in v1.

## Recovery protocol

At the start of a session:

1. Read this file, [state.md](./state.md), and the active phase in
   [plan.md](./plan.md).
2. Run `git status --short`; this workshop opened in an already-dirty worktree.
3. Inspect the active write set and last evidence in `state.md`.
4. If a phase is `IN_PROGRESS`, rerun its checks before trusting its edits.

Only `state.md` carries live phase marks. A phase becomes `COMPLETE` only after
its evidence is recorded. The bulk migration uses a row-per-artifact ledger so
a replacement agent never has to infer progress from filename order.

## Files

- [state.md](./state.md) — current phase, next action, write set, and evidence.
- [plan.md](./plan.md) — the four remaining v1 phases.
- [inventory.md](./inventory.md) — dated baseline and affected surfaces.
- `v1-shape.md` — created in P1 with exact before/after examples.
- `migration.tsv` — created before P3 bulk edits.

The workshop is temporary. The implementation and ADR become durable; this
directory is removed when the work closes.

---

- [Ingest source units and supporting material](../../reference/proposals/ingest-source-units-and-supporting-material.md) — input: the already-selected primary-plus-secondary direction
- [ADR 045: source genre is a single open field on the snapshot](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md) — current authority allocation that the v1 ADR must supersede or revise
- [Source collection contract](../../sources/COLLECTION.md) — current-system: the tracked snapshot/analysis split being migrated
