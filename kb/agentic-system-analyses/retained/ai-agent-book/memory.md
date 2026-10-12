---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AI Agents in Depth memory mechanisms: user-memory tools, disk reload, offline consolidation and sequential campaign checkpoints, with other suite variants unresolved."
run-id: AAS-2026-10-12-ai-agent-book-d56e8121d636-01
source-identity: "https://github.com/bojieli/ai-agent-book"
reviewed-boundary: "dbc046eb896ac4e39aa19c7774c8bf49583b89a6"
---

# AI Agents in Depth memory report

## Boundary and evidence

This report traces the user-memory loop initially witnessed in [boundary](boundary.md#boundary-and-evidence), and annotates the selected context and retry-policy routes in the supplied runtime. It does not treat the teaching suite as one shared memory runtime. SRC-1 at the frozen commit supplies implementation and doctrine/design, not observed execution or causal experiments. No target code, tests, examples, providers or services were run. HEAD was rechecked as `dbc046eb896ac4e39aa19c7774c8bf49583b89a6`.

Direct reads cover `chapter3/user-memory/memory_manager.py` through the clearing helper; `agent.py` from configuration through reset; complete functional bodies of `conversational_agent.py`, `conversation_history.py` and `background_memory_processor.py`; `memory_cli.py` manager construction, add/query/update/consolidate/show, extraction and dispatch; `main.py` interactive loop, evaluation preparation/answer/cleanup and CLI dispatch; `config.py` provider, memory and storage configuration; and `run_evaluation.py` prompts and per-case checkpoint/update/answer/judge route. Unread portions of drivers, benchmarks and retained results remain inspection limits. Existing runtime findings are supplied evidence, not new direct reads of their source.

| Entry point or operation | Source path / evidence basis | Coverage and prevented conclusion |
| --- | --- | --- |
| Interactive conversation, automatic/manual processing, reset | SRC-1: `chapter3/user-memory/main.py`, `chapter3/user-memory/background_memory_processor.py` | Direct: [MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance), [MEM-RTE-conversation-reload](#mem-rte-conversation-reload). Mode dispatch inspected; full demo body not inspected. |
| Notes and enhanced notes | SRC-1: `chapter3/user-memory/memory_manager.py`, `chapter3/user-memory/agent.py` | Direct: [MEM-OBJ-memory-note](#mem-obj-memory-note); same storage, different requested extraction. |
| Basic JSON and advanced JSON | SRC-1: `chapter3/user-memory/memory_manager.py`, `chapter3/user-memory/agent.py` | Direct: [MEM-OBJ-memory-cards](#mem-obj-memory-cards), [MEM-OBJ-categories](#mem-obj-categories); separate replacement and display semantics. |
| Model mutation tools and direct update helper | SRC-1: `chapter3/user-memory/agent.py`, `chapter3/user-memory/background_memory_processor.py` | Direct: [MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance); helper admission differs from model proposal. Search flag does not register a search tool. |
| Offline CLI write/query/consolidate and online extract | SRC-1: `chapter3/user-memory/memory_cli.py` | Direct: [MEM-RTE-offline-maintenance](#mem-rte-offline-maintenance); extract line-pair adapter and stale display noted below. Demo implementation not inspected. |
| History persistence and optional external search | SRC-1: `chapter3/user-memory/conversation_history.py` | Direct: [MEM-OBJ-conversation-turn](#mem-obj-conversation-turn), [MEM-RTE-history-search](#mem-rte-history-search). Dify payloads inspected; service storage/embedding provenance, actual search behavior and deployed isolation unavailable. |
| Interactive evaluation preparation and memory-only answer | SRC-1: `chapter3/user-memory/main.py` | Direct: preparation, batch mutation and reload; evaluator internals in `chapter3/user-memory-evaluation/` uninspected. No reward validity or benefit conclusion. |
| Sequential memory replacement, checkpoint resume, independent judge | SRC-1: `chapter3/user-memory/run_evaluation.py` | Direct: [MEM-OBJ-memory-states](#mem-obj-memory-states), [MEM-RTE-sequential-campaign](#mem-rte-sequential-campaign). Retained campaign results and recorder implementation uninspected; no observed outcome. |
| Context history, filtering, result serialization | SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py` | Supplied: [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history), [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation); annotations below. Grounding assessor uninspected. |
| Candidate source, rejected-control feedback and manifests | SRC-1: `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/evolution.py` | Supplied: [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate), [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy). Production adoption not established. |
| Other user-memory backends and retrieval variants | SRC-1: `chapter3/mem0/agent.py`, `chapter3/memobase/agent.py`, `chapter3/agentic-rag-for-user-memory/agent.py`, `chapter3/contextual-retrieval-for-user-memory/advanced_memory_manager.py` | Inventoried, uninspected: payload encoding, initial lineage, software/human admission, transformations, actual selectors, read-back consumers and withdrawal propagation unresolved for each. Prevents classifying these alternatives from their labels. |
| Retrieval/indexing/extraction and sanitization experiments | SRC-1: `chapter3/retrieval-pipeline/retrieval_pipeline.py`, `chapter3/dense-embedding/document_store.py`, `chapter3/sparse-embedding/bm25_engine.py`, `chapter3/structured-index/hybrid_retriever.py`, `chapter3/structured-knowledge-extraction/advisor_agent.py`, `chapter3/log-sanitization/agent.py`, `chapter3/agentic-rag/agent.py`, `chapter3/contextual-retrieval/contextual_agent.py` | Inventoried, uninspected: storage, dense/sparse lineage, derived-result consumers, admission/rejection and cleanup coverage remain local unknowns. No suite-wide memory or source-trust conclusion. |
| Other chapter loops, skills, fixtures and results | [boundary](boundary.md#boundary-and-evidence) | Included in frozen target but outside this report's traced subset, not declared absent. Compaction, checkpoints, instruction adoption, trace learning, training and evaluator feedback in those paths remain uninspected. Prevents exhaustive suite claims. |

## Core ideas

The traced memory route separates raw dialogue from model-authored retained facts. A conversation agent persists user/assistant turns; a background agent interprets recent turns and directly invokes mutation tools; subsequent conversation calls reload the resulting user file. The update consumer therefore receives mixed human/model traces, while the later answer consumer receives derived notes/cards. Both facts and assistant mistakes can enter the extraction input; the request to extract factual information is not a source-verification gate. See [MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance) and [MEM-BAP-memory-context](#mem-bap-memory-context).

Storage shape does not determine behavioral form. Notes are prose. JSON keys and metadata have symbolic addressing rules, but factual values and backstories influence answers through model interpretation. Advanced display removes internal metadata while preserving a supplied backstory; basic JSON displays source metadata too. No note-level token targeting is implemented in the inspected context builders. The configured `max_memory_context` fields do not constrain those builders. SRC-1: `chapter3/user-memory/conversational_agent.py`, `chapter3/user-memory/agent.py`, `chapter3/user-memory/memory_manager.py`.

The separate sequential campaign is a counterexample to equating memory with the interactive disk schema. It replaces an arbitrary JSON memory state after every historical session and persists states and request receipts in a checkpoint. Later writers receive only the latest derived state plus the next session; the final answer receives only that state and the question. The judge receives all original histories. A failed grade does not roll back that state or initiate a revision in the inspected `run_one`. See [MEM-RTE-sequential-campaign](#mem-rte-sequential-campaign).

## Shared records

### Components

#### MEM-CMP-analysis-model
Label: UserMemoryAgent analysis model

Source-native identity: `UserMemoryAgent.model`, including the instance created as `BackgroundMemoryProcessor.analysis_agent`. Representational form: opaque distributed-parametric completion model; proposals arrive as text and symbolic function calls. Storage substrate: configured external OpenAI-compatible service. SRC-1: `chapter3/user-memory/agent.py`, `chapter3/user-memory/background_memory_processor.py`.

Parameters changing during operation: uninspected at the provider; the caller implements inference, not weight updates. Exact version pinned: no immutable weight identity. Mutable endpoint resolving to another model: afforded by provider/model arguments and OpenRouter fallback mapping; provider alias behavior uninspected. Distinct from [RT-CMP-context-model](runtime.md#rt-cmp-context-model) and [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model): different clients, prompts and consumers, not evidence of distinct underlying weights.

> self.analysis_agent = UserMemoryAgent(
> --- `chapter3/user-memory/background_memory_processor.py`

#### MEM-CMP-conversational-model
Label: ConversationalAgent answer model

Source-native identity: `ConversationalAgent.model`. Representational form: distributed-parametric provider model receiving prose messages. Storage substrate: external service. Parameters changing during operation: provider internals uninspected; no weight-update operation in this client. Exact version pinned: no. Mutable endpoint resolving to another model: afforded by configuration and fallback; service behavior uninspected. Unlike [MEM-CMP-analysis-model](#mem-cmp-analysis-model), this client answers and writes raw dialogue, without mutation tools. No supplied runtime component denotes this client. SRC-1: `chapter3/user-memory/conversational_agent.py`.

> # Initialize memory manager (read-only access)
> self.memory_manager = create_memory_manager(user_id, memory_mode)
> --- `chapter3/user-memory/conversational_agent.py`

#### MEM-CMP-writer-client
Label: Sequential campaign writer model

Source-native identity: `Campaign.writer_client` with `args.writer_model`. Representational form: distributed-parametric external model producing JSON replacement memories and text answers. Storage substrate: configured writer service. Parameters changing during operation: uninspected; inference only in caller. Exact version pinned: no; mutable endpoint/model overrides can change resolution. Distinct from the tool-based [MEM-CMP-analysis-model](#mem-cmp-analysis-model); no supplied runtime counterpart. SRC-1: `chapter3/user-memory/run_evaluation.py`.

#### MEM-CMP-judge-client
Label: Sequential campaign judge model

Source-native identity: `Campaign.judge_client` with `args.judge_model`. Representational form: distributed-parametric model producing JSON judgments; host then applies symbolic score clipping, thresholds and hallucination veto. Storage substrate: configured judge service. Parameters changing during operation: uninspected; no caller update. Exact version pinned: no. Mutable endpoint resolving to another model: afforded by configuration; alias resolution unavailable. Separate endpoint/client role from [MEM-CMP-writer-client](#mem-cmp-writer-client), not authenticated independence of model internals. No supplied runtime counterpart. SRC-1: `chapter3/user-memory/run_evaluation.py`.

### Operative objects

#### MEM-OBJ-memory-note
Label: MemoryNote content and addressing metadata

Source-native identity: `MemoryNote` objects in `NotesMemoryManager.notes`. Storage substrate: list and per-user JSON file under `Config.MEMORY_STORAGE_DIR`. Representational form: natural-language `content`, with symbolic UUID, tags, session and timestamps. Lineage: tool/direct/CLI-authored content plus generated metadata; enhanced notes use the same class with a different extraction instruction. Actual content origin is caller-dependent, and preexisting files' provenance is unresolved. The session ID records the writing agent's session, not a verbatim source citation or extraction reason. All fields enter formatted model context. No supplied runtime counterpart; different user/store from [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history). SRC-1: `chapter3/user-memory/memory_manager.py`, `chapter3/user-memory/agent.py`.

> # Both basic and enhanced notes use the same manager
> # The difference is in the prompts used by the agent
> return NotesMemoryManager(user_id)
> --- `chapter3/user-memory/memory_manager.py`

#### MEM-OBJ-memory-cards
Label: Basic hierarchical memory cards

Source-native identity: `JSONMemoryManager.memory_cards`. Storage substrate: nested dictionaries and the per-user JSON file. Representational form: symbolic category/subcategory/key addressing and source/timestamp metadata; values are arbitrary content interpreted by the model, not executable rules merely because they are JSON. Lineage: direct dictionaries, parsed tool-add strings or legacy colon-text fallback; update with a string stores that string as the value rather than parsing a replacement dictionary. Add overwrites an existing addressed value; update replaces value/source/timestamp. Entire dictionary is rendered to the model. Distinct from [MEM-OBJ-memory-note](#mem-obj-memory-note); no supplied runtime counterpart. SRC-1: `chapter3/user-memory/memory_manager.py`, `chapter3/user-memory/agent.py`.

> self.memory_cards[category][subcategory][key] = {
>     'value': value,
>     'source': session_id,
>     'updated_at': datetime.now().isoformat()
> }
> --- `chapter3/user-memory/memory_manager.py:426-430`

#### MEM-OBJ-categories
Label: Advanced JSON category cards

Source-native identity: `AdvancedJSONMemoryManager.categories`. Storage substrate: nested dictionary and per-user JSON file. Representational form: symbolic category/card-key addressing and metadata; arbitrary JSON card facts, person, relationship and backstory are model-interpreted content. Lineage: tool/direct proposals with generated metadata and default fields. Add supplies a missing backstory as an empty string; a requested rationale is not necessarily retained. Update replaces the card rather than merging arbitrary missing fields; it preserves creation metadata but refreshes source/update metadata. Display excludes `_metadata`, not backstory. Thus later consumers can receive a supplied explanation without its internal write metadata. Distinct from basic cards and all supplied runtime objects. SRC-1: `chapter3/user-memory/memory_manager.py`, `chapter3/user-memory/agent.py`.

> # Remove internal metadata from display
> display_card = {k: v for k, v in card.items() if k != '_metadata'}
> --- `chapter3/user-memory/memory_manager.py`

#### MEM-OBJ-conversation-turn
Label: Raw conversation turns

Source-native identity: `ConversationTurn` in `ConversationHistory.conversations`. Storage substrate: list, per-user history JSON, and optionally external Dify documents. Representational form: natural-language user and assistant messages with symbolic session/turn/time metadata. Lineage: interactive answer writes both sides; direct evaluation can supply fixture histories; no extraction occurs in the local history write. Processor reads recent persisted turns across sessions; conversational agent reads current-session turns. Optional index payload contains text and session/time/turn metadata, not a user identifier. Distinct from [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history): different object, driver and persistence. SRC-1: `chapter3/user-memory/conversation_history.py`, `chapter3/user-memory/main.py`.

#### MEM-OBJ-memory-states
Label: Sequential campaign derived states and raw checkpoint receipts

Source-native identity: `checkpoint["memory_states"]`, `writer_calls`, `judge_calls`, `answer`, and `result`. Storage substrate: in-memory dictionaries and per-case/mode JSON checkpoints, atomically replaced via thread-specific temporary file. Representational form: mixed container. Derived `memory` content is model-interpreted JSON; session indices, purpose/signature/status fields are symbolic resume controls; requests/responses are raw receipt payloads. The initial state is empty list except basic JSON's empty dictionary. Each replacement derives from previous memory and one supplied fixture session. Receipt internals are not independently authenticated or fully inspected. States retain prior versions for checkpoint evidence, but the next writer selects only the last state. No supplied runtime counterpart; not the interactive managers' schema. SRC-1: `chapter3/user-memory/run_evaluation.py`.

> states = list(checkpoint.get("memory_states", []))
> memory: Any = states[-1]["memory"] if states else initial_memory(mode)
> --- `chapter3/user-memory/run_evaluation.py`

### Routes

#### MEM-RTE-trace-maintenance
Label: Conversation trace to directly mutated user memory

Endpoints/progression: interactive caller increments count → processor reloads history → recent/unprocessed turns become an analysis task → UserMemoryAgent model proposes add/update/delete → local dispatcher mutates its manager and attempts persistence → later answer reload. Owner: processor and local Python dispatcher; model authors selected mutations. Direct `analyze_conversation` accepts caller-supplied history instead of the disk selector; `apply_memory_updates` is another exposed mutation helper, not the ordinary analysis return path. Distinct from supplied [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate): user-fact mutation, not policy-source generation. SRC-1: `chapter3/user-memory/background_memory_processor.py`, `chapter3/user-memory/agent.py`, `chapter3/user-memory/memory_manager.py`, `chapter3/user-memory/main.py`.

Trigger: interval count, manual process/save, direct/batch analysis. Proposed change: selected facts/preferences, replacement of changed content and removal of inaccurate content. Admission: parse tool JSON, fixed names, Python argument/manager checks; basic JSON permits text fallback; advanced JSON rejects unparsable strings. No factual answer oracle or content-by-content human approval. The human launches/configures the workflow and supplies dialogue, not each extraction. Unknown names and parsing/errors can reject calls; writes that preceded later errors are not rolled back. Save failures are logged and swallowed by managers, so a success label is not proof of durable admission. Guidance is mode-specific extraction prose and the analysis task; reasons are not required in note/basic-card storage. Recovery is new mutation/reload, not a transactional previous-version restore. Operating mode: open conversations or caller-supplied batches, with a bounded fifteen-iteration default per analysis task.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ordinary analyze returns an empty update list even after direct tool mutation; recent-processing reconstructs a summary from recorded tool calls; direct apply returns counters/details.
- Later read-back: persisted notes/cards reach later conversational requests via reload; the analysis agent's live conversation also retains previous tasks, context and tool replies across processing calls.
- Delegated visibility: provider receives supplied user/assistant transcript, formatted memories and accumulated analysis conversation; dispatcher receives tool arguments; there is no separate evaluator approving fact truth.
- Selection predicate: recent tail bounded by context_window (default ten turns), minus in-memory processed IDs; min_conversation_turns guard; model chooses mutation contents/IDs. Batch/direct paths supply their own transcripts.
- Invalidation or expiry: IDs/counts marked before analysis; restart clears processed IDs. Explicit update/delete/clear and note-count eviction change retained state. No rollback on provider error.
- Activation or effect: local mutations and delivery to future prompts are wired; actual extraction, compliant answers and improved capacity remain unobserved.
- Evidence limits: persistence errors may not propagate; processed IDs are not durable; external/direct concurrent edits can be overwritten by stale writer instances; no observed campaign or deployed filesystem contract.

> # Since the agent directly updates memories via tools, we don't need to return updates
> # The memories are already updated in the memory manager
> # Return empty list as updates were applied directly
> return []
> --- `chapter3/user-memory/background_memory_processor.py`

> if turn_id not in self.processed_turn_ids:
>     unprocessed_turns.append(turn)
>     self.processed_turn_ids.add(turn_id)
> --- `chapter3/user-memory/background_memory_processor.py`

#### MEM-RTE-conversation-reload
Label: Reload retained facts into later conversation requests

Endpoints/progression: chat call → reload manager file → render all retained notes/cards and active-session history → append context to transient latest user message → provider → raw answer/history write. Owner: ConversationalAgent. Distinct from [RT-RTE-context-task](runtime.md#rt-rte-context-task), which uses live context-agent state and does not load this user file. SRC-1: `chapter3/user-memory/conversational_agent.py`, `chapter3/user-memory/memory_manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed answer or caught error text; successful answers append a raw turn to history.
- Later read-back: next chat reloads changed user memory, including across process/session boundaries; current-session history can recur, while older-session raw dialogue is withheld by this builder.
- Delegated visibility: model sees all rendered retained content, current-session turns and live conversation. Advanced internal metadata is omitted; raw messages, not augmented context blocks, are persisted in conversation/history.
- Selection predicate: enable_memory_context gates this builder; user ID selects the file, not relevant items. Active session ID filters raw history. Every retained item is rendered, without query or max_memory_context slicing.
- Invalidation or expiry: reset_session resets live conversation/session, not long-term file; disk deletion affects the freshly rendered block, but previous raw exchanges already in live conversation are not withdrawn.
- Activation or effect: prompt supply is wired, not reliable factual reliance or obedience. No item-level token budget is enforced in this builder; max_tokens bounds requested output, not selected retained input.
- Evidence limits: no successful reload/model trace inspected; availability of the file is not evidence that its content is true; live conversation may preserve consequences of earlier memory after withdrawal.

> self.memory_manager.load_memory()
> --- `chapter3/user-memory/conversational_agent.py`

> self.conversation.append({"role": "user", "content": message})
> api_messages = self.conversation[:-1] + [{"role": "user", "content": full_message}]
> --- `chapter3/user-memory/conversational_agent.py`

#### MEM-RTE-offline-maintenance
Label: CLI and direct manager editing and consolidation

Endpoints/progression: explicit add/update/consolidate command → fresh manager/file load → supplied content or deterministic consolidation → file save → query/show or later conversation reload. Owner: CLI caller and deterministic manager. Distinct from [MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance): no model required for notes editing/consolidation. No supplied runtime counterpart. SRC-1: `chapter3/user-memory/memory_cli.py`, `chapter3/user-memory/memory_manager.py`.

Trigger/proposal/admission: CLI add/update explicitly supplies text, IDs and tags; a human operator can author these, but generic library callers leave initial human control unresolved. Consolidation computationally chooses retained versions under an unchanged rule: normalized equal text merges tags and keeps newest; different content grouped under first tag keeps most recently updated. Human chooses whether conflict pass runs, not each winner. This is not semantic proof of contradiction or recency correctness. No answer oracle or substantive review gate. Invalid update IDs fail; notes add CLI excludes card modes. Direct deletion/clear APIs remove state. Rejection of consolidation is possible by not invoking it or disabling conflict resolution; no built-in undo stores discarded versions. Report returns superseded content; ordinary note storage does not retain that report as a later model rationale.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: IDs/status, query/show display, or consolidation report with counts and superseded content.
- Later read-back: modified persisted content is visible to a fresh CLI manager and conversation reload; report itself has no inspected model-consumer route.
- Delegated visibility: inapplicable — offline commands dispatch local code and display to the caller without provider delegation.
- Selection predicate: query is case-insensitive substring over note content/tags or card path/value fields; consolidation uses normalized text, first tag and update timestamp, not embeddings or learned relevance.
- Invalidation or expiry: overwritten/deleted/evicted entries leave the current file; notes add enforces MAX_MEMORY_ITEMS (default 100). Other managers have no equivalent item eviction in inspected methods.
- Activation or effect: computational mutation and query/display are wired; semantic correctness and benefit unobserved.
- Evidence limits: direct callers may be software rather than humans; atomic replacement is not multi-writer synchronization or rollback; save errors are swallowed; CLI update supplies strings and is not a general card-editor adapter.

> winner = max(members, key=lambda m: m.updated_at)
> superseded = [m for m in members if m is not winner]
> --- `chapter3/user-memory/memory_manager.py`

#### MEM-RTE-history-search
Label: Local history search and optional Dify indexing/search

Endpoints/progression: add_turn → local save and optional Dify index; search_history API → local substring search or configured Dify request → parsed ConversationTurns returned to caller. Owner: history manager/client. This API is a capability, not an established model retrieval route: inspected UserMemoryAgent advertises and dispatches only add/update/delete despite enable_memory_search and prompt wording. Distinct from [RT-RTE-context-task](runtime.md#rt-rte-context-task); no supplied counterpart. SRC-1: `chapter3/user-memory/conversation_history.py`, `chapter3/user-memory/agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: matching local or reconstructed remote turns; remote failures return empty list.
- Later read-back: uninspected — API can return retained turns to an unspecified caller, but no inspected shipped model consumer invokes this search operation.
- Delegated visibility: configured Dify receives user/assistant text and session metadata, then query and retrieval parameters. Service embedding payload/storage semantics are opaque.
- Selection predicate: local first limit substring matches; Dify receives semantic search, reranking, top_k twice limit and threshold 0.5. user_id argument is not transmitted in the inspected search payload; no user filter is established there.
- Invalidation or expiry: local clears do not issue an external index deletion in inspected methods; remote expiry and deletion behavior uninspected.
- Activation or effect: index/search HTTP request wiring only; neither target service compatibility, cross-user exposure nor successful model consumption is observed.
- Evidence limits: no registered Dify service snapshot; dataset configuration might separate users, but that contract is not evidenced. SimpleEmbeddingSearch uses Jaccard keywords and has no inspected consumer here.

> payload = {
>     'query': query,
>     'limit': limit,
> --- `chapter3/user-memory/conversation_history.py`

#### MEM-RTE-sequential-campaign
Label: Sequential memory replacement and checkpointed evaluation

Endpoints/progression: case histories and mode → checkpoint resume → latest memory plus one session to writer → parsed replacement state → fresh memory-only answer → full-source judge → host grade/checkpoint. Owner: Campaign.run_one; model proposes each replacement; host accepts parsed JSON without fact-level human review or a required mode schema. The human chooses cases/modes/models and budgets. Distinct from [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation): sequential retained user-state comparison, not same-agent context omission. SRC-1: `chapter3/user-memory/run_evaluation.py`.

Trigger: historical session sequence and mode comparison. Proposed change: replace memory, preserving useful facts under the mode instruction. Admission/rejection: JSON parsing and response reuse rules; no pre-answer factual grade gate. A grade's hallucination veto controls reported pass/reward, not reversal of memory. Resume rejects mismatched endpoint/model/seed signatures, but the inspected signature does not include fixture hash or prompt/budget identity. Guidance is the extraction instruction, current memory and new session; advanced instruction requests ordered conflicting versions. Checkpoints retain state versions and raw calls. Recovery skips stored states or reuses a successful purpose-labelled response; completed checkpoints return the old result. There is no inspected operational deployment/adoption beyond the campaign answer and next writer.

Answer oracle: judge gets original fixture histories, question, criteria and expected behavior as its reference, then produces a model judgment; host clips scores and uses hallucination veto plus thresholds. This is an explicit source/rubric, not proof of judge truth or independence. Operating mode: bounded case-by-mode experiment. No content-directed criticism/revision loop from judge output back to writer is traced.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-case/mode memory states, answer, raw judgment, host summary and receipts; completed checkpoints can return cached result.
- Later read-back: derived memory shapes the next session's writer request and final answer; checkpoint resume restores latest state and reuses prior calls/results across invocations.
- Delegated visibility: writer gets latest derived state plus current raw fixture session, not older raw sessions; answer gets memory and question; judge gets all raw fixture histories plus answer/rubric. Calls/state evidence persists separately.
- Selection predicate: case/mode checkpoint name, signature equality, last state and session index; successful-call search by purpose excluding error/length finish. Configured memory_max_tokens bounds proposed output, not a fact-relevance selector or current-state input slicing.
- Invalidation or expiry: signature mismatch raises; caller can choose another checkpoint directory; no automatic state expiry, rollback from grade or old-version deletion in inspected run_one.
- Activation or effect: parsing, replacement, later prompt delivery and source-based grading are wired; actual memory retention quality and improved future capacity remain unobserved.
- Evidence limits: recorder internals, retained campaign runs and outer report aggregation not inspected; checkpoint signature does not establish source/case freshness; generated memory schema and factual completeness are not validated by parse_json.

> parsed = parse_json(content)
> memory = parsed.get("memory", parsed)
> --- `chapter3/user-memory/run_evaluation.py`

> "CURRENT MEMORY STATE (the only retained information from older sessions):\n"
> --- `chapter3/user-memory/run_evaluation.py`

### Claims

#### MEM-CLM-backstory-confusion
Label: Advanced backstory and person confusion prevention

Claimed operation: prompt says backstory/person prevent confusion about entity ownership. This is requested rationale-bearing content and attributed design, not measured effectiveness. Supported mechanism is retaining supplied fields and delivering them after metadata filtering, as [MEM-OBJ-categories](#mem-obj-categories) records. No supplied counterpart. SRC-1: `chapter3/user-memory/agent.py`.

> CRITICAL: The backstory and person fields prevent confusion. For example, without proper person identification,
> a dermatologist for a child might be mistakenly suggested for an elderly parent's Alzheimer's care.
> --- `chapter3/user-memory/agent.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-context
Label: Retained user facts as model context

Consumer: ConversationalAgent completion model, and UserMemoryAgent analysis model. Channel: rendered notes/card contents embedded in user messages; system prose requests personalization or memory management. Force: natural-language interpretation, not verified knowledge or an executable policy. Horizon: subsequent calls/sessions while the file and managers persist; accumulated analysis prompts may preserve older versions even after a current-file delete. Distinct from [RT-BAP-system-prompt](runtime.md#rt-bap-system-prompt): dynamically retained user content, not the static context-agent instruction. SRC-1: `chapter3/user-memory/conversational_agent.py`, `chapter3/user-memory/agent.py`, `chapter3/user-memory/memory_manager.py`; [MEM-RTE-conversation-reload](#mem-rte-conversation-reload), [MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance).

#### MEM-BAP-campaign-state
Label: Derived campaign state as later writer and answer context

Consumer: writer model in next-session update and final answer. Channel: JSON-dumped latest memory in user prompt. Force: model-interpreted information under extraction/answer system guidance, not parser-enforced factual reliance. Horizon: rounds of one case/mode and resumed checkpoint invocations. Host resume additionally grants symbolic authority to status/signature/session index and stored calls when skipping work. Distinct from [RT-BAP-candidate-policy](runtime.md#rt-bap-candidate-policy): no compiled memory rule or installed policy. SRC-1: `chapter3/user-memory/run_evaluation.py`; [MEM-RTE-sequential-campaign](#mem-rte-sequential-campaign).

## Annotations

#### On [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history)

Memory consumer is a subsequent completion invocation on the same live context-agent object. Form is mixed roles/tool IDs and prose tool/task/answer content; storage is in-process. Full mode delivers accumulated history, while NO_HISTORY withholds earlier stored material. Reset/replacement ends that horizon. The serialized single-task result is a raw report, not a derived memory with a proven reload consumer. Supplied [RT-RTE-context-task](runtime.md#rt-rte-context-task) and [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation) provide the source passages and wired/uninspected distinction. No new direct-source claim.

#### On [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate)

The supplied campaign's rejected-control check summary is trace-fed feedback to a later coding request, not merely retained logging. Synthetic trajectories and software-authored rejection lineage distinguish it from user dialogue. Diagnosis/rejected reasons and source persist in artifacts/receipts; executable candidate content reaches evaluator functions, while rejected reasons reach the coding provider. Stable unchanged and no traced installation limit authority to generation and evaluation, not cross-session live policy learning. The supplied route and [RT-BAP-candidate-policy](runtime.md#rt-bap-candidate-policy) support these findings and retain independent theory/self-improvement limits.

## Write side

[MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance) supplies the raw-to-derived-to-later-consumer chain. Automatic recent-turn selection is count-triggered and session-independent; direct batch analysis bypasses that selector. Inputs mix original user text and generated assistant replies. Authoring is model-directed; storage I/O is deterministic; semantic admission has no separate fact-check gate. The mode prompts ask for facts and correction, but this does not establish criticism of formulated theories or truthful extraction. Learning as improved future capacity is uninspected even though trace-fed behavior-shaping writes are wired.

The direct `apply_memory_updates` helper accepts externally supplied decisions. Its advanced add can turn `MemoryUpdate.reason` into `backstory`; ordinary `analyze_conversation` does not return those updates and uses tools directly. This counterpath prevents concluding that all routes either retain or omit reasons uniformly. Notes/basic cards retain no mandatory extraction rationale. Advanced cards can retain a supplied backstory that later display includes. SRC-1: `chapter3/user-memory/background_memory_processor.py`, `chapter3/user-memory/memory_manager.py`.

Updates, deletes and clearing alter the current file; they do not withdraw already embedded context from the analysis agent's live conversation. Analysis `_get_memory_context` renders its existing manager without reloading; the conversational read side does reload. The processor's own manager is a third instance. `memory_cli extract` prints that separate instance after tool writes without an intervening reload, so its display is not dependable evidence of resulting disk content. Its alternating nonblank-line role adapter also does not authenticate the origin of a supplied transcript. SRC-1: `chapter3/user-memory/agent.py`, `chapter3/user-memory/background_memory_processor.py`, `chapter3/user-memory/memory_cli.py`.

[MEM-RTE-offline-maintenance](#mem-rte-offline-maintenance) adds explicit caller-authored notes and deterministic newest-version selection. Consolidation can discard distinct facts that share a first tag; the algorithm's conflict label is not a semantic warrant. Atomic save protects against a partially dumped final file, but shared temporary filenames and separate stale lists do not establish multi-writer consistency. Persistence failures log rather than fail the tool's success return. No universal deletion/rollback guarantee follows. SRC-1: `chapter3/user-memory/memory_manager.py`.

[MEM-RTE-sequential-campaign](#mem-rte-sequential-campaign) provides an alternative checkpoint form: raw receipts and all derived memory states coexist. Next-state selection uses only the latest state; preservation of rationale is instruction-dependent rather than a mandatory reason field. Judge reasoning persists as a result, without an inspected next-update consumer. This differs from the supplied retry-policy route, where rejected-check reasons enter a subsequent model request.

## Read-back

[MEM-RTE-conversation-reload](#mem-rte-conversation-reload) is automatic context supply on each chat request, not a model-requested item search. Trigger and selector inputs are the call, enable flag, user ID and active session ID. Selected parts are all rendered memories plus active-session raw turns. No relevance query or enforced item/token input cap occurs; note-count eviction is a write-side storage limit, not targeted read selection. Content reaches the provider as user-message context and gains only interpretive authority.

The mutation agent offers a different read: all in-memory facts and optionally all local history, plus previous augmented tasks/tool results already in its live conversation. Its advertised `enable_memory_search` flag does not add a search tool. [MEM-RTE-history-search](#mem-rte-history-search) therefore remains an exposed capability, not an established model retrieval route. Optional Dify index/search calls do not prove end-to-end service operation or subsequent answer consumption. SRC-1: `chapter3/user-memory/agent.py`, `chapter3/user-memory/conversation_history.py`.

The evaluation path in `main.py` calls batch analysis, clears answering agent raw history in memory, resets its prompt and reloads derived memory before asking the test question. That establishes an intended structured-memory-only answer path. It does not reset the processor's analysis agent before every test in the inspected preparation, nor validate the truth of extracted memories. Batch summaries can say no updates because analysis returns `[]` after directly mutating tools; the printed summary is not proof that no write happened. The grade then goes to the framework, not into a traced memory correction. SRC-1: `chapter3/user-memory/main.py`, `chapter3/user-memory/background_memory_processor.py`.

> # CRITICAL: Reload the agent's memory manager to get the memories saved by the processor
> # The processor and agent have separate memory manager instances, so we need to reload
> # from file to get the memories that were just saved
> agent.memory_manager.load_memory()
> --- `chapter3/user-memory/main.py`

The sequential campaign instead restores state/calls from disk and reuses purpose-labelled receipts. Latest memory feeds the next writer and answer; all original sessions are restricted to the judge's reference channel. A stored result can bypass new model calls, so changed fixtures/prompts with an unchanged checkpoint signature would not automatically generate fresh evidence. See [MEM-RTE-sequential-campaign](#mem-rte-sequential-campaign).

## Integration issues

- No correction to a supplied runtime declaration is required. Its selected-loop limits remain valid. All new records describe separate user-memory or campaign entities; no possible duplicate with supplied runtime records after comparison. Context history and candidate feedback are annotations rather than new declarations.
- The suite's uninspected backends, retrieval variants, skills and other chapter loops remain included unresolved coverage, not exclusions or absences. The coverage table states missing facts and prevents suite-wide classification; reconciliation must not generalize this subset's admission, storage or read-back mechanisms.
- [MEM-RTE-trace-maintenance](#mem-rte-trace-maintenance): recent-processing marks turns before successful analysis, and ordinary analysis returns an empty list after direct mutation. Batch reports and no-update labels can hide writes/failures. Separate manager instances and retained analysis conversation limit reliable reset, withdrawal and evaluator independence. Supported by SRC-1: `chapter3/user-memory/background_memory_processor.py`, `chapter3/user-memory/agent.py`, `chapter3/user-memory/main.py`.
- [MEM-RTE-history-search](#mem-rte-history-search): search-tool wording is unsupported by the inspected dispatcher; service user isolation and deletion propagation remain unresolved. Local API and external indexing capability must not be promoted to a deployed model read-back route. SRC-1: `chapter3/user-memory/agent.py`, `chapter3/user-memory/conversation_history.py`.
- [MEM-RTE-offline-maintenance](#mem-rte-offline-maintenance), [MEM-OBJ-categories](#mem-obj-categories): recency-based selection and card replacement are not semantic adjudication or guaranteed rationale preservation. Save-success and disk durability differ. SRC-1: `chapter3/user-memory/memory_manager.py`.
- [MEM-RTE-sequential-campaign](#mem-rte-sequential-campaign): schema/freshness checks are weaker than labels may suggest; grade is retained evidence, not a feedback-driven revision or admission veto on memory. Fixture provenance, recorder behavior and observed results remain uninspected. SRC-1: `chapter3/user-memory/run_evaluation.py`.

## Limitations and checks

Source identity and full HEAD match the supplied boundary. Method identity is the supplied memory job, memory member type, worker rules and records contract; no prior analyses or peer state were consulted. Direct implementation inspection and supplied runtime findings are kept separate. No new source ID or evidence layer is introduced. No source/model execution, service calls, dependencies, fixtures, observed-run assertions, causal benefit, reliable semantic authority or suite-wide negatives are claimed.

Deterministic validation: the invocation's `commonplace-run validate-output` passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes structure and quotation occurrence, not semantic acceptance. Uninspected variants, model internals, persisted-file provenance, external Dify storage and retained run evidence prevent stronger conclusions.
