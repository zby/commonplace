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

**TL;DR.** We propose a way for systems built around large language models to
learn: hold the model weights fixed, and let the system learn by refining
written theories that it keeps outside the model and consults on later work.
A theory here is an explicit, revisable account of some subject that guides
the system's decisions. This is *theory refinement*, an established learning
operation, in a new setting. The alternatives are adapting the weights, and
retaining records of experience without an explanation. The paradigm may
offer continual learning, learning from fewer observations, and learned state
that can be inspected and rolled back piece by piece; each is a conjecture.
This article states the paradigm, the system that would carry it, and the
hypotheses that would test it. No test has been run.

## A case

A system maintains a release exporter, which builds a deployment manifest
from a configured list of input files. The system checks documentation edits
for syntax only, because they do not affect the manifest. It retains a short
written account of why, in two parts: an edit needs a manifest check when an
executable consumer reads the edited file, and the configured input list
identifies every file the exporter reads.

Later the exporter starts reading service definitions from named Markdown
files, which are added to the configured list. The account already says what
to do: those files now have an executable consumer, so their edits need
manifest checks. No new rule was written.

Later still, the exporter gains included snippets. A snippet that no
configured file names, but that a configured file includes, carries a service
definition. An edit to it passes its syntax check, and a release ships with an
invalid manifest. The account's second part has failed: the configured list
names the exporter's entry points, not everything it reads. The system
revises that part only, to say the inputs are the configured files plus
whatever they include, and applies it to snippets it has not touched. The
first part stands.

Three things happened. A written account guided a decision on a case it did
not mention. A failure contradicted one part of the account, and only that
part was revised. And the revision was chosen for what else it would handle,
not only for the failure that caused it. The rest of the article argues that
these three things can carry a learning paradigm.

## Theory refinement, and what is new here

[Theory refinement](../notes/definitions/theory-refinement.md) revises an
existing explicit theory against cases, correcting its errors while keeping
what was right, instead of learning from scratch. The name comes from the work
of Ourston, Richards, and Mooney in the early 1990s, whose systems traced a
wrong consequence of expert-supplied logical rules to its source and edited
that rule.

The operation needs a theory of a particular shape. The theory must have
consequences a case can contradict, parts a failure can point at, and parts
that can be edited separately. We call such a theory **addressable**. The
exporter account is addressable: it predicted which edits needed which
checks, the failure pointed at its assumption about the input list, and that
assumption was revised on its own.

The theory is also a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory)
in Karl Popper's sense: held open to criticism however many tests it
survives. How much support it needs before the system relies on it
routinely is a policy the system has to set.

The paradigm keeps the operation and changes its setting in three ways. These
are our departures, not claims of the classical work.

- **The interpreter is a language model, so the theory can be prose.** The
  classical systems could refine only theories in the one form their
  procedures handled. A fixed language model can be asked to apply and revise
  an account nobody has formalized, so a theory can enter the loop before
  anyone writes a checker for it. The cost is that whether a case
  contradicts a prose theory is itself a reading, and two readings can
  differ. Refinement moves parts into schemas, validators, or tests as they
  settle, which makes their stated consequences mechanically checkable,
  though not certainly correct.
- **The theory is partly normative.** A commitment such as "every query must
  respect the active tenant" is a rule the system keeps true, so a failure
  can be fixed by changing the product or the theory. Descriptive assumptions
  are the system's to revise. A requirement supplied from outside, such as
  tenant isolation, is not: weakening it would hide a failure without
  improving anything.
- **The theory may be about the system itself.** The account of which checks
  to run is part of the system's own production machinery. When the same loop
  revises how the system builds, tests, and revises its theories, the loop is
  *reflective*.

Two further choices are the paradigm's own. The first is **revision by
reach**: among revisions that fit the evidence, prefer the one that would also
handle cases the failure did not show. That is why the exporter account was
revised to cover included files instead of gaining an exception for one
snippet. The second is that **the system is the learner**: the whole deployed
system learns, not the model, because [retrieval, scheduling, tools, and
validators jointly determine behaviour with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
What it retains includes theories, procedures, tests, tools, and
evaluators. When a new theory needs a check the system cannot yet perform,
[the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md).

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation beat methods built from human knowledge, and written theories
look hand-crafted. The answer turns on
[how the structure is produced, not the form it is kept
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here computation forms and revises the theories, builds the tools and
evaluators, and selects changes from evidence. People may build the seed, the
theories and machinery the system starts from; after that, project-specific
structure is learned. This shows compatibility, not a scaling advantage;
adapting weights on the same evidence may still be cheaper.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that fits the current theory is written down and takes effect. A fact
  that contradicts it forces a reconciliation: decide which commitment gives
  way, revise it, and re-check what depended on it. This is the paradigm's
  counterpart of retraining: a local edit whose consequences can reach
  several later decisions. Reconciliation is also where the costs of
  [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate: admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter. In the
  exporter case, one discovered dependency changed the checking decision for
  several files. The conjecture that [theory refinement improves sample
  efficiency](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names. Fewer
  observations need not mean lower total cost once theory construction and
  maintenance are counted.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. A rollback still needs a
  dependency check, because later changes may rely on the reverted item;
  legibility means the target and its dependents can be found.

## The theory builder

Because the system is the learner, questions about the paradigm are
questions about a whole system. We call that system a [theory
builder](../notes/definitions/theory-builder.md): the persistent system that
develops and revises tentative theories about the subjects it is asked to
investigate. Its boundary follows roles. Whoever supplies questions, cases,
and acceptance judgments is outside. Whoever interprets a theory, chooses
what to blame, produces a revision, or repairs the machinery is inside,
person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when changes
to its machinery pass through a theory of its own machinery. The two
properties are independent.

The program's central conjecture is that a theory builder on fixed public
models can learn this way: its capability can improve over time through
revised retained theories alone.

## What would test it

**Fixed weights are an experimental condition**, not a recommendation for
mature systems. Fixing them rules out parameter updates as the source of any
improvement. It does not by itself credit an improvement to retained state: a
different task mix, more computation, a human intervention, or run-to-run
variation could each explain a gain. Attribution needs matched comparisons
with the retained change removed.

The three attractions are tested in bounded components: matched runs that
vary what is retained. The main hypotheses are claims about a whole system
under external assessment, and neither level substitutes for the other. The
program states three whole-system hypotheses, each with what would refute
it.

- **Sufficiency.** A learning methodology written in prose and code is enough
  for a computational builder on fixed public models to develop, retain, and
  use theories across declared areas, to a reliability target under a stated
  budget and external assessment. Refuted by a builder that needs people in
  inside roles, or a new learning method per area, to reach the target.
- **Comparison.** Under matched demands and resources, the methodology gains
  capability over its frozen seed and over a baseline that searches the raw
  records without it, and its reliability comes within a preset margin of a
  human-staffed builder's. Refuted by matched runs in which the controls do as
  well.
- **Reflection.** A builder whose machinery changes pass through a causally
  connected theory of itself gains capabilities beyond its seed that a
  matched builder without one does not. Better outcomes alone do not test
  this; the records of a reflective episode against a matched non-reflective
  builder do.

Each hypothesis claims success within a finite evaluation, not on every
problem or budget. They are tested through an *externally tested* builder:
one that receives from outside an objective, failures it does not judge
itself, and an outcome level independent of its own evaluators. Where a claim
lacks that external assessment, [the builder must supply its own rules for
contradiction, comparison, and attribution](../notes/a-claim-without-external-assessment-carries-three-obligations.md).
This setup is a first design, stated but not exercised, and we expect it to
change before any scored run. The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both levels.

## The first arrangement

The first arrangement proposed for testing the paradigm is Commonplace, a
framework for knowledge bases operated by agents. In the proposed run,
Commonplace produces a knowledge base and its supporting software for a
consuming project. Agents in that project use the knowledge base on their
tasks, and the project's own judges accept or reject the work; those
judgments supply the external objective and failures. Commonplace would
revise the delivered knowledge base, and, when a failure exposed a limit in
its own methods, revise those too. People still perform several inside roles
today, so it is a human-inclusive builder. How those roles would move to
computation is the subject of the [bootstrap
supplement](./bootstrapping-the-first-automated-software-house.md). No
consuming-project run has been performed.

A different arrangement takes software as the product: an automated software
house whose theory is Naur's program theory of the software it maintains.
Software fails visibly, so it offers a stronger source of failures, at the
price of a harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md) develops
it and compares the two.

## Open questions

- What support licenses each kind of reliance on a retained theory: guiding
  an experiment, routine use, compilation into a test.
- Whether current models read prose theories consistently enough for
  diagnosis and repair, not only for application.
- How to assign credit when a later failure could lie in the theory, the
  retrieval, or the evaluator.
- Whether the paradigm's total cost, with theory maintenance counted,
  compares well with adapting weights on the same evidence.

## Five ideas to take away

- **Addressable theory.** Refinement needs a theory with consequences a case
  can contradict and parts that can be blamed and edited separately.
- **Revision by reach.** Among fixes that fit a failure, prefer the one that
  handles cases the failure did not show.
- **The system is the learner.** With weights fixed, learning lives in the
  retained theories, procedures, tools, and evaluators of the deployed system.
- **The theory builder.** The whole system that develops and revises
  theories, with its boundary drawn by roles, not by what is a model.
- **Fixed weights as an experimental condition.** Holding the model fixed
  isolates learning through retained state; matched comparisons still have
  to attribute any gain to it.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state the
terms with their boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the external assessment, and the first arrangement's protocol.
[Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems.
