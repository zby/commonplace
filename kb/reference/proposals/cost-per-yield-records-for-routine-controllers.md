---
description: "Proposal: give each routine search controller a record of what it brought to stronger evaluation and what it cost, stating the context regime it ran in, so that controllers in unattended pipelines can be compared on cost as well as yield"
type: reference/types/design-proposal.md
tags: [evaluation, improvement-loop]
---

# Cost-per-yield records for routine controllers

## Current state (as of 2026-10-30)

- A search controller is judged by what it routes into stronger
  evaluation, compared with alternatives under matched tasks, resources and
  downstream evaluation
  ([a search controller is tested by what it brings to stronger evaluation](../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md)).
- Seven recorded Commonplace comparisons fit that definition. Cost entered
  the basis in three (the description-length assay, the meta-analyser
  investigation order, bundled review output) and reversed no preference;
  all three are in the automated review pipeline. The controllers a person
  still drives have no cost record: the connect sampler has an ordinal "in
  order of cost" list, the grounding reading budget disclaims an attention
  price, the full-pass finding-routing report type has no cost field, and
  the revise-autoreason critic records a call budget and one trial's
  minutes. Review gates are described as "cheap per pair" with no figures.
- The direction of development is toward unattended pipelines (the
  `review-on-workjig` and `recurring-task-runner` workshops), where a
  controller runs many times without a person and computation becomes the
  binding cost.
- The comparison form for controllers of unequal cost is known: net value
  of a computation is its benefit to the decision minus its cost, and
  unequal-cost controllers are compared with the exchange rate swept
  ([Russell and Wefald](../../sources/russell-wefald-principles-of-metareasoning.ingest.md)).
  It needs cost per controller run, which nothing records.

## Problem

Matched-budget comparison of controllers stays valid in every regime, but
unattended runs make the other case common: two controllers whose costs
differ materially, where the question is whether the extra yield is worth
the extra cost. That comparison cannot be made, or even posed, for the
routine controllers, because their cost is not recorded. Adding the record
is cheap while the pipelines are few and the controllers are being rebuilt
as workflows; it is costly once many runs exist without it, since the
record cannot be reconstructed afterwards. This is the
[machinery-investment](../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md)
argument applied to measurement.

A cost record needs two things the resource figures of one call do not
give. The context boundary is a feasibility limit, not a price
([context is scarce for feasibility before cost](../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md)):
work that fits one session and work that must cross through sub-agents,
code-managed workflows or any multi-step process are not two points on
one cost scale, and a run's regime is context metadata that says which
comparisons are like for like. Crossing also adds a cost component that
per-call figures miss: coordination machinery and handoff loss
([coordination guarantees](../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md));
ADR 113 and ADR 118 priced one crossing at about 3,000 lines of
consistency machinery against 1,000 of domain logic. Neither fact makes
the regime a cost figure. Which of two controllers is cheaper is decided
by resource figures summed over the run, including the crossing
machinery, or left unknown.

## Design space

What a record holds, from least to most:

1. **Context metadata only.** Per controller run: whether it stayed
   inside one context or crossed, and if it crossed, by what (sub-agent,
   headless worker, workflow step), plus the yield measure the controller
   note already asks for (what reached stronger evaluation and whether it
   changed a later decision). Cost is recorded as unknown. Cheap, and
   enough to say which later comparisons are like for like; it cannot say
   which controller is cheaper.
2. **Regime plus coarse resource figures.** The above plus calls, elapsed
   time and, where a harness reports it, tokens. Enough for a matched-budget
   comparison and for an exchange-rate sweep when costs differ.
3. **Full ledger.** Per-step accounting across the run. Likely more than
   the comparison needs and a maintenance burden of its own.

Where the record lives is a free choice between the run's result file
(the review-on-workjig result files already carry note and criterion
hashes) and a separate per-controller log; the former keeps cost next to
yield.

## Forces

- The yield side must credit only a changed later decision; a controller
  step that raises confidence without changing a choice earns nothing and
  pays its cost (Russell and Wefald, Section 5.1.1).
- A regime flag is near-free to record and never wrong, but it is not a
  cost figure; resource figures are, and they vary by harness and may not
  be comparable across runs.
- Recording cost for human-driven controllers measures the person's
  attention, which the declared objective already counts as human
  judgment; the record is for unattended runs first.
- A ledger that nobody consumes is itself a conversion built ahead of
  recurrence; option 1 keeps the stake small until a comparison is run.

## Operativity and warrant

The consumer is the workflow that runs the controller: it writes the
record as part of its result. The first candidates are the review
workflows being rebuilt over Workjig and the recurring tasks, since both
run controllers unattended and already write result files. No oracle is
added; the record supplies inputs to a comparison a person or a later
instruction makes.

## Adoption criteria

- Adopt option 1 when the first unattended workflow ships a controller it
  would be useful to compare with an alternative; the record then costs one
  field per run.
- Move to option 2 when a comparison between controllers of materially
  different cost is actually wanted; option 1 records cannot decide it.
- Withdraw if, after two unattended workflows have run for a period, no
  comparison has used the records.

---

Relevant Notes:

- [A search controller is tested by what it brings to stronger evaluation](../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — rests-on: the yield side of the record and the matched-resources comparison it keeps available
- [Context efficiency is the central design concern in agent systems](../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — rests-on: separates the feasibility face (context metadata) from the aggregate cost face (resource figures); the record keeps both apart
- [An optimal long-run learning strategy invests in its own machinery](../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — rests-on: why the record is worth adding before the runs multiply
