---
description: Defines staged comparisons that isolate theory-mediated search, candidate choice, evidence acquisition, and cross-episode retention before combining them.
type: kb/types/note.md
---

# How to test theory-mediated learning

> **Status:** Proposed design. None of these comparisons has been run.

The design asks two questions. First, does an explicit working theory improve a specific decision relative to direct action or equally resourced deliberation without an explicit theory? Second, does retaining and revising theories improve decisions in later episodes relative to reconstructing a fresh theory from the same history?

Isolate these roles before combining them. Otherwise, an end-to-end gain cannot show whether theory improved candidate search, candidate choice, or evidence acquisition. Using one theory across all three roles may also create a self-confirming loop.

## Common protocol

Each study should select one decision for the theory to guide. For that decision, compare three reasoning arms:

1. **Direct baseline:** make the decision without an explicit intermediate artifact.
2. **Deliberation-matched control:** use the same call structure and resource budget for a structured plan or scratchpad, but do not require a mechanism, premises, scope, or falsifiable consequences.
3. **Theory treatment:** construct a working theory `tau` that states a mechanism or invariant, premises, scope, expected and collateral consequences, uncertainty, and a possible falsifier.

Record the theory before making the decision it is meant to guide and before revealing the corresponding hidden outcomes. Separate theory-construction and decision contexts make it possible to withhold, shuffle, or modify a load-bearing premise. If those interventions do not change the decision as predicted, the artifact may be unused narration rather than a mediator.

Hold the base model, visible evidence, task instances, available actions, and total resource budget fixed where possible. Charge and report any unavoidable differences in model calls, tokens, latency, tools, or human judgment. Score each decision with an independent audit that remains hidden until the decision is frozen. Predeclare the primary endpoint, harm bound, cost-accounting rule, and advancement rule, then replicate across tasks, seeds, and held-out change families.

## Test one role at a time

| Role | Hold fixed | Primary comparison |
|---|---|---|
| **Candidate search** | Task evidence, model, available edit surface, candidate count, total budget, and hidden full evaluator | Best independently evaluated candidate found within budget; total cost to the first admissible improvement is a secondary measure |
| **Candidate choice** | Candidate pool and observed evidence | Selection regret and harmful adoption |
| **Evidence acquisition** | Candidate set, obligation and procedure registry, procedure source, and commitment rule | Total decision cost subject to a predeclared harmful-miss bound |

In the search study, run the same independent evaluator on every candidate after generation and prioritization are frozen. Evaluator-only anchors must remain hidden until then. This prevents theory-guided evidence selection from being mistaken for better search.

In the choice study, every arm sees the same candidates and evidence. Theory-derived projections may organize that evidence, but they do not count as additional observations.

In the evidence study, compare a direct non-theory selector, a deliberation- and budget-matched non-theory selector, and a theory-guided selector. Treat full evaluation as a reference, not as a budget-matched arm. Record `I_tau(S, Omega, Delta)` before outcomes are revealed. Use shadow full evaluation or randomized audits of omitted obligations to identify harmful misses. Keep the procedure source fixed at this stage so that procedure-generation failures cannot be attributed to the theory or selector. The [selective-evaluation model](./selective-evaluation-model.md) defines the obligation and acceptance distinctions this phase tests.

## Test retention separately

A later study should compare:

1. direct reasoning over raw episodic history with no explicit theory;
2. a fresh `tau_n` reconstructed from that same history in every episode; and
3. a retained, revisable `T_n` that is retrieved and applied to form `tau_n`.

All arms must receive the same source observations and authorized evaluator outcomes. Charge theory construction, storage, retrieval, applicability checking, maintenance, and correction. Record whether the retained theory was actually retrieved and used; storage alone cannot explain a later effect.

The task stream should contain shifts that preserve the theory's named mechanism, break one stated premise, and invalidate the theory more broadly. Predeclare either decision quality at a fixed total cost or total cost at a fixed quality and harm bound as the primary result. Count harmful negative transfer from stale or overbroad theories. A frozen retained theory can be added later to separate reuse from revision.

Candidate changes and theory revisions need separate gates. A candidate may work for the wrong reason, while a failed candidate may still expose a useful counterexample. Where possible, replay common audit outcomes across arms so that a theory is not credited for evidence only one trajectory happened to observe.

## Combine only effects that survive isolation

If individual roles qualify, compare search-only, choice-only, evidence-only, and combined theory treatments. Keep an independent audit outside the theory-shaped evidence surface. For online studies, use common checkpoints or replay because accepted changes alter later states and opportunities.

The objective, evaluator, and comparison rule must be fixed independently of any candidate within an episode. A proposal to change any of them belongs in a separately authorized episode.

## Treat generated procedures as another factor

Only after an evidence selector qualifies should a study compare fixed registered procedures with retrieved, adapted, or generated procedures. A generated procedure needs three checks:

- **Technical validity:** it executes safely, remains contained, and satisfies its structural constraints.
- **Observational validity:** it can detect the obligation it claims to measure.
- **Decision value:** its construction, validation, and execution cost is justified for the current decision.

[SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) motivates this factor through its adaptive generation of executable environments. It does not test the proposed theory-conditioned selector, so procedure generation remains an independent treatment.

## System-specific handoffs

- **HCL:** The [HCL reading](./hcl-reading.md) motivates inserting a pre-recorded theory between execution evidence and harness proposal, first under full evaluation and later in the selective-evaluation study.
- **SPADE:** The [SPADE invitation](./for-spade-authors.md) asks whether a designer can generate procedures for theory-derived obligations or disagreements between rival theories.
- **Exo:** The [Exo case](./exo-case.md) and [evidence ledger](./exo-evidence.md) motivate the retained-theory study on a mutable substrate. A compounding claim requires showing that the productivity of a later improvement episode counterfactually depends on an earlier retained benefit.

An isolated improvement establishes only that theory helped one role under the tested conditions. Advance to a combined or deployed study only when the primary endpoint improves without violating the predeclared harm bound after total cost is counted. A null or harmful result should stop or narrow the proposal rather than be rescued by adding more moving parts.
