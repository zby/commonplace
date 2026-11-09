---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Kherad runtime baseline tracing source authoring, model compilation, review, retrieval and alternate admission paths."
run-id: AAS-2026-11-08-kherad-ac3e4da97ac6-01
reviewed-boundary: "2a8d6992b87a33760688e1f956653c21a6292294"
---

# Kherad runtime report

## Runtime account

### Work and evidence basis

Kherad ships an organizational wiki, not a general autonomous coding agent. Its consequential model-dependent work is interviewing and drafting, proposing section replacements, converting uploaded material, compiling source pages into a navigable knowledge bundle, and answering questions through retrieval. The ordinary publication chain separates source authoring, compilation proposals and publication; it does not make every read or every default-branch change pass the same review gate. [SRC-1] `README.md`, `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/routes/ingest.ts`, `apps/api/src/agents/indexer/run.ts`, `apps/api/src/routes/chat.ts`.

All findings below concern inspected implementation or supplied instructions in SRC-1 at the frozen commit. No target code was executed. Model compliance, actual tool grants, exercised recovery, answer quality and benefit remain unobserved. Added inspection beyond the boundary member's initial list includes source-branch selection, concrete indexer and specialist tools, section admission and manual-save branches, shared permission implementation, direct ingest model calls, document-remote admission, skill administration, model construction and MCP tool loading. These are implementation evidence at the same registered source, not new sources. Detailed retained-content revision and epistemic assessments belong to the specialists; this baseline identifies the control and effect paths they can rely on.

### Ordinary invocation: compile, review, answer

An author explicitly saves source Markdown on a long-lived user branch; the shared page writer returns a commit and branch. A reviewer invokes `POST /bundles/:bundleId/compile`, or imports a specialist draft into an LLM-compiled bundle with review permission. The compile endpoint checks bundle existence, review permission, `llm_compiled` mode and configured AI settings; it returns 202 and a run ID. The importer uses the same `startIndexerRun` function after its source write, and can instead return a skipped/failed compile result without undoing that write. [RT-RTE-source-authoring](#rt-rte-source-authoring), [RT-RTE-indexer-compile](#rt-rte-indexer-compile).

The run orchestrator owns progression outside the model. It checks for a recent running row, marks rows older than 30 minutes failed, inserts a run row and launches background work. This is recoverable status bookkeeping, not a durable work queue or proof of mutually exclusive distributed execution: the active-row lookup and insertion are separate operations. The agent branch is `agent/okf-<bundleId>`, not a fresh branch per request. The run loads live raw page identities, compares them with the published mirror, and can terminate successfully without a model call if nothing changed. Otherwise it supplies a full/delta kickoff, existing document names and related document names to the indexer. The model chooses reads and writes; tools return raw content or existing compiled content and accumulate writes/deletions in a per-run map. Code bounds generation to 64 steps. [SRC-1] `apps/api/src/agents/indexer/run.ts`, `apps/api/src/agents/indexer/tools.ts`.

After generation, code rejects an empty pending map. A first compile must supply `index.md`; an incremental compile may copy the existing published index instead. A missing log gets a synthesized entry, but a model-supplied log is not checked for preservation of history. Code rewrites resource URLs, builds source mirror writes, overlays untouched published files onto the long-lived agent branch, commits once, and opens or refreshes an OKF-scoped MR when a diff remains. Thus the model's final text is not the published artifact; accepted tool writes and the orchestrator's transformations are. The terminal run row records success/failure, MR ID and statistics for polling. Exceptions after the initial response are logged and recorded rather than propagated to that caller. [RT-OBJ-pending](#rt-obj-pending), [RT-RTE-indexer-compile](#rt-rte-indexer-compile).

A reviewer approves an open MR. The API checks review permission, resolves the live author-branch head and performs a scope-prefixed squash merge into the bundle's default branch. A no-op returns 409 and keeps the MR open; conflicts become stored conflict rows and a conflict status. Rejection returns open/conflicted MRs to draft on the same branch. Approval reads the live tip, not an immutable content approval token submitted by the reviewer. The ordinary review protocol therefore admits the branch state at the merge call, not necessarily a previously viewed diff. Search synchronization follows the Git change, before recording the merged status; these effects are not shown as one cross-Git/database transaction. [RT-RTE-review-merge](#rt-rte-review-merge).

A reader calls bundle chat with messages and optional thread ID. Code requires view permission and compiled mode, loads settings, checks anonymous IP spend limits, verifies authenticated thread ownership when a thread ID is supplied, and streams a 16-step agent through the AI SDK/Fastify response. The model can read the published index/document tree or invoke semantic/metadata search scoped to that bundle's OKF source. It decides which tools to call and how to answer under a natural-language grounding/citation policy. It is not a deterministic answer checker. The server sends the submitted message array to the model; it does not reconstruct model history from the thread table on POST. Authenticated user and assistant messages are persisted separately, with assistant persistence failures logged. [RT-RTE-bundle-chat](#rt-rte-bundle-chat).

### Forcing routes and guarantee coverage

Four forcing cases materially qualify the ordinary chain:

1. **Draft-source consumption.** Indexer source reads call `getLatestSourcePageAtRef`, whose consumer examines default plus user branches and chooses content by branch-tip commit timestamp. The engine supplies the actual branch list. Consequently unmerged author content can enter compilation and source mirrors; compilation does not certify prior raw-page approval. A newer branch-tip timestamp is not necessarily the latest edit of that particular page. This is an implemented selection rule, not an observed stale-read incident. [SRC-1] `packages/core/src/git/source.ts`, `packages/core/src/git/engine.ts`, `apps/api/src/agents/indexer/tools.ts`.
2. **Attached raw pages in chat.** The chat route appends `buildPageMentionContext` to the system instructions. Supported custom `data-pageMentions` user-message parts select permission-checked raw pages, including latest user-branch content, and instruct the model to prefer them over general recall. This supplies content outside the compiled-only tool surface. Thus “only approved compiled knowledge” describes the chat prompt/tool intent, not every supported context input. Arbitrary submitted conversational text also remains model input. [RT-RTE-bundle-chat](#rt-rte-bundle-chat), [RT-BAP-attached-pages](#rt-bap-attached-pages).
3. **Manual edit save.** Section proposal tools store changes awaiting user decisions, and the ordinary save branch assembles only accepted overrides. However, the same supported save body accepts a `content` string and writes it instead, without querying accepted overrides. Session ownership/agent access and current page edit permission still apply. This is an intentional manual-content route, not a demonstrated way for the model to call the save endpoint itself. “Every saved change must be accepted section-by-section” would be false. [RT-RTE-source-authoring](#rt-rte-source-authoring).
4. **Remote and extension effects.** An admin document-remote pull writes compiled documents to the default branch and reconciles searchable state without an MR. Raw bundle pull likewise directly updates default-branch sources. Specialist MCP tools are an additional effect surface: enabled, attached servers' advertised tool objects are forwarded into the model tool set. Local draft and MR controls do not establish restrictions on those remote tools' effects. [RT-RTE-remote-pull](#rt-rte-remote-pull), [RT-RTE-specialist-session](#rt-rte-specialist-session).

The load-bearing guarantees have distinct owners and strengths:

| Guarantee | Owner and enforcement | Coverage, alternates and external contract | Separate conclusions |
|---|---|---|---|
| Ordinary compilation cannot directly publish its pending writes | Orchestrator commits the pending map to the agent branch and opens/updates an MR; approval endpoint checks review permission | Covers the inspected indexer tool route. Human OKF edits, raw writes and remote synchronization have their own consumers; remote compiled pull does not traverse this MR. Git/DB correctness remains external to the source-level proof. Strength: protocol. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Concept writes have basic structure | `write_concept_doc` calls path and frontmatter checks before mutating `pending` | Covers that tool, with reserved index/log exceptions. Does not check factual accuracy, source entailment, complete index coverage, log preservation or delta-only editing. Other admission routes are not thereby validated. Strength: invariant at this tool boundary. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Organizational grounding and citations | Chat/indexer/specialist instruction text; model is the decision owner | Policy, not semantic enforcement. Attached pages and client messages broaden chat inputs; provider compliance is an external contract not established here. Strength: policy. | instruction conclusion status: wired; compliance conclusion status: uninspected |
| Local access control | API checks plus shared `checkPermission`: admin override, public view, most-specific path grant, then bundle grant | Covered endpoints are named in route records; a bundle check with null path does not perform a per-page filter. Built-in specialist raw reads do check page view; chat uses bundle-level OKF access. MCP has separate remote authorization and cannot inherit a universal local page-control guarantee. Strength: protocol. | implementation conclusion status: wired; deployment conclusion status: uninspected |

Evidence for these boundaries is retained in the route records and [RT-CLM-reviewed-chat](#rt-clm-reviewed-chat). Runtime-client controls are HTTP inputs, permission checks, tool schemas, step bounds and configured provider/tool selection. These are not a process sandbox. Docker Compose separates API, web, Postgres and converter services and mounts the Git repository into both API and web; it does not establish a deployed isolation envelope for model-controlled remote operations. Actual credentials, remote tool inventories, external-provider internals and network policy are unobserved. [SRC-1] `docker-compose.yml`, `apps/api/src/agents/mcp.ts`, `apps/api/src/routes/mcp-servers.ts`.

### Other shipped routes that change the work

Specialist sessions are separate user-owned task contexts, not children spawned by a foreground agent. Creation selects create/edit mode, role, goal, aggressiveness, skills, optional bundle and MCP attachments. Each turn rebuilds instructions from those settings; edit mode adds a fresh section-status recap and tools reading the saved snapshot plus accepted overrides. Create mode can research viewable bundles, read uploads, ask structured questions and write a proposed draft. `ask_question` returns an awaiting-answer payload and a stop instruction; it is not code-level suspension of the entire model loop. Proposals can persist before any import; import/save is separately authorized. See [RT-RTE-specialist-session](#rt-rte-specialist-session) and [RT-RTE-source-authoring](#rt-rte-source-authoring).

The context controls visible here preferentially keep full documents outside the initial window: model-selected index/document reads, semantic snippets, upload reads, section reads and source-delta kickoff. Section tools recommend h3+ granularity but return a requested known section even when a coarse h1/h2 has children. Attached-page assembly retains only the most recent eight distinct mentions and truncates each selected body to 20,000 characters; specialist text quotes use the latest user message, at most six excerpts and 2,000 characters each. These rules bound the generated attachment blocks, not the whole submitted history or token budget. The client and session records can preserve material outside those blocks; the routes inspected do not establish a general summarization/compaction mechanism. Static instructions are rebuilt rather than learned during the call. These are input selection and task-frame separation, not evidence of child-frame execution or behavioral activation. [SRC-1] `apps/api/src/agents/page-mentions.ts`, `apps/api/src/agents/specialist/page-edit-tools.ts`, `apps/api/src/agents/search-tools.ts`, `apps/api/src/routes/agent-sessions.ts`.

Ingestion also calls models without Mastra tools: OCR posts page images to a chat-completions endpoint, STT posts audio to a transcription endpoint, and placement uses `generateText` on an excerpt and source-path list. Their outputs become editable proposed Markdown or placement, not automatic publication. [RT-RTE-ingest-document](#rt-rte-ingest-document). Administrator changes to skill text, model configuration and MCP registry are capability/instruction admission, separate from knowledge review. [RT-RTE-admin-configuration](#rt-rte-admin-configuration). No inspected mechanism here modifies shipped application source code as a consequence of model performance; that is a scope-limited observation, not an exhaustive absence finding.

## Shared records

### Components

#### RT-CMP-indexer-model
Label: Configured indexer model

Source-native identity: `buildModel(settings, "indexer")`, used by the `okf-indexer` Agent. Representational form: distributed-parametric provider model; numerical weights reside at an external provider, not in the Git knowledge bundle. Postgres holds symbolic provider/base URL/model identifiers and encrypted credentials. Parameter changes during operation: no local weight-update operation in the inspected construction/generate path; provider-side changes are uninspected. Exact weight version is not pinned by these settings; an editable model string and endpoint can resolve to different weights. A mutable endpoint can resolve to another model. [SRC-1] `apps/api/src/agents/settings.ts`, `apps/api/src/routes/ai-settings.ts`, `apps/api/src/agents/indexer/run.ts`.

> const modelId =
>     which === "indexer" ? settings.indexerModel : settings.chatModel;
> --- `apps/api/src/agents/settings.ts`

#### RT-CMP-chat-model
Label: Configured chat and specialist model

Source-native identity: `buildModel(settings, "chat")` and `buildModel(settings, "interviewer")` both select `chatModel`; placement uses the same chat selector. Representational form: distributed-parametric inference at the provider; identifiers/credentials are symbolic Postgres settings. No local parameter update is wired in these call sites; provider-side parameter mutation is uninspected. Exact version is not weight-pinned. The admin can change both model ID and base URL; a stable endpoint/model name can also resolve differently externally. Distinct from the independently configured indexer selector, though actual deployments may choose the same model. Evidence: SRC-1 `apps/api/src/agents/settings.ts`, `apps/api/src/routes/chat.ts`, `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/routes/ingest.ts`; selector quotation in [RT-CMP-indexer-model](#rt-cmp-indexer-model) also establishes the shared selection rule.

#### RT-CMP-embedding-model
Label: Configured embedding model

Source-native identity: `createEmbedder` constructs `textEmbeddingModel(settings.model)` at an OpenAI-compatible endpoint. Distributed-parametric inference is external; dense vectors are derived outputs in the search subsystem, while settings are symbolic Postgres values. No parameter update is shown in the embed wrapper; provider internals are uninspected. Exact model weights are not pinned and the configured mutable endpoint can resolve to a different model. The model string filters compatible search chunks but is not a weight digest. Missing settings returns null and semantic search returns an error. [SRC-1] `apps/api/src/lib/embedder.ts`, `apps/api/src/agents/embedding-settings.ts`, `apps/api/src/agents/search-tools.ts`.

> const model = provider.textEmbeddingModel(settings.model);
> --- `apps/api/src/lib/embedder.ts`

#### RT-CMP-ocr-model
Label: Configured OCR model

Source-native identity: `loadOcrSettings` / `callOcrBatch`, default model string `gpt-4o`. Representational form: distributed-parametric external vision model; symbolic Postgres settings select endpoint/model and images are request data. No local weight update occurs in this request path; provider parameter changes are uninspected. Exact weight version is not pinned; mutable endpoint/model selection can resolve to another model. [SRC-1] `apps/api/src/agents/ocr-settings.ts`, `apps/api/src/routes/ingest.ts`.

> const url = `${settings.baseUrl}/chat/completions`;
> --- `apps/api/src/routes/ingest.ts`

#### RT-CMP-stt-model
Label: Configured speech-to-text model

Source-native identity: `loadSttSettings` / `callSttTranscription`, default model string `whisper-1`. Representational form: distributed-parametric external speech model selected by symbolic settings in Postgres. No local parameter-update operation is visible; provider mutation is uninspected. Exact weight version is not pinned; a mutable endpoint can resolve differently. [SRC-1] `apps/api/src/agents/stt-settings.ts`, `apps/api/src/routes/ingest.ts`.

> form.append("model", settings.model);
> --- `apps/api/src/routes/ingest.ts`

The converter additionally delegates document parsing/export to Docling. Its internal models, exact weight identities and mutability are uninspected dependency behavior, not established by Kherad's wrapper; the wrapper constructs PDF pipeline options and exports Markdown/page previews. [SRC-1] `apps/ingest/main.py`.

### Operative objects

#### RT-OBJ-pending
Label: Indexer pending write map

Source-native identity: `pending`, a `Map<string, string | null>` allocated in `runIndexer`. Representational form: symbolic path/deletion map whose string values are natural-language Markdown, with symbolic frontmatter consumed by validators and later indexes. Storage substrate: current-process JavaScript memory until conversion to Git file writes. This is current-run staging, not a durable queue. Tool writes alter the map; only the orchestrator converts it into an agent-branch commit. [SRC-1] `apps/api/src/agents/indexer/run.ts`, `apps/api/src/agents/indexer/tools.ts`.

> const pending = new Map<string, string | null>();
> --- `apps/api/src/agents/indexer/run.ts`

### Routes

#### RT-RTE-indexer-compile
Label: Indexer compilation proposal

Endpoints/progression: reviewer compile request or authorized specialist import → background run row → source/mirror delta → model/tools → pending map → Git agent branch → open/refreshed MR or no-diff completion. Owner: API orchestrator for progression, model for semantic decomposition and tool selection. Context includes static natural-language OKF instructions and symbolic full/delta inventories, with content fetched on demand. State/effects are run-row changes, pending writes, mirror writes and branch commits. Model component: [RT-CMP-indexer-model](#rt-cmp-indexer-model). [SRC-1] `apps/api/src/routes/indexer.ts`, `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/agents/indexer/run.ts`, `apps/api/src/agents/indexer/tools.ts`, `apps/api/src/agents/indexer/prompt.ts`.

- Immediate return: compile endpoint returns run ID/202; model tool writes return staged path acknowledgments, not publication.
- Later read-back: existing published compiled documents and mirrored source state enter a later run; MR publication is separate.
- Delegated visibility: one newly constructed indexer receives kickoff/instructions and its tool results; no parent-agent delegation is shown.
- Selection predicate: live raw pages excluding deletion/redirect rows; mirror diff determines first/delta/no-op; model selects tools/documents within an exposed bundle surface.
- Invalidation or expiry: new source differences drive subsequent compilation; older running rows cease blocking after 30 minutes; pending state dies with process/run.
- Activation or effect: tool calls stage map changes; code commits transformed writes to agent branch and proposes an MR. Model compliance with semantic rules is unobserved.
- Evidence limits: implementation only; no supplied run establishes compilation quality, exact-once execution or benefits of delta selection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: a review-authorized trigger begins an open organizational-content task, not a bounded benchmark. The model proposes compiled text/deletions under OKF rules; code rejects invalid paths/frontmatter, missing writes or first-compile index. The human reviewer can veto publication through [RT-RTE-review-merge](#rt-rte-review-merge). No expected-answer/reference oracle is supplied. Recovery is failure recording and later rerun; the agent branch is reused and untouched files are overlaid from main. Guidance persists as shipped prompt text; produced documents, mirror content and update log persist in Git, not model parameters. This is content compilation, not evidence by itself of formulated theory criticism or improved future capacity.

> if (nothingToDo) {
>     return {
>       mrId: null,
> --- `apps/api/src/agents/indexer/run.ts`

> const frontmatterError = requireFrontmatterType(validPath, content);
>       if (frontmatterError) {
>         return { error: frontmatterError };
>       }
>
>       pending.set(validPath, content);
> --- `apps/api/src/agents/indexer/tools.ts`

The prompt limits incremental rewrites, but the tool does not receive an allowlist of dirty-source-linked output paths. Thus delta-only editing is policy rather than an enforced write exclusion. A run can copy a prior index when the model fails to supply one; no coverage check verifies every concept is indexed. [SRC-1] `apps/api/src/agents/indexer/run.ts`, `apps/api/src/agents/indexer/tools.ts`.

> Leave every other existing OKF concept document untouched (do not call write_concept_doc on them).
> --- `apps/api/src/agents/indexer/prompt.ts`

#### RT-RTE-review-merge
Label: Merge-request admission

Endpoints/progression: open MR → authorized approve → scoped squash merge → search synchronization → merged row; conflict → stored conflict state; reject → draft. Owner: reviewer decides admission, API/Git execute it. State: branch tips, MR rows and conflicts. Natural-language reviewer judgment is separate from symbolic status/permission/merge rules. [SRC-1] `apps/api/src/routes/merge-requests.ts`.

- Immediate return: merged response, no-op/error or conflict response with paths; rejection returns updated draft MR.
- Later read-back: default-branch files become retrievable/wiki-renderable and searchable after synchronization; MR status/conflicts support later review/recovery.
- Delegated visibility: inapplicable — HTTP reviewer action, not a delegated model context.
- Selection predicate: bundle and MR identity, review permission, open status for approval; scope determines path prefix.
- Invalidation or expiry: branch edits change the live candidate; rejection retains branch for rework, not permanent closure.
- Activation or effect: default-branch Git change and search sync admit knowledge to later consumers; answer changes are not observed.
- Evidence limits: source wiring does not prove human inspection, race-free approval, atomic Git/database updates or exercised conflict recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: author/indexer proposes; a user satisfying review permission decides and can reject. `checkPermission` makes admin sufficient and manager the minimum ordinary review role. No answer oracle or automatic truth test is supplied. Operating mode is ongoing open content review; improvement triggers are new edits/compiles and review decisions, not scored experiments. Guidance includes submitted material, diff and comments; retained results are Git content and MR/conflict state. Recovery includes rejection to draft, no-op 409 and conflict state; no automatic reversal after a successful merge is demonstrated in this endpoint.

> const result = await git.squashMerge(
>           mr.branchName,
>           bundle.defaultBranch,
>           `Merge request ${mr.id}`,
>           mrPathPrefix(bundle, mr),
>         );
> --- `apps/api/src/routes/merge-requests.ts`

#### RT-RTE-bundle-chat
Label: Bundle question answering

Endpoints/progression: client messages → view/mode/settings checks → attached-page instruction assembly → model with bundle tools → streamed UI response → optional authenticated message persistence. Owner: user supplies question/history; model selects retrieval and answer; API executes tools and streaming. Forms: natural-language instructions/messages/content and symbolic tool arguments, scope filters and stored message parts. Uses [RT-CMP-chat-model](#rt-cmp-chat-model), optionally [RT-CMP-embedding-model](#rt-cmp-embedding-model). [SRC-1] `apps/api/src/routes/chat.ts`, `apps/api/src/agents/chat/tools.ts`, `apps/api/src/agents/chat/prompt.ts`, `apps/api/src/agents/search-tools.ts`, `apps/api/src/agents/page-mentions.ts`.

- Immediate return: SSE/UI message stream and authenticated thread header when available; tools return content or ranked snippets/metadata/errors.
- Later read-back: authenticated messages are stored and GET can return them; POST consumes caller-supplied history, not a server-loaded thread transcript.
- Delegated visibility: inapplicable — freshly constructed foreground Q&A agent, no inspected subordinate worker route.
- Selection predicate: bundle tools read default-branch OKF files; search enforces bundle/source scope, model identifier for embeddings and optional metadata; raw attachments use per-page view checks.
- Invalidation or expiry: later calls read live default-branch files and current attachment pages; retained thread deletion removes stored history. No general context compaction is established.
- Activation or effect: answer is generated from supplied context/tool outputs; grounding, citations and changed behavior from retrieved content are not observed.
- Evidence limits: no execution trace or oracle; a tool's published-branch restriction does not restrict all client messages/attachment instructions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open questions, not a benchmark. Model is next-step decision maker and answer producer; no reference-answer oracle or human per-answer admission is wired. The 16-step cap and anonymous 10 requests/5 minutes/IP window bound local work/spend, not factual quality or multi-instance abuse. Errors persisting assistant history are logged rather than necessarily failing an already streamed answer. [SRC-1] `apps/api/src/routes/chat.ts`.

> const agentStream = await agent.stream(messages, { maxSteps: MAX_AGENT_STEPS });
> --- `apps/api/src/routes/chat.ts`

#### RT-RTE-specialist-session
Label: Specialist task context

Endpoints/progression: authorized session creation → per-turn owner/admin lookup → settings/uploads/skills/MCP load → create or edit instructions/tools → 24-step streamed model → message persistence/disconnect. Owner: user chooses task and attachments; model chooses research/questions/proposals; API executes. Source-native state includes session goal/role/aggressiveness, saved snapshot, draft, section proposals and messages in Postgres. [SRC-1] `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/agents/specialist/tools.ts`, `apps/api/src/agents/specialist/page-edit-tools.ts`, `apps/api/src/agents/mcp.ts`.

- Immediate return: streamed response; `ask_question` emits selectable question payload; `propose_document` stores a draft and returns its status/length; section proposal returns review payload.
- Later read-back: subsequent turns reload session skills and edit status; tools read accepted overrides/draft-related state, uploads and wiki content. Message history is supplied by the caller.
- Delegated visibility: session has separate messages/state and selected context, not automatic inheritance from another agent; MCP receives arguments through forwarded remote tools, with server internals uninspected.
- Selection predicate: agent-access permission plus session owner/admin; research tools filter bundle/page visibility; create/edit mode determines tools; enabled attached MCP servers supply additional tools.
- Invalidation or expiry: skill loads are live; section proposals block another proposed edit for the same section; snapshot is captured at creation rather than automatically refreshed from live page content.
- Activation or effect: built-in tools persist drafts/proposals, not immediate publication. MCP effects depend on advertised tools and granted credentials, not the local draft protocol.
- Evidence limits: no observed user/model dialogue or remote tool execution; namespace/effect behavior inside Mastra/MCP dependencies is not independently established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes; user accepts/rejects section edits or chooses import/save; software checks proposal IDs and status and current save permissions. Operating mode is an open task with research and clarification. Aggressiveness selects prompt guidance about when to ask, not a numeric truth threshold. No reference-answer oracle is present. Guidance includes role/goal, skill texts, selected excerpts and source pages; proposals/messages/status persist. Rejected sections do not become accepted overrides; re-proposal and manual content save are distinct recovery routes. Remote capabilities do not require the local per-section decision endpoint before executing.

> tools = {
>           ...createSpecialistTools({ db, git, user, sessionId: session.id }),
>           ...mcpResult.tools,
>         };
> --- `apps/api/src/routes/agent-sessions.ts`

> tools[name] = tool;
> --- `apps/api/src/agents/mcp.ts:890-898`

The local capability surface is the union of research/proposal tools and dynamically listed remote tools, not an inspected shell/subprocess grant. The current grant set is session-specific and unobserved. MCP setup/list failures become warnings and skip that server; disconnect is attempted on stream finish, exception and connection close. These are best-effort resource handling, not durable cancellation/retry guarantees. [SRC-1] `apps/api/src/agents/mcp.ts`, `apps/api/src/routes/agent-sessions.ts`.

#### RT-RTE-source-authoring
Label: Draft import and edit save

Endpoints/progression: session draft import or edit save → owned session checks → current target/path edit permission → user-branch commit → session/page update; import may then attempt compilation. Owner: user/API, not a model-exposed commit tool. Content is natural-language Markdown; admission decisions and path allocation are symbolic rules. [SRC-1] `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/lib/write-page-content.ts`.

- Immediate return: save returns commit OID/branch; import returns page and compile outcome.
- Later read-back: saved raw files are available to subsequent source reads and compilation, including before raw-page MR approval through latest-branch selection.
- Delegated visibility: inapplicable — caller's HTTP admission action; no nested worker.
- Selection predicate: import uses stored nonempty draft and resolves create/update target; save requires edit mode and live raw target, then manual content or accepted section overrides.
- Invalidation or expiry: rejected proposals are not loaded as accepted overrides; manual content replaces assembled content; Git history records successive saves.
- Activation or effect: raw content commits to a user branch; publication/compile are separate effects, except optional authorized compile initiation after import.
- Evidence limits: source shows authorized API shapes, not that every caller is a human or that every saved draft was semantically reviewed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: the model stores a proposal/draft, caller chooses save/import, code can reject empty/invalid/unauthorized inputs. No answer oracle; open editing mode. The edit-save `content` string deliberately avoids the accepted-overrides assembly branch, so section acceptance is one admission mechanism, not an invariant of all saves. Recovery is later edits/history rather than an automatic rollback shown here. The guidance that shaped model proposals is retained in specialist prompts/session settings; only content and metadata are committed, not a verified explanation of its correctness.

> if (manualContent !== null) {
>       content = manualContent;
>     } else {
>       const overrides = await loadAcceptedSectionOverrides(db, session.id);
> --- `apps/api/src/routes/agent-sessions.ts`

> const branch = await git.createUserBranch(user.id);
> --- `apps/api/src/lib/write-page-content.ts`

#### RT-RTE-remote-pull
Label: Remote content admission

Endpoints/progression: admin remote pull → decrypted remote credentials → Git pull into default branch → raw/OKF metadata and search reconciliation → remote timestamp/OID update. Separate raw bundle and compiled document endpoints. Owner: administrator selects configured remote and triggers pull; Git helper executes. Forms: symbolic remote configuration/tree paths and natural-language Markdown payloads. [SRC-1] `apps/api/src/routes/bundle-remote.ts`, `apps/api/src/routes/document-remote.ts`.

- Immediate return: changed flags, reconciliation counts/settings or remote/decryption error.
- Later read-back: default-branch raw or compiled content and reconciled searchable records feed wiki, compilation or chat.
- Delegated visibility: inapplicable — remote synchronization rather than a delegated model context.
- Selection predicate: configured bundle subtree for raw pull; document remote supplies compiled tree and can create missing compiled bundles.
- Invalidation or expiry: exact-mirror document pull can remove compiled trees absent remotely; credentials and remote OIDs/timestamps are updated independently.
- Activation or effect: default-branch replacement and index reconciliation bypass local MR approval; no observed downstream answer change.
- Evidence limits: remote contents/server enforcement and exercised recovery are uninspected; caller's admin status does not establish per-document human approval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: remote authors propose content outside this frozen repository; admin trigger plus software pull admits it without local MR veto. Mode is ongoing synchronization, not scored experimentation; no answer oracle. Guidance shaping remote content is uninspected. Remote errors are surfaced as 502 where recognized. No automatic cross-store rollback is shown if reconciliation fails after Git changes. Persisted content/OIDs, rather than model parameters, are the changed knowledge substrate.

> result = await git.pullDocumentsFromRemote(DEFAULT_BRANCH, {
>         url: row.url,
>         branch: row.branch,
>         token,
>       });
> --- `apps/api/src/routes/document-remote.ts`

> const pages = result.changed
>         ? await reconcileRawPagesFromGit(db, git, bundle, await createEmbedder(db))
>         : { upserted: 0, deleted: 0 };
> --- `apps/api/src/routes/bundle-remote.ts`

#### RT-RTE-ingest-document
Label: Ingest conversion and placement

Endpoints/progression: edit-authorized upload → Docling conversion or direct STT → temporary job; optional image OCR replaces job Markdown; optional placement suggestion → caller-supplied commit → user branch/raw page row. Model-free conversion and direct model requests are alternate paths, not Mastra tool invocations. Owner: caller chooses steps and final content; API/converter/provider execute transformations. [SRC-1] `apps/api/src/routes/ingest.ts`, `apps/ingest/main.py`.

- Immediate return: editable Markdown, previews/job ID, placement title/path, or created raw page; failures surface validation/upstream errors.
- Later read-back: only committed source content enters Git source-consumption paths; temporary conversion jobs are not publication.
- Delegated visibility: converter receives uploaded bytes; OCR receives page-image batches; STT receives audio; placement receives first 6,000 Markdown characters and up to 80 existing source path/title rows.
- Selection predicate: bundle edit gates conversion; ownership/bundle checks select OCR job; placement requires compiled mode and configured AI; commit checks final resolved path edit permission.
- Invalidation or expiry: missing/expired jobs are rejected; OCR updates the job Markdown; commit accepts supplied Markdown independently of conversion-job provenance.
- Activation or effect: provider text is returned/staged; explicit commit writes caller content to user branch and upserts raw page metadata, not default-branch publication.
- Evidence limits: wrapper source only; Docling/provider internals, transcription/OCR accuracy and model compliance with placement prompt remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission roles: models/converter propose text or placement; caller supplies final `markdown`, title and path to commit; software checks types, paths, permissions and rewrites embedded images. Placement output is JSON/schema/path checked and collision-allocated, not a factual answer oracle. Operating mode: one uploaded document/open placement request. Guidance asks OCR for faithful transcription and placement for a noncolliding path. The resulting source Markdown persists only on commit; no learned weights or automatic improvement claim follows. Recovery includes retrying failed conversion or editing supplied Markdown; no automatic semantic rejection gate is shown.

> const { text } = await generateText({ model, prompt });
> --- `apps/api/src/routes/ingest.ts`

> const excerpt = markdown.slice(0, 6000);
> --- `apps/api/src/routes/ingest.ts`

#### RT-RTE-admin-configuration
Label: Administrator instruction and capability configuration

Endpoints/progression: admin skill/model/MCP configuration → stored settings/skill records → subsequent session instruction assembly, provider construction or tool loading. Owner: administrator supplies instruction/configuration content; software validates basic fields and persists it. Forms: natural-language skill content and symbolic provider/tool registry fields in Postgres. [SRC-1] `apps/api/src/routes/skills.ts`, `apps/api/src/routes/ai-settings.ts`, `apps/api/src/routes/mcp-servers.ts`, `apps/api/src/agents/skills.ts`, `apps/api/src/agents/specialist/prompt.ts`, `apps/api/src/agents/mcp.ts`.

- Immediate return: updated setting/skill responses; secrets are not returned as plaintext in the inspected AI response.
- Later read-back: sessions reload attached skill contents; new calls construct model/provider from current settings and load enabled attached MCP servers.
- Delegated visibility: specialist sees appended skill text and remote tool definitions; actual remote effects are externally defined.
- Selection predicate: admin-gated configuration; skill attachment IDs choose contents; enabled attached MCP server rows choose advertised tools; model selector chooses indexer versus chat model.
- Invalidation or expiry: skill edits affect later loads; disable/detach prevents later tool loading; model settings changes apply on later construction.
- Activation or effect: instructions and executable remote tool affordances enter subsequent model calls; reliable compliance and actual tool use are unobserved.
- Evidence limits: source cannot establish actual deployment settings, precise provider weights, remote inventories or improvement from a configuration change.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: administrator supplies/edits/replaces content and can delete skills or change configuration. Software rejects malformed required fields; there is no separate model/human critic admission gate in these endpoints. These are ongoing manual configuration modes, with no reference oracle or trace-driven improvement trigger. Guidance is the admitted skill content itself; no required criticism/rationale is persisted. Recovery is a later edit/delete/reconfiguration, not a demonstrated versioned rollback of skill text. This is an instruction/capability change path, not evidence of autonomous self-improvement.

> const content = request.body.content?.trim().slice(0, MAX_CONTENT_CHARS);
> --- `apps/api/src/routes/skills.ts`

> const tools: Record<string, unknown> = {};
> --- `apps/api/src/agents/mcp.ts:845-848`

### Claims

#### RT-CLM-reviewed-chat
Label: Reviewed-content-only chat claim

Claimed operation: chat instructions describe the compiled knowledge base as human-reviewed and the sole source of organizational answers. This is doctrine/policy, with a read-only compiled tool implementation behind part of it. [SRC-1] `apps/api/src/agents/chat/prompt.ts`, `apps/api/src/agents/chat/tools.ts`.

> You answer questions using ONLY the bundle's compiled knowledge base (Open Knowledge Format documents), which you access through your tools. This knowledge base was reviewed and approved by humans — it is your single source of truth.
> --- `apps/api/src/agents/chat/prompt.ts`

The supported raw-attachment path and compiled remote pull qualify the universal reading. See [RT-RTE-bundle-chat](#rt-rte-bundle-chat), [RT-RTE-remote-pull](#rt-rte-remote-pull) and [RT-BAP-attached-pages](#rt-bap-attached-pages). No observed model output establishes either compliance or violation.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-attached-pages
Label: Attached raw pages as primary instructions context

Consumer: chat and specialist model invocations. Channel: page-mention custom parts select permission-checked source files; assembled text is appended to agent instructions. Force: natural-language direction to read and prefer attached material, not deterministic execution or guaranteed compliance. Horizon: current call and follow-up turns when mentions are replayed; source bodies are fetched afresh. Representational form: natural-language content within an instruction string, selected by symbolic mention/bundle/path rules. [SRC-1] `apps/api/src/agents/page-mentions.ts`, `apps/api/src/routes/chat.ts`, `apps/api/src/routes/agent-sessions.ts`.

> const bytes = await git.getLatestSourcePageAtRef(bundle.defaultBranch, bundle.slug, mention.path);
> --- `apps/api/src/agents/page-mentions.ts`

> The user explicitly attached these wiki pages to the conversation. Treat them as primary context for their request — read them before answering, and prefer their content when it conflicts with your general recall.
> --- `apps/api/src/agents/page-mentions.ts`

This is source content being granted model-level interpretive priority; it neither proves all content is malicious nor establishes safe separation from instructions. The latest-branch selection can supply unmerged drafts. Capability to deliver this content is wired; behavioral activation remains unobserved.

#### RT-BAP-session-skills
Label: Session skill instructions

Consumer: specialist create/edit agent instruction construction. Channel: attached skill records loaded from Postgres on each turn, interpolated into natural-language instructions. Force: directive to apply the skills as working method; actual compliance is not enforced by a skill evaluator. Horizon: later turns and sessions attaching the skill, including after an administrator edits it. Storage substrate: Postgres text plus attachment rows; content is natural-language method text, not provider weights. [SRC-1] `apps/api/src/agents/skills.ts`, `apps/api/src/agents/specialist/prompt.ts`, `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/routes/skills.ts`.

> const skillsBlock = ctx.skills.length
>     ? `\n\n## Additional skills\n\nThe following skills were attached for this session by the user or by default for this role. Apply them as part of how you work:\n\n${ctx.skills
> --- `apps/api/src/agents/specialist/prompt.ts`

The admission mechanism is [RT-RTE-admin-configuration](#rt-rte-admin-configuration). Delivery establishes an instruction path, not learning, demonstrated improvement or independent criticism of that method.

## Annotations

none
