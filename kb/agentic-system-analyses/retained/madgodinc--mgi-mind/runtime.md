---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MGI-Mind runtime baseline: assistant-controlled memory calls, service controls, context assembly and optional extraction at the frozen revision."
run-id: AAS-2026-11-08-mgi-mind-e0f02081480f-01
reviewed-boundary: a8defc36f7d0bcd5108714763a12625a0eda0868
---

# MGI-Mind runtime report

## Runtime account

MGI-Mind executes memory operations, not the enclosing assistant's problem-solving loop. An assistant or operator chooses when to call it and what to store or retrieve. The ordinary shipped OpenAI Agents example gives the assistant `remember` and `recall` functions. Those functions call the Python HTTP client; the HTTP server reaches shared Rust storage. The returned text goes back through a host tool result, and the host model decides what to answer. The example invokes the agent once to remember a database address and again to answer a port question. This is implemented demonstration code, not a supplied execution trace ([RT-RTE-assistant-memory](#rt-rte-assistant-memory)).

The capability surface is larger than a deployed grant: the binary exposes direct CLI, stdio MCP and HTTP service modes, plus specialized maintenance, fact, procedure, skill and session commands. A host may register only two wrappers, as the example does, or expose the broader MCP tools. Neither tool descriptions nor the operating manual prove that an assistant uses them. `main` builds a Tokio runtime, parses Clap arguments and dispatches through `cli::run`; MCP reads newline-delimited JSON-RPC serially, while HTTP uses Axum handlers. MCP can advertise tools even when initialization is missing, then return errors on storage calls. CLI/MCP output rendering and HTTP structured output are distinct return surfaces (SRC-1, `src/main.rs`, `src/cli.rs`, `src/mcp.rs`, `src/http_api.rs`).

The source-native purpose is durable assistant memory. The boundary's retained manual quotations establish both agent-authored candidate extraction and the requirement to wire its protocol into a host's rules. Here the principal distinction is between a **requested habit** (search before acting) and **enforced server behavior** (validate this request and persist or return its result). [RT-BAP-host-recall](#rt-bap-host-recall) describes that separation. There is no basis here for treating a recall result as automatically obeyed, true, or beneficial.

### Ordinary invocation and result boundary

For `remember`, the example's model supplies a string. `Memory.add` selects the configured `agent` library and posts `/memory/add`. Without an explicit JSON format that handler calls `mind_add`, which requires library/content and calls `add_memory_authored`. Storage rejects an unregistered library or content matching its secret detector, splits long content, embeds chunks, creates dense and lexical vectors, and upserts Qdrant points with payload metadata. The immediate result is a chunk-count confirmation, not proof of future recall. The sample assumes a working configured server and library; it does not itself create the library (SRC-1, `docs/integrations/openai_agents.py`, `clients/python/mgimind/_client.py`, `src/http_api.rs`, `src/mcp.rs`, `src/storage.rs`).

For `recall`, the example calls `mem.search(query, tier=2)`, not unified recall. The query and metadata filter reach `search_filtered`. Dense and sparse prefetches use the same filter and are fused with reciprocal-rank fusion. Optional cross-encoder scoring reorders full candidate content; a failure leaves the existing fused order, despite comments calling it the dense order. Results are limited and only then display-truncated: tier 1 to 100 characters, tier 2 to 500, otherwise full content. In-process query/access activity is recorded. Python converts the response to text, the host returns it as a tool result, and the external assistant produces `final_output`. Search failure, transport failure, missing models and absent collections have different outcomes; in particular an absent memories collection returns an empty list, while a query/inference error can propagate. No autonomous retry of the enclosing assistant is established ([RT-RTE-assistant-memory](#rt-rte-assistant-memory), SRC-1, `src/storage.rs`, `clients/python/mgimind/_client.py`).

### Forcing cases and guarantee scope

Three source-level challenges change conclusions that a happy path would suggest:

1. **Direct add versus ingest.** Relevance and novelty gating are not universal admission conditions. `mind_add`, CLI add and HTTP add reach storage without `run_ingest_authored`; storage still performs its own library and secret checks. Ingest may quarantine and later promote rather than reject permanently. A failed neighbor query can cause novelty acceptance. Thus the gate is a recoverable selection policy, not a truth guarantee or mandatory human approval ([RT-RTE-ingest-admission](#rt-rte-ingest-admission)).
2. **Scoped HTTP read shapes and formats.** Scope canonicalization considers both `library` and `libraries`, replaces empty or non-object reads with the allowlist, and requires writes to name a permitted singular library. The consumer uses the canonical plural filter. Scoped unified JSON recall suppresses global facts/procedures; text recall is explicitly rejected because its fused dispatcher cannot honor that filter. This is narrower than either “all recall formats are confined” or “the text path bypasses the gate.” The text branch is reachable for unscoped callers, not scoped callers ([RT-RTE-scoped-http](#rt-rte-scoped-http)).
3. **Scoped ingest with optional extraction.** HTTP overwrites `_confine_extraction` and the explicit Fact/Procedure candidate branches honor it. However the accepted Memory branch can enqueue auto-extraction without checking `confine`. Its queue carries config/content, not scope; the worker writes extracted triples through global `knowledge::add_fact`. Therefore explicit-candidate confinement is wired, but global-write exclusion is not a universal invariant in an extractor-enabled installation. A valid scoped memory request can reach that enqueue if relevance/novelty/dedup checks admit it and the extractor installation check succeeds. Actual extraction, emitted triples and successful global writes remain unobserved, not a demonstrated exploit ([RT-RTE-auto-extraction](#rt-rte-auto-extraction)).

The HTTP ACL owner is server code, enforced at route middleware, per-handler authentication and scope rewriting, and ultimately Qdrant filters. Guarantee strength: invariant for the inspected request-shape transformations and explicit rejection branches; best effort for semantic content quality. Implementation conclusion status: wired. Operation conclusion status: uninspected. The contract requires correct Qdrant filter execution and that callers cannot access the storage service or local files independently. The server's supported request paths are not an OS sandbox. CLI, trusted stdio, local maintenance and optional subprocess code do not inherit HTTP token restrictions. No deployed network/filesystem isolation was supplied. `/health` is an unauthenticated handler, so the source's blanket comment about every route needing a token is too broad (SRC-1, `src/http_api.rs`).

Embedding compatibility is another path-specific control: `serve-http` startup propagates `assert_embedding_space` failure, whereas MCP startup warns and continues. Neither service choice proves every direct CLI consumer has passed the same startup check. Reranking is explicitly best effort, not guaranteed output ranking. These guarantees belong to their enforcement paths, not to every product invocation (SRC-1, `src/cli.rs`, `src/mcp.rs`, `src/storage.rs`).

### Other material loops and admission surfaces

Session/context assembly is requested, not unsolicited host injection. `mind_context` builds a text briefing from last-session files, visible facts, pinned blocks, skill catalogue and inventory. The builder uses globally newest session selection (`last(None)`), while the session API supports an agent filter. It preferentially loads skill names/triggers rather than full bodies, and requests on-demand matching. This is a pointer/index-and-reload pattern, not observed host compaction or a separate sub-agent stack frame. For facts, it selects the newest 20 candidates passing valid/status filters, then checks only whether `valid_until` is absent or later than now. It does not check `valid_from` or use the world-time helper; complete stored-interval validity is not established. The builder does not decide what the host subsequently keeps in its context window ([RT-RTE-context-briefing](#rt-rte-context-briefing)).

A named skill can be replaced by caller-supplied text without a per-content human gate; it becomes a later retrieved playbook rather than changing model weights ([RT-RTE-skill-admission](#rt-rte-skill-admission)). Markdown reconciliation treats disk content as the replacement source and deletes existing points before writing replacements; consolidation separately gates mutations on `apply`. These are distinct mechanisms and do not establish one transaction or one universal rollback policy ([RT-RTE-markdown-reconcile](#rt-rte-markdown-reconcile), [RT-RTE-store-consolidation](#rt-rte-store-consolidation)). Fact validity, procedure outcome weighting, transcript ingestion and doubt-window maintenance remain included responsibilities identified in the boundary; their revision semantics belong to the memory/epistemic analyses, not a runtime-wide claim of reliable self-correction. MCP startup wires the background doubt loop; HTTP startup must not be assumed to have identical lifecycle behavior merely because it uses the same dispatcher (SRC-1, `src/mcp.rs`, `src/http_api.rs`, `src/cli.rs`).

Product/production changes are also possible through ordinary source/package deployment and explicit installation/configuration commands. They are not the same as admitting a memory candidate. The repository describes feature-branch PRs and tests in `PROCESS.md`; this is process doctrine, not observed release governance. The inspected executable dispatch offers extractor install/uninstall and local process startup, but this report does not establish model-authored code changes, dynamic extension loading, or automatic deployment based on outcomes. Shipped `fetch` shells out to `crw`; the extractor starts `llama-server`; these are host-process effects rather than remote autonomous workers (SRC-1, `PROCESS.md`, `src/cli.rs`, `src/extractor.rs`, `src/mcp.rs`).

### Evidence and coverage

All source-dependent findings use SRC-1 at the boundary's frozen commit. This report adds implementation inspection of HTTP argument normalization and return branches; MCP direct/ingest dispatch and startup; storage write/search/filter consumers; embedder/reranker loading; extractor queue, installer identity and retry; Python transport and the OpenAI/LangGraph drivers; context assembly; session end/last; skill admission/storage; Markdown apply; consolidation apply. `src/integrity.rs` supplies artifact-pin implementation; `PROCESS.md` supplies doctrine only. These are added coverage within the registered repository, not new sources. No target or tests were executed. Installer completeness, actual artifact identity on disk, full host tool scheduling, framework compatibility, benchmark results and performance benefits remain unobserved here. Included but not deeply traced maintenance and evaluator implementations cannot support exhaustive safety or benefit conclusions. Parameter ownership is separated in the component records below; no external provider internals are inferred.

## Shared records

### Components

#### RT-CMP-embedder
Label: Local embedder

Source-native `embedder` is an ONNX inference session plus tokenizer loaded from `models/<model_name>/`; parameters are distributed-parametric, files are local storage and the process caches a mutex-protected session. Inspected paths infer embeddings and do not train weights. Model name, prefixes and pooling are configurable. Exact deployed bytes are unobserved: default artifact hashes exist in `src/integrity.rs`, but the session loader reads a local file, not an immutable service revision. There is no remote model endpoint in this path; changing configured files can select another model on later process initialization, and the cached session is not reloaded per call. SRC-1, `src/embedder.rs`, `src/config.rs`, `src/integrity.rs`.

> let session = builder
>             .commit_from_file(&model_path)
>             .map_err(|e| anyhow::anyhow!("Failed to load ONNX model: {e}"))?;
> --- `src/embedder.rs`

#### RT-CMP-reranker
Label: Local reranker

Source-native `reranker` is a separately cached ONNX cross-encoder and tokenizer on local disk, selected by `rerank_model`. Distributed-parametric weights score query/passage pairs, with no parameter-update operation in the inspected scoring path. Default BGE artifact hashes exist; deployed file identity is not established. The path is not a mutable remote endpoint, but file/config replacement can change the next process's model. A failed call is swallowed by search, so use is option- and success-dependent. SRC-1, `src/reranker.rs`, `src/config.rs`, `src/integrity.rs`, `src/storage.rs`.

> if let Ok(scores) = crate::reranker::scores(config, query, &texts).await
>             && scores.len() == cands.len()
> --- `src/storage.rs`

#### RT-CMP-extractor
Label: Optional local extractor

Source-native `extractor` runs Qwen GGUF distributed-parametric weights through a local `llama-server` child and authenticated loopback completion calls. Default and Lite artifact hashes are populated even though download URLs use `resolve/main`. The installed bytes/server implementation were not inspected as artifacts. The inference route does not update parameters; prompt repair changes input wording, not weights. The local server endpoint is managed by this process rather than a caller-chosen model API; install/config/file replacement can change future process selection. SRC-1, `src/extractor.rs`, `src/integrity.rs`.

> pub const EXTRACTOR_QWEN_3B_Q4_K_M: &str =
>     "626b4a6678b86442240e33df819e00132d3ba7dddfe1cdc4fbb18e0a9615c62d";
> --- `src/integrity.rs`

#### RT-CMP-host-model
Label: Integration host model

The OpenAI Agents driver's model is owned by the external SDK/provider; LangGraph explicitly names `claude-opus-4-8`. Distributed-parametric state and its storage reside outside inspected source. OpenAI model selection is delegated to SDK defaults, not pinned here; LangGraph's model identifier is not immutable weight provenance. Whether either provider can retarget that identifier, change parameters during service operation or maintain opaque state is uninspected. Host inference determines tool choice and final answers; local memory storage does not establish host parameter training. SRC-1, `docs/integrations/openai_agents.py`, `docs/integrations/langgraph.py`.

> model=ChatAnthropic(model="claude-opus-4-8"),
> --- `docs/integrations/langgraph.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-assistant-memory
Label: Assistant remember and search

The external assistant proposes strings/queries; its tool wrapper owns the handoff to Python HTTP, Rust storage and back. Configured library and optional caller metadata identify scope; durable Qdrant content is distinct from current host messages. Calls operate on open user requests, not a curriculum. The model proposes, server validation decides physical admission, and no per-item human veto or reference-answer oracle is wired in this example. Model instructions request recall/remember; no evidence proves compliance. Storage permits later deletion/editing and exact-content upsert, not atomic undo of all host effects. This admission is distinct from gated ingest in [RT-RTE-ingest-admission](#rt-rte-ingest-admission). SRC-1, `docs/integrations/openai_agents.py`, `clients/python/mgimind/_client.py`, `src/http_api.rs`, `src/mcp.rs`, `src/storage.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Remember returns a storage confirmation; recall returns search results rendered by the Python object, then the host returns its final answer.
- Later read-back: Future search calls can retrieve admitted chunks from Qdrant across assistant invocations.
- Delegated visibility: Host sees returned text, not the whole database or inference internals; wrappers grant only remember/recall in this driver.
- Selection predicate: Configured library plus query hybrid retrieval, optional reranking and limit; tier 2 truncates returned content to 500 characters after ranking.
- Invalidation or expiry: Archive/quarantine filters hide entries from ordinary search; edits/deletion and other maintenance are separate calls, not this wrapper's automatic expiry.
- Activation or effect: Writes and tool-result delivery are wired; changed assistant decisions and improved answers are not observed.
- Evidence limits: Source code only; host implementation, installed service/library, actual tool use and final answer correctness remain uninspected.

> return self._post("/memory/add", _add_body(content, library or self.library, agent or self.agent))
> --- `clients/python/mgimind/_client.py`

> tools=[recall, remember],
> --- `docs/integrations/openai_agents.py`

> cands.truncate(limit);
> --- `src/storage.rs`

#### RT-RTE-ingest-admission
Label: Candidate ingest admission

Caller-proposed tagged candidates or heuristic extraction from raw text feed `run_ingest_authored`. Code selects candidates when supplied, otherwise the heuristic; memory candidates pass secret, cheap relevance, novelty and near-duplicate checks. Quarantine can preserve content for reassertion/promotion. Explicit facts/procedures take different branches, including scoped suppression. The server is admission owner, the caller supplies content and may choose direct add instead. Open-request ingestion uses no expected-answer oracle or mandatory per-content human decision. Cheap rules/neighbor overlap guide selection; preserved material is content plus metadata, not a retained proof of truth. Errors propagate or are handled locally (novelty query failure accepts; promotion failure can fall through). Recovery includes promotion/reassertion and live-point guards, not global rollback. SRC-1, `src/ingest.rs`, `src/mcp.rs`, `src/storage.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rendered counters distinguish stores, quarantine, reassertions, secret/duplicate skips and confined candidates.
- Later read-back: Live memories reach search; quarantine remains outside ordinary search until promotion; explicit facts/procedures reach their own consumers.
- Delegated visibility: Caller sees report counters, not a separate sub-agent transcript; optional extractor visibility is handled in its own route.
- Selection predicate: Candidate tag selects the branch; memory relevance/novelty/dedup decide ordinary versus quarantine placement, with fail-soft neighbor checks.
- Invalidation or expiry: Quarantine promotion/expiry and separate storage maintenance can change visibility; not all stores pass this policy.
- Activation or effect: Server writes or quarantines selected candidates; later behavioral effect is unobserved.
- Evidence limits: Gating is inspectable policy, not semantic truth testing; no runtime corpus or per-item approval evidence supplied.

> // No neighbors yet (empty library, or query failed
>                         // softly) — accept, novelty cannot be assessed.
>                         _ => crate::relevance::Verdict::Accept,
> --- `src/ingest.rs`

> if confine {
>                     report.skipped_scope_facts += 1;
>                     continue;
>                 }
> --- `src/ingest.rs`

#### RT-RTE-scoped-http
Label: Scoped HTTP request control

Bearer-token mapping establishes a server-derived agent and optional library list. Route middleware denies routes unable to honor that list. Authentication, argument normalization and consumer filters then control permitted requests; generic HTTP transport does not confer filesystem isolation. Read library names are canonicalized into `libraries`; the MCP filter parser consumes that key; storage installs conditions on both retrieval arms. Scoped JSON unified recall deliberately omits global fact/procedure silos; text unified recall rejects the request instead of forwarding it. By-agent is explicitly allowed in middleware and injects its own scope filter, so older comments calling it denied must not be treated as current policy. SRC-1, `src/http_api.rs`, `src/mcp.rs`, `src/storage.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unauthorized/forbidden/bad-request responses on failed checks, otherwise route-specific results.
- Later read-back: Confined memory writes may reach later scoped memory reads; global store exclusion must be qualified by the optional extraction route.
- Delegated visibility: Scoped recall receives empty facts and procedures fields, not hidden global values; direct CLI/stdio are separate trust paths.
- Selection predicate: Token-derived allowed libraries; unnamed/non-object reads become the allowlist, both singular/plural requests are checked, writes require a permitted singular library.
- Invalidation or expiry: Token/scope configuration is startup state in the inspected service, not a time-limited grant mechanism.
- Activation or effect: Rejection and filtering are wired request controls, conditional on external Qdrant filter semantics; they are not isolation against local administrators.
- Evidence limits: No HTTP execution supplied; no universal confinement claim across filesystem access, CLI, stdio or extractor-enabled side effects.

> if requested.is_empty() {
>         // Confine an unlibraried read to the allowlist so it can not span other
>         // agents' libraries.
>         obj.remove("library");
>         obj.insert(
>             "libraries".to_string(),
>             Value::Array(allowed.iter().map(|s| Value::String(s.clone())).collect()),
>         );
>         return Ok(());
>     }
> --- `src/http_api.rs`

> Ok(Format::Text) if is_scoped(&state, &derived) => (
>             StatusCode::FORBIDDEN,
> --- `src/http_api.rs`

#### RT-RTE-auto-extraction
Label: Optional background fact extraction

Accepted memory ingest is the trigger, conditional on compiled `extractor` feature and installation detection. Ingest enqueues config/content; one dedicated worker extracts triples and calls global fact admission. Local code proposes the extraction request, Qwen proposes triples, parser and knowledge API decide accepted structure/store effects; no per-triple human veto or answer oracle is wired. This is an automatic open-input side effect, not a benchmark. Natural-language extraction guidance and a stricter JSON repair request shape model input; parsed triples persist, not the repair conversation. Failures log/drop; queue overflow drops jobs; fact-write errors are ignored by the worker. There is no durable job retry or all-triples rollback in the inspected worker. SRC-1, `src/ingest.rs`, `src/extractor.rs`, `src/main.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ingest returns without awaiting extraction completion; bounded enqueue can drop overflow.
- Later read-back: Successful extracted fact writes can reach fact query/context consumers after the triggering memory call.
- Delegated visibility: Worker gets content/config rather than the assistant's complete window; caller does not receive a guaranteed extraction result or fact IDs.
- Selection predicate: Newly stored accepted memory with installed extractor; parsed response triples feed the fact API. The enqueue branch does not inspect `confine`.
- Invalidation or expiry: Job is transient; dropped/failed jobs have no queue replay here; fact validity and maintenance govern admitted results separately.
- Activation or effect: A scoped accepted memory can reach the global-fact writer in an enabled build; actual triples, writes and downstream use remain unobserved.
- Evidence limits: Default-off feature, installation and acceptance conditions bound reachability; model output quality, active installation and successful side effect are not demonstrated.

> #[cfg(feature = "extractor")]
>                     if crate::extractor::is_llama_server_installed() {
>                         crate::extractor::enqueue_auto_extract(config, &content);
>                     }
> --- `src/ingest.rs`

> let _ = crate::knowledge::add_fact(
>                                 &job.config,
>                                 &t.subject,
>                                 &t.predicate,
>                                 &t.object,
>                             )
>                             .await;
> --- `src/extractor.rs`

#### RT-RTE-context-briefing
Label: Session context briefing

Caller requests context; `build_context` reads files/Qdrant and returns natural-language output. Caller-authored session summary is atomically written by `session::end`; the builder uses `session::last(None)` and selected facts, pinned blocks and skill catalogue. Thus session identity separation in another API does not establish agent-specific briefing here. Host decides whether to request and inject the output. Admission of summaries comes from whoever calls end, without a mandatory per-summary human review; no answer oracle or experiment mode is present. Summary replacement and session restart are caller/storage recovery mechanisms, not model-directed host compaction. SRC-1, `src/session.rs`, `src/cli.rs`, `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rendered briefing with operating rule, pinned blocks, catalogue, last session, visible facts, libraries and quarantine information.
- Later read-back: Session end's persisted text reaches later context calls; pinned blocks and retained skills/facts have independent write routes.
- Delegated visibility: No isolated assistant frame is created; only selected rendered material is returned to the host.
- Selection predicate: Global newest session; facts with `valid = true` and default-visible status, ordered newest-first by `created_at` and limited to 20 before retaining only those with absent `valid_until` or `now < valid_until`; pinned blocks; up to 24 skill catalogue entries rather than bodies. The fact check passes no lower bound and does not read `valid_from` or call the world-time helper, so it does not establish complete interval validity.
- Invalidation or expiry: Subsequent sessions change newest selection; fact valid/status filters and the `valid_until` upper-bound check apply, not a full world-time interval check; catalogue directs callers to match for full bodies.
- Activation or effect: Selective context supply is wired; automatic injection, host eviction and compliance with its operating rule are unobserved.
- Evidence limits: No supplied invocation proves host window contents or behavior; this is a server briefing, not control of the enclosing context manager.

> let session =
>         crate::session::last(None)?.unwrap_or_else(|| "No previous sessions.".to_string());
> --- `src/cli.rs`

> // The skill catalogue: names and triggers only. A skill body can run to
>     // kilobytes and most of them do not apply to the task at hand, so the
>     // context carries the index and `mind_skill(action="match")` fetches the
>     // one that does.
> --- `src/cli.rs`

The briefing calls `fact_valid_at` with `None` for its start bound. Fact add can retain caller-supplied `valid_from`, including through the shipped CLI, but briefing does not consult it. A future-dated `valid_from` is therefore not excluded by this temporal check. This is an implementation distinction, not observed delivery of such a fact. SRC-1, `src/cli.rs`, `src/knowledge.rs`.

> if crate::knowledge::fact_valid_at(None, valid_until.as_deref(), &now) {
> --- `src/cli.rs`

> let effective_valid_from = valid_from.map(str::to_string).or(existing_valid_from);
> --- `src/knowledge.rs`

> if let Some(vf) = &effective_valid_from {
>         payload.insert("valid_from".into(), vf.clone().into());
>     }
> --- `src/knowledge.rs`

#### RT-RTE-skill-admission
Label: Named playbook admission

Caller supplies name, trigger and body; `skill::set` normalizes name and rejects empty body, then storage validates size/trigger and upserts a stable skill ID. Human versus model authorship depends on caller; code admission does not require per-content human approval. Open-request edits retain original creation time and have outcome history separate from body replacement. Guidance is the caller's natural-language house rule, not generated parameters. The inspected code does not expose supplied skill contents from which to assess formulated-theory criticism or learning; admission and retrieval alone establish neither. Caller can remove/rewrite; no automatic old-body rollback is established. SRC-1, `src/skill.rs`, `src/storage.rs`, `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/updated skill confirmation with ID and trigger.
- Later read-back: Context exposes a catalogue; skill match/show can return body for later tasks.
- Delegated visibility: Caller receives selected playbook text, not an isolated worker execution.
- Selection predicate: Stable normalized name for replacement; task-trigger retrieval and trust-aware ranking for later match.
- Invalidation or expiry: Explicit removal or same-name replacement; no time-based body expiry shown.
- Activation or effect: Durable instruction-content replacement is wired; consumption/compliance and improved future capacity are unobserved.
- Evidence limits: No per-skill content, observed outcomes or reference-answer oracle inspected; do not infer autonomous criticism from a mutable playbook.

> let existed = storage::get_skill(config, &name).await?.is_some();
>     let id = storage::add_skill(config, &name, when, body).await?;
> --- `src/skill.rs`

#### RT-RTE-markdown-reconcile
Label: Markdown replacement admission

Caller chooses a directory/library and apply flag. Planning compares disk text with existing stored entries; applying follows plan actions, deleting old entries before replacement writes. The content source is local Markdown, not a model truth judgment. Caller can decline apply; this is workflow authorization, not proof that a human reviewed each changed note. No expected-answer oracle is involved. The durable result is searchable replacement content plus audit metadata. Failed replacement after deletion is not an atomic rollback; the source files remain the potential reconstruction input. SRC-1, `src/md_reconcile.rs`, `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dry-run plan or apply counts, with failures propagated.
- Later read-back: New/replacement chunks reach ordinary memory search.
- Delegated visibility: Reconciliation is local filesystem work, not a delegated model frame; consumers see stored chunks.
- Selection predicate: Plan actions New/Replace mutate; Unchanged/Skip do not; caller must request apply on shipped surface.
- Invalidation or expiry: Replacement deletes prior points; future file reconciliation can replace again.
- Activation or effect: Admission from disk through normal storage writes is wired, without ingest novelty gating.
- Evidence limits: No applied plan or recovery observed; apply is not a cross-file transaction or universal safe-update guarantee.

> for old in &f.existing {
>                     storage::delete_memory(config, &plan.library, &old.id)
>                         .await
>                         .with_context(|| format!("Failed to delete old point for {}", f.source))?;
>                 }
> --- `src/md_reconcile.rs`

#### RT-RTE-store-consolidation
Label: Store consolidation admission

Caller selects options; code computes duplicate/cold candidates and mutates only under apply. This is deterministic policy-guided maintenance, not model content-directed criticism. Caller can withhold apply and choose archive versus prune; generic caller identity does not establish human per-record approval. No expected-answer oracle is used. Archive is reversible through restoration, deletion is not equivalent to archive, and the apply loop is not shown as transactional. SRC-1, `src/consolidate.rs`, `src/storage.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Scanned/duplicate/cold/action counters and applied state.
- Later read-back: Future search excludes archived/deleted points by the relevant filter/storage effect.
- Delegated visibility: Code operates on metadata/neighbors rather than spawning a model context.
- Selection predicate: Duplicate and coldness rules propose changes; apply enables deletion; archive takes precedence over prune for cold candidates.
- Invalidation or expiry: Archive can be restored; deleted content requires an independent recovery source.
- Activation or effect: Maintenance changes later retrieval membership when applied; benefit and correctness of candidate choices are unobserved.
- Evidence limits: No consolidation run inspected; it supplies neither semantic truth testing nor guaranteed improvement.

> if opts.apply {
>         let to_delete: Vec<String> = removed.iter().cloned().collect();
>         storage::delete_memories(config, &to_delete, "consolidate").await?;
>         if opts.archive_cold {
> --- `src/consolidate.rs`

### Claims

#### RT-CLM-recall-habit
Label: Requested recall habit

Claimed operation: the assistant should store durable facts and recall before answering questions that may depend on them. Source: the integration's agent instructions, SRC-1, `docs/integrations/openai_agents.py`. This is natural-language guidance delivered to a host, not server enforcement or observed compliance. The boundary's manual-loading limitation prevents inferring this habit merely from installing MCP tools.

> "You have a persistent memory. Use `remember` to store durable facts "
>         "and `recall` before answering anything that may depend on them."
> --- `docs/integrations/openai_agents.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-recall
Label: Host recall authority

Consumer: the external assistant model. Channel: tool-result text from `recall`, alongside natural-language agent instructions requesting use. Force: advisory/contextual model interpretation, not executable enforcement of belief or action. Horizon: the immediate answer; persisted memory can be requested again in later calls/sessions. [RT-RTE-assistant-memory](#rt-rte-assistant-memory) establishes the wired return path, not activation. SRC-1, `docs/integrations/openai_agents.py`, `clients/python/mgimind/_client.py`.

> def recall(query: str) -> str:
>     """Search the agent's long-term memory for anything relevant to a query."""
>     return str(mem.search(query, tier=2))
> --- `docs/integrations/openai_agents.py`

## Annotations

none
