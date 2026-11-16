---
description: "Use as the criterion of the review operation of `commonplace-review run rewrite`: decide whether the exact candidate text of a rewritten note may be published, as a typed review result"
type: types/instruction.md
---

# Review a rewrite candidate

Goal: the candidate reaches the operator's publication stop only when an
independent reviewer finds that this exact text makes the commissioned
contribution on the evidence, within the contracts. The findings that do not
block reach the operator before publication and can be triaged after it.

Consumption: the rewrite workflow (`commonplace-review run rewrite`) runs a
review operation with this file as its criterion, in the `review` step and,
after one repair, in the `review-repair` step. A fresh headless worker
receives this file as the criterion, the candidate as the note's text, and the
other inputs below as operational inputs. The prompt names the inputs, the
review-result contract and the output file. Nothing else is inherited.

## Inputs

- The note's text input: the candidate, the exact text to judge. It is not
  the note's current file.
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
- `start`: the note's text when the run started.
- `type-contract` and `collection-contract`, when present: the contracts the
  note must meet.
- `kb-role`, when present: the `## Role` section of the note's role report.
  It says which of the note's terms and claims other notes rely on.
- `earlier-decisions`, when present: the operator's decisions in earlier
  revise and rewrite runs on this note, with the operator's reasons.
- `finding-decisions`, when present: the findings of earlier reviews of this
  note against this instruction that the operator rejected, with the rule
  for raising one again.

## What you must not do

- Do not edit the candidate or any file. Write nothing except the output
  file.
- Do not choose the repair. Say what must change; the author changes it.
- Do not read the note's file in the checkout, earlier runs or earlier
  reviews. Judge the inputs.

## Procedure

Check, in this order:

1. The delta from `start` to the candidate against the claim account and
   the report: every material commitment of the existing note is kept,
   replaced or omitted with a reason, and no commitment appears that the
   claim account does not give.
2. The commission and the brief: the intended contribution, what must be
   kept and excluded, and no reserved decision taken.
3. The note's dependents and the operator's earlier decisions. Report as a
   finding a term or claim `kb-role` lists as relied on that the candidate
   renames, redefines or drops, unless the commission's current direction
   asks for it and the report says so. Report as a finding a candidate that
   reintroduces a change the operator rejected in `earlier-decisions`, or
   drops a wording the operator approved there, unless the commission's
   current direction says otherwise. Content `kb-role` lists as unused is
   not for that reason a finding.
4. The contracts: the type and the collection.
5. Evidence: each claim has the support or the inference the reconstruction
   gives, with its scope and qualifiers.
6. Specificity, relevance and prose.

A finding blocks when the candidate cannot be published without the change.
A finding about missing evidence says that the sources lack it; the session
agent then grounds or adds a source and starts again.

## Output

Write a review result as the supplied review-result contract defines it:

1. Each finding has `scope`, `quotes`, `reason` and `level`.
   - `scope: passage` with `quotes` holding the passage of the candidate the
     finding anchors to, verbatim and occurring once. Use `scope: document`
     with empty `quotes` for an absence, such as a dropped commitment.
   - `reason` states `Basis:`, the input and passage that show the problem,
     and then `Required change:`, the change the candidate needs.
   - `level: fail` for a finding that blocks; `level: warn` for one that
     asks for a change but does not block; `level: info` for a remark that
     asks for no change.
2. `outcome: fail` when any finding has level `fail`: the candidate is
   blocked. Otherwise `outcome: warn` when a finding has level `warn`, and
   `outcome: pass` when no finding asks for a change. Code refuses an
   outcome that does not match the levels, and a `warn` or `fail` finding
   whose reason lacks `Basis:` or `Required change:`.
3. A `# Review` body that explains the judgment without repeating each
   finding.

Code binds the result to the candidate through its target hash. A `warn`
result reaches the publication stop; the operator hears of its findings
before deciding. When the operator publishes this exact candidate, the result
becomes the note's current result, and a triage presents its `warn` findings.
