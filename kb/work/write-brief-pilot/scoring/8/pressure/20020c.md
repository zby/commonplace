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
  - kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
---
# Learning by Theory Refinement with Fixed Models

*A research program for systems that learn outside their weights*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** Systems built around language models usually learn by adapting
weights or by retaining raw records of experience. We propose a third way:
hold the weights fixed and let the system refine written theories that it
retains and consults on later work. This is *theory refinement*, an
established learning operation, in a setting where a language model
interprets the theory. Its three attractions are conjectures: learning is
continual, it may need fewer observations, and what is learned can be
inspected and rolled back piece by piece. This article states the paradigm
and five ideas it rests on; supplements say how it would be tested. No test
has been run.

## A case

A system maintains a release exporter, which builds a deployment manifest
from a configured list of input files. The system checks documentation
edits for syntax only, and it retains a two-part account of why: an edit
needs a manifest check when an executable consumer reads the edited file,
and the configured input list identifies every file the exporter reads.

Later the exporter starts reading service definitions from named Markdown
files, which are added to the configured list. The account already says
what to do: those files now have an executable consumer, so their edits
need manifest checks. No new rule was written. An existing explanation was
applied to a new fact.

Later still, the exporter gains included snippets. A snippet that no
configured file names, but that a configured file includes, carries a
service definition. An edit to it passes its syntax check, and a release
ships with an invalid manifest. The account's second part has failed: the
configured list names the exporter's entry points, not everything it reads.
The system revises that part only: the inputs are the configured files plus
whatever they reach through includes. The first part stands. The system
then applies the revised account to snippets it has not touched.

Three things happened. The account guided a decision on a case it did not
mention. A failure pointed at one part, and only that part was revised. The
revision was chosen for what else it would handle, not only for the failure
that caused it. These three things are the core of the paradigm.

## Theory refinement, and what is new here

[Theory refinement](../notes/definitions/theory-refinement.md) revises an
existing explicit theory against cases, correcting its errors while keeping
what was right, instead of learning from scratch. The name comes from
Ourston, Richards, and Mooney in the early 1990s. Their theory was a set of
logical rules supplied by an expert, and their cases were labelled
examples. Their systems derived consequences from the rules, traced a wrong
consequence to its source, and edited that part.

The operation needs a theory of a particular shape. The theory must have
consequences a case can contradict, parts a failure can point at, and parts
that can be edited separately. We call a theory with these properties
**addressable**. The exporter account is addressable: it predicted which
edits needed which checks, the failure pointed at its assumption about the
input list, and that assumption was revised on its own.

The theory is a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory)
in Karl Popper's sense: put forward as a solution, held open to criticism,
and never promoted to settled truth by surviving tests. The status licenses
nothing by itself; how much support justifies relying on a theory is a
policy the system has to set.

The paradigm keeps the operation and changes the setting in three ways.
These departures are ours, not claims of the classical work.

- **The interpreter is a language model, so the theory can be prose.** The
  classical systems refined theories only in one formal language. A
  language model can apply and revise an unformalized account, so a theory
  can enter the loop before anyone writes a checker for it. The cost is
  that consequences are interpreted, not computed: whether a case
  contradicts a prose theory is itself a reading, and two readings can
  differ. As parts settle, refinement compiles them into schemas,
  validators, or tests, which gains checkability, not certainty.
- **The theory is partly normative.** A commitment such as "every query
  must respect the active tenant" is a rule the system keeps true, so a
  failure can be resolved by changing the product or by revising the
  theory. Descriptive assumptions and implementation choices are the
  system's to revise. **Requirements supplied from outside are not.**
  Weakening tenant isolation would hide a failure without improving
  anything; such a requirement changes only when its supplier renegotiates
  it.
- **The theory may be about the system itself.** The account of which
  checks to run is part of the system's own machinery. When the same loop
  revises how the system builds, tests, and revises its theories, the loop
  is *reflective*.

Two further choices belong to the paradigm. First, among revisions that fit
the evidence, prefer the one with more **reach**: the one that would also
handle cases the failure did not show. That is why the exporter account was
revised to cover includes instead of gaining an exception for one snippet.
Second, treat the whole deployed system as the unit that learns, because
[retrieval, scheduling, tools, and validators jointly determine behaviour
with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
When a new theory needs a check the system
cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md).

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation outperform methods built from human knowledge, and written
theories look like hand-crafted structure. The answer
is that the lesson selects [**production methods, not retained
forms**](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
In this paradigm, computation forms and revises the theories, builds tools
and evaluators, and selects changes from evidence. People may build the
seed the system starts from. After that, project-specific structure is a
learned product.

That makes the paradigm compatible with the lesson, not favoured by it.
Search and credit assignment over retained artifacts may scale badly, and
adapting weights on the same evidence may reach the same competence at
lower cost. Those comparisons are part of what the program has to run.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that contradicts the theory forces a reconciliation: decide which
  commitment gives way, revise it, and re-check what depended on it. The
  edit is local; its consequences may spread to several later decisions,
  which is the point. The cost is
  [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
  admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter. In
  the exporter case, one discovered dependency changed the checking decision
  for several files. The conjecture that [theory refinement improves sample
  efficiency](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  holds only for shifts that preserve the structure the theory names, and
  fewer observations need not mean lower total cost once theory
  construction and maintenance are counted.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. Reverting it still needs a
  dependency check, because later changes may rely on it; legibility makes
  the target and its dependents findable, not independent. It describes
  the retained state and does not guarantee that the model uses that state
  faithfully.

## The system that carries the paradigm

We call the system a [theory builder](../notes/definitions/theory-builder.md):
the complete persistent system that develops and revises tentative theories
about the subjects it is asked to investigate. Its boundary follows roles.
Whoever supplies questions, cases, and acceptance
judgments is outside. Whoever interprets a theory, chooses what to blame,
produces a revision, or repairs the machinery is inside, person or program.
A builder is [autonomous](../notes/definitions/autonomous-theory-builder.md)
when computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when changes
to its machinery pass through a theory of that machinery. The two
qualifiers are independent.

## What would test it

Fixed weights are an experimental condition, not a recommendation for
mature systems. Fixing them rules out parameter updates as the source of an improvement. It
does not by itself credit retained state: a different task mix, more
computation, a human intervention, or run-to-run variation could explain a
gain. Attribution needs matched comparisons with the retained change
removed.

Tests run at two levels that do not substitute for each other. The three
attractions are mechanism claims, tested in bounded components by matched
runs that vary what is retained. Better overall performance would not show
that fewer observations were needed, and a component result would not show
that a whole system reaches a reliability target. At the whole-system
level, under external assessment, the program states three hypotheses.

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
  matched builder without one does not. Better outcomes alone do not test
  this. The records of a reflective episode against a matched
  non-reflective builder do.

Each hypothesis is a bounded claim about a finite evaluation, not a promise
of success on every problem.

The hypotheses are tested through an *externally tested* builder. It
receives three things from outside: a falsifier (failures it does not judge
itself), an objective, and an outcome level independent of its own
evaluators. With those supplied, outcomes can be compared before the
builder has settled how much support its internal theories need. Where a
claim lacks that assessment, [the builder owes three things for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for contradiction and support, a comparison level for changing an
objective, and attribution when it asserts a cause. The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both
levels. The setup is a first design, stated but not exercised, and we
expect it to change before a scored run.

## The first arrangement

The first arrangement proposed for testing is Commonplace, a framework for
knowledge bases operated by agents. In the proposed run, Commonplace
produces a knowledge base and supporting software for a consuming project
whose agents use it and whose own judges accept or reject the work; those
judgments are the external falsifier and objective. Commonplace would
revise the product and, when a failure exposed a limit in its own methods,
those methods too. People still perform several inside roles, so it is a
human-inclusive builder; the [bootstrap
supplement](./bootstrapping-the-first-automated-software-house.md) asks how
those roles would pass to computation. No consuming-project run has been
performed.

The alternative arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. Software fails visibly, which gives a stronger falsifier, at the
price of a harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Open questions

Beyond the hypotheses, three questions stay open. Does a succession of
revisions, each justified by its own evidence, compose into a justified
lineage? What support licenses each kind of reliance on a retained theory,
from guiding an experiment to compilation into a test? And do current
models interpret prose theories consistently enough for diagnosis and
repair, not only for application?

## Five ideas to take away

- **Theory refinement with fixed weights.** Learn by revising retained,
  explicit, tentative theories that a fixed model interprets.
- **Addressability.** Refinement needs theories whose consequences can be
  contradicted and whose parts a failure can point at and edit separately.
- **Reach.** Prefer the revision that also handles cases the failure did
  not show.
- **Requirements supplied from outside are not the system's to weaken.**
  Repair the product or a descriptive assumption, not the requirement.
- **Production method, not retained form.** The Bitter Lesson judges how
  structure is produced, so learned written theories are compatible with
  it.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions give
the terms with their boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the first arrangement's protocol, and component experiments
built on the exporter case. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen systems against the software-house conditions, and
[transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) examines
the requirement that every change to a builder arise through its own
machinery.
