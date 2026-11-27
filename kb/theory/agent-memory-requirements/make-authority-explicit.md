---
description: "Memory architecture must state who can read, write, promote, activate, enforce, revise, and retire memory across risk levels"
type: types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering, warranted-autonomy, self-improving-systems, learning-theory]
---

# Make Authority Explicit

The memory system must say who or what is allowed to write, promote, activate, enforce, revise, and retire memory. The [comparative review's agency trilemma](../../agent-memory-systems/agentic-memory-systems-comparative-review.md) remains decisive: no option combines high agency, high throughput, and high curation quality without trade-offs. Agent-managed memory has task context but spends reasoning budget. External services scale but guess what matters. Humans curate well but slowly. Learned policies need strong oracles.

## Team And Multi-Agent Topology

For team or multi-agent memory, authority is also a topology problem. A system may need private notebooks, shared team knowledge, reviewer promotion, single-writer queues, scoped worktrees, channel state, and explicit local-to-team promotion. [WUPHF](../../agentic-system-analyses/retained/nex-crm--wuphf/memory.md#mem-rte-scoped-notes) copies a private note into shared storage on promotion; the private copy remains. In [cq](../../agentic-system-analyses/retained/mozilla-ai--cq/runtime.md#rt-rte-local-drain), a successful transfer deletes the local entry, but ordinary remote reads still require approval. A lesson can therefore disappear from local retrieval before the team can use it. The requirement is to name which memory is private, team-visible, canonical, pending, or operational state.

## Access Control, Tenancy, And Audit

Write authority is incomplete if the system cannot say who may read which memory, which tenant or account owns it, and what provenance trail proves the operation happened. [SAGE](../../agentic-system-analyses/retained/l33tdawg--sage/runtime.md#rt-rte-targeted-recall) checks authorization when serving targeted recall. [OpenViking](../../agentic-system-analyses/retained/volcengine--openviking/runtime.md#rt-clm-scoped-retrieval) constructs scope filters for retrieval; their effect depends on the configured backend enforcing them. [Hindsight](../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-clm-tenant-check) exposes a tenant check, but its default extension does not authenticate callers. Naming a tenant is not proof of isolation. Not every local single-user system needs this machinery, but any shared or regulated memory system does.

## Authority Rules

- Automatic systems can capture traces and propose low-authority candidates.
- Extractors can write observations with confidence, source pointers, and candidate status.
- Context engines can activate low-risk cues under explicit budget and ranking rules.
- Human or reviewed-agent workflows should approve durable [knowledge artifacts](../definitions/knowledge-artifact.md) when source interpretation matters.
- Shared systems should distinguish private capture, team-visible candidates, approved canonical memory, and operational channel or session state.
- High-priority [system-definition artifacts](../definitions/system-definition-artifact.md), always-loaded instructions, checks, guardrails, and executable policies need the strongest review or behavioral evaluation.
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
