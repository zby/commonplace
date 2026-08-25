# The grounding-alignment link budget miscounts

Found 2026-08-25 while running review job 8051, the first exercise of ADR 073's
`(snapshot required)` route. Written for whoever fixes the gate; nothing here is
fixed yet.

## The defect

[`semantic/grounding-alignment`](../../instructions/review-gates/semantic/grounding-alignment.md),
line 23:

> For linked notes and ordinary linked sources, read the linked material and
> follow at most five links in total.

The budget counts **link occurrences**. The resource it protects is **distinct
artifacts loaded**. Five links to one ingest is one load; five links to five
ingests is five. Counting occurrences makes a reviewer stop early for no saving.

## Evidence

- **239 of 314 linked notes (76%) repeat a link target.**
- **45 notes carry more than five link occurrences across five or fewer distinct
  targets.** Under the occurrence reading a reviewer exhausts its budget and
  leaves links unchecked that would cost nothing extra to open. Worst case:
  `a-retrieval-miss-is-a-local-reflective-path-failure`, 11 occurrences over 5
  distinct targets.
- Job 8051 checked 5 of 9 links on a note whose 9 occurrences happened to be 9
  distinct targets, so the miscount did not bite there — but the reviewer
  disclosed four unopened internal links, making the PASS a verdict on a sample.

## Two further questions, deliberately not settled here

**Is five still the right number?** It looks inherited rather than derived. The
snapshot the route loaded was 128 KB ≈ 32k tokens, and the reviewer's entire job
came to 88k tokens including the gate, the note, and all five links. Corpus
snapshots run 23 KB median, 112 KB p90, 456 KB max ≈ 116k tokens. **Following
links is not the expensive operation it may once have been**, so the cap should
be re-derived against current costs the way
[ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md)
re-derived the description ceiling that had "inherited an earlier full-index cost
concern."

**Do ingest routes draw on the same budget?** The gate states the five-link cap
for "linked notes and ordinary linked sources," then gives ingests their own two
routes without saying whether they consume it. Job 8051's reviewer assumed they
do and counted them. That reading should be made explicit rather than left to
inference — it is exactly the kind of arbitrary, non-inferable detail an
instruction should carry.

## Superseded direction: do not add evidence classes

An earlier version of this file proposed prioritising source links over internal
ones, on the strength of the reviewer choosing that order unprompted. **Operator
decision 2026-08-25: do not add rules splitting evidence into classes; keep the
cap global.** A ranking rule buys a better default ordering at the cost of one
more classification an author and a reviewer must both apply consistently.

The direction taken instead is
[Review link budget prices reviewer attention](../../reference/proposals/review-link-budget-prices-reviewer-attention.md),
which dissolves all three defects above rather than patching them: material
already loaded costs no further bytes, heterogeneous sizes get priced, and a
reviewer holding a byte budget spends it well without being told how to rank.

## Cost of the fix, and why to batch

Editing this gate stales **775 review pairs** as `criterion-changed` — the ADR
038 mechanic working as designed, but a large sweep to trigger twice. The
counting rule, the number, and the ingest-budget ambiguity are three edits to one
file; doing them in one pass costs one sweep instead of three.

Those re-reviews are not waste. Every prior verdict was reached under a cap that
counted the wrong thing, and on link-dense notes that means earlier passes may
have sampled where they appeared to be exhaustive.

## What not to assume

**That the cap should simply be raised or removed.** Job 8051 shows a reviewer
budgeting sensibly and disclosing what it skipped; the disclosure is what keeps a
sampled verdict honest. A larger number without the disclosure requirement would
be worse than a smaller one with it.

**That this is urgent.** It is a correctness-of-scope issue on a gate that
currently passes, not a live failure. It became visible only because the
snapshot route made one link much heavier than the others.
