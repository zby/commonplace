# RF-03 — Report results have no standard handling route

**State:** open  
**Repair shape:** disposition-lifecycle design  
**Severity:** medium  
**Related:** [RF-02](./rf-02-fail-has-no-disposition-route.md)

## Finding

A report-kind assay completes without an outcome, becomes fresh, and retains its
body in a result file. No standard selector or batch handoff returns fresh but
unhandled reports. The documentation correctly distinguishes freshness from
handling, but the operational route for the latter is missing.

## Evidence

- [The review-system guide](../../reference/README-REVIEW-SYSTEM.md) says report
  completion has no outcome and freshness does not mean findings were handled.
- [`finalize_review_job()`](../../../src/commonplace/review/finalization.py)
  completes report pairs and advances their baselines.
- The registered warning selector handles verdict findings, not report bodies.

## Why it matters

A successful critique can consume model work and become permanently skipped
without its findings reaching an operator. This is a delivery gap, not a claim
that reports should acquire verdict outcomes.

## Provisional repair direction

Give reports the same separate handling lifecycle proposed for RF-02 while
preserving their outcome-free protocol. The queue item should carry the report
body, evidence pair, and an explicit handled/deferred state.

## Done when

- A completed report appears in a documented handling selector.
- Handling does not invent PASS/WARN/FAIL semantics for report-kind results.
- Supersession and retirement define what happens to an unresolved report.
- Tests cover report completion, queueing, disposition, and supersession.
