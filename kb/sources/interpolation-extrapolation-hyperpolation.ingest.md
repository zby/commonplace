---
description: "Toby Ord's hyperpolation paper gives a geometric vocabulary for off-subspace creativity, sharpening the KB's synthesis-oracle and discovery/reach notes."
source_snapshot: "interpolation-extrapolation-hyperpolation.md"
ingested: "2026-05-19"
type: kb/sources/types/ingest-report.md
source_type: scientific-paper
domains: [creativity, generalisation, oracle-theory, ai-limits]
---

# Ingest: Interpolation, Extrapolation, Hyperpolation

Source: interpolation-extrapolation-hyperpolation.md
Captured: 2026-05-19
From: https://arxiv.org/pdf/2409.05513

## Classification

Type: scientific-paper -- arXiv preprint with formal definitions, worked mathematical examples, citations, and a conceptual argument connecting generalisation, creativity, machine learning, and evolution. It is closer to a theoretical/conceptual paper than an empirical ML paper.
Domains: creativity, generalisation, oracle-theory, ai-limits
Author: Toby Ord is an academic philosopher best known for work on ethics and existential risk. The author signal is useful for conceptual clarity, not authority on ML benchmarking.

## Summary

Ord introduces **hyperpolation** as a third kind of function generalisation alongside interpolation and extrapolation: estimating values at points outside the affine hull of the known data, not merely between or beyond known points along the same subspace. The paper gives a formal convex-hull / affine-hull definition, then argues that hyperpolation is possible when a lower-dimensional slice is better explained as part of a simpler higher-dimensional structure. It extends the idea to creativity: scientific and artistic novelty often requires moving outside the subspace of existing examples, and generative AI's apparent lack of "fundamental creativity" may reflect limited ability to find high-quality off-manifold points. The paper closes by comparing AI with evolution, where genotype mutation supplies an easy way to specify new phenotype directions while environmental selection supplies the quality test.

## Connections Found

The connect report found a tight cluster around discovery, reach, and oracle-limited synthesis. The strongest connection is [automated synthesis is missing good oracles](../notes/automated-synthesis-is-missing-good-oracles.md): Ord's generative-hyperpolation framing separates *reaching* new regions from *evaluating* whether those regions contain high-quality artifacts, which is the same generate-cheap / verify-expensive asymmetry the KB already names for synthesis. The paper also supports [discovery is seeing the particular as an instance of the general](../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md), because its ripple and cone examples formalize discovery as seeing a known slice as an instance of a higher-dimensional structure. It gives [first-principles reasoning selects for explanatory reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) a geometric vocabulary for reach beyond the observed subspace, and it supports [oracle strength spectrum](../notes/oracle-strength-spectrum.md) / [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) by making creative generation depend on some quality function or environmental test outside the training manifold.

Source-level siblings include [Geometry of Knowledge](./geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md), which provides an empirical latent-conditioning case for broadening generation diversity but lacks an OOD/low-quality oracle, and [GIANTS](./giants-generative-insight-anticipation-scientific-literature.ingest.md), which manufactures a soft oracle for one narrow discovery-like task by backcasting known downstream insights. [Creative Thinking](./creative-thinking-by-claude-shannon.ingest.md) is adjacent as a heuristic creativity source, but Ord contributes a formal taxonomy rather than an operator checklist.

## Extractable Value

1. **Hyperpolation as a name for off-subspace generalisation** -- The KB already talks about discovery depth, explanatory reach, and OOD generalisation, but lacks a compact term for "generalise into a dimension not spanned by the examples." Hyperpolation names that gap and makes it easier to distinguish novelty within a known axis from novelty that changes the space. [quick-win]

2. **Creative generation decomposes into specification plus quality evaluation** -- Ord's evolution analogy is directly useful: mutation can specify off-subspace candidates, but environmental selection evaluates quality. For AI and KB synthesis, generation may be cheap while the off-manifold quality test is the bottleneck. This sharpens the `automated-synthesis-is-missing-good-oracles` note. [quick-win]

3. **The discovery note gains a formal worked example** -- Seeing a sinuous curve as a slice of a ripple pattern is a clean instance of "particular as instance of general." It demonstrates that a more general higher-dimensional structure can be simpler than the observed slice, which strengthens the note's generative-model depth. [quick-win]

4. **Reach can be described geometrically** -- Interpolation and extrapolation remain on the affine hull of known data; hyperpolation leaves it. This gives the reach/adaptive-fit distinction a useful spatial metaphor, but it should remain metaphorical for KB methodology unless a specific representation space is defined. [just-a-reference]

5. **Specialized systems can learn hyperpolation functions without solving general creativity** -- Ord's image-to-video discussion distinguishes learning a specific hyperpolation task from learning to hyperpolate out of the whole training-data manifold. This is a useful caution for interpreting benchmark wins: a model may learn one supervised off-dimension mapping without acquiring broad creative reach. [experiment]

6. **Backcast and latent-diversity sources look like partial hyperpolation machinery** -- GIANTS manufactures a soft target for scientific-insight reconstruction; Geometry of Knowledge moves sampling into embedding space. Hyperpolation supplies a common vocabulary for comparing these as attempts to move beyond a current subspace while still needing a quality oracle. [experiment]

## Limitations (our opinion)

The paper is conceptually valuable but not empirical evidence that current AI systems lack fundamental creativity. The ML claims are plausible framing, not a benchmark result. "Training data manifold" and "space of ideas" are doing substantial metaphorical work, and the paper does not define a measurable representation space for artistic or scientific creativity.

Hyperpolation is not a well-posed mathematical problem by Ord's own account. The source's examples rely on simplicity priors and human recognition of elegant higher-dimensional forms. That is exactly why the concept fits the KB's oracle problem, but it also means the paper should not be cited as if it supplies a deterministic method.

The evolution analogy is illuminating but can overreach. Genotype mutation plus environmental selection gives a concrete generate/evaluate loop, but human creative work and KB synthesis often lack an equally strong external selector. Where selection is weak, hyperpolation names the problem rather than solving it.

Finally, "fundamental creativity" remains underdefined. The paper distinguishes interpolation/extrapolation/hyperpolation more cleanly than it defines creativity, so promotion should extract the geometric vocabulary and the generator/evaluator split, not the broad conclusion that AI lacks creativity.

## Recommended Next Action

Update [automated synthesis is missing good oracles](../notes/automated-synthesis-is-missing-good-oracles.md) with a short paragraph using hyperpolation to name the off-subspace version of synthesis: candidate generation can move outside the current idea manifold, but automation still stalls unless the system has a quality oracle for that new dimension. Cite this source alongside [Geometry of Knowledge](./geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md) and [GIANTS](./giants-generative-insight-anticipation-scientific-literature.ingest.md) as three complementary cases: conceptual vocabulary, latent-generation machinery, and backcast soft-oracle construction.
