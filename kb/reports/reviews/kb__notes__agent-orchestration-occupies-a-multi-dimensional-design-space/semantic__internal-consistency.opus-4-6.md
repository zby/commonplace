Key claims by section:

- **Intro**: Single-axis taxonomies collapse independent choices. The better picture is a multi-dimensional design space.
- **Five dimensions**: Scheduler placement, persistence horizon, coordination form, coordination guarantee, boundary-return artifact.
- **Why this matters**: Multi-dimensional framing explains why single-axis taxonomies break. Slate and forking as examples.
- **Closing**: "Should stay an open map, not a closed classification. The current dimensions are salient, not final."

---

**Pairwise contradiction: none found**

- "Separable dimensions" (intro) vs. open question "Which dimensions interact, and which vary independently?" (why this matters) — consistent. "Separable" means they can be independently varied in principle; "interact" means they may constrain each other in practice. The note doesn't claim full orthogonality.
- "Current dimensions are salient, not final" (closing) vs. the detailed treatment of exactly five dimensions — consistent. The note presents a specific set while explicitly leaving it open to revision.

**Definition drift: none observed**

Each dimension is introduced with a bolded name and a clear one-sentence question (e.g., "Where the scheduler lives," "How long orchestration knowledge persists"). These definitions are used consistently throughout. No term shifts meaning.

**INFO — coordination guarantee is partially derivative**

Coordination guarantee is presented as an independent dimension alongside coordination form. However, the note says "The form of coordination does not tell you whether the architecture is safe" — which argues for the separation. But the three guarantee families (isolation, consistency, adjudication) are each associated with specific composition modes (flat context, shared state, output aggregation), which are themselves related to coordination forms. INFO — the guarantee dimension is conceptually distinct but operationally coupled to coordination form. The note handles this by citing the coordination-guarantees note, which provides the detailed argument. The coupling doesn't create a contradiction but might lead a reader to question whether guarantee should be a sub-dimension of form rather than a peer dimension.

**No summary/body mismatch** — no compressed summary section. The "Why this matters" section accurately restates the core thesis with examples.

One INFO on form/guarantee coupling. No WARN, no contradiction, no drift.
