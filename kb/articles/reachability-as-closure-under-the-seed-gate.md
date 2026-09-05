---
description: "Supplement to the automated software house conjecture: fixed computational semantics allow mutable update policies; practical reachability requires both reaching adequate states and sustaining them"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md
  - kb/sources/goedel-machines-schmidhuber.ingest.md
---
# Reachability as transition closure under the seed's successor relation

> **Draft supplement.** Everything in this supplement may still change. It is
> the full treatment behind the transition-closure and Gödel-machine passages
> in [The Automated Software House
> Conjecture](./automated-software-houses-with-fixed-llms.md). Comments and
> counterexamples are welcome on [the repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

**TL;DR.** An automated software house develops and maintains software without
humans in internal production roles. Every internal change must arise through
its current machinery and permitted external inputs, even when the change
rewrites that machinery. A Gödel machine obeys the same causal requirement,
with proof governing its rewrites. The practical question is how reliably the
process reaches an adequate state and sustains it across later demands. One
lucky path establishes only possibility.

## The observation

Represent the mutable state of the house by \(s\): its product, notes, tools,
evaluators, context assembly, and update machinery. Include every internal
history-dependent variable that can affect an update; persistent tool or
environment state must either belong to \(s\) or be declared external. Pinned
[distributed-parametric](../notes/definitions/representational-form.md)
components, such as model weights and trained routers, remain fixed parameters.
Indexes regenerated from mutable records under pinned algorithms belong to
\(s\), while their embedding model remains fixed.

Write \(R(s,x)\) for the possible successors of state \(s\) on permitted input
\(x\), under the declared computational semantics and pinned components.
Inputs can include user demands, tool results, and operating consequences;
sampling rules may assign probabilities to successors. If omitted state or
earlier history can affect an update, augment the representation. The list of
artifact types alone does not establish that the current state is sufficient.

The reachable set is the least set containing the seed \(s_0\) and closed
under permitted successor transitions over the declared input histories.
This is **transition closure**. It applies to both explicitly gated updates
and direct updates, whether deterministic or involving several possible
successors.

The overall relation \(R\) stays fixed, but the update policy encoded in
\(s\) may change. Rewriting an evaluator changes what it accepts under the
same rules for executing code. The rewrite is itself an \(R\) transition
from the preceding state. Closure therefore permits self-modification without
requiring the seed to specify every later decision.

A human correction in an internal production role breaks the autonomous
lineage, even if the machinery could have produced the same result. After
people leave those roles, each transition must arise through the house's
machinery and permitted external inputs.

## Consequences for the conjecture

### Bare reachability is cheap

If an update process can emit and retain arbitrary state, an adequate state
may be possible yet extremely unlikely. Practical reachability requires more:

- **Hitting probability:** how likely the process is to reach an adequate
  automated house within the resource budget.
- **Continuation reliability:** how likely that house is to remain adequate
  across later demands over the declared horizon.

A process that sometimes reaches a good state and immediately drifts differs
from one that reaches it less often but sustains it. The witness must set
acceptable thresholds or evidence for both quantities.

### Existential reachability and nondeterminism are separate

The conjecture says at least one eligible construction and declared regime
works. That construction may be deterministic, nondeterministic, or
probabilistic. Its transition model does not settle whether the success
criterion requires one possible path, all paths, almost-sure success, or a
probability threshold. The witness protocol must specify that separately.

### The declared input process is part of the claim

Distinguish three objects:

1. the set of admissible demand and consequence histories;
2. the history realized in one run; and
3. the probability distribution or procedure selecting histories.

With \(R\) fixed, allowing more histories can enlarge the reachable set without
making adequate states more probable. The selection procedure may direct more
runs toward failure. Reachability therefore depends on the declared input
process, not an informal claim that the house receives richer demands.

### The reachable update path can exclude or suppress adequate successors

The policies reachable from the seed may exclude adequate states or make them
negligibly likely. An evaluator can govern a rewrite of itself, but the current
machinery must be capable of producing that rewrite. Coherent revision tests
whether new evidence leads to an adequate policy and continued operation
without internal human decisions. An evaluator-editing operation alone does
not establish that capacity.

### The closure observation is general

Transition closure applies to any autonomous lineage whose successors arise
from internal state and declared inputs. Fixing learned components is an
additional experimental restriction in the software-house conjecture.

## The Gödel-machine comparison

A Gödel machine admits a rewrite only after proving the target theorem under
its current axioms and utility function. Those can themselves be rewritten,
but only as the predecessor formalization licenses. Its proof-governed policy
is mutable state within the overall transition relation.

Both systems obey transition closure; their update policies differ:

| | Gödel machine | Conjectured house |
|---|---|---|
| Rewrite condition | Proof under current axioms and utility | A fallible process produces and, where applicable, admits a successor from evidence |
| External input | Observations enter through the formalization, including `state2theorem`; rewrites still require proof | Current interpretive capabilities use demands, tool results, and consequences to challenge retained theory |
| Warrant | Conditional proof relative to the encoded formalization | Empirical warrant bounded by evaluators and later exposure |
| Characteristic failure | Useful changes cannot be proved and remain unreachable | Harmful successors receive enough probability to undermine continued adequacy |

Deductive closure concerns the theorems derivable from the Gödel machine's
axioms. Transition closure concerns its reachable machine states. Both apply;
neither alone establishes reliable software-house operation.

## What this changes in the witness

Declare the seed, mutable state, pinned components, permitted inputs, update
protocol, product scope, budget, and horizon before testing. Then estimate
whether the process reaches and sustains adequate states with the required
reliability.

The main article's four conditions test program-theory application, coherent
revision, automated continuation, and practical reliability on that path.
Acquiring decisive understanding absent from the seed is a further question for
the [training](./the-software-house-as-the-unit-of-training.md) and
[bootstrap](./bootstrapping-the-first-automated-software-house.md) articles.

## Open questions

- What minimum evidence should establish usable hitting probability and
  continuation reliability without pretending that one universal threshold
  fits every product and risk level?
- How should a witness specify admissible histories and their selection process
  while preserving relevant novelty and preventing post-hoc removal of failed
  demands?
- Which parts of the environment belong in the successor relation, and which
  should be treated as exogenous inputs whose provenance and authority must be
  reported separately?
