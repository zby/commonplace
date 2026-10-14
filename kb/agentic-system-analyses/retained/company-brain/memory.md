---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Company Brain's hosted document and derived-memory lifecycle, scoped recall, learned style, instruction admission and retained investigation context."
run-id: AAS-2026-10-14-company-brain-30a9e8cfaeca-01
source-identity: "https://github.com/supermemoryai/company-brain"
reviewed-boundary: ef8a45ef3aed97b32599c7d8007edefab6d14e9a
---

# Company Brain memory report

## Boundary and evidence

The subject is the shipped Company Brain worker at `ef8a45ef3aed97b32599c7d8007edefab6d14e9a`, with the whole-system scope and external-service limits fixed by [boundary](boundary.md#boundary-and-evidence). All new findings cite SRC-1, implementation unless explicitly identified as doctrine/design. HEAD was rechecked against that revision. Sources were read, not executed; there is no observed run or experiment.

The memory scope includes interactive and approval-resume capture; passive public-channel knowledge curation; delayed public-thread style observation; hosted documents, derived memories and extraction configuration; local tags, node mappings and generation guards; ambient, semantic, tag and tree recall; principal-scoped investigation checkpoints; standing prompts and skills; signup/domain research, entity caching, schedules and research draft history; and the shipped human-facing graph/recent/export readers. Remote extraction, bucket assignment, embeddings, ranking, versioning and deletion internals remain opaque. Tool-result and approval compaction are included as working-context control and later-invocation memory, not conflated with company knowledge. Ordinary untransformed live turn accumulation and external app state are not independent company-memory stores. Sandbox reuse is only the scoped capability already described by [RT-RTE-sandbox-work](runtime.md#rt-rte-sandbox-work); provider filesystem lifetime is uninspected.

The table distinguishes direct source inspection (D) from supplied runtime findings (R). An available but uninspected leaf does not establish an absence. Coverage is at the material-operation level, not an exhaustive audit of every file or permission gate.

| Entry point / operation | Source paths and inspection | Covering records or bounded uncertainty |
|---|---|---|
| Main and fast inference used by memory routes | R: model roles; D: fast-model call sites in memory/observer files | [RT-CMP-brain-main](runtime.md#rt-cmp-brain-main), [RT-CMP-triage-model](runtime.md#rt-cmp-triage-model); no additional weight store inferred |
| `save_memory`, completed Slack and resumed writeback | D: `src/brain/turn/capture-tools.ts`, `src/brain/slack/turn.ts`, `src/brain/memory/index.ts`, `src/brain/memory/writeback.ts` | [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), [MEM-OBJ-brain-document](#mem-obj-brain-document); resumed caller inspected directly, initial eligibility also supplied by R |
| Public-channel observer and retry batch | D: bounded ranges of `src/brain/slack/channel-observe.ts`, including system prompt, SQL tables, spool and complete processing/run functions | [MEM-OBJ-channel-batch](#mem-obj-channel-batch), [MEM-RTE-channel-curation](#mem-rte-channel-curation); detailed legacy scheduler repair not fully read, so no exhaustive recovery guarantee |
| Public-thread persona observer | D: complete `src/brain/turn/interaction-observe.ts`, `src/brain/memory/interaction-style.ts`; R: delayed arming | [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), [MEM-OBJ-agent-style](#mem-obj-agent-style), [MEM-RTE-style-recall](#mem-rte-style-recall) |
| Hosted admission, derivation, list hydration and service search | D: `src/compat/routes/memories/handler-effect.ts`, `src/memory/client.ts`, `src/memory/memories.ts`, `src/compat/routes/v4/search/handlers.ts` | [MEM-OBJ-brain-document](#mem-obj-brain-document), [MEM-OBJ-derived-memory](#mem-obj-derived-memory), [MEM-CLM-service-curation](#mem-clm-service-curation); embeddings and internal lineage inaccessible |
| Extraction policy and bucket provisioning | D: complete `src/brain/memory/profile-config.ts`, `src/brain/memory/profile-sync.ts` | [MEM-OBJ-profile-config](#mem-obj-profile-config), [MEM-RTE-profile-provision](#mem-rte-profile-provision); initial remote configuration and successful classification unobserved |
| Scoped semantic, tag and ambient reads | D: complete `src/brain/memory/{read-scope,search-brain,profile-recall}.ts`, bounded selector/fetch functions in `src/brain/memory/tags.ts`, `src/brain/turn/context-tools.ts`, context assembly in `src/brain/turn/compute.ts` | [MEM-RTE-ambient-recall](#mem-rte-ambient-recall), [MEM-RTE-requested-recall](#mem-rte-requested-recall); private membership freshness supplied by runtime/boundary, membership leaf not fully inspected |
| Tree mapping, hydration, splitting | D: `src/brain/memory/split.ts`, bounded mapping/repoint/hydration functions in `src/brain/memory/tree.ts` | [MEM-OBJ-memory-index](#mem-obj-memory-index), [MEM-RTE-node-splitting](#mem-rte-node-splitting); outline rendering and all normalization branches not exhaustively inspected |
| Preview/apply forget; stale document cleanup; registry reset | D: complete `src/brain/tools/forget-memories.ts`, `src/compat/routes/v4/memories/forget-matching.ts`, `src/brain/memory/cleanup.ts`; reset function in `src/brain/turn/agent.impl.ts`; D search for reset callers throughout `src/` and `web/` | [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal); source search found exposed reset method/delegation, not a deployed HTTP/UI caller or remote wipe; prevents a whole-memory-reset claim |
| Alternative debug writer | D: complete `debugTurn` in `src/brain/turn/agent.impl.ts` | [MEM-RTE-debug-capture](#mem-rte-debug-capture); principal identity is supplied by caller, human per-content approval unresolved |
| Investigation checkpoint and approval compaction | D: complete `src/brain/turn/thread-investigation.ts`, restore/save call sites in `src/brain/turn/compute.ts`; R: `src/brain/turn/context.ts` compaction | [MEM-OBJ-thread-investigation](#mem-obj-thread-investigation), [MEM-RTE-investigation-recall](#mem-rte-investigation-recall), [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary), [RT-RTE-approval-resume](runtime.md#rt-rte-approval-resume); compacted bodies not reconstructed |
| Skills and standing workspace instructions | R: `src/brain/skills/{store,tools,slack-interactions}.ts`, `src/routes/workspace-prompt.ts`; D: complete `src/brain/configuration.ts`, prompt ordering in `src/brain/prompt/build.ts` | [RT-OBJ-brain-skill](runtime.md#rt-obj-brain-skill), [RT-OBJ-workspace-prompt](runtime.md#rt-obj-workspace-prompt), [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission), [MEM-RTE-config-edit](#mem-rte-config-edit); HTTP versus tool paths remain distinct |
| Signup/domain research, entity caching | D: research memory-admission and stale-aspect functions in `src/brain/turn/research.ts`, domain trigger in `src/brain/configuration.ts`; R: `src/brain/memory/entities.ts` | [RT-RTE-entity-web](runtime.md#rt-rte-entity-web), [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), [MEM-OBJ-brain-document](#mem-obj-brain-document); full web summarization pipeline not read, prevents accuracy/complete acquisition claims |
| Scheduled and independent research consumers, draft history | R: schedule admission and draft storage/send; D: `src/brain/auto-research/plan.ts` context assembly, searches in `src/brain/auto-research/draft.ts` | [RT-RTE-scheduled-task](runtime.md#rt-rte-scheduled-task), [RT-RTE-research-draft](runtime.md#rt-rte-research-draft); complete history selection/storage leaves not read, prevents completeness and exact retention-horizon claims |
| Recent memories, export and graph display | D: complete `src/routes/memories.ts`, `src/routes/graph.ts`; UI is supplied boundary inventory, not browser inspection | [MEM-RTE-human-readers](#mem-rte-human-readers); no editor/deletion behavior inferred from a graph label |
| Reply-quality and research-draft flags | D: bounded searches in `src/brain/observability/reply-quality.ts`, `src/brain/auto-research/draft.ts`; R: stored draft flags | Evaluation concerns malformed reply text and missing tool evidence, not proven memory truth or an inspected automatic rewrite consumer. Full evaluators are available but uninspected; no claim that evaluative feedback trains or revises memory. |
| CLI, hooks and dispatch | R: `package.json`, `src/worker.ts`, `src/routes/index.ts`; D: tool registration and exported service methods above | HTTP, Slack, model tools, alarms and DO/library methods are the established surfaces. No CLI/hook absence is asserted from this bounded inventory; deployment/admin parity remains unestablished. |

## Core ideas

1. **A submitted document is not the later memory.** Slack turns produce compact subject documents; channel observation produces curated clusters. A compatibility adapter submits them to Supermemory. Ambient and tree reads normally consume live derived memories, while node splitting reads original document text. These consumers therefore do not necessarily see the same content or provenance. [MEM-OBJ-brain-document](#mem-obj-brain-document), [MEM-OBJ-derived-memory](#mem-obj-derived-memory).
2. **Recall has several selectors, not one semantic search.** Automatic profile supply uses recent bucketed people/channel memories plus tagged non-person baseline and a topic map. Requested search ranks across accessible containers. Tag recall matches lexical tag metadata, then packs text to an estimated budget. Tree navigation follows document mappings, hydrates derived memories and pages by timestamp. None is a whole-brain guarantee. [MEM-RTE-ambient-recall](#mem-rte-ambient-recall), [MEM-RTE-requested-recall](#mem-rte-requested-recall).
3. **Learned style, knowledge and standing instructions differ in authority.** Style notes have a dedicated observer and self container; prompt text requests that they shape voice but not override policy. Workspace prompts outrank style and memories in the authored prompt hierarchy. Skill bodies are separately admitted and loaded. These are model-interpreted text, not executable access policy or demonstrated compliance. [MEM-OBJ-agent-style](#mem-obj-agent-style), [RT-BAP-standing-instructions](runtime.md#rt-bap-standing-instructions).
4. **Local indexes and generation guards are not the remote store.** Tags and document-to-node mappings live in DO SQL. Reset advances a generation and clears local observation/index/research state; stale writes request document deletion. Forget marks individual derived memories through the remote API. Remote document content, later extraction and tenant isolation require service contracts not implemented by these local labels. [MEM-RTE-node-splitting](#mem-rte-node-splitting), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal).
5. **Continuations retain lossy experience as well as facts.** Approval compaction preserves bounded messages; investigation checkpoints preserve selected methods, one answer-derived evidence string, last answer and bounded tool trajectories for a later matching principal/thread. A successful tool call is not proof that the answer called `verifiedEvidence` is verified. [MEM-RTE-investigation-recall](#mem-rte-investigation-recall), [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-brain-document
Label: Submitted brain document

Source-native identity: `MemoryDocInput` transformed to the document submitted by `addMemorySingle`. Form: natural-language content and source references; symbolic title/date/custom ID/container/tag metadata route admission and retrieval. Substrate: hosted Supermemory documents; temporary capture objects remain in the worker. Lineage includes user conversation, model/tool-derived interactive synthesis, curated HUMAN channel material and web research summaries. It is not necessarily raw evidence. Hosted extraction, embeddings and later memory provenance are uninspected. Distinct from [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state); closest supplied route is [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), not a document declaration.

`buildSlackMemoryWriteRequest` supplies `DOCUMENT_DATE`, optional event date, sources and normalized tags, writes to one scope container, and hashes content/title/tags/date with an optional generation suffix. Content-empty, unresolved DM scope and agent-backed empty-tag proposals can be rejected. `writeMemory` checks generation before and after service admission, accepts `queued` or `done`, then registers local tags and node mappings. These statuses establish accepted submission, not completed extraction. SRC-1, `src/brain/memory/writeback.ts`, `src/brain/memory/index.ts`.

> return result.status === "queued" || result.status === "done"
> --- `src/brain/memory/index.ts`

The executable adapter forwards content, custom ID, containers, task type and flattened scalar metadata. It does not forward its accepted `dreaming`, `preserveBrainTags` or `isFullReplace` options. Thus callers naming instant extraction or replacement do not establish that service behavior. SRC-1, `src/compat/routes/memories/handler-effect.ts`.

> flat[key] = Array.isArray(value) ? value.join(",") : value
> --- `src/compat/routes/memories/handler-effect.ts`

The document schema requests rationale and owners to remain together, but this does not prove retention of reasons through hosted extraction. SRC-1, `src/brain/memory/writeback.ts`.

#### MEM-OBJ-derived-memory
Label: Hosted derived memory

Source-native identity: `BrainMemory` / `DerivedMemory` returned by `/v4/memories/list` and documents-by-IDs. Form: natural-language `memory` text; separate symbolic IDs, tags, buckets, source-document IDs, source counts, timestamps and liveness flags. Substrate: remote service, materialized as worker objects. Embedding representation and derivation algorithm are opaque provider parts, not locally observed numerical components. Lineage is attributed by returned `documentIds`; the application cannot reconstruct why the provider extracted or superseded a claim. Distinct from the submitted document and [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state); [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff) supplies the closest consumer route.

List readers page at 100, deduplicate IDs, reject nonlatest/forgotten/expired entries, sort by update time and enforce an overall limit. Bucket hydration looks up source documents and maps derived memory IDs to bucket arrays. Missing buckets can therefore exclude a person's otherwise retrievable fact from ambient injection. Node readers hydrate derived content rather than original document bodies; semantic search also permits chunks. SRC-1, `src/memory/memories.ts`, `src/brain/memory/tree.ts`, `src/brain/memory/search-brain.ts`.

> if (entry.isLatest === false || entry.isForgotten) return false
> return !entry.forgetAfter || new Date(entry.forgetAfter).getTime() > now
> --- `src/memory/memories.ts`

Authority at update/read consumers differs: returned text guides later models and humans; metadata controls filtering and navigation. Corroboration counts and similarity scores are selector inputs, not locally checked warrant.

#### MEM-OBJ-channel-batch
Label: Public channel spool and curated batch

Source-native identity: `brain_channel_observe_pending` and `PersistedChannelBatch` in `brain_channel_observe_batch`. Form: raw Slack message text with symbolic timestamps/author labels, then model-authored natural-language clusters plus tag metadata; no local embedding. Substrate: organization DO SQL. Lineage: channel history → bot-labeled spool → bounded humanized prompt → fast-model clusters → hosted documents → derived memories. The raw spool and clusters have different roles; pending raw rows are deleted after batch acceptance, whereas accepted documents can affect later turns. SQL cursor/schedule/retry/scan rows are access/progress metadata, not durable company claims. Distinct from [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state) and the interactive/style route [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff). SRC-1, `src/brain/slack/channel-observe.ts`.

> clusters_json TEXT NOT NULL,
> created_at INTEGER NOT NULL,
> --- `src/brain/slack/channel-observe.ts`

#### MEM-OBJ-agent-style
Label: Agent-self style memory and carried observer state

Source-native identity: agent-self documents with `source_type: company-brain-self-observe`, their derived bucketed memories, and `brain_observe_cursor.carried_state`. Form: natural-language generalized persona notes and prior-note tail; symbolic cursor/custom IDs and bucket-to-facet mapping. Substrate: hosted documents/memories, with cursor and carried state in DO SQL. The note derives from bounded labeled public-thread messages, including bots as context; the observer is instructed to use HUMAN preference evidence only. Kept carried state is the last eight lines bounded to 1,200 characters and is later supplied to the observer, not the main agent as a raw cursor value. Main-agent style comes through derived bucketed memories instead. This object elaborates, but does not duplicate, [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff); no corresponding supplied object. SRC-1, `src/brain/turn/interaction-observe.ts`, `src/brain/memory/interaction-style.ts`.

> Speaker labels are evidence boundaries. Each message body is a JSON string. Learn only from HUMAN lines.
> --- `src/brain/turn/interaction-observe.ts`

This instruction is doctrine/design embedded in an implemented inference request, not proof of model compliance. The route skips DMs and channels not positively public, checks workspace ownership/generation, rejects empty/non-note outputs, and only advances carried notes after `queued`/`done`. It retains generalized guidance, not an explicit criticism/evidence/rationale ledger. Hosted source documents may remain, but the later style renderer supplies note text, not reasons or human message quotations.

#### MEM-OBJ-memory-index
Label: Brain tags and document-node mappings

Source-native identity: `brain_memory_tag`, `brain_memory_node`, `brain_memory_state.reset_epoch`. Form: symbolic container/key/document/path relations, counters, descriptions and reset generation; natural-language descriptions inform models through tag/tree navigation. Substrate: DO SQL, distinct from hosted derived memory tags. Lineage: accepted writes register tags and map documents; model partitioning can change mappings and augment derived-memory metadata. Consumers: tag canonicalization, lexical tag selection, outline navigation, subtree hydration and generation fences. Distinct from [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state); closest supplied memory route is [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff). SRC-1, `src/brain/memory/index.ts`, `src/brain/memory/tags.ts`, `src/brain/memory/tree.ts`.

Descriptions and counts are not claim contents. A stale or incomplete mapping can change tree reachability without removing the semantic-search capability. The tag list ranks by use count/update time and deduplicates across selected scopes; it is a bounded navigation inventory, not complete knowledge.

#### MEM-OBJ-profile-config
Label: Container extraction context and buckets

Source-native identity: `entityContext`, `profileBuckets`, and container name supplied by `upsertBrainSpaceConfig`. Form: natural-language extraction guidance with symbolic bucket keys, container targets and local sync timestamps. Substrate: remote container-tag settings; shipped policy text in source, throttle in DO SQL. Lineage: fixed policy plus org name/domain/about, asker name or channel name. Unknown initial hosted settings do not suppress the known subsequent provisioning. The remote extractor is the intended update consumer; downstream models consume extracted bucketed notes, not this config directly. No counterpart among supplied components/objects; this is distinct from [RT-OBJ-workspace-prompt](runtime.md#rt-obj-workspace-prompt), which targets main-agent context. SRC-1, `src/brain/memory/profile-sync.ts`, `src/brain/memory/profile-config.ts`.

The write helper accepts but ignores `visibility`; a configuration label such as private/unlisted does not establish remote access enforcement.

> no equivalent, so `visibility` is accepted and ignored.
> --- `src/brain/memory/profile-sync.ts`

#### MEM-OBJ-thread-investigation
Label: Retained thread investigation checkpoint
Part of: [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state)

This record isolates the reusable `TurnState.checkpoint` part from live coordination state. Source-native identity: `ReusableInvestigation` serialized in `brain_thread_investigation`. Form: natural-language goal, last answer and answer-derived evidence; bounded literal tool inputs/outputs and method names with symbolic digests/status/times/schema version. Substrate: DO SQL JSON keyed by thread and principal. It is not the whole approval conversation or a dereferenceable raw-result archive. SRC-1, `src/brain/turn/thread-investigation.ts`, `src/brain/turn/state.ts`.

The local field called `verifiedEvidence` receives a bounded answer whenever any current native call succeeded. The success flag does not check every answer claim. One evidence string, up to six deduplicated recent trajectory entries, methods and a last answer survive; each string has separate bounds and the total checkpoint is limited to 160,000 characters. Original omitted content is not recoverable from digests.

> verifiedEvidence:
> answer && hasSuccessfulEvidence
> ? [compactText(answer, MAX_EVIDENCE_CHARS)]
> : [...(args.state.checkpoint?.verifiedEvidence ?? [])].slice(-1),
> --- `src/brain/turn/thread-investigation.ts`

### Routes

#### MEM-RTE-channel-curation
Label: Public channel curation and admission

Endpoints/progression: armed public-channel callback → Slack history spool → oldest pending bounded batch → humanized/tagged fast-model distillation → persisted cluster batch → `writeMemories` → hosted admission → cursor advance and spool/batch deletion. Owner: scheduling/ownership code chooses eligible scope and batch; fast model proposes content; software admits schema-valid tagged current-generation submissions. Humans author input messages but do not approve each retained cluster. Guidance asks durable HUMAN changes, coherent subjects, preserved dates/rationale and no bot-derived facts. Operating mode: continuous observation, not an experiment; no expected-answer oracle. SRC-1, `src/brain/slack/channel-observe.ts`, `src/brain/memory/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: callback completes, continues, retries or becomes stale; no user answer.
- Later read-back: hosted derived cluster memories reach ambient, semantic, tag and tree consumers; persisted cluster batches also resume failed writes without redistillation.
- Delegated visibility: fast model receives up to 60 pending messages packed to 8,000 characters plus roster/guidance; hosted service receives cluster documents and metadata, not necessarily the whole raw spool.
- Selection predicate: positively public channel, current org/schedule/generation; oldest pending messages; model-selected durable subjects; person IDs restricted to batch authors/mentions.
- Invalidation or expiry: stale ownership/generation rejects work; nonpublic/rebound scope terminates; failed admission retries the persisted batch and does not advance the processed cursor.
- Activation or effect: durable derived knowledge can enter later model context; changed behavior and benefit unobserved.
- Evidence limits: HUMAN-only and no-chatter constraints are inference instructions, not verified provenance filters on output; remote dedup/supersession are opaque; retry ownership is not an end-to-end exactly-once proof.

> if (out.written !== out.total) return "retry"
> --- `src/brain/slack/channel-observe.ts`

The raw-to-derived chain retains content dates and optional source fields but not a mandatory explanation of selection. Successful submission deletes local raw/pending batch rows; later recall may carry even less provenance. Rejection/repair is software/schema/service failure handling, not a truth evaluation. No complete rollback of a partly submitted batch is implemented here.

#### MEM-RTE-ambient-recall
Label: Automatic ambient profile supply

Endpoints/progression: `computeTurn` → derive readable containers → list live hosted rows and buckets → person/channel/static selection → deduplication and compact rendering plus tree outline → runtime-context message → model. Owner: deterministic code, not foreground tool choice. This is independently supplied context on invocation; query-based retrieval is a separate route. SRC-1, `src/brain/memory/profile-recall.ts`, `src/brain/turn/compute.ts`, `src/brain/memory/read-scope.ts`. Distinct read selector within the broad [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), not a duplicate of that admission route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ambient text or null on unavailable/empty/error context.
- Later read-back: prior derived knowledge is automatically delivered to later model invocations; no new content write occurs.
- Delegated visibility: model receives selected text shortened to 300 characters per memory and a labels-only topic outline, not all source documents or retrieval metadata.
- Selection predicate: accessible containers; at most eight deduplicated people; asker candidates 250, mentioned-person candidates 25; channel candidates 250; static candidates 500, filtered to tagged non-person material; person/channel rows require nonempty buckets.
- Invalidation or expiry: hosted-list liveness filtering excludes nonlatest/forgotten/expired entries; scope changes alter containers; errors return null; bucket lookup failures do not establish absence of facts.
- Activation or effect: supplies knowledge/preferences/channel disposition as model context; no proof the model follows or benefits from them.
- Evidence limits: ambient candidate caps and 300-character rendering prevent complete profiles; no final token budget appears in this renderer; remote bucket/corroboration meanings unverified.

> const AMBIENT_MENTIONED_CANDIDATE_LIMIT = 25
> --- `src/brain/memory/profile-recall.ts`

The source comment saying profiles are injected with “no caps” describes the last rendering stage, not acquisition. Recent retrieval already capped rows before bucket filtering. A strong completeness inference is false even before per-memory truncation. This is a bounded automatic supply route, not a single total-memory retrieval operation.

#### MEM-RTE-requested-recall
Label: Requested semantic tag and tree recall

Endpoints/progression: model selects a memory tool → container resolution → operation-specific selection → result rendering → model tool-result context. Owner: foreground model chooses query/focus/tag subject/path/page; deterministic code enforces local limits; hosted search controls ranking. SRC-1, `src/brain/turn/context-tools.ts`, `src/brain/memory/search-brain.ts`, `src/brain/memory/profile-recall.ts`, `src/brain/memory/tags.ts`, `src/brain/memory/tree.ts`. Distinct selectors complement [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff); same broad consumer, not a competing memory-write identity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: semantic results, compact tagged context, labels/tree, or 250-memory node page with possible `nextCursor`.
- Later read-back: retained hosted facts/chunks are pulled into later invocations; a read alone does not admit or revise knowledge, though tree reconciliation may prune mappings.
- Delegated visibility: semantic query/container/filter reaches service; tag/tree readers deliver selected memory text, not full documents or mandatory source reasons.
- Selection predicate: semantic hybrid search uses query and optional OR brain-tag filter, 40 results per container, score dedup/global top 40, concurrency six; tag recall uses lexical key/label/description matching plus resolved people, ten keys, 500 candidates, normalized-text dedup and estimated 20,000-token packing; tree recall uses document-node descendants and derived-memory timestamp range.
- Invalidation or expiry: list/node hydration applies live-memory checks; tree reconciliation removes mappings missing a nonfailed document status; semantic request excludes forgotten memories but service compliance is external; explicit container override replaces derived scope, including empty override.
- Activation or effect: retrieved text becomes model evidence/context; labels and similarity do not prove truth or answer completeness.
- Evidence limits: remote ranking/embedding internals unavailable; tag selector is lexical, not semantic; timestamp-only strict-before pagination can omit other entries tied at the boundary time, so full enumeration is not guaranteed; missing document-status responses can prune live mappings.

> .sort((a, b) => b.similarity - a.similarity)
> .slice(0, 40)
> --- `src/brain/memory/search-brain.ts`

> if (range?.before && memory.updatedAt >= range.before) return false
> --- `src/brain/memory/tree.ts`

Read scope differs from write scope. Shared reads include shared; a private channel adds its own container; a DM adds personal and all private-channel tags returned by membership state. Foreground semantic and tag recall can reach facts excluded from bucketed ambient profiles. `read_current_thread` separately reloads omitted Slack history in bounded batches and applies query/page selection; it is source retrieval/working-context control, not evidence that omitted content was already retained in the brain. SRC-1, `src/brain/memory/read-scope.ts`, `src/brain/turn/context-tools.ts`.

#### MEM-RTE-style-recall
Label: Agent style recall and context authority

Endpoints/progression: current invocation → list agent-self memories with buckets → asker-specific then non-person rows → bucket-to-facet rendering → `<interaction_style>` runtime context. Owner: deterministic selector, remotely assigned buckets, later model interpretation. SRC-1, `src/brain/memory/interaction-style.ts`, `src/brain/turn/compute.ts`, `src/brain/prompt/build.ts`. Read part of the broader [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), not a new observer identity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: facet profile/string or null; no write.
- Later read-back: previously extracted style guidance automatically reaches later turns; observer separately reads its carried prior-note tail.
- Delegated visibility: model sees selected note text grouped into voice/social/culture/operating/avoid/self, not original human reaction evidence.
- Selection predicate: latest live 80 candidate memories from agent-self; include matching asker tags and non-person rows; only recognized bucket keys enter facets.
- Invalidation or expiry: hosted liveness filters and forget affect visible rows; unknown buckets are ignored; clearing observer carry prevents that local tail from regenerating notes after reset, but does not itself delete remote notes.
- Activation or effect: prompt requests voice/register adjustment with lower authority than workspace prompt/system policy; reliable adjustment is unobserved.
- Evidence limits: no aggregate rendered token cap inspected; generalized notes need not preserve reasons; remote bucket assignment and instruction-following cannot be proved from the call.

> These are stored memories, not fixed rules: when a teammate says one of them is wrong, forget it with forget_memories instead of only agreeing.
> --- `src/brain/prompt/build.ts`

#### MEM-RTE-profile-provision
Label: Extraction profile provisioning

Endpoints/progression: scope sync request → 24-hour SQL throttle → compose entity context/buckets → update remote container settings → mark synced. Owner: application code proposes/adopts generated config, no per-config content approval. Human-supplied org/name/domain fields may shape it but are not approval of each assembled policy. Trigger: profile synchronization for shared, self, asker or private channel. Proposed change: extraction guidance/bucket configuration, not model weights. Guidance is [MEM-OBJ-profile-config](#mem-obj-profile-config); service errors reject marking synced and permit later retry. Operating mode: maintenance; no answer oracle. SRC-1, `src/brain/memory/profile-sync.ts`, `src/brain/memory/profile-config.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: best-effort completion; exceptions captured per scope.
- Later read-back: remote extraction is intended to use settings on future documents; locally known derived bucket consumers are ambient/style readers.
- Delegated visibility: remote settings receive source-authored instructions plus org/person/channel context, not current whole conversation.
- Selection predicate: scope-specific throttle; preserve user-renamed names; shared/self/personal/private-channel bucket and context builders.
- Invalidation or expiry: 24-hour refresh throttle; reset clears throttle; subsequent config replaces current values; historical rollback uninspected.
- Activation or effect: changes remote extraction inputs; actual changed memory meanings/buckets and later behavior unobserved.
- Evidence limits: remote classification/decay/supersession behavior remains claimed; `visibility`, owner and org parameters do not become locally enforced remote access controls in this helper.

> const SYNC_INTERVAL_MS = 24 * 60 * 60 * 1000
> --- `src/brain/memory/profile-sync.ts`

#### MEM-RTE-node-splitting
Label: Topic node partition and repoint

Endpoints/progression: accepted write triggers split check → reconcile document mappings → hydrate original document text → sample → fast-model child proposal → validate/reject unusable assignments → derived metadata updates → local mapping moves → register child tags. Owner: code threshold/sampling/guards, fast model partitions, software adopts; no per-partition human gate. Trigger: node reaches 125 live document members; sample capped at 160. Proposed change: retrieval organization, not factual text revision. Prompt requests two to four coherent subthemes, leaves broad documents at parent, rejects catch-all `other`; no expected-answer oracle. Operating mode: automatic maintenance. SRC-1, `src/brain/memory/split.ts`, `src/brain/memory/tree.ts`, `src/memory/memories.ts`. No corresponding supplied route; related object is [MEM-OBJ-memory-index](#mem-obj-memory-index), closest supplied scope is [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: best-effort background completion or caught failure.
- Later read-back: changed DO mapping determines future tree reads; added child tags can influence later tag/semantic filters, subject to metadata representation.
- Delegated visibility: fast model sees original document texts and their indexes; remote metadata patch receives same derived-memory text plus added tags; main agent later receives derived memory text via recall.
- Selection predicate: at least 125 mappings/live documents, newest hydrated sample up to 160, model-selected child indexes; invalid indexes ignored and overlapping source-document assignments use later-child-wins.
- Invalidation or expiry: generation fences; process-local per-node in-flight guard; remote metadata updates precede DO moves; failures skip local move and allow later retry, not transactional rollback of all prior remote patches.
- Activation or effect: changes navigation/retrieval placement; content equality in metadata patch means this is organizational curation, not demonstrated factual correction.
- Evidence limits: patches may be partial; repoint only handles array-valued derived tags while admission flattens arrays to comma strings; provider response normalization is uninspected, preventing unconditional tag/tree consistency.

> // tag-scoped reads look. Their documents keep the original tags.
> --- `src/brain/memory/tree.ts`

The substantive source code adds a child tag, not replacement of the parent. Original document metadata stays unchanged; hosted derived-memory metadata and DO mappings are different parts. Provider memory patch semantics are requested through same-text `newContent`, not independently verified versioning. Split rationale is only child description; no per-assignment criticism/evidence account or later rationale reader is established.

#### MEM-RTE-memory-withdrawal
Label: Scoped forgetting and local invalidation

Endpoints/progression: interactive model preview query → semantic candidates from conversation write container plus agent-self → IDs/sample → requester approval for apply → forget-by-ID per container; independently stale-generation/aspect cleanup deletes a document, and exposed `resetMemoryRegistry` advances generation/clears local state. These operations are grouped as withdrawal but have different admission, retained results and consumers. Owner: model proposes query/IDs, code validates resolved scope/nonempty apply IDs, requester can veto SDK-gated apply; stale cleanup/reset are software operations whose external caller admission is not established here. Operating mode: user corrections/maintenance, no expected-answer oracle. SRC-1, `src/brain/tools/forget-memories.ts`, `src/compat/routes/v4/memories/forget-matching.ts`, `src/brain/memory/cleanup.ts`, `src/brain/turn/agent.impl.ts`. Closest supplied controls are [RT-RTE-approval-resume](runtime.md#rt-rte-approval-resume) and generation-aware [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff); no supplied withdrawal referent.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: preview count/eight samples/IDs; apply fulfilled count and random batch ID, errors or partial results; reset helper returns after local clearing/cancel attempts.
- Later read-back: list/derived node readers filter forgotten/nonlatest/expired entries; semantic search requests exclusion; document delete is intended to remove its derivations; reset-generation checks stop stale local producers.
- Delegated visibility: preview query and container reach hosted search; apply sends supplied IDs/container/reason; no locally retained audited preview object was inspected.
- Selection predicate: resolved conversation write scope plus agent-self, not every readable container; preview threshold default 0.5/cap 100 (up to 500); apply requires IDs but maps explicit IDs directly, without proving they came from that preview or reapplying the cap.
- Invalidation or expiry: remote forget flag/semantics govern derived entries; source-document deletion is separate; reset clears local tags/nodes/observer carry/research state and cancels schedules best effort, not all remote documents, skills, prompts or investigation SQL.
- Activation or effect: can withdraw retained derived context or navigation, but successful remote deletion, prevention of re-extraction from surviving documents and deployed reset activation are unobserved.
- Evidence limits: actual preview membership is model/approval-protocol guidance, not a locally validated provenance relation; remote ID/container authorization and cascade are external contracts; partial failures do not guarantee atomic forget or rollback.

> needsApproval: ({ dryRun }) => dryRun === false,
> --- `src/brain/tools/forget-memories.ts`

> const candidates: ForgetCandidate[] = explicit
> ? explicit.map((id) => ({ id, memory: "", score: 1 }))
> : await searchCandidates()
> --- `src/compat/routes/v4/memories/forget-matching.ts`

The wrapper comment mentions container-scoped SQL, but the current adapter sends `client.memories.forget` requests instead. A preview IDs list is not persisted/checked by the adapter; fulfilled service calls count as forgotten. Do not infer a locally enforced “exact prior preview” guarantee from the description. Main prompt's forget-then-save correction is doctrine/design, not an atomic revise operation. SRC-1, `src/brain/prompt/system.ts`, `src/compat/routes/v4/memories/forget-matching.ts`.

Reset is an exposed method whose inspected implementation clears local state, not an inspected remote wipe:

> clearInteractionObserveState(agent)
> clearBrainProfileSync(agent)
> clearBrainMemoryRegistry(agent)
> --- `src/brain/turn/agent.impl.ts`

#### MEM-RTE-investigation-recall
Label: Investigation checkpoint save and recall

Endpoints/progression: nonpassive nonephemeral completed compute turn with connected-app work → deterministic checkpoint construction → SQL save → later matching thread/principal invocation → parse/expiry checks → restored turn state. Owner: host code derives bounded state from model answer and native-call trajectory; no per-checkpoint human approval. Guidance is persistence schema/bounds, not content-directed critique. Operating mode: open task continuity; successful native call is a selector flag, not an answer oracle. Related live container: [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state); distinct from whole-message [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary). SRC-1, `src/brain/turn/thread-investigation.ts`, `src/brain/turn/compute.ts`, `src/brain/turn/state.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: checkpoint or undefined; serialization bound failure caught by caller.
- Later read-back: subsequent nonephemeral compute restores matching checkpoint to turn state, retaining prior answer/method/evidence/trajectory context.
- Delegated visibility: selected bounded state is reachable by later turn assembly; not every raw tool output or omitted original; full final state-rendering visibility is uninspected in this member.
- Selection predicate: connected-app work, successful current call for new answer-as-evidence, recent deduplicated trajectories; thread key plus principal tuple including user, personal/shared-only and read-only flags.
- Invalidation or expiry: six-hour idle TTL renewed on save; expiry/schema/parse failures delete or omit checkpoint; ephemeral runs do not load/save, passive turns do not save new checkpoints.
- Activation or effect: restores retained experience to later decision state; answer correctness, effective reuse and benefit unobserved.
- Evidence limits: `verifiedEvidence` is a label over answer text plus a success predicate, not verified claim provenance; bounded literals/digests are lossy and cannot reload originals; complete rendering/consumption downstream is not proven by SQL storage alone.

> export const INVESTIGATION_IDLE_TTL_MS = 6 * 60 * 60 * 1000
> --- `src/brain/turn/thread-investigation.ts`

Raw trajectory excerpts and derived answer summaries are separately retained. This capacity is automatic trace-fed update/read-back, but improved future capacity is not demonstrated. No theory-builder classification is assigned merely because a prior answer is kept.

#### MEM-RTE-debug-capture
Label: Debug-turn alternative memory writer

Endpoints/progression: exported `debugTurn` input → load org → compute without Slack lookup → completed memory output → shared `writeMemories` when explicit `input.userId` exists. Owner: caller supplies text/identity, model authors memory, software checks nonempty memory and explicit user ID. Human per-content approval is unresolved from a generic API principal; no extra approval is implemented in this function. Operating mode: open API task, no answer oracle; ordinary capture guidance applies through compute. Closest supplied route is [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), but this caller lacks Slack scope/current-thread delivery control. SRC-1, `src/brain/turn/agent.impl.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reply, memory and boolean written; suspended action returns approval-needed text and no memory write.
- Later read-back: accepted shared document can enter later ambient/search/tag/tree consumers.
- Delegated visibility: compute input reaches model, accepted document reaches hosted service.
- Selection predicate: loaded organization, explicit user ID and nonempty memory; undefined memory scope defaults shared write container; current generation read by writer.
- Invalidation or expiry: generation fences/service failures can reject; no independent Slack revision fence here; hosted liveness affects later derived reads.
- Activation or effect: alternate durable knowledge admission, without proving API exposure/authentication or successful deployment.
- Evidence limits: exported method is positive shipped wiring, not proof a human invoked it or authorized every document; no deployment caller or exhaustive API permission assessment.

> if (memoryDocsFromWriteback(memory).length && input.userId) {
> --- `src/brain/turn/agent.impl.ts`

#### MEM-RTE-config-edit
Label: Model-mediated standing configuration edit

Endpoints/progression: `update_configuration` tool → field schema validation → actor admin check → workspace prompt replacement/null or symbolic settings/domain update → later context/model/research. Owner: foreground model proposes supplied text/value; software role/schema admits; admin request is guidance, but this path has no separate per-proposed-text approval card. Trigger: requested configuration change; operating mode open editing, no answer oracle. Rejection: invalid input/nonadmin/unavailable org/domain; recovery includes replacement/null overrides, not a historical rollback store. Same prompt referent as [RT-OBJ-workspace-prompt](runtime.md#rt-obj-workspace-prompt); distinct admission surface supplementing [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission), not a second prompt object. SRC-1, `src/brain/configuration.ts`, `src/brain/turn/tools.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: updated field/detail or rejection reason.
- Later read-back: stored prompt enters future turns; symbolic settings resolve model/proactivity; changed domain can start research whose summaries become shared documents.
- Delegated visibility: proposed configuration enters tool host; later selected prompt reaches model; domain reaches research.
- Selection predicate: exposed unless `allowWrites` false; `actor.isAdmin` checked at execution; workspace text length/schema enforced.
- Invalidation or expiry: replacement/null removes overrides; current same-domain queued/running/done research can avoid rerun; no historical prompt version recovery established.
- Activation or effect: changes later guidance/settings and may initiate research; reliable following or improved behavior unobserved.
- Evidence limits: admin actor check is local policy, not proof requested content was human-authored or separately approved; HTTP/Slack admission guarantees cannot be copied unchanged to this surface.

> if (!ctx.actor.isAdmin) {
> return { updated: false, reason: ADMIN_ONLY_REASON }
> }
> --- `src/brain/configuration.ts`

#### MEM-RTE-human-readers
Label: Recent export and graph memory readers

Endpoints/progression: authenticated org/user HTTP request → shared plus viewer-personal containers → hosted list or documents-with-memories → JSON/Markdown/browser consumer. Owner: deterministic routes/service; human chooses page/export. Distinct consumer from [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff); no supplied human-read route. SRC-1, `src/routes/memories.ts`, `src/routes/graph.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: total count and newest eight; export up to 2,000 live rows per shared/personal container; graph page default 200/max 500.
- Later read-back: retained memory is delivered to a human in later requests; exporting does not establish a further model consumer or re-ingest path.
- Delegated visibility: graph removes document `content` and filters memory entries to the two allowed containers; list/export provide text; browser receives no teammate-private container selected by these handlers.
- Selection predicate: current authenticated user/org; fixed shared plus own personal surface, narrower than a Slack DM's private-channel read set.
- Invalidation or expiry: list/export use live filters; graph endpoint forwards service entries with container filtering but no local latest/forgotten/expiry predicate; count is raw service total, not guaranteed equal to visible live rows.
- Activation or effect: display/download affords human inspection; no verified editing, deletion or adoption follows from graph display.
- Evidence limits: route implementation does not establish browser use, truth, service authorization or cross-tenant isolation; source documents and summaries may expose different detail than compact model reads.

> documents: response.documents.map(({ content: _content, ...doc }) => ({
> --- `src/routes/graph.ts`

### Claims

#### MEM-CLM-service-curation
Label: Hosted extraction supersession and decay claims

Claimed operation: source prompts request one current answer per subject, supersession, inferred repeated patterns, transient forget horizons and profile bucketing. Source: SRC-1, `src/brain/memory/profile-config.ts`, `src/brain/slack/channel-observe.ts`. The adapter delegates extraction/chunking/embedding to the service; remote internals and runs are unavailable. The application does enforce derived-list liveness filtering, but it cannot establish how decay horizons, duplicate merging or updates were assigned. Closest supplied claim-bearing route: [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), not a declaration of those service mechanisms.

> When new information supersedes an old fact (moved from X to Y, no longer, now), update the existing memory rather than creating a parallel one.
> --- `src/brain/memory/profile-config.ts`

- claim conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

Implementation wiring concerns submitting guidance and filtering returned liveness fields, not remote semantic curation. Requested behavior is not reliable model/service compliance or measured benefit. In particular, public distillation says HUMAN-stated facts while shared extraction config permits inference from patterns; provenance and criteria differ across stages and must not be mapped to one universal evidence rule.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-context
Label: Retained knowledge and style influence later models

Consumer: later main-agent turn; research planning also receives company/profile context and past draft/sent snippets. Channel: automatic runtime-context text, requested memory tool results, and research-plan prompt. Force: natural-language knowledge/guidance interpreted by model, not access authorization, validated truth or demonstrated compliance. Horizon: problems/sessions while retained and selected; investigation continuity is separately limited by thread/principal/TTL. Source: SRC-1, `src/brain/turn/compute.ts`, `src/brain/prompt/build.ts`, `src/brain/turn/context-tools.ts`, `src/brain/auto-research/plan.ts`. Distinct from instruction-specific [RT-BAP-standing-instructions](runtime.md#rt-bap-standing-instructions) and executable [RT-BAP-tool-policy](runtime.md#rt-bap-tool-policy).

> Do not repeat anything in the already-sent or already-drafted lists, even reworded or under a different label.
> --- `src/brain/auto-research/plan.ts`

Research planning normalizes and cuts each past body to 240 characters, so retained output history guides novelty rather than preserving full source evidence. It calls `buildBrainProfileContext` with only org ID: no query or person keys are supplied, so that call can return a topic outline without retrieving a full corpus of facts. Treating the method name as whole-company recall would overstate what reaches this consumer. SRC-1, `src/brain/auto-research/plan.ts`, `src/brain/memory/profile-recall.ts`, `src/brain/memory/tags.ts`.

## Annotations

#### On [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff)

Memory-specific lineage is mixed: main capture is model-authored synthesis of conversation/tool observations, not HUMAN-only raw logging; channel and style observers have their own bounded producer routes. `save_memory` captures a proposal in the live turn rather than doing hosted I/O itself. The schema requests one coherent compact subject, sources and dates, max three documents per turn; once-only timing and durable/nonvolatile restrictions are instructions, not semantic validation. Downstream retained documents/derived text are [MEM-OBJ-brain-document](#mem-obj-brain-document) and [MEM-OBJ-derived-memory](#mem-obj-derived-memory). SRC-1, `src/brain/turn/capture-tools.ts`, `src/brain/memory/writeback.ts`, `src/brain/memory/index.ts`.

> capture.memory = memory
> --- `src/brain/turn/capture-tools.ts`

The style update consumer receives prior carried notes and fresh bounded labeled messages; its later main-agent consumer receives bucketed derived notes, not this carried state or full human evidence. See [MEM-OBJ-agent-style](#mem-obj-agent-style), [MEM-RTE-style-recall](#mem-rte-style-recall). Reset-generation cleanup requests external deletion; accepted `queued`/`done` is submission success, not extracted correctness or completed curation.

#### On [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary)

Retained compacted messages are by-value natural-language excerpts plus symbolic stubs/digests and serialized structures in approval storage. Supplied evidence establishes deterministic preferential removal of old state, skill bodies and older tool output, with newer output/discovery retained. The digest is neither a pointer nor enough to reconstruct the omitted tool result. Skill stubs can trigger `load_skill`, which reloads current SQL/source skill content, not a pinned omitted version. These are later-resume consumers and working-context controls; they are not the hosted knowledge extractor. Evidence/limits supplied by the cited runtime record; no duplicate compaction declaration.

#### On [RT-OBJ-brain-skill](runtime.md#rt-obj-brain-skill)

Natural-language body is the behavior-shaping part; symbolic scope/status/version controls who can list/load it. Human-approved Slack creation differs from automatic observer memory capture. Usage counters are selector/maintenance metadata, not retained reasons. A later model sees the visible index, then loaded body; compaction can replace that body with a reload stub. The supplied store/admission evidence establishes update/delete/disable, not historical version rollback or retention of the originating conversation. [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission), [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary).

#### On [RT-OBJ-workspace-prompt](runtime.md#rt-obj-workspace-prompt)

At the actual prompt consumer, standing text is described as above learned style/memories and below fixed policy, authorization, tool rules and explicit current request. It is escaped for markup but remains natural-language model input, not executable policy. Current prompt replacement/null can change later input; the additional model-mediated admin writer is [MEM-RTE-config-edit](#mem-rte-config-edit). SRC-1, `src/brain/prompt/build.ts`, `src/brain/configuration.ts`.

> Treat it as high-priority workspace context: follow it over learned <interaction_style>, memories, entity or tag context, and situational defaults when they conflict.
> --- `src/brain/prompt/build.ts`

#### On [RT-RTE-entity-web](runtime.md#rt-rte-entity-web)

Cached canonical entity/aliases/domain is model-derived knowledge, not a retained rationale for identification. The supplied record establishes later current-generation lookup and read-only persistence suppression; external search truth remains unverified. Distinguish this specialized optional cache from ordinary `MemoryDocSchema` guidance excluding bare identity stubs. Its existence is a countercase to interpreting the main document guidance as a universal entity-cache prohibition.

#### On [RT-RTE-scheduled-task](runtime.md#rt-rte-scheduled-task)

Payload instruction is retained natural-language task guidance; timing/creator/scope/destination/read-only flags are symbolic scheduling/access state. Automatic callback delivery is different from requested memory retrieval: the callback pushes a later task execution, which can itself load normal context/tool memory under its actor. Creator update/cancel changes future use; no rationale/evaluation history is established by payload persistence. Supplied runtime source/status fields bound this finding. Do not infer memory writeback merely because `save_memory` is assembled: durable hosted admission still needs a caller write route.

#### On [RT-RTE-research-draft](runtime.md#rt-rte-research-draft)

Retained draft/sent text is later planning input as well as human-review output. The directly inspected planner cuts normalized past bodies to 240 characters each and prompts against repeating them. This is trace-derived output reuse, not a tested improvement signal or answer oracle. Draft turns isolate full transcripts; only selected draft text/trace/flags cross to local review/send. Complete persistence/history-selection horizon remains uninspected. SRC-1, `src/brain/auto-research/plan.ts`; isolation/storage supplied by cited runtime record.

## Write side

**Admission is route-specific.** Main `save_memory` is a model proposal captured in the current run; current completed Slack callers perform physical I/O without per-document human approval. The resumed Slack writer checks completed/current status and uses carried memory scope/person IDs. Public-channel distillation is separately automatic with persisted retry clusters. Public-thread style notes are automatically admitted after non-note/ownership/generation checks, not approved by the people whose reactions are evidence. Domain research begins from setup/admin domain input, but each web-summary document is model/software admitted. `debugTurn` is another caller, not the coordinated Slack path. Human-authored messages or starting research do not equal per-content approval. See [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), [MEM-RTE-channel-curation](#mem-rte-channel-curation), [MEM-RTE-debug-capture](#mem-rte-debug-capture), SRC-1 `src/brain/slack/turn.ts`, `src/brain/turn/research.ts`.

**Transformations retain different things.** Interactive synthesis requests self-contained knowledge with rationale/sources. Channel curation persists subject clusters before calling the hosted extractor; after accepted submission it deletes the local raw spool/batch. Style observation retains short generalized notes and a bounded prior-note tail, then remote extraction buckets later style. The service may further extract, merge, version, decay or embed, but only requests and returned fields are inspectable. Splitting reads document content, proposes organization, adds derived child tags and moves local mappings; it does not establish changed factual meaning. Checkpoint construction deterministically retains selected raw tool excerpts plus answer-derived summary, unlike both hosted extraction and whole-message compaction. [MEM-RTE-node-splitting](#mem-rte-node-splitting), [MEM-RTE-investigation-recall](#mem-rte-investigation-recall), [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary).

**Rejected/withdrawn material has bounded downstream exclusion.** Invalid/empty/stale documents are not admitted locally; service failures return false/retry. A stale accepted write requests document deletion. A changed research domain retires an old aspect document when no replacement was written, using exact aspect custom ID, not fuzzy tag deletion. Forget applies to derived-memory IDs in conversation write scope plus self; the wider read set can contain memories this tool cannot correct from that surface. Local list/node readers check liveness, but deleting derived knowledge and deleting original documents are different operations. Reset clears local observation/index/research state and cancels schedules, not an inspected full remote wipe. [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), SRC-1 `src/brain/turn/research.ts`, `src/brain/memory/cleanup.ts`.

**Material editing differs from learning proposals.** Slack skills have requester approval/scope and stored active body; HTTP standing text is human-supplied under admin gates. The additional `update_configuration` path can persist model-supplied prompt text under admin actor validation without a separate proposed-text approval card. Model choices are symbolic settings, not parameter updates. These positive text-admission mechanisms do not establish content-directed criticism, learning benefit or exercised self-improvement. [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission), [MEM-RTE-config-edit](#mem-rte-config-edit).

The automatic style and knowledge chains are trace-fed updates with later context consumers. They establish retained behavior-shaping capacity, not causal improvement. Reasons are requested in document guidance, but not guaranteed through derivation/rendering. No claim of a theory builder or exercised self-improvement is made from persistence, a reflection function name, or a score alone.

## Read-back

The consumer receives the result **after** selection/transformation: compact ambient text, grouped style notes, ranked semantic text/chunks, budgeted lexical-tag context, paged live subtree memories, skill bodies/current reloads, standing workspace instructions, or bounded checkpoint state. Service extraction can change what later readers see relative to submitted documents. Tag/tree metadata supplies targeting and navigation, not evidence of correctness. The read routes and budgets are [MEM-RTE-ambient-recall](#mem-rte-ambient-recall), [MEM-RTE-requested-recall](#mem-rte-requested-recall), [MEM-RTE-style-recall](#mem-rte-style-recall), [MEM-RTE-investigation-recall](#mem-rte-investigation-recall), and runtime instruction/compaction records.

Independent supply occurs when compute loads ambient/style/standing context, when a scheduled callback starts a turn, and when later research planning consumes stored draft/sent snippets. Requested pull occurs through memory tools, skill load and omitted-thread reload. Export/graph are wired later human consumers, not hypothetical callers of a storage API. Profile-config update targets remote extraction; it is not main-agent push until derived results pass later selectors. An exported reset method establishes an invalidation capability, not a deployed remote reset route.

Working-context control has three different re-entry forms: skill body stubs can load a current body; omitted Slack history can be fetched in bounded source batches; investigation state and approval resumes replay bounded retained values, not original omitted tool data. Independent ephemeral research drafts keep their full transcripts out of the parent and return selected products/trace flags. The stack-frame analogy fits that last isolation/return boundary, but none of the by-value text/digests is a general heap pointer that can recover an evicted original. [RT-RTE-research-draft](runtime.md#rt-rte-research-draft), [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary), SRC-1 `src/brain/turn/context-tools.ts`, `src/brain/turn/thread-investigation.ts`.

## Integration issues

1. **Additional material admission paths.** The runtime explicitly leaves detailed configuration surfaces open. [MEM-RTE-config-edit](#mem-rte-config-edit) supplements [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission): `update_configuration` is model-mediated with admin execution validation, not necessarily human-authored HTTP text or a separate skill-like approval. [MEM-RTE-debug-capture](#mem-rte-debug-capture) adds a shipped shared writer distinct from coordinated Slack eligibility. These are extensions, not duplicate prompt/document objects. SRC-1, `src/brain/configuration.ts`, `src/brain/turn/agent.impl.ts`.
2. **No unconditional instant/replacement guarantee.** [MEM-OBJ-brain-document](#mem-obj-brain-document) narrows any inference from `dreaming: instant`, `preserveBrainTags` or replacement labels: the compatibility adapter accepts but does not forward those controls. `queued`/`done` establishes submission success only. This bounds [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), not its correctly scoped claim that writes are locally wired. SRC-1, `src/compat/routes/memories/handler-effect.ts`.
3. **Partial overlap, not duplicate identity.** Automatic/query/style selectors and channel admission elaborate different endpoints around [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff). Their storage objects have no supplied object counterpart. [MEM-OBJ-thread-investigation](#mem-obj-thread-investigation) is explicitly part of [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state); its route differs from approval message compaction. No new declaration is intended to replace a supplied whole record.
4. **Tenant and visibility contract unresolved.** The direct memory client is keyed only by `SUPERMEMORY_API_KEY`; several service helpers accept `orgId` without forwarding it as a tenant selector, and the provisioning helper ignores visibility. Container scoping is locally implemented, but no end-to-end multi-organization isolation guarantee follows without deployment key/service contracts. This is a qualification, not evidence of leakage. [MEM-OBJ-profile-config](#mem-obj-profile-config), [MEM-RTE-requested-recall](#mem-rte-requested-recall), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal); SRC-1, `src/memory/client.ts`, `src/compat/routes/v4/search/handlers.ts`, `src/compat/routes/v4/memories/forget-matching.ts`.
5. **Withdrawal and reset are not complete memory erasure.** The apply adapter does not validate actual prior preview membership; forget is limited to write scope plus self, and derived forget differs from document removal. Remote cascade/re-extraction behavior is unavailable. The exposed reset clears local producer/index/research state, while no remote wipe caller was found in the bounded source search; prompts, skills and investigation state are not cleared by its inspected body. This prevents extending runtime stale-generation cleanup into whole-memory erasure. [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal), [RT-RTE-approval-resume](runtime.md#rt-rte-approval-resume), [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff).
6. **Metadata consistency and retrieval completeness unresolved.** Admission flattens arrays, list readers parse comma strings, but split repoint requires arrays in derived metadata. Remote normalization is unknown. Reconciliation can drop mappings when document status calls fail; tree paging is strict-before timestamp without a tie-breaking ID; ambient candidate/text caps contradict an unqualified complete-profile reading of the renderer comment. These limit tag/tree consistency and full enumeration, not existence of recall. [MEM-RTE-node-splitting](#mem-rte-node-splitting), [MEM-RTE-requested-recall](#mem-rte-requested-recall), [MEM-RTE-ambient-recall](#mem-rte-ambient-recall).
7. **Labels and source-trust stages differ.** `verifiedEvidence` is answer text selected by any successful native call, not verified evidence; style observer requires direct HUMAN preferences while extraction self-config describes broader operating guidance; shared extraction permits inferred patterns while channel distillation asks HUMAN-stated facts. The actual remote reconciliation/provenance is opaque. [MEM-OBJ-thread-investigation](#mem-obj-thread-investigation), [MEM-CLM-service-curation](#mem-clm-service-curation), [MEM-OBJ-agent-style](#mem-obj-agent-style). This prevents universal HUMAN-only or fact-verified memory classifications.
8. **Bounded available-but-uninspected consumers.** Full checkpoint rendering, draft-history storage/selection, private-membership freshness, all evaluator outputs and detailed UI editors remain available but not fully inspected. They prevent claims of exhaustive consumption/permission equivalence, exact history horizon or evaluative feedback-driven revision. Established planner context/history snippet consumption and API human readers remain positive findings. [MEM-RTE-investigation-recall](#mem-rte-investigation-recall), [RT-RTE-research-draft](runtime.md#rt-rte-research-draft), [MEM-RTE-human-readers](#mem-rte-human-readers), [MEM-BAP-retained-context](#mem-bap-retained-context).

## Limitations and checks

Frozen source identity and HEAD were checked against boundary's repository and full revision. Supplied invocation, job, member/peer types, collection, worker rules and records contract were read completely; bounded runtime reads were recovered through their final range. Source additions are recorded above under SRC-1 implementation or embedded doctrine/design. No extra source, target execution, provider call, prior analysis, delegation, stage or commit was used.

The report distinguishes submission, delivery, activation and benefit. Hosted extraction/ranking/decay/authorization internals and all actual operation remain uninspected; no reliable provenance, privacy, truth, learning benefit or exercised self-improvement conclusion follows. Several local selectors and guards have source-supported countercases retained rather than erased to make labels look consistent. Static prompts/policies are instructions/config inputs, not by themselves learned memory.

Validation: the required invocation-specific `commonplace-run validate-output` check passed after correcting status-field syntax and restoring the exact source comment quotation. Its pass establishes deterministic form, quotation occurrence and invocation constraints, not semantic acceptance or exercised behavior.
