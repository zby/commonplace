# A trial-cost decision before any outcome exists

This worked case was recorded on 2026-10-05 from the operator's direction and
the [retained synthesis distinction protocol](../../reports/retained/synthesis-distinction-pilot-20261005/protocol/README.md).
It tests whether a small ordinary-work record can preserve a useful decision
without presenting a planned comparison as evidence that the treatment works.

## Episode at the decision point

| Item | Contemporaneous record |
|---|---|
| Decision | Replace the proposed 36–48-call synthesis/review pilot with an eight-call feasibility check. Continue the use-and-outcome records investigation as the broader way to steer with less experimental work. |
| Idea used | A controlled trial should be requested when its expected contribution to a later decision warrants its cost; ordinary observations can guide reversible next steps while their causal limits remain explicit. This is the workshop's working direction, not an adopted rule. |
| Conditions | One frozen Dynamic Cheatsheet case; control and combined-treatment instructions; `gpt-6-luna` at medium effort; no model trials had run when the decision was made. |
| Observed input | The full plan required 36–48 independent model jobs. A prepared first-round packet was about 343 KB, including about 176 KB of required instructions and records and 165 KB of optional source. The initial 200,000-token cumulative ceiling was recognized as too tight because repeated tool outputs can increase usage; preflight raised it to 1,000,000. These are preparation facts, not measured job usage. |
| Human judgment | The operator judged the full experiment costly and preferred a smaller run to see whether the approach behaves as intended, while shifting method work toward information gained from ordinary operation. |
| Expected value of the smaller check | It may expose failure to preserve the known distinction, failure to catch the known overclaim, a false objection to a qualified claim, or material coverage loss. It cannot estimate reliability or isolate which treatment paragraph caused a difference. |
| Outcome as of recording | The plan and scoring guide were narrowed to eight calls. No synthesis or review outcome exists yet. The cost of an executed job is unknown. |
| Next observation | Record actual call count, time, tokens, outputs, scoring judgments, and any decision about provisional use or a larger trial. Keep the initial expectation above unchanged when adding those results. |

The [experiment plan](../../reports/retained/synthesis-distinction-pilot-20261005/protocol/README.md),
[scoring guide](../../reports/retained/synthesis-distinction-pilot-20261005/protocol/scoring.md), and
[execution preflight](../../reports/retained/synthesis-distinction-pilot-20261005/protocol/execution-preflight.md)
carry the detailed protocol and preparation evidence. A session pointer is
not needed to recover the decision and its grounds from this record.

## What this case tests in the record design

One episode bears on at least two ideas: whether a narrow synthesis prompt
change is worth further testing, and whether the decision process can use
cost and operational feedback before running a controlled trial. The episode
does not attribute a future favorable result to either idea. It also
distinguishes three different outcomes: plan changed, trial result pending,
and later production benefit unknown.

The compact table and linked detailed protocol fit in one workshop file;
three storage layers need not mean three files. If later readers need the
exact model trace, the retained experiment report must own it. If they need
only the decision and its limits, this compact record should suffice. That
access claim remains to be tested with a later reader who did not witness the
session.

This case suggests a candidate information-efficiency question for the
workshop: **What is the least costly next observation that could change the
actual decision?** Answering it requires naming the decision, the live
uncertainty, the evidence already available, and the inference the proposed
observation would permit. Stakes, reversibility, observability, and total
capture/retrieval cost affect the choice. The question is a working heuristic,
not a numeric score or a default requirement to run a trial.

The delayed-outcome problem is visible already. `Plan changed` is an observed
process outcome; `treatment works` is unobserved. A later result should be
appended with its date and evidence link rather than replacing this initial
record. If the trial is never run, the record should say so instead of
silently treating absence of a failure as success.

## Follow-up observation, 2026-10-05

The first control writer reached an output in 182.7 seconds but reported
1,283,864 cumulative input and output tokens, above the predeclared
1,000,000-token ceiling. Most input tokens were cached. The [retained
execution record](../../reports/retained/synthesis-distinction-pilot-20261005/README.md)
preserves the trace and exact attempt. This is a resource and execution
observation, not a favorable or unfavorable treatment outcome. The control
draft was not semantically scored, and no treatment writer or reviewer had
run when this follow-up was recorded.

The observation changes the next decision: continuing the eight-call schedule
under the same ceiling would mark an otherwise completed writer incomplete.
A larger ceiling or fewer model turns would require a separately identified
protocol version. The record keeps that revision question distinct from the
original decision to run a smaller check.

## Trial outcome observed later on 2026-10-05

The execution changed a delivery detail common to both arms: version 2 put
the required documents in the initial prompt and kept source files available
for targeted checks. All eight planned version 2 calls completed in 332.32
seconds of aggregate model runtime and 1,950,094 reported input-plus-output
tokens, including 1,563,392 cached input tokens. The [retained report](../../reports/retained/synthesis-distinction-pilot-20261005/README.md)
keeps every output, trace and [score](../../reports/retained/synthesis-distinction-pilot-20261005/scores.md).
The measured total is much smaller than the original 36–48-call plan would
have required at similar per-call cost, but it is not a controlled cost
estimate for that unrun plan.

The treatment writer omitted the intended retrieval-synthesis distinction,
as did the control writer. Neither reviewer caught the known overclaim in the
original fixed draft. The treatment reviewer correctly accepted the qualified
draft, while the control reviewer falsely blocked it. Both new syntheses
omitted other material overview requirements. Under the predeclared rule this
does not warrant adopting the combined treatment. It also does not show that
either instruction always fails: each diagnostic case and arm ran once.

This episode now has a process outcome (the smaller check ran), a resource
outcome (measured cost and a delivery revision), and a bounded method outcome
(no promising signal in this case). Production benefit remains unobserved.
The first resource failure justified a narrower delivery change before
further calls; the final semantic result does not justify extending this
trial until a preferred answer appears. This is the kind of decision that a
compact use record can convey without treating reuse or execution as
favorable evidence.
