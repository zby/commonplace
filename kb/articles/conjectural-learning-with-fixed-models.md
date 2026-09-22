---
description: "Lead article: the bet that a fully automated conjectural learner, a Popperian conjecture-and-criticism cycle over explicit revisable theories, can be built from today's fixed-weight LLMs; conjectured payoff, Bitter Lesson fit, learning test"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/conjectural-learning.md
  - kb/notes/definitions/tentative-theory.md
  - kb/notes/definitions/addressable-theory.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/retained-theories-may-improve-sample-efficiency.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md
  - kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md
---

# Conjectural Learning with Today's LLMs

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

We propose a learning paradigm based on
[Popper's cycle for the growth of knowledge](https://doi.org/10.1016/S0049-237X(08)71204-7):

> problem → tentative solution → error elimination → revised problem

We call a system that implements this cycle a **conjectural learner**.

Its learned state is explicit and revisable. The system formulates problems,
proposes [tentative theories](../notes/definitions/tentative-theory.md) as
solutions, subjects them to criticism or tests, revises them in response, and
retains the result so that it changes later behaviour. The knowledge base
behind this article calls the process
[conjectural learning](../notes/definitions/conjectural-learning.md) and the
persistent system that carries it a
[theory builder](../notes/definitions/theory-builder.md); this article uses
the plainer name.

## The bet

Our bet is that **a fully automated conjectural learner can be built with
today's fixed-weight LLMs**.

Fully automated means that every internal role in the cycle is performed
computationally. Users still set the tasks and judge the results; what the
learner does not need from people is the formulation, criticism, and
revision of its own theories. The knowledge base states this boundary as the
definition of an
[autonomous theory builder](../notes/definitions/autonomous-theory-builder.md).

The learner is not the LLM alone. It is a system containing an LLM together
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

None of these capabilities needs to be perfect. The point of the cycle is
precisely to expose and correct errors.

## A distinct learning paradigm

If this works autonomously, conjectural learning is a distinct learning
paradigm rather than another agent workflow. Its learning happens through
explicit, criticizable theories rather than only through changes to model
weights, and that difference is where the paradigm's possible strengths and
costs come from.

We conjecture three advantages. The knowledge base develops each in its
[research companion](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md#three-conjectures).

**Criticism carries content.** When a theory fails, the learner formulates
why. A stated diagnosis directs the next attempt differently from a bare
failure signal, and can save search that variant-and-select methods would
spend. A wrong diagnosis can also waste it; the conjecture is about what a
supplied reason buys on balance.

**Theories are addressable.** A theory whose assumptions and parts can be
inspected and revised individually lets criticism name a part, and lets a
revision keep the rest. The knowledge base calls this property
[addressability](../notes/definitions/addressable-theory.md). It can focus
investigation and preserve useful knowledge through a revision; it can also
locate a fault in the wrong part.

**Retention beats reconstruction.** Keeping the assembled theory, and the
criticism that shaped it, spares the learner from rebuilding both from raw
records every time. Whether that saving holds at comparable decision quality
is the efficiency question the companion states in two comparisons.

Two further consequences follow directly. New knowledge becomes available
[without another weight-training cycle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md),
so the learner adapts at deployment time. And a retained theory may
[reduce the observations needed after a shift](../notes/retained-theories-may-improve-sample-efficiency.md)
that preserves the structure it describes, which is the sample-efficiency
advantage most often claimed for explicit knowledge; the note states the
conditions under which the claim is plausible.

Explicit state also has costs. A retained theory requires retrieval,
applicability checks, revision, validation, and maintenance. A false
abstraction can misdirect many decisions, and a correct one that retrieval
misses helps nobody. Keeping episode records alongside distilled rules
[preserves a route for re-examining a rule](../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)
that turns out to be wrong. Construction, retrieval, maintenance, and
mistakes have to be counted on both sides of any comparison with a
weights-only learner.

These are empirical questions. The important claim is that the paradigm is
possible. The bet sits within the
[recursive self-improvement program Schmidhuber describes](https://people.idsia.ch/~juergen/recursive-self-improvement.html),
with natural-language theories interpreted by LLMs in place of program
rewrites; the knowledge base
[states that positioning](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md#research-program-and-development-path)
and what it does not claim.

## Compatible with the Bitter Lesson

[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
does not require learning to happen through any particular internal
mechanism. It argues for general methods that scale with computation rather
than continued injection of human-designed knowledge. What loses in Sutton's
cases is not explicit structure as such. It is
[a claim whose reach was asserted rather than earned](../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md):
a generalization fitted to the cases its designers had in mind and never
tested against the cases that could refute it. Human authorship is the usual
way such claims are produced, not the property the lesson selects against.

Conjectural learning is compatible with the lesson on both counts. Its
theories, criticism, tests, and revisions are explicit, but they need not be
supplied by humans: the lesson
[selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md),
so a theory produced and selected by learning is a learned result whatever
form it is stored in. And error elimination is the step that earns reach. A
theory that has survived tests against refuting cases holds across the range
it claims, and a scalable search that reaches the same range finds the same
structure rather than replacing it. If the entire loop is automated,
additional computation buys more alternatives, stronger criticism, more
tests, and more revision of accumulated knowledge, which is the work the
lesson rewards.

The relevant distinction is therefore not between explicit knowledge and
scalable learning. It is between **human-supplied knowledge** and
**automatically generated, tested, and revised knowledge**.

Two conditions attach. A learner that starts from hand-written theories and
machinery, as ours does, fits the lesson
[only if its learning outgrows that starting state](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation, not people, must come to supply the task-specific knowledge
each new demand needs. And because an improvement to the learning machinery
is reused by every later episode,
[a long-run strategy should spend part of its effort on the machinery itself](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md),
directed at the methods that convert additional computation into capability.

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
a learner can retain and faithfully apply a bad rule. The
[testing supplement](./testing-the-conjectural-learning-program.md) states
the hypotheses that separate these outcomes and what would refute each.

The research question is therefore simple:

> **Can a fixed-weight LLM system autonomously maintain tentative theories,
> expose them to error, revise them, retain the revisions, use them in later
> work, and do better for it?**

We think the answer is yes.

## Where to go next

The [testing supplement](./testing-the-conjectural-learning-program.md)
defines the system under test, the three hypotheses, and the first protocol.
The [bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
starts from Commonplace, a knowledge base currently maintained by people and
agents together, and transfers its internal roles to computation one class at
a time; it also covers the learner's reflection on its own machinery. The
[software-house supplement](./an-automated-software-house-as-a-second-test-of-conjectural-learning.md)
proposes a second arrangement whose failures are more visible. The
[definition](../notes/definitions/conjectural-learning.md) states exactly
what the paradigm requires and what it leaves open.
