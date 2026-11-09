---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "WikiBrain's shipped knowledge-system loop at Git commit 32cc135877c8d7cd7be997ce57f25bb83128d891, including server agents, MCP, templates and web consumers."
run-id: AAS-2026-11-08-wikibrain-f815b0976cda-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "32cc135877c8d7cd7be997ce57f25bb83128d891"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/wikibrain-app/wikibrain
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/wikibrain-181c7af9a7e1/related-systems/wikibrain-app--wikibrain
  revision: "32cc135877c8d7cd7be997ce57f25bb83128d891"
  sha256: null
---

# WikiBrain boundary

## Boundary and evidence

This run analyses the shipped WikiBrain knowledge system, not just its MCP API. Its intended use is to retain sources, compile and maintain a linked wiki, and reuse that wiki in subsequent queries and edits. The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system** for the public repository at the frozen commit. It includes the built-in model-call runners as well as the tools served to external AI clients. Those clients' private orchestration is not attributed to WikiBrain. [SRC-1: `README.md`, `src/mcp.ts`, `src/ingest.ts`, `src/chat.ts`, `src/ai/providers.ts`]

The repository declares its knowledge-layer contract:

> 1. **raw/** holds immutable sources. New material lands here first with front-matter `source_type`, `fetched_at` and, when available, `source_url` and bibliography.
> 2. **wiki/** holds compiled pages that you maintain: source summaries, entity pages, concept pages, comparisons, syntheses. One topic per page; name pages by concept.
> 3. **schema/** holds the rules. Humans own this layer; suggest changes, do not rewrite it yourself.
> --- `templates/general/en/schema/instructions.md`

This is doctrine/design evidence, not proof of model compliance. Executable paths make the target model-dependent rather than merely a Markdown store: the server starts ingest, lint and chat jobs; the job runner supplies workspace tools to provider-specific model loops. [SRC-1: `src/ingest.ts`, `src/chat.ts`, `src/ai/providers.ts`]

> const r = await runAgent({ provider: cfg.provider, model: cfg.model, apiKey: cfg.apiKey, system: spec.system, user: spec.user, history: spec.history, tools: TOOLS, exec: makeExec(ws, spec.actor), maxSteps: spec.maxSteps ?? MAX_STEPS, onEvent });
> --- `src/ingest.ts`

### Functional coverage

The shipped entry point is the package start command, `node dist/server.js`, compiled from `src/server.ts`. It applies migrations, schedules maintenance, marks interrupted jobs failed and mounts the Express application. That application serves the web API, imports, authenticated MCP and the built frontend. The API dispatches ingest/lint/chat and answer filing; these are shipped callers, not excluded hosts. [SRC-1: `package.json`, `src/server.ts`, `src/app.ts`, `src/api.ts`]

The initial trace follows state production through `saveSource` into `createNote`; template application also seeds stored rule and wiki pages. `createNote` and `updateNote` persist Markdown and invoke derived-state writing. Subsequent `readNote`, `searchNotes` and `getInstructions` reload workspace content. The latter queries stored schema pages and prepends pending sources. MCP and server agents share these note functions, while the web workspace reloads notes and job results. This includes the production-to-later-consumption loop rather than stopping at an API definition. [SRC-1: `src/import.ts`, `src/templates.ts`, `src/notes.ts`, `src/mcp.ts`, `src/ingest.ts`, `web/src/pages/Workspace.tsx`]

Chat adds a separate retained conversation path: it loads a session, forwards its prior messages as history to a new job, persists the reply, and can file an answer into the wiki. Its browser caller sends messages, reloads completed sessions and invokes answer filing. [SRC-1: `src/chat.ts`, `web/src/components/ChatPanel.tsx`, `web/src/lib/api.ts`]

> const history = session.messages.map(m => ({ role: m.role, content: m.content }));
> --- `src/chat.ts`

Maintenance belongs inside the boundary: structural lint reads stored pages and links; model-backed lint can write repairs and a report. Template rule updates compare delivered rules with current workspace content and can merge or replace them. Version retention removes old non-current snapshots. The startup path also schedules Zotero synchronization. These paths are included, not assumed to be performed by an external agent. [SRC-1: `src/lint.ts`, `src/ingest.ts`, `src/templates.ts`, `src/retention.ts`, `src/server.ts`, `src/zotero.ts`, `web/src/components/RuleUpdates.tsx`]

### Top-level tracked coverage

The table accounts for every top-level tracked file or directory at the pin. “Included” means within the functional/evidence boundary, not that every leaf has already been read. Initial inspection traced the material loop above; remaining available source can be inspected at this same pin. Uninspected material is distinguished below from unavailable evidence and deliberate exclusions. All rows refer to SRC-1; paths are commit-relative.

| Top-level path | Status | Role, material paths and initial inspection | Limit or conclusion prevented |
|---|---|---|---|
| `.dockerignore` | Included; not yet inspected | Container build inputs/filtering; deployment entry inspected in `Dockerfile`. | No detailed claim about excluded build files yet. |
| `.env.example` | Included; not yet inspected | Configuration surface for service dependencies. | No exhaustive configuration-default assessment yet. |
| `.github/` | Included; partly inspected | `.github/workflows/test.yml` builds and runs backend tests with PostgreSQL; issue templates remain uninspected. | CI definition is not a successful CI execution trace. |
| `.gitignore` | Excluded deliberately | Repository hygiene, not a state producer or consumer. | No assessment of ignored developer artifacts. |
| `.nvmrc` | Included; not yet inspected | Node version selector consumed by CI; `package.json` and `Dockerfile` independently specify Node 24. | Exact selector contents not assessed. |
| `CONTRIBUTING.md` | Excluded deliberately | Contributor process rather than deployed knowledge operations. | No conclusion about contribution governance. |
| `DEPLOY.md` | Included; not yet inspected | Deployment instructions; shipped Docker entry and compose wiring inspected independently. | No complete deployment-procedure assessment yet. |
| `Dockerfile` | Included; inspected | Builds server and web, ships templates and migrations, starts server; bundles Chromium for import. | Source wiring does not establish a successful build or deployment. |
| `LICENSE` | Excluded deliberately | Legal terms, not knowledge-loop implementation. | No legal interpretation. |
| `README.md` | Included; inspected | Declared architecture, intended use and client setup. | Product statements remain attributed design claims. |
| `SECURITY.md` | Included; not yet inspected | Security policy context, not a substitute for enforcement code. | No security-policy assessment yet. |
| `docker-compose.yml` | Included; inspected | App/database startup, persistent PostgreSQL volume, key secret and service configuration. | No observed persistence or recovery outcome. |
| `docs/` | Included; tree inspected, diagrams not yet inspected | Architecture and knowledge-flow SVGs in `docs/diagrams/`; README references them. | No independent diagram-derived conclusions yet. |
| `migrations/` | Included; partly inspected | `migrations/001_phase1_schema.sql` defines workspace notes, versions, links, tags and tokens; later migrations include AI jobs, chat, templates, shares and account plans. | Later schema details require their own inspection, not inference from filenames. |
| `ops/` | Included; partly inspected | `ops/backup/verify.sh` defines a database restore drill; `ops/backup/backup.sh` and `ops/backup/Dockerfile` remain available but uninspected. | Drill source is not a completed recovery test; backup implementation details not established yet. |
| `package-lock.json` | Included; not yet inspected | Locked dependency graph. | No dependency audit or exact transitive-version conclusion. |
| `package.json` | Included; inspected | Build/start/test entry points and declared dependencies. | Declaration is not installed dependency evidence. |
| `scripts/` | Included; tree and consumers inspected, bodies not yet inspected | `scripts/prerender-help.tsx` is called by the build; `scripts/render-diagrams.py` is documented as the diagram generator. | No claims about generated output equivalence. |
| `src/` | Included; material loop inspected | `src/server.ts`, `src/app.ts`, API dispatch in `src/api.ts`; full initial reads of `src/ingest.ts`, `src/chat.ts`, `src/mcp.ts`; persistence/read/rules sections of `src/notes.ts`; loops in `src/ai/providers.ts`; source saving in `src/import.ts`; template application/update sections in `src/templates.ts`; structural checks in `src/lint.ts`; `src/retention.ts`, `src/headless.ts`, `src/ops.ts`; bounded searches trace import and Zotero. Also includes `src/web-api.ts`, auth/workspace/quota enforcement, assets, sharing, export and their supporting modules for later inspection. | Supporting modules not yet inspected are not access gaps. No exhaustive authorization, import-format, billing or renderer correctness claim follows from this initial trace. |
| `templates/` | Included; partly inspected | General, book, PM and researcher templates in English and Traditional Chinese; `templates/general/en/schema/instructions.md` and `templates/general/template.json` inspected; recursive template loader traced. Includes scenario rules, onboarding prompts, index/log and starter content. | General-template quotations do not establish every scenario or translated rule's contents. |
| `test/` | Included; partly inspected | `test/ingest.test.ts` and `test/chat.test.ts` inspected in bounded opening/test sections: mock runners exercise compilation and subsequent query/history/filing. MCP, injection, template rules, retention/account and browser suites are available for later inspection, including `test/e2e/m3_web.py`. | Test definitions are implementation evidence, not observed passing tests or demonstrated real-model knowledge quality. |
| `tsconfig.build.json` | Included; not yet inspected | Server compilation configuration. | No exhaustive compiler-boundary assessment. |
| `tsconfig.json` | Included; not yet inspected | Development/typecheck configuration. | No observed typecheck result. |
| `web/` | Included; material callers searched | `web/src/pages/Workspace.tsx` reads/edits/reloads notes and initiates ingest; `web/src/components/ChatPanel.tsx` reloads sessions and files answers; `web/src/components/IngestPanel.tsx` polls jobs; `web/src/components/RuleUpdates.tsx` admits template rule updates; `web/src/lib/api.ts` wires these operations to server routes. Other editors, import UI, renderers, graphs, settings, help, public assets and build configuration remain included and available. | Search-based caller tracing supports inclusion, not a complete UI, offline-mode or rendering audit. |

### Frozen evidence and external limits

The only frozen source is SRC-1 at commit `32cc135877c8d7cd7be997ce57f25bb83128d891`; its checkout HEAD was verified against acquisition. The analysis cutoff is 2026-11-08, supplied by the run opening. This is a revision-bound source analysis with **code-grounded** evidence, not an observation of the hosted service on that date. No later revisions, live pages, linked upstream design notes or other repositories are admitted.

External dependencies include PostgreSQL, Node/npm packages, model APIs, external AI clients, Chromium and the sites/bibliographic services imported from. Shipped adapters and configuration are included; dependency internals and remote behavior are outside the frozen source. This prevents conclusions about provider reliability, model compliance, client-side planning, third-party security or import coverage in live services. [SRC-1: `package.json`, `docker-compose.yml`, `src/ai/providers.ts`, `src/mcp.ts`, `src/headless.ts`, `src/import.ts`]

The optional hosted operator console is genuinely unavailable: `src/ops.ts` dynamically loads an untracked `src/ops-console.js` and tolerates its absence. The public repository remains a coherent whole-system target, but it is not the full private hosted deployment. The gap prevents conclusions about private operator probes, capacity planning and administrative behavior. Shipped billing, mail and backup code remains in scope despite broader README statements about hosted integrations. [SRC-1: `src/ops.ts`, `src/app.ts`, `src/server.ts`, `README.md`, `ops/backup/verify.sh`]

No target code, examples or tests were executed. No user wiki, production database, model transcript, completed restore drill or experimental comparison was supplied. These are missing execution evidence, not inaccessible repository files. They prevent claims about actual answer quality, long-term knowledge improvement, successful deployment, recovery reliability or causal benefit. The source supports implementation and declared-design accounts only.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/wikibrain-app/wikibrain` | 32cc135877c8d7cd7be997ce57f25bb83128d891 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/wikibrain-181c7af9a7e1/related-systems/wikibrain-app--wikibrain`. Implementation: tracked tree, package/container/CI entry points; server/app; ingest/chat/MCP; note persistence and reload/rules sections; provider loops; source saving; template application/update; structural lint; retention; import browser; optional console loader; bounded API/Zotero and browser-caller searches; opening ingest/chat test sections; initial SQL schema; restore-drill source. Doctrine/design: README, general English schema rules and template metadata. Table above records uninspected available material separately. | Implementation: [server](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/src/server.ts), [jobs](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/src/ingest.ts), [notes](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/src/notes.ts), [chat](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/src/chat.ts), [browser consumer](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/web/src/pages/Workspace.tsx), [test definitions](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/test/ingest.test.ts). Doctrine/design: [README](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/README.md), [rules](https://github.com/wikibrain-app/wikibrain/blob/32cc135877c8d7cd7be997ce57f25bb83128d891/templates/general/en/schema/instructions.md). | Implementation gap: private operator-console implementation absent, so no private hosted-administration assessment. No supplied execution traces or experiments, so no observed-run or causal support. Design limits: instructions and product statements do not establish model compliance or production outcomes. External services and client internals are not frozen here. |
