---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "sift-kg memory: document-derived graph, reusable schema, review decisions and derived prose, with caller-directed agent read-back."
run-id: AAS-2026-10-15-sift-kg-dca68bc45a2c-01
source-identity: https://github.com/juanceresa/sift-kg
reviewed-boundary: d786991c024f5401f113fc0cb70aee96dd1bd3bf
---

# sift-kg memory report

## Boundary and evidence

The memory boundary includes document extraction caches, discovered domains, graph construction and maintenance, review files, communities, derived prose, CLI retrieval, the library entry points and browser/export consumers. It follows the whole-system boundary, not just the primary graph. Host-agent context assembly and session scheduling, provider internals, dependency weights and deployed permissions remain outside the inspected implementation. These limits prevent conclusions about actual cross-session answers, provider retention or end-to-end privacy. Sources are those registered in [boundary](boundary.md#source-register).

Evidence is SRC-1 implementation and doctrine/design at the frozen commit. HEAD was rechecked against that commit. Runtime findings are supplied evidence, not direct observations. Additional direct reads cover the entire bundled skill and extraction/review models; graph load/add/export/save bodies; builder initialization, provenance and postprocessing; bulk extraction; library build; CLI info/search/topology/query; subgraph selection; narrative sidecar/cache handling, context loading and description generation; description prompts; surgery and rejection; and CI configuration. No target code or tests were executed.

| Entry point or memory operation | SRC-1 path | Coverage and limit |
|---|---|---|
| CLI dispatch, module entry, configuration/init/domains | `src/sift_kg/cli.py`, `src/sift_kg/__main__.py`, `pyproject.toml` | CLI commands inventoried directly; supplied runtime traces configuration and entry points. Init/domains are setup/static guidance, not accumulated-memory routes. |
| Document/OCR/chunk extraction, direct text/document API, cache reuse | `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/models.py`, `src/sift_kg/ingest/` | Direct bulk/cache/model reads; other paths supplied by [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction). Opaque OCR alternatives remain separately identified by [RT-CMP-ocr-backends](runtime.md#rt-cmp-ocr-backends). |
| Schema discovery/reload | `src/sift_kg/domains/discovery.py`, `src/sift_kg/pipeline.py` | Direct build reload plus supplied [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery); generated definitions are guidance, not verified ontology. |
| Build, pre-dedup, normalization/pruning, communities | `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/graph/communities.py` | Direct builder/store reads, supplied [RT-RTE-graph-build](runtime.md#rt-rte-graph-build). SemHash dependency internals remain opaque, not omitted. |
| Resolve, optional embeddings, review/manual YAML, apply/reject | `src/sift_kg/resolve/`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py` | Direct models/surgery; supplied resolution/review routes. Retained reasons and executable statuses have different consumers. |
| Narrate, descriptions, themes, rewrite, communities-only | `src/sift_kg/narrate/generator.py`, `src/sift_kg/narrate/prompts.py` | Direct context/description/cache/save reads, supplied [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation); no factual outcome evaluation supplied. |
| Info, search, query, topology | `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py` | Direct reads; [MEM-RTE-project-info](#mem-rte-project-info), annotation on [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval). |
| Direct small-graph loading and session-start protocol | `.agents/skills/sift-kg/SKILL.md` | Direct doctrine read; annotation on [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill). External host compliance uninspected. |
| View/export and library getters/load/save | `src/sift_kg/visualize.py`, `src/sift_kg/export.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/graph/knowledge_graph.py` | Supplied [RT-RTE-view-export](runtime.md#rt-rte-view-export), direct store methods. Getters alone are capabilities; shipped CLI/library drivers establish consumers. |
| Evaluators and example outputs | `.github/workflows/ci.yml`, `tests/`, `examples/` | CI read directly; tests/examples inventoried in supplied boundary. No evaluator result-to-memory update is established; no test run or example reproduction performed. |
| Hooks/tools/service alternatives | `.agents/`, `pyproject.toml`, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py` | Scoped symbol/dispatch search and supplied [RT-ABS-tool-execution](runtime.md#rt-abs-tool-execution). No additional operative memory hook was identified in these inspected surfaces; this is not a claim about external integrations. |

## Core ideas

1. **The durable knowledge is transformed document content, not conversational history.** Per-document JSON is the rebuild substrate; graph identities, support records and prose derive from it. A first-chunk model summary helps other chunks in the same extraction but is not itself a durable conversational checkpoint. See [MEM-OBJ-document-extraction](#mem-obj-document-extraction).
2. **Different retained files exert different authority.** A domain conditions future extraction and normalization; graph data supplies knowledge to callers; review statuses command surgery; prose supplies interpreted summaries. A reason string is not an executable admission rule. See [MEM-OBJ-discovered-domain](#mem-obj-discovered-domain), [MEM-OBJ-merge-proposals](#mem-obj-merge-proposals), [MEM-OBJ-relation-review](#mem-obj-relation-review).
3. **Retrieval reduces the graph, not necessarily to a fixed context budget.** Name/alias lookup, hop distance and topology select data. There is no query token cap in the inspected selector. The skill's approximately 500-entity threshold is advice to a host, not enforced eviction. See the retrieval and skill annotations below.
4. **Persistence does not establish freshness or approval.** Cache identity omits source contents; build recreates the graph; flags do not quarantine relations; sidecars can outlive graph edits. These source-supported countercases qualify the persistent-memory label without denying the wired reload paths. See [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-review-application](runtime.md#rt-rte-review-application) and [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-document-extraction
Label: DocumentExtraction retained per-document results

Source-native identity: `DocumentExtraction`, persisted as `extractions/{Path.stem}.json`. Symbolic fields identify document path, model, domain name, chunk size, timestamp, counts, errors and typed records; names, contexts, evidence and arbitrary descriptive attributes carry natural-language content. Metadata supports cache decisions; it is not source verification. Storage is JSON on the host filesystem, parsed into Pydantic objects. SRC-1: `src/sift_kg/extract/models.py`, `src/sift_kg/extract/extractor.py`.

> context: str = ""  # Quote from source text
> --- `src/sift_kg/extract/models.py`

> extraction_path.write_text(extraction.model_dump_json(indent=2))
> --- `src/sift_kg/extract/extractor.py:514-514`

Lineage: reader/OCR text → overlapping chunks and transient first-chunk summary → model judgments → shape validation → same-name/type dedup with collected contexts. This is derived knowledge, not raw source text or a retained model-reasoning trace. Build consumes typed records; narration consumes name-matched contexts; cache reload consumes configuration metadata. Source documents remain separately reachable by path, not embedded whole. The comment calling context a quote is not an entailment or verbatim check. Admission/failure/cache limits are supplied by [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction). Distinct identity: this is that route's persisted output, not the route itself; runtime declares no object counterpart.

#### MEM-OBJ-discovered-domain
Label: Discovered domain configuration

Source-native identity: `discovered_domain.yaml`, a filesystem YAML encoding of `DomainConfig`. Symbolic type names, source/target lists and canonical constraints drive code; natural-language descriptions and system context become model instructions. Lineage is sampled corpus prefixes → model schema proposal → typed/nonempty checks → saved configuration. Extraction and build reload it across invocations; it can be edited/replaced by a file writer, with no per-schema human gate. SRC-1: `src/sift_kg/domains/discovery.py`, `src/sift_kg/pipeline.py`; the minimum discovery witness and independent theory-property limits are in [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery). This object is distinct from that route and from static shipped domains. Reasons for choosing the schema and criticism histories are not established as retained fields; reuse of definitions is established. Build's actual consumer witness:

> discovered = load_discovered_domain(output_dir / "discovered_domain.yaml")
> --- `src/sift_kg/pipeline.py`

#### MEM-OBJ-graph-data
Label: Saved graph entity and provenance state

Source-native identity: `KnowledgeGraph.graph` and the node/metadata portions of `graph_data.json`. Storage is a NetworkX MultiDiGraph and filesystem JSON. Symbolic IDs/types, document nodes, provenance edges, counts and paths coexist with natural-language names, contexts and attributes. Lineage is retained extractions plus domain constraints → automatic pre-dedup/build/postprocess → optional later surgery. Source nodes/paths are access metadata, not the underlying readable document. Later build creates a new graph; query, resolve, narrate, topology, search, view/export load saved state. These consumers do not all receive the same fields. SRC-1: `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/knowledge_graph.py`.

> kg = KnowledgeGraph()
> --- `src/sift_kg/graph/builder.py`

Entity update keeps higher confidence, unions source documents, updates attributes and fills missing context; that is lossy aggregation, not retention of every conflicting version. Admission is automatic build or status-controlled surgery, not authenticated source endorsement. Distinct identity: output/state of [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) and [RT-RTE-review-application](runtime.md#rt-rte-review-application), not a duplicate route. Relation support is separated in the next object because its aggregation and delivered evidence differ.

#### MEM-OBJ-relation-support
Label: Canonical relation support and representative evidence

Source-native identity: canonical edge fields `mentions`, `support_count`, `support_documents`, `confidence`, `evidence` and `source_document`, in `KnowledgeGraph` and `graph_data.json`. Symbolic triples and numeric support metadata aggregate derived extraction mentions; evidence remains natural language. They are not independent raw-document attestations. Default product-complement aggregation combines mention confidences; a representative evidence/source pair can replace earlier display evidence. The full mention list persists on default save, while query emits selected support fields and representative evidence, not all mentions. SRC-1: `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/graph/communities.py`.

> if mention["confidence"] >= self._normalize_confidence(best_so_far):
>     edge_data["_best_mention_confidence"] = mention["confidence"]
>     edge_data["evidence"] = evidence
>     edge_data["source_document"] = source_document
> --- `src/sift_kg/graph/knowledge_graph.py`

This is a distinct operative part of graph state, not a replacement for [MEM-OBJ-graph-data](#mem-obj-graph-data). Closest supplied records are [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) and [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval); neither declares this object. Aggregated confidence is not an evaluated probability of truth. The builder's overlapping-chunk inputs prevent assuming independent supporting observations.

#### MEM-OBJ-merge-proposals
Label: Merge proposals and retained reasons

Source-native identity: `MergeFile`/`MergeProposal` in `merge_proposals.yaml`. YAML stores symbolic canonical/member IDs, status and confidence, with natural-language names/reasons. Model identity comparisons and code-generated cross-type matches create proposals; threshold code, interactive review or direct file editing changes status. Review displays reasons, application filters status and node existence, and info counts statuses. Surgery does not consume the reason as a rule or copy a reasoned decision history into the graph. SRC-1: `src/sift_kg/resolve/models.py`, `src/sift_kg/resolve/engine.py`, `src/sift_kg/cli.py`.

> reason: str = ""  # LLM's explanation for why these should merge
> --- `src/sift_kg/resolve/models.py`

> confirmed = merge_file.confirmed
> --- `src/sift_kg/resolve/engine.py`

This is retained decision material, not raw execution history or a reversible patch set. Rejected proposals remain readable but application selects confirmed ones. No graph-version binding or automatic replay at build is established. Distinct output object of [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) and control input of [RT-RTE-review-application](runtime.md#rt-rte-review-application), not duplicate routes.

#### MEM-OBJ-relation-review
Label: Relation review entries and rejection controls

Source-native identity: `RelationReviewFile`/`RelationReviewEntry`, persisted in `relation_review.yaml`. Symbolic endpoints/type/status/confidence and natural-language evidence/flag reasons reside in YAML. Build flags existing graph relations; resolve can append variant proposals. These have different origins despite sharing a file. Reviewers see evidence/flags, info counts statuses, application removes rejected triples in both directions. A confirmed proposed variant does not insert an edge. SRC-1: `src/sift_kg/resolve/models.py`, `src/sift_kg/resolve/engine.py`; supporting progression and gate witnesses are [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-review-application](runtime.md#rt-rte-review-application).

> rejected = review_file.rejected
> --- `src/sift_kg/resolve/engine.py`

Statuses are behavioral controls at surgery, not a universal trust filter at retrieval. DRAFT relations already built into the graph are available to query. Deletion concerns current graph edges; extraction inputs can recreate them at rebuild. Distinct object, not a redeclaration of either supplied route.

#### MEM-OBJ-communities
Label: Community assignments and theme labels

Source-native identity: `communities.json`, an entity-ID-to-label mapping on disk. Symbolic membership keys support grouping/topology; labels are default text or generated natural-language themes. Louvain detection derives membership from graph structure; narration can name communities or regenerate them, sometimes over described entities. Topology/query/view and narration cache reuse are later consumers. SRC-1: `src/sift_kg/graph/communities.py`, `src/sift_kg/narrate/generator.py`, `src/sift_kg/cli.py`.

> if cached_labels_are_themed:
>     logger.info("Communities already cached, skipping detection + theme naming")
> --- `src/sift_kg/narrate/generator.py`

Themed-cache detection is not a graph-revision check. Labels guide human/model interpretation but do not establish semantic equivalence or correct clustering. This is distinct retained output/input across [RT-RTE-graph-build](runtime.md#rt-rte-graph-build), [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) and [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval), not any one route's referent.

#### MEM-OBJ-entity-descriptions
Label: Entity description sidecar

Source-native identity: `entity_descriptions.json`, a symbolic ID-to-natural-language-description mapping on disk. Selected graph entities plus relations and name-matched extraction contexts feed completion calls. Software admits returned descriptions and optional style rewrites without mandatory human approval or factual comparison. Search with description requested, viewer and export are downstream consumers. SRC-1: `src/sift_kg/narrate/generator.py`, `src/sift_kg/narrate/prompts.py`, `src/sift_kg/cli.py`; [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation).

> if entity_descriptions:
>     desc_path = output_dir / "entity_descriptions.json"
> --- `src/sift_kg/narrate/generator.py`

This conditional save leaves possible older prose when generation yields none. Graph surgery does not itself refresh the sidecar; current-ID lookup can miss removed members or return old prose for surviving IDs. These are derived readable summaries, not opaque numerical payloads or raw evidence. Distinct object produced by the supplied narrative route and consumed by retrieval/presentation routes.

#### MEM-OBJ-narrative
Label: Reader-facing narrative Markdown

Source-native identity: `narrative.md`, natural-language overview, relationship/timeline prose and entity profiles, with Markdown structure, stored on the filesystem. Graph ranking, extraction contexts and model calls produce it; style checks can request rewrites. The file is a durable reader-facing artifact. Info tests existence, not factual quality; no inspected automatic extraction or graph-update consumer treats the narrative as new evidence. External human/agent reading is afforded, not observed. SRC-1: `src/sift_kg/narrate/generator.py`, `src/sift_kg/cli.py`.

> output_path.write_text(md, encoding="utf-8")
> --- `src/sift_kg/narrate/generator.py`

Distinct output object of [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation). Unlike descriptions/themes, the supplied source account does not establish a later programmatic semantic consumer of the whole narrative. Its existence is not evidence of grounding benefit.

### Routes

#### MEM-RTE-project-info
Label: Project state to session orientation information

An invoking user/host asks `sift info --json`; CLI code loads configuration, graph and review files, counts extraction files and tests narrative existence, then prints metadata. This is distinct from the supplied [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval), whose progression covers query/search/topology rather than project-status inspection. SRC-1: `src/sift_kg/cli.py`, `.agents/skills/sift-kg/SKILL.md`.

> data["documents_processed"] = len(list(extractions_dir.glob("*.json")))
> --- `src/sift_kg/cli.py`

- Immediate return: JSON configuration/counts/review-status totals, or a rich table without the JSON flag.
- Later read-back: Saved graph and status files inform a later caller's orientation; the skill requests this at session start.
- Delegated visibility: Metadata and counts reach the invoking host; no completion-model call in this command.
- Selection predicate: Caller-selected output directory; file presence and status counts, with metadata-stripped graph counts for JSON.
- Invalidation or expiry: Each invocation reads current files; file count is not a test that every document was successfully processed or remains current.
- Activation or effect: Output wiring exists; host decisions based on it are unobserved. It writes no new knowledge.
- Evidence limits: Static implementation and skill protocol only, not a session trace or success evaluator.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The caller requests the lookup; deterministic code selects fields. There is no candidate-admission decision or expected-answer oracle here. The skill requests orientation but does not schedule this command independently.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

Memory-specific lineage is raw documents/OCR → transient character chunks and model first-chunk summary → derived extraction → build/narration/cache consumers. The summary remains in `doc_contexts` during the run; the persisted `DocumentExtraction` fields do not include that summary or all chunk text. This is not a trace-fed conversational compaction checkpoint. File paths allow external source access but do not reload original text into query responses. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/models.py`; [MEM-OBJ-document-extraction](#mem-obj-document-extraction).

The default context mechanism excludes other chunks from a given extraction call, adds shared first-chunk orientation and lets only parsed results escape. Runtime supplies chunk-size/overlap and adapter-isolation evidence. This resembles bounded independent call frames, not spawned agents or pointer-based liveness. Bulk cost rejection can still yield a persisted partial/empty document; its cache can later avoid reprocessing it. Starting extraction is not human approval of its content.

#### On [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery)

Retained schema is corpus-derived guidance, not experience from an observed failed extraction. Symbolic constraints and interpreted text have separate downstream force, as [MEM-OBJ-discovered-domain](#mem-obj-discovered-domain) explains. Automatic admission is typed/nonempty checks, not human schema acceptance. File editing affords human replacement; exercised criticism-to-revision is not established. SRC-1: `src/sift_kg/domains/discovery.py`, `src/sift_kg/pipeline.py`; the supplied route retains the discovery witness and theory limits.

#### On [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

Build curates retained extraction content through identity normalization, pre-dedup, relation aggregation, pruning and optional domain normalization/direction fixes. It creates rather than patches the old graph. The resulting knowledge is authoritative as current saved data to read consumers even while review is pending. It is not universal content verification. SRC-1: `src/sift_kg/graph/builder.py`, `src/sift_kg/pipeline.py`; [MEM-OBJ-graph-data](#mem-obj-graph-data), [MEM-OBJ-relation-support](#mem-obj-relation-support).

> # Save graph
> graph_path = output_dir / "graph_data.json"
> kg.save(graph_path)
> --- `src/sift_kg/pipeline.py`

The later review flags are not an admission gate before this save. Missing source-file deletion is not a withdrawal instruction to this builder: its retained input is extraction JSON, not a fresh reconciliation against the source directory. Bulk extraction reuses/writes current inputs without deleting orphan JSONs. Removing an original document alone therefore does not establish removal from later graph state. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/graph/builder.py`.

#### On [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution)

The saved proposal retains a reason, but downstream surgery selects status/IDs, not the explanatory content. Resolution context excludes full source passages and most graph attributes; runtime's selected identity-field witness bounds the sameness decision. Optional embeddings are transient name/alias vectors, not a persisted retrieval index. Their provenance/model pinning limits remain in [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer). SRC-1: `src/sift_kg/resolve/resolver.py`, `src/sift_kg/resolve/engine.py`; [MEM-OBJ-merge-proposals](#mem-obj-merge-proposals).

#### On [RT-RTE-review-application](runtime.md#rt-rte-review-application)

Human decisions, automatic thresholds and direct YAML edits are distinct admission channels. Physical file writing is performed by software in the CLI, regardless of who decided the status. Retained reasons are visible to review; status is operative at surgery; the graph contains the mutation but not an inverse patch/history. Rejected relation decisions remove both-direction matching types from current state, while later rebuild can restore extraction-derived content. SRC-1: `src/sift_kg/resolve/engine.py`, `src/sift_kg/resolve/models.py`; the supplied route provides threshold/gate evidence. Confirming a variant has no graph insertion effect, so retention of that decision alone cannot establish learned new graph knowledge.

#### On [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation)

Narration reads selected graph content and extraction excerpts, not raw originals. `_load_entity_contexts` groups by lowercased entity name, splits ` ||| ` contexts and does not key by type/document. The description selector uses the current display name, not all aliases; merging/renaming can change which passages arrive. Same-name entities can share gathered contexts. Prompt construction further caps description relations at 40 and distinct contexts at 30. This bounds support actually delivered to the model, rather than assuming all retained evidence is present. SRC-1: `src/sift_kg/narrate/generator.py`, `src/sift_kg/narrate/prompts.py`.

> source_quotes = entity_contexts.get(entity["name"].lower().strip(), [])
> --- `src/sift_kg/narrate/generator.py`

> contexts = contexts[:30]
> --- `src/sift_kg/narrate/prompts.py`

Other overview/chain/timeline ranking and caps are supplied by the runtime. Style-regex feedback produces another model text proposal; returned prose is automatically retained. It is neither a factual oracle nor a demonstrated improvement in future action. No raw-to-derived conversational trace-learning chain is established by this document-fed summarization. The outputs and stale-cache cases are [MEM-OBJ-communities](#mem-obj-communities), [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions) and [MEM-OBJ-narrative](#mem-obj-narrative).

#### On [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval)

Read-back is caller-requested, not an independent push scheduler. Query selector inputs are exact ID or substring/type plus hop depth; name ambiguity is resolved by substantive degree, not semantic relevance scoring. BFS operates over a metadata-stripped undirected graph and returns directed edges among selected nodes. It excludes node contexts, document nodes, provenance edges and full mention lists; it returns source-document IDs, attributes, representative relation evidence and support totals/documents. Thus provenance accessibility is partial at this delivery channel. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py`.

> nodes.append(node_dict)
>
> # Extract directed edges between visited nodes
> --- `src/sift_kg/graph/communities.py`

Hop depth limits distance, not tokens, node count or evidence length. Search JSON can include descriptions and relations but relation entries omit evidence; unlike query it does not explicitly skip DOCUMENT nodes in its matching loop. Pretty search truncates description display to 300 characters and relation display to 10 by default (1000 verbose), whereas JSON is a different delivery budget. Topology gives up to five top IDs per community plus bridges/isolation/connections. None of these fields implies truth verification or actual host-answer uptake. Pending review is not a read filter. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py`.

#### On [RT-RTE-view-export](runtime.md#rt-rte-view-export)

Browser/export deliver retained graph/prose to readers. Native graph export can preserve mentions while analytical exports flatten/strip metadata; those consumers cannot be assumed to receive identical provenance. Static generated HTML/export files are additional copies, not live views proven to follow later surgery. Supplied runtime evidence covers these implementation paths. SRC-1: `src/sift_kg/export.py`, `src/sift_kg/visualize.py`, `src/sift_kg/pipeline.py`. Storage/getter methods expose capabilities; only named shipped drivers or documented readers establish a consumption route.

#### On [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill)

The host is asked to keep topology in session context, query before relevant answers, compare topology before/after rebuild and choose direct loading only for small graphs. The retained graph is the knowledge input; the shipped skill is static guidance, not material learned from use. Its topology-before snapshot example uses `/tmp/topology_before.json`; the external host must retain/compare it. No automatic comparison-to-graph write follows in sift-kg. SRC-1: `.agents/skills/sift-kg/SKILL.md`.

> **Graph scale:** For graphs under ~500 entities, `graph_data.json` can be loaded directly into context. For larger graphs, always use `sift topology` and `sift query` — never attempt to load the full JSON.
> --- `.agents/skills/sift-kg/SKILL.md`

This affords an alternative whole-file read-back route whose selection is the host's choice, not a graph-file identifier functioning as semantic retrieval. The host owns eviction, persistence of returned tool results and future reload. No token budget, compactor, automatic context injection or observed compliance is established by this instruction.

## Write side

Acquisition is user/host-supplied documents, with optional OCR; the original input is not an agent execution trace. Model extraction authors content, parsers admit shapes, dedup collects contexts, and filesystem code persists it. Human source authorship, initiating the command and approving each extracted statement are different operations. The supplied extraction route and [MEM-OBJ-document-extraction](#mem-obj-document-extraction) retain these distinctions. Discovery automatically admits reusable guidance under a separate nonempty-schema gate; custom/static domains are manually configurable alternatives, not evidence of human approval of discovered definitions.

Build is another admission mechanism: automatic graph construction and postprocessing. Pre-dedup name collapse precedes reviewed surgery. Review flags are retained assessment candidates after graph save. Resolve creates reasons/confidences, review may assign statuses automatically or interactively, direct editing can replace them, and application enforces only confirmed-merge/rejected-relation status behavior. A rejected merge proposal does not undo a previously applied merge; rejection prevents selection at application. Exact prior graph restoration requires an external copy or reconstruction, not a reversible decision log. See graph/review annotations and [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval).

Narration adds a distinct automatic text-admission surface. Banned-phrase detection selects rewrites but does not verify facts. Descriptions/themes/narrative persist without mandatory human content acceptance; they carry graph/document-derived interpretations rather than model reasoning histories. Reasons persist in proposal YAML and can be displayed to reviewers; they are not consumed semantically by surgery or supplied wholesale to ordinary retrieval.

Withdrawal has multiple scopes. Rejected relations disappear from the saved graph after application, not from extraction JSON. Rebuild can restore them and overwrite prior merges. Source deletion alone does not purge retained extractions. Graph mutation does not automatically invalidate descriptions, themes or already generated HTML/exports. Force/rerun/edit/remove files are operator recovery controls, not a coordinated transactional withdrawal mechanism. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/graph/builder.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/resolve/engine.py`, `src/sift_kg/narrate/generator.py`; supplied runtime recovery account.

CI runs lint and pytest on repository changes; its configuration establishes an evaluator invocation, not an online feedback loop updating user memory. No supplied run result connects evaluation to a durable behavior-shaping update. Extraction costs/errors and review decisions are retained metadata, but their presence alone is not trace-fed learning or demonstrated improved capacity. SRC-1: `.github/workflows/ci.yml`, `src/sift_kg/extract/models.py`, `src/sift_kg/resolve/models.py`.

## Read-back

Durable results cross invocations through explicit filesystem reloads. Cached extraction metadata decides whether to skip work; discovered domains affect extraction/build; graph data feeds resolve, narration, CLI lookup and presentation; proposal/review statuses control surgery; description sidecars feed optional search/view/export; community membership/labels feed topology/query and narration reuse. Each has a named consumer rather than a hypothetical API caller. Whole narrative reading is afforded to an external reader; only its existence check is established programmatically here. See the corresponding object records and annotations.

Agent read-back is pull-oriented at the CLI: the host asks, symbolic code selects, stdout returns JSON/text. The skill prescribes asking at session start and when relevant, but provides no enclosing scheduler. Direct small-graph loading is an alternative afforded host route; it can expose more provenance than query. Selection depends on names, aliases, structural degree, hops or community structure, not an inspected vector retrieval store. Embeddings in resolution and SemHash in build are separate transient similarity mechanisms. See [RT-CMP-sem-hash](runtime.md#rt-cmp-sem-hash), [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer).

The model-visible working context is stage-specific selected input rather than a growing chat window. Extraction isolates chunks, resolution isolates candidate batches, narration selects graph/text subsets, and agent lookup restores selected external data on demand. The returned value survives each completion call, not the provider's whole internal processing. There is no established alternate conversation-tail checkpoint; opaque provider state remains uninspected. Delivery to a host establishes availability, not compliance, grounding success or benefit.

## Integration issues

- **Search is not uniformly metadata-filtered.** The supplied retrieval record is accurate about substantive degree and query neighborhoods but should not imply every search match excludes DOCUMENT nodes. Search iterates all nodes without that skip, and pretty search can display provenance relations. SRC-1: `src/sift_kg/cli.py`; annotation on [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval). This also qualifies the skill's claim that all agent-facing counts/subgraphs use the filtered view; exact-ID query matching and search matching are separate from neighborhood filtering.
- **Retention is not source-change detection or incremental graph editing.** Supplied runtime already qualifies the skill: cache checks omit content and build starts fresh. The memory consequence is that document deletion does not itself retract cached knowledge and rebuilding can lose surgery. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/graph/builder.py`; [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-graph-build](runtime.md#rt-rte-graph-build). These are compatible additions, not requests to erase supported runtime findings.
- **Derived state has independent freshness.** Communities/themes, descriptions, narrative and generated presentations need not reflect a later graph mutation. SRC-1: `src/sift_kg/narrate/generator.py`, `src/sift_kg/resolve/engine.py`; [MEM-OBJ-communities](#mem-obj-communities), [MEM-OBJ-entity-descriptions](#mem-obj-entity-descriptions), [MEM-OBJ-narrative](#mem-obj-narrative), [RT-RTE-view-export](runtime.md#rt-rte-view-export). No revision-linked guarantee should be inferred from file presence.
- **Partial evidence delivery matters.** Query's representative evidence/support metadata omits contexts and full mentions; narration joins contexts by display name, not provenance identity. SRC-1: `src/sift_kg/graph/communities.py`, `src/sift_kg/narrate/generator.py`; [MEM-OBJ-relation-support](#mem-obj-relation-support), [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation). The source supports retained traceability fields, not universal passage fidelity.
- **Record identity check:** runtime declares no operative objects. The nine object declarations describe retained outputs/parts across supplied routes, not duplicate components/routes. [MEM-RTE-project-info](#mem-rte-project-info) adds the status/orientation command not traced by the supplied query/search/topology progression; its overlap is shared graph/status inputs, not identical operation. No possible duplicate requiring supersession was found.
- **Unresolved operation:** no host-session trace, deployed backend choice, exact dependency weights, extraction-quality evaluation or controlled benefit comparison is supplied. These prevent observed uptake, accuracy and improvement conclusions, not the wired persistence/consumer findings. SRC-1 scope and dependencies are in [boundary](boundary.md#source-register); [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-ocr-backends](runtime.md#rt-cmp-ocr-backends) retain opaque alternatives.

## Limitations and checks

The inspected target remains the registered repository at `d786991c024f5401f113fc0cb70aee96dd1bd3bf`; no outside source, model call, test execution or example replay was added. This report follows the supplied memory type, worker rules and record contract. Supplied runtime records carry supporting passages where cited; new load-bearing findings retain direct source witnesses. Source reading and quotation checks cannot establish model fidelity, actual sessions or causal benefit. The report does not infer learning from persistence, reflection from document subject matter, or self-improvement from derived prose.

Deterministic validation: the invocation-specific validate-output check passed after writing this member; it checks structure and quotation occurrence, not semantic acceptance or observed behavior.
