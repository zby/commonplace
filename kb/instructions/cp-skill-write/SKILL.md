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

All documents in the KB live in a **collection**: a directory under `kb/` with a local `COLLECTION.md`, such as `kb/notes/`, `kb/reference/`, `kb/instructions/`, or an installed library collection like `kb/commonplace/notes/`. Each collection that accepts writes has a `COLLECTION.md` with its register, quality goal, type offerings, and linking conventions. Nested `COLLECTION.md` files inside an existing collection are outside the current collection model.

Documents with frontmatter carry a path-valued `type:` that points to a type-spec doc, for example `type: kb/types/note.md` or `type: kb/reference/types/adr.md`. Files with no frontmatter are implicit `text`.

### Step 1 - Parse Arguments

**Edit mode**: first argument is a path to an existing `.md` file. Read it, infer collection from the path, and read its `type:` path from frontmatter. If it has frontmatter but no `type:`, stop and fix that structural problem before editing. If it has no frontmatter, treat it as implicit `text`. Open the type-spec doc named by `type:` before making structural edits.

**New-write mode**: everything else. Extract collection, type, and topic from the arguments. Defaults: collection `notes`, type `kb/types/note.md`. If the requested type is an instruction and no collection is explicit, use collection `instructions`.

For new writes, resolve the target collection to a directory under `kb/` with a local `COLLECTION.md`; shorthand names such as `notes` mean `kb/notes/`. Read that collection's `## Types` section and pick one listed type path. If the requested type is not listed and the user did not give an explicit path, stop and list the available types. If the user gives an explicit `kb/.../*.md` type path, open that file and verify it is a type-spec doc before using it.

### Step 2 - Load Collection Conventions

Read the target collection's `COLLECTION.md` for the collection's writing conventions, including outbound-linking rules. Find the outbound-linking section (heading varies — look for the one that names destinations and labels) and treat it as authoritative. It tells you which destination collections this source may link to, which destinations are excluded, which labels are authorised for which source->destination pairs, and the reader-need each label serves. Internal format varies (per-destination blocks, a single labels table with a destinations column, prose) — read it for content, not shape. There is no separate linking doc to consult.

**Hard fail** if the target collection has no `COLLECTION.md`. Every collection that accepts writes must have a `COLLECTION.md`; its register, quality goal, and linking rules are what distinguish collections. Do not proceed with default conventions.

### Step 3 - Load The Type Spec

Read the selected type-spec doc. Its frontmatter must include `type: kb/types/type-spec.md`, `name`, `description`, and `schema`. Its body supplies the artifact shape and may include a template block. Follow that body as the structural authoring contract.

Do not use legacy split type sidecars. Do not fall back from a missing type path to `note`.

For `text`, write raw markdown with no frontmatter only when the user explicitly wants unstructured capture. Otherwise use `kb/types/note.md`.

### Step 4 - Search Before Writing

Unless the user requests otherwise, the write flow does not run active discovery. Link candidates come from three cheap sources, in order:

1. **Destination `dir-index.md`.** For each destination collection authorised by the source `COLLECTION.md`'s outbound section, read that destination's `dir-index.md` once. Titles and descriptions are the full surface — enough to catch near-duplicates in the target collection and enough to surface obvious connection points in other destinations. Do not open candidate notes to inspect their bodies unless the dir-index line itself is a match.
2. **Context already loaded.** Notes, sources, and ingests that were pulled into the session for this write are first-class candidates. If it was worth reading, it is worth considering as a link.
3. **User-named targets.** Link targets the user mentions in the prompt.

In edit mode, also run a backlinks lookup on the target note — one query, no body search — so edits don't orphan dependents.

Active prospecting (body search, tag traversal, link-following, reverse-edge reasoning) belongs to `cp-skill-connect`, not here.

### Step 5 - Draft And Save

Follow the type-spec doc and collection conventions. Derive a lowercase-hyphenated filename from `# Title` unless editing an existing file. For typed artifacts, set `type:` to the exact repo-relative type-spec path, not the type name.

Set traits only when clearly warranted: `title-as-claim`, `definition`, `has-comparison`, `has-external-sources`, `has-implementation`.

Preserve existing frontmatter and links during edits unless the requested change requires changing them.

### Step 6 - Validate

Run targeted validation on the written or edited artifact, not the whole KB:

```bash
commonplace-validate path/to/written-file.md
```

If the task wrote or edited multiple KB artifacts, validate each explicit path or the smallest containing directory that covers only those artifacts. Bare `commonplace-validate kb` and `commonplace-validate all` are rejected — scope must be a specific collection or file. Fix structural failures in the touched artifacts before stopping.

Then suggest `cp-skill-connect` as the next step. Step 4 commits links the author already had reason to believe in (dir-index, loaded context, user-named); the rest of the note's share of the graph — body-search candidates, tag-traversal hits, link-following, reverse-edge candidates from other collections — only surfaces under the connect skill. The suggestion is not optional polish.

## Universal Mechanics

These apply to all typed artifacts regardless of collection.

**Frontmatter** makes notes queryable. No frontmatter means implicit `text`; any file with frontmatter must include a path-valued `type:`. Most library notes also need `description` (double-quoted, 50-200 chars), plus optional `traits`, `tags`, and `status`.

**Descriptions** are retrieval filters, not summaries. The test: if an agent searched for this note's concept and got 5 results, would this description help pick this one? Paraphrasing the title adds zero retrieval value.

**Vocabulary.** Use the active vocabulary declared in root `AGENTS.md`. When writing or materially editing prose, gloss and link active vocabulary on first meaningful mention when the reader may not know the term. Do not churn untouched passages only to add vocabulary links.

**Links.** Use relative markdown paths from the source file. Every link must point to a real file.

Position encodes commitment. **Inline** prose connectors (`since [X](./x.md)`, `because [X](./x.md)`, `but [X](./x.md)`) are strongest — the target is a premise of the current argument. **Footer** links carry an explicit label and context phrase: `- [title](./path.md) — label: context phrase`.

The collection's `COLLECTION.md` authorises labels per destination and names the reader-need each label serves. Pick a label whose reader-need matches the link's purpose; write the context phrase to answer *"[source] connects to [target] because [specific reason]."* If no authorised label fits, the candidate is off-scope for this collection — drop the link or raise it to the collection author to extend the authorisation.

**Filenames** are lowercase, hyphenated, `.md`, derived from `# Title`, max 70 chars.

**Distillation tracking**: when distilling from notes into a focused artifact, add `Distilled into:` in each source note's footer. The distilled artifact does not link back.

**Renames**: never rename manually. Use `commonplace-relocate-note` to update backlinks.
