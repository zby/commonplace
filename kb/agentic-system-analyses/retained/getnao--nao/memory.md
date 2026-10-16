---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "nao's user-memory extraction, conversation checkpoints, saved-file read-back and retained context recommendations at the frozen commit."
run-id: AAS-2026-10-14-nao-f9d36a4b7276-01
source-identity: "https://github.com/getnao/nao"
reviewed-boundary: "0085625a8fd22e4f404b6a3971d153f6b6699479"
---

# nao memory report

## Boundary and evidence

This report covers the retained material and context controls of the enclosing nao runtime at SRC-1, commit `0085625a8fd22e4f404b6a3971d153f6b6699479`. It includes automatic user-memory extraction, manual maintenance, raw conversation replay, compaction, saved files and story replay, project context delivery, skills, delegated frames, and recommendations derived from usage. It does not equate all persisted output with learned guidance. Static shipped context is relevant to working-context control but is not itself read-back accumulated through use.

Direct reads add implementation coverage of the memory service, extractor, queries, both DB schema memory ranges, tRPC mutations, prompt selection, compaction model and selector, saved-file operations, built-in tool registration, CLI dispatch and recommendation persistence/reconciliation/prompt rendering. Prompt texts supply doctrine/design, not evidence of reliable model behavior. Other caller and delivery findings explicitly rely on the supplied runtime records. No additional source is registered. No target code, tests, examples or services were executed.

| Entry point or operation | Source path and inspection basis | Coverage and local limits |
| --- | --- | --- |
| Stream-triggered extraction | Direct: `apps/backend/src/services/agent.ts`, `apps/backend/src/services/memory.ts`, `apps/backend/src/agents/memory/memory-extractor-llm.ts` | [MEM-RTE-memory-extraction](#mem-rte-memory-extraction); stream input, not current response verification, supplies traces. |
| Active-memory reload and default prompt | Direct: `apps/backend/src/queries/memory.ts`, `apps/backend/src/components/ai/system-prompt.tsx`, agent prompt-building range | [MEM-OBJ-memories](#mem-obj-memories), [MEM-BAP-user-memory](#mem-bap-user-memory); alternate prompt replacement qualifies delivery. |
| Human edits, deletion and disabling | Direct: `apps/backend/src/trpc/memory.routes.ts`, memory queries; frontend memory route redirect | [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance); full account-settings caller not inspected, so no UI-completeness assertion. |
| Compaction production and rehydration | Direct: `apps/backend/src/services/compaction.ts`, `apps/backend/src/agents/compaction/compaction-llm.ts`, `apps/backend/src/utils/ai.ts`, agent step range | [MEM-RTE-chat-compaction](#mem-rte-chat-compaction); alternative streaming/nonstreaming checkpoint persistence distinguished. |
| Raw history, edited suffix, SQL/story result replacement | Direct: agent message-preparation/story-sync/pruning ranges; supplied web route for persistence and suffix supersession | [RT-RTE-web-chat](runtime.md#rt-rte-web-chat), [MEM-OBJ-compaction](#mem-obj-compaction); raw DB transcript differs from later model input. |
| Chat forks and selected-story forks | Located in `apps/backend/src/queries/chat.queries.ts`; agent reads fork metadata | Not traced through fork producer/copied payload. Prevents a complete account of alternative fork initialization, including whether compaction markers are copied or discarded. |
| Saved output files, attachment pointers, explicit read | Direct: `apps/backend/src/services/storage/user-files.ts`, `apps/backend/src/agents/tools/read.ts`, `apps/backend/src/agents/tools/write.ts`, agent attachment range | [MEM-RTE-saved-files](#mem-rte-saved-files); binary conversion, full deletion policy and each storage-provider implementation remain uninspected. |
| Custom-story versions/draft mount and opaque app state | Direct story-sync range and read/write dispatch; supplied ordinary write boundary | [RT-CLM-context-readonly](runtime.md#rt-clm-context-readonly); known latest-version replay. Full story publication, app-state and blob-cleanup chains uninspected; no claim that all story payloads are automatically recalled or derived guidance. |
| Skills, citation/table expansion, explore frames | Direct preparation chain and tool registration; supplied explore/working-context account | [RT-RTE-explore-task](runtime.md#rt-rte-explore-task), [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance); detailed dynamic load_skill output and forked-skill behavior not traced. |
| Recommendation generation, reconciliation, dismissal and later selection | Direct: `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/services/context-recommendations.reconcile.ts`, query selection ranges, recommendation prompt | [MEM-OBJ-context-recommendation](#mem-obj-context-recommendation), annotation on [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation). Feedback fallback internals and full query_app_db filtering uninspected; no exhaustive lineage/security claim. |
| PR creation, live Git refresh, CLI sync and deployment context | Supplied runtime delivery/recommendation findings; direct CLI dispatcher | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); provider-specific outputs and API upload admission remain uninspected. Merge, deployment and content-quality approval not established. |
| Tests, automations, MCP and messaging callers | Supplied runtime routes and channel creation-site findings | [RT-RTE-test-answer](runtime.md#rt-rte-test-answer), [RT-RTE-automation-run](runtime.md#rt-rte-automation-run), [RT-RTE-mcp-chat](runtime.md#rt-rte-mcp-chat); channel-specific history and memory policy not independently traced. Direct MCP tools do not inherit enclosed-chat retention by implication. |
| Remote model/provider state | Inspected selection wrappers; external implementation outside frozen repository | [MEM-CMP-memory-extractor](#mem-cmp-memory-extractor), [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model); opaque provider retention/training cannot be classified from local adapters. |

The compact table names operative alternatives even where they were not traced. These are inspection limits, not unavailable repository evidence. External services and deployed state are not frozen; actual operation, semantic accuracy, permissions and benefit remain unobserved.

## Core ideas

1. User memory is a separate, user-scoped store. A model derives directives and personal facts from a bounded text-only conversation sample; code admits its normalized output without per-item human approval. Later default prompts automatically supply a budgeted subset, excluding memories attributed to the current chat. This is neither transcript replay nor task-targeted semantic retrieval. [MEM-OBJ-memories](#mem-obj-memories), [MEM-RTE-memory-extraction](#mem-rte-memory-extraction).
2. Compaction is a second trace-fed transformation with a different horizon. A summary replaces the old prefix in the working window; a successful streamed marker can reconstruct summary plus recent turns on continuation. The summarizer itself can see only a budget-selected suffix of that prefix. Older messages remain retained as raw history, but later summarization cannot be assumed to preserve everything. [MEM-RTE-chat-compaction](#mem-rte-chat-compaction).
3. Files and stories are durable work products with read-back routes, not automatically extracted rules. Storage documents enter the window as path descriptions until an explicit read; story history is refreshed to current DB content and older duplicates are suppressed. A path is not an automatically dereferenced model pointer. [MEM-RTE-saved-files](#mem-rte-saved-files), [RT-RTE-web-chat](runtime.md#rt-rte-web-chat).
4. Context recommendations retain diagnoses and proposed edits separately from live project context. Prior findings reach later diagnostic runs only as summaries; dismissed fingerprints constrain deterministic reconciliation. PR creation, an applied status, repository merge and live delivery are different operations. [MEM-OBJ-context-recommendation](#mem-obj-context-recommendation), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

## Shared records

### Components

#### MEM-CMP-memory-extractor
Label: Memory extractor model

Source-native identity: MemoryExtractorLLM resolved by MemoryService using the project's `other` model selection or annotation/extractor fallback. Representational form: distributed-parametric. Storage substrate: provider-hosted weights; the repository retains configuration and usage, not weights. Parameters changing during operation: no local update step in the inspected extraction wrapper; provider internals uninspected. Exact version pinned: no weight digest established. Mutable endpoint resolving to another model: afforded by the shared configurable provider resolver, but external alias behavior uninspected. This is a distinct call role from [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) and [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model), even if selected model IDs coincide. SRC-1: `apps/backend/src/services/memory.ts`, `apps/backend/src/agents/memory/memory-extractor-llm.ts`; provider resolution limits are supplied by the runtime model record.

> const pinned = await resolveDefaultModelSelection(opts.projectId, 'other');
> --- `apps/backend/src/services/memory.ts`

### Operative objects

#### MEM-OBJ-memories
Label: User memories

Source-native identity: `memories` DB rows. Natural-language operative content is a normalized directive (`global_rule`) or personal statement (`personal_fact`). Symbolic access/lineage metadata comprises ID, userId, nullable chatId, category, timestamps and supersededBy. Substrate: SQLite or PostgreSQL tables. The schemas do not give these rows a projectId; reload filters userId and active status. A project setting controls use, not project-local content scope. Initial rows' provenance is not established by schemas alone; the traced producer is extraction and the traced editor is the user mutation path.

This is distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): persisted memory supplies that assembled string rather than being the string. The actual analytics consumer receives category/content, not row IDs, chat lineage or supersession history. Extraction instead reloads active rows with IDs for replacement selection. Recommendation prompts also request mining global rules through the app DB; complete view admission/filtering remains uninspected. SRC-1: `apps/backend/src/db/pg-schema.ts`, `apps/backend/src/db/sqlite-schema.ts`, `apps/backend/src/queries/memory.ts`, `apps/backend/src/services/memory.ts`, `apps/backend/src/components/ai/context-recommendations-prompt.tsx`.

> const memories = await memoryQueries.getUserMemories(userId, excludeChatId);
> return memories.map((memory) => ({
> category: memory.category,
> content: memory.content,
> }));
> --- `apps/backend/src/services/memory.ts`

Reasons for each directive are not retained in this schema. chatId is provenance metadata, not the original reasoning. Superseded rows remain stored but active retrieval excludes them. The schema sets chatId null when its referenced chat is deleted; this is not automatic withdrawal of derived content. User deletion cascades memory rows. Physical deletion of a replacement does not clear other rows' supersededBy through the inspected delete query; no automatic restoration of the older rule is established.

#### MEM-OBJ-compaction
Label: Conversation compaction marker

Source-native identity: `data-compaction` part with summary and optional error/usage. Representational form: natural-language summary plus symbolic part type/status/usage. Substrate: working model-message array and, on streaming completion, persisted UI message parts. Lineage: the pre-last-user prefix of prepared model messages, then image stripping and token-budget selection. This is a material checkpoint part of the web-chat route, not a duplicate route or the external compaction model.

Part of: [RT-RTE-web-chat](runtime.md#rt-rte-web-chat)

The parent is a route rather than an object because it encloses checkpoint production and persistence. Other streaming callers can use the same marker mechanism. Immediate consumer: subsequent tool-loop steps; later consumer: conversation reconstruction through useLastCompaction. Failure markers with empty summaries are not selected as valid checkpoints. SRC-1: `apps/backend/src/services/compaction.ts`, `apps/backend/src/services/agent.ts`, `apps/backend/src/utils/ai.ts`.

> if (part.type === 'data-compaction' && (part.data.summary ?? '').trim() !== '') {
> return [part.data, i];
> }
> --- `apps/backend/src/utils/ai.ts`

#### MEM-OBJ-context-recommendation
Label: Context recommendation

Source-native identity: DBContextRecommendation values persisted by applyActions/upsertFields. Substrate: application DB. Natural-language parts: rootCause, title, summary, suggestedAction, fixGuidance and fixPrompt. Symbolic parts: fingerprint, suggestedFile, subjectKey, status, counts/scores, source model/run IDs and feedback/trigger references. Proposed edits are structured paths and patch text whose content requires interpretation; they are not live context until separately admitted. Reasons and trace pointers are retained here, unlike extracted user-memory rows.

Part of: [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation)

This names a retained result inside that supplied route, not a second declaration of the diagnostic route. Lineage: model-collected findings, reference repair, fingerprint grouping, scoring, then transaction and feedback coverage/normalization. Later diagnostic prompts display only status, fingerprint, file, subjectKey and title from existing findings. Thus storage of full rootCause/insights does not establish automatic rationale delivery to the next diagnostic model. The PR/manual-fix surfaces can consume proposed edits/guidance; their runtime admission separation is supplied by the parent record. SRC-1: `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/services/context-recommendations.reconcile.ts`, `apps/backend/src/components/ai/context-recommendations-prompt.tsx`.

> [{r.status}] fingerprint={r.fingerprint} file={r.suggestedFile} subject={r.subjectKey} — {r.title}
> --- `apps/backend/src/components/ai/context-recommendations-prompt.tsx`

#### MEM-OBJ-user-files
Label: Permanent user files

Source-native identity: scoped storage keys for uploaded documents and produced text/binary outputs. Substrate: configured local or S3 provider; provider implementation and deployment durability are not audited here. Form: opaque binary payloads or text/data interpreted after readable conversion; key/path/size/media type are symbolic metadata, not the payload's meaning. Lineage: user-supplied bytes, foreground-model-authored text, or files produced elsewhere through byte/from-disk APIs. Model-visible read output is converted text, not necessarily original bytes. This is distinct from [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context), whose scope identifiers select access, and from raw transcript tool results. SRC-1: `apps/backend/src/services/storage/user-files.ts`, `apps/backend/src/agents/tools/write.ts`, `apps/backend/src/agents/tools/read.ts`.

> return toReadableText(relativePathFromKey(scope, key), await readUserFileBytes(scope, relativePath));
> --- `apps/backend/src/services/storage/user-files.ts`

### Routes

#### MEM-RTE-memory-extraction
Label: User memory extraction

Endpoints/progression: AgentManager.stream request dispatch → safeScheduleMemoryExtraction with supplied UI history → enabled check and provider resolution → bounded text sampling plus existing active memories → structured extractor output → normalization and replacement-ID filter → transaction → later prompt reload. Owner: software triggers and admits; the model proposes content/replacements. User utterances author source material but do not constitute per-derived-item approval. Users can later edit, delete or disable use. This is a distinct trace-fed suboperation of [RT-RTE-web-chat](runtime.md#rt-rte-web-chat), also reachable through reuse of streaming managers; it is not that full invocation.

- Immediate return: fire-and-forget scheduling; errors are logged rather than failing the foreground request.
- Later read-back: active category/content enters later default prompts via user-scoped query and a 1000-token content budget; extractor also reloads existing active rows for future supersession decisions.
- Delegated visibility: extractor receives at most 17 recent UI messages, text only, truncated to 1250 characters each except the latest user text at 2000; existing memories are appended in a separate user message.
- Selection predicate: user and project enablement; latest user text at least 3 characters; model selection; recent user/assistant text; output categories; supersedes_id must name a loaded existing row.
- Invalidation or expiry: replacement marks old row superseded; manual deletion removes a row; disabling prevents extraction/injection, without deleting content; no timed expiry found in these inspected queries.
- Activation or effect: code inserts normalized natural-language content and marks replacements in a transaction. Later delivery is wired; changed model behavior or improved future capacity is unobserved.
- Evidence limits: extractor permanence/accuracy is requested, not independently validated; mixed user/assistant text feeds it, not just verbatim user declarations. It does not inspect current-response correctness before writing. Concurrency and provider behavior untested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission rejects empty normalized text and invalid replacement IDs, not false or unsafe meanings. The prompt asks for permanence signals for directives, persistent profile facts, English text, and default no change. Structured schema checking is not an answer oracle. Mode: automatic extraction from an open conversation, not an experiment. Guidance persists as compressed directives/facts without explanatory rationale. Failed extraction logs an error; successful writes precede inference telemetry persistence, so downstream telemetry failure is not proof of no write. SRC-1: `apps/backend/src/services/memory.ts`, `apps/backend/src/agents/memory/memory-extractor-llm.ts`, `apps/backend/src/types/memory.ts`, `apps/backend/src/components/ai/memory-system-prompt.tsx`.

> const recent = uiMessages.slice(-CONVERSATION_MESSAGE_LIMIT);
> --- `apps/backend/src/agents/memory/memory-extractor-llm.ts`

> ].filter(({ supersedesId }) => (supersedesId ? existingIds.has(supersedesId) : true));
> --- `apps/backend/src/services/memory.ts`

#### MEM-RTE-memory-maintenance
Label: User memory maintenance

Endpoints/progression: projectProtectedProcedure edit/delete/setEnabled → current-user-scoped query → retained content/change of enablement → future extraction/default prompt query. Owner: authenticated caller supplies an edit, deletion or enablement decision; software checks shape/ownership and performs I/O. The mutation is an afforded human content-admission surface, although full UI caller wiring is not inspected. Distinct from automatic extraction; neither mutation creates project-scoped memory. SRC-1: `apps/backend/src/trpc/memory.routes.ts`, `apps/backend/src/queries/memory.ts`.

- Immediate return: edited row, enablement flag, or completed delete; absent-owned-row raises NOT_FOUND.
- Later read-back: edited active content enters later default prompts/extractor input; deleted content is absent from later queries; disablement bypasses use without erasing rows.
- Delegated visibility: edit supplies text/ID; the model need not participate in this write.
- Selection predicate: ctx.user.id plus memoryId, with trimmed nonempty edit input up to 1000 characters before normalization; enablement is a user flag gated also by project settings during use.
- Invalidation or expiry: physical delete; in-place edit; disabled use. Reenabling can expose remaining rows again. No automatic restoration of superseded predecessors is wired by the delete query.
- Activation or effect: content or flag changes are implemented; no exercised downstream model reliance established.
- Evidence limits: full authenticated-procedure implementation and account-settings UI not inspected; this does not establish all possible memory writers or per-item confirmation of extraction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/admission: caller submits specific changed content or withdrawal and software accepts after input/ownership checks. Rejection: schema errors/empty normalized input/not found. Recovery: no undo history or content-quality comparison is established by these mutations. Answer oracle: none. Mode: direct maintenance, not optimization. SRC-1: `apps/backend/src/trpc/memory.routes.ts`.

> const content = memoryService.normalizeMemoryContent(input.content);
> --- `apps/backend/src/trpc/memory.routes.ts`

#### MEM-RTE-chat-compaction
Label: Chat history compaction

Endpoints/progression: prepareStep token estimate → model summarization of selected prefix → in-place message replacement → streamed marker → response-message persistence → useLastCompaction on later continuation. Owner: code triggers/selects the eligible span; compaction model proposes summary; code accepts returned text without semantic approval. Distinct suboperation from the supplied ordinary [RT-RTE-web-chat](runtime.md#rt-rte-web-chat), using [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model).

- Immediate return: summary/usage or undefined on failure; current step receives assistant summary plus preserved system/current-user tail.
- Later read-back: latest nonempty stored marker reconstructs an assistant summary plus messages starting at the user turn before that marker. Nonstreaming generate has no stream writer to persist this marker through that mechanism, although in-process replacement still occurs.
- Delegated visibility: compaction model sees image-stripped prefix messages selected backward under its own context-window budget, minus 16000 output tokens and prompt overhead; assistant/tool pairs are kept together. Foreground receives only summary, not summarizer processing.
- Selection predicate: estimated message+tool+reserved-output tokens exceed 75% of main context window; summarize from first non-system message up to but excluding last user; choose most recent fitting prefix messages for the summarizer.
- Invalidation or expiry: latest valid marker supersedes older model-visible prefixes; empty/error marker skipped. Raw stored history is not physically deleted by these functions. No automatic reload of the omitted prefix into the model is established.
- Activation or effect: summary changes current/continued model input; preservation of important findings or successful context fit afterward is unobserved.
- Evidence limits: an old part of the replaced span can be dropped before summarization when the summarizer budget is smaller. The requested continuity is not complete coverage or reversible compression; provider behavior and SDK persistence semantics not executed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `apps/backend/src/services/compaction.ts`, `apps/backend/src/agents/compaction/compaction-llm.ts`, `apps/backend/src/utils/ai.ts`, `apps/backend/src/services/agent.ts`. Trigger/proposed change/admission: automatic budget crossing proposes a summary; software replaces the span on model return. Failure reports an empty error marker and continues. No independent oracle, semantic veto or rollback restoring model-visible history after successful compaction is established. Mode: context maintenance. The prompt requests analytical findings, goals, results, decisions and recent outcomes, but does not require retaining every reason.

> const textOnlyMessages = stripImageParts(messages);
> const selectedMessages = selectMessagesInBudget(textOnlyMessages, budget, this._tc);
> --- `apps/backend/src/agents/compaction/compaction-llm.ts`

#### MEM-RTE-saved-files
Label: Saved file read-back

Endpoints/progression: upload or model write/byte producer → scoped storage → later named-path read → readable conversion → model tool result. Owner: user chooses uploaded material; model chooses generated text and tool reads; code scopes/checks physical I/O. Distinct from memory extraction and from [RT-CLM-context-readonly](runtime.md#rt-clm-context-readonly), which describes a write boundary rather than this durable content route. Ordinary write does not modify project rules. SRC-1: `apps/backend/src/services/storage/user-files.ts`, `apps/backend/src/agents/tools/read.ts`, `apps/backend/src/agents/tools/write.ts`, `apps/backend/src/services/agent.ts`.

- Immediate return: write returns path/size; upload returns stored object; read returns converted content and total-line count before display rendering.
- Later read-back: model can call read on retained storage path; stored-document attachment bytes remain out of initial window, replaced by a description instructing explicit read.
- Delegated visibility: reader receives converted display content, not arbitrary storage bytes; byte-oriented APIs separately afford nonconversation consumers. Their existence alone does not establish an additional deployed consumer route.
- Selection predicate: foreground model or caller names file_path under scoped storage; read dispatch distinguishes story, storage and project paths. This is requested path access, not semantic relevance ranking.
- Invalidation or expiry: model text write can overwrite a named output; uploads choose unused names. Complete UI deletion, provider lifecycle/TTL and cleanup semantics uninspected.
- Activation or effect: scoped content persistence and model-readable delivery implemented; later reliance and analytical improvement unobserved.
- Evidence limits: storage provider reliability, binary conversion fidelity and final display truncation not audited; scope/size/type checks do not establish truth of retained contents.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Human upload admits chosen bytes; model write admits authored text automatically after path/size checks. Byte/from-disk APIs allow other producers, whose full admission controls are uninspected. No universal human review or semantic oracle is established. Mode: work-product authoring/retrieval. Recovery/withdrawal remains local to overwrite or uninspected delete facilities, not automatic quality rejection.

> if (isStoragePath(part.url)) {
> return [{ type: 'text' as const, text: describeStoredAttachment(part) }];
> }
> --- `apps/backend/src/services/agent.ts`

### Claims

#### MEM-CLM-memory-replacement
Label: Memory replacement deletion claim

Claimed operation: extraction instructions say a superseded memory will be deleted/replaced. Implementation instead inserts a successor and marks the predecessor's supersededBy. That withdraws it from active reads without physically deleting it. This is distinct from the supplied read-only claim. SRC-1: `apps/backend/src/components/ai/memory-system-prompt.tsx`, `apps/backend/src/queries/memory.ts`.

> When <Code>supersedes_id</Code> is set, the old memory will be deleted and replaced by the new one. Use this
> when:
> --- `apps/backend/src/components/ai/memory-system-prompt.tsx`

> .set({ supersededBy: newMemoryId })
> --- `apps/backend/src/queries/memory.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-user-memory
Label: User memory to analytics model

Part of: [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance)

Consumer: selected foreground analytics model under default prompt construction. Channel: MemoryBlock in system instructions. Force: natural-language facts/directives, framed as previously established but defeasible under new user messages; this is not an executable permission grant or guaranteed compliance. Horizon: persisted user rows can cross chats/projects; injection is reconstructed per invocation and gated by user/project enablement. Own-current-chat rows are excluded. Category priority gives rules before facts; query ordering makes newer rows earlier within categories; estimated content tokens are capped at 1000, skipping oversized items and continuing. IDs/provenance and reasons do not reach this consumer. A complete override bypasses default memory composition, as the parent record establishes. SRC-1: `apps/backend/src/components/ai/system-prompt.tsx`, `apps/backend/src/types/memory.ts`, `apps/backend/src/queries/memory.ts`, `apps/backend/src/services/agent.ts`.

> if (totalTokens + memoryTokens > limit) {
> continue;
> }
> --- `apps/backend/src/components/ai/system-prompt.tsx`

## Annotations

#### On [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation)

Retained inputs: usage/feedback summaries, current context files, existing recommendations and dismissed fingerprints. Full prior recommendation rationale is stored, but the initial later prompt only renders status/fingerprint/file/subject/title. Code reconciliation reloads occurrenceCount/status for update decisions; dismissed fingerprints are a separate selector input, not model-visible instruction text by that mechanism. A recorded finding updates an existing fingerprint even below the new-insert impact floor; duplicate recordings in a pass collapse with last winning. Existing applied findings can reopen. A resolve action itself also writes applied status, so the parent's PR-opening interpretation is not the only producer of that label. SRC-1: `apps/backend/src/services/context-recommendations.reconcile.ts`, `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/queries/context-recommendation.queries.ts`, `apps/backend/src/components/ai/context-recommendations-prompt.tsx`.

> if (dismissed.has(fingerprint)) {
> continue;
> }
> --- `apps/backend/src/services/context-recommendations.reconcile.ts`

> { status: 'applied', statusChangedAt: new Date() },
> --- `apps/backend/src/services/context-recommendations.service.ts`

Trace-fed result: persisted diagnosis/proposed edits in [MEM-OBJ-context-recommendation](#mem-obj-context-recommendation). Later update consumer is the recommendation model/code; ordinary analytics receives admitted project files, not a recommendation solely because it is stored. Initial human governance of remote source content remains unresolved; software reconciliation and optional auto-PR creation are not per-content human approval. The diagnostic prompt requests re-reading target files before resolving and evidence-grounded root causes. These are requested curation behaviors, not observed corrections. Initial selection uses default incremental period after last completed run, or 90-day fallback/explicit period; 40-step budget limits investigation. SRC-1: `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/components/ai/context-recommendations-prompt.tsx`.

#### On [RT-RTE-explore-task](runtime.md#rt-rte-explore-task)

Working-context control is an isolated model frame with explicit selected task input and report-only return. The parent can retain that report as a tool result; internal child messages are not equivalent to this retained report. It resembles a stack frame, not a separate permission principal: ToolContext is shared. The runtime supplies the quoted runner and toModelOutput evidence. No child transcript replay or automatic pointer-following of omitted context is established by those inspected paths.

## Write side

The trace-fed extraction write uses recent user/assistant text, not tool payloads, images or the current response's verified outcome. Its prompt says to analyze the full conversation, but its implementation supplies only a recent, truncated text sample. Permanence filtering and duplication decisions are delegated to a model; code enforces schema, normalization and existing-ID membership. The stored result changes future available guidance without retaining the reasons for selecting it. This supports an automatic trace-fed memory update mechanism, not demonstrated improvement. [MEM-RTE-memory-extraction](#mem-rte-memory-extraction).

Withdrawal differs by mechanism. Supersession soft-excludes an old row; explicit deletion removes a row; disabling suspends use; chat deletion can null lineage without removing derived memory. Existing manager strings are not proved to hot-refresh after maintenance. Replacement deletion does not automatically unsupersede its predecessor. These local policies prevent equating revocation, deletion and rollback. [MEM-OBJ-memories](#mem-obj-memories), [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance).

Compaction derives a summary from prepared trace material. The qualifying chain is raw persisted history → portability/story/mention transformations → prefix extraction → image stripping/budget suffix selection → summary → subsequent steps and streamed checkpoint replay. Streaming and nonstreaming generate are different checkpoint forms: generate can summarize current process state without the stream-writer persistence channel. Summaries may retain decisions and outcomes, but neither the prompt nor inspected schema ensures reason preservation. [MEM-RTE-chat-compaction](#mem-rte-chat-compaction), [RT-RTE-test-answer](runtime.md#rt-rte-test-answer).

Recommendations retain more explicit reasons and evidence pointers. The model proposes; deterministic fingerprint/dismissal/score logic decides DB admission. Manual dismissal supplies a later software veto by fingerprint; the specific status-mutation UI policy remains uninspected. Reference repair drops unresolvable pointers, which can reduce downstream impact scores. Prior full reasons are not automatically in the next prompt. Optional PR creation changes a proposal repository, not live context; independent delivery mechanisms admit the bytes later. No answer-quality gate is established by the score or Git guards. [MEM-OBJ-context-recommendation](#mem-obj-context-recommendation), annotation on [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

Files admit chosen uploads, model-authored outputs and external byte producers. Story replay incorporates user-edited current versions; the ordinary write tool cannot write project context. CLI sync, deployment and Git refresh can replace that context independently. Operator initiation chooses a workflow/source but does not prove human approval of every generated/transferred file. Full provider, story-app-state and cleanup admission policies remain unresolved in the coverage table. [MEM-RTE-saved-files](#mem-rte-saved-files), [RT-CLM-context-readonly](runtime.md#rt-clm-context-readonly), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

## Read-back

Memory injection is automatic supply triggered by default prompt construction, not a foreground semantic search request. Inputs to selection are current user/project enablement, excluded current chat, active status, category priority, creation order and content-token budget. Selected category/content reaches system instructions; lineage does not. Project-scoped enablement cannot be read as project-scoped memory storage. [MEM-BAP-user-memory](#mem-bap-user-memory).

Conversation reconstruction is request-driven by chat identity, then automatically narrowed by the latest successful marker. Step pruning removes old reasoning and suggest_follow_ups calls; story synchronization replaces old bodies with latest DB versions and earlier duplicates with stubs; provider portability and superseded SQL marking alter tool display. These control what reaches the consumer, not necessarily what is retained. No general automatic reload of all pruned material is shown. [MEM-RTE-chat-compaction](#mem-rte-chat-compaction), [RT-RTE-web-chat](runtime.md#rt-rte-web-chat). SRC-1: `apps/backend/src/services/agent.ts`.

Files use explicit model/caller reads. Storage APIs alone are capabilities; the read tool and attachment path instructions establish the concrete model-facing route. Readable display can differ from payload; complete truncation/conversion limits remain uninspected. Skills can be expanded on mention with the supplied 16000-character bound; detailed load_skill selection is not established here. Table/citation expansion and inline image versus deferred document delivery are separate working-context controls. [MEM-RTE-saved-files](#mem-rte-saved-files), [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance).

Explore isolates most investigative context and returns one report into parent history. This matches stack-frame input/return visibility but not permission isolation. Compaction resembles lossy eviction with a retained checkpoint. The analogy stops at explicit reload: path strings and summary references are not counted/reachable pointers automatically dereferenced by the model. [RT-RTE-explore-task](runtime.md#rt-rte-explore-task), [MEM-RTE-chat-compaction](#mem-rte-chat-compaction).

Recommendations supply compact prior-finding summaries to future diagnostic runs and complete stored rows to deterministic reconciliation. Their full rationales are retained without an established automatic later rationale reader in the initial prompt. Project context then reaches later analytics only after a distinct live-delivery route. Evaluation reports, recurring automation output and direct MCP tool results do not acquire future guidance authority merely by existing. [MEM-OBJ-context-recommendation](#mem-obj-context-recommendation), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-automation-run](runtime.md#rt-rte-automation-run), [RT-RTE-test-answer](runtime.md#rt-rte-test-answer).

## Integration issues

- **Correction to applied-status interpretation:** [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation) associates applied with PR opening. That producer exists, but applyActions also uses applied for model-resolved findings. Retain both producers; status alone proves neither PR creation nor deployed correction. SRC-1: `apps/backend/src/services/context-recommendations.service.ts`; annotation and [MEM-OBJ-context-recommendation](#mem-obj-context-recommendation) retain the evidence.
- **Additional qualification of compaction coverage:** the supplied working-context account names the whole old prefix, but the summarizer selects a token-budget suffix after stripping images. The replaced range can exceed the content actually seen by the summarizer. Do not infer preservation of all old information. [MEM-RTE-chat-compaction](#mem-rte-chat-compaction), [MEM-OBJ-compaction](#mem-obj-compaction); SRC-1: `apps/backend/src/agents/compaction/compaction-llm.ts`, `apps/backend/src/utils/ai.ts`.
- **Source-native deletion claim corrected:** [MEM-CLM-memory-replacement](#mem-clm-memory-replacement) distinguishes prompt wording from soft supersession. No supplied runtime statement requires replacement deletion, but later analyses must not inherit that misleading prompt label.
- **Identity review:** no new declaration intentionally duplicates a supplied referent. The checkpoint and recommendation objects are parts of supplied routes; the memory authority path is a part of supplied guidance. New extraction/compaction/file routes are narrower transformations rather than replacement candidates for enclosing chat or delivery routes. Extractor and foreground/compaction calls remain distinct roles even when provider IDs coincide.
- **Unresolved included alternatives:** fork producers/copied checkpoints; full dynamic skill loading; channel-specific memory/history; story publication/app-state/blob cleanup; upload and saved-file deletion/lifecycle; provider-specific CLI/API context admission; feedback fallback and full app-DB filtering. The coverage table identifies source roots and prevented conclusions. Known subsequent extraction, summary, file and recommendation transformations remain supported despite these missing facts; none establishes complete enumeration of memory consumers.
- **Unresolved semantic/deployed facts:** model extraction quality, supersession race behavior, binary conversion fidelity, Git review governance, provider fixity, successful live change consumption and beneficial outcomes lack run evidence. Relevant records: [MEM-RTE-memory-extraction](#mem-rte-memory-extraction), [MEM-RTE-chat-compaction](#mem-rte-chat-compaction), [MEM-RTE-saved-files](#mem-rte-saved-files), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). These limits do not erase implemented update routes.

## Limitations and checks

The frozen checkout HEAD was rechecked as `0085625a8fd22e4f404b6a3971d153f6b6699479`, matching boundary and source identity. Supplied invocation, types, worker rules and complete record contract were read, including bounded continuation reads. Added paths are all in SRC-1; no prior analysis or other worker state was used. Directly inspected source and supplied runtime evidence are separated in the coverage table. Some exploratory searches used nonexistent filename guesses and returned errors; they supplied no absence evidence, and relevant actual paths were then located/read.

Counterexamples checked include complete system overrides bypassing memory; project-independent memory querying despite project gates; prompt deletion wording versus soft supersession; budget-selection omission before summary; generate without streaming checkpoint persistence; applied status without PR creation; and latest edited story content replacing historical outputs. These narrow positive mechanisms rather than asserting universal guarantees.

No exercised learning, model compliance, answer-quality improvement, provider-state updates or causal self-improvement is established. The source supports retained-content transformations and later delivery, not their benefit. Missing paths remain inspection limits rather than bounded absences. Deterministic validation: the supplied validate-output command passed with “Member content check passes; invocation residue not checked.” This checks form and quotation occurrence, not job acceptance or semantic claim support.
