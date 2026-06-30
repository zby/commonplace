# Phase 8: Docs, ADR, and workshop close

**Status: planned.** Phase 8 promotes the durable decisions and closes the workshop after the queued-job pipeline behavior has landed.

## Purpose

Turn the implementation into durable reference knowledge and remove workshop scaffolding that should not become a permanent navigation surface.

## Scope

In scope:

- draft and promote the Phase 2+ ADR, likely ADR 034;
- record the queued-job pipeline, execution media, command surface, ack-provenance tightening, and no-relocation decision;
- mark the new ADR as superseding ADR 031 and extending ADR 029, ADR 030, and ADR 033;
- update `kb/reference/review-architecture.md`;
- update command reference docs;
- update operator docs and review-system docs;
- remove command wrappers that survived only as temporary bridges;
- remove or archive obsolete workshop files;
- close the workshop by promoting durable artifacts and deleting the work folder if no active design remains.

Out of scope:

- changing implementation behavior;
- adding new queue features;
- adopting the model partition registry proposal;
- adopting the content-hash/event-log source-of-truth alternative.

## ADR content

The ADR should record:

- review execution as a queued-job pipeline;
- two execution media: subprocess runner and orchestrator-driven agents;
- one job state machine over both media;
- selector JSON as the target handoff;
- job-owned prompt/output paths;
- the first-version simplification that keeps `model_partition` as freshness identity while concrete subprocess model is supplied at execution time and validated against the partition;
- the orchestrator-agent limitation that thinking effort is inherited from the parent/session or fixed subagent configuration, not dynamically requested per job;
- ack carrying forward existing review evidence;
- no automatic review relocation.

If acceptance provenance feels too large for the same ADR, split it into a sibling ADR rather than burying it in reference docs.

## Tests and validation

- full `pytest`;
- `commonplace-validate` on updated docs;
- command reference examples match actual CLI flags;
- no live docs describe removed command surfaces as current;
- workshop README points only to remaining active work, or the workshop is deleted.

## Done when

Phase 8 is done when the shipped system is described in durable reference docs and ADRs, old command surfaces are no longer documented as current, and the workshop has either closed or been reduced to explicitly remaining future work.
