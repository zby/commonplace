---
description: "Document-to-social-simulation stack with Neo4j graph extraction, cross-platform round memory, belief drift, and ReACT report traces"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# MiroShark

MiroShark, by Aaron Mars, is a document-to-simulation system that turns an uploaded scenario, document, question, or live item into a Neo4j-backed social world. It extracts entities and relationships, generates personas, runs Twitter/Reddit/Polymarket-style rounds, records action traces, updates agent beliefs, and writes analytic reports over the resulting simulation evidence. Its memory system is therefore split across document-derived graph state, simulation-derived traces, prompt-time round/belief memory, and report reasoning traces rather than one general-purpose memory store.

**Repository:** https://github.com/aaronjmars/MiroShark

**Reviewed commit:** [44d1c4e1247a76c243dee14f2bfae6efb507e83a](https://github.com/aaronjmars/MiroShark/commit/44d1c4e1247a76c243dee14f2bfae6efb507e83a)

**Last checked:** 2026-05-16

## Core Ideas

**Uploaded documents compile into a Neo4j graph, not files.** The project state layer stores uploaded files, extracted text, ontology, graph id, and simulation metadata under server-side upload directories, while durable knowledge lives mainly in Neo4j nodes and relationships rather than inspectable Markdown ([backend/app/models/project.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/models/project.py)). `GraphBuilderService` chunks text, stores ontology on the graph, and sends chunks through `GraphStorage.add_text()` in parallel ([backend/app/services/graph_builder.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/graph_builder.py)). `Neo4jStorage.add_text()` then creates an `Episode`, extracts entities and relations, embeds entity summaries and relation facts, resolves duplicate entities, invalidates contradicted edges, and creates `RELATION` edges with `valid_at`, `invalid_at`, `kind`, `source_type`, and `source_id` metadata ([backend/app/storage/neo4j_storage.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/storage/neo4j_storage.py)).

**Graph retrieval is a mixed symbolic/distributed-parametric view over one substrate.** Search combines Neo4j vector indexes, full-text indexes, graph traversal, temporal filters, epistemic-kind filters, and optional reranking ([backend/app/storage/search_service.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/storage/search_service.py)). The representational form is mixed: entity and relation records are symbolic graph state, fact text and summaries are prose, embeddings and reranker scores are distributed-parametric retrieval aids, and temporal fields are symbolic lineage controls. The community layer adds a zoom-out view by clustering valid graph edges with Leiden, asking an LLM for community titles/summaries, embedding those summaries, and writing `Community` nodes with `MEMBER_OF` edges ([backend/app/storage/community_builder.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/storage/community_builder.py)).

**Personas are generated from graph context plus optional web enrichment.** MiroShark does not merely assign random social profiles. The Wonderwall profile generator builds entity context from attributes, related edges, related nodes, hybrid graph search results, and optional web enrichment when context is thin or the entity is notable; then an LLM creates individual or institutional personas for social simulation ([backend/app/services/wonderwall_profile_generator.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/wonderwall_profile_generator.py)). Those personas become behavior-shaping system-definition artifacts inside the simulation because they are loaded into agent prompts and platform profile CSV/JSON surfaces, even though their source lineage back to exact graph edges is not preserved as a first-class citation contract.

**Simulation memory is prompt-time, sliding-window, and partly distilled.** The synchronized simulation loop injects round memory, belief state, market/media context, cross-platform digests, director events, and optional MCP results before agents act ([backend/scripts/run_parallel_simulation.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/scripts/run_parallel_simulation.py)). `RoundMemory` records platform actions by round, keeps the previous round in full detail, compacts older rounds into LLM summaries, batch-compacts ancient summaries, and injects the resulting prose into agent system messages ([backend/scripts/round_memory.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/scripts/round_memory.py)). This is a high-authority system-definition surface during a run, but the compacted round memory itself is in-process state, not a durable source-of-truth artifact.

**Belief state is durable per-simulation behavior state.** Each agent has mutable positions, confidence, trust, and exposure history. Beliefs update heuristically from seen posts, engagement, novelty, social proof, and trust, then render into a prompt section that tells the agent what it currently believes ([backend/wonderwall/social_agent/belief_state.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/wonderwall/social_agent/belief_state.py)). `BeliefTracker` initializes beliefs from generated config, restores saved belief files, updates after each round, writes per-platform and merged trajectories, and persists `belief_states_<platform>.json` so pause/resume and branches keep accumulated stance rather than resetting to profile defaults ([backend/scripts/belief_integration.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/scripts/belief_integration.py)). These belief files and trajectories are not just evidence; when reinjected, they directly steer later agent actions.

**Reports use traces as evidence and record their own reasoning trace.** The report agent is a ReACT-style analyst over graph tools, simulation feeds, market state, belief trajectories, and report-specific tools ([backend/app/services/report_agent.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/report_agent.py)). It also persists report reasoning as `Report`, `ReportSection`, and `ReasoningStep` nodes in Neo4j, with step kinds for thought, tool call, observation, and conclusion ([backend/app/storage/reasoning_trace.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/storage/reasoning_trace.py)). That trace has knowledge-artifact authority for audit and later analysis, but the inspected code does not show an automated loop that promotes report-trace findings into new simulation rules.

## Comparison with Our System

| Dimension | MiroShark | Commonplace |
|---|---|---|
| Primary purpose | Generate and analyze synthetic social/market trajectories from a scenario or document | Maintain a durable methodology KB for agents and maintainers |
| Storage substrate | Upload directories, Neo4j graph, platform SQLite/log files, JSON trajectory/belief/export files, optional DKG citation files | Git-tracked Markdown, type specs, source snapshots, generated indexes, validation outputs, review artifacts |
| Representational form | Mixed graph records, prose facts/summaries/personas, JSON traces/configs, embeddings, prompt blocks, report reasoning subgraphs | Mostly prose and structured frontmatter, with symbolic links, schemas, scripts, validators, and generated indexes |
| Lineage | Stronger in raw graph edges, actions logs, trajectories, reproduce exports, and lineage endpoints; weaker in generated personas and compacted prompt memory | Source-pinned notes, archived replacements, citations, type contracts, validation, review-state lifecycle |
| Activation | Automatic prompt injection during simulation rounds; report tools query graph, feed, market, trajectory, and reasoning state | Agents activate knowledge through `rg`, indexes, links, type specs, skills, instructions, and validation/review workflows |
| Behavioral authority | Personas, belief prompts, round memory, market/media context, config, and report prompts shape behavior inside a run | Instructions, skills, schemas, validators, ADRs, and curated notes shape behavior across tasks |

MiroShark is much more dynamic than commonplace. It treats memory as a simulation substrate: source documents become graph facts; generated personas become agents; agent actions become logs, graph updates, belief trajectories, reports, exports, and sometimes further prompt context. Commonplace treats memory as a maintained library: claims become typed notes, instructions, ADRs, and indexes that later agents inspect and validate.

The most useful comparison is the artifact split. A MiroShark graph edge from an uploaded document is a knowledge artifact when retrieved as evidence or context. A graph edge produced by `GraphMemoryUpdater` from an agent post is also trace-derived evidence, with `kind="belief"` or `kind="observation"` and `source_type="agent"` ([backend/app/services/graph_memory_updater.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/graph_memory_updater.py)). A belief-state prompt, round-memory prompt, persona, simulation config, market question, or report-agent prompt is a system-definition artifact because it instructs, configures, routes, or conditions future behavior. Commonplace tries to make those authority differences explicit in artifact type contracts; MiroShark implements them operationally, but mostly as application conventions rather than inspectable review contracts.

MiroShark is stronger on live activation. Agents do not have to remember to search; the runner injects current beliefs, previous-round memory, market-media bridge context, cross-platform digests, and director events before the next action. Commonplace is stronger on durable trust. A commonplace note can say where it came from, how fresh it is, what type contract it satisfies, and which validation/review gates have checked it. MiroShark has useful lineage artifacts, especially `reproduce.json`, trajectory exports, lineage navigation, report reasoning traces, and graph temporal fields, but its generated personas and compacted summaries are less auditably tied to the source graph facts that produced them ([backend/app/services/repro_export.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/repro_export.py), [backend/app/services/lineage_service.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/lineage_service.py)).

The graph store is also a counterexample to filesystem-first assumptions. For high-volume simulation state, Neo4j plus vector/fulltext indexes make sense: multi-hop graph retrieval, temporal filters, epistemic-kind filters, contradiction invalidation, and report-trace traversal are operational queries, not authoring surfaces. The cost is that the retained knowledge is no longer easy for a coding agent to inspect, diff, review, or repair with ordinary file tools.

## Borrowable Ideas

**Separate source-derived graph facts from trace-derived simulation beliefs.** Ready to borrow as vocabulary discipline. MiroShark's `kind` and `source_type` fields show a compact way to mark whether an edge came from a document, an agent belief, or an observation, though commonplace would need stronger citation and review metadata before promoting such edges into library notes.

**Use prompt-time belief state only inside a workshop.** Worth borrowing for active simulations or multi-agent workshops, not for durable methodology notes. A mutable belief object can steer agents efficiently during a run, but it should not become a library claim without a promotion step.

**Keep reproducibility exports near shareable reports.** MiroShark's `reproduce.json`, trajectory CSV/JSONL, notebook export, and lineage API are good examples of making a generated result analyzable after the run ([backend/app/services/trajectory_export.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/trajectory_export.py), [backend/app/services/notebook_export.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/notebook_export.py)). Commonplace review bundles could borrow this posture: make the artifact that supports a conclusion exportable, stable, and independently inspectable.

**Persist reasoning traces as queryable structures, not only logs.** MiroShark's `ReportSection` and `ReasoningStep` subgraph is a stronger audit surface than a plain text report log. Commonplace semantic reviews could eventually benefit from a structured trace format, but only if it stays tied to source notes and decisions.

**Do not borrow implicit authority boundaries.** MiroShark's personas, round summaries, belief prompts, graph edges, report traces, and public exports each have different authority, but the boundaries live in code and convention. Commonplace should keep those distinctions explicit in type specs and validation rules.

## Trace-derived learning placement

**Trace source.** MiroShark qualifies as trace-derived learning, but mostly within a simulation/run rather than as cross-task self-improvement. Raw traces include platform `actions.jsonl` files, platform SQLite state, in-memory round records, per-agent action dictionaries, belief snapshots, trajectories, report-agent JSONL logs, and ReACT steps. `SimulationRunner` reads platform action logs and can pass each action into `GraphMemoryUpdater` when graph memory update is enabled ([backend/app/services/simulation_runner.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/simulation_runner.py)).

**Extraction.** There are several extraction paths. `GraphMemoryUpdater` turns agent actions into natural-language episode text, batches them, assigns an epistemic `kind`, and sends them through the same NER/embedding/Neo4j ingestion path used for documents ([backend/app/services/graph_memory_updater.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/graph_memory_updater.py)). `RoundMemory` compacts older rounds with an LLM or fallback summary ([backend/scripts/round_memory.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/scripts/round_memory.py)). `BeliefTracker` derives per-agent stance and trust changes from post exposure, engagement, and heuristic analysis ([backend/scripts/belief_integration.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/scripts/belief_integration.py)). The report agent derives analytic sections and stores its reasoning trace after tool use ([backend/app/storage/reasoning_trace.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/storage/reasoning_trace.py)).

**Storage substrate.** Source documents persist in upload directories and as document-derived Neo4j episodes/entities/edges. Raw simulation traces persist in platform action logs, platform databases, run-state JSON, trajectory JSON, and report logs. Distilled or behavior-shaping trace-derived state persists in Neo4j graph edges with `source_type="agent"`, `belief_states_<platform>.json`, `trajectory_<platform>.json`, merged `trajectory.json`, report reasoning subgraphs, and generated export artifacts.

**Representational form.** Raw logs and configs are symbolic JSON plus prose content. Graph entities and relations are symbolic records with prose fact fields and vector embeddings. Round memory is prose prompt context. Belief state is symbolic numeric state rendered into prose instructions. Report reasoning is a symbolic subgraph with prose step content. The operative behavior-shaping parts are mixed: numeric beliefs and symbolic configs are converted into instruction-bearing prompt text.

**Lineage.** Document-derived graph edges have episode ids, timestamps, source type/id, temporal validity, contradiction invalidation, and graph id. Simulation-derived graph edges keep batch-level source ids such as platform/round and epistemic kind. Belief trajectories preserve per-round snapshots, but the active belief prompt does not cite the exact posts that moved each number. Round-memory compactions are not durable canonical artifacts. Report reasoning traces keep section and step order, tool names, parameters, observations, and final text, but they do not automatically invalidate or revise the report when underlying graph state changes.

**Behavioral authority.** Raw action logs, trajectories, report traces, and graph facts are knowledge artifacts when consumed as evidence, context, explanation, or audit material. Belief prompts, round-memory prompts, personas, simulation configs, market/media bridge context, director events, and report-agent prompts are system-definition artifacts because they configure and instruct future model calls. Search scores, embeddings, and reranker outputs have ranking authority over what evidence becomes active.

**Scope.** The learning scope is primarily per-simulation and per-project. Belief state, round memory, trajectories, and action-derived graph updates shape the current run, resumed run, fork, or report. The inspected code does not show a cross-project promotion path that turns successful simulations into durable reusable policies, tests, skills, or model updates.

**Timing.** Trace capture and belief updates happen online during simulation. Round compaction is staged during the run, often in a background thread. Report reasoning traces are created during report generation. Reproducibility and lineage exports are read-only after the run.

**Survey placement.** MiroShark belongs on the trace-to-artifact and trace-to-state axes of the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey split between raw traces and behavior-shaping artifacts: action logs alone are not memory; the behavior change comes when traces are converted into graph edges, belief state, round summaries, report traces, or prompt context. It also shows a separate source-derived graph path: uploaded document facts and simulation traces share Neo4j infrastructure but have different lineage and authority.

## Takeaways

**MiroShark is graph-grounded simulation infrastructure, not a general agent KB.** Its memory is optimized for creating, running, analyzing, and reproducing simulations from source material.

**Trace-derived status applies, but needs splitting.** Source-document graph facts, simulation action traces, belief-state updates, round summaries, and report reasoning traces are different retained artifacts. Treating all of them as one "memory" would hide the design.

**The strongest behavior memory is prompt-time state.** Round memory and belief prompts influence the next round directly. Neo4j graph facts matter when retrieved, but belief and round context are injected without waiting for an agent to search.

**Lineage is uneven.** Graph edges and reproducibility exports carry useful metadata. Generated personas, belief changes, and compacted summaries are less inspectable as derived artifacts.

**The graph path is a useful database-first counterexample.** For simulation traces and multi-hop retrieval, Neo4j plus embeddings is a pragmatic substrate; for durable methodology claims, commonplace still needs files, citations, validation, and human-readable review.

## Curiosity Pass

The most interesting mechanism is not the social simulation itself but the way simulation state changes authority as it moves. A post starts as an action log row, may become a graph episode, may influence another agent's belief state, may be summarized into round memory, and may later be cited by a report. Each step changes storage substrate, representational form, lineage, and behavioral authority.

Round memory sounds more durable than it is. The compacted summaries are behavior-shaping during a live run, but the inspected `RoundMemory` object keeps them in process and frees old records after batch compaction. Durable audit lives elsewhere: action logs, trajectories, graph updates, report traces, and exports.

Belief state is intentionally heuristic. That is probably the right tradeoff for a simulation engine, because every round needs cheap, predictable state change. It would be too weak as a durable knowledge-claim mechanism without source citations and review.

The document and trace ingestion paths share Neo4j, but their epistemology differs. A document-derived edge is the system's best extraction of source material. An action-derived edge is evidence of what a simulated agent said or did. MiroShark has the fields to distinguish them; any downstream analysis has to preserve that distinction.

## Open Questions

- How often does graph-memory updating run in normal simulations, and do report agents rely on action-derived graph edges or mostly on action logs and trajectory files?
- Should generated personas carry explicit links to graph facts, web-enrichment snippets, and prompt versions so a surprising simulated behavior can be audited?
- Does round-memory compaction preserve enough detail for long simulations, or does it erase minority arguments and weak signals that later matter?
- How should conflicts between document-derived facts, agent beliefs, and report conclusions be represented in the graph?
- Can report reasoning traces be used to improve future report prompts, or are they currently audit-only?
- What quality checks determine whether a simulation result is credible rather than merely internally reproducible?

## What to Watch

- Whether graph-memory updating becomes enabled by default and starts driving report quality.
- Whether action-derived graph edges gain stronger lineage back to exact action-log rows and platform database records.
- Whether persona generation gains source citations or cached prompt/response artifacts.
- Whether belief-state updates become configurable, learned, or validated against held-out outcomes.
- Whether report traces feed a promotion loop into better report prompts, retrieval policies, or simulation diagnostics.
- Whether DKG publishing evolves from citation anchoring into a broader provenance contract for source graph, trajectory, and report artifacts ([backend/app/services/dkg_publisher.py](https://github.com/aaronjmars/MiroShark/blob/44d1c4e1247a76c243dee14f2bfae6efb507e83a/backend/app/services/dkg_publisher.py)).

## Bottom Line

MiroShark is the strongest nearby reference for graph-grounded simulation loops. It compiles source material into Neo4j, turns graph context into personas and simulation configs, updates prompt-time belief and round memory from traces, and records reports plus reasoning traces over the resulting world. Commonplace should borrow the artifact split, reproducibility exports, and trace/state vocabulary, but not the implicit authority model: source facts, simulated beliefs, prompt state, and report conclusions need separate lineage and review paths before they become durable methodology knowledge.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: MiroShark combines source-derived graph memory with simulation trace-derived graph, belief, trajectory, and report artifacts.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: MiroShark requires separate analysis of storage substrate, representational form, lineage, and behavioral authority for each retained surface.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: document facts, action logs, trajectories, and report traces advise or evidence later analysis.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: personas, round memory, belief prompts, configs, and report prompts condition future behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: MiroShark's strongest behavior change comes from automatic prompt injection, not passive storage.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares: MiroShark's run directory and simulation state are workshop-like retained state whose value is consumed during active work.
