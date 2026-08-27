# RF-11 — Acknowledgement is not bound to inspected input hashes

**State:** open  
**Repair shape:** CLI/API guard and tests  
**Severity:** high

## Finding

`commonplace-ack-review` checks the expected baseline revision, then snapshots
the note and criterion as they exist at command execution. It does not bind the
transition to the hashes the operator previously selected or inspected. A file
can change between inspection and acknowledgement and still be accepted.

## Evidence

- [`ack_pairs()`](../../../src/commonplace/review/acknowledgement.py) passes no
  selected input observations to the transition.
- [`ack_target_inputs()`](../../../src/commonplace/freshness/transitions.py)
  already supports `selected_inputs` and rejects a live-hash mismatch when they
  are supplied.
- [RF-10](./rf-10-joint-input-changes-are-compressed.md) shows how the preceding
  selector can also omit one changed input from the operator's view.

## Why it matters

Acknowledgement is the operation that extends old evidence to new bytes. Its
optimistic guard currently protects baseline state from concurrent transitions,
but not the inspected candidate from concurrent file edits.

## Provisional repair direction

Make the selector return explicit input observations or a bounded candidate
token. Require acknowledgement to submit those identities and use the existing
`selected_inputs` comparison before mutation.

## Done when

- Acknowledgement succeeds only for the exact note and criterion versions the
  caller selected.
- An intervening edit fails without advancing the baseline.
- The command can intentionally acknowledge only the changed input roles while
  preserving unchanged accepted snapshots.
- CLI tests cover the inspection-to-ack race.
