---
gate_id: sentence/concept-attribution
name: Concept attribution
description: 'The prose identifies a concept with one from a linked note, but the target defines or uses that concept differently.'
type: kb/types/review-gate.md
lens: sentence
watches: [body]
staleness: changed
---

## Failure mode

The prose claims that a concept in this note IS a concept from a linked note, but the linked note defines or discusses that concept differently. The reader who follows the link will find a mismatch between what the prose promised and what the target says.

## Test

For each sentence that identifies this note's concept with a concept from another note — phrases like "this is the X problem from [note]," "this is X in architectural form," "the same mechanism as [note]'s Y" — read the target note's treatment of that concept. Does the target's version match the identity claim?

Check up to 5 such identity claims. Report all mismatches.

An attribution is valid if the linked note's core concept supports the claim being made, even if the exact phrasing differs. Only flag when the linked note's treatment of the concept is substantively different — not merely when the vocabulary doesn't match verbatim.

## Example (fail)

"This is the return-value problem from the scoping note in architectural form" — but the scoping note's "return value problem" section discusses progressive typing of sub-agent returns, not trace leakage through implicit interfaces. The two problems are related but not the same.

## Example (pass)

"This is the scoping note's frame-boundary problem in architectural form" — and the scoping note does discuss frame boundaries as the place where isolation breaks down, matching the claim.
