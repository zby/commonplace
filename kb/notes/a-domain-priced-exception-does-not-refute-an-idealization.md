---
description: "Idealization is a fourth repair for a defeated crisp claim, and its honesty test is whether the domain itself already prices the exception — via a marked interface, pejorative name, runtime charge, governance ritual, or rival paradigm"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, failure-modes, kb-maintenance]
---

# A domain-priced exception does not refute an idealization

When counterexamples defeat a crisp claim, three repairs are standard: narrow the subject until the counterexamples fall outside it, reframe to whatever the evidence still warrants, or delete. Physics routinely uses a fourth. The ideal-gas law is false of every real gas and the frictionless plane exists nowhere, yet neither was narrowed to the cases that obey it nor reframed into a checklist of pressure-dependent tendencies. Both were kept as declared first-order models with a stated validity domain and correction terms of their own. That is idealization, and the question it raises is which observations still count as refuters. The answer proposed here is a criterion about the domain rather than about the claimant: an exception fails to refute an idealization when the domain's own practice already prices it, and an exception the domain treats as ordinary unmarked practice still refutes.

## Idealization is a distinct repair, not a soft version of keeping

The three standard repairs each give up something specific. **Narrowing** keeps the claim crisp and gives up range; its characteristic failure is running to the analytic limit, since [narrowing bought to survive review is paid for in content](./narrowing-bought-to-survive-review-is-paid-for-in-content.md). **Reframing** keeps range and gives up crispness: "each remedy acts on exactly one object" becomes "these are three diagnostic questions with different primary targets" — true, useful, and no longer a generator. The crisp version predicted, for a remedy nobody had catalogued yet, where it would and would not act; the reframed version files remedies after someone has worked that out. **Deletion** gives up both.

Idealization keeps range and crispness together and pays somewhere else. An idealization's content has two levels: what the first-order model forbids inside its declared domain, and what the claim asserts about its own exceptions — that they are marked rather than ordinary, bounded rather than open-ended, and subordinate rather than dominant. The second level is what keeps the claim refutable after the first-order counterexamples are conceded. The ideal-gas law survives its refutation because finite molecular volume and intermolecular attraction produce corrections you can write down, measure, and bound in the declared regime. A model whose deviations were erratic, unbounded, or larger than the effect being modelled would be refuted as an idealization, not merely bounded by one.

This is the Lakatosian correction that anomalies are not automatically refutations, applied to claim maintenance rather than to research programmes. It is not an exemption from criticism. What changes is which observations count as refuters, and the criterion below is what stops the change from becoming what Popper attacked as an immunizing stratagem: an adjustment that makes the refuting case stop biting while risking nothing itself.

## The test: is the exception priced by the domain, independently of the claim?

An idealization can absorb any counterexample by calling it a correction, so it needs a discriminator that the claimant does not control. Physics supplies one form of it — the correction is written as a term in an equation with a measurable size — but that form is not available in every domain. The general form is that the domain's own practice already treats the exception as exceptional, in ways attested before anyone raised it against the claim. Recurring signatures of that pricing:

- **A marked separate interface.** The exception is reachable only through a reflection API, metaobject protocol, unsafe block, or escape hatch, rather than through the ordinary construct.
- **A pejorative or warning name.** The domain calls it monkey-patching, a hack, a workaround — its own vocabulary marks it as off the normal path.
- **A tooling or runtime charge.** Taking the exception costs something measurable: deoptimization, cache invalidation, lost static checking, a slow path.
- **A governance ritual.** Doing it requires ceremony the ordinary case does not: a changeset, a migration callback, a review sign-off, a versioned upgrade hook.
- **A rival organized around rejecting the ideal.** A competing paradigm exists whose defining move is not making the commitment at all — evidence that the commitment is real in the original rather than an accident of description.

Two constraints keep this from collapsing into permission to keep anything.

**The pricing must be independently attested.** It has to exist in the domain's practice before the counterexample was raised against this claim. Pricing invented by the author after the counterexample lands is exactly the immunizing move; it is the difference between citing a runtime's deoptimization penalty and asserting that the case "is really an edge case".

**Unpriced exceptions still refute.** If the domain performs the exception routinely, through the ordinary interface, with no name, cost, or ceremony marking it, then the idealization has misdescribed what the domain does. So does evidence that the ideal mechanism is not the dominant one — that the corrections carry more of the behaviour than the first-order model does. Those two remain live refuters of an idealized claim, which is what keeps it a claim.

These are the idealization-direction analogues of the guards on the other escapes from counterexamples: the forbids-test for [generality bought to avoid counterexamples](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md), and the refuter test for narrowing. Each escape is legitimate in some cases and degenerate in others, and each needs its own discriminator.

## A worked case: counterexamples that the domain prices

A 2026 full improvement pass in this repository defeated three premises of a note comparing agent definitions and sessions to the class/instance relation, now retitled [instantiation alone cannot model agent learning across sessions](./instantiation-alone-cannot-model-agent-learning-across-sessions.md). The defeated premises were that class-based object orientation fixes a class before its instances exist with no instance-caused path to changing behaviour inherited by later instances, that it fixes the class/instance boundary at authoring time, and that instance state can only parameterize a repertoire the class fixes. Each was defeated globally by a real counterexample: mutating `type(self)` from an instance method in Python, Ruby singleton methods, per-instance bound methods.

Every one of those counterexamples is priced by the domain that supplies it. Class mutation goes through reflection rather than ordinary class syntax; the practice is named monkey-patching, which is not a compliment; runtimes charge for it by deoptimizing code specialized on the old shape; long-lived systems ritualize it into changesets or migration callbacks such as Erlang's `code_change`; and prototype-based object orientation exists as a rival organized around not making the class/instance split at all. On the criterion above, the defeated premises were arguably ideal-type claims about the paradigm whose exceptions the paradigm itself prices — which does not settle whether keeping them would have been right, only that the question was answerable and the pass had no slot in which to ask it. The conversion has since been made by direct revision: the note now states the fixed class as the paradigm's first-order model and carries the pricing in its own body, where a future pass can attack it.

## A second case: the option was absent, not rejected

An earlier pass on the note now titled [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) defeated its claim that each remedy class acts on exactly one of three objects, using the observation that a schema meant only to narrow the specification can also steer the interpreter off format violations. The pass repaired by reframing, and the crisp model survives only informally as "primary target".

This case cuts the other way on the merits, and that is why it is worth keeping next to the first. The defeating cross-effects are not obviously priced: nothing in the domain marks a schema's steering effect as an exceptional path, and it is not clear the cross-effects are subordinate to the primary ones. An idealization attempt here might well have failed the test honestly. What the case shows is narrower and structural — the repair vocabulary in use (keep, delete, merge, rehome, with reframing as a keep variant) offered no form in which such an attempt could be made, so no one had to decide.

## A verdict vocabulary without the option ratchets claims toward weakness

The consequence for review systems is sharper than "sometimes idealization is right". A pipeline whose premise verdicts are only DEFEATED and HOLDS has no verdict for *holds as an idealization, exceptions priced*. It therefore cannot accept such a repair and cannot reject one either, because rejecting requires running the pricing test and there is no slot where the test applies. Every available repair for a DEFEATED premise weakens the claim — narrow it, hedge it, drop it. When authors independently sweep their drafts for absolutes and scope them down, the two pressures point the same way, and a claim can be walked from a strong ideal-type form to a hedged one in individually defensible steps, with no step at which anyone considered that the strong form was the more useful one.

Scope this honestly: two witnessed cases, not a measured trend. In the second case the reframed claim arguably ended up sharper than what it replaced, so the pipeline's bias did not produce a worse artifact there. What the two cases jointly establish is the mechanism and the missing verdict, not a rate.

## Scope

The criterion applies to defeated claims that were crisp or exclusive and whose unification is worth keeping. It is not a licence to retain any refuted claim under a new name. Where the exceptions are unmarked, unbounded, or carry more of the behaviour than the model does, narrowing, reframing, or deletion remains the honest repair, and an idealization attempted there should fail its own test.

The domain-pricing criterion needs a domain with enough settled practice to price anything. Mature engineering paradigms, physical sciences, and established professional fields have vocabularies, tooling, and rituals that mark their own exceptions. A young or contested domain may have no such attestation available, in which case the test returns no answer rather than a pass, and the ordinary repairs apply.

The claim is about which observations refute, not about which repair wins in a given case. Adding the verdict does not say how often it should be chosen; a system could add it and correctly reject nearly every attempt. What a vocabulary lacking it cannot do is record that rejection as a decision.

## Open Questions

- Who judges pricing, and how contestable is it? "The domain prices this" is itself a claim about a domain's practice, and a motivated author will find marked-looking features around any exception. Whether the five signatures above are discriminating enough in practice, or need a stated threshold such as more than one independent signature, is untested.
- Does an idealization need scheduled re-testing? Exceptions that were marked and rare under one regime may become ordinary as the domain evolves — reflective mutation becoming routine in a language community, say — which would refute the idealization without any new counterexample to the first-order model.

---

Relevant Notes:

- [narrowing bought to survive review is paid for in content](./narrowing-bought-to-survive-review-is-paid-for-in-content.md) — contrasts: the narrowing escape and its analytic limit; idealization is the preservation move, with immunization rather than emptiness as its degenerate limit
- [generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — contrasts: the widening escape; each escape from counterexamples needs its own honest-versus-degenerate discriminator, and this note supplies idealization's
- [title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — grounds: the Popperian maintenance frame this criterion sits inside, where a claim title is the exposed commitment a repair must answer for
- [instantiation alone cannot model agent learning across sessions](./instantiation-alone-cannot-model-agent-learning-across-sessions.md) — evidenced-by: the pass whose defeating counterexamples were each priced by their own domain; the note has since been converted by revision and carries the strong claim as a declared idealization with its pricing inline
- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — evidenced-by: the pass where the pricing question was structurally unaskable, and where the counterexamples may not have been priced anyway
- [methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — contrasts: idealization keeps unification in the generator layer instead of letting it migrate into methodology-shaped content
