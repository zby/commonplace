# Review freshness decoupling workshop

## Purpose

Prepare the current review system for the broader lineage work by fixing two concrete couplings first:

1. review freshness must not depend on Git;
2. review freshness selection must be separate from batch/run execution.

This workshop is a prerequisite for `kb/work/lineage-mechanisms/` and the first concrete slice of the more universal lineage system. The lineage workshop should not generalize from review until review itself has a clean boundary between "what needs attention" and "how a refresh is run."

## Scope

In scope:

- current review subsystem only;
- notes and review gates as KB markdown files identified by path;
- SQLite review store;
- accepted baselines, snapshots, selector reasons, ack, and full-review acceptance;
- the dependency direction between freshness code and batch/runner code.

Out of scope:

- generic lineage tables;
- source, report, or external repository lineage;
- package asset modeling beyond what review gates need later;
- runner adapters, prompt protocol, parsing, or batch-packing redesign;
- making review state shared between users.

## Working Hypothesis

The minimal stable boundary is:

- freshness owns snapshots, accepted baselines, stale/missing target selection, ack, and full-review acceptance;
- execution owns run creation, prompt rendering, runner invocation, batch grouping, ingest, and readable review artifacts.

Freshness should be callable by any execution strategy. Execution should not be encoded into freshness state.

The universal part is intentionally small: a target keyed by file-path inputs plus a partition, accepted input snapshots in SQLite, and a selector that emits refresh targets. Review supplies the first implementation of that shape without committing the rest of Commonplace to review-specific tables or gate shorthands.

## Closure Conditions

Close this workshop when it produces:

- a minimal schema/API design for DB-owned review input snapshots;
- a selector-vs-runner boundary for the current review subsystem;
- a migration plan away from Git blob/commit baselines;
- a scoped implementation plan that can be executed without solving general lineage.

## Working Files

- [minimal-review-snapshot-design.md](./minimal-review-snapshot-design.md) - current-review-only design for DB-owned note/gate snapshots and freshness/execution separation.
- [review-snapshot-and-rationalization-plan.md](./review-snapshot-and-rationalization-plan.md) - stopped-operation cutover plan to land the design plus the review-subsystem rationalization (dead-state cleanup, immutable declared `model_partition`, finished migration runner); backfill consumes legacy baselines before the legacy fields are dropped.
