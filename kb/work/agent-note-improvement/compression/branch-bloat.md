---
gate_id: compression/branch-bloat
name: Branch bloat
description: 'A note carries side claims that may be interesting, but they compete with or weaken the main claim instead of supporting it.'
type: kb/types/review-gate.md
lens: compression
watches: [body]
staleness: changed
---

## Failure mode

A note accumulates branch ideas: analogies, hypotheses, predictions, related mechanisms, or future extensions that are not needed for the main claim. The branch may be plausible and worth preserving somewhere, but in this note it dilutes the argument, creates extra attack surface, or makes the central point harder to see.

Bias this gate toward protecting the main note. Do not keep a branch in place merely because it is interesting.

## Test

Identify the main claim the note should preserve, using the artifact's own commitments. Then ask which parts would still belong if the note had to make only that claim well.

Before flagging a branch, check whether it supplies a premise, boundary condition, counterexample, source setup, opponent concession, or trust-building contrast needed by the note's stated argument. Do not remove a branch merely because the main conclusion still sounds plausible without it.

Report **WARN** when a branch should be removed, demoted to an open question, or rehomed as a separate note/workshop lead.

Report **INFO** when a branch may be useful but its destination is unclear.

Report **PASS** when side material directly strengthens the main claim in its current place.

In output, focus on branches that need action. Do not list every supporting paragraph as PASS.

## Example (fail)

A note argues that LLM generation can hide a dropped reasoning constraint. It then adds a speculative analogy to hallucination and a prediction about future artifact rates. Both are interesting, but each needs different evidence and distracts from the witness/relaxation mechanism. Report WARN and recommend deletion, open-question demotion, or a separate note.

## Example (pass)

A note argues that LLM generation can hide a dropped reasoning constraint, then adds one compact contrast with code tests to bound where the mechanism weakens. The contrast directly limits the main claim and prevents overuse, so it stays.
