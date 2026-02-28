---
source_snapshot: spacedriveapp-spacebot-ai-agent.md
ingested: 2026-02-23
type: tool-announcement
domains: [agent-architecture, multi-agent, concurrency, memory-systems]
---

# Ingest: Spacebot — AI Agent for Teams and Communities

Source: spacedriveapp-spacebot-ai-agent.md
Captured: 2026-02-23
From: https://github.com/spacedriveapp/spacebot

## Classification

Type: **tool-announcement** — This is a GitHub repository README presenting a new agent framework. It describes architecture, capabilities, and deployment, but does not report on building experience or argue a theoretical position.

Domains: agent-architecture, multi-agent, concurrency, memory-systems

Author: Spacedrive (the team behind the Spacedrive file manager). They are building Spacebot as their AI agent infrastructure. The project has 1.2k stars and is written in Rust, suggesting serious engineering investment. The FSL-1.1-ALv2 license indicates commercial backing with eventual open-source transition.

## Summary

Spacebot is a concurrent AI agent framework built in Rust, designed for multi-user environments (Discord, Slack, Telegram, etc.). Its central architectural claim is that agent systems should never block: conversation, thinking, task execution, context management, and memory synthesis all run as separate concurrent processes. The five process types (channels, branches, workers, compactor, cortex) decompose what most agent frameworks handle in a single sequential loop into parallel concerns. The memory system uses typed categories with graph edges and hybrid vector/full-text retrieval. Model routing uses a four-level system (process-type defaults, task-type overrides, complexity scoring, fallback chains) to select appropriate models per call. The framework supports MCP integration and a skills registry for extensibility.

## Connections Found

The source connects to four areas of the existing knowledge base (3 strong, 5 moderate connections):

**Multi-agent architecture (strong):** Spacebot's "branches" (independent thinking forks inheriting channel context) are a production implementation of the forking pattern [voooooogel predicts will survive](../notes/research/voooooogel-multi-agent-future.md) stronger models. But Spacebot's five-process-type hierarchy is exactly the "hand-crafted hierarchy" voooooogel argues will be dissolved — the tension is instructive. Spacebot [hard-codes its worker taxonomy](../notes/dynamic-agents-runtime-design.md) (shell, file, browser, coding) while llm-do lets the taxonomy emerge at runtime via `agent_create`/`agent_call` — opposite design bets for the same problem. The branch-as-fork pattern also provides evidence for the [subagent onboarding protocol](../notes/subagent-onboarding-protocol.md) — implicit context inheritance replaces explicit Q&A, and Spacebot's "Batch Onboarding" maps directly to the note's fork pattern section.

**Runtime design (moderate):** Both Spacebot and llm-do build runtime infrastructure on top of raw LLM calls, but optimize for orthogonal concerns. Spacebot's contribution is concurrency (conversation never blocks); llm-do's is composition (unified tool/agent namespace, progressive stabilization). The [llm-do vs PydanticAI runtime](../notes/llm-do-vs-pydanticai-runtime.md) comparison gains a third reference point, and Spacebot's concurrent processes exemplify the intra-run interference patterns in the [toolset state spectrum](../notes/toolset-state-spectrum-from-stateless-to-transactional.md).

**Persistent learning (moderate):** Spacebot's typed memory system (eight categories, graph edges, vector+FTS hybrid recall) contrasts with [crystallisation](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) as competing substrates for "never forgets." Spacebot's approach is opaque — you cannot diff what the system learned. Crystallisation's repo artifacts are inspectable, testable, and reviewable. Within the [three-timescale framework](../notes/deploy-time-learning-the-missing-middle.md), Spacebot's memory occupies an unnamed position between in-context (ephemeral) and crystallisation (inspectable) — structured-but-opaque persistence. The opaque substrate also directly exemplifies the problem [inspectable-substrate-not-supervision](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) identifies.

## Extractable Value

1. **Concurrency-first architecture as design pattern** — The five-process-type decomposition (channel/branch/worker/compactor/cortex) is a concrete answer to "how do you structure an agent system that never blocks." Worth studying even if we disagree with the fixed taxonomy. [just-a-reference]

2. **Compactor as separate concern** — Separating context compaction into its own monitored process that runs independently of conversation is a pattern llm-do does not have. Currently context management is implicit in PydanticAI. This could inform future context window management design. [experiment]

3. **Memory system taxonomy** — Eight typed memory categories (Fact, Preference, Decision, Identity, Event, Observation, Goal, Todo) with explicit graph edges (RelatedTo, Updates, Contradicts, CausedBy, PartOf) is a structured approach to agent memory. Worth comparing against crystallisation's approach where "memory" is versioned artifacts. [deep-dive]

4. **Model routing with complexity scoring** — Four-level model selection (process-type defaults, task-type overrides, prompt complexity scoring, fallback chains) is more sophisticated than llm-do's per-agent model selection. The complexity scoring layer in particular is novel — automatically routing simpler prompts to cheaper models. [experiment]

5. **Message coalescing** — Batching rapid-fire user messages into single LLM turns is a practical UX pattern for multi-user environments that llm-do has not considered. Less relevant for single-user CLI but potentially useful for programmatic embedding. [just-a-reference]

6. **Branch-as-fork pattern** — Branches that "inherit channel context for analysis" are the forking pattern voooooogel describes, implemented in production. This provides evidence that the pattern works, relevant to our subagent onboarding protocol design. [just-a-reference]

7. **skills.sh as community registry** — A skills registry for installing community-built capabilities. Relates to the Agent Skills Standard Unification note and the broader question of agent capability distribution. [just-a-reference]

## Recommended Next Action

File as reference — interesting but does not change our thinking or practices. Spacebot solves a different problem (multi-user concurrent chat agents) than llm-do (single-user progressive stabilization). The most valuable insight is the compactor-as-separate-process pattern for future context management design, but this is not urgent. Concrete next steps:

1. Update [What Survives in Multi-Agent Systems](../notes/research/voooooogel-multi-agent-future.md) with a one-line reference to Spacebot as a production implementation of the branch/fork pattern and as evidence for the hierarchy-dissolution tension.
2. Consider adding Spacebot as a reference in the "Batch Onboarding (Fork Pattern)" section of [Subagent Onboarding Protocol](../notes/subagent-onboarding-protocol.md) — it validates the fork-based implicit onboarding approach at production scale.
3. The observation that Spacebot's memory system occupies an unnamed position between in-context and crystallisation may warrant a note if more examples of this pattern surface.
