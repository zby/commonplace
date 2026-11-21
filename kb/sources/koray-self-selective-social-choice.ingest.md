---
description: "Koray defines how outcome preferences induce votes over voting rules and proves when a rule can always elect itself."
source: https://repository.bilkent.edu.tr/bitstreams/3b6fb3d1-f34e-4d09-a827-96d7d8fd13e3/download
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 11e59bcfd3b2a7e3be63c0d2eca50fefdbb551958dc19b9b7e6fc0c67612c1d8
ingested: "2026-11-21"
occasion: "What does it mean to apply a choice rule to the choice of rules?"
type: types/ingest-report.md
domains: [social choice, self-selectivity, voting rules, independence of irrelevant alternatives]
---

# Ingest: Self-Selective Social Choice Functions Verify Arrow and Gibbard-Satterthwaite Theorems

## Classification

Semih Koray, of Bilkent University's Department of Economics, published this theoretical paper in *Econometrica* in 2000. It offers definitions, a worked election and proofs.

## Summary

Run each candidate voting rule on the same ballots. Each voter then ranks the rules by the outcome each one chose, tying rules that chose the same outcome. Apply one candidate rule to these new ballots, with ties broken in ways that respect each voter's strict preferences. The rule is self-selective for this election and menu of rules if at least one such tie-breaking profile makes it choose itself. Universal self-selectivity requires this for every profile of strict rankings and every finite menu of neutral rules containing the candidate. Koray proves that among neutral, unanimous, single-winner rules defined for all finite nonempty sets of alternatives and a fixed finite electorate, exactly the dictatorships pass this universal test. Such a rule always chooses the same voter's favorite.

## Contribution assessment (our opinion)

Koray extends a question Binmore posed for constitutions on three alternatives to voting rules that select one winner from any finite number of alternatives. The substantive advance appears to be the bridge to Arrow's theorem. Universal self-selection forces the winner to survive removal of losing alternatives. At each profile, choices from subsets then reveal a social ranking, to which Arrow's result applies under unanimity. This explains why a requirement about choosing procedures can constrain whose preferences determine ordinary outcomes.

## Quotes

No source quotes have been retained yet.

## Connections Found

Koray supplies a comparison case for the question of what licenses a change of objective. A rule can lose under its own procedure because voters supply independent rankings of the outcomes its rivals produce. The procedure used to aggregate preferences is up for choice while the voters' ends remain fixed. Changing those ends poses a separate question in [Revising an improvement objective is licensed from outside it](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md).

## Extractable Value

1. **Distinguish a rule choosing itself once from a rule that can always do so.** In Koray's example, a Borda rule and a Condorcet-based rule can each elect itself when plurality is a third candidate. Remove plurality and each elects the other, even though the voters' rankings of the original outcomes stay fixed. This gives a worked counterexample to inferring general self-selection from one successful vote. [quick-win]
2. **Specify how ties between rules are resolved.** Two rules can disagree on most elections yet choose the same outcome today. Each voter is then indifferent between them under Koray's construction. The test asks whether *some* compatible resolution lets a rule win. Requiring it to win for *every* resolution would exclude even dictatorships from universal self-selection. [just-a-reference]

## Limitations (our opinion)

Voters evaluate a rule solely by its winner at the given profile. Preferences about fairness of procedure, costs, or performance in future elections could induce different rankings of rules. The dictatorship characterization also depends on unanimity (a common top choice wins), neutrality (renaming alternatives preserves the choice), and the domain of all strict profiles across all finite menu sizes. A collective decision in a particular KB review supplies no evidence by itself that these conditions hold.

## Recommended Next Action

Use Koray's three-rule election on pages 986–987 as the worked example in a short KB note answering what it means for a choice rule to choose itself.
