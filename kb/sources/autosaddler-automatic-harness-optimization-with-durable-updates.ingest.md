---
description: "AutoSaddler supplies benchmark and ablation evidence for trace-grounded harness patching while bounding its supervised update space and durability claims."
source: https://arxiv.org/abs/2608.23041
captured: "2026-08-25"
capture: pdftotext
genre: scientific-paper
snapshot_sha256: 3dd95428f1ae30babc46696299e96f9d06df2c55eec779f766ef5d96c0a55044
ingested: "2026-08-25"
type: kb/sources/types/ingest-report.md
domains: [agent-harnesses, optimization, evaluation]
---

# Ingest: AutoSaddler: Automatic Harness Optimization with Durable Updates

## Classification

This arXiv preprint is a scientific paper: it defines an intervention over agent harnesses, evaluates it on three benchmarks, and reports component and finer-grained ablations.
Author: A thirteen-author academic and industry team from POSTECH, KAIST, Southern University of Science and Technology, and Microsoft; the corresponding authors are affiliated with POSTECH and Microsoft.

## Summary

AutoSaddler treats harness improvement as offline learning: optimizer agents inspect successful and failed execution traces plus harness code, propose phase-constrained patches to prompts, tools, and middleware, verify patches on the current mini-batch, evaluate locally successful candidates on a development set, and retain results and lessons in an EvoDAG for later selection and recombination. Its test tables show improvements from 53.0% to 62.0% on GAIA2, 37.3% to 46.9% on SWE-Bench Pro, and 40.0% to 50.0% on Terminal-Bench 2.0, alongside lower rollout use than the adapted automated baselines. The decision-relevant result is bounded evidence that deeper diagnosis, structured intervention, and held-out selection can improve a fixed agent harness; it is not evidence that the chosen harness decomposition is complete or that the updates remain beneficial across later optimization episodes or production drift.

## Quotes

- **Source extract (verbatim):** Specifically, we evaluate a “w/o in-depth diagnosis” variant that replaces CA-SDK-based diagnosis with a shallow diagnostic baseline: a single LLM call receives the execution trace and evaluation results, and infers the failure reason, a strategy commonly used in automatic prompt optimization pipelines for failure reflection [36, 1]. The inferred failure reason is then passed back to CA-SDK for patch generation. In contrast, AutoSaddler’s in-depth diagnosis actively explores both execution traces and source code to investigate failures.
  - **Source location:** Section 5.3, RQ1, p. 8
- **Source extract (verbatim):** As shown in Table 2, removing in-depth diagnosis substantially degrades test-set performance on GAIA2, reducing Pass@1 from 62.0 to 57.8.
  - **Source location:** Section 5.3, RQ1, p. 8

## Connections Found

AutoSaddler is an empirical anchor for [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) and for the cost of [false-positive acceptance](../notes/false-positive-generation-is-filtered-before-retention.md): its diagnosis ablation reduces GAIA2 test performance, while its no-generalization-selection run retains an over-broad hook followed by a development-set regression spike. The method also instantiates the [proposal-selection loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), and its bundled headline ablations plus narrower appendix ablations make it a worked example of why [an experiment identifies only the contrast it runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md). Relative to [Meta-Harness](./meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), it adds explicit diagnostic and reflection roles, a typed and phased intervention schedule, and development-set selection; the [phased agent-optimizer study](./agent-optimizers-compound-terminal-bench.ingest.md) is the counterpoint that keeps its durability claim limited to transfer within one offline study.

The learner can condition proposals on task descriptions, supervised outcome signals, successful and failed trajectories, harness source, before-and-after traces, development scores, and accumulated EvoDAG lessons. It can diagnose failures; add or modify prompts, tool interfaces and implementations, hooks, infrastructure, and loop logic; and select, rebase, or recombine explored harnesses. Its effective hypothesis class is therefore the set of harness programs reachable through those operations and the chosen optimizer roles. Model weights, memory and skill curation, the stateless-task assumption, gold success metrics, dataset partitions, and most outer-loop design choices remain fixed. Under [the fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the gains support optimization inside that space, while each ablation supports only the particular choice it varies; they do not validate the excluded components or the decomposition as a whole.

## Extractable Value

1. **Bounded evidence for diagnostic richness** -- On GAIA2, replacing code-and-trace investigation with a shallow single-call diagnosis lowers average test Pass@1 from 62.0% to 57.8%; the full system also accumulates 20 accepted patches rather than 15. This is a concrete second case for the existing diagnostic-richness claim, scoped to this optimizer and benchmark. [quick-win]
2. **A behavioral acceptance-error case** -- Without reflection and development-set selection, an over-broad hook on a frequently used tool is retained and the measured development regression rate spikes from 8% to 22%; the full path blocks the analogous patch. This makes the cost of admitting a locally successful but over-scoped edit observable. [quick-win]
3. **A bounded intervention-space result** -- On GAIA2 mini-batches, capability patches and steering patches have similar fix rates (55% and 58%) but different regression rates (8% and 17%). The result supports investigating executable capability repairs before accumulating textual steering rules, but it does not establish that ordering beyond the tested harnesses. [experiment]
4. **An ablation-attribution example** -- The headline structured-intervention ablation removes both the taxonomy and phase schedule, while the headline generalization-aware ablation removes both development filtering and reflection with EvoDAG. Appendix variants isolate phase scheduling and development filtering more narrowly, providing a compact case for matching claims to the actual contrast. [quick-win]
5. **A durability boundary** -- Disjoint task-group tests and one Opus-to-Haiku transfer evaluation support held-out transfer, but no experiment introduces later tasks and re-optimizes the retained harness. Comparing this source with the phased optimizer study separates one-episode generalization from compounding under later updates. [deep-dive]
6. **A reusable optimizer-state pattern** -- EvoDAG retains patch lineage, scores, before-and-after lessons, and failed attempts so later search can rebase, revert, and recombine instead of continuing a single edit chain. This is a technical instance of operative retention in a proposal-selection loop rather than a new general claim. [just-a-reference]

## Limitations (our opinion)

This is a v1 preprint, and no released implementation was inspected or executed for this ingest. The paper can establish reported experimental results, but it cannot by itself confirm implementation fidelity or reproduce training, cost, and benchmark outcomes. Most methods receive one expensive optimization run; the extra stochasticity check covers a second GAIA2 run and one test universe, while three repeated test executions characterize rollout variance more than optimizer variance. Baseline adaptations and differing evaluation schedules also leave room for implementation-sensitive comparisons.

The evidence is further bounded by supervised gold outcomes, three benchmark environments, mostly Claude Opus 4.6, and stateless independent tasks. Memory, skill curation, model-weight updates, stateful deployments, security approval, canarying, and rollback sit outside the effective update space. The headline ablations remove mechanism bundles, and the finer-grained variants cover only some components on GAIA2 Universe 22, so causal claims should stay at the grain of those contrasts. Section 5.2 also contains arithmetic and assignment errors: 37.3% to 46.9% is 9.6 rather than 8.4 points, and the strongest-baseline gains for SWE-Bench Pro and Terminal-Bench 2.0 are 4.4 and 6.7 points rather than the values assigned there. Finally, held-out evaluation within one optimization study does not establish durability under later task arrival, repeated optimization, or production drift.

## Recommended Next Action

Update [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) with one bounded AutoSaddler evidence case that cites this ingest as `(snapshot required)`, reports the 62.0% versus 57.8% GAIA2 diagnosis contrast, and states that the ablation tests one trace-and-code-access treatment within a fixed optimizer and harness space.
