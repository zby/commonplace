---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Graphiti memory: episode lineage, derived facts and summaries, selective read-back, and limits of withdrawal at the frozen repository boundary."
run-id: AAS-2026-10-12-graphiti-1d535ca565a4-01
source-identity: "https://github.com/getzep/graphiti"
reviewed-boundary: "964bb11d1e7020e3cc67fab244268b0736b6c219"
---

# Graphiti memory report

## Boundary and evidence

Graphiti retains caller episodes and derived graph content for later extraction and retrieval. This report includes the library, supplied/direct graph writes, service admission and retrieval, community and saga maintenance, shipped assistant instructions, the LangGraph consumer and graph-building evaluator. It follows the whole-system boundary in [boundary](boundary.md), SRC-1 at commit `964bb11d1e7020e3cc67fab244268b0736b6c219`. It does not attribute external provider weights, database durability, LangGraph internals, MCP-host compliance or proprietary Zep operation to Graphiti.

Correction-round direct reads rechecked single and bulk persistence, bulk serialization, notebook scheduling/tool-loop code and REST episode deletion. Direct source reads added object definitions, namespaces, saga selection, entity summarization, withdrawal, community construction, read formatting and example/evaluator code to the supplied runtime account. Evidence is implementation and doctrine/design only. No target, test, provider or database was executed. Historical notebook outputs are not run evidence. All source paths below belong to SRC-1; supplied-record links identify inherited evidence rather than a fresh implementation check.

| Memory operation or part | Source path and inspection basis | Coverage or unresolved fact and prevented conclusion |
|---|---|---|
| Single/bulk episode admission, raw retention, prior context | Direct: `graphiti_core/graphiti.py`, `graphiti_core/utils/bulk_utils.py`, `graphiti_core/utils/maintenance/graph_data_operations.py`; supplied runtime for full bulk resolution | [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion), [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion), [MEM-OBJ-episodic-node](#mem-obj-episodic-node). Single ingestion suppresses raw text when configured; bulk passes content unchanged at both writes even with suppression configured. Schema/source control is not truth approval; extraction equivalence of bulk variants remains uninspected. |
| Entity/fact text, lineage and vectors | Direct: `graphiti_core/nodes.py`, `graphiti_core/edges.py`, summary and temporal portions of `graphiti_core/utils/maintenance/node_operations.py` and `graphiti_core/utils/maintenance/edge_operations.py` | [MEM-OBJ-entity-node](#mem-obj-entity-node), [MEM-OBJ-entity-edge](#mem-obj-entity-edge), [MEM-OBJ-graph-metadata](#mem-obj-graph-metadata), [MEM-OBJ-graph-embeddings](#mem-obj-graph-embeddings). All prompt variants and attribute provenance are not fully traced; no universal factual-warrant claim. |
| Storage and direct mutation | Direct: `graphiti_core/namespaces/nodes.py`, Neo4j episode save/delete in `graphiti_core/driver/neo4j/operations/episode_node_ops.py`; namespace edge surface searched; supplied direct REST/triplet findings | [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes). Backend operations, query/index adapters and migration details remain partly uninspected; no backend parity, transaction or complete metadata-roundtrip guarantee. |
| REST/MCP queue admission | Supplied: `server/graph_service/routers/ingest.py`, `server/graph_service/zep_graphiti.py`, `mcp_server/src/services/queue_service.py`; direct MCP tool signatures searched | [RT-RTE-service-admission](runtime.md#rt-rte-service-admission). Process-local acceptance is not retained knowledge or durable completion. |
| Query, episode and UUID read-back; service display | Direct: `graphiti_core/graphiti.py`, `graphiti_core/search/search.py`, `graphiti_core/search/search_filters.py`, fulltext portion of `graphiti_core/search/search_utils.py`, `server/graph_service/routers/retrieve.py`, MCP tools and `mcp_server/src/utils/formatting.py` | [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval), [MEM-CLM-display-lineage](#mem-clm-display-lineage). Date filters and raw episode retrieval differ from semantic selection; all search/backend combinations uninspected. |
| Community derivation and incremental maintenance | Direct: `graphiti_core/utils/maintenance/community_operations.py`, `graphiti_core/nodes.py`; supplied core rebuild envelope | [MEM-OBJ-community-node](#mem-obj-community-node), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes). Cluster quality, update completeness and external consumer activation unobserved. |
| Saga summary and watermark read-back | Direct: `graphiti_core/graphiti.py`, `graphiti_core/nodes.py`, `mcp_server/src/graphiti_mcp_server.py` | [MEM-OBJ-saga-node](#mem-obj-saga-node), [MEM-RTE-saga-summary](#mem-rte-saga-summary). Character/byte budgets can drop content; losslessness is not supported. |
| Invalidation, rejection, deletion and clear | Direct: temporal resolution, core/MCP episode deletion and REST router/client deletion; supplied clear/rebuild | [MEM-CLM-withdrawal-scope](#mem-clm-withdrawal-scope), [MEM-CLM-saga-losslessness](#mem-clm-saga-losslessness). Removing graph objects is not demonstrated retraction from derived summaries or already delivered/checkpointed context. |
| Shipped conversation and checkpoint | Direct notebook code: `examples/langgraph-agent/agent.ipynb` | [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop), [MEM-OBJ-memory-saver](#mem-obj-memory-saver). Admission runs after every successful model response, including tool-call responses; returned tool rounds can feed tool-result/model-response episodes. Graph facts and checkpoints have separate consumers; framework durability/compatibility uninspected. |
| Assistant instructions and static prompt configuration | Supplied: `mcp_server/docs/cursor_rules.md`, `graphiti_core/prompts/lib.py`, `graphiti_core/llm_client/llm_runtime.py`; direct registered MCP names | [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions), [RT-RTE-prompt-routing](runtime.md#rt-rte-prompt-routing). Static instructions are not accumulated memory; host loading and procedural compliance unobserved. |
| Evaluation entry and retained results | Direct: `tests/evals/eval_e2e_graph_building.py`; entry searched: `tests/evals/eval_cli.py`; supplied comparison findings | [MEM-OBJ-graph-results](#mem-obj-graph-results), [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison). No measured quality or automatic deployment selection established. |
| MCP executable dispatch | Direct: `mcp_server/main.py`; registered operations searched in `mcp_server/src/graphiti_mcp_server.py` | Wrapper calls service main; registered add/search/delete/get/summarize/rebuild/triplet/clear tools match the inventory above. Host-side hooks/permissions remain outside frozen evidence, not inferred from tool registration. |
| Other examples, tests, prompt variants, provider alternatives and deployment configuration | Included and inventoried in boundary: quickstarts, ecommerce, podcast, wizard-of-oz, GLiNER2/Azure/telemetry examples; `tests/`, `spec/`, root and service configuration | Supplied findings establish some ingestion/search callers and alternate provider components. Their remaining memory transformations, evaluator routes and integration compatibility are available but not deeply inspected here. This prevents exhaustive consumer/prompt/backend enumeration and effectiveness claims; it does not suppress the directly established chains above. |

## Core ideas

1. **Raw suppression differs by admission path.** Episode content supplies later extraction context; derived facts supply retrieval. Single ingestion can blank raw content while preserving facts and lineage UUIDs. Bulk ingestion does not apply that suppression, and passes episode content unchanged to both writes even when raw retention is disabled. See [MEM-OBJ-episodic-node](#mem-obj-episodic-node) and [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
2. **Curation is not only model summarization.** Entity summaries can append facts directly before crossing a size threshold. Communities recursively compress entity summaries. Sagas fold new raw episodes into a previous summary under explicit budgets. These different transformations have different loss and withdrawal behavior. See [MEM-OBJ-entity-node](#mem-obj-entity-node), [MEM-OBJ-community-node](#mem-obj-community-node), [MEM-RTE-saga-summary](#mem-rte-saga-summary).
3. **Authority belongs to the eventual delivery channel.** Graph facts can arrive as data-rich MCP records, bare fact strings in a notebook system message, or candidates in an extraction prompt. Those channels carry different evidence and requested influence. Stored source labels and timestamps do not themselves authenticate the content. See [MEM-CLM-display-lineage](#mem-clm-display-lineage) and [RT-BAP-facts-context](runtime.md#rt-bap-facts-context).
4. **Temporal invalidation and deletion are not global forgetting.** Date fields permit historical selection. Deletion removes selected graph objects, but does not demonstrate revision of every summary or checkpoint that used them. See [MEM-CLM-withdrawal-scope](#mem-clm-withdrawal-scope).

## Shared records

### Components

none declared in this member. Provider model, embedder, reranker and notebook model identities are already declared in runtime; their weights and endpoint fixity are not reclassified as local graph memory.

### Operative objects

#### MEM-OBJ-episodic-node
Label: Retained episode content

Source-native identity: `EpisodicNode.content`, with message/text/JSON source typing and source description. Storage: graph node properties via driver saves; initially local objects. Form: raw natural-language messages/text, or caller JSON whose fields may mix symbolic and textual content. A JSON source label does not establish field-level provenance. Lineage: caller input; notebook episodes combine the latest state message object's string representation with newly generated `response.content`. On entry the latest message can be human input; after tool execution it is a tool result, potentially containing retrieved facts; supplied state can also end in a model message. Admission is scheduled after every successful model response, including tool-call responses. The unconditional user-name prefix does not authenticate human origin. Authorship and human approval are unresolved for generic callers. Single ingestion blanks content before its core persistence when raw retention is disabled; bulk ingestion does not apply that control. Later consumers: time/source/group-selected prior episodes in extraction and resolution, saga summarizer, REST/MCP episode recipients. API exposure alone does not establish what an unspecified recipient does with it. Closest supplied records are [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion) and [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop); this object is their retained input/result, not a duplicate route. SRC-1: `graphiti_core/nodes.py`, `graphiti_core/graphiti.py`, `examples/langgraph-agent/agent.ipynb`.

> content: str = Field(description='raw episode data')
> --- `graphiti_core/nodes.py`

Single `add_episode` calls `_process_episode_data`, which clears `ep.content` before calling the bulk persistence helper when raw storage is disabled; the clearing passage is retained in [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion). In contrast, `add_episode_bulk` creates or loads episodes, passes them directly to its initial and final bulk writes, and never invokes that clearing step. The helper serializes episode objects without suppressing content. Thus bulk raw retention is not merely a temporary prewrite: disabling the flag does not suppress raw text at either bulk write. Existing-UUID inputs use the loaded content. Actual database execution remains unobserved. SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/utils/bulk_utils.py`; [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion).

> episodes = [dict(episode) for episode in episodic_nodes]
> for episode in episodes:
>     episode['source'] = str(episode['source'].value)
>     episode.pop('labels', None)
> --- `graphiti_core/utils/bulk_utils.py`

> # save data to KG
> await add_nodes_and_edges_bulk(
>     driver,
>     episodes,
>     resolved_episodic_edges,
>     final_hydrated_nodes,
>     resolved_edges + invalidated_edges,
>     clients.embedder,
> )
> --- `graphiti_core/graphiti.py`

#### MEM-OBJ-entity-node
Label: Entity names, summaries and attributes

Source-native identity: textual/attribute portions of `EntityNode`. Storage: graph properties, with backend-specific attribute serialization. Form: names and summaries are natural language; typed attributes may have symbolic consumers or textual interpretation depending on caller schema. Model/software extraction and resolution derive content from episodes and existing candidates; direct callers may supply or replace it. Later consumers: entity resolution includes candidate summaries truncated to 120 characters; subsequent summarization reads existing summary/attributes; communities consume summaries; MCP node results supply readable summary/attributes to assistants. Summary content is not a reasoning transcript or certified warrant. Closest supplied records: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion), [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); no runtime object counterpart. SRC-1: `graphiti_core/nodes.py`, `graphiti_core/utils/maintenance/node_operations.py`, `mcp_server/src/utils/formatting.py`.

> if summary_with_edges and len(summary_with_edges) <= MAX_SUMMARY_CHARS * 2:
>     node.summary = summary_with_edges
>     continue
> --- `graphiti_core/utils/maintenance/node_operations.py`

This direct concatenation is a counterexample to treating every summary as model-compressed text. With `MAX_SUMMARY_CHARS = 1000`, the shortcut can keep up to 2000 characters. Model summaries are sentence-truncated to 1000; `skip_fact_appending` routes eligible nodes through the episode prompt instead, and `should_summarize_node` can skip them. The batch size is 30 nodes. Unknown returned entity names are logged rather than installed; matching is case-insensitive and can update multiple same-name nodes. These are software admission controls, not a truth oracle. SRC-1: `graphiti_core/utils/text_utils.py`, `graphiti_core/utils/maintenance/node_operations.py`.

#### MEM-OBJ-entity-edge
Label: Retained relationship fact text

Source-native identity: `EntityEdge.fact`, relation name and caller/schema-dependent attributes. Storage: graph relationship properties or backend-specific equivalent. Form: fact text is natural language; relation name/typed fields have symbolic consumers in filters/schema dispatch. Lineage: episode-derived extraction, duplicate reuse and temporal comparison, or supplied triplet/direct edge writes. Later consumers: searches, duplicate/contradiction resolution and entity summary generation; notebook assistant receives fact text only. Source episode UUIDs are separately programmatic lineage, not retained model reasons. Closest supplied records: [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion), [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval), [RT-BAP-facts-context](runtime.md#rt-bap-facts-context); distinct retained content. SRC-1: `graphiti_core/edges.py`, `graphiti_core/utils/maintenance/edge_operations.py`.

> fact: str = Field(description='fact representing the edge and nodes that it connects')
> --- `graphiti_core/edges.py`

#### MEM-OBJ-graph-metadata
Label: Graph identity, lineage and temporal selectors

Source-native identity: node/edge UUIDs, group IDs, endpoints, `EpisodicNode.entity_edges`, `EntityEdge.episodes`, timestamps and saga/community membership edges. Storage: graph properties and relationships; form: symbolic. These parts connect retained content to executable retrieval, deduplication, chronology and deletion. Episode references originate in extraction attribution or fallback to all batch episodes; they are lineage claims produced by software/model indices, not authenticated citations. `valid_at` and `invalid_at` represent event-time bounds; `expired_at` records invalidation processing time. Saga watermarks are assessed separately with [MEM-OBJ-saga-node](#mem-obj-saga-node). Groups scope selection/database routing, not demonstrated principal authorization. Closest supplied record: [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval); this object supplies selector inputs rather than a second retrieval route. SRC-1: `graphiti_core/nodes.py`, `graphiti_core/edges.py`, `graphiti_core/utils/maintenance/edge_operations.py`, `graphiti_core/search/search.py`.

> episodes: list[str] = Field(
>     default=[],
>     description='list of episode ids that reference these entity edges',
> )
> --- `graphiti_core/edges.py`

Content and metadata have different downstream survival: the notebook drops this metadata, while MCP fact search serializes it. Customer `episode_metadata` exists in the node model; the inspected explicit Neo4j single-save parameter map does not pass it. Full roundtrip behavior across bulk/query/backend variants is unresolved, so no universal customer-metadata retention claim is made. SRC-1: `graphiti_core/driver/neo4j/operations/episode_node_ops.py`, `mcp_server/src/utils/formatting.py`.

#### MEM-OBJ-graph-embeddings
Label: Retained graph search vectors

Source-native identity: entity/community `name_embedding`, edge `fact_embedding`. Storage: graph properties/index-supported backend representations, with transient local vectors during generation. Form: distributed numerical representations, separate from model parameters. Entity names and fact text are newline-normalized before embedding; vectors are inference results, not trained graph-owned weights. They influence semantic candidate selection and reranking; readable text remains the assistant-facing payload. Initial vectors for caller-supplied objects and community-generation variants are not uniformly traced. Closest supplied component: [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder); this is its stored output, not the model. SRC-1: `graphiti_core/nodes.py`, `graphiti_core/edges.py`, `graphiti_core/search/search.py`.

> text = self.fact.replace('\n', ' ')
> self.fact_embedding = await embedder.create(input_data=[text])
> --- `graphiti_core/edges.py`

MCP node and fact display strips embedding payloads. Evaluation exports likewise clear entity name and edge fact vectors before retaining results. Those readable summaries must not be mistaken for the complete numerical search state. SRC-1: `mcp_server/src/utils/formatting.py`, `tests/evals/eval_e2e_graph_building.py`.

#### MEM-OBJ-community-node
Label: Community summary and name

Source-native identity: `CommunityNode.summary` and generated name. Storage: graph properties; membership edges link entity nodes; form: natural-language summary/name, with symbolic membership and a separately classified embedding. Lineage: clusters of entities supply summaries; pairwise model reduction produces a bounded summary and a model-generated description/name. Incremental updates combine entity and existing community summary. Later consumers: advanced community search, future community updating, and MCP rebuild responses. No inspected notebook route consumes communities, so search capacity is not a demonstrated assistant-context route. Closest supplied record: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); distinct derived object. SRC-1: `graphiti_core/utils/maintenance/community_operations.py`, `graphiti_core/nodes.py`, `graphiti_core/search/search.py`, `mcp_server/src/graphiti_mcp_server.py`.

> summaries = [entity.summary for entity in community_cluster]
> --- `graphiti_core/utils/maintenance/community_operations.py`

The reduction retains summary text rather than model criticisms/reasons; membership retains source entities but does not prove every source fact survives compression. Rebuild first removes old community state, as quoted in [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes).

#### MEM-OBJ-saga-node
Label: Running saga summary and watermarks

Source-native identity: `SagaNode.summary`, first/last episode UUIDs, `last_summarized_at`, `last_summarized_episode_valid_at`. Storage: graph properties; form: natural-language summary plus symbolic cursor/recency metadata. Lineage: linked raw episodes and existing summary enter model generation, then bounded summary replaces the previous text. Later consumers: next `summarize_saga` prompt and MCP caller receiving summary; no notebook saga-context delivery is established. Ingestion-time cursor determines subsequent eligibility; event-time watermark describes recency and is not the filter cursor. Private selection counters are process-local diagnostics, not the saved summary. Closest supplied record: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); object not duplicate route. SRC-1: `graphiti_core/nodes.py`, `graphiti_core/graphiti.py`, `mcp_server/src/graphiti_mcp_server.py`.

> last_summarized_episode_valid_at: datetime | None = None
> _summary_episodes_fetched: int = PrivateAttr(default=0)
> --- `graphiti_core/nodes.py`

#### MEM-OBJ-memory-saver
Label: Notebook conversation checkpoint

Source-native identity: notebook `memory = MemorySaver()` used as graph checkpointer. Storage: external LangGraph in-process checkpointer requested by shipped code; exact internal representation and durability uninspected. Form at the notebook boundary: structured message/state objects with natural-language payloads and symbolic thread/tool fields; not a Graphiti summary or embedding. Lineage: conversation updates, separate from asynchronously ingested episodes. Later consumer: resumed notebook graph state supplies accumulated `state['messages']` to the model; checkpoint implementation is outside the frozen source. Closest supplied record: [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop); distinct retained alternative to derived graph memory. SRC-1: `examples/langgraph-agent/agent.ipynb`.

> "graph = graph_builder.compile(checkpointer=memory)"
> --- `examples/langgraph-agent/agent.ipynb`

#### MEM-OBJ-graph-results
Label: Retained evaluation graph results

Source-native identity: `baseline_graph_results.json` and candidate graph result exports, reconstituted as `AddEpisodeResults` for judgment. Storage: caller-local JSON files and evaluation graph state. Form: structured graph-result records carrying natural-language content and symbolic associations; entity/edge embeddings are cleared before export. Lineage: selected dataset messages processed by configured graph builders, not independently certified reference truth. Later consumer: candidate evaluator reloads baseline records and supplies baseline/candidate content to its judge; numerical score is immediate comparison output, not learned production guidance. Closest supplied record: [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison); distinct retained artifact. SRC-1: `tests/evals/eval_e2e_graph_building.py`.

> filename = 'baseline_graph_results.json'
> --- `tests/evals/eval_e2e_graph_building.py`

### Routes

#### MEM-RTE-saga-summary
Label: Incremental saga summary read-back
Part of: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)

This route specializes one operation in the supplied multi-operation maintenance container, not a replacement for it. Owner: `Graphiti.summarize_saga`; MCP resolves caller saga name/group to UUID before invoking it. Trigger: explicit caller/tool invocation. Progression: load saga → select linked episodes newer than ingestion cursor → budget and event-time reorder → prompt with previous summary → bounded summary and watermarks → save → return; next invocation reads the saved result. Proposed change is summary text and cursors. Caller initiates; model proposes text; software validates shape, truncates and persists. Human per-content approval/veto is unresolved. Guidance: configured saga prompt and previous summary; output retains text, not an exposed criticism/reasoning record. Mode: open caller-triggered maintenance, not bounded quality comparison. Answer oracle: inapplicable — no certified summary is supplied. Errors can reject generation/save; repair is caller-driven, with no whole-operation rollback history established. SRC-1: `graphiti_core/graphiti.py`, `mcp_server/src/graphiti_mcp_server.py`.

- Immediate return: updated `SagaNode`, unchanged node if no eligible content fits, or exception; MCP converts success to summary response and exceptions to errors.
- Later read-back: stored summary and ingestion cursor shape the next summarizer invocation; MCP returns readable text to an external tool caller without demonstrated downstream compliance.
- Delegated visibility: selected episode text, saga name and existing summary reach the configured model; graph driver receives summary and watermarks.
- Selection predicate: saga UUID, linked episodes with `created_at > last_summarized_at`, oldest ingestion first, at most 20; 100000-character episode packing, then assembled messages plus schema under 128 KiB; prompt episodes reordered by event time. Existing/output summary cap is 4000 characters, output request 8192 tokens. Oversized oldest episode is truncated rather than skipped.
- Invalidation or expiry: summary replacement; cursor advances to maximum creation time actually submitted, event-time watermark advances only forward. Later deferred episodes remain eligible, but truncated tails and equal-time cursor ties are not protected by that rule.
- Activation or effect: software writes the derived state and supplies it in the next prompt; faithful compression, assistant activation and improved capacity are unobserved.
- Evidence limits: external model/database execution unobserved; strict-time selection and text truncation prevent universal no-loss/no-skip claims; no inspected notebook saga consumer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> saga.last_summarized_at = max(summarized_created_ats) if summarized_created_ats else None
> --- `graphiti_core/graphiti.py`

### Claims

#### MEM-CLM-saga-losslessness
Label: Saga summary losslessness is not established

Claimed operation/source: the `summarize_saga` docstring says the existing summary is provided "so no information is lost" and that first call includes all episodes. The implementation instead caps the fetched window, truncates previous/output summaries, and can truncate the oldest episode. Advancing the cursor for that truncated episode prevents automatically revisiting its unsubmitted suffix. A strict greater-than creation-time filter also leaves tied creation times beyond a capped batch unresolved. This narrows documentation, not the supported incremental read-back mechanism. Closest supplied record: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); the supplied report did not assert losslessness. See [MEM-RTE-saga-summary](#mem-rte-saga-summary). SRC-1: `graphiti_core/graphiti.py`.

> When the oldest episode alone exceeds the budget, truncate it rather than
> skip, matching Go entity-summary behavior for a single oversized episode.
> --- `graphiti_core/graphiti.py`

#### MEM-CLM-withdrawal-scope
Label: Episode withdrawal does not ensure downstream retraction

Claimed operation/source: MCP `delete_episode` documentation promises preservation of entities and facts supported by other episodes. Its delegation reaches core `remove_episode`, which deletes an edge when the removed episode is first in `edge.episodes`, without requiring that list to have only one member. Therefore an edge with multiple supports can be removed if this episode is first; a sole-support deletion guarantee cannot be inferred from that documentation. Nodes use a count-of-mentions check instead. The inspected deletion body does not regenerate surviving entity/community/saga summaries or update external checkpoint messages; already delivered text is beyond its graph mutations. Closest supplied record: [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); distinct correction to source doctrine and qualification of withdrawal, not duplicate route. SRC-1: `mcp_server/src/graphiti_mcp_server.py`, `graphiti_core/graphiti.py`.

> for edge in edges:
>     if edge.episodes and edge.episodes[0] == episode.uuid:
>         edges_to_delete.append(edge)
> --- `graphiti_core/graphiti.py`

REST episode deletion is a distinct withdrawal path: its router calls `delete_episodic_node`, which loads and directly deletes the episode rather than invoking core `remove_episode`. It therefore does not run MCP's first-reference edge and mention-count node cleanup. Backend incident-edge effects remain uninspected; neither service establishes global derived-summary/checkpoint retraction. SRC-1: `server/graph_service/routers/ingest.py`, `server/graph_service/zep_graphiti.py`.

> async def delete_episodic_node(self, uuid: str):
>     try:
>         episode = await EpisodicNode.get_by_uuid(self.driver, uuid)
>         await episode.delete(self.driver)
> --- `server/graph_service/zep_graphiti.py`

Temporal invalidation is another retained-result path: code writes `invalid_at`/`expired_at`, not removal. Caller date filters can constrain reads. The inspected basic-search default uses empty `SearchFilters`, and fulltext fallback constructs date predicates only from supplied filters; no global current-truth-only guarantee follows from the temporal labels or search docstring. Other driver-native search implementations remain uninspected. SRC-1: `graphiti_core/utils/maintenance/edge_operations.py`, `graphiti_core/search/search_filters.py`, `graphiti_core/search/search_utils.py`, `graphiti_core/graphiti.py`.

> edge.invalid_at = resolved_edge.valid_at
> edge.expired_at = edge.expired_at if edge.expired_at is not None else utc_now()
> invalidated_edges.append(edge)
> --- `graphiti_core/utils/maintenance/edge_operations.py`

#### MEM-CLM-display-lineage
Label: Retrieval display changes available evidence

Claimed operation/source: the notebook passes bare fact strings into system/tool context, as already established by [RT-BAP-facts-context](runtime.md#rt-bap-facts-context). MCP fact search differs: `format_fact_result` serializes edge fields while excluding `fact_embedding`, retaining episode references and temporal fields at that boundary. Node display keeps summary/attributes and strips embedding-named attributes. Thus the notebook's loss of metadata is not a universal Graphiti read-back property. Neither display proves source trust; UUID lineage is not a checked quote, and summarization reasons are not exposed by these fields. Closest supplied record is the cited behavioral-authority path; this claim assesses an alternate display rather than redeclaring that path. SRC-1: `mcp_server/src/utils/formatting.py`, `examples/langgraph-agent/agent.ipynb`.

> "    return '-' + '\\n- '.join([edge.fact for edge in entities])"
> --- `examples/langgraph-agent/agent.ipynb`

### Evidenced absences

none declared in this member. Unobserved correctness, provider processing, compliance and remaining backend variants are limits, not absent mechanisms.

### Behavioral-authority paths

none declared in this member. Notebook and requested MCP assistant influence are already declared in [RT-BAP-facts-context](runtime.md#rt-bap-facts-context) and [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions). Summary read-back affects later model inputs; no observed activation is inferred from delivery.

## Annotations

#### On [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion)

Memory read-back includes previous raw episodes, not just vector-selected facts. The inspected fallback retrieves episodes with event time at or before reference time, filters group/source/saga as supplied, takes latest `last_n`, then reverses to chronological order. Explicit previous UUIDs bypass that temporal selector in single ingestion. Selected text/timestamps go into extraction/resolution context; prior graph facts and entity summaries guide deduplication and updates. Consumer authority is evidentiary/model-interpreted for text, fixed software authority for IDs/remapping. Single-ingestion raw suppression controls later inspectability rather than factual approval; bulk bypasses that suppression as described in [MEM-OBJ-episodic-node](#mem-obj-episodic-node). SRC-1: `graphiti_core/utils/maintenance/graph_data_operations.py`, `graphiti_core/graphiti.py`; [MEM-OBJ-episodic-node](#mem-obj-episodic-node), [MEM-OBJ-graph-metadata](#mem-obj-graph-metadata).

> ORDER BY e.valid_at DESC, e.created_at DESC
> LIMIT $num_episodes
> --- `graphiti_core/utils/maintenance/graph_data_operations.py:152-167`

#### On [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval)

Core advanced selection has separately configured edge, node, episode and community layers; only recipes needing similarity/MMR generate a query vector. REST `get-memory` concatenates supplied role/content messages into one query and returns selected facts, not an assembled assistant prompt. MCP node selection chooses RRF or node-distance, then slices `results.nodes[:max_nodes]` after recipe-limited search: a requested count above that recipe's limit does not guarantee that many nodes. Fact search forwards its positive count to core. These are request-driven selectors, not independently triggered pushes. Formatted delivery drops vectors but retains different textual/metadata parts by endpoint. SRC-1: `graphiti_core/search/search.py`, `server/graph_service/routers/retrieve.py`, `mcp_server/src/graphiti_mcp_server.py`, `mcp_server/src/utils/formatting.py`; [MEM-CLM-display-lineage](#mem-clm-display-lineage).

> nodes = results.nodes[:max_nodes] if results.nodes else []
> --- `mcp_server/src/graphiti_mcp_server.py`

#### On [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop)

Trace-fed memory chain: latest state message representation (human, tool or model origin) plus new model response content → unconditionally scheduled single-episode ingestion after each successful model response → extraction/resolution and configurable single-path raw persistence → retained graph facts/summaries → later query-selected facts → system message or tool return. Tool-call responses also schedule ingestion; the tools-to-agent edge then permits tool-result/model-response episodes without a new human turn. Retrieved facts returned by the tool can therefore re-enter extraction. The user-name prefix does not validate origin or confer user authority. This is implemented trace-fed curation, not demonstrated improvement. It retains content and lineage rather than the assistant's reasons; notebook formatting omits lineage at the later model. A second path keeps conversation messages through `MemorySaver` and supplies them as model context. Graph clear does not by itself demonstrate clearing that separate checkpoint. No independent unsolicited memory push is wired: graph retrieval is triggered by chatbot invocation. SRC-1: `examples/langgraph-agent/agent.ipynb`; [MEM-OBJ-memory-saver](#mem-obj-memory-saver), [MEM-OBJ-entity-edge](#mem-obj-entity-edge).

> "            episode_body=f'{state[\"user_name\"]}: {state[\"messages\"][-1]}\\nSalesBot: {response.content}',\n",
> --- `examples/langgraph-agent/agent.ipynb`

> "graph_builder.add_edge('tools', 'agent')\n",
> --- `examples/langgraph-agent/agent.ipynb`

#### On [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes)

Direct save is separate admission from extraction: `EntityNodeNamespace.save` generates a name vector and hands the supplied object to operations, without an episode-extraction call in that body. Who authored or approved supplied text remains unresolved; physical database I/O does not answer that question. Community summary derivation and saga folding are software/model admission, while explicit delete/clear/rebuild are caller-triggered withdrawal/maintenance. Their different substrates and later consumers are [MEM-OBJ-community-node](#mem-obj-community-node), [MEM-OBJ-saga-node](#mem-obj-saga-node) and [MEM-OBJ-entity-node](#mem-obj-entity-node). SRC-1: `graphiti_core/namespaces/nodes.py`, `graphiti_core/utils/maintenance/community_operations.py`, `graphiti_core/graphiti.py`.

> await node.generate_name_embedding(self._embedder)
> await self._ops.save(self._driver, node, tx=tx)
> return node
> --- `graphiti_core/namespaces/nodes.py:47-49`

#### On [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison)

Baseline/candidate exports are retained derived outputs, not raw conversation histories. The baseline JSON read-back reaches a model judge; it does not establish installation of improved production instructions. The supplied character-sliced judge-context finding remains consequential: result export is real wiring, but intended contextual comparison and score interpretation are bounded. SRC-1: `tests/evals/eval_e2e_graph_building.py`; [MEM-OBJ-graph-results](#mem-obj-graph-results).

## Write side

Acquisition accepts caller episode text/source/time/schema and direct supplied objects; the notebook's mixed human/tool/model-origin feed is directly established. It schedules ingestion on tool-call responses as well as terminal responses, and returned tool rounds can record retrieved facts as part of a tool result rather than new human testimony. Human authorship, editing and approval remain separate unknowns for generic callers. Software extraction, entity/fact resolution, summary generation and embedding admit derived state, while input/schema validation, invalid model results and exceptions can reject stages. None of those controls authenticates factual truth. Single/bulk write and queue envelopes retain the distinct failure limits in [RT-CLM-write-envelope](runtime.md#rt-clm-write-envelope) and [RT-CLM-queue-completion](runtime.md#rt-clm-queue-completion).

Raw-text admission control is path-specific: single ingestion applies `store_raw_episode_content` in `_process_episode_data`; bulk bypasses that step and serializes unchanged content at both writes. This is a policy-scope discrepancy, not merely a prewrite or durability caveat. It affects later raw-episode extraction context, saga inputs and episode getters; see [MEM-OBJ-episodic-node](#mem-obj-episodic-node).

Entity summary appending, bounded model summaries, community reduction and saga folding are curation mechanisms, not synonyms for an evidence review. Existing graph text shapes future transformations. Static prompts/routes can be changed by configuring callers but are not automatically revised by accumulated traces in [RT-RTE-prompt-routing](runtime.md#rt-rte-prompt-routing). The implemented trace-fed notebook writes produce later-readable knowledge; no measured learning benefit or retained content-directed criticism is established by these mechanisms. Evaluation judgment remains a separate retained-results consumer, not a production gate.

Withdrawal includes temporal annotations, individual delete, MCP/core episode cleanup, REST direct episode-node deletion, graph clear and destructive community rebuild. REST and MCP do not invoke equivalent episode cleanup. Each changes particular retained state rather than restoring a whole prior version. The source documentation overstates shared-edge preservation and saga losslessness; [MEM-CLM-withdrawal-scope](#mem-clm-withdrawal-scope) and [MEM-CLM-saga-losslessness](#mem-clm-saga-losslessness) retain the counterexamples.

## Read-back

- **Automatic processing after a request:** new ingestion retrieves prior episodes and graph candidates; selector inputs are event time, source/group/saga or explicit UUIDs. The later consumers are extraction/resolution models and symbolic remapping code, not necessarily an assistant. See annotation on [RT-RTE-episode-ingestion](runtime.md#rt-rte-episode-ingestion).
- **Query-driven agent context:** latest notebook message and user center node select five facts; shoe tool selects ten around product center. Bare text reaches system/tool channels, while checkpoint messages independently enter conversation context. A tool return can become the latest message in the next chatbot invocation, be used as the next query and enter a newly scheduled episode with model response content. Thus later facts can derive from earlier human, tool or model material, not only user testimony. See [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop) and [MEM-CLM-display-lineage](#mem-clm-display-lineage).
- **Service retrieval:** REST message-concatenation and MCP node/fact query/filter selectors return readable records. Specific UUID/episode getters expose lineage lookup, not a hypothetical behavioral consumer. Shipped rules establish an afforded external assistant role for preferences/procedures, but actual host mapping and compliance are uninspected in [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions).
- **Summary maintenance:** entity/community updates consume previous derived text; saga folding consumes previous summary and bounded new episodes. Community advanced search is a read capability with unspecified external caller; saga next-invocation summary consumption is concretely wired in [MEM-RTE-saga-summary](#mem-rte-saga-summary).
- **Evaluation:** saved baseline results are reloaded for candidate judgment. They carry model-produced reference content, not certified expected truth; see [RT-RTE-evaluation-comparison](runtime.md#rt-rte-evaluation-comparison).

The mechanisms above are request-driven even when an automatic selector runs internally. Delivery and persistence are supported; exercised behavioral activation and benefit are not observed.

## Integration issues

1. **Withdrawal doctrine correction:** MCP promises shared fact preservation, but core tests first supporting episode rather than sole support. REST instead directly deletes the episode through `delete_episodic_node`, without core cleanup; the service effects must not be equated. Preserve [MEM-CLM-withdrawal-scope](#mem-clm-withdrawal-scope) beside [RT-RTE-maintenance-writes](runtime.md#rt-rte-maintenance-writes); no supplied fact is directly contradicted, but reconciliation must not expand "delete" into globally safe retraction.
2. **Saga doctrine correction:** no-loss/all-episodes wording is contradicted by bounded batches, previous/output summary truncation and truncated input cursor advancement. Tied creation-time eligibility also remains unresolved. [MEM-CLM-saga-losslessness](#mem-clm-saga-losslessness) qualifies [MEM-RTE-saga-summary](#mem-rte-saga-summary), without negating wired incremental read-back.
3. **Display scope:** [MEM-CLM-display-lineage](#mem-clm-display-lineage) limits the bare-fact authority finding to notebook formatting; MCP retains richer metadata. Do not generalize [RT-BAP-facts-context](runtime.md#rt-bap-facts-context) to all consumers.
4. **Possible overlaps:** the saga route is explicitly part of the supplied maintenance container. Other new objects have no supplied operative-object counterpart; they are inputs/results of the cited runtime routes, not duplicate route identities. New claims qualify operations already covered by runtime but establish different source-doctrine/display findings. No other possible duplicates found in the supplied records.
5. **Unresolved operative details:** all-backend customer-metadata persistence, driver-native date filtering/deletion/index cleanup, combined-versus-separate bulk content, other example consumers/evaluators, attribute-level source lineage and community update completeness remain partly uninspected. Coverage table gives paths and prevented generalizations. Opaque external model processing does not settle factual trust or reasoning retention.
6. **Host/instruction wiring:** shipped rule name `search_facts` differs from registered `search_memory_facts`; loading/mapping/compliance are unresolved as already noted in [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions). The afforded procedural role is not a deployed control guarantee.
7. **Queue/checkpoint timing:** process-local acceptance and unawaited ingestion do not ensure next-turn availability; graph deletion is not checkpoint deletion. Retain these limits from [RT-RTE-service-admission](runtime.md#rt-rte-service-admission), [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop) and [MEM-OBJ-memory-saver](#mem-obj-memory-saver).

8. **Trace-origin correction:** the previous memory report described the notebook feed too narrowly as user-message/model-response. [MEM-OBJ-episodic-node](#mem-obj-episodic-node), the conversation annotation and dependent prose now retain human/tool/model origins, unconditional response scheduling and graph-fact recirculation. These agree with the supplied corrected [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop); no human-origin authentication follows from the user-name prefix.
9. **Raw-retention correction:** the previous report incorrectly generalized final suppression from single ingestion to bulk. [MEM-OBJ-episodic-node](#mem-obj-episodic-node) now distinguishes single-path clearing from unchanged-content bulk prewrite and final write. This qualifies [RT-RTE-bulk-ingestion](runtime.md#rt-rte-bulk-ingestion) without retracting single-path suppression; bulk raw content remains eligible for later extraction, saga summarization and getters when successfully persisted.

## Limitations and checks

Source HEAD was rechecked as `964bb11d1e7020e3cc67fab244268b0736b6c219`, matching boundary and report identity. Run ID and source identity match the supplied invocation. The supplied memory job, member/peer types, worker rules, collection and records contract were read completely; runtime's trailing range was recovered. No other run or prior review was inspected, and no target execution or dependency installation occurred.

Conclusions cover inspected code wiring and supplied findings, not deployed durability, successful provider processing, factual correctness, assistant compliance, improved future capacity or causal benefit. Remaining included source variants are explicitly named in coverage rather than silently treated as absent. Deterministic validation is recorded below after execution; it checks structure and quote occurrence, not analytical completeness or job acceptance.

Validation: completed successfully with the invocation-specified role/artifact command.
