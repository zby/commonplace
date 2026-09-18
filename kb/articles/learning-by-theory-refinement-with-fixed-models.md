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
later work. What is learned is a *tentative theory*, an explicit and revisable
account of some subject that guides the system's decisions. Experience refines
the theory; the refined theory guides later work. This is *theory refinement*,
an established learning operation, in a new setting. The paradigm is
attractive on three counts, each still a conjecture: learning is continual,
it may need fewer observations, and what is learned can be inspected and
rolled back piece by piece. This article states the paradigm. The supplements
state how it would be tested, and the first system that would test it. No
test has been run.

## A case

Consider a system that maintains a release exporter. The exporter builds a
deployment manifest from a configured list of input files. Documentation
edits do not affect the manifest, so the system checks them for syntax
only. The system retains a short written account of why, in two parts: an
edit needs a manifest check when an executable consumer reads the edited
file, and the configured input list identifies every file the exporter
reads.

Later the exporter starts reading service definitions from named Markdown
files, and those files are added to the configured list. The retained
account already says what to do: those files now have an executable
consumer, so their edits need manifest checks. No new rule was written. An
existing explanation was applied to a new fact.

Later still, the exporter gains support for included snippets. A snippet
that no configured file names directly, but that a configured file
includes, carries a service definition. An edit to it passes its syntax
check, and a release ships with an invalid manifest. The account's second
part has failed: the configured list identifies the exporter's entry
points, not everything it reads. The system revises that part, and only
that part: the exporter's inputs are the configured files plus whatever
they reach through includes. The first part, that checks follow executable
consumers, stands. The system then applies the revised account to other
snippets it has not touched.

Three things happened. A written account guided a decision on a case it
did not mention. A failure contradicted one part of the account, and that
part was revised rather than the whole account replaced. The revision was
chosen for what else it would handle, not only for the failure that caused
it. The rest of this article says why those three things are the core of a
learning paradigm.

## Theory refinement, and what is new here

[Theory refinement](../notes/definitions/theory-refinement.md) is the
learning operation that revises an existing explicit theory against
empirical cases, correcting its errors while preserving what was right,
instead of learning from scratch. The name comes from the work of Ourston,
Richards, and Mooney in the early 1990s, where the theory was a set of
logical rules supplied by an expert and the cases were labelled examples. Their systems derived consequences from the rules, found where a
wrong consequence came from, and edited that part.

The operation needs a theory of a particular shape. It must have
consequences a case can contradict. It must have parts that a failure can
point at as candidate repair locations. And those parts must be editable
separately. A theory with these properties is *addressable*. The account in
the case above is addressable: it predicted which edits needed which
checks, the failure pointed at its exhaustiveness assumption, and that
assumption was revised on its own.

We call the theory a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory),
in Karl Popper's sense: put forward as a solution, held open to criticism,
and never promoted to a settled truth by surviving tests. The status
licenses nothing by itself. How much support a theory needs before the
system relies on it routinely, or compiles it into a test, is a policy the
system has to set.

The paradigm keeps the operation and changes the setting in three ways.
Each is our departure, not something the classical work claims.

- **The interpreter is a language model, so the theory can be prose.** The
  classical systems could only refine theories written in the one form
  their procedures handled. A fixed language model can be given an account
  that has not been formalized and asked to apply and revise it, so a
  theory can enter the loop before anyone has written a checker for it.
  Whether the model does this reliably is one of the open questions at the
  end.

  The cost is that consequences are interpreted rather than computed.
  Whether a case contradicts a prose theory is itself a reading, and two
  readings can differ. Compiling a part into a schema, validator, or test
  makes its specified consequences mechanically checkable, which removes
  that disagreement for those consequences. It does not remove the
  questions of whether the check represents the theory correctly or
  measures the right property. Prose can also make a prediction clear
  enough that an observation plainly contradicts it. Refinement moves parts
  across the line into code as they settle, and gains checkability, not
  certainty, by doing so.
- **The theory is partly normative.** The account in the case is not only
  a hypothesis about the exporter. A commitment such as "every query must
  respect the active tenant" is a rule the system keeps true. A failure can
  therefore be resolved by changing the product to fit the theory as well
  as by revising the theory to fit the evidence, and the system must decide
  which. That choice has a constraint. Descriptive assumptions, such as
  what the configured list identifies, and implementation choices are the
  system's to revise. A requirement supplied from outside, such as tenant
  isolation, is not: weakening it would make a failure disappear without
  improving anything, and it changes only when whoever supplied it
  renegotiates it. The external objective introduced below is what holds
  that line.
- **The theory may be about the system itself.** The account of which
  checks to run is part of the system's own production machinery. When the
  same loop revises how the system builds, tests, and revises its theories,
  the loop is *reflective*. A system that holds a description of itself
  without that two-way connection is not reflective in this sense.

Two further choices are the paradigm's own. Among revisions that fit the
evidence, prefer the one with more reach, the one that would also handle
cases the failure did not exhibit. That is why the case revises the account of
what the exporter reads instead of adding an exception for one snippet. And treat the
whole deployed system as the unit that learns, because [retrieval,
scheduling, tools, and validators jointly determine behaviour with the
model fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
What the paradigm retains includes theories, procedures, tests, tools,
evaluators, and the update process itself. When a new theory needs a check
the system cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and with weights fixed that capacity has to persist outside the model.

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation beat methods built from human knowledge. Written theories look
like hand-crafted structure, so the objection is natural. The answer turns
on [how the structure is produced, not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
In this paradigm, computation forms and revises the theories, builds the
tools and evaluators, and selects changes from evidence. People may build
the seed, the theories and machinery the system starts from. After that,
project-specific structure is a learned product.

That is compatibility, not a scaling advantage. Search, validation, and
credit assignment over retained artifacts may scale badly, or adapting
weights on the same evidence may reach the same competence at lower total
cost. Those comparisons are part of what the program has to run.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture, and each has a cost the program must weigh against it.

- **Continual learning.** What is learned is usable at the next request. A
  fact that fits the current theory is written down and takes effect. A
  fact that contradicts it forces a reconciliation: decide which commitment
  gives way, revise it, re-check what depended on it. That reconciliation
  is the paradigm's counterpart of retraining. The edit is local, to an
  identifiable part of the theory, rather than a global refit. Its
  consequences need not be local, and that spread, one revision changing
  several later decisions, is the point.
  Reconciliation is where the costs of [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate: admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter. In
  the case above, one discovered dependency changed the checking decision
  for several files. The conjecture that [theory refinement improves sample
  efficiency under structured
  shifts](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names. Fewer
  observations need not mean a cheaper method once theory construction,
  retrieval, and maintenance are counted.
- **Legibility.** Each learned assumption, rule, or test is an identifiable
  target: it can be read, challenged, and named as the thing to revert.
  Reverting it is not free of consequences, because later changes may have
  depended on it, so a rollback needs the same dependency check as a
  revision. What legibility buys is that the target and its dependents can
  be found, not that they are independent. A learner confined to [a fixed
  decomposition inherits that decomposition's
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  a learner that can rewrite its own representations and tools has a wider
  space to repair in. Legibility is a property of the retained state, not a
  guarantee that the model uses it faithfully.

## The system that carries the paradigm

Questions about a learning paradigm are questions about a whole system,
not about a model. We call that system a [theory
builder](../notes/definitions/theory-builder.md): the complete persistent
system responsible for developing and revising tentative theories about the
subjects it is asked to investigate. Its boundary follows roles. Whoever
supplies questions, cases, and acceptance judgments is outside. Whoever
interprets a theory, chooses what to blame, produces or selects a revision,
or repairs the machinery is inside, person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when its
machinery changes pass through a theory of its own machinery. The two
conditions are independent. The evidence supplement gives the boundary,
the seed, and the rule for what counts as the same builder over time in
full, together with the systems that sit on the edges of the definition.

## What would test it

Fixing the weights is an experimental condition. It rules out parameter
updates as the source of any improvement, which isolates the proposed
learning channel for study. It does not by itself attribute an improvement
to retained state: a different task mix, more computation, a human
intervention, or run-to-run variation could each explain a gain. Attribution
needs matched comparisons with the retained change removed, which the
evidence supplement specifies. Fixing weights is not a recommendation for
mature systems, and not a claim that learning outside weights is generally
better.

The three attractions above are claims about a mechanism, and they are
tested in bounded components: matched runs that vary what is retained and
measure influence, transfer, and observations used. The program's headline
hypotheses are claims about a whole system's performance under external
assessment. The two levels do not substitute for each other. Better overall
performance would not show that fewer observations were needed or that a
rollback was safe, and a component result would not show that a whole
system reaches a reliability target. The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both
levels. The program states three whole-system hypotheses.

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

A finite evaluation supports a bounded claim. None of the hypotheses
promises success on every problem or within every budget.

The hypotheses are tested through an *externally tested* builder, one that
receives from outside a falsifier, meaning failures it does not judge
itself, an objective, and an outcome level independent of its own
evaluators. With those supplied, outcome comparisons can proceed before
the builder has settled how much support its internal theories need. Where a claim lacks that external
assessment, [the builder owes three things for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level for
changing an objective, and attribution when it asserts a cause.

The whole experimental setup is a first design. It has been stated but not
exercised, and we expect it to change under testing before a scored run.

## The first arrangement

The first arrangement proposed for testing the paradigm is Commonplace, a
framework for knowledge bases operated by agents. In the proposed run,
Commonplace produces a knowledge base and its supporting software for a
consuming project. Agents in that project use the knowledge base on their
tasks, and the project's own judges accept or reject the work. Those
judgments are the external falsifier and objective. Commonplace would
revise the delivered product, and when a failure exposed a limit in its own
methods, revise those too. Today people still perform several inside
roles, so it is a human-inclusive builder; how those roles would transfer
to computation is the [bootstrap
supplement's](./bootstrapping-the-first-automated-software-house.md)
subject. No consuming-project run has been performed. The evidence
supplement gives the protocol's shape.

A different arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. It offers a stronger falsifier, since software fails visibly, at
the price of a different and harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Open questions

- Whether a succession of revisions, each justified by its own evidence,
  composes into a justified lineage once evaluation results guide later
  revisions.
- What support licenses each kind of reliance on a retained theory:
  guiding an experiment, routine use, compilation into a test.
- Whether current models interpret prose theories consistently enough for
  diagnosis and repair to work, rather than only for application.
- How to assign credit across artifacts when a later failure could lie in
  the theory, the retrieval that never surfaced it, the evaluator that
  admitted a change, or a skipped check.
- Whether the paradigm's total cost, with theory maintenance counted,
  compares well with adapting weights on the same evidence.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state
the paradigm's terms with their exclusions and boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the external assessment, the first arrangement's protocol, and
the component experiments. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions.
[Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery, and what that does and does not establish.
