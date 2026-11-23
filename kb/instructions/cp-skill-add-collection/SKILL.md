---
name: cp-skill-add-collection
description: Add one new collection under kb/ with its binding COLLECTION.md, landing README, tag participation and routing, then validate it. Use when a project needs a new kind of long-lived content that no existing collection's contract fits.
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

# Add a collection

Goal: a new directory `kb/<name>/` whose `COLLECTION.md` binds every artifact
written there, which agents can find through the project's routing, and which
passes validation.

## Inputs

- **Name**: lowercase letters, digits and hyphens, used as `kb/<name>/`.
- **Purpose**: what contribution the collection holds and for which reader.
- **Model contract** (optional): an existing `COLLECTION.md` to model it on,
  in this project or supplied as a file.

Ask for the name or purpose if either is missing. Do not invent a purpose
from the name.

## 1. Check that a collection is the right answer

Stop and report instead of creating anything when:

- the content is in-flight work whose value is consumed when it finishes: it
  belongs in a workshop, `kb/work/<name>/`;
- an existing collection's contract already covers the contribution: write
  there, or propose a subdirectory of it;
- `kb/<name>/` already exists;
- the name is `tags`, `sources`, `reports`, `workflow-state`, `work`, `types` or
  `agentic-system-analyses`. Commonplace commands rely on those locations
  for system roles, so the name is not available for ordinary content.

## 2. Write `kb/<name>/COLLECTION.md`

Read the project's KB goals in `AGENTS.md` and the
[collection-contract type](../../types/collection-contract.md) first. Then
read the contract the caller named, or look for a `kb/*/COLLECTION.md` in the
project that fits the new purpose. If none fits, list the installed starting
contracts with `ls "$(commonplace-source)"/_data/templates/user-*-COLLECTION.md`.
Adapt a suitable contract, or draft one directly. The project owns the new
file; later changes to a template do not update the copy.

Frontmatter:

```yaml
---
type: types/collection-contract.md
description: "<what the collection holds, for agents choosing where to read or write>"
---
```

Add `unquoted-source-limit: <n>` only when the collection's artifacts will
be held to a one-pass grounding review against tracked sources; validation
then fails any artifact citing more than `<n>` tracked sources without a
verified verbatim quotation. If you set it, read
[the unquoted-source limit](../../reference/validation-contract.md#the-unquoted-source-limit)
for what counts and how authors discharge a source, and state those
conventions in the contract body.

The body must cover the contract's three roles. Derive each from the stated
purpose and the project's goals; do not add requirements nobody asked for.

1. **Goals**: what belongs here, its scope, and which existing collection
   takes nearby content instead.
2. **Quality standards**: the quality goal and its tests, title and
   description conventions, and any attribution or evidence requirements.
3. **Linking.** In the "Outbound links" section, name the permitted destinations.
   For formal links, list each label and the reader need it serves for that
   destination. Consult the [label catalogue](../../reference/link-vocabulary.md#label-catalogue) before naming a formal relation. Use a listed name only for its defined meaning and direction. If none fits, define a local label under an unreserved name. In either case, authorise the label for the intended destination in the new contract.
   To authorise inline citations to `external`, state their permitted purpose
   and where they may appear. These citations need no formal label.

Do not restate which types the collection may use; validation enforces that
for every collection. Create `kb/<name>/types/` only when a local type is
needed now; its artifacts then name it `type: <name>/types/<type>.md`.

## 3. Write the landing

Create `kb/<name>/README.md`: a heading, one sentence saying what the
collection holds, a link to `COLLECTION.md`, and "No artifacts have been
added yet." Do not create `index.md`; a collection may have only one landing.

## 4. Connect it to the rest of the KB

1. **Tags.** If its artifacts will carry `tags:`, add `<name>` to the
   `participating:` list in `kb/tags/COLLECTION.md`'s frontmatter. Change
   nothing else in that file. Skip this when the collection will not be
   tagged.
2. **Routing.** Add a row for `kb/<name>/` to the collection table in
   `AGENTS.md`, stating its contribution in the same style as the other rows.
   If the project has a content-routing document, add the collection there
   too.
3. **Neighbouring contracts.** Where another collection's contract routes the
   new kind of content elsewhere ("belongs in …"), or should be able to link
   to it, propose the edit to the user rather than making it. Those contracts
   bind other artifacts.

## 5. Validate

```bash
commonplace-validate <name>
commonplace-validate landings
commonplace-validate tags        # only if participating changed
```

Fix failures in the files you wrote. Report any failure in files you did not
touch without fixing it.

Do not stage or commit unless asked.

## Report

State the new path, the contract you modelled on, whether it participates in
tags, the routing rows you added, the validation results, and any proposed
edits to neighbouring contracts.
