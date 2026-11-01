---
description: "GSM-DC benchmark: irrelevant context degrades LLM math reasoning as a depth-dependent power law in distractor count, hurting both path selection and arithmetic; hard-distractor training and PRM search help"
source: https://arxiv.org/html/2505.18761v2
captured: "2026-03-26"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea
ingested: "2026-11-01"
type: types/ingest-report.md
domains: [irrelevant-context, distractor-robustness, synthetic-math-benchmark, process-reward-model]
tags: [context-engineering]
learning_claims: true
---

# Ingest: How Is LLM Reasoning Distracted by Irrelevant Context? (GSM-DC benchmark)

## Classification

This is an empirical research paper. It builds a synthetic benchmark, runs
controlled prompting experiments on six models, runs fine-tuning ablations on
one small model, and tests an inference-time search method.
Author: Minglai Yang, Ethan Huang, Liang Zhang, Mihai Surdeanu, William Wang
and Liangming Pan. The snapshot names authors only, without affiliations.
The paper is an arXiv v2 dated 22 Sep 2025 and reads as academic NLP work.

## Summary

GSM-DC (Grade School Math with Distracting Context) represents each math word
problem as a symbolic dependency DAG with one solution path. It then injects
off-path distractor nodes, which leave the correct solution unchanged, and
renders the graph into templated sentences. A symbolic parser scores each
chain of thought for Step Accuracy (SAcc: every equation correct and well
ordered) and Path Accuracy (PAcc: every required dependency used and no
distractor used). Across six instruction models under a fixed five-shot
prompt, accuracy falls as distractor count m rises from 1 to 15. Error
roughly follows a power law in m, and the exponent grows with reasoning depth
(Grok-3-Beta: δ ≈ 0.11 at 2 steps, ≈ 0.49 at 5). The paper reads the
SAcc/PAcc gap as showing that distractors disrupt arithmetic execution as
well as path selection. All of this holds within one decomposition: a single
flat prompt in which distractors are shuffled with relevant sentences. No
arm filters, scopes or decomposes the context. Training ablations, all on
LLaMA-3.2-1B with 30K samples, find that continued pretraining beats LoRA
and that training on hard distractors beats clean, mixed or easy training,
including on out-of-distribution depths. A tree search guided by a process
reward model (PRM) keeps in-distribution accuracy and raises
out-of-distribution step accuracy by up to 6.29%.

## Contribution assessment (our opinion)

The problem matters: deployed prompts routinely carry material that the task
does not need, and the earlier GSM-IC result used a single distractor at
shallow depth. The main contribution is an instrument rather than an
explanation. Generating problems from DAGs makes distractor count and depth
independently controllable, and the stepwise parser separates path errors
from execution errors. This turns "distractors hurt" into a dose-response
measurement with a testable depth interaction. That is a real improvement in
test strength, and the depth × count interaction is the most reusable
result. The paper offers no mechanism for why the exponent grows with depth.
Its training and PRM findings are narrower: one 1B model, one training-set
size, and gains on its own synthetic distribution. They show that the
benchmark can measure interventions more than they establish general
remedies. Relative to iGSM and GSM-∞, which the paper itself names, the
novelty claim is explicit distractor control inside the DAG. I cannot judge
priority beyond that comparison. The template realization and the missing
filtering or decomposition baselines narrow how far the results transfer,
but they do not undermine the benchmark contribution.

## Quotes

> We find it roughly follows a power-law trend: E(m; rs) ∝ m^δ(rs), where δ(rs) reflects a model's IC sensitivity. Error increases with m, and the degradation steepens with deeper reasoning.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 4.1, Finding II.

> The model trained on Clean data consistently shows a higher Δ, suggesting that IC affects not only reasoning path selection, but also arithmetic execution.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 4.3, Finding IV.

> Each node is mapped to an entity (e.g., "Arts Campus's T&T Supermarket") from the hierarchical entity vocabulary of the GSM8K dataset, and each edge is rendered using a templated relational statement (e.g., "the number of Zion Markets is 1 more than the number of T&T Supermarkets"). These templates capture the underlying dependencies while maintaining simple, readable language.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 3.3, “Natural Language Realization”

> To systematically analyze how irrelevant context (IC) affects LLM reasoning, we conduct controlled experiments by injecting varying numbers of irrelevant context (m = 1–15) into math word problems M drawn from *GSM-DC*. We evaluate performance across four levels of reasoning steps, denoted rs ∈ {2, 3, 4, 5}, and sample 100 instances per condition to ensure statistical stability.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 4.1, “Impact of Irrelevant Context”

> We benchmark six instruct models: Grok-3-Beta, GPT-4.1, GPT-4o-mini, LLaMA-3.3-70B, LLaMA-3.1-8B and LLaMA-3.2-1B.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 4.1, “Impact of Irrelevant Context”

> Step Accuracy (SAcc): Our symbolic parser reads the model's chain-of-thought and executes every intermediate equation in topological order. SAcc = 1 iff *all* equations are arithmetically correct *and* each step references only symbols that have already been defined.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 3.4, “Stepwise Solution Evaluator”

> Path Accuracy (PAcc): To quantify *distraction robustness* we check whether the model confines its reasoning to the augmented dependency graph G' after injecting irrelevant context. PAcc = 1 iff (i) every required dependency on P is present, and (ii) no irrelevant node is used in the computation of any step on P.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 3.4, “Stepwise Solution Evaluator”

> A lower ratio indicates a larger gap — arithmetic errors occurring even when the reasoning path is correct.
> --- `kb/sources/.snapshots/gsm-dc-llm-reasoning-distracted-irrelevant-context.md` @ `sha256:4ca8f78f9c59c7ae2b4d95be21b2e9d42c7ae1458b4947452f60940ba07f3dea` — Section 4.3, Finding IV

## Connections Found

This source is the KB's controlled anchor for interference from semantically
inert irrelevant context. Two notes already depend on it.
[Soft degradation can bind before the hard cap](../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md)
cites it as evidence for its interference claim. GSM-DC is evidence for that
note's point that irrelevant tokens can cost more than their volume. The
evidence is bounded to templated math problems, m ≤ 15, depths 2 to 5 and a
single flat prompt. The note's open question, how stable the depth × count
interaction is outside this benchmark, is one the paper cannot answer.
[Process structure and output structure are independent levers](../theory/process-structure-and-output-structure-are-independent-levers.md)
uses the PAcc/SAcc split as a bound rather than a test. The two metrics
separate path selection from execution inside one shared trace format.
Neither varies a process instruction against an output constraint.

GSM-DC is evidence for the architectural premise of
[LLM context is composed without scoping](../theory/llm-context-is-composed-without-scoping.md).
In a flat context nothing excludes off-path sentences, and they still steer
the computation. It is the inert-noise end of the comparison that note draws
with [semantic leakage](./semantic-leakage-lms-gonen.ingest.md) and
[content effects on reasoning](./language-models-like-humans-show-content-effects-on-reasoning.ingest.md).
The shared axis is what kind of unlicensed content each study varies: GSM-DC
varies count, Gonen varies associative concepts, and Lampinen varies belief
congruence inside the premises. The training responses differ. Hard
distractor training helps here, whereas instruction tuning increases leakage
in Gonen and leaves content effects unchanged in Lampinen. That divergence is
evidence against assuming one mechanism across the three paradigms. It does
not establish that the mechanisms differ.
[Context contamination operates below compliance reasoning](../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md)
compares with it on the same axis, at the agent-stance end.

Three sibling sources separate variables that GSM-DC holds together or
leaves out. [ConvexBench](./convexbench-can-llms-recognize-convex-functions.ingest.md)
compares with it on depth versus volume. ConvexBench keeps token count small
while depth varies, and it supplies a focused-context arm, which is the
scoping baseline that GSM-DC lacks.
[Paulsen's maximum effective context window](./paulsen-maximum-effective-context-window-mecw.ingest.md)
compares with it on volume versus interference. Paulsen varies span length;
GSM-DC bounds total graph size and varies only off-path nodes.
[The web-agents long-context benchmark](./llm-webagents-long-context-reasoning-benchmark.ingest.md)
compares with it on dose. That benchmark injects irrelevant prior tasks into
agent histories of 25k to 150k tokens, but varies length and content
together. For the execution errors on correct paths,
[the J-space workspace paper](./verbalizable-representations-global-workspace-llms.ingest.md)
offers one candidate mechanism, workspace displacement. That paper reports
that chain of thought makes GSM8K more robust to ablation. GSM-DC enforces
chain of thought and still degrades, which bounds that relief claim.

## Learning Claims (our opinion)

On its own terms, the paper's learning mechanism is supervised fine-tuning
of LLaMA-3.2-1B on GSM-DC problems. The variables are adaptation method
(continued pretraining vs LoRA) and distractor exposure (clean, IC-only,
clean+IC, and easy, mixed or hard IC). The inference-time mechanism is a
PRM. It is trained on reasoning paths into which distractors and arithmetic
errors were injected, and it scores partial paths to guide a tree search.

Mapped onto Commonplace: the fine-tuning results are weight-level adaptation
inside a fixed decomposition, as in
[learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
The task representation (one flat prompt with distractors shuffled in), the
action basis (free-text chain of thought), and the template vocabulary stay
outside the update space. The learner can only become better at ignoring
distractors that it still reads. The result supports "hard exposure improves
robustness within this decomposition." It provides no comparison with
changing the decomposition, for example by filtering, scoping or splitting
context before the call. It therefore says nothing about whether training is
preferable to exclusion. The claim that "difficulty rather than variety"
drives the gain is attributable only to the mixes tested at one model scale
and one data size.

Against the [theory builder](../theory/definitions/theory-builder.md)
conditions: the fine-tuned model fails localized content, since what it
learns resides in weights, with no stated units to point at. Consumption,
criticism and iteration therefore do not apply in the defined sense. The PRM
search comes closer within one run. Partial reasoning steps are stated text.
The PRM criticizes them, which is weak, learned and not itself open to
criticism. Low-scoring branches are pruned, and the retained frontier shapes
the next expansion. That meets the content-directed criticism and iteration
conditions only within an episode, and the results do not persist across
problems. Whether the PRM scores discriminate distractor use specifically,
rather than general step quality, is not reported. The learning claim that
is actually supported is improved future capacity of the fine-tuned 1B model
on GSM-DC-like distributions, including deeper out-of-distribution problems.
That is an observed improvement, not a demonstrated mechanism.

## Extractable Value

1. **Depth × distractor interaction as a quantitative bound.** Error grows
   roughly as m^δ, and δ rises with reasoning depth while model capacity sets
   the intercept. This sharpens the soft-degradation argument: the cost of
   irrelevant material is not fixed per token; it compounds with how many
   dependent steps the task needs. This holds for a single flat prompt with
   shuffled templated distractors. Transfer to natural prose, partially
   relevant material or agent histories is untested. The reach is moderately
   high as a design heuristic (scope harder for deeper tasks) and low as a
   numeric rate. [quick-win]
2. **Distractors reach execution, not only selection.** SAcc can fail where
   PAcc succeeds, and the paper reports this gap as larger for clean-trained
   models. If it holds, filtering that only keeps the model on the right path
   does not by itself protect arithmetic. The evidence sits in the
   ambiguously stated Δ passage (see Limitations), and the shared five-shot
   chain-of-thought format is fixed. Treat this as a conjecture to check
   against Figure 6 before reuse. [experiment]
3. **The benchmark design pattern: generate from a graph, inject off-path
   nodes, score with a symbolic parser.** This is a reusable way to build a
   controlled interference test in which the correct answer is invariant to
   the manipulation. A Commonplace-scale analogue could inject off-topic KB
   notes into a fixed retrieval context and check whether a derivation cites
   them. [experiment]
4. **Training on hard distractors helps, within the fixed prompt
   decomposition.** This is evidence that interference is partly learnable
   away in weights, and a datum for the cross-paradigm divergence (Gonen,
   Lampinen). It does not compare training with exclusion, so it is not
   evidence for choosing training over scoping. [just-a-reference]
5. **PRM search as an inference-time filter.** A step-level critic trained
   on corrupted paths gives a modest out-of-distribution gain. It is a datum
   for verifier-in-the-loop designs, but its discrimination against
   distractors is not isolated. [just-a-reference]

## Limitations (our opinion)

- **No scoping or decomposition baseline.** Every arm keeps distractors in
  the same flat prompt. The paper cannot say whether pre-filtering,
  retrieval narrowing or step decomposition would beat Hard-IC training, so
  its "most effective intervention" claims rank only within-decomposition
  remedies. ConvexBench's focused-context arm is the nearest comparison in
  the KB.
- **Inert, templated distractors.** Distractors are off-path DAG nodes
  rendered from the same templates and entity vocabulary as relevant
  sentences. This tests count, not semantic proximity or partial relevance.
  The paper itself concedes limited linguistic expressiveness. A simpler
  account is that the model is pattern-matching template surface forms, and
  it is not ruled out.
- **The Δ passage is internally inconsistent as stated.** The paper defines
  Δ as an SAcc/PAcc ratio and says a lower ratio means a larger gap. It then
  says clean-trained models show a higher Δ, yet concludes that they suffer
  more execution damage. The ingest cannot resolve which reading Figure 6
  supports, because the snapshot does not include the figure. The
  "IC affects arithmetic execution" finding should be used only after
  checking it against the published figure.
- **Training evidence is one small model.** All fine-tuning is on
  LLaMA-3.2-1B with 30K samples. The continued-pretraining vs LoRA and
  hard-vs-mixed conclusions may not hold at scale.
- **Power-law fit reported loosely.** "Roughly follows a power-law" is
  stated without fit quality, intervals or comparison with rival functional
  forms over a narrow range (m = 1 to 15, 100 instances per condition). The
  exponents are descriptive, not predictive.
- **Prompt confound.** The five-shot prompt adds a structured Background
  section that encodes the relevant dependencies. Robustness under ordinary
  prompting may differ, and EAcc stays high partly because of the enforced
  format.
- **Capture boundary.** The snapshot omits figures and tables (Figure 4 to
  6, Table 1), so this ingest relies on the paper's text for every numeric
  result except those quoted in the prose.

## Recommended Next Action

Check the Δ(SAcc, PAcc) direction against Figure 6 of the
[arXiv paper](https://arxiv.org/html/2505.18761v2). Then update the GSM-DC
sentence in
[soft degradation can bind before the hard cap](../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md),
which currently says the disruption "affected both correct path selection
and arithmetic execution", to either keep or qualify the arithmetic-execution
clause.
