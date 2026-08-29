---
description: "A hand-crafted starting state is compatible with the Bitter Lesson only when it is provisional state for a domain-extensible search-and-learning process that can produce, revise, and replace the bootstrap itself"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, foundations]
---

# A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it

[The Bitter Lesson selects production methods rather than representational
forms](./the-bitter-lesson-selects-production-methods-not-representational.md).
Its target is useful structure that continues to be supplied by designers when
a more general search-and-learning method can discover better structure by
using increasing computation. Starting from hand-crafted artifacts is not by
itself a counterexample to the lesson. The decisive question is whether those
artifacts are the intended endpoint or provisional state in a process that can
learn to replace them.

A hand-crafted bootstrap is compatible with the lesson only when the learning
path can outgrow both its initial content and consequential parts of the
machinery that produced that content. The bootstrap must make a more general
learning process operable; it cannot be a protected store of domain knowledge
that the process only applies.

## Bootstrap state is not final domain knowledge

The hand-designed vision and game-playing approaches in Sutton's comparison
put designer knowledge into the object-level solution for a predefined problem
class. Their methods could use computation inside that design, but they did not
provide a path by which search and learning could replace the designed features,
knowledge, or decomposition that bounded the solution. The later general
methods won by changing how useful structure was produced.

The bootstrap thesis makes a different claim about present theories,
methodologies, prompts, schemas, validators, and programs. They are working
state for a process intended to:

1. propose candidate theories and machinery;
2. test them against consequences that can reject them;
3. retain, revise, or retire selected artifacts;
4. revise the artifact types, decompositions, routing, and evaluators when those
   choices become the bottleneck; and
5. repeat the process in domains whose useful concepts were not enumerated when
   the system was designed.

The fifth condition is **domain-extensibility**. It is stronger than competence
in several domains. A system with ten hand-built ontologies and ten specialized
update procedures is still a collection of predefined solutions. A
domain-extensible process can construct the project-specific theory,
representations, methods, and checks needed for an eleventh domain without a
person first supplying another complete domain model.

Domain-extensibility does not mean that the system invents its own objective.
An objective or commitment may remain supplied, [because self-improvement is
relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md).
The claim concerns how the system acquires and revises the knowledge and
machinery used to pursue that objective.

## The learning path must reach its own scaffolding

Editable files are not enough. A model can rewrite a prompt while the prompt
schema, mutation operator, evaluator, routing policy, and acceptance rule remain
fixed human design. That is a bounded learned update inside a hand-crafted
decomposition. It may be useful, but it does not establish the bootstrap thesis.

The thesis requires a reachable path beyond each consequential fixed choice.
The path need not revise every layer at once, and some authority may remain
outside it. It must nevertheless expose the current machinery to evidence and
permit replacement when a better production method earns warrant. This is the
recursive consequence of the rule that [reflective machinery persists by
warrant rather than by its position in the loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).

A bootstrap-compatible system therefore needs more than proposal. It needs a
[proposal-selection loop with search, reject-capable evaluation, and operative
retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md),
plus credit assignment rich enough to identify which theory, artifact, or
production rule should change. It also needs a way to revise a decomposition
without losing every unit of attribution and validation, because [learning
inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

## What would distinguish the thesis from a story

The strongest test introduces a demanding domain that was not used to design
the artifact ontology or improvement procedure. The system should have to form
new project-specific theory, derive or construct operative methods, expose them
to independent consequences, and revise them after a failure. The same general
learning process should carry the episode without a person supplying a new
special-purpose representation and evaluator for each step.

Evidence should track at least:

- which candidate artifacts and machinery were produced by search rather than
  written directly;
- whether an outcome changed the theory, decomposition, or update procedure;
- whether the retained change altered a later episode;
- how much domain-specific human judgment, evaluator construction, review, and
  repair the episode required; and
- whether the process transfers to another unanticipated domain without a new
  hand-built learning architecture.

The claim fails as a scaling account when useful artifact production remains
artisanal, when each new domain requires a bespoke ontology and oracle, when the
human evaluation burden grows with the artifact corpus, or when the core
production machinery is outside revision in practice.

## Where Commonplace currently stands

Commonplace is a human-assisted bootstrap toward this architecture. A language
model can interpret and propose changes across heterogeneous natural-language
and symbolic artifacts. Retained theory can guide later work, and stable parts
can become instructions, validators, schemas, or code. The system can also turn
its theory toward parts of its own operation.

The decisive production work has not moved far enough to establish the thesis.
People still choose objectives, identify many reusable lessons, assign blame,
decide which representation to use, construct or approve evaluators, and accept
consequential changes. Current evidence supports a useful bootstrap and a
coherent path to test. It does not yet show a scalable, domain-extensible
learning method over explicit artifacts.

## Scope

- Compatibility is a property of a declared learning path, not of an artifact
  class or a stated intention. A path becomes compatible only where search and
  evidence actually take over production.
- The claim does not predict that natural-language or symbolic artifacts will
  remain separate carriers. Learned functions may migrate into other
  representations while the learning path remains compatible.
- A fixed component can remain justified where changing it is outside the
  objective, unsafe, or uneconomic. The bootstrap thesis fails only when fixed
  designer choices are presented as a general learning path beyond their
  actual revision surface.
- Domain-extensibility is an empirical burden. General semantic competence in
  the base model makes it plausible; it does not demonstrate it.

## Open Questions

- What sequence of domains would distinguish domain-extensible artifact
  learning from a broad but still predefined ontology?
- How can evaluators for a new domain be learned without merely moving unlimited
  human judgment into evaluator construction?
- Which production choices must become revisable before a bootstrap counts as
  more than a collection of bounded automation envelopes?

---

Relevant Notes:

- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: supplies the production-method axis that makes a learned explicit artifact coherent
- [Machinery persists by warrant, not position in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — grounds: extends the production requirement recursively to the learning machinery
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: supplies the minimum loop that turns provisional artifacts into learned state
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why editable object-level artifacts are insufficient when the update space remains fixed
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: supplies one empirical reason explicit theories might earn a role inside the bootstrap
