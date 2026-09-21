---
description: "Definition — an addressable theory is a theory formulated in language whose assumptions, scope, and parts can be inspected and revised individually; a graded structural property, separate from tentative status"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Addressable theory

An **addressable theory** is a theory formulated in language whose
assumptions, scope conditions, and parts can be inspected and revised individually. A failure
can then guide a search over candidate parts, and an edit can change selected
parts while the rest stays in place.

The KB needs the term to keep a structural property apart from an epistemic
status. Every theory the KB retains is a [tentative theory](./tentative-theory.md);
only some are addressable.
[Conjectural learning](./conjectural-learning.md) does not require it. The
expected benefit is that criticism can name a part, so a revision keeps what
still works while changing what failed; whether that benefit arrives is an
empirical question.

## Scope

- **It comes in degrees.** A theory with separately stated assumptions and
  scope conditions is more addressable than an undivided document. Whole
  replacement can still change a theory's scope; addressability lets the
  revision target that scope separately.
- **It follows the localization axis.** Of the two axes that derive
  [representational form](../../../notes/definitions/representational-form.md),
  localization supplies addressability: natural-language and symbolic
  artifacts have parts to point at, and distributed-parametric state has
  none. See [reflection buys addressability](../../../notes/reflection-buys-addressability.md).
- **How strongly a case can contradict the theory is a separate matter.** It
  follows the other axis, assigned consequences. Where a defined consumer
  such as a validator, schema, or test fixes what a part implies, a
  contradiction can be mechanically checked relative to that encoding.
  Whether the encoding captures the intended claim remains criticizable.
  Where a reader derives the implication from prose, that interpretation
  also enters the diagnosis. See
  [codification](../../../notes/definitions/codification.md).
- **A located part is a candidate.** A failure rarely
  identifies one faulty commitment. Popper notes that a test may bear on a
  large part of a theoretical system, while holding that some cases do
  identify the responsible hypotheses
  ([Conjectures and Refutations, Chapter 10, section XVI](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
  Unchanged text also does not guarantee unchanged consequences; a revision
  is checked against the failure and against other cases.

## Precedent

The classical theory-refinement systems of machine learning,
[EITHER](../../../sources/theory-refinement-analytical-empirical-methods.ingest.md)
and [FORTE](../../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md),
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

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — contrasts: the epistemic status, which requires no structure
- [Conjectural learning](./conjectural-learning.md) — extends: the paradigm in which addressability is a conjectured benefit
- [Representational form](../../../notes/definitions/representational-form.md) — grounds: the localization and assigned-consequences axes
- [Codification](../../../notes/definitions/codification.md) — grounds: the crossing that gives a part computed consequences
- [Reflection buys addressability](../../../notes/reflection-buys-addressability.md) — extends: what addressability changes about an improvement pathway
- [Theory refinement combining analytical and empirical methods](../../../sources/theory-refinement-analytical-empirical-methods.ingest.md) — evidenced-by: the classical precedent
- [Automated refinement of first-order Horn-clause domain theories](../../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md) — evidenced-by: the classical precedent and its search limits
