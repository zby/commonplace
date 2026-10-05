# A trial-cost decision before any outcome exists

This worked case was recorded on 2026-10-05 from the operator's direction and
the [synthesis distinction workshop](../synthesis-distinction-experiment/README.md).
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

The [experiment plan](../synthesis-distinction-experiment/README.md),
[scoring guide](../synthesis-distinction-experiment/scoring.md), and
[execution preflight](../synthesis-distinction-experiment/execution-preflight.md)
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
