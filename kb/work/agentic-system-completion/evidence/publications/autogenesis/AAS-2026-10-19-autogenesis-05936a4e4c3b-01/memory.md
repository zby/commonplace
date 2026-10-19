---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Autogenesis memory: lifecycle-fed tiers, lossy compaction, separate display persistence, task plans and explicit corpus retrieval."
run-id: AAS-2026-10-19-autogenesis-05936a4e4c3b-01
source-identity: https://github.com/DVampire/Autogenesis
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis memory report

## Boundary and evidence

This member covers memory and working-context mechanisms inside the whole-system [boundary](boundary.md), at SRC-1 commit `5b070d5cd497e951a188a01409138e8b530eaf4a`. It follows the supplied [runtime](runtime.md), then directly inspects lifecycle hooks, concrete backends, their consumers, memory generation and evaluation, persistent conversations, plans, knowledge operations, trajectory export and alternative checkpoints. Source text supplies implementation and doctrine/design evidence, not observed operation. No target code or examples were run.

The central distinction is between `TieredMemory.get()`, which selects live in-process state for the next model decision, and `_render()`, which writes a disk display. Their selections differ. A memory source edit that changes only `_render()` does not thereby change the model's next memory view. File persistence also does not imply restart rehydration. Conversation transcript reopening, todo reload and workflow resume are different paths with different consumers.

All paths below are in SRC-1. “Direct” means source read for this member; “supplied” means the runtime's retained findings and passages. Uninspected available material is not an access gap or an absence.

| Entry point or operation | Source paths and inspection | Coverage and conclusion limit |
|---|---|---|
| Console/Gateway/direct driver | `autogenesis/cli.py` direct entry range; `autogenesis/gateway/service.py` memory initialization searches and conversation handlers direct; example bootstrapping supplied | [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task), [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent); terminal uses Gateway rather than a second memory loop. |
| Lifecycle writes, overflow and prompt reads | `autogenesis/hook/default/memory.py`, `autogenesis/hook/default/compact.py`, `autogenesis/memory/default/tiered.py`, both built-in renderers direct; agent context range direct | [MEM-RTE-tiered-context](#mem-rte-tiered-context), [MEM-RTE-history-compaction](#mem-rte-history-compaction); selected event records, not a guaranteed complete transcript. |
| Registry, legacy session/state APIs, cleanup | `autogenesis/memory/server.py`, `autogenesis/memory/types.py` direct; initialization, registration, build/restore/cleanup and wrapper ranges of `autogenesis/memory/context.py` direct | [MEM-OBJ-memory-config](#mem-obj-memory-config), [MEM-ABS-tiered-reload](#mem-abs-tiered-reload). Legacy wrappers call methods not supplied by TieredMemory; cannot infer functional old insights/state routes from API names. Copy/update internals were only searched; no complete lifecycle audit. |
| Memory machinery authoring/admission | `autogenesis/hook/default/memory_registration.py`, generator and optimizer finalization direct; `autogenesis/extension/server.py` startup/add/load/unload ranges direct | [MEM-RTE-memory-admission](#mem-rte-memory-admission), a memory-specific part of supplied extension admission; class registration leaves instance null. |
| Evaluation and creator guidance | `autogenesis/agent/evaluator/memory_evaluate_agent.py`, `autogenesis/prompt/default/memory_evaluate_agent.html`, `autogenesis/skill/creator/memory_creator_skill/SKILL.md` direct | [MEM-CLM-memory-guidance](#mem-clm-memory-guidance); incompatible contracts and unresolved named inspection/probe tools prevent treating evaluator scores as retention evidence. |
| Shipped alternative memory renderers | `extension/memory/constraint_memory.py`, `extension/memory/file_system_memory.py` direct | [MEM-OBJ-memory-display](#mem-obj-memory-display); keyword-based “confirmed constraints” change persisted display, not inherited get/compaction. No independent verification or protected constraint tier established. |
| Todo mutations and reinjection | `autogenesis/tool/default/todo.py` write, reload and dispatch ranges; `autogenesis/agent/types.py` context range direct | [MEM-RTE-todo-context](#mem-rte-todo-context); disk-backed model-authored plan, separate from lifecycle-derived display todos. Export/update edge cases not exhaustively inspected. |
| Conversation transcript and chat feedback | `autogenesis/conversation/server.py`, Gateway conversation/chat handlers and `frontend/src/App.tsx` resumeChat range direct | [MEM-RTE-conversation-replay](#mem-rte-conversation-replay); client replay is wired, restoration of TieredMemory is not. Feedback's downstream improvement consumer is uninspected. |
| Knowledge ingestion/retrieval and workflow dispatch | `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`, `autogenesis/workflow/runtime.py` manager dispatch range direct | [MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval); request-directed top-k records in data envelope, not automatic agent prompt injection. |
| Data/process operations | `autogenesis/data/server.py` save/load direct; `autogenesis/process/server.py` signatures searched; workflow dispatch direct | Dataset save/load uses local HuggingFace storage or Hub, selected repo/source/split, full records returned. Upstream process transformations and graph consumers beyond the manager handoff remain uninspected; no automatic trace-to-trained-model chain established. |
| Snapshot, trace and trajectory | `autogenesis/hook/default/snapshot_hook.py`, `autogenesis/trajectory/server.py` direct; trace server signatures searched | [MEM-OBJ-execution-records](#mem-obj-execution-records); training export capability is not a trained successor. Trace writer and downstream training consumers uninspected. |
| Workflow/canvas and capability-version checkpoints | Supplied workflow route; `autogenesis/command/default/checkpoint.py`, `autogenesis/command/default/restore_checkpoint.py` direct | [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) plus annotation below; three different checkpoint forms, none a generic agent mailbox/memory restore. |
| Provider chat-memory alternatives | `autogenesis/plugins/types.py` MemoryPluginTool range, Mem0/Astra adapters direct; workflow DATASOURCE dispatch direct | [MEM-OBJ-plugin-history](#mem-obj-plugin-history); Astra external history is an adapter capability, Mem0 deliberately raises. Provider storage internals, deployed configuration, expiration and actual callers are unavailable/uninspected. |
| Static prompts, skills, sub-agent isolation and model state | Supplied runtime records, agent context range direct | [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation), [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager); no reclassification of static shipped instructions as use-derived memory. |

Excluded from this memory account are remote provider/dependency internals and external gitlinks already excluded by boundary. General workspace file editing can retain arbitrary products, but individual domain tools, sandbox environments and every frontend view were not traced as memory consumers. These limits prevent a universal inventory of all possible user-authored file recall and provider-native context features. They do not weaken the concrete compaction/read-back chain below.

## Core ideas

1. **Model context is rebuilt from selected state.** Agent requests memory by context identity; code chooses a chronological tail and recent summary chunks, then injects them into template context. It does not rank these records by current task similarity. Counts, not token lengths, bound the selection. Todo text and workspace state are additional inputs. See [MEM-RTE-tiered-context](#mem-rte-tiered-context) and [MEM-RTE-todo-context](#mem-rte-todo-context).
2. **Overflow becomes model-written memory.** A code threshold removes oldest records, a compact hook asks a model to summarize them, and later get calls deliver those summaries. Empty summarization restores the chunk. Successful compaction replaces raw details without retaining an explicit per-summary evidence map. This is a trace-fed, behavior-shaping write path; it establishes neither reliable summarization nor improved future capacity. See [MEM-RTE-history-compaction](#mem-rte-history-compaction).
3. **Display, retrieval and executable retention policy are separate.** JSON contains more raw records than HTML's recent tail, and HTML can visibly label constraints without changing prompt selection. The creator skill conflates `_render` with prompt delivery. A second gap is that extension class registration creates a temporary memory instance but stores null as the active instance. Both countercases qualify claims that registering a customized renderer immediately improves future recall. See [MEM-CLM-memory-guidance](#mem-clm-memory-guidance) and [MEM-RTE-memory-admission](#mem-rte-memory-admission).
4. **Persistence has several horizons.** Tiered state survives later calls while resident; todo files can be reread; conversation events reopen in a client; corpus records are retrieved by query; workflow checkpoints restore execution frames. None alone proves that every agent's remembered history returns after restart. See [MEM-ABS-tiered-reload](#mem-abs-tiered-reload).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-recent-history
Label: Recent history records

Source-native identity: `_SessionState.recent`, a deque of `MemoryRecord(ts,event,detail,status)` keyed by session ID. Python fields are symbolic access/status data; task/action/error/result strings are natural-language or stringified payload content interpreted by the summarizer and later agent. This is a selected projection of lifecycle traces, not the complete TraceEvent or opaque provider transcript. Agent starts, ends, tool/skill results, errors and explicit notes contribute. Reasoning can label the flow chart rather than enter recent history verbatim. Storage: process memory, also all retained recent records in GeneralMemorySystem JSON, only a recent tail in built-in FileSystemMemory HTML. Lineage: task input and model-selected tool/child/environment output can include external material; the label “raw” means uncompressed within this projection, not untouched original provenance. SRC-1, `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/memory.py`, `autogenesis/memory/default/general_memory_system.py`, `autogenesis/memory/default/file_system_memory.py`.

Closest supplied record: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) describes the broader invocation, not this stored object; no supplied object counterpart. Consumers are [MEM-RTE-history-compaction](#mem-rte-history-compaction) and [MEM-RTE-tiered-context](#mem-rte-tiered-context). The hook admits syntactically valid lifecycle input automatically; no human per-record approval or truth oracle is wired there. ON_STOP maps success from absence of error rather than preserving every success distinction.

> success=not bool(inp.error), result=inp.result,
> --- `autogenesis/hook/default/memory.py`

#### MEM-OBJ-working-memory
Label: Working memory summaries

Source-native identity: `_SessionState.working`, `deque[str]` with `maxlen=working_max` (default 10); natural-language summaries in process memory and rendered JSON/HTML. Derived from chronological chunks of [MEM-OBJ-recent-history](#mem-obj-recent-history), with the immediately previous summary supplied to avoid repetition. The compact model writes the text; code admits any nonempty result, and deque overflow drops oldest summary chunks. Later get selects the last `working_fetch` (default 5) chunks. No token bound, claim-level validation or retained per-summary source-event identifiers is implemented in this representation. Exact paths/errors are requested, not guaranteed. A source fact can survive as text, but no explicit criticism/reason record is required. SRC-1, `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py`.

No supplied object counterpart; complements the context supply point in [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task).

> self.working: Deque[str] = deque(maxlen=working_max)  # drops oldest summary when full
> --- `autogenesis/memory/default/tiered.py`

#### MEM-OBJ-memory-display
Label: Persisted memory displays

Source-native identity: `_SessionState.file_path`, GeneralMemorySystem `.memory.json`, FileSystemMemory `.memory.html`, and shipped constraint-oriented `_render` overrides. Disk encoding is symbolic JSON/HTML structure surrounding natural-language content. Todos and flow status are derived bookkeeping/display metadata, not separately verified world knowledge. Explicit snapshot metadata can replace todos/flow, long todo descriptions can be model-shortened, and labels are truncated to 80 characters. Get returns working/recent/final result, not todos/flow. General JSON retains every current recent record and working summary; built-in HTML displays only `recent_fetch` recent records but all retained summaries. Therefore disk render and prompt read are not interchangeable representations. SRC-1, `autogenesis/memory/default/tiered.py`, `autogenesis/memory/default/general_memory_system.py`, `autogenesis/memory/default/file_system_memory.py`.

The extension FileSystemMemory separates keyword matches before truncating the remaining recent list; ConstraintMemory writes keyword matches under “Confirmed constraints.” Both inherit unchanged get and oldest-first compaction. These are separate display variants within this object, not an additional protected knowledge store or evidence of verified constraints. Initialization of actual session content remains event-driven; mere inclusion of an example file does not establish its deployment. SRC-1, `extension/memory/constraint_memory.py`, `extension/memory/file_system_memory.py`.

> if "constraint" in text or "established" in text or "verified fact" in text:
> --- `extension/memory/constraint_memory.py`

No supplied object counterpart. Relation to [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest): that object records component source versions, not these per-session content files.

#### MEM-OBJ-memory-config
Label: Memory configuration and legacy interfaces

Source-native identity: `MemoryConfig`, `_memory_configs`, `_memory_history_versions`; symbolic class/config/version/metadata/code fields in process memory. Source code is executable Python, distinct from session content. `model_dump` deliberately omits the live instance. Initialization discovers registry classes and builds instances, while code-config loading starts with an empty dictionary. History and configs are cleared by manager cleanup; comments about saving are not file writes. Get returns the stored instance, contrary to the server docstring's “new instance each time.” SRC-1, `autogenesis/memory/context.py`, `autogenesis/memory/types.py`, `autogenesis/memory/server.py`.

The exposed legacy start/add/end/clear/get_state wrappers delegate to instance methods such as get_event/get_summary/get_insight. The inspected TieredMemory/base Memory implementation supplies emit/get instead, not those legacy methods. Thus API exposure alone is not an operative legacy memory consumer. Direct register/update/restore are software/caller operations; caller identity does not establish human approval. Their behavior is not equivalent to the extension's archived-source rollback. Closest supplied object is [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest), with distinct substrate/referent: manifest/archive versus in-process memory registration.

> return memory_config.instance if memory_config.instance is not None else None
> --- `autogenesis/memory/context.py`

#### MEM-OBJ-todo-files
Label: Todo plan files

Source-native identity: TodoTool per-ID `<safe_id>_steps.json` and `<safe_id>_todo.md`, plus cached `Todo.steps`. JSON step/status/priority/time/parameters are symbolic fields; names and result summaries are natural-language agent-authored plans and assertions. Mutation serializes structured steps and produces Markdown. Prompt content reads Markdown directly; cache recreation reloads JSON. This differs from [MEM-OBJ-memory-display](#mem-obj-memory-display)'s lifecycle-generated todos. Model-selected add/complete/update/clear changes the plan under software field checks, not independent verification. SRC-1, `autogenesis/tool/default/todo.py`, `autogenesis/agent/types.py`. No supplied object counterpart; context supply belongs to [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task).

> return Todo.read_content(self._file_path(id, "todo.md"))
> --- `autogenesis/tool/default/todo.py`

#### MEM-OBJ-conversation-events
Label: Conversation transcripts and identity

Source-native identity: ConversationManager metadata and per-conversation event JSONL under project paths. Metadata is symbolic identity, title, time and task associations; events retain mixed conversational/trace payloads. Save atomically replaces metadata; append is unbounded, best-effort, and requires a materialized parent directory. Events reads skip malformed lines. The later client receives events, not a reconstructed tiered backend. Gateway also exposes a separate owner/session chat.jsonl plus meta.json and feedback.jsonl surface; that API returns role/content records and stores thumbs feedback without establishing a learning consumer. Human authorship of a caller-supplied role/content/feedback record is unresolved. SRC-1, `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`.

Distinct object underlying supplied [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task)'s broad client reopening claim; no supplied object counterpart.

> Append-only and unbounded on purpose: this is the record of what
> happened, and the Gateway's in-memory buffer is neither.
> --- `autogenesis/conversation/server.py`

#### MEM-OBJ-knowledge-corpus
Label: Named knowledge corpus

Source-native identity: KnowledgeManager base directory `corpus.jsonl` and `manifest.json` selecting bm25/tfidf. Documents preserve supplied fields with normalized string `text`; source provenance/author/verification are caller-dependent optional content, not established by the base name or retrieval score. Symbolic JSON records contain natural-language texts; ranker numerical scores are computed selection data, not retained trained parameters. Each retrieval rebuilds sparse BM25 or TF-IDF/cosine ranking from current texts. No dense learned embedding backend is implemented by these two built-ins. Storage is disk corpus, loaded per retrieval; cleanup clears backend objects rather than deleting corpus files. SRC-1, `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`.

No supplied object counterpart. Its workflow consumer is a distinct part of [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution), not the automatic tiered-memory injection.

> tokenized = [str(text).lower().split() for text in texts]
> --- `autogenesis/knowledge/default/rankers.py`

#### MEM-OBJ-execution-records
Label: Snapshots and training trajectories

Source-native identity: SnapshotHook numbered per-agent HTML prompt snapshots; TrajectoryManager task-ID trajectories in memory and `<log_root>/trajectory/<task_id>.jsonl` on finalize/reward backfill. HTML is readable display of sent messages, not a hidden/opaque model checkpoint. Trajectories hold messages, reasoning, actions, observations, usage, success, final result and optional reward. Symbolic envelopes organize natural-language and stringified payloads. Trace server separately exposes emit/subscribe/writer; writer internals were not inspected here. SRC-1, `autogenesis/hook/default/snapshot_hook.py`, `autogenesis/trajectory/server.py`, `autogenesis/trace/server.py`.

Immediate source lineage is lifecycle inputs. Task/session IDs join records but are not content trust certificates. Trajectory export_sft/export_rl reads in-memory trajectory objects for optional training consumers; this module does not itself train a model or reload persisted trajectories. Reward backfill changes labels, not model weights. No supplied object counterpart; do not duplicate [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager)'s external model state or [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest)'s capability archives.

> step.messages_sent = inp.get("messages") or []
> --- `autogenesis/trajectory/server.py`

> traj = self._trajectories.get(task_id)
> return traj.to_sft_records() if traj else []
> --- `autogenesis/trajectory/server.py`

#### MEM-OBJ-plugin-history
Label: External plugin chat histories

Source-native identity: MemoryPluginTool message history; AstraDBChatMessageHistory adapter and Mem0ChatMemoryTool. Returned records have symbolic role/content envelopes containing natural-language messages; external storage substrate, indexing, expiry and transformations are opaque outside SRC-1. The base adapter can add user/AI messages or read all `.messages` by caller-selected session ID, delivering them as data records; it is not wired into TieredMemory.get. Astra requires external credentials/SDK. Mem0's _history explicitly raises NotImplementedError even with a key. The adapter wrappers also do not forward their explicit credential parameters to _memory; environment-based fallback remains possible for Astra. No successful service call was observed. SRC-1, `autogenesis/plugins/types.py`, `autogenesis/plugins/default/datastax/tools/astradb_chatmemory.py`, `autogenesis/plugins/default/mem0/tools/chat_memory.py`.

No supplied object counterpart. Workflow DATASOURCE dispatch affords a named plugin caller, but actual configured plugin registration, consumer graph and model delivery are uninspected, so no deployed read-back route is declared.

> raise NotImplementedError("Mem0 uses a client API; use mem0.MemoryClient(api_key).search/add.")
> --- `autogenesis/plugins/default/mem0/tools/chat_memory.py`

### Routes

#### MEM-RTE-tiered-context
Label: Tiered memory context delivery
Part of: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task)

Progression and owner: lifecycle memory hook validates the event envelope and emits to the selected primary and optional FileSystemMemory secondary sink; TieredMemory updates session state; each Agent context build requests get by ctx.id and review_steps, then supplies memory_context to its template. This route is the retained-state part of the broader task execution. Direct drivers use the same agent supply point when configured. Meta configuration selects file_system_memory, with memory enabled and evolvability true; its prompt_readable false flag is not consulted by this agent read. Hook errors are logged/swallowed. SRC-1, `autogenesis/hook/default/memory.py`, `autogenesis/memory/default/tiered.py`, `autogenesis/agent/types.py`, `configs/meta_agent.py`, `configs/memory/file_system_memory.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: emit updates resident state and schedules debounced persistence; get returns Markdown text or None, and context assembly substitutes placeholders for empty/missing memory.
- Later read-back: later model invocations receive working summaries, a recent tail, and final_result when present; same resident context identity can span tasks in one conversation, not guaranteed process restarts.
- Delegated visibility: child output enters parent action memory; full child context is not copied by delegation, as supplied runtime establishes.
- Selection predicate: code resolves configured memory and exact session ID, selects last working_fetch summaries and last short_term_n records (agent review_steps overrides recent_fetch), and includes final_result. No current-query relevance scoring.
- Invalidation or expiry: compaction removes oldest raw chunks; bounded working deque drops oldest summaries; least-recently-accessed sessions are evicted over max_sessions after persistence; missing state returns None rather than loading disk.
- Activation or effect: selected text can guide the next model decision; delivery is wired, changed behavior and truthful use are unobserved.
- Evidence limits: record counts do not bound text tokens; final_result is not bounded by the fetch counts; best-effort writes and async compaction do not guarantee complete durable history.

Admission is automatic software routing, not a human content decision. Inputs may originate in user tasks, model decisions, external tools or child responses. The consumer receives selected strings without source-tier-specific verification in get; a “done” or “confirmed” display label is not an independent truth warrant.

> recent = list(state.recent)[-n:] if n else list(state.recent)
> --- `autogenesis/memory/default/tiered.py`

> "memory_context": memory_body,
> --- `autogenesis/agent/types.py`

#### MEM-RTE-history-compaction
Label: History overflow compaction

No supplied route counterpart: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) identifies memory delivery but leaves the derived-memory write mechanism open. This is a distinct trace-fed transformation within the backend, also usable by other configured agent invocations.

Trigger/owner/progression: appending beyond recent_max schedules code-owned compaction; it pops the oldest compact_chunk records, formats lines and supplies the previous summary plus new records to the compact hook/model. Nonempty output is appended to working memory, then persisted; empty output restores the chunk and stops. Default recent_max=30, compact_chunk=10, working_max=10; selection uses working_fetch=5. The foreground agent does not select the chunk with a memory tool. Model role/configuration comes through the existing manager, not an additional independently pinned model component; model fixity/provider limits are [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager). SRC-1, `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: background consolidation updates working/recent state; no direct user answer or independently judged correctness result.
- Later read-back: later get requests deliver the selected retained summaries through [MEM-RTE-tiered-context](#mem-rte-tiered-context); the summarizer itself also reads the most recent prior summary on the next overflow.
- Delegated visibility: summarizer sees formatted records and one prior summary, not the whole foreground prompt, other sessions or complete trace artifacts.
- Selection predicate: chronological overflow threshold and oldest chunk, not topic relevance or verified importance; summarizer is asked for 2–4 sentences preserving paths, numbers and errors.
- Invalidation or expiry: successful summary replaces the removed raw chunk; empty summary restores it, while working deque overflow silently drops oldest summaries. Restored overflow can remain over threshold until a later attempt.
- Activation or effect: model-produced text becomes later decision context; actual reliance, fidelity and improved outcomes remain unobserved.
- Evidence limits: no provenance map links each summary assertion to raw events; restoring on empty result is not a semantic rejection gate for a misleading nonempty summary.

Software threshold chooses the candidate input, a runtime model proposes condensed text, and software nonemptiness decides admission. No per-summary human approval or answer oracle. This runs in ongoing open tasks, not a bounded comparison curriculum. Guidance requests preserving failures and values, not revising an explanation of why a capability failed. Output may retain reasons when summarized, but neither guaranteed reason preservation nor a separate rationale reader is implemented. This is automatic trace-to-derived-memory wiring, not merely raw logging, but learning as improved capacity is unestablished. Theory-builder conditions 1–4 are not established by compression alone: the output is history prose of unknown content, not necessarily a formulated theory with content-directed criticism and iteration.

> text = await self._summarise(items, existing)
> if text:
>     state.working.append(text)
> else:
>     async with state._lock:  # lossless: restore and stop
>         state.recent.extendleft(reversed(chunk))
>     break
> --- `autogenesis/memory/default/tiered.py`

#### MEM-RTE-memory-admission
Label: Memory component admission
Part of: [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission)

This is the memory-module branch, not a duplicate of generic extension admission. A successful memory generator/optimizer response invokes memory_registration_hook; code locates the .py, validates/promotes a staged path, and calls extension_manager.add_component("memory", ..., enable_evolving=True). Extension loading registers the class with memory_manager; archive/manifest and optional generic smoke follow. Proposal is executable retention machinery, not a session-memory assertion. SRC-1, `autogenesis/agent/generator/memory_generate_agent.py`, `autogenesis/agent/optimizer/memory_optimize_agent.py`, `autogenesis/hook/default/memory_registration.py`, `autogenesis/extension/server.py`, `autogenesis/memory/context.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registered name or hook block/exception; generator finalization can mark its response unsuccessful on block. Registration config can exist without an active instance.
- Later read-back: source is archived/manifested for reload, but the class-based register branch stores instance=None; get_info-based hooks and agent reads skip it until an additional build supplies an instance. No such build appears in the inspected extension load/add path.
- Delegated visibility: authoring worker returns reasoning/path and source is dynamically loaded in process; it does not transfer old backend session contents into a new instance.
- Selection predicate: located source path, registered class/name, existing evolvability gate and optional smoke; neither rubric scores nor explicit human approval are mandatory admission inputs here.
- Invalidation or expiry: override replaces config; generic smoke can revert/unload via supplied extension route, and unregister removes config without a tier-state migration protocol. Existing session content and artifact recovery must be distinguished.
- Activation or effect: registration changes configuration/source and can execute import/constructor code, but usable memory context delivery is not guaranteed by this class branch. The missing live instance qualifies the runtime's generic active-manager claim for memory.
- Evidence limits: no executed registration, migration or later recall trace; archive rollback is not recovery of an old live session, and generic smoke does not demonstrate retention correctness.

The model authors source under creator guidance; software validates/promotes and can reject. Caller-driven promotion is not proof of human content approval. Operating mode is open-task capability generation/repair, optionally prompted long-run retention probes. There is no independent expected recall answer consumed by this hook; the generic smoke oracle and optional bypass remain as supplied runtime documents. Software register/update and startup loading are alternative admissions, not all guaranteed to perform the same checks. Register accepts instance objects too, in which case it retains the supplied live instance; startup build also supplies instances. These countercases prevent a blanket claim that all memory configurations are inert.

> instance=memory_instance if isinstance(memory, Memory) else None,
> --- `autogenesis/memory/context.py`

> cfg = await memory_manager.register(cls, memory_config_dict=config, override=True, version=version)
> --- `autogenesis/extension/server.py`

#### MEM-RTE-todo-context
Label: Todo plan read-back
Part of: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task)

Owner/progression: foreground model/caller chooses todo_tool action and task/status/result fields; code validates and writes JSON plus Markdown. Each subsequent agent context build calls content(ctx.id), independently of use_memory. This is plan memory, not lifecycle memory curation. SRC-1, `autogenesis/tool/default/todo.py`, `autogenesis/agent/types.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutation/list/show returns a tool Response; disk Markdown is separately read for the next context.
- Later read-back: every later context build for the same ID requests the Markdown; tool cache recreation loads steps JSON if present. This has a disk read path missing from TieredMemory.
- Delegated visibility: content uses context ID; fresh child IDs do not automatically inherit parent plan files. Shared workspace effects remain possible.
- Selection predicate: exact sanitized ID filename; full Markdown content, no query ranking, importance selection or explicit length budget in this read.
- Invalidation or expiry: update/complete/clear rewrites steps and Markdown; clear removes completed steps; cleanup drops cached object/lock, not disk files.
- Activation or effect: supplies plan/result assertions as natural-language guidance with symbolic status markers, not executable obligation or correctness certification.
- Evidence limits: caller attribution/human control unresolved; file-write errors can be logged rather than propagated, and independent JSON/Markdown edits can diverge the two consumers.

Admission is model/caller-supplied content under software shape checks, with no independent oracle. A completed plan step is an asserted state, not evaluator-verified success. No automatic trace-to-plan learning mechanism is established by this route.

> todo_body = await todo_info.instance.content(ctx.id)
> --- `autogenesis/agent/types.py`

#### MEM-RTE-conversation-replay
Label: Conversation transcript replay
Part of: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task)

Owner/progression: Gateway records conversation events via ConversationManager; a later client requests conversation.list/events; resumeChat selects the latest chat conversation and requests its persisted events. Gateway filters by after_seq; no TieredMemory loader participates. SRC-1, `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`, `frontend/src/App.tsx`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: metadata or requested event list; append itself is best-effort file I/O.
- Later read-back: reopened/reconnected client receives persisted events after the sequence cursor; this is actual shipped caller wiring, not only a storage API.
- Delegated visibility: inapplicable — client transcript reopening does not create an agent child frame.
- Selection predicate: owner/project/conversation identity, view and updated-time ordering for choosing latest, then after_seq; chronological metadata selection, not task relevance.
- Invalidation or expiry: conversation delete removes metadata and transcript; malformed lines are skipped; this deletion does not clear same-ID resident TieredMemory or todo files in the inspected handler.
- Activation or effect: reconstructs client-visible history and preserves conversation identity for submissions; model recall after process restart does not follow from visual replay.
- Evidence limits: full frontend rendering and all reconnect branches were not traced; no supplied restart execution establishes history completeness or model dependence.

The separate chat append/load/delete handlers retain role/content by session ID and feedback records without a demonstrated automated update consumer. Their generic API caller does not establish human authorship, nor does feedback persistence establish learning.

> const replay = await socket.request('conversation.events', { session_id: sessionId, conversation_id: latest });
> --- `frontend/src/App.tsx`

#### MEM-RTE-corpus-retrieval
Label: Knowledge corpus ingestion and retrieval
Part of: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)

Owner/progression: caller/graph provides named base/documents and backend choice; knowledge_ingest normalizes and appends corpus records, updates backend manifest; later knowledge_retrieve loads that corpus and asks its selected ranker for top-k hits. Workflow KNOWLEDGE steps call the manager directly. This is retained external/user/model-supplied material, not intrinsically execution-trace memory. SRC-1, `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`, `autogenesis/workflow/runtime.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ingestion counts or retrieved records/scores in Response.data; the readable retrieval message reports counts, not full document bodies.
- Later read-back: later retrieval invocations reload disk corpus and deliver selected document fields to workflow result data; subsequent graph/model use depends on authored wiring, not automatic agent-memory injection.
- Delegated visibility: inapplicable — manager retrieval does not spawn a model child; a later graph agent step needs explicit payload mapping.
- Selection predicate: caller-selected base and query/task, manifest-selected bm25/tfidf, top_k integer at least one, default four; sparse ranking over text, no token budget or confidence threshold.
- Invalidation or expiry: ingestion appends, with no replacement/deduplication/delete operation in this manager; cleanup clears backends but preserves corpus. A changed manifest backend changes future ranking.
- Activation or effect: supplies knowledge candidates and scores to downstream workflow state; retrieval score is not truth, and actual model behavior depending on hits is unobserved.
- Evidence limits: initial document provenance is caller-dependent; empty/invalid or unavailable bases/backend errors return failures; no observed retrieval quality or deployed external vector store established.

Software admits document content after normalization/base/type checks; no per-document human approval, independent answer oracle, contradiction resolution or content-directed criticism gate is implemented here. Operating mode is caller-defined graph work, not a mandatory comparison curriculum. Raw strings/records can come from users, models or upstream data/process nodes; no source-native guarantee makes all documents experience-derived or vetted knowledge.

> results = [{**docs[index], "score": score} for index, score in hits if 0 <= index < len(docs)]
> --- `autogenesis/knowledge/server.py`

### Claims

#### MEM-CLM-memory-guidance
Label: Memory creation and evaluation guidance

Claimed operation: creator skill says a TieredMemory subclass changes which records enter the next prompt by overriding _render; evaluator prompt asks for an inspect-first scored evaluation and an in-process memory_eval_runner probe. Source layer is doctrine/design, not observation. SRC-1, `autogenesis/skill/creator/memory_creator_skill/SKILL.md`, `autogenesis/prompt/default/memory_evaluate_agent.html`. Closest supplied claim is [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance); this is a distinct, memory-specific method and interface conflict, not a second declaration of its general approval claim.

> def _render(self, state: _SessionState) -> str:
>     """Return the text injected into the agent's next prompt."""
>     return "\n".join(r.as_line() for r in state.recent)
> --- `autogenesis/skill/creator/memory_creator_skill/SKILL.md`

Counterevidence: TieredMemory.get builds its own selection; _render is called by persistence. The shipped constraint overrides therefore do not implement the prompt-retention change their descriptions suggest. The evaluator prompt also asks for `@ENVIRONMENT`, get_state/actions/lifecycle requirements, while the creator skill describes `@MEMORY_SYSTEM`, TieredMemory emit/get and retention/boundedness. Neither rubric is a code admission gate. Bounded searches for `inspect_memory_tool` and `memory_eval_runner` across autogenesis/configs found references in prompts/agent documentation/skill, not their implementations or configurations. This prevents assuming the named probes are callable in the frozen shipped configuration; dynamically supplied alternatives remain possible. The evaluator class itself just runs the base agent loop and returns a scored report, producing no registrable artifact. SRC-1, `autogenesis/memory/default/tiered.py`, `autogenesis/agent/evaluator/memory_evaluate_agent.py`.

> - `@ENVIRONMENT.register_module(force=True)` decorator present.
> --- `autogenesis/prompt/default/memory_evaluate_agent.html`

Theory account for the creator method: localized natural-language retention guidance and a long-run diagnostic test are supplied. Theory-builder conditions 1–4: condition 1 implementation conclusion status: wired (method text is localized); condition 2 operation conclusion status: uninspected (meaning-dependent model use not observed); condition 3 operation conclusion status: uninspected (no criticism episode with challenged claim/result/blame/revision supplied); condition 4 operation conclusion status: uninspected (repeat-until-good is prescribed, not an observed retained criticism shaping a next round). Addressability is section/rule/source-method level; no claim of individually enforced formal predicates. Persistence is shipped method across sessions plus admitted executable source/archive, not mandatory retained criticism. Learning as improved future capacity is unestablished. Reflection is afforded by inspecting and editing the system's own retention policy; representations can guide edits, but actual bidirectional exercised change is unobserved and the renderer/instance gaps limit the downstream path. Reflective theory builder and autonomous theory builder remain uninspected as exercised properties. Self-improvement attribution: boundary is Autogenesis retention machinery, horizon later rounds/tasks, objective preserving task-relevant early facts. Guidance proposes evidence-driven self-change, but no supplied episode establishes objective evidence shaping an installed working policy and subsequent behavior depending on it, much less benefit.

### Evidenced absences

#### MEM-ABS-tiered-reload
Label: Tiered session reload absent

- implementation conclusion status: absent

Bounded finding: no disk-to-session reload is implemented by inspected TieredMemory and its two built-in subclasses at SRC-1 `5b070d5cd497e951a188a01409138e8b530eaf4a`. Direct reads of all three files covered initialization, get, _get_or_create, persistence and eviction; inspection sought file reads/session reconstruction as counterexamples to resident-only recall. Constructor initializes an empty _sessions dict; get returns None on a miss; _get_or_create creates a blank state rather than reading persisted JSON/HTML. Thus a new built-in instance or evicted ID cannot recover its previous tiers through these methods. This is not an absence of all recovery in Autogenesis: todo reload, client transcript replay, external histories and workflow checkpoint resume are separately included. SRC-1, `autogenesis/memory/default/tiered.py`, `autogenesis/memory/default/general_memory_system.py`, `autogenesis/memory/default/file_system_memory.py`. No supplied absence counterpart; narrows the unestablished restart claim in [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task).

> self._sessions: Dict[str, _SessionState] = {}
> --- `autogenesis/memory/default/tiered.py`

> if state is None:
>     return None
> --- `autogenesis/memory/default/tiered.py`

### Behavioral-authority paths

#### MEM-BAP-memory-context
Label: Retained context authority

Consumer: foreground agent model on a later think call; for working summaries, also the compact model on a later overflow. Channel: memory_context template text from get and todo template text from content, not direct execution of the stored prose. Force: natural-language guidance with symbolic status/heading organization; delivery does not force compliance or verify truth. Horizon: subsequent calls sharing resident session state for tiers, and disk-readable same-ID todo plans across cache/process reconstruction. SRC-1, `autogenesis/agent/types.py`, `autogenesis/memory/default/tiered.py`, `autogenesis/tool/default/todo.py`. Distinct from [RT-BAP-method-instructions](runtime.md#rt-bap-method-instructions)'s static prompt/skill methods and [RT-BAP-capability-load](runtime.md#rt-bap-capability-load)'s executable machinery. [MEM-RTE-history-compaction](#mem-rte-history-compaction) supplies the load-bearing raw-to-derived-to-consumer passages.

## Annotations

#### On [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

Working-context control: code creates a fresh identity/context carrying selected task/files/explicit allowlists; child internal memory and raw transcript stay out of parent model context. Returned child message crosses back through action handling and can be compacted later. This resembles a frame with selected arguments and a return value, not isolated effects: shared workspace and registry changes escape too. Full child-context recovery is not supplied by delegation itself. Supplied record supports these limits; direct parent hook inspection adds that the returned action result is an input to [MEM-OBJ-recent-history](#mem-obj-recent-history), not an automatic copy of the child's retained state. SRC-1, `autogenesis/hook/default/memory.py`.

#### On [RT-OBJ-skill-content](runtime.md#rt-obj-skill-content)

Memory consumer distinction: registered skill body can be retrieved again from registry, whereas its returned action body survives later context only through the selected memory projection and potential compaction. Static file retention is not a trace-fed update. Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) establishes resource-path rewriting before return; this member's direct hook/tier inspection establishes the later text may be omitted or summarized rather than carried whole. SRC-1, `autogenesis/hook/default/memory.py`, `autogenesis/memory/default/tiered.py`.

#### On [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)

Checkpoint distinction: supplied route restores graph execution frames/completed invocation results under version/program-hash checks. The separate `/checkpoint` command writes a symbolic capability-type/name → version map with label/time in JSON; `/restore-checkpoint` calls each manager's restore when available and reports failures. It does not capture the agent's memory tiers or mailbox. The command's get_manager helper does not map the memory type, and MemoryManagerServer does not expose restore although MemoryContextManager does. A capability-version map therefore does not restore a memory component or its session through this command. SRC-1, `autogenesis/command/default/checkpoint.py`, `autogenesis/command/default/restore_checkpoint.py`, `autogenesis/command/default/_helpers.py`, `autogenesis/memory/server.py`, `autogenesis/memory/context.py`.

> snapshot[f"{ctype}/{n}"] = await version_manager.get_current_version(ctype, n)
> --- `autogenesis/command/default/checkpoint.py`

> if mgr is None or not hasattr(mgr, "restore"):
>     failed.append(key)
>     continue
> --- `autogenesis/command/default/restore_checkpoint.py`

## Write side

[MEM-RTE-tiered-context](#mem-rte-tiered-context) admits lifecycle observations automatically and projects them into history, display todos/flow and result. Acquisition is not independent verification: external tool assertions, child return text, errors and model outputs share the projection. Explicit metadata snapshots can replace displayed structure; todo descriptions can be model-shortened. Those automatic display transformations do not imply that the model receives that shortened todo text, since get omits display todos. Separate todo_tool writes supply the plan actually injected into agent context.

[MEM-RTE-history-compaction](#mem-rte-history-compaction) traces the automatic raw projection → model summary → stored working chunk → later get/model consumer chain. Successful summarization removes raw source chunks; nonempty text is admitted without a fidelity evaluator. Empty summaries restore raw records, and summary deque expiry discards older chunks. A raw event log or training trajectory can coexist but is not automatically consulted to recover the lost detail. Fixed input/output count limits leave a potentially large text budget. No mechanism here guarantees retaining reasons for behavior-shaping claims; the prior summary and whatever reasons survive in the new text are the later summarizer's available context.

[MEM-RTE-memory-admission](#mem-rte-memory-admission) changes executable retention machinery through software promotion/registration, separately from session-content writes. Frozen-target checks, optional generic smoke and archives can reject/recover source changes, not prove retention quality or migrate live tiers. The instance-null countercase prevents assuming current registration always yields a live memory reader. Instance registration and startup build are real alternatives, so this is a path-specific gap rather than a system-wide inability to use memory.

[MEM-RTE-corpus-retrieval](#mem-rte-corpus-retrieval) admits normalized documents by append and backend checks, without a truth/contradiction gate; content origin is caller-dependent. Conversation and training artifacts preserve records through software I/O, while feedback/reward fields are evaluative metadata, not self-executing learning. Dataset save/load affords a separate corpus transfer in workflow data nodes; inspected code uses dataset identifiers/splits and returns whole records, not a configured automatic training loop (SRC-1, `autogenesis/data/server.py`, `autogenesis/workflow/runtime.py`).

Withdrawal is mechanism-specific: raw-history replacement, summary eviction, LRU session eviction, plan clear, conversation deletion, component unload/rollback, and workflow restore checks are different operations. Conversation deletion does not cascade to resident memory in the inspected handler. Memory-manager cleanup clears config/history dictionaries, without an implemented TieredMemory flush/rehydration protocol there. No global erasure guarantee follows.

## Read-back

The ordinary read is agent-requested get by identity, followed by code-selected text delivery, not unsolicited independently chosen memory injection. The overflow trigger independently invokes a summarizer, but the retained result reaches the foreground agent only through a later context build. Count windows exclude older records/chunks; no source trust filter separates facts from instructions before consumption. [MEM-BAP-memory-context](#mem-bap-memory-context) states the actual force: guidance to a model, not guaranteed action.

Todo reinjection is a separate automatic supply point during context construction, including when tiered memory is disabled. Full Markdown is read by filename, not searched by current task. Child contexts keep parent internal history out and return a selected result; dropping the frame does not erase shared side effects. Skill bodies can be rerequested independently of whether their prior action result survives the tail/summary budget.

Client replay reloads persisted events to a real shipped caller but is not model-context rehydration. Corpus retrieval is caller-requested query targeting and top-k selection; its retained document bodies occur in Response.data, while the message is only a count summary. The workflow graph must route that data to any subsequent model consumer. Dataset and trajectory exports establish storage/transfer/export capabilities; unknown external training callers do not establish a later trained-model route. Astra plugin get similarly returns records via an adapter, with deployment/storage internals unresolved; Mem0 is a labeled stub rather than operational memory retrieval in the inspected adapter.

## Integration issues

1. **Memory-specific correction to generic live registration.** [MEM-RTE-memory-admission](#mem-rte-memory-admission) qualifies [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission) and [RT-BAP-capability-load](runtime.md#rt-bap-capability-load): loading a memory class through extension registration leaves active MemoryConfig.instance null. Import/constructor effects and archive admission still occur, but later memory-hook/get consumers skip the instance. A subsequent build is required; no such call was found on inspected add/load paths. Other capability modules are not implicated by this finding.
2. **Renderer contract conflict.** [MEM-CLM-memory-guidance](#mem-clm-memory-guidance), [MEM-OBJ-memory-display](#mem-obj-memory-display) and [MEM-RTE-tiered-context](#mem-rte-tiered-context) establish that creator guidance and sample constraint renderers modify persisted views, not inherited get selection. Prevented conclusion: source renderer changes alone improve next-prompt retention. This is a correction to source-native guidance, not a duplicate of runtime's general evolution claim.
3. **Evaluator reliability/callability unresolved.** Memory evaluator prompt and creator skill demand incompatible interfaces; named inspection/probe tool implementations/configuration were not located by the bounded searches stated in [MEM-CLM-memory-guidance](#mem-clm-memory-guidance). Neither the score report nor generic smoke proves useful memory retention. A runtime-generated tool could alter availability; none was supplied as execution evidence.
4. **Restart and deletion scopes differ.** [MEM-ABS-tiered-reload](#mem-abs-tiered-reload) establishes a bounded built-in reload absence, while [MEM-RTE-conversation-replay](#mem-rte-conversation-replay), [MEM-RTE-todo-context](#mem-rte-todo-context) and the workflow annotation preserve real positive reload paths. Client history persistence must not be merged into a universal model-memory recovery claim. Conversation deletion has no demonstrated cascade into resident tiers/plans.
5. **Record identity comparison.** Route parts explicitly name their supplied containers; none proposes replacing a supplied record. New objects distinguish per-session retained content from [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest), registry skill content, and provider parameters. No unresolved possible duplicate remains after those referent comparisons. Corpus workflow part and generic workflow route overlap by containment, not identity.
6. **Open coverage limits.** Provider histories, trace-writer internals, downstream trajectory training consumers, all process transforms, full frontend replay/rendering and arbitrary workspace recall remain unresolved at the scope stated in the coverage table. They prevent global claims about learning, retention completeness, provider state and all recall channels; they do not negate the implemented compaction and disk reread routes. No supplied run demonstrates beneficial behavior change from any of these retained artifacts.

## Limitations and checks

Source HEAD matched the boundary revision and tracked working-tree diff was empty on initial inspection. New source paths remain under SRC-1 at that revision; no new source identity or evidence layer was introduced. Invocation, report type, boundary/runtime types, collection, worker rules and full record contract were read; this report applies those supplied method inputs, not a different authoring workflow. Analysis is static: no target tests, examples, provider calls or service executions were performed. External model/SDK/storage behavior and source-native claimed operation remain bounded by the source register.

Validation: the required validate-output command passed (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Deterministic validation establishes format and quotation occurrence, not semantic acceptance, observed operation or benefit.
