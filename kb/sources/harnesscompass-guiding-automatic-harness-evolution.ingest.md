---
description: "Grounded agent self-feedback raises search-set performance but hurts held-out transfer until two-track integration, while fixed-partition ablations limit the mechanism claim"
source: https://arxiv.org/abs/2608.01918
captured: "2026-08-06"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 61ecc14ec059bff03f9ee417f0711eb162fde0ad759b8476b6d66e583009910f
ingested: "2026-08-06"
type: kb/sources/types/ingest-report.md
domains: [harness-evolution, self-improvement, diagnostic-feedback, evaluation]
---

# Ingest: HarnessCompass

## Classification

An arXiv v1 preprint that specifies an automatic harness-evolution method and reports a progressive ablation, disjoint held-out evaluation, and frozen cross-model transfer.
Author: Luan Zhang, Ruochen Zhou, Dandan Song, and collaborators from Beijing Institute of Technology, City University of Hong Kong, and an independent affiliation. The manuscript is under review, reproduces its prompts, and reports direct implementation results, but this KB has not independently reproduced them.

## Summary

HarnessCompass evolves a fixed-model coding-agent harness through three controls: a generalization gate that rejects task-specific edits and separates executable capability changes from natural-language guidance; blind and hindsight first-person feedback that is reconciled and checked against trajectories; and parallel structural/guidance optimization followed by Revision, Recombination, and Refinement (R3). Starting from a bash-only GPT-5.4 harness on 50 SWE-bench Verified evolution tasks, it reports 66.0% Pass@1 after five iterations, versus 63.0% for Agentic Harness Engineering after twenty. On 450 disjoint tasks it scores 60.4% versus 54.7%, and the frozen harness raises Claude-Sonnet-4.6's full-benchmark score from 70.0% to 73.8%. The progressive ablation is more informative than the headline: the gate alone reaches 58.4% held-out, adding self-feedback raises the evolution score but lowers held-out performance to 55.8%, and adding R3 restores it to 60.4%.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a new empirical case for [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): unlike Meta-Harness's external raw-trace access, it adds the task agent's own blind and hindsight account, treats that account as a claim, and grounds it against the trajectory. Its gate also operationalizes the requirement to [state where an abstracted lesson stops](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) by demanding a transferable criterion with an applicability condition. Architecturally it extends the code-grounded [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md) loop and compares usefully with [Self-Harness](self-harness-harnesses-that-improve-themselves.ingest.md), [Meta-Harness](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), and the [phased optimizer study](agent-optimizers-compound-terminal-bench.ingest.md). The held-out and cross-model results test the final edits' reach, but [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) limits what they establish about the paper's fixed component taxonomy, two-track partition, gate, merger, and evaluator.

## Extractable Value

1. **Diagnostic evidence has viewpoint and grounding, not only volume** -- the blind report removes verdict hindsight, the hindsight report assigns failure cause, reconciliation records agreement, and a separate pass checks each item against the trajectory. This extends diagnostic richness beyond raw-versus-summarized evidence to whose perspective generated the diagnosis and how that claim earns admission. [quick-win]
2. **More diagnostic signal can improve fit while weakening transfer** -- adding proactive feedback to the gate raises evolution-set Pass@1 from 62.0% to 66.0% but lowers held-out Pass@1 from 58.4% to 55.8% and takes twelve rather than two iterations. Richer evidence expands useful search, but it is not monotonically beneficial when the resulting edits can still specialize to the search sample. [quick-win]
3. **A boundary clause can be made into an edit-admission rule** -- the gate bans task identifiers, test names, private symbols, task-specific keyword dispatch, and answer-like recitations; admissible guidance must instead state a reusable decision criterion and when it applies. This is a concrete implementation of boundary-statability, though lexical task-agnosticism alone does not prove behavioral generality. [quick-win]
4. **Held-out task and cross-model transfer give meaningful edit-level reach evidence** -- relative to the bash-only seed, the final harness gains 8.8 points on 450 unseen GPT-5.4 tasks and 3.8 points across all 500 tasks with Claude-Sonnet-4.6 without further evolution. This tests more than repeated use on the evolution set, while the per-repository regressions under Claude show that transfer is aggregate rather than uniform. [just-a-reference]
5. **Track isolation and R3 are promising hypotheses, not isolated causes** -- the final configuration restores held-out Pass@1 from 55.8% to 60.4% while preserving the 66.0% evolution score, consistent with reduced edit interference. A useful follow-up would compare joint optimization, separate tracks without R3, R3 without the structural/guidance partition, and alternative partitions under matched search budgets. [experiment]
6. **Map the effective update space before crediting the decomposition** -- behavior may condition on raw trajectories, verifier outcomes, blind and hindsight reports, reconciled feedback, confidence aggregates, and current harness state. The learner can compose edits to tools, middleware, sub-agents, prompts, tool descriptions, skills, and long-term memory, with GPT-5.4 expressing the evidence-to-edit mapping. Model weights, the seven-component representation, structural/guidance partition, two-track search, generalization gate, R3 procedure, seed harness, SWE-bench task split, verifiers, two-rollout Pass@1 objective, and acceptance rule remain fixed. The results improve choices within that space; they do not validate the space as a whole. [deep-dive]

## Limitations (our opinion)

The evidence comes from one recent preprint, one random 50/450 split of SWE-bench Verified, two rollouts per task, and apparently one evolution trajectory per configuration. The paper reports no confidence intervals, repeated evolution runs, or sensitivity to the task-sampling seed. Repeated selection on 50 tasks can reward noise, while the final 450-task evaluation is stronger evidence only for the selected final harness. Cross-model transfer covers one other, stronger model and is uneven: the appendix reports aggregate gains but regressions of 10.5 points on pytest and 4.5 points on sphinx for Claude-Sonnet-4.6.

The progressive ablation is cumulative, not factorial, and its configurations use different numbers of iterations. Adding “R3 Integration” also brings the component-wise optimization design whose independent tracks R3 merges, so the table does not isolate merging from the structural/guidance partition, parallel search, or changed search dynamics. There is no matched-budget comparison with joint optimization, no alternative partition, and no intervention that measures the claimed cross-component interference directly. The improvement therefore supports the compound final configuration more strongly than the R3 mechanism.

The generalization gate filters obvious textual leakage but cannot exclude subtler benchmark specialization. First-person reports and trajectory grounding are produced by roles sharing the same GPT-5.4 base model, so correlated diagnosis and grounding errors may survive. More broadly, the fixed evidence representation, action/component basis, hypothesis class, objective, and benchmark verifier exclude corrections that require other signals, operations, mappings, or decompositions. Held-out and cross-model performance earn scope for the evolved harness in these tested contexts; they do not show that the seven-component taxonomy or two-track split is necessary or preferable.

## Recommended Next Action

Update [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) with HarnessCompass as an `evidenced-by` qualification: add viewpoint and grounding as evidence-design axes, record the 62.0%→66.0% evolution-set gain alongside the 58.4%→55.8% held-out drop from proactive feedback, and state that richer diagnostics need transfer discipline rather than being monotonically beneficial.
