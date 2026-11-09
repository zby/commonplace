---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "sqz memory report: persistent originals, heuristic context residency, explicit recovery, and partially connected session continuity."
run-id: AAS-2026-11-09-sqz-154fb86209ba-01
source-identity: "https://github.com/ojuschugh1/sqz"
reviewed-boundary: "495c078d8f4c94d060ecfbb4d919286670b87898"
---

# sqz memory report

## Boundary and evidence

sqz retains context representations for external agents. This report uses the whole-system boundary in [boundary](boundary.md#boundary-and-evidence), SRC-1 at `495c078d8f4c94d060ecfbb4d919286670b87898`. Native CLI/MCP retention, recovery, maintenance, installed guidance, session continuity, exposed library alternatives and browser/IDE context controls are included. External host window management, provider caches, models, downloaded binaries and live browser DOM behavior are not established. Excluding those implementations prevents claims about actual model visibility, reference comprehension, deployment parity or task quality.

Evidence is implementation and doctrine/design, not an observed run. The runtime input is a provisional source account, not execution evidence. Direct reads here added storage schema and methods, continuity, correction replay, CTX parsing, pin management, cache transformations, dependency pre-caching, hooks, auxiliary indexers and context-control APIs. The checkout HEAD was rechecked against the frozen revision. No target code or tests were executed.

### Coverage inventory

“Supplied” means supported by runtime records; “direct” means source text inspected for this member. All paths below are SRC-1. Inclusion does not imply complete review of every algorithm.

| Entry point or operation | Source path and inspection | Covering record or unresolved limit |
|---|---|---|
| Native compression, verification and safe fallback | `sqz_engine/src/engine.rs`, `sqz_engine/src/pipeline.rs`; supplied, facade additions direct | [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress), [RT-CMP-compression-pipeline](runtime.md#rt-cmp-compression-pipeline); verification is not a semantic admission proof |
| CLI stdin formatter, direct compression, hooks and post-hook | `sqz/src/main.rs`, `sqz/src/cli_proxy.rs`; supplied plus direct dispatch/maintenance/dependency reads | [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress), [RT-RTE-integration-install](runtime.md#rt-rte-integration-install), [MEM-OBJ-known-files](#mem-obj-known-files) |
| MCP registered compress/passthrough/expand/recall/read/grep/list | `sqz-mcp/src/lib.rs`; direct dispatcher and recall, other bodies supplied | [RT-RTE-file-read](runtime.md#rt-rte-file-read), [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), [MEM-RTE-recall-search](#mem-rte-recall-search); passthrough does not recover omitted material |
| Cache exact/slice/delta, original recovery | `sqz_engine/src/cache_manager.rs`, `sqz_engine/src/session_store.rs`; direct plus supplied slice analysis | [MEM-OBJ-cache-original](#mem-obj-cache-original), [MEM-OBJ-cache-compressed](#mem-obj-cache-compressed), annotations on cache route |
| Predictive dependency admission and path annotation | `sqz/src/cli_proxy.rs`; direct | [MEM-RTE-dependency-precache](#mem-rte-dependency-precache); cache admission can precede model delivery |
| Pin add/set/unset/list/clear; session-turn pins | `sqz/src/main.rs`, `sqz_engine/src/pin_manager.rs`; direct | [MEM-RTE-cache-maintenance](#mem-rte-cache-maintenance), [MEM-OBJ-session](#mem-obj-session); these are different pin substrates |
| PreCompact, compact, reset, low-level invalidation/LRU | `sqz/src/main.rs`, `sqz_engine/src/cache_manager.rs`, `sqz_engine/src/context_evictor.rs`, `sqz_engine/src/session_store.rs`; direct | [MEM-RTE-cache-maintenance](#mem-rte-cache-maintenance); compact is not host eviction and LRU is an exposed capability, not demonstrated automatic cleanup |
| Import/export/search/resume; SessionStart integration | `sqz/src/main.rs`, `sqz_engine/src/ctx_format.rs`, `sqz_engine/src/session_continuity.rs`, `sqz_engine/src/tool_hooks.rs`; direct | [MEM-RTE-session-continuity](#mem-rte-session-continuity), [MEM-OBJ-snapshot](#mem-obj-snapshot); initial session acquisition remains caller supplied |
| Generic hook actions and correction replay | `sqz_engine/src/hook_manager.rs`, `sqz_engine/src/correction_log.rs`; direct | [MEM-OBJ-session](#mem-obj-session); returning BuildSnapshot/RestoreSnapshot action values does not implement persistence or restoration |
| Dashboard synthetic session and statistics/regret | `sqz/src/main.rs`, `sqz_engine/src/session_store.rs`, `sqz_engine/src/regret_tracker.rs`; direct | [MEM-OBJ-operation-metadata](#mem-obj-operation-metadata), [MEM-OBJ-session](#mem-obj-session); synthetic dashboard rows are not full sessions |
| MCP proxy retained lazy descriptions and transformed results | `sqz-mcp/src/proxy.rs`; supplied | [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy); process-local docs and persistent content cache have different horizons |
| HTTP request/history shortening | `sqz_engine/src/api_proxy.rs`, `sqz/src/main.rs`; supplied | [RT-RTE-request-transform](runtime.md#rt-rte-request-transform); omitted middle has no established retained reload route |
| WASM memoization/session import/export; browser proposal/UI/stats | `sqz-wasm/src/lib.rs`; direct; `extension/content/common.js`, `extension/background.js`, `extension-firefox/background.js`; supplied plus storage searches | [RT-CMP-wasm-engine](runtime.md#rt-cmp-wasm-engine), [RT-RTE-browser-compress](runtime.md#rt-rte-browser-compress), annotations; no source-to-binary equivalence |
| IDE caller/fallback compression | `vscode-extension/src/sqzBridge.ts`, `jetbrains-plugin/src/main/kotlin/com/sqz/SqzBridge.kt`; supplied | Runtime account's Other shipped consumers; no separate retained IDE original/reload path established |
| URL index, advanced search, tee output | `sqz_engine/src/url_indexer.rs`, `sqz_engine/src/advanced_search.rs`, `sqz_engine/src/tee_mode.rs`, `sqz/src/main.rs`; direct | [MEM-CMP-library-stores](#mem-cmp-library-stores); APIs establish storage/search capabilities, not an unspecified agent consumer |
| File read modes, prompt-boundary detection, sink preservation, LITM positioning, repeat throttling | `sqz_engine/src/file_reader.rs`, `sqz_engine/src/prompt_cache.rs`, `sqz_engine/src/kv_cache_optimizer.rs`, `sqz_engine/src/engine.rs`, `sqz_engine/src/progressive_throttle.rs`; direct interfaces and selected bodies | [MEM-CMP-context-controls](#mem-cmp-context-controls); exact FileReader task/entropy algorithms and all integration callers uninspected, preventing a complete selection/activation claim |
| Subprocess stdout filtering | `sqz_engine/src/sandbox_executor.rs`; direct execute/filter/result bodies | [MEM-CMP-context-controls](#mem-cmp-context-controls); transient FTS is destroyed after filtering, not a later retrieval service |
| Quality evaluator | `sqz/tests/quality_bench.rs`; direct definition and harness | [MEM-CLM-evaluation-scope](#mem-clm-evaluation-scope); test design, not an observed test result or feedback-driven policy revision |
| Other shipped transform modules, site adapters, integration variants, installers and benchmark reports | `sqz_engine/src/lib.rs` inventory; boundary tree inventory and runtime coverage | Not all bodies inspected. This prevents exhaustive transform semantics, host parity and measured efficacy claims. It does not hide the named alternative stores/consumers above. |

## Core ideas

1. **Retention and context residence are separate.** Native cache originals survive in SQLite, but a reference is only a short text token. Timestamp freshness and pin flags estimate whether the consumer already has the body. They do not inspect its window. Dependency pre-caching is a concrete counterexample to “cached means previously shown” ([RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), [MEM-RTE-dependency-precache](#mem-rte-dependency-precache)).
2. **Recovery is a second explicit request.** Recall selects snippets by query; expand selects retained content by hash prefix and optional range. Neither causes model attention to dereference a pointer. The host/agent must request recovery and interpret the resulting text ([MEM-RTE-recall-search](#mem-rte-recall-search), [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)).
3. **Several different things are called continuity or memory.** Full session JSON, compact event snapshots, printed guides, raw originals, compressed text, access metadata, process-local WASM memoization and statistics are not interchangeable. Initial session facts and corrections can be imported; ordinary cache writes do not imply creation of a complete session trace ([MEM-OBJ-session](#mem-obj-session), [MEM-OBJ-snapshot](#mem-obj-snapshot), [MEM-OBJ-operation-metadata](#mem-obj-operation-metadata)).
4. **Most curation is deterministic representation selection.** Cache transformations, query ranking, clipping, priority dropping and rule generation do not establish truth, formulated criticism, learning benefit or reliable model compliance. Source provenance is mostly caller/input identity and access metadata, not a trust assessment. Installed text requests behavior through natural language; freshness flags instead govern code directly ([RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance), [MEM-BAP-reference-policy](#mem-bap-reference-policy)).

## Shared records

### Components

#### MEM-CMP-library-stores
Label: Alternative library storage capabilities

These source-native APIs are distinct from native cache/session storage in [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), not duplicate deployed retrieval routes. SRC-1, `sqz_engine/src/url_indexer.rs`, stores derived Markdown and heading/body chunks in SQLite plus FTS, with URL/time/TTL metadata. A caller supplies a ContentFetcher, URL and force flag; software accepts successful fetch/transformation, deletes the old URL data and inserts the replacement. No per-content human approval is imposed, and caller humanity is unresolved. TTL controls whether fetch is repeated; the search method returns ranked stored matching sections without a TTL check in its inspected body. The code can provide later section retrieval, but no inspected CLI/MCP dispatcher wires this API to an agent.

> let markdown = html_to_markdown(&html);
>         let chunks = chunk_by_headings(&markdown);
> --- `sqz_engine/src/url_indexer.rs`

`AdvancedSearch` stores caller-authored text with symbolic IDs in an in-memory SQLite database; index upserts replace content. Its own search combines BM25/trigram, fusion, fuzzy fallback and proximity/snippet operations. It is not the persistent recall index. Text has natural-language authority only if a caller delivers and a consumer interprets it; IDs/indexes are symbolic. No unspecified external caller is counted as a route.

> let db = Connection::open_in_memory()?;
> --- `sqz_engine/src/advanced_search.rs:152-158`

`TeeManager` retains uncompressed caller-supplied output strings in timestamp/command-named `.txt` files with JSON sidecars, normally under `~/.sqz/tee/`. Always/failures/never controls admission; failures tests the supplied exit code, not content truth. `sqz tee list/get` is an actual later CLI file consumer, while automatic production by ordinary compress calls was not found in the inspected main/CLI proxy/MCP/facade searches. Thus saving is a library capability and retrieval is wired for existing files; an automatic capture loop remains unestablished. `get` returns text by ID. Same-second naming and filesystem behavior delimit retention; no versioned rollback is established. Raw output content and sidecar access metadata are separate operative parts, not derived lessons.

> let should_save = match self.mode {
>             TeeMode::Always => true,
>             TeeMode::Failures => exit_code != 0,
>             TeeMode::Never => false,
>         };
> --- `sqz_engine/src/tee_mode.rs`

#### MEM-CMP-context-controls
Label: Auxiliary text context controls

These are symbolic library functions and in-memory selectors, distinct from the supplied [RT-CMP-compression-pipeline](runtime.md#rt-cmp-compression-pipeline) and deployed MCP/file routes. SRC-1, `sqz_engine/src/file_reader.rs`, `sqz_engine/src/prompt_cache.rs`, `sqz_engine/src/kv_cache_optimizer.rs`, `sqz_engine/src/progressive_throttle.rs`, `sqz_engine/src/engine.rs`, and `sqz_engine/src/sandbox_executor.rs`, expose caller-directed read modes, boundary heuristics, protected prefixes, section ordering, call counters and intent-filtered subprocess output. Their text inputs/outputs are natural language or source syntax at the eventual consumer; counters, modes and indices are symbolic local state. The Read-back section retains per-surface trigger, selector, output and inspection limits. No distributed learned weights or unspecified downstream consumer is established.

> let should_filter = result.stdout.len() > self.filter_threshold
>             && intent.map_or(false, |i| !i.trim().is_empty());
> --- `sqz_engine/src/sandbox_executor.rs`

### Operative objects

#### MEM-OBJ-operation-metadata
Label: Statistics and regret parts

SRC-1, `sqz_engine/src/session_store.rs`, retains symbolic compression counts/stages/project attribution in compression_log and rerun/expand signals in regret_log. These are raw operating measurements, not compressed knowledge or a durable adaptive policy. CLI stats/dashboard consumers report them. Separate RegretTracker holds caller-supplied events and derived per-content numerical recommendations in in-memory maps/vectors, using fixed arithmetic rules rather than learned distributed parameters. Its own source distinguishes that capability from shipped SQLite signals. Closest supplied [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress) describes statistics writes, not this operative object; no duplicate object exists.

> NOTE: this in-memory tracker is not wired into the hook path (each hook
> //! invocation is a fresh process, so nothing here persists). The shipped
> //! regret signals live in the session store's `regret_log` table
> --- `sqz_engine/src/regret_tracker.rs`

Write admission is software logging after relevant operations; initiating a command is not approval of each metric. Recommendation updates admit caller events without a human veto; reset clears in-memory profiles/events. No inspected later production compressor consumes those recommendations, so a trace-fed automatic policy-learning chain is unestablished. Statistics reports can inform a human but do not prove such intervention occurred. Regret signals are proxies, not evidence locating a particular false retained claim. Their retention/removal scope differs from cache originals and ordinary CLI stats reset.

#### MEM-OBJ-cache-original
Label: Native cache original bytes

SRC-1, `sqz_engine/src/session_store.rs`, stores nullable `cache_entries.original` BLOBs under a symbolic content hash. The payload can be natural language, source code or opaque bytes; raw storage alone gives no linguistic or symbolic interpretation. The actual recovery consumer receives original bytes in CLI stdout, or text through MCP presentation. The content's origin is the admitted input at that caller, not necessarily a whole original file or a conversation trace. Current wrapper writes retain originals; old/no-original callers may leave NULL. Conflict updates preserve an existing original against NULL. This is the raw part of the cache capability already described by [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), not a duplicate route. No supplied operative-object counterpart exists.

> original = COALESCE(excluded.original, original)
> --- `sqz_engine/src/session_store.rs`

Expansion has data-delivery authority, not execution or instruction priority. Deleting storage removes recovery capability; expiry of ref freshness alone does not delete originals. Knowledge, instructions and untrusted tool output share this substrate; no source-truth promotion is implied.

#### MEM-OBJ-cache-compressed
Label: Native cached compressed representation

Distinct from [MEM-OBJ-cache-original](#mem-obj-cache-original), `CompressedContent` is serialized JSON in `cache_entries.data` (SRC-1, `sqz_engine/src/session_store.rs`). It contains derived text plus symbolic counts, stages, provenance and optional verifier results. The text is natural language/code/encoded syntax depending on input and transform; decoding and interpretation are consumption-specific. CacheManager's similarity index is process-local computed MinHash data over compressed text, not model weights. The JSON is durable; the similarity index is not the durable payload. Closest supplied record is [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery); no supplied object duplicates this part.

> let data = serde_json::to_string(compressed)?;
> --- `sqz_engine/src/session_store.rs`

Later consumers use its text for near-duplicate baselines and compressed-only expansion. `try_delta_against` compares a new input with `cached.data`, not with retained raw original bytes. The candidate scan tries LSH candidates and recent LRU entries; unlike exact/slice reference selection, the inspected delta baseline method has no `is_ref_fresh` call. Therefore the exact-ref freshness story must not be generalized to all delta baselines (SRC-1, `sqz_engine/src/cache_manager.rs`).

> self.delta_encoder.encode(&cached.data, new_content, hash_prefix)
> --- `sqz_engine/src/cache_manager.rs`

Counts/stages/verification are transformation metadata, not reasons for individual retained claims. The representation can shape later context without retaining a criticism or rationale for each deletion.

#### MEM-OBJ-known-files
Label: Known files and residency metadata

SRC-1, `sqz_engine/src/session_store.rs`, retains path/timestamp rows in `known_files`; cache access timestamps, pinned bits and `metadata.last_compaction_at` are separate symbolic access-policy data. They are not the file's content or evidence the model still sees it. Code consumers use them for annotation and freshness. Compared with [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress) and [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), this declares metadata, not another route.

> let note = format!("{} [in context]", marker);
> --- `sqz/src/cli_proxy.rs`

The proxy tracks selected file-reading command labels and also adds pre-cached dependencies. Later error messages can be annotated `[in context]` using persistent paths with no host-window inquiry. The inspected PreCompact handler invalidates refs, not known-file rows. Pins bypass freshness checks, not by re-injecting content but by code trusting the stored flag. Physical persistence exceeds the consumer knowledge warranted by the label.

#### MEM-OBJ-session
Label: Persisted SessionState

Source-native `Session`/`SessionState` in SRC-1, `sqz_engine/src/types.rs`, is a mixed object: natural-language turns, key/value facts and edit text; symbolic roles, source-turn indices, times, paths, pins, budgets and tool-cost records. `save_session` serializes it as JSON bytes in SQLite `sessions.data`, alongside searchable summaries and metadata. It is distinct from cache originals/compressed content. Closest supplied account is the resume paragraph and [RT-RTE-integration-install](runtime.md#rt-rte-integration-install); no supplied session object exists.

> pub conversation: Vec<Turn>,
>     pub corrections: EditHistory,
>     pub pins: Vec<PinnedSegment>,
>     pub learnings: Vec<KvFact>,
>     pub compressed_summary: String,
> --- `sqz_engine/src/types.rs`

Authoring is caller supplied through save/import; how an initial non-imported full session is assembled remains unresolved for ordinary shipped compression. Starting a compression is not per-content approval or a fact-extraction trace. CTX imports can replace an existing same-ID session through upsert. `CorrectionLog::append` preserves entries in memory; `replay_into` delivers correction text to a simple Vec-backed ContextWindow, not directly to a live model. Session pin/unpin APIs edit turn flags and PinEntry records and save the full session, with an index-range error on invalid pin requests. These are not cache pin flags.

> context.entries.push(entry.correction.clone());
> --- `sqz_engine/src/correction_log.rs`

Edit records can retain original, correction and context; resume emits original → correction, omitting the edit context. Facts retain `source_turn`, but the guide emits key/value only. Retention of reasons is possible inside caller text, not guaranteed by these fields, and guide consumption does not necessarily expose them. Names “learnings” and “decisions” do not prove automatic extraction or improved future capacity.

The dashboard is a counterexample to treating every sessions row as a resumable full trace. It auto-creates a dashboard row after savings accrue; its data is only a conversation-empty JSON object. The ordinary typed loader requires the full SessionState fields. Thus latest-session selection can encounter a synthetic row that cannot deserialize as a full session (SRC-1, `sqz/src/main.rs`, `sqz_engine/src/session_store.rs`, `sqz_engine/src/types.rs`).

> let empty_data = serde_json::to_vec(&serde_json::json!({"conversation":[]}))?;
> --- `sqz_engine/src/session_store.rs`

#### MEM-OBJ-snapshot
Label: Snapshot and session guide parts

SRC-1, `sqz_engine/src/session_continuity.rs`, provides symbolic SnapshotEvent type/priority metadata enclosing natural-language content. The alternative library checkpoint uses `snapshot:{session_id}` cache keys and serialized event JSON, via `save_cache_entry` without an original. The generated guide is natural-language category text inside `<session_knowledge>` wrappers, for interpretation by a later agent. Snapshot JSON and displayed guide are different operative parts; budgets can omit material before the later consumer. No supplied object counterpart exists; related installed delivery is [RT-RTE-integration-install](runtime.md#rt-rte-integration-install).

> let hash = format!("snapshot:{session_id}");
>         self.store.save_cache_entry(&hash, &compressed)?;
> --- `sqz_engine/src/session_continuity.rs`

`build_snapshot` sorts priority and stops at the first event that exceeds a default 2048-byte serialized snapshot budget. It does not continue trying smaller low-priority events. The helper extracts last user text, tool-name-derived “active files,” fact key/values and recent error-like assistant text; the file label is not evidence of retained file paths. By contrast, CLI resume assembles events itself from summary, five recent turns, facts and edits; it neither calls the budgeted builder nor reloads `snapshot:` checkpoints. Guide generation uses a 2000 constant, with byte-length checks and safe text truncation, category order and wrapper overhead; the documented ~500 tokens is an estimate, not a hard token-budget proof.

> if candidate.size_bytes() > self.max_snapshot_bytes {
>                 // Remove the event that pushed us over budget.
>                 included.pop();
> --- `sqz_engine/src/session_continuity.rs`

### Routes

#### MEM-RTE-recall-search
Label: Recall snippet then explicit recovery

CLI recall and MCP sqz_recall consume caller query/limit, select FTS5 BM25 hits and return snippets with output hashes or session IDs. Source owner is SessionStore plus presentation handlers (SRC-1, `sqz_engine/src/session_store.rs`, `sqz/src/main.rs`, `sqz-mcp/src/lib.rs`). This search is distinct from supplied [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery), which resolves a known hash; it leads to that route rather than duplicating it.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked snippets, kind/date and output ref or session ID; no-match and errors are explicit.
- Later read-back: Previously admitted originals or nonempty session summaries supply indexed text; selected output hashes permit a separate expand request, while session IDs can target resume/export.
- Delegated visibility: CLI caller or MCP host receives text; no model worker context is created.
- Selection predicate: FTS query derived from supplied terms and BM25 rank; CLI limit clamped 1–50, MCP default 5 and clamp 1–25. Snippets use 24 FTS tokens, not a vector similarity search.
- Invalidation or expiry: Cache deletion removes matching recall rows; clear_cache removes output-kind recall rows. Search has no context-residency TTL gate.
- Activation or effect: Delivers recalled text and locators; actual model use and any avoidance of reruns are unobserved.
- Evidence limits: Indexing skips empty/NUL-containing inputs, caps indexed text at 262144 bytes and silently ignores indexing errors; no guarantee that all retained or previously seen content is searchable.

> ORDER BY bm25(recall_index) LIMIT ?2
> --- `sqz_engine/src/session_store.rs`

Admission occurs on successful original-cache writes or nonempty session-summary saves; it is automatic derived indexing, not another human approval. Index upsert replaces by ref_hash. A hash is an access locator, not proof of source correctness. Binary originals can remain expandable despite having no recall entry. Alternative checkpoint saves without originals do not enter the output index merely because a comment says they are indexed.

#### MEM-RTE-dependency-precache
Label: Predictive dependency pre-caching

Part of: [RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress)

This is the CLI route's distinct write subpath: `track_file` recognizes selected read commands, DependencyMapper parses output imports, and the proxy resolves/reads dependencies and admits their content with `store_compressed` (SRC-1, `sqz/src/cli_proxy.rs`). It is not an independent request to deliver those dependencies.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Surrounding compression output and optional pre-cache count, not dependency bodies.
- Later read-back: Admitted original/compressed dependency bytes feed future exact references, deltas, recall/expand and known-file annotations.
- Delegated visibility: No delegated agent; filesystem reads occur in the proxy process.
- Selection predicate: Recognized read-command base and final path, parsed import dependencies, resolution against parent path, existing readable file, never_store false, no fresh dedup hit and successful compression.
- Invalidation or expiry: Normal cache freshness and deletion apply; known-file rows persist separately.
- Activation or effect: Adds content and path metadata before any established model delivery of the dependency.
- Evidence limits: Parsing/resolution is heuristic; no host trace demonstrates the dependency was previously in context.

> // Compress and persist to L2 cache
>                     if let Ok(compressed) = self.engine.compress(&dep_content) {
> --- `sqz/src/cli_proxy.rs`

The software proposes and admits each write; the initiating caller is not a per-file human approver. Pattern rejection and read/compression failures can skip a file. No answer oracle or outcome-based improvement loop is involved. Recovery is original expansion or deletion, not rollback of a model's prior decisions.

#### MEM-RTE-cache-maintenance
Label: Cache pinning freshness and withdrawal

This collects explicit cache-policy writes under native CLI/store ownership, distinct from ordinary admission/expansion in [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery) and installed hooks in [RT-RTE-integration-install](runtime.md#rt-rte-integration-install). SRC-1, `sqz/src/main.rs`, `sqz_engine/src/cache_manager.rs`, `sqz_engine/src/session_store.rs`, implements pin add/set/unset, precompact markers, compact reporting, reset and lower-level deletion/LRU.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pin/status messages; compact summary; precompact empty JSON; reset plan/confirmation/result; low-level methods return Result/count.
- Later read-back: Persisted pinned/access/compaction metadata changes later cache presentation; deleting entries removes later recovery content and recall rows.
- Delegated visibility: Hook host or CLI caller receives results; no direct mutation of a model's context window.
- Selection predicate: Pin hash/prefix or add input; hook event; compact descriptors scored by age/frequency with default minimum keep 5 and ratio 0.3; reset flags/project/confirmation; low-level LRU by accessed_at and serialized-data size.
- Invalidation or expiry: Unpin restores normal age/marker checks; PreCompact persists last_compaction_at; clear_cache deletes entries/output recall/marker; invalidate(path) deletes only the hash of current file bytes; LRU removes entries until configured serialized size fits.
- Activation or effect: Deterministically changes later code selection or removes recovery storage; compact merely reports hypothetical evictions and marks refs stale when nonempty.
- Evidence limits: Pin does not re-inject content, LRU has no pin exclusion in its inspected loop, and its size accounting excludes original BLOB bytes. No inspected automatic evict_lru invocation establishes a hard disk-size ceiling.

> self.store.delete_cache_entry(hash)?;
> --- `sqz_engine/src/cache_manager.rs:722-743`

Admission controls differ: pin add ingests stdin, an existing file or literal text through the lower-level cache manager, calling `engine.compress` as transform rather than the engine's cache wrapper. It therefore does not inherit the wrapper's never_store write veto. Set/unset checks existing hash resolution. These explicit caller actions can be human or automated; content authorship is not established. Reset requires confirmation unless --yes; nonterminal empty input refuses. Software decides marker writes and hypothetical evictions. No task-answer oracle or per-content quality gate governs these metadata changes.

CLI reset defaults to clearing cache and statistics, not sessions, known_files or regret_log. `reset_all` is a different low-level method: it deletes cache, compression_log, sessions, known_files, metadata and recall_index, but not regret_log in the inspected SQL. Its “equivalent to deleting sessions.db” comment is therefore too strong. A project-filtered CLI reset changes project statistics and deliberately does not clear the global cache. These limits prevent interpreting reset as complete privacy withdrawal.

> if clear_cache && project_dir.is_none() {
>         match store.clear_cache() {
> --- `sqz/src/main.rs`

#### MEM-RTE-session-continuity
Label: Session import and resume delivery

CLI import reads CTX text; engine deserializes and saves it; export loads and serializes; resume selects an explicit ID or latest updated session, loads typed content, derives events, generates and prints a guide (SRC-1, `sqz/src/main.rs`, `sqz_engine/src/engine.rs`, `sqz_engine/src/ctx_format.rs`, `sqz_engine/src/session_continuity.rs`). This adds the actual session consumer to the integration route [RT-RTE-integration-install](runtime.md#rt-rte-integration-install); it is not a second installation record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Import ID/error, export CTX JSON, or resume guide on stdout with token metadata on stderr; missing/latest/load failures return without a guide.
- Later read-back: A later resume/export reads durable sessions.data; installed Claude SessionStart compact hook invokes sqz resume. The separate snapshot store/load API is available but not used by this CLI resume.
- Delegated visibility: CLI/hook host receives the guide; actual model injection/compliance depends on the host contract and was not observed.
- Selection predicate: Explicit ID or latest-session timestamp; resume includes summary, last five turns each clipped to 200 bytes safely, all facts and edit pairs before guide category/budget selection.
- Invalidation or expiry: Same-ID save/import replaces session content; no session TTL in the inspected consumer. Low-level reset_all deletes sessions; ordinary CLI reset does not. Removing hook/guidance stops the installed delivery request.
- Activation or effect: Produces a bounded later-context narrative; it does not change model weights, establish a truthful memory or directly restore a host window.
- Evidence limits: Initial full-session producer for ordinary cache operations is unresolved; dashboard synthetic rows may fail typed loading; guide truncation can omit source pointers, edit context and entire lower-priority categories.

> "matcher": "compact",
>                 "hooks": [{ "type": "command", "command": format!("{sqz_path} resume") }]
> --- `sqz_engine/src/tool_hooks.rs`

Admission: caller supplies CTX content; serde enforces structure, not factual correctness. Unsupported envelope versions warn but are not rejected solely for version. Same-ID upsert contradicts the facade comment that import always creates a new session. The source model field is metadata, not provenance authentication. There is no mandatory per-content human approval or semantic answer oracle. The caller can withhold/replace an import; restoration of an earlier exported file is possible, but no versioned rollback transaction is established. Guidance persists as caller session text/fields and generated guide, not automatically derived formulated criticisms.

> if envelope.version != "1.0" {
>             // Log a warning but still attempt to use the session.
> --- `sqz_engine/src/ctx_format.rs`

The library checkpoint alternative has afforded persistence/load operations, not established deployed read-back. The generic HookManager returns action enum values; its `BuildSnapshot` label and generated `build_snapshot = true` TOML do not themselves connect session acquisition, store_snapshot, load_snapshot and model delivery. The shipped PreCompact CLI actually marks references stale, while SessionStart executes resume from sessions.data.

### Claims

#### MEM-CLM-evaluation-scope
Label: Shipped evaluator measures retention and recovery

SRC-1, `sqz/tests/quality_bench.rs`, defines a binary-level evaluator with fixture facts/noise, sensitive/verbatim flags, token proxies and second-run/ref expansion checks. Closest supplied claim is [RT-CLM-recoverable-results](runtime.md#rt-clm-recoverable-results); this is distinct evaluator scope, not another universal recoverability claim.

Claim conclusion status: claimed

> byte-exact recovery: a second run yields a `§ref:HASH§` and
> //!   `sqz expand` returns the original bytes
> --- `sqz/tests/quality_bench.rs`

Fixture authors supply expected retained facts; this is an answer/reference oracle for that bounded benchmark, not a task-quality oracle in production. Test assertions can reject a build/test run, but no inspected route feeds benchmark outcomes into automatic content/preset revision. No tests were executed here, and fixture coverage does not establish model benefit or all-route recovery.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-reference-policy
Label: Retained metadata governs reference delivery

Consumer: native CacheManager and CLI proxy. Channel: SQLite access/pin/marker/path metadata. Force: deterministic code rules deciding ref/body eligibility and adding `[in context]` hints. Horizon: later invocations/processes sharing the database. This is distinct from [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance): metadata controls code, while any displayed hint/reference controls a model only through interpretation. SRC-1, `sqz_engine/src/cache_manager.rs`, `sqz/src/cli_proxy.rs`.

> if let Ok(true) = self.store.is_cache_entry_pinned(hash) {
>             return true;
>         }
> --- `sqz_engine/src/cache_manager.rs`

A durable flag can change later delivery without proving its residency premise. The horizon of the code policy is longer than the evidence that a particular model still knows a particular body.

## Annotations

#### On [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)

Storage and lineage split into [MEM-OBJ-cache-original](#mem-obj-cache-original), [MEM-OBJ-cache-compressed](#mem-obj-cache-compressed) and [MEM-OBJ-known-files](#mem-obj-known-files). Raw input bytes are distinct from derived text and access metadata. Exact-ref freshness defaults to 30 minutes and persisted markers; repeated ref sends refresh accessed_at, not proof of body presence. Explicit expansion reads retained originals without requiring freshness. The similarity path compares against compressed data and can select a baseline without the exact-ref freshness test (SRC-1, `sqz_engine/src/cache_manager.rs`; quoted in the object record). This qualifies a uniform freshness interpretation, not the existence of the supplied route.

#### On [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy)

The supplied passage establishes a requested compression route, not observed downstream activation. Lazy full descriptions in `tool_docs` are process-local natural-language documentation indexed by symbolic tool name; name-targeted help is explicit requested read-back. Shortened descriptions reduce initial tool context, and a help request can restore description content while the process retains it. This is different from persistent tool-result originals and hash expansion. It is not a subagent frame; upstream is a process/tool server, not an isolated model conversation. Source support and limits are the supplied record's passages, SRC-1, `sqz-mcp/src/proxy.rs`.

#### On [RT-CMP-wasm-engine](runtime.md#rt-cmp-wasm-engine)

The memoized hash→compressed-string cache has later identical-call reuse in process memory, but does not return native refs or store raw originals for expansion. Its separate session `{turns, corrections}` JSON is exported/imported, not the dedup cache, and `compress` does not append turns or corrections in the inspected body (SRC-1, `sqz-wasm/src/lib.rs`). Thus the exposed session interchange is not evidence of automatic browser trace memory. Import content is caller-authored with parser admission, not a model's learned update; its downstream behavioral consumer remains unestablished.

> serde_json::to_string(&self.session).map_err(|e| e.to_string())
> --- `sqz-wasm/src/lib.rs`

#### On [RT-RTE-browser-compress](runtime.md#rt-rte-browser-compress)

Selection is automatic proposal generation followed by accept/skip or submit-time adoption. The UI changes current input context; pending text is not durable session knowledge. Extension-local statistics/settings are symbolic local-storage state; memoized compressed content lives with WASM. Storage-key searches of SRC-1, `extension/background.js`, `extension-firefox/background.js`, `extension/content/common.js`, found statistics/settings operations, not an export_ctx/import_ctx caller. Available browser site adapters and bundle bytes remain uninspected for behavioral parity. Native SQLite recovery cannot be inferred.

## Write side

**Acquisition and admission.** Cache writes are automatic use-fed retention by the native engine wrappers/CLI/MCP; the never_store pattern guard and caller-specific gates differ. The runtime documents the length gate and no-cache limitations. Pin add is a lower-level alternative with different admission; dependency pre-caching retains material never established as delivered. Index admission is another lossy transformation: NUL/empty rejection, text decoding and byte cap affect search while leaving a captured original recoverable. Content writers, callers choosing a route and the software physically writing the DB are different agencies ([RT-RTE-cli-compress](runtime.md#rt-rte-cli-compress), [RT-RTE-file-read](runtime.md#rt-rte-file-read), [MEM-RTE-cache-maintenance](#mem-rte-cache-maintenance), [MEM-RTE-dependency-precache](#mem-rte-dependency-precache), [MEM-RTE-recall-search](#mem-rte-recall-search)).

**Derived results and later consumers.** Native input → compressed JSON/raw original → later cache probes, delta baselines, recall/expand is wired. File-tool originals begin after decoding/ranging/capping; command originals are the admitted command output, not an entire shell execution trace. Session content → imported durable SessionState → resume event projection → bounded guide is wired conditionally on valid stored content. Library session→priority snapshot→cache checkpoint has store/load capability, but no inspected shipped restoration from that checkpoint. Corrections/facts in imported sessions can carry trace-derived material, yet the initial author/extraction route remains unresolved. This prevents claiming an automatic trace-to-lesson loop. Reasons can survive full session text and edit context; the guide selectively drops those fields ([MEM-OBJ-session](#mem-obj-session), [MEM-OBJ-snapshot](#mem-obj-snapshot), [MEM-RTE-session-continuity](#mem-rte-session-continuity)).

**Metadata is not learned content.** CLI reruns and expansions write regret_log; compression writes counts/stages/project data; dashboard and stats later read these metrics. Those raw signals are not a retained policy update. The separate RegretTracker does adjust numeric in-memory aggressiveness recommendations, but its own source states the hook path does not use it. Initial content IDs and event kinds are caller supplied, not evidence of authenticated model criticism (SRC-1, `sqz_engine/src/regret_tracker.rs`, `sqz_engine/src/session_store.rs`; [MEM-OBJ-operation-metadata](#mem-obj-operation-metadata)).

**Editing and withdrawal.** Configuration reload and installed natural-language rules can change later context selection; these existing routes are [RT-RTE-preset-reload](runtime.md#rt-rte-preset-reload) and [RT-RTE-integration-install](runtime.md#rt-rte-integration-install). They are caller/operator changes, not automatic improvements inferred from feedback. Imported same-ID content replaces sessions. Unpin changes policy, not payload; freshness invalidation leaves payload available; cache deletion removes it. Neither marker writes nor compact summaries delete host messages. CLI reset does not cover every retained substrate, and tee files/browser state are separate stores. No universal rollback or full withdrawal guarantee follows ([MEM-RTE-cache-maintenance](#mem-rte-cache-maintenance), [MEM-CMP-library-stores](#mem-cmp-library-stores)).

## Read-back

**Requested recovery.** Query-bearing recall requests select indexed snippets; a second hash/range request recovers retained bytes. Query targeting and prefix addressing are different selectors. A ranged recovery restores only that range. Compressed-only entries cannot produce original bytes. Content delivery does not promote it to trusted instructions; the eventual external consumer assigns meaning and priority ([MEM-RTE-recall-search](#mem-rte-recall-search), [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)).

**Automatic selection within a request.** A file/command request triggers hash/slice/similarity selection of prior content or a reference; this is an automatic choice inside requested delivery, not independent unsolicited memory injection. No hard model-window budget or membership test is established. The guide hook is the notable push-style alternative: SessionStart with matcher compact runs resume, which chooses latest session, projects its parts and prints the bounded guide. Host scheduling and stdout injection remain external contracts; the library snapshot loader is not this route ([MEM-RTE-session-continuity](#mem-rte-session-continuity)).

**Working-context control beyond persistence.** HTTP history shortening keeps recent messages and first/last lines of selected older material; no reloadable middle is established. Browser/IDE transforms replace proposed/current input, with no native recovery guarantee. MCP lazy descriptions leave short text while full docs remain reachable by help. File-tool caps keep continuation locators but omitted file portions require another read; they were not retained by that cache entry. These controls are distinct from accumulating turns ([RT-RTE-request-transform](runtime.md#rt-rte-request-transform), [RT-RTE-browser-compress](runtime.md#rt-rte-browser-compress), [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy), [RT-RTE-file-read](runtime.md#rt-rte-file-read)).

The additional exposed context-control capabilities below are not evidence of an unspecified live consumer. Their code operates on text or symbolic counters, not provider weights or opaque KV tensors. Their integration/benefit limits remain local.

### Additional library context controls

`FileReader::read` accepts caller-supplied source, mode, intent and cached_content; Full/Map/Signatures/Diff/Aggressive/Entropy/Task/Lines select current-call representations. It is not the MCP handler simply by having a similar name. The interface supplies a cached baseline for diff, but establishes no internally persisted originals. Detailed entropy/task mode algorithms and caller adoption remain uninspected (SRC-1, `sqz_engine/src/file_reader.rs`).

`SqzEngine::reorder_context` uses a LITM positioner on caller sections; prompt-boundary detection heuristically splits caller text; sink preservation protects estimated byte prefixes/markers and compresses the tail. These symbolic functions determine candidate model-visible text without accessing a provider cache. Reordering guidance alone establishes no observed attention benefit. `ProgressiveThrottler` records in-memory tool-name/parameter-hash counts and returns Normal/Reduced/Blocked labels, resetting on explicit calls; its method does not itself trim results, block a tool or establish retained cross-process memory (SRC-1, `sqz_engine/src/engine.rs`, `sqz_engine/src/prompt_cache.rs`, `sqz_engine/src/kv_cache_optimizer.rs`, `sqz_engine/src/progressive_throttle.rs`).

> let count = self.counts.entry(key).or_insert(0);
>         *count += 1;
> --- `sqz_engine/src/progressive_throttle.rs`

`SandboxExecutor::execute_with_intent` runs caller code through a subprocess, caps/decodes stdout, and for sufficiently large stdout plus intent, uses transient in-memory FTS to return matched sections and a vocabulary. The local FTS connection is not retained for a future search; matched output replaces stdout. Stderr is not captured on the inspected executor path. This is non-model computation with a filtered return boundary, not an isolated model agent whose whole conversation frame is popped. Its interface and filter support working-context reduction, not later restoration of the omitted stdout (SRC-1, `sqz_engine/src/sandbox_executor.rs`).

> result.stdout = filtered.matched_sections.join("\n\n");
> --- `sqz_engine/src/sandbox_executor.rs`

The stack-frame analogy is therefore limited: temporary computation can keep bulk out and return a selected value, but no inspected sqz-owned subagent context exists on these paths. Native refs are text locators, not heap pointers automatically followed by model attention; pinned data and persisted paths have no host-window liveness semantics. The distinction matters most after compaction or predictive pre-caching.

## Integration issues

1. **Delta freshness qualification.** [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery) describes freshness with the combined cache route. [MEM-OBJ-cache-compressed](#mem-obj-cache-compressed) establishes that the inspected delta baseline method reads compressed data without exact-ref freshness gating. Keep exact/slice freshness separate from the near-duplicate baseline's availability and the unknown downstream reconstruction behavior.
2. **Full-session acquisition is not ordinary cache admission.** [MEM-OBJ-session](#mem-obj-session) and [MEM-RTE-session-continuity](#mem-rte-session-continuity) add CTX import, actual SessionStart compact delivery and a failing alternative: dashboard-only rows do not satisfy typed SessionState loading. The supplied runtime already leaves production completeness open; do not reconcile this into an automatic complete trace capture loop. Latest-session selection is not project-scoped in the inspected resume call.
3. **Checkpoint alternatives are not equivalent.** [MEM-OBJ-snapshot](#mem-obj-snapshot) and [MEM-RTE-session-continuity](#mem-rte-session-continuity) distinguish stored snapshot JSON, budgeted builder and CLI's direct event projection. Snapshot save lacks an original and therefore lacks the normal output-index upsert; its comment claiming FTS retrieval is not sufficient. Reconciliation must not infer that PreCompact stores a snapshot or resume loads one.
4. **Pin/reset limits.** [MEM-RTE-cache-maintenance](#mem-rte-cache-maintenance) adds lower-level pin-add admission, non-pin-aware LRU and reset scope. Cache pins, session-turn pins and host context retention are different. The low-level reset_all comment overstates SQL scope because regret_log remains. No supplied record is replaced; these qualify any blanket cache/privacy guarantee.
5. **Origin and operation gaps.** [MEM-RTE-dependency-precache](#mem-rte-dependency-precache) is explicitly part of the supplied CLI route, not a duplicate declaration. New object records split content and metadata that supplied routes combine; none duplicates a supplied object. No other possible duplicate identified. Generic HookManager, auxiliary stores, adaptive recommendations, sink/cache heuristics and browser interchange have available APIs but unestablished deployed consumer chains. Detailed mode bodies, other site adapters, all exposed transform algorithms and package bytes are not fully inspected, preventing exhaustive equivalence or control claims.

## Limitations and checks

This is a source-grounded architectural account, not a successful execution report. No model/provider parameters were inspected or updated; no source-to-binary correspondence, actual host-window membership, observed recall use or measured quality benefit was established. Available but uninspected bodies are named in coverage, not called access failures or absences. The direct-source additions all remain within SRC-1 and its pin; the method was the supplied memory job, member types and record contract, with no prior-analysis exposure or target execution. Validation: the required commonplace-validate candidate check passed for role memory against the supplied artifact. Its complete result was: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes form and quotation occurrence, not analytical correctness or acceptance.
