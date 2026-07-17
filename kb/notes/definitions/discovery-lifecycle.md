---
description: "Definition — the discovery lifecycle is the staged path by which an ampliative conjecture earns acceptance; the compound is technical, bare 'discovery' stays ordinary English"
type: kb/types/definition.md
tags: [learning-theory, discovery]
---

# Discovery lifecycle

The **discovery lifecycle** is the staged process by which an *ampliative* conjecture — a claim not entailed by the evidence in hand — becomes an accepted part of the knowledge base. The stages: observe an anomaly or repeated case without granting it authority; posit the conjecture; work out its testable consequences; test them against cases; accept the claim with a declared boundary and maintenance regime; and reintegrate prior evidence under the new concept. The staged view is not a Commonplace coinage — it borrows the Peircean cycle of abduction, deduction, and induction and the process/product distinction from the discovery literature. The term earns its keep by separating an *untested conjecture* from an *accepted discovery*: naming the stages lets an author say which one a given artifact has reached, rather than letting any ampliative sentence claim the finished status.

| Phase | Peircean analogue | KB operation |
|---|---|---|
| Observation / anomaly | surprising fact, repeated case, unexplained pattern | capture the case without granting rule authority |
| Conjecture | abduction | posit the candidate rule, mechanism, or general type — a claim not entailed by the evidence |
| Consequence derivation | deduction | work out what should be seen if the conjecture holds |
| Test / accumulation | induction | compare consequences with cases; gather support and rivals |
| Acceptance | gated commitment | accept the claim, declare its boundary, record its maintenance regime |
| Integration | evidence transport | reconnect prior evidence under the new concept; update affected artifacts |

## Scope

Use the compound when an artifact sits somewhere on this path and you need to say where. It is a term-boundary, not an operating manual: it fixes what "conjecture" versus "accepted discovery" asserts, not how to run an investigation.

**The routing rule.** Ampliative traffic enters the lifecycle at the *conjecture* stage. An untested generalization is a conjecture, never an accepted discovery — accepted status is reached later, through testing, and is not claimed by the ampliative sentence itself. This is operationally implemented by the discipline that [trace-extracted memory earns authority per operation, not at capture](../trace-extracted-memory-earns-authority-per-operation-not-at-capture.md): the abstract rung of that ladder *is* the conjecture step, and [boundary-statability](../abstract-an-experience-only-when-you-can-state-the-boundary.md) is the oracle that licenses the conjecture toward acceptance.

**Grading the conjecture's distance.** How far a conjecture reaches beyond its evidence is graded by Ord's [interpolation / extrapolation / hyperpolation](../../sources/interpolation-extrapolation-hyperpolation.md) triple:

- **interpolation** — output stays inside what the evidence already fixes; this is *not* a conjecture at all (see Exclusions).
- **extrapolation** — routine induction: the output extends along dimensions already present in the cases.
- **hyperpolation** — discovery proper: the output posits a new dimension, mechanism, or generative model.

The caveat is load-bearing: a knowledge base's claim space has no literal geometry, so there is no convex hull to be inside or outside of. The carving is qualitative — a borrowed depth vocabulary for how far a conjecture stretches, not a metric.

**The degenerate case.** The instant-insight picture — where [discovery is seeing the particular as an instance of the general](../discovery-is-seeing-the-particular-as-an-instance-of-the-general.md), the general concept and its known instances co-arising in one act — is the *degenerate* lifecycle: the evidence was already accumulated, so the observation, conjecture, and (apparent) acceptance stages collapse into a single moment. It sits at the deep, hyperpolation end, where a generative model and its instances appear together. The staged lifecycle is the general case; the co-arising insight is its limit where the phases telescope.

## Exclusions

- **Not every ampliative sentence is a discovery-lifecycle instance.** Interpolative content — claims recoverable from a source plus the declared consumer goal — is *derived*, not conjectured. Its home is the derived layer described in [theory and methodology form a two-layer execution system](../theory-and-methodology-form-a-two-layer-execution-system.md), and its lineage is carried by the `derived-from` / `Derived into:` labels in [link-vocabulary.md](../../reference/link-vocabulary.md), not by this term. A large change in form, register, or order with zero change in content stays derivation.
- **Bare "discovery" claims nothing technical.** The technical, staged sense rides only on the exact compound "discovery lifecycle" and its phase names. In ordinary prose "discovery" is plain English and asserts no stage, no authority, and no maintenance regime. This is the naming rule of [vocabulary collisions are prevented at write time, not resolved at read time](../vocabulary-collisions-prevented-at-write-time-not-read-time.md) applied: a multi-word coinage is greppable and collision-free where a captured common word is not.
- **Not the technique of investigation.** How to actually run observation, testing, or acceptance is the business of instructions, ADRs, and workflow notes; the definition only fixes when the compound applies and what using it asserts.

## Misuse Cases

- Calling an untested generalization "a discovery" as though it had reached acceptance. It is at the conjecture stage; the finished status is earned per test, not asserted by writing the sentence.
- Applying "discovery lifecycle" to a re-shaping that adds no claim beyond its source. That is derivation; routing it through the lifecycle grants it authority it never earned and hides its cheaper recomputable-copy maintenance regime.
- Loading the bare word "discovery" as if it carried the staged technical sense. Only the exact compound binds; the plain word does not.
- Treating the polation grades as coordinates in a real claim space. They are a qualitative depth vocabulary; there is no hull to compute membership in.

---

Relevant Notes:

- [discovery is seeing the particular as an instance of the general](../discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — degenerate case: the co-arising insight is the lifecycle with its phases telescoped, at the deep hyperpolation end
- [trace-extracted memory earns authority per operation, not at capture](../trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — operational implementation: the abstract rung is the conjecture step and authority is earned per test, not at capture
- [abstract an experience only when you can state where the lesson stops](../abstract-an-experience-only-when-you-can-state-the-boundary.md) — oracle: boundary-statability is the check that licenses a conjecture toward acceptance
- [theory and methodology form a two-layer execution system](../theory-and-methodology-form-a-two-layer-execution-system.md) — boundary: the derived side that interpolative content belongs to, distinct from conjectured content
- [vocabulary collisions are prevented at write time, not resolved at read time](../vocabulary-collisions-prevented-at-write-time-not-read-time.md) — naming rule: why the technical sense rides on the compound and bare "discovery" stays ordinary English
- [Interpolation, Extrapolation, Hyperpolation](../../sources/interpolation-extrapolation-hyperpolation.md) — source: grades the conjecture's distance from its evidence, with the no-literal-geometry caveat
- [link-vocabulary.md](../../reference/link-vocabulary.md) — boundary: the lineage labels that carry the derived/abstracted distinction the lifecycle routes into
- [Charles Sanders Peirce (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/peirce/) — external grounding: abduction, deduction, and induction as phases of inquiry
- [Scientific Discovery (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/scientific-discovery/) — external grounding: discovery as process versus product, and the hypothesis-generation / testable-consequence focus
