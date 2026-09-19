---
description: "Definition — conjectural learning is Popper's process of conjecture and criticism run by a system in which an articulated tentative theory guides decisions and the effect of criticism persists across a declared horizon"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Conjectural learning

**Conjectural learning** is the learning paradigm in which a system
runs Popper's process of conjecture and criticism under two conditions:

1. **An articulated theory guides decisions.** A
   [tentative theory](./tentative-theory.md) formulated in language, natural
   or formal, is on the causal path of the system's decisions: changing or
   withholding it would change what the system does.
2. **The effect of criticism persists across a declared horizon.** Outcomes
   and arguments bear on the theory, and what they change guides work beyond
   a stated boundary, such as the next episode or a later task.

What the system has learned is the change in its later behavior that is
attributable to the persisted effect of criticism.

The effect can persist in two ways. The system may retain the theory itself
and revise or replace it, or it may retain records and reconstruct a theory
from them when one is needed. Both are implementations of the paradigm.
Retaining the theory is the implementation the KB prefers, on an efficiency
conjecture stated under Scope.

The process is Popper's schema for the growth of knowledge,
`P1 → TT → EE → P2`: a problem, a tentative theory, attempted error
elimination, and a new problem
([Popper 1966](../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
The KB cites the schema and does not redefine it. *Conjectural* is Popper's
own word for the status of theories, which "remain essentially tentative, or
conjectural, or hypothetical"
([Conjectures and Refutations, Chapter 1](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
It does not mean speculative or unsupported.

## What is Popper's and what is ours

- **Popper's.** The process, the tentative status, and criticism that is
  broader than empirical test. Articulation is also partly his. He holds that
  a descriptive language developed outside the body gives critical discussion
  its object, that informal argument is criticized before it is formalized,
  and that scientists "try to let [their false theories] die in their stead"
  ([Popper 1968](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes),
  §4 and §6). He makes this claim about rational criticism, not about
  learning in general, which he extends to behaviour and evolution.
- **Ours.** The theory's place in a particular system's decisions, the
  declared horizon, and the evidence that establishes each. In Popper's
  schema criticism results "as a rule" in a new problem, not a revised
  theory; the requirement that its effect persists and guides later work is
  our addition.
- **Empirical.** Whether a model interprets a prose theory reliably enough to
  apply and criticize it, and whether retaining a theory is cheaper than
  reconstructing one. The definition is neutral on both.

## Scope

- **The horizon is declared, and the claim is relative to it.** A theory
  revised and reused within one episode supports a within-episode claim.
  The research program's claims concern horizons that cross episodes.
- **Retention against reconstruction is an efficiency question.** The KB's
  conjecture is that reconstructing a theory from records repeats
  interpretive and inferential work that retaining and revising it avoids,
  and that bounded context raises this cost, because the relevant records
  may not fit together and must first be retrieved, selected, or summarized.
  Retention has maintenance costs of its own. The comparison is of cost at
  comparable decision quality, not of membership in the paradigm.
- **Narrower than Popper's process.** Popper extends the schema to behaviour
  and evolution, where nothing is articulated. The term covers only the
  process under the two conditions above.
- **Not a success term.** A system that carries a mistaken theory forward is
  still a conjectural learner. Whether it improved anything is
  measured separately.
- **Revision is not required to be small.** Criticism may change one part,
  replace the theory, or change the problem. Local repair is a possible
  benefit of an [addressable theory](./addressable-theory.md), not part of
  the definition.
- **Fixed weights are a study condition.** Holding the weights fixed rules
  out parameter updates as the source of a change. It is not part of the
  definition, and a system may also adapt its weights.
- **Any subject and machinery.** The theory may describe an external subject
  or the system's own organization; the second is the reflective case, which
  composes this term with [reflective system](../../../notes/definitions/reflective-system.md).
  A model, a program, or a mixture may apply and criticize the theory.
- **The carrier is separate.** The system that runs the process is a
  [theory builder](../../../notes/definitions/theory-builder.md), identified
  by responsibility and lineage.
- **A partial case is reportable at its own strength.** Evidence that a
  theory guided a decision, or that one criticism changed it, shows that
  part. The [evidence ladder](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder)
  says what evidence each part needs.

## Separate comparisons

These arrangements may also run Popper's process. The research program
specifies each as its own comparison.

- **A theory built while reasoning and discarded after the decision.** It can
  guide that decision. Nothing of it persists across an episode-crossing
  horizon.
- **Weight adaptation.** Something persists, but it is not articulated, so
  there is no formulation to criticize. Whether conjecture and criticism
  occur inside is not settled by the parameter change.

## Exclusions

- **A theory that is applied and never criticized**, such as fixed
  instructions. No effect of criticism exists to persist.
- **A stored theory or record nothing consumes.** It is not on the causal
  path of decisions, since
  [a representation matters only through its consumption path](../../../notes/an-action-model-matters-only-through-its-consumption-path.md).

## Misuse Cases

- Calling a system a conjectural learner because it retains prose
  about its subject or about itself. The term names a process on the causal
  path of decisions, not an artifact.
- Using *theory refinement* or *learning by theory refinement* for the
  paradigm. Those were the KB's earlier names, taken from the classical
  theory-refinement systems of machine learning. The systems remain a
  precedent for repairing an [addressable theory](./addressable-theory.md);
  the paradigm does not inherit their representation, operators, or
  preference for minimal change.
- Treating fixed weights as part of the definition.
- Reading the term as a claim that the paradigm works or beats the
  separate comparisons. That is the conjecture in
  [learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md).

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — defined-in: the status of the theory that guides decisions
- [Addressable theory](./addressable-theory.md) — extends: the structural property that makes local criticism and repair possible
- [Theory builder](../../../notes/definitions/theory-builder.md) — contrasts: the system that carries the process, defined by responsibility and not by whether or how it learns
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md) — extends: the evidence ladder for the parts of the process
- [Learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — extends: the payoff conjecture the definition stays neutral on
- [Popper, Epistemology without a knowing subject](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) — evidenced-by: language as the object of critical discussion
