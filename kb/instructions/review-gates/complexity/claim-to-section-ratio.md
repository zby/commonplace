---
gate_id: complexity/claim-to-section-ratio
name: Claim-to-section ratio
description: 'The note has more sections than distinct non-obvious claims, so sections restate rather than extend the argument.'
type: types/review-gate.md
lens: complexity
watches: [body]
staleness: changed
---

## Failure mode

The note has more sections than distinct non-obvious claims, so sections restate rather than extend the argument.

## Test

List the distinct non-obvious claims, then count sections. Treat support sections as justified only when they carry boundary conditions, failure cases, or inference steps that need separate treatment for the note's stated argument. If sections outnumber the claims plus those separately necessary support units, identify which sections are repeating framing instead of adding new substance.

---

Relevant Notes:

- [Short composable notes maximize combinatorial discovery](../../../theory/short-composable-notes-maximize-combinatorial-discovery.md) — rests-on: sections should track distinct claims because short single-claim notes are what co-loading composes
- [A note is an atomic step relative to the check that reads it](../../../theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — rests-on: a note is bounded by one claim the reader can hold and one inference the checker can verify
