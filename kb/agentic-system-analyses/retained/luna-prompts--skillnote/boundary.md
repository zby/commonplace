---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SkillNote's shipped skill registry, authoring, distribution and feedback paths at commit 7ea2fc7a8435af64d1c080d8765c0eabba1121ea."
run-id: AAS-2026-10-14-skillnote-0ccfe85cda4a-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/luna-prompts/SkillNote
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/skillnote-0ccfe85cda4a/related-systems/luna-prompts--SkillNote
  revision: "7ea2fc7a8435af64d1c080d8765c0eabba1121ea"
  sha256: null
---

# SkillNote boundary

## Boundary and evidence

SkillNote is in scope as a **memory/knowledge/context-engineering system**: it retains reusable procedural instructions and serves them to model-driven agents. Its intended use is a self-hosted skill registry, not an enclosing agent runtime. The target includes the registry and its shipped consumers, not just its REST or MCP interface. SRC-1, `README.md`, declares:

> Self-host your team's <code>SKILL.md</code> library. Version it, scope it, and ship it to Claude Code and OpenClaw from one CLI.
> --- `README.md`

The **whole-system** boundary includes the web authoring interface and browser-local state, backend admission and version storage, imports and upstream refresh/publishing, collection scoping, CLI installation and update, Claude Code/Codex hooks, OpenClaw skill instructions and watcher, MCP delivery, claude.ai browser connector, analytics, ratings and comments. These are shipped parts of the same state loop, even where the final skill is consumed in an external agent. The boundary includes model-facing maintenance instructions as system behavior contracts, not instructions for this analysis.

Initial tracing establishes the major loop surfaces:

- **Produce and persist:** the web store calls skill creation/update APIs; backend creation and edits write skill content and content versions. The import service also admits retained content, while ZIP publishing and bundle storage provide another admission path. SRC-1, `src/lib/skills-store.ts`, `backend/app/api/skills.py`, `backend/app/services/imports/importer.py`, `backend/app/api/publish.py`, `backend/app/services/storage_service.py`.
- **Agent-assisted maintenance:** skill-push instructs an agent to draft, review and POST/PATCH reusable procedures, with a confirmation gate. It is not merely documentation of a library API. SRC-1, `plugin/skills/skill-push/SKILL.md`:

> Stop and wait for an explicit yes. Do NOT draft the name/description/content, fetch collections, or present a preview until the user confirms. Unsolicited drafts feel pushy and waste attention.
> --- `plugin/skills/skill-push/SKILL.md`

- **Reload and consume:** the Claude Code plugin fetches collection-filtered content and writes project skills and a manifest. The Codex plugin has its own hook-driven sync path. CLI `add` installs bundles through agent adapters and records a manifest; it is included alongside plugin sync rather than treated as an external caller. SRC-1, `plugin/hooks-handlers/sync.sh`, `plugin/hooks/hooks.json`, `plugin-codex/hooks/hooks.json`, `plugin-codex/hooks/handlers/sync.sh`, `cli/src/commands/add.ts`. The Claude Code sync implementation includes:

> with open(filepath, 'w') as f:
>         f.write(content)
> --- `plugin/hooks-handlers/sync.sh`

- **Model-facing retrieval:** MCP builds tools from retained skill rows and returns their instruction text. The enclosing model's choice to apply those instructions is outside the implementation boundary. SRC-1, `backend/mcp_server.py`:

> content = f"# {self.skill_name}\n\n{self.content_md}"
> --- `backend/mcp_server.py`

- **Later use and feedback:** OpenClaw's shipped skill and generated sidecar instruct sync, selection, use, usage logging and conditional ratings. Claude Code hooks and complete-skill instructions report usage or ratings. The claude.ai connector polls operations, uploads groups, retires deselected groups, and imports remote-authored skills. SRC-1, `plugin-openclaw/skillnote/SKILL.md`, `plugin-openclaw/skillnote/sync.sh`, `plugin-openclaw/skillnote/log-watcher.py`, `plugin/skills/complete-skill/SKILL.md`, `backend/app/api/hooks.py`, `extensions/claude-ai/src/background.ts`, `backend/app/services/claude_ai_sync.py`. These surfaces permit investigation of feedback collection; they do not by themselves establish improved task performance.

The immutable evidence boundary is SRC-1 at **7ea2fc7a8435af64d1c080d8765c0eabba1121ea**. HEAD was checked against the acquired pin. The applicability cutoff is **2026-10-14**, the supplied run date; this is not a claim about the date of the last successful deployment. The overall tier is **code-grounded**, with source-native documentation as doctrine/design evidence. No target code, tests or examples were executed, and no services were contacted.

### Repository coverage

Every top-level tracked entry is classified below. “Included” sets the functional boundary, not a claim that every file has been audited. Initial inspection combines tree inventory, targeted symbol searches and source reads. Unread files in included directories remain available at the registered commit; they are **not access gaps**. Tests were inventoried and representative test source inspected, not run.

| Top-level entry | Classification and material paths / role | Inspection and exclusion limit |
| --- | --- | --- |
| `backend/` | Included: `app/main.py`; `app/api/skills.py`, `imports.py`, `publish.py`, `downloads.py`, `collections.py`, `setup.py`, `hooks.py`, `analytics.py`, `comments.py`, `openclaw.py`, `claude_ai.py`, `cli.py`; `app/services/imports/`, `claude_ai_sync.py`, storage; `app/db/`, `alembic/`; `mcp_server.py`; `scripts/`, `seed_data/`; `tests/` | Entry-point imports and material producer/consumer symbols traced; selected CRUD, hook and MCP bodies read. Model/schema/migration and endpoint details remain for later inspection. Representative MCP unit tests and OpenClaw usage test declarations inspected. |
| `cli/` | Included: `src/index.ts`, `commands/`, `agents/`, `api/`, `manifest/`, `state/`, `bridge/poll.ts`, Docker lifecycle, assets, tests | CLI package entry and command source traced; connect and add bodies read; bridge and adapter/test surfaces located. Other command details remain available. |
| `plugin/` | Included: hook manifest and `hooks-handlers/`; `bin/`; `skills/skill-push/`, `complete-skill/`, `collection/`; `agents/skill-creator.md`, commands, output style, tests | Hook manifest, sync, authoring and rating instructions read; plugin test assertions searched. Picker and other handler internals remain available. |
| `plugin-codex/` | Included: plugin descriptor, `hooks/hooks.json`, `hooks/handlers/`, `skills/` | Hook manifest read; sync persistence and context-output symbols located. Full handler and prompt details remain available. |
| `plugin-openclaw/` | Included: `skillnote/SKILL.md`, `sync.sh`, `log-watcher.py`, configuration/security, `skillnote-doctor/`, tests | Setup/selection instructions and generated sidecar read; persistence and watcher symbols traced. Remaining prompt and test details remain available. |
| `extensions/` | Included: `claude-ai/src/background.ts`, `content.ts`, clients, storage, UI, manifests and tests | Queue polling, delivery, group retirement and reverse-import source read; client tests searched. Other client, content-script and UI internals remain available. |
| `src/` | Included: app skill editor/history/versions, collection picker, import workspace, integration/settings/analytics pages; `lib/skills-store.ts`, `lib/api/`, validation and CLI jobs | Store creation/edit API calls read; editor callback surface searched; app/component tree inventoried. Rendering and other API details remain available. |
| `e2e/` | Included: skill lifecycle, import journeys, connector, MCP, ratings and integration test specifications | Tree and representative `skills.spec.ts` mock/persistence surfaces inspected; not observed executions or evidence of task benefit. |
| `docs/` | Included: integration guides/runbooks, endpoint contracts, hardening log, `superpowers/` plans/specs, screenshots and terminal illustrations | Tree inventoried; design/history and illustrations only until individually inspected. Plans cannot establish shipped behavior. |
| `ideas/` | Excluded: plugin brainstorm, skill-push and sync-hook PRDs | Deliberate exclusion from shipped-behavior evidence; prevents treating proposed features as implemented. |
| `.github/` | Included: workflow build, release and smoke checks | Tree and CLI PR build checks searched; CI declarations do not prove a run passed. |
| `scripts/` | Included: installation preflight, README checks, release tooling and icon generation | Inventory and preflight surface inspected; remaining script bodies available. |
| `deploy/` | Included: pinned-image Compose deployment | Service/image declarations inspected; published image bytes and deployed state are not frozen here. |
| `Formula/` | Included: `skillnote.rb` packaging entry | Package and CLI executable declarations inspected; package archive not acquired. |
| `public/` | Included: `sw.js` browser delivery and static assets | Tree and service-worker search inspected; image content not interpreted. No visual-quality conclusion. |
| `docker-compose.yml` | Included: local-source service graph, volumes, plugin mounts and startup | Read; establishes shipped API/MCP/web/Postgres wiring, not successful deployment. |
| `Dockerfile` | Included: web image entry | Build and CMD declarations inspected. |
| `install.sh` | Included: source-install entry | Located through tree and README; script internals remain available. |
| `package.json`, `package-lock.json` | Included: frontend scripts/dependencies and lock | Package script/dependency surface searched; dependency implementation not frozen. |
| `next.config.ts` | Included: web/server configuration and API proxy | Located in deployment wiring and searched; detailed rules remain available. |
| `playwright.config.ts`, `test-editor-ux.mjs` | Included: test configuration and editor probe | Inventoried; Playwright configuration searched; no execution results. |
| `components.json`, `eslint.config.mjs`, `next-env.d.ts`, `postcss.config.mjs`, `tsconfig.json` | Included: frontend generation, typing, style and lint/build support | Inventory only; not independent evidence of retention or agent behavior. |
| `.dockerignore`, `.gitignore` | Included: build/version-control packaging support | Inventory only; no claim of complete packaging audit. |
| `README.md` | Included: product intent, setup and architecture doctrine | Opening product and integration sections read; remaining text available, not assumed authoritative over code. |
| `CHANGELOG.md`, `MIGRATION-v0.5.md`, `RELEASE-NOTES-0.5.3.md` | Included: source-native release/migration declarations | Inventory only; not observed operation at this pin. |
| `HARDENING_SPEC.md` | Included: source-native security design | Inventory only; no claim that requirements were fulfilled. |
| `CLAUDE.md` | Included: repository development instructions | Inventory only; not a substitute for inspecting shipped prompts or runtime behavior. |
| `LICENSE` | Excluded from operational analysis: licensing terms | Deliberate exclusion prevents a legal/licensing assessment, not tracing the skill loop. |

### External dependencies and limits

The shipped stack depends on Postgres, Python/FastAPI/FastMCP, Node/Next.js, browser extension APIs and local shell/Python/curl tooling. Their implementations are not separate registered sources. Source wiring is visible in SRC-1, `docker-compose.yml`, `backend/app/main.py`, `backend/mcp_server.py`, `cli/package.json`, `extensions/claude-ai/src/background.ts`.

Claude Code, Codex, OpenClaw and claude.ai itself are excluded external hosts. Their model calls, skill discovery semantics, context limits and compliance with returned instructions are not established by this checkout. The shipped adapters, hooks, prompts and connector are included; responsibilities of the external hosts are not attributed to SkillNote. Remote Git repositories used as skill origins, npm/Homebrew archives, GHCR images and third-party dependencies are not captured. This prevents claims about their contents or compatibility beyond the source-declared interfaces. No deployed database, actual user skill corpus, host transcript or measured intervention is supplied. This prevents claims of successful end-to-end operation, reliable rating behavior, learning effectiveness or causal task improvement. These are evidence limits, not inaccessible material shipped code paths, and do not require a partial-loop boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/luna-prompts/SkillNote` | 7ea2fc7a8435af64d1c080d8765c0eabba1121ea | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/skillnote-0ccfe85cda4a/related-systems/luna-prompts--SkillNote`. Implementation: tracked tree; representative backend entry, CRUD, hook and MCP bodies; CLI connect/add; plugin hook/sync; OpenClaw sync/watcher surfaces; browser connector poll/execute paths; UI store creation/edit; representative test source and packaging declarations. Doctrine/design: README product/setup sections, skill-push and complete-skill prompts, OpenClaw setup/selection instructions and generated sidecar. Coverage table distinguishes remaining available material from inspected source. | Implementation: [API](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/backend/app/api/skills.py), [MCP](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/backend/mcp_server.py), [plugin sync](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/plugin/hooks-handlers/sync.sh), [CLI delivery](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/cli/src/commands/add.ts), [browser connector](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/extensions/claude-ai/src/background.ts). Doctrine/design: [README](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/README.md), [authoring prompt](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/plugin/skills/skill-push/SKILL.md), [OpenClaw prompt](https://github.com/luna-prompts/SkillNote/blob/7ea2fc7a8435af64d1c080d8765c0eabba1121ea/plugin-openclaw/skillnote/SKILL.md). | No known checkout access gap. Implementation supports static behavior tracing, not successful execution. Prompts and documentation support intended agent behavior, not host compliance. No registered observed run or causal experiment; no deployment, external-host or task-improvement conclusion. |
