---
description: "xMemory review: trace-derived hierarchical agent memory with JSONL stores, Chroma/BM25 search, semantic themes, graph files, and pull-only retrieval"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-05"
---

# xMemory

xMemory, from `HU-xiaobai/xMemory`, is research code accompanying the 2026 paper "Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation." The inspected implementation is a Python library and evaluation harness that turns conversation messages into episodic summaries, semantic statements, theme nodes, kNN neighborhoods, and a hierarchical graph, then retrieves over those retained layers with BM25, Chroma embeddings, and evaluation-time hierarchical selection.

**Repository:** https://github.com/HU-xiaobai/xMemory

**Reviewed commit:** [375ae1495095aa14a39eb169f83737f4779391c6](https://github.com/HU-xiaobai/xMemory/commit/375ae1495095aa14a39eb169f83737f4779391c6)

**Last checked:** 2026-06-05

## Core Ideas

**xMemory treats dialogue memory as a bounded, coherent stream rather than a generic document corpus.** The README argues that ordinary fixed top-k RAG returns redundant spans for agent memory and can prune temporally linked prerequisites, then positions xMemory as decoupling memories into components and aggregating through a hierarchy ([README.md](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/README.md)). The code mirrors this: messages are buffered, boundary detection creates episodes, semantic extraction creates atomic statements, and optional CAM-inspired routines organize semantics into themes and a graph ([src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py), [src/core/memory_hierarchy.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_hierarchy.py)).

**The write path is trace-derived and LLM-mediated.** `add_messages()` stores incoming role/content/timestamp records in a per-user buffer, runs LLM boundary detection when configured, creates an episode from buffered messages, and publishes an `episode_created` event that schedules asynchronous semantic generation ([src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py), [src/core/boundary_detector.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/boundary_detector.py)). Episodes preserve original messages, and semantic memories are extracted from episodes by either direct LLM extraction or a prediction-correction loop over existing semantic memory ([src/generation/episode_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/episode_generator.py), [src/generation/semantic_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/semantic_generator.py), [src/generation/prediction_correction_engine.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/prediction_correction_engine.py)).

**The hierarchy is an access structure, not just a visualization.** `ThemeManager` attaches new semantic nodes to theme centroids, splits oversized or heterogeneous themes, merges similar small themes when a sparsity-plus-semantics score improves, recomputes theme kNN edges, and persists theme summaries/vectors ([src/core/memory_hierarchy.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_hierarchy.py)). `HierarchicalMemoryGraph` persists message, episode, semantic, and theme nodes plus cross-level edges to GEXF, so later retrieval and analysis can operate over the retained structure ([src/core/memory_hierarchy.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_hierarchy.py)).

**Context efficiency is the central design move.** The library defaults to bounded buffers, top-k episode and semantic retrieval, Chroma vector search, BM25 lexical search, reciprocal-rank fusion, caches, and per-user index loading ([src/config.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/config.py), [src/search/unified_search.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/search/unified_search.py), [src/search/chroma_search.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/search/chroma_search.py)). The LoCoMo evaluation harness adds query answering over selected episodic and semantic memory, plus an adaptive hierarchy strategy that selects representatives and tracks prompt-token use ([evaluation/locomo/xMemory_search_framework.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/xMemory_search_framework.py)).

**The adoption surface is library plus scripts, not an agent runtime wrapper.** The public `xMemory` facade exposes `add_messages`, `flush`, `wait_for_semantic`, `search`, theme updates, graph updates, and async search ([src/api/facade.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/api/facade.py)). I did not find a deployed integration that automatically injects retrieved memory into a host agent's next model call; the repository shows construction and retrieval APIs plus evaluation scripts.

## Artifact analysis

- **Storage substrate:** `files` `vector` `graph` `in-memory` - Episodes and semantic memories persist as per-user JSONL files under `storage_path`; ChromaDB persists episode and semantic embedding collections; theme JSONL/vector files and semantic-kNN JSON files persist hierarchy access structures; GEXF and `.npy` files persist the hierarchy graph; buffers, caches, task state, and search indices also live in memory while the process runs ([src/storage/episode_storage.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/storage/episode_storage.py), [src/storage/semantic_storage.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/storage/semantic_storage.py), [src/search/chroma_search.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/search/chroma_search.py), [src/core/memory_hierarchy.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_hierarchy.py)).
- **Representational form:** `prose` `symbolic` `parametric` - Episode titles/content, semantic statements, theme summaries, prompts, and answer contexts are prose; JSONL records, metadata fields, source episode ids, theme ids, graph nodes/edges, BM25 token indexes, thresholds, and search strategies are symbolic; embeddings, Chroma vectors, centroid similarities, kNN weights, and ranking scores are parametric.
- **Lineage:** `authored` `trace-extracted` - Source code, prompts, configuration, and evaluation scripts are authored; episodes, semantic memories, themes, semantic kNN files, graph nodes, and graph edges are derived from message traces, episode summaries, semantic extraction, embeddings, and LLM-generated theme summaries. I did not find imported external knowledge as a standing memory lineage beyond evaluation datasets used as input traces.
- **Behavioral authority:** `knowledge` `routing` `ranking` `learning` - Episodes, semantic statements, theme summaries, and graph nodes serve as knowledge artifacts for answering questions; user ids, episode ids, semantic ids, theme ids, graph edges, search methods, and hierarchy levels route retrieval; BM25/vector/RRF/kNN/centroid scores rank candidate memories; prediction-correction, semantic extraction, theme splitting/merging, and graph construction learn durable memory structure from traces. The library also has validation-like guards around config and duplicate detection, but these are operational checks rather than a reviewed memory governance layer.

**Episode records.** Episodes are LLM-generated summaries over buffered messages, persisted with original message payloads, message counts, boundary reasons, and timestamps. They are both knowledge artifacts and source material for semantic extraction ([src/generation/episode_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/episode_generator.py), [src/models/episode.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/models/episode.py)).

**Semantic memories.** Semantic memory rows are atomic prose statements linked back to source episode ids, stored in JSONL, embedded into Chroma, checked for vector-duplicate similarity, and exposed to retrieval as semantic results ([src/generation/semantic_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/semantic_generator.py), [src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py), [src/storage/semantic_storage.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/storage/semantic_storage.py)).

**Themes, kNN files, and hierarchy graph.** Theme nodes aggregate semantic memories into higher-level summaries with centroids, neighbors, and member ids. The graph connects message -> episode -> semantic -> theme, but message nodes are only added when callers pass message dictionaries to the graph update path; the ordinary episode path currently has empty `message_ids` unless the `Episode` object carries a `messages` attribute ([src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py), [src/core/memory_hierarchy.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_hierarchy.py)).

**Promotion path.** xMemory promotes raw message traces into episodes, episodes into semantic statements, semantic statements into theme summaries and kNN neighborhoods, and those layers into graph structure. The promotion increases abstraction and routing/ranking authority, but does not promote findings into reviewed notes, explicit rules, or validators.

## Comparison with Our System

| Dimension | xMemory | Commonplace |
|---|---|---|
| Primary purpose | Runtime/evaluation memory retrieval for dialogue agents | Git-native methodology KB for agents and maintainers |
| Canonical retained artifact | JSONL episode, semantic statement, theme, graph node, embedding index | Typed Markdown artifact with citations, links, validation, and review |
| Write path | Automatic trace extraction, prediction-correction, hierarchy maintenance | Authored notes, snapshots, indexes, validation, and semantic review |
| Read-back | Explicit search/API/evaluation retrieval | Explicit file/index/link retrieval and loaded instructions |
| Governance | Similarity thresholds, config checks, duplicate detection, evaluation metrics | Collection contracts, schemas, citations, review gates, deterministic validation |

xMemory is stronger than Commonplace at turning a long dialogue trace into a compact, multi-level retrieval structure. Commonplace is stronger at inspectable authority: a note's source, type, review status, and links are visible in the repository before it shapes later work. xMemory's generated hierarchy can improve answer-time context economy, but its LLM extraction and theme summaries are not retained with claim-level citations or review state.

The main design divergence is what counts as durable knowledge. xMemory's durable units are generated from behavior traces and optimized for retrieval diversity; Commonplace's durable units are authored or reviewed artifacts optimized for reuse, critique, and maintenance. For Commonplace, xMemory is evidence that hierarchical compression can be useful, but also a warning that generated abstractions need provenance before they become high-authority methodology.

### Borrowable Ideas

**Decoupling before aggregation.** Commonplace could use a light version for large source snapshots: extract small source-grounded statements first, then cluster or route them into higher-level review sections. Ready only when paired with preserved citations.

**Representative selection over redundant memory.** xMemory's theme/semantic coverage logic is a useful alternative to naive top-k for long review histories or repeated warnings. Needs a concrete retrieval workload before implementation.

**Prediction-correction extraction.** The loop "predict from existing memory, compare with new episode, extract differences" is an interesting way to avoid restating known facts. Commonplace could test it on workshop logs, but not as durable note creation without human or semantic-gate review.

**Hierarchical graph as an optional access artifact.** A graph connecting raw messages, episodes, semantic claims, and themes could help review trace-derived work. It should remain an access structure, not a source of authority by itself.

**Do not borrow opaque theme promotion directly.** Theme split/merge decisions are useful for context economy, but Commonplace would need visible source memberships, invalidation, and review state before generated themes influence instructions or indexes.

## Write side

**Write agency:** `manual` `automatic` - Users manually call library methods, scripts, `flush`, theme update, graph update, and search routines; automatic writes create episodes from buffers, generate semantic memories asynchronously after episode creation, deduplicate by embedding similarity, add BM25/Chroma indexes, maintain semantic kNN files, update themes through attach/split/merge/coalesce operations, and persist hierarchy graphs.

**Curation operations:** `dedup` `consolidate` `evolve` `promote` - Semantic writes skip near-duplicates by vector similarity; episodes and theme summaries consolidate lower-level traces/statements into shorter prose units; existing themes evolve through appended semantic ids, recomputed centroids, summaries, neighbors, and split/merge operations; semantic statements are promoted into theme membership, kNN neighborhoods, and graph nodes. Extraction from newly arriving messages is acquisition from traces, not itself a curation operation on already-stored memory.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` `trajectories` - xMemory consumes ordered role/content/timestamp message streams and stores them as episodes and source traces. It does not require tool-call traces in the core library, though evaluation data can include multimodal/search metadata in message content ([evaluation/locomo/add.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/add.py)).

**Learning scope:** `per-project` `cross-task` - The core storage is scoped by `user_id`; within that scope, accumulated episodes, semantic memories, themes, and graph structure can affect later searches across questions/tasks over the same memory store.

**Learning timing:** `online` `staged` - Episode creation can happen online as messages are added or when a caller flushes the buffer; semantic generation is asynchronous after episode creation; theme and graph updates are staged through explicit facade calls using the latest incremental episode/semantic batches.

**Distilled form:** `prose` `symbolic` `parametric` - Distilled artifacts include prose episode summaries, semantic statements, and theme summaries; symbolic JSONL/GEXF records, ids, edges, and metadata; and parametric embeddings, centroids, neighbor similarities, and retrieval scores.

**Extraction.** The extraction oracle is LLM-based. Boundary detection asks whether buffered conversation has reached an episode break; episode generation summarizes message lists; semantic generation either extracts persistent statements directly or predicts an episode from relevant existing semantic statements and extracts new knowledge from the mismatch ([src/core/boundary_detector.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/boundary_detector.py), [src/generation/episode_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/episode_generator.py), [src/generation/semantic_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/semantic_generator.py), [src/generation/prediction_correction_engine.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/prediction_correction_engine.py)).

**Scope and timing.** The durable learning loop can run during a session, but the full hierarchy requires callers to wait for semantic generation, fetch incremental batches, update themes, update the graph, and mark the batch consumed ([src/api/facade.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/api/facade.py)). That makes the core trace-derived memory automatic, while the highest-level graph assembly is an explicit staged maintenance step.

**Survey fit.** xMemory fits the trace-to-hierarchical-retrieval family. It strengthens the survey claim that trace-derived memory can be more than flat facts: the retained behavior-shaping artifact is also an access hierarchy that affects diversity, abstraction level, and search cost.

## Read-back

**Read-back:** `pull` - The implemented library read path is explicit `search`/`search_all`/`asearch` retrieval over a caller-provided query and user id; I did not find a host-agent wrapper that pushes retained xMemory content into a model invocation without an explicit search or evaluation step.

The evaluation harness does place retrieved semantic and episodic memories into an answer prompt, but that is a scripted question-answering run after a search strategy has selected memories, not an ambient agent integration that automatically recalls memory for arbitrary future actions ([evaluation/locomo/xMemory_search_framework.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/xMemory_search_framework.py)). Direct library consumers receive result dictionaries; they decide whether and how to feed those results to a model.

Selection is bounded by configured top-k episode and semantic counts, BM25/vector/hybrid method choice, Chroma query limits, RRF fusion, per-user loading caches, and the evaluation harness's hierarchy/representative-selection strategy. Actual retrieval precision, answer faithfulness, and context dilution are evaluated in LoCoMo scripts and metrics, but the library code itself does not include a with/without memory ablation or post-action audit proving that retrieved memories faithfully change downstream agent behavior.

Other consumers include the evaluation scripts, graph visualization tooling, any application using the `xMemory` facade, and humans inspecting generated JSONL, GEXF, result JSON, token stats, and score files.

## Curiosity Pass

**The hierarchy is only partly wired into the public runtime.** The facade exposes incremental theme and graph maintenance, but ordinary `search()` still delegates to episode/semantic search; the more elaborate adaptive hierarchy appears mainly in the LoCoMo evaluation harness.

**Message-level graph edges may be sparse in ordinary use.** `HierarchicalMemoryGraph` supports message nodes and message-to-episode edges, but `_fetch_new_episodes_for_user()` emits empty `message_ids` unless the episode object has a `messages` attribute. Episodes do preserve `original_messages`, so the raw material is not lost, but the graph path may not connect every raw message automatically.

**The README's "faithful high-level node organisation" is structurally plausible but not provenance-rich.** Theme summaries carry member semantic ids and embeddings, not claim-level source citations or review decisions. That is enough for retrieval structure and visualization, not enough for high-authority KB claims.

**The prediction-correction loop is more interesting than standard extraction.** It tries to learn what existing memory failed to predict from a new episode. If effective, that is a real context-efficiency mechanism: it stores deltas rather than repeatedly storing obvious facts.

## What to Watch

- Whether xMemory wires hierarchy search into the public facade, not only the evaluation harness; that would change the central read-back mechanism from flat episode/semantic pull to hierarchical pull.
- Whether theme and semantic outputs gain source-span provenance or review metadata; that would make generated abstractions safer to reuse outside benchmark answering.
- Whether the repository adds automatic pre-call recall wrappers for agents; that would change the read-back verdict from pull to both.
- Whether graph construction gets reliable message-level edges from ordinary episode creation; that would strengthen lineage from raw messages through episodes, semantics, and themes.
- Whether prediction-correction is evaluated separately from ordinary semantic extraction; that would tell us whether the delta-learning idea is worth borrowing.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: xMemory derives episodes, semantic memories, themes, and graph structure from conversation traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: xMemory stores memory but exposes pull retrieval rather than automatic agent activation in the inspected code.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: xMemory's JSONL records, Chroma indexes, themes, graph files, and evaluation prompts carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: episodes, semantic statements, and theme summaries advise later answering.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: xMemory converts conversation traces into durable abstractions for later retrieval.
