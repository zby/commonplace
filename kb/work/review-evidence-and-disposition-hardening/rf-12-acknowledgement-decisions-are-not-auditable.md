# RF-12 — Acknowledgement decisions are not auditable

**State:** open  
**Repair shape:** event/provenance design and schema change  
**Severity:** medium  
**Related:** [RF-11](./rf-11-acknowledgement-is-not-bound-to-inspected-inputs.md)

## Finding

After acknowledgement, retained state shows the current accepted snapshots,
revision, time, and preserved evidence pair. It does not retain that the change
was an acknowledgement rather than a rereview, who or what authorized it, the
reason, or the inspected candidate hashes.

## Evidence

- [`freshness_baselines` and `freshness_inputs`](../../../src/commonplace/store-schema.sql)
  retain only current state.
- [`ack_target_inputs()`](../../../src/commonplace/freshness/transitions.py)
  replaces the accepted input state without writing an acknowledgement event.
- [`ack_pairs()`](../../../src/commonplace/review/acknowledgement.py) accepts no
  actor or rationale.

## Why it matters

An old evidence pair can acquire a wider applicability history that cannot be
reconstructed. When a later failure appears, the operator cannot distinguish a
bad review from an over-broad acknowledgement or determine why the latter was
considered safe.

## Provisional repair direction

Retain a transition event containing target identity, previous and new input
snapshots, prior and new revision, transition kind, timestamp, caller identity
when available, and a short required rationale or classified reason. Keep the
current-baseline tables optimized for current state.

## Done when

- Current state can be traced through rereview, manual ack, automatic trivial
  ack, and retirement transitions.
- The event binds the exact inspected hashes from RF-11.
- Status or a dedicated history command exposes the transition without making
  history part of ordinary selection context.
