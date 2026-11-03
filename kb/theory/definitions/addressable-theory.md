---
description: "Definition — an addressable theory is a theory formulated in language whose assumptions, scope, and parts can be inspected and revised individually; a graded structural property, separate from tentative status"
type: types/definition.md
tags: [self-improving-systems, learning-theory, theory-builder]
---

# Addressable theory

An **addressable theory** is a theory formulated in language whose
assumptions, scope conditions, and parts can be inspected and revised individually. A failure
can then guide a search over candidate parts, and an edit can change selected
parts while the rest stays in place.

The KB needs the term to keep a structural property apart from an epistemic
status. Every theory the KB retains is a [tentative theory](./tentative-theory.md);
only some are addressable. A [theory builder](./theory-builder.md) requires
only the minimum, localized content: some unit carries what the theory says.
Finer grades are Commonplace's design commitment, not a membership condition.
The expected benefit is that criticism can name a part, so a revision keeps what
still works while changing what failed; whether that benefit arrives is an
empirical question.

## Scope

- **It comes in degrees.** A theory with separately stated assumptions and
  scope conditions is more addressable than an undivided document. Whole
  replacement can still change a theory's scope; addressability lets the
  revision target that scope separately.
- **It follows the localization axis.** Of the two axes that derive
  [representational form](./representational-form.md),
  localization supplies addressability under the consumption path in question.
  Natural-language and symbolic artifacts have parts the consumer takes up
  separately. Distributed-parametric state exposes no such instruction-level
  parts under the path on which a system runs it as a model. The same parameters
  are addressed numerical units under the runtime's path; changing one does not
  thereby identify an instruction-level commitment. See
  [reflection buys addressability](../reflection-buys-addressability.md).
- **How strongly a case can contradict the theory is a separate matter.** It
  follows the other axis, assigned consequences. Where consumers are held to
  a reference that fixes a part's consequences, a validator or executable test
  can mechanically check a contradiction within the predicate it implements.
  This does not make every consequence decidable. Whether the encoding captures
  the intended claim remains criticizable. Where a reader derives the implication
  from natural language without such a reference, that interpretation also enters
  the diagnosis. See [codification](./codification.md).
- **Addressability does not guarantee affordable inspection of consequences.**
  A prompt under a pinned model adopted as its reference remains separately
  editable, but the instruction-level rule assigning its consequences is not
  separately exposed in the weights. It is symbolic and can be opaque under
  that path. A readable script or validator can expose that rule; symbolic
  membership alone does not.
- **A located part is a candidate.** A failure rarely
  identifies one faulty commitment. Popper notes that a test may bear on a
  large part of a theoretical system, while holding that some cases do
  identify the responsible hypotheses
  ([Conjectures and Refutations, Chapter 10, section XVI](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
  Unchanged text also does not guarantee unchanged consequences; a revision
  is checked against the failure and against other cases.
- **Locating a fault and containing a repair are separate.** A trace can
  implicate a shared rule even when many other parts depend on it. That rule
  can be a repair candidate while checking the edit requires cases across
  those dependencies. [Near-decomposability](../opacity-is-the-lack-of-a-known-near-decomposition-for-the-question.md)
  proposes weak interaction as a condition that can reduce this inspection
  burden; it is not a requirement for addressability or for identifying a
  candidate part.

## Precedent

The classical theory-refinement systems of machine learning,
[EITHER](../../sources/theory-refinement-analytical-empirical-methods.ingest.md)
and [FORTE](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md),
are the fully addressable case with computed consequences: a Horn-clause rule
set, a proof procedure, and named repair operators. They show that, in such a
setting, proof traces can connect a discrepancy to candidate repair
locations. They do not show unique fault identification, and FORTE's search
can stop before its training cases are consistent. The KB cites them as a
precedent for repair under addressability. It takes neither its paradigm nor
a preference for minimal revision from them.

## Exclusions

- **A latent world model as such.** It is non-localized, so it is revised
  without separately stated assumptions or claims to target. An inspectable
  causal model or simulator program can expose those parts and be both a
  world model and an addressable theory.
- **Storage location.** A theory kept in a file is not thereby addressable,
  and addressability does not require a particular store. Traces with an
  index locating conjectures, their parts, and their testing record can
  implement the same addressable objects as separate theory documents.

## Misuse Cases

- Reading mechanically checked consequences into a prose part. For a
  natural-language part, "derived" means interpreted until the part is
  codified.
- Treating a successful local edit as confirmation of the theory that
  motivated it.
- Assuming an addressable prompt's consequences can be read from an adopted
  model reference. The prompt is localized; that does not expose the
  reference's instruction-level rule.

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — contrasts: the epistemic status, which requires no structure
- [Theory builder](./theory-builder.md) — extends: the system whose condition 1 is addressability's minimum; Commonplace's design commits to finer grades
- [Representational form](./representational-form.md) — grounds: the localization and assigned-consequences axes
- [Codification](./codification.md) — grounds: the crossing that fixes a part's consequences against a reference, separately from whether those consequences are affordable to inspect
- [Reflection buys addressability](../reflection-buys-addressability.md) — extends: what addressability changes about an improvement pathway
- [Opacity is the lack of a known near-decomposition for the question](../opacity-is-the-lack-of-a-known-near-decomposition-for-the-question.md) — mechanism: proposes when weak interaction can make inspection of a repair's effects local
- [Theory refinement combining analytical and empirical methods](../../sources/theory-refinement-analytical-empirical-methods.ingest.md) — evidenced-by: the classical precedent
- [Automated refinement of first-order Horn-clause domain theories](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md) — evidenced-by: the classical precedent and its search limits
