---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Ultimate's shipped coding-agent runtime, extensions and project-memory loop at commit e2b9fa61962f6aecd394dea1c670688fac3ec432."
run-id: AAS-2026-11-01-ultimate-f5179584de71-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "e2b9fa61962f6aecd394dea1c670688fac3ec432"
analysis-cutoff: "2026-11-01"
evidence-tier: code-grounded
source:
  identity: https://github.com/HazAT/ultimate
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/ultimate-f5179584de71/related-systems/HazAT--ultimate
  revision: e2b9fa61962f6aecd394dea1c670688fac3ec432
  sha256: null
---

# Ultimate boundary

## Boundary and evidence

This run analyses Ultimate as the shipped local coding-agent application, not just its memory API or its Pi Durable integration. Its intended use is a project-specialized agent with a browser UI, standing agents, coordinator branches, bounded subagents and extensible tools. The target is in scope because its server opens and resumes a model-driven harness and its shipped callers submit inputs and consume stored conversations. It is an **enclosing runtime** at the application boundary, even though model execution and durable scheduling use external packages. The boundary kind is **whole-system**: the supervisor, server, browser client, built-in extensions, prompts, project configuration and maintenance paths are included together. SRC-1: `README.md`, `package.json`, `bin/ultimate.ts`, `server/main.ts`, `server/harness.ts`, `server/api.ts`, `web/src/sdk/api.ts`.

> A coding agent you specialize for the project you work on. Start it in your repository and it is Pi's coding agent in a
> web UI.
> --- `README.md`

The executable entry is `ultimate` → `bin/ultimate.ts`; development can enter through `server/main.ts`. The supervisor forks that server, gates replacement with a type check, releases the old storage owner and activates the new one. The server prepares extensions and API services, opens storage and resumes the harness. The browser's submit endpoint is a shipped consumer, not an excluded host application: it reaches `conversation.submit` in the same system. SRC-1: `package.json`, `bin/ultimate.ts`, `server/main.ts`, `server/api.ts`, `web/src/sdk/api.ts`.

> const child = fork(join(ultimateRoot, 'server/main.ts'), [], {
> --- `bin/ultimate.ts`

> storage = await openNodeSqliteStorage(chapter.database)
> --- `server/harness.ts`

The functional boundary includes state production, persistence, admission and later consumption. Initial project memory is instructed through onboarding; `remember` and landing-triggered distillation maintain root memory. Branch creation consumes a memory index and recent landings instead of the root's full tally when memory exists. The `memory` tool and recall hook retrieve fuller content later. Compaction, catch-up, memory review and dream/chapter handover are included maintenance paths, not external editorial work. These statements identify paths for later analysis; they do not establish successful recall, faithful summaries or effective self-improvement. SRC-1: `agents/ultimate.md`, `extensions/lineage/server.ts`, `extensions/lineage/memory.ts`, `extensions/recall/server.ts`, `extensions/dream/DREAM.md`, `extensions/dream/seed.ts`.

> The model text a branch from `root` starts from instead of its tally, read inside `tx` before its first table
> * write; undefined while the root has no memories. `tip` is the root's newest entry.
> --- `extensions/lineage/memory.ts`

> Only @ultimate writes project memory; tell @ultimate what to remember (message, reply: false).
> --- `extensions/lineage/server.ts`

> Recalled from project memory for the message above. Act on each that applies, and say so in one line when it changes what you do:
> --- `extensions/recall/server.ts`

The checkout is frozen at **e2b9fa61962f6aecd394dea1c670688fac3ec432**. Its HEAD matched acquisition and its working tree was clean on inspection. The applicability cutoff is **2026-11-01**, the supplied run date, not a claim about any later upstream state. Overall evidence is **code-grounded**. Documentation and agent instructions supply doctrine/design; inspected source supplies implementation evidence. Test source supplies intended executable checks, not observed passing runs. No target, tests, examples, model calls or external services were executed.

### Shipped coverage

Every top-level tracked entry is classified below. All included entries remain inside the registered commit for later source inspection. “Not yet inspected” means available but not initially read in detail, never an access gap. Whole-system describes the functional scope and traced loop, not a claim that every file has already been audited. All repository path references in this table refer to SRC-1.

| Top-level entry | Classification and material paths | Initial inspection and role; exclusion consequence |
|---|---|---|
| `bin/` | Included: `bin/ultimate.ts`, `bin/dashboard.ts`, `bin/tsconfig.json` | Supervisor boot/swap traced in `bin/ultimate.ts`; dashboard and configuration not yet inspected in detail. Includes the shipped driver that owns process replacement. |
| `server/` | Included: `server/main.ts`, `server/harness.ts`, `server/api.ts`, `server/project.ts`, `server/extensions.ts`, `server/skills.ts`, discovery, events, security and trace services | Read server/harness/project code and API submission slice; searched extension installation and skill loading. Covers storage open/reload, input admission, extension registration and outward state indexes. Remaining service implementation not yet inspected in detail. |
| `shared/` | Included: `shared/protocol.ts`, `shared/events.ts`, `shared/extension-api.ts` | Inventoried contracts linking server and clients; declarations not yet inspected in detail. |
| `extensions/` | Included in full, including server and web facets, APIs, READMEs and embedded agent definitions | Traced `extensions/lineage/server.ts`, `extensions/lineage/memory.ts`, `extensions/recall/server.ts`, `extensions/subagents/children.ts` and server entry points. Read `extensions/dream/DREAM.md` and seed-building slice; searched `extensions/workspaces/lander.ts` through landing event emission. These cover memory writing, validation, persistence via documents, branch consumption, later recall, subagent creation and maintenance. Searched server declarations for conversations, messages, codemode, automations and cloud. Other built-ins, rendering facets, delivery, scheduler and backup details remain included but not yet inspected in detail. |
| `lib/` | Included: `lib/agents.ts`, `lib/chapters.ts`, `lib/compaction.ts`, `lib/entries.ts`, settings, Git, remote and persistence helpers | Searched agent definition/instruction composition; followed chapter and settings imports from the harness. Remaining helper implementations not yet inspected in detail. These are system support, not an excluded caller. |
| `web/` | Included: `web/src/sdk/api.ts`, `web/src/sdk/store.ts`, `web/src/sdk/resume.ts`, `web/src/app/`, extension host, components and public assets | Read submit/history client slice and searched browser resume path; inventoried app/SDK. Includes user input and later consumption of retained history. Other rendering and client-state implementation not yet inspected in detail. |
| `agents/` | Included: `agents/ultimate.md`, `agents/coordinator.md`, worker, scout, reviewer, designer, watcher and dream-pass definitions | Read standing-agent definition, onboarding, memory maintenance and dream instructions; scanned definition headings/tool declarations. Other bodies not yet inspected in detail. Prompts are part of the loop, not commentary outside it. |
| `skills/` | Included: `skills/how-ultimate-works/SKILL.md`, `skills/integrate-ultimate/SKILL.md`, `skills/adopt-ultimate-setup/SKILL.md`, `skills/write-extension/SKILL.md`, `skills/verify-ui/SKILL.md`, `skills/ui-preview-round/SKILL.md` | Inventoried/scanned procedure headings and traced skill expansion through server code. Full procedure bodies not yet inspected. Includes shipped customization and verification instructions. |
| `.ultimate/` | Included: `.ultimate/README.md`, `.ultimate/settings.json`, agent overlays/reviewers and `.ultimate/skills/` with helper scripts and preview fixture | Read README and inventoried every tracked path. Repository-local specialization is included, separately from generic built-ins; settings, overlay bodies and skill helpers not yet inspected in detail. No claim that these repository settings apply to every consuming project. |
| `AGENTS.md`, `CLAUDE.md` | Included: repository instructions and instruction alias | Read `AGENTS.md`; Git tree identifies `CLAUDE.md` as a symlink. Instructions cover coordination, memory, verification and reload responsibilities. |
| `docs/` | Included: `docs/running.md`, `docs/durability.md`, `docs/subagents.md`, settings, extensions, worktrees, upstream coupling and architecture HTML | Read running/durability/subagents documentation; other documents inventoried but not yet inspected. Supplies declared contracts, not independent operational proof. |
| `test/` | Included: `test/lineage-memory.test.ts`, `test/recall.test.ts`, `test/dream.test.ts`, `test/ultimate.test.ts`, `test/e2e/`, `test/web/` and other tests/fixtures | Read recall test with faux provider and mocked classification; searched memory/dream/standing-agent checks and inventoried remaining tests. Includes evaluators and shipped drivers; not run, so no passing-suite or live-provider conclusion. |
| `scripts/` | Included: `scripts/reset.ts`, `scripts/restore.ts`, `scripts/setup-machine.ts`, `scripts/deps.ts` | Inventoried; reset/restore roles also documented in `docs/running.md`. Source bodies not yet inspected. State reset/restoration and setup remain in scope. |
| `patches/` | Included: patches for Pi Durable, Chord and Claude Code provider | Inventoried; patch registration and purpose searched in `pnpm-workspace.yaml`. Patch bodies not yet inspected. Repository-shipped alterations are evidence; full upstream implementations are not thereby captured. |
| `lint/` | Included: `lint/ultimate.ts` | Inventoried and referenced by shipped conventions; implementation not yet inspected. Includes static policy checks, not proof of compliance. |
| `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml` | Included | Read package entry points/dependencies; searched workspace patch declarations. Lockfile not yet inspected in detail. Defines the build/dependency boundary, not evidence of installed external package behavior. |
| `components.json`, `tsconfig.json`, `tsconfig.swap.json`, `tsconfig.web.json`, `vite.config.ts` | Included | Inventoried and traced through startup/type-check references; bodies not yet inspected. Build, UI and swap configuration remain available to inspect. |
| `README.md` | Included | Read in full: declared product use, startup, customization and memory/context overview. |
| `.github/` | Excluded: `.github/pull_request_template.md` | Deliberate administrative exclusion after tree inventory; prevents conclusions about contribution-template enforcement, not about the running state loop. |
| `.gitignore` | Excluded | Deliberate repository-administration exclusion after tree inventory; no conclusion about completeness of untracked local runtime artifacts. |
| `CONTRIBUTING.md` | Excluded | Deliberate contribution-process exclusion; prevents assessing upstream contribution governance. Runtime and maintenance instructions elsewhere remain included. |
| `LICENSE` | Excluded | Deliberate legal-text exclusion; no licensing/compliance assessment. |

### External dependencies and limits

Pi Durable, Pi Coding Agent, Pi AI, Chord, codemode/MCP adapters and the Claude Code provider are external dependencies, not additional frozen repositories. Their declared versions and the shipped patches are in scope; their complete upstream implementations are unavailable within this evidence set. The inspected harness demonstrates Ultimate's integration calls, not the internal crash consistency or scheduling correctness of those packages. SRC-1: `package.json`, `pnpm-workspace.yaml`, `server/harness.ts`.

Model providers, Claude Code CLI, Chromium/browser execution, Git, Tailscale and cloud services are environmental dependencies. Local adapter source and UI remain in scope; actual credentials, live installations, remote instances, user/project additions outside this checkout and production databases/traces are not supplied. This prevents conclusions about live service reliability, realized cross-machine behavior, actual user customization, token costs and retention outcomes. The source's own operational claims may be attributed but are not observed runs. SRC-1: `README.md`, `docs/running.md`, `server/project.ts`, `server/harness.ts`.

No material shipped path was inaccessible during initial inspection. Files explicitly marked not yet inspected are available under the same pin; they must be read before making detailed claims about their behavior. The traced persistence and memory loop supports a whole-system scope without excluding the prompts, maintenance procedures, callers or evaluators that give that loop its purpose.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/HazAT/ultimate` | e2b9fa61962f6aecd394dea1c670688fac3ec432 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/ultimate-f5179584de71/related-systems/HazAT--ultimate`. Implementation: tracked tree; package entry points; supervisor boot/swap; server/harness/project; API submission and web submit/history; lineage memory write/distil/branch paths; recall hook; subagent child creation; dream seed-building; bounded searches of extension installation, prompt/skill composition, landing, conversations, automations, messages, codemode and cloud. Test source: recall faux-provider test and bounded searches of lineage-memory/dream/ultimate tests, not executed. Doctrine/design: README, AGENTS, running/durability/subagents docs, standing-agent definition, dream procedure, repository-local README and skill/agent headings. | Implementation: [entry point](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/bin/ultimate.ts), [harness](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/server/harness.ts), [memory](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/extensions/lineage/memory.ts), [recall](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/extensions/recall/server.ts), [test source](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/test/recall.test.ts). Doctrine/design: [standing-agent prompt](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/agents/ultimate.md), [dream procedure](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/extensions/dream/DREAM.md), [README](https://github.com/HazAT/ultimate/blob/e2b9fa61962f6aecd394dea1c670688fac3ec432/README.md). | No shipped-source access gap. No frozen external package implementations, production state, observed run or causal experiment: cannot establish live reliability, memory quality, provider behavior or causal improvement. Initial uninspected files are identified in the coverage table, not treated as unavailable. |
