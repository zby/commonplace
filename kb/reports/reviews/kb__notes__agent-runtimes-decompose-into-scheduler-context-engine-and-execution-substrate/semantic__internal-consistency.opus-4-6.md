Key claims by section:

- **Intro**: Three separable components (scheduler, context engine, execution substrate). "The functions are analytically distinct."
- **Why the split matters**: Eliminates recurring confusions. Each component maps to existing KB theory.
- **Practitioner mapping**: Six practitioner components → three runtime components.
- **Scheduler**: Formalized by bounded-context orchestration model.
- **Context engine**: Formalized by context engineering (routing, loading, scoping, maintenance).
- **Execution substrate**: Persistent state, tool execution, safety boundaries. Both scheduler and context engine depend on it.
- **Convergence**: Three independent sources emphasize different parts of the same decomposition.
- **Scope limits**: "A decomposition, not a claim that these three components are the only ones that matter."

---

**Pairwise contradiction: none found**

- "The functions are analytically distinct" (intro) vs. "Not every system exposes these as neat modules; in many real systems the boundaries blur" (intro) — consistent. Analytical distinction ≠ implementation separation.
- "Both the scheduler and context engine depend on exact external state" (substrate section) vs. the substrate being described as a peer component rather than a foundation — the text says both depend on the substrate but the decomposition doesn't impose a layered hierarchy. Consistent but could be clearer. INFO — the dependency relationship (scheduler and context engine depend on substrate) implies substrate is foundational, yet the three are presented as peers. This is a representational choice, not a contradiction — the dependency exists but doesn't make the decomposition hierarchical for other purposes.
- "A decomposition, not a claim that these three components are the only ones that matter" (scope limits) is consistent with the open treatment throughout.

**Definition drift: none observed**

"Scheduler," "context engine," "execution substrate" are each defined once with clear one-sentence questions and used consistently. "Memory" is distinguished from context-engine decisions explicitly. No drift.

**Summary/body check**

No compressed summary section. The scope limits section functions as a closing qualification that accurately reflects the body's hedged claims. ✓

One INFO on the dependency-vs-peer tension in component presentation. No WARN, no contradiction, no drift.
