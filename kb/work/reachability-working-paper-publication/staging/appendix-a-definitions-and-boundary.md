# Appendix A — Definitions and system boundary

```text
Versioned argument snapshot for: The Reachability Conjecture
Paper version: pending
Mode: paper adaptation
Frozen source tag: pending
Source paths: kb/notes/definitions/software-house.md;
  kb/notes/definitions/representational-form.md;
  kb/articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md;
  kb/articles/reachability-as-closure-under-the-seed-gate.md
Live successors: the same paths on the main branch
Status: staging — not published
```

This appendix fixes the meanings the paper uses and states how they depend on
one another. The live definitions are broader; only the meanings this paper
needs appear here. Definitions marked *paper-specific* exist for this paper and
are not claimed as general terms.

## A.1 Software house

A **software house** is the complete persistent system responsible for
developing and evolving software for external users. It responds to their
requirements, feedback, and the consequences that arise when the software meets
its operating environment. It is not necessarily a company, a tool, or a
particular production method. It includes the software it is responsible for,
the production knowledge and machinery it uses, and every person or
computational component that fills an internal role.

*Persistence* means continuity of responsibility for the software across demands
and consequences. It does not mean indefinite life, fixed membership, or
retention of every change. Persistence alone establishes neither retention nor
learning; those are separate claims (A.7).

The paper writes **the house** for the software house under discussion.

## A.2 Internal role and external user

An **internal role** is work the house depends on to produce the software,
whoever performs it. For this paper the decisive internal roles are diagnosing
implementation failures, comparing internal candidates, editing the project
theory, and choosing which revision is kept. The live definition calls this an
internal production role.

A **user** stays outside the house while supplying requirements, domain
knowledge, preferences, feedback, observed outcomes, later demands, or
acceptance judgments about visible behaviour. The same person may be a user in
one interaction and fill an internal role in another. The role, not the person,
decides which side of the boundary an act falls on.

An **automated software house** is one in which no human is required for an
internal role over its declared product scope and operating horizon. User
participation is compatible with automation; dependence on a human for an
internal role is not.

## A.3 Product scope, operating horizon, and budget

**Product scope** is the declared range of software and demands the house is
responsible for. The **operating horizon** is the declared period, or number of
demands, over which it must keep serving that scope. The **budget** is the
declared compute, time, and cost within which the claim is tested. All three
are declared before a witness run and may not be narrowed after a failure is
seen.

## A.4 Forms of retained state

Retained state is classified by how its behaviour-shaping content is encoded and
consumed.

- **Natural-language** state takes its consequences from interpretation by a
  language model or a person: notes, rationale, policies, playbooks.
- **Symbolic** state takes its consequences from a defined consumer such as a
  parser, runtime, schema, validator, or test: code, schemas, tests, tools,
  rules for how production is done.
- **Distributed-parametric** state carries content in numerical parameters:
  model weights, adapters, embedding spaces, learned rankers.

The paper writes **notes and code** for the natural-language and symbolic state
together, and **weights** for distributed-parametric state. The conjecture
pins every distributed-parametric component and lets only notes and code learn.
Derived indexes regenerated from notes and code under pinned machinery are
views of that state, not learned state.

## A.5 Program theory

A **program theory**, after Naur, is the capacity to relate the software to the
activity it supports, to explain why the software is organized as it is, and to
relate a new demand to that organization. The paper treats it as a capacity of
the house as a whole. It may be carried by explicit notes, by reliable
reconstruction from retained records at the moment of use, or by a mix. No
single component holds it: a note nobody loads is inert, a fixed model without
project state guesses, and code executes a decision without supplying the
judgment that chose it.

A learning path is **theory-mediated** when it represents a candidate theory
as an intermediate object and changes behaviour by adopting, applying,
rejecting, or revising it, so that the process can reason about what the
theory says rather than only reproduce the behaviour it induces. The
explicit-theory hypothesis in the paper body is the claim that a house learns
better along such a path than by reconstructing its understanding from raw
records each time.

## A.6 State, seed, successor, and regime

A **house state** is the complete mutable content of the house at one moment:
its notes, software, production machinery, retention rules, evaluators, and
context assembly. Pinned weights are fixed parameters of the experiment, not
part of the state.

The **seed** is the hand-built initial state. A **successor** is a state
produced from the current state by the house's own update machinery and a
permitted external input. Once no human fills an internal role, every later
state is a successor of a successor, so the seed governs the lineage by
descent: a change to the update machinery itself must be produced by machinery
already reachable from the seed.

A **regime** (*paper-specific*) is the full declaration a witness makes before
a run: the pinned models and other weights, the seed, the permitted external
inputs, the demand process (A.8), the product scope, the horizon, and the
budget. Every claim in the paper is relative to a regime.

## A.7 Learning by the house

A retained change is **learning by the house** when experience causes it and it
changes how the house handles a later job it has not yet been given. Carrying
forward the product state an earlier request asked for is not learning, because
the next job starts from the changed product either way. A validator added
because a bug class recurred, which later blocks that class, is learning. A
note never loaded by context assembly is not.

## A.8 Demand process

The **demand process** (*paper-specific*) is the declared source of demands and
consequences a witness run draws on. Three objects in it are distinct and are
all fixed before the run:

1. the set of **admissible histories**: which sequences of demands and
   consequences the process may produce;
2. the **realized history**: the one sequence a particular run produced; and
3. the **selection distribution**: how likely each admissible history was.

None may be changed after a failure is seen; a failed demand may not be removed
after the fact. The process is **open-ended** when the admissible set is not a
fixed list of benchmark tasks and permits *relevant novelty*: demands whose
correct handling is not stated verbatim anywhere in the seed and that require
relating the demand to the product's organization.

## A.9 Adequate state

A house state is **adequate** (*paper-specific*) for a regime when the house,
starting from that state with no human in an internal role, handles the demands
the process may next produce coherently: its changes fit the software's
existing organization, preserve the purposes recorded for it, and do not
require later rescue; and its project-specific notes and code are causally used
in producing those changes, including on implications the state does not spell
out. Adequacy is a property of a state under the fixed machinery, judged over
the demands that follow it, not at an instant.

Adequacy is tested, not read off. With everything else held equal, withholding
or replacing the relevant project-specific state must change what the house
does next in a predicted way. A state whose notes are stored but never govern
a decision is not adequate however complete the notes look.

## A.10 Hitting probability and continuation reliability

Under a regime, the successor relation induces a distribution over lineages
from the seed. Two quantities of that distribution are distinct
(*paper-specific*):

- **Hitting probability** is the probability that the lineage reaches an
  adequate state with no human in an internal role within the budget.
- **Continuation reliability** is the probability that, having reached an
  adequate state, the house remains adequate across the rest of the declared
  horizon and its demands.

A house that occasionally reaches a good state and then drifts differs from one
that reaches it less often but stays coherent; the two numbers keep those
apart. The paper fixes no universal threshold for either. The witness declares,
before the run, what values count as usable for its product and risk level
(Appendix C).

## A.11 Practical reachability

Adequate states are **reachable** under a regime when at least one lineage from
the seed contains one. That is cheap: if the update machinery can emit almost
any state, almost any state lies somewhere in its support, and one lucky path
establishes only possibility.

Adequate states are **practically reachable** (*paper-specific*) under a regime
when both the hitting probability within the budget and the continuation
reliability across the horizon meet the thresholds the witness declared in
advance. The reachability conjecture is the claim that at least one regime
built on models available by the cutoff date makes adequate states practically
reachable for a non-trivial product scope.

## A.12 How the definitions fit together

A regime (A.6) fixes what may vary. Its demand process (A.8) and successor
relation generate lineages of states from the seed. Some of those states are
adequate (A.9), meaning they carry a program theory (A.5) that the house as a
whole uses. Hitting probability and continuation reliability (A.10) say how
reliably lineages reach and keep adequate states; practical reachability
(A.11) is the declared-threshold version of that. Learning by the house (A.7)
is what must happen along a lineage for the seed's hand-built theory to be
outgrown rather than merely preserved. The internal-role boundary (A.2) is what
makes the lineage the house's own rather than a person's.
