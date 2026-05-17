---
description: "AriGraph review: TextWorld agent memory that extracts observation traces into an in-run triplet graph plus episodic observations for planning, navigation, exploration, and QA retrieval"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-04-27"
---

# AriGraph

> Replaced 2026-05-16. See [AriGraph](./AriGraph.md) for the current review.

AriGraph is AIRI Institute's graph-memory architecture for text-game agents. The inspected repository implements an Ariadne-style TextWorld pipeline where each step's observation is distilled into graph facts, stale facts are removed, episodic observations are embedded, and the planner/action selector receives graph and episodic context. The system is closer to an online world-model memory for an embodied text environment than to a general project knowledge base.

**Repository:** https://github.com/AIRI-Institute/AriGraph

**Reviewed commit:** e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2

**Commit URL:** https://github.com/AIRI-Institute/AriGraph/commit/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2

## Core Ideas

**Memory is an in-run semantic graph plus episodic observation store.** `ContrieverGraph` inherits a simple `TripletGraph` whose core state is a list of triplets, then adds Contriever embeddings for triplet strings and item names. During `update(...)`, each observation is passed through an LLM extraction prompt, converted into `(subject, object, label)` records, embedded, and added to the current graph. The same update stores `obs_episodic[observation] = [new_triplets_str, obs_embedding]`, making raw observations retrievable as episodic memory. See [graphs/parent_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/parent_graph.py), [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), and [prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py).

**The graph update path includes conflict repair, not just appending.** After extracting new triplets, `ContrieverGraph.update(...)` finds already-associated facts for the newly mentioned entities, asks an LLM which existing triplets should be replaced, deletes the predicted outdated triplets except spatial links between known locations, and then adds the new facts. That gives AriGraph a lightweight world-state correction mechanism for moving objects and changing states. The authority model is still prompt-mediated: there is no durable review record or confidence state for a deletion. See [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py) and [prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py).

**Retrieval starts from LLM-selected entities and expands through embedding search.** The agent first asks `GPTagent.item_processing_scores(...)` to extract important entities from the current observation and plan. For each entity, graph retrieval embeds candidate triplet strings, searches by similarity, expands through the endpoints of accepted triplets up to the requested depth, and returns associated triplets above a threshold. Episodic retrieval combines similarity between the current plan and stored observation embeddings with overlap between retrieved subgraph facts and the facts extracted from prior observations. See [agents/parent_agent.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/agents/parent_agent.py), [utils/retriever_search_drafts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/retriever_search_drafts.py), [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py), and [utils/contriever.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/contriever.py).

**The memory changes the action surface.** `pipeline_arigraph.py` injects the associated graph facts and top episodic memories into both planning and action-selection prompts. It also uses graph state operationally: known locations become synthetic `go to {loc}` actions, `find_path(...)` turns a destination into low-level movement steps through the spatial graph, and exploration prompts can ask for unexplored exits inferred from location facts. This is stronger than QA retrieval because memory can alter navigation affordances, not only answer questions. See [pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [graphs/parent_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/parent_graph.py), [prompts/system_prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/system_prompts.py), and [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py).

**A parallel hypergraph prototype stores events, theses, and entities.** `Hypergraph` replaces subject-relation-object triplets with thesis hyperedges linked to entity nodes and event nodes. It extracts sentence-like theses from observations, removes outdated theses, stores events as observation texts, and ranks episodic events by embedding similarity plus thesis overlap. This looks like an experimental variant rather than the primary runnable pipeline, but it exposes the same design pressure: environment traces become a semantic structure plus an episodic event layer. See [graphs/hypergraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/hypergraph.py) and [prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py).

**The QA path reuses the graph as a corpus memory.** `musique_test_big.py` clears the graph for each QA task, ingests each paragraph with `update_without_retrieve(...)`, extracts question entities, retrieves associated subgraph facts and episodic paragraph texts, and asks a QA model to answer from those memory surfaces. That is not the system's strongest fit, but it shows that the implementation treats AriGraph as a general extraction-and-retrieval substrate over text, not only a TextWorld navigation hack. See [musique_test_big.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/musique_test_big.py) and [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py).

**Baselines make the memory comparison explicit.** The repository includes full-history, summary, and smart-RAG pipelines beside AriGraph. Full history keeps all prior observations in prompt context; summary maintains a rolling LLM summary; smart RAG ranks prior observations by recency, poignancy, and embedding similarity. AriGraph's distinct move is to maintain an entity-linked semantic graph and episodic memories at the same time. See [pipeline_fullhist.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_fullhist.py), [pipeline_summary.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_summary.py), and [pipeline_smartrag.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_smartrag.py).

## Comparison with Our System

| Dimension | AriGraph | Commonplace |
|---|---|---|
| Primary substrate | In-memory Python triplet graph, embeddings, episodic observation dict, logs | Markdown files in git |
| Source signal | TextWorld observations, actions, inventory, locations, environment facts, QA paragraphs | Authored notes, source snapshots, reviews, instructions, ADRs, validation outputs |
| Memory atom | Triplet, thesis, entity, observation episode, associated subgraph | Typed note, source, instruction, ADR, review, index |
| Retrieval | LLM entity extraction, Contriever similarity, graph expansion, episodic scoring | `rg`, indexes, descriptions, links, review reports, explicit reading decisions |
| Activation | Prompt injection plus graph-derived navigation actions | Agent reads selected artifacts and applies procedures or claims |
| Lifecycle | Append, prompt-mediated replacement, per-run clearing, logs | Status, replacement, validation, review gates, generated indexes, git history |
| Governance | Prompt instructions and benchmark logs | Type specs, link contracts, semantic review, source citations, validation |

AriGraph is stronger where memory is an operational world model. The graph does not merely retrieve passages; it supports pathfinding, unexplored-exit detection, entity-centered context, and episodic reminders inside a live control loop. Commonplace currently has no equivalent automatic spatial/semantic model that can synthesize actions from accumulated observations.

Commonplace is stronger where memory must be inspectable, durable, and governed across projects. AriGraph's central memory state is not a maintained source artifact: it is rebuilt during a run, updated by prompts, and logged as execution output. There is no type system for memory roles, no explicit provenance per fact beyond the observation episode stored nearby, no review status, and no promotion path from repeated traces into a stronger instruction, test, script, or index.

The key design difference is scope. AriGraph optimizes for online task performance in a bounded environment where facts change and the agent must act immediately. Commonplace optimizes for long-lived methodology knowledge where the expensive part is trust, maintenance, and future activation under bounded context. AriGraph is a useful retrieval and activation reference, but not a governance model.

## Borrowable Ideas

**Use trace-derived graph state for local task worlds.** Ready to borrow only for workshops with an explicit temporary world model. A commonplace analogue would build a disposable graph over a work session's files, claims, entities, and decisions, then discard or promote selected findings when the workshop ends.

**Separate semantic facts from episodic observations.** Ready as a conceptual pattern. AriGraph keeps extracted graph facts and raw observation memories side by side, then retrieves both. Commonplace already separates notes and sources; session/workshop tooling could make the same separation sharper for active work traces.

**Let memory produce affordances, not only context.** AriGraph's `go to {loc}` actions are a concrete example of memory changing the available action set. In commonplace, a comparable mechanism would let validated KB state expose commands, checklists, or task-specific scripts when a note or instruction makes them relevant. This needs a narrow use case first.

**Use replacement prompts as a weak contradiction-management layer.** AriGraph's stale-triplet deletion prompt is worth studying for mutable domains. Commonplace should not copy the prompt-mediated authority model directly, but generated reports could suggest superseded claims or conflicting instructions for human/agent review.

**Keep baselines close to the target system.** The full-history, summary, and smart-RAG pipelines make AriGraph easier to interpret because the alternatives are runnable in the same task shape. Commonplace evaluations would benefit from similarly adjacent baselines before adding retrieval machinery.

## Trace-derived learning placement

**Trace source.** AriGraph qualifies as trace-derived learning. The raw signal is an online task trace: TextWorld observations, inventory strings, current location, admissible actions, chosen actions, environment facts, and in the QA path paragraph texts treated as observations.

**Extraction.** Extraction is LLM-mediated. Observation text is converted into triplets or theses; another prompt decides which prior facts are outdated; entity-selection prompts decide what to retrieve for the current plan; episodic retrieval is scored by embedding similarity and overlap with retrieved facts.

**Representational form.** The primary distilled substrate is symbolic plus vector-indexed state: natural-language triplets/theses, graph edges, entity names, observation episodes, and Contriever embeddings. It is not an opaque weight update and not a prose rulebook.

**Behavioral authority.** Most retained state has knowledge-artifact use, with some action-affordance effects. Retrieved facts and episodes inform planning and action prompts, while spatial graph facts enable pathfinding and synthetic navigation commands. The memory does not rewrite the agent's policies or prompts as reusable system-definition artifacts.

**Scope.** Scope is per-task and per-run for games, and per-question for the QA script. The repository ships logs and environments, but the implemented graph state is not exported as a reusable cross-run memory library.

**Timing.** Learning is online during deployment: each observation updates the graph before the next planning/action step. QA ingestion is staged within each question: paragraphs are loaded into a fresh graph before answering.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), AriGraph belongs in the trace-to-symbolic-world-model branch. It strengthens the claim that trace-derived artifacts can change behavior without becoming policies or code: a per-run graph can alter retrieval, exploration, and navigation even when it remains temporary.

## Curiosity Pass

The most interesting part of AriGraph is not graph RAG by itself; it is the combination of semantic graph retrieval, episodic observation retrieval, and action-space modification inside one control loop. That makes the memory meaningfully behavior-changing even though it is not durable.

The implementation is less persistent than the paper-level framing can imply. `ContrieverGraph.clear()` resets the graph, QA tasks explicitly clear it per example, and the main game pipeline constructs a new graph inside each attempt. The logs preserve traces, but the reviewed code does not promote those logs into future memory.

The deletion path is useful but fragile. It protects spatial location links from deletion, but otherwise relies on an LLM parsing a replacement format. A bad deletion can silently remove a fact that later retrieval or navigation needed.

The hypergraph variant points at a richer representation than the primary triplet pipeline, but it is not clearly integrated as the main evaluated agent. Treat it as evidence of design exploration, not as the default AriGraph mechanism.

The repository is research-code shaped. There is no package manifest beyond a UTF-16 `requirements.txt`, API keys are edited into scripts, and pipeline configuration lives in top-level "changeable part" blocks. That is fine for reproducing experiments, but weak for adopting AriGraph as reusable memory infrastructure.

## What to Watch

- Whether AriGraph gains persistence for graph state across episodes, tasks, or environments.
- Whether observation-to-fact provenance becomes first-class enough to audit why a fact exists or why it was deleted.
- Whether the hypergraph representation replaces the triplet graph in the main pipeline.
- Whether graph updates get deterministic checks, confidence scores, or human-readable diff reports.
- Whether logs become training or promotion material for future instructions, skills, or world models instead of remaining run records.
- Whether the QA path evolves into a maintained retrieval library or remains an experiment script.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: AriGraph is an online trace-to-world-model case with per-run graph and episodic memory.
- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: AriGraph's memory matters because it is activated in planning, action selection, and navigation.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: extracted graph and episodic memories compress prior observations before they enter the prompt.
- [distillation](../../notes/definitions/distillation.md) - exemplifies: observations are compressed into graph facts and episodic retrieval handles.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: AriGraph separates raw observations/logs, graph facts, embeddings, and prompt-injected retrieval surfaces.
