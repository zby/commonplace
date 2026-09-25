---
description: "Schmidhuber's RSI retrospective distinguishes reward-based retention, proof-authorized rewrites, and learned update rules, without establishing sustained compounding or a preferred KB design."
type: ingest-report
source: https://people.idsia.ch/~juergen/recursive-self-improvement.html
captured: "2026-09-20"
ingested: "2026-09-20"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: 76c844c4d886e206c5369b2ef9c957706407955adeb0f719ef85201d7b9c07c1
domains: [recursive-self-improvement, meta-learning, learning-theory]
learning_claims: true
---

# Ingest: Recursive Self-Improvement Since 1987

## Classification

A historical and conceptual retrospective by Jürgen Schmidhuber, published as Technical Note IDSIA-9-26 on 17 September 2026. The author participated in the research described and supplies extensive references. This makes the source useful for his account of mechanisms and intellectual lineage; it does not independently establish his priority claims or reproduce the cited experiments.

## Summary

Schmidhuber traces recursive self-improvement from 1987 program evolution through lifelong self-modifying policies, neural networks that learn weight-update procedures, incremental program search, proof-authorized software rewrites, and curiosity-driven experiment generation. He distinguishes changing a learner's own learning procedure from ordinary transfer learning or hyperparameter adjustment. The most useful distinction for Commonplace is between modifications retained on reward evidence and modifications admitted by a proof of utility under an encoded formalization. The article also treats fixed-weight in-context adaptation as meta-learning and argues that full recursive self-improvement ultimately requires physical hardware production. It summarizes experimental successes within particular neural and program-search designs, but supplies neither detailed comparative results nor evidence that those fixed designs are preferable to alternatives. Its contribution is a historical map of mechanisms, not a demonstration of sustained compounding in an agent-operated KB.

## Quotes

- **Source extract (verbatim):** *True RSI* is about encoding the initial learning algorithm in a universal programming language
  - **Source location:** Introduction, paragraph immediately before Section 1, opening clause; the sentence continues with a neural-network example and code-modification requirements.

- **Source extract (verbatim):** recurrent neural network or RNN
  - **Source location:** Same sentence, parenthetical example immediately after “universal programming language”.

## Connections Found

Section 5 corroborates the distinction in [Gödel machines are a proof-governed case of reflective self-modification](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md): statistical evidence of reward acceleration and a proof licensing a rewrite are different grounds for retaining changes. The existing note already treats these mechanisms and distinguishes them from modern empirical agent evolution. This retrospective adds historical context rather than replacing the original construction as formal evidence.

The source also supplies a useful comparison with [Improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md). OOPS reuses prior solutions while searching for later ones, and self-modifying policies can change their future update procedures. Both describe pathways by which earlier work could make later improvement more productive. Neither the recursive structure nor this article's brief experimental summaries establish the counterfactual productivity effect required by the KB's compounding claim.

## Learning Claims (our opinion)

The mechanisms change different objects and use different signals. A self-modifying policy changes a probability distribution over executable programs, including programs that modify that distribution; its learning history is a single non-resettable life, and reward per time evaluates retained changes. OOPS searches programs that may reuse previous solutions and alter search procedures. A Gödel machine searches proofs comparing a rewrite with continued search, using axioms about its utility, hardware, and initial software. Neural meta-learning instead trains initial parameters whose subsequent dynamics implement adaptation, sometimes by addressing and changing the network's own weights. These should not be collapsed into one generic feedback loop.

In Commonplace terms, software that represents and modifies its own learning procedure offers a route to reflective self-modification. It does not by itself establish a [theory builder](../notes/definitions/theory-builder.md), which needs stated theories that guide action, a working process of criticism aimed at what they say, and retention for later problems. Reward-selected program changes are localized and retained, but keeping whatever raises reward per time is trial and error unless a stated reason bears on what a program says; the retrospective shows no such reason, so condition 3 decides. Neural fitting and fast-weight adaptation also fail condition 1, since no unit of the adapted state says anything by itself. The Gödel construction does expose a formal self-representation, but proving a beneficial switch under current premises differs from criticizing those premises because empirical cases challenge them; the definition leaves the [Gödel machine](../notes/definitions/theory-builder.md#boundary-cases) open for that reason. Whether any of these mechanisms improves capacity for future action is a separate learning claim.

The neural examples also qualify a weight-centered account of learning. Fixed trained weights can implement an adaptive algorithm whose activations or fast weights change with experience. Thus unchanged pretrained parameters do not establish unchanged behavior-determining state. Conversely, episode-local adaptation does not establish retention across episodes, and the retrospective does not specify a persistent KB consumption path for in-context changes.

The article's broad rewrite spaces bear on [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): exposing update procedures to modification moves some choices inside the learner's effective update space. Universal program expressibility still does not supply missing observations, affordable search, or an adequate objective. Neural examples retain supplied architectures, interfaces, and training objectives; the article gives no controlled comparison isolating those choices. Its account supports analyzing the actual revision boundary, without establishing that recursion eliminates consequential fixed assumptions.

## Extractable Value

1. **Historical reference for distinct grounds for change.** The contrast between reward-based retention and proof-authorized rewrites gives an accessible author account of a distinction already retained in the Gödel-machine note. Its value is corroboration and routing to earlier work, rather than a new general theory. [just-a-reference]
2. **Adaptation need not change pretrained weights.** The fast-weight and activation-based examples help separate the learned update procedure from the state it updates. Their usefulness is conceptual; the reported successes remain within supplied neural architectures and do not establish which state representation an agent-operated KB should adopt. [just-a-reference]
3. **A bounded route to studying recursive productivity.** OOPS and lifelong policy modification identify concrete candidate pathways from earlier solutions to later search improvements. Investigating those pathways would require the original studies and suitable comparisons; the retrospective alone does not establish compounding. [deep-dive]

## Limitations (our opinion)

The article is an interested participant's retrospective. Claims of first invention, equivalence to later architectures, and historical compute-price ratios are not independently checked here. Its bibliography is a route to evidence, not a substitute for inspecting it.

The cited experiments are reported at summary level. For example, the self-referential weight-matrix work is described as competitive on few-shot learning and multitask reinforcement learning, but this article does not supply the baselines, effect sizes, or ablations needed to attribute results to recursion. Likewise, claims of successful reward acceleration and useful OOPS reuse do not specify enough controls here to establish sustained improvement of the improvement process.

The Gödel-machine optimality claim is conditional on the encoded utility, assumptions, and availability of the required proof. It does not promise practical discovery of useful rewrites within finite budgets. The existing Gödel-machine note states these boundaries more fully. The article's grouping of modern Gödel-inspired agents also does not establish that they inherit the classical proof requirement.

The claim that full RSI requires self-improving hardware extends the system boundary to autonomous physical production. The article sketches that prospect but does not demonstrate it or establish its necessity for useful software self-improvement. It supplies no direct evidence about Commonplace's theory-building process or its outcome quality.

## Recommended Next Action

File this ingest as a source-only historical reference alongside the existing Gödel-machine note, without promoting a new theory note.
