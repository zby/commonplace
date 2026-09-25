---
description: "Zhang et al. frame LLM-assisted science as a hypothesis–experiment–observation loop, separating creative proposals from reliable tests while leaving autonomous discovery and self-revision unproven."
source: https://www.nature.com/articles/s44387-025-00019-5.pdf
captured: "2026-09-19"
capture: pdftotext
capture_scope: full-source
doi: "10.1038/s44387-025-00019-5"
genre: scientific-paper
snapshot_sha256: 161288e80d6230f9581d947f888a7fe181282021121950b79a3d5ae85acdfb9c
ingested: "2026-09-19"
occasion: "Reconsider the learning paradigm from Popperian epistemology: compare the epistemic process, computational realization, changeable representations and tests, fixed-model learning, reflection, and supporting evidence."
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, learning-theory, evaluation]
learning_claims: true
---

# Ingest: LLMs in the scientific method—from hypothesis to discovery

## Classification

A research perspective published in *npj Artificial Intelligence* in August 2025. It synthesizes cited applications and limitations and proposes a research agenda; it reports no new dataset or empirical study. Yanbo Zhang and twelve coauthors, including Jesper Tegner and corresponding author Hector Zenil, bring affiliations spanning AI, biology, computational science, and scientific discovery. That breadth supports its value as an interdisciplinary framing, not independent verification of the cited results.

## Summary

Zhang and colleagues distinguish LLMs that improve scientific productivity from prospective creative systems capable of posing new questions and discovering principles. They organize assistance around observation, hypothesis proposal, experimentation, and automation of the resulting loop. Their examples span literature retrieval, domain-specific foundation models, code and tool execution, formal checking, iterative feedback, and reusable skill libraries. They argue that speculative generation can help at the proposal stage while experiments require reliable assessment, and they emphasize negative results and human participation. The paper offers a conceptual agenda supported by heterogeneous cited cases, rather than a tested architecture for autonomous discovery; its proposed system-level confidence assessment and question-generating capabilities remain open problems.

## Quotes

No source quotes have been retained yet.

## Connections Found

For reconsidering the learning paradigm, this source supplies an independently argued scientific-process comparison. Its hypothesis–experiment–observation loop resembles the conjecture and testing core of the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md), but does not separately specify Commonplace's consequence derivation, acceptance, and integration obligations. The comparison supports separating an epistemic process from the computational machinery implementing it, without making the paper an origin or validation of the KB's six-phase construction.

The distinction between creative proposals and reliable assessment compares directly with [automated synthesis is missing good oracles](../notes/automated-synthesis-is-missing-good-oracles.md). The paper adds a concrete caution: an LLM can mistranslate a hypothesis into a formal language, so checking the translation need not test the original claim. Its discussion is conceptual support for scrutinizing that interface, not a controlled demonstration that evaluation is the dominant bottleneck. Its unresolved transition from useful tools to independent question generation also fits the boundary identified in [known-target discovery benchmarks](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md): success on supplied tasks leaves prospective problem selection and assessment to be established separately.

## Learning Claims (our opinion)

The source describes several mechanisms rather than one learning algorithm. Foundation models acquire distributed representations through training. Agent workflows instead feed observations, failed attempts, scores, and retrieved literature into later proposals and plans; generated programs can accumulate in a skill library. The authors also describe model training against formal feedback. Their analogy between a scientific community and a reinforcement-learning agent connects publication and experimentation to learning, but supplies neither a common objective nor a specified update rule for that community.

In Commonplace's terms, this makes the epistemic process broader than any one [theory builder](../notes/definitions/theory-builder.md). A hypothesis revised after an adverse experimental result meets condition 3 when the result counts against something the hypothesis says; the arrangement is a builder only if the revised hypothesis also guides later work (condition 2) and the result of the criticism is kept and shapes the next conjecture (condition 4); how long that result persists is a matter of grade. Whether the revision improves later work is a separate learning claim. Generating another candidate, retrieving a paper, or choosing a better plan does not alone show condition 3, and fitting model weights fails condition 1. The paper does not trace a single retained theory through criticism, revision, and a later round, so conditions 3 and 4 remain unestablished for the systems it surveys. Its own Popperian framing also combines verification language with falsification and reward search; these are the authors' organizing approximations, not a demonstration that successful optimization establishes a conjecture's truth.

Fixed model weights do not entail fixed system behavior in the agent examples: changing accessible histories, hypotheses, plans, code, and retrieved skills can change later actions. This is a mechanism for system adaptation without requiring a weight update at every step. It does not follow that each changed artifact is an addressable theory, that improvements persist across tasks, or that model retraining is dispensable. The review cites examples of both training and contextual adaptation without a matched comparison of their effectiveness.

The paper also makes representations consequential. It contrasts end-to-end domain models with separate encoders and tool-mediated composition, warns that converting scientific modalities can lose information, and lets agents write and compose programs. These mechanisms potentially enlarge the effective update space described in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Yet it does not establish a system that can revise every consequential representation, observation method, tool interface, or evaluation criterion. In its formal-checking examples, the chosen formalism and the fidelity of translation remain conditions of the result. In experimental workflows, changing a proposed experiment is different from validating or repairing the machinery that interprets its outcome. Gains within such arrangements do not select among alternative arrangements.

Finally, the paper's reflection methods revise answers and plans using feedback; this does not by itself meet the [reflective qualifier](../notes/definitions/theory-builder.md#qualifiers), under which the builder's own method is stated, consumed, and criticized as its other theories are. Its warning that self-correction without new information can degrade answers helps distinguish internal reconsideration from informative criticism. This is a useful constraint on the learning account, but the paper provides no direct test of a reflective theory builder or its claimed advantages.

## Extractable Value

1. **Separate the inquiry loop from its implementation.** The paper supplies a scientific-method comparison in which conjectures, tests, and observations can be implemented through humans, frozen-model agent workflows, trained models, and symbolic tools. Use it to clarify the level at which Commonplace claims learning, without treating those implementations as empirically interchangeable. [quick-win]

2. **Make the representation-to-test interface explicit.** A formal check may establish a property of an incorrectly translated hypothesis. This gives a concrete case for asking whether a test bears on the retained claim and whether that mapping can itself be criticized and revised; it does not demonstrate autonomous repair of that mapping. [quick-win]

3. **Test fixed-model adaptation and reflective revision separately.** Retaining failed attempts, revised hypotheses, and executable skills can alter behavior with an unchanged model. Determining whether this also revises a consumed self-representation needs a separate episode trace and later use test; the perspective does not provide one. [experiment]

4. **Retain negative results as inputs to further inquiry.** The paper argues that failure records can improve proposal and experiment selection, including at scientific-community scale. This is a plausible rationale for preserving refuted candidates and their test conditions, not comparative evidence for a particular KB retention policy. [just-a-reference]

## Limitations (our opinion)

The source is a perspective, not a new intervention or systematic meta-analysis. It reports no newly generated or analyzed dataset. Its application examples were not reproduced for this ingest, and their original studies were not independently assessed here. The cited improvements therefore cannot be pooled into a performance claim for the proposed scientific loop or used to establish which components caused improvement.

The reward-search formulation leaves important epistemic choices unspecified: what makes a question valuable, how novelty is distinguished from fabrication, how conflicting observations are resolved, and what justifies changing the test itself. The [discovery lifecycle](../notes/definitions/discovery-lifecycle.md) exposes some of these missing commitments by separating testing from acceptance. Internal agreement, human endorsement, and a formal proof of a translated statement supply different evidence; none automatically establishes empirical adequacy of the original claim.

The review contrasts end-to-end and compositional approaches but does not run a matched comparison holding task, information, and budget constant. It therefore leaves open whether gains attributed to richer workflows reflect better feedback, more attempts, retrieved information, human corrections, or a more effective representation. Its game-exploration examples also have supplied environments and action interfaces; the authors themselves acknowledge their distance from physical science. These cases suggest mechanisms without establishing open-ended revision of scientific representations and tests.

The proposal to exploit hallucinations as hypotheses remains speculative, as does the proposed predictive confidence measure for complete agent systems. Unreliable statements become useful conjectures only if they are treated as candidates and assessed; the paper offers no general method showing that screening their errors costs less than their proposal value. Its discussion of reflection and self-explanation likewise does not establish a reliable, persistent self-revising theory builder.

## Recommended Next Action

Closed: the [theory-builder definition](../notes/definitions/theory-builder.md) now draws the distinction. Revising a hypothesis is condition 3 applied to a theory about the subject; revising the representation and tests through which the hypothesis is criticized is revision reaching the machinery, which condition 3 allows and which, when that method is itself stated and criticized, makes the builder [reflective](../notes/definitions/theory-builder.md#qualifiers).
