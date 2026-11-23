# Experiment 4: enumerated demotions

Designed 2026-11-22 by an agent (claude-fable-5-2), before any run.

## The question

**If a fixed procedure generates the candidates, can a worker select the
ones the operator ruled?**

Experiments 1 and 2 found that workers rarely propose the operator's
ruling: 1 of 64 runs and 1 of 15. Experiment 2 found that they often accept
it when it is shown: 3 of 4. So the missing step is generating the
candidate.

Several of the operator's rulings on this definition are one move. A
condition of membership is taken out and reported as a property that a
learner may or may not have. That move can be applied to every condition
without anyone noticing anything. This experiment generates the candidates
that way and tests the selection.

## Setup

Materials at `13a1803f6`, the state of experiment 2: the draft, the checks
file and the on-balance note, all declared open to change. Each worker is a
headless Opus run with no tools, started in an empty directory, with the
materials pasted into the prompt.

The draft at that state has three numbered conditions. The procedure makes
one candidate for each:

| Candidate | The demotion | What the operator later did |
|---|---|---|
| D1 | "Legible store" becomes a reported property. | Ruled it out of membership in a later session. The adopted definition says a readable store is not required. |
| D2 | "Judgment in the loop" becomes a reported property. | Kept it. The adopted definition requires an evaluation that can reject. |
| D3 | "Open to criticism" becomes a reported property. | Ruled it out of membership at `7568780d3`, row 4 of the replay index. |

Each candidate is stated by one template, with the condition's name filled
in: remove the condition from membership, report it as a property, and
place again the cases that this condition alone put outside. The template
gives no reason for or against.

### Part S: selecting

| Condition | Runs | Task |
|---|---|---|
| S1, one candidate | 3 for each candidate, 9 in all | Adopt or reject this change, with reasons in at most five sentences. |
| S3, all three | 4, the candidates in rotated order | Give a verdict on each change separately. |

### Part G: generating by the procedure

Three runs. The worker receives the materials and the procedure in words:
list every condition of membership, and for each write the change that
demotes it to a reported property. It gives no verdicts. This tests whether
a worker can run the enumeration that the experimenter ran by hand for
Part S.

That is 16 worker runs and one scoring run.

## Scoring

Two blind scorers, the designing agent and a fresh Opus run, grade answers
under shuffled ids before the key is opened.

- **Part S.** Each verdict is graded adopt, reject or unclear. An answer
  that adopts a weakened form, such as keeping a minimal condition, is
  graded reject and the weakened form is noted.
- **Part G.** For each of D1, D2 and D3, whether the list contains it.

The pattern that matches the operator is adopt D1, adopt D3 and reject D2.
A worker that adopts every candidate matches on two of three, and one that
rejects every candidate on one of three. D2 is what separates selection
from agreeing with whatever is offered.

## Predictions

Recorded before the runs.

| Candidate | S1, adopted | S3, adopted |
|---|---|---|
| D1 | 1 of 3 | 1 of 4 |
| D2 | 0 of 3 | 0 of 4 |
| D3 | 2 of 3 | 3 of 4 |

Part G: all three candidates in 3 of 3 lists.

The draft at this state argues at length for the legible store, so D1 is
expected to be defended as the fixed-measure boundary was in experiment 1.

## What each outcome would show

- **D3 adopted, D2 rejected.** Selection works on this ruling once the
  candidate exists, and a procedure can supply the candidate. The
  operator's part at that point could be replaced by the procedure and a
  selecting worker.
- **D1 rejected.** The procedure reaches a ruling that the workers do not
  select. Enumeration then widens the search and the selection still needs
  the operator for that ruling.
- **Everything adopted, or everything rejected.** The workers follow the
  framing of the task and not the content. The result says nothing about
  selection.

## Limits

- One decoy. With three candidates, a matching pattern can occur by chance.
- The operator ruled D1 in a later session, after the term and its purpose
  had changed again. At `13a1803f6` the right answer for D1 is less settled
  than for D3.
- The move tested is one the designing agent found by reading the
  operator's messages after the rulings. A procedure built from the rulings
  it is tested on can show that the procedure is sufficient for them. It
  cannot show that it would have been found beforehand.
- One state, one model, three or four runs per cell.

## A later extension

The same procedure can be applied at `a6bdbb508` to the exclusion of
fixed-measure learners. In experiment 1 no chooser with the checks file
accepted that ruling, so the expected result is rejection. It is left out
of this run to keep the first test small.
