---
description: "Definition — learning by theory refinement is the recurrent loop in which a retained addressable theory guides decisions, outcomes refine it, and the refined theory guides later work; the paradigm, distinct from the single refinement operation"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Learning by theory refinement

**Learning by theory refinement** is the learning paradigm in which a
system retains an addressable
[tentative theory](./theory-refinement.md#tentative-theory) outside its
model weights, the theory guides its decisions, the outcomes of that work
refine the theory, and the refined theory guides later work. What the
system has learned is the change in its later behavior that is attributable
to the change in the retained theory.

The KB needs the term because [theory refinement](./theory-refinement.md)
names one operation, a single episode of revising a theory, while the
research program's claims concern the recurrent loop built on it. Without
its own name the loop borrows the operation's name, and claims about one
are read as claims about the other. The compound is the technical term.

The loop has four parts, and each is necessary:

- **Retained.** The theory survives between decisions as an object that can
  be inspected and revised.
- **Guides decisions.** The theory is on the causal path of a decision:
  changing or withholding it would change what the system does.
- **Refined by outcomes.** Outcomes of the work bear on the theory, and the
  theory is revised against them part by part. This is theory refinement.
- **Guides later work.** Later decisions use the refined state. This closes
  the loop.

The last three correspond to the claims of the
[evidence ladder](../reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder):
mediation, empirical contact and theory refinement, and recurrent
mediation. For example, a system whose account of which edits need which
checks fails on one included snippet, revises the part of the account that
failed, and afterwards checks snippets it has never seen fail, has
completed one turn of the loop.

The loop resembles Popper's schema for the growth of theories,
`P1 → TT → EE → P2`: a problem, a tentative theory, attempted error
elimination, and a new problem. The resemblance is our reading, and it is
loose in one respect. In Popper's schema "the result of criticism, or of
error-elimination, applied to a tentative theory, is as a rule the
emergence of a new problem"
([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md), verbatim),
not a revised theory. The loop defined here adds what the schema leaves
open: the theory that survives or replaces the criticized one is retained,
and it guides the work in which the next problem is met.

## Scope

- **Not a success term.** A loop that carries a mistaken theory forward is
  still learning by theory refinement. Whether it improved anything is
  measured separately.
- **Fixed weights are a study condition.** Holding the weights fixed rules
  out parameter updates as the source of a change, which isolates the
  loop. It is not part of the definition, and a system may run the loop and
  adapt its weights as well.
- **Any form, machinery, and subject.** The term inherits these from the
  operation. The theory may be prose, a program, or a mixture; a model or a
  program may do the refining; and the theory may describe an external
  subject or the system's own organization, which is the reflective case.
- **The carrier is separate.** The system that runs the loop is a
  [theory builder](./theory-builder.md), which is identified by
  responsibility and lineage and need not learn.
- **Records may be kept alongside.** Retaining the records a theory was
  derived from, as evidence for re-examining it, is compatible with the
  paradigm. What the definition requires is that a theory is retained and
  refined, not that nothing else is.
- **What the definition leaves open.** It says what the paradigm is, not
  how to measure it. What evidence establishes each part, and how a later
  change is attributed to a revision, belongs to the evidence ladder and to
  the experiments, and some of it is unsettled. A partial loop is
  reportable at its own strength: a system that shows guidance or one
  refinement without later reuse has shown that part, not the paradigm.

## Exclusions

- **A theory built while reasoning and discarded after the decision.** It
  can guide that decision, but nothing remains to refine.
- **Keeping records or summaries of experience and rebuilding an
  explanation when one is needed.** No explanation is retained as an object
  to revise.
- **Adapting weights.** What is learned is not a theory with parts that can
  be inspected and revised.
- **A retained theory that is applied and never revised**, such as fixed
  instructions. The system uses a theory; it does not learn by refining
  one.
- **A stored theory nothing consumes**, since
  [a representation matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md).

## Misuse Cases

- Calling a system a learner by theory refinement because it retains prose
  about its subject or about itself. The term names a loop on the causal
  path of decisions, not an artifact.
- Using *theory refinement* for the loop, or *learning by theory
  refinement* for a single revision.
- Treating fixed weights as part of the definition.
- Reading the term as a claim that the paradigm works or beats the
  alternatives. That is the conjecture in
  [theory refinement may improve sample efficiency under structured shifts](../theory-refinement-may-improve-sample-efficiency-under-shifts.md),
  and the definition is neutral on it.

---

Relevant Notes:

- [Theory refinement](./theory-refinement.md) — defined-in: the operation the loop is built on, the addressable theory it requires, and the tentative-theory status
- [Theory builder](./theory-builder.md) — contrasts: the system that carries the loop, defined by responsibility and not by whether or how it learns
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../reflective-theory-refinement-needs-interpretation-and-retention.md) — extends: the evidence ladder whose claims correspond to the parts of the loop
- [Theory refinement may improve sample efficiency under structured shifts](../theory-refinement-may-improve-sample-efficiency-under-shifts.md) — extends: the payoff conjecture the definition stays neutral on
- [An action model matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md) — grounds: why a stored theory nothing consumes is excluded
