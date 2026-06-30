---
description: Complexity review wrapper — keep the old entrypoint, but route execution through the gate bundle
type: kb/types/instruction.md
---

# Complexity Review

This file is a compatibility wrapper. The canonical complexity bundle now resolves directly from:

- `kb/instructions/review-gates/complexity/`

Treat this instruction as shorthand for:

> Run `kb/instructions/run-review-batches.md` with requested mode on `{note-path}` for gates: `complexity`

Do not copy the old monolithic check text from this file into new workflows. The gate files are the source of truth.
