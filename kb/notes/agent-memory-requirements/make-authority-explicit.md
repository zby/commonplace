---
description: "Memory architecture must state who can read, write, promote, activate, enforce, revise, and retire memory across risk levels"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering]
status: current
---

# Make Authority Explicit

The memory system must say who or what is allowed to write, promote, activate, enforce, revise, and retire memory. The [comparative review's agency trilemma](../../agent-memory-systems/agentic-memory-systems-comparative-review.md) remains decisive: no option combines high agency, high throughput, and high curation quality without trade-offs. Agent-managed memory has task context but spends reasoning budget. External services scale but guess what matters. Humans curate well but slowly. Learned policies need strong oracles.

## Team And Multi-Agent Topology

For team or multi-agent memory, authority is also a topology problem. A system may need private notebooks, shared team knowledge, reviewer promotion, single-writer queues, scoped worktrees, channel state, and explicit local-to-team promotion. [WUPHF](../../agent-memory-systems/reviews/wuphf.md) shows a rich version of this shape with per-agent notebooks, a shared wiki, broker state, and reviewer promotion; [cq](../../agent-memory-systems/reviews/cq.md) shows a narrower local-to-team path with approval gates. The requirement is to name which memory is private, team-visible, canonical, pending, or operational state.

## Access Control, Tenancy, And Audit

Write authority is incomplete if the system cannot say who may read which memory, which tenant or account owns it, and what provenance trail proves the operation happened. [SAGE](../../agent-memory-systems/reviews/sage.md) is the strongest reviewed RBAC example, while [OpenViking](../../agent-memory-systems/reviews/openviking.md) bakes account/user/agent scope into URIs and [Hindsight](../../agent-memory-systems/reviews/hindsight.md) exposes tenancy extensions, webhooks, async operation logs, and audit logging. Not every local single-user system needs this machinery, but any shared or regulated memory system does.

## Authority Rules

- Automatic systems can capture traces and propose low-authority candidates.
- Extractors can write observations with confidence, source pointers, and candidate status.
- Context engines can activate low-risk cues under explicit budget and ranking rules.
- Human or reviewed-agent workflows should approve durable knowledge artifacts when source interpretation matters.
- Shared systems should distinguish private capture, team-visible candidates, approved canonical memory, and operational channel or session state.
- High-priority system-definition surfaces, always-loaded instructions, checks, guardrails, and executable policies need the strongest review or behavioral evaluation.
- Access-controlled systems should record tenant, account, user, agent, permission, and audit provenance for memory reads and writes.
- Retirement and relaxation should be scheduled work, not accidental decay.

## Evaluation Questions

- Does the architecture name authority for each memory operation?
- Are read, write, promotion, activation, enforcement, revision, and retirement separately governed?
- Does authority vary by risk, representational form, and consumption path?
- Are team-visible and canonical memories gated differently from private capture?
- Is audit provenance available for shared or regulated use?

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - places authority inside the memory boundary
- [The boundary of automation is the boundary of verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) - grounds why high-impact memory mutation needs stronger review
