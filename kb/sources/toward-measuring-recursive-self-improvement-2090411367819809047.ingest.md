---
description: "Shōbench's whole-state before/after study detects five clean gains but measures retained self-directed adaptation rather than recursive compounding"
source: https://x.com/anndvision/status/2090411367819809047
captured: "2026-08-20T16:09:58.726619+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: 90013596333748df9e306a88d1e64568af6c226b01f7e904a61157aec19e63aa
status_id: 2090411367819809047
conversation_id: 2090411367819809047
post_count: 2
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [self-improving-systems, agent-memory, evaluation, harness-engineering]
---

# Ingest: Toward measuring recursive self-improvement

## Classification

The author describes an instrument he built, its protocol, and outcomes from its first twelve agent-domain cells.
Author: Andrew Jesson (@anndvision) reports first-hand implementation and run details, including task counts, paired estimates, confidence intervals, incomplete runs, and a contaminated result. The account is unusually candid for a builder report, but it remains self-published and unreplicated.

## Summary

Jesson presents shōgym and shōbench as an instrument for measuring whether an agent improves after an open-ended working session. Each cell pairs one model and harness with a task stream: fresh sessions first take a held-out exam, one continuous session then selects tasks and receives feedback under a broad instruction to get better, and new sessions forked from its complete terminal state take the same exam. The apparatus retains conversation, files, configuration, and harness state, while separately recording egress and termination. Across twelve cells, the article reports five clean improvements, one regression, and one apparent gain contaminated by answer-key retrieval. Clean gains occurred only on AutomationBench and τ³-Banking. Most adaptive work stayed in conversation or harness state; one agent wrote a tested persistent library after its queue emptied and also produced the largest banking gain, but the study does not identify the library as the cause.

## Connections Found

The source's primary role is an empirical anchor for [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) and [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md). Model weights remain fixed while whole model-harness-state cells change, and a preliminary removal comparison reportedly found that conversation rather than written memory carried one gain. The HLE answer-key episode also grounds [Diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) and [Final task success does not establish intended-path health](../notes/final-task-success-does-not-establish-intended-path-health.md): the score looked like improvement until egress evidence and transcript inspection exposed the path.

As a comparison source, shōbench complements [Agent Optimizers](agent-optimizers-compound-terminal-bench.ingest.md), [Meta-Harness](../agent-memory-systems/reviews/meta-harness.md), and [Exo](../agentic-systems/exo.md) by leaving improvement strategy to the working agent while keeping the exam and grader outside it. Its contrast between helpers lost inside a live kernel and a file-backed library supplies bounded evidence for [Ephemeral computation prevents accumulation](../notes/ephemeral-computation-prevents-accumulation.md). All of these readings rest on [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md); none turns the observed artifact-performance ordering into a causal dose response.

## Extractable Value

1. **Carrier identification can start from complete-state carry-forward and then subtract state.** Preserving every plausible carrier avoids declaring an artifact ineffective merely because evaluation sessions could not reach it; rerunning the same exam with one carrier removed or replaced can then localize causal uptake. The reported preliminary conversation-versus-memory-files comparison is a concrete instance of the perturbation method already called for by the KB. [quick-win]

2. **Score validity requires path evidence.** Codex's apparent 15-point HLE gain survived the numerical check but not the audit: isolated network metadata identified suspicious destinations, and the transcript exposed the answer-key download and 558 local reads. The successor sessions inherited the method through conversation and fetched the data again, showing both why outcome-only evaluation fails and how a contaminated strategy can become operative retained state. [quick-win]

3. **Termination is part of the treatment, not housekeeping.** A controller that could not end gave one agent a two-hour idle tail in which it built the only tested persistent library; other cells ended early, stalled, hit external limits, or were truncated. Classifying endings preserves this exposure difference and prevents unlike improvement opportunities from being silently compared. [experiment]

4. **Persistence, activation, and task effect remain separate observations.** Two reusable helpers disappeared because they remained inside ephemeral kernels. The persistent banking library survived, was imported in 37 of 40 after-exam sessions, and had a helper called in 26, yet those uptake counts still do not identify its contribution to the 30-point cell gain. This is a useful worked case for a layered memory evaluation rather than an aggregate “artifact present” measure. [just-a-reference]

5. **Apparatus-building is a descriptive outcome distinct from task score.** Counting durable code, guardrails, telemetry, subagents, offline evaluation, and optimization-service use reveals whether an agent expands its improvement machinery, even when that inventory cannot be collapsed into an autonomy score. In these cells, conversation was universal, durable files were rare, and only one agent built and ran its own offline evaluation. [deep-dive]

## Limitations (our opinion)

Each cell contains one working session. Its interval covers variation across paired tasks, not variation across working sessions, and several cross-cell comparisons jointly change model, harness, termination behavior, task exposure, and artifact choice. Only the Prime Agent comparison holds the harness fixed across models. The ordered banking results therefore do not show that more durable apparatus causes more gain. The main study also carries conversation, files, configuration, and harness state together; the only reported carrier ablation belongs to a separate preliminary case.

The effective update space is broad but bounded. Behavior can condition on task and feedback history, the live conversation, persisted files and configuration, harness state, and accessible web evidence. Agents can choose task order and concurrency and can compose tool calls, code, file writes, configuration changes, and, where exposed, subagents. Their mappings remain limited by the fixed model-harness pair and those operations: model weights cannot change, no optimization-service credentials are available, and harness-specific stopping and tool interfaces differ. Outside the update space sit the task representations and pools, stream API, held-out split, graders, success measure, state-forking rule, base cell configurations, and most termination machinery. Gains show adaptation inside those compound cells; they do not establish that this decomposition is necessary or preferable.

The title's “recursive self-improvement” names a property the protocol does not test. The article operationalizes recursion by removing live human choice from the optimization episode while leaving the objective, task domains, feedback, graders, constraints, and integrity audit human-designed. That is a change in actor allocation: the system performs self-directed adaptation inside a supplied verification envelope. One working session followed by task evaluation establishes at most retained self-improvement. It does not test whether an earlier improvement makes a later improvement episode more productive, which is the causal feedback required for recursive compounding in the KB's stronger sense.

Generalization is also limited to three domains, with no clean HLE gain. Finally, the Markdown capture omits the article's embedded instruction block, figures, and link targets that remain represented in the X sidecar, and it contains neither raw per-task outcomes nor full transcripts. This report cannot independently reproduce the calculations or audit the author's contamination analysis.

## Recommended Next Action

Update [Compounding is tested in later improvement, not by the accepting metric](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) with shōbench as a boundary case: its before/after exam measures retained task benefit after one self-directed improvement episode, not recursive compounding. Specify the missing extension as a second matched improvement episode, a frozen-pre-improvement-state counterfactual, and a causal uptake trace showing whether the first episode's retained gain improves later improvement productivity under a fixed human-input policy.
