---
description: "Definition — a theory builder grows objective knowledge by conjecture and refutation: it states theories in localized units, acts on them, criticizes what the units say, and retains the results; learning is tested, not assumed"
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

1. **Localized content.** Its theories are stated in natural or formal
   language, so identifiable units carry their content: each unit says
   something that can be pointed at. This is the localized side of
   [representational form](./representational-form.md). Popper's objective
   knowledge is knowledge "contained in a book; or stored in a library"
   ([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)),
   and he holds that criticism needs this form: without a descriptive
   language "there can be no object for our critical discussion"
   ([Popper 1968](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
2. **Consumption.** Its theories guide what it does through what they say.
   In Popper's words, "all our actions in the first world are influenced by
   our second-world grasp of the third world"
   ([Popper 1968](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)).
   A difference in a theory's content that matters to a decision changes the
   decision ([operative change](./operative-change.md)).
3. **Criticism.** It has a working process of attempted refutation aimed at
   what identified units say: critical argument, comparison with rivals, and
   tests of stated consequences. A criticism is itself stated, so it can be
   criticized in turn; in particular, it can blame the test, the data, or an
   auxiliary assumption instead of the theory. Theories that fail are
   revised, or rejected whole and replaced by a new conjecture. Revision need
   not be small: it may change a core assumption, the problem, or the
   machinery.
4. **Growth.** It retains its theories and the record of their criticism, so
   that the new problem `P2` becomes the starting point of later work. A
   builder that keeps only the record of criticism and rebuilds a theory from
   it when needed also meets this condition: the rebuilt theory is a new
   conjecture informed by the retained criticism. Later work consumes what is
   retained, and in Popper's sense consumption includes "criticising them,
   changing them, and often even demolishing them, in order to replace them
   by better ones" ([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
   Retention counts when what is kept is taken up on a new problem. Rounds
   of revision on one problem, however many, are one pass of error
   elimination; the unit is the problem, not the process run, so a single
   run that carries its results into later, different problems meets the
   condition.

**Criticism against gradient descent.** Gradient descent also eliminates
error, and it assigns blame more finely than any text: every parameter gets
its share. But no parameter says anything by itself, so the blame cannot be
stated as an error in what the theory says, and it cannot be argued with; the
loss and the data are fixed from outside the process. This is Popper's
distinction between the critical method and trial and error, which is applied
"in a more dogmatic fashion, by the amoeba also"; the difference "lies not so
much in the trials as in a critical and constructive attitude towards errors"
([Conjectures and Refutations, Chapter 1](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
Conditions 1 and 3 together draw this line: localization supplies units that
say something, and criticism aims at what they say.

**Error elimination is attempted, not guaranteed.** The parentheses in
Popper's "(attempted) error-elimination" are his. A builder whose criticism
finds nothing, or whose revisions do not improve later work, is still a
theory builder. Whether a theory builder learns, in the sense of improving
its capacity for future action
([Simon's criterion](../learning-is-not-only-about-generality.md)), is an
empirical question about it. The definition does not settle it.

## Addressability

Condition 1 sets the minimum: some unit carries content, even if that unit is
the whole theory. Above the minimum,
[addressability](./addressable-theory.md) comes in grades: the finer the
units, the more precisely criticism can name what it blames. At the high end,
a theory's assumptions, scope conditions, and parts are stated separately and
can be revised individually. Popper grants Duhem that a test often bears on a
whole system, but replies: "It is possible in quite a few cases to find which
hypothesis is responsible for the refutation"
([Conjectures and Refutations, Chapter 10](../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
Commonplace builds for the high end. That this pays is a conjecture, tested
against builders whose theories are coarser.

Addressability is relative to the unit criticism names, and this applies to
the machinery as well as to the theories. A model is not localized inside,
but as a component of the builder it is an addressable part: a method text or
configuration states which model does which work, criticism can blame that
choice, and the builder can replace the model whole. What the builder cannot
do is criticize what the model's weights say, because no unit in them says
anything.

## Boundary

The builder is the whole system that performs the operations above: people,
models, tools, and retained texts. The operations are proposing a theory,
deriving what it implies, criticizing it, choosing what to blame, producing a
revision, selecting the theory to keep, and changing the machinery that does
these things. Users who supply problems and judge the products are outside
the builder unless they perform one of these operations. The boundary follows
the operation, not the person, so a claim about a builder declares the
boundary it assumes.

Retention is the builder's, not the interpreter's: a model may propose and
evaluators may assess, but what is kept for later work is decided by the
builder's process.

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
  finds the gap. Reflection reaches the models only as addressable parts: the
  builder can hold theories about a model and criticize the choice of it, but
  it changes the model only through what it gives the model or by replacing
  it.
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
- **Criticism applied through weights.** Critique-trained reinforcement
  learning and "textual gradient" methods state a criticism, then use it to
  update weights. The revised theory is the weights, where no unit says
  anything, so the arrangement is outside. It becomes a builder only when the
  criticism aims at a stated theory that the system retains and consumes.
- **Content located in weights.** Model editing and interpretability methods
  can find weights that carry a particular fact. To that extent those parts
  of a model move toward the localized side, and criticism aimed at them can
  meet condition 3. The definition tracks localization, not substrate, so
  whether weights are excluded is an empirical question about a given model
  and method.
- **The Gödel machine** stays open. Its switching is governed by proof from
  premises that the construction does not criticize; whether a deployment
  criticizes them elsewhere is not settled by the construction. See
  [Gödel machines are a proof-governed case of self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md).

## Exclusions

- **Dispositions and weight adaptation.** Popper counts expectations and
  dispositions as tentative theories in a wider sense. Their content is not
  localized, so they fail condition 1, and adjusting them by gradient fails
  condition 3. A system whose only change is weight adaptation is not a
  theory builder. Its models can still be components of one.
- **Black-box optimization.** Variants of prompts or programs are generated
  and kept by outcome score, with no stated reason bearing on what a variant
  says. The variants are localized, but selection does not aim at what they
  say, so this is trial and error and fails condition 3. Real systems fall
  between this case and a builder; the test is whether a stated reason bears
  on what a unit says.
- **A fixed theory.** A stated theory guides decisions and the system never
  criticizes it. It fails condition 3.
- **Work on one problem only.** A theory built while reasoning and then
  discarded fails condition 4. So does iterated refinement on a single
  problem, such as one invocation of FORTE over a supplied theory and
  training set, or counterexample-guided synthesis of one program: the
  rounds are one pass of error elimination, and nothing is taken up on a new
  problem. This does not classify a larger system that uses the procedure.
- **A stored theory nothing consumes.** It fails condition 2. See
  [an action model matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md).

## Misuse Cases

- Calling a model, a prompt, a harness, or a review pipeline a theory builder
  when it is one component of the system that performs the operations.
- Counting a system as a theory builder because it stores prose about its
  subject or itself. Storage satisfies condition 1 at most.
- Reading membership as evidence of learning. A builder can criticize and
  revise without improving; improvement needs its own comparison.
- Counting a user inside the builder because their problems or verdicts
  changed a theory, when they performed none of the internal operations.

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — defined-in: the status of every theory the builder holds
- [Representational form](./representational-form.md) — grounds: the localization axis that condition 1 uses
- [Addressable theory](./addressable-theory.md) — defined-in: the graded property above condition 1's minimum
- [Reflective system](./reflective-system.md) — defined-in: the causal connection the reflective qualifier requires
- [Learning is not only about generality](../learning-is-not-only-about-generality.md) — grounds: the sense of learning the definition leaves to test
- [Commonplace studies conjectural learning through retained theories](../commonplace-studies-conjectural-learning-through-retained-theories.md) — extends: the research program's conjectures about builders
- [Popper, A realist view of logic, physics, and history](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) — evidenced-by: the schema, objective knowledge, and consumption
- [Popper, Epistemology without a knowing subject](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) — evidenced-by: formulation as a condition of criticism, action guided by objective knowledge, self-criticism
- [Popper, Conjectures and Refutations](../../sources/popper-conjectures-and-refutations.ingest.md) — evidenced-by: the critical method against trial and error, and locating the refuted hypothesis
