---
description: "HCL turns harness edits into retention-gated continual learning, but finite anchors bound its no-forgetting claim and fixed partitions limit its ablations"
source_snapshot: "harness-continual-learning-adaptation-beyond-model-parameters.md"
ingested: "2026-08-21"
type: kb/sources/types/ingest-report.md
domains: [harness-learning, continual-learning, self-improvement, evaluation]
---

# Ingest: Harness Continual Learning: Continual Adaptation Beyond Model Parameters

Source: [harness-continual-learning-adaptation-beyond-model-parameters.md](harness-continual-learning-adaptation-beyond-model-parameters.md)
Captured: 2026-08-21
From: https://arxiv.org/abs/2608.19013

## Classification

Genre: scientific-paper -- an arXiv v1 preprint that formalizes sequential harness updates and reports benchmark comparisons, a retention-budget sweep, and component ablations.
Domains: harness-learning, continual-learning, self-improvement, evaluation
Author: Borui Kang, Jinrui Gu, Junhan Lv, Wenbin Li, Lei Wang, and Yang Gao, affiliated with Nanjing University and the University of Wollongong. They report direct implementation results, but this recent preprint is not peer reviewed and its outcomes have not been independently reproduced in this KB.

## Summary

Harness Continual Learning (HCL) treats a frozen-model agent's Task Interface, Experience Memory, Capability Map, and Adaptive Router as one persistent, jointly versioned learning state. A Continual Optimizer uses post-execution evidence to propose isolated component changes; a Continual Evaluator commits the resulting candidate only if it improves current validation performance, stays within a historical-anchor loss budget, and passes validity checks. Across ALFWorld, Minecraft, four textual-reasoning tasks, and four multimodal tasks, the authors report capability gains together with measurable regressions on earlier behavior. A textual sweep makes the stability–plasticity control concrete: average forgetting rises from 0.39 at historical-loss tolerance b = 0 to 3.45 at b = infinity, while final average performance peaks at the intermediate b = 1 rather than under unrestricted updates.

## Connections Found

This paper is a direct empirical anchor for [governing behaviour-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md) and treating [the deployed system, not the model alone, as the learning unit](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): model weights remain frozen while committed prompt, memory, skill, and routing changes produce both gains and forgetting. Its optimizer–evaluator–commitment path is a worked [proposal-selection improvement loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). Relative to [Self-Harness](self-harness-harnesses-that-improve-themselves.ingest.md), HCL adds an explicit sequential history, sampled anchors, and a tunable loss budget; relative to the near-inversely named [Continual Harness](continual-harness-online-adaptation-foundation-agents.ingest.md), it replaces direct online edit adoption and optional weight training with isolated fixed-weight candidates. The finite-anchor result qualifies the whole architecture through [oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), while its experimental interpretation rests on the [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

## Extractable Value

1. **A retention budget controls strictness over an oracle sample, not global forgetting** -- b = 0 forbids losing any incumbent-solved anchor, yet separate historical test sets still show nonzero forgetting: 0.39 in the textual budget sweep, 0.22 in the main multimodal run, and 2.64 in ALFWorld. This is a concrete empirical case for separating gate strictness from the domain represented by its checks. [quick-win]
2. **Harness-level forgetting names a real non-parametric regression class** -- a later prompt, memory, skill, or routing update can break an earlier answer, tool call, or action trajectory even when model weights never change. The term gives the KB a useful retrieval handle for the regression problem already implied by governed deployment-time writes. [quick-win]
3. **Proposal, evaluation, and commitment can be made explicit harness-state transitions** -- HCL keeps a candidate separate from deployed state, compares incumbent and candidate under matched model, decoding, tool, environment, and seed conditions, and makes current improvement, historical retention, and validity conjunctive admission requirements. Joint commitment prevents a partially accepted multi-component candidate from becoming operative, although it does not by itself solve search or credit assignment. [experiment]
4. **Atomic deployment and component-wise search are different design choices** -- the final harness is committed as a whole, but alternatives are generated and retained sequentially in a predefined component order while the other components stay fixed. This makes deployment consistency explicit while leaving an order-dependent coordinate-search hypothesis class; “jointly versioned” should not be read as joint optimization. [deep-dive]
5. **More plasticity is not monotonically better in the reported trajectory** -- the independent textual sweep's best final average is 63.46 at b = 1, compared with 60.13 at b = infinity, while forgetting increases monotonically across the tested budgets. This supports testing historical regression constraints as a search bias, but the single fixed-order sweep does not establish the authors' proposed overwrite mechanism or a general optimal budget. [experiment]
6. **The effective update space is auditable** -- behavior can condition on raw interaction, structured task input, execution context, outcome, feedback, raw and abstract memory, and prior harness state; the evaluator additionally sees current validation cases and historical anchors. The learner can compose edits to interface prompts and parsers, memory records and summaries, inner skills, and routing prompts, criteria, and workflows; frozen LLMs implement the evidence-to-edit, summarization, skill-extraction, and routing mappings. Fixed outside that space are model weights, outer capabilities and runtime, the four-part state partition and memory-to-skill pipeline, optimizer/evaluator procedures, component order and alternative budget, anchor sampling and success criteria, task representations and order, objectives, and the all-or-none commitment rule. The experiments test improvement within this compound design, not whether its fixed layer is necessary or preferable. [deep-dive]

## Limitations (our opinion)

The evidence is paper-only. The snapshot exposes no implementation repository, no code was inspected or executed, and none of the training or benchmark outcomes was reproduced. The tables report point estimates without repeated-run uncertainty, despite random tie-breaking and trajectory-dependent proposals. Different model families are used for different task regimes, so coverage across models and coverage across tasks are confounded rather than a controlled transfer test. The MemP and MemRL baselines are reimplemented inside the authors' harness rather than run from their official repositories, and Minecraft retains skill tests without systematically replaying completed tasks, so its result is skill-level rather than full task-level retention.

The retention guarantee is deliberately local but easy to overstate. Historical anchors are finite samples, and b = 0 only protects anchors that the incumbent currently solves; it says nothing about unrepresented prior behavior. The paper's own held-out forgetting at b = 0 demonstrates this gap. Validity checks cover syntax, schema compliance, legal tool use, task constraints, and environment consistency, not general semantic or safety preservation. The autonomous commitment rule is therefore warranted only within the evaluator's sampled and task-specific domain.

The four-component account is a useful engineering partition, not an experimentally validated decomposition. Every ablated component remains present with initialized contents while only its persistent updates are disabled. Disabling Memory also removes Abstract Memory as a source of new skills, so that arm varies direct memory learning and a downstream capability path together. Variants then follow different candidate trajectories, making their commitment counts and later states non-comparable; small final-average differences are reported without uncertainty. As [an experiment identifies only the contrast it runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), these interventions support the tested update-permission bundles, not the necessity of Task Interface, Memory, Capability Map, or Router as the correct four-part carve.

A simpler account of much of the gain is repeated benchmark-guided adaptation over prompts, stored examples, output schemas, skills, and routing under extra evaluation, rather than a general continual-learning paradigm. The paper strengthens that account by measuring sequential regression and varying the retention gate, but fixed task orders, short controlled streams, one textual budget sweep, task-specific success criteria, and a frozen outer optimizer leave long-lived open-domain retention, alternative decompositions, and evaluator evolution untested.

## Recommended Next Action

Update [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) with HCL as a worked empirical case: record that a zero-loss gate over finite historical anchors still produced nonzero held-out forgetting, and use it to distinguish acceptance strictness from retention-coverage warrant.
