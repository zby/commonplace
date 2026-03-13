---
description: Error correction for LLM output is viable whenever the oracle has discriminative power (TPR > FPR) and checks are decorrelated — amplification cost scales with 1/(TPR-FPR)² and independence of errors
type: note
tags: [llm-interpretation-errors]
status: seedling
---

# Error correction works with above-chance oracles and decorrelated checks

Error correction builds reliable systems from unreliable parts through redundancy and verification. The [MAKER paper](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) demonstrates this for LLM execution tasks: voting across independent samples achieves zero errors over a million steps. But MAKER uses hard oracles (deterministic verification). The general principle is broader — error correction works whenever the oracle has discriminative power, provided the checks are sufficiently decorrelated. This note develops both conditions: what discriminative power means precisely, how many repetitions it costs, and why decorrelation is the binding constraint for LLM-based checks.

## The amplification condition: TPR > FPR

The classical result is [Condorcet's jury theorem](https://ar5iv.labs.arxiv.org/html/2002.03153) (1785): if each voter independently chooses correctly with probability p > 1/2, majority vote converges to the correct answer as the number of voters grows. The ML equivalent is [strength of weak learnability](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) — weak classifiers (barely above chance) can be boosted into arbitrarily accurate ones.

But "above chance" needs to be stated carefully. The naive version — "accuracy > 50%" — is misleading when classes are imbalanced, which is the normal case for LLM output (most outputs are roughly correct).

Consider an oracle that checks an LLM output and says "accept" or "reject." Define:

- **TPR** (true positive rate) = P(oracle says "accept" | output is correct)
- **FPR** (false positive rate) = P(oracle says "accept" | output is incorrect)

The oracle has discriminative power when **TPR > FPR** — it is more likely to accept correct outputs than incorrect ones. This is the condition for amplification to work, regardless of the base rate of correct outputs.

Why not aggregate accuracy? Suppose 90% of LLM outputs are correct. An oracle that always says "accept" has 90% aggregate accuracy — well above 50% — but TPR = 1.0 and FPR = 1.0. It says the same thing regardless of correctness. Majority voting over N copies still always says "accept"; no amplification occurs. The Condorcet theorem's "p > 1/2" condition sidesteps this by assuming equiprobable classes, where aggregate accuracy > 50% *is* equivalent to TPR > FPR. The [boosting formulation](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) handles imbalanced classes directly: a weak learner must achieve > 50% accuracy on *any reweighted distribution* over instances. An always-accept oracle fails this because on a distribution that upweights incorrect outputs, it drops below 50%.

### How discriminative power determines cost

| Oracle | TPR | FPR | Gap | 10 votes on correct (expected accepts) | 10 votes on incorrect (expected accepts) |
|--------|-----|-----|-----|---------------------------------------|----------------------------------------|
| Strong | 0.8 | 0.3 | 0.5 | ~8 | ~3 |
| Weak but useful | 0.55 | 0.45 | 0.1 | ~5.5 | ~4.5 |
| Always "accept" | 1.0 | 1.0 | 0 | ~10 | ~10 |
| Biased but flat | 0.7 | 0.7 | 0 | ~7 | ~7 |

The strong oracle separates with 10 repetitions. The weak oracle needs ~100 repetitions to reliably separate (the binomial distributions overlap heavily at 10). The last two never separate regardless of repetitions.

The scaling law: the number of repetitions needed grows as **1/(TPR - FPR)²**. We are separating two binomial distributions whose means differ by (TPR - FPR), and each distribution's standard deviation scales as 1/sqrt(N). To get the means separated by several standard deviations, N must grow quadratically as the gap shrinks:

- Gap of 0.5 → ~4 repetitions
- Gap of 0.1 → ~100 repetitions
- Gap of 0.01 → ~10,000 repetitions
- Gap of 0 → no number of repetitions helps

This makes the practical question not "how strong is your oracle?" but "how cheaply can you get TPR > FPR?" — because amplification handles the rest, given decorrelation.

## Decorrelation: the binding constraint for LLM checks

Signal strength alone is not enough. Repetitions must produce independent errors. If all checks share the same systematic bias — same model, same prompt, same training data — voting converges to the shared bias, not to the truth. Correlated noise does not average out.

The ceiling on reliability is the product of signal strength and independence. A strong but correlated oracle plateaus fast. A weak but independent oracle converges slowly but surely. The design problem is maximising this product per unit cost.

Since LLMs have systematic biases, naive repetition (same prompt, same model) produces highly correlated checks — the effective TPR-FPR gap after accounting for correlation is smaller than the nominal gap. Decorrelation strategies must actively disrupt the sources of correlation:

- **Vary the prompt** — rephrase the question, change the framing, alter the instruction style.
- **Vary the model** — different models have different failure modes. But model diversity alone has limits (see content bias below).
- **Metamorphic transformations** — change the *input* structurally (reorder evidence, remove context, translate and back-translate) so that correlated biases are disrupted. Each transformation probes a different axis, producing structurally independent signal from a single underlying oracle. This makes metamorphic checks particularly valuable: they introduce decorrelation by design.
- **Orthogonal check dimensions** — combine structural checks (formatting) with semantic checks (consistency) with metamorphic checks (invariance). Each catches a different class of errors, so their failures are structurally independent.

### Content bias: an empirically measured correlation source

[Lampinen et al. (2024)](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) demonstrate a concrete source of correlated error: content effects on reasoning. LLMs reason more accurately when semantic content supports the correct inference (familiar, believable premises) and less accurately on abstract or belief-violating content — mirroring human performance patterns across syllogisms, NLI, and the Wason selection task.

The critical finding for decorrelation: content effects are shared across architecturally different models (Chinchilla, PaLM 2, GPT-3.5) and survive both scaling and instruction tuning (Flan-PaLM 2). **Model diversity alone is insufficient for decorrelating reasoning errors** driven by content bias. Voting across different models on the same content-biased problem converges to the shared bias, not to the truth — exactly the correlated-noise failure that defeats amplification.

The implication: when checks involve reasoning about semantic content, decorrelation requires varying the **semantic framing** — rephrasing premises, abstracting concrete terms, or using [metamorphic transformations](./process-structure-and-output-structure-are-independent-levers.md) that disrupt the content-correctness alignment. Chain-of-thought prompting partially achieves this by improving performance on abstract/unfamiliar conditions without degrading familiar ones, suggesting that [process structure](./process-structure-and-output-structure-are-independent-levers.md) can serve as a content-bias decorrelation mechanism.

## Ways to construct above-chance oracles

Given the amplification condition and the decorrelation requirement, the design question becomes: what mechanisms can cheaply produce TPR > FPR with structurally independent failure modes?

- **Structural checks** — does the output have required sections, valid formatting, correct length? Deterministic, cheap, but narrow. TPR ≈ 1 for well-formed correct outputs, FPR < 1 for malformed incorrect ones.
- **Self-consistency** — do multiple generations agree? MAKER's core approach. Decorrelation comes from sampling randomness, which may be limited.
- **Metamorphic checks** — does the answer stay the same under rephrasing, reordering, or irrelevant context addition? No ground truth needed. Each transformation probes a different failure mode, combining signal (invariance violation → likely error) with decorrelation (each transformation is an independent probe).
- **LLM-as-judge** — does another model (or the same model with a different prompt) rate this as good? Signal is soft but often has TPR > FPR. Decorrelation depends on how different the judge's failure modes are from the generator's.
- **Cross-document consistency** — does this contradict established content? Uses the existing knowledge base as ground truth.

## Implications for the knowledge system

Structured document types already function as error correction: they constrain the output space (structural checks) and steer the model toward [higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md). The framework developed here suggests going further:

- **Validation scripts** are hard-oracle checks — cheap, deterministic, but narrow.
- **Multiple generation + voting** could improve seedling quality before human review.
- **Metamorphic checks on claims** — does rephrasing the evidence change the conclusion? Does removing one piece of evidence weaken it proportionally? These test argument robustness without requiring ground truth.
- **Cross-note consistency** — does a new claim contradict existing notes? This uses the KB itself as an oracle.

The progression from [oracle hardening](./oracle-strength-spectrum.md) to error correction is: first construct an oracle with TPR > FPR, then amplify through decorrelated repetition. [Codification](./codification.md) moves components toward harder oracles, making error correction cheaper — but it is not a prerequisite. Even weak oracles support error correction if you can decorrelate.

---

Relevant Notes:

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — foundation: the spectrum of oracle strength this note extends with error correction as an amplification mechanism
- [MAKER paper](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — example: voting with hard oracles achieves O(s ln s) scaling for million-step tasks; this note generalises beyond hard oracles
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — enables: structured templates are one error-correction mechanism (distribution selection constrains output); this note places them in the broader design space
- [reliability dimensions map to oracle hardening stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — extends: reliability dimensions are specific oracle-hardening moves; error correction amplifies whatever oracle strength they achieve
- [codification](./codification.md) — parallel: codification moves toward harder oracles, making error correction cheaper; but error correction doesn't require hard oracles
- [spec mining as codification](./spec-mining-as-codification.md) — feeds: spec mining manufactures the oracles (TPR > FPR) that error correction then amplifies through decorrelated repetition
- [operational signals that a component is a relaxing candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — enables: metamorphic checks double as relaxing signal detectors — measuring paraphrase brittleness classifies components on the bitter lesson spectrum
- [content effects on reasoning tasks](../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.ingest.md) — grounds: content bias is shared across model families and survives scaling/instruction tuning, making it a concrete example of correlated error that model diversity alone cannot decorrelate
- [process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md) — speculative: process constraints (forced reasoning steps) may serve as content-bias decorrelation mechanisms
