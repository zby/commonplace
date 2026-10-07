---
description: "Iceberg documents snapshot reads, atomic metadata publication, and assumption-checked retries: a bounded model for shared KB state, not semantic reconciliation."
source: https://iceberg.apache.org/docs/latest/reliability/
captured: "2026-10-07"
capture: trafilatura
capture_scope: full-source
genre: official-statement
snapshot_sha256: ed54517ec5319dcbde1911279386fd1b8e0854a2c21227c10bbf60cc9829f0c2
ingested: "2026-10-07"
occasion: "We need a simple model that can support all of these interactions."
type: types/ingest-report.md
domains: [storage, concurrency, coordination]
---

# Ingest: Apache Iceberg reliability

## Classification

Official project documentation explaining the intended correctness mechanisms and guarantees of Iceberg tables. It is an authoritative account of the design, not an independent evaluation of its implementation.

Author: Apache Iceberg project; the maintainers describe their own table format and commit protocol.

## Summary

Iceberg replaces reconstructing table contents through file listings with explicit file membership in persistent snapshot metadata. Writes and deletes prepare new snapshots that reuse earlier metadata; commits atomically replace the current table metadata reference. The project attributes consistent lock-free reads, a linear history of table updates, rollback, and safe file-level operations to this construction. Concurrent writers use optimistic concurrency: a writer whose commit loses rebuilds metadata against current state, checks that its operation's assumptions still hold, and reuses unaffected work where possible. Compaction, for example, may remove two input files and add their merged replacement only if both inputs remain in the table. The page also claims planning and object-store compatibility benefits from avoiding directory listings and renames, but provides no measurements.

## Quotes

> Every write or delete produces a new snapshot that reuses as much of the previous snapshot's metadata tree as possible to avoid high write volumes.
> --- `kb/sources/.snapshots/apache-iceberg-reliability.md` @ `sha256:ed54517ec5319dcbde1911279386fd1b8e0854a2c21227c10bbf60cc9829f0c2` — Reliability

> Valid snapshots in an Iceberg table are stored in the table metadata file, along with a reference to the current snapshot. Commits replace the path of the current table metadata file using an atomic operation.
> --- `kb/sources/.snapshots/apache-iceberg-reliability.md` @ `sha256:ed54517ec5319dcbde1911279386fd1b8e0854a2c21227c10bbf60cc9829f0c2` — Reliability

> **Reliable reads** : Readers always use a consistent snapshot of the table without holding a lock
> --- `kb/sources/.snapshots/apache-iceberg-reliability.md` @ `sha256:ed54517ec5319dcbde1911279386fd1b8e0854a2c21227c10bbf60cc9829f0c2` — Reliability guarantees

> If the atomic swap fails because another writer has committed, the failed writer retries by writing a new metadata tree based on the new current table state.
> --- `kb/sources/.snapshots/apache-iceberg-reliability.md` @ `sha256:ed54517ec5319dcbde1911279386fd1b8e0854a2c21227c10bbf60cc9829f0c2` — Concurrent write operations

> Commits are structured as assumptions and actions. After a conflict, a writer checks that the assumptions are met by the current table state. If the assumptions are met, then it is safe to re-apply the actions and commit.
> --- `kb/sources/.snapshots/apache-iceberg-reliability.md` @ `sha256:ed54517ec5319dcbde1911279386fd1b8e0854a2c21227c10bbf60cc9829f0c2` — Retry validation

## Connections Found

For the caller's search for a simple interaction model, Iceberg supplies a concrete shared-state protocol: read a snapshot, prepare a change, check its assumptions, and atomically publish accepted state. It is a bounded engineering illustration for [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md): shared storage alone is not the guarantee; snapshot visibility and conflict admission are explicit mechanisms. This protocol addresses structural inconsistency, not the note's other concerns about contamination, semantic adjudication, or delegated accountability. It also compares with [Edge ownership selects the key; choosing files or a database requires a workload comparison](../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md). Iceberg documents a file-backed construction with additional atomic publication machinery, so neither files nor database rows alone determine coordination guarantees. It supplies no workload comparison that would select a Commonplace storage implementation.

## Extractable Value

1. **A compact shared-state interaction model.** Separate reading accepted state, preparing candidate work, validating operation assumptions, and publishing through one atomic boundary. Iceberg makes these stages concrete without requiring that payload preparation hold a reader lock. This could clarify the shared-state part of the occasion; the unspecified “all of these interactions” prevents claiming complete coverage. [quick-win]
2. **Retry permission depends on current assumptions.** A competing commit is not permission to replay blindly. The compaction example supplies a precise rejection condition: either missing input invalidates the operation. For agent-operated KB changes, analogous predicates would need to be defined per operation; file membership alone would not establish that an edited claim remains justified. [experiment]
3. **Payload files and accepted membership are distinct.** Iceberg's metadata reference determines which prepared files belong to the readable table. This is a concrete comparison for the existing storage-choice note: file-backed coordination can require an explicit publication layer, whose implementation and operating costs belong in the workload comparison. [just-a-reference]

## Limitations (our opinion)

The page states the project's intended guarantees without independent tests, benchmarks, implementation inspection, or a detailed account of backend-specific atomic commit primitives. Atomic metadata-reference replacement is a required premise, not a property established for every object store by this ingest. The planning and compatibility claims should remain documentation claims rather than measured performance or verified deployment results. The historical Hive/S3 motivation does not establish the present behavior of every Hive or S3 configuration.

The compaction example concerns known concurrent changes to file membership. It does not cover ambiguous external effects, arbitrary idempotency, semantic conflict resolution, or safe retries for every operation. Serializing accepted table states cannot decide whether agent-authored knowledge is true. As the coordination-guarantees note emphasizes, different interaction modes need different protections; this source supports only the shared-state portion of a broader model. The moving `latest` URL is not a version pin; this report describes the captured observation.

## Recommended Next Action

Schedule a focused brainstorm to map the interactions meant by the occasion onto the read–prepare–validate–publish model, identifying which require guarantees beyond shared-state consistency before proposing a Commonplace-wide model.
