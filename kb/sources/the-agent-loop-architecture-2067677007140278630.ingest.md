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

The article's "agent loop" is not the same unit as the KB's [tool loop](../notes/tool-loop-README.md), even though both terms are often collapsed under "agentic loop" in public discourse. The tool loop is the inner model/tool dispatch cycle: call the LLM, execute a requested tool, feed the result back, and repeat until the model stops. The article's loop is the outer production loop around that cycle: a scheduled or triggered decision process that invokes skills, survives restarts, checkpoints step results, controls concurrency, and records history. The source makes this distinction most clearly when it says "LLMs and tools are inside the loops"; its contribution is therefore a runtime-layer reframing, not a replacement definition for the tool loop.

## Connections Found

The companion connect report found direct evidence links into [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md), [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md), [deploy-time learning is the missing middle](../notes/deploy-time-learning-is-the-missing-middle.md), [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), and [agent runtimes decompose into scheduler context engine and execution substrate](../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md). It also found `compares-with` candidates for [GBrain as an agentic system](../agentic-systems/gbrain.md) and [Claude Code dynamic workflows](../agentic-systems/claude-code-dynamic-workflows.md), because both are existing inspected systems in the same loop/orchestrator/durable-skill design space. The new value is a production framing that bundles three persistence targets the KB currently treats separately: checkpointed run-state, promoted reusable skills or control strategies, and retained diagnostic evidence for future skill improvement.

## Extractable Value

1. **Durability splits into three different persistence targets** -- the source bundles step checkpointing, deployed skills, and run-history observability under "durable orchestration"; relative to the existing KB, the useful extraction is to separate within-run run-state, cross-task skill/control-strategy promotion, and diagnostic history instead of treating durability as one property. [deep-dive]
2. **Lifetime mismatch has concrete failure modes** -- duplicate notifications, repeated LLM calls, repeated sub-agent spawns, and lost position after restarts are good practitioner examples for the boundary in [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md), where operative `K` must become checkpointable external state. [quick-win]
3. **Skills as durable workflows sharpen deploy-time learning** -- the source's "skill" is executable, retryable, independently deployable infrastructure rather than only a prompt package; that usefully extends the KB's deploy-time-learning examples from readable artifacts toward mixed prose/code system-definition artifacts. [experiment]
4. **Observability becomes authority infrastructure when agents write code** -- the source's developer-view section treats step-level traces, inputs, outputs, retries, and failure hooks as the trust layer for agent-authored skills, matching [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) but in a production operations vocabulary. [quick-win]
5. **The source disambiguates two overloaded loop levels** -- public "agentic loop" language often names the inner ReAct/tool-use loop, but this article uses "agent loop" for a durable outer orchestration loop that contains LLM/tool cycles; this distinction should inform any future note so it does not conflate model dispatch with production scheduling. [quick-win]
6. **The article prefers loop vocabulary over recursion vocabulary** -- it treats "loops supervising loops" and sub-agent spawning as the natural next architecture rather than framing the same shape as recursive composition of tool loops; that bias is useful evidence of practitioner terminology, but the KB should keep recursion available as a neutral structural description. [quick-win]
7. **Inngest/Utah is a candidate agentic-system review target** -- the linked `github.com/inngest/utah` project may be a concrete orchestration-aware agent harness worth reviewing if Commonplace needs code-grounded evidence for durable function registration, hot reload, and sidecar-based skill authoring. [deep-dive]

## Limitations (our opinion)

The source should not be treated as neutral evidence that Inngest is the right orchestration substrate. It is vendor-authored, provides no benchmark or incident data, and its implementation claims about Utah are not code-inspected here. It also collapses several distinct persistence concerns under the word durability; the KB's existing notes on [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) and [diagnostic richness constrains outer-loop learning quality](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) are better guides for what should persist, why, and under what authority. The source's rhetoric also makes loops sound like the privileged primitive over recursion, but in the KB's computational model recursive sub-agent calls and durable orchestration loops are different structural choices rather than a simple better/worse ordering. Use this source as practitioner framing and example vocabulary, not as proof that every agent loop needs a full durable-execution platform from the start.

## Recommended Next Action

Write a seedling synthesis note at `kb/notes/durable-agent-loops-separate-run-state-strategy-and-diagnostics.md` arguing that durable agent-loop infrastructure has three separable persistence targets: checkpointed run-state for recovery, promoted skills/control strategies for cross-task reuse, and diagnostic history for later learning. Start by distinguishing the outer durable agent loop from the inner tool loop so the note does not inherit the overloaded "agentic loop" ambiguity. Cite this source as practitioner evidence, then connect it to the existing tool-loop and deploy-time-learning notes.
