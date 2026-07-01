---
description: "Superseded historical decision: review state moved to invocation-owned note-gate pairs, later simplified into current all-or-nothing review jobs and review pairs"
type: ../types/adr.md
tags: []
status: superseded
---

# 031-Review state uses invocation-owned review pairs

**Status:** superseded by [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md)
**Date:** 2026-06-22

## Context

[ADR 010](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) moved review state into SQLite once reviews stopped being authored git artifacts and became operational state. Its first implementation still carried a note-scoped execution shape into the schema while the prompt protocol, selector, warning picker, and acceptance state were already reasoning in `(note, gate)` pairs.

[ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) made the execution protocol explicit: the unit of review work is one `(note_path, gate_id)` pair, while note-packed and gate-packed calls are only packing strategies over that same pair protocol.

The storage model needed to match the protocol's real invariant: one prompt invocation owns the requested `(note, gate)` pairs.

## Decision

Store review execution state as invocation-owned review pairs.

The durable part of this decision is current:

- `review_pairs` stores every requested `(note_path, gate_path)` pair inside one review job.
- Missing output was originally represented at the pair level; ADR 035 later removed persisted pair status.
- Completed pairs were originally salvageable from a failed containing job; ADR 035 later made live finalization all-or-nothing.
- Acceptance points at a concrete completed pair, so warnings and stale-state checks can recover the exact reviewed text and provenance.

ADR 034 later simplified the parent row into `review_jobs`, removed pair-level model duplication, required selector JSON as the creation input, and required every acceptance row to carry completed review evidence. ADR 035 later removed claim/running state, pair status, and partial salvage. ADR 036 later collapsed acceptance to one current row per key.

## Consequences

Easier:

- The database, prompt protocol, parser, selectors, and warning surfaces share the same unit of work.
- Packing becomes provenance on the parent job, not a different data model.
- Finalization is simpler: requested rows already exist and parsed output completes matching rows. ADR 035 later made absent output fail the whole job without pair-level missing state.
- Batch artifacts have one stable job id, manifest, prompt, and bundle output for the invocation that produced them.
- Cleanup and repair tools can reason over obsolete review pairs without deleting a whole shared job directory unless every pair in that job is obsolete.

Harder / accepted costs:

- A parent job no longer means "one note". Consumers must inspect `packing` and child pairs instead of inferring shape from the id.
- The original partial-success design created two layers of state. ADR 035 removes that live behavior: failed jobs do not accept a completed subset.

---

Relevant Notes:

- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — supersedes: keeps the SQLite storage boundary while refining the concrete schema.
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — see-also: the protocol decision whose pair unit this storage model made persistent.
- [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) — supersedes: current job/pair schema and command surface.
- [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — supersedes: current all-or-nothing finalization and derived artifact paths.
- [review system architecture](../review-architecture.md) — part-of: the subsystem whose data model centers on `review_jobs` and `review_pairs`.
- [storage architecture](../storage-architecture.md) — part-of: the broader storage boundary that treats review state as the SQLite-backed exception.
