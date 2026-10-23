---
type: types/type-spec.md
name: task
description: Stable runbook for a task that runs unattended on a cadence, paired with an appended log
schema: null
---

# Task

## Authoring Instructions

Use this template for a task that runs unattended on a cadence. `kb/tasks/` is flat: the runbook `kb/tasks/<name>.md` sits beside its log `kb/tasks/<name>-log.md`. There is no backlog or active queue; one-off work is a workshop under `kb/work/`.

- This file is a runbook, not a run log. Update it only when the process or scope changes.
- `Scope` should name the files or areas covered by the recurring review.
- `Run Procedure` should be a stable checklist.
- `Cadence` says when a run is due, in terms the heartbeat can compute from the log's latest dated section.
- `Output` should say where each run's findings are recorded and how to append them.
- `Write scope` lists the only paths a run may change and the commit subject it uses.
- `Consumer` names what reads the output; a task nothing reads is not admitted.

## Frontmatter

No frontmatter is currently required for task documents; this type has `schema: null`, and existing task files may be plain Markdown. If a runbook is explicitly typed for discovery or review, use these fields:

| Field | Required | Use |
|---|---:|---|
| `description` | No | Retrieval description of the task's scope. |
| `type` | No | `tasks/types/task.md` when the runbook is made into an explicitly typed artifact. |
| `tags` | No | Routing tags for the work area or review cadence. |

Individual run state belongs in the output log. Do not add a generic frontmatter `status` field to the stable runbook.

The template below predates the heartbeat work; the `Cadence`, `Write scope` and `Consumer` sections are being settled in `kb/work/recurring-task-runner/` and will be added here once two hand launches have used them.

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

Record findings in `kb/tasks/review-<area>-log.md`.
Append one dated section per run (for example `## 2026-02-06`) with summary, findings, and follow-ups.
```
