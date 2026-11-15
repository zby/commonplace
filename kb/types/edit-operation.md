---
type: types/type-spec.md
name: edit-operation
description: "One named edit that a worker applies to one note text, returning a changed text, the unchanged text or a list of proposed changes"
schema: ./edit-operation.schema.yaml
---

# Edit operation

An edit operation is an instruction that takes one text of a note and returns one text of that note, or a list of changes it proposes. It is one of three kinds of improvement atom, beside review gates and stops. Use this type when the instruction edits the note's body within the kind of change its goal names. Use [`review-gate`](./review-gate.md) for a check that judges a text and edits nothing. Use [`instruction`](./instruction.md) for a procedure that arranges several operations, writes a second file, or edits more than one note.

An instance runs alone on one note. The [review command](../reference/commands.md) runs it as `commonplace-review run edit OPERATION NOTE`, and its result is an [edit result](./edit-result.md).

## The contract every instance shares

These rules hold for every instance, so no instance repeats them. The worker receives them from [execute a revision pass](../instructions/simplification-passes/execute-a-revision-pass.md).

- **Reads.** Files only: the text to edit, the operation, and the input files the caller names by role. An instance that needs something no file carries does not meet this contract.
- **May change.** The note's body, within the kind of change the instance's goal names.
- **Must preserve.** The title, the H1, the type and the brief declaration. Every link target, unless the result names its removal. Every quoted span. Every claim, qualification and example the instance does not explicitly permit changing. A needed title or claim change is reported, not applied.
- **Returns.** The changed text with one report line per change; or the unchanged text with a report of why nothing changed; or, for a `per-item` instance, a list of proposed changes applied to nothing. An instance that cannot proceed within these bounds reports a problem.

An instance does not edit the checkout, commit, launch other work or choose another operation.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/edit-operation.md` |
| `description` | Yes | The trigger condition: when the operation should be chosen. |
| `effort` | Yes | `simple` when a fresh worker on a cheaper profile can run it; `judgment` when it needs the stronger profile. |
| `decision` | Yes | `none` when the operation applies its changes. `per-item` when it first returns a list and the operator decides each entry; the second run applies the approved entries. |
| `depth` | No | Integer from 1. The order of concerns among edit operations; 1 runs first. A best-effort declaration, corrected from runs. |
| `responds-to` | No | Review criteria or lenses whose findings select this operation. A best-effort declaration. Without it, a plan or the operator selects the operation. |

`decision` records what the operation does. It does not grant authority to skip the operator's decision.

## Body

After the H1, an opening paragraph states the goal: what the operation exists to make true. Then three sections:

- `## Steps` — what the worker does. A step that needs an input file names its role, such as `findings` or `diff`, so the caller can supply it with `--input ROLE=PATH`.
- `## Report` — what the report lists, one line per change, and what is reported but not applied. A `per-item` operation also says what one proposal contains.
- `## Preserve` — what the operation keeps beyond the shared contract, and any removal it permits.

## Template

```markdown
---
description: "{When to choose this operation}"
type: types/edit-operation.md
effort: {simple | judgment}
decision: {none | per-item}
depth: {integer, optional}
responds-to: [{criterion or lens, optional}]
---

# {Imperative title}

{Goal: one sentence on what the operation makes true.}

## Steps

{What the worker does.}

## Report

{What the report lists.}

## Preserve

{What the operation keeps beyond the shared contract.}
```

---

Relevant Notes:

- [ADR 133 — Edit operations run alone through one typed route](../reference/adr/133-edit-operations-run-alone-through-one-typed-route.md) — depends-on: the decision that registered this type and its execution route
- [review architecture](../reference/review-architecture.md) — see-also: the code that runs an operation and checks its result
