---
description: "SkillLift learns textual rubrics from execution rankings to guide cheaper skill revision, supporting calibrated diagnostic feedback within task-specific search rather than general rubric reliability."
source: https://arxiv.org/abs/2609.15396
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 92482348f09cab8e54aaf29f620c9c657db4e253241f1254cd05c8f70b507baa
ingested: "2026-09-25"
type: types/ingest-report.md
domains: [agent-skills, learning-theory, evaluation, context-engineering]
learning_claims: true
---

# Ingest: SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution

## Classification

A research preprint presenting an optimization method, benchmark comparisons, component ablations, prompts, and two task trajectories. Haoxiang Kang and Ming Wen list independent-researcher and Fudan University affiliations. The evidence consists of the authors' reported experiments; this ingest does not independently reproduce them.

## Summary

SkillLift improves persistent agent skills without changing model weights by alternating skill revision with revision of the rubric that guides it. A rubric, called a receipt, contains signed, weighted binary criteria assessed from the visible skill package. Criterion hits guide cheap inner-loop edits; occasional execution rollouts rank candidates, select the champion, and expose disagreements used to revise the rubric. Across 60 WildClawBench tasks and 87 SkillsBench tasks, the paper reports better results than the tested static and evolving baselines across three model families. These are task-specific searches within fixed benchmark harnesses, execution oracles, and a package-inspection rubric interface. Within that setup, removing rubric revision lowers performance, while replacing rank alignment with score regression loses 2.7–5.3 percentage points on SkillsBench. Reported token savings concern selected threshold-crossing tasks and do not establish lower total cost across every attempted task. The useful contribution is a concrete way to keep inexpensive guidance open to execution-based correction while retaining execution outcomes for final selection.

## Quotes

No source quotes have been retained yet.

## Connections Found

SkillLift is a useful comparison for [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Criterion hits and short rationales guide revisions, whereas executed outcomes select the champion. The no-rubricator ablation retains dense feedback but lowers SkillsBench performance, supporting the importance of calibrating that guidance within this fixed package-inspection interface. It does not show that a criterion failure uniquely identifies the cause of an execution failure, or that this representation beats other diagnostic surfaces.

The paper also compares with the [pairwise-comparison test plan](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md): its ranking-versus-regression ablation tests a surrogate's supervision target through downstream optimization outcomes. It does not compare pairwise LLM judge prompts with scalar judge prompts, test tournament aggregation, or establish resistance to position bias.

As a boundary case for [warranted autonomy](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), the surrogate can guide unattended search without acquiring authority to select the final skill. Selection still uses the execution oracle. Agreement on three current candidates and a cached champion is local calibration, not evidence that the rubric can safely assess unseen skills or properties absent from the oracle.

## Learning Claims (our opinion)

The retained objects are both skill packages and the criteria used to revise them. The generator can patch or replace packages, including executable code and agent-facing instructions. The rubricator receives visible package evidence, local score and rank disagreements, and criterion hits; it revises the receipt while the candidates remain frozen. Subsequent search consumes those changes. The paper therefore describes adaptation of the search guidance as well as adaptation of the task procedure.

Our interpretation is that the rubric can function as an [addressable theory](../notes/definitions/addressable-theory.md) of which visible package features predict execution success. Against the [theory-builder definition](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: named criteria and skill packages are stated units, and subsequent search consumes them. Condition 3 is met as described: a disagreement between the rubric's predicted ordering and executed outcomes challenges it, and the rubricator is instructed to state an evidence-bounded explanation or acknowledge that none is visible. Rank selection alone would be trial and error. Condition 4 (iteration) is met: revised criteria and packages are kept and consumed by the next round of search. SkillLift is therefore inside the term. Each search revises one skill and one rubric for one task and reports the per-task best, so the persistence grade reached is across rounds of one run on one task; nothing is taken up on other problems. As a separate learning claim, the ablation supports the utility of the revision component within a task's search, but does not isolate formulated explanations from the rest of that component.

The paratransit example illustrates replacing inadequate checks with route-replay and capacity-audit guidance. The separate TicToc example improves from 0.00 to 1.00 and reports three successful post-stop trials while its receipt remains unchanged. The latter supports skill improvement under an adequate local rubric; it is not an instance of rubric revision. These cases keep the distinction between using retained criteria and criticizing those criteria visible.

The effective update space includes skill contents and rubric criteria, but leaves the backbone, benchmark harness, execution oracle, and visible-package scoring interface fixed. Following [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the results support improvement within those boundaries. They do not establish that binary package criteria are the best representation or that the oracle captures every intended task property. Nor do task-specific improvements establish transfer of one learned skill library to new tasks.

## Extractable Value

1. **Diagnostic guidance needs calibration as well as detail.** The no-rubricator comparison adds a bounded empirical case to the diagnostic-richness account: within SkillLift's package-scoring loop, retaining criterion-level feedback without revising its alignment yields worse outcomes. This supports checking guidance against independent execution evidence; it does not establish a universal advantage for rubrics over traces or other representations. [quick-win]
2. **Test supervision targets through the outcomes they produce.** Rank alignment beats score regression by 2.7–5.3 percentage points under the reported identical oracle budget, with the rubric interface and task-specific search otherwise retained. This supplies an adjacent comparison for the pairwise-test plan while preserving the distinction between a ranking objective and pairwise judge prompting. [experiment]
3. **Separate proxy calibration from final acceptance.** The method spends execution calls on current candidates, reuses the champion's prior score, and uses those outcomes both to criticize guidance and to select the next champion. This is a reusable experimental design for cheap search between expensive checks, conditional on a sufficiently informative outcome oracle. Its savings should be evaluated over all attempted tasks, including failures to reach a target. [experiment]

## Limitations (our opinion)

The evaluation reports mean per-task best evolved-skill scores over three rollout seeds. It does not establish a generally reusable library or out-of-sample rubric reliability. Repeatedly fitting the ordering of four current skills can overfit that population; reusing a noisy champion score also leaves selection error possible. The paper's claim that oracle selection prevents a misaligned rubric from corrupting final output is too strong: poor guidance can restrict the candidates reached, and the oracle itself can be incomplete or noisy.

The cost comparison includes framework and rollout tokens, but excludes tasks already above the target and tasks that never reach it. Table 7 reports baseline-to-SkillLift ratios of 2.13–2.74, implying approximately 53–64% savings for those reported crossings. This is narrower than a general 40–70% saving over all tasks. Baselines receive twice SkillLift's default token budget, but SkillOpt also uses reduced settings and disables several components. The result compares these configurations, not every implementation of the baseline methods.

The seed ablation changes initial population size as well as seed conditions, so its loss cannot be attributed to seed quality alone. Cross-benchmark differences also change harnesses, task distributions, and oracle characteristics; larger gains on deterministic tasks are consistent with better oracle guidance but do not isolate oracle quality as the cause.

The method description allows removing criteria, while the appendix rubricator forbids removing positive criteria and biases revision toward strengthening them. That inconsistency matters to the claimed capacity to correct a bad criterion. The paratransit narrative also calls its final 1.0 a verifier score, whereas the TicToc appendix explicitly identifies execution-based rewards and post-stop trials. The two case endpoints should not be treated as equally clear outcome evidence. No implementation was inspected or executed for this ingest, so these specification ambiguities remain unresolved.

## Recommended Next Action

Update [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) with the bounded no-rubricator comparison, explaining why detailed guidance can still misdirect search when its criteria are not calibrated against execution outcomes.
