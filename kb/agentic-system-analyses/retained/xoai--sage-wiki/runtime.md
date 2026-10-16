---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Sage-wiki runtime baseline: capture, tiered compilation, retrieval and answer admission, with direct-write, provider and parser alternatives at the frozen commit."
run-id: AAS-2026-10-15-sage-wiki-cc43456fb833-01
reviewed-boundary: d3ef3a1346405c82eac01b4d7c493c94c1c59169
---

# Sage-wiki runtime report

## Runtime account

### Work and evidence boundary

Sage-wiki is a knowledge-state producer and consumer, not the enclosing agent's execution runtime. Code schedules model calls to summarize sources, extract concepts and relations, write articles, extract conversation knowledge and synthesize answers. External agents can instead supply finished content through tools. These are materially different admission paths: model compilation is not a compulsory gate on every retained article. SRC-1: `internal/compiler/fullpipeline.go`, `internal/mcp/tools_write.go`, `internal/query/query.go`.

All findings below concern implementation or attributed design at the boundary's frozen commit. No target command, test, example, provider or remote service was executed. No supplied execution trace or causal experiment establishes actual activation, operational reliability or benefit. A successful-looking source branch is not an observed run. The read-only checkout supplies evidence, not the deployed workspace's credentials, model identities, parser grants or host isolation.

Additional SRC-1 coverage beyond the boundary's initial inspection includes implementation in `internal/compiler/write.go`, `internal/compiler/worker_cycle.go`, `internal/compiler/ondemand.go`, `internal/compiler/evidence_gate.go`, `internal/trust/predicate.go`, `internal/extract/external.go`, `internal/extract/sandbox_linux.go`, `internal/llm/client.go`, `internal/llm/injected.go`, `internal/embed/embed.go`, `internal/prompts/prompts.go`, `internal/prompts/untrusted.go`, `internal/pack/merge.go`, `internal/hub/search.go`, `internal/mirror/hydrate.go`, `internal/serve/auth.go`, `internal/skill/skill.go` and `internal/skill/writer.go`. These are implementation/design evidence, not new sources or observed operation.

### Entry paths and ordinary invocation

An ordinary shipped CLI question enters `runQuery`: it joins question arguments, opens a mutable engine workspace to acquire the single-writer lock, refuses an unadopted old format, calls `query.Query`, prints the answer and optionally its filed path. The lock is significant because question answering writes knowledge, not just reads it. SRC-1: `cmd/sage-wiki/main.go`.

> // SPEC-01: query auto-files its answer (a workspace mutation), so it
> // takes the engine's single-writer lock and fails fast during an
> // active compile (spec §B.1 8e).
> --- `cmd/sage-wiki/main.go`

[RT-RTE-query-answer](#rt-rte-query-answer) traces this invocation. Code loads workspace configuration and a database, selects articles through hybrid search and optional graph expansion, truncates and filters assembled context, then issues one synthesis call. The model proposes prose, not the next runtime action. Code rejects an empty synchronous response and calls the configured filing route. The terminal product is an answer with source metadata and, when filing succeeds, a durable output. If retrieval supplies no context, code returns a fixed no-results answer without synthesis or filing. Synthesis success and filing success are distinct.

Shipped alternatives are not all REST aliases. MCP registers read, write and compound tools; `wiki_query` invokes the same synchronous Q&A code with the server database. Standalone MCP has stdio and loopback SSE transports. REST routes include capture, search, queued compile, graph, document read, export, jobs, metrics and events; its capture endpoint dispatches to MCP capture. Browser/terminal streaming uses a separate `StreamQuery` implementation. Embedded Go exposes `Workspace.Capture`, `Compile`, `Search` and graph operations; the CLI explicitly notes that this engine surface does not expose Q&A. Python/TypeScript clients and examples are callers, not a second model scheduler. SRC-1: `internal/mcp/server.go`, `internal/mcp/tools_compound.go`, `internal/serve/server.go`, `internal/query/query.go`, `pkg/engine/methods.go`, `cmd/sage-wiki/main.go`; caller scope is established in `boundary.md`.

Production before a question commonly follows [RT-RTE-capture-source](#rt-rte-capture-source) or [RT-RTE-capture-knowledge](#rt-rte-capture-knowledge), then [RT-RTE-compile-sources](#rt-rte-compile-sources). The latter loads configuration, prompts and manifest, diffs sources and classifies compile-key drift before the no-work fast path. Code selects tiers and claims queue items. Tier 0 indexes text; tier 1 adds embeddings/chunks; tier 3 runs summarize → extract → write. Optional triple extraction, entity resolution and communities extend that graph-producing pipeline. A per-pass model does not receive the whole caller conversation by default. Its inputs are rendered source/summary/concept/article data chosen by code. SRC-1: `internal/compiler/pipeline.go`, `internal/compiler/fullpipeline.go`.

### Owners, context and change admission

| Loop | Principal and next-step owner | Decision policy and context | Durable effects and return |
|---|---|---|---|
| Capture and compile | CLI/API/tool caller supplies content or source identity; Go code owns progression; model supplies extracted/generated candidates | Configured source tiers, diff/compile keys, queue claims, rendered templates; code filters and persists results | Raw files, compiled markdown, manifest, entries/chunks/vectors/ontology and queue state; IDs, counters, paths and errors |
| Query and file | Human or agent caller asks; Go code selects context and calls synthesis; trust code or unrestricted branch admits output | Hybrid retrieval, graph expansion, inclusion mode, approximate context budget; no per-answer expected-answer oracle | Answer returned; pending or indexed output persists; later queries can consume permitted outputs |
| Direct write and scribe | Tool caller supplies article/learning, or CLI caller supplies transcript; code applies structural checks | Direct writes bypass compile generation; scribe model selects entity candidates and code compares definitions | Article/index/manifest changes, stored learnings or ontology updates; acknowledgements/counters |
| Extension and restoration | Caller chooses pack, configuration/provider injection or remote restore | Code validates pack paths/config and restore preconditions; parser execution needs an explicit grant | Prompts, skills, config, parser files, or restored workspace state; result/report or error |

These summaries are expanded in the route records, including selection, expiry, recovery and admission roles. Initiating an operation does not establish a human's per-content approval. Generic CLI/tool identities do not resolve whether the caller is human or computational.

Model components are [RT-CMP-llm-client](#rt-cmp-llm-client) and [RT-CMP-embedder](#rt-cmp-embedder). Symbolic scheduling and grants reside in [RT-OBJ-config](#rt-obj-config) and [RT-OBJ-compile-items](#rt-obj-compile-items); natural-language proposal guidance resides in [RT-OBJ-prompts](#rt-obj-prompts). [RT-RTE-apply-pack](#rt-rte-apply-pack) admits instruction and capability changes without rebuilding the binary. [RT-BAP-generated-skill](#rt-bap-generated-skill) reaches external agent instruction files, but their loading and authority are a host contract, not something Sage-wiki enforces.

Working-context control is primarily *selection before each independent completion*, not a managed chat transcript with eviction and reload. Q&A retains selected article prefixes in its call, leaves other files outside the window and reachable by later search/read, and omits material by trust predicates, deduplication, count limits and approximate budgets. Article writing receives source sections, an existing article and related concepts. Scribing removes thinking/tool material before extraction and retains selected user/assistant text. A frame analogy fits these separate calls: chosen inputs enter; content/candidates return; the internal provider context does not become a caller agent frame. It breaks where durable files and ontology updates outlive a call and can be selected again, and because the excluded host owns its own history/compaction. SRC-1: `internal/query/query.go`, `internal/compiler/write.go`, `internal/scribe/session.go`.

### Forcing cases and guarantee boundaries

Four source-supported forcing cases bound the important assurances. Implementation conclusion status for this inspection is **wired**; operation conclusion status is **uninspected** for each case.

1. **Retrieval does not deliver every selected chunk verbatim.** Enhanced search supplies document IDs, but Q&A rereads article files and takes prefixes up to 16,000 bytes per article, estimating tokens as bytes/4. If the next article would exceed the budget, that loop breaks. Graph-related and neighbor files then have their own iteration under the remaining budget. Chunk IDs returned for trust scoring are collected before this assembly, so they are not proof that every identified chunk reached synthesis. If the chunk index is empty or enhanced search fails/has no hits, document-level hybrid retrieval is an alternate. This is a code-owned **best effort** context-size control, not an exact tokenizer or completeness guarantee. Required external contract: accessible article files and compatible retrieval stores. SRC-1: `internal/query/query.go`.

2. **Output review is neither universal knowledge review nor a single atomic publication gate.** The shared predicate covers `output:` identities; non-output documents always pass. Explicit unrestricted mode files/indexes answers directly. Manual article tools and scribing are alternate admissions. Even on the reviewed path, `PromoteOutput` indexes before its final state change, but automatic consensus code can set `state = 'confirmed'` inside the earlier transaction before post-transaction promotion/indexing. Thus the advertised ordering is not a global invariant. See [RT-RTE-admit-output](#rt-rte-admit-output). Predicate owner: trust package; enforcement: search/context consumers that call it; strength: **policy**. Required external contract: accurate identity/state, durable stores and correct caller use. SRC-1: `internal/trust/predicate.go`, `internal/trust/promote.go`, `internal/trust/hooks.go`, `internal/mcp/tools_write.go`.

3. **Parser opt-in is not sandbox isolation.** The full pipeline and tier orchestration load project parser commands when external parsers are enabled and trusted. `ExternalRegistry.Parse` also gates execution; on inspected Linux code, `canSandbox` returns false. Execution uses a temporary directory, reduced environment, timeout and process-group kill, but no filesystem/network namespace isolation. A granted parser can execute host code; a model's prose does not itself receive this subprocess interface. Capability surface: configured commands and arguments; current grant set: unknown workspace configuration; deployed envelope: unknown OS/container permissions. See [RT-RTE-run-parser](#rt-rte-run-parser). Owner: parser/config code; enforcement: loading and Parse; strength: **policy**, not deployment guarantee. SRC-1: `internal/compiler/pipeline.go`, `internal/compiler/fullpipeline.go`, `internal/extract/external.go`, `internal/extract/sandbox_linux.go`.

4. **Provider injection and cost controls have separate contracts.** `WithProvider` supplies search embeddings only; `WithCompileProvider` separately replaces compile completions. Injected completion bypasses HTTP formatting/retry code, leaving retries/rate limits/temperature to caller code. Model/version pinning cannot be inferred from either interface. The standard full-pipeline budget check compares known tracked cost between passes; unknown cost never trips it, and a pass can overshoot before its next check. On-demand `FullPipelineOpts` in the inspected path does not pass MaxCost/Tracker; batch mode has separate submission/resumption. Therefore a strict system-wide spend ceiling is not established. Owner: compiler/client and caller provider; enforcement: pass boundary and provider adapter; strength: **best effort**. Required external contract: accurate usage/pricing and cooperative context cancellation by custom code. SRC-1: `pkg/engine/engine.go`, `internal/llm/injected.go`, `internal/compiler/fullpipeline.go`, `internal/compiler/ondemand.go`, `internal/compiler/pipeline.go`.

HTTP bearer authentication is another path-local control, not a universal tool permission system. The HTTP middleware accepts a valid configured token (Authorization or query token), exempts health/readiness, and admits all routes when no tokens are configured. `CheckRefusal` rejects non-loopback binding without tokens unless explicitly overridden. Standalone MCP stdio, loopback SSE, direct Go calls and local CLI do not traverse this middleware. All read/write/compound tools are registered by the inspected MCP constructor. Nothing in those inspected registrations demonstrates content-specific human approvals or role-scoped tool grants. Guarantee owner: HTTP server; enforcement: bind check/middleware; strength: **policy**; implementation conclusion status: **wired**; operation conclusion status: **uninspected**. Transport security and OS access control remain deployment contracts. SRC-1: `internal/serve/auth.go`, `internal/mcp/server.go`.

Prompt framing is a request to the model, not an execution isolation boundary. The canonical wrapper neutralizes literal delimiter tags and labels source text as data. Its own comments identify unwrapped existing-article/learning sections and metric-judge prompts. Workspace prompt overrides are another path that can change the framing. Consequently model resistance to injected instructions remains unobserved, not an invariant of compilation or Q&A. Owner: prompt builders; enforcement: string construction; strength: **best effort**. SRC-1: `internal/prompts/untrusted.go`, `internal/prompts/prompts.go`, `internal/compiler/write.go`.

> // a whitespace-tolerant model may still read it as the tag — neutralization
> // raises the bar, it does not close it (see spec Non-goals).
> --- `internal/prompts/untrusted.go`

### Persistence, coordination and limits

Compilation uses persistent queue claims, worker tokens, leases and heartbeats; CLI runs as an in-process worker. The server worker scans diffs and claims tiers 0/1/3; on-demand compilation selects matching unfinished sources, promotes them to tier 3 and uses a coordinator. The serve job runner refuses a conflicting compile, while on-demand compilation can wait and return an indexed-sources-only message on timeout. These are code-owned scheduling protocols, not evidence of successful crash recovery. SRC-1: `internal/compiler/pipeline.go`, `internal/compiler/worker_cycle.go`, `internal/compiler/ondemand.go`, `internal/serve/deps.go`.

Write-then-index-then-manifest ordering is not a cross-file/database transaction. Article files are written atomically, while many subsequent index errors log and continue. Interrupted tier-3 work suppresses pass advances/manifest save so later diff processing can retry; already-written files/index effects need not disappear. Quality retry explicitly deletes an article before rewriting and can leave its file absent if rewriting fails. Thus retryability is narrower than rollback. Event brackets, per-pass usage recording, error counters, quality scores and logs expose state, but neither their presence nor the source comments establish repaired consistency in operation. SRC-1: `internal/compiler/write.go`, `internal/compiler/fullpipeline.go`, `internal/compiler/pipeline.go`, `internal/mcp/tools_write.go`.

> // failure fails the article; store-mutation failures log and continue.
> --- `internal/compiler/write.go`

Durable variants remain included. Federated search queries multiple project stores and filters output identities using each project's trust state. Mirror hydration admits a selected remote generation into an empty destination, with an explicit partial-resume exception and verification/decryption gates. These are alternate delivery/recovery paths, not autonomous knowledge validation. Deep WAL replay, remote-object concurrency, PostgreSQL behavior, browser rendering, all parser platforms, every batch provider and evaluator correctness were not fully inspected here. They remain available evidence, not evidenced absences; no end-to-end durability, isolation, benchmark benefit or complete adapter equivalence is concluded. SRC-1: `internal/hub/search.go`, `internal/mirror/hydrate.go`; evaluator/caller limits in `boundary.md`.

## Shared records

### Components

#### RT-CMP-llm-client
Label: LLM client and completion provider

Source-native identity: `llm.Client`, including config-built HTTP providers and the injected completion adapter. The active model is distributed-parametric content held by an external provider or caller implementation; messages/options and adapter rules are symbolic, while message bodies carry natural-language guidance/data. Model weights are not stored in Sage-wiki's inspected client. SRC-1: `internal/llm/client.go`, `internal/llm/injected.go`, `pkg/provider/provider.go`.

Parameters changing during operation: uninspected inside external providers; the inspected API requests inference and exposes no weight-update operation. Exact version pinned: no implementation-enforced immutable weight identity; model strings come from configuration, defaults or the provider response. Mutable endpoint resolving to another model: afforded by configured service/base URL and arbitrary caller implementation; actual endpoint behavior is uninspected. Compile, capture, scribe and query can select different configured models. A single global fixed-model conclusion is unwarranted.

> Complete(ctx context.Context, req CompleteRequest) (*CompleteResponse, error)
> --- `pkg/provider/provider.go`

The provider surface returns content and usage, not a Sage-wiki action plan or tool-call execution loop. Custom callback internals can do more, but are outside the frozen implementation. Their retries, side effects and parameter behavior are not inherited from the default HTTP adapter.

#### RT-CMP-embedder
Label: Embedding provider

Source-native identity: `embed.Embedder`; configured cascade/override or the engine search provider adapter. Distributed-parametric model state is external; returned dense float vectors are numerical representations retained by vector stores. Text/model names and request routing are separate symbolic/natural-language parts. SRC-1: `internal/embed/embed.go`, `pkg/engine/search.go`, `pkg/provider/provider.go`.

Parameters changing during operation: provider-internal, uninspected; inspected calls request vectors, not training. Exact version pinned: not enforced; default labels such as `text-embedding-3-small` and configuration overrides are names, not frozen weight hashes. A mutable service or caller callback can resolve to another implementation/model. Whether a particular deployment does so is uninspected. Persisting a vector changes retained representations without demonstrating changed model parameters.

> type Embedder interface {
> Embed(text string) ([]float32, error)
> Dimensions() int
> Name() string
> }
> --- `internal/embed/embed.go`

### Operative objects

#### RT-OBJ-config
Label: Workspace config

Source-native identity: workspace `config.yaml` / `config.Config`. Symbolic YAML fields select source roots, output paths, providers/models, prompts' surrounding operation, tiers, limits, trust inclusion and parser grants; substrate is the filesystem plus loaded Go configuration. Consumers include compiler, query, capture, pack application and server setup. Pack admission only allows selected top-level overlays; direct local configuration is a different authority path. SRC-1: `internal/compiler/pipeline.go`, `internal/query/query.go`, `internal/pack/merge.go`, `internal/extract/external.go`.

> "trust":        true,
> "type_signals": true,
> "ignore":       true,
> --- `internal/pack/merge.go`

#### RT-OBJ-prompts
Label: Prompt registry bodies

Source-native identity: embedded `internal/prompts/templates/*.txt` plus workspace `.md`/`.txt` overrides loaded into `prompts.Registry`. Operative bodies are natural-language proposal guidance; template parsing/substitution is a symbolic consumption mechanism, not another model. Filesystem and embedded binary templates are substrates; the loaded registry is current-process state. Missing override files fall back to defaults; successful load replaces templates/provenance together. Existing article/source material is selected separately by callers. SRC-1: `internal/prompts/prompts.go`, `internal/compiler/write.go`.

> // LoadFromDir merges user prompt templates from a directory into the
> // registry. Templates in the directory override embedded defaults by
> // filename. Falls back to embedded defaults for any template not found.
> --- `internal/prompts/prompts.go`

#### RT-OBJ-compile-items
Label: Compile items

Source-native identity: persistent `compile_items` through `store.CompileItemStore`. Symbolic database state records source paths, tiers, pass progress, compile keys, quality and queue claims. It is not model memory in the form of weights. CLI and background workers claim/release units, and on-demand code promotes selected rows. Source changes, invalidation and lease expiry influence later work. SRC-1: `internal/compiler/pipeline.go`, `internal/compiler/worker_cycle.go`, `internal/compiler/ondemand.go`.

> // Queue lifecycle (P2-3): the CLI is an in-process worker of one. It
> // requeues crashed leases, resets dead letters under --fresh, then
> // claims/processes/releases per tier with heartbeats, so a killed
> // compile leaves resumable queue state exactly like the server worker.
> --- `internal/compiler/pipeline.go`

This passage states the intended recovery protocol; operational crash recovery was not observed.

### Routes

#### RT-RTE-capture-source
Label: Engine source capture

Caller → `Workspace.Capture` → path/URL ingestion or reader-file persistence. Code owns validation and effects under the workspace mutex and mutability check. A reader source is a text surface, not model extraction. Exactly one of path, URL or reader must be supplied; the reader branch enforces bytes/encoding, sanitizes type, checks containment and writes frontmatter plus text to `raw/captures`. SRC-1: `pkg/engine/methods.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Document/source ID or validation/I/O error.
- Later read-back: Captured raw files are discoverable by later compiler source scans and later retrieval after indexing.
- Delegated visibility: No sub-agent invocation; path/URL helpers and file I/O execute under the calling process's authority.
- Selection predicate: Exactly one source variant; reader metadata and configured byte/encoding limits select admissible text.
- Invalidation or expiry: Persistent until changed/removed; later diff/hash processing can schedule changed content.
- Activation or effect: Writes source material and emits capture events when configured; effect on later model behavior is unobserved.
- Evidence limits: Reader branch directly inspected; path/URL delegate calls located, but their complete network/format/security behavior is not established here.

Admission: caller proposes bytes/source identity; code decides structural acceptance, with no per-content semantic approval. Human contribution is unresolved for a generic caller. Open capture requests, not a curriculum or answer-oracle comparison. Caller metadata shapes frontmatter; raw text persists. Rejection: mutability, exclusive-variant, size, encoding, name and containment checks. Recovery: write error returned; no semantic rollback operation is supplied in this route.

> return "", fmt.Errorf("engine: exactly one of Source.Path, Source.URL, Source.Reader must be set")
> --- `pkg/engine/methods.go`

#### RT-RTE-capture-knowledge
Label: MCP knowledge capture

Tool/REST caller → `handleCapture` → rendered capture template and structured completion → source-file writes → batched manifest mutation. Model proposes title/content items; Go validates them and persists without a human approval step. Configured summarize model is used, with a default fallback name. SRC-1: `internal/mcp/tools_write.go`, `internal/serve/server.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Captured item count/titles, no-items notice, error, or fallback raw-file acknowledgement.
- Later read-back: Item markdown under `raw/captures` enters later compile scans; failed extraction can retain raw content for later processing.
- Delegated visibility: Completion provider receives rendered guidance, caller context/tags and wrapped source content; no Sage-wiki sub-agent is spawned.
- Selection predicate: Nonempty content within capture-size/encoding constraints; decoded model items within batch cap and nonempty sanitized titles.
- Invalidation or expiry: Files and manifest persist; subsequent writes may replace same-slug paths, and later source diff can recompile changed files.
- Activation or effect: Knowledge candidates become raw sources; no proof of correct extraction or later behavioral activation.
- Evidence limits: No extraction execution; structured output and JSON decoding constrain form, not truth; failed file/manifest writes can produce partial persistence.

Admission: model proposes decomposed knowledge, code admits structurally; extraction failure takes a code-selected raw fallback. The caller may be human or agent. Open requests; no expected-answer oracle. Guidance asks for knowledge extraction via the loaded capture prompt, and the returned candidate prose persists in source files. Over-cap and invalid-title cases reject before item writes. File write failures log/continue; manifest failure leaves files discoverable by Diff. This is not a transaction over all item files.

> // Fallback: store raw content as single file
> --- `internal/mcp/tools_write.go`

#### RT-RTE-compile-sources
Label: Tiered source compilation

CLI/embedded call, MCP compound tool, REST job or background scan → compiler/worker queue → tier-specific processing → manifest/index/artifact updates. Code owns next steps and tier selection; models propose summaries, concepts, articles and optional graph material. SRC-1: `internal/compiler/pipeline.go`, `internal/compiler/fullpipeline.go`, `internal/compiler/worker_cycle.go`, `internal/compiler/ondemand.go`, `internal/serve/deps.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compile counts/errors/cost metadata or job handle/progress; on-demand returns matching article information or a compile-in-progress message.
- Later read-back: Compiled markdown/indexes feed later search and synthesis; compile keys/pass flags/quality and source hashes influence later work selection.
- Delegated visibility: Independent model calls receive selected source/summary/concept/existing-article context; providers do not acquire a general tool grant from those calls.
- Selection predicate: Diff plus drift/resume classification, configured tiers, queue leases and limits; on-demand searches matching unfinished sources and promotes them to tier 3.
- Invalidation or expiry: Source/removal and compile-key changes cause processing; interrupted work avoids completion advances; expired leases can be reclaimed. Optional prune removes certain orphaned artifacts.
- Activation or effect: Writes generated knowledge and indexes; quality scores can cause a fresh rewrite and later scheduling changes. Activation in actual later answers remains unobserved.
- Evidence limits: Wiring inspected, not run; no global atomic commit, factual correctness, hard spend bound or all-adapter equivalence established.

Admission and selection roles: callers supply sources/options; models propose content; code applies source-count evidence gating, configured curation/dedup, empty-response checks, output postprocessing and writing. Human approval is not required by this inspected path. Config/templates and existing selected content shape proposals; markdown, manifest, graph and derived indexes persist. Open requests and background maintenance are implemented modes; quality retry is a bounded retry within them, not an expected-answer experiment. Its format/grounding/coverage/wikilink/anti-pattern score is not an oracle supplying a known correct answer. Content-specific theory criticism is not inferred from a score-triggered rewrite.

Recovery is resumable processing rather than full rollback. Failed/cancelled passes withhold completion flags/manifest save. Article atomic writes precede index updates. A below-threshold article can still ship after retry, counted as an error. The background worker never prunes article files in its inspected removal path. The serve runner has a coordinator fence; the MCP compound `handleCompile` calls `compiler.Compile` directly, so that specific runner fence must not be generalized to every entry.

> // content (#145 prepareArticle gotcha). Still-low after the retry
> // counts as a compile error — the article ships with its final
> // score recorded either way.
> --- `internal/compiler/fullpipeline.go`

> // paths. Failure is advisory: count it and proceed uncurated.
> --- `internal/compiler/fullpipeline.go`

Batch is a separate provider-native route: config/flag/auto threshold can select batch submission, except subscription auth forces standard mode. Its checkpoint/resumption branches exist in `internal/compiler/pipeline.go`; the mode seam was inspected, but complete provider batching/resume semantics remain uninspected. No equivalence to synchronous provider injection or a uniform timeout/budget promise is asserted.

#### RT-RTE-search-wiki
Label: Search and explicit read

Agent/human request → MCP or engine search → retrieval results; requested article path → MCP read → file text. This route can return retained knowledge without native answer generation. Federated hub search is a separate parallel per-project document-search implementation that merges/truncates results and applies each project's output policy. SRC-1: `internal/mcp/server.go`, `pkg/engine/search.go`, `internal/hub/search.go`, `internal/trust/predicate.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked hits/content/paths, full requested file text, or error; hub results carry project identity.
- Later read-back: Search/read delivers previously retained files/entries to later caller invocations; what the host preserves afterward is outside this runtime.
- Delegated visibility: External caller receives tool results; the host decides subsequent reads, answer generation or captures. Federated goroutines are project searches, not delegated model agents.
- Selection predicate: Query, retrieval weights and result limits; output inclusion predicate on search surfaces; explicit read uses a caller-supplied path and lexical project containment.
- Invalidation or expiry: Fresh calls consult current stores/files; stale indexes or changed files can differ. No host-context eviction protocol is established here.
- Activation or effect: Delivery of retained content is wired; host reliance/compliance is unobserved. Direct read does not apply the search output-inclusion predicate.
- Evidence limits: Core entry points and hub implementation inspected; engine/MCP ranking internals and every caller's result handling are not exhaustively traced.

Selection is software-owned with optional provider assistance, not a known-answer oracle. This read route alone admits no proposed content. Its difference from synthesis matters: a rejected search output identity is not an OS-level prohibition on reading a known workspace path.

> content, err := os.ReadFile(fullPath)
> --- `internal/mcp/server.go`

#### RT-RTE-query-answer
Label: Retrieve synthesize and file

CLI/MCP/UI question → `Query` or `StreamQuery` → `buildQueryContext` → synthesis → filing. Code selects the configured query model or write-model fallback. The returned prose is a proposed answer; downstream admission is [RT-RTE-admit-output](#rt-rte-admit-output). SRC-1: `internal/query/query.go`, `internal/mcp/tools_compound.go`, `cmd/sage-wiki/main.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synchronous answer, sources, chunk IDs, optional filed path and separate FilingError; streaming token callbacks plus sources/error.
- Later read-back: Filed answers can later enter retrieval according to trust mode; retained source articles are reread on every question.
- Delegated visibility: Synthesis receives system guidance, wrapped question and assembled article context; optional retrieval expansion/reranking has separate calls. No autonomous tool-selection loop is implemented at this site.
- Selection predicate: TopK, chunk-index availability, enhanced/document fallback, graph relations, seen-path deduplication, output predicate, article prefixes and approximate token budget.
- Invalidation or expiry: Context is invocation-local; files remain reachable by new retrieval. Output state/source-change checks affect later eligibility, not an already-delivered answer.
- Activation or effect: Answer content returned and filing attempted; content's causal effect on a real user or later model is unobserved.
- Evidence limits: Approximate budgets and pre-assembly chunk metadata do not establish complete model-visible provenance. Stream and synchronous error contracts differ.

Open questions are the operating mode; there is no supplied reference-answer oracle in native synthesis. Guidance requests precise factual answers with wikilink citations; this is not code-enforced truth. Empty synchronous content fails before filing. Empty streaming content is not filed, while tokens may already have been delivered; streaming filing failures are logged rather than exposed as synchronous FilingError. `SaveAnswer` also accepts externally supplied prose and delegates to autoFile, so not every filed answer was generated by native synthesis.

> // MCP tool serializes OutputPath as a contract (issue #125 review).
> --- `internal/query/query.go`

> result.FilingError = err.Error()
> --- `internal/query/query.go`

#### RT-RTE-admit-output
Label: Output trust admission

Generated or caller-supplied answer → `autoFile` → unrestricted outputs/indexes or `trust.ProcessOutput` → pending/conflict/confirmation state → possible promotion; manual promote/demote/reject functions are additional controls. Code compares similar questions and answers; confirmation/independence/grounding/configured thresholds can authorize automatic promotion. SRC-1: `internal/query/query.go`, `internal/trust/hooks.go`, `internal/trust/promote.go`, `internal/trust/predicate.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Filed path/action or error; some post-transaction promotion and file-write failures log without failing ProcessOutput.
- Later read-back: Permitted `output:` entries can join future search/Q&A context; pending records support future similarity/confirmation comparisons.
- Delegated visibility: Embeddings and answer-comparison provider calls receive relevant question/answer material; promotion itself is local code, not a delegated agent.
- Selection predicate: Trust mode; similar-question match; answer agreement; distinct chunk-evidence sets; configured auto-promotion and grounding/consensus thresholds. Non-output identities pass the shared inclusion predicate.
- Invalidation or expiry: Demote deindexes while retaining output state; reject removes tracked output/file; verified-mode compiler source checks can demote stale outputs. Operations have separate failure surfaces, not global rollback.
- Activation or effect: Admission changes future retrieval eligibility and index state; correctness and downstream reliance remain unobserved.
- Evidence limits: Manual APIs do not identify a human principal. Agreement is not truth; complete comparison/grounding algorithms are left to specialist inspection. No observed promotion or recovery.

Proposer: synthesis model or SaveAnswer caller. Decider/veto: software trust policy, configured modes and explicit promote/demote/reject callers. Human per-content control is available through explicit caller action but is not necessary on the automatic or unrestricted paths; actual caller identity is unresolved. Mode: open Q&A with recurring-answer comparison, not a reference-answer experiment. Comparison to a retained answer is not an expected-answer oracle. Proposed answer text, source hashes and confirmation evidence persist.

The load-bearing ordering exception is visible in automatic promotion:

> tx.Exec(`UPDATE pending_outputs SET state = 'confirmed', promoted_at = ? WHERE id = ?`,
> now, match.Output.ID)
> *promoteAfterTx = match.Output.ID
> --- `internal/trust/hooks.go`

By contrast, the explicit promotion function says:

> // Mark confirmed LAST — only after all artifacts are durable
> --- `internal/trust/promote.go`

These are different enforcement points. Neither establishes an atomic file/index/state publication invariant across all callers. Embedding/ontology operations also include best-effort writes. Review exclusion is scoped to output identities and consumers applying the predicate, not all knowledge or all file access.

#### RT-RTE-write-article
Label: Caller-authored knowledge writes

MCP caller → summary/article write or `wiki_learn` → local file/index/manifest or learning store. The caller supplies content; these handlers do not invoke compiler generation as a precondition. Source-native knowledge types in wiki_learn are caller labels, not evidence of improved capacity. SRC-1: `internal/mcp/tools_write.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Write/store acknowledgement or validation/I/O/manifest error.
- Later read-back: Article/summary data becomes searchable; stored learning content is available to later configured consumers, whose complete loading is not traced in this runtime record.
- Delegated visibility: Calling host decides what to supply and receives acknowledgement; no model delegated by the inspected write handlers.
- Selection predicate: Required content/identity, valid concept identifier and project-path checks; learning requires type and content.
- Invalidation or expiry: Article/summary writes replace selected paths; caller edits/removal and later compile may change content. No universal expiry or prior-content rollback in these handlers.
- Activation or effect: Durable caller-authored knowledge is admitted without compile/trust-output gating; later host/model reliance remains unobserved.
- Evidence limits: All caller authorship and human approval are unresolved; downstream learning-store consumers need specialist tracing. Direct write success can coexist with logged index failure.

Admission proposer and content decider are the caller, with software structural veto. Operating mode: open writes, no expected-answer oracle. No built-in substantive proposal guidance in the handler; external instructions may guide callers. Article/summary atomic file persistence precedes index work and locked manifest mutation. A later manifest error does not undo a file already written.

> if err := fsutil.WriteFileAtomic(absPath, []byte(content), 0644); err != nil {
> --- `internal/mcp/tools_write.go`

#### RT-RTE-scribe-session
Label: Session scribe extraction

CLI transcript file → JSONL text compression → model entity extraction → ontology add/update/relations → counters and selected entities. Code omits thinking/tool-use/tool-result records and keeps user/assistant text; the provider does not receive the entire original transcript through this path. SRC-1: `cmd/sage-wiki/main.go`, `internal/scribe/session.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Scribe result with input/compressed/extracted/kept/skipped counts and entity/relation output, or extraction error.
- Later read-back: Added/updated ontology entities and relations persist for later graph consumers; exact later article/answer delivery is not established by this route alone.
- Delegated visibility: Extraction provider sees filtered transcript text; original thinking/tool records do not cross this extraction boundary.
- Selection predicate: Parseable JSONL user/assistant text, nonempty compressed content, extracted kebab-case IDs; existing entity updates require a differing nonempty definition.
- Invalidation or expiry: Differing definitions can overwrite prior definitions; no history/rollback is established in this inspected Process path.
- Activation or effect: Model-proposed domain representations enter ontology through code; no evidence of better future capacity or actual later reliance.
- Evidence limits: This is a separate producer, not proof that live agent sessions are automatically observed; malformed/omitted transcript content cannot support extraction-completeness claims.

Admission: model proposes; code checks specificity/existence/difference and writes. The initiating caller may be human but is not asked to approve each entity. Open transcript processing; no expected-answer oracle. Guidance is entity extraction, not criticism of the system's own method. The persisted result is ontology content, not the hidden model deliberation. Update errors may log while the returned kept count advances, limiting its use as a durability witness.

> // UPDATE: new definition differs — update it
> --- `internal/scribe/session.go`

#### RT-RTE-apply-pack
Label: Pack and prompt admission

Caller-selected pack manifest/files → `pack.Apply` → path validation, snapshots, allowed config/ontology merge, prompts/skills/samples and optionally parsers. This changes behavioral guidance and capabilities without a model proposing the update. Workspace prompt loading later selects overrides over embedded defaults. SRC-1: `internal/pack/merge.go`, `internal/prompts/prompts.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Apply result listing changes/conflicts or error.
- Later read-back: Future prompt-registry loads and configured pipeline calls consume installed guidance/config; external hosts may load installed skills. Parser files require separate execution grants.
- Delegated visibility: Pack acquisition/author content is external; apply performs local copying/merging. No model review is invoked in the inspected Apply path.
- Selection predicate: Validated manifest-relative paths, merge versus replace mode, config allowlist and merged-config validation; parser installation gated by EnableParsers.
- Invalidation or expiry: Reapply can replace or conflict; pre-apply snapshots support rollback and later removal. Existing loaded registries are not evidence of instant live reload.
- Activation or effect: Prompt/config/skill/parser files can alter later completion proposals, host guidance or executable capabilities; actual later activation is unobserved.
- Evidence limits: Apply implementation inspected; registry authenticity, all acquisition/update/removal behaviors and deployed host reloads are not established here.

Admission proposer: pack author; selection/admission caller: operator or program, identity unresolved; decider/veto: validation and mode rules. No per-content human approval or reference-answer oracle. Mode: caller-directed installation/update, not an autonomous improvement cycle. What persists includes new prompt/skill prose, symbolic configuration/ontology and parser files. Snapshot recovery is implemented as best effort: deferred restore calls ignore their returned errors. Local direct editing and provider injection are alternate change paths outside this pack gate.

> // copy prompts (mode-aware: merge skips existing, replace overwrites)
> --- `internal/pack/merge.go`

#### RT-RTE-run-parser
Label: Granted external parser execution

Compiler source extraction → registered extension command/arguments → subprocess with source bytes on stdin → stdout text back to extraction. Configuration and parser registry, not a model-selected shell tool, own this execution decision. SRC-1: `internal/compiler/pipeline.go`, `internal/compiler/fullpipeline.go`, `internal/extract/external.go`, `internal/extract/sandbox_linux.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parser stdout or timeout/process/gate error.
- Later read-back: Parsed text can become retained indexed/compiled content through the parent pipeline; parser subprocess-private state is uninspected.
- Delegated visibility: Process receives source bytes, configured arguments, a temp cwd and minimal environment; host filesystem/network access is not sandboxed by the inspected Linux implementation.
- Selection predicate: Matching registered extension, available command, enabled/trusted loader and Parse's sandbox-or-trust gate.
- Invalidation or expiry: Process timeout bounds duration; temp directory is removed on return; installed command files/grants persist until changed.
- Activation or effect: Runs arbitrary granted parser code and consumes its returned text; no observed isolation or parse correctness.
- Evidence limits: Linux implementation inspected; other platform details and external parser internals remain uninspected. Reduced environment/cwd are not filesystem confinement.

Capability admission is upstream in pack/config/local file changes, not an additional change admission inside each Parse call. Code can reject missing command/extension or absent grant. Caller-selected parser guidance is symbolic command/args; returned prose is input data. Open parsing operation, no known-answer oracle or model approval. Cancellation attempts process-group kill, not rollback of subprocess external effects.

> // canSandbox returns false — no real filesystem sandbox is implemented.
> // All external parser execution requires trust_external.
> --- `internal/extract/sandbox_linux.go`

#### RT-RTE-hydrate-workspace
Label: Remote workspace restoration

Caller restore request → mirror credentials/client → destination/lock/manifest gates → selected remote state → verified/decrypted restoration. This is an admission/recovery route for existing knowledge and production state, not new model synthesis. SRC-1: `internal/mirror/hydrate.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Restore report/error; facade exposes error-only hydration.
- Later read-back: Restored database/markdown/vector state can be opened by later workspace consumers.
- Delegated visibility: Remote S3-compatible object service receives object requests; no model agent is delegated.
- Selection predicate: Requested generation/time options and remote state; empty destination, except explicit partial resume with a progress marker; encrypted mirror requires a key.
- Invalidation or expiry: Restores a selected snapshot/generation rather than merging live knowledge; partial progress supports retry. Full failure-cleanup and WAL semantics remain uninspected here.
- Activation or effect: Existing state is installed for future use; the inspected gates establish neither semantic trustworthiness nor successful deployment activation.
- Evidence limits: Initial restore gates/verified download closure inspected; no remote operation or full replay/concurrency audit.

Proposer: remote retained state originally produced elsewhere in the workspace lifecycle. Decider: caller options plus software integrity/precondition gates. A human's semantic approval is unresolved. Mode: operator/program-directed restoration; hashes/AEAD check bytes, not a reference-answer oracle. Rejection includes nonempty destination, lock/manifest/key errors and verified download/decryption failure. Recovery is partial-resume capable; do not infer atomic rollback of the entire destination.

> // Empty-dir rule (no merge semantics). A --partial resume into a dir
> // with a progress marker is the one exception (spec: a follow-up
> // hydrate --partial resumes incomplete phases).
> --- `internal/mirror/hydrate.go`

### Claims

#### RT-CLM-review-order
Label: Promotion publication ordering

Claimed operation: explicit promotion moves/indexes output before its final confirmed-state write. SRC-1: `internal/trust/promote.go`. Implementation supports this local ordering, but it is not a system-wide guarantee: [RT-RTE-admit-output](#rt-rte-admit-output) records the earlier automatic state-write exception and best-effort subwrites. No observed durability outcome.

> // Index into search stores BEFORE marking confirmed
> --- `internal/trust/promote.go`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-query-guidance
Label: Query instruction and selected context

Consumer: synthesis completion provider. Channel: system message requesting factual cited answers and user message containing wrapped question/context. Force: natural-language guidance and evidence supply, not code-enforced truth or tool permission. Horizon: current synthesis invocation; the answer may subsequently persist through output admission. SRC-1: `internal/query/query.go`; [RT-RTE-query-answer](#rt-rte-query-answer).

> {Role: "system", Content: "You are a knowledge base Q&A assistant. Answer questions using the provided wiki articles as context. Cite sources using [[wikilinks]]. Be precise and factual."},
> --- `internal/query/query.go`

#### RT-BAP-generated-skill
Label: Generated host knowledge instructions

Consumer: external agent host reading its instruction file. Channel: `WriteSkill` renders and inserts/replaces marked content in target files including `CLAUDE.md`, `AGENTS.md` and `GEMINI.md`. Force: requested host behavioral policy, conditional on actual host loading and instruction precedence. Horizon: later host sessions until changed, not only the generation call. Template data describes the current project/types; static procedure guidance prescribes search/read before work and capture afterward. SRC-1: `internal/skill/skill.go`, `internal/skill/writer.go`, `internal/skill/packs/base.md.tmpl`.

> Before making changes or answering questions, search the wiki first:
> --- `internal/skill/packs/base.md.tmpl`

Generation writes instructions, but neither file presence nor this imperative demonstrates the host executed the prescribed knowledge loop. Updating a marked section preserves surrounding host content; external host authority, reload and compliance remain uninspected.

## Annotations

none
