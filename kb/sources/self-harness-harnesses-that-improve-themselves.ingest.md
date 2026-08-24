---
description: "Same-model harness optimization improves three Terminal-Bench agents through structured failure mining and regression-gated local edits, within a tightly fixed outer method"
source: https://arxiv.org/html/2606.09498v1
captured: "2026-08-02"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 28b4792629559f4ffd2bb587a64ee281d5f13a561cc0b49b1d36358cc1d63b11
ingested: "2026-08-02"
type: kb/sources/types/ingest-report.md
domains: [self-improvement, harness-learning, trace-learning, evaluation]
---

# Ingest: Self-Harness: Harnesses That Improve Themselves

## Classification

An arXiv v1 preprint that defines an iterative harness-editing method and evaluates it on a fixed Terminal-Bench-2.0 subset across three base models.
Author: Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, and Shuyue Hu of the Shanghai Artificial Intelligence Laboratory; the recent results have not been independently reproduced in this KB.

## Summary

Self-Harness asks whether the model being improved can also propose changes to its own operating harness, without a stronger external proposer. The loop mines failed held-in execution traces into verifier-grounded signatures, gives the same fixed model a bounded set of editable harness surfaces and structured failure evidence, generates several minimal candidate edits, and promotes only candidates that improve at least one of two task splits without reducing pass count on the other. On a filtered 64-task Terminal-Bench-2.0 set, the authors report held-out pass-rate changes from 40.5% to 61.9% for MiniMax M2.5, 23.8% to 38.1% for Qwen3.5-35B-A3B, and 42.9% to 57.1% for GLM-5. Retained edits differed by model but converged on artifact reliability, bounded tool use, recovery from repeated failures, persistent environment changes, and earlier movement from exploration to implementation and verification.

## Claims

No claims have been grounded yet.

## Connections Found

The paper is a direct empirical instance of a [proposal-selection improvement loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): parallel bounded edits perform search, a reject-capable two-split gate performs evaluation, and merged harness changes become operative retention. It adds another fixed-weight case for [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and its separation of verifier outcomes from structured failure mechanisms bears on [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Its distinctive role is actor allocation: unlike [Meta-Harness](meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) and the reviewed [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md), the target model is also the proposer; unlike [Co-Harness](co-harness-co-evolving-harness-and-model-weights.ingest.md), model weights stay fixed. That supports the reallocation frame in [Computationally directed self-improvement](../notes/computationally-directed-self-improvement-is-a-reallocation.md), while [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) limits what the benchmark gains establish about the human-designed outer method.

## Extractable Value

1. **Same-model proposal generation works in a bounded harness loop across three model families** -- the reported gains show that useful harness search need not always rely on a stronger external coding agent; the evaluated model can turn its own failure evidence into operative edits when the editable surfaces and gate are tightly structured. This is evidence for a computational allocation, not for methodological closure. [just-a-reference]
2. **The trace-to-edit interface is unusually explicit** -- each failure signature separates terminal verifier cause, the causal status of the relevant behavior, and an abstract mechanism; the proposal record then names the targeted pattern, edited surface, expected effect, and regression risks. That is a reusable candidate architecture for turning traces into falsifiable local changes. [experiment]
3. **Selection signals and proposal evidence are kept distinct** -- held-out pass counts decide promotion, while held-in trace patterns, passing behaviors, and prior-attempt summaries condition the next proposal. This operationalizes the KB's diagnostic-richness distinction more cleanly than a scores-only optimizer, although the paper does not ablate the structured bundle against raw traces, summaries, or scores. [quick-win]
4. **The accepted edits expose both common and model-specific harness debt** -- all three final harnesses improve delivery or preservation of verifier-required artifacts, while retry discipline, environment persistence, structured tool content, and exploration limits differ by model. This cautions against treating one hand-tuned harness as model-independent while still suggesting artifact reliability as a cross-model pressure. [just-a-reference]
5. **The effective update space is narrow enough to audit** -- behavior can condition on held-in task traces, verifier outcomes, inferred failure signatures, passing examples, and prior edit summaries; the same model can compose bounded edits over declared instructions, tools, verification guidance, memory/skill/subagent slots, and runtime controls. The hypothesis class excludes model-weight changes and broad replacement of the control architecture, while the DeepAgent base, default tools, benchmark subset, task split, evaluator, failure-signature representation, pass-rate objective, and acceptance rule remain fixed. The gains establish improvement inside this compound configuration, not that those fixed choices are necessary or best. [deep-dive]

## Limitations (our opinion)

The reported “held-out” split is hidden from the proposer but repeatedly consulted by the promotion gate. It is therefore validation or selection data, not an untouched final test set, so its improvement cannot independently establish generalization beyond the optimization procedure. The study reports only a filtered 64-task subset of one terminal benchmark, two attempts per harness candidate, three models, and no confidence intervals or matched untouched test evaluation; pass-count non-regression can accept stochastic noise, especially after repeated candidate selection.

The central components are not isolated. There is no scores-only, raw-trace, alternative-summary, no-clustering, external-proposer, random-edit, or equal-budget search control, so the results do not identify whether same-model proposal, the failure-signature decomposition, proposal diversity, minimality, or simply repeated benchmark-guided editing caused the gains. Exact clustering is deterministic only after causal status and abstract mechanism have been inferred; the paper does not establish that those attributions are faithful. Merging individually accepted edits can also introduce interactions not attributed to any one proposal.

Finally, the experiment fixes the model, evaluator, objective, DeepAgent architecture, declared edit surfaces, evidence representation, and benchmark distribution, while excluding unsupported multimodal tasks and unreliable external-resource tasks. In the terms of [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the loop can improve mappings expressible by local harness edits from the retained trace signals, but it cannot test corrections requiring different observations, operations, architectures, objectives, or weight updates. The paper supports bounded harness adaptation, not open-ended or generally warranted self-improvement.

## Recommended Next Action

Add a worked Self-Harness case to [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), using it to show computational search/evaluation/retention in one fixed-weight harness while explicitly preserving the distinction between reallocated pathway functions and the human-fixed outer method.
