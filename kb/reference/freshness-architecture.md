---
description: "Code architecture of the general freshness substrate: commonplace store, file-text versioning, target baselines, transitions, global status, and the review adapter"
type: kb/types/note.md
tags: []
---

# Freshness architecture (`commonplace.store` + `commonplace.freshness`)

General artifact freshness records exact input snapshots against which a target was accepted, compares them with current resolved versions, and selects affected targets. It does not adjudicate truth, run reviews, or rewrite notes. Review is the first consumer: `review-pair` targets with `note` and `criterion` `file-text` inputs.

For review execution (jobs, pairs, finalization, prompts), see [review architecture](./review-architecture.md). For operator workflows, see [commands](./commands.md) and [README-REVIEW-SYSTEM](./README-REVIEW-SYSTEM.md).

## Physical store

| path | role |
|---|---|
| `kb/reports/commonplace-store.sqlite` | Current operational database (review + freshness) |
| `kb/reports/review-store.sqlite` | Schema-v7 backup; read-only migration source |
| `COMMONPLACE_STORE` | Env override for store path (`COMMONPLACE_REVIEW_DB` still honored as fallback) |

`commonplace.store` owns connection setup, schema version refusal (`PRAGMA user_version = 1`), foreign-key enforcement, and whole-store integrity dispatch. `commonplace.review.review_schema` delegates to it. If the new default is absent but the legacy backup exists beside it, store preparation refuses with a migration command rather than creating an empty database.

Migrate retained evidence with `scripts/migrate-review-db-v7-to-commonplace-store.py` ([ADR 052](./adr/052-general-freshness-store-review-first-migration.md)).

## Data model

| Table / view | Role |
|---|---|
| `artifact_snapshots` | Path-keyed `file-text` versions: exact UTF-8 text, SHA-256, capture time |
| `freshness_baselines` | One current row per `(target_kind, target_key_json)` with monotonic `revision` |
| `freshness_inputs` | Accepted input roles for a target, each FK to an `artifact_snapshots` row |
| `review_freshness_evidence` | Review-only bridge retaining the completed evidence pair for a `review-pair` target |
| `review_jobs`, `review_pairs` | Review execution state (unchanged role; snapshot FKs retargeted to `artifact_snapshots`) |
| `current_review_freshness_baselines` | Review adapter view over generic tables — not canonical state |

v1 admits only `file-text` versioning and `review-pair` targets. Target identity is canonical JSON (`target_kind` + sorted `target_key_json`). Review keys use `{note_path, criterion_path, model_partition}`.

## Package layout

```
commonplace.store          Connection, schema, integrity, path resolution
commonplace.freshness/
  models.py                ArtifactSnapshot dataclass
  keys.py                  Canonical target JSON encoding
  versioning.py            file-text resolution from repo paths
  snapshots.py             Insert/dedupe/load artifact snapshots
  baselines.py             Review-pair baseline read/write (capture + observation)
  selector.py              Repository-wide stale target selection
  status.py                Status projection and JSON rendering
  transitions.py           accept, ack, retire, capture refresh primitives
  integrity.py             Hash and review-pair structural checks
commonplace.cli.freshness_*   Global status, accept, ack, retire CLIs
```

Review adapters in `commonplace.review` call into `freshness` for compare/persist; they retain review-specific discovery (`missing-baseline`), reason mapping (`criterion-changed` before `note-changed`), trivial ack, and capture finalization.

## Transitions

| transition | owner | live check | evidence |
|---|---|---|---|
| capture refresh | `finalize_capture_refresh()` in review finalization | no | replaced |
| observation refresh | `commonplace-freshness-accept` | yes | n/a (rejects `review-pair` in v1) |
| observation ack | `commonplace-freshness-ack`, `commonplace-ack-review` | yes | preserved on review-pair |
| retirement | `commonplace-freshness-retire` | — | cascade delete bridge |

Queued review jobs record `review_pairs.expected_baseline_revision` at pair create. Capture finalization CASes that revision; a moved baseline after queue yields `stale-baseline-revision` (or `stale-queued-capture` at migration).

## Selection and status

`commonplace-freshness-status` reports all registered targets. It dedupes resolution, supports `--json`, `--diff`, `--all`, and `--model-partition`, and exits `0`/`1`/`2` per [freshness JSON contracts](../work/artifact-freshness-and-referential-checks/freshness-schemas.md).

`commonplace-review-target-selector` keeps `missing-baseline` discovery for applicable pairs not yet registered. Global status does not replace that discovery path.

Malformed registered state is a store error — never downgraded to `missing-baseline` or ordinary staleness.

## Command surface

- `commonplace-freshness-status` — repository-wide status over registered targets
- `commonplace-freshness-accept` — observation refresh for non-review targets (v1: rejects `review-pair`)
- `commonplace-freshness-ack` — ack changed inputs from a status-derived manifest
- `commonplace-freshness-retire` — remove a registered baseline

## Deferred

Collection-as-artifact freshness (`collection-text`, `collection-maintenance`) is not implemented. See [proposal: collection-as-artifact freshness](./proposals/collection-as-artifact-freshness.md).

## See also

- [ADR 052](./adr/052-general-freshness-store-review-first-migration.md) — decision record
- [Storage](./storage-architecture.md) — where the store sits among authored markdown and derived indexes
- [Review architecture](./review-architecture.md) — review adapter and execution flow