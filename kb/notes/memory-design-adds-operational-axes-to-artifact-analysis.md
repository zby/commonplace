---
description: "Memory design needs operational policy axes (capture, derivation, activation, authority assignment, lifecycle, evaluation) on top of substrate, form, lineage, and behavioral authority"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, title-as-claim]
tags: [agent-memory, context-engineering, learning-theory, artifact-analysis]
---

# Memory design adds operational axes to artifact analysis

[Axes of artifact analysis](./axes-of-artifact-analysis.md) separates retained behavior-shaping artifacts by [storage substrate](./definitions/storage-substrate.md) (where state persists), [representational form](./definitions/representational-form.md) (how the operative part is encoded and consumed), [lineage](./definitions/lineage.md) (what source dependencies govern invalidation), and [behavioral authority](./definitions/behavioral-authority.md) (who consumes it, through which channel, with what force). That taxonomy prevents category mistakes like treating "files versus weights" as a single design choice. Agent memory needs those fields, but artifact identity is not enough on its own. A memory system also needs to say how retained material is captured, transformed, activated, governed, evaluated, and retired over time.

This seedling note names those cross-cutting operational axes. It does not replace the detailed memory-requirements notes. It makes those requirements easier to compare when a memory discussion starts from a storage format, representational form, or memory-mechanism label.

Here, an operational axis is a recurring comparison question, not a claim that the questions form a uniquely exhaustive or pairwise-independent basis. This checklist remains provisional: if repeated system comparisons support a different grouping, its rows should be merged or split.

## Artifact fields

[Axes of artifact analysis](./axes-of-artifact-analysis.md) answers what retained artifact exists and how a consumer can use it:

| Axis | Question | Memory example |
|---|---|---|
| Storage substrate | Where does the artifact live? | Repo file, SQL row, vector record, graph edge, service-owned memory object |
| Representational form | How is the operative part represented and consumed? | Distributed-parametric policy in weights, natural-language memory entry, symbolic test or schema |
| Lineage | What source dependencies or derivations does it carry? | Trace-extracted fact, generated cue, compiled prompt view, canonical workflow |
| Behavioral authority | Who consumes it, through which channel, and with what force? | Reference advice, prompt instruction, validator enforcement, ranking influence, learning input |

These fields are necessary because memory discussions often conflate them. [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) collects the recurring confusions, and [the comparative agent-memory review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) shows how substrate-first comparisons can miss consequential curation and lifecycle differences. A vector store is a substrate, not a representational form. A prompt rule is usually natural-language in form, but it shapes behavior only through a specific authority path. A Markdown file can advise when read as reference and instruct when loaded as standing context.

But artifact fields stop at the artifact boundary. They do not explain how retained material becomes future capacity.

## Operational memory axes

Operational axes describe the policies that turn retained material into usable memory:

| Axis | Question | Common choices |
|---|---|---|
| Capture policy | What qualifies for retention, and what triggers a write? | [Declared output specification](./open-domain-memory-retention-needs-a-declared-output-spec.md), write everything, heuristic trigger, LLM curator, user-marked item, post-session mining |
| Derivation policy | How does raw material become usable? | Keep raw traces, summarize, extract facts, build graph edges, create cues, generate [system-definition artifacts](./definitions/system-definition-artifact.md) consumed with binding instruction, validation, routing, or configuration force |
| Activation policy | How does memory reach a future bounded context? | Always injected, hook-driven retrieval, tool-driven search, on-reference loading, on-situation cue |
| Authority policy | Who may write, promote, revise, and retire memory? | Harness, cheap model, main model, background model, user, reviewer, deterministic validator |
| Lifecycle policy | How does memory change or leave? | Supersede, invalidate, decay, redact, delete, relax enforcement, regenerate compiled views |
| Evaluation policy | What proves the memory helped? | Retrieval score, task outcome, behavior change, artifact quality, human review, ablation |

What is new here is the framing, not the underlying design pressures. Capture and derivation cover ingress and trace extraction. Activation covers behavior-changing memory. Authority covers write, promotion, revision, and retirement rights. Lifecycle covers decay, supersession, redaction, relaxation, and temporal validity. Evaluation covers downstream effects rather than storage volume.

Behavioral authority describes how a retained artifact affects its consumer at use time. Authority policy instead governs who may change the memory's content or status. It meets lifecycle at retirement: authority answers *who* may retire a memory, while lifecycle answers *how* retirement happens.

Capture also has a **signal-timing** refinement: which evidence the learning consumes. [Machine Studying](../sources/machine-studying.ingest.md), a practitioner report and benchmark, isolates corpus-only preparation before any downstream task, reward, demonstration, or execution trace exists. [Agent Workflow Memory](../agent-memory-systems/reviews/agent-workflow-memory.md), by contrast, learns from execution trajectories. Self-generated questions remain pre-task when they derive only from the corpus, while mining the agent's own execution traces is conditioned on the task loop.

## Why the split matters

The same artifact fields can produce different memory behavior. Two systems might store natural-language memory entries in files and use them as behavior-shaping instructions. One may write only human-approved entries, while another may mine traces after every session. One may activate cues automatically before risky actions, while another may wait for manual search. Substrate, form, lineage, and authority can match while operational policies diverge.

Artifact fields do not fully determine operational policies, and specifying one subset of those policies need not determine another. Specifying capture and derivation can still leave activation open: [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md). Activation still has to settle whether memory arrives by lookup or unsolicited injection, what triggers it, when it arrives, its scope, and its force at consumption.

The [Rosebud LLM-memory essay](../sources/everything-you-need-to-know-about-llm-memory.md) provides a practitioner instance of this choice path: after deciding what gets stored, a system still has to choose how material is derived, written, retrieved, processed, curated, and forgotten. These policies cross component boundaries. Storage belongs to the execution substrate, activation belongs to the context engine, and learning and lifecycle decisions cut across both.

## Detailed notes

Use this note as a router into the detailed requirement notes:

- Capture and derivation: [raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) and [use trace extraction as meta-learning](./agent-memory-requirements/use-trace-extraction-as-meta-learning.md).
- Activation: [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md).
- Authority: [Make Authority Explicit](./agent-memory-requirements/make-authority-explicit.md).
- Lifecycle: [Retire, Redact, Supersede, And Relax Memory](./agent-memory-requirements/retire-redact-supersede-relax.md).
- Compiled views: [Keep Memory Roles And Compiled Views From Drifting](./agent-memory-requirements/keep-compiled-views-aligned.md).
- Evaluation: [Evaluate Memory By Effects](./agent-memory-requirements/evaluate-memory-by-effects.md).

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — extends: develops the checklist into a requirements map for memory-system design
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: learned memory-management policy implements the operational questions when a domain supplies a clear oracle
