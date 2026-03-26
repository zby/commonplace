<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: semantic/completeness-boundary-cases
gate-hash: 053b48e685ea43922bddff685682f7d56447b657
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 83bf8f1a6ba444b8fc31203360327290a8b66d5e
recorded-at: 2026-03-26T20:40:46+01:00
-->
=== GATE REVIEW: semantic/completeness-boundary-cases ===

Framework tested: three-dimension taxonomy of the soft bound (volume, complexity, irrelevant context).

Boundary cases generated:

1. **Arrangement/positioning** (between items) — The lost-in-the-middle effect is grouped under volume, but arrangement can vary independently: same volume, same complexity, same irrelevant-context proportion, different ordering → different performance. The note acknowledges this implicitly ("arranged in a way the model couldn't effectively use" in the interactions closing) but does not account for it in the enumeration. Arrangement could be a fourth dimension or a cross-cutting modifier.

2. **Conflicting relevant context** (between items) — Two simple, relevant instructions that contradict each other degrade performance. Not volume (little added), not complexity (individually simple), not irrelevant (both relevant to the task). Could be forced under "complexity" (resolving contradictions requires extra work), but the fit is strained — the complexity section is about compositional depth and interpretation overhead, not logical conflict.

3. **Stale/outdated context** (adjacent concept) — Context that was relevant at an earlier point but is no longer. The "tokens that shouldn't be there" framing implicitly covers this as a species of irrelevant context. Clean fit.

4. **Partially relevant context** (adjacent concept) — Content mixing relevant and irrelevant information within the same passage. Handled as a combination of dimensions. Clean fit.

5. **Redundant relevant context** (extreme instance) — Same relevant content repeated many times. Pure volume increase with no irrelevant content and no added complexity. The volume dimension handles this. Clean fit.

WARN:
- (none)

INFO:
- Arrangement/positioning sits between the enumerated dimensions. The note acknowledges it implicitly but groups it under volume via the lost-in-the-middle citation, even though arrangement effects can vary independently of token count.
- Conflicting relevant context does not map cleanly to any single dimension. It can be forced under complexity but the fit is strained given the section's focus on compositional depth.

PASS:
- Stale context, partially relevant context, and redundant context all map cleanly into the framework.
- The three dimensions partition the primary evidence base correctly: ConvexBench → complexity, GSM-DC + web agents → irrelevant context, lost-in-the-middle + MECW → volume.

Overall: CLEAN (2 info)
===
