---
description: "Bootstrap supplement: build an autonomous theory builder from a partially automated system that retains what operator and machinery learn, applies it reflectively to the learning machinery, and builds new software"
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

A fully automated [theory builder](./building-a-theory-builder-from-todays-llms.md)
is not a builder without people. It is one in which computation performs
every internal role in building theories: diagnosing failures, producing and
evaluating revisions, choosing which theory to keep, and repairing the
machinery that does this. Users still supply tasks and judge the results
against what they asked for. The knowledge base calls such a builder
[autonomous](../notes/definitions/theory-builder.md#qualifiers).

Such a builder does not have to be built in one step. We start with a
partially automated system in which a human operator and automated machinery
learn together. Because the builder includes whoever performs its internal
operations, such a system is already a theory builder, staffed partly by
people; what the bootstrap changes is who performs those operations. We
require only that what is learned is retained in the system, changes later
behaviour, and changes it for the better; the lead article says how that last
condition is tested. Commonplace is our implementation of this bootstrap.

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
[that use is the initial selection environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md)
where no fixed test of a theory's fit yet exists.

## Use reflection to improve the learning machinery

Some of what the system learns concerns its own operation. A recurring
failure in review, decomposition, evaluation, or representation can become
an object of learning, and the resulting knowledge can change the machinery
used in future learning. A builder whose methods are stated as theories,
consumed by its operations and criticized against records of its own
operation, is what the knowledge base calls
[reflective](../notes/definitions/theory-builder.md#qualifiers).

This closes a feedback loop:

> learning → improved learning machinery → greater future learning capacity → further learning

Every later episode that runs through improved machinery reuses the
improvement, so its return grows with reuse. That is why
[an optimal long-run learning strategy invests in its own machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).

So far the record shows only what the loop starts from.
[In a 2026-08-30 revision](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md),
the model read the retained project theory, searched over reformulations of
the research program, and proposed the edits; the operator supplied the
decisive judgments about which formulation fit; later commits built on the
revised state rather than reconstructing the old one. That shows retention
and later use. It does not show a change to the learning machinery, and no
improvement in later performance was demonstrated.

## Let the builder build its machinery

Improving the machinery may take more than revising text. A new theory may
call for new tools, experiments, search procedures, or schedulers, and
testing hypotheses reliably or at scale may require exact symbolic
computation rather than repeated LLM interpretation. We therefore do not
assume that sustained self-improvement is possible through natural-language
changes alone while the surrounding software stays fixed. Commonplace uses
LLMs both to revise retained knowledge and to build and modify the software
that puts it into operation.

The division of labor is deliberate. The LLM handles semantic
interpretation. Software handles exact bookkeeping, orchestration, and
enforceable checks, where it is more reliable, following
[the error-correction asymmetry between schedulers and LLMs](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).
The boundary between them is not fixed: the software is part of the system
and changes as learning reveals new requirements. With model weights held
fixed,
[procedures the builder acquires must persist outside the weights](../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md),
and code is one place they can live.

A stronger possibility stays open: general learning may not merely benefit
from this ability but require it, if new theories keep creating new ways of
testing, organizing, and applying knowledge.

## Move functions from the operator to the machinery

A hand-built start fits the Bitter Lesson
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
The functions that remain with the operator show where machinery is
missing, where an objective is unsettled, where authority is deliberately
kept, or where transfer is not worth its cost.

## The bootstrap

Commonplace is therefore an environment in which what operator and
machinery learn together is retained, applied reflectively to the learning
process, turned into new executable machinery, and moved function by
function from the operator to that machinery. The aim is to use that
process to build the capabilities required for fully automated learning.

The hard part is not the recurring judgments. It is the work that currently
makes improvement possible at all: noticing the next problem, diagnosing it,
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
