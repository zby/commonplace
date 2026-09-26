---
description: "Lead article: theory refinement with fixed model weights as a learning paradigm — addressable theories, preference for reach, the deployed system as learner, fixed weights as an experimental condition, and external testing through three hypotheses"
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
later work. A theory here is an explicit, revisable account of some subject
that guides the system's decisions. The alternatives are adapting the
weights, and retaining records of experience without an explanation. The
paradigm may offer continual learning, learning from fewer observations, and
learned state that can be inspected and rolled back piece by piece; each is
a conjecture, and no test has been run. The article ends with five named
ideas that carry the argument.

## A case

Consider a system that maintains a release exporter. The exporter builds a
deployment manifest from a configured list of input files. The system
retains a short written account of which edits need a manifest check, in
two parts: an edit needs a manifest check when an executable consumer reads
the edited file, and the configured input list identifies every file the
exporter reads. Documentation edits therefore get a syntax check only.

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
then applies the revised account to snippets it has not touched.

Three things happened. The account guided a decision on a case it did not
mention. A failure contradicted one part, and only that part was revised.
The revision was chosen for what else it would handle, not only for the
failure that caused it. These three things are the core of the paradigm.

## Theory refinement, and what is new here

[Theory refinement](../notes/definitions/theory-refinement.md) is the
learning operation that revises an existing explicit theory against cases,
correcting its errors while keeping what was right, instead of learning
from scratch. The name comes from Ourston, Richards, and Mooney's work in
the early 1990s, where the theory was a set of logical rules supplied by an
expert and the cases were labelled examples. Their systems derived
consequences from the rules, found where a wrong consequence came from, and
edited that part.

The operation needs a theory whose consequences a case can contradict, and
whose parts a failure can point at and an edit can change separately. We
call such a theory *addressable*. The exporter account is addressable: it
predicted which edits needed which checks, the failure pointed at its
assumption that the input list was complete, and that assumption was
revised on its own. The theory is also
[tentative](../notes/definitions/theory-refinement.md#tentative-theory) in
Karl Popper's sense: held open to criticism however many tests it has
survived. How much support a theory needs before the system relies on it
routinely is a policy the system must set.

The paradigm keeps the operation and changes its setting in three ways.
These departures are ours, not claims of the classical work.

- **The theory can be prose.** The classical systems refined theories
  written in the one formal language their procedures handled. A language
  model can apply and revise an account nobody has formalized. The cost is
  that consequences are interpreted rather than computed, and two readings
  can differ. Compiling a settled part into a schema, validator, or test
  makes its consequences mechanically checkable. That gains checkability,
  not certainty: the check may still misrepresent the theory.
- **The theory is partly normative.** A commitment such as "every query
  must respect the active tenant" is a rule the system keeps true, not only
  a hypothesis. A failure can then be resolved by changing the product to
  fit the theory as well as by revising the theory. Descriptive
  assumptions and implementation choices are the system's to revise. A
  requirement supplied from outside is not: weakening it would make the
  failure disappear without improving anything.
- **The theory may be about the system itself.** The exporter account is
  part of the system's own production machinery. When the same loop revises
  how the system builds, tests, and revises its theories, the loop is
  *reflective*.

Two further choices belong to the paradigm. First, among revisions that fit
the evidence, prefer the one with more *reach*: the one that would also
handle cases the failure did not show. That is why the case revises the
account of what the exporter reads instead of adding an exception for one
snippet. Second, treat the whole deployed system as the unit that learns,
because [retrieval, scheduling, tools, and validators jointly determine
behaviour with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
What the system retains includes theories, procedures, tests, tools,
evaluators, and the update process itself. When a new theory needs a check
the system cannot yet perform, [the system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and with weights fixed that capacity must persist outside the model.

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation outperform methods built from human knowledge. Written theories
look like hand-crafted structure. But the lesson concerns [how structure is
produced, not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here, computation forms and revises the theories, builds tools and
evaluators, and selects changes from evidence. People may build the seed,
the theories and machinery the system starts from; after that,
project-specific structure is learned. This shows compatibility, not a
scaling advantage: search over retained artifacts may scale badly, and
adapting weights may be cheaper. The program has to run that comparison.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost.

- **Continual learning.** What is learned is usable at the next request. A
  fact that contradicts the theory forces a reconciliation: decide which
  commitment gives way, revise it, re-check what depended on it. The edit
  is local; its consequences can reach many later decisions. Reconciliation is also where the costs of
  [governing behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate: admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter. In
  the case, one discovered dependency changed the checking decision for
  several files. The conjecture that [theory refinement improves sample
  efficiency](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  is bounded to shifts that preserve the structure the theory names, and
  fewer observations need not mean lower total cost once theory
  maintenance is counted.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. Later changes may depend on
  it, so a rollback needs the same dependency check as a revision. A
  learner confined to [a fixed decomposition inherits that decomposition's
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  one that can rewrite its own representations and tools has more room to
  repair. Legibility does not guarantee that the model uses the retained
  state faithfully.

## The system and its test

We call the system that carries the paradigm a [theory
builder](../notes/definitions/theory-builder.md): the complete persistent
system responsible for developing and revising tentative theories about
the subjects it investigates. Its boundary follows roles. Whoever supplies
questions, cases, and acceptance judgments is outside. Whoever interprets a
theory, chooses what to blame, produces or selects a revision, or repairs
the machinery is inside, person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when its
machinery changes pass through a theory of its own machinery. The two
conditions are independent.

Fixing the weights is an experimental condition. It rules out parameter
updates as the source of an improvement. It does not by itself credit
retained state, because a different task mix, more computation, a human
intervention, or run-to-run variation could each explain a gain;
attribution needs matched runs with the retained change removed. Fixing
weights is not a recommendation for mature systems.

The three attractions are claims about a mechanism, tested in bounded
components by varying what is retained. The main hypotheses are claims
about a whole system under external assessment; neither level substitutes
for the other. In brief:

- **Sufficiency.** A learning methodology written in prose and code is
  enough for a computational builder on fixed public models to develop,
  retain, and use theories across declared areas, reaching a reliability
  target under a stated budget and external assessment. Refuted by a
  builder that needs people in inside roles, or a new learning method per
  area, to reach the target.
- **Comparison.** Under matched demands and resources, the methodology
  gains capability over its frozen seed and over a baseline that searches
  the raw records without it, and its reliability is within a preset margin
  of a human-staffed builder's. Refuted by matched runs in which the
  controls do as well.
- **Reflection.** A builder whose machinery changes pass through a
  causally connected self-theory gains capabilities beyond its seed that a
  matched builder without one does not. Better outcomes alone do not test
  this; the records of reflective episodes against a matched builder do.

A finite evaluation supports only a bounded claim. The hypotheses are tested through an *externally
tested* builder: one that receives from outside a falsifier (failures it
does not judge itself), an objective, and an outcome level independent of
its own evaluators. Where a claim lacks that external assessment, [the
builder owes three things
for itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level
for changing an objective, and attribution when it asserts a cause. The
[evidence supplement](./testing-the-theory-refinement-program.md) states
the hypotheses as adopted. The setup is a first design, not yet exercised.

## The first arrangement

The first arrangement proposed for testing is Commonplace, a framework for
knowledge bases operated by agents. In the proposed run, Commonplace
produces a knowledge base and its supporting software for a consuming
project. That project's agents use the knowledge base on their tasks, and
the project's own judges accept or reject the work; those judgments are the
external falsifier and objective. Commonplace would revise the product and,
when a failure exposed a limit in its own methods, those methods too. People still perform several inside roles, so today it is a
human-inclusive builder; how those roles would move to computation is the
[bootstrap
supplement's](./bootstrapping-the-first-automated-software-house.md)
subject. No consuming-project run has been performed.

A different arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. There the theory is about a separate product that fails
visibly, which gives a stronger falsifier, at the price of a harder
existence claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Open questions

- Whether revisions that are each justified compose into a justified
  lineage when evaluation results guide later revisions.
- What support licenses each kind of reliance on a retained theory:
  guiding an experiment, routine use, compilation into a test.
- Whether current models interpret prose theories consistently enough for
  diagnosis and repair, not only for application.
- How to assign credit when a failure could lie in the theory, the
  retrieval, the evaluator that admitted a change, or a skipped check.
- Whether total cost, with theory maintenance counted, compares well with
  adapting weights on the same evidence.

## Five ideas to take away

1. **Theory refinement on addressable theories.** Learning revises the part
   of an explicit theory that a failure points at and keeps the rest. It
   needs theories whose consequences can be contradicted and whose parts
   can be edited separately.
2. **Prefer reach.** Among revisions that fit the evidence, choose the one
   that also handles cases the failure did not show.
3. **The deployed system learns, not the model.** Theories, tools, tests,
   evaluators, and the update process are all retained state; the theory
   builder is the whole system that revises them.
4. **Fixed weights are an experimental condition.** Holding weights fixed
   isolates learning through retained state; attributing a gain to it still
   needs matched runs without the retained change.
5. **External testing.** A builder's claims are tested by a falsifier, an
   objective, and an outcome level supplied from outside the builder.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state
the paradigm's terms with their boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the first arrangement's protocol, and the component
experiments. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions.
[Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery, and what that does and does not establish.
