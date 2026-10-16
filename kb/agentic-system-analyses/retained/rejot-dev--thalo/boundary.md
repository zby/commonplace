---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Thalo's plain-text knowledge system and shipped synthesis loop at commit cdb9aae983e6bc0b75eff1606bc99b088c3aebff."
run-id: AAS-2026-10-14-thalo-86fcc3efe983-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/rejot-dev/thalo
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/thalo-86fcc3efe983/related-systems/rejot-dev--thalo
  revision: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
  sha256: null
---

# Thalo boundary

## Boundary and evidence

This run analyses Thalo as a structured plain-text knowledge system for human and AI collaboration, not merely its parser API. Intended use is to characterize how retained entries are produced, checked, queried, selected for synthesis, rewritten and consumed on later passes. The target class is `memory/knowledge/context-engineering system`; the boundary kind is `whole-system`. The README declares this knowledge use and distinguishes context preparation from downstream model generation (SRC-1, `README.md`):

> Thalo is a plain-text format that gives your knowledge _just enough_ structure for tools and AI to
> work with it, while staying readable and editable by humans. Just text files in git, editable in
> Cursor or by Claude Code.
> --- `README.md`

> Actualization is intentionally minimal. It runs the user-defined query and prints the _new_ entries
> that match the query together with the prompt. This can then be piped to an LLM to do anything, but
> generally to create synthesized content.
> --- `README.md`

The functional boundary includes the language, parser, workspace and schema model, checker, queries, Git and timestamp change tracking, CLI, formatter, merge driver, editor integrations, browser playground, authored instructions and example KB. It also includes the GitHub synthesis action and the shipped Pi synthesis command. These are not excluded enclosing applications: the repository supplies both their state-handling code and a workflow connecting them. The root CLI registers initialization, checking, querying, actualization, formatting, language-server and merge commands (SRC-1, `apps/thalo-cli/src/mod.ts`). The CLI loads `.thalo` and Markdown files into a workspace, while actualization reloads synthesis definitions and their latest checkpoint entries (SRC-1, `apps/thalo-cli/src/files.ts`, `packages/thalo/src/services/synthesis.ts`, `packages/thalo/src/commands/actualize.ts`).

The action passes selected entries and checkpoints to a command, then commits and pushes resulting file changes and creates or updates a pull request. The shipped workflow selects the repository's Pi command and the `thalo-test` KB. This establishes an inspectable model-dependent path within the target, despite the CLI's deterministic context preparation (SRC-1, `packages/thalo-action/src/action.ts`, `.github/workflows/test-action.yml`):

>       - name: Test action
>         uses: ./packages/thalo-action
>         with:
>           github-token: ${{ secrets.GITHUB_TOKEN }}
>           command: node ../packages/scripts/src/synthesize-with-pi.mjs
>           syntheses: ^typescript-guide
>           working-directory: thalo-test
> --- `.github/workflows/test-action.yml`

The command reads existing synthesis-file content, combines it with the selected entries and prompt, calls a Pi agent and writes updated Markdown plus an actualization checkpoint. Subsequent workspace loading and latest-actualization lookup are included, not just the returning prompt API (SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo/src/services/synthesis.ts`):

> await agent.prompt(userPrompt);
> --- `packages/scripts/src/synthesize-with-pi.mjs`

> await writeFile(absoluteFilePath, updated);
> --- `packages/scripts/src/synthesize-with-pi.mjs`

External dependencies include Node.js, Tree-sitter/native or WASM parser support, the filesystem and Git, the VSCode/LSP host, GitHub Actions and its API, and the Pi packages and OpenAI service used by the shipped command. Their implementations, provider behavior, credentials, deployed services and human PR approval are outside the frozen repository. These exclusions prevent conclusions about provider reliability, enclosing-agent planning, production hosting and actual human acceptance. They do not exclude Thalo's adapters, prompts or Git publication code. A caller-supplied synthesis command is an external extension point; only the shipped command's implementation is frozen (SRC-1, `packages/thalo-action/action.yml`, `packages/thalo-action/src/action.ts`, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo-vscode/src/mod.ts`).

The acquired checkout is frozen at `cdb9aae983e6bc0b75eff1606bc99b088c3aebff`; HEAD matched this pin and the checkout was clean when inspected. The analysis cutoff is 2026-10-14, the supplied run date, not a claim that the source reflects later development. Overall evidence is `code-grounded`: implementation and source-native doctrine are available. No target execution, tests, provider requests or service calls were performed. Test source and a configured workflow are not observed successful operation; they cannot establish synthesis quality, operational reliability or causal improvement.

### Repository coverage

Every tracked top-level file or directory is classified below. Included scope is the run's coverage obligation, not a claim that every file has already been read. All listed implementation paths remain eligible for later inspection at the same commit. No material shipped loop path was unavailable. Items marked not yet inspected are available evidence, not access gaps.

| Top-level item | Inclusion and role | Initial inspection; exclusion or remaining limit |
| --- | --- | --- |
| `.changeset` | Excluded: release bookkeeping. | Tree inventoried; not content-inspected. No release-history assessment. |
| `.claude` | Excluded: repository-development commands in `commands/chore-*.md` and `commands/skill-frontend.md`. | Paths inventoried; not content-inspected. No assessment of agents developing Thalo itself. KB-user prompts under `skills` remain included. |
| `.codex` | Excluded: development skill-discovery link, `skills`. | Git tree identifies a tracked symlink; destination not inspected. No Codex setup assessment. |
| `.gitattributes` | Included: repository Git configuration context. | Available, not yet content-inspected; merge behavior must be grounded in configuration and driver code before assessment. |
| `.github` | Included: synthesis driver and evaluation/build workflow definitions. | Inspected `workflows/test-action.yml`, including checkout, command and KB selection. `workflows/ci.yml` and `workflows/release.yml` inventoried, not yet inspected; no successful CI or deployment conclusion. |
| `.gitignore` | Excluded: checkout hygiene. | Inventoried only. No packaging completeness conclusion. |
| `.oxlintrc.json` | Excluded: code lint configuration. | Inventoried only. No development lint-policy assessment. |
| `.prettierignore` | Excluded: repository formatting exclusions. | Inventoried only. No repository formatting-policy assessment. |
| `CLAUDE.md` | Included: source-native monorepo architecture and development context. | Read package map and tooling declarations; not authority for behavior where code differs. |
| `CONTRIBUTING.md` | Excluded: contributor process. | Inventoried only. No contribution-governance assessment. |
| `LICENSE` | Excluded: legal terms. | Inventoried only. No legal conclusion. |
| `README.md` | Included: target purpose, agent feedback-loop doctrine and synthesis contract. | Read completely; intent is distinguished from implementation. |
| `apps` | Included: CLI and web consumers. Material paths: `thalo-cli/src/mod.ts`, `commands/{init,check,query,actualize,format,lsp,merge-driver,setup-merge-driver}.ts`, `files.ts`; `docs/app/components/playground/`, `docs/app/components/demo/`, `docs/content/docs/` and `docs/content/blog/`. | Traced CLI registration, init persistence, checking, workspace reload, actualize output and merge-driver persistence; read `docs/app/components/playground/thalo-runner.ts`, including workspace synchronization, queries and actualization. Demo state, in-memory filesystem internals, most documentation and remaining CLI command implementations are available, not yet inspected. General web styling, logos, public assets and deployment scaffolding are deliberately excluded; no visual-design or production-web conclusion. |
| `lefthook.yml` | Excluded: developer hooks. | Inventoried only. No hook-enforcement conclusion. |
| `package.json` | Included: monorepo entry scripts and build/test dependencies. | Read completely. Script declarations do not establish execution success. |
| `packages` | Included: `thalo/src/{ast,model,schema,semantic,checker,services,commands,git,merge,vfs}/`, parser and workspace APIs; `grammar/`; `thalo-action/{action.yml,src/}`; `scripts/src/synthesize-with-pi.mjs`; `thalo-lsp/src/`; `thalo-vscode/src/`; `thalo-prettier/src/`; colocated tests. | Read synthesis service and command, tracker factory and timestamp tracker, VFS persistence, action contract and complete action orchestration, complete LSP server and VSCode client, formatter export, and actualize tests. Traced action → command → file write → checkpoint reload and editor disk reload → diagnostics. Grammar internals, Git tracker internals, query/checker rule internals, merge internals, library API consumers and many tests remain available, not yet inspected. `typescript-config` and scripts for PR review/reply or build compatibility are excluded development support; no assessment of those developer workflows. |
| `patches` | Included: parser compatibility context in `web-tree-sitter@0.25.10.patch`. | Inventoried, not yet inspected. No compatibility guarantee. |
| `pnpm-lock.yaml` | Included: dependency-resolution evidence. | Available, not yet inspected. No exact transitive-dependency behavior conclusion. |
| `pnpm-workspace.yaml` | Included: package workspace wiring. | Available, not yet inspected. No build-resolution conclusion beyond inspected entry points. |
| `prettier.config.mjs` | Included: formatter integration context. | Available, not yet inspected; formatter implementation remains in scope. |
| `skills` | Included: shipped KB authoring and maintenance instructions, `thalo/SKILL.md` and `thalo/references/{entities.thalo.txt,example-entries.thalo.txt,scripting-api.md}`. | Read skill completely. References are inventoried, not yet inspected. Skill declarations are doctrine, not proof that initialization creates all files it names. |
| `specs` | Excluded: development process documents `README.md` and `COMMIT.md`. | Read `README.md`; no substantive runtime specification listed there. No development-process assessment. |
| `thalo-test` | Included: shipped KB and synthesis fixtures, `AGENTS.md`, `entities.thalo`, `entries.thalo`, `syntheses.thalo` and Markdown synthesis files. | Read `AGENTS.md`; inventoried retained-content files and found actualization records in example Markdown. Fixture content remains available for later inspection; it is not a retained execution trace. |
| `turbo.json` | Excluded: build orchestration. | Inventoried only. No build-caching or task-scheduling assessment. |

Coverage anchors are SRC-1, `README.md`, `CLAUDE.md`, `package.json`, `apps/thalo-cli/src/mod.ts`, `apps/thalo-cli/src/commands/init.ts`, `apps/thalo-cli/src/commands/check.ts`, `apps/thalo-cli/src/commands/merge-driver.ts`, `apps/docs/app/components/playground/thalo-runner.ts`, `packages/thalo/src/vfs/persistence.ts`, `packages/thalo-lsp/src/server.ts`, `packages/thalo-vscode/src/mod.ts`, `packages/thalo-prettier/src/mod.ts`, `skills/thalo/SKILL.md`, `thalo-test/AGENTS.md` and `specs/README.md`. Tracked-path inventory supplies placement, not behavioral claims for uninspected files.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/rejot-dev/thalo` | cdb9aae983e6bc0b75eff1606bc99b088c3aebff | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/thalo-86fcc3efe983/related-systems/rejot-dev--thalo`. Implementation: CLI registration, init/check/actualize/merge-driver, workspace file loading, synthesis extraction and checkpoint lookup, tracker selection and timestamp filtering, VFS persistence, action orchestration, Pi synthesis writeback, editor reload and browser runner; actualize test source and bounded test-name searches for action, persistence and Git tracking. Doctrine/design: root README and package map, CLI README, action contract/workflow, shipped Thalo skill and example KB instructions, spec-process README. Full tracked root and material subtree inventories. | Implementation: [CLI](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/thalo-cli/src/mod.ts), [actualization](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/commands/actualize.ts), [checkpoint reload](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/synthesis.ts), [action](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-action/src/action.ts), [Pi command](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/scripts/src/synthesize-with-pi.mjs), [browser caller](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/docs/app/components/playground/thalo-runner.ts), [editor reload](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-lsp/src/server.ts). Doctrine/design: [README](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/README.md), [skill](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/skills/thalo/SKILL.md), [shipped driver](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/.github/workflows/test-action.yml). | No repository access gap found. External provider/host implementations and live deployments are not frozen. No observed run or causal experiment supplied: code and test definitions cannot establish actual model quality, successful workflow execution or causal gains. Available paths not initially inspected are listed in coverage, not treated as unavailable. |
