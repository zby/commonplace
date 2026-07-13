---
description: "General artifact freshness lives in commonplace-store.sqlite; review is the first target adapter over file-text inputs and review-pair targets"
type: ../types/adr.md
tags: []
status: accepted
---

# 052-General freshness store, review-first migration

**Status:** accepted  
**Date:** 2026-07-13  
**Supersedes in part:** [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md), [ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md)

## Context

Review freshness worked, but its tables and helpers were review-shaped: `review_file_snapshots`, review-only `freshness_baselines`, and compare/persist logic embedded in the review package. That blocked repository-wide status, generic accept/ack/retire over registered targets, and a second consumer without duplicating the mechanism.

[ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) established DB-owned snapshots and filesystem comparison. [ADR 043](./043-review-state-separates-completion-outcomes-and-freshness-baselines.md) separated completion, outcomes, and baselines. [ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) kept full-pass captures packet-owned. Collection-as-artifact freshness (`collection-text`, `collection-maintenance`) was explored in workshop but deferred to a follow-on proposal — not this ADR's implementation scope.

## Decision

The operational database is now `kb/reports/commonplace-store.sqlite` (`COMMONPLACE_STORE`). The retained `kb/reports/review-store.sqlite` is an immutable schema-v7 backup and migration source; commands refuse to create an empty new default while the old file still exists beside it.

One freshness mechanism owns:

- `artifact_snapshots` — path-keyed `file-text` versions with mandatory stored text;
- `freshness_baselines` — one current row per `(target_kind, target_key_json)` with monotonic `revision`;
- `freshness_inputs` — accepted input roles pointing at snapshot ids; and
- `review_freshness_evidence` — review-only bridge retaining the completed evidence pair for `review-pair` targets.

v1 admits only `file-text` inputs and `review-pair` targets. Review commands are adapters: they keep `missing-baseline` discovery, reason mapping (`criterion-changed` before `note-changed`), trivial ack, all-or-nothing finalization, evidence retention, and pruning. Global commands `commonplace-freshness-{status,accept,ack,retire}` operate over registered targets; generic accept rejects `review-pair` because capture refresh requires a completed pair id.

Two refresh paths remain distinct:

- **Capture refresh** — review finalization (`finalize_capture_refresh()`): job snapshots, CAS on `review_pairs.expected_baseline_revision`, evidence replaced.
- **Observation refresh/ack** — live revalidation against resolved file text; ack preserves review evidence.

Queued jobs record `expected_baseline_revision` at pair create. Finalization CASes the stored revision; stale capture after queue is `stale-baseline-revision` at runtime and `stale-queued-capture` at migration. Retirement (`commonplace-freshness-retire`) removes a registered baseline and cascades inputs plus review evidence without deleting jobs or historical result files.

`current_review_freshness_baselines` is a review adapter view over generic tables, not canonical state. Full-pass packet captures remain outside SQLite ([ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) unchanged).

Migration is source-to-destination via `scripts/migrate-review-db-v7-to-commonplace-store.py`: read-only v7 source, skip baselines whose paths no longer exist, fail queued jobs whose captures disagree with accepted inputs, preserve snapshot ids, verify projection parity, atomically install the destination, and re-hash the untouched backup.

## Consequences

Easier:

- one compare/persist substrate for review and future non-review targets;
- repository-wide freshness status with shared exit semantics;
- explicit retirement for relocated or deleted artifacts; and
- optimistic revision without file locks.

Harder:

- operators must migrate before the new code can use retained evidence on the default path;
- malformed registered baselines are store errors, never ordinary staleness; and
- collection-as-artifact targets remain unimplemented until proposal adoption.

## See also

- [Review system architecture](../review-architecture.md)
- [Proposal: collection-as-artifact freshness](../proposals/collection-as-artifact-freshness.md)