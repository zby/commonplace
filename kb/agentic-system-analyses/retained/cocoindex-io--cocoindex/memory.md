---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "CocoIndex memory: dependency-conditioned internal reuse, maintained content indexes and shipped retained-session search consumers."
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
source-identity: "https://github.com/cocoindex-io/cocoindex"
reviewed-boundary: "1639793b3602408a9cb220728fb30e306d433473"
---

# CocoIndex memory report

## Boundary and evidence

This report covers CocoIndex at the frozen revision in [boundary](boundary.md#source-register), SRC-1. The memory scope includes internal component/function reuse, persistent user state, target bookkeeping, externally retained text and numerical indexes, imported coding-session checkpoints, extraction products and shipped read-back programs. It includes maintenance and diagnostic entry points, not just vector storage. It does not treat the separately linked CocoIndex-code product as acquired evidence. External database, provider, embedding-weight and Entire checkpoint-generator implementations remain outside the frozen source; their adapters and example consumers remain inside it.

The supplied runtime is provisional evidence for the routes it traces. Direct reads here extend it with the schema and submit lifecycle, Python function-cache and state APIs, ID generation, session ingestion and display, diagnostic CLI and alternate retrieval consumers. Every source finding below is implementation evidence from SRC-1 unless explicitly called documentation, test specification or inventory. No execution evidence was supplied or generated.

| Entry point / memory operation | Source path in SRC-1 | Coverage and conclusion limit |
|---|---|---|
| CLI update, Python/Rust SDK update; live, preview and drop | `python/cocoindex/cli.py`; `rust/core/src/engine/app.rs`; `rust/sdk/cocoindex/src/app.rs` | Supplied [RT-RTE-index-update](runtime.md#rt-rte-index-update), [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance), [RT-RTE-preview-update](runtime.md#rt-rte-preview-update), [RT-RTE-drop-app](runtime.md#rt-rte-drop-app); CLI diagnostic bodies also read directly. SDK bodies not independently reread. |
| Component memo restore | `rust/core/src/state/db_schema.rs`; `rust/core/src/engine/execution.rs` | Schema read directly; dependency checks supplied by [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), annotated below. |
| Function memo restore/write and stable IDs | `python/cocoindex/_internal/function.py`; `python/cocoindex/resources/id.py`; `rust/core/src/state_store/submit_session.rs` | Direct bounded reads; [MEM-OBJ-function-memoization](#mem-obj-function-memoization), [MEM-RTE-function-reuse](#mem-rte-function-reuse). |
| User-state assignment, serialization and later keyed access | `python/cocoindex/_internal/api.py`; `python/tests/core/test_use_state.py`; `rust/core/src/state_store/submit_session.rs` | Direct API/commit and counter-test reads; [MEM-OBJ-state-handle](#mem-obj-state-handle), [MEM-RTE-state-access](#mem-rte-state-access). Generic API is a capability; counter consumer is test wiring, not deployed use. |
| Target ownership, staging, child existence and retry | `rust/core/src/state_store/submit_session.rs`; `rust/core/src/engine/execution.rs`; `python/cocoindex/connectors/postgres/_target.py` | Direct lifecycle/commit/GC/delete reads; [MEM-OBJ-tracking-info](#mem-obj-tracking-info). Detailed conflict resolution and every connector's retirement semantics remain uninspected. |
| Text rows, vectors, lineage and top-k delivery | `examples/text_embedding/main.py` | Full direct read; [MEM-OBJ-doc-embedding](#mem-obj-doc-embedding), [MEM-OBJ-doc-vector](#mem-obj-doc-vector); supplied query route annotated. |
| Session transcript, prompt, context and metadata admission and retrieval | `examples/entire_session_search/main.py` | Full direct read; [MEM-OBJ-session-embedding](#mem-obj-session-embedding), [MEM-OBJ-session-metadata](#mem-obj-session-metadata), [MEM-RTE-session-search](#mem-rte-session-search). Upstream summary generation unavailable within SRC-1. |
| Typed manual extraction | `examples/manuals_llm_extraction/main.py` | Supplied [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), annotated; no independently inspected later query consumer. |
| Image search HTTP APIs and hybrid filing search | `examples/image_search/api.py`; `examples/image_search_colpali/api.py`; `examples/sec_edgar_analytics/search.py` | Direct reads; [MEM-RTE-alternate-search](#mem-rte-alternate-search). Image producer/helper signatures searched, not fully traced; filing producer and model freshness remain unresolved. |
| DSPy patient extraction to JSON files | `examples/patient_intake_extraction_dspy/main.py` | Full direct read: page images → fixed ChainOfThought signature → Patient JSON → declared local files. No optimizer, evaluation-fed revision or later file consumer established by this file; dependency behavior uninspected. |
| Diagnostic `ls`/`show`, app-loaded and database-only paths | `python/cocoindex/cli.py` | Dispatch inventoried; show/query/render bodies read directly; [MEM-RTE-inspect-state](#mem-rte-inspect-state). Display summaries do not expose all opaque payloads. |
| Contributor hooks and public authoring guidance | `.claude/settings.json`; `skills/cocoindex/SKILL.md` | Hook configuration directly read: PostToolUse Edit/Write and Stop launch check scripts. Script effects uninspected; cannot infer a retained criticism-to-policy loop. Public skill content supplied via boundary, not reread. Static guidance is not use-derived memory. |
| Other connectors, examples, benchmarks and graph/model operations | `python/cocoindex/connectors/`; `examples/`; `benchmarks/`; `python/cocoindex/ops/` | Source-tree inventory and bounded searches only beyond rows above. Graph extraction, entity resolution, multi-codebase summaries, audio, other stores and Rust image-query programs remain included but not independently traced. Their admission, provenance, cleanup and later consumers cannot inherit the inspected paths' conclusions. |

Searches checked frozen CLI dispatch and exposed Python APIs against runtime routes. A bounded search for MCP/tool registration in `python/cocoindex/`, `pyproject.toml` and `.claude/` identified no additional registration to trace; it is not a repository-wide absence finding. No inaccessible repository file is claimed: remaining coverage gaps are uninspected source. The frozen checkout HEAD matched the reviewed commit and its status was clean.

## Core ideas

1. **Reuse memory and retrieval memory have different consumers.** Internal memos let the execution engine substitute retained returns and preserve declared dependencies. External rows let separately invoked search programs select content. The first changes work performed during an update; the second changes the material delivered in search results. Neither establishes an answering-agent memory loop. See [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), [MEM-RTE-function-reuse](#mem-rte-function-reuse) and [RT-RTE-query-index](runtime.md#rt-rte-query-index).
2. **Freshness is tracked identity, not semantic trust.** Cache checks and target ownership mediate reuse/maintenance; selected source text and model-produced records are not admitted by a factual-support judge. The manual route's typed validation does not establish entailment. Unchanged model aliases can hide external changes. These countercases bound the claim that an index is always current or correct. SRC-1: `python/cocoindex/_internal/function.py`; [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), [RT-CMP-sentence-transformer-embedder](runtime.md#rt-cmp-sentence-transformer-embedder).
3. **Retaining traces is not the same as learning a method.** Session search automatically parses and embeds transcript text, imports prompt/context artifacts and later prints selected snippets. It does not itself create the imported context summary or install it as an agent instruction. Source roles and checkpoint IDs provide lineage, not trust levels. [MEM-RTE-session-search](#mem-rte-session-search).
4. **The context budget is implemented at specific boundaries.** Text indexing splits at 2000 with 500 overlap; text querying defaults to five rows; session display truncates each selected text to 200 characters. These are chunk/result/display controls, not an inspected model-window budget. No supplied route shows a host removing old conversation turns, popping an agent frame or reloading a compacted host checkpoint. Provider-visible manual Markdown is an explicit request context, not evidence of conversation compaction. SRC-1: `examples/text_embedding/main.py`, `examples/entire_session_search/main.py`; [RT-BAP-extraction-prompt](runtime.md#rt-bap-extraction-prompt).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-function-memoization
Label: FunctionMemoizationEntry

Source-native function memo, distinct from supplied [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization): schema has separate FunctionMemoizationEntry and ComponentMemoizationInfo structs. Both live within per-app LMDB, but function entries additionally retain declared target paths and side-effect dependency entries. Its envelope is symbolic serialized metadata; return bytes can encode text, vectors or arbitrary registered values, so the envelope's form does not classify every payload. Lineage is a memoized function call, logic dependencies, context/memo states and target-provider generations. Later function calls consume it through a cache probe, not natural-language interpretation. SRC-1: `rust/core/src/state/db_schema.rs`, `rust/core/src/state_store/submit_session.rs`; storage doctrine in `docs/src/content/docs/advanced_topics/internal_storage.mdx`.

> pub struct FunctionMemoizationEntry<'a> {
>     /// Memoization info is stored in the component metadata
>     #[serde(rename = "R", borrow)]
>     pub return_value: MemoizedValue<'a>,
> --- `rust/core/src/state/db_schema.rs`

This retains computed results and validation dependencies, not necessarily reasons for the result. The embedding-return case can hold numerical memory without updating model parameters. Stable ID generation also uses memoized calls keyed by dependency fingerprint and ordinal, giving later updates reusable identities rather than semantic knowledge. SRC-1: `python/cocoindex/resources/id.py`.

#### MEM-OBJ-state-handle
Label: StateHandle persistent value

The Python handle exposes per-component, per-StableKey user state, with serialized backing in the internal store and an object-backed value during execution. Its key/slot and serialization protocol are symbolic; arbitrary payload form and provenance depend on caller code. It is distinct from component memoization: caller assignment changes this value rather than the engine automatically substituting a cached call return. Closest supplied record is [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), not the same referent. SRC-1: `python/cocoindex/_internal/api.py`, `rust/core/src/state_store/submit_session.rs`.

> self._stored = self._core_processor_ctx.update_user_state(self._key, new_value)
> --- `python/cocoindex/_internal/api.py`

Initial state control belongs to the API caller; the interface alone does not identify a human editor. Serialization is deferred to commit and in-place object changes before commit can be captured. A concrete shipped test stores a counter, reloads it and increments it; that is symbolic numeric state, not a demonstrated learned rule. Other opaque caller payloads cannot inherit this classification. SRC-1: `python/tests/core/test_use_state.py`.

#### MEM-OBJ-tracking-info
Label: StablePathEntryTrackingInfo and submit bookkeeping

This record covers the symbolic internal reconciliation envelope: component tracking, ownership rows, child-existence records, tombstones and staging information. Storage is per-app LMDB. These are access/recovery metadata, not searchable document text. The engine consumes them to determine ownership, reuse and cleanup. Distinct from [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), though related memo information can reside in tracking data; this record does not redeclare that memo referent. SRC-1: `rust/core/src/state_store/submit_session.rs`, `rust/core/src/engine/execution.rs`.

> // Only drop the owner row if it still points at us. A
> // component that preempted this path between our last
> // run and this delete has already upserted itself as
> // owner; deleting unconditionally would orphan it.
> --- `rust/core/src/state_store/submit_session.rs`

Lineage is execution/reconciliation, not model-authored curation. Precommit, external sink application and final internal commit are separate phases; source does not establish an atomic transaction spanning all stores. Durable tombstones support later cleanup retries, not guaranteed immediate withdrawal from a queryable external index.

#### MEM-OBJ-doc-embedding
Label: DocEmbedding text and lineage fields

Text is natural-language source content retained in PostgreSQL; filename, character offsets and ID are symbolic lineage/identity fields consumed by fixed code. Rows derive from Markdown splitting, not abstractive summarization. The query selects text and filename but omits stored offsets and IDs from its printed projection. The row's vector part is separately assessed in [MEM-OBJ-doc-vector](#mem-obj-doc-vector). Closest supplied record [RT-RTE-index-update](runtime.md#rt-rte-index-update) is its producer route, not an object duplicate. SRC-1: `examples/text_embedding/main.py`.

> filename=str(filename),
> chunk_start=chunk.start.char_offset,
> chunk_end=chunk.end.char_offset,
> text=chunk.text,
> --- `examples/text_embedding/main.py`

Later consumer authority is search-result content interpreted by the recipient, not a system instruction. Source editing or code changes can replace the indexed material through another update; there is no per-chunk approval gate in this example. Source roots, filters, chunking and target schema are author-selected symbolic policy.

#### MEM-OBJ-doc-vector
Label: DocEmbedding embedding field

Dense embeddings are distributed-parametric representations stored alongside the text in PostgreSQL and consumed numerically by distance ordering. They derive from chunk text through [RT-CMP-sentence-transformer-embedder](runtime.md#rt-cmp-sentence-transformer-embedder), not from training in the inspected route. Exact weights are unpinned and their resolved provenance is outside SRC-1. The vector influences which text reaches the recipient; it is not itself readable evidence for the text's assertions. Distinct operative part of the produced row, with different consumption from [MEM-OBJ-doc-embedding](#mem-obj-doc-embedding); closest supplied producer is [RT-RTE-index-update](runtime.md#rt-rte-index-update). SRC-1: `examples/text_embedding/main.py`.

> embedding: Annotated[NDArray, EMBEDDER]
> --- `examples/text_embedding/main.py`

#### MEM-OBJ-session-embedding
Label: SessionEmbeddingRow

PostgreSQL retains session text, dense vectors and symbolic checkpoint/session/content-type/role/ID fields. The text and vector consumption paths differ: vectors select records; the recipient interprets the displayed text. Raw source files are not wholly reproduced: transcript parsing keeps textual parts, ignores invalid JSON and drops text shorter than 20 characters; context Markdown is chunked; prompt text is stripped and embedded. These products are derived retrieval memory from imported traces, not newly formulated explanations. Upstream `context.md` authorship, summarization method and completeness are unknown. This is distinct from the document rows above and has no supplied object counterpart; the nearest route comparison is [RT-RTE-query-index](runtime.md#rt-rte-query-index). SRC-1: `examples/entire_session_search/main.py`.

> elif isinstance(part, dict) and part.get("type") == "text":
>     text_parts.append(part.get("text", ""))
> --- `examples/entire_session_search/main.py`

> if len(text) < 20:
>     continue
> --- `examples/entire_session_search/main.py`

The same model name is used as in the supplied embedder record; its inference-only call and unpinned-weight limits apply. Role labels are descriptive data. Retrieval does not promote an imported assistant statement into authoritative guidance.

#### MEM-OBJ-session-metadata
Label: SessionMetadataRow

Separate PostgreSQL rows keyed by checkpoint/session retain imported intent text, computed total token count, serialized filenames and optional attribution percentage. Intent is natural-language display/content material; counts, identifiers and serialized arrays are symbolic. Lineage is `metadata.json`, not the entire conversation. The inspected query reads only the embedding table, not this metadata table: storage is wired, a later metadata consumer is uninspected. This is distinct from [MEM-OBJ-session-embedding](#mem-obj-session-embedding) and has no supplied record counterpart after comparison with the text-index route. SRC-1: `examples/entire_session_search/main.py`.

> input_t = token_usage.get("input_tokens", 0) or 0
> output_t = token_usage.get("output_tokens", 0) or 0
> total_tokens = input_t + output_t
> --- `examples/entire_session_search/main.py`

No evidence turns these counters into a later optimization/admission criterion. Invalid metadata JSON returns without declaring a metadata row; that differs from admitting every source byte unchanged.

### Routes

#### MEM-RTE-function-reuse
Label: Function memo reuse

Endpoints: later memoized function invocation → fingerprint/cache reservation → validation → cached return or execution and resolution. Python wrapper/core guard own selection and the commit path persists results. Distinct from supplied [RT-RTE-index-update](runtime.md#rt-rte-index-update): this is its reusable internal function mechanism, also available to other pipelines; the component memo object is separately supplied. SRC-1: `python/cocoindex/_internal/function.py`, `rust/core/src/state_store/submit_session.rs`.

- Immediate return: Deserialized cached value when reusable, otherwise newly computed function result.
- Later read-back: Stored function return/dependencies reach later calls with the matching memo fingerprint.
- Delegated visibility: Cache validation sees stored positional/context states and current registered state methods; caller receives typed return, not a rationale transcript.
- Selection predicate: Fingerprinted call and configured memo-key transforms, followed by cache/state validity checks.
- Invalidation or expiry: Invalid state causes execution; commit plans can clear/delete entries. No universal wall-clock TTL is established by these reads.
- Activation or effect: Cache hit bypasses execution and joins retained dependencies; successful real reuse is unobserved.
- Evidence limits: Generic payload semantics and external change-detection adequacy depend on caller/provider contracts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> assert guard.cached_value is not None
> return cast(
>     R_co,
>     guard.cached_value.get(self._resolved_return_deserializer),
> )
> --- `python/cocoindex/_internal/function.py:1465-1469`

Automatic admission follows successful function completion and memo resolution/commit, not human result approval. Code authors can alter memo keys or logic, while callers can force reprocessing through the supplied update path. Errors may prevent completion; invalid entries are recomputed rather than semantically repaired. Guidance is the authored function and its state/key protocol; retained products are return values and dependencies, not automatically revised guidance. No answer oracle or improvement experiment is present on this route.

#### MEM-RTE-state-access
Label: Persistent state access

Endpoints: component caller → `use_state(key, initial_value)` → handle read/assignment → commit → later keyed access. This is an API affordance plus a concrete counter consumer in test source, not a demonstrated production application route. It differs from [RT-RTE-index-update](runtime.md#rt-rte-index-update) and cached return substitution. SRC-1: `python/cocoindex/_internal/api.py`, `rust/core/src/state_store/submit_session.rs`, `python/tests/core/test_use_state.py`.

- Immediate return: StateHandle with stored or initial value; assignment updates its object-backed cell.
- Later read-back: A subsequent component run requesting the same key can receive the committed value; the counter test explicitly reads and increments it across updates.
- Delegated visibility: Caller reads its component/key value with optional type-directed deserialization; arbitrary payload meaning is not exposed by the slot API.
- Selection predicate: Stable component identity and StableKey, not semantic relevance.
- Invalidation or expiry: Commit plans clear/write/delete user-state slots; explicit app drop removes per-app state. Detailed undeclared-slot retirement logic is not independently traced here.
- Activation or effect: Test caller uses prior counter value to compute its successor; production payload behavior remains unspecified.
- Evidence limits: Test source is not a passing test run; the generic API alone establishes no deployed consumer or human admission role.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> handle = coco.use_state("counter", 0)
> _captured[item] = handle.value
> handle.value = handle.value + 1
> --- `python/tests/core/test_use_state.py`

Caller code proposes and assigns state; engine constraints and commit serialization admit it. The API rejects calls inside memoized functions and shifted component-subpath blocks. Starting an app is not content approval; initial human control is unresolved for arbitrary callers. Recovery is caller-defined or reinitialization/drop, not an established semantic rollback. No answer oracle, improvement objective or learned theory is established by the counter example.

#### MEM-RTE-session-search
Label: Session checkpoint search

Endpoints: checkpoint files → parsing/chunking/embedding → PostgreSQL rows → later user query embedding → SQL selection → printed snippet. Indexing code and query code own separate steps. This extends the supplied runtime's acknowledged uninspected session path; it is distinct from [RT-RTE-query-index](runtime.md#rt-rte-query-index), which reads document chunks. SRC-1: `examples/entire_session_search/main.py`.

- Immediate return: Index app completes separately; query prints checkpoint/session identity, content-type/role, score and a snippet.
- Later read-back: Retained transcript, prompt and imported context text reach a later query invocation through embedding-table selection.
- Delegated visibility: Embedder sees the current text/query; SQL sees the query vector and top-k; recipient sees only the first 200 characters of each selected text, not full stored context or tool payloads.
- Selection predicate: Source matcher admits full.jsonl, prompt.txt, context.md and metadata.json, excluding content_hash.txt; query orders embedding cosine distance ascending, default limit five.
- Invalidation or expiry: Memoized file processing and mounted source maintenance can change rows; no TTL is specified. Exact external checkpoint provenance and independent model alias drift remain unresolved.
- Activation or effect: Parsed traces become searchable derived rows and bounded display; no answering-agent injection or behavior change is observed.
- Evidence limits: Source-only; metadata-table retrieval, upstream summary generation and downstream use of snippets are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> print(f"    {r['text'][:200]}")
> --- `examples/entire_session_search/main.py`

Admission is automatic transformation of matcher-selected files, not per-record human approval. Invalid JSON and trivial text are rejected by code; imported context is accepted as content without verifying its claims. The operator can edit inputs or rerun/drop, but no reconstruction of missing tool payloads is shown. The raw-trace → filtered textual record → dense retrieval key → later snippet chain is wired; this is trace-fed indexing, not demonstrated improvement of future capacity. Imported context may already contain a summary, but this application does not establish how it was made or whether its reasons survive. Fixed file routing and splitter settings guide transformation; those settings are not revised from search outcomes. No answer oracle or candidate-improvement competition is shown.

#### MEM-RTE-alternate-search
Label: Alternate retained-content search

Endpoints: image HTTP search or filing-search CLI → query transformation → external index selection → response/display. These are alternate read-back channels, not duplicate instances of [RT-RTE-query-index](runtime.md#rt-rte-query-index). Image app startup also explicitly starts live maintenance and waits for READY; serving search does not rely solely on a hypothetical library caller. SRC-1: `examples/image_search/api.py`, `examples/image_search_colpali/api.py`, `examples/sec_edgar_analytics/search.py`.

- Immediate return: Image APIs return filename/score JSON; filing search prints filename, source type, topics, score and text prefix.
- Later read-back: Qdrant payload filenames and retained filing_chunks text/metadata reach later requests. Image bytes are served separately from local static files, not returned from the vector payload by this handler.
- Delegated visibility: Image helper receives query embedding and limit; response projection omits stored vectors and other payload parts. Filing output truncates text to 160 characters.
- Selection predicate: Image caller supplies q and limit (default five); ranking delegated to searched pipeline helpers/Qdrant and not fully traced here. Filing code combines vector-distance and lexical ranks using reciprocal rank fusion with optional source_type filter and default limit five.
- Invalidation or expiry: Image live maintenance wiring is visible; detailed vector regeneration, model revision detection and filing producer retirement are uninspected.
- Activation or effect: Retained identifiers/text are delivered through shipped service/CLI code; model-answer use is not established.
- Evidence limits: Full producer/helper algorithms and external search-engine contracts are not audited; no real service request or quality result is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 1.0/(60 + s.rk) + 1.0/(60 + l.rk) AS rrf
> --- `examples/sec_edgar_analytics/search.py`

The query handlers read rather than admit new content; producer admission is unresolved for these alternate indexes. Image model internals are not inferred from the API. This preserves the shipped consumption witness without pretending that inspecting the HTTP projection establishes every numerical selector or model-fixity property.

#### MEM-RTE-inspect-state
Label: Internal state inspection

Endpoints: CLI show with app or database/app name → stable-path or target-state query/iteration → readable diagnostic output. Code owns the selector and projection. Distinct from supplied production query route [RT-RTE-query-index](runtime.md#rt-rte-query-index): this consumes internal bookkeeping rather than semantic content. SRC-1: `python/cocoindex/cli.py`.

- Immediate return: Printed stable paths/details, memo-presence flags, target-state counts, ownership/generation and dangling markers.
- Later read-back: Persistent internal metadata is exposed to a later operator diagnostic invocation, including database-only access without loading an app.
- Delegated visibility: Renderer receives detail/entry summaries; default output is not deserialized function returns or complete user-state content.
- Selection predicate: Explicit stable path with recursive/parent options, full iteration, or target-state listing; optional fingerprint rather than readable-label display.
- Invalidation or expiry: inapplicable — diagnostic selection does not itself expire retained content.
- Activation or effect: Diagnostic delivery is wired; subsequent operator edits or decisions are unobserved.
- Evidence limits: CLI consumers are inspected, underlying inspection implementation only inventoried; no complete raw-payload inspection guarantee follows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> f"    has_memoization:{'true' if detail.has_memoization else 'false'}"
> f" target_state_count:{detail.target_state_count}"
> --- `python/cocoindex/cli.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization)

Storage: per-app internal LMDB, according to SRC-1 `docs/src/content/docs/advanced_topics/internal_storage.mdx`, separate from external content targets. The serialized envelope is symbolic; return/memo-state bytes may encode other forms. Direct schema inspection confirms inline byte payloads and separate positional/context memo states. Later engine probes reuse returns under tracked validity, giving this material execution-substitution authority, not instruction authority. Reasons are not a required field of this schema. SRC-1: `rust/core/src/state/db_schema.rs`.

> pub enum MemoizedValue<'a> {
>     #[serde(untagged, borrow)]
>     Inlined(#[serde_as(as = "Bytes")] Cow<'a, [u8]>),
> }
> --- `rust/core/src/state/db_schema.rs`

#### On [RT-RTE-query-index](runtime.md#rt-rte-query-index)

Read-back is pull: the user initiates a query, code embeds it, SQL selects retained text by numerical distance, and the printer delivers text/filename/score. The default five-row budget is a result count, not a token budget or model-visible context limit. Direct source read confirms that stored chunk offsets do not cross the SQL projection. Natural-language text reaches a human-facing result channel; no answering-model authority is established. SRC-1: `examples/text_embedding/main.py`.

#### On [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction)

Write-side lineage is source PDF → converted Markdown → model-proposed ModuleInfo → schema-validated record/full JSON, as supported by the supplied route and its passages. PostgreSQL content and memo returns can persist, but a concrete later content reader for this example remains uninspected. The stored extraction is not shown retaining a separate criticism or justification history, nor being reloaded as a system instruction. Admission is software/schema-mediated; generic operator initiation is not per-record human approval. SRC-1: `examples/manuals_llm_extraction/main.py`.

## Write side

Acquisition is author-configured and code-admitted. In the directly inspected text and session examples, source matching determines what gets read. Splitting, role/text parsing, embeddings and declarative row construction transform that material automatically. Markdown chunks preserve source text with overlap; session parsing discards non-text content and short/invalid entries; metadata computes totals rather than reproducing raw JSON. These are different transformations and provenance losses, not one universal summarizer. [MEM-OBJ-doc-embedding](#mem-obj-doc-embedding), [MEM-OBJ-session-embedding](#mem-obj-session-embedding), [MEM-OBJ-session-metadata](#mem-obj-session-metadata).

Authorship, admission and physical writes differ. Source authors supply material; application authors set matching/schema/model policy; wrapper/core/connector code admit cached results or target changes. The inspected manual and DSPy routes let a model propose content and code persist the structured result, without establishing a human support check. DSPy naming alone does not establish optimization: the inspected file instantiates ChainOfThought and writes Patient JSON, while optimizer/dependency behavior remains uninspected. SRC-1: `examples/patient_intake_extraction_dspy/main.py`; [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction). Arbitrary StateHandle initialization may have human or software origin; that uncertainty does not erase known subsequent assignment/commit semantics. [MEM-RTE-state-access](#mem-rte-state-access).

Internal writes preserve reusable computation and maintenance metadata. The directly read submit lifecycle separates precommit, sink apply and final commit. Commit writes function memos and regular user state and reconciles child existence; owner deletion checks that the current owner is still the retiring component. Therefore a single internal transaction is not evidence of one atomic database-plus-LMDB rollback. SRC-1: `rust/core/src/state_store/submit_session.rs`; [MEM-OBJ-tracking-info](#mem-obj-tracking-info).

Withdrawal reaches later consumers only after the relevant store changes succeed. Missing children create durable cleanup work; GC launches delete operations, while failed child deletions can leave tombstones for later retry. The PostgreSQL adapter issues key-based DELETE commands, so successful application removes candidates from subsequent SQL selection. Default root-update error swallowing and explicit-drop propagation differ, as supplied by runtime and confirmed in the GC body. Deleting tracking state alone is not proof that all external content disappeared. SRC-1: `rust/core/src/engine/execution.rs`, `python/cocoindex/connectors/postgres/_target.py`; [RT-RTE-drop-app](runtime.md#rt-rte-drop-app).

Preview is a proposal display, not per-content approval or provider isolation; it does not install planned target actions. Other direct effects can still occur, so it is not a universal rejection/rollback gate. Relevant tests specify repeated reuse/state and rejection behavior but were not executed here. No source result in this report establishes retrieval quality, supported extraction accuracy, or outcome-driven admission of a better policy. [RT-RTE-preview-update](runtime.md#rt-rte-preview-update); SRC-1: `python/tests/core/test_use_state.py`, `rust/core/src/engine/component.rs`.

## Read-back

There are four distinct consumer classes, not one memory injection mechanism:

- **Execution consumers:** component/function probes select by identity/dependency validity and substitute a retained return; persistent user state is keyed access. These are fixed-rule symbolic operations even when a retained payload contains a vector or text. [MEM-RTE-function-reuse](#mem-rte-function-reuse), [MEM-RTE-state-access](#mem-rte-state-access).
- **Semantic search recipients:** explicit queries select retained text by numerical rank, then print it. Session search returns bounded snippets, not complete transcripts; metadata rows have no shown consumer in that query. [RT-RTE-query-index](runtime.md#rt-rte-query-index), [MEM-RTE-session-search](#mem-rte-session-search).
- **Service/alternate search clients:** shipped HTTP handlers return selected filename/score payloads; a separate CLI combines lexical and semantic ranks over filings. Availability of a retained vector does not imply that the image itself or a model explanation crossed the response channel. [MEM-RTE-alternate-search](#mem-rte-alternate-search).
- **Diagnostics:** explicit inspection delivers readable access/ownership summaries, not every opaque return payload. The presence of a readable processor name, fingerprint or memo flag is not equivalent to readable memory content. [MEM-RTE-inspect-state](#mem-rte-inspect-state).

Live watchers push source changes into maintenance, but this is not unsolicited context injection into an agent. The inspected semantic retrieval remains query-requested. No additional automatic model-context selector, agent frame isolation, conversation trimming or host-summary reload is established in these paths. This is a bounded coverage limit, not a repository-wide absence. Imported `context.md` remains externally produced content; no alternative host checkpoint payload was inspected that would justify calling it a complete restorable state. SRC-1: `examples/entire_session_search/main.py`; [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance).

## Integration issues

- **No correction to a supplied fact is required by these reads.** In particular, executable vector-index declaration confirms runtime's warning about stale text-example comments. SRC-1: `examples/text_embedding/main.py`; [RT-RTE-query-index](runtime.md#rt-rte-query-index).
- **Potential identity overlap:** [MEM-OBJ-tracking-info](#mem-obj-tracking-info) is a broad bookkeeping envelope that relates to the supplied memo object. Do not supersede [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization): the latter owns the cache-return referent; the former adds ownership/stage/child-recovery material. FunctionMemoizationEntry is a separate schema type, not a renamed component memo. SRC-1: `rust/core/src/state/db_schema.rs`, `rust/core/src/state_store/submit_session.rs`; [MEM-OBJ-function-memoization](#mem-obj-function-memoization).
- **Imported checkpoint uncertainty:** upstream creation and factual reliability of context/metadata are unresolved. This prevents a compaction-generation, reason-preservation or host-resumption claim, but not the implemented parse-to-search finding. [MEM-OBJ-session-embedding](#mem-obj-session-embedding), [MEM-OBJ-session-metadata](#mem-obj-session-metadata), [MEM-RTE-session-search](#mem-rte-session-search).
- **Consumer gaps:** manual extraction rows, patient JSON and session metadata have known writes but no independently inspected later content consumer. Do not promote storage to an answering-agent route. Other graphs, summaries, Rust examples and alternate connectors remain included/uninspected as listed in coverage. [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), [MEM-OBJ-session-metadata](#mem-obj-session-metadata); SRC-1: `examples/patient_intake_extraction_dspy/main.py`.
- **Alternate-search scope:** image API delivery is established, but full image model fixity, multivector selection details and every producer's retirement behavior remain unresolved. Filing search ranks are inspectable, while producer lineage was not traced. These facts prevent a uniform all-index freshness or numerical-form assessment. [MEM-RTE-alternate-search](#mem-rte-alternate-search).
- **Human control and failure boundary:** arbitrary user-state caller control and connector-specific recovery are not established by the generic APIs. Neither operator startup nor successful internal commit proves content approval or external-store rollback. [MEM-RTE-state-access](#mem-rte-state-access), [MEM-OBJ-tracking-info](#mem-obj-tracking-info).

## Limitations and checks

All claims are bounded to SRC-1 at 1639793b3602408a9cb220728fb30e306d433473. HEAD and clean status were checked directly. Required invocation, type, boundary/runtime, collection and worker/record contracts were read completely, including the supplied bounded ranges. Source evidence is implementation plus explicitly labelled documentation/test specification; no target code, provider, database, test or example was executed. Available uninspected source is not an access failure or an evidenced absence. No causal benefit, observed activation, complete connector audit or model-answer memory effect is established.

Deterministic validation: `commonplace-run validate-output` passed for this invocation after disambiguating the async function-cache quotation with the validator-supplied source range. Validation tests structure and quotation occurrence, not factual correctness, execution success or acceptance by reconciliation.
