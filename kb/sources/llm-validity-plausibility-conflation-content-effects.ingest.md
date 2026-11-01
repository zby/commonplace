---
description: "Steering study: LLMs encode syllogism validity and conclusion plausibility as aligned linear directions; each steers the other, and a task-difference vector cuts content effects"
source: https://arxiv.org/abs/2510.06700
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 76f334f8b80507ce299cd421e64b66bb51ae62b0aaf528a84b838e0a43f7d781
ingested: "2026-11-01"
occasion: "the epistemic-relevance-and-conceptual-blending workshop (kb/work/epistemic-relevance-and-conceptual-blending/) screened this paper as evidence-register entry E15 from an operator-supplied external review; the workshop needs the paper's own content on how validity and plausibility are represented and whether interventions on one affect the other. Ingest it as a tracked source; do not edit the workshop."
type: types/ingest-report.md
domains: [content-effects, activation-steering, syllogistic-reasoning, linear-representations]
tags: [llm-reliability]
---

# Ingest: How Language Models Conflate Logical Validity with Plausibility

## Classification

This is an empirical interpretability paper (arXiv 2510.06700v3, April 2026).
It runs behavioural measurements, linear probing by difference-in-means and
activation-steering interventions on ten open-weight models, and reports
regression statistics. Author: Leonardo Bertolazzi (University of Trento),
with Sandro Pezzelle (Amsterdam) and Raffaella Bernardi (Bozen-Bolzano). The
group built the syllogism dataset the paper reuses (Bertolazzi et al., EMNLP
2024), so the authors have prior work on LLM syllogistic content effects.
The authors say code and data are public; this ingest did not inspect them.

## Summary

The paper asks why LLMs show content effects, meaning that a syllogism's
validity verdict tracks whether its conclusion is true in the real world. It
tests ten instruction-tuned models (Qwen-2.5, Qwen-3, Gemma-3; 4B–32B) on
1,280 syllogisms covering all 64 premise types, crossed by validity and
conclusion plausibility. Plausibility is operationalized as binary real-world
truth. It also builds a separate true/false task over 1,056 conclusion
statements. All models show a zero-shot content effect, and CoT prompting
reduces it to near zero for most models. The representational analysis
extracts difference-in-means directions from the last-token residual stream,
with classes defined by the model's predicted labels rather than ground truth.
A single direction per concept flips the model's verdicts in late layers
(steering power near 1). In the layers where steering works, the validity and
plausibility directions have cosine similarity of about 0.5–0.64. Control
concepts score much lower: harmlessness and hypernymy, at roughly ±0.1–0.17.
Two further results test whether the alignment does causal work. First,
adding the plausibility direction flips validity verdicts, and the validity
direction flips true/false verdicts, in a subset of late layers. Second, in a
mixed-effects regression over 57 model–prompt pairs, alignment predicts
content-effect size (β = 0.557, p = 0.017), with prompting style held as a
separate predictor. Last, a task-difference vector (mean validity-task
activation minus mean plausibility-task activation), scaled by 1.5 and added
at one chosen layer, cuts the zero-shot content effect, for example from
0.348 to 0.072 on Qwen2.5-32B. Accuracy improves without parameter updates.
All of these findings hold only within one decomposition: last-token
residual-stream directions, mean-difference extraction and binary
classification prompts. The paper does not compare this decomposition with
alternatives such as sparse features or token-sequence dynamics. The authors
flag two open points. CoT lowers content effects while alignment and
cross-steering persist. The training-data cause, that valid arguments in text
are usually also sound, is only conjectured.

## Contribution assessment (our opinion)

Content effects in LLMs are well documented behaviourally, and a mechanism
account is a real gap; the paper's claim to be first to apply interpretability
here is plausible, though Valentino et al. (2026) already steer against the
same bias, and priority cannot be verified beyond the paper's own comparison. The
strongest contribution is the conjunction of three tests that could each have
failed: concept-specific alignment against two controls, bidirectional causal
cross-steering, and an across-model dose–response between alignment and
content effect. Together they make "entangled representation" a falsifiable
mechanism conjecture rather than a relabelling of the behaviour. The account
is weakened at its most important point, however: the largest behavioural
change in the data (CoT) leaves alignment unchanged, so alignment explains
cross-model variation within a prompting style but not the main lever that
removes the bias. The debiasing result is demonstrated but thinly controlled
(per-layer and α selection, no held-out selection reported in the read text),
and the "disentangling" interpretation of a task-mean difference vector is
asserted rather than tested. Likely significance: a useful, moderately
original mechanistic datum for one bias on one task family, whose generality
to other content effects remains a stated conjecture.

## Quotes

No source quotes have been retained yet.

## Connections Found

Within the occasion's question, this paper is the KB's only source that
measures how validity and plausibility are represented inside a model and
tests interventions on one against judgements of the other. Its answer is
that the two are linearly encoded, geometrically aligned, and causally
cross-coupled in both directions, and that a task-difference intervention
can reduce the coupling's behavioural effect. That answer holds within the
last-token residual-stream decomposition and for binary syllogism and
true/false prompts only.

Its closest companion is the behavioural anchor it cites. It
**compares-with** [Language models, like humans, show content effects on
reasoning](./language-models-like-humans-show-content-effects-on-reasoning.ingest.md)
on the same syllogism paradigm, at a different level of account: Lampinen
measures the bias, while this paper proposes and tests a representational
cause. The two diverge on CoT. Lampinen reads CoT as partly restoring
content-independent reasoning. Here, CoT lowers the content effect, but the
measured alignment and cross-steering persist. The two ingests therefore
should not be cited together as support for "CoT removes the content-bias
mechanism".

For theory, the paper is causal evidence for an interpreter-failure kind. It
**is-evidence-for** the currently unsourced "Content bias" entry in
[out-of-spec output is a failure of the interpreter, not the
spec](../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md).
Steering along plausibility changes validity verdicts on fixed syllogisms that
a conforming interpreter would judge by structure alone. Its debiasing vector
is a model-internal remedy that the note's remedy list does not include, and
API-level harnesses cannot reach it. It **is-evidence-for** [error correction works
above chance oracles with decorrelated
checks](../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)
as a qualification: the same aligned-direction pattern appears across three
model families, which supports a correlated error source, but its strength
varies by model and predicts effect size, so "shared" is graded. It bounds
[LLM context is composed without
scoping](../theory/llm-context-is-composed-without-scoping.md). The note groups
the content-effect paradigm with other prompt-steering phenomena. This paper
locates that member's steering signal in the task's own premise and
conclusion content, which no scoping or exclusion step can remove. It does
not test whether the other members share the mechanism. It **is-evidence-for**
[structured-prompt gains do not establish training-distribution
selection](../theory/structured-prompt-gains-do-not-establish-distribution-selection.md):
the CoT gain arrives with no change in the measured representational
signature, and the authors' training-data explanation remains untested. It
gives analogous, bounded support to [reasoning production is not reasoning
evaluation](../theory/reasoning-production-is-not-reasoning-evaluation.md),
where an evaluator accepts a plausible destination instead of checking the
route. The task differs, so the link supports the shape of the failure and
does not test the note's review-gate claim.

Among sources, it **compares-with** [semantic leakage in language
models](./semantic-leakage-lms-gonen.ingest.md) on where unlicensed content
influence is located. Gonen measures it behaviourally from injected unrelated
concepts; this paper locates it representationally in the task's own content.
This paper gives a mechanism for one paradigm only, so it must not be read as
settling the common-mechanism question across interference sources. It also
**compares-with** [symbols, neural networks and mathematical
intelligence](./symbols-neural-networks-mathematical-intelligence.ingest.md)
and [Fodor and Pylyshyn
(1988)](./fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md)
on how a learned approximation of a formal relation departs from it. The
learned validity concept shares geometry with a content concept that a formal
checker would ignore. That is a measured performance failure of structure
sensitivity, not a refutation of either position.

## Extractable Value

1. **Direct answer to the occasion's representation question** -- Within
   last-token residual-stream, difference-in-means directions, validity and
   plausibility are each single linear directions that control verdicts in
   late layers. Where steering is effective, they are aligned at cosine
   ~0.5–0.64, against ~0.1 and negative values for control concepts. The
   alignment is about the same under zero-shot and CoT prompting. This is a
   measured representational fact for one task family, not a general claim
   about how models encode epistemic properties. [quick-win]
2. **Interventions on one property move judgements of the other, both ways**
   -- Adding the plausibility direction flips validity verdicts, and adding the
   validity direction flips true/false verdicts, in a subset of late layers in
   all ten models. Qwen3-4B is the exception, with only moderate cross-steering
   (~0.5). This is the occasion's causal datum. The vectors are added at full
   unnormalized magnitude, with the sign chosen to oppose the model's current
   verdict. So the result shows that the overlapping component can flip a
   decision. It does not show how much ordinary plausibility variation moves
   validity at inference time. [quick-win]
3. **Alignment predicts bias across models but not the CoT gain** -- Higher
   alignment predicts a larger content effect across model–prompt pairs, yet
   CoT reduces the content effect sharply while alignment and cross-steering
   persist. The mechanism therefore explains variation within a prompting
   style but not the main remedy. This is a usable warning against inferring
   a fixed bias from representational geometry, or a fixed representation from
   behavioural repair. [quick-win]
4. **A plausibility-swapped check design** -- The paper's 2×2 design (valid or
   invalid × plausible or implausible conclusion) and its content-effect
   metric give a direct template for a check that holds structure fixed and
   varies content. That is the decorrelation lever that error-correction
   theory asks for against a correlated bias. Because content-effect is a
   difference metric, such a check should report per-cell accuracy, not only
   the difference. [experiment]
5. **Model-internal remedy layer** -- The task-difference debiasing vector
   reduces content effects without retraining. It shows that a remedy layer
   exists below the prompt and harness surfaces the KB's remedy taxonomy
   covers. Hosted-API agents cannot reach that layer, so its value to
   Commonplace is mainly taxonomic: it adds a scope sentence to the remedy
   list, not a usable tool. [just-a-reference]
6. **Endogenous versus exogenous interference** -- This paper places the
   content-effect signal in the judged task's own content. That sharpens a
   distinction the KB has not named. Exogenous interference, from injected or
   irrelevant context, responds to scoping and exclusion. Endogenous
   interference requires varying the content or intervening inside the model.
   It remains a log-level observation until a note states the mechanism.
   [deep-dive]

## Limitations (our opinion)

The central causal claim is bounded by how the directions are built and
applied. Both concepts are extracted as difference-in-means over the
model's own predicted labels, from binary-answer prompts whose positive
classes are both affirmative answers ("valid", "true"). A shared
affirmation or answer-correctness direction is a simpler account that the
controls only partly exclude. The harmlessness and hypernymy controls are
tested for cosine similarity. The read text reports no cross-steering control,
for example whether a harmlessness vector also flips validity. Steering adds
unnormalized vectors at the magnitude needed to flip a decision. Flipping by
an overlapping component is close to guaranteed at cosine ~0.6. The causal
test is therefore less severe than "plausibility drives validity at inference
time" suggests.

The alignment-to-content-effect regression has 57 points from ten models in
three families, with p = 0.017. Model capability, family and alignment are not
separated. The paper's own data show that alignment does not change when CoT
removes most of the bias. So alignment is at most one contributor, and the
paper does not explain the CoT gain, as the authors acknowledge.

The debiasing result is the least controlled. The scale α was grid-searched
on the two headline models, and the intervention layer was picked per model
from per-layer curves against the baseline. The read text does not show that
this selection used held-out data. The vector is a difference of task means.
It therefore also encodes the instruction and format differences between the
syllogism and true/false prompts. Its description as "disentangling" validity
from plausibility is an interpretation, not a tested orthogonalization.
Because content-effect is a difference between cells, it can fall when the
congruent cells get worse. The Qwen2.5-32B accuracy gain is small (81.62 to
82.21) while the content effect falls from 0.348 to 0.072. The main text does
not report per-cell post-intervention accuracy for that model, so the debiased
judgements may be less content-driven without being more logical.

There are minor internal inconsistencies. The main-text cosine range is
0.48–0.64, while the Figure 3 caption gives 0.53–0.64. Qwen3-14B CoT figures
differ between Table 1 (96.70, CE 0.014) and Table 3 (98.47, CE 0.017).
Qwen3-14B's post-debiasing zero-shot accuracy is reported as exactly 96.70,
the same as the Table 1 CoT accuracy. Together, these warrant checking numbers
before reuse.

Scope is narrow. The paper tests categorical syllogisms over ten taxonomic
term triples, with binary real-world truth as "plausibility". It tests no
graded plausibility, natural argument text or reasoning beyond syllogisms.
It analyses only last-token residual representations; the authors name sparse
features and sequence-level dynamics as untested alternatives. The
training-data explanation, that valid arguments are usually sound in text, is
an untested conjecture.

## Recommended Next Action

Cite this ingest in the workshop's evidence-register entry E15 as the answer to
its representation-and-intervention question. Record three bounded findings:
aligned linear directions within the last-token decomposition, bidirectional
cross-steering at full-magnitude vectors, and a content-effect-reducing
task-difference vector whose layer and scale were selected rather than
pre-registered. Also record that CoT lowers the bias without changing the
measured alignment.
