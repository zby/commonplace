---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Sentry Skills as a host-consumed skill and subagent package at frozen commit d18b7aa8ba878354e5c348310230e652f7690f9c."
run-id: AAS-2026-10-14-skills-2719567f917c-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: complete artifact, partial loop
reviewed-boundary: d18b7aa8ba878354e5c348310230e652f7690f9c
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/getsentry/skills
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/getsentry-skills-2719567f917c/related-systems/getsentry--skills
  revision: d18b7aa8ba878354e5c348310230e652f7690f9c
  sha256: null
---

# Sentry Skills boundary

## Boundary and evidence

This run examines Sentry Skills as a package of model-consumed workflows, reference material, subagent prompts and deterministic helper scripts for Sentry employees. Its intended use is engineering and writing assistance, including maintaining the skills themselves. It is an **extension or tool mechanism**, not an enclosing agent runtime. The functional boundary includes the complete repository artifact, including its shipped authoring and evaluation paths. The operational boundary is **complete artifact, partial loop**: the package supplies instructions and helpers, while external agent hosts interpret them, issue model calls and execute tools. The run does not claim to cover those hosts' execution loops or enforcement behavior. SRC-1, `README.md`, `agents/code-simplifier.md`, `skills/skill-writer/SKILL.md`.

> Agent skills for Sentry employees, following the [Agent Skills](https://agentskills.io) open format.
> --- `README.md`

> Restart Claude Code after installation. Skills activate automatically when relevant.
> --- `README.md`

The shipped entry chain is the marketplace entry with source `./`, the root plugin manifest, and repo-root `skills/` and `agents/`. The README also declares installation through skills.sh for compatible agents. Local `.agents/skills` mirrors the canonical skill tree; `CLAUDE.md` is a symlink to `AGENTS.md`. These are distribution and discovery surfaces, not independently implemented runtimes. SRC-1, `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `README.md`, `.agents/skills`, `CLAUDE.md`.

> The canonical skill source for the `sentry-skills` plugin lives at repo-root `skills/`.
> `.agents/skills` mirrors that tree for local agent tooling, and the root plugin manifest loads repo-root `skills/` and `agents/`.
> --- `README.md`

The included maintenance loop routes repository changes through `skill-writer`, which specifies synthesis, iteration, authoring, description optimization, registration and structural validation. Its registration guidance and Python validator are shipped responsibilities, not excluded callers. The evaluator configuration and scenario also belong to the artifact: they install the local skill for Codex, copy repository material into an isolated workspace and judge generated artifacts. AXIS and Codex themselves are external dependencies, not implementations frozen by this run. SRC-1, `AGENTS.md`, `skills/skill-writer/SKILL.md`, `skills/skill-writer/references/registration-validation.md`, `skills/skill-writer/scripts/quick_validate.py`, `skills/skill-writer/EVAL.md`, `skills/skill-writer/evals/axis.config.json`, `skills/skill-writer/evals/scenarios/small-inline-workflow.json`.

> ALWAYS use `/skill-writer` — it handles requirements, writing, registration, and validation.
> --- `AGENTS.md`

> The validator is a structural check. It should fail only for invalid skill format or missing referenced files. The size warning requires author judgment, not a machine gate.
> --- `skills/skill-writer/references/registration-validation.md`

A representative consumption loop is `iterate-pr`: the skill tells the host agent to fetch feedback and checks, fix code, verify locally, commit and push, then monitor again. The bundled monitor implements GitHub CLI polling and terminal markers; it does not implement the model's code-repair decisions. The `agents-md` skill similarly supplies instructions to persist project guidance in `AGENTS.md` and optionally a `CLAUDE.md` symlink, but subsequent host loading remains external. SRC-1, `skills/iterate-pr/SKILL.md`, `skills/iterate-pr/scripts/monitor_pr_checks.py`, `skills/agents-md/SKILL.md`.

> 5. if changed, verify, commit, push, restart loop
> --- `skills/iterate-pr/SKILL.md`

> - If a Claude-compatible entrypoint is required, symlink `CLAUDE.md` to `AGENTS.md`.
> --- `skills/agents-md/SKILL.md`

### Artifact coverage at boundary declaration

The tracked tree was inventoried before classification. Included means inside the functional evidence boundary, not that every file has already been read. Initial inspection traces installation, model-consumed entry points, maintenance, deterministic helpers and an evaluator; leaf-by-leaf behavioral analysis remains later work.

| Top-level tracked path | Treatment and role | Initial inspection and limit |
|---|---|---|
| `.agents/` | Included: local discovery mirror `.agents/skills` | Tracked symlink and README declaration inspected; host discovery implementation is external. |
| `.claude-plugin/` | Included: `marketplace.json`, `plugin.json` installation manifests | Both read completely; installer behavior is not observed. |
| `.claude/` | Included: `settings.json` permissions and skill registration | Read completely; this establishes declared configuration, not enforcement. |
| `.gitignore` | Included: excludes local settings, AXIS reports and editor files | Read completely; ignored execution reports are not supplied evidence. |
| `AGENTS.md` | Included: skill authoring and registration instructions | Read completely. |
| `CLAUDE.md` | Included: alias to repository instructions | Tracked symlink inspected; not a separate instruction source. |
| `CONTRIBUTING.md` | Included: local invocation testing and PR maintenance procedure | Read completely; no local testing was executed. |
| `LICENSE` | Included: repository licensing artifact | Inventoried, contents not yet inspected; no legal interpretation claimed. |
| `README.md` | Included: intended users, installation, skills and subagent inventories, layout and contribution contract | Read completely. |
| `agents/` | Included: `code-simplifier.md`, `senpai.md` model-consumed subagent prompts | Both searched for entry metadata; code-simplifier read completely. Senpai body remains not yet inspected. |
| `skills/` | Included: all canonical `SKILL.md` prompts, bundled references/assets, `SPEC.md` and `SOURCES.md` maintenance records, scripts and evals | Every skill entry scanned for metadata and headings. Full initial reads: agents-md, iterate-pr and skill-writer entry points; skill-writer registration reference, validator, EVAL, AXIS configuration and small-inline scenario; iterate-pr monitor. Other leaf contents remain not yet inspected, not unavailable or excluded. Script entry points were inventoried across gh-review-requests, iterate-pr, skill-scanner and skill-writer. |
| `warden.toml` | Included: skill-scanner registration for pull-request and local triggers | Read completely; Warden execution is external and not observed. |

All coverage claims above refer to SRC-1 and the corresponding commit-relative paths. No material repository subtree is deliberately excluded. The partial-loop designation concerns absent enclosing-host implementations and external service execution, not a narrowed selection of repository skills.

### Frozen evidence and limits

The frozen source is `https://github.com/getsentry/skills` at commit `d18b7aa8ba878354e5c348310230e652f7690f9c`; its read-only access root is the absolute checkout path in frontmatter. HEAD was checked against the acquired pin. The applicability cutoff is **2026-10-14**, the supplied run date; it is not a claim that the commit was authored or released on that date. The overall tier is **code-grounded**, supported by inspected Python implementation and configuration, alongside prompt and maintenance doctrine. No target code, tests, evaluators or examples were executed.

External host runtimes, model providers, plugin/skills installers, AXIS, Warden, GitHub and Sentry/Notion or other service integrations are not separately captured. Their absence prevents conclusions about actual host loading, model compliance, permission enforcement, service-side effects, operational reliability or evaluator effectiveness. Host/tool prerequisites vary by skill; for the inspected PR workflow, authenticated `gh`, `uv` and a target repository are explicitly required. SRC-1, `README.md`, `.claude/settings.json`, `warden.toml`, `skills/iterate-pr/SKILL.md`, `skills/skill-writer/EVAL.md`. Linked upstream documentation supplies no independent frozen evidence here. Unread available repository files are not access gaps. No execution traces, stored evaluator results or causal experiments have been inspected or registered.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/getsentry/skills` | d18b7aa8ba878354e5c348310230e652f7690f9c | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/getsentry-skills-2719567f917c/related-systems/getsentry--skills`. Implementation: complete reads of `skills/skill-writer/scripts/quick_validate.py`, `skills/iterate-pr/scripts/monitor_pr_checks.py`, plugin and project settings, Warden registration, skill-writer AXIS config and small-inline scenario; script entry-point inventory across all bundled scripts. Doctrine/design: complete reads of README, AGENTS, CONTRIBUTING, agents/code-simplifier, agents-md/iterate-pr/skill-writer SKILL files, skill-writer registration reference and EVAL; metadata/heading scans of every skill and both agents. Full tracked tree and symlink entries inventoried. | Implementation: [validator](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/skills/skill-writer/scripts/quick_validate.py), [monitor](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/skills/iterate-pr/scripts/monitor_pr_checks.py), [eval config](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/skills/skill-writer/evals/axis.config.json). Doctrine/design: [README](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/README.md), [skill-writer](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/skills/skill-writer/SKILL.md), [iterate-pr](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/skills/iterate-pr/SKILL.md), [EVAL](https://github.com/getsentry/skills/blob/d18b7aa8ba878354e5c348310230e652f7690f9c/skills/skill-writer/EVAL.md). | No checkout access gap established. Unread leaf files remain available at this same pin. External host and service implementations and actual run results are not frozen: implementation supports helper behavior, doctrine supports prescribed agent behavior, neither proves observed end-to-end operation or causal effectiveness. |
