---
name: cp-skill-write
description: Write one KB note whose intended contribution is already determined, under its collection and type contracts; validate it and hand broader graph discovery to cp-skill-connect.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[path | collection | type] [topic or claim/purpose] — a note path for editing, or a collection/type/subject for new notes"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

All documents in the KB live in a **collection**: a directory under `kb/` with a local `COLLECTION.md`, such as `kb/notes/`, `kb/reference/`, `kb/instructions/`, or an installed library collection like `kb/commonplace/notes/`. Each collection that accepts writes has a `COLLECTION.md` with its purpose, intended contribution, quality goal, and linking conventions.

Documents with frontmatter carry a path-valued `type:` that points to a type-spec doc, for example `type: kb/types/note.md` or `type: kb/reference/types/adr.md`. Files with no frontmatter are implicit `text`.

### Step 1 - Parse Arguments

**Edit mode**: first argument is a path to an existing `.md` file. Read it, infer collection from the path, and read its `type:` path from frontmatter. If it has frontmatter but no `type:`, stop and fix that structural problem before editing. If it has no frontmatter, treat it as implicit `text`. Open the type-spec doc named by `type:` before making structural edits.

**New-write mode**: everything else. Extract collection, type, and topic from the arguments. Default an unspecified collection to `notes` and an unspecified type to `kb/types/note.md`. If the requested type is an instruction and no collection is explicit, use collection `instructions`.

For new writes, resolve the target collection to a directory under `kb/` with a local `COLLECTION.md`; shorthand names such as `notes` mean `kb/notes/`. Resolve the type independently of the collection contract:

- If the user or calling workflow supplied a type path, open it and verify that its own frontmatter identifies it as a type-spec doc.
- If the user supplied a shorthand type name, search Markdown files under `kb/types/` and every collection `types/` directory below `kb/`. Inspect each candidate's own opening frontmatter and require exactly one type-spec doc whose `name:` equals the shorthand. If none or several match, stop and report the matching paths; do not guess or apply collection-specific precedence.
- If no type was supplied, use `kb/types/note.md`.

This lookup identifies the contract; it does not authorize the type for the target collection. Do not add collection-specific eligibility logic or a `kb/work/` branch. `commonplace-validate` owns that decision. An explicit request for `text` means frontmatter-free Markdown, not a `type:` pointer.

### Step 2 - Load Collection Conventions

Read the target collection's `COLLECTION.md` for the collection's writing conventions, including outbound-linking rules. Find the outbound-linking section (heading varies — look for the one that names destinations and labels) and treat it as authoritative. It tells you which local collections this source may link to, whether the reserved `external` destination is authorized, which destinations are excluded, which labels are authorised for which source->destination pairs, and the reader-need each label serves. The destination wildcard `any` includes `external`. Internal format varies (per-destination blocks, a single labels table with a destinations column, prose) — read it for content, not shape. There is no separate linking doc to consult.

**Hard fail** if the target collection has no `COLLECTION.md`. Every collection that accepts writes must have a `COLLECTION.md`; its purpose, intended contribution, quality goal, and linking rules are what distinguish collections. Do not proceed with default conventions.

### Step 3 - Load The Type Spec

Read the selected type-spec doc. Its frontmatter must include `type: kb/types/type-spec.md`, `name`, `description`, and `schema`. Its body supplies the artifact shape and may include a template block. Follow that body as the structural authoring contract.

Do not fall back from a missing type path to `note`.

For `text`, write raw markdown with no frontmatter only when the user explicitly wants unstructured capture. Otherwise use `kb/types/note.md`.

### Step 4 - Resolve The Intended Contribution

Before drafting, identify from the user's request and the target artifact in edit mode:

- the intended audience, using the collection default when the task does not narrow it;
- the governing question, target claim, or practical purpose;
- what the reader should understand, infer, or do because this artifact exists; and
- any scope or angle needed to distinguish it from materially different artifacts on the same topic.

The repository and collection contracts constrain the acceptable contribution class, quality bar, and often the default audience. They do not by themselves select an artifact-specific claim or purpose. Resolve that choice from the task, the incumbent artifact, and any retained intent supplied for this write. Treat a context block as retained intent only when it identifies its source, subject, scope, and whether its role is authoritative or advisory. Current user direction prevails. If retained intent conflicts with the incumbent or another applicable input and no explicit precedence resolves the conflict, ask the user rather than silently amending the commission.

Remembered intent may complete a bare request, but it is not meaning contained in that request, a choice licensed by model priors, or evidence that warrants factual claims. Do not add an ad hoc history search to this skill; older interaction history counts only when a memory mechanism supplies it through the retained-intent input.

When those inputs already determine the choices, proceed without a formal brief. If several materially different contributions still fit, treat that as a specification gap rather than something a stronger model should guess: ask one focused question, or use an exploratory workshop when determining the contribution is itself the work. When the contribution is determined but its claims still need substantial grounding or synthesis, stop and explain why the ordinary path is insufficient. Ask whether the user wants to continue with `cp-skill-write-multistage`, and invoke it only after explicit confirmation.

### Step 5 - Search Before Writing

Write does not run active discovery — that is `cp-skill-connect`'s job. Write authors one note and commits only links the author already has in hand, plus a cheap duplicate guard:

This guard is intra-KB only. Do not search the external literature for missing
prior art and do not infer novelty from the absence of a named source. If the
user explicitly asks whether an artifact duplicates, restates, or is subsumed
by external literature, or asks for an artifact disposition on that basis,
invoke `cp-skill-write-multistage` with the same target and request. That
explicit request supplies the confirmation required by Step 4; do not ask the
user to authorize the handoff again. The multistage skill loads the specialised
literature-disposition procedure.

1. **Near-duplicate check.** Search the target collection for the new note's distinctive title terms with `rg` (e.g. `rg -i "key term" kb/notes/ --glob "*.md"`). This is a targeted term search — do **not** enumerate the whole collection; a complete listing costs linear context and is the wrong tool for a single note's duplicate check. If a near-duplicate already exists, prefer editing it to creating a second note.
2. **Context already loaded.** Notes, sources, and ingests pulled into the session for this write are first-class link candidates. If it was worth reading, it is worth considering as a link.
3. **User-named targets.** Link targets the user mentions in the prompt.

In edit mode, also run a backlinks lookup on the target note — one query, no body search — so edits don't orphan dependents.

All discovery beyond this — collection-wide description scans, cross-destination prospecting, body search, tag traversal, link-following, reverse-edge reasoning — belongs to `cp-skill-connect`, not here. Write stays focused on authoring one note.

### Step 6 - Draft The Candidate

Follow the type-spec doc and collection conventions. Derive a lowercase-hyphenated filename from `# Title` unless editing an existing file. For typed artifacts, set `type:` to the exact repo-relative type-spec path, not the type name.

Set traits only when clearly warranted. The available traits and their meanings are defined in the target type's spec (e.g. the traits table in `kb/types/note.md`) — take the vocabulary from there, not from a remembered list.

Preserve existing frontmatter and links during edits unless the requested change requires changing them.

For a substantive edit, remove `user-verified` from the candidate. Verification
attests to the prior substantive contents and must be granted again explicitly
by a human. Preserve it only when the user has explicitly authorized a
mechanical trivial-change workflow.

Draft the complete candidate in working context without creating or changing
the target file. The source-dependency guard in Step 7 must finish before the
first durable target write.

### Step 7 - Guard Named Source Dependencies

Inspect the candidate for every addition or material change that depends on a
named external source, regardless of the target collection. The guard applies
when, for example:

- the user or brief names a source, URL, or ingest as support;
- the candidate adds or materially changes an attribution, quotation,
  empirical result, or borrowed mechanism tied to a named source; or
- a review finding asks for exact claim/source grounding.

A passing mention or adjacent example that the candidate does not use as
support is not a source dependency. In edit mode, compare against the incumbent
and do not retrigger the guard for unchanged source-dependent wording.

For each guarded dependency, resolve exactly one direct tracked
`kb/sources/<slug>.ingest.md` from the supplied ingest, canonical source URL, or
unambiguous source identity. Read its complete Quotes section and the
`semantic/grounding-alignment` gate from the installed framework gate catalog.

- When the retained verbatim quotes contain enough source material for the
  gate to judge the candidate's use, apply the gate directly to that use. Link
  the ingest without a snapshot marker and keep target-specific transfer
  reasoning in the target. Ignore every ingest section outside Quotes as source
  support.
- Use the snapshot route only when an earlier grounding run returned `snapshot
  required`. Put the exact marker `(snapshot required)` in the ingest link
  text. Derive the exact name-paired snapshot, require its exact-byte SHA-256
  and canonical source to match the ingest, read it, and apply the same gate to
  the candidate's use. Stop if the snapshot is absent, mismatched, or does not
  support the use.
- Otherwise, if Quotes is insufficient and the ingest exists, invoke
  `cp-skill-ground` with `Target: <ingest path>` and `Claim needed: <the
  source-side proposition or question>`, then act on its route: `quotes
  sufficient` or `quotes added` — re-read the Quotes section and apply the gate
  as in the first bullet; `snapshot required` — take the snapshot route above;
  a blocker — stop before saving and report it. Record every `quotes added`
  result, with the ingest path, in this skill's final report so the append is
  never a silent side effect of a write.
- If the dependency names a URL with no tracked ingest, stop before saving and
  report the exact URL for a separate `cp-skill-ingest` run; this writer does
  not create source records.

If neither an exact ingest nor a canonical URL can be resolved, stop and ask
for that source identity rather than inventing an input. This writer invokes
the grounding skill but never edits an ingest itself, never creates one, and
introduces no separate result protocol. It reads a source snapshot only for a
declared `snapshot required` dependency.

### Step 8 - Save

Only after Step 7 passes, write the complete candidate to the resolved target
path. This is the first durable target write.

### Step 9 - Validate

Validate the note you wrote or edited:

```bash
commonplace-validate path/to/file.md
```

Fix structural failures before stopping.

Then suggest `cp-skill-connect` as the next step. Step 5 commits only links the author already had in hand (loaded context, user-named) plus a duplicate guard; the rest of the note's share of the graph — collection-wide description scans, cross-destination candidates, body-search hits, tag-traversal, link-following, reverse-edge candidates — only surfaces under the connect skill. The suggestion is not optional polish.

## Universal Mechanics

These apply to all typed artifacts regardless of collection.

**Frontmatter** makes notes queryable. No frontmatter means implicit `text`; any file with frontmatter must include a path-valued `type:`. Most library notes also need `description` (double-quoted, 50-250 chars), plus optional `traits`, `tags`, and `user-verified`. Never grant user verification implicitly.

**Descriptions** are retrieval filters, not summaries. The test: if an agent searched for this note's concept and got 5 results, would this description help pick this one? Paraphrasing the title adds zero retrieval value.

**Vocabulary.** Use the active vocabulary declared in root `AGENTS.md`. When writing or materially editing prose, gloss and link active vocabulary on first meaningful mention when the reader may not know the term. Do not churn untouched passages only to add vocabulary links. Keep one term for one concept through the artifact: do not vary a word for variety, because in technical prose a changed word reads as a changed referent.

**Links.** Use relative markdown paths from the source file. Every link must point to a real file.

Position encodes commitment. **Inline** prose connectors (`since [X](./x.md)`, `because [X](./x.md)`, `but [X](./x.md)`) are strongest — the target is a premise of the current argument. **Footer** links carry an explicit label and context phrase: `- [title](./path.md) — label: context phrase`.

The collection's `COLLECTION.md` authorises labels per destination and names the reader-need each label serves. Pick a label whose reader-need matches the link's purpose; write the context phrase to answer *"[source] connects to [target] because [specific reason]."* If no authorised label fits, the candidate is off-scope for this collection — drop the link or raise it to the collection author to extend the authorisation.

**Filenames** are lowercase, hyphenated, `.md`, derived from `# Title`, max 70 chars.

**Lineage tracking**: when a focused artifact is worked up from a source, record the dependency in the source's footer — `Derived into:`, `Abstracted into:`, `Operationalized into:`, or `Adapted into:`, whichever the source collection authorizes and [link-vocabulary.md](../../reference/link-vocabulary.md)'s test fits; never stack more than one for the same edge. The produced artifact does not link back.

**Renames**: never rename manually. Use `commonplace-relocate-note` to update backlinks.
