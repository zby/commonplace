---
description: "Why prototype standing tracks operational binding rather than representational form: prose leaves consequences interpretive, symbols give encoded choices formal semantics, and either form can remain exploratory or become costly to revise"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining, self-improving-systems]
---

# Representational form does not determine whether a theory is a prototype

A theory — [an account whose premises, mechanism, consequences, and scope can be inspected and revised as named parts](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — has prototype standing while its commitments remain cheap to revise or reject because little operational machinery depends on their current version. This is a lifecycle standing, not an epistemic status. An accepted theory can remain a prototype, while a conjecture can become entrenched before it earns acceptance.

*Prototype* is an engineering gloss here, not new canonical vocabulary. It means a build kept cheap to revise while its commitments are still being tested. It does not mean the clone-once contract text of a collection prototype or an exemplar that stands for a category. A rejected theory is no longer a prototype because its claim has been retracted. A surviving theory can retain prototype standing in either natural-language or symbolic form.

Representational form does not decide this standing. [Representational form](./definitions/representational-form.md) is how retained content is encoded and consumed. Natural language leaves consequences to interpretation. [Codification](./definitions/codification.md) crosses into a symbolic artifact whose formal consumer assigns consequences to the encoded choices. Although this increases semantic determinacy, it does not by itself establish adoption, downstream dependency, or rollback cost. An authoritative prose theory can bind training, audits, policies, and decisions. A scratch formal model can remain disposable.

## Form changes interpretation; binding changes revision cost

Natural language allows direct criticism before every operational detail has been fixed. A language-capable agent can inspect a theory, derive a test, and revise a premise without first translating the account into a formal language. The cost is interpretation at each use: different readings can assign different consequences.

Symbolic form fixes how a formal consumer treats the choices actually encoded. It can still leave a range open through parameters, nondeterminism, or quantification. Codification gives that range formal semantics; it need not select one concrete value for every unresolved choice.

Neither interpretive openness nor formal semantic determinacy determines how far a revision propagates. Revision remains local only while consumers are loosely coupled to the current version. A natural-language theory embedded in an approved safety case may require coordinated changes to procedures, training, and certification. A formal model used only to explore a candidate can be discarded without migration. [Entrenchment begins when replacement stops being cheap](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md), regardless of medium.

## When codification becomes attractive

Among theories with comparable downstream coupling, pressure to codify tends to rise with invocation frequency and the cost of a wrong reading, and to fall with volatility. This is a prevalence claim, not a definition. A finding that working systems, under otherwise similar conditions, preferentially formalize rare, volatile, cheap-to-misread theories over frequent, stable, expensive-to-misread ones would count against it.

Formalization cost is a bundle rather than a single quantity. Translating concepts into a model, constructing the artifact, generating a proof, and checking a supplied proof can become cheaper or more expensive independently. Cheaper proof checking does not make the translation of unsettled concepts cheap. Any comparison must identify which cost changed and which consumer benefits.

Codification often accompanies stronger commitment because formally assigned consequences make an artifact easier for validators, executables, and other components to consume. Adding those consumers can increase rollback cost. The causal step, however, is the added binding rather than symbolic form itself. A formal artifact used only for early exploration can remain cheap to discard, while prematurely adopting either prose or a symbolic artifact as operative makes being wrong expensive.

## Codification and acceptance are independent

The [discovery lifecycle](./definitions/discovery-lifecycle.md) is the staged path by which a conjecture is developed, tested, accepted, and integrated. Codification changes representation; it is not itself an epistemic decision. A theory can be formalized before acceptance so that rival models expose different consequences. It can also be accepted for a use that needs no formal consumer and remain in prose.

The normative condition is narrower: a codified artifact should become operative authority only after the theory has been accepted for the scope that the artifact commits. This is a warrant rule, not part of the definition of codification. [Exact implementation of a requirement does not show that the requirement fits its objective](./exact-implementation-does-not-validate-a-requirement.md), so executable success cannot substitute for acceptance.

Prototype standing must be assessed at the grain to which consumers bind. If one premise becomes an operative checked invariant while the rest of the account remains loosely coupled, that premise can lose prototype standing while the remainder retains it. Partial codification may expose component boundaries, but it creates mixed lifecycle standing only when operational binding differs across components.

## Formal checking moves, but does not erase, interpretation

Verification-oriented codification can produce a formal model and obligations such as a theorem, invariant, type property, model-checking condition, or test suite. Other codifications may produce only an executable rule; obligations are not constitutive of the form change. Where obligations exist, proof or exhaustive checking can establish that a translated consequence holds throughout the model. [That warrants entailment from the formal assumptions, not that the variables, domain, and assumptions represent the external claim](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md). For externally interpreted theories, codification relocates interpretation to the translation and correspondence boundary rather than eliminating it.

Suppose a theory attributes scheduler failures to demand exceeding a fixed capacity. A model encodes that capacity, and a proof shows that admitted demand never exceeds it. Deployment can still fail because another process consumes the resource. The proof remains valid for the model; the world-facing capacity premise was wrong.

One repair path reopens the concepts in prose, adds the missing premise, and then codifies a revised model. Another revises the symbolic model directly because the relevant concepts are already precise there. Returning a theory to prose is one theory-level extension of the [codify-and-relax trajectory](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), but it is neither the only meaning of relaxing nor a required response to failure.

Two external cases make the correspondence boundary concrete. [Eigenius](../agentic-systems/eigenius.md), an agent-operated typed execution and verification substrate, checks supplied proof terms in Lean, a proof-assistant language, against an allowlisted axiom set. Its reviewed code treats correspondence to a graph claim as a separate conditional check; proof validity alone does not establish faithful encoding. [DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), an interactive benchmark built from simulated counterfactual physics worlds, asks agents for both a natural-language explanation and a Python implementation of a discovered law. Strong predictive accuracy does not guarantee a strong conceptual explanation. In both cases, the representations remain separate objects to assess.

Purely formal theories mark the boundary of this argument. When natural language is only an informal presentation of an authoritative formal definition, no model-to-world observational claim need remain. The correspondence argument applies to empirical and otherwise externally interpreted theories, not to every formalization.

## Cheap formalization changes the prototype loop

If machine assistance reduces artifact-construction, proof-generation, or checking costs, more candidates can be expressed symbolically before anyone adopts them. Formal models then become experiments within the prototype phase. A theory may move repeatedly between prose and symbols, or be revised entirely within symbolic form, while its operational coupling remains low.

For externally interpreted theories, cheaper in-model checking can make translation and world correspondence a larger share of the remaining uncertainty. It does not show that translation itself became cheaper, that uncertainty must concentrate there, or that prose is the only medium in which concepts can be revised. Cheap formalization removes one reason to defer symbolic experiments; it does not remove the lifecycle need for cheap rejection and revision.

This is a conditional mechanism, not a measured prevalence trend. It predicts a change only where formalization cost was the bottleneck. It makes no prediction about theories whose concepts remain infeasible to formalize, whose content may not be formalizable, or whose intended consumers gain no value from formally assigned consequences.

## Scope

- *Theory* retains the inspectable-parts sense stated in the opening. Procedures, records, and descriptions of state have different retirement conditions; a procedure is superseded rather than refuted.
- *Cheap* and *local* are relative to named consumers and dependencies. Where neither prose nor a symbolic artifact has consumers, both can be cheap to discard.
- Prototype standing is component-relative when consumers bind at different grains. Partial codification can expose those grains, but it creates mixed lifecycle standing only when binding differs across them.
- Rejection retracts the claim. Revision and suspension preserve a surviving claim's prototype standing only while its operational coupling remains low.
- The model-to-world boundary applies to empirical or otherwise externally interpreted theories. Purely formal theories can terminate the interpretive chain in an authoritative formal definition.
- The argument covers natural-language and symbolic forms. It does not decide whether absorption into distributed-parametric form is another form change or a different lifecycle event.

## Open Questions

- Which observable dependency and rollback costs distinguish a prototype from an adopted or entrenched theory?
- How should a system inventory prose authorities whose operational coupling is real but not machine-readable?
- When consumers bind to partially codified theories at different grains, which grain should a review or acceptance decision target?
- Can theories that are not yet understood be distinguished operationally from theories that cannot be formalized?

---

Relevant Notes:

- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](./superseded-choices-are-retained-superseded-beliefs-are-not.md) — extends: explains what the rejection exit implies for retaining or removing the artifact
- [Selective revision needs a faithful rationale, not just a legible one](./selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — contrasts: cheap editing does not guarantee that a revision targets the premise that failed
- [Treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) — extends: places this two-form theory path inside a three-form learning frame
- [The bitter-lesson defense portfolio has one load-bearing member for the form-only rebuttal](./the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) — extends: locates cheap formalization as an objection to permanent form, not to a prototype function
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — contrasts: a fixed proof gate excludes unformalized candidates without making every formal candidate operative
