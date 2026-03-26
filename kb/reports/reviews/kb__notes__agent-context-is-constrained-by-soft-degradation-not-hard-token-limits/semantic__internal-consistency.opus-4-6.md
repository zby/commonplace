<!-- GATE-REVIEW
note-path: kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
gate-id: semantic/internal-consistency
model: opus-4.6
gate-hash: 9076e845827408a541d23168e69701e8a66d2969
recorded-commit: b34b33c12f7199564136b76b6124efb69f6be91b
watched-hash: 2bb82ffde2f8ccb2643ff41fb89d22b79519c0b2
recorded-at: 2026-03-26T23:07:14+01:00
-->
## Internal consistency review

### Key claims extracted

1. **Opening**: The soft bound is the binding constraint; performance degrades before the hard limit.
2. **Volume**: More tokens dilute attention. Irrelevant context is "particularly damaging."
3. **Complexity**: Interpretation overhead is proportional to context complexity.
4. **Open questions**: Volume and complexity are "distinguishable but not fully separable." Irrelevant context "may be an independent dimension."
5. **Invisible**: The soft bound is not a single number; it shifts with task type, depth, arrangement, framing, and model version.
6. **Consequences**: Silent degradation makes heuristic design rational (not a placeholder). Programmatic constructability is the genuine advantage, creating "high control over inputs, low observability of effective processing."

### Pairwise contradiction check

**Volume/Complexity separation vs "not fully separable."** The note presents Volume and Complexity as separate sections with distinct evidence, then says they are "distinguishable but not fully separable." No contradiction — the structure distinguishes them, and the open-questions section explicitly limits the claimed separation. Consistent.

**"The soft bound" (singular concept) vs "not a single number" (multi-dimensional).** The note uses "the soft bound" throughout as a unifying concept, while saying it is a multi-dimensional surface. The note resolves this by describing a "soft degradation surface" — singular concept, multi-dimensional realization. Consistent.

**"Heuristic design rational, not a placeholder" vs the implicit possibility of future measurement.** The note says these heuristics are "the rational strategy, not a placeholder until better measurement arrives." The body supports this: if the bound is invisible and task-dependent, heuristics are permanently needed, not temporary. Consistent.

### Definition drift check

- "Soft bound" / "soft degradation": used consistently as performance degradation below the hard token limit.
- "Volume" and "complexity": stable meanings throughout (token count vs compositional depth).
- "Irrelevant context": consistently means context tokens unrelated to the task at hand.
- "Binding constraint": used once in the opening, reprised implicitly in consequences. Stable.

### Summary/body mismatch check

The `description` field says: "The binding constraint on agent context is silent degradation across multiple dimensions (volume, complexity, possibly irrelevant context), not the hard token limit providers advertise." This accurately reflects the body's structure: two named dimensions, one candidate third, the invisibility property, and the contrast with hard limits. No mismatch.

The title ("Agent context is constrained by soft degradation, not hard token limits") accurately captures the core claim. No mismatch.

### Findings

**INFO — Irrelevant context placed under Volume but flagged as possibly independent.** The Volume section discusses irrelevant context at length, and the Open Questions section asks whether it is an independent dimension. This creates a structural tension: the reader encounters irrelevant context as a Volume sub-topic, then is told it might not belong there. This is not a contradiction — the note is transparent about the ambiguity — but the placement could mislead a reader who stops at the Volume section. Consider a brief forward-reference from the Volume section to the Open Questions discussion, or restructuring so irrelevant context gets its own subsection parallel to Volume and Complexity.
