# S1 outcome — Remove the snapshot mutation exception

**State:** resolved 2026-08-23.

## Outcome

[ADR 072](../../../reference/adr/072-ingests-own-source-authority-and-snapshots-are-local.md)
superseded ADR 045's field placement instead of implementing this plan's
one-field exception. The tracked ingest now owns durable `genre`. A local
snapshot may contain a provisional capture-time genre, but ingestion records
its closer-reading classification on the report and never edits the snapshot.

This is a stronger boundary than the planned captured-content envelope:
snapshots are whole-file immutable after capture, and `snapshot_sha256` covers
the exact bytes that grounded the ingest. The source collection, both source
types, and `cp-skill-ingest` agree that snapshotting may create the ignored
reading copy while ingestion writes only the tracked report.

## Acceptance evidence

- The ingest schema requires `genre` and `snapshot_sha256`; the snapshot schema
  makes `genre` optional.
- `cp-skill-ingest` copies no snapshot genre, asks the drafting worker to set
  genre after reading, and verifies that the snapshot checksum is unchanged
  across the handoff.
- Exact recapture, checksum mismatch, and absent-material behavior are covered
  by the snapshot resolver tests without any ingest or snapshot rewrite.
- I3 retains one follow-through obligation: its future installed sources
  template must project this resolved contract.
