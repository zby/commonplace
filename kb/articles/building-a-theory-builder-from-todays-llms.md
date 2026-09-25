---
description: "Lead article: the bet that a fully automated theory builder that learns, a Popperian conjecture-and-criticism cycle over explicit theories, can be built from fixed-weight LLMs; payoffs, conjectures, Bitter Lesson, learning test"
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

A system that runs this cycle over explicit theories is a **theory
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

The definition has no success condition: a builder that never improves
still meets it. That is why the bet below is about a builder that learns.

## The bet

Our bet is that **a fully automated theory builder that learns can be built
with today's fixed-weight LLMs**. Learning here means that the builder's own
conjecture and criticism improve its capacity for later work. The test below
says how that is shown.

Fully automated means that computation performs the roles the cycle needs:
noticing problems in the builder's own theories and work, and formulating,
criticizing, revising, and selecting its theories. Users still set the tasks
and judge the results. The knowledge base
[calls a builder autonomous](../notes/definitions/theory-builder.md#qualifiers)
when computation also changes the method that does this work; the approach
described below covers that.

The builder is a whole system: an LLM together with retained knowledge,
tools, tests, evaluators, and control code.
[The deployed system, not the model, is the unit that learns](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md):
prompts, retrieval, tools, and runtime policy jointly determine what it does,
so the learning claim is made about that whole.

Current LLMs appear capable of the main functions the loop requires:

- formulating and reformulating problems,
- generating tentative solutions,
- deriving consequences,
- criticizing alternatives,
- designing and interpreting tests,
- revising explicit knowledge,
- using retained knowledge in later work.

The capabilities can be imperfect: the cycle exists to expose and correct
errors.

## Formalize it, or leave it to people

Self-improving machines have a long history. Schmidhuber's
[program](https://people.idsia.ch/~juergen/recursive-self-improvement.html)
has pursued them since 1987: policies that modify their own update rules,
program search that reuses its earlier solutions, and the
[Gödel machine](https://arxiv.org/abs/cs/0309048), which may rewrite any part
of its own software — the proof searcher included — once it has proved that
the rewrite beats carrying on unchanged. These are real learning machines,
and the Gödel machine's optimality result is a formal theorem.

They require the work to be formalized first. The environment, the machine,
and the utility function enter as axioms, and a change is admitted by a proof
under them. The paper states the consequence: the machine "must ignore those
self-improvements whose effectiveness it cannot prove." This makes it
[a proof-governed case of self-modification](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md).
It is rigorous relative to its formalization and silent about whether that
formalization is adequate, since a valid proof under the wrong premises can
certify a change nobody wanted. The machine's starting program is costly
for the same reason: everything the first improvement needs has to be there
already, in executable form.

Beyond this restriction, the program leaves one operation unspecified.
Proving that a switch is beneficial under the current premises is one thing.
Revising those premises because cases have gone against them is another, and
the second is most of what open-ended learning consists of.

We know of no formalization of that operation, and Peter Naur argued that
there cannot be one: the judgments that relate a program to the world cannot
be reduced to formulated criteria, so the theory of a program is bound to the
people who hold it. As the knowledge base
[reconstructs that inference](../notes/naur-equates-machine-execution-with-formulated-criteria.md),
it needs one further premise: that a computer can make a judgment only by
executing criteria formulated in advance. Grant the premise and the work
divides in two. What can be formalized goes to machines, and what cannot
stays with people. Schmidhuber's constructions develop the first half as far
as it goes, and Naur's conclusion is what the second half implies.

This division leaves out a middle, because narrowing what an artifact can be
taken to mean is a [gradient](../notes/definitions/constraining.md). Defining
a term rules out some readings. A convention rules out more. A structured
document assigns meaning to positions in it. A schema or a validator rejects
the readings it does not admit. Only the last steps cross into a symbolic
medium, where a formal consumer assigns the consequences. That crossing is
[codification](../notes/definitions/codification.md). Every earlier step leaves natural language that an interpreter still has to read.
The choice between formalizing and leaving it to people treats the far end
of that gradient as the whole of it.

An LLM can be the interpreter for that middle. Suppose a definition is
written precisely enough to rule out the readings that would change what it
asks for. A model can then apply it to a case nobody anticipated when it was
written. Nothing assigns the definition its consequences, so this is not
formalization: wherever the words leave a choice open, the interpreter's
judgment decides. But the judgment is the model's, so the operation is not
left to people either.

This is why the theory builder is stated through definitions, and why so
much effort goes into those definitions. They say what it takes for later behaviour
to depend on a retained change, what lets criticism name one part of a
theory, and what a criticism has to do. Each is constrained as far as it will
go, and the interpreter handles the rest. Parts that stop changing can be
codified afterwards, one at a time, as the knowledge base's validators and
schemas have been. The rest stays open to criticism.

This position has costs. The first is how it fails. A proof gate fails
closed: it refuses every change it cannot certify, including the good ones.
An interpreter fails open. Given a definition that contradicts another, it
will apply either one and produce plausible work, and the medium gives no
sign of the contradiction. Error correction therefore has to be built into
the system. The second cost is that constraining can go too far: a
definition made more precise than the understanding behind it fixes a wrong
reading in place. The third is a lost guarantee. In the
earlier constructions a proof certified each accepted change. Here the
interpreter's judgments are hidden and have to be checked by other means.

## A distinct learning paradigm

If a fully automated theory builder learns, theory building is a distinct
learning paradigm and not just another agent workflow. The difference is
where its learning happens: in explicit, criticizable theories, and not only
in changes to model weights. Three payoffs follow from that difference.

**Learning without retraining.** New knowledge
[becomes usable as soon as it is retained](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md),
so the builder adapts at deployment time instead of waiting for the next
training run.

**Fewer observations after a shift.** A retained theory may
[reduce the observations needed after a shift](../notes/retained-theories-may-improve-sample-efficiency.md)
that preserves the structure it describes. This is the sample-efficiency
advantage most often claimed for explicit knowledge, and the linked note
states the conditions it depends on.

**Learned knowledge that can be read.** What the system has learned is held
as stated text: prose, and code where a part has been codified. It
can be read, diffed, tested, and reverted.

The reader can be an agent:
[inspectability is a property of the artifact's form](../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md),
so agents can do the reading at a volume people could not. What the system
has learned is available for oversight now, whatever the pace of weight
interpretability research.

Readability has a limit.
[A legible artifact need not be the one actually driving behaviour](../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md).
That is why the learning test below alters the retained state instead of
inspecting it: the medium makes the question testable, and the test settles it.

Three further advantages are conjectural. The payoffs above follow from the
form of the knowledge; these concern how well the loop learns. The knowledge
base develops each in its
[research companion](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#three-conjectures).

*Criticism carries content.* When a theory fails, the builder formulates
why. A stated diagnosis directs the next attempt differently from a bare
failure signal, and can save search that variant-and-select methods would
spend. A wrong diagnosis can also waste search. The conjecture concerns what
a supplied reason buys on balance.

*Theories can be revised in parts.* A theory whose assumptions and parts
can be inspected and revised individually lets criticism name a part, and
lets a revision keep the rest. The knowledge base
[defines this property](../notes/definitions/addressable-theory.md). It comes
in degrees, and the comparison is with a builder that criticizes and replaces
each theory whole. Naming a part can focus investigation and preserve useful
knowledge through a revision. It can also locate a fault in the wrong part.

*Persistence saves work.* The comparison holds decision quality fixed.
Keeping the assembled theory, and the criticism that shaped it, across
problems may cost less than keeping results only within one run. It may also
cost less than rebuilding them each time, whether from retained criticisms
or from records of inputs and outcomes alone.

Explicit knowledge also has costs. A retained theory requires retrieval,
applicability checks, revision, validation, and maintenance. A false
abstraction can misdirect many decisions, and a correct one that retrieval
misses is never used. Keeping episode records alongside distilled rules
[preserves a route for re-examining a rule](../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)
that turns out to be wrong. Construction, retrieval, maintenance, and
mistakes have to be counted on both sides of any comparison with a
weights-only learner.

The advantages and the costs are both empirical questions. The claim that
matters here is that the paradigm is possible. The companion states
[what the research program claims and what it does not](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#research-program-and-development-path).

## Compatible with the Bitter Lesson

[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
contrasts leveraging human knowledge with leveraging computation through
search and learning. That is a claim about how the content that determines a
system's behaviour gets made. It says nothing about the form the content is
kept in. Its folk version, *structure loses to weights*, turns it into a
claim about form. The lesson
[selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

Sutton himself leans toward the folk version. In a 2026
[interview](https://sequoiacap.com/podcast/rich-sutton-and-khurram-javed-why-ai-models-stop-learning-and-how-to-start-it-again),
he and Khurram Javed argue that forming new concepts needs continued weight
updating. That is a separate hypothesis: the bet runs against it, and the
essay does not establish it. The essay's own cases separate production from
form. Scale displaced hand-tuned weights as well as hand-written feature
extractors. The displaced methods spanned both forms, so what decided the
outcome was how the content was produced.

A theory builder sits on the computation side.
Its theories, criticism, tests, and revisions are explicit, but they need not
be supplied by people. A theory proposed, criticized, and revised by the loop
is a learned result whatever form it is retained in. And if the entire loop
is automated, additional computation buys more alternatives, stronger
criticism, more tests, and more revision of accumulated knowledge, which is
the work the lesson rewards.

The relevant distinction is therefore not between explicit knowledge and
scalable learning. It is between **human-supplied knowledge** and
**automatically generated, tested, and revised knowledge**.

One condition attaches. A builder that starts from hand-written theories and
method, as the one described here does, fits the lesson
[only if its learning outgrows that starting point](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation must come to supply the task-specific knowledge each new demand
needs.

## What would count as learning?

For learning to occur, the result of one episode must durably change the
system in a way that affects later behaviour:

> K(t) → conjecture and criticism → K(t+1) → different later behaviour

Here K is the retained state. In the first arrangement K is a knowledge
base: files holding theories, the criticism recorded against them, and the
instructions derived from them, which later runs read before acting.

This gives a direct empirical test in two parts. First, withholding or
altering the retained state should change later behaviour. A change that
passes this test is shown to be
[operative](../notes/definitions/operative-change.md): later behaviour
depends on it. Second, the changed behaviour should be better. Showing that
a theory was formulated, criticized, and revised, and that the revision was
used,
[does not by itself establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md),
because a builder can retain and faithfully apply a bad rule. The
[testing supplement](./testing-whether-a-theory-builder-learns.md) gives
tests that separate an operative change from an improvement, and states the
program's hypotheses and what would refute each.

The research question is therefore:

> **Can a fully automated fixed-weight LLM system maintain tentative theories,
> expose them to error, revise them, retain the revisions, use them in later
> work, and do better for it?**

We think the answer is yes.

## How Commonplace builds it

The bet is about what can be built. Commonplace is the knowledge base behind
this article, maintained by people and agents together. It builds a theory
builder reflectively from the start: the builder's own method is one of the
theories it states, criticizes, and revises. At first, people perform many
of its operations. The work is to move those operations to computation, and
the [bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
describes that path. Results are kept across problems, so they change later
work on other questions. The definition sets no minimum for how long results
persist.

A builder that learns could also keep a fixed method. Reflection is chosen
because an improvement to the method is paid for once and reused by every
later learning episode. Over a long horizon its return can exceed that of
immediate learning, and where it does,
[an optimal learning strategy invests in its own machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).
That return requires method improvements to compound: each one makes later
improvement cheaper, more reliable, or possible where it was not. Such
compounding is where recursive self-improvement begins. It takes more than
reflection, and the
[testing supplement](./testing-whether-a-theory-builder-learns.md) tests
learning first and compounding after.

## Where to go next

The [testing supplement](./testing-whether-a-theory-builder-learns.md)
defines the system under test, the three hypotheses, and the first protocol.
The [bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
starts from Commonplace and transfers its internal roles to computation one
class at a time. It also covers the builder's reflection on its own method.
The
[software-house supplement](./an-automated-software-house-as-a-second-test-of-a-theory-builder.md)
proposes a second arrangement whose failures are more visible. The
[survey](./which-existing-self-improving-systems-are-theory-builders.md) places
eighteen existing self-improving systems against the four conditions and
judges their reported gains separately. The
[definition](../notes/definitions/theory-builder.md) states exactly
what a theory builder requires and what it leaves open.
