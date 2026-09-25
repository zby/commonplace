---
description: "MerchantBench measures persistent operation with delayed feedback; its skill traces separate retained procedure use from demonstrated learning, without isolating memory effects."
source: https://arxiv.org/abs/2607.28956
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 1c7d5e26fb30c762c5f2c9596739a2e49e7e7c36d13b267561d75ca92d2fcd5e
ingested: "2026-09-24"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, agent-memory, long-horizon-agents, deploy-time-learning]
learning_claims: true
---

# Ingest: MerchantBench: Long-Term Coherence in E-Commerce Operations

## Classification

An empirical benchmark paper defining a simulator, reporting comparative runs, and interpreting operating traces. Qiming Shi and colleagues are affiliated with Alibaba Group, Zhejiang University, Peking University, and Fudan University. Their access to 1688 product and supplier records supports the data grounding; the simulator's construction and evaluation remain the authors' own work. The captured paper is arXiv v2, dated 4 August 2026.

## Summary

[MerchantBench](https://arxiv.org/abs/2607.28956) tests continued store operation over 365 simulated days using 98,843 real product records, changing demand, immediate procurement costs, and delayed order outcomes. Eight models run under ReAct and Hermes, with three repetitions per configuration; the best configuration reaches 27.3% of the mean final net assets of three human participants. The simulator fixes the terminal objective, merchant interface, and demand and settlement rules. Within that setting, Hermes averages 53.3% higher final net assets than ReAct, but the comparison changes prompts, code tools, memory and skills, and context management together. Trace analysis distinguishes declining intervention from policies that remain active but fail to follow the objective or accumulated evidence. Hermes creates skills in 17 of 24 runs, while reported memory errors sometimes persist alongside damaging operating choices. These observations make the paper useful for evaluating memory through sustained behavior and outcomes, without establishing which memory mechanism caused success or failure.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies a bounded empirical case for [evaluating memory by effects](../notes/agent-memory-requirements/evaluate-memory-by-effects.md): it reports created skills, subsequent recorded uses, policy content, and terminal outcomes as different observations. Seventeen of 18 created skills record later use, but that does not establish beneficial causal uptake. Because Hermes versus ReAct is a comparison of framework bundles, its performance advantage cannot supply the missing memory-specific attribution.

It also illustrates the concern behind [governing behaviour-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md). In one Claude Opus 4.8 Hermes run, the agent inferred that removing weak listings would concentrate traffic, and its shelf contracted from 47 listings on Day 54 to three on Day 322 despite the simulator's independent demand opportunities. The case shows why retained operating beliefs deserve evaluation; it does not test whether a particular admission or revision procedure would have prevented the loss.

## Learning Claims (our opinion)

The source studies adaptation during operation: agents query realized evidence, attribute outcomes to products, change prices and portfolios, and sometimes retain procedures for later use. Hermes additionally reviews traces in the background to create and patch skills. The paper describes a range from evidence-backed rule revision to duplication and accumulation. It also reports day-stamped hypotheses marked as validated or rejected in memory. Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, skills and hypotheses are stated text (condition 1). Seventeen of 18 skills record later use, which shows consumption at trace strength (condition 2). Hypotheses labeled rejected and skills revised by evidence-cited rules show attempted refutation aimed at what stated units say, in the runs whose traces show them; other runs only accumulate or duplicate (condition 3). A year of operation presents successive decision windows with changing products, demand, and outcomes, and retained skills and hypotheses are taken up on those later decisions (condition 4). Nothing crosses runs, and treating each window as a new problem, not a round on the single net-assets objective, is our reading. On that reading the Hermes runs with evidence-cited revision are theory builders at trace strength. Learning is a separate claim, and it remains unestablished: the framework comparison changes several components together and has no memory-specific intervention.

The effective update space includes policy changes over merchant-visible histories, a run-local memory document available in both frameworks, and Hermes's additional code, memory, and skill operations. It excludes changing the simulator's terminal objective, hidden event-generation rules, and merchant action interface. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), better outcomes within this space do not compare alternative choices for those fixed boundaries. Nor does partial observability establish an irreparable information omission: order histories can reveal useful risk evidence over time. The study strengthens the demand for outcome and uptake evidence without requiring a revision to Commonplace's learning definition.

## Extractable Value

1. **An empirical separation of persistence, use, and benefit.** Skill creation in 17 of 24 Hermes runs and later use of 17 of 18 skills establish observable retention and access. The framework comparison supplies outcomes but changes several components together, leaving the causal benefit of those skills unresolved. This adds a concrete long-horizon case to the existing effects-based evaluation requirement. [quick-win]
2. **Delayed feedback creates a follow-up obligation.** A listing commits cash before settlement or adverse outcomes become visible. The relevant behavior spans detecting an anomaly, attributing it to a product, removing risk, and replacing the lost opportunity. For KB experiments, this suggests testing whether retained state supports a later decision after intervening work, rather than testing immediate recall alone; the transfer beyond merchant operations remains untested. [experiment]
3. **Changing conditions need a comparison that separates adaptation from passive improvement.** The paper's Time-aware Sourcing Gain compares actual monthly portfolio alignment with the same run's annual product mix held fixed across months. This distinguishes portfolio reallocation from favorable seasonal change affecting unchanged holdings. It is a useful evaluation construction, although its positive association with assets does not isolate the causal effect of learning. [just-a-reference]

## Limitations (our opinion)

There are three runs per model-framework configuration and three human participants, each completing a simulated year over five calendar days. The best configuration has a reported coefficient of variation of 55.1% in final assets. The 27.3% comparison therefore describes these samples and interfaces, not a general ratio between human and agent capability or a year of real deployment.

Real product histories constrain the simulation, but demand elasticity, listing exposure, rating thresholds, risk sampling, and settlement rules still determine the operating world. A simple alternative explanation for part of the performance gap is failure to exploit these particular rules consistently. The paper does not isolate a domain-general coherence mechanism from task knowledge, quantitative bookkeeping, exploration, or context management. Tool activity correlates with outcomes, yet neither more calls nor more recorded memory proves better decisions.

The framework comparison has no matched skill-withholding or memory-content intervention. Trace examples of erroneous beliefs and shrinking portfolios are suggestive, not controlled evidence that retained memory caused the loss. The paper reports a released implementation, but no implementation was inspected or executed for this ingest; reported outcomes have not been reproduced here.

## Recommended Next Action

Update [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) with MerchantBench as a bounded case separating created skills, recorded use, and business outcomes, keeping the absence of a memory-specific intervention beside the example.
