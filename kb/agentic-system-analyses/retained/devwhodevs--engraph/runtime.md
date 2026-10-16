---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Engraph runtime baseline: shipped retrieval, vault admission, maintenance and server controls at f9a95bc96accc792c02ee384d9e6bf768a88c8c8."
run-id: AAS-2026-10-14-engraph-0cd4f00695b0-01
reviewed-boundary: f9a95bc96accc792c02ee384d9e6bf768a88c8c8
---

# Engraph runtime report

## Runtime account

### Work, entry paths and evidence

Engraph turns a Markdown vault into searchable retained context. Its own runtime retrieves and transforms information; an external agent decides when to invoke tools and what to do with their results. The external conversation loop is not attributed to Engraph. The frozen whole-system scope and sole source are established in [boundary](boundary.md#boundary-and-evidence). All findings below concern SRC-1 at the reviewed commit. They establish inspected implementation or declared design, not executed behavior, retrieval accuracy, latency, agent compliance or benefit. No target, tests or examples were executed.

The shipped CLI dispatches index, search, context, identity, setup/configuration, write and migration commands. `serve` opens the saved index, resolves its vault path, loads local models, starts a watcher and serves MCP over stdio; optional HTTP shares the same store, models and vault. The library exposes the same underlying operations. Those are alternate callers within the system, not independent enclosing agents (SRC-1, `src/main.rs`, `src/serve.rs`, `src/lib.rs`). The skill recommends indexing, search, graph inspection and budgeted context; its `allowed-tools` declaration belongs to the external client's permission interpretation, not to a Rust sandbox (SRC-1, `skills/engraph/SKILL.md`).

This inspection adds implementation coverage of model loading/inference and orchestration prompts (`src/llm.rs`), HTTP authorization and mutating endpoints (`src/http.rs`), setup application (`src/onboarding.rs`), context assembly (`src/context.rs`), write variants (`src/writer.rs`), watcher startup/changed-file consumption (`src/watcher.rs`), per-file indexing (`src/indexer.rs`), migration preview/application/undo (`src/migrate.rs`), placement strategy selection (`src/placement.rs`), config defaults and persistence (`src/config.rs`), and orchestration cache access (`src/store.rs`). It also reads the release workflow and CI declarations as doctrine/design (`.github/workflows/release.yml`, `.github/workflows/ci.yml`). Supporting internals beyond these selected paths remain available but uninspected; this is not a source-access gap.

### One ordinary invocation, end to end

For an ordinary MCP search, the principal is the connected MCP client. It submits query text and optional `top_n`; Engraph does not authenticate a person on the stdio path. Startup requires `engraph.db` with saved `vault_path` and a loadable embedding model. The server loads optional orchestration and reranking models when intelligence is enabled; individual load failures disable those enhancements rather than the mandatory embedder (SRC-1, `src/serve.rs`, `src/config.rs`).

The handler locks Store, embedder, and any optional model objects, then calls the search implementation. Code owns the next step throughout. Query orchestration is either a cached JSON result, local generated intent/expansions/date range, or a heuristic result. The generated route supplies the query in a user message and a fixed analyzer prompt in a system message; it greedily generates at most 256 tokens and falls back on generation or JSON-parse failure. The weights used for retrieval are symbolic code selected by intent, not weights learned during the invocation. See [RT-RTE-query-search](#rt-rte-query-search), [RT-CMP-llama-embed](#rt-cmp-llama-embed), [RT-CMP-llama-orchestrator](#rt-cmp-llama-orchestrator) and [RT-CMP-llama-rerank](#rt-cmp-llama-rerank).

Each expansion gets an embedding and vector retrieval plus full-text retrieval. Best hits are grouped by file and deduplicated across expansions. Graph expansion uses combined seeds; a requested date range adds dated-file seeds. Reciprocal-rank fusion combines the lanes. Optional reranking scores only up to 30 pass-one candidates using the original query and candidate snippet. Temporal scoring applies to dated candidates when applicable. The final return takes `top_n` and includes paths, IDs, scores, confidence, headings and snippets; MCP serializes only the results, not the whole internal fusion explanation. This is delivery to the client, not a completed conversational answer (SRC-1, `src/serve.rs`, `src/search.rs`).

Recovery differs by failure point. Mandatory query embedding/vector errors propagate; FTS and graph failures can become empty lanes, rerank errors become zero scores, and concrete orchestration falls back to heuristics. Therefore successful return does not guarantee all advertised lanes participated. Mutexes coordinate in-process adapters and watcher consumers; they do not serialize arbitrary external file editors or separate CLI processes. The client owns any subsequent read or answer and must preserve result references if it wants more context (SRC-1, `src/search.rs`, `src/serve.rs`, `src/watcher.rs`).

### Selected forcing routes and guarantee boundaries

Four source-supported forcing cases bound the account.

1. **Intelligence absent or failed versus full search.** CLI search and the server's search handlers can use optional models. Topic context instead calls `search_internal`, which constructs search configuration without those models. A claim that all context consumption uses model orchestration/reranking is false. The returned context also rereads current disk bodies rather than returning only indexed snippets; stale index selection can therefore lead to current content. [RT-RTE-topic-context](#rt-rte-topic-context) retains the actual selector and trimming behavior (SRC-1, `src/search.rs`, `src/context.rs`, `src/serve.rs`).
2. **Read-only service versus setup and index mutation.** Ordinary content-write handlers check read-only before calling the writer, but setup apply and explicit reindex have no such guard in either adapter. Startup cleanup and watcher reconciliation are also independent of read-only. Thus read-only blocks selected note-edit operations, not all persistent-state mutation. HTTP additionally requires a write key for setup/reindex; MCP has no corresponding bearer layer. [RT-CLM-server-readonly](#rt-clm-server-readonly), [RT-RTE-http-access](#rt-rte-http-access), [RT-RTE-setup-apply](#rt-rte-setup-apply) and [RT-RTE-index-refresh](#rt-rte-index-refresh) capture the boundaries (SRC-1, `src/serve.rs`, `src/http.rs`, `src/onboarding.rs`, `src/watcher.rs`).
3. **Create transaction versus filesystem and alternate writes.** Create/append precompute embeddings, change database entries transactionally, commit, and only then rename the temporary file. A failure after commit can leave database/disk disagreement. Startup removes temporary files and orphan rows and runs reconciliation; that is recovery machinery, not a cross-resource atomic invariant. Section edit and rewrite instead atomically replace disk content and update mtime without reindexing inside those writer functions. Move deletes old vectors/FTS/edges and inserts a new file record without recreating chunks before renaming. These paths cannot inherit create's indexing guarantee merely because they return a write result (SRC-1, `src/writer.rs`, `src/serve.rs`). See [RT-RTE-note-admission](#rt-rte-note-admission) and [RT-CLM-write-consistency](#rt-clm-write-consistency).
4. **Vault path label versus actual effect boundary.** Create accepts an explicit folder, forms a relative-path string and joins it to `vault_path`; move likewise joins a caller-provided folder, and explicit reindex joins a caller-provided file. The inspected operations do not canonicalize and verify containment before those I/O calls. Absolute folders or parent components therefore defeat a vault-contained interpretation at the source level, subject to OS permissions. No exploit execution is claimed. This prevents treating a vault root, bearer authentication or read-only setting as deployed filesystem isolation (SRC-1, `src/writer.rs`, `src/serve.rs`, `src/http.rs`).

The capability surface includes search/read/context and note/metadata editing, move/archive/delete, setup and reindex. Actual grants depend on the launched mode, configured HTTP keys and external client tool grants, none of which were captured from a deployment. HTTP defaults to disabled and loopback when enabled; `--no-auth` is rejected with a non-127.0.0.1 host in the shipped server entry path. The HTTP layer authorizes operations, not semantic content or filesystem containment. It exposes discovery/health-check routes without authorization. Direct library calls, CLI operations, watcher writes and stdio MCP do not pass through HTTP authorization (SRC-1, `src/config.rs`, `src/http.rs`, `src/serve.rs`, `src/main.rs`). External isolation, tunnel behavior and host scheduling remain unobserved.

### Change admission and limits

Knowledge admission is caller-authored content plus code-controlled tag resolution, link insertion, frontmatter merging and placement. Exact-name/alias and sufficiently confident fuzzy links can be applied automatically; other suggestions return to the caller. An explicit folder bypasses automatic placement. Otherwise type rules, semantic folder centroids and inbox fallback decide placement. Initiating a write is not evidence of a human approving the transformed content. `created_by` values such as `claude-code`, `cli` and `http-api` are adapter labels, not authenticated authorship (SRC-1, `src/writer.rs`, `src/placement.rs`, `src/main.rs`, `src/serve.rs`, `src/http.rs`). Memory-specific revision mechanisms and placement corrections are left to the memory member rather than inferred from the existence of centroids.

Setup persists identity/configuration, detects and writes a vault profile, indexes and extracts dynamic identity facts. Migration proposes heuristic classifications in saved preview files, then a separate application request moves eligible notes; undo uses a stored migration log. These admission routes have software decisions and caller veto opportunities, not answer oracles proving the correctness of content or placement. See [RT-RTE-setup-apply](#rt-rte-setup-apply) and [RT-RTE-para-migration](#rt-rte-para-migration).

Product changes use repository edits and build/release workflows, not the query loop. CI declares formatting, clippy and library tests for pushes/PRs; tagged releases build archives and update a Homebrew formula through a secret-bearing job. Source contains no workflow result here, so checks and release success are unobserved. The workflow declaration does not itself establish branch-protection or a mandatory CI admission gate (SRC-1, `.github/workflows/ci.yml`, `.github/workflows/release.yml`). Model replacement occurs through configured model URIs or local files and restart/loading, not inspected online parameter training. [RT-RTE-product-release](#rt-rte-product-release) describes that separate plane.

The optional Obsidian helper supports fixed subprocess commands, process-availability checks, a three-second timeout and circuit cooldown; this is not arbitrary shell execution. Its presence does not establish a live delegation route: inspected `edit_note` receives but ignores `_obsidian`, and inspected callers operate through writer functions. Other activation is uninspected, not claimed absent (SRC-1, `src/obsidian.rs`, `src/writer.rs`). No external worker or model-native tool execution was observed. Static agent setup instructions can shape the external client's use of Engraph, but their delivery/compliance is not evidence of internal autonomous theory revision; see [RT-BAP-agent-skill](#rt-bap-agent-skill).

## Shared records

### Components

#### RT-CMP-llama-embed
Label: LlamaEmbed

Source-native `LlamaEmbed` holds a local llama.cpp `LlamaModel`, tokenizer, target dimension and prompt format. Distributed-parametric weights reside in a cached GGUF file under the models directory and the loaded model object. Default URI names embeddinggemma-300M-Q8_0; config may override it. Document/query formatting differs. Inference creates a per-call context, mean-pooled vectors are truncated to target dimension 256 and L2-normalized (SRC-1, `src/llm.rs`).

Parameters changing during operation: inspected inference performs encode, not a parameter update; external file replacement is outside the inference call. Exact version pinned: no immutable weight revision or checked digest in this loading route. Mutable endpoint can resolve to another model: yes, fresh acquisition uses `resolve/main`; existing cache files are reused. llama.cpp internals and actual model bytes are uninspected. This mutability finding also applies separately to the following two components through their own calls to `ensure_model`.

> download_model(&uri.download_url(), &path, None)?;
> --- `src/llm.rs`

#### RT-CMP-llama-orchestrator
Label: LlamaOrchestrator

Source-native `LlamaOrchestrator` holds local distributed-parametric GGUF weights in a loaded `LlamaModel`; default is Qwen3-0.6B-Q8_0, configurable through `models.expand`. The model supplies query intent, expansions and optional dates under a natural-language analyzer prompt, with JSON parsing and heuristic fallback as symbolic consumers. Per-call contexts and greedy decoding do not train parameters (SRC-1, `src/llm.rs`).

Parameters changing during operation: no update in inspected generation. Exact version pinned: no, URI/default names a file but not immutable bytes. Mutable endpoint can resolve to another model: yes, missing cache resolves through the shared `resolve/main` downloader; loaded weights are retained for that process. Provider/model internals and quality are uninspected.

> match self.generate(&prompt, 256) {
> --- `src/llm.rs`

#### RT-CMP-llama-rerank
Label: LlamaRerank

Source-native `LlamaRerank` is a local distributed-parametric cross-encoder, default Qwen3-Reranker-0.6B-Q8_0, configurable through `models.rerank`. Cached GGUF and loaded `LlamaModel` are its storage substrates. It forwards formatted query/document text and computes a softmax from Yes/No token logits. Search uses this as another ranked lane, not a reference-answer oracle (SRC-1, `src/llm.rs`, `src/search.rs`).

Parameters changing during operation: no training in inspected forward scoring. Exact version pinned: no immutable weight revision/digest in loading. Mutable endpoint can resolve to another model: yes, a fresh download uses shared `resolve/main`, while an existing file is reused. Weight contents and numerical correctness remain uninspected.

> let score = yes_exp / (yes_exp + no_exp);
> --- `src/llm.rs`

### Operative objects

#### RT-OBJ-search-config
Label: SearchConfig

Source-native `SearchConfig` is symbolic Rust current-invocation state: optional mutable model references, Store reference and rerank candidate limit. It is held in process memory, not retained between calls. It determines which enhanced lanes are available, while intent-selected `LaneWeights` determine their fusion contribution (SRC-1, `src/search.rs`, `src/serve.rs`). Distinct from persisted orchestration results below.

> rerank_candidates: 30,
> --- `src/serve.rs:383-403`

#### RT-OBJ-llm-cache
Label: llm_cache

Source-native `llm_cache` is persisted SQLite state in Store. JSON strings encode symbolic intent, expansions and dates consumed by retrieval; expansion text is subsequently interpreted by the embedder and full-text consumer. Query SHA256 is the lookup key. The cache stores a model label and timestamp, but the inspected getter selects only by query hash, not model identity or age. It is distinct from loaded weights and current search configuration (SRC-1, `src/store.rs`, `src/search.rs`). Memory inventory and revision implications belong to the memory member.

> .prepare("SELECT result FROM llm_cache WHERE query_hash = ?1")?;
> --- `src/store.rs`

### Routes

#### RT-RTE-query-search
Label: Query search

Endpoints: CLI or MCP/HTTP request → orchestration → embedding/FTS/graph → fusion/rerank/temporal → ranked result return. The caller chooses query/count; symbolic Rust code owns progression. Optional orchestrator proposes query variants; code parses them and selects intent-specific weights. Optional reranker scores candidate snippets; neither model supplies a known correct answer. Operating mode: open retrieval requests, not a bounded curriculum. Answer oracle: none in this inspected runtime route; relevance scores are model/code judgments (SRC-1, `src/main.rs`, `src/serve.rs`, `src/http.rs`, `src/search.rs`, `src/llm.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked file-level results with IDs, headings and snippets; CLI can also format explanations, while MCP returns the results array.
- Later read-back: Optional orchestration JSON is saved and retrieved on later same-query calls; indexed vault content is selected from previously persisted state.
- Delegated visibility: MCP/HTTP/CLI caller receives selected results, not the full database or model context; external client handling is uninspected.
- Selection predicate: Expanded-query vector and FTS results, combined graph seeds, optional dates, intent-dependent RRF weights and top_n; optional rerank evaluates up to 30 pass-one snippets.
- Invalidation or expiry: Inspected cache getter has no age/model predicate; index freshness depends on maintenance. Cache writes replace the same hash. Other cache deletion paths are uninspected.
- Activation or effect: Code consumes orchestration fields and scores to select/order return values; downstream agent behavior is unobserved.
- Evidence limits: Implementation only; no demonstrated lane quality, original-query preservation by every model output, deployment or answer benefit.

> None => llm::heuristic_orchestrate(query),
> --- `src/search.rs`

#### RT-RTE-topic-context
Label: Topic context

Endpoints: topic request and budget → basic internal search → reread disk bodies → selected/truncated bundle. Client proposes topic/budget; code selects and trims. `context_topic_with_search` does not pass optional orchestration/rerank models. State is index references plus current file contents; terminal output is a serializable `ContextBundle`. The consumer is the client, not an internal answer generator (SRC-1, `src/context.rs`, `src/search.rs`, `src/serve.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Topic, sections with path/docid/content, total_chars, budget_chars and truncated flag.
- Later read-back: Retained notes are read from disk after index selection; full-note read routes can retrieve omitted content by returned path/docid.
- Delegated visibility: Client receives only bundled sections; the library has no authority over the client's accumulated conversation window.
- Selection predicate: Top five basic search hits first, then one-hop neighbors of the top three, deduplicated by path; direct matches get remaining budget, related bodies at most budget/8.
- Invalidation or expiry: Bundle is current-call state; retained notes remain until changed or removed. Selection freshness depends on index refresh.
- Activation or effect: Code removes frontmatter and truncates bodies at UTF-8 boundaries before delivery; this changes supplied context, not evidence of client compliance.
- Evidence limits: Budget accounting uses string byte lengths despite character-oriented names; truncation markers are added after the available-body calculation, so this is not a strict total-byte cap. No captured client-window or answer effect.

> let search_output = crate::search::search_internal(topic, 5, params.store, embedder)?;
> --- `src/context.rs`

This working-context control is code-decided exclusion/trimming of external material before a tool return, not host compaction of old turns or an isolated agent frame. Omitted content remains on disk and reloadable; Engraph does not control whether the caller actually reloads it.

#### RT-RTE-http-access
Label: HTTP access control

Endpoints: request headers and configured keys → authorization/rate limit → endpoint handler. The host operator supplies key grants at launch; code matches Bearer keys and tests whether a requested operation is a write. Optional no-auth mode bypasses key/permission checks but still rate-limits. Discovery and liveness endpoints are separately public (SRC-1, `src/http.rs`, `src/config.rs`, `src/serve.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unauthorized/forbidden/rate-limit errors or permission to run the handler; authorized handlers return their own outputs.
- Later read-back: inapplicable — authorization itself admits no retained content; launched config supplies grants rather than use-derived read-back.
- Delegated visibility: HTTP client receives only handler/error output; the configured key identifies a grant, not a proven human author.
- Selection predicate: Exact configured key match; reads allowed for any recognized key, writes only when permissions equals write; configured per-key rate limit.
- Invalidation or expiry: HTTP config is captured into ApiState at startup; the inspected authorization function has no token-expiry predicate. Restart/config replacement changes the loaded grant set.
- Activation or effect: It prevents unauthorized HTTP handler dispatch for covered endpoints; it does not cover CLI, library, MCP, watcher or OS access.
- Evidence limits: No deployed keys, rate-limit exercise, TLS/tunnel envelope or network isolation were captured.

> permission == "write"
> --- `src/http.rs`

Guarantee owner: HTTP adapter. Enforcement point: `authorize` at protected handlers. Guarantee strength: policy. Required external contract: trusted process/config and appropriate binding/network protection; the shipped run_serve no-auth loopback restriction must be retained by callers. Current grants and deployment envelope: uninspected. This is neither per-content approval nor a complete filesystem boundary.

#### RT-RTE-note-admission
Label: Note admission

Endpoints: caller content/edit/move request → writer transformation → filesystem and/or Store mutation → result; later indexing may complete derived-state refresh. Caller proposes text or target; software decides tag/link/placement transformations. Explicit folders override placement. Human authorship or per-content approval is unresolved for generic clients. Operating mode: open write requests. Answer oracle: none; successful I/O and placement confidence do not establish knowledge correctness. Trigger is a tool/CLI/library invocation, not an internal autonomous knowledge-generation loop (SRC-1, `src/writer.rs`, `src/placement.rs`, `src/main.rs`, `src/serve.rs`, `src/http.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Create/append/move return path/docid/tags/placement or link information; section/rewrite operations return path and edit mode; failures return errors.
- Later read-back: Persisted Markdown reaches read/context; create/append also write derived search state immediately. Section edit/rewrite defer chunk reindexing beyond their writer functions; move removes old retrieval entries and inserts only a new file record.
- Delegated visibility: Caller receives result metadata and suggestions, not proof of human review or all transformed bytes; later readers can inspect the retained file.
- Selection predicate: Explicit target resolution for edits; create resolves tags, applies exact/alias or fuzzy links at confidence_bp >= 920 by default, then explicit folder or type/centroid/inbox placement.
- Invalidation or expiry: Overwrite/edit, archive/delete/move and index refresh affect future access. Append checks indexed versus disk mtime before proceeding, not after concurrent external modifications.
- Activation or effect: Code writes persistent files and derived entries; successful downstream retrieval and behavioral use remain unobserved.
- Evidence limits: Adapter author labels are not authenticated people; no per-content semantic approval, cross-resource atomicity or vault-containment guarantee follows from these paths.

Admission/rejection: guarded server note mutations can be vetoed by read-only, HTTP writes by key permission, duplicate create/move targets by collision checks, and append by its mtime comparison. Caller can omit a request or disable create auto-linking; initiated transformation is software admission. Rollback/recovery: pre-commit create/append failures roll back and remove temp files; post-commit rename failures require reconciliation. Disk edit/rewrite have no saved previous body in these functions. Guidance that shapes and persists in proposals consists of caller text plus symbolic tag/link/placement rules; retained Markdown/frontmatter and derived state persist, not a critique of those rules.

> let rel_path = format!("{}/{}", placement_result.folder, filename);
> let final_path = vault_path.join(&rel_path);
> --- `src/writer.rs`

#### RT-RTE-index-refresh
Label: Index refresh

Endpoints: CLI index, watcher startup/events or explicit reindex → shared/per-file indexer → Store search state and edges. Trigger/principal differs: caller for explicit paths, OS events and server code for watcher paths. Rust code owns progression; local embedding supplies numerical derived state. Per-file indexing parses tags/created_by/date, chunks with tokenizer counts, embeds, deletes old entries and inserts replacements. Watcher performs a second edge-building pass; failures log warnings rather than proving freshness (SRC-1, `src/indexer.rs`, `src/watcher.rs`, `src/serve.rs`, `src/http.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Explicit paths return counts/docid or errors; watcher logs processing and remains available for later batches.
- Later read-back: Changed index entries and edges feed later search/context and identity extraction; external file contents themselves persist independently.
- Delegated visibility: Clients see later selected state or explicit reindex output, not every watcher event or failed update.
- Selection predicate: Watcher filters configured exclusions and skips a recent tool write only when recorded mtime exactly matches; explicit reindex takes caller file path and does not invoke that watcher filter.
- Invalidation or expiry: Changed/deleted/moved events or rebuild replace/remove derived entries; startup reconciliation catches downtime changes. Errors can leave stale state.
- Activation or effect: Software admits filesystem content into retrieval structures without separate semantic approval; explicit reindex and watcher mutate state even under server read-only.
- Evidence limits: No run demonstrates event delivery, consistency or recovery; concurrent external writes and direct caller path control are outside the in-process mutex guarantee.

Admission: caller or filesystem supplies content; tokenizer/chunker/embedder/indexer transforms it. Operating mode: open synchronization, not an improvement experiment. Answer oracle: none. Rejection: exclusion rules on traversal/watch paths, unreadable files and indexing errors; no content-truth veto. Recovery: later events, explicit index/rebuild or startup reconciliation; atomic recovery of all error cases is not established.

> // Startup reconciliation: run index to catch changes since last shutdown
> --- `src/watcher.rs`

#### RT-RTE-setup-apply
Label: Setup apply

Endpoints: interactive/JSON CLI setup or MCP/HTTP setup apply → configuration/profile/index/identity-fact persistence → setup response. Caller proposes identity fields. Detection code builds a profile from the vault; apply saves supplied fields, writes profile, indexes and extracts facts. A detect request is a separate non-applying mode. HTTP requires write authorization; neither inspected setup handler checks server read-only (SRC-1, `src/onboarding.rs`, `src/serve.rs`, `src/http.rs`, `src/main.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON status, config path, completed steps, summaries/counts and next steps, or error.
- Later read-back: Config identity reaches identity requests; persisted profile reaches subsequently loaded placement/context resources; index/facts reach later retrieval and identity formatting.
- Delegated visibility: Client sees setup summaries; already loaded server profile/model/config objects are not all replaced by setup, so persistence does not guarantee immediate in-process reconfiguration.
- Selection predicate: ApplyFlags and supplied name/role/purpose determine edited fields; vault detection/indexing determine profile and facts.
- Invalidation or expiry: Later setup/config edits replace durable values; restarts reload captured server resources. No global expiry in the inspected apply procedure.
- Activation or effect: Saves config/profile and invokes indexing/fact extraction; later identity text delivery is wired, external agent effect unobserved.
- Evidence limits: No execution; intermediate completed writes can precede a later error. Generic client input leaves per-content human control unresolved.

Admission: caller chooses apply or abstains; software applies fields and detected profile without a second approval. Answer oracle: none. Operating mode: open setup/update. Rejection: bad mode, HTTP permissions and operational errors. Recovery: rerun or replace config/profile and reindex; no all-step transaction or built-in config rollback is established. Guidance is supplied identity text plus detection rules, retained as TOML/profile and extracted facts.

> config.save().context("saving identity to config")?;
> steps_completed.push("identity_saved".into());
> --- `src/onboarding.rs`

#### RT-RTE-para-migration
Label: PARA migration

Endpoints: preview generation → saved JSON/Markdown → explicit apply → file moves/log → optional undo. Code proposes categories using note content, path, metadata, recency and edges; uncertain candidates are separated from eligible files. Caller decides to apply or abstain, and can review the preview. Starting apply is not proof that a human reviewed each move. Operating mode: bounded migration batch, not a retrieval-quality experiment. Answer oracle: none; classification confidence is heuristic (SRC-1, `src/migrate.rs`, `src/main.rs`, `src/serve.rs`, `src/http.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Preview classifications or migration/undo ID, moved/restored counts and per-file errors.
- Later read-back: Saved JSON supplies a later apply; SQLite migration log supplies undo; moved paths affect subsequent vault reads and maintenance.
- Delegated visibility: Caller receives preview/results, while move_note handles filesystem/Store effects; external approval is not authenticated.
- Selection predicate: Apply iterates preview.files with suggested paths, skipping unchanged paths; uncertain candidates are not included by generator. Undo iterates recorded entries in reverse.
- Invalidation or expiry: Preview files can be replaced; undo targets last logged migration and deletes its log even when some restores fail.
- Activation or effect: Successful move_note calls change filesystem paths and Store records; consistent eventual search coverage depends on maintenance rather than immediate chunk recreation.
- Evidence limits: No exercised rollback, correct PARA classification, per-file review or migration-wide atomicity; partial errors are expressly returned.

Admission/rejection: explicit apply request admits preview moves, guarded by server write checks where present and target-collision checks; absent requests veto the batch. Recovery: undo attempts recorded reverse moves but is best effort, and its unconditional log deletion bounds retryability. Guidance is heuristic PARA classification and saved proposed destinations; proposed locations and migration history persist, not revised classifier theory.

> store.delete_migration(&migration_id)?;
> --- `src/migrate.rs`

#### RT-RTE-product-release
Label: Product release

Endpoints: repository change/push/PR → declared CI; version-tag push → release build/archive/upload and Homebrew update. Maintainers propose code/workflow changes and choose release tags; CI runs fixed checks. The release job possesses contents-write permission and a tap token for external publication. This is a product/production-machinery plane, distinct from vault writes (SRC-1, `.github/workflows/ci.yml`, `.github/workflows/release.yml`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Declared workflow check/build outcomes and archives if execution succeeds; no run artifacts were supplied.
- Later read-back: Published binary/source/formula can be installed by future users; installation and use are unobserved, and this is not runtime memory read-back.
- Delegated visibility: GitHub Actions receives repository state and configured credentials; tap implementation and deployment grants are outside the frozen source.
- Selection predicate: CI push/PR to main; release pushes tags matching v*; fixed platform matrices.
- Invalidation or expiry: Subsequent source/tag/formula updates change distribution; rollback/version retention policy is uninspected.
- Activation or effect: Workflow is wired to build and publish, not evidence that a changed product was installed or improved behavior.
- Evidence limits: No observed build/tests/release; branch protection, maintainer review/veto practices and external tap state are uninspected.

Admission/rejection: maintainers edit/push/tag; declared build failure can block dependent update-homebrew, but the release workflow has no explicit dependency on CI. CI formatting/clippy/library tests are software checks, not a semantic answer oracle. Guidance is fixed workflow YAML/build configuration; repository code and release artifacts persist. Recovery requires maintainer action; no automated release rollback in these declarations.

> needs: build
> --- `.github/workflows/release.yml`

### Claims

#### RT-CLM-server-readonly
Label: Server read-only

Claimed operation: read-only startup announces disabled write tools. Owner is the server adapters; enforcement is the explicit read_only tests on create/append/metadata/move/archive/edit/rewrite/frontmatter/migration apply/undo/delete and HTTP migration preview. Guarantee strength: policy. Covered paths do not call their writer when read-only; alternate setup apply, reindex, startup cleanup and watcher mutation remain wired. Direct CLI/library paths have no server flag. Required external contract: callers must not interpret the mode as a process/filesystem sandbox (SRC-1, `src/serve.rs`, `src/http.rs`, `src/main.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> eprintln!("Read-only mode: write tools disabled");
> --- `src/serve.rs`

The wording is broader than the inspected guard coverage. It does not guarantee unchanged config, profile, index or filesystem housekeeping. The setup and reindex witnesses above defeat that stronger interpretation.

#### RT-CLM-write-consistency
Label: Write consistency

Claimed operation: writer documentation calls create a pipeline and atomic_write an atomic rename. Owner is writer code; enforcement points are DB transaction, temp-file rename, append's initial mtime check and startup recovery. Guarantee strength: best effort for combined DB/filesystem consistency; the atomic rename concerns one file, subject to filesystem semantics, not the whole pipeline. Covered create/append DB failures attempt rollback; successful DB commit precedes rename. Edit/rewrite/move have materially different indexing and conflict coverage (SRC-1, `src/writer.rs`, `src/serve.rs`, `src/watcher.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Step 8: COMMIT
> store.commit()?;
> // Step 9: Atomic rename temp → final
> std::fs::rename(&temp_path, &final_path)?;
> --- `src/writer.rs`

Required external contract: reliable SQLite/filesystem operations and no conflicting external writers are needed for stronger consistency. No captured failure test supports crash-safe cross-resource atomicity. Startup repair is a recovery affordance, not evidence that all interrupted updates restore the requested content.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-query-analyzer
Label: Query analyzer prompt

Consumer: local LlamaOrchestrator. Channel: fixed natural-language ChatML system prompt plus caller query as user message. Force: requested classification/expansion; JSON parser and search consumers turn accepted fields into concrete retrieval selection. Horizon: each orchestration invocation; accepted cache can bypass regeneration on later same-query searches. The prompt is not edited by the inspected retrieval loop, and faithful inclusion of the original query is requested rather than proved for every generated output (SRC-1, `src/llm.rs`, `src/search.rs`).

> - "expansions": 2-4 alternative phrasings (always include the original query first)
> --- `src/llm.rs`

#### RT-BAP-agent-skill
Label: Agent-facing skill

Consumer: external agent/client loading the shipped Engraph skill. Channel: natural-language Markdown instructions, symbolic tool-grant declaration and client-interpreted status command. Force: guidance for when/how to index/search/context-query; actual tool permissions and compliance are supplied by the client, not enforced by Engraph. Horizon: client skill/session lifetime, unobserved. Static skill text is not use-derived retained memory. The repository supplies an invocation instruction, not proof that an agent follows it (SRC-1, `skills/engraph/SKILL.md`).

> allowed-tools: Bash(engraph:*), mcp__engraph__*
> --- `skills/engraph/SKILL.md`

## Annotations

none
