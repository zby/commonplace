---
description: "Surveys how ELECTRE uses concordance and vetoes to compare alternatives without forcing an order, and gives a technical basis for comparing KB routing changes."
source: https://link.springer.com/chapter/10.1007/0-387-23081-5_4
captured: "2026-11-24"
capture: font-map-repaired-pdftotext-with-local-pdf
capture_scope: full-source
doi: "10.1007/0-387-23081-5_4"
genre: scientific-paper
snapshot_sha256: ce6b94ad6bb94a4b9e4b27f17133329a51851d1cbe581cf41a851bd9f8531267
ingested: "2026-11-24"
occasion: "How do concordance and vetoes decide whether one alternative outranks another, and when does neither outrank the other?"
type: types/ingest-report.md
domains: [ELECTRE, multicriteria decision aiding, outranking, veto thresholds]
---

# Ingest: ELECTRE Methods

## Classification

A scholarly handbook chapter that surveys a family of decision methods. It explains how the methods work and cites applications and technical literature rather than reporting a new experiment.
Author: José Figueira, Vincent Mousseau, and Bernard Roy, researchers affiliated with the University of Coimbra and LAMSADE at Université Paris-Dauphine; Roy helped develop the original ELECTRE method.

## Summary

ELECTRE tests whether one alternative is at least as good as another by asking whether enough criteria support that claim (concordance) and whether any opposing criterion objects too strongly (discordance). In ELECTRE Iv, criteria on which the first alternative is no worse contribute their weights to concordance. The sum must meet a cutoff, and a loss beyond a veto threshold on any veto-bearing criterion blocks the claim. Weights represent voting power, not exchange rates between gains and losses. Testing both directions distinguishes a strict preference (only one passes), indifference (both pass), and incomparability (neither passes). Other variants grade support or weaken the credibility of a claim before opposition reaches a full veto. The chapter separates building the relation from using it to shortlist, rank, or assign alternatives to categories, and discusses how to elicit parameters and check whether conclusions survive changes to them.

## Contribution assessment (our opinion)

The chapter's likely value is as a synthesis for decisions where heterogeneous criteria make a common score hard to defend or where large losses should not be offset by gains elsewhere. Comparing variants makes clear which judgments belong in the pairwise rule and which belong in the procedure that turns comparisons into advice. The formal rules establish what can follow from those choices, such as incomparability. The cited applications suggest practical reach, but the chapter offers no controlled comparison showing when those choices lead to better decisions. That limits claims of superiority, not the value of the synthesis.

## Quotes

> 1 Concordance. For an outranking aSb to be validated, a sufficient majority of criteria should be in favor of this assertion. 2 Non-discordance. When the concordance condition holds, none of the criteria in the minority should oppose too strongly to the assertion aSb. These two conditions must be fulfilled for validating the assertion aSb.
> --- `kb/sources/.snapshots/electre-methods.md:227-233` @ `sha256:ce6b94ad6bb94a4b9e4b27f17133329a51851d1cbe581cf41a851bd9f8531267` — §2.2, local p. 137

> By strength of the concordant coalition, we mean the sum of the weights associated to the criteria forming that coalition.
> --- `kb/sources/.snapshots/electre-methods.md:361-362` @ `sha256:ce6b94ad6bb94a4b9e4b27f17133329a51851d1cbe581cf41a851bd9f8531267` — §3.1.1, local p. 140

> Veto thresholds express the power attributed to a given criterion to be against the assertion “a outranks b”, when the difference of the evaluation between g(b) and g(a) is greater than this threshold.
> --- `kb/sources/.snapshots/electre-methods.md:271-273` @ `sha256:ce6b94ad6bb94a4b9e4b27f17133329a51851d1cbe581cf41a851bd9f8531267` — §2.4, local p. 138

> aSb and bSa, i.e., aIb (a is indifferent to b). Not aSb and not bSa, i.e., aRb (a is incomparable to b).
> --- `kb/sources/.snapshots/electre-methods.md:215-217` @ `sha256:ce6b94ad6bb94a4b9e4b27f17133329a51851d1cbe581cf41a851bd9f8531267` — §2.2, local p. 137

## Connections Found

The chapter gives a technical basis for the veto example in [On-balance judgment with an LLM](../theory/on-balance-judgment-with-an-llm.md). An ordinary-ingestion regression could block the claim that a routing remedy is at least as good as the incumbent even if better quotation routing and lower maintainer effort provide enough support. That veto neither establishes the reverse claim nor makes the remedy ineligible against every rival. This is different from [necessary preference across compatible measures](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md): ELECTRE incomparability can arise under one fixed model, whereas disagreement among compatible measures can leave the necessary-preference comparison open.

## Extractable Value

1. **Check each direction for sufficient support and no veto.** In a constructed ELECTRE Iv example (§§2.2, 3.1.1–3.1.2), suppose two remedies each lead on one criterion weighted 0.4 and tie on a third weighted 0.2. Both directions meet a concordance cutoff of 0.6. If each remedy's loss on the criterion where it trails exceeds that criterion's veto threshold, neither outranks the other. A direction can also fail for insufficient concordance alone. Record two failed directions as incomparability, not a tie. [quick-win]
2. **Keep the comparison separate from the decision.** The raw relation need not be transitive (§§2.2–2.3). For a routing decision, specify separately what to do if neither direction passes rather than building a forced winner into the comparison. [quick-win]

## Limitations (our opinion)

A veto is conditional on the chosen criteria, thresholds, and assessed outcomes. The chapter's robustness discussion (§4.1) asks whether a conclusion survives across a specified range of parameter settings; it does not establish which range Commonplace can defend. Nor can varying a threshold substitute for measuring ordinary-ingestion regressions. The application references do not establish that ELECTRE or an LLM using it makes better KB maintenance decisions than the existing process. The capture is a complete local typeset chapter, not a verified copy of the publisher's version of record; some formulas remain incomplete in the extracted text, so use a rendered source for implementation details.

## Recommended Next Action

Add a worked ELECTRE Iv routing comparison to [On-balance judgment with an LLM](../theory/on-balance-judgment-with-an-llm.md) that shows how an ordinary-ingestion veto can block one direction without establishing the other.
