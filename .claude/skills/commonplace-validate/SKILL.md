---
name: commonplace-validate
description: Run the deterministic validation script on KB notes. Checks frontmatter validity, enum values, link health, required sections, and batch signals (orphans, seedling count).
user-invocable: true
allowed-tools: Bash
context: fork
---

## EXECUTE NOW

Run the packaged validation command:

```bash
commonplace-validate-notes "$ARGUMENTS"
```

**Target: $ARGUMENTS**

- Note path or name: validate that specific note
- "all" or "notes": validate all `.md` files in `kb/notes/`
- "recent" or "today": validate notes modified today
- Empty: ask which note to validate

Report the script output directly. Do not interpret, supplement, or override its findings.

For judgment-based frontmatter checks, run `kb/instructions/run-review-bundle-on-note.md` with the `frontmatter` bundle.
