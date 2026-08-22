# Writing conventions for kb/instructions/

## Text contract and precision

This collection contains procedures, conventions, skill bodies, and operational rules. It directs what to do — optimised for an agent (or human) executing on first reading, without prior context.

Quality goal is **executability + precision** — every step actionable, every decision point explicit, ambiguity eliminated. A vague prescription wastes bounded context on interpretation rather than action.

Tests for precision:
- Could an agent with no prior context execute each step without asking a clarifying question?
- Are decision points explicit — "if X, do A; otherwise do B" — rather than implied?
- Are scope boundaries stated — when does this NOT apply, and what to do instead?
- Is reasoning minimal — just enough for edge cases, with the "why" living in theory notes?

**Frontloading.** Self-contained enough for an agent with no prior context. Define terms inline; don't assume the reader has loaded other KB documents.

**Reasoning constraint.** Cut explanations of *why* each step exists from the instruction body. If worth preserving, record in a theory note and link via `rests-on` (for meta-readers only). Keep only enough reasoning for edge cases and decisions.

**Instruction duality.** These docs are both content and working system — changing an instruction changes agent behaviour immediately. Treat edits as deployments, not documentation updates: before changing one, name what consumes it and through which channel (the type spec's Operativity section states the test); the edit is live for the next agent that loads the text, with no separate release step. The same duality means an instruction nothing loads is inert — it deploys to no one, and nothing will report that (rationale: [operative change](../notes/definitions/operative-change.md)).

## Title and description conventions

**Imperative titles.** Answer "what does this tell me to do?" — "Write an instruction", "Review triage", "Fix warnings". For promoted skills, the skill name is the title (`write/SKILL.md`).

**Description** (frontmatter) should name the trigger condition — when to use this procedure.

## Outbound links

**Links are exceptional in this collection.** A procedure must execute from its own text; an executing agent should not follow outbound links to complete the task. Permitted cases:

- **Context-transfer** — sub-agent invocations (link is a bootstrap for a new, clean context, not a required read in the current one).
- **Conditional deviations** — error procedures, specialised branches, paths followed only on a specific trigger. Frontloading every deviation would bloat the main path.
- **Meta-reader needs** — `rests-on` links serve reviewers and developers updating the procedure, never executing agents.

Author each outbound link from the reader need at its source. A reciprocal link is allowed when the reverse direction independently helps readers, subject to this collection's exceptional-link posture; never add one merely to mirror an existing edge. Find inbound links on demand with repository search; no backlink view is currently generated. Inline for strongest commitment, with a connective word that fits (e.g. `after [title](path)`, `if [title](path)`). Footer for labelled — `- [title](path) — label: context phrase`.

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
| `rests-on` | notes | (meta-reader) this procedure or rule depends on the target theoretical claim |

## Frontmatter

Minimal. Plain instructions need `description` and `type: kb/types/instruction.md`. Promoted skills add skill-specific fields (`name`, `allowed-tools`, `context`, `model`) in their `SKILL.md`. Review gates use `type: kb/types/review-gate.md` and the gate-specific fields documented in that type spec; see `../reference/README-REVIEW-SYSTEM.md` for runtime concepts.

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

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Descriptions of how the system works → `kb/reference/`
- Generated reports and reviews → `kb/reports/`
- Work in progress → `kb/work/` (workshops)
