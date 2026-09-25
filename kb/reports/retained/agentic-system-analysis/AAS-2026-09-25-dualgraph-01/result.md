---
{
  "type": "kb/types/agentic-system-analysis-result.md",
  "description": "Complete code-grounded DualGraph workflow analysis: within-report graph/outline reuse, warrant limits and static default-path defects.",
  "run-id": "AAS-2026-09-25-dualgraph-01",
  "system": "DualGraph",
  "run-date": "2026-09-25",
  "result-disposition": "complete",
  "target-class": "workflow",
  "boundary-kind": "subsystem-only",
  "reviewed-boundary": "c090b7d57e3996c8900e86fecd16085b27e07f29",
  "analysis-cutoff": "2026-09-25",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Named DualGraph subsystem: accumulated within-report outline, evidence, knowledge graph, embeddings/clusters/chains, query/URL history, report prefix/products, optional Neo4j projection and human demo/live display read-back. Excludes static prompts as memory, other DKI_LLM subsystems, external provider internals and benchmark/generated-output execution evidence. Wired denotes inspected code connections, not successful operation; RTE-9 records default-path defects.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "files",
          "graph",
          "in-memory"
        ],
        "records": [
          "OBJ-10",
          "OBJ-11",
          "OBJ-12",
          "OBJ-13",
          "OBJ-14",
          "OBJ-15",
          "OBJ-16",
          "OBJ-17",
          "OBJ-18",
          "OBJ-19",
          "OBJ-6",
          "OBJ-20",
          "OBJ-21",
          "OBJ-22",
          "OBJ-23",
          "RTE-8"
        ],
        "note": "In-memory state, serialized products and optional Neo4j graph. Embedding lists are cached in the in-memory graph object, not a separate vector database. External service internals are excluded."
      },
      "representational_form": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "records": [
          "OBJ-10",
          "OBJ-11",
          "OBJ-12",
          "OBJ-13",
          "OBJ-14",
          "OBJ-15",
          "OBJ-16",
          "OBJ-17",
          "OBJ-18",
          "OBJ-19",
          "OBJ-6",
          "OBJ-20",
          "OBJ-21"
        ],
        "note": "Prose plus typed graph records, identifiers, sets, numeric vectors and scores. Vectors are numerical inputs to explicit algorithms; no retained learned model parameters are established inside this boundary."
      },
      "lineage": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "imported",
          "other-compiled",
          "trace-extracted"
        ],
        "records": [
          "OBJ-10",
          "OBJ-11",
          "OBJ-12",
          "OBJ-13",
          "OBJ-14",
          "OBJ-15",
          "OBJ-16",
          "OBJ-17",
          "OBJ-18",
          "OBJ-19",
          "OBJ-6",
          "OBJ-20",
          "OBJ-21"
        ],
        "note": "Imported source metadata/snippets, automatic extraction from page-reader/search/model outputs, and compiled topology/cache/access metadata. Static authored prompts and initial task requests are not accumulated memory."
      },
      "behavioral_authority": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "enforcement",
          "instruction",
          "knowledge",
          "ranking",
          "routing",
          "validation"
        ],
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-5",
          "RTE-6",
          "RTE-7"
        ],
        "note": "Evidence and report prefix inform; outline instructs section/query roles; graph metadata ranks; IDs route evidence; visited/history sets enforce exclusions; outline is consumed by the completion judge. No model-weight learning authority."
      },
      "write_agency": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "automatic"
        ],
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-7",
          "RTE-8"
        ],
        "note": "Scoped accumulated memory is automatically produced and updated. Human query/settings and optional blocked URL input trigger or configure it; no wired human editing/adoption loop for retained memory was found."
      },
      "curation_operations": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "consolidate",
          "decay",
          "dedup",
          "evolve",
          "promote",
          "synthesize"
        ],
        "records": [
          "RTE-2",
          "RTE-4",
          "RTE-5",
          "RTE-7"
        ],
        "note": "Semantic normalization reduces and merges retained concepts; outline/graph metadata evolve; orphan concept pruning forgets; core-entity flag promotion raises planning salience; missing-link candidates and their probability/gap claims are synthesized from retained graph structure. No history-preserving invalidation route established. See rationale for narrow mappings."
      },
      "read_back_direction": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "pull",
          "push"
        ],
        "records": [
          "RTE-2",
          "RTE-5",
          "RTE-6",
          "RTE-7",
          "RTE-8"
        ],
        "note": "Models receive automatically assembled context; the human demo consumer explicitly requests replay. Neo4j load_graph alone does not establish another consumer route."
      },
      "read_back_signal": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-2",
          "RTE-5",
          "RTE-7",
          "RTE-8"
        ],
        "note": "Partial supported mapping is coarse, identifier, inferred-embedding and inferred-judgment. Topology/evidence-count/community selectors are also implemented but have no faithful controlled token; do not silently describe the partial set as complete."
      },
      "trace_learning": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "yes"
        ],
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-7"
        ],
        "note": "Automatic retained page summaries, derived graph/outline/plans and growing report prefix feed later roles. This is the comparison contract's trace-fed context criterion, not demonstrated improvement or weight training. Default-route defects constrain successful execution."
      },
      "trace_source": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "tool-traces",
          "trajectories"
        ],
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-7"
        ],
        "note": "Search/page-reader returns feed summaries and derived state; prior generated outline, plans and report sections feed subsequent calls. No raw log ingestion is required or established."
      },
      "learning_scope": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "per-task"
        ],
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-7"
        ],
        "note": "Fresh state is allocated inside one report process; its iterative and section-writing routes establish the report task horizon. Demo replay and database serialization do not establish cross-task agent learning."
      },
      "learning_timing": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "online"
        ],
        "records": [
          "RTE-2",
          "RTE-3",
          "RTE-4",
          "RTE-5",
          "RTE-7"
        ],
        "note": "Qualifying writes and later consumption occur during report generation. Saved product files are not an offline learning pipeline."
      },
      "distilled_form": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "records": [
          "OBJ-10",
          "OBJ-11",
          "OBJ-12",
          "OBJ-13",
          "OBJ-14",
          "OBJ-15",
          "OBJ-16",
          "OBJ-17",
          "OBJ-18",
          "OBJ-19",
          "OBJ-20",
          "OBJ-21"
        ],
        "note": "Qualifying trace-fed routes retain textual summaries/outline/report prose and symbolic graphs, access structures and numeric derived representations; no learned parameters."
      },
      "faithfulness_tested": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "no"
        ],
        "records": [
          "ABS-1"
        ],
        "note": "No admitted retained execution evidence tests dependence on recalled content. README benchmark claims are not a recalled-content intervention."
      }
    }
  }
}
---

# DualGraph agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-dualgraph-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/dualgraph.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-dualgraph-01/memory-report.md`

**Memory analysis report SHA-256:** `1477e69def70f140d5be8c9988aac6cc6f7f5878e786c4cf3917d93a490dba8a`

Frozen specialist input SHA-256: `f36aaa4b767977d891b6299b65c872e668f406b81a5e04d3413a680e3902e9b0`.

## Boundary and evidence

This complete, source-only analysis characterizes the named DualGraph report workflow in microsoft/DKI_LLM, not the enclosing repository. Boundary kind: subsystem-only. Includes CLI and Chainlit live/demo entry paths, search/read/summarization, outline and knowledge-graph mutations, planning, completion judging, report production and optional graph persistence. Source revision `c090b7d57e3996c8900e86fecd16085b27e07f29`, cutoff 2026-09-25, code-grounded. The intended use is architectural understanding and a normalized memory comparison.

External LLM/embedding/search/reader/Neo4j/GDS services are dependencies; their implementation and deployed behavior are excluded, preventing guarantees about accuracy, weight fixity, isolation and availability. Other repository subsystems, benchmark reproduction and generated example-report prose are excluded. No candidate artifact, observed run or causal experiment is admitted. All wired conclusions describe inspected connections conditional on route prerequisites; RTE-9 prevents treating the shipped defaults as a demonstrated successful pipeline.

## Source register

SRC-1 — Git `https://github.com/microsoft/DKI_LLM` at `c090b7d57e3996c8900e86fecd16085b27e07f29`; operational access root `/home/zby/llm/commonplace/related-systems/microsoft--DKI_LLM`. Implementation: commit-addressed DualGraph/deepresearch/baselines main, app, data_model, knowledge_graph_module, search_module, outline_module, terminal_module, write_module, llm_utils and neo4j_kg_store modules plus their prompt files. Doctrine/design and reported benchmark claim: `DualGraph/README.md:7,80-168`. Anchors below name full commit-relative paths. No source access gap; external runtime and candidate evidence are unavailable by boundary. Initial truncated whole-repository listing was discarded and repeated as bounded DualGraph listing; truncated content reads were repeated before use. No prior analyses supplied evidence.

## Shared records

### Components

CMP-1 — CLI/report orchestration and Chainlit interface, Python control flow and configuration; user supplies query/settings, process controls iteration and files. Implementation conclusion status: wired, with RTE-9 defects. SRC-1 `DualGraph/deepresearch/baselines/main.py:17-23,136-306`; `DualGraph/deepresearch/baselines/app.py:278-443`.

CMP-2 — External LLM wrapper used for outline, extraction, merge, query selection, page summary, judge and writer. Representational form: distributed-parametric provider models, accessed through prompt/response API; local parameters are configuration, not trained weights. Endpoint/model resolution conclusion status: wired; mutable configured OpenAI/Azure/custom deployment names do not pin provider weights. Operational parameter-change/fixity conclusion status: uninspected for provider internals; inspected wrapper issues inference requests, not an optimizer. Shared wrapper across roles does not create an independent answer oracle. SRC-1 `DualGraph/deepresearch/baselines/llm_utils.py:79-248,271-413`; `DualGraph/deepresearch/baselines/main.py:87-118,854-890`.

CMP-3 — Search providers, page readers and summary role. Local Python dispatch plus external Bing/Serper and reader services; content and snippets pass through a model usefulness/summary decision. Implementation conclusion status: wired, with RTE-9 Serper caveat. SRC-1 `DualGraph/deepresearch/baselines/search_module.py:63-352,481-712,783-1005`.

CMP-4 — KnowledgeGraph/EvidenceNode objects and graph extraction/planning algorithms. Symbolic in-memory structures with natural-language labels; graph transformations and algorithmic rankings are local, model semantic decisions external. Implementation conclusion status: wired conditional branches. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:11-100,256-651`; `DualGraph/deepresearch/baselines/knowledge_graph_module.py:415-1432,1435-2148`.

CMP-5 — External embedding interface, local numeric cache, HDBSCAN and community algorithms. Embedding identity resolution conclusion status: wired to configured provider name, default text-embedding-3-large; exact provider weight identity and updates conclusion status: uninspected. Cached vectors are numeric algorithm inputs, not local learned weights. Clustering changes graph metadata and optionally merges nodes. SRC-1 `DualGraph/deepresearch/baselines/llm_utils.py:414-441`; `DualGraph/deepresearch/baselines/knowledge_graph_module.py:26-169,1857-1895`.

CMP-6 — Optional Neo4j store and GDS interface. Database external; Python serialization, replacement, partial load and feedback call sites inspected. Implementation conclusion status: wired, disabled by default; deployment correctness uninspected. SRC-1 `DualGraph/deepresearch/baselines/neo4j_kg_store.py:110-283,347-385`; `DualGraph/deepresearch/baselines/main.py:270-295`.

### Operative objects


OBJ-1 — Outline text. Hierarchy, research points and inline evidence IDs are mixed natural-language/symbolic content, produced by model calls and retained in memory and iteration text files. The initial outline comes from the root query; updates come from earlier outline, new evidence and graph. Query generators, terminal judge and section writer consume it as a plan, evidential summary and completion-test input. The code returns strings despite an initial SkeletonGraph annotation. SRC-1 `DualGraph/deepresearch/baselines/outline_module.py:26-77,175-225`; `DualGraph/deepresearch/baselines/main.py:328-332,630-655`. No separate operative graph traversal over a SkeletonGraph is established.

OBJ-2 — EvidenceNode records. Integer ID, source title/URL and content are retained. Content normally contains model-generated Summary and model-selected Evidence, not the complete raw page. Both page-reader output and fallback search snippets can feed it. Stored in memory, graph JSON/products and optional Neo4j evidence nodes; later consumed by extraction, outline revision and selected report sections. Natural-language payload plus symbolic addressing; imported attribution with trace-extracted content; advisory knowledge authority. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:11-15,91-100`; `DualGraph/deepresearch/baselines/search_module.py:318-352,870-883`.

OBJ-3 — KnowledgeNode/KnowledgeEdge records and merge history. Natural-language node/relation labels in a symbolic directed graph; edge-to-evidence objects carry source attribution. Node-level content contains no retained extraction rationale. Merge history retains old ID/name/new ID, not semantic-merge justification. Graph state informs outline revision and query planning; direct writer delivery is an optional branch. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:38-73,256-388,408-544`.

OBJ-4 — Numeric embedding cache, semantic-cluster metadata and graph communities. In-memory lists/dictionaries and graph JSON hold computed vectors, labels and membership. Embeddings come from an external API; the visible payload is a list of floats used for explicit cosine distance/similarity. It is not a locally updated model weight payload. Semantic clusters keep a generated algorithm label/size justification, but ordinary graph JSON/TOON omits cluster/community metadata; communities remain operative in graph algorithms. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:63-169,494-575,683-760`; `DualGraph/deepresearch/baselines/data_model.py:160-203,546-651`; `DualGraph/deepresearch/baselines/llm_utils.py:414-441`.

OBJ-5 — Chains, visited-edge keys and planned queries. Chains carry symbolic IDs/types/node pairs, natural-language content and an explicit reason; they are regenerated from current graph state and passed into model planning. Visited keys persist across iterations in memory; chain JSON and selected content/query files are observer copies. Selected does not mean executed or confirmed. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:685-691`; `DualGraph/deepresearch/baselines/knowledge_graph_module.py:2109-2148`; `DualGraph/deepresearch/baselines/main.py:704-739`.

OBJ-6 — Executed-query history and visited/blocked URL sets. Exact strings/identities suppress repeat work in code; query history is also included in model prompts. A passed blocked URL set seeds visited state, without a human editing loop over later memory. Successful admitted evidence adds URLs; rejected/failed pages generally remain eligible. SRC-1 `DualGraph/deepresearch/baselines/main.py:300-306,410-420,573-584,704-711`; `DualGraph/deepresearch/baselines/search_module.py:101-150,229-251,998-1005`.

OBJ-7 — Growing report, final report and references. Generated natural-language sections accumulate in memory and are supplied to later section calls. The completed report is written to Markdown; reference postprocessing deduplicates URL entries and rewrites numeric citations. Citation renumbering does not validate factual support. SRC-1 `DualGraph/deepresearch/baselines/write_module.py:24-99,323-426`; `DualGraph/deepresearch/baselines/main.py:788-805`.

OBJ-8 — Product files, logs/usage and optional Neo4j projection. Iteration files preserve outline, graph JSON, evidence, queries and chains; usage/logs are observer records, not a read-back learning corpus. Neo4j replacement persists nodes/evidence/relations under report_id, but omits the embedding cache, merge history, semantic-cluster list and community_list. Its load method reconstructs a partial graph, not a complete continuation checkpoint. SRC-1 `DualGraph/deepresearch/baselines/main.py:392-447,607-628,714-739`; `DualGraph/deepresearch/baselines/neo4j_kg_store.py:120-283`; `DualGraph/README.md:117-151`.

OBJ-9 — Completion decision. The judge receives root query and current outline, parses numeric ratings and returns a threshold conjunction; it can end the loop. This is task-completion control, not source verification or durable experience memory. SRC-1 `DualGraph/deepresearch/baselines/terminal_module.py:74-142`; `DualGraph/deepresearch/baselines/main.py:741-763`.


The combined seed records above retain their identities and generic descriptions. For the epistemic inventory, the following heterogeneous seeds are superseded by separately addressable parts: OBJ-1 by OBJ-10 and OBJ-11; OBJ-2 by OBJ-12 and OBJ-13; OBJ-3 by OBJ-14 and OBJ-15; OBJ-4 by OBJ-16 and OBJ-17; OBJ-5 by OBJ-18 and OBJ-19; OBJ-7 by OBJ-20 and OBJ-21; OBJ-8 by OBJ-22 and OBJ-23; OBJ-9 by OBJ-24 and OBJ-25. These are part refinements, not evidence upgrades.

OBJ-10 — Outline substantive points. Natural-language claims and inline evidence IDs, produced/replaced by outline model, consumed by queries/judge/writer; inherited OBJ-1 lineage and files. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/outline_module.py:175-225`.

OBJ-11 — Outline organization. Hierarchy and writing/search plan, instructional structure, same production/storage as OBJ-1. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/outline_module.py:175-225`.

OBJ-12 — Evidence attribution. Imported title/URL/ID, symbolic metadata for source lookup and references. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:11-15`.

OBJ-13 — Evidence Summary/Evidence text. Model-generated summary and selected excerpts from page or fallback snippet; natural-language payload; usefulness rationale discarded. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/search_module.py:318-352,870-883`.

OBJ-14 — Graph content. Natural-language entity/concept/relation labels in symbolic node/edge records, model-derived and merged, used by outline/planner. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:256-388,408-544`.

OBJ-15 — Graph attribution and merge lineage. Edge evidence pointers and old-name/ID→new-ID merge records; structural lineage, not semantic-merge justification. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:325-388,462-519`.

OBJ-16 — Embedding vectors. External-model numeric vectors cached locally and used for similarity algorithms; not model parameters. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:63-169,683-760`.

OBJ-17 — Cluster/community metadata. Membership and algorithm summaries; ordinary JSON/TOON omits them, community algorithms still consume membership. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:160-203,546-651`.

OBJ-18 — Exploration hypotheses and reasons. Missing-link candidate/probability/gap assertions and retained reason text; planner consumes as search possibilities, not established edges. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:864-964,2028-2033`.

OBJ-19 — Planning control. Chain IDs/types, selected query strings and visited pair/type keys; symbolic operational state distinct from confirmed search execution. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:2109-2148`.

OBJ-20 — Report prose. Generated sections and growing prior prefix; model-produced natural-language content, later section context and final file. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/write_module.py:323-426`.

OBJ-21 — References. URL/title/number mapping and citation marks, symbolic attribution formatted after writing. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/write_module.py:24-99`.

OBJ-22 — Saved graph/outline/report products and Neo4j projection. Symbolic/prose serialization and optional human replay; partial database load differs from full continuation. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/neo4j_kg_store.py:120-283`.

OBJ-23 — Usage/log records. Observer records, no admitted learning consumer. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/main.py:788-851`.

OBJ-24 — Completion ratings. Model numerical quality assertions from root query and outline, not source-evidence verification. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/terminal_module.py:74-142`.

OBJ-25 — Completion controls. Threshold conjunction and iteration/disable options, symbolic loop control. Implementation conclusion status: wired, subject to RTE-9. SRC-1 `DualGraph/deepresearch/baselines/main.py:741-763`.

### Routes

RTE-1 — Per-report initialization. Trigger: CLI report item or live request. Producer: orchestrator. It skips an existing final report or creates fresh graph/history/visited state; it does not load previous graph products. Persistence is separate from initialization. Status: wired CLI initialization; live invocation has the configuration defect in RTE-9. SRC-1 `DualGraph/deepresearch/baselines/main.py:247-306`; `DualGraph/deepresearch/baselines/app.py:387-443`.

>         knowledge_graph = KnowledgeGraph()
>         history_search_queries = (
>             []
>         )  # Only tracks actually-executed queries, to avoid duplicate searches
>         visited_urls = set()  # Dedup set to avoid re-fetching the same page
>         if blocked_urls:
>             visited_urls.update(blocked_urls)
> --- `DualGraph/deepresearch/baselines/main.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


RTE-2 — Outline generation/revision and query generation. Trigger: initialization or iteration after graph update. Producer: model called with retained outline, evidence and graph. Returned text replaces the active outline and is saved. Later consumers are outline query generator, chain selector, completion judge and writer. The selector is automatic, usually supplies the complete outline, and uses configured query count as a prompt instruction. Status: wired, subject to upstream default failures. SRC-1 `DualGraph/deepresearch/baselines/outline_module.py:175-225,255-302`; `DualGraph/deepresearch/baselines/main.py:630-695`.

RTE-3 — Search/page acquisition to retained evidence. Search calls filter exact visited URL identities; model URL selection chooses from returned results with a fallback to all results on parse error, followed by a maximum-five URL cap. Page readers return text/Markdown; optional Jina fallback or snippets feed the summarizer. Model usefulness governs admission. Accepted Summary/Evidence is stored in OBJ-2 and product files, then consumed by RTE-4, RTE-2 and RTE-7. Status: wired, with Serper default defect noted below. SRC-1 `DualGraph/deepresearch/baselines/search_module.py:101-150,229-352,435-478,687-712,783-797,870-885`; `DualGraph/deepresearch/baselines/main.py:379-402`.

RTE-4 — Graph extraction, admission and maintenance. Trigger: each evidence batch. Model receives selected evidence text, root/search queries, optionally existing graph; defaults omit existing graph during extraction. Code integrates model nodes/edges, merges duplicate names/triples and evidence links, promotes repeated nodes to core when designated, and prunes disconnected non-core concepts. A separate semantic-merge call receives the whole graph; code replaces concepts/edges and migrates evidence. Subsequent graph planner and outline updater consume the result. Status: wired implementation with the default summary helper missing. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:1435-1523,1624-1742,1745-1897`; `DualGraph/deepresearch/baselines/data_model.py:256-544`.

>             merge_knowledge_node_end_time = time.time()
>             llm_output = safe_json_loads(response.content)
>             if llm_output is None:
>                 raise ValueError("safe_json_loads returned None")
>             knowledge_graph.apply_merge_node_results(llm_output)
> --- `DualGraph/deepresearch/baselines/knowledge_graph_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


RTE-5 — Graph access metadata and exploration planning. Trigger: graph creation/update before next iteration. Producers: embedding client, HDBSCAN, Leiden, graph scoring code and model selector. Inputs: graph labels/edges, evidence counts, community memberships, visited keys, outline and query history. Cached vectors and graph metadata support later algorithms; generated chains and query strings become next-round search controls. Ordinary quotas total at most 60 candidates; the empty-candidate fallback supplies all graph edges and can exceed that budget. Status: wired, conditional on data, dependencies and configuration. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:26-169,172-314,415-462,465-659,662-779,782-967,1097-1432,1952-1976,2015-2148`.

>             similarity = compute_semantic_similarity(core_entity_id, concept_id)
>             scored_pairs.append((similarity, core_entity_id, concept_id))
> 
>     # Sort by semantic similarity descending
>     scored_pairs.sort(key=lambda x: x[0], reverse=True)
> 
>     # Select top-20 and create Chain objects
>     top_20_pairs = scored_pairs[:20]
> --- `DualGraph/deepresearch/baselines/knowledge_graph_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


RTE-6 — Completion judgment. Trigger: iteration end. Producer/consumer: judge model receives current retained outline; orchestrator consumes parsed ratings via threshold result. Failure to parse after retries assigns zero ratings. Early stopping can be disabled. Status: wired, not a correctness gate for each memory claim. SRC-1 `DualGraph/deepresearch/baselines/terminal_module.py:74-142`.

>     pass_thresholds = PASS_THRESHOLDS_HIGH if threshold_level == "high" else PASS_THRESHOLDS_LOW
>     return all(ratings.get(name, 0) >= threshold for name, threshold in pass_thresholds.items())
> --- `DualGraph/deepresearch/baselines/terminal_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


RTE-7 — Report context assembly and continuation. Trigger: final writing phase and each section. Selector parses outline citation IDs, fetches matching retained evidence, supplies section outline, selected content and the entire report prefix to the section model. This is automatic push into model context, even though the host internally invokes getters. Main explicitly disables direct graph-to-writer text; an API flag affords that extra input using evidence-linked edges. Final reference mapping is a separate output transformation. Status: wired ordinary evidence/prefix path; afforded optional direct-graph branch. SRC-1 `DualGraph/deepresearch/baselines/main.py:767-778`; `DualGraph/deepresearch/baselines/write_module.py:103-184,328-426`; `DualGraph/deepresearch/baselines/data_model.py:205-228`.

>         evidence_nodes = []
>         if knowledge_graph and evidence_ids:
>             for eid in evidence_ids:
>                 node = knowledge_graph.get_evidence_node_by_id(eid)
>                 if node:
>                     evidence_nodes.append(node)
> --- `DualGraph/deepresearch/baselines/write_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


>             if full_report.strip():
>                 user_prompt += f"PREVIOUS CONTENT:\n{full_report}\n\n"
> --- `DualGraph/deepresearch/baselines/write_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


RTE-8 — Persistence and human read-back. Trigger: graph update or human demo/live report use. Neo4j replace_graph clears the report projection before rewriting it. A configured main path calls GDS then copies returned cluster labels back to in-memory nodes. Human `demo` requests replay of saved outlines/search queries/report; live polling supplies newly appeared outlines and final report. No admitted run attests either. Database load_graph is a storage API with no call site in the pinned baselines subtree, so it is not an agent restart route. Status: wired serialization/demo/GDS call sites, live path limited by RTE-9; afforded graph load API only. SRC-1 `DualGraph/deepresearch/baselines/main.py:270-295,449-459,616-628`; `DualGraph/deepresearch/baselines/neo4j_kg_store.py:110-122,212-283,347-385`; `DualGraph/deepresearch/baselines/app.py:278-287,293-366,446-539`.

>     def replace_graph(self, kg: KnowledgeGraph, iter_idx: Optional[int] = None) -> None:
>         self.ensure_schema()
>         self.clear_report()
> --- `DualGraph/deepresearch/baselines/neo4j_kg_store.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


>         with open(outline_path, "r", encoding="utf-8") as f:
>             outline_text = f.read()
> 
>         outline_md = _outline_to_markdown(outline_text)
> 
>         async with cl.Step(name=f"{_ts()} Iteration {i} — Outline") as step:
>             step.output = outline_md
> --- `DualGraph/deepresearch/baselines/app.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


RTE-9 — Static entry/default defects: pinned default-route defects. First, both extraction helpers call `_extract_summary_from_content` when use_summary_only is true. The module neither defines nor imports it; scoped commit grep finds only the two call sites. The `data_model` wildcard import cannot supply this absent name. Defaults are true in create/update; main does not override them. Any nonempty evidence group entering that branch should raise NameError before the model extraction call; this is a static consequence, not an observed failure. Second, search_with_filtering_visited_urls passes its Pydantic Field default for bingsearch_num_results into Serper, whose `num_results * 2` arithmetic has no FieldInfo normalization (Bing has one). Third, app.py imports RunConfig from the local main module and live app constructs it with multiple keywords absent from its three-field dataclass. Under the shipped local module resolution this raises TypeError before process_single_report_og_kg is submitted; demo branches earlier and does not construct this configuration. These prevent assuming normal default execution, even though downstream memory code is inspectable. SRC-1 `DualGraph/deepresearch/baselines/knowledge_graph_module.py:1-23,1465-1473,1557-1567,1632-1634,1753-1755`; `DualGraph/deepresearch/baselines/main.py:17-23,424-432,589-597,837-851`; `DualGraph/deepresearch/baselines/search_module.py:91-100,164-170,206-212,693-695,757-770`; `DualGraph/deepresearch/baselines/app.py:24-39,410-419`.

>     # Build evidence text
>     evidence_texts = []
>     for en in evidence_nodes:
>         txt = (
>             _extract_summary_from_content(en.content)
>             if use_summary_only
>             else en.content
>         )
>         evidence_texts.append(f"EN{en.id}: {txt}")
> --- `DualGraph/deepresearch/baselines/knowledge_graph_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


>     bingsearch_num_results: int = Field(
>         default=5, description="Number of search results to return (1-10, default: 5)"
>     ),
> --- `DualGraph/deepresearch/baselines/search_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


>     payload = json.dumps({
>         "q": query,
>         "num": min(num_results * 2, 20),  # fetch more for deduplication
>         "gl": gl,
> --- `DualGraph/deepresearch/baselines/search_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


> @dataclass
> class RunConfig:
>     """All configurable run parameters, passed via function args (no module-level globals)."""
> 
>     kg_query_num: int = 10  # queries generated from KG per iteration
>     og_query_num: int = 10  # queries generated from OG per iteration
>     search_provider: str = "serper"  # bing / serper
> --- `DualGraph/deepresearch/baselines/main.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


>     cfg = RunConfig(
>         kg_query_num=kg_query_num,
>         og_query_num=og_query_num,
>         og_query_num_in_og_only=20,
>         enable_enrich_chain=True,
>         enable_explore_chain=True,
>         only_entity_concept_explore_chains=False,
>         use_lightrag_kg=False,
>         search_provider=search_provider,
>     )
> --- `DualGraph/deepresearch/baselines/app.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


> from main import (
>     process_single_report_og_kg,
>     RunConfig,
>     load_env_or_explain,
>     env_str,
>     env_bool,
>     env_float,
> )
> --- `DualGraph/deepresearch/baselines/app.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`


The supporting excerpts below attach jointly to RTE-2 (outline preservation/context), RTE-3 (summary admission), RTE-4 (semantic merge and graph projection), RTE-5 (chain reasons and structural probabilities), RTE-7 (report continuation), and RTE-8 (GDS feedback). They retain the specialist's evidence once, rather than duplicating it in lens overlays.

>     user_prompt = f"""
>     Root Query: {root_query}
>     
>     Current Outline: {outline}
>     
>     New Evidences: {evidence_str}
>     
>     Current Knowledge Graph: {knowledge_graph.to_json()}
>     
>     Language: {language}"""
> --- `DualGraph/deepresearch/baselines/outline_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>                 is_useful = crawl_result.get("is_useful", True)
>                 if is_useful:
>                     summary = crawl_result.get("summary", "")
>                     evidence = crawl_result.get("evidence", "")
>                     rational = crawl_result.get("rational", "")
>                     # TODO decide whether to include summary and rational based on requirements
>                     # content = f"**Summary**: {summary}\n**Evidence**: {evidence}\n**Rational**: {rational}"
>                     content = f"\n**Summary**: {summary}\n**Evidence**: {evidence}"
> --- `DualGraph/deepresearch/baselines/search_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>     # Append unvisited explore chains to prompt
>     for chain in chains:
>         if chain.is_visited:
>             continue
>         user_prompt += f"{chain.id}. {chain.content} -- Reason: {chain.reason}\n"
>     user_prompt += f"""Generate Search Queries in {language}."""
> --- `DualGraph/deepresearch/baselines/knowledge_graph_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>   5. **Justification Requirements**
>   - Each proposed merge group must include a concise, domain-specific justification.
>   - Justifications must reference conceptual meaning or domain knowledge, not just linguistic resemblance.
>   - Limit each justification to **under 50 words**.
> --- `DualGraph/deepresearch/baselines/prompt_lib/merge_knowledge_node.yaml` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>               if edge_key in new_edge_map:
>                   # Existing edge: only migrate evidence
>                   existing_edge = new_edge_map[edge_key]
>                   for evidence in edge.evidence_nodes:
>                       if not any(e.id == evidence.id for e in existing_edge.evidence_nodes):
>                           existing_edge.evidence_nodes.append(evidence)
>               else:
>                   # Create new edge with first relation name encountered
>                   new_edge_id = self.last_knowledge_edge_id + 1
>                   self.last_knowledge_edge_id = new_edge_id
>                   
>                   new_edge = KnowledgeEdge(
>                       id=new_edge_id,
>                       source_id=new_source_id,
>                       target_id=new_target_id,
>                       relation_name=edge.relation_name,  # Keep the first relation name
>                       evidence_nodes=edge.evidence_nodes.copy()  # Copy all evidence
> --- `DualGraph/deepresearch/baselines/data_model.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>   - Never remove or alter existing citation IDs.
>   - Insert new citation IDs only where the new evidence directly supports the point.
>   - New content should integrate naturally; avoid duplicating existing nodes.
>   ## Guidance of Citation & Semantic Integrity Principle
>   - Think of each cited line as "evidence-anchored". Once an id is attached, that line is tied to real-world findings.
>   - You cannot safely change what that line *means*—only how it’s *expressed* within semantic equivalence.
>   - If new evidence contradicts or reshapes a cited point, create a **new sibling or child node** to reflect nuance, rather than overwriting the anchored one.
> --- `DualGraph/deepresearch/baselines/prompt_lib/update_outline_by_kg.yaml` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>             # Estimate block connection probability matrix B
>             smoothing = 0.1
>             B_matrix: Dict[Tuple[str, str], float] = {}
>             for comm_pair, possible_pairs in community_pair_pairs.items():
>                 actual_edges = community_pair_edges.get(comm_pair, 0)
>                 prob = (actual_edges + smoothing) / (possible_pairs + 2 * smoothing)
>                 prob = max(0.0, min(1.0, prob))
>                 B_matrix[comm_pair] = prob
> --- `DualGraph/deepresearch/baselines/knowledge_graph_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>         section_content = response.content.strip()
> 
>         full_report += f"{section_content}\n\n"
> --- `DualGraph/deepresearch/baselines/write_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>         "knowledge_nodes": [
>           {
>             "node_id": f"n{node.id}",
>             "knowledge": node.knowledge,
>             "is_core_entity": node.is_core_entity,
>             # "cluster_id": node.cluster_id,
>             # "community_id": node.community_id,
>           }
>           for node in self.knowledge_nodes],
>         "knowledge_edges": [
>           {
>             "edge_id": f"e{edge.id}",
>             # "relation_name": edge.relation_name,
>             "representation": f"{id2node[edge.source_id].knowledge} - {edge.relation_name} -> {id2node[edge.target_id].knowledge}",
>           }
>         for edge in self.knowledge_edges],
>         # "semantic_clusters": self.semantic_clusters,  # 可选：包含语义聚类信息
>         # "community_list": self.community_list,  # 可选：包含社区发现信息
> --- `DualGraph/deepresearch/baselines/data_model.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>         def _sync_clusters_back_to_memory(
>             kg: KnowledgeGraph, node_id_to_cluster: Dict[int, str]
>         ) -> None:
>             if not node_id_to_cluster:
>                 return
>             for node in kg.knowledge_nodes:
>                 if node.id in node_id_to_cluster:
>                     node.cluster_id = str(node_id_to_cluster[node.id])
> --- `DualGraph/deepresearch/baselines/main.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

RTE-10 — Additional structural admission and report formatting checks. Graph insertion skips unknown endpoints but creates an edge before processing evidence mappings; unmatched/missing evidence does not reject the edge. Merge rewires on endpoint pair, retaining the first relation name and combining evidence, so semantic preservation is not guaranteed. Writer removes unmapped numeric citations and deduplicates references by URL; this does not check the cited proposition. Owner: local Python; trigger: model output; proposed change: graph/prose/reference state; admission: structural identity/JSON checks; rejection: malformed or unmapped elements, retries at outer roles; rollback: no whole-iteration transaction established. Guidance: extraction/evidence/merge prompts request support and semantic equivalence, not an executable entailment test. Implementation conclusion status: wired, conditional on reaching the branch. SRC-1 `DualGraph/deepresearch/baselines/data_model.py:325-388,462-519`; `DualGraph/deepresearch/baselines/write_module.py:24-99`.

>               # Create new edge
>               new_edge_id = self.last_knowledge_edge_id + 1
>               self.last_knowledge_edge_id = new_edge_id
>               edge_id_mapping[raw_edge_id] = new_edge_id
>               
>               # Add to edge list (initially no evidence)
>               self.knowledge_edges.append(KnowledgeEdge(
>                   id=new_edge_id,
>                   source_id=source_id,
>                   target_id=target_id,
>                   relation_name=relation,
>                   evidence_nodes=[]
>               ))
>               existing_edges[edge_key] = new_edge_id
> --- `DualGraph/deepresearch/baselines/data_model.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

>                 if nn not in seen_local:
>                     seen_local.add(nn)
>                     new_nums.append(nn)
>         if not new_nums:
>             return ''
> --- `DualGraph/deepresearch/baselines/write_module.py` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

Across RTE-2, RTE-3, RTE-4, RTE-5 and RTE-7, model proposals use shipped natural-language instructions plus current accumulated state. Parse/identity checks can veto structures; code does not independently veto false prose. Outline/current graph are replaced or mutated, iteration files retain snapshots, and exceptions/retries are recovery rather than semantic rollback. RTE-4 protects core nodes and merges concept groups; optional clustering errors are logged/skipped. Missing merge/usefulness rationale does not establish absent internal criticism: model processing remains uninspected. Retained chain reasons have a later model consumer on RTE-5. Prompt rules are individually readable/addressable; runtime rewriting of these source rules is not established.

### Claims

CLM-1 — Claimed co-evolving OutlineGraph and KnowledgeGraph separate report organization from fine-grained knowledge and guide targeted exploration. Conclusion status: claimed. SRC-1 `DualGraph/README.md:7`. The implementation's outline is text, not a traversed SkeletonGraph.

CLM-2 — Claimed stronger depth, breadth and factual grounding, including 53.08 RACE with GPT-5. Conclusion status: claimed; benchmark execution excluded. SRC-1 `DualGraph/README.md:7,98-109`.

> We introduce **DualGraph Memory**, an architecture that separates what the agent knows from how it writes via two co-evolving graph structures: an **Outline Graph (OG)** that governs report structure and a **Knowledge Graph (KG)** that stores fine-grained knowledge units. By analyzing KG topology alongside OG structural signals, DualGraph generates targeted search queries for more efficient and comprehensive iterative knowledge-driven exploration. DualGraph consistently outperforms state-of-the-art baselines in report depth, breadth, and factual grounding across three benchmarks, and reaches a **53.08 RACE score** on DeepResearch Bench with GPT-5.
> --- `DualGraph/README.md` @ `c090b7d57e3996c8900e86fecd16085b27e07f29`

### Evidenced absences

ABS-1 — No admitted retained recall-dependence experiment. Conclusion status: absent within the commissioned implementation/README boundary, which deliberately excludes generated example prose and benchmark reproduction. Inspected `DualGraph/README.md:7,98-109` and RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8 are code/documentary evidence only; none is a recalled-content intervention with candidate-linked measured result. This supports only the scoped faithfulness-tested=no field, not a claim that authors never tested the system.

ABS-2 — Summary helper definition/import absent. Conclusion status: absent. Commit-addressed grep for `_extract_summary_from_content` over `DualGraph/deepresearch/baselines` returns only two calls in `DualGraph/deepresearch/baselines/knowledge_graph_module.py:1469,1563`; module imports1-23 and wildcard source data_model inspected. Supports RTE-9 static NameError condition, not an observed failed run.

### Behavioral-authority paths

BAP-1 — Model roles consume automatically assembled outline/graph/evidence/history/report-prefix prompt content; knowledge is advisory, outline instructs, citation IDs select evidence. Horizon one report/section sequence. Source SRC-1 RTE-2, RTE-3, RTE-4, RTE-5, RTE-7 anchors. Delivery wiring established; behavioral activation/benefit uninspected.

BAP-2 — Orchestrator consumes query strings/chain selections/visited sets/ratings via Python objects and threshold checks; enforcing force for repeat filtering/loop termination, ranking force for candidates. Horizon current report. SRC-1 `DualGraph/deepresearch/baselines/main.py:704-763`; `DualGraph/deepresearch/baselines/knowledge_graph_module.py:2092-2126`.

BAP-3 — Human/UI and optional database consumers receive saved products; replay is human-requested, live display automatic when reachable. No established cross-report agent continuation. SRC-1 `DualGraph/deepresearch/baselines/app.py:278-366,446-539`; `DualGraph/deepresearch/baselines/neo4j_kg_store.py:212-283`.

## Runtime account

A caller supplies a dataset query or web message; CLI assigns report identity and initializes fresh state unless a numeric report Markdown filename already exists. This skip is file existence, not source/input freshness. The ordinary sequence is initial outline → OG queries → search/read/model summaries → graph extraction/merge → graph-planned queries → repeated acquisition/graph/outline updates and next-query planning → outline-only completion judging → sequential evidence-backed report writing → reference formatting/files. Python owns progression; models propose content/queries and score sufficiency; provider/search/read services execute external effects. The user chooses task/settings, not each proposed relation or query. The bounded iteration count and disable-early-stop option are runtime-client controls. Report IDs/usage/files aid observation, not full restart recovery. SRC-1 RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8.

Alternatives matter: Bing versus Serper; page-reader choice and optional Jina then snippet fallback; summary-only versus whole evidence extraction; optional direct graph writer flag (false in main); Neo4j disabled versus write/GDS branches; Python Leiden versus graph-service branch; destructive semantic-cluster merge opt-in; web live versus demo replay. Main GDS feeds cluster_id while operative community planning reads community_list/community_id, so successful label feedback does not establish active planning improvement. Main uses a fresh graph and never calls load_graph for resumption. Model APIs accept tool parameters in a wrapper, but inspected ordinary research roles do not run a provider-native tool execution loop. No universal sandbox/approval or isolated deployment guarantee follows from these interfaces.

Default and forcing cases, all static: (1) nonempty evidence entering default summary extraction encounters ABS-2; Serper default argument can fail arithmetic; web live constructs unsupported RunConfig keywords. Demo branches earlier. (2) a graph edge with valid endpoints but no valid evidence mapping remains available and may receive high enrich priority; semantic merge can combine differing relation labels. (3) a selected chain is marked visited before its queries run, and the end-of-round judge can terminate after next queries are planned. Selection history is not executed-search history. (4) a preexisting report filename skips changed inputs; final check-then-open is not atomic ownership and failures can leave intermediates. These conditions support route limits, not observed failure counts.

Guarantee owners are bounded. Python exact-set membership enforces duplicate query/URL suppression on the covered paths (invariant at the local check), not semantic redundancy. LLM prompts request support/preservation/85% equivalence (policy); JSON/identifier validation enforces shape only. Completion threshold conjunction is a control invariant given parsed ratings, not factual warrant. External API availability/output quality is a required service contract, uninspected. Search failures can yield no results, page failures can degrade to snippets, malformed model outputs retry, clustering errors are skipped, outer report failures return error and retain diagnostic/intermediate files. No transaction across all effects is established.

The workflow serves caller research requests and dataset batches, not an inspected training curriculum. No supplied expected-answer oracle enters ordinary decisions: root query, retrieved sources and self-generated outline are inputs to model judges, not a reference answer. Benchmarks in CLM-2 are outside this operating-mode boundary. Diagnosis/selection/admission are computational; no human factual veto is wired on the ordinary path. Runtime content can change future search within a report; improvement of task performance remains uninspected.

No dynamic check planned. Considered model-backed CLI/web execution, Neo4j restart and malformed-input probes; static branches suffice for the selected findings, while external dependencies/credentials and excluded services would prevent these from testing the admitted source-only claims. None was attempted.

Route read-back audit:

| Route | Immediate return / later consumer | Selection, expiry and effect limit |
|---|---|---|
| See RTE-1 | Fresh state or skip status; later research roles | File existence selection; no freshness invalidation; restart not loaded |
| See RTE-2 | Outline/query text; later planner/judge/writer | Complete current outline push; replace active outline, keep iteration file; activation unobserved |
| See RTE-3 | Accepted evidence; later graph/outline/writer | URL identity exclusion, max5 and model usefulness; failed URLs may retry; snippet lineage may be degraded |
| See RTE-4 | Mutated graph; later planner/updater | Batch5/defaultsummary, whole merge projection; overwrite/prune without semantic rollback; default defect |
| See RTE-5 | Chains/queries; later acquisition | Topology/count/embedding/model ranking; visited before execution; ordinary60count cap, fallback all edges, not token cap |
| See RTE-6 | Boolean stop; loop consumer | Rootquery+outline ratings; perround reset, no durable fact acceptance |
| See RTE-7 | Sections/final report; later section model and human | Evidence ID matching plus full prefix; no token budget/semantic citation enforcement |
| See RTE-8 | Files/database/demo response; human consumer | Named replay pull/live push; partial load afforded, no wired restart; old files not automatically invalidated |
| See RTE-9 | Error condition where entered | No memory consumption beyond affected branch; recovery per enclosing handler, successful run unobserved |
| See RTE-10 | Structured graph/reference state | Valid identity/URL conditions; later writer/planner; no truth-validation force |

## Lens scoping

### Memory/context scope

Full lens triggered by accumulated outline/evidence/graph, query/URL history, derived chains, embeddings/clusters, report prefix and products (OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8). All material read-back/admission routes RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8 inspected. Fresh specialist owns source-native findings/profile; static prompts excluded as memory, provider internals and observed behavior excluded.

### Epistemic scope

Full standalone lens, triggered by CLM-1, CLM-2 and truth-apt summary/graph/outline/report content. Assesses all material transformations, structural checks, stop decisions and authority routes inside SRC-1, with worker memory evidence integrated as generic records. No candidate run or benchmark admitted; six-block overlay below preserves architectural status separately from observed candidate state.

## Lens outputs

### Memory/context lens

The accepted specialist identifies within-report trace-fed context: page summaries, revised graph/outline/plans and growing report prefix are retained and delivered to later calls. This warrants trace_learning=yes at wired connection level, with tool-traces/trajectories, per-task horizon, online timing and natural-language/symbolic forms. It does not show successful default execution, behavioral activation, improved capacity or weight training. Observer logs do not qualify. Files and optional graph persistence increase availability without establishing cross-task agent learning.

Push consumers and selectors are explicit: updater receives whole current outline/new evidence/graph projection; planner uses topology, counts, embeddings, model selection and retained reasons; writer matches inline evidence IDs and receives complete prefix. Human demo is requested pull. Signal mapping remains not-determinable because controlled tokens cover coarse/identifier/embedding/model-judgment but omit topology/evidence counts; a partial set must not masquerade as complete. Curation maps narrowly: orphan pruning as decay, core flag as promotion, concept merging as dedup/consolidation, graph/outline mutation as evolve, missing-link proposals as synthesize. No time-based forgetting or truth promotion follows.

Graph lineage retains IDs/source evidence and merge mappings, but loses separate merge/usefulness rationale. Chain reasons are retained and read. Neo4j reconstructs only a projection; GDS cluster_id does not establish the same effects as community_list. ABS-1 bounds faithfulness-tested=no to admitted evidence. All findings are self-contained in shared records; the local report is provenance, not semantic clearance.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 for DualGraph revision/evidence layers and CLM-1, CLM-2 for claims. Question: what content is produced, checked, granted reliance and reused by the research workflow? Assessed families: acquisition, model transformations, graph maintenance/planning, structural checks, completion control, writing, persistence/replay. Unassessed external provider/service truth and benchmark routes prevent factual-performance and causal conclusions. No observed candidate is admitted.

#### 2. Epistemic-object inventory

Generic form/lineage/producer/consumer are inherited from canonical parts, not duplicated here. OBJ-10: substantive outline claims, intended report support; OBJ-13: source-derived summary/excerpts, intended evidence; OBJ-14: extracted/merged relational claims, intended planning knowledge; OBJ-18: missing-relation/probability/gap hypotheses, intended search targets; OBJ-20: report claims; OBJ-24: model quality ratings. All have truth-apt content but no candidate instance observed. OBJ-12, OBJ-15 and OBJ-21 supply attribution, not independent warrant. OBJ-16 and OBJ-17 are numerical access structures, not semantic truth guarantees. OBJ-11, OBJ-19, OBJ-6 and OBJ-25 govern operations. OBJ-22 is a carrier of content already inventoried; OBJ-23 is observer bookkeeping. Anchors and production details remain on these records.

#### 3. Authority-route ledger

Each row has one function. Unless stated otherwise architectural status is implemented, activation is the conditional invocation described on the canonical route, observed activation is uninspected, and SRC-1 plus the named route's anchors is the evidence. RTE-9 remains a prerequisite limitation. Epistemic license does not exceed the explicit scope below.

| Route / function | Target and content/update relation | Evaluator/condition, timing and result | Force, authority and limit |
|---|---|---|---|
| See RTE-3 — content transformation | OBJ-13; acquisition/import then summary indeterminate | Page/snippet and model usefulness/summary role during acquisition | BAP-1 advisory evidence per report; source warrant unknown/degraded by snippet or unverified paraphrase; CLM-2 not established |
| See RTE-3 — disposition/acceptance | OBJ-13; no content change | is_useful defaults true ifmissing; admits Summary/Evidence | Operational evidence admission, not truth acceptance; BAP-2; source fidelity untested |
| See RTE-4 — content transformation | OBJ-14; indeterminate extraction/semantic merge | Model plus structured node/edge mutation after each batch | BAP-1 planning representation; policy demands support/equivalence, implementation does not establish entailment |
| See RTE-10 — check/evidence production | OBJ-14, OBJ-15; no content change | Endpoint/evidence identity and parse checks | Structural consistency only; BAP-2; missing evidence can survive |
| See RTE-4 — retention | OBJ-14, OBJ-15; no content change | In-memory mutation and snapshot writes | Available to later planning; no independent factual acceptance or lifecycle integration |
| See RTE-2 — content transformation | OBJ-10, OBJ-11; indeterminate substantive rewrite/non-truth-apt plan update | Model consumes old outline/new evidence/KG | BAP-1 instructive/advisory; preservation/contradiction-sibling rule is policy only |
| See RTE-5 — content transformation | OBJ-18; ampliative conjecture | Graph missing-pair/embedding/community/SBM heuristic generates possible links/reasons | Candidate search targets, not factual edges; BAP-1/BAP-2 ranking; CLM-1 partly supported |
| See RTE-5 — operational admission/selection/consumption | OBJ-18, OBJ-19; no content change | Ranking plus model selectedchain IDs; valid-ID check and markvisited | Next searches/avoidance, no truth acceptance; pre-execution marking may exceed actual work |
| See RTE-6 — check/evidence production | OBJ-24; indeterminate quality assertion | Model rootquery+outline rubric after iteration | Quality/sufficiency opinion, no evidence-body validation; BAP-1 |
| See RTE-6 — disposition/acceptance | OBJ-25; no content change | Parsed ratings meet conjunction thresholds | BAP-2 stops loop, licenses report writing only; does not accept individual claims |
| See RTE-7 — content transformation | OBJ-20; indeterminate report composition | Section model from outline/selectedevidence/prefix | BAP-1 advisory content→BAP-3 final report; factual entailment untested |
| See RTE-10 — lineage/freshness/recovery | OBJ-21; non-ampliative reference formatting | URL dedup/numeric remapping/removal | Attribution formatting only; unmappedcitationsremoved, unsupportedclaimsnotrejected |
| See RTE-8 — retention | OBJ-22; no content change | Files/optionalDBwrites per iteration/report | BAP-3 availability, partialprojection, no factual acceptance |
| See RTE-8 — operational admission/selection/consumption | OBJ-22; no content change | Human demo selects stored artifacts | Replay forhuman, no establishedlateragentlearning |

No content-specific epistemic acceptance/lifecycle-integration route is established for graph hypotheses by these structural, ranking and completion mechanisms. This scoped conclusion does not rule out unobserved model reasoning.

#### 4. Per-object lifecycle disposition

OBJ-18, via RTE-5: transformation ampliative conjecture. Observation/anomaly: graph gaps and sparse evidence, implemented, no instance observed (SRC-1 RTE-5). Conjecture: candidate missing-link/probability/reason generation, implemented, no instance observed. Derived consequence: specific falsifiable consequence beyond a search target, not determinable, no instance observed. Test/evidence: RTE-3 can acquire more pages after selected queries, implemented, no instance observed; candidate-linked falsification/confirmation is not established. Acceptance: a factual evaluator/criterion/intended license for the proposed relation is not determinable; selected chain is only an operational search choice, no instance observed. Lifecycle integration after factual acceptance: not determinable, no instance observed. Missing evidence: candidate trace relating its stated proposition, test result and reliance change. Retention or planned use is not that phase.

OBJ-10, OBJ-13, OBJ-14, OBJ-20 and OBJ-24: transformation indeterminate. Possible preservation, ampliation or unsupported loss cannot be decided from prompts/code alone. RTE-2, RTE-3, RTE-4, RTE-6, RTE-7 preserve some source IDs/input lineage and impose structural or model-judgment checks, but no linked input/output candidate permits semantic entailment/preservation assessment. Needed evidence: exact source inputs, output claims and content-directed checking. All observed candidate states: no instance observed. Semantic-merge percentage and citation labels do not resolve this classification.

OBJ-12, OBJ-15 and OBJ-21: non-ampliative attribution/index reshaping under RTE-3, RTE-4 and RTE-10; discovery lifecycle not applicable. Warrant limited to the mapping executed, not truth of related prose. OBJ-16 and OBJ-17: explicit numeric/access derivations under RTE-5, with premise/vector/provider quality uninspected; discovery lifecycle not applicable to cluster membership as an algorithmic output. No lifecycle record for OBJ-11, OBJ-19, OBJ-6, OBJ-25 or OBJ-23: no candidate truth-apt output for these operational objects; relevant direct updates RTE-1, RTE-2, RTE-5, RTE-6, RTE-8. OBJ-22 merely retains already inventoried content; no new candidate lifecycle. Superseded containers inherit these part dispositions.

#### 5. System-claim versus route comparison

CLM-1 (SRC-1 README doctrine): implemented RTE-2/RTE-4/RTE-5 connect outline text and knowledge graph to subsequent search. No observed run or causal support. Supported: a connected co-updating design, with RTE-9 defaults and projection differences; no guarantee that retained relations are knowledge in the epistemic sense.

CLM-2 (SRC-1 README reported benchmark): implemented evidence-attribution, ranking and writing routes are compatible with its purpose; no admitted benchmark protocol/result, observed factual assessment or component intervention. Supported conclusion remains claimed performance only. No source-grounding or independent component benefit follows from code connection.

#### 6. Bounded conclusion

DualGraph acquires attributed material, transforms it through summaries/graph/outline/report roles, and uses the retained content to plan more searches and write sections. Its strongest inspectable controls govern shape, identity, search repetition and stopping. Missing-link candidates are proposals for acquisition; neither graph retention nor outline quality thresholds supplies a candidate-specific factual acceptance transition. Formal derivation of factual report claims is not established. Default defects further separate architecture from successful execution.

## Reconciliation

Fresh report identity/input/method/completion and full content checked. MEM-LIM-1 maps to RTE-9; MEM-ABS-1 maps to ABS-1. All canonical seed IDs preserve referents; heterogeneous object splits explicitly supersede containers and use new monotonic IDs. Profile references are expanded to the applicable parts below without changing assessment/basis/value sets.

All seven specialist issues accepted: coordinated web RunConfig check is not independent convergence; outline is text; ordinary writer direct graph delivery false; cluster summaries omitted from JSON and main GDS labels do not establish community-planning activation; usefulness/merge rationale loss differs from retained chain reasons; signal mapping remains incomplete; wired profile retains default-path defects. No substantive conflict or specialist report correction required. Memory findings and proposed profile remain specialist-owned; parent contributes runtime and epistemic overlays, not a second memory pass. Static source claims are never upgraded to observed behavior.

## Bounded synthesis

DualGraph implements an iterative research-report architecture with two differently used representations: an outline organizes writing and search, while an evidence-linked graph generates enrichment and missing-link search targets. The report writer ordinarily reads selected evidence and prior sections, not direct graph prose. This makes lineage/selection and the distinction between planned and executed search consequential.

For studying source-connected research planning, the frozen code exposes the relevant mechanisms and per-task trace-fed retention. For inferring a working default deployment, RTE-9 requires resolution first. For assessing factual performance or retained-memory benefit, CLM-2 and code inspection are insufficient; candidate-linked runs and controlled recall comparisons would change the assessment.

Formulation of tentative graph/search claims and their operative use are wired; content-directed criticism, resulting reliance revision and improved future capacity attributable to that criticism remain uninspected without candidate evidence. Addressability of graph labels/relations/outline points is wired, retention is wired, and neither establishes conjectural learning. A limited reflection route is wired: the report's own knowledge/search-progress representation changes with acquisition and steers later work (OBJ-18, OBJ-19, OBJ-6 via RTE-5); this is task-level self-representation, not an established revised theory of the workflow's organization. Reflective theory-building and self-improvement in measured future capacity remain uninspected. These are separate findings from the normalized trace-learning yes.

## Limitations

| Limitation | Affected records | Boundary / prevented conclusion | Resolving evidence |
|---|---|---|---|
| Default source defects | RTE-9, ABS-2 | No successful ordinary pipeline demonstrated | Corrected source and reached execution |
| External services/models | CMP-2, CMP-3, CMP-5, CMP-6 | No provider fixity, correctness or isolation guarantee | Pinned service contracts and relevant execution |
| No candidate run | RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7 | No activation, semantic preservation or criticism-linked improvement | Candidate-linked source/output/check traces |
| Benchmark/recall evidence excluded | CLM-2, ABS-1 | No performance or causal memory-benefit finding | Admitted protocol/results and interventions |
| Incomplete signal vocabulary | RTE-5 | Complete controlled selector set not representable | Suitable controlled taxonomy, no source gap |
| Optional partial persistence | RTE-8 | No exact restart/transaction/recovery guarantee | Wired continuation and failure/recovery checks |

## Verification and blockers

### Semantic verification

Checked profile scope against all scoped branches; read-back consumers/selectors and each qualifying trace-fed write are retained. Known sets include optional persistence and external-interface forms only within declared boundaries. Provider weights excluded, cached vectors classified as algorithm inputs. Signal uncertainty preserved. Generic IDs/part splits, evidence statuses, route ownership and every specialist issue checked. Quotations matched full pinned blobs and citation endpoints checked; source/worker/input hashes unchanged. No result depends on prior reviews or generated example prose. All observed/causal upgrades withheld; no unresolved evidence conflict.

### Deterministic validation

`commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-dualgraph-01/result.md` passed cleanly; final bytes are revalidated before publication. This is structural validation, not independent semantic review.

### Blockers

None.
