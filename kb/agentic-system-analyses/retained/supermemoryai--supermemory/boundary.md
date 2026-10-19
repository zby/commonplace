---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Supermemory's public memory integrations and documentation at f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe, with the server-side memory loop unavailable as code."
run-id: AAS-2026-10-19-supermemory-1cc18c778c48-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/supermemoryai/supermemory
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-supermemory/related-systems/supermemoryai--supermemory
  revision: f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe
  sha256: null
---

# Supermemory boundary

## Boundary and evidence

This run analyses Supermemory as a memory/knowledge/context-engineering system, using its public repository to explain how retained content is submitted and later supplied to model applications. The intended use is a source-grounded account of its memory interfaces, shipped integration loops and declared server behavior, not a verification of product performance. The frozen revision is `f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe`; the applicability cutoff is 2026-10-19. The checkout's HEAD matched that revision and its working tree was clean at initial inspection.

The boundary kind is **complete artifact, partial loop**. The entire registered Git artifact is eligible evidence, including shipped callers, prompts, maintenance guidance, examples and tests. It is not the complete implementation of the Supermemory product. Its own self-hosting documentation explicitly separates the public components from the server codebase (SRC-1, `apps/docs/self-hosting/overview.mdx`):

> The SDKs and other components in the [public repository](https://git.new/memory) are open source; the downloadable self-hosted server binary is built from a separate, non-public codebase.
> --- `apps/docs/self-hosting/overview.mdx`

The overall evidence tier is **code-grounded** because executable memory adapters, an MCP server and application callers can be inspected. Claims about extraction, graph maintenance, contradiction resolution, automatic forgetting, embedding generation and backend ranking remain documentation-grounded unless the frozen artifact supplies a narrower implementation basis. The non-public server is an unavailable implementation dependency, not an inspected subsystem. This gap prevents an end-to-end code-grounded explanation of how submitted content becomes maintained memories and profiles.

### Shipped paths and initial inspection

The repository tree and root workspace manifest were inspected before classification (SRC-1, `package.json`). The following is a scope and initial-inspection map, not a claim that every file has been read. Material not yet inspected remains within the evidence boundary for later source analysis.

| Path family | Functional inclusion and initial inspection | Limit on conclusions |
|---|---|---|
| `apps/mcp/` | Included: HTTP/MCP entry point, tool registration, profile/context consumption, namespace selection and API client. Initially read `src/server/index.ts` entry declarations, `src/server/server.ts`, `src/server/tools/index.ts`, `src/server/client/index.ts` and `src/server/prompts/context.ts`. Widget UI, individual tool handlers, durable state and tests remain available for inspection. | Server registration and client operations are established; comprehensive authorization, UI and state-transition correctness are not established by this initial trace. |
| `packages/tools/` | Included: public exports and framework memory middleware. Initially inspected `package.json`, `src/vercel/index.ts` generation path, `src/vercel/middleware.ts` persistence/retrieval functions and `src/conversations-client.ts`. Other adapters, shared prompts, caching, Claude memory operations, examples and tests remain in scope. | The initial Vercel trace does not establish behavioral parity across OpenAI, Mastra, Voltagent or other adapters. |
| `apps/sdk-playground/` | Included as a shipped consumer, not an external host. Initially inspected `src/lib/chat-handlers.ts` AI SDK and OpenAI middleware callers. Python server, request handlers, context display and browser state remain available. | This establishes a shipped model-call consumer, not verified cross-session browser behavior. |
| Python integration packages | Included: `packages/agent-framework-python/`, `packages/cartesia-sdk-python/`, `packages/livekit-sdk-python/`, `packages/openai-sdk-python/`, `packages/pipecat-sdk-python/`, including examples and tests. Tree inspected; implementations not yet inspected. | No Python lifecycle or adapter-equivalence conclusions at boundary declaration. |
| Graph paths | Included: `packages/memory-graph/` and `apps/memory-graph-playground/`, including API routes and evaluative tests. Tree inspected; initial backend graph-fetch boundary seen in the MCP client. | Visualization behavior and graph semantics require further inspection; visualization is not evidence of backend inference. |
| Documentation and skills | Included: `apps/docs/`, `skills/supermemory/`, root README files, `CLAUDE.md` and `CONTRIBUTING.md` as source-native guidance, not instructions binding this analysis. Initially inspected `README.md`, `apps/docs/self-hosting/overview.mdx`, `apps/docs/memorybench/overview.mdx` and the capability/integration portions of `skills/supermemory/SKILL.md`. Other prompts, rules, review/forgetting guidance and API-version documents remain in scope. | Product promises and installation examples do not establish implemented backend mechanisms or version consistency across every example. |
| Evaluative material | Included: `apps/mcp/e2e/`, colocated tests, `packages/tools/test/`, Python test directories and `packages/docs-test/`. Tree inspected; no tests executed. MemoryBench's overview was read as a description of an external evaluator. | No observed-run or causal-experiment evidence is established. Benchmark rankings and latency/recall claims are not independently verified. |
| Other support paths | Included where relevant: `apps/web/`, `packages/lib/`, `packages/hooks/`, `packages/ui/`, `packages/validation/`, `.github/` and root configuration, lockfiles and license. Initially read `apps/web/app/page.tsx`, which redirects users to the console; remaining support implementations are not yet inspected. | The redirect is not an implementation of the destination console. Build, publication, validation and shared UI behavior need their own inspection before claims. |

### Entry points and retained-state consumers

The initial trace establishes more than a library API alone. `@supermemory/tools` declares its framework entry points in `packages/tools/package.json`; its Vercel wrapper intercepts generation, retrieves memory before the base model call and invokes the persistence helper afterward when configured to save. The helper serializes the conversation and submits it through the SDK (SRC-1, `packages/tools/src/vercel/index.ts`, `packages/tools/src/vercel/middleware.ts`, `packages/tools/src/conversations-client.ts`). The application consumer in `apps/sdk-playground/src/lib/chat-handlers.ts` constructs the wrapper with a namespace and conversation ID and passes the wrapped model to `generateText`.

The submitted conversation retains an explicit grouping identifier and requests immediate memory processing; this is a client request, not evidence that backend processing completed (SRC-1):

> content: formatConversationText(params.messages),
> id: params.id,
> dreaming: "instant",
> --- `packages/tools/src/conversations-client.ts`

The MCP entry imports the server factory; that factory registers tools, resources and a context prompt. Its API client delegates memory creation, forgetting, search and profile reads to the external `supermemory` SDK/API. The context prompt consumes the returned static and dynamic profile facts and returns a user-role message. Thus retained-content consumption and model-facing instructions are included, not treated as responsibilities of an excluded application (SRC-1, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/tools/index.ts`, `apps/mcp/src/server/client/index.ts`, `apps/mcp/src/server/prompts/context.ts`). The prompt explicitly constrains cross-space use:

> Use a space key with space-aware tools when the user asks about another space. Keep space contexts separate unless the user asks to combine them.
> --- `apps/mcp/src/server/prompts/context.ts`

### External dependencies and evidence limits

The npm/Python `supermemory` SDK implementations, hosted API and authentication services, non-public server binary, model providers, connector services and separately linked coding plugins are outside the frozen repository unless represented by source text inside it. Their documented interfaces are usable as declared contracts, not inspected implementations. Framework runtimes and MCP clients remain external execution dependencies; the repository's own middleware, MCP server and shipped application callers remain included. These limits prevent attributing host scheduling, model reasoning or remote storage correctness to the inspected code (SRC-1, `packages/tools/package.json`, `apps/mcp/src/server/client/index.ts`, `apps/mcp/src/server/index.ts`, `README.md`).

MemoryBench is described as a separate repository in `apps/docs/memorybench/overview.mdx`; neither that repository nor benchmark runs are registered here. README results therefore remain attributed reports, not observed evaluation evidence. No target code, examples or tests were executed, no model/service calls were made and no linked repository or live page was added to this source set.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/supermemoryai/supermemory` | f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-supermemory/related-systems/supermemoryai--supermemory`. Implementation: tracked tree, root `package.json`, `packages/tools/package.json`, `packages/tools/src/vercel/index.ts` generation path, `packages/tools/src/vercel/middleware.ts` persistence/retrieval sections, `packages/tools/src/conversations-client.ts`, `apps/sdk-playground/src/lib/chat-handlers.ts` middleware callers, MCP entry declarations, server factory, tool registry, API client, context prompt and `apps/web/app/page.tsx`. Doctrine/design: `README.md`, `apps/docs/self-hosting/overview.mdx`, capability/integration portions of `skills/supermemory/SKILL.md`, `apps/docs/memorybench/overview.mdx`. Reported operation: README benchmark and performance claims, not independently verified. | Implementation: [Vercel wrapper](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/packages/tools/src/vercel/index.ts), [conversation submission](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/packages/tools/src/conversations-client.ts), [shipped caller](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/apps/sdk-playground/src/lib/chat-handlers.ts), [MCP factory](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/apps/mcp/src/server/server.ts), [MCP client](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/apps/mcp/src/server/client/index.ts). Doctrine/design: [server availability](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/apps/docs/self-hosting/overview.mdx), [shipped skill](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/skills/supermemory/SKILL.md). Reported operation: [README](https://github.com/supermemoryai/supermemory/blob/f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe/README.md). | Non-public engine and external SDK/service implementations prevent end-to-end implementation conclusions about extraction, admission, maintenance and retrieval quality. External plugins and MemoryBench implementation/runs are not captured; their operation and reported results cannot be independently verified here. Available but initially uninspected paths are not access gaps. No observed run or causal experiment is registered. |
