---
description: "Lead article: theory refinement with fixed model weights as a learning paradigm, its departures from classical refinement, its conjectured attractions, and an outline of the theory builder, hypotheses, and first arrangement"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/theory-refinement.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
---
# Learning by Theory Refinement with Fixed Models

*A research program for systems that learn outside their weights*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** We propose a learning paradigm for systems built around large
language models: hold the model weights fixed, and let the system learn by
refining written theories that it retains outside the model and consults on
later work. The alternatives are adapting the weights, and retaining raw
records or summaries of experience without an explanation. The paradigm
rests on five ideas, named as they appear: **theory refinement**,
**addressability**, **reach**, **the deployed system as the learner**, and
the **theory builder** with its three testable hypotheses. Its attractions
(continual learning, fewer observations, legibility) are conjectures. The
supplements state how it would be tested and the first arrangement proposed
to test it. No test has been run.

## A case

Consider a system that maintains a release exporter. The exporter builds a
deployment manifest from a configured list of input files. Documentation
edits do not affect the manifest, so the system checks them for syntax
only. The system retains a short written account of why, in two parts: an
edit needs a manifest check when an executable consumer reads the edited
file, and the configured input list identifies every file the exporter
reads.

Later the exporter starts reading service definitions from named Markdown
files, which are added to the configured list. The account already says
what to do: those files now have an executable consumer, so their edits
need manifest checks. No new rule was written.

Later still, the exporter gains included snippets. A snippet that no
configured file names, but that a configured file includes, carries a
service definition. An edit to it passes its syntax check, and a release
ships with an invalid manifest. The account's second part has failed: the
configured list names the exporter's entry points, not everything it reads.
The system revises that part only: the inputs are the configured files plus
whatever they reach through includes. The first part stands. The system
then applies the revised account to other snippets it has not touched.

Three things happened. A written account guided a decision on a case it did
not mention. A failure contradicted one part, and only that part was
revised. The revision was chosen for what else it would handle, not only
for the failure that caused it. These are the first three ideas below:
theory refinement, addressability, and reach.

## Idea 1: theory refinement

[Theory refinement](../notes/definitions/theory-refinement.md) is the
learning operation that revises an existing explicit theory against
empirical cases, correcting its errors while keeping what was right,
instead of learning from scratch. The name comes from Ourston, Richards,
and Mooney in the early 1990s. Their theories were expert-supplied logical
rules and their cases were labelled examples. Their systems derived
consequences from the rules, found where a wrong consequence came from,
and edited that part.

We call the theory a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory),
in Karl Popper's sense: put forward as a solution, held open to criticism,
and never promoted to settled truth by surviving tests. How much support a
theory needs before the system relies on it is a policy the system has to
set.

## Idea 2: addressability

Refinement needs a theory of a particular shape. It must have consequences
a case can contradict, parts a failure can point at as candidate repair
locations, and parts that can be edited separately. We call a theory with
these properties *addressable*. The exporter account is addressable: it
predicted which edits needed which checks, the failure pointed at its
assumption that the configured list was complete, and that assumption was
revised on its own.

The paradigm keeps the operation and departs from the classical setting
in three ways.

- **The interpreter is a language model, so the theory can be prose.** The
  classical systems refined theories only in the one form their procedures
  handled. A fixed language model can be asked to apply and revise an
  account nobody has formalized, so a theory can enter the loop before
  anyone writes a checker for it. The cost is that consequences are
  interpreted rather than computed, and two readings can differ. As parts
  settle, refinement compiles them into schemas, validators, or tests,
  which gains checkability, not certainty.
- **The theory is partly normative.** A commitment such as "every query must
  respect the active tenant" is a rule the system keeps true, not only a
  hypothesis. A failure can therefore be resolved by changing the product to
  fit the theory, or by revising the theory to fit the evidence. Descriptive
  assumptions and implementation choices are the system's to revise. A
  requirement supplied from outside, such as tenant isolation, is not:
  weakening it would hide a failure, and only whoever supplied it can
  renegotiate it.
- **The theory may be about the system itself.** The account of which checks
  to run is part of the system's own production machinery. When the same
  loop revises how the system builds, tests, and revises its theories, the
  loop is *reflective*.

## Idea 3: reach

Among revisions that fit the evidence, the paradigm prefers the one with
more reach: the one that would also handle cases the failure did not
show. That is why the exporter case revises the account of what the
exporter reads, instead of adding an exception for one snippet. A patch
fixes one failure; a revision with reach also changes decisions on cases
nobody has reported yet.

## Idea 4: the deployed system is the learner

The unit that learns is the whole deployed system, because [retrieval,
scheduling, tools, and validators jointly determine behaviour with the
model fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
What the paradigm retains includes theories, procedures, tests, tools,
evaluators, and the update process itself. When a new theory needs a check
the system cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and with weights fixed that capacity has to persist outside the model.

This answers an objection from Rich Sutton's Bitter Lesson, that methods
which scale with computation beat methods built from human knowledge.
Written theories look hand-crafted, but the lesson turns on [how structure is produced, not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here computation forms and revises the theories, tools, and evaluators.
People may build the seed; after that, project-specific structure is a
learned product. That is compatibility, not a scaling advantage: search and
credit assignment over retained artifacts may scale badly, and adapting
weights may be cheaper. The program has to run those comparisons.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that contradicts the current theory forces a reconciliation, the
  paradigm's counterpart of retraining: decide which commitment gives way,
  revise it, re-check what depended on it. The edit is local; its
  consequences need not be. Reconciliation is where the costs of [governing
  behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate.
- **Fewer observations.** A correct theory says which new cases matter. In
  the exporter case, one discovered dependency changed the checking decision
  for several files. The conjecture that [theory refinement improves sample
  efficiency under structured
  shifts](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names, and
  fewer observations need not mean lower total cost.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. A rollback still needs a
  dependency check, because later changes may rely on it; legibility makes
  the target and its dependents findable. And unlike a learner confined to
  [a fixed decomposition, which inherits that decomposition's
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md),
  a system that can rewrite its own representations and tools has a wider
  space to repair in.

## Idea 5: the theory builder and its three hypotheses

A [theory builder](../notes/definitions/theory-builder.md) is the complete
persistent system responsible for developing and revising tentative
theories about the subjects it is asked to investigate. Whoever supplies
questions, cases, and acceptance judgments is outside it; whoever
interprets a theory, chooses what to blame, revises, or repairs the
machinery is inside, person or program. A builder
is [autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when its
machinery changes pass through a theory of its own machinery. The two
conditions are independent.

Fixing the weights is an experimental condition, not a recommendation for
mature systems. It rules out parameter updates as the source of a gain, but
task mix, computation, human intervention, or run-to-run variation could
still explain one, so attribution needs matched comparisons with the
retained change removed.

The program states three whole-system hypotheses, each with what would
refute it.

- **Sufficiency.** A learning methodology written in prose and code is
  enough for a computational builder on fixed public models to develop,
  retain, and use theories across declared areas, to a reliability target
  under a stated budget and external assessment. Refuted by a builder that
  needs people in inside roles, or a new learning method per area, to reach
  the target.
- **Comparison.** Under matched demands and resources, the methodology
  gains capability over its frozen seed and over a baseline that searches
  the raw records without it, and its reliability is comparable to a
  human-staffed builder's within a preset margin. Refuted by matched runs
  in which the controls do as well.
- **Reflection.** A builder whose machinery changes pass through a
  causally connected self-theory gains capabilities beyond its seed that a
  matched builder without one does not. Refuted by matched records in which
  the non-reflective builder gains as much; better outcomes alone do not
  test it.

A finite evaluation supports only a bounded claim. The three attractions
are tested separately, in component experiments that vary what is
retained; whole-system results and component results do not substitute for
each other.

The hypotheses are tested through an *externally tested* builder, one that
receives from outside a falsifier (failures it does not judge itself), an
objective, and an outcome level independent of its own evaluators. Where a
claim lacks that external assessment, [the builder owes three things for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level for
changing an objective, and attribution when it asserts a cause. The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both
levels. The setup is a first design, stated but not exercised, and we
expect it to change before a scored run.

## The first arrangement

The first arrangement proposed for testing the paradigm is Commonplace, a
framework for knowledge bases operated by agents. In the proposed run,
Commonplace produces a knowledge base and its supporting software for a
consuming project. Agents in that project use the knowledge base on their
tasks, and the project's own judges accept or reject the work; those
judgments are the external falsifier and objective. Commonplace would revise
the delivered product and, when a failure exposed a limit in its own
methods, revise those too. People still perform several inside roles; how
those roles would move to computation is the [bootstrap
supplement's](./bootstrapping-the-first-automated-software-house.md)
subject. No consuming-project run has been performed.

A different arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. Software fails visibly, so it offers a stronger falsifier, at the
price of a harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Open questions

- Whether revisions, each justified by its own evidence, compose into a
  justified lineage, and what support licenses each kind of reliance on a
  retained theory.
- Whether current models interpret prose theories consistently enough for
  diagnosis and repair, not only application.
- How to assign credit when a later failure could lie in the theory, the
  retrieval that never surfaced it, the evaluator that admitted a change,
  or a skipped check.
- Whether total cost, with theory maintenance counted, compares well with
  adapting weights on the same evidence.

## The five ideas to carry away

1. **Theory refinement.** Learn by revising an explicit, tentative theory
   against cases, keeping what was right.
2. **Addressability.** Refinement works when a theory has consequences a
   case can contradict and parts a failure can point at and edit alone.
3. **Reach.** Among revisions that fit the evidence, prefer the one that
   also handles cases the failure did not show.
4. **The deployed system as the learner.** With weights fixed, what learns
   is everything retained around the model, including the machinery that
   revises it.
5. **The theory builder.** The system that carries the paradigm, tested by
   three refutable hypotheses: sufficiency, comparison, and reflection.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state
the paradigm's terms with their exclusions and boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the external assessment, the first arrangement's protocol, and
the component experiments. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions,
and [transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery.
