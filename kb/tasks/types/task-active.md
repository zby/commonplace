---
type: kb/types/type-spec.md
name: task-active
description: Work-in-progress task state document for resumable active work
schema: null
---

# Task active

## Authoring Instructions

Use this template for work that is currently underway.

- `Status` should name the current execution state in operational terms.
- `Prerequisites` should make blocking dependencies explicit.
- `Goal` should define what done looks like.
- `Context` should gather the files, tasks, notes, and verification hooks needed to continue the work later.
- `Decision Record` is for choices made during execution.
- `Tasks` should reflect the actual next steps, not aspirational backlog.
- `Current State` should let another agent resume the work without rereading everything.

## Template

```markdown
# Task Name

## Status
information gathering | ready for implementation | waiting for <dependency>

## Prerequisites
- [ ] other-task-name (dependency on another task)
- [ ] design decision needed (new design / approval)
- [ ] none

## Goal
{What done looks like}

## Context
- Relevant files/symbols:
- Related tasks/notes/docs:
- How to verify / reproduce:

## Decision Record
- Decision:
- Inputs:
- Options:
- Outcome:
- Follow-ups:

## Tasks
- [x] completed step
- [ ] next step
- [ ] future step

## Current State
{Current state}

## Notes
- Short observations, gotchas, things tried
- Reference external docs for longer explanations
```
