---
description: "DocMason review: repo-native local document KB with provenance, deterministic retrieval/trace, interaction-memory promotion, and governed ask activation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-01"
---

# DocMason

Replaced by [docmason.md](./docmason.md) on 2026-06-04.

DocMason, from JetXu-LLM's `DocMason` repository, is a repo-native local application for building a provenance-aware knowledge base from private work documents and answering through a host agent such as Codex or Claude Code. The repository is both product and runtime surface: source files go under `original_doc/`, compiled evidence is published under `knowledge_base/current/`, host activity and answer artifacts live under `runtime/`, and canonical agent workflows live as skills inside the repo.

**Repository:** https://github.com/JetXu-LLM/DocMason

**Reviewed commit:** [f84935b2b7e1e59e64d8ba78066c35d5f55c8559](https://github.com/JetXu-LLM/DocMason/commit/f84935b2b7e1e59e64d8ba78066c35d5f55c8559)

**Last checked:** 2026-06-01

## Core Ideas

**The repo is the operating surface, not just storage.** `AGENTS.md` defines DocMason as a repo-native workspace where files, directories, scripts, skills, and CLI contracts define workflow boundaries; ordinary questions enter through canonical `ask`, while setup, sync, status, review, and adapter work route to explicit operator workflows (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/AGENTS.md). The architecture docs make the same boundary concrete: `original_doc/` is private source input, `knowledge_base/current/` is published truth, `knowledge_base/staging/` is a working area, and `runtime/` holds local execution, review, and audit state (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/docs/architecture/README.md).

**The stable public CLI separates deterministic operations from agent reasoning.** The CLI exposes `prepare`, `doctor`, `status`, `sync`, `retrieve`, `trace`, `validate-kb`, `sync-adapters`, `update-core`, and `workflow`; hidden `_ask` and `_hook` entrypoints are kept out of public help and used for host integration plumbing (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/cli.py). This split matters architecturally: deterministic setup, sync, validation, retrieval, and trace are symbolic system-definition surfaces, while the host LLM remains the reasoning runtime.

**Document ingestion compiles private files into structured evidence bundles.** Supported inputs include PDF, Office files, markdown/plain text, email, and lightweight text formats; Office support depends on local LibreOffice and PDF support uses local Python parsing/rendering libraries (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/project.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/pyproject.toml). The evidence compiler creates per-source manifests, extracted unit text, structure JSON, render references, artifact indexes, and modality-specific signals for PDFs, slides, spreadsheets, documents, emails, and text (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/knowledge.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/evidence_artifacts.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/text_sources.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/email_sources.py).

**Context efficiency is handled by compiled retrieval records and compact host projections.** Sync builds source, unit, and artifact retrieval records from the published corpus, including source summaries, entities, key points, claims, unit text, structure summaries, render references, affordance descriptors, semantic overlays, and graph edges (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/retrieval.py). Runtime retrieval ranks sources by lexical field weights, unit matches, artifact matches, structure context, semantic overlays, trust/citation signals, graph expansion, comparison coverage, and interaction-memory policy; the public workflow tells hosts to prefer `--json --compact` and inspect selected fields before loading nested evidence into chat (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical/grounded-answer/SKILL.md). This is a context-engineering system: it does not put the whole KB in context; it compiles smaller read surfaces and staged escalation paths.

**Provenance and answer admissibility are first-class outputs.** The public `trace` command traces a source, answer file, or session back to published evidence, and the grounded-answer workflow requires retrieval, answer-file drafting, trace, and hidden ask finalization before a final ordinary answer is legal (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/cli.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical/grounded-answer/SKILL.md). The shared contracts require committed turns to declare `answer_state` and `support_basis`, and the allowed answer states are `grounded`, `partially-grounded`, `unresolved`, and `abstained` (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/contracts.py).

**Host interactions become a second, lower-trust memory source.** Claude hooks mirror session, prompt, tool-use, stop, and session-end events into `runtime/interaction-ingest/claude-code` (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/.claude/settings.json, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/hooks.py). Sync groups pending interaction entries by conversation, builds `interaction-memory-*` directories with source/evidence manifests, extracted turns, copied attachments, semantic fields such as `memory_kind`, `durability`, `answer_use_policy`, and `retrieval_rank_prior`, then publishes and marks entries as promoted (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/interaction.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/knowledge.py). These memories are deliberately distinguished from source documents with `source_family = interaction-memory` and `trust_tier = interaction`.

**Semantic overlays are additive, bounded, and lower than primary evidence.** Deterministic affordances describe which evidence channels are available, while `semantic_overlay/*.json` sidecars can add cross-region or multimodal semantics for hard artifacts such as charts, tables, page images, diagrams, and weak text layers (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/affordances.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/semantic_overlays.py). The knowledge-construction skill explicitly says overlays are additive and not a second primary truth surface (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical/knowledge-construction/SKILL.md).

## Artifact analysis

- **Storage substrate:** `files` — The workspace filesystem under `original_doc/`, with sample public fixtures separately held under `sample_corpus/` and copied only for demo use (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/docs/product/distribution-and-benchmarks.md)
- **Representational form:** `prose` `symbolic` — Source documents, summaries, answer files, and turn excerpts are prose; manifests, JSON/JSONL state, graph edges, retrieval records, trace records, workflow metadata, and validation contracts are symbolic.
- **Lineage:** `authored` `imported` `trace-extracted` — Canonical skills and contracts are authored repo state, private documents are imported source inputs, and interaction memories are derived from host session, prompt, tool-use, and stop traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Source evidence and interaction memories supply knowledge; skills and contracts instruct; ask/finalization gates enforce; workflows route; validation and trace check support; retrieval policies rank; interaction promotion turns traces into retained memory.

**Private source corpus.** The storage substrate is the workspace filesystem under `original_doc/`, with sample public fixtures separately held under `sample_corpus/` and copied only for demo use (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/docs/product/distribution-and-benchmarks.md). The representational form is mixed: binary Office/PDF, text, email, markdown, and lightweight structured text. Lineage is source-of-truth input lineage, tracked through source manifests, fingerprints, path history, first/last seen metadata, and source IDs during sync. Behavioral authority is knowledge artifact authority: source files are evidence and reference, not direct instructions to the agent until compiled and retrieved.

**Published knowledge base.** The storage substrate is `knowledge_base/current/`, produced from staging and versioning paths under `knowledge_base/` (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/project.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/versioning.py). The representational form is mixed prose plus symbolic JSON: `source_manifest.json`, `evidence_manifest.json`, `knowledge.json`, `summary.md`, extracted unit text, structure assets, render assets, artifact indexes, graph edges, retrieval records, trace records, affordances, and optional semantic overlays. Lineage is derived and partially regenerable from active sources plus sync state; validation checks required keys, citations, unit references, renders, summaries, related-source IDs, and placeholder content before retrieval/trace artifacts are rebuilt. Behavioral authority is primarily knowledge artifact authority at read time, with some system-definition authority in ranking, validation, provenance, and evidence-channel constraints.

**Canonical skills and agent contracts.** The storage substrate is repo-tracked markdown under `AGENTS.md`, `.claude/CLAUDE.md`, and `skills/canonical/*/SKILL.md` (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/AGENTS.md, https://github.com/JetXu-LLM/DocMason/tree/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/.claude/CLAUDE.md). The representational form is prose instruction plus some symbolic workflow metadata. Lineage is authored repository state, with generated adapters treated as translations rather than canonical truth. Behavioral authority is system-definition authority: these files instruct routing, govern ordinary ask legality, constrain evidence handling, and tell host agents when a final answer may be emitted.

**Runtime ask, logs, traces, and answer files.** The storage substrate is `runtime/`, especially `runtime/answers/`, `runtime/runs/`, `runtime/logs/`, `runtime/control_plane/`, `runtime/state/`, and `runtime/interaction-ingest/` (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/project.py). The representational form is mixed markdown answers plus symbolic JSON/JSONL state. Lineage is per-turn and per-session: hidden ask opens a canonical turn, retrieval produces query sessions, trace binds answers or source IDs to evidence, and finalize commits the turn under explicit support state (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical/ask/SKILL.md). Behavioral authority varies by consumption path: logs and traces are knowledge artifacts for audit and evidence; control-plane records, shared jobs, support contracts, answer-state checks, and finalization rules are system-definition artifacts that gate execution.

**Interaction-derived memories.** The storage substrate begins as host hook mirrors and reconciled native ledgers under `runtime/interaction-ingest/`, then moves through sync into `knowledge_base/staging/interaction/` and `knowledge_base/current/interaction/` memory directories (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/hooks.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/interaction.py). The representational form is mixed: JSONL event traces, prose turn excerpts, copied attachments, manifests, `interaction_context.json`, `knowledge.json`, `summary.md`, affordance JSON, and retrieval/trace records. Lineage is trace-derived: memory IDs are based on grouped interaction IDs, manifests preserve conversation and interaction IDs, fingerprints derive from interaction IDs, and promotion marks entries with promoted memory IDs. Behavioral authority starts as knowledge artifact authority during capture, then becomes ranked contextual evidence during retrieval and trace; it remains lower trust than source corpus evidence through `trust_tier = interaction`, `answer_use_policy`, `memory_kind`, and ranking policy.

**Promotion path.** DocMason's clearest promotion path is source or trace material -> staged evidence/manifests -> validation -> published KB -> retrieval/trace records -> answer support. It can also add semantic overlays after a bounded hard-artifact follow-up. That crosses representational form and behavioral authority: raw documents and host traces become structured evidence, validation inputs, ranking inputs, and eventually answer-support artifacts. It does not train a model or write opaque vector state.

## Comparison with Our System

| Dimension | DocMason | Commonplace |
|---|---|---|
| Primary purpose | Local private-document research app with governed answers and provenance | Methodology KB framework for agent-operated knowledge bases |
| Canonical substrate | Repo workspace plus private `original_doc/`, generated `knowledge_base/current/`, and local `runtime/` | Git-tracked `kb/` collections, type specs, validation, indexes, sources, reviews, and instructions |
| Ingestion | Compiles Office/PDF/text/email into manifests, extracted units, render/structure/artifact evidence, and summaries | Authors or snapshots markdown artifacts, then validates collection/type contracts |
| Read-back | Canonical `ask`, retrieve, trace, warm-start evidence, pending interaction relevance, and compact host projections | `rg`, indexes, skills, reports, authored links, and explicit review/workflow commands |
| Trace-derived learning | Promotes host interactions into lower-trust interaction memories and retrieval/trace inputs | Uses review/workshop artifacts; no automatic conversation-to-library promotion by default |
| Authority model | Strong runtime gates for answer legality, sync, support contracts, and provenance | Strong artifact contracts, schema validation, review gates, and git-native lifecycle |

DocMason and Commonplace share a filesystem-first instinct, but DocMason is a product runtime for private corpora while Commonplace is a methodology library and framework. DocMason's storage substrate deliberately includes ignored local state (`original_doc/`, `knowledge_base/`, `runtime/`) that should not be committed to a public repo. Commonplace makes most durable knowledge artifacts git-native and reviewable by default.

The strongest alignment is the explicit separation between knowledge artifacts and system-definition artifacts. DocMason keeps source evidence, compiled summaries, render assets, and interaction memories distinct from workflow contracts, validation rules, answer-state contracts, and control-plane gates. Commonplace uses the same split in collection contracts, type specs, validators, review bundles, and instructions.

The main divergence is that DocMason gives the runtime more power. Canonical ask owns turn opening, gating, sync decisions, retrieval, trace, final answer state, and finalization. Commonplace usually leaves more of that path to agent instructions, deterministic validation, and human-visible markdown review. DocMason is therefore a useful example of making a KB not just searchable, but operationally binding at answer time.

DocMason's context strategy is also more engineered than ordinary markdown-vault lookup. It compiles multiple retrieval surfaces, hides heavy nested payloads behind compact projections, tracks evidence channels, recommends render escalation only when needed, and can include previous answer evidence pointers or interaction-derived memory based on question profile. Commonplace's current default navigation is cheaper and more transparent, but less directly optimized for host-agent context budgets.

**Read-back:** `both` — With engineered push of retained warm-start answer evidence and interaction memory through canonical ask, plus pull through explicit `retrieve` and `trace`

### Borrowable Ideas

**Treat answer legality as a runtime contract.** Commonplace has validation and review gates, but DocMason's `answer_state` plus `support_basis` finalization model is a sharper answer-time contract. Borrow as a pattern for workflows where an agent must emit a grounded final answer, not merely pass note validation. Ready for high-stakes review or synthesis workflows; probably too heavy for ordinary note editing.

**Compile compact host-facing projections.** DocMason's `--compact` retrieval and trace guidance is a good model for Commonplace commands that may otherwise dump large JSON or many markdown files into the active context. Ready as CLI output design for future search/review commands.

**Keep interaction memory lower-trust by construction.** DocMason promotes conversation-derived memories into the same retrieval/trace machinery while retaining `source_family`, `trust_tier`, `memory_kind`, durability, uncertainty, and answer-use policy. Commonplace should copy the explicit trust-tier idea before allowing runtime traces to influence durable methodology artifacts.

**Use bounded multimodal follow-up packets.** The Lane B/Lane C pattern around semantic overlays gives agents a finite work packet instead of a vague "inspect the PDF" instruction. Commonplace could use the same shape for source review tasks that need screenshots, PDFs, or rendered artifacts. Needs a concrete multimodal workflow before implementation.

**Separate canonical workflow contracts from generated adapters.** DocMason's `.claude/CLAUDE.md` imports `AGENTS.md` and treats generated adapter files as convenience translations. Commonplace already has similar skill and instruction sources; DocMason reinforces the value of avoiding parallel per-host truths. Ready as a maintenance rule.

**Do not borrow private-runtime state into the library layer by default.** DocMason's local `runtime/` is useful precisely because it is not the public corpus. Commonplace should preserve a workshop/runtime boundary for traces, logs, and interaction capture instead of letting them silently become notes.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `synthesize` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `tool-traces` `event-streams` — Host-agent session starts/ends, user prompts, selected tool uses, stop events, and reconciled native threads are mirrored into interaction entries.

**Learning scope:** `per-project` `cross-task` — Interaction memory is workspace-local and conversation-grouped, then participates in later retrieval and trace across future asks in the same project corpus.

**Learning timing:** `online` `staged` — Hooks capture online, while durable promotion happens at sync time and is published only after validation.

**Distilled form:** `prose` `symbolic` — Turn excerpts, summaries, and copied attachment context are prose; JSONL events, manifests, interaction context, semantic fields, retrieval records, trace records, and promoted-entry markers are symbolic.

**Trace source.** DocMason qualifies as trace-derived learning. The qualifying traces are host-agent session and turn traces: Claude Code hook events mirror session starts/ends, user prompts, selected tool uses, and stop events into JSONL files, and the interaction subsystem also reconciles active Codex or Claude Code native threads into interaction entries (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/hooks.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/interaction.py).

**Extraction.** Extraction is mostly deterministic grouping and projection rather than LLM profile synthesis. Pending interaction entries are grouped by conversation, turn text and assistant excerpts are written into per-turn text assets, attachments are copied, relation hints are preserved, and memory semantics are normalized into `memory_kind`, `durability`, `uncertainty`, `answer_use_policy`, and `retrieval_rank_prior` (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/interaction.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/routing.py). If previous semantic outputs exist, the builder preserves them across rebuilds; otherwise the interaction memory can remain pending semantic output until the sync/knowledge-construction path covers it.

**Four fields.** Raw trace storage is `runtime/interaction-ingest/` JSONL and reconciled runtime entries; durable distilled storage is `knowledge_base/current/interaction/<interaction-memory-id>/` plus derived retrieval and trace records. The representational form moves from structured event traces and conversation prose to mixed prose/symbolic memory directories. Lineage is preserved through conversation IDs, turn IDs, native turn IDs, interaction IDs, copied attachment references, interaction-input digests, fingerprints, and promoted-entry markers. Behavioral authority moves from audit evidence to lower-trust contextual retrieval and trace support; it does not become a hard rule or validator unless a later human or agent promotes it into a canonical skill or workflow contract.

**Scope and timing.** Scope is workspace-local and conversation-grouped. Capture is online through host hooks or thread reconciliation; durable promotion is staged at sync time and published only after validation. Pending interaction memory can affect ask-time governance before promotion as an overlay or blocker, while promoted memories participate in published retrieval and trace as lower-trust sources.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), DocMason belongs in the trace-to-contextual-memory family, not the trace-to-policy or trace-to-fine-tune family. It strengthens the survey claim that a durable behavior-shaping artifact can be file-native and reviewable without model training: the raw trace remains audit material, while the promoted interaction memory becomes a structured, ranked, lower-trust evidence source.

## Read-back placement

**Direction.** DocMason is both pull and push. Public `retrieve` and `trace` are pull tools when an operator or inner workflow deliberately invokes them. From the receiving agent's perspective, canonical `ask` also pushes retained memory surfaces into the turn before answer drafting: warm-start pointers from historical answer records and pending interaction-derived memory notices. Its routed execution metadata, support contracts, and required workflow steps are shipped/system-definition context rather than memory read-back, but they govern how the pushed memory may be used (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical/ask/SKILL.md, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/front_controller.py).

**Read-back signal:** `inferred / lexical` — Warm-start answer evidence and pending interaction relevance key on token overlap and lexical question/memory profiles, with policy gates for corpus signature, question domain, memory kind, answer use, durability, and source scope.

**Faithfulness tested:** `no` — The review found trace/admissibility checks and evaluation support, but no production with/without read-back ablation proving fired memory changed a future answer.

**Targeting and signal.** Push activation is engineered and instance-targeted rather than always-load only. The final memory relevance signal is `inferred / lexical`: `question_execution_profile` normalizes question class/domain, evidence requirements, source-scope intent, and a `memory_query_profile`, then computes warm-start evidence by token overlap against similar historical answer questions under corpus-signature and question-domain constraints (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/front_controller.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/routing.py). Pending interaction activation also keys on lexical overlap, then gates or adjusts the result with memory-kind, answer-use, durability, memory-query profile, source scope, and question-domain policy before it blocks, warns, or participates in retrieval (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/interaction.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/retrieval.py).

**Injection point.** Canonical ask runs before the answer workflow and can route to sync, wait for shared jobs, block, warn, or hand the turn to grounded-answer/composition/retrieval/provenance workflows (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/skills/canonical/ask/SKILL.md). Retrieval and trace happen during the evidence loop, and finalization happens after the answer draft to check support and admissibility.

**Selection, scope, and complexity.** Selection is bounded by top-k retrieval, graph hops, document/source filters, compact projections, source-scope policy, evidence-channel preferences, and question-class/domain routing (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/cli.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/retrieval.py). Interaction memory has additional policy gates through `memory_score_adjustment` and pending-interaction relevance, so contextual-only or ephemeral memories do not automatically dominate ordinary answers.

**Authority at consumption.** Retrieved source and interaction records are advisory evidence until the workflow uses them in an answer. Support contracts, control-plane waits, validation status, final trace, and answer-state commit rules have stronger system-definition authority because they can block or qualify final output. Effective faithfulness still depends on the host agent following the workflow, but the hidden ask finalization path makes that more than a documentation convention.

**Faithfulness.** The implementation includes answer trace/admissibility checks, support-basis contracts, and an evaluation subsystem for retrieval/trace/ask-turn cases, but I did not find a production read-back ablation that proves a fired memory changed a future answer relative to a no-memory condition (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/evaluation.py, https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/src/docmason/operator_eval.py). Structural activation is implemented; behavioral effect quality is runtime evidence, not fully proven from code.

**Other consumers.** Humans can inspect the same published KB, source manifests, trace outputs, answer files, logs, review requests, and evaluation artifacts. Generated host adapters also consume canonical workflow contracts, but those are translations of repo-authored sources rather than separate memory.

## Curiosity Pass

**DocMason is more governance runtime than RAG wrapper.** The retrieval scorer matters, but the distinctive design is the ask lifecycle around it: front-door legality, sync gating, shared-job state, evidence-channel requirements, final trace, answer-state contracts, and admissibility repair.

**The strongest memory mechanism is not a vector store.** The system builds JSON records and graph edges from files, then ranks deterministically. That makes lineage and debugging easier than hidden embedding state, at the cost of relying on lexical/structural matching and agent-authored overlays for harder semantic cases.

**Interaction memory is intentionally demoted.** Promoted interactions join retrieval and trace, but they carry `source_family = interaction-memory`, `trust_tier = interaction`, answer-use policy, uncertainty, and rank priors. That is a healthier design than treating user chat residue as equivalent to source documents.

**The README's "AI app" framing hides a strict local boundary.** DocMason itself makes no model API calls for document reasoning; the host agent supplies LLM reasoning and carries its own privacy boundary (https://github.com/JetXu-LLM/DocMason/blob/f84935b2b7e1e59e64d8ba78066c35d5f55c8559/README.md). That keeps DocMason inspectable, but it means product quality depends heavily on the host following repo contracts.

**Generated adapters are a maintenance risk worth respecting.** The repo tries to keep canonical truth in `AGENTS.md` and canonical skills, with adapters generated from them. If users hand-edit generated adapters, the authority model could fracture.

**The system is alpha but unusually contract-heavy.** Many surfaces are present: source parsing, retrieval, trace, interaction ingest, control plane, evaluation, release bundles, and adapters. The cost is complexity. A future reviewer should check whether ordinary users can stay on canonical `ask` without needing to understand the machinery.

## What to Watch

- Whether interaction memory promotion gains stronger review or user approval before contextual-only chat residue participates in high-stakes answers.
- Whether the evaluation subsystem adds explicit WITH/WITHOUT read-back ablations for interaction memories and warm-start evidence.
- Whether semantic overlays remain additive sidecars or become a de facto second truth surface for complex visual documents.
- Whether generated adapters for Claude, Codex, and other hosts stay synchronized with canonical skills as the workflow surface grows.
- Whether retrieval ranking remains explainable as structure, semantic overlays, graph expansion, interaction memories, and warm-start evidence interact.
- Whether clean/demo bundle update checks remain bounded to release metadata and do not blur the local-only privacy boundary.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: DocMason promotes host interaction traces into lower-trust published interaction memories.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: DocMason combines storage with canonical ask activation, retrieval, trace, and answer-state gates.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: DocMason separates source corpus, published KB, runtime logs, interaction memories, skills, adapters, validation, and trace artifacts by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: source documents, extracted evidence, summaries, logs, traces, and interaction memories serve mainly as evidence, context, or audit material.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: canonical skills, CLI contracts, validation rules, control-plane records, ranking policy, and finalization checks instruct, route, enforce, or evaluate behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: interaction memories are derived from agent/session/tool traces and later consumed by retrieval and trace.
