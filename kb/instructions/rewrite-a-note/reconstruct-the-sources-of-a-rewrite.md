---
description: "Use for the headless worker of the reconstruct step of `commonplace-review run rewrite`: build a source-faithful basis for the commissioned note without seeing the note"
type: types/instruction.md
---

# Reconstruct the sources of a rewrite

Goal: the author of the rewrite gets a basis that says what the authorized
sources support, what is only inferred from them, and where they conflict or
fall short, for the contribution the commission names.

Consumption: the rewrite workflow (`commonplace-review run rewrite`) gives
this file to a fresh headless worker as its `instruction` input. The prompt
names the other inputs and the output file. Nothing else is inherited.

## Inputs

- `commission`: the operator's current direction for this rewrite and the
  sources with their roles. When the note has no write brief, it also states
  the intended contribution and reader update, what to keep and exclude, and
  the decisions reserved for the operator. When the note has a brief, it
  holds only what this rewrite adds to the brief, and it names any brief item
  the operator amended for this rewrite.
- `brief`, when present: the note's write brief. It is binding retained
  intent. Its Intent, Must keep, Must exclude and Reserved decisions hold
  together with the commission's additions. A commission that only adds to
  the brief does not contradict it.
- `sources`: the source list. Each entry gives a path and a role. A captured
  source's text is the input it names, such as `source-1`. A referenced
  source is a repository file you read at its path.
- `type-contract` and `collection-contract`, when present: the contracts the
  note must meet.

## What you must not do

- Do not read the note, its write brief file, its earlier texts in git
  history or under `kb/reports/`, or any file that quotes it. The workflow
  withholds it so that the basis comes from the sources alone.
- Read no repository file except the referenced sources the list names.
- Use no source the list does not name. Do not search the web.
- Do not write the note's claims, outline or prose. The author does that.
- Write nothing except the output file.

## Procedure

1. Read the commission and the brief. If they contradict each other, write
   the problem file and name both passages. Do not resolve the conflict.
2. Read every source for what bears on the intended contribution.
3. Write the reconstruction. For each commitment the contribution needs,
   say what the sources support and where, with the source path and a short
   locator. Keep each source's scope, qualifiers and uncertainty.
4. Keep inference apart from support. An inference names the supported
   points it rests on.
5. Keep conflicts between sources. Do not choose a side unless a source
   settles it.
6. Name the gaps: a commitment the contribution needs that no source
   supports, and a term with no definition in the sources.

## Output

Write the reconstruction as Markdown with these sections. Code checks that
each heading is present. Write `None.` in a section with nothing in it.

- `## Support`: what the sources state, with path and locator.
- `## Inference`: what follows from the support, with what it rests on.
- `## Conflicts`: where sources disagree, with both sides.
- `## Scope`: the conditions and limits under which the support holds.
- `## Gaps`: what the contribution needs and the sources do not give.

You may add other sections.
