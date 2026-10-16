---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Quicky Wiki runtime: source-to-graph compilation, query consumption, client mutation and maintenance at cfeecbffce5b6d0f16533b258a1e88edd86f731e."
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
---

# Quicky Wiki runtime report

## Runtime account

### Evidence and work boundary

Quicky Wiki implements a code-directed knowledge compiler and returning question-answer computation, not a general model-controlled action loop. Code chooses extraction, comparison, resolution, summary and answer calls; models supply claim text, semantic matches, page assignments and answers. The enclosing MCP client may have its own agent loop, but that client's planning is not this implementation. This account uses SRC-1 implementation and shipped prompt/design evidence only. No target execution, provider call, operational trace or causal experiment was supplied or performed. Implementation wiring does not establish model compliance, actual deployment grants, activation or benefit (SRC-1, `src/cli.ts`, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/query.ts`, `src/mcp/server.ts`).

The package exposes three aliases for the same CLI bundle, an importable library, a dashboard and MCP stdio/HTTP servers. Library exports include the store and compiler operations themselves: embedding callers need not pass through CLI or MCP checks. The CLI routes initialization, ingestion, query/consensus, watch, compilation/export, listing, discovery, lint and metabolism commands. The model adapter supplies text chat rather than a provider-native tool execution cycle (SRC-1, `package.json`, `src/cli.ts`, `src/lib.ts`, `src/llm/adapter.ts`; [RT-CMP-llm-adapter](#rt-cmp-llm-adapter), [RT-RTE-client-access](#rt-rte-client-access)).

Coverage added to the boundary's initial inspection under SRC-1: complete extraction, comparison, resolution, confidence, consensus, JSON parsing, watch, save-answer, setup, URL conversion, red-team, resurfacing, discovery, Markdown renderer, cascade and temporal implementations; store schema and mutation/retrieval portions; dashboard server routing and complete MCP implementation. These extend implementation/design inspection at the same registered commit, not the source register or evidence tier. Remaining UI templates, alternative export templates and dependency internals are not needed to establish the traced control paths; no exhaustive security, renderer or dependency audit is claimed.

### Ordinary invocation: source to later answer

1. A user runs `qw init`. Setup chooses the explicit provider/model or detects available providers/models and writes JSON to `.quicky/config.yaml`, plus `raw/`, `wiki/` and starter files. Subsequent commands load configuration from the current working directory and open `.quicky/graph.sqlite`; the database constructor creates schema/indexes if necessary. Principal identity is the host process, not a per-user database identity. Model/service identity comes from configuration, not a captured weight artifact ([RT-RTE-runtime-setup](#rt-rte-runtime-setup); SRC-1, `src/cli/create.ts`, `src/cli/context.ts`, `src/graph/store.ts`).
2. On `qw ingest raw/example.md`, the CLI resolves a path, loads config, opens the store and creates an adapter. Ingestion hashes the complete bytes, parses Markdown frontmatter and separates its body. Kind comes from override, first matching configured kind rule, frontmatter type, or `topic`. Frontmatter and optional overrides supply metadata. Existing identical bytes skip extraction but still synchronize primary-page kind and metadata. New/changed source identity and hash are written **before** model extraction ([RT-RTE-source-ingest](#rt-rte-source-ingest); SRC-1, `src/cli/ingest.ts`, `src/compiler/ingest.ts`).
3. Code supplies a fresh system/user message pair requesting atomic claims, confidence, tags, related concepts and dependencies. Long bodies are processed as sequential overlapping chunks; only extracted claim arrays escape each call. Code multiplies confidence by source-quality weight and clamps it. With no existing claims all extracted claims become new; otherwise one comparison call sees all retained and extracted statements and selects reinforcement, challenge or new admission. The comparison is model judgment, not reference-answer verification. Resolution mutates the graph automatically, then assigns new claims to pages in batches of eight and summarizes touched or summary-less pages with at most three workers ([RT-RTE-source-ingest](#rt-rte-source-ingest), [RT-OBJ-knowledge-diff](#rt-obj-knowledge-diff); SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/compiler/confidence.ts`).
4. The CLI prints the diff, attempts missing summaries, renders nonempty pages to Markdown and prints store totals. SQLite remains authoritative for the next command; Markdown is a derived view, not query input. Errors can leave partial source/graph state. Summary errors are swallowed; malformed extraction can return zero claims; malformed comparison instead treats all extracted claims as new. No workflow transaction wraps the entire invocation ([RT-RTE-source-ingest](#rt-rte-source-ingest); SRC-1, `src/cli/ingest.ts`, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/render/markdown.ts`).
5. On a later `qw query`, code searches the retained graph using the question, constructs page-grouped statements/confidence context and invokes a fresh answer call. CLI prints answer/confidence; dashboard and MCP use the same function with different result serialization. Optional CLI `--save` writes an answer-derived raw source, not an immediate graph update. Manual ingest or an active watcher can close that next admission loop ([RT-RTE-question-answer](#rt-rte-question-answer), [RT-RTE-answer-save](#rt-rte-answer-save); SRC-1, `src/graph/query.ts`, `src/cli/query.ts`, `src/cli/save-answer.ts`, `src/cli/watch.ts`).

### Material variants and working-context boundaries

The ingestion family has several shipped triggers. CLI directory ingestion sorts immediate `.md`, `.mdx` and `.txt` children and continues after individual failures. CLI URL ingestion fetches HTML, strips/converts it, writes a title-derived raw Markdown file, then uses the same compiler. The watcher initially scans recursively for paths not already registered, then debounces change notifications and suppresses concurrent processing of the same path. It is not a global work queue: different files and external clients can interleave around awaited calls. Deletions are ignored, and an existing changed file missed while the watcher was down is not reprocessed by the initial unregistered-only scan. Dashboard bookmarks fetch/write/ingest but do not follow the CLI's Markdown rendering tail. MCP ingestion follows the compiler with missing summaries and rendering. Direct library/store consumers can bypass these driver tails entirely (SRC-1, `src/cli/ingest.ts`, `src/cli/fetch-url.ts`, `src/cli/watch.ts`, `src/cli/serve.ts`, `src/mcp/server.ts`, `src/lib.ts`; [RT-RTE-source-ingest](#rt-rte-source-ingest), [RT-RTE-client-access](#rt-rte-client-access)).

Context control is per-call construction rather than conversation trimming. Extraction splits only when content exceeds 12,000 characters, uses 8,000-character chunks with 500 overlap, then deduplicates normalized statement prefixes of length 80. Comparison loads all existing statements; assignment supplies all page titles; summaries receive all claims on one page. Normal answers use lexical search with limit 50 per result category, plus up to ten claims from a matched page lacking a direct claim hit. Consensus instead supplies all page-associated claims to every responder. These are distinct selectors, not one uniform context bound. Independent calls resemble disposable frames whose returns escape, but there is no source-level sub-agent runtime, frame reload pointer or model-visible reference semantics in these implementations. The retained store permits a later query to reconstruct a different context; it does not restore hidden reasoning or prior message history (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/query.ts`, `src/compiler/consensus.ts`).

Consensus is a material forcing route: models answer independently, then the primary model compares successful parsed responses. Despite a comment saying the primary is always included, the code adds it only when no configured adapter initializes. A single successful response is returned as agreed claims, and comparison failure returns the first response as agreed. Thus `agreed` is not always evidence of agreement among multiple models ([RT-RTE-consensus-answer](#rt-rte-consensus-answer); SRC-1, `src/compiler/consensus.ts`).

### Guarantees, forcing cases and authority envelope

The capability surface is host filesystem reads/writes, SQLite mutation, remote fetching, provider requests, MCP tools and dashboard mutation routes. Current grants are whichever filesystem, credentials, network and process privileges the operator supplies; no deployment grant set was captured. The deployed isolation envelope is unobserved. Neither a displayed localhost URL nor a tool description establishes sandboxing. The model adapter sends messages and consumes text; action authority resides in host code and callers, not in model-issued shell/tool calls (SRC-1, `src/llm/adapter.ts`, `src/mcp/server.ts`, `src/cli/serve.ts`, `src/cli/fetch-url.ts`). Four source-inspected forcing cases bound the important guarantees:

| Forcing case and owner | Enforcement, strength and covered path | Alternate path / external contract | Separate conclusions |
|---|---|---|---|
| MCP `ingest_file` says a file must exist in `raw/`; host tool handler owns enforcement | Description is policy, not a containment invariant: handler only resolves caller path before shared ingestion | CLI accepts arbitrary file paths, URL ingestion writes fetched bytes, and library accepts caller paths/store writes. Actual containment would require host filesystem restrictions or additional caller policy | implementation conclusion status: wired; operation conclusion status: uninspected. Wired behavior is unrestricted resolution, not the described containment |
| Identical-byte ingestion skips extraction; compiler owns hash check | Conditional invariant for that compiler path: matching registered path/hash returns an empty diff after metadata/kind sync | Hash is updated before successful extraction/resolution; retrying unchanged failed bytes can skip the unfinished work. Store mutation and config changes are alternate inputs. Reliable completed-ingestion semantics need a stronger external recovery contract | implementation conclusion status: wired; operation conclusion status: uninspected |
| SQLite mutation integrity; store owns local transactions | Transactional invariant for the writes within `addClaim`, `reinforceClaim`, `challengeClaim`, `deleteClaim` and `deletePage`, subject to SQLite contract; foreign keys and WAL enabled | `deleteEmptyPages`, called directly by dashboard prune and CLI lint prune, deletes links and pages in separate statements without a method-wide transaction. Multi-call ingest, async model calls, render files and raw-file writes are not one transaction. Direct statement/confidence changes do not follow reinforcement event recording. No captured backup/recovery contract | implementation conclusion status: wired; operation conclusion status: uninspected |
| Honest confidence/citations and consensus; prompt/model plus parsing code own answer production | Policy/best effort: natural-language instruction and permissive parsing, not verified factual or citation correctness | Standard query omits claim IDs in model-visible context; one-model consensus and first-response fallback weaken multi-model agreement. Requires truthful source inputs, appropriate models and any downstream verification | implementation conclusion status: wired; operation conclusion status: uninspected |

These are bounded static cases, not exploit tests. Evidence: SRC-1, `src/mcp/server.ts`, `src/compiler/ingest.ts`, `src/graph/store.ts`, `src/compiler/resolve.ts`, `src/graph/query.ts`, `src/compiler/consensus.ts`; minimum passages appear in the corresponding route records below. No deployment guarantee is inferred.

Dashboard routing adds a concrete reachability qualification: its first `/api/page` branch checks pathname alone, so the later `/api/page` DELETE branch is shadowed. Claim PATCH/DELETE and prune are separately reachable branches. MCP HTTP and dashboard both use `server.listen(port)` without an explicit host and allow wildcard CORS in their responses; their inspected dispatchers show no authentication/approval stage. This does not establish external reachability in any actual installation. Direct library code can also mutate the store; no CLI-level control can cover arbitrary embedding callers (SRC-1, `src/cli/serve.ts`, `src/mcp/server.ts`, `src/lib.ts`; [RT-RTE-client-access](#rt-rte-client-access)).

### Admission, maintenance and change horizon

Knowledge admission is automatic after workflow initiation: the user supplies a source or a caller supplies a tool request, but neither constitutes per-claim approval. Code accepts parsed extraction/diff decisions and executes changes, with store constraints and fallback behavior rather than an independent truth oracle. Direct dashboard edits and MCP metadata merges are separate admission mechanisms. Decay changes confidence by a time rule; red-team, resurfacing and discovery return suggestions without a wired acceptance step in those callers ([RT-RTE-source-ingest](#rt-rte-source-ingest), [RT-RTE-client-access](#rt-rte-client-access), [RT-RTE-health-review](#rt-rte-health-review)). The graph influences subsequent calls as evidence-like text, not as newly installed executable capabilities ([RT-BAP-retained-context](#rt-bap-retained-context)). Detailed memory revision assessments remain for the memory member.

Production configuration changes provider identity and extraction instructions on later loads; it does not modify model weights. Shipped product changes enter through repository/main version change, build/typecheck and npm publication, not through knowledge compilation. The release workflow is a declared delivery pipeline, not evidence of a successful release or runtime self-modification ([RT-RTE-runtime-setup](#rt-rte-runtime-setup), [RT-RTE-package-release](#rt-rte-package-release)). No demonstrated improvement, calibrated confidence, reliable criticism or exercised self-improvement follows from these source paths. Model internals, actual concurrent executions, deployment security, latency, long-term quality and actual recovery remain unobserved.

## Shared records

### Components

#### RT-CMP-llm-adapter
Label: Configured chat model endpoints

Source-native identity: `LLMAdapter` produced by `createLLMAdapter`, with provider/model name and `chat` method. Symbolic TypeScript adapter code is stored in the package; the model it addresses is distributed-parametric, stored in external service or local provider machinery, not in this Git capture. Anthropic uses its SDK; OpenAI, Gemini, Ollama and compatible providers use OpenAI chat-completion interfaces. Provider credentials are explicit config values or environment variables; compatible/local endpoints permit a placeholder key (SRC-1, `src/llm/adapter.ts`).

Parameters are not updated by inspected adapter calls: they request inference. Provider-side mutation/training remains uninspected. Exact weight version is not pinned by the adapter; a model string is supplied, and a mutable base URL/model alias can resolve to another model. Consensus uses multiple instances of this component with the same fixity limits, not a distinct captured weight artifact. No inaccessible provider state is treated as absent memory (SRC-1, `src/llm/adapter.ts`, `src/compiler/consensus.ts`).

> const response = await anthropic.messages.create({
>   model: cfg.model,
>   max_tokens: options?.maxTokens ?? 4096,
> --- `src/llm/adapter.ts`

The SDK calls carry text messages, temperature/token options and optional JSON response format; no provider-native tools are passed by these adapter implementations. An embedding caller can provide its own adapter under the library's interface; its internals and grants are not established here (SRC-1, `src/lib.ts`, `src/llm/adapter.ts`).

### Operative objects

#### RT-OBJ-knowledge-store
Label: KnowledgeStore graph and event substrate

Source-native identity: `KnowledgeStore`, opened by CLI at `.quicky/graph.sqlite`. SQLite rows and relations are symbolic: UUID/path identities, confidence/time numbers, source/provenance/dependency/event links, kind and JSON metadata. Claim statements and page summaries are natural-language parts stored in those rows and interpreted by model/human consumers; they are not executable rules merely because SQLite stores them. Source bytes remain in files; source rows retain paths/hashes/metadata rather than a full raw snapshot. Generated wiki files are a separate derived text view (SRC-1, `src/graph/store.ts`, `src/cli/context.ts`, `src/render/markdown.ts`).

> export function getDbPath(): string {
>   return join(getDataDir(), "graph.sqlite");
> }
> --- `src/cli/context.ts`

> this.db.pragma("journal_mode = WAL");
> this.db.pragma("foreign_keys = ON");
> --- `src/graph/store.ts`

#### RT-OBJ-knowledge-diff
Label: Ingestion KnowledgeDiff

Source-native identity: `KnowledgeDiff`, an in-process object returned by comparison, consumed and filled with IDs during resolution, then returned to drivers. Symbolic arrays classify actions and name IDs/confidences; natural-language fields carry statements, challenge reasons and gaps. It is not itself a durable transaction or approval artifact. Durable consequences are store mutations; CLI output is a partial presentation. Extraction's dependency statements do not survive as dependency-edge writes through this diff/resolution path (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`).

> confidenceAfter: Math.max(0.01, existing.confidence * 0.6),
> reason: match.reason || "Contradicted by new evidence",
> downstreamAffected: store_deps.length,
> --- `src/compiler/diff.ts`

### Routes

#### RT-RTE-runtime-setup
Label: Project and model configuration admission

User/embedding principal → setup/config files → command loaders → adapter and compiler. Setup owns the next step, choosing explicit options or detected provider/model, then writing project configuration. Config is symbolic JSON despite its `.yaml` name; entity prompt strings are natural-language guidance consumed by extraction, separately from symbolic kind-rule matching. Host setup writes raw/wiki directories and config, not model weights. SRC-1, `src/cli/create.ts`, `src/cli/context.ts`, `src/compiler/ingest.ts`.

- Immediate return: Setup prints project/provider information; loader returns config and adapter to the driver.
- Later read-back: Subsequent commands load `.quicky/config.yaml`; watcher/server retain their startup config rather than reloading on every request.
- Delegated visibility: Provider receives the chosen messages and options; extraction receives the selected entity-kind prompt, not all configuration fields.
- Selection predicate: Explicit provider/model override detection; extraction uses `entityPrompts[pageKind]`; first matching kind rule wins.
- Invalidation or expiry: File replacement changes later loads; malformed/non-JSON config falls back to defaults; shallow merge does not independently validate nested config.
- Activation or effect: Config is wired to adapter identity, raw/wiki destinations and extraction policy; actual use and effects are unobserved.
- Evidence limits: No installed config, credentials or provider model listing was supplied; no actual selection or model quality established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: user options and environment/detection propose provider selection; setup code decides/writes without a second approval. A user can override before invocation or edit configuration afterwards. Reinitialization overwrites config/starter files; no backup/rollback is implemented there. Guidance is defaults/provider preference logic and configured entity prompt text; the resulting config persists. Operating mode is open setup, not an experiment; answer oracle is inapplicable because no expected answer is assessed (SRC-1, `src/cli/create.ts`, `src/cli/context.ts`).

> return { ...DEFAULT_CONFIG, ...JSON.parse(raw) };
> --- `src/cli/context.ts`

> const entityExtra = ctx.entityPrompts?.[ctx.pageKind]?.trim();
> --- `src/compiler/ingest.ts`

#### RT-RTE-source-ingest
Label: Source extraction and automatic graph admission

File/URL/watch/MCP/bookmark trigger → host compiler → extraction model → comparison model or empty-store shortcut → resolver/store → summaries → driver return/render where wired. Code owns sequencing; the model supplies semantic decisions. UUID source/claim/page identities are assigned by the store, while model matching uses transient array indices. Context, partial-state boundaries and driver variants are traced above. SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/cli/ingest.ts`, `src/cli/watch.ts`, `src/mcp/server.ts`, `src/cli/serve.ts`.

- Immediate return: KnowledgeDiff with resolution IDs, driver counts/diff display, optional rendered paths.
- Later read-back: Newly written claims, confidence, summaries and provenance are selected by later queries, comparisons, page reads and reviews.
- Delegated visibility: Each provider sees its supplied source chunk or retained/new statement lists; assignment sees page titles; summaries see one page's claims. No autonomous remote-worker delegation is implemented by these calls.
- Selection predicate: Registered path/hash skip; chunk threshold and deduplication; empty-store shortcut; model action/index matches; page assignment batches of eight; touched and missing-summary pages.
- Invalidation or expiry: Changed bytes trigger another compilation; identical hash skips claims even if prompt/config changed. Store mutations and deletion can change retained content independently.
- Activation or effect: Code writes reinforce/challenge/new claims and summaries without per-item human approval; actual semantic correctness and later behavioral influence remain unobserved.
- Evidence limits: No supplied execution; permissive JSON parsing and model-selected indices do not establish complete extraction or correct matching. Comparison can omit claims by omitting matches.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes extracted statements/actions/page titles; code accepts parseable arrays and valid referenced indices, applies fixed score rules and writes. The initiating user selects source/type/quality but does not approve each claim. Rejection consists of parse/index/DB failure, not an independent correctness gate. Extraction parse failure returns empty; comparison parse failure admits all as new. Missing assignments fall back to first page or `General`; summaries are noncritical. No whole-ingest rollback: source/hash and earlier mutations can survive a later failure. Guidance persists in shipped prompts, not as a newly revised method; outputs persist as graph content. Operating mode is open document ingestion; source text is evidence input, not an independent expected-answer oracle (SRC-1, cited compiler paths).

> if (existing && existing.contentHash === contentHash) {
>   syncPrimaryPageEntity(store, title, resolvedKind, pageMetadata);
> --- `src/compiler/ingest.ts`

> if (existing) {
>   store.updateSourceHash(existing.id, contentHash);
>   source = { ...existing, contentHash };
> --- `src/compiler/ingest.ts`

> // Fallback: treat all as new
> --- `src/compiler/diff.ts`

The extraction prompt asks for dependencies, but `computeKnowledgeDiff` drops `dependsOnStatements` and the complete resolver does not call `addClaimDependency` or `addClaimContradiction`. A source-tree symbol search finds only those method declarations in the store. Thus cascade code can operate on externally populated edges, but automatic ingestion is not shown constructing them. This qualifies any universal claim that extraction dependencies necessarily become graph edges (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/store.ts`, `src/graph/cascade.ts`).

#### RT-RTE-question-answer
Label: Retrieved single-model answer

CLI, MCP or dashboard question → `queryKnowledge` → store search/context construction → configured chat endpoint → parsed answer/confidence/claim IDs → driver. Code controls retrieval and return; model decides answer content under an uncertainty/citation request. SRC-1, `src/graph/query.ts`, `src/graph/store.ts`, `src/cli/query.ts`, `src/mcp/server.ts`, `src/cli/serve.ts`.

- Immediate return: Answer with caveats, claim ID array and overall confidence; malformed JSON returns raw text, no IDs and confidence 0.5. MCP further replaces IDs with their count.
- Later read-back: inapplicable — plain queries do not persist answers; the separate save route supplies optional retention.
- Delegated visibility: Provider gets page titles, statements and rounded confidence, plus question. Source bodies, source identities, claim IDs, full histories and graph edges are not included in this answer context.
- Selection predicate: ASCII-alphanumeric sanitization, stop-word/short-word removal, prefix-OR FTS search limited to 50 each for pages/claims, LIKE fallback on search failure; up to ten claims for title/summary-only page hits.
- Invalidation or expiry: Each invocation rebuilds context from current graph; there is no persistent chat history in queryKnowledge.
- Activation or effect: Retained statements are delivered as evidence-like context; model compliance, faithful citations and actual influence are unobserved.
- Evidence limits: Returned IDs are not verified against selected claims, and model-visible statement lines omit IDs despite requesting them. No answer oracle or calibration evaluation supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode is open user question answering. The model proposes and decides the returned answer; parsing supplies fallback but no factual veto. The requester can reject the output externally. No expected-answer/reference-outcome oracle is implemented (SRC-1, `src/graph/query.ts`).

> `  - [${((c.confidence ?? 0) * 100).toFixed(0)}%] ${c.statement}`,
> --- `src/graph/query.ts`

> claimIds: parsed.relevantClaimIds ?? [],
> confidence: parsed.overallConfidence ?? 0.5,
> --- `src/graph/query.ts`

#### RT-RTE-consensus-answer
Label: Independent responders and model comparison

CLI `--consensus` → provider/model detection → adapter creation → parallel independent answer calls → primary model comparison when at least two parsed responses → CLI display. SRC-1, `src/cli/query.ts`, `src/compiler/consensus.ts`, `src/llm/detect.ts`.

- Immediate return: Agreed/disputed/uncertain arrays, synthesis, model names and overall confidence; zero responders yields explicit no-response output.
- Later read-back: inapplicable — this branch prints results and does not enter the standard branch's `--save` code.
- Delegated visibility: Each responder sees the same page-grouped claims/confidences; comparison sees successful response claims, reasoning and answers, not an independent source corpus.
- Selection predicate: Available detected providers initialize adapters; failed calls/JSON are dropped; primary substitutes only if no adapter initializes. One parsed response bypasses comparison.
- Invalidation or expiry: In-process responses last for this invocation; new runs redetect models and reread graph.
- Activation or effect: Response synthesis is wired, but agreement labels can arise from one response or first-response fallback rather than multi-model convergence.
- Evidence limits: No captured runs, independence validation, reference answers or evidence of improved accuracy; shared context/model error can survive comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode is open multi-model answering, not a bounded experiment. Responders propose; primary compares when possible; code controls fallback/admission to result arrays. Human selects the mode and can reject output externally, but no per-claim veto is wired. There is no answer oracle: model comparison is judgment, not a supplied correct answer (SRC-1, `src/compiler/consensus.ts`).

> if (modelResponses.length === 1) {
>   const r = modelResponses[0];
> --- `src/compiler/consensus.ts`

> // If consensus comparison fails, return best-effort
> --- `src/compiler/consensus.ts`

#### RT-RTE-answer-save
Label: Answer-derived raw source admission

Standard CLI query with `--save` → `saveAnswerAsSource` → raw Markdown file → later explicit ingestion or watched-file processing. Code owns serialization; the human opts into saving, not per-statement factual approval. Source question/answer/confidence are natural-language/numerical output content; symbolic frontmatter identifies it as `note` and `blog`. SRC-1, `src/cli/query.ts`, `src/cli/save-answer.ts`, `src/cli/watch.ts`.

- Immediate return: Saved path and instruction to ingest it; file contains answer, question, confidence metadata and resolved cited statements.
- Later read-back: Compiler can read generated file and admit its re-extracted content to graph; active watch can initiate that automatically after the file write.
- Delegated visibility: Later extractor sees the generated document, not hidden reasoning or authenticated original evidence. Unresolvable claim IDs omit cited statements.
- Selection predicate: Only standard answer branch with `opts.save`; filename is question-derived slug limited to 80 characters.
- Invalidation or expiry: Same question/slug can overwrite the same file; graph update still follows ordinary hash/ingest rules.
- Activation or effect: Raw-file retention is wired; eventual graph admission and answer influence require the later route and are unobserved.
- Evidence limits: Saving is not validation; answer-generated source does not establish independent evidence or improved future capacity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission uses user save flag plus unconditional file write; later per-claim admission belongs to [RT-RTE-source-ingest](#rt-rte-source-ingest). No backup/undo is implemented in the save helper. Guidance is fixed serialization with `quality: blog`, not criticism/revision of method. Open query-save mode has no answer oracle (SRC-1, `src/cli/save-answer.ts`).

> await writeFile(filePath, content, "utf-8");
> --- `src/cli/save-answer.ts`

#### RT-RTE-client-access
Label: MCP, dashboard and direct store access

Client/tool/HTTP request → dispatcher → read/query/shared compiler or direct store mutation → JSON/text response. MCP advertises schemas but dispatches cast arguments; dashboard uses local type checks on selected fields. Store/library consumers can invoke mutations without either dispatcher. Caller identity is process/transport access, not an authenticated user record in these handlers. SRC-1, `src/mcp/server.ts`, `src/cli/serve.ts`, `src/lib.ts`, `src/graph/store.ts`.

- Immediate return: Tool text JSON/read results, ingest counts or mutation acknowledgements; tool exceptions become `isError`, dashboard errors become HTTP responses.
- Later read-back: Ingestion, metadata changes and reachable claim PATCH/DELETE/prune affect later store readers. Page DELETE handler is shadowed by the earlier pathname-only page read branch.
- Delegated visibility: MCP query exposes answer/confidence and claim-reference count; page tools expose statements/confidence/source counts and metadata, not full original files. Client policies beyond these payloads are uninspected.
- Selection predicate: RPC method/tool name and provided arguments; page title/ID, entity kind/metadata equality, search text and confidence filters; dashboard route/method checks.
- Invalidation or expiry: Dashboard-owned writes invalidate its cache; cached read TTLs range from 5 to 60 seconds. External CLI/MCP writes do not call this in-process invalidator. Direct store edits do not automatically regenerate Markdown views.
- Activation or effect: Dispatcher connects clients to the graph and host file ingestion; actual client use, exposure and isolation are unobserved.
- Evidence limits: Descriptions/CORS/local URLs are not access-control guarantees. Host OS, network policies and enclosing client grants were not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission mechanisms differ: MCP metadata merge accepts caller content; dashboard claim edits accept supplied string/number; ingestion uses compiler decisions; deletion/prune is code-directed on caller request. Starting a server is not approval of every later mutation. Handlers do not interpose human approval; available requests can be withheld by callers/host restrictions. SQLite transactions cover `deleteClaim` and `deletePage`, but not `deleteEmptyPages`: dashboard prune calls that method directly, so link/page deletions are not atomic as a whole. Direct confidence/statement edits do not record reinforcement/challenge events or supply versioned rollback. User restoration/backups are external, unobserved. Mode is open client requests with no reference-answer oracle (SRC-1, `src/graph/store.ts`, `src/mcp/server.ts`, `src/cli/serve.ts`).

> description:
>   "Ingest a source file into the wiki. File must exist in the raw/ directory.",
> --- `src/mcp/server.ts`

> const filePath = resolve(args.path as string);
> --- `src/mcp/server.ts`

> } else if (url.pathname === "/api/claim" && req.method === "PATCH") {
> --- `src/cli/serve.ts`

HTTP handlers do not establish a deployed authentication or sandbox boundary; MCP stdio relies on who controls the process pipes. The two HTTP servers bind with the port alone. JSON schemas advertise expected arguments but `handleJsonRpc` calls the dispatcher directly rather than validating them against `TOOLS`. These are static control-path findings, not proof of a successful attack (SRC-1, `src/mcp/server.ts`, `src/cli/serve.ts`).

#### RT-RTE-health-review
Label: Maintenance and review outputs

User maintenance/discovery/lint request → store selection → deterministic calculation or model review → CLI report; decay/prune also mutate. Health/stale/cascade inputs are symbolic statistics/relations plus natural-language claims; critique and discovery outputs are natural-language proposals. SRC-1, `src/cli/metabolism.ts`, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/discovery/discover.ts`, `src/graph/temporal.ts`, `src/graph/cascade.ts`.

- Immediate return: Health/decay details, review questions, critiques/suggested confidence adjustments or discoveries. CLI red-team prints suggestions without applying them.
- Later read-back: Decay writes new confidence; ordinary confidence updater also resets `last_reinforced`. Critiques/resurfacing/discoveries are not persisted or automatically admitted by the inspected functions/caller.
- Delegated visibility: Red-team sees up to five highest-confidence claims at least 0.7 with confidence/source counts, not source bodies. Resurfacing sees up to five stale/low-confidence claims; discovery sees page-grouped claim statements.
- Selection predicate: Red-team confidence ordering; resurfacing stale over 14 days or confidence at most 0.5, deduplicated and weakest first; user discovery mode; decay time and claim decay rate.
- Invalidation or expiry: Review results are invocation-local. Decay changes future confidence/staleness inputs; it has no separate critique-based acceptance queue or undo in this caller.
- Activation or effect: Decay update is wired; model critiques are delivered as proposals, not demonstrated changes in reliance or accepted revisions.
- Evidence limits: Review prompt is not proof of valid criticism; no supplied review trace, acted-on critique or measured improvement. Dependency-based effects require populated edges.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Computational roles: code selects candidates; model proposes review/diagnosis; CLI displays. Human may act later via another route, but no rejection/acceptance decision over proposed critique is wired here. Decay admits numeric updates by fixed exponential rule/clamp once user requests cycle; rollback is external. CLI lint prune directly calls `deleteEmptyPages`, whose link and page deletions have no method-wide transaction; an interrupted prune can leave partial deletions. This maintenance path does not inherit the atomicity of `deleteClaim` or `deletePage` (SRC-1, `src/cli/lint.ts`, `src/graph/store.ts`). Guidance is shipped maintenance prompts/rules and existing graph contents; confidence persists, critique text does not. These are open maintenance requests, not controlled experiments; no expected-answer oracle is supplied. They do not by themselves establish content-directed theory revision, retained criticism iteration, learning or reflection (SRC-1, cited maintenance files).

> store.updateClaimConfidence(claim.id, clamped);
> --- `src/graph/temporal.ts`

> console.log(`    ${c.critique}`);
> --- `src/cli/metabolism.ts`

The prune method executes the following deletion sequence without wrapping the method in `this.db.transaction` (SRC-1, `src/graph/store.ts`). Both callers invoke it directly (SRC-1, `src/cli/lint.ts`, `src/cli/serve.ts`):

> for (const row of emptyPages) {
>   this.db
>     .prepare(
>       "DELETE FROM page_links WHERE from_page_id = ? OR to_page_id = ?",
>     )
>     .run(row.id, row.id);
>   this.db.prepare("DELETE FROM pages WHERE id = ?").run(row.id);
> }
> --- `src/graph/store.ts`

#### RT-RTE-package-release
Label: Repository change to published package

Main-branch push → version comparison → conditional dependency install/build/typecheck → npm publish/release. Owner is repository/CI operator; next-step decisions are workflow conditions and command success. Product artifacts are symbolic executable package bytes, separate from graph content. SRC-1, `.github/workflows/publish.yml`, `package.json`.

- Immediate return: CI step results, intended npm publication and GitHub release creation.
- Later read-back: inapplicable — installation/consumption of a newly published release is outside captured execution evidence, not a retained-memory read-back established here.
- Delegated visibility: CI receives source and configured publication token; npm/GitHub receive publish/release requests.
- Selection predicate: Main-branch push and changed package version relative to previous commit.
- Invalidation or expiry: Unchanged version skips publish; failed required steps prevent later steps by ordinary workflow sequencing. Actual registry state is uninspected.
- Activation or effect: Production-delivery pipeline is wired; no captured publication, installation or later execution.
- Evidence limits: No branch-protection, review approval, actual CI run or registry artifacts supplied; build/typecheck are not behavioral correctness evaluation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: repository contributors propose product changes; authorization of merge/push remains external/uninspected; workflow gates publication by version/build/typecheck, not an LLM decision. Failure can reject before publication; no publication rollback step is specified. Guidance is package build/type contract; release artifacts persist externally if published. Mode is event-driven delivery, not improvement experimentation; no expected-answer oracle. No knowledge/compiler output installs new code or tools through this workflow (SRC-1, `.github/workflows/publish.yml`).

> run: npm publish --provenance --access public
> --- `.github/workflows/publish.yml`

### Claims

#### RT-CLM-confidence-citations
Label: Confidence-aware cited answers

The MCP query tool claims an answer with confidence and cited claims. Implementation requests citation behavior, but the ordinary answer prompt receives statement/confidence lines without IDs, returns unvalidated model-provided IDs and MCP serializes only their count. This supports a requested/structured answer feature, not verified citation integrity or calibrated truth (SRC-1, `src/mcp/server.ts`, `src/graph/query.ts`; [RT-RTE-question-answer](#rt-rte-question-answer)).

> "Ask a question against the Quicky Wiki knowledge base. Returns answer with confidence score and cited claims.",
> --- `src/mcp/server.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-retained-context
Label: Retained claims to future model decisions

Consumer: extraction comparison, page assignment/summary, ordinary answer, consensus and maintenance models. Channel: host-constructed text messages containing selected retained statements, titles, confidence or model responses. Force: natural-language evidence/guidance interpreted by model, not guaranteed obedience or executable capability. Horizon: across command invocations through the SQLite graph; within an invocation through intermediate arrays. Model returns become graph changes only through resolver or explicit save/reingest/direct-edit routes. Delivery is wired, while activated influence and benefit are unobserved (SRC-1, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/query.ts`, `src/compiler/consensus.ts`, `src/metabolism/redteam.ts`).

> content: `Knowledge base contents:\n\n${context}\n\nQuestion: ${question}`,
> --- `src/graph/query.ts`

Configuration's selected entity prompt is a stronger instruction channel than ordinary graph evidence: appended to extraction's system prompt. It is separately admitted through project configuration, not automatically derived from observed performance or critique in the inspected paths (SRC-1, `src/compiler/ingest.ts`, `src/cli/context.ts`; [RT-RTE-runtime-setup](#rt-rte-runtime-setup)).

## Annotations

none
