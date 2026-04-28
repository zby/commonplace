---
description: "Memory design needs operational policy axes (capture, derivation, activation, authority, lifecycle, evaluation) on top of artifact class, backend, and role"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, title-as-claim]
tags: [agent-memory, context-engineering, learning-theory]
status: seedling
---

# Memory design adds operational axes to artifact analysis

[Axes of artifact analysis](./axes-of-artifact-analysis.md) separates artifacts by class, backend, and role. That taxonomy prevents category mistakes like treating "files versus weights" as a single design choice. Agent memory needs those axes, but artifact identity is not enough. A memory system also needs to say how retained material is captured, transformed, activated, governed, evaluated, and retired over time.

This seedling note names those cross-cutting operational axes. Its job is not to replace the detailed memory-requirements notes, but to make those requirements comparable when a memory discussion starts from storage format, artifact class, or backend.

## Artifact axes

[Axes of artifact analysis](./axes-of-artifact-analysis.md) answers what kind of artifact exists and how a consumer reads it:

| Axis | Question | Memory example |
|---|---|---|
| Class | How is the learned result represented? | Opaque policy in weights, prose memory entry, symbolic test or schema |
| Backend | Where does the artifact live? | Repo file, SQL row, vector record, graph edge, service-owned memory object |
| Role | How does the consumer read it? | Reference knowledge, behavior-shaping instruction, or both |

These axes are necessary because memory discussions often conflate them — [agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) collects the recurring confusions, and [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md) shows backend-first comparisons missing the more consequential axes. A vector store is a backend, not an artifact class. A prompt rule is usually prose-class but behavior-shaping in role. A markdown file can have knowledge role when read as reference and system-definition role when loaded as instruction.

But artifact axes stop at the artifact boundary. They do not explain how retained material becomes future capacity.

## Operational memory axes

Operational axes describe the policies that turn retained material into usable memory:

| Axis | Question | Common choices |
|---|---|---|
| Capture policy | What enters the memory system? | Write everything, heuristic trigger, LLM curator, user-marked item, post-session mining |
| Derivation policy | How does raw material become usable? | Keep raw traces, summarize, extract facts, build graph edges, create cues, generate system-definition artifacts |
| Activation policy | How does memory reach a future bounded context? | Always injected, hook-driven retrieval, tool-driven search, on-reference loading, on-situation cue |
| Authority policy | Who decides and who can revise? | Harness, cheap model, main model, background model, user, reviewer, deterministic validator |
| Lifecycle policy | How does memory change or leave? | Supersede, invalidate, decay, redact, delete, relax enforcement, regenerate compiled views |
| Evaluation policy | What proves the memory helped? | Retrieval score, task outcome, behavior change, artifact quality, human review, ablation |

The framing is what's new, not the underlying design pressures. Each axis maps onto existing requirement notes: capture and derivation cover ingress and trace extraction; activation covers behavior-changing memory; authority covers write, promotion, enforcement, and revision rights; lifecycle covers how memory changes (decay, supersession, redaction, relaxation, temporal validity); evaluation covers downstream effects rather than storage volume. Authority and lifecycle meet at retirement: authority answers *who* may retire a memory, lifecycle answers *how* retirement happens.

## Why the split matters

The same artifact axes can produce different memory behavior. Two systems might store prose memory entries in files and use them as behavior-shaping instructions. One may write only human-approved entries; another may mine traces after every session. One may activate cues automatically before risky actions; another may wait for manual search. Artifact class, backend, and role match, but operational axes diverge.

The [Rosebud LLM-memory essay](../sources/everything-you-need-to-know-about-llm-memory.md) makes this explicit as a practitioner design map. After choosing what gets stored, a system must still choose how material is derived, written, retrieved, processed after retrieval, curated, and forgotten. The source's strongest contribution is not a new backend taxonomy. It is the reminder that memory quality comes from the path through these operational choices.

This also explains why [agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md). Storage belongs to the execution substrate. Activation belongs to the context engine. Learning and lifecycle decisions cut across both. The operational axes name the places where those components meet.

## Detailed notes

Use this note as a router into the detailed requirement notes:

- Capture and derivation: [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) and [use trace-derived extraction as meta-learning](./agent-memory-requirements/use-trace-derived-extraction.md).
- Activation: [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md).
- Authority: [Make Authority Explicit](./agent-memory-requirements/make-authority-explicit.md).
- Lifecycle: [Retire, Redact, Supersede, And Relax Memory](./agent-memory-requirements/retire-redact-supersede-relax.md).
- Compiled views: [Keep Memory Roles And Compiled Views From Drifting](./agent-memory-requirements/keep-compiled-views-aligned.md).
- Evaluation: [Evaluate Memory By Effects](./agent-memory-requirements/evaluate-memory-by-effects.md).

## Status

This note is a seedling companion to [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md). If the six-axis list proves stable across new memory-system reviews and design discussions, fold it into the design note rather than maintaining a separate claim.

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) - extends: adds memory-specific operational policies around the base class, backend, and role taxonomy
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - sharpens: this note names the operational axes behind the requirements map
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - grounds: operational memory axes cross storage, context engineering, and learning rather than belonging to one subsystem
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) - exemplifies: learned memory-management policy is one implementation of the operational axes when a domain supplies a clear oracle
- [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md) - evidence: reviewed systems vary most consequentially by curation agency and lifecycle choices, not only backend
- [Everything you need to know about LLM memory](../sources/everything-you-need-to-know-about-llm-memory.md) - evidence: practitioner map of raw and derived memory, write triggers, retrieval timing, curator identity, and forgetting propagation
