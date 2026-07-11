---
description: "getsentry/skills review: Sentry's repo-backed skill and subagent marketplace with authored prompts, routed references, scripts, and validation rules"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# getsentry/skills

`getsentry/skills`, by Sentry, is a Claude Code / Agent Skills marketplace for Sentry employee workflows: code review, PR writing, skill authoring, issue triage, security review, presentation creation, SRED summaries, onboarding explanation, and similar repeated work. At the reviewed commit it is not a runtime memory database. Its durable behavior surface is a repository-backed corpus of authored `SKILL.md` files, optional `SPEC.md` maintenance contracts, routed references, helper scripts, subagent prompts, plugin manifests, and Claude permission settings.

**Repository:** https://github.com/getsentry/skills

**Reviewed commit:** [b10e2db21d3165de1904bdf3fa64285016765fe5](https://github.com/getsentry/skills/commit/b10e2db21d3165de1904bdf3fa64285016765fe5)

**Last checked:** 2026-06-04

## Core Ideas

**Skills package Sentry-specific operating knowledge as installable instructions.** The README describes the repository as "Agent skills for Sentry employees" and lists the available skills and subagents; the marketplace manifest exposes the repo-root plugin as `sentry-skills`, while `plugin.json` names it "Sentry-specific agent skills for code review, commits, and more" ([`README.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md), [`.claude-plugin/marketplace.json`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude-plugin/marketplace.json), [`.claude-plugin/plugin.json`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude-plugin/plugin.json)). The retained artifacts mostly change future agent behavior by telling the agent what to inspect, which tools to call, what to skip, and what output shape to use.

**Context efficiency comes from host routing plus progressive disclosure inside each skill.** The README says skills activate automatically when relevant, and complex skills keep `SKILL.md` as a router to conditional references: `skill-writer` lists dozens of flat `references/*.md` files with "Open when..." reasons, while `prompt-optimizer` loads different references for new prompts, existing prompts, model-family ports, and repeated failures ([`README.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md), [`skills/skill-writer/SKILL.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/SKILL.md), [`skills/prompt-optimizer/SKILL.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/prompt-optimizer/SKILL.md)). This bounds initial context to the selected skill body and makes deeper context explicit, but actual activation quality is delegated to the host's skill router.

**The corpus mixes prose instruction with symbolic control surfaces.** Each skill is Markdown with YAML frontmatter; some skills declare `allowed-tools`, bundled scripts, or MCP tools, and repository settings allow named skill invocations and specific shell / web operations ([`skills/triage-frontend-issues/SKILL.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/triage-frontend-issues/SKILL.md), [`skills/skill-scanner/SKILL.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-scanner/SKILL.md), [`.claude/settings.json`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude/settings.json)). The prose is the main instruction channel; symbolic metadata, settings, and scripts make parts of the corpus routable, checkable, or executable.

**Maintenance is authored, reviewed, and lightly validated rather than learned from traces.** `AGENTS.md`, `README.md`, and `CONTRIBUTING.md` require new skills to live under `skills/<skill-name>/`, include `SKILL.md` and usually `SPEC.md`, update the README table, add Claude settings entries, and test by local plugin installation ([`AGENTS.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/AGENTS.md), [`README.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md), [`CONTRIBUTING.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/CONTRIBUTING.md)). `skill-writer` has a structural validator for skill frontmatter and local file references, but I found no code that derives durable skill updates from agent session logs, tool traces, or repeated trajectories ([`skills/skill-writer/scripts/quick_validate.py`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/scripts/quick_validate.py)).

**Adoption affordances are strong for coding agents already living in GitHub, Claude Code, and Sentry tooling.** The repo installs through Claude plugin marketplace commands or `npx skills add`, vendors copied skills for reliability, exposes `.agents/skills` as a local mirror, and includes helper scripts around `gh`, Sentry MCP, and repository-local workflows ([`README.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md), [`AGENTS.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/AGENTS.md), [`skills/gh-review-requests/scripts/fetch_review_requests.py`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/gh-review-requests/scripts/fetch_review_requests.py)). The tradeoff is that correctness mostly relies on source inspection, user confirmation, local tests, and human judgment rather than a central memory governance layer.

## Artifact analysis

- **Storage substrate:** `repo` - The central retained artifacts are versioned repository contents: `skills/*/SKILL.md`, optional `SPEC.md`, `SOURCES.md`, routed references, scripts, `agents/*.md`, `.claude-plugin/*.json`, `.claude/settings.json`, and repo instructions ([`README.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md), [`AGENTS.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/AGENTS.md)).
- **Representational form:** `prose` `symbolic` - Skill bodies, subagent prompts, specifications, source inventories, references, and templates are prose; YAML frontmatter, plugin manifests, Claude settings, Python helper scripts, Warden config, and workflow files are symbolic artifacts consumed by hosts, scripts, or CI ([`.claude/settings.json`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude/settings.json), [`warden.toml`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/warden.toml), [`skills/skill-writer/scripts/quick_validate.py`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/scripts/quick_validate.py)).
- **Lineage:** `authored` `imported` - Most artifacts are authored Sentry workflow guidance; some skills and agents are explicitly vendored or source-backed, with README attribution rules and `SOURCES.md` files preserving imported sources and decisions ([`README.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/README.md), [`skills/skill-writer/SOURCES.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-writer/SOURCES.md), [`agents/code-simplifier.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/agents/code-simplifier.md)).
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` - Skills and subagents instruct agents when loaded; descriptions and plugin metadata route selection; `SPEC.md` and `SOURCES.md` preserve knowledge for maintainers; validators and scanners check structure or security; some skills enforce operational constraints such as "archive only" and confirmation before mutation ([`skills/triage-frontend-issues/SKILL.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/triage-frontend-issues/SKILL.md), [`skills/skill-scanner/SKILL.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/skill-scanner/SKILL.md), [`skills/agents-md/SPEC.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/skills/agents-md/SPEC.md)).

**Skill packages.** A typical skill is `skills/<name>/SKILL.md`, sometimes with `SPEC.md`, `SOURCES.md`, `references/`, `scripts/`, or static assets. The operative part is the prose procedure plus frontmatter trigger text; script-backed skills add executable symbolic helpers. The skill's authority is instruction when loaded, routing through its description, knowledge through examples and sources, and sometimes validation or enforcement through scripts and hard rules.

**Subagent prompts.** `agents/senpai.md` and `agents/code-simplifier.md` are durable persona / task prompts, not ordinary skills. They include frontmatter metadata, model/tool declarations, examples, and long-form operating instructions; when a host delegates to them, they become stronger instruction artifacts than a reference note ([`agents/senpai.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/agents/senpai.md), [`agents/code-simplifier.md`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/agents/code-simplifier.md)).

**Plugin and permission metadata.** `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, and `.claude/settings.json` are symbolic surfaces that package the corpus and authorize its expected tool/skill usage. They do not contain task knowledge themselves, but they govern what can be installed and what operations the local Claude environment may allow ([`.claude-plugin/marketplace.json`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude-plugin/marketplace.json), [`.claude/settings.json`](https://github.com/getsentry/skills/blob/b10e2db21d3165de1904bdf3fa64285016765fe5/.claude/settings.json)).

**Promotion path.** The strongest path is authored: a maintainer creates or revises a skill, adds maintenance metadata, updates README and Claude settings, runs local validation or tests, then merges through the repo. `skill-writer` can guide this process and `quick_validate.py` can catch structural errors, but there is no implemented automatic path from usage traces to promoted skills.

## Comparison with Our System

getsentry/skills and Commonplace both use inspectable repository files as behavior-shaping memory. Both prefer exact paths, local scripts, and authored conventions over an opaque hosted memory service. The shared lesson is that an agent memory surface can be plain Markdown plus a small amount of symbolic metadata when the host already knows how to route and load it.

The main divergence is artifact typing. Commonplace separates notes, references, instructions, sources, reviews, types, indexes, and work artifacts, then validates those boundaries. getsentry/skills has a flatter package model: most durable behavior is a skill, a subagent prompt, or a support file below a skill. That is efficient for distribution but weaker for cross-artifact reasoning, provenance, and lifecycle management.

The Sentry repo is more operationally embedded than Commonplace's general KB methodology. Several skills directly mutate external systems or PR state through `gh` or MCP tools, with hard rules and confirmation gates. Commonplace's own instruction layer could borrow some of that concrete operational specificity, but it should keep stronger collection/type contracts for accumulated knowledge.

### Borrowable Ideas

**`SPEC.md` beside complex skills.** Commonplace skills could adopt a short maintenance contract next to high-risk or frequently changed skills, separate from runtime instructions. Ready now for promoted `cp-skill-*` workflows.

**Skill-root-relative script validation.** `quick_validate.py` checks frontmatter and referenced local files without trying to judge all semantic quality. Commonplace could add a similarly narrow validator for skill packages. Ready now because the behavior is deterministic and cheap.

**Repository permission allowlist as a reviewed artifact.** `.claude/settings.json` makes expected skill and shell permissions explicit. Commonplace could document or validate the minimum permissions its shipped skills require, but only after there is a stable consumer for that metadata.

**Confirmation-first mutation skills.** `triage-frontend-issues` shows a strong pattern for external mutations: build a plan, get explicit approval, mutate only the approved set, and report failures. Commonplace can reuse that shape for KB operations that touch remote systems or shared indexes.

**Do not borrow the flat skill corpus as the full KB shape.** For Commonplace, "everything is a skill" would erase important authority and lineage distinctions. The Sentry layout is a good distribution surface, not a replacement for typed knowledge artifacts.

## Write side

**Write agency:** `manual` - The skill corpus changes through authored repository edits by humans or agents acting under user/review control. Helper scripts fetch, classify, validate, or mutate external work systems, but I found no repository mechanism that automatically curates existing skills in place, consolidates stored memories, deduplicates them, decays them, or derives new durable skills from agent traces.

## Read-back

**Read-back:** `pull` - Accumulated repository knowledge such as `SPEC.md`, `SOURCES.md`, references, scripts, settings, and maintenance rules reaches future maintainers or agents by explicit file loading, search, validation, or running bundled scripts. Host skill activation can push static baseline skill prose into an agent session, but the reviewed repo does not implement a push path for memory accumulated from use.

The practical read-back path is still agent-shaped: skill descriptions route initial loading, `SKILL.md` files route deeper references, scripts return structured JSON, and subagent prompts give the host a specialized delegate. Effective faithfulness is not verified from code; the repository tests local behavior manually and structurally rather than with WITH/WITHOUT behavioral ablations.

## Curiosity Pass

**This is more a skill distribution system than a memory system.** It is included in the landscape because skills are durable behavior-shaping retained artifacts, but the repo does not accumulate user/session memory on its own.

**The most memory-like files are the maintenance contracts.** `SPEC.md` and `SOURCES.md` preserve why a skill exists, what evidence shaped it, and how it should change. They are more comparable to Commonplace notes than the runtime `SKILL.md` files.

**Some skills mutate external state without mutating the skill store.** `triage-frontend-issues`, `iterate-pr`, and `gh-review-requests` can read or change Sentry/GitHub workflows, but those operations are task execution, not curation of the repository's own retained memory.

**The validation layer is intentionally shallow.** `quick_validate.py` proves structure and reference existence, not skill usefulness. That keeps validation cheap and avoids false confidence about semantic behavior.

## What to Watch

- Whether usage evidence, PR outcomes, triage mistakes, or skill activation logs start being recorded in repo files; that would create an actual read/write memory loop instead of a static skill corpus.
- Whether `skill-writer` grows an automatic promotion path from `SOURCES.md`, examples, or review feedback into skill revisions; that would add automatic curation operations.
- Whether the Claude plugin marketplace manifest begins listing multiple domain plugins from this repo; that would make routing and permission boundaries more important than the current single root plugin.
- Whether `SPEC.md` becomes required for every material skill change and gets validated; that would strengthen lineage and maintenance authority.
- Whether mutation skills add post-action audits that verify the intended external state changed correctly; that would improve behavioral faithfulness without requiring a central memory backend.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - explains why installed static skill prose is not counted as accumulated memory read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - provides the storage, form, lineage, and authority vocabulary used to classify skills, subagents, manifests, and validators.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - applies to `SPEC.md`, `SOURCES.md`, examples, references, and maintenance notes when they advise later agents or maintainers.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - applies to skill instructions, plugin metadata, permission settings, validators, and hard-rule workflow skills.
- [Lineage](../../notes/definitions/lineage.md) - frames authored, vendored, source-backed, and validation-derived skill artifacts.
- [Context engineering](../../notes/definitions/context-engineering.md) - names the routing and progressive-disclosure problem solved by skill selection and conditional references.
