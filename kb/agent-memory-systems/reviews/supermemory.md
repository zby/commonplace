---
description: "Supermemory review: hosted memory API with generated SDK contracts, profile/search injection middleware, MCP tools, browser capture, graph UI, and trace-derived memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-05"
---

# supermemory

Supermemory, from `supermemoryai/supermemory`, is a hosted memory and context platform plus open-source clients around it. At the reviewed commit, this checkout exposes the public docs, API validation schemas, browser extension, hosted MCP server wrapper, framework middleware, memory graph UI, and tool packages. The hosted engine claims fact extraction, profiles, graph relations, contradiction handling, forgetting, hybrid search, connectors, and file processing, but the core backend algorithms that create those retained artifacts are not fully present in this repository.

**Repository:** https://github.com/supermemoryai/supermemory

**Reviewed commit:** [c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77](https://github.com/supermemoryai/supermemory/commit/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77)

**Last checked:** 2026-06-05

## Core Ideas

**The repository is mostly integration surface around a hosted memory engine.** The README describes Supermemory as "the memory and context layer for AI" with memory extraction, profiles, hybrid search, connectors, and file processing, while the local MCP server and wrappers call `https://api.supermemory.ai` or an injected `API_URL`/`baseUrl` rather than implementing the extraction engine locally ([README.md](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/README.md), [apps/mcp/src/client.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/mcp/src/client.ts), [packages/tools/src/shared/context.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/shared/context.ts)). Treat docs about graph evolution and forgetting as hosted API contracts unless backed by visible client code.

**Documents and memories are separate API objects.** The docs frame documents as raw inputs and memories as extracted, contextual knowledge units; the shared schemas mirror that split with `DocumentSchema`, `ChunkSchema`, and `MemoryEntrySchema` carrying content, chunks, embeddings, relations, versioning, source counts, `isLatest`, `isForgotten`, and `forgetAfter` fields ([apps/docs/concepts/how-it-works.mdx](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/docs/concepts/how-it-works.mdx), [packages/validation/schemas.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/validation/schemas.ts)). The visible client layer assumes a memory graph but does not show the full derivation implementation.

**Graph memory is a facts-on-facts relation model, not just vector RAG.** The docs name `updates`, `extends`, and `derives` as relationship types; the validation schema and memory graph package expose the same relation vocabulary and render relation edges from backend-supplied `memoryRelations` or legacy `parentMemoryId` fallback ([apps/docs/concepts/graph-memory.mdx](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/docs/concepts/graph-memory.mdx), [packages/memory-graph/src/api-types.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/memory-graph/src/api-types.ts), [packages/memory-graph/src/hooks/use-graph-data.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/memory-graph/src/hooks/use-graph-data.ts)). This is a stronger memory contract than plain document search, even though graph construction is hosted.

**Context efficiency is split between profile condensation and query-scoped retrieval.** The middleware mode can be `profile`, `query`, or `full`: profile mode injects static/dynamic user profile facts; query/full mode extracts the latest user message and asks the hosted profile/search API for query-relevant memories ([packages/tools/src/shared/types.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/shared/types.ts), [packages/tools/src/shared/memory-client.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/shared/memory-client.ts)). The wrapper then formats only deduplicated profile/search strings into the system prompt, avoiding full-store context injection by default.

**Adoption is broad because read/write surfaces are native to host tools.** The repo ships Vercel AI SDK tools and middleware, Mastra processors, VoltAgent middleware, OpenAI middleware, Python OpenAI and Microsoft Agent Framework middleware, a hosted MCP server, a browser extension, a consumer web app, and a memory graph React component ([packages/tools/src/ai-sdk.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/ai-sdk.ts), [packages/tools/src/mastra/wrapper.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/mastra/wrapper.ts), [apps/mcp/src/server.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/mcp/src/server.ts), [apps/browser-extension/entrypoints/background.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/browser-extension/entrypoints/background.ts), [packages/openai-sdk-python/src/supermemory_openai/middleware.py](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/openai-sdk-python/src/supermemory_openai/middleware.py), [packages/agent-framework-python/src/supermemory_agent_framework/middleware.py](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/agent-framework-python/src/supermemory_agent_framework/middleware.py)).

## Artifact analysis

- **Storage substrate:** `service-object` `vector` `graph` — The durable memory store is a hosted Supermemory service object reached by API clients; visible schemas and UI contracts expose embedding fields, chunk search, memory relations, version chains, forgotten/expiry flags, and document-memory joins, but this checkout does not reveal the production storage engine behind those contracts.
- **Representational form:** `prose` `symbolic` `parametric` — Memory content, profile facts, summaries, prompts, and documents are prose; container tags, custom IDs, metadata filters, schemas, relation types, processing statuses, version fields, and tool definitions are symbolic; embeddings, similarity scores, hybrid search, reranking, and query rewriting are parametric or model-mediated access structures.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author direct memory/document content; browser capture, Twitter bookmarks, connectors, uploads, URLs, PDFs, images, and videos are imported; conversations, tool/plugin sessions, browser prompts, and chat messages are trace sources that the hosted API turns into memory entries, profiles, relations, and summaries.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Retrieved memories and profiles advise agents; MCP/tool descriptions and injected memory blocks instruct host agents; container tags/projects/custom IDs route scope; zod schemas and middleware guards validate calls; search modes, thresholds, embeddings, rerank, and relation expansion rank context; hosted extraction/profile/graph updates implement learning from accumulated traces.

**Hosted memory entries and profiles.** Storage substrate: Supermemory API objects, visible through `MemoryEntrySchema`, `/v4/profile`, `/v4/search`, `client.add`, `client.profile`, and `client.search.memories`. Representational form: memory strings and profile facts plus symbolic fields such as `isStatic`, `isLatest`, `memoryRelations`, `forgetAfter`, metadata, container tags, and embeddings. Lineage: authored or imported raw material becomes extracted memory; conversation and prompt traces become profile/search facts through hosted processing. Behavioral authority: knowledge context when returned to a user or agent, ranking input when embeddings/relations shape search, and learning input when new conversations update future profiles.

**Documents, chunks, connectors, and browser captures.** Storage substrate: hosted document API objects with local schemas and extension clients. Representational form: raw content, extracted chunks, summaries, metadata, processing state, and source/provider identifiers. Lineage: imported from browser pages, highlights, Twitter/X bookmarks, connector syncs, uploads, and URLs; invalidation/regeneration depends on the hosted processing pipeline, not visible local code ([apps/browser-extension/utils/api.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/browser-extension/utils/api.ts), [apps/browser-extension/utils/twitter-import.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/browser-extension/utils/twitter-import.ts), [packages/validation/api.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/validation/api.ts)). Behavioral authority: knowledge source and extraction substrate for later memories.

**Middleware and MCP prompt surfaces.** Storage substrate: mostly not durable themselves, except MCP Durable Object session/client metadata and cached project tags; their durable effect comes from calls into the hosted memory API. Representational form: symbolic tool schemas plus prose prompts and memory blocks. Lineage: authored integration code assembled with hosted profile/search results just before a model call. Behavioral authority: instruction and knowledge because injected system prompts or MCP prompts can steer the next model invocation ([apps/mcp/src/server.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/mcp/src/server.ts), [packages/tools/src/vercel/memory-prompt.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/vercel/memory-prompt.ts), [packages/tools/src/shared/prompt-builder.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/shared/prompt-builder.ts)).

**Memory graph UI and API types.** Storage substrate: derived frontend state over hosted document/memory responses. Representational form: symbolic graph nodes/edges plus prose memory/document labels. Lineage: derived view over API documents and memory entries; edge computation uses `memoryRelations` first and `parentMemoryId` only as fallback. Behavioral authority: human/operator inspection and debugging, not direct agent enforcement, though it reveals what the hosted system claims as memory relationships.

Promotion path: the intended ladder is raw content or conversation trace -> hosted document/chunk processing -> extracted memory entries -> profile/static/dynamic facts and memory relations -> injected or retrieved context. The local repository verifies the wrapper and schema layers of that ladder, but not the hosted extraction oracle's precision, contradiction resolution, or forgetting policy.

## Comparison with Our System

| Dimension | Supermemory | Commonplace |
|---|---|---|
| Primary purpose | Hosted memory/context platform for products and AI tools | Repo-native methodology KB for agents and maintainers |
| Canonical retained artifact | Hosted document, memory entry, profile fact, relation, embedding/search result | Git-tracked typed Markdown artifact with explicit source links |
| Write path | API/MCP/browser/framework ingestion; hosted extraction and profile updates | Authored notes, reviews, source snapshots, validation, review gates |
| Read-back | Pull tools/search plus push middleware/system-prompt/profile injection | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | API schemas, client guards, project/container scoping, hosted forgetting/version fields | Collection contracts, type specs, deterministic validation, semantic review, git history |

Supermemory is stronger as a deployable memory service. It has OAuth/API-key MCP, SDK and framework wrappers, browser capture, consumer UI, graph visualization, connector docs, profile APIs, and pre-call middleware. Commonplace is stronger as an inspectable knowledge substrate: the artifact text, source lineage, type contract, and validation behavior all live in the repository and can be reviewed in diffs.

The main tradeoff is hosted power versus source-visible authority. Supermemory can offer profiles, semantic memory search, relation-aware graph memory, and automatic context injection with minimal application code. But the most consequential learning behavior - which facts are extracted, what updates or derives what, when something is forgotten, and whether current facts beat stale ones - lives behind the hosted API. Commonplace cannot provide that turnkey runtime, but its behavior-shaping state is reviewable without trusting a service.

### Borrowable Ideas

**Make profile context a first-class retrieval shape.** Ready for narrow use. Commonplace could expose "current operator/project profile" summaries for review runs or workshops, separate from ordinary search results.

**Keep profile mode, query mode, and full mode distinct.** Ready now as an API design pattern. It prevents "always include everything" from being the only read-back strategy and makes context volume/complexity explicit.

**Use relation types that distinguish update, extension, and derivation.** Needs a concrete artifact family. Commonplace links already carry labels, but memory-like facts could benefit from explicit `updates` versus `extends` semantics when maintaining current operational state.

**Do not borrow hosted opacity for high-authority artifacts.** The convenience of automatic extraction is useful for low-authority memory, but Commonplace should require source spans, review state, or validation before trace-derived material becomes instruction or enforcement.

**Expose memory graph visualization as an inspection layer.** Needs a bounded use case. A visual graph over notes/reviews could help operators inspect clusters and stale relations, but it should remain a view over repo-native artifacts, not the source of truth.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents manually save memories/documents through SDK, MCP, browser, web UI, and tools; automatic paths include middleware conversation capture, browser prompt capture, connector/import flows, hosted extraction into memory entries, profile updates, relation/version fields, and forgetting/expiry contracts.

**Curation operations:** `evolve` `synthesize` `invalidate` `decay` `promote` — Hosted docs/API contracts describe memory updates, extensions, derived memories, current/latest flags, forgetting, expiring memories, static/dynamic profiles, and preference strengthening. The local checkout exposes the fields and client calls, but not the full backend algorithms, so these operations are contract-level rather than fully implementation-verified here.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Framework middleware saves chat messages or conversations; OpenAI/Agent Framework wrappers can store conversations around model calls; MCP tools save explicit user/agent facts; browser content scripts capture prompts, highlighted pages, full page markdown, and Twitter bookmark streams.

**Learning scope:** `per-project` `cross-task` — Memory is scoped by `containerTag`, `containerTags`, projects, `customId`, and conversation IDs, allowing per-user, per-project, tenant, or session grouping reused across later conversations and clients.

**Learning timing:** `online` `staged` — Middleware retrieves before a call and can save conversation traces in the same request path or background task; browser/import/connector flows are staged ingestion; hosted processing queues documents through extracting, chunking, embedding, indexing, and done states.

**Distilled form:** `prose` `symbolic` `parametric` — Outputs include prose memory facts, profile facts, summaries, and prompt blocks; symbolic relations, version flags, forget fields, metadata, project tags, and processing states; and embeddings/similarity/rerank signals for retrieval.

**Trace source.** Supermemory qualifies as trace-derived because durable memory is explicitly built from conversation and tool-use surfaces, not only manually authored notes. Vercel middleware converts prompts and assistant responses into `/v4/conversations` messages; OpenAI middleware can save the conversation before/alongside the wrapped call; Python Agent Framework middleware creates background save tasks; browser code captures prompts and pages; MCP `memory` saves facts the assistant decides are worth remembering ([packages/tools/src/vercel/middleware.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/vercel/middleware.ts), [packages/tools/src/openai/middleware.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/tools/src/openai/middleware.ts), [packages/agent-framework-python/src/supermemory_agent_framework/middleware.py](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/packages/agent-framework-python/src/supermemory_agent_framework/middleware.py), [apps/browser-extension/entrypoints/background.ts](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/browser-extension/entrypoints/background.ts)).

**Extraction.** The extraction oracle is hosted. The docs claim automatic fact extraction, profile maintenance, relation creation, contradiction resolution, and forgetting; local code shows the API payloads and response fields that carry those products, but not the model prompts, graph update logic, or quality gates that decide which trace becomes memory.

**Scope and timing.** Scope is mainly container/project based. Timing is online for wrapper injection and optional conversation save, staged for browser imports, connector syncs, and document processing. The visible `processingMetadata` and document status enums make processing phase explicit, which is useful even though the processing workers are not visible.

**Survey fit.** Supermemory strengthens the trace-to-profile and trace-to-graph-memory families: raw conversations and imported user activity become lower-volume profile facts and related memory entries that future agents can receive without searching the original traces. It also highlights a recurring survey caveat: hosted trace-derived systems may expose enough API contract to classify the artifact but not enough implementation to audit extraction fidelity.

## Read-back

**Read-back:** `both` — Direct SDK, MCP, browser, and AI SDK tools support explicit pull search/profile/list operations; framework middleware and model wrappers also push retained profile/search context into system prompts or instructions before the receiving model call.

**Read-back signal:** `coarse` `inferred / embedding` — Profile mode is coarse because it injects static/dynamic profile facts for the container without a query; query/full modes infer relevance from the latest user message and call hosted profile/search APIs that expose semantic memory search, similarity thresholds, hybrid search, rerank, and related-memory expansion.

**Faithfulness tested:** `no` — I found unit/integration tests and docs for wrappers, graph edge computation, schemas, and API calls, but not an ablation or post-action audit showing that injected memories changed the agent's behavior.

**Direction edge cases.** MCP `recall`, `memory`, `listProjects`, `memory-graph`, SDK `search.memories`, and AI SDK `searchMemories` are pull tools from the acting agent's perspective. MCP's `context` prompt and framework middleware are push when the host invokes them to assemble context for a model. External plugin docs for Codex and Claude Code describe stronger hook-based push, but those plugin implementations live in separate repositories, so this review treats them as documented integrations rather than implementation-visible behavior ([apps/docs/integrations/codex.mdx](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/docs/integrations/codex.mdx), [apps/docs/integrations/claude-code.mdx](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/docs/integrations/claude-code.mdx)).

**Targeting and signal.** Coarse push comes from profile/static/dynamic memories and the MCP `context` prompt. Instance-targeted push comes from query/full modes that extract the latest user message, request hosted profile/search results, deduplicate them, and append them to a system prompt. The visible client code does not implement local BM25/vector ranking; it delegates relevance to `/v4/profile`, `/v4/search`, `client.profile`, or `client.search.memories`.

**Injection point.** Read-back happens pre-invocation. Vercel middleware transforms model call params before generation; OpenAI middleware rewrites chat messages or Responses API instructions before calling the original client; VoltAgent and Python middleware mutate/prepend system messages before `call_next`; MCP `context` returns a prompt message for the host to include before model action.

**Selection, scope, and complexity.** Selection controls include container tags, project IDs, custom IDs, mode, query text, limits, thresholds, `searchMode`, related-memory include flags, rerank, query rewriting, and custom prompt templates. Complexity can grow when full mode combines profile facts with search results, or when `include.relatedMemories`/hybrid results bring document chunks and relation context. Actual context dilution is not proven by code.

**Authority at consumption.** Injected memory is usually advisory system-prompt context. MCP/tool descriptions raise authority by telling the agent when to save/recall, but they do not enforce behavior. The memory graph is a human/debugging consumer surface; wrappers and model calls are the agent-facing consumers.

**Faithfulness.** Structural tests can show that wrappers inject, deduplicate, cache, and save, and graph tests show relation rendering behavior. They do not demonstrate that a model obeys the memory or that profile/search output is true, current, or causally responsible for downstream action.

**Other consumers.** Humans consume the same retained state through the consumer app, graph view, browser extension, MCP app UI, settings/connections pages, and docs. The web app's Nova chat also highlights memories used by Nova in a graph rail, but its backend retrieval implementation is not fully visible in this checkout ([apps/web/components/chat/chat-graph-context-rail.tsx](https://github.com/supermemoryai/supermemory/blob/c5bf8ff1f75fc5de22d03ca4be2e03630daa9f77/apps/web/components/chat/chat-graph-context-rail.tsx)).

## Curiosity Pass

**The most important implementation is outside the checkout.** The repo is still useful because it exposes schemas, wrappers, and docs, but reviewers should not mistake the open-source integration layer for the hosted extraction and graph-update engine.

**Supermemory's strongest context-efficiency idea is not top-k search; it is profile shape.** Static/dynamic profile facts are a pre-distilled context surface that avoids repeatedly asking semantic search for basic user context.

**Graph visualization makes hidden hosted state auditable only after the fact.** The memory graph package can reveal relation and forgetting state returned by the API, but it cannot explain why the relation was created.

**The wrapper defaults are authority-heavy.** Several integrations default to `addMemory: "always"` or automatic prompt injection, which is good for adoption but risky for privacy and low-quality trace capture unless applications scope container tags and custom IDs carefully.

**The docs distinguish memory from RAG better than many systems.** The explicit documents-versus-memories split is useful, even if the backend evidence for temporal reasoning is service-side.

## What to Watch

- Whether the hosted extraction, relation creation, contradiction handling, and forgetting algorithms become source-visible or externally auditable; that determines whether Supermemory can be reviewed beyond API contract fidelity.
- Whether framework wrappers add behavioral faithfulness tests, such as with/without memory ablations for profile and query/full modes.
- Whether `memoryRelations`, `isLatest`, `isForgotten`, and `forgetAfter` gain source-span provenance in API responses; that would make automatic graph updates more reviewable.
- Whether external Codex/Claude Code plugin implementations are pulled into this monorepo or cited with pinned source; their hook behavior is central to push read-back but currently outside this checkout.
- Whether default automatic capture remains opt-out; for Commonplace-like high-authority use, automatic trace capture needs explicit scope, redaction, and promotion gates.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Supermemory has both explicit pull tools and middleware/profile push into model context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: hosted memory entries, documents, graph relations, middleware prompts, and graph UI views carry different substrates, forms, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: profile facts, memory entries, document chunks, and graph views usually advise as context or evidence.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: MCP tool schemas, middleware injection code, zod validation schemas, search parameters, and relation/ranking policies configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Supermemory turns conversations, prompts, browser captures, and imported activity into retained profiles and memory graph entries.
