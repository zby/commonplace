# Phase 1: Honest job state

**Status: ready to implement.** This is the uncontested first phase extracted from [implementation-plan.md](./implementation-plan.md). It carries no new commands, no acceptance-data migration, no acceptance-semantics change, and no rename. Everything else in the queued-job design stays in the main plan as Phase 2 (design, not yet scheduled).

## Why this is worth doing on its own

The live-agent / orchestrator path records a prepared prompt as `running` before any reviewer has touched it: `src/commonplace/review/review_db.py:create_run_with_pairs` hardcodes `status="running"`, and `review_runs.started_at` is `NOT NULL`, so a prepared run must claim a start time it does not have. That is a real bug in the current system, independent of the queue.

Phase 1 fixes it by giving review runs a `queued` state and an honest clock. It is also a strict prerequisite for the queued-job pipeline, so none of the work is wasted if Phase 2 slips.

## Scope

In scope:

- the review-store migration substrate (`user_version` runner + table-rebuild helper), built once here and reused by all of Phase 2;
- the `review_runs` status machine and its timing columns;
- the two code gates that assume `running`;
- the run-creation callers that currently rely on the hardcoded `running` default.

Out of scope (stays Phase 2): the `create-review-jobs` / `run-review-jobs` / `job-list` commands, the shared execution core, the selector contract reshape, dropping item-level `model_partition`, ack provenance, no-relocation, the parallel runner, and the `review_runs`→`review_jobs` rename. **Phase 1 keeps the current names** (`review_runs`, `review_pairs`) to stay minimal; the rename is the first task of Phase 2.

## Schema change

In `review-schema.sql`, on `review_runs`:

- add `queued` to the status CHECK: `status IN ('queued', 'running', 'completed', 'failed')`;
- add `created_at TEXT NOT NULL` (preparation time);
- make `started_at` nullable (worker claim/start time; null for a run that goes `queued` → `completed` through orchestrator ingest);
- `completed_at TEXT` already exists and is unchanged.

State meanings after the change:

- `queued`: prompt and pair rows exist; no worker has claimed execution;
- `running`: a worker has claimed execution;
- `completed`: all required pairs completed and accepted;
- `failed`: execution, parse, or coverage failed; salvaged completed pairs retained per existing policy.

The index `idx_review_runs_model_partition_started` currently orders by `started_at DESC`; switch it to `created_at DESC` so queued rows (null `started_at`) still sort. Rename it to `idx_review_runs_model_partition_created` in the same schema/migration change so integrity checks do not preserve a misleading index name.

## Migration substrate comes first

There is **no migration runner today**. `ensure_db` → `init_db` applies the schema only when `review_runs` does not exist (`src/commonplace/review/review_db.py:init_db`); existing stores are never altered, and `CREATE TABLE IF NOT EXISTS` will not relax a `NOT NULL` or change a CHECK. So Phase 1 has two parts, in order:

**Part A — build the migration substrate** (Slice 0 in the main plan; uncontested and reused by all of Phase 2):

- add a `LATEST_REVIEW_SCHEMA_VERSION = 1` constant and `PRAGMA user_version` handling;
- fresh DB creation applies `review-schema.sql`, then sets `PRAGMA user_version = 1`;
- `ensure_db` reads `user_version` on an existing DB and applies ordered migration functions until current;
- add a table-rebuild helper (SQLite cannot `ALTER` away `NOT NULL` / a CHECK in place) and a post-migration integrity check (`PRAGMA foreign_key_check`, expected tables/indexes/views present);
- migrations live next to `review_db.py`, since every command calls `ensure_db`. A migration that cannot preserve integrity fails and leaves the old DB unchanged.

**Part B — the honest-job-state change is migration version 1.** It rebuilds `review_runs`: create the new-shape table, `INSERT ... SELECT` copying `started_at` into `created_at` (existing rows were all created-as-running, so `created_at := started_at` is correct and `started_at` is preserved), drop, rename, recreate the index on `created_at DESC`. This preserves acceptance history; no store rebuild and no re-review.

The table-rebuild helper must handle dependent foreign keys deliberately. `review_pairs.review_run_id` references `review_runs` with `ON DELETE CASCADE`, so dropping/replacing the parent table with foreign keys active can fail or cascade destructively. For a controlled rebuild, the helper may disable `PRAGMA foreign_keys` only around the table swap, but SQLite requires this outside any active transaction. `ensure_db` must not wrap this controlled swap in an outer `with conn:` transaction:

1. `PRAGMA foreign_keys = OFF`;
2. `BEGIN IMMEDIATE` or `BEGIN EXCLUSIVE`;
3. create/copy/drop/rename/reindex the table;
4. run `PRAGMA foreign_key_check`, row-count checks, and expected-index/view checks before commit;
5. rollback on any failed check, leaving the old DB readable;
6. commit;
7. `PRAGMA foreign_keys = ON` in a `finally` path even if the swap fails;
8. run `PRAGMA foreign_key_check` again after re-enabling.

This is not optional or silent. If the controlled swap proves too fragile in implementation, rebuild `review_runs` and its dependent tables together instead of risking a parent-table drop.

The substrate is the only part of Phase 1 with design content, and it is the foundation every later schema change reuses — which is why it belongs in the first phase rather than being improvised per change.

## Code changes

1. **Run creation stops lying.** Change the creation API, not just the default status: `create_run` / `create_run_with_pairs` should take `created_at: str`, `started_at: str | None`, and an explicit `status` instead of requiring `started_at: str` and hardcoding `status="running"` in `src/commonplace/review/review_db.py:create_run_with_pairs`. Confirm every run-creation caller and set its status explicitly.
2. **Loaded run rows match the schema.** Add `created_at` to `ReviewRunRow`, make its `started_at` field `str | None`, and update `_review_run_from_row`, `load_review_run`, and any direct run-row SELECTs/tests that assume `started_at` is always present and non-null.
3. **Both status gates accept `queued` or `running`.** Two places reject any status other than `running` and must be widened, or a prepared run cannot be ingested:
   - `src/commonplace/review/batch.py:ingest_batch_output`;
   - `src/commonplace/review/finalization.py:record_and_finalize_run`.
4. **Check the failure-cleanup path.** `fail_running_review_runs` (`src/commonplace/review/executor.py`, invoked from `src/commonplace/review/batch.py:prepare_review_batch` and the immediate executor flow) is currently named and filtered for `running` only. Rename it to reflect the widened behavior, or keep the old name only as a short-lived wrapper, and ensure it transitions `queued` preparation failures as well as `running` execution failures to `failed`.

Caller contract:

| Caller | Purpose | Phase 1 status/timing |
|---|---|---|
| `src/commonplace/review/batch.py:prepare_review_batch` via `commonplace-create-review-runs` and `commonplace-prepare-review-batch` | live-agent / orchestrator preparation only | `queued`, `created_at=now`, `started_at=NULL` |
| `src/commonplace/review/run_review_bundles.py:_run_group` | subprocess runner executes immediately | `running`, `created_at=now`, `started_at=now` |
| `src/commonplace/review/run_gate_sweep.py:prepare_batch_targets` | subprocess runner executes immediately | `running`, `created_at=now`, `started_at=now` |
| review DB test helpers and direct schema tests | fixture setup | explicit status and timing matching the fixture's intent |

Phase 1 intentionally does **not** add a generic worker-claim transition. Prepared orchestrator runs can go `queued` → `completed` or `queued` → `failed` during ingest/finalization. Immediate subprocess runs keep the existing `running` → `completed` / `failed` lifecycle. A real `queued` → `running` claim API belongs to Phase 2 with the queued-job runner.

## Tests

- a fresh DB initializes at the latest schema version; an existing `user_version = 0` DB migrates exactly once; a failed migration rolls back and leaves the old tables readable;
- the `review_runs` rebuild preserves row counts, foreign keys, and indexes, renames the model-partition time index to `idx_review_runs_model_partition_created`, and populates `created_at` from the old `started_at`;
- the controlled rebuild does not delete dependent `review_pairs`; `PRAGMA foreign_key_check` is clean after migration;
- `load_review_run` exposes `created_at` and returns `started_at=None` for queued runs;
- preparing a live-agent / batch run creates it `queued` with a non-null `created_at` and null `started_at`;
- the subprocess executor path creates `running` runs with `started_at` set;
- `batch.ingest` accepts a `queued` run;
- `record_and_finalize_run` accepts a `queued` run (does not raise on status);
- both gates still reject `completed` and `failed`;
- a preparation failure moves a `queued` run to `failed`;
- current tests that expect live-agent prepared runs to be `running` are updated to assert `queued`, not weakened;
- immediate subprocess tests still assert rows become `running` before execution finalizes, or use a focused unit seam where final status does not race past `running`;
- `kb/reference/REVIEW-SYSTEM.md` and `kb/reference/review-architecture.md` document `queued`, `created_at`, and nullable `started_at`.

## Done when

`pytest` passes, a prepared run is observably `queued` rather than `running`, an existing review store has been migrated without losing acceptance history, and ADR 033 has been promoted from [adr-draft-033-honest-review-run-state.md](./adr-draft-033-honest-review-run-state.md) if the implementation lands. At that point Phase 2 can begin with the `review_runs`→`review_jobs` rename on a clean, honest state machine.
