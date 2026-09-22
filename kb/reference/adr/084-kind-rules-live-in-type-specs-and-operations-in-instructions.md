---
description: "Decision that a subdirectory never carries binding rules: rules about a kind of artifact live in its type spec, rules about location in COLLECTION.md, and lifecycle operations in instructions the type spec names"
type: ../types/adr.md
tags: []
status: accepted
---

# 084-Kind rules live in type specs and operations in instructions

**Status:** accepted
**Date:** 2026-09-22
**Amends:** [ADR 028](./028-design-proposals-live-in-reference-proposals.md) (where the proposal contract lives), [ADR 056](./056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) (which documents carry the archiving rules)
**Extends:** [ADR 071](./071-text-contract-is-part-of-the-collection-definition.md)

## Context

Some rules bind less than a whole collection. The design-proposal rules bind
`kb/reference/proposals/` only; the archive rules bind one directory below it.
Commonplace has two enforced write-time surfaces. A type spec binds every
artifact that declares the type ([ADR 038](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)).
A `COLLECTION.md` binds every artifact located in the collection
([ADR 041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md)).
`cp-skill-write` reads both, and review hashes both, so an edit to either
re-checks exactly its cohort. Neither surface is scoped to a subdirectory.

The forces that would recur if this decision were reverted:

- **A rule in a subdirectory README is inert.** No write step reads it and no
  review pair hashes it. The operativity-and-warrant clause was added to
  `kb/reference/types/adr.md` and to the proposals README in one commit; the
  type edit re-checked the ADR cohort, and the README edit re-checked nothing.
- **README rules conflict with ADR 071.** ADR 071 keeps each `COLLECTION.md`
  as the only binding local contract, while the proposals README said its
  clauses bind through authoring and review.
- **Per-directory fixes do not hold.** The proposals rules moved into a
  collection-local type, and a binding archive README appeared one level
  deeper the next day. At that point one archiving rule was stated in four
  places, each mixing what must hold with how to carry it out.
- **Nested contracts make composition the whole design.** A nested
  `COLLECTION.md` would need a merge rule for every clause kind (quality goal,
  type eligibility, title conventions, link grammar), a choice between one
  review per ancestor contract and one against the nearest, and a writer who
  assembles the effective contract from several files. It would also spend
  ADR 041's guarantee that the nearest contract is the only one.

## Decision

**A subdirectory inside a collection carries no binding rules.** Collections
do not nest. A README in a subdirectory is navigation and orientation: it may
list, explain, and point, but it states no requirement.

**A rule is placed by what it binds:**

| The rule binds | It lives in | Enforced by |
|---|---|---|
| a kind of artifact, wherever it sits | that kind's type spec, collection-local when the kind exists in one collection | the type-conformance review and the type's schema |
| what may live where | the collection's `COLLECTION.md` | the collection-conformance review and the validator |
| how to carry out a lifecycle operation | an instruction in `kb/instructions/` | the executor that invokes it |

The type spec states the invariant (what must hold of the artifact in each
lifecycle state) and names the instructions for its lifecycle operations. The
instruction states the steps. `COLLECTION.md` states placement once. None of
the three restates another; each links to the others where a reader needs
them.

**A kind's states are stated by its type.** An archived design proposal is
still a design proposal, so the type spec states what holds of it after
archiving. A rule that belongs to a directory with no kind to name is a
placement rule: it goes in `COLLECTION.md` and, when it is mechanical, in the
validator, as the archive link boundary already is.

**Applied now to design proposals.** The proposal contract moves from
`proposals/README.md` into the `design-proposal` type spec. The proposals and
archive READMEs become navigation. Partial-adoption extraction and
current-state refresh become instructions beside
[retire an artifact](../../instructions/retire-artifact.md). This decision
adopts and retires the proposal "Where subtree-scoped write-time contracts
live".

## Considered alternatives

**Keep the README as an unenforced area contract.** No machinery, and the
contract stays cheap to revise. Rejected because the clauses that carry the
most judgment reach only a reader who follows a link, and a non-conformant
author is not detectable.

**Fold area rules into `COLLECTION.md`.** Immediately enforced at no
machinery cost, as `kb/agent-memory-systems/` does for its areas. Rejected as
the general rule because every write and conformance review in the collection
then loads rules that apply to one subdirectory, and the cost grows with each
area. It remains right for placement rules, which are what it now carries.

**Nested `COLLECTION.md` files.** The general form of location scope.
Rejected for the composition costs named in Context. A restricted form, where
a nested contract may only add clauses and each ancestor contract gets its own
review, would compose without merge rules. It is not built because every live
case is either a kind or a mechanical boundary. A subdirectory rule that is
neither, and that recurs, is the trigger to reconsider it.

**A separate area-contract surface with its own review kind.** A third gate
kind scoped to a subtree, plus a write step that reads the nearest area
contract. Rejected as the most machinery for a need the type surface already
meets.

**Have `cp-skill-write` read the nearest README.** Cheap, and it helps any
option. Rejected because it makes an unreviewed document operative at write
time; a README edit would change behavior without re-checking anything.

**Free choices.** `kb/notes/proposals/` had the same README-as-contract
shape and now follows the same rule, with a collection-local
`theory-proposal` type. Experiment designs stay in
`kb/reference/proposals/` as design proposals; whether they need a separate
type is left until protocol records need structure the design-proposal type
cannot give.

## Consequences

A reader learns what binds a proposal from two documents the write path
already loads: the type spec and `COLLECTION.md`. The proposals README can be
revised freely because nothing depends on it.

The type spec grows by the proposal contract's judgment clauses. Editing them
re-checks the proposal cohort and nothing else, which is the scope the
clauses have. The placement clause cannot live in the type, because a type
binds by declaration and cannot bind an artifact that never enters the
directory.

Instructions do not bind by location, so an operation is followed only when
invoked. The type spec's lifecycle section is the routing point: an agent
that loads the type to write or review a proposal is told which instruction
each transition uses.

**Operativity path.** `cp-skill-write` reads the type spec at its type step,
with binding authoring force. The type-conformance review pair puts the type
spec on the gate side, so the clauses are reviewed against every
design-proposal and a clause edit stales that cohort. The schema keeps its
mechanical checks. The validator keeps the archive link boundary.
Instructions are consumed by the agent that runs the named operation, with
the force of a followed procedure; nothing checks that a lifecycle transition
used them.

---

Relevant Notes:

- [ADR 038: type-conformance reviews use the type spec as the gate](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — see-also: the mechanism that makes a type spec's natural-language rules enforceable for exactly its cohort
- [ADR 041: collection-conformance reviews use COLLECTION.md as the gate](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — see-also: the nearest-contract-only guarantee this decision keeps
- [Collections and types](../collections-and-types.md) — part-of: the two-surface model this decision completes with a placement rule
- [Design proposal](../types/design-proposal.md) — implemented-by: the type spec that now carries the proposal contract
- [Why directories despite their costs](../../notes/why-directories-despite-their-costs.md) — rests-on: local conventions are a directory affordance, and each directory with its own rules taxes routing and skills
- [Methodology enforcement is constraining](../../notes/methodology-enforcement-is-constraining.md) — rests-on: the gradient from an instruction an agent may not read to a gate that always runs
