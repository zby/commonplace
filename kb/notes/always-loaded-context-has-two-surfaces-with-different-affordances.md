---
description: CLAUDE.md enforces universal constraints (imperative/push); skill descriptions advertise opt-in capabilities (suggestive/pull) — guidance belongs on whichever surface matches its enforcement model
type: note
traits: []
tags: []
status: current
---

# Always-loaded context has two surfaces with different affordances

Both CLAUDE.md and skill descriptions are always loaded, but they work differently:

**CLAUDE.md** is imperative — "do this, don't do that." The agent follows these instructions whether or not it's aware of them as separate rules. Good for universal constraints (git conventions, guardrails) and routing ("when you need X, look here").

**Skill descriptions** are suggestive — "this capability exists if you need it." The agent sees a menu of available commands and decides whether to invoke one. The description needs to be good enough that the agent recognizes when a skill is relevant, but the detailed instructions only load when invoked. Good for task-specific workflows that the agent should know about but not always execute.

The overlap is intentional but serves different purposes. CLAUDE.md says "before creating notes, read WRITING.md" (imperative routing). A skill description says "/connect — find connections between notes" (available capability). Both point toward the same kind of work but through different mechanisms — one pushes, the other pulls.

**Key design question:** When should guidance live in CLAUDE.md vs in a skill description? If the agent must always follow it, CLAUDE.md. If the agent should know it's available and choose when to use it, skill description + skill body.

---

Relevant Notes:

- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — foundation: the loading hierarchy that establishes why always-loaded context must be slim; this note distinguishes the two always-loaded surfaces within that hierarchy
