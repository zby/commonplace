---
description: "Two-phase optimizer study exposes transfer and re-optimization failures, but its compounding claim lacks a fresh-start causal control and rests on a fixed Terminal-Bench decomposition."
source: https://arxiv.org/html/2607.14004v1
captured: "2026-08-04"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 08b1a1e55d05498fd3e71b2407df86bec90dce73ca7b6ce244c325f3854a0847
ingested: "2026-08-04"
type: kb/sources/types/ingest-report.md
domains: [self-improvement, harness-optimization, continual-learning, evaluation]
---

# Ingest: Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0

## Classification

An arXiv v1 preprint that defines a phased continual-learning protocol and reports controlled benchmark outcomes for three agent-harness optimizers.
Author: Wenxiao Wang, Priyatham Kattakinda, and Soheil Feizi of RELAI.ai. They release the compared artifacts and have direct implementation access, but they also introduce RELAI-VCL, the method that wins their comparison; the results have not been independently reproduced in this KB.

## Summary

The paper asks whether a harness optimizer can preserve first-round gains, transfer them to newly introduced tasks, and continue improving after those tasks enter the objective. It gives GEPA, Meta Harness, and RELAI-VCL 200 rollouts on 12 hard Terminal-Bench 2.0 tasks, evaluates transfer on a 22-task union, then gives each surviving method another 200-rollout optimization phase on that union. All three beat the baseline in Phase 1. GEPA then falls below baseline on transfer before recovering under Phase-2 optimization; Meta Harness transfers well but falls under re-optimization; RELAI-VCL leads at every stage, with pass rates of 79.2% in Phase 1, 72.7% on transfer, and 77.3% after Phase 2. The authors attribute this pattern to RELAI-VCL's in-loop rule that rejects candidates which lose previously solved tasks.

## Connections Found

This source is a useful empirical boundary case for [compounding being tested in later improvement](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). Its second phase is genuinely a later optimization episode starting from a retained first-round agent, but the experiment does not compare that start against an equally budgeted fresh start on the combined task set. It therefore shows retention, transfer, and continued optimization together, not that the retained Phase-1 benefit made the later improvement more productive under the KB's stronger causal meaning of [compounding](../notes/improvements-can-accumulate-without-compounding.md). Architecturally, the methods instantiate a [proposal-selection improvement loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), while RELAI-VCL adds another case of an effective but [frozen evaluation function](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md). Compared with [Self-Harness](self-harness-harnesses-that-improve-themselves.ingest.md) and the earlier [Meta-Harness analysis](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), its new contribution is the phased task-arrival protocol rather than another static optimizer score. All results remain bounded by [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

## Extractable Value

1. **Separate static gain, transfer, and continued improvement** -- the three-stage protocol prevents a strong one-shot score from hiding two different failures: GEPA's first update transfers poorly, while Meta Harness's transferred agent fails to improve under a second search budget. This is a reusable evaluation shape for artifact-learning systems. [quick-win]
2. **Treat prior-task regression as a selection-time signal** -- RELAI-VCL rejects a candidate during search when new-task gains cost previously solved tasks. The result supports testing regression control as an inductive bias, but the comparison does not isolate that mechanism from the optimizer's broader search space and implementation. [experiment]
3. **Do not collapse retention plus another successful update into causal compounding** -- the Phase-1 agent is retained and Phase 2 can improve it, yet no fresh-start Phase-2 arm shows that the earlier improvement helped produce the later one. The paper supplies a precise terminology boundary for the KB's compounding claims. [quick-win]
4. **Keep the failure-mode vector, not only the lifelong average** -- GEPA and Meta Harness have similar reported lifelong averages, 66.0% and 64.6%, while failing in opposite ways. A scalar average hides whether an update generalizes, remains revisable, or merely fits the current objective. [just-a-reference]
5. **Map the effective update space before crediting the optimizer** -- behavior can condition on the current harness, verifier outcomes, previously solved tasks, and method-specific candidate histories, traces, and scores. GEPA can compose prompt edits; Meta Harness can edit harness code; RELAI-VCL can propose changes to prompts, tools, workflows, memory, skills, and code. Their evidence-to-edit mappings are still determined by fixed proposer models and optimizer procedures. The underlying GPT-5.5 agent, Harbor interface, Terminal-Bench representation and timeout-based partition, two-trial scoring, rollout budgets, task verifiers, and each method's acceptance machinery remain outside the update space. The experiment compares mappings expressible within those choices; it does not validate the decomposition as a whole. [deep-dive]

## Limitations (our opinion)

The study compares three compound methods, not one optimizer with and without regression control. RELAI-VCL has a broader declared edit space than prompt-only GEPA, and Meta Harness uses a different proposer and code-search process. GEPA's code-editing variant fails to produce a valid Phase-1 candidate and is removed from later comparisons. A simpler account of RELAI-VCL's lead is therefore that its proposer, search implementation, or editable surface is stronger; the experiment does not identify the no-regression rule as the cause.

The empirical base is 22 loosely related hard Terminal-Bench tasks selected by timeout, with two trials per task and no reported uncertainty over the headline comparison. The second phase supplies only one further update episode. There is no fresh-start optimizer arm on the 22-task union, no long sequence of task arrivals, and no correlated production-domain stream. These omissions matter because the paper's “compounding” result could be retention plus a strong second optimizer run rather than a causal productivity benefit from the first retained change. More broadly, the fixed task partition, verifiers, pass-rate objective, base harness, and outer search machinery exclude corrections that need different signals, operations, mappings, or representations. The results support bounded continual harness optimization on this task population, not a general law that regression-aware optimizers compound.

## Recommended Next Action

Update [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) with this study as an `evidenced-by` boundary case: credit its later-episode and transfer design, then state that a fresh-start Phase-2 control is still required to identify the retained first-round improvement's causal contribution.
