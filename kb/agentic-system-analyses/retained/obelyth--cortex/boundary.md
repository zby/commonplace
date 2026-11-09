---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Cortex's shipped memory service, dashboard, maintenance instructions and evaluators at commit 65d449a3275eee51efd6ce0c275572806ee9d553."
run-id: AAS-2026-11-07-cortex-6101286707a0-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "65d449a3275eee51efd6ce0c275572806ee9d553"
analysis-cutoff: "2026-11-07"
evidence-tier: code-grounded
source:
  identity: https://github.com/obelyth/cortex
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/cortex-b09108a35d0c/related-systems/obelyth--cortex
  revision: 65d449a3275eee51efd6ce0c275572806ee9d553
  sha256: null
---

# Cortex boundary

## Boundary and evidence

This run examines Cortex as a shipped memory system, not merely its MCP library API. The intended use is to explain how private Markdown notes and working state enter storage, become context or model inputs, and are maintained across sessions and surfaces. The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system**: it includes the Next.js application, MCP tools, dashboard callers, storage adapters and schemas, maintenance procedures, setup and import drivers, and evaluation tooling in this repository. It does not classify Cortex as the enclosing runtime of every connected assistant. SRC-1, `README.md`, `package.json`, `lib/handler.ts`, `lib/tools.ts`.

The source declares this product boundary directly:

> Cortex is a self-hosted AI memory system for private Markdown notes. Its
> protected dashboard lets you inspect and operate that memory. Its Model Context
> Protocol (MCP) server gives compatible AI clients a standard way to read it and,
> when trusted, write to it.
> --- `README.md`

Its durable and database-backed state have different recovery boundaries:

> Cortex keeps durable notes in a private GitHub repository you control. Note writes become Git commits. An optional Supabase database adds a rebuildable notes mirror, working notes, device records, and operations history. Working notes and operations records are not recoverable from the notes repository, so back up that database separately.
> --- `README.md`

The in-scope loop is not confined to one request handler. The ordinary bearer route and trusted secret-URL alias call the shared handler; the guest alias calls its guest variant. That handler registers tools from `lib/tools.ts`. Trusted writes and captures reach `lib/brain.ts`, which writes through GitHub and attempts index regeneration. Subsequent requests reload a corpus through `lib/corpus.ts`; context and handoff surfaces serve retained content to callers. The MCP ask path loads the corpus, consults answer caching, and invokes `ask` with `modelReader`. The dashboard's Ask route is also a shipped consumer of that reader path, while its working-state route calls the working-state service backed by the bubble store. These are included callers, not excluded host applications. SRC-1, `app/api/[transport]/route.ts`, `app/api/s/[secret]/[transport]/route.ts`, `app/api/g/[secret]/[transport]/route.ts`, `lib/handler.ts`, `lib/tools.ts`, `lib/brain.ts`, `lib/corpus.ts`, `lib/handoff.ts`, `app/s/[secret]/console/ask/run/route.ts`, `app/s/[secret]/console/working-state/route.ts`, `lib/working-state.ts`.

The system qualifies even though several context tools are deterministic: its Ask path explicitly serves model calls over retained notes. In the inspected implementation, prompt construction precedes the injected reader call, and the reply is checked against the loaded corpus. This establishes code-level model dependence, not successful live operation. SRC-1, `lib/ask.ts`:

> raw = await read({ stable, question: variable }, model, { timeoutMs: readerMs });
> --- `lib/ask.ts`

The groundskeeper is part of the shipped maintenance design. Its external scheduling host is not supplied as a running service, but its prompt is not excluded merely because a client must execute it. It instructs a model-driven caller to read daily logs, file durable items into notes, check drift, review proposals and capture a digest using the server's tools. SRC-1, `ops/groundskeeper/SKILL.md`:

> This is a TEMPLATE: fill in the <angle-bracket> paths, then
> register it as a scheduled task in Claude Code.
> --- `ops/groundskeeper/SKILL.md`

The evaluator is also in scope as a shipped consumer of the product path, not evidence that an evaluation was performed. Its implementation calls `ask` using `modelReader`, loads a corpus and external labels, and writes scored results. Retrieval and prediction evaluators are included for subsequent inspection of their own measurement boundaries. SRC-1, `scripts/eval.ts`, `scripts/eval-retrieval.ts`, `scripts/eval-prediction.ts`.

### Frozen evidence and exclusions

The only frozen source is SRC-1 at **65d449a3275eee51efd6ce0c275572806ee9d553**, with applicability cutoff **2026-11-07**. The acquired checkout's HEAD was verified against that commit. The evidence tier is **code-grounded**; documentation and prompts supply attributed design intent alongside implementation text. No target program, test, setup wizard, maintenance job or evaluator was executed. There is no observed-run or causal-experiment evidence in this boundary.

The source tree is available read-only. There is no known inaccessible material shipped path. Initial inspection is selective: the coverage table distinguishes inspected paths from available paths retained for later analysis. Inclusion is a functional scope declaration, not a claim that every source line has already been inspected.

External dependencies include GitHub for the private notes repository and application operations, optional Supabase/Postgres for database state, optional Upstash for KV state, reader model providers, Vercel/deployment infrastructure and optional alert email delivery. Their adapter code, contracts and shipped workflow configuration are included; their service implementations and actual account permissions are not frozen. The private notes repository, live working state, deployment secrets, external evaluator labels, and production execution histories are not supplied. This prevents claims about a particular installation's corpus, recall, answer quality, operational reliability, actual maintenance execution, provider delivery or end-to-end recovery. The generic MCP clients and Claude Code scheduler are external hosts: their independent conversation management, model policies and scheduling guarantees cannot be attributed to Cortex. SRC-1, `README.md`, `package.json`, `ops/groundskeeper/SKILL.md`, `ops/heartbeat/README.md`, `scripts/eval.ts`.

### Top-level tracked coverage

Every top-level tracked file or directory is classified below. Grouped file rows apply to each named file. “Available” means not an access gap and not evidence of inspected behavior. Directory rows identify the material paths and responsibilities that remain in scope.

| Top-level tracked path(s) | Classification and role | Initial inspection / exclusion limit |
| --- | --- | --- |
| `app/` | Included: MCP routes under `app/api/`; Ops report and sweep routes; protected dashboard under `app/s/[secret]/console/`, including Ask, working-state, proposals, attention, configuration and operations; root and health/map entry pages. | Tree inspected; all three MCP routes and console Ask route read; working-state and sweep wiring searched. Other pages and routes available, not yet inspected in detail. No dashboard state producer or consumer is deliberately excluded. |
| `lib/` | Included: `handler.ts`, `tools.ts`, `brain.ts`, `github.ts`, `proposal-git.ts`, `proposals.ts`, `corpus.ts`, `mirror.ts`, `bubble.ts`, `working-state.ts`, context/handoff, selection, ask/reader/verify, edges/access/prediction, settings/auth/guest, and Ops/configuration/job adapters. | Handler read; tool and brain write/capture excerpts inspected; corpus, handoff, proposals, working-state and reader wiring searched; ask packing/call/verification tail inspected. Remaining implementation available for later mechanism tracing. |
| `ops/` | Included: `groundskeeper/SKILL.md` and `healthcheck.sh`; `heartbeat/` reporter, service and timer; `routines/report.sh`. Maintenance instructions and operational drivers. | Groundskeeper prompt and heartbeat README read; scripts/service entry points searched. No actual scheduled job or installed timer supplied. |
| `scripts/` | Included: onboarding/bootstrap/update/import drivers; `ingest.mjs`, `backfill-descriptions.ts`, `split-project-page.ts`, `build-edges.ts`, `lifecycle-sweep.ts`; `eval.ts`, `eval-retrieval.ts`, `eval-prediction.ts`, lexical benchmarks and supporting utilities. | Reader evaluator and lifecycle sweep read; ingest, edge builder and other evaluator wiring searched; remaining drivers available. Source contracts do not establish executed imports, measurements or upgrades. |
| `supabase/` | Included: `bootstrap.sql` and `migrations/`, defining mirror/sync, working state, access and edges, retirement nominations, device/operations/job/configuration state. | Tree and bootstrap declarations searched; full SQL bodies and migration ordering remain available for detailed inspection. No deployed schema or data supplied. |
| `brain-template/` | Included: `.gitignore`, `INDEX.md`, `profile.md`, the shipped blank-brain seed. | Tree and README setup contract inspected; file bodies available, not yet inspected. Not a private operational corpus. |
| `tests/` | Included: unit, route, integration, optional Postgres and evaluation-integrity tests plus helpers; especially brain/corpus, proposal, working-state, learning, handoff and evaluator tests. | Test tree inspected; test bodies available, not yet inspected. Assertions are not passing-run evidence. |
| `docs/` | Included: database/bootstrap, export, Codespaces and GitHub setup guides, releases, wiki and learning-layer design specification. | Tree inspected; document bodies available, not yet inspected. Historical design requires checking against executable code. |
| `.github/` | Included: dependency documentation, release/setup automation, CI and `workflows/cortex-dashboard-checks.yml`, plus repository templates. The dashboard workflow is a shipped operational integration, not an external caller. | Tree and README operational prerequisites inspected; workflow bodies available, not yet inspected. No hosted Actions result supplied. |
| `README.md` | Included: current product, storage, access, deployment and recovery contracts. | Read completely. |
| `DESIGN.md`, `ROADMAP.md`, `SECURITY.md`, `CONTRIBUTING.md` | Included: declared design, future intentions, security and contributor contracts. | Available, not yet inspected; no present implementation claim is based on their titles. |
| `.env.example` | Included: provider, storage, credential and configuration contract. | Available, not yet inspected; prerequisites initially traced through README and package manifest. |
| `Cortex Setup.command`, `Cortex Setup.sh` | Included: packaged setup entry points, with bootstrap/onboarding consumers in `scripts/`. | Listed and described by the inspected README; shell bodies available, not yet inspected. No installation outcome established. |
| `package.json`, `package-lock.json` | Included: command entry points and dependency boundary. | Manifest read; lockfile available, not yet inspected. Dependency versions do not freeze remote service behavior. |
| `vercel.json` | Included: scheduled `/api/ops/sweep` entry point. | Read; sweep route wiring searched. Configuration is not proof that cron ran. |
| `instrumentation.ts`, `sentry.server.config.ts`, `next.config.ts` | Included: application initialization, monitoring and framework configuration. | Available, not yet inspected. |
| `tsconfig.json`, `vitest.config.ts`, `sonar-project.properties` | Included: compilation and evaluation/static-analysis configuration. | Available, not yet inspected; no quality-gate outcome inferred. |
| `.devcontainer/` | Included: `devcontainer.json`, development environment setup. | Tree inspected; configuration available, not yet inspected. |
| `.gitignore` | Included: repository file-retention configuration. | Available, not yet inspected. |
| `public/` | Excluded from functional mechanism analysis: `brand/`, favicon and font license assets. | Deliberate exclusion; prevents assessment of visual branding and asset licensing compliance, not memory-state behavior. |
| `CODE_OF_CONDUCT.md`, `LICENSE`, `THIRD_PARTY_NOTICES.md` | Excluded from functional mechanism analysis: governance and licensing text. | Deliberate exclusion; prevents legal/compliance or community-governance conclusions. |

Coverage classification and path existence use SRC-1's tracked tree. Responsibility claims above are anchored by SRC-1, `README.md`, `package.json`, `lib/handler.ts`, `lib/tools.ts`, `lib/brain.ts`, `lib/ask.ts`, `ops/groundskeeper/SKILL.md`, `scripts/eval.ts`, `scripts/lifecycle-sweep.ts`, `supabase/bootstrap.sql` and `vercel.json`. Available-but-uninspected material remains inside the evidence boundary; later source inspection at this same commit does not require a new source identity.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/obelyth/cortex` | 65d449a3275eee51efd6ce0c275572806ee9d553 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/cortex-b09108a35d0c/related-systems/obelyth--cortex`. Implementation: tracked tree; `package.json`; `lib/handler.ts`; three MCP route files; `lib/tools.ts` excerpts; `lib/brain.ts` write/capture excerpts; `lib/ask.ts` selection/call/verification/rendering excerpts; corpus, reader, proposals, handoff and working-state wiring; dashboard Ask route; working-state/sweep wiring; `vercel.json`; `scripts/eval.ts`; lifecycle sweep; ingest/edge-builder/evaluator wiring; bootstrap SQL declarations; Ops shell/service wiring. Doctrine/design: `README.md`, `ops/groundskeeper/SKILL.md`, `ops/heartbeat/README.md`. | Implementation: [manifest](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/package.json), [tools](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/lib/tools.ts), [brain](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/lib/brain.ts), [ask](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/lib/ask.ts), [evaluator](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/scripts/eval.ts). Doctrine/design: [README](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/README.md), [groundskeeper](https://github.com/obelyth/cortex/blob/65d449a3275eee51efd6ce0c275572806ee9d553/ops/groundskeeper/SKILL.md). | No known source-tree access gap. Private corpus, runtime database, provider accounts, external hosts, labels and execution results are not supplied: implementation supports source-level behavior only; doctrine supports declared procedure, not actual scheduling, effectiveness, successful operation or causal benefit. |
