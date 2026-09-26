---
description: "Lead article: theory refinement with fixed model weights as a learning paradigm — addressable theories, preferring reach, the deployed system as learner, fixed weights as a control — its conjectured attractions, hypotheses, and first arrangement"
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
records or summaries of experience without an explanation. We develop
five ideas: *theory refinement*, *addressable theories*,
*preferring reach*, *the deployed system as the learner*, and *fixed weights
as a control*. The paradigm's attractions (continual learning, fewer
observations, legible and reversible changes) are conjectures. No test has
been run.

## A case

Consider a system that maintains a release exporter. The exporter builds a
deployment manifest from a configured list of input files. The system
retains a short written account of which edits need a manifest check, in
two parts: an edit needs a manifest check when an executable consumer reads
the edited file, and the configured input list identifies every file the
exporter reads. Documentation edits get a syntax check only.

Later the exporter starts reading service definitions from named Markdown
files, which are added to the configured list. The account already says
what to do: those files now have an executable consumer, so their edits
need manifest checks. No new rule was written. An existing explanation was
applied to a new fact.

Later still, the exporter gains support for included snippets. A snippet
that a configured file includes, but that the list does not name, carries a
service definition. An edit to it passes its syntax check, and a release
ships with an invalid manifest. The account's second part has failed: the
list identifies the exporter's entry points, not everything it reads. The
system revises that part only: the exporter's inputs are the configured
files plus whatever they reach through includes. The first part stands. The
system then applies the revised account to snippets it has not touched.

Three things happened. A written account guided a decision on a case it did
not mention. A failure contradicted one part of the account, and only that
part was revised. The revision was chosen for what else it would handle.
The rest of this article argues that these three things are the core of a
learning paradigm.

## Idea 1: theory refinement

[Theory refinement](../notes/definitions/theory-refinement.md) revises an
existing explicit theory against cases, correcting its errors while keeping
what was right, instead of learning from scratch. The name comes from work
by Ourston, Richards, and Mooney in the early 1990s, whose systems took
expert-supplied logical rules, traced a wrong consequence on a labelled
example to its source, and edited that part.

What is learned is a [tentative
theory](../notes/definitions/tentative-theory.md) in Karl Popper's sense:
put forward as a solution and held open to criticism, however many tests it
survives. That status licenses nothing by itself. How much support a theory
needs before the system relies on it routinely, or compiles it into a test,
is a policy the system has to set.

## Idea 2: addressable theories

Refinement needs a theory of a particular shape. It must have consequences
a case can contradict. It must have parts that a failure can point to. And
those parts must be editable separately. We call such a theory
[addressable](../notes/definitions/addressable-theory.md). The exporter
account is addressable: it predicted which edits needed which checks, the
failure pointed at its assumption that the list was exhaustive, and that
assumption was revised on its own.

The paradigm keeps the operation and changes the setting in three ways.
These are our departures, not claims of the classical work.

- **The theory can be prose.** The classical systems refined theories only
  in the one form their procedures handled. A fixed language model can be
  given an unformalized account and asked to apply and revise it, so a
  theory can enter the loop before anyone writes a checker for it. The cost
  is that consequences are interpreted rather than computed, and two
  readings of whether a case contradicts the theory can differ. As parts
  settle, refinement compiles them into schemas, validators, or tests,
  which gains mechanical checkability but not certainty: the check may
  still misrepresent the theory.
- **The theory is partly normative.** A commitment such as "every query
  must respect the active tenant" is a rule the system keeps true, not only
  a hypothesis. A failure can therefore be resolved by changing the product
  to fit the theory, or the theory to fit the evidence, and the system must
  decide which. Descriptive assumptions and implementation choices are the
  system's to revise. A requirement supplied from outside, such as tenant
  isolation, is not: weakening it would hide the failure without improving
  anything.
- **The theory may be about the system itself.** The account of which
  checks to run is part of the system's own production machinery. When the
  same loop revises how the system builds, tests, and revises its theories,
  the loop is *reflective*.

## Idea 3: prefer reach

Many revisions can fit the same failure. The paradigm prefers the one with
more reach: the one that would also handle cases the failure did not show.
That is why the exporter case revises the account of what the exporter
reads instead of adding an exception for one snippet: the revised
explanation also covers snippets nobody has edited yet.

## Idea 4: the deployed system is the learner

With weights fixed, what learns is the whole deployed system, because
[retrieval, scheduling, tools, and validators jointly determine behaviour
with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
What it retains includes theories, procedures, tests, tools, evaluators,
and the update process itself. When a new theory needs a check the system
cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and that capacity has to persist outside the model.

We call this system a [theory
builder](../notes/definitions/theory-builder.md): the complete persistent
system that develops and revises tentative theories about the subjects it
is asked to investigate. Its boundary follows roles: whoever supplies
questions, cases, and acceptance judgments is outside; whoever interprets a
theory, chooses what to blame, produces a revision, or repairs the
machinery is inside, person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when its
machinery changes pass through a theory of its own machinery. The two
conditions are independent.

**The Bitter Lesson.** Rich Sutton's Bitter Lesson says that general
methods which scale with computation outperform methods built from human
knowledge, and written theories look like hand-crafted structure. The
answer turns on [how the structure is produced,
not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here computation forms and revises the theories, builds the tools, and
selects changes from evidence; people may build only the seed the system
starts from. That shows compatibility, not a scaling advantage. Adapting
weights on the same evidence may be cheaper, and that comparison is part of
the program.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that fits the current theory is written down and takes effect. A
  fact that contradicts it forces a reconciliation, the paradigm's
  counterpart of retraining: decide which commitment gives way, revise it,
  and re-check what depended on it. The edit is local; its consequences
  need not be, and one revision changing several later decisions is the
  point. Reconciliation is where the costs of [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate.
- **Fewer observations.** A correct theory says which new cases matter. In
  the exporter case, one discovered dependency changed the checking
  decision for several files. The conjecture that [theory refinement
  improves sample efficiency under structured
  shifts](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names. Fewer
  observations need not mean lower total cost once theory construction and
  maintenance are counted.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. Reverting still needs a
  dependency check, because later changes may rely on it; legibility means
  the dependents can be found, not that there are none. A learner confined to [a fixed decomposition inherits that
  decomposition's
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  a learner that can rewrite its own representations and tools has more
  room to repair.

## Idea 5: fixed weights as a control

Fixing the weights is an experimental condition, not a recommendation for
mature systems. It rules out parameter updates as the source of an
improvement. It does not by itself credit the improvement to retained
state: a different task mix, more computation, a human intervention, or
run-to-run variation could each explain a gain. Attribution needs matched
comparisons with the retained change removed.

Testing runs at two levels that do not substitute for each other. The three
attractions are claims about a mechanism, tested in bounded components:
matched runs that vary what is retained and measure influence, transfer,
and observations used. The main hypotheses are claims about a whole
system's performance under external assessment. The
[evidence supplement](./testing-the-theory-refinement-program.md) specifies
both levels. The whole-system hypotheses are three.

- **Sufficiency.** A learning methodology written in prose and code is
  enough for a computational builder on fixed public models to develop,
  retain, and use theories across declared areas, to a reliability target
  under a stated budget and external assessment. Refuted by a builder that
  needs people in inside roles, or a new learning method per area.
- **Comparison.** Under matched demands and resources, the methodology
  gains capability over its frozen seed and over a baseline that searches
  the raw records without it, and its reliability is within a preset margin
  of a human-staffed builder's. Refuted by matched runs in which the
  controls do as well.
- **Reflection.** A builder whose machinery changes pass through a causally
  connected self-theory gains capabilities beyond its seed that a matched
  builder without one does not. Better outcomes alone do not test this; the
  records of a reflective episode against a matched non-reflective builder
  do.

The hypotheses are tested through an *externally tested* builder, one that
receives three things from outside: a falsifier (failures it does not judge
itself), an objective, and an outcome level independent of its own
evaluators. Where a claim lacks that external assessment, [the builder owes
three things
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level for
changing an objective, and attribution when it asserts a cause. This setup
is a first design, not yet exercised.

## The first arrangement

The first proposed arrangement is Commonplace, a framework for knowledge
bases operated by agents. Commonplace would produce a knowledge base and
its supporting software for a consuming project, whose agents use it on
their tasks and whose judges accept or reject the work; those judgments are
the external falsifier and objective. Commonplace would revise the product
and, when a failure exposed a limit in its own methods, those methods too.
People still perform several inside roles today; how those roles would move
to computation is the [bootstrap
supplement's](./bootstrapping-the-first-automated-software-house.md)
subject. No consuming-project run has been performed.

An alternative takes software as the product: an automated software house
whose theory is Naur's program theory of the software it maintains.
Software fails visibly, which gives a stronger falsifier, at the price of a
harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Open questions

- What support licenses each kind of reliance on a retained theory:
  guiding an experiment, routine use, compilation into a test.
- Whether current models interpret prose theories consistently enough for
  diagnosis and repair, not only application.
- How to assign credit when a later failure could lie in the theory, the
  retrieval that never surfaced it, the evaluator that admitted a change,
  or a skipped check.

## Five ideas to take away

1. **Theory refinement.** Learn by revising the part of an explicit theory
   that a failure points to, and keep the rest.
2. **Addressable theories.** Refinement works on theories with
   contradictable consequences and separately editable parts; prose
   theories qualify, and parts move into code as they settle.
3. **Prefer reach.** Among revisions that fit a failure, choose the one
   that also handles cases the failure did not show.
4. **The deployed system is the learner.** With weights fixed, learning
   lives in retained theories, tools, tests, and the update process, and
   the theory builder is defined by roles.
5. **Fixed weights as a control.** Holding weights fixed isolates the
   mechanism under study; attributing a gain still needs matched
   comparisons and external assessment.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state
the terms with their boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the protocol, and the component experiments. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions.
[Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery, and what that does and does not establish.
