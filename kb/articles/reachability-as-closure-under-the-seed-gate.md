---
description: "Supplement to the automated software house conjecture: an autonomous house's states are the transition closure of its seed under a state-dependent successor relation and declared inputs; the Gödel machine differs in admission, not closure"
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

> **Draft supplement.** This is the full treatment behind the transition-closure
> and Gödel-machine passages in [The Automated Software House
> Conjecture](./automated-software-houses-with-fixed-llms.md).
> It is kept separate so the main article can state the consequence without
> carrying the transition-system detail.

## The observation

Once no human fills an internal production role, every change counted as an
internal house transition must arise through the computational machinery and
permitted external inputs in its declared system. Represent the mutable state
inside that declared boundary by \(s\): its notes, software, production
machinery, retention rules, evaluators, and context assembly. Persistent tool
or environment state on which a transition depends must either be included in
\(s\) or declared as external. The pinned
[distributed-parametric](../notes/definitions/representational-form.md)
components, the model weights and any other learned numerical component, remain
fixed parameters of the experiment rather than mutable parts of \(s\).

Let the declared external inputs include user demands, tool results, and
operating consequences. Define \(s\) broadly enough to include every
history-dependent variable inside the boundary that can affect the next update.
The current state and one permitted input then determine a set or distribution
of possible successor states. If omitted state or earlier history can still
affect the successor, the representation must be augmented; the listed artifact
classes are not by themselves a claim of Markov completeness. This **successor
relation** covers both architectures with an explicit proposal-and-admission
gate and direct update architectures in which no separate gate is exposed.

From a seed state \(s_0\), the reachable set is the least set that contains
\(s_0\) and is closed under those permitted successor transitions over the
declared input histories. This is transition closure: the ordinary reachable
set of a state-transition system. If model sampling or environmental events
make several successors possible, the relation is nondeterministic or
probabilistic; that does not make it less of a closure.

The successor relation may itself change because production machinery belongs
to the mutable state. A house can rewrite an evaluator, retention rule, or
update procedure. But that rewrite must still be produced by the predecessor
state's successor relation. In this limited sense the lineage remains causally
descended from the seed: every later revision of the updating machinery must
enter through machinery already reachable from it. This descent relation does
not mean that the seed explicitly settles each later revision.

A human correction during bootstrapping can introduce a transition or decision
that the autonomous relation would not have produced. It is therefore
exogenous to the autonomous lineage. Exogenous does not mean correct or
warranted; it identifies where the transition came from. When the human leaves,
the tested lineage is restricted to its own successor relation and the inputs
the witness permits.

## The Gödel-machine comparison

A Gödel machine is a particularly explicit self-modifying transition system.
Its next rewrite executes only after its proof searcher proves the target
theorem under the axioms and utility function then in force. Those axioms and
that utility function may themselves be rewritten, but only through a rewrite
the predecessor formalization licenses. Its later machine states therefore
remain causally descended from the seed through proof-gated successor relations
in the same structural sense.

The conjectured house does not differ by having closure where the Gödel machine
has deduction. Both have transition-reachable state sets. They differ in the
successor relation that admits or produces a rewrite:

| | Gödel machine | Conjectured house |
|---|---|---|
| Successor condition | A target theorem is proved under the current axioms and utility | The current fallible update process produces and, where applicable, admits a successor from production evidence |
| External input | Observed state can enter a proof through `state2theorem` when the formalization represents it, but the rewrite still requires derivation in the current formal system | Declared demands, tool outputs, and operating consequences affect a transition only through capabilities supplied by the current state; when interpreted as relevant evidence, they may defeat part of the current theory |
| Reachable states | Transition closure under a proof-gated successor relation | Transition closure under a fallible successor relation that responds to evidence |
| Warrant | Conditional proof relative to the encoded formalization | Empirical warrant bounded by the available evaluators and later exposure |
| Characteristic failure | Starvation: useful changes remain unreachable because they cannot be proved | Drift: harmful or incoherent successors may receive non-negligible probability |

Deductive closure applies to the theorems derivable from the Gödel machine's
axioms. Its machine states are not themselves a deductive closure; they are
states reachable through proof-gated transitions. The comparison is therefore
between two admission or update relations, not between deduction and closure.

## Consequences for the conjecture

### Existential reachability and nondeterminism are separate

The conjecture is existential because it claims that at least one eligible
construction, meaning one built on models available by the cutoff date, and
declared regime works. A particular construction may be deterministic,
nondeterministic, or probabilistic. Nondeterminism does not choose whether the
success criterion is existential, universal, almost-sure, or a probability
threshold; the witness protocol must choose that separately.

### Bare reachability is cheap

If the successor relation can emit and retain arbitrary state, almost any state
may lie somewhere in its support. One lucky path then establishes only
set-theoretic reachability. The practical claim needs adequate states to receive
usable probability mass within the declared compute, time, and cost envelope.

Two quantities should remain distinct:

- **hitting probability** — the probability that the lineage reaches an
  adequate human-free state within the resource budget; and
- **continuation reliability** — the probability that, once reached, the house
  remains adequate across the declared horizon and later demands.

A system that occasionally reaches a good state and immediately drifts differs
from one that reaches it less often but remains coherent. The main article's
practical-reliability condition is the requirement that both count as
practical; the witness must set the evidence or thresholds for it.

### The declared input process is part of the claim

Three objects must not be called one "demand stream":

1. the set of admissible demand and consequence histories;
2. the particular history realized in one run; and
3. the probability distribution or selection procedure over those histories.

Holding the successor relation fixed, expanding the admissible-history set can
enlarge the set-theoretic reachable support because it permits more paths. It
does not follow that useful states become more probable: changing the selection
distribution may move probability mass away from them. A witness therefore
establishes reachability only relative to its declared input process, not to an
informal ordering from poorer to richer streams.

### The reachable update path can exclude or suppress adequate successors

The main risk exposed by this framing is not that the seed remains visibly
unchanged. It is that the starting update machinery and the successor relations
reachable from it may be so narrow or unreliable that adequate states lie
outside the reachable set, or inside it only with negligible probability. This
is the fallible counterpart of a Gödel machine having to ignore an improvement
it cannot prove.

Revision of the updating machinery does not escape the issue. An evaluator or
acceptance rule can govern a rewrite of itself, but only when the predecessor
state's relation permits that rewrite. New production evidence can change what
the house accepts only through interpretive and update capabilities already
reachable from the seed. Coherent revision is therefore a test of whether
those capabilities can use permitted evidence to move the house to an adequate
successor without importing a human decision. The conjecture does not require
the lineage to outgrow the seed's task-specific contents: the seed may carry a
human-written theory and human-built machinery. It requires that every
revision after the declared start comes through the sequence of successor
relations reachable from the seed.

### The closure observation is general

Nothing in the transition-closure argument requires a fixed LLM. It applies to
any autonomous lineage whose successors arise from prior internal state and a
declared set of external inputs. The fixed-model and fixed-parametric-state
conditions are additional restrictions that make the automated software house conjecture a
specific empirical claim about where learning can occur.

## What this changes in the witness

The witness must declare the seed, mutable state, pinned components, permitted
external inputs, successor/update protocol, product scope, budget, and horizon
before interpreting the result. It must then show not only that an adequate
state appears on some path, but that the process reaches and sustains such
states with the practical reliability the claim requires.

The four conditions in the main article locate the difficult transitions.
Holding and application tests the adequacy of the current state. Coherent
revision tests whether later evidence can move the process, through its own
successor relation, to an adequate replacement. Automated continuation tests
whether those transitions remain inside the computational boundary over the
declared horizon. Practical reliability is the hitting-probability and
continuation-reliability requirement stated above. Whether the relation can
also reach an adequate state without receiving the decisive project
understanding from the seed is the stronger question the training and
bootstrap articles ask; it is not a condition of the witness.

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
