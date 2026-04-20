---
type: kb/types/instruction.md
description: Workshop review gate for checking completeness boundary cases during review-revise experiments
gate_id: semantic/completeness-boundary-cases
name: Completeness and boundary cases
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

An enumeration, framework, or taxonomy claims to cover a space but leaves out edge cases or breaks when tested against the boundaries of its own scope.

## Test

For each enumeration or framework:

1. Find its grounding definition, either from a cited source or from the note's own framing.
2. Generate 3-5 boundary cases:
   - the simplest instance
   - the most extreme instance
   - cases between enumerated items
   - adjacent concepts near the stated boundary
3. Test whether each case maps cleanly into the framework.

WARN when a case clearly falls outside the claimed coverage. INFO when coverage is possible but strained.

Before recommending expansion, check whether the taxonomy's weight is justified. If the taxonomy is already longer than its argumentative role warrants, the right fix may be compression or scope clarification rather than adding another category.
