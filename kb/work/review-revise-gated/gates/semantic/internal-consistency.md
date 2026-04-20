---
type: kb/types/instruction.md
description: Workshop review gate for checking internal consistency during review-revise experiments
gate_id: semantic/internal-consistency
name: Internal consistency
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

Different parts of the note contradict each other, shift definitions, or compress tensions away in the summary.

## Test

Extract the key claims from each section, then check:

- pairwise contradiction
- definition drift
- summary/body mismatch when a compressed summary is present

WARN on contradiction. INFO on ambiguity or likely drift that needs human confirmation.
