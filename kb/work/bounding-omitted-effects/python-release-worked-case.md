# Worked case: is a new Python version an improvement?

Written 2026-11-21 by an agent (claude-fable-5-2) at the operator's request,
to record how the definition would work on one case. The facts about Python
3.10 and 3.11 are the four checks in the
[on-balance note](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md#a-release-judgment-python-311-over-310).
Every number below is illustrative. Nothing here was measured.

## The definition applied

A step is an improvement on balance when, for every reasonable measure, the
successor scores higher than the predecessor. No measure is selected. The
[workshop framing](./README.md#the-definition) gives the definition
and the reasons for it.

This case shows the definition working on one release: a measure that favours
the step, measures that do not, and how deciding which of them are reasonable
gives the verdict.

## Step 1 — fix the comparison

The on-balance note asks three things before any measure is considered.

- **The alternative.** Python 3.11 against 3.10 as whole releases. Nobody can
  take the faster interpreter and keep the removed interface.
- **Whose work.** People continuing application development. A project may
  stay on 3.10 when it has a reason.
- **The period.** The time the project keeps running its code.

The question is therefore: is 3.11 the better default?

## Step 2 — one precise measure

Take one simple measure. For each project, add up what the default costs or
saves over the period, in hours.

- A project that moves cleanly gains $g$: faster runs, and library support
  such as `asyncio.TaskGroup` and `tomllib` when it wants them.
- A project with a blocking dependency, such as a call to the removed
  `inspect.getargspec`, loses $L$ if it moves and breaks.
- A share $p$ of projects is blocked.

Under this measure 3.11 is the better default when $(1-p)\,g > p\,L$. The
break-even ratio is $L/g = (1-p)/p$. With one project in ten blocked, that is
nine: the same shape as the 90/10 example in the note.

We never have to say what $g$ is. Any $g$ and $L$ on the right side of the
boundary give a precise measure that favours 3.11. This shows that such
measures exist. It does not yet show an improvement.

## Step 3 — a measure that says the opposite

Existence is not enough. Other measures show that 3.11 is worse:

- **Count only the worst-off project.** One project whose essential dependency
  cannot be repaired loses everything. Under this measure 3.10 wins.
- **Set $L$ very high.** If a broken deployment costs a week, the boundary is
  crossed at a small $p$.
- **Serve a different group.** For someone running old scripts unchanged, 3.11
  offers little and risks breakage.

If one reasonable measure favoured 3.11 and another favoured 3.10, the
verdict would be "open". So the next step is to ask which of these measures
are reasonable.

## Step 4 — which measures are reasonable

Each measure gets one question: is it reasonable for this purpose? Nobody
asks how much each measure should count.

- **The worst-off measure is not reasonable here.** The purpose is to choose a
  default. A project with an unrepairable dependency can stay on 3.10. The
  measure charges 3.11 with a loss that the default does not impose.
- **The different-group measure answers a different question.** It is
  reasonable for running archived scripts. Step 1 already said whose work
  this comparison serves.
- **The high-$L$ measure is reasonable only without a check before moving.**
  The note points out that a removed interface can be found by testing the
  application's dependencies first. With that check, a blocked project pays
  the cost of the check, $c$, and stays. The condition becomes
  $(1-p)\,g > c$.

After these three judgments, every measure left in the set favours 3.11 unless
almost every project is blocked or the check costs more than the gain. The
verdict is "improvement": the inequality holds for every reasonable measure.

No weighting over measures was needed. Each judgment was yes or no, and each
was made only because it could flip the verdict. Any weighted average of the
remaining measures also favours 3.11, so the verdict does not depend on how
they would be combined.

## Step 5 — when membership is contested

Someone can contest a judgment from step 4. For example: "many projects cannot
run a dependency check, so the high-$L$ measure stays in." That dispute matters
because it could reverse the verdict. It is settled by evidence about those
projects, or it leaves the verdict open for them.

A dispute that could not reverse the verdict is not pursued. There is no
further level to climb: the dispute is about whether one measure belongs in
the set.

## Step 6 — the effects nobody listed

A release changes hundreds of things. The note checks four. The omitted ones
are handled by an argument about channels, not by counting:

- A changed interface can affect a project only if the project or one of its
  dependencies uses it.
- Removals and deprecations are listed in the release notes.
- Running the project's tests on the new version exercises the interfaces it
  uses.

So the reach of the unlisted changes is bounded by what the project calls, and
most of it is found before moving. What stays open is behaviour that changed
without a listed removal and that no test covers.

## What the case shows

- **No measure was defined.** The verdict needed the boundary and a judgment
  about which side the plausible values fall on.
- **Judgment entered in two places.** Step 1 chose whose work counts. Step 4
  chose which measures are reasonable for that purpose.
- **The evidence does not carry the whole verdict.** The four checks show that
  each kind of gain and loss is real. They do not give $p$. The note says so:
  the checks are "not a survey of how often each reason applies". The verdict
  rests on the judgment that blockers are not widespread, and the note states
  what would overturn it.
- **Disagreement leaves the verdict open.** If reasonable measures split, for
  instance for a team that cannot test before moving, weighting them is the
  same act as choosing one measure. That is a value judgment for that team.
  The step can be taken as a decision. It should not be reported as a
  demonstrated improvement.

## Open

- The measure in step 2 is additive. A project whose gains depend on each
  other, or whose one failure blocks everything else, does not fit it.
- "Reasonable for this purpose" was argued case by case. The workshop has no
  general test for it.
- This is one agent's reconstruction. Nobody else has checked whether a
  different reasonable measure survives step 4 and favours 3.10.
