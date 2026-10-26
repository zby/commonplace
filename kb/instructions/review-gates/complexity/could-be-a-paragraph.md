---
gate_id: complexity/could-be-a-paragraph
name: Could be a paragraph
description: 'After removing background and connections, the note reduces to a single simple insight that does not justify a multi-section structure.'
type: types/review-gate.md
lens: complexity
watches: [body]
staleness: changed
---

## Failure mode

After removing background and connections, the note reduces to a single simple insight that does not justify a multi-section structure.

## Test

Rewrite the note mentally as one paragraph. If no non-obvious claim, support path, boundary case, failure condition, or load-bearing inference is lost, the note is over-complex for its actual content.

This is the strongest complexity signal because it means the section structure itself is probably unnecessary.

---

Relevant Notes:

- [Short composable notes maximize combinatorial discovery](../../../theory/short-composable-notes-maximize-combinatorial-discovery.md) — rests-on: one insight per note is the unit the library composes; a multi-section wrapper around one insight adds reading cost without a second claim
