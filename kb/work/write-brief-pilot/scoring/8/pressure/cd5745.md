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

**TL;DR.** We propose a way for systems built around large language models
to learn: hold the model weights fixed, and let the system refine written
theories that it keeps outside the model and consults on later work. This is
*theory refinement*, an established learning operation, moved into a new
setting, and an alternative to adapting weights or storing raw records of
experience. We conjecture that it learns continually, from fewer
observations, in a form that can be inspected and rolled back piece by
piece. This article states the paradigm and five ideas to keep from it.
Supplements say how it would be tested. No test has been run.

## A case

A system maintains a release exporter, which builds a deployment manifest
from a configured list of input files. The system retains a short written
account of which edits need a manifest check, in two parts: an edit needs a
manifest check when an executable consumer reads the edited file, and the
configured input list names every file the exporter reads. Documentation
edits therefore get a syntax check only.

Later the exporter starts reading service definitions from Markdown files
added to the configured list. The account already covers this: those files
now have an executable consumer, so their edits need manifest checks. No new
rule was written. An existing explanation was applied to a new fact.

Later still, the exporter gains included snippets. A snippet that no
configured file names, but that a configured file includes, carries a
service definition. An edit to it passes its syntax check, and a release
ships with an invalid manifest. The account's second part has failed: the
list names the exporter's entry points, not everything it reads. The system
revises that part only: the inputs are the configured files plus whatever
they include. The first part stands. The system then applies the revised
account to other snippets it has not touched.

Three things happened. A written account decided a case it did not
mention. A failure pointed at one part, and only that part was revised. The
revision was chosen for what else it would handle, not only for the failure.
These three are the core of the paradigm.

## Theory refinement, and what is new here

[Theory refinement](../notes/definitions/theory-refinement.md) revises an
existing explicit theory against cases, correcting errors while keeping
what was right. The name comes from Ourston, Richards, and Mooney in the
early 1990s, whose systems took expert-supplied logical rules, traced a
wrong consequence on a labelled example to the rule that produced it, and
edited that rule.

The operation needs a theory of a particular shape. It must have
consequences a case can contradict, parts a failure can point at, and parts
that can be edited separately. We call such a theory **addressable**. The
exporter account is addressable: it predicted which edits needed which
checks, the failure pointed at its assumption about the input list, and that
assumption was revised alone.

The theory is a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory)
in Karl Popper's sense: put forward as a solution, held open to criticism,
and never promoted to settled truth by surviving tests. That status licenses
nothing by itself; how much support justifies routine reliance is a policy
the system must set.

The paradigm keeps the operation and changes the setting in three ways. These
are our departures, not claims of the classical work.

- **The theory can be prose.** A language model can apply and revise an
  account nobody has formalized, so a theory can enter the loop before anyone
  writes a checker for it. The cost is that consequences are interpreted, not
  computed, and two readings can disagree about whether a case contradicts
  the theory. Compiling settled parts into schemas or tests makes their
  stated consequences mechanically checkable. It does not make the check a
  correct statement of the theory.
- **The theory is partly normative.** A commitment such as "every query must
  respect the active tenant" is a rule the system keeps true, not only a
  prediction. A failure can be resolved by changing the product to fit the
  theory or the theory to fit the evidence, and the system must choose. The
  choice is constrained. Descriptive assumptions and implementation choices
  are the system's to revise. A **requirement supplied from outside** is not:
  weakening it would make a failure disappear without improving anything, so
  it changes only when whoever supplied it renegotiates it.
- **The theory can be about the system itself.** The exporter account is part
  of the system's own production machinery. When the same loop revises how
  the system builds, tests, and revises its theories, the loop is
  *reflective*.

Two further choices belong to the paradigm. First, among revisions that fit
the evidence, prefer the one with more **reach**: the one that would also
handle cases the failure did not show. That is why the case revised what the
exporter reads instead of adding an exception for one snippet. Second, treat
the whole deployed system as what learns, because [retrieval, scheduling,
tools, and validators jointly determine behaviour with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
When a new theory needs a check the system cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and with fixed weights that capacity must persist outside the model.

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation beat methods built from human knowledge. Written theories look
like the hand-built structure it warns against. The answer is to separate **production method from retained form**: [the lesson selects how
structure is produced, not the form it is kept
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here computation forms and revises the theories, builds the tools and
evaluators, and selects changes from evidence. People may build the seed the
system starts from. After that, project-specific structure is learned.

That is compatibility, not a scaling advantage. Search and credit assignment
over retained artifacts may scale badly, and adapting weights on the same
evidence may reach the same competence more cheaply. Those comparisons are
part of the program.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that contradicts the theory forces a reconciliation: decide which
  commitment gives way, revise it, and re-check what depended on it. The edit
  is local; its consequences may spread, and that spread is the point. The
  cost is [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
  admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter; in
  the case, one discovered dependency changed the decision for several
  files. The conjecture that [refinement improves sample efficiency under
  structured
  shifts](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names. Fewer
  observations need not mean lower total cost once theory construction and
  maintenance are counted.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. Later changes may depend on
  it, so a rollback needs the same dependency check as a revision; legibility
  makes the target and its dependents findable, not independent. And since
  a learner confined to [a fixed decomposition inherits its
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md),
  one that can rewrite its own representations has more room to repair.
  Legibility describes the retained state, not whether the model uses it
  faithfully.

## The system that carries the paradigm

A learning paradigm is a claim about a whole system. We call that system a
[theory builder](../notes/definitions/theory-builder.md): the complete
persistent system that develops and revises tentative theories about the
subjects it is asked to investigate. Its boundary follows roles. Whoever
supplies questions, cases, and acceptance judgments is outside. Whoever
interprets a theory, chooses what to blame, produces a revision, or repairs
the machinery is inside, whether person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when changes
to its machinery pass through a theory of that machinery. The two qualifiers
are independent.

## What would test it

**Fixed weights are an experimental condition**, not a recommendation for
mature systems and not a claim that learning outside weights is better.
Fixing them rules out parameter updates as the source of an improvement.
It does not by itself credit retained state: task mix, extra computation, a
human intervention, or run-to-run variation could explain a gain. Credit
needs matched comparisons with the retained change removed.

The program tests at **two levels that do not substitute for each other**.
The three attractions are mechanism claims, tested in bounded components:
matched runs that vary what is retained and measure influence, transfer, and
observations used. The main hypotheses are whole-system claims under external
assessment. Better overall performance would not show that fewer
observations were needed, and a component result would not show that a
whole system reaches a reliability target. The three whole-system
hypotheses:

- **Sufficiency.** A learning methodology written in prose and code is
  enough for a computational builder on fixed public models to develop,
  retain, and use theories across declared areas, to a reliability target
  under a stated budget and external assessment. Refuted by a builder that
  needs people in inside roles, or a new learning method per area, to reach
  the target.
- **Comparison.** Under matched demands and resources, the methodology gains
  capability over its frozen seed and over a baseline that searches the raw
  records without it, and its reliability is comparable to a human-staffed
  builder's within a preset margin. Refuted by matched runs in which the
  controls do as well.
- **Reflection.** A builder whose machinery changes pass through a causally
  connected self-theory gains capabilities beyond its seed that a matched
  builder without one does not. Better outcomes alone do not test this. The
  records of a reflective episode against a matched non-reflective builder
  do.

A finite evaluation supports a bounded claim; no hypothesis promises success
on every problem or budget.

The hypotheses are tested through an *externally tested* builder. It
receives from outside a falsifier (failures it does not judge itself), an
objective, and an outcome level independent of its own evaluators. Where a
claim lacks that external assessment, [the builder owes three things
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level for
changing an objective, and attribution when it asserts a cause. The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both test
levels. The setup has been stated but not exercised, and we expect it to
change before a scored run.

## The first arrangement

The first arrangement proposed for a test is Commonplace, a framework for
knowledge bases operated by agents. In the proposed run, Commonplace produces
a knowledge base and supporting software for a consuming project. Agents in
that project use the knowledge base, and the project's own judges accept or
reject their work; those judgments are the external falsifier and objective.
Commonplace would revise what it delivered and, when a failure exposed a
limit in its methods, those methods too. People still perform several
inside roles, so it is a human-inclusive builder; how those roles would move
to computation is the [bootstrap
supplement's](./bootstrapping-the-first-automated-software-house.md)
subject. No consuming-project run has been performed.

The alternative takes software as the product: an automated software house
whose theory is Naur's program theory of the software it maintains. Software
fails visibly, which gives a stronger falsifier, at the price of a harder
claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Five ideas to take away

1. **Addressability.** Refinement needs a theory whose consequences can be
   contradicted and whose parts can be blamed and edited separately.
2. **Reach.** Among revisions that fit the evidence, prefer the one that also
   handles cases the failure did not show.
3. **Requirements supplied from outside.** A partly normative theory can fail
   by the product or by the theory, but the system may not weaken a
   requirement someone else supplied.
4. **Production method versus retained form.** The Bitter Lesson constrains
   how structure is produced, not whether it is kept as readable text.
5. **Fixed weights as an experimental condition.** Holding weights fixed
   isolates retained state as the mechanism under study, and mechanism-level
   and whole-system tests answer different questions.

## Open questions

- Whether current models interpret prose theories consistently enough for
  diagnosis and repair, not only application.
- How to assign credit when a failure could lie in the theory, the retrieval
  that missed it, the evaluator that admitted a change, or a skipped check.
- Whether total cost, with theory maintenance counted, compares well with
  adapting weights on the same evidence.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions give the
terms with their boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the tests.
[Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions.
[Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery.
