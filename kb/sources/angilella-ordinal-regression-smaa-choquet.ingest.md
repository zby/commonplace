---
description: "Angilella and colleagues distinguish preferences that hold across every compatible model from rank frequencies under sampled models, including when criteria interact."
source: "https://pure.port.ac.uk/ws/portalfiles/portal/3520792/GRECO_2015_cright_O_Robust_Ordinal_Regression_and_Stochastic_Multiobjective.pdf"
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 4d8549589f6711ddc30809a652e2541ec19c6a8411a02072aa1e22892bf01f90
ingested: "2026-11-21"
occasion: "What can Commonplace conclude when a comparison leaves trade-off weights open?"
type: types/ingest-report.md
domains: [robust ordinal regression, stochastic multiobjective acceptability analysis, Choquet integral]
tags: [evaluation, robust-comparison]
learning_claims: true
---

# Ingest: Robust ordinal regression and rank acceptability for hierarchical Choquet models

## Classification

Silvia Angilella, Salvatore Corrente, Salvatore Greco and Roman Słowiński develop a mathematical method for decision aiding. The manuscript gives derivations and illustrates the calculations with university data.

## Summary

A decision maker can say how two alternatives compare on research, for instance, while leaving their overall ranking open. The authors translate such judgments into constraints on a Choquet integral, a scoring rule that allows criteria to reinforce one another or count partly toward the same benefit. One set of parameters for the elementary criteria also determines scores at higher levels of the hierarchy. Once the constraints admit a solution, robust ordinal regression establishes which pairwise preferences hold for every compatible model and which hold for at least one. Stochastic multiobjective acceptability analysis estimates how often a rank occurs under a distribution over compatible models. With 220 universities and one hypothetical decision maker's judgments, university U61 ranked first in 93.29% of sampled rankings and second in the remainder.

## Contribution assessment (our opinion)

The advance over earlier hierarchical Choquet models appears to be the ability to elicit judgments at one level and determine their consequences at several levels while keeping the full range of compatible models. Deriving all the local scoring rules from the same parameters makes those consequences testable together. The university example shows that the procedure yields informative comparisons even among universities where each has some advantage. Its practical value for people choosing between real alternatives still needs testing.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper gives a formal counterpart to the break-even example in [On-balance judgments](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md). The proportion of tasks helped enters the example as evidence about use. The proportion of compatible models that favor a revision answers a different question and depends on how models are sampled. Compared with the additive model in [Ordinal Regression Revisited](./greco-ordinal-regression-revisited.ingest.md), the Choquet model also lets the value of a gain depend on what the alternative achieves on other criteria.

## Learning Claims (our opinion)

The authors describe a decision maker inspecting results and supplying further judgments. Each stated comparison identifies a preference at a particular node. The solver uses it to exclude incompatible scoring rules and recompute rankings. In Commonplace's [theory builder](../theory/definitions/theory-builder.md) terms, the comparisons have localized content and the solver demonstrably consumes them. An incompatible comparison challenges the fit of a scoring rule. Whether the comparison itself deserves revision requires judgment by the person using the results. The proposed loop retains judgments for subsequent rounds of the same decision. The hypothetical case leaves open whether people revise their reasoning or make better later decisions, either in that episode or across problems.

## Extractable Value

1. **Report what the admissible trade-offs imply.** For a nonempty family of compatible models, “A is at least as good as B” is necessary if it holds throughout and possible if it holds anywhere. A single compatible model that strictly favors B defeats the necessary claim. [quick-win]
2. **Name the population behind a percentage.** An estimated share of compatible parameter settings favoring A needs a sampling distribution. Interpreting that percentage as a share of actual users or tasks requires separate evidence about them. [quick-win]
3. **Check whether the gains overlap.** A weighted sum gives each criterion the same marginal contribution regardless of the others. If two KB checks detect much the same errors, examining their joint value may change which trade-offs deserve consideration. This is a proposed application of the interaction model. [experiment]

## Limitations (our opinion)

A guarantee applies only within the chosen family, criteria, evaluation scales and preference constraints. The university example assumes judgments from a hypothetical decision maker and uses pairwise interactions on a common evaluation scale. It illustrates how to derive a ranking under those assumptions. It supplies no evidence that the distribution of sampled parameters represents university applicants' preferences, or that the chosen hierarchy improves their decisions relative to a simpler model.

## Recommended Next Action

Add a distinction to the break-even example in [On-balance judgments](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) between a conclusion holding across all plausible trade-offs and one holding for a specified share under an explicit distribution over those trade-offs.
