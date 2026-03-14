---
description: Reusable distilled procedures that live in kb/instructions/ — same format as skills but without activation triggers or CLAUDE.md routing entries; invoked when a human points the agent at them
type: note
traits: []
tags: []
status: seedling
---

# Instructions are skills without automatic routing

Instructions are not notes. Notes are for reasoning — an agent or human building understanding. Instructions are for execution — an agent that needs to act, not deliberate. They're a different kind of artifact, the way source files and task files are different, and they get their own directory (`kb/instructions/`) for the same reason sources and tasks do. The directory is the type signal.

Skills have two aspects: the procedure itself (distilled from methodology, execution-optimized) and the routing machinery that makes them discoverable (descriptions in the control-plane file, symlinks into the runtime's skill directory such as `.claude/skills/`, `.agents/skills/`, or optionally `$CODEX_HOME/skills`, slash-command triggers where supported). Not every distilled procedure needs automatic routing. Some procedures are used occasionally, invoked by a human saying "follow the procedure in X." These are instructions — same distillation quality as skills, but without the activation trigger plumbing.

Instructions include a description in frontmatter, same as skills. This helps a human scanning the directory decide which instruction to invoke, and makes promotion to a full skill frictionless — move it into a dedicated skill subdirectory, add the symlink, and add the routing table entry.

## Optimized for execution, not understanding

Instructions are written for a different reader than notes. The agent reading an instruction needs to act, not reason. This means:

- **Imperative voice** — "do X", not "X is important because..."
- **Step-sequenced** — order matters, each step builds on the previous
- **Behaviourally complete** — every branch the agent might encounter must be handled; it can't fill gaps from understanding it doesn't have
- **Minimal reasoning** — just enough to handle edge cases, not enough to justify the procedure
- **Explicit scope boundaries** — the instruction must say when it doesn't apply, because the agent won't sense this on its own
- **Frontloaded** — self-contained enough for an agent with no prior context. Terms must be defined inline, not by reference to other documents. An instruction may be handed to a sub-agent that has nothing else in its context window.

These constraints are why instructions don't belong in `kb/notes/`. An agent searching notes for understanding shouldn't wade through execution procedures. An agent executing a procedure shouldn't load discursive reasoning it doesn't need. Mixing them muddies the signal — the directory tells the agent what kind of reading the document demands.

## How instructions differ from adjacent concepts

**Ad hoc instructions notes** ([ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md)) are one-off — written for a specific situation, not expected to be reused. Instructions in `kb/instructions/` are reusable procedures distilled from repeated manual operations.

**Skills** are instructions plus routing. The procedure is the same; the difference is discoverability. A skill is found through the routing table; an instruction is found through a human pointing the agent at it, or through a note that describes and links to it.

**Methodology notes** are the source material instructions are distilled from. They carry reasoning, context, justification. Instructions carry procedure. The relationship is the same [source vs. compiled](./agent-statelessness-makes-routing-architectural-not-learned.md) split that holds between methodology and skills.

## How instructions get created

The methodology is distillation from repeated manual operations:

1. Do the task manually several times in different contexts
2. Notice the stable core — steps that recur vs. parts that vary
3. Extract the procedure, parameterize the variable parts, drop the reasoning (but keep it accessible in methodology notes)

This is the same process that produces skills. The difference is a judgment call about whether the procedure is common enough to warrant automatic routing. Instructions that prove themselves through repeated use get promoted to skills by adding the trigger machinery. Skills that turn out to be too niche can be demoted to instructions rather than deleted.

## Platform independence

In Claude Code, skills are discovered from `.claude/skills/`; in Codex, they can be discovered from project-local `.agents/skills/`, with `$CODEX_HOME/skills` (default `~/.codex/skills`) as an optional global install location. Instructions are independent of this mechanism — they work with any agent that can read a file and follow it. This keeps the knowledge base portable across agent platforms rather than coupled to one tool's skill discovery system.

---

Relevant Notes:

- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — foundation: the distillation process that produces both skills and instructions
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — context: instructions sit on the constraining gradient between ad-hoc instructions notes and skills
- [ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — distinguishes: ad hoc notes are one-off; instructions are reusable distilled procedures
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — motivates: the source/compiled split applies to instructions the same way it applies to skills
- [instructions are typed callables](./instructions-are-typed-callables.md) — extends: instructions, like skills, have implicit type signatures — they accept and produce document types
