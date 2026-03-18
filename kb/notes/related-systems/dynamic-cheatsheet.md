---
description: Test-time adaptive memory that carries forward a prompt-shaped cheatsheet across queries — artifact-learning via full cheatsheet rewrites and optional retrieval/synthesis, without weight updates
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-18
---

# Dynamic Cheatsheet

Dynamic Cheatsheet is a Python framework for test-time learning with an evolving cheatsheet. A model answers a query with the current cheatsheet in context, then a second prompt rewrites that cheatsheet for the next query. The repo also supports retrieval variants that pull similar past examples and optionally synthesize them into a per-query cheatsheet. Built by Mirac Suzgun and collaborators, MIT-style research code rather than a production memory service.

**Repository:** https://github.com/suzgunmirac/dynamic-cheatsheet

## Core Ideas

**The learned artifact is one carried-forward cheatsheet string.** The primary state is a single cheatsheet text blob passed from one query to the next. In the cumulative mode, each call returns `final_cheatsheet`, and the benchmark runner feeds that text into the next sample. There is no separate note graph, ledger, or typed memory store in the repo.

**Curation is full-document rewrite, not local mutation.** The prompts talk about preserving good content, incrementing counts, removing redundancy, and refining the cheatsheet. But the implementation extracts a `<cheatsheet>...</cheatsheet>` block from the model response and replaces the old cheatsheet wholesale. This is real artifact learning, but the maintenance mechanism is rewrite-and-carry-forward, not operation-based editing.

**The strongest implemented distinction is cumulative versus retrieval-shaped memory.** The repo exposes several approaches: cumulative cheatsheet growth, retrieval-only, retrieval plus synthesis, and cumulative plus retrieval. The retrieval paths use embeddings and cosine similarity over prior examples, then either inject those examples directly or ask the model to synthesize a custom cheatsheet for the current query.

**The trace substrate is benchmark query history, not live sessions.** Dynamic Cheatsheet learns from ordered problem attempts in benchmark runs. The raw signal is the current question, the model answer, and optionally previous input-output pairs or retrieved examples. It is not mining assistant tool traces or multi-role execution logs.

**Counts exist at the prompt level, not as enforced state transitions.** The curator prompts require `** Count:` fields on memory items, but the repo does not enforce or independently update those counts in code. The counter policy is delegated to the LLM's rewrite behavior.

## Comparison with Our System

Dynamic Cheatsheet is a clear artifact-learning system, but a much looser one than the workshop-memory systems in our KB. It has persistent learning across queries, yet the substrate is one prompt-shaped document rather than a collection of separately addressable artifacts.

| Dimension | Dynamic Cheatsheet | Commonplace |
|---|---|---|
| Trace source | Ordered benchmark queries, answers, and retrieved prior examples | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | One evolving cheatsheet text blob | Notes, links, instructions, workshop artifacts |
| Promotion target | Inspectable text only | Inspectable text only |
| Update style | Full cheatsheet rewrite each step | Manual curation and targeted file edits |
| Retrieval model | Optional embeddings + cosine retrieval over prior examples | Agent-driven navigation over linked markdown |
| Oracle strength | Usually implicit task success within benchmark workflow | Weak, mostly human judgment |
| Storage model | Files plus embedding cache/results outputs | Files in git |

**Trace-derived learning placement.** On axis 1 of the survey, Dynamic Cheatsheet fits the **trajectory-run pattern**: it learns from repeated problem attempts, not from one live session stream. On axis 2, it is clearly **trace-derived artifact-learning**: the learned result is an inspectable cheatsheet, never weights. It should be added to the survey, but with a caveat: it is closer to prompt-state accumulation than to explicit memory-system curation.

Compared with [Pi Self-Learning](./pi-self-learning.md), Dynamic Cheatsheet uses a much broader freeform artifact and much weaker structural constraints. Compared with trajectory-informed memory generation, it is more online and cumulative, but less explicit about extraction categories and lifecycle.

## Borrowable Ideas

**Carry-forward artifact as the minimum learning loop.** Ready now as a framing. Dynamic Cheatsheet shows the minimal closed loop for artifact learning: current artifact in, revised artifact out, feed it forward. That is useful as a lower bound against which richer workshop systems can be judged.

**Retrieval-plus-synthesis as a hybrid mode.** Needs a use case first. The retrieval-synthesis variants are a concrete pattern for combining global accumulated memory with task-local recalled examples.

**Example-conditioned artifact rewrite.** Needs a use case first. The retrieval-synthesis prompt is a plausible mechanism for rewriting a local playbook from a small bank of nearby precedents, rather than from the full history.

## Curiosity Pass

The repo's strongest idea is not "adaptive memory" in the abstract. It is the explicit comparison between several cheap memory-update strategies: keep one growing cheatsheet, retrieve similar examples, synthesize a per-query cheatsheet, or combine both. That makes the system useful as an ablation reference for artifact-learning loops.

The weaker part is maintenance fidelity. The prompts ask the model to preserve, compress, count, and improve the cheatsheet, but the code does not enforce those invariants. Because the state update is "extract `<cheatsheet>` and replace the old one," the whole lifecycle depends on the rewrite quality of one model call.

So Dynamic Cheatsheet is genuinely more than retrieval, but less than a structured memory system. It is best understood as test-time artifact learning through prompt-mediated state carryover.

## What to Watch

- Whether later versions move from full cheatsheet rewrite to operation-level maintenance
- Whether the retrieval variants outperform cumulative-only mode outside narrow benchmark settings
- Whether the repo grows any explicit memory schema stronger than freeform XML-like blocks
- Whether this line of work converges toward structured workshop artifacts or stays at prompt-state level

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Dynamic Cheatsheet is a clean additional artifact-learning case built from repeated task attempts and prompt-carried memory
- [Pi Self-Learning](./pi-self-learning.md) — contrasts: both reinject textual learnings, but Pi Self-Learning uses narrow schemas and explicit scoring while Dynamic Cheatsheet relies on freeform cheatsheet rewrites
- [Autocontext](./autocontext.md) — contrasts: both learn across runs into artifacts, but Autocontext has richer orchestration and optional weight export, while Dynamic Cheatsheet stays at prompt-state artifacts
- [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: Dynamic Cheatsheet is the artifact-side counterpart to weight-learning systems that also depend on strong recurring task signals
- [deploy-time learning](../deploy-time-learning-the-missing-middle.md) — sharpens: this system sits squarely in the deploy-time artifact-update space, using persistent prompt-state rather than weights
