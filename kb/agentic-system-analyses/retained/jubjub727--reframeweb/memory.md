---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ReframeWeb memory: reviewed decision guidance, graph-selected history and project locators, linked instructions and checkpoint-backed execution inputs."
run-id: AAS-2026-10-14-reframeweb-cff918d7eb1e-01
source-identity: https://github.com/jubjub727/ReframeWeb
reviewed-boundary: 318987dcde9a016f8e3db819ed9a73abf6b3ad81
---

# ReframeWeb memory report

## Boundary and evidence

This report covers retained context and its consumers inside the [frozen whole-system boundary](boundary.md#boundary-and-evidence). Direct inspection used SRC-1 at commit `318987dcde9a016f8e3db819ed9a73abf6b3ad81`; HEAD matched and the checkout was clean. Evidence is implementation and embedded prompt doctrine, not observed execution. The supplied runtime establishes the enclosing routes; this report traces their memory parts and alternative writers. Provider weights, Codex's inner context management, user databases and deployed checkpoints remain outside the captured evidence.

| Entry or operation | Paths in SRC-1 and inspection basis | Coverage and limit |
| --- | --- | --- |
| Setup, voice, browser, workspace and relevance benchmark CLI dispatch | Direct searches of `agent-host/src/reframe_agent_host/cli.py` and `agent-host/src/reframe_agent_host/commands/`; direct reads of loaders and memory service below | [MEM-RTE-context-reload](#mem-rte-context-reload), [MEM-RTE-node-curation](#mem-rte-node-curation), [MEM-RTE-memory-migration](#mem-rte-memory-migration); supplied [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle). Search is an entry inventory, not an audit of every CLI implementation. |
| Five guidance collections and global preferences | Direct: `agent-host/src/reframe_memory/context_memories.py`, `agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py`, candidate review/writeback sources | [MEM-OBJ-context-memory](#mem-obj-context-memory); annotation on [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review). Preference initialization authorship is unresolved, not inferred from the collection name. |
| Conversation and session context; graph retrieval and relevance filtering | Direct: `agent-host/src/reframe_agent_host/agent_flow/session_context.py`, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`, `agent-host/src/reframe_memory/graph_retrieval.py`, query fragments, BAML selection and prompt-context assembly | [MEM-OBJ-session-memory](#mem-obj-session-memory), [MEM-RTE-context-reload](#mem-rte-context-reload), [MEM-RTE-graph-selection](#mem-rte-graph-selection). Other session creation/editing callers are not exhaustively inspected. |
| Tool receipts, output data and summary | Direct: `agent-host/src/reframe_agent_host/task_tools/history.py`, `agent-host/src/reframe_agent_host/task_tools/outputs.py`, `agent-host/src/reframe_memory/task_history.py`, `agent-host/src/reframe_agent_host/agent_flow/action_history.py` | [MEM-OBJ-task-history](#mem-obj-task-history), [MEM-RTE-history-summary](#mem-rte-history-summary). Agent feedback route is supplied by [RT-RTE-codex-task](runtime.md#rt-rte-codex-task); no durable summary index is inferred. |
| Registered project verification and save tools | Direct: `agent-host/src/reframe_agent_host/task_tools/project_memories.py`, `agent-host/src/reframe_agent_host/task_tools/save_artifacts.py`, locator migration | [MEM-RTE-project-locator](#mem-rte-project-locator); separates metadata from saved bytes. |
| Linked instructions, explicit edits and task workspace preparation | Direct: `agent-host/src/reframe_memory/instruction_memories.py`, `agent-host/src/reframe_memory/task_memories.py`, `agent-host/src/reframe_agent_host/task_tools/store_instructions.py`, `agent-host/src/reframe_agent_host/workspace/task_preparation.py`, `agent-host/src/reframe_agent_host/agent_flow/task_execution.py` | [MEM-OBJ-instruction-memory](#mem-obj-instruction-memory), [MEM-BAP-linked-instructions](#mem-bap-linked-instructions). Linked instructions bypass graph relevance selection. |
| Directory registration, checkpoint publication, dependency resolution | Direct: `agent-host/src/reframe_agent_host/workspace/memory_service.py`, `agent-host/src/reframe_agent_host/workspace/publication_service.py`, `agent-host/src/reframe_agent_host/workspace/planning.py`, retention adapter and native Store layout | [MEM-OBJ-filesystem-memory](#mem-obj-filesystem-memory), [MEM-OBJ-workspace-store](#mem-obj-workspace-store); annotation on [RT-RTE-saved-store](runtime.md#rt-rte-saved-store). Native mount, retention and blob-cleanup leaves remain uninspected; no crash-durability or exhaustive garbage-collection claim. |
| Store publication, startup, application instructions/task edits and panel services | Supplied runtime findings, plus direct Store locator selection and instruction-edit sources | Annotations on [RT-RTE-saved-store](runtime.md#rt-rte-saved-store), [RT-RTE-application-publish](runtime.md#rt-rte-application-publish). Native service state and UI internal state are not treated as general agent memory without a demonstrated delivery path. Their complete persistence semantics remain outside this memory inspection. |
| Generic graph maintenance and old-database import | Direct browser API/UI, `agent-host/src/reframe_memory/merge_databases.py`, `agent-host/src/reframe_memory/graph_merge.py`, `agent-host/src/reframe_memory/locator_migration.py` | [MEM-RTE-node-curation](#mem-rte-node-curation), [MEM-RTE-memory-migration](#mem-rte-memory-migration). These counter a reading that model review is the sole admission gate. |
| Evaluation | Direct bounded read: `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`; supplied runtime's evaluator inventory | [MEM-CLM-selection-evaluation](#mem-clm-selection-evaluation). No benchmark was run or stored result audited; no measured accuracy or automatic production update is established. |

## Core ideas

There is no single memory admission or retrieval policy. Reviewed guidance, unfiltered layer reloads, relevance-selected historical material, explicit task links and executable Store startup references have different controls. Keeping a candidate guidance ID is neither permission to invoke tools nor proof of truthful content. Conversely, a task-linked instruction need not win relevance selection to reach execution ([MEM-BAP-linked-instructions](#mem-bap-linked-instructions), [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt)).

The graph path selects text and locators before resolving files. A saved project candidate displays metadata, not the checkpoint's file bodies. The downstream composer then rewrites selected context into a standalone input; the executor does not inherit all upstream objects. These are meaningful context boundaries, not a shared reference-addressable model window ([MEM-RTE-graph-selection](#mem-rte-graph-selection)).

The clearest automatic trace-fed guidance path is optional model proposal → model admission → title/description persistence → future layer prompt. Review asks for reusable decision lessons, but its input is candidates and stored guidance rather than an independent execution test. The write adapter discards staging IDs and retains no separately structured rejection reasons, observation links or review argument. A description could contain reasons, but the interface does not require that. This supports a retained guidance mechanism, not demonstrated learning or reliable criticism (annotation on [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-context-memory
Label: Layer guidance and preference text

Source-native identity: `ContextMemoryStore` and its five decision-guidance collections plus `UserPreferenceMemoryStore`. These share title/description storage and reload mechanics, but differ in admission lineage: model-reviewed candidates write only the five guidance destinations; preference origin is not established by that writer. Natural-language title/description is interpreted by later models. Symbolic collection edges, tags and timestamps route and describe it. Substrate: SurrealDB `memory_node`, root `contains` relations and configured local SurrealKV or remote database adapter. `read_at` is access metadata, not a truth, use or benefit score. Lineage of pre-existing collection content is unresolved. No counterpart object is declared in the supplied runtime; closest route is [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review).

Evidence: SRC-1, `agent-host/src/reframe_memory/database.py`, `agent-host/src/reframe_memory/context_memories.py`, `agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py`.

> ORDER BY updated_at DESC, created_at DESC;
> --- `agent-host/src/reframe_memory/context_memories.py`

#### MEM-OBJ-session-memory
Label: Session text, conversation messages and locator records

Source-native identities: `SessionMemoryStore`, `ConversationMessage`, and project locators encoded in `SessionMemory.description`. Substrate: SurrealDB nodes and session/conversation relations. Natural-language message and memory bodies coexist with symbolic roles, IDs, timestamps and `relevance_required`. Locator descriptions are JSON strings containing prose plus runtime identity, paths and provenance fields; display text is not copied file content. Raw human and validation replies are written by host callbacks; verified and saved locators are generated by tools. Other session memory authorship is caller-dependent. Initial arbitrary session memories are not proved to be summaries or learned lessons. Later consumers are context loaders and graph selection, not direct execution of locator JSON. Closest supplied record is [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle), a route rather than this retained material.

Evidence: SRC-1, `agent-host/src/reframe_memory/session_memories.py`, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`, `agent-host/src/reframe_agent_host/task_tools/project_memories.py`, `agent-host/src/reframe_agent_host/task_tools/save_artifacts.py`.

> ConversationMessage(role="human", content=transcript),
> --- `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`

#### MEM-OBJ-instruction-memory
Label: Independent linked instruction bodies

Source-native identity: `InstructionMemoryStore`, `InstructionMemory` and `TaskMemoryLinks`. Natural-language `instructions` is separate from descriptive title/description; symbolic task associations determine delivery. Substrate: graph nodes under the instruction root and many-to-many `task_memory` edges. Store metadata also references instruction IDs. The root description says user-authored, but the code permits application publication and assigned-tool edits; that label does not prove per-content human control. Task preparation emits assembled `AGENTS.md`; direct execution appends the instruction bodies. This is not the saved Store metadata referent of [RT-RTE-saved-store](runtime.md#rt-rte-saved-store), though that route can reference it.

Evidence: SRC-1, `agent-host/src/reframe_memory/instruction_memories.py`, `agent-host/src/reframe_memory/task_memories.py`, `agent-host/src/reframe_agent_host/workspace/task_preparation.py`.

> "User-authored instructions linked explicitly to tasks.",
> --- `agent-host/src/reframe_memory/instruction_memories.py`

> # Always replace an imported assembled root. Never derive graph instructions
> # from it or infer memory changes from subsequent agent edits.
> --- `agent-host/src/reframe_agent_host/workspace/task_preparation.py`

#### MEM-OBJ-filesystem-memory
Label: Filesystem memory locators

Source-native identities: `DirectoryFilesystemMemory`, `CheckpointFilesystemMemory`, `base_memory_ids`. Symbolic graph content identifies either a mutable directory path or a backing store plus immutable manifest, with dependency IDs; natural-language title/description is catalog display. Substrate: graph records, not the retained bytes themselves. Identity checks bind content to a persistent identity. Directory registration does not freeze directory content. Checkpoint lineage includes base-memory dependencies, whereas graph title text alone supplies no file-level provenance. Consumers resolve explicit IDs into materialization sources; they reject cycles, missing source directories and missing backing stores. This is a material object used by [RT-RTE-saved-store](runtime.md#rt-rte-saved-store), not a second declaration of that route.

Evidence: SRC-1, `agent-host/src/reframe_memory/filesystem_memories.py`, `agent-host/src/reframe_agent_host/workspace/planning.py`, `agent-host/src/reframe_agent_host/workspace/memory_service.py`.

> if memory_id in resolving:
>             raise WorkspaceError(f"filesystem memory dependency cycle: {memory_id}")
> --- `agent-host/src/reframe_agent_host/workspace/planning.py`

#### MEM-OBJ-workspace-store
Label: Checkpoint bytes and workspace recovery substrate

Source-native identity: native workspace `Store`, `PersistedMemorySource`, manifests and session files. Substrate: `workspace.sqlite3`, `blobs` and `sessions` directories. Manifests and source identities are symbolic; payload form depends on individual files, potentially natural-language instructions, symbolic source/executable artifacts or opaque binaries. No inspected path establishes model weights as a retained workspace payload. Graph checkpoint descriptions are readable summaries, not representations sufficient to reconstruct bytes without the backing store. Recovery state survives attempts; explicit publication makes selected content available for later tasks or startup. Detailed native crash recovery and blob deletion remain uninspected. Distinct from [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt), an in-memory authority ledger, and from graph locator [MEM-OBJ-filesystem-memory](#mem-obj-filesystem-memory).

Evidence: SRC-1, `workspace-fs/crates/workspace-daemon/src/store.rs`, `agent-host/src/reframe_agent_host/workspace/publication_service.py`; supplied [RT-RTE-codex-task](runtime.md#rt-rte-codex-task).

> fs::create_dir_all(root.join("blobs"))?;
>         fs::create_dir_all(root.join("sessions"))?;
> --- `workspace-fs/crates/workspace-daemon/src/store.rs`

#### MEM-OBJ-task-history
Label: Raw tool outcome graph

Source-native identities: `ToolHistory`, `TaskHistoryStore`, actions and ordered history nodes. Symbolic call/task/attempt IDs and outcome status accompany arbitrary JSON arguments, results and artifacts, which may include natural-language text. Substrate: graph nodes/relations; the live `outcomes` list is additionally in process. The host writes actual adapter outcomes and final data, not independently verified world truth. A summarizer later renders this history. This object is separate from [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt): the latter owns authority and uncertainty, while this persists receipts. Closest routes are [RT-RTE-model-task](runtime.md#rt-rte-model-task) and [RT-RTE-codex-task](runtime.md#rt-rte-codex-task).

Evidence: SRC-1, `agent-host/src/reframe_agent_host/task_tools/history.py`, `agent-host/src/reframe_memory/task_history.py`, `agent-host/src/reframe_agent_host/task_tools/outputs.py`.

> input={"task_id": binding.task_id, "attempt_id": binding.attempt_id,
>                    "call_id": outcome["call_id"], "arguments": arguments},
>             output=outcome, tags=("task-tools", outcome["status"]),
> --- `agent-host/src/reframe_agent_host/task_tools/history.py`

### Routes

#### MEM-RTE-context-reload
Label: Automatic layer and session context reload

Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

Trigger/owner: BAML cycle invokes host context callbacks; Python selects by collection and acceptance-bound session/conversation, not a model search request. It loads all entries returned by each guidance/preference collection and current session memories not requiring relevance. The session conversation loader retrieves role-labelled messages. This is automatic prompt supply from retained state, not independent unsolicited action. No numerical context budget or recency truncation is implemented in these inspected loaders; ordering by timestamps is not a cap.

- Immediate return: typed task catalog, guidance, preferences, conversation and session-memory context objects.
- Later read-back: later task-choice/search/depth/relevance/composition invocations receive retained collection text; task/provider catalog also supplies stored prompts, model selection and tool IDs.
- Delegated visibility: layer guidance projects title/description/tags/timestamps without durable memory IDs; preferences retain IDs for selection. Non-relevance session context omits locator bodies requiring selection.
- Selection predicate: collection membership, current session/conversation binding and `relevance_required` filtering; `TaskConversation` additionally excludes validation replies and other active human replies except the current one.
- Invalidation or expiry: reloads reflect subsequent edits/deletion; this loader defines no content TTL. Task-frame omission does not delete stored messages.
- Activation or effect: text is delivered for model interpretation; task/provider metadata has code-level dispatch consequences. Reliable compliance is unobserved.
- Evidence limits: no actual retained contents or invocation sizes supplied; upstream database contents and deployment limits unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py`, `agent-host/src/reframe_agent_host/agent_flow/session_context.py`, `agent-host/baml_src/ns_voice_turn/task_flow.baml`.

> memories = [memory for memory in memories if not memory.content.relevance_required]
> --- `agent-host/src/reframe_agent_host/agent_flow/session_context.py`

> message.role != "validation_reply"
> --- `agent-host/baml_src/ns_voice_turn/task_flow.baml`

#### MEM-RTE-graph-selection
Label: Planned graph retrieval and selected project resolution

Part of: [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle)

Progression: model search hints and timestamp depths → Python graph queries → decoded candidate context and read timestamps → Store-project search → relevance model IDs → `SelectedGraph` → `PromptContexts` → model-composed standalone task input. Code owns retrieval, ID intersection and reference resolution; models choose search and kept IDs and rewrite text. The user supplies the request, not per-memory approval. No independent answer oracle is used in production selection; operating mode is open task requests. This selection does not admit new durable guidance.

- Immediate return: retrieved graph, relevance decision, selected context list and composed task prompt.
- Later read-back: stored sessions/messages, session memories, task catalog, preferences and saved Store locators can reach a later task invocation. Selected Store project IDs additionally resolve referenced instruction/filesystem memories during agent workspace preparation.
- Delegated visibility: relevance sees candidate summaries and contextual metadata; composer receives filtered contexts; executor receives rewritten task prompt, with separately appended/materialized linked inputs. File bytes are not loaded merely because a locator became a relevance candidate.
- Selection predicate: tag/string hints and per-domain created/updated/read thresholds; a missing past-context depth returns no historical candidates. Current non-relevance session memories use a separate query. Store projects use string hints, deliberately ignore global tag hints and cap results at 32. Kept IDs filter each retained part, including individual messages; parent wrappers may survive because a child survives.
- Invalidation or expiry: timestamp windows limit search, not stored lifetime; missing selected Store references fail resolution. Retrieval marks decoded read IDs before model relevance, so access metadata is not proof of final selection or execution use.
- Activation or effect: retained content is supplied to relevance/composition and explicit project inputs can materialize in a later workspace. Model-dependent behavioral change is not observed.
- Evidence limits: inspected queries and transforms establish wiring, not recall completeness, semantic relevance, prompt-token sufficiency or trusted factual content. Exact provider context handling is external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/src/reframe_memory/graph_retrieval.py`, `agent-host/src/reframe_memory/graph_retrieval_query_conversations.py`, `agent-host/src/reframe_memory/graph_retrieval_query_sessions.py`, `agent-host/src/reframe_memory/store_projects.py`, `agent-host/baml_src/ns_memory/selection/selection.baml`, `agent-host/baml_src/ns_memory/ns_internal/selection.baml`, `agent-host/baml_src/ns_task/prompting/memory_context.baml`, `agent-host/baml_src/ns_task/prompting/flow.baml`.

> await self.database.mark_record_ids_read(list(decoded.read_ids))
> --- `agent-host/src/reframe_memory/graph_retrieval.py`

> # Store publication has no authored tag taxonomy. Global memory tag hints
>     # must not hide a locator explicitly named by its ID, name or description.
> --- `agent-host/src/reframe_memory/store_projects.py`

> The downstream runner has
>         no access to the upstream context objects.
> --- `agent-host/baml_src/ns_task/prompting/flow.baml`

#### MEM-RTE-project-locator
Label: Verified and saved project locator writes

Assigned task tools offer two distinct admissions. `project_remember` accepts model/caller description but code requires completed successful calls from this attempt and kind-specific live evidence. Panel verification requires screenshot and DevTools tool names; Store verification requires a completed invocation without failure events. This checks evidence shape and live identity, not independent task correctness. `save_visual_panel`/`save_semantic_store` instead validate prepared-workspace registration and explicit relative paths, checkpoint without task linking and append a saved-artifact locator. These save tools do not inherit `project_remember`'s verification predicate. No human content approval is established by the generic caller. Operating mode: open maintenance; no expected-answer oracle. Content guidance is in the tool descriptions: use registered task-local sources, never unrelated workspaces and inspect partial failures.

- Immediate return: memory ID/path for verified locators; saved checkpoint receipt plus complete/partial locator-publication status for save tools.
- Later read-back: JSON descriptions persist as relevance-required session memories and can enter subsequent graph selection. Checkpoint bytes remain separately referenced.
- Delegated visibility: later relevance gets locator text and metadata, not an opaque runtime's entire state or full source tree.
- Selection predicate: assigned tool authority plus per-tool verification/registration checks; later retrieval hints and kept IDs govern delivery.
- Invalidation or expiry: append rather than overwrite another identity; live runtime may later disappear. No locator TTL is established. Failed locator write preserves the actual checkpoint receipt and reports partial status, not global rollback.
- Activation or effect: new locators become retrievable; saving does not itself start a project or attach its bytes to every future task.
- Evidence limits: verification event predicates are not observed acceptance outcomes, and locator prose remains caller-authored. No content-specific human review is implied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Distinct from supplied [RT-RTE-saved-store](runtime.md#rt-rte-saved-store): this route records verified/saved session locators, not saved Store metadata CAS or activation. It overlaps that route's checkpoint producer but has a separate session-memory consumer and rejection gate. Evidence: SRC-1, `agent-host/src/reframe_agent_host/task_tools/project_memories.py`, `agent-host/src/reframe_agent_host/task_tools/save_artifacts.py`.

> if outcome["status"] != "ok":
>                 raise ValueError("failed or uncertain calls are not verification")
> --- `agent-host/src/reframe_agent_host/task_tools/project_memories.py`

> arguments = {"paths":selected, "link_to_task":False}
> --- `agent-host/src/reframe_agent_host/task_tools/save_artifacts.py`

#### MEM-RTE-node-curation
Label: Explicit graph editing and withdrawal

The shipped browser's PATCH edits tags/content; DELETE removes the node and its relation edges. The browser UI asks confirmation before deletion. A human interacting with that UI chooses exact content, while direct API caller identity is unspecified. Independently, `edit_store_instructions` permits assigned-tool replacement only for an instruction attached to the selected Store, with expected-text guard and read-back verification. These are alternative admissions to model guidance review, not automatic curation. Operating mode: explicit maintenance. No answer oracle; object-shape or expected-content checks do not evaluate semantic quality. Tool guidance states that active prompts remain unchanged.

- Immediate return: saved record, deleted ID or instruction ID/text with future-preparation effective horizon.
- Later read-back: later collection reloads, task preparation and startup references see changed or missing graph content. `TaskMemoryLinks.unlink` removes future task association without deleting the underlying memory.
- Delegated visibility: browser displays editable JSON; instruction edit returns saved text; already assembled prompts/workspaces are not retroactively rewritten.
- Selection predicate: browser node ID and basic list/object checks; Store edit requires attached identity and expected current instructions. Task link admission validates task and instruction/filesystem membership.
- Invalidation or expiry: browser delete removes enumerated incident relation edges but does not cascade into child records; no graph-wide reference repair or automatic rollback is established. Store edit rejects concurrent change rather than overwriting it blindly.
- Activation or effect: later text consumers can receive edited instructions; generic browser writes may violate typed consumers' expectations despite accepting JSON shape. Withdrawal does not undo earlier external effects.
- Evidence limits: UI interaction was not observed; HTTP deployment/authentication is not assessed. No blanket claim that all memory changes require a human or the guarded edit API.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No supplied route has this referent; closest overlap is instruction maintenance adjacent to [RT-RTE-saved-store](runtime.md#rt-rte-saved-store). Evidence: SRC-1, `agent-host/src/reframe_agent_host/memory_browser/records.py`, `agent-host/src/reframe_agent_host/memory_browser/static/app.js`, `agent-host/src/reframe_agent_host/task_tools/store_instructions.py`, `agent-host/src/reframe_memory/task_memories.py`.

> for table in MEMORY_RELATIONS:
>             await database.query(
>                 f"DELETE {table} WHERE in = {record_id} OR out = {record_id};"
>             )
> --- `agent-host/src/reframe_agent_host/memory_browser/records.py`

> 'effective':'future task preparation; active prompts are unchanged'}
> --- `agent-host/src/reframe_agent_host/task_tools/store_instructions.py`

#### MEM-RTE-memory-migration
Label: Explicit graph import and locator-policy migration

The standalone module defaults to dry run. Caller supplies old and target database directories; `--apply` requires a new backup directory. Code vetoes conflicting identities, guards the complete target snapshot inside a transaction and verifies post-merge read-back. It preserves source records rather than synthesizing lessons. Generic caller identity leaves human per-content admission unresolved. Separately, `apply_schema` automatically upgrades old saved/verified session locators to `relevance_required=true` by tag, retaining identity/links/timestamps. This is a code-directed visibility change, not a semantic correction or model judgment. No answer oracle; operating mode is migration/maintenance, not improvement experimentation.

- Immediate return: dry-run/apply additions report and task listing; schema migration returns after updating matching flags.
- Later read-back: imported graph records join normal collection/task/startup consumers; upgraded locators cease entering unconditional session context and instead require relevance selection.
- Delegated visibility: backups retain raw source/target snapshots; later prompts receive ordinary projected context, not migration reports by default.
- Selection predicate: missing stable record identities for import; saved-artifact/verified-project tags plus false/missing relevance flag for policy migration.
- Invalidation or expiry: conflicting or stale snapshots reject merge; backups support manual recovery but automatic rollback after a failed post-merge comparison is not established. Flag migration is idempotent, not deletion.
- Activation or effect: target content and future context visibility change; an explicit module entry is an afforded maintenance invocation, while schema-to-locator update is wired.
- Evidence limits: neither migration was executed; database transaction/crash behavior is not measured. Imported authorship and original traces remain source-database dependent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No supplied counterpart; [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review) is an alternative writer with a different gate. Evidence: SRC-1, `agent-host/src/reframe_memory/merge_databases.py`, `agent-host/src/reframe_memory/graph_merge.py`, `agent-host/src/reframe_memory/locator_migration.py`, `agent-host/src/reframe_memory/database.py`.

> raise ValueError("--apply requires a new --backup directory")
> --- `agent-host/src/reframe_memory/merge_databases.py`

> UPDATE $locators SET content.relevance_required = true;
> --- `agent-host/src/reframe_memory/locator_migration.py`

#### MEM-RTE-history-summary
Label: Recorded action history to completion summary

Part of: [RT-RTE-model-task](runtime.md#rt-rte-model-task)

Host writes tool receipts/final data, renders a retained history by ID and invokes the task provider's summarizer. The next completion invocation receives derived text. This is trace-fed context reduction with a concrete later consumer, even within one turn; it is not evidence that raw traces become durable decision guidance. Model writes summary text; code owns admission of receipts and control flow; user approval is not interposed. The completion judge is not an independent answer oracle.

- Immediate return: summary string, or failure propagated by the host boundary.
- Later read-back: summary reaches completion checking and retry context in the enclosing cycle; raw history remains graph-backed. Cross-session durable summary retrieval is uninspected.
- Delegated visibility: completion receives summary and scoped conversation/failure state, rather than the full tool transcript. Codex uses a different executor-supplied feedback route, not this summarizer.
- Selection predicate: task history ID and selected task/provider; no content relevance selector in this summarizer. Raw JSON is rendered before the model call.
- Invalidation or expiry: the summarizer returns text without a durable summary write in the inspected function; retained history is separate. Retry bounds come from the parent route, not this transformation.
- Activation or effect: derived text supplies the later completion model, which may influence retry selection; accuracy and outcome dependence remain unobserved.
- Evidence limits: no actual summary or measured compression fidelity. Requested summary behavior does not prove preserved reasons or full effect visibility.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `agent-host/src/reframe_agent_host/agent_flow/action_history.py`, `agent-host/src/reframe_agent_host/voice/turn_side_effects.py`; supplied [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle).

> recorded_action_history = await database.task_history.render(task_history_id)
>         inputs = {"recorded_action_history": recorded_action_history}
> --- `agent-host/src/reframe_agent_host/agent_flow/action_history.py`

### Claims

#### MEM-CLM-selection-evaluation
Label: Relevance benchmark measures expected ID selection

Claimed operation: benchmark results record expected IDs, kept IDs, correctness, task correctness, latency and usage against reusable candidate snapshots. Expected labels provide a bounded benchmark oracle, unlike the production relevance model's own judgment. This is evaluator design; no inspected result establishes successful operation or causal memory benefit. No automatic admission/update edge from these scores to production guidance was established. No supplied record has this evaluator referent; closest consumer route is [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle).

Evidence: SRC-1, `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`.

> "expected_kept_memory_ids": expected_ids,
>         "kept_memory_ids": list(decision.kept_memory_ids),
>         "correct": baml_benchmarks.MemorySelectionCorrect(decision, expected_ids),
> --- `agent-host/src/reframe_agent_host/benchmarks/memory_relevance_execution.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-linked-instructions
Label: Task-linked instruction delivery

Consumer: direct task executor and delegated Codex executor. Channel: instruction bodies appended through `TaskPromptWithInstructions`, or root `AGENTS.md` assembled from explicit task/selected-Store references. Force: natural-language behavioral guidance, interpreted by a model, not tool permission enforcement. Horizon: next task execution/preparation; retries can reuse an already prepared workspace. Root instruction edits in that workspace are not inferred as graph edits, and generated `AGENTS.md` is excluded from checkpoint output. Symbolic task tool IDs separately constrain Host operations. This path differs from [RT-BAP-store-callback](runtime.md#rt-bap-store-callback), which performs revision/grant checks on guest requests, not prose interpretation.

Evidence: SRC-1, `agent-host/src/reframe_agent_host/agent_flow/task_execution.py`, `agent-host/src/reframe_agent_host/workspace/task_preparation.py`; supplied [RT-RTE-codex-task](runtime.md#rt-rte-codex-task).

> policy=WorkspacePolicy(checkpoint_exclusions=["AGENTS.md"]),
> --- `agent-host/src/reframe_agent_host/workspace/task_preparation.py`

## Annotations

#### On [RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review)

Write lineage is model-proposed decision-layer observations, with prompt-level prohibitions on promoting user/task input into guidance. Review can keep no candidate; code intersects kept IDs and persists only title/description. The proposal/review path is automatic computational admission during an open request, not demonstrated content-level human review. Storage and later consumers are [MEM-OBJ-context-memory](#mem-obj-context-memory) and [MEM-RTE-context-reload](#mem-rte-context-reload). This is a qualifying trace-fed guidance write architecture, but the originating observation's truth, provenance completeness and any improved future capacity are not established. It is not a separate durable criticism log. Review API exposes only purpose, candidate entries and stored guidance; rejection reasons and the full interaction are not separate inputs/outputs there.

Evidence: SRC-1, `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`, `agent-host/baml_src/ns_memory/candidate_review_types.baml`, `agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py`.

> Favor guidance that is durable, supported by the observed interaction, distinct from stored guidance, and useful beyond the immediate request.
> --- `agent-host/baml_src/ns_memory/candidate_review_prompt.baml`

> class CandidateMemoryReviewDecision {
>     kept_candidate_ids: string[],
> }
> --- `agent-host/baml_src/ns_memory/candidate_review_types.baml`

> ContextMemory(
>                     title=candidate.title,
>                     description=candidate.description,
>                 )
> --- `agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py`

#### On [RT-RTE-saved-store](runtime.md#rt-rte-saved-store)

Memory parts separate graph locator metadata, backing bytes, independent instruction bodies and saved Store configuration. Explicit retention normally links the published checkpoint to a task; save-artifact tools deliberately pass `link_to_task=False`. Directory registration is an additional source form and does not create an immutable snapshot. Dependency resolution recursively materializes base memories before derived sources. Publication reconciliation writes the graph record before acknowledging the daemon outbox; it does not make Store activation or locator creation part of one global transaction. Startup consumes executable/UI references as symbolic configuration and artifacts, not merely as model knowledge. Future task preparation instead supplies editable files and instruction prose. The parent's activation/admission claims remain scoped as supplied, not upgraded to observed durability.

Evidence: SRC-1, `agent-host/src/reframe_agent_host/agent_execution/retention.py`, `agent-host/src/reframe_agent_host/workspace/publication_service.py`, `agent-host/src/reframe_agent_host/workspace/planning.py`, `agent-host/src/reframe_agent_host/workspace/task_preparation.py`, `agent-host/src/reframe_agent_host/task_tools/save_artifacts.py`; supplied startup evidence in the annotated record.

> node = await self._publish_graph(checkpoint)
>         await asyncio.to_thread(
>             self._daemon.complete_checkpoint_publication,
>             publication.manifest_id,
>             node.id,
>         )
> --- `agent-host/src/reframe_agent_host/workspace/publication_service.py`

#### On [RT-RTE-application-publish](runtime.md#rt-rte-application-publish)

The supplied source-traced publisher establishes an explicit non-candidate-review writer for instructions, task prompt/tool metadata and startup membership. The resulting text has later model consumers through task catalog and linked instructions, while executable references have the startup consumer. Per-content human control is unresolved: script invocation alone is not approval of each instruction or grant. Application receipt gates apply to that publication route, not all graph writes or subsequent browser edits. The native application's internal Store/UI state was not directly inspected here; no agent-memory use is inferred for arbitrary internal fields.

## Write side

Admission is local to each mechanism. Model-reviewed guidance writes are automatic after a computational keep decision. Background human/validation message recording stores raw interaction without guidance review. The project-verification gate validates receipts/live identity, while saved-artifact locators follow registration/path checks. Generic browser edits and direct store APIs can write content without the review model; caller identity is not automatically human. Explicit instruction edits use attached-Store and expected-content checks. Import uses backup/conflict/snapshot gates; schema migration changes visibility by tag. These distinctions are recorded in [MEM-RTE-project-locator](#mem-rte-project-locator), [MEM-RTE-node-curation](#mem-rte-node-curation), [MEM-RTE-memory-migration](#mem-rte-memory-migration) and the guidance annotation.

Checkpoint publication retains bytes and identity, not an automatically extracted lesson. Ordinary workspace persistence supports recovery; explicit selected-path retention publishes reusable content. Save tools can succeed at checkpoint publication and fail at locator creation, preserving a partial receipt. Graph deletion removes incident edges, not descendant bytes; task unlinking changes association rather than deleting memory. Uninspected native retention/blob-cleanup leaves prevent a complete lifecycle or disk-reclamation account. These limits do not negate known graph withdrawal and publication behavior.

Trace-to-derived chains must remain separate: tool receipts → rendered history → completion summary; optional layer observations → reviewed title/description → later guidance prompt; registered live verification → provenance-bearing session locator → relevance selection. Only the second writes general decision guidance. None alone demonstrates a better future capacity. Root `AGENTS.md` is reconstructed from retained instructions, not mined back into memory after an agent edits it. No opaque Codex/provider compaction or parameter update is inferred.

## Read-back

The automatic reload and request-targeted search routes coexist. At cycle start, code loads all layer guidance/preferences and non-relevance session memories; task-specific graph search then requests history by hints/time ranges and asks a model to select candidates. A relevance instruction to include every relevant option is not a token-budget controller. Inspected loaders impose no numerical global budget; the Store-project search has a 32-result cap. Source: SRC-1, `agent-host/baml_src/ns_memory/selection/flow.baml`, `agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py`, `agent-host/src/reframe_memory/store_projects.py`; [MEM-RTE-context-reload](#mem-rte-context-reload), [MEM-RTE-graph-selection](#mem-rte-graph-selection).

Task-linked instructions and files take an explicit association route, not a relevance score. Selected Store references can add inputs, but task links alone suffice to append instruction prose or prepare filesystem content. Startup's saved executable selection is another actual consumer, with symbolic configuration authority. A bare create/get API for some arbitrary memory caller would not establish these routes; the inspected execution/preparation and supplied startup wiring does.

Working-context controls operate by value: BAML filters role-labelled conversation into a task frame; graph selection filters retained objects; composition rewrites them into self-contained input; Codex runs ephemerally and returns bounded feedback while filesystem state survives retries; summary substitutes for raw action history at completion. A selected-input frame resembles a call frame, but discarded model context is not a graph reference the executor can dereference automatically. Reload requires host callbacks, explicit graph references or workspace materialization. Full upstream context and opaque Codex intermediate reasoning do not cross the return boundary ([RT-RTE-codex-task](runtime.md#rt-rte-codex-task), [MEM-RTE-history-summary](#mem-rte-history-summary)).

Trust is also channel-specific. The composer is instructed to preserve speaker attribution/provenance and distinguish live observations from remembered assertions; those are requested model behaviors, not semantic validation. Graph role/status metadata supports attribution but does not authenticate every stored assertion. Task tool assignment and Store activation checks enforce symbolic authority independently of prose. Source: SRC-1, `agent-host/baml_src/ns_task/prompting/flow.baml`; [RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt), [RT-BAP-store-callback](runtime.md#rt-bap-store-callback).

> Distinguish observed live state from remembered assertions.
> --- `agent-host/baml_src/ns_task/prompting/flow.baml`

## Integration issues

- No correction to a supplied fact is required. The supplied runtime appropriately leaves memory revision semantics open. Its guidance-review gate must not be generalized to browser/API/import writers or to saved-artifact locator admission; the direct source gates differ ([MEM-RTE-node-curation](#mem-rte-node-curation), [MEM-RTE-project-locator](#mem-rte-project-locator), [MEM-RTE-memory-migration](#mem-rte-memory-migration)).
- No duplicate referent is intentionally declared. Context reload and graph selection are parts of [RT-RTE-request-cycle](runtime.md#rt-rte-request-cycle); history summarization is a part of [RT-RTE-model-task](runtime.md#rt-rte-model-task). The project-locator route overlaps checkpoint production in [RT-RTE-saved-store](runtime.md#rt-rte-saved-store), but adds separate verification/save gates and session-memory results rather than duplicating metadata publication/activation. Objects name retained parts, not the supplied enclosing routes.
- Preference and arbitrary pre-existing session/guidance content initialization remain caller-dependent. Known automatic writes do not settle all initial authorship or per-content human control ([MEM-OBJ-context-memory](#mem-obj-context-memory), [MEM-OBJ-session-memory](#mem-obj-session-memory)).
- Native workspace cleanup, crash recovery, mount behavior and application internal Store/UI persistence were not deeply inspected. This prevents exhaustive deletion/durability/internal-state read-back findings, not the supported checkpoint publication/task/startup consumer findings ([MEM-OBJ-workspace-store](#mem-obj-workspace-store), annotation on [RT-RTE-application-publish](runtime.md#rt-rte-application-publish)).
- Provider/Codex hidden compaction and parameter state remain outside evidence. No automatic guidance benefit, accurate summary fidelity or actual instruction compliance can be inferred without observations. The relevance benchmark provides an available expected-ID evaluator, not production outcome evidence ([MEM-CLM-selection-evaluation](#mem-clm-selection-evaluation)).

## Limitations and checks

Source and method identities were rechecked against the supplied boundary, member types, worker rules and shared record contract. Inspection stayed within SRC-1 and read-only source operations; no target tests, services, models or experiments were executed. Claims were challenged against alternative writers, directory versus checkpoint storage, saved versus verified locator gates, filtered versus unconditional inputs and generated-root exclusion. Available but unread implementation leaves are explicitly inspection limits, not access gaps or evidence of absence.

Deterministic validation: the required invocation-specific `commonplace-run validate-output` command passed (exit status 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Validation checks form and quotation occurrence, not semantic correctness or integration acceptance.
