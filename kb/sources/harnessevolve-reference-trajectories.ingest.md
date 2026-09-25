---
description: "HarnessEvolve adds answer-conditioned reference trajectories to harness diagnosis; its ablation supports diagnostic access within a fixed optimization and gating procedure."
source: https://arxiv.org/abs/2609.00829
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 77ff329f0488883d7870efffabb8f27b968b995309515c8a32135933aed2b1cd
type: kb/sources/types/ingest-report.md
domains: [agent-harnesses, learning-theory, evaluation]
learning_claims: true
---

# Ingest: HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution

## Classification

A research preprint with a specified optimization procedure, five benchmark evaluations, cross-framework skill transfer, and component ablations. Wen Jiang and colleagues are affiliated with Huawei's ICT AI Competence Center; two evaluated datasets and one execution framework are in-house. This is the authors' empirical account of their system, without independent replication in the retained source.

## Summary

[HarnessEvolve](https://arxiv.org/abs/2609.00829) optimizes a frozen-model execution agent's prompts, skills, tools, and execution logic through separate evaluation, diagnosis, and gating modules. It first generates successful reference trajectories with the training answers supplied, checks them with an evaluation model, and compares failed runs against accepted references to propose repairs. It clusters error causes, checks edits for answer leakage and excess examples, and tests candidates on the current and two recent batches before selecting an archived snapshot by validation accuracy. The most useful comparison for Commonplace is its CloudCoreNetwork-QA ablation with domain-tuned Qwen3.6-27B: removing reference comparison lowers reported accuracy from 86.9% to 57.8% within the same harness optimization procedure. This supports the supplied diagnostic treatment in that setup; it does not establish that the first differing action is the true cause of failure. Overall results favor HarnessEvolve across five datasets, but comparisons with baselines also vary editable harness scope. The optimizer's reference construction, diagnosis rules, judges, and acceptance procedure remain supplied design choices.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper adds bounded empirical support to [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). In its one-domain reference-removal ablation, the proposer loses an answer-conditioned successful execution while retaining failed trajectories; reported accuracy falls by 29.1 percentage points. This extends the note's evidence beyond richer inspection of existing failures to generating an additional diagnostic reference. The result concerns that whole treatment, including reference verification and comparison, rather than proving its first-divergence explanation. Candidate selection remains a separate function performed by the gates and validation selection.

The source also illustrates the boundary in [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Broad execution-harness editability does not expose the reference generator, diagnosis priorities, judge criteria, replay window, or stopping rules to optimization. Successful harness changes therefore show improvement under those choices, without comparing their alternatives or showing that a fixed choice is mistaken.

## Learning Claims (our opinion)

The paper's learning mechanism retains changes in executable and natural-language harness artifacts while leaving model weights frozen during evolution. Failed task execution supplies criticism; reference comparison supplies a proposed cause; clustered causes guide candidate edits; and quality checks, replay, and validation selection decide what persists. The retained reference cache supplies diagnostic evidence, while accepted harness snapshots change subsequent execution. These are different roles for persistent state.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: candidate instructions and programs state ways to perform tasks, and accepted revisions govern later execution. Condition 3 is met as described: a failed execution compared with a reference yields a stated cause, and that diagnosis aims the edit at what an instruction or tool says; gates and validation then select. Condition 4 is met within a run: accepted harness snapshots are the starting point of later batches, so each diagnosis-driven edit is a new conjecture re-tested by replay and validation. HarnessEvolve is therefore a theory builder at the grade of rounds within one run. Nothing persists beyond the run: each run optimizes one harness for one dataset, and test-set use and cross-framework transfer reuse the frozen product, which ends the builder. As a separate learning claim, the reported test gains support improved task capacity for the compound procedure. The paper does not trace a particular diagnosis through a particular edit and a discriminating test well enough to establish that diagnosis as the cause of a gain.

[Addressable theory](../notes/definitions/addressable-theory.md) helps distinguish a candidate repair location from a proved cause. A first divergent action can direct attention to a tool argument or instruction that can be revised separately. It need not be the erroneous action: two valid plans can diverge early, and answer access can produce a successful path unavailable to ordinary execution. HarnessEvolve's ablation strengthens the case for supplying diagnostic comparisons; it leaves open whether first-divergence localization, richer successful examples, or another part of reference access explains their benefit. It supplies no reason to revise the theory-builder definition or to treat the optimizer's fixed diagnosis scheme as learned knowledge.

## Extractable Value

1. **A distinct diagnostic-access intervention.** The 86.9% versus 57.8% result adds answer-conditioned reference comparison to the evidence behind diagnostic richness. Retain it as a one-domain, one-model ablation within a fixed optimization procedure, with reference verification included in the treatment. It does not show that more context always helps or that reference matching identifies a unique cause. [quick-win]
2. **Cause grouping as a separately varied proposal input.** Removing error clustering lowers reported accuracy to 68.6% in the same ablation setting. The method groups diagnoses by cause and preserves singleton groups. The comparison supports the grouping stage as a whole; it does not separately test singleton preservation or show that the inferred causes are correct. This is a useful candidate treatment for comparing repair proposals formed from individual failures with those formed from grouped failures. [experiment]
3. **An explicit, limited retention rule.** Current-batch acceptance uses a zero improvement margin, while replay permits degradation up to 2.5 percentage points on each of two recent batches. Validation then selects among archived snapshots. These details offer a reusable distinction between admitting a candidate locally and selecting a retained incumbent, while showing why neither operation guarantees global non-regression. [just-a-reference]

## Limitations (our opinion)

The strongest mechanistic result is the reference-removal ablation, not the overall baseline ranking. GEPA, ACE, and SkillOpt have narrower editable surfaces than HarnessEvolve. The paper does not report matched search cost, repeated-run uncertainty, or complete split counts. Its ablations use only CloudCoreNetwork-QA with domain-tuned Qwen3.6-27B, so their effect sizes should not be carried directly to other models, tasks, or KB revision workflows. Transferring optimized skills across frameworks on the same datasets' test sets supports framework portability, not cross-domain transfer by itself.

Reference reliability rests on a model judging answer-conditioned trajectories. There is no reported independent calibration of those judgments, diagnosis accuracy, or earliest-divergence attribution. A simpler account of the reference benefit is that successful demonstrations help propose repairs, even when their causal interpretation is wrong. Separating the execution, optimization, and judging modules limits direct self-evaluation coupling; it does not establish that their evaluations cannot be gamed.

The quality-gate ablation reports 80.1% accuracy after removing leakage and prompt-bloat filtering. That compound removal does not distinguish the two checks or independently demonstrate reduced shortcut learning. Its prose describes accepting all candidates without those filters, leaving the precise interaction with the performance gate insufficiently clear. No separate performance-gate ablation establishes how much that gate contributes.

The configured performance gate permits ties and bounded recent-batch regression. It does not guarantee improvement on each accepted update or preservation across all earlier tasks. A rising maximum in the snapshot archive follows from retaining candidates; repeated selection on validation data is not independent generalization evidence. The final test is separate, but uncertainty around its reported results is absent. No implementation was inspected or executed for this ingest, and the text capture does not preserve the depicted code edits in Figure 3 as readable examples.

## Recommended Next Action

Update [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) with the reference-access ablation as a bounded third diagnostic comparison, keeping the one-domain setup and the distinction between useful references and validated causal localization beside the result.
