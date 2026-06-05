---
description: "xMemory review: trace-derived episodic and semantic memory with theme hierarchy, kNN structure, adaptive retrieval, and entropy-gated expansion"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# xMemory

> Replaced 2026-06-05. See [xMemory](./xMemory.md) for the current review.

xMemory, by HU-xiaobai, is the code release for "Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation." At the reviewed commit it is a Python research memory system and LoCoMo evaluation pipeline: conversations are buffered into LLM-generated episodes, episodes are distilled into semantic memories, semantic memories are clustered into themes and graph edges, and retrieval can answer benchmark questions through a hierarchy-aware search strategy rather than flat top-k RAG.

**Repository:** https://github.com/HU-xiaobai/xMemory

**Reviewed commit:** [375ae1495095aa14a39eb169f83737f4779391c6](https://github.com/HU-xiaobai/xMemory/commit/375ae1495095aa14a39eb169f83737f4779391c6)

**Last checked:** 2026-06-02

## Core Ideas

**The memory write path starts from dialogue traces.** `xMemory.add_messages()` delegates to `MemorySystem.add_messages()`, which converts incoming role/content/timestamp dictionaries into `Message` objects, runs LLM boundary detection when enabled, buffers by user, and creates episodes from completed buffers or explicit flushes ([src/api/facade.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/api/facade.py), [src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py), [src/core/boundary_detector.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/boundary_detector.py)).

**Episodes preserve the raw trace and an LLM narrative.** `EpisodeGenerator.generate_episode()` formats original messages, asks an LLM for a title, narrative content, and timestamp, then stores both the generated episode and `original_messages` in the episode object ([src/generation/episode_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/episode_generator.py), [src/models/episode.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/models/episode.py)). This keeps a useful evidence trail, but the generated narrative itself is not reviewed or source-cited beyond the retained message list.

**Semantic memory uses prediction-correction over prior knowledge.** After an episode is created, an event schedules background semantic generation. With default config, the `PredictionCorrectionEngine` retrieves relevant existing semantic statements, predicts the likely episode, compares that prediction to the original conversation, and extracts high-value persistent facts that become `SemanticMemory` records with source episode ids ([src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py), [src/generation/semantic_generator.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/semantic_generator.py), [src/generation/prediction_correction_engine.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/generation/prediction_correction_engine.py), [src/models/semantic.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/models/semantic.py)).

**Themes are the distinctive index layer.** New semantic memories are absorbed into `ThemeNode` clusters by centroid similarity, split when they exceed size or heterogeneity thresholds, merged or coalesced when close enough, summarized by an LLM, and saved as JSONL plus local vector arrays. The theme manager also computes theme kNN neighbors used later for representative selection ([src/core/memory_hierarchy.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_hierarchy.py), [src/core/memory_system.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/core/memory_system.py)).

**Context efficiency is structural, not just top-k.** Baseline search combines BM25 and Chroma vector retrieval with separate episode and semantic top-k values, but the advertised xMemory path is `adaptive_hier`: load themes, semantic memories, semantic kNN, episodes, and embeddings; pick representative themes and semantics by graph coverage plus query score; then use entropy/information-gain checks to decide which episodes and original messages deserve expansion ([src/search/unified_search.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/search/unified_search.py), [evaluation/locomo/xMemory_search_framework.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/xMemory_search_framework.py)). The design manages both volume and complexity by selecting high-level themes first, narrowing semantics, and only expanding episodes when the answer uncertainty improves.

**The public API is small, while the research harness carries much of the behavior.** The `xMemory` facade exposes add, flush, wait, search, stats, and explicit hierarchy-update helpers. LoCoMo construction code calls `fetch_incremental_batches()`, `update_themes()`, `update_hierarchy_graph()`, and `mark_incremental_consumed()` after semantic generation; the benchmark searcher then reads persisted hierarchy files directly ([src/api/facade.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/api/facade.py), [evaluation/locomo/add.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/add.py), [evaluation/locomo/xMemory_search_framework.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/xMemory_search_framework.py)).

## Artifact analysis

- **Storage substrate:** `vector` — Per-user JSONL files under `storage_path/episodes/`, Chroma episode collections, BM25 indexes, caches, and optional graph nodes
- **Representational form:** `prose` `symbolic` `parametric` — prose trace narratives/facts/summaries, symbolic metadata/original-message JSON/timestamps/graph and kNN sidecars, and distributed-parametric embeddings
- **Lineage:** `authored` `trace-extracted` — authored prompts, thresholds, retrieval policy, and answer assembly operate over conversation traces distilled into episodes, semantic memories, themes, graph edges, and sidecars
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — episodes and semantic facts advise as knowledge; prompts instruct answer generation; themes, kNN, entropy gates, and retrieval policy route/rank context; extraction and hierarchy updates learn from traces

**Episode records.** Storage substrate: per-user JSONL files under `storage_path/episodes/`, Chroma episode collections, BM25 indexes, caches, and optional graph nodes. Representational form: mixed prose trace narrative, symbolic metadata, original-message JSON, timestamps, and distributed-parametric embeddings. Lineage: trace-derived from conversation messages, transformed by LLM boundary detection and episode generation; invalidated by changes to prompts, message timestamps, boundary configuration, model behavior, or source conversations. Behavioral authority: knowledge artifact when retrieved as evidence or context; ranking artifact through BM25/vector indexes; weak audit artifact because original messages are preserved but not independently validated.

**Semantic memory records.** Storage substrate: per-user `semantic/*.jsonl`, Chroma semantic collections, semantic embedding caches, and `semantic_knn/*.json`. Representational form: prose facts plus symbolic type, confidence, source episode ids, revision count, and embeddings. Lineage: trace-derived from episodes and original messages through either prediction-correction or per-episode extraction prompts; source episode ids preserve a useful but coarse evidence link. Behavioral authority: knowledge artifact when read as facts; ranking and neighborhood artifact through vector similarity, semantic kNN, duplicate checks, and retrieval scoring.

**Theme layer.** Storage substrate: `themes/{user}_themes.jsonl`, `themes/vector/{user}_theme_ids.json`, `themes/vector/{user}_embeddings.npy`, optional Chroma theme collection, and in-memory `ThemeManager` state. Representational form: mixed symbolic cluster membership, centroids, neighbor ids/scores, and LLM prose summaries. Lineage: derived from semantic memories by centroid attachment, split/merge/coalescing thresholds, the sparsity-plus-semantics scoring function, and LLM summarization. Behavioral authority: system-definition artifact for retrieval because it routes which semantic memories and episodes are considered; knowledge artifact when theme summaries are injected into answer context.

**Hierarchical memory graph.** Storage substrate: NetworkX graph persisted as `graphs/{user}_memory_graph.gexf`; embeddings are tracked in graph node attributes during construction but sanitized out of GEXF. Representational form: symbolic graph nodes and typed edges linking episode, semantic, and theme levels, plus prose text attributes. Lineage: incrementally derived from the latest episode/semantic/theme batch; no message-level nodes are currently added by the LoCoMo construction path. Behavioral authority: diagnostic and structural routing evidence; the benchmark searcher mainly consumes the theme and semantic sidecar files rather than traversing the GEXF graph directly.

**Retrieval and answer pipeline.** Storage substrate: source code, config, generated result JSON, token stats, and loaded hierarchy files. Representational form: symbolic thresholds/top-k values, embedding similarity, graph-neighbor maps, entropy estimates, prompt templates, and assembled prose context. Lineage: authored retrieval policy operating over current memory artifacts and the current question. Behavioral authority: system-definition artifact with selection, ranking, prompt-construction, and evaluation force over what the answer LLM sees.

Promotion path: raw dialogue messages become episodes, episodes become semantic memories, semantic memories become themes and graph edges, and retrieval turns selected themes/semantics/episodes into prompt-visible context. The path raises authority from trace evidence to retrieval-routing artifacts, but it does not promote memories into reviewed rules, executable skills, validators, or host instructions.

## Comparison with Our System

| Dimension | xMemory | Commonplace |
|---|---|---|
| Primary purpose | Research memory index for long dialogue QA | Agent-operated methodology KB with typed Markdown artifacts |
| Canonical retained artifacts | Episodes, semantic facts, themes, semantic kNN, hierarchy graph | Notes, instructions, reviews, sources, type specs, generated indexes |
| Storage substrate | JSONL files, Chroma, BM25, numpy arrays, GEXF, result JSON | Git-native Markdown plus generated indexes/reports |
| Write path | Message traces -> LLM episode -> LLM semantic extraction -> theme/graph update | Authored or source-derived artifacts under collection/type contracts |
| Read-back | Pull API plus evaluation-time adaptive push into the answer prompt | Mostly pull through search/indexes/links, with explicit loaded instructions and gates |
| Governance | Prompts, thresholds, duplicate checks, benchmark metrics | Type specs, validation, source citations, review gates, git diffs |

xMemory is stronger than Commonplace on one narrow axis: high-volume dialogue memory can be compressed into a multi-level retrieval structure whose query path spends context on themes, semantics, episodes, and raw messages only as needed. Commonplace is stronger on artifact governance. Its durable claims are files with frontmatter, source links, type contracts, review status, validation, and replacement history; xMemory's learned facts and themes are useful retrieval state, but they lack review state, citation granularity, contradiction handling, or promotion gates.

The architectural lesson is not "use themes instead of notes." xMemory's themes are retrieval-control summaries over many small semantic facts, not durable explanatory notes. In Commonplace terms they look more like generated indexes or search-side clusters than library artifacts. Treating them as notes would overstate their lineage and authority.

**Read-back:** `both` — The `xMemory.search()` facade is an explicit pull interface, while the LoCoMo `adaptive_hier` answer loop performs relevance- and entropy-gated retrieval over retained memories before `answer()` assembles them into the LLM prompt

### Borrowable Ideas

**Use hierarchy as a retrieval budget controller.** Needs a concrete search layer first. Commonplace could generate theme-like clusters for large source/review collections, but the output should be a routing aid or report, not an authoritative note.

**Borrow entropy-gated expansion for expensive evidence.** Worth prototyping in review/report workflows. xMemory's episode information-gain check is a sharper rule than "read the top-k full files"; Commonplace could test a similar gate for deciding when to open full source snapshots after index hits.

**Keep raw trace, distilled fact, and routing summary separate.** Ready now as vocabulary discipline. xMemory's episode/semantic/theme split maps cleanly onto Commonplace's distinction between evidence, distilled knowledge artifact, and generated navigation artifact.

**Do not borrow automatic semantic-fact promotion without review.** Ready as a caution. xMemory accepts LLM-extracted facts when duplicate checks pass; Commonplace should require citations and review before any extracted fact affects methodology notes or instructions.

**Treat graph sidecars as operational indexes, not the knowledge base.** Ready now. A GEXF or kNN sidecar can improve navigation, but the durable library still needs inspectable files and source-grounded claims.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
- **Trace source:** `session-logs` — conversation messages with speaker roles, content, timestamps, annotations, and retained original-message lists
- **Learning scope:** `per-task` — memory is scoped per user/conversation id rather than project-wide or global
- **Learning timing:** `online` `staged` — episodes are written while messages are added or flushed, while semantic generation, theme updates, and hierarchy updates run in delayed stages
- **Distilled form:** `prose` `symbolic` `parametric` — LLM episode narratives, semantic facts, theme summaries, symbolic metadata/sidecars/graph structure, and embeddings

**Trace source.** xMemory qualifies as trace-derived. The raw traces are conversation messages from benchmark or API inputs: speaker roles, content, timestamps, image/search annotations in LoCoMo preprocessing, and original message lists retained inside episodes ([evaluation/locomo/add.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/add.py), [src/models/episode.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/models/episode.py)).

**Extraction.** The first extraction boundary is episode creation: LLM boundary detection decides whether the current buffer should close, then an LLM turns buffered messages into an episode title/content/timestamp. The second boundary is semantic extraction: default prediction-correction retrieves relevant prior semantic facts, predicts the new episode, compares prediction against original messages, and extracts persistent high-value knowledge. The third boundary is theme construction: semantic memories are clustered, summarized, split, merged, and linked by kNN and graph edges.

**Scope and timing.** Scope is per user/conversation id. Episode writes happen online while messages are added or flushed. Semantic generation is scheduled in a background executor after episode creation. Theme and hierarchy updates are explicit post-processing calls in the LoCoMo construction script, not automatic inside every `add_messages()` call. Read-back happens later at question time.

**Survey placement.** xMemory belongs in the trace-to-symbolic-artifact branch of the trace-derived survey, with a distinctive retrieval-index emphasis: the learned behavior is not a model weight or executable skill, but a hierarchy of extracted facts, summaries, kNN sidecars, and selection policies that change future context assembly. It strengthens the survey's split between raw trace retention and derived retrieval-control state.

## Read-back placement

**Direction.** xMemory is both pull and push over retained memory. The library facade exposes explicit pull through `search()`. The LoCoMo QA harness turns a question into pre-answer retrieval, then pushes selected episode, semantic, and theme memories into the answer prompt. That push is memory read-back, not shipped baseline documentation.

**Read-back signal:** `inferred / embedding` — the engineered push path keys on the current question by embedding similarity over semantic memories, themes, and episode candidates before entropy/information-gain refinement

**Faithfulness tested:** `no` — the review found benchmark answer evaluation and token statistics, not a general with/without-memory behavioral ablation or deployment-time faithfulness gate

**Targeting and signal.** The push path is instance-targeted: it keys on the current question, not on an always-load or generic session-start event. The primary signal is `inferred / embedding`: `adaptive_hier` embeds the question, scores semantic memories and themes by cosine similarity, then builds episode candidates from source episodes plus vector hits. The selection is mixed because semantic/theme neighbor coverage and entropy/information-gain checks refine the final payload, but the first instance selector is content-derived embedding similarity rather than an assigned identifier ([evaluation/locomo/xMemory_search_framework.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/xMemory_search_framework.py)). The baseline explicit `search()` path also supports `inferred / lexical` BM25 and vector/hybrid ranking, but that is pull unless a host wraps it into pre-action prompt assembly.

**Injection point.** Read-back happens before answer generation in the evaluation loop, so it can change the response. Semantic generation and theme updates happen after prior conversations, so they affect later questions rather than the current trace.

**Selection, scope, and complexity.** The adaptive path has explicit caps such as semantic pool size, maximum themes, maximum semantic memories, episode vector candidates, probe count, and episode maximum. It reduces context complexity by showing theme and semantic summaries first, then expands only selected episodes and optionally original messages. Actual context dilution and retrieval precision are not verified from code.

**Authority at consumption.** Retrieved memories are advisory context for the answer LLM, not hard gates. The `ANSWER_PROMPT` instructs the model to answer from semantic and episodic memories, but the repository does not prove the model faithfully follows the supplied memory under perturbation.

**Faithfulness.** The repo includes LoCoMo evaluation scripts, generated score tooling, LLM judge utilities, and token accounting. I did not find a general with/without-memory behavioral ablation for arbitrary host agents; the code-grounded evidence is benchmark answer evaluation and token statistics rather than a deployment-time faithfulness gate.

**Other consumers.** Human researchers consume result JSON, score files, token stats, and optional GEXF graph visualization. Those are evaluation and inspection surfaces, not additional runtime activation channels.

## Curiosity Pass

**The README's top-down hierarchy claim is implemented mostly in evaluation code.** The library facade exposes helper methods, but the sophisticated `adaptive_hier` selector lives in `evaluation/locomo/xMemory_search_framework.py`, not in a general production API.

**The GEXF graph is less central than the theme/semantic sidecars.** `update_hierarchy_graph()` writes a graph, but the adaptive searcher loads themes, semantics, semantic kNN, and episodes directly. The graph is useful for analysis, while retrieval authority mostly sits in JSONL/numpy sidecars and search code.

**Original-message expansion is selective and late.** Episodes preserve original messages, but the answer context only expands them when `expand_original` is set by the entropy-gated search path and within the configured expansion limit.

**Config construction requires an OpenAI key even when the README emphasizes local/HF Llama inference.** `MemoryConfig.__post_init__()` raises without `OPENAI_API_KEY`, while evaluation scripts inject a local/HF LLM for some paths. That makes the adoption story more research-environment-specific than the README's high-level explanation suggests ([src/config.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/src/config.py), [evaluation/locomo/add.py](https://github.com/HU-xiaobai/xMemory/blob/375ae1495095aa14a39eb169f83737f4779391c6/evaluation/locomo/add.py)).

**The duplicate threshold default is effectively exact.** `semantic_similarity_threshold` defaults to `1`, so semantic deduplication is conservative unless configured otherwise. That protects recall but can leave redundant facts for the hierarchy to manage.

## What to Watch

- Whether `adaptive_hier` moves from the LoCoMo evaluation script into the public `xMemory.search()` API. That would make the hierarchy a general activation mechanism rather than a benchmark harness feature.
- Whether semantic memories gain contradiction, expiry, provenance review, or confidence-update workflows. That would change them from retrieval facts toward governed memory artifacts.
- Whether theme summaries gain source-span provenance back to contributing semantic facts and episodes. Without that, themes should remain generated routing summaries rather than durable knowledge.
- Whether the graph file becomes a retrieval substrate instead of an analysis sidecar. That would make graph lineage and update consistency more important.
- Whether evaluations include with/without-memory and perturbation tests for answer faithfulness, not just answer quality and token efficiency.

## Bottom Line

xMemory is a code-grounded trace-derived memory system for long dialogue QA. Its strongest contribution is the retrieval-control stack: message traces become episodes, semantic facts, themes, kNN neighborhoods, and entropy-gated episode expansion before answer generation. Commonplace should borrow the artifact split and expansion-gate idea, but not the automatic promotion policy: xMemory's learned facts and themes are useful retrieval state, not reviewed knowledge artifacts with enough lineage to become instructions or methodology claims.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: xMemory derives episodes, semantic facts, themes, and retrieval sidecars from conversation traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: stored episodes and semantic facts affect answers only through search and prompt assembly.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: xMemory separates episodes, semantic memories, themes, kNN sidecars, graph files, and prompt builders by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: episodes and semantic facts primarily advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: extraction prompts, theme clustering, retrieval thresholds, and answer prompt assembly constrain future behavior.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: dialogue traces are distilled into reusable memory artifacts that shape later answer context.
