---
gate_id: complexity/claim-to-section-ratio
name: Claim-to-section ratio
description: 'The note has more sections than distinct non-obvious claims, so sections restate rather than extend the argument.'
type: kb/types/review-gate.md
lens: complexity
watches: [body]
staleness: changed
---

## Failure mode

The note has more sections than distinct non-obvious claims, so sections restate rather than extend the argument.

## Test

List the distinct non-obvious claims, then count sections. Treat support sections as justified only when they carry boundary conditions, failure cases, or inference steps that need separate treatment for the note's stated argument. If sections outnumber the claims plus those separately necessary support units, identify which sections are repeating framing instead of adding new substance.
