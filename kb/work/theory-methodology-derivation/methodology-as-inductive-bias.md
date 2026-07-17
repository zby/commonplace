# ML framing: the methodology is a learned inductive bias

Two distinct connections to inductive bias, worth keeping separate.

## The methodology *is* an inductive bias

Inductive bias is whatever lets a learner prefer some generalizations over others beyond what the data forces. Each promoted rule is a commitment that an observed regularity extends to unseen cases — the "every codification is a bet" framing of [codification and relaxing](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), and the generality-for-reliability trade is the bias side of the bias–variance dilemma.

The [no-free-lunch source](../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.md) supplies the argument for why the methodology must exist at all: no learner generalizes without bias, and the theory alone is too weakly biased (too general) to be cheap. The methodology supplies distribution-specific bias mined from actual use.

The bias here is *learned rather than fixed a priori* — promotion is the system acquiring its own inductive bias from the corner-case distribution. Structurally a meta-learning claim.

The two-layer architecture is also a way to get a strong bias without paying its cost globally: the biased fast layer handles the covered region, the weakly-biased general layer catches the rest. The bias–generality dilemma is resolved architecturally rather than by picking a point on the curve.

## Inductive bias predicts which promotions are durable

The [induction-bias source (Ebrahimi et al., 2026)](../../sources/induction-bias-sequence-models-ebrahimi-2026.md) — already used by the codification-and-relaxing note — argues architectural bias is a *permanent* advantage for calculator-class tasks, not one that scale dissolves. Mapped onto the two-layer pattern: promotions in the arithmetic regime (the rule exhausts the subproblem) never need demotion; promotions that encode a proxy theory of the corner cases are the ones that later relax. The existing [exact-spec / proxy-theory split](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) doubles as a theory of which methodology growth is monotone and which is provisional.

## Open questions

- Is the meta-learning point (system acquires its own bias) a claim or a decoration? It becomes a claim if it predicts something — e.g., that methodology quality depends on the corner-case *sampling* (what the system happened to encounter), which would argue for deliberately seeking corner cases rather than waiting for them.
- Does this framing merge into the structure note or stand alone? It stands alone only if the durability prediction (exact-spec promotions are monotone) is worth its own title-as-claim.

---

Working links:

- [codification and relaxing navigate the bitter lesson boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: its bet framing, restated as bias selection
- [fixed artifacts split into exact specs and proxy theories](../../notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — mechanism: the split that predicts promotion durability
- [Ebrahimi et al., induction bias in sequence models](../../sources/induction-bias-sequence-models-ebrahimi-2026.md) — evidence: architectural bias is permanent for calculator-class tasks
- [no free lunch theorem](../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.md) — grounds: why a distribution-specific bias layer must exist
