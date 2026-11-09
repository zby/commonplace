---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Citadel runtime baseline: authenticated capture and search, asynchronous projection, promotion and scheduled index curation."
run-id: AAS-2026-11-09-citadel-de4383eefa4e-01
reviewed-boundary: "749a24014a6cef59499dbe13b6fb4c348f8044a4"
---

# Citadel runtime report

## Runtime account

### What runs, and where decisions sit

Citadel is an organization-memory service, not the coding agent that solves the user's engineering task. Its consequential work is accepting source material, projecting it into searchable stores, selecting scoped context, and admitting selected private material into shared Central. The enclosing host decides whether to use returned context. The frozen scope and evidence limits are in [boundary](boundary.md). All source findings below use SRC-1 at that boundary's commit. Implementation is inspected; no target execution, provider calls, tests or examples were run. Activation, production configuration and task benefit remain unobserved.

The shipped paths include Python CLI, HTTP server, MCP forwarding, host hooks and browser/plugin consumers. The boundary establishes packaging and browser/Obsidian entries; additional implementation coverage here includes `kb/cli.py` local handlers, `kb/mcp_server.py` forwarding and tool contracts, `kb/hooks/search_inject.py`, `kb/hooks/sync_session.py`, `kb/model_routing.py`, `kb/embedding_profile.py`, `kb/skills.py`, and the admission/projection/maintenance passages cited below. These add coverage under SRC-1, not new sources or observed runs.

The ordinary selected invocation is a coding host's UserPromptSubmit hook. The host starts a one-shot Python process, supplies the prompt on stdin and supplies a seat token through the environment. Code removes fenced commands, logs, traceback material and URLs from the query, bounds it to 1,000 characters, redacts secrets, and requests three hits. The service authenticates the token, derives datasets and sessions, searches, shapes a public page, and returns it. The hook emits at most three short result descriptions, explicit trust/provenance labels, and a policy reminder to stdout. It does not own the next model decision or execute retrieved instructions. See [RT-RTE-task-search](#rt-rte-task-search) and [RT-BAP-context-delivery](#rt-bap-context-delivery). SRC-1: `kb/hooks/search_inject.py`, `kb/server.py`.

A later SessionEnd invocation can distill the host transcript and POST a personal note. This is not a child reasoning agent: there is no separate autonomous model loop in this hook. Its local extraction uses deterministic string processing. Capture, projection and retrieval are distinct effects, not one atomic learning operation. See [RT-RTE-session-capture](#rt-rte-session-capture), [RT-RTE-source-projection](#rt-rte-source-projection). SRC-1: `kb/hooks/sync_session.py`, `kb/service.py`, `kb/lifecycle_worker.py`.

### Control and guarantee boundaries

1. **Private-by-default is an authenticated routing protocol, not universal isolation.** Server `require_access` checks role and scope; non-bypass seat callers reach their personal node with the light tier. Explicit Central requests and org/promotion tags are rejected there. Omitted datasets do not mean globally unscoped search: seat defaults expand to the personal node, permitted Central, and session traces. Environment identities, admin identities and identities with `access:manage` bypass the dataset allowlist. Local CLI calls instantiate `Citadel` directly rather than passing through HTTP authorization. These are distinct principals and execution envelopes, not demonstrated token escalation. The source does not reveal actual grants or deployed filesystem/container isolation. Owner: server/access configuration; enforcement: `require_access`, `resolve_write_targets`, `resolve_search_datasets`; guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected. External contract: token secrecy, correct identity issuance, and trusted local service/operator access. SRC-1: `kb/server.py`, `kb/cli.py`. See [RT-RTE-local-access](#rt-rte-local-access).

2. **User capture avoids synchronous generative enrichment on the inspected HTTP path, not every subsequent model computation.** `/ingest` rejects `cognify=True`, calls `execute_learning_writes` with its default `allow_llm=False`, and defers cognify. `LearningProcess.learn` then disables its enrichment and improvement steps. But `Citadel.ingest` can start vector-only background projection even when deferred. Embedding calls may follow; scheduled graph work may use generative models. Direct Python callers have a different default (`allow_llm=True` in `learn`) and therefore do not inherit the HTTP helper's exclusion. Owner: HTTP orchestration; enforcement: helper argument and learning branch; guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected. Required external contract: gateway/provider implementations must honor the separate projection methods. SRC-1: `kb/server.py`, `kb/learning.py`, `kb/service.py`, `kb/lifecycle_worker.py`. See [RT-RTE-ingest-admission](#rt-rte-ingest-admission).

3. **An accepted receipt does not attest completed indexing.** Lifecycle acceptance retains source bytes and returns source revision/job identity; backend completion and read checks are separate. Legacy mode calls Cognee directly and uses process-local duplicate exclusion, not lifecycle receipts. Vector recall in lifecycle mode uses current searchable revision IDs and validates returned bindings; exact Linear identity lookup and lexical fallback are materially different return branches. The lexical path can return retained source without completed vector/graph projection. Owner: lifecycle service/worker; enforcement: acceptance, receipts and read filters; guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected. Required external contract: durable SQLite/filesystem writes and truthful gateway read checks; this is not a measured durability guarantee. SRC-1: `kb/service.py`, `kb/lifecycle_worker.py`.

4. **Explicit approval is an agent-facing policy, not a universal server admission requirement.** The MCP ingest description asks for approval; its request contains no approval attestation. The SessionEnd hook automatically posts extracted material with a token. Promotion may automatically admit qualifying known-org work, while new-org-project candidates enter a review queue. No claim that every write is human-approved survives these alternate paths. The host's tool permission mechanism, if any, is external and unobserved. Owner: host/operator for ordinary MCP consent; enforcement: instructional text, not a server consent gate; guarantee strength: policy; implementation conclusion status: afforded; operation conclusion status: uninspected. SRC-1: `kb/mcp_server.py`, `kb/hooks/sync_session.py`, `kb/promotion.py`.

These four forcing cases challenge stronger readings of privacy, model exclusion, acceptance and approval. They do not establish a security exploit or exhaustive audit. Direct model calls, typed decision calls, provider embedding, background workers, local CLI, and scheduled service identities are material alternate paths here. No enclosing agent shell/tool policy is inferred from Citadel's API surface.

### Coordination, recovery and change admission

The HTTP search budget allocates 75% to vector-capable search, then spends remaining time on a lexical-only attempt after timeout. A slot limits concurrent requests; overload yields 429, exhaustion yields typed 504, and provider/general errors have separate handling. The service itself catches vector errors in lifecycle mode and can continue with lexical retrieval; legacy mode re-raises. Availability does not establish recall quality. SRC-1: `kb/server.py`, `kb/service.py`; [RT-RTE-task-search](#rt-rte-task-search).

The lifecycle worker owns progression after acceptance. It leases work, reads retained bytes, verifies relational visibility, projects vectors, checks chunk counts, and optionally projects/checks graph presence. Tombstones activate current-head exclusion receipts without provider content writes. Receipt resumption, cancellation lease handling and provider-error classification support recovery; inspected source does not establish that outages were recovered in a deployment. SRC-1: `kb/lifecycle_worker.py`; [RT-RTE-source-projection](#rt-rte-source-projection).

Scheduled evolution is an opt-in server task with an interval of at least 60 seconds. Stage drivers include GitHub/repository-content/Linear source synchronization, promotion, self-improvement and feedback. `run_evolve_in_loop` permits explicit stage selection and a capture-run identity; the web scheduler can place projection barriers between source and consumer stages. The standalone and in-loop lists are not interchangeable: feedback is in the in-loop list. This is cooperative maintenance on a shared service/event loop, not delegated model agents exchanging independent contexts. SRC-1: `kb/server.py`, `scripts/run_railway.py`.

Retained knowledge can change through user capture, connector ingestion, automatic promotion and model-proposed optimization notes. [RT-RTE-promotion-review](#rt-rte-promotion-review) and [RT-RTE-index-curation](#rt-rte-index-curation) establish distinct admission owners. Model parameters are not shown being trained by these operations: the models supply decisions, embeddings or proposed text. Component records separate chat, typed decision, embedding and Cognee generation surfaces. Fixed code and mutable model aliases must not be confused. Skill-catalog refresh re-hashes files already supplied by a deployment; it does not itself author or install model-proposed code. [RT-RTE-skill-refresh](#rt-rte-skill-refresh) marks this narrower production-change surface. Other release/build machinery remains outside detailed inspection, not evidenced absent. SRC-1: `kb/self_improve.py`, `kb/promotion.py`, `kb/skills.py`.

## Shared records

### Components

#### RT-CMP-openrouter-chat
Label: OpenRouter chat completion helper

Source-native identity: `openrouter_chat` and task routes. Representational form: distributed-parametric remote chat model; symbolic HTTP/JSON wrapper and natural-language messages are distinct inputs, not its parameters. Storage substrate: external provider weights, inaccessible in this source. Parameters changing during operation: no training/update operation is shown in this helper; provider-internal changes remain uninspected. Exact version pinned: no immutable weight identity is supplied; routine/reasoning/research defaults use `openrouter/free`. Mutable endpoint resolving to another model: yes, the router alias and configurable endpoint permit it; the helper logs the selected model returned by the provider. SRC-1: `kb/llm_enrichment.py`, `kb/model_routing.py`.

> DEFAULT_ROUTINE_MODEL = "openrouter/free"
> --- `kb/model_routing.py`

> "%s LLM route selected: requested=%s selected=%s",
> --- `kb/llm_enrichment.py`

#### RT-CMP-promotion-decision
Label: Promotion typed decision model

Source-native identity: `promotion_decision_model` / `openrouter_decide`, default Jev `typesafe/jev-1.13`. Representational form: distributed-parametric decision model consuming text and symbolic question schema; returned confidences are symbolic values. Storage substrate: external `/systemone` provider. Parameters changing during operation: no update path inspected; provider internals uninspected. Exact version pinned: a version-like model name is requested, not a verified immutable model artifact. Mutable endpoint can resolve to another model: configurable model and endpoint allow substitution; alias resolution internals are uninspected. On no usable verdict the implementation falls back to chat; a usable negative decision does not trigger fallback. SRC-1: `kb/promotion.py`, `kb/llm_enrichment.py`.

> if decision_model:
>     decided = self._classify_via_decision(text, decision_model)
>     if decided is not None:
>         return decided
> return self._classify_via_chat(text)
> --- `kb/promotion.py`

#### RT-CMP-embedding-profile
Label: Embedding profile models

Source-native identity: `PRIMARY_EMBEDDING_PROFILE` and `LOCAL_EMBEDDING_PROFILE`, respectively Nemotron remote embedding and FastEmbed `BAAI/bge-small-en-v1.5`. Representational form: distributed-parametric models producing dense numerical vectors. Storage substrate: remote provider or local cached model artifacts; vectors are projection data, not model weights. Parameters changing during operation: no training shown in inspected profile/worker paths. Exact version pinned: model names and dimensions are configured, but inspected code does not establish immutable weight hashes. Mutable endpoint substitution: remote provider/configuration can change; local model contents and dependency internals are uninspected. Lite checks the offline model name against the image's baked choice rather than proving weight identity. SRC-1: `kb/embedding_profile.py`, `kb/lite_runtime.py`, `kb/lifecycle_worker.py`.

> LOCAL_MODEL = "BAAI/bge-small-en-v1.5"
> LOCAL_DIMENSIONS = 384
> --- `kb/embedding_profile.py`

#### RT-CMP-cognee-models
Label: Cognee extraction and summarization models

Source-native identity: Cognee extraction, summarization and query model environment settings. Representational form: distributed-parametric provider models behind the Cognee gateway. Storage substrate: provider weights, not retained source store. Parameters changing during operation: no weight training established; model selection can change. Exact version pinned: defaults use a router alias. Mutable endpoint substitution: yes; inspected fallback may rewrite process environment once, except when projection digest v2 disables the swap. The v2 option restricts runtime route changes; it does not turn an external model alias into immutable weights. Cognee dependency internals and actual per-request chosen model remain uninspected. SRC-1: `kb/model_routing.py`, `kb/lifecycle_worker.py`.

> if os.getenv("CITADEL_PROJECTION_DIGEST_V2", "").strip().lower() in {
>     "1",
>     "true",
>     "yes",
>     "on",
> }:
> --- `kb/model_routing.py`

### Operative objects

#### RT-OBJ-ingest-result
Label: IngestResult acceptance receipt

Source-native identity: `IngestResult` returned from `Citadel.ingest`. Representational form: symbolic fields interpreted by fixed client/server rules. Substrate: Python object serialized as HTTP JSON; durable lifecycle source/job identifiers refer to separate retained state. The receipt distinguishes acceptance, source-searchability and projection state rather than establishing semantic correctness or completed graph indexing. SRC-1: `kb/service.py`, `kb/server.py`.

> return IngestResult(
>     True,
>     "queued_not_confirmed",
>     target_dataset,
> --- `kb/service.py`

#### RT-OBJ-optimize-prompt
Label: OPTIMIZE_SYSTEM_PROMPT

Source-native identity: shipped optimization system prompt. Representational form: natural-language curation request plus symbolic output-shape example. Substrate: Python string in repository/deployment, delivered in a chat request. It asks for better tags/summaries using labels and existing tags, not a criticism of Citadel's own method. Detailed retained-memory objects and revisions belong to the memory analysis. SRC-1: `kb/self_improve.py`.

> "Keep labels unchanged. Never invent facts and never include secrets."
> --- `kb/self_improve.py`

### Routes

#### RT-RTE-task-search
Label: Task prompt to scoped context

Endpoints/progression: host stdin → query extraction/redaction → authenticated HTTPS `/search` → dataset/session resolution → service recall/lexical retrieval → public result shaping → hook stdout. Owner/decision roles: code chooses query transformations, scope and bounds; embedding/retrieval providers supply candidates; host/model owns any subsequent action. Context/state/effects: current task query and identity drive read-only retrieval with audit/telemetry side effects. MCP search uses the same HTTP endpoint and compacts the result; local CLI is a distinct route. Operating mode: open task requests, not a curriculum. Answer oracle: none established; scoring/ranking is not an expected-answer oracle. SRC-1: `kb/hooks/search_inject.py`, `kb/server.py`, `kb/service.py`, `kb/mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bounded context text and policy reminder; HTTP callers receive a shaped page or typed error.
- Later read-back: retained source can be selected at later prompt invocations; this hook does not retain its own result window.
- Delegated visibility: host receives at most three result descriptions, not the complete indexed corpus or worker state.
- Selection predicate: cleaned prompt query, authenticated dataset/session scope, top-k and configured retrieval; explicit callers can request supported filters.
- Invalidation or expiry: lifecycle current-revision binding excludes obsolete/tombstoned vector hits; no separate expiry for emitted stdout is established.
- Activation or effect: delivery is wired; host compliance and behavior changes remain unobserved.
- Evidence limits: no supplied host trace, ranking experiment or task outcome; dependency implementation is not inspected.

> MAX_CONTEXT_CHARS = 6000
> MAX_SNIPPET_CHARS = 500
> --- `kb/hooks/search_inject.py`

> allow_generative=False,
> --- `kb/service.py`

Working-context control: code preferentially omits executable wrappers/logs from the query and all but short descriptions from the returned page. Full documents remain outside the window and can be requested through MCP document drilldown. This is bounded external-memory supply, not conversation compaction or a model-selected subagent frame. The host retains control over whether stdout enters a model context. Provider timeout triggers the lexical-only retry described above; hook failures are swallowed and the reminder still prints.

#### RT-RTE-session-capture
Label: SessionEnd personal note capture

Endpoints/progression: host SessionEnd payload → allowlisted transcript JSONL → deterministic distillation → byte cap → HTTPS `/ingest` with no dataset → personal node acceptance receipt. Principal: configured token holder; owner: host invokes hook, hook code chooses extraction, server decides admission. A one-time setup is not per-note human approval. Source-native guidance is the deterministic distiller, not a runtime model judgment. Operating mode: automatic session close. Answer oracle: inapplicable, no answer comparison. SRC-1: `kb/hooks/sync_session.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: exit zero and best-effort receipt distinguishing accepted/rejected/unconfirmed; empty extraction sends nothing.
- Later read-back: admitted note can be selected by later personal-node searches.
- Delegated visibility: server receives distilled text and tags, not the full transcript through this route.
- Selection predicate: token present, allowed resolved transcript path, extractable content; dataset omitted for server identity routing.
- Invalidation or expiry: no note expiry established here; downstream lifecycle policy governs retained content.
- Activation or effect: automatic write request is implemented; actual retention and future influence unobserved.
- Evidence limits: host installation/triggering, actual transcript and token grants are not supplied.

> body = json.dumps({"data": data, "tags": tags}).encode("utf-8")
> --- `kb/hooks/sync_session.py`

Admission: server can reject content; local failures do not block host shutdown. Recovery: a timeout is reported as unconfirmed rather than proof of non-storage. No unconditional retry is shown in this hook. HTTPS and refusal of redirects protect the credential channel under the inspected urllib path, not every other client.

#### RT-RTE-ingest-admission
Label: HTTP source admission

Endpoints/progression: authenticated `/ingest` → write-target resolution → sequential learning writes → filter/content scan/chunk guard → lifecycle acceptance or legacy Cognee remember. Owner: server code; proposer: caller supplying content; decider/veto: role/scope/dataset rules and content guards. Operating mode: open capture requests; no expected-answer oracle. Human authorship or per-content approval cannot be inferred from generic token identity. Proposed change: retained source content and eventual searchable projections. Guidance: request data/tags and shipped filtering/enrichment policy; source text and metadata persist, not a new executable capability. SRC-1: `kb/server.py`, `kb/learning.py`, `kb/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: IngestResult receipt with source/job identifiers in lifecycle mode, not proof of completed projection.
- Later read-back: retained accepted content is reachable through lifecycle lexical search and subsequent projected retrieval.
- Delegated visibility: downstream stores/providers receive permitted source/chunk data and metadata; user HTTP admission suppresses generative enrichment before that projection stage.
- Selection predicate: writer role plus kb:ingest scope, identity-specific target rules, source-key restrictions, size and content/path guards.
- Invalidation or expiry: rejected writes do not enter the store; lifecycle chunk replacement can tombstone obsolete chunk keys after all new chunks are accepted.
- Activation or effect: source acceptance and optional background vector projection are wired, not observed.
- Evidence limits: configured scanner strength, actual persistence and external provider behavior are not established; sequential multi-target writes are not shown to be transactional.

> allow_llm: bool = False,
> --- `kb/server.py:3098-3098`

> if not allow_llm or tier in {"light", "shared"}:
>     enrichment = None
>     effective_run_improve = False
> --- `kb/learning.py`

> (not defer_cognify or self._lifecycle_vector_only)
> --- `kb/service.py`

Rejection/recovery: secret findings become HTTP 422; generic failures become 500. Legacy duplicate claims are released if remember fails. Source acceptance is not rolled back merely because later projection is pending or failed. This route does not establish universally secret-free data: the scanner is configurable and pattern detection is not a semantic secrecy proof.

#### RT-RTE-source-projection
Label: Retained source to searchable projections

Endpoints/progression: leased durable lifecycle job → retained source bytes → relational write/read check → vector write/chunk check → optional graph write/presence check. Owner: lifecycle worker and lease heartbeat; providers perform delegated computations. State: source revision, generation/config projection identity and per-backend receipts. Effect boundary: configured relational/vector/graph stores, not a host agent's arbitrary tool executor. SRC-1: `kb/lifecycle_worker.py`, `kb/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: worker completion/retry bookkeeping rather than a generated user answer.
- Later read-back: service retrieval consumes source and verified projection bindings; worker can reload source after interruption.
- Delegated visibility: gateway receives retained text for remember and selected revision IDs for vector/graph projection.
- Selection predicate: worker lease/job filters and active projection identity; graph work depends on include_graph.
- Invalidation or expiry: lease expiry/cancellation and retry policies govern work; tombstones activate current-head exclusion without requiring provider deletion.
- Activation or effect: backend writes and verification receipts are wired; successful read checks are not a demonstrated semantic retrieval guarantee.
- Evidence limits: inspected gateway call sites and receipt checks do not expose provider internals or deployed recovery history.

> content = self.store.read_retained_content(source.source_revision_id)
> --- `kb/lifecycle_worker.py:699-699`

> if not self.include_graph:
>     self.store.defer_graph_enrichment(lease, now=now)
>     return
> --- `kb/lifecycle_worker.py`

The worker marks vector searchability only after finding at least one chunk for the accepted source revision. Relational recovery can reconcile an existing source revision instead of rewriting it. Graph-less and legacy-gateway paths differ; graph success must not be inferred from vector success. The inspected error classification distinguishes retryable provider trouble, quota backoff and permanent failures; these are reliability mechanisms, not observed reliability.

#### RT-RTE-local-access
Label: Local CLI service access

Endpoints/progression: explicit CLI `--local` handler → `Citadel.from_env()` → `ingest` or `search` directly → JSON/result shaping. Owner/principal: local process operator, not an authenticated HTTP seat identity. Context/state: local environment and optional dataset/session flags. This supported caller demonstrates that server role/scope enforcement does not cover all service calls. It does not prove a remote caller can reach this authority. SRC-1: `kb/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON receipt or shaped search payload and exit status.
- Later read-back: local admitted material can be retrieved through its configured service stores.
- Delegated visibility: configured service/provider sees the operator-supplied input; no separate subagent context.
- Selection predicate: explicit local mode; dataset/session from CLI rather than HTTP identity routing.
- Invalidation or expiry: downstream service/lifecycle rules, not a separate CLI TTL.
- Activation or effect: direct service invocation is wired; actual local installation/configuration unobserved.
- Evidence limits: no claim that an untrusted remote token can invoke the local process.

> result = await kb.ingest(
>     args.data,
>     dataset=args.dataset,
> --- `kb/cli.py`

Admission: caller proposes source; service content guards can reject, while HTTP-specific Central policy does not run. No per-content human approval is encoded by this handler. Operating mode: explicit operator requests; answer oracle: inapplicable. Recovery/rollback follows service receipts and failure semantics, not an independent CLI transaction.

#### RT-RTE-promotion-review
Label: Seat candidate to Central promotion

Endpoints/progression: enabled engine enumerates bounded seat candidates → personal-tag/secret controls → organization-reference assessment → typed model decision or chat fallback → relevance/sensitivity/score threshold → automatic known-work admission, new-project review queue, or skip → shared learning writes and audit. Owner: engine code; proposer: candidate enumerator plus source content; model supplies judgment, fixed rules decide admission class, authorized reviewer approves/rejects pending candidates. Operating mode: bounded maintenance sweep, not an answer-key experiment. Answer oracle: none established; organizational reference lookup and model scores are not known correct answers. SRC-1: `kb/promotion.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposals, queued/promoted counts and reasons; dry-run does not execute promotion writes.
- Later read-back: accepted Central copy is searchable by later shared consumers; rejection state is checked against candidate hash.
- Delegated visibility: classifier sees capped candidate text; review queue retains candidate content for authorized decision.
- Selection predicate: enabled flag, seat dataset, candidate cap, reference status, relevant and non-sensitive judgment above configured threshold; personal/secret/rejected candidates are skipped.
- Invalidation or expiry: rejected hash blocks later promotion; pending items must remain pending to be decided; no automatic expiry established in inspected engine.
- Activation or effect: automatic and reviewer-mediated shared writes are wired, not observed.
- Evidence limits: model judgment reliability, complete candidate enumeration, reviewer exercise and actual accepted Central writes are unobserved.

> if reference.status == "new_org_project":
>     return ProposedPromotion(
>         decision="pending_approval",
> --- `kb/promotion.py`

> if proposal.decision == "pending_approval":
>     self._enqueue_pending(seat_slug, seat_dataset, proposal)
> --- `kb/promotion.py`

Admission/recovery: the synthetic env/admin promotion identity can write personal and Central targets. `_promote` reuses learning writes with deferred cognify; secret or write errors return `write_blocked`, and rejected Central ingestion does not count as promoted. Approval consumes a pending item even if the resulting write is not accepted; returned `write_reason` separates those outcomes. Rejection can veto pending content; it is not a required veto opportunity for every automatic known-work write. No atomic rollback across the sequential seat/Central writes is established.

#### RT-RTE-index-curation
Label: Scheduled optimization note admission

Endpoints/progression: maintenance driver → recent Central mesh activity → Cognee improve → optional model proposals from labels/tags → parsed known-label proposals → non-dry-run learning ingestion → audit/mesh summary. Owner: SelfImprovement code; model proposes tags/summaries, parser and downstream ingestion guards decide acceptability. The user does not approve each scheduled proposal. Operating mode: bounded periodic index curation, not a controlled comparison. Answer oracle: none established. SRC-1: `kb/self_improve.py`, `scripts/run_railway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bounded proposal/result summary including optimized count and improve result.
- Later read-back: admitted optimization notes can enter later Central retrieval; previous optimization notes are excluded from this route's proposal-input document selection.
- Delegated visibility: proposal model receives labels and tags, not full source bodies or raw feedback events through propose_optimizations.
- Selection predicate: Central recent document nodes excluding self-improvement tag, capped to at most 50; known-label output validation, non-dry-run, successful prior improve result.
- Invalidation or expiry: source-keyed self-improve notes may receive later revisions; no rollback or quality-based undo is established here.
- Activation or effect: source-note admission is wired; future behavioral reliance and improved capacity are unobserved.
- Evidence limits: counted feedback is not shown as proposal-model input; upstream Cognee improve semantics are opaque at this inspected boundary.

> if proposals and not dry_run:
>     applied = await self._apply(proposals[:limit], dataset=dataset)
> --- `kb/self_improve.py`

> source_key=f"self-improve:{source_key}",
> --- `kb/self_improve.py`

Guidance: [RT-OBJ-optimize-prompt](#rt-obj-optimize-prompt). What persists is an optimization note with summary/proposed tags/source pointer, not trained weights, a code patch or demonstrated formulated methodological criticism. Malformed/unavailable proposals become no-op; individual re-ingest failures skip an item. The `dry_run` flag suppresses applying these notes, but does not skip the preceding `_improve` call or result recording; it is not established as a whole-route no-side-effects guarantee. Calling this module self-improvement does not establish exercised system improvement: changed notes could influence later retrieval, but later operation depending on them and objective-responsive benefit are not supplied. Learning, reflection and theory-building cannot be inferred from the name or persistence alone.

#### RT-RTE-skill-refresh
Label: Deployment skill change detection

Endpoints/progression: scheduled skill refresh → fresh catalog of bundled files → compare hashes with prior JSON → persist current hash map and report changes. Owner/decider: code detects differences; deployment supplied the files. This route admits change-detection state, not new skill content. Operating mode: scheduled maintenance; answer oracle: inapplicable. SRC-1: `kb/skills.py`, `scripts/run_railway.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed/added/removed skill slugs and catalog.
- Later read-back: saved hashes are compared next refresh; actual skills remain deployment files.
- Delegated visibility: clients can request public skill content; refresh does not start a model or install code in a host.
- Selection predicate: canonical bundled skill catalog, hash inequality against prior state.
- Invalidation or expiry: current hash map replaces previous detection state; no content rollback in this routine.
- Activation or effect: detection/reporting wired; host loading or honoring updated instructions unobserved.
- Evidence limits: broader code-release admission and installed host skill versions are not assessed.

> The catalog itself is
> always computed fresh from disk; this only tracks change detection state.
> --- `kb/skills.py`

### Claims

#### RT-CLM-explicit-approval
Label: MCP explicit-approval instruction

Claimed operation: MCP tool text requests human approval before ingest. Source and strength: policy supplied to the enclosing agent, not a verified server consent event. The automatic session hook and automatic known-work promotion are countercases to interpreting it as a universal admission invariant. SRC-1: `kb/mcp_server.py`, `kb/hooks/sync_session.py`, `kb/promotion.py`.

> **Always ask the user for explicit approval before calling this tool.**
> --- `kb/mcp_server.py:1316-1316`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-delivery
Label: Search context into host model window

Consumer: enclosing coding host/model. Channel: hook stdout or MCP search return, with short text and symbolic trust/provenance metadata. Force: advisory/untrusted context; code can bound and label delivery but cannot force the model's interpretation. Horizon: current task invocation; underlying stored source can influence later invocations if selected again. SRC-1: `kb/hooks/search_inject.py`, `kb/mcp_server.py`. Connected route: [RT-RTE-task-search](#rt-rte-task-search).

> "# Citadel task context (untrusted context)",
> --- `kb/hooks/search_inject.py`

#### RT-BAP-curation-guidance
Label: Curation prompt into proposed knowledge

Consumer: remote chat model, then fixed parser and learning admission pipeline. Channel: system-role optimization prompt and user-role label/tag lines. Force: requested semantic behavior, constrained by structural output checks and ingest guards, not a proof of truth or fidelity. Horizon: one proposal call, potentially later Central retrieval after note admission. SRC-1: `kb/self_improve.py`; [RT-RTE-index-curation](#rt-rte-index-curation), [RT-CMP-openrouter-chat](#rt-cmp-openrouter-chat). The model cannot directly execute a repository edit through this inspected response channel.

> {"role": "system", "content": OPTIMIZE_SYSTEM_PROMPT},
> --- `kb/self_improve.py`

## Annotations

none
