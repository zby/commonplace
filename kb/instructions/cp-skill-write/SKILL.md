---
name: cp-skill-write
description: Write a KB artifact using the default note workflow or a discovered type template. Routes by type, reads the target collection's COLLECTION.md, searches first, and validates after writing. Use with an optional type and optional topic.
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[path | collection | type] [topic] — a note path for editing, or a collection/type/topic for new notes"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

All documents in the KB live in a **collection** — a top-level directory under `kb/` (`kb/notes/`, `kb/reference/`, `kb/instructions/`). Each collection has a `COLLECTION.md` with its writing conventions. Documents have a **type** (`note`, `definition`, `adr`, etc.) that determines their structural template.

### Step 1 — Parse arguments

**Edit mode** — first argument is a path to an existing `.md` file: read it, infer collection from path (`kb/notes/` → notes, etc.), read `type` from frontmatter (default `note`; no frontmatter → `text`). Remaining arguments describe what to change.

**New-note mode** — everything else. Extract the collection, type, and topic from the arguments (natural language is fine). Defaults: collection `notes`, type `note`. No arguments → ask the user what to write about.

**Type resolution**: for non-default types, find the template at `kb/**/types/{type}.template.md`. The template's location tells you which collection the type belongs to (e.g. `kb/reference/types/adr.template.md` → `kb/reference/`). If no template is found, list available types and stop.

### Step 2 — Load collection conventions

Read `kb/<collection>/COLLECTION.md` for the collection's writing conventions.

**Hard fail** if `kb/<collection>/COLLECTION.md` does not exist: stop and tell the user the collection is not configured. Every collection that accepts writes must have a COLLECTION.md — its register, quality goal, and linking rules are what distinguish collections. Do NOT proceed with default conventions; a silently-default write produces content that doesn't follow the collection's quality goals and the failure won't be caught until review.

### Step 3 — Search before writing

Search the target collection first, then `kb/notes/` if different. Read closest matches to avoid duplication and find connection points. In edit mode, also search for notes linking to the target.

### Step 4 — Draft and save

**Template**: for types other than `note`, use the template found during type resolution. If `{type}.instructions.md` exists alongside it, follow it. For `text`, raw markdown without frontmatter. Never invent a type when no template exists. For the default `note` type, use this template:

```
---
description: ""
type: note
traits: []
tags: []
status: seedling
---

# {Title — style per collection conventions}

{Opening paragraph.}

{Body.}

## Open Questions

- {Omit section if none}

---

Relevant Notes:

- [related-note](./related-note.md) — {relationship per collection's outbound linking rules}
```

**New notes**: follow resolved template and collection conventions. Derive lowercase-hyphenated filename from `# Title` (max 100 chars). Set traits only when clearly warranted: `title-as-claim`, `definition`, `has-comparison`, `has-external-sources`, `has-implementation`.

**Edits**: apply requested changes respecting collection conventions. Preserve existing frontmatter and links unless the edit specifically changes them.

### Step 5 — Validate

Run `cp-skill-validate` on the written file. Fix structural issues before stopping. Suggest `cp-skill-connect` as the next step.

## Universal mechanics

These apply to all typed artifacts regardless of collection.

**Frontmatter** makes notes queryable. No frontmatter → `text` type. Required: `description` (double-quoted, 50-200 chars). Optional: `type`, `traits` list, `tags` list, `status` (`seedling` / `current` / `speculative` / `outdated`).

**Descriptions** are retrieval filters, not summaries. The test: if an agent searched for this note's concept and got 5 results, would this description help pick THIS one? Paraphrasing the title adds zero retrieval value.

**Links**: relative markdown paths from source file. Prefer inline links as prose ("Since [claim](./claim.md)..."). Footer links for connections outside prose, always with relationship annotation (`— extends / foundation / contradicts / enables / example`). Every link must point to a real file — verify with `ls`.

**Filenames**: lowercase, hyphens, `.md`, derived from `# Title`, max 100 chars.

**Distillation tracking**: when distilling from notes into a focused artifact, add `Distilled into:` in each source note's footer. The distilled artifact does NOT link back.

**Renames**: never rename manually — use `commonplace-relocate-note` to update backlinks.
