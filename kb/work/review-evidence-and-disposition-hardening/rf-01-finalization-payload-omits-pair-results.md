# RF-01 — Finalization omits per-pair results from its return payload

**State:** open  
**Repair shape:** local API and test change  
**Severity:** medium

## Finding

Successful finalization returns job status and a completed-pair count, but not
each pair's result kind, outcome, or result path. The refreshed manifest carries
pair paths and display status but also omits outcomes. A parent that just
performed the work must issue a separate job-list query or inspect artifacts to
learn what happened.

## Evidence

- [`FinalizeReviewJobOutcome.to_payload()`](../../../src/commonplace/review/finalization.py) constructs only the job-level completion payload.
- [`manifest_payload()`](../../../src/commonplace/review/artifacts.py) serializes pair status and paths without outcomes.
- [The batch procedure](../../instructions/run-review-batches.md) verifies only that intended pairs are no longer stale.

## Why it matters

This omission makes an outcome easy to lose at the orchestration boundary. It is
not itself the missing `FAIL` disposition route in RF-02, but it makes that gap
harder to notice and forces every consumer to rediscover pair state.

## Provisional repair direction

Return a stable `pairs` array containing pair ID, note, criterion, result kind,
outcome, and derived result path. Keep SQLite canonical; the payload is an
immediate projection of committed state.

## Done when

- Successful verdict and report finalizations return every completed pair.
- Verdict entries include the canonical outcome; report entries make the lack
  of an outcome explicit.
- Failure and no-op payloads retain an unambiguous shape.
- CLI and library tests cover PASS, WARN, FAIL, and REPORT.
