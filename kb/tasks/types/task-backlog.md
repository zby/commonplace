---
type: kb/types/type-spec.md
name: task-backlog
description: Deferred task idea document with activation trigger and rough scope
schema: null
---

# Task backlog

## Authoring Instructions

Use this template for ideas that are worth keeping but not yet active work.

- `Idea` says what the task would do.
- `Why` explains why it might matter.
- `Rough Scope` should stay high level.
- `Why Not Now` records the current reason it is not active.
- `Trigger to Activate` should say what new condition would move it into active work.

## Frontmatter

No frontmatter is currently required for backlog task documents; this type has `schema: null`, and existing task files may be plain Markdown. If a task is explicitly typed for discovery or review, use these fields:

| Field | Required | Use |
|---|---:|---|
| `description` | No | Retrieval description of the deferred work and the condition that would make it relevant. |
| `type` | No | `kb/tasks/types/task-backlog.md` when the task is made into an explicitly typed artifact. |
| `tags` | No | Routing tags for the work area. |
| `status` | No | KB lifecycle status if needed; the backlog state itself belongs in `## Why Not Now` and `## Trigger to Activate`. |

## Template

```markdown
# Feature Name

## Idea
What this would do.

## Why
Why it might be valuable.

## Rough Scope
High-level bullets of what's involved.

## Why Not Now
What's blocking or why it's not a priority.

## Trigger to Activate
What would make this worth doing.
```
