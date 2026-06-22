# Workshop: review-run-lifecycle

## Question

How should the review system represent the lifecycle of a review run so that all execution paths produce the same correct data for:

- run status
- requested gate set
- model partition
- telemetry
- gate reviews
- acceptance events

## Why this workshop exists

The system now has multiple live ways to produce review data:

- split agent path via `create_review_run`
- split bundle path via `record_bundle_review`
- nested runner path via `run_review_bundle`
- batched nested runner path via `run_gate_sweep`

They do not all produce the same data. In particular:

- some paths create `review_runs` rows before any execution starts
- some paths treat `status='running'` as "prepared but not launched"
- some paths capture telemetry and actual model partitions
- some paths never capture telemetry at all
- `run_review_bundle --dry-run` persists a real `review_runs` row even though no review happens

This workshop is about tightening that lifecycle so the data model reflects what actually happened rather than which script happened to be used.

## Scope

This workshop is about the **review run lifecycle**, not the whole review subsystem:

- how runs are created
- how execution starts
- how telemetry is attached
- how gate reviews are written
- how completion/failure is finalized
- which module should own those transitions

It is not a redesign of:

- gate definitions
- selector freshness rules
- acceptance semantics
- the general note-writing workflow

## Current grounding

- [review-runs-direct-write](../review-runs-direct-write/README.md) — introduced the parent `review_runs` model and direct-write framing
- [review system](../../reference/REVIEW-SYSTEM.md) — current workflow contract and user-facing commands
- [run review bundle on note](../../instructions/run-review-bundle-on-note.md) — current split agent workflow
- [review-architecture.md](../../reference/review-architecture.md) — code architecture overview

## Working direction

Centralize lifecycle transitions into ~3 functions without adding schema complexity:

- scripts become thin CLI frontends over shared lifecycle functions
- telemetry attachment and model rekeying happen in one place
- no new statuses, no typed state machines, no schema splits
- Path 2 (split bundled) removed; repair script deletion deferred to follow-up
- dry-run persistence is fixed as a standalone bug

## Files in this workshop

- [design.md](./design.md) — proposed reorganization around a central lifecycle library

## Design constraints

1. Split gate-by-gate agent execution must remain supported.
2. The same logical review should produce the same DB shape regardless of command path.
3. A dry run must not leave behind a fake live review run.
4. Acceptance should remain a finalization step, not something each write path advances independently.
5. No new schema complexity (statuses, column splits) unless a concrete consumer needs it.
