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
---

# Bootstrapping a Fully Automated Learner with Commonplace

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

A fully automated [conjectural learner](./conjectural-learning-with-fixed-models.md)
does not have to be built in one step.

We start with a partially automated system in which a human operator and
automated machinery learn together. The key requirement is that what is
learned is retained in the system and changes later behaviour.

Commonplace is our implementation of this bootstrap.

## Retain learning in the system

The operator may initially contribute anywhere in the process: choosing
problems, criticizing results, interpreting evidence, approving changes, or
supplying missing capabilities.

We do not need to decide in advance which functions must already be
automated.

What matters is that successful learning leaves durable changes in the
system rather than remaining only in the operator's head. In Commonplace,
those changes can take the form of theories, instructions, schemas,
validators, tests, code, and other persistent artifacts.

Two conditions attach to this start. Sustaining the operator's supply of
the functions not yet automated requires a system people want to use, so
that the judgments they supply are part of work they would do anyway.
Commonplace is one: its operators build and use the knowledge base for
their own work, and
[that use is the initial selection environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md)
where no fixed oracle exists. And a hand-built start fits the Bitter Lesson
[only if learning outgrows it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation, not the operator, must come to supply the knowledge each new
demand needs.

## Use reflection to improve the learning machinery

Some of what the system learns can concern its own operation.

A recurring failure in review, decomposition, evaluation, or representation
can become an object of learning. The resulting knowledge can then change
the machinery used in future learning. A learner that holds such knowledge,
connected to its machinery in both directions, is what the knowledge base
calls a [reflective theory builder](../notes/definitions/reflective-theory-builder.md).

This creates a reflective feedback loop:

> learning → improved learning machinery → greater future learning capacity → further learning

Because an improvement to learning machinery is reused by every later
episode, its return grows with reuse. This is the argument developed in
[An optimal long-run learning strategy invests in its own machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).

## Move functions from the operator to the machinery

Automation grows one function at a time. A judgment the operator makes
repeatedly, and whose scope has stabilized, can become a test, a validator,
a procedure, or a search objective; the knowledge base calls this
[codification](../notes/definitions/codification.md). A function has moved
when computation now makes the decision and the change is recorded in the
system, so that a later reader can see what was transferred and when.

What does not move is named rather than hidden. A person still in the loop
is recorded as such, and their contribution is not credited to computation.
The residue is informative:
[transfer leaves people the decisions hardest to warrant](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md),
so the functions that remain with the operator say where the machinery is
still missing.

## Let the learner build its machinery

We do not assume that sustained self-improvement is possible through
natural-language changes alone while the surrounding software remains
fixed.

Some new theories may require new executable machinery: tools, experiments,
validators, search procedures, schedulers, or tests. Testing hypotheses
reliably or at scale may in particular require exact symbolic computation
rather than repeated LLM interpretation.

Commonplace therefore uses LLMs not only to revise retained knowledge, but
also to build and modify the software that operationalizes it.

Commonplace applies a deliberate division of labor between language-model
reasoning and symbolic software: the LLM can handle semantic interpretation,
while software handles exact bookkeeping, orchestration, and enforceable
checks when those tasks are more reliable there. This follows the
error-correction asymmetry described in
[Scheduler–LLM separation exploits an error-correction asymmetry](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).

The boundary is not fixed. The symbolic machinery is itself part of the
system and can be changed as learning reveals new requirements. With model
weights held fixed,
[procedures the learner acquires must persist outside the weights](../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md),
and code is one place they can live.

This leaves open a stronger possibility: sufficiently general learning may
require the ability to construct new software as new theories create new
ways of testing, organizing, and applying knowledge.

## The bootstrap

Commonplace is therefore an environment in which human-assisted learning is
retained, can be applied reflectively to the learning process, can move
function by function from the operator to the machinery, and can be turned
into new executable machinery.

The aim is to use that process to build the capabilities required for fully
automated learning.
