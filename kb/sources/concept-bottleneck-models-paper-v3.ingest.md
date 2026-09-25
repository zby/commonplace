---
description: "Supervised concept interfaces enable test-time correction, but prediction accuracy alone does not establish correction benefit; evidence is bounded by fixed concepts and oracle interventions."
source: https://arxiv.org/pdf/2007.04612v3
captured: "2026-09-18"
ingested: "2026-09-18"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 091a335dd7648510a3354a35a48025b019e5625cf2a814ce1800e44a9357e008
type: kb/sources/types/ingest-report.md
domains: [interpretability, supervised-learning, intervention, concept-representations]
learning_claims: true
---

# Ingest: Concept Bottleneck Models, full v3 paper

## Classification

Scientific paper by Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen Mussmann, Emma Pierson, Been Kim, and Percy Liang, affiliated with Stanford University and Google Research. This is the December 2020 arXiv v3 of their ICML 2020 paper. Its evidence comprises supervised vision benchmarks, intervention experiments, architectural and training comparisons, a synthetic background-shift experiment, and a restricted linear-regression analysis. The full paper, including appendices, is the primary observation.

## Summary

Concept bottleneck models learn an input-to-concept predictor and a concept-to-label predictor, with all label prediction passing through a layer supervised against human-specified concepts. On knee osteoarthritis grading (OAI) and bird identification (CUB), the paper compares independent, sequential, and joint training with standard predictors. Accuracy costs depend on the task: OAI bottlenecks match or improve on the standard model, while CUB bottlenecks lose accuracy, with joint training closing much of the gap. Under these fixed annotated concept sets, oracle correction of predicted concepts can improve predictions, but ordinary task and concept accuracy do not determine intervention benefit. On OAI, changing the concept-to-label map from nonlinear to linear reduces correction benefit despite similar pre-intervention accuracy; a separate low-concept-loss control learns worse concept alignment and can become less accurate after correction. CUB additionally exposes dependence on the numerical interface used for correction. The paper provides evidence for testing an editable intermediate through its downstream behavior, without establishing persistent learning from corrections or transfer to prose rationales.

## Quotes

- **Source extract (verbatim):** By construction, we can intervene on these concept bottleneck models by editing their predicted concept values and propagating these changes to the final prediction.
  - **Source location:** Abstract: editing predicted concepts at test time.

- **Source extract (verbatim):** To study this setting, we use an oracle that can query the true value of any concept for a test input.
  - **Source location:** Section 6, Test-time intervention: oracle protocol.

- **Source extract (verbatim):** Specifically, the joint model with λ = 0.01 learned a concept representation that was not as well-aligned with the true concepts, and replacing ĉ with the true c at test time slightly increased test error (“control” model in Figure 4-Left).
  - **Source location:** Section 6.1, Intervening on OAI: low-concept-loss control, Figure 4-left.

- **Source extract (verbatim):** c → y model from the 3-layer multi-layer perceptron used throughout the paper to a single linear layer. Surprisingly, test-time intervention was less effective here compared to the non-linear counterparts (Figure 4-Mid), even though task and concept accuracies were similar before intervention (concept RMSEs of the sequential and independent models are not even affected by the change in c → y).
  - **Source location:** Section 6.1, Intervening on OAI: linear versus nonlinear downstream predictor, Figure 4-middle.

- **Source extract (verbatim):** Altogether, these results suggest that task and concept accuracies alone are insufficient for determining how effective test-time intervention will be on a model.
  - **Source location:** Section 6.1, conclusion of the two OAI ablations.

- **Source extract (verbatim):** We emphasize that we study interventions on the value of a predicted concept within the model, not on that concept in reality.
  - **Source location:** Section 2, Causal models: within-model rather than real-world intervention.

- **Source extract (verbatim):** Finally, how might we have models learn from interventions to avoid making similar mistakes in the future?
  - **Source location:** Section 8, Discussion: Intervention effectiveness, future-work question.

## Connections Found

The strongest role is a worked empirical analogy for [Revision guided by rationale needs faithfulness, not just legibility](../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md). Section 6 distinguishes two failures already separated in that note: insufficient concept alignment under low concept-loss weight, and poorer intervention benefit from a linear downstream predictor despite similar initial accuracy. These results concern a supervised numerical interface with a prescribed concept vocabulary and oracle replacements. They support evaluating correction behavior separately from inspection or prediction accuracy; extending that requirement to retained natural-language rationales is Commonplace's inference, not an experiment in the paper.

The paper also supplies a useful comparison for [Explicit retention provides direct targets for selective revision](../notes/only-explicit-retention-is-durable-writable-and-addressable.md): numerical activations can have named edit targets when architecture and supervision install them. This is instance-level addressability. Replacing a concept value does not edit a durable predictive rule or show that the model avoids the same mistake later.

## Learning Claims (our opinion)

The learning mechanism is supervised parameter fitting from input, concept, and label annotations. Independent training fits the label predictor on true concepts; sequential training fits it on the concept predictor's outputs; joint training updates both predictors using task and concept losses. These choices change what the downstream predictor learns to consume. Independent models consequently face predicted rather than true concepts at ordinary test time, while full oracle replacement restores their training interface. The converse mismatch can affect sequential and joint models. The paper presents this as an explanation for differences in intervention behavior, not as a complete causal account of every observed difference.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the important contribution is a designed, inspectable correction surface inside a neural computation. The concept layer partly meets condition 1: each unit is tied to a named, human-specified concept, so a correction can point at what that unit asserts about one instance. The fitted input-to-concept and concept-to-label maps, which carry the general theory, are weights and do not meet it. The label predictor consumes the concept values, so a corrected value changes the prediction (condition 2 for the concept layer). Condition 3 is not met: training is gradient fitting, and the test-time corrections are oracle replacements of instance estimates, not criticism of what a stated theory says. Condition 4 fails and settles the verdict: the corrections update no retained state, and Section 8 leaves learning from interventions as future work. The system is outside. The paper qualifies any substrate-wide claim that numerical representations cannot expose selective edit targets; it shows no learning from corrections.

The concept vocabulary, annotations, and input–concept–label partition remain supplied by the experimenter. Joint fitting can change how concepts are represented, but does not discover and validate a replacement concept vocabulary. As in [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within this update space is not evidence that the chosen concepts are generally sufficient. The paper does compare bottleneck, ordinary, and multitask architectures, and varies the downstream function and numerical interface. Those comparisons test particular design choices; none establishes the superiority of human-specified decomposition in general. Conversely, a potentially incomplete concept set does not by itself prove information loss: continuous outputs can carry information beyond their intended concept interpretation, a possibility the authors discuss as a concern about alignment.

## Extractable Value

- **[quick-win] Direct evidence for evaluating correction separately.** In the OAI linear-versus-nonlinear ablation, similar pre-intervention task and concept accuracy accompanies different correction benefit under the same supplied concept interface. Keep this distinct from the low-concept-loss alignment failure. This sharpens the existing rationale note's analogy without turning it into evidence about prose.
- **[experiment] Treat the correction interface as an experimental variable.** On CUB, sequential and joint models consume concept logits; intervention sets these to training-distribution percentiles. A joint model consuming probabilities instead improves intervention behavior while raising ordinary task error from 0.199 to 0.224. The reusable experimental lesson is to compare the downstream effects of the actual edit representation. The result does not isolate a universal advantage of probabilities, because the interface change also changes training and ordinary performance.
- **[just-a-reference] Keep selective correction separate from durable learning.** Named neural activations furnish a concrete comparison for the explicit-retention note's operation-based account of addressability. The demonstrated operation changes one prediction; the paper supplies no retention or later-use test of the correction.
- **[just-a-reference] Retain bounded data-efficiency and robustness results.** With the supplied clinical concepts, an OAI sequential model using approximately one quarter of the dataset performs similarly to the standard model. In TravelingBirds, bottlenecks reduce error under deliberately reassigned backgrounds when concepts are less tied to those backgrounds than species labels. These are useful cases of supervised structure helping in specified regimes, not evidence for the KB's retained-theory sample-efficiency conjecture or arbitrary concept choices.

## Limitations (our opinion)

The evidence covers two vision tasks whose concept annotations are unusually convenient. OAI's ten clinical concepts are used in grading the target itself. CUB uses 112 processed attributes, replacing noisy instance annotations with majority-voted class-level concepts. Neither task tests whether a learner can acquire an adequate concept vocabulary or revise a deficient one. The limited accuracy cost should therefore not be generalized to domains without comparable annotations or concept coverage.

Human collaboration is simulated with an oracle. OAI uses a fixed intervention order selected on held-out validation data. CUB queries concept groups in random order, applies visibility checks, and assumes correct class-level concept values. These protocols differ in query meaning and selection; their gains do not estimate a common human-effort budget. No human study establishes net benefit after expert mistakes, consultation time, or disagreement.

The intervention evidence also has two distinct boundaries. A correction's effect depends on both its semantic alignment and the downstream predictor's response; the authors leave the linear-versus-nonlinear difference incompletely explained. Moreover, Section 2 explicitly distinguishes changing a prediction inside the model from changing a real-world cause. Improved prediction after concept replacement establishes neither world-causal validity nor a faithful account of how a human or prose-based learner formed its judgment.

The TravelingBirds experiment deliberately preserves useful concept–label relationships while disrupting background–label correlations. It does not test arbitrary distribution shifts. The appendix's data-efficiency argument assumes a well-specified linear model and favorable concept dimensionality and noise; it does not establish the same result for neural learning generally. Reported outcomes remain paper evidence: no implementation was inspected or experiments reproduced for this ingest.

## Recommended Next Action

Update the concept-bottleneck citation in [Revision guided by rationale needs faithfulness, not just legibility](../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) to this full-paper ingest, using a snapshot-required link for its Section 6 comparison and preserving the note's explicit boundary between supervised concept interventions and retained prose rationales.

---

Relevant Sources:

- [Concept Bottleneck Models, arXiv v3](https://arxiv.org/pdf/2007.04612v3) — derived-from: primary paper, especially Sections 3–8 and the experimental appendices
