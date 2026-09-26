---
description: "Lead article: theory refinement with fixed model weights as a learning paradigm, its departures from classical refinement, its conjectured attractions, five named takeaway ideas, and an outline of the theory builder, hypotheses, and first arrangement"
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
later work. This is *theory refinement*, an established learning operation,
in a new setting. The alternatives are adapting the weights, and retaining
raw records or summaries of experience without an explanation. The paradigm
has three conjectured attractions: learning is continual, it may need fewer
observations, and what is learned can be inspected and rolled back piece by
piece. This article states the paradigm and ends with five ideas worth
carrying away. Companion supplements state how it would be tested. No test
has been run.

## A case

Consider a system that maintains a release exporter, which builds a
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

Three things happened. A written account guided a decision on a case it did
not mention. A failure contradicted one part of the account, and only that
part was revised. The revision was chosen for what else it would handle,
not only for the failure that caused it. These three are the core of the
paradigm.

## Theory refinement, and what is new here

[Theory refinement](../notes/definitions/theory-refinement.md) revises an
existing explicit theory against empirical cases, correcting its errors
while keeping what was right, instead of learning from scratch. The name
comes from Ourston, Richards, and Mooney in the early 1990s, where the
theory was a set of logical rules from an expert and the cases were
labelled examples. Their systems derived consequences from the rules, found
where a wrong consequence came from, and edited that part.

The operation needs a theory with three properties. It has consequences a
case can contradict. It has parts that a failure can point at as candidate
repair locations. Those parts can be edited separately. We call a theory
with these properties **addressable**. The exporter account is addressable:
it predicted which edits needed which checks, the failure pointed at its
assumption about the input list, and that assumption was revised on its
own.

The theory is a [tentative theory](../notes/definitions/theory-refinement.md#tentative-theory)
in Karl Popper's sense: put forward as a solution, held open to criticism,
and never promoted to settled truth by surviving tests.

The paradigm keeps the operation and changes the setting in three ways.
These are our departures, not claims of the classical work.

- **The interpreter is a language model, so the theory can be prose.** The
  classical systems refined theories in the one formal language their
  procedures handled. A language model can apply and revise an account
  nobody has formalized, so a theory can enter the loop before anyone
  writes a checker for it. The cost is that whether a case contradicts a
  prose theory is itself a reading, and two readings can differ.
  Refinement moves parts into schemas, validators, and tests as they
  settle, and gains checkability, not certainty, by doing so.
- **The theory is partly normative.** A commitment such as "every query
  must respect the active tenant" is a rule the system keeps true, not only
  a hypothesis. A failure can then be resolved by changing the product to
  fit the theory, or the theory to fit the evidence, and the system must
  decide which. A requirement supplied from outside, such as tenant
  isolation, is not the system's to weaken: that would make a failure
  disappear without improving anything.
- **The theory may be about the system itself.** The account of which
  checks to run is part of the system's own production machinery. When the
  same loop revises how the system builds, tests, and revises its theories,
  the loop is *reflective*.

Two further choices belong to the paradigm. First, among revisions that fit
the evidence, **prefer the one with more reach**: the one that would also
handle cases the failure did not show. That is why the case revises the
account of what the exporter reads instead of adding an exception for one
snippet. Second, **treat the deployed system as the learner**, because
[retrieval, scheduling, tools, and validators jointly determine behaviour
with the model
fixed](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
When a new theory needs a check the system cannot yet perform, [the
system has to build
it](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md)
and retain it outside the model.

## Why the Bitter Lesson does not rule this out

Rich Sutton's Bitter Lesson says that general methods which scale with
computation outperform methods built from human knowledge, and written
theories look like hand-crafted structure. The answer turns on [how the
structure is produced, not the form it is retained
in](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Here computation forms and revises the theories and selects changes from
evidence; people may build only the seed the system starts from. That
establishes compatibility, not a scaling advantage: adapting weights on the
same evidence may still be cheaper, which the program has to test.

## What the paradigm would buy

The attractions come from [retained artifacts changing later behaviour
without a training
cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
Each is a conjecture with a cost attached.

- **Continual learning.** What is learned is usable at the next request. A
  fact that fits the current theory is written down and takes effect. A
  fact that contradicts it forces a **reconciliation**: decide which
  commitment gives way, revise it, and re-check what depended on it.
  Reconciliation is the paradigm's counterpart of retraining. The edit is
  local to an identifiable part of the theory, but its consequences spread,
  and that spread is the point: one revision changes several later
  decisions. Reconciliation is also where the costs of [governing
  behaviour-changing
  writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
  concentrate: admission, coordination, and credit assignment.
- **Fewer observations.** A correct theory says which new cases matter. In
  the case, one discovered dependency changed the checking decision for
  several files. The conjecture that [theory refinement improves sample
  efficiency](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  holds only for shifts that preserve the structure the theory names, and
  fewer observations need not mean lower total cost once theory
  maintenance is counted.
- **Legibility.** Each learned assumption, rule, or test can be read,
  challenged, and named as the thing to revert. A rollback still needs the
  same dependency check as a revision, because later changes may rest on
  it. A learner confined to [a fixed decomposition inherits that
  decomposition's
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  one that can rewrite its own representations and tools can repair more.
  Legibility is a property of the retained state, not a guarantee that the
  model uses it faithfully.

## The system that carries the paradigm

We call the learner a [theory builder](../notes/definitions/theory-builder.md):
the complete persistent system that develops and revises tentative
theories about the subjects it is asked to investigate. Its boundary
follows roles: whoever supplies questions, cases, and acceptance judgments
is outside; whoever interprets a theory, chooses what to blame, revises, or
repairs the machinery is inside, person or program. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every inside role, and
[reflective](../notes/definitions/reflective-theory-builder.md) when changes
to its machinery pass through a theory of that machinery. The two
conditions are independent.

## What would test it

**Fixing the weights is an experimental control**, not a recommendation for
mature systems. It rules out parameter updates as the source of any
improvement. It does not by itself attribute a gain to retained state: a
different task mix, more computation, human intervention, or run-to-run
variation could explain it. Attribution needs matched comparisons with the
retained change removed.

The three attractions are tested in bounded components, with matched runs
that vary what is retained. The main hypotheses concern a whole system
under external assessment, and neither level substitutes for the other.
The [evidence
supplement](./testing-the-theory-refinement-program.md) specifies both, and
states three whole-system hypotheses.

- **Sufficiency.** A learning methodology written in prose and code lets a
  computational builder on fixed public models develop, retain, and use
  theories across declared areas, to a reliability target under a stated
  budget. Refuted if reaching the target needs people in inside roles or a
  new learning method per area.
- **Comparison.** Under matched demands and resources, the methodology
  outperforms its frozen seed and a baseline that searches the raw records,
  and its reliability comes within a preset margin of a human-staffed
  builder's. Refuted if the controls do as well.
- **Reflection.** A builder whose machinery changes pass through a causally
  connected self-theory gains capabilities beyond its seed that a matched
  builder without one does not. Tested against the records of reflective
  episodes, not outcomes alone.

The hypotheses are tested through an *externally tested* builder: one that
receives from outside a falsifier (failures it does not judge itself), an
objective, and an outcome level independent of its own evaluators. Where a
claim lacks that external assessment, [the builder owes three things for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as contradiction and support, a comparison level for
changing an objective, and attribution when it asserts a cause. The setup
is a first design, not yet exercised.

## The first arrangement

The first arrangement proposed for testing is Commonplace, a framework for
knowledge bases operated by agents. In the proposed run, Commonplace
produces a knowledge base and supporting software for a consuming project.
Agents in that project use the knowledge base on their tasks, and the
project's own judges accept or reject the work; those judgments are the
external falsifier and objective. Commonplace would revise the delivered
product and, when a failure exposed a limit in its own methods, those
methods too. People still perform several inside roles today; how those
roles would pass to computation is the [bootstrap
supplement's](./bootstrapping-the-first-automated-software-house.md)
subject. No consuming-project run has been performed.

A different arrangement takes software as the product: an automated
software house whose theory is Naur's program theory of the software it
maintains. Software fails visibly, which gives a stronger falsifier, at the
price of a harder claim. The [software-house
supplement](./an-automated-software-house-as-an-alternative-test.md)
develops it and compares the two.

## Five ideas to carry away

1. **Addressable theory.** Refinement works on a theory whose consequences
   a case can contradict and whose parts a failure can point at and edit
   separately. That is what let the exporter account lose one assumption
   and keep the other.
2. **Reconciliation instead of retraining.** A contradicting fact forces a
   local edit and a re-check of what depended on it. The edit is local; its
   effect on later decisions is not.
3. **Prefer the revision with more reach.** Among fixes that fit the
   failure, choose the one that also handles cases the failure did not
   show, as the revised account of the exporter's inputs did.
4. **The deployed system is the learner.** Theories, tools, tests,
   retrieval, and the update process together form a theory builder,
   defined by roles, not by whether a person or a program fills them.
5. **Fixed weights are a control.** Holding the model fixed isolates
   learning through retained state for study; it is not a claim that such
   learning is better.

## Open questions

- What support licenses each kind of reliance on a retained theory:
  guiding an experiment, routine use, compilation into a test.
- Whether current models interpret prose theories consistently enough for
  diagnosis and repair, not only for application.
- How to assign credit when a later failure could lie in the theory, the
  retrieval that never surfaced it, the evaluator that admitted a change,
  or a skipped check.

## Where to go next

The [theory refinement](../notes/definitions/theory-refinement.md) and
[theory builder](../notes/definitions/theory-builder.md) definitions state
the paradigm's terms with their boundary cases. The [evidence
supplement](./testing-the-theory-refinement-program.md) develops the
hypotheses, the protocol, and the component experiments. [Nearest existing
constructions](./nearest-existing-constructions-to-a-witness-house.md)
compares eighteen existing systems against the software-house conditions.
[Transition closure and continuation
reliability](./transition-closure-and-continuation-reliability.md) develops
the requirement that every change to a builder arise through its own
machinery, and what that does and does not establish.
