---
description: "Lead article: learning by theory refinement with fixed model weights as a learning paradigm, its departures from classical refinement, its conjectured attractions, and an outline of the theory builder, hypotheses, and first arrangement"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/learning-by-theory-refinement.md
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
  - kb/notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md
---
# Learning by Theory Refinement with Fixed Models

*A research program for systems that learn outside their weights*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** We propose a learning paradigm for systems built around large
language models: the system learns by refining written theories that it
retains outside the model and consults on later work. We study it with the
model weights held fixed, so that any learning has to come from what is
retained. What is learned is a *tentative theory*, an explicit and revisable
account of some subject that guides the system's decisions. The system
revises it by *theory refinement*, an established learning operation that
seeks to correct an existing theory against new cases while preserving
useful prior knowledge.
The setting is new. The paradigm is set against two alternatives: adapting
the weights, and retaining raw records or summaries of experience without
an explanation. Its three attractions are each still a conjecture: learning
is continual, it may need fewer observations, and each learned part can be
read, and the part to revert can be found along with what depends on it.
This article states the paradigm. The supplements state how it would be
tested and which system would be tested first. No test has been run.

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

Four things happened. A written account guided a decision on a case it
did not mention. A failure contradicted one part of the account, and that
part was revised rather than the whole account replaced. The revision was
chosen for what else it would handle, not only for the failure that caused
it. And the revised account went on to guide later decisions. The rest of
this article says why those four things are the core of a learning
paradigm.

## Theory refinement

[Theory refinement](../notes/definitions/theory-refinement.md) is the
learning operation that revises an existing explicit theory against
empirical cases, seeking to correct errors while preserving useful prior
knowledge instead of learning from scratch. The name comes from the work of Ourston,
Richards, and Mooney in the early 1990s, where the theory was a set of
logical rules supplied by an expert and the cases were labelled examples. Their systems derived consequences from the rules, found where a
wrong consequence came from, and edited that part.

The operation needs a theory of a particular shape. It must have
consequences a case can contradict. It must have parts that a failure can
point at as candidate repair locations. And those parts must be editable
separately. A theory with these properties is *addressable*. The account in
the case above is such a theory: it predicted which edits needed which
checks, the failure pointed at its second part, on what the configured
list identifies, and that part was revised on its own.

We call the theory a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory),
in Karl Popper's sense: put forward as a solution, held open to criticism,
and never promoted to a settled truth by surviving tests. The status
licenses nothing by itself. How much support a theory needs before the
system relies on it routinely, or compiles it into a test, is a policy the
system has to set.

## The paradigm defined

[Learning by theory
refinement](../notes/definitions/learning-by-theory-refinement.md)
is the loop built on that operation. A system retains a tentative theory
outside its model weights. The theory guides its decisions. The outcomes of
that work refine the theory, part by part. The refined theory guides later
work. What the system has learned is the change in its later behaviour that
comes from the change in the retained theory. In the case, the revision
changes later checking decisions: the system checks included snippets it
has never seen fail.

The definition has boundaries. It does not require success: a system that
carries a mistaken theory forward is still learning this way, and whether
it improved is measured separately. A theory built while reasoning and
discarded after the decision does not count, because nothing remains to
refine. Adapting the weights is a different paradigm, because what is
learned there is not a theory with parts that can be inspected and revised.
Keeping records or summaries of experience and rebuilding an explanation
when one is needed is a different design, because no explanation is
retained as an object to revise. A later section compares the two. And
fixed weights are not part of the definition. We hold them fixed to study
the paradigm, and a system could run the loop and adapt its weights as
well.

This definition is meant to say what the paradigm is, not yet how to
measure it. What counts as evidence that the theory guided a decision, or
that a later change came from the revision, is the [evidence
supplement's](./testing-the-theory-refinement-program.md) subject, and some
of those details are still open.

## What is new in the setting

The paradigm keeps the operation and changes the setting in three ways.
Each is our departure, not something the classical work claims.

- **The interpreter is a language model, so the theory can be prose.** The
  classical systems each refined theories written in the one form their
  procedures handled. A fixed language model can be given an account
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
  into code as they settle, and gains checkability, not certainty, by doing
  so.
- **The theory is partly normative.** The theory in the case is not only
  a hypothesis about the exporter. A commitment such as "every query must
  respect the active tenant" is a rule the system keeps true. A failure can
  therefore be resolved by changing the product to fit the theory as well
  as by revising the theory to fit the evidence, and the system must decide
  which. That choice has a constraint. Descriptive assumptions, such as
  what the configured list identifies, and implementation choices are the
  system's to revise. A requirement supplied from outside, such as tenant
  isolation, is not: weakening it would make a failure disappear without
  improving anything, and it changes only when whoever supplied it
  renegotiates it. The external objective introduced below records such
  requirements and who may change them.
- **The theory may be about the system itself.** The theory of which
  checks to run is part of the system's own production machinery. When the
  same loop revises how the system builds, tests, and revises its theories,
  the loop is *reflective*: revisions of the self-theory change the machinery,
  and machinery changes update the self-theory. A system that holds a
  description of itself without that two-way connection is not reflective
  in this sense.

Two further choices are the paradigm's own. The first is a preference
among revisions that fit the evidence: prefer the one with more reach, the
one that would also handle cases the failure did not show. That is why the
case revises the theory of what the exporter reads instead of adding an
exception for one snippet.

The second is to treat the whole deployed system as the unit that learns,
because [retrieval, scheduling, tools, and validators jointly determine
behaviour with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
What the paradigm retains includes theories, the records they were derived
from, procedures, tests, tools, evaluators, and the update process itself. When a new theory needs a check
the system cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and with weights fixed that capacity has to persist outside the model.

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation outperform methods built from human knowledge. Written theories look
like hand-crafted structure, so the objection is natural. The answer turns
on [how the structure is produced, not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
In the autonomous version we aim to build, computation forms and revises
the theories, builds the tools and evaluators, and selects changes from
evidence. People may build the seed, the theories and machinery the system starts from. After that,
project-specific structure is a learned product.

That is compatibility, not a scaling advantage. Search, validation, and
credit assignment over retained artifacts may scale badly, or adapting
weights on the same evidence may reach the same competence at lower total
cost. Those comparisons are part of what the program has to run.

## Why not just keep the records

A simpler design keeps the records of past work, such as observations, tool
output, and outcomes, and has the model search them when a decision needs
them. The model can still build an explanation while it reasons, and it
discards the explanation afterwards. This is a common design today. While
a system's experience fits in what the model can use at once, keeping the
records preserves every recorded detail and commits to no abstraction that
might be wrong. But reading and interpreting the records again at each
decision has a cost that a reused theory may save.

The paradigm claims nothing about what can be learned in principle: a system
with unlimited context and computation could rebuild every explanation from
its records at every decision. Limits on context and computation create two
needs, and neither selects theories. A decision that depends on more
evidence than the model can use at once needs intermediate results that
stand in for that evidence. And when rebuilding those results at every
decision costs more than the decision's budget allows, the system has to
keep and reuse them. Search over records, summaries, periodic
reconstruction, and retained theories are all ways to meet these needs, and
a system can combine them: search can supply the evidence for a revision,
and reconstruction can replace a theory that has gone wrong.

Retaining and refining theories is our provisional choice among them. The
conjecture is that theories are an efficient compression of experience for
later decisions: for the space they take and the upkeep they need, they
preserve more of what those decisions depend on than the other forms do.

The case illustrates how a retained theory could help; it does not show
that records with good search would do worse. When the named Markdown
files were added, the theory applied to a situation that no earlier record
needed to resemble, because it says why checks are needed. After the
snippet failure, the revised theory covers snippets the system has not
touched, without the failure having to be found and interpreted again. A
system that searches its records before choosing checks might reach the
same decisions. Whether the provisional choice pays is a comparison
the program has to run, against records with good search and not against
records alone. The comparison must measure costs and decision errors for
both systems: finding and reinterpreting records, constructing, revising,
and consulting theories, and mistakes caused by missed evidence or
misleading theories. The evidence supplement's [component
experiment](./testing-the-theory-refinement-program.md#component-experiments-that-can-run-first)
is a first design for it.

The paradigm keeps the records as well. A retained theory can carry a
mistaken abstraction forward, or omit a detail a later case needs, and [the
records are the evidence for re-examining
it](../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).
They also let a later, better model redo the derivation. What changes is
what is loaded by default: the theory, with the records consulted when the
theory is in doubt.

## What the paradigm would buy

The attractions are stated mainly against adapting weights. They come from
[retained artifacts changing later behaviour without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
A system that keeps records also takes in new experience without a training
cycle, but readable records do not by themselves identify the learned
assumptions and what depends on them, and they count as learning only
through their effect on later work. The previous section gives the
comparison with that design. Each attraction is a conjecture, and each has a
cost the program must weigh against it.

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
  for several files. The conjecture that [theory refinement may improve sample
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
or repairs the machinery is inside, person or software. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every internal role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when its
machinery changes pass through a theory of its own machinery. The two
conditions are independent. The evidence supplement gives the boundary,
the seed, and the rule for what counts as the same builder over time in
full, together with the borderline cases of the definition.

## What would test it

Fixing the weights is an experimental condition. It rules out parameter
updates as the source of any improvement, which isolates learning through
retained state as the mechanism under study. It does not by itself attribute an improvement
to retained state: a different task mix, more computation, a human
intervention, or run-to-run variation could each explain a gain. Attribution
needs matched comparisons with the retained change removed, which the
evidence supplement specifies. Fixing weights is not a recommendation for
mature systems, and not a claim that learning outside weights is generally
better.

The three attractions above are claims about a mechanism, and they are
tested in bounded components: matched runs that vary what is retained and
measure influence, transfer, and observations used. The program's main
hypotheses are claims about a whole system's performance under external
assessment. The two levels do not substitute for each other. Better overall
performance would not show that fewer observations were needed or that a
rollback was safe, and a component result would not show that a whole
system reaches a reliability target. The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both
levels. The program states three whole-system hypotheses.

- **Sufficiency.** A training methodology written in prose and code is
  enough for an autonomous builder on fixed public models to develop,
  retain, and use theories across declared areas, to a reliability target
  under a stated budget and external assessment. Refuted by a builder that
  needs people in internal roles, or a new learning method per area, to reach
  the target.
- **Comparison.** Under matched demands and resources, the builder using
  this methodology gains capability over its frozen seed and over a
  baseline that searches the raw records without the learned methodology.
  Its reliability is comparable to a human-staffed builder's within a preset
  margin. Refuted by matched runs
  in which the controls do as well.
- **Reflection.** A reflective builder gains capabilities beyond its seed
  that a matched non-reflective builder does not. Better outcomes alone do
  not test this. The records of a reflective episode against a matched
  non-reflective builder do.

A finite evaluation supports a bounded claim. None of the hypotheses
promises success on every problem or within every budget.

The hypotheses are tested through an *externally tested* builder. It
receives three things from outside: a falsifier, an objective, and an
independent outcome judgment. The falsifier supplies evidence that an
outcome failed the acceptance requirements. The objective states those
requirements and who may change them. The outcome judgment does not treat
the builder's own evaluators' approval as sufficient. With these supplied,
outcome comparisons can proceed before the builder has settled how much
support its internal theories need. Where a claim lacks that external
assessment, [the builder owes three things for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a standard for judging
whether an objective change is warranted, and attribution when it asserts
a cause.

The whole experimental setup is a first design. It has been stated but not
exercised, and we expect it to change under testing before a scored run.

## The first arrangement

The first arrangement proposed for testing the paradigm is Commonplace, a
framework for knowledge bases operated by agents. In the proposed run,
Commonplace produces a knowledge base and its supporting software for a
consuming project. Agents in that project use the knowledge base on their
tasks, and the project's own judges accept or reject the work. Their
assessments supply the failure signals; the project's acceptance
requirements supply the objective. Commonplace would revise the delivered
product, and when a failure exposed a limit in its own
methods, revise those too. Today people still perform several internal
roles, so it is not yet an autonomous builder. How those roles would transfer
to computation is the [bootstrap
supplement's](./bootstrapping-an-autonomous-theory-builder.md)
subject. No consuming-project run has been performed. The evidence
supplement gives the protocol's shape.

A different arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. It offers a stronger falsifier, since software fails visibly, at
the price of a different and harder claim. The [software-house
supplement](./an-automated-software-house-as-a-second-test-of-theory-refinement.md)
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
- Whether retained theories serve later decisions better than records with
  good search, for which decisions, and from what amount of experience.

## Where to go next

The [learning by theory
refinement](../notes/definitions/learning-by-theory-refinement.md), [theory
refinement](../notes/definitions/theory-refinement.md), and [theory
builder](../notes/definitions/theory-builder.md) definitions state the
paradigm's terms with their exclusions and boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the external assessment, the first arrangement's protocol, and
the component experiments. It also examines an assessed run in which every
change to the builder must arise through its own machinery, and [what a
run under that requirement does and does not
establish](./testing-the-theory-refinement-program.md#what-a-runs-path-can-and-cannot-show).
[Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the requirements for the
automated software house described above and says what that survey shows
for the paradigm: its parts have precedents, and the reviewed evidence does not test its central mechanism.
