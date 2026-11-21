# When can omitted effects reverse an improvement judgment?

Posed by the operator on 2026-11-21. What must we establish about “improves on balance” to use it as a success condition for learning? The operator proposes that it suffices to show that the judgment admits a reasonable precise definition, and in practice a range of such definitions. We can leave the choice among them open. This question connects the [on-balance account of improvement](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) to [Naming the learning method](../learning-method-name/README.md).

A definition is reasonable insofar as its treatment of gains and losses can be defended from the purpose of the work, whoever wins the comparison. If two such definitions rank a particular change differently, each still gives “on balance” a precise meaning. The verdict on that change then depends on which trade-off we accept. Bounds on omitted effects can show when a verdict survives a range of definitions.

The operator sees the same kind of judgment one level up. When we ask whether a measure is reasonable, we weigh how well it serves the purpose across cases, including cases where its verdict seems costly or mistaken. Two measures can each capture something we value and differ on what they sacrifice. Giving one measure an exact formula makes its verdict checkable while leaving our reasons for accepting the trade-off open to criticism. When would resolving a disagreement about those reasons change the improvement claim?

The operator leaves a mathematical question for future work. Could the repeated assessment of a measure's reasonableness be formulated as a map for which a fixed-point theorem applies? The current argument can proceed with that question open.

Two results bear on this question. Beisbart, Betz and Brun model alternating revisions of a theory and judgments about cases. Their Proposition 2 proves that revision reaches a fixed point under a given weighted score. Proposition 5 shows that if two choices of weights have the same set of best states, every linear mixture of those weights has the same best states, holding the rest of the model fixed. The authors leave open how to justify the weights themselves. [Making Reflective Equilibrium Precise, Appendix B](https://journals.publishing.umich.edu/ergo/article/1152/galley/144/download/)

Koray asks what happens when a voting rule is used to choose among voting rules, including itself. In his model, among neutral and unanimous rules, only dictatorships always select themselves. This illustrates how demanding universal self-selection can be. The workshop asks about a range of reasonable measures for a particular comparison. [Self-Selective Social Choice Functions Verify Arrow and Gibbard-Satterthwaite Theorems](https://repository.bilkent.edu.tr/bitstreams/3b6fb3d1-f34e-4d09-a827-96d7d8fd13e3/download)

## The starting example

Suppose there are at most a million omitted effects. If each can reduce the successor's advantage by at most $10^{-10}$ in the same units, their combined downside is at most $10^{-4}$, even if all go against the successor. A lower bound on the known gain above $10^{-4}$ settles the direction of this comparison. These are illustrative numbers. Applying the argument requires evidence for the number of effects and their combined reach. A small effect measured with every other input held at one baseline can grow when those inputs change together.

The earlier 90/10 example leaves a trade-off weight open. This example also leaves outcomes open. A comparison might hold across all defensible weights and outcomes, hold in expectation, or reverse only with a bounded probability. Which claim can Commonplace support when task frequencies, consequences, and their dependence are only partly known? Where judgments are expressed as fuzzy ranges, what does their degree of membership mean for the conclusion?

## Research leads

### First ingest batch

1. [Beisbart, Betz and Brun, *Making Reflective Equilibrium Precise*](../../sources/making-reflective-equilibrium-precise.ingest.md) — How can revisions of judgments and principles settle, and how much depends on the choice of weights?
2. [Semih Koray, *Self-Selective Social Choice Functions Verify Arrow and Gibbard-Satterthwaite Theorems*](../../sources/koray-self-selective-social-choice.ingest.md) — What does it mean to apply a choice rule to the choice of rules?

### Ingest batch on omitted effects and incomplete preferences

| Paper | Question for the workshop |
|---|---|
| [Kritzer, Pillichshammer and Wasilkowski, *Truncation Dimension for Function Approximation*](../../sources/truncation-dimension-for-function-approximation.ingest.md) | How many variables must we retain to bound the combined error from omitting the rest? |
| [Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*](../../sources/hoeffding-bounded-random-variables.ingest.md) | When can we bound the probability that many small effects accumulate in the same direction? |
| [Bertsimas and Sim, *The Price of Robustness*](../../sources/the-price-of-robustness.ingest.md) | What can we conclude if the uncertain effects have a shared limit on how far they can move against a decision? |
| [Salo and Hämäläinen, *Preference Assessment by Imprecise Ratio Statements*](https://doi.org/10.1287/opre.40.6.1053) | Which comparisons can we settle from intervals for the relative importance of outcomes? |
| [Greco, Mousseau and Słowiński, *Ordinal Regression Revisited*](../../sources/greco-ordinal-regression-revisited.ingest.md) | Which preferences hold under some or all value functions compatible with judgments already made? |
| [Lahdelma, Hokkanen and Salminen, *SMAA — Stochastic Multiobjective Acceptability Analysis*](https://doi.org/10.1016/S0377-2217(97)00163-X) | What assumptions let us say how much of the range of weights favors an alternative? |
| [Baudrit, Couso and Dubois, *Joint Propagation of Probability and Possibility in Risk Analysis*](../../sources/baudrit-joint-propagation-probability-possibility.ingest.md) | How can the same comparison use observed frequencies and fuzzy ranges for poorly known inputs? |

The **1992 PAIRS** and **1998 SMAA** originals remain pending full-text access. Two later studies provide worked examples for those questions:

- [Mustajoki, Hämäläinen and Salo on interval SMART/SWING (2005)](../../sources/mustajoki-interval-smart-swing.ingest.md) compare alternatives under the same admissible weights. Their separate score ranges can overlap even when every shared weighting favors one alternative.
- [Angilella and colleagues on ordinal regression and SMAA (2016)](../../sources/angilella-ordinal-regression-smaa-choquet.ingest.md) show how to sample compatible preference models when criteria can interact. The share of models favoring a change depends on the sampling distribution.

## What closes the workshop

Explain why at least one precise interpretation fits the work Commonplace values. Use a comparison to show where the choice among reasonable interpretations matters or can be left open. The existing example of adding a routing instruction to `AGENTS.md` is a candidate. The gain concerns tasks that reach the right instructions. The same line also loads on other tasks, so estimating its total cost requires knowing how often extra context matters and what failures cost. If the comparison stays open, identify the missing bound and what observation could change the judgment.

Check the applicable assumptions against the primary literature. Retain the resulting claim and its limits in the on-balance note or a linked theory note, or record why the calculation adds no usable criterion. Carry any consequence for a learning claim back to the naming workshop if it is still active. Then remove this directory and its active-list entry.

Commits carry `Workshop: kb/work/bounding-omitted-effects`.
