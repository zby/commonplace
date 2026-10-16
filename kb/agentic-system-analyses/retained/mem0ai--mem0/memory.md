---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Mem0 memory: additive and direct writes, separate traces and indexes, expiry counterpaths, and shipped agent recall/capture consumers."
run-id: AAS-2026-10-14-mem0-5b642a1731b4-01
source-identity: "https://github.com/mem0ai/mem0"
reviewed-boundary: "0724291bd864cf807e88ee8981c8226644e8fb42"
---

# Mem0 memory report

## Boundary and evidence

Mem0 retains conversation-derived text and indexes it for later extraction and answer generation. This report keeps the boundary's **complete artifact, partial loop**: the hosted backend and evaluation-submodule contents are unavailable. All source evidence is SRC-1 at the frozen commit. No target code, model, test, example or service was executed. Implementation establishes wiring, not exercised retention, truthful extraction, successful recovery or improved answers.

Direct reads added Python persistence, extraction, entity indexing, ranking and mutation bodies; TypeScript persistence/search portions; OpenClaw recall and triage instructions; Claude Code hooks, checkpoint conversion and recall formatting; Hermes prefetch, sync and tools; and the Pi adapter's shared lifecycle. Runtime findings are supplied evidence, not automatically direct inspection. The following inventory distinguishes these layers and preserves unresolved included parts rather than assuming parity. Source paths in the table are SRC-1 implementation anchors unless identified as instructions.

| Entry point or memory part | Evidence and coverage | Records or local limit |
| --- | --- | --- |
| Python inferred `Memory.add` | Direct: `mem0/memory/main.py`, `mem0/memory/storage.py`; additive prompt passage supplied by runtime | [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), annotations below; text, traces and indexes separated below |
| Python raw/procedural add, update/delete/delete-all/history/reset | Direct: `mem0/memory/main.py`, `mem0/memory/storage.py` | [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), [MEM-OBJ-procedural-memory](#mem-obj-procedural-memory), [MEM-OBJ-history](#mem-obj-history); deletion is not complete trace erasure |
| Python public search and ID lookup; extraction's private retrieval | Direct ranking and extraction bodies: `mem0/memory/main.py`; runtime supplies public validation/get-all and README driver | [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories), [RT-BAP-extraction-context](runtime.md#rt-bap-extraction-context); expiry differs by route |
| Async Python engine | Supplied runtime tracing in `mem0/memory/main.py`; this report does not re-audit all async methods | [RT-RTE-extract-add](runtime.md#rt-rte-extract-add); sync details are not universal async guarantees |
| TypeScript OSS inferred/raw addition and search | Direct post-extraction insertion, return, get and ranking portions: `mem0-ts/src/oss/src/memory/index.ts`; supplied runtime extraction account | [MEM-RTE-typescript-memory](#mem-rte-typescript-memory); raw details, provider-specific history and all mutation parity remain uninspected |
| SQLite versus alternative history stores | Direct Python SQLite; TypeScript storage files inventoried under `mem0-ts/src/oss/src/storage/` | [MEM-OBJ-messages](#mem-obj-messages); TypeScript optional save/load calls do not prove equivalent retention for Dummy/Supabase/SQLite managers |
| Model/embedder/vector-store/reranker variants | Supplied default model records; direct engine factory/use sites in `mem0/memory/main.py` | [RT-CMP-openai-llm](runtime.md#rt-cmp-openai-llm), [RT-CMP-openai-embedding](runtime.md#rt-cmp-openai-embedding); adapter internals, exact models and database durability remain provider-specific/uninspected |
| Hosted Python and TypeScript clients | Python supplied: `mem0/client/main.py`; TypeScript used by directly inspected Pi adapter | [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client), [MEM-RTE-pi-memory](#mem-rte-pi-memory); backend admission, lifecycle and store encoding are opaque |
| Server configuration, HTTP CRUD, admin listing | Supplied: `server/main.py`, `server/server_state.py`, `server/auth.py` | [RT-RTE-server-access](runtime.md#rt-rte-server-access), [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config); dashboard editing/refresh flows uninspected, so no UI consistency claim |
| README answer driver and proxy | Supplied source passages and incompatibility findings: `README.md`, `mem0/proxy/main.py` | [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories), [RT-RTE-proxy-chat](runtime.md#rt-rte-proxy-chat); proxy is not a verified working read-back path |
| OpenClaw hooks, tools and instruction protocol | Direct `integrations/openclaw/recall.ts` and portions of `integrations/openclaw/skills/memory-triage/SKILL.md`; supplied hook/add bodies | [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add); provider translation and category TTL enforcement not fully inspected |
| Claude Code capture/PreCompact/SessionEnd, first-prompt and MCP recall, sidekick | Direct `integrations/claude-code-plugin/hooks/hooks.json`, `integrations/claude-code-plugin/core/memory_core.py`, `integrations/claude-code-plugin/core/hook_runner.py`, `integrations/claude-code-plugin/core/mcp_server.py`, `integrations/claude-code-plugin/agents/sidekick.md` | [MEM-RTE-coding-flush](#mem-rte-coding-flush), [MEM-RTE-coding-recall](#mem-rte-coding-recall); worker scheduling/recovery only partly inspected |
| Shared Python and other coding-agent builds | Inventoried `integrations/agent-plugin-core/`, `integrations/mem0-agent-plugin/`, `integrations/codex-plugin/`, `integrations/kimi-plugin/`, `integrations/cursor-plugin/`, `integrations/antigravity-plugin/`, `integrations/deepseek-plugin/`, `integrations/opencode-plugin/` | Their adapters, build equality and host-specific capture/compaction differences remain uninspected. Claude Code findings cannot establish their loops; this is a coverage limit, not an exclusion or absence |
| Pi capture/recall and shared TypeScript lifecycle | Direct `integrations/pi-agent-plugin/src/entry.ts`, `integrations/pi-agent-plugin/src/capture/index.ts`, `integrations/agent-plugin-core/typescript/src/lifecycle.ts` | [MEM-RTE-pi-memory](#mem-rte-pi-memory); explicit tools/commands and scope resolver bodies remain uninspected |
| Hermes prefetch/sync and tools | Direct `integrations/hermes-plugin-mem0/__init__.py`; backend methods located in `integrations/hermes-plugin-mem0/_backend.py` | [MEM-RTE-hermes-memory](#mem-rte-hermes-memory); backend construction, retry and full breaker policy remain uninspected |
| Strands, Vercel, n8n and Zapier | Strands client method search: `integrations/mem0-strands/python/src/mem0_strands/client.py`; remaining trees inventoried | Raw and inferred Strands calls located, but store/consumer delivery and other framework nodes uninspected; no admission/authority or end-to-end conclusion for these alternatives |
| Python/Node CLI and skills | Python dispatch and command methods searched: `cli/python/src/mem0_cli/app.py`, `cli/python/src/mem0_cli/commands/memory.py`; supplied Platform backend contract | CRUD, search, import, entity deletion and event polling are exposed, but all command bodies, Node parity and skill-driven adoption remain uninspected; not evidence of a standalone agent loop |
| Other examples, docs, tests and evaluators | Boundary supplies repository inventory and benchmark qualification | Most available tests/examples/docs uninspected, none run; unavailable `evaluation` submodule prevents evaluation-protocol inspection. No retention-quality or causal-benefit claim follows |

## Core ideas

1. **Derived facts and raw context are separate retained results.** Inferred Python addition both extracts text for the vector store and saves a bounded raw-message tail for future extraction. A no-facts or parse-empty result can still alter that tail. History is a third object: old/new text and events for inspection, not the next extraction's conversation input. See [MEM-OBJ-memory-data](#mem-obj-memory-data), [MEM-OBJ-messages](#mem-obj-messages), [MEM-OBJ-history](#mem-obj-history).
2. **Admission is route-specific.** The extraction model proposes, code filters and persists; raw writes bypass that proposal step; procedural writes summarize; OpenClaw skills delegate fact choice to the foreground agent. Caller identity does not establish human per-item approval. The coding-agent hooks introduce another trace-fed transformation through the opaque hosted extractor. See [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add), [MEM-RTE-coding-flush](#mem-rte-coding-flush).
3. **Retrieval metadata is not the fact's warrant.** Hashes, scopes, embeddings, lemmatized text and entity links control eligibility or ranking. They neither prove truth nor retain a necessary explanation of why the fact was extracted. The README consumer reduces results to text and grants it system-message placement. See [MEM-OBJ-memory-access](#mem-obj-memory-access), [MEM-OBJ-memory-vectors](#mem-obj-memory-vectors), [RT-BAP-answer-context](runtime.md#rt-bap-answer-context).
4. **Visibility, erasure and rejection differ.** Public search hides expired payloads by default; extraction's internal top-ten vector retrieval does not apply that visibility filter. Explicit deletion removes the vector object but keeps old text in history and does not delete the raw message tail. Failed TypeScript insertions can still produce ADD-shaped results. See [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), [MEM-RTE-typescript-memory](#mem-rte-typescript-memory).
5. **Hooks can supply context without owning the host window.** OpenClaw budgets recalled facts; coding-agent adapters redact, truncate and suppress already-shown IDs. These mechanisms control supplied context, not the enclosing host's entire accumulated conversation or compaction. See [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [MEM-RTE-coding-recall](#mem-rte-coding-recall), [MEM-RTE-pi-memory](#mem-rte-pi-memory).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-data
Label: Python memory payload text

Source-native identity: vector payload `data`, exposed as `memory`. Natural-language text stored as a field in the configured vector database, separately from its dense vector and symbolic access fields. Lineage may be current conversation extraction, direct non-system message content, explicit replacement or procedural summary. Unknown initial authorship remains local to those inputs. Later consumers include extraction, search/API callers and the shipped answer driver; language influences model interpretation, not a truth-enforced rule. The required record contains text, not an explanation of extraction or a quoted-source span. SRC-1, `mem0/memory/main.py`; [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) supplies extraction evidence. Distinct object, not a duplicate of that route or of the model components.

> new_metadata["data"] = data
> new_metadata["hash"] = hashlib.md5(data.encode()).hexdigest()
> --- `mem0/memory/main.py:1983-1984`

#### MEM-OBJ-memory-access
Label: Python memory access payload

Source-native identity: payload identity fields, `hash`, `text_lemmatized`, timestamps, `expiration_date` and attribution metadata. Symbolic fields in the vector-store payload; numerical embeddings are separately classified. Scope fields originate from caller inputs processed by the engine; hashes and lemmatization derive from text. Search and mutation code interpret them for filtering, scoring, deduplication and display. Caller-selected scopes are not authenticated ownership. `attributed_to` is optional extracted attribution, not verified source lineage. Direct metadata editing changes selection without necessarily changing text. SRC-1, `mem0/memory/main.py`; closest supplied records are [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) and [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), distinct routes spanning these fields rather than object counterparts.

> mem_metadata["data"] = text
> mem_metadata["text_lemmatized"] = text_lemmatized
> mem_metadata["hash"] = mem_hash
> --- `mem0/memory/main.py:1032-1034`

#### MEM-OBJ-memory-vectors
Label: Python retained memory embeddings

Source-native identity: inserted `vectors` and updated `vector` for memory IDs. Distributed-parametric dense representations stored in the configured vector database. Produced by the configured embedding model from proposed/raw/replacement text, with version and upstream training provenance unresolved beyond [RT-CMP-openai-embedding](runtime.md#rt-cmp-openai-embedding). These are outputs, not that component's weights. Search interprets numerical similarity to select textual candidates; the answer model receives text, not these vectors. Re-embedding changes index state, not evidence of weight training or improved capacity. Distinct retained object, no supplied object counterpart. SRC-1, `mem0/memory/main.py`.

> self.vector_store.insert(
>             vectors=[embeddings],
>             ids=[memory_id],
>             payloads=[new_metadata],
>         )
> --- `mem0/memory/main.py`

#### MEM-OBJ-messages
Label: SQLite recent messages

Source-native identity: SQLite `messages` table; natural-language `content` separated from symbolic `role`, `name`, session scope and timestamp columns by their consumers. Substrate is `SQLiteManager` at configured `history_db_path`, not necessarily the vector database. Saved raw input messages are not extracted facts. Engine code reloads the latest ten scoped rows chronologically into a later extraction prompt; software evicts older rows at save time. This is context-window selection by row count, not a token budget or a summary. No mandatory per-message human admission occurs at SQLite insertion. Source of messages can include generated assistant text. Distinct retained object used by [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), not a duplicate of the route. SRC-1, `mem0/memory/storage.py`, `mem0/memory/main.py`.

> DELETE FROM messages WHERE session_scope = ? AND id NOT IN (
>                         SELECT id FROM (
>                             SELECT id FROM messages WHERE session_scope = ? ORDER BY created_at DESC LIMIT 10
>                         )
>                     )
> --- `mem0/memory/storage.py`

#### MEM-OBJ-history
Label: SQLite mutation history

Source-native identity: SQLite `history`, queried by `memory_id`. Natural-language `old_memory`/`new_memory` values retain previous text; symbolic event, actor, role, timestamps and deletion marker identify mutations. Code writes records following vector mutations. `Memory.history` returns these rows to a requesting caller; no inspected automatic answer/extraction route reads them. History can outlive the deleted vector object and is not automatic rollback. It retains changed text, not required criticism or evidence for accepting it. Its physical store can survive engine reconstruction when configuration points at the same database; actual durability is unobserved. No object counterpart in the supplied report; it is used by [RT-RTE-direct-write](runtime.md#rt-rte-direct-write). SRC-1, `mem0/memory/storage.py`, `mem0/memory/main.py`.

> prev_value,
>             None,
>             "DELETE",
>             created_at=created_at,
>             updated_at=updated_at,
>             actor_id=existing_memory.payload.get("actor_id"),
>             role=existing_memory.payload.get("role"),
>             is_deleted=1,
> --- `mem0/memory/main.py:2128-2135`

#### MEM-OBJ-entity-links
Label: Entity access index

Source-native identity: entity-store payload `data`, `entity_type`, `linked_memory_ids` plus scope keys. Entity text is a readable label; link lists and types are symbolic access metadata. Entity embeddings are dense numerical representations in the separate lazily constructed entity collection of the configured vector provider. These parts are not additional factual memories offered directly to the README answer model. Source lineage is entity extraction from persisted memory text; exact normalization and semantic matches merge linked IDs. Search embeds up to eight query entities, looks up matches, and turns links into per-memory boosts. Link cleanup on explicit text update/delete is best effort. This is not evidence of a proposition graph, truth maintenance or independently evaluated entities. Distinct object, no supplied object counterpart; it contributes to [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories). SRC-1, `mem0/memory/main.py`.

> entity_payload = {
>                     "data": entity_text,
>                     "entity_type": entity_type,
>                     "linked_memory_ids": [memory_id],
>                     **{k: v for k, v in search_filters.items()},
>                 }
> --- `mem0/memory/main.py:638-643`

#### MEM-OBJ-procedural-memory
Label: Procedural summary text

Part of: [RT-RTE-direct-write](runtime.md#rt-rte-direct-write)

This object is the retained output of the procedural branch within the supplied multi-branch route, not a duplicate route. Source-native identity: `procedural_memory`, stored as memory text with `memory_type=procedural`. Natural-language model summary in the vector store with an embedding. Input is supplied messages plus caller prompt or shipped procedural instruction; the model proposes the summary, code rejects empty output then stores it. Required persisted state is summary and metadata, not the original derivation. Subsequent search can return it as memory; no specialized executable-procedure interpreter is established. Procedural naming alone does not establish an operational rule's adoption. SRC-1, `mem0/memory/main.py`.

> metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
> --- `mem0/memory/main.py`

#### MEM-OBJ-evidence-store
Label: Coding-agent local evidence and delivery state

Source-native identity: Claude Code `EvidenceStore`, default `evidence.sqlite3`. Raw/selected conversation and tool evidence are serialized into SQLite `events.payload_json`; natural-language content is not itself the derived hosted memory. Symbolic session scopes, flush statuses, event ranges and retrieval records control checkpoint delivery, recovery and already-shown filtering. `retrievals.memory_text` is a local copy of recalled text with ID/rank/score, not newly established knowledge. Local storage is software-controlled from host events; a workflow trigger is not human approval of each event. Later consumers are checkpoint assembly and recall/sidekick bookkeeping. Remote memory remains an opaque alternative, separated in [MEM-RTE-coding-flush](#mem-rte-coding-flush). No supplied counterpart; not the engine SQLite history. SRC-1, `integrations/claude-code-plugin/core/memory_core.py`.

> self.path = path or directory / "evidence.sqlite3"
> --- `integrations/claude-code-plugin/core/memory_core.py`

> CREATE TABLE IF NOT EXISTS retrievals (
>                 session_id TEXT NOT NULL,
>                 repo_id TEXT NOT NULL,
>                 memory_id TEXT NOT NULL,
>                 injected_at TEXT NOT NULL,
>                 rank INTEGER,
>                 score REAL,
>                 memory_text TEXT,
>                 context_chars INTEGER NOT NULL DEFAULT 0,
>                 PRIMARY KEY(session_id, repo_id, memory_id)
>             );
> --- `integrations/claude-code-plugin/core/memory_core.py`

### Routes

#### MEM-RTE-typescript-memory
Label: TypeScript OSS memory persistence and recall

Separate TypeScript engine invocation, not another declaration of Python [RT-RTE-extract-add](runtime.md#rt-rte-extract-add). The supplied runtime traces extraction; direct inspection extends it through batch insertion, history, entity attempts, message save and return. Caller initiates the open request; model proposes inferred text, code hashes/embeds and attempts storage. No mandatory human approval or independent answer oracle is shown. Raw mode is a separate admitted branch, not subject to inferred-text selection. Provider-specific rollback and alternative history stores remain uninspected. SRC-1, `mem0-ts/src/oss/src/memory/index.ts`.

Insertion fallback logs individual errors but does not remove failed records from the list subsequently used for history and returned ADD objects. This differs from Python's `persisted_records` filter; ADD-shaped output is not confirmation of persistence here. Search still has concrete selection implementation: scoped semantic pool, optional keyword scores and entity boosts, expiry filtering, ranking, formatting and optional reranking. No answer-producing caller specific to this OSS route was traced.

> } catch (e) {
>           console.error(`Failed to insert memory ${allIds[i]}: ${e}`);
>         }
> --- `mem0-ts/src/oss/src/memory/index.ts`

> return records.map((r) => ({
>       id: r.memoryId,
>       memory: r.text,
>       metadata: { event: "ADD" },
>     }));
> --- `mem0-ts/src/oss/src/memory/index.ts`

- Immediate return: Proposed records mapped to IDs/text/ADD metadata, including potentially failed inserts; errors can also arise outside the swallowed per-item insertion failures.
- Later read-back: Successfully inserted text can be selected by later search/get; prior-message read/write depends on history-store capabilities. Search alone is a storage capability, not an established downstream answer route.
- Delegated visibility: Providers receive text, vectors and payloads; API caller receives formatted text, metadata and scores. No direct exposure of stored dense vectors to an answer model was established.
- Selection predicate: Retrieved hashes and within-batch hashes suppress exact duplicates; search over-fetches max(topK*4,60) semantic candidates and scores them using optional lexical/entity contributions.
- Invalidation or expiry: Search removes expired candidates unless showExpired; ID get body does not apply that check. Full mutation/reset/store-specific parity is uninspected.
- Activation or effect: Code attempts retention and exposes selected text to callers; neither successful retention nor changed answers is observed.
- Evidence limits: Separate implementation; no Python guarantee inherited. History/ADD bookkeeping can overstate persisted results. Hosted TypeScript client is not this engine.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-coding-flush
Label: Coding-agent trace checkpoint to hosted memory

Claude Code host events → local EvidenceStore → selected checkpoint/episode → redacted user/assistant messages plus bounded repository evidence → batched hosted inferred-add requests → event polling and stored flush status. Code owns collection, selection and submission; remote software/model admission is opaque. Automatic triggers include registered PreCompact and SessionEnd, with periodic/idle scheduling present in hook runner. This route has no supplied counterpart: [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client) is a different SDK wrapper, not this shipped trace producer. SRC-1, `integrations/claude-code-plugin/hooks/hooks.json`, `integrations/claude-code-plugin/core/hook_runner.py`, `integrations/claude-code-plugin/core/memory_core.py`.

Admission distinguishes user problems, assistant conclusions and supporting subagent/tool evidence. Shipped project instructions ask to prefer completed behavior and accepted decisions, not proposals; personal instructions ask for user facts. These instructions are requests to the service, not verified policy. The source is mixed user/assistant/tool trace, not necessarily a human-authored fact. No mandatory human per-memory review or reference-answer oracle is shown. Operating mode is ongoing coding-session capture, not an evaluated curriculum. Changed-path evidence is capped; passing test/build details generally stay local, whereas failed command details can be included. Derived hosted facts need not preserve all evidence or reasons. Local events and flush state are not interchangeable with the derived result.

> "agent_custom_instructions": PROJECT_MEMORY_INSTRUCTIONS,
>         "custom_instructions": PERSONAL_MEMORY_INSTRUCTIONS,
>         "custom_categories": CODING_MEMORY_CATEGORIES,
>         "infer": True,
> --- `integrations/claude-code-plugin/core/memory_core.py`

> Use the coding agent's final response for conclusions about current repository behavior. Do not save proposed or recommended changes unless the user accepted them or the coding agent completed them. Treat subagent responses as supporting repository evidence, not as decisions.
> --- `integrations/claude-code-plugin/core/memory_core.py`

> messages = [
>         {"role": message["role"], "content": redact(message["content"]).strip()}
>         for message in structured.get("extraction_messages", [])
>         if message.get("role") in {"user", "assistant"} and message.get("content")
>     ]
> --- `integrations/claude-code-plugin/core/memory_core.py`

- Immediate return: Local flush status, packet/event identifiers and counts, or queued handoff at the hook boundary; no-key and no-session cases return without remote admission.
- Later read-back: Remote derived facts are requested by later first-prompt/MCP recall in [MEM-RTE-coding-recall](#mem-rte-coding-recall); local events and stored event IDs feed assembly/retry, not an automatic raw-trace dump into the next answer.
- Delegated visibility: Hosted service receives redacted message batches and scope/branch/source metadata; raw tool detail is selected before submission. Host compaction internals remain outside the adapter.
- Selection predicate: Completed-exchange/message/character checkpoint thresholds or force reason; extraction batching defaults to estimated 24000 input tokens, keeping exchanges/assignment-response pairs together when possible and splitting oversized content.
- Invalidation or expiry: Pending event IDs/status support polling and retry; failed/missing events can be cleared for resubmission. Separate explicit remote forgetting can return partial deletion. No cross-service atomic rollback or full local/remote erasure guarantee established.
- Activation or effect: Code wires trace transformation and subsequent recall; hosted extraction compliance and later behavioral activation remain unobserved.
- Evidence limits: Remote derived representation/admission is unavailable. Exact detached-worker recovery, all checkpoint provenance and non-Claude adapters remain partially uninspected; local successful bookkeeping is not end-to-end benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-coding-recall
Label: Coding-agent first-prompt and requested recall

Claude Code first-prompt hook automatically requests remote retained facts; MCP `search_memories` affords explicit foreground/sidekick retrieval. Code selects identity/repository/directory-related scope, optional category/run and bounded result count, rejects task_episode objects, suppresses IDs already shown in a tracked session, formats text and returns context. Host owns subsequent model invocation. Distinct from [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks) and [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories): different shipped consumers and selection/state. SRC-1, `integrations/claude-code-plugin/core/memory_core.py`, `integrations/claude-code-plugin/core/hook_runner.py`, `integrations/claude-code-plugin/core/mcp_server.py`.

> memories = [
>             memory
>             for memory in memories
>             if isinstance(memory, dict)
>             and (memory.get("metadata") or {}).get("record_kind") != "task_episode"
>         ][:result_limit]
> --- `integrations/claude-code-plugin/core/memory_core.py`

> "hookEventName": "UserPromptSubmit",
>             "additionalContext": context,
> --- `integrations/claude-code-plugin/core/hook_runner.py`

A sidekick's separate conversation/worktree is declared in the shipped agent definition. Start code reuses the parent session's injected-memory text, and stop records final message and transcript path. These crossings establish selected context and a returned/retained summary surface, not host-wide isolation or an opaque transcript's complete reconstruction. SRC-1, `integrations/claude-code-plugin/agents/sidekick.md`, `integrations/claude-code-plugin/core/memory_core.py`.

> context = combine_context(
>         format_context(store.injected_memories(session_id, repo.identity))
>     )
> --- `integrations/claude-code-plugin/core/memory_core.py`

- Immediate return: Hook additionalContext or a text-only MCP result; failure/no-match replies are distinct in the formatter.
- Later read-back: Derived facts from earlier checkpoints reach future coding invocations. Local retrieval snapshots can be supplied to the sidekick at its first start.
- Delegated visibility: Host receives formatted/redacted fact text with optional branch labels, not the full local evidence database or remote derivation. Sidekick receives selected parent recall rather than the parent's whole conversation.
- Selection predicate: First sufficiently long prompt (default minimum 20 characters), bounded query of 6000 characters, top five and two-second timeout; explicit search defaults top three and caps at twenty, with optional category/run/scope and session deduplication.
- Invalidation or expiry: Format limit defaults 4000 characters, clamped 1000–10000; first oversized entry can be truncated and later entries omitted. Remote delete affects future retrieval, not already copied context. Local unseen filtering can suppress later re-delivery; host compaction does not prove those facts remain visible.
- Activation or effect: Source returns additional context/tool text; interpretation by the coding model and effects on decisions are unobserved.
- Evidence limits: Remote latest_only is requested, not implemented here. IDs can be marked injected before formatting omits text, so bookkeeping does not certify full text reached the model. Host's native compaction and subagent execution are external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-hermes-memory
Label: Hermes prefetch, trace sync and foreground tools

Hermes memory-provider entry points implement current-query prefetch, nonblocking turn sync, and explicit search/add/update/delete tools. Code supplies user-scoped filters, formats prefetch results as `## Mem0 Memory`, and exposes tool IDs/text/scores. Trace sync sends truncated user and assistant text for inference; foreground add passes infer=False. Foreground agent/caller chooses direct fact text and mutation; code checks required arguments and checks ownership before update/delete, rejecting a present mismatched owner. No mandatory human per-item review, semantic truth oracle or autonomous improvement experiment is established. This route is distinct from supplied OpenClaw and SDK routes; backend alternatives delegate to platform, server or local engine. SRC-1, `integrations/hermes-plugin-mem0/__init__.py`, `integrations/hermes-plugin-mem0/_backend.py`.

> messages = [
>                     {"role": "user", "content": _truncate_for_sync(user_content, self._sync_max_chars)},
>                     {"role": "assistant", "content": _truncate_for_sync(assistant_content, self._sync_max_chars)},
>                 ]
>                 self._try(lambda: self._add(messages, infer=True), logger.warning, "Mem0 sync failed: %s")
> --- `integrations/hermes-plugin-mem0/__init__.py`

> result = self._add([{"role": "user", "content": args["content"]}], infer=False)
> --- `integrations/hermes-plugin-mem0/__init__.py`

- Immediate return: Prefetch text if ready after a short wait, otherwise empty; sync schedules work or skips; tools return JSON results/errors, including queued-versus-stored wording.
- Later read-back: Accepted sync-derived or direct facts can reach future prefetch/search. This is a documented provider role with concrete methods, not proof the external host invoked them.
- Delegated visibility: Backend sees bounded paired turn messages or direct facts; model-facing prefetch drops result IDs and scores, while explicit search preserves them.
- Selection predicate: Current query plus user scope; completed prefetch is accepted only for the same query. Tool top_k is clamped 1–50; rerank is platform-specific. Prior sync still busy after a five-second wait causes the next sync to skip.
- Invalidation or expiry: Foreground ID mutation invokes backend update/delete after ownership check; old prefetch/window copies are not shown to be revoked. No durable queue or automatic rollback established by the inspected sync method.
- Activation or effect: Source wires capture/prefetch/tool responses; external Hermes scheduling and actual answer effects are unobserved.
- Evidence limits: Missing-owner records pass the inspected mismatch test. Backend admission and failure semantics depend on selected mode; full configuration/breaker/retry behavior remains uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-pi-memory
Label: Pi automatic recall and conversation capture

The shipped adapter constructs a hosted TypeScript MemoryClient, registers before-agent-start recall and agent-end capture, and resets lifecycle seen IDs at session start. Capture keeps user/assistant textual blocks, removes other roles/nontext blocks, redacts matched secrets and submits project-scoped messages. Remote admission is opaque; software supplies no mandatory human content gate. Static MEMORY_POLICY and custom categories guide the route, not a local truth oracle or candidate evaluation. This is not the OSS TypeScript engine in [MEM-RTE-typescript-memory](#mem-rte-typescript-memory), nor the generic Python HTTP wrapper [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client). SRC-1, `integrations/pi-agent-plugin/src/entry.ts`, `integrations/pi-agent-plugin/src/capture/index.ts`, `integrations/agent-plugin-core/typescript/src/lifecycle.ts`.

> return {
>       systemPrompt: (event.systemPrompt ?? "") + "\n\n" + extra,
>     };
> --- `integrations/pi-agent-plugin/src/entry.ts`

> await mem0.add(conversation, {
>         ...addParams,
>         customCategories: DEFAULT_CUSTOM_CATEGORIES,
>       });
> --- `integrations/pi-agent-plugin/src/capture/index.ts`

- Immediate return: Extended system prompt containing policy and optional recall; capture awaits add or logs failure. Missing API key disables registration.
- Later read-back: Hosted conversation-derived facts can enter later prompt-time searches; session-local seen IDs suppress duplicate recall and clear at session start, not durable knowledge admission.
- Delegated visibility: Service receives textual user/assistant conversation after role/block filtering and regex redaction. Host receives formatted memory strings rather than raw retained conversation or service rationale.
- Selection predicate: Enabled contextInjection and nonempty redacted query bounded to 6000 characters; project-scope search; two-second default race; unseen IDs; formatted recall default 4000-character budget including wrapper with first-entry truncation.
- Invalidation or expiry: Search failure/timeout yields empty recall; losing the race does not demonstrate cancellation. AutoCapture setting gates writes. No direct host compaction handler or erasure of already supplied system context established in the inspected entry point.
- Activation or effect: Adapter appends memory to system input and submits captured conversation; hosted persistence, host compliance and behavioral change remain unobserved.
- Evidence limits: Source comment calls retrieval guaranteed, but disabled injection, empty query, timeout, error and no-result cases yield no memory. Explicit tools/commands/scope resolver and host internals are not fully inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-extract-add](runtime.md#rt-rte-extract-add)

Memory-specific storage and lineage: [MEM-OBJ-messages](#mem-obj-messages) supplies raw recent context; [MEM-OBJ-memory-data](#mem-obj-memory-data) stores derived text; [MEM-OBJ-memory-access](#mem-obj-memory-access), [MEM-OBJ-memory-vectors](#mem-obj-memory-vectors) and [MEM-OBJ-entity-links](#mem-obj-entity-links) supply distinct access state. Caller messages can mix human and model-originated text. Model proposes facts, software parsing/nonempty/hash/embedding/persistence gates admit them; triggering add is not human approval of each fact. Empty extraction still saves input. The required derived payload contains no separate reasoning field or source-span link. SRC-1, `mem0/memory/main.py`, `mem0/memory/storage.py`.

> if not extracted_memories:
>             # Save messages even if nothing extracted
>             self.db.save_messages(messages, session_scope)
>             return []
> --- `mem0/memory/main.py`

Read-back is pull at the extraction call: current parsed messages select ten vector matches and the scope selects ten prior raw messages. The supplied additive prompt instructs using prior text for context/deduplication, not fresh extraction; see [RT-BAP-extraction-context](runtime.md#rt-bap-extraction-context). No token budget is established here. This gathering uses the vector adapter directly, without the public search's expiry filtering, hybrid ranking or optional reranker. Expired stored text may therefore still shape later extraction. Numerical ID remapping is not verified citation lineage. Batch hash checks cover the retrieved set and batch, not all retained text. Insertion confirmation depends on adapter success; history/entity failures can leave divergence. SRC-1, `mem0/memory/main.py`.

> existing_results = self.vector_store.search(
>             query=parsed_messages,
>             vectors=query_embedding,
>             top_k=10,
>             filters=search_filters,
>         )
> --- `mem0/memory/main.py`

#### On [RT-RTE-direct-write](runtime.md#rt-rte-direct-write)

Memory-specific curation and withdrawal: raw addition stores non-system message content without extraction and returns before inferred-path message-tail save/entity linking. Procedural addition instead stores model summary; [MEM-OBJ-procedural-memory](#mem-obj-procedural-memory) names its retained part. Explicit update replaces text/re-embeds or merges metadata, preserves original created_at, refreshes updated_at/hash/lemmatization, writes history and relinks entities when text changed. Caller-selected edits are admissions without mandatory human approval; supplied caller identity leaves human control unresolved. The implementation provides neither an answer oracle nor required change justification. SRC-1, `mem0/memory/main.py`.

> text_changed = data != prev_value
> --- `mem0/memory/main.py:2070-2070`

> if text_changed:
>             self._remove_memory_from_entity_store(memory_id, session_filters)
>             self._link_entities_for_memory(memory_id, data, session_filters)
> --- `mem0/memory/main.py`

Delete removes the vector row, writes old text/deletion history, then attempts entity cleanup. Delete-all repeatedly lists scoped batches and stops on repetition; its generic success message need not certify an empty store if the adapter repeats a batch. Neither inspected single delete nor delete-all deletes recent message rows. Reset drops SQLite history/messages and recreates stores, with nonfatal entity-reset failure. Those operations withdraw future vector availability, not copies already delivered to models, complete trace erasure or atomic cross-store rollback. Scope/access trust and TTL visibility remain as runtime qualifies them. SRC-1, `mem0/memory/main.py`, `mem0/memory/storage.py`.

> if batch_ids in seen_batches:
>                 logger.warning("Stopping delete_all after a repeated memory batch")
>                 break
> --- `mem0/memory/main.py:1943-1945`

#### On [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories)

Memory-specific selection: direct inspection of the underlying Python search body shows max(limit*4,60) semantic over-fetch; keyword scores and entity boosts rescore that pool rather than add lexical-only memories. Public default expiry filtering precedes scoring. Query/entity embeddings are current computation; stored text/vectors/links are the retained inputs. Result formatting preserves selected metadata, but this README consumer drops all but text before system-message delivery. Retrieval scores are not confidence in fact truth; provider ranking quality is untested. Storage capability alone does not add other unspecified consumers. SRC-1, `mem0/memory/main.py`; the supplied record supplies the README passage.

> # Step 7: Build candidate set from semantic results
>         candidates = []
>         for mem in semantic_results:
>             payload = mem.payload if hasattr(mem, 'payload') else {}
>             if not show_expired and _payload_is_expired(payload):
>                 continue
> --- `mem0/memory/main.py:1680-1685`

#### On [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks)

Memory-specific automatic selector: skills recall sanitizes query metadata, searches user long-term candidates at maxMemories*2 and optional session candidates at five, deduplicates IDs, then sorts category before importance before relevance. Defaults are fifteen memories, threshold 0.4 and estimated 1500 tokens. Identity/configuration items bypass the budget if identityAlwaysInclude, while still counting against maximum count. Text estimates use four characters/token and formatting overhead is outside the selection estimate. Thus a count limit and approximate token target are distinct. Text, category and importance reach recall context, not stored embeddings or full derivation. SRC-1, `integrations/openclaw/recall.ts`.

> if (identityAlwaysInclude && isIdentity) {
>       selected.push(memory);
>       usedTokens += memTokens;
>       continue;
>     }
> --- `integrations/openclaw/recall.ts`

Static triage guidance asks for future utility, novelty, factuality and safety checks, updating changed facts and preserving reasons for standing rules. It labels project facts as expiring after ninety days and memory_update as atomic. These are instruction-layer assertions, not proof of configured TTL or cross-store atomicity; Python mutation is not atomic across vector/history/entity stores. The protocol's request to retain reasons can put reasons inside fact text, but cannot guarantee preservation or that a later budgeted recall includes them. Skills versus legacy capture and model-versus-software admission remain separate as runtime describes. SRC-1, `integrations/openclaw/skills/memory-triage/SKILL.md`.

> Known but materially changed → UPDATE (find old → update in place)
> --- `integrations/openclaw/skills/memory-triage/SKILL.md`

## Write side

**Acquisition and transformation.** The ordinary Python chain is supplied conversation → raw tail reload plus similar retained facts → model extraction → parsed text → embeddings/hash/lemmatization → confirmed-by-adapter insertions → history/entity attempts → raw message save. [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) and its annotation distinguish raw versus derived persistence and structural rejection from truth checks. Supplied input can contain facts, generated assertions, mistakes or instructions; provenance is not verified by assigning an actor or role. The configured model component remains separate from retained index changes.

**Alternate admissions.** Raw insertion, explicit text/metadata update and procedural summarization are not variations of one extraction gate; see [RT-RTE-direct-write](runtime.md#rt-rte-direct-write). OpenClaw skills give the foreground agent fact selection and request direct storage; see [RT-RTE-openclaw-add](runtime.md#rt-rte-openclaw-add). Hermes has both raw foreground tools and inferred trace sync; Pi submits filtered conversation to a hosted extractor. These are software/model admissions; no generic caller implies human review. Server custom instructions can change how later extraction proposes facts, but the generate-instructions endpoint returns a proposal, not adoption; [RT-OBJ-custom-instructions](runtime.md#rt-obj-custom-instructions), [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config).

**Trace-fed retained results.** Python's message tail is raw storage with bounded eviction; its derived facts can shape subsequent extraction and answers. Procedural memory is a different model-produced summary. Claude Code checkpoints retain local structured evidence but submit selected messages and repository details for hosted derivation. That route separates local event/flush metadata, selected checkpoint batches, remote derived memory and later recall; it does not equate a successful API event with sound learned knowledge. Requested preservation of constraints/reasons remains language-level guidance. See [MEM-RTE-coding-flush](#mem-rte-coding-flush), [MEM-RTE-coding-recall](#mem-rte-coding-recall). Host compaction's own verbatim-tail/summary/checkpoint forms remain outside the inspected plugin; a PreCompact flush is not evidence of controlling native compaction or automatically restoring all removed content.

**Maintenance, evaluation, rejection and withdrawal.** Python mutations preserve old/new text in history and try to maintain indexes, but history is an inspection capability rather than an automatic critic or rollback. Empty/malformed extraction, failed embedding and duplicate hashes can reject proposals; these checks do not evaluate truth. In TypeScript, an insertion-rejected proposal may still enter history and ADD results, preventing reliable output-based accounting. Expiry hides default search results but not all read-back; deletion leaves history and recent traces. Already delivered context is not revoked. Evaluation-submodule content is unavailable, and available tests have not been executed or systematically inspected, so no empirical retention/cleanup correctness follows. Relevant records: [MEM-OBJ-history](#mem-obj-history), [MEM-RTE-typescript-memory](#mem-rte-typescript-memory), [RT-RTE-direct-write](runtime.md#rt-rte-direct-write), [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client).

## Read-back

- **Extraction-time request:** [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) selects the latest ten raw messages by scope and ten vector matches by current message semantics. Delivered text influences the extraction model through natural-language context. No public-search expiry guarantee or answer-quality oracle transfers to this path.
- **Answer-time request:** [RT-RTE-chat-memories](runtime.md#rt-rte-chat-memories) makes a concrete search-to-system-message delivery. Its top-three text selection omits IDs, source lineage and reasons unless contained in the retained text. The supplied [RT-BAP-answer-context](runtime.md#rt-bap-answer-context) is the authority path; no duplicate is declared here. Direct get/list/history APIs only afford caller retrieval, not an inferred automatic downstream model consumer.
- **Prompt-build supply:** [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [MEM-RTE-coding-recall](#mem-rte-coding-recall), [MEM-RTE-hermes-memory](#mem-rte-hermes-memory) and [MEM-RTE-pi-memory](#mem-rte-pi-memory) implement automatic recall initiated by host events/current prompt. They still issue backend pull requests; the automatic supply is from hook/provider to host. This differs from foreground explicit tool search. Budgets, scopes, redaction, truncation and seen-ID suppression determine what reaches the consumer.
- **Separate-context work:** Claude Code's shipped sidekick keeps its own conversation/worktree and receives selected parent recall; final message/transcript reference is recorded on stop. The host owns frame creation, tool execution and return. Selected input and final output resemble a separate work frame, but memory text is copied into contexts, not a live dereferenceable pointer. Neither vector deletion nor marking an ID seen establishes that a copied fact is absent from or still present in a model window. OpenClaw subagent restrictions are plugin-local as runtime states.
- **Opaque or broken alternatives:** [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client) is a service affordance, not evidence of proprietary internals. [RT-RTE-proxy-chat](runtime.md#rt-rte-proxy-chat) remains source-incompatible on the inspected recall branch. Uninspected framework/CLI/dashboard alternatives stay in the inventory; their existence does not establish delivered context, atomic updates or automatic read-back.

## Integration issues

1. **Expiry must stay consumer-specific.** [RT-RTE-extract-add](runtime.md#rt-rte-extract-add) directly calls vector_store.search without the public search's expiry filter (SRC-1, `mem0/memory/main.py`, passage in its annotation). The runtime already limits its guarantee to public visibility, so this is a necessary extension, not a contradiction. Reconciliation must not turn expiry into withdrawal from every later model context.
2. **Python ADD accounting cannot describe TypeScript.** [MEM-RTE-typescript-memory](#mem-rte-typescript-memory) shows insertion failures logged while all records feed history/return (SRC-1, `mem0-ts/src/oss/src/memory/index.ts`). The runtime explicitly left TypeScript post-extraction behavior unresolved. Integrate this positive divergence rather than copying Python's confirmed-record guarantee.
3. **Delete is not complete forgetting.** [MEM-OBJ-history](#mem-obj-history), [MEM-OBJ-messages](#mem-obj-messages) and the annotation on [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) show old text and recent traces surviving vector deletion (SRC-1, `mem0/memory/main.py`, `mem0/memory/storage.py`). No automatic history-to-answer reader is established, but this prevents an erasure claim and leaves copied-context withdrawal unresolved.
4. **Instruction labels overstate guarantees.** OpenClaw triage calls update atomic and declares category retention periods; direct source does not establish cross-store atomicity or inspect the complete TTL translation route. Pi's guaranteed-retrieval comment has explicit timeout/error/disabled alternatives. See [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [MEM-RTE-pi-memory](#mem-rte-pi-memory), SRC-1 at their cited instruction/implementation anchors. Keep the policy request separate from enforcement.
5. **Additional shipped coding-agent routes are material.** [MEM-RTE-coding-flush](#mem-rte-coding-flush), [MEM-RTE-coding-recall](#mem-rte-coding-recall), [MEM-RTE-hermes-memory](#mem-rte-hermes-memory), [MEM-RTE-pi-memory](#mem-rte-pi-memory) extend the runtime inventory, not replace SDK/OpenClaw routes. Their service consumer role and selected trace transformations are source-grounded; uninspected adapters and native host compaction prevent a universal integration model.
6. **No new declaration is intended to duplicate a supplied referent.** The closest supplied records are identified in each declaration. [MEM-OBJ-procedural-memory](#mem-obj-procedural-memory) is explicitly a retained part of the supplied multi-branch route; all other Python objects are storage/form parts used by several supplied routes, not alternative declarations of those routes or the model components. Existing runtime referents receive annotations. New TypeScript and host routes have different entry points/owners.
7. **Coverage questions remain, with bounded consequences.** TypeScript alternative history-store retention, async mutation parity, other coding-agent adapters/build equality, explicit Pi tools, complete OpenClaw provider TTL behavior, dashboard operations, non-default providers/rerankers, CLI import/entity deletion/adoption, framework callers and evaluator source remain partly or wholly uninspected. The coverage table names paths and prevented conclusions. The hosted backend and evaluation submodule are unavailable, not merely unread. These limits prevent whole-system parity, complete consumer enumeration and reliability/effect claims; they do not erase inspected positive routes.

## Limitations and checks

All source-dependent findings use SRC-1 at `0724291bd864cf807e88ee8981c8226644e8fb42`. HEAD matched the supplied boundary and Git status was clean before source inspection. The supplied member types, collection contract, worker rules and full record contract were read; supplied runtime was read in bounded ranges with continuation checked. No additional source, mutable website, prohibited prior characterization or execution evidence was used. The report's available-but-uninspected parts are explicit, not absences. Method identity is the supplied invocation/contracts; no method-commit value was supplied or inferred from engine state.

The strongest warranted conclusion is implemented retention, selection and delivery, with concrete counterpaths and unresolved alternatives. There is no observed activation, causal performance result, successful learned capacity or guaranteed model compliance. Native host compaction, service internals and external database/model durability remain outside the evidence. Deterministic validation: the required `commonplace-run validate-output` invocation passed with “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Initial quotation ambiguities were repaired with validator-supplied ranges, without narrowing findings. The check tests form and quotation occurrence, not semantic acceptance.
