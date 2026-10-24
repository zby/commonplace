---
type: types/note.md
description: "Distinguish a stricter acceptance policy from another correctness check when conjunctive lower-bound gates use fixed nondecreasing transforms of the same probability."
traits: [title-as-claim, has-external-sources]
---

# Thresholding fixed monotone transforms of one probability does not add an independent check

Two lower-bound gates on fixed nondecreasing transforms of the same probability implement one effective scalar cutoff when acceptance requires both gates to pass. The second gate can make acceptance stricter. It does not supply another correctness observation conditional on knowing that probability.

## Deterministic reuse and the cutoff consequence

Let `p` be a reported probability in `[0,1]`. If another reported statistic is exactly `c=f(p)` under a fixed configuration, knowing `p` suffices to compute `c`. Any policy `A(p,c)` can be rewritten as `A(p,f(p))`. This lack of additional input requires no monotonicity. Here an *independent check* means an additional evidential input relative to `p`, not a claim about formal statistical independence.

A narrower result follows for fixed nondecreasing functions `f` and `g` and acceptance exactly when:

```text
f(p) >= a AND g(p) >= b
```

Each gate's accepted set is upward closed: if it accepts one value of `p`, it accepts every larger value. Their intersection is also upward closed. The pair therefore implements one upper-tail cutoff policy on `p`. It may accept all values or none; otherwise its boundary may be open or closed. Threshold numbers expressed in different units cannot simply be compared.

**Hypothetical example, not a producer formula:** suppose `c=p²`. On `[0,1]`, the policy `p>=0.80 AND c>=0.81` is exactly `p>=0.90`. A case with `p=0.85` passes the first gate but fails the second because `c=0.7225`. The second gate changes the decision, but its verdict is fully calculable from `p`. These illustrative thresholds imply no error frequency and are not proposed operating values.

## Producer descriptions do not establish the premises

[TypeSafe's retained confidence documentation](../sources/typesafe-confidence-20261024.ingest.md) describes confidence as a statistic computed from the answer's probability distribution. That does not establish dependence on the picked-answer probability alone, much less a monotone mapping from it. The retained [basal-2.0-max card](../sources/basal-2-0-max-20261024.ingest.md) describes confidence as the probability of the answer it picks. This is a producer card statement, not a code audit or a guarantee about the current service; the statement alone also does not establish that selection always takes the maximum.

A picked component is a distribution statistic, so the descriptions are compatible without identifying the same statistic. Neither retained source documents the hypothetical paired gates above. They bound possible applications of the argument; they are not tests of it.

## One KB application

Consider advisory tag suggestions. If two acceptance gates demonstrably satisfy the scalar assumptions above, expressing their effective cutoff makes the actual policy legible. Tightening it can send more suggestions to review, but should not be described as two agreeing assessments of tag fit. Whether the stricter policy is useful depends on task-specific evaluation and the consequences of errors. [TypeSafe's threshold guidance](../sources/typesafe-confidence-20261024.ingest.md) likewise calls for thresholds suited to the action and evaluation on local data; it supplies no validated KB threshold.

A schema or allowed-tag check instead enforces specified structural or membership constraints. An authorization check enforces a separately specified permission rule. Sharing a workflow does not make these checks transforms of semantic confidence, and neither check proves that a tag fits the document. For a proposed second correctness check, specify what input or constraint it adds beyond `p`, then evaluate which relevant failures it catches. Separateness alone proves neither independent errors nor better decisions.

## Scope

- **Distribution dependence is not scalar dependence.** In the hypothetical distributions `(0.60,0.40,0.00)` and `(0.60,0.20,0.20)`, with the first option picked in both, the picked and winning probabilities are both `0.60`. Yet the top-two margins are `0.20` and `0.40`. A distribution summary can therefore distinguish cases that `p` cannot. It adds information relative to `p`, not relative to the already-known full vector. This does not identify TypeSafe's formula or show that margin predicts errors better.
- **The cutoff result needs its directions and composition.** It assumes nondecreasing transforms, lower-bound comparisons, and conjunction. Decreasing or nonmonotone deterministic transforms still reuse `p`, but their gates need not produce an upper-tail policy.
- **Ranking needs a fixed mapping.** A strictly increasing transform preserves order and ties exactly; a nondecreasing one can merge values into ties but cannot reverse order. Changed calibration, temperature, task-specific mapping, or scale requires reestablishing the relevant relationship. A fixed calibrated transform can still reuse the same input; this does not argue against calibration's usefulness.
- **Actual vendor applicability remains unestablished.** The retained material supplies no exact TypeSafe/Jev formula, Jev version, or Jev–TypeSafe naming relationship. It does not establish an actual redundant vendor gate pair or cross-product equality. A whole-distribution summary or separate predictor is not ruled out by the scalar result.
- **Stricter acceptance is not demonstrated error reduction.** The argument supplies no local KB performance, universal risk threshold, model choice, or deployment recommendation. Whether excluding cases improves accepted-case error requires evaluation on the relevant task.

---

Relevant Notes:

- [Generation confidence does not by itself certify soundness](./generation-confidence-does-not-by-itself-certify-soundness.md) — the broader distinction between confidence and correctness; this note instead derives a dependency condition for multiple gates.
