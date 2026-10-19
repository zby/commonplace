---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "sift-kg memory: extraction caches, graph maintenance, generated sidecars and selective external-agent reload."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
source-identity: https://github.com/juanceresa/sift-kg
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
---

# sift-kg memory report

## Boundary and evidence

This report covers the retained document-to-graph loop and its later consumers at SRC-1, commit d786991c024f5401f113fc0cb70aee96dd1bd3bf, under the [source register](boundary.md#source-register). Memory includes extraction JSON, reusable discovered domains, saved graph content and provenance, review decisions, community assignments, generated descriptions and narrative, and explicit retrieval/export/view calls. The bundled skill supplies a prescribed external-agent consumer, not an observed session. Source documents are acquisition inputs, not transcripts of sift-kg's own operation. No conversation-history or provider-state learning claim follows from their ingestion.

The supplied runtime orders the main routes. Direct additional inspection covered `src/sift_kg/extract/models.py`, extraction cache/summary/deduplication bodies, `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/knowledge_graph.py`, cleanup/pruning bodies in `src/sift_kg/graph/postprocessor.py`, neighborhood projection in `src/sift_kg/graph/communities.py`, `src/sift_kg/resolve/engine.py`, narrative orchestration/context loading/description generation, export dispatch/flattening, viewer loading/node construction, CLI search/query, exported stage wrappers and the full bundled skill. These are implementation and doctrine/design layers of the existing SRC-1, not new sources or execution evidence.

### Coverage inventory

| Entry point or memory operation | Source path (SRC-1) | Coverage and limits |
|---|---|---|
| Console/module dispatch and Python exports | `pyproject.toml`; `src/sift_kg/cli.py`; `src/sift_kg/__init__.py`; `src/sift_kg/pipeline.py` | Direct command/export scan plus supplied runtime entry account. Stage functions and `KnowledgeGraph` are exposed; convenience pipeline does not run review/apply. |
| Document acquisition, summary, extraction cache; direct text/single-file alternatives | `src/sift_kg/extract/extractor.py`; `src/sift_kg/extract/models.py` | Direct reads; [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [MEM-OBJ-document-extraction](#mem-obj-document-extraction). Reader/OCR internals remain supplied-runtime coverage; no OCR-quality conclusion. |
| Discovered/custom schema reuse | `src/sift_kg/domains/discovery.py`; `src/sift_kg/pipeline.py` | Direct serialization tail and extraction/build consumers; supplied [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery), [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config). No independent schema-quality test. |
| Build, normalization, pruning and relation flags | `src/sift_kg/graph/builder.py`; `src/sift_kg/graph/postprocessor.py`; `src/sift_kg/pipeline.py` | Direct build/load/flag and cleanup reads; supplied normalization/direction findings in [RT-RTE-graph-build](runtime.md#rt-rte-graph-build). |
| Graph save/load, mention aggregation and direct mutation API | `src/sift_kg/graph/knowledge_graph.py` | Direct full read; [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data), [MEM-OBJ-relation-support](#mem-obj-relation-support). Public mutation/save methods afford caller-authored writes; unspecified external callers do not establish additional deployed routes. |
| Candidate selection and review | `src/sift_kg/resolve/resolver.py`; `src/sift_kg/resolve/reviewer.py`; `src/sift_kg/resolve/models.py` | Supplied [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions); direct stage-wrapper cross-check. Detailed reviewer/resolver bodies not independently reread. |
| Apply, rejection and withdrawal | `src/sift_kg/resolve/engine.py`; `src/sift_kg/pipeline.py` | Direct engine and caller reads; [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions). Graph mutation is not cache/sidecar mutation. |
| Narrative, descriptions, community labels and style rewriting | `src/sift_kg/narrate/generator.py` | Direct orchestration/context/description reads plus supplied [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) for rewrite details; three distinct sidecar objects below. Prompt-specific excerpt truncation beyond inspected caller construction remains uninspected. |
| info/topology/query/search; external-agent consumption | `src/sift_kg/cli.py`; `src/sift_kg/graph/communities.py`; `.agents/skills/sift-kg/SKILL.md` | Direct query/search/projection/skill reads; info/topology internals supplied by [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval). Host delivery is afforded, actual compliance unobserved. |
| Export and browser view | `src/sift_kg/export.py`; `src/sift_kg/visualize.py`; `src/sift_kg/pipeline.py`; `src/sift_kg/cli.py` | Direct dispatcher, flattening, wrapper and view data-construction reads; [MEM-RTE-export-artifacts](#mem-rte-export-artifacts), [MEM-RTE-view-artifacts](#mem-rte-view-artifacts). Browser event/rendering bodies and every format serializer not fully inspected; no complete presentation-fidelity claim. |
| Hooks, registered tools, services | `pyproject.toml`; `src/`; `.agents/` | Entry scan and bounded search for hook/tool/MCP registrations found no additional route in these roots. This bounds the inventory, not an ecosystem-wide absence claim. |
| Example artifacts, tests, demos | `examples/`; `tests/`; `pages/` | Boundary inventory only; bodies not independently inspected here. They establish neither measured accuracy nor actual sessions in this report. |

External provider state is opaque as recorded in [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client); optional embeddings are a temporary selector, not an inspected durable vector store ([RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer)). User corpora, deployed host context management and provider internals are unavailable. No target code, tests, models, services or examples were executed.

## Core ideas

1. **The extraction cache, not the edited graph, is the reconstruction base.** Build loads every parseable extraction file and constructs a fresh graph. Applied merges/rejections change only the graph. Rebuilding can therefore restore removed material; removing a source document without removing its extraction file does not remove that file from build input. This follows from the direct cache loader and apply writer, not an observed incident ([MEM-OBJ-document-extraction](#mem-obj-document-extraction), [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions)).
2. **Retained evidence and delivered evidence differ.** Graph edges retain mentions and aggregate support, but query delivers selected evidence/support fields rather than all mentions. Repeated mentions can increase confidence even within one document; the formula is not an independent truth check ([MEM-OBJ-relation-support](#mem-obj-relation-support)).
3. **Review is a downstream mutation path, not universal admission.** Parsed extractions and generated prose enter stores automatically. Relation flags are written after graph save; reviewer thresholds can decide statuses without individual human approval. A rejected relation is removed from the saved graph only on apply, not from extractions or previously generated prose ([RT-RTE-graph-build](runtime.md#rt-rte-graph-build), [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions)).
4. **Read-back is requested, selective and multi-surface.** Host instructions request session orientation and question-specific graph lookup. Query uses ID/name/alias targeting and hop selection, not semantic retrieval or an automatic push. Search, export and view have different projections. Descriptions and labels can outlive the graph state that produced them ([RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions), [MEM-OBJ-communities](#mem-obj-communities)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-document-extraction
Label: DocumentExtraction cache

Source-native identity: `DocumentExtraction`, serialized to `extractions/<document_id>.json`. Storage substrate: filesystem JSON and parsed Pydantic objects. Symbolic document identity/configuration metadata, confidence and typed records drive cache reuse/build. Names, attributes, contexts and evidence are natural-language material when interpreted by models/humans; names also participate in fixed string matching. These are model-derived document representations, not raw document text or an agent action log. `document_path` is a pointer, not embedded source contents. Distinct from the supplied graph object and extraction route: it is their persistent upstream product/input, not a duplicate of either. Closest records: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data).

Lineage: read document → overlapping chunks → first-chunk summary plus per-chunk model extraction → structural parsing → confidence-based entity deduplication and collected context strings → per-document JSON. Caller supplies documents/settings; their original authorship is not established. Software admits parsed fields and writes automatically; initiation is not per-record human approval. Bulk/single-file extraction persists the object. Direct `extract_from_text` returns it without persisting that extraction, though its optional schema-discovery path can write YAML. Evidence: SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/models.py`.

> Incremental — skips documents whose extraction config matches.
> --- `src/sift_kg/extract/extractor.py`

Consumers: later extraction can return cached content without rereading the source; build reads all sorted JSON files, not just currently supplied documents; narration independently reloads entity contexts by lowercased name. Metadata freshness checks model string/domain name/chunk size, not document bytes or schema contents. Filename-stem collisions share a destination. Force regenerates requested inputs but does not itself remove other cache files. User file editing/deletion can change the reconstruction input, but no inspected synchronizing withdrawal journal propagates graph-only decisions back to these files. Evidence: SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/graph/builder.py`, `src/sift_kg/narrate/generator.py`.

> for path in sorted(extractions_dir.glob("*.json")):
> --- `src/sift_kg/graph/builder.py`

#### MEM-OBJ-relation-support
Label: Canonical relation mentions and support

Part of: [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data)

Source-native identity: canonical edge `mentions`, `support_count`, `support_documents`, `support_doc_count`, `confidence`, and representative `evidence`. Substrate: edge dictionaries in NetworkX and `graph_data.json`; symbolic endpoints/types/counts/confidence and natural-language evidence quotes. This is the provenance/aggregation part of the supplied graph container, not an alternative graph record. It is derived from extracted relation mentions, not independent measurements of truth. Original documents remain outside the serialized edge.

`add_relation` normally coalesces equal source/type/target triples, appends mentions, counts mentions separately from distinct support documents and aggregates confidence. Default product-complement admits repeated evidence as reinforcing signals without a source-independence test in that function. `canonicalize=False` is an alternate public API path retaining separate edges; no shipped driver using that alternative was established. Save includes mentions by default; `export(include_mentions=False)` can omit them. Load normalizes support from mentions and recomputes confidence; it is not a byte-preserving reload. Evidence: SRC-1, `src/sift_kg/graph/knowledge_graph.py`.

> # Trust mentions as source of truth; ignore stale support_count
> support_count = len(mentions)
> --- `src/sift_kg/graph/knowledge_graph.py`

> # product_complement: independent weak signals reinforce one another
> return 1.0 - prod(1.0 - c for c in confidences)
> --- `src/sift_kg/graph/knowledge_graph.py`

Later authority differs by consumer: flagging compares aggregated edge confidence to a threshold; query returns representative evidence and support summaries; narration obtains edge evidence plus separately reloaded extraction contexts. Query omits edge `mentions` and node `context`, so full retained justification is not delivered through that projection. The quote retained on an edge is model-supplied evidence, not verified entailment. Direct source: SRC-1, `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/communities.py`, `src/sift_kg/narrate/generator.py`.

#### MEM-OBJ-communities
Label: Community assignments and generated labels

Source-native identity: `communities.json`, entity-ID-to-label mapping. Substrate: filesystem JSON and runtime dictionaries. IDs and label equality operate symbolically for grouping/filtering; theme text conveys natural-language meaning to a human/agent. Distinct sidecar, not part of the graph JSON: its independent generation/invalidation matters. Closest supplied records are [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) and [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation), producers rather than the object itself.

Lineage/admission: deterministic Louvain grouping at build; automatic model naming during narration or explicit community regeneration. Fixed code admits algorithm/model results without per-label approval. Consumers: topology/query community context, narration's cache/grouping branch, and view color/group controls. Build overwrites assignments, apply does not refresh them, and narration's cache check accepts any nonempty set not entirely matching placeholder labels; it is not graph-revision binding. View loads this sidecar relative to the HTML destination directory, whereas its descriptions path comes from the output directory. A custom HTML destination can therefore miss otherwise available assignments and compute fallback communities. Evidence: SRC-1, `src/sift_kg/pipeline.py`, `src/sift_kg/narrate/generator.py`, `src/sift_kg/visualize.py`.

> communities_path = output_path.parent / "communities.json"
> --- `src/sift_kg/visualize.py`

> if unique_labels and not all(_PLACEHOLDER_LABEL.match(lbl) for lbl in unique_labels):
>     cached_labels_are_themed = True
> --- `src/sift_kg/narrate/generator.py`

#### MEM-OBJ-entity-descriptions
Label: Entity description sidecar

Source-native identity: `entity_descriptions.json`, entity-ID-to-generated-prose mapping. Filesystem JSON stores symbolic keys and natural-language descriptions. Lineage: graph entities/relations plus extraction contexts → model descriptions → phrase-triggered rewrite → retained prose. Not a raw trace, not opaque model state, and not merely access metadata. Closest supplied record [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) is its producer, not the sidecar.

Software selects degree-qualified entities, admits returned prose automatically and writes only when the new description dictionary is nonempty. Accordingly a no-descriptions or all-failed pass need not erase an old sidecar. Explicit rerun/edit/delete is the available operator replacement surface; no inspected per-description approval or revision history. Later consumers are `search --description`, view generation, and CLI non-JSON exports. `run_export` does not load this sidecar; `export_graph` accepts an optional caller-supplied map; JSON export saves the graph instead of joining descriptions. These alternate routes prevent a universal description-enrichment claim. Evidence: SRC-1, `src/sift_kg/narrate/generator.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/export.py`, `src/sift_kg/visualize.py`.

> # Save descriptions as JSON sidecar for viewer integration
> if entity_descriptions:
>     desc_path = output_dir / "entity_descriptions.json"
> --- `src/sift_kg/narrate/generator.py`

Delivery grants interpretive context to host/human, not executor authority. A graph-only correction does not rewrite earlier prose; description ID lookup can join old text to a surviving canonical node. No observed consumption or factual accuracy is supplied.

#### MEM-OBJ-narrative
Label: Narrative Markdown

Source-native identity: `narrative.md`, retained natural-language report on the filesystem. Generated overview, relationship/timeline prose, descriptions and structural material are assembled under fixed Markdown construction after optional style rewrites. Automatically admitted product, not a transcript or encoded model weights. Distinct from descriptions and community labels because the Markdown is independently written and lacks an inspected automatic reload into later extraction/build calls. Closest supplied record: its producer [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation).

The bundled skill lists it as an optional output, affording human/host file reading, but does not prescribe a concrete narrative read-back command. Presence of a file therefore does not establish a wired agent-memory route for its full prose. Rerunning narration can replace it; graph application/rebuild need not regenerate it. Evidence: SRC-1, `src/sift_kg/narrate/generator.py`, `.agents/skills/sift-kg/SKILL.md`.

> output_path = output_dir / "narrative.md"
> output_path.parent.mkdir(parents=True, exist_ok=True)
> output_path.write_text(md, encoding="utf-8")
> --- `src/sift_kg/narrate/generator.py`

### Routes

#### MEM-RTE-export-artifacts
Label: Retained graph export

Explicit CLI/library export request → graph reload → format projection → output artifact. Owner: caller selects paths/format; code executes transformation/writes. Distinct from [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval): delivery is an exported file, not query/topology stdout. Not a duplicate; both consume [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data). No model comparison or answer oracle: open deterministic export. Caller can withhold request/change destination; output is admitted automatically, with no content approval or inspected version journal. Regeneration from input is recovery, not automatic rollback. SRC-1, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py`, `src/sift_kg/export.py`.

- Immediate return: exported path, plus CLI completion output; native JSON or analytical files on disk.
- Later read-back: saved graph and optional descriptions enter this later export invocation; external tools may load the resulting files, but no deployed external importer is established.
- Delegated visibility: inapplicable — no delegated model invocation; consumers receive the format projection, not an LLM prompt.
- Selection predicate: explicit output directory/format/destination. JSON retains native graph; other formats strip metadata. CLI loads descriptions when available; run_export omits that join. GraphML/GEXF flatten fields and combine parallel relations, so they are not exact native checkpoints.
- Invalidation or expiry: explicit regeneration writes outputs; no source-revision freshness gate or automatic propagation of subsequent graph edits established.
- Activation or effect: deterministic file projection; user interpretation and downstream deployment remain uninspected.
- Evidence limits: dispatch and flattening inspected; every format serializer and external consumer behavior not fully inspected. File production does not prove import fidelity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if fmt == "json":
>     return _export_json(kg, output_path)
> --- `src/sift_kg/export.py`

#### MEM-RTE-view-artifacts
Label: Retained graph to browser artifact

Explicit CLI/library view request → graph/description/community reload → metadata stripping and graph filters → HTML node/edge construction → optional browser opening. Caller selects scope; code chooses projections and assignments. Distinct from [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), which returns CLI structural JSON rather than browser artifacts. No oracle or model judgment inside view; no human per-node approval. Generated presentation is admitted automatically, can be withheld/recreated/deleted by caller, and has no inspected versioned rollback. Evidence: SRC-1, `src/sift_kg/pipeline.py`, `src/sift_kg/visualize.py`.

- Immediate return: HTML path and optional browser opening.
- Later read-back: later invocation reloads saved graph, ID-keyed descriptions and destination-relative communities; browser receives embedded presentation data.
- Delegated visibility: inapplicable — no model delegation; filtered graph data and descriptive text are serialized for a human-facing browser consumer.
- Selection predicate: top-N, confidence, source document, neighborhood/depth and community inputs select view scope. Missing/empty community map permits full-graph Louvain fallback before metadata stripping; existing map is reused.
- Invalidation or expiry: explicit view regeneration; graph apply does not update existing HTML; sidecar loading has no graph-revision check here.
- Activation or effect: descriptions become node description fields; communities shape grouping/colors. This establishes data construction, not observed browser interaction or belief change.
- Evidence limits: Python load/filter dispatch and node construction inspected; detailed browser controls and rendering not executed or fully traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> desc = entity_descriptions.get(node_id, "")
> --- `src/sift_kg/visualize.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

Working context: code keeps other chunks out of each extraction call, sends one chunk with domain and first-chunk summary, and gathers structured results outside those calls. The summary is model-produced natural language retained in process memory for later chunk invocations, not a persisted per-document summary field. Its input is the document's first chunk, not an execution trace. This is within-job derived context, while JSON extractions provide cross-invocation disk memory. There is no removed conversation tail or summary-based chat reload in this inspected route. The isolated-call lens fits selected inputs/return values; it does not turn calls into conversational subagents or the model window into pointer-addressable storage. SRC-1, `src/sift_kg/extract/extractor.py`.

> "Summarize this document excerpt in 2-3 sentences. "
> --- `src/sift_kg/extract/extractor.py`

Curation: deduplication keeps a highest-confidence entity but aggregates distinct context fragments into its context string, instead of keeping only that winner's quote. Later narration splits this field back into fragments. These are retained claimed source excerpts; no inspected exact-source verification is established. SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/narrate/generator.py`.

> entity.context = " ||| ".join(sorted(all_ctx))
> --- `src/sift_kg/extract/extractor.py`

#### On [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config)

Persistent generated schema is document-sample-derived guidance, not a revision from an evaluated agent-session trace. It can affect later extraction model prompts and deterministic build transformations. The consumer force is split: descriptions/hints are interpreted; configured vocabularies and fallback rules drive particular code branches. Cached YAML is editable/replacable independently of model parameters, but name-only cache checks do not establish content freshness. Initial custom schema authorship remains caller-dependent; automatic discovery authorship and later reuse are known. Evidence and minimum passages are supplied by [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance); direct consumer cross-check: SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/pipeline.py`.

#### On [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

Curation includes automatic removal of self-loops/transitive redundant edges and pruning nodes having only metadata connections. These are structural rules, not a content-directed factual adjudication. The optional postprocess bypass is a countercase to treating cleanup as universal. Pruning changes what later query can find while extraction contexts can remain available to narration. SRC-1, `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/postprocessor.py`.

> if not has_substantive:
>     to_remove.append(node_id)
> --- `src/sift_kg/graph/postprocessor.py`

#### On [RT-OBJ-review-files](runtime.md#rt-obj-review-files)

Decision statuses are symbolic control material at apply; reasons/evidence are natural-language review context. A confidence-based automatic decision and a person's edit reach the same status representation. Merge reasons persist in YAML and can inform reviewer display, but the merge engine does not copy them onto graph nodes/edges or consult them to execute. Relation evidence and flag reasons likewise do not become universal provenance of later graph surgery. This separates retained reasons from reasons actually read by the execution consumer. SRC-1, `src/sift_kg/resolve/engine.py`; reviewer display/decision evidence supplied by [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions).

> # Build full merge map: member_id → canonical_id
> merge_map: dict[str, str] = {}
> --- `src/sift_kg/resolve/engine.py`

#### On [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions)

Revision horizon: graph changes survive subsequent graph loads, not necessarily a rebuild from unchanged extraction files. Canonical-node values take precedence during merge, with member source-document references/confidence/attributes/aliases folded in; the engine does not preserve all node contexts as a revision history. Rejection removes matching type/endpoints in both directions, not merely one supporting mention/document. It does not remove source caches, regenerate descriptions/communities, or insert confirmed variant suggestions. SRC-1, `src/sift_kg/resolve/engine.py`, `src/sift_kg/pipeline.py`.

> # Also handle symmetric — if A→B rejected, B→A should be too
> rejection_keys.add((entry.target_id, entry.source_id, entry.relation_type))
> --- `src/sift_kg/resolve/engine.py`

#### On [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation)

Read-back joins graph content and extraction contexts by lowercased entity name, not stable ID/type/document provenance at the context-lookup point. This can combine homonymous entities' excerpts and does not automatically include contexts stored under merged aliases. Graph-only rejection cannot guarantee withdrawal from these independently loaded excerpts. This is a code-supported limit, not a measured contamination event. SRC-1, `src/sift_kg/narrate/generator.py`.

> source_quotes = entity_contexts.get(entity["name"].lower().strip(), [])
> --- `src/sift_kg/narrate/generator.py`

Budget/context selection: overview is capped at 50 entities and 150 selected relations; descriptions at 250 entities with degree at least three. Degree ranking uses the full graph here, unlike substantive-degree query ranking. Phase-specific prompts isolate overview/chains/timeline/descriptions; return prose escapes each call, not a retained conversation frame. Further prompt-side truncation was not independently inspected; these caps are caller-level limits, not a universal token cap. The style rewrite takes generated text plus phrase feedback, retaining revised prose rather than a criticism history. It is an automatic output-fed curation path; actual factual preservation or improved future capability is unestablished. SRC-1, `src/sift_kg/narrate/generator.py`; rewrite passage supplied by the annotated runtime record.

#### On [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval)

Read-back direction: caller requests info/topology/query/search, code selects retained parts and delivers through stdout. The skill's session-start trigger is a host protocol, not a target-side unsolicited push. Query depth bounds graph distance, not response token count; high-degree neighborhoods may still be large. Exact ID and fuzzy name/alias targeting differ, and neither is dense-vector retrieval. Node context and full mention arrays are omitted from neighborhood projection even though graph JSON retains them. SRC-1, `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py`.

The existing runtime exact-DOCUMENT exception is not the only metadata exception: search iterates all graph nodes without query's fuzzy DOCUMENT exclusion. Its JSON matches can include DOCUMENT nodes; substantive-degree counting does not remove those matches. Optional description lookup joins by ID; search relation summaries do not provide the neighborhood's evidence/support detail. Thus the skill's all-agent-facing filtered-view wording cannot be used as an invariant for search either. SRC-1, `src/sift_kg/cli.py`; exact-ID countercase and source claim supplied by the runtime.

> for node_id, data in kg.graph.nodes(data=True):
>     name = data.get("name", "")
>     if entity_type and data.get("entity_type", "").upper() != entity_type.upper():
>         continue
> --- `src/sift_kg/cli.py`

#### On [RT-BAP-host-skill](runtime.md#rt-bap-host-skill)

Host working-context policy is scale-conditioned: small graphs may be loaded as full JSON; larger graphs should use topology plus selected query neighborhoods. Static skill text is instruction supply, not accumulated memory. The graph/community outputs it requests are later read-back. The skill also prescribes a before/after topology snapshot in `/tmp` for rebuild comparisons; this is a host-authored artifact protocol, not an automatic sift comparison/persistence feature. No inspected session shows host snapshot retention or adoption of the resulting suggestions. SRC-1, `.agents/skills/sift-kg/SKILL.md`.

> **Graph scale:** For graphs under ~500 entities, `graph_data.json` can be loaded directly into context. For larger graphs, always use `sift topology` and `sift query` — never attempt to load the full JSON.
> --- `.agents/skills/sift-kg/SKILL.md`

## Write side

Admission is mechanism-local. Acquisition supplies caller-selected documents; the caller's identity or authorship is unresolved. Extraction code automatically admits structurally parsed model records and cached reuse; discovery automatically retains a model-generated schema. Build automatically merges/normalizes/prunes and saves graph material before relation review. Human initiation is not content approval. Relevant routes: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery), [RT-RTE-graph-build](runtime.md#rt-rte-graph-build).

Resolution admits draft proposals, not graph merges. Reviewer thresholds or human keys admit status changes; manual YAML editing is another supported route. Apply consumes those symbolic decisions and overwrites changed graph state. The same saved status does not establish which actor approved it. Confirmed relation suggestions are not general insertion instructions. Reasons persist for review but do not become an executed justification store. These findings retain the supplied distinctions rather than equating curation with verification ([RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions), [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions)).

Withdrawal has three different scopes: removing/changing cache inputs affects a future build; graph apply removes/merges current saved structure; regenerating/deleting sidecars changes generated prose/presentation. None implies all three. Build's loader still admits orphaned extraction files, while graph-only edits need not survive rebuild. Old review YAML can also survive a build with no new flags. These are explicit countercases to automatic consistency, not evidence that every artifact is always stale. SRC-1, `src/sift_kg/graph/builder.py`, `src/sift_kg/pipeline.py`; [MEM-OBJ-document-extraction](#mem-obj-document-extraction), [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions), [MEM-OBJ-communities](#mem-obj-communities).

Raw-to-derived chains are document text → chunk summary/extractions → graph → descriptions/labels/narrative → later reads, plus generated prose → phrase-triggered rewrite → retained prose. These are document-derived and output-fed transformations, not evidence of learning from an agent's action/outcome history. The direct graph API affords arbitrary caller mutations/saves, but unspecified callers do not establish additional trace-fed learning routes. Provider learning is uninspected. No improved future capacity is inferred from persistence, automatic curation or the second-brain label.

## Read-back

- **Reuse and reconstruction:** extraction reload uses stem-selected files and a configuration predicate; build loads every parseable extraction JSON. These are automatic selectors within caller-initiated operations, not unsolicited host delivery ([MEM-OBJ-document-extraction](#mem-obj-document-extraction)).
- **Later model input:** cached schema changes prompt construction; narration reloads saved graph and name-keyed extraction excerpts. Document summaries instead reach later chunk calls within the same job and are not persisted summaries. Scope, budgets and join limits are in the route annotations.
- **Later human/agent context:** topology returns structure; query returns a requested neighborhood; search returns matching entries and optional descriptions. External agent authority is interpretive guidance under the shipped skill, not target-enforced obedience. The host decides subsequent calls and final answers ([RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [RT-BAP-host-skill](runtime.md#rt-bap-host-skill)).
- **Other delivery:** export and view are concrete later consumers, unlike an isolated storage accessor. Their saved files afford subsequent external consumption, but external importer/browser success is not observed ([MEM-RTE-export-artifacts](#mem-rte-export-artifacts), [MEM-RTE-view-artifacts](#mem-rte-view-artifacts)). Narrative file presence alone establishes no automatic read-back into the pipeline ([MEM-OBJ-narrative](#mem-obj-narrative)).

## Integration issues

1. **Metadata-filter qualification:** retain the runtime's exact-ID exception and add the independently inspected search exception. Search's substantive-degree helper filters counts, not match eligibility. This extends the qualification of [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), not a correction to its supported query-subgraph finding. Evidence: SRC-1, `src/sift_kg/cli.py`; annotation above. It prevents treating all agent-facing responses as metadata-free.
2. **Description/export route difference:** [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation)'s broad consumer inventory should retain that CLI export loads descriptions but `run_export` does not; JSON export does not join them. [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions), [MEM-RTE-export-artifacts](#mem-rte-export-artifacts) establish the distinction. Evidence: SRC-1, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py`, `src/sift_kg/export.py`. No universal description-bearing export conclusion.
3. **Consistency questions remain local:** graph revision is not bound to review files, communities, descriptions or narrative in the inspected model/callers. After rejection/merge/rebuild, which sidecars a deployed host regenerates is unknown. This prevents a deployment-wide fresh/withdrawn-memory claim, not the wired mutation finding. Records: [RT-OBJ-review-files](runtime.md#rt-obj-review-files), [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions), [MEM-OBJ-communities](#mem-obj-communities), [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions), [MEM-OBJ-narrative](#mem-obj-narrative). Evidence: SRC-1, `src/sift_kg/pipeline.py`, `src/sift_kg/narrate/generator.py`.
4. **Identity comparison:** new cache/sidecar objects are products consumed/produced by supplied routes, not re-declarations of those routes. [MEM-OBJ-relation-support](#mem-obj-relation-support) is explicitly a part of [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data). New export/view routes share its input but have distinct delivery mechanisms from [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval). No possible duplicate requiring replacement is identified after comparison.
5. **Unresolved operational questions:** actual external-agent compliance, document/schema accuracy, source independence behind confidence, prompt-side truncation beyond inspected caller caps, browser interaction, external import fidelity and provider-side updates remain uninspected. The inventory names the affected paths; no operation, accuracy or learning benefit is inferred for these records. These limits require no source/boundary change.

## Limitations and checks

The source HEAD was rechecked as d786991c024f5401f113fc0cb70aee96dd1bd3bf. Source checkout status was clean at inspection. Supplied member identities, record citations and evidence layers were retained; this worker writes only its assigned candidate and auxiliary outputs. Source-dependent findings use SRC-1 and commit-relative anchors. Minimum passages support the new load-bearing distinctions; supplied runtime records supply passages for carried findings. No target execution or experimental validation occurred.

Available-but-uninspected files are not access gaps. Excluded external service and host internals prevent guarantees about compliance, deployed freshness, accurate extraction and causal benefit. Local deterministic validation is recorded after executing the required validate-output command; a pass establishes form/citation/quotation checks, not analytical correctness or acceptance.

Validation: required `commonplace-run validate-output` completed with exit status 0: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”
