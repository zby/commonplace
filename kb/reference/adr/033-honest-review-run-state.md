---
description: "Review runs gain a queued state and an honest created/started clock, introduced through a versioned migration substrate for the review store"
type: ../types/adr.md
tags: []
status: accepted
---

# 033-Honest review-run state behind a versioned migration substrate

**Status:** accepted
**Date:** 2026-06-28

## Context

[ADR 031](./031-review-state-uses-run-owned-review-pairs.md) made the persistent unit of review work a run-owned `(note, gate)` pair, and [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) moved freshness onto DB-owned snapshots keyed by `model_partition`. Review state lives in a SQLite store (`kb/reports/review-store.sqlite`).

Two problems in that store blocked further work and misrepresented reality:

1. **Prepared prompts lied about being in progress.** `review_runs.status` allowed only `running`, `completed`, and `failed`, and `started_at` was `NOT NULL`. `create_run_with_pairs` hardcoded `status="running"`. So the live-agent and batch-prepare paths recorded a prompt as `running`, with a fabricated start time, before any reviewer had consumed it.
2. **The store had no migration path.** `ensure_db` applied `review-schema.sql` only when `review_runs` was absent; `CREATE TABLE IF NOT EXISTS` cannot relax a `NOT NULL` or change a CHECK. Any schema change on an existing store required a manual rebuild that risked acceptance history.

This is the first, self-contained phase of a larger queued-job review-execution refactor. It stands on its own: the honest state fixes a live bug, and the migration substrate is a prerequisite for later schema changes. The remaining pipeline work — the `review_runs` -> `review_jobs` rename, the create/run/finalize command surface, dropping item-level `model_partition`, and acceptance-provenance tightening — remains out of scope.

## Decision

Two coupled commitments land on the current table names (`review_runs`, `review_pairs`).

**1. Introduce a versioned migration substrate for the review store.**

`PRAGMA user_version` is the stored schema version, against a `LATEST_REVIEW_SCHEMA_VERSION` constant. `ensure_db` creates a fresh DB from `review-schema.sql` at the latest version, and for an existing DB applies ordered migration functions until it reaches the latest version. Changes SQLite cannot express with a simple `ALTER TABLE` use an explicit table-rebuild path guarded by integrity checks: `PRAGMA foreign_key_check`, expected tables/indexes/views present, and row counts preserved. A migration that cannot preserve integrity fails and leaves the old DB readable. Migration code lives next to `review_db.py`, because every command calls `ensure_db`.

**2. Make review-run state an explicit, queue-capable machine with an honest clock.**

Status is now:

```text
queued, running, completed, failed
```

Meanings:

- `queued`: prompt and pair rows exist; no worker has claimed execution;
- `running`: a worker has claimed execution;
- `completed`: all required pairs completed and accepted;
- `failed`: execution, parse, preparation, or coverage failed.

The clock splits into `created_at TEXT NOT NULL` (preparation time) and nullable `started_at` (worker claim/start time); `completed_at` is unchanged. Run creation sets status explicitly: the live-agent and batch-prepare paths create `queued` with `started_at = NULL`; subprocess execution paths create `running` with `started_at` set. The ingest/finalization gates accept `queued` or `running`, so a prepared run can be finalized without first being marked running.

The honest-state change is migration **version 1**. It rebuilds `review_runs`, copying each existing row's `started_at` into `created_at` while preserving `started_at`, and recreates the model-partition time index ordered by `created_at`. Acceptance history is preserved; no store rebuild and no re-review are required.

## Consequences

Easier:

- Prepared prompts are represented honestly as `queued` instead of fabricated `running` rows.
- The review store can evolve through versioned migrations instead of manual, history-losing rebuilds.
- `created_at` and `started_at` become distinct timestamps, so run age and worker-start state are answerable.
- A `queued` state exists, which is the precondition for the later queued-job pipeline.
- The schema change preserves acceptance history.

Harder / accepted costs:

- `ensure_db` now owns schema migration as well as initial creation.
- The version-1 migration rebuilds a parent table referenced by `review_pairs`, so it must temporarily disable SQLite foreign-key enforcement around the controlled table swap and then run integrity checks.
- `ReviewRunRow`, run loaders, status gates, and run-creation callers must handle nullable `started_at`.
- The tables still say `run` while the concept is moving toward `job`. That naming mismatch remains until the later mechanical rename.

---

Relevant Notes:

- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) — extends: refines the run row it defined with an honest status/clock, without restructuring pairs.
- [032-Review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) — see-also: same SQLite review store; this adds the reusable migration substrate.
- [030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters](./030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the prepare/ingest seams whose prepared runs are now honestly `queued` rather than `running`.
