---
description: "DRAFT for ADR 033 — review runs gain a queued state and an honest created/started clock, introduced through a new versioned migration substrate for the review store"
type: kb/types/note.md
---

> **Promoted draft.** Phase 1 landed and this decision was promoted as [ADR 033](../../reference/adr/033-honest-review-run-state.md). Scope tracks [phase-1-honest-job-state.md](./phase-1-honest-job-state.md).

# 033-Honest review-run state behind a versioned migration substrate

**Status:** promoted as [ADR 033](../../reference/adr/033-honest-review-run-state.md)
**Date:** 2026-06-28

## Context

[ADR 031](../../reference/adr/031-review-state-uses-run-owned-review-pairs.md) made the persistent unit of review work a run-owned `(note, gate)` pair, and [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) moved freshness onto DB-owned snapshots keyed by `model_partition`. Review state lives in a SQLite store (`kb/reports/review-store.sqlite`).

Two problems in that store block further work and misrepresent reality today:

1. **Prepared prompts lie about being in progress.** `review_runs.status` allows only `running`, `completed`, and `failed`, and `started_at` is `NOT NULL`. `create_run_with_pairs` hardcodes `status="running"`. So the live-agent / orchestrator path and the batch-prepare path record a prompt as `running`, with a fabricated start time, before any reviewer has consumed it. "Prepared" and "executing" are conflated, `started_at` is not actually a start time, and there is no state that means "ready, not yet claimed."

2. **The store has no migration path.** `ensure_db` applies `review-schema.sql` only when `review_runs` is absent; `CREATE TABLE IF NOT EXISTS` cannot relax a `NOT NULL` or change a CHECK. Any schema change on an existing store is currently impossible without a manual rebuild that discards acceptance history and forces re-review.

This is the first, self-contained phase of a larger queued-job review-execution refactor held in the [review-execution-pipeline workshop](./README.md). It is separated out because it stands on its own: the honest state fixes a live bug, and the migration substrate is a prerequisite for every later schema change. The remaining pipeline work — the `review_runs`->`review_jobs` rename, the `create`/`run`/`finalize` command surface, dropping pair-level `model_partition`, and acceptance-provenance tightening — is deliberately out of scope here and will land under later ADRs.

## Decision

Two coupled commitments, both on the current table names (`review_runs`, `review_pairs`).

**1. Introduce a versioned migration substrate for the review store.**

`PRAGMA user_version` is the stored schema version, against a `LATEST_REVIEW_SCHEMA_VERSION` constant. `ensure_db` creates a fresh DB from `review-schema.sql` at the latest version, and for an existing DB applies ordered migration functions inside a transaction until it reaches the latest version. Changes SQLite cannot express with a simple `ALTER TABLE` use an explicit table-rebuild helper — create the new-shape table, `INSERT ... SELECT`, drop, rename, recreate indexes and views — guarded by a post-migration integrity check (`PRAGMA foreign_key_check`, expected tables/indexes/views present, row counts preserved). A migration that cannot preserve integrity fails and leaves the old DB unchanged. Migration code lives next to `review_db.py`, because every command calls `ensure_db`.

**2. Make review-run state an explicit, queue-capable machine with an honest clock.**

Status becomes `status IN ('queued', 'running', 'completed', 'failed')`:

- `queued`: prompt and pair rows exist; no worker has claimed execution;
- `running`: a worker has claimed execution;
- `completed`: all required pairs completed and accepted;
- `failed`: execution, parse, or coverage failed.

The clock splits into `created_at TEXT NOT NULL` (preparation time) and a nullable `started_at` (worker claim/start time); `completed_at` is unchanged. Run creation sets status explicitly: the prepare / live-agent / batch paths create `queued` with `started_at = NULL`; the subprocess executor, which runs immediately, creates `running` with `started_at` set. The two code gates that assume `running` — `batch.ingest` and `record_and_finalize_run` — accept `queued` or `running`, so a prepared run can be finalized without first being marked running.

The honest-state change is migration **version 1**, exercising the substrate from commitment 1. It rebuilds `review_runs`, copying each existing row's `started_at` into `created_at` (all existing rows were created-as-running, so this is correct) while preserving `started_at`, and recreates the model-partition time index ordered by `created_at`. Acceptance history is preserved; no store rebuild and no re-review.

## Consequences

Easier:

- Prepared prompts are represented honestly as `queued` instead of fabricated `running` rows; the live-agent "prepared == running" lie is gone.
- The review store can evolve. Every future schema change rides the versioned migration substrate instead of a manual, history-losing rebuild — this is the durable enabler the rest of the refactor depends on.
- `created_at` and `started_at` become real, distinct timestamps, so run age and "has a worker started" are answerable.
- A `queued` state exists, which is the precondition for the queued-job pipeline; this ADR unblocks that work without committing to it.
- The schema change preserves acceptance history, so no re-review is triggered.

Harder / accepted costs:

- `ensure_db` is no longer a one-shot apply; the store now carries migration code and a schema version, and each future schema change must ship a tested migration.
- The table-rebuild path toggles `PRAGMA foreign_keys` around the swap inside a transaction to avoid `ON DELETE CASCADE` from `review_pairs` destroying rows during a parent-table replace. It is guarded by integrity checks, but it is more delicate than a plain `ALTER`.
- Adding `queued` and making `started_at` nullable ripples into row-reading code (`ReviewRunRow`, run loaders, the status gates) and any caller assuming `started_at` is non-null.
- This is a partial step: the tables still say `run` while the concept is moving to `job`. That naming mismatch persists until the Phase 2 rename, and is accepted to keep this phase minimal and low-risk.

---

Relevant Notes:

- [031-review state uses run-owned review pairs](../../reference/adr/031-review-state-uses-run-owned-review-pairs.md) — extends: refines the run row it defined with an honest status/clock, without restructuring pairs.
- [032-Review freshness uses DB snapshots, not Git](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: same SQLite review store; this adds the reusable migration substrate that 032's one-off stopped-operation migration lacked.
- [030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters](../../reference/adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the prepare/ingest seams whose prepared runs are now honestly `queued` rather than `running`.
