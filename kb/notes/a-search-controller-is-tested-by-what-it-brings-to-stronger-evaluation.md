---
description: "A search controller should be evaluated by the branches and probes it routes into stronger evaluation, not by treating every provisional judgment as an acceptance claim"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, evaluation, self-improving-systems]
---

# A search controller is tested by what it brings to stronger evaluation

A search controller decides which branches or probes receive further work. It
does not itself establish that those branches are correct or worth adopting.
Its evaluation should therefore follow what it routes into stronger evaluation.

A useful controller brings forward branches that later produce valuable
candidates, discriminating evidence, informative failures, or improved
recovery. A false lead does not individually refute it, just as one successful
branch does not establish it. The comparison concerns the distribution of
consequences produced by its routing decisions.

The controller can be compared with alternatives under matched tasks,
resources, and downstream evaluation. This does not require knowing the best
branch in the full counterfactual search space, which is normally unavailable
in the open-ended setting.

## Scope

- Stronger evaluation may be immediate, delayed, empirical, or formal. The
  claim does not select one evaluator.
- Search-controller quality does not establish that any accepted result was
  adequately warranted; acceptance remains a separate judgment.

---

Relevant Notes:

- [Lightweight search control allocates further search without licensing adoption](./lightweight-search-control-does-not-license-adoption.md) — grounds: supplies the limited-authority controller whose output is being evaluated
- [Open-ended improvement must allocate search before decisive evaluation is available](./open-ended-improvement-allocates-search-before-evaluation.md) — grounds: explains why comparison cannot assume exhaustive evaluation of every branch
- [Backtracking keeps lightweight search control provisional](./backtracking-keeps-lightweight-search-control-provisional.md) — mechanism: explains how a mistaken branch can still improve recovery while remaining provisional
- [A failure explanation becomes search control only when it changes a later branch decision](./failure-explanation-changes-later-branch-decisions.md) — mechanism: identifies when an informative failure actually changes subsequent routing
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds: explains why inspectable evidence and failures are valuable downstream consequences apart from acceptance
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: limits controller attribution to comparisons that vary the controller rather than a larger treatment bundle
