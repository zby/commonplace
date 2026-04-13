---
name: cp-skill-validate
description: Run the deterministic validation script on KB notes. Checks frontmatter validity, enum values, link health, required sections, and batch signals (orphans, seedling count).
user-invocable: true
allowed-tools: Bash
context: fork
---

## EXECUTE NOW

Run the packaged validation command:

```bash
commonplace-validate "$ARGUMENTS"
```

**Target: $ARGUMENTS**

- Note path or name: validate that specific note
- Directory path or collection name: validate `.md` files under that directory
- "all": validate all `.md` files under `kb/`
- "notes": validate all `.md` files in `kb/notes/`
- "recent" or "today": validate notes modified today
- Empty: ask which note to validate

Report the script output directly. Do not interpret, supplement, or override its findings.

For judgment-based frontmatter checks, run `kb/instructions/run-review-bundle-on-note.md` with the `frontmatter` bundle.
