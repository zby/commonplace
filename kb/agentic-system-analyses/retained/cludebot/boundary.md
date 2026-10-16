---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Cludebot's shipped memory system and its bot, service, client and maintenance paths at commit cecf234f10397b1e21dec2ff65ded864982f3564."
run-id: AAS-2026-10-15-cludebot-cb70d11d215b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: cecf234f10397b1e21dec2ff65ded864982f3564
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/sebbsssss/cludebot
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-cludebot/related-systems/sebbsssss--cludebot
  revision: cecf234f10397b1e21dec2ff65ded864982f3564
  sha256: null
---

# Cludebot boundary

## Boundary and evidence

This run analyses the Cludebot repository's shipped system, called Clude in its own documentation, to explain how retained memory is produced, maintained, retrieved and consumed. The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system**, not the exported SDK alone. It includes the repository's bot and model-calling consumers, hosted server, workers, local stores, MCP and CLI integrations, user-facing clients, portability and admission paths, and evaluators. This classification does not imply that every deployment enables every path or that each storage mode has identical behavior (SRC-1, `README.md`, `package.json`, `Dockerfile`, `packages/brain/src/sdk/cortex.ts`, `packages/brain/src/mcp/server.ts`, `apps/workers/src/jobs/index.ts`).

The frozen source is the acquired checkout at **cecf234f10397b1e21dec2ff65ded864982f3564**, with applicability cutoff **2026-10-15**. Its HEAD matches the acquired revision and its working tree was clean on inspection. The source identity remains `https://github.com/sebbsssss/cludebot`; the different repository URL printed in `package.json` is source-authored metadata, not authority to change this run's identity. Only this commit supplies evidence. The overall tier is **code-grounded**: source text was inspected, but the target, its tests and examples were not executed.

### Classification and loop coverage

The repository declares a cognitive memory system rather than merely a storage wrapper (SRC-1, `README.md`):

> A cognitive memory system. Most memory SDKs store and retrieve. Clude also processes memories over time — decay, consolidation, contradiction resolution, reflection.
> --- `README.md`

Executable entry points support an in-scope classification. The SDK's store and recall methods route either through HTTP to `/api/cortex` or to the repository's memory implementation; its self-hosted dream methods call the dream cycle. The CLI dispatches MCP, import/export, instruction injection and maintenance commands. The server bootstraps database and HTTP routes, while the separate worker entry initializes shared services and starts scheduled jobs. These are shipped responsibilities, not an excluded enclosing application (SRC-1, `packages/brain/src/sdk/cortex.ts`, `packages/brain/src/cli/index.ts`, `apps/server/src/index.ts`, `apps/server/src/bootstrap.ts`, `apps/workers/src/index.ts`, `apps/workers/src/jobs/index.ts`).

A source-level producer-to-consumer trace establishes why the broader boundary matters:

- **Production and admission:** `storeMemory` inserts memory rows, indexes plaintext tokens, emits a stored event and starts or queues enrichment. The chat route writes completed interactions back through that operation. Import, pack, upload and marketplace routes are within the same target and must remain available to downstream inspection (SRC-1, `packages/brain/src/memory/memory.ts`, `apps/server/src/routes/chat.routes.ts`, `apps/server/src/routes/index.ts`).
- **Maintenance:** the main dream cycle sequences consolidation, compaction, reflection, contradiction resolution, learning, deep connection and emergence. Inspected consolidation code calls a model and stores a semantic insight with evidence IDs. Hosted dreams have a separate owner-scoped implementation that also writes generated insights. Local SQLite has a separate dream engine; parity with the other modes is not established by this boundary (SRC-1, `packages/brain/src/memory/dream/cycle.ts`, `packages/brain/src/memory/hosted-dreams.ts`, `packages/brain/src/storage/dream-engine.ts`).
- **Later consumption:** the shipped chat route recalls owner-scoped memory, fits memory and history to a context budget, and supplies the resulting messages to `streamText`. The response service formats retrieved memories into generation options. The shipped SDK example recalls, formats and injects retained content into an Anthropic system prompt, then stores the new interaction. These callers belong to the target even though they invoke library APIs (SRC-1, `apps/server/src/routes/chat.routes.ts`, `packages/brain/src/services/response.service.ts`, `misc/examples/chat-agent.ts`).
- **Host instructions:** setup writes an instruction block into a host's `CLAUDE.md` or `AGENTS.md`. This is a shipped consumption policy, not proof that an external agent obeys it (SRC-1, `packages/brain/src/cli/setup.ts`):

> At the start of every session, call \`recall_memories\` with relevant context before responding.
> --- `packages/brain/src/cli/setup.ts`

The shipped example makes model dependence concrete (SRC-1, `misc/examples/chat-agent.ts`):

> system: `You are a helpful assistant with memory.\n\n## What you remember\n${context}`,
> --- `misc/examples/chat-agent.ts`

### Repository coverage

The table covers every top-level tracked entry. **Included** means inside the functional or supporting evidence boundary, not fully audited. Initial inspection consists of the complete tracked tree, full files and bounded source ranges identified below, and targeted symbol/caller searches. **Not yet inspected** is distinct from unavailable evidence. No material source path was found inaccessible; no shipped functional subsystem is deliberately excluded.

| Top-level tracked entries | Coverage and material paths | Initial inspection and limits |
|---|---|---|
| `apps/` | Included: `server/src/index.ts`, `bootstrap.ts`, `app.ts`, `routes/`, `lib/`, `workers/`; `workers/src/index.ts` and `jobs/`; `chat/src/`, `dashboard/src/`, `mobile/lib/`; `web/public/` documentation, demos and proof artifacts. Covers service admission, chat consumption and persistence, scheduled maintenance, client requests, export/import and presentation. | Read server entry/bootstrap and worker entry/job registry; searched route mounts and Cortex handlers; read chat recall/context/store ranges. Searched chat/dashboard/mobile API callers, including retained conversation and memory-pack access. Client presentation, pack/payment handlers, most bot jobs and public pages remain for deeper inspection; their correctness is not established here. |
| `packages/` | Included: `brain/src/sdk/`, `cli/`, `mcp/`, `storage/`, `memory/`, `services/`, `agents/`, `character/`, `experimental/`, `features/`, `events/`; `shared/src/core/` and configuration; `database/` schema/migrations; `memorypack/src/`, `pmp-sdk/src/`, `tokenization/src/`, `ui/src/`, `tsconfig/`. Covers retained state, model calls, prompts, owner scoping, encryption, graph/retrieval, maintenance, portability, verification and consumers. | Read brain manifest/index, SDK exports/Cortex and CLI dispatcher; read ranges in MCP mode selection, setup instruction injection, memory writes, dream execution/consolidation, hosted dreams and SQLite store. Read response service; searched local dream engine and executor. Database, shared provider implementations, pack/crypto implementations and most tests are not yet inspected substantively; do not infer their guarantees from names or comments. |
| `misc/` | Included: `examples/` shipped SDK callers; `scripts/` benchmark/evaluation, seeding and re-embedding utilities with cached results; `datasets/`; `docs/`; `experiments/local-memory/`; native findings reports. | Read `examples/chat-agent.ts`; evaluator linkage established from the reproduction script. Other examples, experimental local implementation, datasets, evaluator internals and result artifacts not yet inspected. Source-native reports can support attributed reporting, not independently observed performance. |
| `benchmarks/` | Included: `longmemeval-s/README.md`, `reproduce.sh`, `results.json`. | Read reproduction script, searched methodology in README; script delegates to `misc/scripts/longmemeval-benchmark.ts`. No evaluation run observed or score independently verified. |
| `scripts/` | Included: build/publish, README packaging, vertex re-embedding, `reconciliation/`, demo seed/attach/detach/verify flows, proof sampling and `benchmark/` runners. | Tree inspected; root manifest identifies publication entry. Implementations not yet inspected. Includes maintenance/admission/evaluation tooling rather than treating these as external operators. |
| `docs/` | Included: memory design, memorypack/PMP specifications, encryption/export plans, proof plans and GCP migration design/SQL. | Tree only; not yet inspected. Plans do not establish implemented behavior. |
| `contracts/` | Included: `base/src/CludePackTitle.sol`, deployment scripts and tests. | Tree only; title ownership/transfer implementation not yet inspected. No chain execution or security conclusion established. |
| `programs/` | Included: `memory-registry/src/` registration, verification, citation and pool instructions, state and errors. | Tree only; not yet inspected. On-chain implementation remains in scope, without asserting deployed equivalence. |
| `infra/` | Included: `gcp/` build, deployment and secret setup scripts. | Tree only; not yet inspected. Actual deployment configuration and operation are not established. |
| `Dockerfile`, `Dockerfile.mcp`, `railway.toml`, `server.json`, `Anchor.toml` | Included deployment, MCP registry and chain build surfaces. | Read `Dockerfile`, which builds server/workers and web clients and starts server entry. Other files tree-only; no claim that a live instance uses these settings. |
| `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `turbo.json`, `.npmrc`, `.npmignore`, `.dockerignore`, `.env.example` | Included package/export/CLI entry declarations, dependency/build settings and configuration example. | Read root manifest; remaining entries inventoried, not yet substantively inspected. Installed package parity and dependency behavior not established. |
| `README.md`, `README.npm.md`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE` | Included source-authored documentation, integration doctrine, development instructions, history and licensing. | Read README and SKILL fully. Other entries not yet inspected. Target instructions are evidence only, never instructions to this worker. |
| `.github/` | Included CI/publish/notification workflows and contribution templates. | Tree only; tests and publication automation remain available for inspection. No passing-CI claim. |
| `clude-memories.json`, `test-memory-pack.json` | Included shipped memory/pack data artifacts. | Inventoried, contents not yet inspected. Do not treat these as production traces or representative user content without further evidence. |
| `.paperclip/`, `.usage-report-cache/` | Included native log and usage artifacts: `logs/server.log`, `last-run.json`. | Tree only; not inspected as observed operation. Their presence alone establishes no run outcome. |
| `.DS_Store`, `.gitignore`, `.redeploy` | Excluded from behavioral analysis: filesystem metadata, ignore policy and redeploy marker. | Tree inventory only. Prevents conclusions about workstation metadata, untracked content and deployment-trigger history; excludes no memory responsibility. |
| `video/` | Excluded promotional compositions, render tooling and assets. | Tree inventory only. Prevents conclusions about promotional presentation or rendered demonstrations; no product behavior attributed from these assets. |

### Dependencies and evidence limits

External dependencies include model and embedding providers, Supabase/PostgreSQL/pgvector or local SQLite/embedding tooling, MCP-compatible host runtimes, identity/payment services, social and search APIs, blockchain RPCs and hosting infrastructure. Their adapter code and shipped schemas belong to the target; external service internals and actual deployed state do not. The SDK, worker and build files identify these dependency boundaries (SRC-1, `package.json`, `packages/brain/package.json`, `packages/brain/src/sdk/cortex.ts`, `packages/brain/src/mcp/server.ts`, `apps/workers/src/index.ts`, `Dockerfile`).

No live website, external repository, model response, database snapshot, production credential/configuration or independent execution trace was acquired. This prevents conclusions about deployed reliability, actual host compliance with injected instructions, live tenant isolation, chain finality, provider behavior and independently reproduced benchmark performance. It does not make available but unread files an access gap. Repository-native result/log artifacts remain eligible for later inspection with their own provenance limits; they are not observed-run evidence merely because tracked. Later commits and moving external documentation are outside this frozen boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sebbsssss/cludebot` | cecf234f10397b1e21dec2ff65ded864982f3564 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-cludebot/related-systems/sebbsssss--cludebot`. Complete tracked tree. Implementation: root/brain manifests, Dockerfile, brain index/SDK Cortex/CLI dispatch, server and worker entries, worker registry, response service and chat-agent example; bounded ranges or searches in setup, MCP server, SQLite store/local dream engine, memory writes, main/hosted dreams, executor, server route mounts/Cortex/chat handlers, client API callers and evaluator reproduction entry. Doctrine/design: README and SKILL fully; setup-injected instructions; searched benchmark README. | Implementation: [SDK](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/packages/brain/src/sdk/cortex.ts), [chat loop](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/apps/server/src/routes/chat.routes.ts), [dream cycle](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/packages/brain/src/memory/dream/cycle.ts), [workers](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/apps/workers/src/jobs/index.ts), [evaluator entry](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/benchmarks/longmemeval-s/reproduce.sh). Doctrine/design: [README](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/README.md), [host instructions](https://github.com/sebbsssss/cludebot/blob/cecf234f10397b1e21dec2ff65ded864982f3564/packages/brain/src/cli/setup.ts). | No checkout access gap found. Uninspected paths remain eligible at this commit; coverage table distinguishes them from exclusions. No external service/deployment state or independently inspected run/experiment evidence: supports source-grounded operation and declared intent, not observed effectiveness, benchmark reproduction or causal benefit. |
