---
description: "Exploratory map of backtracking, learning, and complexity models that expose budgets relevant to fallible theory-guided search"
type: kb/types/note.md
traits: [has-comparison]
tags: [learning-theory, computational-model, self-improving-systems]
---

# Cost-sensitive formalisms for fallible theory search

This note is an exploratory catalogue, not a claim that one formalism is the
right model. Its question is: which formal models expose the costs of a process
in which a partial project theory orders search, a failed path may cause
rollback or theory revision, and later search inherits retained effects from
the failure?

The target is the fallible program theory described in [holding a program
theory means sustaining coherent search under delayed
feedback](./program-theory-sustains-search-under-delayed-feedback.md). Ordinary
nondeterministic reachability hides most of the relevant distinctions. It asks
whether an accepting branch exists. It does not by itself price finding that
branch, preserving alternatives, detecting that a branch failed, reconstructing
a discarded state, changing the theory that orders later branches, or suffering
the consequences of a tentative change.

## Budgets the model may need to expose

| Budget | Possible measure | Question made visible |
|---|---|---|
| Search work | expanded states, model calls, experiments, wall time, or money | How much exploration is affordable? |
| Horizon | branch depth or work before reconsideration | How long may a theory keep the process on one path? |
| Discrepancy | departures from the theory's preferred successor | How many wrong turns may the current theory make? |
| Frontier memory | retained alternatives, rationales, or open states | Which abandoned branches remain cheap to resume? |
| Checkpoints | restorable operative states | How far can the process roll back without reconstruction? |
| Theory revision | mind changes, changed premises, or changed scope | How much revision can occur inside the operating horizon? |
| Evaluation | tests, critics, deployments, and delayed observations | What does finding that a branch failed cost? |
| Recovery | reverted work and reconstruction after failure | How expensive is backtracking after a change becomes operative? |
| Realized loss | production damage before detection and recovery | How costly is learning through a wrong theory? |
| Human contribution | diagnoses, successor choices, or authorizations | Did the automated path stay inside the declared boundary? |

These budgets need not collapse into one scalar. A resource envelope could
bound each component separately, while a comparison could scalarize only the
components for which an explicit exchange rate is warranted.

One minimal mathematical scaffold is a weighted transition system. A state
contains the current software, theory, evaluation gate, retained search state,
and checkpoints. Each transition has a cost vector. Budgeted reachability then
asks whether an adequate state can be reached by a specified search controller
without any component exceeding its bound. This is stronger than unweighted
reachability because the controller and the cost of discovering a path become
part of the question.

## Candidate model families

### Time-, space-, and nondeterminism-bounded machines

A time- and space-bounded nondeterministic Turing machine supplies the broadest
complexity-theoretic baseline. Limited-nondeterminism variants additionally
bound the number of nondeterministic moves or guessed bits by a function such
as `g(n)`. Parameterized-complexity characterizations can instead make the
nondeterministic budget depend on a parameter `k`.

The named class families to investigate are the `P_g(n)` limited-nondeterminism
hierarchies, `W[P]` and neighboring parameterized classes for
parameter-bounded nondeterminism, and `UP` or `FewP` for machines with one or
few accepting paths. They bound different things and should not be treated as
interchangeable merely because each narrows `NP`-style branching.

Possible parameters for this setting include the number of consequential
choice points, theory discrepancies, revisions, retained premises, or failure
classes. A target running time of `f(k) * poly(n)` would say that combinatorial
explosion is confined to the selected theory-error parameter and would put the
problem on the fixed-parameter-tractable side for that parameterization.
Classes based on few or unique accepting paths are less direct: they bound
ambiguity in the solution set, not the work a real controller spends finding a
path.

This family preserves familiar complexity questions but usually treats the
transition relation, acceptance predicate, and input as fixed. It therefore
does not yet represent an operative theory that changes its own successor
ordering or evaluation machinery.

### Limited discrepancy search

Limited discrepancy search starts with a heuristic ordering of successors and
budgets departures from the preferred path. Read the current theory as that
heuristic. A discrepancy is then a decision that overrides the theory's first
choice.

For a binary decision tree of depth `d`, searching every path with at most `k`
discrepancies considers

```text
sum from i=0 to k of choose(d, i)
```

paths instead of all `2^d` paths. This makes `k` a candidate measure of how
fallible the theory may be while remaining useful. A weighted variant could
charge more for contradicting a load-bearing premise than for choosing a
second-ranked local implementation.

The static form assumes that the solution tree and heuristic ordering already
exist. Theory revision can instead create new distinctions, new candidate
operators, and a new ordering. Modelling that requires the heuristic and
possibly the successor generator to be part of the mutable state.

### Iterative-deepening and cost-bounded search

Depth-limited and iterative-deepening search expose a horizon directly.
Iterative-deepening A* replaces a depth threshold with a path-plus-heuristic
cost threshold. These methods trade repeated exploration for small memory.

They may model a process that repeatedly widens how much change it will
consider while retaining little detailed frontier state. The repeated work is
not overhead to hide: it is a measurable reconstruction cost caused by the
retention choice.

### Memory-bounded heuristic search

Memory-bounded A* variants retain only a bounded frontier. When memory fills,
they discard a less promising subtree while keeping a backed-up estimate that
can cause later regeneration.

This resembles a system that keeps a compressed rationale or failure summary
but not the full abandoned investigation. Memory, summary quality, and
re-expansion work become separate variables. The analogy depends on whether a
backed-up scalar can represent what a retained natural-language rationale does;
that should not be assumed.

### Real-time heuristic search

Real-time heuristic search bounds lookahead per decision and interleaves search
with action. Learning variants update their heuristic after encountering
costly regions or dead ends.

This family exposes a constraint absent from offline backtracking: the process
must act before it has searched to completion. It can therefore price
provisional commitment, later retreat, and improvement across repeated trials.
Its usual learned state is a value estimate rather than an addressable theory,
so the comparison is functional rather than representational.

### Conflict-directed backtracking, learned constraints, and restarts

Conflict-directed search turns a failed branch into a retained constraint,
then backjumps to a decision implicated by that constraint. Restart variants
discard the current assignment while retaining some learned constraints and
search statistics. Practical budgets can count conflicts, decisions,
backjumps, retained constraints, constraint size, or work between restarts.

This is a close operational analogy for failure explanation changing later
search. Its standard logical setting also marks the main mismatch: a learned
constraint is normally required to be sound, while a retained natural-language
failure explanation may itself be wrong. A fallible analogue needs to permit
later retraction or rescoping of learned constraints and to price the search
space incorrectly pruned before correction.

### Inductive inference with bounded mind changes

Mind-change bounds limit how many times a learner may replace its current
hypothesis before stabilizing. This supplies a direct revision budget, but a
count alone misses the unequal cost of revisions. Narrowing one scope condition
and replacing a project decomposition can both count as one change while
having very different downstream effects.

A useful extension would weight a mind change by the operative dependencies it
invalidates and the reconstruction it requires.

### Checkpoint and pebble games

Pebble-style models expose time-space trade-offs in retaining intermediate
states. Read a pebble as a checkpoint from which execution can resume. Fewer
pebbles save storage but cause more recomputation when the process must recover
an earlier state.

This family may model rollback mechanics better than theory selection. It can
be combined with discrepancy or real-time search so that one model decides
which path to reconsider and the other prices whether that path remains
recoverable.

### Restart schedules and probabilistic search

A restart schedule gives successive attempts explicit cutoffs. It is useful
when search duration varies substantially between runs and the process cannot
tell early whether the current run is a long failure. A warm restart can retain
failure constraints or heuristic updates; a cold restart discards them.

Probability is optional at the architectural level. With a stochastic
generator, evaluation can compare expected cost, cost quantiles, or the
probability of reaching adequacy within a fixed envelope. Without probability,
the same schedule can be evaluated by worst-case or adversarial cost.

### Budgeted decision processes and games

A budgeted or constrained decision process represents actions with resource
costs and admits only policies that remain inside declared bounds. A stochastic
model can represent model sampling and uncertain consequences. A game model
can instead treat the house's choices and the demand stream as choices made by
different players.

This family can express ongoing operation and environment interaction, but it
is very general. It becomes informative only after the state, available
actions, observations, cost dimensions, and success condition have been fixed.

## A candidate composite to investigate

The following combination appears worth testing without yet selecting it:

1. Use limited discrepancy search to measure departures from theory-guided
   choices.
2. Use a real-time search rule to bound work before an operative decision.
3. Retain conflict explanations or other failure summaries that change later
   search.
4. Bound frontier memory and checkpoints separately, charging reconstruction
   when discarded detail is needed again.
5. Bound theory revision by propagated reconstruction cost rather than only by
   the number of mind changes.
6. Evaluate the resulting controller by reached quality, total cost, recovery,
   and human contribution over a declared demand stream.

This composition would specialize the [proposal-selection improvement loop's
search, evaluation, and operative-retention
functions](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
with distinct resource measures. It would also preserve the requirement that
theory use, consequence, revision, and later use remain on [one causally
connected path](./theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## Complexity questions

- Which parameter best predicts tractability: discrepancies, theory revisions,
  unresolved premises, retained alternatives, or evaluator weakness?
- Is budgeted reachability fixed-parameter tractable when the current theory is
  wrong at no more than `k` consequential decisions?
- Does allowing theory revision reduce discrepancy depth enough to repay the
  cost of invalidating dependent machinery?
- What changes when learned failure constraints are retractable rather than
  sound and permanent?
- Can a memory-bounded controller preserve completeness by retaining summaries,
  or can an unfaithful summary make an adequate branch effectively
  unrecoverable?
- Should success be a shortest-path objective, a reach-and-maintain property,
  bounded regret over a demand sequence, or a probability threshold under a
  resource envelope?
- Which budgets compose additively, and which impose hard independent caps?

## Scope

- This catalogue does not select or define a new machine model.
- The model names and proposed mappings are research leads. They require
  source grounding before they support a design decision or historical claim.
- Most candidate families assume a fixed search space or exact failure signal.
  A theory-mediated system may revise the representation, successor generator,
  evaluator, and search space together.
- Budgeted search does not by itself establish that the retained state is a
  theory, that a failure was attributed correctly, or that later work consumed
  the revision.

---

Relevant Notes:

- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — grounds: supplies the partial-theory, search, backtracking, delayed-evidence, and revision target being formalized
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: supplies the distinct functions to which resource budgets may attach
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — grounds: supplies the connected causal path a cost model must preserve
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: supplies the possible gain and broad-wrong-theory cost that a budgeted model could measure
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — contrasts: supplies the proof-gated case whose acceptance and failure costs differ from fallible empirical search
