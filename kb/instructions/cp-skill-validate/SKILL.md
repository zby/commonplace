---
name: cp-skill-validate
description: Run the deterministic validation script on KB notes. Checks frontmatter validity, schema constraints, link health, required sections, and batch signals such as orphans.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Bash
context: fork
---

## EXECUTE NOW

Run the packaged validation command. For `all`, invoke each top-level collection separately because the CLI deliberately rejects a repository-wide literal scope:

```bash
if [ "$ARGUMENTS" = "all" ]; then
  for contract in kb/*/COLLECTION.md; do
    commonplace-validate "$(basename "$(dirname "$contract")")" || exit $?
  done
else
  commonplace-validate "$ARGUMENTS"
fi
```

**Target: $ARGUMENTS**

Prefer the narrowest target that covers the user's request. For write/edit workflows, validate the new or edited file paths explicitly; do not validate the whole KB unless the user asked for a full maintenance check.

- Note path or name: validate that specific note
- Multiple note paths: validate those specific notes, one command per path if needed
- Directory path or collection name: validate `.md` files under that directory, only when the edited set is directory-scoped
- "all": validate each top-level collection in a separate command
- "notes": validate all `.md` files in `kb/notes/`
- "recent" or "today": validate notes modified today
- Empty: ask which note to validate

Report the script output directly. Do not interpret, supplement, or override its findings.

For judgment-based frontmatter checks, run `kb/instructions/run-review-batches.md` with the `frontmatter` bundle.
