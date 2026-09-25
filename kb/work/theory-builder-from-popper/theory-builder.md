---
description: "Definition — a theory builder grows objective knowledge by conjecture and refutation: it formulates theories, acts on them, criticizes them, and retains the results; learning is tested, not assumed"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Theory builder

<!-- Maintenance: when changing this definition, please apply the checks in
[theory-builder-checks.md](./theory-builder-checks.md). -->

A **theory builder** is a system that grows knowledge by Popper's method of
conjecture and refutation, applied to theories it keeps as objective
knowledge. It works through Popper's schema `P1 → TT → EE → P2`: faced with a
problem, it proposes a [tentative theory](./tentative-theory.md), attempts to
eliminate its errors, "especially by way of critical discussion", and takes
up the new problems that result
([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
The KB needs the term to name the kind of system Commonplace builds and
studies.

A system is a theory builder when it meets four conditions, each stated in
Popper's terms.

1. **Objective knowledge.** Its theories are formulated in language and kept
   as products outside any single mind or model. Popper's objective knowledge
   is knowledge "contained in a book; or stored in a library"
   ([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
   He also holds
   that criticism needs this form: without a descriptive language "there can
   be no object for our critical discussion"
   ([Popper 1968](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
2. **Consumption.** Its theories guide what it does through what they say.
   In Popper's words, "all our actions in the first world are influenced by
   our second-world grasp of the third world"
   ([Popper 1968](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
   A difference in a theory's content that matters to a decision changes the
   decision ([operative change](./operative-change.md)).
3. **Criticism.** It has a working process of attempted refutation aimed at
   what its theories say: critical argument, comparison with rivals, and
   tests of stated consequences. Theories that fail are revised, or rejected
   whole and replaced by a new conjecture. Revision need not be small: it may
   change a core assumption, the problem, or the machinery. Popper separates this critical method from trial and error, which
   is applied "in a more dogmatic fashion, by the amoeba also"; the
   difference "lies not so much in the trials as in a critical and
   constructive attitude towards errors"
   ([Conjectures and Refutations, Chapter 1](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
4. **Growth.** It retains its theories and the record of their criticism, so
   that the new problem `P2` becomes the starting point of later work. A
   builder that keeps only the record of criticism and rebuilds a theory from
   it when needed also meets this condition: the rebuilt theory is a new
   conjecture informed by the retained criticism. Later work consumes what is
   retained, and in Popper's sense consumption includes "criticising them,
   changing them, and often even demolishing them, in order to replace them
   by better ones" ([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).

**Addressability is a design commitment, not a condition.** How
[addressable](./addressable-theory.md) a part of the builder is comes in
grades. At the high end, a theory's assumptions, scope conditions, and parts
can be inspected and revised individually, so criticism can name the part it
blames. At the low end, a component can only be replaced whole: a model's
weights are revised by fine-tuning them without addressing parts, or by
replacing the model. Popper grants Duhem that a test often bears on a whole
system, but replies: "It is possible in quite a few cases to find which
hypothesis is responsible for the refutation"
([Conjectures and Refutations, Chapter 10](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
Commonplace builds for the high end. That this pays is a conjecture, tested
against builders whose theories are less addressable.

**Error elimination is attempted, not guaranteed.** The parentheses in
Popper's "(attempted) error-elimination" are his. A builder whose criticism
finds nothing, or whose revisions do not improve later work, is still a
theory builder. Whether a theory builder learns, in the sense of improving
its capacity for future action
([Simon's criterion](../learning-is-not-only-about-generality.md)), is an
empirical question about it. The definition does not settle it.

## Boundary

The builder is the whole system that performs the operations above: people,
models, tools, and retained texts. The operations are proposing a theory,
deriving what it implies, criticizing it, choosing what to blame, producing a
revision, selecting the theory to keep, and changing the machinery that does
these things. Users who supply problems and judge the products are outside
the builder unless they perform one of these operations. The boundary follows
the operation, not the person, so a claim about a builder declares the
boundary it assumes.

The builder is identified by its continuing process, not by any component.
Every theory, procedure, and model in it may be replaced over time through
its own criticism and revision. A change installed from outside that process
is an intervention and is recorded as one.

## Qualifiers

- **Reflective.** The builder's method is part of its objective knowledge.
  The problems it works on, its standards of criticism, and its procedures
  meet the four conditions, as its other theories do. Popper places these
  objects in the third world: only there "the problems and standards of
  rational criticism can develop"
  ([Popper 1968](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
  A procedure is a tentative solution to a problem about how to build
  theories. Criticism aims at its stated conjecture about why it works, so a
  procedure with no stated purpose can be tried but not criticized.
  The causal connection that [reflective system](./reflective-system.md)
  requires runs through conditions 2 and 3: the builder's operations consume
  the method texts, and criticism tests those texts against records of the
  builder's own operation. Popper describes the human version as "the give
  and take between ourselves and our work", with "feed-back that can be
  amplified by self-criticism"
  ([Popper 1968](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
  Unlike computational reflection, this connection is not kept up
  automatically. When the machinery changes outside the texts, for example
  when a model is replaced, text and operation can diverge until criticism
  finds the gap. Reflection covers only the formulated part of the method.
  The interpreter's weights are not objective knowledge: the builder can hold
  theories about them, but it changes them only through what it gives them or
  by replacing them.
- **Autonomous.** Computation performs every operation inside the boundary.
  Users still supply problems and judge products. Autonomy does not
  establish that the operations are reliable.

The qualifiers are independent. Commonplace today is a reflective,
human-staffed theory builder; the research program's bet is an autonomous one.

## Boundary cases

- **A research community** is a theory builder, with the community as the
  declared system. It is Popper's own case. No single member holds the whole
  theory or supplies all the criticism.
- **Commonplace's note-review loop**, with the operator performing internal
  operations, is a human-staffed theory builder.
- **The Gödel machine** stays open. Its switching is governed by proof from
  premises that the construction does not criticize; whether a deployment
  criticizes them elsewhere is not settled by the construction. See
  [Gödel machines are a proof-governed case of self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md).

## Exclusions

- **Dispositions and weights.** Popper counts expectations and dispositions
  as tentative theories in a wider sense. They are not formulated, so they
  fail condition 1. A system whose only change is weight adaptation is not a
  theory builder. Its models can still be components of one.
- **Black-box optimization.** Variants of prompts or programs are generated
  and kept by outcome score, with no stated reason bearing on what a variant
  says. This is trial and error, and it fails condition 3. Real systems fall
  between this case and a builder; the test is whether a stated reason bears
  on what the theory says.
- **A fixed theory.** A formulated theory guides decisions and the system
  never criticizes it. It fails condition 3.
- **A single run without retention.** A theory built while reasoning and then
  discarded, or one invocation of a refinement procedure such as FORTE, fails
  condition 4. This does not classify a larger system that uses the
  procedure.
- **A stored theory nothing consumes.** It fails condition 2. See
  [an action model matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md).

## Misuse Cases

- Calling a model, a prompt, a harness, or a review pipeline a theory builder
  when it is one component of the system that performs the operations.
- Counting a system as a theory builder because it stores prose about its
  subject or itself. Storage satisfies none of conditions 2 to 4.
- Reading membership as evidence of learning. A builder can criticize and
  revise without improving; improvement needs its own comparison.
- Counting a user inside the builder because their problems or verdicts
  changed a theory, when they performed none of the internal operations.

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — defined-in: the status of every theory the builder holds
- [Addressable theory](./addressable-theory.md) — defined-in: the graded structural property the builder is designed for
- [Reflective system](./reflective-system.md) — defined-in: the causal connection the reflective qualifier requires
- [Learning is not only about generality](../learning-is-not-only-about-generality.md) — grounds: the sense of learning the definition leaves to test
- [Commonplace studies conjectural learning through retained theories](../commonplace-studies-conjectural-learning-through-retained-theories.md) — extends: the research program's conjectures about builders
- [Popper, A realist view of logic, physics, and history](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) — evidenced-by: the schema, objective knowledge, and consumption
- [Popper, Epistemology without a knowing subject](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) — evidenced-by: formulation as a condition of criticism, action guided by objective knowledge, self-criticism
- [Popper, Conjectures and Refutations](../../sources/popper-conjectures-and-refutations.ingest.md) — evidenced-by: the critical method against trial and error, and locating the refuted hypothesis
