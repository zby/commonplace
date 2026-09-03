---
description: "DuMateBench supports whole-system agent evaluation with real-session workflows while leaving component causes and fixed benchmark choices unresolved."
source: https://arxiv.org/html/2608.26546v1
captured: "2026-09-03"
capture: trafilatura
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 8c431ed5041deaebfc75c392d09f63e8462d68e161f5c9b94452548de077d8f7
ingested: "2026-09-03"
type: kb/sources/types/ingest-report.md
domains: [agent-evaluation, benchmark-design, agent-reliability, workflow-execution]
---

# Ingest: DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows

## Classification

This is a scientific preprint that introduces a benchmark, documents its construction and evaluation protocol, and reports comparative experiments across agent-framework and base-model configurations. Author: 15 named researchers document a multi-system study and report public code and data, but the paper also evaluates DuMate on tasks derived from DuMate's own production platform, so it is not independent evidence about that system.

## Summary

DuMateBench reconstructs 200 tasks from privacy-screened production-agent sessions, retaining pre-task user-visible history and workspace state, then evaluates five agent frameworks crossed with four base models in containers with missing dependencies, transient failures, and workspace noise. It combines deterministic requirement checks with artifact-specific LLM judging and reports that completion quality, noise robustness, latency, token use, and sampled failure categories vary materially with both framework and model. The benchmark is most useful as broad whole-system evidence and as a concrete design for heterogeneous-workflow evaluation; it does not isolate framework components or establish that its task reconstruction, perturbations, score aggregation, or artifact partitions are the right decomposition for other settings.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a broad empirical anchor for [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): its fully crossed framework-model results show that user-visible performance belongs to the pair, while leaving individual framework components unidentified. Its sampled trace diagnoses provide bounded evidence for [Agent-runtime analysis should separate scheduling, context assembly, and external state](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md), and its modality-specific evidence representations and rubrics are a concrete implementation of [Verification needs a typed target before it needs an oracle](../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md). As a comparison, [Same Model, Different Harness](./same-model-different-harness-different-coding-agent-results.ingest.md) offers a narrower fixed-model harness contrast, whereas DuMateBench provides broader workflow and environment coverage without component-level causal attribution.

## Extractable Value

1. **Framework-model interaction is a measured property of the deployed pair.** Across the five-by-four experiment, both framework rankings and sensitivity to model choice vary, supporting whole-system evaluation over model-only attribution. [quick-win]
2. **Real-session reconstruction supplies a reusable benchmark-construction pattern.** A cutoff separates historical context from the target request, post-cutoff artifacts are excluded, pre-cutoff workspace state is restored, and human review checks fidelity, solvability, leakage, privacy, and safety. [deep-dive]
3. **Typed artifacts drive a practical hybrid verifier.** Atomic deterministic checks cover explicit constraints, while artifact-specific judges receive modality-appropriate representations such as extracted text, formulas, rendered pages, images, or video frames; this operationalizes typed verification for heterogeneous outputs. [experiment]
4. **Trace review separates several runtime responsibility classes.** Sampled non-complete runs distinguish budget and execution closure, requirement or context grounding, environment or dependency recovery, and implementation or tool use, but the single-primary-category coding supplies diagnostic cases rather than unique causal attribution. [just-a-reference]
5. **The noise ablation measures one fixed contrast only.** Seeded workspace distractors are varied while the base model is fixed to Opus-4.8, so the observed framework-specific degradation supports claims about distractor handling in that setup, not general robustness to insufficient or unstable environments. [just-a-reference]
6. **The evaluated behavior remains inside a consequential fixed decomposition.** Agents can condition on the reconstructed instruction, visible history, workspace, tool feedback, and native framework state; compose shell, network, document, installation, fallback, and artifact-production operations; and express mappings allowed by each model-framework pair. Task selection and consolidation, available frameworks and releases, resource limits, fault schedules, artifact classes, judge inputs, and the 30/70 score weighting remain outside that effective update space, so performance gains do not validate those choices. [deep-dive]

## Limitations (our opinion)

The study draws tasks from one production platform and evaluates that platform's own DuMate framework, which limits population coverage and independence. The source does not report a component ablation within any framework, standardize decoding across runtimes, or provide a causal design for its trace-derived failure categories. Its controlled noise experiment uses only Opus-4.8, while the insufficient and unstable settings are benchmark conditions rather than matched ablations, so robustness claims should remain contrast-specific. The paper also gives inconsistent taxonomy totals: the abstract and introduction describe eight broad scenarios and 17 fine-grained categories, while the task-statistics section reports five coarse scenarios and 14 capabilities. Finally, deterministic checks and Gemini-based rubric scores are combined with a fixed 30/70 weighting; that evaluation design can rank the tested systems but does not establish that the chosen target partitions, evidence representations, judge, or weighting preserve every user-relevant distinction.

## Recommended Next Action

Update [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) to cite this ingest as bounded empirical evidence from a fully crossed framework-model benchmark, with the absence of component attribution stated alongside the result.
