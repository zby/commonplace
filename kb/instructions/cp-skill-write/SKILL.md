---
name: cp-skill-write
description: Write a single KB note — apply the target collection's conventions and path-valued type-spec, commit only in-hand links plus a cheap duplicate check, validate, then hand graph discovery to cp-skill-connect.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[path | collection | type] [topic] — a note path for editing, or a collection/type/topic for new notes"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

All documents in the KB live in a **collection**: a directory under `kb/` with a local `COLLECTION.md`, such as `kb/notes/`, `kb/reference/`, `kb/instructions/`, or an installed library collection like `kb/commonplace/notes/`. Each collection that accepts writes has a `COLLECTION.md` with its register, quality goal, type offerings, and linking conventions.

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

Do not fall back from a missing type path to `note`.

For `text`, write raw markdown with no frontmatter only when the user explicitly wants unstructured capture. Otherwise use `kb/types/note.md`.

### Step 4 - Search Before Writing

Write does not run active discovery — that is `cp-skill-connect`'s job. Write authors one note and commits only links the author already has in hand, plus a cheap duplicate guard:

1. **Near-duplicate check.** Search the target collection for the new note's distinctive title terms with `rg` (e.g. `rg -i "key term" kb/notes/ --glob "*.md"`). This is a targeted term search — do **not** enumerate the whole collection; a complete listing costs linear context and is the wrong tool for a single note's duplicate check. If a near-duplicate already exists, prefer editing it to creating a second note.
2. **Context already loaded.** Notes, sources, and ingests pulled into the session for this write are first-class link candidates. If it was worth reading, it is worth considering as a link.
3. **User-named targets.** Link targets the user mentions in the prompt.

In edit mode, also run a backlinks lookup on the target note — one query, no body search — so edits don't orphan dependents.

All discovery beyond this — collection-wide description scans, cross-destination prospecting, body search, tag traversal, link-following, reverse-edge reasoning — belongs to `cp-skill-connect`, not here. Write stays focused on authoring one note.

### Step 5 - Draft And Save

Follow the type-spec doc and collection conventions. Derive a lowercase-hyphenated filename from `# Title` unless editing an existing file. For typed artifacts, set `type:` to the exact repo-relative type-spec path, not the type name.

Set traits only when clearly warranted. The available traits and their meanings are defined in the target type's spec (e.g. the traits table in `kb/types/note.md`) — take the vocabulary from there, not from a remembered list.

Preserve existing frontmatter and links during edits unless the requested change requires changing them.

### Step 6 - Validate

Validate the note you wrote or edited:

```bash
commonplace-validate path/to/file.md
```

Fix structural failures before stopping.

Then suggest `cp-skill-connect` as the next step. Step 4 commits only links the author already had in hand (loaded context, user-named) plus a duplicate guard; the rest of the note's share of the graph — collection-wide description scans, cross-destination candidates, body-search hits, tag-traversal, link-following, reverse-edge candidates — only surfaces under the connect skill. The suggestion is not optional polish.

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
