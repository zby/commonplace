---
description: "Superseded historical decision: honest queued/running review state and a general migration substrate were reduced to queued/completed/failed jobs; a later release added one narrow v4→v5 migration"
type: ../types/adr.md
tags: []
status: superseded
---

# 033-Honest review state behind a versioned migration substrate

**Status:** superseded by [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) and [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)
**Date:** 2026-06-28

## Context

With review work stored as invocation-owned pairs ([ADR 031](./031-review-state-uses-run-owned-review-pairs.md)) and freshness on DB-owned snapshots ([ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md)), the store shape misrepresented prepared prompts as already in progress: prompt creation wrote a start time and a running status before any reviewer had consumed the prompt. Schema evolution was also hard, because `CREATE TABLE IF NOT EXISTS` could not alter existing checks or nullability.

## Decision

Represent review invocation state as an explicit state machine (`queued`, `running`, `completed`, `failed`) in which a prepared prompt is `queued` until a reviewer starts on it, and gate the store on a schema version, moving mismatched stores forward through an explicit in-place migration substrate rather than transforming table shapes implicitly.

## Consequences

Prepared prompts are no longer reported as in progress, and stores at an unsupported version are rejected rather than silently reshaped. A general migration substrate is a standing maintenance commitment for every schema change; ADR 034 and ADR 035 kept queued state and version gating, dropped `running` and the migration framework, and a later schema version added one explicit version-specific migration as the exception.

---

Relevant Notes:

- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) — predecessor: defined pair ownership for a review invocation.
- [032-Review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) — see-also: same SQLite review store and freshness model.
- [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) — supersedes: keeps honest job state while removing in-place schema migration.
- [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — supersedes: reduces live job state to queued/completed/failed.
