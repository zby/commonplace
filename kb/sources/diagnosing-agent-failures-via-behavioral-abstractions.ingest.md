---
description: "AgentScope finds that structured trajectory abstractions and mode-specific neural checks improve agent-failure diagnosis, but the evaluated intervention is bundled."
source: https://arxiv.org/abs/2609.02371
captured: "2026-09-09"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: a0158b5f9fdc06de1123e9b1204bec27337b0a9a0e7ecc4308c04b7f4e071d69
ingested: "2026-09-09"
type: kb/sources/types/ingest-report.md
domains: [agent-failure-diagnosis, trajectory-evaluation, neuro-symbolic-methods, llm-as-judge]
---

# Ingest: Diagnosing Agent Failures via Behavioral Abstractions

## Classification

This arXiv preprint is a scientific paper: it defines a diagnosis method, introduces the AgentErrata benchmark, and evaluates failure localization and attribution against two LLM-judge baselines.
Author: Researchers affiliated with Tsinghua University, Microsoft Research, Microsoft, and the University of Illinois Urbana-Champaign; the paper reports both a public benchmark and an author-created, manually verified fault-injection dataset.

## Summary

AgentScope converts an agent trajectory into a directed Reasoning-Action Graph whose steps carry structured intent/context, reasoning/action, and signal/validation fields. It then applies LLM-evaluated checks for ten predefined failure modes, retains multiple candidate violations, and selects the failure whose downstream impact best explains the unsuccessful outcome. Across Who&When and the 303-trajectory AgentErrata dataset, this combined pipeline generally improves exact-step localization and failure-mode classification over all-at-once and prefix-based LLM judging. The result is most useful as evidence that explicit trajectory structure and staged diagnosis can outperform monolithic judgment, not as evidence for any one pipeline component or for the authors' chosen taxonomy and decisive-error rule.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is bounded empirical support for [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md): a diagnosis pipeline with structured step histories, localized checks, retained candidates, and explicit selection outperforms raw-trajectory judges. Its role is evidence for that compound diagnostic treatment, because the experiment does not vary ReAG construction, intermediate representations, neural checks, candidate retention, or decisive selection independently. It also complements [Evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md): the authors first turn an empirically developed failure taxonomy into explicit checks and manually verify injected cases, but do not independently calibrate each neural function as an oracle.

As a counterpoint, [Agent-runtime analysis should separate scheduling, context assembly, and external state](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) shows that AgentScope's reasoning, control-flow, and action labels describe observed behavior rather than identify the runtime responsibility that should be changed. [A failure explanation becomes search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md) marks a second boundary: AgentScope demonstrates diagnosis, not learning or repair from diagnosis. Its use of “invariant” should also be distinguished from the predeclared constraint and recovery semantics analyzed in [Agent Behavioral Contracts for Reliable Agents](./agent-behavioral-contracts-formal-specification-runtime.ingest.md).

## Extractable Value

1. **Structured diagnosis as a compound intervention** -- AgentScope supplies benchmark evidence that graph reconstruction, semantic step fields, mode-specific checks, candidate retention, and global selection can jointly outperform monolithic or prefix-local LLM judging. This supports richer diagnostic evidence while preserving the bundled-treatment qualification. [deep-dive]
2. **Failure target choice is part of the evaluation contract** -- Who&When usually labels the first mistake, whereas AgentScope selects the failure with the greatest downstream impact. Their disagreements show that “root cause” must be operationalized before exact-step accuracy can be interpreted. [quick-win]
3. **Behavioral category is not repair ownership** -- The ten-mode taxonomy can localize and name a symptom in a trajectory, but labels such as Wrong Context and Execution Failure do not determine whether scheduling, context assembly, or an external service owns the correction. [quick-win]
4. **The diagnosis space is fixed by the decomposition** -- Available evidence includes instrumented history, task context, tool interactions, and LLM-derived semantic fields; available operations are fixed neural checks plus a single decisive-error selection. The hypothesis space can express only the supplied failure modes and selection target, so performance inside it does not validate the ReAG partition, taxonomy, or greatest-impact rule against excluded alternatives. [deep-dive]
5. **Diagnosis does not yet become adaptation** -- Candidate violations remain auditable inputs, but the evaluated system neither tests a repair nor feeds the explanation into a later branch decision. This makes the paper a useful diagnostic reference without evidence for outer-loop improvement. [just-a-reference]

## Limitations (our opinion)

The main comparison changes the representation, checking procedure, candidate policy, and final selection rule together, so it cannot attribute gains to structured trajectories or neural invariants alone. AgentErrata is author-created from 303 initially successful trajectories through taxonomy-guided injection, LLM suitability screening, and manual filtering; this controls labels but may favor the same taxonomy and omit failures that do not survive its construction process. Who&When and AgentScope use different notions of the target step, making some exact-step errors disagreements about whether onset or downstream impact counts as the root cause. The paper also does not report independent calibration for every LLM-based check, matched alternatives to the ReAG and ISR decomposition, or evidence that the ten-mode taxonomy covers failures outside the tested frameworks and benchmarks. Runtime measurements cover only 20 trajectories, and the source does not test whether its diagnoses lead to successful repairs.

## Recommended Next Action

Update [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) with AgentScope as bounded empirical evidence for a structured diagnostic bundle, explicitly preserving the component-attribution and fixed-decomposition limits.
