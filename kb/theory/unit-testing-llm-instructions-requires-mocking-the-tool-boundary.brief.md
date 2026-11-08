---
type: types/write-brief.md
description: "Commission for the tool-boundary testing note: explain controlled execution through one generic example without documenting Commonplace's search stack."
---

# Brief: testing instructions at the tool boundary

## Intent

The operator commissioned this revision on 2026-11-08 during the frontier-work
reconsideration. Explain what tool mocking makes observable that checking a
final artifact alone would miss.

## Must keep

- One concrete, generic discovery-only example, with controlled search results
  and captured attempted writes.
- The limits of isolation and mock fidelity; mocking is not the only testing
  route.

## Must exclude

- Commonplace's tool inventory, search policy, or reasons for removing a search
  dependency. These are local details, not part of this claim.
- A test-harness design, unsupported fixture sizes, or generic testing advice
  added merely to expand the note.
