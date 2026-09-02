---
description: "Supplement to the reachability-conjecture article: with no human inside, the house's reachable states are the nondeterministic closure of the seed under its gate and demand stream; Gödel-machine descent structure, different admission relation"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md
  - kb/sources/goedel-machines-schmidhuber.ingest.md
---
# Reachability as closure under the seed's gate

> **Draft supplement.** This is the full treatment behind three short
> passages in [The reachability conjecture](./the-reachability-conjecture-train-the-house-not-the-llm.md):
> the Gödel-machine contrast, the closure sentences in the seed-engineering
> paragraph, and the "bare reachability is cheap" sentences in the boundaries
> section. It is intended to become a footnote to that article and is kept
> separate so the article stays simple.

## The observation

The Gödel machine's axioms and utility function are rewritable, but only
under a proof from the formalization then in force. [Schmidhuber's
paper](../sources/goedel-machines-schmidhuber.ingest.md) states this at
printed page 16 and in its FAQ. So the initial formalization governs every
successor by descent: nothing enters the lineage that the original axioms
could not, transitively, license.

The conjectured house has the same structure once no human is inside. Each
successor state, meaning its notes, software, retention rules, validators,
and context assembly, is admitted by the gate the prior state supplies, and
that gate is itself made of prior notes, prior software, and the fixed LLM.
The seed governs the lineage by descent.

While a person is inside, corrections can enter that no prior state would
have admitted. The person is an exogenous source of warrant, outside the
lineage. This is what "people still correct it at first" means in the
article's TL;DR. The moment the person leaves, the lineage closes under its
own gate. With humans the same regress is Neurath's boat: people also revise
their standards only by their current standards. The difference is that for
the automated house the closure holds by construction, and nobody has to
argue for it.

## Reachability is a closure, nondeterministic

The set of states the house can occupy is the closure of the seed under the
transition relation. The relation is nondeterministic, since the LLM samples
and interpretation is fallible, and it reads an input alphabet: the demand
stream and production consequences. This is the reachable set of a
nondeterministic automaton, not something weaker than a closure. An earlier
draft of this argument said the fallible case is "not a closure in any formal
sense"; that was wrong.

So the Gödel machine and the house do not differ in closure versus no
closure. They differ in the admission relation:

| | Gödel machine | Conjectured house |
|---|---|---|
| Admission | derivability under the current axioms and utility | acceptance by a fallible gate reading production consequences |
| External input | observations enter as theorems (`state2theorem`) the axioms can already use | consequences enter as evidence the current theory interprets, and can contradict it |
| Reachable set | deductive closure of the seed | nondeterministic closure of the seed under gate and stream |
| Guarantee | proved improvement relative to the formalization | none; the price is fallibility |
| Failure mode | starves: must ignore what it cannot prove | drifts: may admit what does not help |

The last two rows are the existing contrast in [the Gödel-machine
note](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md).
The first three rows are what this treatment adds.

## Three consequences for the conjecture

**The title's word is exact.** The conjecture is literally a reachability
claim over this closure: from the seed, under the evidence-driven relation,
some path reaches a state that holds an adequate theory with no human
inside. The existential form of the conjecture and the nondeterminism of the
relation are the same fact.

**Bare reachability is cheap.** If the LLM can emit any text and the gate can
admit anything, every state is reachable and the claim is empty. The gate's
selectivity is what makes the reachable set nontrivial, and the claim is
nontrivial only as a statement about probability mass: adequate states are
reached with usable probability inside the declared resource envelope. This
is what the article's "practically reachable" already says. The closure
framing shows why the envelope clause is not bookkeeping: it converts an
existence claim over paths into a claim about mass under a budget.

**The stream is part of the closure.** The reachable set is fixed by the seed
and the relation together, and the relation reads the demand stream. A
richer stream enlarges the reachable set, a poorer one shrinks it. So
declaring the stream open-ended is not only an anti-rescue rule. It is part
of what determines the closure, and a witness that succeeds on a rich stream
has not shown reachability on a poor one.

## What this does to the open doubts

A full review pass over the article left one premise as its top doubt: the
seed scaffold may keep deciding what counts as coherent, so the apparent
learned theory is a product of the scaffold. This treatment gives that doubt
its mechanism. Restated: the gate's selectivity may be inherited from the
seed tightly enough that adequate states lie outside the closure, or inside
it only with negligible mass. Same shape as "must ignore what it cannot
prove", with proof replaced by a fallible gate and probability replacing
derivability. [Warrant is bounded by the gate's
domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) on
either side.

The same pass asked whether the training path stays viable when the
machinery that selects and validates updates is itself under revision. That
is the same question from the other side. Gated goal change in the Gödel
machine shows that [an acceptance rule can govern rewrites of
itself](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).
The house's gate can too, by the same descent. What it cannot do is admit a
revision of itself that its current form would reject, and that is where
production consequences must do the work a proof cannot.

Obligations 2 and 3 in the article, initial and successor acquisition, are
then the tests of whether fallible interpretation of external evidence
outgrows the interpretive capacity the seed supplied. That is a sharper
statement of what the witness must show than the article carries.

## Open

- Whether "adequate states are reached with usable probability" can be
  stated as a measurable property of a witness, or stays a qualitative
  reading of the envelope clause.
- Whether the descent argument needs the fixed LLM at all, or holds for any
  automated lineage whose gate is made of its own prior state. If the
  latter, it belongs in a note as well as in this footnote.
