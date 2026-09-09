---
description: "Definition -- a universal theory manipulator is the fully codified limit of refinement machinery: it expresses any computable theory and computes consequences, but admits only formalized theories, supplies no bias, and never refines against evidence"
type: kb/types/definition.md
tags: [foundations, learning-theory, self-improving-systems]
---

# Universal theory manipulator

> **Status:** Workshop draft, 2026-09-09, staged for `kb/notes/definitions/`.
> Ideal type: it fixes a limit case and claims no construction. The Gödel
> machine is cited as the worked instance through its ingest; verbatim quotes
> beyond the one the ingest retains need the ingest re-pinned to the
> 2026-09-09 snapshot first.

A **universal theory manipulator** is refinement machinery at the fully
codified limit. Its representation language can express any computable
theory. Its consequence procedure is execution or proof, so what a theory
implies for a case is computed and a contradiction is a fact. Its repair
operators are edits to symbolic expressions, and its evaluator is a computable
check. Every part of every theory it holds sits on the symbolic side of
[codification](../../notes/definitions/codification.md). The KB needs the term
to name one end of the boundary along which
[theory refinement](../../notes/definitions/theory-refinement.md) moves parts
of a theory, and to state exactly what that end can and cannot do.

The declared universality axis, in the sense of
[universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md),
is **constructional expressivity**. The manipulator is not universal in
acquisition reach. Two things it lacks by construction:

- **It admits a theory only once formalized.** A theory whose language,
  variables, and acceptance test do not yet exist cannot enter. Formalizing a
  new family is work done outside the manipulator, or by other machinery that
  writes into it.
- **It supplies no search bias.** Universal search over its expressions
  exists and is order-optimal up to a constant that hides everything.
  Tractable refinement in a family needs that family's bias, which
  expressivity does not provide.

## The worked instance

Schmidhuber's Gödel machine is a universal theory manipulator applied to a
theory of the machine itself
([ingest](../../sources/goedel-machines-schmidhuber.ingest.md)). Its
components map onto the clauses above and add three that a definition written
from first principles would miss.

- **The theory.** An axiomatic system encoded in the initial program, with six
  axiom classes: hardware transitions, costs and rewards, environment
  assumptions, arithmetic and probability, the initial state including the
  program itself, and the utility function (Section 3.2, item 1). This is a
  checklist of what a complete formal theory of a running system contains.
- **Consequences.** Proof techniques, programs in a universal language that
  emit proofs from the axioms, under six instructions that make it impossible
  to add an unproven theorem (Section 3.2).
- **Evidence entry.** An observation instruction turns the current contents of
  a state region into a time-labelled theorem without proving it from the
  initial state (Section 3.2, item 6). Even the fully formal machine needs an
  unproven entry point for observations, and the paper notes that some of the
  machine's own state cannot be read without changing it.
- **Bias supplied, not derived.** The initial searcher is universal search
  over proof techniques under a supplied prior, and the paper closes by asking
  which theorems a person should hand-install as initial bias so the searcher
  need not prove them (Sections 5.1 and 7).
- **Revision by proof only.** The machine may replace its axioms by theorems
  derivable from them, and may change its utility function only when the
  change is provably better under the old one (Section 6.1, items 3 and 4).

## What the limit cannot do

At this limit a theory is never revised against evidence. Observations enter
as theorems and change conclusions drawn under the axioms; the axioms change
only by proof from themselves. A contradiction between an observation and an
axiom is not an informative case, as it is for FORTE. It is an inconsistency,
and the consistency of the axioms is an assumption of the machine's
optimality theorem, not a result (Theorem 4.1).

The paper's own handling of this shows what the assumption costs. The
environment axioms say only that the environment is drawn from an unknown
distribution in a known class, which observation cannot contradict, and the
substantive knowledge of the environment lives in the posterior computed
under the axioms rather than in the axioms (Section 3.2, item 1c). Where the
axioms are substantive, in the hardware and initial-state classes, they can
be contradicted, and the paper's remedy is to make the machine probabilistic,
because "predictions proven to come true with probability less than 1.0 do
not necessarily cause contradictions even when they do not match the
observations" (Section 6.3; snapshot required). A theory kept consistent this
way is kept from misfitting by being too weak to misfit. What the machine must
leave alone is stated directly: it "must ignore those self-improvements whose
effectiveness it cannot prove"
([Schmidhuber, Section 2.4](../../sources/goedel-machines-schmidhuber.ingest.md), verbatim).

So the manipulator is a limit, not a destination. Codifying a part of a theory
moves it toward the manipulator, where it becomes something assumed true and
checked rather than something refined. A builder that reached the limit would
keep derivation and lose refinement. Substantive, fallible theories, the ones
that can fit or fail to fit the world, live on the partially codified side,
where a contradicting case is a repair signal.

## Scope

- Use the term for the fully codified end of the codification boundary, when
  an argument needs to say what exact machinery can and cannot supply.
- Use it as one of two refuters of the claim that open-endedness forces
  family-specific machinery construction: the position that every new family
  arrives formalized, or is formalized by fixed machinery.
- The term is an ideal type. No witness is asked for, and no Gödel machine has
  been built.

## Exclusions

- **A universal Turing machine.** The analogy holds on expressivity only. A
  universal Turing machine simulates any machine; the manipulator expresses
  any computable theory and computes its consequences. Nothing about
  simulation, halting, or optimality carries over.
- **A theory refiner.** At the limit, refinement against evidence is absent.
  Refinement is what happens when a part is on the interpreted side or when
  an observation is allowed to count against an axiom.
- **A general interpreter.** A model that interprets prose theories is the
  other candidate for machinery not fixed per family. It admits pre-formal
  theories and supplies bias from its weights, at the cost of interpreted
  consequences. The two are the two ends of one boundary, not rivals.
- **The Gödel machine as such.** The machine bundles a utility function,
  self-modification, and an optimality claim. The manipulator takes only its
  formal-theory machinery.

## Misuse Cases

- Reading "universal" as universal in acquisition reach, and concluding that
  a builder with a universal language needs no family-specific machinery.
  The bias and the formalization for each family are still supplied.
- Treating full codification as the goal of refinement. At the limit the
  refinement operation disappears.
- Reading the consistency assumption as empirical adequacy. It is logical
  consistency, needed so that the proof gate is not vacuous, and it is bought
  by keeping substantive world-content out of the axioms.

---

Relevant Notes:

- [Theory refinement](../../notes/definitions/theory-refinement.md) — contrasts: the operation the limit lacks; the machinery departure names the manipulator as the candidate not taken first
- [Codification](../../notes/definitions/codification.md) — grounds: the crossing whose far end this term names
- [Universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md) — rests-on: the rule that fixes the axis to expressivity
- [Gödel machines are a proof-governed case of reflective self-modification](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — see-also: the KB's reading of the same construction as a change loop
- [Machinery persists by warrant, not position, in a reflective loop](../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — see-also: why a codified part is assumed-and-checked rather than exempt
