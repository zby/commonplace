---
description: The loading hierarchy (CLAUDE.md → skill descriptions → skill bodies → task docs) should match instruction specificity to loading frequency — always-loaded context competes for attention every session
type: note
traits: [has-external-sources]
areas: [kb-design]
status: current
---

# Instruction specificity should match loading frequency

Every line in always-loaded context competes for attention with the actual task. The design response is progressive disclosure: match how specific an instruction is to how often it needs to be present.

## The loading hierarchy

1. **CLAUDE.md** — always loaded. Slim. Routes to everything else. Contains universal instructions (coding conventions, git rules, guardrails), routing tables, search patterns, and links to task-specific docs.
2. **Skill descriptions** — always loaded as a list of available `/slash` commands with short descriptions. A second always-loaded surface with [different affordances](./always-loaded-context-has-two-surfaces-with-different-affordances.md).
3. **Skill bodies** — loaded on demand when a `/slash` command is invoked. Each skill pulls in its own detailed instructions. Good container for task-specific guidance that doesn't belong in CLAUDE.md.
4. **Task-specific docs** (WRITING.md, tasks/README.md) — read explicitly when the agent is about to do that kind of work. Referenced from CLAUDE.md so the agent knows they exist.

The principle: **match instruction specificity to loading frequency.** Universal rules load always. Task-specific rules load when doing that task.

CLAUDE.md should NOT contain detailed instructions for specific tasks (how to write notes, template catalogs, link conventions). Those belong in targeted files that are read when needed — e.g. `kb/instructions/WRITING.md` for note creation.

---

Sources:

- Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — describes Claude Code following this exact pattern: a CLAUDE.md file as a slim router with grep/glob for just-in-time retrieval of everything else.

Relevant Notes:

- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: 100-line AGENTS.md as "a map with pointers" converges independently on the routing concept at production scale
- [Always-loaded context has two surfaces with different affordances](./always-loaded-context-has-two-surfaces-with-different-affordances.md) — extends: distinguishes the two always-loaded surfaces (CLAUDE.md vs skill descriptions) and their design tradeoffs

Topics:

- [kb-design](./kb-design.md)
