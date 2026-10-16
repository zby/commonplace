---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MiroShark memory: round compaction, persistent belief checkpoints, graph ingestion and selective report/profile read-back."
run-id: AAS-2026-10-15-miroshark-b3df0e053a29-01
source-identity: https://github.com/aaronjmars/MiroShark
reviewed-boundary: e95d3d8c2a2206b8b6695648e8504cf23436d3de
---

# MiroShark memory report

## Boundary and evidence

The subject and frozen SRC-1 repository are fixed by [boundary](boundary.md). This account includes simulation working context, action-derived memory, persistent belief state, document/activity graph memory, communities, persona/configuration reuse, interview context and retained report traces. It distinguishes model-readable text from symbolic control fields and dense retrieval representations. It does not assess model-provider hidden state or establish deployed retention, successful summarization, predictive validity or improved decisions. No target code, tests, providers or services were executed.

All direct reads below are implementation evidence at the reviewed commit; comments and prompts establish requests/design, not successful operation. Source quotations are from SRC-1. Supplied runtime records provide the orchestration baseline; direct reads extended it as recorded below. Available but uninspected parts remain included uncertainties, not access gaps or absences.

| Entry point / memory operation | Source paths (SRC-1) | Coverage and limits |
|---|---|---|
| Document or activity ingestion; ontology; deletion | `backend/app/storage/neo4j_storage.py`, `backend/app/services/graph_memory_updater.py`, `backend/app/services/simulation_runner.py` | Direct reads; [MEM-RTE-graph-ingestion](#mem-rte-graph-ingestion), [MEM-OBJ-episode](#mem-obj-episode), [MEM-OBJ-relation](#mem-obj-relation). Uploaded-text initialization/ontology authorship remains supplied [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population), not a full upload/parser audit. |
| Graph extraction, resolution and embeddings | `backend/app/storage/neo4j_storage.py`, `backend/app/storage/entity_resolver.py`, `backend/app/storage/ner_extractor.py` | Ingestion call site directly read; resolver/NER internals not read. Canonicalization is wired, but extraction validity and full merge semantics are not established. Encoder facts supplied by [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service). |
| Contradiction withdrawal and filtered/unfiltered reads | `backend/app/storage/contradiction_detector.py`, `backend/app/storage/search_service.py`, `backend/app/services/graph_tools.py` | Direct bounded reads; [MEM-RTE-graph-retrieval](#mem-rte-graph-retrieval). Withdrawal is consumer-specific, not universal. |
| Round compaction and system-text replacement | `backend/scripts/round_memory.py`, `backend/scripts/run_parallel_simulation.py` | Complete compactor read plus driver call-site search; [MEM-RTE-round-history](#mem-rte-round-history), part of [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds). |
| Belief initialization/update/checkpoint/resume | `backend/scripts/belief_integration.py`, `backend/wonderwall/social_agent/belief_state.py`, `backend/wonderwall/social_agent/round_analyzer.py` | Direct bounded reads; [MEM-RTE-belief-feedback](#mem-rte-belief-feedback). Analyzer fallback distribution details remain uninspected; approximate exposures cannot establish actual reading. |
| Cross-platform digest | `backend/scripts/cross_platform_digest.py` | Complete direct read; [MEM-OBJ-cross-platform-log](#mem-obj-cross-platform-log), round-route annotation. |
| Environment payload and Camel context | `backend/lib/env_compact.py`, `backend/wonderwall/social_agent/agent_environment.py`, `backend/wonderwall/social_agent/agent.py` | Complete pure compactor read; environment wiring searched, agent behavior supplied by runtime. [MEM-OBJ-agent-observation](#mem-obj-agent-observation). Camel eviction/pruning implementation is external/uninspected. |
| Single-platform and env-only alternatives | `backend/scripts/run_twitter_simulation.py`, `backend/scripts/run_reddit_simulation.py`, `backend/scripts/run_parallel_simulation.py` | Searches show dedicated Reddit belief initialization/trajectory save and dedicated scripts' reset calls; full reset/resume parity not inspected. Supplied [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual) covers env-only/interview path. Do not generalize synchronized compaction/checkpoints to all scripts. |
| Fork/counterfactual reuse | `backend/app/services/simulation_manager.py`, `backend/scripts/counterfactual_loader.py` | Fork file-copy body directly read; loader complete. Annotation on config and [RT-RTE-director-context](runtime.md#rt-rte-director-context). No full live-state clone established. |
| Community build/search/detail | `backend/app/storage/community_builder.py`, `backend/mcp_server.py` | Builder selection/write directly read, clustering algorithm not read; MCP registration/dispatch searched and supplied [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp). [MEM-RTE-community-rebuild](#mem-rte-community-rebuild). |
| Profile graph enrichment | `backend/app/services/wonderwall_profile_generator.py` | Direct query/formatting read; annotation on [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles). Remote enrichment and all generation prompts not assessed. |
| Report tools, previous-section context, saved reports and traces | `backend/app/services/report_agent.py`, `backend/app/storage/reasoning_trace.py`, `backend/app/storage/neo4j_storage.py` | Direct bounded reads/searches; report-route annotation, [MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace). Raw action/report wiring also supplied by [RT-RTE-report-sections](runtime.md#rt-rte-report-sections). |
| CLI, HTTP/browser consumers, optional external-tool results | `backend/cli.py`, `backend/app/api/graph.py`, `backend/app/api/simulation.py`, `backend/mcp_server.py` | CLI dispatch, graph endpoints, trajectory/quality/export API references searched. Optional external-tool pending-result delivery supplied by [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp). Full browser/export/publication/cache invalidation and external payload provenance remain uninspected; no complete downstream-erasure claim. |
| Evaluators and hooks | `backend/tests/`, `backend/tests/test_unit_agent_env_compaction.py` | Scoped search finds compaction byte-saving assertions and many trajectory analytics tests. Not run; no observed semantic-preservation evidence. No separate memory-maintenance hook was established by the inspected dispatch paths; this is not a repository-wide absence finding. |
| Market/media feedback | `backend/scripts/run_parallel_simulation.py`, `backend/scripts/market_media_bridge.py` | Driver references show sentiment update/social-summary injection; bridge implementation not read. Included unresolved numerical/text transforms prevent a complete account of cross-market authority. |

## Core ideas

1. Memory is layered rather than one store: raw actions, lossy round narratives, numeric belief checkpoints, graph relations and report traces have different consumers and lifetimes. Raw persistence does not establish restoration of a model's prior context ([MEM-RTE-round-history](#mem-rte-round-history), [MEM-RTE-belief-feedback](#mem-rte-belief-feedback)).
2. The synchronized driver pushes code-selected history into system text. It does not ask each agent to retrieve its own relevant history. The cross-platform digest is agent-targeted; the common round history is not ([MEM-OBJ-cross-platform-log](#mem-obj-cross-platform-log), annotation on [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)).
3. Graph labels describe provenance categories, not verified truth. Activity batching assigns one kind to a whole batch; report/profile adapters can remove the kind and lineage before a model sees the text. Default edge search excludes invalidated relations, but unfiltered fallback reads can bring them back ([MEM-RTE-graph-ingestion](#mem-rte-graph-ingestion), [MEM-RTE-graph-retrieval](#mem-rte-graph-retrieval)).
4. Report reasoning retention is an inspection surface, not demonstrated automatic learning. Stored thoughts are emitted report-loop content, not inspectable provider-internal reasoning; observation retention is truncated ([MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-episode
Label: Episode source text

Identity: Neo4j `Episode.data` created by `add_text`. Form: natural-language source or activity description; substrate: Episode node with UUID, graph ID, processed flag and creation time. Unlike the extracted relation, it retains the submitted text. Document originals and action JSON are upstream sources; an activity episode is already a rendered/combined derivative, not raw action I/O. SRC-1, `backend/app/storage/neo4j_storage.py`, `backend/app/services/graph_memory_updater.py`. No exact operative-object counterpart in runtime; closest is its ingestion route [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population).

> CREATE (ep:Episode {
>     uuid: $uuid,
>     graph_id: $graph_id,
>     data: $data,
>     processed: true,
>     created_at: $created_at
> })
> --- `backend/app/storage/neo4j_storage.py`

Relation episode IDs support lineage storage. The inspected hybrid search returns entities/relations, not episode data; persistence of the text does not establish later model access to the original reasons. Explicit graph deletion matches graph-ID nodes and detaches/deletes them; file copies and external caches have independent lifetimes.

#### MEM-OBJ-relation
Label: Relation text and provenance fields

Identity: `RELATION.fact` and associated UUID/endpoints, episode IDs, `kind`, `source_type`, `source_id` and temporal fields. Text form: natural language interpreted by later models. Metadata form: symbolic keys used by filters and navigation. Dense `fact_embedding` is a separate retrieval representation generated from fact text, not itself a readable justification. Substrate: Neo4j relationships. Entity summaries/attributes and embeddings are related node material, not identical relations. SRC-1, `backend/app/storage/neo4j_storage.py`. Closest supplied references are [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory) and [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service); neither declares this retained object.

> episode_ids: [r.episode_id],
> created_at: $now,
> valid_at: $valid_at,
> invalid_at: null,
> expired_at: null,
> kind: $kind,
> source_type: $source_type,
> source_id: $source_id
> --- `backend/app/storage/neo4j_storage.py`

Extraction/embedding plus entity resolution produce this derived memory. Existing entity merges retain nonempty summary text while updating attributes and embeddings; thus even text and vector lineage can diverge. Consumer authority and withdrawal differ by adapter in [MEM-RTE-graph-retrieval](#mem-rte-graph-retrieval).

#### MEM-OBJ-round-memory
Label: RoundMemory retained narratives

Identity: `RoundMemory._rounds`, each `RoundRecord.platform_actions`/`compacted_summary`, and `_ancient_summary`. Substrate: process-resident Python dictionaries/strings, with selected text copied into agent system messages. Action dictionaries are symbolic trace data carrying natural-language content. Summaries are natural-language derived memory; round IDs/time labels are symbolic selection metadata. This is a material state part of the broader synchronized route, not an alternative identity for that route.

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

SRC-1, `backend/scripts/round_memory.py`. Retention reaches later invocations within the resident run. No compactor serialization/reload path is established by this class, unlike persistent belief checkpoints. Batched history removes original resident records:

> # Free memory for batched rounds
> for rnum in to_batch:
>     del self._rounds[rnum]
> --- `backend/scripts/round_memory.py`

Raw database/log retention is separate; the injected history is not a live pointer to it. Summaries are asked to preserve names/arguments but no separate justification ledger or summary-faithfulness check is retained here.

#### MEM-OBJ-belief-state
Label: BeliefState and checkpoint content

Identity: per-agent `BeliefState.positions`, `confidence`, `trust`, exposure-history hashes, serialized `belief_states_<platform>.json`, and its rendered stance section. Form: symbolic topic-keyed numerical state with fixed update rules, not distributed model weights; rendered labels become natural language at the agent consumer. Substrate: Python objects, JSON files and system text. Derived trajectory snapshots are a separate analytical record generated from these updates. SRC-1, `backend/wonderwall/social_agent/belief_state.py`, `backend/scripts/belief_integration.py`. Material state part of [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds), not a duplicate of model parameters.

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

> return cls(
>     positions=data.get("positions", {}),
>     confidence=data.get("confidence", {}),
>     trust={int(k): v for k, v in data.get("trust", {}).items()},
>     exposure_history=set(),  # not persisted for size
> )
> --- `backend/wonderwall/social_agent/belief_state.py`

Checkpoint restoration preserves stance/confidence/trust but not novelty history. Checkpoints therefore do not restore behaviorally identical exposure weighting. `exposure_count` is a count, not the omitted content hashes or reasons for a stance. Later model text names stance/confidence and up to five high-trust and five low-trust users, not the raw supporting posts.

#### MEM-OBJ-cross-platform-log
Label: CrossPlatformLog targeted activity memory

Identity: `_log[platform][agent_id]` with action types/arguments. Substrate: bounded in-process dictionaries/lists and rendered system-message digests. Form: symbolic selection keys plus natural-language activity descriptions. Trace origin: simulation actions, filtered to exclude idle/search/refresh noise; automatic admission and trimming, not per-action human approval. SRC-1, `backend/scripts/cross_platform_digest.py`. Material part of [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds).

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

> # Trim to keep memory bounded
> if len(bucket) > self.max_actions_per_agent:
>     del bucket[:-self.max_actions_per_agent]
> --- `backend/scripts/cross_platform_digest.py`

Defaults keep fifteen entries per agent/platform and deliver five per other platform with content previews at 200 characters. Agent ID and excluded current platform actually select retained parts; they are not merely file identifiers. No persistence method is established in the completely read class. Its marker replacement truncates everything after the old marker, unlike the round-memory helper's preservation of a following section. Actual section survival depends on injection order.

#### MEM-OBJ-agent-observation
Label: Compacted environment observation payload

Identity: output of `_compact_posts_for_agent`/`_compact_post_for_agent` and its environment-message display. Substrate: transient dictionaries/JSON then model conversation context. Form: symbolic IDs/counts/relative time plus natural-language posts/comments. This is working-context selection, not by itself a durable learned result. Closest supplied route is [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds); unlike round memory this filters the current environment before accumulation. SRC-1, `backend/lib/env_compact.py`, `backend/wonderwall/social_agent/agent_environment.py`.

> kept = sorted(cmts, key=_comment_score, reverse=True)[:_MAX_COMMENTS_PER_POST]
> out['comments'] = [_compact_comment(c) for c in kept]
> if total > len(kept):
>     out['comments_total'] = total
> --- `backend/lib/env_compact.py`

The default comment cap is three. Zero-valued engagement fields are omitted and timestamps made relative to the most recent available post. A count survives omitted comments, not their text or a reloadable reference. The source's semantic-equivalence/cost claims are attributed, not established by these field transformations or a successful byte-size assertion.

#### MEM-OBJ-community
Label: Community summaries and membership

Identity: `Community.title`, `summary`, `summary_embedding`, `member_count` and `MEMBER_OF` links. Substrate: Neo4j nodes/edges. Natural-language summaries, symbolic membership/UUIDs and dense retrieval vectors have distinct roles. Lineage: selected entity graph clusters → capped entity-description prompt → generated or fallback summary → embedding. SRC-1, `backend/app/storage/community_builder.py`. This is a retained part of [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp), which names the broader stdio consumer, not this object.

Part of: [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp)

> MAX_MEMBERS_IN_PROMPT = 15
> blocks = []
> for i, members in enumerate(clusters, start=1):
>     lines = [f"Community {i} ({len(members)} entities):"]
>     sample = members[:MAX_MEMBERS_IN_PROMPT]
> --- `backend/app/storage/community_builder.py`

Only the first fifteen descriptions (each summary preview capped at 100 characters) shape a cluster's generated wording; all kept members can still have membership links. Summary/title are capped at 600/120 characters. The summary is not evidence that every member's content reached the model.

#### MEM-OBJ-reasoning-trace
Label: Report reasoning trace inspection record

Identity: `Report`, `ReportSection`, ordered `ReasoningStep` records from `ReasoningTraceRecorder`. Substrate: per-section memory buffer flushed to Neo4j. Text content is emitted thought/observation/conclusion prose; tool names, arguments JSON, iteration/index/timestamps and linkage are symbolic trace/navigation metadata. This is not opaque provider reasoning made readable. SRC-1, `backend/app/storage/reasoning_trace.py`, `backend/app/storage/neo4j_storage.py`. Material output part of [RT-RTE-report-sections](runtime.md#rt-rte-report-sections).

Part of: [RT-RTE-report-sections](runtime.md#rt-rte-report-sections)

> MAX_LEN = 6000
> if len(content) > MAX_LEN:
>     content = content[:MAX_LEN] + f"\n...[{len(content) - MAX_LEN} more chars truncated]"
> self._append("observation", content, iteration=iteration)
> --- `backend/app/storage/reasoning_trace.py`

Finalization records a conclusion and flushes; recording outside a section drops the step. Storage returns ordered steps/final text by section UUID; [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp) exposes actual request/response wiring to external clients. External interpretation is afforded; deployed use and a later report-generator consumption of prior traces are not established. File-report deletion is not graph-trace deletion.

### Routes

#### MEM-RTE-round-history
Label: Trace compaction to later round history

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

Owner: parallel driver and RoundMemory. Trigger: successful platform postprocessing records fetched actions; at round end compactor targets N-2; before later actions the driver builds/injects history. Raw action dictionaries → filtered text (180-character content previews and skipped low-signal actions) → model two-to-three-sentence summary or counts → ancient merged narrative → later SocialAgent system text. SRC-1, `backend/scripts/round_memory.py`, `backend/scripts/run_parallel_simulation.py`.

Code selects rounds and admits model output directly. The historian prompt requests arguments, trades, opinion shifts and named actors; it is not an expected-answer oracle or content-verification gate. Open simulation mode, no per-summary human approval. Exceptions select fallback counts; ancient summaries can be replaced/deleted from the resident store without a content-directed veto or semantic rollback. Guidance is static; summary text persists within this object/run.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted context string; compaction submission can return before the worker completes.
- Later read-back: later active-agent invocations receive recent rendered actions, older summaries/counts and an ancient narrative copied into system text.
- Delegated visibility: shared rendered history across platforms, not complete raw events, omitted searches or model-internal reasoning.
- Selection predicate: code selects older rounds, previous round detail and any available current-round actions; the synchronized driver builds before concurrent platform steps, so it does not establish same-round sequential awareness.
- Invalidation or expiry: marker replacement removes previous injected history; ancient batching deletes corresponding resident records; process recreation has no demonstrated RoundMemory restoration.
- Activation or effect: delivery instructs agents to use history; actual compliance, summary accuracy and benefit are unobserved.
- Evidence limits: the method's sequential usage docstring is not the synchronized driver's actual order; pending work can yield counts rather than prose, and raw logs surviving do not restore omitted context automatically.

> target = current_round - 2
> if target < 0:
>     return
> --- `backend/scripts/round_memory.py`

> summary = self.llm.chat(messages=messages, temperature=0.3)
> rec.compacted_summary = summary.strip()
> --- `backend/scripts/round_memory.py`

Single-round compaction uses a one-worker executor. Ancient batch compaction is called synchronously and can make its own LLM call in the round path; do not treat all compaction as nonblocking. Fallback concatenation on a failed ancient merge uses the selected individual summaries, not necessarily the prior ancient text, so preservation of all old narrative is not guaranteed.

#### MEM-RTE-belief-feedback
Label: Action exposure to checkpointed stance feedback

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

Owner: BeliefTracker/RoundAnalyzer/BeliefState. Initialization derives topics from requirement and state from configuration, then loads matching checkpoint IDs. After rounds, explicit interaction actions update trust; analyzer reads SQLite recommendation/engagement data, falling back to action-derived exposure when recommendation coverage is under 0.5. Fixed sentiment/topic/novelty/trust/social-proof/confidence rules update stance and confidence. Prompt labels plus feedback reach active agents; checkpoints and per-platform/merged trajectories are saved. SRC-1, `backend/scripts/belief_integration.py`, `backend/wonderwall/social_agent/belief_state.py`, `backend/wonderwall/social_agent/round_analyzer.py`.

This is automatic trace-fed behavior-shaping revision, not a model proving beliefs true. Software computes/adopts the update and model interpretation handles later action guidance. Starting the simulation is not human per-belief approval; configuration authorship is mixed/unspecified at this layer. No reference-outcome oracle or independent quality-based rejection appears in the inspected update. Invalid/missing checkpoint reads retain defaults; saving is best effort. Recovery restores only serialized fields; no semantic undo of actions follows. Open simulation mode, not controlled evaluation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: round snapshot, mutable belief updates and injected feedback; disk saves may fail without stopping simulation.
- Later read-back: subsequent agent invocations receive rendered beliefs; a new BeliefTracker reloads matching checkpoint agents; report analyze_trajectory reads merged trajectory.json.
- Delegated visibility: agent gets labeled stance/confidence and selected trust users, not the complete posts, algorithm inputs or a retained chain of reasons.
- Selection predicate: active IDs and topic matching for updates; recommendation exposure or action fallback; checkpoint restoration only for IDs initialized from config; report caller selects simulation/focus.
- Invalidation or expiry: checkpoints overwrite per-platform files using temporary-file replacement; exposure hashes are not restored; merged trajectories regenerate from available per-platform files and collisions are last-write-wins.
- Activation or effect: numerical state changes and prompt supply are wired; neither actual agent dependence nor improved future capacity is observed.
- Evidence limits: approximate posts/engagement and synthesized exposure cannot certify what an agent actually read; resume stance is not full conversation/history restoration, and new tracker trajectory starts empty before saving.

> # Social pushback: decrease confidence (not position)
> drop = min(0.15, (dislikes_received - likes_received) * 0.03)
> self.confidence[topic] = max(0.1, current_conf - drop)
> --- `backend/wonderwall/social_agent/belief_state.py`

> if aid in self.belief_states:
>     self.belief_states[aid] = BeliefState.from_dict(bs_dict)
> --- `backend/scripts/belief_integration.py`

This numeric feedback has no retained formulated criticism naming a challenged proposition and allocating blame. Its existence should not be erased merely because learning benefit or model-internal deliberation is unknown. Checkpoint content retains values and counts, not the reasons that produced them.

#### MEM-RTE-graph-ingestion
Label: Document and activity admission to graph memory

Owner: graph build/storage; optional runner monitor/updater for simulation actions. Caller text/ontology and automatically rendered activity batches enter `add_text`; NER extracts entities/relations, embeddings supply retrieval vectors, resolver folds names, storage merges nodes and creates relations. It retains episode text and lineage metadata. This is distinct from the population preparation consumer in [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) and the claim [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory); it spans both document admission and optional trace-fed graph updates rather than replacing either supplied record. SRC-1, `backend/app/storage/neo4j_storage.py`, `backend/app/services/graph_memory_updater.py`, `backend/app/services/simulation_runner.py`.

Optional feature enablement admits the updater, not each assertion. The monitor forwards action log records without an inspected success-only admission gate; updater excludes event records/DO_NOTHING, batches five by platform and labels the whole batch belief only when all actions are expressive, observation otherwise. Models propose extraction and contradiction verdicts; software saves them without a human per-relation approval. Ontology guides extraction, but caller/ontology initialization control is not fully established here. The kind enum check rejects invalid categories, not false propositions. Updater retries three times and then increments failure count; partial graph writes/retries have no established global rollback. Open ingestion mode; no expected-answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: add_text returns an episode UUID; optional updater queues activity and records batch success/failure counts.
- Later read-back: graph search feeds profile/report tools and MCP consumers; optional action-derived graph material can enter the same routes as document material.
- Delegated visibility: downstream adapters can supply selected fact/summary text without kind, source IDs or episode originals.
- Selection predicate: enabled updater, filtered activity and batch-level classification; NER result endpoints must resolve to created/merged entities for relation creation.
- Invalidation or expiry: ingestion can invalidate older same-endpoint relations before new relations are created; delete_graph removes graph-ID nodes/relationships, not independently retained simulation/report files.
- Activation or effect: trace-fed derived graph state is wired to later retrieval, not proof that every action reaches the graph or changes a later model decision.
- Evidence limits: generated statements are not ground truth by virtue of default fact kind; mixed batch labels, platform/round-only source IDs and partial-write retries prevent assertion of precise per-agent/per-run provenance or exactly-once persistence.

> edge_kind = (
>     "belief"
>     if all(a.action_type in expressive_actions for a in activities)
>     else "observation"
> )
> --- `backend/app/services/graph_memory_updater.py`

> if ex.get("fact") == new_rel.get("fact"):
>     continue
> --- `backend/app/storage/contradiction_detector.py`

The latter only skips contradiction comparison of exact replays; relation creation still uses CREATE. It is not ingestion deduplication. Contradiction selection is bounded to existing same-endpoint valid edges, at most five per pair/thirty comparisons; only verdict `contradicts` triggers invalidation. Model failure defaults to no invalidation. Verdict reasons are not retained by this detector; the older text/timestamps survive for historical retrieval.

#### MEM-RTE-graph-retrieval
Label: Selective graph read-back and withdrawal boundaries

Owner: SearchService, GraphTools, profile generator and MCP adapter. Request graph/query/scope → embed → vector/keyword/optional traversal candidates → score fusion/optional reranker → limited records → adapter formatting → model context or external MCP result. Retrieval components are already [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service) and [RT-CMP-reranker-service](runtime.md#rt-cmp-reranker-service), not new components here. This route describes shared inner retrieval and profile/report consumption, overlapping but not identical to the stdio-only [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp). SRC-1, `backend/app/storage/search_service.py`, `backend/app/services/graph_tools.py`, `backend/app/services/wonderwall_profile_generator.py`, `backend/app/storage/neo4j_storage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: limited entities/relations or formatted SearchResult; MCP serializes with embeddings removed.
- Later read-back: previously ingested/updated graph content reaches persona generation and report invocations; external MCP clients can explicitly request it.
- Delegated visibility: report search flattens relation text into facts and drops kind/source/temporal fields; profile context takes at most twenty fact strings and ten node-summary strings from queries requesting thirty edges/twenty nodes.
- Selection predicate: query semantics, graph namespace, scope, limits and retrieval scores; edge temporal/kind filters when supplied; profile queries target entity name, while MCP caller supplies query/IDs.
- Invalidation or expiry: default hybrid edge search excludes invalid_at relations; as_of/include_invalidated can reopen historical content. Node vector/BM25 hits do not inherit edge kind/time filtering. GraphTools fallback reads all edges without those filters.
- Activation or effect: delivered prose can shape generated personas/report answers; retrieval success is not observed model uptake or truth enforcement.
- Evidence limits: no universal withdrawal or trusted-fact-only conclusion; uninspected graph-tool panorama/insight formatting may have further transformations and external clients may cache prior results.

> _EDGE_KIND_FILTER = "($kinds IS NULL OR r.kind IN $kinds)"
> --- `backend/app/storage/search_service.py`

> all_edges = self.storage.get_all_edges(graph_id)
> scored_edges = []
> for edge in all_edges:
>     score = match_score(edge.get("fact", "")) + match_score(edge.get("name", ""))
> --- `backend/app/services/graph_tools.py`

`get_all_edges` matches graph relations without an invalidation predicate. Thus the failure fallback is a source-supported counterexample to treating edge invalidation as universal exclusion. Retrieval read-back is requested selection, not an independently unsolicited graph push. Metadata survives in storage but does not automatically reach the interpretation consumer.

#### MEM-RTE-community-rebuild
Label: Cluster summary construction and requested browsing

Part of: [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp)

Owner: CommunityBuilder/storage and MCP browse adapter. Missing-community browse or explicit storage operation triggers graph clustering, min-size/max-count selection, generated/fallback labels, embedding and replacement. Requested browsing then lists largest clusters or query hits; detail expands retained member links. SRC-1, `backend/app/storage/community_builder.py`, `backend/app/storage/neo4j_storage.py`, supplied [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp).

Code decides membership and truncation; model proposes summary text and software admits it, with generic fallback text when generation fails. No per-community human approval, truth oracle or quality rejection is established. Caller-requested graph overview is the mode; summary instructions describe relationships, not a controlled test. Existing community nodes are deleted before writes in separate helper sessions despite the nearby transaction comment; no atomic replacement/rollback guarantee is justified. Small-graph early return differs from the no-kept-cluster branch that deletes old communities.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rebuild statistics or requested community metadata/detail/semantic search results.
- Later read-back: persisted generated overview reaches subsequent MCP browse/search/detail requests and graph-tool community lookup.
- Delegated visibility: cluster label/summary and optional member entities, not all original evidence or complete summarization inputs.
- Selection predicate: graph namespace, clustering/minimum size/maximum count; first fifteen member descriptions for wording; external query or limited largest-first slice for delivery.
- Invalidation or expiry: explicit rebuild replaces old community nodes; missing-only auto-build does not establish automatic refresh after every graph mutation or relation invalidation.
- Activation or effect: retained overview is available to external clients/report graph tools; actual interpretation and benefits are unobserved.
- Evidence limits: clustering internals not read; stale derived summaries and separate delete/write calls prevent freshness and all-or-nothing rebuild conclusions.

> # Replace in one transaction
> self._delete_existing(graph_id)
> self._write(graph_id, kept, labels, embeddings)
> --- `backend/app/storage/community_builder.py`

The comment is not an enforcement guarantee: `_delete_existing` and `_write` each open their own session and call session.run. This checks the stronger source label against its implementation rather than adopting it.

### Claims

#### MEM-CLM-observation-equivalence
Label: Claimed semantic equivalence of observation compaction

SRC-1, `backend/lib/env_compact.py`, claims the wire-format changes do not alter what the agent semantically sees and reports token/cost benefits without supplied run artifacts. This is distinct from [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory), which concerns graph retention. The implementation actually omits lower-ranked comment text; equivalence is not guaranteed by a byte-size test. [MEM-OBJ-agent-observation](#mem-obj-agent-observation) identifies the actual retained part.

> changes here that don't change what the agent semantically sees:
> --- `backend/lib/env_compact.py`

- claim conclusion status: claimed
- operation conclusion status: uninspected

The comment's attributed percentages do not constitute observed-run or causal-experiment evidence in this run.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

Memory-specific parts are [MEM-OBJ-round-memory](#mem-obj-round-memory), [MEM-OBJ-belief-state](#mem-obj-belief-state), [MEM-OBJ-cross-platform-log](#mem-obj-cross-platform-log) and [MEM-OBJ-agent-observation](#mem-obj-agent-observation). Driver scheduling selects active IDs and injects available common history plus per-agent beliefs and other-platform digests. These are automatic pushes triggered by round scheduling, not foreground tool requests. Cross-platform log uses agent/platform/tail limits; RoundMemory uses time/age, not query relevance. Marker replacement keeps windows bounded by replacing sections but offers no global token-budget invariant. SRC-1, `backend/scripts/run_parallel_simulation.py`, `backend/scripts/round_memory.py`, `backend/scripts/cross_platform_digest.py`.

Supplied Camel tool-pruning configuration in the runtime passage is a host request; its precise retained conversation and token eviction remain external. It does not prove removal of ordinary environment messages. State and summary updates establish trace-fed future context, not improved capacity.

#### On [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles)

Graph enrichment is requested using an entity-name query. It retrieves up to thirty relations and twenty nodes, deduplicates text into sets, then formats at most twenty facts and ten summary/related-name strings. Kind/source/time metadata do not accompany those strings. SRC-1, `backend/app/services/wonderwall_profile_generator.py`.

> if results["facts"]:
>     context_parts.append("Fact Information:\n" + "\n".join(f"- {f}" for f in results["facts"][:20]))
> --- `backend/app/services/wonderwall_profile_generator.py`

This enriches the profile-generation context; it does not mean later simulation agents have graph access. File personas persist across starts/forks and enter model system messages as described by the supplied record. No independent human approval of each retrieved or generated statement is established.

#### On [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config)

Forking copies three platform profile files and rewrites configuration with a new simulation ID/optional requirement; it retains the parent graph ID in new state. The inspected copy list is not a clone of platform databases, belief checkpoints, RoundMemory or Camel conversations. SRC-1, `backend/app/services/simulation_manager.py`.

> files_to_copy = [
>     "reddit_profiles.json",
>     "twitter_profiles.csv",
>     "polymarket_profiles.json",
> ]
> --- `backend/app/services/simulation_manager.py`

Thus reusable persona/configuration lineage differs from accumulated experience restoration. The config reasoning field is descriptive provenance, not automatic execution of its reasons. Counterfactual loader text is a later-read file instruction with round trigger; caller-provided scenario content is not trace learning (SRC-1, `backend/scripts/counterfactual_loader.py`, [RT-RTE-director-context](runtime.md#rt-rte-director-context)).

#### On [RT-RTE-report-sections](runtime.md#rt-rte-report-sections)

Storage/read-back includes file report metadata/Markdown plus optional [MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace). Tool observations derive from graph queries, interview responses, action logs and trajectories, not necessarily raw source documents. Direct SRC-1 reads/searches of `backend/app/services/report_agent.py` show trajectory loading and separate section-local messages. Previous-section excerpts target a nominal 6000-character total using max(400, total/section count); this is not a strict cap for many sections or separators. Parallel sections explicitly receive no previous sections.

> previous_sections=[],  # parallel: sections don't see each other
> --- `backend/app/services/report_agent.py`

This isolates section frames: selected inputs enter; returned prose escapes; complete sibling message histories do not. Frame isolation is a useful stack analogy, but a graph/file ID is not an automatically followed pointer into model context. Trace retention exposes reasons to explicit MCP inspection; no inspected automatic prior-trace-to-next-report learning route follows. `delete_report` removes the report folder/legacy files, not Neo4j report nodes or reasoning steps.

> if os.path.exists(folder_path) and os.path.isdir(folder_path):
>     shutil.rmtree(folder_path)
>     logger.info(f"Report folder deleted: {report_id}")
>     return True
> --- `backend/app/services/report_agent.py`

#### On [RT-BAP-agent-context](runtime.md#rt-bap-agent-context)

Derived history and stance inherit model-interpreted behavioral authority at this consumer, not factual or deterministic control. Round history says to use it for decisions. Belief text says to guide rather than rigidly dictate actions; it does not deliver underlying update reasons. SRC-1, `backend/scripts/round_memory.py`, `backend/wonderwall/social_agent/belief_state.py`.

> "These reflect your evolving understanding based on what you've "
> "observed and experienced. Let them guide (but not rigidly dictate) "
> "your actions."
> --- `backend/wonderwall/social_agent/belief_state.py`

The wording can present heuristic stance updates as experienced understanding; delivered text is evidence of the request, not observed dependence, learning benefit or a truthful account of actual exposure.

## Write side

Admission mechanisms are distinct from physical writes. [MEM-RTE-graph-ingestion](#mem-rte-graph-ingestion) accepts caller documents or automatically rendered simulation activity, then software/model extraction determines derived content. [MEM-RTE-round-history](#mem-rte-round-history) admits historian output or counts without per-summary approval. [MEM-RTE-belief-feedback](#mem-rte-belief-feedback) admits fixed-rule changes derived from recommendations/actions/engagement. [MEM-RTE-community-rebuild](#mem-rte-community-rebuild) admits size-filtered clusters and generated/fallback labels. These mechanisms persist different results and do not share one truth gate.

The raw-to-derived chains are explicit: action records → RoundMemory rendering → compacted narrative → later system section; platform exposure/actions → numeric stance/trust/confidence → checkpoint/label → later agent; activity log → combined episode → extracted graph → later profile/report retrieval. Trajectory JSON is derived analytical state, not a transcript of the agent's reasoning. Model-produced profiles/reports are admitted under the supplied preparation/report routes. The initiation of those workflows does not establish human approval of every content unit.

Maintenance includes old-round deletion, action-tail eviction, field/comment filtering, checkpoint overwrite, community replacement and graph invalidation. Failure alternatives keep counts, defaults or generic summaries rather than verified content. Contradiction handling withdraws specific old relations but retains temporal audit content; graph-wide deletion and file-report deletion reach different substrates. Rejection is primarily syntactic/exception-based in these inspected paths, not demonstrated semantic falsification. Persistent rationale is strongest in optional report traces, but even there observations can be truncated and the later reader is an explicit inspection client. Round/belief summaries do not automatically carry their raw reasons back to agents.

## Read-back

- **Automatic round pushes:** common history and per-agent stance/digests are selected by code at round activation and copied into system text. Budgets are round-age policies, entry/preview caps and replacement markers, not a unified token budget. See [MEM-RTE-round-history](#mem-rte-round-history), [MEM-RTE-belief-feedback](#mem-rte-belief-feedback) and round-route annotation.
- **Requested graph retrieval:** caller/model supplies query, scope and limit; storage selects scored retained relations/entities; adapters decide which text and metadata reach profile/report models. [MEM-RTE-graph-retrieval](#mem-rte-graph-retrieval) retains default-filter, node-search and fallback distinctions. A lower-level search API alone would not establish this route; inspected profile/report callers do.
- **Requested overview/trace inspection:** [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp) delivers retained community/report/section content to an external MCP client. [MEM-RTE-community-rebuild](#mem-rte-community-rebuild) separates automatic build on a missing overview from requested delivery. Neither proves a deployed client's interpretation.
- **Reload and interview:** saved persona/config files and belief checkpoints can enter a new process through separate paths. Env-only interview recreation is not full RoundMemory/Camel restoration. Supplied [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual) carries the interview memory/channel details; its optional conversation recording must not be conflated with every interview updating durable reasoning memory.
- **Optional tool returns:** [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp) retains pending results per agent and pops them on later activation. These are external tool observations, not graph-derived memory by default. Complete payload lineage/remote retention is uninspected.

The decisive authority is the actual consumer: graph kind metadata guides filters only where forwarded; natural-language facts or stance labels influence models through interpretation; numeric belief rules determine updates in code. Storage does not confer universal trust, instruction priority, complete access or demonstrated uptake.

## Integration issues

1. **Refinement, not contradiction of runtime's resident-context limit:** [MEM-RTE-belief-feedback](#mem-rte-belief-feedback) establishes persisted belief-state reload, while [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual) correctly declines full in-memory restoration. Reconciliation should preserve both; exposure history is omitted and resident round narratives are separate.
2. **Nonblocking compaction qualification:** [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds) describes background compaction. [MEM-RTE-round-history](#mem-rte-round-history) distinguishes background single-round work from synchronous ancient merge. The claim must not expand into an all-compaction nonblocking guarantee.
3. **Graph memory is optional and lossy:** [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory) is a source claim, not full retention. [MEM-RTE-graph-ingestion](#mem-rte-graph-ingestion) adds batch-level kind, skipped actions, no success-only monitor gate and limited source IDs. Per-action/per-run provenance and exactly-once ingestion remain unestablished.
4. **Withdrawal does not propagate uniformly:** [MEM-RTE-graph-retrieval](#mem-rte-graph-retrieval) includes unfiltered fallback and node hits; [MEM-RTE-community-rebuild](#mem-rte-community-rebuild) includes missing-only refresh. There is no established cascade from invalidated relation to profile/report copies or cached summaries. File-report deletion also leaves graph trace state outside its inspected deletion scope ([MEM-OBJ-reasoning-trace](#mem-obj-reasoning-trace)).
5. **Source comment corrections:** [MEM-RTE-community-rebuild](#mem-rte-community-rebuild) rejects the stronger same-transaction comment from separate-session helpers. [MEM-CLM-observation-equivalence](#mem-clm-observation-equivalence) retains a semantic-equivalence claim as claimed despite omitted comments; attributed performance is not observed evidence.
6. **Overlaps/identity:** all declared Part of relations identify distinct state/operation pieces of supplied routes. [MEM-RTE-graph-retrieval](#mem-rte-graph-retrieval) overlaps [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp) in storage calls but adds profile/report consumers; it is not a substitute identity. [MEM-RTE-graph-ingestion](#mem-rte-graph-ingestion) overlaps preparation's upstream input, not its population-generation endpoint. No candidate whole-record duplicate was found after comparison with the supplied runtime.
7. **Included unresolved mechanisms:** market/media bridge transformations; complete dedicated-script reset/resume behavior; complete extraction/resolution internals; initialization approval/ontology control; graph-tool panorama/insight transformations; browser/export/cache withdrawal and all auxiliary publishing consumers remain uninspected as localized in the coverage table. They prevent claims of exhaustive context/recovery/erasure or uniform source trust, not the positive routes already established. No other analyst reports were supplied, so possible future epistemic/workflow overlaps remain for reconciliation rather than guessed citations.

## Limitations and checks

The reviewed checkout HEAD was rechecked as e95d3d8c2a2206b8b6695648e8504cf23436d3de. Supplied run/source/boundary identities are retained exactly. The full invocation, member types, boundary/runtime inputs, collection, worker rules and record contract were read, recovering bounded-range continuations. No prior analysis or other attempt state was consulted; writes are confined to assigned output/identity paths. Analysis-method identity is the supplied instruction/type/record files; no separate method-commit was supplied to this worker.

Consequential counterexamples checked include synchronous ancient compaction, incomplete checkpoint restoration, unfiltered fallback retrieval, loss of provenance in adapters, nontransactional community replacement and semantically omitted comments. No observed-run or causal-experiment layer exists. Uninspected dependency and included auxiliary surfaces are stated above. No absent-learning or absent-theory conclusion is inferred from opaque model processing; no improved-capacity or exercised self-improvement claim is made from persistence alone.

Validation: validate-output reports “Member content check passes; invocation residue not checked.” This establishes the performed deterministic content checks, not job acceptance, claim support or successful target operation.
