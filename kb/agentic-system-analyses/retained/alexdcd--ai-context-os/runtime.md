---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AI-Context-OS runtime baseline tracing desktop chat, MCP context serving and workspace change admission at the public snapshot."
run-id: AAS-2026-10-18-ai-context-os-82777c0c3926-01
reviewed-boundary: "9ed263080cadf98702bebb42d5260b45bd526f6c"
---

# AI-Context-OS runtime report

## Runtime account

### Work and evidence basis

AI-Context-OS (MEMM) supplies selected local knowledge to external agents and its own desktop chat. It is not, on the inspected paths, a general-purpose tool-executing agent loop. The Rust selector decides which memories and detail levels to deliver; a configured provider generates chat text or ingestion proposals; callers decide when to request context and invoke writes. These are separate decision roles, not one autonomous controller. The boundary, source identity and exclusions are fixed in [the boundary](boundary.md). All findings below use SRC-1 at the frozen revision. They concern inspected implementation or source-native instructions, not observed operation. No target, tests, providers or examples were executed.

Added inspection within SRC-1 covers the full context engine through both assemblers; all MCP tool bodies; HTTP transport; chat request shapes, both provider payload builders and response parsers; desktop chat submission; scoring commands; proposal inference, generation, rejection, application and destination validation; memory-save and raw-write guards; provider configuration and model installation commands; CLI scoring and stdio startup; generated reading instructions; connector handoff; index traversal; and optimization-command bodies. These are implementation evidence, except generated natural-language instructions, which also supply doctrine/design. The existing boundary's broader coverage remains in scope; these reads do not establish exhaustive security or algorithmic correctness.

### Ordinary desktop invocation

A human selects a ready provider, types text and sends it. `ChatPanel.handleSend` rejects empty text, a concurrent send and an unready provider, then inserts a user turn and pending assistant turn. Its current `useVaultContext` setting determines whether it calls `buildChatContext`. The frontend passes the current query and a budget; Rust scans the active workspace, reads canonical memories, scores and packages selected material. The frontend then sends all prior local turns plus the new user turn, the system prompt, optional context string, memory IDs and selected model to `chat_completion`. It does not include the pending assistant placeholder in that history. [SRC-1: `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/scoring.rs`]. See [RT-RTE-desktop-chat](#rt-rte-desktop-chat) and [RT-RTE-context-query](#rt-rte-context-query).

The backend loads workspace-scoped provider configuration. With context disabled, it clears the separate context string and IDs. With context enabled but no nonblank context string, it uses the latest user message to rerun selection, with at least a 1000-token nominal budget. A supplied nonblank context is forwarded without this reconstruction. OpenAI-compatible requests put the context in a user message before history; Anthropic requests put it in a first user turn and normalize history roles to user/assistant. The provider, not MEMM's selector, owns answer generation. The Rust consumer extracts a text response and returns IDs/debug data; the frontend replaces the pending turn or renders the error. There is no tool-call execution step in these inspected provider consumers. No answer oracle or correctness evaluation intervenes. [SRC-1: `src-tauri/src/commands/inbox.rs`, `src-tauri/src/core/types.rs`]. See [RT-CMP-inference-provider](#rt-cmp-inference-provider).

Current-run conversation turns accumulate; the inspected send path does not trim or summarize them. Selected vault content is re-created for the current query rather than appended wholesale from previous retrievals. Prior answers can nevertheless retain vault-derived information in history. This is query-time external-context selection, not removal of old turns or a separate agent frame. Successful delivery cannot establish that the provider used the context correctly. [SRC-1: `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/inbox.rs`]

### Other shipped routes and coordination

Desktop startup shares root/config/observability locks with a background HTTP MCP server. It binds loopback port 3847 at `/mcp`, uses stateful local sessions and restricts browser CORS origins. The separate CLI and embedded desktop `mcp-server --root` entry create their own state and serve the same tools over stdio. A stdio server's initial root/config are not the desktop's live shared locks. Transport session identity is distinct from the optional caller-supplied `session_id` used in context observability. No per-user permission set is established by that string. [SRC-1: `src-tauri/src/lib.rs`, `src-tauri/src/cli.rs`, `src-tauri/src/core/mcp_http.rs`, `src-tauri/src/core/mcp.rs`]

MCP `get_context` returns a rules prelude, loaded L1/L2 material and unloaded L0 references. It records selected memory access and attempts observability writes; failures of those accounting steps do not block the returned package. `get_skill` is a separate ID-directed read: full skill body plus immediate required and optional dependency L1 bodies, without the query allocator. Despite the tool description's “full dependency chain,” its inspected loops do not recursively traverse dependencies. Missing dependency files are skipped. The caller owns the next request and any task execution. [SRC-1: `src-tauri/src/core/mcp.rs`]. See [RT-RTE-skill-load](#rt-rte-skill-load).

Static adapters offer another context path: generated `claude.md`, Cursor and Windsurf artifacts give a compact discovery map and tell a host to open canonical files. Their instruction to read L1 before L2 is interpretive policy, not an I/O gate. CLI `show` prints both bodies; CLI `score` computes a separate ranking with empty graph proximity and budgets L2 estimates, rather than executing the shared allocation engine. Connector copy/handoff calls the simulation endpoint but renders only IDs and L0 summaries, not the loaded L1/L2 bodies. Handoff also writes `.ai/scratch/handoff.md`; a later external reader is possible, not demonstrated. [SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/cli.rs`, `src/views/ConnectorsView.tsx`]. See [RT-RTE-adapter-handoff](#rt-rte-adapter-handoff).

### Load-bearing controls and forcing cases

1. **Budget is local accounting, not a complete model-window guarantee.** Owner: Rust engine; enforcement: `select_load_level` and remaining-budget subtraction; strength: invariant for the allocated estimates under ordinary arithmetic inputs, not for actual provider tokens. Covered paths: shared context queries from desktop build/fallback, simulation and MCP. The allocator limits L2 to three high-scoring memories and may downgrade to L1/L0. Required external contract: token estimation must approximate the consuming model. The MCP assembler adds an uncharged prelude and all unloaded references, including budget-exhausted memories; chat also adds headers and history. `get_skill`, static direct reads and CLI `show` bypass this allocator. Thus there is no system-wide output-size cap. [SRC-1: `src-tauri/src/core/engine.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/cli.rs`]

- budget implementation conclusion status: wired
- budget operation conclusion status: uninspected

2. **Context opt-out clears only its dedicated channel.** Owner: backend chat command; enforcement: clearing `context_prompt` and IDs before provider dispatch; strength: invariant for those fields in that command. The Boolean defaults to true in deserialization and is explicitly supplied by desktop chat. A false request can still contain prior vault information in `messages` or `system_prompt`, both forwarded to the provider. A true request with a nonblank caller context bypasses scoring; true with an empty context falls back; failure/empty selection still allows a provider answer. The lower-level provider dispatcher is also used by proposal inference and health checks with explicitly constructed requests. Required external contract: callers must not treat the flag as content provenance filtering or confidentiality isolation. No demonstrated deployment bypass is claimed; the narrower pass-through behavior follows directly from the request shape and consumer. [SRC-1: `src-tauri/src/core/types.rs`, `src-tauri/src/commands/inbox.rs`, `src/components/chat/ChatPanel.tsx`]

- opt-out implementation conclusion status: wired
- opt-out operation conclusion status: uninspected

3. **Protected content is guarded by mutation API, not OS isolation.** Owners: desktop memory/raw-file commands and MCP save; strength: policy with executable rejection on inspected guarded paths. Desktop save permits a restricted unlock transition; MCP rejects an existing indexed protected memory. Raw write checks protected/generated targets, but unlike raw read does not require canonical target containment in root. MCP validates a new destination folder lexically, yet joins the independently supplied `id` to that folder without a kebab-case/path-separator validator in the inspected body. Existing-ID writes instead use the scanned existing path. These distinctions prevent claiming universal path confinement from the folder validator. The registered commands and string wrappers expose these input shapes; ordinary UI selection need not generate them. External hosts can edit files directly under their own OS permissions and are only instructed not to edit protected content. Symlink behavior, actual IPC grants and deployment permissions were not audited sufficiently to claim an exploit or secure isolation envelope. [SRC-1: `src-tauri/src/commands/memory.rs`, `src-tauri/src/commands/filesystem.rs`, `src-tauri/src/core/mcp.rs`, `src/lib/tauri.ts`, `src-tauri/src/lib.rs`]. See [RT-RTE-workspace-write](#rt-rte-workspace-write).

- protection implementation conclusion status: wired
- protection operation conclusion status: uninspected

4. **Inbox promotion is one admission path, not universal human review.** Owner: index traversal for exclusion, proposal command caller for admission; strength: invariant for skipping root `inbox/` during the inspected recursive scan, protocol for proposal review. A nested folder named inbox is not covered by the root-only comparison. MCP defaults new writes to the excluded inbox but also accepts user folders and `.ai/rules`/`.ai/skills`; direct canonical edits are independently consumed. Folder-contract violations produce warnings and are still indexed. Proposal inference produces pending proposals, but `apply_ingest_proposal` itself does not check that the loaded proposal is pending before dispatch. Its `update_memory` and `needs_review` actions change item state rather than update a canonical memory body. Consequently action names and review language cannot establish a universal approval gate or implemented merge capability. Required external contract: a trusted caller chooses whether and what to apply. Frontend wrappers exist; a repository search for their names found declarations, not an exercised review UI. [SRC-1: `src-tauri/src/core/index.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/inbox.rs`, `src/lib/tauri.ts`]. See [RT-RTE-ingest-proposal](#rt-rte-ingest-proposal).

- admission implementation conclusion status: wired
- admission operation conclusion status: uninspected

### Capability, grants and change horizon

The capability surface includes context reads, canonical and raw file writes, session logging, generated-instruction refresh, proposal inference/application, provider configuration and local model installation/removal. It does not establish a current grant set for any particular external agent. HTTP loopback binding is a network placement decision; CORS is not proof of authentication. The HTTP router inspected here adds CORS but no application authentication middleware; dependency-internal controls and deployed host permissions remain uninspected. Shell access, provider-native tools, remote workers and host callbacks are not alternate executors in the inspected chat payload/response path; external hosts may have them under contracts outside this target. [SRC-1: `src-tauri/src/core/mcp_http.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/lib.rs`]

Changes to knowledge and instructions enter through [RT-RTE-workspace-write](#rt-rte-workspace-write) and [RT-RTE-ingest-proposal](#rt-rte-ingest-proposal), then later scanning or router generation can expose them to consumers. Config/model commands admit changes to the inference backend, not target weight training. [RT-RTE-provider-change](#rt-rte-provider-change) keeps that distinction. Optimization analysis creates suggestions from usage/size patterns; the inspected “apply” command updates the suggestion status only. This does not establish autonomous canonical optimization, learning benefit or exercised self-improvement. [RT-RTE-optimization-status](#rt-rte-optimization-status) records the narrower mechanism. Source edits/build/release remain a maintainer-controlled product-change route, not a model-generated successor loop established by this report. No inspected run shows activation, improved retrieval, latency benefit or subsequent behavioral dependence on an admitted change.

## Shared records

### Components

#### RT-CMP-inference-provider
Label: Configured inference provider

Identity: provider selected by workspace `InferenceProviderConfig`, with optional per-request model override. Representational form: distributed-parametric inference; model parameters reside in an external provider or local Ollama/LM Studio service, not in the Markdown vault. Configuration is symbolic JSON on local disk. Parameter change during operation: the inspected client sends inference requests, not weight updates; provider-internal mutation is uninspected. Exact model version pinned: no immutable model/weight digest is required by the inspected request builder. Mutable endpoint resolving another model: possible through base URL/model aliases or configuration changes; exact provider resolution is uninspected. No embedding service is required by the inspected BM25/PPR context route. [SRC-1: `src-tauri/src/commands/inbox.rs`, `src-tauri/src/core/engine.rs`]

> "model": request.model.clone().unwrap_or_else(|| config.model.clone()),
> "messages": messages,
> "temperature": 0.2,
> --- `src-tauri/src/commands/inbox.rs`

The text-only OpenAI response consumer selects the first choice's message content; Anthropic selects the first content block's text. Provider internals, training, context limits and accuracy are uninspected. Packaging these services as “local” does not establish identical versions or offline operation for every configured endpoint.

### Operative objects

#### RT-OBJ-memory
Label: Canonical Markdown memory

Identity: memory file with YAML metadata, L0 summary and L1/L2 body markers; storage substrate: workspace filesystem. Representational form: natural-language body/summary interpreted by humans or models, with symbolic metadata consumed by indexing/scoring and role/dependency selection. These parts share a file, not an identical authority mechanism. This is the runtime container; detailed memory transformations remain for the memory analyst. [SRC-1: `src-tauri/src/core/index.rs`, `src-tauri/src/core/router.rs`, `src-tauri/src/core/mcp.rs`]

> out.push_str("AI Context OS workspace. Canonical knowledge lives in Markdown memories with YAML frontmatter plus `<!-- L1 -->` / `<!-- L2 -->` markers.\n");
> --- `src-tauri/src/core/router.rs`

#### RT-OBJ-context-result
Label: Context query result

Identity: `ContextResult` with loaded/unloaded/scored vectors, rules string and token accounting. Storage: transient Rust values, serialized differently for MCP, chat and simulation. Form: symbolic selection metadata plus natural-language selected bodies and prelude; no parameter update. Chat omits the prelude and unloaded list; MCP includes both. [SRC-1: `src-tauri/src/core/engine.rs`]

> if result.loaded.is_empty() {
>     return String::new();
> }
> --- `src-tauri/src/core/engine.rs`

This quote is from the chat assembler. An empty chat context does not mean the MCP assembler would return no material.

#### RT-OBJ-ingest-proposal
Label: Ingest proposal

Identity: `IngestProposal` with action, state, confidence, rationale, candidate content and derivation/provider fields. Storage: JSON proposal files under the workspace's system paths. Form: symbolic action/state and natural-language rationale/content. It is not itself a canonical memory; application dispatch controls whether content is written. [SRC-1: `src-tauri/src/commands/inbox.rs`]

> action: parsed.action,
> state: ProposalState::Pending,
> confidence: parsed.confidence.clamp(0.0, 1.0),
> rationale: parsed.rationale,
> --- `src-tauri/src/commands/inbox.rs`

### Routes

#### RT-RTE-context-query
Label: Query-selected context delivery

Endpoints/progression: query and nominal budget → scan/read → BM25-informed base scores → top-five graph seeds → PPR-informed scores → skill-required IDs and optional boosts → greedy level allocation → consumer-specific assembly. Owner: Rust code; context/state: active root/config and parsed memories, not an LLM planner. Required dependencies influence selection but do not reserve budget ahead of higher-ranked items. Candidate comparison is deterministic scoring, open-query mode, with no expected-answer oracle or human per-item selection. [SRC-1: `src-tauri/src/core/engine.rs`, `src-tauri/src/commands/scoring.rs`, `src-tauri/src/core/mcp.rs`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP Markdown with rules/loaded/unloaded items; desktop build returns selected chat string and IDs; simulation returns scored entries only.
- Later read-back: future queries rescan retained files; MCP records accesses that subsequent scans can overlay through usage metadata. This report does not assess the revision effect of those counters.
- Delegated visibility: MCP caller receives the assembled string, not an isolated worker execution; chat provider receives the chat assembler's output only.
- Selection predicate: two-pass scores, thresholds relative to the top score, at most three L2 allocations, remaining estimated budget, required/optional dependencies from top-five qualifying skills.
- Invalidation or expiry: context is rebuilt per query; file read failures skip material; changes to files/config affect later queries without invalidating already delivered strings.
- Activation or effect: wired delivery and accounting, not observed model compliance or benefit.
- Evidence limits: estimates do not bound the final provider window; unloaded references/prelude and history are not all charged to this allocator. Scoring accuracy is unmeasured.

> let ppr_scores = personalized_pagerank(&memories, &selected_ids, 0.15);
> --- `src-tauri/src/core/engine.rs`

> let tokens_used = token_budget - remaining_budget;
> --- `src-tauri/src/core/engine.rs`

#### RT-RTE-desktop-chat
Label: Desktop provider chat

Endpoints/progression: user Send → optional context build → `chat_completion` → provider payload → response text → local assistant turn. Owners: user for trigger/context toggle, code for packaging and fallback, provider for answer. State: component turn history and active workspace/provider config. Coordination: frontend `sending` gate and pending-turn identity, then one awaited provider call; no recursive next-action scheduler in this inspected path. Answer oracle: none supplied; operating mode: open conversation. [SRC-1: `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/core/types.rs`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: provider text with memory IDs and optional context debug, or an error rendered in the pending turn.
- Later read-back: current component history is sent on later turns; durable cross-session chat retention is uninspected here and is not inferred from turn accumulation.
- Delegated visibility: configured provider receives system prompt, dedicated context user turn when present and conversation history; no sub-agent frame or tool result protocol is implemented by these builders.
- Selection predicate: user toggle; caller context if nonblank; otherwise latest user query and backend fallback selection when enabled.
- Invalidation or expiry: each send rebuilds retrieval; disabling context clears its dedicated fields, not historical content; provider errors propagate rather than establishing a grounded answer.
- Activation or effect: HTTP request and text delivery are wired; use of delivered knowledge is unobserved.
- Evidence limits: opt-out is not a guarantee that all request text is vault-free; no whole-history token bound or answer-quality oracle was found in this path.

> if !request.include_vault_context {
>     request.context_prompt = None;
>     request.context_memory_ids.clear();
>     context_memory_ids.clear();
> }
> --- `src-tauri/src/commands/inbox.rs`

> messages.extend(
>     request
>         .messages
>         .iter()
>         .map(|m| json!({ "role": m.role, "content": m.content })),
> );
> --- `src-tauri/src/commands/inbox.rs`

#### RT-RTE-skill-load
Label: Explicit skill dependency loading

Endpoints: MCP `skill_id` → indexed skill lookup → full skill L1/L2 → required L1 bodies → found optional L1 bodies → caller string. Owner: MCP tool code; caller chooses ID and later execution. Symbolic role/dependency metadata selects natural-language material. [SRC-1: `src-tauri/src/core/mcp.rs`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: assembled skill/dependency text or not-found/read error.
- Later read-back: canonical bodies remain available for subsequent calls; access recording covers the skill and loaded required IDs in the inspected code, not optional IDs.
- Delegated visibility: caller gets text, not execution in a separate model context.
- Selection predicate: exact ID with Skill role, then immediate `requires` and available `optional` IDs; no recursive dependency walk.
- Invalidation or expiry: scans on invocation; absent/unreadable dependencies are silently omitted; delivered text is not revoked.
- Activation or effect: instruction delivery and some access accounting are wired; skill execution is caller-owned and unobserved.
- Evidence limits: no token-budget guard in this tool; “full dependency chain” is broader than the inspected one-hop implementation.

> for req_id in &skill_meta.requires {
>     if let Some((_, dep_path)) =
>         all_entries.iter().find(|(m, _)| m.id == *req_id)
> --- `src-tauri/src/core/mcp.rs`

#### RT-RTE-workspace-write
Label: Direct workspace content mutation

Endpoints: desktop structured save/raw write or MCP save → local filesystem → index/router refresh or later scan. Owners: caller proposes exact content and invokes write; software serializes/checks/executes. Human versus model authorship is not enforced by these APIs. Admission trigger: explicit command, not autonomous scoring. Guidance: generated Markdown schema/protection rules; MCP ontology enum and folder checks, metadata normalization and existing protected-ID rejection; desktop restricted unlock policy and raw protected/generated-path guards. Caller can refrain or revise; guarded calls can reject, but there is no second human approval step for MCP canonical writes. Open content-editing mode; no answer oracle. [SRC-1: `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/memory.rs`, `src-tauri/src/commands/filesystem.rs`, `src-tauri/src/core/router.rs`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved memory/path or error; MCP can report that content was saved even though router regeneration failed.
- Later read-back: subsequent scans/queries consume successfully parsed files outside excluded paths; generated adapters can expose changed summaries/instructions across sessions.
- Delegated visibility: MCP caller receives outcome; desktop emits memory-change events; actual external host instruction loading is unobserved.
- Selection predicate: desktop indexed ID/raw path; MCP existing scanned ID or new folder plus ID-derived filename. Default MCP inbox writes remain excluded from canonical scans.
- Invalidation or expiry: overwrite changes retained content; no transaction/automatic rollback is shown in the inspected write bodies. Serialization/I/O can fail; router generation can fail after disk mutation.
- Activation or effect: durable writes and refresh calls are wired; later behavioral dependence on edited content is not observed.
- Evidence limits: protection/path checks differ across APIs; lexical destination-folder validation does not validate the independently supplied ID. OS direct edits remain outside these API guards.

> let target_folder = match resolve_memory_folder(&root, params.folder.as_deref()) {
>     Ok(path) => path,
>     Err(e) => return format!("Invalid folder: {}", e),
> };
> target_folder.join(format!("{}.md", params.id))
> --- `src-tauri/src/core/mcp.rs`

> let root = state.get_root();
> if let Some(error) = path_contains_protected_content(&root, Path::new(&path)) {
>     return Err(error);
> }
> --- `src-tauri/src/commands/filesystem.rs`

#### RT-RTE-ingest-proposal
Label: Governed ingestion proposal admission

Endpoints: captured inbox item → duplicate/heuristic proposal → optional provider replacement → pending JSON → caller reject/apply → action-specific persistence. Proposer: duplicate/heuristic code and configured model; decider/veto: caller invoking reject/apply, not model confidence. A command invocation need not establish a human per-content judgment. Trigger: requested item set or all items; pending items are skipped during generation. Operating mode: open ingestion, not a bounded experiment; no expected-answer oracle. Guidance: conservative JSON-only system prompt, response schema, source item and duplicate policy; proposal rationale/contents/provider provenance persist. Inference errors retain heuristic output. [SRC-1: `src-tauri/src/commands/inbox.rs`, `src/lib/tauri.ts`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated/applied/rejected proposal and change/progress events, or error.
- Later read-back: proposals reload from disk; promoted/source memories can enter later canonical scans; input item state and operational log persist.
- Delegated visibility: proposal inference receives the item/schema without assembled vault context; caller receives candidate/rationale; subsequent readers receive only content actually written by the chosen action.
- Selection predicate: requested IDs or all items, pending-proposal skip, hash/URL duplicates; inferred proposal does not replace a duplicate discard. Apply selects proposal ID and action, not a confidence threshold.
- Invalidation or expiry: rejection persists a Rejected state; application persists Applied. Inspected apply does not enforce Pending state or automatic rollback. Writes preceding later log/refresh failures can remain.
- Activation or effect: promote writes a memory; route-to-sources writes a source memory and copies attachments; discard updates state; update_memory/needs_review only mark processed. Downstream use remains unobserved.
- Evidence limits: source names do not establish an implemented canonical update/merge; wrappers establish callable surface, not an observed human review process.

> let system_prompt = "You are generating governed ingestion proposals for AI Context OS. Reply with JSON only. Allowed action values: promote_memory, route_to_sources, update_memory, discard, needs_review. Allowed ontology values: source, entity, concept, synthesis. Keep proposals conservative.";
> --- `src-tauri/src/commands/inbox.rs`

> ProposalAction::NeedsReview | ProposalAction::UpdateMemory => {
>     let _ = update_item_status(
>         &root,
>         &item.id,
>         InboxItemStatus::Processed,
>         ProposalState::Applied,
>     )?;
> }
> --- `src-tauri/src/commands/inbox.rs`

#### RT-RTE-adapter-handoff
Label: Static adapter and connector handoff

Endpoints: scan/manifest → generated adapter/catalog/index; connector action → simulation scores → L0 text → clipboard and optional scratch file. Owners: generator code and human/caller action; external host chooses when and whether to read files. Representational forms: symbolic paths/IDs and natural-language rules/summaries. Canonical edits and explicit regenerate requests trigger replacement of generated artifacts; code admits generated output without model/human review of each line. Guidance: static reading/writing rules. Recovery: regenerate from canonical state; scratch handoff is overwritten on a later handoff. No answer oracle; mode: external-host context handoff. [SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/cli.rs`, `src/views/ConnectorsView.tsx`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated files or copied L0 text and UI feedback; not an executed external-agent task.
- Later read-back: adapters/catalog and scratch handoff are local files potentially read by later host invocations; actual host loading is unobserved.
- Delegated visibility: connector exports summaries and IDs, not selected full bodies or a worker transcript; static adapters expose file pointers for host-directed retrieval.
- Selection predicate: manifest role/index logic; connector uses fixed query `general project context` and 4000/6000 budgets, then maps returned scored entries to L0.
- Invalidation or expiry: regenerate replaces derived artifacts; copied text and already loaded host context are not revoked by file updates.
- Activation or effect: file/clipboard production wired; host instruction compliance and task benefit unobserved.
- Evidence limits: adapter directions are protocol, not enforcement of host I/O; connector simulation output is not equivalent to chat or MCP context assembly.

> text = memories.map((m) => `## ${m.memory_id}\n${m.l0}`).join("\n\n");
> --- `src/views/ConnectorsView.tsx`

#### RT-RTE-provider-change
Label: Provider and local model configuration

Endpoints: settings/caller → save provider config → normalized JSON; local model pull/delete command → Ollama API. Owner: human settings action or other authorized command caller; backend performs persistence/HTTP request. Trigger/proposed change: endpoint/model/config selection or named model installation/removal. Admission/rejection: configuration normalization plus I/O/provider success; user may cancel/change selection. Guidance is configuration, not a learned successor policy. Recovery: save another configuration or pull/delete another model; exact previous-weight rollback is not established. No answer oracle; mode: manual backend management. [SRC-1: `src-tauri/src/commands/inbox.rs`, `src/components/settings/tabs/LocalLLMTab.tsx`, `src/components/settings/tabs/CloudLLMTab.tsx`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normalized configuration or pull/delete success/error.
- Later read-back: later inference loads workspace provider configuration and model name; external service retains installed model state under its own contract.
- Delegated visibility: Ollama receives a model name at loopback API; subsequent chat/proposal requests reach the configured provider.
- Selection predicate: caller-selected configuration/model; no autonomous model tournament or quality-based successor selector established.
- Invalidation or expiry: overwrite config, replace model selection or delete installed model; no client-enforced immutable weight pin.
- Activation or effect: backend replacement/installation requests wired; actual installed versions and later behavior unobserved.
- Evidence limits: changing selected parameters' source is not client weight training; provider availability, downloads and exact model identity were not tested.

> .post("http://127.0.0.1:11434/api/pull")
> .json(&json!({ "model": model_name, "stream": false }))
> --- `src-tauri/src/commands/inbox.rs`

#### RT-RTE-optimization-status
Label: Optimization suggestion disposition

Endpoints: analysis command → usage/size detectors → stored suggestions; apply/dismiss → database status. Owners: detector code proposes, caller marks disposition. Trigger: explicit analysis request, using observability stats and scanned memories. Proposed changes include compression/importance advice, but inspected apply admits a status change, not that content revision. Veto: caller can dismiss; recovery: analysis clears prior pending suggestions and recomputes. Guidance: coded detector thresholds, not formulated criticism of the method. Oracle: none; operating mode: maintenance suggestions, not causal comparison. [SRC-1: `src-tauri/src/core/optimizer.rs`, `src-tauri/src/commands/observability.rs`]

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: suggestions or status update result.
- Later read-back: database suggestion status remains available to maintenance UI/API; canonical edits are not established by this command.
- Delegated visibility: caller receives descriptions/evidence; no executor for the suggested canonical change is invoked in the inspected apply body.
- Selection predicate: detector thresholds over size, usage and memory metadata; disposition by suggestion ID.
- Invalidation or expiry: fresh analysis clears pending optimizations; status can be marked applied/dismissed; content rollback is inapplicable because this apply body edits no canonical body.
- Activation or effect: suggestion/status persistence wired; retrieval improvement and autonomous revision unobserved.
- Evidence limits: a database value `applied` cannot establish that the suggested transformation occurred, much less improved future behavior.

> Some(db) => db.update_optimization_status(id, "applied"),
> None => Err("Observability DB not initialized".to_string()),
> --- `src-tauri/src/commands/observability.rs`

### Claims

#### RT-CLM-context-start
Label: Context at task start

Claimed operation: MCP clients should call `get_context` at the start of every task. Source-native instruction, not a guarantee of host activation; the consumer is an external client/model. [SRC-1: `src-tauri/src/core/mcp.rs`]

> info.instructions = Some("AI Context OS — Intelligent memory system for AI tools. Use get_context at the start of every task to load relevant context.".into());
> --- `src-tauri/src/core/mcp.rs`

#### RT-CLM-protected-edit
Label: Protected memories require unlock

Claimed operation: generated writing guidance forbids edits/deletes before unlock. Inspected mutation APIs supply narrower executable guards as described in [RT-RTE-workspace-write](#rt-rte-workspace-write); externally executed file edits remain host-owned. [SRC-1: `src-tauri/src/core/router.rs`]

> out.push_str("- `protected: true` memories must be unlocked before editing or deleting\n");
> --- `src-tauri/src/core/router.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-provider
Label: Selected knowledge reaches provider

Consumer: configured chat provider. Channel: loaded bodies in an added user message/turn, alongside caller system prompt and full history. Force: advisory natural-language grounding interpreted by the model, not a code-enforced answer obligation. Horizon: current provider invocation; its resulting text can recur in later local history. The selector controls delivery, not truth or compliance. [SRC-1: `src-tauri/src/commands/inbox.rs`]. See [RT-RTE-desktop-chat](#rt-rte-desktop-chat).

> messages.push(json!({ "role": "user", "content": ctx }));
> --- `src-tauri/src/commands/inbox.rs`

#### RT-BAP-workspace-instructions
Label: Workspace guidance reaches host

Consumer: MCP caller or host reading generated adapters. Channel: MCP prelude, skill text and static instruction files. Force: natural-language task/write policy; symbolic metadata separately controls server selection, but cannot enforce a host's direct file operations. Horizon: each delivered package and later sessions that reload retained instructions. Rule prelude carries rule L0 summaries, not necessarily full rule bodies; chat's assembler omits that prelude. [SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/mcp.rs`]. See [RT-RTE-adapter-handoff](#rt-rte-adapter-handoff).

> for rule in &manifest.rules {
>     out.push_str(&format!("- [{}] {}\n", rule.id, rule.l0));
> }
> --- `src-tauri/src/core/router.rs`

## Annotations

none
