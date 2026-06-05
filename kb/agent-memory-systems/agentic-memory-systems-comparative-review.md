---
description: "What 129 code-grounded agent-memory reviews show on one matrix: storage predicts almost nothing, capture and activation move together except on graph stores, automatic activation ships almost entirely unverified, and curation is bimodal — 13 systems do none, 6 do all of it."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
status: current
---

# What the matrix shows across 129 agent memory systems

129 code-grounded reviews, each classified on the same axes — [storage substrate](../notes/definitions/storage-substrate.md), [lineage](../notes/definitions/lineage.md), [behavioral authority](../notes/definitions/behavioral-authority.md), and how memory [reaches the next action](../notes/knowledge-storage-does-not-imply-contextual-activation.md) — and parsed into [`systems.csv`](./systems.csv) and the [comparison table](./systems-table.md). What divides the field is not storage but activation and verification. Four surprises.

## Storage predicts nothing

Files-family substrates lead at **70%**, but read that with care: the roster was assembled largely from the llm-wiki discussions that followed Karpathy's sketch of the idea, which over-sample file-based systems, so the majority is a fact about *this collection*, not the field. The durable point is the spread. Substrate runs from [Agent-R](./reviews/agent-r.md), whose "memory" is not a store but a fine-tune baked into weights, to [supermemory](./reviews/supermemory.md), a hosted service behind an API — and it predicts almost nothing about how a system behaves. It is an operational floor, not the architectural fork it is usually treated as.

## Capture and activation are one choice — except on graphs

Whether a system learns automatically and whether it injects memory unasked turn out to be the same decision: **82%** of trace-learners push, and **70%** of pull-only systems are hand-authored. The field splits into an **automatic camp** (50% — learns from traces, pushes) and a **curated camp** (25% — authored, waits to be asked). The clean exception is graph memory: [Graphiti](./reviews/graphiti.md), [Cortex](./reviews/cortex.md), and [dense-mem](./reviews/dense-mem.md) all capture automatically yet stay strictly pull-only, because a graph is dear to build and cheap to query — so it can afford to wait to be asked rather than guess what to push.

## Automatic activation is shipped on faith

Pushing is the survey's most common capability and its least verified. **75%** of pushes are a coarse always-load, not a selection for the moment (an actual LLM relevance judgment fires in only **17%**). And just **5 of 83** pushing systems ever test that the memory they injected changed the agent's behavior — and those five ([Reflexion](./reviews/reflexion.md), [Synapptic](./reviews/synapptic.md), [KBLaM](./reviews/KBLaM.md), [auto-harness](./reviews/auto-harness.md), [Meta-Harness](./reviews/meta-harness.md)) are all systems where measuring the outcome was already the point. Everywhere else, [storage is simply assumed to imply activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

## Curation is a barbell

Capture is solved; lifecycle maintenance is not — and it is bimodal, not gradual. Of the 120 systems that write automatically, **13 do no curation at all** (pure acquisition, never touching what is already stored), while **6 run all seven operations** ([Clude](./reviews/cludebot.md), [GBrain](./reviews/gbrain.md), [LACP](./reviews/lacp.md), [Origin](./reviews/origin.md), [Stash](./reviews/stash.md), [WUPHF](./reviews/wuphf.md)); the middle is thin. The rarest is genuine `synthesize` — a *new* claim across stored entries rather than a summary of them — which stays mostly aspirational even where the matrix records the token.

## For us

Commonplace is curated-camp (authored, pull-first, files): the minority bet, strong on review and weak on scale. The data argues not for defecting to automatic capture but for *automating the curation* while keeping memory authored — sliding from the empty end of the barbell toward the full one. And faithfulness testing is the cheap edge: nearly absent across 129 systems, so checking whether a loaded note actually changed an agent's behavior would measure what almost the whole field only assumes.

Relevant Notes:

- [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds: the read-back / activation distinction the second and third findings rest on
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - see-also: why the dividing axes span storage, retrieval, and learning at once
- [trace-derived-learning-techniques-in-related-systems](./trace-derived-learning-techniques-in-related-systems.md) - see-also: the focused survey of the automatic camp this matrix quantifies
