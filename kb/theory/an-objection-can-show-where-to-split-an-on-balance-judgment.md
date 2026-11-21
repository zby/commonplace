---
description: "Use a Python release comparison to distinguish a split that reveals a new constraint from one that merely names an unmeasured loss."
type: types/note.md
traits: [title-as-claim]
tags: [evaluation, judgment-governed-self-improvement]
---

# An objection can show where to split an on-balance judgment

An [on-balance judgment](./on-balance-judgments-can-guide-improvement-without-a-global-measure.md) need not begin with a list of effects or measures. Start with the whole comparison. An objection identifies a part worth splitting when a plausible answer could change the verdict. Stating the disputed assumption separately makes the reasoning [addressable](./definitions/addressable-theory.md): a critic can challenge that assumption without rejecting the whole comparison. The split helps only if it exposes evidence or a constraint that was missing from the whole judgment.

Consider the [choice of Python 3.11 over 3.10](./on-balance-judgments-can-guide-improvement-without-a-global-measure.md#a-release-judgment-python-311-over-310) as the default for continuing application development. Existing programs can run faster, maintained projects gain library facilities, and a project blocked by a removed interface can stay on 3.10. Why not prefer 3.11?

**“Staying on 3.10 isn't free. How does a project know it is blocked?”** Separate the cost of *discovering* a broken dependency from the cost of *deploying* with one. Suppose a check catches that dependency before deployment. Everyone who checks pays for the check, including projects that migrate successfully. But a project that catches the problem and stays on 3.10 does not also pay for a failed deployment. Counting both losses against that project would overstate the case against the upgrade.

For illustration, let a clean migration gain `g` per project over the period considered, a check cost `c`, and the blocked share be `p`. If all projects check and the check catches every blocker, their mean gain net of checks is `(1 − p)g − c`. This is not an estimate for Python. It shows why the cost of checking even the projects that migrate successfully matters to the default. No finer breakdown of the gains is needed if even their lower bound covers the checks and all remaining losses. If the comparison is close, the size of the gains matters.

Keep shared quantities together when reporting what the split reveals. Suppose one part of a migration saves `x + 1` hours and another costs `x` hours, with `x` between zero and ten. Reporting a saving of one to eleven hours and a cost of zero to ten suggests a loss is possible. Both estimates depend on the same `x`, so the net saving is exactly one hour.

**“What about changes the tests miss?”** A branch can stay whole if its *combined* downside cannot erase the advantage. Showing that each loss would be small on its own is not enough. Tests and a route back to 3.10 identify which losses could remain; neither bounds their size. A silent error might affect many outputs before anyone notices it. Without grounds to bound that loss, report the default preference with its assumption, not as a demonstrated improvement across projects.

The same reasoning applies inside a branch. Splitting the check cost into staff time and machine time helps if those quantities can be estimated and the difference matters to the choice. Otherwise the split adds two unknowns in place of one. The point is to learn enough about the disputed part to tell whether it could change the whole judgment, not to finish an inventory of the release.
