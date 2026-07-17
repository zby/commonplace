---
description: "AriGraph review: in-run knowledge-graph world model with episodic observation memory, Contriever retrieval, LLM extraction/refinement, and prompt pushback"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# AriGraph

AriGraph, from AIRI Institute, is a research codebase for a TextWorld and QA memory architecture: observations or paragraphs are converted into graph facts, stale/conflicting graph entries are refined, embedding retrieval selects relevant subgraphs and episodic observations, and the pipeline pushes those memories into planning, action, or answer prompts. The reviewed implementation is primarily an in-process experiment harness rather than a reusable persistent memory service.

**Repository:** https://github.com/AIRI-Institute/AriGraph

**Reviewed commit:** [e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2](https://github.com/AIRI-Institute/AriGraph/commit/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2)

**Last checked:** 2026-06-04

## Core Ideas

**The central memory is a learned world graph, not a note store.** The README describes AriGraph as a semantic knowledge graph with episodic vertices and edges for TextWorld agents, and the code implements the main path with `ContrieverGraph`, a `TripletGraph` subclass that stores triplets, embeddings, observation episodes, and retrieved episodic candidates in object fields ([README.md](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/README.md), [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [graphs/parent_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/parent_graph.py)). The store is reset for each game attempt or QA task in the inspected pipelines, so its authority is strongest inside an episode, not across projects.

**LLMs write symbolic graph facts from traces.** Each game step calls `graph.update(...)`; the graph prompts an LLM to extract triplets from the current observation, asks another prompt which existing triplets should be replaced, deletes predicted outdated triplets, adds navigation edges, and embeds new triplets ([pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py), [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py)). That makes the graph trace-derived and symbolic, with parametric embeddings as the access structure.

**Read-back combines graph-neighborhood retrieval and episodic recall.** Current observations and plans are first reduced to "crucial items"; each item seeds Contriever search over triplet strings and graph expansion, while episodic observations are ranked by plan embedding plus overlap with the current associated subgraph ([agents/parent_agent.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/agents/parent_agent.py), [utils/retriever_search_drafts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/retriever_search_drafts.py), [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py)). The agent then receives the selected graph facts and top episodic observations in its plan/action prompt.

**Context efficiency is small retrieved slices over a growing in-run store.** The TextWorld pipeline keeps only `n_prev` recent observations/actions in plain history, retrieves up to six graph facts per seed query with depth limits, and injects `topk_episodic` episodic memories ([pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [utils/retriever_search_drafts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/retriever_search_drafts.py)). There is no explicit token packer, provenance-aware budget, or complexity guard beyond top-k/depth parameters and the graph representation.

**The same graph code is reused for QA ingestion.** `musique_test_big.py` clears the graph for each task, writes paragraph-derived triplets with `update_without_retrieve`, then retrieves a subgraph and episodic texts for the question-answering prompt ([musique_test_big.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/musique_test_big.py)). This confirms the graph is a general RAG substrate in the code, but it remains task-local.

## Artifact analysis

- **Storage substrate:** `in-memory` `files` — The behavior-shaping graph, embeddings, observation episodic store, plans, and recent history live mainly in Python objects during a run; experiment logs, benchmark data, prompts, QA datasets, and source code live as repository files.
- **Representational form:** `prose` `symbolic` `parametric` — Observations, plans, episodic memories, prompts, and answers are prose; graph triplets, hypergraph theses/entities/events, JSON prompts, action JSON, and retrieval parameters are symbolic; Contriever embeddings and LLM model behavior are parametric access and generation surfaces.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompts and pipelines are authored; TextWorld environments and QA datasets are imported; triplets, outdated-entry decisions, navigation edges, episodic observations, QA paragraph memories, and run logs are extracted from observations, paragraphs, actions, and trajectories.
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — Retrieved graph facts and episodes advise the planner/action/QA model as knowledge; system prompts instruct extraction, planning, action, and refinement; graph paths route `go to` navigation; embeddings and overlap scores rank memories; LLM extraction/refinement turns traces into later prompt-affecting memory.

**Triplet graph.** `TripletGraph` keeps canonical triplets as Python lists and implements association lookup, duplicate suppression, deletion, spatial graph construction, and path search ([graphs/parent_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/parent_graph.py)). Its operative split is symbolic facts for world state plus routing authority for navigation.

**Contriever graph.** `ContrieverGraph` adds embeddings for triplets/items, an `obs_episodic` map from observation text to extracted triplets plus embedding, and retrieval routines over both graph facts and episodes ([graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py)). Embeddings rank memory; they are not the source of truth.

**LLM extraction and refinement prompts.** `prompt_extraction_current` defines the triplet extraction contract, and `prompt_refining_items` asks the model to identify old triplets replaced by new observations ([prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py)). This is the main promotion path: raw trace text -> symbolic graph fact -> embedding-indexed prompt memory. The code deletes stale triplets instead of retaining explicit invalidation history.

**Hypergraph variant.** `Hypergraph` stores events, theses, and entities with embeddings, deletes predicted outdated theses, and retrieves semantically related theses through entity expansion ([graphs/hypergraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/hypergraph.py)). It is a useful variant, but the main TextWorld pipeline imports `ContrieverGraph`.

**Baselines and evaluation artifacts.** `pipeline_fullhist.py`, `pipeline_summary.py`, `pipeline_smartrag.py`, run logs, and QA scripts provide comparison surfaces against full-history, summary, and RAG-style memory ([pipeline_fullhist.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_fullhist.py), [pipeline_summary.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_summary.py), [logs](https://github.com/AIRI-Institute/AriGraph/tree/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/logs)). They validate aggregate task performance, but they are not themselves the live memory read-back mechanism.

## Comparison with Our System

AriGraph and Commonplace both treat memory as an artifact that should shape later agent behavior, but they optimize for different lifetimes. AriGraph builds a compact, task-local world model while an agent acts; Commonplace builds durable, reviewable Markdown artifacts that outlive any single session. AriGraph's graph is operationally closer to a run-time cognitive state than to Commonplace's library layer.

The strongest alignment is the explicit separation between source trace and derived artifact. AriGraph reads observations/paragraphs, distills them into graph facts, and then reads those facts back instead of replaying the full trace. Commonplace uses notes, indexes, reviews, and reports for the same broad context-compression goal, but with stronger source links, validation, and replacement semantics.

The strongest divergence is governance. AriGraph delegates fact extraction, contradiction detection, and episodic selection to LLM prompts plus embeddings. It can react online, but provenance is weak: graph facts do not retain stable source citations, confidence, review state, or invalidation history. Commonplace is slower and more manual, but it can preserve lineage and auditability at the artifact level.

AriGraph is also a useful reminder that graph memory can have real routing authority. Its spatial graph is not just context for an LLM; `find_path` can produce hidden navigation actions for a requested destination. Commonplace mostly uses links for navigation and retrieval, not as an executable world model.

### Borrowable Ideas

**In-run world model separate from durable notes.** Commonplace could let agents maintain a task-local graph or scratch model while working, then promote only reviewed conclusions into the KB. Ready as a workshop-layer pattern; not ready as a standing library mutation path without lineage.

**Outdated-fact refinement prompt.** AriGraph's explicit "which old facts are replaced by these new facts?" step is a concrete truth-maintenance move. Commonplace could adapt that as a review helper for candidate note updates, but it should retain superseded evidence rather than silently deleting it. Needs a concrete note-revision use case.

**Graph facts as executable routing state.** For workflows with explicit entities and paths, Commonplace could derive temporary route graphs from notes or logs to plan navigation through tasks. Needs a domain where graph routes have clear correctness tests.

**Small-k episodic recall.** AriGraph shows a cheap pattern: keep full recent context short, then add a few high-similarity episodes. Commonplace could use this for repeated operational workflows, but candidate episodes should enter as reports or observations before becoming instructions.

**Benchmark against full-history and summary baselines.** The repository keeps comparable pipelines for full history, summary, RAG, and graph memory. Commonplace review tooling could similarly compare context assembly methods before adopting a more complex retrieval surface. Ready where a repeatable task benchmark exists.

## Write side

**Write agency:** `automatic` `manual` — The main pipelines automatically extract graph facts and episodic entries from observations/paragraphs during a run; operators manually choose environment, model, API key, top-k values, attempts, and which pipeline/baseline to execute.

**Curation operations:** `evolve` — New observations can cause the system to remove conflicting old triplets or theses and add newer graph facts. This is weak online evolution of the store, not full invalidation, because the implementation deletes old entries instead of retaining supersession history.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `trajectories` — TextWorld observations, inventories, actions, locations, rewards, and histories feed graph updates; QA paragraphs feed `update_without_retrieve`; run logs preserve observed behavior after execution.

**Extraction.** The main extraction oracle is an LLM prompt that emits triplets or theses from the current trace text. A second LLM prompt identifies existing graph statements to replace. Navigation edges are rule-derived from action direction and location change, and episodic memory stores observation text with extracted graph facts and embeddings.

**Learning scope:** `per-task` — In the inspected TextWorld and QA pipelines, the graph is constructed inside one game attempt or one QA task and reset between attempts/tasks.

**Learning timing:** `online` — TextWorld memory updates happen during the acting loop before each planning/action decision; QA memory is built before answering each question.

**Distilled form:** `prose` `symbolic` `parametric` — Raw observations remain as episodic prose; extracted triplets/theses are symbolic; Contriever embeddings are parametric retrieval state over both graph facts and episodes.

**Survey placement.** AriGraph is a strong example of trace-derived in-run learning: raw traces become symbolic and parametric memory that affects later actions in the same episode. It weakens any survey claim that trace-learning must be durable across sessions, but it strengthens the distinction between trace-derived knowledge artifacts and stronger reviewed system-definition artifacts.

## Read-back

**Read-back:** `both` — `ContrieverGraph.retrieve` and graph association methods are pull-capable APIs, while the TextWorld and QA pipelines automatically insert selected graph facts and episodic memories into the receiving planner/action/answer prompts.

**Read-back signal:** `identifier` `inferred / embedding` — Current observations/questions are reduced to entity-like seed items, then Contriever embedding search and graph expansion select relevant triplets; episodic recall uses plan/question embeddings plus overlap with currently associated graph facts.

**Faithfulness tested:** `no` — The repository reports benchmark results and contains ablation-style logs, but the inspected code does not audit whether a particular fired memory changed the next model action, nor does it run a per-decision with/without-memory faithfulness check.

**Direction edge case.** Retrieval is pull from the orchestrating Python code, but push for the LLM planner, action agent, or QA model that receives `subgraph` and `top_episodic` in the prompt without making an explicit memory call.

**Selection, scope, and complexity.** Selection is bounded by seed-item count, graph retrieval `topk=6`, max depth, similarity threshold, and `topk_episodic` ([utils/retriever_search_drafts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/retriever_search_drafts.py), [pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py)). Complexity is lower than full history, but the injected facts can still be stale or over-compressed because source spans and confidence are not carried into the prompt.

**Injection point.** Read-back happens before the model call that updates the plan, chooses an action, or answers the question. Later observation processing and graph updates are write-side maintenance for the next decision.

**Authority at consumption.** Graph facts and episodic memories are advisory context for LLM planning/action/QA. Spatial graph pathfinding has stronger routing authority when `go to` actions are expanded into concrete environment moves, but ordinary retrieved facts are not validators or hard gates.

## Curiosity Pass

**The graph is more transient than the README framing can suggest.** The public framing calls AriGraph an external memory architecture, but the inspected pipelines construct memory inside a run or QA task. That is still real read-back, just not persistent agent memory across sessions.

**Deletion is not truth maintenance.** The refinement prompt removes outdated facts, but because deleted entries are not retained with invalidation metadata, the system cannot later audit why a belief changed.

**Embedding retrieval and LLM extraction share a provenance gap.** The code can retrieve relevant-looking graph facts efficiently, but the prompt-injected fact does not carry the original observation, step id, or extraction confidence.

**The QA path clarifies the architecture.** By clearing the graph, loading paragraphs, and then answering a question from retrieved facts, `musique_test_big.py` shows AriGraph as a general graph-RAG construction, not only a TextWorld navigation memory.

**The hypergraph path may be a richer successor, but it is not the main pipeline.** `Hypergraph` has event/thesis/entity structure and episodic sorting, yet the primary AriGraph TextWorld pipeline uses `ContrieverGraph`.

## What to Watch

- Whether future code persists graph memory across attempts or sessions; that would change the storage and lineage story from in-run state to durable learned memory.
- Whether graph facts gain source spans, confidence, or invalidation history; that would make AriGraph much closer to a reviewable KB substrate.
- Whether the hypergraph implementation replaces the triplet graph in the main pipeline; that would shift the representational form from edge facts toward event/thesis memory.
- Whether evaluation includes per-decision memory ablations or fired-memory audits; that would strengthen the read-back faithfulness claim.
- Whether the TextWorld route graph becomes a reusable action planner outside game navigation; that would make graph memory a stronger routing mechanism worth comparing with Commonplace workflow routing.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: AriGraph's graph matters because the pipeline reads it back into prompts, not merely because it stores facts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating in-memory graph state, prose observations, embeddings, prompts, and evaluation logs.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames AriGraph's observation-to-graph loop as trace-learning.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies retrieved graph facts and episodic observations as advisory evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes authored prompts and pathfinding/routing code from ordinary graph facts.
- [Lineage](../../notes/definitions/lineage.md) - highlights the review risk around extracted facts that lack source-span provenance or invalidation history.
