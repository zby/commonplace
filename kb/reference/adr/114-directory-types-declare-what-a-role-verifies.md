---
description: "A layout role may declare the roles it verifies; the engine derives a verifies relation for each, coverage requires it, and only a judgment of the handed version covers it, never a content check"
type: reference/types/adr.md
status: accepted
---

# 114 — Directory types declare what a role verifies

**Status:** accepted
**Date:** 2026-10-09
**Amends:** [ADR 111](./111-directory-types-declare-their-layout.md): a role's layout entry gains `verifies`, a second relation kind beside `cites` and `identity`, with engine semantics the other two do not have.

## Context

ADR 111 gave a layout two relation kinds: `identity`, which fields a role
repeats from another, and `cites`, whose declarations a role's references
resolve against. ADR 113 made the engine derive the artifact's relations from
the layout and require an accepted judgment over each before publication.

The analysis artifact has three verifying roles. Each reads other roles and
reports blockers against them, and a code job applies the verdict by judging
the exact versions the verifier was handed. That judgment needed a relation
to cover, and the only one available was the verifier's `cites` to its
subject. So `record-verification:cites:runtime` carried two meanings: the
verification's references resolve against the runtime report, and the
runtime report is accepted by the verification. Nothing in the type said
which meaning a relation had.

Two things followed. The invariant that a verdict's content acceptance must
not cover its subjects' gates was kept by convention: every apply handler
named its subjects by hand so the shared check could exclude them from its
scope. And the compact plan proposed in
[plans without structural wrapper code](../proposals/plans-without-structural-wrapper-code.md)
could not derive a verifier's apply job, because the subjects lived in
handler constants, not in the declaration. A plan that omitted verification
would have published an artifact the type declared complete.

## Decision

A role in a layout may declare `verifies`, a list of roles. It states that
an instance of the artifact is one whose listed roles this role has
verified. The layout parser accepts it beside `cites` and `identity` and
requires each named role to exist; validation gives it no other meaning.
Reference resolution stays with `cites`, so a verifier that cites what it
verifies lists the roles under both.

The engine derives one relation `<role>:verifies:<partner>` per entry.
Coverage requires an accepted judgment over it like any relation, so an
artifact whose verifier has not accepted a subject is not publishable, and
a plan cannot leave verification out without the run stopping short of
publication. The engine does not know what a verification says; it knows
only that the relation needs a judgment.

One invariant holds for every consumer: a content check never covers a
`verifies` relation. The shared check's scope is the type's `cites` and
`identity` relations from the candidate's role to the partners in its
snapshot, and excludes `verifies` relations by rule rather than by a list of
subjects the handler supplies. A `verifies` relation is covered only by a
judgment of the subject's version that the verifier was handed, recorded by
the apply job or by the operator's judge command naming that relation.

The analysis set declares that record-verification verifies the runtime,
memory, epistemic and reconciliation reports, profile-verification verifies
the memory profile, and synthesis-verification verifies the synthesis. Its
plan's judgment inputs and its apply handlers name `verifies` relations.

## Considered alternatives

**Declare the subjects in the plan, on the verifier's job.** The loader
would learn them without touching the type. Lost because the type would not
notice a plan that omitted verification: coverage would still be satisfied
through `cites`, and a published artifact would carry unverified records the
type calls complete. Whether an artifact's records are verified is part of
what the artifact is, which is the layout's subject.

**Keep the overloaded `cites` relation with subjects named in handlers.**
The state before this decision. Lost because the invariant lived in each
handler's argument list, the relation names in the plan did not say which
meaning they carried, and the loader would have had to read Python
constants.

**Let `verifies` imply `cites`.** It would spare the analysis set three
repeated lists. Rejected to keep the validator's meaning of a layout
separate from the engine's: a verifier might one day verify a role it does
not cite, and the two lists would then diverge for a reason.

**A general vocabulary of named relation kinds.** Deferred. Two kinds with
engine semantics and one without is what the one directory type needs; a
third kind with its own coverage rule can be added when a type needs it.

**A `verifies` frontmatter field naming the verification's stage.** The
verification document carried `verifies: records | profile | synthesis`, and
the type rule checked it against the role. Dropped: the role already names
the stage, the field's only check was that it repeated the role, and it
shared its name with the layout relation while meaning something else. A
verification in progress that still carries the field fails the schema and
is rewritten without it.

## Consequences

The plan's relation names say what they mean, and the invariant that a
content pass cannot settle a verification gate is the engine's rule, not a
convention each handler repeats. A loader can derive a verifier's apply job
and its subjects from the layout alone, which removes the last reason the
compact plan needed handler constants. A verification left out of a plan
stops the run short of publication instead of publishing.

Harder: every judgment input, handler scope and plan that named a
`cites` relation for a verification gate changes to the `verifies` name,
and a verifier declares its subjects under both keys when it cites them.

Operativity. The decision reaches its consumers through the layout
frontmatter of each directory type, consumed by: the layout parser and
directory validator; the engine's relation derivation, coverage and the
shared check's scope rule; the analysis plan's judgment inputs and its
apply handlers; the one directory type that declares a layout and the
engine tests' toy type; the validation contract and ADR 111's prose; the
compact-plan loader when it is built. The operator's judge command accepts
the new relation names through the same declaration.

This decision has been exercised by one consumer with three verifiers whose
subject sets are disjoint. A role verified by two verifiers would need both
relations accepted, which is the natural reading but untested. A chain, a
verification that is itself verified, is untested. Deterministic coverage
of a `verifies` relation records that a verdict was applied, not that the
verdict was right.
