Key claims by section:

- **Two phenomena**: Semantic underspecification (property of spec language) vs. execution indeterminism (property of engine). "Fundamentally different in kind."
- **Indeterminism obscures**: People attribute variation to randomness, avoiding the harder spec-language question.
- **Projection model**: Spec → choose interpretation → execute. LLM performs projection, not compilation.
- **Narrowing**: System prompts, few-shot, schemas, temperature. "The line between disambiguating the spec and biasing the engine is rarely clean."
- **Boundaries**: LLM components have both phenomena, code has neither. Boundaries are checkpoints.
- **Constraining/relaxing**: Spectrum from underspecified to precise. Progressive constraining recommended.
- **Testing/debugging**: Different challenges per phenomenon. "Retry vs. rewrite the spec."
- **Design implications**: Seven points.

---

**Pairwise contradiction: none found**

- "The two are not entirely orthogonal" (intro) vs. treating them as separable throughout — consistent. The note says they're "fundamentally different in kind" while acknowledging interaction ("indeterminism is the mechanism by which different interpretations get surfaced across runs"). Different in kind ≠ fully independent.
- "Temperature is often cited as purely an indeterminism control, but it's subtler" (narrowing) vs. "Execution indeterminism... largely eliminable via temperature=0" (intro) — consistent. The intro says indeterminism is largely eliminable; the narrowing section adds that temperature also affects which interpretation surfaces. These are compatible: lowering temperature reduces variation but doesn't ensure the right interpretation.
- "Natural language specs remain underspecified even under maximum constraint" (narrowing) vs. the constraining section's description of moving to precise semantics — consistent. Constraining moves individual components to precise semantics; the system as a whole retains underspecified components for open-ended tasks.

**Definition drift: none observed**

"Underspecification," "indeterminism," "projection," "constraining," "relaxing," "boundary" — all used consistently across all sections. The terminology is introduced carefully and maintained throughout.

**Seven design implications check**

Each implication traces to a specific section: (1) boundaries section, (2) constraining section, (3) narrowing section, (4) narrowing section, (5) constraining section, (6) projection model, (7) constraining section. All are consistent with their source arguments.

No WARN, no INFO. Clean internal consistency.
