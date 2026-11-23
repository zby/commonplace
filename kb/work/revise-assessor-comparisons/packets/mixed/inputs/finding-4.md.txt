---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: b9f1acc4a87549f288e2be90a8db8423
completed-at: '2026-11-20T18:55:15Z'
findings:
- scope: passage
  quotes:
  - This is a practical commitment about the work we value, not a claim that every
    project should use the same measure.
  reason: Defensive redundancy. The paragraph already opens with 'For Commonplace,
    we choose' and gives a Commonplace-specific reason ('because we repeatedly have
    to decide...'), so the scope is already local and chosen. The trailing sentence
    guards against a universal reading that the opening already rules out. Cut it,
    or keep only 'This is a practical commitment about the work we value' if the reader
    needs a stance marker before the order-theoretic paragraph.
  level: warn
- scope: passage
  quotes:
  - it does not do the weighing or guarantee that a single stable ranking exists
  reason: The 'does not do the weighing' half repeats the sentence two before it ('The
    operator and users supply that judgment') and the earlier 'Analysis can expose
    that trade-off; it cannot supply the weights'. Only the stable-ranking admission
    is new. Trim it to '...; it does not guarantee that a single stable ranking exists.'
  level: warn
- scope: passage
  quotes:
  - A better error message settles which message to show. Adopting the release means
    taking its other changes too.
  reason: 'Each of the three bullet glosses mostly repeats a point the note has already
    made: messages versus releases ends the random.py paragraph, visits versus residents
    is the library case, and saving time repeatedly echoes the paragraph just above.
    The bold questions do work as a reusable checklist, but the glosses may be longer
    than a back-reference needs. I am unsure whether the recap adds enough uptake
    to keep the glosses at their current length.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/b9f1acc4a87549f288e2be90a8db8423/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/59e29f246272bf63faa7f47a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/b9f1acc4a87549f288e2be90a8db8423/outputs/review.md
raw-output-sha256: 0f7ded75793e2f8a56819b847359a45fef99f8868b7f605b4b5783a3ea10b2c2
---

# Review

## Summary

Most of the note earns its space. The Python 2/3 opening, the `random.py` contrast, the 3.11 table and its interpretation, the library case, the investigate-only-if-it-could-reverse rule, the `AGENTS.md` worked case and the binding-requirements paragraph each add a distinct example, boundary or decision rule. The closing paragraph restates the questions, but it turns them into a stance for agents and adds an admission ("does not establish that any particular agent judges well"). The conclusion check therefore leaves it alone.

Two clauses fail the defensive-redundancy test. In each, the qualification guards against a misreading that the nearby text already rules out. Both fixes are small trims, not restructuring.

One non-obvious pass: "That is a possible loss, not an observed failure" may look like a hedge after "could tip". It stays because the next paragraph opens "This distinction guides a decision" and depends on the contrast between observed and possible effects.

The bullet glosses under "Three choices fix the comparison" are marked INFO, not WARN. The questions are new as a checklist, but their glosses mainly point back to earlier examples. Whether that recap helps memory or just takes space is a judgment call.
