---
description: "Inngest practitioner framing of durable agent loops as loop + skill + orchestrator, useful for the run-state and skill-persistence boundary"
source_snapshot: "the-agent-loop-architecture-2067677007140278630.md"
ingested: "2026-06-19"
type: kb/sources/types/ingest-report.md
source_type: practitioner-report
domains: [agent-orchestration, durable-execution, deploy-time-learning]
---

# Ingest: The Agent Loop Architecture

Source: [the-agent-loop-architecture-2067677007140278630.md](./the-agent-loop-architecture-2067677007140278630.md)
Captured: 2026-06-19T06:32:44.632033+00:00
From: https://x.com/djfarrelly/status/2067677007140278630

## Classification

Type: practitioner-report -- a production-oriented essay by an Inngest author arguing from implementation patterns and an internally tested project, not a formal paper or neutral survey.
Domains: agent-orchestration, durable-execution, deploy-time-learning
Author: @djfarrelly writes from the perspective of an orchestration vendor and points to Inngest/Utah as a working example, so the report has strong practitioner signal but also vendor-positioning bias.

## Summary

The source argues that production agent loops should be understood as three layers: the loop that schedules and decides, the skill as a durable multi-step workflow, and the orchestrator that checkpoints steps, retries failures, enforces concurrency, records run history, and lets agents author or revise skills that persist beyond a conversation. Its strongest contribution for this KB is not the existence of loops, which the tool-loop cluster already covers, but the operational boundary where host-language orchestration stops being enough: restarts, duplicate side effects, long-running sub-agents, review loops, and auditability force run-state, skill definitions, and diagnostic history into durable infrastructure.

## Connections Found

The companion connect report found direct evidence links into [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md), [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md), [deploy-time learning is the missing middle](../notes/deploy-time-learning-is-the-missing-middle.md), [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), and [agent runtimes decompose into scheduler context engine and execution substrate](../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md). It also found `compares-with` candidates for [GBrain as an agentic system](../agentic-systems/gbrain.md) and [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md), because both are existing inspected systems in the same loop/orchestrator/durable-skill design space. The new value is a production framing that bundles three persistence targets the KB currently treats separately: checkpointed run-state, promoted reusable skills or control strategies, and retained diagnostic evidence for future skill improvement.

## Extractable Value

1. **Durability splits into three different persistence targets** -- the source bundles step checkpointing, deployed skills, and run-history observability under "durable orchestration"; relative to the existing KB, the useful extraction is to separate within-run run-state, cross-task skill/control-strategy promotion, and diagnostic history instead of treating durability as one property. [deep-dive]
2. **Lifetime mismatch has concrete failure modes** -- duplicate notifications, repeated LLM calls, repeated sub-agent spawns, and lost position after restarts are good practitioner examples for the boundary in [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md), where operative `K` must become checkpointable external state. [quick-win]
3. **Skills as durable workflows sharpen deploy-time learning** -- the source's "skill" is executable, retryable, independently deployable infrastructure rather than only a prompt package; that usefully extends the KB's deploy-time-learning examples from readable artifacts toward mixed prose/code system-definition artifacts. [experiment]
4. **Observability becomes authority infrastructure when agents write code** -- the source's developer-view section treats step-level traces, inputs, outputs, retries, and failure hooks as the trust layer for agent-authored skills, matching [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) but in a production operations vocabulary. [quick-win]
5. **Inngest/Utah is a candidate agentic-system review target** -- the linked `github.com/inngest/utah` project may be a concrete orchestration-aware agent harness worth reviewing if Commonplace needs code-grounded evidence for durable function registration, hot reload, and sidecar-based skill authoring. [deep-dive]

## Limitations (our opinion)

The source should not be treated as neutral evidence that Inngest is the right orchestration substrate. It is vendor-authored, provides no benchmark or incident data, and its implementation claims about Utah are not code-inspected here. It also collapses several distinct persistence concerns under the word durability; the KB's existing notes on [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) and [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) are better guides for what should persist, why, and under what authority. Use this source as practitioner framing and example vocabulary, not as proof that every agent loop needs a full durable-execution platform from the start.

## Recommended Next Action

Write a seedling synthesis note at `kb/notes/durable-agent-loops-separate-run-state-strategy-and-diagnostics.md` arguing that durable agent-loop infrastructure has three separable persistence targets: checkpointed run-state for recovery, promoted skills/control strategies for cross-task reuse, and diagnostic history for later learning. Cite this source as practitioner evidence, then connect it to the existing tool-loop and deploy-time-learning notes.
