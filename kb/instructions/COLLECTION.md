# Writing conventions for kb/instructions/ (prescriptive register)

## Register and precision

Prescriptive [register](../notes/definitions/register.md): procedures, conventions, skill bodies, and operational rules. Directs what to do — optimised for an agent (or human) executing on first reading, without prior context.

Quality goal is **executability + precision** — every step actionable, every decision point explicit, ambiguity eliminated. A vague prescription wastes bounded context on interpretation rather than action.

Tests for precision:
- Could an agent with no prior context execute each step without asking a clarifying question?
- Are decision points explicit — "if X, do A; otherwise do B" — rather than implied?
- Are scope boundaries stated — when does this NOT apply, and what to do instead?
- Is reasoning minimal — just enough for edge cases, with the "why" living in theory notes?

**Frontloading.** Self-contained enough for an agent with no prior context. Define terms inline; don't assume the reader has loaded other KB documents.

**Reasoning constraint.** Cut explanations of *why* each step exists from the instruction body. If worth preserving, record in a theory note and link via `rationale` (for meta-readers only). Keep only enough reasoning for edge cases and decisions.

**Instruction duality.** These docs are both content and working system — changing an instruction changes agent behaviour immediately. Treat edits as deployments, not documentation updates.

## Title and description conventions

**Imperative titles.** Answer "what does this tell me to do?" — "Write an instruction", "Review triage", "Fix warnings". For promoted skills, the skill name is the title (`write/SKILL.md`).

**Description** (frontmatter) should name the trigger condition — when to use this procedure.

## Outbound links

**Links are exceptional in this collection.** A procedure must execute from its own text; an executing agent should not follow outbound links to complete the task. Permitted cases:

- **Context-transfer** — sub-agent invocations (link is a bootstrap for a new, clean context, not a required read in the current one).
- **Conditional deviations** — error procedures, specialised branches, paths followed only on a specific trigger. Frontloading every deviation would bloat the main path.
- **Meta-reader needs** — `rationale` links serve reviewers and developers updating the procedure, never executing agents.

Forward-authored; backlinks are computed. Inline for strongest commitment, with a connective word that fits (e.g. `after [title](path)`, `if [title](path)`). Footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/instructions/`, `kb/notes/`, and `kb/reference/` for link targets. Do not link into `kb/agent-memory-systems/`, `kb/agentic-systems/`, or `kb/work/`. Keep chains shallow — a procedure that requires chasing five other procedures to execute isn't a procedure, it's a reading list.

**Labels:**

| label | destinations | reader-need / when to use |
|---|---|---|
| `composition` | instructions | sequential: complete this, then follow the target. Reader drops current context |
| `precondition` | instructions | conditional: verify target is done/true before starting; skip if already satisfied |
| `invokes` | instructions | subroutine call. **Prefer sub-agent invocation** so context resets; same-context only for small, heavily-reused procedures |
| `applies-when` | instructions | conditional branch; reader follows only if the trigger applies |
| `see-also` | instructions | reserved for error procedures and conditional fallbacks |
| `operates-on` | reference | the system component this procedure acts on |
| `rationale` | notes | (meta-reader) the theoretical claim this rule rests on |

## Frontmatter

Minimal. Plain instructions need `description` and `type: kb/types/instruction.md`. Promoted skills add skill-specific fields (`name`, `allowed-tools`, `context`, `model`) in their `SKILL.md`. Review gates use `type: kb/types/review-gate.md` and the gate-specific fields documented in that type spec; see `../reference/REVIEW-SYSTEM.md` for runtime concepts.

## Promoted skills

Some subdirectories are promoted into runtime skill surfaces (`.claude/skills/`, `.agents/skills/`) by `commonplace-init`. Promoted skills:

- Must not rely on on-disk location being `kb/instructions/<name>/`
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

| type | file | use for |
|---|---|---|
| `instruction` | `kb/types/instruction.md` | procedures, skills, wrapper prompts, review gates |
| `index` | `kb/types/index.md` | generated directory indexes and instruction navigation hubs |

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Descriptions of how the system works → `kb/reference/`
- Generated reports and reviews → `kb/reports/`
- Work in progress → `kb/work/` (workshops)
