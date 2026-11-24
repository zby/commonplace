---
description: "Proposes asymmetric necessary preference across compatible measures as one formal way to make on-balance judgments without a global score, admitting Pareto wins with four verdicts"
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [evaluation, self-improving-systems, robust-comparison]
---

# Necessary preference can guide improvement without a global measure

One formal way to carry out an on-balance judgment without inventing a single global score is to ask which preference survives across *every* weighting compatible with the work's purpose. Suppose a trial of a revised instruction finds that it helps on 90 tasks, hurts on 10, and makes no difference elsewhere. Should we keep it? Answering quantitatively requires two assumptions: those counts reflect expected use, and gains and losses add up across tasks. Let a helped task gain `g` on average and a harmed task lose `l`. The revision comes out strictly ahead whenever `90g > 10l`, that is, when the loss-to-gain ratio `l/g` is below nine, and breaks even at nine.

Nobody has to know the exact ratio. The question is which ratios the purpose of the work leaves plausible:

- **At most nine (with ratios below nine plausible).** If each gain saves a manual check and each loss adds a comparable check, we have grounds to rule out ratios above nine while leaving the exact value open. Every compatible ratio scores the revision at least as high as the old instruction, and ratios below nine strictly favor it. Even if the boundary `l/g = 9` stays in the plausible range, no compatible weighting favors keeping the old instruction, so we can adopt the revision without picking one ratio.
- **Only nine.** If the only compatible ratio is exactly nine, the two versions tie under every compatible measure and nothing favors switching.
- **Across nine.** If a loss can invalidate a day's work, ratios above nine become plausible. Some compatible ratios favor the revision and others favor the old instruction, so the comparison stays open.

The same counts give different answers depending on the set of weightings the work admits. The general method is to prefer one version only when no admissible weighting opposes it and at least one strictly favors it, and to state precisely where weightings disagree.

## What this rule establishes

First fix four choices: the **alternative** (what we would have instead), the **work** being judged, the **affected parties** whose gains and losses count, and the **horizon**. Then:

**A step is an improvement when every compatible measure of that work scores the successor at least as high as the predecessor, and at least one compatible measure scores it strictly higher.**

A measure here is a whole way of valuing the work—such as one loss-to-gain ratio—not a single dimension such as cost. A measure is **compatible** when its treatment of gains and losses agrees with the purpose of the work and the commitments established so far. Compatibility must be argued from those commitments independently of which version a measure favors; excluding a measure because it delivers an unwanted verdict smuggles a weighting back in without defending it.

This criterion is **asymmetric necessary preference**, or Pareto dominance across the compatible family. A clean Pareto win—fixing a live failure with zero cost or downside for any other task or party—counts as an improvement even if some compatible measure gives weight zero to that failure: no compatible measure loses, and every measure that values fixing the failure strictly gains. Conversely, as soon as a change carries any real cost (such as diffuse context load or maintenance effort), any compatible measure that counts that cost scores the successor lower and moves the verdict out of improvement.

The robustness structure comes from [Greco, Mousseau and Słowiński](../sources/greco-ordinal-regression-revisited.ingest.md)'s ordinal regression (UTAGMS), which keeps all additive value functions consistent with a decision maker's reference comparisons rather than picking one arbitrary fit. They define "the necessary weak preference relation which holds for any two alternatives a, b from set A if and only if for all compatible value functions a is preferred to b" ([source](../sources/greco-ordinal-regression-revisited.ingest.md), verbatim), and "the possible weak preference relation which holds for this pair if and only if for at least one compatible value function a is preferred to b" ([source](../sources/greco-ordinal-regression-revisited.ingest.md), verbatim). With no reference judgments, "When no preference information is provided, the necessary weak preference relation is a weak dominance relation" ([source](../sources/greco-ordinal-regression-revisited.ingest.md), verbatim), and each new consistent judgment narrows the family and orders more pairs.

Our improvement rule is simply the asymmetric part of that necessary weak preference relation: the successor is necessarily at least as good as the predecessor, and the predecessor is *not* necessarily at least as good as the successor (which holds if and only if at least one compatible measure strictly favors the successor). That excludes pure ties without excluding clean Pareto wins or no-downside break-even bounds. Two explicit guards adapt the source to open-ended work. First, the compatible set must be nonempty—otherwise every universal statement holds vacuously, and conflicting commitments must be revised first (which the source handles by isolating conflicting reference judgments). Second, UTAGMS was built for interactive human ranking over a fixed table of numerically scored criteria; in open-ended work, criteria are not fixed in advance, so an objection can introduce an unlisted criterion, widen the compatible set, and reopen an earlier verdict.

For any nonempty compatible set, the relation partitions comparisons into four mutually exclusive verdicts:

- **Improvement.** Every compatible measure scores the successor at least as high, and at least one strictly favors it. (Covers both unanimous strict wins and clean Pareto wins where some compatible measures are indifferent.)
- **Loss.** Every compatible measure scores the predecessor at least as high, and at least one strictly favors it.
- **Tie.** Every compatible measure scores the versions equal.
- **Open.** Some compatible measures strictly favor the successor and others strictly favor the predecessor (so each is only possibly preferred), or the evidence does not yet establish which verdict holds. Say which.

A possible preference alone cannot establish improvement: if one compatible measure favors a step and another favors undoing it, both the step and its reversal would count as improvements. Conversely, under a fixed nonempty set of compatible measures, asymmetric necessary preference is a strict partial order: no compatible measure ever drops and at least one strictly rises at every step, so a chain of improvements cannot cycle. Aggregate degradation enters through open decisions, nonlinear cumulative effects, or shifted measures.

This is a working definition—one formalization of on-balance judgment, not the only meaning of "better". State it, along with the four fixed choices and the compatible set, before a test, and keep it fixed for that test. New evidence can still overturn a verdict; revising the standard after seeing who lost starts a new test.

## Open for missing evidence, open for trade-offs

If the frequency or severity of rework is unknown, better outcome evidence can settle whether the loss-to-gain ratio stays below nine. If outcomes are known but compatible valuations still fall on both sides of nine, more observations of those same outcomes cannot settle the comparison. A narrower range needs a further commitment justified by the purpose of the work.

## Scope

- **One formalization, not the whole of on-balance judgment.** UTAGMS assumes pre-fixed, exhaustive, numerically scored criteria and compensatory additivity across them. When an on-balance judgment turns on discovering which facts or criteria apply, checking hard non-compensatory commitments, or tracing causal mechanisms across rival remedies ([On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md)), a family of compatible measures disciplines the trade-off check rather than replacing qualitative inquiry.
- **Additive assumptions.** The break-even arithmetic assumes frequencies that reflect expected use and additive value across tasks. When the value of one gain depends on other tasks—as with cumulative context load—an additive family can exclude the relevant trade-off.
- **No probability over weights.** Possible preference carries no probability. Saying what share of plausible weightings favors a change requires an explicit distribution over them, which this rule does not supply.

---

Relevant Notes:

- [On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md) — exemplifies: agreement across compatible measures is one formal check inside an LLM's on-balance judgment when exact trade-offs are unknown
- [Defining improvement for open-ended work](./defining-improvement-for-open-ended-work.md) — extends: this note proposes one working definition answering that note's question (indexing to the alternative, fixing the definition for a test, and clear wins without forced closure)
- [Selection-based learning needs only a local comparison](./selection-based-learning-needs-only-a-local-comparison.md) — extends: why selection needs only a comparison among candidates at hand; this note supplies one such comparison
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: why the objective must be identifiable independently of the change it judges
