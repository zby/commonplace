---
description: Create a new instruction in kb/instructions/ by distilling repeated manual operations into a reusable, execution-optimized procedure.
---

# Write an Instruction

An instruction is a reusable procedure that lives in `kb/instructions/`. It has the same format as a skill but is invoked manually rather than through automatic routing.

Instructions are created through **distillation** — extracting a stable procedure from repeated manual operations. You do a task by hand several times, notice which steps recur and which vary, then write down the recurring steps as a procedure. The variable parts become parameters or decision points. The reasoning that produced the steps stays in methodology notes, not in the instruction.

Instructions must be **frontloaded** — self-contained enough for an agent with no prior context. Define terms inline. Don't assume the reader has loaded other KB documents. An instruction may be handed to a sub-agent that has nothing else in its context window.

## Prerequisites

You should have performed the task manually at least twice in different contexts. If you haven't, do it manually first — you can't distill what you haven't done.

## Steps

1. **Identify the stable core.** Review what you did across instances. Which steps recurred? Which parts varied by context? The recurring steps are the procedure. The varying parts become parameters or decision points.

2. **Draft the procedure.** Write it as a sequence of imperative steps. Use "do X" not "X is important because." Include:
   - What to check before starting (prerequisites)
   - The steps in execution order
   - Decision points where context determines the path
   - What to verify when done
   - What NOT to do (critical constraints)

3. **Add frontmatter.** Every instruction needs:
   ```yaml
   ---
   description: One line — what this instruction does, when to use it.
   ---
   ```
   The description helps a human scanning the directory decide whether this instruction fits their situation. It also makes promotion to a skill frictionless.

4. **Cut the reasoning.** Remove explanations of *why* each step exists. If the reasoning is worth preserving, it belongs in a methodology note that links to this instruction — not in the instruction itself. Keep only enough reasoning for the agent to handle edge cases and decision points.

5. **Test the boundaries.** Add explicit scope boundaries — when does this instruction NOT apply? The agent won't sense this on its own. If the task falls outside scope, say what to do instead.

6. **Write a companion note** (optional but recommended). A note in `kb/notes/` that describes the instruction, explains its rationale, links to the methodology it was distilled from, and links to the instruction file. This is what makes the instruction findable through normal KB search.

## Verify

- The instruction reads as a sequence of actions, not an essay
- An agent reading it cold could execute it without asking clarifying questions
- Reasoning is minimal — just enough for edge cases
- Scope boundaries are explicit
- Frontmatter has a description

## Promotion to skill

If the instruction proves useful enough to warrant automatic routing: copy it to `skills/<name>/SKILL.md`, add the skill frontmatter fields (`name`, `allowed-tools`, `context`, `model`), symlink into `.claude/skills/`, and add a routing table entry in CLAUDE.md.
