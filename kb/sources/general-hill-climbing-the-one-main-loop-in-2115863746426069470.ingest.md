---
description: "Miessler frames AI work as intent capture, evaluation, and iteration; useful for specification repair, not evidence of universal hill-climbing or autonomous learning."
source: https://x.com/DanielMiessler/status/2115863746426069470
captured: "2026-10-30T17:18:39.820607+00:00"
capture: xdk
genre: conceptual-essay
snapshot_sha256: 25aa8841542ac959714236c72a80537a494f579ff1201b0367d5c3168959ee75
ingested: "2026-10-30"
type: types/ingest-report.md
domains: [hill-climbing, ideal-state-articulation, evaluator-revision]
status_id: 2115863746426069470
conversation_id: 2115863746426069470
post_count: 2
learning_claims: true
---

# Ingest: General Hill-Climbing: The One Main Loop in AI

## Classification

A single-author conceptual argument presented on X, with illustrative evaluator checks rather than measured outcomes. Its references to TELOS and AI harnesses do not make it a tested system report.
Author: Daniel Miessler (@DanielMiessler), presenting his own framework and advocating its general use; the captured text supplies no independent validation.

## Summary

Miessler proposes a general AI work loop: record purpose and context in TELOS, an open-source single-file framework; articulate a task's ideal state; build evaluators; execute; and revise. He argues that agents act on the captured specification rather than the intention in a person's head, making articulation a major bottleneck. His evaluator menu spans deterministic checks, model judgments, factual verification, and repeated execution, with cheap checks preceding expensive judges. A second loop revises goals and evaluators when outputs pass checks but remain unsatisfactory. This is a useful account of explicit specification and feedback, but the essay supplies no experiments establishing that articulation is today's primary limitation or that retaining only score improvements is a universal problem-solving strategy.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a conceptual comparison for the [proposal-selection improvement loop](../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md): its candidate changes and keep-better rule describe search and rejection, while reuse of accepted changes supplies retention in the proposed workflow. Repeated output refinement alone does not establish improvement of the system's own machinery. It also provides a counterpoint to [specification strategy following where understanding lives](../theory/specification-strategy-should-follow-where-understanding-lives.md). Its strong upfront-articulation advice fits understanding already available to the operator; its later concession that ideal states evolve acknowledges the need for execution-informed specification. Neither connection requires treating the essay as empirical corroboration or promoting a new general theory.

## Learning Claims (our opinion)

On the source's terms, adaptation occurs by generating work against an explicit ideal state, checking it, retaining improvements, and repairing the ideal state or evaluators when they no longer express what is wanted. The proposed system includes the people who articulate intent and judge dissatisfaction, not just the AI executing the task.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), **localized content** is explicit in the proposed purpose file, task document, and written checks, although not every goal statement is an explanatory conjecture. **Consumption** is prescribed: the AI is meant to build from the task document and use the checks to guide revision; no execution trace establishes that path in practice. **Content-directed criticism** is only partially specified: identifying an omitted criterion can criticize what a check says, but a score or preference verdict alone need not state a reason bearing on identified content. **Iteration** is explicit as a design intention, since revised outputs and checks guide the next round; it is not demonstrated by a worked sequence. The account supports within-task retention conceptually, but supplies no history showing reuse across runs or problems. Improved capacity for future action remains a separate, untested claim.

The source opens both task descriptions and evaluators to revision, so it is broader than optimization under a permanently fixed score. Nevertheless, as [learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains, progress among available candidates cannot establish the adequacy of excluded representations or operations. The essay does not specify the generator's effective update space, retained histories, or how to assess revisions to the evaluators themselves. It therefore offers a plausible human-involved adaptation pattern, not a demonstration of autonomous evaluator criticism or a reason to revise Commonplace's distinction between iteration and demonstrated learning.

## Extractable Value

1. **Separate specification capture from later discovery.** The contrast between intended outcome, written artifact, and built result is a useful source-side illustration for the existing specification-strategy note. The essay's own allowance for evolving goals limits its recommendation for exhaustive upfront capture. [just-a-reference]
2. **Use passing-but-unsatisfactory outputs to investigate evaluator coverage.** This is a concrete trigger for revisiting checks rather than endlessly optimizing the current score. It is a diagnostic prompt, not proof that an omitted check is the cause or that the replacement evaluator is valid. [quick-win]
3. **Stage evaluation by cost.** Running cheap deterministic checks before model judgments is a reusable workflow suggestion for artifact review. The source supplies a practical rule, not a measured cost or quality advantage. [just-a-reference]

## Limitations (our opinion)

The central universal framing is not supported by comparative results. The essay moves from a narrow definition of hill-climbing—small changes retained only when they score better—to a much broader feedback-and-revision loop. It does not argue that local score improvement can cross plateaus, escape local optima, or handle temporarily worse stepping stones. Its useful general feedback advice therefore does not establish its narrower search rule as universal.

The claim that articulation is the primary current limitation has no failure-frequency evidence or comparison with execution, environment, or evaluator failures. The [specification-strategy note](../theory/specification-strategy-should-follow-where-understanding-lives.md) supplies a consequential qualification: more initial dictation cannot capture understanding that only execution will reveal. Likewise, dissatisfaction with a passing output can motivate criticism, but it does not identify the faulty premise or validate a new criterion by itself. No reported tests establish judge reliability, resistance to optimizing proxies, or improved future performance.

The retained text contains an unfinished sentence in the experimentation discussion. Capture scope is not declared, so the missing continuation cannot be reconstructed or used to supply an argument about experimentation. The report establishes only the proposals visible in the captured post, not claims from the linked blog or TELOS implementation.

## Recommended Next Action

File this ingest as a source-only reference for `kb/theory/specification-strategy-should-follow-where-understanding-lives.md`, without promoting its universal hill-climbing claim.
