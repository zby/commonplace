---
name: cp-skill-convert
description: Convert notes between types. Currently supports text to note by adding unverified structured frontmatter, renaming the file to match the title, and fixing backlinks. Use with a note path or note name.
type: kb/types/instruction.md
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
description: [50-200 chars, adds mechanism/scope/implication beyond the title]
type: kb/types/note.md
traits: []
tags: []
---
```

**Rules:**
- Do not add `user-verified` — conversion structures the note but cannot grant human attestation.
- `description` must add information beyond the title. See [note base type](../../types/note.md) for quality criteria.
- `traits` is always `[]` — trait assignment is semantic work, done later by the `cp-skill-validate` skill or human review.
- `tags` is always `[]` — tag assignment is semantic work, done later by the `cp-skill-connect` skill or human review.
- Do NOT modify the body content. Conversion adds structure, not editorial changes.

#### Step 3a: Rename the file

After adding frontmatter, check whether the filename matches the `# Title` heading.

The filename should match the title — whether the title itself is good is a semantic question for the `cp-skill-validate` skill.

**Decide whether to rename:**
- If the current filename is already a good slug of the `# Title` — keep it
- If the filename diverges from the title (e.g. file is `connect-pipeline-features.md` but the title is `# Connect pipeline should detect reciprocal links`) — rename it to match

**To rename:**
1. Derive the new filename from the `# Title` heading. Slugify: lowercase, hyphens for spaces, strip punctuation, `.md` extension.
2. Check for backlinks to the old path:
   ```bash
   rg -l 'old-filename\.md' kb/
   ```
3. If backlinks exist, update them all to point to the new filename (preserve the same relative path structure — only the filename changes, not the directory).
4. Rename the file:
   ```bash
   git mv old-path/old-filename.md old-path/new-filename.md
   ```

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
- Run the `cp-skill-connect` skill on `new-filename.md` — find connections
- Run the `cp-skill-validate` skill on `new-filename.md` — check quality
- Optionally ask the user to verify the artifact after review; only the human may add `user-verified: true`
===
```

### Future conversions (not yet implemented)

These are documented as directions, not working features. If a user requests one, explain it's not implemented yet.

- **note → structured-claim**: add Evidence/Reasoning/Caveats sections and set the collection-local structured-claim type
- **note → spec**: add Design/Implementation sections
- **note → review**: add Findings section, date
- **note → adr**: add Context/Decision/Consequences sections
- **any → text**: strip frontmatter, demote to raw capture (for notes that didn't work out)

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
- Fix all backlinks when renaming
- Use `git mv` for renames so git tracks the history
- Report what was done so the user can review
