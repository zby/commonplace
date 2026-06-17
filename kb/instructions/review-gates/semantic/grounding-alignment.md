---
gate_id: semantic/grounding-alignment
name: Grounding alignment
description: 'The note cites sources or linked notes as if they ground a claim more directly or more broadly than they actually do.'
type: kb/types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

The note cites sources or linked notes as if they ground a claim more directly or more broadly than they actually do.

## Test

For the central causal claims and conclusions:

1. Extract the route the note itself gives: the claim, the cited evidence, and the stated or implied inference from evidence to claim.
2. Read the linked source or note, following at most 5 links.
3. Check attribution accuracy for vocabulary mismatch and scope mismatch.
4. Check domain coverage across the whole note, not just quote-level accuracy.
5. Check whether the note's stated route supports the conclusion. Do not substitute a better argument, outside evidence, or a reconstruction that only reaches a similar conclusion.

Report WARN for scope overreach or invalid inference. Report INFO for plausible but not airtight inferences.
