# The stop-coordination prediction compared with the implementation

Written 2026-11-18 by an agent, after the merge `5d97ab35f`. It compares
[the analysis](./stop-coordination-analysis.md), written before any
implementation, with the merged code. The line counts are from `wc -l` at
the merge. No live run has exercised the new flow, so the third test of the
analysis ("a live continuation shows a case where the captured copy
protected the operator") is still open.

## Outcome

The prediction about which pieces go was right. The prediction about size
was wrong: the six source files fell by 77 lines, not by 300 to 450. The
analysis said that when source does not shrink, the change moved the
coordination and did not simplify it. By line count that is close to what
happened. By number of mechanisms it is not: seven were removed and four
were added.

## Pieces

| Piece | Predicted | Result |
|---|---|---|
| Answers file, type, validator, question hash | stays | stayed |
| `decide-items.md`, `approve-a-text.md` | stay, without approve-then-repeat | stayed, rewritten so |
| Operator records and the captured copy | removed | removed; `headless/operator.py` deleted |
| The `approve` command and proposal keys | removed | removed, with `test_revise_keys.py` and `revise_keys.json` |
| `edited()`, `invalidate()`, `unapproved-edits`, restoring publication files | removed | removed |
| Replay up to a stop; recorded mode and options | removed | removed, with `--restart` |
| Open-run lookup, `mark_open()`, second case of `known_text()`, `-2` suffix | removed | removed |
| `revised_problems()` | stays | stayed |
| Bookkeeping of a revised candidate across repeats | removed | removed |

No piece predicted as removed had to stay.

Both predicted replacements were needed and stayed small in concept:
`answers record FILE`, and a decision listing that reads kept answers
(`answers/*.json` in each run). The second grew `decisions.py` from 553 to
730 lines, which the analysis did not foresee.

## Size

| File | At `209d4dc3d` | At merge |
|---|---:|---:|
| `headless/operator.py` | 121 | deleted |
| `review_workflows/edits.py` | 618 | 503 |
| `review_workflows/revise.py` | 1291 | 1393 |
| `review_workflows/rewrite.py` | 743 | 675 |
| `review_workflows/decisions.py` | 553 | 730 |
| `cli/review_workflows.py` | 795 | 743 |
| Source total | 4121 | 4044 |
| Six test files of the baseline | 2884 | 2711 |

Outside the baseline: `scripts/convert_operator_records.py` (121 lines) and
its test (98 lines), both one-off and removable now that the conversion has
run.

`test_revise.py` went from 66 tests to 65, but the diff rewrote about 700
of its 1855 lines. The estimate "at most 29 tests change" counted tests by
name and missed that most tests set up a run through the repeated command.

## Why the size estimate missed

1. **Continuation record.** The analysis listed it as new code and did not
   size it. Building one item per kind of unfinished work, with its command,
   actor and evidence, is about 130 lines of `revise.py`.
2. **Guards that the captured copy used to give.** Without a captured copy,
   each consuming command checks its input itself: the note still holds the
   text the proposals were made for, the write brief is unchanged, and a
   held candidate, its diff and its review are the files that were held
   (`sha256` fields in `held.json`). Two reviews found these one at a time.
3. **What the shared run directory used to give.** Repeated runs shared a
   directory, so they shared a lock, a scope and a finding. With one
   directory per run, each had to be carried explicitly: a per-note
   publication lock, one-entry plan files that keep an entry's scope, and
   run-owned copies of findings. The analysis did not see that the run
   directory was doing this work. The README had placed the publication
   lock outside the workshop; the second review showed that the change
   itself removed the protection, so the lock is in.
4. **Decision listing.** See above.

## Against the explanation

The analysis named four observations that would count against "each piece
exists because the command is repeated".

- *A removed piece has to stay.* Not observed.
- *The replacements grow to the size of what they replace.* Not for the two
  named replacements. But points 2 and 3 above are replacements the analysis
  did not name, and together with the continuation record they cancel most
  of the removal.
- *A live case where the captured copy protected the operator.* Not yet
  testable.
- *Source does not shrink.* It shrank by 2%.

So the explanation holds for the approval machinery, and it was incomplete:
the repeat also supplied shared context between the steps of one piece of
work, at no cost in code. Ending the run at a stop makes that context
explicit data. What the operator and the session agent gain is a simpler
procedure (no approve-then-repeat, no keys, one rule: name the file), not
less code.

## Defects found in review

Two independent reviews after implementation found defects, all fixed with
tests before the merge. The first review's findings included lost operator
answers after a failed run and an unverified review file at publication.
Five came from the second: a dropped scope on two paths, the
lost update between two runs, a replaceable finding and a wrong stale count.
The first review missed the second's five. Each of the second's five is a
case of point 3.

## Conversion

Run on the main checkout on 2026-11-18: 18 answered operator records
converted to kept answers, 10 unanswered records left in place, 12
`start.json` files written, no problems; a second run changed nothing.
`commonplace-review decisions` lists the converted decisions. One live
unanswered plan stop, on
`kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md`,
is no longer listed; the operator left it for later work.
