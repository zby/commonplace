---
type: reference/types/design-proposal.md
description: "Proposal (adopted): Historical run-ID collisions and worktree transfer state before ADR 106 introduced tokenized runs and Git integration"
---

# Merging analysis runs back from isolated worktrees

> **Archived** (see [archive README](./README.md)). Adopted by
> [ADR 106](../../adr/106-merge-analysis-publications-from-isolated-worktrees.md).
> The analysis skill, integration command and ADR carry the live design. The
> dated collision and transfer observations below remain historical evidence.

## Current state (as of 2026-10-05)

Preparation made a detached worktree under `.commonplace/worktrees/` and wrote
its commit and command environment to a sibling `.preparation.json` file. It
did not record a separate worktree token. Each worktree allocated its own
`AAS-<date>-<slug>-<nn>` sequence under ignored run state.

Three Dynamic Cheatsheet runs in three worktrees received the same
`AAS-2026-10-04-dynamic-cheatsheet-01` ID. The first became the incumbent on
`main`; the third reached publication but was refused with “replacement
requires a new run ID.” The public Dynamic Cheatsheet set entered as commit
`c59d2b8a4`, whose parent was its method commit `bb3126f84`. No general
transfer procedure existed; the skill only said to transfer after operator
authorization.

The `retained_overview_path` helper derived a source slug by dropping the
last segment of a run ID. Only tests called it. Type prose used the old ID
placeholder while schemas accepted any additional lowercase segment.

The three reliability audits under `kb/work/analysis-collection-split/`
recorded the same run ID. Their evidence files distinguished runs only by
worktree path and used both `method-commit` and `method_commit` keys. One
completed worktree had already been removed, although the skill said not to
remove worktrees because their run state was evidence.

## Retained boundary

These observations describe the pre-adoption system. ADR 106 records the
chosen identity, integration and evidence-retention rules. No implementation
commission remains in this archive entry.
