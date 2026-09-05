---
description: "Methodological closure tracks what a retained method settles; computational closure tracks the absence of human decisions during the assessed operation, without requiring every judgment to have explicit criteria"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems]
---

# Methodological and computational closure track different changes

An improvement pathway can use a settled method while depending on a human
actor. It can also operate without a human while leaving consequential choices
to a model's judgment. These are different properties.

**Methodological closure** asks whether the retained methodology settles the
consequential decisions that the pathway raises. Naming a decider or saying
“use judgment” settles routing, not the content of that judgment.

**Computational closure** asks whether the assessed operation requires a human
decision. A function is computationally closed when computation supplies its
required decisions; a whole pathway is computationally closed when this holds
for every required function within the declared boundary and horizon.

These readings are not the cybernetic notion of organizational closure. The
[reflective-system definition](./definitions/reflective-system.md#exclusions)
keeps that separate. Neither reading alone establishes competence, improvement,
or warranted authority.

## Boundaries and the time of a contribution matter

A [reflective system](./definitions/reflective-system.md) may include people.
A maintainer can inspect a representation, revise it, and put the revision into
operation. That supplies a reflective path without demonstrating computational
performance of the maintainer's decisions.

Report consequential functions as human, computational, or joint. An agent
writing most of a patch does not make diagnosis or admission computational when
a person supplies those decisions. Conversely, human authorship of a starting
method does not make every later automatic execution joint. Declare the seed
and its construction separately from interventions during the assessed run.
The [fixed-boundary reallocation account](./computationally-directed-self-improvement-is-a-reallocation.md)
develops the transition toward removing internal human roles.

Per-function reporting has a precedent in [Parasuraman, Sheridan, and
Wickens](https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf).
Here the functions are those of the improvement pathway, such as search,
evaluation, and retention in a proposal-selection loop. This use does not
inherit their within-function level scale. Cross-system comparison still needs
a basis for matching responsibilities: [autonomy measurement](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md)
cannot be reduced to the fraction of generated text or code.

## Declare the assessed work and permitted inputs

Evidence for computational closure must identify the task-selection process,
objective, boundary, permitted inputs, horizon, resource limits, and treatment
of failures. Selecting easy cases or ending observation before the next human
intervention can otherwise make an open pathway appear closed.

Task selection and user participation may remain external. For a [software
house](./definitions/software-house.md), users can supply requirements, domain
facts, observations, and acceptance judgments about visible behaviour. Supplying
implementation diagnosis, internal design selection, or admission of a retained
successor instead fills an internal production role. Calling that contribution
“feedback” does not change it.

A component experiment can assess a narrower set of decisions, but must not
present the result as whole-house automation. Record failures, refusals,
timeouts, and reopened human roles. A failure reached without human help may
still be computationally closed; it is not thereby adequate.

The task-selection process can introduce new kinds of work. Declaring how an
evaluation selects requests does not require fixing the house's future product
family. The evidence remains limited to the paths and conditions assessed.

## Four combinations

| Improvement decision | Methodologically closed? | Computationally closed? | Why |
|---|---:|---:|---|
| A maintainer applies an exact checklist before accepting a patch | Yes | No | The method settles the criterion, but a human supplies the verdict. |
| A validator accepts only when a specified structural predicate holds | Yes | Yes | The criterion is settled and computation executes it. |
| An unattended agent inspects failures and chooses a revision using its judgment | No | Yes | No human intervenes, but the retained method leaves consequential choices unresolved. |
| A maintainer and agent jointly judge a note against “is this good?” | No | No | The method does not settle the criterion and a human participates. |

Stable but unarticulated expertise does not, by itself, add a criterion to the
retained methodology being assessed. That is a limit of what the method states,
not a claim that the expertise is unreal, inconsistent, or impossible to
transfer. The same distinction applies to model competence. [Explicit
retention](./only-explicit-retention-is-durable-writable-and-addressable.md)
provides direct targets for criticizing a criterion; it does not define all
possible governance or learning.

A hosted model can supply a computational decision while depending on external
inference infrastructure. That dependency must be declared, but it is not a
human production decision merely because a provider operates the service.
Selecting a model binding also does not give the system [reflective
coverage](./reflective-coverage-is-graded-across-representational-forms.md)
over the provider's parameters. A fixed-model witness additionally needs the
model identity and pinning required by its protocol.

## One route that advances both properties

A recurring human decision may become easier to transfer when the house makes
its inputs, criterion, and failure response explicit. Three functions describe
that route:

1. **Representation:** make relevant premises available to the deciding
   process, using the direct handles that [reflection can
   supply](./reflection-buys-addressability.md).
2. **Settlement:** state or reference a criterion that constrains the result,
   rather than merely naming its author. [Methodology governing its own
   extension](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md)
   explains the limit of that settlement.
3. **Warranted execution:** obtain evidence that the computational process
   performs the decision adequately within the intended scope. [Available
   checks](./warranted-autonomy-is-bounded-by-oracle-domain.md) bound that evidence.

This is not a necessary sequence for every computational transfer. A model may
already supply the judgment or infer it from examples while leaving its
criterion unstated. Where parameter learning is permitted, it supplies another
possible route. Such cases can advance computational closure without making
the retained method more complete.

Under a fixed-model premise, new retained capacity must instead use the
permitted surrounding state. A written theory, examples, tools, or a procedure
can guide the fixed model without spelling out a complete judgment rubric.
Explicit criteria are useful for inspection and selective revision, not a
logical precondition of every automatic decision.

Nor does making a criterion explicit warrant its execution. A settled gate can
encode a poor proxy, and an agent can misapply a sound instruction. Admission,
independent outcomes, and recovery therefore need evaluation separately from
both kinds of closure. The [Commonplace reference
case](./evidence/commonplace-as-a-reflective-system.md) records one human-agent
path rather than demonstrating a general computational transfer.

## Reflection is separate

Reflectivity requires a causally connected self-representation that processes
inside the boundary can use and change. It does not require a method that
settles every next decision. A reflective house can revise its own principles
through fallible judgment. A fixed pipeline can settle its operational choices
without representing or revising itself.

The properties can reinforce each other when the represented object is the
improvement method. Making an assumption addressable permits criticism;
settling a revised criterion permits repeatable application; transferring its
execution removes one human role. Each step can fail independently.

## Scope

Both closure readings are relative to a declared pathway and horizon. A
completed update is not the same as closure, and an observed closed path is not
proof of reliable continuation on untested requests. The method may also
explicitly leave a tolerable choice open; assess whether that choice matters
to the claim before treating it as a missing criterion.

## Open Questions

How should trials distinguish seed construction from run-specific human design
supplied through an apparently external input? What evidence establishes that a
computational implementation preserves a criterion rather than substituting a
convenient proxy? These are boundary and outcome questions, not reasons to
identify explicitness with automation.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: supplies functions over which closure can be assessed
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: defines what the retained method must settle
- [Explicit retention provides direct targets for selective revision](./only-explicit-retention-is-durable-writable-and-addressable.md) — mechanism: explains the inspection advantage without making explicit criteria necessary for automation
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — extends: describes removal of required human production roles
- [Software house](./definitions/software-house.md) — defined-in: supplies the complete producer's functional boundary
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: separates actor allocation from justified authority
- [Distinct residue classes require distinct functions in a self-improving architecture](./residue-classes-need-different-mechanisms-so-architecture-is-mixed.md) — extends: distinguishes the functions missing from transfers that remain human
