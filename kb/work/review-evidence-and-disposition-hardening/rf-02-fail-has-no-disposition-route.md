# RF-02 — FAIL has no consequential disposition route

**State:** open  
**Repair shape:** disposition-lifecycle design plus implementation  
**Severity:** high  
**Related:** [RF-01](./rf-01-finalization-payload-omits-pair-results.md), [RF-03](./rf-03-report-results-have-no-handling-route.md)

## Finding

A `FAIL` completes normally, establishes a freshness baseline, and is omitted
from later stale selection. The standard warning/fix path consumes WARN only.
Job-list can expose the stored outcome, but no normal route turns `FAIL` into the
downstream disposition work promised by the gate contract.

## Evidence

- [The gate contract](../../types/review-gate.md) calls FAIL an escalation signal
  and says verdicts generate fix, reject, or defer work.
- [`record_and_finalize_job()`](../../../src/commonplace/review/finalization.py)
  treats FAIL as successful verdict completion.
- [`scan_reviews()`](../../../src/commonplace/review/warn_selector.py) is the
  standard fix queue and has no dedicated FAIL branch.
- The intervention in [the evidence boundary](./evidence-boundary.md) observed a
  fresh, completed FAIL absent from both stale selection and warn selection.

## Why it matters

Freshness means input applicability, not approval. Using freshness as the only
batch-completion check nevertheless hides the most severe verdict from the
normal workflow.

## Provisional repair direction

Represent handling separately from freshness. A dedicated or unified
disposition selector should return every unresolved FAIL until an operator
records fix, reject, or defer. This need not make FAIL a merge blocker.

## Done when

- A finalized FAIL is returned by the normal batch handoff and a documented
  disposition selector.
- It remains visible until an explicit disposition event resolves it.
- Freshness selection remains about input change and does not become an outcome
  queue by accident.
- End-to-end tests cover finalize, select, disposition, and resolution.
