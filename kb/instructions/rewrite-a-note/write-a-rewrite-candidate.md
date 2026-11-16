---
description: "Use for the headless worker of the candidate and candidate-repair steps of `commonplace-review run rewrite`: write the full rewritten note from the frozen claim account and reconcile it with the existing note"
type: types/instruction.md
---

# Write a rewrite candidate

Goal: one complete candidate text of the note that makes the commissioned
contribution from the claim account, and a report that accounts for every
material commitment of the existing note.

Consumption: the rewrite workflow (`commonplace-review run rewrite`) gives
this file to a fresh headless worker as its `instruction` input, in the
`candidate` step and, after a blocking review, in the `candidate-repair`
step. The prompt names the other inputs and the two output files. Nothing
else is inherited.

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
- `reconstruction`: the source-faithful basis.
- `claim-account`: how the note treats each commitment of the
  reconstruction. It is frozen. Follow it.
- `note`: the note's text when the run started. It is a reconciliation
  input. It supplies no warrant for its own claims.
- `type-contract` and `collection-contract`, when present: the contracts the
  note must meet.
- `kb-role`, when present: the `## Role` section of the note's role report.
  It says what the note is for in the KB and which of its terms and claims
  other notes rely on.
- `earlier-decisions`, when present: the operator's decisions in earlier
  revise and rewrite runs on this note. Each entry gives the passage, the
  change or finding, the decision and the operator's reason.
- In the `candidate-repair` step also `review`, the review that blocked the
  earlier candidate, and `blocked-candidate`, that candidate.

## What you must not do

- Do not add a material commitment the claim account does not give. If the
  note needs one, write the problem file and name it.
- Do not make a decision the commission reserves for the operator. If the
  candidate cannot be written without one, write the problem file and name
  the decision.
- Do not rename, redefine or drop a term or claim that `kb-role` lists as
  relied on, unless the commission's current direction explicitly asks for
  it. When it does, say so in the report. If the claim account leaves out
  such a claim and the current direction does not ask for that, write the
  problem file and name the claim and the dependents. A term or claim
  `kb-role` lists as unused is not for that reason a candidate for cutting.
- Do not reintroduce a change the operator rejected in `earlier-decisions`,
  and keep a wording the operator approved there, unless the commission's
  current direction says otherwise.
- Do not change the frontmatter `title`, `type` or `brief` declaration, or
  the H1. A retitle is not part of this workflow.
- Do not edit the note's file, its brief, the sources or any other file.
  Write nothing except the two output files.

## Procedure

1. If the commission and the brief contradict each other, write the problem
   file and name both passages.
2. Write the candidate from the claim account. Choose the order,
   decomposition, examples and wording within the commission, the brief and
   the contracts.
3. Keep the existing note's valid frontmatter and links unless the claim
   account or the commission requires otherwise. Resolve each link from the
   note's path. Remove `user-verified` when the body changes.
4. Reconcile the existing note: for each of its material commitments, say
   whether the candidate keeps it, replaces it or omits it, and why.
5. In the `candidate-repair` step, make the change each finding of the
   review requires. Change nothing a finding does not require, except what
   the change itself forces. If a finding asks for evidence the sources do
   not give, or for an operator decision, write the problem file and name
   the finding.

## Output

- The candidate: the complete text of the note, frontmatter included.
  Code checks that the frontmatter parses, keeps `title`, `type` and the
  `brief` declaration, that the H1 is unchanged, that `user-verified` is gone
  when the body changed, and that validation finds no new failure. In the
  repair step code also checks that the candidate differs from the blocked
  one.
- The report, Markdown with the sections `## Kept`, `## Replaced` and
  `## Omitted`. Code checks that each heading is present. Each entry names a
  material commitment of the existing note and the reason. Write `None.` in
  a section with nothing in it. You may add other sections.
