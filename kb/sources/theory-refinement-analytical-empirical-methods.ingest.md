---
description: "EITHER uses proof-guided diagnosis and induction to repair an imperfect external Horn-clause theory, with bounded evidence for accuracy and sample efficiency."
source: https://doi.org/10.1016/0004-3702(94)90028-0
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
capture_url: https://www.cs.utexas.edu/~ai-lab/pubs/either-aij-94.pdf
genre: scientific-paper
snapshot_sha256: 2b96da859254945fe46dc4ef1a07ada8a1d9357bfb41f592813bc3a9ae70af29
ingested: "2026-08-31"
occasion: "Determine what this source establishes about learning from an explicit but fallible theory: how theory guides inference, search, or generalization; how empirical success or failure bears on the theory; how defects are localized and repaired; and whether the revised theory changes later learning. Distinguish a theory of an external problem domain from a reflective theory of the learner's own software organization. This is source ingestion, not a request to confirm the proposed synthesis."
type: kb/sources/types/ingest-report.md
domains: [learning-theory, theory-refinement, knowledge-base-revision, symbolic-machine-learning]
---

# Ingest: Theory Refinement Combining Analytical and Empirical Methods

## Classification

This is a scientific paper: it specifies the EITHER algorithm, analyzes its complexity and consistency property, and reports repeated train/test experiments on two expert classification rule bases. Authors: Dirk Ourston and Raymond J. Mooney, the system's developers, writing from Science Applications International Corporation and the University of Texas at Austin and evaluating their own method.

## Summary

EITHER treats an approximate acyclic propositional Horn-clause classification theory as both prior knowledge and an addressable repair surface. Deduction identifies misclassified examples and the proofs of false positives; abduction constructs partial proofs for false negatives; greedy near-minimum covers nominate rules or antecedents; and an ordered sequence of retraction, generalization or specialization, ID3-based induction, and inverse-resolution compression repairs the theory while preserving or creating intermediate concepts. Given consistent training examples, the procedure returns a theory consistent with them. On DNA promoter recognition and soybean disease diagnosis, the revised theories achieved higher held-out accuracy than ID3 across the plotted nonzero training sizes, but this is evidence for the compound EITHER configuration in two constrained domains, not for every fixed representation or repair choice within it.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a historical technical basis for [theory-mediated system learning](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md): an explicit fallible theory shapes inference and repair, but the theory represents an external classification domain rather than the learner's own software organization. It is also evidence for [diagnostic richness constraining outer-loop learning](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), because complete and partial proof structures nominate repair sites and restrict the examples passed to induction instead of merely scoring finished candidates.

Its learning curves provide bounded evidence for the intermediate premise in [theory-mediated learning may improve sample efficiency](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), not for controlled-shift reuse or total learning cost. Its fixed observables, category partition, Horn language, repair operators, inductive learner, and batch objective also make it a concrete case of [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): improvement validates the compound setup in the tested domains but does not isolate or vindicate those fixed choices.

## Extractable Value

1. **Proof-guided theory repair is a concrete theory-mediated pipeline** -- Labeled feature vectors and the theory's complete or partial proof structures condition search; deduction and abduction localize suspect rules or antecedents; induction then constructs a correction from an analytically selected subset of examples. This is stronger than using a theory only as extra context. [quick-win]
2. **Empirical failure and success constrain different parts of repair** -- False positives expose overly general proof paths, false negatives expose missing proof support, and already correct examples bound how far a proposed generalization or specialization may extend. Held-out classification then tests the revised compound theory beyond exact training consistency. [quick-win]
3. **Failure localization and repair admission are separate stages** -- Proof structure nominates an edit site, while ordered repair operators reject changes that create the opposite error and the final full-training-set check admits the revision. This supplies a formal comparison case for contemporary systems that localize failures with ownership or model-generated traces but use different promotion gates. [deep-dive]
4. **The effective update space is unusually explicit** -- EITHER can retract, generalize, specialize, add, relocate, and compress Horn rules, including creating intermediate concepts, but can express only mappings available to its acyclic extended propositional Horn hypothesis class. The observables, disjoint categories, closed-world assumption, edit vocabulary, ID3 learner, syntactic-minimality bias, and consistency objective remain fixed outside learning. [quick-win]
5. **The sample-efficiency evidence supports only a bounded prior-knowledge claim** -- In two tasks, EITHER outperformed its ID3 component without an initial theory and sometimes reached a given accuracy with fewer examples. The result does not isolate proof-based diagnosis, establish reuse under a structured shift, or compare total compute and knowledge-engineering cost. [just-a-reference]
6. **The repaired theory is external, not reflective** -- The revised objects encode DNA promoter or soybean disease classifications. EITHER does not represent or revise its own deduction, abduction, induction, control flow, evaluator, software organization, or purpose, so it supplies an epistemic lineage for reflective theory learning rather than evidence of reflection itself. [quick-win]
7. **Changed later learning is not established** -- EITHER runs in batch mode and evaluates the resulting theory on held-out classification. The paper argues that lower-level shared-rule repair can benefit other categories and cites separate cross-category-transfer work, but it does not run a later learning episode in which the revised theory changes subsequent search, diagnosis, or revision. [experiment]

## Limitations (our opinion)

The empirical case is narrow: two small expert classification domains, fixed datasets, and ID3 as the principal no-theory comparator. There is no matched ablation for proof diagnostics, greedy covering, operator order, intermediate-concept creation, or the quality of the starting theory. The soybean study further depends on a lossy translation from probabilistic expert rules to Horn clauses and a custom flexible test procedure after the translated theory's standard classification accuracy fell far below the originally reported rules. Exact consistency on the training examples neither guarantees a syntactically minimal repair, which EITHER only approximates heuristically, nor establishes robust generalization.

The learner observes one batch of labeled examples over fixed observable features and proof structures. Its available responses are the supplied Horn-rule edits and compression operators; its expressible mappings remain acyclic extended propositional Horn classifiers. Consequently, improvement shows that this compound decomposition sufficed for the tested cases, not that its features, category partition, hypothesis class, or repair strategy were necessary or preferable. The stated inability to handle negation as failure, relational structure, probabilistic rules, overlapping categories, and examples of intermediate concepts marks consequential repairs outside its effective update space.

Finally, the source studies a theory of an external problem domain, not a causally connected theory of the learner's own organization. It contains no longitudinal feedback loop, no revision of the learning machinery, and no experiment showing that one revised theory governs a later learning episode. Its results therefore should not be generalized to reflective or open-ended self-improvement without a new experiment.

## Recommended Next Action

Update [Theory-mediated system learning combines runtime self-modeling with theory refinement](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md) to replace its direct DOI citation with a `(snapshot required)` link to this ingest and expand the EITHER case with the proof-guided repair mechanism, fixed Horn update space, and absence of reflective or later-learning evidence.
