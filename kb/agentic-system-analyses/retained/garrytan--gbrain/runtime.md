---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "GBrain runtime baseline: capture admission and publication, MCP controls, context delivery, delegated tool execution and shared-skill revision at the frozen commit."
run-id: AAS-2026-10-11-gbrain-9de8e3c225d3-01
reviewed-boundary: da434385572e0dc0d825649179aabed4107d6e60
---

# GBrain runtime report

## Runtime account

GBrain supplies explicit retained knowledge to existing agents, and also ships internal model-driven jobs. It is not the enclosing conversation runtime in its OpenClaw integration. The CLI, library, MCP transports and context plugin are shipped entry paths; the package wiring and original scope are established in [the boundary](boundary.md). This report keeps its **complete artifact, partial loop** scope. All new evidence below is implementation or separately identified doctrine from SRC-1 at the frozen commit. No target execution, observed trace or causal experiment was supplied or performed. Wiring therefore does not establish use, model compliance, quality or improvement.

### Ordinary invocation: capture text, admit intent, publish, return a receipt

For a local `gbrain capture "a thought" --slug inbox/thought`, the invoking operator or agent supplies the proposed content. The CLI parses options, reads positional/file/stdin bytes, rejects recognized binary signatures, checks for NUL and empty normalized input, and only then decodes or submits text. It allocates or preserves a request UUID. That UUID is the replay identity, not the content hash. Thin-client configuration routes the same proposal to remote MCP; otherwise the CLI first offers it to a resident local owner and falls back to the operation handler on a connected engine. Source resolution precedes the local handler. SRC-1 `src/commands/capture.ts`; [RT-RTE-capture-write](#rt-rte-capture-write).

The handler's dry-run branch returns a preview. The live branch invokes the persistence submission mechanism. Its context distinguishes trusted local CLI (`remote: false`) from agent-facing stdio and authenticated remote principals. Preparation resolves one source, obtains its incarnation, checks replay identity and current authority, validates/normalizes the slug, adds capture frontmatter and computes the normalized-content hash. An existing identical request is reauthorized and returns its earlier result; changed intent under the same request UUID is refused. SRC-1 `src/core/ops/pages.ts`, `src/core/persistence/page-mutations.ts`, `src/core/persistence/journal.ts`.

The owner of the next step changes at admission. The durable journal stores intent and accepted authority; the persistence consumer prepares and publishes rather than allowing the CLI to treat acceptance as completion. Source-incarnation and live-grant checks run under transaction locks at admission and again at publication. Page identity and revision are checked at the publication boundary. File-backed publication records recovery state, publishes the canonical file, applies database changes and commits the receipt. Effects are queued separately; a committed page receipt is not evidence that every derived effect has completed. SRC-1 `src/core/persistence/journal.ts`, `src/core/persistence/coordinator.ts`; [RT-OBJ-persistence-requests](#rt-obj-persistence-requests).

> const outcome = await withCoordinatedWrite(tx, [row.source_id], () => prepared.apply(tx, snapshot), publicationAttribution(row, prepared.trust));
> --- `src/core/persistence/coordinator.ts`

> await queuePublicationEffects(tx, row, final, outcome, prepared);
> --- `src/core/persistence/coordinator.ts`

The waiter starts or wakes the consumer, listens for settlement and polls within the response deadline. Stopping, timeout or read failure need not cancel admitted work. Pending/error responses carry the request identity for inspection or retry. The CLI does not print a fabricated successful page slug for a noncommitted receipt. Committed output includes the receipt/revision and file-write information, as available. SRC-1 `src/core/persistence/service.ts`, `src/commands/capture.ts`.

> if (receipt && receipt.state !== 'committed') {
> --- `src/commands/capture.ts`

This is a software admission decision, not a required human review of each captured statement. Human authorship depends on the caller. Source/type/permission checks do not certify truth. The actual page/fact curation and later memory semantics belong to the memory analyst.

### Selected forcing routes and guarantees

Three forcing cases qualify the ordinary path rather than generalizing its controls to all execution:

1. **Remote versus local dispatch.** Shared MCP dispatch rejects hidden operations, inappropriate local-only/CLI-only calls and missing remote source scope. Handler-level durable authority adds a second boundary for admitted writes. Direct local handlers do not traverse MCP catalog/schema gates. Thus the capability catalog, a connection's allowed operations/scopes and a deployment's isolation are different facts. Current installed grants and filesystem/process isolation were not supplied. SRC-1 `src/mcp/dispatch.ts`, `src/core/persistence/authority.ts`; [RT-RTE-mcp-dispatch](#rt-rte-mcp-dispatch).
2. **File-backed versus database-only publication.** Write-through may be disabled; jobs without an allowed-prefix override can receive a database-only `subagent_sandbox` reason; missing repositories, connector sources, unbound-source policy and mirrors also change file responsibility. This disproves a universal claim that capture always writes a Markdown file. A publication exception can leave durable recovery, and unknown external bytes block rather than authorize blind overwrite. SRC-1 `src/core/persistence/page-mutations.ts`, `src/core/persistence/page-prepare.ts`, `src/core/persistence/coordinator.ts`; [RT-RTE-capture-write](#rt-rte-capture-write).
3. **Durable subagent caller versus generic gateway caller and CLI provider subprocess.** The gateway tool loop accepts optional persistence callbacks and optional per-turn permits. The shipped subagent caller supplies both. A generic library caller need not. The Claude CLI provider is another process, but this adapter explicitly disables its built-in tools, MCP discovery, slash commands and hooks; it returns model output to GBrain's tool loop instead of granting provider-native shell execution. These are launch-protocol controls whose effectiveness depends on the external CLI honoring them, not a demonstrated OS sandbox. SRC-1 `src/core/ai/gateway.ts`, `src/core/minions/handlers/subagent.ts`, `src/core/ai/providers/claude-cli-language-model.ts`; [RT-RTE-subagent-loop](#rt-rte-subagent-loop).

Load-bearing guarantees have these bounded owners and enforcement points:

| Guarantee | Owner / enforcement point | Strength and coverage | Alternate paths / required external contract | Status |
|---|---|---|---|---|
| Identical request replay cannot silently change intent | Persistence admission: digest comparison, principal/request lookup, transaction checks | invariant for inspected journaled page and skill requests | New UUID is a new request; raw database/filesystem changes are outside this check. Requires engine transaction/locking and durable-store semantics. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Revoked/narrowed authority or replaced source can refuse an accepted write | `authorizeWrite` and `authorizeStoredRequest`, at admission and locked publication | invariant within inspected coordinator paths; checks accepted ceiling and live grant, not only token state at initial call | Generic application/raw-engine changes and untraced maintenance producers are not covered by this evidence. Requires database lock serialization with grant mutation. | implementation conclusion status: wired; operation conclusion status: uninspected |
| File/DB divergence has a recoverable protocol rather than one atomic filesystem/database transaction | Durable recovery plus canonical owner, file hashes and receipt transaction | protocol for inspected coordinator file publication | Database-only paths need no file restoration. Native locking, filesystem durability and external DB behavior are dependencies, not independently verified guarantees. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Assistant/pending tool state precedes side effect | Gateway loop order plus the subagent's awaited persistence callbacks | protocol for the inspected durable subagent caller | Optional callbacks mean the standalone gateway does not guarantee durability; pending non-idempotent work is refused on resume, not universally exactly-once. Requires faithful tool idempotence declarations and store commits. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Skill editor cannot silently widen disclosure/policy | Shared-skill admission and publication validation; separate publisher scope | policy enforced by symbolic checks for the inspected remote skill path | Trusted reviewed host import is deliberately different; downstream copies cannot be recalled merely by deleting a canonical head. Requires correct source grants and consuming hosts honoring managed activation. | implementation conclusion status: wired; operation conclusion status: uninspected |

The table is not a universal security assessment. Shell access held by the external host or trusted local operator can alter files outside the request path. Provider callbacks, raw engine mutation, other internal job handlers, grouped publication, scheduler/fleet recovery and administrative topology changes have not been exhaustively traced. Available source is not an access gap, and no absence is inferred from this bounded inspection.

### Consumption and change admission

Requested retrieval and independent context supply are distinct. Query returns selected, redacted, capped evidence rows to its caller; it does not itself demonstrate the caller's final answer. Image query has a separate vector branch with its own scope/filter threading. The OpenClaw adapter independently adds live context, core additions, optional checkpoints, memory instructions and salient-entity pointers on assembly; it returns original messages and a system-prompt addition. Pointers are not automatic full-page delivery. Host model interpretation remains external. SRC-1 `src/core/ops/search.ts`, `src/core/context-engine.ts`; [RT-RTE-query-read](#rt-rte-query-read), [RT-RTE-context-assembly](#rt-rte-context-assembly), [RT-BAP-context-addition](#rt-bap-context-addition).

The internal subagent loop uses distributed-parametric chat judgment to choose tools, symbolic handler membership and replay state to constrain execution, and durable callbacks to coordinate recovery. It stops on no tools, refusal/filter, abort or bounded turns; output-cap termination is distinguished from clean finish. Model/backend selection is configuration-dependent, including a fallback chain and provider-compatible endpoints, not pinned weight identity. SRC-1 `src/core/ai/gateway.ts`, `src/core/minions/handlers/subagent.ts`; [RT-CMP-chat-model](#rt-cmp-chat-model), [RT-CMP-embedding-model](#rt-cmp-embedding-model), [RT-CMP-reranker-model](#rt-cmp-reranker-model).

Shared-skill publication admits instruction/capability material through complete revision proposals, compare-and-swap, policy and dependency-closure checks. It changes canonical files and catalog heads; the read tool describes assets as data, not automatic execution. The authority to edit skills is separate from authority to approve disclosure/runtime requirements. Future downstream activation is not established by publication alone. SRC-1 `src/core/shared-skills/publication.ts`, `src/core/ops/skills-catalog.ts`; [RT-RTE-skill-publication](#rt-rte-skill-publication), [RT-OBJ-shared-skill-heads](#rt-obj-shared-skill-heads).

Maintenance is an additional admission driver. Without `--safe` it previews; with `--safe` it runs stale extraction and source-cycle work chosen from health/doctor state. This is a before/action/after diagnostic workflow, not an answer oracle proving improvement. The cycle includes optional synthesis, patterns, consolidation and skill optimization paths, among others. Their existence does not establish their exact transformation or approval contract; those internals remain for specialist inspection. Product source/release upgrades and production-machinery migration admission were not traced, so this report makes no general autonomous self-modification claim. SRC-1 `src/commands/maintain.ts`, `src/core/cycle.ts`; [RT-RTE-maintenance-run](#rt-rte-maintenance-run).

### Added source coverage and residual limits

Beyond the boundary's initial inspection, this member inspected bounded consequential sections of SRC-1 `src/core/persistence/authority.ts`, `src/core/persistence/journal.ts`, `src/core/persistence/service.ts`, `src/core/persistence/coordinator.ts`, `src/core/persistence/page-prepare.ts`, `src/core/persistence/page-mutations.ts`, `src/commands/capture.ts`, `src/core/ops/pages.ts`, `src/mcp/dispatch.ts`, `src/core/ops/search.ts`, `src/core/context-engine.ts`, `src/core/ai/gateway.ts`, `src/core/minions/handlers/subagent.ts`, `src/core/ai/providers/claude-cli-language-model.ts`, `src/core/shared-skills/publication.ts`, `src/core/ops/skills-catalog.ts`; and complete SRC-1 `src/commands/maintain.ts`, `src/core/ai/defaults.ts`. Scoped searches in SRC-1 `src/core/cycle.ts` identified phase/driver boundaries, not verified phase implementations. This supplies implementation evidence only; comments describing prior tests or performance are not observed runs here.

Retrieval-ranking internals, full read redaction, memory withdrawal, checkpoint banking, core-memory writers, scheduled dream drivers, optimizer/evaluator internals, UI clients, native lock machinery, connector flows and release machinery remain incompletely inspected. These prevent complete loop, universal admission, complete memory-selection, quality and exercised-learning conclusions. They do not prevent the positive bounded runtime findings below.

## Shared records

### Components

#### RT-CMP-chat-model
Label: Gateway chat model

Source-native identity: `chat_model`, per-call `model`, and configured `chat_fallback_chain`, resolved through gateway provider recipes. Representational form: distributed-parametric model; natural-language system/messages and symbolic tool definitions are its inputs. Storage substrate: external provider weights, or external Claude CLI service/session; GBrain caches model client objects, not weights. Parameters changing during operation: uninspected provider internals; inspected gateway performs inference and endpoint/config selection, not a demonstrated parameter update. Exact weight version pinned: not established by model strings. Mutable endpoint can resolve another model: configurable provider/base URL and fallback permit another backend/model; remote alias resolution remains external. SRC-1 `src/core/ai/gateway.ts`.

> if (fallbackChain?.length) return chatWithFallback(opts, opts.model ?? getChatModel(), fallbackChain, chat, { onRefusal: _config?.chat_fallback_on_refusal !== false });
> --- `src/core/ai/gateway.ts`

#### RT-CMP-embedding-model
Label: Gateway embedding model

Source-native identity: `embedding_model`, per-call embedding override, and optional multimodal model. Representational form: distributed-parametric inference producing dense vectors. Storage substrate: external weights; vector outputs stored by engine consumers, not model parameters. Operational parameter mutation: provider internals uninspected; gateway requests inference. Exact weight version pinned: not established; default is a named `voyage:voyage-4` endpoint, not a weight digest. Mutable endpoint can resolve another model: configuration/model override and compatible provider base URLs allow replacement; provider alias mutability is unverified. The gateway refuses to reinterpret an unverified existing embedding identity through a new default. SRC-1 `src/core/ai/defaults.ts`, `src/core/ai/gateway.ts`, `src/core/ops/search.ts`.

> if (cfg.embedding_identity_unverified) throw unverifiedEmbeddingIdentityError();
> return cfg.embedding_model ?? DEFAULT_EMBEDDING_MODEL;
> --- `src/core/ai/gateway.ts`

#### RT-CMP-reranker-model
Label: Gateway reranker model

Source-native identity: `reranker_model` and per-call rerank model. Representational form: distributed-parametric ranking, consumed as numerical ordering signals. Storage substrate: external service weights, ordinary process configuration/client state locally. Operational parameter mutation: uninspected externally; no training finding from this inference interface. Exact version pinned: named model only, not exact weights; default `voyage:rerank-2.5`. Mutable endpoint can resolve another model: recipe/configuration endpoint and model selection can change; external alias resolution uninspected. Configured availability does not prove query activated reranking. SRC-1 `src/core/ai/defaults.ts`, `src/core/ai/gateway.ts`.

> export const DEFAULT_RERANKER_MODEL = 'voyage:rerank-2.5';
> --- `src/core/ai/defaults.ts`

### Operative objects

#### RT-OBJ-persistence-requests
Label: Persistence request journal

Source-native identity: `persistence_requests`. Representational form: symbolic UUIDs, operation, principal, source incarnation, digest, authority, status and recovery fields; the stored intent carries proposed natural-language content whose meaning is not certified by journal admission. Storage substrate: engine SQL table/JSONB through PGLite/Postgres abstraction. It coordinates work/replay, not a model's knowledge of a successful outcome. SRC-1 `src/core/persistence/journal.ts`, `src/core/persistence/service.ts`.

> INSERT INTO persistence_requests
> (principal_kind,principal_id,request_id,operation,source_id,source_incarnation,page_id,slug,
> worktree_id,topology_generation,digest,intent,authority,intent_bytes,terminal_reservation,target_kind,protocol_version,
> admitter_version,admitter_host_id,client_request_id)
> --- `src/core/persistence/journal.ts:228-231`

#### RT-OBJ-shared-skill-heads
Label: Shared skill catalog heads

Source-native identity: `shared_skill_heads`, linked to immutable `shared_skill_revisions` and canonical pack files. Representational form: symbolic source/incarnation/pack/name/revision identity, tombstone and policy epoch. The linked file content includes natural-language instructions and potentially executable assets; those contents have different consumers from the head selector itself. Storage substrate: SQL tables/JSONB plus canonical files and `skillpack.json`. Heads determine later managed catalog selection; they do not themselves execute assets. SRC-1 `src/core/shared-skills/publication.ts`, `src/core/ops/skills-catalog.ts`.

> DO UPDATE SET revision=excluded.revision,metadata=excluded.metadata,deleted=excluded.deleted,policy_epoch=excluded.policy_epoch,updated_at=now()
> --- `src/core/shared-skills/publication.ts`

### Routes

#### RT-RTE-capture-write
Label: Capture write admission and publication

Endpoints/progression: CLI content → registered capture handler → preparation → durable journal → persistence consumer → coordinator file/database publication → receipt. Owner: caller proposes; symbolic persistence checks decide admission; canonical owner executes publication. Source/slug/principal/request UUID, source incarnation and page identity/revision bind state. Local caller, authenticated remote client or agent stdio writer supplies the proposal; human involvement is not inferable merely from lane identity. No per-content human approval is required by this inspected route. No answer oracle. Operating mode: open content request, not experimental successor comparison. Proposed retained-knowledge change: a captured page with provenance/frontmatter; guidance consists of executable source/type/identity/authority constraints, not a model-authored theory. Admission can refuse invalid content/grants, replay mismatch or stale state; publication can refuse current authority, ownership or conflicting bytes. Recovery restores/settles canonical publication from durable before/after state, with unknown bytes held for operator resolution. SRC-1 `src/commands/capture.ts`, `src/core/ops/pages.ts`, `src/core/persistence/page-mutations.ts`, `src/core/persistence/journal.ts`, `src/core/persistence/coordinator.ts`, `src/core/persistence/service.ts`.

- Immediate return: committed receipt and available slug/revision/file-write metadata, or pending/error receipt and retry/inspection guidance; dry-run returns preview.
- Later read-back: committed pages become candidates for subsequent reads; journal receipts are reread for identical request retries and recovery, not assumed final-answer knowledge.
- Delegated visibility: remote writes bind one granted source; job namespace restrictions and source/slug fences apply where carried by authority.
- Selection predicate: explicit/default capture slug, active source incarnation and replay key; publication compares accepted page identity and prepared revision.
- Invalidation or expiry: source replacement/archive, grant revocation/narrowing, revision conflict or canonical byte changes can invalidate publication; this is not a page-retention expiry claim.
- Activation or effect: coordinator applies admitted page state and optional canonical file, queues derived effects, and commits outcome; exercised behavior unobserved.
- Evidence limits: no supplied execution; raw-engine/direct filesystem producers and every grouped/maintenance path not audited; memory meaning/revision semantics not assessed here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await authorizeStoredRequest(tx, row, true, { pageVisibility: skill });
> --- `src/core/persistence/coordinator.ts`

> if ((snapshot?.revision ?? null) !== prepared.observedRevision) throw new OperationError('revision_conflict', 'The page changed during preparation.', 'Read its current revision and submit the updated intent with a new request_id.');
> --- `src/core/persistence/coordinator.ts`

#### RT-RTE-mcp-dispatch
Label: MCP dispatch control path

Endpoints/progression: transport-supplied operation/params/options → shared dispatcher → schema/source/capability checks → operation context → handler → metadata/notices/error or success tool response. Owner: GBrain dispatcher; transport supplies authenticated grant and source state. Policy is symbolic allowed-operation membership, transport flags, required scopes and handler-level authority, not model discretion. It constrains both reads and proposal admission; caller human/computational origin remains unresolved. No answer oracle; open tool-request mode. Dispatch is not a human approval ceremony. SRC-1 `src/mcp/dispatch.ts`.

- Immediate return: tool response or typed error, including notices/retrieval metadata and pending-write details where produced.
- Later read-back: handler-dependent retained data; dispatcher invalidates hot-memory cache after mutating operations, preventing reuse of its pre-write hot state.
- Delegated visibility: source/slug/client restrictions are placed in operation context and checked; actual current grant values were not supplied.
- Selection predicate: registered operation plus optional allowedOps, localOnly/cliOnly, source binding, parameter validation and required scopes.
- Invalidation or expiry: connection grants and handler live-authority checks can deny later calls; hot-memory invalidation occurs on successful mutating handler return.
- Activation or effect: invokes an allowed handler; dispatcher itself neither proves truthful stored text nor successful host-model compliance.
- Evidence limits: transport authentication implementations and all handler-specific fences not exhaustively audited; direct local/library handlers bypass shared dispatch checks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (opts.allowedOps && !opts.allowedOps.has(name)) {
>   return unknownToolEnvelope(name, opts);
> }
> --- `src/mcp/dispatch.ts`

> if ((opts.remote ?? true) && !opts.sourceId) {
> --- `src/mcp/dispatch.ts`

#### RT-RTE-query-read
Label: Requested query evidence delivery

Endpoints/progression: query/image request → granted source scope, filters and evidence plan → text hybrid or image vector search → trust labels, redaction/caps/projection → evidence rows. Owner: query handler and search engine; requesting host chooses when to invoke and what answer to produce. Selection mixes symbolic scope/mode/budget with optional model expansion and numerical retrieval; detailed ranking internals are not established here. The expansion/embedding/reranker interfaces are distinct from final answer authorship. SRC-1 `src/core/ops/search.ts`, `src/core/ai/gateway.ts`.

- Immediate return: evidence rows and retrieval metadata, not a demonstrated final synthesized answer; image route reports unsupported delivery-plan variants where relevant.
- Later read-back: retrieves retained page/chunk evidence; this requested route consumes earlier state rather than establishing its update lineage.
- Delegated visibility: remote granted scope and privacy/safe-chunk restrictions are threaded into query branches; trusted local search can span sources.
- Selection predicate: query or image, source scope, type/date/trust filters, effective limit, detail, evidence plan and optional expansion; ranking internals remain uninspected.
- Invalidation or expiry: uninspected — full hybrid-cache versioning and evidence freshness internals were not traced.
- Activation or effect: supplies capped/redacted/projected evidence for a later consumer; answer influence unobserved.
- Evidence limits: inspected branch wiring and final output wrapper do not establish every upstream exclusion, relevant-result completeness, reranker activation or answer correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return projectRows(capped.map(factRowOutput), rows);
> --- `src/core/ops/search.ts`

#### RT-RTE-context-assembly
Label: OpenClaw context assembly

Endpoints/progression: host assemble callback with session/messages/prompt/tools/budget → deterministic live context and optional core/checkpoint/memory/reflex additions → system-prompt addition and unchanged messages. Owner: GBrain plugin for additions, external host for next conversation step and legacy compaction. Representational form: natural-language context/instructions and pointers generated from symbolic state. Source session identity is sanitized; optional checkpoint failure is fail-open. SRC-1 `src/core/context-engine.ts`.

- Immediate return: original message array, estimated message tokens and combined systemPromptAddition.
- Later read-back: optional checkpoint/core material is supplied during later assembly; its persistence producer and exact retained contents remain uninspected here.
- Delegated visibility: host receives additions; salient-entity reflex detects and supplies compact pointers, not complete page bodies.
- Selection predicate: per-assembly callback; core lane plus available optional memory function, sanitized session checkpoint and turn/window entity resolution.
- Invalidation or expiry: optional checkpoint lookup may fail or omit a block; complete core/checkpoint invalidation policy is uninspected.
- Activation or effect: host-facing system-prompt supply is wired; model uptake is not observed. See [RT-BAP-context-addition](#rt-bap-context-addition).
- Evidence limits: host session identity and prompt interpretation are external contracts; full core/checkpoint producers and OpenClaw host behavior not verified.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> systemPromptAddition: parts.join('\n\n'),
> --- `src/core/context-engine.ts`

#### RT-RTE-subagent-loop
Label: Durable subagent tool loop

Endpoints/progression: job context/prompt and selected tool definitions → prior message/tool replay state → per-turn lease → gateway chat → persisted assistant → pending tool row → registered executor → settled tool result → next model turn or terminal output. Owner: minions handler coordinates persistence/grants; model proposes next tools; gateway loop sequences actions; registered handler executes. State identity combines job/message/ordinal with stable GBrain tool-use UUID rather than trusting provider IDs to be globally unique. Natural-language prompt/history, symbolic registry/replay policy and distributed-parametric model decisions coexist. No reference-answer oracle in this inspected tool loop; open delegated-task mode. Writes proposed through tools are software-admitted under their own constraints, not necessarily reviewed by a human. SRC-1 `src/core/minions/handlers/subagent.ts`, `src/core/ai/gateway.ts`.

- Immediate return: loop final text, stop reason and usage; refusal/filter, length, abort and max-turn outcomes differ from clean completion.
- Later read-back: subsequent job resumes reload subagent_messages and subagent_tool_executions; completed/failed stable tool outcomes short-circuit replay.
- Delegated visibility: selected tool definitions/handlers bound the callable surface; wrapper executes with remote true and jobId; exact installed job grants/tool catalog not fully inventoried.
- Selection predicate: model-emitted tool names must exist in handler map; replay status decides reuse, allowed idempotent retry or non-idempotent refusal.
- Invalidation or expiry: turn/abort/deadline and rate-lease loss stop/requeue work; exact worker retry/dead-letter policy remains uninspected.
- Activation or effect: registered handler executes after durable caller callbacks; results become subsequent model context. Tool-input classifier is observe-only/fail-open, not a veto.
- Evidence limits: generic gateway callbacks/permits are optional; direct chat, legacy Anthropic loop and full worker scheduling are not covered by this durable-route conclusion; no observed execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await opts.onAssistantTurn?.(turnIdx, assistantMessageIdx, chatResult.blocks, chatResult.usage, chatResult.model);
> --- `src/core/ai/gateway.ts`

> if (prior?.status === 'pending' && !handler.idempotent) {
> --- `src/core/ai/gateway.ts`

For the provider subprocess alternative, GBrain's launch contract removes Claude CLI's native tools rather than trusting its unconstrained enclosing runtime. This does not prove credential/state isolation: hermetic configuration is optional. SRC-1 `src/core/ai/providers/claude-cli-language-model.ts`.

> '--tools', '',
> '--strict-mcp-config',
> --- `src/core/ai/providers/claude-cli-language-model.ts`

#### RT-RTE-skill-publication
Label: Shared skill revision publication

Endpoints/progression: complete put_skill/delete_skill proposal → capability/source/incarnation/request/CAS checks → disclosure/dependency closure → journal skill_bundle → canonical-owner coordinator → files and catalog heads/revisions → receipt. Owner: editor proposes, software validates, separate publisher/host authority controls widened policy or reviewed import. Trigger is explicit tool/CLI request; proposed change is a complete skill revision or deletion, not a patch to model weights. Guidance: existing versioned publication policy constrains classes, audiences and requirements; it is applied, not automatically criticized or revised by this route. No answer oracle; open publication-request mode rather than measured variant tournament. Proposal may be computational or human; the remote request alone proves neither human review nor autonomous authorship. Rejection: stale CAS, invalid grants/incarnation, changed policy, malformed closure, widened disclosure or unexplained file edits. Recovery uses coordinator bundle before/after state; a further revision can replace a published head, but downloaded bytes are not recalled. SRC-1 `src/core/shared-skills/publication.ts`, `src/core/ops/skills-catalog.ts`, `src/core/persistence/coordinator.ts`.

- Immediate return: durable publication/deletion receipt, revision and affected skill IDs, or typed refusal/pending response.
- Later read-back: new catalog heads and immutable revision data support later get_skill/get_skill_asset; downstream installation/follow activation was not traced.
- Delegated visibility: remote requires explicit skill_editor plus write and allowed operations; publisher authority is separate; exact deployed grants unobserved.
- Selection predicate: source/incarnation/pack/name and expected_revision; affected dependency heads, policy epoch and current canonical hashes bind publication.
- Invalidation or expiry: publication refuses changed heads/policy/files; deletion revokes future managed activation, not previously downloaded bytes; detailed lease/retention behavior uninspected.
- Activation or effect: canonical files, manifest and SQL heads/revisions change under coordinator; asset retrieval is described as data-only, not automatic execution.
- Evidence limits: host-import implementation, managed activation and full shared-file policy consumers were not audited; publication does not establish operational improvement or model compliance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (policy.epoch !== intent.policy_epoch) {
> --- `src/core/shared-skills/publication.ts`

> throw opError('approval_required', 'Widening an existing skill disclosure or file class requires a trusted owner-reviewed import, not editor authority.',
> --- `src/core/shared-skills/publication.ts`

#### RT-RTE-maintenance-run
Label: Conservative maintenance driver

Endpoints/progression: CLI maintain options → health and doctor before-state → stale extraction action and per-source cycle actions → health/doctor after-state → report. Owner: maintain command; symbolic counters and cycle_freshness diagnostics choose work. Human/computational caller can authorize apply mode with --safe; starting it is not per-content approval. Proposed changes: stale database extraction and selected source cycles; exact synthesized revisions belong to uninspected phase implementations. Guidance: executable freshness/runbook policy determines action eligibility. No expected-answer oracle; health/doctor outputs are diagnostic outcomes, not independent proof of semantic quality. Operating mode: default bounded preview, explicit safe apply. Software skips empty actions and reports failed cycle as blocked; deeper phase veto/rollback remains uninspected. SRC-1 `src/commands/maintain.ts`, `src/core/cycle.ts`.

- Immediate return: before/action/after health and doctor report, in JSON or human-readable form.
- Later read-back: extraction/cycle changes can become later retained-state inputs; exact changed artifact inventory and consumers remain uninspected.
- Delegated visibility: cycle is passed a selected sourceId and optional local brainDir; inner/global phase scope needs separate inspection.
- Selection predicate: stale_pages greater than zero and non-ok cycle_freshness messages naming source IDs; --safe permits execution unless --dry-run is also present.
- Invalidation or expiry: freshness diagnoses recur; full phase cache, lease and rollback policies not established here.
- Activation or effect: apply mode invokes extraction/cycle functions; preview only emits would_apply actions.
- Evidence limits: full cycle transformations, scheduler invocation, skill optimization, evaluator comparisons and observed before/after runs remain uninspected; diagnostic changes alone would not identify learning or successful self-improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> dryRun: args.includes('--dry-run') || !safe,
> --- `src/commands/maintain.ts`

### Claims

#### RT-CLM-memory-control
Label: Explicit memory under user control

Claimed operation: GBrain gives existing agents explicit memory with sources, correction/withdrawal and keyless retrieval, with optional semantic/synthesis/background work. This is doctrine, not an empirically established across-host continuity or quality guarantee. Source: SRC-1 `README.md`, also retained in `boundary.md`.

> GBrain stores explicit facts with their sources, supports corrections and withdrawal, and makes the same memory available across your agents.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-addition
Label: Context addition to host model

Consumer: enclosing OpenClaw conversation model through the host context engine. Channel: returned systemPromptAddition containing live/core/checkpoint additions, memory instructions and entity pointers. Force: natural-language instruction/knowledge supply, interpreted by an external model; deterministic composition does not imply deterministic behavior. Horizon: current assembly/turn; retained checkpoint/core supply can extend across later callbacks, with producer/retention limits stated in [RT-RTE-context-assembly](#rt-rte-context-assembly). SRC-1 `src/core/context-engine.ts`.

> if (checkpointBlock) parts.push(checkpointBlock);
> if (memoryAddition) parts.push(memoryAddition);
> if (reflexAddition) parts.push(reflexAddition);
> --- `src/core/context-engine.ts`

## Annotations

none
