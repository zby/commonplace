---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "CrewAI memory: extracted and consolidated records, selective recall, knowledge ingestion, feedback lessons and retained execution state."
run-id: AAS-2026-10-15-crewai-62e53db969a7-01
source-identity: "https://github.com/crewAIInc/crewAI"
reviewed-boundary: "3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8"
---

# CrewAI memory report

## Boundary and evidence

This report covers retained context within the whole-system [boundary](boundary.md), at SRC-1 commit `3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8`. The supplied [runtime](runtime.md) orders the investigation but does not limit it. Direct reads establish implementation wiring, not successful execution. There are no supplied observed runs or causal experiments.

Memory scope includes unified Memory and its caller/tool/API admissions; LanceDB and Qdrant Edge alternatives; scopes and slices; knowledge ingestion; feedback-derived instructions; summary replacement; replay, checkpoint and Flow-state read-back. Static skills, ordinary task-context selection, delegation and file-context cleanup are included as working-context controls, not automatically counted as experience-derived memory. External model, embedding and database implementations, hosted services, downstream application policy and provider-side retained state remain outside frozen implementation evidence. Their correctness and deployed security cannot be concluded.

The following table separates direct source inspection from supplied findings. Paths are SRC-1 commit-relative anchors. An uninspected row remains included and unresolved; it is not an absence claim.

| Entry point or operation | Source path / evidence | Coverage and limit |
|---|---|---|
| Crew task extraction; standalone output extraction | Direct: `lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py`, `lib/crewai/src/crewai/agent/core.py` | [MEM-RTE-memory-encoding](#mem-rte-memory-encoding); supplied [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail) supplies rejection ordering. |
| Public remember/remember_many and async wrappers | Direct bounded ranges: `lib/crewai/src/crewai/memory/unified_memory.py` | [MEM-RTE-memory-encoding](#mem-rte-memory-encoding). Async wrapper parity not exhaustively inspected. |
| Encoding, duplicate rejection, consolidation and fallback extraction | Direct: `lib/crewai/src/crewai/memory/encoding_flow.py`, `lib/crewai/src/crewai/memory/analyze.py` | [MEM-RTE-memory-encoding](#mem-rte-memory-encoding), [MEM-CLM-retention-limits](#mem-clm-retention-limits). Analysis helper exception branches beyond extraction were not fully read; their precise fallback policies remain unresolved. |
| Recall, shallow/deep selection, display, scope and slice | Direct: `lib/crewai/src/crewai/memory/recall_flow.py`, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/memory/memory_scope.py` | [MEM-RTE-memory-recall](#mem-rte-memory-recall). No hard security isolation or exhaustive filter correctness established. |
| Search memory / Save to memory, tool hooks | Direct: `lib/crewai/src/crewai/tools/memory_tools.py`; supplied hook mediation | [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-memory-encoding](#mem-rte-memory-encoding), [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch). |
| Storage reopening and backend replacement | Direct bounded ranges: `lib/crewai/src/crewai/memory/storage/lancedb_storage.py`, `lib/crewai/src/crewai/memory/storage/qdrant_edge_storage.py`, `lib/crewai/src/crewai/memory/storage/factory.py` | [MEM-OBJ-memory-content](#mem-obj-memory-content), [MEM-OBJ-memory-vector](#mem-obj-memory-vector). Qdrant constructor and operation inventory read, not complete merge/delete internals; cross-process durability, withdrawal and conflict semantics remain unresolved. |
| CLI memory inspection; reset command | Direct CLI dispatch/search and TUI operation inventory: `lib/cli/src/crewai_cli/cli.py`, `lib/cli/src/crewai_cli/memory_tui.py`; direct reset utility | [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). TUI details not fully read; inventory establishes inspection/recall rather than an authored editing workflow. |
| Knowledge source admission and task retrieval | Direct: `lib/crewai/src/crewai/knowledge/knowledge.py`, `lib/crewai/src/crewai/knowledge/storage/knowledge_storage.py`, `lib/crewai/src/crewai/knowledge/source/base_knowledge_source.py`, `lib/crewai/src/crewai/knowledge/source/string_knowledge_source.py`, `lib/crewai/src/crewai/agent/utils.py` | [MEM-RTE-knowledge-context](#mem-rte-knowledge-context). PDF, CSV, Excel, JSON, text-file and Docling parsers listed in the registry but not traced individually; exact preprocessing, provenance preservation and source-specific withdrawal cannot be concluded. Custom knowledge factory and RAG backend persistence remain uninspected. |
| Flow feedback lessons | Direct: `lib/crewai/src/crewai/flow/human_feedback.py`, `lib/crewai/src/crewai/flow/runtime/__init__.py`, DSL option search | [MEM-RTE-feedback-lessons](#mem-rte-feedback-lessons). Async feedback resumption into lesson storage not fully traced. |
| Training and skills | Supplied runtime only | Annotations on [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents), [RT-RTE-crew-training](runtime.md#rt-rte-crew-training), [RT-RTE-skill-disclosure](runtime.md#rt-rte-skill-disclosure). No independent reread of training/evaluator internals. |
| Overflow summary and task/delegation frames | Supplied runtime only | Annotations on [RT-RTE-context-summary](runtime.md#rt-rte-context-summary), [RT-RTE-agent-delegation](runtime.md#rt-rte-agent-delegation), [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff). Experimental/provider-specific compaction and opaque reasoning-payload preservation uninspected. |
| Kickoff output log and replay | Direct Crew replay; SQLite storage operation inventory: `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/memory/storage/kickoff_task_outputs_storage.py` | [MEM-RTE-output-replay](#mem-rte-output-replay). Full serialization fidelity not established. |
| Flow UUID state and pending feedback snapshots | Direct bounded SQLite source, supplied runtime reload | [MEM-OBJ-flow-state](#mem-obj-flow-state), annotation on [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution). Pending-feedback persistence schema inspected; full pause/resume cleanup and custom persistence contracts uninspected. |
| Event checkpoints, JSON and SQLite alternatives | Direct bounded: `lib/crewai/src/crewai/state/checkpoint_listener.py`, `lib/crewai/src/crewai/state/runtime.py`, `lib/crewai/src/crewai/state/provider/json_provider.py`; SQLite provider operation inventory | [MEM-OBJ-runtime-state](#mem-obj-runtime-state), [MEM-RTE-checkpoint-restore](#mem-rte-checkpoint-restore). Entity-specific opaque payloads, migration fidelity, SQLite pruning internals and CLI checkpoint command internals unresolved. |
| File inputs, tool-result caches, retrieval adapters and manual runners | Supplied boundary/runtime inventory, not independently traced here | Ordinary file cleanup and tool caching are described in supplied routes. `lib/crewai-files/`, `lib/crewai-tools/` and runner-specific retained-state consumers remain uninspected at memory-detail level; no complete system-wide retention or withdrawal claim follows. |

## Core ideas

1. **Retention transforms rather than merely logs.** Crew task execution extracts statements from task, role, expected output and result. Encoding can reject duplicates, infer organization, update existing text or delete records. The default retained object is not the complete execution transcript. Extraction failure is an important counterexample: it retains the full input blob instead. See [MEM-RTE-memory-encoding](#mem-rte-memory-encoding).
2. **Read-back has several owners.** Runtime automatically requests task memories; the foreground model can request Search memory; a caller can use the library directly. Selection combines vector search, scope/category/privacy filters and ranking, with optional model query analysis. These are not unsolicited independent memory agents. See [MEM-RTE-memory-recall](#mem-rte-memory-recall).
3. **Content and access metadata have different authority.** Text reaches later models as guidance. Scopes, IDs, scores, privacy flags and vectors govern selection. `MemoryMatch.format` does not expose every stored field, and consolidation reconstruction can discard provenance/privacy fields. Consequently a memory label is neither source authentication nor a guaranteed trust boundary. See [MEM-OBJ-memory-content](#mem-obj-memory-content), [MEM-OBJ-memory-metadata](#mem-obj-memory-metadata), [MEM-CLM-retention-limits](#mem-clm-retention-limits).
4. **Retained execution state is not all distilled memory.** Replay outputs, Flow snapshots and runtime checkpoints have symbolic reconstruction consumers; summaries and trained suggestions have later model consumers. The later consumer, not the storage label, determines their authority. See [MEM-RTE-output-replay](#mem-rte-output-replay), [MEM-RTE-checkpoint-restore](#mem-rte-checkpoint-restore) and the runtime annotations.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-content
Label: MemoryRecord textual content

Source-native identity: `MemoryRecord.content`, including extracted statements, full-content fallback, explicit caller/tool text and consolidated replacements. Representational form: natural language interpreted by encoding/review models and later task models. Substrate: the selected StorageBackend; built-in default LanceDB reopens a named table in a filesystem database. Qdrant Edge is an alternative with worker-local and central shard paths; a supplied backend or process-wide factory can replace these. Lineage is mixed: task traces can include user input, model outputs and expected-result instructions; explicit writes have caller-dependent provenance. No universal human authorship or approval follows. This object is distinct from runtime's trained suggestions and static skills: [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents), [RT-OBJ-skill](runtime.md#rt-obj-skill). Neither is its container.

SRC-1, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/memory/storage/lancedb_storage.py`, `lib/crewai/src/crewai/memory/storage/factory.py`, `lib/crewai/src/crewai/memory/storage/qdrant_edge_storage.py`.

> content: str = Field(description="The textual content of the memory.")
> --- `lib/crewai/src/crewai/memory/types.py`

> self._table: Any = self._db.open_table(self._table_name)
> self._vector_dim: int = self._infer_dim_from_table(self._table)
> --- `lib/crewai/src/crewai/memory/storage/lancedb_storage.py`

#### MEM-OBJ-memory-metadata
Label: MemoryRecord selection and provenance fields

Source-native identity: ID, scope, categories, importance, metadata, created/access times, source and private flag. Symbolic fields drive fixed filters/ranking; free metadata values may also be displayed to the model. Storage accompanies [MEM-OBJ-memory-content](#mem-obj-memory-content), but these fields are not the statement itself. Caller values, model-inferred fields and generated IDs/timestamps have distinct lineage. `source` is a caller-supplied identifier, not verified authorship. Privacy is recall filtering, with an explicit include-private override; default-null source has no authenticated principal semantics. The supplied runtime has no counterpart after comparison with [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents).

SRC-1, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/memory/unified_memory.py`.

> if not include_private:
>     raw = [
>         (r, s)
>         for r, s in raw
>         if not r.private or r.source == source
>     ]
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

#### MEM-OBJ-memory-vector
Label: MemoryRecord embedding

Source-native identity: `MemoryRecord.embedding`, dense numerical representation used by the storage search consumer, not model-readable reasoning. Representational form: distributed numerical representation; substrate: database vector field/shard alongside textual records. Produced from text by [RT-CMP-memory-embedder](runtime.md#rt-cmp-memory-embedder), not identical to that encoder component. Encoding embeds new content; replacements are re-embedded. Caller update can retain the existing vector when a new embedding is empty, so text/vector agreement is not guaranteed by every path. Encoder version, parameter mutability and endpoint limits are those of the supplied component; this object is output state, not updated encoder weights. Serialization excludes this field from the public model dump, while storage can retain it. SRC-1, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/memory/encoding_flow.py`, `lib/crewai/src/crewai/memory/unified_memory.py`.

> if content is not None:
>     updates["content"] = content
>     embedding = embed_text(self._embedder, content)
>     updates["embedding"] = embedding if embedding else existing.embedding
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

#### MEM-OBJ-knowledge-chunks
Label: Knowledge source chunks

Source-native identity: `BaseKnowledgeSource.chunks` and stored RAG documents. Natural-language chunks are distinct from backend-generated embeddings and symbolic collection/record metadata. Default KnowledgeStorage writes document content to a RAG client collection; its durable substrate depends on that client or custom storage, not necessarily unified-memory LanceDB. String source slicing defaults to 4000 characters with 200 overlap. Origins may be caller strings, files or external conversions; only the string path was traced completely. Metadata declared on the base source is marked unused, and the inspected storage save constructs content-only documents; rich source lineage must not be assumed. No counterpart in supplied runtime objects; [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff) merely identifies retrieval as a task preparation step. SRC-1, `lib/crewai/src/crewai/knowledge/source/base_knowledge_source.py`, `lib/crewai/src/crewai/knowledge/source/string_knowledge_source.py`, `lib/crewai/src/crewai/knowledge/storage/knowledge_storage.py`.

> rag_documents: list[BaseRecord] = [{"content": doc} for doc in documents]
> --- `lib/crewai/src/crewai/knowledge/storage/knowledge_storage.py:118-118`

#### MEM-OBJ-flow-state
Label: Persisted Flow state and pending feedback

Source-native identity: SQLiteFlowPersistence `flow_states.state_json` and separate `pending_feedback` context/state JSON columns. Symbolic JSON structure is consumed by Flow restoration; application fields may contain natural-language outputs or opaque strings. Substrate: SQLite `flow_states.db` by default, not vector memory. Each save appends a UUID/method/timestamp state row; latest ID selects reload. Pending feedback has a distinct unique-UUID row and retained review context; it is not a distilled lesson. Exact application payload lineage and downstream meaning depend on method bodies. Distinct object, not a duplicate of [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution), which describes the enclosing control route. SRC-1, `lib/crewai/src/crewai/flow/persistence/sqlite.py`.

> SELECT state_json
> FROM flow_states
> WHERE flow_uuid = ?
> ORDER BY id DESC
> LIMIT 1
> --- `lib/crewai/src/crewai/flow/persistence/sqlite.py`

#### MEM-OBJ-runtime-state
Label: RuntimeState checkpoint payload

Source-native identity: RuntimeState serialization with entities, event_record, CrewAI version and parent/branch lineage. Symbolic JSON is a reconstruction artifact; entity message text remains natural language at a later model consumer, and provider-specific hidden/opaque payload fidelity is unresolved. Default substrate is JSON files; a SQLite provider is also shipped. Raw execution/event state is not automatically consolidated into reusable advice. Compare [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff), [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff) and [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution): those are consumers, not duplicate objects. SRC-1, `lib/crewai/src/crewai/state/runtime.py`, `lib/crewai/src/crewai/state/provider/json_provider.py`.

> "entities": [e.model_dump(mode="json") for e in self.root],
> "event_record": self._event_record.model_dump(mode="json"),
> --- `lib/crewai/src/crewai/state/runtime.py`

### Routes

#### MEM-RTE-memory-encoding
Label: Memory extraction and encoding

Crew executor or standalone finalization produces a task/input-output blob; Memory's analysis LLM extracts statements. Caller/API writes and Save to memory bypass extraction but still use encoding. `remember` serializes through the save pool and waits; `remember_many` submits background work and returns an empty list. Encoding embeds, drops intra-batch near-duplicates, searches similar records, resolves missing scope/categories/importance and requests a consolidation plan when similarity crosses its threshold. Fully supplied fields with no sufficiently similar records take a no-LLM insertion branch. Code applies model-proposed keep/update/delete/insert plans, with first action per record winning; no separate human approval of each statement or consolidation is shown. The human may supply original content, but generic caller identity leaves that unresolved for explicit API writes. Operating mode is open-request retention, not an experiment; model analysis supplies no answer oracle.

Guidance comes from memory extraction/save/consolidation prompts selected through I18N and typed analysis schemas. The persisted results are content and organization, not necessarily the proposed action reasons. Read-only blocks remember; extraction can return no statements, dedup can drop entries and consolidation can decline insertion. HookAborted propagates; other extraction errors fall back to retaining the whole raw input. No transactional rollback of partially applied delete/update/insert is established. See [MEM-CLM-retention-limits](#mem-clm-retention-limits).

Distinct from [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff) and [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff): this is their retained-content transformation, also independently exposed through tools and API. Task rejection ordering remains owned by [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail).

- Immediate return: remember returns a record or None; remember_many returns [] before persistence completes; tool reports synchronous save or background submission.
- Later read-back: resulting records enter [MEM-RTE-memory-recall](#mem-rte-memory-recall), whose read barrier waits for pending saves.
- Delegated visibility: extractor receives task/input, role, expected result and output, not necessarily all tool turns; encoding LLM receives content, organizational candidates and similar stored text as appropriate.
- Selection predicate: configured memory, read-only flag, nonempty input, embedding similarity thresholds and model consolidation plan; executor also skips output containing its delegation-action marker.
- Invalidation or expiry: model consolidation can delete or replace prior records; explicit maintenance can withdraw them; no universal retention deadline established.
- Activation or effect: writes derived statements, raw fallback blobs and organization to storage; successful future behavior change is unobserved.
- Evidence limits: model compliance and semantic quality unobserved; provider internals and complete backend atomicity unresolved; background save can be abandoned during shutdown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py`, `lib/crewai/src/crewai/agent/core.py`, `lib/crewai/src/crewai/memory/unified_memory.py`, `lib/crewai/src/crewai/memory/encoding_flow.py`, `lib/crewai/src/crewai/memory/analyze.py`, `lib/crewai/src/crewai/tools/memory_tools.py`.

> raw = (
>     f"Task: {self.task.description}\n"
>     f"Agent: {self.agent.role}\n"
>     f"Expected result: {self.task.expected_output}\n"
>     f"Result: {output.text}"
> )
> extracted = memory.extract_memories(raw)
> --- `lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py`

> _logger.warning(
>     "Memory extraction failed, storing full content as single memory: %s",
>     e,
>     exc_info=False,
> )
> return [content]
> --- `lib/crewai/src/crewai/memory/analyze.py`

> if fields_provided and not has_similar:
>     self._apply_defaults(item)
>     item.plan = ConsolidationPlan(actions=[], insert_new=True)
> --- `lib/crewai/src/crewai/memory/encoding_flow.py`

#### MEM-RTE-memory-recall
Label: Memory recall and delivery

Runtime requests task-description recall at limit five; standalone kickoff recalls from input at limit twenty. Foreground Search memory supplies one or more model-chosen queries and requests twenty per query, deduplicating IDs across queries without a global twenty-result cap. A caller can also recall directly; that exposed capability alone establishes no additional consumer. Runtime caller details are supplied by [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff) and [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff).

Memory drains writes, joins root/request scopes and chooses shallow or default-deep retrieval. Shallow embeds the raw query and reranks returned candidates. Deep skips query analysis for short queries; otherwise the memory LLM proposes targeted queries, scopes and optional time cutoff. It embeds at most three queries, selects at most twenty candidate scopes, searches their combinations, filters time/privacy, ranks by semantic/recency/importance and truncates to requested limit. Low confidence/complexity can trigger budgeted exploration. That exploration requests extraction from top-five excerpts per finding, but re_search calls the same search operation with unchanged query embeddings/scopes; final synthesis ranks records rather than returning the extraction as a new authoritative answer. Thus “deep” does not establish semantic synthesis or adaptive query expansion in every route.

- Immediate return: ordered MemoryMatch objects; tools/runtime convert them to text.
- Later read-back: later task or tool-model invocation receives selected accumulated content, categories and non-null metadata; API-only callers have no specified later model consumer.
- Delegated visibility: match formatting includes score/content/categories/metadata, not full stored provenance/privacy fields, embedding, match reasons or evidence gaps.
- Selection predicate: caller/automatic query, depth, scopes/categories, privacy controls, embedding candidates, optional model analysis and composite ranking; slices merge oversampled per-scope results and deduplicate globally.
- Invalidation or expiry: recall can touch access timestamps unless read-only; deleted/replaced records affect later searches, not already-delivered prompt text; executor reset/summary controls invocation retention.
- Activation or effect: prompt or tool observation delivery is wired; semantic reliance and useful recall remain unobserved.
- Evidence limits: scope suggestions are sliced rather than visibly intersected with the caller prefix in filter_and_chunk; source is not general public-record filtering; backend correctness and strict isolation are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/crewai/src/crewai/memory/unified_memory.py`, `lib/crewai/src/crewai/memory/recall_flow.py`, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/memory/memory_scope.py`, `lib/crewai/src/crewai/tools/memory_tools.py`.

> queries = queries[:3]
> --- `lib/crewai/src/crewai/memory/recall_flow.py`

> selected_scopes = candidates[:20]
> self.state.candidate_scopes = selected_scopes
> --- `lib/crewai/src/crewai/memory/recall_flow.py`

> lines = [f"- (score={self.score:.2f}) {self.record.content}"]
> if self.record.categories:
>     lines.append(f"  categories: {', '.join(self.record.categories)}")
> if self.record.metadata:
>     for key, value in self.record.metadata.items():
>         if value is not None:
>             lines.append(f"  {key}: {value}")
> return "\n".join(lines)
> --- `lib/crewai/src/crewai/memory/types.py`

#### MEM-RTE-memory-maintenance
Label: Explicit memory maintenance

Library callers can update a record by ID, delete by criteria and reset a scoped or complete store. Caller proposes and decides these changes; whether a human directly approves the exact content is unresolved. Update bypasses consolidation, changing provided fields and re-embedding changed content. Forget/reset withdraw storage content. Read-only checks differ: update returns the unchanged object, whereas inspected forget/reset bodies call storage without testing read_only. Omission of Save to memory from tool registration is therefore not a universal store immutability guarantee. CLI reset discovers crews/flows, calls their reset APIs and reports progress. TUI dispatch offers inspection and recall; no complete editing admission workflow was traced.

- Immediate return: updated record, deletion count or reset completion; errors depend on call site/storage.
- Later read-back: subsequent recall observes surviving/revised store state; prior prompts and checkpoints are not retracted by these methods.
- Delegated visibility: explicit update fields, deletion predicates and scope; reset-all intentionally ignores root_scope.
- Selection predicate: ID, scope, category, age and metadata filters; CLI flags choose memory/knowledge/agent-knowledge/kickoff outputs or all.
- Invalidation or expiry: physical withdrawal/reset, not a retained rejection rationale or versioned rollback; reset drains pending writes before deletion.
- Activation or effect: mutates backend records; does not prove erasure from every shard, backup or earlier consumer.
- Evidence limits: Qdrant merge/deletion, concurrent API mutation races and custom backend withdrawal guarantees uninspected; CLI completion text is not verified erasure.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This independently exposed route is distinct from ordinary execution [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff). SRC-1, `lib/crewai/src/crewai/memory/unified_memory.py`, `lib/crewai/src/crewai/utilities/reset_memories.py`, `lib/cli/src/crewai_cli/cli.py`.

> return self._storage.delete(
>     scope_prefix=effective_scope,
>     categories=categories,
>     record_ids=record_ids,
>     older_than=older_than,
>     metadata_filter=metadata_filter,
> )
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

> with self._reset_lock:
>     self.drain_writes()
>     self._storage.reset(scope_prefix=None)
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

#### MEM-RTE-knowledge-context
Label: Knowledge ingestion and task context

Knowledge assigns storage and invokes each configured source's add. String source slices caller content; KnowledgeStorage creates/uses its collection and adds content documents. Caller configuration admits sources; no per-chunk human approval or truth check is shown. Author identity remains unresolved. During task preparation the agent generates a search query, requests agent and crew knowledge and appends extracted snippets to the prompt. This is open retrieval, not an answer-oracle experiment; the model/query score is not a factual validity gate. Reset deletes the selected collection; reconfiguration and reinsertion are the available inspected recovery surfaces, not version rollback.

- Immediate return: ingestion completes or raises; search returns snippets, with KnowledgeStorage errors logged and reduced to [].
- Later read-back: agent/crew knowledge queries during later tasks append stored textual snippets to the task prompt.
- Delegated visibility: source processor sees configured content; RAG client gets document text; foreground model receives extracted snippet context, not necessarily original files or source metadata.
- Selection predicate: generated query, agent/crew collections, configured result limit and score threshold; defaults differ between Knowledge.query and Crew.query_knowledge.
- Invalidation or expiry: collection reset affects future retrieval; no source-level retraction propagation or general automatic time expiry established.
- Activation or effect: retained chunks enter later prompts as knowledge context, not mandatory executable rules or verified facts.
- Evidence limits: only string preprocessing was fully traced; custom storage, vector provider/version and other parser lineage remain unresolved; no empirical retrieval/quality results.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Distinct from the enclosing [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff), which does not declare this ingestion mechanism. SRC-1, `lib/crewai/src/crewai/knowledge/knowledge.py`, `lib/crewai/src/crewai/knowledge/source/string_knowledge_source.py`, `lib/crewai/src/crewai/knowledge/storage/knowledge_storage.py`, `lib/crewai/src/crewai/agent/utils.py`.

> for source in self.sources:
>     source.storage = self.storage
>     source.add()
> --- `lib/crewai/src/crewai/knowledge/knowledge.py`

> if agent.agent_knowledge_context:
>     task_prompt += agent.agent_knowledge_context
> --- `lib/crewai/src/crewai/agent/utils.py:173-174`

#### MEM-RTE-feedback-lessons
Label: Flow feedback lesson retention

With learn enabled and memory present, Flow pre-reviews compatible method output against recalled lessons before human review. After feedback, code requests generalizable lessons from method name, output and raw feedback; structured output or parsed lines are admitted to unified memory without a separate human approval of every derived lesson. Human feedback is evaluative input, not a supplied expected-answer oracle. Open feedback handling uses the configured LLM and I18N distillation/pre-review prompts; empty lessons or empty feedback admit nothing. Non-strict failures preserve raw output or skip lesson storage; strict failures and HookAborted propagate. Subsequent encoding/withdrawal follows unified memory, not a separate lesson database.

Part of: [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution)

The part is the learn-enabled feedback transformation within the enclosing Flow route, not its arbitrary method execution or UUID restoration.

- Immediate return: current feedback result/outcome; lesson save is background submission; pre-review can return a revised same-type value.
- Later read-back: later compatible method output triggers recall query containing method name and rendered output, then the review LLM receives only matched record content as lessons.
- Delegated visibility: distiller sees output and human feedback; later reviewer sees output plus selected lesson strings, not the original feedback trace or consolidation reasons.
- Selection predicate: learn flag, non-null memory, nonempty feedback for storage; pre-review accepts strings or fully visible Pydantic models, skips hidden-value models and other output types; recall passes learn_source.
- Invalidation or expiry: unified-memory replacement/deletion/reset controls later lesson availability; no automatic lesson withdrawal after reviewer disagreement established.
- Activation or effect: code can replace current output with review-model output before human review; successful correction or durable benefit unobserved.
- Evidence limits: learn_source is a privacy/source argument, not a filter excluding other public memories; asynchronous pending-feedback continuation and custom feedback provider behavior not fully traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/crewai/src/crewai/flow/human_feedback.py`, `lib/crewai/src/crewai/flow/runtime/__init__.py`.

> query = f"human feedback lessons for {method_name}: {rendered}"
> matches = mem.recall(query, source=learn_source)
> if not matches:
>     return method_output
> --- `lib/crewai/src/crewai/flow/human_feedback.py`

> if lessons:
>     mem.remember_many(lessons, source=learn_source)  # type: ignore[union-attr]
> --- `lib/crewai/src/crewai/flow/human_feedback.py`

#### MEM-RTE-output-replay
Label: Stored task output replay

Crew replay loads kickoff outputs, locates and validates the requested task, uses supplied inputs or stored inputs, reconstructs preceding TaskOutputs and resumes task execution at the selected index. This is retained raw/structured output reuse, not consolidation or learned advice. SQLite output storage's inspected operation inventory serializes outputs and inputs as JSON; full serialization fidelity is unresolved. Caller decides replay target and optional input replacement. Validation can reject mismatched/ambiguous task identities; this is structural admission, not a truth oracle. No per-content human approval is implied by triggering replay.

Part of: [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)

This is an alternative entry into Crew task execution using stored prior results.

- Immediate return: CrewOutput from resumed execution, or invalid-replay error.
- Later read-back: reconstructed earlier task outputs become available to task-context aggregation during resumed execution.
- Delegated visibility: prior output description/role/raw/structured fields and messages are reconstructed; task context policy still determines actual model-visible text.
- Selection predicate: requested task ID, saved task identity validation, preceding indices and optional replacement inputs.
- Invalidation or expiry: kickoff-output reset withdraws future replay input; replay can overwrite execution logs; full history/rollback guarantees unresolved.
- Activation or effect: prior stored output becomes current Task.output and can affect later prompts; actual model reliance unobserved.
- Evidence limits: output handler/storage body not fully traced, no successful replay supplied, no exactly-once external-effect guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/memory/storage/kickoff_task_outputs_storage.py`.

> self.tasks[i].output = task_output
>
> self._logging_color = "bold_blue"
> return self._execute_tasks(self.tasks, start_index, True)
> --- `lib/crewai/src/crewai/crew.py`

#### MEM-RTE-checkpoint-restore
Label: Runtime checkpoint save and restore

Configured checkpoint events trigger serialization of prepared entities and event record. JsonProvider writes a branch/lineage-named file; configured pruning removes oldest files. Restore reads provider data, validates RuntimeState and carries checkpoint lineage forward. SQLite is an alternative provider; its complete internals were not traced. Caller selects checkpoint configuration/location; software serializes state without per-field human approval. This is recovery-state admission, not evaluation-guided knowledge revision or a reference-answer experiment. Stored state is distinct from [MEM-OBJ-flow-state](#mem-obj-flow-state)'s UUID snapshots. Supplied [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff), [RT-RTE-agent-kickoff](runtime.md#rt-rte-agent-kickoff) and [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution) establish later execution entry points; no single one contains the cross-runtime persistence mechanism.

- Immediate return: checkpoint location or restored RuntimeState; failures emit events and raise.
- Later read-back: explicit restore supplies reconstructed entities to Crew/Agent/Flow resumption, not semantic vector retrieval.
- Delegated visibility: serialized entity fields and event state; full provider-specific hidden payload and file-reference fidelity uninspected.
- Selection predicate: configured event triggers, explicit restore location and branch retention policy; identifier selection targets recovery state, not semantic content.
- Invalidation or expiry: max_checkpoints prunes old branch files; invalid state fails validation; no general compensation for external effects on restore.
- Activation or effect: reconstructs execution state and lineage; completed-method skipping versus UUID hydration differs as supplied runtime notes.
- Evidence limits: no exercised checkpoint, migration compatibility or hidden reasoning-token replay verified; SQLite/custom provider details and CLI restore internals remain unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/crewai/src/crewai/state/checkpoint_listener.py`, `lib/crewai/src/crewai/state/runtime.py`, `lib/crewai/src/crewai/state/provider/json_provider.py`.

> raw = provider.from_checkpoint(location)
> state = cls.model_validate_json(raw, **kwargs)
> state._provider = provider
> --- `lib/crewai/src/crewai/state/runtime.py`

### Claims

#### MEM-CLM-retention-limits
Label: Consolidation provenance and rejection limits

The implemented consolidation path can change content without preserving all provenance/privacy fields. New insertions copy resolved source/private, but the update reconstruction below does not supply them; MemoryRecord defaults are source=None and private=False. Hence a private sourced existing record updated through this branch is reconstructed with those defaults before storage.update. This is a source-supported counterexample to treating privacy labels as invariant through consolidation, not an observed data leak. Action reasons/insert_reason exist in the plan schema but the inspected persistence assembly does not put them into the retained record. Later MemoryMatch display also omits them. Code comments about a write lock do not establish transactional multi-operation rollback; the inspected execute_plans body calls delete/update/save successively without an encompassing visible lock context. Backend operations may lock individually.

Task output guardrail rejection is a different gate: supplied [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail) establishes executor memory saving before Task validation, while standalone finalization saves after its own guardrail. No general “only approved results are remembered” guarantee follows. SRC-1, `lib/crewai/src/crewai/memory/encoding_flow.py`, `lib/crewai/src/crewai/memory/types.py`, `lib/crewai/src/crewai/memory/analyze.py`.

> updated = MemoryRecord(
>     id=existing.id,
>     content=new_content,
>     scope=existing.scope,
>     categories=existing.categories,
>     metadata=existing.metadata,
>     importance=existing.importance,
>     created_at=existing.created_at,
>     last_accessed=now,
>     embedding=new_emb if new_emb else existing.embedding,
> )
> self._storage.update(updated)
> --- `lib/crewai/src/crewai/memory/encoding_flow.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-memory-context
Label: Recalled content to model context

Consumer: later task/standalone agent model, or model after Search memory. Channel: automatic prompt append or tool observation formatted from matches. Force: natural-language context/guidance, not proof, authenticated origin or mandatory compliance. Horizon: later invocations while records persist and within an invocation until reset/summary replacement. Source and minimum display passage are [MEM-RTE-memory-recall](#mem-rte-memory-recall); supplied [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff) establishes task delivery. Distinct from [RT-BAP-training-instructions](runtime.md#rt-bap-training-instructions): records are selected by recall rather than role-keyed imperative training suggestions.

#### MEM-BAP-feedback-review
Label: Retained lessons to output review

Consumer: Flow pre-review LLM, then human reviewer/downstream Flow consumers of its returned value. Channel: matched memory record contents placed in the review prompt with current output. Force: requested natural-language revision, followed by code adopting the returned compatible output; reliable improvement is not established. Horizon: later feedback-enabled method invocations while memory survives. Source and minimum passages: [MEM-RTE-feedback-lessons](#mem-rte-feedback-lessons). Distinct from [RT-BAP-training-instructions](runtime.md#rt-bap-training-instructions): different producer, selector and immediate review consumer.

## Annotations

#### On [RT-OBJ-trained-agents](runtime.md#rt-obj-trained-agents)

The pickle artifact's suggestions are derived memory, not the raw feedback trace. Evaluation fields and role indexing are symbolic; the selected suggestions are natural-language instructions. The supplied object and [RT-RTE-crew-training](runtime.md#rt-rte-crew-training) supply substrate, lineage, overwrite/failure cleanup and minimum passages. Later prompt construction consumes suggestions, not necessarily the retained score or original reasons. This is use-derived instruction retention even though provider weights are unchanged. Physical pickle decoding has separate process authority from the prompt guidance.

#### On [RT-RTE-crew-training](runtime.md#rt-rte-crew-training)

Raw initial outputs, feedback and revised outputs feed evaluator-produced suggestions; later prompts read suggestions by role. That is a trace-to-derived-instruction-to-consumer chain. Human feedback shapes the input; software admits evaluator output, so human task review is not approval of every stored instruction. The supplied evaluator/save/prompt passages ground this annotation. Actual quality improvement, formulated theory criticism and exercised self-improvement remain independently unestablished.

#### On [RT-RTE-context-summary](runtime.md#rt-rte-context-summary)

The supplied helper passage establishes raw history to model-produced summary to next model invocation. Storage is the mutable executor message list; retained summary text is natural language, whereas roles and file blocks have symbolic framing. Runtime code triggers on overflow, the summary model decides retained wording, system messages and files survive, and non-system history is replaced rather than retaining a guaranteed verbatim tail. No explicit reasons for omitted details or automatic verbatim reload are established by the supplied record. This is within-run retained memory, not merely ordinary turn accumulation. Checkpoint capture could preserve the resulting frame, but exact entity/opaque payload completeness remains unresolved in [MEM-RTE-checkpoint-restore](#mem-rte-checkpoint-restore).

#### On [RT-RTE-agent-delegation](runtime.md#rt-rte-agent-delegation)

The supplied selected-agent invocation passage grounds a separate task frame with selected task/context crossing inward and returned result crossing outward. Whole transcript visibility is withheld, but the callee's own memory/tools remain available. The frame analogy concerns context selection, not a sandbox: retained memory or external effects can escape, and returned prompt text is not a dereferenceable reference to the discarded frame. This route alone does not establish a separately persisted delegation transcript.

#### On [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff)

Supplied task.context aggregation controls which prior outputs cross task frames: explicit selections, accumulated outputs when unspecified, or none for false context. Executor messages reset unless resuming. File context cleanup is another working-context removal, not memory withdrawal. Retained memory and replay outputs can survive those removals through [MEM-RTE-memory-recall](#mem-rte-memory-recall) and [MEM-RTE-output-replay](#mem-rte-output-replay).

#### On [RT-RTE-skill-disclosure](runtime.md#rt-rte-skill-disclosure)

Catalog/label selection keeps full skill instructions outside context until requested, while inline/already-active skills may enter immediately. Tool loading returns instruction text by value, not a pointer to the source resource. This is static instruction/context loading in the supplied evidence, not a trace-fed skill-write route. Already-delivered text is not withdrawn by changing the external source. The supplied loader/tool passages ground this annotation; mutable registry/file content provenance remains unresolved.

#### On [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution)

UUID hydration selects latest persisted state, not a semantic subset or a guarantee that completed methods are skipped. Direct SQLite inspection adds [MEM-OBJ-flow-state](#mem-obj-flow-state): JSON snapshot rows and separate pending-feedback context/state. Application bodies consume restored fields under their own rules, so payload semantics and model authority are not uniform. The supplied persistence.load_state passage and the object's SELECT passage ground this annotation. Full pending-feedback cleanup/resume and custom persistence behavior remain uninspected; they cannot support an exactly-once or universal expiry conclusion.

## Write side

Acquisition has three distinct controls. Explicit content writers select statements through API or Save to memory; the initiating human's role is unresolved unless the caller is known. Runtime task/standalone finalization automatically selects an input/output blob for model extraction. Flow feedback combines a human evaluation with software/model distillation, not direct human authorship of each lesson. All enter [MEM-RTE-memory-encoding](#mem-rte-memory-encoding); [MEM-RTE-feedback-lessons](#mem-rte-feedback-lessons) is a separate upstream admission mechanism. Shipped tool hooks may veto a mediated tool invocation, but automatic saves and public API writes are not thereby universally mediated: [RT-CLM-tool-veto](runtime.md#rt-clm-tool-veto).

Encoding retains derived text, model-inferred organization and vectors; it can also retain raw blobs on extraction failure. The default model analysis component and embedding component are [RT-CMP-memory-llm](runtime.md#rt-cmp-memory-llm) and [RT-CMP-memory-embedder](runtime.md#rt-cmp-memory-embedder), not newly declared model identities. Fully supplied records can bypass model field resolution but still face consolidation when similar material exists. The plan schema includes reasons, yet the inspected record construction does not persist them as an audit trail. Consequently later content can be available without the grounds for its admission or replacement. This does not prove absence of theories or criticism in arbitrary stored text; it limits rationale-preservation claims about the mechanism.

Rejection occurs at several non-equivalent gates: read-only write checks, empty extraction, similarity dedup, consolidation insertion refusal and Task/standalone output validation. Task rejection is not transactional withdrawal of prior memory. Explicit update/forget/reset can edit or withdraw future retrieval material, but have different read-only checks and no demonstrated propagation to prior prompts, checkpoints or backups. These limits are recorded in [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance) and [MEM-CLM-retention-limits](#mem-clm-retention-limits).

Knowledge uses source admission and chunk storage rather than trace extraction: [MEM-RTE-knowledge-context](#mem-rte-knowledge-context). Training retains evaluated role suggestions rather than model weights, as annotated above. Summarization retains a compressed working frame for the next invocation. Replay logs, Flow state and runtime checkpoints retain raw/structured recovery material rather than necessarily edited advice. No common update, approval or cleanup policy can be inferred across those artifacts.

## Read-back

Automatic task recall is a runtime request followed by memory selection and prompt delivery. Foreground Search memory is a model request followed by the same selection and tool-observation delivery. Neither proves the returned memories changed behavior. Public recall alone supplies only an API affordance absent a named caller. [MEM-RTE-memory-recall](#mem-rte-memory-recall) distinguishes all three and gives budgets. Limits are counts, not a hard token budget; formatted arbitrary metadata can expand output length. Scope/slice wrappers add targeted selectors but do not prove authenticated tenants or immutable provenance.

Deep recall returns selected records, not automatically the intermediate exploration prose. Evidence-gap strings can exist on MemoryMatch yet are omitted by format, alongside original source/private fields and match reasons. Thus a source-native “evidence gap” or provenance label is not proof that the downstream agent saw a warning. The actual formatted content determines [MEM-BAP-memory-context](#mem-bap-memory-context).

Feedback pre-review consumes matched content strings before the human review step; original feedback and derivation reasons need not cross that boundary. Passing learn_source does not restrict public records to lessons. Knowledge retrieval separately appends selected snippets. Trained suggestions are loaded by role and appended imperatively. Summaries are pushed after overflow into the next invocation, preserving system/file material while replacing history. These routes have different selectors and different authority, even when each eventually produces natural-language context.

Replay and checkpoint consumers reconstruct symbolic execution state. UUID Flow reload selects latest state for an identifier; checkpoint restore reconstructs entities/event state; replay reconstructs prior TaskOutputs before scheduled continuation. They are targeted recovery reads, not semantic memory selection or automatic claim adoption. Exact opaque provider payload fidelity and pending-feedback resumption remain unresolved rather than being inferred from a readable JSON summary or filename.

## Integration issues

- **No supplied record correction is required.** The supplied distinction between Task post-save rejection and standalone pre-save guardrails survives direct source checks. [RT-RTE-output-guardrail](runtime.md#rt-rte-output-guardrail), [MEM-RTE-memory-encoding](#mem-rte-memory-encoding).
- **Containment, not duplicate identity:** feedback lesson processing is part of [RT-RTE-flow-execution](runtime.md#rt-rte-flow-execution); replay is an alternate retained-state entry into [RT-RTE-crew-kickoff](runtime.md#rt-rte-crew-kickoff). Their declarations carry Part of fields. Cross-runtime checkpoint persistence overlaps Crew/Agent/Flow restoration but is not wholly contained in one supplied route. [MEM-RTE-feedback-lessons](#mem-rte-feedback-lessons), [MEM-RTE-output-replay](#mem-rte-output-replay), [MEM-RTE-checkpoint-restore](#mem-rte-checkpoint-restore). No candidate duplicate object after comparison with supplied training/skill objects.
- **Consolidation privacy/provenance loss:** reconstruction omits source/private while preserving other fields. This prevents invariant privacy/provenance claims and needs to remain visible in synthesis, not be erased by the nominal schema contract. [MEM-CLM-retention-limits](#mem-clm-retention-limits), [MEM-OBJ-memory-metadata](#mem-obj-memory-metadata).
- **Scope and source limits:** deep query scope suggestions are not visibly intersected with request scope in the inspected selector, and source only gates private records. Strong scope confinement or lesson-only retrieval cannot be concluded. Backend-level filtering and arbitrary model suggestions were not tested. [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-feedback-lessons](#mem-rte-feedback-lessons).
- **Read-only is not universal immutability:** forget/reset omit the read_only test used by remember/update. Tool omission is narrower than backend withdrawal authority. [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance).
- **Deep exploration has limited downstream use:** re_search repeats unchanged selector inputs; final output ranks records and format drops evidence gaps. This prevents inferring a synthesized answer or downstream gap awareness from the labels alone. [MEM-RTE-memory-recall](#mem-rte-memory-recall).
- **Unresolved included alternatives:** Qdrant cross-process merge/delete semantics, non-string knowledge preprocessing and custom RAG persistence, async pending-feedback lesson continuation/cleanup, SQLite checkpoint pruning/migration and opaque provider payload reconstruction remain uninspected or only inventoried. Consequences and exact inspected paths are in the coverage table and [MEM-OBJ-flow-state](#mem-obj-flow-state), [MEM-OBJ-runtime-state](#mem-obj-runtime-state). They prevent complete durability, withdrawal, provenance and recovery-fidelity conclusions, not the positive wired routes established here.
- **Additional unresolved surfaces:** file-cache/retrieval-adapter retained-state consumers, TUI editing possibilities, async wrapper equivalence and provider-specific summary behavior are not fully traced. Supplied runtime control routes remain valid within their stated scope; no exhaustive system-wide retention inventory or no-other-routes claim is made.

## Limitations and checks

HEAD was rechecked as the exact frozen commit; Git status was clean. Source identity is the boundary's registered repository, not the mutable access path. The supplied invocation, governing types, collection and record contract were read completely, including bounded continuation reads. Analysis used source reading/search only: no target execution, tests, examples, model calls, dependency installation or external web evidence. Missing empirical evidence prevents observed activation, reliable recall, output-quality benefit and causal improvement conclusions; it does not negate wired transformation and consumer routes.

Source coverage is intentionally explicit about available-but-uninspected alternatives. No observed-run or causal-experiment layer is claimed. Runtime-only annotations rely on supplied records and their quotations, not fresh independent inspection. Deterministic validation: the supplied validate-output command passed after disambiguating two repeated sync/async quotations with validator-supplied checked ranges. The pass establishes format and quotation occurrence, not semantic correctness or job acceptance.
