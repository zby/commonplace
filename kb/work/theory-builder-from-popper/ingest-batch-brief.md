# Ingest re-judging brief (D7)

Worker packet for batches B1–B7 in the
[consumer inventory](./consumer-inventory.md#delegation-batches-for-ingest-re-judging).
The parent names the batch; the file list is the inventory's row for it.

## Purpose

Source ingests in `kb/sources/` carry a `Learning Claims (our opinion)`
section that judged each source against the retired
`conjectural-learning.md` definition. Re-judge each ingest in the batch
against the new [theory-builder definition](../../notes/definitions/theory-builder.md)
so the KB's opinions match the definition it now holds. Read the definition
and its [checks](../../notes/definitions/theory-builder-checks.md) first; the
checks' cases are the calibration set.

## The definition in brief

Four conditions: 1 localized content (theories stated in natural or formal
language, identifiable units carry content); 2 consumption (theories guide
what the system does through what they say); 3 criticism (a working process
of attempted refutation aimed at what identified units say; a criticism is
itself stated and can blame the test, data, or an auxiliary; score selection
over variants is trial and error, not criticism; gradient descent fails 1 and
3); 4 iteration (the result of criticism is kept and shapes the next
conjecture; a revised theory re-tested on the cases that refuted its
predecessor faces a real test; keeping the record of criticism and rebuilding
from it counts; a critic whose report feeds no next conjecture fails).
Persistence is graded, not a condition: record the grade reached (within one
reasoning episode, across rounds of one run, across runs on one task, across
problems and sessions). Freezing a product and handing it off ends the
builder; it was still a builder while it ran. This superseded, on 2026-09-25,
an earlier reading that required retained results to be taken up on a new
problem; verdicts decided only by that reading are wrong. No success condition: learning
(improved capacity for future action) is a separate claim. Fine-grained
addressability is a graded design commitment, not a condition; a model
replaced whole is an addressable part of the machinery. Reflective and
autonomous are qualifiers.

## Edit boundary (precedent f4dc912d)

Edit only: the `Learning Claims (our opinion)` section, footer links, and
follow-up lines. Keep unchanged: source-native terminology, summaries,
provenance, every quote, `snapshot_sha256`, frontmatter other than links.
Replace every link to `conjectural-learning.md`, `conjectural-learning-checks.md`,
`reflective-theory-builder.md`, `autonomous-theory-builder.md`, or
`externally-tested-theory-builder.md` with the fitting target:
`theory-builder.md` (anchors `#qualifiers`, `#boundary`, `#addressability`),
or `../notes/a-claim-without-external-assessment-carries-three-obligations.md`
for the externally tested concept. Links to the precedents note and the
research companion keep their current paths; a later relocation rewrites
them.

## Rewrite rule

State each condition the source shows or fails, at its evidence strength.
Name the deciding condition for a negative verdict. State learning
(improvement, attribution) separately. Do not infer a missing condition from
its neighbours. Opacity leaves a condition unestablished, not failed. Where
the source's evidence does not settle a condition, say so; do not guess. Keep
the section about as long as it was. Grounding must not narrow the KB's own
claims to fit a source: change a verdict because the definition changed, not
because a source is quiet.

## Scope and output

Write scope: only the ingest files in your batch. Do not commit. Verify each
with `commonplace-validate <file>` from the repo root. Return one line per
file: conditions met (1–4, each met / failed / unestablished), deciding
condition, learning claim status, and flip versus the inventory's prediction
(confirmed or corrected, with the reason when corrected). Flag any file whose
verdict you could not settle.
