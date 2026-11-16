---
description: "Use for the headless worker of the claim-account step of `commonplace-review run rewrite`: decide how the rewritten note treats each commitment of the reconstruction, before seeing the note"
type: types/instruction.md
---

# Account for the claims of a rewrite

Goal: the claim selection of the rewrite is fixed from the evidence before
anyone sees the existing note, so that the note cannot lend warrant to its
own claims.

Consumption: the rewrite workflow (`commonplace-review run rewrite`) gives
this file to a fresh headless worker as its `instruction` input. The prompt
names the other inputs and the output file. Nothing else is inherited.

The workflow freezes your claim account. A later fresh worker writes the
candidate from it. So the account carries the judgment of what the note
claims; write it so that another writer can follow it.

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
- `reconstruction`: the source-faithful basis. It separates support from
  inference and names conflicts, scope and gaps.
- `type-contract` and `collection-contract`, when present: the contracts the
  note must meet.

## What you must not do

- Do not read the note, its write brief file, its earlier texts in git
  history or under `kb/reports/`, or any file that quotes it.
- Read no repository file. The inputs are the whole evidence for this step.
- Do not add a commitment the reconstruction does not support or infer.
- Do not make a decision the commission reserves for the operator. Name it
  as reserved instead.
- Do not write the note's prose. Write nothing except the output file.

## Procedure

1. If the commission and the brief contradict each other, write the problem
   file and name both passages.
2. List the material commitments of the reconstruction: each claim,
   definition or distinction the contribution could rest on.
3. For each, decide its treatment: state it, state it with a qualifier,
   state it as inference, leave it out, or leave it to the operator. Give
   the basis in the reconstruction, the scope and qualifiers it needs, what
   it depends on, and where it goes in the note.
4. Say what the note must not claim because the reconstruction names it as a
   gap or a conflict.

## Output

Write the claim account as Markdown with one `## ` section per material
commitment. Code checks that there is at least one such section. Each
section names the commitment, its treatment, its basis, its scope and
qualifiers, its dependencies and its destination in the note. You may end
with a section of commitments the note must not make.
