---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Atomic runtime baseline tracing chat, model-authored writes, wiki admission, reports and maintenance at the frozen repository revision."
run-id: AAS-2026-10-12-atomic-f98683232831-01
reviewed-boundary: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
---

# Atomic runtime report

## Runtime account

Atomic combines a knowledge store with bounded model-dependent consumers and shipped maintenance drivers. It is not the enclosing runtime of an arbitrary external MCP client. The source boundary and source register are in [boundary](boundary.md#source-register). All evidence here is SRC-1 implementation or explicitly attributed doctrine/design. No execution trace or experiment was supplied, and no target execution was performed. Every route's operation remains uninspected; source wiring does not establish successful activation, reliability or benefit.

### Ordinary shipped invocation: one chat turn

An authenticated client posts a conversation ID and user text to `/api/conversations/{id}/messages`. The server registers a cancellation handle keyed by request job scope and conversation ID, chooses the plain or page/canvas-aware core entry, and awaits it. Atomic saves the user message before invoking the provider, reloads conversation scope and messages, builds a system message from the source-native instructions and optional custom prefix/UI context, and trims the prompt to the configured context budget. The provider receives messages and tool schemas. It chooses an answer or tool names/JSON arguments; Rust owns lookup, execution, iteration and persistence. See [RT-RTE-chat-turn](#rt-rte-chat-turn).

The shared AgentRun iterates up to ten model rounds for chat, executes each requested tool sequentially, appends results, and stops on an answer, cancellation or cap. A cap is not a bound on individual tools: one response can request several, and an empty cap result can cause an extra tool-free salvage completion. Cancellation is cooperative, sampled before rounds and between tools and raced against provider completion; it does not interrupt an already awaited tool or undo completed writes. The runtime records tool start/completion timestamps, failures and streaming events. Unknown tools become failed results rather than execution of arbitrary names. SRC-1: `crates/atomic-core/src/agent_runtime/run.rs`, `crates/atomic-core/src/agent.rs`.

Atomic resolves citation markers against the run ledger, saves the assistant message, then tool calls and citations, then emits completion. These are successive fallible operations, not one demonstrated transaction. A provider failure leaves the previously saved user turn; a later persistence failure can leave partial assistant state. Cancellation yields a marked partial answer, not rollback. Untitled conversations can start separate title generation after completion. SRC-1: `crates/atomic-core/src/agent.rs`, `crates/atomic-server/src/routes/chat.rs`.

### Grants, enforcement and forcing cases

The capability surface is the compiled tool implementations. The current chat grant set is assembled afresh: search, atom/tag/wiki/report/finding readers, plus create/edit atom, with page context and canvas navigation added conditionally. The registry rejects unknown names, but this is a local dispatch invariant, not OS isolation. Tools capture storage, settings, caches and callbacks; they execute with those host privileges. No deployed container, host permission set or provider-native capability envelope is established here. Registry replacement by same name is afforded to Rust callers; runtime installation of arbitrary model-proposed plugin code is not established by this mechanism. SRC-1: `crates/atomic-core/src/chat_tools.rs`, `crates/atomic-core/src/agent_runtime/tools.rs`.

Four source forcing cases bound the conclusions:

1. **Read scope versus mutation.** Chat ID-based readers use ScopeGuard, and search carries scope into queries. But EditAtom uses MutationDeps, loads the supplied atom ID directly and does not apply that guard. Create/edit tools are always registered. The “only when explicitly asked” constraint is tool-description guidance, not an independent human approval step. Thus conversation scope is a reader boundary, not a universal mutation authorization boundary. See [RT-RTE-atom-mutation](#rt-rte-atom-mutation).
2. **Reviewed wiki versus direct publication.** Proposal acceptance checks live article ID and timestamp under a local tag lock. However `update_wiki` proposes and immediately accepts; `generate_wiki` directly saves a replacement. Human review is an available workflow, not an invariant across wiki admission. Direct generation also lacks the durable ledger semantics of `regenerate_wiki`. See [RT-RTE-wiki-admission](#rt-rte-wiki-admission).
3. **Shared loop versus alternate loops and calls.** Wiki agentic research has its own provider/tool dispatch, fifteen-round cap and chunk selection budget. Reports use AgentRun for research but then a separate structured markdown final pass. Single-shot tagging and embedding calls do not use AgentRun. Therefore its cancellation, prompt trimming and grant set do not govern every model call. See [RT-RTE-report-finding](#rt-rte-report-finding) and [RT-RTE-state-maintenance](#rt-rte-state-maintenance).
4. **Inline writes versus durable/background execution.** Core creation inserts first, enqueues enrichment and may process it inline; chat mutations spawn background enrichment, imports can write pending rows directly, and cloud dispatch uses explicit batch workers. A returned atom is not proof of completed enrichment. Graph maintenance even marks claimed edge batches complete after a caught edge-computation error. Therefore queue/task status is not a universal semantic-success guarantee. See [RT-RTE-capture-write](#rt-rte-capture-write) and [RT-RTE-state-maintenance](#rt-rte-state-maintenance).

The standalone composition wraps API routes in BearerAuth and MCP routes in McpAuth; the exported route scopes themselves are deliberately unwrapped so cloud composition can supply different middleware. Inspected BearerAuth checks a token against the active core before awaiting the service result. This is an HTTP principal gate, not per-content human consent. Direct core/storage calls and command-line SQLite import do not pass through it. Cloud quota, billing and tenant-auth composition are included but their detailed enforcement is not audited here, so no universal tenant-isolation or quota invariant is asserted. SRC-1: `crates/atomic-server/src/app.rs`, `crates/atomic-server/src/auth.rs`, `crates/atomic-cloud/src/main.rs`, `scripts/import/shared/index.js`.

### Claimed work, state changes and coverage limits

The inspected routes admit captured notes, model-authored atom edits, wiki replacements, automated report findings and derived graph state. Settings edits can change model endpoints, prompts and strategies on later operations, with an explicit-provider mode that overrides settings-derived provider selection. These are separate admission mechanisms, not evidence of autonomous source-code improvement. Proposal/decision/veto roles and answer-oracle limits are recorded in the routes. Parameter mutability is separately recorded in [RT-CMP-agentic-model](#rt-cmp-agentic-model), [RT-CMP-tagging-model](#rt-cmp-tagging-model) and [RT-CMP-embedding-model](#rt-cmp-embedding-model).

This member adds source inspection under SRC-1 of `crates/atomic-core/src/chat_tools.rs`, `agent_runtime/tools.rs`, `providers/mod.rs`, `reports/agentic.rs`, `graph_maintenance.rs`, `wiki/runner.rs`, `crates/atomic-server/src/app.rs`, `auth.rs`, and the cited bounded regions of previously registered files. It establishes the selected control paths, not complete implementation auditing of every included client. Browser/mobile/Obsidian/Discord capture, frontend saved answers, desktop sidecar and direct import are shipped paths identified by the boundary; their retries and admission UI details remain uninspected here. Cloud backpressure, storage transaction implementations, schema enforcement internals, backup/account deletion, compaction, provider-native service behavior and benchmark outcomes remain unresolved at this runtime layer. Those limits prevent universal isolation, durability, semantic correctness and improvement claims; they do not remove these mechanisms from scope.

## Shared records

### Components

#### RT-CMP-agentic-model
Label: Agentic model

Source-native identity: provider-configured chat/wiki/report LLM; chat resolves `chat_model`, reports resolve `wiki_model` for OpenRouter, while local/compatible providers use their configured LLM. Representational form: distributed-parametric weights externally hosted, with text/JSON interfaces. Storage substrate: external provider or local Ollama service; only identifiers/configuration are in Atomic storage. Parameter updates during operation: provider internals uninspected; inspected calls request inference, not weight updates. Exact version pinned: not established by a model-name string. Mutable endpoint can resolve another model: yes, endpoint/model settings are configurable; explicit-provider mode can hold selection outside stored settings. SRC-1 implementation: `crates/atomic-core/src/providers/mod.rs`, `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/reports/agentic.rs`, `crates/atomic-core/src/lib.rs`.

> pub const DEFAULT_AGENTIC_MODEL: &str = "anthropic/claude-sonnet-5";
> --- `crates/atomic-core/src/providers/mod.rs`

#### RT-CMP-tagging-model
Label: Tagging model

Source-native identity: configured utility LLM for structured extraction. Representational form: distributed-parametric model; returned tag applications are symbolic names/parent names interpreted by storage routines. Storage substrate: external provider or local model service; Atomic stores model configuration and derived tags, not inspected weights. Parameters changing during operation: uninspected inside providers; no weight-update call established in extraction. Exact version pinned: no immutable weight identity established. Mutable endpoint can resolve another model: yes, provider and tagging-model settings configure the call. SRC-1 implementation: `crates/atomic-core/src/providers/mod.rs`, `crates/atomic-core/src/extraction.rs`, `crates/atomic-core/src/embedding.rs`.

> pub const DEFAULT_TAGGING_MODEL: &str = "openai/gpt-5-nano";
> --- `crates/atomic-core/src/providers/mod.rs`

#### RT-CMP-embedding-model
Label: Embedding model

Source-native identity: configured embedding provider/model, used for enrichment and query embeddings. Representational form: distributed-parametric model and dense numerical outputs; vectors are not model weights. Storage substrate: service-side weights; derived vectors in Atomic's database/vector indexes. Parameters changing during operation: uninspected service behavior; inspected client requests inference. Exact version pinned: no immutable weight pin established. Mutable endpoint can resolve another model: yes, configurable provider URL/model; model-space changes have a separate re-embedding entry path. SRC-1 implementation: `crates/atomic-core/src/providers/mod.rs`, `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/lib.rs`.

> pub const DEFAULT_EMBEDDING_MODEL: &str = "qwen/qwen3-embedding-8b";
> --- `crates/atomic-core/src/providers/mod.rs`

### Operative objects

#### RT-OBJ-tool-registry
Label: ToolRegistry

Source-native identity: per-run ordered tool definitions and name-to-AgentTool map. Representational form: symbolic Rust objects and JSON schemas; descriptions have a separate natural-language model consumption path. Storage substrate: process memory, not a persistent capability-installation store. Rust constructs the grant set and a duplicate name replaces an earlier registration. SRC-1 implementation: `crates/atomic-core/src/agent_runtime/tools.rs`, `crates/atomic-core/src/chat_tools.rs`.

> self.by_name.insert(definition.name, Arc::new(tool));
> --- `crates/atomic-core/src/agent_runtime/tools.rs`

### Routes

#### RT-RTE-chat-turn
Label: Chat turn

Endpoints/progression: authenticated HTTP caller → conversation core → AgentRun/provider → local tool executor → persisted assistant turn and HTTP/WebSocket result. Owner: server cancellation registry for turn lifetime; AgentRun for next-step dispatch; model for requested tool/answer choice; storage for retention. Context: system prose, stored conversation, scoped reader tools and optional UI context. State: messages, per-run citation ledger and tool history; UUIDs identify messages and conversation ID identifies reload. Effects: host storage and frontend event callbacks, not a remote delegated worker.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ChatMessageWithContext in HTTP response; streaming/tool/progress and completion events on WebSocket.
- Later read-back: stored conversation is reloaded for the next turn, converted and context-trimmed; detailed conversion of historical tool messages remains uninspected here.
- Delegated visibility: provider receives the trimmed messages and offered tool schemas/results, not an automatic dump of the database.
- Selection predicate: requested conversation ID, stored scope and tool-specific selection; optional context determines conditional registrations.
- Invalidation or expiry: current-run registry/ledger expire with the run; stored history has no expiry established by this trace, and context truncation can omit older messages.
- Activation or effect: source wires provider requests, local execution and persistence; actual model reliance and successful operation are unobserved.
- Evidence limits: no supplied run; host isolation and provider compliance are not established; cancellation may return an unbalanced raw run history, while chat saves its text/call records rather than replaying that raw history directly.

Guarantee owner/enforcement: AgentRun checks registry names and loop count; unknown names cannot invoke an unregistered AgentTool through this dispatch. Guarantee strength: invariant for this lookup, best effort for cooperative cancellation. Covered paths: shared AgentRun executions. Alternate paths: wiki's own loop, direct provider calls, MCP/core calls and imports are outside that enforcement point. External contract: provider must return tool calls in the adapter's expected form; individual tools validate arguments and can perform host effects. Ten iterations are model rounds, not a maximum number of tools or total network requests. SRC-1 implementation: `crates/atomic-server/src/routes/chat.rs`, `crates/atomic-core/src/agent.rs`, `crates/atomic-core/src/agent_runtime/run.rs`.

> 'iterations: for _ in 0..config.max_iterations {
> --- `crates/atomic-core/src/agent_runtime/run.rs`

> None => ToolResult::failed(format!("Unknown tool: {}", name)),
> --- `crates/atomic-core/src/agent_runtime/run.rs`

#### RT-RTE-atom-mutation
Label: Agent atom mutation

Endpoints/progression: model's create/edit JSON → registered CreateAtom/EditAtom → storage insert or compare-and-update → background enrichment and AtomCreated/AtomUpdated event. Owner: model proposes content; deterministic code validates shape/nonempty/change and storage concurrency. There is no independent per-content human veto in these handlers. Operating mode: open chat requests; no answer oracle or reference outcome used. Guidance says to mutate only on explicit user request and prefer targeted edits, but the executor does not itself verify that request. Persisted result is atom content, not a retained criticism of the method. Recovery: malformed edits fail before save, update compares prior timestamp, successful writes invalidate canvas cache; user correction/deletion is external to this tool, and completed effects are not undone on cancellation. SRC-1 implementation: `crates/atomic-core/src/chat_tools.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: created/updated atom payload, reference and possible citation index, plus UI mutation event.
- Later read-back: changed atom is available to subsequent atom/search consumers; enrichment is separately scheduled, so immediate vector-search freshness is not guaranteed.
- Delegated visibility: model receives the mutation result; background task receives storage/settings and atom ID.
- Selection predicate: caller/model content and atom_id; edit loads that ID directly rather than through ScopeGuard.
- Invalidation or expiry: canvas cache invalidated; derived enrichment enqueued; atom remains durable until another mutation/deletion.
- Activation or effect: executor writes model-proposed content automatically when validations pass; actual later consumer reliance is unobserved.
- Evidence limits: prompt compliance and content correctness unobserved; conversation scope enforcement is not present in this inspected edit handler and must not be generalized from reader enforcement.

Guarantee owner/enforcement: EditAtom/apply_atom_edits and update_atom_if_unchanged reject invalid edits, unchanged/empty output and detected concurrent modification. Guarantee strength: protocol for that update path, not semantic correctness or user-consent guarantee. Coverage: this handler; ordinary core/MCP/UI writes use their own admission. External contract: storage implements compare-and-update semantics; implementation of that storage primitive is not audited here.

> let existing = match self.deps.storage.get_atom_impl(atom_id).await {
> --- `crates/atomic-core/src/chat_tools.rs`

> .update_atom_if_unchanged_impl(atom_id, &request, &now, &existing.atom.updated_at)
> --- `crates/atomic-core/src/chat_tools.rs`

#### RT-RTE-wiki-admission
Label: Wiki admission

Endpoints/progression: caller's generation/update request → configured strategy → selected chunks and model synthesis/section operations → either live article save or stored proposal → accept/dismiss. Identities: tag ID, article ID, proposal UUID, base_updated_at. Owner: model/strategy proposes; caller chooses accept/dismiss in review mode; Rust enforces stale-base rejection. Operating modes: reviewed updates, immediate propose-and-accept and direct generation. No expected-answer oracle established. Guidance: stock research/synthesis instructions plus per-tag/global custom prompts; only selected and budget-trimmed chunks reach synthesis. Persistence: article/citations/links and pending proposal; previous article versions archived by the save path as described at the call site. This is a knowledge-product update account, not a demonstrated theory-builder cycle. SRC-1 implementation: `crates/atomic-core/src/lib.rs`, `crates/atomic-core/src/wiki/agentic.rs`, `crates/atomic-core/src/wiki/runner.rs`, `crates/atomic-server/src/routes/wiki.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: article, optional pending proposal, or error/no-change; dismiss deletes the proposal without promotion.
- Later read-back: live wiki readers consume published article/citations; pending-proposal readers can present a future acceptance choice.
- Delegated visibility: research provider sees search results and session chunk IDs; synthesis receives selected, trimmed chunks rather than all search results.
- Selection predicate: configured strategy/tag scope; agentic search filters to captured content, deduplicates chunks and records selected indices; budget trimming limits synthesis input.
- Invalidation or expiry: new proposal supersedes the pending one; stale article ID/timestamp rejects acceptance; generation deletes prior pending proposal best effort, with stale-base check as fallback.
- Activation or effect: acceptance/direct generation changes live article and links; exercise and benefit are unobserved.
- Evidence limits: no human review invariant across alternate modes; local lock is not by itself a cross-process lock; storage archive/restore and section-operation validation internals remain uninspected.

Trigger/proposed change/admission: user/API request or durable regeneration retry; strategy drafts content/ops, software saves proposal or publishes directly, caller can dismiss in reviewed mode. Recovery: stale proposals require regeneration; ledger-wrapped regeneration uses retry/backoff, whereas direct `generate_wiki` lacks ledger interaction. No automatic rollback of a successfully published bad article established here.

Guarantee owner/enforcement: core accept method, local per-tag lock and base identity/timestamp check. Guarantee strength: protocol; covers accept path, not all external database changes or universally human-approved publication. External contract: save/archive and proposal storage operations must succeed; saving and deleting proposal are separate awaits.

> Some(_) => self.accept_wiki_proposal(tag_id).await,
> --- `crates/atomic-core/src/lib.rs`

> if existing.article.updated_at != proposal.base_updated_at
>     || existing.article.id != proposal.base_article_id
> --- `crates/atomic-core/src/lib.rs`

> let kinds = crate::models::KindFilter::only(crate::models::AtomKind::Captured);
> --- `crates/atomic-core/src/wiki/agentic.rs`

#### RT-RTE-report-finding
Label: Report finding admission

Endpoints/progression: manual/scheduled report → per-report task claim → source/context scope resolution → seeded citation ledger and research AgentRun → separate final markdown pass → nonempty guard → finding/provenance/citation write → cache and ledger completion. Owner: caller supplies configuration/instructions; model chooses research and prose; software decides structural admission. No per-finding human approval gate or expected-answer oracle established. Mode: open report instructions over bounded source selection and configurable research rounds, not a controlled improvement experiment. Proposed change: new generated finding atom with report/run identity and output tags. Guidance: stock scaffold, report-specific instructions and final-pass request. Persistence: prose plus only ledger-resolved citation markers actually present in final content. Recovery: failures route to ledger fail/retry-or-abandon; empty source/content completes without writing a finding. SRC-1 implementation: `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-core/src/reports/agentic.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Succeeded with finding ID, EmptyScope, Failed or Skipped; research does not directly publish its intermediate text.
- Later read-back: report/finding readers and enabled generated-content search can consume stored findings; source-only citation policy limits eligible references, not all text the model may have seen.
- Delegated visibility: provider sees initial source batch, report instructions and research tool results; final pass receives research messages plus an instruction to write prose without tools.
- Selection predicate: source scope/window/cap and context filter; report citation policy chooses SeededOnly or Open ledger, then cited_in retains only markers used in final text.
- Invalidation or expiry: resolution-time watermark advances future source-window selection; report deletion/edits and ledger retry rules affect later runs; retained finding expiry not established here.
- Activation or effect: nonempty final content becomes an automatically admitted finding with provenance/citations; groundedness of claims and later reliance remain unobserved.
- Evidence limits: transactional helper is called but its storage internals are not audited here; cache/ledger completion follows the finding write separately, so no end-to-end exactly-once claim; research read_atom and context isolation internals require specialist inspection.

Guarantee owner/enforcement: report runner rejects empty content; ledger determines claim/retry; CitationLedger bounds resolvable citation identities under policy. Guarantee strength: protocol for lifecycle and citation eligibility, not factual support. External contract: storage transactions/claims and structured final-call parser. Covered path: run_report; alternate handwritten atoms/chat answers/wiki do not inherit these gates. No answer oracle is created by the final model pass.

> if output.content.trim().is_empty() {
> --- `crates/atomic-core/src/reports/runner.rs`

> CitationPolicy::SourceOnly => CitationAdmission::SeededOnly,
> CitationPolicy::SourceAndContext => CitationAdmission::Open,
> --- `crates/atomic-core/src/reports/agentic.rs`

#### RT-RTE-capture-write
Label: Capture write

Endpoints/progression: core/MCP request → optional source-URL skip → atom UUID and storage insert → enqueue embed/tag job → optional inline processing → atom return. Owner: principal/caller supplies proposed content; core/software admits without model judging truth. Human authorship is not established merely by caller identity; MCP callers can be computations. Mode: open capture/import, no answer oracle. Guidance: request fields and tool descriptions, not retained method criticism. Alternate direct importer writes SQLite pending rows, and frontend saved answers go through createAtom; these do not establish identical enrichment timing. SRC-1 implementation: `crates/atomic-core/src/lib.rs`, `crates/atomic-server/src/mcp/server.rs`; boundary's inspected `scripts/import/shared/index.js`, `src/components/chat/saveAnswerAsAtom.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: inserted atom or None on optional duplicate-source check; not proof of successful enrichment.
- Later read-back: storage atom readers can retrieve content; enriched search/graph consumers depend on subsequent jobs.
- Delegated visibility: enrichment gets atom ID and resolves content/settings; external MCP client's own context/decisions remain outside Atomic's enclosing-runtime boundary.
- Selection predicate: request content, tags/source URL; nonempty content triggers core enrichment; importer selects source records independently.
- Invalidation or expiry: core invalidates canvas cache; later updates/deletion change stored content; expiry not established by this route.
- Activation or effect: captured content is inserted, enrichment is requested; successful execution and later interpretation are unobserved.
- Evidence limits: duplicate check is not demonstrated atomic uniqueness under concurrency; insert precedes enqueue, so not an audited all-or-nothing capture/enrichment transaction.

Admission/rejection/recovery: software can return duplicate skip or storage error; caller can subsequently edit/delete. No per-content semantic approval, automatic rollback or source-dependent benefit established. Guarantee strength: no claimed guarantee of semantic validity.

> self.storage.enqueue_pipeline_jobs_sync(&[job]).await?;
> self.process_queued_pipeline_jobs(on_event).await?;
> --- `crates/atomic-core/src/lib.rs:1395-1396`

#### RT-RTE-state-maintenance
Label: State maintenance dispatch

Endpoints/progression: enqueued jobs/dirty graph/due task or manual action → standalone scheduler or cloud WorkItem dispatcher → core claim-and-run routines → derived storage and events. Cloud classifies pipeline, maintenance, ingestion and LLM jobs into execution pools; conditional core claims decide actual work after scans. Graph maintenance waits for pipeline idle or staleness, computes edges, centroids and FTS refresh, and advances a dirty watermark. Owner: scheduler/software determines trigger and admission; model-dependent tagging proposes derived tag applications, while numerical graph derivation follows fixed code. Operating mode: recurring maintenance, not expected-answer comparison; no answer oracle established. Guidance: configured tagging prompt/tree, numerical thresholds and task settings. Persisted changes: enrichment/associations, edges/centroids/index state and task statuses, not demonstrated improvements to model parameters. SRC-1 implementation: `crates/atomic-cloud/src/dispatcher.rs`, `crates/atomic-core/src/graph_maintenance.rs`, `crates/atomic-core/src/embedding.rs`, `crates/atomic-core/src/extraction.rs`, `crates/atomic-server/src/main.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: core/dispatcher outcome or progress/error events; manual graph execution returns success/error, not a proof of edge completeness.
- Later read-back: subsequent search/graph/wiki selection can use updated derived state; scheduler consumes task and dirty watermarks on later ticks.
- Delegated visibility: cloud workers resolve the account/database core; tagging receives selected atom text and eligible tag-tree context, not an unrestricted host shell grant.
- Selection predicate: due/claimable jobs and dirty-plus-idle-or-stale graph predicate; tagger status/settings/API-key/target-tree checks can skip tagging.
- Invalidation or expiry: canvas invalidations and dirty watermarks coordinate refresh; cloud delegates lease/backoff recovery to core ledgers; detailed lease expiry enforcement not audited here.
- Activation or effect: software installs derived state and schedules later work; semantic correctness, completeness and benefit unobserved.
- Evidence limits: deterministic status advancement can outpace successful derived computation; direct/manual maintenance variants must not inherit every dispatcher admission or quota property.

Admission/rejection/recovery: software validates and writes derived output; disabled/no-key/no-target tagging can skip, job/provider failure paths emit errors, cloud inspects classified pipeline failures for backpressure. Manual run_now directly executes graph body; no human per-edge/tag approval. Graph failure caveat: caught compute error returns zero, then batch is marked complete; automatic retry of that particular claimed batch is not established. Guarantee owner/enforcement: core claims and watermark code. Guarantee strength: protocol for selected coordination paths, best effort for derived-state completion. Required external contract: database claim semantics and provider outputs; live isolation/reliability unobserved.

> active_pipeline_jobs == 0 || stale
> --- `crates/atomic-core/src/graph_maintenance.rs`

> tracing::error!(error = %e, "Failed to compute graph maintenance edge batch");
> 0
> --- `crates/atomic-core/src/graph_maintenance.rs`

> .set_edges_status_batch_sync(&batch, "complete")
> --- `crates/atomic-core/src/graph_maintenance.rs`

#### RT-RTE-settings-change
Label: Settings change admission

Endpoints/progression: authenticated settings request → core routing → registry/global/per-DB setting write → subsequent AI operations resolve effective configuration. Owner: caller proposes key/value, software routes it; caller may be human or computation. Operating mode: open configuration change, no answer oracle or objective-based variant selection established. Changes can affect prompts, model/service selection and strategies; natural-language instructions are interpreted by models, symbolic settings select fixed code behavior. Guidance: caller settings and source defaults; persisted result is key/value configuration. Explicit-provider mode supplies provider config authoritatively and can prevent stored provider changes from affecting live calls. SRC-1 implementation: `crates/atomic-core/src/lib.rs`, `crates/atomic-server/src/routes/settings.rs`, `crates/atomic-core/src/providers/mod.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: settings write success/error; embedding-space keys have a re-embedding-aware route.
- Later read-back: AI operations read resolved settings; chat custom prefix and wiki custom generation/update prompts enter later requests.
- Delegated visibility: provider receives effective prompts/model parameters; credentials remain client configuration, not an established model-visible channel.
- Selection predicate: workspace-only key, database count and per-DB override routing; explicit provider config overrides provider-related settings.
- Invalidation or expiry: replacement/clearing changes effective settings; embedding-space updates can require re-embedding; no blanket cache/rollback guarantee audited.
- Activation or effect: later requests can use changed configuration; actual later operation/reliance is unobserved.
- Evidence limits: setting write alone does not establish improvement, model identity stability or self-revision of executable machinery; validation and quota/auth details beyond inspected standalone routing remain uninspected.

Admission/rejection/recovery: software writes caller-specified values or returns error; no independent content reviewer in inspected core set_setting. Later replacement/override clearing is available; atomic rollback of derived re-embedding plus settings is not established. Guarantee strength: protocol for routing, no claimed improvement guarantee.

> if settings::is_workspace_only(key) {
>     return registry.set_setting(key, value);
> }
> --- `crates/atomic-core/src/lib.rs`

### Claims

#### RT-CLM-explicit-mutation
Label: Explicit mutation request constraint

Claimed operation: create/edit should occur only on explicit user request. Source: tool descriptions, doctrine/design embedded in implementation; this is policy guidance to the model, not a separate authorization check. The registered mutation handlers implement direct writes after structural/concurrency checks. SRC-1: `crates/atomic-core/src/chat_tools.rs`; see [RT-RTE-atom-mutation](#rt-rte-atom-mutation).

> "Create a new atom with markdown content. Only use this when the user explicitly asks you to create, save, draft, or add a new atom/note. Do not call this for ordinary answers. After creating an atom, mention it in your final response using [[atom_id]] so the UI can link to it.",
> --- `crates/atomic-core/src/chat_tools.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-chat-prompt
Label: Chat prompt authority

Consumer: configured chat model. Channel: system message combining custom_chat_prefix with stock scope/tool instructions and conditional UI context. Force: natural-language guidance, not a code-enforced consent or confidentiality guarantee. Horizon: future turns while stored setting remains effective; current stored history is separately selected/truncated. SRC-1 implementation: `crates/atomic-core/src/agent.rs`; see [RT-RTE-settings-change](#rt-rte-settings-change) and [RT-RTE-chat-turn](#rt-rte-chat-turn).

> Some(prefix) => format!("{prefix}\n\n{base_system}"),
> --- `crates/atomic-core/src/agent.rs`

## Annotations

none
