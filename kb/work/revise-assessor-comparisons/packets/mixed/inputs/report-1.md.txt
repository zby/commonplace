---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: aedaa6fe2f3a40239d8e2c1e31fcace7
completed-at: '2026-11-20T18:56:12Z'
findings:
- scope: passage
  quotes:
  - If such blockers were widespread and costly, that would challenge the default
    itself. These checks give reasons for the judgment, not a survey of how often
    each reason applies.
  reason: 'UNSUPPORTED — The note''s own test for the 3.11 default is a prevalence
    condition: the default fails if blockers like the removed `inspect.getargspec`
    are widespread and costly. It then disclaims any survey of how often each reason
    applies. The bolded ''On balance, yes'' therefore rests on an unestablished premise
    that blockers are rare. On the gain side, ''existing code can benefit repeatedly''
    generalizes from one microbenchmark that the table itself scopes to ''one workload
    on two builds''. The four checks show what enters the judgment, not that the balance
    falls on the 3.11 side.'
- scope: passage
  quotes:
  - investigate an unknown only if a plausible answer could reverse the choice
  reason: THIN — The broken-dependency example shows that some investigations cannot
    change the choice. It does not show how to know beforehand which answers are plausible,
    or whether one would reverse the preference. Both require the weighing that 'What
    analysis can settle' says analysis cannot supply. So the rule moves the hard judgment
    into 'plausible' and 'reverse' instead of discharging it. The rule also ignores
    investigation whose value lies in later decisions; the note's own 'revisit it'
    advice suggests such value exists.
- scope: passage
  quotes:
  - A partial order can represent the preferences we can defend under a consistent
    set of priorities.
  reason: THIN — The preceding sentences show that evidence is incomplete and that
    the operator must supply the value weights. Incomplete evidence makes some pairs
    incomparable. It does not ensure that the comparisons defended one at a time,
    each with weights chosen for that case, are transitive. A partial order requires
    transitivity. The library example shows that different priorities give opposite
    preferences, and 'under a consistent set of priorities' assumes that the choice
    between those priorities has already been settled. The closing hedge, that it
    does not 'guarantee that a single stable ranking exists', concedes part of the
    gap without saying when the order holds.
- scope: passage
  quotes:
  - This is a hypothetical case; what transfers to a KB decision is the question of
    whose loss a higher total can hide.
  reason: THIN — The transfer is asserted, not shown. The KB sections later analyse
    the `AGENTS.md` line by task frequency and failure risk, and the tag-head case
    by who stops searching. Neither puts a group's loss against an aggregate gain,
    as Tuesday and Saturday do. Without a KB case where a higher total hides a specific
    party's loss, the reader cannot tell which Commonplace decisions turn on whose
    work counts rather than on uncertainty.
- scope: passage
  quotes:
  - Those reasons can be checked independently of who offered them. Their availability
    makes a judgment criticizable; it does not establish that any particular agent
    judges well.
  reason: HOLDS — The conclusion is limited to criticizability and explicitly excludes
    judgment quality. The reasons named (which work changed, whose costs count, what
    observation would change the recommendation) can each be checked against observable
    facts, as the Python checks were. Under the skeptical default, nothing beyond
    that limited claim is asserted.
contract: report
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/aedaa6fe2f3a40239d8e2c1e31fcace7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/c2e9796896aa687db75e878a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/aedaa6fe2f3a40239d8e2c1e31fcace7/outputs/review.md
raw-output-sha256: d8d4ad49e36ff160655258ddc89fa83c0724d4c4d019afed7c07443fb213767d
---

# Friction check: On-balance judgments can guide improvement without a global measure

**Central claim (one sentence):** One version can be justified over another by stating which work changed, for whom, and why it matters, with no score that ranks every version, and analysis is worth spending only on unknowns whose plausible answers could reverse that choice.

## Filter
**Filter:** SURVIVES

The properties the claim must hold at once are: the judgment guides action, it uses no global measure, and it is criticizable rather than arbitrary. These properties can coexist because the note makes each judgment local to an alternative, a set of affected parties and a period, and makes it criticizable through the reasons it gives. The closest tension is the Commonplace objective, "more useful and better-warranted knowledge work for the human judgment spent". It reads like a global measure. The note presents it as a declared objective that is weighed case by case, not scored, so it does not reintroduce the measure the title rejects. A secondary strain appears in the partial-order passage; it is a joint below, not a contradiction.

## Thinnest joints

The 3.11 verdict ranks first. It is the note's only fully worked release judgment, and the note states the condition that would defeat it, then says it did not check that condition. The investigation rule ranks second because the note uses it as its main practical instruction, yet it depends on judgments of plausibility and reversal that the note says analysis cannot supply. The partial-order step and the library transfer are both thin, but they matter less: the first concerns how preferences are represented, not which choice to make, and the second weakens the bridge from an analogy to the KB without affecting the Python argument. The last joint is listed only to show that the note's final, narrowly hedged inference holds.

The rationale for the Commonplace objective ("because we repeatedly have to decide...") is a declared commitment, not an inference, so it was not ranked. However, "Automation alone does not answer that question" is not connected to the sentence that follows it.

## For the human
Start with the 3.11 paragraph. Either give a reason to believe blockers like `getargspec` are rare, or present 'On balance, yes' as conditional on that rarity.
