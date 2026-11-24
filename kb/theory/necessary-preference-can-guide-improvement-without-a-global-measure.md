---
description: "Proposes strict necessary preference across compatible measures as a working definition of improvement without a global score, with six verdicts and open-case handling"
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [evaluation, self-improving-systems, robust-comparison]
---

# Necessary preference can guide improvement without a global measure

Suppose a trial of a revised instruction finds that it helps on 90 tasks, hurts on 10, and makes no difference elsewhere. Should we keep it? Answering requires two assumptions: those counts reflect expected use, and gains and losses add up across tasks. Let a helped task gain `g` on average and a harmed task lose `l`. The revision comes out ahead exactly when `90g > 10l`, that is, when the loss-to-gain ratio `l/g` is below nine.

Nobody has to know that exact ratio. The question is which ratios the purpose of the work leaves plausible:

- **All below nine.** If each gain saves a manual check and each loss adds a comparable check, we have grounds to rule out a ratio near nine while leaving the exact value open. Every remaining ratio favors the revision, so we can keep it without choosing one.
- **Up to exactly nine.** At nine, the revision and the old instruction score the same. Every plausible ratio makes the revision at least as good, but one makes it no better.
- **Across nine.** If a loss can invalidate a day's work, ratios above nine become plausible. Some plausible ratios favor the revision and others favor the old instruction, so the comparison stays open.

The same counts give three different answers. What changes is the set of weightings the work admits, not the evidence about tasks. That is the general method: rank two versions only where every admissible weighting agrees, and state precisely where they do not.

## What this rule establishes

First fix four choices: the **alternative** (what we would have instead), the **work** being judged, the **affected parties** whose gains and losses count, and the **horizon**. Then:

**A step is an improvement when every compatible measure of that work scores the successor strictly higher than the predecessor.**

A measure here is a whole way of valuing the work—such as one loss-to-gain ratio—not a single dimension such as cost. A measure is **compatible** when its treatment of gains and losses agrees with the purpose of the work and the commitments established so far. Compatibility must be argued from those commitments independently of which version a measure favors; excluding a measure because it delivers an unwanted verdict smuggles a weighting back in without defending it.

The method comes from [Greco, Mousseau and Słowiński](../sources/greco-ordinal-regression-revisited.ingest.md)'s ordinal regression, where compatible measures are additive value functions consistent with a decision maker's judgments on reference alternatives. They define "the necessary weak preference relation which holds for any two alternatives a, b from set A if and only if for all compatible value functions a is preferred to b" ([source](../sources/greco-ordinal-regression-revisited.ingest.md), verbatim), and "the possible weak preference relation which holds for this pair if and only if for at least one compatible value function a is preferred to b" ([source](../sources/greco-ordinal-regression-revisited.ingest.md), verbatim). Their preference is weak (at least as good): "When no preference information is provided, the necessary weak preference relation is a weak dominance relation" ([source](../sources/greco-ordinal-regression-revisited.ingest.md), verbatim), and a new judgment can order more pairs when it is not already implied.

Our working definition builds on that source in one formal choice and one domain difference. The source already handles an empty compatible set by locating conflicting judgments; we state nonemptiness explicitly as a precondition, since if no measure fits the commitments, every universal comparison holds vacuously and the commitments need revision first. Our one choice beyond the source is requiring **strict** preference under every compatible measure, so the break-even case at nine satisfies necessary weak preference but is not an improvement. Finally, while the source fixes its criteria in advance and does not validate a stated purpose or extract criteria from prose, here an objection can introduce an unlisted criterion—widening the compatible set and potentially withdrawing an earlier verdict.

Report one of six verdicts:

- **Improvement.** Every compatible measure strictly favors the successor.
- **Weakly better.** Every compatible measure scores the successor at least as high, some strictly favor it, and some score them equal. No compatible measure favors the predecessor—including a clean Pareto win when some compatible measure assigns zero weight to the improved dimension—so this still supports selecting the successor while falling short of strict improvement under every measure.
- **Tie.** Every compatible measure scores the versions equal.
- **Weakly worse.** Every compatible measure scores the predecessor at least as high, some strictly favor it, and some score them equal.
- **Loss.** Every compatible measure strictly favors the predecessor.
- **Open.** Some compatible measures favor the successor and others favor the predecessor (so each is only possibly preferred), or the evidence does not yet establish which verdict holds. Say which.

A possible preference alone cannot establish improvement: if one compatible measure favors a step and another favors undoing it, both the step and its reversal would count as improvements. Conversely, under a fixed set of compatible measures, a chain of strict improvements stays an improvement without cycling, because every compatible measure rises at every step. Aggregate degradation enters through open decisions, nonlinear cumulative effects, or shifted measures.

This is a working definition, not the only meaning of "better". State it—along with the four fixed choices and the compatible set—before a test, and keep it fixed for that test. New evidence can still overturn a verdict; revising the definition after seeing who lost starts a new test.

## Open for missing evidence, open for trade-offs

If the frequency or severity of rework is unknown, better outcome evidence can settle whether the loss-to-gain ratio reaches nine. If outcomes are known but compatible valuations still fall on both sides of nine, more observations of those same outcomes cannot settle the comparison. A narrower range needs a further commitment justified by the purpose of the work.

## Scope

- The break-even arithmetic assumes frequencies that reflect expected use and additive value across tasks. When the value of one gain depends on other tasks—as with cumulative context load—the additive family can exclude the relevant trade-off.
- Possible preference carries no probability. Saying what share of plausible weightings favors a change requires an explicit distribution over them, which this rule does not supply.

---

Relevant Notes:

- [On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md) — exemplifies: agreement across compatible measures is one way to judge a proposed change when the exact trade-off is unknown
- [Defining improvement for open-ended work](./defining-improvement-for-open-ended-work.md) — extends: this note proposes one working definition answering that note's question (indexing to the alternative, fixing the definition for a test, and clear wins without forced closure)
- [Selection-based learning needs only a local comparison](./selection-based-learning-needs-only-a-local-comparison.md) — extends: why selection needs only a comparison among candidates at hand; this note supplies one such comparison
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: why the objective must be identifiable independently of the change it judges
