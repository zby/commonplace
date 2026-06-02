---
description: "MiroShark review: Neo4j graph memory, swarm simulations, trace-derived belief state, MCP/report retrieval, and provenance exports"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# MiroShark

MiroShark, from Aaron Mars's `aaronjmars/MiroShark` repository, is a web application and CLI/MCP stack for turning source material into a Neo4j-backed social-simulation world. It ingests documents into a graph, generates personas, runs Twitter/Reddit/Polymarket-style agents over many rounds, updates beliefs and optional graph memory from simulation traces, and exposes reports, traces, exports, and provenance surfaces for finished simulations.

**Repository:** https://github.com/aaronjmars/MiroShark

**Reviewed commit:** [edf11dd6807c54133007f88f916ca3c385937ce9](https://github.com/aaronjmars/MiroShark/commit/edf11dd6807c54133007f88f916ca3c385937ce9)

**Last checked:** 2026-06-02

## Core Ideas

**The durable source-memory layer is Neo4j graph storage.** MiroShark replaced earlier Zep-style storage with a `GraphStorage` abstraction and `Neo4jStorage` implementation. Source text is chunked, passed through ontology-guided NER/relation extraction, embedded, entity-resolved, written as `:Entity`, `:Episode`, and `RELATION` structures, and indexed for vector, BM25, and traversal search ([backend/app/storage/graph_storage.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/storage/graph_storage.py), [backend/app/storage/neo4j_storage.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/storage/neo4j_storage.py), [backend/app/services/graph_builder.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/graph_builder.py)). The implementation tags graph edges by epistemic kind: `fact`, `belief`, or `observation`, plus `source_type`, `source_id`, `valid_at`, and `invalid_at`, so source-derived facts and simulation-derived opinions are not the same retained artifact even when both live in Neo4j ([backend/app/storage/neo4j_storage.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/storage/neo4j_storage.py)).

**Context efficiency is mostly engineered through search fusion, compaction, and scoped prompt injection.** Graph retrieval runs vector edge/node search, Neo4j fulltext search, and graph traversal, fuses the candidates, and optionally cross-encoder reranks the top pool before returning a small `limit` set ([backend/app/storage/search_service.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/storage/search_service.py)). Inside the simulation loop, old rounds are compacted into summaries, the previous round remains full-detail, and the current round includes only partial platform activity already seen, which is then injected into agents before they act ([backend/scripts/round_memory.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/scripts/round_memory.py), [backend/scripts/run_parallel_simulation.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/scripts/run_parallel_simulation.py)). This is stronger than a raw transcript window but still weaker than a governed knowledge-base route: actual retrieval precision, prompt dilution, and agent faithfulness are runtime properties not verified from code.

**Simulation traces become multiple retained surfaces.** The runner writes per-platform action logs and run state, while `BeliefTracker` persists `belief_states_<platform>.json`, `trajectory_<platform>.json`, and a merged `trajectory.json` after every round ([backend/app/services/simulation_runner.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/simulation_runner.py), [backend/scripts/belief_integration.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/scripts/belief_integration.py)). Belief updates are heuristic rather than LLM-learned: posts seen, engagement, novelty, trust, confidence, and stance heuristics change mutable per-agent belief state ([backend/wonderwall/social_agent/belief_state.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/wonderwall/social_agent/belief_state.py), [backend/wonderwall/social_agent/round_analyzer.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/wonderwall/social_agent/round_analyzer.py)). Optional graph-memory update converts batched agent activities into natural-language episodes, then re-enters the normal graph extraction path as `belief` or `observation` edges ([backend/app/services/graph_memory_updater.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/graph_memory_updater.py), [backend/app/api/simulation.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/api/simulation.py)).

**Reports are both outputs and inspectable reasoning traces.** The report agent uses ReACT-style tool calls over graph search, simulation feed, market state, trajectory analysis, equilibrium analysis, and report context ([backend/app/services/report_agent.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/report_agent.py), [backend/app/services/graph_tools.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/graph_tools.py)). Its reasoning recorder persists each report section as a `Report -> ReportSection -> ReasoningStep` subgraph with `thought`, `tool_call`, `observation`, and `conclusion` nodes, making report decisions queryable after generation ([backend/app/storage/reasoning_trace.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/storage/reasoning_trace.py)).

**There are two MCP surfaces with different authority.** The standalone stdio MCP server exposes graph and report tools to Claude Desktop, Cursor, Windsurf, and Continue: list graphs, search graph, browse/search communities, list reports, list sections, and fetch reasoning traces ([backend/mcp_server.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/mcp_server.py), [docs/MCP.md](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/docs/MCP.md)). Separately, simulation personas can be given per-agent MCP tools: the runner injects a catalogue, parses `<mcp_call .../>` tags from generated posts, dispatches calls through subprocess bridges, and injects results into the next round's system message ([backend/scripts/mcp_agent_injection.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/scripts/mcp_agent_injection.py), [backend/scripts/run_parallel_simulation.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/scripts/run_parallel_simulation.py)). The first is pull access for an external assistant; the second is push context for a simulated agent selected by persona configuration.

**The product surface is broad and deployment-oriented.** The repository includes Flask backend APIs, a Vite frontend, deployment files for Docker/Railway/Render/Cloud Run, a dependency-light HTTP CLI, public watch/share/gallery/export endpoints, bilingual docs, and operator-facing configuration docs ([backend/cli.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/cli.py), [frontend](https://github.com/aaronjmars/MiroShark/tree/edf11dd6807c54133007f88f916ca3c385937ce9/frontend), [docs/INSTALL.md](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/docs/INSTALL.md), [README_DEPLOYMENT.md](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/README_DEPLOYMENT.md)). This matters for adoption: the memory system is not a library alone; it is wrapped in a runnable simulation workbench with inspectable exports.

**The citation layer treats finished simulations as provenance-bearing artifacts.** `reproduce.json` exports a schema-locked blob with scenario, platform toggles, rounds, timing, lineage, director events, and config reasoning ([backend/app/services/repro_export.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/repro_export.py)). Optional DKG publishing anchors a Turtle representation and reproduce hash through OriginTrail's Working Memory -> Shared Working Memory -> Verified Memory flow, while WaybackClaw submission stores a JSON snapshot with IPFS/Nostr identifiers ([backend/app/services/dkg_publisher.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/dkg_publisher.py), [docs/DKG.md](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/docs/DKG.md), [backend/app/services/waybackclaw_publisher.py](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/backend/app/services/waybackclaw_publisher.py), [docs/WAYBACKCLAW.md](https://github.com/aaronjmars/MiroShark/blob/edf11dd6807c54133007f88f916ca3c385937ce9/docs/WAYBACKCLAW.md)). These are not agent memory in the narrow sense, but they strengthen lineage and auditability for simulation outputs.

## Artifact analysis

- **Storage substrate:** `graph` — Neo4j plus on-disk upload/project state
- **Representational form:** `mixed` — Mixed symbolic/prose/vector, with entity nodes, relation edges, ontology JSON, raw episode text, embeddings, temporal fields, and epistemic kind fields

**Source graph.** Storage substrate: Neo4j plus on-disk upload/project state. Representational form: mixed symbolic/prose/vector, with entity nodes, relation edges, ontology JSON, raw episode text, embeddings, temporal fields, and epistemic kind fields. Lineage: authored or imported source text is chunked into NER-derived entities and relation facts; entity resolution and contradiction detection derive a current graph view while retaining invalidated edges for point-in-time queries. Behavioral authority: mostly knowledge artifact for simulation setup, report evidence, graph search, MCP retrieval, and frontend display; it gains ranking authority when vector/BM25/traversal/rerank decide what facts enter a report or assistant response.

**Simulation runtime state.** Storage substrate: simulation directories under the backend upload area, per-platform SQLite databases, `actions.jsonl`, `run_state.json`, `state.json`, platform trajectory files, merged `trajectory.json`, and belief-state JSON. Representational form: symbolic JSON/SQLite records plus prose action content. Lineage: trace-derived from agent actions, database rows, engagement, market events, and heuristic belief updates. Behavioral authority: both knowledge artifact and system-definition artifact. It is evidence for exports, reports, watch pages, and charts, but belief summaries and round memory are injected into active agents before later actions, giving them advisory system-definition force inside the simulation.

**Optional graph memory from simulation traces.** Storage substrate: Neo4j, reached through `GraphMemoryUpdater`. Representational form: natural-language descriptions converted through NER into graph nodes/edges. Lineage: trace-extracted from batched agent activity; expressive actions become `belief` edges and other actions become `observation` edges with `source_type="agent"` and source ids such as `twitter:round_7`. Behavioral authority: knowledge artifact for later analysis and retrieval; ranking authority when it appears in graph search; weaker than source facts because extraction rephrases simulated actions and depends on the NER/LLM path.

**Round memory and belief injection blocks.** Storage substrate: in-process `RoundMemory` records during a run, plus persisted belief/trajectory JSON after each round. Representational form: prose summaries and symbolic belief positions/confidence/trust. Lineage: trace-derived from prior rounds, compacted by an LLM when available, or summarized by fallback counts; beliefs update through heuristics over observed posts and engagement. Behavioral authority: system-definition artifact for simulated agents because the runner appends marker-delimited sections to system messages before the next action.

**Report and reasoning artifacts.** Storage substrate: report folders for JSON/Markdown/log files and Neo4j report/reasoning subgraphs. Representational form: prose reports, JSONL logs, and symbolic `ReasoningStep` graph nodes. Lineage: derived from simulation state, graph search, tool calls, observations, market state, and LLM-generated conclusions. Behavioral authority: knowledge artifact for users and external assistants; audit artifact for inspecting why a report said something; possible future evaluation input if traces are mined across reports.

**MCP and CLI surfaces.** Storage substrate: no independent memory store; they expose existing backend/Neo4j/simulation artifacts. Representational form: symbolic tool schemas and prose/JSON results. Lineage: derived views over the same graph/report/simulation state. Behavioral authority: pull tools provide context or evidence to a calling assistant; per-agent MCP injection becomes system-definition context for selected simulated agents because tool catalogues and prior results are inserted into their system messages.

**Provenance exports.** Storage substrate: simulation directories for `reproduce.json`, `dkg-citation.json`, and `waybackclaw-record.json`, plus optional DKG/IPFS/Nostr external stores. Representational form: symbolic JSON, RDF/Turtle, hashes, UALs, transaction ids, CIDs, and event ids. Lineage: derived from finished simulation state and reproducibility config bytes. Behavioral authority: audit and citation authority rather than runtime memory; it constrains what a later reader can verify about a published simulation.

Promotion path is present but uneven. Source documents can become graph facts; simulation actions can become graph beliefs/observations; report reasoning can become a queryable trace; finished simulations can become provenance-anchored public artifacts. The system does not yet show a governed promotion path from trace-derived observations into stable rules, validators, or high-authority instructions outside the simulation.

## Comparison with Our System

| Dimension | MiroShark | Commonplace |
|---|---|---|
| Primary purpose | Run and publish graph-grounded swarm simulations | Build and maintain an agent-operated methodology KB |
| Canonical store | Neo4j graph plus simulation directories and frontend/backend state | Git-tracked markdown collections, type specs, validation, reports, and indexes |
| Retained traces | Agent actions, belief trajectories, report ReACT traces, optional graph-memory edges | Sources, notes, review reports, validation output, workshop artifacts |
| Read-back | Hybrid graph search, report tools, MCP tools, pre-round prompt injection | `rg`, indexes, links, skills, validation and review workflows |
| Trace-derived learning | Heuristic belief updates, round compaction, action-to-graph extraction, reasoning traces | Mostly explicit source-grounded writing and review; trace learning is a methodology axis, not the default store |
| Governance | Runtime flags, feature gates, provenance exports, public/private gates | Collection contracts, schemas, deterministic validation, semantic review gates, git history |

MiroShark is much more operational than Commonplace. It runs a world, captures the traces, and turns those traces into prompts, graphs, reports, exports, and public artifacts. Commonplace is narrower and more static: it aims to make retained methodology artifacts inspectable, typed, validated, and durable in git. The useful comparison is not "graph database versus markdown"; it is how each system assigns authority to retained state.

MiroShark's most important authority split is source facts versus simulated beliefs. Source-derived graph facts can ground persona generation and report search. Simulation-derived actions and beliefs can be stored in the same graph, but they are explicitly `belief` or `observation` edges. That split is a good discipline: a simulated trader's claim should not silently become a world fact just because it entered the graph.

Compared with Commonplace, MiroShark has richer activation machinery. It injects compacted history, beliefs, market/media context, director events, and MCP results into agents at the point of action. Commonplace has stronger artifact governance but weaker automatic activation: the agent must search, follow indexes, or run skills. MiroShark shows the cost and value of pushing state into context: agents get timely situational memory, but the system must manage prompt growth, stale sections, and faithfulness.

The report reasoning trace is a strong analogue to Commonplace review reports. Both preserve why an output happened, not only the output. The difference is substrate and lifecycle. MiroShark stores traces in Neo4j and report folders for later inspection; Commonplace stores review artifacts in the repo with status, validation, and replacement conventions.

**Read-back:** `both` — External graph/report/MCP queries are pull, while simulation round memory, belief state, director events, market/media context, and per-agent MCP results are pushed into active agents before later actions

### Borrowable Ideas

**Preserve epistemic kind on graph-like artifacts.** Commonplace should keep distinguishing source facts, agent beliefs, observations, generated summaries, and review judgments when any future graph/index layer is added. Ready now as a vocabulary and schema requirement.

**Use sliding-window compaction for trace-heavy workshops.** MiroShark's round memory pattern is a practical template: ancient summary, recent compacted rounds, previous full detail, current partial state. Commonplace could borrow it for long workshop investigations or review sweeps where every raw event cannot stay in context. Ready as a workshop/run-report design pattern.

**Expose reasoning traces as first-class artifacts.** The report `ReasoningStep` subgraph suggests a Commonplace analogue for semantic review bundles: preserve tool calls, observations, and conclusions as navigable evidence, not only final notes. Needs a concrete use case before adding a new durable artifact type.

**Keep provenance hashes close to public outputs.** `reproduce.json`, DKG, and WaybackClaw are heavier than Commonplace needs for ordinary notes, but the idea is useful for published evaluations: export the exact parameters and source hashes that let someone reproduce or verify a claim. Ready for eval/report artifacts, not for every note.

**Do not collapse simulation traces into method claims.** MiroShark's graph-memory update is useful because it labels trace-derived edges as beliefs or observations. Commonplace should keep a similarly explicit promotion boundary: repeated trace evidence can propose a rule, but a reviewed instruction needs a separate artifact and validation.

## Trace-derived learning placement

**Trace source.** MiroShark qualifies as trace-derived learning. The qualifying traces are platform action logs, per-platform SQLite rows, simulated posts/comments/trades, engagement, market state, director/counterfactual events, per-round belief snapshots, and report-agent ReACT tool/thought/observation traces. Source documents are not trace-derived; they are imported source material that generates graph facts.

**Extraction.** Extraction has several routes. `BeliefTracker` and `RoundAnalyzer` compute belief deltas from posts seen, engagement, trust, novelty, and sentiment heuristics. `RoundMemory` compacts prior rounds into prompt summaries. `GraphMemoryUpdater` converts batched agent actions into natural-language episode text, then reuses NER/entity-resolution/embedding to write graph edges. `ReasoningTraceRecorder` records report-agent thoughts, tool calls, observations, and conclusions as a Neo4j subgraph.

**Scope and timing.** Belief and round memory are per-simulation and online: they update during a run and influence the next round. Graph-memory update is optional and online while the runner tails action logs. Report reasoning traces are generated during report creation after or during a completed simulation. DKG and WaybackClaw outputs are explicit post-publication provenance actions.

**Raw versus distilled authority.** Raw action logs, SQLite rows, and per-round snapshots are knowledge artifacts. Compacted round memory and belief prompt text are distilled system-definition artifacts for active simulated agents. Graph-memory edges are derived knowledge artifacts with epistemic labels; they become ranking inputs when later retrieved. Report reasoning traces are audit artifacts unless a later process uses them to change report generation or evaluation policy.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), MiroShark belongs in the simulation-trace-to-state and trace-to-graph families. It strengthens the survey claim that trace learning often splits into raw evidence and behavior-shaping summaries: the same run produces logs, trajectories, prompt injections, graph edges, report traces, and public provenance records with different authority.

## Read-back placement

**Direction.** MiroShark is both pull and push. Graph search, report tools, CLI report/status/frame commands, and the standalone MCP server are pull surfaces. Inside the simulation loop, agents receive pushed memory/context before action: belief state, compacted round history, market/media context, director events, and per-agent MCP results.

**Trigger and relevance signal.** Push activation is engineered by simulation round, platform membership, active-agent selection, feature flags, and persona/tool configuration. It is not semantic relevance matching over the whole graph, but it is a before-action hook with scope controls: only active agents in the current platform round receive the relevant marker-delimited blocks, and tool results are delivered to the agent that requested them.

**Timing relative to action.** Round memory, beliefs, market/media context, director events, and MCP results are injected before `env.step`, so they can change the next post, trade, or comment. Belief updates and MCP dispatch happen after a round, then affect the next activation. Report reasoning traces are post-hoc and do not affect the simulation that produced them.

**Selection, scope, and complexity.** Round memory limits complexity by summarizing ancient rounds, keeping recent compacted summaries, preserving the previous round in full detail, and using current partial context. Belief state is per-agent and compact. MCP results are capped in the injection layer. The graph search path has a `limit`, candidate-pool sizing, kind/time filters, and reranking, but graph search only acts when called by a report agent, MCP client, or API consumer.

**Authority at consumption.** Simulation push blocks are advisory system-message context, not hard gates. They can guide actions but do not enforce them. MCP graph/search tools supply evidence to external assistants. Report reasoning traces supply audit context. Effective faithfulness is not verified from code; I did not find WITH/WITHOUT ablation or post-action checks proving that injected memory changes behavior as intended.

**Other consumers.** Human users consume the same retained state through frontend watch/share/gallery/report pages, transcript/trajectory/export endpoints, CLI commands, MCP clients, DKG/WaybackClaw records, notifications, and deployment docs. These consumer surfaces are not all "memory" for an agent, but they shape reviewability and reuse.

## Curiosity Pass

**The graph is both pre-simulation grounding and post-simulation memory.** That dual use is powerful, but it is also the main place where lineage discipline matters. The code's `kind` and `source_type` fields are the safeguard against treating simulated beliefs as source facts.

**The strongest push path is not the graph search path.** MiroShark's relevance-gated search is pull unless a caller invokes it. The actual push mechanism is the simulation loop's pre-round injection of compacted history, beliefs, context, and tool results.

**Round compaction is behavior-changing but not durable in the same way as graph edges.** The compacted summaries live in the in-process `RoundMemory` object during a run. Belief trajectories and action logs persist, but the exact LLM-compressed prompt summaries are not obviously retained as canonical artifacts.

**Report reasoning traces are unusually useful for review.** They make "why did the report conclude this?" queryable, which is often missing from agent-memory systems. The remaining gap is evaluation: traces are inspectable, but not clearly used to improve or gate future reports.

**The provenance stack is more mature than the governance stack.** DKG, WaybackClaw, `reproduce.json`, public/private gates, and export formats make finished simulations citable. They do not by themselves validate that the simulated world, agent outputs, or report conclusions are accurate.

**MCP appears in two quite different roles.** The standalone MCP server gives external assistants pull access to graph/report memory. Per-agent MCP tools change the simulated agents' action loop. Reviews should not collapse those into one "MCP integration" claim.

## What to Watch

- Whether graph-memory update becomes enabled by default or remains opt-in; that determines whether simulation traces routinely join the graph memory store.
- Whether trace-derived graph edges gain stronger provenance, such as original action ids, source offsets, or links back to exact `actions.jsonl` rows.
- Whether round-memory compaction outputs become durable artifacts, which would make their lineage and reviewability more important.
- Whether report reasoning traces feed evaluation, regression tests, or report-generation improvements rather than staying audit-only.
- Whether the system adds faithfulness checks for pushed memory, such as ablations comparing runs with and without belief/round/context injection.
- Whether DKG and WaybackClaw records are used as downstream verification inputs or remain publication extras.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: MiroShark turns simulation actions into beliefs, prompt summaries, graph edges, trajectories, and reasoning traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: graph storage is pull until search is invoked, while simulation memory changes behavior only through explicit pre-round injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: MiroShark requires separating source graph facts, simulated beliefs, trajectories, prompt injections, report traces, MCP tools, and provenance records by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: source graph facts, action logs, trajectories, reports, and provenance records mainly serve as evidence, reference, or audit context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: pre-round injected memory, belief context, director events, tool catalogues, search ranking, and feature flags configure or influence future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: simulation traces can produce durable state, but promotion into higher-authority rules still needs an explicit review boundary.
