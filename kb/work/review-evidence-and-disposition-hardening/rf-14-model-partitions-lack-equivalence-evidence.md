# RF-14 — Model partitions lack equivalence evidence

**State:** open  
**Repair shape:** conservative identity policy plus calibration  
**Severity:** medium

## Finding

The partition registry aliases multiple model generations and reasoning efforts
to one freshness identity. The mapping is mechanically tested, but no inspected
calibration evidence establishes that the grouped configurations make equivalent
review judgments. Concrete model and effort provenance may also be absent.

## Evidence

- [`MODEL_PARTITION_REGISTRY`](../../../src/commonplace/review/review_model.py)
  groups several GPT-5 variants under `codex` and all listed Luna/Sol efforts
  under their family partition.
- Finalization validates concrete model/effort only when the parent supplies it.
- [The calibration proposal](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)
  treats model partition as part of the judgment configuration but supplies no
  equivalence result for the current aliases.

## Why it matters

A result from an older or lower-effort configuration can satisfy freshness for a
newer or higher-effort request. The registry silently turns an unmeasured quality
claim into identity policy.

## Provisional repair direction

Use exact model plus effort as the default evidence identity. Introduce a coarse
partition only after a labelled calibration demonstrates the intended
equivalence, and version the partition policy so later registry changes can
reselect affected evidence.

## Done when

- Every finalized job has sufficient concrete provenance for its identity rule.
- Each alias group cites an accepted calibration result and equivalence criterion.
- Changing a partition definition cannot silently reinterpret existing baselines.
