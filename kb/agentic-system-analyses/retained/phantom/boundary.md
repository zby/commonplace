---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Phantom's shipped agent service, interfaces and persistence loops at commit f8c7ab42d885936ee54abc785528000260f4acc5."
run-id: AAS-2026-10-15-phantom-cc566f03ac40-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "f8c7ab42d885936ee54abc785528000260f4acc5"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/ghostwright/phantom
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/phantom-cc566f03ac40/related-systems/ghostwright--phantom
  revision: f8c7ab42d885936ee54abc785528000260f4acc5
  sha256: null
---

# Phantom boundary

## Boundary and evidence

This run examines Phantom as a deployed autonomous co-worker service, not merely its memory API or SDK wrapper. Intended use is to establish how the shipped service admits work, calls models and tools, retains state, maintains learned content and supplies that content to later work. The target class is **enclosing runtime**: Phantom owns service startup, ingress, session coordination, prompt construction, persistence, scheduled work and learning orchestration. It delegates the inner model/tool execution loop to a selectable Agent SDK. The boundary is **whole-system** at the repository revision, not a claim that dependency internals or a cloud deployment have been inspected. [SRC-1: `package.json`, `src/index.ts`, `src/agent/runtime.ts`, `src/agent/agent-sdk.ts`, `src/agent/agent-sdk-loader.ts`]

The project's declared composition is:

> Phantom is a single Bun process that runs on a VM. It combines an agent runtime, memory system, self-evolution engine, MCP server, and multi-channel communication into one process.
> --- `docs/architecture.md`

### Entry points and state-loop coverage

The executable chain is `package.json`'s `phantom` bin → `src/cli/main.ts` → `src/cli/index.ts` → `src/cli/start.ts` → `src/index.ts`. The direct `start` script and Docker entrypoint also reach `src/index.ts`. These shipped drivers are included, not treated as external callers. Startup wires the database, vector memory, evolution engine and cadence, MCP tools, scheduler, channel router, web-chat stores and HTTP service. [SRC-1: `package.json`, `src/cli/main.ts`, `src/cli/index.ts`, `src/cli/start.ts`, `scripts/docker-entrypoint.sh`, `src/index.ts`]

> // Import and run main directly
> await import("../index.ts");
> --- `src/cli/start.ts`

Functional inclusions cover these distinct paths; their existence does not establish identical learning behavior across ingress types:

- **Channel work and post-response learning:** the router callback calls `runtime.handleMessage`, delivers its response, invokes vector-memory consolidation when ready, and submits session summaries to evolution. Feedback has a separate evolution submission path. [SRC-1: `src/index.ts`, `src/memory/consolidation.ts`, `src/evolution/engine.ts`]
- **Web chat and later consumption:** startup wires dedicated chat stores and a handler rather than routing its hot path through the channel callback. `ChatSessionWriter` persists user/assistant messages, stream events and durable run timelines, and calls `runtime.runForChat` with context rebuilt from retained events and timeline artifacts. Web chat remains inside the boundary; the channel callback's post-response learning must not be attributed to it without tracing its own callers. [SRC-1: `src/index.ts`, `src/chat/http-handlers.ts`, `src/chat/writer.ts`, `src/chat/continuity-context.ts`]
- **Other admitted work:** scheduler execution and the HTTP trigger call the runtime directly. Their inclusion prevents treating the router callback as the only driver. [SRC-1: `src/scheduler/executor.ts`, `src/core/server.ts`]
- **Vector memory:** consolidation creates episodes and heuristically extracted facts; the context builder recalls facts, episodes and procedures under a prompt budget. This is distinct from file reflection. [SRC-1: `src/memory/consolidation.ts`, `src/memory/context-builder.ts`]
- **File memory and maintenance:** evolved configuration, agent-written notes, working memory, SDK user/project settings, dashboard memory-file editing, installed skills and the reflection teaching prompt are included. The assembler injects evolved sections and instructions, while agent notes are deliberately left for tool-mediated reading rather than automatic injection. [SRC-1: `src/agent/prompt-assembler.ts`, `src/agent/prompt-blocks/evolved.ts`, `src/agent/prompt-blocks/agent-memory-instructions.ts`, `src/agent/runtime.ts`, `src/memory-files/paths.ts`, `src/memory-files/storage.ts`, `scripts/docker-entrypoint.sh`]
- **Learning admission and refresh:** the evolution gate feeds a persistent queue; the reflection subprocess writes permitted files, checks post-state and commits or restores snapshots. Startup registers a callback that refreshes the live runtime's evolved configuration after applied changes. Shipped tests and evaluators are included as executable specifications, not test results. [SRC-1: `src/evolution/engine.ts`, `src/evolution/reflection-subprocess.ts`, `src/index.ts`, `e2e/reflection-subprocess.spec.ts`, `.github/workflows/ci.yml`]

Two short passages establish that the inspected boundary reaches both admission control and subsequent consumption, rather than ending at a write API:

> if (!invariant.passed) {
> restoreSnapshot(input.config, snapshot);
> --- `src/evolution/reflection-subprocess.ts`

> engine.setOnConfigApplied(() => {
> runtime.setEvolvedConfig(engine.getConfig());
> });
> --- `src/index.ts`

### Top-level tracked coverage

The tracked tree was enumerated at the pin. Every top-level tracked entry is classified below. “Included” means within the functional/evidence boundary, not that every file has already been read. Initial inspection is identified separately; unread available material is not an access gap. All paths in this table belong to SRC-1.

| Top-level entry | Classification | Material paths, role and initial inspection | Exclusion limit |
|---|---|---|---|
| `.dockerignore` | Included; not yet inspected | Build-context selection. | None; no detailed build-context conclusion yet. |
| `.env.example` | Included; not yet inspected | Deployment/configuration example. | None; no exhaustive environment-variable account yet. |
| `.github/` | Included | Read `.github/workflows/ci.yml`: lint, typecheck, migration safety, tests, UI build and external fixture drift check. Docker publishing and issue templates remain uninspected. | None; CI configuration is not evidence of a passing run. |
| `.gitignore` | Excluded | Version-control hygiene; enumerated only. | No conclusion about ignored local deployment state. |
| `CLAUDE.md` | Included; not yet inspected | Repository-local development/agent instructions; not assumed to be the deployed user's instruction file. | None; its precise SDK relevance remains to be checked. |
| `CODE_OF_CONDUCT.md` | Excluded | Community policy; enumerated only. | No assessment of community governance. |
| `CONTRIBUTING.md` | Excluded | Contributor procedure; enumerated only. | No assessment of contribution workflow. |
| `DEPLOY-WITH-CLAUDE.md` | Included; not yet inspected | Agent-assisted deployment instructions. | None; no claim of deployment parity from this document. |
| `Dockerfile` | Included | Searched build stages, dependency installation, skills/config copying, default backups and runtime user; includes the chat UI build. | None; image not built. |
| `LICENSE` | Excluded | License text; enumerated only. | No legal/licensing assessment. |
| `README.md` | Included; not yet inspected | Product and operator-facing entry documentation. | None; initial declared architecture comes from `docs/architecture.md`. |
| `SECURITY.md` | Included; not yet inspected | Security disclosure/operational policy. | None; no security-audit conclusion. |
| `biome.json` | Included; not yet inspected | Static-check configuration. | None; checks not run. |
| `bun.lock` | Included; not yet inspected | Locked server dependency graph. | None; exact transitive implementation not established. |
| `bunfig.toml` | Included; not yet inspected | Bun tooling/runtime configuration. | None; no detailed tooling conclusion. |
| `chat-ui/` | Included | Searched `chat-ui/src/hooks/use-chat.ts` and `chat-ui/src/lib/client.ts`: stream, abort and resume consumers; tree includes session UI, durable client state, tests and build configuration. Component bodies remain mostly uninspected. | None; no browser-behavior or visual-quality result. |
| `config/` | Included | Read `config/evolution.yaml`; searched `config/memory.yaml`. Includes `phantom.yaml`, `channels.yaml`, `mcp.yaml`, `roles/`, curated plugins: shipped configuration and role inputs. Other bodies remain uninspected. | None; no claim all defaults are active in any deployment. |
| `docker-compose.quick.yaml` | Included; not yet inspected | Alternate deployment topology. | None; topology parity not yet established. |
| `docker-compose.user.yaml` | Included; not yet inspected | Alternate user deployment topology. | None; topology parity not yet established. |
| `docker-compose.yaml` | Included | Read full stack, service dependencies and persistent config/data/public/credential volumes. | None; persistence configuration is not a recovery experiment. |
| `docs/` | Included | Read `docs/architecture.md`; tree identifies `memory.md`, `self-evolution.md`, providers, MCP, roles, channels, security and deployment guides. Other guides/assets remain uninspected. | None; documentation is attributed design, not verified operation. |
| `e2e/` | Included | Inspected setup and assertions in `e2e/reflection-subprocess.spec.ts`; `e2e/chat.spec.ts` identified but not read. Includes model-dependent evaluation drivers. | None; no tests executed and no pass rate established. |
| `package.json` | Included | Read entry points, server scripts and direct dependencies. | None. |
| `phantom-config/` | Included | Enumerated `constitution.md`, persona/profile/domain files, `strategies/`, `memory/` and `meta/` including golden-suite/version/metrics/log seeds. Read their consumers and reflection permissions; seed bodies not yet inspected. | None; filenames and seed logs alone establish no production learning or evaluation result. |
| `prompts/` | Included; not yet inspected | Shipped development/research task prompts, including memory and continuity work. They are not assumed to be active runtime prompts; active prompt construction was read under `src/agent/` and `src/evolution/`. | None; no prompt-to-runtime equivalence claimed. |
| `public/` | Included | Searched `public/dashboard/memory-files.js` list/read/edit/delete calls. Includes dashboard settings, evolution, memory, skills, sessions, generated-page examples and static shells. Other bodies remain uninspected. | None; operator state mutation remains in scope. |
| `research/` | Included; not yet inspected | Target-authored chat/continuity implementation, review and verification records. May supply attributed reported operation if later inspected, not independent findings. | None; no operational claim imported from these records. |
| `scripts/` | Included | Searched `docker-entrypoint.sh`, `install.sh`, `install-phantom-ui-skill.sh`: startup, baseline preservation, skill seeding and service launch. Includes `scripts/skills/phantom-ui.md` and VM deploy driver; those bodies remain uninspected. | None; installed host state not captured. |
| `skills-builtin/` | Included | Tree includes echo, list-plugins, mirror, overheard, ritual, show-my-tools and thread. Searched `skills-builtin/thread/SKILL.md` memory retrieval instructions; seeding traced in entrypoint. Other skill bodies remain uninspected. | None; instruction presence does not establish successful use. |
| `slack-app-manifest.yaml` | Included; not yet inspected | Slack application integration contract. | None; no live Slack configuration verified. |
| `src/` | Included | Read all `src/index.ts`, CLI dispatch/start, SDK boundary/loader, prompt assembler and selected prompt blocks, consolidation/context builder, chat writer and selected continuity code, evolution engine/subprocess ranges, memory-file paths/storage ranges. Searched HTTP/chat admission, scheduler executor, dashboard configuration/storage and invariant paths. Tree also includes `channels/`, `core/`, `db/`, `email/`, `hooks/`, `integrations/`, `mcp/`, `onboarding/`, `persona/`, `plugins/`, `roles/`, `secrets/`, `shared/`, `skills/`, `subagents/`, `tenancy/`, `ui/`, `utils/` and subsystem tests. These service/tool/state responsibilities are all included; detailed internals beyond initial traces remain for downstream analysis. | None; enumeration and selected traces are not exhaustive correctness or security review. |
| `tsconfig.json` | Included; not yet inspected | Server typechecking configuration. | None; typechecking not run. |

### Frozen evidence and external limits

The acquired checkout's HEAD was verified as `f8c7ab42d885936ee54abc785528000260f4acc5`; its status was clean. This exact Git object is the sole frozen source. `analysis-cutoff` is the supplied run date, **2026-10-15**, not a claim that the revision reflects subsequent upstream changes. Evidence tier is **code-grounded**: source text establishes implemented branches and wiring; target documentation establishes declared intent. No target code, examples, tests, providers or services were executed.

External dependencies are not omitted Phantom subsystems. The Anthropic Agent SDK, optional Murph-compatible runtime/module override, model providers, Qdrant, Ollama, Bun/SQLite, browser/MCP packages and channel/email services supply external execution or storage. Phantom's configuration, invocation, adapters and consumption of them are included; their own implementation is not in this source. This prevents conclusions about provider internals, SDK-enforced sandbox effectiveness, storage durability under failure or end-to-end model quality. [SRC-1: `package.json`, `src/agent/agent-sdk.ts`, `src/agent/agent-sdk-loader.ts`, `src/evolution/reflection-subprocess.ts`, `docker-compose.yaml`]

Cloud fleet provisioning, metadata gateway/server implementations and the external `phantom-cloud-deploy` fixture are not frozen here. Shipped metadata clients, readiness wiring, identity overlays and CI references remain included. The external gap prevents conclusions about fleet isolation, provisioning correctness and cross-repository fixture agreement. [SRC-1: `src/index.ts`, `.github/workflows/ci.yml`]

No independent execution trace or causal experiment has been registered. Available but unread target-authored verification records are not access gaps and are not silently counted as observed runs. This boundary supports source-grounded analysis of the shipped service, not claims of successful deployment, learning benefit or cross-channel learning equivalence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ghostwright/phantom` | f8c7ab42d885936ee54abc785528000260f4acc5 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/phantom-cc566f03ac40/related-systems/ghostwright--phantom`. Implementation: tracked tree; complete CLI dispatch/start, startup wiring, SDK integration/loader, prompt assembler, selected prompt blocks, vector consolidation/context builder, chat writer, memory-file paths; selected continuity, evolution engine/reflection, admission, dashboard, deployment and evaluator ranges as itemized above. Doctrine/design: `docs/architecture.md`, `config/evolution.yaml`, reflection teaching prompt and main-agent memory instructions; selected skill instructions and comments. No observed-run or causal-experiment layer claimed. | Implementation: [entry scripts](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/package.json), [service wiring](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/index.ts), [runtime](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/runtime.ts), [chat persistence](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/chat/writer.ts), [reflection admission](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/reflection-subprocess.ts), [memory retrieval](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/context-builder.ts). Doctrine/design: [architecture](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/docs/architecture.md), [maintenance instructions](https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/subprocess-prompt.ts). | No repository access gap found. External dependency implementations, live deployment state, cloud control plane and independent execution evidence are not supplied: no end-to-end efficacy, deployed security, recovery or fleet correctness conclusion. Unread available files remain eligible at this same pin, not missing evidence by inaccessibility. |
