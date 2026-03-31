## prose/proportion-mismatch

**Result: WARN**

The note's core claim (per title and description) is the two-phenomena distinction and the spec-to-program projection model. Approximate section sizes:

| Section | Lines | Role |
|---|---|---|
| Two Distinct Phenomena + subsection | ~15 | Core: introduces the distinction |
| Spec-to-Program Projection + example | ~20 | Core: formalizes the model |
| Narrowing the Interpretation Space | ~10 | Application |
| Boundaries | ~15 | Application |
| **Constraining and Relaxing** + 3 subsections | **~40** | Application / downstream |
| Testing and Debugging | ~8 | Application |
| Design Implications | ~10 | Summary |

The **Constraining and Relaxing** section is the longest in the note (~40 lines including "Why constrain?", "One-shot vs progressive constraining", and "Relaxing as extension"), yet it is downstream of the core framework. The "Why constrain?" subsection alone (cost/latency/reliability) is practical guidance that doesn't advance the two-phenomena argument — it motivates constraining as a practice, which is useful but secondary.

The description does not mention constraining/relaxing at all, reinforcing that it's application material rather than the note's thesis.

Consider whether "Constraining and Relaxing" should be thinned (moving the "Why constrain?" rationale to the linked [codification](./definitions/codification.md) note) or promoted into the description if it's meant to carry equal weight.
