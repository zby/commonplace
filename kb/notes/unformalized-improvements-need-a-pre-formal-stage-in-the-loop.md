---
description: "A proof gate cannot admit unformalized candidates; upstream translation relocates the criticism needed to settle their concepts, while cheaper formalization shortens that stage only after those concepts stabilize"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, self-improving-systems, constraining]
---

# Reaching unformalized improvements needs a pre-formal stage somewhere in the loop

A [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) has two known limits: evaluation cannot select a candidate search never generates, and [acceptance is warranted only for candidates the oracle can discriminate](./warranted-autonomy-is-bounded-by-oracle-domain.md). A third concerns the [representational form](./definitions/representational-form.md) in which any stage can inspect a candidate. An improvement whose concepts are not yet fixed enough to formalize is reachable only if some stage can criticize, revise, and reject it before it has a formal representation. Where that stage sits is an architectural choice; that it exists is not.

The claim concerns externally interpreted theories about a system or its domain, read by a person or a language model. It excludes prose that binds the system through a procedure, audit, or contract.

## A Gödel machine has a warrant limit and an admission limit

[The Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), the proof-gated limiting case, excludes candidates in two distinct ways. A rewrite may be fully expressed as a program while no proof under the fixed axioms shows that switching to it beats continuing the search: a warrant limit, which better proof search or a different axiomatization can move. And a prose conjecture — "the failures come from an unrepresented shared resource" — is not an unproved member of the candidate space; the machine searches over programs and proofs, so it is not a candidate at all: an admission limit, which stronger proof search does not touch.

## Translation relocates the stage; it does not remove it

A formal-only gate can receive a prose-born improvement once something upstream formalizes it, so the gate's language bounds direct submission, not the reach of the loop. But formalizing an unsettled concept is not transcription. The translator must decide what the prose commits to, resolve ambiguity, choose a boundary, and often revise the claim — pre-formal criticism, relocated upstream. And the gate cannot discharge the resulting correspondence obligation with the check it applies to the surrogate: a proof establishes consequences within a formalization, not that the formalization preserves the source theory. A prose-reading gate and an upstream prose translator are two placements of one stage. A Gödel machine contains neither.

## What the stage does, and what makes it cheap

In the stage a theory is a **prototype**: explicit enough to criticize and revise, with no operational machinery bound to its commitments. A language-capable critic can challenge a premise, narrow a scope, or derive a discriminating test without a build step; running the test may still need an experiment or deployment. Because the premises are explicit, [reflection can target a retained commitment directly](./reflection-makes-retained-lessons-second-order.md), and [theory-mediated learning can operate on the theory as a theory](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md). Once the concepts stabilize, the part a formal consumer needs is [codified](./definitions/codification.md) into a schema, validator, test, or formal model while the rest stays reopenable. Many theories never leave: no formal consumer needs them, formalizing them is infeasible in practice, or their content may not be formalizable at all. The note does not estimate that residue.

The medium does not make rejection cheap; authority, downstream coupling, sunk work, and rollback cost do. Nonbinding prose can motivate months of building, and a low-authority formal sketch can stay disposable. What natural language contributes is narrower: it exposes unsettled commitments before a faithful formalization exists. Codifying before that point [freezes one projection of the theory](./progressive-constraining-commits-only-after-patterns-stabilize.md) and [raises replacement cost toward entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md).

## The relaxed Gödel machine

Commonplace has this shape, and the arrangement can be named a **relaxed Gödel machine**: a Gödel-shaped reflective loop with a pre-formal stage added. Candidates enter as natural-language theories, are criticized and revised there, and their stabilized parts harden into deterministic machinery — [one worked pathway records a design decision criticized as prose and later codified into a schema and validator](./evidence/commonplace-as-a-reflective-system.md). The name marks the added stage only. It asserts no optimality property, and accepted changes must still become operative.

The stage changes the warrant target. A proof warrants entailment within a formalization; criticism judges whether the formalization's premises fit their setting, bounded by the critic's oracle domain. A proof gate can miss an unproved improvement or accept a valid change built on a false world-facing premise; a criticism gate can accept a bad change, [after which the error becomes operative and can compound](./false-positive-generation-is-filtered-before-retention.md). The choice turns on the warrant required, the cost of each error, and how many candidates can be formalized at all.

## Failure in the world reopens concepts, not only parameters

Suppose a retained theory attributes scheduler failures to demand exceeding fixed capacity. It becomes a capacity model plus a proof that the implementation respects it. Deployment still fails, because another process consumes the same resource. The proof is intact — [it warrants entailment from its premises, not the interpretation that supplied them](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — and the world-facing premise was wrong.

If capacity is already a model parameter, a runtime trace can revise its value and trigger a new proof without prose. But "capacity depends on what another process is doing" changes the concept, not its value. A precise revision can be made directly in the symbolic model; an unsettled one must be stated, criticized, and bounded before a new model is built. This is [the codify-and-relax trajectory](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) at the level of theories, where relaxing reopens a concept rather than swapping a component. Two external cases keep a formalization and its fit apart: [Eigenius](../agentic-systems/eigenius.md), an agent-operated execution substrate, checks Lean proof terms but treats correspondence to the claim as a separate conditional check; [DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), a counterfactual-physics benchmark, scores a law's prose explanation and its Python implementation separately and finds predictive accuracy does not guarantee a strong explanation.

## Cheap formalization shortens the stage for settled concepts

Formalization cost has parts — translating concepts into a model, building the artifact, generating a proof, checking it — and when the last three fall, formal models enter the prototype stage earlier and rival specifications become easy to compare. For a settled concept, cheap translation may carry a candidate into a formal gate with no interval in prose. For an unsettled one the bottleneck is elsewhere: deciding what the premise commits to, and obtaining evidence that the model fits the world. Cheap formalization thus defeats the cost argument for natural language without removing the stage, because it is the concepts, not the cost, that are unsettled. The durable claim defends a stage, not prose, [as scaffolding recurs at the deployment frontier while earlier scaffolding is absorbed](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md). How much of a loop's candidate space is unsettled at any time is an empirical question.

## Open Questions

- When do two representations preserve enough consequences to count as the same candidate, so that a translator has moved rather than replaced it?
- Can a loop tell, from inside, a concept that cannot be formalized from one that is merely not yet understood or too costly to formalize?
- Can a natural-language stage bound its own false-acceptance rate mechanically, or does formalizing the criticism protocol reintroduce the admission limit one level up?

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the loop and its search-range limit, to which this note adds where unformalized candidates are worked on
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: oracle domain bounds which admitted candidates can be warranted; this note bounds which candidates can be worked on at all
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the limiting case with a warrant limit stated and an admission limit by construction
- [Commonplace as a reflective self-improving system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: a criticism-gated loop whose stabilized decisions were codified into a schema and validator
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: the pathway the pre-formal stage runs, which a formal-only gate cannot run
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: the codify-and-relax trajectory for operations, applied here to theories where relaxing reopens a concept
- [Causal and proof obligations are two formal routes to assessing explanatory-reach](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — grounds: what a codified theory's proof establishes and the translation it leaves unchecked
- [The bitter-lesson defense portfolio has one load-bearing member for the form-only rebuttal](./the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) — context: classifies this note as the answer to the separate cheap-formalization objection
