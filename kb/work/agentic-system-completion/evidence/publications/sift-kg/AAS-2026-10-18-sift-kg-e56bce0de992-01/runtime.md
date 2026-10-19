---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "sift-kg runtime baseline: document extraction, graph admission, review and agent-facing retrieval at d786991c024f5401f113fc0cb70aee96dd1bd3bf."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
---

# sift-kg runtime report

## Runtime account

### Boundary, entry and ordinary work

sift-kg runs a code-owned document-to-graph workflow, not an open-ended model tool loop. The shipped CLI owns stage sequencing and filesystem effects; models supply extraction content, proposed identity judgments and prose. An external agent can operate the CLI under the bundled skill, but that host's tool execution and final answers are outside this boundary. Evidence is inspected implementation and source-native instructions at SRC-1, as registered in [boundary](boundary.md#source-register). No target code, tests, services or examples were executed. Operation, actual host compliance and benefit remain unobserved.

The installed `sift` entry, Python module entry and exported library stages are included. CLI settings select a model, input documents, domain, extraction/OCR backend and output directory; the library takes explicit arguments rather than requiring those CLI configuration checks. The convenience `run_pipeline` calls extract, build and optionally narrate, not resolve/review/apply. Its comment that resolve/apply require human review describes intent, not the full admission mechanism: the reviewer can auto-confirm. Evidence: SRC-1, `pyproject.toml`, `src/sift_kg/__main__.py`, `src/sift_kg/__init__.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`.

> sift = "sift_kg.cli:app"
> --- `pyproject.toml`

An ordinary source-supported invocation is `sift extract ./documents/ -o output/`, then `sift build -o output/`. Later `sift topology -o output/` and `sift query "name" -o output/` return the retained graph's structure. This is a reconstructed code path, not a supplied successful run. The progression is:

1. A caller supplies documents and settings. The CLI discovers supported files and constructs an `LLMClient`. Extraction derives each document ID from its filename stem. Cached extractions can return before document reading. For uncached work, the reader obtains text, the chunker forms overlapping segments, schema-free mode may discover and retain a domain, and a model summarizes each document's first chunk.
2. Code creates one extraction task per chunk under a shared semaphore. Each call receives the chunk, domain guidance and document summary, not the whole corpus or a conversational transcript. JSON parsing and Pydantic construction select admissible fields; malformed entries are skipped, and handled model/parse failure yields an empty chunk result. Code combines chunks, deduplicates entities by type/name, and writes per-document JSON.
3. Build loads all parseable extraction JSONs, constructs a new graph, performs deterministic deduplication and optional postprocessing, then saves `graph_data.json`. Community assignments are also written. Flagging relations occurs after graph saving; a flag is not a quarantine gate.
4. Optional resolve/review/apply stages propose identity merges, set proposal/relation statuses, then mutate the saved graph. Optional narrate writes generated prose and descriptions and can replace community labels. Query/topology reload saved state in later invocations; the external agent decides how to use the returned JSON.

These loops, their decision roles, operating modes, answer-oracle limits and admission points are declared in [RT-RTE-document-extraction](#rt-rte-document-extraction), [RT-RTE-schema-discovery](#rt-rte-schema-discovery), [RT-RTE-graph-build](#rt-rte-graph-build), [RT-RTE-entity-resolution](#rt-rte-entity-resolution), [RT-RTE-review-decisions](#rt-rte-review-decisions), [RT-RTE-apply-decisions](#rt-rte-apply-decisions), [RT-RTE-narrative-generation](#rt-rte-narrative-generation) and [RT-RTE-agent-retrieval](#rt-rte-agent-retrieval). Model fixity is separated in [RT-CMP-llm-client](#rt-cmp-llm-client) and [RT-CMP-sentence-transformer](#rt-cmp-sentence-transformer).

### Control coverage and forcing cases

**Cost control is best effort, not a hard dollar cap.** Owner: extraction/narrative orchestration, not the provider client. The extraction budget predicate runs before semaphore acquisition and after schema discovery and per-document summaries. Tasks can all pass before queued calls incur cost. The client tracks usage after receiving a response; it does not reserve cost or enforce a cap. Narrative overview, chains, timeline, rewrites and theme calls are not all governed by the entity-description budget check. The library pipeline constructs separate clients for extraction and narration and passes the same budget to each, not a shared remaining balance. Required external contract: provider/LiteLLM usage and cost estimates must be available and accurate. Covered paths: bulk extraction chunk admission and narrative description admission only. Alternate paths: single-document/text APIs, schema/summary calls, other narrative phases, resolve and direct client calls. Implementation conclusion status: wired. Operation conclusion status: uninspected. Guarantee strength: best effort. Evidence: SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/llm_client.py`, `src/sift_kg/narrate/generator.py`, `src/sift_kg/pipeline.py`.

> if max_cost and llm.total_cost_usd >= max_cost:
>     return doc_id, ExtractionResult(source_document=doc_id, chunk_index=chunk.chunk_index)
> async with sem:
> --- `src/sift_kg/extract/extractor.py`

**Confirmed-only merge application is a narrow invariant; human-only graph admission is not.** Owner/enforcement: `MergeFile.confirmed` and the merge engine's iteration over that list. Both shipped CLI and library apply callers use it. Required external contract: writable YAML and graph files must be trusted if status is to mean approval by a particular person. The engine checks status, not the identity or process that wrote it. Reviewer defaults automatically confirm sufficiently confident proposals; users can disable that with threshold 1.0. Editing YAML is a supported path to confirmation. Build also admits extraction content and deterministic deduplication before review. Guarantee strength: invariant for selecting confirmed merge proposals in this engine; no claimed guarantee of human approval across graph writes. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-review-decisions](#rt-rte-review-decisions) and [RT-RTE-apply-decisions](#rt-rte-apply-decisions). Evidence: SRC-1, `src/sift_kg/resolve/models.py`, `src/sift_kg/resolve/engine.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`.

**Incremental reuse does not detect every changed document.** The skill says only new/changed documents are processed, but the implemented stale check compares model string, domain name and chunk size. It does not read or hash the current document before returning a matching cache entry. Replacing a file with the same stem and those settings can therefore reuse old content. Domain contents can also change under an unchanged domain name. The countercase is reachable from both CLI bulk extraction and the single-document API, not merely an unsupported input. `force` bypasses this reuse; schema discovery is then also eligible to rerun. Owner: extractor. Guarantee strength: policy for configuration-based reuse, not content freshness. Implementation conclusion status: wired. Operation conclusion status: uninspected. Evidence: SRC-1, `src/sift_kg/extract/extractor.py`, `.agents/skills/sift-kg/SKILL.md`.

> if existing.model_used != model:
>     return f"model changed ({existing.model_used} → {model})"
> if existing.domain_name != domain_name:
>     return f"domain changed ({existing.domain_name} → {domain_name})"
> if existing.chunk_size != chunk_size:
>     return f"chunk size changed ({existing.chunk_size} → {chunk_size})"
> return None
> --- `src/sift_kg/extract/extractor.py`

**Metadata exclusion is consumer-local.** The clean graph helper removes DOCUMENT nodes and MENTIONED_IN edges; neighborhood extraction checks those again when emitting nodes/links. However query's supported exact-ID branch selects directly from the original graph, bypassing the fuzzy branch's DOCUMENT and type filters. An exact `doc:<stem>` can produce DOCUMENT match metadata while its subgraph is empty. An exact entity ID also takes precedence over `--type`. This does not show that excluded nodes leak into subgraph arrays; those remain filtered. It defeats the broader skill wording that all agent-facing results are a uniformly filtered view. Owner: query and graph helpers. Guarantee strength: invariant scoped to emitted neighborhood arrays, not the entire response envelope. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: callers distinguish match metadata from subgraph contents. Evidence: SRC-1, `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py`, `src/sift_kg/graph/postprocessor.py`, `.agents/skills/sift-kg/SKILL.md`.

> if kg.graph.has_node(query_str):
>     matched_id = query_str
> else:
> --- `src/sift_kg/cli.py`

> if entity_id not in undirected:
>     return {"nodes": [], "links": []}
> --- `src/sift_kg/graph/communities.py`

These four forcing cases bound consequential controls rather than establish general security or reliability. Provider failures, hostile documents, concurrent processes writing one output directory, browser behavior and corpus accuracy were not experimentally tested.

### Effects, permissions and context

Capability surface: callers can select documents, schemas, model routes and output paths; build and apply can overwrite durable graph state; narration writes prose/labels; retrieval returns selected state. Current grants: CLI/API arguments and process credentials, including provider keys and filesystem access. Deployed isolation envelope: not supplied. The inspected model client sends messages at temperature 0.1 with timeout/retries, not model-chosen executable tools. Its return is consumed as text/JSON by stage code. This supports a bounded executor account, not a claim that untrusted input is safely sandboxed or that dependency internals cannot execute code. The source skill's demand to confirm paid extraction/resolve calls is host guidance, not a CLI approval enforcement point ([RT-BAP-host-skill](#rt-bap-host-skill)). Evidence: SRC-1, `src/sift_kg/extract/llm_client.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`, `.agents/skills/sift-kg/SKILL.md`.

Working-context control is task-input construction, not chat-history compaction. Extraction keeps other document chunks out of each call, sharing a first-chunk model summary instead. The code combines returned structured records outside the model window. Resolution restricts comparison to type batches and identity-relevant attributes; embedding clustering is an optional selector, not an extra deliberating agent. Narration ranks/truncates graph material and makes separate calls for overview, chains, timeline and descriptions. The return-value-only shape resembles isolated task frames, but these are ordinary API calls with constructed prompts, not nested conversational agents; retained graph material requires an explicit later reload. The external skill recommends topology and selective neighborhoods rather than full graph loading at large scale; actual host context eviction/reload behavior is unobserved. Evidence: SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/resolve/resolver.py`, `src/sift_kg/narrate/generator.py`, `.agents/skills/sift-kg/SKILL.md`.

Recovery is stage-local: retries/backoff and rate limiting in the client; empty/default results on selected extraction, summary and narration failures; reusable extraction files between invocations. JSON graph saving is a direct file write, not an inspected transactional checkpoint or undo log. Rebuilding reconstructs from extraction caches and can discard applied graph-only edits; it is not an exact inverse of a merge. Apply does not regenerate community assignments or descriptions. The convenience pipeline skips review entirely. These facts matter when interpreting later retrieval and stale sidecars; detailed memory revision semantics belong to the memory analyst. Evidence: SRC-1, `src/sift_kg/extract/llm_client.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py`.

Added source coverage under SRC-1 is implementation: extraction/cache/client/chunker bodies; schema discovery serialization; graph construction, relation flagging and persistence; resolution batching, parsing, clustering, review and engine; narrative phase orchestration, description admission and phrase rewrites; topology/query and clean-subgraph consumers. Doctrine: bundled agent skill. These are additional inspections of the same registered commit, not new sources or observed-run evidence. Export/view entry wrappers were inspected in `src/sift_kg/pipeline.py`; format internals, OCR dependency internals and browser rendering remain uninspected here, preventing claims about their completeness or isolation, not excluding them from the system boundary.

## Shared records

### Components

#### RT-CMP-llm-client
Label: LLMClient model service

Source-native identity: `LLMClient.model`, passed to LiteLLM completion/acompletion. Representational form: distributed-parametric model behind a service endpoint; client messages and responses are separate text/symbolic interfaces. Storage substrate: provider-managed weights/state, uninspected. Parameters are not updated by inspected client/stage code; provider-side mutation is uninspected. Exact version is not pinned by sift-kg: callers supply a model string, which may be an alias or a separately versioned model. A mutable service route may resolve to another model; endpoint contracts are external. Retries, sliding-window RPM limiting, timeout and post-response usage accounting are client controls, not accuracy controls. Evidence: SRC-1, `src/sift_kg/extract/llm_client.py`.

> response = await litellm.acompletion(
>     model=self.model,
>     messages=messages,
>     timeout=self.timeout,
>     temperature=0.1,
> )
> --- `src/sift_kg/extract/llm_client.py`

#### RT-CMP-sentence-transformer
Label: SentenceTransformer resolution selector

Source-native identity: optional `SentenceTransformer(model_name)` with default `all-MiniLM-L6-v2`. Representational form: distributed-parametric embedding encoder; dense output embeddings are temporary numerical state. Storage substrate: externally loaded model and process memory; download/cache internals uninspected. The inspected route encodes names/aliases without training encoder parameters. Exact model artifact revision is not pinned; the name-based loader's external resolution may change. KMeans fits per-call cluster centers, not the encoder, and its labels control which entities share a comparison prompt. Small sets return without loading the encoder; missing/failing dependencies fall back to lexical batching. Evidence: SRC-1, `src/sift_kg/resolve/clustering.py`, `src/sift_kg/resolve/resolver.py`.

> model = SentenceTransformer(model_name)
> embeddings = model.encode(texts, show_progress_bar=False)
>
> kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
> labels = kmeans.fit_predict(embeddings)
> --- `src/sift_kg/resolve/clustering.py`

### Operative objects

#### RT-OBJ-domain-config
Label: DomainConfig executable vocabulary

Identity/substrate: bundled/custom domain YAML and generated `discovered_domain.yaml`, loaded as `DomainConfig` in process memory. The symbolic part is type names, endpoint-type lists, canonical names/fallbacks, symmetry and review flags consumed by fixed code rules. The natural-language part is descriptions, extraction hints and system context consumed through model interpretation. These parts share a file but have different force: a prompt instruction is not a runtime validator. Discovery emits reusable guidance automatically; caller-supplied domains can replace it through settings. No claim that the schema constitutes a formulated explanatory theory is made. Evidence: SRC-1, `src/sift_kg/domains/models.py`, `src/sift_kg/domains/discovery.py`, `src/sift_kg/extract/prompts.py`, `src/sift_kg/graph/builder.py`.

> Types with canonical_names enforce closed vocabularies: non-canonical
> entities are retyped to fallback_type, and canonical entities are
> pre-created so relations always resolve.
> --- `src/sift_kg/graph/builder.py`

That docstring is conditional: the implementation only retypes a noncanonical name if its configured fallback is non-null. Direction repair also keeps unfixable type mismatches as-is. Neither the type lists nor prompt rules establish full schema validation.

#### RT-OBJ-graph-data
Label: KnowledgeGraph retained stage boundary

Identity/substrate: `KnowledgeGraph` wraps a NetworkX MultiDiGraph in memory and serializes nodes, links and metadata to `graph_data.json`. Symbolic IDs, endpoints, types, confidence and provenance fields are consumed by deterministic algorithms; natural-language names, attributes, contexts and evidence are delivered to models/humans through later routes. Separate consumption paths retain that distinction, rather than treating all JSON as fixed-rule knowledge. Model-produced records are products admitted by code, not facts independently certified by storage. Build recreates the graph from extraction files; apply changes the saved graph; retrieval/narration reload it. Evidence: SRC-1, `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/graph/builder.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py`.

> out.write_text(json.dumps(self.export(), indent=2, default=str))
> --- `src/sift_kg/graph/knowledge_graph.py`

#### RT-OBJ-review-files
Label: Merge and relation decision files

Identity/substrate: `merge_proposals.yaml` and `relation_review.yaml`, parsed into Pydantic models. Symbolic statuses DRAFT/CONFIRMED/REJECTED, entity IDs and relation keys drive execution. Natural-language reasons/evidence and display names inform human review. Model or deterministic proposal writers supply initial content; reviewer code, human key decisions or external file edits supply statuses. Those authorship paths are not authenticated by the engine. Evidence: SRC-1, `src/sift_kg/resolve/models.py`, `src/sift_kg/resolve/io.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/resolve/engine.py`.

> StatusType = Literal["DRAFT", "CONFIRMED", "REJECTED"]
> --- `src/sift_kg/resolve/models.py`

### Routes

#### RT-RTE-schema-discovery
Label: Corpus samples to retained extraction schema

Endpoints/progression: schema-free extraction caller → sampled first chunks → model JSON → `DomainConfig` → saved YAML → extraction prompts and later build. Owner/next-step decision: code decides sampling, reuse and fallback; the model proposes vocabulary/descriptions. Trigger: uncached schema-free work or force. Proposed change: reusable domain vocabulary. Admission: parse/construct types, reject empty entity-type output, write without per-content human approval. Caller may replace/delete the file or force regeneration; no versioned rollback is implemented in the inspected writer. Guidance asks for corpus-specific entity/relation types and constraints; the resulting schema, not a criticism history, persists. Mode: open corpus processing, no curriculum or reference-answer oracle. Evidence: SRC-1, `src/sift_kg/domains/discovery.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/pipeline.py`.

- Immediate return: concrete DomainConfig to extraction, or handled failure retaining schema-free mode.
- Later read-back: discovered_domain.yaml reloads on subsequent extraction/build invocations.
- Delegated visibility: model receives first-chunk samples capped at 3000 characters each, up to five documents for bulk discovery; single-text route uses one sample.
- Selection predicate: schema_free and no usable cached domain, or force; bulk sampling takes first prepared documents.
- Invalidation or expiry: force bypasses discovery cache; no content-addressed expiry in the inspected path; corrupt cache loads return None.
- Activation or effect: parsed domain changes subsequent extraction prompt construction and build normalization inputs; actual model compliance unobserved.
- Evidence limits: samples are not the whole corpus; no run establishes discovered schema quality, learning or benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not entity_types:
>     raise ValueError("Discovery returned no entity types")
> --- `src/sift_kg/domains/discovery.py`

#### RT-RTE-document-extraction
Label: Documents to cached entity and relation records

Owner/progression: caller initiates, CLI/API discovers files, code reads/chunks, model supplies summary and extraction JSON, code parses/deduplicates/persists. Model identity is the caller's LLMClient route; document identity is path stem, with per-document extraction JSON at that stem. Stage code owns next actions and filesystem writes. Trigger/proposed change/admission: document input produces retained records automatically after structural parsing; no human content veto inside extraction. Caller can withhold documents, change guidance, force regeneration or remove artifacts. Recovery: read errors become error records, handled chunk call/parse failures become empty results, summary failure becomes empty context; previously written document results can be reused. No exact rollback snapshot is written. Mode: open document extraction; no expected-answer oracle. Guidance asks for explicit relationships and supporting quotes, not an independent entailment check. Evidence: SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/prompts.py`, `src/sift_kg/ingest/chunker.py`.

- Immediate return: DocumentExtraction list plus CLI counts/cost and per-document JSON writes; direct text API returns one object without the bulk writer.
- Later read-back: extraction cache reuse, graph build and narrative source-context loading consume these artifacts.
- Delegated visibility: each model call receives one overlapping chunk with domain and first-chunk summary; other chunks remain outside that invocation.
- Selection predicate: supported discovered documents not reused by the model/domain-name/chunk-size stale check; force overrides reuse.
- Invalidation or expiry: matching metadata reuses indefinitely; no source-content hash check; filename stems can collide.
- Activation or effect: code admits parsed model fields and highest-confidence duplicate entity entries; stored content can become graph nodes/edges at build.
- Evidence limits: prompt requests do not prove explicitness or quotation accuracy; handled empty chunks can still contribute to a saved extraction with no document-level error.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> except (RuntimeError, ValueError) as e:
>     logger.warning(f"Extraction failed for {doc_id} chunk {chunk.chunk_index}: {e}")
>     return ExtractionResult(source_document=doc_id, chunk_index=chunk.chunk_index)
> --- `src/sift_kg/extract/extractor.py`

#### RT-RTE-graph-build
Label: Extraction cache to rebuilt graph and review flags

Owner/progression: caller starts build; fixed Python rules load parseable extraction files, skip error records, pre-deduplicate names, resolve relation endpoints, add provenance, optionally clean/normalize, save graph, detect communities and flag relations. Model output is input data, not next-step control. Trigger/proposed change: a fresh graph from all loaded extraction records. Admission: automatic code rules; relations with unresolved names are skipped, but low-confidence relations can be saved before being flagged. Human initiation is not per-record approval. Rejection/recovery: user may edit inputs/settings, disable postprocess or rebuild; graph-only corrections are not merged back into extraction inputs by this route. Mode: deterministic construction, not a scored experiment; no answer oracle. Evidence: SRC-1, `src/sift_kg/graph/builder.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/graph/postprocessor.py`.

- Immediate return: KnowledgeGraph/library return or CLI summary; graph_data.json, communities.json and optional relation_review.yaml written.
- Later read-back: query/topology, resolve, apply, narrate and export/view stages reload outputs.
- Delegated visibility: inapplicable — build itself does not delegate model judgment.
- Selection predicate: sorted extractions/*.json that parse and have no extraction error; endpoint resolvability controls relation inclusion.
- Invalidation or expiry: each build replaces graph and community state; no automatic migration of prior applied graph edits; old review files are not necessarily rewritten when no flags exist.
- Activation or effect: graph data becomes directly queryable before review; postprocess=False bypasses cleanup, relation normalization and direction correction.
- Evidence limits: normalization is not semantic verification; CLI and library differ in discovered-domain handling, including canonical/review settings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Save graph
> graph_path = output_dir / "graph_data.json"
> kg.save(graph_path)
> --- `src/sift_kg/pipeline.py`

> f"entity types outside schema constraints (kept as-is)"
> --- `src/sift_kg/graph/postprocessor.py`

#### RT-RTE-entity-resolution
Label: Graph identities to draft merges and variant suggestions

Owner/progression: CLI/library reload graph; code selects type batches, optional embeddings cluster names/aliases, model compares identities; code parses member IDs, deduplicates overlapping proposals and adds same-name cross-type proposals. The latter use degree-selected canonical identity and confidence 0.95, not a model call. If no comparison tasks exist, the async function returns before that cross-type pass. Model receives identity-relevant attributes, not the full document evidence. Trigger: explicit resolve. Proposed change: draft merge groups and EXTENDS suggestions. Admission: proposal serialization only; merge application is separate. Human can reject/edit proposals; failed model batches return no proposals; embedding failure falls back to lexical windows. Mode: open candidate comparison, no expected-answer oracle; confidence is model output or a code constant, not a calibrated reference outcome. Evidence: SRC-1, `src/sift_kg/resolve/resolver.py`, `src/sift_kg/resolve/clustering.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`.

- Immediate return: MergeFile and variant relation entries; shipped callers write proposals and append variants to relation-review YAML.
- Later read-back: reviewer and apply callers reload decision files.
- Delegated visibility: each model comparison receives same-type batch IDs/names/aliases and selected identity attributes with domain context; encoder sees names/aliases.
- Selection predicate: default excludes DOCUMENT type, skips singleton types/batches; caller API can supply entity_types; lexical windows or optional clusters bound comparisons.
- Invalidation or expiry: resolve may overwrite merge proposals; no graph-revision binding/expiry in inspected proposal model.
- Activation or effect: proposals do not themselves merge nodes; variant entries are retained suggestions, not automatically added graph edges by apply.
- Evidence limits: selected batches do not prove globally complete deduplication; same-name cross-type heuristic is not identity verification.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> status="DRAFT",
> members=members,
> reason=group.get("reason", ""),
> --- `src/sift_kg/resolve/resolver.py`

#### RT-RTE-review-decisions
Label: Confidence policy and human keys to persisted decision statuses

Owner/progression: explicit CLI review loads YAML, code auto-confirms high-confidence drafts, auto-rejects low-confidence relation drafts, then human keys approve/reject/skip/quit remaining items. CLI defaults: auto-approve 0.85, auto-reject relations 0.5; library reviewer defaults differ for rejection (0.0). Merge auto-confirm requires all member confidences to meet threshold; 1.0 disables auto-approval rather than merely requiring confidence 1.0. Human veto covers manual drafts and later file edits, not a mandatory pause on auto-approved content. Trigger/proposed change: drafts become executable statuses. Admission: threshold rule or human key, then caller writes updated YAML. Mode: confidence triage plus manual review, no supplied expected-answer oracle. Reason/evidence informs the human, not a machine fact checker. Recovery: skip/quit leaves remaining drafts; statuses can be edited before apply, but there is no automatic prior-status history. Evidence: SRC-1, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`.

- Immediate return: review statistics, modified in-memory models and CLI-persisted YAML.
- Later read-back: apply reloads confirmed merges and rejected relations.
- Delegated visibility: human sees canonical/member IDs, confidence and reason, or relation/evidence panel; no model call in reviewer.
- Selection predicate: only DRAFT items enter review; auto policies run before manual prompts.
- Invalidation or expiry: statuses persist without expiry or authenticated reviewer identity; non-drafts are skipped on later review.
- Activation or effect: CONFIRMED authorizes merge engine selection; REJECTED authorizes relation removal, not automatic addition of confirmed variant suggestions.
- Evidence limits: review policy does not establish human inspection of each admitted item or correctness of decisions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if auto_approve_threshold < 1.0 and min_conf >= auto_approve_threshold:
>     proposal.status = "CONFIRMED"
>     auto_approved.append(proposal)
> --- `src/sift_kg/resolve/reviewer.py`

#### RT-RTE-apply-decisions
Label: Decision files to graph surgery

Owner/progression: CLI/library load graph and decision files, engine selects confirmed merges, checks node existence, combines node data, rewrites incident edges, removes members/self-loops, then removes relations matching rejected keys in either direction. Caller saves only when changes occurred. Trigger/proposed change/admission: explicit apply invocation admits file-authored statuses via fixed selection rules; no new model or human approval is requested here. Caller/file author can reject before application; missing nodes are skipped. Recovery: no inverse merge log/backup in inspected engine and save path; reconstruction from extraction inputs is a different operation. Mode: execution of prior decisions; no oracle. Guidance is fixed engine policy, not an adaptive method revision. Evidence: SRC-1, `src/sift_kg/resolve/engine.py`, `src/sift_kg/resolve/models.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`.

- Immediate return: mutation statistics and overwritten graph_data.json when changed.
- Later read-back: retrieval, resolution and narration load changed graph in later invocations.
- Delegated visibility: inapplicable — apply executes local code without a delegated judge.
- Selection predicate: CONFIRMED merge proposals with existing member/canonical nodes; REJECTED relation keys match source/target/type and reversed endpoints.
- Invalidation or expiry: proposals are not consumed or graph-revision stamped; repeated application skips missing member nodes; community/description files are not regenerated here.
- Activation or effect: nodes/edges are directly changed; relation CONFIRMED statuses are not insertion commands, so confirmed EXTENDS suggestions do not become new edges through this engine.
- Evidence limits: status is not provenance of approval; graph-only edits can be lost on rebuild; external concurrent writes untested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return [p for p in self.proposals if p.status == "CONFIRMED"]
> --- `src/sift_kg/resolve/models.py`

> if merge_stats.get("merges_applied", 0) or rejected_count:
>     kg.save(graph_path)
> --- `src/sift_kg/pipeline.py`

#### RT-RTE-narrative-generation
Label: Graph and extraction excerpts to prose and community labels

Owner/progression: CLI/library reload graph; code ranks entities, selects overview inputs, finds chains/timeline candidates and calls the model in separate phases. Description calls use entity neighborhoods and cached extraction quotes. Regex matches identify unwanted phrases; another model call rewrites flagged prose. Code then writes Markdown/descriptions and may create themed communities; communities-only mode skips the full narrative. Trigger/proposed change: explicit narration regenerates retained prose/labels. Admission: model output after text processing and assembly, without per-content human approval or factual oracle. Failure recovery uses fallback overview text, omitted descriptions or original prose on rewrite failure; user can rerun or replace outputs, not roll back through an inspected version journal. Mode: open generation plus local style correction, not a bounded accuracy experiment. Guidance includes graph/source excerpts, domain context and style rules; no inspected route revises the shipped method in response to results. Evidence: SRC-1, `src/sift_kg/narrate/generator.py`, `src/sift_kg/narrate/prompts.py`, `src/sift_kg/pipeline.py`.

- Immediate return: narrative.md path, description JSON and optional community labels; communities-only returns communities.json.
- Later read-back: viewer/search can consume descriptions; topology/query can consume community labels; skill lists narrative as an optional retained artifact.
- Delegated visibility: overview capped at 50 entities and 150 selected relations; at most 250 degree-qualified entities receive descriptions; source quotes and other phase-specific inputs are constructed separately.
- Selection predicate: graph degree and phase-specific structural rules; descriptions require degree at least three; phrase matches trigger rewrite; themed community cache can skip relabeling.
- Invalidation or expiry: explicit regeneration replaces artifacts; themed cache test is label-based, not graph-revision-based; no universal freshness guarantee.
- Activation or effect: model prose/labels are stored directly; phrase rewriting requests preservation of facts but does not validate it or guarantee all banned phrases disappear.
- Evidence limits: style correction is not factual validation, theory criticism or demonstrated improved capacity; budget only checks description admission, not every phase.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Keep everything else EXACTLY the same. Do not add new information. Do not change facts. Only fix the flagged phrases.
> --- `src/sift_kg/narrate/generator.py:640-650`

#### RT-RTE-agent-retrieval
Label: Later graph reload to agent-visible topology or neighborhood

Owner/progression: human/external agent issues info/topology/query/search; CLI reloads artifacts and code returns JSON or optional human presentation. Query exact IDs take precedence; otherwise substring names/aliases are filtered by optional type and ranked by substantive degree. Neighborhood selection is BFS on a metadata-clean undirected graph, then directed edges are emitted from the original graph with exclusions. No model answers the question inside query. Topology returns community summaries, bridges, connections and isolated entities, not a complete graph dump. The external agent owns further queries and final response. Mode: open retrieval; no answer oracle or change admission in this read route. Evidence: SRC-1, `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py`, `.agents/skills/sift-kg/SKILL.md`.

- Immediate return: JSON match/subgraph, other_matches on ambiguity, topology summary or search results; missing match returns empty arrays.
- Later read-back: this is the later consumer of retained graph/community state; the read route itself writes no accumulated memory.
- Delegated visibility: external host receives selected JSON by CLI stdout; host tool-result handling and downstream compliance are uninspected.
- Selection predicate: requested output directory, exact ID or name/alias substring, optional type on fuzzy route, degree ranking, requested hop depth; exact DOCUMENT match can survive only in match metadata.
- Invalidation or expiry: every invocation reloads files; no consistent-snapshot/version check across graph and community sidecars is shown.
- Activation or effect: graph data is delivered to a caller; changed host answers or ideas are not established by delivery.
- Evidence limits: external agent execution/context management remains outside target; topology can be stale after graph-only apply until assignments are regenerated.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> candidates.sort(key=lambda c: _sub_degree(c[0]), reverse=True)
> matched_id = candidates[0][0]
> --- `src/sift_kg/cli.py`

### Claims

#### RT-CLM-second-brain
Label: Persistent understanding for external agents

Claimed operation: graph reload should orient an agent and ground its answers across sessions. This is shipped host doctrine, not evidence that a host complied or benefited. The implemented retrieval affordance is [RT-RTE-agent-retrieval](#rt-rte-agent-retrieval). Evidence: SRC-1, `.agents/skills/sift-kg/SKILL.md`.

> **Treat the graph as your persistent understanding of the user's world.**
> --- `.agents/skills/sift-kg/SKILL.md`

#### RT-CLM-incremental-extraction
Label: Changed-document reuse promise

Claimed operation: only new/changed documents are processed. The implemented stale predicate is narrower, as traced in [RT-RTE-document-extraction](#rt-rte-document-extraction) and the forcing case. Evidence: SRC-1, `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/extract/extractor.py`.

> Extraction is cached — only new/changed documents are processed on re-run.
> --- `.agents/skills/sift-kg/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-domain-guidance
Label: Retained schema to later extraction and build behavior

Consumer: extraction prompt builders and graph-build code. Channel: discovered/custom domain YAML loaded as DomainConfig. Force: natural-language descriptions/hints request model interpretation; symbolic vocabulary/config fields constrain selected deterministic transformations, not every graph input. Horizon: later chunks and later CLI/API invocations using the same output/domain settings. [RT-RTE-schema-discovery](#rt-rte-schema-discovery) installs the content; [RT-RTE-document-extraction](#rt-rte-document-extraction) and [RT-RTE-graph-build](#rt-rte-graph-build) consume it. Evidence: SRC-1, `src/sift_kg/domains/discovery.py`, `src/sift_kg/extract/prompts.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/pipeline.py`.

> cached_domain = load_discovered_domain(discovered_path)
> if cached_domain is not None and not force:
>     logger.info(f"Using cached discovered schema ({len(cached_domain.entity_types)} entity types)")
>     domain = cached_domain
> --- `src/sift_kg/extract/extractor.py`

#### RT-BAP-host-skill
Label: Agent skill to external host operations

Consumer: external agent reading the bundled skill. Channel/substrate: natural-language Markdown at .agents/skills/sift-kg/SKILL.md. Force: asks the host to orient each session, query before answering domain questions and confirm paid extract/resolve operations. The target CLI does not enforce that host confirmation protocol. Horizon: prescribed sessions and task-specific retrieval, not an observed continuing host state. Symbolic CLI command examples supply callable operations; instruction uptake remains external. Evidence: SRC-1, `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/cli.py`.

> **Always confirm with the user before running extract or resolve** — these make LLM API calls that cost money.
> --- `.agents/skills/sift-kg/SKILL.md`

## Annotations

none
