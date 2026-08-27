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

**Amended by:** [ADR 065](./065-publish-only-supported-freshness-transitions.md) — generic accept was withdrawn until an end-to-end non-review target is adopted

## Context

Review freshness worked, but its snapshot and baseline tables and its compare/persist logic were review-shaped and embedded in the review package. That blocked repository-wide status, generic accept/ack/retire over registered targets, and a second consumer without duplicating the mechanism.

[ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) established DB-owned snapshots and filesystem comparison; [ADR 043](./043-review-state-separates-completion-outcomes-and-freshness-baselines.md) separated completion, outcomes, and baselines; [ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) kept full-pass captures packet-owned. Collection-as-artifact freshness was deferred to a follow-on proposal.

## Decision

The operational database is `kb/reports/commonplace-store.sqlite` (`COMMONPLACE_STORE`).

One freshness mechanism owns path-keyed `file-text` artifact snapshots with mandatory stored text; one current baseline per registered target with a monotonic revision; accepted input roles pointing at snapshots; and a review-only bridge retaining the completed evidence pair for `review-pair` targets.

v1 admits only `file-text` inputs and `review-pair` targets. Review commands are adapters: they keep `missing-baseline` discovery, role-labelled change mapping, trivial ack, all-or-nothing finalization, evidence retention, and pruning. When both registered inputs change, the review selector retains both observations rather than prioritizing one reason. Global commands `commonplace-freshness-{status,ack,retire}` operate over registered targets. Review finalization owns initial acceptance and replacement because capture refresh requires a completed pair id. No generic initial-acceptance or refresh transition ships ([ADR 065](./065-publish-only-supported-freshness-transitions.md)).

Two baseline-update paths remain distinct:

- **Capture refresh** — review finalization: job snapshots, a compare-and-swap on the pair's expected baseline revision, evidence replaced.
- **Observation ack** — live revalidation against resolved file text; ack preserves review evidence for an existing baseline.

Queued jobs record the expected baseline revision at pair creation; finalization compares-and-swaps it, and a capture that went stale after queueing is a distinct runtime reason. Retirement removes a registered baseline and cascades inputs plus review evidence without deleting jobs or historical result files.

The review freshness view is a review adapter over the generic tables, not canonical state. Full-pass packet captures remain outside SQLite ([ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) unchanged).

## Consequences

Easier:

- one compare/persist substrate for review and future non-review targets;
- repository-wide freshness status with shared exit semantics;
- explicit retirement for relocated or deleted artifacts; and
- optimistic revision without file locks.

Harder:

- malformed registered baselines are store errors, never ordinary staleness; and
- collection-as-artifact targets remain unimplemented until proposal adoption.

## See also

- [Review system architecture](../review-architecture.md)
- [ADR 065: Publish only supported freshness transitions](./065-publish-only-supported-freshness-transitions.md)
- [Proposal: collection-as-artifact freshness](../proposals/collection-as-artifact-freshness.md)
