---
name: cp-skill-write
description: Write a KB artifact by reading the target collection conventions and the selected path-valued type-spec doc before drafting and validating.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[path | collection | type] [topic] — a note path for editing, or a collection/type/topic for new notes"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

All documents in the KB live in a **collection**: a top-level directory under `kb/` such as `kb/notes/`, `kb/reference/`, or `kb/instructions/`. Each collection that accepts writes has a `COLLECTION.md` with its register, quality goal, type offerings, and linking conventions.

Documents with frontmatter carry a path-valued `type:` that points to a type-spec doc, for example `type: kb/types/note.md` or `type: kb/reference/types/adr.md`. Files with no frontmatter are implicit `text`.

### Step 1 - Parse Arguments

**Edit mode**: first argument is a path to an existing `.md` file. Read it, infer collection from the path, and read its `type:` path from frontmatter. If it has frontmatter but no `type:`, stop and fix that structural problem before editing. If it has no frontmatter, treat it as implicit `text`. Open the type-spec doc named by `type:` before making structural edits.

**New-write mode**: everything else. Extract collection, type, and topic from the arguments. Defaults: collection `notes`, type `kb/types/note.md`. If the requested type is an instruction and no collection is explicit, use collection `instructions`.

For new writes, read the target collection's `## Types` section in `kb/<collection>/COLLECTION.md`. Pick one listed type path. If the requested type is not listed and the user did not give an explicit path, stop and list the available types. If the user gives an explicit `kb/.../*.md` type path, open that file and verify it is a type-spec doc before using it.

### Step 2 - Load Collection Conventions

Read `kb/<collection>/COLLECTION.md` for the collection's writing conventions.

**Hard fail** if `kb/<collection>/COLLECTION.md` does not exist. Every collection that accepts writes must have a `COLLECTION.md`; its register, quality goal, and linking rules are what distinguish collections. Do not proceed with default conventions.

### Step 3 - Load The Type Spec

Read the selected type-spec doc. Its frontmatter must include `type: kb/types/type-spec.md`, `name`, `description`, and `schema`. Its body supplies the artifact shape and may include a template block. Follow that body as the structural authoring contract.

Do not use legacy split type sidecars. Do not fall back from a missing type path to `note`.

For `text`, write raw markdown with no frontmatter only when the user explicitly wants unstructured capture. Otherwise use `kb/types/note.md`.

### Step 4 - Search Before Writing

Search the target collection first, then `kb/notes/` if different. Read closest matches to avoid duplication and find connection points. In edit mode, also search for notes linking to the target.

### Step 5 - Draft And Save

Follow the type-spec doc and collection conventions. Derive a lowercase-hyphenated filename from `# Title` unless editing an existing file. For typed artifacts, set `type:` to the exact repo-relative type-spec path, not the type name.

Set traits only when clearly warranted: `title-as-claim`, `definition`, `has-comparison`, `has-external-sources`, `has-implementation`.

Preserve existing frontmatter and links during edits unless the requested change requires changing them.

### Step 6 - Validate

Run targeted validation on the written or edited artifact, not the whole KB:

```bash
commonplace-validate path/to/written-file.md
```

If the task wrote or edited multiple KB artifacts, validate each explicit path or the smallest containing directory that covers only those artifacts. Do not run `commonplace-validate kb` or `cp-skill-validate all` as part of ordinary writing; full-KB validation is a separate maintenance operation and can surface unrelated warnings. Fix structural failures in the touched artifacts before stopping. Suggest `cp-skill-connect` as the next step when connection discovery would help.

## Universal Mechanics

These apply to all typed artifacts regardless of collection.

**Frontmatter** makes notes queryable. No frontmatter means implicit `text`; any file with frontmatter must include a path-valued `type:`. Most library notes also need `description` (double-quoted, 50-200 chars), plus optional `traits`, `tags`, and `status`.

**Descriptions** are retrieval filters, not summaries. The test: if an agent searched for this note's concept and got 5 results, would this description help pick this one? Paraphrasing the title adds zero retrieval value.

**Links** use relative markdown paths from the source file. Prefer inline links as prose. Footer links for connections outside prose should carry a relationship annotation (`extends`, `foundation`, `contradicts`, `enables`, `example`). Every link must point to a real file.

**Filenames** are lowercase, hyphenated, `.md`, derived from `# Title`, max 100 chars.

**Distillation tracking**: when distilling from notes into a focused artifact, add `Distilled into:` in each source note's footer. The distilled artifact does not link back.

**Renames**: never rename manually. Use `commonplace-relocate-note` to update backlinks.
