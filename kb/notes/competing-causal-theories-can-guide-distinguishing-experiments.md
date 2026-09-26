---
description: "Why observationally equivalent mechanisms can tell a theory builder what to test next: a noisy binary example separates evidence acquisition from choosing or verifying an explanation."
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [learning-theory, self-improving-systems, theory-builder]
---

# Competing causal theories can guide distinguishing experiments

Two causal theories can agree on every passive observation yet predict different outcomes under an intervention. When that intervention is feasible, retaining both [tentative theories](./definitions/tentative-theory.md)—theories held open to criticism and revision—can guide evidence collection before the available evidence favors either. Their disagreement specifies what to test next.

Structural causal models make this distinction explicit: an intervention replaces a selected variable's assignment while preserving the other mechanisms and the distribution of background causes. This is established causal-inference semantics ([Bareinboim et al., §1.2 (snapshot required)](../sources/on-pearls-hierarchy-foundations-causal-inference.ingest.md)), applied here to the value of retaining unresolved explanations.

## A constructed example

This illustration comes from the motivating discussion, not from the cited papers. Let $U$ be an unobserved fair random bit and let $E$, independently, equal 1 with probability $0.1$. Write exclusive-or as $\oplus$. Consider:

$$
\begin{aligned}
A:\quad &X:=U,\qquad Y:=X\oplus E;\\
B:\quad &X:=U,\qquad Y:=U\oplus E.
\end{aligned}
$$

Under passive observation, both reduce to $Y=U\oplus E$. They therefore give exactly the same joint distribution: $P(0,0)=P(1,1)=0.45$ and $P(0,1)=P(1,0)=0.05$, where each pair denotes $(X,Y)$. In particular, both give $P(Y=1\mid X=1)=0.9$.

Replacing $X:=U$ with $X:=1$ leaves different mechanisms for $Y$:

$$
P_A(Y=1\mid do(X=1))=0.9,\qquad
P_B(Y=1\mid do(X=1))=0.5.
$$

A randomized experiment instead replaces $X:=U$ with $X:=R$, where $R$ is a fresh fair bit independent of $U,E$, retaining each candidate's $Y$-mechanism:

| Assignment | A predicts $P(Y=1)$ | B predicts $P(Y=1)$ |
|---|---:|---:|
| $R=1$ | $0.9$ | $0.5$ |
| $R=0$ | $0.1$ | $0.5$ |

Randomization concerns assignment being independent of background causes. Outcomes still follow the respective $Y$-mechanisms; their differences need not be purely random. **The theories specify an experiment with different predicted outcome distributions despite identical predictions under passive observation.**

The limitation concerns evidence and assumptions, not output format. A probability vector or structured answer can preserve both possibilities; it cannot identify the actual mechanism from evidence identical under both. Neural models can represent causal mechanisms, while greater expressiveness alone does not resolve non-identifiability ([Xia et al., §2, Theorem 1 and Corollary 1 (snapshot required)](../sources/causal-neural-connection.ingest.md)).

## Testing without final verification

[Popper's critical method](../sources/popper-conjectures-and-refutations.ingest.md) seeks demanding attempted refutations; surviving them can supply corroboration while the theory remains tentative. Randomized trials are one testing method, not the definition of corroboration. Here, under independent repetitions, both models assign positive probability to every finite binary outcome sequence in either group. A finite trial therefore supplies statistical discrimination under a stated testing rule, not deductive refutation or final verification.

## Commonplace's design consequence

For Commonplace's [theory builder](./definitions/theory-builder.md), which consumes and criticizes stated theories and uses the results in later work, our design consequence is that retained theories should help determine what evidence to seek next. When competing explanations matter to a decision, their disagreements should guide a feasible discriminating test. Retaining the predictions, intervention assumptions, testing rule, and results gives later criticism a basis for revising the explanations or the test. This applies established causal inference and critical testing to KB operation. Whether retention improves performance relative to reconstructing theories remains part of [Commonplace's research program](./commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md).

Schmidhuber's [Driven by Compression Progress](../sources/driven-by-compression-progress.ingest.md) supplies a neighboring account of choosing future observations. For curiosity-driven exploration, its controller seeks experiences expected to improve compression; progress compares old and new compressors on the same history. Our comparison is that both approaches let the learner's current state guide evidence acquisition. Their selection criteria differ: here, experiments target disagreement between causal theories; there, exploration targets expected compression improvement. Better compression of the shared observational distribution still cannot distinguish A from B.

## Scope

The experimental inference assumes that the procedure implements the intended intervention without changing the other mechanisms or background distribution. A different manipulation tests a different claim, since [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md). Both candidate explanations may also be wrong.

Some rivals agree under every feasible experiment. Additional justified causal assumptions can also identify particular effects from observational data without a new experiment or a unique complete mechanism ([Bareinboim et al., §1.4, Definition 17 (snapshot required)](../sources/on-pearls-hierarchy-foundations-causal-inference.ingest.md)). The claim is that retained causal disagreement **can** guide distinguishing experiments, not that experiments always resolve it.
