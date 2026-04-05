---
description: Complexity review wrapper — keep the old entrypoint, but route execution through the gate bundle
---

# Complexity Review

This file is a compatibility wrapper. The canonical complexity bundle now resolves directly from:

- `kb/instructions/review-gates/complexity/`

Preferred execution path for shell automation:

```bash
uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} complexity
```

If you are invoking this instruction from an agent, treat it as shorthand for:

> Run `kb/instructions/run-review-bundle-on-note.md` on `{note-path}` for gates: `complexity`

Do not copy the old monolithic check text from this file into new workflows. The gate files are the source of truth.
