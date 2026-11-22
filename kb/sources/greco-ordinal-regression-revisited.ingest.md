---
description: "Greco, Mousseau and Słowiński show which comparisons follow from every additive value function consistent with a decision maker's judgments, and which depend on unresolved trade-offs."
type: types/ingest-report.md
source: https://www.lamsade.dauphine.fr/mcda/biblio/PDF/UTAGMS-Ejor.pdf
captured: "2026-11-21"
ingested: "2026-11-21"
capture: pdftotext
capture_scope: full-source
doi: "10.1016/j.ejor.2007.08.013"
genre: scientific-paper
snapshot_sha256: 51c5ee8d3204e0eccfd73137916e2fbcb10eadfe0ffd6dfcaeecc828c3908b84
occasion: "What can Commonplace conclude when a comparison leaves trade-off weights open?"
domains: [ordinal regression, multiple criteria decision analysis, preference elicitation]
tags: [robust-comparison]
learning_claims: true
---

# Ingest: Ordinal Regression Revisited

## Classification

Salvatore Greco, Vincent Mousseau and Roman Słowiński present a mathematical method for ranking alternatives evaluated on several criteria. The accepted manuscript for the *European Journal of Operational Research* gives proofs, linear programming formulations and a hypothetical hiring example.

## Summary

A decision maker compares familiar alternatives. UTAGMS retains every additive value function consistent with those judgments, allowing each criterion's contribution to increase at different rates along its scale. A weak preference for A over B is necessary if every compatible function scores A at least as high as B, and possible if at least one does. With no reference judgments, the necessary relation reduces to criterion-by-criterion weak dominance. Adding consistent judgments can establish further necessary comparisons and rule out previously possible ones. The authors also show how to handle judgments supplied with different confidence levels and how to locate conflicting judgments when no function fits.

## Contribution assessment (our opinion)

Several models can reproduce the same examples and disagree on the very choice the decision maker faces. Compared with selecting a single fit in earlier ordinal regression methods, testing the full family gives a stronger justification for some comparisons and identifies precisely where others remain open. The proofs and feasibility tests establish that contribution within the additive model. Whether the extra distinctions help people make better decisions remains an empirical question.

## Quotes

> The preference model built via ordinal regression is the set of all additive value functions compatible with the preference information. Using this model, one can deﬁne two relations in the set A: the necessary weak preference relation which holds for any two alternatives a, b from set A if and only if for all compatible value functions a is preferred to b, and the possible weak preference relation which holds for this pair if and only if for at least one compatible value function a is preferred to b. These relations establish a necessary and a possible ranking of alternatives from A, being, respectively, a partial preorder and a strongly complete relation. The UTAGMS method is intended to be used interactively, with an increasing subset AR and a progressive statement of pairwise comparisons. When no preference information is provided, the necessary weak preference relation is a weak dominance relation, and the possible weak preference relation is a complete relation. Every new pairwise comparison of reference alternatives, for which the dominance relation does not hold, is enriching the necessary relation and it is impoverishing the possible relation, so that they converge with the growth of the preference information.
> --- `kb/sources/.snapshots/greco-ordinal-regression-revisited.md` @ `sha256:51c5ee8d3204e0eccfd73137916e2fbcb10eadfe0ffd6dfcaeecc828c3908b84` — abstract

## Connections Found

The paper gives a formal reading of the nine-to-one break-even example in [On-balance judgments can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md). If the admissible loss-to-gain ratios are all below nine, every admitted weighting favors the revision. If the range includes values on both sides, each strict ordering has a witness. The source adds a way to narrow such a range by eliciting preferences between reference cases, even when the shapes of the individual criterion functions are also open.

## Learning Claims (our opinion)

The method infers a family of preference models from examples. The hypothetical hiring case illustrates several features of a [theory builder](../theory/definitions/theory-builder.md) in the combined work of the decision maker and solver. Each comparison has identifiable content and constrains which rankings the solver returns. The solver localizes a conflict to two judgments of indifference that cannot both hold under additivity. The decision maker withdraws the less certain judgment, and the next ranking uses the revised constraints. This illustrates selective repair within one decision. The criterion set and additivity stay fixed throughout. The example supplies no measure of improvement on subsequent hiring decisions.

## Extractable Value

1. Test the strongest claim a comparison supports. A single compatible scoring rule witnesses possibility. To establish that A is at least as good as B throughout a nonempty family, rule out every compatible scoring rule that strictly favors B. A tie at a break-even weight preserves the weak claim but defeats a claim of strict improvement. [quick-win]
2. Ask for another judgment on a familiar pair when remaining models disagree on a consequential choice. If the new judgment eliminates every model, isolate the conflicting inputs and reconsider the judgments or the additive assumption. [experiment]

## Limitations (our opinion)

Necessity depends on the chosen criteria, their evaluations, monotonicity, additivity and the reference judgments. If the value of improving one criterion depends on the level of another, the additive family can exclude the relevant trade-off. Possibility carries no probability or prevalence estimate. The hypothetical hiring example illustrates computations and revision of inputs, leaving the cognitive cost and practical accuracy of elicitation unmeasured.

## Recommended Next Action

Annotate the nine-to-one example in the on-balance note with the strongest comparison supported when admissible ratios fall below, reach, or cross the break-even value.
