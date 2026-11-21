# Supporting the on-balance definition of improvement

Posed by the operator on 2026-11-21. The directory name comes from the first
question the workshop asked, about omitted effects. The operator then set the
goal below.

## Goal

Give the [on-balance account of improvement](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
the support it needs to serve as a definition of improvement, and so as the
success condition for learning. [Defining the learning process](../learning-method-name/README.md)
depends on the result.

## The definition

Stated by the operator on 2026-11-21:

> A step is an improvement on balance when, for every reasonable measure, the
> successor scores higher than the predecessor.

No measure is selected. The library note distinguishes these verdicts:

- **Improvement:** every reasonable measure favours the step.
- **Loss:** every reasonable measure favours the predecessor.
- **Tie:** every reasonable measure scores both versions equally.
- **Better or worse on some, tied on the rest:** report the direction. No
  measure favors the other version, but not all strictly prefer this one.
- **Open:** some measures favor each version, or evidence is missing.

A measure is reasonable insofar as its treatment of gains and losses can be
defended from the purpose of the work, whoever wins the comparison.

Two decisions the operator made on the way:

- **"A reasonable measure exists" is not the definition.** If one reasonable
  measure favours a step and another favours undoing it, the step and its
  reversal would both be improvements. Existence shows only that the claim is
  well defined.
- **No measure over measures is needed.** A weighting over measures gives
  their weighted average, which is one more measure, as a probability
  distribution over probability distributions reduces to one distribution. So
  when every reasonable measure favours the step, every weighting of them does
  too. When they disagree, choosing weights is the same act as choosing one
  measure: a value judgment for the people affected. The step can then be
  taken as a decision, and is not a demonstrated improvement.

The reduction needs the measures to share a scale. An exchange rate between
units is itself a weight.

## The process is recursive

Stated by the operator on 2026-11-21. The definition describes a result. The
way people reach it is recursive. For a Python release they say: this change
breaks some programs and speeds up others. How to compare those two sets is
an on-balance decision. So is each side of it: how bad the breakage is for one
program, and whether one program's speed-up matters. In principle the whole
tree can be unwound into single cases, and the judgment is then about just
those cases. People do not work on the unwound list.

The operator added: when people need more precision, they try to decompose.
So the tree is not given beforehand. A judgment starts whole, and a part of it
is split only when the whole judgment is not precise enough for the decision.

So the definition and the process are different things. "Every reasonable
measure favours the step" says what improvement means. It does not say that a
judge must first list the measures or the effects. A judge can start with the
whole comparison. A challenge such as "you are understating the cost to
blocked projects" then says where to look more closely. Criticism therefore
does more than register disagreement: it selects what to open.

What follows is the agent's (claude-fable-5-2) account of the consequences,
revised after a comment from Astra relayed by the operator on 2026-11-21. The
rule for what a node passes up, the difference between leaving a branch whole
and dropping it, and the point that splitting alone buys nothing are Astra's.

- **The tree is what makes the judgment possible.** The unwound list is the
  "enormous test array" a symbolic system would need. Nobody can weigh it at
  once. Each node of the tree is a comparison small enough to judge.
- **The tree is what makes the judgment criticizable.** A disagreement can
  name a node: "you underrate the breakage", not "your overall verdict is
  wrong". This is the same property the KB calls
  [addressability](../../theory/definitions/addressable-theory.md).
- **A node passes up enough to tell whether it could change its parent.**
  That is the rule, and it does not fix a form.
  - Sometimes a direction is enough. If one branch gives a strict gain, no
    branch gives a loss, and the parent adds them, no size is needed.
  - Sometimes a range is too little. Suppose one branch saves $x + 1$ hours
    and another costs $x$ hours, with the same unknown $x$ between 0 and 10.
    Reporting "saves 1 to 11, costs 0 to 10" makes a loss look possible.
    Keeping the shared $x$ shows a gain of exactly one hour. The Mustajoki
    paper shows the same effect for weights.
- **Leaving a branch whole is not dropping it.** This is the workshop's
  clearest answer to its original question about omitted effects.
  - A branch can stay whole when we can defend an upper bound on its combined
    losses, and that bound cannot erase the gain.
  - Dismissing each loss separately, because none could erase the gain alone,
    gives no such warrant. Many of them together might.
- **Decomposition helps when the parts bring something new.** Splitting a
  judgment narrows it only if the parts come with evidence or constraints
  that the whole did not have. Splitting alone buys no precision.
- **It is used on demand.** People split a node when what it passes up cannot
  settle its parent, or when someone contests it. Otherwise it stays whole.
  This is the reversal test seen from the other side.
- **It has a price.** It costs effort, and a split can lose what the parts
  share, as in the $x$ example.
- **Two kept sources describe refinement on demand.** The Greco ingest: ask
  for another judgment on a familiar pair when the remaining models disagree
  on a consequential choice. The Mustajoki ingest: direct further questions
  to the comparisons that remain open.

[The learning-process workshop](../learning-method-name/README.md) calls this
process deliberation, and keeps "on balance" for the verdict it reaches. Its
draft defines deliberative learning as learning in which this process decides
what is retained.

This recursion runs downward, into the parts of one comparison. It is
different from the measure over measures, which would have run upward and
which reduces to a single measure.

## Worked case

[Is a new Python version an improvement?](./python-release-worked-case.md)
runs the process on Python 3.11 over 3.10. It starts from the whole judgment,
opens one branch after an objection, leaves one branch whole with a bound, and
separates what evidence could settle from what stays a judgment about purpose.

[Four further cases](./further-cases.md) differ from that one:

- **A refactoring.** The whole gain lies in future work, so the verdict rests
  on a forecast and is confirmed later.
- **Approving a medicine.** Gains and losses have no common scale and a loser
  cannot opt out. An open verdict is resolved by narrowing what the claim
  covers.
- **A removal.** The loss is visible and the gain is not. The same measures
  must serve additions and removals.
- **An irreversible step.** Reversibility can change the on-balance judgment.
  If the team can detect a mistake and undo the step, it can avoid later
  losses. It still counts the harm already done and the cost of going back.

The library companions now cover [how an objection can direct a comparison](../../theory/an-objection-can-show-where-to-split-an-on-balance-judgment.md) and [when reversibility limits future loss](../../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md). The Python companion does not claim that tests and rollback bound silent failures.

## Support from sources

The ingests were written on 2026-11-21. None has retained quotes yet, so the
proposition numbers and figures below are unchecked against the papers.

| What the definition needs | Source | What it supplies |
|---|---|---|
| A relation defined over all admissible measures | [Greco, Mousseau and Słowiński](../../sources/greco-ordinal-regression-revisited.ingest.md) | A preference is *necessary* if every compatible value function gives it, and *possible* if at least one does. With no judgments, the necessary relation is plain dominance; each added judgment can extend it. |
| A test for two alternatives | [Mustajoki, Hämäläinen and Salo](../../sources/mustajoki-interval-smart-swing.ingest.md) | Compare both at the same weights and ask whether the difference stays positive across the admissible set. Separate score ranges can overlap while every shared weighting favours one side. |
| Checking a range by its extremes | [Beisbart, Betz and Brun](../../sources/making-reflective-equilibrium-precise.ingest.md), Proposition 5 | If two choices of weights have the same best states, so does every mixture of them. |
| Deciding which measures are in the set | Beisbart, Betz and Brun, Proposition 2 | A model of revising principles and case judgments against each other until neither changes. The authors leave the justification of their own weights open. |
| Uncertain sizes of known effects | [Bertsimas and Sim](../../sources/the-price-of-robustness.ingest.md) | How much simultaneous adverse movement erases a measured advantage, with no probability model. |
| Frequencies mixed with poorly known ranges | [Baudrit, Couso and Dubois](../../sources/baudrit-joint-propagation-probability-possibility.ingest.md) | Bounds that differ when one unknown value holds across all cases. This fits the `AGENTS.md` routing example, where one line loads on every prompt. |
| Judgments arranged in a tree | [Angilella and colleagues](../../sources/angilella-ordinal-regression-smaa-choquet.ingest.md) | A hierarchy of criteria in which a judgment given at one node has consequences at the others. This is the closest source for the recursive process. The paper also models gains that overlap, and reports the share of sampled measures favouring an alternative, which the definition does not use. |

The on-balance note's 90/10 example fits the first three rows. The revision
wins for every loss-to-gain ratio below nine, ties at nine, and the verdict is
open when the admissible range crosses nine.

**Sources removed on 2026-11-21** as not fitting the definition: Hoeffding's
inequalities (they need independent effects and a known positive margin), the
truncation-dimension paper (it needs an ordered list of variables with assumed
decay), and Koray's self-selective voting rules (the definition does not ask a
measure to select itself). Their ingests were deleted from `kb/sources/`.

**Sources still wanted.** The first two rows of the next section rest on
memory.

| Work | Why |
|---|---|
| Kit Fine, *Vagueness, Truth and Logic* (1975) | Truth under every admissible sharpening. |
| Amartya Sen on intersection orderings; the specific work is not yet identified | An incomplete ordering built from what all reasonable rankings share. |
| [Salo and Hämäläinen, *Preference Assessment by Imprecise Ratio Statements*](https://doi.org/10.1287/opre.40.6.1053) (1992) | The original of the pairwise test. Awaits full-text access. |
| Research on when decomposing a judgment improves it; the agent recalls MacGregor and Armstrong, *Judgmental decomposition: when does it work?* (1994), unverified | Whether splitting a judgment helps only when the whole judgment is very uncertain. |

## Formalisms that fit

Recorded by an agent (claude-fable-5-2).

| Part of the reasoning | Formalism |
|---|---|
| The definition itself | Supervaluation: a vague claim is true when it holds under every admissible way of making it precise, and indeterminate when those ways disagree. |
| The relation between versions | Sen's intersection ordering: keep only the comparisons every reasonable ranking shares. |
| The test for one comparison | Interval weights with pairwise dominance. |
| Names for the verdicts | Necessary and possible preference. |
| Excluding a measure | Reflective equilibrium. |
| When to stop investigating | Value of information: information that cannot change the decision has no value for it. |

Supervaluation has a known open problem that applies here: which sharpenings
are admissible is itself vague. For this definition that matters only when the
boundary of the set falls near the break-even point.

## Limits the support must state

Raised by an agent (claude-fable-5-2); they await the operator's view.

- **The definition makes a claim meaningful, not true.** Each claim that a
  system improved needs its own evidence that the inequality holds across the
  set.
- **"Open" may be common.** The definition is strict. Nobody has checked how
  often Commonplace changes would get that verdict.
- **The judgment moves into the set.** Every method takes the criteria, the
  bounds and the form of the score as given. Deciding which measures are
  reasonable is where purpose enters. There is no general test for it; the
  worked case argues each exclusion separately.
- **Omitted effects are not bounded by these methods.** Each guarantee covers
  only the effects it represents. The operator's starting example shows what
  a bound would need: at most a million omitted effects, each able to reduce
  the advantage by at most $10^{-10}$, give a combined downside of at most
  $10^{-4}$. A count and a per-effect bound are what an omitted effect lacks.
  Two other bounds are available. The worked case uses the channels a change
  can act through. The irreversible-step case uses reversibility: if undoing the step stops the harm, an upper
  bound on the rate of loss and the time to correction bounds the loss
  during the trial. The cost of correction also counts.
  Either one bounds a branch as a whole, which is what leaving it unopened
  requires.
- **Additivity is assumed almost everywhere.** If two gains overlap, or one
  effect grows with another, an additive score misstates the balance.
- **Shared causes defeat counting.** In the routing example every loss comes
  through one channel, so the losses are not independent.

## Set aside

The operator asked whether repeated assessment of a measure's reasonableness
could be a map with a fixed point. Since a weighting over measures reduces to
one measure, there are no levels to iterate, and the definition does not need
the answer.

## What closes the workshop

- The on-balance note, or a theory note linked from it, states the definition:
  improvement holds when every reasonable measure favours the step, no measure
  has to be chosen, and a weighting over measures adds nothing.
- One worked comparison shows the process: one branch worth opening, one
  worth leaving whole, and what remains a judgment about purpose after the
  evidence is in.
- The limits above are stated in the note or answered.
- The claims taken from the sources are checked against the papers, with
  quotes retained in the ingests.
- The consequence for a learning claim is carried to the learning-process
  workshop if it is still active. Done on 2026-11-21: its draft defines
  "learned" by this workshop's definition and cites the irreversible-step
  case.

Then remove this directory and its active-list entry.

Commits carry `Workshop: kb/work/bounding-omitted-effects`.
