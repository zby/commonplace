---
description: "LibContinual exposes data access, retained-state accounting, and task-stream structure as hidden privileges in continual-learning evaluation"
source: https://arxiv.org/abs/2512.22029
captured: "2026-08-21"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 5ea8d8c15c4cdbdae7307422c9ac4e19de5d208d04a93f7f37e5c57d719546f4
ingested: "2026-08-21"
type: kb/sources/types/ingest-report.md
domains: [continual-learning, evaluation-methodology, resource-accounting, benchmark-design]
---

# Ingest: LibContinual: A Comprehensive Library towards Realistic Continual Learning

## Classification

An arXiv v1 preprint that specifies a continual-learning library, reproduces 19 methods, and reports controlled benchmark investigations of data access, retained-state cost, and task composition.
Author: Wenbin Li, Shangge Liu, Borui Kang, Yiyang Chen, KaXuan Lew, Yang Chen, Yinghuan Shi, Lei Wang, Yang Gao, and Jiebo Luo, affiliated with Nanjing University, the University of Wollongong, and the University of Rochester. They are direct implementers of the reported framework, but this recent preprint has not been independently reproduced in this KB.

## Summary

LibContinual is a modular PyTorch framework that reimplements 19 image-classification continual-learning methods across regularization, replay, optimization, representation, and architecture families. Its more important contribution for Commonplace is evaluative: it argues that mainstream results inherit three often-hidden privileges -- multi-epoch access to each task's data, incomparable amounts and forms of retained state, and semantically coherent task groupings. The paper introduces a single-pass protocol, a unified additional-memory budget over images, features, model copies, parameters, and prompts, and a category-randomized five-dataset setting. Method rankings and absolute results change substantially under these protocols, showing that a continual learner's apparent stability and plasticity are conditional on its access, resource, and stream construction.

## Connections Found

The paper is a technical basis for treating evaluation privilege as part of a learner's effective environment. Its interpretation rests on [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and on the rule that [an experiment identifies only its observed contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): LibContinual varies useful outer conditions, but its own supervised image tasks, method families, backbones, metrics, and protocol definitions stay fixed. It compares with [continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md) as a distributed-parametric resource-accounting slice rather than a whole deployed-system treatment. Most directly, it qualifies [HCL](harness-continual-learning-adaptation-beyond-model-parameters.ingest.md): finite-anchor retention is only one evaluation axis; persistent harness-state cost, deployment-evidence access, and task-stream construction also need declaration and sensitivity tests. The [agentic-adaptation survey](adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) supplies the broader component-counterfactual and dynamics-aware agenda that LibContinual partly operationalizes.

## Extractable Value

1. **Realism is a vector of declared evaluation privileges, not a benchmark label** -- Data-revisit access, retained-state allowance, and task-stream construction independently change what a continual learner can exploit. HCL already exposes retention-gate coverage; LibContinual adds three upstream conditions that should be declared before an adaptive system's result is called continual or realistic. [quick-win]
2. **Retained-state comparisons need one accounting boundary across storage forms** -- LibContinual converts buffered images, stored features, model snapshots, added parameters, and prompts into one additional-memory measure beyond the backbone. The transferable move is the common accounting boundary, not its particular byte metric: adaptive-harness evaluations should count all persistent candidate and deployed state rather than granting different methods unpriced memory under different names. [experiment]
3. **Task-stream construction can supply a shortcut that disappears under interleaving** -- On the five-dataset comparison, category randomization produces large and divergent last-accuracy changes, including -29.08 points for RanPAC, -20.72 for DualPrompt, and +23.84 for MoE-Adapter4CL. The result warrants a task-structure sensitivity test; it does not yet isolate semantic coherence as the cause. For agent and KB learning, the corresponding experiment would interleave heterogeneous change requests rather than presenting neat topic blocks. [experiment]
4. **Single-pass results can be dominated by prior representation and update-space size** -- On ImageNet-R, all training-from-scratch methods report last accuracy below 8%, while the tested pre-trained-model methods range from 62.76% to 86.59%. This is useful as a design warning: adaptation cadence and inherited representations may dominate the named continual-learning mechanism. Because architecture, pretraining, and method differ together, the table is not a causal estimate of single-pass access or pretraining alone. [deep-dive]
5. **More retained bytes are not monotonically better under the paper's accounting** -- L2P uses more than 440 MB yet is consistently outperformed by CodaPrompt using less than 4% as much, while RanPAC's TinyImageNet result moves only from 88.33% to 89.55% as reported memory grows from 16 MB to 439 MB. This supports measuring performance-cost frontiers instead of rewarding peak outcome alone, while remaining specific to the tested methods and exclusion of backbone cost. [just-a-reference]
6. **A benchmark should report a sensitivity profile, not only a final ranking** -- The three protocols expose different failure surfaces: rapid assimilation, resource efficiency, and robustness to task composition. A single endpoint accuracy conflates them; an adaptive-system evaluation should report how conclusions move as access, budget, stream order, and retention coverage change. [experiment]

## Limitations (our opinion)

The evidence is paper-only. The snapshot is an arXiv v1 preprint; the linked repository was not inspected, no code was executed, and none of the reported training or benchmark outcomes was reproduced.

The offline-access investigation does not provide a fully matched epoch-one-versus-multi-epoch intervention for each method under a common backbone and dataset. Its strongest headline comparison places training-from-scratch CNN methods against ViT- or CLIP-based methods with large pretraining histories and much smaller update spaces. The table demonstrates compound-system performance under the stated single-pass protocol, but it does not isolate whether pretraining, architecture, parameter count, optimizer, or data-revisit access caused the gap.

The unified memory measure is narrower than total system resources. It excludes the backbone's own size and pretraining cost, and it does not normalize compute, latency, bandwidth, privacy exposure, or the information value of one stored byte. Several methods expose fixed rather than continuously adjustable memory points. Converting heterogeneous retained objects to bytes improves transparency, but it does not make their access costs or behavioral effects equivalent.

Category randomization changes a bundle: semantic co-occurrence, domain mixture within tasks, class ordering, task-boundary usefulness, and possibly per-task difficulty. The paper does not quantify semantic similarity or independently vary those factors. The results therefore show sensitivity to the tested shuffled construction, not that semantic shortcuts caused each loss or gain.

Under the fixed-decomposition lens, behavior can condition on current labeled batches, task identity when the setting permits it, pretrained features, and method-specific retained images, features, model copies, parameters, or prompts. It can compose only the update operations supplied by the 19 implemented methods, through their fixed architecture- and backbone-specific hypothesis classes. Outside that effective update space remain supervised image classification, disjoint class labels, selected datasets and task partitions, class order, pretrained backbones, hyperparameters, the five-family taxonomy, last/average-accuracy metrics, and the definitions of online access and additional memory. Improvements within these compound configurations do not validate that fixed decomposition or transfer directly to open-ended agent and KB adaptation.

## Recommended Next Action

Write a note titled **“Continual-learning evaluations must declare access privileges, retained-state budget, and stream structure”** that synthesizes this paper with [HCL](harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) and the [agentic-adaptation survey](adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md), turning their combined evidence into an evaluation contract for adaptive harnesses without importing LibContinual's image-classification decomposition as a default.
