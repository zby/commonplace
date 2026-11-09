---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "semquery runtime baseline: CLI admission, persistent hybrid retrieval, local answer generation and forcing paths."
run-id: AAS-2026-11-09-semquery-b21559990932-01
reviewed-boundary: "0820927160b1400990fa8cc057807c73bbf6d025"
---

# semquery runtime report

## Runtime account

### Evidence and work boundary

Semquery is a document-indexing and returning question-answering system, not an enclosing autonomous-agent loop. The ordinary principal is the CLI user; the library caller can supply alternate components. Code owns progression from registration through indexing, recall, ranking, prompt construction and return. The chat model decides answer text, not the next tool or maintenance action. This account uses SRC-1 implementation at the frozen revision in [boundary](boundary.md). No execution trace or experiment was supplied; wiring, successful operation and benefit are separate conclusions throughout.

Additional inspected coverage under SRC-1 includes `crates/semquery-model/src/{embed,rerank,hub,gguf}.rs` (the individual paths are cited below), `crates/semquery-core/src/traits.rs`, `crates/semquery-indexer/src/reader_registry.rs`, the implementation of `crates/semquery-indexer/src/chunker.rs` through candidate construction, `crates/semquery-retrieve/src/fusion.rs`, and `crates/semquery-synth/src/citation.rs`. These supply implementation evidence, not observed-run evidence. External inference, hub and database dependency internals and actual model artifacts remain uninspected.

### Ordinary invocation

A user first initializes or opens a workspace, then runs `semq add <path> --name <name>`. `main` loads explicit configuration or creates/reads the platform-default configuration, opens logging, and dispatches. `run_add` canonicalizes and commits the collection registration before loading models. It calls `Engine::need_reindex`; config drift chooses all collections, otherwise only the named collection. It drains progress to a terminal event and reports counts. A failed index leaves registration present and asks the operator to retry. The old `index` CLI command only prints a migration hint and exits unsuccessfully; library index methods remain shipped. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`; [RT-RTE-index-admission](#rt-rte-index-admission).

The indexer enumerates registered-reader extensions, excludes hidden/default ignored names, extracts text, skips unchanged content hashes unless forced, constructs chunks and segmented lexical text, embeds new chunks and commits storage writes in groups. Path hashes identify documents; content hashes identify shared chunks. Later `search` and `ask` reopen the workspace and consume those retained results. Storage is local `semq.db`, with WAL, foreign keys and sqlite-vec integration. Collection names are registrations, not query-time access-control identities: search uses workspace storage, not a caller-specific grant filter. Evidence: SRC-1, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-indexer/src/reader_registry.rs`, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-retrieve/src/retriever.rs`.

For an ordinary `semq ask <query>`, `Engine::open` initializes storage without models, then `ask_stream` lazily loads embedding, reranking and chat models, constructing a retriever and synthesizer. The retriever concurrently runs segmented/sanitized FTS5 recall and raw-query embedding/vector recall. Reciprocal-rank fusion combines positions rather than raw score magnitudes; reranking scores a configured prefix. The synthesizer asks for five hits, emits them, and builds numbered context blocks containing file paths, byte ranges and chunk text. It passes that prompt to local chat inference. The CLI prints streamed token deltas in text mode, or the terminal `Answer` in JSON mode; citations are backfilled from valid numeric markers. Each call ends with an answer or error, not another autonomous task. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-retrieve/src/retriever.rs`, `crates/semquery-retrieve/src/fusion.rs`, `crates/semquery-synth/src/synthesizer.rs`; [RT-RTE-hybrid-search](#rt-rte-hybrid-search), [RT-RTE-answer-generation](#rt-rte-answer-generation).

### Forcing routes and guarantees

1. **Citation metadata is filtered; answer truth and answer text are not.** Both direct `Synthesizer::ask` and `ask_stream` parse valid markers but return raw model text. Invalid markers can remain in text and already-emitted token events. A valid marker refers to an offered hit, not proof that its passage supports the associated sentence. No-hit paths return empty answers without generation, although Engine loads its models before that branch. Owner/enforcement: synthesizer and citation parser. Strength: invariant for the filtered metadata list under the parser contract; best effort for grounding requested in natural language. Required external contract: LLM prompt compliance is not enforced. implementation conclusion status: wired. operation conclusion status: uninspected. Evidence and counterpath: [RT-CLM-citation-filter](#rt-clm-citation-filter), [RT-RTE-answer-generation](#rt-rte-answer-generation).

2. **Context selection does not guarantee all offered passages reach inference.** Both GGUF completion methods format system/user messages, tokenize and retain only the tail when over budget. This can remove the system message, leading context or citation blocks while retaining the query near the end. The marker set remains based on the pre-truncation hits. Owner/enforcement: GGUF adapter; strength: best effort for context fit, not an evidence-completeness invariant. Required external contract: backend handling of the configured context and formatted token sequence. implementation conclusion status: wired. operation conclusion status: uninspected. Direct custom `Llm` implementations need not use this truncation. See [RT-RTE-answer-generation](#rt-rte-answer-generation), [RT-CMP-gguf-llm](#rt-cmp-gguf-llm).

3. **Atomic transactions are not atomic whole indexing runs.** Owner/enforcement: SQLite BEGIN/COMMIT and rollback-on-drop, subject to SQLite and successful connection locking. Strength: protocol per transaction. `flush_batch` commits every five files; collection admission precedes indexing; deletion sweeps and metadata writes occur separately. Errors can therefore leave earlier committed work. The transaction object locks the shared connection per method, not for its entire lifetime; the inspected code does not establish isolation between interleaved callers sharing it. implementation conclusion status: wired. operation conclusion status: uninspected. Recovery is retry/reindex or explicit deletion, not restoration of a complete prior workspace snapshot. [RT-CLM-transaction-scope](#rt-clm-transaction-scope).

4. **Config-change reindexing is a route, not a global freshness barrier.** CLI add selects all collections on baseline drift, but search/ask do not first enforce `need_reindex`. Library callers can index one collection. Furthermore, `index_sources_stream` processes sources sequentially and each directory pass recalculates drift and updates the shared baseline. After the first successful source writes the new baseline, a later source can see matching configuration and skip unchanged files. That source-level progression prevents attributing guaranteed all-collection re-embedding to the CLI's initial all-source choice. A changed vector dimension can instead be rejected by storage initialization before indexing. Owner: CLI/Indexer baseline checks and storage schema check; strength: best effort for workspace freshness, protocol for schema rejection. implementation conclusion status: wired. operation conclusion status: uninspected. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-storage/src/sqlite.rs`; [RT-RTE-index-admission](#rt-rte-index-admission).

### Alternate clients, capability and isolation

`Engine::new` accepts caller-provided storage, embedder, chunker, segmenter, readers, optional reranker and LLM. These are real trait-object extension points, not an authorization gate. Its prebuilt branches reuse components without the ordinary lazy model loaders. An optional absent reranker preserves fusion order; a populated but uninitialized reranker cell errors rather than falling back. Public lower-level `Llm::complete`, retriever and synthesizer calls are also alternatives to the facade; the default trait streaming implementation returns one complete string through the callback. Consequently, claims about local inference, hub loading, context trimming or ranking are scoped to their concrete adapters. Evidence: SRC-1, `crates/semquery/src/engine.rs`, `crates/semquery-core/src/traits.rs`, `crates/semquery-retrieve/src/retriever.rs`.

The inspected shipped inference path invokes no model-selected shell or tool executor. The process itself reads user-selected files, writes workspace/cache/log/config state and can download model artifacts. Its capability surface is therefore broader than the model's answer channel. There is no separate per-operation approval shown on these inspected paths; starting add/delete is the user's command, not review of each admitted chunk. Filesystem permissions and backend behavior are external contracts, not a demonstrated sandbox. A deployment's actual grants and isolation envelope are not supplied. Library callbacks and injected trait implementations run in the host process and can have effects beyond these defaults; their deployments are not frozen here. These are scoped implementation findings, not a universal claim about all hosts. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-model/src/hub.rs`, `crates/semquery-model/src/gguf.rs`, `crates/semquery-core/src/traits.rs`.

Streaming uses bounded channels and spawned tasks rather than durable jobs. Stage events and timings provide source-wired observability, not performance evidence. Receiver failure is checked at forwarding/stage boundaries, but already-running inference is not interrupted by the token callback: its send errors are ignored. On multithreaded Tokio the callback uses blocking sends; on current-thread Tokio it uses best-effort `try_send`. Thus documentation about cancellation/every-token delivery is not an unconditional runtime invariant. No resume checkpoint for an answer is established by these paths. Model and chunk state reside in shared cells/storage; per-generation context is freshly allocated, not a retained conversation. Evidence: SRC-1, `crates/semquery/src/engine.rs`, `crates/semquery-retrieve/src/retriever.rs`, `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-model/src/gguf.rs`.

## Shared records

### Components

#### RT-CMP-fast-embed
Label: FastEmbedEmbedder

SRC-1, `crates/semquery-model/src/embed.rs`: distributed-parametric embedding model accessed through `Mutex<TextEmbedding>`; numerical weights reside in model/cache artifacts and inference memory, while returned dense vectors enter SQLite through the index route. The inspected adapter performs inference, not parameter updates. Exact deployed weights are not pinned by the report or default configuration. The adapter maps `spec.repo_id` to a FastEmbed enum and supplies the cache directory, but does not pass the configured revision/filename into `TextInitOptions`; hub resolution metadata therefore does not establish exact embedding artifact identity. Mutable hub/default revisions can resolve differently, and dependency-internal artifact selection remains uninspected. Injected embedders have caller-defined behavior.

> let options = TextInitOptions::new(model).with_cache_dir(hub.cache_dir().to_path_buf());
> let inner = TextEmbedding::try_new(options).map_err(|e| ModelError::ModelInitFailed(e.to_string()))?;
> --- `crates/semquery-model/src/embed.rs`

#### RT-CMP-fast-reranker
Label: FastEmbedReranker

SRC-1, `crates/semquery-model/src/rerank.rs`: distributed-parametric cross-encoder accessed through `Mutex<TextRerank>`; cached model artifacts/in-memory inference state produce query/chunk scores, not a parameter update in inspected operation. Exact artifact version is unresolved: defaults use symbolic revisions, and this adapter maps repo ID to an enum and cache directory rather than forwarding configured filename/revision into inference options. The mutable resolution surface may select another artifact on a later initialization; dependency internals and injected rerankers remain uninspected.

> let options = RerankInitOptions::new(model).with_cache_dir(hub.cache_dir().to_path_buf());
> let inner = TextRerank::try_new(options).map_err(|e| ModelError::ModelInitFailed(e.to_string()))?;
> --- `crates/semquery-model/src/rerank.rs:19-20`

#### RT-CMP-gguf-llm
Label: GgufLlm

SRC-1, `crates/semquery-model/src/gguf.rs`, `crates/semquery-model/src/hub.rs`, `crates/semquery/src/config.rs`: distributed-parametric local chat model, GGUF artifact in hub cache loaded as `LlamaModel`; generation allocates a new context and samples tokens. No weight-changing operation appears in these completion methods. Configurable repo/revision/filename select the file; defaults use `main`, `to_spec` supplies no checksum, and `resolve` uses hub `get` without an explicit checksum check. A default symbolic revision is not an immutable model pin and can resolve to another artifact on later resolution; the already-loaded model is shared through a OnceCell. The frozen repository commit does not freeze downloaded weights. Provider internals and caller-injected LLMs are outside this fixity finding.

> let repo = Repo::with_revision(spec.repo_id.clone(), RepoType::Model, spec.revision.clone());
> --- `crates/semquery-model/src/hub.rs:49-49`

> LlamaModel::load_from_file(&backend, &path, &model_params).map_err(|e| LlmError::ModelLoad(e.to_string()))?;
> --- `crates/semquery-model/src/gguf.rs:47-47`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-index-admission
Label: Collection admission and incremental indexing

Endpoints: CLI path/name or library collection registration to persisted collection/document/chunk/vector/FTS state. The user/caller proposes the collection and chooses invocation; code canonicalizes, registers, enumerates, extracts, hashes, chunks, embeds, stores and removes missing entries. Directory scanning uses extension dispatch, ignores hidden/default ignored names and silently skips traversal errors. Document IDs hash paths; chunk IDs hash text. The embedding model supplies representations, not a content-admission judgment. No per-chunk human veto or answer oracle is invoked. Operating mode: open document ingestion, triggered explicitly by add or library index calls, with drift/hash rules for maintenance rather than an experimental improvement curriculum. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-indexer/src/reader_registry.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Progress events and terminal file/chunk/skip/removal counts, or errors; registration can outlive a failed index.
- Later read-back: Committed chunks, lexical text, vectors, paths and baseline metadata feed later search/ask or indexing calls after workspace reopen.
- Delegated visibility: inapplicable — no delegated agent; local embedding inference receives selected new chunk texts.
- Selection predicate: Registered source path and reader eligibility; unchanged document hash skips unless drift forces; shared chunk hashes suppress duplicate embedding unless reembedding.
- Invalidation or expiry: Explicit delete, directory deleted-file sweep, changed content or model/chunk config; no timed expiry in the inspected route.
- Activation or effect: Software commits retrieval material for subsequent consumers; actual later use or better answers is not demonstrated.
- Evidence limits: Source-only; extraction fidelity, backend success and whole-workspace reembedding correctness are not established. Search does not impose a freshness check, and per-source baseline updates narrow the all-collection reindex claim.

Admission/recovery: computational transformations automatically admit extracted content and derived representations after a user/caller chooses a source. No model fact-check or human content approval is a condition. Reader/chunker configuration guides selection and structure; persisted output is document material and numerical/lexical retrieval representations, not a revised system method. Transaction drop attempts rollback of uncommitted work; earlier batch commits survive. Explicit deletion removes registrations and solely owned indexed material while preserving shared chunks; source files are untouched by Engine deletion. `del_document` requires canonicalization, so a missing filesystem path is not handled by that direct deletion route; the scan sweep is a different removal path (SRC-1, `crates/semquery/src/engine.rs`, `crates/semquery-indexer/src/indexer.rs`).

> let doc_id = sha256_hex(&path_str);
> --- `crates/semquery-indexer/src/indexer.rs`

> if !force_reembed && existing.content_hash == content_hash {
>         return Ok(None);
>       }
> --- `crates/semquery-indexer/src/indexer.rs`

> if tx_count >= TX_BATCH_SIZE {
>         tx.commit()?;
>         tx = self.storage.begin_tx()?;
>         tx_count = 0;
>       }
> --- `crates/semquery-indexer/src/indexer.rs`

The config-drift forcing countercase follows these two operations in the same per-source implementation, while `index_sources_stream` invokes that method for successive paths:

> let force_reindex = self.need_reindex()?;
> --- `crates/semquery-indexer/src/indexer.rs:324-345`

> self.update_index_meta()?;
> --- `crates/semquery-indexer/src/indexer.rs:400-420`

#### RT-RTE-hybrid-search
Label: Hybrid recall and candidate ranking

Endpoints: query/top-k to hit list with paths, chunks, score explanations and timings. Owner: Retriever code; embedder and optional cross-encoder supply numerical judgments. Context: raw query reaches embedding/reranking; segmented sanitized query reaches FTS5. BM25 runs on a blocking task concurrently with vector recall. Either recall error terminates rather than degrading to the successful channel. RRF fuses ranks, then code either preserves fused order or reranks its configured prefix, fetches paths and takes top-k. This is candidate comparison: models score, code decides order, caller controls limits/configuration, and no human per-hit approval or reference-answer oracle is used. Operating mode: open query, no bounded curriculum. SRC-1, `crates/semquery-retrieve/src/retriever.rs`, `crates/semquery-retrieve/src/fusion.rs`; model identities in [RT-CMP-fast-embed](#rt-cmp-fast-embed) and [RT-CMP-fast-reranker](#rt-cmp-fast-reranker).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Completed hits/statistics or propagated stage error; empty/whitespace query returns an empty result inside Retriever.
- Later read-back: Reads previously indexed workspace chunks/vectors/FTS data; this route does not itself retain answer or search outcomes for a future invocation.
- Delegated visibility: inapplicable — no delegated worker; scoring components see query and selected document text.
- Selection predicate: Recall limits, rank fusion, optional rerank_top_n, final top_k and existing-chunk lookup; missing chunk entries are omitted during assembly.
- Invalidation or expiry: Underlying index maintenance changes subsequent results; per-query ranking state ends with the call.
- Activation or effect: Selected hits become caller output or the ask prompt; relevance and consumer reliance remain unobserved.
- Evidence limits: Dependency scoring and actual retrieval quality unobserved; Engine still loads models before the Retriever empty-query fast path. Injected no-reranker configuration is reachable through EngineComponents.

> let (bm25_res, vec_res) = tokio::join!(self.bm25_recall(query, tx), self.vector_recall(query, tx));
> --- `crates/semquery-retrieve/src/retriever.rs`

> None => {
>         let ids: Vec<String> = fused.iter().take(top_k).map(|(id, _)| id.clone()).collect();
>         let chunks = self.storage.get_chunks(&ids)?;
>         let map = chunks.into_iter().map(|c| (c.id.clone(), c)).collect();
>         Ok((map, HashMap::new(), fused))
>       }
> --- `crates/semquery-retrieve/src/retriever.rs`

#### RT-RTE-answer-generation
Label: Grounded prompt and answer generation

Endpoints: query to five retrieved hits, formatted prompt, sampled answer and filtered citation metadata. Code owns progression and termination; the chat model generates natural language. The caller may choose generation config/system prompt, but no per-answer approval or external expected-answer oracle is called. Operating mode: open question answering, not a candidate-improvement loop. Selection is [RT-RTE-hybrid-search](#rt-rte-hybrid-search); concrete chat component is [RT-CMP-gguf-llm](#rt-cmp-gguf-llm). SRC-1, `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-synth/src/prompt.rs`, `crates/semquery-synth/src/citation.rs`, `crates/semquery-model/src/gguf.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Empty answer for no hits; otherwise tokens and terminal Answer with raw text and validated-marker source metadata, or inference/retrieval error.
- Later read-back: Retrieved document material comes from persisted index; this inspected answer route does not save its output as future knowledge or conversation memory.
- Delegated visibility: inapplicable — a model completion is not a separate task-owning worker; the LLM receives formatted selected context, subject to token truncation.
- Selection predicate: Fixed five-hit retrieval; build_ask_prompt supplies all returned hit texts and query; GGUF keeps a tail if formatted input exceeds n_ctx minus max_tokens, floored at one.
- Invalidation or expiry: Per-call inference context is recreated; no history reload or summary store appears in either GGUF completion method. Index changes affect later retrieval.
- Activation or effect: Delivered context can shape generated text, but source wiring establishes neither compliance, factual grounding nor improved capacity.
- Evidence limits: No supplied runs; raw tokens precede citation parsing. A marker can validate against an offered hit even if its passage was removed by backend truncation. Injected Llm implementations define their own context policies.

Working-context control: code first keeps out all nonselected corpus chunks, then reserves generation room by discarding the beginning of the fully formatted token input. It preferentially retains the suffix, not a semantic summary or specifically trusted instructions. Both `complete` and `complete_stream` do this; over-budget inputs are reachable because queries and chunk texts have no total prompt-token admission check in the synthesizer. The surviving suffix remains in a fresh per-call context; removed passages remain reachable only through another retrieval invocation, with no within-generation reload route here. This resembles a per-call frame that returns text; it is not a subagent context and no pointers preserve removed tokens for the model.

> prompt.push_str("Given the context information and not prior knowledge, answer the query.\n");
> prompt.push_str("Cite sources using [1], [2], etc.\n");
> --- `crates/semquery-synth/src/prompt.rs`

> let max_prompt_tokens = (self.config.n_ctx as usize).saturating_sub(self.config.max_tokens).max(1);
> --- `crates/semquery-model/src/gguf.rs:160-214`

> &tokens[tokens.len() - max_prompt_tokens..]
> --- `crates/semquery-model/src/gguf.rs:160-214`

Streaming reliability qualification:

> } else {
>         let _ = tx.try_send(event);
>       }
> --- `crates/semquery-synth/src/synthesizer.rs`

The callback ignores send failure; generation still returns the full raw string if inference succeeds. CLI JSON uses the terminal Answer when present, with buffered-text fallback if no terminal event arrives without an error; text mode prints deltas and sources. `Engine::ask` instead errors when its stream ends without `AnswerComplete` (SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`).

#### RT-RTE-config-admission
Label: Configuration and component admission

Endpoints: operator-edited TOML or caller-supplied EngineComponents to model loading, chunk/retrieval parameters and system-message behavior. The file reader parses config; numeric temperature/top-p conversion can reject invalid strings. The CLI writes defaults only when config is missing; subsequent replacement is external authorship, not model-generated self-modification. Library injection admits executable trait implementations directly. These are different proposal surfaces sharing caller-controlled admission rather than a runtime evaluator. Source: SRC-1, `crates/semquery/src/config.rs`, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-core/src/traits.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed configuration/constructed Engine, or load/parse/model initialization errors on the relevant path.
- Later read-back: CLI reloads saved config on subsequent launches; shared model cells reuse loaded objects during an Engine lifetime. Injected implementations persist only as the caller arranges.
- Delegated visibility: inapplicable — no delegated agent; adapters consume selected config fields.
- Selection predicate: Explicit --config or default config directory; supplied EngineComponents take prebuilt branches instead of ordinary lazy loading.
- Invalidation or expiry: Editing/replacing file affects subsequent opens, not an already-loaded OnceCell; caller reconstructs Engine for changed components.
- Activation or effect: Config system_prompt enters GGUF system messages, generation limits enter inference, and model repo selections enter adapters. Artifact identity limits differ for FastEmbed and GGUF as recorded above.
- Evidence limits: Human authorship of a particular deployed config is unknown. No supplied trace shows any replacement, approval or behavior change.

Admission decisions: external author/caller proposes and can withhold or replace configuration/components; code parses and can reject unsupported model IDs, malformed config or failed loading. No learned proposal, comparison oracle or production-optimization trigger is invoked here. Operating mode: operator/caller configuration, not a bounded experiment. Rollback means restoring earlier external config/components and reopening; no managed configuration history or automatic deployment rollback is established by these paths. The persisted guidance is literal config (including natural-language system prompt), not criticisms of prior operation.

> pub system_prompt: String,
> --- `crates/semquery/src/config.rs`

> LlamaChatMessage::new("system".into(), self.config.system_prompt.clone())
> --- `crates/semquery-model/src/gguf.rs:160-214`

### Claims

#### RT-CLM-citation-filter
Label: Citation filtering scope

Claimed operation: the synthesizer documents that invalid markers are silently dropped. Inspected implementation supports dropping them from the citation vector, not scrubbing raw answer text. Owner: parse_citations and Synthesizer. Covered routes: direct and streamed synthesis; Engine drives streaming. Alternate direct/custom LLM calls do not inherit citation validation. Strength: invariant for marker-set membership of returned citation metadata, not a truth guarantee. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1, `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-synth/src/citation.rs`.

> if !valid.contains(marker) || !seen.insert(marker.to_string()) {
>       continue;
>     }
> --- `crates/semquery-synth/src/citation.rs`

> Ok(Answer { text: raw, citations })
> --- `crates/semquery-synth/src/synthesizer.rs`

The prompt's grounding instruction is a behavioral request. Metadata membership proves neither that a citation supports the statement nor that the model saw the full passage after truncation.

#### RT-CLM-transaction-scope
Label: Transactional write scope

Claimed operation: StorageTx documentation says reindex failure cannot leave the store half-written. Concrete SQLite implements BEGIN, COMMIT and rollback-on-drop, but indexer commits groups and metadata separately. Scope is a transaction, not a complete invocation or workspace migration. Required contract: SQLite transactions, successful connection access, and caller sequencing. Concurrent same-connection transaction ownership is not established by per-method mutexes. Strength: protocol. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1, `crates/semquery-core/src/traits.rs`, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-indexer/src/indexer.rs`.

> /// Atomic write transaction over the indexed tables. All mutations flow
> /// through this trait so a re-index / re-embed failure cannot leave the
> /// store half-written.
> --- `crates/semquery-core/src/traits.rs`

> if !self.committed
>       && let Ok(conn) = self.conn.lock()
>     {
>       let _ = conn.execute_batch("ROLLBACK");
>     }
> --- `crates/semquery-storage/src/sqlite.rs`

Earlier committed batches and collection registration are counterexamples to whole-run rollback, not evidence that a completed SQLite transaction itself lacks atomicity.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-influence
Label: Retrieved text and configured prompt influence

Consumer: concrete GGUF chat inference. Channel: natural-language configured system message and user message containing query plus selected retained chunks. Force: requested answer grounding and source citation through model interpretation, not executable enforcement or a hard truth constraint. Horizon: one generation; saved config and corpus content can recur across launches through [RT-RTE-config-admission](#rt-rte-config-admission) and [RT-RTE-hybrid-search](#rt-rte-hybrid-search). Instruction/data separation is textual inside a user prompt; no runtime content sanitizer or per-passage approval appears in this construction. Actual compliance, malicious-instruction effects and answer benefit are unobserved. SRC-1, `crates/semquery-synth/src/prompt.rs`, `crates/semquery-model/src/gguf.rs`.

> LlamaChatMessage::new("user".into(), prompt.to_string()).map_err(|e| LlmError::InferenceFailed(e.to_string()))?,
> --- `crates/semquery-model/src/gguf.rs:160-214`

The retrieval and truncation routes determine what arrives; membership in saved storage alone does not establish activation.

## Annotations

none
