---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MDCP's shipped documentation skill, maintenance workflows and compile/check toolchain at commit 1a198715a4da72dd89bad93f84cf5d4b3ab56b01."
run-id: AAS-2026-11-08-mdcp-1e4e8314c1e4-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/betsalel-williamson/mdcp
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/mdcp-b6e2b2e8741f/related-systems/betsalel-williamson--mdcp
  revision: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
  sha256: null
---

# MDCP boundary

## Boundary and evidence

This run analyses MDCP as a repository-based documentation and context system for agents and humans. Its intended use is keeping durable intent in small Markdown shards, discovering the relevant shard for later work, updating it before implementation, and compiling and checking the documentation. It qualifies as a memory/knowledge/context-engineering system through its shipped agent instructions and retained-document workflow, not because its TypeScript compiler itself calls a model. SRC-1, `README.md` and `skills/mdcp/SKILL.md` distinguish the agent skill from its deterministic toolchain.

> **mdcp** (MarkDown Context Protocol) is a **documentation system** delivered as an [Agent Skill](https://agentskills.io) plus a small compile/check toolchain.
> --- `README.md`

> Discover the relevant shard with host search (`rg`, IDE search) or the guide
> `index.md`, then open **one** `.md` shard. Broader reads of compiled output are
> last resort.
> --- `skills/mdcp/SKILL.md`

The boundary is **whole-system** for MDCP's shipped documentation loop. It includes the parent skill, complementary archetype skills, workflow and review references, CLI and core, lint presets, local host setup, repository dogfooding, publication consumers, tests and optional skill-evaluation tooling. The enclosing agent host supplies inference, filesystem and search tools, conversational state, and any scheduling. Those host responsibilities are dependencies, not MDCP runtime capabilities. The repository describes the application as a CLI rather than a long-running server (SRC-1, `AGENTS.md`).

Initial tracing covers these material handoffs:

- **Produce and maintain:** the skill instructs agents to edit source shards and update indexes; the feature workflow writes documentation before code; the doc-review workflow directs merge, split, move, reword, link and delete decisions. This is shipped doctrine, not proof of agent compliance (SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`, `skills/mdcp/references/workflows/doc-review.md`).
- **Persist and derive:** the `mdcp` executable invokes the core through `compile-workspace.ts`; core assembly reads guide indexes and shard files, and output writing persists compiled guides. The refs registry is written as JSON and later read by CLI commands. The analysis includes these shipped callers, not merely the core API (SRC-1, `packages/mdcp-cli/package.json`, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-cli/src/compile-workspace.ts`, `packages/mdcp-core/src/compile/assemble.ts`, `packages/mdcp-core/src/refs/registry.ts`).
- **Admit and repair:** CLI `check` combines orphan checks, compilation, refs, link checks, configured peer linters, optional path checks and coverage policy. `review` reports mechanical sprawl signals; the skill's review workflow supplies interpretive decisions. Repository CI invokes skill validation, docs checks and compilation, then checks for a diff. A check pass is not established semantic truth (SRC-1, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-core/src/validate/review.ts`, `.github/workflows/ci.yml`, `skills/mdcp/references/workflows/doc-review.md`).
- **Reload and consume:** later agent tasks are instructed to find and read source shards using host search or indexes. CLI `refs-list` reloads the registry. The site generator reads shards, compiled outputs and refs, resolves slug ownership, and writes pages and navigation. Root scripts and `docs/mdcp.config.json` wire this repository's README, developer guide, package guides and presentation outputs into that loop (SRC-1, `skills/mdcp/SKILL.md`, `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-site/scripts/sync-content.mjs`, `package.json`, `docs/mdcp.config.json`).
- **Evaluate:** unit/smoke tests and live skill fixtures are within scope. The optional live-evaluation instructions call for with/without-skill runs and grading; the vendored trigger evaluator launches `claude -p`. These are evaluator paths, not a production MDCP inference engine. No evaluation was executed or run result inspected for this boundary (SRC-1, `docs/developer/live-skill-evals.md`, `tests/skills/mdcp/evals/README.md`, `.agents/skills/skill-creator/scripts/run_eval.py`).

> - Shards under `docs/**/` are the source of truth.
> --- `skills/mdcp/SKILL.md`

> `mdcp check` validates structure, not truth.
> --- `skills/mdcp-arch-research/SKILL.md`

### Repository coverage

The tracked root tree was enumerated at the frozen commit. Every top-level entry is classified below. “Included” establishes functional scope, not exhaustive inspection of every file. Material loop entry points and their consumers above were inspected; other included files remain available for detailed analysis. No material loop path was inaccessible. The roles below are grounded in SRC-1's tree, `package.json`, `AGENTS.md`, `docs/mdcp.config.json` and the specifically named entry points.

| Top-level tracked entry | Treatment and role; inspection status or exclusion limit |
| --- | --- |
| `skills/` | Included: `mdcp/SKILL.md`, workflow and review references produce, retrieve and maintain shards; `mdcp-arch-*` supply architecture overlays. Parent skill, feature and doc-review workflows, and research overlay inspected initially; remaining overlays/references included for later detail. |
| `packages/` | Included: `mdcp-cli/src/cli.ts` and `compile-workspace.ts` drive core; `mdcp-core/src/compile/`, `refs/`, `links/`, `validate/`, `config/` implement derivation and checks; `mdcp-presets/` supplies lint rules; `mdcp-site/scripts/sync-content.mjs` consumes retained material for publication; `skill-mdcp*` carry skill versions. Initial inspection traced CLI, core exports, assembly reads/writes, refs persistence, review signals, site generation and parent skill carrier. Package tests are included, not run. |
| `docs/` | Included: `mdcp.config.json` wires outputs; `features/` contains protocol, design, workflows and source-native research; `client-cli/` and `client-core/` document interfaces; `developer/` covers maintenance and evals; `glossary/` supplies reusable definitions; `repo-readme/` and `presentation-la-devops/` feed outputs; lint configuration/styles participate in validation. Config and live-eval maintainer instructions inspected initially; not all documentation or research records read. |
| `tests/` | Included: `skills/mdcp/evals/` prompts, assertions and fixture repositories test routing and maintenance behavior. Suite README inspected; fixtures and assertions available for later analysis, not treated as actual operation. |
| `.agents/` | Included as a maintainer improvement plane: vendored `skill-creator/` instructions, graders, comparator, scripts and viewer; `writing-skills/` authoring guidance. Trigger evaluator inspected at its model-launch path; broader helper behavior not yet assessed. Not attributed to MDCP's production CLI. |
| `.claude/` | Included host integration: `settings.json` registers `hooks/session-start.sh`, which installs dependencies, builds and installs the checkout's skill for remote sessions. Both inspected; host execution not observed. |
| `.cursor/` | Included local host setup via `environment.json`; tree identified, detailed configuration not initially inspected. No claim about successful cloud provisioning. |
| `.github/` | Included admission/publication integration: `workflows/ci.yml`, pages and release workflows, issue/adoption templates and ownership/security automation. CI docs/skill gate inspected; other workflows remain available, with no claim of successful runs. |
| `scripts/` | Included maintenance/evaluation tooling: context-size and performance benches, skill validation/version synchronization, release scripts, formal checking and test/report helpers. Root script consumers and `release-build.mjs` inspected; benchmarks not run and their results not presumed. |
| `examples/` | Included `sample-guides/` config, indexes, refs, inserts, tables and media as shipped compile/check examples. Tree and root check wiring inspected; no example executed. |
| `presentations/` | Included `la-devops-2026.md` as a generated retained-document consumer/output. Config and root render/compile wiring inspected; presentation not independently evaluated. |
| `AGENTS.md`, `CLAUDE.md` | Included repository-agent entry instructions and their alias; `AGENTS.md` inspected for shard discipline, output map and CLI responsibilities. |
| `README.md`, `DEVELOPERS.md` | Included generated entry and contributor guides; README inspected, developer output mapped through config and source instructions. They are not independent corroboration of their source shards. |
| `package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml` | Included command routing, workspace and dependency boundary. Root package scripts inspected; dependency implementations outside this repository are not frozen here. |
| `skills-lock.json`, `skills.sh.json` | Included skill discovery/provenance metadata; skills directory grouping inspected, lock contents not initially assessed. |
| `.changeset/` | Included release-maintenance metadata and pending release notes, not current product truth. Tree and root script usage inspected; no release outcome inferred. |
| `.husky/` | Included local commit gate integration (`pre-commit`, `commit-msg`); tree and root package wiring identified; hook internals not initially assessed. |
| `formal/`, `infra/` | Deliberately excluded from detailed analysis: `formal/alloy/landing.als` and `infra/github/` govern repository landing/protection rather than the documentation-state loop. Prevents conclusions about formal verification, deployed GitHub protection or infrastructure correctness. |
| `legacy/` | Deliberately excluded historical shell/Python compile, shard and validation toolchain. The current package entry points are the target; no behavioral equivalence or migration-correctness claim for legacy scripts. |
| `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | Deliberately excluded governance/legal detail; no legal assessment or security-response audit. README's archive notice remains in scope as target status doctrine. |
| `.gitignore`, `.gitleaks.toml`, `.markdownlintignore`, `.npmrc`, `.nvmrc`, `.prettierignore`, `.prettierrc.json`, `commitlint.config.mjs`, `eslint.config.mjs`, `tsconfig.base.json` | Included supporting build, formatting, security-scan and repository hygiene configuration; identified by tree and package wiring, not individually audited. Their presence does not establish security or formatting effectiveness. |

### Frozen evidence and limits

The source is the acquired checkout at **1a198715a4da72dd89bad93f84cf5d4b3ab56b01**, with applicability cutoff **2026-11-08**. Its HEAD matched the acquired pin. The evidence tier is **code-grounded**: implementation text supports toolchain structure, while skills and workflow prose support declared agent behavior. This boundary does not register an observed run or causal experiment.

The README and skill announce that MDCP is archived and renamed Merlon Docs (SRC-1, `README.md`, `skills/mdcp/SKILL.md`). The successor repository is not part of the frozen source. This prevents conclusions about successor features, compatibility in practice or current support beyond what this commit declares; it does not require changing this run's target or source identity.

External agent hosts, model providers, Git/PR services, the skills installer, Node/pnpm, md-tree and optional peer tools such as Vale, Prettier and Markdown linters are dependencies rather than additional frozen sources (SRC-1, `README.md`, `package.json`, `packages/mdcp-cli/src/cli.ts`, `skills/mdcp/SKILL.md`). Their actual behavior, service availability and installed versions are not verified here. No target, test, example, model call or benchmark was executed. Consequently this run cannot infer actual agent adherence, cross-session retrieval success, throughput, cost or comparative effectiveness from source structure alone. Files not initially inspected are inspection limits, not access gaps.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/betsalel-williamson/mdcp` | 1a198715a4da72dd89bad93f84cf5d4b3ab56b01 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/mdcp-b6e2b2e8741f/related-systems/betsalel-williamson--mdcp`. Implementation: `packages/mdcp-cli/src/cli.ts`, `packages/mdcp-cli/src/compile-workspace.ts`, `packages/mdcp-core/src/index.ts`, selected assembly read/write paths in `packages/mdcp-core/src/compile/assemble.ts`, `packages/mdcp-core/src/refs/registry.ts`, signal construction in `packages/mdcp-core/src/validate/review.ts`, `packages/mdcp-site/scripts/sync-content.mjs`, host hook/settings, CI docs gate, release-build script and vendored trigger evaluator launch path. Doctrine/design: README, AGENTS, root/CLI/skill-carrier manifests, parent skill, feature and doc-review workflows, research archetype, docs config, maintainer live-eval instructions, suite README and skills grouping. Entire tracked tree enumerated; detailed scope recorded above. | Implementation: [CLI](https://github.com/betsalel-williamson/mdcp/blob/1a198715a4da72dd89bad93f84cf5d4b3ab56b01/packages/mdcp-cli/src/cli.ts), [refs](https://github.com/betsalel-williamson/mdcp/blob/1a198715a4da72dd89bad93f84cf5d4b3ab56b01/packages/mdcp-core/src/refs/registry.ts), [site consumer](https://github.com/betsalel-williamson/mdcp/blob/1a198715a4da72dd89bad93f84cf5d4b3ab56b01/packages/mdcp-site/scripts/sync-content.mjs). Doctrine/design: [skill](https://github.com/betsalel-williamson/mdcp/blob/1a198715a4da72dd89bad93f84cf5d4b3ab56b01/skills/mdcp/SKILL.md), [review workflow](https://github.com/betsalel-williamson/mdcp/blob/1a198715a4da72dd89bad93f84cf5d4b3ab56b01/skills/mdcp/references/workflows/doc-review.md), [eval instructions](https://github.com/betsalel-williamson/mdcp/blob/1a198715a4da72dd89bad93f84cf5d4b3ab56b01/docs/developer/live-skill-evals.md). | No inaccessible material shipped loop identified. External hosts, dependencies and successor repository are not captured; no observed run or experiment registered. Source text establishes implementation and prescribed use, not successful operation or causal benefit. |
