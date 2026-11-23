# Experiment 5: elaborated demotions

Designed 2026-11-22 by an agent (claude-fable-5-2), before any run.

## The question

**If a procedure names the candidates and a worker writes each one out as a
whole draft, do choosers select the ones the operator ruled?**

Two results on the draft at `13a1803f6` point in opposite directions.

- In [experiment 3](./experiment-3-results.md), 10 of 12 workers chose the
  operator's worked-out two-condition draft over the three-condition draft.
- In [experiment 4](./experiment-4-results.md), 7 of 7 workers rejected a
  one-sentence proposal to make the same change. They also rejected the
  other two enumerated demotions, 21 verdicts of 21.

One reading is that selection needs a worked-out candidate. Another is that
choosers prefer whichever draft is newer or more developed, whatever it
changes. This experiment separates them. A worker writes out each
enumerated demotion without judging it, including the decoy, and choosers
compare each result with the original.

## Setup

Materials at `13a1803f6`: the draft, the checks file and the on-balance
note. Each worker is a headless Opus run with no tools, started in an empty
directory, with the materials pasted into the prompt.

The candidates are those of experiment 4, stated by the same template.

| Candidate | The demotion | What the operator later did |
|---|---|---|
| D1 | "Legible store" becomes a reported property. | Ruled it out of membership in a later session. |
| D2 | "Judgment in the loop" becomes a reported property. | Kept it. |
| D3 | "Open to criticism" becomes a reported property. | Ruled it out of membership at `7568780d3`. |

### Stage E: writing out

Two runs for each candidate, six in all. The worker receives the materials
and one candidate. It is told that the authors have decided to make the
change and that its job is to write the whole revised draft, complete and
consistent, as the authors would publish it. It is told not to judge the
change, not to mark the draft as a proposal, and to output only the draft.

The designing agent reads each revised draft before Stage C and records
whether it makes the change it was given. A draft that does not is kept in
the record and left out of Stage C.

### Stage C: choosing

Four runs for each revised draft, two in each order, 24 in all. The prompt
is the choosing prompt of experiment 3, unchanged: two versions labelled
"Version 1" and "Version 2", the note, and the checks file described as
written for one of the versions. The chooser says which version to adopt
and what to keep from the other.

That is 30 worker runs and one scoring run.

## Scoring

A chooser is graded by the version it names, Version 1 or Version 2, and
the key maps that to the original or the revised draft. Two scorers read
the version named: the designing agent and a fresh Opus run. Neither needs
the key to do so.

## Predictions

Recorded before the runs.

| Candidate | Choosers for the revised draft |
|---|---|
| D1 | 3 of 8 |
| D2 | 1 of 8 |
| D3 | 6 of 8 |

## What each outcome would show

- **D3 chosen, D2 not.** Enumeration followed by writing out supplies the
  candidate that the operator supplied for this ruling, and choosers tell
  it from the decoy.
- **D1 chosen as well.** The procedure also reaches a ruling the operator
  made only in a later session.
- **All three chosen.** Choosers prefer the revised draft whatever it
  changes. Experiment 3's ten of twelve then shows a preference for the
  developed version and not selection of the ruling.
- **None chosen.** A draft written by a worker on instruction is not the
  operator's draft. What made the operator's version win is then something
  in how it was worked out, and the answers should say what.

## Limits

- Two revised drafts for each candidate. The quality of one writer's draft
  can decide a cell.
- The writer is told the change is decided. A draft written without
  conviction may read worse than one written by an author who holds the
  view, and this design cannot tell those apart.
- One decoy, one state, one model.
- The revised drafts will differ in length from the original and from each
  other. Word counts are recorded with the results.
