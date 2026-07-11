---
description: "MiroShark review: simulation knowledge graph with Neo4j graph memory, trace-derived agent activity edges, report-agent reasoning traces, and many public export surfaces"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-derived]
---

# MiroShark

MiroShark is a simulation platform that turns source material and a scenario into a Neo4j-backed world graph, LLM-generated agent personas, social-platform simulations, report-agent analysis, and public share/export surfaces. At the reviewed commit its memory-relevant core is not one chat memory store; it is a graph substrate plus on-disk simulation artifacts, with automatic writes from document ingestion, simulation agent actions, report-agent traces, community summaries, and public analytics counters.

**Repository:** https://github.com/aaronjmars/MiroShark

**Reviewed commit:** [570cd00ea20682145a55b6c3c4f5fa20a73693a2](https://github.com/aaronjmars/MiroShark/commit/570cd00ea20682145a55b6c3c4f5fa20a73693a2)

**Last checked:** 2026-06-04

## Core Ideas

**Neo4j is the durable graph memory substrate.** `GraphStorage` defines graph lifecycle, ontology, text ingestion, node/edge reads, hybrid search, graph data export, and point-in-time search parameters; `Neo4jStorage` implements those operations with graph nodes, entity nodes, episode nodes, relation edges, embeddings, full-text indexes, and contradiction invalidation ([graph_storage.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/storage/graph_storage.py), [neo4j_storage.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/storage/neo4j_storage.py)). A text chunk becomes an `Episode`, extracted entities, relation facts, embeddings, timestamps, epistemic `kind`, and source metadata rather than remaining a flat document.

**Simulation preparation reads the graph into generated agents and runtime configuration.** `SimulationManager.prepare_simulation()` filters graph entities, generates Wonderwall profiles from those entities, and passes `graph_id`, document text, and entity records into `SimulationConfigGenerator.generate_config()`; the generator writes time, event, platform, market, and per-agent configuration JSON for the simulation ([simulation_manager.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/simulation_manager.py), [simulation_config_generator.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/simulation_config_generator.py)). This is read-back at preparation time: retained graph facts shape the generated agent population and the run envelope.

**Agent actions can be written back into the graph as belief or observation edges.** `GraphMemoryUpdater` consumes simulation activity dictionaries, converts posts, likes, follows, comments, searches, and other actions into natural-language episode text, batches them by platform, and calls `storage.add_text()` with `source_type="agent"`, round-level source ids, `valid_at`, and `kind="belief"` for expressive actions or `kind="observation"` for other actions ([graph_memory_updater.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/graph_memory_updater.py), [simulation.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/api/simulation.py)). The stored artifact is trace-derived graph state, not just a transcript.

**Graph retrieval is hybrid and tool-shaped.** `SearchService` combines vector search, BM25 full-text search, graph-neighbor traversal, optional temporal and epistemic filters, result fusion, and optional reranking; `GraphToolsService` wraps that store as `quick_search`, `panorama_search`, `insight_forge`, `browse_clusters`, graph-structure tools, and agent interviews for the report agent ([search_service.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/storage/search_service.py), [graph_tools.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/graph_tools.py)). The same graph is also exposed through a stdio MCP server with tools for graph listing, graph search, community browsing, reports, sections, and reasoning traces ([mcp_server.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/mcp_server.py), [mcp.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/api/mcp.py)).

**The report agent is a graph-using ReACT agent with persistent traces.** `ReportAgent` preloads graph context for outline planning, then generates sections through a ReACT loop that can call graph tools, simulation feed tools, interviews, trajectory analysis, market state, and cluster browsing; `ReportLogger` writes JSONL logs, and `ReasoningTraceRecorder` can persist thoughts, tool calls, observations, and conclusions as Neo4j `Report`, `ReportSection`, and `ReasoningStep` subgraphs ([report_agent.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/report_agent.py), [reasoning_trace.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/storage/reasoning_trace.py)).

**The new export, clone, surface, and stats APIs widen provenance and consumer surfaces without changing the core memory authority.** `agent_export.py` derives machine-readable participant rosters from profile files and trajectory data; `clone_service.py` reconstructs a wire-compatible `/api/simulation/create` payload; `repro_export.py` and `lineage_service.py` expose reproducibility and fork/counterfactual parentage; `surfaces_catalog.py`, `surface_stats.py`, and `project_stats.py` publish discoverability and usage analytics ([agent_export.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/agent_export.py), [clone_service.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/clone_service.py), [repro_export.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/repro_export.py), [lineage_service.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/lineage_service.py), [surfaces_catalog.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/surfaces_catalog.py), [surface_stats.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/surface_stats.py), [project_stats.py](https://github.com/aaronjmars/MiroShark/blob/570cd00ea20682145a55b6c3c4f5fa20a73693a2/backend/app/services/project_stats.py)). These are important provenance and adoption surfaces, but they mostly serve humans, integrators, and evaluators rather than injecting memory into a future agent call.

## Artifact analysis

- **Storage substrate:** `graph` `files` — durable memory lives in Neo4j graphs, entities, relation edges, episodes, communities, and reasoning-trace subgraphs, plus on-disk simulation folders, report folders, JSON/JSONL logs, transcripts, exports, profiles, configs, counters, and share artifacts.
- **Representational form:** `prose` `symbolic` `parametric` — raw and generated prose includes documents, posts, transcripts, reports, cluster summaries, and persona text; symbolic state includes graph labels/properties, JSON configs, API routes, schemas, counters, lineage records, and tool definitions; parametric state includes entity, fact, and community embeddings used for search and ranking.
- **Lineage:** `authored` `imported` `trace-extracted` — authored code, prompts, templates, and catalog entries define the system; external documents and scenario inputs are imported into graph/config state; simulation activities, trajectory files, surface counters, report logs, and reasoning traces are extracted from runtime traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — graph facts, reports, transcripts, and exports serve as knowledge; prompts, generated configs, MCP/server tools, and report-agent tool definitions instruct and route; route validators and publish gates validate; embeddings, BM25, traversal, rerankers, community search, gallery sorting, and surface stats rank; graph updates and community summaries learn from traces.

**Graph entities, relation edges, and episodes.** Storage substrate: Neo4j `Graph`, `Episode`, `Entity`, `RELATION`, and `Community` nodes/edges. Representational form: prose data/facts/summaries plus symbolic graph properties and distributed embeddings. Lineage: imported source text and scenario material, plus trace-extracted agent activity batches when graph memory is enabled. Behavioral authority: knowledge artifacts when browsed or exported; ranking/routing artifacts when hybrid search selects facts, entities, or clusters; weak instruction context when injected into report or simulation-generation prompts.

**Simulation folders.** Storage substrate: on-disk state files, `simulation_config.json`, profile JSON, action logs, trajectory JSON, quality records, platform folders, and public export derivatives. Representational form: symbolic JSON/JSONL plus generated prose personas, posts, transcripts, reports, and share text. Lineage: generated from project inputs, graph entities, LLM calls, simulated actions, and operator settings. Behavioral authority: configs and profiles instruct the simulator; trajectories, actions, and exports are knowledge artifacts for analysis, reproduction, and public citation.

**Report-agent artifacts.** Storage substrate: files under the reports directory plus optional Neo4j report subgraphs. Representational form: report Markdown/prose, JSON metadata/progress/outline/logs, and symbolic reasoning-step graph nodes. Lineage: trace-extracted from the report-generation ReACT loop and its graph-tool observations. Behavioral authority: report files are knowledge artifacts; reasoning traces become audit and future-query material; report-agent prompts and tool schemas are system-definition artifacts that govern generation.

**Retrieval indexes and community summaries.** Storage substrate: Neo4j vector/full-text indexes, relation/entity embeddings, and `Community` nodes. Representational form: parametric vectors, symbolic index configuration, and prose summaries. Lineage: derived from graph facts and entity neighborhoods; community building clusters current valid graph edges and asks an LLM to summarize each kept community. Behavioral authority: ranking and routing authority over what an agent, MCP client, report, or API caller sees first.

**Public surfaces and analytics.** Storage substrate: service modules, route handlers, simulation-folder files, `surface-stats.json`, archive manifests, reproducibility blobs, lineage payloads, and aggregate stats scans. Representational form: symbolic JSON/CSV/JSONL/SVG/notebook/ZIP plus prose Markdown/thread/transcript outputs. Lineage: derived views over simulation config, state, profiles, actions, trajectories, quality, and public-gate status. Behavioral authority: mostly knowledge, provenance, discovery, and evaluation evidence; the clone payload and reproduce config can route future reproduction work, but they do not by themselves push memory into an agent.

Promotion path: source/scenario material becomes graph entities and relation facts; graph state becomes generated personas and simulation config; simulation actions can become new graph belief/observation edges; report generation can turn graph state and simulation traces into report files and optional reasoning-trace subgraphs; community browsing can promote graph neighborhoods into summarized cluster nodes. MiroShark's strongest promotion step is trace -> graph fact/trace subgraph -> retrieval/report/export, not trace -> reviewed rule or enforced policy.

## Comparison with Our System

| Dimension | MiroShark | Commonplace |
|---|---|---|
| Primary purpose | Simulate social reaction and publish citable/reproducible simulation surfaces | Build and maintain a methodology KB for agent-operated knowledge systems |
| Main substrate | Neo4j graph plus simulation/report files and public APIs | Git-tracked Markdown collections, type specs, indexes, sources, and review reports |
| Write path | Document graph ingestion, LLM extraction, simulation traces, report traces, counters, export derivations | Authored/snapshotted artifacts, validation, review gates, index generation |
| Read-back | Automatic graph context in simulation/report generation, ReACT/MCP/API graph pulls, public exports | Mostly deliberate search/index/link/skill pull with some instruction loading |
| Governance | API validation, publish gates, route auth, contradiction invalidation, temporal filters, traceability fields | Collection contracts, schemas, citations, deterministic validators, semantic reviews, git history |

MiroShark is more operational and service-shaped than Commonplace. It treats memory as a live substrate for simulations and reports: graphs, embeddings, tool APIs, run state, counters, exports, and share pages all keep moving. Commonplace is slower and more inspectable: its artifacts are typed prose and symbolic files whose behavioral authority is explicit in collection contracts, validators, and review workflows.

The strongest alignment is provenance. MiroShark's newer clone, reproduce, lineage, roster, surface-catalog, and stats APIs make simulation outputs more citable and reproducible. That resembles Commonplace's preference for retained artifacts that can explain where they came from and how they should be consumed. The difference is that MiroShark's provenance mostly supports external consumers and reruns, while Commonplace's provenance supports artifact review, invalidation, and controlled promotion to instructions or validators.

The main tradeoff is automatic authority. MiroShark can convert live simulated behavior into graph facts and later retrieve those facts for analysis. That is powerful, but the graph fact itself is LLM-extracted from a synthetic trace, not a reviewed KB claim. Commonplace should treat this as a useful runtime evidence layer, not as a model for promoting generated claims directly into durable methodology.

### Borrowable Ideas

**Make reproduction an explicit export surface.** Ready now. Commonplace already has source snapshots and replacement history, but review artifacts could expose a small machine-readable reproduction block: source URL, commit, checkout path, reviewed files, and validation command.

**Separate surface catalogs from documentation.** Ready for public command/API surfaces. MiroShark's literal surface catalog gives integrators a stable discovery API without scraping docs; Commonplace could borrow the idea for CLI commands, skills, or generated review reports if consumers need machine-readable capability discovery.

**Use trace-derived graph updates as evidence, not final authority.** Useful for workshops. A Commonplace analogue could convert agent review events into queryable evidence records while keeping promotion to notes, instructions, or validators behind review.

**Expose clone/fork lineage for analyses.** Ready conceptually. MiroShark's lineage view is a good pattern for showing how a retained artifact branched from a prior run. Commonplace could use similar lineage for iterative reviews, replacement reviews, and generated note variants.

**Do not borrow the whole public-surface multiplier without a consumer.** MiroShark has many share/export surfaces because simulations are products to publish, cite, replay, and embed. Commonplace should add surfaces only when they improve agent work or review, not because every artifact can be exported.

## Write side

**Write agency:** `manual` `automatic` — users/operators create projects, graphs, simulations, forks, reports, share settings, and exports, while code automatically ingests text into Neo4j, generates configs/personas, writes simulation and report files, converts agent actions into graph memory, records report reasoning traces, builds community summaries, updates counters, and derives public export payloads.

**Curation operations:** `dedup` `synthesize` `invalidate` `consolidate` — entity resolution merges extracted entity variants; NER/relation extraction, generated configs, reports, and community summaries synthesize retained artifacts; contradiction detection invalidates superseded edges while preserving history; community building consolidates graph neighborhoods into cluster summaries.

### Trace-derived learning

**Trace source:** `tool-traces` `event-streams` `trajectories` — qualifying traces include simulation action logs, platform activity events, trajectory files, surface-request counters, report-agent thoughts/tool calls/observations, and report logs.

**Learning scope:** `per-project` `cross-task` — graph state is scoped by project/graph/simulation, while a graph can be reused across simulations, reports, MCP clients, and public analysis surfaces.

**Learning timing:** `online` `staged` — graph memory updates can run during simulation, report traces are captured during report generation, and community summaries/export surfaces are built or served in later stages.

**Distilled form:** `prose` `symbolic` `parametric` — traces become prose episode text, relation facts, reports, and summaries; symbolic graph nodes/edges/properties, JSON logs, lineage, counters, and exports; and embeddings over facts/entities/communities.

**Trace source.** MiroShark qualifies as trace-derived. `GraphMemoryUpdater` records simulated agent behavior by converting activity events into natural-language episodes and extracting graph edges from them. `ReasoningTraceRecorder` records the report agent's ReACT thought/tool/observation/conclusion chain into Neo4j. Simulation trajectory and action files also feed transcript, roster, stats, report, and public analysis surfaces.

**Extraction.** Extraction is mixed. Agent activities are deterministically formatted into episode text, then passed through the graph text ingestion path that runs NER/relation extraction, embeddings, entity resolution, contradiction detection, and Neo4j writes. Report traces are recorded structurally from the ReACT loop. Community summaries are LLM-mediated distillations over graph clusters. Surface counters are deterministic read-modify-write analytics over public route serves.

**Four fields.** The raw stage is action logs, trajectory files, report JSONL logs, and route serve events. The distilled stage is graph edges/entities/episodes, community summaries, report sections, reasoning-step subgraphs, and export payloads. Raw traces are mostly knowledge/audit artifacts; distilled graph state gains ranking/routing authority through search and report tools, while generated configs/profiles gain instruction authority inside the simulator.

**Scope and timing.** Trace learning is per simulation and per graph, but the graph's reuse across reports, MCP tools, and future simulation preparation gives it cross-task consequences. Timing is mixed: simulation graph updates are online relative to a running sim; report traces are online during report generation; public exports, clone payloads, project stats, surface stats, and community summaries are staged or read-time derivations.

**Survey note.** MiroShark strengthens the survey distinction between trace storage and behavior-shaping retrieval. The important step is not that action logs exist; it is that selected traces become graph edges, report subgraphs, community nodes, and exports that later searches, reports, and reproductions can consume.

## Read-back

**Read-back:** `both` — Graph/API/MCP/report tools are pull surfaces, while simulation preparation and report outline planning also push graph-derived context into downstream LLM calls before those calls act.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — push and pull paths use graph ids, simulation ids, report ids, entity ids, route ids, and surface keys as identifiers, and graph search uses BM25/full-text plus vector similarity over the current query or scenario.

**Faithfulness tested:** `no` — the code exposes retrieval, reports, traces, exports, and stats, but I did not find a standing with/without-memory ablation or post-action audit proving that read-back changed agent behavior faithfully.

Simulation preparation is a push-like path from the receiving LLM's perspective: the prepare flow reads graph entities and document text, then includes them in profile/config-generation calls. Report outline planning is also push-like: `ReportAgent._plan_outline()` calls `get_simulation_context()` before outline generation and includes graph statistics, entity types, and related facts in the prompt. The report section ReACT loop and MCP tools are pull: the agent or external client deliberately calls `quick_search`, `insight_forge`, `panorama_search`, `browse_clusters`, `search_graph`, `get_reasoning_trace`, or related tools.

Targeting is mixed. Identifier targeting appears through `graph_id`, `simulation_id`, report ids, section ids, entity UUIDs, community UUIDs, project ids, and route parameters. Instance relevance appears when a scenario, query, report section, or user-supplied MCP query is embedded, searched lexically, expanded through graph traversal, or decomposed into subqueries by `insight_forge`.

The main injection points are pre-invocation: simulation configuration/profile prompts, report outline prompts, report-section tool observations appended to the ReACT conversation, and MCP tool results returned to the host agent. After-run exports and counters are write-side or consumer surfaces, not a separate post-action read-back path.

Selection is bounded mostly by `limit`, configured candidate pool sizes, graph search seed counts, community caps, and report prompt truncation. Complexity can still be high: a graph query can combine vector hits, full-text hits, graph traversal, reranking, temporal filtering, epistemic kind filtering, community summaries, and report-agent subquery generation.

Authority at consumption depends on the path. Graph facts in report prompts are advisory knowledge with some ranking force. Generated simulation config and profiles have stronger instruction authority over simulator behavior. MCP and API search results are available context until the host agent chooses how to use them. Public clone/reproduce/lineage surfaces route future reruns and analysis, but they do not automatically affect an agent unless a caller consumes them.

Faithfulness is structurally unverified. MiroShark can show what was retrieved, logged, exported, or counted, and reasoning traces can audit a report section's tool path. That is not the same as testing whether injected graph context caused correct downstream behavior.

Other consumers include frontend users, public viewers, researchers downloading trajectories/notebooks/archives, webhook recipients, MCP clients, social unfurlers, gallery browsers, and operators reading project/platform/surface stats.

## Curiosity Pass

**The graph memory update loop is synthetic-trace learning.** It records behavior produced by simulated agents, not observations of real users. That is still trace-derived, but the authority of the learned graph facts should be read as simulation evidence, not world truth.

**Report reasoning traces are more auditable than most report agents.** The Neo4j `ReportSection` and `ReasoningStep` subgraph is a useful audit design because it preserves thoughts, tool calls, observations, and final section text in the same graph family as the facts being queried.

**Public surfaces are not the same as memory read-back.** The new roster, clone, reproduce, lineage, surface catalog, surface stats, and project stats APIs materially improve provenance and downstream use. They do not by themselves change the read-back classification unless a host agent consumes them.

**Community summaries are a compact graph-memory layer.** Auto-building cluster summaries on first browse gives the report agent a zoom-out path before drilling into individual facts. The cost is another LLM-derived layer whose source graph and rebuild conditions matter.

**Contradiction invalidation is the closest thing to truth maintenance.** Edges are marked invalid/expired rather than deleted, and search supports `as_of` and `include_invalidated`. That is stronger governance than plain vector memory, though the contradiction detector's semantic quality is not established here.

## What to Watch

- Whether graph memory updates are enabled by default for simulations or remain an optional run flag; that determines whether trace-derived graph learning is routine or situational.
- Whether future reports use stored reasoning traces as retrieval evidence, not only audit artifacts; that would make report traces part of future read-back rather than post-hoc observability.
- Whether community summaries gain provenance fields listing member entity ids, source edge ids, and rebuild hashes; that would make the zoom-out layer easier to validate and invalidate.
- Whether clone/reproduce/lineage exports are consumed by an agent workflow for automatic reruns or counterfactual planning; that would raise their behavioral authority from provenance surface to routing input.
- Whether the system adds faithfulness tests for graph read-back, such as report generation with and without retrieved graph context or perturbation tests on graph facts.

## Bottom Line

MiroShark is a graph-centered simulation memory system with unusually broad public provenance surfaces. Its most distinctive memory design is the loop from source/scenario material and simulated activity traces into Neo4j graph state, then back out through simulation preparation, report-agent retrieval, MCP tools, community summaries, and reproducible exports. For Commonplace, the strongest borrow is not the full simulation stack; it is the combination of trace-derived graph evidence, explicit lineage/reproduction surfaces, and audit-ready reasoning traces.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: MiroShark converts simulation actions and report-agent traces into durable graph/report artifacts.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: MiroShark has both stored graph memory and concrete read-back paths through preparation, reports, MCP, and APIs.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: graph edges, embeddings, generated configs, reports, reasoning traces, and export surfaces differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: graph facts, transcripts, reports, public exports, and stats are mostly evidence/context unless a downstream workflow gives them stronger force.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated simulation configs, profile prompts, route handlers, graph retrieval tools, and report-agent tool definitions shape behavior.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: runtime traces can become retained artifacts, but their promotion boundary must be explicit.
