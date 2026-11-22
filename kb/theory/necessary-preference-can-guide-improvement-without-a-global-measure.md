---
description: "How to decide whether to keep a change when gains and losses fall on different tasks, and which uncertainties justify further investigation before acting"
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [evaluation, self-improving-systems, robust-comparison]
---

# Necessary preference can guide improvement without a global measure

Is Python better than it was twenty years ago? “On balance, yes” is a defensible answer even from someone who can name programs made worse by the transition. Consider text handling. In Python 2, adding a byte string to a Unicode string could pass a test on an ASCII name, then fail on a name containing an accented letter: the implicit conversion assumed ASCII. Python 3 rejects the mixed addition even on the ASCII name. For the author of a new program, that early failure exposes a decoding decision the test would otherwise miss. For someone running a working Python 2 script unchanged on the same old files, the incompatibility is a loss.

Those facts do not decide twenty years of language development. They do show what a reason for preferring one version looks like: identify work that changed, say for whom, and explain why the difference matters. Two programmers can agree on the behavior yet choose different versions for their projects. Neither needs a score for every Python release before choosing the next one to use. A comparison of this kind can choose between versions without a global measure, and for the decision at hand, an unknown is worth investigating only if a plausible answer could reverse the choice.

A narrower question admits a firmer answer. Run a script named `random.py` that imports `random` and calls `random.randrange(10)`. CPython 3.12.8 reported a likely circular import. CPython 3.13.1 named the local file that hid the standard library module and suggested renaming it. Renaming it to `draw.py` fixed the failure on both versions. Keep the newer diagnostic: its extra words give the person facing the error a repair that works. That resolves the choice between messages, not the choice between releases.

## A release judgment: Python 3.11 over 3.10

Would we take Python 3.11 as the default for continuing application development, given the choice between those two releases? As a default for maintained projects, **on balance, yes**, assuming breaking removals are rare enough to catch before moving. That is a choice between whole releases: we cannot take the new interpreter and libraries while keeping every old interface. Four checks on local CPython 3.10.16 and 3.11.11 builds illustrate what enters the judgment.

| What changed | Who gains or loses |
|---|---|
| The same calculation ran faster without a source edit. In eight paired runs, alternating which interpreter went first, 500 evaluations of `sum(x*x for x in range(10000))` took a median 0.46 seconds on 3.10 and 0.32 on 3.11. | An existing program can benefit without adopting a new feature. This checks one workload on two builds, not the speed of Python applications in general. |
| 3.11 supplies `asyncio.TaskGroup`. In a two-task check, one task failed; its waiting sibling ran its cleanup before the caller handled the failure. 3.10 did not supply that facility. | Service authors who want this failure behavior can rely on the library rather than implement or import the coordination themselves. |
| The standard library in 3.11 parsed a TOML configuration with `tomllib`; the module was absent in 3.10. | A tool that reads TOML can drop a parser dependency if it no longer targets 3.10. Parsing TOML itself is not a new capability. |
| Calling `inspect.getargspec` on a function returned its arguments on 3.10, with a deprecation warning. The same call failed on 3.11 because the interface was gone. | An application can stop working on upgrade even if the offending call belongs to a dependency. A warning gave maintainers notice; it did not do the repair for them. |

The case for 3.11 is not that the table has three gains and one loss. One indispensable broken dependency can outweigh all three gains for its users. The reason to prefer 3.11 as a **default** is that existing code can benefit repeatedly, and maintained projects gain library support they can adopt when it serves them. A loss like the removed `getargspec` can be found before moving: we can test a particular application's dependencies first. If an essential dependency cannot be repaired, keeping that application on 3.10 is consistent with preferring the 3.11 release overall. If such blockers were widespread and costly, that would challenge the default itself. These checks illustrate the reasons for the judgment, not a survey of how often each reason applies. Without evidence bounding how widespread blockers or uncaught regressions are, they support adopting 3.11 as a default under that stated assumption, not claiming a demonstrated improvement across projects. [Separating discovery cost from deployment failure](./an-objection-can-show-where-to-split-a-comparison.md) shows what a challenge to that judgment can settle and what the tests leave open.

## What analysis can settle

Several precise measures can support the same judgment even when we leave the exact weights open. Suppose a trial of a revised instruction finds that it helps on 90 tasks, hurts on 10, and makes no difference elsewhere. Suppose those frequencies reflect expected use. For a measure that adds up gains and losses across tasks, the break-even point is clear. The revision comes out ahead whenever the average loss on a harmed task is less than nine times the average gain on a helped task. Every positive ratio below nine gives a precise weighting that favors the revision.

The practical question is whether a ratio of nine or more is plausible for this work. If each gain saves a manual check and each loss adds a comparable check, we may have good grounds to rule that out while leaving the exact ratio undecided. If a loss can invalidate a day's work, the same task counts leave the choice open. Evidence about the consequences tells us which weights deserve consideration.

A timing test can tell us which interpreter ran a particular program faster. An estimate of how often that program will run can bound the likely saving, but cannot settle future use. Even with both quantities in hand, deciding whether the saving is worth someone else’s porting effort is a judgment about value. Analysis can expose that trade-off; it cannot supply the weights merely by assigning each feature a score.

Some comparisons turn less on uncertainty than on **whose work the decision serves**. Suppose a public library can staff either Tuesday morning or Saturday morning, but not both. After a trial, Saturday drew twice as many visits; Tuesday had been the only session one group of residents could reach. Even a perfect attendance count would not decide which hours to keep. If the purpose is to serve the most visits, keep Saturday. If the library has undertaken to preserve access for residents with no alternative, the same evidence favors keeping Tuesday or finding different hours to cut. The case is hypothetical, but a KB decision faces the same question of whose loss a higher total can hide.

Three choices fix the comparison:

- **What is the alternative?** A better error message settles which message to show. Adopting the release means taking its other changes too.
- **Who gains, and who bears the loss?** The library hours above show the question.
- **Over what period?** Porting a dependency costs effort now. A faster interpreter can save time repeatedly, but only for work the team will continue to run.

**For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice.** If an application depends on a library that might break on upgrade, test that dependency. A more precise timing result will not make a broken dependency run. When the preference holds across the plausible answers, we can act without settling every uncertainty.

## What a claim of improvement asserts

The cases above share a form. Once those three choices fix the comparison, **a step is an improvement when every compatible measure of the work scores the successor higher than the predecessor.** No measure is selected. A measure here is a whole way of scoring the work, such as one loss-to-gain ratio. It is not one dimension of the work, such as cost: if the success rate rises while cost and reliability stay the same, every measure that gives success any weight scores the successor higher. A measure is **compatible** when its treatment of gains and losses agrees with the purpose of the work and with the preferences established so far, whichever version it favors.

The rule is old and standard: rank two options only where every member of a set of evaluations agrees. Pareto dominance and stochastic dominance are familiar cases. Stochastic dominance ranks one gamble above another when every increasing utility function prefers it, and restricting the set to risk-averse utilities orders more pairs. We take two terms from a later statement of the rule in multiple-criteria decision analysis. [Greco, Mousseau and Słowiński](../sources/greco-ordinal-regression-revisited.ingest.md) call a preference **necessary** when it holds under every value function compatible with the decision maker's stated judgments, and **possible** when it holds under at least one. An improvement in the sense above is the strict form: every compatible measure scores the successor higher, not merely at least as high. The size of the compatible set fixes how much the rule can order. With one measure in the set, the rule is selection by a single score. With no preference information, the paper shows that necessary preference is plain dominance, criterion by criterion, which leaves most real changes unordered. Each established preference removes measures from the set, and more pairs become ordered.

**TODO:** The older traditions named here come from the agent's training data, not from a systematic search. Search each one and compare it with the rule as stated here: Pareto dominance, majorization, stochastic dominance, utility theory without complete preferences, supervaluation, Sen's intersection orderings, dominance with partially known weights, and imprecise probability. For each, record what set the rule ranges over, how membership in the set is justified, and what the tradition says about deciding a pair the rule leaves unordered.

Two things differ here. In the paper the criteria are fixed and a person supplies the judgments. Here the purpose of the work supplies the first constraints, and an objection can introduce a criterion nobody had listed. That widens the set before later preferences narrow it, so a verdict of improvement can be withdrawn.

If a little extra reading on every task counts against adding a routing line, then time saved across tasks must also count in favor of removing one. The saving need not be large enough to justify removal; it cannot be dismissed merely because no reader reports a line they no longer have to read.

In the trial of the revised instruction, the compatible measures are the loss-to-gain ratios that are plausible for the work. If all of them lie below nine, every one favors the revision. So does any weighted average of them, so nobody has to say how the measures would be combined.

Report the result of the comparison:

- **Improvement.** Every compatible measure favors the successor: it is necessarily preferred.
- **Loss.** Every compatible measure favors the predecessor.
- **Tie.** Every compatible measure gives the versions equal scores: for instance, two changes that differ only in aspects none of the compatible measures track, or whose gains and losses exactly offset under every admitted weighting. Neither version is better for the declared work.
- **Better on some measures, tied on the rest.** No compatible measure favors the predecessor. This can justify the step, but it falls short of improvement under every measure. Report the converse just as precisely: worse on some, tied on the rest.
- **Open.** Some measures favor each version, so each is only possibly preferred, or the evidence does not yet establish the verdict. Say which. For example, a refactoring may make future edits cheaper without changing current behavior. Later edits can test that forecast; they cannot decide how much the team values those savings against the cost of the rewrite.

A possible preference is not enough. Some compatible measure favors the step, but another compatible measure might favor undoing it, and then the step and its reversal would both count as improvements.

Purpose enters when we decide which measures are compatible. The two purposes for the library admit different measures, and each gives a definite answer. Excluding a measure takes an argument from purpose. For the choice of a default Python release, a measure that counts only the worst-off project is not compatible, because a project with an unrepairable dependency can stay on 3.10. The same kind of measure would be compatible where the people harmed cannot avoid the loss.

Shared purpose still leaves genuine disagreement over time horizons, tolerance for rare severe failures, or how to weigh author effort against maintainer effort. Narrowing the set of compatible measures merely to force agreement smuggles a weighting back in without defending it. Keeping the set honest means many consequential trade-offs finish **Open**. Requiring every compatible measure to agree still guides improvement there: it rules out options that lose across the board, isolates the unknowns that could reverse a choice, and separates what evidence established from what an operator still has to decide.

An open verdict does not forbid the step. We can still take it as a decision, as the deletion rule below shows. We should then report a decision and not a demonstrated improvement. If we can recognize and correct a mistake, [reversibility can change the judgment itself](./reversibility-can-favor-a-change-by-limiting-future-loss.md) by limiting losses to later work.

## What Commonplace chooses to count

**Commonplace's objective is more useful and better-warranted knowledge work for the human judgment spent.** We choose this objective because we repeatedly have to decide whether a gain is worth the judgment it takes to build, operate, and maintain the change. Automation alone does not answer that question. This is a practical commitment about the work we value, not a claim that every project should adopt it.

Those three terms can pull in opposite directions. Stricter checks can raise warrant while consuming more human judgment; looser checks can speed up useful work at the risk of missed errors. The objective therefore bounds which measures are compatible rather than collapsing them into one score. We do not need to rank every version of Commonplace to decide whether to keep a change. A validator finding a note that the old search missed is evidence of a gain. How often that gain matters is a question about use. Whether it is worth the upkeep is a judgment for the people who rely on the index and those who maintain it. The objective tells us what to consider; it does not calculate the answer.

## What to do with an incomplete comparison

First ask what improved over the predecessor. Use of a new instruction shows uptake, not a gain. A review gate that catches the same ambiguity as the old review has not thereby improved detection. By contrast, the [tag coverage trace](./evidence/tag-readme-trace-observed-causal-connection.md) records a validator finding a member the documented search missed. That establishes a local gain. Whether maintaining marked heads is worth the effort depends in part on who relies on them to stop searching.

Now suppose one line in `AGENTS.md` reliably directs agents to instructions for a task they previously mishandled. Other prompts load that line too. On a task already near the limit of what the agent can use effectively, even one line could tip a correct answer into failure. The cost there would be failure and rework, not just the extra text. That is a possible loss, not an observed failure.

This asymmetry is common in KBs and agent systems: gains are usually local and visible, such as a caught omission or a fixed routing error, while costs such as context load, upkeep, and rule interaction are diffuse and silent. Treating only observed failures as real losses biases these comparisons toward accretion, so diffuse costs belong in the plausible loss estimates even when no single task reports them.

If the routing benefit is worth keeping across plausible estimates of how often important tasks run near that limit, keep the line. If a plausible frequency would reverse the preference, investigate those tasks; knowing the precise length of the line will not settle it. If the evidence supports only the routing gain, leave the overall judgment open. The reason for today's choice also tells us when to revisit it: a longer `AGENTS.md` table or a different mix of tasks can change the balance. Under a fixed set of compatible measures, a chain of genuine **Improvements** stays an improvement: every measure rises at every step, so the final state beats the first on all of them. Aggregate degradation enters when steps were **Open** decisions, when local estimates missed nonlinear cumulative effects such as context saturation, or when the task mix or compatible measures shifted. Compare the whole `AGENTS.md` table with its earlier, shorter version rather than assuming that a succession of locally accepted additions remains an improvement in aggregate.

**Leaving the comparison open does not mean leaving the design undecided.** Commonplace needed a rule for proposals whose problem had gone away. [ADR 085](../reference/adr/085-withdrawn-proposals-are-deleted.md) chose to delete a withdrawn proposal after extracting anything still useful. That keeps the list of open proposals accurate. The decision accepts a loss: someone with a shallow clone may no longer have the old text. With more resources we could try deletion, archiving, and marking proposals in place across comparable collections, then measure the effort spent reviewing stale entries or recovering old designs. We can commit to deletion without claiming it won that comparison. If recovery becomes a recurring cost, we have a reason to reopen the decision. Even a well-funded trial could tell us how often recovery matters without deciding how much to value it.

Known requirements need not be weighed afresh. A [factory comparison fixed before development](./a-better-factory-claim-compares-operative-states.md) can require a gain while forbidding deterioration beyond a threshold on prior capabilities. A pass answers that defined question; a comparison across compatible measures does not override a binding requirement. Nor does preferring the successor identify which component deserves credit: [a comparison tests only the contrast it actually makes](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).

An agent can offer reasons for such a preference without calculating a global score. Ask which work changed, whose costs count, and what observation would change its recommendation. The factual parts of those reasons, such as which work changed, can be checked independently of who offered them; the weighing of whose costs count cannot be checked that way. Their availability makes a judgment criticizable; it does not establish that any particular agent judges well.

---

Relevant Notes:

- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: why the objective must be identifiable independently of the change it is used to judge
