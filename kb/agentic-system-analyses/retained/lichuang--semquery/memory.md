---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "semquery memory: persistent document parts, hybrid read-back, withdrawal and bounded answer context."
run-id: AAS-2026-11-09-semquery-b21559990932-01
source-identity: https://github.com/lichuang/semquery
reviewed-boundary: "0820927160b1400990fa8cc057807c73bbf6d025"
---

# semquery memory report

## Boundary and evidence

This report covers the shipped CLI, Engine and lower-level indexing, storage, retrieval and synthesis operations at SRC-1 commit `0820927160b1400990fa8cc057807c73bbf6d025`. The memory boundary includes document acquisition, extracted text, chunk construction, lexical/numerical derivatives, association and maintenance metadata, configuration, model caches, diagnostic logs and model-visible context selection. It excludes external document authorship, downstream applications, dependency internals and downloaded weights, as established in [boundary](boundary.md). Those exclusions prevent conclusions about original source truth, external caller policies and exact deployed model identity.

The supplied runtime is a provisional route account, not an inspection limit. Direct source reads confirm the core routes and add storage-part and withdrawal qualifications. All additional evidence below belongs to SRC-1 and supplies implementation evidence, except CLI help/comments where explicitly treated as declarations. No target code, tests or examples were executed. No observed run or causal experiment was supplied.

### Coverage inventory

Paths below are commit-relative SRC-1 anchors. “Direct” distinguishes new source inspection from reliance on supplied runtime findings. The table inventories memory operations rather than asserting exhaustive backend correctness.

| Entry point or operation | Source path and evidence basis | Covering records or local limit |
|---|---|---|
| CLI init/add/index hint/del/remove/status/search/ask | Direct: `crates/semquery/src/main.rs`, command enum, dispatcher, logger and add/delete handlers | [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation); annotations below cover withdrawal. Removed index CLI is a hint, not an alternate indexing worker. |
| Engine registration, add_file, del, del_document, remove_collection, clear_collections, index/index_one and stream variants | Direct: `crates/semquery/src/engine.rs`, registration/maintenance methods and lazy loaders; supplied runtime for search/ask stream forwarding | [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission). Library components may replace default storage/readers/models; deployed custom behavior is uninspected. |
| Directory and single-file indexer paths | Direct: `crates/semquery-indexer/src/indexer.rs`, constructor, baseline checks, file/directory/source methods, preparation, batching and sweep | [MEM-OBJ-chunks](#mem-obj-chunks), [MEM-OBJ-fts-chunks](#mem-obj-fts-chunks), [MEM-OBJ-vec-chunks](#mem-obj-vec-chunks), [MEM-OBJ-document-paths](#mem-obj-document-paths), [MEM-CLM-empty-retention](#mem-clm-empty-retention); direct file and source-loop wrappers differ but share automatic content admission. |
| Reader registration and acquisition | Direct: `crates/semquery-indexer/src/reader_registry.rs`, `crates/semquery-indexer/src/reader/txt_reader.rs`, `crates/semquery-indexer/src/reader/pdf_reader.rs`, `crates/semquery-indexer/src/reader/docx_reader.rs` | [MEM-OBJ-chunks](#mem-obj-chunks); text, PDF and DOCX extraction inspected, external extraction libraries not inspected. Extraction success does not establish faithful layout or complete content. |
| Chunking and lexical segmentation | Direct: `crates/semquery-indexer/src/chunker.rs`, `crates/semquery-indexer/src/tokenizer.rs` | [MEM-OBJ-chunks](#mem-obj-chunks), [MEM-OBJ-fts-chunks](#mem-obj-fts-chunks); tokenizer/dependency internals remain uninspected. |
| SQLite reopen, schema, insertion, associations, orphan cleanup and search operations | Direct: `crates/semquery-storage/src/sqlite.rs`, open/init, insertion/deletion helpers, get_chunks, path resolution and text/vector search | [MEM-OBJ-document-paths](#mem-obj-document-paths), [MEM-CLM-chunk-lineage](#mem-clm-chunk-lineage); lower-level mutations are storage capabilities, not evidence of an unidentified external consumer route. |
| Hybrid selector, reranking and retained chunk resolution | Direct: `crates/semquery-retrieve/src/retriever.rs`, recall and candidate preparation; supplied runtime for fusion progression | [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search). Reranker and embedder parameter-fixity findings remain supplied runtime findings, not new model-artifact inspection. |
| Both synthesis entry points, numbered prompt, inference trimming | Direct: `crates/semquery-synth/src/synthesizer.rs`, ask and streaming generation; `crates/semquery-synth/src/prompt.rs`; `crates/semquery-model/src/gguf.rs`, both completions | [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation), [RT-BAP-prompt-influence](runtime.md#rt-bap-prompt-influence); supplied runtime supports terminal citation-filter detail. |
| Config reload, symbolic controls and system-prompt editing | Direct: `crates/semquery/src/config.rs`, defaults/types/load; `crates/semquery/src/main.rs`, ensure_config | [MEM-OBJ-config](#mem-obj-config), [MEM-OBJ-system-prompt](#mem-obj-system-prompt), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission). Actual author and human approval of deployed edits are unknown. |
| Model cache/version metadata | Direct: `crates/semquery-model/src/hub.rs`, `crates/semquery/src/engine.rs`, lazy model and tokenizer loaders | [MEM-OBJ-document-paths](#mem-obj-document-paths); annotations on supplied model components. Cached files are not learned experience; their contents and exact deployed revisions are uninspected. |
| Diagnostics, evaluation and post-deletion probes | Direct: `crates/semquery/src/main.rs`, logging setup; `test-integration.sh`; reader/chunker/tokenizer inline tests encountered during source reads. Supplied runtime describes Engine tests | [MEM-OBJ-semq-log](#mem-obj-semq-log). Integration driver asks/searches after deletion but supplies no executed outcomes or answer-quality oracle; no warranted benefit conclusion. |
| Hooks, tool registration, service surface | Direct inventory: CLI enum/dispatch, Engine public operations, `crates/semquery/src/lib.rs` exports and `crates/semquery-core/src/traits.rs` signatures; scoped search of CLI/Engine/retrieve/synth for hooks/tool calls/evaluation | No additional model-selected tool or hook route was found in these inspected surfaces. README's unchecked MCP roadmap item is not shipped service wiring (SRC-1, `README.md`). This bounds the route inventory, not all possible injected implementations. |

## Core ideas

1. **Retained documents are separated from their retrieval machinery.** Text chunks, tokenized FTS text, dense vectors and symbolic ownership metadata are different operative parts with different consumers. Neither vector similarity nor a content hash supplies a truth judgment. See [MEM-OBJ-chunks](#mem-obj-chunks), [MEM-OBJ-fts-chunks](#mem-obj-fts-chunks), [MEM-OBJ-vec-chunks](#mem-obj-vec-chunks) and [MEM-OBJ-document-paths](#mem-obj-document-paths).
2. **Read-back is request-driven, then code-selected.** A query initiates hybrid recall and ranking; selected retained text becomes search output or a five-hit answer prompt. No independent unsolicited context supplier is established by these routes. Prompt delivery remains subject to tail truncation and model interpretation, not guaranteed use of every hit. See [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation) and their annotations.
3. **Maintenance is mechanical curation, not experience-driven revision.** Extraction, chunking, deduplication, embedding, hashing, reindexing and orphan removal alter representations and membership. They do not themselves revise document claims against answer outcomes. The inspected answer path does not write its answers back as knowledge; diagnostics remain separate. See [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [MEM-OBJ-semq-log](#mem-obj-semq-log) and [MEM-CLM-empty-retention](#mem-clm-empty-retention).
4. **Source identity and freshness are weaker than the display suggests.** Shared chunk text gets one stored range and a selected document identity; those can originate from different occurrences. Empty/unreadable-content transitions can preserve old indexed text. A valid source label does not establish current-file byte fidelity. See [MEM-CLM-chunk-lineage](#mem-clm-chunk-lineage), [MEM-CLM-empty-retention](#mem-clm-empty-retention) and supplied baseline-drift qualifications in [RT-RTE-index-admission](runtime.md#rt-rte-index-admission).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-chunks
Label: chunks text

Distinct retained output of [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), not another indexing route. Source-native identity: `chunks.text`, keyed by SHA-256 of its text. Representational form: natural language at the answer-model or human consumer. Storage: SQLite chunks table in the reopened workspace `semq.db`; full original files remain external, not stored as opaque PDF/DOCX payloads. Evidence: SRC-1, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-indexer/src/indexer.rs`.

Lineage: default text reader accepts UTF-8 txt/md/tex; PDF extraction produces text; DOCX reads word/document.xml and extracts text nodes, tabs and breaks. These are source extraction, not model summaries. SentenceSplitter constructs contiguous extracted-text slices with configurable token-sized grouping and overlap. It falls back from paragraphs/sentences to words/characters for long units and drops carried overlap when it would overflow. Byte positions therefore belong to the extracted string, not necessarily raw binary-file bytes. Reader and chunker internals inspected: SRC-1, `crates/semquery-indexer/src/reader/txt_reader.rs`, `crates/semquery-indexer/src/reader/pdf_reader.rs`, `crates/semquery-indexer/src/reader/docx_reader.rs`, `crates/semquery-indexer/src/chunker.rs`.

> let chunk_text = text[start..end].to_string();
> --- `crates/semquery-indexer/src/chunker.rs:137-149`

> id: sha256_hex(&c.text),
> --- `crates/semquery-indexer/src/indexer.rs`

Admission is software-controlled after source selection: extraction/chunking/storage success, not human review or semantic validation. Original authors and reasons are not recorded separately. Reasons present inside document text may survive slicing, but no rationale-preservation contract is implemented. Later consumers: reranker receives raw selected chunk text; search returns it; synthesis embeds it in numbered context. Authority is evidence-like natural-language influence, not executable instructions; actual reliance is unobserved. See [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-BAP-prompt-influence](runtime.md#rt-bap-prompt-influence).

#### MEM-OBJ-fts-chunks
Label: fts_chunks lexical text

Distinct lexical output of [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), consumed by [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), not a duplicate of either route or raw chunk text. Storage: FTS5 virtual table keyed with chunk IDs. Form: symbolic retrieval representation; fixed FTS rules consume segmented terms rather than interpreting claims as prose. Lineage: chunk text through Jieba segmentation, not answer traces or learned revisions. SRC-1, `crates/semquery-indexer/src/tokenizer.rs`, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-storage/src/sqlite.rs`.

> jieba().cut(text, false).join(" ")
> --- `crates/semquery-indexer/src/tokenizer.rs`

> let tokenized_texts: Vec<String> = chunk_texts.iter().map(|t| self.segmenter.segment(t)).collect();
> --- `crates/semquery-indexer/src/indexer.rs`

Automatic code admits lexical derivatives; no content-level human/model approval. Query terms are also segmented then sanitized for FTS syntax. The FTS index yields IDs/scores; it is not the text delivered in the answer prompt. Its authority is candidate selection, not truth or instruction authority. It is overwritten for inserted/reembedded IDs and removed on orphan sweep. Reuse of old shared chunks can retain earlier derivatives; changes to segmenter behavior are not independently tracked by the model/chunk-size baseline shown in indexer. This prevents claiming universal lexical freshness across arbitrary injected segmenters.

#### MEM-OBJ-vec-chunks
Label: vec_chunks embeddings

Distinct numerical output of [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), not the parameter-bearing [RT-CMP-fast-embed](runtime.md#rt-cmp-fast-embed). Form: distributed-parametric dense representation of chunk text, with symbolic chunk IDs. Storage: sqlite-vec FLOAT dimension table, serialized little-endian f32 input. Lineage: selected new/reembedded chunk texts through the embedder; no execution-feedback provenance is supplied. SRC-1, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-indexer/src/indexer.rs`.

> let all_embeddings = embedder.embed(&embed_texts).await?;
> --- `crates/semquery-indexer/src/indexer.rs`

> bytes.extend_from_slice(&f.to_le_bytes());
> --- `crates/semquery-storage/src/sqlite.rs`

Automatic admission follows the software keep-set and embedding success; dimensions are checked by storage initialization. Vectors change when software admits new/reembedded values, not through in-place online weight training in this route. The embedder's parameter fixity and unresolved exact model identity are separate supplied findings. Later consumer: cosine-distance recall using the current query vector. Effect: candidate eligibility/order before fusion and optional reranking, not direct language instructions. Reembedding uses delete/insert; orphan cleanup removes vectors. Search does not itself recheck configuration freshness. Successful retrieval quality and semantic fidelity are unobserved.

#### MEM-OBJ-document-paths
Label: Document and index metadata

Distinct symbolic retained control/access state associated with [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) and [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), not a duplicate of either route. Storage: SQLite documents, document_paths, chunk_documents, collections, model_versions and meta tables. These share code-controlled admission and fixed-rule consumption, but not identical lineage: caller path/name supplies registration; extraction/hash/time supply document fields; indexing supplies links and success baselines; hub ensure supplies configured model specs. SRC-1, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-model/src/hub.rs`.

> let content_hash = sha256_hex(content);
> let path_str = path.to_string_lossy().to_string();
> let doc_id = sha256_hex(&path_str);
> --- `crates/semquery-indexer/src/indexer.rs`

> storage.set_model_version_atomic(spec.role, spec)?;
> --- `crates/semquery-model/src/hub.rs:36-40`

The document hash is of reader-supplied extracted content, not necessarily original file bytes. Symbolic consumers: incremental indexer compares content hashes; baseline checks compare serialized ModelSpec and chunk size/overlap; ownership cleanup uses associations and registered roots; get_chunks selects one linked doc ID; path resolution builds display/citation metadata; status counts inventory. None of these fields establishes document truth. Model-version rows record configured specs, not authenticated exact embedding provenance, and are separate from the successful-index baseline. Deletion and baseline drift have the limits in supplied runtime and the annotations below.

#### MEM-OBJ-config
Label: config symbolic controls

Retained control object consumed on [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), not a second configuration route. Form: symbolic TOML fields for model specs, indexing, retrieval, generation and logging. Substrate: platform-default global config.toml or explicit selected file; in-memory parsed config during Engine use. The natural-language field is assessed separately in [MEM-OBJ-system-prompt](#mem-obj-system-prompt). SRC-1, `crates/semquery/src/config.rs`, `crates/semquery/src/main.rs`.

> let config: Self = toml::from_str(&text).map_err(|e| anyhow::anyhow!("parse config {}: {e}", path.display()))?;
> --- `crates/semquery/src/config.rs`

Default creation is automatic software authorship when absent. Later edits are external authorship; whether a human supplies/approves any deployed content is unknown. Code parses and may reject malformed/unsupported configuration; external authors can withhold, replace or restore it. Actual consumers apply fixed retrieval counts, chunk-size controls, model selection and generation limits. Persisted configuration gives behavior-determining authority across launches but retains no managed history or criticism/outcome record. Injected EngineComponents can bypass these defaults. See [RT-RTE-config-admission](runtime.md#rt-rte-config-admission).

#### MEM-OBJ-system-prompt
Label: system_prompt text

Natural-language part of configuration, stored in TOML then cloned into LlmConfig; distinct from the symbolic controls in [MEM-OBJ-config](#mem-obj-config). Closest supplied route/authority records are [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) and [RT-BAP-prompt-influence](runtime.md#rt-bap-prompt-influence), which describe consumption rather than this retained object. SRC-1, `crates/semquery/src/config.rs`, `crates/semquery-model/src/gguf.rs`.

> system_prompt: "You are a helpful assistant.".into(),
> --- `crates/semquery/src/config.rs`

Default text is shipped guidance, not use-derived memory; an externally edited saved replacement can recur across launches. No runtime-generated revision or per-content human approval is established. Concrete GGUF supplies it as a system message, subject to the same later formatted-token truncation as the user message. Its force is model-interpreted instruction, not a hard software guarantee. Its text may retain reasons if an author adds them, but there is no separate rationale store or later reason-directed reader established here. Deployment-specific replacements and compliance remain uninspected.

#### MEM-OBJ-semq-log
Label: semq diagnostic logs

Distinct diagnostic retention, not an index or future-answer memory route. Closest supplied records are [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) and [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), whose progress/errors can generate diagnostics. Substrate: configured/default workspace log files through flexi_logger, with size-based rotation and retained-file count. Form: human-readable natural-language event/timing/error text; file management uses symbolic configuration. No complete conversation-payload archive is established. SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/config.rs`, `crates/semquery-retrieve/src/retriever.rs`.

> Cleanup::KeepLogFiles(logging.max_files),
> --- `crates/semquery/src/main.rs`

Logs are automatic raw operational diagnostics, not derived recommendations, summaries or corrected knowledge. Software admits writes under log-level and rotation policy. They are potentially readable by an operator, but no inspected index/retrieval/synthesis path automatically selects them to revise future answers or policy. An operator could separately add a log as a document; that hypothetical admission is not demonstrated. Retention alone therefore does not establish a trace-fed learning route. No actual log artifact or consumer run is supplied.

### Routes

none declared in this member

### Claims

#### MEM-CLM-chunk-lineage
Label: Shared text versus occurrence provenance

Implementation finding: text deduplication preserves a single chunk's range, while read-back chooses one associated document independently. Closest supplied record: [RT-RTE-index-admission](runtime.md#rt-rte-index-admission); this is a distinct lineage qualification on its retained output [MEM-OBJ-chunks](#mem-obj-chunks), not another route. SRC-1, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-indexer/src/indexer.rs`.

> INSERT OR IGNORE INTO chunks (chunk_id, text, start_byte, end_byte)
>      VALUES (?1, ?2, ?3, ?4)
> --- `crates/semquery-storage/src/sqlite.rs`

> SELECT cd.doc_id FROM chunk_documents cd
>          WHERE cd.chunk_id = c.chunk_id
>          ORDER BY cd.doc_id LIMIT 1
> --- `crates/semquery-storage/src/sqlite.rs`

The countercase to exact provenance is identical chunk text at different positions in different files: one row's original range survives, while lexicographic doc ID selection need not select the originating occurrence. Many-to-many links preserve membership and prevent deletion of another document's shared text; they do not preserve per-occurrence ranges. Moreover, PDF/DOCX ranges refer to extracted text. The source display in [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation) cannot by itself certify exact source-file byte location. This is source-supported possibility, not an observed corrupted citation.

#### MEM-CLM-empty-retention
Label: Skipped content can retain old chunks

Implementation finding: reindexing an existing listed file that now yields no document or no chunk candidates can leave its old indexed content available. Distinct freshness qualification of [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), not a duplicate of its hash/config-drift finding. SRC-1, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-indexer/src/reader/txt_reader.rs`, `crates/semquery-indexer/src/reader_registry.rs`.

> Ok(Some(doc)) => doc,
>           Ok(None) => return Ok(None),
> --- `crates/semquery-indexer/src/indexer.rs`

> let candidates = self.chunker.chunk(content);
>     if candidates.is_empty() {
>       return Ok(None);
>     }
> --- `crates/semquery-indexer/src/indexer.rs`

Directory sweep checks presence in listed current_doc_ids before content reading. A now-empty supported file remains listed; the reader returns None, or the chunker produces no candidates, so it never enters the update/unlink write. Likewise invalid UTF-8 text is skipped by the text reader. This is not a semantic rejection that withdraws old knowledge. It prevents claiming that every completed add makes storage an exact current-file view. Actual stale retrieval is unobserved; explicit deletion remains a supported withdrawal path.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-index-admission](runtime.md#rt-rte-index-admission)

Memory lineage and admission: user/caller chooses a collection root or file, but software admits individual extracted slices, lexical terms and vectors automatically. Human document authorship and per-content approval are distinct and unknown for a deployed corpus. Text transformations are deterministic extraction/chunking plus model embedding; no answer/outcome record is an input to the inspected prepare/flush chain. Kept material is document content and retrieval/access state, not reasons for revising a system method. The split outputs are [MEM-OBJ-chunks](#mem-obj-chunks), [MEM-OBJ-fts-chunks](#mem-obj-fts-chunks), [MEM-OBJ-vec-chunks](#mem-obj-vec-chunks) and [MEM-OBJ-document-paths](#mem-obj-document-paths).

Withdrawal/read-back effects: del/remove unlinks solely owned documents under the selected collection, respecting surviving collection roots; del_document unlinks one canonicalized file; clear_collections removes all registrations and indexed documents. Indexer sweep separately removes missing listed-file IDs under a raw string prefix. SQLite orphan sweep removes chunks, FTS and vectors only when no links remain. Thus shared chunk text can remain available through other documents after a deletion. Source files are not edited. This narrows deletion to future index consumers, not removal of already returned answers, logs, external source files or model weights. SRC-1, `crates/semquery/src/engine.rs`, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-storage/src/sqlite.rs`.

> p.starts_with(&target_path) && !surviving.iter().any(|root| p.starts_with(root))
> --- `crates/semquery/src/engine.rs`

> let orphaned = "chunk_id NOT IN (SELECT chunk_id FROM chunk_documents)";
> --- `crates/semquery-storage/src/sqlite.rs`

A maintenance countercase matters: indexer sweep uses string starts_with rather than path-component containment and does not apply Engine del's surviving-root test. A directory prefix can match a sibling's longer name; therefore cleanup safety cannot be generalized from the explicit collection-delete implementation. This is a bounded implementation risk, not observed loss.

> if !file_path.starts_with(&dir_prefix) {
>         continue;
>       }
> --- `crates/semquery-indexer/src/indexer.rs`

Baseline updates retain serialized model spec plus chunk-size/overlap, consumed by later indexing checks. This is change detection, not experience learning or a search-time freshness barrier. Automatic storage errors can reject a write; transaction rollback protects uncommitted work only, as [RT-CLM-transaction-scope](runtime.md#rt-clm-transaction-scope) establishes. Explicit retry/reindex/deletion are the available recovery mechanisms, not an indexed revision history.

#### On [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search)

Read-back trigger/direction: a caller's query requests delivery; code automatically selects within that request, not independently unsolicited supply. Selector inputs are query text, query embedding, segmented/sanitized terms, persisted FTS/vector IDs and retrieval configuration. Defaults are BM25 100, vector 100, RRF smoothing 60, rerank prefix 20 (SRC-1, `crates/semquery/src/config.rs`). The optional no-reranker path can directly return fused top-k, so cross-encoder selection is not universal across injected clients. Returned retained parts are raw chunk text and selected document/path/range metadata, not vector/FTS payloads in the answer prompt. Supporting passage and alternate route are retained in the supplied record; concrete candidate handling was also read in SRC-1, `crates/semquery-retrieve/src/retriever.rs`.

Persistence/horizon: the index survives workspace reopen and later queries; candidate rankings and query embeddings are current-call working state. Reranking does not retain a revised chunk claim or permanent preference. The code can use retained material to shape the prompt without establishing relevance, compliance or improved future capacity. Scope/lineage caveats: [MEM-CLM-chunk-lineage](#mem-clm-chunk-lineage), [MEM-CLM-empty-retention](#mem-clm-empty-retention).

#### On [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation)

Working-context control: code excludes the nonselected corpus, retrieves at most five hits for synthesis, formats complete selected chunk texts plus paths/ranges/query, then the concrete GGUF adapter tokenizes the system/user template. Its prompt budget is max(1, n_ctx minus max_tokens); defaults n_ctx=8192 and max_tokens=512 are configuration, not universal capacity. Excess tokens are dropped from the beginning, preserving a suffix rather than a semantic summary. Both complete and complete_stream allocate fresh inference contexts. Citations are still checked against the pre-truncation offered hit set; the runtime's quote-backed truncation and citation countercase were confirmed by direct reads of SRC-1, `crates/semquery-model/src/gguf.rs`, `crates/semquery-synth/src/prompt.rs`, `crates/semquery-synth/src/synthesizer.rs` and defaults in `crates/semquery/src/config.rs`.

Removed material stays in the persisted index and can be selected by another query, but there is no within-generation dereference/reload operation or summary checkpoint on this inspected path. The query near the prompt suffix can survive while leading instructions or highest-ranked context vanish. The analogy is a fresh call frame returning answer text, not a separate subagent: no nested task owns an isolated reasoning context, and nothing acts as a model-followable pointer to dropped tokens. The returned answer is not persisted by this synthesis path; streaming deltas and terminal Answer are immediate output, not retained memory. Custom Llm implementations have uninspected context policies, so this finding is concrete-adapter scoped.

#### On [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)

The later-launch consumption chain is saved file → parsed symbolic controls and literal system-prompt text → adapter initialization and system-message construction. Code loads defaults if absent; actual edits are external. Consumers and forms differ between [MEM-OBJ-config](#mem-obj-config) and [MEM-OBJ-system-prompt](#mem-obj-system-prompt). Neither configuration persistence nor replaceable EngineComponents establishes runtime criticism or trace-driven revision. SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/config.rs`, `crates/semquery-model/src/gguf.rs`.

#### On [RT-CMP-fast-embed](runtime.md#rt-cmp-fast-embed)

Cache storage is distinct from corpus memory: model/cache artifacts are loaded into an inference object shared during Engine use; output vectors are separately retained in [MEM-OBJ-vec-chunks](#mem-obj-vec-chunks). ModelHub tracks configured specs in storage, but exact loaded embedding identity remains unresolved as the supplied adapter record explains. Direct inspection of SRC-1, `crates/semquery-model/src/hub.rs` and `crates/semquery/src/engine.rs` adds no weight-artifact verification or model-training evidence.

#### On [RT-CMP-fast-reranker](runtime.md#rt-cmp-fast-reranker)

Cached cross-encoder artifacts/shared inference state produce per-query scores; those scores order candidates rather than updating the persistent corpus. No retained reranking outcome-to-policy route is established by the inspected candidate-preparation implementation (SRC-1, `crates/semquery-retrieve/src/retriever.rs`). Parameter fixity and exact-version limits remain the supplied record's findings. A readable score explanation is not a readable display of the model's distributed parameters.

#### On [RT-CMP-gguf-llm](runtime.md#rt-cmp-gguf-llm)

Model weights persist in the hub cache while generation state does not persist as a conversation. Each completion allocates a new context; this was directly checked in SRC-1, `crates/semquery-model/src/gguf.rs`. ModelHub resolves repo/revision/filename and may record the spec, not a checksum-authenticated record of the actual deployed weights (SRC-1, `crates/semquery-model/src/hub.rs`). No summary/answer checkpoint is reloaded by either completion method. This does not constrain an injected alternative Llm or unseen dependency internals.

#### On [RT-BAP-prompt-influence](runtime.md#rt-bap-prompt-influence)

Retained natural-language chunks and configured system text reach model interpretation through different message roles but one eventually truncated formatted token sequence. Chunk provenance, not content review, is the trust boundary here: prompt construction interpolates retained text directly, with textual separators and citation instructions. The record's own supporting passage and [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation) support the request/force distinction; direct prompt construction read confirms no hard passage-level authority gate (SRC-1, `crates/semquery-synth/src/prompt.rs`). This establishes an influence channel, not measured instruction-following or prompt-injection success.

## Write side

Acquisition begins with a supplied path/name, not a model deciding what to remember. Canonical registration precedes CLI indexing; lower-level library callers may supply arbitrary registered readers, storage or model components. Automatic file eligibility rejects ignored/unsupported paths, skips empty/invalid-data text, and propagates extraction errors. File traversal errors are skipped; they are not human rejection decisions. Reader extraction and SentenceSplitter/segmenter transformations build source slices and retrieval representations. Content hashes skip unchanged extracted text; keep-sets avoid embedding duplicate chunk text, while reembedding can replace vectors. These checks admit representations, not warranted knowledge. Evidence and retained outputs: [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [MEM-OBJ-chunks](#mem-obj-chunks), [MEM-OBJ-fts-chunks](#mem-obj-fts-chunks), [MEM-OBJ-vec-chunks](#mem-obj-vec-chunks).

Curation includes source updates, association unlink/relink, deduplication, forced reembedding and orphan sweep. There is no guaranteed removal for a now-empty listed file ([MEM-CLM-empty-retention](#mem-clm-empty-retention)); registration replacement and partial commits are not a complete rollback protocol. A software admission failure may leave earlier batches retained. Explicit withdrawal changes later retrieval membership, subject to shared ownership and prefix-sweep qualifications in the index-admission annotation. A future query cannot retrieve a successfully removed sole-owned chunk through the removed index entries, but this says nothing about deletion of previous outputs or copies elsewhere.

Configuration admits externally authored literal controls/guidance, separate from automatic document transformation. Initial human versus software selection of deployed corpus/config is unresolved beyond the CLI/caller interfaces; subsequent extraction and admission are inspectable automation. No trace-fed compaction, alternative conversation checkpoint or outcome-derived method update is established in the inspected index/retrieve/synth/GGUF paths. Raw diagnostic retention is not such an update ([MEM-OBJ-semq-log](#mem-obj-semq-log)). The shipped integration driver probes post-deletion behavior, not a production evaluator that accepts/rejects document claims. No actual evaluator result feeds a durable behavioral update in the inspected chain (SRC-1, `test-integration.sh`). These limits do not turn external authoring or opaque provider internals into evidenced absences.

## Read-back

There are three materially different later-consumer chains:

- **Content chain:** committed chunk text plus FTS/vectors/associations → requested hybrid search → selected hits → caller or ask prompt → GGUF suffix-budgeted inference. Persistence spans workspace reopen; selection is query-dependent and default budgets are explicit in the route annotations. Source text acts as natural-language evidence/instruction-like influence, vectors/terms as selection machinery, and paths/ranges as access/display metadata. Delivered context does not establish activation or benefit. [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation).
- **Maintenance chain:** stored hashes/spec baseline/chunk configuration/registrations → later indexing, deletion or status invocation → code skip/reindex/unlink/count decisions. This is real later consumption of use-produced state, but not a reasoning summary or semantic criticism. Query-time freshness is not enforced by the baseline. [MEM-OBJ-document-paths](#mem-obj-document-paths), [RT-RTE-index-admission](runtime.md#rt-rte-index-admission).
- **Configuration/cache chain:** saved configuration and cached model/tokenizer artifacts → later CLI open/lazy component initialization → retrieval/context/inference behavior. Literal system text has model-interpreted force; numeric controls have fixed software semantics; opaque weights/tokenizer artifacts have unresolved deployed identity. [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), [MEM-OBJ-config](#mem-obj-config), [MEM-OBJ-system-prompt](#mem-obj-system-prompt), supplied model components.

Storage get/set APIs alone do not add an unspecified future-agent consumer route. Logs have potential operator access, not a demonstrated automatic read-back chain. Static shipped prompts/defaults are guidance, not material accumulated through use. There is no independently unsolicited push route in the inspected entry points; automatic selection occurs inside a requested search/ask, not as autonomous task initiation. The source-supported return is hits/answer, not a tool-using agent loop.

## Integration issues

- **No supplied fact requires withdrawal.** The runtime's main route account is retained, including its citation, transaction, baseline and truncation qualifications. The new objects identify retained parts where runtime declared no operative objects; they are not duplicate routes/components. Annotations reuse existing referents rather than redeclare them.
- **Lineage qualification:** [MEM-CLM-chunk-lineage](#mem-clm-chunk-lineage) qualifies [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) and [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation): shared-text ranges and selected document identity are not per-occurrence provenance. Storage insert/get_chunks evidence prevents exact source-location attribution from display alone. No observed bad citation supplied.
- **Freshness qualification:** [MEM-CLM-empty-retention](#mem-clm-empty-retention) adds a countercase beyond supplied hash/config drift: listed files skipped after becoming empty/invalid-data can keep old chunks. Reconciliation must not equate successful indexing with current-file mirroring.
- **Withdrawal qualification:** [RT-RTE-index-admission](runtime.md#rt-rte-index-admission)'s annotation separates safe path-component/surviving-root checks in explicit collection deletion from raw string-prefix directory sweep. The source supports a possible sibling-prefix cleanup hazard, not an observed deletion failure. Shared-chunk preservation and orphan cleanup are known independently of this qualification.
- **Model/initialization uncertainty:** [RT-CMP-fast-embed](runtime.md#rt-cmp-fast-embed), [RT-CMP-fast-reranker](runtime.md#rt-cmp-fast-reranker), [RT-CMP-gguf-llm](runtime.md#rt-cmp-gguf-llm) retain unknown exact deployed weights and opaque dependency behavior. Tokenizer files are resolved through configured hub identity, but their actual contents are not supplied. This prevents claims of immutable inference semantics or complete embedding lineage, not the known chunk/FTS/vector transformation chain.
- **Human control and operation uncertainty:** external document/config authorship and deployed per-content human involvement are unknown ([MEM-OBJ-chunks](#mem-obj-chunks), [MEM-OBJ-config](#mem-obj-config)). CLI initiation is not per-chunk approval. No observed read-back, compliance, evaluation result or capacity improvement is supplied; logs/test source do not fill that gap ([MEM-OBJ-semq-log](#mem-obj-semq-log)).
- No record is identified as a possible duplicate after comparison with the supplied runtime declarations. New operative objects and claims have distinct referents; no supersession is proposed. No additional unresolved integration question requires another source or a scope change.

## Limitations and checks

The frozen checkout HEAD was rechecked as `0820927160b1400990fa8cc057807c73bbf6d025`; source identity and run identity match the handed boundary and invocation. Inputs and complete invocation were read in the required batches/ranges; trailing continuation ranges were recovered. Inspection used the supplied worker rules, member types and record contract, without prior-analysis exposure. The initial attempted segmenter filename did not exist; file inventory located the implemented `crates/semquery-indexer/src/tokenizer.rs`, which was then read. This was a resolved lookup error, not an access gap.

The report establishes implementation wiring, not successful execution. External dependency extraction/tokenization/inference/storage internals, cached payload contents, user workspaces, custom components and actual human review remain uninspected. No model execution or tests were run. No conclusion of benefit, exercised learning, reflection or self-improvement is inferred from retention or retrieval alone. The strongest known qualifications are the lossy provenance/display chain, empty-content retention, raw-prefix sweep, partial-run persistence, baseline freshness limits and formatted-input tail truncation; supported positives coexist with them.

Deterministic validation: passed using the invocation's prepared `commonplace-validate` command with this report, artifact directory and role `memory`. This checks structure, relations and quote occurrence, not analytical truth or workflow acceptance.
