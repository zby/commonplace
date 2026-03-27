---
gate_id: semantic/grounding-alignment
name: Grounding alignment
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

The note cites sources or linked notes as if they ground a claim more directly or more broadly than they actually do.

## Test

For the central causal claims and conclusions:

1. Read the linked source or note, following at most 5 links.
2. Check attribution accuracy for vocabulary mismatch and scope mismatch.
3. Check domain coverage across the whole note, not just quote-level accuracy.
4. Check whether the conclusion actually follows from the cited evidence.

Report WARN for scope overreach or invalid inference. Report INFO for plausible but not airtight inferences.
