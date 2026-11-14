# First run of the fix-findings variant

## What was run

On 2026-11-14 the [fix-findings variant](./first-variant-fix-findings.md)
was run once, by the session agent, on
[two context boundaries govern operations on read-together note sets](../../theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md).
It was the only note with fresh warnings that no other session was
editing. The five run types were first registered under
`kb/reports/types/`, since the run directory cannot be validated without
them.

The run directory is
`kb/reports/state/improve/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets/20261114-072641/`.
It is local and ignored, like the rest of the state tree.

## Result

| | |
|---|---|
| Fresh warnings at the start | 8, holding 10 warning-level findings |
| Findings fixed | 5, by 4 edits in one run of the fix operation |
| Findings left open | 5, each a pending item with the agent's view |
| Higher-order check | Skipped; it is not an atom yet |
| Ending | `partly-applied` |
| Re-review of the edited text | 40 results: 33 pass, 7 warn |
| Re-review cost | 41 launches, about 4.8 USD |

`commonplace-validate` accepts the run directory. Three deliberately broken
copies were refused: a rejection without a reason, an answers member naming
another note, and a closed run with the answers member missing. The types
therefore enforce what the drafts said they would.

## What the run showed about the design

1. **The types hold a real run.** No member needed a field the schemas
   lacked, and the layout's identity and requiredness checks fired on the
   broken copies.
2. **The re-review does not show cleanly whether the fixes worked.** Of the
   four pairs whose findings were fixed, two passed afterwards and two
   still warned, on other sentences. One pair whose finding was left open
   and whose passage was not edited went from warn to pass. Two pairs
   outside the start set warned. Verdicts move between runs for reasons
   other than the edits, as the calibration workshop also found for weak
   proposals. A single re-review is weak evidence about a fix.
3. **An open item can outlive its warning.** The item on the relation
   between "collection" and "area" is still pending, while the gate that
   raised it now passes on a text where that paragraph is unchanged. The
   closing rules expire an item when the text changes; they do not say
   what a passing re-review means for it.
4. **The variant is silent on INFO-level findings.** The reviews held
   about a dozen. They were read and neither recorded nor worked. "Note
   everything" suggests they should be recorded; working them would widen
   the variant beyond warnings.
5. **Re-review findings are cited but not transcribed.** The seven new
   warnings are entries with a citation and a placeholder text. Reading
   and listing them is the next run's first step, so transcribing them
   twice was avoided. The variant should say so.
6. **Which text an item is proposed against needed a choice.** The items
   were written after the edits, so they carry the final text's hash. The
   variant should state that items written in a run that also edits are
   checked against, and name, the text the run ends on.
7. **The re-review is most of the cost.** The fixes took four small edits;
   the sweep took 41 launches. Whether every run needs a full sweep is
   open choice 3 of the variant, now with a number.
8. **The decisions command does not see the five pending items.** They are
   findable only by opening the run. This blocks the second run's first
   step and is the next code change the design needs.
9. **Writing the members by hand is laborious.** The agent wrote them with
   a script that computed the hashes and citations. An agent following the
   variant in a session would need the same; a small helper that opens a
   run, stores a text and cites a launch would remove most of the labour
   without deciding anything.

## What is not shown

One run on one note by the agent that drafted the variant. It does not
show that another agent can follow the variant, that the conservative rule
produces a manageable number of open items across notes, or anything about
the higher-order step, the closing rules across runs, or a decision being
recorded and applied.
