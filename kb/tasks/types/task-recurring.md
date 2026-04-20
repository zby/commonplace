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
