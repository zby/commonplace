---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Compound Engineering Plugin's shipped skill workflows, knowledge loop, host integrations and improvement tooling at commit 50532b00de523980010d97fe950965b35382a3b7."
run-id: AAS-2026-10-13-compound-engineering-plugin-6ac79f4e7555-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "50532b00de523980010d97fe950965b35382a3b7"
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/EveryInc/compound-engineering-plugin
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/compound-engineering-plugin-6ac79f4e7555/related-systems/EveryInc--compound-engineering-plugin
  revision: 50532b00de523980010d97fe950965b35382a3b7
  sha256: null
---

# Compound Engineering Plugin boundary

## Boundary and evidence

This run examines the complete shipped plugin, not just its converter API or its learning-capture skill. Its intended use is to structure coding-agent work and carry durable project learning into later work. The target is in scope as an **extension or tool mechanism**: model-facing skills direct a host agent, and bundled programs support dispatch, state handling, validation and integration. It is not the enclosing agent runtime. The **whole-system** boundary includes the plugin's workflows, producers and consumers of retained knowledge, maintenance and admission paths, host loading, converter/install tooling, and repository-local improvement and evaluation plane.

The initial trace connects native entry points to their consumers. `package.json` declares Pi resources and the root OpenCode module; `index.js` exports `.opencode/plugins/compound-engineering.js`, which loads skill files and registers them and commands with the host. `.pi/extensions/compound-engineering.ts` supplies skill paths through resource discovery. `.codex-plugin/plugin.json` declares the same skill tree. The separate `src/index.ts` CLI routes install and conversion to `src/commands/install.ts`, `src/commands/convert.ts` and `src/targets/index.ts`; these are shipped distribution paths, not excluded applications (SRC-1 at those paths).

> export default function compoundEngineeringPiExtension(pi: any) {
>   pi.on("resources_discover", async () => ({
>     skillPaths: [skillsDir],
>   }))
> }
> --- `.pi/extensions/compound-engineering.ts`

The knowledge loop is included on both sides of storage. Capture eligibility, writing and grounding are specified by `skills/ce-compound/SKILL.md` and its assembly and grounding references. `skills/ce-compound-refresh/SKILL.md` and `references/per-action-flows.md` maintain, replace, consolidate and delete retained learning. `skills/ce-plan/references/research.md` dispatches the local learnings researcher and reads its output during consolidation. That researcher searches the retained corpus and declared packs. `skills/lfg/SKILL.md` is a shipped caller that conditionally invokes capture after implementation and review; it cannot be excluded merely because it delegates the write (SRC-1 at these paths).

> **Outcome:** one qualifying solved problem is written as a durable learning under `<root>/solutions/`, grounded against the current tree, discoverable by the next agent.
> --- `skills/ce-compound/SKILL.md`

> Open `$SCRATCH_DIR/learnings.md` when that dispatch ran, and show the user any `Skipped pack files` line once.
> --- `skills/ce-plan/references/research.md`

The improvement plane includes the repository-local authoring skill, standing authoring instructions, tests, behavioral evaluation drivers and CI/release gates. These are distinguished from instructions installed into user projects. The target explicitly states this distinction (SRC-1, `AGENTS.md`):

> `AGENTS.md`, `CLAUDE.md` (symlink to `AGENTS.md`), and `GEMINI.md` are authoring context for this source repository. Skills are installed into end-user environments, where they run against the user's local instruction files, not this repo's. Behavioral rules that must affect a skill at runtime belong in that skill's `SKILL.md` or files under its own `references/` directory.
> --- `AGENTS.md`

### Frozen revision and evidence limits

The sole frozen source is SRC-1 at **50532b00de523980010d97fe950965b35382a3b7**, with applicability cutoff **2026-10-13** from the opening input. The acquired checkout's HEAD matches the pin and its status was clean. The acquired source object is retained unchanged in frontmatter. The cutoff is the run date, not a claim that upstream changes after this commit were reviewed.

The overall tier is **code-grounded**: executable resource loading, CLI dispatch, pack resolution and evaluation drivers were inspected alongside model-facing instructions. Skill prose supplies doctrine/design evidence; it does not itself demonstrate that an agent obeyed it. No target execution, installation, tests or model calls were performed. Supplied tests and evaluation drivers are inspectable implementation, not newly observed runs. The source register does not claim observed-run or causal-experiment evidence merely because the repository contains fixtures and authored reports.

External dependencies include enclosing coding-agent hosts and their skill loaders, model providers, native subagent facilities or companion packages, and the Node/npx/acpx and local agent-CLI transport used by cross-model routes. The initial cross-model trace includes `skills/ce-work/references/cross-model-execution.md`, `skills/ce-work/scripts/cross-model-work.sh` and `skills/ce-work/scripts/peer-job-runner.py` (SRC-1). Their host-facing protocol is included; implementations of external hosts, transport packages and services are not frozen here. This prevents conclusions about host scheduling internals, provider-side memory, actual permission enforcement across every host, or actual served-model identity. Third-party packs, live project repositories and real user sessions are not supplied captures: their absence prevents conclusions about installed-project learning quality, successful later reuse, or improvement attributable to the plugin. The included resolver and session-history tooling may still establish how those inputs are requested and consumed.

There is no identified source-access gap. Uninspected files at this commit remain available evidence, not missing evidence. Initial inspection establishes the boundary and principal shipped loop; it is not a claim that every skill or every platform adapter has already received a behavioral audit.

### Top-level coverage

Every top-level tracked entry is classified below. All rows refer to SRC-1. “Included” denotes functional coverage by this run, not a claim of exhaustive initial reading. “Indexed” means the tracked paths were enumerated but their bodies were not yet inspected. Directory rows identify material paths rather than treating a directory label as evidence of loop coverage.

| Top-level entry | Coverage and material paths | Role and initial inspection; exclusion limit |
|---|---|---|
| `skills/` | Included: each `SKILL.md`, local references/personas, scripts, schemas and assets; especially capture, refresh, plan, work, review, setup, handoff and `lfg` | Runtime workflow and knowledge production/admission/maintenance/consumption. Read capture and refresh kernels, capture assembly/grounding, refresh action flows, planning research and researcher, `lfg`, setup directive, cross-model execution; inspected ranges/searches of runner, adapter and pack resolver. Remaining skill bodies indexed, not an access gap. |
| `src/` | Included: `index.ts`, `commands/`, `parsers/`, `converters/`, `targets/`, `utils/`, `data/`, `dev/`, `release/`, `types/` | Distribution, conversion, cleanup, development loading and release admission. Read CLI entry, install, convert and target registry; underlying parsers/writers and other utilities indexed for later tracing. |
| `tests/` | Included: converter/host/skill contract tests, `skills/`, `fixtures/`, `skill-eval-cell/`, `windows/` | Mechanical and behavioral evaluation plane. Read eval-cell README, host planner, and run-driver setup/dispatch/persistence ranges; other test bodies indexed. Fixtures are not assumed to be real successful production traces. |
| `.agents/` | Included: `plugins/marketplace.json`, `skills/ce-skill-work/` and its references | Catalog routing and repository-local skill improvement. Read authoring kernel, searched marketplace source fields; mode references indexed. |
| `.claude/` | Included: `skills` link and `commands/triage-prs.md` | Repository-local discovery and maintenance caller; indexed and identified by authoring instructions, not assumed to be installed end-user instructions. |
| `.claude-plugin/` | Included: plugin/marketplace manifests and changelog pointer | Native distribution entry points; manifest fields searched, CI validation path read. |
| `.codex-plugin/` | Included: `plugin.json` | Native consumer routing to `skills/`; full manifest read. |
| `.cursor-plugin/` | Included: plugin/marketplace manifests and changelog pointer | Native distribution; plugin fields searched, remaining metadata indexed. |
| `.devin-plugin/`, `.grok-plugin/`, `.kimi-plugin/` | Included: plugin manifests and available marketplace catalogs | Native distribution; manifest fields searched, catalog bodies indexed. |
| `.omp-plugin/` | Included: `marketplace.json` | Native catalog entry; source routing searched, installation contract read in README. |
| `.agy/` | Included: `plugin.json`, `skills` link, `INSTALL.md` | Compatibility distribution surface; manifest searched, README installation contract read; local install document indexed. |
| `.cline/` | Included: `INSTALL.md`, `scripts/install-skills.sh` | Shipped install caller; README invocation traced to this script, script body indexed. |
| `.opencode/` | Included: `plugins/compound-engineering.js`, `INSTALL.md` | Executable native skill/command loader; full implementation read, install document indexed. |
| `.pi/` | Included: `extensions/compound-engineering.ts` | Executable resource discovery; full implementation read. |
| `.compound-engineering/` | Included: `config.example.yaml` | Shipped config surface for consumer workflows; path indexed, configuration consumers traced in skill instructions and resolver. |
| `.cursor/` | Included: `BUGBOT.md`, `environment.json` | Repository-local review/environment setup; indexed, not evidence of user-project runtime behavior. |
| `.github/` | Included: CI, acpx canary, release/preview/pages workflows, release metadata and PR template | Admission, evaluation and distribution plane. CI read completely; remaining workflow bodies indexed. Third-party action implementations are external. |
| `scripts/` | Included: test runner, acpx pin updater, Codex development and release preview/sync/validation drivers | Shipped improvement and release callers, not external applications. Commands registered by inspected `package.json`; driver bodies indexed. |
| `docs/` | Included: `guides/`, `install/`, `specs/`, `solutions/`, `development.md`, plans, brainstorms, ideation and dogfood reports | User contracts and repository-retained design/learning/evaluation material. Tree indexed and dependencies traced from inspected prompts. Historical plans and reports are attributed evidence only; their existence establishes neither adoption nor successful operation. |
| `site/` | Included: configuration, `_plugins/`, `_includes/`, navigation, linked guides/assets, install/upgrading pages, tests and build files | Documentation distribution, identified in `AGENTS.md` and package scripts; indexed, rendering internals not yet inspected. |
| `assets/` | Included: demo README/tape/replay script and explainer JavaScript; image branding is incidental | Presentation and reported-operation surface. Indexed only; no demonstrated later reuse inferred from the README's demo claim. |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | Included | Repository authoring instructions and aliases; read initial AGENTS sections including runtime/authoring distinction, indexed aliases. |
| `CONCEPTS.md`, `STRATEGY.md`, `CODING_STANDARDS.md`, `CONTRIBUTING.md` | Included | Vocabulary, design intent, authoring standards and contribution admission; concepts/strategy headings searched, remaining bodies indexed. |
| `README.md`, `CHANGELOG.md` | Included | Full README read for entry points, workflow and dependency contracts; changelog pointer indexed. |
| `package.json`, `plugin.json`, `index.js` | Included | Package resources, commands, root manifest and executable host export; all read completely. |
| `bun.lock`, `bunfig.toml`, `tsconfig.json`, `.gitattributes`, `.gitignore` | Included | Dependency/build/test and tracking configuration; indexed. Dependency bodies and actual build/test results are not established by configuration. |
| `LICENSE`, `PRIVACY.md`, `SECURITY.md`, `favicon.png` | Excluded from functional analysis | Legal/policy and incidental branding surfaces, indexed and available. Prevents a legal, privacy-policy or vulnerability-disclosure-process assessment; excludes no workflow or knowledge-loop responsibility. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/EveryInc/compound-engineering-plugin` | 50532b00de523980010d97fe950965b35382a3b7 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/compound-engineering-plugin-6ac79f4e7555/related-systems/EveryInc--compound-engineering-plugin`. Entire tracked tree enumerated. Implementation: `index.js`, `.opencode/plugins/compound-engineering.js`, `.pi/extensions/compound-engineering.ts`, `src/index.ts`, `src/commands/install.ts`, `src/commands/convert.ts`, `src/targets/index.ts`; selected resolver/adapter/runner ranges and searches; eval-cell `hosts.ts` and run-driver setup/dispatch/persistence. Doctrine/design: full README, manifests, capture/refresh kernels and action/grounding references, planning research and learnings researcher, `skills/lfg/SKILL.md`, setup compounding directive, cross-model execution contract, repository-local authoring kernel, initial AGENTS sections and CI. | Implementation: [OpenCode loader](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/.opencode/plugins/compound-engineering.js), [Pi loader](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/.pi/extensions/compound-engineering.ts), [eval host planner](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/tests/skill-eval-cell/hosts.ts). Doctrine/design: [capture](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/skills/ce-compound/SKILL.md), [planning consumer](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/skills/ce-plan/references/research.md), [refresh](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/skills/ce-compound-refresh/SKILL.md), [authoring boundary](https://github.com/EveryInc/compound-engineering-plugin/blob/50532b00de523980010d97fe950965b35382a3b7/AGENTS.md). | No identified checkout access gap. External host/provider/transport implementations, third-party pack contents and real project/session evidence are not captured. Implementation supports inspected source behavior, not successful execution. Doctrine/design supports prescribed workflows, not compliance, successful later knowledge activation or causal improvement. Indexed but unread paths remain available within this registered commit. |
