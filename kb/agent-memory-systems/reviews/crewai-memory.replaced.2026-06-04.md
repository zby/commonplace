---
description: "CrewAI Memory review: unified vector memory with LLM extraction, scoped recall, task-output learning, tools, and LiteAgent prompt injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-01"
---

# CrewAI Memory

Replaced by [crewai-memory.md](./crewai-memory.md) on 2026-06-04.

CrewAI Memory is the memory layer inside crewAIInc's Python multi-agent framework. At this revision it is no longer the older short-term / long-term / entity split described in some ecosystem material; the implemented center is a unified `Memory` class with hierarchical scopes, LLM-assisted save analysis, vector retrieval, optional consolidation, agent/crew/flow integration, memory tools, and a LiteAgent path that injects recalled memories into the next LLM call.

**Repository:** https://github.com/crewAIInc/crewAI

**Reviewed commit:** [4dafb05735dfa0d6e265eaccbe784b820e8fbfad](https://github.com/crewAIInc/crewAI/commit/4dafb05735dfa0d6e265eaccbe784b820e8fbfad)

**Last checked:** 2026-06-01

## Core Ideas

**Memory is a standalone object, then wired into agents, crews, and flows.** `Memory` can be used directly with `remember`, `recall`, `forget`, `update`, `scope`, `slice`, `tree`, and category/scope inspection methods ([unified_memory.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/unified_memory.py)). `Crew(memory=True)` creates a `Memory` rooted under `/crew/<name>` and passes the crew embedder through; `Agent(memory=True)` creates a default agent memory; `Flow` auto-creates memory under `/flow/<name>` unless it is an internal memory flow ([crew.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/crew.py), [base_agent.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/agents/agent_builder/base_agent.py), [flow.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/flow/flow.py)).

**The retained unit is a scored, scoped `MemoryRecord`.** Each record carries content, scope, categories, metadata, importance, timestamps, optional source, privacy flag, and an embedding excluded from serialization ([types.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/types.py)). This gives CrewAI a single behavior-shaping artifact type rather than separate entity and episodic classes.

**Saving is an LLM-mediated encoding flow.** The encoding pipeline batch-embeds items, drops near-exact duplicates, searches for similar records, asks the LLM to infer missing scope/categories/importance/metadata, optionally asks for consolidation actions against similar records, then deletes, updates, or inserts records in storage ([encoding_flow.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/encoding_flow.py), [analyze.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/analyze.py)). If callers provide all fields and no similar record crosses the consolidation threshold, the path avoids the save-analysis LLM call.

**Recall combines vector search with scopes, recency, importance, and optional LLM query analysis.** Shallow recall embeds the query and searches once. Deep recall can analyze long queries into up to three recall queries, infer scopes and time filters, search across candidate scopes in parallel, route low-confidence or complex queries through one LLM extraction round, deduplicate results, then compute a composite semantic/recency/importance score ([recall_flow.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/recall_flow.py), [types.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/types.py)).

**Storage is pluggable but database-first.** The default memory backend is LanceDB under `$CREWAI_STORAGE_DIR/memory` or CrewAI's platform app-data directory; it stores rows with JSON-encoded categories/metadata, vector, timestamps, source, private flag, scope index, locking, retries, and background compaction ([lancedb_storage.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/storage/lancedb_storage.py), [paths.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai-core/src/crewai_core/paths.py)). The alternate `qdrant-edge` backend uses worker-local shards plus a central shard, merging reads and flushing local writes on close ([qdrant_edge_storage.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/storage/qdrant_edge_storage.py)).

**Agents get both memory tools and automatic trace learning.** When a crew resolves tools for a task, it adds `Search memory` and, unless read-only, `Save to memory` tools for the agent's memory or the crew memory ([crew.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/crew.py), [memory_tools.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/tools/memory_tools.py)). After a normal Crew agent finishes, the executor builds a trace-like text from task description, agent role, expected result, and output, extracts discrete memories with the LLM, and saves them under an agent-specific scope when crew memory has a root scope ([base_agent_executor.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py)).

**Context efficiency is active but not absolute.** The system has scopes, slices, read-only views, recall limits, oversampling, query-analysis skipping for short queries, candidate-scope caps, category filters, privacy filters, and `remember_many` batch operations. But selected memories are still injected or returned as prose lists, and recall quality depends on embedding model, LLM analysis, stored scope quality, and whether the host uses automatic injection or only tools.

## Artifact analysis

- **Storage substrate:** `vector` — LanceDB rows by default, or Qdrant Edge points when `storage="qdrant-edge"` is configured
- **Representational form:** `prose` `symbolic` `parametric` — prose content, symbolic scope/categories/metadata/importance/timestamps/source/private fields, and embeddings
- **Lineage:** `authored` `imported` `trace-extracted` — records can be authored directly, imported through Knowledge sources, or extracted from agent/task and LiteAgent outputs
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `ranking` `learning` — memories act as evidence/context, prompt-injected advice, read-only/access-constrained tool surfaces, scope routing, retrieval ranking, and LLM-mediated mutation inputs

**Memory records.** Storage substrate: LanceDB rows by default, or Qdrant Edge points when `storage="qdrant-edge"` is configured. Representational form: mixed symbolic/prose/distributed-parametric records: prose content, symbolic scope/categories/metadata/importance/timestamps/source/private fields, and embeddings. Lineage: authored directly through `remember`, trace-extracted through agent and LiteAgent outputs, flow-authored through `Flow.remember`, or updated/deleted by consolidation and explicit operations. Behavioral authority: knowledge artifact when read as evidence/context; ranking influence when embedding similarity, recency, importance, scopes, categories, and privacy filters decide what reaches the agent; advisory system-definition material when injected into prompts or returned by the memory tool.

**Encoding analyses and consolidation plans.** Storage substrate: transient flow state, with durable effects applied to memory storage. Representational form: symbolic LLM outputs constrained by Pydantic schemas: suggested scope, categories, importance, extracted metadata, and keep/update/delete/insert decisions. Lineage: derived from new content, existing scopes/categories, and similar memory records. Behavioral authority: learning and mutation authority, because these decisions determine where memories are stored, whether old memories are updated or deleted, and which metadata will later steer retrieval. They are not retained as auditable review artifacts.

**Hierarchical scopes, slices, and root scopes.** Storage substrate: scope strings stored on records plus runtime `MemoryScope` and `MemorySlice` view objects. Representational form: symbolic path prefixes. Lineage: user-authored, LLM-inferred during save, or framework-derived from crew/flow/agent names. Behavioral authority: routing and access authority; scopes constrain search, write placement, reset, and read-only sliced views ([memory_scope.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/memory_scope.py), [utils.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/memory/utils.py)).

**Memory tools.** Storage substrate: runtime tool objects injected into an agent's tool list. Representational form: symbolic tool schemas plus prose descriptions from translations. Lineage: generated whenever a task has resolved memory. Behavioral authority: system-definition artifacts with tool-execution force: they define the commands the agent can call for pull recall and explicit save. In read-only memory, the save tool is omitted, so the view's authority changes the tool surface.

**LiteAgent injected memory block.** Storage substrate: not stored separately; it is an assembled prompt fragment produced from recalled records. Representational form: prose list formatted into the system message with a warning that automatic memories may be incomplete. Lineage: derived at call time from the last user message, current memory contents, and recall scoring. Behavioral authority: push advisory context, because the agent receives it before answering without needing to call the memory tool ([lite_agent.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/lite_agent.py), [en.json](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/translations/en.json)).

**Knowledge sources and RAG storage.** Storage substrate: separate Knowledge storage, defaulting to the global RAG client, which defaults to persistent ChromaDB; Qdrant is also available through the RAG abstraction. Representational form: source chunks and embeddings. Lineage: imported from strings, files, PDFs, CSV/Excel/JSON, or docling sources, then saved as vector-store documents. Behavioral authority: knowledge artifact context for agent/crew queries, not the same system as unified Memory, though reset commands and docs place them near each other ([knowledge.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/knowledge/knowledge.py), [knowledge_storage.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/knowledge/storage/knowledge_storage.py), [chromadb/config.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/rag/chromadb/config.py)).

The main promotion path is task or conversation trace -> LLM extraction into discrete memory statements -> LLM field analysis and optional consolidation -> durable vector record -> tool recall or prompt injection. CrewAI can also move authored knowledge sources into vector retrieval, but that is ingestion rather than trace-derived learning.

## Comparison with Our System

| Dimension | CrewAI Memory | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory for agent executions, crews, LiteAgents, and flows | Git-tracked methodology KB for agents and maintainers |
| Main substrate | LanceDB/Qdrant Edge memory records; Chroma/Qdrant RAG for knowledge | Markdown files, source snapshots, schemas, scripts, generated indexes |
| Retained unit | `MemoryRecord` with content, scope, categories, metadata, importance, timestamps, embedding | Typed notes/reviews/instructions with frontmatter, links, status, citations |
| Learning path | Agent/task output -> LLM extracted memories -> vector records | Source/workshop artifacts -> reviewed notes/instructions -> validation and review gates |
| Read-back | Pull tools plus LiteAgent engineered prompt injection | Mostly deliberate pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Runtime scopes, privacy flag, read-only slices, reset commands, events | Collection contracts, type specs, validation, semantic review, git lifecycle |

CrewAI is a runtime memory layer; Commonplace is a durable knowledge base. CrewAI optimizes for getting remembered facts back into an agent loop with minimal user ceremony. Commonplace optimizes for source-pinned claims, reviewability, and controlled promotion of artifacts with different behavioral authority.

The strongest overlap is the artifact split. CrewAI's memory records, scopes, embeddings, tool schemas, and injected prompt blocks already occupy different substrates, forms, lineage paths, and authority levels. The system becomes confusing only when these are flattened into "memory." A `MemoryRecord` inspected by a human is a knowledge artifact; the same record selected into a system prompt becomes advisory system-definition material; an LLM consolidation plan carries mutation authority even though it is transient.

CrewAI is ahead of Commonplace on runtime activation. Its LiteAgent can retrieve and inject memories before a response, and its ordinary agent loop exposes memory as tools without the developer writing those tools manually. Commonplace is ahead on retained lineage: a review or note keeps source URLs, status, and git diff history, while CrewAI's derived memories do not retain the extraction prompt version, exact source excerpt, consolidation rationale, or review state as durable first-class fields.

**Read-back:** `both` — CrewAI has pull read-back through `Search memory`, `Memory.recall`, scopes, flows, and knowledge queries; it has engineered push activation in LiteAgent, where the last user message triggers instance-targeted inferred/embedding recall and prompt injection before the LLM call

### Borrowable Ideas

**Make runtime memory views explicit.** Ready as design language. CrewAI's `MemoryScope` and read-only `MemorySlice` are a useful way to represent "this consumer may read/write only this subset." Commonplace could use the same vocabulary for generated context packs or workshop-scoped views, without changing the file substrate.

**Separate extraction from storage.** Ready now. `extract_memories()` is a pure helper before `remember()`, which keeps "what should be retained" distinct from "where and how it is stored." Commonplace review workflows already benefit from this split; it is worth naming as a pattern.

**Treat automatic prompt memory as incomplete by design.** Ready now for any future push context. CrewAI's injected memory text warns the model that automatic selection may be incomplete and tells it to use the search tool for counting/listing tasks. Commonplace could apply the same caution to generated context bundles.

**Use a read-only memory surface for derived context.** Worth borrowing when Commonplace exposes generated bundles to agents. A read-only slice can safely provide evidence without granting mutation authority.

**Do not borrow unaudited consolidation.** CrewAI lets an LLM decide updates/deletes against similar memories. That is pragmatic for runtime memory, but Commonplace should keep durable note edits and warning acknowledgments behind explicit review, validation, or semantic gates.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` — task/conversation bundles from Crew agent completion and LiteAgent calls provide the source signal for extraction.
**Learning scope:** `per-task` `cross-task` — extraction is triggered from individual task or call results, then retained under crew/agent/flow scopes for later tasks or runs.
**Learning timing:** `online` — memory extraction and LiteAgent saving happen in the runtime path after the producing task or answer.
**Distilled form:** `prose` `symbolic` `parametric` — reusable memory statements become prose content with symbolic fields and embeddings in `MemoryRecord` storage.

**Trace source.** CrewAI qualifies as trace-derived learning. The ordinary Crew agent executor captures task description, agent role, expected output, and final result, then feeds that trace-like bundle to memory extraction. LiteAgent captures the last user message, agent role, and final output. Flows can also call `remember` or `extract_memories` from application code, but the automatic trace-derived path is clearest in the agent executors.

**Extraction.** Extraction is LLM-mediated. `extract_memories_from_content` asks for discrete, reusable statements and falls back to storing the full content as one memory if the extraction call fails. The later encoding flow may run additional LLM analysis for scope, categories, importance, metadata, and consolidation against similar existing memories.

**Scope and timing.** Crew extraction happens after task completion, so it cannot affect the task that produced it. LiteAgent injection happens before answering, and LiteAgent saving happens after the answer. Crew memory roots are crew-scoped and, for automatic saves, agent-scoped under the crew root; Flow memory is flow-scoped by default; standalone memory has whatever scope the caller or LLM assigns.

**Authority transition.** The raw task/conversation trace is not the durable memory object. The distilled memory statement becomes a durable `MemoryRecord` and later acts as evidence, advisory context, or ranking input. The encoding/consolidation plan is a transient learning-control artifact with stronger authority than a retrieved memory because it can update or delete prior records.

**Survey placement.** CrewAI belongs in the trace-to-vector-memory family with LLM extraction and LLM-assisted consolidation. It strengthens the survey distinction between raw traces and distilled retained artifacts: CrewAI does not simply replay task history; it extracts reusable statements, scores them, scopes them, and recalls them by semantic/recency/importance signals. It also shows the risk of runtime trace learning without durable lineage: useful memories can persist without source snippets, extraction prompt versions, or review status.

## Read-back placement

**Direction.** Both. Pull paths include `Memory.recall`, Flow `recall`, `Search memory`, and `query_knowledge`. Push paths are narrower: LiteAgent automatically recalls from the last user message and appends relevant memories to the system message before the LLM call. Ordinary Crew agents get memory tools and post-task saving, but I did not find a source-visible general Crew task pre-prompt injection path equivalent to the LiteAgent path.

**Read-back signal:** `inferred / embedding` `inferred / judgment` — LiteAgent push is keyed by the last user message through vector recall, with deep recall able to add LLM query analysis.
**Faithfulness tested:** `no` — this review found observable prompt insertion but no with/without ablation proving downstream behavioral use.

**Targeting and signal.** LiteAgent's trigger is a pending LLM call with memory configured, but the memory push is not a coarse always-load: it is `targeting: instance`, keyed by the last user message for this call. The signal is `inferred / embedding` as the primary selector: `_inject_memory_context()` passes the last user message to `memory.recall(query, limit=10)`, and recall embeds the query or LLM-distilled recall queries before vector search. Deep recall can add an LLM `judgment` layer by analyzing longer queries into scopes, time filters, and up to three recall queries, then confidence-routing low-confidence or complex cases; scopes/categories/privacy/recency/importance shape filtering and ranking. Precision, recall, context dilution, and effective authority are runtime properties, not established by the code alone.

**Injection point.** LiteAgent retrieval happens after messages are formatted and before `_execute_core` invokes the LLM, so it can change the next answer. Crew agent auto-saving happens after the task result and only affects future tasks or future runs. Memory tools can affect an action only if the agent chooses or is prompted to call them during its reasoning loop.

**Selection, scope, and complexity.** LiteAgent caps injected recall at 10 matches. General recall defaults to limit 10, oversamples vector results, caps distilled queries at three, caps candidate scopes at 20, and can filter by scope, categories, source, private flag, and time cutoff. The injected representation remains a prose bullet list; complex or enumerative tasks are explicitly warned not to trust the automatic set as complete.

**Authority at consumption.** The LiteAgent memory block is advisory prompt context, not a hard gate. Memory tools are stronger as executable capabilities: `Search memory` and `Save to memory` let the agent pull or write retained state. `MemorySlice(read_only=True)` removes the save tool, proving that the read path can reduce mutation authority.

**Faithfulness.** The code emits memory retrieval and save events and includes tests elsewhere for memory behavior, but this review did not find an implementation-level with/without ablation proving that injected memories causally improve agent behavior. Presence in the prompt is observable; correct use by the model is not guaranteed.

**Other consumers.** Humans can inspect memory through `tree`, `info`, `list_records`, `list_categories`, reset commands, events, and storage files if they know the backend. Observability listeners can consume memory events. These are operational surfaces, not strong review surfaces for the truth of a retained claim.

## Curiosity Pass

The docs say "before each task, the agent recalls relevant context from memory and injects it into the task prompt," but the source-visible Crew path I found adds memory tools and saves after task execution; automatic pre-call prompt injection is visible in LiteAgent ([memory docs](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/docs/en/concepts/memory.mdx), [crew.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/crew.py), [lite_agent.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/lite_agent.py)). That matters for classification: Crew memory is pull-capable by default; LiteAgent memory is engineered push.

The old memory taxonomy survives as reset aliases only. `long`, `short`, `entity`, and `external` are mapped to unified `memory` in reset handling, while the implemented retained artifact is the unified `MemoryRecord` ([crew.py](https://github.com/crewAIInc/crewAI/blob/4dafb05735dfa0d6e265eaccbe784b820e8fbfad/lib/crewai/src/crewai/crew.py)).

The Knowledge system is adjacent but separate. It uses knowledge sources and RAG storage for imported reference material; unified Memory uses LanceDB/Qdrant Edge and stores learned records. Both can influence an agent, but their lineage and authority differ.

Consolidation is powerful and under-audited. A failed LLM extraction degrades to storing the full content, which preserves signal; a successful consolidation can update or delete previous records without retaining the deliberation as a reviewable artifact.

The context-efficiency story has two layers: backend selection narrows candidates, then prompt assembly still dumps selected content as prose. The system controls volume better than complexity.

## What to Watch

- Whether ordinary Crew task execution gains the same source-visible pre-prompt memory injection as LiteAgent. That would broaden `push-activation` from a LiteAgent path to the central Crew path.
- Whether `MemoryRecord` gains durable source-excerpt, extraction-prompt, consolidation-plan, and review-status fields. That would make trace-derived memories more auditable and more comparable to Commonplace notes.
- Whether consolidation decisions become inspectable events or retained proposals before mutation. That would reduce hidden authority drift.
- Whether Memory and Knowledge converge or stay separate. If they converge, reviews should re-check storage substrate, lineage, and reset semantics because imported reference documents and learned task memories have different trust requirements.
- Whether the warning in the injected memory block evolves into a real faithfulness or coverage test for enumerative tasks. That would turn a prompt caution into measurable governance.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: CrewAI distills task and LiteAgent traces into scoped vector memory records.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Crew memory storage becomes pull tools by default, while LiteAgent has a source-visible push path.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: CrewAI extracts reusable statements from task results before storing them.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: memory records, tools, injected prompt blocks, scopes, and consolidation plans carry different behavior-shaping force.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - applies: CrewAI shows the same retained fact moving between evidence, advisory prompt context, ranking influence, and mutation input.
