---
description: "Proposal: Commonplace's strategy as a testable conjecture — support for search judgments and commitments built for theory building generalizes to other kinds of knowledge work more economically than per-kind tools — with its defeaters"
type: reference/types/design-proposal.md
tags: [self-improving-systems, learning-theory]
---

# Reusable commitment support as the route from theory building to other knowledge work

Workshop draft (closing condition 4 of
[open-ended-work-economics](./README.md)). Declares the design-proposal
type so the contract checks it; it moves to `kb/reference/proposals/` at
extraction and does not adopt anything.

## Current state (as of 2026-10-30)

- Commonplace's declared objective is more useful and better-warranted
  knowledge work per unit of human judgment
  ([Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md)).
  Its strategy is stated in pieces: build a theory builder and test whether
  it learns; start from a running system because use supplies selection
  where no fixed oracle exists; invest in machinery because an improvement
  is paid once and reused. No artifact states the step from that program to
  other kinds of knowledge work, or what would show the step is uneconomical.
- The machinery that exists serves theory building in a KB: types and
  collection contracts, validators, review gates, freshness baselines,
  connect and ingest skills, the search-control and commitment notes, and
  the draft refinement interface (derive, compare, locate, revise,
  evaluate, apply) in the
  [theory-refinement-interface](../theory-refinement-interface/README.md)
  workshop, which is not promoted.
- Transfer has not been demonstrated: "Both instances were authored inside
  the system that states the claim and assessed by nobody outside it"
  (instrument note). No second kind of knowledge work runs on the
  machinery. The
  [first-downstream-run](../first-downstream-run/README.md) workshop holds
  the template for an outside KB-building trial, not yet handed over.
- The library's generality rule for the KB framework is to demote closed
  taxonomies to guarded defaults and gate universality on heterogeneous
  worked cases
  ([universal knowledge framework](../../theory/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md));
  ADR 042 is its implemented instance (text contract plus profiles).
- The only recorded shared engine built ahead of its second consumer was
  retired on its carrying cost (ADR 113 to ADR 118); the
  [codify-versus-LLM](../../theory/codify-versus-llm-decision-heuristics.md)
  note's "Stake and odds" section now carries that lesson.
- The direction of development is toward unattended pipelines
  ([review-on-workjig](../review-on-workjig/README.md),
  [recurring-task-runner](../recurring-task-runner/README.md)), where
  computation cost becomes the binding comparison for controllers.

## Problem

The work-level claim is held: open-ended work allocates search before
decisive evidence, keeps "worth investigating" apart from "warranted to
adopt", retains commitments by their ground-truth status, and converts
stable patterns into routines. What is not held is the architecture-level
claim the program rests on: that *reusable* support for these operations,
built for theory building, is an economical route to supporting other
kinds of open-ended knowledge work (scientific investigation, software
architecture, legal drafting, exploration). The claim is implicit in the
lead article's bet and in the software-house endpoint, but nowhere stated
with its universality axis declared or its defeaters named. Without that
statement, every success inside the KB reads as support and no failure
reads as refutation.

The brief that posed this names the endpoint "a general computational
environment". The library does not use that term and this proposal does
not introduce it (see the workshop's
[vocabulary decisions](./vocabulary.md)); the conjecture is stated as
generalization from theory building to other kinds of knowledge work, with
the [software house](../../theory/definitions/software-house.md) as the
software-specific case of the endpoint.

## The conjecture

Stated in the form the library already uses for factories,
`F_P = configure(G, K_P)`
([agentic substrate](../../theory/agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md)):

> There is general machinery **G** — support for making, recording,
> criticizing, routing and retaining search judgments and commitments —
> such that each kind of open-ended knowledge work **P** is served by
> `configure(G, K_P)`, where **K_P** is that kind's domain knowledge
> (its types, oracles, routines and vocabulary). Building and improving
> **G** once, and acquiring **K_P** per kind, costs less over the horizon
> than building per-kind tools, and the cost of the shared abstractions
> stays below the duplication they remove.

Three held results give it its economic form. A machinery improvement is
paid once and reused by every later episode, so **G**'s return grows with
the number of kinds and episodes that use it
([machinery investment](../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md)).
The expensive part per kind is acquiring **K_P**, not constructing
machinery
([factory construction does not establish knowledge acquisition](../../theory/factory-construction-does-not-establish-knowledge-acquisition.md)),
so a shared **G** does not remove the hard work; it removes rebuilding the
easy part. And conversion of a kind's stable patterns into routines is the
mechanism by which that kind's work gets cheaper, and the conversion
machinery (observe, commit when stable, relax on failure signals, price
the stake) is the same for every kind.

**Universality axis, declared** (per the
[universality-axis note](../../theory/universal-software-factory-needs-a-declared-universality-axis.md)):

- Axis: constructional expressivity of **G** across kinds, *plus* reuse
  economy. Not production-knowledge acquisition reach: whether computation
  acquires **K_P** from evidence is the program's separate bet, and this
  proposal allows **K_P** to be human-supplied.
- Covered class: kinds of knowledge work in which consequential branches
  are generated during the work and results accumulate across bounded
  episodes. Routine work, where no search judgment is uncertain, is out.
- Supplied inputs: **K_P** by people initially; problems and acceptance
  judgments by users throughout.
- Adequacy: the declared objective, measured as the
  [ablation proposal](../../reference/proposals/ablation-baselines-for-the-declared-objective.md)
  measures it, per kind.
- Human boundary: internal production roles may be human in **K_P**
  acquisition; the conjecture is about **G**'s reuse, not about autonomy.
- Horizon and resources: stated per test; the claim is comparative over a
  horizon long enough for **G**'s reuse to amortize.

## Design space

Three options for how **G** comes to exist. The proposal does not choose.

1. **Interface first.** Promote the refinement interface and the
   search-control and commitment machinery as the declared **G**, then
   configure a second kind against it. Cheapest to state, dearest if the
   interface was shaped by theory building alone: a description that
   contains its target is weak expressivity (universality-axis note).
2. **Second kind first, extract later.** Serve a second kind with the
   existing machinery as it stands, allow bespoke additions, and extract
   **G** from what two kinds in fact shared. This is
   [progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md)
   applied to the architecture: commit the shared layer only after the
   pattern stabilizes across kinds. It pays observation time and risks the
   second kind's additions entrenching before extraction.
3. **No shared layer.** Commonplace stays a KB framework; other kinds use
   generic harness features and their own tools. This is the rival the
   conjecture must beat on total cost, and the option the bootstrap note's
   last failure condition names ("a more direct learning method achieves
   better results at comparable total cost").

Option 2 is consistent with every rule the library already applies to
itself (demote taxonomies to defaults, promote on stable repetition, size
the stake to the stated odds) and with the ADR 113 lesson. That is a
reason to expect it to be chosen, not a decision.

## Forces

- **Entrenchment and coordination value.** A shared **G** earns its cost
  only under an enduring constraint, scoped transfer evidence, or
  coordination value
  ([entrenchment](../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md),
  [coordination value](../../theory/definitions/coordination-value.md)).
  Adoption by more kinds raises migration cost without demonstrating
  transfer.
- **Carrying cost of shared abstractions.** The one recorded case (ADR 113)
  had consistency machinery exceed the domain logic it served. The
  natural-language analogue is the
  [checked-inline-blocks](../../reference/proposals/checked-inline-blocks-for-shared-instruction-text.md)
  problem: one authoritative definition against literal, sufficient text in
  each bounded context.
- **Expressiveness is not economy.** "An operation that is possible but
  too costly is different from one the permitted machinery cannot express"
  ([fixed-model house](../../theory/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md)).
  A **G** whose operations are available by interpretation for every
  kind establishes expressivity, not the conjecture.
- **Preferential codification.** A shared layer takes the predictable
  parts of each kind; the kind keeps the hard parts
  ([preferential codification](../../theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md)).
  Success of **G** therefore does not show the kind's work got easier
  overall; the measure must be per unit of human judgment, not per task.
- **Cost is step-shaped at the context boundary.** Work that fits one
  session is cheap and roughly uniform; work that must cross the boundary,
  through sub-agents, code-managed workflows or multi-step processes, pays
  for coordination machinery and handoff loss
  ([context is scarce for feasibility before cost](../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md),
  [coordination guarantees](../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md);
  ADR 113/118 priced one crossing). So the operations of **G** that stay
  inside one context are cheap for every kind, and the ones that must
  cross are where **G**'s carrying cost and the per-kind cost both
  concentrate. The conjecture's economy therefore depends on how much of
  each kind's work **G** keeps below the boundary, which is a measurable
  property of a second-kind run.
- **Unattended runs make unequal-cost comparison common.** Matched-budget
  comparison of controllers stays valid; where costs differ materially,
  net value with the exchange rate swept is the added option (the
  [Russell–Wefald ingest](../../sources/russell-wefald-principles-of-metareasoning.ingest.md)).
  **G**'s controllers need cost-per-yield records that state the regime
  they ran in before either comparison is possible.
- **The brief's wider claim is not carried.** That economic reasoning is a
  more general organizing principle than epistemology, and the rivalry
  with resource-rational accounts of routinization, are deferred in the
  workshop and are not premises here.

## Operativity and warrant

No consumer yet. What would consume **G** is a second kind of knowledge
work run on Commonplace by an operator who is not its author, through the
installed package and skills (ADR 086's delivery path), with **K_P** as
that project's collections, types and routines. The first-downstream-run
template is the nearest prepared instance, though its task is still KB
building. No oracle is added by this proposal; the ablation proposal's
measures are reused, and their warrant stops where that proposal says.

## Adoption criteria

Evidence that would support the conjecture, all comparative:

- A second kind of knowledge work runs on the machinery with only **K_P**
  added, and the record counts how much of **G** was reused unmodified,
  how much **K_P** was needed, what maintenance of **G** the second kind
  caused, and what share of the kind's work **G** kept inside one context.
- Per the ablation measures, human decisions per verified improvement in
  the second kind do not exceed those in theory building after **K_P**
  stabilizes.
- At least one of **G**'s operations moves from interpreted to mechanical
  for the second kind using the same codification path as for the first,
  so reuse is economical and not only expressive.

Evidence that would defeat it, each already named as a failure condition
in the
[bootstrap note](../../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
or the instrument note:

- The second kind requires a bespoke ontology and evaluator that share
  nothing operative with **G**.
- Maintenance of **G** grows with the number of kinds rather than
  amortizing across them.
- Human judgment per verified improvement grows as kinds are added.
- A per-kind tool, or generic harness features alone (option 3), reaches
  the same adequacy at lower total cost over the same horizon.
- **G**'s operations stay interpreted for every second kind: expressive,
  never economical.

The trigger for an adoption decision is the first completed second-kind
run with those counts recorded. Until then the proposal holds the
conjecture and its defeaters, and the program's successes inside the KB
remain evidence about theory building only.

---

Relevant Notes:

- [An optimal long-run learning strategy invests in its own machinery](../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — rests-on: the amortization argument that gives the conjecture its economic form
- [Universal software factory needs a declared universality axis](../../theory/universal-software-factory-needs-a-declared-universality-axis.md) — rests-on: the declarations a generality claim must make, applied here to kinds of knowledge work
- [Agentic substrate needs family-specific machinery to be a factory](../../theory/agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md) — rests-on: the `configure(G, K_P)` form the conjecture borrows
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — rests-on: the failure conditions reused as defeaters
- [Codify-versus-LLM decision heuristics](../../theory/codify-versus-llm-decision-heuristics.md) — rests-on: the stake-and-odds rule that bears on building G ahead of its second consumer
