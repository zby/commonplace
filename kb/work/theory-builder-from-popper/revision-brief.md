# Post-migration revision brief

Worker packet for the coherence pass after the theory-builder migration. The
parent names your files; edit only those.

## Purpose

On 2026-09-25 the KB replaced *conjectural learning* and the reflective,
autonomous, and externally tested builder definitions with one redefined
[theory builder](../../notes/definitions/theory-builder.md). Many notes and
articles were patched in several passes by different workers, and condition 4
changed meaning mid-way. Patched text tends to keep leftovers and to lose
flow. Make each file read as if it had been written against the current
definition from the start, without changing what it claims beyond what
consistency with the definition requires.

## The current definition in brief

Read the definition and its [checks](../../notes/definitions/theory-builder-checks.md)
before editing. Four conditions: 1 localized content, 2 consumption,
3 criticism aimed at what stated units say, 4 iteration (the result of
criticism shapes the next conjecture). No success condition: learning
(improved capacity for future action) is a separate claim. Addressability and
persistence are graded design commitments above the minimums of conditions 1
and 4; Commonplace builds for the high end of both, and that this pays is
conjectured. Reflective and autonomous are independent qualifiers. The
externally tested case lives in the
[three-obligations note](../../notes/a-claim-without-external-assessment-carries-three-obligations.md)
and the evaluation apparatus in the
[testing article](../../articles/testing-whether-a-theory-builder-learns.md).

## Leftovers to find and fix

- Retired terms used as KB vocabulary: *conjectural learning/learner*,
  *reflective/autonomous/externally tested theory builder* as separate
  definitions (as qualifiers of a theory builder they are fine), *theory
  refinement* as the KB's operation.
- Superseded condition names and readings: condition 4 as *growth* or
  *retention*, retention as a membership condition, "taken up on a new
  problem", "rounds on one problem are one pass of error elimination",
  "five conditions", addressability as a condition.
- Link text showing old titles; links or claims about deleted definitions;
  descriptions that no longer match the body.
- Contradictions with the definition, or with another file in the same
  group.
- Repeated caveats or definitions restated several times after patching.

## Flow and coherence

- Transitions broken by inserted paragraphs; sections that now answer a
  question the file no longer asks; ordering that made sense before the
  patch.
- An argument's chain should run in one direction. Merge duplicates, cut
  restatements, and move qualifications next to the claim they limit.
- Keep each note's title claim. Keep anchors that other files link to (check
  with `rg '<file>#' kb`).
- Follow the writing quality bar in `AGENTS.md` and the collection's
  `COLLECTION.md` (articles: reader-only body, five-unquoted-source limit).
  Keep citations and quotes exact; never invent a quote or precision.

## Scope and output

Content edits only: no renames, no commits. Do not change another file to fit
yours; report the conflict instead. Verify each file with
`commonplace-validate <file>` from the repo root. Return per file: leftovers
fixed, flow changes made, word delta, and anything that needs an operator
decision (for example a claim you think is now wrong but did not change).
