---
description: "Superseded historical decision: honest queued/running review state survived, while the versioned in-place migration substrate was removed"
type: ../types/adr.md
tags: []
status: superseded
---

# 033-Honest review state behind a versioned migration substrate

**Status:** superseded by [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md)
**Date:** 2026-06-28

## Context

[ADR 031](./031-review-state-uses-run-owned-review-pairs.md) made the persistent unit of review work a `(note, gate)` pair owned by one review invocation, and [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) moved freshness onto DB-owned snapshots keyed by `model_partition`.

The previous store shape misrepresented prepared prompts as already in progress: prompt creation wrote a non-null start time and a running status before any reviewer had consumed the prompt. It also made schema evolution hard, because SQLite's `CREATE TABLE IF NOT EXISTS` could not alter existing checks or nullability.

This ADR introduced two ideas:

1. an explicit state machine with `queued`, `running`, `completed`, and `failed`;
2. an in-place schema migration substrate.

## Decision

The honest state survived and is current. A review job is `queued` after deterministic prompt creation, `running` after a parent claims it for dispatch, and then `completed` or `failed` after finalization.

The migration substrate did not survive the simplification. The current review store is schema-current only: a missing DB is created from the packaged schema; a mismatched review store is rejected and must be recreated.

## Consequences

Kept:

- Prepared prompts are represented honestly as `queued`.
- `created_at` and `started_at` remain distinct timestamps.
- Finalization accepts `queued` or `running` for manual recovery when output exists before an explicit claim.

Removed:

- In-place review-store migrations.
- Historical table-shape transforms.
- Any promise that old local operational review stores can be opened by the current package.

---

Relevant Notes:

- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) — predecessor: defined pair ownership for a review invocation.
- [032-Review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) — see-also: same SQLite review store and freshness model.
- [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) — supersedes: keeps honest job state while removing in-place schema migration.
