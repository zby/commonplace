---
description: "Preferred overview of Schmidhuber's compression-progress framework: a later, expanded treatment than Driven by Compression Progress, with an explicit implementation typology."
source: https://people.idsia.ch/~juergen/ieeecreative.pdf
captured: "2026-11-06"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6
ingested: "2026-11-06"
type: types/ingest-report.md
domains: [intrinsic-motivation, compression-progress, exploratory-learning]
learning_claims: true
---

# Ingest: Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990-2010)

## Classification

A theoretical scientific paper and retrospective review of artificial-curiosity implementations. Jürgen Schmidhuber writes as an IDSIA researcher and originator of the research program surveyed. The formal constructions, historical experiment summaries, and interpretations of human creativity have different evidential strengths; this is not a new comparative benchmark.

## Summary

Schmidhuber proposes rewarding an agent for improvements in its ability to predict or compress its action-observation history, rather than for prediction error or compressibility alone. A predictor learns regularities, a progress measure compares its performance before and after learning on the same data, and a reinforcement learner seeks actions yielding future progress. This avoids rewarding either already understood regularity or persistent unlearnable noise in the ideal formulation. The paper supplies discrete, asynchronous, and continuous formulations, discusses computation costs and theoretical optimality, and reviews approximate implementations. Reported advantages over random exploration concern those implementations' supplied predictors, interfaces, and reward estimators, not a controlled comparison of alternative decompositions. A detailed typology separates these design choices and distinguishes intrinsic reward from internal rewards justified solely by external goals. Extensions to art, humor, and science are explanatory proposals, not demonstrations of a complete account of human creativity.

## Contribution assessment (our opinion)

The work addresses an important problem: how an agent can choose informative activity when external rewards are sparse. Its clearest contribution appears to be a precise, criticizable objective that distinguishes learning progress from persistent error, together with a framework for comparing implementations without conflating objectives and optimizers. The retrospective evidence suggests workable approximations, but does not establish a generally efficient learner or isolate which component causes each reported benefit. Those limits narrow practical significance without defeating the formal distinction. The available comparisons do not establish historical priority; the breadth of the human-creativity interpretation remains less well supported than the computational framework.

## Quotes

> The above description of the agent’s motivation conceptually separates the goal (finding or creating data that can be modeled better or faster than before) from the means of achieving the goal. Let the controller’s RL mechanism figure out how to translate such rewards into action sequences that allow the given world model improvement algorithm to find and exploit previously unknown types of regularities.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section II-A

> Cl (p, h(≤ t)) denotes p’s compression performance on h(≤ t): the number of bits needed to specify both the predictor and the deviations of the sensory history from its predictions, in the sense of loss-free compression.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section II-B

> The basic principle can be formulated as follows: Learn a mapping from actions (or action sequences) to the expectation of future performance improvement of the world model. Encourage action sequences where this expectation is high.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section III-B

> The second implementation replaces the confidence network by a network H which at every time step is trained to predict the current change of the model network’s output due to the model’s learning algorithm. That is, H will learn to approximate the expected first derivative of the model’s prediction error, given the inputs. The absolute value of H’s output is taken as the intrinsic reward, thus rewarding learning progress.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section III-B

> Both variants avoid the theoretically desirable but impractical regular evaluations of the predictor on the entire history so far, as discussed in Section II-B. Instead they monitor the recent effects of learning on the learning mechanism (a neural network in this case).
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section III-B

> Here the curiosity reward is proportional to the predictor’s surprise / information gain [15], measured as the Kullback-Leibler distance [39] between the learning predictor’s subjective probability distributions on possible next events before and after new observations - the relative entropy between its prior and posterior, essentially another measure of learning progress.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section III-C

> An internal storage for temporary computational results of the programs is viewed as part of the changing environment. Each module can suggest experiments in the form of probabilistic algorithms to be executed, and make predictions about their effects, betting intrinsic reward on their outcomes. The opposing module may accept such a bet in a zero-sum game by making a contrary prediction, or reject it. In case of acceptance, the winner is determined by executing the algorithmic experiment and checking its outcome; the intrinsic reward eventually gets transferred from the surprised loser to the confirmed winner.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section III-D, opposing program modules

> Thus both modules are motivated to discover truly novel algorithmic patterns, where the dynamically changing subjective baseline for novelty is given by what the opponent already knows about the (external or internal) world’s repetitive patterns. Since the execution of any computational or physical action costs something (as it will reduce the cumulative reward per time ratio), both modules are motivated to focus on those parts of the dynamic world that currently make learning progress easy, to minimize the costs of identifying promising experiments and executing them.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section III-D

> d) Results of internal computations through sequences of internal actions as in Section III-D [79]? This will motivate a curious agent to create novel patterns not only in the space of sensory inputs but also in the space of abstract input transformations, such as earlier learnt mappings from images of cars to an internal symbol “car”. The agent will also be motivated to create purely “mental” novel patterns independent of external inputs, such as number sequences obeying previously unknown mathematical laws (corresponding to mathematical discoveries).
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section V, predictor subtype 1A(d)

> A) Is the entire history used to evaluate the predictor’s performance as in Section II [85], [92], [97], [96] (in theory the correct thing to do, but sometimes impractical)? Or only recent data, e.g., the one acquired at the present time step as in Section III-B [70], or in a limited time window of recent inputs? (If so, a performance decline on earlier parts of the history may go unnoticed.)
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section V, progress reward subtype 2A

> a) Mean squared prediction error or similar measures as in Section III-A [71], [3], [107], [36]? This may fail whenever high prediction errors do not imply expected prediction progress, e. g., in noisy environments, but also when the limitations of the predictor’s learning algorithm prevent learning progress even in deterministic worlds.
> --- `kb/sources/.snapshots/schmidhuber-formal-theory-creativity.md` @ `sha256:260f63e52578ab7c128cdd2fd7ab5b4d450d5e9aa6830a3e5173efdbdf4f73a6` — Section V, progress reward subtype 2B(a)

## Connections Found

Use this paper as the **preferred overview** of Schmidhuber's compression-progress framework. It is a later, expanded treatment of the same research program than the retained April 2009 version of [Driven by Compression Progress](./driven-by-compression-progress.ingest.md), not an independent empirical replication. Both use observer-relative compression improvement to motivate exploration. The distinct reusable contribution here is Section V's explicit separation of predictor, progress reward, and reward optimizer, plus its distinction between intrinsic reward and internal rewards serving external objectives. Retain the earlier paper for its particular exposition and existing grounded citations; this reading preference does not replace those citations.

## Learning Claims (our opinion)

The mechanism couples two adaptations: the predictor learns from interaction history, while the controller learns which actions yield future predictor improvement. Section II-E freezes a history, evaluates old and new compressors on it, and delivers the resulting reward asynchronously. Retained model changes affect later predictions and rewards; delayed credit assignment remains the controller's problem. Practical variants use local approximations rather than repeatedly evaluating the entire history.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the conditions have different support. **Localized content:** neural parameters do not establish stated theories; Section III-D's programs and explicit bets provide identifiable predictions at least at the experiment level. **Consumption:** predictive content guides the model-based controller of III-A, and competing predictions determine accepted experiments and reward in III-D; the generic framework does not require every controller to consume a stated theory. **Content-directed criticism:** III-D executes experiments that decide between opposing predictions, but the overview does not establish a retained, stated criticism that identifies which program assumption failed. Prediction-error fitting alone does not meet that condition. **Iteration:** the described adaptive models and co-evolving programs retain updates that shape subsequent rounds, although retention of criticism as such is not established. Persistence is described across a continuing run or lifetime; transfer across separately initialized runs is not demonstrated here. The universal proof-governed constructions do not by themselves settle these missing conditions.

Learning as improved capacity for future action is a separate claim. Sections III-B and III-C report advantages over random exploration, and III-E reports faster external reward acquisition in earlier studies. These support bounded implementation-level claims through the author's retrospective account, not a new reproduction. Intrinsic progress can also harm external performance.

The paper makes the [fixed-decomposition boundary](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) unusually explicit. Its typology asks what history is accessible, which actions and internal computations are available, what the predictor can represent, and how progress is measured. Finite-window statistical predictors and more general program learners admit different regularities. Better exploration within one such configuration does not establish the adequacy of its fixed interface or hypothesis class; surveying different configurations does not isolate their causal effects.

## Extractable Value

1. **Separate objective, measurement, and optimizer.** Section V supplies a concrete diagnostic for a proposed KB exploration loop: identify what model changes, what measured change earns reward, and what selects the next action. Internal scores used only to improve an external task objective are not intrinsic motivation under the paper's definition. This is a sharper implementation checklist than treating all exploratory behavior as curiosity. [quick-win]

2. **Compare models on common evidence.** Section II-E's frozen-history comparison prevents a changing observation set from masquerading as model improvement. A KB transfer experiment could compare old and revised representations on the same retained cases, while checking downstream usefulness separately. The earlier compression-progress ingest already captures this principle; this source adds explicit asynchronous scheduling and delayed-credit costs. [experiment]

3. **Make the learner's limits part of the progress claim.** Section V separates accessible histories, action repertoires, predictor classes, and reward approximations. These distinctions help specify a KB experiment's effective update space before interpreting an improvement. The reviewed comparisons against random exploration support gains within supplied configurations, not superiority of those boundaries over alternative representations. [quick-win]

## Limitations (our opinion)

The practical evidence is a retrospective summary of cited experiments, not a newly reported matched benchmark with effect sizes and enough configuration detail to isolate component contributions. Prediction-error reward, expected predictor change, prior/posterior divergence, and measured description-length improvement are not interchangeable operational measures. The paper itself describes non-universal predictors, Markovian restrictions, heuristic learning rates, and approximate progress evaluations.

Theoretical optimality is conditional on the environment class, prior, utility, or proof system and may require incomputable methods or impractical computation. It does not answer the paper's stated question of how best to spend a fixed online computation budget. Whole-history comparisons grow costly; recent-window approximations can miss deterioration on earlier data. These costs directly affect whether progress rewards remain useful in an implemented system.

The account of art, humor, and scientific motivation relies chiefly on illustrative interpretations. It does not discriminate the proposed drive from rival explanations of human behavior. Nor does improved compression alone establish truth, causal understanding, or external task value. The paper explicitly allows harmful curiosity and assumes sufficiently benign environments when advocating the bias. No KB workflow is tested, so transfer to Commonplace remains a design hypothesis rather than outcome evidence.

## Recommended Next Action

Use this later treatment as the starting overview for future compression-progress and learning-loop discussions. Retain Driven by Compression Progress for its existing grounded citations and particular exposition; no new theory note is recommended solely from this overlap.
