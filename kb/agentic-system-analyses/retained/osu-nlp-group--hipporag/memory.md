---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "HippoRAG document memory: derived search structures, provenance-sensitive withdrawal, response reuse and passage delivery at the frozen revision."
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
source-identity: https://github.com/OSU-NLP-Group/HippoRAG
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
---

# HippoRAG memory report

## Boundary and evidence

This account covers the whole-system document-memory boundary in boundary.md: Python indexing/reload/deletion, graph and dense retrieval, QA, offline extraction, StandardRAG, MCP and plugin maintenance guidance. SRC-1 implementation and doctrine/design are the evidence layers. There is no observed-run or causal-experiment evidence. The checkout HEAD was rechecked as d5c8329422e0a0b834a15874545cb6a74b4f9b26. Source identity and scope remain those of the supplied boundary.

Direct reads covered core mutation, OpenIE merge/save/reload, retrieval preparation, query-vector reuse, graph selection, synonym construction and QA in `src/hipporag/HippoRAG.py`; `src/hipporag/embedding_store.py`; `src/hipporag/preprocessing.py`; `src/hipporag/rerank.py`; the cache wrapper in `src/hipporag/llm/openai_gpt.py`; normalization/reformatting in `src/hipporag/utils/misc_utils.py`; selection defaults in `src/hipporag/utils/config_utils.py`; StandardRAG initialization/mutation; the complete MCP server and both plugin skills. These are SRC-1 implementation except the skills' doctrine/design. Entry-point and backend searches supplemented the supplied runtime account; they do not establish complete adapter equivalence.

| Operation or part | Source path | Coverage and limit |
| --- | --- | --- |
| Preprocess, index, reject, delete and reload | `src/hipporag/HippoRAG.py`, `src/hipporag/preprocessing.py`, `src/hipporag/embedding_store.py` | Direct; [RT-RTE-index-state](runtime.md#rt-rte-index-state), object records below and index annotation. No crash experiment. |
| Compatibility manifest | `src/hipporag/utils/state_utils.py` | Supplied [RT-OBJ-index-manifest](runtime.md#rt-obj-index-manifest) and [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility), not independently reread helper internals. Cannot strengthen configuration compatibility into atomicity or truth. |
| Online and alternate extraction | `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/information_extraction/openie_vllm_offline.py`, `src/hipporag/information_extraction/openie_transformers_offline.py` | Supplied [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction) and [RT-RTE-index-state](runtime.md#rt-rte-index-state); direct field searches plus direct merge/save inspection. Offline engine behavior unobserved. |
| Fact selection, graph search, DPR, supplied solutions and QA | `src/hipporag/HippoRAG.py`, `src/hipporag/rerank.py` | Direct normal selection/QA; alternate DPR and supplied-solution bypass supplied by [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). |
| IRCoT thoughts and merged passages | `src/hipporag/HippoRAG.py`, `src/hipporag/utils/qa_utils.py` | Supplied [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval); no independent full loop reread. Current-call state, not demonstrated durable thought memory. |
| StandardRAG | `src/hipporag/StandardRAG.py`, `main.py` | Direct initialization/index; remainder supplied by [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag). Separate dense baseline, not graph storage. |
| CLI and tools | `src/hipporag/mcp_server.py`, `pyproject.toml`, `setup.py`, `plugins/hipporag/.claude-plugin/plugin.json` | Complete server read and entry-point/launcher search; [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools). All five registered tools and config resource checked. No hook-based memory admission appears in inspected server dispatch; plugin host internals uninspected. |
| Folder admission and refresh | `plugins/hipporag/skills/hipporag-memory/SKILL.md`, `plugins/hipporag/skills/index-folder/SKILL.md` | Both direct; [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills). Host compliance only claimed. |
| Response reuse | `src/hipporag/llm/openai_gpt.py` | Direct; [MEM-RTE-response-reuse](#mem-rte-response-reuse). Other provider caches remain uninspected; no universal cache lifecycle claim. |
| Alternate vector substrates | `src/hipporag/vector_stores/qdrant_store.py`, `src/hipporag/vector_stores/chroma_store.py`, `src/hipporag/vector_stores/milvus_store.py`, `src/hipporag/vector_stores/naming.py` | Factory read and scoped interface/content/persistence searches only. Backends expose content/vector collections and reload caches; external database semantics, ordering and concurrent deletion guarantees remain uninspected. |
| Shipped consumers and evaluation | `main.py`, `examples/_shared.py`, `tests/integration/_shared.py` | Supplied runtime lifecycle plus call-site searches. Gold-reference scores are post-generation evaluation, not content admission. |
| Shipped extraction fixtures and datasets | `outputs/`, `reproduce/dataset/` | Included but contents uninspected. No verified fixture provenance, corpus-quality or reproducibility conclusion. |

Remote model/provider state, external database internals and the enclosing host remain opaque. Bulk fixtures and available alternate adapters are not access failures. Their limits prevent universal semantic, privacy, durability and benefit claims without preventing the source-grounded default lifecycle account.

## Core ideas

HippoRAG retains original passages and builds a separate search representation from them. Model-generated triples, normalized entity/fact strings, embeddings and source-aware graph edges change which passages later reach a consumer. QA still receives original passage text rather than the complete graph. This separation preserves source text while allowing extraction mistakes to alter access to it. [RT-RTE-index-state](runtime.md#rt-rte-index-state), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer).

Content hashes are identities; `source_id` is replaceable metadata. Consequently, identical text from two sources is not two independently owned passages. Deletion preserves shared facts across different retained chunk hashes, but does not implement multi-owner provenance for the same text. [MEM-OBJ-chunk-metadata](#mem-obj-chunk-metadata), [MEM-OBJ-openie-state](#mem-obj-openie-state).

“Recognition memory” is a query-time model filter, not a durable critique or learned method. The filter constrains output to candidate triples using nearest-string matching; empty output causes dense fallback. It need not accept a semantically correct triple. “Retrieve makes no LLM call” in the skill is therefore not a universal implementation fact. [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills).

Context control is primarily count-bounded selection by value. The full corpus stays outside each prompt; candidates reach filtering, and a passage prefix reaches QA. Defaults are five linked candidates, 200 returned passages and five QA passages, not a total prompt-token budget. MCP retrieval separately bounds requested `top_k` to 1–100. Default preprocessing leaves each submitted document intact; host skill chunking is guidance rather than a server token cap. SRC-1: `src/hipporag/utils/config_utils.py`, `src/hipporag/mcp_server.py`, `src/hipporag/preprocessing.py`.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-passage-text
Label: Retained passage text

Source-native identity: chunk store `content` rows. Storage: default `vdb_chunk.parquet`, reopened into mappings; alternative collections are named in the coverage table. Representational form: natural-language content at extraction and QA; chunk hashes are symbolic access identities. Lineage: caller strings or `Chunk.content`, unchanged by the default preprocessor. The caller supplies content; generic caller identity does not establish human authorship, editing or approval. This is source material, not an execution log or summary. Closest supplied record is [RT-RTE-index-state](runtime.md#rt-rte-index-state), a lifecycle route rather than this retained object. SRC-1: `src/hipporag/preprocessing.py`, `src/hipporag/embedding_store.py`, `src/hipporag/HippoRAG.py`.

> docs = [self.chunk_embedding_store.get_row(key)["content"] for key in passage_keys]
> --- `src/hipporag/HippoRAG.py`

Later consumers: extraction model interprets content to propose structures; retrieval returns selected text; QA interprets a prefix. These are knowledge inputs, not a code-level grant or verified instruction hierarchy. Exact-text delete removes chunk membership; changing a source's text without deleting its old text adds another hash.

#### MEM-OBJ-entity-text
Label: Normalized entity strings

Source-native identity: entity store `content` strings, default `vdb_entity.parquet`. Representational form: localized symbolic identity strings for hashing, equality and graph mapping, with natural-language meaning supplied to the encoder. Lineage is normalized triple subjects/objects, not simply the complete NER entity list. Code deduplicates, persists and deletes unreferenced entities; no human approval is required by this transformation. The distinct object is produced by [RT-RTE-index-state](runtime.md#rt-rte-index-state). SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/misc_utils.py`, `src/hipporag/embedding_store.py`.

> triple_entities.update([t[0], t[2]])
> --- `src/hipporag/utils/misc_utils.py`

Entity strings identify search nodes; they are not independently established claims of truth or a whole-passage summary. Their vectors have a separate role below.

#### MEM-OBJ-fact-text
Label: Normalized fact strings

Source-native identity: fact store `content`, default `vdb_fact.parquet`, containing stringified normalized triples. Form: symbolic tuple structure decoded by code; natural-language relation content interpreted by the encoder and fact-filter model. Lineage: extracted triples, case/punctuation/whitespace normalization, deduplication and `str(fact)`. This material is derived knowledge, without a retained argument for why each relation is true. Distinct output object of [RT-RTE-index-state](runtime.md#rt-rte-index-state), later selected by [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/misc_utils.py`.

> self.fact_embedding_store.insert_strings([str(fact) for fact in facts])
> --- `src/hipporag/HippoRAG.py`

Filter interpretation controls search seeds, not permanent deletion or adoption of a revised fact. A failed match or empty selection can change the current route to dense retrieval without changing the retained fact text.

#### MEM-OBJ-passage-embeddings
Label: Passage embeddings

Source-native identity: chunk store `embedding` arrays, default Parquet column plus in-memory passage arrays. Form: distributed-parametric dense representation, not localized proposition text. Caller content is encoded by [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model); vectors persist for later dense similarity and passage seed weights. Rows are added/deleted, not trained by QA outcomes. Exact producer weights are not pinned; mutable endpoints can change model resolution. Encoder parameters and stored vectors are distinct state. Closest supplied route: [RT-RTE-index-state](runtime.md#rt-rte-index-state); StandardRAG has an analogous separately initialized chunk store through [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag), not necessarily the same index. SRC-1: `src/hipporag/embedding_store.py`, `src/hipporag/HippoRAG.py`, `src/hipporag/StandardRAG.py`.

> missing_embeddings = self.embedding_model.batch_encode(texts_to_encode)
> self._upsert(missing_ids, texts_to_encode, missing_embeddings)
> --- `src/hipporag/embedding_store.py`

#### MEM-OBJ-entity-embeddings
Label: Entity embeddings

Source-native identity: entity store `embedding` arrays, default Parquet and loaded entity arrays. Form: distributed-parametric. Lineage: normalized entity strings → configured encoder → persisted dense vectors. Later KNN similarity proposes synonym edges; code threshold/top-k admission, not semantic adjudication, decides their retention. Addition/deletion changes stored representations without encoder training. Producer fixity limits are those of [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). Distinct from the passage-vector object and the lifecycle in [RT-RTE-index-state](runtime.md#rt-rte-index-state). SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/embedding_store.py`.

> query_entity_embs = self.entity_embedding_store.get_embeddings(query_node_keys)
> entity_embs = self.entity_embedding_store.get_embeddings(entity_node_keys)
> --- `src/hipporag/HippoRAG.py`

#### MEM-OBJ-fact-embeddings
Label: Fact embeddings

Source-native identity: fact store `embedding` arrays, default Parquet and loaded `fact_embeddings`. Form: distributed-parametric. Lineage: normalized fact strings → encoder → stored vectors. Query vectors select candidate fact strings for the filter; the filter receives strings, not opaque vector coordinates. Store additions/deletions are not encoder parameter updates; exact producer weights remain unpinned as recorded in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). Closest supplied consumer is [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), a route rather than this object. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/embedding_store.py`.

> self.fact_embeddings = np.array(self.fact_embedding_store.get_embeddings(self.fact_node_keys))
> --- `src/hipporag/HippoRAG.py`

#### MEM-OBJ-openie-state
Label: OpenIE state

Source-native identity: `openie_state.json` in the working directory, optional exported `openie_results_ner_*.json`, and loaded `_openie_info`. Form: symbolic JSON schema and provenance plus natural-language passages/entities/triples. Storage forms are alternative inputs to the same loader, not separate evidence sources. Preferential read order is local state then export. File-level provenance and duplicate/coverage checks gate reuse; older IDs are recomputed from passage text. Model proposals are admitted by structural checks, not a truth oracle. Distinct retained object traversed by [RT-RTE-index-state](runtime.md#rt-rte-index-state) and [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction). SRC-1: `src/hipporag/HippoRAG.py`.

> merged_rows.append({'idx': chunk_key, 'passage': passage, 'extracted_entities': entities, 'extracted_triples': triples})
> --- `src/hipporag/HippoRAG.py`

That persisted row is derived extraction plus its source passage, not the complete raw response, usage metadata or rationale. Reload reconstructs extraction containers with `response=None` and empty metadata. Later index construction, retrieval preparation and deletion read this state to recover source mappings. Cached raw model messages can survive independently; they are not read by preparation as reasons for individual edges. SRC-1: `src/hipporag/utils/misc_utils.py`, `src/hipporag/HippoRAG.py`.

#### MEM-OBJ-chunk-metadata
Label: Chunk metadata

Source-native identity: `chunk_metadata.json`, loaded `chunk_metadata`. Form: symbolic per-hash mapping, carrying arbitrary caller JSON whose internal meaning is opaque to core selection. Substrate: local JSON and process memory. Lineage: copied `Chunk.metadata`, overridden with explicit `Chunk.source_id` when supplied. It is provenance/access metadata, not an authenticated source assertion or a second passage identity. Distinct object within the writes of [RT-RTE-index-state](runtime.md#rt-rte-index-state), and consumed by [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools). SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/mcp_server.py`.

> self.chunk_metadata[chunk_id] = metadata
> --- `src/hipporag/HippoRAG.py`

Repeated identical text can replace its metadata even when no embedding or extraction is added. Later retrieval returns that metadata; MCP source deletion matches its current `source_id` then deletes exact text. Two sources with identical text therefore cannot rely on separately retained ownership in this mapping. Source identifiers support targeting and display, not authorization. QA prompt construction uses passage text, not this metadata.

#### MEM-OBJ-graph-state
Label: Source-aware graph

Source-native identity: `self.graph`, persisted via `_graph_pickle_filename`; storage is local pickle and an igraph instance. Form: symbolic vertices/edges and fixed-rule numerical weights, distinct from dense vector representations. Lineage: normalized triples, passage links, source-count attribution and entity-similarity edges. Software controls construction; thresholded similarity does not prove synonymy. Later PPR propagates query-dependent weights over an undirected projection. Distinct retained product of [RT-RTE-index-state](runtime.md#rt-rte-index-state), read by [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). SRC-1: `src/hipporag/HippoRAG.py`.

> self.graph.write_pickle(temporary_path)
> os.replace(temporary_path, self._graph_pickle_filename)
> --- `src/hipporag/HippoRAG.py`

Source counts let deletion remove one chunk's fact contribution while preserving other chunk support and independent synonym weights. Graph state shapes ranking, not directly the wording of a QA instruction. It retains attribution needed for withdrawal, not a criticism history establishing relations' correctness.

#### MEM-OBJ-response-cache
Label: Model response cache

Source-native identity: SQLite `cache` table in `CacheOpenAI.cache_file_name`. Storage: local `llm_cache` database. Form: symbolic request digest and metadata plus natural-language raw message. Lineage: successful model response before downstream interpretation; raw output is distinct from selected/normalized OpenIE rows. This is not a human-authored memory or an opaque weight checkpoint. The closest supplied mention is response reuse within [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer); the table object is not separately declared there. SRC-1: `src/hipporag/llm/openai_gpt.py`.

> "INSERT OR REPLACE INTO cache (key, message, metadata) VALUES (?, ?, ?)",
> (key_hash, message, json.dumps(metadata)),
> --- `src/hipporag/llm/openai_gpt.py`

Its later consumers are matching inference requests through the wrapper, not graph traversal. The digest provides exact-request reuse, not semantic memory selection. Metadata does not prove immutable provider weights. This bounded raw-response reuse can affect future extraction/QA without constituting outcome-directed method revision.

### Routes

#### MEM-RTE-response-reuse
Label: Response cache reuse

Distinct route: the CacheOpenAI wrapper's persistence/replay subroute, shared across inference roles rather than coextensive with [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) or [RT-RTE-index-state](runtime.md#rt-rte-index-state). Trigger: inference request. Owner/selector: wrapper code. It normalizes generation parameters and incorporates messages, provider class, endpoint, Azure settings and schema into a SHA-256 key. On hit it returns retained message/metadata; on miss it calls the provider then writes the result. `store=True` bypasses this local cache. SRC-1 implementation: `src/hipporag/llm/openai_gpt.py`.

- Immediate return: message, metadata and cache-hit boolean to extraction, filtering or QA caller.
- Later read-back: a matching later inference invocation receives the retained message and metadata instead of fresh provider generation.
- Delegated visibility: a hit remains local; a miss passes the request to the configured inference provider. Other adapters are not covered by this wrapper finding.
- Selection predicate: exact normalized request digest equality, not similarity, usefulness or truth.
- Invalidation or expiry: no expiry or document-delete cascade occurs in the inspected wrapper/core delete methods; request changes select other keys. `store=True` bypasses lookup/write. Endpoint weight drift is not itself encoded as an immutable weight revision.
- Activation or effect: hit branch is wired to replace inference output; actual hits or downstream behavioral changes were not observed.
- Evidence limits: source-level wrapper only, not all providers, deployed cache access or a secure-erasure experiment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software-controlled after provider return, before the downstream extraction/filter/QA semantic interpretation. The provider proposes text, the wrapper retains it, and later parsers/consumers can reject or filter it without deleting that cache entry. There is no per-response human approval or answer oracle in this route. Open and benchmark calls use the same cache mechanism; benchmark scores do not govern admission. Recovery is fresh requests or external file management, not a demonstrated coupled rollback with knowledge deletion. Guidance remains the request's prompt, not a retained revised method.

> if row is not None:
>     message, metadata_str = row
>     return message, json.loads(metadata_str), True
> --- `src/hipporag/llm/openai_gpt.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Memory-specific write agency: caller content enters the default preprocessor unchanged; extraction proposes entities/triples, while normalization, deduplication and graph construction are software transformations. Physical persistence is not evidence of human approval. The host skill requests approval for large batches and some deletions, but direct Python/MCP callers do not require such content approval. Source trust is caller provenance plus producer compatibility, not factual verification. SRC-1: `src/hipporag/preprocessing.py`, `src/hipporag/HippoRAG.py`, `src/hipporag/mcp_server.py`, `plugins/hipporag/skills/hipporag-memory/SKILL.md`.

Retained lineage separates original passage text, extracted rows, normalized strings, vectors, graph attribution and metadata through the objects above. Casefolding and punctuation removal can collapse distinct surface strings; this is implemented curation, not demonstrated preservation of every meaning. SRC-1: `src/hipporag/utils/misc_utils.py`.

> normalized = ''.join(character if character.isalnum() or character.isspace() else ' ' for character in text.casefold())
> return ' '.join(normalized.split())
> --- `src/hipporag/utils/misc_utils.py`

Deletion updates the loaded/exported OpenIE state, stores, graph contributions and chunk metadata. It retains shared triple/entity references from surviving chunks. This prevents stale deleted-source graph support on the traced path, but does not imply raw-response erasure, removal of a fact independently supported elsewhere, or transactional multi-file withdrawal. SRC-1: `src/hipporag/HippoRAG.py`.

> if remove_sources_from_mapping(self.proc_triples_to_docs, str(processed_triple), chunk_ids_to_delete):
>     unreferenced_processed_triples.append(processed_triple)
> --- `src/hipporag/HippoRAG.py`

#### On [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer)

Read-back is caller-requested: a question triggers code similarity selection, model filtering and graph/dense ranking. Automatic internal selection is not unsolicited memory injection. Persisted fact vectors choose candidate strings; filtering interprets those strings; original passages are finally copied by value into returned solutions and QA prompts. The retained graph itself is not put in the QA window. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/rerank.py`.

The QA consumer receives neither source metadata nor the full extracted evidence/rationale history in this path. It receives passage text and question within a static dataset template. This gives knowledge content influence through model interpretation, not guaranteed obedience or verified grounding. Static examples stay separate from memory accumulated through use. SRC-1: `src/hipporag/HippoRAG.py`.

> for passage in retrieved_passages:
>     prompt_user += f'Wikipedia Title: {passage}\n\n'
> prompt_user += 'Question: ' + query_solution.question + '\nThought: '
> --- `src/hipporag/HippoRAG.py`

Context budgeting uses item counts, not a demonstrated aggregate token limiter. In-memory `query_to_embedding` retains query vectors for later requests on that prepared instance; preparation resets it after mutation. It is derived numerical access state, not a summary of reasoning or a learned selection policy. The source permits multiple query-instruction modes and may share query vectors when the encoder treats instructions as ignored/shared. SRC-1: `src/hipporag/HippoRAG.py`.

#### On [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools)

Later external consumer role is concrete: MCP `retrieve` returns passage text, rank, scores, `source_id` and metadata to the client; the memory skill tells the enclosing agent to answer from those passages and cite sources. This establishes wired server delivery and claimed host consumption, not observed host activation. `rag_qa` instead returns a server-generated answer and its QA passage prefix. `index_stats` and the redacted config resource are access/configuration views, not content-memory read-back. SRC-1: `src/hipporag/mcp_server.py`, `plugins/hipporag/skills/hipporag-memory/SKILL.md`.

> Read the passages, answer in your own words, and cite `source_id`s.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`

## Write side

Acquisition has two materially different admission surfaces. Python accepts strings/Chunks or a custom preprocessor; the default does not chunk. The plugin asks the host to read files, skip hidden/build/binary/large content, drop boilerplate, split at boundaries and carry headings before calling MCP. That is a host-interpreted transformation and selective admission policy, not an implemented server crawler. Its initial source choices, editing and human confirmations remain unobserved. [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills), [MEM-OBJ-passage-text](#mem-obj-passage-text).

The durable transformation chain is passage → model extraction → persisted extracted rows → normalized entity/fact strings → vectors and attributed graph. The content is retained knowledge, not a trace of HippoRAG's success or failure at using it. Raw inference text can persist separately in the response cache; OpenIE rows omit response metadata and reasons. Later preparation reconstructs source mappings from the extracted rows and passages, not from a rationale or outcome critique. [MEM-OBJ-openie-state](#mem-obj-openie-state), [MEM-OBJ-response-cache](#mem-obj-response-cache), [RT-RTE-index-state](runtime.md#rt-rte-index-state).

Rejection is layered: malformed extraction/online batch failures, schema and provenance checks, and graph/store coverage checks can prevent further progress. Earlier passage/metadata persistence can already have occurred. Offline vLLM staging retains OpenIE then intentionally raises pending online construction; Transformers-offline is a separate path. These alternatives prevent interpreting any single rejection policy as universal. [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction), [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility).

Maintenance includes missing-hash deduplication, metadata replacement, incremental synonym links, explicit delete/rebuild and skill-guided delete-then-index refresh. Delete-then-index is not atomic replacement: a failed new index can leave the old source withdrawn. Repeated identical text is not entirely a no-op because metadata can change. No benchmark-outcome-directed retained method update is established by these inspected routes. That limit does not deny the implemented new-document memory or response reuse. [MEM-OBJ-chunk-metadata](#mem-obj-chunk-metadata), [MEM-OBJ-graph-state](#mem-obj-graph-state), [MEM-RTE-response-reuse](#mem-rte-response-reuse).

## Read-back

The shipped reload caller in [RT-RTE-index-state](runtime.md#rt-rte-index-state) establishes a source-level cross-instance consumer, not just an API's hypothetical capability. Persistent stores/graph/metadata reload; preparation reconstructs derived mappings and arrays. Runtime-supplied StandardRAG provides a graph-free later consumer, and IRCoT repeats index reads using generated thoughts. Its current-call thought accumulation is not host compaction or durable thought admission. [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag), [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval).

Normal selection and its count budgets are described in the retrieval annotation. Direct DPR and caller-supplied `QuerySolution` bypass portions of that chain; the latter can send caller-selected passages directly to QA. That counterexample prevents attributing universal producer provenance to every QA input. Fact-filter rejection changes current selection rather than deleting retained facts. Response-cache read-back instead uses exact request identity and delivers raw previous output to the calling parser/QA procedure. [RT-OBJ-query-solution](runtime.md#rt-obj-query-solution), [MEM-RTE-response-reuse](#mem-rte-response-reuse).

For context-management purposes, these prompts receive selected values, not dereferenceable pointers into the corpus. The external stores remain reachable through another retrieval request; material not selected is not thereby deleted. No separate sub-agent frame or removal of old host turns is established by the inspected server/core selection paths. Opaque host context handling remains outside the boundary, not an evidenced global absence.

## Integration issues

- Qualification, not correction of the runtime: the runtime already rejects universal no-LLM/one-call guidance. The server's own instruction also calls repeated passage indexing a no-op, whereas metadata replacement is implemented. Preserve the narrower embedding/extraction deduplication claim and current-metadata deletion semantics. Evidence: SRC-1 `src/hipporag/mcp_server.py`, `src/hipporag/HippoRAG.py`; [MEM-OBJ-chunk-metadata](#mem-obj-chunk-metadata), [RT-RTE-index-state](runtime.md#rt-rte-index-state).
- Withdrawal does not establish secure forgetting. Core deletion does not cascade into the inspected response cache; prior raw outputs can remain. The cache route overlaps the runtime's brief response-reuse finding but has a distinct wrapper scope across extraction/filter/QA, so it should not replace the whole retrieval route. [MEM-RTE-response-reuse](#mem-rte-response-reuse), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). Source: SRC-1 `src/hipporag/llm/openai_gpt.py`, `src/hipporag/HippoRAG.py`.
- No new object duplicates a supplied object: comparison was against manifest and per-call query solution. New objects decompose retained material traversed by supplied routes; they are not alternative declarations of those routes. [RT-OBJ-index-manifest](runtime.md#rt-obj-index-manifest), [RT-OBJ-query-solution](runtime.md#rt-obj-query-solution).
- Open questions remain local: alternative provider cache lifecycles, backend persistence/concurrency, shipped fixture provenance and host approval/context behavior have not been established. These prevent universal deletion, producer-identity, performance and exercised-admission conclusions. The coverage table names their available/unavailable evidence. Producer weight fixity remains bounded by [RT-CMP-extraction-llm](runtime.md#rt-cmp-extraction-llm), [RT-CMP-qa-llm](runtime.md#rt-cmp-qa-llm) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model).

## Limitations and checks

The supplied run/source identity and checkout revision were rechecked without changing the frozen source. Governing member types, worker rules and records contract were read completely. Newly inspected files all belong to SRC-1 at the same commit; no additional source is declared. Target tests/examples/providers were not executed. Selection wiring does not prove activation, factual accuracy, secure erasure, successful recovery or improved future capacity. Explicit uninspected parts above remain limits, not absent mechanisms.

Validation: the invocation's `commonplace-run validate-output` completed successfully: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes the check's bounded content result, not analytical acceptance or causal benefit.
