# Plan

Revised 2026-11-20 after position D. The earlier version wrote dependent edits
before the test that would license them; this one does not.

## Step 1 — the operator rules D4

Proposed ruling, on which B, C and D converge:

> The objective counts human judgment spent on construction, operation, repair
> and maintenance over a stated period, reported by who supplied it. A
> reader's cost of using the work counts in the numerator, as usefulness.
> Model strength is reported with any comparison. The cost of one more task
> may be reported, labelled as that.

## Step 2 — cold-reader check on the instrument note alone

Needs no ruling; it reads the note as it stands.

A fresh agent with no workshop context reads
`kb/reference/commonplace-as-an-instrument.md` and its linked notes as it
chooses, then answers one open question: "What does this note claim the
tag-readme trace shows about Commonplace?" A second open question covers the
objective: "What does this note say Commonplace is trying to achieve, and how
would you measure it?"

Score the answers for overclaims: any statement that the trace shows the
framework's effect, that the parts composed without human bridging, or that
the objective has been met. Record the question, the answer and the scoring in
`cold-reader-check.md`. The runner should not be position B's author.

Prediction on record (D): no overclaim, because the note disclaims effect at
L21, L39, L47 and L55. The second question is expected to expose the
unstated denominator, which is the D4 gap and not an overclaim.

## Step 3 — the minimal edits

Applied whatever step 2 finds, once D4 is ruled and D5 + D7 is settled:

- **Objective declaration.** Two sentences carrying the D4 ruling, in the
  owner that D5 + D7 selects: the instrument note at L11 (B, C) or the frame
  note (D).
- **Frame note, one sentence.** Under B: it fixes boundary and partition;
  horizon and improvement objective are declared per attribution. Under D:
  replaced by the objective declaration itself.
- **Two proposals.** Replace the copied objective sentence with a citation.
- **Instrument note, L17.** Replace "components" with a word that does not
  collide with the partition's.

## Step 4 — only if step 2 finds an overclaim

Then, and only then:

- Edit the passage the reader overclaimed from, stating locally what was
  observed and who decided.
- Run the same open-question check on the other artifacts that link the frame
  note or make effect claims about Commonplace. The list from the earlier plan
  is the starting set: the reflective-system classification, the two tag-readme
  trace notes, `a-repeatable-operative-path…`, `only-explicit-retention…`,
  `commonplace-revision-used-theory-guided-computational-search`,
  `commonplace-builds-a-theory-builder…`.
- If several artifacts show the same overclaim, propose one review criterion
  under `kb/reference/proposals/`. Otherwise add no rule.

Hypotheses this step would test, not edits to make in advance: that L19–21
lets a reader infer composition without human bridging, and that L39 hides the
rival explanations.

## Step 5 — close

If step 2 finds nothing, the workshop's whole output is step 3. Mark D1 and D3
moot, D6 and D8 resolved as "no addition", validate the changed files with
`commonplace-validate`, delete the directory and remove its entry from
`kb/work/README.md`.

The observation and effect-claim distinction is then not placed anywhere. It
is recorded in `kb/log.md` as a first observation, since no artifact needed
it.

## Commits

One commit for step 3, one for closure, each with
`Workshop: kb/work/frame-and-objective-declaration`.
