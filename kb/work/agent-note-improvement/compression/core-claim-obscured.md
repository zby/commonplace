---
gate_id: compression/core-claim-obscured
name: Core claim obscured
description: 'The strongest claim is present, but supporting apparatus makes it hard to find or remember.'
type: kb/types/review-gate.md
lens: compression
watches: [body]
staleness: changed
---

## Failure mode

The note contains a strong claim, but the reader has to dig through setup, caveats, analogies, terminology, or related-note machinery to find it. The support may be individually defensible, but the artifact's shape hides the sentence that should be doing the work.

This gate is about reader uptake. If the main claim is not easy to state after reading the note once, the note is carrying too much apparatus in front of or around it.

## Test

State the note's strongest claim in one sentence, using only commitments the artifact actually makes. Then check whether the note itself makes that sentence prominent early and keeps later material subordinate to it.

If the reviewer can infer a stronger or cleaner claim than the note states, report that separately as a possible revision target. Do not optimize the note around a reconstructed claim that the current artifact does not support.

Report **WARN** when the core claim should be moved earlier, restated more plainly, or protected by cutting/folding surrounding apparatus.

Report **INFO** when the claim is findable but the note's shape makes it less memorable than it should be.

Report **PASS** when the note's structure makes the core claim easy to find and later material clearly serves it.

In output, focus on the obscuring material and the simplest way to restore the main claim's prominence.

## Example (fail)

A note's strongest claim is that a checked redundant copy is sometimes better than a single source of truth. The note opens with terminology, several analogies, and caveats before saying that plainly. Report WARN and recommend moving the core claim earlier or compressing the setup.

## Example (pass)

A note opens with its central claim, then uses definitions, examples, and caveats in the order needed to support that claim. The apparatus does not hide what the note is for.
