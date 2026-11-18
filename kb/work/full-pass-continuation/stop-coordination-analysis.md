# How stops coordinate the operator and the workflow, and what the change should remove

Written 2026-11-18 by an agent, before any implementation, from the source
at commit `209d4dc3d`. It is a prediction to compare with the result. The
mechanism was read in `headless/operator.py`, `edits.publication()`, and
`_decide()` and `_triage()` in `revise.py`. The tests were counted by name,
not read. `rewrite.py` was not read beyond its use of the publication stop.

## The mechanism at `209d4dc3d`

A stop is coordinated through four pieces.

1. **Pending answers file.** The workflow writes it under the run's
   `artifact/`: one item per decision, each naming its question and the
   question's hash.
2. **Operator record.** `operator/<digest>.json` holds the proposal text and
   a key computed from the file name, the inputs that produced the proposal
   and the proposal (`operator.answer()`).
3. **Approval.** The session agent records the operator's decisions in the
   answers file and runs `commonplace-review approve RUN FILE --key KEY`.
   Under the run lock, `operator.approve()` copies the file's current text
   into the operator record as `answer`, with `answered-at`.
4. **Repeat.** The agent repeats the workflow command. The run replays every
   answered call up to the stop, calls `operator.answer()` again and now
   receives the captured copy. It validates the copy and continues.

The workflow reads the captured copy, never the editable file. Support for
that separation:

- the key, so that an old approval command cannot approve a proposal later
  replaced at the same path;
- `operator.edited()`, which detects a change after approval; the report
  lists it under `unapproved-edits`;
- `operator.invalidate()`, which withdraws an approval when the publication
  files changed; `edits.publication()` then restores the generated
  candidate, diff and pending answers;
- `candidate_key()` and `revised_key()`, which bind a publication approval
  to the start text, the candidate, the decision context and a revised
  candidate.

Five places stop this way: per-item proposals (`_decide()`), triage findings
(`_triage()`), the plan stop (`stop-answers.md`), the publication stop
(`edits.publication()`, also used by every rewrite run) and `record` for an
overtaken run.

`commonplace-review decisions` and the carry-over of earlier decisions
(`decisions.earlier()`, `earlier_stops()`) read the operator records: the
captured `answer` and `answered-at`.

## The explanation

Each of these pieces exists because the same command is repeated, and a
repeat must never count as approval. The captured copy separates "the
operator approved this text" from "this file is on disk when the command
runs again". The key, the edit detection and the invalidation protect that
separation over the interval between approval and the repeat.

When a pass ends at its stop, and a later command is given the answers file
by name, there is no repeat and no interval. The command reads the file and
keeps a copy in its own run.

## Predictions

| Piece | Predicted |
|---|---|
| Answers file, its type and validator; the question hash that ties answers to the exact proposal | stays |
| `decide-items.md` and `approve-a-text.md` | stay, without the approve-then-repeat steps |
| Operator records and the captured copy | removed; the consuming run's copy of its input is the record |
| The `approve` command and proposal keys | removed, except as below |
| `edited()`, `invalidate()`, `unapproved-edits`, restoring changed publication files | removed |
| Replay up to a stop; recorded mode and options for the repeat | removed |
| The lookup of an open run, `mark_open()`, the second case of `known_text()`, the `-2` suffix | removed |
| The candidate checks for a revised text (`revised_problems()`) | stay |
| The bookkeeping that withdraws or keeps a revised candidate across repeats | removed |

**Assurance is expected to be unchanged.** At `209d4dc3d` the agent runs
`approve` on the operator's word. Afterwards it runs the consuming command
on the operator's word. Both depend on the agent doing that honestly.

**Two replacements are expected to be needed.**

- Decisions nothing consumes: a rejection, a deferral, a plan-stop answer
  and `record` have no later command to copy them. They need a small command
  that records an answers file, or a rule that a valid answers file with
  every item decided is the record.
- The decision listing and the carry-over of earlier decisions must read
  answers files in place of operator records: the copies in consuming runs,
  and the decided files from the first point.

Decided on 2026-11-18, after this analysis: naming the answers file is the
approval, and a small recording command covers the first point.

**New code is expected** for the continuation record, the focused run that
takes an answers file, a command that publishes a held candidate, and
planning fixes from triage answers.

## Baseline for the comparison

Lines at `209d4dc3d`:

| File | Lines | Tests |
|---|---:|---:|
| `src/commonplace/headless/operator.py` | 121 | |
| `src/commonplace/lib/review_workflows/edits.py` | 618 | |
| `src/commonplace/lib/review_workflows/revise.py` | 1291 | |
| `src/commonplace/lib/review_workflows/rewrite.py` | 743 | |
| `src/commonplace/lib/review_workflows/decisions.py` | 553 | |
| `src/commonplace/cli/review_workflows.py` | 795 | |
| `tests/commonplace/headless/test_operator.py` | 71 | 4 |
| `tests/commonplace/review_workflows/test_revise.py` | 1855 | 66 |
| `tests/commonplace/review_workflows/test_revise_keys.py` | 138 | 1 |
| `tests/commonplace/review_workflows/test_rewrite.py` | 541 | 17 |
| `tests/commonplace/review_workflows/test_publication.py` | 144 | 7 |
| `tests/commonplace/review_workflows/test_review_decisions.py` | 135 | 5 |

Source total 4121; test total 2884.

Estimates, held with low confidence because the tests and `rewrite.py` were
not read:

- `operator.py` goes, or shrinks to under 30 lines.
- `test_revise_keys.py` goes.
- Source falls by 300 to 450 lines net of the new code.
- 29 of the 66 tests in `test_revise.py` have a name about stops, approvals
  or repeats. At most that many change or go.

## What would count against the explanation

- A piece predicted as removed has to stay for a reason other than the
  repeat. Record the reason.
- The two replacements grow to the size of what they replace.
- A live continuation shows a case where the captured copy protected the
  operator and the named-input command does not.
- Source does not shrink. Then the change moved the coordination; it did not
  simplify it.
