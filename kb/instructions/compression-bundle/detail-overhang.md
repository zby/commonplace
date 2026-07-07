---
gate_id: compression/detail-overhang
name: Detail overhang
description: 'Examples, caveats, mechanisms, or background details outgrow their argumentative role.'
type: kb/types/review-gate.md
lens: compression
watches: [body]
staleness: changed
---

## Failure mode

An artifact includes detail whose kind is useful but whose amount is not. The example, caveat, mechanism, source gloss, or background explanation keeps elaborating after it has done its job. The issue is proportion, not relevance.

Bias this gate toward shortening. If a detail can do the same work as a phrase, sentence, or footnote-style aside, it should not occupy a paragraph or section.

Do not make the note skeletal. Some detail earns its space by giving the argument force rather than by adding a new premise. A fair opponent concession, a short source setup, or a vivid contrast can be necessary when removing it would make the answer feel like it is dodging the strongest version of the objection.

## Test

Find details that support the main claim, then ask whether their current length is proportional to the work they do.

Before flagging setup or source context, ask what argumentative job it performs:

- Does it carry a premise, boundary condition, counterexample, or inference step in the note's stated support route?
- Does it establish the opponent or source fairly enough that the response has force?
- Does it make the main contrast memorable without adding a second thesis?
- Would compressing it make the note technically shorter but rhetorically weaker or easier to dismiss?

Report **WARN** when a detail should be compressed in place.

Report **INFO** when the detail is probably long but may be needed for accessibility, grounding, or argumentative force.

Report **PASS** when the current detail length is necessary for the reader to understand, trust, remember, or apply the claim.

In output, report only details that need compression unless a non-obvious PASS prevents a likely false positive.

## Example (fail)

A note needs one example to show that a status label has operational consequences. It spends a full paragraph walking through every possible consequence and template branch. The example is relevant, but it has outgrown its role. Report WARN and recommend compression.

## Example (pass)

A note introduces an unfamiliar mechanism and gives a worked example because the mechanism cannot be understood from a name alone. The detail earns its space if deleting it would leave the claim abstract or unactionable.

A note answers a polemic. It spends a short opening paragraph conceding the polemic's strongest point before making its own distinction. The concession does not add a new mechanism, but it prevents straw-manning and makes the answer credible. Do not flag it merely because the central claim could be stated without it.
