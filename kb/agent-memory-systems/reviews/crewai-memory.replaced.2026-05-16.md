---
description: "CrewAI's in-framework memory layer with LLM-scoped vector records, composite recall, async save barriers, agent memory tools, and HITL lesson distillation"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation]
tags: []
status: outdated
last-checked: "2026-04-13"
---

# CrewAI Memory

> Replaced 2026-05-16. See [CrewAI Memory](./crewai-memory.md) for the current review.

CrewAI Memory is the in-framework memory layer for [CrewAI](https://github.com/crewAIInc/crewAI), the CrewAI Inc. Python framework for multi-agent crews, standalone agents, and flows. It exposes one `Memory` API that stores LLM-analyzed vector records, injects recalled records into agent prompts, gives agents explicit "Search memory" and "Save to memory" tools, and mines task results plus optional human feedback into durable memory records. In the current implementation it is strongest as retrieval infrastructure and a trace-to-record adapter, not as a knowledge medium with inspectable argument structure or a mature learning lifecycle.

**Repository:** https://github.com/crewAIInc/crewAI

**Reviewed commit:** https://github.com/crewAIInc/crewAI/commit/1d6f84c7aab08bf460a08180a1fc7f15326f22ab

## Core Ideas

**One record type plus scope paths replaces named memory classes.** The code now centers on `MemoryRecord`: `content`, hierarchical `scope`, `categories`, arbitrary `metadata`, `importance`, `source`, and a `private` flag, with embeddings excluded from Pydantic serialization to reduce prompt leakage ([types.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/types.py)). `Memory` is lazily exported from the top-level package to avoid loading LanceDB at import time ([__init__.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/__init__.py)). This is an architectural simplification: the older short-term/long-term/entity/external split is folded into a single record model where namespace, category, source, and privacy flags carry the distinctions.

**Encoding is a five-stage flow, not a direct write.** `EncodingFlow` batch-embeds all items, drops intra-batch near-duplicates by cosine similarity, searches for similar existing records, runs LLM analysis/consolidation in parallel, then applies deletes, updates, and inserts ([encoding_flow.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/encoding_flow.py)). The fast path skips LLM field inference only when the caller supplied scope, categories, and importance and no similar record crosses the consolidation threshold. Otherwise the LLM infers scope/categories/importance or decides whether similar records should be kept, updated, deleted, or superseded ([analyze.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/analyze.py)). This is good deduplication and conflict-handling machinery, but it is still local consolidation, not synthesis across a body of knowledge.

**Recall is vector search with composite ranking and optional LLM planning.** Shallow recall embeds the query, runs one storage search, then computes `semantic_weight * similarity + recency_weight * decay + importance_weight * importance`. Deep recall wraps that in `RecallFlow`: query analysis, candidate scope selection, parallel search across query/scope combinations, confidence-based routing, and optional recursive exploration ([recall_flow.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/recall_flow.py)). Short queries skip LLM query analysis, which is the right optimization for the common "what did we decide?" case. The interesting design choice is not the vector store; it is the explicit blend of similarity, time decay, and importance, with match reasons surfaced in `MemoryMatch`.

**The runtime integration makes memory prompt middleware and an agent tool.** When a crew has `memory=True`, it creates `Memory(root_scope="/crew/{crew_name}")`; flows auto-create memory under `/flow/{flow_name}` unless they are internal memory flows; agents use either their own memory or the crew memory ([crew.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/crew.py), [flow.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/flow/flow.py)). Before task execution, agents recall relevant memories and append them to the task prompt; standalone agent kickoff and `LiteAgent` do the same around their message input ([agent/core.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/agent/core.py), [lite_agent.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/lite_agent.py)). Separately, `create_memory_tools()` gives agents recall/save tools when memory is available, omitting save when the view is read-only ([memory_tools.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/tools/memory_tools.py)).

**Background writes are treated as a consistency problem.** Single `remember()` calls run through the serialized save pool and block for a result; `remember_many()` returns immediately and saves in a background thread. Every `recall()` calls `drain_writes()` before searching, and crew/flow kickoff drains pending saves in `finally` blocks ([unified_memory.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/unified_memory.py)). The storage layer mirrors that concern: LanceDB is the default backend, with lock-guarded writes, commit-conflict retries, scope scalar indexing, and background compaction; Qdrant Edge is an optional backend with a local-worker/central-shard sync pattern ([lancedb_storage.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/storage/lancedb_storage.py), [qdrant_edge_storage.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/storage/qdrant_edge_storage.py)).

**Human feedback can become reusable lessons.** The `@human_feedback(..., learn=True)` path first recalls prior lessons for the method output, lets an LLM pre-review the output against those lessons, then distills new generalizable lessons from the human's feedback and stores them with `source="hitl"` ([human_feedback.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/flow/human_feedback.py)). This is the most explicit learning loop in the inspected code because it has a trigger boundary, a source trace, an extraction prompt, a reinjection point, and a narrow artifact type: reusable human-feedback lessons.

## Comparison with Our System

| Dimension | CrewAI Memory | Commonplace |
|---|---|---|
| Primary substrate | LanceDB or Qdrant Edge vector records | Markdown files in git |
| Memory atom | `MemoryRecord` string with scope/categories/metadata/importance | Notes, indexes, ADRs, instructions, source reviews |
| Organization | LLM-inferred hierarchical scopes plus categories | Curated collections, type contracts, explicit indexes |
| Retrieval | Automatic prompt injection, explicit recall tool, vector search | Agent-driven navigation through descriptions, links, and search |
| Trace learning | Task/result and HITL feedback distilled into memory strings | Workshop and source artifacts reviewed into library notes |
| Curation | LLM local consolidation on similar records | Human/agent review, frontmatter validation, link semantics |
| Inspectability | TUI/events/API over database rows | Directly readable, diffable files |

CrewAI is stronger as runtime infrastructure. It handles the boring but real engineering concerns: async saves, read barriers, scope isolation, storage conflict retries, source/private filters, and framework hooks. Commonplace does not have an equivalent runtime memory API because it is not trying to sit inside every agent step.

Commonplace is stronger as a knowledge medium. CrewAI records can be retrieved, but they cannot carry a title-as-claim, a link reason, a status, a source snapshot, a semantic review history, or a type transition. Its consolidation step can update or delete similar records, but it has no path from "this appeared in a task output" to "this should become a decision, procedure, index, or structured claim." In [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) terms, CrewAI persists symbolic artifacts, but it does not move them along the [verifiability gradient](../../notes/verifiability-gradient.md).

The most important divergence is that CrewAI makes scope the universal separator. A project decision, a user preference, a task result, and a human-feedback lesson can all land in the same record class. The scope tree and categories mitigate the [flat-memory](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) failure, but they do not enforce different lifecycles for operational debris, durable knowledge, and self/preference memory. Commonplace keeps those differences in artifact types and collection conventions; CrewAI keeps them in metadata and retrieval filters.

## Borrowable Ideas

**Read barriers after async writes.** Ready to borrow if Commonplace adds runtime capture. The combination of non-blocking batch save plus mandatory drain-before-read is simple and correct. It lets the main agent keep moving without making recall race stale writes.

**Root scopes as structural tenancy.** Ready to borrow as a naming convention. CrewAI's `/crew/{name}`, `/flow/{name}`, and `/agent/{role}` scopes are not a full access-control model, but they are a useful default namespace grammar for multi-agent memory.

**Composite scoring with an explicit half-life.** Ready to borrow for any future retrieval layer below the KB. The formula is crude but honest: semantic similarity alone is not the same as usefulness. The half-life parameter also makes the intended domain visible: sprint memory and architectural memory should decay differently.

**Memory tools as active recall policy.** Needs a use case first. CrewAI's automatic prompt injection includes a warning that selected memories may be incomplete and the agent should use the search tool for counting/listing tasks. That recognizes a real retrieval problem: preloaded context is a sample, not an exhaustive answer. If we add generated recall bundles, pairing them with an explicit "search the KB before counting" rule would be worth copying.

**HITL lesson distillation.** Needs a narrow pilot, not a general automation project. The flow feedback loop is compact: retrieve prior lessons, pre-review output, distill new lessons only when human feedback contains guidance. A Commonplace analogue would likely write workshop-local lessons first, then require review before promoting them into instructions.

**Storage backend protocol around one record type.** Useful below the KB, not inside the library. The `StorageBackend` protocol is clean for runtime memory records, but importing that substrate into the library would erase too much structure. The right use would be a cache or workshop capture layer that points back to durable notes.

## Trace-derived learning placement

**Trace source.** CrewAI qualifies as trace-derived learning. The main traces are task execution outputs (`Task`, agent role, expected output, result) saved by the agent executor, standalone agent/LiteAgent input-result pairs, and optional human-feedback method outputs plus raw human feedback when `learn=True` ([base_agent_executor.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py), [agent/core.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/agent/core.py), [lite_agent.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/lite_agent.py), [human_feedback.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/flow/human_feedback.py)).

**Extraction.** Ordinary task/run traces go through `extract_memories_from_content()`, whose prompt asks for discrete reusable statements and falls back to storing the whole content if extraction fails. Save-time analysis then infers scope, categories, importance, and metadata; consolidation compares against similar records and can update/delete/insert. HITL learning uses a separate lesson-distillation prompt that asks for reusable rules or preferences and returns an empty list for approval-only feedback ([translations/en.json](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/translations/en.json), [analyze.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/analyze.py)).

**Promotion target.** The target is symbolic service memory: database-backed `MemoryRecord` rows with vector embeddings, not model weights and not human-authored notes. Records are inspectable through code/TUI/events but not naturally diffable or linkable as primary knowledge artifacts.

**Scope.** Per-crew, per-flow, per-agent, or user-provided memory scope. Shared crew memory is rooted under the crew; agent-level memory can use `MemoryScope` for a private subtree; `MemorySlice` can expose several scopes as a read-only or writable view ([memory_scope.py](https://github.com/crewAIInc/crewAI/blob/1d6f84c7aab08bf460a08180a1fc7f15326f22ab/lib/crewai/src/crewai/memory/memory_scope.py)).

**Timing.** Online during deployment. Agent task results and standalone runs are stored after execution; memories are recalled before later tasks or agent kickoff; HITL lessons are recalled before review and updated after feedback. There is no offline sweep over many sessions in the inspected code.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), CrewAI adds a "framework-integrated runtime memory" case: the agent framework owns the trace boundary and memory hooks, but the promotion target is still symbolic memory records. It strengthens the survey's symbolic-artifact claim and splits the service-backed category: not every database-backed trace learner is an external memory service; some are embedded directly in the agent runtime.

## Curiosity Pass

**The HITL loop is more learning-shaped than the generic task-output memory.** Generic task-output extraction may just preserve useful facts. HITL lesson extraction has a stronger oracle: a human provided feedback, and the prompt asks for reusable guidance rather than facts. If any part of CrewAI Memory should be studied as learning rather than recall, it is this path.

**`private=True` is a retrieval filter, not a security boundary.** Private records are hidden unless the caller's `source` matches or `include_private=True` is passed. That is useful for default behavior, but it is not comparable to SAGE-style RBAC or tenant-enforced ACLs. Treat it as scoping policy inside trusted code.

**Scope inference is doing too much semantic work.** Letting the LLM grow a scope tree organically reduces setup cost, but it makes organization non-reproducible. Over time the tree can encode arbitrary one-off judgments about where a fact "belongs." For user personalization memory this may be acceptable; for methodology knowledge it would be a liability.

**Consolidation is local, not conceptual.** The code compares a new item against a small set of similar records and chooses keep/update/delete/insert. That prevents duplicate accumulation, but it cannot notice that five weak records should become one stronger abstraction unless they happen to be close in embedding space and arrive through the same save path.

**The docs slightly overstate the storage default.** The docs say default storage is `./.crewai/memory`, but the inspected LanceDB constructor uses `$CREWAI_STORAGE_DIR/memory` when set and otherwise falls back to CrewAI's platform data directory; explicit path strings are supported. This is documentation drift, not a memory-design issue, but it is the kind of detail that matters for operators.

## What to Watch

- Whether the human-feedback lesson path grows lifecycle controls: confidence, supersession, expiry, or review states.
- Whether CrewAI adds a typed split between task facts, user preferences, agent lessons, and project decisions, or continues to rely on scopes/categories.
- Whether Qdrant Edge becomes a first-class default for multi-process crews or stays an optional backend.
- Whether the Memory TUI grows editing/review affordances; that would move the system closer to a curatable knowledge medium.
- Whether benchmark evidence appears for composite scoring and RecallFlow against simpler vector search. The mechanisms are plausible, but the inspected repo does not prove the weight defaults.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: CrewAI is a framework-integrated trace-to-symbolic-memory case, distinct from external services and offline trajectory learners
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — contrasts: CrewAI persists deployment-time artifacts but does not provide a lifecycle for constraining or codifying them into stronger forms
- [The verifiability gradient](../../notes/verifiability-gradient.md) — contrasts: CrewAI's importance floats and consolidation decisions do not indicate how verified a memory has become
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — sharpens: CrewAI's database backend still stores symbolic artifacts; the backend choice is separate from representational form
- [Flat memory predicts specific cross-contamination failures that are empirically testable](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — predicts: CrewAI's single record model plus scope tree should be tested for operational debris and preference/knowledge mixing
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — contrasts: CrewAI optimizes recall selection, but returned records are still full strings rather than progressive disclosure artifacts
- [Claw learning loops must improve action capacity not just retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — grounds: HITL lessons are action-capacity learning, while generic memory recall is mostly retrieval improvement
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — suggests: CrewAI's task-output memories resemble workshop traces that would need an extraction bridge before becoming durable library knowledge
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: CrewAI automates extraction and local consolidation but leaves judgment-heavy synthesis and lifecycle promotion unsolved
- [ClawVault](./clawvault.md) — compares: both mine runtime traces into symbolic artifacts, but ClawVault has a richer observation/promotion lifecycle while CrewAI has deeper in-framework integration
- [OpenViking](./openviking.md) — compares: both use LLM memory extraction and deduplication; OpenViking owns a service-style message schema, while CrewAI integrates memory directly into agent and flow execution
