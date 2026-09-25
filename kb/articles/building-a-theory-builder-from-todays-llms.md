---
description: "Lead article: the bet that an autonomous theory builder that learns, a system running a Popperian conjecture-and-criticism cycle over explicit revisable theories, can be built from fixed-weight LLMs; payoffs, conjectures, Bitter Lesson, learning test"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/tentative-theory.md
  - kb/notes/definitions/addressable-theory.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/retained-theories-may-improve-sample-efficiency.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md
  - kb/notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md
  - kb/notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/definitions/constraining.md
  - kb/notes/definitions/codification.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md
---

# Building a Theory Builder from Today's LLMs

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Agent systems already keep notes, decide what is worth keeping, and revise
what they kept. How far they run without a person depends on how precisely
those operations are defined, because an interpreter fills in whatever a
definition leaves open.

We propose a learning paradigm based on
[Popper's cycle for the growth of knowledge](https://doi.org/10.1016/S0049-237X(08)71204-7):

> problem → tentative solution → error elimination → revised problem

We call a system that runs this cycle over explicit theories a **theory
builder**. Faced with a problem, it proposes a
[tentative theory](../notes/definitions/tentative-theory.md) as a solution.
The knowledge base behind this article
[defines the theory builder](../notes/definitions/theory-builder.md) by four
conditions on how it treats such theories:

1. it states them in natural or formal language, so that identifiable units
   say something;
2. it acts on them, so that what a theory says changes what the system does;
3. it criticizes what they say, by argument, by comparison with rivals, or
   by testing their consequences, and revises or replaces those that fail;
4. it keeps the result of criticism, so that it shapes the next round.

The definition sets no minimum for how long results persist. The arrangement
we build keeps them across problems, so that they change later work on other
questions. The definition also has no success condition: a builder that
never improves still meets it. That is why the bet below is about learning,
not only about building.

## The bet

Our bet is that **a fully automated theory builder that learns can be built
with today's fixed-weight LLMs**. Learning here means that the builder's own
conjecture and criticism improve its capacity for later work; the test below
says how that is shown.

Fully automated means that every internal role in the cycle is performed
computationally. Users still set the tasks and judge the results; what the
builder does not need from people is the formulation, criticism, revision,
and selection of its own theories, or changes to the machinery that does this
work. That boundary is what the knowledge base calls
the [autonomous qualifier](../notes/definitions/theory-builder.md#qualifiers).

The builder is not the LLM alone. It is a system containing an LLM together
with persistent state, tools, tests, evaluators, and control machinery.
[The deployed system, not the model, is the unit that learns](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md):
prompts, retrieval, tools, and runtime policy jointly determine what it does,
so the learning claim is made about that whole.

Current LLMs already appear capable of the main functions the loop requires:

- formulating and reformulating problems,
- generating tentative solutions,
- deriving consequences,
- criticizing alternatives,
- designing and interpreting tests,
- revising explicit knowledge,
- using retained knowledge in later work.

None of these capabilities needs to be perfect. The point of the cycle is to
expose and correct errors.

The bet is the first stage of the program, not all of it. A builder that
learns can do so with a fixed method. Given such a builder, the next stage
makes it reflective: its own method becomes one of the theories it states,
criticizes, and revises. The stage after that is compounding, where
improvements to the method make later improvement cheaper, more reliable, or
possible where it was not. Reflection opens that path but does not complete
it; the [bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
says what else it takes, and the
[testing supplement](./testing-whether-a-theory-builder-learns.md) tests
compounding only after learning is shown.

## Formalize it, or leave it to people

Self-improving machines are not new. Schmidhuber's
[program](https://people.idsia.ch/~juergen/recursive-self-improvement.html)
has pursued them since 1987: policies that modify their own update rules,
program search that reuses its earlier solutions, and the
[Gödel machine](https://arxiv.org/abs/cs/0309048), which may rewrite any part
of its own software — the proof searcher included — once it has proved that
the rewrite beats carrying on unchanged. These are real learning machines,
and the Gödel machine's optimality result is a formal theorem.

What they require is that the work be formalized first. The environment, the
machine, and the utility function enter as axioms, and a change is admitted
by a proof under them. The paper is blunt about the consequence: the machine
"must ignore those self-improvements whose effectiveness it cannot prove."
We read this as
[a proof-governed case of self-modification](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md):
rigorous relative to its formalization, and silent about whether that
formalization is adequate, since a valid proof under the wrong premises
warrants nothing anyone wanted. The seed is costly for the same reason.
Everything the first improvement needs has to be there already, in executable
form.

One operation is missing rather than restricted. Proving that a switch is
beneficial under the current premises is a different thing from revising
those premises because cases have gone against them, and the second is most
of what open-ended learning consists of. Schmidhuber's retrospective leaves
that operation unspecified.

No one has formalized that operation, and that has generally been taken to
settle the matter. Peter Naur argued the point from the other side: the
judgments that relate a program to the world cannot be reduced to formulated
criteria, so the theory of a program is bound to the people who hold it. As
the knowledge base
[reconstructs that inference](../notes/naur-equates-machine-execution-with-formulated-criteria.md),
it needs one further premise — that a computer can make a judgment only by
executing criteria formulated in advance. Grant the premise and the work
divides in two. What can be formalized goes to machines; what cannot stays
with people. Schmidhuber's constructions push the first half as far as it
goes, and Naur's conclusion is what the second half implies.

The division is not exhaustive, because narrowing what an artifact can be
taken to mean is a [gradient](../notes/definitions/constraining.md) rather
than a switch. Defining a term rules out some readings. A convention rules
out more. A structured document assigns meaning to positions in it. A schema
or a validator rejects the readings it does not admit. Only the last steps
cross into a symbolic medium whose consequences a formal consumer assigns,
which is what we mean by
[codification](../notes/definitions/codification.md); everything before them
is still natural language, waiting to be read. The dichotomy takes the far
end of that gradient for the whole of it.

An LLM is an interpreter for the middle. A definition written precisely
enough to rule out the readings that would change what it asks for can be
applied, by a model, to a case nobody anticipated when it was written. That
is not formalization — nothing assigns the definition consequences, and the
interpreter's judgment fixes what happens wherever the words leave a choice
open. But it is not leaving the operation to people either. This is why the
paradigm below is stated through definitions and why they are worked as hard
as they are: what it takes for a retained change to count as operative, what
makes a theory addressable, what a criticism has to do. Each is constrained
as far as it will go and then left to the interpreter. Parts that settle can
be codified afterwards, one at a time, as our validators and schemas have
been; the rest stays open to criticism.

Two costs come with this position. A proof gate fails closed: it refuses
every change it cannot certify, including the good ones. An interpreter fails
open. It will apply a definition that contradicts another definition and
produce plausible work from either, and nothing in the medium announces the
contradiction, so error correction has to be built rather than inherited.
Constraining is not free to add either: a definition pinned down harder than
the thing is understood freezes a wrong reading in place. And against the
earlier constructions we give up warrant, since a proof certified each
accepted change there, where here the interpreter's judgments are hidden and
have to be checked by other means.

## A distinct learning paradigm

If this works autonomously, theory building is a distinct learning
paradigm rather than another agent workflow, because its learning happens
through explicit, criticizable theories rather than only through changes to
model weights. Three payoffs follow from that difference.

**Learning without retraining.** New knowledge becomes available
[without another weight-training cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md),
so the builder adapts at deployment time rather than at the next training
run.

**Fewer observations after a shift.** A retained theory may
[reduce the observations needed after a shift](../notes/retained-theories-may-improve-sample-efficiency.md)
that preserves the structure it describes, which is the sample-efficiency
advantage most often claimed for explicit knowledge; the note states the
conditions under which the claim is plausible.

**A learned state that can be read.** What the system has learned is held as
stated text, prose and code where a part has been codified, so it can be
read, diffed, tested, and reverted the way a weight update cannot be. Nothing about this requires a human reader:
[inspectability is a property of the artifact's form, not of who inspects it](../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md),
so agents can do the reading at a volume people could not, and what the
system has learned stays available for oversight without waiting on progress
in weight interpretability. But
[a legible artifact need not be the one actually driving behaviour](../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md),
which is why the learning test below alters the retained knowledge instead of
inspecting it: the medium makes the question testable, not settled.

Three further advantages are conjectural, and concern how well the loop
learns rather than what its form makes possible. The knowledge base develops
each in its
[research companion](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#three-conjectures).

*Criticism carries content.* When a theory fails, the builder formulates
why. A stated diagnosis directs the next attempt differently from a bare
failure signal, and can save search that variant-and-select methods would
spend. A wrong diagnosis can also waste it; the conjecture is about what a
supplied reason buys on balance.

*Theories are addressable.* A theory whose assumptions and parts can be
inspected and revised individually lets criticism name a part, and lets a
revision keep the rest. This property is
[addressability](../notes/definitions/addressable-theory.md), and it comes
in degrees; the comparison is with a builder that criticizes and replaces
each theory whole. Naming a part can focus investigation and preserve useful
knowledge through a revision; it can also locate a fault in the wrong part.

*Persistence saves work.* Keeping the assembled theory, and the criticism
that shaped it, across problems may cost less at comparable decision quality
than keeping results only within one run, or than rebuilding them each time,
either from retained criticisms or from records of inputs and outcomes
alone.

Explicit state also has costs. A retained theory requires retrieval,
applicability checks, revision, validation, and maintenance. A false
abstraction can misdirect many decisions, and a correct one that retrieval
misses helps nobody. Keeping episode records alongside distilled rules
[preserves a route for re-examining a rule](../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)
that turns out to be wrong. Construction, retrieval, maintenance, and
mistakes have to be counted on both sides of any comparison with a
weights-only learner.

The advantages and the costs are both empirical questions. The claim that
matters here is that the paradigm is possible; the companion states
[what the research program claims and what it does not](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#research-program-and-development-path).

## Compatible with the Bitter Lesson

[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
contrasts leveraging human knowledge with leveraging computation through
search and learning. That is a claim about how a system's
behaviour-determining content gets made, not about the form the content is
kept in. Its folk version, *structure loses to weights*, quietly swaps the
second for the first; the lesson
[selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Sutton appears to hold something close to the folk version himself — in a
2026 [interview](https://sequoiacap.com/podcast/rich-sutton-and-khurram-javed-why-ai-models-stop-learning-and-how-to-start-it-again)
he and Khurram Javed argue that forming new concepts needs continued weight
updating — but that is a separate hypothesis, which our bet runs against and
the essay does not establish. The essay's own cases separate the two axes:
what scale displaced included hand-tuned weights as well as hand-written
feature extractors, so the losing side spanned both forms and the selection
ran on how the content was produced.

A theory builder sits on the computation side of that axis. Its theories,
criticism, tests, and revisions are explicit, but they need not be supplied
by people: a theory proposed, criticized, and revised by the loop is a
learned result whatever form it is retained in. And if the entire loop is
automated, additional computation buys more alternatives, stronger criticism,
more tests, and more revision of accumulated knowledge, which is the work the
lesson rewards.

The relevant distinction is therefore not between explicit knowledge and
scalable learning. It is between **human-supplied knowledge** and
**automatically generated, tested, and revised knowledge**.

Two conditions attach. A builder that starts from hand-written theories and
machinery, as ours does, fits the lesson
[only if its learning outgrows that starting state](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation, not people, must come to supply the task-specific knowledge
each new demand needs. And because an improvement to the learning machinery
is paid for once and then reused by every later episode,
[a long-run strategy should spend part of its effort on that machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).
That spending is **reflection**: the builder turns its own methods into
theories it can criticize and revise, and the lesson says which revisions to
look for — those that convert additional computation into capability.

## What would count as learning?

Repeated problem solving is not enough. For learning to occur, the result of
one episode must durably change the system in a way that affects later
behaviour:

> K(t) → conjecture and criticism → K(t+1) → different later behaviour

where K is the retained tentative knowledge. In our first arrangement K is a
knowledge base: files holding theories, the criticism recorded against them,
and the instructions derived from them, which later runs read before acting.

This gives a direct empirical test in two parts. First, withholding or
altering the retained knowledge should change subsequent behaviour; the
knowledge base calls a change that passes this test
[operative](../notes/definitions/operative-change.md). Second, the changed
behaviour should be better. Showing that a theory was formulated, criticized,
and revised, and that the revision was used,
[does not by itself establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md);
a builder can retain and faithfully apply a bad rule. The
[testing supplement](./testing-whether-a-theory-builder-learns.md) states
the hypotheses that separate these outcomes and what would refute each.

The research question is therefore simple:

> **Can a fixed-weight LLM system autonomously maintain tentative theories,
> expose them to error, revise them, retain the revisions, use them in later
> work, and do better for it?**

We think the answer is yes.

## Where to go next

The [testing supplement](./testing-whether-a-theory-builder-learns.md)
defines the system under test, the three hypotheses, and the first protocol.
The [bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
starts from Commonplace, a knowledge base currently maintained by people and
agents together, and transfers its internal roles to computation one class at
a time; it also covers the builder's reflection on its own machinery. The
[software-house supplement](./an-automated-software-house-as-a-second-test-of-a-theory-builder.md)
proposes a second arrangement whose failures are more visible. The
[survey](./which-existing-self-improving-systems-are-theory-builders.md) places
eighteen existing self-improving systems against the four conditions and
judges their reported gains separately. The
[definition](../notes/definitions/theory-builder.md) states exactly
what a theory builder requires and what it leaves open.
