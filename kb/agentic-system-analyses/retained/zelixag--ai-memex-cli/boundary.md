---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ai-memex-cli's agent-maintained Markdown knowledge system at commit 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f"
run-id: AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/zelixag/ai-memex-cli
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-ai-memex-cli/related-systems/zelixag--ai-memex-cli
  revision: 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f
  sha256: null
---

# ai-memex-cli boundary

## Boundary and evidence

This run analyses how ai-memex-cli captures source material, maintains durable Markdown knowledge and makes that knowledge available to later agent sessions. The target is the repository's knowledge system, not only its library functions or deterministic CLI. It is in scope as a **memory/knowledge/context-engineering system**: the shipped skills serve model-driven workflows, and command implementations launch external agents for semantic work. The package exposes `memex` through `dist/cli.js`; its source driver imports the capture, maintenance, retrieval and integration commands (SRC-1, `package.json`, `src/cli.ts`).

The boundary is **whole-system** at the repository level. It includes the CLI driver, its state-producing and state-consuming commands, agent adapters, installable skills and workflow references, vault schema and page templates, generated integration instructions, maintenance loop and source-level tests. The shipped CLI and skill callers are part of the target even though actual model inference runs in an external agent executable. The separation between management and use is explicit in the shipped skill (SRC-1, `templates/skills/ai-memex/SKILL.md`):

> This skill makes the agent the main interface for maintaining an LLM wiki. Use the `memex` CLI as a deterministic toolbox, not as the source of semantic judgment.
> --- `templates/skills/ai-memex/SKILL.md`

> Practical rule: if a workflow modifies wiki pages, prefer the CLI command that spawns a sub-agent. If it only reads or summarizes, do it in the current session.
> --- `templates/skills/ai-memex/SKILL.md`

The initial trace covers both directions of the retention loop:

- **Produce and retain:** initialization writes the vault layout and schema; fetch writes captured Markdown under `raw/<scene>/`; distillation has mechanical session-conversion and delegated-agent paths; ingestion reads the live vault schema and index, then launches an agent with the vault as its working directory. Its prompt directs updates to wiki pages, `index.md` and `log.md` while preserving raw sources (SRC-1, `src/commands/init.ts`, `src/commands/fetch.ts`, `src/commands/distill.ts`, `src/commands/ingest.ts`). These are implementation paths and prompt contracts, not evidence that an agent complied.
- **Maintain and check:** deterministic lint constructs reports from reloaded wiki pages; optional semantic lint delegates to an agent. The watcher calls the ingest/lint loop, including file-event and periodic health-check paths. The loop feeds prior mechanical findings into subsequent ingestion and can refresh registered project contexts after a clean report (SRC-1, `src/commands/lint.ts`, `src/commands/watch.ts`, `src/core/ingest-lint-loop.ts`). A clean mechanical report does not establish factual correctness.
- **Reload and consume:** search reloads retained wiki/raw content; inject reads schema includes and optionally keyword-selected wiki pages; glob writes a project-local projection. Context installation and refresh reload the wiki index and render instructions/digests into host files. The query reference directs the current outer agent to search, read pages and answer with citations (SRC-1, `src/commands/search.ts`, `src/commands/inject.ts`, `src/commands/glob.ts`, `src/commands/context.ts`, `src/core/context-block.ts`, `templates/skills/ai-memex/references/query-workflow.md`). Host execution of those instructions is not observed here.

The ingestion prompt makes the intended durable writes explicit (SRC-1, `src/commands/ingest.ts`):

> 1. Read all source files in the target.
> 2. Create or update wiki pages following the schema above.
> 3. Never modify or delete raw source files.
> 4. After writing pages, update ${vault}/index.md and ${vault}/log.md as instructed in the schema.
> --- `src/commands/ingest.ts`

### Repository coverage

The table classifies every top-level tracked file or directory. “Included” means within the functional evidence boundary, not exhaustively inspected. Named paths identify material responsibilities. Initial inspection consists of source reads and bounded tree/call-site searches; available but unread material is not an access gap.

| Top-level tracked path | Treatment and material paths / role | Initial coverage and limit |
|---|---|---|
| `.claude/` | Included: `commands/memex/*.md`, `skills/ai-memex/SKILL.md` and its workflow references are repository-local agent interfaces. Release skill/scripts are excluded from the knowledge loop. | Command tree and `commands/memex/query.md` inspected; installable equivalents traced through templates and hook installation. Other local prompt contents remain available, not yet individually inspected. Excluding release automation prevents claims about release-process safety. |
| `.cursor/` | Included: `rules/memex.mdc` is a shipped bootstrap consumer instruction. | Read through scoped search; its machine-specific vault location is not captured vault content or observed execution. |
| `.gitignore` | Excluded: repository file-management configuration. | Tree inventory only; no claim about ignored local data or repository hygiene. |
| `.vscode/` | Excluded: `settings.json`, editor configuration. | Tree inventory only; no conclusion about editor integration behavior. |
| `AGENTS.md` | Included: development doctrine and an embedded generated memex context block. | Bounded heading/data-flow/context search; referenced local vault pages are unavailable, not registered evidence. |
| `CHANGELOG.md` | Included as release-history doctrine, not executable behavior. | Available, not yet inspected; no historical change claim established. |
| `CLAUDE.md` | Included: development doctrine and embedded context bootstrap instructions. | Bounded heading/data-flow/context search; neither host compliance nor the referenced vault is established. |
| `CONTRIBUTING.md` | Excluded: contributor procedure. | Tree inventory only; no contributor-process assessment. |
| `LICENSE` | Excluded: licensing text. | Tree inventory only; no legal assessment. |
| `README.md` | Included: product intent, workflow and installation documentation. | Opening product/workflow/setup sections inspected; remaining sections available for later source tracing. Claims remain attributed doctrine. |
| `README.zh-CN.md` | Included: Chinese product documentation. | Available, not yet inspected; no translation-equivalence claim. |
| `design/` | Included as design evidence: `agent-native-architecture*.md`, `agent-native-iteration-plan*.md`, `skill-mvp-spec*.md`, `slash-command-spec*.md`, `migration-tasks*.md` and indexes. | Tree inventory; contents not yet inspected. Designs do not establish implemented behavior. |
| `dev-notes/` | Included as target-authored development reports: session summary and project-knowledge draft. | Tree inventory; contents not yet inspected. No operation or outcome is inferred from their presence. |
| `docs/` | Excluded: deployed website HTML/assets and static markers. | Tree inventory; no deployed-site correctness conclusion. Not a runtime vault or an execution trace. |
| `llm-wiki-pattern.md` | Included as declared conceptual lineage and workflow doctrine. | Bounded heading/agent/schema search; not a substitute for implementation tracing. |
| `outreach/` | Excluded: content, execution/growth plans and comparison blog. | Tree inventory only; no outreach effectiveness or external-system comparison conclusions. |
| `package.json` | Included: package identity, executable entry point, distributed files, dependencies and scripts. | Read completely; build/test scripts were not executed. |
| `pnpm-lock.yaml` | Included as dependency pin metadata. | Available, not yet inspected; third-party dependency behavior is not established. |
| `scripts/` | Excluded: `sync-docs.mjs` builds/deploys the presentation website. | Bounded source search; no documentation build/deployment reliability assessment. |
| `src/` | Included: `cli.ts`; all command modules, including setup/config/update/migration; `core/` adapters, vault/config/schema, indexing/linking/search/fetch, session distiller, context registry/rendering and ingest-lint loop; `utils/` process/filesystem support; CLI parse guard and version reader. | CLI driver read; direct source reads cover init, ingest/prompt, distill dispatch, lint, context install/refresh, inject, search dispatch, hook installation/template copying, adapter registry and context rendering. Bounded call-site searches trace fetch persistence, glob projection, new/log/migrate writes, watcher triggers and evaluators. Helper and command details not read remain in scope for later jobs. |
| `templates/` | Included: vault `AGENTS.md`; six page templates; `skills/ai-memex/SKILL.md` and capture/distill/ingest/lint/query/protocol/safety references. | Vault schema, main skill and ingest/lint/query/safety references read; installer recursively copies the skill directory, and init loads the vault schema. Remaining page/capture/distill/protocol contents are available, not yet inspected individually. |
| `tests/` | Included: command/core/utils tests, helpers and mock-vault fixture. These are source-level evaluators, not run results. | Test inventory; loop test setup and clean/repair cases read; bounded test-name inspection covers stopping/reporting variants, injector and hook installation. No tests executed; no model-quality or end-to-end success claim. |
| `tsconfig.json` | Included: TypeScript build configuration. | Available, not yet inspected; no successful compilation claim. |
| `vitest.config.ts` | Included: test configuration. | Available, not yet inspected; no executed-suite coverage claim. |
| `website/` | Excluded: `client/` presentation UI/pages/components/i18n, `server/index.ts` static serving, website build/config/dependencies and generated `docs/`. | Tree inventory and server source read; server serves static content and SPA routing. No conclusion about website claims, UI correctness or deployed operation. |

### External dependencies and evidence limits

External coding-agent executables and their model providers are dependencies, not enclosed runtimes attributed to this target. Adapter profiles select executable names, prompt delivery and flags (SRC-1, `src/core/agent-adapter.ts`). Their internal planning, tool permissions, model behavior and provider persistence cannot be concluded from those invocation definitions. Ripgrep and optional qmd are retrieval dependencies; network retrieval relies on external websites/search responses and imported libraries (SRC-1, `src/commands/search.ts`, `src/commands/fetch.ts`, `package.json`). Their live contents and service behavior are not frozen evidence.

No user vault, agent-session transcript, provider response, execution trace or causal experiment was supplied. The Windows vault paths embedded in repository bootstrap files do not grant access to that vault. These gaps prevent conclusions about actual retained knowledge, semantic accuracy, cross-session improvement, runtime compatibility or successful autonomous maintenance. Tests inspected here use stubbed ingest/lint functions; they support understanding the intended control contract, not observed model performance (SRC-1, `tests/core/ingest-lint-loop.test.ts`). The target's Git-backed description does not itself establish an automatic commit policy.

The evidence is frozen to Git commit `4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f`, verified as the checkout HEAD with no reported working-tree changes. The applicability cutoff is **2026-10-15**, the supplied run date; this does not imply that the revision was current upstream on that date. Only this repository at this commit supplies evidence. No linked upstream pattern, dependency repository, live web page or later release is included. Overall evidence tier: **code-grounded**, with implementation and separately attributed doctrine/design; no observed-run or causal-experiment layer.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/zelixag/ai-memex-cli` | 4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-ai-memex-cli/related-systems/zelixag--ai-memex-cli`. Implementation: package/CLI driver; init, ingest, distill, lint, search, inject, context and hook-installation paths; adapter registry, context rendering and ingest-lint loop; bounded fetch/glob/new/log/migration/watch call-site inspection; loop tests and injector/install test inventory. Doctrine/design: README opening, vault schema, installed skill and ingest/lint/query/safety references; bounded root agent instructions, Cursor rule, query slash prompt and pattern text. Coverage table separates unread material from exclusions. | Implementation: [package](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/package.json), [driver](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/cli.ts), [retention](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/ingest.ts), [maintenance](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/core/ingest-lint-loop.ts), [reuse integration](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/src/commands/context.ts), [evaluator](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/tests/core/ingest-lint-loop.test.ts). Doctrine/design: [skill](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/skills/ai-memex/SKILL.md), [schema](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/AGENTS.md), [query](https://github.com/zelixag/ai-memex-cli/blob/4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f/templates/skills/ai-memex/references/query-workflow.md). | No material shipped path was inaccessible. External agent internals, live services, real vault/session data and execution results are absent: no end-to-end operation, semantic-quality or causal-improvement conclusion. Source-level tests were read, not run. |
