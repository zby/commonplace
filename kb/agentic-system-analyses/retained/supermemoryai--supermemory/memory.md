---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Supermemory's document-to-fact/profile memory chain, public read-back adapters and documented review/withdrawal controls, with opaque engine maintenance."
run-id: AAS-2026-10-19-supermemory-1cc18c778c48-01
source-identity: https://github.com/supermemoryai/supermemory
reviewed-boundary: f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe
---

# Supermemory memory report

## Boundary and evidence

The subject is the public Supermemory artifact at the boundary's frozen commit, not the non-public extraction server. The [boundary](boundary.md#boundary-and-evidence) includes shipped consumers, tools, prompts, documentation and evaluations. Memory scope here follows automatic middleware, model-selected tools, MCP, voice lifecycle hooks, exact-file memory, connector ingestion and graph display. The backend's processing, review and withdrawal contracts are included as doctrine/design, not executable implementation. All new source findings use SRC-1. No service, target example or target test was executed.

Direct reads extend the supplied runtime with `packages/tools/src/shared/memory-client.ts`, `packages/tools/src/shared/prompt-builder.ts`, `packages/tools/src/tools-shared.ts`, the complete Claude memory adapter and its simple example, the complete LiveKit memory implementation and agent subclass, MCP tool registration/client/formatting/search/document/guided-save handlers, the graph-data hook and playground graph API, and the documentation cited below. Selected Mastra/VoltAgent hook bodies were read directly; searches located other Python lifecycle surfaces without establishing all their transformations. The runtime's Vercel/OpenAI/Agent Framework routes remain supplied evidence, not new direct inspections of those complete adapters.

| Entry or operation | Source paths in SRC-1 | Coverage and remaining limit |
| --- | --- | --- |
| Automatic conversation write and profile/search injection | `packages/tools/src/vercel/index.ts`, `packages/tools/src/vercel/middleware.ts`, `packages/tools/src/conversations-client.ts`; shared helpers above | Supplied [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call), [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache); direct helper annotations below. Backend admission/visibility remains opaque. |
| OpenAI Chat/Responses and framework tools | `packages/tools/src/openai/middleware.ts`, `packages/tools/src/ai-sdk.ts`, `packages/tools/src/tools-shared.ts` | Supplied [RT-RTE-openai-call](runtime.md#rt-rte-openai-call), [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop); direct withdrawal helper inspection. Not a universal human approval boundary. |
| MCP registration, saves, upload and space routing | `apps/mcp/src/server/tools/index.ts`, `apps/mcp/src/server/client/index.ts`, `apps/mcp/src/server/tools/guided-save.ts` | Registry directly checked against supplied [RT-RTE-mcp-save](runtime.md#rt-rte-mcp-save), [RT-RTE-upload-session](runtime.md#rt-rte-upload-session), [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget), [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context). Guided-save opens a draft view; it is not itself a retained write. Widget save interaction internals uninspected; cannot establish exercised human approval. |
| MCP search/profile/list/document read | `apps/mcp/src/server/tools/search-memory.ts`, `apps/mcp/src/server/tools/get-document.ts`, `apps/mcp/src/server/format.ts`, `apps/mcp/src/server/client/index.ts` | Direct [MEM-RTE-mcp-read](#mem-rte-mcp-read); supplied context prompt route remains distinct. |
| Claude exact-file commands and shipped driver | `packages/tools/src/claude-memory.ts`, `packages/tools/src/claude-memory-simple-example.ts`, `packages/tools/package.json` | Direct [MEM-OBJ-claude-file](#mem-obj-claude-file), [MEM-RTE-claude-file](#mem-rte-claude-file). Export and caller checked; no inferred graph extraction required for exact read-back. |
| LiveKit recall, capture, explicit remember/forget | `packages/livekit-sdk-python/src/supermemory_livekit/memory.py`, `packages/livekit-sdk-python/src/supermemory_livekit/agent.py` | Direct [MEM-RTE-livekit-session](#mem-rte-livekit-session); tool schemas and external SDK compatibility not fully inspected. Legacy API signatures differ from current v5 JS callers. |
| Agent Framework | `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py` | Supplied [RT-RTE-python-context](runtime.md#rt-rte-python-context): optional storage includes system text. Other connection/middleware entry internals not directly traced here; no all-entry parity conclusion. |
| Mastra and VoltAgent | `packages/tools/src/mastra/processor.ts`, `packages/tools/src/voltagent/hooks.ts`, `packages/tools/src/voltagent/middleware.ts` | Selected direct reads/searches: tagged system-message replacement and output processors/hooks are alternative consumers. Detailed conversions, advanced search parameters and merged-hook ordering remain uninspected; not asserted equivalent to Vercel. |
| Cartesia, Pipecat, Python OpenAI | `packages/cartesia-sdk-python/src/supermemory_cartesia/agent.py`, `packages/pipecat-sdk-python/src/supermemory_pipecat/service.py`, `packages/openai-sdk-python/src/supermemory_openai/middleware.py` | Source searches locate per-turn context/legacy prompt fallback, frame interception/storage queue, and sync/async facades respectively. Full predicates, payload transformations and consumer placement remain uninspected; prevents adapter-wide filtering, persistence or failure guarantees. These are available evidence, not access gaps or absences. |
| Extraction, chunking, embeddings, dreaming, graph/profile synthesis | `apps/docs/concepts/how-it-works.mdx`, `apps/docs/concepts/graph-memory.mdx`, `apps/docs/recall/user-profiles.mdx` | Direct doctrine/design: [MEM-RTE-engine-dreaming](#mem-rte-engine-dreaming), objects below; non-public implementation prevents verification of model selection, update reasons, initial state and ranking. |
| Inference review, source update/delete, semantic withdrawal | `apps/docs/recall/memory-review.mdx`, `apps/docs/recall/memory-operations.mdx`, `apps/docs/ingestion/document-operations.mdx` | Direct [MEM-RTE-inference-review](#mem-rte-inference-review), [MEM-RTE-source-maintenance](#mem-rte-source-maintenance), [MEM-RTE-semantic-forget](#mem-rte-semantic-forget); deployed callers and propagation to every cached/profile form unobserved. |
| Connectors and selection | `apps/docs/connectors/overview.mdx`, `apps/docs/connectors/managing-resources.mdx` | Direct [MEM-RTE-connector-sync](#mem-rte-connector-sync). Provider implementations and individual provider details not inspected; overview has scheduling inconsistency. |
| Graph read/display | `apps/memory-graph-playground/src/app/api/graph/route.ts`, `packages/memory-graph/src/hooks/use-graph-data.ts`, `apps/mcp/src/server/client/index.ts` | Direct [MEM-CLM-graph-display](#mem-clm-graph-display). UI layout consumes backend relations; not evidence of inference or durable graph edits. Other widget interactions uninspected. |
| Evaluation, prompts, external coding integrations | `packages/tools/package.json`, `apps/docs/memorybench/overview.mdx`, `skills/supermemory/SKILL.md` | Test entry declarations directly read; evaluator and skill initial coverage supplied by boundary. No executed evaluation or durable evaluator-feedback-to-memory loop established. Detailed tests and skill maintenance rules not newly inspected. External plugin code and MemoryBench runs are outside this frozen source; prevents learning/performance attribution. |

No root CLI dispatch for durable memory is asserted. The checked public package exports include Claude/Mastra/OpenAI/VoltAgent and AI SDK paths; the checked MCP registry includes search, profile, list/get, graph, namespace, save, forget and upload operations. Hook alternatives are retained in the table rather than silently reduced to a primary store. Static package publication is covered by [RT-RTE-publish-tools](runtime.md#rt-rte-publish-tools), not treated as memory read-back.

## Core ideas

1. **Documents and derived facts are different retained products.** Raw conversation/file content can remain available as documents/chunks while an opaque model derives facts, links and profiles. `done` for indexing does not imply graph readiness under dynamic dreaming. The source's term “learning model” is not evidence of weight updates or improved capacity. See [MEM-RTE-engine-dreaming](#mem-rte-engine-dreaming).
2. **Selection is usually automatic within a requested or host-triggered route.** A foreground model may request a tool; middleware independently selects profile/query content before a model call. Neither establishes unsolicited delivery independent of an invocation. Backend ranking and profile synthesis are opaque; local mode, namespace, last-user-text extraction and deduplication are inspectable. See annotations on [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call).
3. **The actual consumer receives less provenance than storage can expose.** Default middleware emits fact strings, not inference flags, relation edges, review stamps or source documents. MCP search preserves a document pointer, and a separate document read can recover bounded source text. That optional reload is not automatic grounding. Exact-file memory is a separate path retaining authored prose without requiring fact synthesis. See [MEM-RTE-mcp-read](#mem-rte-mcp-read), [MEM-RTE-claude-file](#mem-rte-claude-file).
4. **Withdrawal changes several layers differently.** Document deletion is documented as permanent; memory forgetting is soft deletion; inference review can undo a decline. Already injected text and local caches are another layer. No inspected withdrawal handler globally purges all model windows. See [MEM-RTE-source-maintenance](#mem-rte-source-maintenance), [MEM-RTE-inference-review](#mem-rte-inference-review) and [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget).

## Shared records

### Components

#### MEM-CMP-claude-model
Label: Claude memory-example model

Identity: the simple example's `claude-sonnet-4-5` Anthropic endpoint. Representational form: distributed-parametric provider model; storage substrate: external provider, not remote memory documents. Parameters changing during operation: uninspected provider internals; adapter issues no weight-update request. Exact immutable version pinned: no weight digest or immutable revision supplied. Mutable endpoint resolution: provider alias behavior uninspected. Distinct from the playground OpenAI generation component [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model). SRC-1, `packages/tools/src/claude-memory-simple-example.ts`, implementation:

> model: "claude-sonnet-4-5",
> max_tokens: 2048,
> messages: [{ role: "user", content: userMessage }],
> --- `packages/tools/src/claude-memory-simple-example.ts`

### Operative objects

#### MEM-OBJ-document-content
Label: Document content and chunks

Identity: namespace-scoped raw submitted documents and source-grounding chunks. Form: natural-language text for transcripts/extracted text, potentially opaque original multimodal input; symbolic document IDs/status/metadata are separate access state, not the text itself. Substrate: remote engine storage; documentation calls it a temporal vector-graph engine, physical implementation uninspected. Lineage: user/assistant transcripts, caller-authored statements, files, URLs or connector items; extraction/OCR/chunking are declared transformations. Backend initialization and actual embedding lineage unknown. Consumers: document retrieval, chunk search and model extraction; content has interpretive authority at model consumers, not guaranteed truth. Distinct from wrapper-local formatted text [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache) and namespace/capability state [RT-OBJ-space-state](runtime.md#rt-obj-space-state). SRC-1, `apps/docs/concepts/how-it-works.mdx`, doctrine/design:

> A **document** is raw input — whatever you hand Supermemory:
> --- `apps/docs/concepts/how-it-works.mdx`

> | **Document chunks** | Grounding in the raw source (RAG / SuperRAG) | [SuperRAG](/concepts/super-rag), [Search API](/recall/search) |
> --- `apps/docs/concepts/how-it-works.mdx`

Dense embeddings are a separate numerical representation, not readable source text. Their declared generation is in the same pipeline; model/storage mutability remains limited by [RT-CMP-local-embeddings](runtime.md#rt-cmp-local-embeddings) and [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary), not inferred from public adapters.

#### MEM-OBJ-memory-facts
Label: Extracted and inferred memory text

Identity: the graph's atomic fact strings, including inferred facts and updates/extensions. Form: natural-language claims; substrate: remote engine, with IDs/edges/access flags separated below. Lineage: document-to-fact extraction and cross-memory derivation, not raw transcripts alone. Documentation promises historical links but does not establish retained explanatory reasons, model deliberation or a proof for each inference. Consumers: backend profile/graph/search and later agent context. Distinct from [MEM-OBJ-document-content](#mem-obj-document-content) by transformation and lifecycle; no object counterpart in runtime, whose [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call) describes their downstream use. SRC-1, `apps/docs/concepts/graph-memory.mdx`, doctrine/design:

> Supermemory **infers** a fact you never stated in one place, from patterns across memories.
> --- `apps/docs/concepts/graph-memory.mdx`

> `isLatest` (and related graph fields) keep retrieval on the current fact without erasing the past.
> --- `apps/docs/concepts/graph-memory.mdx`

#### MEM-OBJ-memory-state
Label: Memory identity, relations and eligibility state

Identity: per-memory IDs, `isLatest`, `isForgotten`, `isInference`, temporal fields, relation links and internal review metadata. Form: symbolic metadata consumed by API selection/review rules and client display rules; substrate: remote graph/API rows, copied selectively into client objects. Lineage: engine and review/forget operations, not authorship of fact text. The backend consumer's exclusion rules are documented, not inspected. The MCP mapper retains version/latest/forgotten/static/inference flags but omits source-document/history arrays from its v5 list mapping. Distinct from content and [RT-OBJ-space-state](runtime.md#rt-obj-space-state): this is fact eligibility/lineage state, not actor namespace routing. SRC-1, `apps/docs/recall/memory-review.mdx`, doctrine/design; `apps/mcp/src/server/client/index.ts`, implementation:

> A reviewed memory gets an internal review stamp in its metadata so it drops out of the
> review queue (declined memories also leave search, since they're forgotten). **Undo**
> clears that stamp — and un-forgets a declined memory — bringing it back.
> --- `apps/docs/recall/memory-review.mdx`

> isLatest: memory.isLatest,
> isForgotten: memory.isForgotten,
> isStatic: memory.isStatic,
> isInference: memory.isInference,
> --- `apps/mcp/src/server/client/index.ts`

#### MEM-OBJ-profile-summary
Label: Static, dynamic and bucketed profile

Identity: per-namespace profile sections sampled/synthesized from memories. Form: natural-language facts and synthesized summaries with symbolic IDs/section names; substrate: service-owned representation, persistence/recomputation strategy uninspected. Lineage: automatically maintained from ingested content; aggregated older-memory summaries are a distinct derived form, not an exact pointer to one memory. Consumers: middleware/MCP/voice context and documented custom applications. Public JS default formatting consumes static/dynamic text, not buckets; MCP explicitly maps entries to strings. Distinct from [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache), which caches formatted output, not the profile's canonical content. SRC-1, `apps/docs/recall/user-profiles.mdx`, doctrine/design:

> The exception is synthesized summaries of older memories, whose `id` starts with `aggregated_` — they don't map to a single memory.
> --- `apps/docs/recall/user-profiles.mdx`

> Buckets are **custom topical categories** for a profile — an axis that sits alongside
> `static` and `dynamic`, grouping facts by subject (e.g. `preferences`, `goals`,
> `work`) instead of by how long-lived they are.
> --- `apps/docs/recall/user-profiles.mdx`

#### MEM-OBJ-claude-file
Label: Claude memory file document

Identity: namespace-scoped documents carrying `source: claude-memory`, `claude_memory_type: file`, `file_path` and text. Form: natural-language authored file body; symbolic path encoding/metadata resolves exact reads and writes. Substrate: remote Supermemory documents, not the local filesystem implied by `/memories/`. Lineage: caller/model create/edit commands; exact-document reads avoid ranked chunks. Its meaning need not be extracted into graph facts to be read again. Consumer: Claude via returned tool-result text with line numbers. Reasons survive only if the author writes them in the file; no automatic rationale schema. Distinct from [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache) and the graph fact/profile objects; no runtime counterpart for this file store. SRC-1, `packages/tools/src/claude-memory.ts`, implementation:

> /** Maps Claude's memory tool commands to Supermemory documents in one namespace. */
> --- `packages/tools/src/claude-memory.ts`

> const document = readResult.document
>
> let content = document.content
> --- `packages/tools/src/claude-memory.ts`

### Routes

#### MEM-RTE-engine-dreaming
Label: Document processing and graph dreaming

Distinct from client submission [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call): this is the remote transformation after admission, not a duplicate adapter route. Trigger: document ingestion/re-ingestion; producer: opaque extraction/memory model and engine. Raw input becomes searchable chunks/embeddings, then facts/relations and profile. Default dynamic dreaming groups related documents; instant processes one document alone. Software/model admission decides what becomes a fact; human provenance or starting ingestion is not per-fact approval. Remote rejection/failure is represented by statuses; internal filtering, retry policy and rollback uninspected. Guidance: documentation's coherent-unit extraction and temporal graph rules, not an inspected extraction prompt. Operating mode: open ingestion; no answer oracle or criticism-driven improvement trigger established. SRC-1, `apps/docs/concepts/how-it-works.mdx`, `apps/docs/concepts/graph-memory.mdx`, doctrine/design.

- Immediate return: Document identity/status from ingestion; not proof of finished extraction.
- Later read-back: Document/chunk search, memory search and profile can deliver different retained derivatives to later invocations; actual completion/durability unobserved.
- Delegated visibility: Service receives content, identity and metadata; later applications receive selected derivatives, not necessarily source or reasons.
- Selection predicate: Namespace and document/grouping identity; dynamic groups related documents, instant isolates the current document; model extraction/ranking internals uninspected.
- Invalidation or expiry: Document reprocessing, updates, temporal expiry, contradiction and noise filtering are documented; exact algorithms and propagation timing uninspected.
- Activation or effect: Derived text is eligible for public retrieval/injection pathways; exercised dependence and benefit unobserved.
- Evidence limits: Non-public engine; no source-supported claim that “learning model” means parameter training, that `done` proves memory readiness, or that inferred statements are true.
- design conclusion status: claimed
- operation conclusion status: uninspected

> A document with status `done` has its chunks indexed for search. Memories (the graph's facts, updates and derived facts) come from a second phase called **dreaming**.
> --- `apps/docs/concepts/how-it-works.mdx`

> - **Time-based** — temporary facts drop after they expire (“exam tomorrow”, “meeting at 3pm today”).
> - **Contradiction** — updates win for “what’s true now.”
> - **Noise filtering** — casual, non-meaningful chatter is less likely to become durable memory.
> --- `apps/docs/concepts/graph-memory.mdx`

#### MEM-RTE-inference-review
Label: Inferred-memory review and undo

Distinct from [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget): a documented review queue and three-action state transition, not MCP exact-match admission. Trigger: client lists inferred memories, then submits approve/decline/undo for one ID. Engine proposes inferred text; caller decides the review action. A human review UI is afforded, but generic HTTP callers do not prove mandatory human control. API permissions and reviewability can veto; undo restores unreviewed state. Guidance is review semantics, not a truth oracle; `parentCount` ranks support quantity, not validated correctness. Operating mode: open maintenance requests. SRC-1, `apps/docs/recall/memory-review.mdx`, doctrine/design.

- Immediate return: Up to 50 queued memories and total, or ID/inference/forgotten/review status after action.
- Later read-back: Approve leaves content searchable without inference flag; decline forgets it and removes it from queue/search; undo un-forgets and requeues. Later search consumers may receive restored text.
- Delegated visibility: Reviewer receives memory text, parent count, timestamps and metadata; response does not establish full derivation reasons or original parents' text.
- Selection predicate: Namespace and unreviewed inferred state; excludes forgotten/expired/reviewed; parent count descending then creation time descending; action targets one memory ID.
- Invalidation or expiry: Internal review stamp removes reviewed entries from queue; undo clears it. Profile/cache propagation timing uninspected.
- Activation or effect: State transitions and search consequences are documented; no deployed review execution or answer change observed.
- Evidence limits: This is not pre-search quarantine: approval says “stays in search.” Backend implementation, human participation and objective correctness uninspected.
- design conclusion status: claimed
- consumer conclusion status: afforded
- operation conclusion status: uninspected

> | **Approve** | `isInference` cleared | Stays in search, no longer flagged as inferred |
> | **Decline** | `isForgotten` set | Removed from search entirely — a rejected guess is forgotten |
> | **Undo** | back to unreviewed | Returns to the queue, flagged as inferred again |
> --- `apps/docs/recall/memory-review.mdx`

#### MEM-RTE-source-maintenance
Label: Source document update and deletion

Distinct from extracted-memory forgetting [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget). Trigger/proposal: caller changes a document's content/metadata or supplies IDs to delete. Caller controls proposal; API owns acceptance. Generic SDK caller leaves human authorship/approval unresolved. Content updates reprocess; metadata-only updates merge without reindexing. Deletion allows terminal done/failed documents, reports per-ID errors for processing documents, and is documented permanent. No local approval or restoration transaction follows from API availability. Operating mode: open maintenance; no answer oracle. SRC-1, `apps/docs/ingestion/document-operations.mdx`, doctrine/design; narrower JS tool precheck directly inspected in `packages/tools/src/tools-shared.ts`.

- Immediate return: Updated document operation or delete count/errors; HTTP success can contain partial failures.
- Later read-back: Reprocessed source can alter derived memories; deleting a document is documented to forget its derived memories. Later document/memory retrieval is the affected consumer.
- Delegated visibility: Service receives replacement content/merged metadata or namespace-scoped document IDs; caller sees operation result, not verified downstream prompt eviction.
- Selection predicate: Exact document identity within namespace, including caller-defined IDs; deletion terminal-state eligibility.
- Invalidation or expiry: Permanent document removal; derived memories forgotten; already returned prompt text and local adapter caches not proven purged.
- Activation or effect: API semantics claimed; JS helper checks status and deletion count before reporting success, but no remote operation observed.
- Evidence limits: No non-public reprocessing implementation or proof about shared/multi-document inferred descendants, aggregated profile refresh, or immediate downstream visibility.
- design conclusion status: claimed
- operation conclusion status: uninspected

> Memories derived from a deleted document are forgotten.
> --- `apps/docs/ingestion/document-operations.mdx`

> Deletes are permanent — no recovery.
> --- `apps/docs/ingestion/document-operations.mdx`

#### MEM-RTE-semantic-forget
Label: Semantic preview and bounded forgetting

Distinct from MCP's five-candidate exact-text branch [RT-RTE-mcp-forget](runtime.md#rt-rte-mcp-forget). Trigger: caller topic/query and mandatory `dryRun`; service semantically selects up to 100 matches. Caller may preview and then submit exact IDs to bind application to the reviewed set; a fresh `dryRun: false` request reselects. Software/model match judgment is not an answer oracle. Human review is recommended, not established as protocol-enforced. Backend authentication/acceptance can veto; no general undo promised for this forget route. Operating mode: open maintenance. SRC-1, `apps/docs/recall/memory-operations.mdx`, doctrine/design.

- Immediate return: Count/matches/errors; semantic response alone does not record which dry-run mode was used.
- Later read-back: Applied matches are soft-deleted and documented excluded from search while preserved; preview alone changes no retained fact.
- Delegated visibility: Caller receives selected memory IDs/text, service receives topic or exact IDs; no automatic host-context removal.
- Selection predicate: Namespace and semantic query; at most 100 per semantic request; exact-ID follow-up avoids preview/apply drift.
- Invalidation or expiry: Remote search eligibility changes; preserved rows are not permanent erasure. Local cache/profile propagation uninspected.
- Activation or effect: Documented capability; no applied deletion or downstream answer effect observed.
- Evidence limits: Backend semantic selector and preview stability uninspected; repeating previews is not pagination or a safety proof.
- design conclusion status: claimed
- consumer conclusion status: afforded
- operation conclusion status: uninspected

> **Exact, bound deletes.** Re-running `forgetMatching` with `dryRun: false` re-runs the semantic match, so the result can drift from the preview if the namespace changed in between.
> --- `apps/docs/recall/memory-operations.mdx`

#### MEM-RTE-mcp-read
Label: MCP explicit memory and document read-back

Distinct from requested context prompt [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context): tools expose query results, lists and exact document reload to the MCP host. Trigger: registered tool call; selector: caller arguments plus namespace resolver and service ranking. Search default is ten results at threshold 0.6, memory mode with included documents. Profile mapper returns static/dynamic strings, dropping IDs/buckets. List mapping retains eligibility flags but not history/document pointers despite formatter support for them. `getDocument` first tries a document ID; on 404 it can resolve a memory ID through included document identity. No write/admission occurs here; host decides further use. Operating mode: open requests, no answer oracle. SRC-1, `apps/mcp/src/server/tools/index.ts`, `apps/mcp/src/server/tools/search-memory.ts`, `apps/mcp/src/server/tools/get-document.ts`, `apps/mcp/src/server/client/index.ts`, `apps/mcp/src/server/format.ts`, implementation.

- Immediate return: Text/structured tool result; search gives memory ID, text, similarity and optional source document ID; document gives summary/content/status.
- Later read-back: Retained remote content is read on later tool invocations and becomes host-visible tool context. There is no automatic subsequent model call in these handlers.
- Delegated visibility: MCP host sees selected displays, not the entire store; search text capped at 200,000 characters per item, document content at 200,000; document text summary at 4,000 and list fields at 500.
- Selection predicate: Query plus namespace for search; page/limit for lists; exact ID or memory-to-document fallback for document read; formatter filters forgotten/nonlatest list entries.
- Invalidation or expiry: Requests fetch current API results; no clearing of prior host turns is wired; backend eligibility and cache freshness remain external.
- Activation or effect: Tool dispatch, mapping and formatting wired; model use and evidence-sensitive response unobserved.
- Evidence limits: Similarity is not truth/confidence; optional pointer reload is not guaranteed grounding. Structured document result retains summary separately from text formatting.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> searchMode: "memories",
> threshold: SEARCH_THRESHOLD,
> include: { documents: true },
> --- `apps/mcp/src/server/client/index.ts`

> const MAX_LIST_FIELD_CHARS = 500
> const MAX_DOCUMENT_CONTENT_CHARS = 200_000
> --- `apps/mcp/src/server/format.ts`

#### MEM-RTE-claude-file
Label: Claude file editing and exact reload

No counterpart after comparison with framework tools [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop): this exported adapter uses Anthropic's native memory-command schema and exact file documents, not semantic fact tools. Trigger: caller/model command; adapter dispatches view/create/replace/insert/delete/rename. Path/schema, read resolution and service acceptance admit/veto requests. Model can author arbitrary prose; no per-content human approval or truth filter wired. Creation/update guidance is command semantics; what persists is file content plus metadata, not model weights. Rename writes destination then deletes source without a local transaction rollback; destination can already exist. Operating mode: open requests, no answer oracle. SRC-1, `packages/tools/src/claude-memory.ts`, `packages/tools/src/claude-memory-simple-example.ts`, implementation.

- Immediate return: Success/error or numbered file text/directory listing, wrapped as Anthropic tool result.
- Later read-back: A later `view` fetches exact stored document body or requested lines. The shipped example passes tool results back into a second Claude invocation; actual cross-session reuse unobserved.
- Delegated visibility: Claude gets selected file body/range or listing and operation results; not all graph/profile memory or the account credential.
- Selection predicate: Namespace plus reversible path ID with legacy fallback; stored source/path metadata must match; directory list pages through documents filtered by file metadata and checks path prefix.
- Invalidation or expiry: Edit replaces body using update, add only on not-found; delete checks one deletion; rename can leave partial state on failure. No local TTL or model-window eviction.
- Activation or effect: Command executor and example's return-to-model channel wired; compliance and durable service completion unobserved.
- Evidence limits: File path validation is logical namespace/path checking, not OS isolation. Exact file storage does not establish autonomous curation or repeated refinement. Example performs one tool-result follow-up, not an indefinite agent loop.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // v5 `add` with an existing id appends; `update` replaces, so writes try update first.
> --- `packages/tools/src/claude-memory.ts`

> const toolResult = await memoryTool.handleCommandForToolResult(
> block.input as any,
> block.id,
> )
> toolResults.push(toolResult)
> --- `packages/tools/src/claude-memory-simple-example.ts`

#### MEM-RTE-livekit-session
Label: LiveKit session capture and recall

Distinct from Agent Framework provider [RT-RTE-python-context](runtime.md#rt-rte-python-context), whose LiveKit note only establishes hook dispatch. This route's producer is completed conversation-item events plus explicit remember calls. `attach` registers events; `bind` scopes tag/session identity. `capture: always` defaults on; software admits nonempty user/assistant text, excludes marked injections and duplicate item IDs. Caller may disable capture; service can reject. Captured turns retain their original scope across rebinds. Failure requeues batches, close retries; overflow drops oldest buffered turns. Explicit remember submits trimmed text; forget submits supplied ID/text to legacy SDK. No human per-content veto or local truth check wired. Operating mode: open voice sessions; no answer oracle. SRC-1, `packages/livekit-sdk-python/src/supermemory_livekit/memory.py`, `packages/livekit-sdk-python/src/supermemory_livekit/agent.py`, implementation.

- Immediate return: Enriched chat context, event side effects, or short explicit tool-operation text; normal call can proceed without recall.
- Later read-back: Role-labelled conversation batches become remote documents; later profile/search recall can supply derived context. Remember also supplies source text; extraction remains external. Recall futures/preload text are session-local reuse, not durable canonical memory.
- Delegated visibility: Memory API receives conversation text/tag/custom ID/platform/kind. Host model gets wrapped assistant-role memory before the current user turn when timestamps are supported; caller profile can be fallback.
- Selection predicate: Mode/profile plus current user text; query search threshold default 0.1 and search-limit default ten, maximum twenty; recall deadline default two seconds. Recall reuse keys tag and user ID or query; same-words turns without IDs can share the fallback key. Storage groups leading turns by original scope and targets 100,000 content characters per batch, but an oversized first item is still taken.
- Invalidation or expiry: Prior marked assistant injections removed before recall; failed recall may reuse matching call-start profile. Buffer caps at 2,000; failed batches requeued; successful submission does not evict remote facts. Instant-processing 402 disables instant attempts for rest of call and uses default schedule.
- Activation or effect: Lifecycle/agent hooks, capture and assistant-context insertion wired; actual voice session, SDK compatibility, extraction and benefit unobserved.
- Evidence limits: Uses legacy container-tag/profile/search signatures, not proven interoperable with v5 service. `_seen`, buffer and recalled strings are process state, not durable recovery checkpoints. API forget success label is not verified visibility removal.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> capture: Literal["always", "never"] = "always"
> capture_dreaming: Literal["dynamic", "instant"] = "instant"
> --- `packages/livekit-sdk-python/src/supermemory_livekit/memory.py`

> role = message_role(item)
> if role not in ("user", "assistant"):
> return
> text = message_text(item)
> if not text or is_injected_memory(text):
> return
> --- `packages/livekit-sdk-python/src/supermemory_livekit/memory.py`

> except BaseException:
> async with self._lock:
> self._buffer = batch + self._buffer
> raise
> --- `packages/livekit-sdk-python/src/supermemory_livekit/memory.py`

#### MEM-RTE-connector-sync
Label: Connector acquisition, selection and disconnection

Distinct from file upload [RT-RTE-upload-session](runtime.md#rt-rte-upload-session): documented continuing import from external sources. Trigger: provider setup/OAuth or config, resource selection, webhook/schedule/manual sync. External authors supply documents; connector/service code admits them. User authorization/resource picker controls scope, not per-document truth approval; direct selection update and config providers permit software-driven admission. Admin/write permissions can veto selection; sync already running returns 409. Operating mode: open continuous ingestion; no answer oracle. Guidance is provider/resource configuration and document limits. SRC-1, `apps/docs/connectors/overview.mdx`, `apps/docs/connectors/managing-resources.mdx`, doctrine/design.

- Immediate return: Connector identity, authorization/picker links or sync state; OAuth approval is not completed extraction.
- Later read-back: Imported documents enter namespace processing and later search/profile paths; already imported material can survive disconnection with `deleteDocuments: false`.
- Delegated visibility: Provider authorization grants and selected external content reach service; later applications receive derived results via normal recall, not a demonstrated direct push into agent context.
- Selection predicate: Namespace; GitHub repositories, Gmail labels or Drive files/folders; other providers may sync everything. Saved selection replaces prior selection and starts sync; exact provider filtering implementation uninspected.
- Invalidation or expiry: Default connector delete permanently deletes imported documents; false preserves them. Selection-change removal semantics and downstream profile/cache propagation uninspected.
- Activation or effect: Documented import/read-back affordance; no sync run, provider deletion propagation or agent activation observed.
- Evidence limits: Non-public provider engines; overview prose and table disagree about some schedules. No uniform real-time or four-hour guarantee asserted.
- design conclusion status: claimed
- consumer conclusion status: afforded
- operation conclusion status: uninspected

> Config providers (Web Crawler, S3, Granola) return `authorization: null` and start syncing immediately.
> --- `apps/docs/connectors/overview.mdx`

> The new selection replaces the current one and starts a sync.
> --- `apps/docs/connectors/managing-resources.mdx`

> Setting `deleteDocuments=false` is useful when you want to disconnect an integration without losing the memories that were already imported.
> --- `apps/docs/connectors/overview.mdx`

### Claims

#### MEM-CLM-graph-display
Label: Graph display is a consumer, not the inference engine

Claim: public graph code renders remote document/memory data; it does not establish how the service derives facts. Distinct from [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary): this adds a concrete non-agent consumer and a misleading-label check. The playground API forwards page/limit/sort/order/container tags to the legacy graph endpoint; default limit 500. MCP's graph client uses the same legacy endpoint with schema validation, default limit 200. The graph hook encodes backend relation types as edges, falls back to parent updates and maps unknown relation types to updates. Missing target nodes suppress edges. Thus visible graph structure is a transformed subset, not independent validation of derivation semantics. Local layout coordinates/cluster colors are transient display state, not learned dense embeddings. SRC-1, `apps/memory-graph-playground/src/app/api/graph/route.ts`, `apps/mcp/src/server/client/index.ts`, `packages/memory-graph/src/hooks/use-graph-data.ts`, implementation:

> // 2. Memory-to-memory relation edges from backend data.
> //    Uses memoryRelations (Record<targetId, relationType>) as primary source,
> //    falls back to parentMemoryId for legacy data.
> --- `packages/memory-graph/src/hooks/use-graph-data.ts`

#### MEM-CLM-adapter-variants
Label: Alternative adapter hooks have distinct context controls

Claim: Mastra/VoltAgent cannot be silently treated as Vercel-equivalent. No counterpart after comparison with [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call), which is explicitly Vercel-scoped. Mastra input clears the tagged system-message block every invocation, then may reuse cached text; output submits converted messages when configured always. VoltAgent `onPrepareMessages` chooses raw versus prepared messages; `onEnd` reconstructs input plus assistant output and invokes save. Detailed conversions and failure cleanup require further inspection before all-adapter guarantees. These code hooks establish available integration, not actual host invocation or benefit. SRC-1, `packages/tools/src/mastra/processor.ts`, `packages/tools/src/voltagent/hooks.ts`, implementation:

> messageList.clearSystemMessages("supermemory")
> --- `packages/tools/src/mastra/processor.ts`

> const inputMessages = (args.rawMessages ??
> args.messages) as unknown as VoltAgentMessage[]
> --- `packages/tools/src/voltagent/hooks.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-file-reload
Label: Authored file into Claude tool context

Consumer: Claude's follow-up invocation; channel: numbered file prose in Anthropic user-role tool results; force: interpretive content/instruction, not an enforced program constraint. Horizon: remote documents can survive adapter instances; actual cross-session use unobserved. Distinct from middleware fact insertion [RT-BAP-memory-context](runtime.md#rt-bap-memory-context), using exact authored file documents rather than profile/search text. Source/evidence: [MEM-RTE-claude-file](#mem-rte-claude-file), SRC-1, `packages/tools/src/claude-memory-simple-example.ts`:

> { role: "assistant", content: response.content },
> { role: "user", content: toolResults },
> --- `packages/tools/src/claude-memory-simple-example.ts`

#### MEM-BAP-eligibility-selection
Label: Review and forgetting state into later search eligibility

Consumer: remote search/review selector; channel: symbolic latest/forgotten/inference/review state; force: documented service selection rule, not persuasion of the foreground agent. Horizon: across requests until update/undo/expiry; service enforcement uninspected. Distinct from active namespace routing [RT-BAP-space-selection](runtime.md#rt-bap-space-selection) and text authority [RT-BAP-memory-context](runtime.md#rt-bap-memory-context). [MEM-RTE-inference-review](#mem-rte-inference-review), [MEM-RTE-semantic-forget](#mem-rte-semantic-forget), SRC-1, `apps/docs/recall/memory-operations.mdx`, doctrine/design:

> Forgotten memories are excluded from search results but preserved.
> --- `apps/docs/recall/memory-operations.mdx`

## Annotations

#### On [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call)

Memory lineage: submitted transcript is raw conversation text, mixing user assertions and generated assistant statements; it is not itself a derived, warranted fact. The backend's further trace-to-fact/profile transformation is [MEM-RTE-engine-dreaming](#mem-rte-engine-dreaming). Selected retained parts: static/dynamic profile and query-ranked memory text, with mode-specific omission. Local deduplication normalizes dates, whitespace and case, prioritizing static over dynamic over search. This is exact-variant filtering, not semantic criticism. Query mode avoids suppressing results against a profile that is not delivered.

Read-back selector: latest user text, namespace and mode; shared helper requests memory-mode search at 0.6 threshold alongside profile when applicable. No explicit search count/token truncation is supplied to this shared search request. Default formatter renders strings; custom prompt callback receives selected result objects but default prompt excludes their metadata/lineage. This differs from a universal provenance-preserving memory channel. SRC-1, `packages/tools/src/shared/memory-client.ts`, `packages/tools/src/shared/prompt-builder.ts`, `packages/tools/src/tools-shared.ts`, implementation:

> return memory
> .trim()
> .replace(/^\[recent\]\s*/i, "")
> .replace(/^\[\d{4}-\d{2}-\d{2}\]\s*/, "")
> .trim()
> .replace(/\s+/g, " ")
> .toLowerCase()
> --- `packages/tools/src/tools-shared.ts`

#### On [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache)

Storage/lineage: in-process materialized display string after remote selection/deduplication, not raw source or canonical graph. Authority: a nonempty hit is reused as model context without checking remote mutations. New-user refresh in the supplied Vercel record bounds this staleness; remote forgetting does not imply eviction of a continuation's cached string. The object therefore supplies a working-context reuse mechanism, not durable learning or a historical evidence archive. Evidence is the supplied record and direct shared formatting helpers, SRC-1, `packages/tools/src/shared/memory-client.ts`.

#### On [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop)

Withdrawal curation: shared JS `forgetMemory` uses a semantic dry-run for content input, then filters normalized exact text and forgets those IDs. This is not MCP's candidate confirmation branch, nor arbitrary semantic bulk application. `deleteDocument` first reads the document, rejects defined nonterminal status and checks actual deletion count/errors. Admission remains software/caller-controlled, not per-content human approval; removing remote content does not clear tool results already present in host context. SRC-1, `packages/tools/src/tools-shared.ts`, implementation:

> const preview = await client.memories.forgetMatching(namespace, {
> query: params.content,
> dryRun: true,
> })
> ids = preview.matches
> .filter((match) => normalizeMemoryFact(match.memory) === target)
> .map((match) => match.id)
> --- `packages/tools/src/tools-shared.ts`

#### On [RT-RTE-mcp-save](runtime.md#rt-rte-mcp-save)

Editing/adoption surface: `guided-save` returns prefill, writable namespaces and active space as view data, allowing a draft/review surface distinct from immediate add. Its handler does not itself submit content. A human can edit/approve through the intended interactive experience; generic calls to add/save still do not establish such control. SRC-1, `apps/mcp/src/server/tools/guided-save.ts`, implementation:

> content: [textContent("Opening memory save form...")],
> structuredContent: sc,
> --- `apps/mcp/src/server/tools/guided-save.ts`

#### On [RT-BAP-memory-context](runtime.md#rt-bap-memory-context)

Consumer/authority limits: add LiveKit assistant-role memory insertion as a distinct channel via [MEM-RTE-livekit-session](#mem-rte-livekit-session). It is not system-role enforcement. Source trust is not upgraded by headings such as static profile or by approval clearing an inference flag. MCP client maps static/dynamic entries to `fact.memory`; default shared prompt formats strings. Reasons, parent links, review metadata and numerical vectors are not automatically supplied to the actual generation consumer. SRC-1, `apps/mcp/src/server/client/index.ts`, `packages/tools/src/shared/prompt-builder.ts`, implementation:

> static: result.profile.static.map((fact) => fact.memory),
> dynamic: result.profile.dynamic.map((fact) => fact.memory),
> --- `apps/mcp/src/server/client/index.ts`

## Write side

Automatic middleware and voice capture supply trace-fed writes, but the raw trace and durable behavior-shaping derivative must be distinguished. [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call) submits converted conversation after generation; [RT-RTE-openai-call](runtime.md#rt-rte-openai-call) submits supplied history before generation; [RT-RTE-python-context](runtime.md#rt-rte-python-context) defaults storage off and can include system text. [MEM-RTE-livekit-session](#mem-rte-livekit-session) captures completed user/assistant events, excludes its marked injections, buffers/retries and requests instant processing unless unavailable. These are different write admissions, not a single transcript policy.

The raw-to-derived-to-consumer chain is conversation/file/connector source → remote document/chunks → opaque extraction/dreaming → fact/profile → selected model context. The public adapter establishes submission and later retrieval wiring, while [MEM-RTE-engine-dreaming](#mem-rte-engine-dreaming) establishes only the declared internal transformation. Alternate retained forms include exact source documents, chunks, fact history, aggregated older-memory summaries and authored Claude files. None is shown as a complete host-context checkpoint. Backend initialization, extraction prompts and detailed embeddings provenance remain unknown without suppressing known formatting/capture transformations.

Human control differs by mechanism: exact content supplied in a tool call can be human-authored, model-authored or mixed; immediate save has no universal human approval. Guided-save affords content editing; connector OAuth/resource selection authorizes acquisition scope, not individual facts. Model-authored Claude files are admitted by path/command/service checks. Inference review explicitly affords per-fact decisions, but inferred facts are already searchable before approval. Software truth validation is not established by any of these admission checks. Sources and passages are retained in the corresponding records.

Maintenance has separate products and reversibility: source update reprocesses; metadata-only edits do not reindex; source delete is permanent and claims derived forgetting; semantic forgetting is soft and can drift between preview/apply; inference review has undo. The JS exact-text helper and MCP exact-candidate handler are narrower alternatives. Connector deletion can preserve imported documents. Those outcomes are traced to search eligibility and later consumers in their routes, not equated with physical erasure or global context cleanup.

Derived behavior-shaping strings do not automatically carry reasons. Document pointers, relation edges and parent counts can expose some lineage, but not a checked explanation of why an inference is warranted. Default prompt paths omit even much of that metadata. Authored files can retain arbitrary rationale; whether the model writes useful reasons or later uses them is unobserved. No inspected evaluator result was shown admitted into a revised extraction rule, file, fact or prompt; package tests and benchmark reports are not by themselves trace learning evidence.

## Read-back

There are three materially different request directions. Middleware/lifecycle hooks automatically select retained material when a host is about to invoke its model; a model/caller can explicitly request search/profile/document/file tools; documented connector sync automatically writes documents but does not independently push them into model context. Backend results still depend on requested recall. Profile “always-on” language is a usage pattern, not proof that every model invocation receives every memory.

Vercel's bounded retrieval wait and LRU reuse govern context preparation, not a total model-token budget. Shared default formatting performs deduplication without a local token cap. MCP requested context limits fact counts, while explicit document tools cap characters and expose truncation. Claude exact reads offer line ranges but no universal prompt-token accounting. LiveKit caps query-result count and recall time, strips prior injections and can fall back to call-start profile. These choices can preserve stale facts after a remote mutation; successful forgetting is not a proof of immediate absence from all consumers.

Working-context control in the inspected paths is selective replacement/removal of owned blocks, tagged messages or marked assistant injections, plus optional reload of external retained content. Caller-authored instructions and ordinary host turns remain under host control. This is not an inspected full-history summary/compaction implementation. Documentation's dynamic profile compaction denotes remote synthesis of selected facts/episodes, including aggregated summaries; its algorithm and reasons retention remain opaque. No stack-frame-style sub-agent context isolation is inferred from adapters or from opaque backend model processing. The source account does not require that analogy to explain selection and omission.

MCP source-document reload and Claude exact-file view are real alternative consumers, not hypothetical storage APIs. The former recovers bounded document text by ID after search or list; the latter's shipped driver feeds returned text to Claude. Graph rendering is another actual consumer, but has presentation authority rather than agent behavioral authority. Read-back establishes delivery/eligibility, not compliance, correctness, learning benefit or improved future capacity.

## Integration issues

- **No correction to the supplied runtime is required.** Its selected trace explicitly leaves other adapters and backend maintenance unresolved. This report extends that inventory rather than converting those limits into absences. [MEM-CLM-adapter-variants](#mem-clm-adapter-variants) and [MEM-RTE-livekit-session](#mem-rte-livekit-session) add differentiated consumers.
- **Record overlap:** [MEM-RTE-mcp-read](#mem-rte-mcp-read) is adjacent to, not identical with, [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context): explicit tools versus prompt request, different budgets and payloads. [MEM-RTE-engine-dreaming](#mem-rte-engine-dreaming) follows [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call) but belongs to the opaque engine. [MEM-RTE-livekit-session](#mem-rte-livekit-session) expands the hook note in [RT-RTE-python-context](runtime.md#rt-rte-python-context), not the Agent Framework referent. [MEM-BAP-file-reload](#mem-bap-file-reload) and [MEM-BAP-eligibility-selection](#mem-bap-eligibility-selection) are distinct from runtime text/namespace paths. No proposed duplicate or supersession remains after these identity comparisons.
- **Version skew:** current v5 profile is query-free, while inspected LiveKit and searched Python voice adapters use legacy profile/container-tag signatures. [MEM-RTE-livekit-session](#mem-rte-livekit-session), [MEM-OBJ-profile-summary](#mem-obj-profile-summary), SRC-1, `apps/docs/recall/user-profiles.mdx` and LiveKit source. Consequence: implementation wiring does not establish service compatibility or all-adapter behavior. No deployed version evidence resolves it.
- **Readiness and replacement:** dynamic `status: done` can precede memory readiness; stable-ID add appends while Claude replacement uses update. [MEM-RTE-engine-dreaming](#mem-rte-engine-dreaming), [MEM-RTE-claude-file](#mem-rte-claude-file), SRC-1, `apps/docs/ingestion/document-operations.mdx`, `packages/tools/src/claude-memory.ts`. Consequence: successful submission cannot be promoted to finished graph refresh, and repeated ID is not generic overwrite.
- **Lineage lost at delivery:** [MEM-OBJ-memory-state](#mem-obj-memory-state), [MEM-RTE-mcp-read](#mem-rte-mcp-read) and runtime authority annotation show that source storage/display schema richness exceeds default model payloads. MCP list mapper does not preserve formatter-supported source/history arrays; profile flattening loses IDs/buckets, and aggregate IDs are not individually forgettable source facts. Consequence: no default complete audit/reasoning trail at the model consumer.
- **Withdrawal propagation:** [MEM-RTE-inference-review](#mem-rte-inference-review), [MEM-RTE-source-maintenance](#mem-rte-source-maintenance), [MEM-RTE-semantic-forget](#mem-rte-semantic-forget), [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache). Remote exclusion is documented, not observed; refresh of synthesized profile summaries, multi-source descendants and already injected/cached text is unresolved. Prevents universal removal and immediate-consistency claims.
- **Connector schedule ambiguity:** overview describes OneDrive as scheduled, while its table lists webhooks; general synchronization prose includes schedules that do not apply uniformly to Granola. [MEM-RTE-connector-sync](#mem-rte-connector-sync), SRC-1, `apps/docs/connectors/overview.mdx`. Consequence: retain acquisition/selection contracts without asserting one timing guarantee. Selection changes' removal semantics also unresolved.
- **Uninspected alternative integrations/evaluation:** coverage table names public Cartesia/Pipecat/Python OpenAI, Agent Framework middleware, advanced VoltAgent behavior and detailed tests not fully traced. [MEM-CLM-adapter-variants](#mem-clm-adapter-variants) is deliberately bounded. No cross-adapter guarantee, exhaustive maintenance taxonomy or evaluator-driven update loop can be concluded from this sample. Non-public extraction/ranking and external benchmark/plugin code remain access limits, not local omissions disguised as absences.

## Limitations and checks

The source HEAD was rechecked as `f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe` and `git status --short` was empty. No source mutation, target execution, dependency installation or external evidence acquisition occurred. Method identity is the complete supplied job, member types, worker rules and record contract read for this attempt; no different method version or source identity was substituted. The worker identity records the Pi environment's model and reasoning level.

Public implementation supports concrete submission, selection, context replacement, exact reload and local failure behavior. It does not expose remote extraction/maintenance algorithms or demonstrate exercised memory use, truth, model compliance, performance, parameter updates or improved capacity. Available but uninspected adapter paths are explicitly retained in coverage. Review and automatic-forgetting semantics remain attributed design, not audited enforcement.

Deterministic validation: the required invocation-specific `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked.” This establishes content form and quotation occurrence, not job acceptance, analytical support or exercised behavior.
