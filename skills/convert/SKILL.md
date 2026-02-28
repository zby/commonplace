---
name: convert
description: Convert notes between types. Currently supports text→note (add frontmatter with status seedling, rename file to match title, fix backlinks). Future directions include note→spec/review/adr and demotion back to text. Triggers on "/convert", "/convert [note]".
user-invocable: true
allowed-tools: Read, Edit, Grep, Glob, Bash
context: fork
model: sonnet
argument-hint: "[note] — path or filename in kb/notes/. Optional: [note] to [type]"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:
- If target contains just a note name or path: convert text → note
- If target contains "[note] to [type]": convert to the specified type
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
type: note
traits: []
areas: []
status: seedling
---
```

**Rules:**
- `status` is always `seedling` — conversion structures the note but does not endorse it. Human review flips to `current`.
- `description` must add information beyond the title. See [note base type](../../types/note.md) for quality criteria.
- `traits` is always `[]` — trait assignment is semantic work, done later by `/validate` or human review.
- `areas` is always `[]` — area assignment is semantic work, done later by `/connect` or human review.
- Do NOT modify the body content. Conversion adds structure, not editorial changes.

#### Step 3a: Rename the file

After adding frontmatter, check whether the filename matches the `# Title` heading.

The filename should match the title — whether the title itself is good is a semantic question for `/validate`.

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

text → note (status: seedling)

renamed: old-filename.md → new-filename.md  [or "filename unchanged" if no rename]
backlinks updated: 3 files  [or "none" if no backlinks]

description: [the description you wrote]
areas: [list or empty]

Next steps:
- /connect new-filename.md — find connections
- /validate new-filename.md — check quality
- Review and set status: current when endorsed
===
```

### note → structured-claim

Promotes a note with a claim title into a fully structured argument with Toulmin-derived sections.

#### Step 1: Locate and verify

Resolve the target to a file path. Read the file. Verify it has frontmatter with `type: note` (or no explicit type). If it's already `type: structured-claim`, report and stop.

#### Step 2: Restructure body

Add or identify `## Evidence`, `## Reasoning`, and `## Caveats` sections. Move existing content into the appropriate sections:
- Observations, facts, references → `## Evidence`
- Principles connecting evidence to the title claim → `## Reasoning`
- Scope limits, assumptions, counterarguments → `## Caveats`

#### Step 3: Update frontmatter

- Set `type: structured-claim`
- Keep `status` unchanged (conversion doesn't endorse)

#### Step 4: Report

```
=== CONVERTED: filename.md ===

note → structured-claim

Sections added: Evidence, Reasoning, Caveats
description: [unchanged]

Next steps:
- /validate filename.md — check quality
- Review and set status: current when endorsed
===
```

### Future conversions (not yet implemented)

These are documented as directions, not working features. If a user requests one, explain it's not implemented yet.

- **note → spec**: add Design/Implementation sections
- **note → review**: add Findings section, date
- **note → adr**: add Context/Decision/Consequences sections
- **any → text**: strip frontmatter, demote to raw capture (for notes that didn't work out)

## Critical Constraints

**Never:**
- Set `status: current` — that requires human review
- Modify body content — only add/change frontmatter
- Convert a text file that already has frontmatter (it's not a text file)
- Write a description that merely restates the title
- Move a file to a different directory — rename only changes the filename within its current directory

**Always:**
- Set `status: seedling` for text → note conversions
- Write a description that adds mechanism, scope, or implication
- Rename the file to match the `# Title` heading (unless it already does)
- Fix all backlinks when renaming
- Use `git mv` for renames so git tracks the history
- Report what was done so the user can review
