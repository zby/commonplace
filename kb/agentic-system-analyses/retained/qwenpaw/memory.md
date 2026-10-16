---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "QwenPaw memory: backend-dependent extraction and retrieval, Scroll history and continuation state, editable Markdown and alternative context consumers."
run-id: AAS-2026-10-15-qwenpaw-e41495d47fc0-01
source-identity: https://github.com/niceirene/qwenpaw
reviewed-boundary: "16b2e712d198166c9359e77055b13bf2668bf5ae"
---

# QwenPaw memory report

## Boundary and evidence

This report covers memory and context mechanisms inside the whole-system boundary fixed by [boundary](boundary.md). SRC-1 is the repository at 16b2e712d198166c9359e77055b13bf2668bf5ae. Direct inspection of its adapters, middleware, commands, configuration, context managers and editors supplements the provisional [runtime](runtime.md). Executable source supplies implementation evidence; guidance and embedded dependency job descriptions supply doctrine/design, not observed results. No target code, tests, examples, provider calls or services were executed. No execution evidence was supplied.

Memory is not one store. Native session checkpoints, Scroll raw history, derived continuation state, ReMe Markdown, ADBPG service results and editable prompt files have different producers and consumers. Backend `none` disables memory-manager tools and middleware, not every other persistence mechanism. The native and harness lifecycles must also remain separate.

### Coverage inventory

All paths below are commit-relative SRC-1 paths. “Direct” means source text was inspected, not executed. A bounded excerpt or search is not complete file coverage. Unresolved included surfaces remain part of the account rather than evidenced absences.

| Entry point or operation | Source paths and evidence basis | Covering records or unresolved limit |
|---|---|---|
| Session save/load, legacy checkpoint conversion | Supplied runtime; direct `src/qwenpaw/agents/react_agent.py` searches and Scroll checkpoint implementation | [RT-OBJ-session-state](runtime.md#rt-obj-session-state), annotations below; native AgentScope summary generation remains dependency-owned |
| Memory backend registration, disabling, middleware | Direct `src/qwenpaw/agents/memory/__init__.py`, `src/qwenpaw/agents/memory/dummy.py`, `src/qwenpaw/agents/middlewares.py` | [MEM-RTE-trace-extraction](#mem-rte-trace-extraction), [MEM-RTE-memory-retrieval](#mem-rte-memory-retrieval); service-factory selection additionally located in `src/qwenpaw/app/workspace/workspace.py` |
| Auto-memory, manual `/memorize`, `/new`, `/compact` | Direct `src/qwenpaw/agents/command_handler.py`, `src/qwenpaw/agents/memory/base_memory_manager.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` | [MEM-RTE-trace-extraction](#mem-rte-trace-extraction); pending-turn snapshots preserve extraction inputs across compression |
| ReMe tools, jobs, cron declarations, maintenance, results | Direct `src/qwenpaw/agents/memory/reme_config.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` | [MEM-RTE-dream-maintenance](#mem-rte-dream-maintenance), [MEM-RTE-paper-maintenance](#mem-rte-paper-maintenance), [MEM-OBJ-inbox-event](#mem-obj-inbox-event); dependency step implementations and deployed scheduler activation unavailable |
| Explicit and automatic search, reranking, file expansion | Direct ReMe/ADBPG adapters, base query and synthetic-message helpers, memory middleware and guidance | [MEM-RTE-memory-retrieval](#mem-rte-memory-retrieval); internal ReMe hybrid scoring/index consistency not inspectable here |
| ADBPG admission and local fallback | Direct `src/qwenpaw/agents/memory/adbpg_memory_manager.py`, `src/qwenpaw/agents/memory/adbpg_client.py` | [MEM-RTE-adbpg-retention](#mem-rte-adbpg-retention); remote extraction, representation and deletion policy unresolved |
| Operator/API memory edits and working-file instructions | Direct `src/qwenpaw/agents/memory/agent_md_manager.py`; workspace router route searches; supplied runtime's full working-file route | [MEM-RTE-memory-edit](#mem-rte-memory-edit), [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction); generic caller identity does not prove human review |
| Scroll eviction, folding, summary, checkpoint and reload | Direct bounded sections of `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/agents/context/scroll/continuation_summary.py`; supplied runtime | [MEM-RTE-scroll-retention](#mem-rte-scroll-retention); full headline extraction and every eviction-index tier rule not inspected |
| Structured history recall and Python alternative | Direct `src/qwenpaw/agents/context/scroll/recall_tool.py`; searches in `src/qwenpaw/agents/context/scroll/memoryspace.py`; supplied builder findings | [MEM-RTE-history-recall](#mem-rte-history-recall); full Python REPL sandbox and custom SQL semantics uninspected |
| History migration, retention purge and stale-summary withdrawal | Direct searches in `src/qwenpaw/agents/context/scroll/history.py`, `src/qwenpaw/agents/context/scroll/sync.py`; direct manager withdrawal/checkpoint code | [MEM-OBJ-history](#mem-obj-history), [MEM-RTE-scroll-retention](#mem-rte-scroll-retention); no proof of complete erasure across other stores/backups |
| Native offloading, result pruning, debug history reload | Direct `src/qwenpaw/agents/offloader.py`, `src/qwenpaw/agents/tools/utils.py`, command handler; pruning middleware searches | [MEM-RTE-archive-replay](#mem-rte-archive-replay); exact middleware tier/exemption rules not fully traced |
| Request-time visual compression and exact recovery | Direct `src/qwenpaw/agents/context/visual_compression/runtime/middleware.py`, recovery helper excerpts | [MEM-RTE-visual-context](#mem-rte-visual-context); rendering-region selection, pixel encoding and precision algorithms available but uninspected; no semantic-losslessness conclusion |
| Idle proactive consumer | Direct `src/qwenpaw/agents/memory/proactive/proactive_trigger.py`, responder and utility excerpts | [MEM-RTE-proactive-context](#mem-rte-proactive-context); exact recent-session predicate and downstream delivery/persistence not fully inspected |
| Forked workers, Codex/Qoder threads | Supplied runtime only | [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker), [RT-RTE-harness-turn](runtime.md#rt-rte-harness-turn); fork snapshot details and external provider state opaque |
| Memory evaluator | Direct opening UI and seeded-recall test in `e2e/tests/test_memory.py` | [MEM-CLM-memory-evaluator](#mem-clm-memory-evaluator); tests were not run; integration/unit memory suites not inspected |
| Auxiliary retained state and restoration | Boundary inventory includes mail thread storage, governance state, backups, checkpoints, plugins and browser integrations | Not audited as long-term knowledge stores here. Runtime establishes tool-policy and plugin paths. Exact policy reuse, mail-thread read-back, backup restore admission and plugin-owned memory remain uninspected; no exhaustive whole-system forgetting or persistence guarantee follows |

## Core ideas

1. **Distilled memory and raw recovery are deliberately different routes.** ReMe configuration indexes daily/digest Markdown, while Scroll searches raw conversation history. A search over one is not evidence of coverage of the other ([MEM-OBJ-daily-note](#mem-obj-daily-note), [MEM-OBJ-history](#mem-obj-history)).
2. **Automatic retrieval is a constructed model-input interaction.** Code selects the latest external user query, searches once per turn, and injects a simulated completed `memory_search` interaction. Its thinking text is generated by the helper, not evidence that the foreground model decided to recall ([MEM-RTE-memory-retrieval](#mem-rte-memory-retrieval)).
3. **Scroll preserves recovery separately from compact task state.** Exact rows and pointers survive eviction, while a model generates a bounded continuation summary. Deterministic rejection checks and stale-state handling do not prove summary truth ([MEM-RTE-scroll-retention](#mem-rte-scroll-retention)).
4. **Admission is usually programmatic, not per-content human approval.** A user can edit Markdown and initiate maintenance, but automatic extraction and maintenance are not thereby reviewed by that user. ADBPG is a materially different, user-message-only outbound route with opaque server transformation ([MEM-RTE-adbpg-retention](#mem-rte-adbpg-retention)).

## Shared records

### Components

#### MEM-CMP-embedding-model
Label: Configured ReMe embedding model

Source-native identity: `as_embedding:default` and `embedding_model_config`. Storage substrate: configured external/local embedding provider; local cached vectors through `embedding_store`. Representational form: distributed-parametric embedding model and numerical vectors, distinct from natural-language Markdown and symbolic file metadata. Parameters changing during operation: uninspected provider internals; QwenPaw can replace the component, not demonstrated weight training. Exact model version pinned: not established by model-name configuration. Mutable endpoint resolving to another model: not excluded; model/base URL are configurable. This is distinct from inference [RT-CMP-active-model](runtime.md#rt-cmp-active-model), which ReMe reuses for LLM jobs.

SRC-1, `src/qwenpaw/agents/memory/reme_config.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation). Empty/uncredentialed configuration can remove embeddings and leave keyword indexing; embedding-enabled is not universal. A tested model can be hot-applied under a lifecycle lock. A vector-space change clears caches; explicit reindex clears the requirement only if fingerprints still match. These are retrieval-maintenance controls, not content verification or improved-recall evidence.

> self._reme.update_component(
>                     "as_embedding",
>                     "default",
>                     model=tested_model,
>                 )
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

#### MEM-CMP-reranker-model
Label: Optional configured reranker

Source-native identity: `RerankerConfig` and the adapter's reranker API. Substrate: configured external API, whose internal model storage is uninspected. Representational form: model-backed scoring behind symbolic requests and numerical candidate scores; internal parameter encoding is not exposed. Parameters changing during operation: uninspected. Exact immutable model version pinned: not established. Mutable endpoint resolving to another model: not excluded by configurable API integration. This component is distinct from [MEM-CMP-embedding-model](#mem-cmp-embedding-model) and [RT-CMP-active-model](runtime.md#rt-cmp-active-model).

SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation). Reordering, capping and failure fallback are locally inspectable; provider scoring internals and relevance benefits are not.

> await self._rerank_search_results(
>                     query,
>                     response,
>                     reranker_config,
>                 )
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

### Operative objects

#### MEM-OBJ-daily-note
Label: ReMe daily and session memory notes

Source-native identity: configured `daily_dir`, daily Markdown and topic-named session notes. Substrate: workspace files; form: natural-language extracted content, with symbolic paths/index links. Lineage: conversation messages passed to ReMe `auto_memory`; user/model edits are also afforded. Actual initialized contents and dependency extraction internals are unavailable. Consumers: search/indexing, later model file reads, dream maintenance and operator editors. No counterpart after comparison with [RT-OBJ-session-state](runtime.md#rt-obj-session-state): these are derived long-term notes, not serialized live agent state.

SRC-1, `src/qwenpaw/agents/memory/reme_config.py`, `src/qwenpaw/agents/memory/prompts.py` (configuration implementation and doctrine/design). The adapter wires extraction; exact filenames and factual-selection semantics are dependency contracts, not locally observed outputs.

> "description": (
>                     "Auto-memory: record conversation facts into a daily "
>                     "note"
>                 ),
> --- `src/qwenpaw/agents/memory/reme_config.py`

#### MEM-OBJ-digest
Label: ReMe digest and interest material

Source-native identity: `digest_dir`, `interests.yaml`, dream catalog and daily-paper notes. Substrate: configured workspace vault and local catalogs; natural-language digest/topic content is distinct from symbolic catalogs, paths and indexes. Lineage differs: dream derives from daily notes; daily paper incorporates external paper material. Search consumes indexed digest Markdown; maintenance jobs consume/update their configured inputs. Interest consumption by every downstream feature remains unresolved. This is not [RT-OBJ-prompt-files](runtime.md#rt-obj-prompt-files): existence does not automatically place these bodies in the system prompt.

SRC-1, `src/qwenpaw/agents/memory/reme_config.py` (implementation configuration and declared dependency job behavior), supporting passages in [MEM-RTE-dream-maintenance](#mem-rte-dream-maintenance) and [MEM-RTE-paper-maintenance](#mem-rte-paper-maintenance). Reasons or criticisms retained in actual notes are uninspected; the names “dream” and “digest” do not prove reflective criticism.

#### MEM-OBJ-history
Label: Scroll durable history

Source-native identity: `HistoryStore` and configured `history.db`. Substrate: workspace SQLite with text search. Form: symbolic rows, sequence IDs, tool-call/message identity and time metadata around natural-language/raw message and tool-result bodies. Lineage: write-through of live messages/tool results plus session-JSON migration. Exact raw text remains recoverable independently of a summary; earlier pruning may already have changed the incoming message, so “raw” is relative to the admitted representation. Consumer: `MemorySpace` recall queries and continuation-summary construction. Distinct from [RT-OBJ-session-state](runtime.md#rt-obj-session-state): durable historical rows are not the live-window checkpoint.

SRC-1, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/agents/context/scroll/history.py`, `src/qwenpaw/agents/context/scroll/sync.py` (implementation). Migration/retention searches locate a scroll-only importer, timestamp cutoff and manifest; their complete corruption/recovery algorithm remains uninspected. Purge is separate from erasing Markdown, session snapshots or exports.

> if not await self._persist_guarded_async(agent):
> --- `src/qwenpaw/agents/context/scroll/manager.py`

The supplied [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery) also retains that durability gate. The manager's checkpoint/purge and withdrawal passages below establish later consumers and expiry, rather than assuming durable means permanent.

#### MEM-OBJ-continuation-summary
Label: Scroll continuation summary
Part of: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Source-native identity: `continuation_summary`. Substrate: manager state serialized under the agent's Scroll checkpoint in session JSON. Form: natural-language task-state items plus symbolic version, status and source ranges. Lineage: previous valid summary plus bounded previews of newly archived turns and recoverable folded results, generated with the active model. Consumer: later model calls receive a rendered background state alongside the eviction index and raw tail. This material part is distinct from the parent live-message container and owns separate rejection and withdrawal rules.

SRC-1, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/agents/context/scroll/continuation_summary.py` (implementation).

> "continuation_summary": (
>                 self._continuation_summary.to_dict()
>                 if self._continuation_summary is not None
>                 else None
>             ),
> --- `src/qwenpaw/agents/context/scroll/manager.py`

No claim that the summary preserves all reasons is warranted: bounded previews and a task-state schema omit material. Exact archive ranges allow a later recall route to inspect supporting text; pointer existence is weaker than proposition-level support.

#### MEM-OBJ-eviction-index
Label: Scroll eviction index and recovery pointers
Part of: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Source-native identity: `index`, `seq_by_id`, `seq_by_tcid` and persisted bookkeeping. Substrate: manager checkpoint JSON; form: symbolic sequence spans, IDs and tiers, with natural-language headlines/previews. Lineage: code indexes evicted middle spans; not the generated continuation summary. Consumer: rendered model-input recovery map and later recall calls. Different rollback and accuracy properties justify separating it from [MEM-OBJ-continuation-summary](#mem-obj-continuation-summary); both are parts of the supplied session-state object.

SRC-1, `src/qwenpaw/agents/context/scroll/manager.py` (implementation).

> self._index.add_eviction(
>             leaves,
>             seq_lo=lo,
>             seq_hi=hi,
>         )
> --- `src/qwenpaw/agents/context/scroll/manager.py`

#### MEM-OBJ-adbpg-memory
Label: ADBPG retained service memory

Source-native identity: `/v3/memories/add/` and `/v3/memories/search/`. Substrate: external REST service, not inspected database internals. Form: outbound symbolic message/identity JSON with user text; returned `content`/`memory` text and scores. Internal retained payload, embeddings and server extraction provenance are opaque, not inferred from the product name. Later consumers receive filtered text, not a demonstrated full server record. Distinct from local session state [RT-OBJ-session-state](runtime.md#rt-obj-session-state) and local Markdown [MEM-OBJ-daily-note](#mem-obj-daily-note).

SRC-1, `src/qwenpaw/agents/memory/adbpg_client.py`, `src/qwenpaw/agents/memory/adbpg_memory_manager.py` (implementation); passages in [MEM-RTE-adbpg-retention](#mem-rte-adbpg-retention).

#### MEM-OBJ-inbox-event
Label: ReMe result notification

Source-native identity: `append_inbox_event`, memory job result payload. Substrate: application inbox service; exact storage implementation uninspected. Form: symbolic status/job/session/path metadata and a bounded natural-language body from `response.answer`. Lineage: auto-memory, dream or daily-paper result, not necessarily the full modified artifact. Consumer: operator inbox display; automatic adoption by another model is not established. Distinct from notes and supplied runtime objects: a display result is not the memory payload itself.

SRC-1, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation). Config can disable notifications; duplicate and successful-no-op results are suppressed, answers truncated. Thus empty inbox does not prove no maintenance, and a success display does not prove truth.

> answer = str(getattr(response, "answer", "") or "").strip()
>         if len(answer) > MAX_INBOX_BODY_CHARS:
>             answer = f"{answer[:MAX_INBOX_BODY_CHARS].rstrip()}\n..."
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

### Routes

#### MEM-RTE-trace-extraction
Label: Conversation trace to ReMe notes

Endpoints/progression: native reply or compression → `MemoryMiddleware` pending-turn batch/snapshots → memory manager queue → serial `summarize` worker → ReMe `auto_memory` → daily/session Markdown → later search/file read. Middleware/manager code owns scheduling, the configured model/dependency owns fact selection. This extends rather than duplicates [RT-RTE-native-turn](runtime.md#rt-rte-native-turn): it is the asynchronous derived-memory branch, not the response/session-save route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: foreground reply continues; scheduling and summary-status records are not proof of a committed note.
- Later read-back: indexed daily/digest material can reach a later invocation through [MEM-RTE-memory-retrieval](#mem-rte-memory-retrieval).
- Delegated visibility: ReMe receives serialized selected messages, normalized session identity and optional memory hint; it does not receive every independent store.
- Selection predicate: reply cadence uses manager interval and pending user-turn markers; compression preserves snapshots and can flush; automation requests skip this middleware behavior. Empty messages/session IDs skip ReMe work.
- Invalidation or expiry: pending lifecycle data can be reset; failed workers retain failure status; note expiry and dependency rollback are uninspected.
- Activation or effect: code requests model-dependent transformation into durable behavior-shaping text; actual note contents, later reliance and benefit unobserved.
- Evidence limits: queue completion is not independent validation of correctness, and ReMe's step implementation is outside SRC-1.

SRC-1, `src/qwenpaw/agents/middlewares.py`, `src/qwenpaw/agents/memory/base_memory_manager.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/command_handler.py` (implementation). Manual `/memorize` selects recent reply messages; `/new` schedules extraction before clearing; `/compact` can separately queue the evicted messages. These alternate admissions refute a cadence-only account. Filtering removes tagged synthetic auto-search blocks before extraction, reducing direct search-result feedback, not proving every tool result is trustworthy.

> all_messages = self._messages_without_auto_memory_search(all_messages)
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> response = await self._run_reme_job(
>             "auto_memory",
>             needs_llm=True,
>             messages=[message.model_dump(mode="json") for message in messages],
>             session_id=_to_reme_session_id(session_id),
>             memory_hint=str(kwargs.get("memory_hint") or ""),
>         )
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

Admission: software selects batches and invokes the model; no per-note human veto appears in this path. A caller starting `/memorize` is not approval of generated content. Operating mode: open conversations and manual maintenance, not a controlled improvement trial. No expected-answer oracle is supplied. Guidance asks extraction into daily notes; actual retained reasons are uninspected. Revision is capable of changing later context, but neither exercised learning nor successful self-improvement follows.

#### MEM-RTE-dream-maintenance
Label: Dream integration of retained notes

Endpoints/progression: configured cron or `/dream` hint → adapter `dream` → ReMe `auto_dream` configured extract/integrate/topics/finish steps → digest, interests and catalog → future indexing/retrieval. Adapter and service cron declarations own invocation; dependency/model own content transformation. Distinct from [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) and trace extraction: it operates on already retained notes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: adapter raises on unsuccessful response; command reports completion/error; optional inbox notification displays bounded results.
- Later read-back: digest Markdown participates in search; complete interests/catalog downstream consumer wiring remains uninspected.
- Delegated visibility: date/hint reach the job; configured extraction scope uses daily notes and prior digest material, not demonstrated full-session replay.
- Selection predicate: started ReMe plus enabled/nonempty dream cron, or explicit command; configured defaults include two scan days and five maximum units.
- Invalidation or expiry: job/tool configuration includes file move/delete capability; exact merge/rejection/deletion rules and versioned undo are dependency-owned and uninspected.
- Activation or effect: wired maintenance invocation can request revised knowledge artifacts; actual semantic consolidation and benefit unobserved.
- Evidence limits: job descriptions and step names establish intended dependency workflow, not inspected execution of its internals.

SRC-1, `src/qwenpaw/agents/memory/reme_config.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/command_handler.py` (implementation configuration and doctrine/design).

> "Auto-dream: scan today's day-index and daily notes, "
>                     "globally extract merged units/topics, integrate digest "
>                     "units, write interests.yaml, and persist the dream "
>                     "catalog."
> --- `src/qwenpaw/agents/memory/reme_config.py`

Admission: job/model transformation, not established human per-content review. Initiating a cron is not approving each change. Hint is proposal guidance; no independent answer oracle or controlled comparison is shown. The `/dream` “optimization” response label is not evidence of criticism, better memory or retention of reasons. Full rationale lineage remains unresolved at [MEM-OBJ-digest](#mem-obj-digest).

#### MEM-RTE-paper-maintenance
Label: Daily paper to retained digest

Endpoints/progression: configured service cron or exposed `daily_paper` operation → collect/rank/select/analyze/digest dependency steps → paper readings/brief → optional inbox result with digest/note/PDF paths. Distinct from dream and [RT-RTE-native-turn](runtime.md#rt-rte-native-turn): original inputs include external papers, not just user conversation traces.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: failure raises; successful returned body can be published as an inbox event.
- Later read-back: configured digest output can enter indexed Markdown; the exact artifact produced and its later use were not observed.
- Delegated visibility: topics/date/force/mirror settings reach ReMe; inbox gets selected IDs and paths when present, not necessarily full paper payloads.
- Selection predicate: enabled cron with a started backend, or caller operation; configuration sets candidate limit 20, weekly weight 0.7 and history 30 days.
- Invalidation or expiry: force requests regeneration; exact artifact withdrawal, deduplication and rollback remain dependency-internal.
- Activation or effect: adapter wires external-source acquisition and derived knowledge production; no claim of trustworthy papers or correct analysis.
- Evidence limits: dependency fetch/rank/analyze code, external PDFs and output artifacts were not supplied.

SRC-1, `src/qwenpaw/agents/memory/reme_config.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py` (implementation configuration and doctrine/design).

> "steps": [
>                     {"backend": "daily_paper_collect_step"},
>                     {"backend": "daily_paper_rank_step"},
>                     {"backend": "daily_paper_select_step"},
>                     {"backend": "daily_paper_analyze_step"},
>                     {"backend": "daily_paper_digest_step"},
>                 ],
> --- `src/qwenpaw/agents/memory/reme_config.py`

Admission: configured computational ranking and model analysis; per-paper human approval, answer oracle and semantic rejection criteria unestablished. Open scheduled information gathering, not an inspected improvement experiment. This is not attributed as trace-fed learning from QwenPaw's own behavior.

#### MEM-RTE-adbpg-retention
Label: User-message retention through ADBPG

Endpoints/progression: selected backend → post-reply or explicit summarize → user-role text filter → background REST add with configured identities → opaque server memory → later search. Client code owns filtering and I/O; remote service owns extraction/storage. No counterpart after comparison with [RT-OBJ-session-state](runtime.md#rt-obj-session-state): this is a separate outbound retention path.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tasks are scheduled without blocking the reply; `summarize` can say “Persisted” before confirmed remote storage.
- Later read-back: adapter searches by agent/user identity, filters score/content and combines with local file hits; search does not send run ID as a filter.
- Delegated visibility: only user-role text messages reach add, not assistant/tool traces as such; service receives identity fields and optional run ID.
- Selection predicate: configured client, interval one, and unseen user message IDs; explicit summarize filters user messages without that same dedup path.
- Invalidation or expiry: remote expiry/delete/rollback uninspected; IDs are marked after scheduling, and add catches errors, so those IDs do not prove successful retention or automatic retry.
- Activation or effect: code establishes outbound admission and return of retained text into later model context; service fact extraction and behavior change unobserved.
- Evidence limits: no remote server source/state; local fallback means a successful search need not witness successful ADBPG writes.

SRC-1, `src/qwenpaw/agents/memory/adbpg_memory_manager.py`, `src/qwenpaw/agents/memory/adbpg_client.py` (implementation).

> self._schedule_add([single])
> 
>         # Track persisted message IDs
>         for msg in new_messages:
>             self._persisted_msg_ids.add(msg.id)
> --- `src/qwenpaw/agents/memory/adbpg_memory_manager.py`

> _ = run_id
> --- `src/qwenpaw/agents/memory/adbpg_client.py`

Admission is software-driven forwarding; user authorship of the source text does not establish approval of the server's derived facts. Operating mode: open conversations; no answer oracle. Fact-extraction claim is attributed to adapter doctrine, not an inspected server transformation. Its stored reasons and original-message retention are unresolved.

#### MEM-RTE-memory-retrieval
Label: Explicit and automatic memory retrieval

Endpoints/progression: foreground model tool query OR pre-model middleware selection → backend search → optional ReMe rerank/cap/reconstruction or ADBPG score/local-paragraph filtering → model input. Owners: foreground model for explicit requests, code for automatic selection, backend for candidates. This is distinct from [RT-RTE-native-turn](runtime.md#rt-rte-native-turn): it selects previously retained content rather than accumulating a current tool result alone.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: explicit `ToolChunk` result or temporary injected synthetic assistant/tool interaction.
- Later read-back: selected snippets and paths reach subsequent model calls; guidance affords `read_file` expansion when snippets are insufficient.
- Delegated visibility: backend receives query and result budget; explicit ReMe defaults to five results, automatic budget is configurable; child/backend projection is not universally established.
- Selection predicate: explicit query or enabled auto-search, latest external user turn, truncated query text, backend candidate selector, score threshold and result cap. Middleware caches by turn marker, resets on a new turn and skips automation.
- Invalidation or expiry: cache replacement is per-turn; changed underlying notes are not guaranteed to refresh within the same turn; backend index coherence is dependency-owned.
- Activation or effect: relevant text is delivered as evidence/context, not an executable rule; actual compliance or improved answers unobserved.
- Evidence limits: synthetic thinking is helper-authored; relevance and fact truth are not proven by scores, tool success or injection.

SRC-1, `src/qwenpaw/agents/middlewares.py`, `src/qwenpaw/agents/memory/base_memory_manager.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `src/qwenpaw/agents/memory/adbpg_memory_manager.py`, `src/qwenpaw/agents/memory/prompts.py` (implementation plus guidance).

> self._build_auto_memory_search_msg(
>             query=query,
>             max_results=cap,
>             text=text,
>             estimate_divisor=self._resolve_token_estimate_divisor(
>                 agent_config,
>             ),
>         )
> --- `src/qwenpaw/agents/memory/reme_light_memory_manager.py`

> thinking_text = (
>             f"{AUTO_MEMORY_SEARCH_THINKING_PREFIX} I will use the "
>             f"memory_search with the user's query as the search keywords, "
>             f"request up to {max_results} result"
>             f"{'' if max_results == 1 else 's'}."
>         )
> --- `src/qwenpaw/agents/memory/base_memory_manager.py`

ReMe overfetches when a reranker is configured, catches reranker failure, caps results and rebuilds answer text while attempting to preserve linked expansions. The cap is a result-count budget, not demonstrated token bound. ADBPG local fallback keyword-scores paragraphs of `MEMORY.md` and direct `memory/*.md`, truncating snippets to 500 characters. It is not recursive ReMe-equivalent coverage.

> watch_dirs = ["daily_dir", "digest_dir"]
>     watch_suffixes = ["md"]
> --- `src/qwenpaw/agents/memory/reme_config.py`

This positive selector also prevents assuming raw logs or root `MEMORY.md` are automatically in the ReMe index. Static memory guidance is delivered as instructions; retrieved note text is delivered as tool evidence. Trust in source content remains model-interpreted, not independently verified.

#### MEM-RTE-memory-edit
Label: Managed memory Markdown replacement

Endpoints/progression: console/API daily/digest write → manager normalizes path and asserts containment → file replacement → later index/search or file read. API caller proposes, manager admits physically. This parallels but does not duplicate [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction): daily/digest artifacts are a different referent from configured root prompt files.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: file write acknowledgement/error through workspace API.
- Later read-back: memory list/read APIs and subsequent retrieval/file reads can expose replacement text; dependency index refresh timing unobserved.
- Delegated visibility: inapplicable — this route edits a file, not a worker handoff; subsequent consumer projection is separate.
- Selection predicate: selected workspace, daily/digest section, normalized Markdown path and resolved containment.
- Invalidation or expiry: rewriting replaces content; no versioned undo or content expiry is established in this method.
- Activation or effect: admitted text can influence future inference after selection; it is not automatically a system prompt merely because stored as Markdown.
- Evidence limits: API authorization, actual caller identity and semantic approval were not established by path validation.

SRC-1, `src/qwenpaw/agents/memory/agent_md_manager.py`, `src/qwenpaw/app/routers/workspace.py` (implementation).

> file_path = self._memory_path_for_read_write(md_name, section)
>         file_path.parent.mkdir(parents=True, exist_ok=True)
>         file_path.write_text(content, encoding="utf-8")
> --- `src/qwenpaw/agents/memory/agent_md_manager.py`

Admission separates caller authorship from structural checks: no fact validator or answer oracle in the inspected write. Human editing is possible, not inferred for every caller. Ordinary file tools are additionally encouraged by memory guidance; this managed API is not the exclusive write gate. General tool governance remains bounded as in [RT-RTE-tool-governance](runtime.md#rt-rte-tool-governance).

#### MEM-RTE-scroll-retention
Label: Scroll archival and continuation state

Endpoints/progression: native compression/overflow/manual compact → persist live content → token accounting → fold eligible tool outputs and/or evict old dialogue → index plus validated continuation summary plus raw tail → checkpoint → reload and later model input. Owner: Scroll code for policy/admission, active model for summary text, session hooks for cross-request retention. Distinct detail within [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery), whose one provider-overflow retry is not redeclared here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed context and compression statistics, or an unfit-window error; not a new task answer.
- Later read-back: index and summary render into later calls; session checkpoint reload carries them across native requests; exact archived rows can be separately recalled.
- Delegated visibility: bounded prior summary and archived evidence go to a summary model call without tools; no complete-history delegation is implied.
- Selection predicate: token threshold or forced compaction; completed-turn recoverable tool results preferred, recent five results and active turn protected under normal pressure; stronger pressure can fold already-consumed active results.
- Invalidation or expiry: invalid candidate rejected with at most one repair retry; timeout/provider failure preserves previous summary as stale. Missing provenance endpoints withdraw an old summary on reconciliation of restored context. History retention can remove recoverable rows.
- Activation or effect: code changes future model-visible context and requests compact task state; successful task continuation or factual completeness unobserved.
- Evidence limits: durability is conditional on successful local writes; summary quality checks do not entail semantic correctness or indefinite recovery.

SRC-1, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/agents/context/scroll/continuation_summary.py` (implementation). The recent raw reserve is bounded between a useful minimum and 40,000 tokens; output reserve reduces the effective hard limit. Summary input fitting counts model tokens, shrinks archived preview text from an 80,000-character ceiling, and reserves output between 256 and 4,000 tokens. Index rendering has its own bounded character budget. These are different budgets, not a single losslessness guarantee.

> output_tokens = max(256, min(4000, context_size // 4))
> --- `src/qwenpaw/agents/context/scroll/manager.py`

> issues = validate_summary_quality(
>             candidate,
>             evidence_text=evidence_text,
>             existing_seqs=existing_seqs,
>         )
>         if issues:
>             raise _SummaryCandidateError("; ".join(issues))
>         return candidate
> --- `src/qwenpaw/agents/context/scroll/manager.py`

> invented = sorted(extract_identifiers(rendered) - allowed_identifiers)
> --- `src/qwenpaw/agents/context/scroll/continuation_summary.py`

Admission: parser/format/secret/duplicate/identifier/pointer checks decide candidate acceptance; the model proposes, not an independent truth oracle. Source-range endpoints are checked, not every proposition's support. No per-summary human approval is shown. Guidance requests task-state replacement, preserves relevant baseline items and treats focus hints as subordinate to evidence; the actual output's retained reasons remain unobserved. This is a trace-fed derived-memory path, not proof of improved capacity or theory criticism.

> if existing == endpoints:
>             return previous
> --- `src/qwenpaw/agents/context/scroll/manager.py`

The following branch clears unsupported state rather than silently attributing it to new evidence:

> self._continuation_summary = None
>         return None
> --- `src/qwenpaw/agents/context/scroll/manager.py`

Delivery is a user-role synthetic message even though its content uses a `system-info` envelope:

> placeholder = UserMsg(
>             name="memory",
>             content=memory,
>             metadata={
>                 QWENPAW_MESSAGE_TAG_KEY: SCROLL_MEMORY_MESSAGE_TAG,
>             },
>         )
> --- `src/qwenpaw/agents/context/scroll/manager.py`

This counterexample prevents classifying every memory hint as actual system-role authority.

#### MEM-RTE-history-recall
Label: On-demand Scroll history recall

Endpoints/progression: model `recall_history` operation with scalar parameters → fresh bound `MemorySpace` → read-only history query → bounded paginated text → foreground context. Separate `recall_history_python` affords model-authored Python under a sandbox gate, as supplied runtime establishes. This is distinct from [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery): it reintroduces selected removed material rather than compressing the window.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bounded text page, continuation cursor or explicit execution error; `days_between` computes a date result rather than reading retained memory.
- Later read-back: sequence spans, tool-call IDs, keyword/date/session/agent selectors select retained rows for a later model invocation.
- Delegated visibility: scalar selectors enter structured queries; Python alternative receives a separate execution context, not blanket foreground-tool authority.
- Selection predicate: operation `expand`, `search`, `recall_tool` or date calculation; query budget, scope filters and page byte cap constrain results; duplicate-page loop guard prevents identical recall repetition within a turn.
- Invalidation or expiry: retention/purge can remove source rows; cursor fingerprint mismatch rejects a changed snapshot; exact same page can be blocked rather than re-read indefinitely.
- Activation or effect: selected archived evidence is delivered as tool output; whether the model uses it accurately is unobserved.
- Evidence limits: complete memoryspace SQL/filter and Python sandbox internals uninspected; no cross-agent isolation guarantee asserted from selector names.

SRC-1, `src/qwenpaw/agents/context/scroll/recall_tool.py`, `src/qwenpaw/agents/context/scroll/memoryspace.py` (implementation); builder gates are supplied by [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery).

> return MemorySpace(
>             history_db_path=history_db_path,
>             session_id=session_id,
>             agent_id=agent_id,
>         )
> --- `src/qwenpaw/agents/context/scroll/recall_tool.py`

> "the history was NOT read. This is an execution error, not an empty "
>         "history: fix the parameters and retry, or say explicitly that you "
>         "could not retrieve the context"
> --- `src/qwenpaw/agents/context/scroll/recall_tool.py`

Recovery pointers are instructions to copy values back, not live heap references. Their presence neither pins rows against expiry nor automatically refreshes previously injected text.

#### MEM-RTE-archive-replay
Label: Native archives, pruning and debug replay

Endpoints/progression: native compaction/clear or large tool output → date-grouped JSONL / UUID text artifact → path-bearing truncation or operator export → read or explicit `/load_history` → replaced live state. Offloader/pruner/command code owns physical retention and structural replay. Distinct from [RT-OBJ-session-state](runtime.md#rt-obj-session-state): debug JSONL and tool artifacts are alternative checkpoint/recovery forms, not normal session hook JSON.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved path or shortened tool observation; clear/new can reset context; load-history reports replacement status.
- Later read-back: file paths afford targeted file reads; `/load_history` explicitly restores bounded JSONL messages and an optional marked native compressed summary into state for later calls.
- Delegated visibility: inapplicable — these are local file/checkpoint operations, not child task delegation.
- Selection predicate: tool text exceeding byte threshold is saved before fresh truncation; command selects configured debug-history file; native compaction itself is dependency-owned.
- Invalidation or expiry: tool-result cleanup method deletes old text files; scheduling of every cleanup caller uninspected. Load-history clears prior context/summary and resets auto-memory caches; malformed input can fail, without a demonstrated transactional rollback.
- Activation or effect: shorter observations or restored history affect later context; no automatic consumer of every date-grouped JSONL archive was established.
- Evidence limits: file retention alone is not a read-back route; debug replay is explicit and does not prove full Scroll-manager checkpoint restoration.

SRC-1, `src/qwenpaw/agents/offloader.py`, `src/qwenpaw/agents/tools/utils.py`, `src/qwenpaw/agents/command_handler.py` (implementation). JSONL message serialization is symbolic framing around natural-language/raw blocks; UUID text artifacts hold tool evidence, not distilled knowledge. Date archives intentionally mix sessions; session identity is not a partition guarantee there. Fresh pruning failure preserves original text rather than discarding undurable content.

> saved_path = self._save_fresh_text(text, encoding)
>         if saved_path is None:
>             return text, {}
> --- `src/qwenpaw/agents/tools/utils.py`

> self._state.context.clear()
>             self._set_summary("")
> --- `src/qwenpaw/agents/command_handler.py`

Admission/replay: caller selects dump/load; parser accepts bounded message JSON and summary marker, with no inspected expected-answer/content-quality gate. Human authorship or review of the file is unresolved. External archive readers are only afforded when named by documentation; a storage path alone is not counted as an automatic knowledge consumer. The native summary plus JSONL alternative coexists with Scroll's separate summary/index checkpoint.

#### MEM-RTE-visual-context
Label: Request-time visual context and recovery

Endpoints/progression: enabled pre-model middleware → capability/media checks → request transform/render → image-bearing messages/tool schema transformation and recoverable-source receipt → model request or exact-text recovery. Owner: code transformation, not a summarizing LLM. Distinct from [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery): this is a request projection, not demonstrated durable summary replacement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: transformed request or original request on skip/failure.
- Later read-back: inapplicable — inspected recovery store is turn-local; no cross-turn durable visual-memory path established.
- Delegated visibility: transformed messages/tools reach inference; exact source text can be recovered by bounded character/line/query selectors.
- Selection predicate: enabled feature, image-capable current model, media not stripped, configured effort preset and transformation algorithm; exact region choices remain uninspected.
- Invalidation or expiry: recovery receipt is replaced per transform and cleared on disabled/unsupported/error branches; durable persistence not established.
- Activation or effect: changes model-visible encoding and exposes exact-text recovery; semantic equivalence and token benefit unobserved.
- Evidence limits: rendering/precision/pipeline internals not fully traced; visual encoding is not itself a new distributed-parametric memory store.

SRC-1, `src/qwenpaw/agents/context/visual_compression/runtime/middleware.py`, `src/qwenpaw/agents/context/visual_compression/runtime/recovery.py` (implementation).

> self._recovery_store.replace(receipt.recoverable)
>         request["messages"] = transformed
>         request["tools"] = transformed_tools
> --- `src/qwenpaw/agents/context/visual_compression/runtime/middleware.py`

This represents text to a vision-capable model through images while preserving turn-local exact text separately. It is working-context control, not proof of durable memory learning.

#### MEM-RTE-proactive-context
Label: Idle-triggered session-context consumer

Endpoints/progression: enable proactive monitoring → idle/cooldown/busy checks → new proactive agent → selected saved-session text plus optional screen analysis → task extraction → up to three task attempts → final-message generation. Owner: trigger code and separate model-backed agent. Distinct consumer of [RT-OBJ-session-state](runtime.md#rt-obj-session-state), not duplicate normal session restoration or ReMe search.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated message or interruption/no result; enable/disable returns confirmation and starts/stops in-process monitor tasks.
- Later read-back: utility loads saved session contexts and passes cleaned text to a new agent invocation; it does not show a ReMe proactive-job call on this route.
- Delegated visibility: separate agent gets selected text and screen-derived context, not the complete foreground state; generated result returns, not its entire evolving context.
- Selection predicate: enabled idle threshold with cooldown and busy checks; utility filters recent sessions and defaults to 100 messages / 50,000 session characters; exact recent-session predicate remains uninspected.
- Invalidation or expiry: disable cancels monitor/removes in-process configuration; new interaction can interrupt generation; downstream message persistence/delivery not fully traced.
- Activation or effect: retained session text can guide task proposals and tool work; actual unsolicited behavior and usefulness unobserved.
- Evidence limits: independent from ReMe interests by inspected caller; no universal sandbox guarantee, full delivery guarantee or exact task-selection fidelity established.

SRC-1, `src/qwenpaw/agents/memory/proactive/proactive_trigger.py`, `src/qwenpaw/agents/memory/proactive/proactive_responder.py`, `src/qwenpaw/agents/memory/proactive/proactive_utils.py` (implementation).

> tasks = await _extract_tasks_from_memory(memory_context_str, agent)
> --- `src/qwenpaw/agents/memory/proactive/proactive_responder.py`

> if msg.role == "system":
>         return None
> --- `src/qwenpaw/agents/memory/proactive/proactive_utils.py`

Cleaning retains text blocks and omits system messages; legacy parsing does not by itself preserve the native summary as equivalent full history. The proactive agent initializes bypass permission context and a separately assembled toolkit, so native governor claims cannot silently extend to it. The supplied [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker) is another context-isolation mechanism, but not this agent. Both resemble a frame in their selected input/result boundary; neither establishes heap-style live references to retained context.

### Claims

#### MEM-CLM-memory-evaluator
Label: Seeded recall evaluator rather than measured recall quality

Claimed operation: shipped memory E2E test intends that seeded daily-memory content be recalled in a chat reply. Source: SRC-1, `e2e/tests/test_memory.py` (doctrine/design and encoded test expectation). Distinct from [RT-CLM-assistant-work](runtime.md#rt-clm-assistant-work): this is an evaluator contract, not a product claim.

> @pytest.mark.xfail(
>         reason=(
>             "Requires a configured LLM and may also need embedding "
>             "infrastructure; environments without them will not recall "
>             "the seeded keyword."
>         ),
>         strict=False,
>     )
> --- `e2e/tests/test_memory.py`

The test also places the unique keyword in the user query. Merely checking its appearance in a reply cannot distinguish memory recall from copying the current query. UI configuration persistence tests assess settings/UI, not fact-extraction truth. No test was executed; no retrieval-quality or causal benefit result is declared.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-context
Label: Retained content to later model decisions

Consumer: native model calls and the separate proactive agent. Channel: retrieved tool text/synthetic assistant interaction, restored context, Scroll user-role background message, or proactive extraction prompt. Force: natural-language evidence/guidance interpreted by a model, not deterministic enforcement or demonstrated compliance. Horizon: later calls and native sessions while retained state remains available and selected. The update consumer (ReMe/model/service) differs from the downstream task consumer. Distinct from [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt), whose channel is actual system-prompt composition.

SRC-1, `src/qwenpaw/agents/middlewares.py`, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/agents/memory/proactive/proactive_responder.py` (implementation); passages and selectors in [MEM-RTE-memory-retrieval](#mem-rte-memory-retrieval), [MEM-RTE-scroll-retention](#mem-rte-scroll-retention), [MEM-RTE-proactive-context](#mem-rte-proactive-context). Delivery establishes a live behavior-shaping capacity, not observed reliance, increased competence or evidence-responsive self-improvement.

## Annotations

#### On [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Lineage and parts: raw/live context, native summary, pending auto-memory markers/snapshots and Scroll state have different producers. The new continuation-summary and eviction-index records above are material parts, not replacements for the whole session container. `QwenPawAgent` persists/restores Scroll bookkeeping separately from AgentState; legacy memory conversion can restore messages and native summary. SRC-1, `src/qwenpaw/agents/react_agent.py`, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/agents/middlewares.py` (implementation). Checkpointing does not make cached retrieval, derived summary or raw history equivalent. Proactive read-back cleans the saved context before another agent sees it; it is not full-state delegation.

#### On [RT-OBJ-prompt-files](runtime.md#rt-obj-prompt-files)

Memory-specific authority: mutable workspace instructions can shape later system prompts, but default file selection is not a complete memory search. Root `MEMORY.md` is encouraged as editable long-term memory by guidance, whereas ReMe's explicit index watch scope is daily/digest Markdown and ADBPG fallback explicitly includes root `MEMORY.md`. These consumers must not be conflated. SRC-1, `src/qwenpaw/agents/memory/prompts.py`, `src/qwenpaw/agents/memory/reme_config.py`, `src/qwenpaw/agents/memory/adbpg_memory_manager.py`; supplied prompt selection and authority remain [RT-RTE-workspace-instruction](runtime.md#rt-rte-workspace-instruction) and [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt).

## Write side

Automatic trace-fed writes are not just raw logs. [MEM-RTE-trace-extraction](#mem-rte-trace-extraction) requests derived daily/session notes from selected conversation batches; [MEM-RTE-scroll-retention](#mem-rte-scroll-retention) requests compact task-state replacement from archived evidence; both have later consumers. Original sources can include user, assistant and tool content in ReMe batches, while tagged synthetic auto-search blocks are excluded. ADBPG instead forwards user text only, and its server-derived result remains opaque. Retained traces alone in [MEM-OBJ-history](#mem-obj-history) are recovery evidence, not demonstrated learning.

Admission is per mechanism. Background model extraction, deterministic summary checks, remote service acceptance, generic caller file replacement, and foreground file tools do not share one approval gate. Known subsequent transformations remain established even though initial user-workspace contents and dependency algorithms are unknown. [MEM-RTE-dream-maintenance](#mem-rte-dream-maintenance) transforms retained notes; [MEM-RTE-paper-maintenance](#mem-rte-paper-maintenance) mixes external source material. Starting either job is not per-content human review. [MEM-RTE-memory-edit](#mem-rte-memory-edit) affords direct human or computational replacement, but generic API authorship is unresolved.

Rejection and withdrawal differ from generation. Scroll locally rejects malformed, secret-bearing, duplicate or unsupported-identifier candidates, retries a quality failure once, preserves prior valid state on failure and removes stale provenance-linked summary on reload reconciliation. These are bounded checks, not an answer oracle. ReMe embedding changes invalidate vector caches and can require explicit reindex; this changes access representations, not note truth. ReMe's delete/move tool configuration and dream step names do not establish its full semantic withdrawal algorithm. History purge and tool-artifact cleanup are separate retention operations; clearing the live window does not erase every archive, note or remote record. [MEM-RTE-archive-replay](#mem-rte-archive-replay) shows that `/clear` may first archive the old context.

No actual note or summary was supplied to inspect preservation of reasons. Scroll retains source spans and allows later raw recall, but compact task state is not the full causal rationale. ReMe guidance requests daily facts and digests; exact criticism/rationale retention and subsequent rationale-reading routes remain unresolved. The report therefore establishes maintained behavior-shaping representations, not theory-builder conditions, measured learning or successful self-improvement.

## Read-back

Read-back is established by a consumer, not by a save method. Native session reload is supplied in [RT-RTE-native-turn](runtime.md#rt-rte-native-turn); specialist inspection separates its summary/index parts. Explicit search is foreground-requested; auto-search is code-triggered by a new external user query and temporarily injects results without a foreground tool decision. It is automatic context supply, not independent idle initiative. Idle initiative is the separate [MEM-RTE-proactive-context](#mem-rte-proactive-context), whose selected sessions undergo text/system filtering before consumption.

Raw Scroll recall is targeted by sequence, tool-call, keyword/date and scope selectors; its page caps and loop/cursor guards differ from result-count caps in ReMe. Memory guidance affords progressive file expansion. Root `MEMORY.md`, daily/digest Markdown, `history.db`, native date JSONL, debug JSONL and external harness threads are not interchangeable retrieval universes. ReMe's configured index explicitly leaves raw conversation lookup to Scroll. Native archives without a named automatic reader remain storage capability, while debug history has an explicit replay consumer. Harness thread resume is supplied as [RT-RTE-harness-turn](runtime.md#rt-rte-harness-turn), with provider retention semantics uninspected.

Working-context control includes pruning, visual request projection, Scroll eviction/folding, native dependency compaction and child-agent isolation. Pruning retains pointers only after saving fresh large text; visual recovery is turn-local. Scroll retains a recent tail and code-managed index plus derived state; a later recall copies archived values into the window. A separate worker returns selected results rather than keeping its whole window live in the parent, as [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker) establishes. The frame analogy helps describe isolation and return; it fails if taken to imply live references, liveness tracking or automatic reachability of every persisted item.

## Integration issues

- **No supplied fact requires correction.** Runtime explicitly left extraction, recall and summary details unresolved. This report fills those gaps without broadening its native/harness guarantee scope.
- **Containment, not duplicate replacement:** [MEM-OBJ-continuation-summary](#mem-obj-continuation-summary) and [MEM-OBJ-eviction-index](#mem-obj-eviction-index) are separately assessed parts of [RT-OBJ-session-state](runtime.md#rt-obj-session-state). The parent remains valid. [MEM-RTE-scroll-retention](#mem-rte-scroll-retention) overlaps the compression phase of [RT-RTE-context-recovery](runtime.md#rt-rte-context-recovery), but adds extraction/admission/withdrawal and checkpoint consumers; the runtime record includes the distinct provider retry. No other possible duplicate was found after comparison with supplied records.
- **Dependency-owned transformations:** [MEM-OBJ-daily-note](#mem-obj-daily-note), [MEM-OBJ-digest](#mem-obj-digest) and their maintenance routes have inspected adapter wiring/configuration, not inspected ReMe step algorithms. Reconciliation must retain that split rather than upgrade a described merge/delete to observed or fully audited curation.
- **ADBPG persistence acknowledgements are weak:** [MEM-RTE-adbpg-retention](#mem-rte-adbpg-retention) marks IDs after scheduling and the client catches add errors. Remote record semantics, retry reliability, reasons and forgetting remain unknown. This prevents treating returned “Persisted” text as a storage receipt.
- **Selector/authority distinctions:** [MEM-RTE-memory-retrieval](#mem-rte-memory-retrieval) synthesizes assistant thinking/tool interaction; [MEM-RTE-scroll-retention](#mem-rte-scroll-retention) injects user-role background text. Neither should be merged with [RT-BAP-workspace-prompt](runtime.md#rt-bap-workspace-prompt) solely because source comments use “system” or “memory.”
- **Proactive alternate consumer:** [MEM-RTE-proactive-context](#mem-rte-proactive-context) reads saved session text through a separate agent with bypass permission context. Its remaining recent-session predicate and final delivery/persistence details are uninspected. This is an additional limit to universal native governance attribution, not a defect in the runtime's already bounded claims.
- **Unresolved included alternatives:** coverage table names available but uninspected visual pipeline/REPL/eviction tier details, governance reuse, auxiliary mail threads, backup restoration and plugin-owned stores. No complete forgetting, lossless compression, all-caller tenant isolation or whole-system memory inventory is asserted. External dependency internals, actual workspaces and run evidence are unavailable, a different limit from these available uninspected sources.
- **Evaluation cannot establish benefit:** [MEM-CLM-memory-evaluator](#mem-clm-memory-evaluator) is unexecuted and its seeded keyword also appears in the question. It is not an independent witness of successful retrieval or learning.

## Limitations and checks

The frozen source identity was rechecked with `git rev-parse HEAD`, matching the full boundary revision. All cited new paths belong to SRC-1 at that commit. Source-only inspection distinguishes adapter implementation from dependency contract and unobserved deployment. No missing execution evidence is used to infer an absent mechanism. Read/search errors at guessed paths supplied no negative evidence; actual located paths were inspected instead.

No external model/service internals, workspace contents, actual generated notes, supplied traces or experiments were available. Therefore semantic correctness, successful persistence under failures, actual model reliance, causal learning, exercised self-improvement, retrieval quality and complete deletion are not established. Faithfully bounded implementation findings remain positive despite those limits.

Deterministic validation: `commonplace-run validate-output` passed against this invocation. It reported “Member content check passes; invocation residue not checked.” This establishes checked form and quotation occurrence, not semantic adequacy, job acceptance or claim support.
