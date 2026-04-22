# PROPOSED: Writing conventions for kb/instructions/ (prescriptive register)

> Workshop draft. Delta from current `kb/instructions/COLLECTION.md`:
> - Outbound linking section reorganised **per destination collection** rather than by register. Each destination block declares when the connect skill should search it and which labels writers may use.
> - Outbound linking is explicitly **exceptional** — instructions frontload. Links are permitted only for context-transfer (sub-agent invocation), conditional deviations (errors, branches), and meta-reader needs (rationale with audience disclaimer).
> - `defined-in` dropped from outbound — terms needed for execution must be frontloaded, not linked.
> - `see-also` dropped from → `kb/notes/`, → `kb/reference/`, and → `kb/agent-memory-systems/` — weak links to other collections don't earn their keep against the frontloading principle.
> - `→ kb/agent-memory-systems/` block removed entirely (not an active link path from instructions).
> - Intra-prescriptive labels: `composition`, `precondition`, `invokes`, `applies-when`, `see-also` (last scoped to error/fallback paths). `invokes` guidance notes the sub-agent preference.
> - Cross-collection labels selected from the shared catalogue in [`link-vocabulary.md`](./link-vocabulary.md). This `COLLECTION.md` is authoritative for writers; `link-vocabulary.md` is a resource for `COLLECTION.md` authors.
> - `reference` label (prescriptive → descriptive) renamed to `operates-on`. `justification` merged into `rationale` per [`label-audit.md`](./label-audit.md).
> - All other sections unchanged.

## Register

This collection operates in the **prescriptive [register](../../notes/definitions/register.md)** (one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules). Documents here direct what to do — procedures, conventions, skill bodies, and operational rules. They optimize for an agent (or human) executing them on first reading, without prior context.

The quality goal is **executability + precision**: every step must be actionable, every decision point must be explicit, and ambiguity must be eliminated. A vague prescription wastes the reader's bounded context on interpretation rather than action.

## The instruction duality

Instructions in an agent-operated KB are both prescriptive content and part of the working system. Changing an instruction changes agent behavior immediately. Treat edits to instructions as deployments, not just documentation updates.

## Title conventions

**Imperative or action-oriented titles.** Name the document after what it directs: "Write an instruction", "Review triage", "Fix warnings". The title should answer "what does this tell me to do?"

For skill subdirectories, the skill name is the title: `write/SKILL.md`, `connect/SKILL.md`.

## Description conventions

For instructions, descriptions should name the trigger condition — when to use this procedure.

## Precision as quality discipline

Prescriptions fail when they leave room for interpretation. Quick tests:
- Could an agent with no prior context execute each step without asking a clarifying question?
- Are decision points explicit — "if X, do A; otherwise do B" — rather than implied?
- Are scope boundaries stated — when does this procedure NOT apply, and what to do instead?
- Is reasoning minimal — just enough for edge cases, with the "why" living in theory notes?

**Frontloading.** Instructions must be self-contained enough for an agent with no prior context. Define terms inline. Don't assume the reader has loaded other KB documents.

## Outbound linking conventions

**Instructions frontload.** A procedure must be executable from its own text; an executing agent should not be expected to follow outbound links to complete the task. Outbound links in instructions are therefore **exceptional** — limited to cases where linking is the right mechanism:

- **Context-transfer** — sub-agent invocations. The link is the bootstrap for a new, clean context, not a required read in the current one.
- **Conditional deviations** — error procedures, conditional branches to specialised procedures, and any path the reader follows only if a specific trigger applies. Frontloading every possible deviation would bloat the main path.
- **Meta-reader needs** — `rationale` links serve reviewers and developers updating the procedure, not executing agents. These are kept with an explicit audience disclaimer; execution must work without following them.

Outbound rules are organised per destination collection.

### → `kb/instructions/` (within this collection)

**Search:** procedure composition. The current procedure chains to, requires, branches to, or invokes another procedure. Intra-collection links are operational edges — the reader follows only when the composition dictates.

**Labels:**

| label | reader-need / when to use |
|---|---|
| `composition` | sequential: complete this procedure, then follow target. Reader drops current context when moving on. |
| `precondition` | conditional: reader verifies target is done/true before starting — skip if already satisfied |
| `invokes` | subroutine call. **Prefer sub-agent invocation** so context resets; use same-context invocation only for small, heavily-reused procedures |
| `applies-when` | conditional branch; reader follows only if the trigger applies |
| `see-also` | reserved for error procedures and conditional fallbacks the reader may need only on deviation |

Keep chains shallow. Deep composition defeats frontloading — a procedure that requires chasing five other procedures to execute isn't a procedure, it's a reading list.

### → `kb/notes/`

**Audience: meta-readers.** These links serve reviewers and developers updating the procedure, not executing agents. Any definition or reasoning the execution path depends on must be frontloaded into the instruction body, not deferred to a linked note. An agent executing the instruction is not expected to follow these links.

**Search:** when a rule in this procedure exists because of a theoretical claim — worth recording so a future reviewer can locate the rationale.

**Labels:**

| label | reader-need |
|---|---|
| `rationale` | (meta-reader) wants the theoretical claim this rule rests on |

### → `kb/reference/`

**Audience: mixed.** `operates-on` identifies the system component the procedure acts on. For execution, the instruction must frontload enough to operate; the link is for readers (meta or execution) who need depth beyond what can be frontloaded.

**Search:** when the procedure's scope is defined by a specific system component and naming it precisely matters.

**Labels:**

| label | reader-need |
|---|---|
| `operates-on` | wants to know what system component the procedure acts on |

(No `→ kb/agent-memory-systems/` destination — instructions do not have an active link path to external system reviews. If a specific instruction develops a legitimate need, add the destination then.)

**Reasoning constraint.** Cut explanations of *why* each step exists from the instruction body. If the reasoning is worth preserving, record it in a theory note and link via `rationale` for meta-readers — never inline it for the execution reader. Keep only enough reasoning for the agent to handle edge cases and decision points.

## Frontmatter

Instructions use minimal frontmatter. Plain instructions need `description` and `type: kb/types/instruction.md`. Promoted skills add skill-specific fields (`name`, `allowed-tools`, `context`, `model`) in their `SKILL.md`.

## Promoted skills

Some instruction subdirectories are promoted into runtime skill surfaces (`.claude/skills/`, `.agents/skills/`) by `commonplace-init`. Promoted skills:

- Must not rely on their on-disk location being `kb/instructions/<name>/`
- Should use stable workspace-root paths (`kb/notes/`, `kb/instructions/COLLECTION.md`)
- Treat `kb/instructions/` as the searchable source surface and runtime skill directories as compiled copies

## Default template

```markdown
---
description: ""
type: kb/types/instruction.md
---

# {Imperative title}

{Opening: what this procedure does and when to use it.}

## Prerequisites

- {What must be true before starting}

## Steps

1. {Step}
2. {Step}

## Verify

- {How to confirm the procedure succeeded}
```

## Types

- `instruction` -> `kb/types/instruction.md`
  Use for procedures, skills, wrapper prompts, and review gates.
- `index` -> `kb/types/index.md`
  Use for generated directory indexes and instruction navigation hubs.

## What does NOT belong here

- Transferable claims about KB methodology → theoretical register (`kb/notes/`)
- Descriptions of how the system works → descriptive register (`kb/reference/`)
- Generated reports and reviews → `kb/reports/`
- Work in progress → `kb/work/` (workshops)
