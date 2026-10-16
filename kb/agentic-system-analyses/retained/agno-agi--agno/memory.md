---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Agno memory and context: session replay, user-memory admission, six learning stores, knowledge retrieval, compaction archives and result offload."
run-id: AAS-2026-10-13-agno-60e6e09dd4a6-01
source-identity: "https://github.com/agno-agi/agno"
reviewed-boundary: "00497422d4a386d93ab3b45c1a11faf42fcc932f"
---

# Agno memory report

## Boundary and evidence

This report examines retained state and working-context control inside Agno's SDK/AgentOS subsystem at the revision fixed by [boundary](boundary.md). All findings use SRC-1, implementation unless labelled doctrine/design. No target execution, tests, provider calls or outcome traces were used. Implementation wiring is not observed recall, summary fidelity, effective deletion or improved performance.

Memory scope includes sessions and summaries, MemoryManager, all six built-in LearningMachine stores, knowledge insertion/retrieval and managed pages, compaction, compression and tool-result offload. Static skills are included as working-context selection, not automatically called retained memory. Team/workflow context isolation and configuration admission use supplied runtime findings. The terminal CLI, provisioning and hosted UI remain excluded under the boundary; SDK console dispatch is already explained there. AgentOS editing operations are inside this boundary, not hypothetical external consumers.

The following inventory distinguishes new direct source reads from supplied runtime evidence. Rows with unresolved details retain the missing facts; they do not imply those mechanisms are absent. Paths are commit-relative under SRC-1.

| Surface or operation | Inspected path or supplied evidence | Coverage and remaining limit |
|---|---|---|
| Agent session load, separate session/run writes, history replay | `libs/agno/agno/agent/_session.py`; supplied [RT-RTE-agent-run](runtime.md#rt-rte-agent-run), [RT-RTE-context-window](runtime.md#rt-rte-context-window) | Direct storage seams and supplied replay policy; [MEM-OBJ-agent-session](#mem-obj-agent-session). Full storage scrubbing, every backend and workflow checkpoint/resume selection remain uninspected; no complete retention or replay-equivalence guarantee. |
| Session summary production and system delivery | `libs/agno/agno/session/summary.py`, `libs/agno/agno/agent/_messages.py` | [MEM-RTE-session-summary](#mem-rte-session-summary); separate from compaction and learning session context. |
| Automatic user extraction, agentic memory tool, direct API, optimization | `libs/agno/agno/agent/_managers.py`, `libs/agno/agno/agent/_default_tools.py`, `libs/agno/agno/memory/manager.py` | [MEM-RTE-user-memory](#mem-rte-user-memory); automatic input is user-message/extra-message content, not necessarily a completed interaction. Optimization internals/custom strategies unresolved. |
| AgentOS memory create/edit/delete/optimize and learning-row edits | `libs/agno/agno/os/routers/memory/memory.py`, `libs/agno/agno/os/routers/learnings/router.py` | [MEM-RTE-memory-editing](#mem-rte-memory-editing). Direct create/update and learning update/delete bodies read; memory delete/optimize dispatch searched. Full remote enforcement and all router security combinations uninspected. |
| LearningMachine automatic and manually placed doors, capture hooks/tools | `libs/agno/agno/learn/machine.py`, `libs/agno/agno/agent/_managers.py`, `libs/agno/agno/agent/_tools.py` | Direct process/recall/render and background snapshot reads; tool/hook method inventory searched. [MEM-RTE-learning-context](#mem-rte-learning-context). Full capture-hook implementation not read; manual caller-specific final-trace coverage unresolved. |
| UserProfileStore | `libs/agno/agno/learn/stores/user_profile.py` | Direct process/recall/render/extract reads, persistence search; [MEM-OBJ-user-profile](#mem-obj-user-profile), [MEM-RTE-profile-extraction](#mem-rte-profile-extraction). Custom schema validation and every field-update tool unresolved. |
| UserMemoryStore | `libs/agno/agno/learn/stores/user_memory.py` | Direct process/recall/render/extract reads, persistence search; [MEM-OBJ-memories](#mem-obj-memories), [MEM-RTE-memories-extraction](#mem-rte-memories-extraction). Individual add/update/remove merge checks not fully read. |
| SessionContextStore | `libs/agno/agno/learn/stores/session_context.py` | Direct process/recall/render/extract reads, persistence search; [MEM-OBJ-session-context](#mem-obj-session-context), [MEM-RTE-context-extraction](#mem-rte-context-extraction). Summary/planning tool granularity unresolved. |
| LearnedKnowledgeStore | `libs/agno/agno/learn/stores/learned_knowledge.py` | Direct mode guidance, save tool, extraction, save and display reads; [MEM-RTE-learned-knowledge](#mem-rte-learned-knowledge). Deletion/title matching and parsed-result reconstruction not fully traced. |
| EntityMemoryStore | `libs/agno/agno/learn/stores/entity_memory.py`, `libs/agno/agno/learn/schemas.py` | Direct directory/relevance recall, render, supersession and forget reads; schema/persistence/tool methods searched. [MEM-RTE-entity-memory](#mem-rte-entity-memory). Judge prompt, name resolution, relationship reciprocity and concurrency machinery not exhaustively inspected. |
| DecisionLogStore | `libs/agno/agno/learn/stores/decision_log.py` | Direct log tool, recall/render/no-op process; save/outcome methods searched. [MEM-RTE-decision-memory](#mem-rte-decision-memory). Outcome quality is stored reporting, not an independently verified oracle. |
| Curator | `libs/agno/agno/learn/curate.py` | Entire file read; [MEM-RTE-profile-curation](#mem-rte-profile-curation). Only user_profile is selected, and only a profile exposing memories is changed. |
| Vector knowledge, custom retrievers and automatic versus tool retrieval | `libs/agno/agno/knowledge/knowledge.py`, `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/agent/_default_tools.py`, `libs/agno/agno/agent/_tools.py` | Direct retrieval, search, write and deletion seams; [MEM-RTE-knowledge-context](#mem-rte-knowledge-context). Reader/chunker variants, remote services and all vector adapters remain unresolved; no uniform access-control or embedding provenance guarantee. |
| Managed-page sync/publication/pruning; chat/MCP search | `libs/agno/agno/knowledge/page/_coordinator.py`, `libs/agno/agno/knowledge/page/tools.py` | Direct publish/sync/prune and search-tool reads; [MEM-RTE-page-knowledge](#mem-rte-page-knowledge). Search ranking SQL, full-page snapshot validation and all source discovery adapters uninspected. |
| FileSystemKnowledge | `libs/agno/agno/knowledge/filesystem.py` | Direct retrieve body, other entry points searched: grep-based retrieve; file list/get/grep tools exposed. Included alternative with unresolved matching/path-policy detail; no claim of semantic selection or framework-controlled file authoring. |
| Compaction, archive, manual/overflow folds and reload | Supplied [RT-RTE-context-window](runtime.md#rt-rte-context-window); direct `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/compaction/archive.py`, `libs/agno/agno/compaction/compaction.py` | Annotation and [MEM-OBJ-compaction-archive](#mem-obj-compaction-archive). Archives clip tool messages and depend on DB support. Complete backend expiry/deletion policy remains unresolved. |
| Tool compression | `libs/agno/agno/compression/manager.py`, `libs/agno/agno/models/message.py`, `libs/agno/agno/models/base.py` | Direct compression reads and message serialization/integration searches; [MEM-RTE-tool-compression](#mem-rte-tool-compression). Provider-specific compressed-content consumption not audited; no universal later replay claim. |
| Tool-result offload and on-demand read-back, TTL | `libs/agno/agno/offload/store.py`, `libs/agno/agno/offload/tools.py`; registration/model integration search above | [MEM-RTE-result-offload](#mem-rte-result-offload). Payload is distinct from index row and preview; full filesystem/backend quota implementation unresolved. |
| Skills progressive loading | `libs/agno/agno/skills/agent_skills.py`, `libs/agno/agno/agent/_messages.py` | Direct summary snippet and method inventory; static name/description first, instructions/reference/script tools on demand. No inspected trace-fed skill revision or frame-pop route; script safety/loader invalidation unresolved. |
| Team/workflow isolation and configuration revision | Supplied [RT-RTE-team-delegation](runtime.md#rt-rte-team-delegation), [RT-RTE-workflow-step](runtime.md#rt-rte-workflow-step), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) | Separate selected contexts, returned values/state and configuration reconstruction already recorded. Alternate task-board/broadcast/fork/checkpoint routes not directly inspected here. |
| Media offload, provider caches, opaque model/provider state, trace/evaluation records | Runtime persistence/adapter seams; `libs/agno/agno/utils/media_offload.py` and evaluation/router paths discovered, not body-inspected | Included unresolved alternatives: media reconstruction, cache eviction and evaluation-to-memory write linkage unknown. Prevents a complete all-payload replay or evaluator-driven improvement account. Raw tracing/evaluation storage is not assumed to be derived memory. |

## Core ideas

Agno has several independent retention horizons. A session stores runs/state and may store a summary. MemoryManager retains user facts across sessions. LearningMachine combines user, session, entity, decision and reusable-insight stores. Knowledge can contain caller-ingested sources or model-authored results. These do not share one content-admission mechanism. [MEM-RTE-user-memory](#mem-rte-user-memory), [MEM-RTE-learning-context](#mem-rte-learning-context), [MEM-RTE-knowledge-context](#mem-rte-knowledge-context).

Context delivery is also plural. User memories and learning blocks are automatically selected before inference; tool searches request additional content. User/profile lookup is principally identity-based, whereas learned knowledge uses the current message as a query and entity recall expands selected entities beside a bounded directory. Storing everything does not imply showing everything. [MEM-RTE-learning-context](#mem-rte-learning-context), [MEM-RTE-entity-memory](#mem-rte-entity-memory).

Context reduction has different reversibility. Compaction replaces a prefix with summary/tail without rewriting session history, but its separate archive is a clipped display transcript, not always the full original payload. Offload stores a payload and exposes a preview plus explicit read/search tools. Compression produces another text field and can remove uncertainty language by instruction. None proves semantic preservation. [MEM-OBJ-compaction-archive](#mem-obj-compaction-archive), [MEM-RTE-result-offload](#mem-rte-result-offload), [MEM-RTE-tool-compression](#mem-rte-tool-compression).

Source trust is mostly expressed as model guidance: current conversation takes precedence over stored user information. This is not a verified freshness or truth predicate. Likewise PROPOSE mode asks the model to obtain approval; the inspected save-learning function itself accepts content without an approval argument. [MEM-RTE-learned-knowledge](#mem-rte-learned-knowledge).

## Shared records

### Components

#### MEM-CMP-memory-model
Label: MemoryManager extraction and optimization model

Source-native identity: MemoryManager.model/get_model. Form: distributed-parametric provider inference; model settings are symbolic, capture instructions natural language. Substrate: provider-managed weights, local configuration. Parameters changing during operation: provider internals uninspected; inspected calls perform inference, not training. Exact version pinned: not established. Mutable endpoint resolving to another model: caller configuration and provider aliases remain unresolved. Distinct from foreground [RT-CMP-gemini](runtime.md#rt-cmp-gemini) and compaction [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model): different role, not proof of different weights. SRC-1: `libs/agno/agno/memory/manager.py`.

> response = model_copy.response(
>     messages=messages_for_model,
>     tools=_tools,
> )
> --- `libs/agno/agno/memory/manager.py:1095-1099`

#### MEM-CMP-learning-model
Label: Learning-store extraction and judgment models

Source-native identity: configured store.model, inherited/configured through LearningMachine stores; this is a configurable role family, not a single deployed model identity. Form: distributed-parametric inference consuming text and producing text/tool proposals. Substrate: provider weights and local Model configurations. Parameters changing: inaccessible provider internals, no inspected weight-update route. Exact version pinned: unresolved per caller/store. Mutable endpoint: configuration can differ per store and provider aliases remain uninspected. No matching supplied component: closest [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model) serves a different transformation. SRC-1: `libs/agno/agno/learn/machine.py`, `libs/agno/agno/learn/stores/user_memory.py`, `libs/agno/agno/learn/stores/entity_memory.py`.

> model_copy = deepcopy(self.model)
> response = model_copy.response(
>     messages=messages_for_model,
>     tools=functions,
>     tool_call_limit=self.config.max_updates_per_run,
> )
> --- `libs/agno/agno/learn/stores/user_memory.py:728-800`

#### MEM-CMP-summary-model
Label: Session summary model

Source-native identity: SessionSummaryManager.model. Form: distributed-parametric inference to natural-language summary plus structured topics. Substrate: provider weights/local settings. Parameters changing: provider internals uninspected; code requests inference. Exact version pin: not established. Mutable endpoint: caller/provider-dependent. Distinct from [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model); it updates session.summary, not a fold boundary. SRC-1: `libs/agno/agno/session/summary.py`.

> summary_response = self.model.response(messages=messages, response_format=response_format)
> --- `libs/agno/agno/session/summary.py:242-294`

#### MEM-CMP-compression-model
Label: Tool-result compression model

Source-native identity: CompressionManager.model. Form: distributed-parametric inference to condensed natural language. Substrate: provider weights/local settings. Parameters changing: no inspected training; provider internals uninspected. Exact version pin: not established. Mutable endpoint: configuration/provider-dependent. Distinct from [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model); individual tool results are transformed. SRC-1: `libs/agno/agno/compression/manager.py`.

> self.model = get_model(self.model)
> if not self.model:
>     log_warning("No compression model available")
>     return None
> --- `libs/agno/agno/compression/manager.py:105-141`

#### MEM-CMP-openai-embedder
Label: OpenAI embedding adapter alternative

Source-native identity: OpenAIEmbedder, default ID text-embedding-3-small. Form: distributed-parametric provider model and generated dense vectors; ID/dimensions/configuration symbolic. Substrate: provider weights, local settings and vector-store outputs. Parameters changing: provider internals uninspected; adapter requests embeddings, not training. Exact version pinned: no immutable weight digest. Mutable endpoint: configurable base_url/model ID; alias stability unresolved. This establishes an available embedding role, not activation in every knowledge route. No supplied counterpart after comparing [RT-CMP-gemini](runtime.md#rt-cmp-gemini). SRC-1: `libs/agno/agno/knowledge/embedder/openai.py`.

> id: str = "text-embedding-3-small"
> dimensions: Optional[int] = None
> encoding_format: Literal["float", "base64"] = "float"
> --- `libs/agno/agno/knowledge/embedder/openai.py:23-36`

### Operative objects

#### MEM-OBJ-agent-session
Label: AgentSession retained runs, summary and state

Source-native identity: AgentSession loaded by session/user ID; session row and individual RunOutput rows. Form: symbolic identities/order/status/state keys; embedded messages and summary are natural-language content. Substrate: configured database, optional full-session in-process cache. Lineage: runtime inputs, assistant/tool messages, outputs and state mutations; summary has separate derivation. Raw traces are distinct from summary/state interpretation. User identity scopes the load; it is not a per-content approval record. Distinct from in-process [RT-OBJ-run-context](runtime.md#rt-obj-run-context), overlapping the persistence leg of [RT-RTE-agent-run](runtime.md#rt-rte-agent-run). Later consumers: history replay/continuation, optional summary/state prompt supply. Complete storage-copy scrubbing and media reconstruction remain unresolved. SRC-1: `libs/agno/agno/agent/_session.py`.

> Runs are persisted separately via ``save_run()``. This function writes
> only the session row.
> --- `libs/agno/agno/agent/_session.py:231-261`

#### MEM-OBJ-user-memory
Label: MemoryManager UserMemory rows

Source-native identity: UserMemory keyed by memory_id/user_id. Form: natural-language memory/input text inside symbolic IDs/topics/timestamps and provenance fields. Substrate: configured memory DB; get_user_memories refreshes from DB. Lineage: direct supplied memory or model extraction of input. Later consumer: memory text alone is iterated into the system message, not the whole metadata/input record. Cross-session horizon follows user ID; fallback default is a shared logical identity, not inferred authentication. Distinct from [MEM-OBJ-memories](#mem-obj-memories), which uses the learning-row store; no supplied object counterpart after [RT-OBJ-run-context](runtime.md#rt-obj-run-context). SRC-1: `libs/agno/agno/memory/manager.py`, `libs/agno/agno/agent/_messages.py`.

> for _memory in user_memories:  # type: ignore
>     system_message_content += f"\n- {_memory.memory}"
> --- `libs/agno/agno/agent/_messages.py:1070-1211`

#### MEM-OBJ-user-profile
Label: UserProfile learning row

Source-native identity: UserProfileStore schema instance keyed by user-derived learning ID, type user_profile. Form: symbolic schema/identity; profile values receive natural-language interpretation in displayed fields. Substrate: DB learning row via upsert_learning. Lineage: caller save/edit or conversation extraction/update tools. Render selects truthy updateable fields, not every stored field or audit metadata. Later consumer: foreground system context across user sessions; current-conversation precedence is guidance. Distinct from MemoryManager rows and supplied [RT-OBJ-run-context](runtime.md#rt-obj-run-context). SRC-1: `libs/agno/agno/learn/stores/user_profile.py`.

> for field_name in updateable_fields:
>     value = getattr(data, field_name, None)
>     if value:
>         profile_parts.append(f"{field_name.replace('_', ' ').title()}: {value}")
> --- `libs/agno/agno/learn/stores/user_profile.py:184-233`

#### MEM-OBJ-memories
Label: UserMemoryStore Memories learning row

Source-native identity: Memories schema held by UserMemoryStore, deterministic user-derived learning ID and type user_memory. Form: natural-language memory contents plus symbolic row identity/list/time fields. Substrate: DB learning row. Lineage: extraction or explicit updates, not raw conversation storage. Later consumer: rendered get_memories_text or content bullets in system context; stored audit metadata is not automatically shown. Individual memories' exact source/reason retention and merge behavior remain unresolved. No supplied counterpart after [RT-OBJ-run-context](runtime.md#rt-obj-run-context); distinct from [MEM-OBJ-user-memory](#mem-obj-user-memory). SRC-1: `libs/agno/agno/learn/stores/user_memory.py`.

> elif hasattr(data, "memories") and data.memories:
>     memories_text = "\n".join(f"- {m.get('content', str(m))}" for m in data.memories)
> --- `libs/agno/agno/learn/stores/user_memory.py:174-223`

#### MEM-OBJ-session-context
Label: SessionContextStore retained continuity

Source-native identity: SessionContextStore schema and deterministic session-derived learning row, type session_context. Form: structured symbolic fields carrying natural-language summary/planning content. Substrate: DB learning row. Lineage: extraction reads current supplied conversation and existing context, updates through tools. Later consumer: get_context_text or formatted summary in system context. Distinct from session.summary in [MEM-OBJ-agent-session](#mem-obj-agent-session) and fold summary; closest supplied [RT-RTE-context-window](runtime.md#rt-rte-context-window) concerns a different mechanism. Exact field-level retention/reason display unresolved. SRC-1: `libs/agno/agno/learn/stores/session_context.py`.

> Current messages take precedence if there's any conflict with this summary.
> --- `libs/agno/agno/learn/stores/session_context.py:189-232`

#### MEM-OBJ-learned-knowledge
Label: LearnedKnowledge JSON text and index

Source-native identity: LearnedKnowledge with title, learning, context, tags and namespace; saved through Knowledge.insert with TextReader and skip_if_exists. Form: natural-language insight/applicability inside symbolic JSON/scoping metadata; embeddings are distributed numerical representations, not readable reasons. Substrate: Knowledge content/vector stores. Lineage: caller/model save or conversation extraction. Later display includes title, learning, optional context/tags/namespace, not all provenance metadata. Applicability reasons may survive in context; no compulsory criticism/test evidence chain is established. Distinct from supplied component configuration [RT-OBJ-component-config](runtime.md#rt-obj-component-config). SRC-1: `libs/agno/agno/learn/stores/learned_knowledge.py`.

> if hasattr(learning, "context") and learning.context:
>     parts.append(f"_Context: {learning.context}_")
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:1442-1483`

#### MEM-OBJ-entity-memory
Label: EntityMemory facts, events, edges and retirement markers

Source-native identity: EntityMemory learning row scoped by entity/type/namespace/user, with directory and expanded views. Form: symbolic identity/relationships/timestamps/retirement flags; natural-language facts/events. Substrate: learning DB. Lineage: foreground remember/link/forget tools or direct caller operations; automatic process is a no-op. Superseded facts remain recorded but normal rendering uses live facts; whole-entity archive excludes automatic recall but search can reach it. No supplied counterpart after [RT-OBJ-run-context](runtime.md#rt-obj-run-context). Full reciprocal-edge repair and all custom-schema displays unresolved. SRC-1: `libs/agno/agno/learn/stores/entity_memory.py`, `libs/agno/agno/learn/schemas.py`.

> def live_facts(self) -> List[Dict[str, Any]]:
>     """Facts that have not been superseded. Only these render."""
>     return [f for f in self.facts if not (isinstance(f, dict) and f.get("superseded_at"))]
> --- `libs/agno/agno/learn/schemas.py`

#### MEM-OBJ-decision-log
Label: DecisionLog reasoning and outcome row

Source-native identity: DecisionLog, generated decision ID, learning type decision_log. Form: natural-language decision/reasoning/outcome and symbolic identity/category/confidence/time. Substrate: learning DB. Lineage: agent log_decision and record_outcome tools/direct calls; not automatic trace extraction. Later system display reads only five decisions and optional reasoning/outcome, not all alternatives or confidence. No counterpart after comparing [RT-OBJ-run-context](runtime.md#rt-obj-run-context); this is retained self-report, not the current context object or independently observed outcome. SRC-1: `libs/agno/agno/learn/stores/decision_log.py`.

> for decision in decisions[:5]:  # Limit to 5 most recent
>     if isinstance(decision, DecisionLog):
>         context += f"- **{decision.decision}**\n"
>         if decision.reasoning:
>             context += f"  Reasoning: {decision.reasoning}\n"
>         if decision.outcome:
>             context += f"  Outcome: {decision.outcome}\n"
> --- `libs/agno/agno/learn/stores/decision_log.py:147-193`

#### MEM-OBJ-compaction-archive
Label: Compaction record and rendered folded transcript

Source-native identity: CompactionArchive row containing summary, first_kept_message_id, run/session/user IDs, token counts and archived_messages. Form: symbolic fold/lineage metadata plus natural-language summary and rendered transcript. Substrate: DB compaction table when supported. Lineage: selected history prefix, role headings and tool-call argument display; each tool content is clipped at 20,000 characters. This is not a byte-identical backup of arbitrary message/media payloads. Latest/as-of fold consumers and pattern-search tools read different retained parts. Distinct object underlying supplied [RT-RTE-context-window](runtime.md#rt-rte-context-window), not a duplicate route.

SRC-1: `libs/agno/agno/compaction/archive.py`.

> MAX_ARCHIVED_TOOL_RESULT_CHARS = 20_000
> --- `libs/agno/agno/compaction/archive.py`

> parts.append(_clip(content, MAX_ARCHIVED_TOOL_RESULT_CHARS) if message.role == "tool" else content)
> --- `libs/agno/agno/compaction/archive.py`

#### MEM-OBJ-result-store
Label: ResultStore payload, access index and preview

Source-native identity: ResultStore payload file plus tool-result DB row/result ID; preview is a third, derived display. Form: payload preserves string output (possibly opaque JSON or other text); symbolic index provides path/scope/identity; preview text provides incomplete content. Substrate: session-namespaced FileSystem and DB index. Lineage: actual tool result, tool arguments and run/call identity. Later model reads requested slices/search hits after access checks; index/preview is not the payload and does not imply its full interpretation. Distinct from the ordinary Function schema [RT-OBJ-function](runtime.md#rt-obj-function) and compaction archive. SRC-1: `libs/agno/agno/offload/store.py`, `libs/agno/agno/offload/tools.py`.

> session_fs.write(path, output)
> --- `libs/agno/agno/offload/store.py:570-663`

### Routes

#### MEM-RTE-session-summary
Label: Session summary retention and later supply

Endpoints/progression/owner: completed session messages → SessionSummaryManager bounded selection → model summary/parse → session.summary → session persistence → later foreground system message. Host chooses last_n_runs/conversation_limit, model authors summary, parser admits supported structured/string responses. Overlaps completion in [RT-RTE-agent-run](runtime.md#rt-rte-agent-run), but has a distinct retained summary and later reader. SRC-1: `libs/agno/agno/session/summary.py`, `libs/agno/agno/agent/_messages.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SessionSummary or None; parse/model failure can leave no new summary.
- Later read-back: add_session_summary_to_context delivers only session.summary.summary in the system message.
- Delegated visibility: uninspected — team-specific summary persistence and all workflow rehydration were not traced.
- Selection predicate: enable_session_summaries plus manager on completion; configured run/message bounds select producer input; context flag selects consumer supply.
- Invalidation or expiry: successful generation replaces summary; explicit session deletion is exposed, but complete summary/cache deletion lifecycle is uninspected.
- Activation or effect: later model receives condensed continuity guidance; actual use and fidelity unobserved.
- Evidence limits: implementation not successful summarization; topics/audit fields are not all shown to foreground model.

Admission: software enables transformation and parsing; no per-summary human approval is established. Operating mode: open-request continuity, not a controlled experiment. No independent answer oracle. Guidance asks for a session summary; stored result is derived text/topics/time, not compulsory derivation or criticism reasons. Failed parsing rejects candidate; no inspected summary-version rollback.

> if session is not None and session_summary is not None:
>     session.summary = session_summary
>     self.summaries_updated = True
> --- `libs/agno/agno/session/summary.py:242-294`

#### MEM-RTE-user-memory
Label: MemoryManager extraction, mutation and prompt replay

Endpoints/progression/owner: configured background user input or foreground update_user_memory task → MemoryManager model plus DB tools → UserMemory rows → later user-scoped system-message iteration. Direct add/replace/delete and optimization are additional library admission doors. Distinct from [RT-RTE-agent-run](runtime.md#rt-rte-agent-run): specific derived material and cross-session reader. SRC-1: `libs/agno/agno/agent/_managers.py`, `libs/agno/agno/memory/manager.py`, `libs/agno/agno/agent/_default_tools.py`, `libs/agno/agno/agent/_messages.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: background metrics/future or update-task response; direct APIs return mutation results.
- Later read-back: add_memories_to_context fetches all returned memories for effective user ID and renders memory text in the system message; it does not call query-targeted search_user_memories.
- Delegated visibility: user scope follows configured identities; complete team/async equivalence uninspected.
- Selection predicate: nonempty user/extra messages, manager, update_memory_on_run and not enable_agentic_memory select background extraction; foreground tool call selects explicit task; read flag/user ID selects automatic supply.
- Invalidation or expiry: delete/clear/replace update stored memories; optimization with apply clears old set then upserts candidates. Automatic expiry and atomic replacement not established.
- Activation or effect: model-proposed DB operations can alter subsequent personalization context; actual recall/compliance unobserved.
- Evidence limits: extraction starts before foreground completion; user-message string can already include formatted knowledge context. Direct APIs and agentic task are not restricted to the automatic path's user-only provenance.

Admission: caller flags grant automatic/model mutation, not content approval. Capture criteria and existing memories guide model add/update/delete/no-change. Automatic create_or_update offers delete but not clear; explicit task can use broader management. Direct caller authorship/approval is unresolved, distinct from DB I/O. No answer oracle; open conversations and explicit maintenance requests. Optimization apply=False returns candidates; apply=True replaces the set without a shown transaction or rollback. Reasons/input provenance may be stored, but the normal later prompt consumes memory text, not its full rationale.

> and not agent.enable_agentic_memory
> --- `libs/agno/agno/agent/_managers.py:177-217`

> # Clear all existing memories for the user
> self.clear_user_memories(user_id=user_id)
> --- `libs/agno/agno/memory/manager.py:797-867`

#### MEM-RTE-memory-editing
Label: AgentOS retained-memory editing admission

Endpoints/progression/owner: HTTP create/patch/delete/optimize request → database/scope resolution → memory or learning-row write → later SDK reload and model-context rendering. API client supplies content; route/backend enforce scope and write semantics, not content truth. Distinct from [RT-RTE-config-admission](runtime.md#rt-rte-config-admission): memory/learning rows rather than executable component configuration. SRC-1: `libs/agno/agno/os/routers/memory/memory.py`, `libs/agno/agno/os/routers/learnings/router.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: memory/learning response, deletion response or HTTP error; remote DB branch forwards.
- Later read-back: MemoryManager reads the same user-memory rows; learning stores read matching type/ID rows on later recall. Display/schema compatibility of arbitrary edited content is not guaranteed.
- Delegated visibility: uninspected — remote-server scope enforcement and all client/UI presentation are outside inspected bodies.
- Selection predicate: requested memory/learning ID, resolved DB/table, effective user/JWT scope; patch learning requires existing row and non-null content.
- Invalidation or expiry: delete withdraws row; later extraction or direct save may recreate it. No permanent tombstone or cross-cache freshness guarantee established.
- Activation or effect: accepted edits change the text/data available to subsequent reads; actual downstream consumption unobserved.
- Evidence limits: authentication configuration and generic caller identity do not establish human editing/approval; learning patch is last-write-wins with concurrent recreation, not a versioned review gate.

Admission/recovery: scope checks can veto access; missing user, missing row or null content can reject. Proposer is API client, physical writer is DB code. Human intervention is afforded through the API but not identified as exercised per-content control. Guidance is request schema/content, no independent task-answer oracle. No inspected old-content rollback; re-edit is another write. Memory optimization is a separate transformation, not evidence of correctness from reduced token counts.

> # Update-only (never insert). The learning stores key records by a deterministic id
> # shared with this endpoint, so the agent is a live concurrent writer to the same row.
> --- `libs/agno/agno/os/routers/learnings/router.py:492-539`

#### MEM-RTE-profile-extraction
Label: UserProfile automatic trace transformation

Endpoints/progression/owner: background snapshot/manual supplied messages → existing profile plus conversation text → store model update tools → user_profile learning row → later identity recall/render. Separate material producer within LearningMachine, not another [RT-RTE-agent-run](runtime.md#rt-rte-agent-run) declaration. SRC-1: `libs/agno/agno/agent/_managers.py`, `libs/agno/agno/learn/stores/user_profile.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: process returns None; explicit extraction returns model response/update indication.
- Later read-back: later recall(user_id) retrieves profile; rendered truthy updateable fields feed learning context.
- Delegated visibility: agent/team audit identities can accompany extraction; complete delegate history provenance uninspected.
- Selection predicate: ALWAYS mode, nonempty messages/user ID; explicit extract_and_save is a separate door not restricted by process mode.
- Invalidation or expiry: field updates/save/delete; exact merge and custom-schema reset behavior uninspected.
- Activation or effect: retained profile values can personalize later inference; improvement unobserved.
- Evidence limits: background snapshot need not contain current final answer/tools; update flag is not an independent correctness check.

Admission: configured mode and model/tool limit govern software update; model proposes field values, tool code writes. Missing model/DB/input can reject/skip; exact field checks remain unresolved. Human approval not established. Guidance: existing profile and extraction system message; open conversations, no reference-answer oracle. Retained values/audit data do not establish retained explanatory reasons. Direct save and HTTP edit remain alternative authorities.

> Message(role="user", content=f"Extract profile information from this conversation:\n\n{conversation_text}"),
> --- `libs/agno/agno/learn/stores/user_profile.py:819-888`

#### MEM-RTE-memories-extraction
Label: UserMemoryStore automatic trace transformation

Endpoints/progression/owner: messages plus existing Memories → conversation-text extraction/model tools → user_memory learning row → later rendered memory block. Distinct store/admission detail from MemoryManager and from [RT-RTE-agent-run](runtime.md#rt-rte-agent-run). SRC-1: `libs/agno/agno/learn/stores/user_memory.py`, `libs/agno/agno/agent/_managers.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: process None; extraction response or no-updates message.
- Later read-back: user-ID lookup, get_memories_text/content bullets then system learning context.
- Delegated visibility: agent/team IDs retained for audit; exact child-context inclusion uninspected.
- Selection predicate: process ALWAYS, valid user and messages; direct extraction/update tools are additional routes.
- Invalidation or expiry: save/delete/clear exposed; exact individual deletion/merge rules not fully inspected.
- Activation or effect: derived personal facts become later personalization inputs; actual dependence unobserved.
- Evidence limits: not all messages are necessarily current completed results; retained raw conversation is not implied by extraction.

Admission: model chooses mutations under instructions/existing memory and max_updates_per_run, code exposes DB tools. Direct API/HTTP writer can bypass extraction guidance. Human authorship/approval unresolved. Missing model/DB/empty conversation skips; no verified correctness oracle or automatic rollback inspected. Operating mode: open conversation/explicit updates. Rationale retention per memory is unresolved; default display reads content, not a criticism ledger.

> Message(role="user", content=f"Extract memories from this conversation:\n\n{conversation_text}"),
> --- `libs/agno/agno/learn/stores/user_memory.py:728-800`

#### MEM-RTE-context-extraction
Label: SessionContext automatic continuity update

Endpoints/progression/owner: messages plus existing session context → model summary/planning update tools → session_context row → subsequent same-session learning context. Distinct from supplied compaction [RT-RTE-context-window](runtime.md#rt-rte-context-window). SRC-1: `libs/agno/agno/learn/stores/session_context.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: process None; explicit extraction response/update indication.
- Later read-back: keyed session recall followed by get_context_text/formatted summary in system context.
- Delegated visibility: audit user/agent/team IDs available; full workflow cross-session checkpoint behavior uninspected.
- Selection predicate: ALWAYS mode/session/messages for process; direct extraction accepts a supplied conversation.
- Invalidation or expiry: replaces/updates context through save tools; delete/clear exposed, no automatic TTL established.
- Activation or effect: prior decisions/plans can shape continuity; actual compliance unobserved.
- Evidence limits: schema-specific summary versus planning updates not completely inspected; no guarantee the context has every earlier detail.

Admission: model proposes content, configured tools/limits and DB availability govern writing; no identified per-content human approval or oracle. Existing context guides successor extraction; open-request operation. Missing model/DB rejects extraction; exact rollback/versioning unresolved. Retained continuity is derived material, not proof of effective learning or accurate prior conclusions.

> existing_context = self.get(session_id=session_id)
> --- `libs/agno/agno/learn/stores/session_context.py:499-581`

#### MEM-RTE-learned-knowledge
Label: Reusable insight save and targeted recall

Endpoints/progression/owner: ALWAYS-mode conversation extraction, foreground save_learning, or direct save → schema/namespace checks → JSON Knowledge insertion/index → later query search/render → model. Distinct from component configuration [RT-RTE-config-admission](runtime.md#rt-rte-config-admission); producer is not necessarily an evaluator or theory critic. SRC-1: `libs/agno/agno/learn/stores/learned_knowledge.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: save boolean/tool message or extraction completion; search returns learning objects/display text.
- Later read-back: current query/message semantic search defaults to five results with effective namespace/user scoping; rendering carries insight and optional applicability context.
- Delegated visibility: agent/team metadata saved; global versus user namespace changes accessible scope, not automatic entire-history sharing.
- Selection predicate: ALWAYS process for extraction; agent_can_save/search for tool exposure; namespace user requires user ID. Explicit API save is another door.
- Invalidation or expiry: skip_if_exists insertion and explicit delete(title) exposed; complete title matching/replacement semantics uninspected.
- Activation or effect: stored insight can guide later answers through system/tool text; actual dependence and benefit unobserved.
- Evidence limits: PROPOSE is natural-language approval guidance in the inspected path, not an approval token enforced by save_learning. Extraction duplicate search uses first 500 conversation characters and five hits, not exhaustive equivalence checking.

Admission: model/caller proposes title/insight/context/tags; schema/scoping/Knowledge insert accepts. Model can decline to save. PROPOSE requests user yes/no, but direct tool implementation has no explicit approval check; external Function confirmation could add a gate if configured. Human per-content control is therefore requested, not guaranteed or observed. ALWAYS extraction and direct API are materially different. No answer oracle. Open conversations; guidance asks reusable insights and duplicate search, not a controlled evaluation. Saved context may retain when/why applicability; no required retained criticism/outcome chain is established.

> Call `save_learning` ONLY after the user says "yes" to your proposal.
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:326-384`

> success = self.save(
>     title=title,
>     learning=learning,
>     context=context,
>     tags=tags,
>     user_id=user_id,
>     agent_id=agent_id,
>     team_id=team_id,
>     namespace=namespace,
> )
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:569-613`

#### MEM-RTE-entity-memory
Label: Entity admission, retirement and selective expansion

Endpoints/progression/owner: foreground remember/link/forget or direct caller → entity resolution and optional model supersession judgment → learning-row save → bounded directory/relevant expansion or search → model. Closest supplied [RT-RTE-agent-run](runtime.md#rt-rte-agent-run) is the enclosing tool loop, not this store route. SRC-1: `libs/agno/agno/learn/stores/entity_memory.py`, `libs/agno/agno/learn/schemas.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutation/ambiguity/status text or search results.
- Later read-back: automatic recall lists bounded recent directory and expands keyed/name/alias/lexically matched entities; render applies entity/fact/event caps. Search is another requested route, including archived entities.
- Delegated visibility: namespace/user scope and keyed entity/type govern access; full team-specific namespace policy uninspected.
- Selection predicate: process does no automatic capture; foreground tools write. Recall uses current message, configured directory/top-k limits, bounded term search and related names.
- Invalidation or expiry: supersession retires eligible existing facts above confidence threshold; forget retires facts or archives whole entity, can remove edge/event; new remember can revive archived entity.
- Activation or effect: retired facts stop ordinary live rendering, archived entities stop automatic recall; later agent behavior unobserved.
- Evidence limits: retirement is not erasure; archived search remains. Judge prompt/complete confidence calibration and relationship repair unresolved.

Admission: model/caller supplies claims; name/match checks and supersession threshold can reject changes. Ambiguous partial forget matches retire nothing. Computational comparison is not an independent answer oracle; exact content-directed theory criticism is not established merely by retirement. Human approval unresolved; open interaction/explicit maintenance. Reasons persist as replacement/forgotten marker and optional fact history, not necessarily complete criticism; normal consumer receives live facts rather than all retired reasons. No uniform rollback/edge transaction guarantee concluded.

> if confidence < threshold:
>     continue
> if fact_id not in eligible_ids:
>     continue
> --- `libs/agno/agno/learn/stores/entity_memory.py:1454-1491`

> f"Archived {label}. It will no longer be recalled; search_entities can still "
> f"find it, and any new remember_about about it revives it.",
> --- `libs/agno/agno/learn/stores/entity_memory.py:2146-2232`

#### MEM-RTE-decision-memory
Label: Agentic decision and outcome reuse

Endpoints/progression/owner: foreground log_decision/record_outcome or direct call → DecisionLog learning row → recent-decision recall → bounded reasoning/outcome display. Distinct from runtime decision ownership in [RT-RTE-agent-run](runtime.md#rt-rte-agent-run): explicit retained representation, not the decision itself. SRC-1: `libs/agno/agno/learn/stores/decision_log.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: decision ID/update response or search results.
- Later read-back: recall filters agent/type/days, deliberately not current session; default ten results, display first five with reasoning/outcome.
- Delegated visibility: user/session/agent/team metadata records origin but does not mean every metadata field enters model context.
- Selection predicate: agentic tools/direct calls write; automatic process is no-op; query filters or recency select readers.
- Invalidation or expiry: outcome update alters row; generic AgentOS learning delete/edit can withdraw/replace it; full backend expiry uninspected.
- Activation or effect: retained decision explanations/outcomes can guide later model decisions; causal dependence unobserved.
- Evidence limits: reported outcome/quality is not validated environmental feedback, and stored alternatives are not all displayed.

Admission: foreground model/caller authors decision/reasoning and can omit logging; DB saves. Generic caller identity does not identify human approval. Guidance asks significant decisions with reasoning; no independent answer oracle. Open work, not a scored curriculum. No automatic content-directed revision loop inferred from an outcome field. This route retains reasons and has a later reason reader, unlike default personal-memory display.

> def process(self, messages: List[Any], **kwargs) -> None:
>     """No-op: decision logging is AGENTIC-only, capture happens through the tools."""
>     return
> --- `libs/agno/agno/learn/stores/decision_log.py:139-146`

#### MEM-RTE-learning-context
Label: LearningMachine automatic selected context supply

Endpoints/progression/owner: Agent system-message preparation → LearningMachine.recall with user/session/message/agent/context → each enabled store → store.build_context → concatenated guidance/data → foreground model. Manual build_context/instructions provides an afforded caller-controlled placement door; automatic SDK call is wired. Distinct from generic [RT-RTE-agent-run](runtime.md#rt-rte-agent-run). SRC-1: `libs/agno/agno/learn/machine.py`, `libs/agno/agno/agent/_messages.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted learning-context string.
- Later read-back: identity-selected profile/memories/session context, queried insights, entity directory/expansions and recent decisions from earlier writes enter a later system message.
- Delegated visibility: automatic call passes actual run context/metadata/dependencies/state and agent identity; store signature filtering decides accepted selectors. Full custom-store interpretation unresolved.
- Selection predicate: _learning and add_learnings_to_context; current message supplied for targeted stores; user/session keys for identity stores; per-store and display caps, not a shared global token budget shown here.
- Invalidation or expiry: reload uses current store content; store mutation/deletion changes candidates, but cached/custom-store freshness not certified.
- Activation or effect: selected text/guidance is delivered for natural-language interpretation; actual reliance unobserved.
- Evidence limits: failed store recall/render logs and omits that store; partial context can be returned. Automatic direction is host push conditioned on current request, not a model tool request for every store.

> for name, data in results.items():
>     store = self.stores.get(name)
>     if store:
>         try:
>             formatted = store.build_context(data=data)
>             if formatted:
>                 parts.append(formatted)
> --- `libs/agno/agno/learn/machine.py:987-1007`

#### MEM-RTE-profile-curation
Label: Curator profile-memory pruning and deduplication

Endpoints/progression/owner: caller maintenance invocation → user_profile lookup → age/count or normalized-content rules → save modified profile → later profile recall. Distinct from [RT-RTE-context-window](runtime.md#rt-rte-context-window): durable content maintenance, not prompt eviction. SRC-1: `libs/agno/agno/learn/curate.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: count removed, including zero when store/profile/memories unavailable.
- Later read-back: changed profile is available to later profile readers; default render shows updateable fields, so whether a custom profile's memories list is displayed depends on its schema.
- Delegated visibility: inapplicable — this maintenance API does not dispatch a delegate.
- Selection predicate: caller user ID and age/count options; only user_profile with a memories attribute; normalize lowercase/punctuation/whitespace for duplicate equality.
- Invalidation or expiry: deletes entries from current profile list and saves; no archived old-list rollback shown.
- Activation or effect: later profile contents may shrink; actual invocation/behavior unobserved.
- Evidence limits: no general curation of all six stores; missing/unparseable age timestamps kept. Near-exact label does not establish semantic deduplication.

Admission: caller chooses maintenance, code chooses removals; no model judgment or human per-item approval shown. No answer oracle; explicit maintenance operation. No content truth check or beneficial optimization inferred from a removed count.

> store = self.machine.stores.get("user_profile")
> if not store:
>     return 0
> --- `libs/agno/agno/learn/curate.py:36-83`

#### MEM-RTE-knowledge-context
Label: Knowledge admission and automatic or requested retrieval

Endpoints/progression/owner: caller ingestion or granted add_to_knowledge tool → reader/chunk/vector write/content status → later custom retriever or Knowledge.retrieve/search → automatic user references or search-tool result → model. Model-authored query/result JSON and ingested external sources have different origins. No supplied knowledge-object counterpart after [RT-OBJ-component-config](runtime.md#rt-obj-component-config); configuration is not indexed knowledge. SRC-1: `libs/agno/agno/knowledge/knowledge.py`, `libs/agno/agno/agent/_default_tools.py`, `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/agent/_tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: insertion/status response or retrieved documents; add_to_knowledge success string alone is not indexing proof.
- Later read-back: add_knowledge_to_context automatically queries current user text and appends formatted references; search_knowledge offers model-requested query/results. References stored on RunOutput are distinct from consumed references.
- Delegated visibility: resolved knowledge/retriever and user/filter scope follow run context; custom caller signature can change selector inputs. Complete adapter isolation uninspected.
- Selection predicate: reader/chunker/configuration on write; query, max_results, filters/user scope and optional transform/reranker on read. Invalid filter keys may be ignored; custom retriever takes precedence.
- Invalidation or expiry: content deletion cascades site children/vectors; failed deletion preserves retry anchor. Managed pages reject this deletion path and require sync_pages.
- Activation or effect: retrieved text is offered as references/tool results; model adoption/accuracy unobserved.
- Evidence limits: optional query transformation, reranking, remote/LightRAG/reader/embedding internals unresolved; no uniform source trust or freshness guarantee.

Admission: caller supplies material or foreground model proposes query/result, tool exposure grants writes; software checks ownership/reader/backend, handles embedding failures/status/retries. No per-content human review or truth oracle shown. Operating mode: external ingestion and open-request retrieval. Recovery preserves failed deletion rows and can re-ingest partial/failed content; not all writes/deletes are one atomic transaction. Numerical index lineage depends on adapter/embedder, not the mere term knowledge.

> if surviving_children and content is not None:
>     # Some pages could not be removed: the parent stays as the retry anchor,
>     # its cascade record narrowed to what actually survives.
>     self._stamp_row_children(content, surviving_children)
>     return False
> --- `libs/agno/agno/knowledge/knowledge.py:1464-1537`

#### MEM-RTE-page-knowledge
Label: Managed documentation page publication and read-back

Endpoints/progression/owner: caller sync_pages source/transform/index version → discovery/embedding → transactional filesystem/vector/catalog publication → later page search/read tools and Knowledge search. Distinct admission path within knowledge, not a duplicate of [RT-RTE-config-admission](runtime.md#rt-rte-config-admission). SRC-1: `libs/agno/agno/knowledge/page/_coordinator.py`, `libs/agno/agno/knowledge/page/tools.py`, `libs/agno/agno/knowledge/knowledge.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SyncReport counts/status/errors; chat search JSON or MCP typed SearchResult.
- Later read-back: search_pages queries published page index and returns bounded result; read_page/read_full_page/list/grep APIs are exposed alternatives, but complete snapshot/read reconstruction not inspected.
- Delegated visibility: selected bound knowledge namespace and transport budget constrain delivered search result; full MCP caller integration uninspected.
- Selection predicate: source binding, discovery/transform/index fingerprint and reindex flag on write; query/alternatives/output budget on search; full search SQL ranking unresolved.
- Invalidation or expiry: successful complete error-free sync prunes removed/skipped pages transactionally from vector/filesystem/catalog; incomplete discovery/failures prevent pruning.
- Activation or effect: newly published page revisions enter later retrieval candidates; successful deployed sync/agent use unobserved.
- Evidence limits: atomic per-page publish does not mean atomic whole corpus replacement; connection loss may produce commit_outcome_unknown and partial report.

Admission: source-discovery validation callback can veto by raising; a boolean is rejected, not interpreted as approval. Publication checks quotas and vector completeness. Caller initiates source sync, which is not human approval of every page. Transform authorship and source trust unresolved. No content-correctness oracle; explicit source synchronization. Page text, digest/revision, vectors and catalog metadata persist; failed-attempt reports are separate from successfully published content.

> if not self._valid_vectors(conn, page):
>     raise ValueError("incomplete_page_vectors")
> --- `libs/agno/agno/knowledge/page/_coordinator.py:843-942`

> if source.complete and not errors and not failed and not unknown:
> --- `libs/agno/agno/knowledge/page/_coordinator.py:1519-1637`

#### MEM-RTE-tool-compression
Label: Tool message compressed-content transformation

Endpoints/progression/owner: model-loop threshold → CompressionManager selects uncompressed tool messages → compression model → Message.compressed_content → provider message serialization where enabled. Distinct from [RT-RTE-context-window](runtime.md#rt-rte-context-window): per-result field rather than prefix fold. SRC-1: `libs/agno/agno/compression/manager.py`, `libs/agno/agno/models/message.py`, `libs/agno/agno/models/base.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutates message compressed_content and statistics; model error can return original labelled tool text.
- Later read-back: Message serialization includes compressed_content, so it can persist with retained messages; complete later history/provider use uninspected — no universal later-consumer route concluded.
- Delegated visibility: inapplicable — compression subcall gets tool name/content and compression instructions, not delegated task execution.
- Selection predicate: optional token threshold or uncompressed-tool count, default count three; compress all uncompressed tool-role messages when triggered.
- Invalidation or expiry: original content field remains; compressed flag avoids repeated compression. Complete storage scrubbing/retained field expiry uninspected.
- Activation or effect: can reduce current model-visible result detail where compressed-content consumption is enabled; actual fidelity/benefit unobserved.
- Evidence limits: provider-specific activation not exhaustively traced; compressor requests removal of hedging, so preservation of all epistemic qualifications is not guaranteed.

Admission: code triggers, model authors condensed wording, truth is not checked by a reference oracle. Custom prompt can replace default guidance. No human per-result approval. Size statistics do not prove semantic equivalence. This is trace-fed transformation; durable behavior-shaping replay remains a named uncertainty rather than inferred from field storage alone.

> • Hedging language ("might", "possibly", "appears to")
> --- `libs/agno/agno/compression/manager.py:14-50`

> tool_msg.compressed_content = compressed
> --- `libs/agno/agno/compression/manager.py:142-172`

#### MEM-RTE-result-offload
Label: Large tool-result eviction, retention and requested reload

Endpoints/progression/owner: tool result above character threshold → ResultStore payload/index write → bounded preview envelope in model context → foreground read_result/search_result tool → checked payload slice/hits → later model invocation. Store tools are registered in Agent; model/continuation integration invokes offload. Distinct from [RT-RTE-context-window](runtime.md#rt-rte-context-window): exact string payload outside window, not summary fold. SRC-1: `libs/agno/agno/offload/store.py`, `libs/agno/agno/offload/tools.py`, `libs/agno/agno/agent/_tools.py`, `libs/agno/agno/models/base.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: preview/result-ID envelope, or explicit refused-write head/tail envelope; execution continues.
- Later read-back: requested read by result ID/line/character range or search pattern delivers retained output to subsequent model call; same-session cross-run reachability depends on retained index/payload and TTL.
- Delegated visibility: team members sharing session can read same-session payload; when both stored/current user IDs exist they must match. Missing user on either side does not establish a user-level gate.
- Selection predicate: length exceeds threshold; read-back tools exempt from offloading. Foreground model selects ID/range/pattern, code applies scope and page caps (400 lines/16,000 characters for read).
- Invalidation or expiry: TTL sweep and session deletion remove payload/index; index write failure attempts payload cleanup. Deletion exceptions can leave orphan payloads; no secure-erasure guarantee.
- Activation or effect: large result is removed from immediate full delivery but explicit reload can restore selected details; actual requests/use unobserved.
- Evidence limits: refusal loses reload route for omitted details; result ID is not an automatically dereferenced pointer. Full payload/index transaction and all filesystem contracts not established.

Admission: code size rule proposes physical offload, store quota/backend can veto; this is not semantic knowledge approval. No human content gate/oracle. Stored output remains raw trace, envelope is derived display/access metadata. Cleanup deletes payload before index and logs failures; no universal rollback guarantee. The window holds by-value preview/text, so the heap analogy stops at explicit tool-mediated retrieval, not automatic pointer liveness.

> if str(row.get("session_id")) != str(run_context.session_id):
>     return f"Error: result {result_id} belongs to a different session"
> --- `libs/agno/agno/offload/tools.py:23-39`

> except Exception as e:
>     log_warning(f"Result payload delete failed for {row.get('result_id')}: {e}")
> --- `libs/agno/agno/offload/store.py:920-934`

### Claims

#### MEM-CLM-nonlossy-archive
Label: Archive non-lossy claim and bounded implementation

Claimed operation: archive makes compaction non-lossy and allows original detail recovery. Doctrine/design source: SRC-1, `libs/agno/agno/compaction/archive.py`. Claim conclusion status: claimed. Inspected implementation qualifies it: tool contents are clipped, rendered messages omit arbitrary non-text payloads, archive writing may fail or be unsupported, and lookup is output-bounded. Full session history can separately remain intact, but no universal lossless consumer delivery follows. Closest supplied [RT-RTE-context-window](runtime.md#rt-rte-context-window) already distinguishes stored originals from selected context; this record names the stronger source-native wording.

> The archive is what makes compaction non-lossy. A summary alone is a guess about what mattered;
> --- `libs/agno/agno/compaction/archive.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-context
Label: Selected retained text to foreground inference

Consumer: foreground provider model. Channel: system memory/profile/learning/summary blocks, automatic user references and requested tool results. Force: natural-language interpretation; content in a system message has instruction-channel priority but does not become a symbolic truth/freshness rule. Horizon: later calls within session and across user/namespace scopes while retained and selected. Distinct from static [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions): text derives from earlier writes/use. Delivery does not establish compliance. SRC-1: `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/learn/machine.py`.

> system_message_content += session.summary.summary
> --- `libs/agno/agno/agent/_messages.py:1070-1211`

#### MEM-BAP-retirement-filter
Label: Entity retirement markers to live-fact selection

Consumer: EntityMemory.live_facts and context rendering. Channel: symbolic superseded_at flags. Force: fixed code excludes retired facts from ordinary live display; this is distinct from the model interpreting the remaining text. Horizon: subsequent renders until another mutation changes data. No counterpart to static [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions); closest executor path [RT-BAP-function-dispatch](runtime.md#rt-bap-function-dispatch) performs the write, not this retained-state filtering. SRC-1: `libs/agno/agno/learn/schemas.py`; passage supplied by [MEM-OBJ-entity-memory](#mem-obj-entity-memory).

## Annotations

#### On [RT-RTE-context-window](runtime.md#rt-rte-context-window)

Memory-specific continuation: fold persistence has at least two forms, summary/boundary only and summary plus rendered archived messages. Original session history is not rewritten by apply_compaction. Archive latest(up_to_run_id) selects a historical fold rather than a later future-containing summary. A DB without record support can apply a fold while losing separate recoverability. Search uses session-bound pattern alternatives, candidate folds then line matching/output caps; it is requested reload, not automatic full restoration. SRC-1: `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/compaction/compaction.py`, `libs/agno/agno/compaction/archive.py`. [MEM-OBJ-compaction-archive](#mem-obj-compaction-archive) supplies storage/form/clipping evidence. Summary reasoning fidelity and benefit remain unobserved; backend expiry is unresolved.

> # The record is stored either way; the transcript only when archiving is on.
> stored = archive.write(record, to_compact if self.store_compacted_messages else [])
> record.archived = stored and self.store_compacted_messages
> --- `libs/agno/agno/compaction/compaction.py:1037-1095`

> "This database does not implement compaction records; the summary still applies "
> "but the folded messages are not recoverable."
> --- `libs/agno/agno/compaction/archive.py:119-133`

## Write side

The principal trace-fed chains are separate. User input → MemoryManager → memory text → later personalization is [MEM-RTE-user-memory](#mem-rte-user-memory). Conversation snapshot → user/profile/session/insight extraction → corresponding retained row/index → later LearningMachine rendering is split across [MEM-RTE-profile-extraction](#mem-rte-profile-extraction), [MEM-RTE-memories-extraction](#mem-rte-memories-extraction), [MEM-RTE-context-extraction](#mem-rte-context-extraction) and [MEM-RTE-learned-knowledge](#mem-rte-learned-knowledge). Raw message persistence alone is not one of these derived updates.

Automatic learning input is not guaranteed to be the final completed run. The background code snapshots a mutable live message list before/concurrently with foreground generation; manual process/capture doors can supply different traces. Current formatted messages may mix user, history, instructions and retrieved context. Exact final-trace coverage through capture hooks remains unresolved. SRC-1: `libs/agno/agno/agent/_managers.py`, `libs/agno/agno/agent/_run.py`.

> # Snapshot: learning runs concurrently while the model call appends to the live list
> messages = list(run_messages.messages) if run_messages else []
> --- `libs/agno/agno/agent/_managers.py:265-302`

Automatic process does not imply writes to every learning store: entity and decision process are no-ops, with foreground tools as their capture door. [MEM-RTE-entity-memory](#mem-rte-entity-memory), [MEM-RTE-decision-memory](#mem-rte-decision-memory). Direct save and HTTP edit introduce caller-authored material without extraction; actor identity alone cannot classify it as human authorship or approval. [MEM-RTE-memory-editing](#mem-rte-memory-editing).

Maintenance has actual withdrawal consequences but different persistence semantics. Memory optimization can clear then refill; Curator prunes/deduplicates only profile memories; entity forget retires facts/archives entities while search can retain access; knowledge deletion preserves failed cascade anchors; managed page pruning runs only after complete error-free discovery. None is universal erasure. [MEM-RTE-user-memory](#mem-rte-user-memory), [MEM-RTE-profile-curation](#mem-rte-profile-curation), [MEM-RTE-entity-memory](#mem-rte-entity-memory), [MEM-RTE-knowledge-context](#mem-rte-knowledge-context), [MEM-RTE-page-knowledge](#mem-rte-page-knowledge).

Compaction retains summary plus boundary, optionally clipped archive, while raw session history remains separately stored. Compression retains a derived field alongside original content, but complete later provider consumption is unresolved. Offload retains raw payload separately from preview/index and refuses writes visibly. These mechanisms do not prove truth-preserving curation. Their reasons have different later readers: decision reasoning and learned applicability context can be shown; normal personal-memory display does not show source/input metadata; retired fact history is not normal live context. The records retain these distinctions rather than attributing one system-wide learning/improvement result.

## Read-back

Automatic supply is host-triggered: session history bounds/filters/folds in [RT-RTE-context-window](runtime.md#rt-rte-context-window); summary and personal memory in [MEM-RTE-session-summary](#mem-rte-session-summary) and [MEM-RTE-user-memory](#mem-rte-user-memory); store-specific learning selection in [MEM-RTE-learning-context](#mem-rte-learning-context); current-user-text knowledge query and references in [MEM-RTE-knowledge-context](#mem-rte-knowledge-context). The selector uses current request information, but identity lookup is not semantic relevance ranking and model instructions to apply relevant memories do not reduce delivered memory volume themselves.

Requested reload is a different operation: knowledge/learning searches, entity searches including archives, search_compacted_history and ResultStore range/pattern tools. IDs and summaries in a window do not dereference themselves. Page search has chat/MCP typed versus serialized delivery; documented manual build_context supplies an afforded consumer role without proving any external application's placement. Generic getters with unspecified caller establish storage capabilities, not additional completed consumer routes.

Progressive static skills loading keeps full instructions/references out until tools request them. It is working-context control without demonstrated accumulation-through-use. SRC-1: `libs/agno/agno/skills/agent_skills.py`, `libs/agno/agno/agent/_messages.py`.

> This creates an XML-formatted snippet that provides the agent with
> information about available skills without including the full instructions.
> --- `libs/agno/agno/skills/agent_skills.py:90-149`

Team and workflow contexts are selected rather than universally shared, per supplied [RT-RTE-team-delegation](runtime.md#rt-rte-team-delegation) and [RT-RTE-workflow-step](runtime.md#rt-rte-workflow-step). The call-frame analogy fits selected child input and return, but breaks at shared identities/state, retained runs and external effects. Compaction/offload fit eviction plus explicit reload, not automatic heap references. No designation of model-window pointer liveness or semantic reachability is inferred.

## Integration issues

1. **Source claim qualification, not correction of runtime.** [MEM-CLM-nonlossy-archive](#mem-clm-nonlossy-archive) qualifies archive doctrine with tool clipping and unsupported persistence. [RT-RTE-context-window](runtime.md#rt-rte-context-window) is compatible: intact original session records are separate from the clipped lookup transcript. Reconciliation should not turn either into full lossless model read-back.
2. **Partial overlap, no duplicate declarations intended.** New session/summary/extraction/tool-result routes refine different stored objects/consumers around [RT-RTE-agent-run](runtime.md#rt-rte-agent-run), not replace the complete runtime loop. Compaction itself is annotated, not re-declared. The compaction archive is a new object underlying [RT-RTE-context-window](runtime.md#rt-rte-context-window). New model roles are not claims of distinct provider weights from the supplied components.
3. **Automatic trace timing.** [MEM-RTE-learning-context](#mem-rte-learning-context) and extraction records use the concurrent snapshot evidence. Any broader claim of automatic learning from the final current outcome requires capture-hook/finalization inspection; no correction to the supplied runtime's before-call background launch is needed.
4. **PROPOSE authority.** [MEM-RTE-learned-knowledge](#mem-rte-learned-knowledge) distinguishes approval guidance from local symbolic confirmation. Reconciliation must not equate PROPOSE with the enforced marked-Function gate in [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation); explicit confirmation could be configured separately.
5. **Unresolved retained alternatives.** Inventory limits remain for media reconstruction, provider caches/opaque state, workflow checkpoints/forks, full storage scrubbing, custom stores/readers/chunkers/remote services and adapter-specific deletion/embedding guarantees. They prevent exhaustive all-payload/context-policy and uniform security/expiry conclusions, not the positive routes recorded here.
6. **Evaluation linkage unresolved.** Evaluation/tracing surfaces were discovered but not traced to admitted memory updates. Decision outcome reporting in [MEM-RTE-decision-memory](#mem-rte-decision-memory) is not an independently supplied oracle, and extraction/curation is not evidence of exercised or beneficial improvement. No theory-builder or self-improvement classification is asserted from names alone.
7. **Compression later consumer unresolved.** [MEM-RTE-tool-compression](#mem-rte-tool-compression) establishes transformation/integration and a serializable field, not every provider's later-history use. Reconciliation should preserve that uncertainty rather than infer replay from storage capability.
8. **Curator compatibility.** [MEM-RTE-profile-curation](#mem-rte-profile-curation) explicitly requires a profile memories attribute and then a later schema-dependent display. Its narrow selection must not become a claim that all built-in memory stores undergo semantic deduplication.

No supported correction to a supplied runtime identity/fact is requested. The unresolved questions above and in the inventory are conclusion limits, not missing-source access failures.

## Limitations and checks

Frozen checkout HEAD was rechecked as 00497422d4a386d93ab3b45c1a11faf42fcc932f. Source identity is the boundary's Git identity, not the local path. Mandatory invocation/job/type/member/worker/record-contract reads were completed in the supplied batches; source searches and reads stayed within SRC-1 and the selected boundary. No prior characterizations, other attempts, target execution or agents were used. Method identity is the supplied checked-out instructions/types; no separate method commit was supplied to this worker and none is inferred.

The inventory is not an assertion of exhaustive adapter or workflow coverage. In particular no complete cache freshness, universal authorization, atomic whole-store replacement, semantic-preservation, effective forgetting, observed learning or successful self-improvement result follows. Natural-language pressure to use/update/approve content is distinct from code enforcement and from execution evidence.

Validation: the invocation-specific validate-output command reported “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The deterministic content pass covers member form, references and quotation occurrence; it does not establish semantic coverage, source support sufficiency, job acceptance or a checked invocation-residue result.
