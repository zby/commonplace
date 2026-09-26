---
description: "Lead article: theory refinement with fixed model weights as a learning paradigm, its departures from classical refinement, its conjectured attractions, and an outline of the theory builder, hypotheses, and first arrangement"
type: kb/articles/types/article.md
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
records or summaries of experience without an explanation. The article
leaves the reader with five ideas: **theory refinement** as the learning
operation, **addressable theories** as the shape it needs, **explanatory
reach** as the rule for choosing among repairs, the **theory builder** as
the unit that learns, and **fixed weights as an experimental condition**.
The paradigm's attractions, continual learning, fewer observations, and
legibility, are conjectures. No test has been run.

## A case

A system maintains a release exporter that builds a deployment manifest from
a configured list of input files. The system retains a short written account
of which edits need a manifest check, in two parts: an edit needs a manifest
check when an executable consumer reads the edited file, and the configured
input list identifies every file the exporter reads. Documentation edits
therefore get a syntax check only.

Later the exporter starts reading service definitions from named Markdown
files, which are added to the configured list. The account already says what
to do: those files now have an executable consumer, so their edits need
manifest checks. No new rule was written.

Later still, the exporter gains included snippets. A snippet that no
configured file names, but that a configured file includes, carries a
service definition. An edit to it passes its syntax check, and a release
ships with an invalid manifest. The account's second part has failed: the
configured list names the exporter's entry points, not everything it reads.
The system revises that part only: the inputs are the configured files plus
whatever they reach through includes. The first part stands. The system then
applies the revised account to snippets it has not touched.

The case shows three things. A written account guided a decision on a case
it did not mention. A failure contradicted one part of the account, and only
that part was revised. And the revision was chosen for what else it would
handle, not only for the failure that caused it. The first two are theory
refinement on an addressable theory; the third is explanatory reach.

## Idea 1: theory refinement

[Theory refinement](../notes/definitions/theory-refinement.md) is the
learning operation that revises an existing explicit theory against
empirical cases, correcting its errors while preserving what was right,
instead of learning from scratch. The name comes from Ourston, Richards, and
Mooney in the early 1990s, whose systems traced a wrong consequence of
expert-supplied logical rules to its source and edited that part.

The theory is a [tentative
theory](../notes/definitions/theory-refinement.md#tentative-theory) in Karl
Popper's sense: put forward as a solution, held open to criticism, and never
promoted to settled truth by surviving tests. How much support a theory needs
before the system relies on it routinely is a policy the system has to set.

The paradigm keeps the operation and changes its setting in three ways. Each
is our departure, not a claim of the classical work.

- **The interpreter is a language model, so the theory can be prose.** A
  fixed model can apply and revise an account nobody has formalized, so a
  theory can enter the loop before anyone writes a checker for it. The cost
  is that whether a case contradicts a prose theory is itself a reading, and
  two readings can differ. Compiling a part into a validator or test makes
  its consequences mechanically checkable, which gains checkability, not
  certainty: the check may still misrepresent the theory.
- **The theory is partly normative.** A commitment such as "every query must
  respect the active tenant" is a rule the system keeps true, not only a
  hypothesis. A failure can be resolved by changing the product to fit the
  theory or the theory to fit the evidence. Descriptive assumptions are the
  system's to revise; a requirement supplied from outside is not, because
  weakening it would make the failure disappear without improving anything.
- **The theory may be about the system itself.** The account of which
  checks to run is part of the system's own production machinery. When the
  same loop revises how the system builds, tests, and revises its theories,
  the loop is *reflective*.

## Idea 2: addressable theories

Refinement needs a theory of a particular shape. It must have consequences a
case can contradict, parts that a failure can point at as repair locations,
and parts that can be edited separately. A theory with these properties is
*addressable*. The exporter account is: it predicted which edits
needed which checks, the failure pointed at its assumption that the input
list was exhaustive, and that assumption was revised on its own. A record of
past cases with no stated reasons gives a failure nothing to point at.

## Idea 3: explanatory reach

Several revisions usually fit a failure. The paradigm prefers the one with
more explanatory reach: the one that would also handle cases the failure did
not show. That is why the case revises the account of what the exporter
reads instead of adding an exception for one snippet. The revised explanation
also changes decisions about snippets nobody has edited yet.

## Idea 4: the theory builder is what learns

With weights fixed, [retrieval, scheduling, tools, and validators jointly
determine behaviour](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md),
so the unit that learns is the whole deployed system, not the model. What it
retains includes theories, tests, tools, evaluators, and the update process
itself. When a new theory needs a check the system cannot yet
perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and that capacity has to persist outside the model.

We call this system a [theory builder](../notes/definitions/theory-builder.md):
the complete persistent system responsible for developing and revising
tentative theories about the subjects it is asked to investigate. Its
boundary follows roles, not substrate. Whoever supplies questions, cases,
and acceptance judgments is outside. Whoever interprets a theory, chooses
what to blame, produces or selects a revision, or repairs the machinery is
inside, person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when its
machinery changes pass through a theory of its own machinery. The two
conditions are independent.

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation outperform methods built from human knowledge, and written
theories look like hand-crafted structure. The answer turns on [how the structure is
produced, not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here computation forms and revises the theories, builds the tools, and
selects changes from evidence; people build only the seed the system starts
from. That is compatibility, not a scaling advantage: search over retained
artifacts may scale badly, and adapting weights may be cheaper. The program
has to run those comparisons.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that contradicts the theory forces a reconciliation: decide which
  commitment gives way, revise it, re-check what depended on it. The edit is
  local; its consequences need not be, and that spread is the point.
  Reconciliation is where the
  costs of [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate: admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter: in
  the case, one discovered dependency changed the checking decision for
  several files. The conjecture that [theory refinement improves sample
  efficiency under structured
  shifts](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names, and
  fewer observations need not mean lower total cost.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. A rollback still needs a
  dependency check; what legibility buys is that the target and its
  dependents can be found. A learner confined to [a fixed decomposition
  inherits its
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  one that can rewrite its own representations can repair more. Legibility
  does not guarantee that the model uses the retained state faithfully.

## Idea 5: fixed weights as an experimental condition

Fixing the weights rules out parameter updates as the source of any
improvement, which isolates learning through retained state. It does not by
itself attribute an improvement to retained state: a different task mix,
more computation, a human intervention, or run-to-run variation could each
explain a gain. Attribution needs matched comparisons with the retained
change removed. Fixing weights is not a claim that learning outside weights
is generally better.

The three attractions are tested in bounded components: matched runs that
vary what is retained and measure influence, transfer, and observations
used. The program's main hypotheses are about a whole system under external
assessment. Neither level substitutes for the other. The
[evidence supplement](./testing-the-theory-refinement-program.md) specifies
both. The three whole-system hypotheses are:

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

They are tested through an *externally tested* builder, one that
receives from outside a falsifier (failures it does not judge itself), an
objective, and an outcome level independent of its own evaluators. Where a
claim lacks that external assessment, [the builder owes three things for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level for
changing an objective, and attribution when it asserts a cause. The setup is
a first design, stated but not exercised.

## The first arrangement

The first arrangement proposed for testing is Commonplace, a framework for
knowledge bases operated by agents. In the proposed run, Commonplace
produces a knowledge base and its supporting software for a consuming
project. Agents in that project use the knowledge base on their tasks, and
the project's own judges accept or reject the work; those judgments are the
external falsifier and objective. Commonplace would revise the delivered
product and, when a failure exposed a limit in its methods, those methods.
People still perform several inside roles, so it is a
human-inclusive builder; the [bootstrap
supplement](./bootstrapping-the-first-automated-software-house.md) takes up
how those roles would transfer to computation. No consuming-project run has
been performed.

A different arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. Software fails visibly, which gives a stronger falsifier, at the
price of a harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Open questions

- What support licenses each kind of reliance on a retained theory: guiding
  an experiment, routine use, compilation into a test.
- Whether current models interpret prose theories consistently enough for
  diagnosis and repair, not only application.
- How to assign credit when a later failure could lie in the theory, the
  retrieval that never surfaced it, the evaluator that admitted a change, or
  a skipped check.
- Whether total cost, with theory maintenance counted, compares well with
  adapting weights on the same evidence.

## Five ideas to carry away

1. **Theory refinement.** Learn by revising the failing part of an explicit,
   tentative theory and keeping the rest, rather than relearning.
2. **Addressable theories.** Refinement works only on theories whose
   consequences can be contradicted and whose parts a failure can point at
   and edit separately.
3. **Explanatory reach.** Among repairs that fit a failure, prefer the one
   that also changes decisions on cases the failure did not show.
4. **The theory builder learns, not the model.** With weights fixed, the
   whole deployed system, its theories, tools, evaluators, and update
   process, is what learns, and its boundary follows roles.
5. **Fixed weights as an experimental condition.** Holding weights fixed
   isolates learning through retained state; attributing a gain to it still
   needs matched comparisons and external assessment.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state
the terms with their exclusions and boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the first arrangement's protocol, and the component
experiments.
[Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions.
[Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery.
