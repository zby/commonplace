# Revert instructions: undo tag rename and review cross-register links

## Context

An earlier session renamed `type-system` tags to `types` across 11 notes in `kb/notes/`, deleted `type-system-index.md`, and updated links from `../reference/type-system.md` to `../reference/available-types.md`. These changes are all uncommitted.

The tag rename was wrong — tags are per-collection, and notes should keep `type-system` as their tag. The link updates need case-by-case review: some may be legitimate (the target file was renamed), but theory notes linking to description docs should be examined for whether the link is evidence/example (OK) or makes the theory depend on our specific implementation (not OK).

## Step 1: Revert all uncommitted changes to kb/notes/

This is the safest approach — restore everything to the committed state, then make intentional changes.

```bash
# Check what will be restored
git diff --stat -- kb/notes/

# Restore all modified files in kb/notes/ to committed state
git checkout HEAD -- kb/notes/

# Verify the revert
git diff --stat -- kb/notes/
```

This reverts:
- All 11 tag changes (`types` → back to `type-system`)
- All link updates (`available-types.md` → back to `type-system.md`)
- The deletion of `type-system-index.md` (restored)
- Any other uncommitted prose changes in notes

**Note:** This does NOT touch:
- `kb/notes/types-index.md` (committed in e50a651 — still exists, needs separate decision)
- `kb/reference/` changes (committed)
- `kb/instructions/` changes (committed, if any)
- New files added during this session (the three-register theory note, workshop files)

## Step 2: Delete the duplicate types-index.md

`types-index.md` was created in `kb/notes/` to replace `type-system-index.md`. Since we're restoring the original, the duplicate should go.

```bash
git rm kb/notes/types-index.md
```

## Step 3: Fix broken links

After the revert, notes will link to `../reference/type-system.md` which no longer exists (it was renamed to `available-types.md` in a committed change). These links will break.

```bash
# Find broken links
uv run commonplace-validate-notes kb/notes/ 2>&1 | grep "FAIL.*link"
```

For each broken link, decide:
- **If the link is an example/evidence link** (theory uses our system as illustration): update the path to `../reference/available-types.md` but keep the relationship as "example" or "exemplifies"
- **If the link makes the theory depend on our implementation**: remove the link or replace it with a more generic description of the concept

## Step 4: Verify

```bash
# Tags should show type-system, not types
rg "^tags:.*type-system" kb/notes/

# No notes should have tags: [types]
rg "^tags:.*\[types\]" kb/notes/

# type-system-index should exist and use type-system
head -6 kb/notes/type-system-index.md

# types-index should be gone
ls kb/notes/types-index.md 2>/dev/null && echo "STILL EXISTS" || echo "GONE"

# Validate
uv run commonplace-validate-notes kb/notes/
```

## Step 5: Handle document-system-index.md

Check `kb/notes/document-system-index.md` — it may have an uncommitted reference to `types-index.md` that should point to `type-system-index.md` instead. The revert in Step 1 should handle this, but verify.

## What this does NOT resolve

- Whether `kb/reference/` docs should keep their `types` tags (they should — it's a reference-local tag, but reference has no index for it yet)
- Whether to update `sync_generated_index.py` to support per-collection index generation
- The `kb/instructions/WRITING.md` uncommitted changes (check `git diff -- kb/instructions/` separately)
