---
description: "getsentry/skills review: Sentry Claude Code marketplace of Markdown skills, subagents, settings allowlists, script helpers, and Warden skill scanning"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-01"
---

# getsentry/skills

`getsentry/skills` is Sentry's repository of reusable agent skills and subagents for Claude Code and agentskills-compatible hosts. It is not a vector memory store or autonomous learning system; it is a retained system-definition library: Markdown skills, optional maintenance specs and references, helper scripts, plugin manifests, Claude settings, and a Warden review configuration that make Sentry-specific workflows available to agents.

**Repository:** https://github.com/getsentry/skills

**Reviewed commit:** [b10e2db21d3165de1904bdf3fa64285016765fe5](https://github.com/getsentry/skills/commit/b10e2db21d3165de1904bdf3fa64285016765fe5)

**Last checked:** 2026-06-01

## Core Ideas

**The repo is an installable skill marketplace, not only a folder of prompts.** The marketplace manifest exposes one `sentry-skills` plugin whose source is the repository root, while the plugin manifest names the same root plugin for Claude Code installation (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude-plugin/marketplace.json, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude-plugin/plugin.json). The README makes `skills/` and `agents/` the canonical payloads and documents both Claude plugin installation and `npx skills add` installation for broader agentskills-compatible hosts (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md).

**Skills are behavior-shaping instruction packages.** I found 27 canonical `skills/*/SKILL.md` files, each with trigger-oriented frontmatter and runtime instructions. Some are compact prose workflows such as `commit`, `pr-writer`, and `code-review`; others are reference-backed expert systems such as `security-review`, `gha-security-review`, `skill-scanner`, `prompt-optimizer`, and `skill-writer` (https://github.com/getsentry/skills/tree/b10e2db21d3165de1904bdf3fa64285016765fe5/skills, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/security-review/SKILL.md, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/SKILL.md). Their behavioral authority comes from the host loading them as skills, not from an internal runtime in this repo.

**Context efficiency is mostly progressive disclosure.** The system relies on concise descriptions for initial skill selection, `SKILL.md` as the first loaded router, and optional `references/`, `SPEC.md`, `SOURCES.md`, and `scripts/` files for deeper branches. `skill-writer` is the clearest self-description of the pattern: it tells agents to load only the reference files needed for the current step and keeps `SKILL.md` as a runtime router rather than an encyclopedia (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/SKILL.md). The README and AGENTS instructions also cap `SKILL.md` length and push source inventories and maintenance rules into side files (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/AGENTS.md).

**Repository-local settings make the package concrete for Claude Code.** `.claude/settings.json` grants read-oriented shell commands, selected WebFetch domains, every canonical `Skill(sentry-skills:...)` entry, and `enableAllProjectMcpServers: true` (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude/settings.json). That file is a symbolic system-definition artifact: it does not itself decide which skill is relevant, but it changes which skill and command surfaces the host may use.

**A small subset of skills has executable helper scripts.** `skill-writer` includes `quick_validate.py` for structural checks on `SKILL.md`; `skill-scanner` includes `scan_skill.py` for static security scanning; `iterate-pr` includes scripts for PR checks, review feedback, check monitoring, and thread replies; `gh-review-requests` includes a GitHub notification filter (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/scripts/quick_validate.py, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-scanner/scripts/scan_skill.py, https://github.com/getsentry/skills/tree/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/iterate-pr/scripts, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/gh-review-requests/scripts/fetch_review_requests.py). The scripts make parts of governance and workflow automation testable, but most skill behavior remains prose interpreted by an agent.

**Skill governance is emerging as its own workflow.** New or materially changed skills are supposed to include `SPEC.md`, registration in README, registration in `.claude/settings.json`, and an allowlist update in `claude-settings-audit` (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/AGENTS.md, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md). Warden is configured to run `skill-scanner` against `**/skills/**` on pull requests and locally, failing on high findings and reporting medium findings (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/warden.toml, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.github/workflows/warden.yml).

## Artifact analysis

- **Storage substrate:** `files` — Repository files under `.claude-plugin/`
- **Representational form:** `symbolic` — Symbolic JSON metadata

**Plugin and marketplace manifests.** The storage substrate is repository files under `.claude-plugin/`. The representational form is symbolic JSON metadata. Lineage is authored repository configuration. Behavioral authority is system-definition authority at install time: it identifies the plugin package and makes root-level skills and agents installable through Claude Code's marketplace flow. It does not perform runtime selection itself.

**Claude settings allowlist.** The storage substrate is `.claude/settings.json`. The representational form is symbolic permission and capability configuration. Lineage is authored and must be manually updated when new canonical skills are added. Behavioral authority is system-definition authority over which tools, WebFetch domains, MCP servers, and skill identifiers the host may use. The file broadens the available action surface, but relevance and invocation are host-mediated.

**Skill packages.** The storage substrate is the git repository's `skills/<name>/` directories. The representational form is mixed: Markdown prose, YAML frontmatter, optional `allowed-tools`, routed reference files, `SPEC.md` maintenance contracts, `SOURCES.md` inventories, licenses, and occasional scripts. Lineage is mostly authored, adapted, or vendored; some specs name historical examples or observed outcomes as future improvement sources, but I did not find an implemented trace-to-skill derivation pipeline. Behavioral authority is system-definition authority when a host loads the skill: the package instructs the agent, constrains tools when supported, and supplies workflow rules. Reference files and examples inside the package are knowledge artifacts until the active `SKILL.md` routes the agent to consume them.

**Helper scripts.** The storage substrate is Python files under skill-local `scripts/` directories. The representational form is symbolic executable code with PEP 723 dependency headers in several scripts. Lineage is authored implementation supporting a prose skill contract. Behavioral authority is system-definition and evaluation authority when invoked: scripts classify PR feedback, extract CI snippets, scan skills for dangerous patterns, or validate skill structure. They are not automatic hooks in this repository; the active skill or Warden configuration has to call them.

**SPEC and SOURCES side files.** The storage substrate is optional Markdown files beside `SKILL.md`. The representational form is prose plus structured headings for intent, scope, trigger context, source/evidence model, reference architecture, evaluation, limitations, and maintenance notes. Lineage is authored maintenance metadata. Behavioral authority is mostly knowledge artifact authority for maintainers and future agents; it can become system-definition authority when `skill-writer` or a reviewer uses it to decide whether a skill change is acceptable.

**Subagent definitions.** The storage substrate is `agents/senpai.md` and `agents/code-simplifier.md`. The representational form is mixed Markdown frontmatter and prose behavior instructions. Lineage is authored or adapted; `code-simplifier` cites Anthropic's plugin example in an HTML comment (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/agents/code-simplifier.md). Behavioral authority is system-definition authority when the host launches the subagent with its model, tools, persona, and task boundary (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/agents/senpai.md).

**Warden review configuration.** The storage substrate is `warden.toml` plus the GitHub Actions workflow. The representational form is symbolic configuration and CI workflow YAML. Lineage is authored repository governance. Behavioral authority is evaluation and gate authority over skill changes: Warden is configured to run the `skill-scanner` skill on PR events affecting skills, with severity thresholds. This is a review/evaluation path, not a memory read-back path for a working agent.

**Promotion path.** The strongest implemented promotion path is manual: proposed skill knowledge becomes `SKILL.md`, optional `SPEC.md`/`SOURCES.md`/references/scripts, README inventory entries, settings allowlist entries, and Warden-scanned PR changes. `skill-writer` gives a richer process for source capture, examples, validation, and iteration, but the reviewed repo implements that as instructions plus a structural validator rather than as an automatic trace-derived learner.

## Comparison with Our System

| Dimension | getsentry/skills | Commonplace |
|---|---|---|
| Primary purpose | Distribute Sentry-specific agent skills, subagents, and workflow helpers | Maintain a typed methodology KB with reviews, notes, sources, instructions, and validation |
| Canonical substrate | Git-tracked Markdown skill packages, plugin manifests, settings JSON, Python helper scripts | Git-tracked Markdown collections with type specs, schemas, indexes, source snapshots, and review reports |
| Main retained artifact | System-definition artifacts that instruct or constrain agents | Knowledge artifacts and system-definition artifacts separated by collection/type and validation rules |
| Retrieval/activation | Host skill discovery by description, explicit `/skill`, settings allowlist, plugin installation, Warden PR triggers | Explicit lexical search, indexes, authored links, skills, validation, and review workflows |
| Governance | Registration checklist, optional SPEC/SOURCES, quick validation, skill scanner, Warden thresholds | Collection contracts, type specs, frontmatter schemas, validation, semantic review, git lifecycle |
| Context control | Progressive disclosure through `SKILL.md` routers and reference files | Collection routing, generated indexes, scoped source snapshots, artifact types, and review gates |

The closest Commonplace analogue is not the note library; it is `kb/instructions/` plus installed skills. Both systems store behavior-shaping prose in git and rely on agents to read the right artifact at the right time. The difference is authority. `getsentry/skills` is meant to be installed into a host as runtime instruction packages, while Commonplace's KB artifacts remain more explicitly typed by register, source status, validation state, and review workflow.

`getsentry/skills` is stronger on adoption packaging. Claude plugin manifests, README installation commands, a settings allowlist, and a root `skills/` tree make the system easier to install as a team-wide instruction distribution channel. Commonplace is stronger on artifact taxonomy and durable review. It makes the distinction between knowledge artifact, instruction, source, review, and generated index explicit, while `getsentry/skills` leaves many authority distinctions implicit inside skill prose and optional specs.

**Read-back:** `pull` — Memory-only. Agents and maintainers can deliberately read or invoke the repository's skill packages, helper scripts, settings, and Warden configuration, but host-selected `SKILL.md` files and Warden-triggered `skill-scanner` runs are shipped system-definition surfaces, not accumulated memory read-back; I did not find code implementing relevance-gated memory injection into an agent's context

### Borrowable Ideas

**Installable skill marketplace packaging.** Commonplace could package promoted operational skills with a small manifest and installation path instead of relying only on repo-local discovery. Ready as a packaging pattern if the target host is explicit.

**A `SPEC.md` maintenance contract beside runtime instructions.** Sentry's split between runtime `SKILL.md` and maintenance `SPEC.md` maps cleanly onto Commonplace instructions. Ready now for complex skills where intent, scope, evidence, and evaluation should not pollute runtime context.

**Skill-scanner as a governance gate.** A deterministic scan for frontmatter problems, hidden prompt injection, symlinks, scripts, secrets, and excessive permissions would fit Commonplace's validation philosophy. Ready as a narrow validator, with human review required for false positives.

**Path-gated review for skill changes.** Warden's `paths = ["**/skills/**"]` pattern is a useful trigger boundary: skill edits deserve different review checks from ordinary documentation edits. Ready as a CI/review-bundle idea.

**Routed reference tables for context efficiency.** `skill-writer`'s "open when you need to..." tables are a good pattern for keeping runtime instructions small while preserving depth. Ready now for large Commonplace skills.

**Do not borrow host activation as proof of read-back quality.** Description-based skill selection is useful, but the repo does not provide precision/recall evidence or an ablation showing that activated skills change outcomes. Commonplace should keep activation claims separate from effective behavioral authority.

## Curiosity Pass

**The repository is more governance system than memory system.** Its retained artifacts mostly shape agent behavior as instructions, permissions, workflows, and checks. It stores little episodic or factual memory about prior work.

**The README's "skills activate automatically when relevant" claim is host-level behavior.** The repo supplies descriptions and registration; the relevance matcher lives outside the reviewed code (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md). That is enough to explain intended use, but not enough to assign `push-activation`.

**Only a minority of skills have `SPEC.md`.** The repo says new and materially changed skills should include a spec, but only some current skills do. This suggests the maintenance-contract pattern is newer or selectively applied.

**Some skills carry high authority through ordinary prose.** `commit` says agents must always use it before committing, `triage-frontend-issues` can update Sentry issues through MCP after user approval, and `iterate-pr` can commit and push fixes in a loop (https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/commit/SKILL.md, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/triage-frontend-issues/SKILL.md, https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/iterate-pr/SKILL.md). The authority is real once loaded, even though the implementation is mostly Markdown.

**The settings allowlist is broad in one important place.** `enableAllProjectMcpServers: true` delegates substantial trust to project MCP configuration. That may be normal for Sentry workflows, but it is a stronger ambient capability than the mostly read-only Bash allowlist.

## What to Watch

- Whether the host exposes skill-selection logs, scores, or budgets. That would make activation quality reviewable instead of inferred from descriptions.
- Whether more skills adopt `SPEC.md`, `SOURCES.md`, and evidence references. If adoption becomes consistent, the repo moves closer to a typed instruction library.
- Whether Warden's skill-scanner results become durable review artifacts with stable provenance. That would strengthen the governance path from "configured scan" to auditable validation history.
- Whether `skill-writer` grows an implemented examples-to-skill revision loop. That would need a fresh trace-derived assessment if runtime traces or positive/negative examples are transformed into durable skill edits by code.
- Whether helper scripts drift from their `SKILL.md` contracts. The scripts carry the strongest executable authority, so they need tighter validation than prose-only skills.
- Whether plugin installation and settings allowlist rules become more portable across agentskills-compatible hosts. Current packaging is strongest for Claude Code.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: installed skills exist as retained behavior-shaping artifacts, but relevance and use are host-mediated.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: manifests, settings, skill prose, references, scripts, specs, and subagents differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: references, examples, sources, and specs often serve as evidence or maintenance context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: loaded skills, settings allowlists, scripts, subagent definitions, and Warden configuration instruct, route, validate, or constrain behavior.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - relates: routed `SKILL.md` tables and reference files frontload navigation decisions so the active agent need not rediscover the whole instruction package.
