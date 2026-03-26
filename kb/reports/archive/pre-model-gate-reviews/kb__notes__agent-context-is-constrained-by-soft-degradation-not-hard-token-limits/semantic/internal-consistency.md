<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: semantic/internal-consistency
gate-hash: 9076e845827408a541d23168e69701e8a66d2969
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 83bf8f1a6ba444b8fc31203360327290a8b66d5e
recorded-at: 2026-03-26T20:40:47+01:00
-->
=== GATE REVIEW: semantic/internal-consistency ===

Key claims extracted per section and checked for pairwise contradiction, definition drift, and summary/body mismatch.

WARN:
- (none)

INFO:
- [Definition drift, minor] The opening uses "soft degradation curve" (line 11, singular) while the body develops the soft bound as a three-dimensional surface. "Curve" is used metaphorically in the opening and the body never contradicts it, but a reader encountering "curve" first may expect a single-variable relationship rather than the three-dimension framework that follows.

PASS:
- "Two bounds" (hard vs soft) and "three dimensions" (of the soft bound) are distinct concepts used consistently — no conflation.
- "Complexity" is used consistently throughout to mean compositional/interpretive difficulty (the ConvexBench sense), not general difficulty. The irrelevant-context section does not blur into complexity claims.
- "Irrelevant context" is defined implicitly as "tokens that shouldn't be there" and used consistently. The interactions section properly distinguishes established findings from untested conjectures about irrelevant context.
- The "distinguishable but not fully separable" framing in the interactions section is consistent with treating the dimensions as separate sections while acknowledging overlaps.
- The description ("silent degradation across three dimensions") faithfully represents the body's structure and central claim.
- The consequences section follows from the body's premises without introducing new claims or contradicting earlier sections.

Overall: CLEAN (1 info)
===
