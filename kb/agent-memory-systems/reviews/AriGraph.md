---
description: "Text-game memory agent that builds an in-run knowledge graph and episodic store, then relevance-pushes selected facts into planner and action prompts"
type: ../types/agent-memory-system-review.md
tags: [push-activation]
status: current
last-checked: "2026-06-01"
---

# AriGraph

AriGraph, from AIRI Institute, is an external memory architecture for LLM agents in TextWorld games and QA benchmarks. The inspected code implements the Ariadne game loop around a mutable in-memory graph: observations are converted into graph facts, conflicting facts are pruned, entity queries retrieve associated subgraphs, episodic observations are ranked against the current plan, and the selected memory is inserted into the planner and action-selector prompts. The repository also contains baseline pipelines for full history, summary memory, and SmartRAG, plus QA evaluation scripts that reuse the same graph retrieval machinery.

**Repository:** https://github.com/AIRI-Institute/AriGraph

**Reviewed commit:** [e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2](https://github.com/AIRI-Institute/AriGraph/commit/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2)

## Core Ideas

**The main game pipeline is planner, action selector, exploration gate, and graph memory.** `pipeline_arigraph.py` constructs separate GPT agents for item extraction, planning, action choice, and exploration gating, then creates a fresh `ContrieverGraph` for each attempt ([pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py)). Each step processes the TextWorld observation, extracts crucial items from the current observation and plan, updates graph memory, retrieves associated facts and episodic observations, and renders those selected memories into both planning and action prompts.

**Graph memory is extracted from observations, not hand-authored world state.** `ContrieverGraph.update(...)` asks an LLM to extract structured triplets from the current observation, excludes already-known triplets, asks another prompt to identify outdated conflicting facts, and then mutates the graph ([graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py)). Navigation edges are added from movement actions when the current location changes, so the graph mixes LLM-extracted semantic facts with symbolic route facts.

**Retrieval uses a two-stage relevance path: LLM-selected query entities, then embedding graph expansion.** `GPTagent.item_processing_scores(...)` extracts entity queries and relevance depths from the observation and current plan ([agents/parent_agent.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/agents/parent_agent.py)). For each query, `graph_retr_search(...)` embeds graph triplet strings with multilingual Contriever, selects top matches above a threshold, and breadth-expands through matched nodes up to the requested depth ([utils/retriever_search_drafts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/retriever_search_drafts.py), [utils/contriever.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/contriever.py)).

**Episodic memory is observation text ranked by current-plan similarity and graph overlap.** After each update, the graph stores the current observation with its embedding and extracted triplet strings in `obs_episodic`. On later steps, `find_top_episodic_emb(...)` scores past observations by embedding similarity to the current plan and by overlap with the currently retrieved subgraph; the top observations are passed to the planner and action selector ([graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py)).

**The latest checkout includes a thesis/event hypergraph variant, but the primary pipeline still wires `ContrieverGraph`.** `graphs/hypergraph.py` adds entities, thesis hyperedges, and events, extracting sentence-like theses rather than short triplets and ranking episodic events against the current plan ([graphs/hypergraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/hypergraph.py)). Search found no main pipeline importing `Hypergraph`; the reviewed game and QA scripts instantiate `ContrieverGraph` or `LLaMAContrieverGraph` ([pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [musique_test_big.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/musique_test_big.py)).

**The graph doubles as an action affordance.** `process_action_get_reward(...)` intercepts actions of the form `go to <location>`, asks the graph for a shortest path through known navigation edges, and executes the hidden directional steps in the environment ([pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [graphs/parent_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/parent_graph.py)). That gives graph memory more than advisory prompt authority: for navigation actions, it can directly route environment interaction.

**The QA path treats documents as observations.** `musique_test_big.py` clears a graph for each QA task, loads every paragraph through `update_without_retrieve(...)`, extracts question entities, retrieves graph facts and episodic texts, and asks a QA agent to answer from those selected memories ([musique_test_big.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/musique_test_big.py)). This shows the memory mechanism is a graph-RAG substrate, not only a TextWorld-specific route map.

## Artifact analysis

**In-run triplet graph.** The storage substrate is Python process memory: lists and dictionaries on `TripletGraph` / `ContrieverGraph`, with no implemented save/load path for graph state in the main pipeline. The representational form is mixed: symbolic triplets and navigation edges, prose triplet strings, and distributed-parametric embeddings for triplets and entities. Lineage is observation-derived and action-derived inside one attempt: LLM extraction turns observations into triplets; movement actions add navigation edges; a refinement prompt removes predicted outdated facts. Behavioral authority is both knowledge-artifact and system-definition-artifact authority: retrieved facts advise planner/action prompts, and navigation edges are used as routing state for `go to` actions.

**Episodic observation store.** The storage substrate is also in-process memory: `obs_episodic`, `obs_episodic_list`, and `top_episodic_dict_list` on `ContrieverGraph`. The representational form is mixed prose plus embeddings: each stored observation is the textual game observation paired with extracted triplet strings and an embedding. Lineage is raw-ish observation text plus derived graph facts from the same step; it is retained only for later steps in the same run. Behavioral authority is knowledge-artifact authority when inserted as "most relevant episodic memories" into the planner/action prompts.

**Retrieval and scoring machinery.** The storage substrate is code and model state: Python retrieval functions plus the downloaded `facebook/mcontriever` model loaded by Hugging Face. The representational form is symbolic retrieval policy plus distributed-parametric embeddings. Lineage is authored code over derived graph/episode state. Behavioral authority is ranking/routing authority because it decides which graph facts and observations reach the next planning and action calls.

**Prompt templates and role prompts.** The storage substrate is repository files under `prompts/` and string literals in pipeline scripts. The representational form is prose instruction with JSON output contracts. Lineage is authored. Behavioral authority is system-definition-artifact authority: the prompts define extraction, refinement, planning, action selection, exploration gating, summarization, and QA output behavior.

**Run logs.** The `logs/` directory and `Logger` class provide durable text records of reported runs ([utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py), [logs](https://github.com/AIRI-Institute/AriGraph/tree/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/logs)). Their representational form is prose/text trace output. Their lineage is benchmark execution. In the inspected code they are knowledge artifacts for humans and evaluators, not read-back memory for later agent behavior.

The promotion path is therefore narrow. Observations can become graph facts with stronger routing and prompt authority inside a run, but the code does not promote them into durable reviewed rules, skills, validators, or reusable memory files. The durable repository artifacts are implementation, prompts, datasets, and logs; the active learned world model is live run state.

### Borrowable Ideas

**Use graph memory as both evidence and affordance.** Ready as a design pattern. AriGraph's navigation path shows that a retained graph can do more than supply prose context; selected symbolic structure can route actions. A Commonplace analogue would be generated link/path plans or command routing, not only notes shown to an agent.

**Separate extraction, refinement, retrieval, and consumption.** Ready now as vocabulary. AriGraph has distinct prompts and functions for graph extraction, outdated-fact pruning, entity query selection, retrieval expansion, and prompt consumption. Commonplace reviews should keep these operative parts separate instead of calling the whole flow "memory."

**Rank by task/plan, not only by lexical query.** Useful but needs a concrete Commonplace workflow. AriGraph retrieves against entities extracted from the current plan and observation, then ranks episodes against the current plan embedding. A Commonplace equivalent might rank notes by the active task brief plus local artifact type, not only by a string query.

**Treat run-local memory differently from durable KB memory.** Ready now. AriGraph is a good reminder that behavior-shaping retained state can matter within a single run without becoming a durable library artifact. Commonplace should name that scope explicitly when comparing systems.

**Do not borrow prompt-only fact pruning as governance.** Needs stronger gates first. AriGraph's refinement prompt is pragmatic for TextWorld state changes, but Commonplace would need provenance, review status, and deterministic checks before deleting or replacing durable claims.

## Comparison with Our System

| Dimension | AriGraph | Commonplace |
|---|---|---|
| Primary retained state | In-process graph triplets, embeddings, episodic observations, prompts, logs | Git-tracked notes, sources, reviews, instructions, schemas, generated indexes |
| Storage substrate | Python objects during a run; text logs after a run | Filesystem and git as primary substrate |
| Representational form | Symbolic graph facts, prose observations/prompts, Contriever embeddings | Mostly prose with frontmatter, links, schemas, scripts, validation reports |
| Lineage | Observation/action to LLM-extracted facts to retrieved prompt context; weak durable provenance | Source snapshots, commit-pinned reviews, authored links, status, review dates |
| Activation | Orchestrator pushes selected facts/episodes into planner and action prompts | Agent or maintainer pulls by `rg`, indexes, links, and instructions; some instructions are always-loaded |
| Governance | LLM refinement prompt prunes conflicting facts; no durable review gate | Collection contracts, validation, semantic review, archive/replacement lifecycle |

AriGraph is stronger than Commonplace as a low-latency task memory inside an embodied loop. It extracts a world model continuously, uses relevance scoring before every planning/action step, and can turn graph edges into navigation routes. Commonplace is stronger as durable organizational memory: its artifacts are inspectable, versioned, typed, validated, and meant to survive across sessions.

The most important distinction is durability. AriGraph learns from observations, but the learned graph and episodic store are instantiated fresh per attempt in `pipeline_arigraph.py`. That makes the active memory a run-local context-engineering mechanism, not a durable knowledge base. The durable logs preserve traces, but the code does not consume those logs to seed future behavior.

Read-back: push. From the planner/action agent's perspective, the orchestration layer relevance-selects graph facts and episodic memories and inserts them into prompts before each decision; the selected memory is not requested by the planner/action agent through a tool call.

## Read-back placement

**Direction.** AriGraph has engineered push activation from the planner/action agent's perspective. The pipeline, not the planner/action LLM, calls the memory system every step and supplies the selected "Information from the memory module" and "most relevant episodic memories" in the prompt.

**Trigger and relevance signal.** The trigger is the step loop in `pipeline_arigraph.py`: every nonterminal game step processes the current observation, inventory, plan, location set, and previous action. Relevance is engineered through an LLM entity/depth extractor, embedding retrieval over graph strings, graph expansion, a similarity threshold, and top-k episodic ranking.

**Timing relative to action.** Read-back happens before planning and action selection, so memory can change the immediate next plan and command. The graph can also affect environment interaction after action selection when a `go to` action is translated into a route through known navigation edges.

**Selection, scope, and complexity.** The selected subgraph is bounded by query depths, `topk=6`, `post_retrieve_threshold=0.75`, and graph expansion; episodic memory is bounded by `topk_episodic`. The implementation controls volume, but complexity can still grow because graph facts, episodic text, history, inventory, plan, exploration hints, and valid actions are all rendered into one prompt.

**Authority at consumption.** Associated subgraph facts and episodic observations are advisory context for the planner and action selector. Navigation edges have stronger routing authority when `find_path(...)` converts a high-level destination action into hidden directional actions.

**Faithfulness.** The code evaluates benchmark reward and logs retrieved memory, but it does not implement a WITH/WITHOUT ablation or post-action audit that verifies a fired memory changed the model's decision. Effective precision and behavioral uptake are therefore not verified from code.

**Other consumers.** Humans consume the run logs and benchmark outputs; QA scripts consume graph retrieval as evidence for an answer; the TextWorld wrapper consumes graph-derived navigation routes when `go to` is selected.

## Curiosity Pass

**AriGraph is more run-local than its "learning world model" label can sound.** It learns a world model during an attempt, but the inspected pipeline creates a new graph inside each attempt and does not reload prior graph state.

**The repository's newest graph idea is not the default path.** The thesis/event `Hypergraph` class is architecturally interesting because events become parents of thesis hyperedges, but the main reviewed pipeline still imports and instantiates `ContrieverGraph`.

**The same graph class carries several authorities.** It is evidence for prompts, a retrieval index, an episodic store, and a navigation router. That bundling is convenient for research code but makes lifecycle and provenance harder to inspect.

**Prompt-based contradiction handling is a useful local heuristic, not a durable truth-maintenance system.** The refinement prompts tell the model to preserve distinct facts and remove only redundant or conflicting ones, but the artifacts do not record why a fact was deleted or which observation superseded it.

**SmartRAG is a revealing baseline.** `pipeline_smartrag.py` ranks past observations by recency, LLM-rated importance, and embedding similarity, while AriGraph extracts a structured graph first. The comparison isolates the design bet: structure and entity expansion should reduce context cost compared with replaying raw observations.

## What to Watch

- Whether `Hypergraph` becomes wired into the main game or QA pipelines; that would change the central retained artifact from triplet graph to event/thesis hypergraph.
- Whether graph state gains save/load support across attempts or benchmark runs; that would make AriGraph qualify as durable trace-derived learning rather than run-local memory.
- Whether logs become a training, replay, or seeding input for future agents; that would change their authority from human evidence to behavior-shaping lineage.
- Whether contradiction pruning gains explicit provenance for deleted facts, source observations, and replacement decisions.
- Whether the paper-facing performance claims continue to map to the code path in `pipeline_arigraph.py` as experimental graph variants are added.

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: AriGraph's graph matters because selected facts and episodes are actively pushed into planner/action prompts.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: AriGraph structures observations into graph facts to keep prompt context smaller than full-history replay.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: AriGraph requires separating graph facts, episodic observations, embeddings, prompts, and logs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved facts, episodic observations, and logs advise or evidence future decisions when consumed.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt templates, retrieval code, ranking thresholds, and navigation routing rules configure or constrain behavior.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - contrasts: AriGraph derives behavior-shaping memory from traces inside a run, but the inspected code does not make that derived state durable across runs.
