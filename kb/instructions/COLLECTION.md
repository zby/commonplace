# Writing conventions for kb/instructions/ (prescriptive register)

## Register

This collection operates in the **prescriptive register**. Documents here direct what to do — procedures, conventions, skill bodies, and operational rules. They optimize for an agent (or human) executing them on first reading, without prior context.

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

When linking FROM this collection:

| To register | Appropriate relationships | Notes |
|---|---|---|
| Prescriptive (same register) | composition — "after [step A], follow [step B]" | Procedures can chain to other procedures. Keep the chain shallow — deep composition defeats frontloading. |
| Theoretical (kb/notes/) | justification — "this rule exists because [theory]" | Instructions can cite theories as rationale for why a rule exists. The instruction depends on the theory — if the theory changes, the instruction may need revision. |
| Descriptive (kb/reference/) | reference — "this procedure acts on [system X]" | Instructions reference system descriptions when the agent needs to understand what it's operating on. |

**Reasoning constraint.** Cut explanations of *why* each step exists. If the reasoning is worth preserving, it belongs in a methodology note that links to this instruction — not in the instruction itself. Keep only enough reasoning for the agent to handle edge cases and decision points.

## Frontmatter

Instructions use minimal frontmatter. Plain instructions need only `description`. Promoted skills add skill-specific fields (`name`, `allowed-tools`, `context`, `model`) in their `SKILL.md`.

## Promoted skills

Some instruction subdirectories are promoted into runtime skill surfaces (`.claude/skills/`, `.agents/skills/`) by `commonplace-init`. Promoted skills:

- Must not rely on their on-disk location being `kb/instructions/<name>/`
- Should use stable workspace-root paths (`kb/notes/`, `kb/instructions/COLLECTION.md`)
- Treat `kb/instructions/` as the searchable source surface and runtime skill directories as compiled copies

## Default template

```markdown
---
description: ""
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

## What does NOT belong here

- Transferable claims about KB methodology → theoretical register (`kb/notes/`)
- Descriptions of how the system works → descriptive register (`kb/reference/`)
- Generated reports and reviews → `kb/reports/`
- Work in progress → `kb/work/` (workshops)
