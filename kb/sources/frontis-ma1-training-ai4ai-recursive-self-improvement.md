---
source: https://arxiv.org/abs/2607.28568
description: "Open full-stack MLE system aligns execution-grounded post-training with four program-evolution operators and long-horizon evolutionary search"
captured: 2026-08-02
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Frontis-MA1: Training an AI4AI Model toward Recursive Self-Improvement in MLE

Author: Junlin Yang, Che Jiang, Yu Fu, Tianwei Luo, Can Ren, Weizhi Wang, Kaikai Zhao, Hongyi Liu, Yuxin Zuo, Yuru Wang, Yuchen Fan, Kai Tian, Zhenzhao Yuan, Xiaojian Lin, Li Sheng, Rushi Qiang, Guoli Jia, Xingtai Lv, Ermo Hua, Dianqiao Lei, Youbang Sun, Ning Ding, Bowen Zhou, Kaiyan Zhang
Source: https://arxiv.org/abs/2607.28568
Date: 30 July 2026

Snapshot note: Captured from the arXiv PDF. The paper text, section order, tables, and figure captions are preserved as recoverable from layout-aware PDF extraction; multi-column figures and mathematical layout may be simplified.

                                       Frontis-MA1: Training an AI4AI Model towards Recursive
                                          Self-Improvement in Machine Learning Engineering
                                                                                        Horizon Research, Frontis.AI                                                             Tsinghua University
                                                                                                        Project                         § GitHub                                       HuggingFace

                                          Abstract | Recursive self-improvement (RSI) requires AI systems that improve the process of
                                          building AI (i.e., AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed
                                          for studying this capability. We introduce OpenMLE, an open full-stack system for RSI research in
                                          MLE, spanning verifiable task environments with execution feedback (OpenMLE-Gym), operator
                                          learning (OpenMLE-ERL), and long-horizon search (OpenMLE-Evo). On this stack we post-
                                          train Frontis-MA1-35B as a meta-evolution agent for MLE, aligning post-training and inference
arXiv:2607.28568v1 [cs.CL] 30 Jul 2026

                                          around four atomic program-evolution operators (Draft, Improve, Debug, Crossover): the same
                                          operators are trained via execution-grounded SFT and RL on data deduplicated against all evaluation
                                          benchmarks, then composed into long-horizon search, coupling learning and evolution in a single
                                          loop. On MLE-Bench Lite under a 12-hour per-task budget on one RTX 4090 capped at 12 GB
                                          VRAM, Frontis-MA1-35B improves Medal Average from 39.39% to 60.61% over its base model
                                          with OpenMLE-Evo, and reaches 71.21% with OpenMLE-Evo-Max (benchmark-independent
                                          experience priors and asynchronous search), exceeding GPT-5.5 + Codex and approaching GPT-5.6
                                          Sol and the 2.8T Kimi K3. On held-out NatureBench Lite, both components transfer: with the
                                          framework fixed, swapping in the trained model raises Match-SOTA from 50% to 70%; with the
                                          model fixed, swapping in OpenMLE-Evo raises it from 20% to 50%. We release the model weights
                                          and the full OpenMLE stack to enable reproducible research on executable AI4AI toward RSI.

                                          Project Leaders | Junlin Yang, Che Jiang
                                          Correspondence | Kaiyan Zhang, zhangkaiyan@frontis.cn

                                                                    Frontis · Evo               Other models · Evo                     OpenMLE-Evo-Max                             General: Codex / Claude Code / Gemini CLI

                                             All models · all harness results                                                                                                                   Model size × score
                                             Medal avg@3 (%)                                                                                                                                        Medal avg@3 (%)
                                        80                                                                                                                                                     80
                                              72.7 72.7
                                                          71.2
                                        70                       68.2
                                                                        66.7 66.7
                                                                                    65.2 65.2
                                                                                                63.6 63.6
                                                                                                            59.1
                                        60                                                                         56.1 56.1                                                                   60
                                                                                                                               54.5 54.5 54.5
                                                                                                                                                51.5 51.5
                                                                                                                                                            50.0
                                                                                                                                                                   40.9
                                                                                                                                                                          39.4
                                        40                                                                                                                                                     40
                                                                                                                                                                                 34.9

                                        30                                                                                                                                              27.3

                                        20                                                                                                                                                     20
                                                                                                                                                                                                     30B      100B                1T            10T
                                                                                                                                                                                                               Total parameters (log scale)
                                                 35B MA1

                                                             lus

                                                            2.7

                                                             5B
                                                         2.1P

                                                Thin -30B
                                                              h
                                                         t-2.0
                                                           Sol

                                                           .5F

                                                         2.5P
                                                          4.6
                                                         Pro

                                                        Flas

                                                            F
                                                        xM
                                                           .6

                                                     s 4.8

                                                       -5.2

                                                       -4.7
                                                     k-4.5

                                                      .7 P

                                                       .6-3
                                                      -5.5
                                                      i K3

                                                      xM

                                                   p-3.7
                                                    i K2

                                                   ini 3

                                                     net

                                                        k.
                                                         -
                                                   -5.6

                                                  gCa
                                                  ntis

                                                   net

                                                  en3
                                                   oV
                                                  iMa

                                                 bao

                                                   V4
                                               GLM

                                               GLM
                                               GPT

                                                iMa

                                                en3
                                                en3

                                                 V4
                                                Kim

                                               Opu

                                               Son
                                               Gro
                                               Kim

                                             Gem

                                               Ste
                                              Son
                                             GPT

                                              DS-

                                             MiM

                                              Qw
                                              Min

                                             Lon
                                              Fro

                                             Dou

                                             DS-

                                             Min

                                             Qw
                                             Qw

                                       Figure 1 | Results on MLE-Bench Lite. Bars show all completed harness results; the Pareto panel
                                       retains each model’s best harness. Colors and hatching follow the shared model–harness legend.

                                       © 2026 FRONTIS. All rights reserved

Contents

1 Introduction                                                                                      4

2 Problem Formulation                                                                               6

3 OpenMLE-Gym: Building Scalable Verifiable Environments                                            7
3.1 Environment Contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        7
3.2 Scalable Task Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      8
3.3 Task Quality Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    9
3.4 Sandbox Execution at Scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        9
3.5 Composition and Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

4 OpenMLE-ERL: Reinforcing Reusable Evolutionary Operators                                         10
4.1 Trainable Atomic Operators for Evolutionary Inference . . . . . . . . . . . . . . . 12
4.2 Execution-Grounded Supervised Warm Start . . . . . . . . . . . . . . . . . . . . . 12
4.3 Execution-Grounded Reinforcement Learning . . . . . . . . . . . . . . . . . . . . 12

5 OpenMLE-Evo: Scaling Experience-driven Long-Horizon Search                                       15
5.1 Structured Experience Accumulation . . . . . . . . . . . . . . . . . . . . . . . . . 15
5.2 Experience-Guided Parent Selection . . . . . . . . . . . . . . . . . . . . . . . . . . 16
5.3 Operation-Triggered Memory Synthesis . . . . . . . . . . . . . . . . . . . . . . . . 17
5.4 Operator-Conditioned Context Construction . . . . . . . . . . . . . . . . . . . . . 17

6 Experiments                                                                                      17
6.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.2 Training and Search Gains Compose . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.3 Long-Horizon Self-Improvement . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
6.4 Solution Ceiling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
6.5 Search Efficiency and Mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
6.6 Meta-Ability and Transfer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

7 Related Work                                                                                     29

8 Limitations and Future Work                                                                      30

9 Conclusion                                                                                       31

10 Authors                                                                                         32

A OpenMLE-Gym Details                                                                             39
 A.1 Task Construction and Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
 A.2 OpenMLE-Gym Execution Infrastructure . . . . . . . . . . . . . . . . . . . . . . . 40

B OpenMLE-ERL Details                                                                             43
 B.1 SFT Data Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
 B.2 SFT Training Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
 B.3 RL Training Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
 B.4 Asynchronous Rollout      . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
 B.5 Reward Normalization and Entropic Advantage . . . . . . . . . . . . . . . . . . . 49
 B.6 Detection and prevention of reward hacking. . . . . . . . . . . . . . . . . . . . . . 50

C OpenMLE-Evo Inference Details                                                                   50
 C.1 Evolutionary Parent Fitness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
 C.2 Operator Prompt Templates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
 C.3 Structured Experience Records . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
 C.4 Experience-Guided Parent Selection . . . . . . . . . . . . . . . . . . . . . . . . . . 56
 C.5 Operation-Triggered Memory Synthesis . . . . . . . . . . . . . . . . . . . . . . . . 57

D Supplementary Experiments                                                                       59
 D.1 Repeated-Evaluation Statistics on MLE-Bench Lite . . . . . . . . . . . . . . . . . . 59
 D.2 NatureBench Lite Task Composition . . . . . . . . . . . . . . . . . . . . . . . . . . 59

E Simplified comparison of public release surfaces                                                60

## 1 Introduction

AI capability growth is no longer pushed only by human engineers. Increasingly, AI systems write
code, run experiments, search over designs, and help build the next generation of AI systems [Lu
et al., 2024, Novikov et al., 2025, Oh et al., 2025, Romera-Paredes et al., 2024]. This broader
direction, often called AI for AI (AI4AI), seeks to use AI systems to build and improve AI [Chan
et al., 2026, Liu et al., 2025a]. Its more ambitious endpoint is recursive self-improvement (RSI),
where each improved system further improves the process that produces its successors [Eth
and Davidson, 2025, Favaro and Clark, 2026, Good, 1965, Schmidhuber, 2003]. Reaching that
endpoint requires more than stronger one-shot generation or planning. It requires agents that can
perform AI training AI and AutoResearch: inspect data, propose algorithms, execute experiments,
diagnose failures, and decide how to spend the next unit of compute [Karpathy, 2026, Lu et al.,
2024, Nathani et al., 2025].
Machine learning engineering (MLE) is a particularly direct instantiation of AI4AI: an agent
must build a machine learning solution for a real-world task and iteratively improve it through
execution feedback [Chan et al., 2024, Huang et al., 2023, Qiang et al., 2025a]. A trajectory
often begins with a valid pipeline and advances through repeated experiments toward a solution
competitive with strong human or frontier-model pipelines [Du et al., 2026, Hambardzumyan
et al., 2026, Nam et al., 2025]. Each iteration consumes time and compute, and its outcome
may arrive only after minutes or hours. This makes MLE a concrete and demanding testbed for
studying how agents improve AI systems under delayed, noisy, and heterogeneous feedback [Jing
et al., 2024, Lupidi et al., 2026, Nathani et al., 2025].

                                                                                                   MECHANISM HIERARCHY
  AI4AI       Iterative improvement via execution feedback

        ML                    DL                      LLM                 Agent
  features / models    network / training    pretrain / align         planning / tools
       AutoML                NAS            RLAIF / self-play        workflow / harness

                                                                                                         Recursive
                                                                                                     Self-Improvement
  Benchmarks - evaluation layer                                                    ML / DL
                                                                                                         RSI · limiting goal
   ML                                            DL
   MLE-Bench Lite                                NatureBench Lite
   Machine Learning Engineering                  Scientific AutoResearch
                                                                                             Evolution             variation + selection
                                                      evaluated on
                            Frontis-MA1                                this work                         Meta-Evolution
                            Meta-Evolution Agent                                                    the improver is trained
                            trained on verified trajectories
                                                      execution feedback

  OpenMLE - open full-stack infrastructure                        supporting foundation
                                                                                                         Self-Evolution
   OpenMLE-Gym                 OpenMLE-ERL                     OpenMLE-Evo                          experience flows back
   tasks + feedback            train operators                 long-horizon search
   environment layer           learning layer                  search layer

   released in this work      benchmark / external              learning / feedback path

Figure 2 | Positioning of this work. Left: within AI4AI, machine learning engineering (MLE) is
our task domain; the OpenMLE stack trains and deploys Frontis-MA1, which is both the product
of the stack and its engine, evaluated only on third-party benchmarks. Right: the mechanism
ladder from evolution to recursive self-improvement; the meta-evolutionary loop (orange) places
this work at the level where the improver itself is trained—the level after which Frontis-MA1
(Meta-evolution Agent) is named.

Prior work advances MLE agents along three complementary but overlapping strands. The first
develops inference-time harnesses based on structured or evolutionary search [Du et al., 2025,
Fang et al., 2025, InternScience, 2026, Jiang et al., 2025, Liu et al., 2025a, Nam et al., 2025, Toledo
et al., 2025, Zhu et al., 2026b]. The second builds executable tasks and environments [Lupidi
et al., 2026, Nathani et al., 2025, Qiang et al., 2025a,b]. The third uses execution feedback to
post-train MLE agents [Cai et al., 2026, Li et al., 2025b, Liu et al., 2025b, Yang et al., 2025a].
Some systems bridge subsets of these strands—MLE-Dojo supports model tuning, while AceGRPO
recycles iterative execution traces into training [Cai et al., 2026, Qiang et al., 2025a]—but, among
the representative public systems audited in Appendix Table 11, none jointly spans scalable task
and environment construction, execution-grounded agent post-training, and an evolutionary
harness that deploys the trained agent in long-horizon search, together with the artifacts needed
to reproduce the full loop.
We introduce OpenMLE, an open full-stack technical solution for training language models
to construct and iteratively improve machine learning solutions using executable feedback:
OpenMLE-Gym constructs 5,758 quality-gated executable tasks and provides isolated execu-
tion, structured feedback, and task-specific evaluation; OpenMLE-ERL uses budget-adaptive
supervision fine-tuning and reinforcement learning to turn verified solutions and revisions into
stronger MLE behavior; and OpenMLE-Evo organizes long-horizon search around structured
experience, non-greedy selection over quality, progress, and novelty, and operator-conditioned
memory. OpenMLE exposes Draft, Improve, Debug, and Crossover as a shared interface
between post-training and inference. This interface lets verified evolutionary transitions supervise
the same transformations that search later composes, making the trained model the variation
engine of the evolutionary harness and forming the meta-evolutionary loop illustrated in Fig-
ure 2, in which the improver itself is trained. A model trained and deployed in this role is a
meta-evolution agent as introduced in [Jiang et al., 2026].
Using OpenMLE, we train Frontis-MA1-35B (Meta-evolution Agent, generation 1) as our primary
model and evaluate it at the model, harness, and system levels on MLE-Bench Lite under a fixed
12 GPU-hour per-task budget. At the model level, under the identical OpenMLE-Evo harness,
Frontis-MA1-35B improves over Qwen3.6-35B-A3B from 39.39% to 60.61% Medal Average and
from 0.5828 to 0.7647 Human Rank. At the harness level, matched comparisons show that
OpenMLE-Evo outperforms general-purpose Claude Code or Codex scaffolds across four frontier
models and original AIRA-Evo on Frontis-MA1-35B. At the system level, Frontis-MA1-35B with
OpenMLE-Evo-Max1 reaches 71.21% Medal Average and 0.8126 Human Rank, exceeding
GPT-5.5 + Codex. As a controlled cross-model replication, Frontis-MA1-30B improves over
Qwen3-30B-A3B-Thinking-2507 from 34.85% to 53.03% under the same OpenMLE-Evo harness.
Finally, controlled NatureBench [Wang et al., 2026] Lite comparisons provide evidence that both
execution-grounded post-training and adapted evolutionary search transfer beyond competition-
style MLE. We will release the datasets, training and evaluation code, sandbox infrastructure,
harness code, and final post-trained checkpoints. This release will make the complete OpenMLE
workflow reproducible, enabling broader study of meta-evolution in executable AI4AI settings
and its role on the path toward RSI. Our contributions are:
1. We present OpenMLE as a full-stack technical solution for studying recursive self-improvement
 in executable MLE, connecting verifiable environments, post-training, and test-time evolution
 in one validated workflow.
2. We introduce OpenMLE-Gym, which unifies 5,758 challenging tasks with isolated execution,
 structured feedback, and task-specific evaluators for scalable training, search, and evaluation.
3. We introduce OpenMLE-ERL to train reusable Draft, Improve, Debug, and Crossover
 operators through execution-grounded supervised fine-tuning and reinforcement learning.
1 OpenMLE-Evo-Max is an enhanced OpenMLE configuration; see Section 6.1 for details.

4. We introduce OpenMLE-Evo to support experience-guided long-horizon search over the
 environments and feedback exposed by OpenMLE-Gym.
5. Using the complete stack, we train and release Frontis-MA1-35B as our primary model, to-
 gether with Frontis-MA1-30B as a companion model for controlled cross-model replication.
 Evaluations separate the gains from post-training and search on MLE-Bench Lite and provide
 transfer evidence on NatureBench Lite. We also release the datasets, training and evalua-
 tion code, execution infrastructure, and search framework needed to reproduce and extend
 OpenMLE.

## 2 Problem Formulation

From AI for AI to meta-evolution. AI for AI describes the object of optimization: AI systems
participate in creating or improving other AI systems, including training code, model architectures,
algorithms, agent harnesses, and AI hardware. Evolution describes the optimization process: an AI
repeatedly modifies a candidate system according to feedback from its execution. Meta-evolution
closes an additional learning loop by reusing these evolutionary trajectories to train the model
that proposes future modifications. Recursive self-improvement (RSI) requires a stronger and
sustained loop in which each upgraded system further improves the process that produces its
successors. OpenMLE studies a concrete step from evolution toward meta-evolution: executable
search experience is reused through supervised fine-tuning and reinforcement learning to improve
the program-transformation model.
Executable evolution for AI-building tasks. We use machine learning engineering (MLE) as
a measurable testbed for this process. Following MLE-Dojo and MLE-Bench [Chan et al., 2024,
Qiang et al., 2025a], each task 𝜏 contains a natural-language specification, visible data assets, a
submission contract, a task-specific evaluator, and a sandboxed execution environment. At step 𝑡 ,
the inference-time search algorithm selects an operator 𝑎𝑡 and constructs its operator context 𝑐𝑡
from zero or more parent programs and their execution feedback. The model then proposes

                            𝑝𝑡 ∼ 𝑔𝜃 (· | 𝜏, 𝑎𝑡 , 𝑐𝑡 ) ,         𝑠𝑡 = 𝑅𝜏 (E ( 𝑝𝑡 , 𝜏)) .

Here, 𝑔𝜃 denotes the operator-conditioned program-generation policy parameterized by the
language-model parameters 𝜃. Given task 𝜏, operator 𝑎𝑡 , and context 𝑐𝑡 , it defines a distribution
over candidate programs. The sandbox E executes 𝑝𝑡 and returns the task score 𝑠𝑡 mapped by a
task-specific evaluator 𝑅𝜏 together with status, logs, artifacts, and runtime metadata. Because
task metrics have different ranges and directions, Section 4.3 converts 𝑠𝑡 into a signed score ˜𝑠𝑡 ,
for which larger is always better, and then into a normalized reward.
Each program and its execution feedback are stored in a task-local program database, and
program-transformation operators are repeatedly applied to generate new candidates. Within a
finite execution budget, evolutionary inference seeks the candidate with the highest signed score:

                                               𝑝★ = 𝑝arg max𝑡 ∈I ˜𝑠𝑡 ,

where I denotes the index set of all candidate programs recorded in the task-local program
database during the budgeted search. OpenMLE instantiates the operator space with Draft,
Improve, Debug, and Crossover, while leaving their global composition to the inference-time
search algorithm.
Learning to evolve from executable experience. Meta-evolution improves 𝜃 so that 𝑔𝜃 (· | 𝜏, 𝑎, 𝑐)
assigns higher probability to programs with stronger execution outcomes. Both SFT and RL can
be summarized as optimizing

                      Levo ( 𝜃) = −𝔼 ( 𝜏𝑖 ,𝑎𝑖 ,𝑐𝑖 ,𝑝𝑖 ) [𝑤 ( 𝑠𝑖 ) log 𝑔𝜃 ( 𝑝𝑖 | 𝜏𝑖 , 𝑎𝑖 , 𝑐𝑖 )] ,

where
                                      𝑠𝑖 = 𝑅𝜏𝑖 (E ( 𝑝𝑖 , 𝜏𝑖 ))
is the execution score and 𝑤 ( 𝑠𝑖 ) converts this outcome into a learning weight. For SFT, quality
filtering retains high-scoring programs 𝑝+𝑖 and assigns them positive supervision. For RL, newly
sampled programs are weighted by their processed execution rewards and entropic advantages
within the clipped policy objective. Thus, both stages update the same parameters 𝜃 to make
high-quality executable programs more likely under 𝑔𝜃 (· | 𝜏, 𝑎, 𝑐).

## 3 OpenMLE-Gym: Building Scalable Verifiable Environments

 Takeaway |
 • MLE requires a compute-backed, verifiable gym. LLM agents can be improved through
   interaction with executable, data-grounded environments. For MLE, the environment
   must host large, resource-intensive tasks, execute candidate programs under controlled
   budgets, and apply task-specific evaluators to return reproducible diagnostics and rewards.
   OpenMLE-Gym provides this substrate for post-training, search, and evaluation toward
   recursive self-improvement.
 • The gym scales through automated task construction. Our construction and quality-
   control pipeline turns curated anchors, Kaggle datasets, and Kaggle competitions into
   5,758 quality-gated executable environments spanning eight modalities and six core task
   types, with executability validation and semantic quality gating.

AI-for-AI requires agents to build and improve AI systems through executable experimentation,
making machine learning engineering (MLE) a concrete testbed for this loop. Such agents need
large-scale, diverse, high-quality task packages spanning data inspection, preparation, modeling,
prediction, and evaluation. Yet these resources remain scarce: existing benchmarks are limited in
openness, executable diversity, or coverage, while heterogeneous files, formats, and evaluation
protocols make them difficult to scale.
Static task collections alone do not support post-training or search. Agent-generated programs
must execute under controlled resources and produce reliable, informative feedback that guides
subsequent actions. Gym-style environments make this interaction contract explicit by coupling
tasks with actions, transitions, observations, rewards, and stopping conditions [Brockman et al.,
2016, Nathani et al., 2025, Qiang et al., 2025a, Xi et al., 2024]. OpenMLE-Gym therefore unifies
scalable executable tasks with standardized packages, isolated execution, structured diagnostics,
and task-specific evaluation for post-training, test-time search, and AI-for-AI.

### 3.1 Environment Contract

Each OpenMLE-Gym task is an environment instance defined by five elements. The task/state
consists of the task specification, public data, hidden evaluator, resource budget, and current
workspace state. The action is an agent-submitted MLE program together with its execution
requirements. The transition is sandbox execution: the environment materializes the workspace,
runs the program against public data, and invokes the evaluator when a valid submission is
produced. The observation is a structured record containing execution status, task score, logs,
error types, generated artifacts, and runtime metadata. The reward is the verifiable task-specific
score returned by the evaluator. Task completion, controller stopping criteria, and time or compute
budgets determine whether an interaction terminates or is truncated.

        Curation Hierarchy                              Task Curation Funnel                                  Executable Task Format
        trading off quality and scale                    (Kaggle Competitions)                                     unified, execution-ready package
                                                 from the Meta Kaggle catalog to quality-gated tasks
                                                                                                             task_package/
                                  Curated                    Meta Kaggle Catalog
                                                                                                                raw/
                                  Anchors                    ~11,000 competitions
Quality

                                                                                                                    original competition assets
                                  high quality
                            but limited scale             Leaderboard length · MLE-Bench exclusion
                                                                     licensing and rules                        data/

                                                              Eligible Candidates                                   public/                       agent-visible

                                Kaggle                         3,972 (36% retained)                                      description.txt
                          Competitions                                                                                   train.csv / train/ ...
                        Standardization
                                                      Automated package construction · metric validation

                                                                                                                         test.csv / test/ ...
                                    balanced                 Executable Packages
                            quality and scale                                                                            sample_submission.csv
                                                              2,839 (26% retained)
                                                               Strict semantic quality gate                         private/                      hidden labels

                                  Kaggle
                                                                task validity, data sufficiency,                         test_answer.csv
                                                                      raw-data usage,
                                Datasets                      task complexity, and data quality
                                                                                                                utils/
                               Generation
                                                                                                                                                   executable
                                                             Quality-Gated Tasks                                    prepare.py
                                   large scale               2,240 (20% retained)
                              variable quality                                                                      metric.py

                                                           Construction validation precedes
                                                                                                           public inputs + private answers + executable metric
                                Scale                   the independent semantic quality gate

Figure 3 | OpenMLE-Gym task curation and executable format. Left: source hierarchy. Middle:
Kaggle Competition filtering from the Meta Kaggle catalog to quality-gated packages. Right:
public task inputs, private answers, and executable utilities.

### 3.2 Scalable Task Construction

OpenMLE-Gym is our unified executable task suite, constructed from three source-specific paths
that occupy complementary positions in the quality–scale trade-off (Figure 3, left). Curated
Anchors provide the highest-confidence task designs because they are manually selected from
existing papers and benchmarks, but their dependence on prior expert curation limits scale.
We download their original assets and process them directly into executable packages. Kaggle
Datasets substantially broaden task and data coverage, although automatically induced objectives
can have more variable quality. We utilize and extend the existing MLE-Smith dataset-to-task
pipeline [Qiang et al., 2025b], then apply package-level quality control. Kaggle Competitions of-
fer a middle ground: human-authored problem specifications, evaluation metrics, and submission
protocols provide stronger task grounding, while prior participant engagement and leaderboard
records offer additional external evidence that tasks support meaningful, comparable evaluation.
Meanwhile, the Meta Kaggle catalog supports collection at scale. We build our own crawling
and competition-construction pipeline, with MLE-Bench-overlapping competitions excluded to
preserve evaluation integrity.
Following the principles of MLE-Dojo [Qiang et al., 2025a], we map all three sources into a
shared executable task package. Original assets remain under raw/. Agent-visible descriptions,
training data, test inputs, and sample submissions are placed under data/public/, while hidden
answers are isolated under data/private/. A task-specific metric.py validates prediction
files and returns scalar execution feedback. This contract gives heterogeneous tasks the same
agent-facing interaction surface while preserving their original semantics.
For the competition-derived branch, our automated framework converts a Kaggle competition slug
into a standardized executable package. It downloads and inventories the competition files, then
combines local evidence—including schemas, data types, dimensions, and sampled rows—with
Meta Kaggle records describing the problem, evaluation criterion, and submission protocol. From
this grounded context, the framework constructs the task description and generates prepare.py

                        Task Scale                                                           Dataset Distribution
         representative executable task-package resources                        normalized modality, task type, and non-raw package size

 OpenMLE-Gym                                               5,758         Modality Distribution

     MLE-Smith         606
                                                                           Tabular 44%            Image 18%                Time Series 13%
                                                                           Multimodal 11%         Text 9%                  Audio 2%
      MLE-Dojo       200+                                                  Video 1%               Other 2%

       DSBench 74
                                                                         Task Type Distribution
     MLE-Bench 75

                                                                           Classification 56%     Regression 31%           Other 9%
  MLGym-Bench 13
                                                                           Segmentation 2%        Object Detection 1%      Generation 1%

  MLAgentBench 13

                                                                         Package Size Distribution
                 0    1,000     2,000    3,000   4,000   5,000   6,000

   Curated Anchors          Kaggle Datasets        Kaggle Competitions     Under 1 MiB 29%        1-10 MiB 24%             10-100 MiB 23%
   156                      3,362                  2,240                   100 MiB-1 GiB 15%      1 GiB or more 9%

Figure 4 | Scale and composition of OpenMLE-Gym. Left: comparison with executable task-
package resources and source breakdown of 5,758 tasks. Right: normalized modality, task-type,
and non-raw package-size distributions.

to deterministically split labeled data, isolate public inputs from private answers, and produce a
schema-compatible sample submission. It then generates metric.py and validates the complete
package by executing the preparation code and scoring the sample submission. Failures and
assertion errors are returned as feedback for bounded retries; packages that remain unbuildable
or fail to produce a valid scalar metric are removed before semantic quality filtering. A detailed
stage-by-stage view is provided in Appendix A.1 (Figure 20).

### 3.3 Task Quality Filtering

To ensure the quality of constructed task packages, we propose an LLM-based quality filter. For
each task package, the filter jointly inspects the task description, raw files, processing script,
processed outputs, representative data samples, etc. It returns structured judgments along five
dimensions: task validity, data sufficiency, raw-data usage, task complexity, and data quality.
Together, these criteria identify degenerate targets solvable by trivial rules, inadequate training
or evaluation signal, superficial use of source assets, mismatched difficulty, data leakage, annota-
tion errors, and malformed processing. For example, the competition branch applies this final
semantic gate only after leaderboard-length screening, MLE-Bench overlap removal, licensing
and competition-rule screening and executable package and metric validation (Figure 3, middle).
We retain only metric-valid tasks receiving the strict recommended decision, thereby separating
semantic quality assessment from the executability check performed during construction.

### 3.4 Sandbox Execution at Scale

The contract is realized at scale by a shared sandbox execution backend. A centralized scheduler
receives API requests, records each job, tracks worker availability, and dispatches requests to
CPU/GPU Docker workers according to resource requirements. Each worker materializes an
isolated task workspace, mounts the task data and evaluator, executes the candidate program,

and writes logs, submissions, outputs, and artifacts back to shared storage. This separation of
control, execution, and storage supports reproducible scoring and scalable parallel execution
across long-running MLE jobs.
The backend returns six feedback modes: successful completion, runtime error, missing code,
missing submission, scoring failure, and timeout. Each record preserves the triggering condition
together with status, score when available, logs, error type, runtime metadata, and workspace
artifacts, allowing the agent to distinguish invalid execution from weak task performance. Detailed
architecture and representative feedback cases are provided in Appendix A.2.

### 3.5 Composition and Statistics

OpenMLE-Gym contains 5,758 executable tasks2 : 156 manually selected Curated Anchors, 3,362
Kaggle Dataset tasks generated from the official MLE-Smith table and quality-controlled at
the package level, and 2,240 tasks retained from our Kaggle Competition pipeline (Figure 4,
left). Across the three sources, the pool covers tabular, text, time-series, image, and other data
modalities, with classification and regression complemented by more engineering-intensive task
types. After canonicalizing modality and task-type labels, 11% of tasks are multimodal and
classification and regression together account for 87% (Figure 4, right). Additional construction
details are provided in Appendix A.1.

## 4 OpenMLE-ERL: Reinforcing Reusable Evolutionary Operators

 Takeaway |
 • RSI training should improve the best solution a model can find within a fixed budget.
   Execution-grounded SFT increases strong solutions and useful revisions under repeated
   sampling; RL uses adaptive score bounds and entropic advantages to reward candidate
   quality rather than validity alone.
 • Verification cost must shape collection and training. Budget-adaptive SFT stops at an
   accepted-example quota or execution limit, preserving budget for sparse-success tasks;
   asynchronous RL admits completed generation-and-execution groups immediately instead
   of waiting for the slowest job.
 • Evolutionary search depends on learning revisions, not only fresh drafts. We train
   Draft, Improve, Debug, and Crossover from trajectory transitions; stateful RL
   selects parents using reward, child-reward variance, and visit-based cooling.

Motivation. Evolutionary AutoResearch is judged by the best executable program found within
a finite search budget. A controller may invoke Draft, Debug, Improve, and Crossover
hundreds or thousands of times, so the model must learn more than one-shot solution generation:
it must repeatedly repair, refine, and recombine programs as the search unfolds. Post-training
should therefore expand the set of strong programs reachable through repeated sampling while
improving the individual transformations that the inference harness composes.
SFT and RL play complementary roles in meeting this objective. Execution-grounded SFT distills
complete solutions and successful local revisions from stronger teachers, giving the model a
broader set of executable behaviors before online learning begins. RL then moves probability
 2Owing to source-data licensing and copyright constraints, we release full task-package data for 1,415 tasks. For

the remaining 4,343 tasks, we release the corresponding prepare.py and metric.py scripts without redistributing
the source data.

toward the better candidates within that broadened distribution. This division is motivated by
prior analyses of RLVR: RL can raise Pass@1 by reinforcing already-rewarded solutions yet provide
limited gains at large 𝐾 , whereas teacher distillation can introduce behaviors absent from the
base model’s sampled support [Yue et al., 2025].
Executable evolutionary training also differs from short-horizon RLVR on mathematics and
code generation [Shao et al., 2024]. Many programs fail to produce a usable reward, while
successful programs receive continuous task scores drawn from different metrics and ranges.
Feedback arrives only after sandbox runs that may last minutes or hours, and every non-Draft
action depends on the parent program selected for expansion. OpenMLE-ERL addresses these
constraints across both stages: SFT collection uses execution results and per-task budgets to
select useful supervision, while RL preserves score differences among strong candidates, removes
synchronization stalls, and trains each operator on informative program states.

TRAINABLE ATOMIC OPERATORS
Shared operators for code evolution                                        Draft           Improve             Debug          Crossover
                                                                        create code       refine code        repair code     merge parents

 1   Evolutionary Inference                                               3   RL from Execution Feedback
     Operator-driven solution-tree expansion                                  Policy learning from sandbox rewards

                         Root - Task & Data

            </>                   </>                   </>                Raw score        Normalize          Adaptive          Entropic
            0.61                  0.47                 Error                                 reward            bounds            weights

                                                                         Operator-conditioned RL
     </>        </>        </>            </>     </>          </>        Sample op.                                           Sandbox
     0.58      Error       0.73          Error    0.32         0.67
                                                                                             Task
                                                                                           task data                        </> 1    score 1
            Edges: D solid - I dashed - B dotted - X double

Inference loop                                                                                                              </> 2    score 2
                                                                                            Parent         Policy model
   Pick       Select                              Score        Update
                          Create     Execute                                               program           pi(theta)
 operator     parent                              & rank        DB                                                          </> 3    score 3
                                                                                           candidate

                                  iterate
Scaffolds:         Greedy      abMCTS        AIRA-EVO OpenEvolve
                                                                           Sample parent                                   Group advantage
                                                                               F(p)
 2   SFT on Executable Rollouts
     Executable, high-score rollout supervision                                                                Policy update        Update

                          Filter
   Teacher                               Deduplicate     10K+ Draft                            Program database
                          valid,
  MLE rollouts                            by reward        rollouts
                       high-score
                                                                                  Sample by reward,
                                                                                variance & visit cooling         </> 1      s1      meta

                                                                                       high reward               </> 2      s2      meta
                          Warm-start policy
                                                                                      high variance
                          initializes RL policy                                                                  </> 3      s3      meta
                                                                                      under-sampled

Figure 5 | Overview of the OpenMLE training and inference workflow. Trainable atomic operators
are used by evolutionary inference, warm-started through executable SFT rollouts, and further
optimized with online RL from execution feedback.

### 4.1 Trainable Atomic Operators for Evolutionary Inference

A central design principle of OpenMLE is to separate the local skills learned by the model from the
search algorithm used at inference time. Rather than training full trajectories, OpenMLE trains
a compact set of reusable program-transformation operators over executable candidates. This
avoids sparse controller-specific supervision and lets the same learned operators be composed by
different evolutionary search procedures under a shared sandbox protocol.
We instantiate the atomic operators as Draft, Improve, Debug, and Crossover. This
operator vocabulary follows AIRA-style executable MLE search and AIDE-style code-space explo-
ration [Hambardzumyan et al., 2026, Jiang et al., 2025, Toledo et al., 2025], but OpenMLE adapts
it as explicit SFT and RL targets for open-model post-training. Detailed operator definitions,
prompt templates, and controller-specific search details are provided in the appendix.

### 4.2 Execution-Grounded Supervised Warm Start

Execution-grounded, budget-adaptive collection. For each task, we execute sampled programs
in the sandbox and retain examples according to their validity and task-specific scores. Collection
stops when either an accepted-example quota is reached or the task exhausts its execution
budget, allowing easy tasks to terminate early while allocating more attempts to tasks with sparse
successes. This difficulty-aware rejection strategy directs verification compute toward tasks for
which further exploration can still recover useful supervision [Tong et al., 2024].
Parallel and evolutionary sampling paths. The parallel path independently samples and executes
complete Draft solutions, contributing 17,245 full-response examples to the released corpus.
The evolutionary path applies Improve, Debug, and Crossover over executed programs and
retains useful steps from high-quality local trajectory segments, contributing 9,014 trajectory-step
examples. Figure 7 illustrates both paths. Overall, the two paths form the 26,259-example SFT
corpus released with OpenMLE; detailed corpus statistics are provided in Appendix B.1.

### 4.3 Execution-Grounded Reinforcement Learning

                                                                Validation Medal Count (out of 176)

                                                                                                                                                                   0.6
                       0.40                                                                           30
Validation Base Reward

                                                                                                                                             Rollout Base Reward

                       0.35                                                                                                                                        0.5

                       0.30                                                                           20                                                           0.4

                       0.25                                                                           15                                                           0.3

                       0.20                                                                           10                                                           0.2

                       0.15                                                                            5                                                           0.1

                              0   50       100      150   200                                              0   50       100      150   200                               0   50       100      150   200
                                       RL Training Step                                                             RL Training Step                                              RL Training Step

Figure 6 | RL training curves for Frontis-MA1-35B.

Building on the supervised warm start, the reinforcement-learning portion of Figure 7 previews
how state selection, adaptive reward normalization, and upper-tail weighting act on an evolution-
ary rollout.

 LEARNING FROM EXECUTED ROLLOUTS
 SFT corpus construction and RL reward shaping from executed rollouts

   Supervised Warm Start                                                          Reinforcement Learning
   Dr   below threshold    Dr     passes threshold                 SFT-selected        candidate parent           selected parent

   Dr Draft | Im Improve | Cr Crossover | Db Debug
                                                                                  Select Parent                        Reward Normalization
   Parallel Path                           Evolutionary Path
                                                                                                                       with Adaptive Bounds

  Dr     Dr    Dr     Dr     Dr      Dr                      Dr                                                     raw score                 processed reward
                                                                                                                  Top-1 (B)
                                              Im             Cr         Im                                                               remap

          threshold-passing drafts                      Db        Db
                                                                                        selected

                                          debug trace    Db                        parent reward                 Top-K (W)                    adaptive reward in [0,1]
                                                                                   child-reward variance
                                                                                                                current rollout scores       score below W maps to 0
                                                                                   visit cooling
                                              valid endpoint       Db
                                                                                  Concentrate Update

                                                                                   processed reward                                      entropic advantage
                                                                                                           same rollout group

           SFT DATA                                26,259 examples

                                                                                                                                   upper-tail signal amplified

Figure 7 | Learning from executed rollouts. The Parallel Path retains threshold-passing Draft
solutions. In the Evolutionary Path, a valid endpoint can emerge only after repeated Debug
steps; we trace back to the preceding non-debug operator and use an LLM to retain useful steps
from that repair trace. The selected examples from both paths form the 26,259-example released
SFT corpus under a budget-adaptive stopping rule. For a chosen operator, RL selects a parent
using parent reward, child-reward variance, and visit cooling. Top-1/Top- 𝐾 adaptive bounds map
seven nonzero task scores to four nonzero processed rewards in the illustrative rollout group,
with scores below the resolved lower bound clipped to zero; entropic advantages then amplify
the upper-tail learning signal.

Making heterogeneous outcomes comparable. One task may optimize accuracy and another
log loss; even after aligning their directions, raw score ranges remain incomparable. Let ˜𝑠 denote
a raw score converted to the convention that larger is better. We first define a bounded base
reward from a fixed pair of task bounds:
                                                                            𝛼
                                                          ˜𝑠 − 𝑏worst
                   𝑟base (˜𝑠; 𝑏best , 𝑏worst ) = clip                  , 0, 1 , 𝛼 > 0.        (1)
                                                        𝑏best − 𝑏worst

Fixed bounds establish a common interval, but leaderboard or theoretical extrema can be much
wider than the score region reached by the current policy. In that case, meaningfully different
programs collapse to nearly identical rewards. OpenMLE therefore derives tighter adaptive
bounds from each task’s historical on-policy score frontier and remaps ˜𝑠 to a processed reward
𝑟proc . The bounds evolve with the policy, preserving resolution where current candidates actually
lie while retaining a stable reward direction. This follows the broader lesson from adaptive
verifiable learning environments and evolving-rubric training that the evaluator scale must
preserve discriminative on-policy feedback [Shao et al., 2025, Zeng et al., 2025]. Appendix B.5
specifies the bound construction and edge-case handling.
Concentrating learning signal on the upper tail. After scores become comparable, the remaining
question is how strongly each candidate should affect the update. MLE evaluation rewards the
quality of the best program found; a barely viable submission should therefore not receive the

                                                                                                                   Previous reward         Adaptive bounds + entropic weighting

                                  Best-Candidate Advantage                                               0.8
                                                                                                                                                Test medal rate
                         8                                                                                                                        34.8 ± 4.3
                                     4.0x stronger upper-tail signal                                     0.7

                                                                                     Group Best Reward
Mean Processed Advantage

                                                                 6.39
                         6                                                                               0.6

                                                                                                         0.5
                         4                                                                                                            Test medal rate
                                                                                                         0.4                            24.2 ± 5.7

                         2        1.58                                                                   0.3                                 Peak smoothed reward 0.666
                                                                                                                                                      +0.089 vs previous
                                                                                                         0.2
                         0                                                                                     0        50           100          150          200          250
                             Without entropic                 With entropic
                                weighting                      weighting                                                             Training Step

                             (a) Entropic advantage signal                                                                (b) Group Best Reward

Figure 8 | Effect of upper-tail reward shaping. (a) Entropic weighting increases the processed
advantage assigned to the best candidate in a rollout group. (b) Combining entropic weighting
with adaptive bounds yields a stronger smoothed Group Best Reward trajectory than the previous
reward construction. The two test medal rates in panel (b) use a simpler early-stage harness
rather than OpenMLE-Evo.

same positive reward as a top-performing one. OpenMLE uses an entropic advantage that amplifies
reward gaps near the top of each rollout group, following the upper-tail principle studied in
TTT-Discover [Yuksekgonul et al., 2026] and related Best-of- 𝑁 /Pass@𝑘 objectives [Bagirov et al.,
2025, Chen et al., 2025, Peng et al., 2025, Walder and Karkhanis, 2025]. Omitting the stabilizing
max-centering used in implementation, the transform is
                                                                                   exp( 𝛽𝑟proc,𝑖 )
                                                                   𝐴ent
                                                                    𝑖   ≈       1  Í                          − 1,                                                           (2)
                                                                              𝐺 −1   𝑗 ≠ 𝑖 exp( 𝛽𝑟 proc , 𝑗 )

where 𝛽 controls concentration and is selected under a fixed entropy/KL budget. These advantages
replace the usual GRPO-style group-normalized signal in the clipped policy objective. Adaptive
bounds first make within-group differences visible; entropic weighting then directs substantially
more learning signal to the best candidates rather than uniformly reinforcing all non-failing
programs. Figure 8 shows both the resulting best-candidate emphasis and its observed effect
during training. Exact post-processing formulas appear in Appendix B.5.
Removing stragglers with asynchronous rollouts. Unlike token-level verification, the dominant
latency in MLE RL comes from executing candidate programs, and runtimes vary substantially
across tasks and solutions. In a synchronous batch, completed groups remain idle until its slowest
sandbox job returns. OpenMLE instead launches generation-and-execution groups independently
and lets the trainer consume each completed group from a queue. This decouples policy updates
from the longest job in a nominal batch while preserving group-level advantages. Because the
realized speedup depends on the task-runtime distribution and worker allocation, we keep the
main-text claim qualitative and report the measured timing study in Appendix B.4.
Selecting informative states for operator learning. Evolutionary RL must choose not only a
task and an operator, but also the program state on which that operator acts. Uniform parent
sampling spends updates on exhausted or uninformative regions; greedy sampling repeatedly
trains on the current incumbent and suppresses diversity. After selecting the operator to practice,
OpenMLE samples parent programs with a fitness-proportional utility that combines three terms:

                                                   𝐹 ( 𝑝) = norm( 𝑅 𝑝 ) + norm(Var𝑐 ∈child( 𝑝 ) 𝑅 𝑐 ) + norm( 𝐶 𝑝 ) ,                                                        (3)

Here 𝑅 𝑝 favors strong parent programs, child-reward variance Var𝑐 ∈child( 𝑝 ) 𝑅 𝑐 identifies regions
where operator outcomes remain informative, and 𝐶 𝑝 is a cooling coefficient that decreases

with repeated visits. The first term exploits promising solutions, the second targets states with
unresolved learning signal, and the third prevents a single incumbent from monopolizing the
rollout budget. This selection rule exposes Improve, Debug, and Crossover to useful yet
diverse local contexts; Appendix C.1 gives the exact implementation.

## 5 OpenMLE-Evo: Scaling Experience-driven Long-Horizon Search

 Takeaway |
 • Test-time scaling becomes test-time learning when search learns from experience.
   For AI-for-AI and recursive self-improvement, generating more candidates is not enough:
   the search process must convert execution outcomes into reusable evidence that changes
   what it explores next. Evolutionary test-time search provides this closed loop—propose,
   execute, learn from experience, and adapt future expansion over long horizons.
 • Experience-driven evolution hinges on two coupled scientific questions. Which node
   should be expanded next, beyond greedy score maximization? And how should memory
   be constructed so that the selected operator receives actionable evidence rather than an
   ever-growing trace? OpenMLE-Evo addresses the first with non-greedy, multi-factor
   selection over quality, progress, and novelty, and the second with operator-conditioned,
   on-demand synthesis from bounded relevant experience.

Motivation. AI systems that improve AI artifacts must use execution outcomes to determine what
to try next, rather than merely sample more candidates. Evolutionary test-time search opera-
tionalizes this feedback loop by maintaining executable programs, selecting parents, applying
transformations, and evaluating the resulting candidates. Over long horizons, effective search
therefore requires three capabilities: a persistent and queryable representation of prior attempts,
compute allocation across high-quality, improving, and novel branches, and bounded context
tailored to the transformation being applied.
AIDE, AIRA, and AIRA2 establish iterative search over executable programs through tree- or
population-based exploration, repeated execution, and candidate refinement [Hambardzumyan
et al., 2026, Jiang et al., 2025, Toledo et al., 2025]. OpenMLE-Evo adopts an AIRA-Evo-style
population loop to compose OpenMLE’s trained Draft, Improve, Debug, and Crossover
operators, but redesigns how the loop uses execution evidence. Standard AIRA-Evo stores largely
free-form memory, synthesizes it eagerly, selects parents primarily by scalar fitness, and supplies
different operators with broadly similar histories. OpenMLE-Evo instead stores structured
experience records, selects parents by quality, progress, and novelty, and synthesizes bounded
memory on demand for the operator being invoked. The details of each component are described
in the following sections, while the overall experience-guided search framework is illustrated in
Figure 9.

### 5.1 Structured Experience Accumulation

OpenMLE-Evo accumulates search experience at two complementary levels. First, after a
candidate is evaluated in the sandbox, the harness creates a node-level experience card. Its core
metadata is extracted deterministically from the search state and execution result, capturing the
candidate’s provenance, performance, execution outcome, and resource usage. The full schema
details and a grounded record are provided in Appendix C.3. This gives every node a compact and
consistently structured record of both the attempted change and its observed outcome. Second,
the harness aggregates the cards from all evaluated nodes into a task-global experience board.

                                                         Experience Card
                      Task
                                                            Node-id           Method-family     Delta-vs-parent               Rank                ...

                        N1
                       0.61                              One Improve step

                                                          1 Update experience card                2 Three-factor scoring

    N2                  N3                 N4                N7                      Exp card      Quality         Progress          Novelty
   0.64                0.59               0.667                                                               +                 +
                                                             </>                                    0.712           +0.045            0.707

                                                          Sandbox     score 0.712                                 Normalize +
                                                                                                                    Weight

              N5               N6          N7
             0.684            0.626       0.712
                                                          3 Select parent + Improve               4 Memory injection

                                                               Selection utility 1.812
                                                                                                  V = ancestor        V1            H = sibling
      N9                       N10         N8                  Softmax over N5, N6, N7
     0.676                    0.654       0.739                                                                       V2

                                                                         N7 selected parent       H1         H2       N7        H3         H4
                                                                       Improve                               Select V2, H2, H4
                     Draft            Improve
 Operator                                                                                                     LLM synthesis
  edges                                                                  N8
                     Crossover         Experience Card                                                       Relevant memory

Figure 9 | OpenMLE-Evo Search Harness. Left: The search tree expands candidate solutions
through drafting, improvement, and crossover operations, with each evaluated node paired with
a structured experience card. Right: Experience-card metadata is used to update the global
search state, compute parent-selection weights from quality, progress, and novelty, select the
next parent, and retrieve relevant memories from key ancestors and siblings for the subsequent
improvement operation.

The board maintains population-level statistics such as explored method families, family-wise
best candidates, underexplored directions, repeated failures, score trends, and the parent graph.
It therefore exposes the state of the surrounding search neighborhood, allowing a newly selected
node to understand not only its own history but also how its ancestors, siblings, and related
method families have performed. Together, the card and board prevent node-level signals from
being lost in the expanding search space. This queryable deterministic state supplies quality,
progress, and novelty to parent selection, and lineage, neighborhood, failure, and resource
evidence to operation-conditioned retrieval and on-demand memory synthesis.

### 5.2 Experience-Guided Parent Selection

Original AIRA-Evo derives parent-sampling probabilities primarily from normalized fitness. Con-
sequently, although parent selection remains stochastic, the search is driven almost entirely by
a node’s current validation score and tends to concentrate expansion on already strong nodes.
Other informative signals, such as how much a node improves upon its ancestry or whether it
introduces a previously underexplored solution family, are not explicitly considered.
In OpenMLE-Evo, we instead transform the deterministic metadata stored in each experience
card into three complementary factors: normalized validation score ˜𝑠𝑖 , normalized positive
                                    Δ𝑖 , and method-family novelty 𝜈𝑖 . For candidates 𝑖 ∈ I in
improvement over the strongest parent e

a sampled island, we define an experience-guided utility and sample the next parent according to
                                                                         exp(𝑈𝑖 /𝜏)
                                      Δ𝑖 + 𝜆 𝑛 𝜈𝑖 ,
                    𝑈𝑖 = 𝜆 𝑠˜𝑠𝑖 + 𝜆 Δ e               𝑃 ( 𝑖 | I) = Í                     .      (4)
                                                                       𝑗 ∈ I exp(𝑈 𝑗 /𝜏)

Thus, each parent-selection decision jointly considers three aspects of a candidate: its current
solution quality, the progress it achieved relative to its lineage, and the algorithmic novelty of the
direction it represents. This produces a more comprehensive expansion policy: it preserves selec-
tion pressure toward high-quality solutions while still allocating search budget to candidates that
demonstrate meaningful progress or introduce promising, underexplored approaches. Detailed
factor definitions and sampling procedures are provided in Appendix C.4.

### 5.3 Operation-Triggered Memory Synthesis

The original AIRA-Evo memory path eagerly invokes a language model to summarize the history
of every evaluated node by default. This spends inference budget on nodes that are never selected
by a later operator, while producing a summary before the decision context that should shape
it is known. OpenMLE-Evo separates deterministic storage from language-model synthesis:
after sandbox evaluation, it preserves the experience card and experience board, but defers
rich natural-language memory until an Improve, Crossover, or Debug call has selected
its relevant nodes. It then invokes the memory model only for the selected parent(s) and their
retrieved ancestors, siblings, or error-related attempts, and caches the resulting method and
parent-comparison summaries. This on-demand policy avoids unnecessary calls over long search
trajectories, improves the efficiency of LLM-based experience extraction, and lets an optimized
operation-aware extraction template produce more relevant, higher-quality memory. Prompt
templates and representative memory records are deferred to Appendix C.5.

### 5.4 Operator-Conditioned Context Construction

Once a parent has been sampled, OpenMLE-Evo constructs a small, operator-conditioned context
instead of appending the full free-form history. For Improve, it concatenates the selected node’s
deterministic experience record including its validation score, improvement over its parent,
method family, runtime, rank, incumbent status, and direction novelty with a vertical trace of its
recent ancestors and a horizontal set of direct siblings, namely prior candidates sharing at least
one parent. The sibling set is ranked by the same score–improvement–novelty utility used for
parent selection, and only the most informative siblings are retained; the operator can therefore
contrast the chosen trajectory with nearby alternatives rather than unrelated programs elsewhere
in the search. A global experience board, recomputed from all accumulated cards, further
supplies the current best method family, family-level success and failure statistics, underexplored
directions, recent improvement trends, and recurring error signatures. Crossover applies this
construction separately to both parents and adds a method-family complementarity cue, whereas
Debug retrieves prior attempts with the same error signature, falling back to recent attempts
when exact matches are unavailable. Concise method and parent-comparison summaries are
generated lazily for the retrieved nodes and cached, while the core retrieval signals remain
deterministic. This branch-local, bounded context avoids the redundancy of an ever-growing
history and gives each operator evidence that is directly actionable for refinement, recombination,
or repair. The resulting prompt also specifies the remaining search budget, remaining steps,
and per-run execution limit, so that these decisions remain feasible under the task’s actual
computational constraints; Appendix C.5 specifies the retrieval sets and generated fields.

## 6 Experiments

### 6.1 Experimental Setup

Experimental setup. We evaluate on the official 22-task MLE-Bench Lite split released with MLE-
Bench unless otherwise stated [Chan et al., 2024]. Unless specified otherwise, each OpenMLE-Evo
configuration is evaluated with three independent runs under a fixed per-task budget of 12 hours
on a single RTX 4090 (12 GB VRAM)—a smaller per-task sandbox-compute budget than that used
by the vast majority of reported evaluations on MLE-Bench.3 We report three aggregate metrics.
Valid Rate is the mean number of the 22 tasks for which a run produces a valid submission,
written as 𝑥 /22; Medal Average is the mean fraction of tasks receiving any Kaggle medal; and
Human Rank is the fraction of human leaderboard participants whose score is surpassed by the
submitted solution, averaged across tasks and runs, so higher is better. Our primary model is
Frontis-MA1-35B, which is used for the headline model, system, trajectory, and transfer analyses.
We additionally evaluate Frontis-MA1-30B as a companion model to test whether the post-training
gain reproduces on a second backbone and model scale.
OpenMLE-Evo-Max. OpenMLE-Evo-Max extends the OpenMLE-Evo configuration described
in Section 5 in two ways. First, it uses a general pipeline to distill reusable cross-task priors
from public competition artifacts; all MLE-Bench-related sources are excluded before distillation.
Second, it enables asynchronous multi-GPU parallel search while keeping the total sandbox
compute budget unchanged, following insights from AIRA2 [Hambardzumyan et al., 2026].

### 6.2 Training and Search Gains Compose

 Takeaway | Under the identical OpenMLE-Evo harness, execution-grounded post-training
 improves the Medal Average of our primary Frontis-MA1-35B over its corresponding Qwen3.6
 backbone by 21.22 percentage points; the companion Frontis-MA1-30B reproduces this
 gain at 18.18 percentage points over its Qwen3 backbone. Combining Frontis-MA1-35B
 with OpenMLE-Evo-Max further reaches 71.21%, exceeding GPT-5.5 with Codex by
 3.03 percentage points and showing that training and search provide complementary
 improvements.

Table 1 | MLE-Bench Lite results. Panel A presents the primary Frontis-MA1-35B comparison
first, followed by the companion Frontis-MA1-30B replication and matched search comparisons;
Panels B–C provide broader system context.

 Model / system                     Framework                 Valid Rate ↑      Medal            Human
                                                                             Average ↑         Rank ↑

 A. Controlled comparisons
Frontis-MA1-35B
 Qwen3.6-35B-A3B                    OpenMLE-Evo                19.67/22         39.39%           0.5828
Frontis-MA1-35B                   OpenMLE-Evo                21.67/22         60.61%           0.7647
Frontis-MA1-35B                   OpenMLE-Evo-Max            22.00/22         71.21%           0.8126

Frontis-MA1-30B
 Qwen3-30B-A3B4                     OpenMLE-Evo                17.33/22         34.85%           0.5573
                                                                                      Continued on next page

  3 This comparison uses the per-run evaluation compute configurations—accelerator allocation and wall-clock

budget—reported in the official MLE-Bench runs registry. It does not compare model-inference cost or normalize
different accelerators to FLOPs.
  4 The detailed version is Qwen3-30B-A3B-Thinking-2507.

 Table 1 — continued from previous page

 Model / system                  Framework             Valid Rate ↑    Medal       Human
                                                                    Average ↑    Rank ↑
 Frontis-MA1-30B                 OpenMLE-Evo            21.67/22       53.03%      0.7055
 Frontis-MA1-30B                 OpenMLE-Evo-Max        22.00/22       66.67%      0.8053

Matched harness comparison · GLM-5.2
 GLM-5.2                    Claude Code                 21.00/22      59.09%       0.7948
 GLM-5.2                    OpenMLE-Evo                 19.67/22      62.12%       0.7069
 GLM-5.2                    OpenMLE-Evo-Max             22.00/22      66.67%       0.8164

Matched harness comparison · MiniMax M3
 MiniMax M3                 Codex                       22.00/22      54.55%       0.7099
 MiniMax M3                 OpenMLE-Evo                 22.00/22      59.09%       0.7994
 MiniMax M3                 OpenMLE-Evo-Max             22.00/22      65.15%       0.8007

Matched harness comparison · Kimi K2.6
 Kimi K2.6                  Claude Code                 18.00/22      59.09%       0.7062
 Kimi K2.6                  OpenMLE-Evo                 21.67/22      66.67%       0.7859

Matched harness comparison · MiniMax M2.7
 MiniMax M2.7               Claude Code                 18.00/22      45.50%       0.5547
 MiniMax M2.7               OpenMLE-Evo                 22.00/22      50.00%       0.7039

 B. Broader OpenMLE-Evo system context
 Grok-4.5                    OpenMLE-Evo                22.00/22       65.15%      0.8052
 LongCat-2.0                 OpenMLE-Evo                21.00/22       56.06%      0.7343
 Doubao Seed 2.1 Pro         OpenMLE-Evo                20.33/22       56.06%      0.7170
 Qwen3.7 Plus                OpenMLE-Evo                21.67/22       54.55%      0.7234
 DeepSeek-V4-Pro             OpenMLE-Evo                21.67/22       54.55%      0.6849
 DeepSeek-V4-Flash           OpenMLE-Evo                21.33/22       51.52%      0.6957
 GLM-4.7                     OpenMLE-Evo                21.33/22       51.52%      0.6521
 MiMo-V2.5-Pro               OpenMLE-Evo                17.00/22       40.91%      0.5213
 Step-3.7 Flash              OpenMLE-Evo                19.00/22       27.27%      0.4953

 C. General-purpose coding-agent references
 GPT-5.6 Sol                  Codex                     22.00/22       72.73%      0.8891
 Kimi K3                      Claude Code               22.00/22       72.73%      0.8574
 GPT-5.5                      Codex                     21.00/22       68.18%      0.7833
 Claude Opus 4.8              Claude Code               22.00/22       63.64%      0.8219
 Gemini 3.5 Flash             Gemini CLI                20.00/22       63.64%      0.7499
 Claude Sonnet 5              Claude Code               22.00/22       59.09%      0.7730
 Claude Sonnet 4.6            Claude Code               22.00/22       54.55%      0.7670

Primary 35B model and system results. Under the identical standard OpenMLE-Evo harness,
execution-grounded post-training improves Frontis-MA1-35B over its Qwen3.6-35B-A3B base
from 39.39% to 60.61% Medal Average. Under this common harness, Frontis-MA1-35B also
outperforms MiniMax M3, Doubao Seed 2.1 Pro, and DeepSeek-V4-Pro, showing that the post-
trained model is competitive beyond its base-model comparison.
After injecting MLE-Bench-disjoint cross-task priors and widening parallel tree search through
OpenMLE-Evo-Max, Frontis-MA1-35B reaches 71.21%, exceeding GLM-5.2 and MiniMax M3
under the same enhanced harness. The resulting model–harness system also surpasses GPT-5.5

                                                                                            OpenMLE-Evo                Frontis-MA1           Evo-Max gain

71.21                                                                                                                   Frontis-MA1 + Evo-Max = 71.21
             66.67   66.67    65.15      65.15
                                                   56.06    56.06     54.55   54.55
 Evo                  Evo                                                               51.52      51.52
                                          Evo                                                                50.00
60.61                62.12
                                         59.09                                                                           40.91      39.39
                                                                                                                                               34.85
                                                                                                                                                          27.27

 Frontis       Kimi    GLM      Grok MiniMax Doubao LongCat Qwen                DS-V4      GLM      DS-V4 MiniMax MiMo Qwen3.6 Qwen3 Step3.7
35B          K2.6    5.2      4.5    M3     2.1P    2.0   3.7+                 Pro       4.7      Flash  M2.7 V2.5-Pro 35B    30B   Flash

Figure 10 | Model performance on MLE-Bench Lite under the common OpenMLE-Evo harness.
Solid bars report standard OpenMLE-Evo results, while hatched caps show the additional gains
from OpenMLE-Evo-Max for Frontis-MA1-35B, GLM-5.2, and MiniMax M3.

                      general harness       Original AIRA-Evo       OpenMLE-Evo        OpenMLE-Evo-Max increment             Frontis-MA1

     OpenMLE-Evo-Max 71.21
                                        OpenMLE-Evo 66.67           OpenMLE-Evo-Max 66.67        OpenMLE-Evo-Max 65.15

                        OpenMLE-Evo 60.61                                            OpenMLE-Evo 62.12
                                                                                                                       OpenMLE-Evo 59.09
 AIRA-Evo                                      CC 59.09                     CC 59.09                                                   OpenMLE-Evo 50.00
     53.03                                                                                               Codex 54.55

                                                                                                                                             CC 45.50

         Frontis-MA1-35B                    Kimi K2.6                     GLM-5.2                        MiniMax M3                        MiniMax M2.7

Figure 11 | Harness comparison on MLE-Bench Lite. Gray reports the general-purpose Claude
Code or Codex result, light orange reports original AIRA-Evo for the matched Frontis-MA1-35B
comparison, cyan reports OpenMLE-Evo, and hatched caps show the additional OpenMLE-
Evo-Max gain when available. The OpenMLE model is highlighted in saturated orange.

paired with Codex, demonstrating that the training and search gains compose at the system level.
To ensure the robustness of these results, we additionally report the mean and standard deviation
across three evaluation runs in Appendix D.1.
Cross-model replication on 30B. We separately apply the same post-training approach to
Frontis-MA1-30B. Under the identical standard OpenMLE-Evo harness, it improves over Qwen3-
30B-A3B-Thinking-2507 from 34.85% to 53.03% Medal Average; with OpenMLE-Evo-Max, it
further reaches 66.67% Medal Average and 0.8053 Human Rank. This controlled comparison
provides supporting evidence that the post-training and search gains are not confined to the
primary 35B checkpoint.
Harness gains from domain-specific search. Figure 11 compares harnesses while holding the
underlying model fixed. Across multiple model families, OpenMLE-Evo consistently converts
the same model into a stronger MLE system than general-purpose coding-agent harnesses such as
Claude Code and Codex. Against original AIRA-Evo, the matched Frontis-MA1-35B comparison
increases Medal Average from 53.03% to 60.61% under OpenMLE-Evo. The consistency of this
gain indicates that the improvement comes from search specialized for iterative machine learning
engineering, instead of a single favorable model–harness pairing.

                                                                                                                                      Validation to final test

             80%

             70%

             60%
 Medal Rate

             50%

             40%

             30%

             20%
                        GPT-5.6 Sol | Codex: val@12h=77.3%, test=72.7%         Kimi K3 | Claude Code: val@12h=77.3%, test=72.7%

             10%        GLM-5.2 | Evo-Max: val@12h=66.7%, test=66.7%           Frontis-MA1-35B | Evo-Max: val@12h=68.2%, test=71.2%
                        Grok-4.5 | Evo: val@12h=71.2%, test=65.2%              MiniMax M3 | Evo-Max: val@12h=68.2%, test=65.2%
                        Kimi K2.6 | Evo: val@12h=63.6%, test=66.7%             GPT-5.5 | Codex: val@12h=59.1%, test=68.2%
              0%
                   0            2                          4             6                  8                         10              12
                                                  Cumulative sandbox time per task (hours)

Figure 12 | Cross-harness Medal Rate evolution over the 22-task MLE-Bench Lite subset for the
top 8 systems. Each step curve reports the fraction of task outcomes whose best-so-far validation
score has reached any Kaggle medal by the indicated cumulative sandbox time. The separate
final-test panel reports Medal Rate after validation-based node selection, and colored bridges
expose the validation-to-test change for each system.

### 6.3 Long-Horizon Self-Improvement

            Takeaway | OpenMLE-Evo continues to improve well beyond the first executable solution.
            Later Improve and Crossover operations turn accumulated experience into decisive per-
            formance gains. This shows that experience-guided long-horizon search converts additional
            test-time compute into sustained progress rather than redundant sampling.

Aggregate long-horizon improvement. Figure 12 shows that combining Frontis-MA1-35B
with OpenMLE-Evo-Max yields sustained improvement throughout long-horizon search. The
resulting solutions generalize strongly to the final test, achieving a 71.21% Medal Rate, compared
with 68.18% on validation. This performance is comparable to GPT-5.6 Sol with xhigh reasoning
and Kimi K3 with their respective harnesses, both of which achieve 72.73% on the final test.
Structured recombination turns additional search into better ML models. Figure 13 shows
that the main difference is not merely finding an executable solution, but continuing to improve
its structure. Under the same OpenMLE-Evo protocol, the comparison models either plateau at
low Human Rank or improve without reaching a medal-quality held-out solution. In contrast,
Frontis-MA1-35B first uses Debug to establish viable image and tabular branches, then uses
Crossover to preserve their complementary evidence and Improve to upgrade the fused model
only after that design is stable. These latter operations produce 85.0% of the total validation gain,
indicating that the long horizon is spent accumulating and recombining useful branch evidence,
as opposed to repeatedly repairing a single program. The resulting trajectory reaches validation
Human Rank 0.7713 and held-out Human Rank 0.9455 with Bronze; the strongest comparison
reaches only 0.6303 on validation and earns no medal. The lead also holds in the three-epoch
averages, making the mechanism less consistent with a single lucky trajectory.

Memory-guided recombination breaks the search plateau. In figure 14, the comparison trajec-
tories remain near their first viable solutions, whereas Frontis-MA1-35B treats submission repair
as a starting point and subsequently builds specialized audio branches. Here memory matters
through selection, not volume: it preserves which branches contributed robust parsing, imbalance
handling, augmentation, and representation quality, while marking an inferior ResNet50 direction
as evidence to avoid. Improve and Crossover can therefore combine compatible gains instead
of inheriting an undifferentiated history; together they account for 91.9% of the total validation
improvement. This produces validation Human Rank 0.7284 and held-out Human Rank 0.8889
with Silver, while the strongest comparison reaches only 0.2963 in validation and none earns a
medal. The advantage remains after averaging all three epochs, and the shared corrected prompt
rules out the earlier submission-contract ambiguity as its explanation.

                                    Late Crossover and Improve Transform a Leaf Classifier
                                                leaf-classification • epoch 0 • OpenMLE-Evo • Frontis-MA1 nodes with matched baselines

                                                                 Validation Human Rank @ 12h
                           Frontis-MA1-35B 0.771            Qwen3.6 base 0.175         Step-3.7 Flash 0.323           MiniMax-M2.7 0.630                            HELD-OUT BEST OF 3

                       Repair +                Cross-model                  Backbone                            Stress-test                                                        0.945 Bronze
           1.0       branch setup               recombine                    upgrade                             variants
                                                                                                                                                      Frontis-MA1

           0.8                                                                           6                                                                              0.732 No medal
Human Rank

                                                                                                                                                    MiniMax-M2.7

           0.6
                                                                                                                                                                                 0.386 No medal
                       2                                                                                                                                 Step-3.7
           0.4

                                                                                                                                                                        0.183 No medal
           0.2
                                                                                                                                                    Qwen3.6 base

           0.0
             0.0                   1.5             3.0            4.5            6.0            7.5             9.0            10.5          12.0               0.00   0.25      0.50   0.75      1.00
                                                         Cumulative validation sandbox time (hours)                                                                       Human Rank

                 Frontis-MA1 Milestones                                                                                                     Draft       Debug          Improve          Crossover
                 Key program changes at the numbered trajectory nodes.

                     1 DEBUG: VALID CV                                           2 DEBUG: STABLE IMAGE                                     3 IMPROVE: MULTIMODAL

                     Fixes multiclass label encoding,                            Covers all 99 classes and removes                         Combines EfficientNet embeddings
                     unstable folds, and LightGBM                                irrelevant color jitter from the                          with 192 engineered margin, shape,
                     regularization.                                             ResNet18 branch.                                          and texture features.

                     step 2 Log loss 0.44622 Human Rank 0.3534                   step 4 Log loss 0.23730 Human Rank 0.4160                 step 11 Log loss 0.17472 Human Rank 0.4398

                     4 CROSSOVER: HYBRID FUSION                                  5 CROSSOVER: ROBUST FUSION                                6 IMPROVE: CONVNEXT LEAP

                     Fuses the robust ResNet18 branch                            Combines multimodal fusion, stronger                      Uses ConvNeXt-Tiny embeddings with a
                     with regularized LightGBM features                          augmentation, early stopping, and                         regularized MLP over fused image and
                     in one hybrid model.                                        TTA.                                                      tabular features.

                     step 15 Log loss 0.13123 Human Rank 0.4737                  step 29 Log loss 0.08268 Human Rank 0.5407                step 45 Log loss 0.02990 Human Rank 0.7713

Figure 13 | Cross-model search trajectories on leaf-classification. The left panel compares best-so-
far validation-derived Human Rank over 12 cumulative sandbox hours for the same epoch under
the common OpenMLE-Evo protocol; markers and numbered operation cards expose only the
detailed Frontis-MA1-35B trajectory. Its two Crossovers establish and strengthen multimodal
image–tabular fusion, and a late Improve operation produces the largest jump by upgrading the
fused representation to ConvNeXt-Tiny. The separate right panel reports held-out best-of-three
final-test Human Rank, where the selected Frontis-MA1-35B node obtains Bronze.

                               Repair and Recombination Produce a Silver Bird Detector
                                                 mlsp-2013-birds • epoch 0 • OpenMLE-Evo • Frontis-MA1 nodes with matched baselines

                                                               Validation Human Rank @ 12h
                         Frontis-MA1-35B 0.728             Qwen3.6 base 0.272             Step-3.7 Flash 0.296            MiniMax-M2.7 0.272                            HELD-OUT BEST OF 3
                        Submission          Build  Recombine                                               Memory                                                                        0.889 Silver
           1.0            repair          branches                                                       specialization
                                                                                                                                                          Frontis-MA1

           0.8                                                                                                                                                                        0.383 No medal
Human Rank

                                                                                                                                                             Step-3.7
           0.6
                                                                                                                                                                                0.272 No medal
                                                                                                                                                        Qwen3.6 base
           0.4                                         3
                                                                                                                                                                                0.272 No medal
           0.2
                                                                                                                                                        MiniMax-M2.7

           0.0
             0.0                1.5              3.0            4.5                 6.0            7.5              9.0            10.5          12.0                0.00   0.25      0.50     0.75     1.00
                                                       Cumulative validation sandbox time (hours)                                                                              Human Rank

                 Frontis-MA1 Milestones
                                                                                                                                                Draft        Debug          Improve           Crossover
                 Key program changes at the numbered trajectory nodes.

                     1 DEBUG: VALID SUBMISSION                                      2 IMPROVE: AUDIO FUSION                                    3 CROSSOVER: ROBUST AUDIO

                     Fixes the sample-submission merge and                          Fuses filtered spectrograms and segment                    Combines safe parsing, SpecAugment,
                     stabilizes LightGBM under severe class                         histograms with EfficientNet-B0 and an                     stratified CV, and EfficientNet-B2 with
                     imbalance.                                                     MLP.                                                       TTA.

                     step 5 AUC 0.74786 Human Rank 0.2716                           step 48 AUC 0.79390 Human Rank 0.2963                      steps 71-72 AUC 0.82774 Human Rank 0.3704

                     4 CROSSOVER: CLASS BALANCE                                     5 IMPROVE: FOCAL + TTA                                     6 CROSSOVER: MEMORY WINNER

                     Fuses aligned multimodal features with                         Uses focal loss and TTA to improve                         Selects the robust EfficientNet-B2
                     safe per-class AUC and class weighting.                        rare-species predictions.                                  branch with SpecAugment, OneCycleLR,
                                                                                                                                               and safe K-fold handling.

                     step 118 AUC 0.85744 Human Rank 0.4444                         step 119 AUC 0.87737 Human Rank 0.6420                     step 150 AUC 0.88576 Human Rank 0.7284

Figure 14 | Cross-model search trajectories on mlsp-2013-birds using the same corrected task
prompt. The left panel compares best-so-far validation-derived Human Rank over 12 cumulative
sandbox hours under the common OpenMLE-Evo protocol; markers and numbered operation
cards expose only the detailed Frontis-MA1-35B trajectory. Early Debug makes the submission
executable, while later Improve and Crossover operations build progressively stronger multimodal
audio branches. The separate right panel reports held-out best-of-three final-test Human Rank,
where the final Memory-guided Crossover obtains Silver.

### 6.4 Solution Ceiling

            Takeaway | Within matched model and search comparisons, the gains are not limited to
            moving more solutions across the Bronze threshold: stronger systems also produce a larger
            share of Gold solutions.

Figure 15 reveals a consistent qualitative shift for the primary 35B model: post-training and
OpenMLE-Evo-Max do not merely increase medal coverage, but move successful solutions
toward Gold. The companion 30B comparison reproduces the same direction of change, while
the fixed-model GLM-5.2 and MiniMax M3 comparisons show that the pattern also extends to
search improvements. Together, these results indicate improved solution quality rather than
only more Bronze-threshold crossings. Compared with external systems, Frontis-MA1-35B with
OpenMLE-Evo-Max outperforms Claude Opus 4.8 with Claude Code and Gemini 3.5 Flash with
Gemini CLI, and matches Kimi K3’s Gold rate.

 Medal Tier Distribution Across Matched and External Systems                        Gold   Silver        Bronze

                                        0%        25%             50%       75%                   100% Medal rate

 Frontis-MA1-35B
Qwen3.6-35B · OpenMLE-Evo                                                                              39.39%
Frontis-MA1-35B · OpenMLE-Evo                                                                          60.61%
Frontis-MA1-35B · OpenMLE-Evo-Max                                                                      71.21%
 Frontis-MA1-30B
Qwen3-30B · OpenMLE-Evo                                                                                34.85%
Frontis-MA1-30B · OpenMLE-Evo                                                                          53.03%
Frontis-MA1-30B · OpenMLE-Evo-Max                                                                      66.67%
 GLM-5.2 search
GLM-5.2 · OpenMLE-Evo                                                                                  62.12%
GLM-5.2 · OpenMLE-Evo-Max                                                                              66.67%
 MiniMax M3 harness + search
MiniMax M3 · OpenMLE-Evo                                                                               59.09%
MiniMax M3 · OpenMLE-Evo-Max                                                                           65.15%
MiniMax M3 · Codex                                                                                     54.55%
 Representative general-agent harnesses
GPT-5.6 Sol · Codex                                                                                    72.73%
Kimi K3 · Claude Code                                                                                  72.73%
Claude Opus 4.8 · Claude Code                                                                          63.64%
Gemini 3.5 Flash · Gemini CLI                                                                          63.64%

Figure 15 | Gold, Silver, and Bronze decomposition for matched OpenMLE comparisons and
representative general-agent harnesses. Bar lengths report the fraction of evaluated outcomes at
each medal tier; labels report the final Medal Rate.

### 6.5 Search Efficiency and Mechanism

 Takeaway | The available trajectory evidence indicates that bounded, operation-conditioned
 context can improve search productivity while targeted recombination and multi-factor
 parent selection preserve complementary hypotheses that score-only lineage search may
 discard.

OpenMLE-Evo versus original AIRA-Evo. Figure 16 compares complete single-worker trajecto-
ries from the same Frontis-MA1-35B checkpoint under the same seed and 12-hour task budget,
covering 66 task–run evaluations per harness. Lower search cost. Panel A shows that OpenMLE-
Evo reduces total model-token consumption from 129.3M to 75.3M (−41.7%) and prompt tokens
from 83.5M to 41.5M (−50.3%), while the number of evaluated nodes falls only from 3430 to
3004 (−12.4%). The much larger reduction in tokens than in nodes indicates that the saving
comes primarily from making each expansion cheaper, not merely from terminating the search
earlier or evaluating far fewer candidates. Higher search yield. Panel B counts a new-best
validation update whenever a node strictly improves the task–run’s best selection reward after its
first finite result. Although it evaluates fewer nodes, OpenMLE-Evo records 246 such updates
rather than 229, raising new-best updates per million total model tokens from 1.77 to 3.27
(+84.3%). The fraction of Improve operations that establish a new best likewise rises from
44/931 (4.73%) to 72/769 (9.36%), showing that refinement calls are more likely to produce
useful progress. Bounded operation context. Panel C connects this improved yield to the
intended context mechanism. For Improve, the mean serialized user-prompt length falls from
102.8K to 35.7K Unicode characters (−65.3%), and its 99th percentile falls from 389.0K to 54.3K
(−86.1%). For Crossover, the corresponding mean falls from 140.4K to 55.3K (−60.6%), while
the 99th percentile falls from 419.2K to 78.4K (−81.3%). The compression is especially strong in
the tail, consistent with structured operation-conditioned memory preventing long histories from
being repeatedly serialized into every request. Together, the panels show that OpenMLE-Evo
improves the productivity of each refinement. We characterize search efficiency using token
usage, context length, and validation-trajectory productivity.

                      Structured Experience Increases Search Yield per Token
                        Same Frontis-MA1-35B checkpoint · same seed · 12-hour task budget · 66 task-runs per harness

 A   Less search compute                           B    More useful discoveries                                   C    Bounded operation context

 Total tokens                 −41.7%               New-best validation             +7.4%
                                                 updates                                                            35.7k            102.8k
                          129.3M                                                             Improve prompt
                                                                       229
               75.3M                                                                                average
                                                                        246                                                 −65.3%
                                                                                                                            55.3k         140.4k
                                                                                           Crossover prompt
 Prompt tokens                −50.3%               New-best updates per
                                                                                +84.3%              average
                                                 1M model tokens                                                                    −60.6%
                          83.5M                                    1.77
              41.5M                                                                                                         54.3k                      389.0k
                                                                               3.27          Improve prompt
                                                                                              99th percentile
                                                                                                                                          −86.1%
                                                 Improve operations
 Evaluated nodes              −12.4%                                              +98.1%                                            78.4k                 419.2k
                                                 setting a new best
                          3.43k                                                            Crossover prompt
                                                                       4.73%
                                                                                             99th percentile
                       3.00k                                                    9.36%                                                         −81.3%

 0         50       Original = 100                0            Original = 100           2×                        30k         50k       100k      200k     400k
                                                                                                            serialized prompt characters per node (log scale)

                                                      Original AIRA-Evo        OpenMLE-Evo                           99th percentile: 99% of prompts are shorter

Figure 16 | Search efficiency and context-length comparison between original AIRA-Evo (gray)
and OpenMLE-Evo (cyan) over 66 matched task–runs. Panel A normalizes each resource metric
to original AIRA-Evo = 100 and annotates the absolute totals. Panel B reports validation-trajectory
productivity. A “new-best validation update” is a strict increase in selection reward after a task–
run’s first finite score; the per-million-token denominator includes both prompt and completion
tokens, and the Improve rate is the fraction of Improve operations that set a new best. Panel
C reports serialized user-prompt length in Unicode characters on a logarithmic axis; the 99th
percentile is the length below which 99% of prompts fall.

Targeted Crossover escapes a single-branch Debug loop. Figure 17 contrasts two grounded
nomad2018-predict-transparent-conductors traces. Original AIRA-Evo follows a single lineage
after its Draft fails: seven successive Debug attempts inherit an expanding full history, and the
final repair reaches validation RMSE 0.06633 and held-out RMSE 0.06096. The OpenMLE-Evo
trace instead constructs a targeted Crossover at step 81 from complementary evidence. One
parent contributes atomic properties, dynamic covalent edges, and unit-cell volume (validation
RMSE 0.06309); the other contributes a robust parser for irregular .xyz geometries (validation
RMSE 0.06573). Horizontal Memory also marks an RDF-cache TypeError and a 3328 × 94
feature mismatch as negative evidence, thereby avoiding their silent serialization into the child
context. The resulting program combines the physics-informed GNN with the robust parser,
density descriptors, and cosine scheduling, reaching validation RMSE 0.06087 and held-out
RMSE 0.05410, respectively 8.2% and 11.3% below the original trace. The comparison illustrates
the intended mechanism: operation-conditioned Memory converts distinct branch strengths and
known failures into a bounded recombination request instead of repeatedly repairing one lineage.
Three-factor selection preserves a complementary parent. Figure 18 shows why selecting
parents by current score alone can discard useful structure on the-icml-2013-whale-challenge-right-
whale-redux. In the original AIRA-Evo trace, two independently repaired branches reach validation
AUCs 0.94656 and 0.85546; score-only selection keeps the stronger branch, producing held-out
AUC 0.94852. The OpenMLE-Evo step-10 candidate pool exposes a subtler choice. Parent A is
the score leader at AUC 0.99187 and provides a deeper ResNet-SE pipeline with 64-Mel features,
AMP, and test-time augmentation. Parent B scores slightly lower at 0.98773 and ranks only sixth
by score, but ranks first by gain after improving 0.00568 over its own parent; it retains a promising
Log-Mel representation with Delta and Delta-Delta temporal channels. With Score/Gain/Novelty
weights 1.0/0.6/0.3, Parent B moves to the top utility rank, and its selection probability within
the same ten-parent pool increases from 10.47% under score-only softmax to 17.09%, a 63.2%
relative increase. Parent B is then selected for an Improve operation, whose child reaches
validation AUC 0.99203 and held-out AUC 0.99386. This within-pool probability recomputation
directly exposes the selector’s effect: the additional factors do not force a lower-scoring branch to

  CASE STUDY 01 / NOMAD 2018

  From linear repair to evidence-guided fusion

  A / ORIGINAL AIRA-EVO                                                        B / OPENMLE-EVO

  One lineage, repeatedly repaired                                             Selected evidence, bounded by operation
  Score-softmax parent sampling · full-history context                         Three-factor selection · lazy summaries · targeted context

           01 SELECT PARENT                                                        PARENT 01 / PHYSICS        PARENT 02 / ROBUST            FAILED SIBLINGS
           Continue the current repair lineage                                   Atomic properties           Flexible .xyz parser        RDF cache TypeError
           Best available score anchors the next operation.                      Dynamic covalent edges      Irregular formats           3328 × 94 mismatch
                                                                                 Unit-cell volume            Executable repair           Incompatible path
           02 DRAFT
           Execution error                                                       val 0.06309                 val 0.06573                 negative evidence

           No scored evidence enters the branch.

           03 DEBUG × 7                                                             TARGETED CROSSOVER MEMORY / STEP 81
           Repair the same branch again
                                                                                    KEEP physics          KEEP parser            REJECT known failures
           Each retry inherits an expanding history.
           SERIALIZED CONTEXT GROWTH

                                                                                       GENERATED CROSSOVER CHILD
           FINAL DEBUG
                                                                                       Physics GNN + robust parser
                                                                                       Density descriptor · cosine schedule · compatible dimensions
  VALIDATION RMSE                  HELD-OUT RMSE                                       VALIDATION RMSE                       HELD-OUT RMSE

  0.06633                          0.06096                                             0.06087 −8.2%                         0.05410 −11.3%

Figure 17 | Single-branch repair versus targeted Crossover on nomad2018-predict-transparent-
conductors. Original AIRA-Evo repeatedly debugs one lineage using full-history context.
OpenMLE-Evo selects complementary physics and parsing parents, excludes failures observed
in nearby siblings, and forms an operation-bounded Crossover child. Lower RMSE is better.

win, but keep a high-gain, structurally distinct branch actionable long enough to be selected and
refined. Because the full framework also changes targeted Memory, the end-to-end difference
from original AIRA-Evo should not be attributed to the three weights alone.

### 6.6 Meta-Ability and Transfer

 Takeaway | Modality-stratified MLE-Bench results show broad gains across data types, and
 controlled NatureBench Lite results provide initial evidence of transfer beyond competition-
 style MLE; small modality groups and the ten-task transfer set limit the breadth of both
 conclusions.

Cross-modality meta-ability on MLE-Bench. Before testing out-of-benchmark transfer, we ask
whether the learned improvement capability is tied to a narrow input modality. We partition the
22 MLE-Bench Lite tasks into five mutually exclusive groups: image, text, tabular/structured,
audio, and multimodal. Relative to Qwen3.6-35B-A3B under the same OpenMLE-Evo har-
ness, Frontis-MA1-35B raises mean Human Rank in all five groups and never lowers group-level
Medal Rate (Figure 19). The 14 additional medals are distributed across every group (im-
age/text/tabular/audio/multimodal: +2/+4/+1/+4/+3), so the aggregate gain is not explained
by one modality alone.
Generalization to NatureBench. NatureBench evaluates whether coding agents can recover
or improve upon published scientific results [Wang et al., 2026]. Its full benchmark contains
90 containerized tasks distilled from peer-reviewed Nature-family papers across six scientific
domains. Each task hides the test ground truth and paper method behind a host-side evaluator,

   CASE STUDY 02 / RIGHT WHALE

   When the best score is not the best complement

   A / ORIGINAL AIRA-EVO                                                          B / OPENMLE-EVO

   Absolute score controls the gate                                               Complementarity changes who gets selected
   Score-softmax selection · independent repair branches                          Score identiﬁes strength; gain and novelty preserve useful alternatives

   RANKED BY VALIDATION SCORE
                                                                                       PARENT A / SCORE LEADER                                    PARENT B / GAIN LEADER

   01         REPAIR BRANCH A
              Draft error → Debug error → Debug
                                                           AUC 0.94656               Deep ResNet-SE                                             Log-Mel + temporal deltas
                                                                                     64-Mel · AMP · test-time augmentation                      Delta and Delta-Delta channels

                                                                                     AUC 0.99187                        SCORE RANK #1           AUC 0.98773                         SCORE #6 / GAIN #1

   02         REPAIR BRANCH B
              Draft timeout → Debug
                                                           AUC 0.85546

                                                                                         THREE-FACTOR PARENT SELECTION / SAME 10-PARENT POOL

                                                                                          SCORE / ABSOLUTE QUALITY             GAIN / PARENT IMPROVEMENT            NOVELTY / BRANCH DIVERSITY

   SCORE-ONLY FINAL SELECTION                                                             1.0                                  0.6                                  0.3
   Branch A survives
   Branch B contributes nothing to the ﬁnal program.                                      P(SELECT PARENT B)        10.47%                                  17.09%               +63.2% RELATIVE

   FINAL DEBUG
                                                                                                      SELECTED IMPROVE CHILD                                  VALIDATION AUC

   VALIDATION AUC                       HELD-OUT AUC                                                                                                          0.99203
                                                                                                      B's temporal channels
   0.94656                              0.94852
                                                                                                                                                              HELD-OUT AUC

                                                                                                      EMA · 5-way TTA · label smoothing                       0.99386

Figure 18 | Score-only versus three-factor parent selection on right-whale detection. Parent A
leads in current validation AUC, whereas Parent B ranks sixth by score but first by gain and
retains promising temporal channels. Score/Gain/Novelty weighting raises Parent B’s selection
probability from 10.47% to 17.09% over the same ten-parent pool, enabling an Improve child
derived from Parent B. Higher AUC is better.

and compares heterogeneous scientific metrics through the direction-normalized relative gap
                                           𝑚 − 𝑚SOTA
                                   𝑔 = dir            ,                                 (5)
                                            | 𝑚SOTA |
where 𝑚 is the submitted result and dir ∈ {−1, +1} accounts for whether the task metric is
minimized or maximized. We report Match-SOTA (All M), the fraction of tasks with 𝑔 ≥ 0, and
Surpass-SOTA (All S), the stricter fraction with 𝑔 > 0.1.
For a tractable but heterogeneous transfer study, we use NatureBench Lite, a fixed 10-task
subset spanning all six domains, six represented input-modality families, and four ML task types;
Appendix D.2 lists the tasks. We retain the NatureBench task containers, hidden evaluator, validity
rules, web-search-disabled setting, and four-hour search budget per task. The OpenMLE-Evo
NatureBench adapter changes the task interface, resource scheduling, and feedback plumbing
needed to run the same evolutionary program operators against NatureBench’s evaluator; it does
not expose hidden labels or the paper solution. Table 2 reports the reference agent results and
our controlled model–harness comparisons.
The transfer results expose contributions from both the post-trained model and the adapted
search framework. Holding the NatureBench adapter fixed, Frontis-MA1-35B improves over its
Qwen3.6-35B-A3B base by 10 percentage points in All S (3/10 versus 2/10) and 20 points in All
M (7/10 versus 5/10). Holding the base model fixed, the OpenMLE-Evo NatureBench adapter
improves over original AIRA-Evo by 10 points in All S (2/10 versus 1/10) and 30 points in All M
(5/10 versus 2/10). Consequently, the combined Frontis-MA1-35B system matches the 3/10 All S
and 7/10 All M attained by GPT-5.4, GLM-5.1, and MiniMax-M3 on this subset, and exceeds the
reported DeepSeek-V4-Pro, Claude Opus 4.6, and MiniMax-M2.7 configurations. This provides
evidence that execution-grounded post-training transfers beyond competition-style MLE and that
the adapted long-horizon search can convert more of that capability into paper-relative scientific
progress.

               Model performance across MLE-Bench Lite modalities

                                                     Base / Medal Rate            Base / Human Rank                   Frontis / Medal Rate           Frontis / Human Rank

              1.00                                                                                                                                              M 100%
                                                                                                                                                                HR 0.90                              HR 0.88
                                                                                                                                                                                                     M 83%
              0.75                              HR 0.74                                                                   HR 0.76

                     HR 0.65                                                         HR 0.67
 Score / rate

                                                                                     M 60%
                                                          HR 0.56                                                                                                         HR 0.53
              0.50                              M 52%                                          HR 0.52                    M 50%     HR 0.50
                      M 44%
                                                                                                M 42%
                                                           M 33%                                                                     M 33%                                 M 33%
              0.25

              0.00
                               Base   Frontis                       Base   Frontis                       Base   Frontis                       Base    Frontis                       Base   Frontis
                                 Image                                 Text                         Tabular / structured                         Audio                              Multimodal
                                  9 tasks                              5 tasks                              4 tasks                              2 tasks                               2 tasks

Figure 19 | Modality-stratified results on the MLE-Bench Lite subset. Base denotes Qwen3.6-
35B-A3B and Frontis denotes Frontis-MA1-35B, both evaluated with OpenMLE-Evo. Wide
outlined bars show Medal Rate, and narrow filled bars show mean Human Rank; both use all
three task–epoch outcomes per task, with invalid final submissions assigned zero Human Rank.

Table 2 | Results on NatureBench (NB) Lite. S and M denote Surpass-SOTA (𝑔 > 0.1) and
Match-SOTA (𝑔 ≥ 0), respectively. Public reference agents use Codex for GPT models, Gemini CLI
for Gemini 3.5 Flash, and Claude Code for all other models. Bold indicates the best result.

Rank Model                                                             Agent harness                                                              All S ↑                                All M ↑
NatureBench Lite reference agents
1   Claude Opus 4.7       Claude Code                                                                                                  70.0% (7/10) 100.0% (10/10)
2   GLM-5.2               Claude Code                                                                                                  70.0% (7/10) 100.0% (10/10)
3   Gemini 3.5 Flash      Gemini CLI                                                                                                   60.0% (6/10)  80.0% (8/10)
4   GPT-5.5               Codex                                                                                                        40.0% (4/10) 100.0% (10/10)
5   Qwen 3.7 Max          Claude Code                                                                                                  40.0% (4/10)  60.0% (6/10)
6   Kimi K2.6             Claude Code                                                                                                  30.0% (3/10)  90.0% (9/10)
7   GPT-5.4               Codex                                                                                                        30.0% (3/10)  70.0% (7/10)
8   GLM-5.1               Claude Code                                                                                                  30.0% (3/10)  70.0% (7/10)
9   MiniMax-M3            Claude Code                                                                                                  30.0% (3/10)  70.0% (7/10)
 10 DeepSeek-V4-Pro Claude Code                                                                                                          20.0% (2/10)  60.0% (6/10)
 11 Claude Opus 4.6         Claude Code                                                                                                  20.0% (2/10)  50.0% (5/10)
 12 MiniMax-M2.7            Claude Code                                                                                                   0.0% (0/10)  30.0% (3/10)
OpenMLE controlled comparisons
 –   Frontis-MA1-35B      OpenMLE-Evo NB adapter 30.0% (3/10)                                                                                                                    70.0% (7/10)
 –   Qwen3.6-35B-A3B OpenMLE-Evo NB adapter 20.0% (2/10)                                                                                                                         50.0% (5/10)
 –   Qwen3.6-35B-A3B Original AIRA-Evo           10.0% (1/10)                                                                                                                    20.0% (2/10)

NatureBench trajectory: protein variant effect prediction. Under the same NatureBench
adapter, Frontis-MA1-35B reaches task-level aggregate improvement 𝑔 = 0.1161 across 11 protein-
assay instances, versus 𝑔 = 0.0243 for its Qwen3.6-35B-A3B base. The search advances from
a valid Draft at 0.0679 through Debug and Improve nodes to a Crossover incumbent
at 0.1016. Rather than greedily refining only that incumbent, the three-factor selector revisits

a distinct 0.0955 branch whose score, recent gain, and novelty remain promising. Vertical
and horizontal Memory preserve successful physicochemical features while exposing nearby
timeout, KeyError, and nested-mapping failures; the resulting Improve node retains the
robust flat mapping and adds training-label-derived positional priors with five-fold LightGBM
ensembling, reaching 0.1161 without hidden test labels or the paper solution. The trace illustrates
how post-training supplies an effective scientific refinement while structured memory keeps a
non-incumbent hypothesis actionable long enough to overtake the current best.

## 7 Related Work

AutoResearch systems and evaluation targets. AutoResearch systems increasingly automate
hypothesis formation, experimentation, and artifact production, from end-to-end scientific work-
flows and agentic tree search to focused, compute-bounded model-training loops [Karpathy, 2026,
Lu et al., 2024, Yamada et al., 2025]. Recent systems further explore persistent project state,
hypothesis-tree refinement, cross-task skill accumulation, and continuously evolving multi-agent
workflows [Chen et al., 2026, Jin et al., 2026, Kim et al., 2026, Zhu et al., 2026a]. Benchmarks iso-
late complementary slices of this research loop: RE-Bench and PostTrainBench target open-ended
AI R&D and autonomous model post-training [Rank et al., 2026, Wijk et al., 2025]; MLGym, AIRS-
Bench, MLRC-Bench, and ResearchGym study research-oriented problem solving and end-to-end
ML projects [Garikaparthi et al., 2026, Lupidi et al., 2026, Nathani et al., 2025, Zhang et al.,
2025b]; and PaperBench and NatureBench emphasize reproducing papers or published scientific
results [Starace et al., 2025, Wang et al., 2026]. Within executable MLE, MLE-Bench evaluates
agents on end-to-end Kaggle-style competitions [Chan et al., 2024], whereas MLS-Bench targets
improving ML components in ways that generalize across controlled settings and scales [Lyu
et al., 2026]. We evaluate OpenMLE on MLE-Bench Lite as its primary MLE benchmark and on
NatureBench Lite as a focused test of transfer to broader scientific AutoResearch.
Executable MLE environments and scalable task resources. Classical AutoML optimizes
over predefined model and pipeline spaces [Erickson et al., 2020, Feurer et al., 2015, Olson
et al., 2016, Thornton et al., 2013], whereas LLM-based MLE agents operate through open-
ended, code-mediated experimentation. Building on this benchmark lineage, MLAgentBench and
DSBench likewise require agents to write, execute, debug, and submit solutions on realistic ML
and data-science tasks [Huang et al., 2023, Jing et al., 2024]. Complementary efforts expand
the underlying execution and training infrastructure: MLE-Dojo standardizes interactive MLE
environments [Qiang et al., 2025a], while MLE-Smith and SandMLE scale the construction
of executable training tasks [Qiang et al., 2025b, Zhou et al., 2026]. These resources make
execution feedback available at increasing scale, but executable tasks alone do not specify how
experience should be transformed into reusable model capabilities or composed at inference
time. OpenMLE-Gym builds on this line by unifying scalable task environments with isolated
execution, structured feedback, and task-specific evaluators as a shared substrate for post-training,
search, and evaluation.
Inference-time scaffolds and evolutionary search. Given executable evaluators, inference-time
scaffolds amplify frozen models by allocating trials, maintaining search state, and selecting
or transforming candidate programs. MLE systems instantiate this idea through multi-agent
decomposition [Fang et al., 2025, Gandhi et al., 2024, Li et al., 2025c, Trirat et al., 2024],
structured search [Chi et al., 2024, Jiang et al., 2025], and targeted refinement or domain
knowledge [Du et al., 2025, Liu et al., 2025a, Nam et al., 2025, Ou et al., 2025, Zhang et al.,
2025a]. AIRA-style analyses further identify search policy, operator quality, throughput, and
ideation diversity as key performance factors [Audran-Reiss et al., 2025, Hambardzumyan et al.,
2026, Toledo et al., 2025]. More generally, program-evolution systems use language models as
mutation operators and executable evaluators as selection signals [Cemri et al., 2026, Lange

et al., 2025, Novikov et al., 2025, Ye et al., 2026], while ThetaEvolve and TTT-Discover update
problem-solving behavior from test-time feedback [Wang et al., 2025, Yuksekgonul et al., 2026].
These methods establish the value of structured search, but typically rely on transformation
behavior supplied by the frozen backbone or its prompts; OpenMLE-Evo instead composes
operators explicitly trained for the same roles used during search.
Learning MLE agents from executable experience. A complementary line internalizes verifiable
outcomes through supervised or reinforcement-learning updates rather than retaining all im-
provement logic in an external scaffold. RLVR has produced strong learned reasoning capabilities
in mathematics and coding [Guo et al., 2025, Team et al., 2025, Zeng et al., 2025] and has
increasingly been extended to long-horizon agent tasks [MiniMax, 2026, Team et al., 2026,
Zeng et al., 2026]. MLE-specific efforts similarly learn from executable task rewards [Cai et al.,
2026, Li et al., 2025b, Liu et al., 2025b, Yang et al., 2025a], establishing that MLE experience
can be internalized by the model. However, these efforts expose different subsets of the task,
environment, training, evaluation, and model artifacts needed for a reproducible end-to-end
workflow, and their learned policies are not uniformly organized around an interface shared with
long-horizon search (Appendix Table 11). OpenMLE-ERL follows this learning direction but
trains reusable Draft, Improve, Debug, and Crossover transformations whose interfaces
match the operations invoked by OpenMLE-Evo.
AI-for-AI and trainable improvers. AI-for-AI broadens executable improvement from opti-
mizing task solutions to improving the models, operators, and harnesses that generate future
solutions [Jiang et al., 2026]. Search–learning systems begin to return execution experience
to the generator, as in test-time policy updates and schemes that alternate evolutionary search
with hindsight fine-tuning [Pourcel et al., 2025, Wang et al., 2025, Yuksekgonul et al., 2026].
Related work extends improvement from candidate programs to agent and harness design [Hu
et al., 2024, Lee et al., 2026, Zhang et al., 2026a,b]. OpenMLE contributes at the interface of
these directions: verified evolutionary experience post-trains the same program-transformation
operators that subsequently govern evolutionary search, creating a meta-evolutionary coupling
between learning and inference. Relative to a public landscape that often exposes individual
or partial components of the workflow, OpenMLE is organized as an open stack spanning task
packages, sandbox execution, operator training, search, evaluation, and released model weights.
This coupling provides a concrete testbed for studying progress toward RSI in executable MLE,
rather than a claim that OpenMLE realizes general, autonomous recursive self-improvement.

## 8 Limitations and Future Work

OpenMLE provides an open path from executable environments to post-trained models and
long-horizon search, but it does not yet realize the full vision of recursive self-improvement (RSI).
We highlight five capability boundaries that we consider most consequential for closing this gap.
Richer objectives for improving the improver. OpenMLE currently learns primarily from the
measured outcome of an executed solution. This signal reveals whether a program works and how
well it scores, but it does not fully capture whether a research direction is promising, generalizable,
robust, or worth additional computation. As a result, the system is better equipped to optimize
solutions than to judge which ideas deserve to be pursued. A more capable improver will require
objectives that represent not only final performance, but also the quality of hypotheses, reasoning
processes, critiques, and transferable research strategies.
Integrating evolutionary search with general coding agents. Our present system composes
trained operators through an external evolutionary harness. This separation makes training and
search tractable, but it also bounds the range of actions and interactions the model can initiate
on its own. Moving beyond this boundary requires combining evolutionary search with general

coding agents, bringing population-based exploration and flexible agentic problem solving into a
unified framework.
Broader participation in AI development. The current environments ask an agent to improve
external machine learning artifacts. They provide a practical and verifiable testbed for meta-
evolution, but the agent participates in only a limited part of the broader AI development process.
Moving closer to recursive self-improvement requires agents to take part in a larger share of this
process, especially the improvement of language models themselves.
Evolving the evolutionary system. In OpenMLE, evolution operates primarily over candidate
solutions, while the evolutionary system itself remains largely fixed. A further step toward
recursive self-improvement is therefore to make the evolutionary system itself an object of
evolution.
Richer use of experience in node expansion. Our experience-guided node-expansion framework
remains a preliminary prototype. Although each experience card preserves a broad set of deter-
ministic metadata about a node, the current parent-selection policy uses only three factors that we
consider especially important: solution quality, parent-relative improvement, and method-family
novelty. This design demonstrates that structured experience can guide the allocation of search
budget, but it leaves much of the recorded evidence underutilized. Future work could incorporate
additional signals, while learning task-dependent rather than fixed factor weights. More broadly,
enabling the search policy itself to discover which experience signals are predictive would provide
a promising path from hand-designed experience guidance toward an evolutionary system that
improves its own search behavior.

## 9 Conclusion

We presented OpenMLE, an open full-stack technical solution for training and deploying language-
model agents that construct and iteratively improve machine learning solutions through executable
feedback. OpenMLE-Gym provides quality-gated tasks, isolated execution, and task-specific
evaluation; OpenMLE-ERL learns Draft, Improve, Debug, and Crossover transformations
through execution-grounded supervised fine-tuning and reinforcement learning; and OpenMLE-
Evo composes the same operators into long-horizon search using structured experience, multi-
factor parent selection, and operator-conditioned memory. This shared operator and execution
interface makes Frontis-MA1-35B both the product of the training stack and the variation engine
of its evolutionary harness.
The results show that model learning and search provide complementary gains. Under the
identical OpenMLE-Evo harness, Frontis-MA1-35B raises Medal Average over its Qwen3.6-
35B-A3B base from 39.39% to 60.61%, while the companion Frontis-MA1-30B reproduces the
gain on a second backbone and scale. Matched comparisons further show that OpenMLE-Evo
outperforms general-purpose coding-agent scaffolds across four frontier models and original AIRA-
Evo on Frontis-MA1-35B; combining Frontis-MA1-35B with OpenMLE-Evo-Max reaches 71.21%.
Mechanism analyses show sustained late-horizon gains from refinement and recombination, while
the matched AIRA-Evo comparison records shorter bounded contexts, lower token use, and more
validation progress per token. Controlled comparisons on the ten-task NatureBench Lite subset
provide initial evidence that both the post-trained model and the adapted search framework
transfer beyond competition-style MLE. Together with the released stack, these results establish
OpenMLE as a reproducible testbed for meta-evolution in executable AI4AI.

## 10 Authors

Junlin Yang1,2,*,†                      Che Jiang1,2,*,†                          Yu Fu1,3,*
Tianwei Luo2,*                          Can Ren1,*                                Weizhi Wang1,2,*
Kaikai Zhao2,*                          Hongyi Liu2                               Yuxin Zuo2
Yuru Wang1,2                            Yuchen Fan4                               Kai Tian1,2
Zhenzhao Yuan1,2                        Xiaojian Lin2                             Li Sheng2
Rushi Qiang5                            Guoli Jia2                                Xingtai Lv1,2
Ermo Hua2                               Dianqiao Lei1,2                           Youbang Sun2
Ning Ding2                              Bowen Zhou2                               Kaiyan Zhang1,‡

1 Horizon Research, Frontis.AI    2 Tsinghua University   3 Zhejiang University
4 Shanghai Jiao Tong University    5 Georgia Institute of Technology

* Core Contributor   † Project Leader   ‡ Corresponding Author

References
Alexis Audran-Reiss, Jordi Armengol Estape, Karen Hambardzumyan, Amar Budhiraja, Martin Josifoski,
Edan Toledo, Rishi Hazra, et al. What does it take to be a good ai research agent? studying the role of
ideation diversity. arXiv preprint arXiv:2511.15593, 2025.

Farid Bagirov, Mikhail Arkhipov, Ksenia Sycheva, Evgeniy Glukhov, and Egor Bogomolov. The best of n
worlds: Aligning reinforcement learning with best-of-n sampling via max@k optimisation. arXiv preprint
arXiv:2510.23393, 2025. URL https://arxiv.org/abs/2510.23393.

Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech
Zaremba. Openai gym. arXiv preprint arXiv:1606.01540, 2016.

Yuzhu Cai, Zexi Liu, Xinyu Zhu, Cheng Wang, and Siheng Chen. Acegrpo: Adaptive curriculum en-
hanced group relative policy optimization for autonomous machine learning engineering. arXiv preprint
arXiv:2602.07906, 2026.

Mert Cemri, Shubham Agrawal, Akshat Gupta, Shu Liu, Audrey Cheng, Qiuyang Mang, Ashwin Naren,
 Lutfi Eren Erdogan, Koushik Sen, Matei Zaharia, et al. Adaevolve: Adaptive llm driven zeroth-order
 optimization. arXiv preprint arXiv:2602.20133, 2026.

Alan Chan, Ranay Padarath, Joe Kwon, Hilary Greaves, and Markus Anderljung. Measuring AI R&D
automation. arXiv preprint arXiv:2603.03992, 2026. doi: 10.48550/arXiv.2603.03992. URL https:
//arxiv.org/abs/2603.03992.
Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace,
Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, and Aleksander Madry. Mle-bench: Evaluating
machine learning agents on machine learning engineering. arXiv preprint arXiv:2410.07095, 2024.

Guoxin Chen, Jie Chen, Lei Chen, Jiale Zhao, Fanzhe Meng, Wayne Xin Zhao, Ruihua Song, Cheng Chen,
Ji-Rong Wen, and Kai Jia. Toward autonomous long-horizon engineering for ml research. arXiv preprint
arXiv:2604.13018, 2026.

Zhipeng Chen, Xiaobo Qin, Youbin Wu, Yue Ling, Qinghao Ye, Wayne Xin Zhao, and Guang Shi. Pass@k
training for adaptively balancing exploration and exploitation of large reasoning models. arXiv preprint
arXiv:2508.10751, 2025. URL https://arxiv.org/abs/2508.10751.

Yizhou Chi, Yizhang Lin, Sirui Hong, Duyi Pan, Yaying Fei, Guanghao Mei, Bangbang Liu, Tianqi Pang,
Jacky Kwok, Ceyao Zhang, et al. Sela: Tree-search enhanced llm agents for automated machine learning.
arXiv preprint arXiv:2410.17238, 2024.

Shangheng Du, Xiangchao Yan, Dengyang Jiang, Jiakang Yuan, Yusong Hu, Xin Li, Liang He, Bo Zhang,
and Lei Bai. Automlgen: Navigating fine-grained optimization for coding agents. arXiv preprint
arXiv:2510.08511, 2025.

Shangheng Du, Xiangchao Yan, Jinxin Shi, Zongsheng Cao, Shiyang Feng, Zichen Liang, Boyuan Sun,
Tianshuo Peng, Yifan Zhou, Xin Li, Jie Zhou, Liang He, Bo Zhang, and Lei Bai. MLEvolve: A self-evolving
framework for automated machine learning algorithm discovery. arXiv preprint arXiv:2606.06473, 2026.
URL https://arxiv.org/abs/2606.06473.

Nick Erickson, Jonas Mueller, Alexander Shirkov, Hang Zhang, Pedro Larroy, Mu Li, and Alexander Smola.
Autogluon-tabular: Robust and accurate automl for structured data. arXiv preprint arXiv:2003.06505,
2020.

Daniel Eth and Tom Davidson.    Will AI R&D automation cause a software intelligence ex-
plosion?    Forethought, March 2025.   URL https://www.forethought.org/research/
will-ai-r-and-d-automation-cause-a-software-intelligence-explosion.
Haoyang Fang, Boran Han, Nick Erickson, Xiyuan Zhang, Su Zhou, Anirudh Dagar, Jiani Zhang, Ali Caner
Turkmen, Cuixiong Hu, Huzefa Rangwala, Ying Nian Wu, Bernie Wang, and George Karypis. Mlzero:
A multi-agent system for end-to-end machine learning automation. arXiv preprint arXiv:2505.13941,
2025.

Marina Favaro and Jack Clark. When ai builds itself: Our progress toward recursive self-improvement and
 its implications. Anthropic Institute, June 2026. URL https://www.anthropic.com/institute/
 recursive-self-improvement.
Matthias Feurer, Aaron Klein, Katharina Eggensperger, Jost Tobias Springenberg, Manuel Blum, and Frank
 Hutter. Efficient and robust automated machine learning. In Advances in Neural Information Processing
 Systems, volume 28, 2015.

Shubham Gandhi, Manasi Patwardhan, Lovekesh Vig, and Gautam Shroff. Budgetmlagent: A cost-effective
llm multi-agent system for automating machine learning tasks. In Proceedings of the 4th International
Conference on AI-ML Systems, pages 1–9, 2024.

Aniketh Garikaparthi, Manasi Patwardhan, and Arman Cohan. Researchgym: Evaluating language model
agents on real-world ai research. arXiv preprint arXiv:2602.15112, 2026.

Irving John Good. Speculations concerning the first ultraintelligent machine. In Franz L. Alt and Morris
 Rubinoff, editors, Advances in Computers, volume 6, pages 31–88. Academic Press, 1965. doi: 10.1016/
 S0065-2458(08)60418-0.

Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang,
Shirong Ma, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement
learning. arXiv preprint arXiv:2501.12948, 2025.

Karen Hambardzumyan, Nicolas Baldwin, Edan Toledo, Rishi Hazra, Michael Kuchnik, Bassel Al Omari,
Thomas Simon Foster, Anton Protopopov, Jean-Christophe Gagnon-Audet, Ishita Mediratta, et al. Aira_2:
Overcoming bottlenecks in ai research agents. arXiv preprint arXiv:2603.26499, 2026.

Shengran Hu, Cong Lu, and Jeff Clune.         Automated design of agentic systems.       arXiv preprint
arXiv:2408.08435, 2024.

Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. Mlagentbench: Evaluating language agents on
machine learning experimentation. arXiv preprint arXiv:2310.03302, 2023.

InternScience. Mlevolve: An agentic machine learning engineering system for kaggle-style competitions.
 https://github.com/InternScience/MLEvolve, 2026. GitHub repository.
Che Jiang, Jincheng Zhong, Yu Fu, Kai Tian, Junlin Yang, et al. Self-improving agents in the era of
experience: A survey of self- to meta-evolution. OpenReview Archive, 2026. URL https://openreview.
net/forum?id=IUltZSgLMm.
Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxiang
Wu. Aide: Ai-driven exploration in the space of code. arXiv preprint arXiv:2502.13138, 2025.

Jiajie Jin, Yuyang Hu, Kai Qiu, Qi Dai, Chong Luo, Guanting Dong, Xiaoxi Li, Tong Zhao, Xiaolong Ma,
 Gongrui Zhang, Zhirong Wu, Bei Liu, Zhengyuan Yang, Linjie Li, Lijuan Wang, Hongjin Qian, Yutao
 Zhu, and Zhicheng Dou. Toward generalist autonomous research via hypothesis-tree refinement. arXiv
 preprint arXiv:2606.11926, 2026. URL https://arxiv.org/abs/2606.11926.

Liqiang Jing, Zhehui Huang, Xiaoyang Wang, Wenlin Yao, Wenhao Yu, Kaixin Ma, Hongming Zhang, Xinya
 Du, and Dong Yu. Dsbench: How far are data science agents from becoming data science experts? arXiv
 preprint arXiv:2409.07703, 2024.

Andrej Karpathy. autoresearch: AI agents running research on single-GPU nanochat training automatically.
GitHub repository, 2026. URL https://github.com/karpathy/autoresearch.

Yongbin Kim, Yashar Talebirad, and Osmar R. Zaiane. Why solve it twice? hierarchical accumulation
of skills for transfer-efficient ml engineering. arXiv preprint arXiv:2606.30911, 2026. URL https:
//arxiv.org/abs/2606.30911.
Robert Tjarko Lange, Yuki Imajuku, and Edoardo Cetin. Shinkaevolve: Towards open-ended and sample-
efficient program evolution. arXiv preprint arXiv:2509.19349, 2025.

Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, and Chelsea Finn. Meta-harness:
End-to-end optimization of model harnesses. arXiv preprint arXiv:2603.28052, 2026.

Annan Li, Chufan Wu, Zengle Ge, Yee Hin Chong, Zhinan Hou, Lizhe Cao, Cheng Ju, Jianmin Wu, Huaiming
Li, Haobo Zhang, Shenghao Feng, Mo Zhao, Fengzhi Qiu, Rui Yang, Mengmeng Zhang, Wenyi Zhu,
Yingying Sun, Quan Sun, Shunhao Yan, Danyu Liu, Dawei Yin, and Dou Shen. The fm agent. arXiv
preprint arXiv:2510.26144, 2025a. URL https://arxiv.org/abs/2510.26144.

Yujiang Li, Zhenyu Hou, Xiaohan Jia, Zihan Luo, Zhilei Bei, Rui Lu, Hong Huang, Jie Tang, and Yuxiao
Dong. Mle-rl: Reinforcement learning for self-improvement in machine learning agents. OpenReview
preprint, 2025b. URL https://openreview.net/forum?id=nElqyHPHAz.

Ziming Li, Qianbo Zang, David Ma, Jiawei Guo, Tianyu Zheng, Minghao Liu, Xinyao Niu, Yue Wang, Jian
Yang, Jiaheng Liu, Wanjun Zhong, Wangchunshu Zhou, Stephen Huang, and Ge Zhang. Autokaggle: A
multi-agent framework for autonomous data science competitions. In ICLR 2025 Third Workshop on
Deep Learning for Code, 2025c. URL https://openreview.net/forum?id=2SBev23pkd.

Zexi Liu, Yuzhu Cai, Xinyu Zhu, Yujie Zheng, Runkun Chen, Ying Wen, Yanfeng Wang, Siheng Chen, et al. Ml-
master: Towards ai-for-ai via integration of exploration and reasoning. arXiv preprint arXiv:2506.16499,
2025a.

Zexi Liu, Jingyi Chai, Xinyu Zhu, Shuo Tang, Rui Ye, Bo Zhang, Lei Bai, and Siheng Chen. Ml-agent:
Reinforcing llm agents for autonomous machine learning engineering. arXiv preprint arXiv:2505.23723,
2025b.

Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The AI scientist:
Towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292, 2024. doi:
10.48550/arXiv.2408.06292. URL https://arxiv.org/abs/2408.06292.

Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka, Alberto Pepe, Alexis
 Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun, et al. Airs-bench: a suite of tasks
 for frontier ai research science agents. arXiv preprint arXiv:2602.06855, 2026.

Bohan Lyu, Yucheng Yang, Siqiao Huang, Jiaru Zhang, Qixin Xu, Xinghan Li, Xinyang Han, Yicheng Zhang,
Huaqing Zhang, Runhan Huang, Kaicheng Yang, Zitao Chen, Wentao Guo, Junlin Yang, Xinyue Ai,
Wenhao Chai, Yadi Cao, Ziran Yang, Kun Wang, Dapeng Jiang, Huan-ang Gao, Shange Tang, Chengshuai
Shi, Simon S. Du, Max Simchowitz, Jiantao Jiao, Dawn Song, and Chi Jin. MLS-Bench: A holistic and
rigorous assessment of AI systems on building better AI. arXiv preprint arXiv:2605.08678, 2026. doi:
10.48550/arXiv.2605.08678. URL https://arxiv.org/abs/2605.08678.

MiniMax. MiniMax M2.7: Early Echoes of Self-Evolution, March 2026. URL https://www.minimax.
io/news/minimax-m27-en. Accessed: 2026-05-05.
Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Jinwoo Shin, Sercan O. Arik, and Tomas Pfister. Mle-star:
Machine learning engineering agent via search and targeted refinement. arXiv preprint arXiv:2506.15692,
2025.

Deepak Nathani, Lovish Madaan, Nicholas Roberts, Nikolay Bashlykov, Ajay Menon, Vincent Moens, Amar
Budhiraja, Despoina Magka, et al. Mlgym: A new framework and benchmark for advancing ai research
agents. arXiv preprint arXiv:2502.14499, 2025.

Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner,
Sergey Shirobokov, Borislav Kozlovskii, Francisco JR Ruiz, Abbas Mehrabian, et al. Alphaevolve: A
coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131, 2025.

Junhyuk Oh, Gregory Farquhar, Iurii Kemaev, Dan A. Calian, Matteo Hessel, Luisa Zintgraf, Satinder Singh,
Hado van Hasselt, and David Silver. Discovering state-of-the-art reinforcement learning algorithms.
Nature, 648:312–319, 2025. doi: 10.1038/s41586-025-09761-x. URL https://www.nature.com/
articles/s41586-025-09761-x.
Randal S. Olson, Nathan Bartley, Ryan J. Urbanowicz, and Jason H. Moore. Evaluation of a tree-based
pipeline optimization tool for automating data science. In Proceedings of the Genetic and Evolutionary
Computation Conference, pages 485–492, 2016.

Yixin Ou, Yujie Luo, Jingsheng Zheng, Lanning Wei, Zhuoyun Yu, Shuofei Qiao, Jintian Zhang, Da Zheng,
Yuren Mao, Yunjun Gao, et al. Automind: Adaptive knowledgeable agent for automated data science.
 arXiv preprint arXiv:2506.10974, 2025.

Ruotian Peng, Yi Ren, Zhouliang Yu, Weiyang Liu, and Yandong Wen. Simko: Simple pass@k policy
optimization. arXiv preprint arXiv:2510.14807, 2025. URL https://arxiv.org/abs/2510.14807.

Julien Pourcel, Cédric Colas, and Pierre-Yves Oudeyer. Self-improving language models for evolutionary
program synthesis: A case study on arc-agi. arXiv preprint arXiv:2507.14172, 2025.

Rushi Qiang, Yuchen Zhuang, Yinghao Li, Dingu Sagar V K, Rongzhi Zhang, Changhao Li, Ian Shu-Hei
Wong, Sherry Yang, Percy Liang, Chao Zhang, and Bo Dai. Mle-dojo: Interactive environments for
empowering llm agents in machine learning engineering. arXiv preprint arXiv:2505.07782, 2025a.

Rushi Qiang, Yuchen Zhuang, Anikait Singh, Percy Liang, Chao Zhang, Sherry Yang, and Bo Dai. Mle-smith:
Scaling mle tasks with automated multi-agent pipeline. arXiv preprint arXiv:2510.07307, 2025b.

Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Shira Eisenberg, Karina Nguyen, Matthias Bethge, and
Maksym Andriushchenko. Posttrainbench: Can llm agents automate llm post-training? arXiv preprint
arXiv:2603.08640, 2026.

Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M Pawan
Kumar, Emilien Dupont, Francisco JR Ruiz, Jordan S Ellenberg, Pengming Wang, Omar Fawzi, et al.
Mathematical discoveries from program search with large language models. Nature, 625(7995):468–475,
2024.

Jürgen Schmidhuber. Gödel machines: Self-referential universal problem solvers making provably optimal
self-improvements. arXiv preprint cs/0309048, 2003. URL https://arxiv.org/abs/cs/0309048.

Rulin Shao, Akari Asai, Shannon Zejiang Shen, Hamish Ivison, Varsha Kishore, Jingming Zhuo, Xinran
Zhao, Molly Park, Samuel G Finlayson, David Sontag, et al. Dr tulu: Reinforcement learning with
evolving rubrics for deep research. arXiv preprint arXiv:2511.19399, 2025.

Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, Y. K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in
open language models. arXiv preprint arXiv:2402.03300, 2024.

Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan
Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, and Tejal Patwardhan.
Paperbench: Evaluating ai’s ability to replicate ai research. arXiv preprint arXiv:2504.01848, 2025.

Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao,
Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. arXiv
preprint arXiv:2501.12599, 2025.

Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, SH Cai, Yuan Cao, Y Charles, HS Che, Cheng Chen,
Guanduo Chen, et al. Kimi k2. 5: Visual agentic intelligence. arXiv preprint arXiv:2602.02276, 2026.

Chris Thornton, Frank Hutter, Holger H. Hoos, and Kevin Leyton-Brown. Auto-weka: Combined selection
and hyperparameter optimization of classification algorithms. In Proceedings of the 19th ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, pages 847–855, 2013.

Edan Toledo, Karen Hambardzumyan, Martin Josifoski, Rishi Hazra, Nicolas Baldwin, Alexis Audran-Reiss,
Michael Kuchnik, Despoina Magka, et al. Ai research agents for machine learning: Search, exploration,
and generalization in mle-bench. arXiv preprint arXiv:2507.02554, 2025.

Yuxuan Tong, Xiwen Zhang, Rui Wang, Ruidong Wu, and Junxian He. DART-Math: Difficulty-aware
rejection tuning for mathematical problem-solving. Advances in Neural Information Processing Systems,
37, 2024.

Patara Trirat, Wonyong Jeong, and Sung Ju Hwang. Automl-agent: A multi-agent llm framework for
full-pipeline automl. arXiv preprint arXiv:2410.02958, 2024.

Christian Walder and Deep Karkhanis. Pass@k policy optimization: Solving harder reinforcement learning
problems. arXiv preprint arXiv:2505.15201, 2025. URL https://arxiv.org/abs/2505.15201.

Yiping Wang, Shao-Rong Su, Zhiyuan Zeng, Eva Xu, Liliang Ren, Xinyu Yang, Zeyi Huang, Xuehai He,
Luyao Ma, Baolin Peng, Hao Cheng, Pengcheng He, Weizhu Chen, Shuohang Wang, Simon Shaolei Du,
and Yelong Shen. Thetaevolve: Test-time learning on open problems. arXiv preprint arXiv:2511.23473,
2025.

Yuru Wang, Lejun Cheng, Yuxin Zuo, Sihang Zeng, Bingxiang He, Che Jiang, Junlin Yang, Yuchong
Wang, Kaikai Zhao, Weifeng Huang, Kai Tian, Zhenzhao Yuan, Jincheng Zhong, Weizhi Wang, Ning
Ding, Bowen Zhou, and Kaiyan Zhang. Naturebench: Can coding agents match the published sota of
nature-family papers? arXiv preprint arXiv:2606.24530, 2026.

Hjalmar Wijk, Tao Roa Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan,
Michael Chen, Joshua M. Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola
Jurkovic, Megan Kinniment, Aron Lajko, Seraphina Nix, Lucas Jun Koba Sato, William Saunders, Maksym
Taran, Ben West, and Elizabeth Barnes. RE-Bench: Evaluating frontier AI R&D capabilities of language
model agents against human experts. In Proceedings of the 42nd International Conference on Machine
Learning, volume 267 of Proceedings of Machine Learning Research, pages 66772–66832. PMLR, 2025.
URL https://proceedings.mlr.press/v267/wijk25a.html.

Zhiheng Xi, Yiwen Ding, Wenxiang Chen, Boyang Hong, Honglin Guo, Junzhe Wang, Dingwen Yang,
Chenyang Liao, Xin Guo, Wei He, et al. Agentgym: Evolving large language model-based agents across
diverse environments. arXiv preprint arXiv:2406.04151, 2024.

Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune,
and David Ha. The AI scientist-v2: Workshop-level automated scientific discovery via agentic tree
search. arXiv preprint arXiv:2504.08066, 2025. doi: 10.48550/arXiv.2504.08066. URL https:
//arxiv.org/abs/2504.08066.
Sherry Yang, Joy He-Yueya, and Percy Liang. Reinforcement learning for machine learning engineering
agents. arXiv preprint arXiv:2509.01684, 2025a.

Xu Yang, Xiao Yang, Shikai Fang, Yifei Zhang, Jian Wang, Bowen Xian, Qizheng Li, Jingyuan Li, Minrui Xu,
Yuante Li, et al. R&d-agent: An llm-agent framework towards autonomous data science. arXiv preprint
arXiv:2505.14738, 2025b.

Haotian Ye, Haowei Lin, Jingyi Tang, Yizhen Luo, Caiyin Yang, Chang Su, Rahul Thapa, Rui Yang, Ruihua
Liu, Zeyu Li, et al. Evaluation-driven scaling for scientific discovery. arXiv preprint arXiv:2604.19341,
2026.

Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao Huang. Does
reinforcement learning really incentivize reasoning capacity in llms beyond the base model? arXiv
preprint arXiv:2504.13837, 2025. URL https://arxiv.org/abs/2504.13837.

Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz,
 Yejin Choi, James Zou, Carlos Guestrin, et al. Learning to discover at test time. arXiv preprint
 arXiv:2601.16175, 2026.

Aohan Zeng, Xin Lv, Zhenyu Hou, Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin, Chendi Ge, Chenghua
Huang, Chengxing Xie, et al. Glm-5: from vibe coding to agentic engineering. arXiv preprint
arXiv:2602.15763, 2026.

Zhiyuan Zeng, Hamish Ivison, Yiping Wang, Lifan Yuan, Shuyue Stella Li, Zhuorui Ye, Siting Li, Jacqueline
He, Runlong Zhou, Tong Chen, Chenyang Zhao, Yulia Tsvetkov, Simon Shaolei Du, Natasha Jaques, Hao
Peng, Pang Wei Koh, and Hannaneh Hajishirzi. Rlve: Scaling up reinforcement learning for language
models with adaptive verifiable environments. arXiv preprint arXiv:2511.07317, 2025.

Jenny Zhang, Bingchen Zhao, Wannan Yang, Jakob Foerster, Jeff Clune, Minqi Jiang, Sam Devlin, and
Tatiana Shavrina. Hyperagents. arXiv preprint arXiv:2603.19461, 2026a.

Jiayi Zhang, Yongfeng Gu, Jianhao Ruan, Maojia Song, Yiran Peng, Zhiguang Han, Jinyu Xiang, Zhitao
 Wang, Caiyin Yang, Yixi Ouyang, Bang Liu, Chenglin Wu, and Yuyu Luo. Harnessing agentic evolution.
 arXiv preprint arXiv:2605.13821, 2026b.

Ruiyi Zhang, Peijia Qin, Qi Cao, Li Zhang, and Pengtao Xie. Aibuildai: An ai agent for automatically building
ai models. arXiv preprint arXiv:2604.14455, 2026c. URL https://arxiv.org/abs/2604.14455.

Shaolei Zhang, Ju Fan, Meihao Fan, Guoliang Li, and Xiaoyong Du. Deepanalyze: Agentic large language
models for autonomous data science. arXiv preprint arXiv:2510.16872, 2025a.

Yunxiang Zhang, Muhammad Khalifa, Shitanshu Bhushan, Grant D. Murphy, Lajanugen Logeswaran,
Jaekyeom Kim, Moontae Lee, Honglak Lee, and Lu Wang. Mlrc-bench: Can language agents solve
machine learning research challenges? arXiv preprint arXiv:2504.09702, 2025b.

Yuhang Zhou, Lizhu Zhang, Yifan Wu, Jiayi Liu, Xiangjun Fan, Zhuokai Zhao, and Hong Yan. Synthetic
sandbox for training machine learning engineering agents. arXiv preprint arXiv:2604.04872, 2026.

Xinyu Zhu, Yuzhu Cai, Zexi Liu, Cheng Wang, Fengyang Li, Wenkai Jin, Wanxu Liu, Zehao Bing, Bingyang
Zheng, Jingyi Chai, Shuo Tang, Rui Ye, Yuwen Du, Xianghe Pang, Yaxin Du, Tingjia Miao, Yuzhi Zhang,
Ruoxue Liao, Zhaohan Ding, Linfeng Zhang, Yanfeng Wang, Weinan E, and Siheng Chen. Evomaster: A
foundational evolving agent framework for agentic science at scale. arXiv preprint arXiv:2604.17406,
2026a. URL https://arxiv.org/abs/2604.17406.

Xinyu Zhu, Yuzhu Cai, Zexi Liu, Bingyang Zheng, Cheng Wang, Rui Ye, Jiaao Chen, Hanrui Wang, Wei-
Chen Wang, Yuzhi Zhang, et al. Toward ultra-long-horizon agentic science: Cognitive accumulation for
machine learning engineering. arXiv preprint arXiv:2601.10402, 2026b.

## A OpenMLE-Gym Details

### A.1. Task Construction and Selection

This appendix details the construction, validation, and selection mechanisms summarized in
Section 3. All three task sources follow the shared executable contract defined there; we focus
below on the automated competition branch and its post-construction gates.
Competition-construction state machine. The builder consumes the candidate slugs remaining
after upstream filtering. Independent competitions can be dispatched concurrently, while each
competition follows an ordered state machine so that downstream stages run only after their
prerequisites succeed.
For each slug, the pipeline downloads and recursively unpacks the competition archive, preserves
the source assets, and retrieves the pre-computed competition overview and dataset description. A
tool-assisted file-perception stage then enumerates the local tree, probes tabular files for structural
summaries and sampled rows, and reads textual documentation. The resulting inventory and
competition metadata jointly ground the generated task description, avoiding reliance on either
web metadata or filenames alone.
Executable construction and validation. Conditioned on the generated description, the pipeline
produces and executes prepare.py to create deterministic train/test splits, copy associated
modality files, expose participant-visible inputs, and isolate held-out answers. Execution success
alone is insufficient: the builder checks for the task description, training data, test inputs, sample
submission, and private test answers before accepting the package. A failed attempt clears
its partial processed outputs and returns the execution error to the next generation attempt,
preventing malformed intermediate state from being reused.
After preparation succeeds, the pipeline generates the task-specific metric.py from the task de-
scription together with samples of the submission and private-answer schemas. Metric generation
and metric validation are separate stages. The latter dynamically loads the generated evaluator
and scores data/public/sample_submission.csv against data/private/test_answer.
csv; import errors, execution errors, missing inputs, or a missing score fail this gate before
semantic assessment.
Raw assets may remain in raw/. For storage-reduced packages, the generated file inventory is
first preserved as raw.txt before the raw directory is removed. The quality record consumes
this inventory when available; otherwise, raw-data use is assessed from the presence of source
assets, prepare.py, and the resulting public/private data.
Metadata profiling and semantic quality assessment. Post-construction profiling annotates
modality and task type from the task description, measures raw and processed data size, classifies
the expected CPU/GPU requirement, and records metric-validation output. These stages can
process task chunks concurrently but restore the original task order when writing the aggregate
metadata.
The quality evaluator first inspects package structure and executes the metric smoke test. Missing
critical files or failed metric execution deterministically yield not_recommended. For packages
that pass these hard gates, the semantic judge receives the description, prepare.py, train/test
sizes, processed-data size, auxiliary file types, sampled public and held-out rows, available
raw inventory, and metric result. It returns scores for task validity, data sufficiency, raw-data
usage, task complexity, and data quality, together with one of recommended, conditional,
or not_recommended. The evaluator records these judgments without mutating the package
collection; final aggregation admits only metric-valid tasks with the strict recommended decision.
Metadata accounting. The distribution plots in Figure 4 use mutually exclusive normalized

 Task Package Construction
                                                                                                        retry with feedback on failure

                                                                                     LLM                LLM                              LLM

                                                     Fetch Description
   Input Kaggle       Preprocessing                                                                            Generate
                                                                                      Construct                                            Generate
       Slug                                                                              Task                 prepare.py                 Supplemental
                       Download data, unzip,                     Local File           Description                                          Materials
     e.g., AI4Code    build file-tree metadata       Tool Use
                                                                 Inventory                              standardizing raw file tree

                     Data           tree.txt     web_info.json      file_info.txt     description.txt
                     Files                                                                                                                metric.py
                                                                                                                   Standardized
                                                                                                                    Data Files
                                                                                                                                         overview.csv
                                                                                                                                              ...
                                                                                    update

                      standardize

Figure 20 | Automated competition task construction. Competition metadata and local-file
evidence ground package generation; execution feedback revises failed preparation before metric
validation and semantic gating.

groups. Tasks containing multiple modalities are assigned to Multimodal, compound task labels
to Multitask, and rare labels to Other. Package size is measured from constructed task contents.

### A.2. OpenMLE-Gym Execution Infrastructure

Architecture. Figure 21 expands the execution backend summarized in Section 3.4, exposing
the API boundary and the separation among scheduling, isolated workers, shared job state, and
returned feedback.
Representative feedback cases.
Table 3 grounds the six feedback modes summarized in Section 3.4 with representative jobs. Each
row connects a concrete trigger to returned fields and their usable signal; the following transcript
traces one failure end to end.
End-to-end transcript.
The following transcript traces a failed GPU job from the submitted program through execution,
the structured result, and the diagnostic traceback needed to repair it.
Step 1: Agent request. The agent submits a generated Python program together with the task
data directory and resource constraints. In this job, the task is brain-tumor MRI classification and
the public data directory is exposed to the program through DATA_DIR.

 name: brain-tumor-detection-mri@1
 code: <candidate Python program>
 data_dir: <task-public-data-dir>
 resource_type: gpu
 gpu_count: 1
 timeout: 3600

                                                                         feedback record

   Agent Client                     Controller and Scheduler                                Elastic Worker Cluster                      Structured Feedback

       job input                        Nginx gateway                                  Each worker is an isolated Docker runtime.
                                                                                                                                             score

       candidate code                   FastAPI: job API                             CPU/GPU                                                 status
                                                                                      server 1   worker 1   worker 2   ···   worker K

                        request
                         (API)
                                                                                                                                             logs
                                        Redis: queues & states
       task context                                                                  CPU/GPU
                                                                                      server 2   worker 1   worker 2   ···   worker K
                                                                                                                                             error type
                                        Job dispatcher

       resource                                                                                                                              runtime metadata
       constraints
                                        PostgreSQL: persistent storage               CPU/GPU
                                                                                      server N   worker 1   worker 2   ···   worker K

                                                                                                                                             workspace artifacts

                                                                           Shared NFS
                                                                           job workspace

Figure 21 | OpenMLE-Gym execution-backend architecture. Agent requests are dispatched to
CPU/GPU Docker workers, which execute candidate programs against task data and evaluators
and return structured feedback.

Table 3 | Representative coverage of sandbox feedback modes from real job logs. Each row
abstracts one real job into its trigger, returned feedback fields, and usable signal for training or
evaluation.

Case                              Trigger, feedback, and usable signal

Success                           Trigger: candidate finishes training and writes submission.csv.
                                  Feedback: completed; score 0.9991; logs; runtime metadata; validated artifact.
                                  Signal: valid scored trajectory.
Runtime error                     Trigger: code calls an unsupported PyTorch API argument.
                                  Feedback: code_execution_error; null score; exit code; traceback.
                                  Signal: executable code defect before scoring.
Missing code                      Trigger: submitted main.py is empty.
                                  Feedback: code_missing; null score; immediate pre-execution diagnostic.
                                  Signal: invalid request filtered before worker execution.
Missing submission                Trigger: process exits successfully but does not write submission.csv.
                                  Feedback: submission_missing; null score; missing-artifact log.
                                  Signal: distinguishes process success from valid submission.
Scoring failed                    Trigger: submitted file violates the evaluator schema.
                                  Feedback: scoring_failed; null score; evaluator-side validation error.
                                  Signal: invalid artifact separated from low task performance.
Timeout                           Trigger: long-running training exceeds the execution budget.
                                  Feedback: timeout; null score; timeout metadata; partial stdout.
                                  Signal: resource or algorithmic inefficiency with retained debugging evidence.

The server materializes the submitted code as main.py inside the job workspace. The excerpt
below shows the part that later triggers the runtime error; unrelated dataset loading, model
definition, and training code is omitted.

 # Initialize model

 device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
 model = BrainTumorClassifier(
   model_name="efficientnet_b0",
   pretrained=True,
   dropout=0.3,
 ).to(device)

 # Loss function with label smoothing
 criterion = nn.BCEWithLogitsLoss(label_smoothing=0.1)

 optimizer = optim.AdamW(model.parameters(), lr=1e-4, weight_decay=1e-4)
 ...

Step 2: Sandbox execution. The control server materializes the job workspace, assigns an idle
GPU worker, and runs the candidate inside an isolated Docker worker. The actual command binds
the task data path into the process environment, captures stdout/stderr into the job workspace,
and preserves the process exit code.

 export DATA_DIR=<task-public-data-dir>
 python <sandbox-job-workspace>/code/main.py
 2>&1 | tee -a <sandbox-job-workspace>/sandbox_stdout.log

Step 3: Sandbox feedback. The returned record preserves machine-readable status, runtime,
and artifact fields alongside the human-readable log. Because the program fails during execution,
the evaluator is not invoked and the score remains null.

 job_id: job_<id>
 score: null
 status: failed
 logs:
 stdout_stderr: <sandbox-job-workspace>/sandbox_stdout.log
 diagnostic_excerpt: TypeError in BCEWithLogitsLoss(...)
 error_type: code_execution_error
 runtime_metadata:
 resource_type: gpu
 exit_code: 1
 shell_runtime: 11.88s
 evaluation: skipped because code execution failed
 workspace_artifacts:
 workspace: <sandbox-job-workspace>
 submission: missing
 preserved_files: code/main.py, sandbox_stdout.log

Step 4: Diagnostic log. The key diagnostic is the traceback, which points directly to the generated
line that is incompatible with the installed PyTorch API.

 Traceback (most recent call last):
 File "<sandbox-job-workspace>/code/main.py", line 151, in <module>
   criterion = nn.BCEWithLogitsLoss(label_smoothing=0.1)
 TypeError: BCEWithLogitsLoss.__init__() got an unexpected keyword argument
 'label_smoothing'

Together, the status, error, runtime, artifact, and traceback fields localize the failure before
evaluation and provide concrete evidence for the next repair action.

## B OpenMLE-ERL Details

### B.1. SFT Data Generation

Parallel Path Sampling. The teachers first generate multiple independent Draft solutions
for each standardized task, and every candidate is executed in the corresponding task sandbox.
The first collection batch uses GLM-4.7. Among candidates with valid execution scores for the
same task, we remove solutions with duplicate scores, rank the remaining candidates by score,
and retain at most the Top-4. The released corpus contains 11,519 examples from this batch.
The second batch uses both GLM-4.7 and Qwen3-30B-A3B-Thinking-2507. After execution and
output-length screening, candidates from both teachers are jointly ranked within each task: a
GLM-4.7 candidate is retained when it falls in the joint Top-4, whereas a Qwen candidate is
retained only when it ranks first overall. Consequently, each task still contributes at most four
examples rather than four GLM candidates plus an additional Qwen candidate. After corpus-level
assembly, the released corpus contains 5,726 examples from this batch, comprising 5,075 GLM-4.7
and 651 Qwen examples. The two batches contribute 17,245 full-response examples in total.
Evolutionary Path Sampling. Complete solutions expose final programs but do not directly
supervise how execution feedback should be used to revise an existing solution. We therefore
use GLM-4.7 to drive AIRA-Evo searches with Draft, Improve, Crossover, and Debug,
producing search trees with parent relations, program versions, execution feedback, and task
scores. A local segment begins at a Draft, Improve, or Crossover node and follows its
consecutive Debug descendants along true parent–child edges; the segment ends when a branch
reaches another Draft, Improve, or Crossover node. A Draft segment must end with a
positive score, an Improve segment must outperform its parent program, and a Crossover
segment must outperform the better of its two parents. Retained endpoints must additionally
attain a bronze, silver, or gold level.
Single-step segments whose roots are themselves medal-level endpoints are retained directly.
For multi-step segments, DeepSeek-V4-Pro reads each complete segment—including the task
constraints, parent code, endpoint code, adjacent code changes, and stepwise execution feedback—
and determines whether the strategy, program structure, or error repair introduced by each step is
inherited by later steps and contributes to the final effective solution. After corpus-level assembly,
the evolutionary path contributes 9,014 trajectory-step examples to the released corpus.
Assembly and final corpus distribution. We normalize complete solutions and trajectory steps
into the same system–user–assistant message structure and perform exact deduplication over the
normalized full messages content. We then apply the target model’s chat template to the full
message sequence and exclude examples longer than 32,768 tokens. The released SFT corpus
contains 26,259 training examples.
Of the released corpus, 17,245 full responses account for 65.7%, and 9,014 trajectory steps
account for 34.3%. At the atomic-operator level, Draft, Improve, Crossover, and Debug
contribute 19,436, 1,741, 742, and 4,340 examples, respectively, corresponding to 74.0%, 6.6%,
2.8%, and 16.5%. The median full-message lengths are 8,407 tokens for full responses and
14,051 tokens for trajectory steps; the latter are longer because they include parent programs,
execution feedback, and local search context.
Prompt for trajectory-step selection. The annotator follows a causal-inheritance criterion: a
step is retained only when its core strategy, necessary intermediate state, or critical error repair
is inherited by later steps and makes a concrete contribution to the segment endpoint. Cosmetic
edits, blind retries, changes that merely reduce training scale to avoid resource limits, and failed
environment modifications or external-network accesses are discarded. We use DeepSeek-V4-Pro
with temperature 0 and a maximum output length of 4,096 tokens, requiring a fixed JSON schema

(a) Supervision Type                     (b) Atomic Operator                                                      (c) Full-Message Length
                                                                                                                                                                          Full responses
                                                                                                                                                                          Trajectory steps
                                                   16.5%

                                                                                Examples within type (%)
  34.3%                                                                                                                                                            Response median 8.4k
                                            2.8%                                                                                                                  Trajectory median 14.1k

               26,259                      6.6%         26,259
              examples                                 examples
                               65.7%
                                                                  74.0%

          Full responses - 17,245           Draft - 19,436    Crossover - 742                                       k      k      2k        k         k        k           k        k
                                                                                                                 0-4    4-8    8-1       -16       -20      -24        -28       -32
          Trajectory steps - 9,014          Improve - 1,741   Debug - 4,340                                                            12        16       20         24        28
                                                                                                                                                Tokens

Figure 22 | Distribution of the final SFT corpus. (a) Relative proportions of full-response and
trajectory-step supervision among the 26,259 training examples. (b) Distribution of the four
atomic operators. (c) Full-message length distributions for the two supervision types; each bar
reports the percentage within its corresponding supervision type.

that accounts for every input step. The production system prompt is reproduced below.

# Role
You are a machine learning SFT data annotation expert, responsible for selecting high-quality
steps from Agent search-tree trajectory segments for supervised fine-tuning training.

# Core Objective
Inspect a given candidate segment and determine which steps should be kept as SFT training
examples and which steps should be discarded.

# Input Structure and Usage Instructions
You will receive the following five parts of data. You must strictly reason according to a
“causal chain” perspective:

1. TASK_SYSTEM_PROMPT: The original environment and constraint instructions of the task.
 Usage: Used to determine whether any step in the segment violates hard constraints (such as
 forbidden internet downloads, forbidden environment modifications, etc.).

2. TASK_USER_PROMPT: The original problem description of the task.
 Usage: Used to understand the task objective and assist in determining whether the Draft
 step builds a reasonable framework aligned with the task.

3. PARENT_CODES: Baseline code before the root step.
 Usage: Provides a reference baseline for Improve and crossover (which has two parent codes)
 steps, used to evaluate the substantive nature of modifications.
 Note: Draft starts from scratch and does not have PARENT_CODES.

4. FINAL_SOLUTION_CODE: The endpoint code of this segment (the most important semantic
anchor).
 Core usage: It represents the final effective direction adopted by this segment. When
 judging whether a step is inherited, do not check whether the endpoint code literally
 contains the step’s code. Instead, evaluate whether the “core problem solved” or the “core
 strategy proposed” by the step remains a necessary component of the final solution.

5. TRAJECTORY_STEPS: The list of steps to be evaluated (JSON array).
 The first element of this array is the root step (operator is Draft, Improve, or
 Crossover), and all subsequent elements are continuous Debug steps.
 Each step contains the following fields:
 - step_index: The unique identifier of the step.
 - operator: The operator type, taking values draft, improve, crossover, or debug.
 - code content: For root steps (Draft/Improve/Crossover), the code field contains the full
 code generated at that step. For Debug steps, a full_code_diff field is provided in unified
 diff format, but it fully contains the complete updated source code after modification
 without omission or truncation.
 - feedback: Execution feedback after running the step, including status (success/failure),
 error messages, or validation scores.
 During evaluation, you must reconstruct the actual code changes from code or full_code_diff
 and judge the value of each step.

# Special Error Handling Principle

If the feedback of a step shows that its failure belongs to the following category, then the
next step (which must be a Debug step) must be marked as keep_for_sft: false.

This error refers to a mismatch in C-extension binary interfaces or precompiled library
versions. Typical patterns include:
- ValueError: numpy.dtype size changed, may indicate binary incompatibility. Expected X from C
header, got Y from PyObject
- ImportError: this version of pandas is incompatible with numpy < X.X

# Global Hard Filtering Rules
If any of the following behaviors appear in the code, the step must be unconditionally marked
as keep_for_sft: false, regardless of how strong the algorithm is:

- Environment modification: calling pip install, conda install, subprocess-based installation,
modifying sys.path, overriding installed package versions, or using os.system for system-level
commands unrelated to data processing.
- External resource downloading caused failure: feedback explicitly shows that the step
attempted to download pretrained models, datasets, or external resources using wget, curl,
requests.get, urllib.request, torch.hub.load (non-cached),
transformers.AutoModel.from_pretrained (first-time download), and the failure is caused by
download failure, timeout, permission denial, or offline environment restriction.
- Network access attempts caused failure: feedback explicitly shows that the step attempted to
access external servers, non-local network addresses, or external services, and failed due to
connection errors, timeouts, DNS/SSL/HTTP failures, or authentication issues.

# Golden Principle: Causal Inheritance Chain

Before applying operator-specific rules, perform the following reasoning steps:

1. Distinguish “Goal” vs “Method”:
 If a step proposes a specific method (e.g., using LightGBM instead of NN to address
 overfitting), while the endpoint retains the goal “solve overfitting” but uses a completely
 different method (e.g., HistGradientBoosting), then the specific method is NOT considered
 inherited.

 If the endpoint preserves the core mechanism introduced by the step (e.g., a Debug step
 fixes sequence alignment via truncation, and the endpoint still relies on sequence
 alignment even if truncation strategy is adjusted), then it is considered inherited.

2. Identify “Necessary Intermediate States”:
 If a step fixes a blocking execution error, and all subsequent steps depend on the
 corrected state to function, then this step MUST be marked as kept.

 If a step only performs performance tuning (e.g., reducing folds, epochs, or iterations),
 and is fully replaced by another tuning strategy later, then it should be discarded.

3. Distinguish “Strategy Contribution” vs “Implementation Fix”:
 Root steps (Draft / Improve / Crossover) are evaluated based on whether they introduce a
 core strategy. If such a step initially fails due to implementation bugs but is later fixed
 by Debug steps and preserved in the endpoint, it should still be kept. Debug steps are
 evaluated separately based on their fix contribution.

# Operator-Specific Evaluation Rules (must follow causal inheritance chain)

## Draft Rules
Keep condition: The step builds an initial solution framework aligned with the task
description (including key components such as data loading, feature processing, model
training, validation, inference, and submission generation), and this framework provides the
main starting direction for the endpoint solution.

Drop conditions:
- The framework is hollow (only template code without task-specific logic).
- The core algorithmic direction is completely abandoned in the endpoint code (e.g., switching
from CV object detection to NLP classification).
- Note: Draft must NOT be dropped due to later performance optimizations such as acceleration
or library replacement.

## Improve Rules
Keep condition: Introduces a substantive strategy targeting specific issues (such as
overfitting, feature insufficiency, or model bias), and the core idea is still preserved in
the endpoint code (e.g., switching from MLP to tree-based models to solve overfitting, where
tree-based models are still used in the endpoint, even if implementation differs).

Drop conditions:

- Non-substantive modifications (variable renaming, comments, logging, formatting).
- Pure hyperparameter tuning without strategy-level change.
- The improvement direction is explicitly removed or reverted in the endpoint.
- The endpoint only preserves a high-level theme (e.g., still ML or still tree-based models)
but does NOT preserve the specific method introduced by this step.

Important:
- Evaluate Improve based on whether the concrete method is preserved, not whether the abstract
goal is consistent.
- If Improve initially fails due to implementation bugs but its method is later fixed by Debug
steps and preserved in the endpoint, it must be kept.

## Crossover Rules
Keep condition: Effectively combines ideas from two parent branches (e.g., features from A and
models from B), and this fusion direction is adopted in the endpoint code.

Drop conditions:
- Only copies one branch without real fusion.
- The endpoint abandons the fusion direction and follows an unrelated third path.
- Note: If the step fails due to environment issues but is later corrected while preserving
the fusion strategy, it must still be kept.

## Debug Rules
Keep condition: The step accurately identifies and fixes a blocking error, or replaces an
infeasible previous approach with a feasible alternative; and this fix or alternative is
inherited by later steps and becomes a key prerequisite for the endpoint’s effective path.

Drop conditions:
- Blind retry without identifying the concrete failure cause.
- Only adds logging, printing, comments, or formatting without fixing the underlying issue.
- Low-value mechanical edits, such as a one-line typo fix or tiny index change, unless they
form a key reusable fix.
- Only avoids timeout or memory issues by reducing epochs, folds, batch size, sample size,
feature count, training rounds, or model complexity; even if this step is the endpoint and
runs successfully, it should be dropped unless it also introduces a reusable algorithmic or
engineering fix.
- Temporary environment or old-API compatibility workaround that is later replaced by a more
complete refactor in the endpoint.
- The fix or alternative is later rewritten, bypassed, or no longer depended on, so it is not
on the endpoint’s successful path.
- Only leaves local code remnants or architectural similarity in the endpoint, but is not a
key prerequisite for successful execution or core performance.

Notes:
- A Debug step does not have to be the final successful version itself. If its key fix is
inherited by later steps and enters the endpoint, it should still be kept.
- A Debug step does not have to preserve the previous method. If the previous approach is
infeasible under the task constraints, switching to a feasible alternative inherited by the
endpoint should also be kept.

# Output Format
Must output valid JSON only, in the following format:
{
"steps": [
  {
    "step_index": 27,
    "operator": "Improve",
    "keep_for_sft": true,
    "usefulness_reason": "Concise explanation in Chinese describing causal contribution or
    irrelevance to the endpoint."
  }
]
}

# Output Constraints
- The steps array must include every input step exactly once, in input order, with no
omissions.
- The operator field must strictly match Draft, Improve, Crossover, or Debug.
- The usefulness_reason must be specific to the actual step content and avoid generic phrases.
- Do not output Markdown code blocks, only raw JSON.

Each request instantiates the following input template. PARENT_CODES is omitted for Draft,

contains one parent for Improve, and contains two parents for Crossover.

 Annotate the following candidate trajectory using system instructions.

 <TASK_SYSTEM_PROMPT>
 {original task environment and constraints}
 </TASK_SYSTEM_PROMPT>

 <TASK_USER_PROMPT>
 {original task description}
 </TASK_USER_PROMPT>

 <PARENT_CODES>
 {one parent for Improve; two parents for Crossover; omitted for Draft}
 </PARENT_CODES>

 <FINAL_SOLUTION_CODE>
 {complete endpoint code}
 </FINAL_SOLUTION_CODE>

 <TRAJECTORY_STEPS>
 {root full code, subsequent full-file diffs, and execution feedback}
 </TRAJECTORY_STEPS>

### B.2. SFT Training Configuration

Table 4 summarizes the core training settings used for the executable SFT warm starts of Frontis-
MA1-30B and Frontis-MA1-35B.
Table 4 | Core SFT hyperparameters for Frontis-MA1-30B and Frontis-MA1-35B. Settings shared
by both models are centered across the two model columns.

 Item                    Frontis-MA1-30B                            Frontis-MA1-35B
 Base model              Qwen3-30B-A3B-Thinking-2507                Qwen3.6-35B-A3B
 Training stage                                         Full-parameter SFT
 Training framework                              SLIME with Ray and Megatron-LM
 Template / thinking     qwen3 loss mask; <think> supervision       qwen3_5-compatible loss mask; <think>
 mode                    retained                                   supervision retained
 Context cutoff                                            32,768 tokens
 Precision                                                      bfloat16
 Global batch size                                                128
 Per-device batch size                                1 with dynamic batching
 Gradient                64 microbatches per update                 32 microbatches per update
 accumulation
 Learning rate                                              3.0 × 10−5
 Scheduler / warmup                            cosine decay to 0, 0.1 warmup fraction
 Epochs                                                            3

### B.3. RL Training Configuration

Table 5 summarizes the verified RL settings for Frontis-MA1-30B and Frontis-MA1-35B while
retaining the original configuration fields.

Table 5 | RL hyperparameters for Frontis-MA1-30B and Frontis-MA1-35B. Settings shared by
both models are centered across the two model columns.

 Item                 Frontis-MA1-30B                                                Frontis-MA1-35B
 RL initialization    SFT warm-start checkpoint trained from                         SFT warm-start checkpoint trained from
                    Qwen3-30B-A3B-Thinking-2507                                    Qwen3.6-35B-A3B
 Training framework                                                 SLIME with Ray and SGLang
 Operator sampling                                 Draft 0.50, Improve 0.17, Debug 0.17, Crossover 0.16
 probability
 Rollout group        16 prompts per rollout, 16 samples per prompt, global batch size 128, 2 optimizer steps
                                                          per rollout
 Generation                                         temperature 1.0, maximum response length 24,576 tokens
 Advantage /          GSPO with TTT-Discover-style reward post-processing, clip 𝜖 = 3.5 × 10−4 , TIS enabled
 objective
 Optimizer            Adam, learning rate 1.0 × 10−6 , constant schedule, weight decay 0.1, 𝛽1 = 0.9, 𝛽2 = 0.98

### B.4. Asynchronous Rollout

Implementation. A synchronous rollout step must wait for all executions in the batch, so slow
sandbox jobs can leave training resources idle. OpenMLE instead uses a fully asynchronous
rollout worker that draws task groups from the data source, launches generation-and-reward
jobs independently, and pushes completed groups into a queue consumed by the trainer.
Wall-clock benefit and task balance. Figure 23 compares measured wall-clock step time for
synchronous and asynchronous rollouts. Across the 40 matched steps, mean step time is 97.0
minutes for the synchronous run and 50.8 minutes for the asynchronous run, corresponding to
a 1.91× ratio. Although asynchronous collection can consume fast or immediately failing tasks
more often under a fixed wall-clock budget, task exposure remains balanced in practice: in two
representative asynchronous runs, per-task step counts stay within ±2 steps of the run median,
with coefficients of variation of 1.56% and 2.06%.

                                                         Synchronous         Asynchronous

                                       150
                     Step Time (min)

                                       100

                                             0    5       10     15     20        25    30     35
                                                                   Rollout Step

Figure 23 | Wall-clock step-time comparison for synchronous and asynchronous rollout collection
over 40 matched rollout steps. Mean step time is 97.0 minutes for the synchronous run and 50.8
minutes for the asynchronous run.

### B.5. Reward Normalization and Entropic Advantage

We distinguish three quantities: a score-derived base reward used for logging and static compar-
isons, an adaptive-bound processed reward used as the group reward when dynamic bounds are
enabled, and an entropic processed advantage returned by the reward post-processing hook for
RL updates. For a raw task score 𝑠, define the signed score
                             (
                               𝑠,   if larger raw scores are better,
                         𝑧=                                                                (6)
                               −𝑠, otherwise.

Static signed bounds are computed from task metadata after the same sign conversion. For
larger-is-better metrics,

                   𝐵static = max( theoretical_max, leaderboard_max) ,
                                                                                                (7)
                  𝑊static = min( theoretical_min, leaderboard_min) ,

ignoring missing values; lower-is-better metrics use the corresponding signed versions of these
quantities.
Adaptive score range and processed reward. Fixed leaderboard or theoretical bounds can be
much wider than the scores produced by the current policy, making two meaningfully different
programs receive nearly the same reward. We instead rescale each task using a moving score
range built from successful historical programs and the current rollout group. After converting
every metric so that larger values are better, we sort the available scores as

                                       𝑥 (1) ≥ 𝑥 (2) ≥ · · · ≥ 𝑥 ( 𝐾 ) .

The best observed score sets the upper end of the range. The 16th-best score sets the lower
reference point; when fewer than 16 scores are available, we use the lowest available score:

                                𝐵dyn = 𝑥 (1) ,        𝑊dyn = 𝑥 (min(16,𝐾 ) ) .

We then extend the lower end downward by one quarter of the gap between these two reference
scores. This keeps moderately successful programs from being clipped to zero when the observed
scores are tightly clustered:

                           𝑊dyn ← 𝑊dyn − 0.25 max( 𝐵dyn − 𝑊dyn , 0) .

When task metadata provides valid theoretical or leaderboard limits, they prevent the moving
range from extending beyond the task’s valid score range:

                       𝐵 = min( 𝐵dyn , 𝐵static ) ,        𝑊 = max(𝑊dyn , 𝑊static ) ,

with fallback to static bounds if the resulting pair is invalid. The resolved range maps scores to
[0, 1] using the same transformation as Eq. 1; scores below the lower end receive zero:

                                       𝑟proc ( 𝑧 ) = 𝑟base ( 𝑧 ; 𝐵, 𝑊 ) .

Because the range is recomputed from recent and historical policy outputs, it follows the score
frontier as training improves and preserves useful reward differences among current candidates.
The implementation retains both static and adaptive reward views in metadata, while the adaptive
view supplies the reward used by the main RL configuration.
Entropic group advantages. This path replaces the usual GRPO-style normalization of group
rewards into advantages. When entropic post-processing is enabled, rewards are grouped by
prompt group before advantage computation. For group processed rewards 𝑟proc,1 , . . . , 𝑟proc,𝐾 , the

implementation returns zero advantages if 𝐾 < 2 or all rewards are equal. Otherwise it centers
rewards by 𝑐𝑖 = 𝑟proc,𝑖 − max 𝑗 𝑟proc, 𝑗 and defines
                                                                exp( 𝛽𝑐𝑖 )
                                             𝑞𝑖 ( 𝛽 ) = Í 𝐾                    .                                     (8)
                                                               𝑗=1 exp( 𝛽𝑐 𝑗 )

The scalar 𝛽 is chosen by binary search so that
                                                      𝐾
                                                     ∑︁
                                            
                     KL 𝑞 𝛽 ∥ Unif ( 𝐾 ) =                 𝑞𝑖 ( 𝛽 ) (log 𝑞𝑖 ( 𝛽 ) + log 𝐾 ) ≈ log 2,                 (9)
                                                     𝑖=1

with maximum search value 106 and 60 bisection iterations. The returned advantage for sample 𝑖
uses a leave-one-out denominator,
                                        1 ∑︁                      𝑒𝑖
               𝑒𝑖 = exp( 𝛽𝑐𝑖 ) , 𝑍−𝑖 =          𝑒 𝑗,  𝐴𝑖 =                − 1.
                                       𝐾−1
                                           𝑗≠ 𝑖
                                                           𝑍 − 𝑖 + 10 −12

The post-processing hook returns the input rewards as raw_rewards and these 𝐴𝑖 values as
processed_rewards.

### B.6. Detection and prevention of reward hacking.

During the training process, we observed that our models—particularly the smaller ones used
in our early experiments—experience a specific issue during RL on difficult tasks. The reward
quickly plateaus at a very low level.
Based on our case study, we discovered that the models are exhibiting significant reward hacking
behavior. A representative example of this is when a model takes the sample submission, randomly
shuffles it, and submits it as a solution.
To mitigate this, we implemented the following workflow: 1. We use o3-mini as an LLM judge
during the RL process. 2. Before the code is executed in the sandbox, the judge performs a
reward hack check. 3. If reward hacking is detected, the code bypasses sandbox execution and is
assigned a reward of -0.5.

## C OpenMLE-Evo Inference Details

### C.1. Evolutionary Parent Fitness

For a task 𝜏, let P𝜏 be the set of programs stored in the task-local program database. The
implementation recomputes parent fitness at the task level after each insertion. For each node
𝑝 ∈ P𝜏 , define its linked children as

                 C( 𝑝) = { 𝑐 : parent( 𝑐) = 𝑝} ∪ { 𝑐 : 𝑝 ∈ crossover_parents( 𝑐)} .
The three raw components are:
                                                         𝑈 𝑝 = 𝑅base
                                                                𝑝    ,
                   
                   
                    ∅,                                                                            |C( 𝑝)| = 0,
                   
              𝐿 𝑝 = 0,                                                                             |C( 𝑝)| = 1,
                   
                   
                                                                                    2
                    | C 1( 𝑝 ) | 𝑐 ∈ C ( 𝑝 ) 𝑅base − | C 1( 𝑝 ) | 𝑐′ ∈ C ( 𝑝 ) 𝑅base
                                Í                                Í
                   
                                               𝑐                                 𝑐 ′     ,         |C( 𝑝)| ≥ 2,
                   
and                                               (
                                      raw
                                                    1,                                        max 𝑝′ ∈ P𝜏 𝑉𝑝′ = 0,
            𝑉 𝑝 = |C( 𝑝)| ,        𝐶𝑝       =              
                                                                          𝑉𝑝
                                                                                      
                                                    max 0, 1 − max ′                      ,   otherwise.
                                                                         𝑝 ∈P𝜏 𝑉 𝑝′

For finite task-level values { 𝑎 𝑝 }, min–max normalization is
                                  (
                                      𝜂,                           max 𝑝′ 𝑎 𝑝′ − min 𝑝′ 𝑎 𝑝′ < 10−12 ,
                   𝑁𝜂 ( 𝑎 𝑝 ) =          𝑎 𝑝 −min 𝑝′ 𝑎 𝑝′
                                      max 𝑝′ 𝑎 𝑝′ −min 𝑝′ 𝑎 𝑝′ ,   otherwise.

The learning term uses optional normalization: missing 𝐿 𝑝 = ∅ receives the neutral value 𝜂 = 0.5,
while finite learning values are normalized over only the finite entries. Equivalently,
                          (
               opt          𝜂,           𝐿 𝑝 = ∅,
             𝑁𝜂 ( 𝐿 𝑝 ) =
                            𝑁𝜂 ( 𝐿 𝑝 ) , otherwise, with 𝑁𝜂 computed over finite { 𝐿 𝑝′ } .

The implemented fitness is
                                                                   opt
                                  𝐹 ( 𝑝) = 𝑁0.5 (𝑈 𝑝 ) + 𝑁0.5 ( 𝐿 𝑝 ) + 𝑁0.5 ( 𝐶 raw
                                                                                 𝑝 ).

For Improve and Crossover, the candidate set is restricted to programs with positive stored
reward; for Debug, it is restricted to programs with non-positive stored reward. Within the
candidate set S, selection is roulette-wheel sampling without replacement:
                               ( max( 𝐹 ( 𝑝 ) ,0)           Í                  ′
                                                   ′      ,   𝑝′ ∈ S max( 𝐹 ( 𝑝 ) , 0) > 0,
                                Í
                                   𝑝′ ∈S max( 𝐹 ( 𝑝 ) ,0)
                  Pr( 𝑝 | S) = 1
                                 |S| ,                      otherwise.

Crossover draws two parents by applying this rule sequentially and removing the first sampled
parent before the second draw.

### C.2. Operator Prompt Templates

OpenMLE-Evo uses four generation operators with distinct lineage context: Draft proposes
a new solution from the task specification, Improve revises one selected parent, Crossover
synthesizes two selected parents, and Debug repairs a failed or non-positive-reward parent. We
reproduce below the complete system- and user-message schemas used for MLE-Bench inference.
Double-braced expressions denote task- or attempt-specific runtime fields. To make the templates
independent of a particular search trajectory, optional retrieved memory and runtime data-preview
content are left empty; consequently, the empty-memory fallback text is shown.
Draft.

 [SYSTEM MESSAGE]

 You are a Kaggle Grandmaster attending a high-stakes competition. In order to win this
 competition, you need to come up with an excellent and creative plan for a solution and then
 implement this solution in Python.
 {{public_system_prompt}}

 [USER MESSAGE TEMPLATE]

 We will now provide a description of the task.

 Task Description:

 {{task_description}}

 Data Description:

 {{data_description}}

 Draft Guidance:

 Please focus on proposing an advanced idea addressing this task.

Propose exactly one new solution idea that is different from the previously explored ideas.
Keep the evaluation method consistent across iterations.

AIRA Evo Search Context:

Previously explored ideas: none yet.

Execution Budget:

Be aware of the running time of the code, it should complete within {{execution_timeout}}.
Your code will be executed in a sandbox after generation.
A single sandbox run must finish within {{execution_timeout}}.
Always choose a validation/training strategy that leaves enough time to write
./submission.csv.

Submission Check:

Before finishing, verify that ./submission.csv exists, has the same row count and required
columns/order as sample_submission.csv when available, preserves the sample id/order, and
contains no NaN/inf values.
When building features, align train/test columns explicitly and handle missing values before
model fitting or prediction.

{{public_user_prompt}}

Improve.

[SYSTEM MESSAGE]

You are a Kaggle Grandmaster attending a high-stakes competition. In order to win this
competition, you need to come up with an excellent and creative plan for a solution and then
implement this solution in Python, that improves upon an existing solution to the task.
{{public_system_prompt}}

[USER MESSAGE TEMPLATE]

We will now provide a description of the task.

Task Description:

{{task_description}}

Data Description:

{{data_description}}

A previous solution was attempted with the following results:

Code:

```python
{{previous_code}}
```

Feedback:

```
{{previous_terminal_output_with_official_sandbox_score_redacted}}
```

Improve Guidance:

Based on the previous attempt, its score, and execution output, please analyze what worked
well and what didn't, then improve the solution.
Propose exactly one improvement idea that is different from the previously explored
improvement ideas.
Keep the evaluation method consistent across iterations.

AIRA Evo Search Context:

Targeted memory for this improvement: none available.

Execution Budget:

Be aware of the running time of the code, it should complete within {{execution_timeout}}.
Your code will be executed in a sandbox after generation.
A single sandbox run must finish within {{execution_timeout}}.
Always choose a validation/training strategy that leaves enough time to write
./submission.csv.

Submission Check:

Before finishing, verify that ./submission.csv exists, has the same row count and required
columns/order as sample_submission.csv when available, preserves the sample id/order, and
contains no NaN/inf values.
When building features, align train/test columns explicitly and handle missing values before
model fitting or prediction.

{{public_user_prompt}}

Crossover.

[SYSTEM MESSAGE]

You are a Kaggle Grandmaster attending a high-stakes competition. Your goal is to synthesize
the strengths of two provided solutions, neutralize their respective weaknesses, and propose
novel improvements that neither original solution possessed. A simple "merge" of existing code
won't suffice to win. You must identify the hidden synergies between previous attempts and
engineering a third-generation solution that transcends its predecessors.
{{public_system_prompt}}

[USER MESSAGE TEMPLATE]

We will now provide a description of the task.

Task Description:

{{task_description}}

Data Description:

{{data_description}}

Two previous solutions were attempted with the following results:

Code 1:

```python
{{previous_code_1}}
```

Feedback 1:

```
{{previous_terminal_output_1_with_official_sandbox_score_redacted}}
```

Code 2:

```python
{{previous_code_2}}
```

Feedback 2:

```
{{previous_terminal_output_2_with_official_sandbox_score_redacted}}
```

Crossover Guidance:

Based on the previous attempts, their scores, and execution outputs, please synthesize the
winning components of both solutions into a superior hybrid while introducing novel
improvements to address shared weaknesses.

Propose exactly one crossover plan and keep the evaluation method consistent across
iterations.

AIRA Evo Search Context:

Targeted memory for this crossover: none available.

Execution Budget:

Be aware of the running time of the code, it should complete within {{execution_timeout}}.
Your code will be executed in a sandbox after generation.
A single sandbox run must finish within {{execution_timeout}}.
Always choose a validation/training strategy that leaves enough time to write
./submission.csv.

Submission Check:

Before finishing, verify that ./submission.csv exists, has the same row count and required
columns/order as sample_submission.csv when available, preserves the sample id/order, and
contains no NaN/inf values.
When building features, align train/test columns explicitly and handle missing values before
model fitting or prediction.

{{public_user_prompt}}

Debug.

[SYSTEM MESSAGE]

You are a Kaggle Grandmaster attending a high-stakes competition. In order to win this
competition, you need to come up with an excellent and creative plan for a solution and then
implement this solution in Python, that debugs and fixes an existing solution to the task.
{{public_system_prompt}}

[USER MESSAGE TEMPLATE]

We will now provide a description of the task.

Task Description:

{{task_description}}

Data Description:

{{data_description}}

A previous solution was attempted with the following results:

Code:

```python
{{previous_buggy_code}}
```

Feedback:

```
{{execution_output_with_official_sandbox_score_redacted}}
```

Debug Guidance:

Based on the previous attempt, its score, and execution output, please identify the root cause
of the failure and fix the code so it runs successfully and follows the output requirements.
After it runs, improve the solution if possible.
Preserve the current core idea unless the feedback shows that it cannot be made valid.

AIRA Evo Search Context:

Targeted debug memory: none available.

Execution Budget:

 Be aware of the running time of the code, it should complete within {{execution_timeout}}.
 Your code will be executed in a sandbox after generation.
 A single sandbox run must finish within {{execution_timeout}}.
 Always choose a validation/training strategy that leaves enough time to write
 ./submission.csv.
 If the previous attempt timed out, reduce compute first: fewer epochs/folds, smaller input
 size, smaller model, cached features, or simpler ensembling.

 Submission Check:

 Before finishing, verify that ./submission.csv exists, has the same row count and required
 columns/order as sample_submission.csv when available, preserves the sample id/order, and
 contains no NaN/inf values.
 When building features, align train/test columns explicitly and handle missing values before
 model fitting or prediction.

 {{public_user_prompt}}

### C.3. Structured Experience Records

OpenMLE-Evo represents inference-time search state with two deterministic structures. An
experience card is created after every sandbox evaluation and remains attached to that node. The
task-level experience board is recomputed from all accumulated cards whenever the controller
needs global search state. Table 6 gives the complete card content, and Table 7 gives the board
aggregation. We use experience board consistently throughout the paper. The current evaluator
persists the same object under the historical filename strategy_board.json for backward
compatibility; this filename does not denote a separate conceptual structure.

Table 6 | Deterministic node-level experience-card schema in OpenMLE-Evo. The fields are
populated from the program node, sandbox result, and usage record rather than inferred from
test outcomes.

Card component       Stored fields                           Role in search
Identity and         schema_version, node_id, step_id,       Identifies the evaluated program and
lineage              operator, parents,                      reconstructs its incoming search edges.
                   parent_node_ids, generation_id
Observed             score, fitness, reward, status,         Records the validation result and a
outcome              status_code, is_buggy,                  normalized failure signature derived
                   error_signature                         from execution status and logs.
Resource             sandbox_time_used,                      Exposes the computational cost of the
accounting           model_time_used,                        attempted method and supports
                   model_plus_sandbox_time_used,           budget-aware reasoning.
                   cost, and prompt/completion/total
                   token counts
Method               imports, method_family_auto,            Detects a coarse modeling family from
characterization     family_count_before                     the program and measures how often
                                                           that direction has already been
                                                           explored.
Derived search       delta_vs_parent, novelty_score,         Supplies the progress and novelty
signals              is_new_direction, rank,                 factors used alongside validation quality,
                   current_best, selection_utility         plus an auditable parent-selection trace.
Semantic             plan, analysis, and optional            Retains the model proposal and
evidence             rich_summary with                       execution analysis; richer reusable
                   method_overview and                     summaries are generated lazily only
                   parent_comparison_experience            when this node is retrieved.

Table 7 | Task-global experience-board schema. The board is a deterministic aggregation of the
cards available at the current search step.

Board component       Aggregated fields                              Information exposed to the controller
Global incumbent      num_nodes, best_node, best_score,              The size and strongest valid member of the
                    current_best_family                            current population.
Method-family         method_family_stats,                           Per-family counts, valid/failure counts, best
coverage              family_best_nodes,                             score and node, failure rate, and
                    underexplored_families                         low-coverage directions.
Progress and          score_history, recent_delta_trend,             Recent search progress, recurring error
failures              repeated_errors, status_count,                 signatures, and the empirical mix of
                    operator_counts                                operators and outcomes.
Topology and node     parent_graph, novelty_by_node,                 Reconstructs ancestry and provides per-node
state                 rank_by_node, current_best_by_node             novelty, rank, and incumbent indicators for
                                                                   retrieval.
Resources and audit   runtime_stats,                                 Aggregates model/sandbox runtime and
trail                 parent_selection_weights                       preserves the candidate factors, utilities,
                                                                   probabilities, and selected IDs from parent
                                                                   sampling.

Grounded record. For a successful Improve node on leaf-classification, the stored
card records step_id=10, validation log loss fitness=0.012080, delta_vs_parent=0.
753352, method_family_auto=ensemble+xgboost+neural_net+cv, novelty_score=
0.57735, rank=1, current_best=true, 178.58 seconds of sandbox time, and 24,564 to-
tal model tokens. Immediately before generating this node, the experience board identified a
neural_net+cv incumbent with score 0.031825, reported three previous timeouts, and exposed
a recent mean parent-relative gain of 0.01649. Thus, the card states exactly what the new node
achieved, while the board states where that result sits within the surrounding population.

### C.4. Experience-Guided Parent Selection

This subsection specifies the inference-time parent-selection rule used by OpenMLE-Evo and
is distinct from the training-time parent fitness in Appendix C.1. For a sampled island I, each
candidate 𝑖 ∈ I is associated with a deterministic experience card. Let 𝑠𝑖 denote its validation
              par
score and let 𝑠𝑖 be the score of its strongest parent under the task metric. The default score
component applies direction-aware min–max normalization:
                                         𝑠𝑖 − 𝑠min
                                                        if higher is better,
                                      
                                      
                                                   ,
                                ˜𝑠𝑖 =
                                      𝑠
                                      
                                        max  − 𝑠min
                                         𝑠max − 𝑠𝑖
                                      
                                                   ,   if lower is better.
                                       max − 𝑠min
                                      𝑠

When all candidate scores are equal, we set ˜𝑠𝑖 = 0.5. The improvement component retains only
progress over the best available parent:
             (            par                                          Δ𝑖
                                                                                      max 𝑗 ∈ I Δ 𝑗 > 0,
                                                                  
         max(0, 𝑠𝑖 − 𝑠𝑖 ) ,       if higher is better,                          ,
                                                              Δ𝑖 = max 𝑗 ∈ I Δ 𝑗
                                                                  
                                                                  
    Δ𝑖 =         par
                                                              e
         max(0, 𝑠𝑖 − 𝑠𝑖 ) ,       if lower is better,              0,
                                                                  
                                                                                      otherwise.
                                                                  
Nodes without a valid parent receive zero improvement. Finally, if 𝑁 𝑓𝑖 is the number of other
previously recorded cards in candidate 𝑖’s automatically detected method family 𝑓𝑖 , the novelty
component is
                                       𝜈𝑖 = √︁          .
                                               1 + 𝑁 𝑓𝑖

The utility and temperature-controlled softmax are given in Equation 4. The default implemen-
tation uses min–max normalization for score and improvement, while rank-based and hybrid
normalizations are configurable. For Crossover, two parents are sampled sequentially without
replacement from the same island; for Improve, one parent is sampled. Final submission se-
lection is not sampled: it deterministically chooses the best executable candidate with a valid
validation outcome.

### C.5. Operation-Triggered Memory Synthesis

The controller stores every deterministic experience card, but it does not eagerly ask a language
model to summarize every node. Once an operation and its parent nodes have been selected,
it first retrieves a bounded, operation-specific evidence set (Table 8). For any retrieved node
without a cached rich summary, the memory model receives the task description; current and
parent metadata; both plans, programs, and execution outputs; score, parent-relative delta,
runtime, status, and error signature. It must return exactly two JSON fields: method_overview,
a concrete description of the model, features, validation, ensembling, runtime choices, and
submission logic; and parent_comparison_experience, an evidence-based account of what
changed, whether score/status/runtime improved, and what should be reused or avoided. Each
synthesis call summarizes one retrieved node relative to one direct parent; when an operation
retrieves multiple nodes or two crossover branches, their independently cached summaries are
composed only in the subsequent operator-specific context. The resulting summary is cached in
the node and its card, so later operations reuse it without another synthesis call.

Table 8 | Operation-conditioned memory retrieval in OpenMLE-Evo. Ancestor, sibling, and
related-node caps are configurable; the table reports the defaults used by the implementation.

Operator       Default retrieved evidence                                   Purpose of the rendered memory
Draft          No inherited node memory.                                    Starts an independent branch from the
                                                                          task specification.
Improve        The selected parent, its three most recent ancestors,        Preserves what works in the parent,
             and its top three direct siblings. Siblings share at least   identifies changes that helped or hurt
             one parent and are ranked by the same                        along its lineage, and contrasts nearby
             quality–progress–novelty utility used for parent             alternatives without replaying the full
             selection. Relevant board fields are appended.               tree.
Crossover      Two selected parents; for each parent, two recent            Identifies compatible strengths and
             ancestors and two top-ranked direct siblings;                conflicts between branches and
             family-level statistics, repeated errors, and a              discourages a mechanical concatenation
             method-family complementarity cue.                           of both programs.
Debug          The current buggy node followed first by prior nodes         Reuses fixes for the same failure mode
             with the same error signature and then by recent             while retaining a recent-context fallback
             attempts, up to a default total of three related nodes;      for previously unseen errors.
             repeated-error counts are included.

The rendered memory groups selected cards, cached summaries, and board fields into named
sections. Improve receives the selected parent, vertical ancestors, horizontal siblings, and
related board statistics; Crossover repeats the branch sections for both parents and adds the
complementarity cue; and Debug receives the current signature, repeated-error counts, current
buggy node, and related errors. This bounded branch-local context replaces an unbounded
concatenation of prior analyses. The exact system and user-message templates are provided
below.
Complete rich-memory synthesis prompt. The production system prompt and parameterized
user-message template used to extract reusable memories from past trajectories are shown below.

Double-braced expressions denote runtime fields populated from the task, the current node, and
its direct parent.

[SYSTEM MESSAGE]

You are an expert machine learning experiment analyst.
Your job is to distill one completed experiment node into reusable memory.

The memory should explain:
1. What the current node's code actually does, with concrete modeling and implementation
details.
2. What was learned by comparing the current node with its parent, especially whether the
change improved or worsened the result.

Be specific and evidence-based.
Use only the provided code, execution outputs, scores, delta, runtime, and status.
Do not invent results or claim improvements that are not supported by the metadata.

[USER MESSAGE TEMPLATE]

# Task Description
{{task_description}}

# Current Node Metadata
node_id: {{node_id}}
operator_that_created_this_node: {{operator}}
method_family: {{method_family}}
status: {{status}}
score: {{score}}
delta_vs_parent: {{delta_vs_parent}}
runtime_seconds: {{runtime}}
error_signature: {{error_signature}}

# Parent Node Metadata
parent_node_id: {{parent_node_id}}
parent_method_family: {{parent_method_family}}
parent_status: {{parent_status}}
parent_score: {{parent_score}}
parent_runtime_seconds: {{parent_runtime}}

# Current Node Plan
{{current_plan}}

# Parent Node Plan
{{parent_plan}}

# Current Node Code
{{current_code}}

# Current Node Execution Output
{{current_execution_output}}

# Parent Node Code
{{parent_code}}

# Parent Node Execution Output
{{parent_execution_output}}

# Instructions
Write reusable memory for this experiment node.

Focus on two things:

1. method_overview
Summarize what the current code does.
Include concrete details such as:
- model family and main estimator
- feature engineering
- validation strategy
- ensembling or post-processing
- training/runtime choices
- submission generation logic

 2. parent_comparison_experience
 Compare the current node with its parent.
 Explain:
 - what changed from the parent
 - whether the score/status/runtime improved, worsened, or stayed similar
 - what the delta suggests
 - what experience should be reused if it improved
 - what should be avoided or fixed if it worsened or failed

 If the node has no parent, say that it is an initial draft and summarize the initial strategy.
 If the node failed, focus on the failure mode and what should be avoided or fixed.

 Keep the answer concise but information-dense.

 # Output Format
 Return exactly one valid JSON object and nothing else.
 Do not return markdown, code fences, headings, or prose outside the JSON object.

 Use exactly these keys:

 {
   "method_overview": string,
   "parent_comparison_experience": string
 }

 Field requirements:
 - method_overview: 2-5 sentences describing the concrete method used by the current node.
 - parent_comparison_experience: 2-5 sentences comparing current node vs parent and extracting
 success or failure experience.

Grounded rendered context. In the leaf-classification example, the selected ResNet50,
handcrafted-geometry, and XGBoost parent had log loss 0.765432. Horizontal memories exposed
a simpler ResNet18 plus tabular-feature incumbent at 0.031825 and a feature-heavy sibling that
timed out after 7,200 seconds; the board reported current_best_family=neural_net+cv,
repeated_errors:timeout=3, and the parent-family best and failure rate. The next Improve
operation accordingly dropped the oversized ResNet50 and slow handcrafted pipeline, retained
ResNet18 and tabular features, and added calibrated out-of-fold ensembling, yielding 0.012080.
This grounds generated memory in both local alternatives and global search state.

## D Supplementary Experiments

### D.1. Repeated-Evaluation Statistics on MLE-Bench Lite

For model–harness configurations with available repeat-level records, we aggregate three evalu-
ation epochs and report the corresponding mean and standard deviation in Table 9. Repeated
evaluation reduces sensitivity to favorable sampling trajectories and transient sandbox behavior,
while the standard deviation quantifies the remaining run-to-run variability.
Owing to the substantial inference and sandbox cost, Codex, Claude Code, and Gemini CLI
references were evaluated only once and are therefore retained as point estimates in the main
results table. Entries without ± in Table 9 indicate metrics for which the archived summary
contains the aggregate estimate but not the underlying repeat-level dispersion. All reported ±
values denote standard deviations rather than confidence intervals.

### D.2. NatureBench Lite Task Composition

Our generalization study uses the fixed 10-task NatureBench Lite subset summarized in Table 10.
The subset favors moderately tractable tasks while preserving coverage across all six NatureBench
scientific domains and diverse data structures, including biological sequences, omics matrices,
molecular structures, temporal signals, images, and tabular features. This breadth makes the

Table 9 | Repeated-evaluation results on MLE-Bench Lite under the OpenMLE harnesses. Values
are mean ± standard deviation across three evaluation epochs. Valid Rate is the mean number of
tasks producing valid submissions out of 22; Medal Average and Human Rank are higher-is-better.

  Model / system                Framework           Valid Rate      Medal Average ↑   Human Rank ↑
  Qwen3-30B-A3B-Thinking-2507   OpenMLE-Evo       17.33 ± 0.47/22   34.85% ± 2.14%    0.5573 ± 0.0074
  Frontis-MA1-30B               OpenMLE-Evo       21.67 ± 0.47/22   53.03% ± 4.29%    0.7055 ± 0.0505
  Frontis-MA1-30B               OpenMLE-Evo-Max   22.00 ± 0.00/22   66.67% ± 5.67%    0.8053 ± 0.0236
  Qwen3.6-35B-A3B               OpenMLE-Evo       19.67 ± 0.47/22   39.39% ± 5.67%    0.5828 ± 0.0278
  Frontis-MA1-35B               OpenMLE-Evo       21.67 ± 0.47/22   60.61% ± 7.73%    0.7647 ± 0.0376
  Frontis-MA1-35B               OpenMLE-Evo-Max   22.00 ± 0.00/22   71.21% ± 8.57%    0.8126 ± 0.0388
  GLM-5.2                       OpenMLE-Evo-Max   22.00 ± 0.00/22   66.67% ± 8.57%    0.8164 ± 0.0233
  MiniMax M3                    OpenMLE-Evo       22.00 ± 0.00/22   59.09% ± 0.00%    0.7994 ± 0.0225
  MiniMax M3                    OpenMLE-Evo-Max   22.00 ± 0.00/22   65.15% ± 2.14%    0.8007 ± 0.0089
  Kimi K2.6                     OpenMLE-Evo       21.67 ± 0.47/22   66.67% ± 5.67%    0.7859 ± 0.0285
  Grok-4.5                      OpenMLE-Evo       22.00 ± 0.00/22   65.15% ± 2.14%    0.8052 ± 0.0170
  LongCat-2.0                   OpenMLE-Evo       21.00 ± 0.82/22   56.06% ± 5.67%    0.7343 ± 0.0150
  Doubao Seed 2.1 Pro           OpenMLE-Evo       20.33 ± 0.47/22   56.06% ± 2.14%    0.7170 ± 0.0397
  Qwen3.7 Plus                  OpenMLE-Evo       21.67 ± 0.47/22   54.55% ± 6.43%    0.7234 ± 0.0408
  DeepSeek-V4-Pro               OpenMLE-Evo       21.67 ± 0.47/22   54.55% ± 3.71%    0.6849 ± 0.0258
  DeepSeek-V4-Flash             OpenMLE-Evo       21.33 ± 0.47/22   51.52% ± 5.67%    0.6957 ± 0.0200
  GLM-4.7                       OpenMLE-Evo       21.33 ± 0.47/22   51.52% ± 7.73%    0.6521 ± 0.0543
  MiniMax M2.7                  OpenMLE-Evo       22.00 ± 0.00/22   50.00% ± 7.42%    0.7039 ± 0.0298
  MiMo-V2.5-Pro                 OpenMLE-Evo       17.00 ± 1.63/22   40.91% ± 3.71%    0.5213 ± 0.0422
  Step-3.7 Flash                OpenMLE-Evo       19.00 ± 0.00/22   27.27% ± 6.43%    0.4953 ± 0.0385

subset useful for rapid model–harness comparisons, but its ten-task size means that each task
changes All S or All M by ten percentage points.

## E Simplified comparison of public release surfaces

The public release landscape remains fragmented. Table 11 summarizes representative MLE-agent
and MLE-resource work by the artifacts needed to reproduce a full post-training stack. Scores
are not strictly comparable because the systems differ in backbone model, compute and wall-
clock budgets, hardware, external-resource access, number of runs, and aggregation procedure.
Checkmarks denote artifacts that were publicly accessible and independently verifiable from the
cited paper or repository at the time of audit. High-scoring systems often release an inference
framework, evaluation entry point, or leaderboard result; resource projects provide tasks and
environments; training-oriented papers describe RL designs for MLE agents [Cai et al., 2026, Li
et al., 2025b, Liu et al., 2025b, Qiang et al., 2025b, Yang et al., 2025a]. Across these threads,
the combination of executable training data, sandbox infrastructure, training code, RL method,
evaluation framework, and model weights is still rare. This gap motivates treating open MLE
capability as a full-stack problem spanning data, execution, optimization, and inference.

Table 10 | The 10 tasks in NatureBench Lite used for the generalization experiment.

 Task                                                     Domain                          Input modality                              ML task type
 Spatial RNA Velocity Inference                           Cellular Omics                  Single-cell and spatial omics               Simulation / operator
                                                                                                                                      learning
 Disease-Specific Variant Effect Prediction               Cellular Omics                  Biological sequence                         Prediction / regression
 Metabolomic Profile Prediction from                      Cellular Omics                  Tabular / feature matrix                    Prediction / regression
 Microbial Composition
 Protein Variant Effect Prediction                        Protein Biology                 Biological sequence                         Prediction / regression
 Lasso Peptide Property Prediction                        Protein Biology                 Biological sequence                         Prediction / regression
 Anomalous Diffusion Out-of-Distribution                  Physical Modeling               Temporal / signal / spectra                 Classification
 Dynamics Detection
 Zeolite–Molecule Binding Affinity                        Physical Modeling               Molecular / materials structure Prediction / regression
 Prediction
 Spatial Clustering of Single-Molecule                    Biomedical Modeling             Image / volumetric                          Clustering / integration
 Localization Point Clouds
 Molecular Property Prediction                            Molecular Design                Molecular / materials structure Prediction / regression
 Categorical Counterfactual Outcome                       Relational Reasoning            Tabular / feature matrix        Classification
 Estimation

Table 11 | Audited comparison of public release surfaces for representative MLE agents and
resources. Artifact availability was rechecked against the cited papers, official repositories, and
the official MLE-Bench leaderboard submissions as of July 2026.

                                                                  Train RL                 MLE-Bench Lite                        Run
Work                                                   Data Sandbox code method Eval Weights  Medal Rate                          setting                   Best model
No trained MLE model released
AIDE [Jiang et al., 2025]                               ×      ✓        ×       ×       ✓      ×         35.91%                24h · 1×A10                  o1-preview
AutoMLGen / InternAgent [Du et al., 2025]               ×      ✓        ×       ×       ✓      ×         62.12%               12h · 1×A800                 DeepSeek-R1
ML-Master 2.0 [Liu et al., 2025a, Zhu et al., 2026b]    ×      ✓        ×       ×       ✓      ×         75.76%             24h · 2×RTX 4090          DeepSeek-V3.2-Speciale
MLE-STAR-Pro-1.5 [Nam et al., 2025]                     ×      ✓        ×       ×       ✓      ×         68.18%             24h · 2×A100-40G              Gemini-2.5-Pro
MLZero [Fang et al., 2025]                              ×      ✓        ×       ×       ✓      ×         36.36%†            24h · 8×A100-40G            Claude-Sonnet-3.7
AIRA-dojo [Toledo et al., 2025]                         ×      ✓        ×       ×       ✓      ×         55.00%               24h · 1×H200                      o3
Famou-Agent 2.0 [Li et al., 2025a]                      ×      ×        ×       ×       ✓      ×         80.30%               24h · 1×A800             Gemini-3-Pro-Preview
MLEvolve [Du et al., 2026]                              ×      ✓        ×       ×       ✓      ×         80.30%               12h · 1×H200             Gemini-3-Pro-Preview
AIBuildAI [Zhang et al., 2026c]                         ✓      ✓        ×       ×       ✓      ×         77.27%               24h · 1×A100               Claude-Opus-4.6
MLAgentBench [Huang et al., 2023]                       ✓      ✓        ×       ×       ✓      ×            –                        –                           –
MLGym [Nathani et al., 2025]                            ✓      ✓        ×       ×       ✓      ×            –                        –                           –
MLE-Dojo [Qiang et al., 2025a]                          ✓      ✓        ×       ×       ✓      ×            –                        –                           –
MLE-Smith [Qiang et al., 2025b]                         ×      ×        ×       ×       ×      ×            –                        –                           –
R&D-Agent [Yang et al., 2025b]                          ×      ✓        ×       ×       ✓      ×         68.18%               12h · 1×V100                    GPT-5
Post-trained MLE agents
RL-MLE [Yang et al., 2025a]                             ×      ×       ×        ✓       ×      ×             –                      –                            –
ML-Agent [Liu et al., 2025b]                            ×      ×       ✓‡       ✓       ×      ×             –                      –                            –
MLE-RL [Li et al., 2025b]                               ×      ×       ×        ✓       ×      ×          33.30%          12h · A10 (count NR)            MLE-RL-32B-S
AceGRPO [Cai et al., 2026]                              ×      ×       ×        ✓       ×      ×          51.52%              12h · GPU NR                   Ace-30B
OpenMLE (ours)                                          ✓      ✓       ✓        ✓       ✓      ✓          71.21%       12h · RTX 4090(12G VRAM)          Frontis-MA1-35B

Release criteria. For Data, Sandbox, Train code, Eval, and Weights, a tick requires an artifact that was publicly accessible at the time of audit. Data requires downloadable
task/training data or scripts for reconstructing it; Sandbox requires released code capable of running model-generated programs or constructing their execution environment;
Train code requires model-parameter training entry points or configurations; Eval accepts runnable evaluation assets or official per-run grading reports; and Weights requires
downloadable trained MLE-agent weights. A tick under RL method indicates that the work develops or applies an MLE-specific RL post-training method; it does not by itself imply
that the RL implementation is public. Run settings report the per-task wall-clock limit and sandbox GPU allocation; remote LLM-serving compute and CPU/RAM are omitted. NR
means not reported, and “–” means that no corresponding MLE-Bench Lite result is available. GPU-h denotes total sandbox accelerator time rather than elapsed wall-clock time.
† MLZero evaluated 21 of the 22 MLE-Bench Lite tasks, excluding one task because of preprocessing inconsistencies. The displayed rate uses the standard 22-task denominator,
counting the excluded task as a non-medal result.
‡ ML-Agent currently releases its exploration-enriched SFT training code only; its step-wise RL implementation, training dataset, evaluation code, and model checkpoints remain
unreleased.
