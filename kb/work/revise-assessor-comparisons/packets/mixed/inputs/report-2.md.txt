---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/critique-note.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: db780594c200466ea92d61258f733cbb
completed-at: '2026-11-20T18:56:02Z'
findings:
- scope: passage
  quotes:
  - A partial order can represent the preferences we can defend under a consistent
    set of priorities.
  reason: The note relies on 'a consistent set of priorities' but never says where
    those priorities are declared or how consistency across successive decisions is
    checked. Without an antecedent statement of the priorities, the weighting is supplied
    at decision time, after the change is seen. The linked note on declared objectives
    treats that as the post-hoc fitting failure. The note should say what fixes the
    priorities before a change is judged, for example a recorded ranking of protected
    losses or the factory-style fixed requirements it mentions later, and should say
    how a new judgment is checked against earlier ones.
- scope: passage
  quotes:
  - Those reasons can be checked independently of who offered them.
  reason: This holds for the factual reasons (which work changed, and for whom). It
    does not obviously hold for the weighting, and the library example shows that
    the weighting is where disagreement lives. The note should separate the two. Facts
    about who gains are checkable. A weighting can be criticized only for inconsistency
    with a declared objective or with earlier judgments. Without that separation the
    closing claim overstates how criticizable an on-balance judgment is.
- scope: passage
  quotes:
  - If a plausible frequency would reverse the preference, investigate those tasks
  reason: The reversal test needs some range of weights to say whether a plausible
    answer reverses the choice. That is the input the note says analysis cannot supply.
    The test is coherent if it runs over a range of acceptable weightings rather than
    one score, but the note does not say so. One sentence saying that the robustness
    check runs over the plausible weightings as well as the plausible facts would
    close the gap.
- scope: passage
  quotes:
  - whether they yield more useful and better-warranted knowledge work for the human
    judgment spent, on balance
  reason: 'Read literally, the declared Commonplace objective is a ratio of output
    per judgment spent: a global measure in form, even if it is never computed. An
    opponent will read the section as reintroducing the scalar the title disclaims.
    The note should say explicitly that the ratio names the direction of preference
    without being operationalized as a score, and that it orders only the comparisons
    the evidence reaches.'
contract: report
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/db780594c200466ea92d61258f733cbb/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/6e78f0d23c8c6b8844f7b371/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/db780594c200466ea92d61258f733cbb/outputs/review.md
raw-output-sha256: bf9a60ca5f14b4320c24a1162fe2ce8181e2ef0d6ed60d348c4c94e63f2428cd
attack-outcome: partially lands
---

# Critique: On-balance judgments can guide improvement without a global measure

**Note:** kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
**Central commitment:** A version or change can be justifiably preferred "on balance" by giving reasons (which work changed, for whom, why it matters, and whether a plausible unknown could reverse the choice) without computing a global score or total order. Commonplace should choose changes this way.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a decision theorist in the expected-utility and revealed-preference tradition, joined by an auditor worried about drift. Their argument has three steps.

1. **The weights are hidden, not absent.** Any agent that keeps choosing between alternatives with mixed gains and losses acts as if it held trade-off weights. Consistent choices reveal a utility function; inconsistent choices can be exploited or can cycle. Saying "on balance" therefore does not remove the global measure. It removes the written statement of the measure, and with it the main check on the measure: consistency across decisions. In the note's own example, keeping Saturday in one decision and protecting Tuesday-only residents in the next is incoherent unless a stated priority explains the difference. The note offers no place where such a priority is recorded.

2. **The weighting is chosen after the change is seen.** The note's own linked ground, "Self-improvement is relative to a declared objective" (`kb/theory/self-improvement-is-relative-to-a-declared-objective.md`), says an objective must be *antecedent*: identifiable independently of the change it licenses. Otherwise "improvement" becomes "whatever this change does better". An on-balance judgment that sets its weights at decision time, after seeing which tasks gained and which lost, is the redescription failure that note warns about. The Commonplace objective ("more useful and better-warranted knowledge work for the human judgment spent, on balance") names a direction. The phrase "on balance" leaves the trade-offs to the moment of choice, so each judgment can fit its weighting to the change it approves.

3. **The decision rule needs the weights it disclaims.** "Investigate an unknown only if a plausible answer could reverse the choice" is a value-of-information test. Whether an answer reverses the choice depends on how losses are weighed against gains. That is the input the note says "analysis... cannot supply." So either the agent applies private weights, which brings back step 1, or the test cannot be run.

The conclusion is that guidance without a global measure is either a global measure left unstated or an unconstrained judgment. In both cases the note's claim that reasons make the judgment criticizable reaches only the facts, not the decision.

## How the note engages it

**Partially engaged.**

- The note concedes much of step 1 explicitly: a partial order "describes the limits of the ranking; it does not do the weighing or guarantee that a single stable ranking exists." It also places the weighting with "the operator and users". So it does not claim that weighing disappears, only that it need not take the form of a global score. That defeats the crude version of the objection, which treats "no global measure" as "no weights".
- It addresses cumulative drift directly: "Compare the whole table with its earlier, shorter version rather than assuming that a succession of reasonable additions remains reasonable in aggregate." This partly answers the cycling and drift worry by requiring whole-state comparisons.
- It limits on-balance judgment where weights have been fixed in advance: "Known requirements need not be weighed afresh... an on-balance judgment does not override a binding requirement." This is the right antecedent mechanism, but it is offered only for factory-style requirements, not as the general answer to step 2.
- The library example identifies "whose loss a higher total can hide" as the place where value enters. This shows the author sees that the disagreement is about weighting, not facts.
- The note does not engage step 3: the reversal test is presented as if it needed no weights. On step 2, the note invokes "a consistent set of priorities" but never says where those priorities are declared before a change is judged. Its own grounding note makes that the condition separating improvement from post-hoc fitting. The closing paragraph ("Those reasons can be checked independently of who offered them") does not distinguish checkable facts from criticizable weightings.

The attack therefore does not defeat the commitment. Guidance by reasons over a partial order is coherent if the priorities are declared beforehand and the robustness test runs over a range of weightings. The note asserts that guidance without supplying that link.

## Constructive findings

- Say where the "consistent set of priorities" lives before a change is judged. Examples include losses Commonplace treats as protected (like the Tuesday-only residents) or binding requirements fixed in advance. Connect this explicitly to the antecedence condition in the linked declared-objective note, so on-balance judgment cannot be read as post-hoc fitting.
- State that the reversal test ("investigate only if a plausible answer could reverse the choice") runs over plausible weightings as well as plausible facts. A preference that holds across every acceptable weighting needs no single score. A preference that flips between acceptable weightings is a value disagreement to escalate, not an unknown to investigate. The library paragraph already gestures at this distinction; the decision rule should carry it.
- In the closing paragraph, separate the two kinds of reasons. Claims about which work changed and for whom can be checked by anyone. A weighting can be criticized for inconsistency with the declared objective or with earlier recorded judgments. This keeps the "criticizable" claim from overreaching.
- Address the scalar reading of the Commonplace objective. "Knowledge work for the human judgment spent" reads as a ratio. One sentence should say that it fixes the direction of preference without being operationalized as a score.

## Secondary objections (optional)

- The Python 3.11 default rests partly on prevalence ("existing code can benefit repeatedly"), while the note admits its checks are "not a survey of how often each reason applies." A usage-weighted measure is exactly what would settle that. The note answers this adequately by naming the condition under which the default would be challenged ("If such blockers were widespread and costly"), so this is weaker than the main attack.
- The `AGENTS.md` example is a self-described "possible loss, not an observed failure." It illustrates the reversal test but gives no evidence that the test has guided an actual Commonplace decision. That is acceptable for illustration, but the note's evidence that the method works in this KB is the single tag-coverage trace.
