# Worked case: is a new Python version an improvement?

Written 2026-11-21 by an agent (claude-fable-5-2) at the operator's request.
Rewritten the same day after a comment from Astra, to show the process and
not only the result. The facts about Python 3.10 and 3.11 are the four checks
in the
[on-balance note](../../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md#a-release-judgment-python-311-over-310).
Every number and symbol below is illustrative. Nothing here was measured.

The [workshop framing](./README.md#the-definition) gives the definition: a
step is an improvement on balance when every reasonable measure favours the
successor. This case shows how a judge gets there without listing the
measures first.

## 1 — the whole judgment

Fix the comparison as the on-balance note does:

- **The alternative.** Python 3.11 against 3.10 as whole releases.
- **Whose work.** People continuing application development.
- **The period.** The time a project keeps running its code.

The question is whether 3.11 is the better default. The first answer is given
whole:

> Yes. Existing code runs faster without edits, and maintained projects get
> library support they can use when they want it. Some projects are blocked
> by a removed interface such as `inspect.getargspec`. Those projects can stay
> on 3.10.

Nothing has been split yet. Three branches are visible: the gains, the blocked
projects, and the hundreds of changes nobody listed.

## 2 — an objection opens one branch

The objection: "You are understating the cost to blocked projects. Staying on
3.10 avoids a broken deployment, but finding out that you are blocked costs
time."

This names a branch and says what is wrong with it. So that branch is opened.
The loss to a blocked project splits into two parts:

- **Discovery.** Every project that checks its dependencies pays a cost $c$,
  blocked or not.
- **Breakage.** A project that moves without checking, and is blocked, loses
  $L$.

The split brings a constraint the whole judgment did not have: a project that
checks first never pays $L$. With a share $p$ of projects blocked and a gain
$g$ for a clean move, the default wins when

- $(1-p)\,g > c$ for projects that check, and
- $(1-p)\,g > p\,L$ for projects that do not.

The second has a break-even ratio $L/g = (1-p)/p$. With one project in ten
blocked that is nine, the shape of the 90/10 example in the note.

**What the split changed.** The estimated loss. For projects that check, it
fell from $L$ to $c$. Evidence can now settle things it could not before: how
many projects are blocked, what a check costs, and how many projects cannot
run one.

**What the split did not change.** Whether the loss of the worst-off project
should govern the choice of a default. No measurement answers that. It is a
judgment about purpose, taken up in step 5.

Note that $p$ appears on both sides. The gain is scaled by $1-p$ and the loss
by $p$. Reporting "the gain is somewhere in this range" and "the loss is
somewhere in that range" separately would hide that they move together.

## 3 — a branch left whole, with a bound

A release changes hundreds of things. The note checks four. Nobody opens this
branch change by change. It can stay whole because its combined loss has a
bound that does not depend on counting the changes:

- **The channel.** A changed interface can affect a project only if the
  project, or one of its dependencies, uses it.
- **The check.** Running the project's tests on 3.11 exercises the interfaces
  it uses.
- **The way back.** A project that moved can return to 3.10 until it starts
  using features that only 3.11 has.

So the loss from unlisted changes is at most what slips past the project's
tests and accrues until it is noticed. That bound is small against a gain
that repeats on every run.

The contrast matters. Saying "none of these several hundred changes could
outweigh the gain by itself" would be no warrant, because together they
might. The warrant is the bound on the branch as a whole.

What stays open inside the branch: behaviour that changed without a listed
removal, that no test covers, and that fails silently.

## 4 — a branch not opened at all

The gains are not split or sized. The speed-up needs no source edit, and the
new library support is optional. No part of that branch is a loss. For the
parent, the direction is enough, unless the loss side comes close to the
break-even point. Then the size of $g$ would matter and the branch would be
opened.

## 5 — what remains a judgment about purpose

After step 2 the evidence questions are separate from one that evidence cannot
settle: which measures are reasonable for choosing a default. Three measures
favour 3.10:

- **Count only the worst-off project.** Not reasonable here. The purpose is to
  choose a default, and a project with an unrepairable dependency can stay on
  3.10. The measure charges the default with a loss the default does not
  impose.
- **Serve people running old scripts unchanged.** Reasonable for that purpose,
  and a different question from the one fixed in step 1.
- **Set $L$ very high.** Reasonable only for projects that cannot check before
  moving. For the rest, step 2 replaced $L$ by $c$.

With those judgments made, every remaining measure favours 3.11 unless almost
every project is blocked or a check costs more than the gain. The verdict is
"improvement". Any weighted average of the remaining measures agrees, so
nobody has to say how they would be combined.

For a team that cannot check before moving, reasonable measures split. The
verdict for that team is "open". It can still adopt 3.11 as a decision; it
should not report a demonstrated improvement.

## What the case shows

- **The judgment started whole.** No measure and no list of effects came
  first.
- **One branch was worth opening.** An objection named it, and the split
  brought a constraint that changed the estimated loss.
- **One branch was worth leaving whole.** Its combined loss had a defensible
  bound.
- **One branch needed only a direction.**
- **Evidence and purpose came apart.** After the split, it is clear what a
  survey of projects could settle ($p$, $c$, how many cannot check) and what
  stays a judgment (whose loss governs a default).

## Open

- The four checks in the note do not give $p$. The note says they are "not a
  survey of how often each reason applies". The verdict rests on the judgment
  that blockers are not widespread.
- "Reasonable for this purpose" was argued case by case. The workshop has no
  general test for it.
- The formulas add gains and losses across projects. A project whose one
  failure blocks everything else does not fit them.
- This is one agent's reconstruction. Nobody else has checked whether another
  reasonable measure survives step 5 and favours 3.10.
