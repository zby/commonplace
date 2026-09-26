---
description: "Curated head for the context-engineering tag — getting the right knowledge into a bounded LLM context at the right time: routing, loading, scoping, context budgets, scheduling, and what to retain for later loading"
type: types/tag-readme.md
---

# Context engineering

This tag gathers work on getting the right knowledge into a bounded LLM context at the right time: routing and retrieval, loading and prompt assembly, scoping, context budgets and degradation, scheduling work across context windows, and deciding what to store so it can be loaded later. The defining note is [context engineering](../notes/definitions/context-engineering.md), which names routing, loading, scoping, and maintenance as the operational core. Members span `kb/notes/`, reference proposals for write-context assembly, and system analyses in `kb/agentic-systems/`. Nearby but different: [agent-memory](./agent-memory-README.md) covers what an agent retains across sessions and under what authority; a note belongs here when its question is how knowledge reaches a bounded call, whether or not it was retained as memory. This head is selective; use a scoped tag search for full membership.

## Core Claims

- [Context engineering](../notes/definitions/context-engineering.md) - the definition: the discipline of designing systems around bounded-context calls, with routing, loading, scoping, and maintenance as its core
- [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - why context is the scarce resource, and why per-window degradation binds before token cost
- [Design for the first-time human, except on access cost](../notes/design-for-the-first-time-human-except-on-access-cost.md) - explains why human-facing materializations and agent-facing query paths can share a source of truth while following different access modes
- [semantic sub-goals that exceed one context window become scheduling problems](../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) - explains when context limits force orchestration instead of a single larger prompt
- [stateful tools recover control by becoming hidden schedulers](../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) - shows how runtime state can relocate context control behind the tool boundary
- [A context-operation interface bounds the projections its policy can realize](../notes/context-operation-interface-bounds-context-policy.md) - separates structural projection reach from policy success within one interface
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../notes/addressability-grain-sets-a-matched-selective-read-floor.md) - isolates the retrieval-floor condition for a known question that maps to one discriminating unit on each path, while leaving fan-out, sufficiency, reliability, and net value separate
- [Opposed recompute factors do not decide documentation segmentation](../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) - why crossed savings and recurrence rankings do not order cache value, and why cache value alone does not decide whether a second content layer pays
- [A derived copy of recomputable truth must be checked or absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) - names when a recomputable value is safe to inline for context economy: only when a validator can re-derive and check it, otherwise it must stay a live read

## Methodology Activation

- [Capable agents need methodology selection](../notes/capable-agents-need-methodology-selection.md) - relevant but incompatible approaches force choosing a governing methodology, not just supplying knowledge
- [Weight-resident methodologies compress behavior in context](../notes/weight-resident-methodologies-compress-behavior-in-context.md) - a compact cue can activate a methodology already in the weights, at the cost of exact specification

## Write-Context Assembly

- [Deterministic write-context assembly](../reference/proposals/deterministic-write-context-assembly.md) - proposal: code assembles a target's fixed authoring context with closed input roles
- [Per-artifact write briefs](../reference/proposals/per-artifact-write-briefs.md) - proposal: keep an artifact-specific commission and deliver it to writers

## Related Tags

- [Agent memory](./agent-memory-README.md) - the retention side: what agents keep across sessions and how it is activated; most memory-requirements notes carry both tags
- [Computational model](./computational-model-README.md) - the bounded-call substrate context engineering operates on, including framework-owned loops and when scheduling must become explicit
- [Deploy-time learning](./deploy-time-learning-README.md) - the post-release change that context machinery helps absorb without retraining
