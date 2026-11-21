---
description: "Bounds the joint error of omitting coordinates in weighted anchored function spaces, including interactions between retained and omitted variables."
source: https://arxiv.org/abs/1610.02852
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 64fd6ef606a488bddb50499a34cc7cb6cb5f103e0a084938015aba2675257fe6
ingested: "2026-11-21"
occasion: "When can we bound the combined effect of omitted variables?"
type: types/ingest-report.md
domains: [truncation dimension, anchored Sobolev spaces, product weights]
---

# Ingest: Truncation Dimension for Function Approximation

## Classification

Peter Kritzer, Friedrich Pillichshammer and G. W. Wasilkowski prove worst-case approximation bounds and compute examples from them. This numerical analysis preprint extends the authors’ earlier work on truncation for integration.

## Summary

For a function of many ordered coordinates, the authors ask how many to retain when all later coordinates are fixed at zero. In their weighted anchored Sobolev spaces, this substitution removes exactly the components involving at least one omitted coordinate. A bound on their combined contribution gives a sufficient cutoff for a specified error in the output norm, uniformly over functions of unit input norm. For product weights with coordinate weight $j^{-a}$ and input and output exponents both equal to two, the introductory table gives sufficient cutoffs of 79, 22 and 11 for $a=3,4,5$ respectively at tolerance $10^{-5}$. The paper also bounds the error of applying a lower-dimensional approximation algorithm after truncation.

## Contribution assessment (our opinion)

The practical gain is that an algorithm can sample the original function with the omitted coordinates fixed, even when its component functions are unknown. The proof gives an advance guarantee for an entire specified class, complementing function-specific variance decompositions. The numerical examples show how strongly that guarantee depends on weight decay. They establish sufficient dimensions while leaving room for sharper bounds.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies a mathematical comparison for the reversal test in [On-balance judgments can guide improvement without a global measure](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md). Several omissions could jointly change a decision even if each looks harmless alone. The paper shows how to control their combined effect when the coordinates, permitted interactions and error measure are specified. Applying the result to a KB decision would require grounds for those choices and a link between error in that measure and reversal of the decision.

## Extractable Value

1. **Count every component touching the omitted coordinates.** For input exponent $p>1$, Theorem 1 uses the conjugate-exponent norm of the subset weights multiplied by their embedding bounds, taken over every subset containing an omitted index. If this quantity is at most the tolerance, the combined output error is at most that tolerance on the unit ball. This includes interactions across the cutoff and requires no probabilistic independence. [just-a-reference]

## Limitations (our opinion)

The weights constrain mixed derivatives in the chosen function class. The paper gives no procedure for inferring valid weights from a few observed single-variable effects. The guarantee also depends on the output norm. An integrated error bound can allow a large error on a small part of the domain, which matters for a decision governed by a single critical case.

## Recommended Next Action

Keep this paper as a source-only reference for the joint-omission question in the on-balance judgments note until a KB comparison supplies a defensible function class and error measure.
