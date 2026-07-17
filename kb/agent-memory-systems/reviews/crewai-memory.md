---
description: "CrewAI Memory review: unified vector memory with LLM extraction, scoped recall, task/HITL learning, tools, and pre-task prompt injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# CrewAI Memory

CrewAI Memory is the memory layer inside crewAIInc's Python multi-agent framework. At the reviewed commit it is centered on a unified `Memory` class with scoped vector records, LLM-assisted encoding and recall, default LanceDB storage, an alternate Qdrant Edge backend, memory tools, Crew/Agent/Flow integration, automatic task and kickoff learning, and source-visible pre-invocation memory injection for both Crew tasks and standalone agent kickoff.

**Repository:** https://github.com/crewAIInc/crewAI

**Reviewed commit:** [aed69237d4eb7ad6ba8fe3d0b4777979fe949869](https://github.com/crewAIInc/crewAI/commit/aed69237d4eb7ad6ba8fe3d0b4777979fe949869)

**Last checked:** 2026-06-04

## Core Ideas

**The implemented center is unified memory, not separate short/long/entity stores.** `Memory` owns `remember`, `remember_many`, `recall`, `extract_memories`, scopes, slices, storage, lazy LLM/embedder initialization, background saves, read barriers, and events ([unified_memory.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/unified_memory.py)). The docs explicitly frame this as a single `Memory` class replacing separate short-term, long-term, entity, and external memory types ([memory.mdx](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/docs/en/concepts/memory.mdx)).

**The retained unit is a scoped, scored vector record.** `MemoryRecord` stores prose content plus scope, categories, metadata, importance, timestamps, optional source, a privacy flag, and an embedding excluded from serialization ([types.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/types.py)). That makes one durable artifact serve as evidence, ranking input, scoped state, and prompt context depending on the read path.

**Saving is an encoding pipeline with LLM field inference and optional consolidation.** `EncodingFlow` embeds a batch, drops near-exact duplicates, searches similar stored records, uses the LLM to infer missing scope/categories/importance/metadata, optionally asks for keep/update/delete/insert consolidation actions, then applies deletes, updates, and inserts ([encoding_flow.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/encoding_flow.py), [analyze.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/analyze.py)). If callers provide all fields and no similar record crosses the threshold, the save path can avoid field-analysis LLM work.

**Recall is retrieval-first but can ask an LLM to reshape the query.** Shallow recall embeds the query and searches storage directly. Deep recall can skip LLM analysis for short queries, otherwise distill up to three recall queries, suggest scopes and time filters, search across candidate scopes, route low-confidence or complex queries through one deeper extraction round, deduplicate, and rank by semantic, recency, and importance scores ([recall_flow.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/recall_flow.py), [types.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/types.py)).

**Context efficiency is active but still prose-heavy at the end.** CrewAI reduces volume with scope roots, slices, category/source/privacy filters, recall limits, oversampling, candidate-scope caps, query-analysis thresholds, read-only views, and batch writes. It does not reduce recalled memories into a verified compact claim set before prompt insertion: selected `MemoryMatch` objects format back into prose lines for the task prompt, kickoff input, or memory tool result ([agent/core.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/agent/core.py), [memory_tools.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/tools/memory_tools.py)).

**Memory is wired into Crews, Agents, Flows, and human feedback.** `Crew(memory=True)` creates a root-scoped `Memory` with the crew embedder; agents can own memory or use crew memory; flows auto-create memory and expose `remember`, `recall`, and `extract_memories`; human-feedback decorators can recall prior lessons before review and distill new lessons from raw feedback ([crew.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/crew.py), [base_agent.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/agents/agent_builder/base_agent.py), [flow/runtime.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/flow/runtime.py), [human_feedback.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/flow/human_feedback.py)).

## Artifact analysis

- **Storage substrate:** `vector` — The primary behavior-shaping retained memory persists as vector-indexed `MemoryRecord` rows in LanceDB by default, or Qdrant Edge points when configured; local file directories under `$CREWAI_STORAGE_DIR` or platform app-data hold those vector stores ([lancedb_storage.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/storage/lancedb_storage.py), [qdrant_edge_storage.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/storage/qdrant_edge_storage.py), [paths.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai-core/src/crewai_core/paths.py)).
- **Representational form:** `prose` `symbolic` `parametric` — Record content and recalled blocks are prose; scopes, categories, metadata, importance, source, privacy flags, tool schemas, and consolidation plans are symbolic; embeddings and vector distances supply parametric retrieval signals.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents can author memories directly; knowledge sources are imported into adjacent RAG storage; task outputs, standalone kickoff outputs, and human-feedback records are distilled into later memory statements.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `ranking` `learning` — Memory records advise as knowledge, become instruction-like prompt context when injected, enforce visibility through read-only views/private filtering/tool omission, route via scopes and slices, rank through vector/composite scoring, and feed LLM-mediated write/consolidation decisions.

**Memory records.** Storage substrate: LanceDB rows or Qdrant Edge points. Representational form: prose content plus symbolic fields and embeddings. Lineage: directly authored through `remember`/tools/flow calls or trace-extracted from task, kickoff, and feedback output. Behavioral authority: knowledge when returned, ranking input when selected, and advisory instruction when appended to prompts.

**Encoding analyses and consolidation plans.** Storage substrate: transient flow state, with durable effects applied to vector storage. Representational form: symbolic Pydantic-validated LLM outputs for scope, categories, importance, metadata, and keep/update/delete/insert actions. Lineage: derived from new content, existing scopes/categories, and similar records. Behavioral authority: learning and mutation authority; these plans can update or delete retained records but are not themselves retained as auditable artifacts.

**Scopes, slices, source, and privacy.** Storage substrate: symbolic scope/source/private fields on records plus runtime `MemoryScope` and `MemorySlice` views. Representational form: path prefixes, scope lists, category filters, source ids, and boolean read-only/private flags. Lineage: authored, framework-derived from crew/agent/flow names, or LLM-inferred during encoding. Behavioral authority: routing and enforcement, because they constrain search, writes, reset, private recall, and whether a save tool is offered ([memory_scope.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/memory_scope.py)).

**Memory tools and prompt fragments.** Storage substrate: runtime tool objects and assembled prompt strings, not a separate durable store. Representational form: symbolic tool schemas plus prose tool descriptions and recalled memory text. Lineage: generated from an available memory object and current recall results. Behavioral authority: routing and instruction; tools let the agent pull or write memory, while prompt fragments push retrieved memory into the next model call.

**Human-feedback lessons.** Storage substrate: ordinary memory storage through `remember_many`. Representational form: prose lesson statements with symbolic source metadata and embeddings. Lineage: trace-extracted from flow method output and raw human feedback. Behavioral authority: learning and instruction, because later `learn=True` feedback wrappers recall lessons and ask an LLM to pre-review the next method output before human review ([human_feedback.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/flow/human_feedback.py)).

**Knowledge sources.** Storage substrate: adjacent RAG storage, currently Chroma-backed by default through the knowledge/RAG layer rather than the unified `Memory` table. Representational form: source chunks and embeddings. Lineage: imported from strings, files, PDFs, CSV/Excel/JSON, or Docling sources. Behavioral authority: knowledge for agent/crew queries, but it should not be collapsed into unified Memory because its lineage and write path differ ([knowledge.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/knowledge/knowledge.py), [knowledge_storage.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/knowledge/storage/knowledge_storage.py)).

Promotion path: CrewAI can move task/kickoff/feedback traces into extracted prose statements, then into scoped vector records with symbolic fields and embeddings, then back into future prompts or tools. The promotion increases operational reach but does not add durable source excerpts, extraction prompt versioning, consolidation rationale, or semantic review status.

## Comparison with Our System

| Dimension | CrewAI Memory | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory for agent executions, crews, standalone agents, flows, and feedback loops | Git-tracked methodology KB for agents and maintainers |
| Main substrate | LanceDB/Qdrant Edge vector records plus adjacent knowledge RAG stores | Markdown files, source snapshots, schemas, scripts, generated indexes |
| Retained unit | `MemoryRecord` with content, scope, categories, metadata, importance, timestamps, embedding, source, privacy | Typed notes/reviews/instructions with frontmatter, links, status, citations |
| Write path | Direct memory calls, tools, task/kickoff extraction, HITL lesson distillation, LLM consolidation | Authored edits, snapshots, validation, semantic review, index refresh |
| Read-back | Pull tools/API plus pre-task, kickoff, and HITL lesson push | Mostly deliberate pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Runtime scopes, privacy, read-only slices, events, reset commands, tests | Collection contracts, type specs, validation, semantic review, git lifecycle |

CrewAI is stronger as runtime activation infrastructure. It gives agents a search/save tool surface, injects relevant memory into prompts before tasks or standalone kickoff, and extracts new memories after outputs. Commonplace is stronger as a durable review substrate: claims have citations, explicit status, git history, and validation/review gates.

The main tradeoff is hidden mutation authority. CrewAI lets an LLM infer fields and consolidation actions inside the runtime save pipeline. That is useful for operational memory, but it makes the durable record less reviewable than a Commonplace artifact whose source, type, and promotion path are explicit.

### Borrowable Ideas

**Make runtime memory views explicit.** Ready as design language. `MemoryScope`, `MemorySlice`, `read_only`, `source`, and `private` are useful ways to describe who may see or mutate a context subset.

**Use a read barrier before recall.** Ready for generated context serving. `recall()` drains pending saves before searching, which is a practical guarantee for async write paths.

**Separate extraction from storage.** Ready now. `extract_memories()` is a pure helper before `remember_many()`, keeping "what is worth retaining" separate from "where it is stored."

**Treat automatic prompt memory as advisory and incomplete.** Ready for future Commonplace push contexts. CrewAI's selected memory is prompt context, not proof that the model will use it faithfully or completely.

**Do not borrow unaudited consolidation for durable methodology notes.** Ready as a constraint. CrewAI's LLM consolidation can update or delete records without a retained review artifact; Commonplace should keep comparable edits behind visible proposals, validation, and semantic gates.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from direct `Memory.remember`, Flow `remember`, and the `Save to memory` tool; automatic writes come from task-output extraction, standalone agent kickoff extraction, HITL lesson distillation, background batch encoding, deduplication, LLM field inference, LLM consolidation, and timestamp touching.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `promote` — Batch encoding drops near-exact duplicates, consolidation can update/delete existing records, extraction synthesizes discrete memories from larger outputs, task/kickoff/HITL outputs are promoted into durable records, and recall touches `last_accessed` in place.

### Trace-learning

**Trace source:** `session-logs` `event-streams` — Crew tasks, standalone agent kickoff inputs/results, and flow human-feedback events provide the raw signal; memory events expose operational query/save/retrieval activity.

**Learning scope:** `per-task` `per-project` `cross-task` — Extraction starts from individual tasks, agent kickoff calls, or flow methods; crew root scopes, agent subscopes, flow scopes, and explicit user scopes decide how far those memories can affect later tasks or runs.

**Learning timing:** `online` `staged` — Crew and kickoff saves happen in the runtime path after producing output, often through background `remember_many`; HITL lessons are distilled during feedback handling; recall-time `last_accessed` updates and storage compaction are staged maintenance.

**Distilled form:** `prose` `symbolic` `parametric` — Raw outputs become prose memory statements with symbolic scope/category/metadata/importance/source/private fields and embeddings.

**Extraction.** Crew task saving builds a raw bundle from task description, agent role, expected output, and result; standalone kickoff saving builds a bundle from input, agent role, and result; HITL learning builds lessons from method output and raw human feedback. The shared `extract_memories_from_content` helper asks an LLM for discrete self-contained statements and falls back to storing the full content if extraction fails ([base_agent_executor.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py), [agent/core.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/agent/core.py), [analyze.py](https://github.com/crewAIInc/crewAI/blob/aed69237d4eb7ad6ba8fe3d0b4777979fe949869/lib/crewai/src/crewai/memory/analyze.py)).

**Scope and timing.** Crew memory is rooted under `/crew/<name>` when `memory=True`, and automatic task saves add an agent-specific subroot under that crew. Agent kickoff memory uses the agent's own memory. Flow memory defaults under `/flow/<name>`. These writes affect later invocations; they do not revise the action that generated the trace.

**Survey fit.** CrewAI fits the trace-to-vector-memory family with LLM extraction and LLM-assisted consolidation. It strengthens the distinction between raw trace artifacts and distilled behavior-shaping artifacts: traces are not replayed directly, but converted into scoped records that later influence retrieval, prompt context, and tool results.

## Read-back

**Read-back:** `both` — CrewAI has pull read-back through `Memory.recall`, Flow `recall`, `Search memory`, and direct API calls; it has push read-back when Crew task preparation, standalone agent kickoff preparation, and HITL pre-review automatically recall retained memories and append or apply them before the next model/review call.

**Read-back signal:** `inferred / embedding` `inferred / judgment` — Push paths key on the current task description, kickoff message text, or flow method output; recall primarily embeds these inferred queries, and deep recall can add LLM query analysis, scope suggestions, and deeper extraction when confidence is low.

**Faithfulness tested:** `no` — The source and tests cover memory creation, recall/save calls, events, scope/slice behavior, prompt retrieval plumbing, and background writes, but I did not find with/without ablations or post-action audits proving that pushed memories are faithfully used by the model.

**Direction edge cases.** Memory tools are pull even when the tool is available by default, because the agent must call them. Crew task prompt preparation is push for the receiving agent: `_retrieve_memory_context()` calls `recall(task.description, limit=5)` and appends a memory slice before final task execution. Standalone agent kickoff similarly recalls against formatted input and appends the memory slice before invoking the executor. HITL learning is push in a different consumer path: prior lessons are recalled and used to rewrite a method output before human review.

**Targeting and signal.** Push is instance-targeted by inferred content, not coarse always-load. The selected instance text is the task description, kickoff message content, or feedback method output. The primary selector is embedding search over records, with optional LLM query analysis and scope selection in deep recall.

**Injection point.** Read-back is pre-invocation. Crew task memory is appended before `_finalize_task_prompt`; kickoff memory is appended before executor inputs are built; HITL lessons are applied before requesting human feedback. Post-output extraction and background saves are write-side maintenance, not a second read.

**Selection, scope, and complexity.** Crew task push uses five matches; standalone kickoff uses twenty; general recall defaults to ten, oversamples vector search candidates, caps distilled query phrases at three, caps candidate scopes at twenty, filters by scope/categories/source/private state, and ranks by semantic similarity, recency, and importance. Complexity is not just count: injected prose can include multiple scoped memories, metadata fields, and LLM-selected evidence gaps.

**Authority at consumption.** Recalled memories are advisory knowledge when returned by API/tool. When appended to task prompts or kickoff input, they become instruction-like context with practical force but no hard enforcement. Scopes, slices, source/private filters, and read-only tool omission define stronger routing/enforcement authority around who can read or mutate memory.

**Other consumers.** Humans and operators can consume memory through `tree`, `info`, `list_records`, `list_categories`, events, reset commands, tests, and storage inspection. Those surfaces help observability but do not provide semantic review of whether a remembered claim is true.

## Curiosity Pass

**The old taxonomy survives mostly as compatibility/reset language.** The implemented memory object is unified, while reset utilities and docs still have to map older memory concepts into the new single-store surface.

**Push is now broader than the previous review found.** Current source shows ordinary Crew task prompt memory retrieval as well as standalone agent kickoff retrieval, so push read-back is no longer only a LiteAgent-style edge path.

**The same record changes authority by route.** A `MemoryRecord` is a knowledge artifact in a search result, instruction-like context in a prompt, ranking state in recall, and mutation input during consolidation.

**Consolidation is powerful and hard to audit.** A failed extraction preserves the whole content as one memory, but a successful consolidation can update or delete prior records without retaining the deliberation as a durable review artifact.

**Human-feedback learning is unusually direct.** Prior feedback lessons are not merely recalled for display; they can rewrite the next method output before it reaches a human reviewer.

## What to Watch

- Whether consolidation plans become retained proposal artifacts; that would reduce hidden mutation authority and make CrewAI memory more reviewable.
- Whether pushed memory gains faithfulness or coverage tests; that would turn prompt insertion from a structural mechanism into measured behavioral authority.
- Whether Memory and Knowledge converge or stay separate; convergence would require rechecking storage substrate, lineage, and trust boundaries.
- Whether task/kickoff memory gets explicit token budgets or summarization before prompt insertion; that would change the context-efficiency assessment.
- Whether HITL lesson learning adds source excerpts or feedback provenance fields; that would make feedback-derived memories safer to reuse across tasks.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: CrewAI distills task, kickoff, and feedback traces into scoped vector memory records.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: CrewAI stores memory separately from the push/pull paths that bring it into context.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: CrewAI extracts reusable statements from runtime outputs before storing them.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: records, scopes, tools, prompt fragments, and consolidation plans differ by form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: injected prompt memory, memory tools, scopes, and consolidation plans shape behavior more strongly than ordinary retrieved evidence.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - applies: the same retained fact can advise, instruct, route, rank, or drive mutation depending on the consumption path.
