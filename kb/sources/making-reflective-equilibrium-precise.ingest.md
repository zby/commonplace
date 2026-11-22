---
description: "A finite model of reflective equilibrium distinguishes settling from reaching a global optimum and proves when changing weights preserves the result."
source: https://journals.publishing.umich.edu/ergo/article/1152/galley/144/download/
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
doi: "10.3998/ergo.1152"
genre: scientific-paper
snapshot_sha256: b0de5d6d857a41c714a937f135de20521894a8e80fab3c21ef1c949687f8768a
ingested: "2026-11-21"
occasion: "How can revisions of judgments and principles settle, and how much depends on the choice of weights?"
type: types/ingest-report.md
learning_claims: true
domains: [reflective-equilibrium, belief-revision, dialectical-structures]
---

# Ingest: Making Reflective Equilibrium Precise

## Classification

Claus Beisbart, Gregor Betz and Georg Brun present a mathematical model in the philosophy journal *Ergo*. They prove properties of the revision procedure and compare simulated endpoints with optima computed for the same cases.

## Summary

A judgment is represented by a commitment to a sentence. A theory consists of principles whose consequences can account for those commitments. The agent alternates between choosing principles for its current commitments and revising commitments in light of those principles. Both steps maximize the same weighted sum of three desiderata: agreement between consequences and commitments, faithfulness to initial commitments, and systematicity (how much follows from how few principles). The agent keeps its current choice whenever that choice ties for best. Each change therefore raises the score, and the finite set of possible states guarantees termination. A fixed point can still fall short of the global optimum because each step varies only one side. Full reflective equilibrium additionally requires that the theory's consequences coincide with the commitments.

## Contribution assessment (our opinion)

The paper answers a substantive objection to reflective equilibrium by exhibiting one coherent specification of mutual revision. Distinguishing the stopping rule from the ideal gives critics two questions they can investigate separately, including whether a different revision rule would reach the same ideal more often. The proofs establish that distinction. The simulations illustrate the behavior of one specification and leave open which specification philosophers should adopt.

## Quotes

No source quotes have been retained yet.

## Connections Found

Proposition 5 supplies a precise special case for the note on [on-balance judgments](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md). Fix the arguments among sentences, the initial commitments and the component scores. If several weight settings select exactly the same set of global optima, every weighted average of those settings selects that same set. The score of each competing state varies linearly in the weights, so a rival that loses at all the endpoints also loses between them. The note's practical question remains: which weights deserve consideration?

## Learning Claims (our opinion)

The principles are explicit, individually identifiable content. The model consumes them by deriving consequences that guide the next commitment revision. A conflict between a consequence and a commitment can count against a candidate theory, giving the model a form of content-directed criticism. It can also resolve that conflict by dropping the commitment. Each accepted change shapes the next step within the run. This meets several features of a [theory builder](../theory/definitions/theory-builder.md), though the paper assesses criticism through an internal score and supplies no independent test of improved capacity for future action. In particular, the agent can replace principles drawn from its sentence pool. The pool, inferential relations and desiderata remain fixed throughout the run. [Learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)

## Extractable Value

1. **Test the range of weights that matters.** In an additive comparison with fixed alternatives and component scores, agreement on the entire set of best alternatives at the vertices certifies agreement throughout the region they span. Proposition 5 also covers a revision path when the same unique sequence occurs without random choices at each vertex. Merely observing the same final state gives less information. [quick-win]
2. **Distinguish stopping from optimality.** In a finite revision procedure, keeping a tied incumbent prevents changes that move sideways indefinitely. Once both steps keep their incumbents, neither side can improve alone. A coordinated revision can still improve the score. [quick-win]

## Limitations (our opinion)

The authors report two ensembles of 500 runs on their illustrative argument structure. Varying initial commitments at fixed weights produced a global optimum in 95% of runs. Varying weights across the four illustrative cases produced a global optimum in 88%. Among those optima, respectively 75% and 65% met the stronger condition for full reflective equilibrium. The ensembles vary different inputs, so the seven-point difference cannot isolate an effect of weight variation. Neither ensemble tests the introduction of new arguments or measures whether the resulting judgments survive external criticism. The convex-hull proof gives a guarantee for a specified additive score and leaves the choice of desiderata and defensible weights open.

## Recommended Next Action

Add Proposition 5 to the on-balance judgments note as a worked example showing when agreement at the extremes settles the choice throughout a specified range of weights.
