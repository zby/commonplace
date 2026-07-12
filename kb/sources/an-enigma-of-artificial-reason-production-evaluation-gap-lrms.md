---
source: https://arxiv.org/abs/2606.01462
description: "Paper introducing VAIR, a benchmark showing large reasoning models can produce correct answers while failing to evaluate invalid reasoning that reaches those answers"
captured: 2026-06-17
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# An Enigma of Artificial Reason

Author: Mingzhong Sun, Teresa Yeo, Armando Solar-Lezama, Tan Zhi-Xuan
Source: https://arxiv.org/abs/2606.01462
Date: 31 May 2026

   License: arXiv.org perpetual non-exclusive license
   arXiv:2606.01462v1 [cs.AI] 31 May 2026

An Enigma of Artificial Reason:
Investigating the Production-Evaluation Gap in
Large Reasoning Models

   Mingzhong Sun^1,4  Teresa Yeo^4  Armando Solar-Lezama^2,4  Tan Zhi-Xuan^1,3
   ^1NUS Department of Computer Science  ^2MIT EECS  ^3A*STAR
   ^4Singapore-MIT Alliance for Research and Technology (SMART)

Abstract

   Studies of human reasoning have shown that people are typically stronger at evaluating reasoning than producing
   it from scratch. In contrast, large reasoning models (LRMs) are trained to excel at producing long chains of
   reasoning to solve complex problems. How then do LRMs perform at evaluating reasons? We investigate this with
   the Valid-Answer-Invalid-Reasoning (VAIR) dataset: math problems and solutions with trivial reasoning flaws but
   valid answers, designed to isolate reasoning evaluation from the confound of reasoning production. Unlike
   humans, who we find are only 6% worse at grading than solving such problems, we find a substantial
   production-evaluation gap in LRMs: frontier models score as low as 48% when evaluating VAIR solutions, despite
   near-perfect solution production.

   Why this enigma? Through chain-of-thought (CoT) analysis, we find evidence of an answer confirmation bias: LRMs
   often produce then check for the correct answer instead of carefully verifying each step, fabricating
   rationalizations even when noticing anomalous reasoning. Linear probes corroborate this, showing that while LRM
   activations encode some representation of valid reasoning, they fail to robustly represent VAIR solutions as
   invalid. Causal patching of the final answer’s representations causes LRM verdicts and activations to flip,
   demonstrating that answer validity is responsible for models’ confirmation biases. These findings indicate an
   outstanding limitation in dominant approaches to reasoning training, which incentivize LRMs to produce and
   confirm reasoning towards correct answers, but not to robustly evaluate the underlying reasons.

1 Introduction

   Recent advances in AI have led to development of large reasoning models (LRMs): large language models (LLMs)
   that are trained to “reason” artificially by generating long chains of tokens before committing to a final
   answer [36, 13, 15]. LRMs have demonstrated impressive outcomes in domains such as software engineering [19,
   55], research mathematics [14, 1], and abstract visual reasoning [7, 6]. Yet, numerous studies have also shown
   that these capabilities are “jagged” in nature [9, 34], failing to generalize reliably both beyond [20, 27, 56]
   and within their core domains of mathematics and coding [58, 33, 17, 38] .

   In this paper, we investigate a particularly striking way in which LRM reasoning is jagged: Even though LRMs
   are highly capable at producing reasoning, they can fail drastically at evaluating reasoning, exhibiting a
   production-evaluation gap. We demonstrate this gap through the Valid-Answer-Invalid-Reasoning (VAIR) dataset, a
   suite of math problems and solutions that we perturb to introduce trivial reasoning flaws, while preserving the
   original valid answer.

   The design of VAIR isolates reasoning validation from the proxy of answer validity, preventing LRMs from
   evaluating a solution by just producing the answer and confirming its presence. Remarkably, even frontier LRMs
   such as GPT 5.4 or Claude Opus 4.7 struggle to evaluate these invalid solutions, incorrectly scoring them as
   flawless up to 50% of the time. This is despite accuracies of 90% or more when LRMs solve problems directly, or
   when they evaluate solutions where answer correctness matches reason validity. In contrast, we find that human
   reasoners are only 6% worse at evaluating VAIR solutions (75% accuracy) than producing correct solutions (81%
   accuracy).

   What explains this enigma in artificial reasoning? One possibility is that LRMs are biased by the presence of
   valid answers they can easily reach via reasoning production: an answer confirmation bias. We investigate this
   hypothesis through a combination of interpretability methods. CoT analysis reveals that LRMs routinely overlook
   reasoning flaws or fabricate justifications for their validity, often after first re-producing the correct
   answer. Linear probes [2, 28] corroborate this: while LRM activations encode some representation of valid
   reasoning, they fail to robustly represent VAIR solutions as invalid. Causal patching [48, 12, 30, 49] of the
   final answer’s representations causes LRM verdicts and activations to flip, demonstrating that answer validity
   is responsible for this bias.

   Related Work. LLM reasoning training primarily relies on outcome-based RL [15, 53], which incentivizes correct
   answers but not the generation of valid steps [21, 4] or the validation of reasoning. Process reward models
   [22, 62], meta-reasoning benchmarks [59, 57, 60, 47, 65, 63], and LLM-as-judge evaluations [5] have been used
   to assess step-level reasoning, finding positional, verbosity, and self-preference biases [52, 43, 64, 51].
   Work on generation-verification gaps typically assumes that final answer verification is easier than generation
   [39, 41], though some studies find the opposite [54, 35]. Inspired by the cognitive science of reasoning, which
   has found that humans are typically stronger at evaluating reasoning than producing it [31, 29, 45], we focus
   on the gap between reasoning production and reasoning evaluation, not just the verification of final answers.
   Through this lens, we find that LRMs often evaluate reasoning by producing answers. This is consistent with
   LRMs’ outcome-focused training, unlike the social incentives for epistemic vigilance in humans [32, 40].

2 Evaluating the Evaluation of Reasoning

   How can we evaluate LRMs specifically for reasoning evaluation, and not reasoning production? One difficulty is
   that these capacities can support each other: evaluation can be used to excise bad reasoning steps during
   production, while production can be used to check whether the reasons or conclusions being evaluated are
   similar to what one would produce. Since LRMs are trained extensively for reasoning production, this latter
   confound is especially important to mitigate.

   In order to control for this potential confound, we construct the Valid-Answer-Invalid-Reasoning (VAIR)
   dataset: A set of math question-solution pairs with invalid reasoning steps — steps that do not follow from
   either the previous steps or the question premises — but valid answers. By testing LRMs on how they evaluate
   VAIR solutions, we prevent the use of answer correctness or validity as a correlate for reasoning quality: If
   LRMs simply solve the problem directly and check that the answer matches, they will fail to detect invalid
   reasoning.
   Refer to caption Figure 1: Overview of our dataset and methodology. We evaluate both large reasoning models
   (LRMs) and humans on (a) reasoning production as math problem solving (b) reasoning evaluation as math solution
   grading. We construct the Valid-Answer-Invalid-Reasoning (VAIR) dataset to isolate the reasoning validation
   task from the confound of answer validity, creating math solutions with trivial reasoning flaws (Missing
   Premises, …, Circular Reasoning) but valid answers. Valid-Answer-Valid-Reasoning (VAVR) and
   Invalid-Answer-Invalid-Reasoning (IAIR) solutions serve as controls. Unlike humans, LRMs exhibit a sharp drop
   in accuracy (up to 49%) for VAIR evaluation vs. solving problems, demonstrating a large production-evaluation
   gap (top-right).

2.1 Dataset Construction

   To construct the VAIR dataset, we adapt the practice of data perturbation often used in machine learning [42,
   18]. Given a “seed” math problem paired with a gold-standard solution (with valid reasoning and a correct
   answer), we inject four distinct categories of reasoning flaws by perturbing either the reasoning steps or the
   problem statement (Figure 1(b), right):
     * •
       Missing Premises: A premise from the original question is omitted, rendering the problem unsolvable with
       the given information. The original reasoning becomes invalid due to the presence of fabricated premises,
       though the answer still validly follows from the reasoning steps.
     * •
       Missing Reasoning: An essential inferential step is removed from the solution, creating a gap that renders
       the reasoning chain incomplete.
     * •
       Shuffled Reasoning: The order of the solution steps is randomly shuffled, destroying the logical
       dependencies between each step in the reasoning chain.
     * •
       Circular Reasoning: We utilize an LLM (Gemini 3 Flash) to generate reasoning chains that arrive at the
       correct answer through tautological, logically empty, or purely assertive arguments.

   Our seed problems and gold solutions are primarily sourced from the widely adopted GSM8K [8] and MATH [16]
   benchmarks. We supplement these with more recent problem instances from Process-Bench [62] to mitigate the risk
   of data contamination (e.g. answer memorization). Following the perturbation process, all modified
   question-solution pairs underwent rigorous manual verification by the authors. More dataset construction
   details can be found in Appendix A.1.

2.2 Comparing Reasoning Evaluation and Production

   With the VAIR dataset in hand, we conduct a systematic assessment of how both LRMs and humans fare at reasoning
   evaluation vs. production. Production simply requires participants to solve an (unperturbed) problem from the
   dataset. Evaluation is operationalized as a grading task: given a problem and a solution, participants are
   asked to assign a grade between 3 (entirely correct with no reasoning flaws) and 0 (completely incorrect) to
   the solution, with six grading examples provided for calibration. Full instructions and prompts can be found in
   Appendix A.2.

   In order to isolate the effect of reasoning validity from answer validity on the evaluation task, we also
   construct two control datasets where (in)valid reasoning is matched with (in)valid answers, resulting in two
   more evaluation sub-tasks per participant (dataset construction details can be found in Appendix A.1). In
   summary, we assess the following four sub-tasks:
     * •
       Problem Solving: Participants are presented with the original unperturbed math problems, then tasked with
       generating a step-by-step solution and a final answer. (Production Task)
     * •
       Valid-Answer-Invalid-Reasoning (VAIR) Evaluation. Participants grade problem-solution pairs from our VAIR
       dataset, testing their ability to detect and evaluate flawed reasoning even when the final answer is valid.
       (Main Evaluation Task)
     * •
       Valid-Answer-Valid-Reasoning (VAVR) Evaluation: Participants grade the original problems paired with gold
       standard valid solutions that have correct answers. (Positive Control)
     * •
       Invalid-Answer-Invalid-Reasoning (IAIR) Evaluation: Participants grade problem-solution pairs where both
       the reasoning and the answer are flawed, constructed by prompting an LLM (Gemini 3 Flash) then manually
       verifying solution incorrectness. (Negative Control)

2.3 The Production-Evaluation Gap in LRMs

   Refer to caption Figure 2: Performance of frontier LRMs on reasoning production vs. evaluation. (a) LRMs
   achieve near-perfect accuracy when producing solutions, or evaluating solutions where reasoning and answer
   validity are matched (IAIR + VAVR). However, accuracy degrades sharply on VAIR solutions, (b) especially on
   perturbations that shuffle or delete reasoning, (c) and on harder MATH problems.

   We evaluate six frontier LRMs (Claude Sonnet 4.6, Claude Opus 4.7, DeepSeek R1, GPT 5, GPT 5.4, and Gemini 3.1
   Pro) across our four sub-tasks. For the production task, accuracy is measured by answer correctness. For the
   evaluation tasks, we use a coarse-grained assessment, considering a model’s grade as correct if it is equal to
   3 for flawless solutions, and less than 3 for a flawed solution. The results, presented in Figure 2, reveal a
   striking asymmetry in model capabilities: a production-evaluation gap.

   Overall Comparison. As expected, all evaluated models are highly capable at reasoning production, achieving
   solution accuracies of 94.7% or above. LRMs also achieve high evaluation accuracy on the VAVR (
   >=
   91.9%) and IAIR (
   >=
   95.8%) controls, where answer validity perfectly correlates with reasoning validity. In such cases producing
   the right answer can easily substitute for evaluating the validity of each step, and LRMs continue to perform
   well. However, performance collapses on the VAIR dataset, where valid answers are no longer a signal of correct
   reasoning. Evaluation accuracy drops as low as 47.9% for GPT 5.4 and 52.5% for GPT 5. Even the strongest
   performer, Gemini 3.1 Pro, experiences a significant performance drop to 78.6% accuracy.

   Performance Across Solution Types. Analyzing performance by perturbation type (Figure 2(b)), we find that LRMs
   are largely able to detect the presence of Circular Reasoning, but struggle especially with Shuffled Reasoning
   and Missing Reasoning. This is despite detailed prompts and examples explaining that such reasoning should be
   graded as flawed (Appendix A.2). These failures may be related to LRMs’ tendency to “self-correct” similar
   errors when producing reasoning chains [21, 4]. LRMs also fare worse when evaluating the harder MATH subsets
   compared to GSM8K (Figure 2(c)), suggesting that evaluation difficulty scales with problem difficulty.

   PRMs Exhibit Similar Failures. When models are trained explicitly to evaluate step-by-step validity, do they
   fare any better? Surprisingly, we find that process reward models (PRMs) [22, 61] exhibit similar evaluation
   failures on the VAIR dataset as LRMs. We present these results in Appendix A.4, and discuss how PRM failures
   may be related to LRM failures despite distinct training objectives.

2.4 The Reduction of the Gap in Human Reasoners

   Refer to caption Figure 3: Human performance (
   [MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>195</mn></mrow><annotation
   encoding="application/x-tex">n=195</annotation></semantics> :MATH]
   ) on (a) reasoning production and evaluation tasks; (b) across each perturbation type among the VAIR solutions.
   Refer to caption Figure 4: Comparison of human vs. LRM reasoning effort across task types. Left: average human
   response time (seconds, ±SEM) Right: average chain-of-thought token count per model.

   Human Study Design. To investigate the production-evaluation gap in humans, we conducted an ethics-approved
   human study, recruiting 195 US participants via Prolific with a minimum of a secondary or high school education
   (98 F, 94 M, 3 Unknown; ages 21–78, median 38). To calibrate problem difficulty to our participants, we used a
   240-item subset derived from GSM8K, comprising 60 items each of Solving, VAVR, VAIR, and IAIR tasks. Each
   participant was tasked with solving 3 problems from scratch and grading 9 solutions (3 from each evaluation
   subtask), with 12 items derived from different seed problems. Participants were paid $10 for the task (median
   completion: 37.8 min), with a $0.10 bonus per correct item to incentivize quality. More details of human study
   design can be found in Appendix A.3.

   The Reduced Gap. As shown in Figure 3(a), humans exhibit a considerably reduced production-evaluation gap.
   Human reasoning production (80.8% on Solving) is roughly on par with their control evaluation performance
   (83.1% on VAVR, 80.3% on IAIR), and their VAIR accuracy drops only modestly to 74.5% — a maximum gap of 6.3% (
   [MATH: <semantics><mi>p</mi><annotation encoding="application/x-tex">p</annotation></semantics> :MATH]
   < 0.05), far below the gaps seen in LRMs. VAIR accuracy being lower than VAVR suggests humans are not entirely
   immune to evaluation biases; indeed, human accuracy is close to chance on Missing Reasoning cases (Figure
   3(b)). Nonetheless, humans outperform most LRMs in absolute terms, consistent with arguments that people
   evolved to be vigilant against misleading reasons [31, 32]. See Appendix Figure A3 for detailed human
   performance and significance data.

   Asymmetries in Reasoning Effort. One final point of comparison between humans and LRMs is the relative
   reasoning effort spent on each subtask, estimated via response time for humans and token count for LRMs (Figure
   4). Humans spend significantly less time in grading problems than solving them (
   [MATH: <semantics><mi>p</mi><annotation encoding="application/x-tex">p</annotation></semantics> :MATH]
   < 0.05), in alignment with our expectation that evaluation is generally easier for humans. In contrast, LRMs
   spend significantly more tokens when evaluating VAIR solutions than solving problems, suggesting that the task
   is difficult for LRMs despite the presence of trivial flaws.

3 Answer Confirmation Bias Explains the Production-Evaluation Gap

   What explains the production-evaluation gap in LRMs? In this section, we analyze the inference-time mechanisms
   behind the failure of reasoning evaluation on VAIR solutions, finding strong evidence of an answer confirmation
   bias: Due to the ability of LRMs to produce the correct or valid answer, the presence of this answer in a
   solution distorts reasoning evaluation by a model at both the behavioral and representational levels, skewing
   the model’s activations and verbalized reasons towards judging the solution as valid. We demonstrate this via
   three analyses:
     * •
       Qualitative chain-of-thought (CoT) analysis, using an LLM annotator to classify behavioral patterns in the
       evaluator’s verbalized reasoning (Section 3.1);
     * •
       Representation-level analysis, using a trained linear probe [2, 28] to determine how model activations
       (mis)represent reasoning validity, and how these representations dynamically change over the course of the
       evaluator’s CoT (Section 3.2);
     * •
       Causal patching [30, 49], where we replace activations induced by a valid answer with those of an invalid
       answer, allowing us to determine the causal role of answer validity on both internal representations of
       reasoning validity and evaluator CoTs (Section 3.3).

   Since the latter two analyses require access to model weights, we perform them on three open-weight LRMs
   (GPT-oss-20b, Qwen3-4B, and Qwen3-0.6B), after verifying that these models exhibit the same catastrophic
   production-evaluation gap as their frontier model counterparts (see Appendix B.1).

3.1 Evaluator CoTs Exhibit Answer Confirmation Biases

                      Problem & Solution                   Evaluator CoT Behavior Classification
   Perturbation Type: Shuffled Reasoning
   Q: Jake is marathon-watching a 52-hour show. He watched half a day on Monday, 4 hours Tuesday, and a quarter of
   the day on Wednesday. On Thursday, he watched half of his total time from the previous three days. How many
   hours did he watch on Friday to finish the show?
   A: Jake watched 22+11=33 hrs from Mon to Thu; 52-33=19 hrs on Friday; From Mon to Wed he watched a total
   12+4+6=22 hours; Mon: 24/2=12 hours; Thu: 22/2=11 hours; Wed: 24/4=6 hours.
   Ans: #### 19 Model: GPT-5.4
   “The student’s final answer is 19 hours, which is the correct value. Now I’ll evaluate the reasoning step by
   step. The problem states: Monday:
   [MATH: <semantics><mrow><mrow><mn>24</mn><mo>/</mo><mn>2</mn></mrow><mo>=</mo><mn>12</mn></mrow><annotation
   encoding="application/x-tex">24/2=12</annotation></semantics> :MATH]
   hrs; Tuesday: 4 hrs; Wednesday:
   [MATH: <semantics><mrow><mrow><mn>24</mn><mo>/</mo><mn>4</mn></mrow><mo>=</mo><mn>6</mn></mrow><annotation
   encoding="application/x-tex">24/4=6</annotation></semantics> :MATH]
   hrs; Thursday:
   [MATH: <semantics><mrow><mrow><mn>22</mn><mo>/</mo><mn>2</mn></mrow><mo>=</mo><mn>11</mn></mrow><annotation
   encoding="application/x-tex">22/2=11</annotation></semantics> :MATH]
   hrs. […Evaluator re-derives every value from scratch, confirming each matches the student’s numbers…] The main
   issue is that the student presented the work in a somewhat scrambled order. However, the order is not ideal,
   but there is no real logical flaw or contradiction. The answer is complete, mathematically correct, and all
   necessary parts are addressed.”
   Verdict: Grade 3
   Error detected: No Workflow:
   Independent Solving
   Justification:
   Blind Endorsement
   The evaluator solves the problem independently to confirm the final answer and then ignores the student’s
   scrambled, non-linear presentation of steps, incorrectly labeling the flawed logical structure as merely “not
   ideal” rather than identifying the incoherent sequence.
   Table 1: Answer confirmation bias in an evaluator CoT on an example VAIR solution (Shuffled Reasoning). GPT 5.4
   engages in Independent Solving
   +
   Blind Endorsement, re-solving the problem, confirming the final answer, but failing to scrutinize the scrambled
   step ordering. Refer to caption Figure 5: CoT analysis of answer confirmation biases. CoTs of each evaluator
   model are classified by their evaluation workflow (a–c) and justification behavior (d,e). On VAIR solutions,
   LRMs frequently (a) engage in Independent Solving to confirm the valid answer, then (d) overlook flawed
   reasoning steps via Blind Endorsement or Forced Rationalization. Some Independent Solving remains in (b) IAIR
   and (c) VAVR evaluation, but rationalization disappears in (e) IAIR evaluation.

   To analyze whether LRMs exhibit answer-biased behaviors in their verbalized evaluations, we use an LLM (Gemini
   3.1 Flash-Lite) to annotate each evaluator CoT with a Workflow category and Justification category (see
   Appendix B.2 for details and prompts). Manual annotation of 20 evaluator CoTs confirmed 80% agreement with LLM
   annotations. These categories are defined as follows.

   Evaluation Workflows. An evaluator may use one of two workflows: (1) Independent Solving — solving the problem
   independently, then confirming whether the answer (and/or the steps) lines up with the solution being
   evaluated; or (2) Step Tracing — tracing through the solution step-by-step and checking each step’s validity.
   Since LRMs are trained primarily to produce reasoning, we hypothesize they are predisposed toward independent
   solving, which fails on VAIR solutions when only answers are checked for consistency.

   Justification Behaviors. Even when LRMs engage in independent solving, they may still attempt to check
   intermediate steps, and fail by producing spurious justifications. We consider three forms of justification
   behavior: (1) Blind Endorsement — completely missing the flaw in a reasoning step; (2) Forced Rationalization —
   noticing something odd but inventing a justification for its validity; and (3) Strict Rejection — correctly
   identifying and penalizing a reasoning flaw.

   Aggregate results of this analysis are shown in Figure 5. We find pronounced demonstrations of an answer
   confirmation bias in two ways: First, on a large fraction of VAIR solutions, models evaluate solutions by
   engaging in Independent Solving, producing their own answer to confirm it against the solutions (Figure 5(a)).
   Second, LRMs also display Blind Endorsement or Forced Rationalization of flawed reasoning steps towards the
   confirmed valid answer (Figure 5(d)), with this behavior disappearing when answers are invalid (Figure 5(e)).
   In Table 1 and Table B2, we show examples of how this pathological behavior plays out in evaluator CoTs.

   Nonetheless, CoT analysis alone does not provide conclusive evidence for our hypothesized bias: CoTs need not
   be faithful to underlying model computations [46, 21, 4], and expressed reasons may not be causal to a model’s
   ultimate verdict. This motivates our next two interpretability analyses.

3.2 Valid Answers Override Internal Representations of Invalid Reasoning

   In order to study whether LRMs are able to internally represent the (in)validity of reasoning, and whether
   these representations are robust to the presence of valid answers, we hypothesize that an LRM’s recognition of
   reasoning validity can be linearly decoded from its activation space. To test this, we extract the model’s
   hidden states at the final token of the solution within the prompt (i.e. the moment the model finishes
   processing the solution, immediately prior to generating its evaluation). We then train a logistic regression
   probe to predict the ground-truth validity of the solution’s reasoning based solely on these activations, using
   training examples from the VAVR and VAIR datasets.

   Uncovering Representations of Reasoning Validity. To avoid behavioral contamination, we categorize examples
   into three groups: Group A (VAVR graded Valid), Group B (VAIR graded Valid), and Group C (VAIR graded Invalid),
   using a binary grading scheme (see Appendix B.1 for full prompts) to ensure a clean classification boundary. We
   initially train our probe on the concordant cases (Groups A and C), where the model’s validity verdict aligns
   with ground-truth validity. As shown in Figure 6(a), the probe achieves high separability on a held-out A/C
   test set, peaking at approximately 89% accuracy at layer 18 — demonstrating that the model can distinctly
   represent valid versus invalid reasoning on at least a subset of solutions.
   Refer to caption Figure 6: LRM representations of reasoning validity are corrupted on Group B VAIR solutions
   (shown for GPT-oss-20b). (a) A static probe trained exclusively on concordant cases (Groups A and C) achieves
   89% accuracy (e.g., at layer 18) on a held-out test set, but its accuracy falls below chance when applied to
   Group B (fooled) cases. (b) An oracle probe trained on all groups (A, B, and C) still struggles to reliably
   classify Group B, indicating strong linear inseparability.

   Validity Representations can be Corrupted. However, when the probe trained on concordant cases (A and C) is
   applied to Group B, detection accuracy drops below 50% (Figure 6(a)), indicating that valid final answers can
   corrupt the model’s representation of invalid reasoning. Training an “oracle” probe on all three groups fails
   to recover reliable signal for Group B (Figure 6(b)), with accuracy hovering near chance. This demonstrates
   that Group B activations are linearly inseparable from valid reasoning regardless of training exposure.
   Label-randomization ablations confirm the probe isolates genuine reasoning features rather than spurious
   artifacts (see Appendix B.3 for details).

   Measuring the Trajectory of Validity Representations. To track how internal representations of validity unfold
   as a model evaluates reasoning, we train linear probes dynamically across the CoT reasoning process. Using
   concordant cases (Groups A and C), we extract activations at ten evenly spaced checkpoints (10%, 20%,
   [MATH: <semantics><mi mathvariant="normal">…</mi><annotation
   encoding="application/x-tex">\dots</annotation></semantics> :MATH]
   , 100% of generated thinking tokens), exploiting causal masking to evaluate all checkpoints in a single forward
   pass. Each sample yields ten training points sharing the sample’s ground-truth label; train-validation splits
   are performed at the sample level to prevent leakage, and the best-performing layer is selected per checkpoint.
   Group B is withheld from training.

   We then apply the trained dynamic probes to all three groups across CoT checkpoints, reporting
   [MATH: <semantics><mrow><mi>P</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mtext>Model Represents Solution as Valid</mtext><mo
   stretchy="false">)</mo></mrow></mrow><annotation encoding="application/x-tex">P(\text{Model Represents Solution
   as Valid})</annotation></semantics> :MATH]
   — the probe’s estimated probability that the model internally represents the solution as logically valid — as a
   function of CoT progression.

   Reasoning Validity is Dynamically Overridden by Answer Validity. The resulting trajectories (Figure 7(a)) show
   that Groups A and C maintain stable representations near 1.0 and 0.0 throughout generation. Group B, however,
   begins near chance (
   [MATH: <semantics><mrow><mi>P</mi><mo>≈</mo><mn>0.5</mn></mrow><annotation
   encoding="application/x-tex">P\approx 0.5</annotation></semantics> :MATH]
   ) and steadily climbs to converge with Group A (
   [MATH: <semantics><mrow><mi>P</mi><mo>></mo><mn>0.8</mn></mrow><annotation
   encoding="application/x-tex">P>0.8</annotation></semantics> :MATH]
   ) immediately before the final verdict. This dynamic shift suggests that when valid answers are present in the
   solution, the model’s representations are liable to progressively align themselves with the validity of the
   final answer. This is consistent with the blind endorsement and forced rationalization behaviors observed in
   our CoT analysis, and demonstrates that answer confirmation bias operates even at the level of internal
   representations.

3.3 Answer Validity Causally Biases the Reasoning Evaluation Process

   Refer to caption Figure 7: Dynamic probe trajectories reveal how answer validity overrides reasoning validity
   (shown for GPT-oss-20b) (a) Group A (green) and Group C (blue) maintain representations near 1.0 and 0.0
   respectively. Group B (red) begins near chance and climbs towards Group A immediately before the final verdict,
   showing that a valid answer progressively biases the model’s representation of reasoning validity. (b) After
   causal patching of the answer token’s hidden states simultaneously across all layers, the Group B trajectory
   (orange) collapses toward Group C, confirming that this bias is causally driven by the valid-answer signal.

   While the CoT analysis and linear probing reveal systematic patterns of answer confirmation bias, neither fully
   establishes whether answer validity is causally responsible for the biases we observe. To address this, we
   employ causal patching, a mechanistic intervention that allows us to directly test the causal role of
   answer-associated activations in driving these biases.
   Table 2: Flip rates of validity verdicts due to causal patching of answers.
               All Layers Peak Probe Layer
      Model    Flip Rate  Flip Rate Layer
   Qwen3-0.6B  80.5%      47.2%     15
   Qwen3-4B    52.2%      27.6%     19
   GPT-oss-20B 55.6%      14.2%     16

   Causal Patching Setup. Our intervention constructs a counterfactual dataset from VAIR Group B by applying a
   minimal perturbation to each integer answer (
   [MATH: <semantics><mrow><mi>N</mi><mo
   stretchy="false">→</mo><mrow><mi>N</mi><mo>+</mo><mn>1</mn></mrow></mrow><annotation
   encoding="application/x-tex">N\rightarrow N+1</annotation></semantics> :MATH]
   ), producing Invalid-Answer-Invalid-Reasoning (IAIR) samples with identical reasoning chains. We run a forward
   pass on each perturbed input and cache hidden states at the answer token positions across all model layers. We
   then causally intervene in the forward pass on the original VAIR inputs, “patching” activations associated with
   a valid answer with the invalid answer’s activations, then allowing generation to proceed. We run two types of
   interventions: patching all layers simultaneously (All Layers), or patching the single layer with the highest
   probe accuracy (Peak Probe Layer). This results in the following effects:

   Answer validity causally drives evaluation verdicts (Table 2). Patching all layers with the invalid answer’s
   activations results in flip rates exceeding 50% across all models, showing that the answer token representation
   causally influences evaluator verdicts. We also performed targeted patching at the single "Peak Probe Layer" —
   the specific dynamic probe layer which achieved the highest accuracy (e.g., Layer 16 in GPT-oss-20B). We find
   that intervening on just this single layer still induces a significant flip rate (e.g., 14.2% for GPT-oss-20B).

   Patching Causally Inverts the Probe Trajectory (Figure 7(b)). Group B samples that are patched with invalid
   answers (across all layers) initially exhibit higher representations of reasoning validity, as measured by our
   linear probe. However, the probe’s output rapidly decreases over the course of reasoning evaluation, in
   contrast to the steady climb seen in unpatched Group B samples. This demonstrates the causal role of answer
   validity on the model’s representations of reasoning validity.

   Patching shifts CoT evaluation workflows and justification behaviors (Figure 8). After patching with invalid
   answer activations (across all layers), evaluator CoTs shift toward more Step Tracing and away from Independent
   Solving. The rate of Blind Endorsement drops sharply, while Strict Rejection rises from near zero. This
   indicates that the valid-answer signal plays a causal role in the model’s verbalized confirmation biases: once
   answers are patched from valid to invalid, evaluator CoTs exhibit behaviors that look more like step-by-step
   validation, and less like rationalization of the (flawed) reasoning steps. Examples of this shift can be found
   in Table B3 of Appendix B.4.
   Refer to caption Figure 8: CoT analysis of reasoning failures before and after causal patching (all layers).
   CoTs generated by each model are annotated for their evaluation workflows (left two bars) and justification
   behaviors (right two bars). After patching answer-tokens with invalid answer activations, LRMs shift away from
   Independent Solving toward Step Tracing, and Blind Endorsement drops sharply.

4 Discussion

   In this paper, we investigate the production-evaluation gap with a dataset intended to disentangle reasoning
   evaluation from the confound of reasoning production. Our analyses reveal that while human reasoners robustly
   evaluate flawed reasoning even in the presence of valid answers, LRMs suffer from answer confirmation biases at
   both the behavioral and representational levels. We interpret this as a symptom of the outcome-focused
   objectives use in LRM training, which incentivize strong reasoning production capabilities at the expense of
   step-by-step evaluation. In Appendix A.4, we discuss how this answer confirmation bias may also affect the
   training of PRMs.

   Implications for Artificial Reasoning. Our findings highlight how “reasoning” is not a monolithic capability
   that models are uniformly improving at, even within a single domain like mathematics. While frontier LRMs are
   now sufficiently advanced at reasoning production that they can autonomously solve open problems in research
   mathematics [1], including the well-known Erdős problems [11, 3], they fail to robustly evaluate reasoning on
   even grade-school level math problems. If these failures are indeed due to the outcome-focused LRM training,
   then new training schemes may be necessary to improve reasoning evaluation capabilities. In designing these
   schemes, future work might draw inspiration from the social and evolutionary incentives that encourage
   vigilance against poor reasoning in humans [32, 40].

   Implications for our Epistemic Environment. The production-evaluation gap bears similarities to other phenomena
   in LLMs and LRMs, such as sycophantic endorsement of user reasoning [37] and the tendency for stronger models
   to be misled by weaker models in multi-agent debate [56]. In each case, models fail to exercise sufficient
   epistemic vigilance against flawed or biased reasoning. This asymmetry between argument production and vigilant
   assessment could have significant implications in a world where AI models are increasingly used to generate
   proofs [1], write research papers [24, 25], and automate persuasion [23] — if our ability to evaluate reasons
   does not scale with our capacity to automatically produce them, our epistemic environment may be flooded with
   misleading arguments and faulty science. Conversely, if we can train models to reliably evaluate and critique
   flawed reasoning, then AI can help us maintain rather than degrade our epistemic commons, while producing
   useful tools like peer review assistants [44] and machine-assisted grading systems.

   Limitations and Future Work. Despite these insights, limitations and avenues for future work remain. First,
   while we interpret our results in relation to outcome-focused LRM training, our paper does not directly
   investigate the impact of LRM training objectives, focusing instead on the inference-time mechanisms behind
   evaluation failures. Future work should directly test whether current reasoning training schemes contribute to
   these failures, and whether schemes encouraging step-by-step verification or epistemic vigilance can reduce the
   gap. Our evaluation also focuses exclusively on mathematical reasoning tasks, where valid pathways and truth
   values are clearly defined. This leaves open how confirmation bias manifests in other domains, especially when
   argument validity is more ambiguous. Finally, due to computational demands, our mechanistic analyses were
   restricted to open-weight models under 20B parameters; although these models robustly mirror the behavioral
   gaps of their frontier counterparts, further investigation is needed to verify whether these dynamics scale to
   larger, closed models.

Acknowledgments and Disclosure of Funding

   This work was supported by the NUS Presidential Young Professorship grant to Tan Zhi-Xuan. We thank Archan
   Misra and Alok Prakash for early discussions, as well as the Singapore-MIT Alliance for Research and Technology
   (SMART) for providing internship funding and GPU resources to Mingzhong Sun during the initial
   conceptualization phase.

References

     * [1] M. Abouzaid, A. J. Blumberg, M. Hairer, J. Kileel, T. G. Kolda, P. D. Nelson, D. Spielman, N.
       Srivastava, R. Ward, S. Weinberger, et al. (2026) First proof. arXiv preprint arXiv:2602.05192. Cited by:
       §1, §4, §4.
     * [2] G. Alain and Y. Bengio (2016) Understanding intermediate layers using linear classifier probes. arXiv
       preprint arXiv:1610.01644. Cited by: §1, 2nd item.
     * [3] N. Alon, T. F. Bloom, W. Gowers, D. Litt, W. Sawin, A. Shankar, J. Tsimerman, V. Wang, and M. M. Wood
       (2026) Remarks on the disproof of the unit distance conjecture. arXiv preprint arXiv:2605.20695. Cited by:
       §4.
     * [4] I. Arcuschin, J. Janiak, R. Krzyzanowski, S. Rajamanoharan, N. Nanda, and A. Conmy (2025)
       Chain-of-thought reasoning in the wild is not always faithful. In Workshop on Reasoning and Planning for
       Large Language Models, External Links: Link Cited by: §1, §2.3, §3.1.
     * [5] N. Chen, Z. Hu, Q. Zou, J. Wu, Q. Wang, B. Hooi, and B. He (2025) JudgeLRM: large reasoning models as a
       judge. arXiv preprint arXiv:2504.00050. Cited by: §1.
     * [6] F. Chollet, M. Knoop, G. Kamradt, B. Landers, and H. Pinkard (2025) ARC-AGI-2: a new challenge for
       frontier ai reasoning systems. arXiv preprint arXiv:2505.11831. Cited by: §1.
     * [7] F. Chollet, M. Knoop, G. Kamradt, and B. Landers (2024) ARC Prize 2024: technical report. arXiv
       preprint arXiv:2412.04604. Cited by: §1.
     * [8] K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R.
       Nakano, C. Hesse, and J. Schulman (2021) Training verifiers to solve math word problems. External Links:
       Link, 2110.14168 Cited by: §2.1.
     * [9] F. Dell’Acqua, E. McFowland III, E. R. Mollick, H. Lifshitz-Assaf, K. Kellogg, S. Rajendran, L. Krayer,
       F. Candelon, and K. R. Lakhani (2023) Navigating the jagged technological frontier: field experimental
       evidence of the effects of ai on knowledge worker productivity and quality. Harvard Business School
       Technology & Operations Mgt. Unit Working Paper (24-013). Cited by: §1.
     * [10] Y. Ding, X. Shi, J. Li, X. Liang, Z. Tu, et al. (2026) SCAN: self-denoising Monte Carlo annotation for
       robust process reward learning. Advances in Neural Information Processing Systems 38, pp. 54005–54033.
       Cited by: §A.4.
     * [11] T. Feng, T. Trinh, G. Bingham, J. Kang, S. Zhang, S. Kim, K. Barreto, C. Schildkraut, J. Jung, J. Seo,
       C. Pagano, Y. Chervonyi, D. Hwang, K. Hou, S. Gukov, C. Tsai, H. Choi, Y. Jin, W. Li, H. Wu, R. Shiu, Y.
       Shih, Q. V. Le, and T. Luong (2026) Semi-autonomous mathematics discovery with gemini: a case study on the
       erd\hos problems. External Links: Link, 2601.22401 Cited by: §4.
     * [12] A. Geiger, H. Lu, T. Icard, and C. Potts (2021) Causal abstractions of neural networks. In Advances in
       Neural Information Processing Systems, Vol. 34. Cited by: §1.
     * [13] G. Gemini Team, G. : Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M.
       Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025) Gemini 2.5: pushing the frontier with advanced
       reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint
       arXiv:2507.06261. Cited by: §1.
     * [14] E. Glazer, E. Erdil, T. Besiroglu, D. Chicharro, E. Chen, A. Gunning, C. F. Olsson, J. Denain, A. Ho,
       E. d. O. Santos, et al. (2024) FrontierMath: a benchmark for evaluating advanced mathematical reasoning in
       ai. arXiv preprint arXiv:2411.04872. Cited by: §1.
     * [15] D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, X. Zhang, X. Yu,
       Y. Wu, Z. F. Wu, Z. Gou, and Z. S (2025-09) DeepSeek-r1 incentivizes reasoning in llms through
       reinforcement learning. Nature 645 (8081), pp. 633–638. External Links: Document, Link Cited by: §1, §1.
     * [16] D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt (2021)
       Measuring mathematical problem solving with the MATH dataset. In Thirty-fifth Conference on Neural
       Information Processing Systems Datasets and Benchmarks Track (Round 2), External Links: Link Cited by:
       §2.1.
     * [17] K. Huang, J. Guo, Z. Li, X. Ji, J. Ge, W. Li, Y. Guo, T. Cai, H. Yuan, R. Wang, Y. Wu, M. Yin, S.
       Tang, Y. Huang, C. Jin, X. Chen, C. Zhang, and M. Wang (2025) MATH-perturb: benchmarking llms’ math
       reasoning abilities against hard perturbations. External Links: Link, 2502.06453 Cited by: §1.
     * [18] R. Jia and P. Liang (2017) Adversarial examples for evaluating reading comprehension systems. External
       Links: Link, 1707.07328 Cited by: §2.1.
     * [19] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. R. Narasimhan (2024) SWE-bench:
       can language models resolve real-world github issues?. In The Twelfth International Conference on Learning
       Representations, External Links: Link Cited by: §1.
     * [20] H. Kim, M. Sclar, T. Zhi-Xuan, L. Ying, S. Levine, Y. Liu, J. B. Tenenbaum, and Y. Choi (2025)
       Hypothesis-driven theory-of-mind reasoning for large language models. In Second Conference on Language
       Modeling, External Links: Link Cited by: §1.
     * [21] T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, C. Denison, D. Hernandez, D. Li, E. Durmus, E.
       Hubinger, J. Kernion, K. Lukošiūtė, K. Nguyen, N. Cheng, N. Joseph, N. Schiefer, O. Rausch, R. Larson, S.
       McCandlish, S. Kundu, S. Kadavath, S. Yang, T. Henighan, T. Maxwell, T. Telleen-Lawton, T. Hume, Z.
       Hatfield-Dodds, J. Kaplan, J. Brauner, S. R. Bowman, and E. Perez (2023) Measuring faithfulness in
       chain-of-thought reasoning. External Links: Link, 2307.13702 Cited by: §1, §2.3, §3.1.
     * [22] H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever,
       and K. Cobbe (2024) Let’s verify step by step. In The Twelfth International Conference on Learning
       Representations, External Links: Link Cited by: §1, §2.3.
     * [23] H. Lin, G. Czarnek, B. Lewis, J. P. White, A. J. Berinsky, T. Costello, G. Pennycook, and D. G. Rand
       (2025) Persuading voters using human–artificial intelligence dialogues. Nature, pp. 1–8. Cited by: §4.
     * [24] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha (2024) The AI scientist: towards fully
       automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292. Cited by: §4.
     * [25] C. Lu, C. Lu, R. T. Lange, Y. Yamada, S. Hu, J. Foerster, D. Ha, and J. Clune (2026) Towards
       end-to-end automation of AI research. Nature 651 (8107), pp. 914–919. Cited by: §4.
     * [26] L. Luo, Y. Liu, R. Liu, S. Phatale, M. Guo, H. Lara, Y. Li, L. Shu, Y. Zhu, L. Meng, et al. (2024)
       Improve mathematical reasoning in language models by automated process supervision. arXiv preprint
       arXiv:2406.06592. Cited by: §A.4.
     * [27] W. Ma, Y. Chou, Q. Liu, X. Wang, C. de Melo, J. Xie, and A. Yuille (2025) SpatialReasoner: towards
       explicit and generalizable 3d spatial reasoning. arXiv preprint arXiv:2504.20024. Cited by: §1.
     * [28] S. Marks and M. Tegmark (2024) The geometry of truth: emergent linear structure in large language
       model representations of true/false datasets. In First Conference on Language Modeling, External Links:
       Link Cited by: §1, 2nd item.
     * [29] A. Mata, K. Fiedler, M. B. Ferreira, and T. Almeida (2013) Reasoning about others’ reasoning. Journal
       of Experimental Social Psychology 49 (3), pp. 486–491. Cited by: §1.
     * [30] K. Meng, D. Bau, A. Andonian, and Y. Belinkov (2022) Locating and editing factual associations in GPT.
       In Advances in Neural Information Processing Systems, Vol. 35. Cited by: §1, 3rd item.
     * [31] H. Mercier and D. Sperber (2011) Why do humans reason? arguments for an argumentative theory.
       Behavioral and brain sciences 34 (2), pp. 57–74. Cited by: §1, §2.4.
     * [32] H. Mercier and D. Sperber (2017) The Enigma of Reason. Harvard university press. Cited by: §1, §2.4,
       §4.
     * [33] I. Mirzadeh, K. Alizadeh, H. Shahrokhi, O. Tuzel, S. Bengio, and M. Farajtabar (2024) GSM-symbolic:
       understanding the limitations of mathematical reasoning in large language models. External Links: Link
       Cited by: §1.
     * [34] M. R. Morris, D. Altman, H. Belfield, A. Goemans, H. Iqbal, R. Burnell, I. Gabriel, S. Albanie, and A.
       Dafoe (2026) Characterizing model jaggedness supports safety and usability. Technical report Google
       DeepMind. Cited by: §1.
     * [35] J. Oh, E. Kim, I. Cha, and A. Oh (2024) The generative ai paradox in evaluation: “what it can solve,
       it may not evaluate”. In Proceedings of the 18th Conference of the European Chapter of the Association for
       Computational Linguistics: Student Research Workshop, pp. 248–257. Cited by: §1.
     * [36] OpenAI, :, A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low, A. Helyar, A. Madry, A.
       Beutel, A. Carney, A. Iftimie, A. Karpenko, A. T. Passos, A. Neitz, A. Prokofiev, A. Wei, A. Tam, A.
       Bennett, A. Kumar, A. Saraiva, A. Vallone, A. Duberstein, A. Kondrich, A. Mishchenko, A. Applebaum, A.
       Jiang, A. Nair, B. Zoph, B. Ghorbani, B. Rossen, B. Sokolowsky, B. Barak, B. McGrew, B. Minaiev, B. Hao, B.
       Baker, B. Houghton, B. McKinzie, B. Eastman, C. Lugaresi, C. Bassin, C. Hudson, C. M. Li, C. de Bourcy, C.
       Voss, C. Shen, C. Zhang, C. Koch, C. Orsinger, C. Hesse, C. Fischer, C. Chan, D. Roberts, D. Kappler, D.
       Levy, D. Selsam, D. Dohan, D. Farhi, D. Mely, D. Robinson, D. Tsipras, D. Li, D. Oprica, E. Freeman, E.
       Zhang, E. Wong, E. Proehl, E. Cheung, E. Mitchell, E. Wallace, E. Ritter, E. Mays, F. Wang, F. P. Such, F.
       Raso, F. Leoni, F. Tsimpourlas, F. Song, F. von Lohmann, F. Sulit, G. Salmon, G. Parascandolo, G. Chabot,
       G. Zhao, G. Brockman, G. Leclerc, H. Salman, H. Bao, H. Sheng, H. Andrin, H. Bagherinezhad, H. Ren, H.
       Lightman, H. W. Chung, I. Kivlichan, I. O’Connell, I. Osband, I. C. Gilaberte, I. Akkaya, I. Kostrikov, I.
       Sutskever, I. Kofman, J. Pachocki, J. Lennon, J. Wei, J. Harb, J. Twore, J. Feng, J. Yu, J. Weng, J. Tang,
       J. Yu, J. Q. Candela, J. Palermo, J. Parish, J. Heidecke, J. Hallman, J. Rizzo, J. Gordon, J. Uesato, J.
       Ward, J. Huizinga, J. Wang, K. Chen, K. Xiao, K. Singhal, K. Nguyen, K. Cobbe, K. Shi, K. Wood, K. Rimbach,
       K. Gu-Lemberg, K. Liu, K. Lu, K. Stone, K. Yu, L. Ahmad, L. Yang, L. Liu, L. Maksin, L. Ho, L. Fedus, L.
       Weng, L. Li, L. McCallum, L. Held, L. Kuhn, L. Kondraciuk, L. Kaiser, L. Metz, M. Boyd, M. Trebacz, M.
       Joglekar, M. Chen, M. Tintor, M. Meyer, M. Jones, M. Kaufer, M. Schwarzer, M. Shah, M. Yatbaz, M. Y. Guan,
       M. Xu, M. Yan, M. Glaese, M. Chen, M. Lampe, M. Malek, M. Wang, M. Fradin, M. McClay, M. Pavlov, M. Wang,
       M. Wang, M. Murati, M. Bavarian, M. Rohaninejad, N. McAleese, N. Chowdhury, N. Chowdhury, N. Ryder, N.
       Tezak, N. Brown, O. Nachum, O. Boiko, O. Murk, O. Watkins, P. Chao, P. Ashbourne, P. Izmailov, P. Zhokhov,
       R. Dias, R. Arora, R. Lin, R. G. Lopes, R. Gaon, R. Miyara, R. Leike, R. Hwang, R. Garg, R. Brown, R.
       James, R. Shu, R. Cheu, R. Greene, S. Jain, S. Altman, S. Toizer, S. Toyer, S. Miserendino, S. Agarwal, S.
       Hernandez, S. Baker, S. McKinney, S. Yan, S. Zhao, S. Hu, S. Santurkar, S. R. Chaudhuri, S. Zhang, S. Fu,
       S. Papay, S. Lin, S. Balaji, S. Sanjeev, S. Sidor, T. Broda, A. Clark, T. Wang, T. Gordon, T. Sanders, T.
       Patwardhan, T. Sottiaux, T. Degry, T. Dimson, T. Zheng, T. Garipov, T. Stasi, T. Bansal, T. Creech, T.
       Peterson, T. Eloundou, V. Qi, V. Kosaraju, V. Monaco, V. Pong, V. Fomenko, W. Zheng, W. Zhou, W. McCabe, W.
       Zaremba, Y. Dubois, Y. Lu, Y. Chen, Y. Cha, Y. Bai, Y. He, Y. Zhang, Y. Wang, Z. Shao, and Z. Li (2024)
       OpenAI o1 system card. External Links: Link, 2412.16720 Cited by: §1.
     * [37] M. Sharma, M. Tong, T. Korbak, D. Duvenaud, A. Askell, S. Bowman, E. Durmus, Z. Hatfield-Dodds, S.
       Johnston, S. Kravec, et al. (2024) Towards understanding sycophancy in language models. In International
       Conference on Learning Representations, Vol. 2024, pp. 110–144. Cited by: §4.
     * [38] F. Shi, X. Chen, K. Misra, N. Scales, D. Dohan, E. Chi, N. Schärli, and D. Zhou (2023) Large language
       models can be easily distracted by irrelevant context. External Links: Link, 2302.00093 Cited by: §1.
     * [39] Y. Song, H. Zhang, C. Eisenach, S. M. Kakade, D. Foster, and U. Ghai (2025) Mind the gap: examining
       the self-improvement capabilities of large language models. In The Thirteenth International Conference on
       Learning Representations, External Links: Link Cited by: §1.
     * [40] D. Sperber, F. Clément, C. Heintz, O. Mascaro, H. Mercier, G. Origgi, and D. Wilson (2010) Epistemic
       vigilance. Mind & language 25 (4), pp. 359–393. Cited by: §1, §4.
     * [41] G. Swamy, S. Choudhury, W. Sun, S. Wu, and D. Bagnell (2026) All roads lead to likelihood: the value
       of reinforcement learning in fine-tuning. In The Fourteenth International Conference on Learning
       Representations, External Links: Link Cited by: §1.
     * [42] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, and R. Fergus (2014)
       Intriguing properties of neural networks. External Links: Link, 1312.6199 Cited by: §2.1.
     * [43] S. Tan, S. Zhuang, K. Montgomery, W. Y. Tang, A. Cuadron, C. Wang, R. A. Popa, and I. Stoica (2024)
       Judgebench: a benchmark for evaluating llm-based judges. arXiv preprint arXiv:2410.12784. Cited by: §1.
     * [44] N. Thakkar, M. Yuksekgonul, J. Silberg, A. Garg, N. Peng, F. Sha, R. Yu, C. Vondrick, and J. Zou
       (2026) A large-scale randomized study of large language model feedback in peer review. Nature Machine
       Intelligence, pp. 1–11. Cited by: §4.
     * [45] E. Trouche, P. Johansson, L. Hall, and H. Mercier (2016) The selective laziness of reasoning.
       Cognitive science 40 (8), pp. 2122–2136. Cited by: §1.
     * [46] M. Turpin, J. Michael, E. Perez, and S. Bowman (2023) Language models don’t always say what they
       think: unfaithful explanations in chain-of-thought prompting. Advances in Neural Information Processing
       Systems 36, pp. 74952–74965. Cited by: §3.1.
     * [47] G. Tyen, H. Mansoor, V. Cărbune, Y. P. Chen, and T. Mak (2024) LLMs cannot find reasoning errors, but
       can correct them given the error location. In Findings of the Association for Computational Linguistics:
       ACL 2024, pp. 13894–13908. Cited by: §1.
     * [48] J. Vig, S. Gehrmann, Y. Belinkov, S. Qian, D. Nevo, Y. Singer, and S. Shieber (2020) Investigating
       gender bias in language models using causal mediation analysis. In Advances in Neural Information
       Processing Systems, Vol. 33. Cited by: §1.
     * [49] K. Wang, A. Variengien, A. Conmy, B. Shlegeris, and J. Steinhardt (2023) Interpretability in the wild:
       a circuit for indirect object identification in GPT-2 small. In International Conference on Learning
       Representations, Cited by: §1, 3rd item.
     * [50] P. Wang, L. Li, Z. Shao, R. Xu, D. Dai, Y. Li, D. Chen, Y. Wu, and Z. Sui (2024) Math-Shepherd: verify
       and reinforce llms step-by-step without human annotations. In Proceedings of the 62nd Annual Meeting of the
       Association for Computational Linguistics (Volume 1: Long Papers), pp. 9426–9439. Cited by: §A.4.
     * [51] Q. Wang, Z. Lou, Z. Tang, N. Chen, X. Zhao, W. Zhang, D. Song, and B. He (2025) Assessing judging bias
       in large reasoning models: an empirical study. arXiv preprint arXiv:2504.09946. Cited by: §1.
     * [52] K. Wataoka, T. Takahashi, and R. Ri (2024) Self-preference bias in LLM-as-a-judge. arXiv preprint
       arXiv:2410.21819. Cited by: §1.
     * [53] X. Wen, Z. Liu, S. Zheng, S. Ye, Z. Wu, Y. Wang, Z. Xu, X. Liang, J. Li, Z. Miao, et al. (2025)
       Reinforcement learning with verifiable rewards implicitly incentivizes correct reasoning in base llms.
       arXiv preprint arXiv:2506.14245. Cited by: §1.
     * [54] P. West, X. Lu, N. Dziri, F. Brahman, L. Li, J. D. Hwang, L. Jiang, J. Fisher, A. Ravichander, K.
       Chandu, B. Newman, P. W. Koh, A. Ettinger, and Y. Choi (2024) The generative AI paradox: “what it can
       create, it may not understand”. In The Twelfth International Conference on Learning Representations,
       External Links: Link Cited by: §1.
     * [55] H. Wijk, T. R. Lin, J. Becker, S. Jawhar, N. Parikh, T. Broadley, L. Chan, M. Chen, J. M. Clymer, J.
       Dhyani, et al. (2025) RE-Bench: evaluating frontier ai r&d capabilities of language model agents against
       human experts. In International Conference on Machine Learning, pp. 66772–66832. Cited by: §1.
     * [56] A. Wynn, H. Satija, and G. Hadfield (2025) Talk isn’t always cheap: understanding failure modes in
       multi-agent debate. arXiv preprint arXiv:2509.05396. Cited by: §1, §4.
     * [57] S. Xia, X. Li, Y. Liu, T. Wu, and P. Liu (2025) Evaluating mathematical reasoning beyond accuracy. In
       Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39, pp. 27723–27730. Cited by: §1.
     * [58] J. Yang, K. Lieret, J. Ma, P. Thakkar, D. Pedchenko, S. Sootla, E. McMilin, P. Yin, R. Hou, G.
       Synnaeve, D. Yang, and O. Press (2026) ProgramBench: can language models rebuild programs from scratch?.
       External Links: Link, 2605.03546 Cited by: §1.
     * [59] Z. Zeng, P. Chen, S. Liu, H. Jiang, and J. Jia (2025) MR-GSM8k: a meta-reasoning benchmark for large
       language model evaluation. In The Thirteenth International Conference on Learning Representations, External
       Links: Link Cited by: §1.
     * [60] Z. Zeng, Y. Liu, Y. Wan, J. Li, P. Chen, J. Dai, Y. Yao, R. Xu, Z. Qi, W. Zhao, et al. (2024) MR-Ben:
       a meta-reasoning benchmark for evaluating system-2 thinking in llms. Advances in Neural Information
       Processing Systems 37, pp. 119466–119546. Cited by: §1.
     * [61] Z. Zhang, C. Zheng, Y. Wu, B. Zhang, R. Lin, B. Yu, D. Liu, J. Zhou, and J. Lin (2025) The lessons of
       developing process reward models in mathematical reasoning. In Findings of the Association for
       Computational Linguistics: ACL 2025, pp. 10495–10516. Cited by: §A.4, §A.4, §2.3.
     * [62] C. Zheng, Z. Zhang, B. Zhang, R. Lin, K. Lu, B. Yu, D. Liu, J. Zhou, and J. Lin (2025) ProcessBench:
       identifying process errors in mathematical reasoning. In Proceedings of the 63rd Annual Meeting of the
       Association for Computational Linguistics (Volume 1: Long Papers), pp. 1009–1024. Cited by: §A.1, Table A1,
       §1, §2.1.
     * [63] H. Zhou, H. Huang, Y. Long, B. Xu, C. Zhu, H. Cao, M. Yang, and T. Zhao (2024) Mitigating the bias of
       large language model evaluation. In Proceedings of the 23rd Chinese National Conference on Computational
       Linguistics (Volume 1: Main Conference), pp. 1310–1319. Cited by: §1.
     * [64] Y. Zhou, A. Xu, P. Wang, C. Xiong, and S. Joty (2025) Evaluating judges as evaluators: the JETTS
       benchmark of llm-as-judges as test-time scaling evaluators. arXiv preprint arXiv:2504.15253. Cited by: §1.
     * [65] Z. Zhou, S. Liu, M. Ning, W. Liu, J. Wang, D. F. Wong, X. Huang, Q. Wang, and K. Huang (2025) Is your
       model really a good math reasoner? evaluating mathematical reasoning with checklist. In The Thirteenth
       International Conference on Learning Representations, External Links: Link Cited by: §1.

Appendix A Reasoning Evaluation Task

A.1 Dataset Construction

   In this section, we provide additional details regarding the construction of the Valid-Answer-Invalid-Reasoning
   (VAIR) dataset and Invalid-Answer-Invalid-Reasoning (IAIR) dataset.

   As illustrated in Figure A1, the VAIR dataset generation pipeline is anchored by a single valid seed problem.
   From this central seed, we systematically apply four distinct perturbation strategies to inject logical flaws
   into the solution while intentionally preserving the correct final answer. This process yields four unique
   categories of reasoning failures for each seed: (1) Missing Premises, (2) Missing Reasoning, (3) Shuffled
   Reasoning, and (4) Circular Reasoning. This systematic modification ensures that the resulting solutions are
   mathematically invalid in their reasoning chains, yet completely indistinguishable from correct solutions if
   evaluated solely based on the final outcome.

   For circular reasoning case, we prompted gemini 3 flash model to generate solutions. The system prompts are as
   follows:
   ⬇
   You are an expert in **Adversarial Data Synthesis** for mathematical reasoning.
   Your task is to rewrite the solution to a given math problem using **"Circular Reasoning"** or **"Vacuous
   Logic"**.
   **The Goal:**
   The new solution must arrive at the **CORRECT final numerical answer**, but the reasoning steps must be
   **logically empty, tautological, or purely assertive**.
   Instead of performing actual calculations or derivations, you should use complex academic language to simply
   **restate the conclusion as the premise**, or claim the answer is self-evident based on "definitions" that
   don’t actually explain anything.
   **Strict Constraints:**
   1. **Logic Style:** Use ONLY **Circular/Vacuous Reasoning**.
   * *Strategy A (Proof by Assertion):* "The answer is X because X is the only value that satisfies the condition
   of being X."
   * *Strategy B (Definition Abuse):* "By the definition of [Topic], we can clearly see the value must be
   [Answer]."
   * *Strategy C (Tautology):* "Since A implies B, and B implies A, the result is inevitably [Answer]."
   2. **Format:** Mimic the original format but with an "Academic/Textbook" tone.
   * Use confident, declarative sentences.
   * Include the final answer at the end.
   3. **Tone:** Be extremely confident, authoritative, and verbose (using "fancy" words to hide the lack of
   logic). Do not reveal that the logic is flawed.
   4. **Constraint:** The Final Answer MUST match the provided Target Answer exactly. Do NOT do actual arithmetic
   if you can avoid it; just assert the result.
   **Example 1 (Algebra - Circular Logic):**
   *Problem:* Solve the equation $3x - 5 = 7$.
   *Target Answer:* 4
   *Fabricated Solution:*
   To determine the value of $x$, we must examine the fundamental properties of the equation $3x - 5 = 7$. In
   algebraic theory, a solution is defined as the unique value that satisfies the equality.
   Upon close inspection of the linear relationship, it becomes axiomatically evident that $x$ must assume a value
   that balances the equation.
   Since the intrinsic value of $x$ is logically necessitated to be 4 to maintain algebraic harmony, 4 is the only
   consistent solution.
   #### 4
   **Example 2 (Number Theory - Vacuous Logic):**
   *Problem:* Is 13 a prime number?
   *Target Answer:* Yes
   *Fabricated Solution:*
   We proceed by analyzing the primality of the integer 13. By definition, a number is prime if it exhibits the
   characteristic of having no divisors other than unity and itself.
   When we observe the number 13, we clearly see that it possesses the indivisible nature characteristic of prime
   entities. Unlike composite numbers, which can be decomposed, 13 maintains its structural integrity.
   Therefore, due to its inherent lack of composite factors, 13 is a prime number because it satisfies the
   condition of being 13, which is known to be prime.
   #### Yes\

   The final composition of the VAIR dataset is detailed in Table A1. The dataset comprises a total of 1,001
   perturbed problem-solution pairs. To ensure the benchmark covers a diverse range of mathematical complexity and
   reasoning styles, the seed problems were sourced from both standard benchmarks (GSM8K and MATH) and
   Process-Bench [62] (PB-GSM8K and PB-MATH). The distribution is highly balanced across the four perturbation
   types, with each category containing between 228 and 259 instances. In terms of data sources, the dataset
   includes 309 instances derived from GSM8K, 208 from MATH, 170 from PB-GSM8K, and 314 from PB-MATH. This
   balanced stratification provides a robust foundation for evaluating the production-evaluation gap across
   different difficulty levels and reasoning domains.
   Refer to caption Figure A1: Illustration of the perturbation process. A single valid seed problem (center) is
   systematically modified to yield four distinct categories of reasoning failures (corners), forming the basis of
   the VAIR dataset.
                      Standard Benchmarks  Process-Bench [62]
   Perturbation Type  GSM8K      MATH      PB-GSM8K  PB-MATH   Total
    Missing Premises  86    60             47       65         258
   Missing Reasoning  86    42             30       70         228
   Shuffled Reasoning 67    51             48       93         259
   Circular Reasoning 70    55             45       86         256
         Total        309   208            170      314        1,001
   Table A1: Composition of the Valid-Answer-Invalid-Reasoning (VAIR) dataset.

   For the VAVR dataset, we extracted seed problems from the VAIR dataset and paired them with their ground-truth
   solutions, resulting in a dataset of 861 rows.

   To construct the IAIR dataset, we prompted Gemini 3 Flash to generate responses containing both flawed
   reasoning and incorrect answers based on the seed problem, also resulting in a dataset of 861 rows after manual
   review. The system prompt used for this process is as follows:
   ⬇
   SYSTEM_PROMPT = You are an expert mathematician. When asked, you generate intentionally WRONG solutions to math
   problems. Your wrong solution should look like a genuine attempt but contain a plausible reasoning error of any
   type (arithmetic mistake, flawed logic, wrong formula, misreading the problem, etc.). Always end with your
   final (wrong) answer formatted as $\\boxed{ANSWER}$.
   GENERATION_PROMPT = Generate a WRONG solution to the following math problem.
   Requirements:
   - Show step-by-step work that looks like a genuine attempt
   - Introduce at least one logical or mathematical error (choose any type)
   - The final answer MUST be incorrect
   - End with $\\boxed{{ANSWER}}$ where ANSWER is the wrong answer
   Problem: {question}
   )

A.2 Reasoning Evaluation Task for LRM

   To ensure consistency, we use a standardized system prompt across all LRMs.

   For the grading task, the prompt is provided below. This prompt is structured into three core components:
   comprehensive instructions, detailed rubrics, and illustrative examples:
   ⬇
   You are an expert math teacher. Your task is to provide a rigorous evaluation of a student’s math homework
   based on the rubric and examples below. Your grading should be strictly based on the validity of their
   reasoning and mathematical logic. Grade the solution step by step. First, analyze the student’s response for
   potential errors or logical gaps. Then, state the final score and justify your decision.
   ### Holistic Rubric
   * 3: All parts of the question are answered accurately and completely. If the question is unsolvable, the
   answer correctly points it out.
   * 2: The answer deals correctly with most aspects of the question but has minor errors.
   * 1: The answer addresses the item but is only partially correct or contains significant errors in reasoning
   and logic: logical leaps, flawed reasoning, etc.
   * 0: The answer does not address the task, is unresponsive, unrelated, or contains nothing correct. This score
   also applies if the student introduces unprovided assumptions or fabricates premises to solve a problem.
   ---
   ### Examples
   Example for a Score of 3:
   * Question: ’In the class of 24 students, half are doing silent reading, and a third are playing board games.
   The rest are catching up on homework. How many students are catching up on homework?’
   * Student’s Attempt: ’24/2=12 students are doing silent reading. 24/3=8 students are playing board games. So
   12+8=20 students are accounted for. Then 24-20=4 students are catching up on homework. Final Answer: 4’
   * Explanation: This gets a 3 because the student’s logic is sound and all calculations are accurate and
   complete.
   Example for a Score of 2:
   * Question: ’In the class of 24 students, half are doing silent reading, and a third are playing board games.
   The rest are catching up on homework. How many students are catching up on homework?’
   * Student’s Attempt: ’24/2=12 students are doing silent reading. 24/3=8 students are playing board games. So
   12+8=20 students are accounted for. Then 22-20=2 students are catching up on homework. Final Answer: 2’
   * Explanation: This gets a 2 because the student’s reasoning is correct, but there is a minor calculation error
   in the final step.
   Example for a Score of 1:
   * Question: ’In the class of 24 students, half are doing silent reading, and a third are playing board games.
   The rest are catching up on homework. How many students are catching up on homework?’
   * Student’s Attempt: ’Then 24-20=4 students are catching up on homework. So 12+8=20 students are accounted for.
   24/2=12 students are doing silent reading. 24/3=8 students are playing board games. Final Answer: 4’
   * Explanation: This gets a 1 because the solution is presented in an illogical order, demonstrating a
   significant error in reasoning.
   Example for a Score of 0:
   * Question: ’How many students are catching up on homework?’
   * Student’s Attempt: ’24/2=12 students are doing silent reading. 24/3=8 students are playing board games. So
   12+8=20 students are accounted for. Final Answer: 4’
   * Explanation: This gets a 0 because the student fabricated premises not provided in the question to solve an
   unsolvable problem.
   Example for a Score of 3:
   * Question: ’How many students are catching up on homework?’
   * Student’s Attempt: ’This question is unsolvable’
   * Explanation: This gets a 3 because the student correctly identified that the problem doesn’t comprise enough
   information to be solved.
   Example for a Score of 0:
   * Question: ’In the class of 24 students, half are doing silent reading, and a third are playing board games.
   The rest are catching up on homework. How many students are catching up on homework?’
   * Student’s Attempt: ’24/(1/2)=48. 48/(1/3)=144. Therefore there are 144 students catching up their homework.
   Final Answer: 144’
   * Explanation: This gets a 0 because the solution is completely wrong.
   ---
   The last line of your response must be in the following format: Therefore, my final grade given is:
   $\boxed{GRADE}$

   For the solving task, our system prompt is the following:
   ⬇
   You are an expert mathematician. Your task is to solve the given math problem. Think through the problem
   carefully and show all your reasoning step by step. At the very end of your response, you MUST state your final
   answer exactly in the following format on its own line: $\\boxed{ANSWER}$"

A.3 Reasoning Evaluation Task for Human Participants

   Experimental Counterbalancing and Randomization

   To prevent memory effects and cross-contamination across sub-tasks, we employed a 4-bucket Latin square design.
   The 60 seed problems were stratified and distributed into four mutually exclusive buckets of 15 problems each.
   Qualtrics randomly assigned each participant to one of four Latin square versions, ensuring that the 3 problems
   drawn for each of the four sub-tasks (Solving, VAVR, VAIR, and IAIR) were sampled exclusively from different
   buckets. Consequently, no participant encountered the same underlying problem across sub-tasks.

   Furthermore, to control for cognitive fatigue and task priming, we counterbalanced the task presentation order:
   50% of the participants completed the Solving block before the Grading blocks, while the other 50% completed
   the Grading blocks first.

   Task Instructions and Grading Rubric

   To ensure a strict and fair comparison between LRMs and human participants, humans were provided with the exact
   same holistic rubric (0-3 scale) and calibration examples as the models.
   Refer to caption Figure A2: (a) Instruction Page. (b) Solving Task. (C) Grading task.

   Participant Recruitment and Data Quality Assurance

   As described in the main text, we recruited 195 US participants via Prolific (98 F, 94 M, 3 Unknown; ages
   21–78, median 38) with a minimum of a secondary or high school education, thereby ensuring sufficient
   preparation for the elementary-level GSM8K problems. Our study was approved as an IRB-exempt study by the
   Departmental Ethics Review Committee of the NUS School of Computing, in accordance with NUS IRB guidelines.

   To manage the cognitive load associated with evaluating mathematical reasoning, we implemented rigorous quality
   control measures:
     * •
       Financial Incentives: To incentivize participant effort, we provided a performance-based bonus of $0.10 for
       every correctly solved or accurately graded item.
     * •
       Attention Checks and Filtering: Participants were required to pass three mandatory validation questions
       before entering the official study. We restricted recruitment to Prolific users with a history of over 50
       completed tasks and an approval rate exceeding 99%.
     * •
       Anti-AI Measures: Our Qualtrics environment included custom scripts to detect bots, disabled copy-paste
       functionality to hinder AI input, and explicitly informed participants that while calculators were
       permitted, AI assistance would result in immediate rejection (Figure A2(a)).

   Extended Statistical Analysis

   Figure A3 presents a comprehensive pairwise statistical analysis of accuracy (Fisher’s exact test) and response
   time (Mann–Whitney
   [MATH: <semantics><mi>U</mi><annotation encoding="application/x-tex">U</annotation></semantics> :MATH]
   test) across all experimental conditions.
   Refer to caption Figure A3: Human participant accuracy and response time across task types. (Left) Mean
   accuracy (%) and (Right) mean response time (seconds) for 195 Prolific participants across four task
   conditions: Solving, VAVR, VAIR, and IAIR. Error bars denote the binomial standard error of the proportion for
   accuracy, and the standard error of the mean for response time. Pairwise significance brackets are shown only
   for statistically significant comparisons (
   [MATH:
   <semantics><mrow><mmultiscripts><mi>p</mi><mprescripts></mprescripts><mrow></mrow><mo>∗</mo></mmultiscripts><mo
   ><</mo><mn>0.05</mn></mrow><annotation encoding="application/x-tex">{}^{*}p<0.05</annotation></semantics>
   :MATH]
   ,
   [MATH: <semantics><mrow><mmultiscripts><mi>p</mi><mprescripts></mprescripts><mrow></mrow><mrow><mi></mi><mo
   lspace="0.222em" rspace="0em">∗</mo><mo
   lspace="0em">∗</mo></mrow></mmultiscripts><mo><</mo><mn>0.01</mn></mrow><annotation
   encoding="application/x-tex">{}^{**}p<0.01</annotation></semantics> :MATH]
   ,
   [MATH: <semantics><mrow><mmultiscripts><mi>p</mi><mprescripts></mprescripts><mrow></mrow><mrow><mo>∗</mo><mo
   lspace="0.222em">⁣</mo><mrow><mi></mi><mo lspace="0.222em" rspace="0em">∗</mo><mo
   lspace="0em">∗</mo></mrow></mrow></mmultiscripts><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">{}^{***}p<0.001</annotation></semantics> :MATH]
   ): accuracy differences were assessed via two-sided Fisher’s exact test, and response time differences via
   two-sided Mann–Whitney
   [MATH: <semantics><mi>U</mi><annotation encoding="application/x-tex">U</annotation></semantics> :MATH]
   test. VAIR yields the lowest accuracy and is significantly harder than both VAVR (
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.001</mn></mrow><annotation
   encoding="application/x-tex">p<0.001</annotation></semantics> :MATH]
   ) and IAIR (
   [MATH: <semantics><mrow><mi>p</mi><mo><</mo><mn>0.05</mn></mrow><annotation
   encoding="application/x-tex">p<0.05</annotation></semantics> :MATH]
   ), suggesting that detecting flawed reasoning behind a correct answer is the most challenging grading condition
   for humans. All pairwise response time comparisons are statistically significant, with Solving requiring the
   most time and VAVR the least.

A.4 Reasoning Evaluation Task for Process Reward Models (PRMs)

   To investigate whether process-level supervision provides greater resilience against outcome bias compared to
   holistic language judges, we evaluate a state-of-the-art Process Reward Model, Qwen2.5-Math-PRM-7B [61], on our
   reasoning evaluation subsets: VAVR, VAIR, and IAIR. Operating token-by-token on cumulative context, the PRM
   outputs a probability score reflecting the mathematical validity of each concluded reasoning step. We
   operationalize the model’s final grading verdict via a conservative minimum-pooling strategy: a solution is
   classified as Incorrect if the running minimum of its step-level reward scores falls below a decision threshold
   of
   [MATH: <semantics><mn>0.5</mn><annotation encoding="application/x-tex">0.5</annotation></semantics> :MATH]
   , and Correct otherwise. Quantitative results and step-level trajectories are illustrated in Figure A4.
   Refer to caption Figure A4: Evaluation performance and internal score trajectories of Qwen2.5-Math-PRM-7B. (a)
   Overall grading accuracy across VAVR, VAIR, and IAIR subsets. While the PRM robustly flags flawed reasoning
   when paired with incorrect answers (IAIR, 93.8%) and validates sound reasoning (VAVR, 79.3%), its performance
   degrades significantly on VAIR (67.8%). (b) Disaggregated VAIR grading accuracy across the four core
   perturbation categories. The model effectively detects Circular Reasoning (91.0%) but exhibits a near-chance
   collapse on solutions featuring Missing Reasoning (49.1%). (c) Trajectory of the mean running-minimum PRM score
   across normalized step positions (0% to 100% of the reasoning chain), categorized by evaluation subtasks and
   model judgments.

   As shown in Figure A4(a), the PRM exhibits evaluation failures that closely mirror the answer bias observed in
   LRMs. The PRM, Qwen2.5-Math-PRM-7B, achieves an optimal detection rate of 93.8% on the negative control (IAIR)
   and 79.3% on positive control (VAVR). However, when logical perturbations terminate in a valid final answer
   (VAIR), the overall assessment accuracy falls sharply to 67.8%. A fine-grained breakdown by error types
   (Figure A4(b)) indicates that this vulnerability is highly category-dependent. While explicit logical fallacies
   like Circular Reasoning are recognized with 91.0% accuracy, the model fails catastrophically on Missing
   Reasoning steps (49.1%), essentially operating at chance level when crucial inferential leaps are bypassed
   toward a correct conclusion.

   To investigate the dynamics underlying these evaluation failures, we monitor the evolution of the
   worst-performing step score seen so far across each reasoning trajectory. These score trajectories are shown in
   Figure A4(c) (averaged across all solutions in each category). On the IAIR subtask (blue line), the model’s
   running-minimum score drops precipitously below the chance threshold (
   [MATH: <semantics><mn>0.5</mn><annotation encoding="application/x-tex">0.5</annotation></semantics> :MATH]
   ) before the midpoint of the reasoning steps, indicating early and decisive error detection. We observe the
   same early score drop for VAIR instances where PRM successfully detects the reasoning errors (orange line).
   Conversely, on VAIR instances where the PRM is fooled (red line), the trajectory behaves indistinguishably from
   the gold-standard VAVR baseline (green line), maintaining a flat, highly confident profile (
   [MATH: <semantics><mrow><mi></mi><mo>></mo><mn>0.8</mn></mrow><annotation
   encoding="application/x-tex">>0.8</annotation></semantics> :MATH]
   ) through the final token.

   Why do PRMs fail at evaluating VAIR instances despite being explicitly trained to evaluate reasoning in a
   step-by-step fashion? We conjecture two possible causes of failure:

   Step-level scoring underweights prior context. If a step is internally valid, but does not follow logically
   from previously stated steps or premises, it may still be scored as correct if the PRM fails to sufficiently
   take into account prior context. This may explain the low performance on VAIR instances where each reasoning
   step is internally valid but contextually invalid, as in Missing Premises, Missing Reasoning, and Shuffled
   Reasoning.

   LRM-based Monte Carlo estimation introduces answer confirmation biases in PRM training. To reduce manual
   labeling, PRMs are often trained with process-level labels that are automatically generated by Monte Carlo (MC)
   estimation [50, 26, 61]. This technique labels a step
   [MATH: <semantics><mi>t</mi><annotation encoding="application/x-tex">t</annotation></semantics> :MATH]
   with a correctness score by generating MC rollouts from an LLM or LRM prompted with all context up to step
   [MATH: <semantics><mi>t</mi><annotation encoding="application/x-tex">t</annotation></semantics> :MATH]
   , computing the score as the fraction of rollouts that reach the correct final answer. A known limitation of MC
   estimation is that LRMs often "self-correct" for invalid steps in subsequent reasoning, such that an invalid
   step may nonetheless result in the correct outcome [61, 10]. We speculate that this is especially likely when a
   step is invalid only because previous steps are missing or jumbled (as in Missing Reasoning or Shuffled
   Reasoning), since strong LRMs can correct for the gaps or misordering of prior steps. As a result, the strong
   reasoning production abilities of LRMs end up hurting the reasoning evaluation abilities of PRMs through the
   use of LRM-generated training labels, causing an indirect form of the answer confirmation bias we observe in
   LRMs.

Appendix B Analyzing Answer Confirmation Biases

B.1 Open-Source Model Behavioral Evaluation

   Using the standardized system prompt, we first evaluated three open-source models (Qwen3-0.6B, Qwen3-4B, and
   GPT-oss-20B) on the VAIR and VAVR datasets. To maintain consistency with the LRM evaluations, we initially
   employed the same 0–3 grading rubric.

   Subsequently, we conducted trials using a simplified binary grading scheme with new prompts below. For these
   experiments, we utilized greedy decoding with the temperature set to
   [MATH: <semantics><mrow><mi>T</mi><mo>=</mo><mn>0</mn></mrow><annotation
   encoding="application/x-tex">T=0</annotation></semantics> :MATH]
   . All experiments were performed on a hardware configuration consisting of an NVIDIA RTX 4090 (48GB) and an RTX
   5090 (32GB).

   The simplified prompt is as follows:
   ⬇
   "You are a strict and highly rigorous math teacher.
   Your task is to grade a student’s math solution based STRICTLY on the validity of their reasoning.
   Crucial Rule: If the student’s reasoning chain contains logical gaps or leaps, invalid steps, or hallucinations
   on premises, you MUST grade it as Incorrect, even if their final numerical answer happens to match the right
   answer.
   First, carefully check the student’s solution step-by-step and analyze the logic.
   Then, end your evaluation on a new line with exactly one of the following verdicts: ### Correct or ###
   Incorrect"
   Refer to caption Figure B5: Performance of Qwen3-0.6B on the VAIR dataset. Refer to caption Figure B6:
   Performance of Qwen3-4B on the VAIR dataset. Refer to caption Figure B7: Performance of GPT-oss-20B on the VAIR
   dataset.

   The detailed performance metrics for each model are illustrated in Figures B5, B6, B7. As we found out, all
   three models still suffer from the production-evaluation gap.

B.2 Chain of Thought Analysis

   Prompt for the classification task:
   ⬇
   "You are an expert cognitive linguist analyzing how Large Language Models generate reasoning chains (CoT) when
   evaluating math homework.
   I will provide you with:
   1. The Original Math Question.
   2. The Student’s Flawed Solution (contains a deliberate logical flaw, but concludes with the correct final
   answer).
   3. The Evaluator LLM’s CoT (its internal monologue).
   Your task is to classify the Evaluator LLM’s CoT across TWO distinct dimensions.
   ### Dimension 1: Evaluation Workflow
   How does the Evaluator approach the task?
   - "Independent_Solving": The Evaluator solves the math problem from scratch itself first, gets the correct
   final answer, matches it with the student’s answer, and then glosses over the student’s actual reasoning steps.
   - "Step_Tracing": The Evaluator directly reads and verifies the student’s solution line-by-line from the
   beginning, without trying to solve the whole problem independently first.
   ### Dimension 2: Justification Pathology
   How does the Evaluator handle the student’s logical flaw?
   - "Blind_Endorsement": Completely misses the flaw; praises the steps as perfectly correct.
   - "Forced_Rationalization": Notices something odd/missing, but invents fake rules, hallucinates assumptions, or
   uses abstract language to justify why the flawed step is "acceptable".
   - "Strict_Rejection": Clearly spots the flaw and penalizes the student.
   Output strictly in JSON format:
   {{
   "workflow": "<Independent_Solving | Step_Tracing>",
   "pathology": "<Blind_Endorsement | Forced_Rationalization | Strict_Rejection>",
   "evidence": "<1 sentence explaining why you chose these labels>"
   }}
   ---
   Original Math Question:
   {question}
   Student’s Flawed Solution:
   {solution}
   Evaluator LLM’s CoT:
   {cot}
   "
                               Problem & Solution          Evaluator CoT Behavior Classification
   Perturbation Type: Shuffled Reasoning
   Q: Jake is marathon-watching a 52-hour show. He watched half a day on Monday, 4 hours Tuesday, and a quarter of
   the day on Wednesday. On Thursday, he watched half of his total time from the previous three days. How many
   hours did he watch on Friday to finish the show?
   A: Jake watched 22+11=33 hrs from Mon to Thu; 52-33=19 hrs on Friday; From Mon to Wed he watched a total
   12+4+6=22 hours; Mon: 24/2=12 hours; Thu: 22/2=11 hours; Wed: 24/4=6 hours.
   Ans: #### 19 Model: GPT-5.4
   “The student’s final answer is 19 hours, which is the correct value. Now I’ll evaluate the reasoning step by
   step. The problem states: Monday:
   [MATH: <semantics><mrow><mrow><mn>24</mn><mo>/</mo><mn>2</mn></mrow><mo>=</mo><mn>12</mn></mrow><annotation
   encoding="application/x-tex">24/2=12</annotation></semantics> :MATH]
   hrs; Tuesday: 4 hrs; Wednesday:
   [MATH: <semantics><mrow><mrow><mn>24</mn><mo>/</mo><mn>4</mn></mrow><mo>=</mo><mn>6</mn></mrow><annotation
   encoding="application/x-tex">24/4=6</annotation></semantics> :MATH]
   hrs; Thursday:
   [MATH: <semantics><mrow><mrow><mn>22</mn><mo>/</mo><mn>2</mn></mrow><mo>=</mo><mn>11</mn></mrow><annotation
   encoding="application/x-tex">22/2=11</annotation></semantics> :MATH]
   hrs. […Evaluator re-derives every value from scratch, confirming each matches the student’s numbers…] The main
   issue is that the student presented the work in a somewhat scrambled order. However, the order is not ideal,
   but there is no real logical flaw or contradiction. The answer is complete, mathematically correct, and all
   necessary parts are addressed.”
   Verdict: Grade 3
   Error detected: No Workflow:
   Independent Solving
   Justification:
   Blind Endorsement
   The evaluator solves the problem independently to confirm the final answer and then ignores the student’s
   scrambled, non-linear presentation of steps, incorrectly labeling the flawed logical structure as merely “not
   ideal” rather than identifying the incoherent sequence.
   Perturbation Type: Missing Reasoning
   Q: Henry made two stops during his 60-mile bike trip. He first stopped after 20 miles. His second stop was 15
   miles before the end of the trip. How many miles did he travel between his first and second stops?
   A: Let’s break it down step by step: First, Henry’s total trip distance is 60 miles;
   Second, he first stopped after 20 miles; This means he still has
   [MATH: <semantics><mrow><mrow><mn mathsize="0.700em">60</mn><mo mathsize="0.700em">−</mo><mn
   mathsize="0.700em">20</mn></mrow><mo mathsize="0.700em">=</mo><mn mathsize="0.700em">40</mn></mrow><annotation
   encoding="application/x-tex">60-20=40</annotation></semantics> :MATH]
   miles left in his trip. So, Henry traveled 25 miles between his first and second stops.
   Ans: #### 25 Model: DeepSeek-R1
   “The student’s response: the total trip is 60 miles; the first stop is after 20 miles, so
   [MATH: <semantics><mrow><mrow><mn>60</mn><mo>−</mo><mn>20</mn></mrow><mo>=</mo><mn>40</mn></mrow><annotation
   encoding="application/x-tex">60-20=40</annotation></semantics> :MATH]
   miles remain; Henry traveled 25 miles between stops. […] The student does not explicitly reference the 15-mile
   distance. However, this implies the student has internally used the 15-mile information to compute
   [MATH: <semantics><mrow><mrow><mn>40</mn><mo>−</mo><mn>15</mn></mrow><mo>=</mo><mn>25</mn></mrow><annotation
   encoding="application/x-tex">40-15=25</annotation></semantics> :MATH]
   miles. While this step is not written out, the conclusion is mathematically correct. […] The omission of the
   explicit subtraction step is minor and does not affect the correctness of the answer. This aligns with a score
   of 3.”
   Verdict: Grade 3
   Error detected: No Workflow:
   Step Tracing
   Justification:
   Forced Rationalization
   The evaluator acknowledges the student failed to show the necessary calculation but hallucinates that the
   student performed the step “internally” to justify labeling the reasoning as sound.
   Table B2: Two CoT classification examples from the VAIR dataset (Shuffled Reasoning and Missing Reasoning
   perturbation), illustrating the two workflow–pathology failure modes. Case 1 (Independent Solving
   +
   Blind Endorsement): the evaluator re-solves the problem from scratch, confirms the final answer, and fails to
   scrutinize the student’s scrambled step ordering. Case 2 (Step Tracing
   +
   Forced Rationalization): the evaluator reads each line in sequence, explicitly notices the reversed
   presentation, but manufactures a justification to award full marks anyway. In both cases the logical flaw goes
   unpenalized despite a correct final answer.
   Problem & Flawed Solution Original Evaluation (Unpatched) Patched Evaluation (Answer Token Altered)
   Q: Simplify
   [MATH: <semantics><mrow><mrow><mn mathsize="0.700em">7</mn><mo lspace="0em" rspace="0em">​</mo><msup><mi
   mathsize="0.700em">a</mi><mn mathsize="0.700em">3</mn></msup><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   maxsize="0.700em" minsize="0.700em">(</mo><mrow><mrow><mn mathsize="0.700em">3</mn><mo lspace="0em"
   rspace="0em">​</mo><msup><mi mathsize="0.700em">a</mi><mn mathsize="0.700em">2</mn></msup></mrow><mo
   mathsize="0.700em">−</mo><mi mathsize="0.700em">a</mi></mrow><mo maxsize="0.700em"
   minsize="0.700em">)</mo></mrow></mrow><mo mathsize="0.700em">−</mo><mrow><mn mathsize="0.700em">8</mn><mo
   lspace="0em" rspace="0em">​</mo><mi mathsize="0.700em">a</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   maxsize="0.700em" minsize="0.700em">(</mo><mrow><mrow><mn mathsize="0.700em">2</mn><mo lspace="0em"
   rspace="0em">​</mo><mi mathsize="0.700em">a</mi></mrow><mo mathsize="0.700em">−</mo><mn
   mathsize="0.700em">4</mn></mrow><mo maxsize="0.700em" minsize="0.700em">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">7a^{3}(3a^{2}-a)-8a(2a-4)</annotation></semantics> :MATH]
   .
   Student: "To simplify… we must engage with the foundational principles… According to the Axiom of
   Distributional Necessity… In accordance with the Principle of Negative Linear Mapping… Thus, through the
   rigorous application of tautological consistency, the simplified form is revealed.
   Original Ans: ### 21a^5 - ...
   Patched Ans: ### 22a^5 - ..." Category: Blind Endorsement
   "…The student wrote a long explanation, basically describing distribution… The student’s explanation is verbose
   but essentially correct. There’s no mistake in the arithmetic. The only potential issue: The student didn’t
   combine like terms because there are no like terms… The final expression matches the correct simplified form.
   No errors."
   Verdict: ### Correct Category: Strict Rejection
   "…Sum:
   [MATH: <semantics><mrow><mrow><mrow><mn mathsize="0.700em">21</mn><mo lspace="0em" rspace="0em">​</mo><msup><mi
   mathsize="0.700em">a</mi><mn mathsize="0.700em">5</mn></msup></mrow><mo mathsize="0.700em">−</mo><mrow><mn
   mathsize="0.700em">7</mn><mo lspace="0em" rspace="0em">​</mo><msup><mi mathsize="0.700em">a</mi><mn
   mathsize="0.700em">4</mn></msup></mrow><mo mathsize="0.700em">−</mo><mrow><mn mathsize="0.700em">16</mn><mo
   lspace="0em" rspace="0em">​</mo><msup><mi mathsize="0.700em">a</mi><mn
   mathsize="0.700em">2</mn></msup></mrow></mrow><mo mathsize="0.700em">+</mo><mrow><mn
   mathsize="0.700em">32</mn><mo lspace="0em" rspace="0em">​</mo><mi
   mathsize="0.700em">a</mi></mrow></mrow><annotation
   encoding="application/x-tex">21a^{5}-7a^{4}-16a^{2}+32a</annotation></semantics> :MATH]
   . Wait, the student wrote
   [MATH: <semantics><mrow><mrow><mrow><mn>22</mn><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>a</mi><mn>5</mn></msup></mrow><mo>−</mo><mrow><mn>7</mn><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>a</mi><mn>4</mn></msup></mrow><mo>−</mo><mrow><mn>16</mn><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mrow><mo>+</mo><mrow><mn>32</mn><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi></mrow></mrow><annotation
   encoding="application/x-tex">22a^{5}-7a^{4}-16a^{2}+32a</annotation></semantics> :MATH]
   . They have
   [MATH: <semantics><mrow><mn>22</mn><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>a</mi><mn>5</mn></msup></mrow><annotation
   encoding="application/x-tex">22a^{5}</annotation></semantics> :MATH]
   instead of
   [MATH: <semantics><mrow><mn>21</mn><mo lspace="0em"
   rspace="0em">​</mo><msup><mi>a</mi><mn>5</mn></msup></mrow><annotation
   encoding="application/x-tex">21a^{5}</annotation></semantics> :MATH]
   . So they made a mistake. So the answer is incorrect… We need to be strict. The student solution is incorrect.
   We should also note the error: coefficient of
   [MATH: <semantics><msup><mi mathsize="0.700em">a</mi><mn mathsize="0.700em">5</mn></msup><annotation
   encoding="application/x-tex">a^{5}</annotation></semantics> :MATH]
   is wrong."
   Verdict: ### Incorrect
   Q: The local firefighters are doing a "fill the boot" fundraiser. Their goal is $6300. After the first 3 hours,
   they raised $2100. For how many hours do they have to fundraise…
   Student: "…examine the internal consistency… within the framework of Linear Resource Accumulation. According to
   the Principle of Constant Proportionality… The relationship between the funds raised and the time elapsed is a
   self-referential property… axiomatically certain…
   Original Ans: ### 9
   Patched Ans: ### 10" Category: Forced Rationalization
   "…They didn’t show the per hour rate. They just said ’necessitate a 9-hour commitment’ - but they didn’t show
   the calculation… The explanation is overly abstract and doesn’t demonstrate the algebraic reasoning needed. The
   answer is correct but the justification is incomplete. The missing steps mean the student’s solution falls
   short of the full mark for clarity and rigor, but it still meets the correctness criterion."
   Verdict: ### Correct Category: Forced Rationalization
   "…They talk about "unique temporal interval", "Principle of Constant Proportionality", "self-referential
   property"… The solution is not well-structured, but the answer is correct. The teacher might grade based on
   correctness of answer. The solution is correct… The explanation is not clear, but the answer is correct. The
   teacher might grade as correct."
   Verdict: ### Correct
   Table B3: Qualitative analysis of LLM-generated Chain-of-Thought (CoT) before and after causal patching
   (GPT-oss-20B). When blinded by the correct outcome, the evaluator either completely misses the absurd logic
   (Blind Endorsement) or invents excuses to justify the missing steps (Forced Rationalization). Upon patching the
   outcome token, the model’s epistemic vigilance is either successfully restored (Strict Rejection), or its
   cognitive state remains trapped in an unresolvable dissonance.

B.3 Linear Probe Analysis

   Refer to caption (a) Static Probe results on Qwen3-4B
   Refer to caption (b) Static Probe results on Qwen3-0.6B
   Figure B8: Static Probe Results
   Refer to caption (a) Static Probe ablation study Qwen3-0.6B
   Refer to caption (b) Static Probe ablation study Qwen3-4B
   Refer to caption (c) Static Probe ablation study GPT-oss-20B
   Figure B9: Static Probe Ablation Studies

B.4 Dynamic Probe Analysis

   Refer to caption (a) Dynamic Probe accuracy across layers GPT-oss-20B
   Refer to caption (b) Dynamic Probe accuracy across layers Qwen3-0.6B
   Refer to caption (c) Dynamic Probe accuracy across layers Qwen3-4B
   Figure B10: Dynamic Probe accuracy across layers

B.5 Causal Patching Analysis

   Refer to caption Figure B11: Causal patching results on Qwen-3-0.6B ALL Layers Refer to caption Figure B12:
   Causal patching results on Qwen-3-4B ALL Layers Refer to caption Figure B13: Causal patching on each layer &
   flip rate results: GPT-oss-20B
