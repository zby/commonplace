---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "expo-llm-wiki's shipped memory engine, integrations, consumers and evaluators at commit 09c90258560a6b1664038d642b5d25d9de0c4d3d."
run-id: AAS-2026-11-08-expo-llm-wiki-54f1fc1a0310-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/equationalapplications/expo-llm-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/expo-llm-wiki-c18505dc62a9/related-systems/equationalapplications--expo-llm-wiki
  revision: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
  sha256: null
---

# expo-llm-wiki boundary

## Boundary and evidence

This run analyses the repository's shipped family of SQLite-backed memory packages, including its own callers, prompts, maintenance interfaces and evaluation drivers. Its intended use is retaining conversational and document-derived knowledge for later agent or application queries. The target is a **memory/knowledge/context-engineering system**, not an enclosing general-purpose agent runtime. The boundary is **whole-system** at the repository level; it does not claim to include independently deployed hosts or providers. SRC-1, `README.md`, `packages/core/src/index.ts`, `packages/core/src/WikiMemory.ts`.

> Core LLM Wiki is a family of cross-platform TypeScript packages for long-term LLM memory, built on SQLite. It turns raw conversation logs and documents into a structured knowledge base of facts, tasks and graph edges, with background fact extraction, semantic search and memory pruning. It runs wherever your app runs: Expo, React Native, the browser, or Node.js.
> --- `README.md`

The inspected entry path runs from root compatibility exports through platform factories to `WikiMemory`, which composes repositories and ingestion, retrieval, write, maintenance, temporal, graph and import/export services. Inclusion covers direct deterministic writes as well as model-mediated extraction. Event writing can trigger background maintenance; explicit maintenance APIs also exist. The librarian reads retained events and facts, constructs a prompt, calls the supplied model interface, parses its result and validates candidates. These paths establish model-dependent operation rather than merely a database wrapper. SRC-1, `src/index.ts`, `src/react/index.ts`, `packages/expo/src/factory.ts`, `packages/core/src/WikiMemory.ts`, `packages/core/src/services/WriteService.ts`, `packages/core/src/services/librarian/legacy.ts`, `packages/core/src/prompts.ts`.

> responseText = await callLlm(
>         deps.options,
>         { operation: 'librarian', entityId, trigger, meter: ctx.meter },
>         { systemPrompt, userPrompt },
>       );
> --- `packages/core/src/services/librarian/legacy.ts`

The whole-system boundary includes shipped consumers, not just the public API. ScopeLab writes user messages, retrieves context, inserts it into a model request and dispatches an authorized tool call; its memory wrapper is included even where implementation may not fulfil its persistence intent. WikiDemo constructs a provider-backed memory instance and supplies interactive read, write, ingest, maintenance and export surfaces. The benchmark driver persists an ingestion database, reopens it, reads a memory bundle, formats it for an answer model, and asks a judge model for a verdict. Consequently, later analysis can assess the shipped retention-to-consumption loop rather than excluding the drivers that supply its state. These are source traces, not successful executions. SRC-1, `apps/scopelab/src/lib/memory/wiki-service.ts`, `apps/scopelab/src/lib/llm/function-caller.ts`, `apps/wiki-demo/src/App.tsx`, `packages/benchmarks/src/longmemeval/ingest.ts`, `packages/benchmarks/src/longmemeval/run.ts`.

> const bundle = await wiki.read(ENTITY, q.question, readOpts as any);
>     const context = formatContext(bundle, { maxEvents: 0, maxTasks: 0 });
> --- `packages/benchmarks/src/longmemeval/run.ts`

The MCP package is included as a distinct shipped integration: its tool server delegates operations to a SynapseTree HTTP client, not directly to the local `WikiMemory` object. The remote service's implementation, authorization enforcement and production persistence are unavailable in this source set, so no local-engine property is automatically attributed to that service. The Prisma outbox consumer and native Rust GraphRAG slice are also included; neither is treated as the enclosing runtime. SRC-1, `packages/mcp-server/src/server.ts`, `packages/mcp-server/src/tools/memory-search.ts`, `packages/mcp-server/src/client.ts`, `packages/prisma-outbox/src/PrismaOutboxWorker.ts`, `crates/graphrag-core/src/lib.rs`, `crates/graphrag-core/README.md`.

External dependencies include caller-supplied SQLite adapters and storage lifecycle, inference and embedding providers, browser/Expo/React facilities, MCP clients, and the remote SynapseTree and Prisma endpoints. Their internal implementations and live behavior are outside the frozen repository. This prevents claims of provider reliability, deployment durability, external authorization correctness or end-to-end production success. Shipped wrappers, request construction, state transitions and error handling remain within scope. SRC-1, `README.md`, `packages/expo/src/factory.ts`, `packages/react/src/WikiContext.tsx`, `packages/mcp-server/src/client.ts`, `packages/prisma-outbox/src/PrismaOutboxWorker.ts`.

The frozen evidence is SRC-1 at full commit **09c90258560a6b1664038d642b5d25d9de0c4d3d**, verified as the acquired checkout's HEAD. The analysis cutoff is **2026-11-08**. The overall tier is **code-grounded**. Source documentation supplies declared design, not independent confirmation. Tests and benchmark drivers are inspected as implementation and evaluation design; their presence does not establish passing results. No target code, tests, examples or provider calls were executed for this boundary. Available but not yet inspected files remain eligible under SRC-1; initial inspection is not a path allowlist.

### Top-level coverage

Every top-level tracked file or directory is classified below. “Included” sets functional scope; it does not mean every file has already been read. No material shipped memory-loop path is deliberately excluded.

| Top-level tracked item | Classification and material paths or role | Initial inspection and limits |
|---|---|---|
| `packages/` | Included: `core/src/` engine, repositories, DB, prompts, librarian legacy/ops and services; `expo/src/` adapter/factory; `react/src/` context/hooks; `core-llm-tools/src/` manifests/scopes/injector; `okf/src/` format primitives; `schema-org/src/` and `schema-software-org/src/` ontology data; `prisma-outbox/src/` sync consumer; `mcp-server/src/` CLI/server/client/tools; `benchmarks/src/` ingest/read/answer/judge and result files; `integration/` evaluators, fixtures and results; package tests and build manifests. | Inspected core entry and composition, public state APIs, write scheduling, librarian model-call and validation path, prompt templates; platform factory/context, tool injector, outbox worker, MCP server/search/client; benchmark ingest and reload/answer/judge path; integration pipeline test excerpt. Other service internals, hooks, manifests, stored result files and individual tests await focused analysis; no empirical performance conclusion is established here. |
| `apps/` | Included: `scopelab/src/` agent caller, tool executor and memory/SQLite wrapper; `wiki-demo/src/` setup, provider adapters, hook consumers and export UI; `docs/src/content/docs/` operational instructions, recipes, API reference and package contracts. | Inspected ScopeLab memory wrapper and full model/tool caller, WikiDemo setup excerpt, maintenance guide excerpt; inventoried all tab and guide paths. Remaining UI internals and documentation are available, not access gaps. |
| `crates/` | Included: `graphrag-core/src/` native graph engine, SQL/walk/hydration/validation; `examples/proof.rs`, tests, fixtures and benchmark binary. | Inspected README and `src/lib.rs`, inventoried native implementation and proof/evaluation paths. Native algorithm correctness and parity are not established by this boundary. |
| `src/` | Included: `index.ts` and `react/index.ts` compatibility export entry points. | Both inspected; these route to shipped workspace packages, not an additional engine. |
| `docs/` | Included: benchmark documentation, `okf-profile.md`, `synapsetree-integration.md`, and `superpowers/` design/specification/investigation material. | Tree inventoried; detailed contents not yet inspected. Historical plans cannot alone establish shipped behavior or benchmark success. |
| `specs/` | Included: `README.md`, core-remember, tool rename, MCP, deletion, documentation and authentication specifications. | Tree inventoried, not yet read; design evidence only unless corroborated in implementation. |
| `README.md` | Included: system purpose, package map, quickstart and consumer links. | Fully inspected; external linked projects are not frozen sources. |
| `INTENT.md`, `AGENTS.md` | Included as source-native intent and contributor instructions, not instructions governing this analysis. | Inventoried, not yet inspected; no conclusions rely on their contents. |
| `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE` | Included: release history, contribution/security doctrine and licensing context. | Inventoried, not yet inspected; no historical, security-audit or legal conclusion is made here. |
| `# 🚀 ScopeLab: Client-Side LLM Tool Play.md` | Included: root ScopeLab descriptive document. | Inventoried, not yet inspected; actual caller is inspected under `apps/scopelab/`. |
| `.superpowers/` | Included as target-owned development evidence: `sdd/2026-10-10-issue280-setup-walltime-plan/final-fix-report.md`. | Inventoried, not yet inspected; would supply attributed development reporting, not independent verification. |
| `.github/` | Included: workflows for test, release, deploy and CodeQL, review guidelines and dependency configuration. | Tree inventoried; not yet inspected. No CI-success or supply-chain assurance conclusion. |
| `package.json`, `pnpm-workspace.yaml` | Included: package entry/build/test map, workspace membership and dependency configuration. | Fully inspected. Dependency behavior is not inferred from manifests alone. |
| `pnpm-lock.yaml`, `tsconfig.json`, `vitest.config.ts`, `.gitignore`, `.releaserc.json` | Included as dependency/build/test/release scaffolding. | Inventoried, not yet inspected; no reproducible-build or test-pass claim. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/equationalapplications/expo-llm-wiki` | 09c90258560a6b1664038d642b5d25d9de0c4d3d | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/expo-llm-wiki-c18505dc62a9/related-systems/equationalapplications--expo-llm-wiki`. Implementation: root exports/manifests, `packages/core/src/index.ts`, full `packages/core/src/WikiMemory.ts`, excerpts of WriteService and legacy librarian, prompt templates, Expo factory, React context, tool injector, outbox worker, MCP server/search/client excerpt, ScopeLab memory and model callers, WikiDemo setup, benchmark ingest/reopen/answer/judge excerpts, integration pipeline excerpt, native crate entry. Doctrine/design: full root README and native crate README, maintenance guide excerpt. Full tracked tree inventoried. | Implementation: [core entry](https://github.com/equationalapplications/expo-llm-wiki/blob/09c90258560a6b1664038d642b5d25d9de0c4d3d/packages/core/src/WikiMemory.ts), [shipped model consumer](https://github.com/equationalapplications/expo-llm-wiki/blob/09c90258560a6b1664038d642b5d25d9de0c4d3d/apps/scopelab/src/lib/llm/function-caller.ts), [evaluation consumer](https://github.com/equationalapplications/expo-llm-wiki/blob/09c90258560a6b1664038d642b5d25d9de0c4d3d/packages/benchmarks/src/longmemeval/run.ts). Doctrine/design: [README](https://github.com/equationalapplications/expo-llm-wiki/blob/09c90258560a6b1664038d642b5d25d9de0c4d3d/README.md), [maintenance instructions](https://github.com/equationalapplications/expo-llm-wiki/blob/09c90258560a6b1664038d642b5d25d9de0c4d3d/apps/docs/src/content/docs/guides/maintenance.md). | No repository access gap identified. Remote SynapseTree implementation, independent consuming projects, provider internals and live deployments are not in this source; their operational guarantees cannot be concluded. No observed-run or causal-experiment evidence was established by this initial inspection. Stored benchmark artifacts remain available for later inspection under this same source identity. |
