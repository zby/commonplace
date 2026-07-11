---
description: "141 code-grounded reviews: files/repo storage leads; trace-derived learning and push read-back travel together; push is rarely behavior-tested; full lifecycle curation is rare."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
---

# What the matrix shows across 141 agent memory systems

Across 141 code-grounded reviews, each system is classified on the same axes: [storage substrate](../notes/definitions/storage-substrate.md) (where memory lives), [lineage](../notes/definitions/lineage.md) (how retained state was derived), [behavioral authority](../notes/definitions/behavioral-authority.md) (what force memory has), and how memory [reaches the next action](../notes/knowledge-storage-does-not-imply-contextual-activation.md). The classifications live in [`systems.csv`](./systems.csv) and the [comparison table](./systems-table.md). Read together, they show that what divides the collection is less the storage substrate than how memory is activated and verified. Four findings stand out.

## Storage predicts little by itself

Files-family substrates — plain `files` plus `repo` — lead at **98 of 141 systems (70%)**, but that number needs care. The roster was assembled largely from the llm-wiki discussions that followed Karpathy's sketch of the idea, and those over-sample file-based systems, so the majority is a fact about *this collection*, not the field. The durable point is the spread. Substrate runs from [Agent-R](./reviews/agent-r.md), a checkpoint-learning system whose "memory" is fine-tuned weights, to [supermemory](./reviews/supermemory.md), a hosted memory API — and across that range, substrate alone says little about whether memory is authored, trace-derived, pushed, pulled, enforced, or behavior-tested. It is an operational floor, not the architectural fork it is usually treated as.

## Capture and push usually travel together

Whether a system learns automatically and whether it injects memory unasked turn out to be tightly coupled: **79 of 95 trace-derived systems (83%)** push memory, and **34 of 50 pull-only systems (68%)** are not trace-derived. So the collection splits into two camps — an **automatic camp** (79 of 141 — learns from traces and pushes) and a **curated pull-only camp** (34 of 141 — does not mine traces and waits to be asked).

This finding uses the stricter `trace_derived` learning field, not the broader `lin_trace_extracted` lineage field. Lineage says that some retained artifact came from traces; learning says the system automatically distills traces into durable behavior-shaping memory. The gap is meaningful: in the file/repo slice, **70 of 98** systems retain trace-extracted artifacts, but only **60 of 98** have a qualifying trace-derived learning path. The rest keep traces as evidence, recovery state, continuity, or debugging material rather than as distilled lessons, rules, skills, validators, embeddings, adapters, rankers, or other learned memory.

The instructive exception is not graph storage in general but one visible pull-only graph pattern. [Graphiti](./reviews/graphiti.md), [Cortex](./reviews/cortex.md), and [dense-mem](./reviews/dense-mem.md) — three graph-memory systems — all capture automatically yet stay strictly pull-only. A graph is expensive to build and cheap to query, so they can afford to wait for an explicit lookup rather than guess what to push. Other graph-backed systems do push, which narrows the lesson: automatic capture does not force automatic activation when the retained structure has a strong query interface.

## Automatic activation is shipped on faith

Pushing is the survey's most common capability and its least verified. Of the **91** systems that push memory, **70 (77%)** use a coarse always-load, session-start, or generic recall path rather than selecting for the current instance, and an LLM relevance judgment appears in only **15 of 91 (16%)**. Scarcer still: just **5 of 91** pushing systems test whether injected memory actually changed behavior — the evaluation-first systems [Reflexion](./reviews/reflexion.md), [Synapptic](./reviews/synapptic.md), [KBLaM](./reviews/KBLaM.md), [auto-harness](./reviews/auto-harness.md), and [Meta-Harness](./reviews/meta-harness.md). Everywhere else, [storage is simply assumed to imply activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

## Full lifecycle curation is rare

Capture is common; lifecycle maintenance is uneven. Of the **132** systems that write automatically, **17** run no curation operation at all — pure acquisition, never touching what is already stored — while only **6** run all seven tracked operations: the full-lifecycle systems [Clude](./reviews/cludebot.md), [GBrain](./reviews/gbrain.md), [LACP](./reviews/lacp.md), [Origin](./reviews/origin.md), [Stash](./reviews/stash.md), and [WUPHF](./reviews/wuphf.md). Most systems sit between those endpoints, so the pattern is not a clean barbell but partial maintenance: promotion, evolution, consolidation, deduplication, and `synthesize` flags — attempts to derive new material from stored entries — appear often enough, while decay is much rarer. The hard part is not writing memory; it is giving stored memory a complete lifecycle.

## For us

Commonplace sits in the curated pull-only camp: authored, files-family, review-heavy, and weak on scale. The data argues not for defecting to automatic capture but for automating lifecycle curation while keeping durable memory authored. Faithfulness testing is the cheap edge: nearly absent across 141 systems, so checking whether a loaded note actually changed an agent's behavior would measure what almost the whole field only assumes.

Relevant Notes:

- [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) - grounds: the read-back / activation distinction the second and third findings rest on
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - see-also: why the dividing axes span storage, retrieval, and learning at once
- [trace-derived-learning-techniques-in-related-systems](./trace-derived-learning-techniques-in-related-systems.md) - see-also: the focused survey of the automatic camp this matrix quantifies
