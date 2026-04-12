---
description: Claude Code continuity scaffold that persists session, task, decision, and comment state in markdown safeguard files and rebuilds context through prompt-defined recovery routines
type: agent-memory-system-review
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-10"
---

# Claude Context Guard

Claude Context Guard is a Claude Code project scaffold by atreiou that installs prompt assets rather than a standalone runtime: slash-command skills under [`.claude/skills/`](../../../related-systems/claude-context-guard/.claude/skills/start/SKILL.md), light shell hooks under [`.claude/hooks/`](../../../related-systems/claude-context-guard/.claude/hooks/pre-compact-save.sh), and template safeguard files under [`templates/`](../../../related-systems/claude-context-guard/templates/CLAUDE.md). The core idea is to survive rate limits, restarts, and compaction by forcing Claude to keep durable project state in files like `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, and `COMMENTS.md`, then maintain and rebuild context from those files with `/start`, `/save`, `/audit`, and `/end`. It is a real related system because the repo ships an inspectable continuity workflow, but most of the logic lives in prompt procedures rather than executable reconciliation code.

**Repository:** https://github.com/atreiou/claude-context-guard

## Core Ideas

**The memory substrate is explicit project files, not hidden session state.** The [README](../../../related-systems/claude-context-guard/README.md) and [templates](../../../related-systems/claude-context-guard/templates/CLAUDE.md) define a core safeguard set: `CLAUDE.md`, `SESSION_LOG.md`, `TASK_REGISTRY.md`, `DECISIONS.md`, `COMMENTS.md`, `FEATURE_LIST.json`, `plans/`, and on-demand audit history under `audits/`. This is not a database or retrieval service. It is a disciplined file schema for carrying project continuity across Claude Code sessions.

**Recovery is specified as procedural agent behavior, not as an executable reconciler.** The central mechanisms are written in the [`/start` skill](../../../related-systems/claude-context-guard/.claude/skills/start/SKILL.md), [`/audit` skill](../../../related-systems/claude-context-guard/.claude/skills/audit/SKILL.md), [`/save` skill](../../../related-systems/claude-context-guard/.claude/skills/save/SKILL.md), and [`/end` skill](../../../related-systems/claude-context-guard/.claude/skills/end/SKILL.md). Those documents tell Claude how to locate the project root, read safeguard files, cross-check plans against the task registry, detect orphaned work, and maintain session continuity. The repo does not implement those checks in a parser-backed program; it relies on the model following the procedure.

**Current versus archival context is separated to keep always-loaded state lean.** The [README](../../../related-systems/claude-context-guard/README.md) and [template `CLAUDE.md`](../../../related-systems/claude-context-guard/templates/CLAUDE.md) both define a pagination policy: main safeguard files keep recent or still-active content, while older material rotates into `*_page*.md` archives. The `/start` skill explicitly reads current files and only the last three archived plans, while archive pages are noted but not auto-loaded. That is a concrete progressive-disclosure policy for volatile workshop state.

**Continuity is produced by cross-referencing several traces, not by trusting one summary file.** The `/start` and `/audit` skills repeatedly compare `SESSION_LOG.md`, `TASK_REGISTRY.md`, `COMMENTS.md`, `DECISIONS.md`, `FEATURE_LIST.json`, archived plans, and git state. The important design move is not "write a session summary"; it is "treat disagreements between traces as integrity signals." Dropped tasks, unexplained tasks, unlogged sessions, and unpushed commits are all defined as mismatches between artifacts.

**Hooks provide light guardrails around the prompt-defined workflow.** [`settings.json`](../../../related-systems/claude-context-guard/.claude/settings.json) wires three hooks: slash-command detection, pre-commit reminders, and pre-compaction backups. The actual scripts are intentionally small. [`check-slash-commands.sh`](../../../related-systems/claude-context-guard/.claude/hooks/check-slash-commands.sh) warns when Claude should invoke a skill. [`pre-commit-check.sh`](../../../related-systems/claude-context-guard/.claude/hooks/pre-commit-check.sh) emits a checklist before `git commit`, but does not block. [`pre-compact-save.sh`](../../../related-systems/claude-context-guard/.claude/hooks/pre-compact-save.sh) copies safeguard files into timestamped backups. So the hard mechanism is file copying; the rest is reminder infrastructure.

**The Itemisation Protocol turns code into addressable sections through prompt instructions plus diff verification.** The [`/itemise` skill](../../../related-systems/claude-context-guard/.claude/skills/itemise/SKILL.md) is the repo's most distinctive feature beyond session logging. It instructs Claude to insert numbered comment markers, preserve every existing character with edit-only operations, and verify integrity by diffing against backups after stripping numbering comments. This is a real mechanism for making code addressable by section, but again it is prompt-mediated rather than implemented as a deterministic rewriter.

## Comparison with Our System

| Dimension | Claude Context Guard | Commonplace |
|---|---|---|
| Primary concern | Session continuity and anti-forgetting discipline inside one Claude Code project | Durable knowledge accumulation, navigation, and review across a knowledge base |
| Main substrate | Fixed safeguard files plus prompt skills and light hooks | Typed notes, indexes, instructions, skills, validators, and reviews |
| Strongest layer | Workshop-like temporal state: session logs, task registries, decisions, comments, plan archives | Library layer plus growing theory for a workshop layer |
| Recovery model | Re-read current files, cross-check them, inspect git state, reconstruct continuity | Navigate from control-plane guidance into notes, indexes, and instructions as needed |
| Governance | Mostly procedural and advisory; correctness depends on the agent following skill text | Deterministic validation plus semantic review plus human curation |
| Structure of durable knowledge | Flat operational files with fixed roles | Linked notes with explicit relationship semantics and richer type distinctions |

Claude Context Guard is strongest where commonplace is comparatively thin: it treats session continuity and workshop-state hygiene as the main problem. `TASK_REGISTRY.md`, `COMMENTS.md`, and `SESSION_LOG.md` are all first-class durable artifacts, with explicit rules for what gets logged and when. That is much more concrete than our current workshop-layer theory.

Commonplace is stronger where Claude Context Guard stays operational and local. We distinguish library artifacts from instructions, notes from indexes, and durable claims from temporary work. We also have stronger governance for correctness: deterministic validation and semantic review bundles, not just reminders and checklists. Claude Context Guard preserves continuity well enough to resume work; commonplace aims to preserve knowledge in forms that remain composable and inspectable beyond one project's session history.

The deepest difference is that Claude Context Guard is not trying to become a knowledge system in the library sense. It is a recovery scaffold for one working project. Its durable artifacts are there to stop loss of state, not to build a reusable graph of ideas. In commonplace terms, it is almost entirely workshop layer with a very thin library.

## Borrowable Ideas

**Keep volatile workshop state in lean current files plus explicit archive pages.** The archive policy in [`templates/CLAUDE.md`](../../../related-systems/claude-context-guard/templates/CLAUDE.md) is the strongest immediately borrowable idea here. In commonplace, this would look like workshop artifacts that keep only current work hot and rotate older completed material into clearly named archives. Ready to borrow when we formalize workshop artifacts beyond ad hoc directories.

**Cross-check multiple continuity traces instead of trusting one handoff note.** The repo's real insight is that session continuity becomes more robust when plans, task ledgers, comments, decisions, and git state can contradict each other. In commonplace, this would look like workshop subsystems that treat disagreements between traces as reviewable integrity failures rather than assuming the latest summary is true. Ready to borrow conceptually; needs a concrete workshop subsystem first.

**Add pre-compaction backups for volatile agent-maintained files.** [`pre-compact-save.sh`](../../../related-systems/claude-context-guard/.claude/hooks/pre-compact-save.sh) is tiny but useful. A similar hook in commonplace would protect workshop state or active review artifacts against context loss without requiring the whole system to become session-log centric. Ready to borrow now if we identify the right target files.

**Treat parent-directory project discovery as part of the continuity layer.** The `/start` skill's search for a valid `CLAUDE.md` below the current directory is a pragmatic answer to "agents are often launched from the wrong folder." In commonplace, the analogue would be better root discovery for KB-aware commands and workshop tooling. Needs a use case first.

**Make section-addressable code optional rather than universal.** The Itemisation Protocol is interesting because it is framed as a context-budget tool, not as code style. In commonplace, an optional numbered-section layer might help long instruction files or generated artifacts where targeted reads matter. Needs a use case first; it is too invasive to adopt speculatively.

## Curiosity Pass

**The repo's guarantees are mostly normative, not enforced.** The README language suggests a memory system with strong recovery properties, but the code-inspectable core is lighter: an installer, templates, hook wiring, and reminder/backup scripts. The hardest logic lives in skill prose. If Claude follows the instructions well, the system works. If Claude does not, there is little hard enforcement beyond file copies and the user's ability to run `/audit`.

**The most important mechanism is not storage but ritualized maintenance.** Nothing here is technically hard to store. The value comes from forcing repeated maintenance of `COMMENTS.md`, `TASK_REGISTRY.md`, `SESSION_LOG.md`, and `DECISIONS.md`, and from defining cross-check rituals around them. This makes the repo closer to an operational constitution with a fixed file schema than to a memory engine.

**"Persistent context protection" is accurate, but "memory system" overstates the implementation.** Claude Context Guard does not parse transcripts into typed memories, rank observations, or autonomously decide promotion targets. It relies on the active agent to keep symbolic artifacts current. That still matters, but it puts the system closer to prompt-mediated workshop bookkeeping than to learned memory.

**The archive policy is more substantial than the learning story.** The sharpest implemented design choice is the split between active files and archive pages, plus the rule that `/start` should not eagerly reload history. That is a concrete answer to context-budget pressure. By contrast, the stronger integrity claims about dropped tasks, unexplained tasks, and orphaned work remain mostly procedural expectations.

**The Itemisation Protocol may be the repo's most novel contribution.** The safeguard-file pattern has many cousins. The code-addressability layer is more unusual: it tries to make bounded file reads a first-class operating mode for Claude, and it includes an explicit integrity-check story. If anything here deserves deeper follow-up beyond workshop continuity, it is probably that protocol.

## What to Watch

- Whether the maintainer hardens `/start`, `/audit`, and pagination into executable tooling instead of leaving them as prompt-only procedures.
- Whether the archive rotation rules remain stable as projects get larger, especially around task and comment growth.
- Whether the orphaned-work and dropped-task checks gain stronger deterministic support than "Claude should notice this mismatch."
- Whether the Itemisation Protocol becomes a dedicated tool or stays a carefully constrained prompt procedure.
- Whether the system evolves from one-project continuity scaffolding toward reusable knowledge extraction from the accumulated safeguard files.

---

Relevant Notes:

- [Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — exemplifies: this repo deliberately uses all four always-loaded surfaces at once: system prompt file, skills, memory-like files, and hook configuration
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: Claude Context Guard is almost entirely a workshop-layer system built around temporal state and handoff continuity
- [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — converges: current safeguard files stay hot, archive pages stay cold unless recovery or audit actually needs them
- [Files not database](../../notes/files-not-database.md) — exemplifies: project continuity is stored in inspectable files rather than in a service-owned memory backend
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: this repo is a weak but real live-session artifact case, mining agent and user interaction traces into durable project files rather than into ranked memories or weights
- [Context Constitution](./context-constitution.md) — contrasts: both are instruction-defined control layers, but Claude Context Guard is narrower, more procedural, and more tightly coupled to one project's file rituals
- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — converges: much of the system's real behavior is packaged as skill text rather than as a standalone executable subsystem
