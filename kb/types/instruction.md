---
type: kb/types/type-spec.md
name: instruction
description: Prescriptive procedure, skill body, wrapper prompt, or review gate used by agents and maintainers
schema: kb/types/instruction.schema.yaml
---

# Instruction

## Authoring Instructions

Use `instruction` for prescriptive content: procedures, skill bodies, wrapper prompts, review gates, work packets handed to sub-agents. The shared property is that the content tells an agent or maintainer what to do, not what is true.

## Frontmatter

- Set `type: kb/types/instruction.md`.
- Write `description` as the trigger condition: when an agent should use this instruction.
- Additional frontmatter is governed by the specific runtime consumer (the harness for skills, the review system for gates, etc.).

## Structure

- Title imperatively or as an action.
- Keep the body executable on first reading.
- State prerequisites, scope boundaries, decision points, and verification checks where they matter.
- Keep rationale minimal. Put durable reasoning in `kb/notes/` and link from there.

## Template

```markdown
---
description: "{When to use this instruction}"
type: kb/types/instruction.md
---

# {Imperative title}

{What this instruction does and when to use it. Body sections follow the
shape that fits the work.}
```
