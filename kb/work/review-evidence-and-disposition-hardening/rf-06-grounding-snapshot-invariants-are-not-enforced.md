# RF-06 — Grounding snapshot invariants are not enforced

**State:** open  
**Repair shape:** deterministic preflight and tests  
**Severity:** high

## Finding

The grounding criterion requires the derived snapshot's exact SHA-256 and
canonical `source` to match the linked ingest. Runtime preparation checks only
that the derived path exists, is readable, and is a regular file. Finalization
checks output protocol, not the source invariant.

## Evidence

- [The grounding gate](../../instructions/review-gates/semantic/grounding-alignment.md)
  states the exact hash and source requirements.
- [`_target_size()` and snapshot resolution](../../../src/commonplace/review/job_prompt.py)
  perform only filesystem availability checks.
- The invalid-snapshot intervention in
  [the evidence boundary](./evidence-boundary.md) still finalized and became
  fresh when supplied model-shaped PASS output.

## Why it matters

A deterministic integrity invariant is being delegated to an uncalibrated
semantic reviewer without any proof that it ran. The persisted completion state
therefore cannot establish that the named source bytes were checked.

## Provisional repair direction

Move hash and canonical-source equality into deterministic job preflight. Decide
whether a mismatch prevents job creation or produces a machine-authored FAIL;
do not let model prose override the check. Retain the verified snapshot identity
with the pair.

## Done when

- Missing, mismatched-hash, and mismatched-source snapshots cannot become a
  fresh PASS through finalization.
- Valid snapshots expose the exact verified path and hash to the worker and
  retained evidence.
- Tests cover all failure modes without launching a model.
