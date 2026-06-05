---
description: "What 129 code-grounded agent-memory reviews show on one matrix: files/repo storage leads at 86/129 but predicts little by itself, trace-derived capture and push read-back travel together, push is usually coarse and rarely behavior-tested, and full lifecycle curation is rare."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
status: current
---

# What the matrix shows across 129 agent memory systems

Across 129 code-grounded reviews, each system is classified on the same axes: [storage substrate](../notes/definitions/storage-substrate.md) (where memory lives), [lineage](../notes/definitions/lineage.md) (how retained state was derived), [behavioral authority](../notes/definitions/behavioral-authority.md) (what force memory has), and how memory [reaches the next action](../notes/knowledge-storage-does-not-imply-contextual-activation.md). The classifications live in [`systems.csv`](./systems.csv) and the [comparison table](./systems-table.md). Read together, they show that what divides the collection is less the storage substrate than how memory is activated and verified. Four findings stand out.

## Storage predicts little by itself

Files-family substrates — plain `files` plus `repo` — lead at **86 of 129 systems (67%)**, but that number needs care. The roster was assembled largely from the llm-wiki discussions that followed Karpathy's sketch of the idea, and those over-sample file-based systems, so the majority is a fact about *this collection*, not the field. The durable point is the spread. Substrate runs from [Agent-R](./reviews/agent-r.md), a checkpoint-learning system whose "memory" is fine-tuned weights, to [supermemory](./reviews/supermemory.md), a hosted memory API — and across that range, substrate alone says little about whether memory is authored, trace-derived, pushed, pulled, enforced, or behavior-tested. It is an operational floor, not the architectural fork it is usually treated as.

## Capture and push usually travel together

Whether a system learns automatically and whether it injects memory unasked turn out to be tightly coupled: **65 of 79 trace-derived systems (82%)** push memory, and **32 of 46 pull-only systems (70%)** are not trace-derived. So the collection splits into two camps — an **automatic camp** (65 of 129 — learns from traces and pushes) and a **curated pull-only camp** (32 of 129 — does not mine traces and waits to be asked).

The instructive exception is not graph storage in general but one visible pull-only graph pattern. [Graphiti](./reviews/graphiti.md), [Cortex](./reviews/cortex.md), and [dense-mem](./reviews/dense-mem.md) — three graph-memory systems — all capture automatically yet stay strictly pull-only. A graph is expensive to build and cheap to query, so they can afford to wait for an explicit lookup rather than guess what to push. Other graph-backed systems do push, which narrows the lesson: automatic capture does not force automatic activation when the retained structure has a strong query interface.

## Automatic activation is shipped on faith

Pushing is the survey's most common capability and its least verified. Of the **83** systems that push memory, **62 (75%)** use a coarse always-load, session-start, or generic recall path rather than selecting for the current instance, and an LLM relevance judgment appears in only **14 of 83 (17%)**. Scarcer still: just **5 of 83** pushing systems test whether injected memory actually changed behavior — the evaluation-first systems [Reflexion](./reviews/reflexion.md), [Synapptic](./reviews/synapptic.md), [KBLaM](./reviews/KBLaM.md), [auto-harness](./reviews/auto-harness.md), and [Meta-Harness](./reviews/meta-harness.md). Everywhere else, [storage is simply assumed to imply activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

## Full lifecycle curation is rare

Capture is common; lifecycle maintenance is uneven. Of the **120** systems that write automatically, **13** run no curation operation at all — pure acquisition, never touching what is already stored — while only **6** run all seven tracked operations: the full-lifecycle systems [Clude](./reviews/cludebot.md), [GBrain](./reviews/gbrain.md), [LACP](./reviews/lacp.md), [Origin](./reviews/origin.md), [Stash](./reviews/stash.md), and [WUPHF](./reviews/wuphf.md). Most systems sit between those endpoints, so the pattern is not a clean barbell but partial maintenance: promotion, evolution, consolidation, deduplication, and `synthesize` flags — attempts to derive new material from stored entries — appear often enough, while decay is much rarer. The hard part is not writing memory; it is giving stored memory a complete lifecycle.

## For us

Commonplace sits in the curated pull-only camp: authored, files-family, review-heavy, and weak on scale. The data argues not for defecting to automatic capture but for automating lifecycle curation while keeping durable memory authored. Faithfulness testing is the cheap edge: nearly absent across 129 systems, so checking whether a loaded note actually changed an agent's behavior would measure what almost the whole field only assumes.

Relevant Notes:

- [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds: the read-back / activation distinction the second and third findings rest on
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - see-also: why the dividing axes span storage, retrieval, and learning at once
- [trace-derived-learning-techniques-in-related-systems](./trace-derived-learning-techniques-in-related-systems.md) - see-also: the focused survey of the automatic camp this matrix quantifies
