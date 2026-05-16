---
description: "Ashpreet Bedi's ContextProvider pattern: source-scoped sub-agents collapse many raw tools into query/update surfaces to reduce tool-context pollution"
source_snapshot: "context-providers-the-missing-layer-between-agents-and-tools.md"
ingested: "2026-04-27"
type: kb/sources/types/ingest-report.md
source_type: practitioner-report
domains: [context-engineering, tool-loop, agent-orchestration]
---

# Ingest: Context providers: the missing layer between agents and tools

Source: context-providers-the-missing-layer-between-agents-and-tools.md
Captured: 2026-04-27T18:29:20.288781+00:00
From: https://x.com/ashpreetbedi/status/2048817143974613089

## Classification

Type: practitioner-report -- the author reports testing a protocol and gives implementation-shaped examples, but the source is an X article rather than a formal design spec or paper.
Domains: context-engineering, tool-loop, agent-orchestration
Author: Ashpreet Bedi; local authority is mostly practitioner evidence from building/testing this pattern, not external validation in the snapshot.

## Summary

The source argues that agents with many tools hit three walls: context pollution from tool schemas and instructions, ambiguous overlapping tool scopes, and main-agent prompts bloated with source-specific usage rules. The proposed ContextProvider layer wraps each external source, such as Slack, Drive, GitHub, or a filesystem, behind a small natural-language read/write surface: `query_<source>(question)` and `update_<source>(instruction)`. Behind that surface, a source-specific sub-agent owns the raw tools, quirks, pagination, lookup-before-write rules, and optional skills. The result is a main agent with a linear, source-level tool surface and source-scoped sub-agents that absorb operational detail.

## Connections Found

The connect pass found a tight cluster around tool-loop exposure, context scoping, and context-efficiency. The source provides **evidence** for [Subtasks that need different tools force loop exposure in agent frameworks](../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md): source-specific work needs different capability surfaces, so fresh sub-agent frames are cleaner than one giant tool set. It also supports [Bounded-context orchestration model](../notes/bounded-context-orchestration-model.md): the main agent's provider choice is a `select(K)` decision, while the provider sub-agent is the bounded `call(P)` that owns source-specific tools and rules. It also supports [Tool loop](../notes/tool-loop-index.md), [Agent context is constrained by soft degradation, not hard token limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), and [LLM context is composed without scoping](../notes/llm-context-is-composed-without-scoping.md). The most useful comparison is [Tendril](../agent-memory-systems/reviews/tendril.md): both reduce visible tool surface, but Tendril uses a stable tool-making registry while Context Providers wrap each source behind source-specific query/update sub-agents.

## Extractable Value

1. **Source-scoped tool surfaces are a distinct loop-exposure pattern** -- high reach. The source boundary, not just the task phase, can determine the right sub-agent frame because each source carries its own vocabulary, auth, tool set, and operational quirks. [deep-dive]
2. **`query_<source>` / `update_<source>` is a compact interface convention** -- high reach if it holds. It separates main-agent routing from source-agent execution and gives the parent a low-ambiguity action alphabet without requiring a custom orchestration API per source. [experiment]
3. **Skills and Context Providers solve different layers** -- the source sharpens our skill model: skills compress how to do a task, while Context Providers hide that the source-specific task exists until the main agent delegates to that provider. [quick-win]
4. **Context-provider wrappers may improve total cost despite extra hops** -- medium reach. The reported mechanism is plausible: smaller main-agent context offsets sub-agent calls, especially as source count grows. The source gives direction, not proof. [just-a-reference]
5. **MCP servers can be collapsed behind provider agents** -- medium reach. Building provider instructions from `list_tools()` at connection time is a practical pattern for avoiding stale tool docs and hiding large MCP surfaces from the main agent. [experiment]
6. **Security follows the provider boundary** -- medium reach. The GitHub example separates read-only clone access from write worktree/PR access, suggesting that query/update provider splits can carry real permission differences, not just prompt organization. [experiment]

## Limitations (our opinion)

The source should not be trusted as an evaluation result. It reports early tests, Scout workload observations, token/latency improvements, and "composition just works," but the snapshot does not include benchmark data, code, workload definition, or failure cases. Treat those as practitioner hypotheses.

The simplest account is strong: the pattern works because it reduces irrelevant and conflicting context while imposing source-level scope. That is already predicted by [agent context is constrained by soft degradation, not hard token limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) and [LLM context is composed without scoping](../notes/llm-context-is-composed-without-scoping.md). The source's surprising part is not that sub-agents help, but that the uniform read/write provider interface may be enough for many sources.

The central claim is moderately hard to vary: if source-specific tools did not have overlapping names, source quirks, or bulky instructions, the ContextProvider layer would be much less useful. But the article mostly selects examples where those conditions are obvious: Slack, Drive, CRM, GitHub, databases. It does not test small or clean tool surfaces where direct exposure may be better, although it acknowledges that boundary as open.

## Recommended Next Action

Write a note titled `Tool surfaces should be scoped by source when source-specific operational rules dominate`, connecting to [Subtasks that need different tools force loop exposure in agent frameworks](../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md), [LLM context is composed without scoping](../notes/llm-context-is-composed-without-scoping.md), [Skills are instructions plus routing and execution policy](../notes/skills-are-instructions-plus-routing-and-execution-policy.md), and [Tendril](../agent-memory-systems/reviews/tendril.md). It would argue that source boundaries are a first-class reason to spawn sub-agent frames, not merely an implementation detail of tool routing.
