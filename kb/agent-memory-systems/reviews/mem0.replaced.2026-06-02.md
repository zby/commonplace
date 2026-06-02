---
description: "Mem0 review: V3 ADD-only trace extraction into vector memories, entity-link retrieval boosts, plugin hooks, and legacy CRUD prompt remnants"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-30"
---

# Mem0

> Replaced 2026-06-02. See [mem0](./mem0.md) for the current review.

Mem0, from mem0ai, is a production memory layer for AI assistants and agents. At the reviewed commit, the inspected OSS path is no longer the older two-phase "extract facts, then LLM-judge ADD/UPDATE/DELETE/NOOP" pipeline described in earlier coverage. The live `Memory.add()` path is V3 ADD-only extraction: it retrieves nearby existing memories for deduplication and linking context, asks one LLM prompt to extract new memories, inserts only new vector records, writes ADD history, and builds an entity-link side index for retrieval boosts.

**Repository:** https://github.com/mem0ai/mem0

**Reviewed commit:** [a3154d59e52386d4e1189c1f5f44819868f76514](https://github.com/mem0ai/mem0/commit/a3154d59e52386d4e1189c1f5f44819868f76514)

**Last checked:** 2026-05-30

## Core Ideas

**The current add path is additive, not CRUD reconciliation.** `Memory.add()` normalizes messages, rejects unsupported memory types except procedural memory, and then calls `_add_to_vector_store()` for ordinary memory writes ([memory main](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py)). The function's own comment names the "V3 phased batch pipeline": gather session context, retrieve relevant existing vector memories, pass those memories plus recent messages into `ADDITIVE_EXTRACTION_PROMPT`, parse `{"memory": [...]}`, embed extracted text, skip hash duplicates, insert records, write ADD history, link entities, and save recent messages. There is no LLM call in this path that chooses UPDATE or DELETE. The README says the same: the April 2026 algorithm changed to "Single-pass ADD-only extraction" with "no UPDATE/DELETE" ([README](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/README.md)).

**The older CRUD policy still exists as prompt code but is not wired into `Memory.add()`.** `DEFAULT_UPDATE_MEMORY_PROMPT` and `get_update_memory_messages()` still describe a smart memory manager that returns ADD, UPDATE, DELETE, or NONE decisions ([prompts](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/prompts.py)). The active `Memory` class imports the additive prompt and prompt builder, not `get_update_memory_messages()` ([memory main](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py)). UPDATE and DELETE remain direct API methods: `update()` embeds the supplied replacement text, overwrites the vector payload, records UPDATE history, and relinks entities; `delete()` removes the vector and records DELETE history. That is explicit user/API mutation, not automatic LLM-judged reconciliation.

**The extraction prompt has become the main memory policy artifact in the reviewed default path.** `ADDITIVE_EXTRACTION_PROMPT` is long, normative, and highly specific: extract from both user and assistant messages, preserve concrete details, ground relative time to the observation date, avoid echo extraction, return only JSON, and link new memories to related existing memory IDs ([additive prompt](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/prompts.py)). The prompt builder supplies summary, last messages, recently extracted memories, existing memories, new messages, observation date, current date, and optional custom instructions ([prompt builder](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/prompts.py)). The governing policy is therefore readable prose prompt plus surrounding Python control flow, not learned weights or a database trigger.

**Storage is vector-first with SQLite history and a second entity vector collection.** `MemoryConfig` has vector store, LLM, embedder, history DB path, optional reranker, version, and custom instructions; it has no `graph` or `graph_store` field in the inspected OSS config ([config](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/base.py)). Vector providers are loaded through `VectorStoreFactory`, with many database backends including Qdrant, pgvector, Milvus, Redis, Elasticsearch, FAISS, S3 Vectors, and Neptune Analytics ([factory](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/utils/factory.py)). SQLite stores local operation history and recent messages ([storage](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/storage.py)). Entities are extracted with spaCy heuristics, stored in `{collection}_entities`, and linked to memory IDs for later boosts ([entity extraction](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/utils/entity_extraction.py), [memory main](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py)).

**Graph memory has been replaced in the current OSS path by entity linking.** No graph-store package appears under `mem0/`, and the current config has no graph field. The bundled Mem0 skill says V3 replaces graph memory with entity linking and instructs users to remove `enable_graph` and `graph_store` from old configurations ([skill docs](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/skills/mem0/SKILL.md), [features](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/skills/mem0/references/features.md)). Neptune Analytics is present, but as a vector-store adapter that stores vectors on graph nodes and runs vector top-k queries, not as a first-class relation extraction layer ([Neptune vector store](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/vector_stores/neptune_analytics.py)).

**Read-back is usually search, but wrappers and hooks can push memory into agent context.** The plain library surface exposes `search(query, filters, top_k, threshold, rerank)` and returns ranked memory records ([memory main](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py)). The proxy `Chat.Completions.create()` wrapper fetches relevant memories before the LLM call and rewrites the last user message with "Relevant Memories/Facts" and entities ([proxy](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/proxy/main.py)). OpenMemory exposes MCP tools whose descriptions tell agents to add memories when useful and search "EVERYTIME the user asks anything"; those descriptions are high-authority retrieval guidance, not automatic injection by themselves ([OpenMemory MCP](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/openmemory/api/app/mcp_server.py)). The Codex/Claude/Cursor plugin adds lifecycle hooks that inject search rubrics, resume context, error/file-path cues, and save nudges at user-prompt time, and auto-captures transcript windows every third substantial message ([hooks](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/hooks/codex-hooks.json), [user prompt hook](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/on_user_prompt.sh), [auto capture](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/auto_capture.py)).

## Comparison with Our System

| Dimension | Mem0 | Commonplace |
|---|---|---|
| Primary artifact | Extracted memory strings with payload metadata, embeddings, hashes, entity links, and operation history | Typed Markdown notes, source snapshots, instructions, ADRs, reports, schemas, and generated indexes |
| Storage substrate | Vector store plus SQLite history/messages; OpenMemory adds SQLAlchemy app/user/memory state | Git-tracked files plus deterministic scripts and generated indexes |
| Representational form | Prose memory text, symbolic metadata/history/categories, embeddings, entity-link vectors, prompt policy | Mostly prose with frontmatter, authored links, type specs, validation scripts, and review artifacts |
| Lineage | Operation history per memory ID and hashes, but weak trace-to-extracted-fact provenance | Source citations, git history, type contracts, archive/replacement lifecycle, validation reports |
| Activation | Library search, proxy pre-call injection, MCP tool use, plugin prompt hooks | `rg`, indexes, links, instructions, skills, validation and review commands |
| Authority | Extraction prompt, filters, ranking score, entity boosts, MCP descriptions, lifecycle hooks | Collection contracts, AGENTS.md, skills, type specs, schemas, review gates |

Mem0 is stronger than commonplace as an application memory service. It gives app developers a simple add/search/update/delete API, many vector backends, hosted and self-hosted surfaces, MCP tools, browser/editor integrations, and prompt hooks. Commonplace is stronger as an inspectable knowledge system. A Mem0 memory is easy to retrieve but hard to review as a claim, connect with a typed reason, promote into an instruction, or retire through a visible replacement trail.

The current V3 design is less curatorial than earlier Mem0 coverage implied. Older Mem0 looked like a fact-level curation system: extract facts, compare to existing facts, then ADD/UPDATE/DELETE/NOOP. The reviewed code now accumulates new memories and relies on deduplication, linking, scoring, explicit API mutation, and optional user-invoked cleanup. This moves Mem0 closer to trace-derived accumulation with retrieval-time ranking than to automatic memory consolidation.

The graph claim also needs narrowing. The reviewed OSS implementation is not vector store plus optional graph memory in the old Neo4j/Memgraph/Kuzu sense. It is vector memory plus entity extraction and entity-linked boosting, with Neptune available as a graph-backed vector adapter. Entity linking improves retrieval but does not create a navigable, inspectable knowledge graph with typed relationship claims.

Mem0's most important authority surface is the extraction prompt. It acts like a system-definition artifact: it decides what counts as memory, what gets skipped, how detail should be preserved, and how assistant-generated material is attributed. The stored memory rows are knowledge artifacts when read as context; embeddings, filters, entity boosts, rerankers, MCP descriptions, and prompt hooks are system-definition artifacts because they route, rank, inject, or instruct later behavior.

## Borrowable Ideas

**Treat extraction prompt policy as a first-class artifact.** Ready to borrow. Mem0's additive prompt is not merely glue; it is the memory policy. Commonplace should continue making extraction and review policies readable, versioned, and reviewable rather than hiding them in helper code or model weights.

**Use entity linking as a compiled retrieval aid, not as the source of truth.** Worth borrowing if commonplace grows a search layer. Mem0's entity side collection is a lightweight way to improve recall for named things without claiming to maintain a full graph. In commonplace it would belong as a generated index tied back to notes, not as canonical knowledge.

**Separate explicit mutation from automatic extraction.** Useful as a caution. Mem0 V3 avoids automatic overwrite/delete mistakes by making default extraction ADD-only. That reduces destructive errors but increases accumulation pressure. Commonplace already prefers explicit review before authority changes; Mem0 shows the service-side version of the same tradeoff.

**Hook-based memory activation.** Worth tracking. The plugin's prompt hooks are closer to how memory should work for agents than a passive search tool alone: they notice resume/error/file-path contexts and can inject cues before the agent acts. Commonplace skills and instructions could borrow this shape when a cue is cheap and specific.

**Do not borrow unreviewed memory accumulation as KB learning.** Mem0 is excellent at retaining personalized facts, but its default pipeline does not synthesize theories, restructure a corpus, or produce governed instructions. It should be treated as a retrieval substrate or candidate-memory layer, not a replacement for reviewed notes.

## Trace-derived learning placement

**Trace source.** Mem0 qualifies as trace-derived learning in its default `Memory.add(..., infer=True)` conversational path and surrounding wrappers. The source traces are conversation messages passed to `Memory.add()`, chat completions wrapped by `mem0.proxy`, OpenMemory MCP calls, and plugin-captured transcript windows from user-prompt and pre-compaction hooks ([memory main](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py), [proxy](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/proxy/main.py), [auto capture](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/auto_capture.py), [pre-compact capture](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/on_pre_compact.py)). Direct raw storage, explicit `update()`, and explicit `delete()` are real memory paths but are not trace-derived extraction by themselves.

**Extraction.** The default extraction oracle is an LLM answering `ADDITIVE_EXTRACTION_PROMPT`, with nearby existing memories, recent messages, and observation date supplied as context. The output is a list of new memory texts plus attribution and optional linked memory IDs. The older CRUD oracle exists as prompt text, but the reviewed `add()` path does not call it.

**Storage substrate.** Distilled memory text, metadata, hashes, timestamps, and embeddings live in the configured vector store. Local operation history and recent messages live in SQLite. Entities live in a parallel vector collection. OpenMemory adds relational users, apps, memory states, categories, access controls, status history, and access logs ([OpenMemory models](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/openmemory/api/app/models.py)).

**Representational form.** Raw traces are chat/transcript records. Extracted memories are prose knowledge artifacts wrapped in symbolic metadata. Hashes, filters, categories, state enums, app/user IDs, and operation history are symbolic. Embeddings and vector scores are distributed-parametric retrieval state. Entity links are mixed: entity text and linked memory IDs are symbolic, while matching is embedding-based.

**Lineage.** Lineage is operational but not semantically complete. Each memory has a hash, timestamps, payload metadata, and history rows for ADD/UPDATE/DELETE. OpenMemory mirrors memory state and access logs. But a future reviewer cannot reconstruct the exact source message span, prompt version, model response, or human approval state for each extracted memory from the default OSS records alone.

**Behavioral authority.** Stored memories advise future agents when retrieved. Search filters, ranking, entity boosts, rerankers, MCP tool descriptions, and lifecycle hooks have routing and activation authority. The extraction prompt has write-policy authority. The plugin's `dream` skill can ask an agent to consolidate memories by merging duplicates, resolving contradictions, and pruning stale entries, but it is a user-invoked instruction workflow with approval, not an automatic core promotion path ([dream skill](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/skills/dream/SKILL.md)).

**Scope and timing.** Scope is usually per user, agent, run, app, or project, depending on the API surface and filters. Timing can be online during chat, background after user prompts, pre-compaction, or explicit through MCP/API calls. The default add pipeline is online trace-to-memory extraction; plugin cleanup is staged and user-mediated.

**Survey placement.** Mem0 strengthens the survey's trace-to-retrievable-facts family but weakens the older claim that it is primarily LLM-judged CRUD curation. At this commit it is better classified as trace-derived ADD-only accumulation with deduplication, entity-linked retrieval boosts, and explicit/manual mutation paths. It does not climb the reach gradient into reviewed rules, tests, skills, or synthesis notes by default.

## Read-back placement

**Direction verdict:** both. The core `Memory.search()` API is pull, while the proxy wrapper and plugin hooks create true push paths from the receiving agent's perspective. OpenMemory MCP tool descriptions are better classified as high-authority cues that encourage pull retrieval rather than automatic read-back.

**Direction.** Plain library use is pull: an agent or host application must call `search()`. `mem0.proxy.Chat.Completions.create()` is push to the model receiving the completion, because the wrapper fetches memories and injects them before the LLM call. The plugin is also push to the agent: `UserPromptSubmit` can inject resume memories, error cues, file-path cues, a memory-search rubric, and save nudges without the agent first asking for them. MCP tool descriptions sit between those cases: they can instruct an agent to search, but they do not fetch or inject memory unless the agent or host then calls the tool.

**Trigger and relevance signal.** The proxy trigger is a chat completion whose last message is from the user; relevance is semantic memory search over the last six messages. The plugin trigger is the user prompt hook; its shell script uses cheap lexical detectors for resume intent, remember intent, errors, and file paths, and on resume it performs targeted Mem0 searches for session state and recent decisions. Precision and recall of these detectors are not verified from code.

**Timing relative to action.** The proxy inserts memories before the completion call. The user-prompt hook inserts cues before the agent responds. Pre-compaction capture runs before context is lost, but that is a write-back safety net rather than immediate read-back.

**Selection and scope.** Library search uses `top_k`, threshold, filters, optional reranking, semantic over-fetch, BM25 keyword scores where available, and entity boosts. Plugin searches include `user_id` and `app_id` and can filter by metadata type. Actual context dilution is runtime behavior, not established by the implementation.

**Authority at consumption.** Retrieved memories are advisory context, not hard gates. The plugin's injected rubric and MCP tool descriptions have instruction-like force over the agent's process, but the system does not test whether the agent actually obeys them. There is no WITH/WITHOUT ablation or post-action faithfulness check in the reviewed code.

**Other consumers.** Humans can inspect and manage memories through OpenMemory's UI/API state model. Apps and MCP clients consume the same memory records through access controls, categories, status history, and access logs.

## Curiosity Pass

**The earlier Mem0 story is now partly historical.** The code still contains the CRUD reconciliation prompt, and older docs/skills still mention graph memory in places, but the active OSS implementation says ADD-only extraction and entity linking. This is not a small wording difference; it changes the system's curation model.

**ADD-only is a safety move with accumulation costs.** Avoiding automatic update/delete reduces destructive LLM mistakes, but it pushes consolidation to retrieval scoring, explicit updates, manual deletion, or plugin cleanup. That is safer for personal memories but weaker as a knowledge-base learning loop.

**Entity linking is a retrieval feature, not graph knowledge.** The side collection can boost memories that share named entities, but it does not expose relation types, source evidence per edge, temporal validity, or graph traversal as the primary artifact.

**Procedural memory is a separate summary path.** `memory_type="procedural_memory"` with `agent_id` invokes an LLM summary prompt that preserves an agent execution history as a procedural memory ([memory main](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py), [prompts](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/prompts.py)). That is a real synthesis mechanism, but it is per-session summarization, not corpus-level curation.

**The strongest activation work lives outside the core memory class.** The hooks, MCP descriptions, proxy wrapper, and teachability helper are where Mem0 tries to make memory show up at the right time. The core storage engine alone remains ordinary pull retrieval.

## What to Watch

- Whether Mem0 removes the legacy CRUD prompt or rewires it into a controlled consolidation path.
- Whether V3 entity linking grows into typed, source-grounded graph relationships or remains a retrieval boost.
- Whether hosted/platform features diverge further from OSS `Memory`, especially around categories, async add events, graph claims, and webhooks.
- Whether the plugin's `dream` cleanup becomes an evaluated consolidation loop rather than a user-invoked review workflow.
- Whether push activation gains faithfulness tests: do injected memories change agent behavior, and when do they distract?
- Whether extraction records gain source spans, prompt/model versions, and approval states for each durable memory.

## Bottom Line

Mem0 is no longer best described, at this commit, as a two-phase LLM CRUD reconciler over facts. The reviewed OSS system is an ADD-only trace-to-memory extractor with vector storage, SQLite history, entity-linked retrieval boosts, explicit update/delete APIs, and optional wrappers/hooks that push memory into agent context. It is useful evidence for production memory activation and accumulation, but weak evidence for automated synthesis or governed KB learning.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Mem0 is trace-derived ADD-only accumulation with retrieval/entity boosts and manual or explicit mutation paths.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Mem0's plugin hooks and proxy wrapper try to bridge storage-to-context activation beyond passive search.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - contrasts: Mem0 automates fact extraction but not synthesis, relinking as authored semantics, regrouping, or governed promotion.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - contrasts: Mem0 keeps policy in prompts and hooks rather than learned weights; the policy is inspectable but not adaptively trained.
- [Distillation](../../notes/definitions/distillation.md) - defined-in: Mem0 distills conversations and transcripts into compact memory statements.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: extracted memory strings advise later responses when retrieved.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: extraction prompts, filters, ranking, entity boosts, MCP descriptions, and hooks route or instruct later behavior.
