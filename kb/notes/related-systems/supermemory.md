---
description: Monorepo that open-sources Supermemory's MCP/SDK integration layer while delegating core memory extraction, contradiction handling, and profile synthesis to hosted /v3 and /v4 APIs
type: note
traits: [has-comparison, has-implementation]
tags: [related-systems]
status: current
last-checked: 2026-03-22
---

# Supermemory

Supermemory is a hosted memory platform plus a public integration monorepo. This repository contains the MCP server (`apps/mcp`), framework adapters (`packages/tools`, `packages/ai-sdk`, Python SDK wrappers), and graph visualization UI (`packages/memory-graph`). The central memory engine is mostly consumed over hosted endpoints (`/v3/*`, `/v4/*`) rather than implemented in-repo.

**Repository:** https://github.com/supermemoryai/supermemory

## Core Ideas

**Open integration layer, hosted memory core.** The code that is easy to inspect here is the integration shell: MCP tooling, prompt-injection middleware, and UI components. Core memory operations are delegated to hosted API calls such as `POST /v4/profile`, `POST /v4/conversations`, `GET /v3/projects`, and graph endpoints (`/v3/graph/bounds`, `/v3/graph/viewport`) from files like `packages/tools/src/shared/memory-client.ts`, `packages/tools/src/conversations-client.ts`, and `apps/mcp/src/client.ts`.

**MCP is treated as a first-class distribution channel.** `apps/mcp/src/server.ts` registers a broad MCP surface: tools (`memory`, `recall`, `listProjects`, `whoAmI`, `memory-graph`), resources (`supermemory://profile`, `supermemory://projects`), and a `context` prompt. `apps/mcp/src/index.ts` and `apps/mcp/src/auth.ts` support OAuth discovery plus API-key auth fallback, then proxy token validation to the hosted API.

**Authentication mediation is part of the product boundary.** The open MCP server does not just expose tools; it actively bridges client auth modes (OAuth tokens vs `sm_` keys), validates against hosted session endpoints, and injects authenticated user props into tool execution context. For this repo, auth plumbing is part of the architecture, not just deployment detail.

**Memory retrieval is packaged as prompt middleware.** The wrappers in `packages/tools/src/vercel/index.ts` and `packages/tools/src/shared/memory-client.ts` inject retrieved profile/search context into system prompts, with explicit modes (`profile`, `query`, `full`). They also support optional automatic write-back (`addMemory: "always"`) and per-turn caching (`packages/tools/src/shared/cache.ts`) to avoid repeated profile fetches during tool-call continuations.

**Graph observability is a concrete product surface.** The MCP app and graph package expose memory graph structure as interactive UI, including document-memory links, version chains (`parentMemoryId`), and similarity edges (`apps/mcp/src/ui/mcp-app.ts`, `packages/memory-graph/src/*`). This gives users a direct artifact for browsing evolution and forgetting state (`isLatest`, `isForgotten`, `forgetAfter`) even though extraction logic itself remains server-side.

**Cross-language wrapper breadth is a strategic bet.** The repo publishes many adapters (Vercel/AI SDK, OpenAI, Mastra, Agent Framework, Pipecat, Python variants). Most adapter logic repeats the same pattern: fetch profile/search context, deduplicate and format, inject prompt text, optionally save memory. The differentiator is integration ergonomics and coverage, not deep per-adapter algorithmic novelty.

## Comparison with Our System

| Dimension | Supermemory | Commonplace |
|---|---|---|
| Primary substrate | Hosted API service with open SDK/MCP integration layer | Markdown files in-repo as the primary substrate |
| Where memory logic lives | Mostly server-side behind `/v3` and `/v4` endpoints | In notes, links, and explicit curation workflows in the KB |
| Integration surface | Broad: MCP server, TS/Python wrappers, framework middleware | Focused: routing conventions, skills, and KB-native operations |
| Retrieval UX | Prompt-injected profile/search context and explicit recall tools | Progressive traversal through descriptions, indexes, and link semantics |
| Observability artifact | Interactive memory graph UI and viewport APIs | Git history + explicit link semantics + note-level structure |
| Knowledge lifecycle | API-managed memories with version/forget signals exposed in graph payloads | File-based promotion, status transitions, and deliberate refinement |
| Theoretical framing | Product framing around memory/personalization benchmarks | Explicit context engineering, distillation, constraining, codification theory |

Supermemory is stronger where we are thinner: turnkey integration breadth and MCP productization. Commonplace is stronger where Supermemory is opaque: inspectable, file-level reasoning artifacts and explicit semantic link discipline that can be audited without a hosted backend.

## Borrowable Ideas

Borrowable patterns here are mostly integration-shell patterns (middleware, interface boundaries, caching). They should be borrowed independently from any claim about backend extraction quality.

**Turn-keyed retrieval cache in middleware (ready now).** `MemoryCache.makeTurnKey(containerTag, threadId, mode, message)` is a practical guard against repeated API retrieval in one user turn. We can borrow the same shape for any expensive context fetch path.

**Conversation-level append endpoint pattern (needs use case).** `packages/tools/src/conversations-client.ts` treats a conversation as a first-class ingestion object (`/v4/conversations`) instead of only single snippets. This is relevant if we productize workshop/session capture in a structured way.

**Tool + resource + prompt triad in MCP design (ready now).** The MCP server pairs action tools, passive resources, and a dedicated context prompt. This separation is cleaner than one giant tool contract and maps well to our own retrieval vs mutation vs injection concerns.

**Shared cross-adapter core for consistency (ready now).** `packages/tools/src/shared/*` centralizes profile fetch, deduplication, prompt formatting, logging, and cache primitives across wrappers. That shared-core pattern is directly transferable to avoid behavioral drift across multiple integration surfaces.

**Exact-then-semantic forget fallback (ready now).** `apps/mcp/src/client.ts` tries exact forget first, then semantic fallback with a strict threshold. This is a strong deletion UX pattern when identifiers are missing.

## Curiosity Pass

**"Living knowledge graph" claims are only partially inspectable here.** The property claimed is adaptive knowledge evolution (updates, contradictions, forgetting). In this repo, we mostly see clients and UIs consuming that output shape (`isLatest`, `parentMemoryId`, `forgetAfter`) rather than the engine that computes it. Mechanistically, the open code mostly relocates API results into wrappers and interfaces; it does not let us verify extraction/contradiction resolution quality.

**Prompt middleware clearly transforms runtime context, not storage.** The middleware does real work (query extraction, deduplication, formatting, injection), so it is not pure relabeling. But its ceiling is bounded by upstream profile/search quality because local logic is mostly presentational. Even perfect middleware cannot fix weak upstream memory extraction.

**MCP breadth is implementation-real, but model behavior still depends on prompt policy.** The server exposes substantial functionality and auth flows, yet the biggest behavioral effect comes from textual tool descriptions and the `context` prompt encouraging memory writes. The mechanism is valid, but its reliability ceiling is still agent compliance, not hard guarantees.

**Graph UI is a strong inspectability move with a bounded oracle.** It visualizes structure and freshness signals well, and that is genuinely useful. But a graph of memories does not itself verify truth, contradiction handling quality, or extraction correctness; it primarily reveals topology and metadata.

**Cross-language adapter expansion trades uniqueness for reach.** Repeating similar wrapper logic across TypeScript and Python lowers adoption friction and is likely the right product call. The tradeoff is maintenance drift risk and shallow per-adapter innovation unless shared contracts stay tight.

**API contract stability is the hidden risk in this architecture.** Because open clients depend heavily on hosted `/v3` and `/v4` endpoints, integration reliability depends on endpoint semantics remaining stable. Version labels alone do not tell us whether these APIs are evolutionary stages or parallel domains, so compatibility guarantees become a central unknown.

## What to Watch

- Whether more of the core memory engine (not just adapters) becomes inspectable in this repo, especially contradiction-resolution and forgetting policy logic
- Whether wrapper behavior stays consistent across the growing TS/Python adapter set as features evolve
- Whether the graph endpoints become a stable contract for external tooling, not only first-party UI components
- Whether middleware-based prompt injection scales cleanly with very long sessions, or starts to need stronger server-side distillation gates
- Whether `/v3` and `/v4` API boundaries converge, split, or change semantics in ways that create adapter drift
- Whether benchmark leadership claims stay reproducible from public artifacts rather than docs-only references

---

Relevant Notes:

- [files-not-database](../files-not-database.md) — contrasts: Supermemory centers a hosted API substrate while this note argues for file-native knowledge as the primary medium
- [distillation](../distillation.md) — extends: Supermemory wrappers perform runtime context compression/injection, but output quality still depends on backend processing we cannot inspect in this repo
- [a functioning kb needs a workshop layer](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — enables: conversation-level ingestion patterns are a concrete reference for workshop-to-library promotion mechanisms
- [context efficiency is the central design concern in agent systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: per-turn caching and profile/query modes are explicit context-budget controls
- [pointer design tradeoffs in progressive disclosure](../pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: profile mode, query mode, and graph views expose different pointer tradeoffs across specificity, cost, and reliability
- [OpenViking](./openviking.md) — contrasts: both expose memory via service interfaces, but OpenViking foregrounds storage hierarchy while Supermemory foregrounds integration middleware and product adapters
- [Cognee](./cognee.md) — sibling: both use API-first retrieval pipelines and broad integration surfaces, with different emphasis on graph visualization versus pipeline programmability
