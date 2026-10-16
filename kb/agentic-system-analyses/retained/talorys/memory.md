---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Talorys memory lifecycle, lossy conversation summaries and optional hybrid recall over owner-retained information"
run-id: AAS-2026-10-15-talorys-7bce41ba9401-01
source-identity: https://github.com/rociiu/talorys
reviewed-boundary: c5da440010402ed4c1b9789ae22eab96a8f0f379
---

# Talorys memory report

## Boundary and evidence

This member examines the retained-state loop of Talorys at the commit in [boundary](boundary.md). It includes explicit personal memories, lifecycle links and conflict reviews, conversation text and generated summaries, semantic indexes of memories/tasks/notes/automations, their owner and model write surfaces, and the selection paths delivering retained text to later chat or scheduled invocations. Pending approvals and stored routine prompts remain the runtime's records, with memory-specific annotations below. Source evidence is SRC-1 at the frozen commit: executable TypeScript/JavaScript is implementation; shipped prompts and comments are declared policy; the checked-in evaluation is reported operation. There is no supplied target execution or causal experiment.

Direct inspection extended the supplied runtime account through the memory repository, lifecycle, conflict rules and Clef response handling; semantic indexing, storage, item text construction, neighbors, selectors, tools and HTTP maintenance routes; backup merge; conversation repository and HTTP reads; runner/prompt call sites; and the MemoryPage conflict buttons. The registered source is unchanged. The source checkout HEAD was rechecked as `c5da440010402ed4c1b9789ae22eab96a8f0f379`. No source was modified or target code executed.

### Coverage inventory

Rows marked direct describe source reads, not just acceptance of a runtime finding. The rows group operations with common admission/consumption boundaries; they do not claim exhaustive testing.

| Entry point or operation | Source paths, relative to SRC-1 | Coverage and retained consequence |
| --- | --- | --- |
| Tool and API dispatch | `apps/agent/src/tools/index.ts`, `apps/agent/src/api/app.ts`, `apps/agent/src/agent/talorys-agent.ts` | Direct: registry, semantic middleware mounting, memory/Clef/neighbor hooks and runner extension wiring. [MEM-RTE-memory-write](#mem-rte-memory-write), [MEM-RTE-index-maintenance](#mem-rte-index-maintenance). Installer CLI is a provisioning path, not another memory-inference dispatch; supplied [RT-RTE-product-update](runtime.md#rt-rte-product-update) covers it. |
| `remember`, `update_memory`, owner create/edit/correct/status and review resolution | `apps/agent/src/tools/memories.ts`, `apps/agent/src/api/routes/data.ts`, `apps/agent/src/memory/service.ts`, `apps/agent/src/memory/lifecycle.ts`, `apps/agent/src/memory/conflict.ts`, `apps/web/src/pages/MemoryPage.tsx` | Direct: immediate persistence, distinct author/approver roles, optional automatic retirement, reason retention, restore and deletion. [MEM-OBJ-tal-memories](#mem-obj-tal-memories), [MEM-OBJ-memory-reviews](#mem-obj-memory-reviews), [MEM-RTE-memory-write](#mem-rte-memory-write). |
| Keyword prompt recall, memory search tool and general search | `apps/agent/src/agent/memory.ts`, `apps/agent/src/tools/memories.ts`, `apps/agent/src/tools/search.ts`, `apps/agent/src/db/repositories/memories.ts` | Direct: automatic push differs from model-requested search; general keyword search has no lifecycle filter. [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-requested-search](#mem-rte-requested-search). |
| Hybrid recall, recency augmentation and memory neighbor lookup | `apps/agent/src/semantic/recall.ts`, `apps/agent/src/semantic/neighbors.ts`, `apps/agent/src/semantic/index.ts`, `apps/agent/src/memory/service.ts` | Direct: numerical selection, history-intent branch, prompt formatting/budget, stricter neighbor hash check than recall. [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-memory-write](#mem-rte-memory-write). |
| Item recall and alternate search surfaces | `apps/agent/src/semantic/itemRecall.ts`, `apps/agent/src/semantic/itemSearch.ts`, `apps/agent/src/semantic/tools.ts`, `apps/agent/src/semantic/routes.ts`, `apps/agent/src/tools/notes.ts` | Direct: query and turn vectors, item live filters, excerpt selection and bounded note reload; debug search is not prompt recall. [MEM-RTE-item-recall](#mem-rte-item-recall), [MEM-RTE-requested-search](#mem-rte-requested-search). |
| Index production, stale/partial indexes, reindex and opt-out | `apps/agent/src/semantic/indexer.ts`, `apps/agent/src/semantic/itemIndex.ts`, `apps/agent/src/semantic/itemText.ts`, `apps/agent/src/semantic/vectorStore.ts`, `apps/agent/src/semantic/itemStore.ts`, `apps/agent/src/semantic/embeddings.ts`, `apps/agent/src/semantic/routes.ts` | Direct: derived numerical payload versus symbolic lineage metadata, lazy/background repair, separate caps and data removal. [MEM-OBJ-semantic-vectors](#mem-obj-semantic-vectors), [MEM-OBJ-item-vectors](#mem-obj-item-vectors), [MEM-RTE-index-maintenance](#mem-rte-index-maintenance). Remote embedding parameters/provenance remain opaque; [RT-CMP-workers-embedder](runtime.md#rt-cmp-workers-embedder) prevents weight-learning or immutable-model conclusions. |
| Raw conversation retention, compaction, history and deletion | `apps/agent/src/db/repositories/conversations.ts`, `apps/agent/src/agent/memory.ts`, `apps/agent/src/agent/runner.ts`, `apps/agent/src/api/routes/chat.ts`, `apps/agent/src/agent/prompt.ts` | Direct, alongside [RT-RTE-context-window](runtime.md#rt-rte-context-window): raw-to-summary-to-later-model chain and independent UI reads. [MEM-OBJ-conversation-records](#mem-obj-conversation-records), [MEM-OBJ-conversation-summary](#mem-obj-conversation-summary). No automatic full-history reload by the model is established. |
| Backup export/import | `apps/agent/src/services/backup.ts`, `apps/agent/src/semantic/routes.ts` | Direct: lifecycle merge bypasses normal conflict diagnosis, summaries omitted on insert, retained local summaries on conflict, derived indexes rebuilt. Annotation on [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes). |
| Approvals, scheduled routines, notifications and receipts | Supplied runtime plus direct `apps/agent/src/agent/runner.ts`, `apps/agent/src/tools/memories.ts` | [RT-OBJ-pending-actions](runtime.md#rt-obj-pending-actions), [RT-RTE-action-approval](runtime.md#rt-rte-action-approval), [RT-RTE-scheduled-work](runtime.md#rt-rte-scheduled-work). Stored routine prompts supply task instructions; receipts/notifications are owner-facing results, not automatically a chat transcript or extracted fact store. Detailed scheduler/push implementation was not independently re-audited; actual delivery remains uninspected. |
| Retrieval evaluation | `docs/semantic-eval.md`, `scripts/semantic-eval.mjs` | Direct: published 18/18 is a floor-crossing test, not guaranteed target inclusion in the three-item prompt. [MEM-CLM-eval-scope](#mem-clm-eval-scope). No rerun or behavioral-benefit conclusion. |

Excluded implementation is the external Cloudflare SDK, model service internals, cloud persistence and push delivery. These exclusions prevent deployment durability, immutable weight identity, model compliance and delivery guarantees. Available but uninspected dependency internals/tests are not absences. Source labels such as “Learned in chat” describe origin/UI presentation, not demonstrated improvement.

## Core ideas

1. **Saving and validating are separate.** A new fact is saved before diagnosis. Deterministic rules create review obligations rather than retire old facts; optional Clef confidence can retire one automatically. An explicit correction retires its predecessor immediately, including when selected by the chat model. Neither process verifies the new fact against an external truth oracle. [MEM-RTE-memory-write](#mem-rte-memory-write).
2. **Lifecycle state changes selection, not all access.** Prompt recall normally excludes historical memories and labels uncertain ones; owner history and some searches can still expose past text. Keyword general search is a concrete counterpath to treating historical status as universal withdrawal. [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-requested-search](#mem-rte-requested-search).
3. **Vectors select text; they are not the model's remembered wording.** Normalized numerical BLOBs and model/hash/stamp metadata govern ranking and repair. Consumers then load current database rows and deliver selected text/excerpts. Embedding admission validates shape and budgets, not truth. A stale vector can select newly edited text because ordinary recall does not require a matching current content hash. [MEM-RTE-index-maintenance](#mem-rte-index-maintenance).
4. **Conversation memory has two durable forms.** Raw messages remain; a separate model compacts selected overflow into a replaceable summary. Later main-agent turns get that summary by value plus a recent suffix, not a pointer that automatically dereferences omitted history. This is a trace-fed behavior-shaping update without demonstrated improved capacity or preserved derivation reasons. [RT-RTE-context-window](runtime.md#rt-rte-context-window), [MEM-OBJ-conversation-summary](#mem-obj-conversation-summary).
5. **Retained text has different intended force by channel.** Memories and note excerpts are labelled data even when included in the system prompt. A stored automation prompt is deliberately delivered as the scheduled task instruction. Labels and prompt rules do not prove that the provider respects this distinction. [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-tal-memories
Label: tal_memories

Source-native identity: `tal_memories`, accessed by `MemoryRepository`. Storage: owner-bound Durable Object SQLite. Operative parts: natural-language `content` interpreted by owner/model; symbolic ID, category, source, lifecycle status, successor link, validity dates and timestamps interpreted by repository/selection rules. Source is coarse admission metadata (`manual`, `agent`, `import`), not a retained message citation or authentication of the statement's original author. Create trims content and refreshes an identical case-insensitive current memory instead of duplicating it; history rows do not block a new current copy. Explicit correction creates or reuses a current row and links the old row as historical. Owner PATCH instead overwrites wording in place. Lineage links retain predecessor text but no general correction rationale. Consumers are owner list/history/review UI, tool search, prompt selectors and neighbor diagnosis. At the later model, text is intended information under the data policy, while status has programmatic selection force before delivery. This is the concrete fact store behind, not a duplicate of, the multi-channel [RT-BAP-retained-context](runtime.md#rt-bap-retained-context); the supplied runtime declares no matching object. [SRC-1: `apps/agent/src/db/repositories/memories.ts`, `apps/agent/src/memory/service.ts`, `apps/agent/src/memory/lifecycle.ts`, `apps/agent/src/agent/prompt.ts`]

> const dup = this.db.one<Memory>(
>   `SELECT * FROM tal_memories WHERE lower(content) = lower(?) AND status != 'historical' ORDER BY updated_at DESC LIMIT 1`,
>   content,
> );
> --- `apps/agent/src/db/repositories/memories.ts`

#### MEM-OBJ-memory-reviews
Label: tal_memory_reviews

Source-native identity: `tal_memory_reviews` / `MemoryReviewRow`. Storage: DO SQLite. Form: symbolic IDs for newer/older memories and relationship enum; natural-language reason, clipped to 300 characters. Producer: rules or parsed Clef result through the history service; repeated ordered pairs reuse an existing review. It is a diagnosis/admission queue, distinct from destructive-tool authorization in [RT-OBJ-pending-actions](runtime.md#rt-obj-pending-actions). A review is not itself historical or uncertain status: both facts can remain current while awaiting review. Consumer: protected review endpoint joins live memory text; shipped MemoryPage displays both and the reason and sends the owner's selected resolution. Ordinary memory prompt construction does not join this review reason. Deletion/supersession/resolution removes relevant reviews; no durable per-review decision rationale is established beyond remaining fact/link state and a generic activity summary. [SRC-1: `apps/agent/src/db/repositories/memories.ts`, `apps/agent/src/memory/service.ts`, `apps/agent/src/memory/lifecycle.ts`, `apps/agent/src/api/routes/data.ts`, `apps/web/src/pages/MemoryPage.tsx`]

> const row: MemoryReviewRow = { id: newId(), ...input, reason: input.reason.slice(0, 300), created_at: now() };
> --- `apps/agent/src/db/repositories/memories.ts`

#### MEM-OBJ-semantic-vectors
Label: tal_semantic_vectors

Source-native identity: `tal_semantic_vectors`, one row keyed by memory ID. Storage: SQLite little-endian Float32 BLOBs plus a per-database decoded cache. Payload form: distributed numerical dense representation, normalized to unit length; it is derived data, not remote model parameter updates. Symbolic metadata is model name, dimensions, content hash and update time. `embeddingText` and content hashing establish lineage from memory content/category; they do not preserve a verbal account of why dimensions represent a fact. Later consumers perform cosine scanning for recall or neighbor nomination and then load text by ID. Model weights/version opacity remains with [RT-CMP-workers-embedder](runtime.md#rt-cmp-workers-embedder), which is the producer component, not this retained output. Distinct object within the index use described by [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks); no supplied object counterpart. Row-count cache checks catch inserts/deletes, not every same-count out-of-band replacement. Normal writes synchronize cache; this is not a distributed cache-consistency guarantee. [SRC-1: `apps/agent/src/semantic/vectorStore.ts`, `apps/agent/src/semantic/embeddings.ts`, `apps/agent/src/semantic/indexer.ts`, `apps/agent/src/semantic/recall.ts`, `apps/agent/src/semantic/neighbors.ts`]

> const cache = caches.get(db);
> if (cache && cache.model === model && cache.dims === dims && cache.count === count) return cache.vectors;
> --- `apps/agent/src/semantic/vectorStore.ts`

#### MEM-OBJ-item-vectors
Label: tal_semantic_item_vectors

Source-native identity: `tal_semantic_item_vectors`, keyed by item type/ID/part. Storage: SQLite unit-length little-endian Float32 BLOB and decoded cache per type/model/size. Numerical payload is separate from symbolic model/dims/hash/source stamp/part metadata. Unlike the memory index, lineage is chunked: tasks use title and at most 1000 description characters; automations use name and nonredundant message text, not schedule/run state; notes have a title part plus body parts. Bodies above 4000 characters split into at most forty 1200-character chunks without overlap. Text beyond that remains available to nonvector surfaces. Consumers score each item's best part, reload current rows and deliver titles/excerpts or schedules; they never send the numerical payload to the chat model. Pending checks can touch source stamps without recomputing unchanged vectors. A note shrunk since indexing loses extra parts on a writing pass. Distinct from [MEM-OBJ-semantic-vectors](#mem-obj-semantic-vectors) because source stamps, chunk retirement, caps and delivery differ; closest supplied [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks) describes both without declaring an object. [SRC-1: `apps/agent/src/semantic/itemStore.ts`, `apps/agent/src/semantic/itemText.ts`, `apps/agent/src/semantic/itemIndex.ts`, `apps/agent/src/semantic/itemRecall.ts`, `apps/agent/src/semantic/itemSearch.ts`]

> /** Chunks embedded per note; text past the last one is left to full-text search. */
> export const NOTE_MAX_CHUNKS = 40;
> --- `apps/agent/src/semantic/itemText.ts`

#### MEM-OBJ-conversation-records
Label: tal_messages

Source-native identity: `tal_messages` with its `tal_conversations` parent. Storage: SQLite. Parts: natural-language user/assistant text; symbolic role, timestamps, origin, completion/error state; JSON tool activity decoded against a schema. Activity is a readable execution/approval display record, not a guaranteed verbatim replay of provider tool outputs. Raw text originates in live owner/model turns or backup import; source marks imported rows. Later consumers include owner conversation reads, title/message keyword search, main-agent history selection and summary generation. Owner reads refresh approval outcomes but omit summary fields. Search tools return matching conversation titles/IDs, not their full messages. Raw retention therefore establishes independent UI access, not automatic full model reload. Distinct underlying retained object from the transformation route [RT-RTE-context-window](runtime.md#rt-rte-context-window) and ordinary turn route [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat); no supplied object counterpart. [SRC-1: `apps/agent/src/db/repositories/conversations.ts`, `apps/agent/src/api/routes/chat.ts`, `apps/agent/src/tools/search.ts`, `apps/agent/src/agent/runner.ts`]

> const { summary: _s, summary_upto: _u, ...rest } = conversation;
> --- `apps/agent/src/api/routes/chat.ts`

#### MEM-OBJ-conversation-summary
Label: Conversation summary

Source-native identity: `tal_conversations.summary` and `summary_upto`. Storage: SQLite. Natural-language summary is a model-derived replacement of a previous summary plus selected overflow text; timestamp boundary is symbolic exclusion metadata for later message windows. Guidance asks for facts, decisions, open questions and commitments, not a criticism log or derivation rationale. Content is trimmed to 2000 characters, with no fidelity validation or owner per-summary approval. Later chat prompts consume it as “Summary of earlier parts”; omitted raw messages remain in the independent message store until deletion. The summary is not an executable reference to those messages. Incoming backup summaries are not installed on new rows; existing local summaries survive backup conflicts. No alternative opaque checkpoint is shown at these app-level storage/compaction call sites; provider-internal state is uninspected. This is the retained output of [RT-RTE-context-window](runtime.md#rt-rte-context-window), not a second declaration of that route. [SRC-1: `apps/agent/src/agent/memory.ts`, `apps/agent/src/agent/runner.ts`, `apps/agent/src/db/repositories/conversations.ts`, `apps/agent/src/services/backup.ts`, `apps/agent/src/agent/prompt.ts`]

> summary = result.text.trim().slice(0, 2000);
> summaryUpto = window.overflow.at(-1)!.created_at;
> s.conversations.setSummary(conversation.id, summary, summaryUpto);
> --- `apps/agent/src/agent/runner.ts`

### Routes

#### MEM-RTE-memory-write
Label: Memory admission and revision

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Saved fact with superseded rows/review count to owner API or a tool receipt to the model; diagnosis failure does not undo the save.
- Later read-back: Current/history/status/link changes feed subsequent prompt recall, tool search and owner history/review reads; reasons feed owner review display, not normal prompt recall.
- Delegated visibility: Chat model supplies fact wording or explicit correction; Clef receives newer/older text sliced to 500 characters each and fixed relationship criteria, not the full originating conversation.
- Selection predicate: Valid tool/API input; duplicate current wording refreshes timestamp; conflictReview enables nomination on changed writes, and aiConflictCheck plus a real Clef hook and AI budget enables model diagnosis.
- Invalidation or expiry: Owner edit/status restore, explicit correction, review resolution or deletion changes retained facts; historical predecessor text remains until deletion. Reviews for superseded pairs are removed.
- Activation or effect: Automatic writes and explicit correction change future selectable content. Rules produce reviews; sufficiently confident Clef supersession changes older status. Actual later model dependence is unobserved.
- Evidence limits: No truth oracle, runtime trace or demonstrated fact accuracy; bounded candidate search cannot establish complete conflict detection.

Owner and admission: `remember` is an immediate write, at most three calls per turn, with schema and prompt guidance to save lasting owner facts or explicitly requested memories. Setting autoMemory changes instruction text, not a per-content human approval gate. The foreground model authors the extracted statement; code saves it. Owner API creation uses source manual; authenticated submission is per-content supply but not proof of original authorship. Explicit `update_memory` uses `correct` for changed wording: it saves a successor and retires the old memory without an approval card. Owner PATCH instead changes wording in place. Rejection/recovery is schema rejection, later owner edits/restoration/deletion or review actions; diagnosis is best effort after admission, not a gate that can discard the new fact. [SRC-1: `apps/agent/src/tools/memories.ts`, `apps/agent/src/agent/prompt.ts`, `apps/agent/src/api/routes/data.ts`, `apps/agent/src/memory/service.ts`]

> const { duplicate, ...memory } = this.repo.create({ ...input, valid_from: extractStatedDate(input.content) });
> // Saved first: nothing below can lose the memory.
> if (duplicate) return { memory, superseded: [], reviews: [] };
> --- `apps/agent/src/memory/service.ts`

Diagnosis uses up to eight full-text hits per search plus topic-specific searches, current nonhistorical rows and creation-time checks. Rules classify lexical/topic change, refinement and ambiguity. Even when `decide` returns supersede, `ruleDecision` converts that into owner review. With Clef enabled, rule hits and at most three additional semantic neighbors at cosine >= 0.6 are nominated. Clef >= 0.8 supersedes automatically; doubtful supersession produces review. Semantic-only contradiction requires >= 0.7; compatibility >= 0.8 can dismiss some rule reviews, but an unconfirmed rule replacement remains reviewable. No answer/malformed/timeout (default 3000 ms)/unavailable budget falls back to rule reviews, not deletion. Neighbor lookup requires current content hashes, unlike ordinary recall. Code chooses thresholds and applies lifecycle changes; Clef chooses relationships; owner can later restore, but has no per-Clef-result veto before automatic retirement. The operating mode is routine write-time maintenance, not a scored experiment. There is no expected reference outcome beyond fixed relationship criteria. [SRC-1: `apps/agent/src/memory/service.ts`, `apps/agent/src/memory/conflict.ts`, `apps/agent/src/semantic/neighbors.ts`]

> if (action === "supersede") return [{ oldId: a.oldMemoryId, action: "review", relationship: "possible_update", reason: a.reason }];
> --- `apps/agent/src/memory/service.ts`

> if (verdict.relationship === "supersedes") return verdict.confidence >= AUTO_SUPERSEDE_CONFIDENCE ? "supersede" : "review";
> --- `apps/agent/src/memory/conflict.ts`

Review consumer choices are keep both, mark older historical, permanently replace older, or discard newer. They are owner decisions through the shipped buttons. Keeping both removes the review, not the facts. Marking historical links the predecessor and may set valid-until from the newer stated date. Replacing/discarding deletes the selected fact and vector. Explicit correction preserves wording, not its reason; auto-supersession leaves link/status and generic activity, not the full Clef probability record. Thus retained diagnosis and next-read behavior are distinguishable, without attributing truth learning or theory building to relationship labels. Closest supplied routes are [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes) and [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat): this route crosses those entry channels and owns their memory-specific submechanisms, not either entire referent. [SRC-1: `apps/agent/src/memory/lifecycle.ts`, `apps/agent/src/memory/service.ts`, `apps/web/src/pages/MemoryPage.tsx`]

#### MEM-RTE-memory-recall
Label: Automatic memory recall

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected, lifecycle-labelled and budgeted text lines supplied in the system prompt for chat or a scheduled prompt.
- Later read-back: Retained personal facts from earlier writes are selected anew at each invocation; vectors can be repaired during recall, but prompt-only date prefixes/newer-wins note are not persisted facts.
- Delegated visibility: Provider sees fact text/category and lifecycle notes, not vectors, review reasons, raw provenance or the complete store.
- Selection predicate: Current owner message or scheduled prompt drives keyword/optional hybrid selection; history-intent permits past facts; recent active preferences can fill empty slots.
- Invalidation or expiry: Edit/delete/status/history-intent and index/config changes affect later selection; prompt budgeting can drop a selected fact without withdrawing it from storage.
- Activation or effect: Automatic selector pushes retained information into context without the foreground model requesting a search. Delivered text's actual effect on answers is unobserved.
- Evidence limits: Top-k/floors/intent heuristics and estimated token costs are not guarantees of relevance, complete history, recency correctness or model compliance.

Keyword route uses up to eight FTS/BM25 or LIKE matches, current by default; past-intent queries can add direct predecessors until eight slots are filled. Up to four recent active preferences pad remaining slots. Semantic route first indexes a lazy batch of at most fifty memories, fuses up to fifty vector hits and fifty keyword hits by reciprocal rank (k=60), and keeps eight. Vector floors use absolute/relative thresholds, with backstop top-up to four for memories; fallback to keyword applies on embedding failure/cap. Stored-vector near-duplicates can pull in up to two newer memories per hit, displacing eligible weak hits when possible. The implementation can skip pulls, and this numerical neighbor mechanism does not prove every selected past fact includes its actual successor. History intent and preference padding then apply; selected copies are sorted newest-first with saved-time prefixes and, with two or more memories, an extra newer-wins line. [SRC-1: `apps/agent/src/agent/memory.ts`, `apps/agent/src/semantic/recall.ts`, `apps/agent/src/semantic/index.ts`]

The runner then applies a separate memory budget, min(1500, floor(context tokens * 0.2)); cost is estimated content tokens + 8 and over-budget entries are skipped. Lifecycle formatting adds dates and at most 120 successor characters after that estimate, so this is not a strict provider-token bound. Final prompt groups current, uncertain and past sections. The recency note is guidance, not a durable lifecycle update; conflicts under review can still enter the current section. Distinct from [RT-RTE-context-window](runtime.md#rt-rte-context-window), which primarily controls message overflow/summary, and overlaps [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks) only on its enabled branch. The full route also includes the nonsemantic selector, so it is not contained in the semantic-only hook. [SRC-1: `apps/agent/src/memory/service.ts`, `apps/agent/src/agent/runner.ts`, `apps/agent/src/agent/prompt.ts`]

> return Math.min(1500, Math.floor(limits.maxContextTokens * 0.2));
> --- `apps/agent/src/agent/memory.ts`

> const cost = estimateTokens(memory.content) + 8;
> if (used + cost > maxTokens) continue;
> --- `apps/agent/src/memory/service.ts`

#### MEM-RTE-item-recall
Label: Automatic item recall

Part of: [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: At most three task/note/automation lines, with heading under a separate estimated 300-token budget, appended to the foreground system prompt.
- Later read-back: Earlier saved items, not chat summaries, supply current titles, note excerpts and reminder schedules after numerical selection.
- Delegated visibility: Model receives readable lines and IDs, including at most 160 note excerpt characters; not vectors, full notes or full automation prompt payloads.
- Selection predicate: Enabled semantic extension and a query vector already cached by memory recall for the owner message; best-part cosine with absolute/relative floors, no below-floor fallback; done tasks, completed automations, missing rows and failed one-shot automations excluded.
- Invalidation or expiry: Lazy catch-up embeds at most eight parts unless a pass is already running; current row/status checks suppress deleted/ineligible items, but old same-model vectors can still rank changed rows.
- Activation or effect: Code independently supplies selected retained text before model tool choice; the foreground model need not request retrieval. Changed answer behavior is unobserved.
- Evidence limits: No vector means no section, not keyword item recall. Scheduled runner does not call this item hook. Three slots and a token cap can exclude relevant items.

Source-native selector scores per type then globally sorts by cosine and type/ID ties. Notes expose the best chunk if applicable, otherwise the start. Task lines include current due data; automation lines expose schedule/name, not the task instruction used by scheduled execution. This is a material part of the supplied hook route with a distinct consumer payload/budget, not another declaration of its entire extensions object. Stored underlying task/note/automation text comes through direct owner administration, ordinary model tools or backup import under [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes) and [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat); auto-recall itself admits no new fact content. [SRC-1: `apps/agent/src/semantic/itemRecall.ts`, `apps/agent/src/semantic/index.ts`, `apps/agent/src/semantic/itemSearch.ts`, `apps/agent/src/agent/runner.ts`]

> const vector = peekQueryVector(ctx, message);
> if (!vector) return [];
> --- `apps/agent/src/semantic/itemRecall.ts`

#### MEM-RTE-requested-search
Label: Requested retained-data search

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool-result text to the current provider interaction, or protected HTTP search/list/history JSON to the owner client.
- Later read-back: Previously persisted facts/items/conversations are returned on a later explicit request; current tool-result accumulation is not itself another durable memory store.
- Delegated visibility: Search returns bounded facts/titles/excerpts/statuses; `read_note` returns at most 8000 content characters. Conversation search tools return IDs/titles, not a full prior transcript.
- Selection predicate: Model-chosen tool/query or owner HTTP query/ID; schema and executor caps apply. Semantic wrappers combine query and cached turn vectors for item additions while preserving upstream permissions.
- Invalidation or expiry: Current rows are reloaded; item status/view predicates differ by consumer. Owner deletes remove source rows, but an already delivered result is not recalled from a running model interaction.
- Activation or effect: A requesting consumer receives selected saved material through tool or UI delivery. Actual answer reliance is unobserved.
- Evidence limits: A storage API alone is not the consumer route: these findings are limited to registered tools and shipped owner API/UI callers. No unbounded model transcript reload is established.

`search_memories` keyword path returns ten and defaults to history intent/current; general upstream `search` returns five memories with no status filter. With semantic mode, memory search uses hybrid ranking (ten or five); general search replaces its memory objects with text/saved time but omits lifecycle status. Thus withdrawal from automatic current recall does not imply withdrawal from all query surfaces. Tools `search`, `list_tasks` and `search_notes` can append at most three meaning additions per surface using the tool query vector and the original turn vector. Item searches do bounded catch-up, use stored vectors if another pass is running, and schedule backfill where possible. Keyword results stay first; list_tasks additions respect the selected view and available slots. Note search excerpts are 200 or 400 characters; direct read_note allows a larger but still bounded reload. [SRC-1: `apps/agent/src/tools/memories.ts`, `apps/agent/src/tools/search.ts`, `apps/agent/src/tools/notes.ts`, `apps/agent/src/semantic/tools.ts`, `apps/agent/src/semantic/itemSearch.ts`]

> memories: s.memories.search(i.query, 5).map((m) => ({ id: m.id, content: m.content, ...(m.status !== "active" ? { status: m.status } : {}) })),
> --- `apps/agent/src/tools/search.ts`

Protected `/semantic/search` exposes cosine/fused diagnostics; item debug retrieval has no normal prompt status filters. Memory debug search does not run the automatic selector's lazy index pass. Owner `/memories` list and history/review views are separate readers that can explicitly include historical rows. These paths establish actual requested readers, not just hypothetical library callers. Closest supplied [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks) covers semantic tool substitution, but this route spans the keyword and owner diagnostic/read paths too; no duplicate entire referent. [SRC-1: `apps/agent/src/semantic/routes.ts`, `apps/agent/src/api/routes/data.ts`, `apps/web/src/pages/MemoryPage.tsx`]

#### MEM-RTE-index-maintenance
Label: Index production and cleanup

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Index reports/pending counts, asynchronous completion promises, or owner maintenance JSON; saves can return before embedding finishes.
- Later read-back: Persisted vectors feed future recall/search/neighbor nomination; source rows remain the text authority. Failure/cap leaves pending work and possibly stale vectors.
- Delegated visibility: Embedding provider receives bounded constructed source texts or query text; chat model receives only subsequently selected readable content.
- Selection predicate: Memory API/tool writes, lazy recall, item search/chat catch-up, successful import, enabled/model-change backfill or explicit reindex; stored config, pending metadata and separate budget reservations decide work.
- Invalidation or expiry: Orphans/deleted source vectors purged; memory hashes/model/dims and item source stamps/hashes identify pending repair. Explicit semantic data deletion drops derived tables/config without deleting source facts/items.
- Activation or effect: Code writes normalized numerical payloads automatically, shaping future selection. There is no per-vector owner review or evidence that retrieval quality improved.
- Evidence limits: Bounded asynchronous passes are not atomic source/index snapshots; ordinary scans enforce model/dimensions/existence, not current content-hash equality. Exact remote model revisions remain unpinned.

Memory index runs compare every memory's content-derived hash, model and known dimensions, oldest update first, embedding up to fifty by default. Item passes prioritize tasks, automations, note titles then bodies; stamp-equal sources can skip construction/hashing, full passes force checking. Model/dimension mismatch makes work pending. A pass has at most one queued follow-up per database; memory and item passes have separate guards. Memory index and query embeddings share a daily request cap; items have a separate request cap and 500000 estimated tokens/day, with zero memory cap disabling item embedding too. Output validation checks count/dimensions/finite numbers in the adapter; it is not semantic validation. Admission is code-selected transformation following owner config or earlier content admission, not per-derived-content human control. [SRC-1: `apps/agent/src/semantic/indexer.ts`, `apps/agent/src/semantic/itemIndex.ts`, `apps/agent/src/semantic/embeddings.ts`, `apps/agent/src/semantic/itemText.ts`]

> if (v?.model !== model || (dims > 0 && v.dims !== dims) || v.content_hash !== hash) pending.push({ id: row.id, text, hash });
> --- `apps/agent/src/semantic/indexer.ts`

On-save HTTP middleware and wrapped remember/update tools request background memory indexing. Task/note/automation saves defer embeddings to lazy read paths; import requests memory indexing and a full item pass; enabling/changing model backfills; explicit reindex drops all vectors then loops until done/capped/no progress. The owner can disable or delete semantic data; original stores survive so rebuilding is recovery rather than rollback of fact content. MemoryHistoryService deletes memory vectors even without semantic mode, clears reviews/links, and removes the matching memory.created activity quote. Item HTTP/approved deletes purge derived rows even when disabled if config exists; reads additionally skip missing source rows. Cleanup is best effort around HTTP hooks and does not prove privacy erasure of copies in chat, summaries, backups or provider services. [SRC-1: `apps/agent/src/semantic/routes.ts`, `apps/agent/src/semantic/tools.ts`, `apps/agent/src/memory/service.ts`, `apps/agent/src/db/repositories/memories.ts`]

> dropSemanticData(s.db);
> dropVectorCache(s.db);
> deleteSemanticConfig(s.settings);
> invalidateSemanticCache(s);
> --- `apps/agent/src/semantic/routes.ts`

Countercase to a strong freshness claim: if a same-model text edit is pending beyond the batch/cap, ordinary cosine scanning can use its old vector, then load the current text. Neighbor nomination explicitly rejects hash-stale candidates; this stronger check does not transfer to all retrieval routes. Reindexing is not proof that concurrent deletion cannot be followed by an in-flight stale write; later orphan checks and consumer existence checks limit the effect. Closest supplied [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks) concerns runner delivery; this route crosses HTTP/config/import/maintenance and read-time indexing, so is not its duplicate. [SRC-1: `apps/agent/src/semantic/recall.ts`, `apps/agent/src/semantic/itemSearch.ts`, `apps/agent/src/semantic/neighbors.ts`, `apps/agent/src/semantic/indexer.ts`]

### Claims

#### MEM-CLM-eval-scope
Label: Semantic evaluation scope

Claimed operation: the checked-in semantic surfaces evaluation reports PASS for 18/18 cases on bge-m3. It is reported operation, not independently observed execution here. The scorer embeds distinct query/part texts, chooses each item's best cosine, and admits a positive when its target clears the absolute floor; it does not require target placement within the capped prompt section. EX-A2 reports target rank four and a three-item section yet passes. Runtime item recall also applies a relative floor and live status filters that this scorer does not reproduce fully. The expected targets/negative cases are a test oracle for this offline scorer, not an online memory admission gate or answer oracle used by chat. Distinct from supplied [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks): it bounds the evaluation claim, not the hook's wiring. [SRC-1: `docs/semantic-eval.md`, `scripts/semantic-eval.mjs`, `apps/agent/src/semantic/itemRecall.ts`, `apps/agent/src/semantic/itemSearch.ts`]

> const pass = c.kind === "positive" ? targetIndex >= 0 && ranked[targetIndex].score >= floor : sectionItems === 0;
> --- `scripts/semantic-eval.mjs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-context-window](runtime.md#rt-rte-context-window)

The durable raw-to-derived chain is [MEM-OBJ-conversation-records](#mem-obj-conversation-records) → prior-summary plus overflow → [MEM-OBJ-conversation-summary](#mem-obj-conversation-summary) → later main-agent system prompt. Trace origin is mixed owner and assistant text (including imported text once it enters history); approval outcomes are synthesized into the text before compaction. This is an automatic trace-fed write with code admission, not just raw logging. The summarizer frame excludes tools and unrelated main context; only its text return escapes. Code evicts oldest eligible messages and excludes summary-covered timestamps; a recent suffix remains by value. At most 200 messages are loaded before eviction, so raw retention is not a guarantee that all older omitted messages ever enter a summary. Summary failure/cap leaves a suffix without new compaction; there is no demonstrated fidelity or improved capacity. Historical raw text remains independently owner-readable/searchable but no registered conversation-read tool reloads it in full. Source-level context isolation resembles a separate summarization frame, not addressable heap references. [SRC-1: `apps/agent/src/agent/runner.ts`, `apps/agent/src/agent/memory.ts`, `apps/agent/src/db/repositories/conversations.ts`, `apps/agent/src/tools/index.ts`, `apps/agent/src/tools/search.ts`]

The budget is computed from the previous base system string before summary replacement; rebuilding the system string does not recalculate historyBudget. Therefore the estimate is not a hard total-context invariant. Summary content retains compressed facts/decisions, not a durable transcript of its own reasons. See the supplied route's retained summarizer passage and [MEM-OBJ-conversation-summary](#mem-obj-conversation-summary). [SRC-1: `apps/agent/src/agent/runner.ts`]

#### On [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes)

Backup admission differs from normal memory writes: import directly upserts SQL, preserves a same-ID local memory when its update timestamp is newer/equal, restores valid successor links, and does not run the usual duplicate/content conflict diagnosis. New rows use source import, while existing source fields are not changed by the memory ON CONFLICT update. Unknown original authorship stays local to imported content. Export includes raw messages, facts/lifecycle and summaries, but not vectors or pending memory-review reasons. Incoming summaries are dropped for new conversation rows; same-ID existing local summaries survive. Thus “regenerated from visible messages” is an intended future route, not proof that every restored transcript has a corresponding fresh summary. Retained imported messages can feed later history/summary even though retry-as-live-owner-input is fenced. Derived indexes are repaired through import middleware and later reads, not imported as trusted opaque payloads. [SRC-1: `apps/agent/src/services/backup.ts`, `apps/agent/src/semantic/routes.ts`, `apps/agent/src/agent/runner.ts`]

> if (existing && existing.updated_at >= m.updated_at) continue;
> --- `apps/agent/src/services/backup.ts`

#### On [RT-OBJ-pending-actions](runtime.md#rt-obj-pending-actions)

Its owner-readable summary/preview and opaque JSON payload have different consumers: the owner judges text; the approval handler uses structured target/hash/payload. The saved activity metadata carries refreshed approval state into subsequent message windows as short outcome notes, not a full payload replay. Cancellation/expiry rejects the pending effect but does not erase the proposal text from existing conversation activity. This is authorization/result memory rather than inferred personal knowledge. Memory deletion proposals preserve this path; correction writes do not use it. [SRC-1: `apps/agent/src/agent/runner.ts`, `apps/agent/src/tools/memories.ts`]. Supporting passage and dispatch evidence: [RT-RTE-action-approval](runtime.md#rt-rte-action-approval).

#### On [RT-RTE-scheduled-work](runtime.md#rt-rte-scheduled-work)

Stored automation message is a persistent natural-language task instruction; schedule/enabled/state fields are symbolic dispatch controls. The scheduled model receives the stored message as a user message plus automatic memory recall under [MEM-RTE-memory-recall](#mem-rte-memory-recall). It does not receive foreground conversation summary/history or automatic item-section recall. Read tools can still request retained items; read-time semantic maintenance can write derived vectors. Notifications/receipts are later owner-readable results, not automatically saved facts or recurrent model feedback. This route has across-run instruction persistence without evidence that receipts revise the stored routine or improve later operation. [SRC-1: `apps/agent/src/agent/runner.ts`]. Supplied scheduler/receipt evidence: [RT-RTE-scheduled-work](runtime.md#rt-rte-scheduled-work).

#### On [RT-BAP-retained-context](runtime.md#rt-bap-retained-context)

At the update consumer, lifecycle metadata programmatically changes eligibility; at the chat consumer, selected natural-language fact/note/summary text is intended informational context. At the scheduled consumer, the retained automation message supplies actual task guidance. Numerical ranking influences delivery before either interpretation. These forces must remain separate from a claim that all stored natural language is equally trusted or all information is reliably ignored as instructions. The shipped policy says it is data, while prompt construction includes it in system text. [SRC-1: `apps/agent/src/agent/prompt.ts`, `apps/agent/src/agent/runner.ts`]. Supplied policy passage: [RT-CLM-context-authority](runtime.md#rt-clm-context-authority).

## Write side

The admission mechanisms are distinct:

| Mechanism | Author/proposer versus admission decision | Retained result and rejection/recovery |
| --- | --- | --- |
| Model remember/correct | Foreground model authors; schema/executor/history code admits. Prompt autoMemory/explicit-memory guidance is policy, not human per-fact review. | Fact or successor/history link; owner later edits/restores/deletes. [MEM-RTE-memory-write](#mem-rte-memory-write). |
| Owner manual create/PATCH/correct/status | Owner supplies/edits a specific content item; protected endpoint/schema admits. PATCH and correction have different preservation semantics. | New fact, overwritten wording, or historical predecessor; direct delete needs no tool approval. [MEM-RTE-memory-write](#mem-rte-memory-write). |
| Rule/Clef diagnosis | Code nominates; rules defer retirement to owner, Clef plus thresholds can admit retirement automatically. Starting/enabling the feature is not per-result approval. | Review reason or lifecycle state/link. New fact survives failed diagnosis; no external truth oracle. [MEM-RTE-memory-write](#mem-rte-memory-write). |
| Review resolution | Owner sees reason and two live texts, chooses an action; code applies it. | Kept pair, historical link or permanent deletion; reason queue is removed rather than retained as a cumulative criticism history. [MEM-OBJ-memory-reviews](#mem-obj-memory-reviews). |
| Backup merge | Owner selects a file, not necessarily each statement; schema, timestamp, link and field rules decide content admission. | Raw text/facts/items restored; summary, approval and routine-prompt fences limit authority; normal conflict checks bypassed. Annotation on [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes). |
| Index maintenance | Earlier source admission plus owner opt-in/config; code constructs text, provider derives vectors, shape/budget checks admit. | Numerical indexes and symbolic metadata, repairable from source; disable/delete/reindex controlled by owner. [MEM-RTE-index-maintenance](#mem-rte-index-maintenance). |
| Trace compaction | Code overflow/budget trigger; separate model proposes summary; code trims and stores automatically. | Lossy summary plus timestamp; raw records stay independent, not automatically dereferenced. [RT-RTE-context-window](runtime.md#rt-rte-context-window). |
| Stored routine and ordinary task/note editing | Owner API or model tools supply retained work content; destructive model operations use approval, other writes are immediate. | Ordinary source text and routine instruction persist; imported routines paused. Covered by [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes), [RT-RTE-owner-chat](runtime.md#rt-rte-owner-chat), [RT-RTE-action-approval](runtime.md#rt-rte-action-approval), [RT-RTE-scheduled-work](runtime.md#rt-rte-scheduled-work). |

Saving a fact can therefore change later behavior without waiting for evaluation. Retiring a fact does not erase its text; deleting it purges its primary row, relevant reviews/links/vector and the matching creation-activity quote, not independently copied message/summary/backup/provider content. Clear memories is not clear conversation history. Source-grounded scope of deletion is [MEM-RTE-index-maintenance](#mem-rte-index-maintenance) and the separate conversation-delete repository path. There is no basis for a universal privacy-erasure claim. [SRC-1: `apps/agent/src/memory/service.ts`, `apps/agent/src/db/repositories/memories.ts`, `apps/agent/src/db/repositories/conversations.ts`]

Reasons persist only selectively: pending review rows carry short reasons to the owner; history preserves predecessor text/link/dates, while derived vector payloads and summaries have no retained explanatory derivation. The source code can explain a transformation, but that is different from a stored reason read by the later main agent. These retained changes establish memory mechanisms, not independently successful learning, reflection, autonomous theory building or exercised self-improvement.

## Read-back

There are both automatic and requested deliveries. Code supplies selected memories on every chat/scheduled invocation using the current message/routine text; enabled foreground item recall adds a separately capped section. The model does not ask for either push. Tool calls are requested retrieval: the model supplies a query or note ID, and host code selects and returns bounded retained text. Owner list/history/search/debug reads are a third consumer, not evidence that the agent receives all returned UI data. Summary consumption is automatic within a conversation; stored automation consumption is alarm-triggered instruction delivery. [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-item-recall](#mem-rte-item-recall), [MEM-RTE-requested-search](#mem-rte-requested-search), [RT-RTE-context-window](runtime.md#rt-rte-context-window), [RT-RTE-scheduled-work](runtime.md#rt-rte-scheduled-work).

The budgets apply at different stages: memory top-k and its estimated 20%/1500-token cap; item floors/top-three/300-token section; tool-specific result/excerpt/call caps; history suffix and summary compaction; per-context query-vector cache of at most eight normalized queries; separate inference/indexing daily caps. These are not one global token/freshness guarantee. Reloadable source material may remain outside the current model window, but IDs in returned text require an actual exposed tool to recover it: read_note is bounded, and conversation search is title/ID delivery rather than transcript replay. [SRC-1: `apps/agent/src/agent/memory.ts`, `apps/agent/src/semantic/recall.ts`, `apps/agent/src/semantic/itemRecall.ts`, `apps/agent/src/tools/notes.ts`, `apps/agent/src/tools/search.ts`]

## Integration issues

- **Qualification of historical withdrawal:** the supplied hook/context account does not establish universal exclusion of historical facts. Keyword general search has no status filter, and semantic general search omits lifecycle status from its returned memory objects. This corrects any stronger reading of “past facts only for past questions,” not the narrower automatic-selector finding. Consequence: keep automatic eligibility separate from requested access and labelling. [MEM-RTE-requested-search](#mem-rte-requested-search), [MEM-RTE-memory-recall](#mem-rte-memory-recall), [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks). Evidence: SRC-1 `apps/agent/src/tools/search.ts`, `apps/agent/src/semantic/tools.ts`.
- **Qualification of recency/freshness guarantees:** near-duplicate pulls can be skipped and final memory budgeting can omit selected text; stale same-model vectors can select current text. A source comment's “never ... without its replacement” is not a guaranteed final-provider property. Hash-strict neighbor checks are a counterexample to treating all semantic consumers alike. Consequence: do not infer complete conflict protection from the recall label. [MEM-RTE-memory-recall](#mem-rte-memory-recall), [MEM-RTE-index-maintenance](#mem-rte-index-maintenance), [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks). Evidence: SRC-1 `apps/agent/src/semantic/recall.ts`, `apps/agent/src/semantic/neighbors.ts`, `apps/agent/src/memory/service.ts`.
- **Evaluation qualification:** 18/18 floor passes do not prove each target reaches the prompt; EX-A2 rank four passes despite three slots. Consequence: no end-to-end retrieval/answer benefit can be attributed to the reported evaluation. [MEM-CLM-eval-scope](#mem-clm-eval-scope). Evidence: SRC-1 `docs/semantic-eval.md`, `scripts/semantic-eval.mjs`.
- **No duplicate supplied identities found:** the fact/review/vector/raw/summary objects have no supplied object counterparts. The new item-recall route declares containment in the supplied semantic hook. The memory write/recall/search/index-maintenance routes cross multiple supplied entry/runner routes and are deliberately not replacement declarations of them. Reconciliation should connect these parts with [RT-RTE-semantic-hooks](runtime.md#rt-rte-semantic-hooks), [RT-RTE-context-window](runtime.md#rt-rte-context-window), [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes) and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context), preserving their separate referents.
- **Unresolved operation/provenance:** actual enabled configuration, owner decisions, observed retrieval reliance, summary fidelity and provider version/retention are not supplied. Source paths establish wiring, not activation or benefit. This limits operational conclusions for all memory routes and [RT-CMP-workers-embedder](runtime.md#rt-cmp-workers-embedder), [RT-CMP-clef](runtime.md#rt-cmp-clef); it does not erase their inspectable mechanisms.
- **Unresolved concurrent cleanup strength:** static index maintenance can recreate stale/orphan derived rows after asynchronous source changes; later purge/existence checks bound retrieval, but atomic erasure or crash-safe convergence was not established. Consequence: do not promote intended cleanup to complete erasure. [MEM-RTE-index-maintenance](#mem-rte-index-maintenance). Evidence: SRC-1 `apps/agent/src/semantic/indexer.ts`, `apps/agent/src/semantic/itemIndex.ts`, `apps/agent/src/semantic/routes.ts`.

## Limitations and checks

This is static inspection at SRC-1's frozen commit, not a deployment audit. No target tests, examples, model requests, dependency installs or experiments ran. Source identity/revision was checked with Git; every added path belongs to that checkout. The supplied member types and full invocation/record contract were read; this worker wrote only its assigned output, answers and identity paths. Missing execution evidence prevents activation/benefit claims. Coarse source flags, lossy summaries, finite candidate lists and opaque provider state prevent complete provenance, fidelity, conflict detection and parameter-learning conclusions. Available scheduler/push branches outside the direct memory recheck retain the supplied runtime's limits rather than being newly inferred absences.

Validation: `commonplace-run validate-output` passed for the supplied invocation after citation-syntax repair: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The check does not establish semantic support, acceptance or operation.
