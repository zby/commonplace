---
description: "Bootstrap supplement: build a fully automated conjectural learner from a partially automated system that retains what operator and machinery learn, applies it reflectively to the learning machinery, and builds new software"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/codification.md
  - kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md
  - kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
---

# Bootstrapping a Fully Automated Learner with Commonplace

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

A fully automated [conjectural learner](./conjectural-learning-with-fixed-models.md)
does not have to be built in one step. We start with a partially automated
system in which a human operator and automated machinery learn together,
and require only that what is learned is retained in the system, changes
later behaviour, and changes it for the better; the lead article says how
that last condition is tested. Commonplace is our implementation of this
bootstrap.

## Retain learning in the system

The operator may contribute anywhere in the process: choosing problems,
criticizing results, interpreting evidence, approving changes, or supplying
missing capabilities. We do not need to decide in advance which functions
must already be automated.

This works only while the operator keeps contributing. That requires a
system people want to use, so that the judgments they supply are part of
work they would do anyway. Commonplace is built to be such a system: its operator builds and uses
the knowledge base for their own work, and
[that use is the initial selection environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md)
where no fixed test of a theory's fit yet exists.

What matters is that successful learning leaves durable changes in the
system rather than remaining in the operator's head. In Commonplace those
changes take the form of theories, instructions, schemas, validators, tests,
code, and other persistent artifacts.

## Use reflection to improve the learning machinery

Some of what the system learns concerns its own operation. A recurring
failure in review, decomposition, evaluation, or representation can become
an object of learning, and the resulting knowledge can change the machinery
used in future learning. A learner that holds such knowledge, connected to
its machinery in both directions, is what the knowledge base calls a
[reflective theory builder](../notes/definitions/reflective-theory-builder.md).

This closes a feedback loop:

> learning → improved learning machinery → greater future learning capacity → further learning

An improvement to the learning machinery is reused by the later episodes
that run through it, so its return grows with reuse. This is the argument of
[An optimal long-run learning strategy invests in its own machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).

One recorded episode shows the loop's first half.
[In a 2026-08-30 revision](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md),
the model read the retained project theory, searched over reformulations of
the research program, and proposed the edits; the operator supplied the
decisive judgments about which formulation fit; later commits built on the
revised state rather than reconstructing the old one. That shows retention
and later use. It does not show a change to the learning machinery, and no
improvement in later performance was demonstrated.

## Let the learner build its machinery

We do not assume that
sustained self-improvement is possible through natural-language changes
alone while the surrounding software stays fixed: a new theory may call for
new tools, experiments, search procedures, or schedulers, and testing
hypotheses reliably or at scale may require exact symbolic computation
rather than repeated LLM interpretation. Commonplace therefore uses LLMs not
only to revise retained knowledge but also to build and modify the software
that operationalizes it.

The division of labor is deliberate. The LLM handles semantic
interpretation; software handles exact bookkeeping, orchestration, and
enforceable checks, where it is more reliable, following the
error-correction asymmetry described in
[Scheduler–LLM separation exploits an error-correction asymmetry](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).
The boundary is not fixed: the software is part of the system and changes as
learning reveals new requirements. With model weights held fixed,
[procedures the learner acquires must persist outside the weights](../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md),
and code is one place they can live.

A stronger possibility stays open: general learning may not merely benefit
from this ability but require it, if new theories keep creating new ways of
testing, organizing, and applying knowledge.

## Move functions from the operator to the machinery

A hand-built start fits the Bitter Lesson
[only if learning outgrows it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation, not the operator, must come to supply the knowledge each new
demand needs. Automation therefore grows one function at a time, by one of two
routes. A judgment the operator makes repeatedly, once its scope has
stabilized, can be [codified](../notes/definitions/codification.md) into a
test, validator, or check with formal semantics. Or it can be delegated to
the LLM under a retained natural-language procedure, which automates the
judgment without making it a formal rule. A function has moved when
computation makes the decision and the change is recorded, so that a later
reader can see what was transferred, by which route, and when.

What does not move is recorded too. A person still in the loop is named as
such, and their contribution is not credited to computation. What remains with the operator is
informative:
[transfer leaves people the decisions hardest to warrant](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md),
so the functions that remain with the operator show where machinery is
missing, or where an objective is unsettled, authority is deliberately
kept, or transfer is not worth its cost.

## The bootstrap

Commonplace is therefore an environment in which what operator and
machinery learn together is retained, is applied reflectively to the learning process, is turned into
new executable machinery, and moves function by function from the operator
to that machinery. The aim is to use that process to build the capabilities
required for fully automated learning.

The hard part is not the recurring judgments. It is the work that currently
makes improvement possible at all: noticing the next problem, diagnosing it,
and deciding what would count as better. We conjecture that this process can
transfer that work too, not only the judgments it has already stabilized.
The conjecture fails, in the terms of
[the bootstrap condition](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
if the operator's share of that work grows with the system instead of
shrinking.
