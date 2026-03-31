Key claims by section:

- **Motivation**: Context is scarce; bookkeeping and semantics have different error profiles.
- **Model**: Symbolic scheduler + bounded LLM calls. State K accumulates.
- **Select/call loop**: Formal loop with feasibility constraint.
- **Selection difficulty**: Sequential dependence, dual cost, framing matters.
- **Note-selection example**: Concrete instantiation.
- **SDK realization**: Compatible with ordinary SDKs; tool calling doesn't change architecture.
- **Scope**: No clean global optimization; supports local comparative results.

---

**Pairwise contradiction: none found**

- "The full global optimisation problem is probably too rich for clean strategy theorems" (scope) vs. the formal notation suggesting mathematical precision — consistent; the formalism supports local results, not global optimization.
- "Tool calling is not the threshold" vs. tool calling being "a useful inversion of control" — consistent; it's useful but architecturally neutral.
- "K accumulates over the loop" vs. "Whether the scheduler recomputes views on the fly or caches them is an implementation choice" — consistent; K's logical content accumulates, implementation varies.

**Definition drift: none observed**

K, select, call, M, ||P||_t — all formally defined and used consistently. The subscript t for task type is introduced with explicit notation and maintained.

No WARN, no INFO. Clean internal consistency for a formal note.
