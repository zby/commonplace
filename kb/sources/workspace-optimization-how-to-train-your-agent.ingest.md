---
description: "DreamTeam adapts a fixed-model agent by revising typed code and role context from prediction failures, but does not isolate the value of its fixed workspace decomposition."
source: https://arxiv.org/abs/2605.09650
captured: "2026-08-30"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d69a9c2cdba8919ab1feaf95c19b60c93c7718a36d459b364978578b676130ae
ingested: "2026-08-30"
type: kb/sources/types/ingest-report.md
domains: [deploy-time-learning, agent-memory, world-models, multi-agent-systems]
---

# Ingest: Workspace Optimization: How to Train Your Agent

## Classification

This is a scientific preprint that proposes a learning framework, implements it in a multi-agent system, and evaluates the compound system on the 25 public ARC-AGI-3 games. The retained source is arXiv version 1 and does not report peer review or venue acceptance.
Author: Five NVIDIA researchers, including one with a joint Technion affiliation, provide extensive architecture, algorithm, and experiment details plus a public scorecard for one run; their institutional role also gives them an interest in establishing the proposed framework.

## Summary

The paper defines *workspace optimization* as adapting a frozen-model agent by revising the natural-language and symbolic artifacts around model calls. Its DreamTeam implementation assigns observation, dynamics, strategy, probing, critique, and action selection to six owned surfaces; each action commits a prediction, later differences route feedback to an owner, and recent transitions are replayed after executable edits. On the 25-game ARC-AGI-3 public set, the reported two-run mean reaches 38.36% RHAE versus 36.08% for a protocol-matched single Symbolica run while using 31% fewer environment actions per game. The paper is useful as a detailed design and bounded demonstration of within-episode artifact adaptation, but its benchmark comparison does not isolate which workspace mechanisms caused the gain.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source's strongest role in the current KB is as a technical basis and bounded empirical case for [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md): a fixed model jointly revises natural-language role state and symbolic programs inside an explicit replay neighborhood. Its typed prediction diffs, peer audits, error ledger, and historical transitions are evidence for [diagnostic richness as a constraint on outer-loop learning](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). It is also a counterpoint to [governing behaviour-changing writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md), because executable patches enter live state after parse and load checks while replay failures remain feedback for later repair rather than a reject-capable admission gate or rollback. Finally, it limits rather than establishes [persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md): DreamTeam retains changes across steps and levels of a game run, but the experiment does not show selected changes surviving into later sessions.

## Extractable Value

1. **Separate failure localization from repair admission.** DreamTeam localizes failures through direct typed ownership, while related systems use backward textual propagation or model-mediated diagnosis; independently, systems range from live adoption with replay feedback to generated-test rollback and held-out gates. This two-axis synthesis is not yet captured as a KB claim. [quick-win]
2. **Treat a pre-action prediction as an addressable commitment.** Requiring an owned interface to predict before acting turns the next observation into component-specific evidence and avoids reconstructing responsibility from an unstructured multi-agent trace. This is a concrete mechanism connecting diagnostic richness to localized artifact repair. [deep-dive]
3. **Inventory the effective update space before crediting the learning method.** DreamTeam can use grids, action and reward traces, encoded histories, prediction and render differences, peer feedback, logs, and replay ledgers; it can compose actions, probes, policies, and edits to owned code and text. Those choices leave consequential architecture outside the update space, so the measured improvement supports the compound system rather than the fixed partition. [deep-dive]
4. **Distinguish replay feedback from regression-gated admission.** The harness parses and reloads code, then surfaces replay deltas without automatically rejecting or rolling back a harmful patch. This supplies an operational example of why diagnostic evaluation and write governance are separate mechanisms. [quick-win]
5. **Keep the empirical result as context-bound design evidence.** The 38.36% RHAE mean and action-efficiency advantage show that the compound architecture can work on this benchmark, but the small public set, unmatched run completion, and absence of mechanism ablations make the figures unsuitable as general evidence that typed workspace optimization is superior. [just-a-reference]

## Limitations (our opinion)

The empirical comparison is too narrow to identify the cause of the gain. It covers 25 public games and two DreamTeam runs, one of which an operator stopped while 18 games were still in progress; its partial scores enter the reported mean, while the Symbolica comparator is one published run. Provider latency, model versions, benchmark revisions, and a high per-step call and token budget add uncontrolled differences. The paper reports no role, ownership, replay, context, seed, or workspace-form ablation, so it cannot attribute the result to workspace optimization as a framework rather than to the full engineered harness.

The effective update space is broad but still fixed in consequential ways. Behavior can condition on current grids, encoded observation and hidden-state histories, actions, rewards, committed predictions, field and pixel differences, peer feedback, role logs, and a bounded replay ledger. The learner can compose environment actions and policies and can revise owned Python render, dynamics, and strategy functions, schema fields, hypotheses, probes, and text context. However, the base-model weights, environment action interface, six-role ownership partition, named program exports, scheduling and context assembly, validation semantics, replay selectors and metrics, and live-adoption policy remain outside that space. As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within these choices shows that the compound configuration was sufficient here; it does not establish that the fixed decomposition preserved every needed distinction or that another partition would not work better.

The demonstrated persistence is within a game run, not across deployment sessions, and regression replay is diagnostic rather than reject-capable. A patch may therefore enter behavior, break older transitions, and remain live until a later repair. The ARC-AGI-3 setting also rewards rapid construction of a compact executable world model from a small action vocabulary; the source does not test open-ended software, knowledge work, longer-lived KB maintenance, or settings where predictions cannot be assigned to one typed owner.

## Recommended Next Action

Write a note titled **Readable-artifact learners separate failure localization from repair admission**, using DreamTeam as the direct-ownership/live-replay case and the connected Symbolic Learning, Memento-Skills, Harness Continual Learning, and Recuris ingests as contrasts.
