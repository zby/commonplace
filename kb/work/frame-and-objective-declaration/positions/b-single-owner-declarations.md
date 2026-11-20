# Position B: complete the owner declarations and cite them

Author: Claude Code agent, claude-fable-5-2, 2026-11-20
Source: reply to the operator on reading position A's report.

## Revisions after position C (2026-11-20)

B concedes three points to [position C](./c-declare-shared-state-observed-locally.md).
The text below is kept as first written so the record shows what changed.

- **Rule.** C's wording replaces B's. A shared declaration cannot say who
  decided in a particular episode, so the claim must state that locally.
- **D4, whose judgment.** B's "designated-maintainer judgment" was an error. It
  tied the denominator to the boundary, so moving diagnosis to an outside
  contributor would read as a saving. The denominator counts the judgment the
  work requires and reports who supplied it. B's scope answer (build and
  maintenance count) stands and matches C's.
- **D6.** B's bullet was too broad. An observation owes nothing. An effect
  claim owes the rival explanations that could change its conclusion, not the
  closure note's full declaration list.

One residue C's D4 answer leaves open: "the judgment the work requires" needs a
limit once it is no longer bounded by the maintainer role. B's proposal is
judgment required to produce and maintain the work, not judgment a reader
spends using it.

## Revisions after position D (2026-11-20)

B concedes most of [position D](./d-shrink-to-the-objective.md) and disputes
one point.

Conceded:

- **The plan was too large.** It wrote the instrument-note edits before the
  test that would license them. The plan now runs D's open-question check on
  the instrument note first and makes every dependent edit conditional on it.
- **The cold-reader questions were leading.** D's open question replaces them.
- **The convergence is one author's record.** B's author wrote A's and C's
  files, the concessions, the plan and the settlement. The settlement now says
  which rows rest on a relayed comment.
- **D4.** "Spent, by supplier" replaces "requires". Readers' judgment is
  excluded because reader cost is already in the numerator as usefulness.
- **D6 and D8.** No frame-note bullet and no rule unless the check finds an
  overclaim.
- **D1 and D3** are moot, not deferred.

Disputed, D5 and D7:

D is right that these are one question and that cross-pointers do not answer
it. B withdraws its pointer from the frame note to the instrument note. B does
not accept moving the objective into the frame note, for this reason. The
definition's objective parameter is declared per attribution: the tag-readme
classification is read against ADR 026's adopted criterion, not against the
program objective. If the frame note carried "work per unit of human judgment",
every attribution under the frame would appear to be read against it, which
the existing classification contradicts.

B's revised answer: the frame note says in one sentence that it fixes the
boundary and partition, which are the parts shared by all attributions, and
that horizon and improvement objective are declared per attribution. That
removes the second sense of "frame" without a rename. The program objective
stays in the instrument note as what it already is: the objective of the design
program, used when the program itself is assessed. Its accounting scope fits in
two sentences, which answers D's concern about the note's character.

What would change this: an attribution in the KB that is read against the
program objective and would be harder to state with the objective outside the
frame note.

## Diagnosis

1. **The boundary has an owner; the objective and the effect claims do not.**
   The definition names three parameters. [The frame note](../../../reference/commonplace-declared-frame.md)
   owns the boundary and partition. The objective is one sentence at
   `commonplace-as-an-instrument.md:11`, copied into two proposals. No copy
   says which human judgment the denominator counts.
2. **The frame note covers classification claims only.** Its "Using the frame"
   section lists membership, reflectivity, closure and allocation. The
   instrument note makes a different kind of claim: it credits outcomes
   (composition, work per unit of judgment) to the machinery. The frame makes
   such a claim well-formed. It does not support it.
3. **"Frame" has two senses.** The tag head says "declared frame of boundary,
   horizon, and improvement objective". The frame note declares boundary and
   partition only. Its body does not say where the objective is declared; only
   the instrument note's footer says so.
4. **"Components" collides.** The instrument note (L17) uses it for design
   parts. The frame note uses it for actors on each side of the partition.

## Remedy

Rule: each parameter has one owner artifact. Other artifacts link the owner at
the first sentence that depends on it and do not restate it.

Edits:

- **Frame note, opening.** One sentence: this note fixes the boundary
  parameter; the horizon is declared per attribution; the objective is declared
  in the instrument note.
- **Frame note, "Using the frame".** One bullet: a claim that credits an
  outcome to one side of the partition, or to the system rather than to outside
  inputs, is an effect-attribution claim. The frame does not support it. It
  owes the declarations listed in the closure note's "Declare the assessed work
  and permitted inputs": the side credited, seed versus run-time judgment, and
  outside inputs such as model strength.
- **Instrument note, L11.** Make the objective a declaration. The denominator
  is designated-maintainer judgment, including judgment spent building and
  maintaining the methodology. Model strength is a covariate to report.
- **Instrument note, L17.** Link the frame where "components" first appears and
  use a word that does not collide with the partition's.
- **Instrument note, baseline-gap bullet (L39).** Name the three rival
  explanations in one sentence with a link: maintainer repair, seed judgment,
  stronger models.
- **Two proposals.** Replace the copied objective sentence with a citation.

## Answers

- D1: no shift. A maintainer inside the boundary and human judgment as the
  denominator are compatible: the denominator is the cost drawn from the
  frame's human components. L17 is a word collision.
- D2: link at first dependent use. A footer link is too weak; a restatement
  recreates the copies the frame note was written to end, and copies drift.
- D3: not the cause. With maintainers outside the boundary, their input would
  still need metering and model gains would still need a control. The three
  cuts are rival explanations that any effectiveness claim owes under any
  boundary.
- D4: amortized. Build and maintenance judgment count; model strength is a
  reported covariate. The ablation proposal already counts "later maintenance
  cost" and the reusable-commitment proposal already says "not per task".
  This is the operator's decision.
- D5: the instrument note stays the owner; the proposals cite it. A separate
  objective note is not justified until a second artifact needs to extend the
  declaration.
- D6: yes, one bullet as above.
- D7: the frame note says it fixes the boundary parameter. The tag head keeps
  the three-parameter sense.
- D8: nowhere yet. Record the gap; add a review criterion only after a second
  occurrence.

## What would change this position

- A sentence in the instrument note whose truth value differs depending on
  which side of the boundary the maintainer is on. That would establish D1 as
  a shift rather than a collision.
- A cold reader who follows the first-use link and still misreads the note.
  That would favour restatement on D2.
- A second artifact that needs the objective with different accounting. That
  would favour a separate objective note on D5.

## Against other positions

- **A, D1.** L11, L17 and L19 are each consistent with the declared frame.
  L19's human functions are what the classification already reports as
  allocation; they bear on what the trace shows about composition, which is an
  effect question (D6), not a membership question.
- **A, D2.** Restating per note scales with the number of notes and has no
  owner. The frame note's own first paragraph says applications cite it instead
  of re-deriving the boundary.
- **A, D3.** The cited closure-note section declares the three cuts for closure
  evidence in general, including the software-house case, not as a consequence
  of human inclusion.
- **A, confounds.** All three are real and worth naming. Two are already in the
  ablation proposal (maintainer repair at L9, stronger bare model as an arm).
  The second, the denominator's scope, is the one substantive gap, and it is a
  gap in the objective's declaration, not in the boundary's.
