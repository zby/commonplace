---
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
