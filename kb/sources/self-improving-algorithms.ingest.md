---
description: "Ailon et al. learn a product input distribution, then retain data structures that reach entropy-optimal limiting performance"
source_snapshot: "kb/sources/self-improving-algorithms.md"
ingested: "2026-07-21"
type: kb/sources/types/ingest-report.md
domains: [self-improvement, online-learning, algorithms, entropy]
---

# Ingest: Self-Improving Algorithms

Source: [self-improving-algorithms.md](./self-improving-algorithms.md)  
Captured: 2026-07-21  
From: https://page.mi.fu-berlin.de/mulzer/pubs/selfimpSICOMP.pdf

## Classification

Genre: scientific-paper -- a formal algorithms paper with explicit distributional assumptions, constructions, theorems, lower bounds, and proofs.  
Domains: self-improvement, online-learning, algorithms, entropy  
Author: Nir Ailon, Bernard Chazelle, Kenneth L. Clarkson, Ding Liu, Wolfgang Mulzer, and C. Seshadhri; the paper combines established algorithmic analysis with new constructions and lower bounds.

## Summary

The paper studies algorithms that improve expected running time by learning an unknown product distribution over fixed-length inputs. During a training phase, the algorithm gathers distributional information and builds data structures; in a stationary phase, those structures are held fixed and used to process later inputs. For comparison sorting, the limiting expected complexity is O(n + H(π(I))), where H(π(I)) is the entropy of the input's induced rank permutation, with worst-case O(n log n) time; a parallel result gives O(n + H(T(I))) for planar Delaunay triangulation. The paper also proves storage lower bounds and shows that unrestricted distribution classes force large space, making the restriction to product distributions and the time/space trade-off substantive parts of the design.

## Connections Found

Repo-local discovery read the notes README and self-improving-systems index, scanned note titles and descriptions, and ran focused searches for “self-improv*”, “training phase”, “stationary phase”, “entropy”, “distribution D”, and “online learning”. The source is a technical basis and boundary case for [A self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md): it is self-improving through learned operative state, but its training/stationary split is non-reflective and computationally allocated. It also sharpens [Learning is not only about generality](../notes/learning-is-not-only-about-generality.md) by making speed and expected cost the improvement objective. The source does not instantiate the rejectable-candidate architecture in [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md); its learner directly builds and then uses tuned data structures, which is a useful excluded-side example for that subtype.

## Extractable Value

1. **Training and stationary phases separate learning from operation** -- the algorithm gathers evidence first, then freezes a data structure whose later use changes behavior; this is a concrete cumulative-retention pattern for the pathway profile. [quick-win]
2. **Entropy gives an objective-relative measure of improvement** -- limiting complexity tracks the entropy of the induced output structure (rank permutation or Delaunay triangulation), not the entropy of the raw source, showing why “improvement” must name the task representation and objective. [deep-dive]
3. **Self-improvement need not be reflective or proposal-selective** -- the constructions adapt an algorithm’s operative data structures without a self-model, proof gate, or accept/reject evaluator; they support the profile note’s separation of membership, reflection, and update architecture. [quick-win]
4. **Distribution class is a capability boundary** -- product-distribution assumptions make fast learning possible, while the lower bounds show that universal distribution handling requires exponential or super-linear storage; this is a reusable warning against treating “self-improving” as distribution-free. [experiment]
5. **Improvement has a measurable time/space trade-off** -- the ε parameter trades storage for expected limiting time and controls training duration, offering a concrete example of reliability/speed/cost dimensions moving independently of generality. [deep-dive]
6. **Stationarity is conditional, not permanent** -- the paper explicitly returns to training when the input distribution changes substantially, making recalibration a first-class maintenance event rather than a one-time bootstrap. [experiment]

## Limitations (our opinion)

The results are theorem-driven and tested only on sorting and planar Delaunay triangulation under independent product inputs of fixed length. They do not test broad software self-modification, reflective self-models, human-in-the-loop governance, adversarial distribution shift, or whether the learned structures remain useful when the source is non-product, dependent, or nonstationary beyond the paper’s recalibration remarks. “Optimal” is relative to comparison-based lower bounds and the selected entropy measure; it should not be generalized to global task optimality or to an oracle that can judge arbitrary candidate changes. The training structures are retained and behaviorally used, but the paper does not expose a readable rationale or provenance surface for why a particular optimization was chosen.

## Recommended Next Action

Update [A self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md) with this paper as a concrete non-reflective example: explicitly mark its training-to-stationary transition as cumulative operative retention, its computational actor allocation, its task-relative entropy objective, and its distribution-shift recalibration boundary.
