---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: 0639a8d235bbdf791feaa2f1eae21d28a4131c0fe56e0a15fefe51fa524835cf
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/synthesis
launch: ab8bc6970b284070a3c8f4b303e95737
completed-at: '2026-11-20T18:58:04Z'
findings:
- scope: passage
  quotes:
  - Suppose a public library can staff either Tuesday morning or Saturday morning,
    but not both.
  reason: The library-hours hypothetical interrupts the worked Python 3.11 release
    judgment with a different domain and a different point (whose work counts, not
    uncertainty), and its last two sentences restate what the bolded lead and the
    later 'Who gains, and who bears the loss?' bullet already say; a revision could
    move the case into 'What analysis can settle' as the support for that bullet,
    drop the repeated 'another month of counts' sentence, and let the bullet's gloss
    refer back to it instead of re-telling it.
- scope: passage
  quotes:
  - Neither needs a score for every Python release before choosing the next one to
    use.
  reason: Three examples run before any general sentence states the thesis, and the
    second half of the promised claim (investigate an unknown only if a plausible
    answer could reverse the choice) first appears mid-note; a revision could add
    one plain sentence after the opening Python 2/3 example stating both halves of
    the claim, so the later sections read as developing a stated thesis rather than
    accumulating cases.
- scope: passage
  quotes:
  - A partial order can represent the preferences we can defend under a consistent
    set of priorities.
  reason: The point that evidence can expose a trade-off but cannot supply its weights
    is made in 'What analysis can settle', again in the partial-order paragraph ('The
    operator and users supply that judgment'), and a third time in 'does not do the
    weighing', while the partial-order paragraph sits under 'What Commonplace chooses
    to count' although it is general; a revision could state the weighting limit once,
    decide whether the partial-order paragraph belongs beside the analysis-limits
    section, and trim the defensive scope sentence so the Commonplace section carries
    only the declared objective.
contract: report
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/synthesis/calls/launches/ab8bc6970b284070a3c8f4b303e95737/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/synthesis/artifact/reviews/8dfe28d4252fde97341aae64/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/synthesis/calls/launches/ab8bc6970b284070a3c8f4b303e95737/outputs/review.md
raw-output-sha256: 250a7b6348fe7380639c1348f200d010d5ea4954734c9775a4072bc14474c115
---

# Simplification synthesis: On-balance judgments can guide improvement without a global measure

The note's argument is sound and well supported by examples; no gate found material to delete wholesale. The largest gains come from placement: one illustration sits in the wrong section, the thesis arrives after its examples, and one limit (analysis does not supply weights) is spread across two sections with three statements.

## Opportunities

### 1. Relocate the library-hours case to the section it supports

- Location: "A release judgment: Python 3.11 over 3.10", paragraph beginning "Some comparisons turn less on uncertainty than on **whose work the decision serves**", through "whose loss a higher total can hide."; and the bullet "**Who gains, and who bears the loss?**" in "What analysis can settle".
- Reader problem: the release section is the note's main worked example, and a reader following the 3.10/3.11 judgment meets an unrelated staffing scenario before the section ends. The case's point is then re-told in compressed form by the "Who gains" bullet, so the reader encounters it twice in two places.
- Direction: move the case into "What analysis can settle" as the illustration for the "Who gains, and who bears the loss?" question, cut "Asking for another month of counts would miss the disagreement", and shorten the bullet gloss to a back-reference. One possible resolution: the bullet becomes the case's lead-in rather than its summary.
- Combines: branch-bloat (library hypothetical, info); core-claim-obscured (library-hours placement, info); detail-overhang (two trailing sentences, warn); marginal-value-redundancy (bullet glosses repeat earlier examples, info).
- Preserve or decide: keep the distinction that this comparison turns on whose work counts rather than on uncertainty — it is a separate reason more data cannot settle a choice. Keep an explicit marker that the case is hypothetical, since that is an evidence-status claim, even if the transfer gloss is folded into a clause. Keep both purpose-dependent branches.

### 2. State the two-part thesis before the opening examples accumulate

- Location: opening, "Is Python better than it was twenty years ago?" through "That resolves the choice between messages, not the choice between releases."; and "**For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice.**" in "What analysis can settle".
- Reader problem: the body gives the Python 2/3 text case, a two-programmers remark and the `random.py` case before any general sentence says what they show. The reversal rule for which uncertainties to investigate — half of what the description promises — first appears in the third section, and its Commonplace application two sections later, so it reads as one point among several rather than as the note's operating rule.
- Direction: after the opening example, add one general sentence stating both halves: reasons naming what changed, for whom and why it matters can justify preferring a successor without a global score, and an uncertainty is worth investigating only if a plausible answer could reverse the preference. This is one possible formulation, not a settled rewrite.
- Combines: core-claim-obscured (thesis arrives late, info; reversal rule arrives mid-note, info).
- Preserve or decide: keep the "On balance, yes" Python framing and the `random.py` contrast, which the "What is the alternative?" bullet depends on. The preview must not promote the reversal rule into a universal rule; in the note it is scoped "for the decision at hand" and bounded by binding requirements fixed in advance.

### 3. Consolidate the "analysis does not supply the weights" limit

- Location: "What analysis can settle", first paragraph ("Analysis can expose that trade-off; it cannot supply the weights"); "What Commonplace chooses to count", both paragraphs, especially "This is a practical commitment about the work we value, not a claim that every project should use the same measure." and "it does not do the weighing or guarantee that a single stable ranking exists".
- Reader problem: the same limit is stated three times across two sections. The partial-order paragraph is a general point about ranking limits, but it sits under a heading about Commonplace's own objective, which blurs that section's role as the declaration of what Commonplace counts.
- Direction: state the weighting limit once. Decide whether the partial-order paragraph moves next to "What analysis can settle" (where it would extend the timing-test argument) or stays as the bridge from Commonplace's objective to its incomplete comparisons. Trim the defensive scope sentence and the repeated "does not do the weighing" clause, keeping the new admission that no single stable ranking is guaranteed.
- Combines: marginal-value-redundancy (defensive scope sentence, warn; "does not do the weighing", warn); cross-cutting placement of the partial-order paragraph.
- Preserve or decide: the author must decide the conceptual role of the partial-order paragraph — a general claim about evidence, or a statement of how Commonplace's own objective is limited. Preserve "The operator and users supply that judgment", which assigns the weighing to people, and the stable-ranking admission. Keep the Commonplace objective explicitly local: if the scope sentence is cut, the opening "For Commonplace, we choose" must still mark it as a chosen commitment.
