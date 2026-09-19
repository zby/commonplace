---
description: "Proposal: let a builder that regenerates its theories from retained records qualify as a theory builder, leaving the update operation open; records what was declined from a wider refactor"
type: kb/types/note.md
---

# Admitting a regenerating builder in the theory builder definition

This is a [theory proposal](./README.md): finished, unadopted, and not a
premise for other notes.

**What adoption would add.** No new terms. It would let one definition
cover every arm of a retained-form comparison, including a builder that
rebuilds its theory from retained records at each decision and discards it.

**What adoption would change.** Two sentences in
[theory builder](../definitions/theory-builder.md), and the paragraph of
the
[lead article](../../articles/learning-by-theory-refinement-with-fixed-models.md)
that quotes its first sentence. The first-downstream-run evidence protocol
should be checked for wording that assumes every builder retains its
theories.

## Current state (as of 2026-09-19)

The definition says a theory builder is "the complete persistent system
responsible for developing and revising tentative theories". It then says
"Revision is theory refinement" and that development, "constructing a first
theory where none exists", is in scope. Read strictly, a builder that
regenerates its theory from records is not a theory builder: a theory
exists and is ignored, so the work is neither refinement nor development.

The rest of the definition already identifies the builder by
responsibility and lineage, not by method. It says persistence "establishes
neither retention nor learning", that "a builder whose fixed machinery
suffices for every admitted demand still meets this definition", and that
fixed models are a constraint on particular studies.

## The change

- The base sentence names responsibility for developing and maintaining
  tentative theories, and leaves the update operation open.
- In place of "Revision is theory refinement": a builder may update a
  theory by refining it or by regenerating it from retained records. Which
  it does is a property of the builder, and it is what a retained-form
  comparison varies.
- The sentence "Revision is theory refinement" moves to wherever the
  learning paradigm is defined. The builder is then the system that holds
  the responsibility, and the paradigm is how a particular builder learns.
- No new named kinds. "Refining" and "regenerating" describe treatments.

The persistence clause needs one check. A regenerating builder's continuing
state is its records and machinery, and its responsibility is for the
theories it delivers, which it may not retain itself.

## Trigger and cost

Import when a regenerating arm needs classifying, or when the learning
paradigm receives its own definition, since that definition is where the
moved sentence would go. Until then a retained-form comparison can run as
paired treatments of one system without deciding whether each treatment is
a theory builder.

The cost is small: two sentences, one article paragraph, and a check of the
[reflective](../definitions/reflective-theory-builder.md) and
[autonomous](../definitions/autonomous-theory-builder.md) conditions and of
the [software house](../definitions/software-house.md) definition the
clauses were adapted from.

## Declined alternatives

A wider refactor was proposed at the same time: redefine the builder by
responsibility alone and add a hierarchy of kinds above it. Three parts
were declined, and should not be reopened without new evidence.

- **"Learning theory builder" as a named kind.** The definition says
  extension "is not a third condition; it is the quantity a research
  question measures." A kind would turn a budget-relative comparison into a
  classification.
- **Reflection placed under learning.** The hierarchy made the reflective
  builder a case of "learns by theory refinement". The KB keeps reflection
  independent of extension, and the reflection hypothesis tests whether one
  produces the other. Making reflective builders learners by classification
  would make part of that hypothesis true by definition.
- **"Applying" added to the builder's responsibilities.** Consumers often
  apply the theories, and they are outside the boundary.

Most of the rest of that refactor was already in the definition, as the
current-state section shows. The part that held is the change above.

---

Relevant Notes:

- [Theory builder](../definitions/theory-builder.md) — defined-in: the definition this proposal would change
- [Theory refinement](../definitions/theory-refinement.md) — defined-in: the update operation the base definition would stop requiring
- [Retained theories compared with retained traces under resource limits](./retained-theories-compared-with-retained-traces-under-resource-limits.md) — see-also: the comparison whose arms this change would admit
