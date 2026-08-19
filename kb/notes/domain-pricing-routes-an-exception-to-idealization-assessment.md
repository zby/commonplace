---
description: "Pricing signatures are defeasible, author-external evidence that a counterexample deserves idealization assessment; whether it refutes is settled by intended use, the omitted mechanism, consequence bounds, and explanatory dominance"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [document-system, failure-modes, kb-maintenance]
---

# Domain pricing routes an exception to idealization assessment but does not decide it

When counterexamples defeat a crisp claim, the standard repairs all weaken it: narrow the subject, reframe to what the evidence warrants, or delete. Physics routinely uses a fourth repair. The ideal-gas law is false of every real gas, yet it was kept as a first-order model — an idealization — with a stated regime and correction terms. An idealization concedes its counterexamples and remains a claim, so the question it raises is which observations still refute it. The answer has two stages that run on different evidence. **Domain pricing** — the domain's own practice already marks the exception as exceptional — is routing evidence: it shows the exception's special status was not invented by the claimant after criticism, and it earns the claim an idealization assessment. Whether the idealization survives that assessment is decided by adequacy evidence: what the model is for, what mechanism it omits, how large that mechanism's consequences are for the declared use, and whether the first-order account still carries most of the behaviour.

## What an idealization commits to

An idealization keeps the crisp first-order claim and adds commitments about its own exceptions. "First-order model" here means the deliberately simple account that is allowed to be wrong in detail — the ideal gas, the frictionless plane, the immutable class. The commitments are what keep the repaired claim refutable:

- **A declared use or regime.** What the model is for, and where it is meant to hold. Adequacy is judged against this, not in the abstract.
- **A named omitted mechanism.** What the exceptions are made of: molecular volume, intermolecular attraction, reflective class mutation.
- **A bound on the omitted mechanism's consequences** for the declared use.
- **Continued explanatory dominance.** Within the regime, the first-order account carries more of the behaviour than the corrections do.

Each commitment can be contradicted. Deviations that turn out to be erratic, unbounded, or dominant in the declared regime refute the idealization even after its first-order counterexamples are conceded. That is what separates an idealization from an immunized claim — an adjustment that makes refuting cases stop biting while risking nothing itself, the move Popper's critique of ad hoc rescue targets.

## Pricing is routing evidence against post-hoc immunization

An idealization could absorb any counterexample by calling it a correction, so the assessment needs evidence the claimant does not control. Domain pricing supplies it. Recurring signatures:

- **A marked separate interface.** The exception is reachable only through a reflection API, metaobject protocol, or escape hatch, not through the ordinary construct.
- **A pejorative or warning name.** The domain's own vocabulary — monkey-patching, hack, workaround — marks the practice as off the normal path.
- **A tooling or runtime charge.** Taking the exception costs something measurable: deoptimization, lost static checking, a slow path.
- **A governance ritual.** The exception requires ceremony the ordinary case does not: a changeset, a migration callback, a sign-off.
- **A rival organized around rejecting the ideal.** A competing school exists whose defining move is not making the commitment at all.

What the signatures establish is narrow: the exception's exceptional status was attested in the domain before this dispute, which blocks the immunizing move of labelling a counterexample an edge case after it lands. What they do not establish is everything else the assessment needs. A marked interface says nothing about how often the exception occurs or how much behaviour it carries. Temporal priority is not full independence, because a claimant can ship a deliberately marked escape hatch before criticism arrives. A governance ritual can mark an ordinary operation — routine deploys have sign-offs. A rival shows the commitment is real and contestable, and [only that: the test cuts one way](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md), so it cannot certify that departures are rare or bounded. And the signatures have no aggregation rule; several weak marks do not sum to a verdict. Pricing therefore opens an assessment and never closes one.

## Adequacy decides, and it is relative to the declared use

Two constructed cases fix the shape of the second stage.

A break-glass decryption path can be richly priced — marked interface, audit trail, ceremony — and still refute the guarantee "a non-administrator can never decrypt a production record." The guarantee quantifies over exactly the cases the pricing marks, so no amount of marking makes the exception negligible for that use. Routing succeeds, and the assessment still returns refuted, because the declared use tolerates no instances at all.

The same priced exception can pass one assessment and fail another. A schema migration that is marked, ritualized, and rare is negligible for a steady-state query model and decisive for a deployment-compatibility model. Nothing about the exception changed; the declared use did.

The converse holds too: an ordinary, unmarked deviation can be controlled and negligible for a declared use, and direct evidence of its bounds can support an idealization that pricing alone would never route. Pricing is neither sufficient nor necessary; it is the cheap, author-external first pass.

## The repository cases, reassessed

Two review passes in this repository defeated crisp claims and posed the idealization question.

In [instantiation alone cannot model agent learning across sessions](./instantiation-alone-cannot-model-agent-learning-across-sessions.md), premises about the fixed class fell to reflective counterexamples such as mutating `type(self)` from an instance method. The counterexample is priced — class mutation goes through a marked reflection interface — so the routing stage passes. The adequacy stage has not been run: how prevalent reflective mutation is, how much behaviour it carries in the systems the note reasons about, and what the declared use tolerates are not established, so the verdict is open until that assessment is made.

In [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md), the defeating cross-effect — a schema written to narrow the specification also steering the interpreter — is not marked by any practice in prompt engineering. Routing fails, no direct adequacy evidence exists either, and the reframe that pass chose stands.

Neither case shows pricing deciding anything. What both show is that the question needs an explicit place to be asked.

## Consequence for review workflows

Premise verdicts that classify truth — held, doubtful, defeated — are right to stay silent about repair: a false universal premise stays defeated even when the claim deserves to survive as an idealization. The gap sits one level up, in the repair dispositions. If no disposition can convert a defeated crisp claim into a declared idealization, the assessment has no place to run, and no one records its rejection as a decision either. The fix is not a pricing-gated acceptance: "holds as idealization, exceptions priced" would accept claims on routing evidence alone — an immunizing slot built into the workflow. The route worth adding is the assessment itself: pricing opens it, and a retained idealization carries an adequacy record — declared use, omitted mechanism, bound, dominance — that later passes can attack like any other content.

## Scope

The routing stage needs a domain with settled practice; a young or contested domain attests nothing, and there the assessment must start from direct adequacy evidence or not start at all. Which domain's practice counts is itself contestable — reflective mutation is condemned in ordinary application code and ordinary inside a metaprogramming framework — so a pricing argument must state the domain boundary it assumes rather than choosing the convenient one. The claim here is about the roles of evidence in the assessment, not about which repair wins a given case: narrowing, reframing, or deletion remains the honest repair wherever the adequacy commitments cannot be met.

## Open Questions

- What measures fit which uses? Frequency, effect magnitude, semantic reach, safety consequence, and explanatory share can rank the same exception differently, so the assessment needs the measure matched to the declared use rather than chosen freely. The class-instance case now supplies one instance: its declared use consumes the fence itself, so the exception's frequency is irrelevant there and the right measure is fence integrity — whether the exception stays marked.
- Does an idealization need scheduled re-testing? An exception that was marked and rare can become ordinary as the domain evolves, refuting the idealization without any new counterexample to the first-order model. One candidate mechanism: register the pricing attestations as tracked inputs to the claim's review state, so drift surfaces as staleness of a cited attestation.
- Does a passed assessment yield more than a verdict? In the class-instance case the pricing apparatus — the metaobject protocol, change-as-deployment rituals — supplied reusable design vocabulary for the analogous problem in the target domain. Whether the fence a domain builds around its exception is generally a candidate solution structure is untested beyond that one case.

---

Relevant Notes:

- [narrowing bought to survive review is paid for in content](./narrowing-bought-to-survive-review-is-paid-for-in-content.md) — contrasts: the narrowing escape runs to an analytic limit; idealization's degenerate limit is the immunized claim, and the adequacy commitments are its guard
- [generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — contrasts: the widening escape; each escape from counterexamples needs its own honest-versus-degenerate discriminator
- [title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — grounds: the maintenance frame this assessment sits inside, where the adequacy record is the exposed commitment surface a later pass attacks
- [formal systems assess explanatory-reach only through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — grounds: adequacy is judged relative to a declared model and use, not to surface marking, which is this note's second stage stated for formal assessment
- [methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — contrasts: idealization keeps unification in the generator layer instead of letting it migrate into methodology-shaped content
- [reach-assessment](./definitions/reach-assessment.md) — defined-in: the adequacy stage is a content-level reach-assessment, distinct from the pricing that only routes a candidate to it
- [theory warrant should be tracked at the finest granularity evidence licenses](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — grounds: its non-distribution rule is why evidence for exceptional status cannot silently become warrant for bounds, dominance, or adequacy over a declared use
- [repair dispositions for defeated claims are an epistemic policy with an option space](../reference/proposals/repair-dispositions-for-defeated-claims.md) — see-also: the Commonplace design surface that would turn the two-stage criterion into a keep-as-idealization disposition, gate, and freshness design
- [Metaobject Protocols: Why We Want Them and What Else They Can Do](../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.md) — evidenced-by: protocol entry points and explicit base/meta separation attest the marked-interface signature, without establishing prevalence or adequacy
- [Monkey patch](../sources/monkey-patch.md) — evidenced-by: the documented warning term attests the pejorative-name signature; the source is tertiary and records sanctioned uses too, so the inference stays community-relative
- [Fast properties in V8](../sources/fast-properties-in-v8.md) — evidenced-by: hidden classes, dictionary mode, and inline caches attest the runtime-charge signature when stable-shape assumptions break
- [Maps (Hidden Classes) in V8](../sources/maps-hidden-classes-in-v8.md) — evidenced-by: the field-constness trace supplies the concrete deoptimization mechanism behind the runtime charge
- [Release Handling](../sources/erlang-release-handling.md) — evidenced-by: versioned appup/relup plans, synchronized `code_change`, and rollback attest the governance-ritual signature, not the rarity or subordination of live definition change
- [SELF: The Power of Simplicity](../sources/self-the-power-of-simplicity.md) — evidenced-by: a rival organized around eliminating classes, attesting that the class commitment is real and contestable — the one-way half of the rival signature
