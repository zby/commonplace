---
description: "Memory design needs operational policy axes (capture, derivation, activation, authority assignment, lifecycle, evaluation) on top of substrate, form, lineage, and behavioral authority"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, title-as-claim]
tags: [agent-memory, context-engineering, learning-theory, artifact-analysis]
---

# Memory design adds operational axes to artifact analysis

[Axes of artifact analysis](./axes-of-artifact-analysis.md) separates retained behavior-shaping artifacts by [storage substrate](./definitions/storage-substrate.md) (where state persists), [representational form](./definitions/representational-form.md) (how the operative part is encoded and consumed), [lineage](./definitions/lineage.md) (what source dependencies govern invalidation), and [behavioral authority](./definitions/behavioral-authority.md) (who consumes it, through which channel, with what force). That taxonomy prevents category mistakes like treating "files versus weights" as a single design choice. Agent memory needs those fields, but artifact identity is not enough. A memory system also needs to say how retained material is captured, transformed, activated, governed, evaluated, and retired over time.

This seedling note names those cross-cutting operational axes. Its job is not to replace the detailed memory-requirements notes, but to make those requirements comparable when a memory discussion starts from storage format, representational form, or memory mechanism label.

## Artifact fields

[Axes of artifact analysis](./axes-of-artifact-analysis.md) answers what retained artifact exists and how a consumer can use it:

| Axis | Question | Memory example |
|---|---|---|
| Storage substrate | Where does the artifact live? | Repo file, SQL row, vector record, graph edge, service-owned memory object |
| Representational form | How is the operative part represented and consumed? | Distributed-parametric policy in weights, prose memory entry, symbolic test or schema |
| Lineage | What source dependencies or derivations does it carry? | Trace-extracted fact, generated cue, compiled prompt view, canonical workflow |
| Behavioral authority | Who consumes it, through which channel, and with what force? | Reference advice, prompt instruction, validator enforcement, ranking influence, learning input |

These fields are necessary because memory discussions often conflate them — [agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) collects the recurring confusions, and [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md) shows substrate-first comparisons missing the more consequential fields. A vector store is a substrate, not a representational form. A prompt rule is usually prose-form but behavior-shaping only through a specific authority path. A Markdown file can advise when read as reference and instruct when loaded as standing context.

But artifact fields stop at the artifact boundary. They do not explain how retained material becomes future capacity.

## Operational memory axes

Operational axes describe the policies that turn retained material into usable memory:

| Axis | Question | Common choices |
|---|---|---|
| Capture policy | What enters the memory system? | Write everything, heuristic trigger, LLM curator, user-marked item, post-session mining |
| Derivation policy | How does raw material become usable? | Keep raw traces, summarize, extract facts, build graph edges, create cues, generate [system-definition artifacts](./definitions/system-definition-artifact.md) |
| Activation policy | How does memory reach a future bounded context? | Always injected, hook-driven retrieval, tool-driven search, on-reference loading, on-situation cue |
| Authority policy | Who decides and who can revise? | Harness, cheap model, main model, background model, user, reviewer, deterministic validator |
| Lifecycle policy | How does memory change or leave? | Supersede, invalidate, decay, redact, delete, relax enforcement, regenerate compiled views |
| Evaluation policy | What proves the memory helped? | Retrieval score, task outcome, behavior change, artifact quality, human review, ablation |

The framing is what's new, not the underlying design pressures. Each axis maps onto existing requirement notes: capture and derivation cover ingress and trace extraction; activation covers behavior-changing memory; authority covers write, promotion, enforcement, and revision rights; lifecycle covers how memory changes (decay, supersession, redaction, relaxation, temporal validity); evaluation covers downstream effects rather than storage volume. Authority and lifecycle meet at retirement: authority answers *who* may retire a memory, lifecycle answers *how* retirement happens.

## Why the split matters

The same artifact fields can produce different memory behavior. Two systems might store prose memory entries in files and use them as behavior-shaping instructions. One may write only human-approved entries; another may mine traces after every session. One may activate cues automatically before risky actions; another may wait for manual search. Substrate, form, lineage, and authority can match while operational policies diverge.

The operational axes are also mutually independent: fully specifying the capture and derivation (learning) axes leaves the activation axis open — which is why a memory system or review can elaborate its learning loop in detail and still leave read-back (how stored memory re-enters a future action) specified as a single retrieval question. Activation has its own placement choices — whether memory reaches the agent by the agent's own lookup (pull) or arrives unsolicited (push), what trips it, before or after the action, at what scope, and with what force at consumption — none of which are fixed by how the memory was learned.

The [Rosebud LLM-memory essay](../sources/everything-you-need-to-know-about-llm-memory.md) makes this explicit as a practitioner design map. After choosing what gets stored, a system must still choose how material is derived, written, retrieved, processed after retrieval, curated, and forgotten. The source's strongest contribution is not a new substrate taxonomy. It is the reminder that memory quality comes from the path through these operational choices.

This also explains why [agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md). Storage belongs to the execution substrate. Activation belongs to the context engine. Learning and lifecycle decisions cut across both. The operational axes name the places where those components meet.

## Detailed notes

Use this note as a router into the detailed requirement notes:

- Capture and derivation: [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) and [use trace extraction as meta-learning](./agent-memory-requirements/use-trace-extraction-as-meta-learning.md).
- Activation: [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md).
- Authority: [Make Authority Explicit](./agent-memory-requirements/make-authority-explicit.md).
- Lifecycle: [Retire, Redact, Supersede, And Relax Memory](./agent-memory-requirements/retire-redact-supersede-relax.md).
- Compiled views: [Keep Memory Roles And Compiled Views From Drifting](./agent-memory-requirements/keep-compiled-views-aligned.md).
- Evaluation: [Evaluate Memory By Effects](./agent-memory-requirements/evaluate-memory-by-effects.md).

## Status

This note is a seedling companion to [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md). If the six-axis list proves stable across new memory-system reviews and design discussions, fold it into the design note rather than maintaining a separate claim.

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) - extends: adds memory-specific operational policies around the substrate, form, lineage, and authority taxonomy
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - sharpens: this note names the operational axes behind the requirements map
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - grounds: operational memory axes cross storage, context engineering, and learning rather than belonging to one subsystem
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) - exemplifies: learned memory-management policy is one implementation of the operational axes when a domain supplies a clear oracle
- [The fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md) - evidence: reviewed systems vary most consequentially by curation agency and lifecycle choices, not only substrate
- [Everything you need to know about LLM memory](../sources/everything-you-need-to-know-about-llm-memory.md) - evidence: practitioner map of raw and derived memory, write triggers, retrieval timing, curator identity, and forgetting propagation
- [Open-domain memory retention needs a declared output spec](./open-domain-memory-retention-needs-a-declared-output-spec.md) - mechanism: explains why the capture-policy row's choices split the way they do — the missing option is a declared output spec supplying the admission criterion that heuristic and everything-write policies lack
