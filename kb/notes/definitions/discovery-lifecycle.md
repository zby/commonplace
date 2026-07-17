---
description: "Definition — the discovery lifecycle is a proposed six-phase evaluation of an ampliative conjecture; the compound is technical, bare 'discovery' stays ordinary English"
type: kb/types/definition.md
tags: [learning-theory, discovery]
---

# Discovery lifecycle

The **discovery lifecycle** is this note's proposed six-phase model for evaluating one *ampliative* conjecture — a claim not entailed by the evidence in hand — within a knowledge base. It tracks that candidate from the observation that motivates it through testing and, on a successful branch, integration. Its conjecture–consequence–test core adapts American philosopher Charles Sanders Peirce's cycle of abduction, deduction, and induction, while its distinction between inquiry in progress and accepted discovery draws on the discovery literature's process/product distinction. The complete sequence and its KB-operation mappings are this note's construction. The term lets an author state which phase an artifact has reached without letting an untested conjecture claim accepted status.

| Phase | Proposed Peircean analogue | KB operation |
|---|---|---|
| Observation / anomaly | surprising fact, repeated case, unexplained pattern | capture the case without granting rule authority |
| Conjecture | abduction | posit the candidate rule, mechanism, or general type — a claim not entailed by the evidence |
| Consequence derivation | deduction | state what should be observed if the conjecture holds and what would count against it |
| Test / accumulation | induction | compare those consequences with cases; gather support, counterevidence, and rival explanations |
| Acceptance | gated commitment on the successful branch | record that the evidence meets a named criterion for the claim's intended use; declare its boundary and maintenance regime |
| Integration | evidence transport on the successful branch | reconnect prior evidence under the new concept; update affected artifacts |

Testing, acceptance, and integration are different acts. Testing produces evidence about the stated consequences. Acceptance is the consuming workflow's recorded decision that this evidence meets its named criterion; without a named evaluator and criterion, the candidate remains under test or suspended. Integration then changes how the knowledge base organizes or uses the accepted claim. The lifecycle names these boundaries but does not supply one universal acceptance threshold.

From testing, acceptance proceeds to integration, revision returns to conjecture, suspension preserves candidate status while awaiting evidence, and rejection closes the candidate. Integration ends that lifecycle instance. Later counterevidence against an integrated claim opens a new instance at observation / anomaly; the prior acceptance remains part of the record rather than shielding the claim from reassessment.

## Scope

**The routing rule.** An artifact that advances an ampliative claim enters at the *conjecture* phase. An untested generalization never inherits accepted status from the sentence that states it. The recurring authoring decision this vocabulary supports is whether to retain and cite an artifact as a candidate or as an accepted rule. The conjecture phase's internal structure — its posit-and-recognize duality and its depth grading — is described in [conjecture is seeing the particular as an instance of the general](../conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md).

The linked [trace-extraction ladder](../trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) is a separate framework with different units. Its Abstract rung generalizes a fact that has already been verified, so the Abstract rung cannot be identified with this lifecycle's untested conjecture phase. A trace-learning workflow supplies concrete acceptance checks through the [validity and learning-value gates](../choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md): the rule must be trustworthy enough to learn from and worth retaining. [Boundary-statability](../abstract-an-experience-only-when-you-can-state-the-boundary.md) checks its scope within that application. This note therefore places a successfully abstracted trace rule closer to the acceptance branch, but those trace-promotion checks do not define acceptance for every discovery lifecycle.

**Polation is a separate direction analogy.** Philosopher Toby Ord's [taxonomy](../../sources/interpolation-extrapolation-hyperpolation.md) calls a query inside the convex hull (the region between observed inputs) interpolation. A query beyond that region but inside the affine hull (the dimensions spanned by those inputs) is extrapolation. A query outside those spanned dimensions is hyperpolation. Ord notes that all three can admit multiple non-canonical answers.

This note borrows only the qualitative direction: between known cases, beyond known cases along represented dimensions, or toward an unrepresented dimension, mechanism, or generative model. All three may be ampliative. A polation category says nothing about entailment or lifecycle status, and a knowledge base's claim space has no literal hull.

**Compressed cases do not skip testing.** In the [instant-insight picture](../conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md), prior evidence can make observation and conjecture appear simultaneous, but acceptance still requires that evidence to test the conjecture. Under the separate polation analogy, an instant-insight conjecture is hyperpolative only if it introduces an unrepresented dimension or generative model; that proposed mapping still needs worked cases.

## Exclusions

- **Entailed reshaping is not a discovery-lifecycle instance.** Content recoverable from a source plus the declared consumer goal is *derived*, not conjectured. This boundary is independent of the proposed polation analogy: interpolation can be ampliative, while a large change in form, register, or order with zero change in content can remain derivation.
- **Derived content has separate routing.** Its home is the derived layer described in [theory and methodology form a two-layer execution system](../theory-and-methodology-form-a-two-layer-execution-system.md).
- **Derived content has separate lineage.** The `derived-from` / `Derived into:` labels in [link-vocabulary.md](../../reference/link-vocabulary.md) carry that relationship; a discovery-lifecycle phase does not.
- **Bare "discovery" claims nothing technical.** The technical, staged sense rides only on the exact compound "discovery lifecycle" and its phase names. In ordinary prose "discovery" is plain English and asserts no stage, no authority, and no maintenance regime. This is the naming rule of [vocabulary collisions are prevented at write time, not resolved at read time](../vocabulary-collisions-prevented-at-write-time-not-read-time.md) applied: a multi-word coinage is greppable and collision-free where a captured common word is not.
- **Not the technique of investigation.** How to actually run observation, testing, or acceptance is the business of instructions, ADRs, and workflow notes; the definition only fixes when the compound applies and what using it asserts.

## Misuse Cases

- Calling an untested generalization "a discovery" as though it had reached acceptance. It is at the conjecture stage; the finished status is earned per test, not asserted by writing the sentence.
- Applying "discovery lifecycle" to a re-shaping that adds no claim beyond its source. That is derivation; routing it through the lifecycle hides the source lineage that governs its re-derivation or review.
- Loading the bare word "discovery" as if it carried the staged technical sense. Only the exact compound binds; the plain word does not.
- Treating the polation categories as coordinates or authority grades in a real claim space. There is no hull to compute, and no category determines whether an output is entailed or accepted.

---

Relevant Notes:

- [Charles Sanders Peirce (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/peirce/) — evidence: abduction, deduction, and induction as phases of inquiry
- [Scientific Discovery (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/scientific-discovery/) — evidence: discovery as process versus product, and the hypothesis-generation / testable-consequence focus
