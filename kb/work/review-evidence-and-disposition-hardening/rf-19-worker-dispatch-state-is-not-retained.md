# RF-19 — Worker dispatch and attempt state are not retained

**State:** open  
**Repair shape:** orchestration-boundary decision  
**Severity:** medium

## Finding

The store knows `queued`, `completed`, and `failed`, but not whether a queued job
was dispatched, which worker attempt owns it, when it started, whether it was
cancelled, or whether a retry supersedes an earlier attempt. The documented
parent owns scheduling and dispatch bookkeeping, but Commonplace exposes no
retained contract for that bookkeeping.

## Evidence

- [`review_jobs`](../../../src/commonplace/store-schema.sql) admits only the three
  terminal/queue states and no attempt table.
- [The batch procedure](../../instructions/run-review-batches.md) assigns launch,
  lifecycle, and scheduling to the parent harness.
- Registered review implementation contains no worker launch or attempt API.

## Why it matters

After interruption, a later parent cannot distinguish undispatched work from a
running, abandoned, or duplicated attempt. This matters more once RF-15 exposes
partial request state or jobs are executed outside one uninterrupted session.

## Provisional repair direction

First decide ownership. If Commonplace promises resumable batch operation, add
attempt identity, dispatch/start/finish events, lease or abandonment semantics,
and retry/cancel commands. If the harness owns this entirely, narrow the
Commonplace procedure and provide a precise handoff schema the harness must
retain.

## Done when

- Every queued job has a documented recovery classification after parent loss.
- Duplicate workers cannot both finalize without a visible attempt conflict.
- Retry and cancellation behavior are explicit and tested at the chosen owner.
