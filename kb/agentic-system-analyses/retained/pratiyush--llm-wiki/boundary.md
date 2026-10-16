---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llm-wiki's shipped knowledge-system loop and host-facing interfaces at commit b1088890ee0743810a92577aecad946c6b3eb2d2"
run-id: AAS-2026-10-16-llm-wiki-6786c5985cdc-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: b1088890ee0743810a92577aecad946c6b3eb2d2
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/Pratiyush/llm-wiki
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-pratiyush--llm-wiki/related-systems/Pratiyush--llm-wiki
  revision: b1088890ee0743810a92577aecad946c6b3eb2d2
  sha256: null
---

# llm-wiki boundary

## Boundary and evidence

This run analyses llm-wiki as a file-based knowledge system for retaining coding-session material, producing linked summaries, maintaining wiki content, and retrieving it for people and agents. The target is the shipped repository system, not just its Python synthesis API or MCP server. Its knowledge-system classification includes model-mediated writing through shipped instructions and optional model backends; it does not imply that every command calls a model. SRC-1: `CLAUDE.md`, `llmwiki/cli.py`, `llmwiki/synth/pipeline.py`, `.claude/skills/llmwiki-query/SKILL.md`.

The source's own host instructions define both retention and later reuse:

> wiki/          YOU OWN THIS. LLM-generated pages that summarise, cross-reference, and
>                synthesise the raw layer. All of your writes go here.
> --- `CLAUDE.md`

> 1. Read `wiki/index.md` and `wiki/overview.md` to identify relevant pages.
> --- `CLAUDE.md`

The boundary is **whole-system** at the repository's frozen revision. It includes session-store adapters and conversion; raw-file write guards, redaction and conversion state; CLI and agent-directed ingestion; synthesis prompts, backend selection and pending-agent completion; index/log upkeep; candidate, confidence, lifecycle and lint mechanisms; retrieval through prompts and MCP; generated reader pages, search, graph and machine-readable exports; vault/editor interfaces; shipped maintenance procedures; and repository test/evaluation definitions. These responsibilities are not excluded because a shipped caller supplies state or invokes a library. SRC-1: `llmwiki/cli.py`, `llmwiki/convert.py`, `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py`, `llmwiki/lint/__init__.py`, `llmwiki/mcp/server.py`, `llmwiki/build.py`, `integrations/obsidian/main.ts`, `integrations/vscode/src/extension.ts`.

Initial entry-point tracing established the producer-to-consumer paths, rather than inferring completeness from cloning:

- `pyproject.toml` exposes `llmwiki.cli:main`; shell and Windows wrappers dispatch to the package. `cmd_sync` calls conversion and optional follow-up build/lint. Conversion reads adapter records, renders raw Markdown, writes files and persists state. SRC-1: `pyproject.toml`, `build.sh`, `sync.sh`, `build.bat`, `sync.bat`, `llmwiki/cli.py`, `llmwiki/convert.py`.
- `synthesize_new_sessions` reloads prior state, discovers raw files, invokes a backend, writes wiki source pages, persists state and rebuilds the source index after changes. The agent backend writes pending prompts and placeholders; the shipped `/wiki-sync` procedure reads and completes those prompts. Direct agent ingestion additionally maintains entities, concepts and overview. These are distinct shipped paths, not one assumed autonomous runtime. SRC-1: `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py`, `.claude/commands/wiki-sync.md`, `CLAUDE.md`.
- The query skill reloads index, overview and relevant retained pages; the MCP query implementation reads wiki pages and returns ranked snippets and overview context. The site builder consumes raw sessions and project metadata, generates reader/search artifacts and calls exporters; its consumption must not be conflated with the agent's semantic wiki traversal. SRC-1: `.claude/skills/llmwiki-query/SKILL.md`, `llmwiki/mcp/server.py`, `llmwiki/build.py`.
- The lint registry reloads wiki pages and runs selected rules; reflection is a separate model-facing maintenance procedure. CI definitions seed synthetic sessions and invoke quality/build commands. These definitions are evidence of intended checks, not evidence that this revision passed them. SRC-1: `llmwiki/lint/__init__.py`, `.claude/commands/wiki-reflect.md`, `.github/workflows/wiki-checks.yml`, `tests/test_synth_pipeline.py`.

The retention handoff is implemented, not solely described:

> out_path.write_text(page_content, encoding="utf-8")
>
>             # Update state
>             state[rel] = p.stat().st_mtime
> --- `llmwiki/synth/pipeline.py`

### Repository coverage

The table classifies every top-level tracked file or directory from the pinned Git tree. Grouped rows enumerate each root. All rows refer to SRC-1. “Included” fixes functional scope, not a claim that every file has been audited. Entry paths and consumer paths above were inspected; remaining helpers, variants and assets are available for later source tracing at this same pin. Available but not yet inspected material is not an access gap. Development-only exclusions do not remove shipped knowledge-state responsibilities.

| Top-level tracked item(s) | Classification and role | Initial inspection / limits and conclusion prevented |
|---|---|---|
| `llmwiki/` | Included: implementation of ingestion, persistence, synthesis, admission/maintenance, retrieval and publication. Material paths: `cli.py`, `convert.py`, `adapters/`, `synth/` including `prompts/source_page.md`, `candidates.py`, `ingest_queue.py`, `confidence.py`, `lifecycle.py`, `lint/`, `context_md.py`, `mcp/server.py`, `build.py`, `exporters.py`, `vault.py`, `watch.py`, `render/`. | Read entry/dispatch, conversion write loop, synthesis backend selection/write loop and pending completion, lint runner, MCP query and builder consumption; searched maintenance/export/vault/watch interfaces. Individual rules, adapter variants and rendering helpers remain available, not exhaustively inspected. No access gap. |
| `CLAUDE.md`, `AGENTS.md` | Included: host-consumed schemas, ingest/query/lint instructions, page formats and cross-project navigation. | Read Claude schema and agent schema workflows; instructions support doctrine, not demonstrated host compliance. |
| `.claude/` | Included: `commands/wiki-*.md` and `skills/llmwiki-{sync,ingest,query}/SKILL.md`, `skills/wiki-all/SKILL.md`; repository maintainer/self-learn commands and skills are distinguishable maintenance context. | Read sync, synthesize, reflect and the three knowledge skills; searched full-pipeline and self-learn entry structure. Other commands and launch configuration remain available for tracing; no host execution was observed. |
| `.claude-plugin/` | Included: plugin and marketplace registration surfaces. | Read `plugin.json` linking commands, skills, MCP and a SessionStart hook. The registered `hooks/session-start.sh` is absent from the tracked tree: no shipped hook implementation can be inferred from the registration. `marketplace.json` not yet inspected. |
| `.kiro/` | Included: `steering/page-format.md`, `verification-rules.md`, `contributing-rules.md`, alternative host-facing format and verification doctrine. | Searched headings/check surfaces; full bodies remain available, not yet inspected. No conclusion about host enforcement. |
| `wiki/` | Included: index, overview, `CRITICAL_FACTS.md`, folder `_context.md` files, seeded entities/concepts, project pages and hot-directory placeholder. | Tree inventoried and producers/consumers traced. Seed-page bodies not yet inspected; they are not supplied user-history evidence or observed successful retention. |
| `examples/` | Included: `sessions_config.json`, `demo-sessions/`, `obsidian-templates/`, `wiki_dashboard.md`, `scripts/tree_from_graph.py`, ignore example. Configuration, synthetic inputs, scaffold templates and export-consumer example. | Tree inventoried; init and Pages workflow traced their use. Individual example bodies not yet inspected. No real-user outcome claim. |
| `integrations/` | Included: `vscode/src/extension.ts` commands/tree reader and `obsidian/main.ts` sync/build/vault-copy caller, plus manifests and guides. | Read both implementations. Obsidian copy helper implements an index-only proof of concept; including the integration does not imply full recursive mirroring. |
| `tests/` | Included: `test_synth_pipeline.py`, agent/MCP/lint/raw-immutability/vault tests, `e2e/`, `agents/`, fixtures, performance budgets and visual baselines. | Read initial synthesis fixtures/assertions and inventoried other evaluators. No tests executed or test results supplied; cannot establish passing status or semantic answer quality. |
| `.github/` | Included for `workflows/wiki-checks.yml`, `pages.yml` and other shipped automation definitions; issue/review/release administration is supporting context. | Read wiki-check and demo-publication drivers. Other CI, agent healer and release workflows are available but not yet inspected; no CI execution or deployment-success claim. |
| `scripts/` | Included for metadata/title/model repairs, `normalize_wikilinks.py`, preview/recording and screenshot helpers; release-maintenance utilities are supporting context. | Tree and repair-function declarations inspected. Repair bodies and ancillary media/release scripts not yet inspected; no claim that repair execution preserves all content. |
| `docs/` | Included: architecture, framework, configuration, modes, adapters, CLI/reader references, tutorials, maintenance/design material and rendered documentation/assets. | Tree inventoried and `build.py` documentation compiler call traced. Bodies not yet inspected in this boundary job; documentation claims need attribution and implementation checks, not automatic acceptance. |
| `specs/` | Included: reader/UI acceptance specifications (`home.md`, `session-detail.md`, `graph.md`, other view specifications). | Tree inventoried, bodies not yet inspected; cannot establish conformance from their presence. |
| `README.md` | Included: product intent, entry-point and output-format guide. | Read opening feature/usage sections; advertised features are not treated as implementation proof. |
| `pyproject.toml` | Included: package dependencies, console entry point, packaging and test configuration. | Read completely; establishes package contract, not installed-wheel behavior. |
| `action.yml` | Included: reusable GitHub Action caller that installs, initializes, syncs and builds. | Read completely. It installs a registry package without this commit pin; the declaration is frozen here, the resolved external package is not. Cannot equate a future action execution with this revision. |
| `build.sh`, `build.bat`, `sync.sh`, `sync.bat`, `serve.sh`, `serve.bat`, `setup.sh`, `setup.bat`, `upgrade.sh`, `upgrade.bat` | Included: user-facing setup and invocation wrappers. | Read setup/build/sync shell wrappers; searched Windows and serve/upgrade dispatch. No execution or cross-platform validation. |
| `Dockerfile`, `docker-compose.yml`, `flake.nix`, `homebrew/` | Included: deployment/distribution entry surfaces; `homebrew/llmwiki.rb` is the formula. | Tree inventoried, bodies not yet inspected. No claim about deployed images, formula installation or Nix build success. |
| `.llmwiki-synth-state.json` | Included: checked-in synthesis state artifact, distinct from executable persistence logic. | Presence inventoried; contents not yet inspected. Does not establish a successful synthesis run. |
| `CHANGELOG.md`, `RELEASE-NOTES-v1.2.0.md` | Included as attributed release/history context, not current executable behavior. | Not yet inspected; no historical feature-completion conclusions. |
| `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `LICENSE` | Excluded from functional mechanism analysis: contributor/community/legal policy. | Available, deliberate exclusion. Prevents conclusions about governance, vulnerability-response practice or license interpretation; does not exclude wiki-writing instructions in host schemas. |
| `.editorconfig`, `.gitignore`, `.gitlab-ci.yml.example`, `lychee.toml`, `package.json`, `package-lock.json`, `playwright.config.ts` | Included as development/test/deployment configuration context, not the knowledge engine itself. | Names and locations inventoried; bodies not yet inspected. No dependency-security, GitLab deployment or browser-test execution conclusions. |

### External dependencies and evidence limits

The frozen evidence is SRC-1 at **b1088890ee0743810a92577aecad946c6b3eb2d2**, applicable through **2026-10-16**. The acquired checkout's HEAD matches the pin and its working tree was clean when inspected. No other repository, website, model result or revision is admitted. The source register's initial paths are discovery coverage, not an allowlist within this commit.

The overall evidence tier is **code-grounded**: executable persistence, retrieval and caller paths were inspected alongside the source's doctrine. The external coding-agent runtime supplies model execution, tool permissions, conversation scheduling and instruction loading; those host responsibilities are outside this target and cannot be credited to llm-wiki. The source does ship the instructions and pending-prompt handoff that those hosts consume. Ollama's service and model weights are external; only the request adapter is covered. The optional build-time Claude invocation is source-covered, not an observed model run. SRC-1: `llmwiki/synth/ollama.py`, `llmwiki/synth/agent_delegate.py`, `llmwiki/build.py`, `CLAUDE.md`.

Session-store contents, user vaults, generated personal raw/wiki/site data, external packages and services, live demo contents, and live CI results are not frozen here. Their absence prevents conclusions about private-corpus coverage, answer correctness, real-world durability, deployment availability and measured performance. This is an evidence limit, not a reason to exclude the repository's adapters, caller implementations, evaluators or example data. The target was not executed, dependencies were not installed, and no provider was called. The registered source supplies implementation and doctrine/design evidence only, not observed-run or causal-experiment evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Pratiyush/llm-wiki` | b1088890ee0743810a92577aecad946c6b3eb2d2 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-pratiyush--llm-wiki/related-systems/Pratiyush--llm-wiki`. Implementation: `pyproject.toml`, `llmwiki/cli.py` init/sync/build dispatch, `llmwiki/pipeline.py`, `llmwiki/adapters/__init__.py`, conversion persistence loop in `llmwiki/convert.py`, backend selection and write loop in `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py` handoff/completion, `llmwiki/synth/ollama.py` request path, `llmwiki/build.py` build/consumer path, `llmwiki/context_md.py`, lint runner in `llmwiki/lint/__init__.py`, MCP query/read guards in `llmwiki/mcp/server.py`, both editor integrations, setup/build/sync wrappers, `action.yml`, `.github/workflows/{pages,wiki-checks}.yml`, initial tests in `tests/test_synth_pipeline.py`; declaration searches for candidate/queue/lifecycle/confidence/export/vault/watch and repair paths. Doctrine/design: `CLAUDE.md`, `AGENTS.md` workflows, opening `README.md` sections, `.claude/skills/llmwiki-{sync,ingest,query}/SKILL.md`, `.claude/commands/wiki-{sync,synthesize,reflect}.md`, `.claude-plugin/plugin.json`; heading searches for Kiro steering, full-pipeline and self-learn skills. Entire tracked tree inventoried. | Implementation: [CLI](https://github.com/Pratiyush/llm-wiki/blob/b1088890ee0743810a92577aecad946c6b3eb2d2/llmwiki/cli.py), [synthesis persistence](https://github.com/Pratiyush/llm-wiki/blob/b1088890ee0743810a92577aecad946c6b3eb2d2/llmwiki/synth/pipeline.py), [retrieval](https://github.com/Pratiyush/llm-wiki/blob/b1088890ee0743810a92577aecad946c6b3eb2d2/llmwiki/mcp/server.py), [reader build](https://github.com/Pratiyush/llm-wiki/blob/b1088890ee0743810a92577aecad946c6b3eb2d2/llmwiki/build.py). Doctrine/design: [host schema](https://github.com/Pratiyush/llm-wiki/blob/b1088890ee0743810a92577aecad946c6b3eb2d2/CLAUDE.md), [pending completion procedure](https://github.com/Pratiyush/llm-wiki/blob/b1088890ee0743810a92577aecad946c6b3eb2d2/.claude/commands/wiki-sync.md). | No checkout access gap. Plugin-declared hook file is absent from tracked evidence; cannot establish its shipped execution. Available but initially unread material is distinguished in coverage above. External host/service implementations, private data and execution evidence are not supplied: no demonstrated host compliance, provider quality, successful end-to-end operation or measured causal benefit. |
