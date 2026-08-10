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
- Fix only what the executor can't determine at run time: the goal, constraints, what *done* means, privileged facts, and arbitrary choices (paths, names, templates, which valid interpretation to follow). Leave anything the executor can determine from the live system to the executor — a fixed detail is an authoring-time snapshot and goes stale.
- Keep rationale minimal. Put durable reasoning in `kb/notes/` and link from there.

## Operativity

An instruction changes system behavior only through a path: something consumes it, over some channel, with some force. Before writing or editing one, name that path — what loads this text (harness skill selection, a collection contract, a link from another instruction, a human invoking it) and when it fires. An instruction nothing loads is inert: it persists, stays true, and changes nothing — and it fails silently, because no consumer means no error either.

- For link- and search-mediated consumers, the `description` is the retrieval wire: write it to match the query an agent would issue at the moment the instruction should fire, not the vocabulary of the instruction's own content.
- If the instruction should fire on a condition (a kind of change, a kind of artifact), check that a surface loaded in that situation actually routes here. If nothing does, add the route or record the gap — do not assume discovery.

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

---

Relevant Notes:

- [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) - rationale for the detail-level rule: which details to fix and which to leave to the executor
- [Operative change](../notes/definitions/operative-change.md) - rationale for the operativity rule: a change operates only through a consumer, channel, and force over a declared horizon
- [A retrieval miss is a local reflective-path failure](../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) - rationale for the description and routing rules: retrieval is the wire a retained instruction acts along, and it is best-effort unless a loaded surface enumerates the route
