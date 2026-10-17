---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Cortex memory: retained text, graph, vectors, access-derived tiers and bounded read-back at the frozen repository revision."
run-id: AAS-2026-10-17-cortex-3da14ce55a2b-01
source-identity: https://github.com/abbacusgroup/cortex
reviewed-boundary: a51c2209eb6d26812c19c97aaade3cb64ccfc23c
---

# Cortex memory report

## Boundary and evidence

Cortex retains knowledge for later requested retrieval. This report includes capture and import, classification and linking, enrichment and inference, explicit editing and withdrawal, access feedback, diagnostic/query history, temporal snapshots, presentation and repair. It does not treat Cortex as the external agent's conversation manager. The frozen boundary is SRC-1 at `a51c2209eb6d26812c19c97aaade3cb64ccfc23c`, as declared in [boundary](boundary.md#boundary-and-evidence). External host compliance, provider internals, a deployed database and actual task benefit remain outside the available evidence.

The supplied runtime gives provisional route coverage; direct reads below add memory-specific distinctions rather than treating that coverage as an inspection ceiling. All added evidence is implementation or explicitly labelled doctrine/design from SRC-1. No target execution, test execution, live-provider call or production trace was used. There was no required source access gap. Available but uninspected UI details, backup internals and parts of evaluators are not negative evidence.

| Entry point or operation | Source paths in SRC-1 | Coverage and remaining limit |
|---|---|---|
| CLI dispatch, direct reads, registration and operator maintenance | `src/cortex/cli/main.py` | Direct symbol/command inventory and doctor bodies; supplied [RT-RTE-direct-import](runtime.md#rt-rte-direct-import), [RT-RTE-transport-control](runtime.md#rt-rte-transport-control). Direct read records access; no hook-based host context injection established. |
| MCP capture, classify, link, pipeline, update/delete/unlink | `src/cortex/transport/mcp/server.py`; `src/cortex/pipeline/orchestrator.py` | Direct handler/stage reads; annotations on [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) and [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge). Public/admin registration affects exposure, not semantic trust. |
| Obsidian/v1 imports | `src/cortex/pipeline/importer.py` | Direct Obsidian body, dedup and property reads; v1 route from supplied runtime. [RT-RTE-direct-import](runtime.md#rt-rte-direct-import). Initial author/human approval and complete source preservation differ by branch. |
| Document, summary, metadata and FTS storage | `src/cortex/db/content_store.py`; `src/cortex/db/store.py` | Direct schema, update/delete, embedding/config/log and unified mutation reads; [MEM-OBJ-documents](#mem-obj-documents), [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-tier](#mem-obj-tier). FTS triggers are database hooks, not agent lifecycle hooks. |
| Normalize/link/enrich and inference | `src/cortex/pipeline/normalize.py`; `src/cortex/pipeline/link.py`; `src/cortex/pipeline/enrich.py`; `src/cortex/pipeline/reason.py` | Direct first three; rule execution from [RT-OBJ-inference-rules](runtime.md#rt-obj-inference-rules), [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution). [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-OBJ-relationships](#mem-obj-relationships). No derivation journal established. |
| Search/context/document/dossier/list/graph/export/synthesis | `src/cortex/retrieval/engine.py`; `src/cortex/retrieval/presenters.py`; `src/cortex/retrieval/graph.py`; `src/cortex/transport/mcp/server.py` | Direct engine and all presenters, scoped tool reads; graph operations partly supplied runtime. Annotation on [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). Selectors are not interchangeable; synthesis is returned, not automatically retained. |
| Read/feedback, access promotion and optional learner APIs | `src/cortex/retrieval/learner.py`; `src/cortex/transport/mcp/server.py` | Direct; [MEM-RTE-access-promotion](#mem-rte-access-promotion), [MEM-OBJ-access-count](#mem-obj-access-count), [MEM-OBJ-retrieval-weights](#mem-obj-retrieval-weights). No shipped adaptation caller found for persisted weights. |
| Status alerts and advanced reasoning | `src/cortex/retrieval/presenters.py`; `src/cortex/pipeline/advanced_reason.py` | Direct alert and structural/staleness bodies; [MEM-RTE-issue-delivery](#mem-rte-issue-delivery). Pattern/gap implementation partially supplied runtime and evaluator searches. No automatic correction established. |
| Temporal history | `src/cortex/pipeline/temporal.py`; `src/cortex/db/store.py` | Direct complete temporal module and update path; [MEM-OBJ-document-versions](#mem-obj-document-versions). Exposed library capability, not a wired agent history-reading route. |
| Query trail and dashboard/REST consumers | `src/cortex/db/content_store.py`; `src/cortex/transport/mcp/server.py`; `src/cortex/dashboard/server.py`; `src/cortex/transport/api/server.py` | Direct query log/trail and dashboard call search; remaining facades from supplied runtime. [MEM-OBJ-query-log](#mem-obj-query-log). No automatic query-to-weight transformation established. |
| Backup/restore, doctor and diagnostic memory | `src/cortex/cli/backup.py`; `src/cortex/cli/main.py`; `src/cortex/transport/mcp/server.py` | Backup/restore from supplied [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge); doctor directly read; debug tool inventory inspected, detailed debug bodies uninspected. Debug names concern sessions/process allocation, not evidence of semantic learning. Successful recovery and diagnostic payload retention unestablished. |
| Prompts, ontology and evaluations | `llms.txt`; `src/cortex/services/llm.py`; `src/cortex/ontology/cortex.ttl`; `benchmarks/conftest.py`; `tests/retrieval/test_learner.py` | Direct agent doctrine, classification/relationship prompts, benchmark fixture and evaluator searches; ontology and optional model recipes from supplied boundary/runtime. Fixtures supply synthetic/deterministic evaluation, not live benefit. Full evaluator audit and model-recipe activation not established. |

## Core ideas

1. **Capture precedes processing.** Raw/caller-authored text is retained before optional classification, linking and inference. A supplied summary bypasses internal classification; a disabled pipeline bypasses all four stages. The resulting store is not uniformly curated or independently verified. See [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) and its annotation.
2. **Different retained parts have different consumers.** Natural-language bodies and summaries inform hosts; graph predicates influence queries and inference; dense vectors influence candidate retrieval; access counts influence tier metadata. One database container does not give these parts the same lineage or authority. See the parts of [RT-OBJ-store](runtime.md#rt-obj-store) below.
3. **Compact context is a projection, not conversation compaction.** Request-driven ranking and field selection keep bodies out of the briefing response while leaving full documents reachable by ID. Document count and character slices are the inspected budgets; no strict whole-response token budget follows. See the annotation on [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context).
4. **The strongest wired trace-fed adaptation is access-to-tier.** Reads and positive relevance signals increment counters; ten accesses can promote a document. This result is subsequently displayed and preserved by enrichment, but hybrid scoring does not use tier. Persisted weight setters and miss detection do not by themselves close an adaptive ranking loop. See [MEM-RTE-access-promotion](#mem-rte-access-promotion) and [MEM-CLM-learning-scope](#mem-clm-learning-scope).
5. **Detection does not imply withdrawal.** Contradictions, repeated fixes and stale dependencies can be reported without deleting, demoting or replacing the implicated knowledge. Supersession is a graph relation, not a universal retrieval exclusion. See [MEM-RTE-issue-delivery](#mem-rte-issue-delivery) and [MEM-OBJ-relationships](#mem-obj-relationships).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-documents
Label: documents content and raw_markdown

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

The SQLite `documents` rows retain title, content and raw_markdown as natural-language text. The graph receives title/content too, but unified reads use SQLite content and attach graph relationships. Text has informational authority at human/model consumers; the FTS index gives lexical units fixed search semantics rather than making the prose executable instructions. This is the text part of the supplied store, not another store declaration. SRC-1, `src/cortex/db/content_store.py`, `src/cortex/db/store.py`.

Lineage ranges from explicit caller text and template rendering to imported files/rows. `captured_by` identifies an entry channel, not authenticated authorship or human approval. Raw Markdown is not always an untouched original: Store.create defaults it to content, and pipeline-based Obsidian import passes the stripped body. The no-pipeline Obsidian branch separately supplies original file content as raw_markdown. Neither branch establishes an original conversational trace, reasoning history or source signature. Later document reads/export can expose retained content; briefing omits it. SRC-1, `src/cortex/pipeline/importer.py`, `src/cortex/pipeline/orchestrator.py`, `src/cortex/retrieval/presenters.py`.

> raw_markdown=raw_markdown or content,
> --- `src/cortex/db/store.py`

> content=body,
> raw_markdown=content,
> project=project,
> --- `src/cortex/pipeline/importer.py`

#### MEM-OBJ-summary
Label: summary

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

`documents.summary` is retained natural-language derived or caller-supplied metadata, separate from the body and raw_markdown. It can originate from the caller, frontmatter, internal model classification or the model-unavailable fallback. Normalization reuses any nonempty existing summary rather than recomputing it; re-running the pipeline therefore does not guarantee a refreshed summary after a content edit. Public classify can replace it directly. Internal confidence and MCP's fixed 0.9 for supplied summaries are not truth verification. SRC-1, `src/cortex/pipeline/normalize.py`, `src/cortex/services/llm.py`, `src/cortex/transport/mcp/server.py`.

The summary is operative at BriefingPresenter, DossierPresenter and the synthesis model-input builder. Briefing sends summary or title fallback, not full evidence or arbitrary graph properties such as a decision rationale. Summarization requests a short account; it does not establish retention of all reasons, faithful derivation or an independent warrant. If a rationale remains in the body, full read can recover that body, but that is a separate requested route. The classification prompt can extract rationale as a graph property; its existence does not make the briefing carry it. SRC-1, `src/cortex/retrieval/presenters.py`, `src/cortex/services/llm.py`; closest supplied route [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context).

> Respond with ONLY a JSON object (no markdown, no explanation):
> --- `src/cortex/services/llm.py`

> - decision: rationale, alternatives, chosen, decisionStatus
> --- `src/cortex/services/llm.py`

The existing-summary bypass and summary/title projection are quoted in [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline) and [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context).

#### MEM-OBJ-tier
Label: tier and classification metadata

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

The SQLite row's symbolic type, project, tags, tier, stage, confidence and timestamps govern filters, display and maintenance. Tags/project labels contain text but receive fixed matching/filtering roles here. Graph properties partly duplicate metadata; direct component writes can diverge. Archive/recall/reflex name metadata states, not separate physical stores or host instruction priorities. Type/project filter later candidates, created_at affects recency; confidence is used by enrichment, not an inspected truth oracle. SRC-1, `src/cortex/db/content_store.py`, `src/cortex/retrieval/engine.py`, `src/cortex/pipeline/enrich.py`.

Enrichment maps nonempty summary plus positive confidence to recall, otherwise archive, while preserving reflex. Access promotion separately writes SQLite tier. Briefings expose tier and later enrichment reads it; the hybrid score consumes keyword, semantic, graph and recency scores, not tier or access_count. Staleness and connection counts returned by enrichment are not included in its persisted update dictionary. Thus the stage's output labels do not establish a durable staleness field or automatic expiry. SRC-1, `src/cortex/pipeline/enrich.py`, `src/cortex/retrieval/learner.py`, `src/cortex/retrieval/engine.py`.

> if current_tier == "reflex":
>     return "reflex"
> --- `src/cortex/pipeline/enrich.py`

> updates: dict[str, Any] = {
>     "tier": tier,
>     "pipeline_stage": "enriched",
> }
> --- `src/cortex/pipeline/enrich.py`

#### MEM-OBJ-relationships
Label: Graph objects, entities and relationships

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

Oxigraph stores symbolic object/entity identifiers, type/property assertions, mentions and typed relationships. Descriptive property values may be natural-language text; their presence is distinct from executable predicate semantics. Lineage includes explicit links and properties, imported wiki-links/tags, model-discovered links and rule-inferred triples. Entity resolution creates/reuses names and adds mentions; LinkStage rejects unknown predicates, self-links and nonexistent endpoints. Model confidence thresholds do not validate semantic truth. SRC-1, `src/cortex/pipeline/link.py`, `src/cortex/pipeline/importer.py`; formal rule source and executable force are already [RT-OBJ-inference-rules](runtime.md#rt-obj-inference-rules) and [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution).

Graph connectivity boosts hybrid ranking; mentions select dossier/entity results; predicates select contradiction/staleness checks and further inference. These are fixed software consumers. A retained `supersedes` or `contradicts` relation need not remove either text from ordinary search. No premise-to-derived-edge provenance or automatic truth-maintenance retraction is established by the supplied additive rule route. Explicit unlink/delete offer withdrawal, but later reason runs can derive a removed inference again if premises still match. SRC-1, `src/cortex/retrieval/engine.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/pipeline/advanced_reason.py`; [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge).

> # Verify both objects exist
> if not self.store.content.get(from_id) or not self.store.content.get(to_id):
>     logger.debug("Skipping relationship — object not found")
>     continue
> --- `src/cortex/pipeline/link.py`

#### MEM-OBJ-embeddings
Label: embeddings

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

SQLite's embeddings table stores dense distributed numerical representations as BLOBs with model-name/dimension metadata. Normalization embeds title plus the first 2000 body characters, not the entire document, summary rationale or graph. It replaces the vector for the ID when generation succeeds. This derived representation is not provider weights, a readable summary or a retained trace of model reasoning. Providers are separately [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer) and [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider); no parameter update or exact artifact pin follows from a model-name column. SRC-1, `src/cortex/pipeline/normalize.py`, `src/cortex/db/content_store.py`.

Later semantic search embeds the query, loads at most 10000 stored vectors and uses cosine similarity. The read returns doc_id, embedding and dimensions, omitting stored model identity; equal dimension alone does not prove compatible models. Different dimensions yield zero similarity, corrupt bytes are skipped, and provider failure disables that signal. Update/classify handlers do not regenerate vectors; an explicit pipeline run can regenerate one but may keep the existing summary. Direct CLI pipeline construction lacks the MCP embedding provider, qualifying uniform coverage. SRC-1, `src/cortex/retrieval/engine.py`, `src/cortex/transport/mcp/server.py`; [RT-RTE-direct-import](runtime.md#rt-rte-direct-import).

> text = f"{title}\n{content[:2000]}"
> --- `src/cortex/pipeline/normalize.py`

> "SELECT doc_id, embedding, dimensions FROM embeddings LIMIT ?",
> --- `src/cortex/db/content_store.py`

#### MEM-OBJ-access-count
Label: access_count and last_access

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

SQLite config keys `access_count:<id>` and `last_access:<id>` retain symbolic aggregate access metadata, not document content. A successful full read or positive feedback increments the count and stamps current time. These are mixed trace origins: requesting a document is implicit behavior, whereas relevant=true is an explicit caller judgment whose human/model provenance is unresolved. Last-access time and cumulative count discard individual reasons and event histories. SRC-1, `src/cortex/retrieval/learner.py`, `src/cortex/transport/mcp/server.py`.

The live consumer is the promotion threshold and, through an exposed library operation, optional inactivity adjustment. Count also returns with feedback. This is a distinct store part and the retained input to [MEM-RTE-access-promotion](#mem-rte-access-promotion), not a second identity for [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context).

> self.store.content.set_config(count_key, str(current + 1))
> --- `src/cortex/retrieval/learner.py`

#### MEM-OBJ-query-log
Label: query_log

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

SQLite query_log retains timestamp, tool, JSON parameters/result IDs, result count, duration and session_id. These are symbolic raw search-event records with natural-language query values, not a derived policy. Nonempty hybrid searches log their query and selected IDs after ranking; this call does not supply a session identity. Blank queries return before logging. The admin query-trail tool reads the newest records with an upper cap of 1000, and is documented for the dashboard trail page. This is an actual diagnostic read-back consumer, not proof of automated adaptation. SRC-1, `src/cortex/db/content_store.py`, `src/cortex/retrieval/engine.py`, `src/cortex/transport/mcp/server.py`.

> self.store.content.log_query(
>     tool="hybrid_search",
>     params={"query": query, "doc_type": doc_type, "project": project},
>     result_ids=[r["id"] for r in results],
>     duration_ms=duration_ms,
> )
> --- `src/cortex/retrieval/engine.py`

> return store.content.get_query_log(limit=capped)
> --- `src/cortex/transport/mcp/server.py`

#### MEM-OBJ-retrieval-weights
Label: retrieval_weights

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

The SQLite config value `retrieval_weights` is JSON symbolic numeric coefficients. LearningLoop.update_weights persists supplied weights; get_weights loads JSON or defaults and reset_weights stores defaults. Who initially supplies a nondefault value is unresolved without a caller; naming these APIs does not establish automatic optimization. This retained part is distinct from the engine's in-memory weights. SRC-1, `src/cortex/retrieval/learner.py`.

The exposed library can return persisted values, but inspected server construction instantiates RetrievalEngine without learner.get_weights. The engine uses supplied constructor weights or defaults. A source-wide caller search found weight APIs only in their learner definitions/reset and tests, not an operative bridge. Thus this is persistence/reload capability, not an established later ranking-consumer route. See [MEM-ABS-adaptation-wiring](#mem-abs-adaptation-wiring) and [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). No interpretation as distributed model parameters is warranted. SRC-1, `src/cortex/retrieval/engine.py`, `src/cortex/transport/mcp/server.py`.

> self.store.content.set_config(WEIGHTS_CONFIG_KEY, json.dumps(weights))
> --- `src/cortex/retrieval/learner.py`

> engine = RetrievalEngine(store, embedding_provider=embedding_provider)
> --- `src/cortex/transport/mcp/server.py`

#### MEM-OBJ-document-versions
Label: document_versions

Part of: [RT-OBJ-store](runtime.md#rt-obj-store)

TemporalVersioning stores old SQLite documents rows as JSON in document_versions, with doc ID, version number and validity timestamps. Its payload mixes natural-language fields with symbolic row metadata; version metadata is an index, not the content itself. This is an unchanged historical row checkpoint, not model-produced compaction or a full graph/vector/config checkpoint. Store.update snapshots before changing the row. Direct normalize/classify/enrich/learner writes bypass it. SRC-1, `src/cortex/pipeline/temporal.py`, `src/cortex/db/store.py`; closest supplied container [RT-OBJ-store](runtime.md#rt-obj-store).

get_version/get_state_at/list_versions expose library read capabilities. The source search did not find a shipped later consumer of those read methods. Their existence does not establish agent-facing historical read-back or version rollback. In particular, get_state_at falls back to a current row whose created_at precedes the query time; incomplete snapshot coverage prevents a general historical-accuracy guarantee. Versions have no declared foreign-key cascade to the current document, and ContentStore.delete only deletes the current row. Therefore deletion is not demonstrated erasure of historical content, query traces or access keys. SRC-1, `src/cortex/pipeline/temporal.py`, `src/cortex/db/content_store.py`.

> data.get("updated_at", data.get("created_at", now)),
> --- `src/cortex/pipeline/temporal.py`

> "SELECT * FROM documents WHERE id = ? AND created_at <= ?",
> --- `src/cortex/pipeline/temporal.py`

### Routes

#### MEM-RTE-access-promotion
Label: Access-derived tier promotion

Part of: [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Read returns the already rendered document; feedback returns relevance and updated access count.
- Later read-back: Persisted count feeds later record_access invocations; promoted SQLite tier reaches subsequent context/document/list output and later enrichment's reflex-preservation branch.
- Delegated visibility: The host sees a document or feedback response; no worker/model is invoked by promotion itself.
- Selection predicate: Successful MCP full read or relevant=true selects one ID; cumulative count at least ten invokes promotion if the current document exists and is not already reflex.
- Invalidation or expiry: Counts accumulate; library adjust_tiers can demote inactive reflex rows, but no shipped scheduled caller was found. Explicit edits, deletes and restore can change state.
- Activation or effect: Fixed code writes counters and possibly tier; this is durable metadata adaptation, not established tier-dependent hybrid ranking or changed external task behavior.
- Evidence limits: Static wiring only; no observed promotion, retrieval gain or human provenance of feedback. The read result is rendered before its access event, so a threshold-crossing read need not display the newly promoted tier until a later read.

Owner/proposer/decider: fixed LearningLoop code converts an access event to a tier change; the caller proposes a relevance signal but does not approve each resulting write. Negative feedback returns recorded status without decrementing count, storing a negative signal or withdrawing content. The criterion is usage frequency, not an independent answer oracle; mode is open use, not a bounded reference-answer experiment. Enrichment supplies the fixed tier policy; library adjust_tiers uses at most 1000 listed objects and a default 30-day inactivity interval. Recovery is explicit state editing/restoration rather than an inspected promotion rollback journal. SRC-1, `src/cortex/retrieval/learner.py`, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/enrich.py`.

> # Check for promotion threshold
> if current + 1 >= 10:
>     self._maybe_promote(obj_id)
> --- `src/cortex/retrieval/learner.py`

> if doc and doc.get("tier") != "reflex":
>     try:
>         self.store.content.update(obj_id, tier="reflex")
> --- `src/cortex/retrieval/learner.py`

Learning: retained usage changes later metadata and a subsequent enrichment decision. Improved capacity for future action, measured gain and causal attribution remain unestablished; the function name alone supplies none of those conclusions.

#### MEM-RTE-issue-delivery
Label: Requested issue and alert delivery

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Admin status includes current alerts; admin reason returns contradiction, pattern, gap and staleness findings.
- Later read-back: Each invocation selects previously retained documents, relationships and mentions; returned findings are not automatically persisted as a successor knowledge object in the inspected handlers.
- Delegated visibility: MCP/facade caller receives issue dictionaries and object IDs, not a delegated critic's hidden state.
- Selection predicate: Requested status invokes AlertPresenter; requested reason invokes AdvancedReasoner.run_all. Rules inspect graph contradictions, repeated recent fixes, gaps or stale dependencies, with bounded object listings.
- Invalidation or expiry: Findings are recomputed from current state; edits/unlinks/deletes can change later findings. A finding itself does not invalidate the underlying document or exclude it from retrieval.
- Activation or effect: Software selects and displays warnings; content correction, reclassification or withdrawal requires another caller action in the inspected route.
- Evidence limits: No observed notification, critique uptake or resolved contradiction. Proactive naming does not establish unsolicited delivery or a scheduler.

Distinct identity: [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) spans mutation/recovery, while this route isolates read-only issue selection through both status and reason; it is not another declaration of that combined route. SRC-1, `src/cortex/retrieval/presenters.py`, `src/cortex/pipeline/advanced_reason.py`, `src/cortex/transport/mcp/server.py`.

The caller triggers open diagnosis, code decides which matches to report, and a human or external agent decides whether to act. The runtime's warning about structural versus semantic contradiction detection holds: the body invokes structural checks despite the broader docstring. No expected-answer oracle is used by these live checks. Detection does not test or revise the shipped inference rules; their theory assessment remains in [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge). The retained objects may carry domain reasons, but this route does not establish a retained criticism-to-successor-rule chain.

> stats = store.status()
> alerts = AlertPresenter(store).render()
> stats["alerts"] = alerts
> --- `src/cortex/transport/mcp/server.py`

> findings.extend(self._structural_contradictions())
> return findings
> --- `src/cortex/pipeline/advanced_reason.py`

The three staleness notions differ: EnrichStage checks a dependency's pipeline_stage for superseded; AlertPresenter checks dependency tier for archive; AdvancedReasoner checks incoming supersedes relationships. They cannot be collapsed into one invalidation guarantee. SRC-1, `src/cortex/pipeline/enrich.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/pipeline/advanced_reason.py`.

> if dep and dep.get("tier") == "archive":
> --- `src/cortex/retrieval/presenters.py`

> if dep and dep.get("pipeline_stage") == "superseded":
> --- `src/cortex/pipeline/enrich.py`

### Claims

#### MEM-CLM-learning-scope
Label: Learning and proactive labels versus consumers

Source doctrine claims a learning loop that improves retrieval and asks callers to use relevance feedback for future search. The inspected mechanism establishes access-derived tier writes and a separately persisted weight API, not an automatic learned-ranking bridge. Likewise AlertPresenter calls itself proactive, but the inspected server creates it in requested status handling. These are bounded qualifications, not a claim that Cortex lacks retained learning-related state or that an external integrator cannot wire these capabilities. SRC-1, `src/cortex/retrieval/learner.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/transport/mcp/server.py`, `llms.txt`; [MEM-RTE-access-promotion](#mem-rte-access-promotion), [MEM-ABS-adaptation-wiring](#mem-abs-adaptation-wiring), [MEM-RTE-issue-delivery](#mem-rte-issue-delivery).

> - Tunes ranking weights based on feedback
> --- `src/cortex/retrieval/learner.py`

> 6. Use `cortex_feedback` to improve future search results
> --- `llms.txt`

> """Proactive notifications — contradictions, patterns, staleness."""
> --- `src/cortex/retrieval/presenters.py`

### Evidenced absences

#### MEM-ABS-adaptation-wiring
Label: Missing shipped ranking-adaptation bridge

- implementation conclusion status: absent

At SRC-1 revision `a51c2209eb6d26812c19c97aaade3cb64ccfc23c`, symbol searches for get_weights/update_weights/detect_miss/adjust_tiers across `src/`, `tests/` and `benchmarks/` found definitions/internal reset and unit-test use, but no production call wiring those APIs to search, feedback or a scheduler. A second search across `src/`, `pyproject.toml`, `deploy/`, `resources/` and `llms.txt` for hook/reflex/temporal/learner symbols found no such bridge. Direct server/engine/learner reads substantiate this bounded absence: engine construction does not load persisted weights; feedback calls only record_access on a positive signal. This prevents attributing shipped automatic weight tuning, miss-sequence learning or scheduled inactivity demotion. It does not prevent an external library consumer supplying weights or calling adjustment explicitly. SRC-1, `src/cortex/retrieval/learner.py`, `src/cortex/retrieval/engine.py`, `src/cortex/transport/mcp/server.py`; [MEM-OBJ-retrieval-weights](#mem-obj-retrieval-weights), [MEM-RTE-access-promotion](#mem-rte-access-promotion). The quoted constructor and threshold passages above support the bounded conclusion; the supplied runtime never claimed this bridge was wired.

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline)

Memory-specific chain: caller content/template → retained body → optional classification summary/type/properties → resolved mentions and discovered links → enrichment tier → formal graph derivations → later retrieval/projection. All are SRC-1 implementation paths in `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/link.py`, `src/cortex/pipeline/enrich.py`. The supplied route's ingestion/bypass quotations establish that initial retention is not gated on processing success.

Admission control is not authorship: a generic caller supplies text and can preclassify it, fixed software handles parsing and structural checks, an optional model proposes classification/relationships, and none of those steps establishes a human approving each meaning. Normalization requests extraction rather than criticism of the original claims. Text remains in place; summary and vector derivation do not replace a host conversation. Rationale can be retained as caller content or a graph property, but no universal reason-preserving transformation is established. Graph properties and vectors also do not share the temporal snapshot coverage of Store.update. [MEM-OBJ-documents](#mem-obj-documents), [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-relationships](#mem-obj-relationships), [MEM-OBJ-embeddings](#mem-obj-embeddings).

#### On [RT-RTE-direct-import](runtime.md#rt-rte-direct-import)

Import lineage is filesystem Markdown/frontmatter or legacy database rows, not necessarily agent interaction traces. Original authors and per-item human approval remain unresolved; operator invocation alone supplies neither. Obsidian dedup writes its content-hash key before later creation, and title fallback applies only to prior imported documents. Rejected/failed entries can therefore leave a durable admission marker. No automatic source-file resynchronization or removal is established by this route. SRC-1, `src/cortex/pipeline/importer.py`; its hash/skip passage is supplied by the runtime, and the raw-versus-stripped branch is recorded in [MEM-OBJ-documents](#mem-obj-documents).

#### On [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context)

Request and delivery direction: caller supplies topic/query/ID; code selects retained state and returns it through MCP/facades. This is requested retrieval, not automatic unsolicited injection. Working-context control applies to the delivered projection: briefing excludes full bodies and relationships, retains summaries/IDs, and permits explicit full reload. The host owns whether any response enters a model invocation. It does not pop an isolated agent frame or remove old host turns. A returned ID is only an address for a later tool request, not an automatically followed pointer in a context window. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/retrieval/engine.py`, `src/cortex/retrieval/presenters.py`.

Selection/budget distinctions: hybrid retrieval uses requested limit, keyword candidates up to 3× limit, optional semantic candidates up to 3× limit from at most 10000 vectors, then graph and created-at scores. The context tool defaults to ten results. Briefing's approximate tokens/doc comment is not a truncation implementation: summary length is not capped by the presenter. Dossier exact-matches an entity before FTS fallback, shows at most ten summaries but can include a larger timeline/related-entity set. Synthesis lists at most 500 objects, time/project-filters, displays at most 30 source descriptors, and sends at most twenty summary/title records to the LLM. A 3–5-sentence request is guidance, not a hard output cap. Synthesis is returned transiently; persistence would need a separate capture. These paths read retained content but do not all share the hybrid selector. SRC-1, `src/cortex/retrieval/presenters.py`; [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-embeddings](#mem-obj-embeddings).

> for obj in objects[:20]
> --- `src/cortex/retrieval/presenters.py`

> f"brief narrative (3-5 sentences):\n\n{summaries}"
> --- `src/cortex/retrieval/presenters.py`

Authority remains the supplied [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery): informational tool output, not enforced host instruction priority. The actual internal synthesis model receives selected summaries as content under a shipped request; that delivery establishes a model-input dependency, not faithful use or benefit. No access-count signal or tier coefficient appears in the inspected hybrid score.

#### On [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge)

Write and withdrawal coverage: caller classify directly replaces selected metadata and resolves supplied entities; admin update writes nonempty content fields through Store.update and snapshots the prior SQLite row. Both can leave old summary/vector/graph facts unless separately refreshed. Public reprocessing normalizes an existing summary without reclassification. Delete removes current graph/content objects; unlink removes a selected relation; neither handler constitutes retained semantic criticism or a proof that all historical copies were erased. The library temporal APIs offer inspection capability but no shipped consumer was found. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/db/store.py`, `src/cortex/db/content_store.py`, `src/cortex/pipeline/temporal.py`; [MEM-OBJ-document-versions](#mem-obj-document-versions).

Operator doctor repair rebuilds FTS, runs inference and checkpoints the SQLite WAL after a server-running check. This restores search/inference machinery under fixed policies; it does not criticize body meaning or revise rule content. Its admission is operator invocation plus structural checks; a generic invoking process is not proof of a human approving each added inference. Backup/restore remains the supplied whole-store recovery route, not an inferred per-document criticism/revision protocol. SRC-1, `src/cortex/cli/main.py`, `src/cortex/db/content_store.py`; [RT-CLM-store-consistency](runtime.md#rt-clm-store-consistency).

> result = content.fts_rebuild()
> --- `src/cortex/cli/main.py`

## Write side

Acquisition has at least three distinct controls: ordinary capture (caller/template plus optional model processing), imports (file/row mappings with dedup/skip gates), and explicit edits/classification/linking (caller-selected mutations). Starting one route does not establish human approval of every output. Unknown initial authorship coexists with known software transformations. The annotations retain the admission and alternate branches rather than assigning the whole store one uniform control.

Processing makes derived summaries, vectors, entity mentions, relation assertions and tier metadata. Raw-to-derived-to-consumer chains are separately [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-OBJ-relationships](#mem-obj-relationships) and [MEM-OBJ-tier](#mem-obj-tier). These are knowledge transformations, not necessarily trace-fed experience learning: their inputs can be ordinary imported or caller-authored content. No universal retained reasons-to-later-consumer chain follows from type names such as fix, lesson or synthesis. Formal derivations have executable rule authority as already recorded by runtime; derived assertions need not carry a rationale/proof tree.

The trace-fed positive witness is [MEM-RTE-access-promotion](#mem-rte-access-promotion): mixed implicit accesses/explicit relevance → durable counters → tier update → later tier display and enrichment decision. Negative relevance does not withdraw knowledge. Raw query logs have a later dashboard/admin consumer but no established policy transformation; persisted weights have a setter/getter capability but no shipped ranking bridge. These distinctions prevent raw-trace retention, metadata adaptation and successful learning from being conflated.

Rejection occurs at different layers: malformed JSON may be ignored, link proposals can fail structural gates, importer items can be skipped, a stage can fail while the initial object remains, and transport registration can omit admin tools. None is a universal semantic quality gate. Withdrawal requires explicit delete/unlink/update or whole-store restore; supersession/findings alone are not removal. Temporal snapshots preserve some old content rather than guaranteeing rollback or comprehensive deletion. See the maintenance annotation and [MEM-OBJ-document-versions](#mem-obj-document-versions).

## Read-back

Actual later consumers include the requesting external host; optional synthesis model; fixed ranking, graph-query and inference code; tier-preserving enrichment; access promotion; and diagnostic trail/dashboard readers. Their force differs. Host output is informational; ranking coefficients/vector comparisons and graph query bodies receive fixed code interpretation. No automatic promotion of arbitrary stored prose to host system instructions is established. [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery), [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution), [MEM-RTE-access-promotion](#mem-rte-access-promotion).

The retrieval annotation states selector inputs, selected retained parts and budgets for hybrid briefing, full document, dossier and synthesis. Requested graph/list/export views are alternate retained-state projections rather than evidence that every path uses hybrid ranking. Alerts and reasoning are also requested read-back; the label proactive does not make their transport a push path. There is no inspected automatic selector that independently injects retained content into an external host window. Source scope for that limit is the CLI/tool inventory, server handlers and shipped agent guidance, not all possible external integrations. SRC-1, `src/cortex/cli/main.py`, `src/cortex/transport/mcp/server.py`, `llms.txt`.

Temporal version readers, miss detection, inactive-tier adjustment and persisted weight retrieval remain exposed capabilities without a demonstrated shipped later route. Their persistence is reported without inventing a caller. Static prompts, ontology and inference rules are shipped guidance/code, not accumulated read-back memory. Provider state is opaque external dependency state; runtime's model-component records bound version/mutability claims. No host conversation checkpoint or alternative host compaction form was supplied; the in-scope historical alternative is a documents-row snapshot, not a conversation summary.

## Integration issues

- **No correction to a supplied runtime fact is required.** The added record parts refine [RT-OBJ-store](runtime.md#rt-obj-store), not replace it. [MEM-RTE-access-promotion](#mem-rte-access-promotion) is a part of its retrieval route, not a duplicate of [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context). All newly declared objects use the supplied store as their single parent. [MEM-RTE-issue-delivery](#mem-rte-issue-delivery) overlaps read-only portions of [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) and status presentation, but isolates a distinct selection/delivery responsibility. [MEM-CLM-learning-scope](#mem-clm-learning-scope) adds a qualification of source doctrine; it does not contradict the runtime's explicit lack of a learned-weight bridge. No replacement identity or other possible duplicate was found against the supplied records.
- **Summary/vector freshness:** inspected update/classify do not regenerate embeddings; a nonempty summary suppresses reclassification even on reprocessing. Actual stale outputs and external caller refresh policy are unknown. Consequence: neither updated content nor pipeline complete establishes all downstream projections are current. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/normalize.py`; [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-embeddings](#mem-obj-embeddings).
- **Usage metadata is not a proven ranking loop:** source-wide search and constructor/feedback bodies establish a bounded missing bridge, not incapacity of the public library. Actual external wiring is unavailable. Consequence: retain tier adaptation as wired, automatic weight adaptation as absent within the searched shipped boundary, and learning benefit as unestablished. [MEM-ABS-adaptation-wiring](#mem-abs-adaptation-wiring), [MEM-CLM-learning-scope](#mem-clm-learning-scope).
- **Meaning of stale differs across consumers:** pipeline-stage, archive-tier and incoming-supersedes checks do not implement the same test. Consequence: no unified expiry/withdrawal rule and no inference that all stale knowledge is filtered. [MEM-RTE-issue-delivery](#mem-rte-issue-delivery), [MEM-OBJ-tier](#mem-obj-tier).
- **Historical state and erasure:** temporal read APIs have no shipped consumer found and snapshots omit bypass mutations and non-document state. Current-row deletion does not erase independent history/access/query tables. Full administrative erasure and deployed restore behavior remain unestablished. Consequence: do not treat temporal history as universal recovery or delete as complete forgetting. [MEM-OBJ-document-versions](#mem-obj-document-versions), [MEM-OBJ-query-log](#mem-obj-query-log), [MEM-OBJ-access-count](#mem-obj-access-count).
- **Source trust and adoption:** caller identity, imported authorship, model correctness and host use remain unresolved, while parser/structural checks are known. Consequence: semantic trust, actual context injection and task improvement cannot be concluded from retention/delivery. [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline), [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery).
- **Evaluation scope:** `benchmarks/conftest.py` instantiates SyntheticEmbeddingProvider; `tests/retrieval/test_learner.py` assertions cover counter/promotion, miss predicate and weight persistence. These are source evaluation designs, not observed runs or a provider-quality experiment. No online evaluator-to-admission bridge was established. Consequence: neither reported improvement nor causal benefit is supported by this inspection. SRC-1, `benchmarks/conftest.py`, `tests/retrieval/test_learner.py`; [MEM-CLM-learning-scope](#mem-clm-learning-scope).

## Limitations and checks

The checkout HEAD was rechecked as `a51c2209eb6d26812c19c97aaade3cb64ccfc23c`; source identity and report boundary match the supplied invocation and boundary. The memory type, runtime/boundary types, collection contract, worker rules and complete record contract were read. Analysis stayed within the registered source and authorized outputs. An initial evaluator search used three nonexistent guessed directory names and returned exit 2; a subsequent directory listing established the actual suites before further searches. No conclusion rests on that failed search.

Source text establishes wiring and bounded capabilities only. No live retained corpus, externally authenticated provenance, observed host behavior, model-output faithfulness, installed hook activation, successful rollback or causal improvement is established. Coverage intentionally distinguishes supplied runtime findings from additional direct reads; partially inspected optional surfaces remain limits, not exclusions or absences.

Validation: the required deterministic validate-output check passed after expanding an ambiguous importer quotation to its branch-specific context. The check covers content form, citations and quotation occurrence, not analytical acceptance.
