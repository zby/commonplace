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

[ADR 010](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) moved review state into SQLite, but the first schema still carried a note-scoped execution shape while the prompt protocol, selector, warning picker, and acceptance state already reasoned in `(note, gate)` pairs, which [ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) made the explicit unit of review work. Storage must key on the same unit the protocol, selector, and acceptance reason in: one prompt invocation owns its requested `(note, gate)` pairs.

## Decision

Store review execution state as invocation-owned review pairs: every requested `(note, gate)` pair is a row inside the one review invocation that produced it, packing (note-packed or gate-packed) is provenance on the parent rather than a different data model, and acceptance points at a concrete completed pair so warnings and stale-state checks can recover the exact reviewed text and provenance. Missing output is represented at the pair level, and completed pairs are salvageable from a failed containing invocation.

## Consequences

The database, prompt protocol, parser, selectors, and warning surfaces share one unit of work, and each invocation has one stable id, manifest, prompt, and bundle output. A parent row no longer means "one note", so consumers must inspect packing and child pairs instead of inferring shape from the id. Pair-level status and partial salvage created two layers of state; ADR 034 and ADR 035 kept invocation-owned pairs and removed those.

---

Relevant Notes:

- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — supersedes: keeps the SQLite storage boundary while refining the concrete schema.
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — see-also: the protocol decision whose pair unit this storage model made persistent.
- [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) — supersedes: current job/pair schema and command surface.
- [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — supersedes: current all-or-nothing finalization and derived artifact paths.
- [review system architecture](../review-architecture.md) — part-of: the subsystem whose data model centers on `review_jobs` and `review_pairs`.
- [storage architecture](../storage-architecture.md) — part-of: the broader storage boundary that treats review state as the SQLite-backed exception.
