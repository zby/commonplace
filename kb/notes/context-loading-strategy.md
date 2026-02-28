---
description: CLAUDE.md should be a slim router to task-specific docs, not a comprehensive manual — because it's loaded every session
type: note
traits: []
areas: [claw-design]
status: current
---

# CLAUDE.md is a router, not a manual

CLAUDE.md is loaded into context every session. This makes it expensive — every line competes for attention with the actual task. It should contain:

- **Universal instructions** that apply to every session (coding conventions, git rules, guardrails)
- **Routing table** so the agent knows where things go and where to look
- **Search patterns** for the KB (always useful)
- **Links to task-specific docs** that get loaded on demand

It should NOT contain detailed instructions for specific tasks (how to write notes, template catalogs, link conventions). Those belong in targeted files that are read when needed — e.g. `project_claw/WRITING.md` for note creation.

## The loading hierarchy

1. **CLAUDE.md** — always loaded. Slim. Routes to everything else.
2. **Skill descriptions** — always loaded as a list of available `/slash` commands with short descriptions. This is a second always-loaded surface, similar to CLAUDE.md but with different affordances (see below).
3. **Skill bodies** — loaded on demand when a `/slash` command is invoked. Each skill pulls in its own detailed instructions. Good container for task-specific guidance that doesn't belong in CLAUDE.md.
4. **Task-specific docs** (WRITING.md, tasks/README.md) — read explicitly when the agent is about to do that kind of work. Referenced from CLAUDE.md so the agent knows they exist.

The principle: **match instruction specificity to loading frequency.** Universal rules load always. Task-specific rules load when doing that task.

## CLAUDE.md vs skill descriptions

Both are always loaded, but they work differently:

**CLAUDE.md** is imperative — "do this, don't do that." The agent follows these instructions whether or not it's aware of them as separate rules. Good for universal constraints (git conventions, guardrails) and routing ("when you need X, look here").

**Skill descriptions** are suggestive — "this capability exists if you need it." The agent sees a menu of available commands and decides whether to invoke one. The description needs to be good enough that the agent recognizes when a skill is relevant, but the detailed instructions only load when invoked. Good for task-specific workflows that the agent should know about but not always execute.

The overlap is intentional but serves different purposes. CLAUDE.md says "before creating notes, read WRITING.md" (imperative routing). A skill description says "/connect — find connections between notes" (available capability). Both point toward the same kind of work but through different mechanisms — one pushes, the other pulls.

**Key design question:** When should guidance live in CLAUDE.md vs in a skill description? If the agent must always follow it, CLAUDE.md. If the agent should know it's available and choose when to use it, skill description + skill body.

Topics:
- [claw-design](./claw-design.md)
