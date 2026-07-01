---
description: Review acceptance stores only the current accepted baseline per note/gate/model key and prunes superseded review evidence inline
type: ../types/adr.md
tags: []
status: accepted
---

# 036-Review acceptance is current state, not append-only history

**Status:** accepted
**Date:** 2026-07-01

## Context

The review store originally modeled accepted baselines as an append-only ledger.
`acceptance` rows accumulated over time, and `current_gate_acceptances` selected
the latest event per `(note_path, gate_path, model_partition)`. A separate prune
command later deleted superseded rows and whole obsolete job artifacts.

That kept historical acceptance transitions explicit, but no current code
consumed that history. The only runtime readers needed the current accepted
baseline, and the standalone prune command existed to remove the history that the
system did not otherwise use.

## Decision

Store acceptance as current state: one `acceptance` row per
`(note_path, gate_path, model_partition)`.

Successful finalization and acknowledgement upsert that row. When an upsert
supersedes a prior acceptance, the same DB transaction prunes obsolete review
pairs, whole jobs that have no remaining pairs, and unreferenced file snapshots.
Whole obsolete job artifact directories are removed after the DB commit as a
best-effort filesystem cleanup.

Failed reviews never update acceptance and never trigger superseding cleanup, so
the prior last-known-good baseline remains available until a replacement review
successfully finalizes.

This ADR supersedes the append-only acceptance framing in ADR 010, ADR 032, ADR
034, and ADR 035. Those ADRs still stand for the SQLite boundary, DB-owned
snapshots, queued jobs, execution provenance, and all-or-nothing finalization.

## Consequences

Easier:

- Freshness lookup no longer needs a latest-event query; the table is already at
  the accepted state the selector needs.
- Superseded review cleanup happens where superseding happens, so operators do
  not need a periodic prune command.
- Snapshot retention is simpler: a snapshot is deleted only when no current
  acceptance row and no remaining review pair references it.

Harder / accepted costs:

- Acceptance history is not retained in SQLite. The review store keeps current
  operational state and review evidence, not an audit ledger of every accepted
  baseline transition.
- The acceptance write path carries a small cascade-prune helper so bundled jobs
  are retained until all of their pairs are superseded.

---

Relevant Notes:

- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — supersedes-in-part: keeps the SQLite boundary but replaces append-only acceptance history with current-state acceptance
- [032-review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) — refines: current acceptance rows still pin DB-owned note/gate snapshots
- [034-queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) — supersedes-in-part: acceptance evidence still points at completed review pairs, but no longer as an event ledger
- [035-review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — refines: successful finalization upserts acceptance and prunes superseded evidence inside the success transaction
