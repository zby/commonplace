---
description: "Argues that explicit theory and symbolic machinery can be Bitter-Lesson-compatible only as provisional bootstrap state for a domain-extensible learning process that can produce, test, revise, and replace them"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
---

# The Bitter Lesson does not require everything to live in weights

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples and disputed scaling assumptions are welcome through the repository's issue tracker.

The strongest answer to the Bitter Lesson is not that explicit theories,
prompts, tests, schemas, and programs deserve an exemption. They do not. The
answer is that these artifacts can be provisional state in a search-and-learning
process that learns to produce, test, revise, and replace them.

That is the bet behind Commonplace. Its present knowledge base and agent
machinery are partly hand-crafted. The intended endpoint is not a larger set of
hand-written instructions for one area. It is a learning process that can form
project-specific theories and operative methods in areas that were not specified
when the process was designed, and that can eventually revise consequential
parts of its own learning machinery.

This is compatible with Richard Sutton's 2019 essay only if the path works. A
conceptual path beyond hand-crafting is not evidence that the system can follow
it. The Bitter Lesson therefore sets the central empirical burden for the
program rather than supplying a defense from that burden.

## The lesson is about how useful structure is produced

Sutton's historical claim is that methods built around human knowledge tend to
lose, over time, to general methods that exploit increasing computation through
search and learning. The familiar examples include computer vision and game
playing. Researchers designed features, heuristics, and decompositions that
encoded what they believed mattered. More general methods later found better
behavior through computation.

The contrast is about **production method**: whether behavior-shaping content is
specified by designers or selected through search and learning. It is not, by
itself, a rule that every learned result must be stored in model weights.

Hold the representation fixed and change the production method. One engineer
writes a prompt; an optimizer generates and selects another. Both results are
natural-language artifacts, but only the second update was selected through
search. An expert directly sets a dense controller vector; gradient descent
learns another in the same parameterization. Both results are distributed
numerical state, but only the second was learned. Representation affects which
learning methods are practical, but it is a different axis.

This distinction blocks a weights-only inference. It does not establish that
learning over explicit artifacts scales. A large interdependent corpus of
instructions, theories, tests, tool definitions, and programs has no equivalent
of a default chain rule telling the system which artifact should change after a
failure. Evaluation may be expensive, dependencies may be wrong, and the
artifact decomposition itself may be the source of the mistake.

## The important contrast is endpoint versus bootstrap

A hand-crafted starting point is not automatically contrary to the Bitter
Lesson. Every implemented learning system starts with supplied objectives,
representations, algorithms, or machinery. The important question is what the
starting structure permits the process to outgrow.

In the hand-designed vision and game-playing approaches Sutton criticizes,
designer knowledge formed the object-level solution for a predefined problem
class. The features or heuristics were intended to remain the source of
competence. The method could calculate inside the supplied structure, but it did
not contain a path by which evidence could replace the structure that bounded
it.

A bootstrap makes a different commitment. Its current theories, methods, tests,
and programs are working state for a process that can:

1. propose candidate theories and machinery;
2. expose them to consequences that can reject them;
3. retain, revise, or retire selected results;
4. change the artifact types, decompositions, routing, and evaluators when those
   choices become the bottleneck; and
5. repeat the process in a domain whose useful concepts were not enumerated in
   advance.

The fifth property is **domain-extensibility**. It is stronger than working in
several domains. A system can contain ten hand-built ontologies and ten special
update procedures while remaining a bundle of predefined solutions. A
domain-extensible system must be able to construct the project-specific theory,
representations, methods, and checks needed for an eleventh area without a
person first supplying another complete domain model.

This does not require a system to derive its own values. Objectives,
commitments, and grants of authority can remain supplied. The claim concerns how
the system acquires and revises the empirical and procedural structure used to
pursue those objectives.

## Editable artifacts are not enough

An agent that rewrites a prompt has crossed part of the production boundary. It
has not necessarily crossed very far. The prompt schema, mutation operator,
evaluator, routing policy, and acceptance rule may all remain fixed human
design. Search inside that decomposition can be useful while inheriting every
mistake the decomposition makes.

The bootstrap thesis therefore applies recursively. The current learning
machinery receives no exemption because it occupies a meta-level. A validator,
artifact type, theory-writing method, or blame-assignment procedure should
persist because it continues to earn its place, not because the original
designers placed it outside the update target.

This does not mean revising every layer on every run. That would make evaluation
and recovery impossible. It means that consequential fixed choices need a
reachable path by which evidence can challenge them. A system can begin with a
stable decomposition while retaining a slower route that can redraw it when
repeated failures show that the existing units no longer support useful credit
assignment.

At minimum, the learning path needs proposal, reject-capable evaluation, and
operative retention. A proposal without selection generates variation but no
learning. An evaluator that cannot reject plausible harmful candidates supplies
no correction. A selected result that does not affect later operation is a
report, not retained adaptation.

The difficult addition is credit assignment. A failed deployment rarely states
which theory, instruction, test, interface, or artifact boundary caused it.
Explicit dependency links, execution traces, retained episodes, and accumulated
checks can narrow the search, but no general method for a heterogeneous corpus
has yet been established. That is the machinery the program is trying to
bootstrap.

## Why explicit theory may help

Natural-language theory is not defended because humans wrote it. Its possible
advantage is that it can make a project-specific causal account available to the
learning process before that account has been reduced to a formal vocabulary.
The theory can identify what a change should preserve, interpret a failure, and
suggest whether the candidate or the current understanding should be revised.

This matters most under structured change. When a new demand preserves part of
the old causal structure, revising a named assumption or scope condition may
need less evidence than relearning behavior without an addressable intermediate
model. That is a sample-efficiency hypothesis, not an established general
advantage. Explicit theory also imposes retrieval, consistency, interpretation,
and maintenance costs.

The representation is therefore not the defense. The defense is the learning
path around it. A hand-written theory that remains protected knowledge is the
kind of structure the Bitter Lesson warns about. A theory proposed, criticized,
respecified, operationalized, and later retired by a general learning process is
one possible product and working state of the process the lesson favors.

## What Commonplace currently establishes

Commonplace is a human-assisted attempt to build this path. A language model can
work across natural-language and symbolic artifacts. Project theory can be
retained and routed into later work. Stable conclusions can become instructions,
validators, schemas, or code. Failures in using those artifacts can lead to
changes in the knowledge base and, sometimes, in the machinery that consumes it.

This is already useful, but it is not yet the claimed general learner. People
still identify many reusable lessons, assign blame, choose artifact forms,
construct or approve evaluators, authorize consequential changes, and repair
failures beyond represented coverage. The artifact ontology and many update
procedures remain designed rather than learned.

The current evidence supports a deliberately asymmetric position:

- The architecture is not categorically incompatible with the Bitter Lesson.
- It is a useful human-assisted bootstrap toward a compatible learning path.
- Whether it becomes a scalable, domain-extensible learner over heterogeneous
  artifacts remains the central open problem.

The third claim cannot be established by repeating the first two. It needs an
experiment in which production actually moves.

## A test that could change the claim

A serious test should introduce a demanding domain that was not used to design
the artifact ontology or improvement procedure. The system should have to form
new project-specific theory, construct operative methods and checks, receive
refuting evidence, and revise what it built. The retained result should then
change a later episode.

The evidence record should identify:

- which theories, methods, and checks were produced through search rather than
  written directly;
- which objectives, commitments, evaluators, and artifact boundaries remained
  supplied;
- whether a failure changed only an object-level artifact or also the
  decomposition and update procedure;
- whether the same general process transferred to another unanticipated domain;
- how much human evaluator construction, review, diagnosis, and repair was
  required; and
- how the total cost compared with simpler memory, stronger-model, and
  weight-update baselines.

The bootstrap account loses in a tested regime when every new domain needs a
bespoke ontology and oracle, when evaluation and maintenance grow faster than
the useful behavior retained, when failures require repository-wide human
review, or when the production machinery remains outside revision in practice.
It can also lose if stronger models absorb the useful functions more cheaply.
No current carrier is promised survival.

## The lesson becomes the research program

The Bitter Lesson does not require everything to live in weights. It requires
useful complexity to be earned by scalable search and learning rather than
protected as designer knowledge.

For explicit theory and symbolic machinery, that is a demanding standard. Their
localized form can make assumptions, scope, dependencies, and changes easier to
inspect and revise. It does not provide scalable proposal, evaluation, credit
assignment, or decomposition revision for free.

Commonplace should therefore be judged neither as a final hand-designed solution
nor as a conceptual exception. It is a bootstrap attempt. It succeeds only to
the extent that the production boundary moves: the system increasingly learns
to construct, test, retain, revise, and replace the artifacts and machinery that
currently depend on people, and carries that process beyond the domains the
designers anticipated.

The detailed [bootstrap thesis](../notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md)
states the failure conditions. The broader [production-method analysis](../notes/the-bitter-lesson-selects-production-methods-not-representational.md)
examines the missing credit-assignment and scaling machinery.
