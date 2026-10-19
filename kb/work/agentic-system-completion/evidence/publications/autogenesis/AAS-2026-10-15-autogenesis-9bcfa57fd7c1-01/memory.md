---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Autogenesis memory: trace-derived tiers, independent todo reload, corpus ranking, transcript replay and capability recovery."
run-id: AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01
source-identity: https://github.com/DVampire/Autogenesis
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis memory report

## Boundary and evidence

This report covers retained context and recovery within the whole-system boundary in [boundary.md](boundary.md). SRC-1 is the sole source, at commit `5b070d5cd497e951a188a01409138e8b530eaf4a`. Direct reads below are implementation evidence, except source docstrings and declared instructions, which establish intent. Runtime records supply executable extension and workflow recovery evidence; they are not run observations. No target, test, example, model or service was executed.

Memory scope includes event-fed agent tiers, their JSON/HTML projections, the separate todo tool, child-context isolation, knowledge corpora and both built-in rankers, conversation/client replay, diagnostic traces/trajectories, workflow evaluation evidence, and both workflow and capability-version checkpoints. Reusable extension code and static skill/prompt delivery remain included through runtime records rather than duplicate declarations. Provider internals and external Gitlinks remain excluded as in the boundary; neither remote retention nor numerical parameter learning can be established here.

| Entry or operation | Source paths (SRC-1) | Coverage and limits |
|---|---|---|
| CLI control commands and Gateway/direct agent calls | `autogenesis/cli.py`, `autogenesis/agent/types.py`, `autogenesis/gateway/service.py` | Direct scoped reads/searches; [MEM-RTE-tier-context](#mem-rte-tier-context), [MEM-RTE-version-recovery](#mem-rte-version-recovery); supplied [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). |
| Hook ingestion; explicit legacy snapshots; compaction; LRU and disk rendering | `autogenesis/hook/default/memory.py`, `autogenesis/hook/default/compact.py`, `autogenesis/memory/default/tiered.py`, `autogenesis/memory/default/general_memory_system.py`, `autogenesis/memory/default/file_system_memory.py` | Direct reads; [MEM-OBJ-recent-history](#mem-obj-recent-history), [MEM-OBJ-working-memory](#mem-obj-working-memory), [MEM-OBJ-memory-display](#mem-obj-memory-display). |
| Alternative extension renderers | `extension/memory/constraint_memory.py`, `extension/memory/file_system_memory.py` | Constraint renderer read; file-system extension searched, boundary supplied renderer findings. Detailed parity of extension HTML with built-in HTML not established. Keyword-based constraint display is not verified-constraint admission. |
| Registered memory library operations | `autogenesis/memory/server.py`, `autogenesis/memory/context.py`, `autogenesis/memory/types.py` | Server read; context initialization, get/build/restore/cleanup and session wrappers read. Legacy wrappers call methods not supplied by inspected TieredMemory/base Memory; names alone do not establish working clear/get-insight APIs on those classes. |
| Separate todo writes and disk read-back | `autogenesis/tool/default/todo.py`, `autogenesis/agent/types.py` | Direct selected reads; [MEM-RTE-todo-context](#mem-rte-todo-context). Full export and completion implementation not audited; no atomic multi-file guarantee. |
| Child isolation; selected skill bodies | `autogenesis/protocol/server.py`, `autogenesis/skill/context.py` | Supplied [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation), [RT-RTE-skill-instructions](runtime.md#rt-rte-skill-instructions); memory consequences annotated below. |
| Knowledge writes, retrieval and workflow result normalization | `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`, `autogenesis/workflow/runtime.py` | Direct reads; [MEM-OBJ-corpus](#mem-obj-corpus), annotation on [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission). Arbitrary custom backends remain uninspected, not absent. |
| Conversation/session replay; separate chat feedback | `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`, `frontend/src/science/Conversation.tsx`, `frontend/src/canvas/PlaygroundPanel.tsx` | Direct selected reads; [MEM-RTE-client-replay](#mem-rte-client-replay). Full chat-controller and transport implementation not inspected; no universal replay-to-model claim. |
| Trace, prompt snapshot and trajectory export | `autogenesis/trace/writer.py`, `autogenesis/hook/default/snapshot_hook.py`, `autogenesis/trajectory/server.py` | Direct selected reads; [MEM-OBJ-run-records](#mem-obj-run-records). Scoped symbol search in `autogenesis`, `examples`, `configs` found trajectory lifecycle wiring and export/reward APIs, not a training consumer; this bounds rather than proves absence of training elsewhere. |
| Workflow evaluations, withdrawal, resume | `autogenesis/workflow/context.py`, `autogenesis/workflow/server.py`, `autogenesis/tool/default/evolution.py` | Direct reads/searches; [MEM-RTE-evaluation-records](#mem-rte-evaluation-records). Checkpoint execution supplied by [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution). Full canvas compiler/library save and science/kernel state mechanisms remain uninspected; no conclusions about all user-authored workflow or notebook persistence. |
| Memory generation/evaluation and shared capability recovery | `autogenesis/hook/default/memory_registration.py`, `autogenesis/agent/evaluator/memory_evaluate_agent.py`, `autogenesis/command/default/checkpoint.py`, `autogenesis/command/default/restore_checkpoint.py` | Direct reads; [MEM-RTE-memory-admission](#mem-rte-memory-admission), [MEM-RTE-version-recovery](#mem-rte-version-recovery); generic extension lifecycle supplied by runtime. Generator/optimizer prompt content and inspection-tool internals not traced; no conclusion about quality of their proposals or evaluations. |

## Core ideas

1. **The model-visible memory is not the persisted report.** TieredMemory selects working summaries, recent records and an optional final result from its in-process registry. JSON also stores todos and flow steps; HTML renders them, but `get()` does not inject them. A separate todo tool really does reread Markdown each turn. Persistence therefore has different restart horizons at different consumers. [MEM-RTE-tier-context](#mem-rte-tier-context), [MEM-RTE-todo-context](#mem-rte-todo-context).
2. **Compaction changes future context, not just disk size.** Code selects oldest records; a separate model produces short summaries; later model turns receive a bounded tail of those summaries. This is an automatic trace-fed derived-memory write with a wired consumer, but not demonstrated improved capacity. Empty summaries restore the popped chunk; exceptions after popping have only a logging branch, so the source's lossless comment is not a universal guarantee. [MEM-OBJ-working-memory](#mem-obj-working-memory), [MEM-RTE-tier-context](#mem-rte-tier-context).
3. **Source trust is mostly lineage, not truth admission.** Action outputs, failures and summaries become context without a semantic verification gate. The constraint extension's “Confirmed constraints” heading follows keyword matching and only changes rendering. Corpus ingest normalizes supplied documents; its “semantic search” label covers built-in lexical/statistical rankers, not a shipped neural embedding service. [MEM-OBJ-memory-display](#mem-obj-memory-display), [MEM-OBJ-corpus](#mem-obj-corpus).
4. **Recovery and evaluation have several distinct products.** Workflow checkpoints control reuse of completed invocations; version checkpoints select capability versions; evaluation JSON supplies version-filtered metrics and a health signal. None is interchangeable with the agent's history or an independent correctness oracle. [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint), [MEM-OBJ-version-snapshot](#mem-obj-version-snapshot), [MEM-OBJ-workflow-evaluations](#mem-obj-workflow-evaluations).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-recent-history
Label: TieredMemory recent records

Source-native identity: `_SessionState.recent`, a deque of `MemoryRecord` objects. Symbolic event/time/status fields wrap natural-language detail text; substrate is RAM, plus JSON in GeneralMemorySystem. This is a selected event projection, not a complete raw model transcript: start task, action result/error and agent end become records; POST_STEP reasoning instead supplies shortened display labels. The hook uses `ctx.id`, and sends events to the primary memory and the file-system secondary sink. No counterpart is declared in supplied runtime: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) names its consumer, not this store. SRC-1: `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/memory.py`.

> detail = event.error if not ok else _as_text(event.message)
> --- `autogenesis/memory/default/tiered.py`

The hook validates its envelope, skips disabled memory, swallows sink failures and always allows continuation. ON_STOP derives success from the error field, not the optional supplied success value; this limits interpretation of stored lifecycle status. No semantic truth veto or human per-record approval is implemented in this hook. The retained raw projection can feed compaction and later prompts; complete action arguments/reasoning belong to other records, not necessarily this deque.

#### MEM-OBJ-working-memory
Label: Compacted execution summaries

Source-native identity: `_SessionState.working`, bounded natural-language summary strings in a RAM deque and rendered JSON/HTML. Derived from recent-record lines through CompactHook, with the last working summary supplied as prior context. Default retention is ten summaries; default prompt selection is five. The newest summary is not required to contain all prior summaries: the instruction explicitly avoids repeating the existing summary. Lineage is mixed user task, model actions and tool/service/child outputs selected by the hook. Summary reasons and provenance are not guaranteed to survive the prose reduction. Distinct from [RT-OBJ-self-evolving](runtime.md#rt-obj-self-evolving), a static method, and [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint), executable recovery state. SRC-1: `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py`.

> "Summarise the records above in 2-4 sentences. Focus on what agents ran, "
> "what tools/skills were called, key results, and any failures. Preserve exact "
> "values (file paths, numbers, errors). Do not repeat the existing summary."
> --- `autogenesis/hook/default/compact.py`

This is requested preservation, not verified fidelity. Numerical generation is supplied by [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager); no local weight update follows from summary production.

#### MEM-OBJ-memory-display
Label: Persisted memory projections and constraint display

Source-native identity: GeneralMemorySystem JSON and FileSystemMemory HTML rendered from `_SessionState`, including task, todos, flow, tiers and result. Their symbolic layout/status metadata and natural-language content have different consumers: JSON preserves current record fields; HTML is an escaped human-readable display whose recent history is itself limited to `recent_fetch`. Neither is an opaque executable checkpoint. No supplied record declares these projections; [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint) is a separate persistence mechanism. SRC-1: `autogenesis/memory/default/general_memory_system.py`, `autogenesis/memory/default/file_system_memory.py`.

> recent = list(state.recent)[-self.recent_fetch:]
> --- `autogenesis/memory/default/file_system_memory.py`

Explicit todo snapshots can have long descriptions model-summarized to at most 80 characters; flow labels are truncated. These are display transformations: TieredMemory `get()` includes neither todos nor flow. The included ConstraintMemory extension only overrides rendering, classifying current recent records by keywords; it does not add a protected constraints store or override inherited prompt selection. SRC-1: `autogenesis/memory/default/tiered.py`, `extension/memory/constraint_memory.py`.

> if "constraint" in text or "established" in text or "verified fact" in text:
>     constraints.append(r.as_line())
> --- `extension/memory/constraint_memory.py`

“Confirmed” therefore names a display bucket, not an evidential status. Compaction can still remove those recent records.

#### MEM-OBJ-todo-tool
Label: Separate persisted todo plan

Source-native identity: TodoTool per-ID `steps.json` and `todo.md`, under its configured base directory (default workspace root plus `todo_tool`). Symbolic Step IDs/status/priority/parameters are serialized to JSON; task and result text becomes Markdown guidance. The model or another caller authors edits via actions; code validates and persists them. Disk content is consumed directly by Agent context assembly, independently of the tiered-memory todos. Closest supplied [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) is the containing task path, not an object duplicate. SRC-1: `autogenesis/tool/default/todo.py`, `autogenesis/agent/types.py`.

> async def content(self, id: str) -> str:
> --- `autogenesis/tool/default/todo.py`

> return Todo.read_content(self._file_path(id, "todo.md"))
> --- `autogenesis/tool/default/todo.py`

JSON provides cache reconstruction; Markdown supplies model-visible content. External file editing can make the two disagree; no synchronization invariant across arbitrary edits is established.

#### MEM-OBJ-corpus
Label: Named knowledge corpus and backend manifest

Source-native identity: KnowledgeManager `corpus.jsonl` documents and `manifest.json` backend type. Natural-language `text` is retained with arbitrary symbolic metadata; both are disk-backed and reloaded on retrieval. Manifest type is access/selection metadata, not document content. Part of the supplied route, not a duplicate corpus declaration:

Part of: [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)

The parent route produces and reads this store; this record separates its operative parts. Ingest takes caller documents or upstream `data.records`, appends normalized records and replaces the backend type for the whole base. Initial authorship and truth provenance remain caller-dependent. Built-in BM25 lowercases and splits whitespace, constructs BM25Okapi for the supplied corpus and sorts scores. TF-IDF fits corpus vectors per search and compares query cosine similarity. These are numerical statistical intermediates over explicit vocabulary, not inspected learned dense neural embeddings or weight training. No persistent embedding index is written by these rankers. The external packages' implementation/version behavior remains outside the inspected source. SRC-1: `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`.

> tokenized = [str(text).lower().split() for text in texts]
> bm25 = BM25Okapi(tokenized)
> scores = bm25.get_scores(str(query).lower().split())
> --- `autogenesis/knowledge/default/rankers.py`

> matrix = vectorizer.fit_transform([str(text) for text in texts])
> query_vector = vectorizer.transform([str(query)])
> --- `autogenesis/knowledge/default/rankers.py`

#### MEM-OBJ-run-records
Label: Diagnostic transcripts and trajectory products

Source-native identities: ConversationManager event JSONL, Gateway's separate chat/feedback JSONL, TraceWriter session JSONL/index, SnapshotHook per-step prompt HTML, and TrajectoryManager task JSONL. These share observational writing rather than admission to an executable policy, but have distinct payloads and consumers. No supplied runtime object declares these stores; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) establishes lifecycle producers. SRC-1: `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`, `autogenesis/trace/writer.py`, `autogenesis/hook/default/snapshot_hook.py`, `autogenesis/trajectory/server.py`.

Conversation and chat text are natural language with symbolic IDs/roles/events. Trace payloads are serialized event records, not necessarily complete trajectories. Prompt snapshots retain rendered messages for display. Trajectories additionally preserve messages sent, reasoning, action plans, observations, token use, outcome and optional reward; SFT/RL export produces structured data, not an implemented trainer. Trace index, conversation metadata and trajectory header are access/lineage metadata, not substitutes for retained content. Their later readers differ: client replay is wired below, TraceWriter offers disk read helpers, and trajectory get/export uses the in-process registry. APIs without an inspected caller establish capabilities only.

> step.messages_sent = inp.get("messages") or []
> step.reasoning = inp.get("reasoning") or ""
> step.actions = inp.get("plan") or []
> --- `autogenesis/trajectory/server.py`

Reward backfill mutates retained trajectories and re-persists; the scoped symbol search reported above did not establish a driver calling it or a subsequent training/model-input consumer. Gateway feedback likewise writes `feedback.jsonl`; a learning consumer of that file remains uninspected. No learned behavioral update is inferred from these products.

#### MEM-OBJ-conversation-events
Label: Conversation event transcript

Part of: [MEM-OBJ-run-records](#mem-obj-run-records)

Source-native identity: ConversationManager conversation metadata JSON and event JSONL. Symbolic event IDs, sequence numbers and task associations accompany natural-language payloads. Gateway observational append is automatic, guarded by session/conversation presence, and does not judge content truth. Metadata is an access aid, not the dialogue itself. The disk event reader returns oldest-first valid lines to the concrete science-pane replay consumer in [MEM-RTE-client-replay](#mem-rte-client-replay). Deleting a conversation removes its metadata and transcript; it does not erase other stores. This is a material part of the diagnostic container, not the Agent's registry. SRC-1: `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`, `frontend/src/science/Conversation.tsx`.

> for path in (meta, events):
>     if path.is_file():
>         path.unlink()
> --- `autogenesis/conversation/server.py`

#### MEM-OBJ-chat-records
Label: Separate chat text and feedback files

Part of: [MEM-OBJ-run-records](#mem-obj-run-records)

Source-native identity: Gateway chat.jsonl, meta.json and feedback.jsonl. Caller-submitted user/assistant text is natural language; role, message ID, feedback value and timestamps are symbolic metadata. chat.append validates role and appends, while chat.feedback records caller values without an inspected truth or learning gate. Initial human versus computational authorship remains unresolved by caller identity. Playground reads chat text for display; no downstream reader of feedback was established by these handler reads. Directory deletion removes these files, not all session memory. SRC-1: `autogenesis/gateway/service.py`, `frontend/src/canvas/PlaygroundPanel.tsx`.

> if role not in ("user", "assistant"):
>     raise ValueError("role must be 'user' or 'assistant'")
> --- `autogenesis/gateway/service.py`

#### MEM-OBJ-trace-events
Label: TraceWriter events and session index

Part of: [MEM-OBJ-run-records](#mem-obj-run-records)

Source-native identity: TraceWriter session JSONL and index.json. Serialized symbolic event structure carries natural-language payloads; the index records paths/counts rather than replacing event content. Automatic event logging admits observation payloads without semantic curation. read_session rereads disk and skips malformed JSON; no model reinjection caller was traced for that helper. Index replacement does not replace append-only event files. No deletion/expiry policy was established from the inspected writer sections. SRC-1: `autogenesis/trace/writer.py`.

> events.append(json.loads(line))
> --- `autogenesis/trace/writer.py`

#### MEM-OBJ-message-snapshots
Label: Rendered per-step prompt snapshots

Part of: [MEM-OBJ-run-records](#mem-obj-run-records)

Source-native identity: SnapshotHook numbered HTML files under messages/agent-name. Natural-language rendered prompt content is wrapped in symbolic display markup. POST_STEP automatically writes available messages; I/O errors are swallowed, with no per-content approval or quality gate. Agent-name/step-number targeting is not relevance retrieval, and the same output path can be overwritten by later matching writes. An inspectable display file is retained; an automatic later model reload is not established. SRC-1: `autogenesis/hook/default/snapshot_hook.py`.

> file_path = os.path.join(out_dir, f"{step_number + 1:04d}.html")
> --- `autogenesis/hook/default/snapshot_hook.py`

#### MEM-OBJ-trajectories
Label: Task trajectory and reward export

Part of: [MEM-OBJ-run-records](#mem-obj-run-records)

Source-native identity: TrajectoryManager task-keyed RAM objects and task JSONL. Symbolic step/action/token/reward fields retain natural-language messages, reasoning and result strings. Lifecycle code builds observations and decisions; finalization writes a header and steps. Reward backfill rewrites the product, but is not itself model training. get/export_sft/export_rl consume the RAM mapping; no disk loader or concrete trainer caller is established by this class and the scoped symbol search. Version/payload provenance is whatever lifecycle producers supply, not an independently authenticated experiment. SRC-1: `autogenesis/trajectory/server.py`.

> traj.backfill_reward(reward)
> self._persist(traj)
> --- `autogenesis/trajectory/server.py:148-149`

#### MEM-OBJ-workflow-evaluations
Label: Version-scoped workflow evaluation evidence

Source-native identity: WorkflowContextManager `_evaluations` and persisted `evaluations.json`. Symbolic records contain workflow/version/run/case identities, success, quality, costs and timestamps, with optional natural-language notes. They are derived evidence, not workflow program state. Distinct from [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint); the run is a validation input, not the same artifact. SRC-1: `autogenesis/workflow/context.py`, `autogenesis/tool/default/evolution.py`.

> if evaluation.workflow_version != definition.version:
>     raise ValueError("Evaluation version does not match the registered workflow")
> --- `autogenesis/workflow/context.py`

Successful records require a retained terminal run with matching name/version/program hash and success state; costs are taken from that run. Static failures can be admitted with case IDs. Quality and notes are supplied by the caller, not independently proven by these checks. Persisted evidence reloads on context initialization; summaries filter to the currently registered version.

#### MEM-OBJ-version-snapshot
Label: Capability version restore-point map

Source-native identity: `/checkpoint` JSON `{label, created_at, snapshot}` under log-root `command/checkpoints`. Symbolic component-type/name to current-version map, generated from VersionManager and later read by `/restore-checkpoint`. This is distinct from active extension manifest/archive [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest) and workflow run [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint). It stores pointers to versions, not capability source, agent conversation, execution trace, reasons for a change or all external effects. SRC-1: `autogenesis/command/default/checkpoint.py`, `autogenesis/command/default/restore_checkpoint.py`.

> snapshot[f"{ctype}/{n}"] = await version_manager.get_current_version(ctype, n)
> --- `autogenesis/command/default/checkpoint.py`

### Routes

#### MEM-RTE-tier-context
Label: Event compaction and later agent context

Endpoints: agent lifecycle/action hook → primary and secondary TieredMemory → recent/working state → Agent context assembly → later model invocation. Code selects events and age-based chunks; CompactHook's separate model produces derived prose; the foreground model interprets the delivered context. This refines the memory leg of the supplied task route:

Part of: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook allow result; memory get returns Markdown or None, not a complete event transcript.
- Later read-back: each later Agent context request selects the same context-ID registry entry, working tail and recent tail, plus final result when set; delivered through memory_context in rendered model input.
- Delegated visibility: child history is separately addressed; parent receives child result text as an action result rather than all child events.
- Selection predicate: use_memory plus named configured instance and ctx.id; recent overflow above 30 defaults schedules oldest-ten compaction; working deque max ten, get tail five; Agent review_steps overrides default recent_fetch ten. short_term_n zero selects all current recent records, not an empty budget. Counts, not token ceilings, govern these selections.
- Invalidation or expiry: summary maxlen drops oldest summaries; selected raw records leave recent on nonempty summary; LRU eviction beyond default 256 sessions flushes then removes registry entries. get does not reload the file; later emit recreates state if absent.
- Activation or effect: automatic summary output changes material available to later model turns; behavioral dependence, truth preservation and beneficial decisions remain unobserved.
- Evidence limits: no run evidence; async compaction/persistence is best effort, not a transactional/lossless guarantee, and JSON/HTML persistence is not restart prompt restoration.

SRC-1: `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/memory.py`, `autogenesis/hook/default/compact.py`, `autogenesis/agent/types.py`.

> chunk = [state.recent.popleft() for _ in range(k)]
> --- `autogenesis/memory/default/tiered.py`

> text = await self._summarise(items, existing)
> if text:
>     state.working.append(text)
> --- `autogenesis/memory/default/tiered.py`

> state = self._sessions.get(session_id)
> --- `autogenesis/memory/default/tiered.py`

Admission: software admits typed event projections and nonempty compact-hook text without a truth oracle, human per-content decision, or quality comparison. Model authors summary prose; code decides its insertion. Empty output restores the chunk; exception handling logs rather than universally restoring it. Direct todo/flow/final-result snapshots through AGENT_CALL metadata are alternate writes, not proof that a human approved content. Guidance requests exact values and failures in 2–4 sentences; resulting prose and surviving raw records persist, not guaranteed complete reasons. Operating mode is automatic context maintenance during open tasks, not an improvement experiment. See [MEM-OBJ-working-memory](#mem-obj-working-memory).

#### MEM-RTE-todo-context
Label: Todo edits and automatic prompt reread

Endpoints: model/tool caller → TodoTool action → steps JSON and Markdown → Agent._get_agent_context → later model. Distinct sibling of tier context: this store is not TieredMemory.todos. Closest supplied [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) supplies invocation context and prompt consumption, not the detailed file route. SRC-1: `autogenesis/tool/default/todo.py`, `autogenesis/agent/types.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: action Response with message/data or failure; content(ctx.id) returns Markdown directly.
- Later read-back: subsequent context assembly automatically calls todo_tool.content(ctx.id), even outside the use_memory branch; a new Todo cache can reconstruct Step objects from steps.json.
- Delegated visibility: IDs scope separate todo files; no automatic copying of parent plans is established.
- Selection predicate: tool capability/caller action, valid required fields/IDs, then per-context filename; whole Markdown read, not query-targeted retrieval or a token-bounded excerpt.
- Invalidation or expiry: add/update/complete replace state and regenerate files; clear removes completed items through its action; cleanup drops cache/locks, not the disk files. Direct external edits can alter prompt input.
- Activation or effect: retained plans/results are delivered as interpreted guidance on later turns, not enforced executables or proof of correct completion.
- Evidence limits: no run or file consistency experiment; per-file locking is not atomic JSON-plus-Markdown persistence.

> todo_body = await todo_info.instance.content(ctx.id)
> --- `autogenesis/agent/types.py`

Admission roles: caller, often foreground model, proposes plan/status/result; software checks action/arguments and performs writes. Human per-item approval is unresolved and not tested here. Invalid actions/arguments fail; no truth or independent answer oracle. Open task planning, not autonomous quality scoring. Persisted content is task/parameters/results, with whatever reasons the caller actually includes. Recovery uses cached state or disk reconstruction, not an automatic prior-version rollback.

#### MEM-RTE-client-replay
Label: Persistent dialogue replay to clients

Endpoints: Gateway/ConversationManager append or chat.append → disk JSONL/metadata → conversation.events or chat.session.load → frontend display. Closest supplied [RT-RTE-model-playground](runtime.md#rt-rte-model-playground) is model streaming, not this display route; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) supplies task events. SRC-1: `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`, `frontend/src/science/Conversation.tsx`, `frontend/src/canvas/PlaygroundPanel.tsx`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: append acknowledgement, conversation metadata or arrays of persisted events/messages.
- Later read-back: science conversation pane chooses latest science conversation and requests its events; Playground mount selects newest chat record and loads its messages into flow display state; explicit switching can select another record.
- Delegated visibility: client gets transcript events/messages, not reconstructed Agent run frames or all child windows.
- Selection predicate: owner/session/conversation identity, view for science, newest-first metadata lists and explicit ID loads; no semantic relevance selector. Server conversation events can filter by sequence; no model token budget is enforced by display loading.
- Invalidation or expiry: conversation delete removes its metadata and transcript; chat.session.delete removes its record directory. Corrupt transcript lines are skipped. These deletions do not establish deletion of tier memory, todo files, traces or external effects.
- Activation or effect: retained dialogue populates UI state; replay alone does not inject it into Agent memory or resume old running tasks.
- Evidence limits: full frontend send paths and remote client behavior are not traced here; no universal statement that displayed history is or is not sent in later model requests.

> const replay = await request('conversation.events', { session_id: sessionId, conversation_id: latest });
> --- `frontend/src/science/Conversation.tsx`

> setFlowMessages(messages.map((message) => ({ role: message.role === 'user' ? 'user' : 'assistant', content: String(message.content ?? '') })));
> --- `frontend/src/canvas/PlaygroundPanel.tsx`

Admission is append/serialization by code, or caller role validation for chat.append, not a truth gate. User and assistant text are producer labels; arbitrary caller identity does not establish human per-content curation. Recovery rebuilds sessions from manifests, migrates legacy events and seeds sequence counters from transcript disk state. The model-memory registry remains a different consumer. Feedback writes retain ratings but no learning consumer is established by these handlers.

#### MEM-RTE-evaluation-records
Label: Workflow evaluation admission and summary

Endpoints: caller/evolution_tool → WorkflowContextManager.record_evaluation → RAM and evaluations.json → current-version summary/getter and evolution_tool Response. Different product from supplied [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution), whose run is checked as evidence. SRC-1: `autogenesis/tool/default/evolution.py`, `autogenesis/workflow/context.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored normalized evaluation plus aggregate summary through evolution_tool.
- Later read-back: context initialization reloads evaluations.json; evaluations(name) filters current version; subsequent summary calls compute distinct cases, success rate and mean quality.
- Delegated visibility: caller receives structured evaluation/summary and message; a foreground Agent can retain its action message, but no automatic whole-ledger injection is established.
- Selection predicate: matching registered version; run-backed evidence must match name/version/hash, terminality and success and not duplicate a run; static unsuccessful evidence needs case_id. Healthy requires at least three distinct cases, success rate at least 0.8 and average quality at least 0.7.
- Invalidation or expiry: old-version records remain stored but are filtered out; restoring an old version can make its records visible again. Corrupt optional evidence reload resets the in-memory evaluations mapping; no evidence rollback route is established.
- Activation or effect: symbolic summary signal is delivered; no automatic promotion/rollback follows from the inspected summary function.
- Evidence limits: caller quality_score/notes are not an independent answer oracle; no observed evaluations or actual keep/rollback decisions were supplied.

> "healthy": len(distinct_cases) >= 3 and success_rate >= 0.8 and quality >= 0.7,
> --- `autogenesis/workflow/context.py`

Admission is computational validation of identity and recorded lifecycle results, not human approval or adjudication of correctness. Caller proposes evaluation; software can reject mismatches, missing/duplicate/nonterminal runs and unsupported successful static evidence. Open explicit evaluations or requested comparisons can use this API; no fixed curriculum is enforced. Guidance is the evidence schema/health policy; retained notes may contain reasons but are optional, and summary does not interpret those reasons. Atomic temp-file replace protects an individual ledger write, not all related files. This adds a bounded numerical health signal without contradicting the runtime's narrower finding that generated-tool admission has no enforced evaluator-quality threshold.

#### MEM-RTE-version-recovery
Label: Capability restore-point write and replay

Endpoints: CLI/Gateway command dispatch → /checkpoint current-version map → JSON → /restore-checkpoint → individual manager.restore calls. Distinct from [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)'s extension-archive rollback and [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)'s invocation checkpoint resume. SRC-1: `autogenesis/cli.py`, `autogenesis/command/default/checkpoint.py`, `autogenesis/command/default/restore_checkpoint.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: checkpoint path/map, or restored count and failures; partial restore can still return command ok.
- Later read-back: caller-selected label loads snapshot and attempts each recorded version through its owning manager; later dispatch depends on successfully restored registrations.
- Delegated visibility: no conversation/frame restored; only versions resolved through managers cross this recovery boundary.
- Selection predicate: supplied label and component/version map, skipping empty versions; manager availability and restore capability determine success. No relevance or token selector.
- Invalidation or expiry: a checkpoint file can be replaced by the same label; missing file fails; individual missing manager/history/version or exceptions produce reported failures. The map itself does not ensure cross-restart availability of every manager's version history.
- Activation or effect: successful restore changes active configuration; arbitrary prior external effects and newer unsnapshotted components are not undone by the loop.
- Evidence limits: no recovery run, all-manager audit or whole-system transactional rollback guarantee; memory context restore consults in-process version history.

> result = await mgr.restore(name, version)
> --- `autogenesis/command/default/restore_checkpoint.py`

Admission: caller chooses checkpoint/restore label; code serializes current version identities or applies each map entry. Human authorship/decision is not determined by a CLI principal. There is no content-quality gate or answer oracle; missing artifacts can veto individual restores. Operating mode is explicit control/recovery, not automatic self-improvement. It retains version pointers and timestamp, not reasons or criticism. Failures are collected without an inspected transaction reversing earlier successful restores.

#### MEM-RTE-memory-admission
Label: Generated memory implementation admission

Endpoints: completed memory generator/optimizer → MemoryRegistrationHook path resolution → optional staged validation/promotion → ExtensionManager.add_component("memory") → memory registration. Distinct sibling of supplied [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)'s concrete generated-tool path, using its shared extension infrastructure. SRC-1: `autogenesis/hook/default/memory_registration.py`; generic archive/load/smoke constraints supplied by that runtime record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: allow on registration, block with retry instructions when source cannot be found or registration fails.
- Later read-back: later configured consumers can obtain the registered memory implementation; shared manifest loading can reload admitted source. Migration of existing session content into a new implementation is uninspected, not implied by registration.
- Delegated visibility: parent receives generator final response, not necessarily transformed session contents or full evaluator evidence.
- Selection predicate: target_name or a resolvable extension/memory Python token in reasoning; staged validation/promotion and shared add-component checks, rather than mandatory scored evaluator approval.
- Invalidation or expiry: registration failure blocks finalization; shared extension rollback/unload paths apply subject to their runtime limits. Existing history and disk-file compatibility are not guaranteed by the hook.
- Activation or effect: executable memory implementation enters live registration; actual use, changed context selection and improved retention remain unobserved.
- Evidence limits: hook body and generator finalizer directly read; optimizer finalizer not independently retraced here. Generic shared lifecycle is supplied by runtime, not a tested memory-specific smoke result.

> inferred_name = await extension_manager.add_component(
>     "memory", py_path, config={"enable_evolving": True}
> )
> --- `autogenesis/hook/default/memory_registration.py`

MemoryGenerateAgent invokes this hook on a successful response and converts a BLOCK into response failure. SRC-1: `autogenesis/agent/generator/memory_generate_agent.py`.

> if result.decision == HookDecision.BLOCK:
>     response.success = False
> --- `autogenesis/agent/generator/memory_generate_agent.py`

Model/caller proposes source; software decides path validity and registration success; no human answer or independent quality oracle is consumed by this hook. MemoryEvaluateAgent returns a scored-report task through the base loop and has no registrable artifact; its mere existence does not gate admission. SRC-1: `autogenesis/agent/evaluator/memory_evaluate_agent.py`. This is open capability change, not a fixed training curriculum. Guidance shaping the particular proposal is uninspected; source persists, while reasons are only whatever the normal action/history/trajectory channels retain. Learning and exercised self-improvement are unestablished; the source-level possibility of changing context machinery is not benefit evidence.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-guidance
Label: Derived memory to model guidance

Consumer: later Agent decision model. Channel: recent/working strings → memory get → memory_context → rendered messages on [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance). Force: natural-language evidence/guidance, not executable code or verified constraints. Horizon: subsequent turns and tasks retaining the same RAM entry; cross-process restoration from memory display files is not wired by the inspected get/create methods. Objects: [MEM-OBJ-recent-history](#mem-obj-recent-history), [MEM-OBJ-working-memory](#mem-obj-working-memory). Route: [MEM-RTE-tier-context](#mem-rte-tier-context). SRC-1: `autogenesis/memory/default/tiered.py`, `autogenesis/agent/types.py`.

> "memory_context": memory_body,
> --- `autogenesis/agent/types.py`

#### MEM-BAP-todo-guidance
Label: Retained plan to later agent guidance

Consumer: Agent model. Channel: whole todo Markdown → todo context field → rendered turn. Force: interpreted plan/status text, not an enforced scheduling policy. Horizon: later invocations with matching context/file roots, including disk reread after cache loss if files remain reachable. Object: [MEM-OBJ-todo-tool](#mem-obj-todo-tool); route: [MEM-RTE-todo-context](#mem-rte-todo-context). Unlike the supplied static [RT-OBJ-meta-agent](runtime.md#rt-obj-meta-agent), content changes through use. SRC-1: `autogenesis/agent/types.py`, `autogenesis/tool/default/todo.py`.

> "todo": todo_body,
> --- `autogenesis/agent/types.py`

## Annotations

#### On [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)

Storage and lineage: [MEM-OBJ-corpus](#mem-obj-corpus). Retrieval is requested by base/query or task, then automatic ranking over full retained texts, default top_k four clamped to one minimum. It is not independent unsolicited memory injection. No score threshold, truth test, chunking or per-source authority hierarchy is imposed by the inspected handler. Numerical score is selection metadata; returned records preserve document payloads plus score. SRC-1: `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`.

> results = [{**docs[index], "score": score} for index, score in hits if 0 <= index < len(docs)]
> --- `autogenesis/knowledge/server.py`

At the next inspected consumer, WorkflowRuntime normalization preserves `Response.data` and `files`, rather than dropping retrieved records and keeping only the short message. This establishes a program-data delivery channel for downstream workflow expressions; model delivery still requires an authored downstream binding to an agent/model input. No automatic corpus-to-Agent-memory channel follows. SRC-1: `autogenesis/workflow/runtime.py`.

> return {"message": value.message, "data": value.data, "files": value.files}
> --- `autogenesis/workflow/runtime.py`

No corpus eviction or rollback is implemented by the inspected manager's ingest/retrieve/cleanup methods; cleanup only clears backend instances. Caller-directed file edits/deletion remain possible outside these methods. This scoped finding is not an assertion that all application storage is append-only.

#### On [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

Working-context control: fresh context ID keeps child trace out of the parent's ordinary memory selection. Selected task/files/allowlists cross in; response message crosses back and can become a parent recent record. This resembles a separate call frame with a return value; shared file effects break any isolation inference, and a path is not an automatically followed context reference. Supplied route passages establish boundary crossing; parent retention is supported by SRC-1 `autogenesis/hook/default/memory.py` and `autogenesis/memory/default/tiered.py`. No source evidence here establishes query-based recall of the whole child's removed window.

#### On [RT-RTE-skill-instructions](runtime.md#rt-rte-skill-instructions)

Returned skill text enters the same action-result projection as other successful actions and may later be summarized with the oldest recent chunk. No inspected preferential retention rule protects instructional bodies from compaction. Static skill delivery itself is not read-back of use-changed material; subsequent retention/compaction is. Source: SRC-1 `autogenesis/hook/default/memory.py`, `autogenesis/memory/default/tiered.py`; supplied route provides the original text delivery and type-filter limitation.

#### On [RT-OBJ-workflow-checkpoint](runtime.md#rt-obj-workflow-checkpoint)

Storage/lineage/authority: serialized symbolic variables, frames and invocation records derive from execution and govern later resume under fixed code rules. They preserve executable state rather than necessarily criticism or reasons for changing a method. Distinct alternative forms include [MEM-OBJ-version-snapshot](#mem-obj-version-snapshot) (capability-version pointers), [MEM-OBJ-memory-display](#mem-obj-memory-display) (display/prose projection) and [MEM-OBJ-workflow-evaluations](#mem-obj-workflow-evaluations) (version evidence). Supplied [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) supports the completed-versus-incomplete replay distinction; it does not imply general Agent resumption or exactly-once external effects.

#### On [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest)

Memory horizon: active identities and archives provide a later startup consumer for capability implementations, unlike the tiered-memory display's missing reload leg. Archive/source is retained behavior-determining material; manifest is access/version metadata. Runtime evidence supports live/startup loading and rollback, not retention or consumption of complete evaluation rationale. [MEM-OBJ-version-snapshot](#mem-obj-version-snapshot) adds a separate label-addressed restore map, not another declaration of this manifest.

## Write side

Automatic trace-fed writes have three distinguishable outcomes. Event projection supplies recent records; overflow summarization supplies derived working prose; todo/flow extraction supplies display state. Only the first two are selected by TieredMemory.get. Long explicit todo descriptions can be separately model-shortened for display; that is not the separate TodoTool plan. Software admission governs all these transformations, without a per-content human or truth check. Initialization control remains application/configuration-dependent; it does not obscure the known subsequent automatic writes. [MEM-RTE-tier-context](#mem-rte-tier-context).

Compaction is age/count based, not based on what is still needed. Ordinary removal leaves a summary and verbatim tail; old working summaries can later disappear with no pointer retained in the prompt. Disk report writes overwrite current projection, not an immutable history. Raw diagnostic channels can separately retain richer material, but their storage does not establish automatic reload into model context. [MEM-OBJ-run-records](#mem-obj-run-records), [MEM-OBJ-memory-display](#mem-obj-memory-display).

Material editing/adoption is broader than compaction: TodoTool edits plans; corpus ingest appends documents and changes backend metadata; administrative skill content edits and generated extensions change instructions/executables. The supplied [RT-RTE-runtime-configuration](runtime.md#rt-rte-runtime-configuration) and [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) retain those admission distinctions. Memory-class registration likewise admits source, not evaluated session knowledge. [MEM-RTE-memory-admission](#mem-rte-memory-admission).

Rejection and withdrawal have different retained results. Empty compaction output restores its raw chunk; invalid todo calls fail; malformed memory hook input is skipped. Evaluation rejects run/version mismatches, while old-version evidence remains but is not summarized for a different active version. Workflow unregister removes active definitions and invalidates roster cache; restore selects history and invalidates again. Inactive workflow definitions are excluded by get_instruction/function_callings. SRC-1: `autogenesis/workflow/context.py`.

> if item is None or item.status != WorkflowStatus.ACTIVE:
>     continue
> --- `autogenesis/workflow/context.py`

Extension rollback/unload affects future registration/startup, not already delivered prose or arbitrary earlier side effects. Transcript deletion affects its particular files, not every memory substrate. LRU eviction persists a display then drops the registry entry; MemoryContextManager.cleanup clears configs/history, not a demonstrated comprehensive final flush/delete. Legacy clear_session/get_state wrappers call older methods missing from the inspected base/tier class, so their exposed names do not prove an additional operational cleanup or insight store. SRC-1: `autogenesis/memory/context.py`, `autogenesis/memory/types.py`, `autogenesis/memory/default/tiered.py`.

Reasons can survive in result text, trajectory reasoning, notes or optional evaluation notes, but survival is not guaranteed in the short summaries, version map or manifest. The compact instruction preserves selected facts/failures, not a formal criticism dependency structure. Later summary computation uses metrics rather than interpreting notes; version restore reads pointers rather than reasons. No improved-capacity or content-directed-criticism conclusion follows merely from these connected writes.

## Read-back

The wired model-context route is invocation-requested and code-selected: Agent requests memory by ID; get chooses count tails; the remote foreground model receives text. The compactor is a different consumer receiving oldest-record lines plus last summary. Although automatic maintenance changes what later turns see, there is no independent unsolicited query-relevance push into an idle agent. [MEM-RTE-tier-context](#mem-rte-tier-context).

A second automatic per-turn route rereads whole todo Markdown. It bypasses the use_memory conditional, and is file-based rather than registry-based. The model's explicit tool action can edit the plan, while context code delivers it without another show call. [MEM-RTE-todo-context](#mem-rte-todo-context).

Knowledge retrieval reaches a concrete workflow consumer with its data intact, but does not by itself establish a model-input consumer. Transcript replay reaches a concrete frontend consumer but is likewise not Agent history restoration. API-only trace reads and trajectory exports remain capabilities absent an inspected downstream caller. [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [MEM-RTE-client-replay](#mem-rte-client-replay), [MEM-OBJ-run-records](#mem-obj-run-records).

Recovery reads have stronger symbolic authority at their immediate consumers: workflow checkpoint state determines replay/caching, while version maps request manager restores. Neither is a numerical model update. Active workflow selection filters status; evaluation summaries filter version; extension restart loading uses active manifest identities. Already-returned instruction or result text can outlive withdrawal in an existing window, so registry withdrawal is not universal retroactive invalidation. [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution), [MEM-RTE-version-recovery](#mem-rte-version-recovery), [MEM-RTE-evaluation-records](#mem-rte-evaluation-records), [RT-BAP-extension-execution](runtime.md#rt-bap-extension-execution).

## Integration issues

- No supplied record is corrected or superseded. New detailed task-memory route is a declared part of [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); corpus object is a declared part of [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission). Other new objects/routes are distinct from the closest supplied records as stated in their declarations; no possible duplicate remains asserted.
- [RT-RTE-skill-instructions](runtime.md#rt-rte-skill-instructions) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) can now use the positive same-context action-result retention/compaction account in [MEM-RTE-tier-context](#mem-rte-tier-context). This extends, rather than contradicts, the supplied uninspected exact horizon; cross-restart tier restoration remains unestablished.
- A numerical workflow health signal exists in [MEM-RTE-evaluation-records](#mem-rte-evaluation-records). Do not generalize [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)'s lack of an enforced generated-tool quality threshold into absence of all coded evaluation thresholds. Conversely the signal does not establish automatic admission/rollback or trustworthy caller quality scores.
- Generalized “memory persistence” must preserve the split among [MEM-RTE-tier-context](#mem-rte-tier-context), [MEM-RTE-todo-context](#mem-rte-todo-context), [MEM-RTE-client-replay](#mem-rte-client-replay), and [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution). File writing is known; tier reload is not wired by inspected get/create; todo and replay disk readers are wired; workflow resume is symbolic recovery.
- Remaining questions: custom backend/memory implementations and their consumers; whole frontend message resend behavior; a training or feedback-learning consumer of [MEM-OBJ-run-records](#mem-obj-run-records); per-manager cross-restart completeness of [MEM-RTE-version-recovery](#mem-rte-version-recovery); existing-session state migration after [MEM-RTE-memory-admission](#mem-rte-memory-admission); full canvas/library and kernel/notebook persistence. Available source was not fully traced for those questions. These prevent universal coverage, training, recovery and model-delivery conclusions, not the positive scoped routes above.

## Limitations and checks

The source checkout HEAD was rechecked against the full reviewed commit and its short status was empty before inspection. New reads stayed within SRC-1 and this attempt's supplied inputs; no external source or prior analysis was consulted. Method identity is the supplied memory type, job, worker rules and record contract, read completely, with the supplied runtime/boundary versions rather than mutable peer artifacts.

Conclusions concern implementation and declared policy only. No supplied observed-run or causal-experiment evidence establishes exercised compaction, accurate summaries, effective retrieval, useful evaluation, reliable recovery, learning or beneficial self-improvement. Count limits do not imply bounded total prompt tokens; returned text can be large. Partial leaf coverage is explicit in the inventory and integration issues; the report is not a universal storage/security audit.

Validation: the invocation-specific validate-output check passed: “Member content check passes; invocation residue not checked.” This establishes the reported content check, not semantic acceptance, claim support or operational benefit.
