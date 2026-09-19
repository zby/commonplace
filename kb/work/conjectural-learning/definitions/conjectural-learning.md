---
description: "Definition — conjectural learning is Popper's process run by a system in which an addressable tentative theory guides decisions, criticism addresses a part of it, and the effect persists across a declared horizon"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Conjectural learning

**Conjectural learning** is the learning paradigm in which a system runs
Popper's process of conjecture and criticism under two conditions:

1. **An addressable theory guides decisions.** A
   [tentative theory](./tentative-theory.md) is formulated in language,
   natural or formal, so that its assumptions, scope, and parts can be
   inspected and revised individually
   ([addressable theory](./addressable-theory.md)). It is on the causal path
   of the system's decisions through what it says: relevant differences in
   its content change decisions.
2. **Criticism addresses a part of the theory, and its effect persists across
   a declared horizon.** Criticism is attempted error elimination: an
   argument, or a test of a stated consequence, aimed at something the theory
   says, and itself formulated in language. When it fails the theory, it
   names the part that probably caused the failure, and the revision acts on
   that part. When the part survives, the result is recorded against it. In
   both cases what the criticism says shapes what changes, and the change
   guides work beyond a stated boundary, such as the next episode or a later
   task.

What the system has learned is the change in its later behavior that is
attributable to the persisted effect of criticism.

The effect can persist through the theory itself, retained and then revised or
replaced, or through the retained criticisms, from which a theory is
reconstructed when one is needed. Both are implementations of the paradigm.

The process is Popper's schema for the growth of knowledge,
`P1 → TT → EE → P2`: a problem, a tentative theory, attempted error
elimination, and a new problem
([Popper 1966](../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
The KB cites the schema and does not redefine it. *Conjectural* is Popper's
own word for the status of theories, which "remain essentially tentative, or
conjectural, or hypothetical"
([Conjectures and Refutations, Chapter 1](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
It does not mean speculative or unsupported.

## Relation to Popper

Conjectural learning is a narrow part of the learning Popper describes. It
takes from him, unchanged, the schema, the tentative status of every theory,
criticism that is broader than empirical test, and selection in place of
instruction. Each row below keeps one of the cases he covers.

| | Popper covers | Conjectural learning keeps |
|---|---|---|
| Carrier | Dispositions, expectations, and habits as well as formulated theories | Theories formulated in language |
| Structure | Any formulated theory, including one that can only be replaced whole | Addressable theories |
| Elimination | All error elimination, from the death of the carrier to conscious criticism | Criticism of what the theory says |
| Localization | A failed test may implicate a whole theoretical system | Criticism aimed at a part |
| Result | As a rule a new problem, with or without a successor theory | An effect that persists and guides later work |

The KB adds what Popper does not state: the theory's place on the causal path
of a particular system's decisions, the declared horizon, and actual use. The
reasons for each narrowing, and what the KB conjectures the narrowing buys,
are argued in
[conjectural learning keeps the criticizable part of Popper's process](../notes/conjectural-learning-keeps-the-criticizable-part-of-poppers-process.md).

## Scope

- **The horizon is declared, and the claim is relative to it.** A theory
  revised and reused within one episode supports a within-episode claim.
  The research program's claims concern horizons that cross episodes.
- **The term classifies by what is formulated and persists.** It makes no
  claim about what happens inside the machine. A model may criticize
  conjectures internally while reading raw records, as training may inside
  the weights. Such criticism leaves nothing formulated to inspect or to
  criticize in turn, so it is outside the term without being denied.
- **Inspection shows half of membership.** Formulated criticisms aimed at
  parts of a theory can be found by reading the artifacts. That their
  content shaped a revision or a decision is a causal claim. It needs an
  intervention that holds the form fixed: a changed, ablated, or mismatched
  theory or criticism. Withholding is not enough, because adding any text of
  that form can change behavior. The
  [evidence ladder](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder)
  says what evidence each part needs, and a partial case is reportable at its
  own strength.
- **Not a success term.** A system that carries a mistaken theory forward is
  still a conjectural learner. Whether the paradigm improves anything, or
  beats the comparisons below, is a separate question, conjectured in the
  companion note and in
  [learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md).
- **Addressing a part is not minimal revision.** The part may be a core
  assumption, a representation, an auxiliary assumption, a test, the problem,
  or learning machinery, and its successor may be bold. The blamed part is a
  candidate, not a verdict.
- **Fixed weights are a study condition, not part of the definition.**
  Holding the weights fixed rules out parameter updates as the source of a
  change. Declare which models stay fixed and for what interval, and the
  whole learner's boundary, including human contributions and external
  services. The term extends to a system in which weights, prompts, and code
  evolve together, provided both conditions hold; a claim about such a system
  says whether the effect of criticism persisted in the text or in the
  weights.
- **Any subject and machinery.** The theory may describe an
  external subject or the system's own organization; the second is the
  reflective case, which composes this term with
  [reflective system](../../../notes/definitions/reflective-system.md). A
  model, a program, or a mixture may apply and criticize the theory. The
  system that runs the process is a
  [theory builder](../../../notes/definitions/theory-builder.md), which is
  identified by responsibility and lineage and need not learn.

## Separate comparisons

These arrangements may also run Popper's process. Each fails a condition, and
the research program specifies each as its own comparison.

- **A theory built while reasoning and discarded after the decision.**
  Nothing of it persists across an episode-crossing horizon.
- **Reconstruction from raw records.** Traces, inputs, and outcomes are kept,
  and a theory is rebuilt from them when needed. Evidence persists; the
  effect of criticism does not. The arrangement needs no criticism step.
- **Black-box optimization of prompts and programs.** Variants are generated and selected by outcome alone. A proposer may read
  the variants, but no formulated reason for a failure bears on what a
  variant says. Systems lie on a range: the
  test is whether a stated reason bears on what the theory says.
- **Unaddressed revision.** A failure is read, and may be described, but no
  part of the theory is blamed; the theory is rewritten or regenerated whole.
- **Weight adaptation.** Something persists, but nothing is formulated, so
  there is nothing to criticize, replace, or inspect on its own.

## Exclusions

- **A theory that is applied and never criticized**, such as fixed
  instructions. No effect of criticism exists to persist.
- **A stored theory or record nothing consumes.** The term names a process on
  the causal path of decisions, not an artifact;
  [a representation matters only through its consumption path](../../../notes/an-action-model-matters-only-through-its-consumption-path.md).

## Misuse Cases

- Using *theory refinement* or *learning by theory refinement* for the
  paradigm. Those were the KB's earlier names, taken from the classical
  theory-refinement systems of machine learning, which remain only a
  precedent for repairing an [addressable theory](./addressable-theory.md).
- Opposing *criticism* to *selection*. For Popper all learning is selection
  and none is instruction: criticism eliminates, and the successor is a new
  conjecture. Black-box optimization differs in what eliminates and what it
  acts on: a score acting on whole variants, where criticism is an argument
  acting on claims.
- Counting an outcome score that only ranks variants as criticism, or
  counting a system as a conjectural learner because it retains prose about
  its subject or itself.

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — defined-in: the status of the theory that guides decisions
- [Addressable theory](./addressable-theory.md) — defined-in: the structural property the first condition requires
- [Conjectural learning keeps the criticizable part of Popper's process](../notes/conjectural-learning-keeps-the-criticizable-part-of-poppers-process.md) — grounds: the reasons for each narrowing and the two conjectures the comparisons test
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md) — extends: the evidence ladder for the parts of the process
