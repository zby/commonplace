---
description: "TextWorld graph-memory agent that converts observations into an in-run triplet graph plus episodic store for planning, retrieval, exploration, and navigation"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# AriGraph

> Replaced 2026-06-01. See [AriGraph](./AriGraph.md) for the current review.

AriGraph is AIRI Institute's research codebase for Ariadne, a TextWorld agent whose memory is an LLM-extracted knowledge graph plus episodic observation retrieval. The implementation builds graph state from live game observations, queries that graph with entities extracted from the current observation and plan, retrieves relevant prior observations, and injects those memories into separate planning and action-selection prompts. The repository also includes QA experiments that reuse the same graph/episodic machinery over MuSiQue and HotpotQA paragraphs.

**Repository:** https://github.com/AIRI-Institute/AriGraph

**Reviewed commit:** [e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2](https://github.com/AIRI-Institute/AriGraph/commit/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2)

## Core Ideas

**Memory is rebuilt inside each run, not maintained as a cross-run store.** The main TextWorld pipeline instantiates a fresh `ContrieverGraph` for each attempt, then accumulates observations, graph triplets, embeddings, locations, and recent history while the game runs. The only durable repo-level artifacts are scripts, datasets, environment files, and run logs; the active memory substrate is Python object state plus optional log output, not a database, file-backed memory bank, or reusable service. See [pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), and [README.md](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/README.md).

**Observations become symbolic graph facts through an LLM extraction prompt.** `ContrieverGraph.update()` sends the current observation plus examples from the previous retrieved subgraph to `prompt_extraction_current`, parses semicolon-delimited subject/relation/object triples, normalizes them, drops duplicates, asks a second prompt which old facts should be replaced, and then mutates the triplet list. This is real trace-to-symbolic distillation, but the oracle is the same LLM prompt path; there is no independent verifier for extraction or replacement quality. See [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [prompts/prompts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py), and [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py).

**Retrieval mixes graph expansion and dense similarity.** The planner-facing subgraph is found by first asking a `GPTagent` to extract scored entities from the current observation and plan, then running `graph_retr_search()` from each entity over stringified triples. That retrieval embeds triplet strings and query entities with `facebook/mcontriever`, keeps high-scoring matches, and follows discovered endpoint entities for a bounded number of hops. AriGraph is therefore not just vector search and not just graph BFS; it is dense retrieval over graph-edge strings with graph-neighborhood expansion. See [agents/parent_agent.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/agents/parent_agent.py), [utils/retriever_search_drafts.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/retriever_search_drafts.py), and [utils/contriever.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/contriever.py).

**Episodic memory is previous observations plus derived fact lists.** Each update stores the full observation as the key and `[new_triplets_str, obs_embedding]` as the value in `obs_episodic`. Later retrieval scores prior observations by a combination of embedding similarity to the current plan and overlap between current associated subgraph items and the facts attached to the prior observation. The retrieved episodes are injected as text into planning and action prompts. This is a knowledge-artifact surface when stored as evidence and a system-definition-artifact surface when the prompt tells the planner/action agent to use it. See [graphs/contriever_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py), and [pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py).

**The graph has operational affordances beyond recall.** Spatial triplets are used to compute a graph of known locations, infer shortest paths for synthetic `go to {location}` actions, and list unexplored exits when the plan requires exploration. That makes the memory behavior-changing in a concrete way: graph state changes the action set and can collapse multi-step navigation into hidden environment actions. See [graphs/parent_graph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/parent_graph.py), [pipeline_arigraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), and [utils/utils.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py).

**Alternative memory baselines are present but thinner.** The repo includes full-history, summary, and SmartRAG pipelines, plus a `Hypergraph` class that stores thesis/entity/event objects instead of plain triplets. The reported AriGraph path uses `ContrieverGraph`; the hypergraph path is not imported by the main pipelines. That makes the implemented comparison useful: AriGraph's distinctive claim is the triplet graph plus episodic retrieval inside a planner/action loop, not a general memory platform. See [pipeline_fullhist.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_fullhist.py), [pipeline_summary.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_summary.py), [pipeline_smartrag.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_smartrag.py), and [graphs/hypergraph.py](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/hypergraph.py).

## Comparison with Our System

| Dimension | AriGraph | Commonplace |
|---|---|---|
| Primary substrate | In-process Python lists/dicts for triplets, embeddings, episodes, and locations; text logs for runs | Git-tracked markdown artifacts plus generated indexes/reports |
| Representational form | Mixed symbolic/prose/distributed-parametric: triples, observations, prompt text, and transient Contriever embeddings | Mostly prose and symbolic frontmatter/link/type contracts |
| Lineage | Observation -> extracted triples -> replacement decision -> graph/episode state, with weak IDs and no regeneration contract | Source citations, frontmatter status, review artifacts, git history, validation reports |
| Activation | Retrieved subgraph, episodic memories, unexplored exits, and `go to` affordances are injected before planning/action | Search, indexes, links, skills, instructions, and validation routes determine what agents load or obey |
| Lifecycle | Per-run mutation, duplicate suppression, LLM-predicted replacement, attempt reset | Curation, promotion, review, supersession, archive status, and explicit maintenance |
| Behavioral authority | Memory advises and instructs planner/action agents inside prompts; navigation graph also changes available action semantics | Artifacts can advise, instruct, validate, route, enforce, or document depending on type and consumer |

AriGraph is stronger than commonplace as a live world-model loop. It extracts structured state continuously from observations, uses that state for both retrieval and navigation, and directly tests whether memory changes task score in TextWorld. Commonplace has no comparable runtime that turns every observation into graph state and immediately uses it to change an action policy.

Commonplace is stronger as a durable knowledge system. AriGraph's graph entries and episodes do not carry stable provenance pointers, confidence, review status, source spans, contradiction records, or retirement rules. They are effective working memory for one environment run, but they are not library artifacts a later agent can audit, edit, regenerate, or promote.

The deepest divergence is authority. AriGraph's retained artifacts become high-authority prompt material because the planner and action selector are told to pay attention to memory, yet the write path is automatic and weakly governed. Commonplace spends more design effort distinguishing knowledge artifacts from system-definition artifacts, so an artifact's storage substrate, representational form, lineage, and behavioral authority can be reviewed before it changes future behavior.

**Read-back:** push — current observation and plan cues retrieve graph and episodic memory that is injected before planning and action.

## Borrowable Ideas

**Action affordances derived from memory.** Ready as a design reference. AriGraph does not only retrieve text; it turns spatial graph state into `go to` actions. A commonplace analogue would be generated maintenance commands or navigation shortcuts whose availability is computed from validated KB state, not simply suggested by prose.

**Replacement prompts for mutable world facts.** Worth borrowing only in workshop contexts. AriGraph's old-fact replacement prompt is a compact pattern for handling changing state, but it lacks a verification layer. In commonplace, this belongs in transient work surfaces or generated reports before promotion into library notes.

**Pair semantic graph retrieval with episodic recall.** Ready as an evaluation idea. AriGraph retrieves current facts and past observations separately, then injects both. Commonplace could test a similar split between claim-level retrieval and prior-work episode retrieval, especially for review or repair workflows.

**Unexplored-neighborhood cues.** Needs a concrete use case. AriGraph computes unexplored exits from graph state when exploration is required. A KB analogue might surface unreviewed backlinks, missing outbound links, or unvalidated generated indexes only when the current task needs exploration rather than execution.

**Keep benchmark baselines adjacent to the memory mechanism.** Ready as a review standard. The repo keeps full-history, summary, RAG-like, and AriGraph pipelines side by side, which makes mechanism comparison easier even when the code is research-script shaped.

## Trace-derived learning placement

**Trace source.** AriGraph consumes live TextWorld observations, inventory state, selected actions, current location changes, valid actions, current plan text, and recent history within one game attempt. The QA pipeline uses source paragraphs as the trace-like input, but the clearest agent trace is the TextWorld observation/action loop in `pipeline_arigraph.py`.

**Extraction.** The main extraction step asks an LLM to produce concrete subject/relation/object triplets from each observation. A second LLM prompt compares new triplets against associated existing triplets and predicts which old facts should be removed. Entity extraction for retrieval is another LLM prompt over observation plus plan. There is no hard oracle for the extracted knowledge; TextWorld reward evaluates downstream behavior, not each memory write.

**Storage substrate.** Raw traces are logged to text files through `Logger` and example run logs are checked into `logs/`, but active memory lives in process: `triplets`, `triplets_emb`, `items_emb`, `obs_episodic`, `obs_episodic_list`, and `top_episodic_dict_list`. There is no persistent graph database, vector store, or cross-run memory file for the AriGraph path.

**Representational form.** Raw observations are prose traces. Distilled graph memory is symbolic triplets with prose labels. Episodic memory is mixed: prose observation keys plus symbolic fact lists and distributed-parametric embeddings. Contriever embeddings have ranking authority for retrieval but are transient derived state.

**Lineage.** The lineage is observation -> extracted triplets -> duplicate filtering/replacement -> graph state and episodic record -> retrieved subgraph/episodes -> planner/action prompt. It is implemented through object references and string content rather than stable IDs. Resetting an attempt discards active memory, and there is no regeneration or invalidation rule beyond rerunning the pipeline.

**Behavioral authority.** Stored triplets and episodes are knowledge artifacts while they serve as evidence about the world. They gain system-definition-artifact authority when inserted into planner/action prompts that instruct the agent to use memory, and the spatial graph gains stronger operational authority when `find_path()` turns remembered topology into executable hidden navigation steps.

**Scope.** The scope is per-run and per-environment instance. AriGraph can generalize the architecture across TextWorld tasks and QA datasets, but the learned memory contents are not promoted across runs or projects.

**Timing.** Learning is online during deployment. Each step writes memory before planning and action selection for the next step. The checked-in logs are durable traces after the fact, but they are not mined by the runtime into future-run memory.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AriGraph is an online trace-to-world-model system with symbolic artifact learning plus transient embedding-based activation. It strengthens the survey's distinction between in-episode adaptive memory and cross-session deploy-time learning: AriGraph clearly learns from traces during a run, but it does not yet promote those learned artifacts into durable cross-run procedures, notes, skills, or weights.

## Curiosity Pass

**The "knowledge graph" is simpler than the phrase suggests.** The central `ContrieverGraph` stores a list of triples and separate string embeddings; retrieval happens over stringified triples and endpoint expansion. Predicates are labels inside triplets, not typed relations with schemas, constraints, provenance, or graph-database query semantics.

**Replacement is the risky part.** Automatic extraction can add noisy facts, but replacement can delete useful state. The prompt explicitly tells the model to preserve non-conflicting facts, yet there is no deterministic check that a deletion is safe. That is acceptable for a benchmark agent but too weak for a durable KB lifecycle.

**Episodic memory is useful even though it is small.** AriGraph keeps full observations and scores them by both semantic similarity and fact overlap. That split is more behaviorally plausible than only embedding observations, because a prior episode can be retrieved for sharing concrete graph facts with the current situation.

**Logs are evidence, not active memory.** The repository includes many run logs, but the runtime does not load them as future experience. Calling AriGraph "learning" is accurate at the per-run world-model level; it would be inaccurate to describe it as cross-run self-improvement.

**The QA reuse is a useful stress test.** `musique_test_big.py` clears the graph per question, extracts triplets from paragraphs, retrieves a subgraph and episodic texts for the question, and asks an answerer to respond. That shows the architecture is not hardcoded only to TextWorld, but it still resets memory per task.

## What to Watch

- Whether future AriGraph versions persist graph/episodic memory across runs, with IDs back to source observations.
- Whether extraction and replacement get independent verification, confidence, or contradiction handling.
- Whether the hypergraph/thesis path becomes part of reported pipelines or remains an unused experiment.
- Whether logs become a training or memory source rather than evaluation evidence.
- Whether navigation affordances grow into a more general "memory creates tools/actions" pattern.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: AriGraph is an online observation-to-world-model case where learned artifacts stay within the run.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: AriGraph extracts structured memory from traces but shows why signal quality and review matter.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: graph and episodic memory are injected before planning/action, not only queried retrospectively.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: AriGraph's storage substrate, representational form, lineage, and behavioral authority diverge across raw logs, graph facts, episodes, embeddings, and prompts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: AriGraph's core value is activation of retained state through prompts and navigation affordances, not storage alone.
