---
description: "Bootstrap supplement: build an autonomous theory builder from a partially automated system that retains what operator and computation learn, applies it reflectively to the learning method, and builds new software"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/codification.md
  - kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md
  - kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/revising-an-improvement-objective-is-licensed-from-outside-it.md
  - kb/notes/increasing-computational-autonomy-relocates-human-effort.md
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
---

# Bootstrapping an Autonomous Theory Builder with Commonplace

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

An [autonomous](../notes/definitions/theory-builder.md#qualifiers)
[theory builder](./building-a-theory-builder-from-todays-llms.md) is one in
which computation performs every internal role in building theories:
noticing problems, diagnosing failures, producing and evaluating revisions, choosing which
theory to keep, and repairing the method by which it does this. It still has
people: users supply tasks and judge the results against what they asked
for.

Such a builder does not have to be built in one step. We start with a
partially automated system in which a human operator and computation learn
together. Because the builder includes whoever performs its internal
operations, such a system is already a theory builder, staffed partly by
people. The bootstrap changes who performs those operations. We require only
that what is learned is retained in the system, changes later behaviour, and
changes it for the better.
[The lead article](./building-a-theory-builder-from-todays-llms.md) says how
that last condition is tested. Commonplace is our implementation of this bootstrap.

## Retain learning in the system

Successful learning must leave durable changes in the system rather than
remain in the operator's head. In Commonplace those changes take the form of
theories, instructions, schemas, validators, tests, code, and other
persistent artifacts.

Who contributes the learning matters less at the start. The operator may
contribute anywhere in the process: choosing problems, criticizing results,
interpreting evidence, approving changes, or supplying missing capabilities.
We do not need to decide in advance which functions must already be
automated.

This works only while the operator keeps contributing, which requires a
system people want to use. Then the judgments they supply are part of work
they would do anyway. Commonplace is built to be such a system: its operator
builds and uses the knowledge base for their own work, and
[that use is what first selects theories for fit](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md),
before any fixed test of a theory's fit exists.

## Use reflection to improve the learning method

Some of what the system learns concerns its own operation. A recurring
failure in review, decomposition, evaluation, or representation can become
an object of learning, and the resulting knowledge can change the method
used in future learning. A builder whose methods are stated as theories,
consumed by its operations and criticized against records of its own
operation, is what the knowledge base calls
[reflective](../notes/definitions/theory-builder.md#qualifiers).

This opens a feedback loop:

> learning → improved learning method → greater future learning capacity → further learning

An improvement to the method would be reused by every later episode, so over
a long horizon its return can exceed that of immediate learning, and where
it does,
[an optimal long-run learning strategy invests in its own machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).

Reflection makes the method open to criticism, but that alone does not close
the loop. The loop closes only when method changes also compound, making
later improvement cheaper, more reliable, or possible where it was not. That
takes two further things. The builder must be able to change its method
beyond revising text, which the next section takes up. Its evaluators must be
able to tell a better method from a worse one, and approval from the
builder's theory of its own method does not count as that evidence. Showing
that compounding happened takes a later improvement episode, measured on
something other than the check that accepted the change, with a trace
connecting the two; the
[compounding test](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md)
states what counts.

So far the record shows only the loop's starting point: retention and later
use, with no change to the learning method and no demonstrated improvement in
later performance.
[In a 2026-08-30 revision](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md),
the model read the retained project theory, searched over reformulations of
the research program, and proposed the edits. The operator supplied the
decisive judgments about which formulation fit. Later commits built on the
revised state rather than reconstructing the old one.

## Let the builder build its own software

Improving the method can take more than revising text. A new theory can
call for new tools, experiments, search procedures, or schedulers. Testing
hypotheses reliably or at scale can require exact symbolic computation
instead of repeated LLM interpretation. So Commonplace does not count on
natural-language changes around fixed software to sustain self-improvement.
It uses LLMs both to revise retained knowledge and to build and modify the
software that puts it into operation.

The LLM handles semantic interpretation. Software handles exact
bookkeeping, orchestration, and enforceable checks, where it is more
reliable, following
[the error-correction asymmetry between schedulers and LLMs](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).
The boundary between them moves: the software is part of the system and
changes as learning reveals new requirements. With model weights held
fixed,
[procedures the builder acquires must persist outside the weights](../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md),
and code is one place they can live.

General learning may even require this ability, if new theories keep
creating new ways to test, organize, and apply knowledge.

## Move functions from the operator to computation

A hand-built start fits Richard Sutton's Bitter Lesson
[only if learning outgrows it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation, not the operator, must come to supply the knowledge each new
demand needs. Automation therefore grows one function at a time.

A judgment the operator makes repeatedly can move by one of two routes once
its scope has stabilized. It can be [codified](../notes/definitions/codification.md)
into a test, validator, or check with formal semantics, which settles the
judgment in the retained method. Or it can be delegated to the LLM under a
retained natural-language procedure, which automates the judgment while the
method leaves it open. These are
[different changes](../notes/methodological-and-computational-closure-track-different-changes.md),
and the record should say which one happened.

A function has moved when computation makes the decision and evidence shows
that it decides adequately within a stated scope. The evidence condition
matters because handing a decision to an unattended model is easy;
[a computational decision can be trusted only where its checks are reliable](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).
Transfer also runs both ways: a function returns to the operator when its
check turns out to be a poor stand-in for what it was meant to catch.

Each transfer and each return is recorded, so that a later reader can see
what moved, by which route, and when. So is what has not moved. A person
still in the loop is named as such, and their contribution is not credited
to computation. That record is informative, because
[transfer leaves people the decisions hardest to warrant](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).
The functions that remain with the operator show where the means to
automate them are missing, where an objective is unsettled, where authority
is deliberately kept, or where transfer is not worth its cost.

## The bootstrap

Commonplace is therefore an environment in which what the operator and
computation learn together is retained, applied reflectively to the learning
method, turned into new software, and moved function by function from the
operator to computation. The aim is to use that process to build the
capabilities an autonomous theory builder requires.

The hard part is the work that currently makes improvement possible at all: noticing the next problem, diagnosing it,
and deciding which change serves the objective better. We conjecture that
this process can transfer that work too, not only the judgments it has
already stabilized. The conjecture does not cover choosing the objective
itself. The objective stays declared, and
[changing it counts as improvement only against a standard outside it](../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md).

Operator time does not measure progress. In an open-ended system,
[attention freed from routine work moves to harder work](../notes/increasing-computational-autonomy-relocates-human-effort.md),
so the operator's hours can stay flat while the bootstrap succeeds. The
measure is the number of human decisions each completed, verified
improvement requires. The conjecture fails, in the terms of
[the bootstrap condition](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
if that number grows with the system instead of falling. The strongest
evidence of success is
[a removal test](../notes/computationally-directed-self-improvement-is-a-reallocation.md):
withhold the operator's decisions and check whether an improvement process
still completes, over a stated scope and time horizon. The
[testing supplement](./testing-whether-a-theory-builder-learns.md) says how
these decisions are recorded.
