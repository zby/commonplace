---
description: Repo-native document-analysis workspace with staged/published KB boundaries, multimodal evidence channels, provenance tracing, and sync-time promotion of interaction logs into published memories
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# DocMason

DocMason is a Python-first local workspace for deep research over private work documents. It treats the repository itself as the application surface: `original_doc/` is the live corpus boundary, `knowledge_base/current/` is the published read surface, `runtime/` holds execution state, and the host agent is expected to enter through a governed `ask` workflow or a small public CLI. The implementation is substantial and real. The repo contains source parsers for Office/PDF/email/text inputs, staged and published KB lifecycle code, deterministic retrieval and trace artifacts, host-thread reconciliation for Codex and Claude Code, and a sync-time interaction-memory promotion path.

**Repository:** https://github.com/JetXu-LLM/DocMason

## Core Ideas

**The repo is the app, and the agent is the runtime.** DocMason is not a SaaS wrapper around a hidden backend. `AGENTS.md`, canonical skills, and the stable `docmason` CLI define the product boundary directly inside the repository. Ordinary questions are supposed to enter through one governed natural-language front door (`ask`), while deterministic operator work goes through explicit commands like `prepare`, `sync`, `retrieve`, `trace`, and `validate-kb`. This is a stronger version of the "repo-native app" bet than most related systems make: the repo is not just the storage layer, it is also the execution contract.

**Published truth is separated from raw corpus and staging.** The architectural center of gravity is the boundary between `original_doc/`, `knowledge_base/staging/`, and `knowledge_base/current/`. Sync builds staged source directories, validates them, then publishes a single current root through a controlled pointer switch and compact publish ledger. Retrieval and trace are supposed to operate over published artifacts rather than directly over raw files or half-built staging state. This is one of the clearest reviewed implementations of "published truth" as a first-class KB concept instead of an informal convention.

**Multimodal evidence is compiled into explicit evidence channels.** The source builders do more than flatten files to text. PDF, PowerPoint, Word, spreadsheet, email, and text inputs are staged into `source_manifest.json`, `evidence_manifest.json`, extracted text/structure assets, rendered artifacts, media copies, and derived affordance sidecars. The affordance layer makes the published evidence channels used today explicit: `text`, `render`, `structure`, `notes`, and `media`. Where extractors can preserve richer semantics they show up through structure assets and affordances; where they cannot, interactive or time-based behavior is flattened into supportable render/media artifacts rather than preserved as full interactivity. The retrieval path then ranks not only text but also structure summaries, artifact labels, semantic overlays, and channel descriptors.

**Retrieval and provenance tracing are built around support discipline, not just ranking.** The retrieval stack is lexical-plus-graph scoring over published source, unit, and artifact records, but the more distinctive part is the truth-boundary logic around it. `truth_boundary.py` builds source-scope policies such as `source-scoped-hard` and `compare`, while trace assembly checks canonical support, scope satisfaction, support manifests, and render requirements. The result is not just "find relevant files" but "show what evidence this answer is allowed to claim and whether the support basis is explainable."

**Host interaction logs can be promoted into published interaction memories.** DocMason does not only compile source documents. It also reconciles native Codex and Claude Code threads into runtime interaction entries, builds a pending overlay for retrieval/trace, and during sync groups those entries into published `interaction-memory-*` directories with manifests, copied attachments, affordances, and conservative auto-authored `knowledge.json` plus `summary.md`. That makes it a genuine live-session artifact-learning system, though a conservative one: the promoted artifact is a typed symbolic memory, not a high-reach rule set or learned policy.

## Comparison with Our System

| Dimension | DocMason | Commonplace |
|---|---|---|
| Primary problem | Deep research over private office/document corpora with strict provenance | Building and maintaining a navigable, composable knowledge base |
| Product boundary | Repo-native app workspace; repo includes runtime contract, CLI, publication model, and host adapters | Repo-native KB plus methodology, with lighter runtime assumptions and fewer productized operator surfaces |
| Truth surface | Explicit raw/staging/current split; published KB is the reader-facing truth | Notes in git are the truth directly; no separate published snapshot boundary |
| Evidence model | Multimodal compiled artifacts with explicit channels (`text`, `render`, `structure`, `notes`, `media`) | Primarily authored markdown notes, descriptions, links, and indexes |
| Retrieval discipline | Deterministic lexical-plus-graph retrieval over published artifacts, plus source-scope and canonical-support guards | Search, routing, indexes, and semantic links; stronger navigation semantics, weaker runtime gating |
| Learning loop | Sync-time promotion of host interaction traces into published interaction memories | Human/agent-authored notes and occasional trace-derived workshop analysis; no built-in runtime promotion loop |
| Validation model | Validation-gated publication with staged manifests and artifact checks | Structural validation plus semantic review of notes |
| Human/agent coexistence | Strong for document-heavy local analyst work with existing host agents | Strong for long-lived curated knowledge development and methodological reflection |

DocMason is stronger where the problem is "how do I make a local agent answer against messy private business documents without pretending that raw source files are already queryable truth?" Commonplace is stronger where the problem is "how do I make accumulated knowledge legible, composable, and maintainable over time?" DocMason commits more structure into runtime plumbing, manifests, and publication boundaries. Commonplace commits more structure into the documents themselves.

The systems also make different bets about what counts as the hard part. For DocMason, the hard part is preserving evidence identity across multimodal compilation and controlling what the agent may cite. For Commonplace, the hard part is shaping durable knowledge so future agents can find and combine it cheaply. Those are adjacent design spaces, not substitutes.

## Borrowable Ideas

**A published-truth boundary should be a real mechanism, not a social rule.** DocMason's `original_doc/` -> `staging/` -> `current/` pipeline is stronger than our implicit "edited files are the truth" posture for any workflow where raw inputs are not yet trustworthy KB artifacts. Ready to borrow as a design principle whenever we add heavier workshop ingestion or compiled views.

**Evidence channels should be explicit in the retrieval contract.** The `text`/`render`/`structure`/`notes`/`media` model is a strong pattern because it lets the system ask whether the currently published artifacts are sufficient before escalating. We already reason about pointers and disclosure depth; DocMason shows a concrete way to encode evidence modality into retrieval results. Ready to borrow now as a framing pattern.

**Source-scope policy is a useful guardrail against accidental synthesis drift.** The source-reference resolution plus `source-scoped-hard` / `compare` policy is a concrete way to stop a retrieval engine from silently widening the evidence base. Commonplace has link semantics and note-level curation, but we are much thinner on explicit answer-scope enforcement. Ready to borrow when we have more answer-generation workflows over heterogeneous evidence.

**Session traces can promote into symbolic artifacts without leaving the file substrate.** The interaction-memory path is one of the most interesting parts of the repo. It turns host-native turns and attachments into grouped memory directories with source manifests and conservative semantic outputs, then lets published retrieval consume them. We should not copy the exact schema blindly, but the workshop-to-library bridge is immediately relevant. Needs a concrete workshop-memory use case first.

**Separate the ordinary front door from operator commands.** DocMason is unusually explicit that `ask` is for ordinary natural-language work and the CLI is for deterministic operator operations. Commonplace has some of this split in practice, but less productized. Ready to borrow as a user-facing boundary if we ever need a tighter runtime surface.

## Curiosity Pass

**"The repo is the app" is partly packaging, but the package contains real contracts.** The claimed property is that the user can treat the repo itself as a governed application. The mechanism is not just branding: the stable CLI, skill routing, runtime state directories, and host reconciliation logic really do make the repository an executable surface. The simpler alternative is "a repo plus a pile of scripts and README instructions." DocMason is meaningfully stronger than that. But the ceiling is still bounded by the host agent's willingness to follow the contract; the repo can shape entry and evidence use, not guarantee perfect obedience.

**The published-truth boundary is a genuine transformation, not just relocation.** The property is trustworthy read-time state. Here the mechanism really changes what exists: raw files become staged artifacts, validated manifests, retrieval indexes, and one activated current root. The simpler alternative is answering directly against `original_doc/` or against whatever half-built files happen to be present. DocMason is right to reject that. The ceiling, though, is important: publication proves "this snapshot passed DocMason's build and validation rules," not "the synthesized business conclusion is true."

**The multimodal evidence layer is real, but its strength is bounded by extractor quality.** The repo does more than relabel text as multimodal. It creates render assets, structure JSON, artifact indexes, spreadsheet views, and attachment lineage. That is genuine representation change. But some of the pipeline is still conversion-heavy and heuristic: Office files often route through LibreOffice to PDF/PNG, semantic overlays are derived sidecars, and affordance descriptors are partly synthesized from staged metadata. The mechanism improves inspectability and answer support; it does not magically solve document understanding.

**Provenance tracing is strongest as a support-boundary mechanism, not as a correctness oracle.** The claimed property is strict traceability. Mechanistically, DocMason earns a lot of that claim: trace artifacts know source IDs, units, artifacts, consumers, support basis, render requirements, and source-scope policy. The simpler alternative is ranked retrieval plus citations pasted into the answer. DocMason is clearly stronger. But even if the trace path is perfect, the system still cannot prove the synthesis is semantically correct. It proves that the answer points to admissible support through DocMason's published evidence model.

**Interaction-memory promotion is real trace-derived artifact learning, but conservative.** The property is that live host interactions can become durable knowledge. That is genuinely implemented: the repo captures turns, groups them, writes memory directories, auto-authors semantic outputs, and includes promoted memories in published retrieval. The simpler alternative is leaving session logs as unstructured runtime residue. DocMason does more than that. Still, the ceiling is lower than stronger artifact-learning systems like ExpeL or ACE. The promoted output is closer to cautious session condensation with typed semantics than to explicit rule maintenance, contradiction handling, or high-reach lesson extraction.

## What to Watch

- Whether the interaction-memory path grows a stronger maintenance model: deduplication, contradiction handling, retirement, and clearer evaluation of which promoted session artifacts deserve durable status.
- Whether the "ordinary ask plus operator CLI" split stays coherent as support for Codex, Claude Code, and Copilot expands and generated adapters accumulate.
- Whether the multimodal compilation story keeps pace with messy real-world decks and spreadsheets, or whether the repo leans increasingly on hybrid sidecars and manual follow-up to close fidelity gaps.
- Whether the published-truth discipline remains the stable center of the product, or gets diluted as more runtime artifacts, evaluation surfaces, and bundle/update machinery accumulate.

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../files-not-database.md) — foundation: DocMason pushes the file-first bet from KB authoring into multimodal private-document analysis and published evidence serving
- [Inspectable substrate, not supervision, defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — foundation: DocMason's trust story depends on inspectable manifests, renders, and trace artifacts rather than a hidden service boundary
- [Deterministic validation should be a script](../deterministic-validation-should-be-a-script.md) — exemplifies: DocMason treats validation as a hard publish gate instead of a lightweight editorial afterthought
- [A functioning KB needs a workshop layer, not just a library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: interaction-memory promotion is a concrete workshop-to-library bridge built from session traces
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: DocMason adds a repo-native live-session artifact-learning case grounded in host-thread reconciliation and sync-time promotion
- [Substrate class, backend, and artifact form are separate axes that get conflated](../substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: DocMason's interaction memories are symbolic artifacts in a file backend, not a separate memory substrate
