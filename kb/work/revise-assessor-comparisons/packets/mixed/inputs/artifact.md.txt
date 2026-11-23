---
description: "How to decide whether to keep a change when gains and losses fall on different tasks, and which uncertainties justify further investigation before acting"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [evaluation]
---

# On-balance judgments can guide improvement without a global measure

Is Python better than it was twenty years ago? “On balance, yes” is a defensible answer even from someone who can name programs made worse by the transition. Consider text handling. In Python 2, adding a byte string to a Unicode string could pass a test on an ASCII name, then fail on a name containing an accented letter: the implicit conversion assumed ASCII. Python 3 rejects the mixed addition even on the first name. For the author of a new program, that early failure exposes a decoding decision the test would otherwise miss. For someone running a working Python 2 script unchanged on the same old files, the incompatibility is a loss.

Those facts do not decide twenty years of language development. They do show what a reason for preferring one version looks like: identify work that changed, say for whom, and explain why the difference matters. Two programmers can agree on the behavior yet choose different versions for their projects. Neither needs a score for every Python release before choosing the next one to use.

A narrower question admits a firmer answer. Run a script named `random.py` that imports `random` and calls `random.randrange(10)`. CPython 3.12.8 reported a likely circular import. CPython 3.13.1 named the local file that hid the standard library module and suggested renaming it. Renaming it to `draw.py` fixed the failure on both versions. Keep the newer diagnostic: its extra words give the person facing the error a repair that works. That resolves the choice between messages, not the choice between releases.

## A release judgment: Python 3.11 over 3.10

Would we take Python 3.11 as the default for continuing application development, given the choice between those two releases? **On balance, yes.** That is a choice between whole releases: we cannot take the new interpreter and libraries while keeping every old interface. Four checks on local CPython 3.10.16 and 3.11.11 builds illustrate what enters the judgment.

| What changed | Who gains or loses |
|---|---|
| The same calculation ran faster without a source edit. In eight paired runs, alternating which interpreter went first, 500 evaluations of `sum(x*x for x in range(10000))` took a median 0.46 seconds on 3.10 and 0.32 on 3.11. | An existing program can benefit without adopting a new feature. This checks one workload on two builds, not the speed of Python applications in general. |
| 3.11 supplies `asyncio.TaskGroup`. In a two-task check, one task failed; its waiting sibling ran its cleanup before the caller handled the failure. 3.10 did not supply that facility. | Service authors who want this failure behavior can rely on the library rather than implement or import the coordination themselves. |
| The standard library in 3.11 parsed a TOML configuration with `tomllib`; the module was absent in 3.10. | A tool that reads TOML can drop a parser dependency if it no longer targets 3.10. Parsing TOML itself is not a new capability. |
| Calling `inspect.getargspec` on a function returned its arguments on 3.10, with a deprecation warning. The same call failed on 3.11 because the interface was gone. | An application can stop working on upgrade even if the offending call belongs to a dependency. A warning gave maintainers notice; it did not do the repair for them. |

The case for 3.11 is not that the table has three gains and one loss. One indispensable broken dependency can outweigh all three gains for its users. The reason to prefer 3.11 as a **default** is that existing code can benefit repeatedly, and maintained projects gain library support they can adopt when it serves them. The compatibility cost falls on identifiable callers: for a particular application we can test its dependencies before deciding to move it. If an essential dependency cannot be repaired, keeping that application on 3.10 is consistent with preferring the 3.11 release overall. If such blockers were widespread and costly, that would challenge the default itself. These checks give reasons for the judgment, not a survey of how often each reason applies.

Some comparisons turn less on uncertainty than on **whose work the decision serves**. Suppose a public library can staff either Tuesday morning or Saturday morning, but not both. After a trial, Saturday drew twice as many visits; Tuesday had been the only session one group of residents could reach. Even a perfect attendance count would not decide which hours to keep. If the purpose is to serve the most visits, keep Saturday. If the library has undertaken to preserve access for residents with no alternative, the same evidence favors keeping Tuesday or finding different hours to cut. Asking for another month of counts would miss the disagreement. This is a hypothetical case; what transfers to a KB decision is the question of whose loss a higher total can hide.

## What analysis can settle

A timing test can tell us which interpreter ran a particular program faster. An estimate of how often that program will run can bound the likely saving, but cannot settle future use. Even with both quantities in hand, deciding whether the saving is worth someone else’s porting effort is a judgment about value. Analysis can expose that trade-off; it cannot supply the weights merely by assigning each feature a score.

Three choices fix the comparison:

- **What is the alternative?** A better error message settles which message to show. Adopting the release means taking its other changes too.
- **Who gains, and who bears the loss?** More library visits can coexist with fewer residents able to visit at all.
- **Over what period?** Porting a dependency costs effort now. A faster interpreter can save time repeatedly, but only for work the team will continue to run.

**For the decision at hand, investigate an unknown only if a plausible answer could reverse the choice.** If an application depends on a library that might break on upgrade, test that dependency. A more precise timing result will not make a broken dependency run. When the preference holds across the plausible answers, we can act without settling every uncertainty.

## What Commonplace chooses to count

**For Commonplace, we choose changes by asking whether they yield more useful and better-warranted knowledge work for the human judgment spent, on balance.** We choose this objective because we repeatedly have to decide whether a gain is worth the judgment it takes to build, operate, and maintain the change. Automation alone does not answer that question. This is a practical commitment about the work we value, not a claim that every project should use the same measure.

A total order would rank any two versions. The evidence supports only some comparisons: it may show what a new validator caught but not how often the old one missed something important. Even complete observations would leave a question of value: how many routine mistakes avoided are worth one failed high-stakes task? The operator and users supply that judgment. A partial order can represent the preferences we can defend under a consistent set of priorities. It describes the limits of the ranking; it does not do the weighing or guarantee that a single stable ranking exists.

## What to do with an incomplete comparison

First ask what improved over the predecessor. Use of a new instruction shows uptake, not a gain. A review gate that catches the same ambiguity as the old review has not thereby improved detection. By contrast, the [tag coverage trace](./evidence/tag-readme-trace-observed-causal-connection.md) records a validator finding a member the documented search missed. That establishes a local gain. Whether maintaining marked heads is worth the effort depends in part on who relies on them to stop searching.

Now suppose one line in `AGENTS.md` reliably directs agents to instructions for a task they previously mishandled. Other prompts load that line too. On a task already near the limit of what the agent can use effectively, even one line could tip a correct answer into failure. The cost there would be failure and rework, not just the extra text. That is a possible loss, not an observed failure.

This distinction guides a decision. If the routing benefit is worth keeping across plausible estimates of how often important tasks run near that limit, keep the line. If a plausible frequency would reverse the preference, investigate those tasks; knowing the precise length of the line will not settle it. If the evidence supports only the routing gain, leave the overall judgment open. The reason for today's choice also tells us when to revisit it: a longer table or a different mix of tasks can change the balance. Compare the whole table with its earlier, shorter version rather than assuming that a succession of reasonable additions remains reasonable in aggregate.

Known requirements need not be weighed afresh. A [factory comparison fixed before development](./a-better-factory-claim-compares-operative-states.md) can require a gain while forbidding deterioration beyond a threshold on prior capabilities. A pass answers that defined question; an on-balance judgment does not override a binding requirement. Nor does preferring the successor identify which component deserves credit: [a comparison tests only the contrast it actually makes](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).

An agent can offer reasons for such a preference without calculating a global score. Ask which work changed, whose costs count, and what observation would change its recommendation. Those reasons can be checked independently of who offered them. Their availability makes a judgment criticizable; it does not establish that any particular agent judges well.

---

Relevant Notes:

- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: why the objective must be identifiable independently of the change it is used to judge
