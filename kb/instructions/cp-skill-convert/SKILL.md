---
name: cp-skill-convert
description: Convert notes between types. Currently supports text to note by adding unverified structured frontmatter, renaming the file to match the title, and fixing backlinks. Use with a note path or note name.
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Grep, Glob, Bash
context: fork
model: sonnet
argument-hint: "[note] — path or filename in kb/notes/"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:
- If target contains just a note name or path: convert text → note
- If target requests another conversion form, explain that only text → note is currently implemented
- If target is empty: ask which note to convert

## Supported conversions

### text → note (current)

The primary conversion. Adds frontmatter to a raw text file, making it structured and connectable.

#### Step 1: Locate and verify

Resolve the target to a file path. If just a name, search `kb/notes/` recursively.

Read the file. Verify it has **no frontmatter** (does not start with `---`). If it already has frontmatter, report that it's already structured and stop.

#### Step 2: Understand the content

Read the full file. Identify:
- The core topic (what is this about?) — needed for writing the description
- Whether the current filename matches the `# Title` heading (see Step 3a)

#### Step 3: Generate frontmatter

Add YAML frontmatter at the top of the file:

```yaml
---
description: [50-250 chars, adds mechanism/scope/implication beyond the title]
type: types/note.md
traits: []
tags: []
---
```

**Rules:**
- Do not add `user-verified` — conversion structures the note but cannot grant human attestation.
- `description` must add information beyond the title. See [note base type](../../types/note.md) for quality criteria.
- `traits` is always `[]` — trait assignment is semantic work, done later by a writer or human reviewer; deterministic validation does not infer traits.
- `tags` is always `[]` — tag assignment is semantic work and remains empty
  until a separately authorized editing task assigns it. `cp-skill-connect`
  reports candidate links only; it does not edit tags or library artifacts.
- Do NOT modify the body content. Conversion adds structure, not editorial changes.

#### Step 3a: Rename the file

After adding frontmatter, check whether the filename matches the `# Title` heading.

The filename should match the title. Whether the title itself is good is a semantic question for a human or a frontmatter review assay; deterministic validation checks only its structural limits.

**Decide whether to rename:**
- If the current filename is already a good slug of the `# Title` — keep it
- If the filename diverges from the title (e.g. file is `connect-pipeline-features.md` but the title is `# Connect pipeline should detect reciprocal links`) — rename it to match

**To rename:**
1. Dry-run the relocation with the `# Title` heading as the new name:
   ```bash
   commonplace-relocate-note old-path/old-filename.md "Title from the heading"
   ```
   It derives the filename from the title, lists every backlink it will rewrite, and adds the published-site redirect.
2. If the dry run is correct, run the same command with `--apply`. Never rename with `git mv` or by editing backlinks by hand: that skips the redirect and the full backlink rewrite.

**Rules:**
- The file stays in its current directory. Rename only, no move.
- If the title heading changed during frontmatter addition (it shouldn't — see "Do NOT modify body content"), use the original title.

#### Step 4: Report

```
=== CONVERTED: filename.md ===

text → note (unverified)

renamed: old-filename.md → new-filename.md  [or "filename unchanged" if no rename]
backlinks updated: 3 files  [or "none" if no backlinks]

description: [the description you wrote]
tags: []

Next steps:
- Run the `cp-skill-connect` skill on `new-filename.md` — report candidate
  connections without mutating the note
- Run the `cp-skill-validate` skill on `new-filename.md` — check deterministic structure and references
- Optionally ask the user to verify the artifact after review; only the human may add `user-verified: true`
===
```

### Unsupported conversions

If a user requests any conversion other than text → note, explain that it is
not implemented and stop. Do not invent a conversion or retain a speculative
feature catalogue. If repeated use establishes a concrete missing conversion,
route that design gap through the repository's normal proposal process before
adding it here.

## Critical Constraints

**Never:**
- Add `user-verified` — that requires explicit human attestation after review
- Modify body content — only add/change frontmatter
- Convert a text file that already has frontmatter (it's not a text file)
- Write a description that merely restates the title
- Move a file to a different directory — rename only changes the filename within its current directory
- Install software — if a required tool is missing, bail with an error

**Always:**
- Leave `user-verified` absent for text → note conversions
- Write a description that adds mechanism, scope, or implication
- Rename the file to match the `# Title` heading (unless it already does)
- Rename with `commonplace-relocate-note`, which rewrites every backlink and adds the redirect
- Commit a relocation alone, with no content edits, so `git log --follow` survives the rename
- Report what was done so the user can review
