---
name: cp-skill-validate
description: Run deterministic validation on KB artifacts, collections, collection landings, and the published redirect map, including schemas, links, required sections, and batch signals.
type: types/instruction.md
user-invocable: true
allowed-tools: Bash
context: fork
---

## EXECUTE NOW

Run the packaged validation command. For `all`, invoke each top-level collection separately because the CLI deliberately rejects a repository-wide literal scope. Run every check even after a failure, and report failure at the end:

```bash
if [ "$ARGUMENTS" = "all" ]; then
  status=0
  for contract in kb/*/COLLECTION.md; do
    commonplace-validate "$(basename "$(dirname "$contract")")" || status=1
  done
  commonplace-validate landings || status=1
  if [ -f properdocs.yml ]; then
    commonplace-validate redirects || status=1
  fi
  exit $status
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
- "landings": validate that every top-level collection has a non-colliding `README.md`
- "redirects": validate the live `properdocs.yml` redirect map against its published tree
- "notes": validate all `.md` files in `kb/notes/`
- "recent" or "today": validate notes modified today
- Empty: ask which note to validate

Report the script output directly. Do not interpret, supplement, or override its findings.

For judgment-based frontmatter checks, run [run-review-batches](../run-review-batches.md), resolved from this skill's real location, with the `frontmatter` bundle.
