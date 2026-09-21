---
{
  "type": "kb/types/agentic-system-analysis-result.md",
  "description": "Supermemory's public memory clients and documented external engine: context delivery is inspectable, inference quality and backend curation are not.",
  "run-id": "AAS-2026-09-21-supermemory-01",
  "system": "Supermemory",
  "run-date": "2026-09-21",
  "result-disposition": "complete",
  "target-class": "memory/knowledge/context-engineering system",
  "boundary-kind": "complete artifact, partial loop",
  "reviewed-boundary": "57b430b5b6a19106a989651f4cde853c05147682",
  "analysis-cutoff": "2026-09-21",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Publicly represented documents, conversation traces, extracted graph facts, profiles/buckets, virtual memory files and their access metadata/caches; MCP and SDK write/read routes plus committed remote-engine doctrine. Excludes proprietary implementation, model-provider internals, externally linked plugins and hosted-console implementation.",
    "axes": {
      "storage_substrate": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "OBJ-2",
          "OBJ-3",
          "OBJ-6",
          "OBJ-7"
        ],
        "note": "Service objects and an in-memory LRU are implemented interfaces; graph and vector stores are documented. Remote payload and access-structure storage is opaque, preventing a complete substrate set. Virtual files are remote documents, not inspected filesystem storage."
      },
      "representational_form": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "OBJ-2",
          "OBJ-3",
          "OBJ-4",
          "OBJ-5",
          "OBJ-7"
        ],
        "note": "Visible facts/profiles are natural language and access metadata is symbolic. Uploaded multimodal payloads and engine internals prevent a complete form set. Embedding claims do not establish learned model weights."
      },
      "lineage": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "authored",
          "imported",
          "other-compiled",
          "trace-extracted"
        ],
        "records": [
          "OBJ-2",
          "OBJ-3",
          "OBJ-4",
          "OBJ-5",
          "OBJ-7",
          "RTE-7",
          "RTE-8"
        ],
        "note": "Union across manually authored facts/files, imported source documents, compiled metadata/profiles, and documented extraction from automatically acquired traces. Covers the declared public memory objects and documented derivations, not hidden engine training."
      },
      "behavioral_authority": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "knowledge",
          "ranking",
          "routing"
        ],
        "records": [
          "OBJ-3",
          "OBJ-4",
          "OBJ-5",
          "RTE-1",
          "RTE-6",
          "RTE-9"
        ],
        "note": "Recalled content supplies context; inferred/latest/forgotten flags govern documented ranking/eligibility, and container/metadata selectors route access. System-message placement alone is not evidence of binding memory instructions."
      },
      "write_agency": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "automatic",
          "manual"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-9",
          "RTE-10",
          "RTE-11"
        ],
        "note": "Manual fact authoring/disposition and automatic trace acquisition/extraction are distinct. Human-triggered extraction remains automatic. Remote extraction is documented."
      },
      "curation_operations": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-8",
          "RTE-9",
          "RTE-10",
          "OBJ-4"
        ],
        "note": "Documented operations support evolve, invalidate, decay, synthesize, promote and profile consolidation; service-side operation completeness is opaque. Client formatting dedup does not establish dedup of durable memory."
      },
      "read_back_direction": {
        "assessment": "known",
        "basis": "wired",
        "values": [
          "pull",
          "push"
        ],
        "records": [
          "RTE-1",
          "RTE-5",
          "RTE-6",
          "RTE-10",
          "RTE-11",
          "RTE-12"
        ],
        "note": "MCP/tools and virtual-file reads fulfill host/model requests; installed SDK middleware automatically selects and supplies context before the model call. This classifies implemented client routes, without asserting deployed use or benefit."
      },
      "read_back_signal": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-6",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Automatic context supply uses container identity and profile/query modes. Semantic selection is documented; hybrid search, reranking, query rewriting and opaque profile selection prevent a complete normalized signal set."
      },
      "trace_learning": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "yes"
        ],
        "records": [
          "RTE-7",
          "RTE-8",
          "OBJ-3",
          "OBJ-4",
          "RTE-6",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Wired trace persistence plus documented durable fact/profile extraction and wired later context supply establish a claimed complete trace-learning chain. Raw transcript storage alone would not qualify."
      },
      "trace_source": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "session-logs",
          "tool-traces",
          "event-streams"
        ],
        "records": [
          "RTE-7",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Conversation history and optional tool calls/results feed the service; voice integrations acquire user-turn events/context frames. The classification concerns these inspected qualifying writeback routes, not arbitrary uploaded datasets."
      },
      "learning_scope": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Container identities may denote users or projects, while customId groups conversations. Task boundaries and the horizon of remote aggregation are not fixed by those identifiers; no complete task-horizon set follows."
      },
      "learning_timing": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "RTE-7",
          "RTE-8",
          "RTE-11",
          "RTE-12"
        ],
        "note": "Client acquisition runs before/after turns or on events; remote dynamic dreaming can outlive indexing and profile aggregation is periodic. The exact timing of every durable trace-derived transformation is not exposed, preventing a complete timing union."
      },
      "distilled_form": {
        "assessment": "known",
        "basis": "claimed",
        "values": [
          "natural-language"
        ],
        "records": [
          "OBJ-3",
          "OBJ-4",
          "RTE-8"
        ],
        "note": "Documented extracted facts and profile summaries consumed by the qualifying later routes are text. Structural metadata indexes those outputs; custom learning model is not evidence of per-user weight updates."
      },
      "faithfulness_tested": {
        "assessment": "not-determinable",
        "basis": null,
        "values": [],
        "records": [
          "CLM-4"
        ],
        "note": "No retained execution evidence of dependence on recalled content was established in the frozen public boundary. No dynamic probe was authorized; test source and benefit claims cannot decide an observed dependence result."
      }
    }
  }
}
---

# Supermemory agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-21-supermemory-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/supermemory.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-21-supermemory-01/memory-report.md`

**Memory analysis report SHA-256:** f92b526e333a4f13745ac33d9cda71998dc00da8bc689514f845bdd172684d38

## Boundary and evidence

Evidence basis: static source and committed documentation from SRC-1, inspected on 2026-09-21. Intended use: distinguish Supermemory's inspectable memory-delivery and acquisition mechanisms from its claims about the external engine. The complete public artifact participates in a larger loop: hosts own agent scheduling and model decisions, and a separately deployed service owns extraction, graph processing, ranking and durable content. This is a memory/knowledge/context-engineering system, not an enclosing agent runtime.

Included: public MCP server and account state, SDK memory integrations, documented graph processing and inferred-memory review, and shipped schemas. Excluded: separately hosted backend implementation, separately linked client plugins, external model internals, actual deployments, benchmark runs and separate self-hosted binaries. These exclusions prevent claims about service enforcement, model training, graph correctness, installed plugin behavior, runtime activation or measured benefit. Repository examples and tests are code or doctrine, not observed operation. The web app is currently a redirect to a separate console, not that console's implementation.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/supermemoryai/supermemory`; access root `/home/zby/llm/commonplace/related-systems/supermemoryai--supermemory` | `57b430b5b6a19106a989651f4cde853c05147682` | Implementation: MCP and SDK code, schemas. Doctrine/design: committed README and MDX contracts. No observed-run or causal evidence. | `apps/mcp/src/server/`, selected SDK integrations and validation schemas; graph, processing, review and hosting documentation | Full paths on the canonical records below, all at this revision | Backend/provider internals and actual execution are uninspected; worktree and current HEAD never supply evidence. |

## Shared records

### Components

CMP-1 — Supermemory MCP request server. Implementation conclusion status: wired. `apps/mcp/src/server/index.ts` authenticates a request and constructs a server whose registered tools call the external service. Symbolic TypeScript is shipped code, not acquired memory. Next-step ownership stays with the host agent; the MCP server returns tool results. Protocol state is stateless while separate application state persists. Source: SRC-1, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/server.ts`.

> const handler = createMcpHandler(
> 		() =>
> 			createSupermemoryServer(
> 				c.env,
> 				actor,
> 				(promise) => c.executionCtx.waitUntil(promise),
> 				mcpOrigin,
> 			),
> 		{
> 			route: "/mcp",
> 			legacy: "stateless",
> --- `apps/mcp/src/server/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

CMP-2 — External memory model, embedding pipeline and temporal vector-graph engine. Component existence and roles conclusion status: claimed; operational parameter changes conclusion status: uninspected; exact model-version pinning conclusion status: uninspected. The documentation names a custom learning model, but that name establishes neither online weight updates nor a fixed training regime. The public client addresses a configurable service URL rather than selecting an exact engine/model revision. Local-versus-Enterprise documentation describes different model provision; neither external implementation is inspected here. Source: SRC-1, `apps/docs/concepts/how-it-works.mdx`, `apps/docs/self-hosting/local-vs-enterprise.mdx`, `apps/mcp/src/server/client/index.ts`.

> At it's core, supermemory is powered by a custom learning model and a graph database that we built internally.
> --- `apps/docs/concepts/how-it-works.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

CMP-3 — Host language-model components reached through SDK wrappers. The wrapper receives a model/client supplied by its caller and changes invocation context, not a model training interface. Parameter-change conclusion status: uninspected for the external provider; identity-pinning conclusion status: uninspected beyond the caller's model selection. No exact solver version is fixed by this analysis. Source: SRC-1, `packages/tools/src/vercel/index.ts`, `packages/tools/src/openai/middleware.ts`, `packages/openai-sdk-python/src/supermemory_openai/middleware.py`; see the call-path quotes on RTE-6 and RTE-12. These support wrapper wiring without establishing model weights or deployed behavior.

### Operative objects

OBJ-1 — Active container-tag preference and upload capability state. Symbolic values in a Cloudflare Durable Object. The active tag persists across calls for an organization/user pair and changes default routing; upload state holds a token hash, bearer credential and expiry until consumed. These are access and routing state, not extracted user knowledge. Source: SRC-1, `apps/mcp/src/server/space.ts`, `apps/mcp/src/server/space-state.ts`. Implementation conclusion status: wired. See RTE-3 and RTE-4 for evidence and consumers.

#### OBJ-2
Object: source documents and raw conversation inputs. Represented as remote service objects; user text, imported files/URLs and role-labelled messages are inputs, not automatically derived memories. Structured conversations can contain images and optional tool-call arguments/results. Display summaries are separate from complete payloads; opaque multimodal data prevents a complete representational classification. Consumers are ingestion, source-chunk retrieval, document readers and graph extraction. Source provenance is documented, not independently verified.

Source: SRC-1 `apps/docs/concepts/how-it-works.mdx:77-86`.

> 
> - Conversation transcripts and messages
> - Text, markdown, HTML
> - PDFs, images, audio/video, code
> - URLs and connector items (Drive, Notion, Gmail, …)
> 
> You do not pre-chunk or pick an embedding model. See [Multi-modal ingestion](/concepts/content-types) for formats, and [Add context](/ingestion/add-memories) for the API.
> 
> Supermemory handles the ingestion and extraction for you. This also gives us a big advantage for quality - The engine extracts it in an optimized way with Contextual Chunking and other features for better quality search and memory generation.
> 
> --- `apps/docs/concepts/how-it-works.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/conversations-client.ts:9-19`.

> export interface ConversationMessage {
> 	role: "user" | "assistant" | "system" | "tool"
> 	content: string | ContentPart[]
> 	name?: string
> 	tool_calls?: ToolCall[]
> 	tool_call_id?: string
> }
> 
> export type ContentPart =
> 	| { type: "text"; text: string }
> 	| { type: "image_url"; imageUrl: { url: string } }
> --- `packages/tools/src/conversations-client.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### OBJ-3
Object: extracted and inferred graph memory entries. Remote durability and graph/vector storage are source claims. Natural-language facts have graph relations and status metadata, including current-version, inferred and forgotten state. Their consumer authority is contextual knowledge; service ranking/eligibility fields separately control selection. Source relationships provide provenance, but are not necessarily an explanation of why a behavioral prescription should hold. No inspected route requires retaining a reason with every derived fact.

Source: SRC-1 `apps/docs/concepts/graph-memory.mdx:65-69`.

> When content is processed, new facts connect to existing ones through three relationship types.
> 
> ### Updates — information changes
> 
> New fact **replaces** what was true before for search purposes; history can remain for audit.
> --- `apps/docs/concepts/graph-memory.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/concepts/graph-memory.mdx:93-93`.

The source example and its inference claim are retained on OBJ-3.

Source: SRC-1 `apps/docs/concepts/how-it-works.mdx:14-15`.

>   <Card title="Temporal Vector-graph engine">
>     Where the learnings are actually stored, optimized for search. Fact-based temporal graph that has Vector, FTS, and graph built in.
> --- `apps/docs/concepts/how-it-works.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### OBJ-4
Object: static/dynamic profile and topical buckets. These are derived natural-language context, not raw transcripts or parametric learning. Source documentation describes both a memory sample/summary and periodic aggregation of older memories. The latter is a distinct compaction-like form with later profile consumption. Buckets classify memories by topic; the classification labels are symbolic access metadata. Default TypeScript middleware explicitly requests static and dynamic sections, so bucket availability does not establish bucket delivery on that route. No required reason field or reason-reading behavior appears in its plain string formatter.

Source: SRC-1 `apps/docs/user-profiles/buckets.mdx:8-8`.

> Buckets are **custom topical categories** for a profile — an axis that sits alongside `static` and `dynamic`. Where static/dynamic split facts by how long-lived they are, buckets group them by subject (e.g. `preferences`, `goals`, `work`). As content is ingested, a classifier assigns each memory to the buckets it matches, so you can pull just the slice of context a given surface needs.
> --- `apps/docs/user-profiles/buckets.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/user-profiles/buckets.mdx:77-77`.

> **`[Recent]` and `[Summary]` labels.** To keep profiles dense, an entity's older memories are periodically aggregated into a short synthesis. Entries prefixed `[Summary]` are that aggregated context; entries prefixed `[Recent]` were ingested since the last aggregation and aren't summarized yet. The `dynamic` section uses the same `[Recent]` prefix (plus a `[YYYY-MM-DD]` date). Strip the prefixes if you only want raw text, or keep them to signal recency to your model.
> --- `apps/docs/user-profiles/buckets.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/shared/memory-client.ts:35-44`.

> 	const payload = queryText
> 		? JSON.stringify({
> 				q: queryText,
> 				containerTag: containerTag,
> 				include: ["static", "dynamic"],
> 			})
> 		: JSON.stringify({
> 				containerTag: containerTag,
> 				include: ["static", "dynamic"],
> 			})
> --- `packages/tools/src/shared/memory-client.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### OBJ-5
Object: container/document identity, provenance and disposition metadata. A container groups the subject of context; customId groups a document or conversation. User/project identity is an actual selector for automatic context supply. Document metadata filters and graph disposition flags can narrow eligible content. These symbolic fields route or rank information, rather than constituting the memory's factual content. Source-side hard-isolation claims are not a substitute for parent authentication analysis. CustomId is not a task-horizon assertion.

Source: SRC-1 `apps/docs/recall/user-profiles.mdx:132-132`.

> Profiles support the same [metadata filters](/concepts/filtering) as `/search` and `/documents/list` — `filters` narrows which memories are eligible to contribute to `static`, `dynamic`, and `buckets`, not just which search results come back.
> --- `apps/docs/recall/user-profiles.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/recall/memory-review.mdx:28-36`.

> | Action | Result | Effect on search |
> |--------|--------|------------------|
> | **Approve** | `isInference` cleared | Ranks like a stated fact — no longer down-weighted |
> | **Decline** | `isForgotten` set | Removed from search entirely — a rejected guess is forgotten |
> | **Undo** | back to unreviewed | Returns to the queue; inferred and down-weighted again |
> 
> A reviewed memory is stamped with `reviewStatus` in its metadata so it drops out of the
> review queue (declined memories also leave search, since they're forgotten). **Undo**
> clears that stamp — and un-forgets a declined memory — bringing it back.
> --- `apps/docs/recall/memory-review.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### OBJ-6
Object: SDK in-memory recall cache. The TypeScript LRU holds up to 100 retrieval strings by container/thread/mode/normalized-message key. It reduces repeated retrieval inside tool loops; it is not durable learning or consolidation. Eviction from this cache does not establish decay of service memory. Cached content is later supplied by the middleware, with the same knowledge authority as the uncached string.

Source: SRC-1 `packages/tools/src/shared/cache.ts:8-9`.

> export class MemoryCache<T = string> {
> 	private cache: LRUCache<string, T> = new LRUCache({ max: 100 })
> --- `packages/tools/src/shared/cache.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/shared/cache.ts:21-28`.

> 	static makeTurnKey(
> 		containerTag: string,
> 		threadId: string | undefined,
> 		mode: MemoryMode,
> 		message: string,
> 	): string {
> 		const normalizedMessage = message.trim().replace(/\s+/g, " ")
> 		return `${containerTag}:${threadId || ""}:${mode}:${normalizedMessage}`
> --- `packages/tools/src/shared/cache.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### OBJ-7
Object: Claude memory-file document. A path-shaped interface stores `fileText` in remote documents with `file_path`, `line_count` and author metadata. The complete content is read on demand and can be arbitrary authored text. It is not evidence of local file storage or of automatic trace extraction. A caller may write a rationale into that text, but the adapter does not require one or classify its force.

Source: SRC-1 `packages/tools/src/claude-memory.ts:389-399`.

> 			const _response = await this.client.add({
> 				content: fileText,
> 				customId: normalizedId,
> 				containerTags: this.containerTags,
> 				metadata: {
> 					claude_memory_type: "file",
> 					file_path: filePath,
> 					line_count: fileText.split("\n").length,
> 					created_by: "claude_memory_tool",
> 					last_modified: new Date().toISOString(),
> 				},
> --- `packages/tools/src/claude-memory.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`


#### OBJ-8

Extracted/stated fact content, an operative part of graph entries OBJ-3. Natural-language assertions acquired from source documents or authored through a direct-memory interface. The claimed source derivation differs from the inferred part OBJ-9; an explicit statement does not itself warrant its truth. Producer/consumer and storage remain those of OBJ-3, RTE-8 and RTE-9. Source: SRC-1, `apps/docs/recall/memory-review.mdx`, `apps/docs/recall/memory-operations.mdx`; the relevant excerpts are retained on CLM-3 and RTE-9. Transformation fidelity conclusion status: uninspected; specified derivation conclusion status: claimed.

#### OBJ-9

Inferred fact content, another operative part of graph entries OBJ-3. Natural-language guesses with `isInference` metadata (OBJ-5); source-native derives can propose what no source explicitly states. This is ampliative conjecture in the example, not guaranteed entailment. Consumer/retention are those of OBJ-3; the documented review path is RTE-9. Source: SRC-1, `apps/docs/concepts/graph-memory.mdx`, `apps/docs/recall/memory-review.mdx`; exact excerpts remain on OBJ-3, OBJ-5 and CLM-3. Derivation/review-effect conclusion status: claimed. No candidate instance was observed.

### Routes

RTE-1 — Requested MCP search. Implementation conclusion status: wired. The host's tool invocation supplies a query and optional space; the server resolves a default, calls hybrid service search (default limit ten), and returns text and structured memory results. The requester determines the next action. Delivery is wired; activation and benefit are uninspected. Query length has a 1,000-character schema maximum; this is not a total context-token guarantee. The client formats returned scores without independently checking source truth. API failure returns an error result; search itself does not revise retained knowledge. Source: SRC-1, `apps/mcp/src/server/tools/search-memory.ts`, `apps/mcp/src/server/client/index.ts`.

> const effectiveTag = await deps.resolveContainerTag(args.containerTag)
> 				const client = deps.getClient(effectiveTag)
> 
> 				const searchResult = await client.search(args.query)
> --- `apps/mcp/src/server/tools/search-memory.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

> const result = await this.client.search.memories({
> 				q: query,
> 				limit,
> 				...(containerTag ? { containerTag } : {}),
> 				searchMode: "hybrid",
> 				threshold,
> 			})
> --- `apps/mcp/src/server/client/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

RTE-2 — MCP authentication and request admission. Implementation conclusion status: wired. Missing/invalid credentials reject the request; JWT verification checks issuer/audience and required user/organization claims. Opaque API keys use the session endpoint and a per-isolate 60-second successful-result cache. A transient backend failure gives 503 with retry guidance rather than an invalid-token result. This is operational admission, not acceptance of memory claims. No proposal, theory revision or answer oracle applies. Owner: MCP request handler; enforcement point: before server construction; strength: protocol conditional on JWT library, session service and deployment. Backend data authorization remains an external contract; direct SDK calls use their own API credentials and do not pass this MCP guard. Source: SRC-1, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/auth/index.ts`.

> const API_KEY_CACHE_TTL_MS = 60_000
> --- `apps/mcp/src/server/auth/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

> const cached = apiKeyCache.get(token)
> 	if (cached && cached.expiresAt > Date.now()) return cached.user
> --- `apps/mcp/src/server/auth/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

> const { payload } = await jwtVerify(token, verifier, {
> 			issuer,
> 			audience,
> 		})
> --- `apps/mcp/src/server/auth/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

RTE-3 — Active-space revision and selection. Implementation conclusion status: wired. An app-only tool proposes a tag, checks it against service-listed accessible tags, and persists it; absent membership rejects the change. Subsequent default selection reads OBJ-1, while an explicit tag overrides one call. Human UI selection is the intended trigger; host visibility metadata is an interface control, not proof of universal isolation. The retained tag is an identifier, not a theory or model parameter. No content truth check applies; restoring an earlier selection requires another selection. State ownership is organization/user, not a conversation or OAuth client. Source: SRC-1, `apps/mcp/src/server/space.ts`, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/tools/set-active-tag.ts`.

> return `space:${JSON.stringify([actor.organizationId, actor.userId])}`
> --- `apps/mcp/src/server/space.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

> return explicit ?? (await getActiveContainerTag())
> --- `apps/mcp/src/server/space.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

> if (!tags.some((tag) => tag.containerTag === containerTag)) {
> 					return deps.errorResult(
> 						new Error(`No access to container tag '${containerTag}'.`),
> 					)
> 				}
> 				await deps.setActiveContainerTag(containerTag)
> --- `apps/mcp/src/server/tools/set-active-tag.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

RTE-4 — Direct upload capability. Implementation conclusion status: wired. A prepared upload session expires after two minutes. The upload endpoint validates request shape and atomically consumes the token-backed session before forwarding its body using the stored bearer credential. An invalid or expired session rejects upload. The token is single-use even if the subsequent service transfer fails; creating a new session is required to retry. This is acquisition transport and credential admission, not source-content validation. It cannot establish server-side parser safety, graph admission or rollback. Source: SRC-1, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/space-state.ts`.

> if (session.tokenHash !== tokenHash) return undefined
> 
> 			await transaction.delete(UPLOAD_SESSION_KEY)
> 			return {
> 				bearerToken: session.bearerToken,
> 				expiresAt: session.expiresAt,
> 			}
> --- `apps/mcp/src/server/space-state.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-5
Route: requested MCP profile/resource/prompt and document browsing. A host requests the registered resource or prompt; the server retrieves the selected space's profile and returns it. Resource delivery allows 12 facts per section, while the context prompt allows 8 facts per section and 3 recent spaces. These are item-count limits, not token budgets or model salience guarantees. The prompt returns a user-role message. This route is wired pull; an external host could automate requesting it, but no such host selector was established here. Separate document-list/get operations expose summaries and available full content by requested ID; they do not imply profile injection.

Source: SRC-1 `apps/mcp/src/server/resources/profile.ts:10-10`.

> const PROFILE_FACT_LIMIT = 12
> --- `apps/mcp/src/server/resources/profile.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/mcp/src/server/prompts/context.ts:12-13`.

> const CONTEXT_FACT_LIMIT = 8
> const RECENT_SPACE_LIMIT = 3
> --- `apps/mcp/src/server/prompts/context.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/mcp/src/server/prompts/context.ts:27-32`.

> 				const selectedTag = await resolveContainerTag()
> 				const activeKey = selectedTag ?? DEFAULT_PROJECT_ID
> 				const [profileResult, spaces] = await Promise.all([
> 					getClient(activeKey).getProfile(),
> 					getClient().listContainerTags(),
> 				])
> --- `apps/mcp/src/server/prompts/context.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/mcp/src/server/prompts/context.ts:89-96`.

> 				return {
> 					messages: [
> 						{
> 							role: "user" as const,
> 							content: {
> 								type: "text" as const,
> 								text: parts.join("\n"),
> 							},
> --- `apps/mcp/src/server/prompts/context.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-6
Route: TypeScript Vercel automatic context supply. Trigger: wrapped model generation/streaming. Selector: configured container plus profile/query/full mode, current user message for query/full, and per-turn cache key. Selected parts: static/dynamic profile, query results, or both, deduplicated for the current prompt. Delivery: SDK-owned memory block in model parameters, before `doGenerate`/`doStream`. This is wired push relative to the language model: it did not request a memory tool. The wrapper's own service request is the transport step, not another consumer-direction classification. A fixed retrieval-time allowance and fail-open option constrain latency; no inspected complete token budget constrains returned context. Engine selection remains opaque.

Source: SRC-1 `packages/tools/src/vercel/index.ts:154-159`.

> 			if (prop === "doGenerate") {
> 				return async (params: LanguageModelCallOptions) => {
> 					let modelParams: LanguageModelCallOptions = params
> 					try {
> 						modelParams = await transformParamsWithMemory(params, ctx)
> 					} catch (memoryError) {
> --- `packages/tools/src/vercel/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/vercel/index.ts:182-184`.

> 					try {
> 						// biome-ignore lint/suspicious/noExplicitAny: Union type compatibility between V2 and V3
> 						const result = await target.doGenerate(modelParams as any)
> --- `packages/tools/src/vercel/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/vercel/middleware.ts:364-373`.

> 		memories = await buildMemoriesText({
> 			containerTag: ctx.containerTag,
> 			queryText,
> 			mode: ctx.mode,
> 			baseUrl: ctx.normalizedBaseUrl,
> 			apiKey: ctx.apiKey,
> 			logger: ctx.logger,
> 			promptTemplate: ctx.promptTemplate,
> 			...(fetchSignal ? { signal: fetchSignal } : {}),
> 		})
> --- `packages/tools/src/vercel/middleware.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/shared/memory-client.ts:150-164`.

> 	const userMemories =
> 		mode !== "query"
> 			? convertProfileToMarkdown({
> 					profile: {
> 						static: deduplicated.static,
> 						dynamic: deduplicated.dynamic,
> 					},
> 					searchResults: { results: [] },
> 				})
> 			: ""
> 	const generalSearchMemories =
> 		mode !== "profile" && deduplicated.searchResults.length > 0
> 			? `Search results for user's recent message: \n${deduplicated.searchResults
> 					.map((memory) => `- ${memory}`)
> 					.join("\n")}`
> --- `packages/tools/src/shared/memory-client.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-7
Route: TypeScript Vercel conversation writeback. Trigger: completed response with persistable user content and `addMemory: always` (the default). Producer serializes original messages plus assistant text, optionally preserving tool calls/results; it submits them to the conversations endpoint under a stable customId/container. Failure is logged, so delivery of a generated reply does not guarantee persistence. Remote extraction into OBJ-3 and OBJ-4 followed by RTE-6 closes the documented trace-learning chain. The entire chain's weakest basis is claimed because the transformation and durable service state are external. Reasons contained in raw traces are not guaranteed to survive extraction or default recall.

Source: SRC-1 `packages/tools/src/vercel/index.ts:186-203`.

> 						if (
> 							ctx.addMemory === "always" &&
> 							hasPersistableUserContent(params)
> 						) {
> 							const assistantResponseText = extractAssistantResponseText(
> 								result.content as unknown[],
> 							)
> 							saveMemoryAfterResponse(
> 								ctx.client,
> 								ctx.containerTag,
> 								ctx.customId,
> 								assistantResponseText,
> 								params,
> 								ctx.logger,
> 								ctx.apiKey,
> 								ctx.normalizedBaseUrl,
> 								ctx.includeToolCalls,
> 							)
> --- `packages/tools/src/vercel/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/vercel/middleware.ts:169-175`.

> 		const response = await addConversation({
> 			conversationId: customId,
> 			messages: conversationMessages,
> 			containerTags: [containerTag],
> 			apiKey,
> 			baseUrl,
> 		})
> --- `packages/tools/src/vercel/middleware.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/vercel/middleware.ts:217-222`.

> 	/**
> 	 * Persist assistant tool calls and tool results as part of the saved
> 	 * conversation. Off by default: tool payloads are often large and
> 	 * low-signal, and would pollute memory extraction.
> 	 */
> 	includeToolCalls?: boolean
> --- `packages/tools/src/vercel/middleware.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-8
Route: remote dreaming, graph maintenance and profile aggregation. Trigger: ingestion/indexing plus documented dynamic grouping or instant per-document processing, followed by periodic older-memory aggregation. Producer is the external memory model; inputs are OBJ-2 and existing OBJ-3; retained outputs are extracted/updated/inferred facts and summaries in OBJ-4. Later consumers are RTE-1 and the profile/query SDK routes. Conclusion status: claimed. This is not an inspected training implementation or evidence of user-specific model-weight learning. No complete schedule, rejection algorithm, retention guarantee or reason-preservation guarantee is exposed. A source relationship can support inspection without being a retained causal rationale.

Source: SRC-1 `apps/docs/concepts/how-it-works.mdx:122-125`.

> | Mode | Default? | Behavior | When to use |
> | --- | --- | --- | --- |
> | **`dynamic`** | Yes | Related documents are grouped so memories form from **coherent units**, not one isolated write at a time. Graph quality is higher for real multi-turn / multi-doc flows. Memory extraction may continue **after** `status: "done"`. | Production agents, connectors, ongoing sessions |
> | **`instant`** | No | This document is dreamed **on its own, right away**. Memories are available as soon as processing finishes for that doc. Bills **one extra [operation](/overview/billing)** per document. | Demos, quickstarts, “I need the graph now” |
> --- `apps/docs/concepts/how-it-works.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/concepts/graph-memory.mdx:127-142`.

> 
> ## Memory types
> 
> | Type | Example | Behavior |
> | --- | --- | --- |
> | **Facts** | “Alex is a PM at Stripe” | Persists until updated |
> | **Preferences** | “Alex prefers morning meetings” | Strengthens with repetition |
> | **Episodes** | “Met Alex for coffee Tuesday” | Decays unless significant |
> 
> ## Automatic forgetting
> 
> - **Time-based** — temporary facts drop after they expire (“exam tomorrow”, “meeting at 3pm today”).
> - **Contradiction** — updates win for “what’s true now.”
> - **Noise filtering** — casual, non-meaningful chatter is less likely to become durable memory.
> 
> For explicit product controls (forget, review low-confidence derives), see [Forget & update](/recall/memory-operations) and [Memory review](/recall/memory-review).
> --- `apps/docs/concepts/graph-memory.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-9
Route: human/model acquisition, maintenance and withdrawal. MCP add saves submitted content through `client.add`; its name does not imply direct insertion of one final graph fact. Forget tries exact content first; after 404 it searches with threshold 0.85 and selects an extracted memory rather than a chunk. Separately, committed v4 documentation affords manually authored final facts, versioned update and soft deletion; inferred-memory review affords approval, decline and undo by a human-facing application. The server-side effect of review is claimed, not independently validated. `apps/web` contains a forwarding shell rather than an inspected editing console. Active-space routing and parent permissions determine which host requests are accepted.

Source: SRC-1 `apps/mcp/src/server/client/index.ts:159-170`.

> 	async createMemory(
> 		content: string,
> 	): Promise<{ id: string; status: string; containerTag: string }> {
> 		try {
> 			const result = await this.client.add({
> 				content,
> 				containerTag: this.containerTag,
> 				metadata: { sm_source: MCP_SOURCE },
> 			})
> 			return {
> 				id: result.id,
> 				status: "queued",
> --- `apps/mcp/src/server/client/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/mcp/src/server/client/index.ts:192-203`.

> 			} catch (error: unknown) {
> 				const status = objectProperty(error, "status")
> 				if (status !== 404) throw error
> 			}
> 
> 			const SIMILARITY_THRESHOLD = 0.85
> 			const searchResult = await this.search(
> 				content,
> 				5,
> 				SIMILARITY_THRESHOLD,
> 				this.containerTag,
> 			)
> --- `apps/mcp/src/server/client/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/mcp/src/server/client/index.ts:213-225`.

> 			const memoryToDelete = searchResult.results.find((r) => "memory" in r)
> 			if (!memoryToDelete) {
> 				return {
> 					success: false,
> 					message: "No matching memory found (only chunks matched).",
> 					containerTag: this.containerTag,
> 				}
> 			}
> 
> 			await this.client.memories.forget({
> 				id: memoryToDelete.id,
> 				containerTag: this.containerTag,
> 			})
> --- `apps/mcp/src/server/client/index.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/recall/memory-operations.mdx:16-20`.

> 
> Create memories directly without going through the document ingestion workflow. Memories are embedded and immediately searchable.
> 
> This is useful for storing user preferences, traits, or any structured facts where you already know the exact memory content.
> 
> --- `apps/docs/recall/memory-operations.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/recall/memory-operations.mdx:124-124`.

> Soft-delete a single memory — excluded from search results but preserved in the database. Identify it by `id` or by exact `content`, scoped to its `containerTag`.
> --- `apps/docs/recall/memory-operations.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/web/README.md:1-5`.

> # @repo/web
> 
> Serves `app.supermemory.ai`. Every request is forwarded to the console: plugin and OAuth paths get an immediate redirect with the query string intact, and everything else shows a short notice before moving on.
> 
> Set `NEXT_PUBLIC_CONSOLE_URL` to point at a different console origin during local development.
> --- `apps/web/README.md` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `apps/docs/recall/memory-operations.mdx:293-293`.

> Update a memory by creating a new version. The original is preserved with `isLatest=false`.
> --- `apps/docs/recall/memory-operations.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-10
Route: Claude virtual-memory authoring and requested readback. Claude's memory-tool command adapter supports view/create/string replacement/insert/delete/rename, with path validation and scoped exact document lookup. The host/model supplies commands and file text; a later view returns complete stored text or a requested line range, with displayed line numbers. Read/write wiring is implemented; semantic content and a trace-to-file derivation are caller-dependent. String replacement evolves a retained entry by writing changed content under the same normalized identity. A file-looking path does not change the remote substrate. Reasons are retained and read only if the caller puts them in the file and asks for a range containing them; no automatic guarantee follows.

Source: SRC-1 `packages/tools/src/claude-memory.ts:322-334`.

> 			// Resolve the exact document inside the configured scope so reads and
> 			// mutations use the complete stored file, not one ranked search chunk.
> 			const readResult = await this.getFileDocument(filePath)
> 			if (!readResult.success || !readResult.document) {
> 				return {
> 					success: false,
> 					error: readResult.error || `File not found: ${filePath}`,
> 				}
> 			}
> 
> 			const document = readResult.document
> 
> 			let content = document.content
> --- `packages/tools/src/claude-memory.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/claude-memory.ts:445-452`.

> 			const newContent = originalContent.replace(oldStr, () => newStr)
> 
> 			// Update the document
> 			const normalizedId = this.normalizePathToCustomId(filePath)
> 			const _updateResponse = await this.client.add({
> 				content: newContent,
> 				customId: normalizedId,
> 				containerTags: this.containerTags,
> --- `packages/tools/src/claude-memory.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-11
Route family: voice/event integrations. Pipecat triggers on LLM context frames: it snapshots real messages, obtains the latest user occurrence, clears prior injected recall, retrieves profile/query context, enhances the frame for downstream LLM consumption, and queues original messages for storage. Cleanup drains pending storage. Cartesia triggers on UserTurnEnded, obtains memory context, queues new history/current user messages, and passes context to its wrapped agent. These are wired automatic event-fed acquisition and push supply; memory derivation remains RTE-8's claimed remote operation. Both use profile/query text and search-result caps (ten by default), but item caps are not complete context token budgets. A conversation ID supplies no per-task horizon.

Source: SRC-1 `packages/pipecat-sdk-python/src/supermemory_pipecat/service.py:458-463`.

>                 context_messages = context.get_messages()
>                 # Snapshot the real conversation before adding memory context.
>                 # Injected <user_memories> messages must never be persisted or
>                 # included in the sent-message cursor.
>                 storable_messages = _snapshot_storable_messages(context_messages)
>                 latest_user_message, user_prefix = _latest_user_occurrence(storable_messages)
> --- `packages/pipecat-sdk-python/src/supermemory_pipecat/service.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/pipecat-sdk-python/src/supermemory_pipecat/service.py:473-486`.

>                     self._clear_injected_memories(context)
>                     try:
>                         memories_data = await self._retrieve_memories(latest_user_message)
>                         self._enhance_context_with_memories(
>                             context, latest_user_message, memories_data
>                         )
>                         # Mark only successful recalls (including empty ones).
>                         # Failures stay retryable on the next repeated frame.
>                         self._last_query = latest_user_message
>                         self._last_recalled_user_prefix = user_prefix
>                     except MemoryRetrievalError as e:
>                         logger.warning(f"Memory retrieval failed: {e}")
> 
>                 self._queue_context_for_storage(storable_messages)
> --- `packages/pipecat-sdk-python/src/supermemory_pipecat/service.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/cartesia-sdk-python/src/supermemory_cartesia/agent.py:480-493`.

>         try:
>             if type(event).__name__ == "UserTurnEnded":
>                 logger.info("[Supermemory] Processing UserTurnEnded event")
>                 event, memory_context = await self._enrich_event_with_memories(event)
> 
>                 # Store conversation in background
>                 if hasattr(event, 'history') and event.history:
>                     new_messages = self._new_history_messages(event.history)
>                     if new_messages:
>                         logger.info(
>                             f"[Supermemory] Queuing {len(new_messages)} messages for storage"
>                         )
>                         task = asyncio.create_task(self._store_messages(new_messages))
>                         self._background_tasks.add(task)
> --- `packages/cartesia-sdk-python/src/supermemory_cartesia/agent.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/cartesia-sdk-python/src/supermemory_cartesia/agent.py:509-510`.

>                 async for output in self._process_agent(env, event, memory_context):
>                     yield output
> --- `packages/cartesia-sdk-python/src/supermemory_cartesia/agent.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### RTE-12
Route family: other inspected SDK alternatives. OpenAI TypeScript middleware supports Responses instructions as the supply channel; it can persist incoming conversation history and retrieve context concurrently before the model call. OpenAI Python asynchronously queues incoming history (or just the latest user message without customId), injects system context, then calls the client. Neither should be described as always saving the newly generated assistant answer. Microsoft Agent Framework's context provider uses `extend_instructions` or a system message before a run and optionally saves conversation text after a run. Mastra input/output processors retrieve cached or remote context and save output conversation messages. VoltAgent uses onPrepareMessages/onEnd hooks; its advanced branch allows hybrid documents/memories, threshold/limit, rerank, rewrite and filters. Those alternatives establish additional push and writeback wiring while sharing RTE-8's remote derivation limit. Default prompt formatting yields readable facts, not mandatory derivation rationales. Synchronous/streaming/version-specific overloads are not exhaustively audited.

Source: SRC-1 `packages/tools/src/openai/middleware.ts:938-948`.

> 		if (shouldPersist) operations.push(persistResponsesInput())
> 
> 		const queryText = mode !== "profile" ? input : ""
> 		operations.push(
> 			searchAndFormatMemories(
> 				queryText,
> 				containerTag,
> 				logger,
> 				mode,
> 				"responses",
> 			),
> --- `packages/tools/src/openai/middleware.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/openai/middleware.ts:973-980`.

> 		return {
> 			request: originalResponsesCreate.call(
> 				openaiClient.responses,
> 				{
> 					...params,
> 					input: cleanedInput,
> 					instructions: enhancedInstructions,
> 				},
> --- `packages/tools/src/openai/middleware.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/openai-sdk-python/src/supermemory_openai/middleware.py:497-508`.

>         if self._options.add_memory == "always":
>             user_message = get_last_user_message(messages)
>             if user_message and user_message.strip():
>                 content = (
>                     get_conversation_content(messages)
>                     if self._options.custom_id
>                     else user_message
>                 )
>                 custom_id = (
>                     f"conversation:{self._options.custom_id}"
>                     if self._options.custom_id
>                     else None
> --- `packages/openai-sdk-python/src/supermemory_openai/middleware.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/openai-sdk-python/src/supermemory_openai/middleware.py:571-581`.

>         enhanced_messages = await add_system_prompt(
>             messages,
>             self._container_tag,
>             self._logger,
>             self._options.mode,
>             self._api_key,
>             self._base_url,
>         )
> 
>         kwargs["messages"] = enhanced_messages
>         return await original_create(**kwargs)
> --- `packages/openai-sdk-python/src/supermemory_openai/middleware.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py:152-160`.

>         # Use extend_instructions to add memory context
>         if hasattr(context, "extend_instructions"):
>             context.extend_instructions(self.source_id, full_text)
>         elif hasattr(context, "extend_messages"):
>             # Fallback: add as a system message
>             context.extend_messages(
>                 self.source_id,
>                 [Message("system", [full_text])],
>             )
> --- `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py:188-194`.

>             add_params: dict[str, Any] = {
>                 "content": conversation_text,
>                 "container_tag": self._container_tag,
>                 "custom_id": self._connection.custom_id,
>             }
> 
>             await self._client.add(**add_params)
> --- `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/mastra/processor.ts:192-194`.

> 			if (memories) {
> 				this.ctx.memoryCache.set(turnKey, memories)
> 				messageList.addSystem(wrapMemoryContext(memories), "supermemory")
> --- `packages/tools/src/mastra/processor.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/mastra/processor.ts:266-272`.

> 			const response = await addConversation({
> 				conversationId: effectiveCustomId,
> 				messages: conversationMessages,
> 				containerTags: [this.ctx.containerTag],
> 				apiKey: this.ctx.apiKey,
> 				baseUrl: this.ctx.baseUrl,
> 			})
> --- `packages/tools/src/mastra/processor.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/voltagent/hooks.ts:95-99`.

> 				const enhancedMessages = await enhanceMessagesWithMemories(
> 					inputMessages,
> 					ctx,
> 					preparedMessages,
> 				)
> --- `packages/tools/src/voltagent/hooks.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/voltagent/hooks.ts:144-144`.

> 				await saveConversation(messages, ctx)
> --- `packages/tools/src/voltagent/hooks.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/voltagent/middleware.ts:297-312`.

> 			const searchParams: Supermemory.SearchParams = {
> 				q: queryText,
> 				containerTag: ctx.containerTag,
> 			}
> 
> 			if (ctx.threshold !== undefined) searchParams.threshold = ctx.threshold
> 			if (ctx.limit !== undefined) searchParams.limit = ctx.limit
> 			if (ctx.rerank !== undefined) searchParams.rerank = ctx.rerank
> 			if (ctx.rewriteQuery !== undefined)
> 				searchParams.rewriteQuery = ctx.rewriteQuery
> 			if (ctx.filters !== undefined) searchParams.filters = ctx.filters
> 			if (ctx.include !== undefined) searchParams.include = ctx.include
> 			if (ctx.searchMode !== undefined) searchParams.searchMode = ctx.searchMode
> 
> 			const [response, profileResponse] = await Promise.all([
> 				ctx.client.search(searchParams),
> --- `packages/tools/src/voltagent/middleware.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`


### Claims

CLM-1 — The advertised engine extracts facts, handles temporal changes and contradictions, derives unstated facts and updates profiles. Claim conclusion status: claimed. The graph-memory and pipeline documentation explain the intended mechanism; client schemas and calls do not establish its implementation. RTE-1 establishes access to service results, not their correctness. Source: SRC-1, `README.md`, `apps/docs/concepts/graph-memory.mdx`, `apps/docs/concepts/how-it-works.mdx`.

The source example and its inference claim are retained on OBJ-3.

CLM-2 — The README advertises benchmark leadership and recall/context-reduction figures. Claim conclusion status: claimed. No benchmark runs, causal comparisons or matching deployment configuration were captured in SRC-1's inspected boundary; these are not measurements established by this analysis. Source: SRC-1, `README.md`.

> <strong>95% Recall@15 with a 99.4% context reduction · ~50ms user profiles.</strong><br/>
> --- `README.md` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### CLM-3
Claim: provenance and fallibility are represented but need not reach every model-facing prompt. Inference flags, relationships and review state exist in the documented graph; human approval changes ranking, not truth. Default profile conversion emits only strings grouped as Static Profile and Dynamic Profile. This narrows what a consumer can diagnose from that channel alone. A custom prompt template receives metadata-preserving search results, so loss is not universal. Implementation conclusion status for the formatter: wired. Engine fallibility/review conclusion status: claimed.

Source: SRC-1 `apps/docs/recall/memory-review.mdx:8-15`.

> Supermemory's graph automatically **derives** new facts from patterns across your
> existing memories (see [Graph Memory](/concepts/graph-memory)). These derived facts
> are guesses — the engine wasn't told them directly — so they are flagged as
> **inferred** (`isInference: true`) and **down-weighted in search** until confirmed.
> 
> These two endpoints let you build a review experience on top of that queue: list the
> inferred memories awaiting review, then **approve**, **decline**, or **undo** a
> decision on each one.
> --- `apps/docs/recall/memory-review.mdx` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/shared/prompt-builder.ts:24-31`.

> 	if (data.profile.static && data.profile.static.length > 0) {
> 		sections.push("## Static Profile")
> 		sections.push(data.profile.static.map((item) => `- ${item}`).join("\n"))
> 	}
> 
> 	if (data.profile.dynamic && data.profile.dynamic.length > 0) {
> 		sections.push("## Dynamic Profile")
> 		sections.push(data.profile.dynamic.map((item) => `- ${item}`).join("\n"))
> --- `packages/tools/src/shared/prompt-builder.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/shared/memory-client.ts:179-183`.

> 	const promptData: MemoryPromptData = {
> 		userMemories,
> 		generalSearchMemories,
> 		searchResults: deduplicatedSearchResults,
> 	}
> --- `packages/tools/src/shared/memory-client.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### CLM-4
Claim: client delivery is established more strongly than activation, faithfulness or benefit. The inspected wrappers pass modified parameters to model consumers; they do not show whether the model used the memory or whether use improved an outcome. Source tests were not executed and no retained dependence experiment was established. Boundary: this pinned repository and inspected memory routes. This prevents `faithfulness_tested: yes`; it does not establish that no external evaluation exists. Conclusion status: uninspected for operation-level causal dependence.


### Evidenced absences

None asserted. Inaccessible backend behavior and unexecuted integrations are limitations, not evidence that mechanisms do not exist.



### Behavioral-authority paths

BAP-1 — Host model receives shipped MCP server instructions and tool descriptions through protocol metadata. Force: instructions/advice for tool choice; horizon: the host's handling of server metadata. This is static supplied procedure, not memory read-back or demonstrated activation. Source: SRC-1, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/tools/search-memory.ts`; implementation conclusion status: wired. The local wrapper exposes metadata, while actual host enforcement is uninspected.

BAP-2 — Active tag OBJ-1 reaches server space resolution and chooses the default container for later space-aware operations. Force: routing; horizon: until changed or explicitly overridden. RTE-3 provides the exact implementation. This is an operative identifier, not factual warrant. `get_document` can read by ID from any accessible space, so default selection must not be mistaken for a universal authorization boundary. Source: SRC-1, `apps/mcp/src/server/tools/get-document.ts`.

> "Read one stored document by ID from any space you can access, including its summary and available content. Use list_documents to discover document IDs.",
> --- `apps/mcp/src/server/tools/get-document.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

#### BAP-3
Behavior-affecting pattern: SDK memory blocks are replaced and delimiters escaped to preserve caller instructions and avoid accidental re-ingestion of previously supplied context. This is implemented string handling, not semantic prompt-injection immunity. Knowledge delivered in a system/instructions channel does not by itself acquire a proven enforcement role. Pipecat additionally snapshots original conversation before augmentation, as quoted on RTE-11.

Source: SRC-1 `packages/tools/src/shared/memory-context.ts:10-14`.

> /** Prevent retrieved text from terminating or nesting the SDK-owned block. */
> function escapeMemoryContextDelimiters(memories: string): string {
> 	return memories.replace(SUPERMEMORY_TAG_PATTERN, (tag) =>
> 		tag.replace("<", "&lt;").replace(">", "&gt;"),
> 	)
> --- `packages/tools/src/shared/memory-context.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`

Source: SRC-1 `packages/tools/src/shared/memory-context.ts:30-40`.

> /** Replace prior middleware context while preserving caller-authored instructions. */
> export function replaceMemoryContext(
> 	content: string,
> 	memories: string,
> ): string {
> 	const preserved = stripMemoryContext(content)
> 	const memoryContext = wrapMemoryContext(memories)
> 	if (!memoryContext) return preserved
> 	// The newline belongs to the SDK-owned block and is removed with it, so caller
> 	// whitespace round-trips while Markdown/XML boundaries remain valid.
> 	return preserved ? `${preserved}\n${memoryContext}` : memoryContext
> --- `packages/tools/src/shared/memory-context.ts` @ `57b430b5b6a19106a989651f4cde853c05147682`


BAP-4 — Recalled facts, profiles and files reach the requesting host/model through tool/resource/user-prompt returns (RTE-1, RTE-5, RTE-10) or the wrapped model's system/instructions parameters (RTE-6, RTE-11, RTE-12). Force: contextual knowledge, not proven obedience or truth; horizon: that invocation unless the host retains it further. Default formatting may omit provenance/disposition metadata (CLM-3), and actual reliance is uninspected (CLM-4). Delivery implementation conclusion status: wired. Supporting code is retained on those routes.

BAP-5 — Inference/latest/forgotten flags and review state in OBJ-5 reach the remote selection service, changing ranking or eligibility before later model delivery. Force: ranking/selection; horizon: until updated, expired, forgotten or reversed. Source: SRC-1, `apps/docs/recall/memory-review.mdx`, `apps/docs/concepts/graph-memory.mdx`, retained on OBJ-5 and RTE-8. Conclusion status: claimed; service enforcement and effects in operation are uninspected. Approval changes operational reliance without independent epistemic warrant.

## Runtime account

The ordinary MCP route is a host-requested returning computation: bearer authentication (RTE-2), per-request server creation (CMP-1), explicit/default space selection (RTE-3), service request (RTE-1 or a write route), and formatted return. The host owns tool selection, model calls, continuation, approval UI and termination of the enclosing task. The service owns memory content persistence and interpretation. MCP owns only its request processing and separately durable account/upload state. There is no basis here for attributing a whole-agent scheduler or host sandbox to Supermemory.

Alternate routes matter: SDK integrations can inject context and capture conversations without MCP; requested resources/prompts expose profiles; document-by-ID reads need not use the active space; app-only tools expose human selection and upload controls; the web frontend forwards users to an external console. MCP authentication, hints and space defaults do not cover every alternate route. Service-side authorization remains required even when a client validates a tag or supplies a read-only/destructive hint. The declared local binary uses the same API but is not present as inspected implementation.

Four static forcing cases bound the account:

1. **Cached API-key acceptance:** repeated requests can reuse an accepted API-key identity for 60 seconds, while OAuth takes the JWT verifier path. Request authentication must not be described as a fresh remote permission lookup on every call (RTE-2).
2. **Another client changes the active space:** organization/user identity determines shared state; an explicit per-call tag bypasses that default. A space default is neither conversation isolation nor an absolute data-access boundary (RTE-3, BAP-2).
3. **Save returns before graph readiness:** MCP reports a queued service result as saved; the pipeline docs distinguish document indexing from later dynamic dreaming. A successful write response does not establish that facts are already available for recall (CLM-1 and the integrated write route).
4. **Upload transfer fails after token consumption:** the upload capability is already deleted; transport retry cannot safely assume the token remains reusable (RTE-4).

No dynamic check planned. Considered live authenticated MCP save/search, graph-review transitions, SDK model calls and existing integration tests. Static inspection suffices to establish the implemented client paths; live checks would require external credentials/services and could still not inspect backend semantics. None was run, and no failed or absent system behavior is inferred from that decision.

Operating mode: open user and application requests. Clients and host models propose writes; protocol/schema checks and remote service responses govern admission; hosts/humans may decide when to invoke or confirm a tool. The automatic derivation and update decisions belong to the external engine and remain claim-level. Human approve/decline/undo is documented as a review control, without a prescribed truth criterion or independent answer oracle. No bounded experimental curriculum or outcome-driven revision of this repository's own machinery was inspected. Source control, package configuration and endpoint selection remain operator responsibilities, outside the memory loop. A custom learning-model label supplies no evidence of operating-time parameter updates.

Revision admission is route-specific. RTE-7, RTE-11 and RTE-12 retain submitted traces; their public producer uses configured code and caller/model outputs, not an inspected learned theory for proposing system changes. RTE-8 names an external model as the proposer of fact/graph/profile changes, but the guidance it uses, its rejection policy and parameter changes are uninspected. RTE-9 offers deliberate authoring and human/model withdrawal; review approval/decline can veto or reverse reliance according to doctrine. RTE-10 permits caller-authored file changes with structural checks; its payload could contain a theory, but no instance or outcome-driven repair is established. For these routes, acceptance of an API request is not a measured candidate comparison. No independent answer oracle was evidenced. Source rules and parser validation govern execution; retained derivation reasons, diagnosis against them and later corrected use remain separate unknown links. RTE-3 changes a routing identifier and RTE-4 consumes an upload capability, so theory classification is inapplicable to those state changes.

## Lens scoping

### Memory/context scope

Full depth: SRC-1 exposes persistent documents, extracted memory, profiles, explicit retrieval, automatic SDK context injection and conversation writeback. Scoped objects and routes are those in the integrated specialist records, plus default-selection metadata OBJ-1 and RTE-3 where material. Static server instructions and transient authentication/upload state do not become learned memory merely because they affect calls. Backend implementation and separately linked plugins remain excluded; committed backend contracts are claim-level evidence.

### Epistemic scope

Full depth: CLM-1 includes derived facts and truth-maintenance language. SRC-1's graph/pipeline/review documentation, client schemas, source-inspection tools and write/read routes warrant analysis of acquisition, inference, human disposition and later reliance. Runtime controls RTE-2 and RTE-3 govern access, not factual truth. No observed candidates or execution traces were captured. The engine's actual evidence-consumption policy, extraction fidelity and causal benefits remain uninspected.

## Lens outputs

### Memory/context lens

The fresh specialist supplied a complete report against the frozen input and method. Its adopted records distinguish source documents/traces (OBJ-2), derived facts (OBJ-3), profiles and periodic older-memory aggregation (OBJ-4), symbolic access/provenance/disposition metadata (OBJ-5), transient recall cache (OBJ-6), and virtual-file documents (OBJ-7). The metadata determines scope or rank; a displayed fact string does not reveal every original payload or derivation.

Requested MCP/tool/file reads are RTE-1, RTE-5 and RTE-10. Automatic model-context supply is RTE-6, RTE-11 and RTE-12. The service calls made inside those wrappers are transport, not a second push classification. Each push names its trigger, identity and query inputs, selected content and consumer; item caps, cache keys and latency budgets do not become a total token bound. Bucket availability is not default bucket delivery: the default TypeScript profile request asks for static/dynamic sections.

Trace acquisition through RTE-7, RTE-11 and RTE-12 is wired. The automatic conversion of those traces into durable facts and older-memory profile summaries is documented in RTE-8; later reads complete a claimed trace-learning chain. It is not sufficient merely to store the raw trace. The profile preserves this weakest evidence basis, separate source families and unknown task horizon/timing. Session/custom identifiers alone establish neither per-task nor cross-task learning. The transient cache is not durable learning, and its eviction is not service-memory decay.

Maintenance includes document-backed file edits and documented graph update/forget/review operations, with known client behavior separated from remote effects. Source relationships and review flags exist or are documented, but default string formatting need not deliver them to the model (CLM-3). BAP-3 prevents delimiter collisions and replacement feedback in specified wrappers; it does not establish semantic injection immunity.

For retained rationale, raw traces and authored files may contain reasons, while extracted facts and profile strings have no required reason field. RTE-10 can read an authored reason when present and within the requested range; RTE-6 and RTE-12 do not guarantee delivery of derivation reasons. Thus neither diagnosis against prior rationale nor outcome improvement follows from this context-delivery architecture alone. The complete comparison profile records uncertainty instead of silently filling opaque alternatives.

### Epistemic lens

#### 1. Source-and-claim boundary

Use SRC-1 at the recorded revision. Question: which routes acquire or create truth-apt content, what checks license reliance, and how can content influence later work? Assessed: imported documents/traces, direct facts, graph extraction/inference and maintenance, profile aggregation, human review, client selection and model delivery. Backend implementations and observed candidate histories are unassessed. CLM-1 names the knowledge-production claim; CLM-2 is a benefit claim requiring independent evidence beyond interface inspection. Complete-architecture conclusions stop at the client/service boundary.

#### 2. Epistemic-object inventory

| Object/part | Candidate truth-apt content and claimed role | Producer/consumer; source | Limit |
|---|---|---|---|
| OBJ-2 | Source assertions in raw documents or conversation content; retrieval/extraction input | See RTE-7, RTE-9, RTE-11, RTE-12; SRC-1 | Import preserves available source identity, not source truth; opaque payloads cannot be classified from a displayed summary. |
| OBJ-8, part of OBJ-3 | Stated/extracted facts for personalization and recall | See RTE-8, RTE-9; SRC-1 | Extraction may preserve, compress or infer beyond a statement; fidelity is not measured. |
| OBJ-9, part of OBJ-3 | Unstated inferred facts; explicitly described as guesses | See RTE-8, RTE-9; SRC-1 | Ampliation is established by the documented example; no actual generated candidate is observed. |
| OBJ-4 | Static/dynamic profile and older-memory summaries; topical buckets | See RTE-8, RTE-6, RTE-12; SRC-1 | Intended compact representation is clear, but preservation versus new claims is indeterminate without outputs. |
| OBJ-7 | Arbitrary caller-authored file content, possibly factual or procedural | See RTE-10; SRC-1 | Exact retrieval does not validate the file's assertions or establish a theory-repair loop. |
| OBJ-1, OBJ-5 | Identity, provenance and disposition fields governing access/use | See RTE-3, RTE-8, RTE-9; SRC-1 | Operational metadata is distinct from the truth of retained assertions. |
| OBJ-6 | Cached recall text copied from other objects | See RTE-6; SRC-1 | Adds no independently warranted proposition. |

Generic form, storage and identity remain in the canonical object records rather than being reclassified here.

#### 3. Authority-route ledger

Each row below is one function. Architectural status is distinct from observed candidate state. Unless stated otherwise, no candidate instance was observed. Code establishes client mechanics, while doctrine specifies the external engine.

| Route and function | Architectural status | Object and content/update relation | Target, condition and timing | Operational result and behavioral path | Epistemic authority, scope and limit |
|---|---|---|---|---|---|
| RTE-7, RTE-11, RTE-12 — retention | implemented | OBJ-2; acquisition/import of conversation content | Persistable turns/history according to each SDK's trigger | Submits traces for service retention; later RTE-8 may consume them | No truth license or evidence of successful durable write follows from submission. Source: SRC-1, canonical route excerpts. |
| RTE-9 — retention | implemented | OBJ-2; acquisition/import of submitted content | MCP add accepted by remote API | Reports queued input; BAP-4 may later receive its products | Queuing does not establish extraction, source truth or graph readiness. |
| RTE-10 — content transformation | implemented | OBJ-7; caller-authored text changes | Model/caller selects create/edit/delete; structural/exact-content conditions apply | Evolves stored document through the service API; later exact view supplies text | No independent semantic check or prescribed outcome comparison. |
| RTE-8 — content transformation | doctrine only | OBJ-2 to OBJ-8/OBJ-9 and OBJ-4; extraction indeterminate, derives ampliative conjecture, aggregation intended reshaping | External learning model; ingestion/dynamic dreaming/periodic summary triggers | Creates or revises retained content for RTE-1, RTE-6 and other consumers | Source links and temporal flags do not warrant newly inferred claims. Engine implementation is uninspected. |
| RTE-8 — retention | doctrine only | OBJ-3 and OBJ-4; no additional content change | External graph/profile store | Persistence supports later recall | Retaining a guess is not accepting its truth. |
| RTE-9 — disposition/acceptance | doctrine only | OBJ-9 and OBJ-5; no content change to the proposition | Human-facing app sends approve/decline/undo; a semantic criterion is unspecified | Changes inference/forgotten/review flags, with reversal afforded | Documented human disposition licenses a change in product use. Evidence-consuming epistemic acceptance and an independent answer oracle are not established. |
| RTE-8, RTE-9 — operational admission/selection/consumption | doctrine only | OBJ-5; no content change | Current/inferred/expired/forgotten state, including human review | Changes eligibility or rank via BAP-5; unreviewed guesses remain eligible but downweighted | Selection is not a truth test. Actual service enforcement is uninspected. |
| RTE-1, RTE-5 — operational admission/selection/consumption | implemented | OBJ-2, OBJ-3, OBJ-4; no content change except display formatting | Requesting host, query/tag/ID and profile/prompt limits | Delivers service-returned material via BAP-4 | Shape and delivery are established; relevance, truth, activation and benefit are not. |
| RTE-6, RTE-11, RTE-12 — operational admission/selection/consumption | implemented | OBJ-3, OBJ-4, OBJ-6; no new claim from selection | Automatic pre-model or event trigger with identity and optional query | Injects context via BAP-4; formatting protections BAP-3 | Default formatter can omit status/provenance. It does not create epistemic authority or prove obedience. |
| RTE-2, RTE-3, RTE-4 — operational admission/selection/consumption | implemented | OBJ-1 and request credentials; non-truth-apt access state | Authentication, accessible-tag match, expiring upload token | Admits/blocks requests or routes them | Their evaluator domain is access/shape, not the correctness of memory content. |

No inspected source establishes an independent evidence-production route that tests every derived proposition before it can affect retrieval. This is a limit of the documented and public-client boundary, not a backend absence claim. All ledger rows refer to SRC-1 and their canonical source excerpts; generic endpoints and ownership remain on those records.

#### 4. Per-object lifecycle disposition

OBJ-2: acquisition/import through RTE-7, RTE-9, RTE-11 and RTE-12; discovery lifecycle is not applicable to merely retaining supplied assertions. Source warrant remains unknown, with lineage carried only to the extent the interface retains and delivers it.

OBJ-8: transformation indeterminate between faithful extraction/reshaping and additional inference. Input provenance is documented; actual source/output pairs and extraction checks would decide semantic preservation. The direct authored-fact branch of RTE-9 is acquisition, not autonomous discovery. Known text representation does not settle warrant.

OBJ-9: ampliative conjecture through RTE-8, with RTE-9 supplying documented human disposition. The phase account is:

| Phase | Architectural status | Observed candidate state | Evidence and boundary |
|---|---|---|---|
| Observation/input | doctrine only | no instance observed | RTE-8 consumes prior documents/facts; no candidate-linked trace retained. |
| Conjecture | doctrine only | no instance observed | OBJ-3/CLM-1 example derives a plausible unstated workplace focus. |
| Derived consequence | not determinable | no instance observed | No candidate-specific predicted test outcome is specified in the inspected design. |
| Test/evidence | not determinable | no instance observed | The review queue exposes a proposition and parent count, but no prescribed independent test of its truth. |
| Acceptance | not determinable | no instance observed | RTE-9 documents an approve action, not an explicit evidence-consuming criterion for a stated epistemic scope. Operational human disposition is doctrine only. |
| Lifecycle integration | not determinable | no instance observed | RTE-8/RTE-9 retention and ranking are documented, but post-epistemic-acceptance integration cannot be inferred. |

No observed candidate was used to infer acceptance, rejection or integration. Documentation examples are illustrations, not run evidence.

OBJ-4: transformation indeterminate. The intended aggregation reduces older memory into summaries and topic slices; this may be non-ampliative reshaping, but its word “synthesis” does not establish either preservation or novel claims. Later consumption is wired in RTE-6 and RTE-12. Exact pre/post summaries and their derivation would resolve the classification.

OBJ-7: caller-dependent authored content. Acquisition and exact text editing/read-back in RTE-10 have no automatic truth license; there is no observed proposition or repair episode to classify as a discovery lifecycle. OBJ-6 simply caches such context; its copying/eviction is not a new truth-apt transformation.

No lifecycle record for OBJ-1: no candidate truth-apt output for this operational state; relevant update routes are RTE-3 and RTE-4. No lifecycle record for OBJ-5's routing/disposition fields: they direct access or rank rather than create the underlying assertion; relevant update routes are RTE-8 and RTE-9. Their accuracy as metadata and their service enforcement remain separate limits.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design | Inspected implementation | Observed/causal support | Supported conclusion and mismatch/unknown |
|---|---|---|---|---|
| CLM-1 | Documents, fact graph, updates/derives, dreaming and profiles | Acquisition and later delivery are wired; engine transformation remains external | None captured | A coherent documented memory loop with inspectable client ends; no verified graph truth-maintenance or independent fact validation. |
| CLM-2 | Advertised benchmark and latency figures | No implemented measurement result is asserted | None captured | Attributed claim only; cannot infer end-to-end benefit or component effect. |
| CLM-3 | Inferred facts are explicitly guesses with review controls | Default profile formatter emits strings; custom formatting can retain more information | No actual model use observed | A consumer can receive less provenance than the stored graph represents. Loss is channel-specific, not universal. |
| CLM-4 | Intended later context influences behavior | Wrappers deliver modified parameters | No dependence experiment | Delivery is wired; activation, faithful use and benefit remain uninspected. |

#### 6. Bounded conclusion

Supermemory's clients acquire and return information and can automatically place recalled context before a model call. The engine's documented derives are candidate generation; the human review API changes operational reliance, while the available evidence does not establish an independent semantic acceptance test. Extraction and profile aggregation are not automatically knowledge production in the stronger epistemic sense. Raw-source access can support inspection, but default compact delivery can omit inference status and derivation context. These are route-level findings, not a system-wide epistemic grade.

## Reconciliation

The source register and record referents remained fixed. Parent CMP-1 and RTE-1 were checked by the specialist and retain their identities. RTE-1's hybrid return can include chunks; its tool description excludes the profile, not every non-fact payload. Parent authentication, space-routing and upload records remain separate from the memory acquisition/delivery routes. No combined record was silently narrowed or reassigned.

All specialist proposals were accepted with these exact mappings:

| Specialist proposal | Canonical record |
|---|---|
| MEM-OBJ-1 | OBJ-2 |
| MEM-OBJ-2 | OBJ-3 |
| MEM-OBJ-3 | OBJ-4 |
| MEM-OBJ-4 | OBJ-5 |
| MEM-OBJ-5 | OBJ-6 |
| MEM-OBJ-6 | OBJ-7 |
| MEM-RTE-1 | RTE-5 |
| MEM-RTE-2 | RTE-6 |
| MEM-RTE-3 | RTE-7 |
| MEM-RTE-4 | RTE-8 |
| MEM-RTE-5 | RTE-9 |
| MEM-RTE-6 | RTE-10 |
| MEM-RTE-7 | RTE-11 |
| MEM-RTE-8 | RTE-12 |
| MEM-CLM-1 | CLM-3 |
| MEM-CLM-2 | CLM-4 |
| MEM-BAP-1 | BAP-3 |

The two route families RTE-11 and RTE-12 keep their named integration branches and timing differences; no claim of exhaustive overload coverage is made. All fourteen comparison axes retain the specialist's scope, evidence basis, values and rationale, with only identifier remapping. OBJ-1 is surrounding runtime state; it does not broaden the compared derived-memory objects to include upload credentials or auth caches.

Integration issues are disposed as follows: raw inputs stay separate from graph facts and profiles; the virtual-file interface remains remote document storage; profile/resource requests remain pull; inferred review changes ranking/withdrawal rather than proving truth; the external console and remote engine remain uninspected; no session identifier becomes a task boundary; and no source test becomes an observed benefit. Parent review also identified two weak excerpt ranges in the provisional report; the specialist replaced them with relevant source passages before its final hash and validation. This is handoff correction, not independent semantic clearance. The lenses converge on the limits of inferred review and provenance delivery, but shared sources and coordination do not support a claim of independent evidential replication.


## Bounded synthesis

Supermemory connects retained user/application content to later model invocations through several concrete client mechanisms. MCP supplies requested retrieval and authoring; SDK wrappers add automatic identity/query-conditioned context and trace acquisition; the Claude memory adapter adds exact document-backed editing under a file-shaped interface. These distinctions change what is actually automatic, what is retained, and which consumer receives it.

The remote engine is the critical evidential boundary. The committed design describes document indexing followed by dreaming, graph updates and derived facts, profile aggregation, and inferred-memory review. These mechanisms complete a claimed trace-learning loop, while only the public acquisition/delivery ends are inspected as implementation. Calling the model a learning model neither fixes its weights nor establishes online parameter updates. Default context strings and recorded source metadata are also different evidence surfaces: a model may receive a fact without the information needed to judge its inference status.

For a client integrator, the strongest established properties are the available pull/push paths, their selection inputs and result formatting, and their failure/default-state behavior. For assessing the engine's retention correctness, deletion propagation, calibrated inference or claimed performance, this source boundary is insufficient. Appropriate evidence would include the engine implementation at a pin, candidate-linked extraction/review records, and controlled recalled-content interventions with outcomes.

Retained revisable content is present by interface and doctrine. A theory on an outcome-driven repair path is not established: editable facts/files alone do not show that an outcome localized a defect in the theory that guided a decision. Reflective theory refinement is likewise uninspected; no retained theory of Supermemory's own organization was traced through correction and later use. Automatic memory adaptation is claimed through RTE-8 and connected to wired client consumers, but measured self-improvement is not established. These conclusions concern distinct properties and are not an autonomy or maturity grade.

## Limitations

| Limitation | Affected records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| External engine and model internals | CMP-2, RTE-8, RTE-9, OBJ-3, OBJ-4 | Public clients, schemas and committed docs | Backend correctness, complete storage/curation sets, exact timing and parameter behavior | Pinned backend/model implementation and operational records |
| No deployed or causal run | CLM-2, CLM-4, BAP-4 | Static inspection only | Activation, faithful dependence, measured quality/cost or component effect | Retained candidate-linked runs and controlled interventions |
| Inference review has no specified independent truth criterion | OBJ-9, RTE-9, BAP-5 | Committed review endpoint contract | Evidence-based acceptance of a proposition | Reviewer evidence/criterion and linked disposition record |
| SDK task boundaries and alternatives | RTE-7, RTE-11, RTE-12 | Material named branches, not every overload | Complete task-horizon and transformation-schedule classifications | Application task semantics and matched complete route traces |
| Opaque original payloads and reduced delivery | OBJ-2, OBJ-4, CLM-3 | Visible schemas/formatters and docs | Full form set, guaranteed rationale/provenance delivery | Original payload inspection plus captured consumer context |
| External hosts, console, binaries and plugins | CMP-3, BAP-1, RTE-9 | Repository-defined interfaces | Host permissions, approvals, separately deployed consumer behavior and console implementation | Separately commissioned pinned sources or deployment evidence |
| Scope and authentication depend on service enforcement | RTE-2, RTE-3, BAP-2 | MCP checks and documented service contract | Universal tenant isolation or immediate credential revocation across all paths | Service-side policy implementation and adversarial authorization checks |

## Verification and blockers

### Semantic verification

Checked every scoped trace-fed write family (RTE-7, RTE-11, RTE-12) against its later RTE-8 fact/profile transformation and RTE-1/RTE-5/RTE-6 consumers; older-memory profile aggregation is included. Raw storage and cache eviction alone were not counted as learning. All fourteen profile axes retain the specialist's boundaries and weakest evidence basis. Unknown full storage/form/curation/signal/horizon/timing/faithfulness fields remain unknown.

Checked pull versus push by requesting consumer, not HTTP transport direction. Automatic branches name their trigger and selector; requested MCP profiles are not automatic injection, and virtual-file paths are not filesystem storage. Checked source/input/report/method hashes and canonical mappings. Named route families preserve material branches. No source tests or examples were promoted to observed operation; no model endpoint was treated as an exact weight pin. Each material quoted passage matches its frozen blob and supports its attached finding; code/prose evidence tiers remain separated. Review flags change operational eligibility and do not establish semantic acceptance. Runtime token/schema/access controls do not become truth checks. Source and field limits are retained beside the affected claims.

### Deterministic validation

Target: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-21-supermemory-01/result.md`. Passed cleanly: no failures or warnings. Source quotations and identities are also checked against the frozen source before publication; no execution of the target system is claimed.

### Blockers

None. External implementation and operational evidence limits are explicit analytical boundaries, not unresolved execution blockers.
