---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Origin runtime baseline: daemon-owned capture, scheduled organization, page admission and later recall at the frozen Wenlan revision."
run-id: AAS-2026-10-15-origin-805d03bc599f-01
reviewed-boundary: "61b462ea6adf019b3e27d3f58ac5a0fe055f76b1"
---

# Origin runtime report

## Runtime account

Origin, branded Wenlan in this checkout, is a local knowledge service, not the enclosing conversational agent. Its consequential work is admitting source material, organizing it into memories and pages, and delivering selected retained content to humans and AI clients. The [boundary](boundary.md) fixes SRC-1 and the whole-system scope. All findings below concern inspected implementation or attributed instructions at that revision. No program, model, test or example was executed. Activation, operational reliability and benefit remain unobserved.

### Entry paths and ordinary invocation

The daemon owns the database and automatic work. Startup acquires a data-root lock, prepares state, registers optional workers, starts the scheduler unless repair recovery prevents it, then enters serve-and-drain. The desktop can spawn a daemon sidecar; its API module supplies HTTP operations. The CLI recall command uses the HTTP client. MCP defaults to stdio and also ships Streamable HTTP; the optional relay connects OAuth queries to device reverse connections. These are distinct callers and transports, not independent implementations of all knowledge processing (SRC-1, `crates/wenlan-server/src/main.rs`, `app/src/lib.rs`, `app/src/api.rs`, `crates/wenlan-cli/src/commands/recall.rs`, `crates/wenlan-cli/src/client.rs`, `crates/wenlan-mcp/src/main.rs`, `relay/src/worker.ts`).

An ordinary agent capture begins when the external agent invokes MCP with content and optional classification, space, confidence, entity, structured fields or supersession target. MCP resolves agent identity from explicit input where supported, initialized client name, then configured name; capture itself calls that resolver without an explicit override. It computes effective space and posts a store request. The handler resolves the write space, rejects content shorter than ten trimmed characters and duplicate content, validates a supplied memory type, assigns a `mem_` identity, resolves trust, and constructs a document. Classification and extraction are deferred, not synchronously delegated to a generative model. The batcher applies admission and coalesced storage; a degraded path applies the quality gate synchronously. Failure is returned rather than represented as durable success. On successful storage the handler records activity and a write signal, then returns a persisted receipt and enrichment status. See [RT-RTE-capture-store](#rt-rte-capture-store).

Later, the scheduler selects a due phase or maintenance stage, subject to background-AI configuration and resource/quiet/cooldown admission. It supplies budgeted provider handles, awaits a slice and persists a progress cursor. Its principal is the daemon's automatic worker, not a human approving each generated item. Page synthesis uses selected source snippets and a task prompt; model text becomes a candidate, not an unconditional database write. The shared refresh core performs citation processing before invoking the page-write path. See [RT-RTE-ambient-work](#rt-rte-ambient-work) and [RT-RTE-page-refresh](#rt-rte-page-refresh).

A subsequent invocation can request recall through MCP or CLI. Server code resolves read scope, searches, optionally reranks, separates page rows, logs accessed memory IDs and query activity, adds gated supplemental pages when appropriate, and filters supplemental page references through the truth grant. MCP standard mode delivers a reduced hit projection plus supplemental-page text; query-only mode uses another structured projection. CLI table output is a title/score/ID summary rather than full source text. The external recall skill requests query rewriting and agent-side reranking, but following that instruction belongs to the host agent. See [RT-RTE-recall-search](#rt-rte-recall-search) and [RT-BAP-recall-skill](#rt-bap-recall-skill).

### Three forcing cases and bounded guarantees

1. **Storage without a chosen generative model.** The store path still admits and retains material; its return can report background organization as off or paused. Thus “capture runs intelligence immediately” is false for the inspected path. Storage/retrieval mode still depends on embedding infrastructure, so “no generative model” must not be inflated to “no model dependency.” The owner and enforcement point are the store handler and its effective-route status construction; the status is an implementation protocol, not proof of eventual enrichment. See [RT-RTE-capture-store](#rt-rte-capture-store) and [RT-CMP-text-embedding](#rt-cmp-text-embedding).

2. **Reduced-trust correction versus append or unnamed local write.** Store stages a superseding write from a less-than-full-trust agent; it does not stage every agent write. Appends are not subject to this proposal predicate, and an unknown identity is assigned full trust as a first-party local write. This is a selective destructive-change policy, not universal human approval or authenticated attribution. The owner is the daemon; the enforcement point is `pending_revision` construction, with storage/read behavior described in the handler's contract. Actual deployed callers, headers and trust assignments are unavailable. MCP query-only refusal is a different control: its pre-dispatch allowlist governs that MCP instance, not direct daemon access or local file editing. See [RT-RTE-capture-store](#rt-rte-capture-store) and [RT-RTE-remote-query](#rt-rte-remote-query).

3. **Machine refresh of human-owned pages versus user-forced rebuild.** The page-write CAS loop rechecks ownership. Ordinary machine writes stage a revision card for user-edited or authored pages. A user-forced rebuild may override the user-edited flag, but an authored page remains protected by staging. Refresh captures a source revision and page incarnation, but body-write enforcement differs by branch. Only `UserForced` without candidate sources carries both into `PageWrite::UserForcedUpdate`; ordinary refresh and the candidate-source alternative use `update_page_at_source_revision`, which carries the source counter without the captured incarnation. Their source-revision fence does not establish detection of deletion/recreation under a reused ID with matching counters. These are branch-scoped implementation invariants, conditional on callers reaching the corresponding path with the correct writer identity; they are not a filesystem sandbox or a semantic truth guarantee. Human filesystem edits enter a different admission path. See [RT-RTE-page-refresh](#rt-rte-page-refresh) and [RT-RTE-filesystem-edit](#rt-rte-filesystem-edit).

The scheduler's one-call guarantee is narrower still: an atomic provider facade forwards at most one `generate` request across the handles sharing its counter in an automatic slice. The scheduler owns that invariant and instantiates shared counters. Explicit direct provider calls, the shared synthesis function invoked outside the scheduler, and a provider's internal implementation are not covered by that facade. The external provider contract is one interface request returning text; no inference about internal provider calls follows. See [RT-RTE-ambient-work](#rt-rte-ambient-work).

For page synthesis, the gate rejects zero verified citation occurrences or a majority unverified. “Verified” here uses bidirectional lexical overlap, with sentence-to-paragraph fallback, not an answer oracle or semantic entailment proof. The guarantee strength is an implementation admission invariant at `synthesize_candidate_body`, with a best-effort evidential interpretation. Other page writes, including human edits, do not establish coverage by this synthesis-specific gate (SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`, `crates/wenlan-core/src/citations.rs`).

### Context, authority and change surfaces

Working context is built per inference request, rather than managed as a single long conversational transcript by this service. Page refresh reloads source contents, numbers them, caps each snippet and combines them with the compilation prompt. This keeps excess source text out before model invocation; omitted text remains in the store and can be fetched by another request. Provider output limits and synthesis limits bound work but do not establish host-session compaction. The external recall skill additionally selects a small user-facing subset. These are selection and projection controls, not demonstrated model compliance (SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`, `crates/wenlan-core/src/llm_provider.rs`, `plugin/skills/recall/SKILL.md`).

Natural-language prompts guide generated proposals; symbolic code decides scheduling, grants, admission and mutation. Distributed-parametric inference components are separately recorded below. The inspected inference paths do not implement parameter training; downloaded artifact identities and configurable remote model names must not be treated as one globally immutable model. Retained knowledge can change without changing weights.

Knowledge changes enter through capture, automatic organization, explicit page operations and filesystem edits. Prompt override files also admit changes to future task guidance. Software determines capture admission and ordinary machine-page staging; human edits directly supply replacement prose, while a human review decision can accept or dismiss a staged proposal. Starting capture or a distill cycle is not approval of every resulting content item. The runtime report leaves the detailed memory revision graph and review semantics to the specialists. The MCP source also exposes explicit lint repair prepare/apply/verify, refinement acceptance and brief operations; detailed repair admission and artifact semantics were not traced here, so no universal claim about their gates is made (SRC-1, `crates/wenlan-mcp/src/tools.rs`). No inspected route establishes self-modification of executable product code or an autonomous theory-building loop.

Capability surface, grants and isolation are different. A standard local MCP connection offers mutations as well as reads; HTTP withholds designated local-only operations; query-only dispatch narrows the set further. The daemon API and filesystem remain alternate surfaces. Local deployment credentials, OS permissions, selected model endpoints and active trust/grants are not supplied, so neither a current grant set nor a deployed isolation envelope is established. The Claude CLI provider requests no allowed tools and no session persistence; that is a subprocess invocation contract, not an audit of the external CLI or OS isolation (SRC-1, `crates/wenlan-mcp/src/tools.rs`, `crates/wenlan-mcp/src/main.rs`, `crates/wenlan-core/src/llm_provider.rs`).

Added SRC-1 coverage beyond the boundary's initial inspection includes provider request construction and version reporting, embedding initialization, reranker constructors, page-update ownership enforcement, refresh branch dispatch and terminal database fence arguments, citation scoring, MCP pre-dispatch gates, CLI response rendering, and prompt override admission. Each supplies implementation evidence; recall instructions supply doctrine/design. Available but not fully traced here: source-import adapters, all automatic phase internals, direct model/grammar variants, lint repair transactions, app-specific review/claim-attestation behavior, relay authorization helpers and evaluator modes. These limits prevent exhaustive permission, change-admission, provider and quality conclusions; they are not access gaps or evidenced absences.

## Shared records

### Components

#### RT-CMP-text-embedding
Label: TextEmbedding

SRC-1, `crates/wenlan-core/src/db.rs`: the normal database initializer constructs FastEmbed `BGEBaseENV15Q`, wrapped in a shared mutex. Representation is distributed-parametric ONNX inference state and dense embeddings; substrate is downloaded/cache-backed model files plus in-process inference state and database vectors. The inspected construction/inference integration supplies no weight-update mechanism. Exact model bytes are not pinned by the enum shown here; live cache provenance is uninspected. This is a local artifact loader, not a mutable remote inference endpoint; later artifact resolution can differ unless separately pinned.

> let opts = InitOptions::new(EmbeddingModel::BGEBaseENV15Q)
> --- `crates/wenlan-core/src/db.rs:5200-5220`

#### RT-CMP-cross-encoder-reranker
Label: CrossEncoderReranker

SRC-1, `crates/wenlan-core/src/reranker.rs`: optional distributed-parametric cross-encoder inference, held as a mutex-protected FastEmbed `TextRerank`. Construction accepts a model enum or user-provided ONNX directory and tokenizer files. Model identity strings are not immutable artifact digests. Parameters are loaded for inference; no operational training is established by these paths. No remote inference endpoint is involved in these constructors, but downloaded or user-replaced artifacts may resolve differently on a later load. The no-op alternative is symbolic passthrough, not another learned component. Missing reranker wiring can fall back to ordinary search (SRC-1, `crates/wenlan-server/src/memory_routes.rs`).

#### RT-CMP-on-device-provider
Label: OnDeviceProvider

SRC-1, `crates/wenlan-core/src/llm_provider.rs`: distributed-parametric local generative inference, backed by downloaded/cached model files and an in-process engine. Registry resolution selects the model; construction obtains a snapshot-derived version and refuses a model path without that provenance. This identifies a loaded artifact more precisely than a model nickname, but the reviewed repository does not fix which deployed selection or snapshot was used. Inspected operations load/reload inference engines, not train parameters. There is no remote inference endpoint for this component; future configured selection/download can choose another artifact.

#### RT-CMP-api-provider
Label: ApiProvider

SRC-1, `crates/wenlan-core/src/llm_provider.rs`: remote distributed-parametric generation behind the Anthropic messages API. The component holds a configured model string and key in process; provider weights and retained internals are external/uninspected. Requests provide user text, optional system text and output budget. Exact weights are not pinned by this adapter; the service/model name can resolve to changed internals. Whether provider parameters change during operation is uninspected, not established absent.

#### RT-CMP-openai-compatible-provider
Label: OpenAICompatibleProvider

SRC-1, `crates/wenlan-core/src/llm_provider.rs`: distributed-parametric generation via a configured `/chat/completions` endpoint, local or remote, with optional bearer key. Adapter configuration is in memory; weights and server storage are outside the inspected component. A configurable endpoint and model name can resolve to another model, with no immutable model-version guarantee shown here. Provider-side updates are uninspected; the adapter itself constructs inference requests rather than training weights.

#### RT-CMP-claude-cli-provider
Label: ClaudeCliProvider

SRC-1, `crates/wenlan-core/src/llm_provider.rs`: model access through the external `claude` subprocess, with model string, system prompt and stdin user text. Distributed parameters and their persistence are external; the local adapter retains process configuration and receives stdout. Exact weights are not pinned, a model alias can resolve differently, and provider-side parameter mutation is uninspected. The command requests no session persistence and empty allowed tools; it removes the API-key environment variable to select the external CLI's other authentication path. Availability and actual tool isolation are not observed.

> "--no-session-persistence".to_string(),
> "--allowedTools".to_string(),
> "".to_string(),
> --- `crates/wenlan-core/src/llm_provider.rs`

### Operative objects

#### RT-OBJ-prompt-registry
Label: PromptRegistry

Natural-language task instructions in compiled defaults or override text files, loaded into Rust strings. Symbolic field names and loader rules select which text becomes task guidance; model interpretation supplies its behavioral effect. File substrate is the configured data root's `prompts` directory. Consumer roles include classification, extraction, reconciliation, page compilation and context compression by registry field; listing a field does not establish every consumer's execution. SRC-1, `crates/wenlan-core/src/prompts/mod.rs`. Admission is [RT-RTE-prompt-override](#rt-rte-prompt-override).

### Routes

#### RT-RTE-capture-store
Label: MCP capture to durable store

Owner and progression: external agent proposes content; MCP translates it; the daemon resolves space and trust, constructs the memory identity and runs admission before database upsert. Symbolic validation, quality-gate outcome and trust predicate decide admission, not an answer oracle. Mode: open user/agent capture. The software can reject short/duplicate/invalid/gate-failing input; less-than-full-trust supersession is staged, not automatically applied. An anonymous local write receives full trust. This is not per-content human approval. The batcher and synchronous fallback are material equivalent store paths, both running the quality gate; the fallback maps gate errors to rejection. Origin-bearing source-agent values and page-card markers are normalized/stripped before persistence. The handler cleans enrichment-origin metadata on enumerated admission failures. Subsequent deletion/correction is a recovery surface, not demonstrated crash rollback. SRC-1, `crates/wenlan-mcp/src/tools.rs`, `crates/wenlan-server/src/memory_routes.rs`, `crates/wenlan-server/src/main.rs`.

- Immediate return: MCP success/error; a successful store receipt includes source ID, chunk count, warnings, space, gated flag and enrichment state.
- Later read-back: retained admitted documents become candidates for later recall and automatic organization; pending supersession is not promised as live replacement.
- Delegated visibility: daemon receives request fields; optional automatic inference receives selected retained content later, not a current-turn transcript by default.
- Selection predicate: valid resolved space, minimum trimmed length, duplicate/type checks, quality admission and supersession/trust staging predicate.
- Invalidation or expiry: correction/deletion and supersession are separate mutating surfaces; no fixed capture TTL is established by this handler.
- Activation or effect: writes retained document state and signals automatic work; actual later use remains unobserved.
- Evidence limits: implementation and comments, not executed captures or durable-failure tests; complete database revision semantics are deferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let pending_revision = req.supersedes.is_some() && trust_level != "full";
> --- `crates/wenlan-server/src/memory_routes.rs`

> // No agent identified at all → local/first-party write, full trust.
> "full".to_string()
> --- `crates/wenlan-server/src/memory_routes.rs`

> "Stored. Recall is available now; background AI organization is off.".to_string(),
> --- `crates/wenlan-server/src/memory_routes.rs`

#### RT-RTE-recall-search
Label: Retained memory and supplemental page recall

Owner/progression: requester supplies query and optional filters; server resolves scope and chooses ordinary or reranked search; code partitions and gates page delivery; MCP/CLI renders. No answer oracle is used by this handler. Agent-side relevance reranking is a separate instructed judgment, not enforced server behavior. Runtime clients can choose query, limit and optional rerank; the standard MCP projection and query-only projection differ. Source: SRC-1, `crates/wenlan-server/src/memory_routes.rs`, `crates/wenlan-mcp/src/tools.rs`, `crates/wenlan-cli/src/commands/recall.rs`.

- Immediate return: selected memory hits and optional supplemental pages; standard MCP emits text containing projected hits and page JSON, while CLI table mode summarizes.
- Later read-back: this is the later consumer route for retained knowledge; access/query logs persist as telemetry, with no inference here that they revise knowledge.
- Delegated visibility: external agent receives only returned projections, not the whole database; MCP tool text is not an enforced downstream policy.
- Selection predicate: effective scope, query, optional type/agent filter, ranking and limit; fallback supplemental pages additionally use scope/trust visibility, deduplication, a cap of three and final truth-grant filtering.
- Invalidation or expiry: reads reflect current eligible database state; no client-cache expiry is established here.
- Activation or effect: result delivery and access/activity logging are wired; answer changes and benefit are unobserved.
- Evidence limits: database ranking internals and all truth-adapter rules were not exhaustively inspected; no retrieval-quality result is claimed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> wenlan_core::truth_adapter::filter_page_refs(&db, &view.grant, pages, |row| {
>     row.source_id.as_str()
> })
> --- `crates/wenlan-server/src/memory_routes.rs`

#### RT-RTE-ambient-work
Label: Scheduled automatic phase and maintenance slices

Daemon code owns trigger selection, phase progression and provider routing. It selects burst-end, idle, daily, backstop or maintenance work, supplies prompts/configuration and budgeted model handles, and persists cursors after attempts. Models propose content within selected stages; scheduling and call admission remain symbolic. Mode: recurring maintenance of admitted material, not an answer-key experiment. No answer oracle is established by the inspected scheduler. Software can defer work through resource/cooldown/background-AI gates; this is not item-by-item human veto. Knowledge changes are admitted by the selected stage's write path, including page admission in [RT-RTE-page-refresh](#rt-rte-page-refresh). Detailed phase-specific rejection and rollback remain uninspected, so the scheduler is not itself a universal content validator. SRC-1, `crates/wenlan-server/src/scheduler.rs`.

- Immediate return: slice disposition, call accounting and progress/cursor state to the scheduler, not a synchronous result to the original capture caller.
- Later read-back: retained phase effects may be consumed by recall or subsequent maintenance; durable cursors also guide restart progression.
- Delegated visibility: each phase receives database/provider/prompt/configuration handles; exact model-visible content depends on that phase.
- Selection predicate: due trigger, work availability and scheduler admission; selected automatic provider handles share an atomic one-call budget.
- Invalidation or expiry: current configuration can disable background AI before launch; cursors persist across attempts; exact phase retry invalidation varies by worker.
- Activation or effect: code wires automatic phase calls and cursor persistence; operation and model compliance remain unobserved.
- Evidence limits: at-most-one forwarded generate request is a facade invariant, not a bound on remote internals, explicit/manual inference or every daemon task.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> /// Ambient-only provider facade that fails closed after forwarding one LLM
> /// request. The scheduler is serialized today; this guard keeps the thermal
> /// invariant true if a slice later gains a hidden nested call.
> --- `crates/wenlan-server/src/scheduler.rs`

> // Persist after every attempt, including captured errors
> // and panics, so one poison phase cannot pin restarts.
> persist_automatic_phase_cursor(&db, kind, cursor).await;
> --- `crates/wenlan-server/src/scheduler.rs`

#### RT-RTE-page-refresh
Label: Source-backed page synthesis and canonical update

Owner/progression: an automatic source-change sweep or explicit/forced request selects a page; refresh reads its fence and current sources, builds numbered capped snippets, asks the configured provider for candidate prose, then runs citation processing. The page-write path decides whether to mutate, refuse or stage a revision card. Code proposes no expected answer; lexical citation support is an admission heuristic, not an answer oracle. Mode: open knowledge compilation/recompilation. Task prompt and selected source text shape the proposal; accepted prose, provenance and page state persist. Software can discard a candidate; ordinary machine updates to human-owned pages can be vetoed through review. A user-forced rebuild overrides user-edited protection but not authored-page ownership. The concurrency guarantee is branch-specific: `UserForced` without candidate sources dispatches `PageWrite::UserForcedUpdate` with the captured source revision and incarnation. Its terminal body write rejects a changed source revision or replacement incarnation; its later summary update is also incarnation-fenced. Ordinary refresh and the candidate-source alternative dispatch `update_page_at_source_revision`, carrying the source counter but not the captured incarnation. Non-forced writes explicitly refuse an incarnation fence and select a different terminal database operation. Source-revision mismatch can reject obsolete compilation in that branch, but matching counters on a deleted/recreated page do not establish the same protection as forced rebuild. Its later summary update is likewise not incarnation-fenced. Discard markers, in contrast, use the captured full page fence before either body-write branch. Generic wrappers without a compile fence are weaker again; they are not the ordinary refresh route. SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`, `crates/wenlan-core/src/post_write/page_dispatch.rs`, `crates/wenlan-core/src/post_write/page_update.rs`, `crates/wenlan-core/src/db.rs`, `crates/wenlan-core/src/citations.rs`.

- Immediate return: wrote/gated/acknowledged flags, optional revision-card ID or discard reason; not every successful function return means a page changed.
- Later read-back: committed page prose/provenance or a pending review card is durable and available to later page/review consumers; recall still applies its own selection.
- Delegated visibility: provider receives task prompt and numbered source snippets, not necessarily complete source documents; snippet capping occurs before the call.
- Selection predicate: page and reason, current or supplied candidate sources, automatic-reader permit for source-change work, citation gate and page-write CAS/ownership rules.
- Invalidation or expiry: source changes/staleness rearm refresh; changed source counters reject stale body writes. Incarnation mismatch additionally rejects the forced branch without candidate sources, but ordinary/candidate-source body writes lack that check. Discard markers use both fences and are cleared by relevant later writes/stale transitions.
- Activation or effect: verified candidates can reach canonical writes or review cards; measured factuality and downstream activation are unobserved.
- Evidence limits: lexical overlap can accept semantically wrong prose; ordinary/candidate-source refresh has no captured-incarnation body-write guarantee against reused-ID recreation with matching counters. Inspected canonical update coverage does not certify every page writer or external file operation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let user_forced_write = reason == RefreshReason::UserForced && candidate_sources.is_none();
> --- `crates/wenlan-core/src/synthesis/distill.rs`

> if !user_forced && page_fence.is_some() {
>     return Err(WenlanError::Validation(
>         "a page incarnation fence is only carried by a user-forced page rebuild".into(),
>     ));
> }
> --- `crates/wenlan-core/src/post_write/page_update.rs`

> if stats.verified == 0 || stats.unverified > stats.verified {
> --- `crates/wenlan-core/src/synthesis/distill.rs`

> let sentence_verified = bidirectional_support(sentence, &union) >= 0.5;
> --- `crates/wenlan-core/src/citations.rs`

> let human_owned = if user_forced {
>     current.creation_kind == "authored"
> } else {
>     page_is_human_owned(&current)
> };
> --- `crates/wenlan-core/src/post_write/page_update.rs`

#### RT-RTE-filesystem-edit
Label: Markdown projection edit read-back

The human/external editor supplies prose; the daemon watcher scans projected Markdown, resolves page identity and compares normalized bodies. It skips stale projections and uses a source-preserving page update with `fs_edit`. This is content replacement by an external writer, not per-content machine synthesis approval. Software rejects ambiguous identity; the human can replace prose again. Source-list preservation and re-projection maintain the database/projection relationship, but crash recovery effectiveness is unobserved. Mode: open manual editing; no answer oracle or model proposal. SRC-1, `crates/wenlan-core/src/sources/page_watcher.rs`, `crates/wenlan-server/src/scheduler.rs`.

- Immediate return: scan counts and per-file outcomes/logs to the scheduler.
- Later read-back: changed page prose and ownership state reach subsequent database/page reads and machine-write decisions.
- Delegated visibility: watcher reads mapped files; model consumers see content only through later selected routes.
- Selection predicate: known origin ID, non-stale projected version, unique claimant at mapped path and changed normalized prose.
- Invalidation or expiry: old version stamps are skipped; unchanged prose is not rewritten as an edit; source projection may be repaired separately.
- Activation or effect: source-preserving update and re-projection are wired; `fs_edit` is treated as human ownership by the page-update policy.
- Evidence limits: filesystem access control and actual editor identity are external; this is not proof that every file change is human-authored.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if md_version < existing.version {
>     return Ok(Outcome::SkippedDaemonAhead { page_id });
> }
> --- `crates/wenlan-core/src/sources/page_watcher.rs`

#### RT-RTE-prompt-override
Label: Task prompt override loading

An external filesystem writer proposes replacement guidance in a named text file. `PromptRegistry::load` decides syntactically: readable, trimmed nonempty text replaces the default; missing/empty files retain fallback, with selected legacy aliases. No semantic review, human provenance check or answer oracle appears in this loader. Mode: operator configuration, not an automatic improvement experiment. Replacement prose persists on disk; restoring/removing it can recover the default on a later load. Exact hot-reload cadence is uninspected. SRC-1, `crates/wenlan-core/src/prompts/mod.rs`.

- Immediate return: populated registry strings to the caller.
- Later read-back: override files are reloadable task guidance; changing a file does not prove an already-running registry changed.
- Delegated visibility: later prompt-consuming inference paths receive the selected field text.
- Selection predicate: registered field name, canonical filename, readable nonempty trimmed body; legacy alias fallback for selected fields.
- Invalidation or expiry: next load re-evaluates files; no expiry or runtime semantic validator is shown.
- Activation or effect: guidance replacement is afforded by the loader; actual loaded overrides and effects are unobserved.
- Evidence limits: no inspected feedback loop automatically writes these files or proves method improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if !trimmed.is_empty() {
>     log::info!("[prompts] loaded override: {name}");
>     *value = trimmed;
>     loaded = true;
> }
> --- `crates/wenlan-core/src/prompts/mod.rs`

#### RT-RTE-remote-query
Label: HTTP query-only MCP and optional relay

External client initiates MCP; the configured HTTP MCP instance applies profile gates before dispatch. Query-only narrows dispatch to its explicit allowlist; standard HTTP separately denies local-only names. The optional relay's authority object wires OAuth forwarding to reverse-device connections and strips/reconstructs internal headers. The relay implementation examined here establishes routing ownership, not complete authorization correctness. HTTP query-only startup rejects no-auth mode and requires scope configuration. SRC-1, `crates/wenlan-mcp/src/main.rs`, `crates/wenlan-mcp/src/tools.rs`, `relay/src/worker.ts`.

- Immediate return: permitted query response, protocol refusal or unavailable-channel error.
- Later read-back: permitted recall reaches selected retained knowledge via the same daemon; query logging can persist although knowledge mutations are denied by the query-only dispatch profile.
- Delegated visibility: HTTP client receives allowed projections; reverse-device forwarding bridges relay to the device connector.
- Selection predicate: transport, tool profile and explicit name allowlists; actual OAuth grant resolution depends on helpers not fully traced here.
- Invalidation or expiry: relay checks current reverse connection and maintains grant/rate state; exact token lifetime and revocation behavior remain uninspected.
- Activation or effect: dispatch refusal is wired before tool argument handling; live authorized connectivity is unobserved.
- Evidence limits: local stdio, daemon HTTP and filesystem paths remain outside this MCP profile's guarantee; deployed credentials and scope grants are unavailable.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if let Some(refusal) = self.query_only_refusal(request.name.as_ref()) {
>     return Ok(refusal);
> }
> --- `crates/wenlan-mcp/src/tools.rs`

### Claims

#### RT-CLM-ambient-ownership
Label: Automatic enrichment belongs to the scheduler

SRC-1, `crates/wenlan-server/src/memory_routes.rs`, explicitly assigns automatic inference admission and retries to the ambient scheduler rather than request-time spawning. [RT-RTE-ambient-work](#rt-rte-ambient-work) supplies wiring evidence; this does not establish eventual completion under a permanently unavailable pin.

> // Automatic enrichment is intentionally not spawned from the request path.
> // The ambient scheduler owns admission, ordering, retries, and the one-call
> // budget for every automatic inference stage.
> --- `crates/wenlan-server/src/memory_routes.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-recall-skill
Label: Host-agent recall instructions

Consumer: external agent running the shipped recall skill. Channel: natural-language skill text loaded by the host, then MCP tool results. Force: requested query transformation, relevance judgment and presentation policy, not executable enforcement. Horizon: each skill invocation; static shipped guidance is not itself memory accumulated through use. Returned retained memories provide later knowledge context, but compliance and answer effects remain unobserved. SRC-1, `plugin/skills/recall/SKILL.md`.

> Re-read the returned memories against the *original* query. Promote the
> ones that directly answer the question; demote ones that just share
> keywords.
> --- `plugin/skills/recall/SKILL.md`

#### RT-BAP-task-prompts
Label: Registry task guidance to inference

Consumer: inference provider selected for a knowledge-processing task. Channel: registry text copied into the inference request's system prompt, combined with source-derived user text in page refresh. Force: model-interpreted guidance; subsequent code gates determine mutation authority. Horizon: request instance, with defaults/overrides reusable across invocations. Loader and page-refresh evidence establish delivery capacity, not obedience. SRC-1, `crates/wenlan-core/src/prompts/mod.rs`, `crates/wenlan-core/src/synthesis/distill.rs`. Related routes: [RT-RTE-prompt-override](#rt-rte-prompt-override), [RT-RTE-page-refresh](#rt-rte-page-refresh).

> system_prompt: Some(system_prompt.to_string()),
> --- `crates/wenlan-core/src/synthesis/distill.rs:1415-1435`

## Annotations

none
