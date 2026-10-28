---
description: "Zwicky/Ritchey General Morphological Analysis: parameter-value fields pruned by typed pairwise cross-consistency into solution spaces; lineage for design-space maps"
source: https://www.swemorph.com/pdf/gma.pdf
captured: "2026-10-28"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: fb4d1936e4f15f201b2ea750851408858764e334b3c0fede6932d6a50aa2d889
ingested: "2026-10-28"
occasion: "Designing a reusable design-space study for Commonplace: an evidence-bearing, revisable map of decision axes, compatibility rules and candidate regions that sits between a problem statement and an implemented ADR."
type: types/ingest-report.md
domains: [design-space-analysis, problem-structuring, morphological-analysis, decision-support]
---

# Ingest: General Morphological Analysis: A general method for non-quantified modelling

## Classification

This is a short methods paper from operational research. It is adapted from a 1998 EURO Conference paper and revised in 2013. It restates an established method with citations and one worked example, but it reports no data, controlled comparison or evaluation. It is a scientific paper in the expository-methods sense. Its evidence is close to a practitioner report: the author says the method has been used in more than 100 projects and in group trials, but neither is documented here.
Author: Tom Ritchey, a former Research Director at the Swedish National Defence Research Agency (FOI), founder of the Swedish Morphological Society and director of a consultancy that sells GMA facilitation and the MA/Carma software. He is the method's main modern exponent. He is also commercially invested in it.

## Summary

Ritchey presents Fritz Zwicky's General Morphological Analysis (GMA) as a way to model problem complexes that cannot be quantified and that causal modelling cannot handle, such as policy and futures questions. The method has four steps. (1) Define the problem's parameters and give each a discrete range of values. (2) Cross them into a "morphological field" of formally possible configurations. (3) Run a cross-consistency assessment (CCA), judging every pair of values from different parameters for mutual compatibility. CCA makes no causal or directional claim. Each judgment is typed as logical, empirical or normative, and normative judgments are held back until the possible has been mapped. Any configuration containing an inconsistent pair is removed, which leaves an internally consistent "solution space". (4) With software support, query that space as an inference model: fix one or more "driver" values and read off the option space that remains for the other parameters. The argument for tractability is that configurations grow exponentially with the number of parameters, while pairwise judgments grow only quadratically. The worked example is a Swedish bomb-shelter policy field. Its six-parameter segment has 2304 configurations, and the full ten-parameter field has more than 500,000. Ritchey also claims that the field and the CCA matrix together form an audit trail, that badly defined parameters show up as soon as they are cross-assessed, and that differences between groups assessing the same field are informative. Figures 1–5, which show the field, the CCA matrix and the driver queries, are raster images and are not in the text capture.

## Contribution assessment (our opinion)

The problem matters. Judgment-heavy option spaces are common in policy, design and architecture, and most ways of handling them leave no trail from problem framing to conclusion. This paper is not original research. It restates Zwicky's mid-century method. What it adds is a compact, clear statement of the CCA step, the logical/empirical/normative typing of inconsistencies with normative judgments deferred, and the framing of a pruned field as a queryable inference model. As far as background knowledge goes, these are the parts of GMA that later problem-structuring literature cites. The paper demonstrates that the method can be stated precisely and that pruning is computationally feasible. It does not show that GMA produces better decisions or more complete option sets than rival problem-structuring methods. The reproducibility claim rests on unreported group trials. Those limits narrow the paper's support for the method's value but leave its main contribution intact: a precise, criticisable procedure that makes judgments explicit and open to correction. Its significance is that of a reference formulation, not of a tested result.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the design-space study, this source is the **named methodological ancestor** of the mechanism at its core. The closest KB claim is [First-principles analysis maps a design space before selecting within it](../theory/first-principles-analysis-maps-design-space-before-selection.md). That note crosses axis values to generate analytic regions, marks empty cells as unoccupied, impossible under a named constraint, or unresolved, and orders exploration before closure. GMA is evidence for three of these points (is-evidence-for):

- CCA gives a concrete procedure for marking cells as impossible under a named kind of constraint.
- Deferring normative judgment is a practitioner's version of the note's rule that exploration comes before closure.
- The quadratic-versus-exponential argument answers the note's concern about enumerating a combinatorial universe.

GMA does not support the note's rival-map step. GMA takes its parameter set from facilitated group judgment and never derives a materially different decomposition to challenge it. It therefore supports the generate-and-prune stage of the method and leaves the challenge-the-map stage without precedent.

GMA compares with two sources on how a field's compatibility relation is obtained. [Build Systems à la Carte](./build-systems-a-la-carte.ingest.md) has a two-parameter field whose cells are checked by an executable model and filled with existing systems. [Components and generative programming](./components-and-generative-programming.ingest.md) prunes feature-model configuration spaces with engineered feature dependencies and generator buildability checks. GMA uses elicited pairwise human judgment over many parameters, and its cells have no witnesses. Taken together, the three show that a design-space study's compatibility rules can come from execution, engineering or judgment. Each source gives an empty-cell verdict a different warrant.

Two further sources fill different stages of the same study. [Lane 1990](./lane-1990-design-spaces-and-rules.ingest.md) (compares-with) also attaches rules to a dimensional space, but finds hard exclusions rare: most of his rules are weighted preferences, fitted to designer judgments and checked against held-out systems. GMA's typing of exclusions as logical, empirical or normative is what Lane's hard rules lack; Lane's graded rules are what GMA's mostly binary CCA lacks. [ATAM](./kazman-2000-atam-architecture-evaluation.ingest.md) (compares-with) evaluates one chosen architecture against scenarios rather than a space of candidates. It records each tradeoff judgment with written reasoning and the assumptions that would reopen it, which adds model-backed expert reasoning as a fourth warrant for an incompatibility verdict.

The KB had no previous Zwicky, Ritchey or cross-consistency material. This ingest starts that lineage.

## Extractable Value

1. **A direct template for the design-space study's three core parts** -- GMA's parameters and values correspond to decision axes and positions, the CCA matrix to compatibility rules, and the pruned solution space to candidate regions. Driver queries ("given this commitment, what option space remains?") match what an ADR author needs between a problem statement and a decision. GMA is a tested template for a decades-old practice; the study does not have to invent this structure. [quick-win]
2. **Typed compatibility judgments set the warrant of an empty region** -- CCA labels each exclusion as logical, empirical or normative. A design-space study should record that type, plus the evidence behind each entry, on every compatibility rule. A logically excluded region needs no further evidence. An empirically excluded region can be reopened by new evidence. An untested region is neither. This turns the first-principles note's "impossible under a named constraint" into a field the study can store. It also gives the study a concrete form for "evidence-bearing". [quick-win]
3. **Defer normative exclusions to the ADR stage** -- Ritchey requires that what is possible be mapped before what is desirable is judged. For the occasion, this suggests a clean boundary: the design-space study holds logical and empirical exclusions, and the ADR applies requirements and preferences to select among the surviving regions. This separation keeps the study reusable across later decisions with different priorities. [quick-win]
4. **Pairwise judgment as the scaling argument, with its gap stated** -- Pairwise rules keep elicitation quadratic. But pairwise consistency is necessary, not sufficient, for a whole configuration to be consistent. The source never discusses exclusions that involve three or more values. A design-space study that adopts pairwise rules should allow a higher-order rule or a witness check before calling a region a candidate. [experiment]
5. **Cross-assessment as garbage detection for axes** -- Ritchey reports that poorly defined parameters become evident as soon as their values are cross-assessed. This gives the study a cheap test of axis quality during drafting: if a pair cannot be judged, the axis or its values need redefinition. It complements the first-principles note's tests for whether an axis is adequate. [quick-win]
6. **Divergent assessments of the same field are signal** -- Ritchey compares independent groups' CCA matrices for one field and treats disagreement as information about the issues. In Commonplace, independent agent or reviewer passes over the same compatibility table could locate contested rules. This is a cheaper and weaker check than the first-principles note's rival-map derivation. It tests judgments within a decomposition, not the decomposition itself. [experiment]
7. **Lineage citation for the first-principles design-space note** -- The note uses GMA's core mechanism without naming its established predecessor. A single evidence link would let readers find the canonical method and its feasibility-pruning step. [quick-win]

## Limitations (our opinion)

- **No evaluation of outcomes.** The paper reports no comparison with other problem-structuring methods. It gives no evidence that GMA yields more complete or better option sets, and no data from the trials it cites. "More than 100 projects" is a usage count from someone with a commercial interest in the method, not evidence of efficacy. The reproducibility claim rests on group trials whose results are not shown. The paper supports GMA as a precisely stated procedure, not as a validated one.
- **The decomposition is taken as given.** Parameter choice is described only as identifying and defining "the relevant issues". There is no step for generating or comparing rival parameter sets. CCA can only prune within the field it is given. As in [Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), a missing parameter or a badly cut one stays invisible to everything downstream. GMA's "totality research" is total only relative to its axes. The first-principles note says the same thing about itself and adds the rival-map step that GMA lacks.
- **Pairwise pruning undercounts inconsistency.** Configurations that are consistent pair by pair can still be inconsistent as wholes. The solution space is therefore an over-approximation, but the paper presents it as the internally consistent set.
- **The quadratic argument hides the elicitation cost.** "A few hundred" judgments for 100,000 configurations is a count of judgments, not a measure of their quality. With many values per parameter the matrix becomes large, and the paper does not address assessor fatigue or how consistent the judgments are.
- **Inconsistency is mostly treated as binary.** The text mentions judging "to what extent" a pair can coexist but does not explain how graded judgments propagate. The inference model is shown only through figures the capture omits. The driver-query mechanism therefore cannot be checked beyond its prose description.
- **The domain of the claims is policy and futures work.** The trust argument ("based on the fundamental scientific method of alternating between analysis and synthesis") is an argument from analogy to scientific method, not a test. Transfer to software or KB architecture decisions is plausible but untested here.

## Recommended Next Action

Draft the compatibility-rule part of the design-space study's type spec on the CCA model: one entry per value pair (with room for higher-order rules), each recording the judgment kind (logical, empirical or normative), its evidence link and whether it can be revised. Normative exclusions should be deferred to the ADR stage. Cite this ingest as the method's lineage.
