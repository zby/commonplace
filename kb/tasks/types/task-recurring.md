---
type: kb/types/type-spec.md
name: task-recurring
description: Stable recurring maintenance or review runbook
schema: null
---

# Task recurring

## Authoring Instructions

Use this template for stable recurring reviews or maintenance runs.

- This file is a runbook, not a run log. Update it only when the process or scope changes.
- `Scope` should name the files or areas covered by the recurring review.
- `Run Procedure` should be a stable checklist.
- `Output` should say where each run's findings are recorded and how to append them.

## Frontmatter

No frontmatter is currently required for recurring task documents; this type has `schema: null`, and existing task files may be plain Markdown. If a runbook is explicitly typed for discovery or review, use these fields:

| Field | Required | Use |
|---|---:|---|
| `description` | No | Retrieval description of the recurring review or maintenance scope. |
| `type` | No | `kb/tasks/types/task-recurring.md` when the runbook is made into an explicitly typed artifact. |
| `tags` | No | Routing tags for the work area or review cadence. |
| `status` | No | KB lifecycle status if needed; individual run state belongs in the output log, not this runbook. |

## Template

```markdown
# Review: Area Name

Brief description of what this review covers.

This file is a stable runbook. Do not edit it per run; only change it when scope or process changes.

## Scope

- `path/to/module/` - Description
- `path/to/file.py` - Description

## Run Procedure

- Check item 1
- Check item 2
- Check item 3

## Output

Record findings in `kb/code-reviews/review-<area>.md`.
Append one dated section per run (for example `## 2026-02-06`) with summary, findings, and follow-ups.
```
