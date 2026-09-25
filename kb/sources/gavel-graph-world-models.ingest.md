---
description: "GAVEL compares symbolic plan repair with LLM feedback under a fixed robot action model, supporting selective repair while bounding verification and online adaptation claims."
source: https://arxiv.org/abs/2609.19315
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 63adbb7ab105a3f57b70f2405c484c3d975e8533ea5c7f838481ed8fa1dcbe1e
type: kb/sources/types/ingest-report.md
domains: [llm-reliability, symbolic-planning, adaptive-execution]
learning_claims: true
---

# Ingest: GAVEL — Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning

## Classification

An empirical robotics preprint reporting a planning architecture, controlled variants, and five-seed benchmark results. Ruiyang Wang, Hao-Lun Hsu, Swarajh Mehta, Jiwoo Kim, Zhihao Dou, and Miroslav Pajic report their own system's evaluation; the retained paper does not establish peer review or independent replication.

## Summary

[GAVEL](https://arxiv.org/abs/2609.19315) uses an explicit scene graph and action model to simulate LLM plans, repair violations with known corrections, and send unresolved failures back to the LLM. Its most useful comparison holds instruction extraction, graph representation, and nine symbolic action primitives fixed while varying error handling. On 100 BEHAVIOR-1K single-task instructions, Qwen3-4B succeeds on 55.4% with feedback-only replanning, 67.7% with graph repair alone, and 88.8% with both; corresponding Qwen3-8B results are 76.4%, 76.2%, and 91.8%. The comparison supports using supplied action semantics to repair known errors, rather than establishing that this representation or division of work is generally optimal. For 500 instructions containing two to five independent tasks, retaining object-location distributions and updating task order reduces mean travel from 82.45 to 78.01 meters relative to fixed ordering with most-likely locations. Evaluation uses symbolic manipulation with geometric navigation, so verified plans remain conditional on modeled effects and extracted goals.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies bounded intervention evidence for [scheduler–LLM separation](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): direct repair improves on feedback-only replanning for the smaller planner and approximately matches it for the larger one, using one proposal instead of repeated LLM calls. Combining repair and feedback performs best for both. Because all variants inherit the same extraction and action model, this supports delegating model-derived corrections to symbolic execution within that setup, not every claim in the note's explanation of the asymmetry.

It also illustrates [preferential codification](../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md): a missing proximity precondition can induce navigation directly, leaving failures outside the repair rules for LLM interpretation. The rules are supplied, and the paper does not measure whether every removed case is more predictable than every residual case. Finally, it supplies a concrete scope boundary for [exact implementation versus requirement warrant](../notes/exact-implementation-does-not-validate-a-requirement.md): satisfying graph constraints cannot establish manipulation feasibility or correct interpretation of the user's goal.

## Learning Claims (our opinion)

GAVEL combines offline parametric learning with adaptation during execution. Two trained adapters extract objects and goals; a trained room-type predictor initializes location probabilities. During a run, observations localize objects or rule out searched rooms, and the scheduler recomputes the remaining task order. Plans can also change after explicit validation failures. The paper presents learning the environment-specific location prior from repeated observations as future work, not a demonstrated capability.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), GAVEL is outside, and condition 4 (retention) decides it. Plans and the action model are stated units (condition 1), and plans direct execution (condition 2). Simulation against the action model yields structured failures that name the violated precondition, which is criticism aimed at what a plan says (condition 3). The action model's own premises are used but never criticized or revised. Condition 4 fails: plans and schedules are revised within one instruction's execution, and neither revised plans nor their failure records are taken up on a later instruction; learning a location prior across runs is future work. Those revisions are one pass of error elimination on one problem. Changing location probabilities is observation-conditioned adaptation of numbers, not revision of a stated theory. Higher task success supports the usefulness of correction, which is a separate claim from membership.

The relevant [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) is that revised plans and schedules still use supplied object and goal categories, action semantics, restoration constraints, and room-based beliefs. The experiments test improvements within that space. They neither compare alternative representations nor show that the deployed system can repair omissions in its action model.

## Extractable Value

1. **Repair from known semantics before requesting another proposal.** The single-task variants provide a concrete comparison for the separation note: with shared extraction and symbolic action definitions, repair-only exceeds feedback-only for Qwen3-4B and approximately matches it for Qwen3-8B; combining both performs best. Reuse the mechanism where a failed precondition determines a checkable correction, without generalizing the robot representation to arbitrary KB work. [quick-win]
2. **Separate information retention from when decisions are recomputed.** Within the same independent-task benchmark, keeping distributions changes travel from 82.45 to 79.69 meters; recomputing order after completed tasks changes it further to 78.01. The combined 5.4% reduction must not be attributed entirely to online reordering. This is a reusable ablation pattern for distinguishing a richer state representation from more timely use of that state. [experiment]
3. **Keep upstream interpretation outside the guarantee of local verification.** Of 38 residual multi-task failures discussed in the paper, 21 concern object extraction. This gives the requirement-warrant note a concrete example of a bottleneck outside the repair interface, alongside manipulation geometry omitted from the verifier. [quick-win]

## Limitations (our opinion)

The SayPlan and EPoG comparisons reproduce selected mechanisms inside GAVEL's shared pipeline; they are not unchanged deployments of those systems. In particular, the EPoG-style graph-difference planner's failure on appliance-induced states does not establish that symbolic planning generally cannot handle such goals. It reflects the tested procedure generator. The repair ablation establishes neither autonomous acquisition of repair rules nor an optimal symbolic–LLM boundary.

The lightweight executor retains navigation geometry but models manipulation symbolically. Reported agreement with OmniGibson covers all 100 single-task instructions, not the full multi-task benchmark or physical robots. Goal checks also depend on extracted goal predicates. These limits matter under the [requirement-warrant distinction](../notes/exact-implementation-does-not-validate-a-requirement.md): correctness under the supplied model leaves its adequacy for the broader objective open.

Multi-task instructions contain disjoint goal-object sets, with at most five tasks. Enumerating orders exactly minimizes an approximate pairwise cost expression, not the full partially observable control problem. Distance comparisons are conditioned on successful execution, and distributional reasoning changes distance without changing the reported 92.6% success across the three GAVEL scheduling variants. Hosted-model comparisons use only a 100-instruction subset. No implementation was inspected or executed for this ingest; all outcomes are paper-reported.

## Recommended Next Action

Update [Scheduler–LLM separation exploits an error-correction asymmetry](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) with GAVEL's repair-versus-feedback comparison, retaining the shared action-model boundary and the different repair-only results for the two model sizes.
