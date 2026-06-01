---
description: "Sentry's Agent Skills marketplace: a file-backed skill library with provenance contracts, progressive disclosure, validators, and meta-skills for writing and scanning skills"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# getsentry/skills

> Replaced 2026-06-01. See [getsentry-skills](./getsentry-skills.md) for the current review.

`getsentry/skills` is Sentry's repository of employee-facing Agent Skills and Claude Code plugin metadata. It is not a runtime memory database: its durable behavior-shaping state is a versioned file tree of `SKILL.md` instructions, `SPEC.md` maintenance contracts, routed references, scripts, plugin manifests, subagents, and Claude settings. The strongest mechanism is the `skill-writer` meta-skill, which turns source discovery, provenance capture, progressive disclosure, structural validation, and example-aware iteration into a repeatable skill-authoring workflow.

**Repository:** https://github.com/getsentry/skills

**Reviewed revision:** [58c611d2b05403f8e53c0b340bc9a574f8cdd4f0](https://github.com/getsentry/skills/commit/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0)

## Core Ideas

**Skills are behavior-shaping files, not memories in a service.** The repository exposes a root Claude plugin and marketplace manifest, with canonical skills under `skills/`, subagents under `agents/`, and a `.agents/skills` symlink for local agent tooling ([README](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/README.md), [plugin manifest](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/.claude-plugin/plugin.json), [marketplace manifest](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/.claude-plugin/marketplace.json)). The storage substrate is Git-backed Markdown plus small Python scripts and JSON settings. The representational form is mostly prose instructions with symbolic frontmatter, file layout conventions, allowlists, and script interfaces.

**The `SKILL.md` file is a router into progressive disclosure.** The `skill-writer` skill keeps its always-loaded file as a workflow index and sends agents to flat `references/*.md` leaves only when a branch needs them ([`skill-writer/SKILL.md`](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/SKILL.md), [reference architecture](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/references/reference-architecture.md)). That is a concrete progressive-disclosure pattern: high-level activation text and branch table first, deeper guidance only after a path decision.

**`SPEC.md` and `SOURCES.md` split maintenance intent from provenance.** New and materially changed skills are expected to carry a root-level `SPEC.md`, while source inventories, decisions, coverage matrices, gaps, and changelogs live in `SOURCES.md` ([README](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/README.md), [`skill-writer/SPEC.md`](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/SPEC.md), [`skill-writer/SOURCES.md`](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/SOURCES.md)). This gives skills a lightweight lineage model: runtime instructions can stay compact, while the evidence and maintenance rationale remain inspectable.

**Validation is structural and deliberately narrow.** `skill-writer` ends in registration plus lightweight validation, and its `quick_validate.py` checks frontmatter, required fields, directory-name consistency, referenced bundled files, and a size warning ([registration validation](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/references/registration-validation.md), [`quick_validate.py`](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/scripts/quick_validate.py)). The validator is a symbolic system-definition artifact: it enforces format and reference integrity, while semantic quality remains a review judgment.

**Security scanning is a separate behavior-changing workflow.** `skill-scanner` combines a static analyzer with agent review phases for frontmatter, prompt injection, bundled scripts, supply chain, permissions, symlinks, hooks, and suspicious hidden content ([`skill-scanner/SKILL.md`](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-scanner/SKILL.md), [`scan_skill.py`](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-scanner/scripts/scan_skill.py)). This is the repository's strongest example of combining deterministic checks with agent judgment: script findings are leads, not final truth.

**Iteration is specified more than evidenced.** `skill-writer` has an iteration path for positive examples, negative examples, review feedback, validation results, and observed agent behavior, including a proposed `references/evidence/` layout with working and holdout sets ([iteration path](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/references/iteration-path.md), [iteration evidence](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/skill-writer/references/iteration-evidence.md)). At this commit, the checkout does not contain those durable evidence files, and examples such as `prompt-optimizer`'s transformed prompts are illustrative reference material rather than trace-derived retained learning ([transformed examples](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/skills/prompt-optimizer/references/transformed-examples.md)).

## Comparison with Our System

| Dimension | getsentry/skills | Commonplace |
|---|---|---|
| Primary retained artifact | Agent skill directories with `SKILL.md`, `SPEC.md`, `SOURCES.md`, references, and scripts | Typed notes, reviews, instructions, references, ADRs, indexes, and workshop artifacts |
| Storage substrate | Git-backed Markdown, JSON settings, symlinks, bundled scripts | Git-backed Markdown plus schemas, validators, generated indexes, reports, and source snapshots |
| Representational form | Prose instructions with symbolic frontmatter, settings allowlists, script contracts | Prose plus symbolic frontmatter, links, schemas, type specs, scripts, and generated views |
| Behavioral authority | Skills instruct agents; settings allow skills and commands; scripts validate, scan, fetch, monitor, or categorize | Notes advise, instructions direct, types validate, skills route, indexes rank/navigate, review gates evaluate |
| Lineage | `SOURCES.md`, `SPEC.md`, changelogs, source inventories, Git history | Frontmatter, source snapshots, links, reviews, generated indexes, validation output, Git history |
| Activation | Agent skill discovery by description, explicit `/skill`, plugin install, Claude settings allowlist | Agent navigation through indexes, `rg`, links, skills, type contracts, and validation commands |
| Evaluation | Lightweight structural validation, manual local invocation, scanner findings, prompt eval guidance | Deterministic validation, semantic review bundles, link integrity, generated indexes, note review state |

The closest alignment is that both systems treat retained files as operational context, not passive documentation. A Sentry `SKILL.md` changes a future agent run because it is loaded as instruction. A commonplace instruction or type spec changes behavior through the same general authority family, even though commonplace names the artifact type more explicitly.

The major divergence is scope. `getsentry/skills` is a deployable skill marketplace optimized for Sentry workflows. It uses progressive disclosure inside each skill but does not try to build a cross-skill knowledge graph. Commonplace is a knowledge base first: it spends more machinery on typed links, navigation, review state, and generated indexes, and less on plugin packaging.

`getsentry/skills` is stronger on the practical skill-authoring loop. `skill-writer` has a concrete meta-workflow for selecting execution shape, splitting references, recording provenance, validating structure, and registering new skills. Commonplace has richer KB semantics, but its skill-writing guidance is distributed across the local instruction ecosystem rather than demonstrated by a public marketplace with many examples.

Commonplace is stronger on lifecycle visibility across artifacts. Sentry skills have good local contracts in `SPEC.md` and `SOURCES.md`, but there is no collection-level index of relationships, source snapshots, validation history, or retired/superseded authority surfaces beyond Git and changelog prose. That is acceptable for a plugin repo; it is weaker for an agent memory system where future agents need to compare and retire behavior-shaping artifacts systematically.

**Read-back:** push — skill/plugin activation loads selected `SKILL.md` instructions into agent context without agent lookup.

## Borrowable Ideas

**Make runtime files routers by default.** Ready to borrow. The `skill-writer` structure is a good default for complex commonplace skills: `SKILL.md` should name the branch table and output contract, while references answer specific lookup needs.

**Pair every material skill with `SPEC.md` and `SOURCES.md`.** Ready to borrow selectively. Commonplace already has type specs and source snapshots, but skills would benefit from a local maintenance contract plus source/decision log, especially when they encode procedures that may drift.

**Keep validation structural unless semantic validation is real.** Ready to borrow. `quick_validate.py` avoids pretending it can judge skill quality. Commonplace validators should preserve this boundary: enforce parseable contracts mechanically, then route semantic concerns to review.

**Treat scanner scripts as evidence producers, not authorities.** Ready to borrow. `skill-scanner` correctly makes the script produce findings and leaves intent classification to the reviewing agent. That split maps well to commonplace review bundles.

**Store positive and negative examples outside runtime instructions.** Good pattern, not yet demonstrated here. The proposed `references/evidence/` layout is the right shape for example-driven skill improvement because it keeps raw cases from bloating the active prompt. Commonplace should borrow it when it has real repeated examples, not as ceremony for every skill.

**Use settings allowlists as an activation surface.** Needs caution. `.claude/settings.json` explicitly allows plugin skills, read-only shell commands, `gh` queries, and trusted WebFetch domains ([settings](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/.claude/settings.json)). This is useful as an inspectable activation map, but commonplace should avoid turning large allowlists into hidden behavioral policy.

## Curiosity Pass

**The repository is more context-engineering substrate than memory system.** It improves future agent behavior by packaging instructions and tools, but it does not store observations from prior runs as first-class memories. Its memory-like value is in durable system-definition artifacts.

**Trace-derived status is not supported at this commit.** The docs describe iteration from examples, feedback, validation results, and observed behavior, but the checkout does not show actual traces, conversation logs, or labeled outcome corpora being converted into retained skills. The durable artifacts are source-backed and manually authored, not trace-distilled.

**The `README.md` mentions an `EVAL.md` that is absent in the checkout.** The root README points readers to `skills/skill-writer/EVAL.md`, but `rg --files` did not show that file at the reviewed commit ([README](https://github.com/getsentry/skills/blob/58c611d2b05403f8e53c0b340bc9a574f8cdd4f0/README.md)). That looks like a small documentation drift around evaluation, not a core architecture problem.

**The strongest governance surface is local, not global.** `SPEC.md` and `SOURCES.md` make individual skills reviewable. There is less support for asking cross-cutting questions such as "which skills depend on Claude-specific hooks?" or "which skills have stale source inventories?" without scanning files.

**Bundled scripts create a useful authority gradient.** A pure prose skill advises or instructs. A skill with a validator, scanner, PR monitor, or GitHub fetch script can also produce structured evidence that later agent steps consume. That gradient is visible in `skill-writer`, `skill-scanner`, and `iterate-pr`.

## What to Watch

- Whether the proposed `references/evidence/` working and holdout sets start appearing in real skills after repeated failures.
- Whether `skill-writer/EVAL.md` is added, removed from README, or replaced by another evaluation surface.
- Whether plugin manifests gain richer metadata for skills, references, and subagents, making the repository more queryable without opening every `SKILL.md`.
- Whether security scanning becomes a CI or marketplace gate instead of an invoked skill workflow.
- Whether Sentry adds a collection-level index of skill provenance, ownership, validation status, or supersession.
- Whether example-driven prompt optimization produces retained eval cases with source provenance rather than illustrative examples only.

---

Relevant Notes:

- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Sentry skills, settings allowlists, validators, scanners, and bundled scripts are consumed with instruction, configuration, validation, or evidence-production authority
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: `SOURCES.md`, reference docs, and scanner outputs advise or evidence later work until promoted into stronger instructions or checks
- [lineage](../../notes/definitions/lineage.md) - compares-with: `SOURCES.md` and `SPEC.md` are lightweight lineage and maintenance contracts for skills
- [distillation](../../notes/definitions/distillation.md) - contrasts: this repo performs source-backed compression into skills, but does not show trace-derived distillation from run logs at the reviewed commit
- [Designing agent memory systems](../../notes/designing-agent-memory-systems.md) - exemplifies: the important retained state is what changes a future agent action, not whether the repository calls it memory
- [files-not-database](../../notes/files-not-database.md) - aligns: the system gets operational leverage from inspectable files before introducing a service substrate
- [agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) - aligns: progressive disclosure works because the agent chooses which routed reference to open
