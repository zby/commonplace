---
description: "ICLR 2026 HGM paper arguing immediate benchmark score is a weak parent-selection signal for self-improving coding agents; clade-metaproductivity better predicts productive lineages"
source_snapshot: huxley-godel-machine-human-level-coding-agent-development.md
ingested: "2026-04-24"
type: kb/sources/types/ingest-report.md
domains: [deploy-time-learning, harness-engineering, evaluation, self-improvement]
---

# Ingest: Huxley-Gödel Machine

Source: huxley-godel-machine-human-level-coding-agent-development.md
Captured: 2026-04-24
From: https://openreview.net/pdf?id=T0EiEuhOOL

## Classification

Type: scientific-paper -- ICLR 2026 conference paper with formal definitions, an algorithm, benchmark comparisons, ablations/correlation analysis, and citations.
Domains: deploy-time-learning, harness-engineering, evaluation, self-improvement
Author: Wenyi Wang, Piotr Piekos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, and Jurgen Schmidhuber at KAUST; worth attending to because the paper combines Schmidhuber's self-referential-machine lineage with current SWE-bench coding-agent experiments.

## Summary

The paper studies self-improving coding agents as tree search over agent self-modifications. Its central claim is that immediate coding benchmark performance is a poor proxy for an agent's future self-improvement potential: a high-scoring node can have unproductive descendants, while a lower-scoring node can seed a better lineage. The authors call this the Metaproductivity-Performance Mismatch and propose clade-metaproductivity (CMP), a lineage-level metric aggregating descendant outcomes. HGM estimates CMP from partial evaluations, uses Thompson sampling to choose expansion/evaluation, and decouples expansion from evaluation for asynchronous execution. On SWE-bench Verified, Polyglot, SWE-bench Lite, and SWE-bench-Live-style evaluations, the paper reports stronger final agents and lower allocated CPU-hours than DGM/SICA-style greedy benchmark-score selection.

## Connections Found

`/connect` placed HGM in the KB's hard-oracle self-improving-harness cluster. It is `evidence` for [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [deploy-time learning](../notes/deploy-time-learning-is-the-missing-middle.md), and [continual learning as behavior change](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md), because HGM improves durable agent scaffolds and control logic without weight updates. It also grounds [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) and [oracle strength spectrum](../notes/oracle-strength-spectrum.md): HGM works in benchmark-rich coding domains, but shows that oracle availability alone is not enough when the immediate score is not aligned with the long-run search target. Reverse-edge candidates include [HyperAgents](../agent-memory-systems/reviews/hyperagents.md), [auto-harness](../agent-memory-systems/reviews/auto-harness.md), [CORAL](../agent-memory-systems/reviews/CORAL.md), and [trace-learning techniques](../agent-memory-systems/trace-learning-techniques-in-related-systems.md). The closest sibling source is [Meta-Harness](./meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md): Meta-Harness varies diagnostic richness, while HGM varies archive-selection objective.

## Extractable Value

1. **Selection-target alignment is a separate axis from oracle strength.** HGM's strongest transferable contribution is the claim that a hard benchmark oracle can still be the wrong *parent-selection* signal when the objective is long-run lineage improvement. This extends the oracle-strength cluster: build verifiers, but also verify that the score optimizes the right temporal target. [quick-win]

2. **Clade-level evidence is a concrete alternative to greedy benchmark-score selection.** CMP treats descendants as evidence about an ancestor's ability to generate future improvements. That is a high-reach pattern for any archive-based improvement loop: evaluate lineages, not only local nodes, when mutation quality is heritable or path-dependent. [experiment]

3. **Decoupling expansion from evaluation improves control over expensive search.** HGM separates "create a child" from "spend another benchmark trial" and schedules each independently. This is directly relevant to workshop and harness loops where evaluations are costly and partial information should steer both further probing and branch creation. [just-a-reference]

4. **HGM complements Meta-Harness by naming the archive-objective axis.** Meta-Harness made diagnostic richness visible; HGM makes selection-target alignment visible. Together they suggest a three-factor model for outer-loop search: oracle strength, diagnostic access quality, and archive-selection objective. [quick-win]

5. **Benchmark-local human-level claims should be treated as weak evidence.** The reported SWE-bench Lite/SWE-bench-Live results are useful as a signal that the method is competitive, but the source's durable value is not the leaderboard claim; it is the mechanism showing why immediate performance can mis-rank future improvement potential. [just-a-reference]

6. **Symbolic self-improvement remains the tractable near-term substrate.** The paper explicitly frames HGM as editing scaffolds, prompts, and control logic while leaving weights fixed, with weight-space self-modification as future work. This supports the KB's readable-artifact loop framing without settling the opaque-loop question. [just-a-reference]

## Limitations (our opinion)

The main limitation is that the paper's strongest conclusion is benchmark-regime dependent. HGM requires repeatable trials, final-agent utility, and benchmark-style scoring; those assumptions are explicit in Assumption 1 and align with SWE-bench/Polyglot, but they do not transfer directly to KB maintenance, research taste, or other judgment-heavy domains where the oracle is soft or delayed. The simpler account for some reported gains is also not only "CMP is better" but "asynchronous scheduling and more efficient evaluation allocation reduce wasted budget"; the paper attributes both to HGM, but a future comparison would need to isolate lineage scoring from scheduling.

The CMP estimator is an approximation of descendant productivity, not proof of self-improvement in the original Gödel Machine sense. The theorem relies on true CMP under simplified assumptions; the implemented estimator inherits all the usual benchmark risks: overfitting to SWE-bench-family tasks, reward hacking against local task distributions, and instability as leaderboards and model backbones change. The "human-level" framing is especially easy to overread because it is benchmark-local and depends on officially checked submissions at a specific time. For this KB, treat the metaproductivity-performance mismatch as the portable claim and the exact leaderboard numbers as context-bound evidence.

## Recommended Next Action

Write a note titled **"Outer-loop search quality depends on selection-target alignment"** connecting to [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md), [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and [Meta-Harness](./meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md). It should argue that automated artifact-improvement loops need three distinct design surfaces: a reliable oracle, rich diagnostic access, and a selection metric aligned with long-run improvement rather than immediate local score.
