---
description: "Scientific preprint reporting task-conditioned executable harness generation, repair, and streaming retention under a fixed four-module protocol"
source: https://arxiv.org/abs/2608.25593
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: b1a3b32b1c449109499478f200c62f8c485d54330dd8580b7702bde4ff405b92
ingested: "2026-08-31"
type: kb/sources/types/ingest-report.md
domains: [harness-engineering, deploy-time-learning, evaluation, agentic-systems]
---

# Ingest: JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution

## Classification

An arXiv scientific preprint that specifies a trained meta-agent, formalizes its protocol and training objectives, and reports same-backbone benchmark comparisons, a static-versus-streaming evaluation, and qualitative generated-harness cases. Author: a 16-person LV-NUS Lab team led by Guibin Zhang, with Wangchunshu Zhou and Shuicheng Yan listed as corresponding authors; the captured evidence is the research team's arXiv v1 report rather than independent replication.

## Summary

JIT-Agent is a Qwen3.6-27B-based meta-agent that receives a task, a fixed harness protocol, an available capability registry, and retrieved prior harnesses, then emits executable task-specific memory, planning, action, and capability-orchestration modules; separate training stages teach bounded repair and frontier-seeking proposals, while an optional streaming mode retains useful harnesses for later tasks. The authors report improvements in all 18 matched backbone–benchmark comparisons in their main evaluation and all 24 ReAct comparisons across six model variants, plus the lowest reported token use and API cost in all six controlled fixed-harness comparisons. For Commonplace, this is useful evidence that the deployed model–harness pair is a learning and evaluation unit, but it is not evidence that the paper's four-module decomposition is the right general harness boundary.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper's compact role is technical evidence for [the deployed system, not the model alone, as the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): its matched comparisons hold the backbone fixed while replacing the harness. Its static sampling and streaming bank also instantiate [search, reject-capable evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). The bank retains reusable harness strategies and their task, reward, latency, and cost records across tasks rather than carrying the current rollout into the next one, providing a narrow empirical case for [separating orchestration-strategy persistence from run-state persistence](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md).

[Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) supplies the necessary limit. The generator can condition on the task, protocol, capability registry, retrieved harness examples, compiler and runtime diagnostics, and reward, latency, and cost histories; it can compose protocol-compliant implementations of the four modules and short repair patches, expressing mappings from those inputs to executable harness code. The four-module partition and dependency order, shared kernel, interfaces and lifecycle, supplied capabilities, validator, frozen executor, benchmark definitions, two-round repair bound, and archive objective remain outside that update space. The results therefore support improvement within this compound configuration, not the fixed decomposition itself. Compared with [Meta-Harness](./meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md), JIT-Agent moves task-level harness choice from repeated ahead-of-time artifact search into a trained instance-time generator, while both leave consequential meta-level structure fixed.

## Extractable Value

1. **Same-backbone intervention evidence for the model–harness pair.** Improvements across every reported matched pair make the paper a broad empirical example of behavior changing through the harness while model weights stay fixed; the evidence supports the compound JIT treatment, not any individual module. [quick-win]
2. **A distinction between selection time and update-space breadth.** Generating a harness for each task changes when object-level structure is chosen, but does not make the protocol, capability supply, evaluator, or retention rule just-in-time; this sharpens an otherwise ambiguous AOT-versus-JIT taxonomy. [quick-win]
3. **A complete proposal-selection loop over executable artifacts.** Static mode samples and selects candidates, while streaming mode evaluates reward, latency, and cost and makes frontier-preserving harnesses available to later tasks. [just-a-reference]
4. **Structured failures as repair supervision.** Compiler errors, interface mismatches, tool-call failures, and runtime exceptions become inputs to bounded patch generation, furnishing a concrete diagnostic-feedback mechanism even though the paper does not ablate diagnostic richness. [just-a-reference]
5. **Model–harness evaluation should report efficiency beside task quality.** The controlled tables pair performance with token use and API cost under a fixed backbone, offering a reusable evaluation shape; the source does not make clear whether generator and training costs are included. [deep-dive]
6. **Task-shaped state is visible at the representation level.** Generated examples use dependency graphs, evidence matrices, typed stores, phase registers, selective context views, and transactional repair, making the claimed adaptation more concrete than prompt variation alone; these cases remain qualitative illustrations rather than causal tests. [just-a-reference]

## Limitations (our opinion)

The intervention changes a whole generated harness, its selection procedure, and sometimes its retained bank at once. Same-backbone comparisons therefore identify the effect of that bundled treatment, not memory, planning, action, capability orchestration, repair, or candidate selection separately. The static-versus-streaming comparison varies cross-task bank use, but only across three reported streams; it does not establish which retained information produces the gain. Most importantly, no experiment varies the four-module protocol or compares it with another decomposition, so improvement inside the admitted harness space cannot validate choices fixed outside it.

The captured paper is an arXiv v1 report from the system's authors. It provides no independent replication, uncertainty intervals, or statistical significance tests for the headline benchmark differences. The reported API-cost comparisons do not clearly account for training and harness-generation overhead, and the snapshot alone does not establish configuration parity across mature runtime baselines. These gaps limit the cost-performance and generality claims even though the within-backbone direction is consistent across the reported tasks.

## Recommended Next Action

Write a note titled **When harness structure is chosen is separate from what remains fixed** that uses JIT-Agent and [Meta-Harness](./meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) to distinguish instance-time harness selection from the protocol, evidence, evaluator, and retention choices outside the effective update space.
