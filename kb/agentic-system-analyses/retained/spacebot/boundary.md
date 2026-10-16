---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Spacebot's shipped agent runtime and retained-state loop at commit 5c2ee47b397e09c956dc15000ea576ecd28e92bb."
run-id: AAS-2026-10-14-spacebot-6a954b400f95-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "5c2ee47b397e09c956dc15000ea576ecd28e92bb"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/spacedriveapp/spacebot
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/spacebot-6a954b400f95/related-systems/spacedriveapp--spacebot
  revision: "5c2ee47b397e09c956dc15000ea576ecd28e92bb"
  sha256: null
---

# Spacebot boundary

## Boundary and evidence

This run analyses Spacebot as an **enclosing runtime**, not merely its memory API or an OpenCode client. Its intended use is persistent agent operation across conversations, tasks and background work. The boundary is **whole-system**: the repository's shipped runtime, its callers and interfaces, prompts, state stores, maintenance paths and evaluators are included. “Whole-system” describes functional scope, not exhaustive inspection or demonstrated correctness of every file.

The source is SRC-1 at `5c2ee47b397e09c956dc15000ea576ecd28e92bb`, with an applicability cutoff of **2026-10-14**. HEAD matched that revision and the checkout reported no working-tree changes during initial inspection. The overall tier is **code-grounded**. Source text establishes implementation paths; documentation and prompt instructions establish intent. No target executable, test, example, model call or external service was run. Consequently this boundary supplies no observed-run or causal-experiment evidence and establishes neither production reliability nor learning quality.

### Classification and shipped loop

The executable owns startup and channel execution. `Cargo.toml` declares the `spacebot` package and default executable; `src/main.rs` dispatches Start to `cmd_start`, constructs user channels, runs them, and routes their responses to adapters and SSE. The classification rests on these shipped responsibilities, not the project's use of the word “harness” (SRC-1, `Cargo.toml`, `src/main.rs`). A minimum implementation anchor is:

> if let Err(error) = channel.run().await {
>     tracing::error!(%error, "channel event loop failed");
> }
> --- `src/main.rs`

The included loop spans these responsibilities:

- **Admission and execution:** configuration and identity loading, messaging adapters, Portal/API callers, user channels, cron scheduling, durable wakes and autonomy supervision, branches, built-in workers and Spacebot's OpenCode driver. The main executable starts these paths; a caller is not excluded because it uses the library or HTTP API (SRC-1, `src/main.rs`, `src/agent/autonomy.rs`, `src/agent/channel_dispatch.rs`, `src/api/server.rs`, `src/opencode/worker.rs`).
- **State production and persistence:** conversation logging, memory extraction branches, file ingestion, memory-save tools and associations, task/worker lifecycle stores, session chronicles, working memory, skills and instance-wide wiki storage. `src/db.rs` opens per-agent SQLite/LanceDB/redb and instance-level SQLite and applies both migration sets (SRC-1, `src/db.rs`, `src/agent/channel.rs`, `src/agent/ingestion.rs`, `src/tools/memory_save.rs`, `src/wiki/store.rs`).
- **Maintenance and improvement:** compactor and chronicler, cortex loops, the instance memory janitor, write-time consolidation advice, and memory-persistence passes that can reflect on completed work and write skills. Their inclusion does not assert that prompt instructions are always obeyed (SRC-1, `src/main.rs`, `src/agent/compactor.rs`, `src/agent/chronicle.rs`, `src/agent/maintenance.rs`, `src/memory/consolidation.rs`, `prompts/en/memory_persistence.md.j2`).
- **Reload and later consumption:** user channels hydrate durable conversation messages; channel prompt construction renders stored memory and task state, working memory and participant context; the skill loader exposes procedures to later workers. These consumers are inside the boundary rather than assumed external applications (SRC-1, `src/agent/channel.rs`, `src/memory/render.rs`, `src/skills.rs`, `src/prompts/engine.rs`).
- **Operator surfaces and evaluation:** web and desktop clients, shared API client, configuration/admin routes, memory and transcript displays, developer/integration tests and model-dependent behavioral fixtures. Test definitions are evidence of the evaluation design, not results obtained by this analysis (SRC-1, `src/api/server.rs`, `interface/src/api/client.ts`, `desktop/src-tauri/src/main.rs`, `packages/api-client/src/client.ts`, `tests/behavioral_fixtures.rs`).

The retained-state loop is visible at both ends. The persistence prompt declares the extraction responsibility:

> You are a memory persistence process. You have the channel's full conversation history. Your job is to extract and preserve important information as memories.
> --- `prompts/en/memory_persistence.md.j2`

The channel's implemented consumer passes its memory store and task store to the renderer:

> match crate::memory::render::render_memory_store(
>     self.deps.memory_search.store(),
>     &self.deps.task_store,
>     &self.deps.agent_id,
>     cortex_config.memory_render_max_words,
> )
> --- `src/agent/channel.rs`

These passages support inclusion of production and consumption, not a claim that every extracted memory is correct. Skill maintenance instructions and built-in wiki-writing instructions are also runtime content: the binary embeds the built-in skill files through `include_str!` (SRC-1, `src/skills/builtin.rs`, `skills/builtin/wiki-writing/SKILL.md`). Repository-contributor skills under `.agents/` are a different surface.

### Repository coverage

The table accounts for every top-level tracked entry. Included directories name the material responsibilities within them. “Initial inspection” means entry-point tracing, selected bodies or tree/search inspection as stated; it is not a claim to have read every descendant. No material shipped responsibility is excluded because its implementation is large. Unread detail remains available at SRC-1, not an access gap.

| Top-level tracked entry | Scope and role | Initial inspection and conclusion limit |
|---|---|---|
| `src/` | Included: `main.rs` and `cli/` startup/control; `api/` and `messaging/` admission and delivery; `agent/` channels, branches, workers, autonomy, ingestion, cortex, compactor, chronicles and maintenance; `memory/`, `conversation/`, `tasks/`, `wakes/`, `skills/`, `wiki/`, `goals/`, `projects/` retained state; `tools/`, `llm/`, `hooks/`, `prompts/`, `opencode/`, sandbox, secrets, identity, lifecycle and configuration support. `bin/openapi_spec.rs` is a schema-export executable, not another agent host. | Tree/search inspection and selected source bodies traced startup → channel → persistence/reload/render, background maintenance and worker dispatch. API router and schema-export main inspected. Detailed subsystem claims require further pinned-source reads. |
| `migrations/` | Included: per-agent memories, conversations, process runs, working memory, chronicles, identities and worker lifecycle; `global/` instance state. | Migration inventory and both migration invocations in `src/db.rs` inspected; schema details remain available, not independently audited here. |
| `prompts/` | Included: `en/channel.md.j2`, branch/worker prompts, memory persistence and ingestion, compactor/checkpoint/rollup, autonomy/cortex, tool descriptions and instruction fragments. | Inventory, selected channel/worker/memory-persistence text and prompt-engine registrations inspected. Prompts are intent, not proof of execution. |
| `skills/` | Included: `builtin/wiki-writing/SKILL.md` and `builtin/workspace-organization/SKILL.md`, embedded runtime procedures. | Built-in registration and selected wiki-writing text inspected; procedure effectiveness not observed. |
| `presets/` | Included: per-role `IDENTITY.md`, `SOUL.md`, `ROLE.md`, `meta.toml` seed agent definitions. | Tree and main-agent role inspected. Other presets remain available for later source tracing; no equivalence across roles is assumed. |
| `interface/` | Included: `src/api/client.ts`, UI state/Portal/task/memory/worker views and prompt inspector, Vite build, OpenCode embed sources. | Tree, package manifest, request client, build embedding in `build.rs` and static serving in `src/api/server.rs` inspected. No browser session observed. |
| `desktop/` | Included: `src-tauri/src/main.rs`, desktop configuration, packaging and platform code, UI wrapper and voice-overlay integration. | Main's saved-server URL and window entry points inspected. OS integration correctness not tested; it is not treated as an excluded host. |
| `packages/` | Included: `api-client/src/client.ts`, types, events and schema, a shipped client of the same API. | Client request and Portal-history access inspected. Not mistaken for a separate runtime or excluded application. |
| `tests/` | Included: behavioral fixtures, maintenance, context dump, cron, tool-nudge, sandbox and OpenCode integration tests. | Inventory; behavioral fixture design/body and maintenance/context references inspected. No test outcomes established. |
| `docs/` | Included: `content/docs/` shipped system documentation, `design-docs/` design and attributed audit material; documentation-site code as delivery support. | Inventory and selected architecture documentation inspected. Unread design records are not evidence for this member; declarations do not override code. |
| `examples/` | Included: `prometheus.yml` operator integration example. | Tree inspected; not an agent driver. No monitoring deployment validated. |
| `vendor/` | Included: patched `imap-proto-0.10.2` dependency used by the email integration. | Tree and Cargo patch declaration inspected; no vendored parser audit. |
| `Cargo.toml`, `Cargo.lock` | Included: runtime dependency, executable and feature/build identity. | Manifest inspected; lockfile retained as available dependency evidence, not a dependency implementation review. |
| `build.rs` | Included: frontend embedding/build orchestration and version metadata. | Source inspected. No frontend build performed. |
| `docker-entrypoint.sh`, `Dockerfile`, `Dockerfile.cross-aarch64`, `.dockerignore` | Included: container launch/config seeding, packaging and persistent tool-directory conventions. | Entrypoint inspected; packaging inventory. No container behavior demonstrated. |
| `.cargo/`, `Cross.toml`, `rust-toolchain.toml` | Included: compile/link and cross-build configuration. | Tree/manifest context only; no cross-platform compatibility conclusion. |
| `flake.nix`, `flake.lock`, `.envrc`, `nix/` | Included: development/package environment and Nix service/module integration. | Tree inspection; no Nix evaluation or deployment conclusion. |
| `fly.toml`, `fly.staging.toml` | Included: production/staging deployment configuration. | Top-level inventory; not evidence of hosted service operation. |
| `scripts/` | Included: `bundle-docs.sh`, `bundle-sidecar.sh`, `build-opencode-embed.sh` delivery paths; preflight, PR gates, hook installation and release scripts. | Script inventory and build context inspected. No build/release result inferred. |
| `.github/` | Included for workflows `ci.yml`, `interface-ci.yml`, `release.yml`; excluded for decorative/UI image assets. | Tree inspection only. CI success and visual fidelity cannot be concluded. |
| `justfile`, `.githooks/` | Included: developer command/gate entry points. | Inventory only; no claim that gates ran or enforce sufficient coverage. |
| `README.md` | Included: intended use, process model and product claims. | Selected process/state descriptions inspected as doctrine, not benchmarks. |
| `METRICS.md` | Included: instrumentation contract/reference. | Inventory only; no measured performance or cost conclusion. |
| `.agents/`, `AGENTS.md`, `CONTRIBUTING.md`, `RUST_STYLE_GUIDE.md` | Excluded: contributor instructions/skills and coding conventions, not the runtime's embedded procedures. | Contributor skill tree distinguished from `skills/builtin/`; exclusion prevents conclusions about contributor-agent workflow or compliance. |
| `CHANGELOG.md`, `TODO` | Excluded: release history and work backlog as analytical evidence. | Inventory only; exclusion prevents historical-change and roadmap-completion conclusions. |
| `.gitignore`, `LICENSE` | Excluded: repository hygiene and licensing analysis. | Inventory only; exclusion prevents legal/license or ignored-file completeness conclusions. |

### Dependencies and access limits

External services and separately distributed implementations are outside the frozen source: model-provider internals, messaging-platform servers, OpenCode itself, MCP servers, browser/search services, package registries, and hosted Spacebot deployment infrastructure. Spacebot's adapters, provider routing, driver code, policy gates and deployment configuration remain included (SRC-1, `Cargo.toml`, `src/main.rs`, `src/tools.rs`, `src/opencode.rs`, `src/api/server.rs`). Excluding the external implementations prevents conclusions about their internal orchestration, memory, security, uptime or exact deployed behavior. It does not transfer their responsibilities to Spacebot.

Only this repository and revision are frozen. Dependencies named in manifests are not independently registered sources. There are no unavailable repository paths identified by initial inspection. No live deployment data, user database, execution trace or experimental comparison was supplied. That evidence absence prevents efficacy, throughput, recovery-under-failure and model-compliance conclusions. Files not yet read are available evidence for later jobs, not access failures. Documentation, prompts and implementation may disagree; this boundary does not reconcile those disagreements or treat intended behavior as observed behavior.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/spacedriveapp/spacebot` | 5c2ee47b397e09c956dc15000ea576ecd28e92bb | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/spacebot-6a954b400f95/related-systems/spacedriveapp--spacebot`. Implementation: tracked tree; `Cargo.toml`, `build.rs`, `src/main.rs`, `src/db.rs`, channel startup/history/render/persistence portions of `src/agent/channel.rs`, `src/agent/channel_dispatch.rs`, `src/agent/channel_prompt.rs`, `src/agent/autonomy.rs`, `src/agent/ingestion.rs`, `src/agent/chronicle.rs`, `src/agent/compactor.rs`, `src/agent/maintenance.rs`, `src/memory/render.rs`, `src/tools/memory_save.rs`, `src/tools.rs`, `src/skills.rs`, `src/skills/builtin.rs`, `src/prompts/engine.rs`, `src/wiki/store.rs`, `src/api/server.rs`, `src/bin/openapi_spec.rs`, `desktop/src-tauri/src/main.rs`, both UI/API request clients, and `docker-entrypoint.sh`; bounded searches of worker/OpenCode/consolidation and evaluator paths named above. Doctrine/design: selected `README.md`, `docs/content/docs/(core)/architecture.mdx`, `prompts/en/channel.md.j2`, `prompts/en/worker.md.j2`, `prompts/en/memory_persistence.md.j2`, `skills/builtin/wiki-writing/SKILL.md`, `presets/main-agent/ROLE.md`. Evaluation definitions: `tests/behavioral_fixtures.rs` and bounded maintenance/context/invariant searches. Listed paths are initial coverage, not an allowlist. | Implementation: [startup and background wiring](https://github.com/spacedriveapp/spacebot/blob/5c2ee47b397e09c956dc15000ea576ecd28e92bb/src/main.rs), [channel retention and consumption](https://github.com/spacedriveapp/spacebot/blob/5c2ee47b397e09c956dc15000ea576ecd28e92bb/src/agent/channel.rs), [state connections](https://github.com/spacedriveapp/spacebot/blob/5c2ee47b397e09c956dc15000ea576ecd28e92bb/src/db.rs), [API routes](https://github.com/spacedriveapp/spacebot/blob/5c2ee47b397e09c956dc15000ea576ecd28e92bb/src/api/server.rs). Doctrine/design: [persistence instruction](https://github.com/spacedriveapp/spacebot/blob/5c2ee47b397e09c956dc15000ea576ecd28e92bb/prompts/en/memory_persistence.md.j2). Evaluator definition: [behavioral fixtures](https://github.com/spacedriveapp/spacebot/blob/5c2ee47b397e09c956dc15000ea576ecd28e92bb/tests/behavioral_fixtures.rs). | No repository access gap identified. No supplied run or experiment; source definitions cannot establish execution success, production behavior or improvement efficacy. External dependencies and hosted deployments are not frozen and cannot support claims about their internals. |
