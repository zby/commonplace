---
description: Error correction for LLM output is viable whenever the oracle has discriminative power (TPR > FPR) and checks are decorrelated — amplification cost scales with 1/(TPR-FPR)² and independence of errors
type: note
areas: [learning-theory]
status: seedling
---

# Error correction works with above-chance oracles and decorrelated checks

Error correction is basic engineering: build reliable systems from unreliable parts through redundancy and verification. The [MAKER paper](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) demonstrates this for LLM execution tasks using voting across independent samples, achieving zero errors over a million steps. But MAKER uses hard oracles (deterministic verification). The general principle is broader: error correction works whenever your oracle has discriminative power, provided your checks are sufficiently decorrelated.

## Two levers: signal strength and decorrelation

Amplification through repetition — running a check multiple times and voting — is bounded by two independent factors:

**Signal strength.** The oracle must have discriminative power — it must behave differently on correct vs incorrect outputs (see analysis below). The cost of amplification scales with the square of the inverse gap: weaker oracles need quadratically more repetitions.

**Decorrelation.** Repetitions must produce independent errors. If all checks share the same systematic bias — same model, same prompt, same training data — voting converges to the shared bias, not to the truth. Correlated noise doesn't average out.

The ceiling on reliability isn't either factor alone — it's the product. A strong but correlated oracle plateaus fast. A weak but independent oracle converges slowly but surely. The design problem is maximising the product of signal and independence per unit cost.

## When can an oracle be amplified? A concrete analysis

The classical result here is [Condorcet's jury theorem](https://ar5iv.labs.arxiv.org/html/2002.03153) (1785): if each voter independently chooses correctly with probability p > 1/2, majority vote converges to the correct answer as the number of voters grows. The ML equivalent is [strength of weak learnability](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) — weak classifiers (barely above chance) can be boosted into arbitrarily accurate ones.

But "above chance" needs to be stated carefully. The naive version — "accuracy > 50%" — is misleading when classes are imbalanced, which is the normal case for LLM output (most outputs are roughly correct).

### The right condition: TPR > FPR

Consider an oracle that checks an LLM output and says "accept" or "reject." Define:

- **TPR** (true positive rate) = P(oracle says "accept" | output is correct)
- **FPR** (false positive rate) = P(oracle says "accept" | output is incorrect)

The oracle has discriminative power when **TPR > FPR** — it is more likely to accept correct outputs than incorrect ones. This is the condition for amplification to work, regardless of the base rate of correct outputs.

### Why aggregate accuracy is not the right measure

Suppose 90% of LLM outputs are correct. An oracle that always says "accept" has:
- Aggregate accuracy: 90% (well above 50%)
- TPR = 1.0, FPR = 1.0
- **Zero discriminative power** — it says the same thing regardless of correctness

Majority voting over N copies of this oracle still always says "accept." No amplification occurs despite high accuracy.

The Condorcet theorem's "p > 1/2" condition avoids this problem by assuming equiprobable classes — in which case aggregate accuracy > 50% *is* equivalent to TPR > FPR. But in practice, classes are imbalanced, and the distinction matters.

The [boosting formulation](https://en.wikipedia.org/wiki/Boosting_(machine_learning)) handles this cleanly: a weak learner must achieve > 50% accuracy on *any reweighted distribution* over instances. An always-accept oracle fails this because on a distribution that upweights incorrect outputs, it drops below 50%.

### Concrete examples

| Oracle | TPR | FPR | Discriminative? | 10 votes on correct (expected accepts) | 10 votes on incorrect (expected accepts) |
|--------|-----|-----|-----------------|---------------------------------------|----------------------------------------|
| Strong | 0.8 | 0.3 | Yes (gap 0.5) | ~8 | ~3 |
| Weak but useful | 0.55 | 0.45 | Yes (gap 0.1) | ~5.5 | ~4.5 |
| Always "accept" | 1.0 | 1.0 | No (gap 0) | ~10 | ~10 |
| Biased but flat | 0.7 | 0.7 | No (gap 0) | ~7 | ~7 |

The strong oracle separates with 10 repetitions. The weak oracle needs ~100 repetitions to reliably separate (the binomial distributions overlap heavily at 10). The last two never separate regardless of repetitions.

### Scaling: how many repetitions?

The number of repetitions needed to reliably distinguish correct from incorrect outputs scales roughly as **1/(TPR - FPR)²**. This is because we're separating two binomial distributions whose means differ by (TPR - FPR), and the standard deviation of each scales as 1/√N. To get the means separated by several standard deviations, N must grow quadratically as the gap shrinks.

- Gap of 0.5 → ~4 repetitions suffice
- Gap of 0.1 → ~100 repetitions
- Gap of 0.01 → ~10,000 repetitions
- Gap of 0 → no number of repetitions helps

## Ways to construct above-chance oracles

The interesting question isn't "how strong is your oracle?" but "how cheaply can you get TPR > FPR?" — because amplification handles the rest (given decorrelation). Some mechanisms:

- **Structural checks** — does the output have required sections, valid formatting, correct length? Deterministic, cheap, but narrow. TPR ≈ 1 for well-formed correct outputs, FPR < 1 for malformed incorrect ones.
- **Self-consistency** — do multiple generations agree? MAKER's core approach. Decorrelation comes from sampling randomness, which may be limited.
- **Metamorphic checks** — does the answer stay the same under rephrasing, reordering, or irrelevant context addition? No ground truth needed. Each transformation probes a different failure mode, providing structurally decorrelated signal.
- **LLM-as-judge** — does another model (or the same model with a different prompt) rate this as good? Signal is soft but often has TPR > FPR.
- **Cross-document consistency** — does this contradict established KB content? Uses the existing knowledge base as ground truth.

## Decorrelation strategies

Since LLMs have systematic biases, naive repetition (same prompt, same model) produces highly correlated checks. The effective TPR-FPR gap after accounting for correlation is smaller than the nominal gap. Strategies for decorrelation:

- **Vary the prompt** — rephrase the question, change the framing, alter the instruction style
- **Vary the model** — different models have different failure modes
- **Metamorphic transformations** — change the *input* structurally (reorder evidence, remove context, translate and back-translate) so that correlated biases are disrupted
- **Orthogonal check dimensions** — combine structural checks (formatting) with semantic checks (consistency) with metamorphic checks (invariance); each catches a different class of errors

Metamorphic checks are particularly valuable here because they introduce decorrelation by design — each transformation probes a different axis, producing structurally independent signal from a single underlying oracle.

## Implications for the knowledge system

Structured document types are a form of error correction: they constrain the output space (structural checks) and steer the model toward [higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md). But the framework here suggests going further:

- **Validation scripts** are hard-oracle checks — cheap, deterministic, but narrow
- **Multiple generation + voting** could improve seedling quality before human review
- **Metamorphic checks on claims** — does rephrasing the evidence change the conclusion? Does removing one piece of evidence weaken it proportionally? These test argument robustness without requiring ground truth
- **Cross-note consistency** — does a new claim contradict existing notes? This uses the KB itself as an oracle

The progression from [oracle hardening](./oracle-strength-spectrum.md) to error correction is: first construct an oracle with TPR > FPR, then amplify through decorrelated repetition. Crystallisation moves components toward harder oracles, which makes error correction cheaper — but it's not a prerequisite. Even weak oracles support error correction if you can decorrelate.

---

Relevant Notes:
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — foundation: the spectrum of oracle strength this note extends with error correction as an amplification mechanism
- [MAKER paper](../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — example: voting with hard oracles achieves O(s ln s) scaling for million-step tasks; this note generalises beyond hard oracles
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — enables: structured templates are one error-correction mechanism (distribution selection constrains output); this note places them in the broader design space
- [reliability dimensions map to oracle hardening stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — extends: reliability dimensions are specific oracle-hardening moves; error correction amplifies whatever oracle strength they achieve
- [three distinct mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — parallel: crystallisation moves toward harder oracles, making error correction cheaper; but error correction doesn't require hard oracles

Topics:
- [learning-theory](./learning-theory.md)
