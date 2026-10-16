---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Stash runtime baseline: MCP and CLI memory requests, model-driven maintenance and release admission at d34ed430c4348ef741ef95146b488aea8616f4fb."
run-id: AAS-2026-10-15-stash-7ac5612837a0-01
reviewed-boundary: d34ed430c4348ef741ef95146b488aea8616f4fb
---

# Stash runtime report

## Runtime account

### Responsibility and evidence

Stash owns memory operations and a model-dependent maintenance pipeline, not the enclosing agent's task loop. The ordinary shipped interaction is an external MCP client calling a tool, a Go handler calling Brain, Brain calling an embedding provider and PostgreSQL, and the handler returning JSON as MCP text. The client owns the next task decision. Stash's maintenance code instead owns the next stage of consolidation and issues chat-completion requests itself. These responsibilities are distinguished in [RT-RTE-remember-write](#rt-rte-remember-write), [RT-RTE-recall-read](#rt-rte-recall-read) and [RT-RTE-consolidation-run](#rt-rte-consolidation-run). Evidence is implementation and doctrine/design from SRC-1, not observed execution. No target command, test, provider or service was executed; successful operation, client adherence and improved answers remain unobserved. [SRC-1: `cmd/cli/mcp.go`, `internal/brain/consolidate.go`]

Added detailed implementation inspection covers `internal/brain/brain.go`, `internal/brain/context.go`, `internal/embedder/cache.go`, `internal/queries/recall.sql.tmpl`, `internal/db/db.go`, `internal/config/config.go`, the structured-fact and grounding portions of `internal/reasoner/openai.go`, and complete consolidation service drivers. Added doctrine inspection covers the initial server-description protocol in `cmd/cli/mcp_prompts.tmpl`; build/publication wiring was inspected in `.github/workflows/release.yml` and `Dockerfile`. All are SRC-1 at the frozen revision. Secondary goal, failure, hypothesis, pattern and contradiction transformations are identified by consolidation orchestration and MCP/CLI registry searches here, not exhaustively audited; their content revisions belong to specialist analysis. This prevents treating this baseline as a correctness audit of every retained object.

### Ordinary invocation and entry paths

The CLI's Before hook initializes configuration, database migrations, vector dimensions/indexes, embedding adapter plus cache, reasoner adapter, SQL templates and Brain. Credentials, endpoint, embedding model, dimensions and reasoner model are configured; constructing both model clients is part of bootstrap even for a read. Configuration loads `STASHCONFIG`, or `.env`, before environment parsing. Bootstrap failures terminate the command rather than produce a memory result. [SRC-1: `cmd/cli/main.go`, `internal/bootstrap/bootstrap.go`, `internal/config/config.go`, `internal/db/db.go`]

For an ordinary successful `remember` request, the principal is the external caller, content is supplied by that caller, and the identity inside Stash is an exact namespace slug resolved to a database ID. The MCP handler defaults to `/`; it does not run an agent or classify the content's original author. Brain validates content/path, requires an existing namespace, obtains a cached or fresh vector, inserts an episode, and returns its ID. There is no per-content approval call between provider response and insertion. Later `recall` embeds a query, expands requested namespace subtrees, queries facts first, fills remaining slots with episodes, sorts the selected results, and returns serialized records. This is not a combined globally ranked facts-and-episodes candidate search. State is persistent PostgreSQL; request-local state is Go values, contexts and result slices. The effect boundary is SQL storage plus outbound provider calls, not shell execution or autonomous task completion. Errors propagate to the tool caller; a failed insert can still leave an embedding cache entry because embedding precedes insertion. [SRC-1: `cmd/cli/mcp.go`, `internal/brain/episode.go`, `internal/brain/recall.go`, `internal/embedder/cache.go`]

CLI `remember` and `recall` use the same Brain methods, but adapters differ. CLI `remember` accepts an occurrence timestamp and rejects whitespace-only input; Brain only checks empty content and length. CLI `recall` supplies its namespace flags unchanged, and Brain rejects an empty namespace list; MCP defaults to `/`. Stdio and SSE construct the same MCP tool registry. The CLI additionally exposes destructive ID-based purge and explicit hypothesis refinement/testing operations not represented by a generic model tool-call loop. Broad tool registration includes namespace, context, contradiction, causal-link, hypothesis, goal and failure handlers. Listing these affordances establishes neither current client grants nor exercised use. [SRC-1: `cmd/cli/commands.go`, `cmd/cli/main.go`, `cmd/cli/mcp.go`, `internal/brain/brain.go`]

### Maintenance ownership, admission and recovery

Manual CLI consolidation, the MCP consolidation tool, the standalone ticker, the optional MCP background ticker and the combined `serve` driver converge on `ConsolidateByID`. Each ticker iterates resolved namespace IDs; manual callers can overlap with service calls. The inspected drivers do not establish cross-process exclusive ownership. The combined driver starts HTTP health/metrics, MCP SSE and maintenance in separate goroutines; one child's logged error does not itself cancel its siblings. Source includes metrics and result counters, but these are instrumentation, not run evidence. [SRC-1: `cmd/cli/consolidate.go`, `cmd/cli/mcp.go`, `cmd/cli/serve_all.go`, `internal/brain/consolidate.go`]

The eight-stage orchestration performs episode-to-fact synthesis, relationships, causal links, goal progress, failure patterns, abstractions, hypothesis evidence scanning and confidence decay. Each stage is guarded by context cancellation. Stage errors accumulate in `result.Errors`, and the top-level method can still return a nil error. A report or log saying consolidation completed therefore does not imply all stages succeeded. Progress is saved even on cancellation, using a background context then; writes already made are not rolled back as one transaction. The CLI dry-run branch only prints that dry-run was requested; it does not calculate a preview of prospective model output. [SRC-1: `internal/brain/consolidate.go`, `cmd/cli/consolidate.go`]

Admission is split between model proposals and symbolic checks. In stage one code fetches a checkpointed batch, clusters episode vectors by threshold, sends each cluster's text to the reasoner, parses a structured fact, applies a lexical anti-copy validator, embeds a nonempty summary, checks similarity deduplication, inserts a fact with computed confidence, and adds provenance associations. Code can reject malformed responses, near-copies, provider failures or duplicates; no human content veto is wired into this path. The requested extraction policy is natural language, while retry count, SQL insertion and threshold comparisons are symbolic. Subsequent fact reads can deliver the admitted content to an external agent. Parameter mutation is not performed by these adapters; component fixity limits are in [RT-CMP-openai-reasoner](#rt-cmp-openai-reasoner) and [RT-CMP-openai-embedder](#rt-cmp-openai-embedder). [SRC-1: `internal/brain/consolidate.go`, `internal/reasoner/openai.go`]

### Load-bearing controls and forcing cases

**Extraction grounding.** Owner: reasoner adapter. Enforcement points: JSON decoding and `validateFactGrounding` in `ReasonStructured`, at most two application-level attempts. Guarantee strength: policy for extraction-only semantics; invariant only for the explicit rejection predicates on responses processed through this validator. Covered path: structured-fact synthesis, reached by every inspected consolidation driver. Alternate model methods have their own validation and are not covered by this function; direct remember and caller-supplied object writes bypass it. Required external contract: a chat-completions-compatible response from the configured model service. implementation conclusion status: wired. operation conclusion status: uninspected. Semantic faithfulness conclusion status: claimed. The forcing case is a fabricated but novel summary: the validator tests copying, not whether each assertion follows from the events, so its name cannot support a universal grounding guarantee. See [RT-RTE-consolidation-run](#rt-rte-consolidation-run). [SRC-1: `internal/reasoner/openai.go`, `internal/brain/consolidate.go`]

**Namespace selection, not caller isolation.** Owner: Brain; enforcement: path validation, parameterized slug lookup, escaped LIKE descendant patterns and namespace IDs passed into SQL. Guarantee strength: invariant for these selectors' literal matching under PostgreSQL's SQL semantics, not a deployment guarantee of tenancy. Covered paths include recall and maintenance's namespace resolution. `/` deliberately resolves all namespaces; direct object-ID operations such as `GetEpisode` and `PurgeEpisode` do not use this selector. MCP handlers and the SSE setup inspected here carry no caller-to-namespace authorization check; external access controls remain deployment responsibilities rather than an inferred grant policy. implementation conclusion status: wired. operation conclusion status: uninspected. Client exposure and deployed isolation conclusion status: uninspected. [SRC-1: `internal/brain/brain.go`, `internal/brain/episode.go`, `cmd/cli/mcp.go`]

**Vector compatibility.** Owner: database initializer; enforcement: `validateDimensionLock` and vector-column setup. Guarantee strength: invariant for the dimension-setting comparison when bootstrap succeeds under its database contract, not embedding semantic compatibility. Covered paths: shipped commands sharing bootstrap. Alternate: switching to a different model with the same dimension is explicitly allowed, and recall SQL does not filter results by embedding-model identity. Required external contract: PostgreSQL/pgvector storage and an embedding service returning appropriate dimensions. implementation conclusion status: wired. operation conclusion status: uninspected. Semantic model compatibility conclusion status: uninspected. This forcing case disproves treating model metadata as a frozen model-version lock. [SRC-1: `internal/db/db.go`, `internal/queries/recall.sql.tmpl`]

> // This allows switching between different embedding models as long as they have the same dimension.
> --- `internal/db/db.go`

**Working-focus expiry.** Owner: context API; effect boundary: one persisted focus per exact namespace. Guarantee strength: no claimed guarantee of read-time expiry enforcement in the inspected route. MCP sets an expiry one hour ahead, but `GetContext` selects by namespace ID without an expiry predicate. An expired row remains deliverable through this getter unless some other operation clears it. The forcing case distinguishes carrying expiry metadata from enforcing TTL; no actual expired-row run was observed. implementation conclusion status: wired. operation conclusion status: uninspected. See [RT-RTE-context-handoff](#rt-rte-context-handoff). [SRC-1: `cmd/cli/mcp.go`, `internal/brain/context.go`]

### Capability, grants and deployment

The capability surface is the fixed Go command/tool registry, SQL writes and configured outbound embedding/chat requests. The inspected structured model request supplies messages and a model name, not provider-native tools, callbacks, remote workers or a model-controlled shell. This statement covers that request, not every dependency or future extension. External MCP clients can have independent shell or host capabilities; their execution and approvals are outside Stash's responsibility. Current connected clients, grants, credentials and network policy were not supplied. SSE listens on configured host/port and uses the same write-capable registry as stdio; namespace names alone are not security principals. [SRC-1: `internal/reasoner/openai.go`, `cmd/cli/mcp.go`, `cmd/cli/main.go`]

The shipped Compose configuration publishes port 8080, enables background consolidation and retains PostgreSQL in a named volume. The Dockerfile specifies a nonroot distroless image. These are deployable settings, not inspected deployment isolation or operational persistence guarantees. Database durability depends on PostgreSQL and the configured storage; provider privacy/availability is external. Product changes enter through source releases/builds, not through the memory model selecting new executable code; the inspected release route is [RT-RTE-release-build](#rt-rte-release-build). Self-knowledge prompts can ask an external agent to revise behavior using retained `/self` content, but delivery is not evidence of activation, improved capacity or exercised self-improvement. [SRC-1: `docker-compose.yml`, `Dockerfile`, `.github/workflows/release.yml`, `cmd/cli/mcp_prompts.tmpl`]

## Shared records

### Components

#### RT-CMP-openai-reasoner
Label: OpenAI reasoner adapter

Source-native identity: `reasoner.OpenAI`, configured by `buildReasoner`. The operative model is distributed-parametric, hosted behind an OpenAI-compatible endpoint; its parameters' storage substrate is external provider machinery, uninspected here. The Go adapter and messages are symbolic and natural-language interfaces, not the weights. Parameters do not change through the inspected adapter's operational requests; provider-internal updates are uninspected. Exact model version is not pinned by source: model and base URL are environment values, and a mutable endpoint/model alias can resolve to a different model. No supplied configuration identifies an immutable deployed model. [SRC-1: `internal/reasoner/openai.go`, `internal/bootstrap/bootstrap.go`, `internal/config/config.go`]

> Model:    o.model,
> Messages: msgs,
> --- `internal/reasoner/openai.go:156-162`

#### RT-CMP-openai-embedder
Label: OpenAI embedding adapter

Source-native identity: `embedder.OpenAI`, wrapped by `embedder.Cached`. Distributed-parametric embedding model weights reside at the configured provider, not in PostgreSQL. Emitted dense vectors are separate numerical representations stored in episodes/facts/cache. The inspected route does not train or update weights. Exact version is not pinned: the required model string is passed through unchanged, and a mutable endpoint can change its resolution. Persistent cache keys use text hash and model string, not endpoint identity or immutable model revision; a changed endpoint under the same model label is not guaranteed to invalidate cached vectors. Provider-internal parameter mutability is uninspected. [SRC-1: `internal/embedder/openai.go`, `internal/embedder/cache.go`, `internal/config/config.go`]

> "SELECT embedding FROM embedding_cache WHERE text_hash = $1 AND model = $2",
> --- `internal/embedder/cache.go`

### Operative objects

#### RT-OBJ-server-description
Label: MCP server description protocol

Source-native identity: template `server_description` in embedded `mcp_prompts.tmpl`, rendered into the MCP server description. Representational form: natural-language instructions, compiled into the executable as template text; storage substrate: shipped source and binary, not an operation-updated memory row. It prescribes initialization, recall, high-signal storage, maintenance and `/self` use. Tool names/parameters are separately symbolic API schema. This record owns the protocol, not its retained memory payloads. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`]

> server.WithDescription(render("server_description")),
> --- `cmd/cli/mcp.go`

### Routes

#### RT-RTE-remember-write
Label: Caller episode admission

Caller → MCP `remember` or CLI `remember` → Brain validation/exact namespace lookup → embedding cache/provider → episode insertion → ID. Trigger is an open caller request. Caller proposes and chooses content; original human versus agent authorship is unresolved. Brain owns insertion and can reject invalid input, missing namespace, embedding/DB errors; there is no per-content human approval gate. Guidance to store durable signal comes from [RT-OBJ-server-description](#rt-obj-server-description), but the Go route does not evaluate that criterion. No answer oracle is used. Operating mode: open requests, not a bounded experiment. Recovery is caller retry; later forget/purge are distinct controls rather than atomic rollback. The episode contains natural-language text plus separately produced dense vectors and symbolic metadata in PostgreSQL. [SRC-1: `cmd/cli/commands.go`, `cmd/cli/mcp.go`, `internal/brain/episode.go`]

- Immediate return: Inserted episode ID and success message; failures return an error.
- Later read-back: Episode text can be selected by later recall and fed to consolidation.
- Delegated visibility: MCP returns JSON text to its external caller; other callers sharing the database can query selected namespaces.
- Selection predicate: Caller supplies content and exact namespace; Brain requires an existing slug and validates input before insertion.
- Invalidation or expiry: Forget soft-deletes a semantic nearest episode; purge deletes an ID. No write-time episode expiry is specified here.
- Activation or effect: SQL admission is wired; later behavioral use of the text is unobserved.
- Evidence limits: Original author identity, actual successful writes and downstream benefit were not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> nsID, content, pgvector.NewVector(vec), b.embedder.Model(), occurred,
> --- `internal/brain/episode.go`

#### RT-RTE-recall-read
Label: Semantic memory delivery

Caller query and namespaces → query embedding → subtree resolution → fact query → remaining-slot episode query → sorting → JSON/tool text. Brain owns deterministic sequencing; numerical similarity supplies ranking, not a generative answer decision. The external agent decides whether/how to use the result. No reference-answer oracle or admission decision is involved. Working-context contribution is demand-based reloading of selected external material, not Stash trimming the caller's message window. [SRC-1: `internal/brain/recall.go`, `internal/queries/recall.sql.tmpl`, `internal/brain/brain.go`, `cmd/cli/mcp.go`]

- Immediate return: IDs, namespaces, content, scores, types and available confidence/timestamp fields serialized to the caller.
- Later read-back: This route is itself later read-back of retained episodes/facts; returned text is not additionally persisted by recall.
- Delegated visibility: MCP delivers to its external caller; propagation into any sub-agent or final answer is uninspected.
- Selection predicate: Query vector and resolved namespace subtrees; nondeleted rows with embeddings; facts fill up to limit first, episodes fill remaining slots. Limit defaults to 10 and caps at 100.
- Invalidation or expiry: SQL excludes deleted rows; inspected recall SQL has no validity-time or embedding-model filter.
- Activation or effect: Selected content is delivered; compliance with retrieved standing instructions and answer changes remain unobserved.
- Evidence limits: No retrieval-quality evaluation, successful invocation or client-side context policy supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> episodeLimit := limit - len(results)
> --- `internal/brain/recall.go`

#### RT-RTE-consolidation-run
Label: Model-driven consolidation admission

Manual/tool/timer trigger → namespace IDs → progress row → ordered maintenance stages → progress save → result counters/errors. Brain owns stage selection and cancellation checks, with the model proposing semantic output inside each model-dependent stage. Mode is maintenance over retained batches, not a curriculum or reference-outcome experiment. The detailed admission witness is episode-to-fact: model proposes a structured summary under extraction/synthesis guidance; code checks JSON and copying, embeds, deduplicates and inserts. Empty summaries consume the cluster without adding a fact; duplicates also count as processed. The model does not choose executable tools. No human content approval or independent answer oracle is wired into this witness. [SRC-1: `internal/brain/consolidate.go`, `internal/reasoner/openai.go`, `cmd/cli/consolidate.go`, `cmd/cli/mcp.go`]

Guidance applies the static extraction-only prompt and a structured synthesis request. What persists is a fact summary, entity/property/value metadata, embedding, confidence and source links; the stage does not rewrite its prompt or weights. Rejection can arise from decoding, anti-copy validation, API/DB errors or duplicate similarity. Application-level retry is at most two model attempts, with a warning appended after parse/grounding failure. Stage-one checkpoint advances only when its collected errors are empty; already admitted facts remain on failure and deduplication can affect replay. Provenance insertion errors are ignored in this stage, so completed fact insertion is not an invariant of complete provenance. No atomic all-stage rollback is wired. Content-specific revisions of hypotheses, patterns and contradictions require the specialists' findings; merely naming those stages here does not establish formulated criticism or a theory-builder cycle. [SRC-1: `internal/brain/consolidate.go`, `internal/reasoner/openai.go`]

- Immediate return: ConsolidationResult with counts, duration and accumulated errors; early progress failure can return an error.
- Later read-back: Admitted facts are available through recall/query paths; saved checkpoint determines later maintenance input.
- Delegated visibility: Tool/manual callers receive summaries; timer drivers log results rather than unsolicited memory payloads to a foreground agent.
- Selection predicate: Namespace resolution and checkpointed episode batch, vector clustering and dedup thresholds; subsequent stages use their own checkpoints.
- Invalidation or expiry: Pipeline includes contradiction handling and confidence decay; detailed revision predicates are not fully inspected in this runtime member.
- Activation or effect: Facts and progress writes are wired; successful extraction, client activation and improvement are unobserved.
- Evidence limits: Only stage-one admission is traced in detail here; no run proves all stages succeed or generated claims are true.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if float32(matches)/float32(len(summaryWords)) > 0.80 {
> return fmt.Errorf("summary is too close to a verbatim copy of source text")
> }
> --- `internal/reasoner/openai.go`

> if len(errs) == 0 && maxID > cp.LastEpisodeID {
> cp.LastEpisodeID = maxID
> }
> --- `internal/brain/consolidate.go`

#### RT-RTE-context-handoff
Label: Namespace focus replacement and reload

Caller `set_context` → exact namespace validation/lookup → PostgreSQL upsert; later `get_context` → exact-namespace row → tool JSON; `clear_context` → deletion. The caller proposes and chooses focus; code admits/rejects by input/namespace and database success, without a semantic judge or human approval step. Mode: open handoff requests; no answer oracle. Guidance distinguishes active work from durable recall. Focus is natural language; namespace identity, timestamps and upsert rules are symbolic. This is externally stored working context, not a private sub-agent frame or a host compaction mechanism. Stash does not determine which prior messages the caller removes, and it reloads focus only on request. [SRC-1: `internal/brain/context.go`, `cmd/cli/mcp.go`, `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/main.go`]

- Immediate return: Set/clear acknowledge success; get returns focus row or an empty focus payload.
- Later read-back: The single namespace focus survives in PostgreSQL for a later get invocation.
- Delegated visibility: External caller receives focus; other clients requesting the same namespace can receive the same row. No per-session focus key appears in this API.
- Selection predicate: Exact namespace ID, not descendants or vector search.
- Invalidation or expiry: Set replaces focus; clear deletes it. MCP stamps one-hour expiry, but getter does not exclude expired rows. CLI exposes an expiry duration.
- Activation or effect: Persistent focus replacement/reload is wired; resumed work behavior remains unobserved.
- Evidence limits: No expired-row or restart trace; no inference that this API enforces caller-window eviction or TTL.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> FROM contexts WHERE namespace_id = $1`,
> --- `internal/brain/context.go`

#### RT-RTE-release-build
Label: Release product and machinery admission

Published GitHub release event → workflow checkout/build matrix → binary upload → dependent multiarch image build/push. Source maintainers propose source changes; publishing a release triggers this automation. The workflow does not identify review/branch-protection or human approval rules, so actual admission authority beyond the release event is unresolved. Operating mode: release automation, no model proposal and no answer oracle. Build errors can reject the job; Docker publication depends on binary-build completion. Binary/source templates persist in published artifacts; this is product/machinery admission, separate from retained knowledge admission. Database initialization subsequently runs embedded Goose migrations against an operator-configured database. No workflow-level automatic rollback/deployment or data-recovery guarantee is established by these files. [SRC-1: `.github/workflows/release.yml`, `Dockerfile`, `internal/db/db.go`]

- Immediate return: CI job results, uploaded release binaries and registry images on successful build/publication.
- Later read-back: inapplicable — compiled code and embedded prompts are deployed static products, not use-accumulated memory read-back.
- Delegated visibility: Release assets and registry images become available to consumers; actual downloads/deployment are unobserved.
- Selection predicate: Published-release event, checked-out source and architecture matrix; Docker tags include semver variants and latest.
- Invalidation or expiry: Product replacement requires another build/deployment; rollback policy is uninspected, and database schema recovery is not provided by this release workflow.
- Activation or effect: Publication automation and bootstrap migration calls are wired; live product replacement and migration success were not observed.
- Evidence limits: Maintainer approval policy, runner security, publication results and deployed versions are outside the supplied evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if err := goose.Up(sqlDB, "migrations"); err != nil {
> return nil, fmt.Errorf("goose.Up: %w", err)
> }
> --- `internal/db/db.go`

### Claims

#### RT-CLM-session-protocol
Label: Mandatory memory session protocol

Claimed operation: external agents initialize first, recall before history-dependent answers, periodically consolidate and save a session summary. Source is the shipped natural-language MCP description, not a code-enforced order. The remember/recall handlers themselves invoke Brain directly without a prior-init state check. Hence the server delivers a protocol but does not establish adherence or guarantee a correctly remembered answer. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`]

> 2. You MUST read from Stash BEFORE answering anything with history.
> --- `cmd/cli/mcp_prompts.tmpl`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-extraction-policy
Label: Extraction prompt authority

Consumer: configured reasoner model in `ReasonStructured`. Channel: chat-completion system message plus user synthesis prompt. Force: natural-language guidance, then symbolic JSON/anti-copy checks and database admission; not an invariant of factual correctness. Horizon: each maintenance model invocation; the prompt remains compiled/static across deployments of this build. Accepted content can later reach recall, but external behavioral activation is unobserved. [SRC-1: `internal/reasoner/openai.go`, `internal/brain/consolidate.go`]

> - Extract ONLY what is explicitly stated in the provided text.
> --- `internal/reasoner/openai.go`

#### RT-BAP-agent-protocol
Label: MCP description authority

Consumer: external MCP client/agent. Channel: server description rendered from [RT-OBJ-server-description](#rt-obj-server-description). Force: advisory natural-language instructions phrased as requirements; actual client interpretation and higher-level instruction precedence are outside the target. Horizon: requested session-wide behavior and later sessions using the same server. Retained memory can carry preferences or standing instructions when the caller recalls them, but neither the protocol nor successful tool delivery establishes compliance. [SRC-1: `cmd/cli/mcp.go`, `cmd/cli/mcp_prompts.tmpl`]

> When user or project history may matter, read from Stash before answering.
> --- `cmd/cli/mcp_prompts.tmpl`

## Annotations

none
