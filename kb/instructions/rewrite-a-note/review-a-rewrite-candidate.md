---
description: "Use for the headless worker of the review steps of `commonplace-review run rewrite`: decide whether the exact candidate bytes of a rewritten note may be published"
type: types/instruction.md
---

# Review a rewrite candidate

Goal: the candidate reaches the operator's publication stop only when an
independent reviewer finds that these exact bytes make the commissioned
contribution on the evidence, within the contracts.

Consumption: the rewrite workflow (`commonplace-review run rewrite`) gives
this file to a fresh headless worker as its `instruction` input, in the
`review` step and, after one repair, in the `review-repair` step. The prompt
names the other inputs, the candidate's SHA-256 and the output file.
Nothing else is inherited.

## Inputs

- `candidate`: the exact text to judge. The prompt gives its SHA-256.
- `candidate-report`: the author's report of what it kept, replaced and
  omitted from the existing note.
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
- `reconstruction`: the source-faithful basis.
- `claim-account`: how the note was to treat each commitment of the
  reconstruction.
- `note`: the note's text when the run started.
- `type-contract` and `collection-contract`, when present: the contracts the
  note must meet.

## What you must not do

- Do not edit the candidate or any file. Write nothing except the output
  file.
- Do not choose the repair. Say what must change; the author changes it.
- Do not read the note's file in the checkout, earlier runs or earlier
  reviews. Judge the inputs.

## Procedure

Check, in this order:

1. The delta from `note` to `candidate` against the claim account and the
   report: every material commitment of the existing note is kept, replaced
   or omitted with a reason, and no commitment appears that the claim
   account does not give.
2. The commission and the brief: the intended contribution, what must be
   kept and excluded, and no reserved decision taken.
3. The contracts: the type and the collection.
4. Evidence: each claim has the support or the inference the reconstruction
   gives, with its scope and qualifiers.
5. Specificity, relevance and prose.

A finding blocks when the candidate cannot be published without the change.
A finding about missing evidence says that the sources lack it; the session
agent then grounds or adds a source and starts again.

## Output

Write the review as Markdown:

1. YAML frontmatter holding `candidate-sha256:` with the hash the prompt
   gives. Code refuses a review that names another hash.
2. Each finding as a `## ` section with the lines `Anchor:` (the passage or
   heading of the candidate), `Basis:` (the input and passage that show the
   problem) and `Required change:` (the change the candidate needs). Code
   checks each label. Use `## ` headings for findings only.
3. A last line holding only `accept` or `block`. A `block` review has at
   least one finding. An `accept` review may hold findings that do not
   block.
