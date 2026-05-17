---
description: "CrewAI review: unified in-framework memory with scoped vector records, task-output extraction, prompt injection, agent memory tools, and HITL lesson learning"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# CrewAI Memory

CrewAI Memory is the in-framework memory layer in CrewAI, the Python framework from CrewAIInc for building agents, crews, and flows. At the reviewed commit it has moved beyond the older short-term/long-term/entity framing into a single `Memory` API that can run standalone, behind crews, on individual agents, and inside flows. The central design is not a human-readable KB: it is a runtime memory service inside the agent framework, backed by vector storage, LLM-assisted extraction and scoping, automatic recall into prompts, optional agent memory tools, and a narrow human-feedback learning loop.

**Repository:** https://github.com/crewAIInc/crewAI

**Reviewed commit:** [a95d26763f4766b1a4f7c19c039133d1202dbdaa](https://github.com/crewAIInc/crewAI/commit/a95d26763f4766b1a4f7c19c039133d1202dbdaa)

**Last checked:** 2026-05-16

## Core Ideas

**One `Memory` object replaces multiple named memory stores.** The public docs describe a unified memory system with one `Memory` class, and the implementation matches that shape: `Memory` owns LLM analysis, embedding, storage, scoring weights, consolidation thresholds, query-analysis thresholds, a background save executor, and a structural `root_scope` ([memory docs](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/docs/en/concepts/memory.mdx), [unified memory](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/unified_memory.py)). `MemoryRecord` is the durable unit: content, hierarchical scope, categories, metadata, importance, timestamps, optional embedding, source, and privacy flag ([memory types](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/types.py)). That makes records mixed artifacts: prose content is the knowledge artifact, while scope/category/importance/private/source/embedding fields participate in routing and ranking.

**Storage is vector-first with pluggable backends.** `Memory(storage="lancedb")` is the default, and a string path also resolves to LanceDB; `"qdrant-edge"` selects a Qdrant Edge backend ([unified memory](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/unified_memory.py)). LanceDB stores rows with JSON-encoded categories and metadata, scalar scope indexes, vector columns, optimistic-conflict retries, and background compaction ([LanceDB storage](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/storage/lancedb_storage.py)). Qdrant Edge uses a write-local/sync-central pattern: each worker writes a local shard, reads merge local and central shards, and close/cleanup flushes local shards into central storage ([Qdrant Edge storage](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/storage/qdrant_edge_storage.py)). This is runtime infrastructure, not an inspectable note substrate.

**Save is an encoding flow, not a raw append.** `remember()` and `remember_many()` route through `EncodingFlow`: batch embed, drop near-duplicates inside a batch, search for similar existing records, use the LLM to infer scope/categories/importance/metadata and to decide consolidation actions, then insert/update/delete records ([encoding flow](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/encoding_flow.py), [analysis prompts](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/analyze.py)). The code has an important reliability detail: `remember_many()` runs in the background, but `recall()` calls `drain_writes()` before searching, and crew/flow shutdown paths also drain pending saves ([unified memory](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/unified_memory.py), [crew barrier](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/crew.py), [flow barrier](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/flow/flow.py)). The system is careful about avoiding lost writes but does not preserve the raw trace beside the distilled record.

**Recall combines vector retrieval, LLM query analysis, and score policy.** Shallow recall embeds the query and searches once. Deep recall uses `RecallFlow`: skip LLM analysis for short queries, analyze longer queries into subqueries/scopes/time filters, batch-embed up to three subqueries, search candidate scopes in parallel, optionally ask the LLM to explore deeper when confidence is low, deduplicate, and compute a composite score from semantic similarity, recency decay, and importance ([recall flow](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/recall_flow.py), [score function](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/types.py)). The ranking formula is a system-definition artifact: it decides what reaches the agent even though the records themselves remain knowledge artifacts when read as evidence.

**Crew, agent, lite-agent, and flow surfaces all consume the same memory.** A crew with `memory=True` creates `Memory(embedder=crew.embedder, root_scope="/crew/<name>")`; custom `Memory`, `MemoryScope`, and `MemorySlice` instances are accepted as-is ([crew memory setup](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/crew.py), [scoped views](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/memory/memory_scope.py)). Before a crew task runs, the agent recalls against the task description and appends a formatted memory block to the task prompt; lite agents do the same against the last user message ([agent prompt injection](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/agent/core.py), [lite agent injection](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/lite_agent.py)). Crews also add "Search memory" and, unless read-only, "Save to memory" tools to agent tool lists ([memory tools](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/tools/memory_tools.py), [tool injection](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/crew.py)). Flows auto-create `Memory(root_scope="/flow/<name>")` unless explicitly disabled and expose `remember`, `recall`, and `extract_memories` methods ([flow memory](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/flow/flow.py)).

**Trace extraction is automatic after task execution, and HITL feedback can become reusable lessons.** `BaseAgentExecutor._save_to_memory()` builds a raw text bundle from task description, agent role, expected output, and final output, then calls `extract_memories()` and `remember_many()` under an agent-specific root scope; it skips delegation outputs and read-only memories ([base executor](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py)). Direct agent kickoff and lite-agent runs have similar input/result extraction paths ([agent kickoff memory](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/agent/core.py), [lite agent memory](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/lite_agent.py)). Separately, `@human_feedback(learn=True)` recalls prior lessons before a human sees a flow method output, asks an LLM to apply those lessons, then distills new generalizable lessons from the output plus raw feedback and stores them in memory under `source="hitl"` by default ([HITL learning](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/flow/human_feedback.py), [HITL prompts](https://github.com/crewAIInc/crewAI/blob/a95d26763f4766b1a4f7c19c039133d1202dbdaa/lib/crewai/src/crewai/translations/en.json)).

## Comparison with Our System

| Dimension | CrewAI Memory | Commonplace |
|---|---|---|
| Primary artifact | `MemoryRecord` rows/points plus embeddings, scopes, categories, metadata, importance, source, privacy | Typed markdown notes, sources, instructions, reviews, ADRs, schemas, generated indexes |
| Storage substrate | LanceDB by default; optional Qdrant Edge local/central shards; storage backend protocol | Git-tracked files with generated reports and indexes |
| Representational form | Mixed: prose records, symbolic metadata/scopes/categories, distributed embeddings, numeric ranking state | Mostly prose and frontmatter, plus schemas/scripts/validation reports |
| Lineage | Weak at record level: source string and raw prompt bundle pass through extraction, but raw traces and derivation prompts are not retained beside each record | Source snapshots, commit-pinned reviews, citations, git history, replacement/archive lifecycle |
| Activation | Automatic prompt injection, active recall/save tools, flow methods, HITL pre-review, composite ranking | Agent reads instructions/indexes, uses `rg`, follows semantic links, runs skills/validation/review commands |
| Authority | Recall and ranking select context; memory prompt block instructs agent to use/search memory; HITL lessons can rewrite flow outputs before review | Type specs, collection contracts, AGENTS.md, skills, validation/review commands |

CrewAI is much stronger as embedded runtime memory. A user can turn on `memory=True`, and every task execution gets a recall-before-run and extraction-after-run loop without inventing a separate workflow. The read barrier around background saves is especially practical: trace-derived writes can be asynchronous without making the next recall silently miss them.

Commonplace is stronger as an auditable knowledge substrate. A CrewAI memory record may have content, categories, source, importance, and metadata, but it is not a reviewed claim, does not preserve source evidence by default, has no replacement lifecycle, and has no link contract. CrewAI's extracted memories are optimized for future prompt usefulness, not for dispute, maintenance, or methodological transfer.

The important artifact split is between raw traces, `MemoryRecord` rows, embeddings/storage backends, recall ranking, prompt injection, memory tools, and framework settings. Raw task/HITL material is source evidence. The record content is a knowledge artifact when recalled as context. Embeddings, scope filters, composite scores, read-only flags, source/private filters, tool descriptions, prompt-injection templates, and HITL pre-review prompts are system-definition artifacts because they route, rank, constrain, or instruct later behavior.

## Borrowable Ideas

**Read barrier for async memory writes.** Ready to borrow if commonplace ever adds background capture. CrewAI's `remember_many()` returns immediately, but `recall()`, crew kickoff finalization, and flow finalization wait for pending writes. That is the right minimal contract for "fast write, no stale next read."

**A first-class read-only memory view.** Ready as vocabulary. `MemorySlice(read_only=True)` suppresses the save tool while preserving recall. Commonplace has different authority surfaces, but read-only projections would be useful for giving agents compiled context without giving them mutation rights.

**Tool descriptions that encode retrieval obligations.** Useful if commonplace wraps commands as agent tools. CrewAI's memory prompt tells agents not to trust the automatic memory block for counting/listing tasks and to run multiple searches. That is a concrete tool-level control pattern, though it still depends on model compliance.

**Agent-rooted scopes under a crew root.** Worth tracking. CrewAI stores auto-extracted task memories under `/crew/<crew>/agent/<role>`, which creates a useful default separation between shared crew memory and role-specific traces. Commonplace does not need this inside its library layer, but workshops or multi-agent runs could use similar namespace defaults.

**HITL lesson distillation as a narrow loop.** Borrow the shape, not the storage. The best part is the trigger boundary: only human feedback on a marked method becomes candidate lessons, and those lessons are used before future human review. Commonplace would need a reviewed note/instruction promotion step before those lessons gained durable authority.

**Do not borrow opaque vector records as the primary KB.** CrewAI's design is appropriate inside an application framework, where memory is used to improve the next agent run. It would be a poor replacement for methodology notes because the record-level evidence, review state, and lifecycle are too thin.

## Trace-derived learning placement

CrewAI Memory qualifies as trace-derived learning through implemented task-output extraction and HITL lesson learning. It does not merely store user-authored facts; framework execution traces and human-feedback traces can become durable memories that affect later prompts and flow outputs.

**Trace source.** Crew execution traces are task description, agent role, expected output, and final answer assembled after execution by `BaseAgentExecutor._save_to_memory()`; direct agent and lite-agent paths similarly bundle user input plus result text. HITL traces are flow method output plus raw human feedback from `@human_feedback(learn=True)`.

**Extraction.** Task and agent traces go through `extract_memories_from_content()`, whose prompt asks the LLM to emit discrete reusable memory statements. Save-time analysis then infers scope, categories, importance, metadata, and possible consolidation actions. HITL traces go through a separate distillation prompt that asks for generalizable lessons and returns an empty list for approvals or non-generalizable feedback.

**Storage substrate.** Raw traces are mostly transient strings inside the executor/decorator path. Distilled records persist through the configured memory backend: LanceDB rows by default or Qdrant Edge local/central shards. The durable record stores content, scope, categories, metadata, importance, timestamps, source/private flags, and embeddings.

**Representational form.** Raw traces are prose bundles with some symbolic framing fields. Distilled memories and HITL lessons are prose. Scope, categories, source, private flag, importance, timestamps, consolidation plans, and tool schemas are symbolic. Embeddings and vector-distance scores are distributed-parametric. Composite scoring and read/write permissions are symbolic/numeric system-definition state.

**Lineage.** Lineage is the weak point. The extraction input includes task/agent/output or method/output/feedback, but the resulting `MemoryRecord` does not retain a reviewable link to the exact raw trace, model, prompt version, extraction decision, or human approval state. `source="hitl"` distinguishes one learning channel; it is not enough to reconstruct derivation.

**Behavioral authority.** Recalled records advise the agent as knowledge artifacts when shown in the memory block or returned by the search tool. The same records gain stronger authority through automatic prompt injection and HITL pre-review because they are inserted into the model's working context before action. Scoring weights, scope filters, private/source checks, tool availability, and the memory prompt carry system-definition authority over selection and use.

**Scope and timing.** Scope is per standalone memory, per crew root, per agent root under a crew, per flow root, or custom user-provided scopes/slices. Timing is online during framework execution: recall before task/method output use, extraction after outputs or feedback, background batch persistence, and read barriers before later recall.

**Survey placement.** CrewAI strengthens the survey's "trace-to-runtime memory" axis: traces become prompt-time memories and HITL lessons inside the same application framework. It weakens any claim that trace-derived learning necessarily produces reviewed rules or executable skills. The distilled artifact is usually a prose memory record, not a promoted instruction, validator, code patch, or benchmark-gated skill.

## Curiosity Pass

**The memory block is both context and instruction.** It shows selected memories, then tells the agent that automatic selection may be incomplete and mandates extra searches for counting/listing/summing tasks. That is a sensible control, but it means the retrieval mechanism delegates part of correctness back to prompt compliance.

**The LLM does a lot of governance work.** It chooses memory statements, scopes, categories, importance, consolidation actions, query rewrites, and HITL lessons. The fallback paths are pragmatic, but the durable memory has little independent validation of whether the extracted lesson is true, useful, or non-duplicative.

**"Private" is a recall filter, not a full governance model.** `MemoryRecord.private` and `source` can hide records unless the source matches or `include_private=True` is used. That is useful local isolation, but not a tenant/ACL/review model.

**The Qdrant Edge backend is more operationally interesting than the record model.** The local-shard/central-shard pattern directly addresses multi-process write contention. For commonplace, the analogous lesson is about safe generated-index writes, not about adopting Qdrant.

**Trace-derived status should stay narrow.** The baseline standalone `remember()` API can store directly authored facts, and generic memory use is not necessarily trace-derived. The trace-derived classification comes from implemented executor extraction and HITL learning paths.

## What to Watch

- Whether CrewAI starts preserving raw trace lineage, extraction prompts, model identity, and review/approval state beside each `MemoryRecord`.
- Whether HITL lessons gain lifecycle controls: deduplication, expiry, conflict handling, human review, and retirement.
- Whether memory tools become the primary agent-facing surface, or whether automatic prompt injection remains the dominant consumer path.
- Whether Qdrant Edge becomes the default or stays an optional backend for high-concurrency local execution.
- Whether extracted memories ever promote into stronger artifacts such as task validators, guardrails, skills, or crew configuration changes.
- Whether composite scoring remains a fixed hand-tuned formula or gains evaluation-backed weighting.

---

Relevant Notes:

- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: CrewAI memory content advises later agents when recalled as evidence, context, or lessons.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: scoring, scopes, prompt injection, memory tool availability, read-only flags, and HITL pre-review route or instruct behavior.
- [Lineage](../../notes/definitions/lineage.md) - clarifies: CrewAI has source strings and scopes, but not a reviewable derivation chain from raw trace to durable memory.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: CrewAI needs separate treatment for raw traces, records, embeddings, ranking policy, storage shards, prompt blocks, and tools.
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: CrewAI is a runtime trace-to-memory and HITL-feedback-to-lesson system, not a reviewed-rule or executable-skill learning system.
