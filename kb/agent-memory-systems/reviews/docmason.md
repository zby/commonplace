---
description: "DocMason review: repo-native private-document KB with provenance, governed ask, deterministic retrieval, and interaction-memory promotion"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# DocMason

DocMason, from JetXu-LLM's `DocMason` repository, is a repo-native local application for building a provenance-aware knowledge base from private work documents and answering through a host agent such as Codex or Claude Code. The repository is both product and runtime surface: source files go under `original_doc/`, compiled evidence is published under `knowledge_base/current/`, host activity and answer artifacts live under `runtime/`, and canonical agent workflows live as skills inside the repo.

**Repository:** https://github.com/JetXu-LLM/DocMason

**Reviewed commit:** [b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b](https://github.com/JetXu-LLM/DocMason/commit/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b)

**Last checked:** 2026-06-04

## Core Ideas

**The repo is the operating surface, not just storage.** `AGENTS.md` defines DocMason as a repo-native workspace where files, directories, scripts, and skill contracts are the workflow boundary; ordinary questions enter through canonical `ask`, while setup, sync, status, review, and adapter work route to explicit operator workflows ([AGENTS.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/AGENTS.md)). The architecture and workspace helpers make the same boundary concrete: `original_doc/` is private source input, `knowledge_base/current/` is published truth, and `runtime/` holds local execution, answers, logs, control-plane state, and interaction ingest ([docs/architecture/README.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/docs/architecture/README.md), [src/docmason/project.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/project.py)).

**The stable public CLI separates deterministic operations from agent reasoning.** The public parser exposes `prepare`, `doctor`, `status`, `sync`, `retrieve`, `trace`, `validate-kb`, `sync-adapters`, `update-core`, and `workflow`; hidden `_ask` and `_hook` entrypoints are internal host-integration plumbing ([src/docmason/cli.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/cli.py)). This is the main authority split: setup, sync, validation, retrieval, trace, and turn finalization are symbolic system-definition surfaces, while the host LLM supplies the reasoning runtime.

**Document ingestion compiles private files into structured evidence bundles.** Supported inputs cover Office, PDF, markdown/plain text, email, and lightweight text formats; Office conversion depends on local LibreOffice and PDF extraction uses local Python libraries ([src/docmason/project.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/project.py), [pyproject.toml](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/pyproject.toml)). Sync builds source manifests, evidence manifests, extracted unit text, structure JSON, render references, artifact indexes, semantic overlays, retrieval artifacts, and trace artifacts ([src/docmason/knowledge.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/knowledge.py), [src/docmason/evidence_artifacts.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/evidence_artifacts.py), [src/docmason/retrieval.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/retrieval.py)).

**Context efficiency is handled by compiled records and compact host projections.** Retrieval ranks source, unit, and artifact records with lexical field weights, unit matches, artifact matches, graph expansion, trust/citation signals, semantic overlay signals, and interaction-memory policy; the CLI provides `--top`, `--graph-hops`, document/source filters, `--include-renders`, and `--compact` so a host can inspect a bounded projection before escalating to nested evidence ([src/docmason/retrieval.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/retrieval.py), [src/docmason/commands.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/commands.py), [skills/canonical/grounded-answer/SKILL.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/skills/canonical/grounded-answer/SKILL.md)). The design is not "load the corpus"; it is staged retrieval, compact inspection, and render/source escalation only when needed.

**Answer admissibility is a runtime contract.** Canonical `ask` opens a governed turn, routes to an inner workflow, binds retrieve/trace activity to that turn, and requires finalization before a final business answer may be returned ([skills/canonical/ask/SKILL.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/skills/canonical/ask/SKILL.md)). Committed turns must declare `answer_state` and `support_basis`, with allowed answer states of `grounded`, `partially-grounded`, `unresolved`, and `abstained` ([src/docmason/contracts.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/contracts.py)). This makes provenance and admissibility part of the action path, not just a post-hoc report.

**Host interactions become a second, lower-trust memory source.** Claude Code hooks mirror session, prompt, selected tool-use, stop, and session-end events into `runtime/interaction-ingest/claude-code`; DocMason also has native reconciliation helpers for Codex/Claude transcript state ([.claude/settings.json](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/.claude/settings.json), [src/docmason/hooks.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/hooks.py), [src/docmason/interaction.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/interaction.py)). Sync groups pending interaction entries by conversation into `interaction-memory-*` directories with turn text, attachment copies, manifests, `interaction_context.json`, `knowledge.json`, `summary.md`, affordances, and memory semantics such as `memory_kind`, `durability`, `answer_use_policy`, and `retrieval_rank_prior` ([src/docmason/interaction.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/interaction.py)).

## Artifact analysis

- **Storage substrate:** `files` — DocMason's durable retained state is file-backed: private source files under `original_doc/`, published evidence under `knowledge_base/current/`, runtime turn/log/control-plane/interaction state under `runtime/`, repo-tracked canonical skills and contracts, generated adapter files, sample-corpus fixtures, and distribution/update metadata. The repo itself supplies versioned code and workflow truth, but the operative memory substrate is still the local filesystem rather than a database, vector store, or service object.
- **Representational form:** `prose` `symbolic` — Source texts, summaries, answer files, turn excerpts, skills, and workflow docs are prose; manifests, JSON/JSONL state, source IDs, fingerprints, graph edges, retrieval records, trace records, contracts, validation reports, workflow metadata, and hook events are symbolic. I did not find parametric memory such as embeddings, learned weights, or a vector index in the reviewed source.
- **Lineage:** `authored` `imported` `trace-extracted` — Canonical skills, contracts, docs, and code are authored repository state; private work documents and sample corpus files are imported inputs; interaction memories are derived from host session, prompt, tool-use, stop, native transcript, attachment, and answer-turn traces. Published KB artifacts are derived and regenerable from sources plus sync-time state.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Source evidence, summaries, traces, logs, answers, and interaction memories advise as knowledge; canonical skills and `AGENTS.md` instruct; ask/finalization rules, support contracts, control-plane states, workspace trust checks, and validation failures enforce; workflow routing, source-scope policy, memory query profiles, and adapters route; validation and trace check support; retrieval scores, graph promotion, trust/citation bonuses, memory rank priors, and warm-start matching rank attention; interaction promotion turns execution traces into retained memory.

**Private source corpus.** The storage substrate is the local workspace under `original_doc/`; distribution docs explicitly separate private user corpus state from public sample fixtures and warn against committing `original_doc/`, `knowledge_base/`, or `runtime/` ([README.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/README.md), [docs/product/distribution-and-benchmarks.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/docs/product/distribution-and-benchmarks.md)). The retained source artifacts are imported evidence, not direct agent instructions; they gain answer-time force only after sync, retrieval, trace, and workflow use.

**Published knowledge base.** `knowledge_base/current/` is generated from staging and versioning paths under `knowledge_base/`, with manifests, extracted units, render assets, artifact indexes, affordances, optional semantic overlays, retrieval artifacts, and trace artifacts ([src/docmason/project.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/project.py), [src/docmason/versioning.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/versioning.py), [src/docmason/knowledge.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/knowledge.py)). Its authority is mostly knowledge at answer time, with stronger validation, ranking, and provenance authority in the generated symbolic surfaces.

**Canonical skills and agent contracts.** `AGENTS.md`, `.claude/CLAUDE.md`, and `skills/canonical/*/SKILL.md` are authored prose/symbolic system-definition artifacts ([AGENTS.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/AGENTS.md), [skills/canonical/ask/SKILL.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/skills/canonical/ask/SKILL.md), [skills/canonical/knowledge-construction/SKILL.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/skills/canonical/knowledge-construction/SKILL.md)). They route ordinary and operator work, constrain evidence handling, define completion legality, and tell compatible hosts which entry surfaces are canonical.

**Runtime asks, logs, traces, and answers.** The runtime directories hold answer files, runs, logs, control-plane records, state, interaction ingest, and agent work ([src/docmason/project.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/project.py)). These artifacts mix audit knowledge with system-definition authority: logs and traces are evidence for humans and agents, while control-plane state, support contracts, answer-state validation, and finalization rules can block or qualify the final answer ([src/docmason/front_controller.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/front_controller.py), [src/docmason/contracts.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/contracts.py), [src/docmason/retrieval.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/retrieval.py)).

**Interaction-derived memories.** Raw host activity begins as JSONL mirrors, native ledger entries, attachments, and reconciled interaction entries under `runtime/interaction-ingest/`; durable promoted memories are generated under `knowledge_base/<target>/interaction/<interaction-memory-id>/` with manifests, extracted turn text, structures, copied attachments, `interaction_context.json`, `knowledge.json`, `summary.md`, affordances, and work items ([src/docmason/hooks.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/hooks.py), [src/docmason/interaction.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/interaction.py)). The lineage is preserved through conversation IDs, turn IDs, native turn IDs, interaction IDs, input digests, fingerprints, and promoted-entry markers. The authority remains deliberately lower than source evidence through `source_family = interaction-memory`, `trust_tier = interaction`, memory semantics, and retrieval policy.

**Promotion path.** DocMason's core promotion path is source or trace material -> staging artifacts -> validation -> published KB -> retrieval/trace records -> governed answer support. The trace-derived path is host interaction entry -> grouped interaction memory directory -> semantic/trust metadata -> published retrieval/trace participation -> answer-time advisory context. It does not train a model or write opaque vector state; promotion stays file-native and inspectable.

## Comparison with Our System

| Dimension | DocMason | Commonplace |
|---|---|---|
| Primary purpose | Local private-document research app with governed answers and provenance | Methodology KB framework for agent-operated knowledge bases |
| Canonical substrate | Repo workspace plus private `original_doc/`, generated `knowledge_base/current/`, and local `runtime/` | Git-tracked `kb/` collections, type specs, validation, indexes, sources, reviews, and instructions |
| Ingestion | Compiles Office/PDF/text/email into manifests, units, render/structure/artifact evidence, retrieval, and trace | Authors or snapshots markdown artifacts, then validates collection/type contracts |
| Read path | Canonical `ask`, retrieve, trace, warm-start evidence, interaction-memory policy, and compact projections | `rg`, indexes, skills, reports, authored links, and explicit review/workflow commands |
| Trace-derived learning | Promotes host interactions into lower-trust interaction memories and retrieval/trace inputs | Uses review/workshop artifacts; no automatic conversation-to-library promotion by default |
| Governance | Strong runtime gates for answer legality, sync, support contracts, source scope, and provenance | Strong artifact contracts, schema validation, review gates, and git-native lifecycle |

DocMason and Commonplace share a filesystem-first instinct, but DocMason is a product runtime for private corpora while Commonplace is a methodology library and framework. DocMason deliberately keeps much of its durable operational state ignored and local. Commonplace makes most durable knowledge artifacts git-native and reviewable by default.

The strongest alignment is the explicit separation between knowledge artifacts and system-definition artifacts. DocMason keeps source evidence, compiled summaries, render assets, and interaction memories distinct from workflow contracts, validation rules, answer-state contracts, control-plane gates, and retrieval policy. Commonplace uses the same split in collection contracts, type specs, validators, review bundles, and instructions.

The main divergence is that DocMason gives the answer runtime more power. Canonical ask owns turn opening, workspace gating, routing, support contracts, retrieval/trace binding, final answer state, and finalization. Commonplace usually leaves more of that path to agent instructions, deterministic validation, and human-visible Markdown review. DocMason is therefore a useful example of making a KB not just searchable, but operationally binding at answer time.

### Borrowable Ideas

**Treat answer legality as a runtime contract.** Ready for high-stakes review or synthesis workflows. Commonplace has validation and review gates, but DocMason's `answer_state` plus `support_basis` finalization model is sharper for workflows where an agent must emit a grounded final answer.

**Compile compact host-facing projections.** Ready as CLI output design. DocMason's compact retrieve and trace payloads are a good model for Commonplace commands that may otherwise dump large JSON, many notes, or nested evidence into active context.

**Keep interaction memory lower-trust by construction.** Ready as a prerequisite, not as an automatic feature. DocMason promotes conversation-derived memories into retrieval/trace machinery while retaining `source_family`, `trust_tier`, `memory_kind`, durability, uncertainty, answer-use policy, and rank prior. Commonplace should copy that trust-tier discipline before allowing runtime traces to influence durable methodology artifacts.

**Use bounded multimodal follow-up packets.** Needs a concrete Commonplace workflow. DocMason's semantic-overlay and hybrid-refresh machinery turns a hard-artifact gap into a finite work packet rather than a vague instruction to inspect a PDF, slide, or image.

**Separate canonical workflow contracts from generated adapters.** Ready as a maintenance rule. DocMason treats generated adapter guidance as a convenience layer around canonical skills and `AGENTS.md`, which reinforces Commonplace's preference for one authoritative source rather than parallel per-host truths.

**Do not borrow private runtime state into the library layer by default.** Ready as a guardrail. DocMason's `runtime/` is useful precisely because it is local operational state, not the public corpus. Commonplace should preserve the workshop/runtime boundary for traces, logs, and interaction capture.

## Write side

**Write agency:** `manual` `automatic` — Users and operators manually add source files, edit canonical workflow/docs/code, run setup/sync/review workflows, and author semantic overlay or answer artifacts through the host; automatic writes build staging/current KB artifacts, retrieval/trace artifacts, runtime answers/logs/control-plane records, hook mirrors, interaction entries, interaction-memory directories, projection snapshots, generated adapters, and update metadata.

**Curation operations:** `promote` — DocMason promotes pending interaction entries into published interaction memories, marks entries as promoted after successful publish, and carries promoted memories into retrieval/trace surfaces. It also validates, rebuilds, publishes, and repairs derived access structures, but those are provenance/access-structure upkeep rather than semantic curation operations such as deduplication, decay, or in-place evolution.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Claude hooks capture session starts/ends, user prompts, selected tool uses, stop events, and diagnostics; native reconciliation helpers also derive entries from Codex and Claude transcript state.

**Learning scope:** `per-project` `cross-task` — Interaction memory is workspace-local and conversation-grouped, then participates in later ask/retrieve/trace flows in the same project corpus. Generated connector and adapter mechanisms can seed future compatible-host operation, but the retained memories themselves are local to the workspace.

**Learning timing:** `online` `staged` — Hooks and native reconciliation capture traces during operation; durable promotion happens during sync and publish, after grouping, metadata normalization, validation, and publication.

**Distilled form:** `prose` `symbolic` — Turn excerpts, summaries, and copied attachment context are prose; JSONL events, manifests, structures, `interaction_context.json`, memory semantics, retrieval records, trace records, and promoted-entry markers are symbolic.

**Extraction.** Extraction is mostly deterministic grouping and projection, not an LLM-written profile. Pending entries are grouped by conversation, turn text and assistant excerpts are written as extracted units, attachments are copied, relation hints are preserved, memory semantics are normalized, and previous semantic outputs can be preserved across rebuilds ([src/docmason/interaction.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/interaction.py), [src/docmason/routing.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/routing.py)).

**Scope and timing.** The raw unit is an interaction entry from a host turn or event stream. The durable unit is a conversation-grouped `interaction-memory-*` directory. Capture can happen online, but promotion is staged through sync; after publication, `mark_promoted_interaction_entries()` flips pending entries to promoted and records the promoted memory id ([src/docmason/interaction.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/interaction.py)).

**Survey fit.** DocMason belongs in the trace-to-contextual-memory family, not the trace-to-policy or trace-to-fine-tune family. It strengthens the survey claim that durable behavior-shaping artifacts can stay file-native and reviewable: raw traces remain audit material, while promoted interaction memories become structured, ranked, lower-trust evidence sources.

## Read-back

**Read-back:** `both` — DocMason is pull through explicit `retrieve`, `trace`, source/KM inspection, and operator workflows; it is push when canonical `ask` computes warm-start evidence from similar historical answers and allows pending or promoted interaction memory to participate in answer-time retrieval/trace without the receiving agent independently requesting that specific memory.

**Read-back signal:** `inferred / lexical` — Warm-start evidence uses token overlap against historical questions under corpus-signature and question-domain constraints, and interaction-memory participation is governed by lexical source/unit matches plus memory-query profile, question domain, answer-use policy, memory kind, rank prior, and source-scope policy ([src/docmason/front_controller.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/front_controller.py), [src/docmason/retrieval.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/retrieval.py)).

**Faithfulness tested:** `no` — The repository tests retrieval, trace, ask, interaction ingest, review, and evaluation machinery, but I did not find a production with/without ablation proving that fired warm-start evidence or interaction memory changes host-agent behavior.

**Direction edge cases.** `AGENTS.md` and canonical skills are baseline instruction and do not by themselves count as memory read-back. The memory-specific push path is in canonical ask and retrieval policy: a new ask can receive historical answer evidence pointers and interaction-memory records selected by the routed execution profile, memory profile, and retrieval scoring.

**Targeting and signal.** Pull selection is deliberate: the host or operator invokes public retrieve/trace, reads files, or opens workflow surfaces. Push selection is inferred lexical plus policy gates. `warm_start_evidence()` chooses previous answer records by token overlap, question domain, and corpus signature; `should_merge_pending_interaction()` and `memory_score_adjustment()` decide whether interaction memories or pending overlays are allowed and how they affect ranking ([src/docmason/front_controller.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/front_controller.py), [src/docmason/retrieval.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/retrieval.py)).

**Injection point.** The push read occurs before the next model-facing answer work. Canonical ask opens or reuses a governed turn, computes the routed execution profile, returns support contracts and warm-start evidence, then sends the host through the inner workflow; retrieve and trace are bound to the same turn before finalization ([skills/canonical/ask/SKILL.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/skills/canonical/ask/SKILL.md), [src/docmason/front_controller.py](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/src/docmason/front_controller.py)).

**Selection, scope, and complexity.** Selection is bounded by top-k source results, graph hops, source/document filters, source-scope policy, compact projections, memory-query profile, memory rank priors, evidence requirements, and optional render inclusion. Complexity is controlled by progressive disclosure: compact JSON first, nested evidence only when necessary, and render inspection only for genuinely visual/layout-sensitive gaps.

**Authority at consumption.** Retrieved source and interaction records are advisory evidence until an answer workflow uses them. Support contracts, control-plane waits, validation status, final trace, and answer-state commit rules carry stronger system-definition authority because they can block, route, repair, or qualify final output. Effective behavioral uptake still depends on the host agent following the workflow.

**Other consumers.** Humans can inspect the same published KB, source manifests, trace outputs, answer files, logs, review requests, evaluation artifacts, and generated adapter files. DocMason is therefore both an agent-facing memory layer and an operator-facing provenance/audit tool.

## Curiosity Pass

**DocMason is more governance runtime than RAG wrapper.** The retrieval scorer matters, but the distinctive design is the ask lifecycle around it: front-door legality, workspace gating, source-scope policy, support contracts, final trace, answer-state contracts, and admissibility repair.

**The strongest memory mechanism is not a vector store.** The system builds JSON records, graph edges, and file-native interaction memories, then ranks deterministically. That makes lineage and debugging easier than hidden embedding state, at the cost of relying on lexical/structural matching and agent-authored overlays for harder semantic cases.

**Interaction memory is intentionally demoted.** Promoted interactions join retrieval and trace, but they carry `source_family = interaction-memory`, `trust_tier = interaction`, answer-use policy, uncertainty, durability, kind, and rank prior. That is healthier than treating chat residue as equivalent to source documents.

**The local boundary is strict but not total privacy by itself.** DocMason itself makes no model API calls for document reasoning, but the host agent supplies LLM reasoning and has its own telemetry/privacy boundary; the repo also documents a bounded release-bundle update check that is separate from corpus ingestion ([README.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/README.md), [docs/policies/release-entry-and-networking.md](https://github.com/JetXu-LLM/DocMason/blob/b3e3e0ea0937309b4218f7ebf77bf72641fc1a5b/docs/policies/release-entry-and-networking.md)).

**Generated adapters remain a maintenance risk.** The repo tries to keep canonical truth in `AGENTS.md` and canonical skills, with adapters generated from that source. If users hand-edit generated adapters, the authority model could fracture.

## What to Watch

- Whether interaction memory promotion gains stronger review or user approval before contextual-only chat residue participates in high-stakes answers.
- Whether the evaluation subsystem adds explicit with/without read-back ablations for interaction memories and warm-start evidence.
- Whether semantic overlays remain additive sidecars or become a de facto second truth surface for complex visual documents.
- Whether generated adapters for Claude, Codex, Copilot, and other hosts stay synchronized with canonical skills as the workflow surface grows.
- Whether retrieval ranking remains explainable as structure, semantic overlays, graph expansion, interaction memories, warm-start evidence, and source-scope policy interact.
- Whether the clean/demo bundle update check stays bounded to release metadata and does not blur the local-only privacy boundary.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: DocMason promotes host interaction traces into lower-trust published interaction memories.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: DocMason combines storage with canonical ask read-back, retrieval, trace, and answer-state gates.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: source corpus, published KB, runtime logs, interaction memories, skills, adapters, validation, and trace artifacts differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: source documents, extracted evidence, summaries, logs, traces, and interaction memories mostly serve as evidence, context, or audit material.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: canonical skills, CLI contracts, validation rules, control-plane records, ranking policy, and finalization checks instruct, route, enforce, or evaluate behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: interaction memories are derived from agent/session/tool traces and later consumed by retrieval and trace.
