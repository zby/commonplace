---
source: https://arxiv.org/abs/2512.22029
description: "Unified continual-learning benchmark testing offline-data access, memory accounting, and semantic-homogeneity assumptions under stricter protocols"
captured: 2026-08-21
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# LibContinual: A Comprehensive Library towards Realistic Continual Learning

Author: Wenbin Li, Shangge Liu, Borui Kang, Yiyang Chen, KaXuan Lew, Yang Chen, Yinghuan Shi, Lei Wang, Yang Gao, and Jiebo Luo
Source: https://arxiv.org/abs/2512.22029
Date: December 26, 2025

## Abstract

A fundamental challenge in Continual Learning
(CL) is catastrophic forgetting, where adapting to new tasks
degrades the performance on previous ones. While the field
has evolved with diverse methods, this rapid surge in diverse methodologies has culminated in a fragmented research
landscape. The lack of a unified framework, including inconsistent implementations, conflicting dependencies, and varying
evaluation protocols, makes fair comparison and reproducible
research increasingly difficult. To address this challenge, we
propose LibContinual, a comprehensive and reproducible library
designed to serve as a foundational platform for realistic CL.
Built upon a high-cohesion, low-coupling modular architecture,
LibContinual integrates 19 representative algorithms across five
major methodological categories, providing a standardized execution environment. Meanwhile, leveraging this unified framework, we systematically identify and investigate three implicit
assumptions prevalent in mainstream evaluation: (1) offline data
accessibility, (2) unregulated memory resources, and (3) intratask semantic homogeneity. We argue that these assumptions
often overestimate the real-world applicability of CL methods.
Through our comprehensive analysis using strict online CL
settings, a novel unified memory budget protocol, and a proposed
category-randomized setting, we reveal significant performance
drops in many representative CL methods when subjected to
these real-world constraints. Our study underscores the necessity
of resource-aware and semantically robust CL strategies, and
offers LibContinual as a foundational toolkit for future research
in realistic continual learning. The source code is available from
https://github.com/RL-VIG/LibContinual.
## Index Terms

Unified framework, Continual learning, Image
classification, Fair comparison.

## I. Introduction

E

NDOWING machines with the human-like capability
to continuously acquire new knowledge and adapt to
evolving environments represents one of the ultimate milestones toward achieving artificial general intelligence. Continual Learning (CL), also known as lifelong or incremental
learning, is the research paradigm dedicated to this goal. It
requires a model to learn sequentially from a non-stationary
stream of data, acquiring knowledge from a series of tasks
without compromising its performance on previously learned
Wenbin Li, Shangge Liu, Borui Kang, Yiyang Chen, KaXuan
Lew, Yang Chen, Yinghuan Shi and Yang Gao are with the State
Key Laboratory for Novel Software Technology, Nanjing University,
China (e-mails: liwenbin@nju.edu.cn; lshangge@smail.nju.edu.cn; kangborui@smail.nju.edu.cn; yychen@smail.nju.edu.cn; lewkaxuan@gmail.com;
chen-yang@smail.nju.edu.cn; syh@nju.edu.cn; gaoy@nju.edu.cn).
Lei Wang is with the School of Computing and Information Technology,
University of Wollongong, Australia (e-mail: leiw@uow.edu.au).
Jiebo Luo is with the Department of Computer Science, University of
Rochester, USA (e-mail: jluo@cs.rochester.edu).

tasks. However, this ideal learning process is hindered by a
fundamental challenge, catastrophic forgetting [1], [2]. When a
model adjusts its parameters to accommodate a new task’s data
distribution, it often overwrites the knowledge critical for past
tasks, causing significant performance degradation on prior
tasks. Navigating the trade-off between plasticity (the ability
to learn new knowledge) and stability (the preservation of
old knowledge), known as the stability-plasticity dilemma [3],
constitutes the central challenge in the field.
To address this challenge, the research community has explored various technical avenues [4], including regularizationbased methods [5], [6] that protect prior knowledge,
replay-based methods [7], [8], [9] that rehearse past data,
optimization-based methods [10], [11] that constrain parameter
updates, and architecture-based methods [12], [13] that adapt
the model structure. More recently, the advent of Pre-Trained
Models (PTM) has triggered a profound paradigm shift in CL,
giving rise to representation-based methods [14], [15], [16]
that focus on efficiently adapting powerful pre-trained features.
The research focus is gradually moving from “learning from
scratch” [7] to “efficiently and robustly fine-tuning and adapting powerful pre-trained knowledge” [14], [4].
Meanwhile, this rapid surge in diverse methodologies has
culminated in a fragmented research landscape. Methods are
often implemented using different deep learning frameworks,
conflicting dependency versions, and inconsistent data processing pipelines. Such fragmentation makes it difficult to
determine whether performance gains stem from algorithmic innovation or merely from differences in implementation
details and hyperparameter tuning. Consequently, there is a
critical lack of a unified framework capable of providing a
standardized implementation and fair comparison across the
diverse methods. While several libraries have been developed
to aid reproducible research, such as Avalanche [17], Continuum [18] and PyCIL [19], they often exhibit limitations. As
will be discussed in Section II-B, some existing frameworks
suffer from rigid component coupling, which complicates the
extension or customization of internal modules. Others lack
native support for modern Vision-Language Models (VLM),
restricting the comparison between traditional training-fromscratch methods and PTM-based strategies. This absence of
a comprehensive, modular, and up-to-date toolkit creates a
barrier to rigorous empirical analysis and further advances.
To address this challenge, we propose LibContinual, a
comprehensive and reproducible library designed to serve as a
foundational platform for realistic continual learning. LibContinual is built upon a high-cohesion, low-coupling architectural


Data stream

Offline Data Accessibility

Intra-Task Semantic Homogeneity

Unregulated Memory Resources
method A method B method C

Data of
task 𝒯𝒯𝑡𝑡

model

Online Continual Learning
Storage constraint

Data sample 𝑥𝑥,v 𝑦𝑦
data stream

Semantic structure

Task 1

v

Task 2

Inconsistent Cost Accounting

Unified Memory Budge

Category-Randomized setting

Unified & Constrained

Task 1

method A method B method C

v

Task 2

model

Mainstream evaluation

LibContinual = (

,

,

)

Fig. 1: Conceptual illustration of the three implicit assumptions in continual learning evaluation and our proposed experimental
dimensions to investigate them. Standard evaluation paradigms (gray) often rely on idealized conditions. (1) Data Stream (the
Orange Axis): They assume offline access to task data for multi-epoch training, whereas we test models in a strict single-pass
online CL setting. (2) Storage Constraint (the Teal Axis): They permit inconsistent memory cost accounting, making fair
comparison difficult; we enforce a unified memory budget to normalize evaluation. (3) Semantic Structure (the Yellow Axis):
They typically use tasks with high intra-task semantic homogeneity. We introduce a more challenging category-randomized
setting, preventing models from relying on task-level shortcuts and thus testing for more robust representations.
design (detailed in Section III). It decouples the experimental
workflow into modular components, inlcuding Trainer, Model,
Buffer, and DataModule, driven by a unified configuration
system. This design allows researchers to seamlessly mix
and match diverse backbones, classifiers, and buffer strategies within a standardized execution environment. Leveraging
this architecture, we integrate 19 representative algorithms
spanning all five major categories: regularization, replay, optimization, representation, and architecture-based methods. By
providing a unified interface for classical and modern PTMbased methods, LibContinual can enable the community to
conduct fair, transparent, and scalable benchmarking.
Equally important, during the development of LibContinual, the standardization of protocols allowed us to identify
several implicit assumptions deeply embedded in mainstream
evaluation paradigms. These assumptions, often accepted as
convention, may overestimate the real-world applicability of
CL methods. Specifically, we identify three implicit assumption: (1) The Assumption of Offline Data Accessibility, which
presumes multi-epoch training on task data, ignoring the
single-pass nature of real-world streams; (2) The Assumption of Unregulated Memory Resources, where inconsistent
accounting of storage (e.g., raw images vs. abstract features)
obscures true algorithmic efficiency; and (3) The Assumption
of Intra-Task Semantic Homogeneity, which provides models
with artificial contextual shortcuts by grouping semantically
related classes into tasks.
Leveraging the modular capabilities of LibContinual, we
move beyond simple benchmarking to systematically investigate these assumptions. As conceptually illustrated in Figure 1,
our investigation is structured along the three dimensions.
We introduce novel evaluation protocols, including a strict
online CL setting, a unified memory budget, and a challenging
category-randomized setting. Our comprehensive experiments
reveal that when these idealized assumptions are removed, the
performance of some methods degrades significantly, exposing

the fragility of current solutions under realistic constraints.
The contributions of this paper are summarized as follows:
• We propose the LibContinual, a unified and reproducible
framework designed for the rigorous and fair implementation and evaluation of continual learning algorithms.
• We systematically identify and investigate three fundamental yet often overlooked assumptions in mainstream
CL evaluation: offline data accessibility, unregulated
memory resources, and intra-task semantic homogeneity.
• We propose novel evaluation protocols, including a unified memory budget and a category-randomized setting,
to facilitate more realistic and robust benchmarking.
• Through extensive experiments within LibContinual, we
reveal significant performance drops for many representative methods under more realistic settings. Our findings
provide critical insights into their true applicability and
underscore the necessity of developing resource-aware
and semantically robust CL strategies.
## II. Background and Related Work
A. The Continual Learning Problem
Continual Learning is the paradigm for training models
on a sequence of tasks, where the data distribution is nonstationary. The central challenge is to overcome catastrophic
forgetting, where a model’s performance on previously learned
tasks degrades significantly upon learning new ones.
Formally, the problem of continual learning is defined as
a process of sequential learning over a sequence of tasks,
T = {T1 , T2 , . . . , TT }. Each task Tt is characterized by a
distinct data distribution Dt over an input space Xt and a
label space Yt . A learning system, represented by a model fθ
parameterized by θ, learns from this sequence of tasks in order.
When learning the t-th task, the model updates its parameters
from θt−1 to θt based on data sampled from Dt .
The core constraint of continual learning is that while
learning task Tt , the model has very limited access to the


inual Learner

training data from past tasks’ distributions {D1 , . . . , Dt−1 }.
aries
The ultimate objective is to find a single set
parameters
CL of
Methods
θT for the final model that minimizes the total statistical risk
s
across all tasks seen so far,
min
θT

T
X

Checkpoints

E(x,y)∼Dt [L(fθT (x), y)],

(1)

Train&Test Log

Data Module
DataLoader

B. Related Work
While several excellent works have mapped the continual
learning landscape, our work offers a distinct and targeted
contribution. We position LibContinual by comparing it first
against broad academic surveys and then against existing
software libraries.
1) Comparison with Continual Learning Surveys: A significant body of literature provides comprehensive surveys
of the continual learning field. Lange et al. [20], Wang et
al. [4], and Zhou et al. [21] offer extensive taxonomies. They
categorize methods into families such as regularization-based,
replay-based, and architecture-based methods. These surveys
are invaluable for understanding theoretical underpinnings and
the historical progression of algorithms. More focused surveys
also exist for specific sub-fields. For example, Masana et
al. [22] focus on class-incremental learning, while Zhou et
al. [23] provide deep dives into pre-trained models. These
works successfully synthesize and organize existing knowledge.
However, these surveys are primarily descriptive and rely
on results from inconsistent experimental paradigms. These
paradigms often rest on idealized premises that may not hold
in realistic scenarios. In contrast, our contribution shifts from
a descriptive role to an experimental and prescriptive one.
We implement concrete protocols to scrutinize three prevalent implicit assumptions: offline data accessibility, intra-task
semantic homogeneity, and unregulated memory resources.
By rigorously investigating these factors, we complement
theoretical surveys with robust practical verification.
2) Comparison with Continual Learning Libraries: Several
open-source libraries have been developed to aid reproducible
research in continual learning. Avalanche [17] is a comprehensive library offering a vast collection of algorithms
and standard benchmarks. Continuum [18] excels with its
robust and flexible data-loading capabilities. Other libraries
like PyCIL [19] provide a focused toolbox specifically for
class-incremental learning. These frameworks have been instrumental in standardizing experiments.
While these frameworks help standardize experiments, LibContinual advances distinct advancements in architectural design and model compatibility. First, LibContinual features a
unified and decoupled high-level design. We adhere to highcohesion and low-coupling principles by extracting algorithmagnostic components into shared modules. These components

Checkpoints

Trainer

Model

Config File

Backbone

Data Module

t=1

where L is a given loss function. However, this objective is
infeasible in continual learning because restricted access to
past data renders the global empirical risk incomputable. This
inability to evaluate the empirical risk on previous tasks is the
root cause of catastrophic forgetting.

Visualization

Unified
Buffer

Classifier

Log System
Metric Func

Model
Strategy

PyYAML

Loss Func

Optimizer

Pytorch

TensorBoard

Numpy

Scikit-learn

Fig. 2: Architecture of the proposed Libcontinual.
include the training loop, data management, and evaluation
protocols. Consequently, the implementation files remain minimal. Researchers only need to define functions specific to
the unique logic of an algorithm. This modularity reduces
code redundancy and guarantees a standardized execution
environment for fair comparison. Second, LibContinual explicitly supports Vision-Language Models (VLM). The framework seamlessly integrates modern backbones such as Vision
Transformers and CLIP. This capability allows for the direct
implementation and comprehensive evaluation of advanced
PTM-based strategies alongside classical methods.
## III. LibContinual: A Unified Framework for
C ONTINUAL L EARNING
A. The LibContinual Toolbox
The CL landscape is characterized by a rapid expansion of
algorithms. However, this progress is often fragmented across
disparate codebases with inconsistent evaluation protocols,
making fair comparison and reproducible research significant
challenges. To address this critical gap, we propose LibContinual. It is not merely an algorithm repository but a comprehensive and modular research toolbox built upon PyTorch. It
is designed to provide a standardized environment that fosters
transparent, rigorous, and fair algorithmic evaluation.
As shown in Figure 2, LibContinual adheres to highcohesion, low-coupling design principles and is driven by simple YAML files for experiment configuration. Its architecture
is meticulously decoupled into several core modules: a Trainer
module that manages the entire experimental workflow; a
Model module integrating diverse backbones, classifiers, and
algorithms; a specialized DataLoader for CL-specific data
partitioning and augmentation; a versatile Buffer module supporting various memory sampling and update strategies; and
a Config module that orchestrates the entire setup.
This clear modularity and unified interface are designed
to provide researchers with a fair evaluation platform while
significantly lowering the barrier to developing and validating
novel algorithms. We believe LibContinual can serve as a
robust foundation for advancing the field. A detailed overview


of the framework’s architecture, module functionalities, and
implementation specifics is shown in Appendix B.
B. Continual Learning Scenarios Supported in Libcontinual
Continual learning scenarios are typically categorized along
several distinct, often orthogonal, dimensions. These dimensions determine the specific constraints and challenges the
learning algorithm needs to address. A key design goal of
LibContinual is to provide a unified platform that supports the
configuration of these diverse scenarios via modular components and YAML files, enabling systematic performance analysis. In the following, we explore three of these fundamental
dimensions, all configurable within our framework: the data
arrival paradigm, the information accessible at inference time,
and the semantic structure of the tasks.
1) By data arrival paradigm: This dimension defines how
the data for an individual task Tt is presented to the model.
LibContinual supports the two dominant paradigms.
In Offline Continual Learning (or batch CL), the entire
t
training dataset for a task, Dt = {(xi , yi )}ni=1
, is made
available at once. The model parameters are updated from
θt−1 to θt by optimizing over the full training dataset Dt 1 ,
often for multiple epochs. Repeated training ensures the model
thoroughly converges on the objectives for task Tt before
moving on. The learning process for the task can be abstracted
as θt = Train(θt−1 , Dt ).
In Online Continual Learning, data arrives as a continuous
and often rapid stream, demanding that the model learns onthe-fly. The data is typically processed as a sequence
small
SKof
t
mini-batches (Bt,1 , Bt,2 , . . . , Bt,Kt ), where Dt = k=1
Bt,k .
The model is restricted to a single pass, meaning parameters
are updated incrementally after each mini-batch,
θt,k = Update(θt,k−1 , Bt,k ),

for k = 1, . . . , Kt

(2)

where θt,0 = θt−1 and the final parameter set is θt = θt,Kt .
This single-pass constraint gives rise to intra-task forgetting [24], the tendency to forget knowledge from earlier
batches while learning from later ones.
This distinction is configured via the YAML file. Consistent
with online CL protocols [24], [25], users can enforce a strict
single-pass stream by setting ‘epochs: 1’ and specifying a
small batch size (e.g., 10). Conversely, setting ‘epochs > 1’
enables the multi-epoch training.
2) By inference-time accessible information: The second
dimension classifies scenarios based on the information available at test time, leading to the three canonical settings
proposed by [26]: Task-Incremental, Domain-Incremental, and
Class-Incremental Learning.
In Task-Incremental Learning, the model is provided with
the task identity t at inference time. The objective is thus to
learn a task-aware mapping fθ : (X , t) → Yt . This allows
for task-specific components (e.g., a multi-headed classifier),
shifting the primary challenge from merely preventing forgetting to achieving efficient knowledge transfer.
1 Here, D represents the finite, empirical dataset sampled from the undert
lying theoretical data distribution Dt introduced in Section II-A. While the
ultimate goal is to generalize to Dt , the learning algorithm only has access
to Dt .

Task 1

Task 2

Traditional Setting
Task 1

Task 1

Task 2

Cross-Domain Setting

Task 2

Category-Randomized Setting

images from dataset 1 (MNIST)

images from dataset 2 (CIFAR10)

Fig. 3: An illustration of the three continual learning settings defined by inter- and intra-task semantic structure. In
the traditional setting, tasks are subsets of a single dataset,
making them semantically homogeneous. In the cross-domain
setting, each task remains homogeneous but originates from a
different domain, introducing a domain shift between tasks. In
our proposed category-randomized setting, the assumption of
intra-task homogeneity is broken. Each task is a heterogeneous
mix of classes from different domains, forcing the model to
learn disparate concepts simultaneously.
In contrast, both Domain- and Class-Incremental Learning operate without task identity at test time. In DomainIncremental Learning (DIL), all tasks share an identical label
space, i.e., Y1 = · · · = YT = Yshared . The model must learn
a single, unified mapping fθ : X → Yshared that is robust to
shifts in the input data distribution (domains).
Finally, in Class-Incremental Learning, each task introduces a new, disjoint set of classes, where Yt ∩ Yt′ = ∅ for
any t ̸= t′ . The model must learn to discriminate among
all classes seen so far, S
requiring a mapping to the global
T
label space, fθ : X → i=1 Yi . This is widely considered
the most challenging scenario as it requires distinguishing
between classes that are never observed together [26]. Since
guaranteeing the availability of task identity is often impractical in real-world environments, and CIL is considered a more
challenging scenario [4], we focus our investigation primarily
on this setting.
LibContinual provides robust support for the two most
widely studied scenarios: TIL and CIL. In the YAML file,
setting ‘setting: task-aware’ enables the TIL scenario, and
setting ‘setting: task-agnostic’ enforces the CIL scenario.
3) By inter- and intra-task semantic structure: A third
crucial dimension, which we introduce in this work to systematically analyze semantic assumptions, is the Inter- and
Intra-Task Semantic Structure. It defines how the disjoint class
sets (Yt ) are constructed to form the sequence of tasks in a
CIL problem. This construction governs two key properties
of the learning curriculum: the intra-task semantic similarity
(whether classes within a single task are related) and the
inter-task semantic similarity (how related the consecutive
tasks are). LibContinual supports three key setting along this
dimension as illustrated in Figure 3.
Traditional Setting. This setting is characterized by high
intra-task and high inter-task semantic similarity. Tasks are
typically formed by partitioning the classes of a single and
semantically coherent dataset (e.g., splitting CIFAR-100 into
10 tasks). Consequently, classes within any given task are


Optimization-based
Regularization-based

Continual
Learning

Architecture-based
Replay-based

min 𝔼𝔼(𝑥𝑥,𝑦𝑦)∼𝒟𝒟𝑡𝑡 [ℒ 𝑓𝑓𝜃𝜃 𝑥𝑥 , 𝑦𝑦 , s. t. ∇𝜃𝜃 ℒ𝑡𝑡 , ∇𝜃𝜃 ℒ𝑡𝑡−1 ≥ 0
𝜃𝜃

min 𝔼𝔼(𝑥𝑥,𝑦𝑦)∼𝒟𝒟𝑡𝑡 ℒ 𝑓𝑓 𝑥𝑥; 𝜃𝜃⨁𝜃𝜃�𝑡𝑡 , 𝑦𝑦
�𝑡𝑡
𝜃𝜃

Optimization

min 𝔼𝔼(𝑥𝑥,𝑦𝑦)∼𝒟𝒟𝑡𝑡 [ℒ 𝑓𝑓𝜃𝜃 𝑥𝑥 , 𝑦𝑦 + 𝛽𝛽 ⋅ 𝔼𝔼 𝑥𝑥𝑚𝑚,𝑦𝑦𝑚𝑚 ~ℳ [ℒ𝑚𝑚 (𝑓𝑓𝜃𝜃 𝑥𝑥𝑚𝑚 ), 𝑦𝑦𝑚𝑚 ]] ,
𝜃𝜃

Representation-based

min 𝔼𝔼(𝑥𝑥,𝑦𝑦)∼𝒟𝒟𝑡𝑡 [ℒ 𝑓𝑓𝜃𝜃 𝑥𝑥 , 𝑦𝑦 + Ω(𝜃𝜃, 𝜃𝜃𝑡𝑡−1 )]
𝜃𝜃

+ 𝜆𝜆 ⋅ ℛ(𝜃𝜃�𝑡𝑡 ) , s. t. ℛ ⋅ = 𝜃𝜃�𝑡𝑡 sparse
Architecture

𝑡𝑡−1

ℳ = � 𝒮𝒮𝑘𝑘
𝑘𝑘=1

Replay

Regularization

min ℒpretext (𝜃𝜃enc ; 𝒟𝒟pretrain )
𝜃𝜃enc

min

𝜃𝜃cls ,[𝜃𝜃enc ]

𝔼𝔼(𝑥𝑥,𝑦𝑦)∼𝒟𝒟𝑡𝑡 [ℒ 𝑓𝑓cls (𝑓𝑓enc 𝑥𝑥, 𝜃𝜃enc ; θcls ), 𝑦𝑦 ] ,

s. t. 𝑓𝑓enc ∈ ℱstable

Representation

Fig. 4: The taxonomy of continual learning methods categorizes them into five major algorithmic strategies: regularizationbased, replay-based, optimization-based, representation-based, and architecture-based methods.

inherently related, and all tasks are drawn from the same overarching data distribution. This common setup allows models
to leverage task-level semantic context but fails to represent
learning across disparate concepts.
Cross-domain Setting. This setting features high intratask but low inter-task semantic similarity. Each task remains
internally homogeneous as all its classes are sourced from
a single dataset, but different tasks originate from distinct
domains, introducing a significant domain shift. For instance,
a learning sequence might start with Task 1 containing classes
from CIFAR-10 [27] (natural images), followed by Task 2
with classes from MNIST [28] (handwritten digits). Although
framed as a CIL problem with disjoint classes, the primary
challenge here is the abrupt change in data statistics and visual
features between tasks. This setup rigorously tests a model’s
ability to adapt to new data types while preserving knowledge
from entirely different past domains.
Category-randomized Setting. LibContinual supports a
novel category-randomized setting. Unlike the previous two
paradigms which maintain high intra-task semantic homogeneity, this setting is designed to deliberately disrupt this semantic
structure to rigorously test model robustness. We reserve the
detailed formulation, motivation, and implementation details
of this setting for Section IV-C, where we discuss it in the
context of investigating implicit semantic assumptions.
In LibContinual, these scenarios are configured via the
data module. For the traditional setting, users specify a
single dataset and a partitioning scheme. For the crossdomain setting, users can define a sequence of datasets, where
each dataset is treated as a new task. Finally, the categoryrandomized setting is enabled by a flag that pools, shuffles,
and partitions classes from all specified datasets.
C. The Selection of Algorithms for Libcontinual
To ensure a comprehensive and representative evaluation
of the continual learning landscape, we have implemented a
suite of 19 methods within LibContinual (see Table I). Our
selection is guided by recent and widely accepted taxonomies
in the field [4], which categorize CL algorithms into five major families: regularization-based, replay-based, optimizationbased, representation-based, and architecture-based strategies.
By integrating both classical baselines and representative PTM
methods, LibContinual facilitates a rigorous investigation into
how different algorithmic philosophies address the stabilityplasticity dilemma.

Crucially, to provide a cohesive theoretical perspective, we
distill the core logic of each category into a mathematical
formulation as shown in Figure 4. For each category, we will:
(1) present its core principles through our distilled formulation,
(2) highlight representative methods implemented in LibContinual, and (3) provide critical discussion on its distinctive
advantages and unresolved limitations. Detailed descriptions,
implementation specifics, and additional representative methods for each category are provided in Appendix A.
1) Regularization-based methods: These methods augment
the training objective with a penalty term to mitigate forgetting. When learning task Tt , the parameters θt are found by
optimizing,
θt = arg min E(x,y)∼Dt [L(fθ (x), y) + Ω(θ, θt−1 )].
θ

(3)

The objective balances plasticity, driven by the empirical risk
on the new data Dt , with stability, enforced by the regularizer
Ω(θ, θt−1 ) which penalizes deviations from the previous state.
The primary innovation in this category lies in the specific
design of the regularizer Ω.
In early methods, the regularizer Ω can be defined in the
parameter space [5], [29], [30], [31] or functional space [6],
[32], [33], [34]. This principle continues to evolve, with
recent work exploring regularization in the spectral [35] and
topological [36] domains. Furthermore, researchers have also
begun to adapt these regularization methods to the continual
instruction tuning of large multimodal models [37], [38].
Regularization-based methods are foundational to continual
learning due to their simplicity and effectiveness. However,
they face challenges in the era of Pre-trained Models (PTM).
Directly applying global constraints often proves suboptimal
as it restricts the PTM’s inherent adaptability [37]. We argue
that the future value of regularization lies in its flexibility
as a strategic component, for instance, applying targeted
constraints to lightweight modules like Adapters, rather than
as a standalone global solution.
Within this category, LibContinual implements foundational
methods including LwF [6] and EWC [5], which regularize the
model in the functional and parameter space, respectively.
2) Replay-based methods: These methods mitigate catastrophic forgetting by rehearsing a subset of past data stored
in a memory buffer M alongside new task data, thereby approximating training on the joint distribution. The optimization


objective minimizes a composite loss,
min E(x,y)∼Dt [L(fθ (x), y)] + β · E(xm ,ym )∼M [Lm (fθ (xm ), ym )],
θ

M=

t−1
[

Sk .

k=1

(4)

Here, M contains exemplars Sk from past tasks. The content
of this buffer M, fundamentally defines the specific replay
strategy. It may contain raw past examples [7] [39] [40] [41]
[42], pseudo-data synthesized by a generative model [43] [44]
[45] [9], or abstract latent representations [46] [47]. And the
model is regularized by minimizing Lm on samples drawn
from this buffer. The hyperparameter β controls the trade-off
between learning the new task and preserving old knowledge.
The central challenge lies in how to construct, manage, and
utilize the memory buffer M to approximate the true data
distribution of past tasks under strict memory constraints.
Replay-based methods remain at the forefront of continual
learning research due to the direct, data-driven constraint
against forgetting. While effective, their performance is intrinsically tied to the size and quality of the memory buffer,
creating a trade-off between memory overhead, potential privacy risks, and learning efficacy. We argue that future progress
hinges on two key areas: developing more intelligent sampling
strategies to maximize the utility of a limited memory budget,
and establishing a stronger theoretical foundation to explain
why and when replay is most effective.
In LibContinual, we implement representative methods including iCaRL [7], BiC [48], LUCIR [49], WA [50], and the
online-focused OCM [24] and ERAML/ERACE [25].
3) Optimization-based methods: These methods mitigate
the stability-plasticity dilemma by framing continual learning
as a constrained optimization problem. The core idea is to find
parameter updates for a new task that do not increase the loss
on previously learned tasks. This principle is captured by the
general objective,


θt = arg min E(x,y)∼Dt L(fθ (x), y) .
θ

s.t.⟨∇θ Lt , ∇θ Lt−1 ⟩ ≥ 0
(5)

The objective balances plasticity, by minimizing the loss on
new data Dt , with stability, enforced by the constraint that
prevents conflicting updates.
Classic methods like GPM [10] and Adam-NSCL [51]
enforce a strict constraint by projecting the gradient for the
new task into a subspace that is orthogonal to the feature
representations of past tasks. While effective at preventing
interference, these hard constraints can limit plasticity. To
address this, subsequent methods have introduced more flexible constraints. For instance, TRGP [52] uses adaptive trust
regions to allow for beneficial updates within boundaries,
while more recent work like AdaBOP [53] derives a closedform solution for the optimal projection, enabling a finegrained, per-layer balance between stability and plasticity via
tunable hyperparameters.
Optimization-based methods are often adopted as effective
plug-and-play modules for mitigating forgetting. However,
this has led to a focus on applying existing constraint techniques rather than innovating on the underlying optimiza-

TABLE I
C LASSIFICATION OVERVIEW OF IMPLEMENTED METHODS IN
L IB C ONTINUAL . T HIS TABLE SUMMARIZES THE REPRESENTATIVE
ALGORITHMS SUPPORTED BY OUR FRAMEWORK , CLASSIFYING
THEM BY THEIR CORE ALGORITHMIC S TRATEGY (S ECTION III-B)
AND THE FORM OF S TORAGE THEY USE TO MITIGATE
FORGETTING (S ECTION IV-B).
Method

Venue & Year

Algorithm

Storage

LwF [6]
EWC [5]

ECCV 2016
PNAS 2017

Regularization
Regularization

Feature
Model

iCaRL [7]
BiC [48]
LUCIR [49]
WA [50]
ERAML/ERACE [25]
OCM [24]

CVPR 2017
CVPR 2019
CVPR 2019
CVPR 2020
ICLR 2022
ICML 2022

Replay
Replay
Replay
Replay
Replay
Replay

Image
Image
Image
Image
Image
Image

GPM [10]
TRGP [52]

ICLR 2021
ICLR 2022

Optimization
Optimization

Feature
Feature

API [56]
InfLoRA [11]
MoE-Adapter4CL [13]
SD-LoRA [12]

CVPR 2023
CVPR 2024
CVPR 2024
ICLR 2025

Architecture
Architecture
Architecture
Architecture

Feature
Feature
Parameter
Parameter

L2P [14]
DualPrompt [57]
CodaPrompt [58]
RanPAC [15]
RAPF [16]

CVPR 2022
ECCV 2022
CVPR 2023
NeurIPS 2023
ECCV 2024

Representation
Representation
Representation
Representation
Representation

Prompt
Prompt
Prompt
Parameter
Parameter

tion principles themselves [54]. Many current methods still
rely on variations of gradient projection [55]. We believe
future progress lies in re-examining the foundational theory
to develop optimization frameworks that intrinsically encode
forgetting resistance.
In LibContinual, we include prominent optimization-based
methods such as GPM [10] and TRGP [52].
4) Representation-based methods: These methods shift the
CL focus from preserving old knowledge to acquiring universal representations. The core philosophy involves a two-phase
process where the model decomposes into a feature encoder
fcls and a classifier θcls .
Phase 1 (Representation Learning).
min Lpretext (θenc ; Dpretrain ).
θenc

(6)

Phase 2 (Continual Learning).
min E(x,y)∼Dt [L(fcls (fenc (x; θenc ); θcls ), y)]

θcls ,[θenc ]

(7)
s.t.

fenc ∈ Fstable .

In the first phase, a powerful encoder fenc is trained on Dpretrain
via a pretext task, optimizing a pretext loss Lpretext . This phase,
which typically involves self-supervised learning or large-scale
supervised pre-training [59], [60]. Most CL methods concentrate on the strategies for Phase 2, which focuses on adapting
to task Tt while maintaining stability. Strategies to enforce
fenc ∈ Fstable generally fall into two categories: keeping θenc
frozen while optimizing lightweight modules, such as prompts
(L2P [14], DualPrompt [57], CodaPrompt [58]) or random
projection layers (RanPAC [15]), or cautiously fine-tuning the
encoder to balance plasticity and forgetting [61] [62] [16].
Representation-based methods, especially those built upon
PTM, currently represent one of promising frontiers of
rehearsal-free continual learning. Their success highlights a


key insight: the core challenge of CL is not learning new
features from scratch, but rather learning to effectively access
and combine the rich features already present in PTM. Therefore, the central challenges lie in learning more potent feature
representations and developing more fine-grained mechanisms
to identify and preserve the features essential for preventing
forgetting. Furthermore, addressing the representation gaps
and discrepancies between different modalities, and how to
continually learn on them without catastrophic interference,
emerges as a vital new frontier.
In LibContinual, we implement L2P [14], DualPrompt [57],
CODA-Prompt [58], RanPAC [15], and RAPF [16].
5) Architecture-based methods: These methods prevent
catastrophic forgetting by structurally isolating task-specific
knowledge. They typically compose a stable, shared backbone θ with expandable, task-specific modules {θ̂k }tk=1 . The
optimization for task Tt focuses on updating only the newly
introduced parameters,

T

AT =

min E(x,y)∼Dt [L(f (x;θ ⊕ θ̂t ), y)] + λ · R(θ̂t )
θ̂t

Datasets and benchmarks. We integrate widely-used
datasets, including CIFAR-10, CIFAR-100, TinyImageNet,
and the more challenging ImageNet-R. For evaluating domain adaptation, the framework also incorporates the standard
5-datasets cross-domain benchmark (comprising CIFAR-10,
MNIST, Fashion-MNIST, SVHN, and notMNIST) specifically
designed for evaluating domain adaptation capabilities in continual learning scenarios.
Evaluation metrics. While various performance metrics
have been proposed in continual learning to evaluate model
performance, we adopt two standard metrics in our experiments due to their widespread adoption and the convenience
they offer for comparative analysis [13] [70]. Let At,j ∈ [0, 1]
denote the accuracy evaluated on the test set of the j-th task
after incrementally learning up to the t-th task, where j ≤ t.
The Last Accuracy (AT ) is defined as the average accuracy
across all tasks after completing the entire sequence of T tasks:

(8)
s.t.

R(·) = ||θ̂t ||sparse .

Here, θ is typically frozen to ensure stability, while θ̂t provides
plasticity. The operator ⊕ signifies how these parameter sets
are combined, such as through masking, additive decomposition, or modular routing. R(·) is often used to enforce constraints like sparsity, ensuring the model’s growth is scalable.
Early methods focused on parameter isolation within a
fixed-capacity model [63] [64] [65] [66] [67] [56] [64] [65].
These methods, while effective, were often designed for
models trained from scratch. With the advent of PTM, θ̂t is
commonly realized through Parameter-Efficient Fine-Tuning
(PEFT) techniques. Examples include constraining LoRA matrices [11], [12] or utilizing Mixture-of-Experts [13].
Architecture-based methods address the stability-plasticity
dilemma structurally by freezing the general knowledge base
(θ) while enabling targeted updates via θ̂t . However, they face
significant challenges in CIL setting, as selecting the correct
task-specific parameters θ̂t without a task identity oracle is
non-trivial. Moreover, as the number of tasks grows, naively
accumulating task-specific parameters can lead to a linear or
super-linear growth in model size. The future of this domain
lies in developing more sophisticated strategies for managing
θ̂t . Instead of simple expansion, the focus is shifting towards
intelligent parameter reuse, composition, and merging.
In LibContinual, we implement API [56], InfLoRA [11],
MoE-Adapter4CL [13], and SD-LoRA [12], representing both
training-from-scratch and PTM-based methods.

1 X
AT,j .
T j=1

(9)

The Average Accuracy (A) is defined as the average of
accuracies measured immediately after learning each task:
T

A=

1 X
At .
T t=1

(10)

These complementary metrics provide insights into both
the model’s final performance stability (AT ) and its learning
trajectory characteristics throughout the continual learning
process (A).
## IV. Investigating the Implicit Assumptions of
Continual Learning by LibContinual
Leveraging its unified and reproducible framework, LibContinual provides an ideal platform for the rigorous and
fair evaluation of diverse continual learning algorithms. While
the proliferation of CL methods has yielded impressive results on standard benchmarks, we observe that prevailing
CL evaluation paradigms often rest on idealized, implicit
assumptions, which can lead to an overestimation of the realworld applicability of these algorithms. In this section, we
formally identify these assumptions and introduce the corresponding investigative dimensions supported by LibContinual.
Specifically, we systematically identify and investigate the
following three assumptions: (1) the availability of offline
data accessibility, (2) intra-task semantic homogeneity, and (3)
unregulated memory resources.

D. Components and Benchmarks Supported in Libcontinual
To ensure comprehensive and reproducible experiments,
LibContinual provides a modular suite of standardized components, backbones, and benchmarks.
Backbone architectures. The framework supports
both classic Convolutional Neural Networks (CNNs) like
AlexNet [68], ResNet-18, and ResNet-32 [69], as well as
modern Pre-trained Models such as the Vision Transformer
(ViT) [60] and CLIP [59].

A. Investigation of Assumption of Offline Data Accessibility
The first assumption we scrutinize is the assumption of
offline data accessibility. A foundational convention in many
CL evaluations is that the entire dataset Dt for an incoming
task is available to the learner, permitting multi-epoch training.
This offline paradigm allows models to achieve thorough
convergence by repeatedly optimizing over the task data before
advancing to the next task.


Car

Cat

Features

Parameter-based storage
Continual Learner

/
Model

New Model

Prompt-based storage
Prompt Pool

Parameter 1

Prompt 1

Parameter N

Prompt N

...

Prompt

Old Model

...

Parameter

Model

...

Feature

...

...

...

The third critical assumption we scrutinize is the Assumption of Unregulated Memory Resources. In standard CL evaluations, methods are frequently compared solely on accuracy,
with memory usage treated as a secondary or loosely defined constraint. This practice implicitly assumes that different
forms of memory, whether raw pixels, abstract features, or
model parameters, are interchangeable or negligible in cost.
However, this assumption obscures a notable flaw in comparative analysis: methods are not evaluated on an equitable
basis. First, the quantity of auxiliary memory required varies
dramatically between methods [7], [14], [15], [50]. More
fundamentally, the qualitative nature of the stored information
is heterogeneous. For instance, replay methods store raw image
samples [7], while others retain abstract features [6], [16], or
even task-specific parameters [56], [57]. This qualitative diversity renders direct comparison impossible without a unified
standard to account for the specific costs of these disparate
storage forms.
To address this challenge and enable fair comparison,
we introduce the unified memory budget protocol within
LibContinual. This protocol is guided by a novel storagecentric taxonomy, illustrated in Figure 5. We strictly categorize
methods based on their form of preserved knowledge into
five distinct types: Image-based, Feature-based, Model-based,
Parameter-based, and Prompt-based. Crucially, LibContinual
converts these qualitatively different storage forms into a
single quantitative metric: total memory usage in Megabytes
(MB). By enforcing a strict, unified budget across all methods,
we make their cost-benefit trade-offs explicit. This allows
researchers to equitably assess whether the performance gain
of a method justifies its specific memory overhead. Below,
we detail the characteristics and trade-offs of each storage
category supported by our framework.

Image

Image-based storage Feature-based storage Model-based storage
...

B. Investigation of Assumption of Unregulated Memory Resources

Unified Memory Budget

...

However, this assumption contrasts with realistic scenarios,
where data arrives as a single-pass stream [24], [71]. In realworld applications, such as autonomous robots learning on the
fly and edge devices processing sensor feeds, data samples
are often ephemeral. In this case, they must be processed
immediately and cannot be stored for repeated offline rehearsal
due to strict latency constraints. This assumption is further
challenged in the era of large foundation models, where
growing privacy concerns and data regulations often prohibit
the long-term storage of raw incoming user data, mandating
a “train-once” paradigm. The discrepancy between the offline
assumption and the online reality conceals critical weaknesses
in a model’s learning efficiency, specifically its ability to adapt
rapidly from limited data exposure.
To address this, we introduce the Data Stream Dimension
of investigation within LibContinual. Through a strict online
continual learning (online CL) setting, LibContinual enables
a systematic evaluation of the learning efficiency and stability
across diverse methods, directly investigating the prevalent
assumption of multi-epoch data access.

PTM

Fig. 5: The taxonomy of continual learning methods from a
storage-centric perspective. The five categories, image-based,
feature-based, model-based, parameter-based, and promptbased, are illustrated with representative examples of the type
of content stored in memory.
1) Image-based storage: Methods such as iCaRL [7],
BiC [48], LUCIR [49], WA [50], OCM [24], and ERAML/ERACE [25] rely on storing raw input-label pairs (x, y).
Since these methods preserve the highest-fidelity representations of the original data distributions Dt , rehearsal is
grounded in authentic samples, providing a robust defense
against evaluation bias. However, this advantage comes with
significant costs: storing raw data incurs substantial memory
overhead and raises privacy concerns regarding sensitive inputs. Furthermore, the limited buffer size creates an inherent
data imbalance, often biasing models toward new classes.
Consequently, these methods require sophisticated exemplar
selection strategies, such as herding [7] or diversity maximization, to optimize the utility of the limited storage capacity.
2) Feature-based storage: Methods such as LwF [6],
GPM [10], TRGP [52], API [56], InfLoRA [11], and
RAPF [16] store compressed intermediate representations or
gradients to mitigate forgetting. Compared to raw inputs, this
paradigm offers a more compact footprint and better satisfies
privacy constraints by avoiding the retention of original pixels.
However, a critical limitation is the loss of representational
detail. Stored data consists of abstracted high-level semantic
features. These approximations inevitably lose fine-grained
information present in the source data. As the number of
tasks increases, this information loss accumulates, potentially
capping the model’s final performance. Accordingly, recent
methods focus on enhancing the fidelity of these feature
representations to address this bottleneck.
3) Model-based storage: Methods such as EWC [5],
BIC [48], LUCIR [49], WA [50], and CoMA [72] utilize
model snapshots rather than data samples. This paradigm
offers significant privacy advantages by strictly avoiding data
retention. Furthermore, by storing complete or partial states
of previous models, they provide a comprehensive reference
for knowledge distillation, effectively stabilizing the learning
trajectory. However, the scalability of model storage is a
major challenge. With the growing size of modern foundation models, storing even a single historical snapshot can
be prohibitively expensive. Consequently, these methods face
a critical trade-off between the stability provided by model
snapshots and the severe constraints of storage capacity.
4) Parameter-based storage: Methods such as RanPAC [15], MoE-Adapter4CL [13], and RAPF [15] employ dynamically increasing learnable parameters. This involves freez-


TABLE II
E XPERIMENTAL RESULTS FOR THE REPRODUCTION OF CL METHODS . TASK SETTINGS FOLLOW THE FORMAT “ B X- INC - TASK ”, WHERE
“ B X” DENOTES THE TOTAL NUMBER OF BASE CLASSES , “ INC ” DENOTES THE NUMBER OF CLASSES PER INCREMENTAL TASK , AND
“ TASK ” DENOTES THE TOTAL NUMBER OF TASKS . “AVG .” AND “L AST.” REFER TO “AVERAGE ACCURACY ” AND “L AST ACCURACY ”,
RESPECTIVELY, AS DEFINED IN S ECTION III-D. T HE “R EPORTED ” COLUMN SHOWS THE RESULTS FROM THE ORIGINAL PAPERS , WHILE
THE “O URS ” COLUMN SHOWS THE RESULTS REPRODUCED WITH THE L IB C ONTINUAL . A LL METHODS ARE ARRANGED IN
CHRONOLOGICAL ORDER OF THEIR PUBLICATION .
Method

Backbone

Buffer

Learning Rate/Optimizer/Decay

Task Setting

TIL/CIL

Last./Avg.

Reported

Ours

CIL

Avg.
Avg.

44.40
54.40

44.88
56.38

LwF [6]

ResNet32

0

0.3/SGD/Step

b0-10-10
b0-20-5

EWC [5]

ResNet32

0

0.1/SGD/Step

b0-10-10
b0-20-5

CIL

Last.
Last.

13.10
21.90

10.95
20.55

iCaRL [7]

ResNet32

2000

0.05/SGD/Step

b0-10-10
b0-20-5

CIL

Avg.
Avg.

64.10
67.20

63.67
66.83

BiC [48]

ResNet32

2000

0.1/SGD/Step

b20-20-5
b50-50-2

CIL

Last.
Last.

56.69
63.00

54.09
63.03

LUCIR [49]

ResNet32

2000

0.1/SGD/Step

b50-10-6
b50-5-11

CIL

Avg.
Avg.

63.42
60.18

62.34
58.22

WA [50]

ResNet32

10000

0.1/SGD/Step

b0-20-5
b0-10-10

CIL

Last.
Last.

59.20
52.40

58.58
51.62

GPM [10]

AlexNet-5

0

0.01/SGD/PatienceSchedule

b10-10-10

TIL

Last.

72.48

74.43

ERAML [25]

ResNet18

10000

0.1/SGD/Constant

b0-5-20

CIL

Last.

24.30

18.07

ERACE [25]

ResNet18

10000

0.1/SGD/Constant

b0-5-20

CIL

Last.

25.80

26.04

TRGP [52]

AlexNet-5

0

0.01/SGD/PatienceSchedule

b0-10-10

TIL

Last.

74.46

78.22

L2P [14]

ViT-B/16

0

0.03/Adam/Constant

b0-10-10

CIL

Last.

83.83

82.85

OCM [24]

ResNet18

5000

0.001/Adam/Constant

b0-10-10
b0-2-50

CIL

Last.
Last.

42.40
42.20

43.91
42.77

DualPrompt [57]

ViT-B/16

0

0.001/Adam/Cosine

b0-10-10

CIL

Last.

83.05

83.22

API [56]

AlexNet-5

0

0.01/SGD/PatienceSchedule

b5-5-20

TIL

Last.

81.40

80.93

CodaPrompt [58]

ViT-B/16

0

0.001/Adam/Step

b0-10-10

CIL

Last.

86.25

85.33

CIL

Last.
Last.

92.20
92.40

92.43
91.83

86.51

86.54

RanPAC [15]

ViT-B/16

0

0.01/SGD/Cosine

b0-20-5
b0-10-10

InfLoRA [11]

ViT-B/16

0

0.0005/Adam/Step

b0-10-10

CIL

Last.

MoE-Adapter4CL [13]

CLIP-ViT-B/16

0

0.001/AdamW/Step

b0-10-10

CIL

Last.

77.52

78.91

RAPF [16]

CLIP-ViT-B/16

0

0.001/Adam/Step

b0-10-10

CIL

Avg.

86.19

85.53

ViT-B/16

0

0.008/SGD/Constant

b0-10-10

CIL

Avg.

92.54

91.63

SD-LoRA [12]

ing the backbone and allocating dedicated parameter blocks,
such as Adapters or Experts, for new tasks. This paradigm allows for precise control over plasticity and stability. However,
the efficiency of this expansion is difficult to manage. Setting
appropriate parameter dimensions is non-trivial; excessively
large blocks waste memory, while overly limited ones impair
fitting. Furthermore, knowledge transfer across tasks is often
hindered. Since parameters are frequently isolated per task or
expert, effective sharing and reuse of learned representations
remain a challenge. This suggests that while storage-efficient,
the structural utilization of these parameters in CIL and DIL
settings requires further improvement.
5) Prompt-based storage: Methods such as L2P [14], DualPrompt [57], and CODA-Prompt [58] store a small number
of learnable tokens (prompts) that condition a frozen PTM.
This storage paradigm represents the extreme of efficiency. It
enables rapid adaptation through lightweight updates and has
shown remarkable performance in online scenarios. However,
the effectiveness is inextricably linked to the quality of the
underlying PTM. This dependency suggests that performance
gains may stem more from the frozen backbone’s generality
than the prompt mechanism itself. Additionally, finding a

global optimal solution within the extremely limited parameter
space of prompts remains an open optimization challenge.
C. Investigation of Assumption of Intra-task Semantic Homogeneity
The second assumption is the Assumption of Intra-Task
Semantic Homogeneity. In standard benchmark constructions,
whether in traditional or cross-domain settings described in
Section III-B3, tasks are almost invariably formed by grouping
semantically related classes. For instance, a single task might
consist entirely of vehicles, animals, or handwritten digits.
However, we argue that this widely accepted convention
implicitly relies on a critical, unexamined assumption: IntraTask Semantic Homogeneity. This design provides an implicit
contextual shortcut, enabling the model to leverage task-level
semantic regularities to simplify learning. Consequently, this
evaluation practice fails to distinguish if the model can learn
robust, independent class representations. This convention
systematically overestimates a model’s true continual learning
ability, as its success may hinge on exploiting these convenient
but unrealistic structural regularities rather than on a genuine
capacity to manage a disorganized knowledge base.


In real-world applications, new concepts may arrive without
semantic ordering. For instance, a home robot may need to
learn a new plant and new shoes on the same day, driven by
daily events. Similarly, a retail inventory system might process
a shipment containing both new smartphones and organic
snacks, grouped by logistical convenience rather than category. In these realistic scenarios, the assumption of semantic
coherence breaks down.
To systematically investigate the impact of this assumption,
we introduce the Semantic Structure Dimension of investigation within LibContinual. The core of this investigation is the
category-randomized setting, a novel and rigorous evaluation
protocol designed to strip away semantic shortcuts.
In contrast to existing setups, the category-randomized setting is defined by both low intra-task and low inter-task semantic similarity, as shown in Figure 3. LibContinual implements
this by first aggregating all available classes from a diverse
pool of datasets (e.g., combining CIFAR-10, MNIST, SVHN,
etc.) and then randomly shuffling them before partitioning
them into tasks. This process deliberately breaks any semantic
locality. As a result, a single task Tt becomes a semantically
heterogeneous mixture, potentially containing the digit ‘7’
alongside images of ‘dogs’ and ‘airplanes’.
This challenging setup eliminates the implicit semantic
context at the task level. By preventing the model from
using task-level regularities as a contextual cue, the categoryrandomized setting forces the model to learn disparate concepts simultaneously and maintain discriminative boundaries
between unrelated classes. It thereby forces the model to
learn more general and robust representations for each class
independently, providing a truer test of its ability to overcome
catastrophic forgetting.

## V. Experimental Results by LibContinual
A. Implementation Verification
To validate our re-implementation, we adopt the original
settings of 19 continual learning methods (Section III-C) and
systematically reproduce them using the unified LibContinual
framework. Specifically, we employ the task partitioning settings as described in their respective papers, and utilize two
commonly used metrics (Last accuracy and Average accuracy).
The experiments are rigorously conducted in accordance with
the backbones, buffer sizes (i.e., the number of stored images),
learning rates, optimizers, and decay schedules specified in the
original settings, and are performed under five distinct random
seed configurations. As shown in Table II and Figure 6, the discrepancies between our reproduced results and the originally
reported ones fall within an acceptable range. Specifically, for
most methods, the absolute differences in their performance
metrics are within ±2%. However, some methods do not utilize
multiple random seeds in their experiments, which leads to a
certain degree of result variation. The current experimental
results sufficiently confirm the accuracy of the reproduction
functionality provided by LibContinual.

5HSRUWHGYV2XUV
/Z)
(:&
L&D5/
%L&
/8&,5
:$
*30
(5$0/
(5$&(
75*3
/3
2&0
'XDO3URPSW
$3,
&RGD3URPSW
5DQ3$&
,QI/R5$
0R($GDSWHU&/
5$3)
6'/R5$






5HSRUWHG


























$FFXUDF\











2XUV
























Fig. 6: Comparison of reproduced accuracies among different
continual learning methods (Reported vs Ours).
B. Investigation 1: The Impact of Offline Data Accessibility
in Online CL
In applications requiring rapid adaptation to streaming data
(e.g., robot perception, real-time recommendation systems),
models must continuously learn under stringent constraints.
Specifically, prevailing online CL methods [24] [25] simulate
real-world environments using settings with epoch=1 and
batchsize=10, and LibContinual also adopts such settings.
Experiments (Table III) reveal a significant performance divergence between training-from-scratch methods and PTM-based
approaches, motivating the following analysis.
1) Training-from-scratch methods struggle in online CL:
Traditional continual learning methods, which are typically designed under the assumption of multi-epoch training for stable
convergence, exhibit catastrophic performance degradation in
online settings where data is presented in a single pass. As evidenced in Table III, these methods suffer from severe accuracy
collapse, often approaching near-random performance levels.
For instance, on CIFAR-10, EWC achieves only 10% accuracy,
while BiC drops to a mere 2.23% on TinyImageNet. This
failure is primarily attributed to inadequate model fitting, as
these methods lack the opportunity for repeated data exposure.
Consequently, they are unable to sufficiently optimize their
complex parameter sets, leading to rapid forgetting and an
inability to assimilate new knowledge effectively. In contrast,
methods with a frozen pretrained backbone like L2P perform
markedly better. They operate within compact and efficient
parameter subspaces enabled by prompt tuning or random
projection layers. This design facilitates rapid convergence
and strong results even under the strict single-epoch training
constraint. This significant performance gap underscores the
dominant role of pre-trained representations in ensuring online learning efficiency, effectively overshadowing algorithmic
optimizations tailored for training-from-scratch methods.
2) Need for more challenging benchmarks: While PTMbased methods consistently achieve high performance in online
continual learning, their results on conventional benchmarks
such as CIFAR-100 and TinyImageNet tend to be highly
homogeneous, thereby limiting the ability to discern nuanced
differences in adaptation efficiency. As illustrated in Table
III, top-performing methods often cluster within a narrow
performance band, for example, DualPrompt (76.22%) and
MoE-Adapter4CL (79.42%) on CIFAR-100, making it difficult


TABLE III
C OMPREHENSIVE EVALUATION OF VARIOUS METHODS IN ONLINE CONTINUAL LEARNING SETTING . Base INDICATES THE TRAINING
PARADIGM : PTM-based ( PRE - TRAINED MODEL BASED CONTINUAL LEARNING ) OR Training-from-scratch ( TRAINING - FROM - SCRATCH
CONTINUAL LEARNING ). T HE BEST RESULTS ARE IN BOLD , AND THE SECOND - BEST ARE UNDERLINED .
Method
LwF [6]
EWC [5]
iCaRL [7]
BiC [48]
LUCIR [49]
WA [50]
GPM [10]
ERAML [25]
ERACE [25]
TRGP [52]
API [56]
L2P [14]
OCM [24]
DualPrompt [57]
CodaPrompt [58]
RanPAC [15]
InfLoRA [11]
MoE-Adapter4CL [13]
RAPF [16]
SD-LoRA [12]

Base
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
Training-from-scratch
PTM-based
PTM-based
PTM-based
PTM-based
PTM-based
PTM-based
PTM-based
PTM-based
PTM-based

CIFAR10

CIFAR100

TinyImageNet

ImageNet-R

Last Acc.

Avg Acc.

Last Acc.

Avg Acc.

Last Acc.

Avg Acc.

Last Acc.

Avg Acc.

26.60 ± 1.25
10.00 ± 0.00
42.78 ± 2.43
27.62 ± 3.44
23.63 ± 2.59
37.18 ± 5.67
29.24 ± 0.78
50.82 ± 1.99
48.35 ± 5.70
27.06 ± 0.34
26.66 ± 1.57
87.61 ± 3.51
77.91 ± 2.15
82.34 ± 1.85
84.48 ± 3.30
94.42 ± 2.61
86.72 ± 5.73
89.21 ± 5.35
94.39 ± 0.36
89.16 ± 1.15

46.54 ± 4.52
35.91 ± 3.69
55.71 ± 6.45
45.79 ± 2.84
45.02 ± 2.71
52.94 ± 2.42
47.00 ± 2.57
65.64 ± 1.81
65.57 ± 1.92
46.73 ± 2.56
44.44 ± 2.89
93.70 ± 1.05
82.36 ± 1.59
91.00 ± 1.15
91.23 ± 2.62
98.10 ± 0.71
92.32 ± 3.05
94.34 ± 1.49
96.62 ± 0.61
94.37 ± 0.48

9.22 ± 0.73
5.27 ± 0.45
16.16 ± 1.40
5.97 ± 0.66
6.51 ± 0.64
9.52 ± 1.04
13.40 ± 0.23
21.67 ± 0.56
24.71 ± 0.21
13.36 ± 0.40
12.85 ± 0.35
79.07 ± 1.22
41.20 ± 0.81
76.22 ± 0.41
81.73 ± 0.14
88.14 ± 0.84
82.96 ± 0.58
79.42 ± 0.21
71.54 ± 1.55
82.78 ± 0.55

13.53 ± 0.94
11.51 ± 1.20
19.74 ± 1.64
13.00 ± 0.86
12.81 ± 0.88
18.61 ± 1.03
22.49 ± 1.14
28.07 ± 0.77
32.42 ± 0.57
23.01 ± 1.29
26.27 ± 0.54
84.68 ± 0.99
44.00 ± 1.69
83.28 ± 0.72
87.17 ± 0.70
93.27 ± 0.57
88.99 ± 0.31
86.03 ± 0.43
80.74 ± 0.97
88.73 ± 0.31

7.49 ± 0.48
5.00 ± 0.77
10.54 ± 0.88
2.23 ± 0.26
3.10 ± 0.44
3.99 ± 0.58
2.41 ± 0.12
15.29 ± 0.92
20.62 ± 1.09
2.09 ± 0.13
1.67 ± 0.05
82.47 ± 0.43
20.04 ± 0.32
81.21 ± 0.29
84.42 ± 0.40
84.09 ± 0.43
80.33 ± 0.49
76.68 ± 0.08
81.65 ± 0.92
88.72 ± 0.39

11.05 ± 0.62
9.37 ± 0.90
12.87 ± 1.78
4.85 ± 0.72
6.94 ± 1.00
9.17 ± 0.35
5.13 ± 0.33
20.32 ± 0.54
26.53 ± 1.17
5.00 ± 0.22
5.11 ± 0.11
87.09 ± 0.28
24.80 ± 0.84
86.06 ± 0.76
88.89 ± 0.41
90.33 ± 0.23
86.96 ± 0.42
83.71 ± 0.43
85.92 ± 0.59
92.67 ± 0.62

2.38 ± 0.38
1.52 ± 0.14
2.98 ± 0.98
1.07 ± 0.47
1.48 ± 0.35
2.62 ± 0.26
2.77 ± 0.42
4.75 ± 0.86
7.39 ± 0.79
3.08 ± 0.48
1.84 ± 0.33
62.78 ± 0.93
2.12 ± 0.41
62.76 ± 0.59
68.87 ± 0.83
69.70 ± 0.48
67.36 ± 1.34
86.59 ± 1.11
79.52 ± 0.29
75.34 ± 0.57

4.06 ± 0.64
2.81 ± 0.52
4.83 ± 1.12
3.48 ± 0.31
3.92 ± 0.50
5.98 ± 0.60
7.36 ± 0.84
7.14 ± 0.80
11.03 ± 0.85
7.45 ± 1.00
4.56 ± 0.95
67.42 ± 1.59
4.27 ± 0.50
69.45 ± 1.54
75.14 ± 0.49
76.10 ± 1.16
73.63 ± 2.32
90.55 ± 1.07
84.08 ± 0.43
78.32 ± 2.81

to evaluate relative strengths in model plasticity or stability. In
contrast, more complex and semantically diverse datasets like
ImageNet-R reveal significant variations in capability, particularly among ViT-based models. For instance, while MoEAdapter4CL attains 86.59% on ImageNet-R, DualPrompt
achieves only 62.76%, highlighting critical differences in robustness and representational flexibility. Meanwhile, trainingfrom-scratch methods universally collapse to accuracies below
8% on this challenging benchmark, further exposing their limitations. These observations suggest that the current community
reliance on relatively simple datasets such as CIFAR-100 or
TinyImageNet is insufficient for driving meaningful progress
in online continual learning. We therefore advocate for the
adoption of richer, more complex benchmarks like ImageNetR to better expose methodological distinctions and guide the
development of more adaptive and scalable ViT-focused online
CL algorithms.
C. Investigation 2: Algorithmic Efficiency under a Unified
Memory Budget
A critical limitation in current continual learning research
is the lack of a standardized framework for evaluating memory
overhead, which often makes direct comparisons of reported
accuracies misleading. To address this, we conduct a rigorous,
storage-centric analysis through the proposed LibContinual
toolbox. We recognize that the total memory footprint of a
continual learning system is composed of two main parts: the
static memory for the network backbone and the dynamic,
additional storage required by the specific CL strategy. Since
different approaches may employ backbones of varying sizes
(e.g., ResNet [69] vs. ViT [60]), their static memory costs
differ, making total footprint comparisons inequitable.
For a fair and direct comparison of algorithmic efficiency,
we introduce the unified memory budget. This budget is
defined as the total additional memory, measured in megabytes
(MB), that an algorithm requires beyond the backbone’s own
parameters. Detailed methodology regarding memory calculation can be found in the Appendix C. This meticulous

accounting ensures a fair comparison by encompassing all
sources of extra memory cost, including: 1) Image-based
storage for raw data exemplars; 2) Feature-based storage
for intermediate representations or gradients; 3) Model-based
storage for snapshots of past models needed for regularization
or distillation; 4) Parameter-based storage for dynamically
expanded network modules such as adapters or new projection
layers; and 5) Prompt-based storage for learnable prompt tokens. By unifying these qualitatively distinct forms of memory
under a single quantitative metric, we can set uniform memory
budgets to observe how the performance of different methods
changes as storage increases.
As illustrated in Figure 7, our experiments are conducted
on four benchmark datasets: CIFAR-10, CIFAR-100, TinyImageNet, and ImageNet-R. Methods are categorized into
two groups based on their training paradigm: those trained
from scratch and those leveraging pre-trained models. Notably,
certain methods incapable of scaling their memory usage are
represented as fixed points in the plots, reflecting their static
memory allocation.
1) Analysis of training-from-scratch methods: For methods
trained from scratch, the experimental plots reveal a clear,
though often inefficient, positive correlation between memory
consumption and last accuracy. Replay-based methods, such
as iCaRL, LUCIR, and ERACE, consistently demonstrate that
increasing the memory allocated for an image buffer leads to
significant performance gains. On CIFAR-10, for instance, the
accuracy of iCaRL improves dramatically from approximately
35% to over 90% as the memory budget expands from 4 MB
to 100 MB, highlighting the substantial benefit of rehearsing
past data. However, this strategy exhibits inefficiency and
diminishing returns. A particularly illustrative case is WA,
which consumes nearly 100 MB of memory but achieves substantially lower final accuracy (82.28%) compared to iCaRL
(91.44%) at a comparable 100 MB budget, demonstrating
iCaRL’s superior memory efficiency.
In contrast, low-memory strategies that rely on model regularization, such as EWC and LwF, consistently occupy the low-


(a) Comparison of last accuracy for training-from-scratch methods and PTM-based methods on different memory configurations on
CIFAR-10.

(b) Comparison of last accuracy for training-from-scratch methods and PTM-based methods on different memory configurations on
CIFAR-100.

(c) Comparison of last accuracy for training-from-scratch methods and PTM-based methods on different memory configurations on
TinyImageNet.

(d) Comparison of last accuracy for training-from-scratch methods and PTM-based methods on different memory configurations on
ImageNet-R.

Fig. 7: Comparison of last accuracy achieved by the training-from-scratch methods and PTM-based methods across different
memory configurations on various datasets.


TABLE IV
C ROSS - DOMAIN AND CATEGORY- RANDOMIZED CONTINUAL LEARNING RESULTS ON 5- DATASETS BENCHMARK . T HE ‘T YPE ’ COLUMN
INDICATES THE CORE ALGORITHMIC STRATEGY. I N THE ‘D IFFERENCE ’ COLUMNS , SIGNIFICANT GAINS (≥8) ARE IN BLUE ,
SIGNIFICANT LOSSES (≥8) ARE IN RED , AND MINOR CHANGES (<8) ARE IN GREEN .
Method
LwF [6]
EWC [5]
iCaRL [7]
BiC [48]
LUCIR [49]
WA [50]
GPM [10]
ERAML [25]
ERACE [25]
TRGP [52]
L2P [14]
OCM [24]
DualPrompt [57]
API [56]
CodaPrompt [58]
RanPAC [15]
InfLoRA [11]
MoE-Adapter4CL [13]
RAPF [16]
SD-LoRA [12]

Type
Regularization
Regularization
Replay
Replay
Replay
Replay
Optimization
Replay
Replay
Optimization
Representation
Replay
Representation
Architecture
Representation
Representation
Architecture
Architecture
Representation
Architecture

Cross-Domain Setting

Category-Randomized Setting

Difference (Cat-R - Cross-D)

Last Acc.

Avg Acc.

Last Acc.

Avg Acc.

∆ Last Acc.

∆ Avg Acc.

39.79 ± 4.55
26.24 ± 4.93
81.18 ± 0.88
51.64 ± 0.75
66.69 ± 0.67
83.56 ± 0.40
69.87 ± 1.09
84.11 ± 0.38
85.85 ± 0.45
60.43 ± 0.78
64.69 ± 0.68
83.72 ± 0.64
73.53 ± 1.52
62.85 ± 3.55
71.54 ± 1.87
87.10 ± 0.07
83.67 ± 0.93
52.94 ± 3.14
87.88 ± 0.12
69.03 ± 1.33

64.23 ± 1.33
53.24 ± 1.61
85.70 ± 0.29
66.98 ± 0.98
76.94 ± 0.92
87.64 ± 0.22
81.08 ± 0.37
80.22 ± 0.75
81.76 ± 0.64
72.36 ± 0.37
82.69 ± 0.68
78.49 ± 0.46
87.05 ± 1.01
77.89 ± 2.63
86.99 ± 0.99
94.33 ± 0.02
92.78 ± 0.28
77.48 ± 0.91
92.27 ± 0.12
87.78 ± 0.71

54.86 ± 5.45
28.70 ± 5.88
81.79 ± 1.66
47.54 ± 10.34
49.51 ± 6.03
71.51 ± 4.22
62.51 ± 4.59
80.12 ± 0.96
82.69 ± 0.53
54.20 ± 4.44
47.59 ± 1.86
81.40 ± 3.44
52.81 ± 2.03
62.48 ± 1.88
55.35 ± 5.59
58.02 ± 4.16
57.13 ± 9.25
76.78 ± 6.17
80.40 ± 1.57
73.39 ± 9.60

74.12 ± 1.27
49.46 ± 2.42
90.32 ± 0.60
72.19 ± 7.97
74.75 ± 2.90
85.33 ± 1.67
76.43 ± 4.52
86.94 ± 2.06
88.47 ± 1.32
72.51 ± 3.49
67.39 ± 5.72
87.77 ± 1.11
71.21 ± 5.12
77.02 ± 2.29
75.94 ± 3.57
77.05 ± 2.71
77.41 ± 4.29
87.40 ± 2.74
87.57 ± 1.75
83.64 ± 4.90

+15.07
+2.46
+0.61
-4.10
-17.18
-12.05
-7.36
-3.99
-3.16
-6.23
-17.10
-2.32
-20.72
-0.37
-16.19
-29.08
-26.54
+23.84
-7.48
+4.36

+9.89
-3.78
+4.62
+5.21
-2.19
-2.31
-4.65
+6.72
+6.71
+0.15
-15.30
+9.28
-15.84
-0.87
-11.05
-17.28
-15.37
+9.92
-4.70
-4.14

performance corner of the plots. Their inability to effectively
combat catastrophic forgetting on more challenging benchmarks like TinyImageNet and ImageNet-R underscores their
limitations when past data is not accessible. In essence, for
scratch-based methods, performance is predominantly dictated
by the size of the replay buffer. This “brute-force” approach,
while intuitive, is not a scalable or memory-efficient solution
for realistic, resource-constrained lifelong learning scenarios.
2) Analysis of PTM-based methods: The experimental results of PTM-based methods reveals a far more different
phenomenon, challenging the conventional wisdom that more
memory leads to better results. First, across all four datasets, a
high-efficiency “sweet spot” emerges in the low-memory range
(typically under 20 MB). In this region, methods like CodaPrompt, RanPAC, and InfLoRA achieve state-of-the-art or
highly competitive performance at a minimal memory cost. On
the challenging CIFAR-100 benchmark, for instance, RanPAC
achieves a remarkable 90.59% accuracy with only 16.0 MB,
while CodaPrompt attains 83.78% with 15.7 MB. This proves
that with intelligent mechanisms, exceptional performance is
attainable without significant memory overhead.
More significantly, our analysis uncovers a core finding:
more memory does not guarantee better performance and can
be dramatically inefficient. This is best exemplified by comparing L2P with prompt-based methods. On every benchmark,
L2P consumes over 440 MB of memory, yet its performance
is consistently outmatched by CodaPrompt, which uses less
than 4% of that memory. Similarly, RanPAC’s accuracy on
TinyImageNet only improves from 88.33% to 89.55% as its
memory cost explodes from 16.0 MB to 439 MB, highlighting
a severe decline in efficiency. These results strongly suggest
that for PTM-based continual learning, the quality and structure of the stored knowledge are far more critical than the

sheer quantity. Efficient strategies that learn to query and
adapt the vast knowledge already embedded within PTMs
(e.g., CodaPrompt’s dynamic prompting) are more effective
and scalable than those that simply allocate more memory for
new parameters.
In summary, our unified memory analysis provides a crucial perspective for the continual learning community. It
demonstrates that progress should be measured not just by
peak accuracy, but by performance efficiency (accuracy per
megabyte). For future research, the focus should shift away
from memory-intensive replay or naive parameter expansion,
and towards developing sophisticated, low-cost mechanisms to
intelligently manage and access knowledge in powerful pretrained models. This is the key to building truly practical and
scalable lifelong learning systems.
D. Investigation 3: Robustness to Semantic Structure in Crossdomain and Category-randomized Settings
To assess algorithmic robustness against varying semantic
structures, we conduct experiments on the 5-dataset benchmark [73] [10] [52] [14] [57] [56]. We compare performance in
two configurations introduced in Section III-B3: the standard
cross-domain setting and our proposed category-randomized
setting. The latter deliberately breaks this coherence by creating tasks from a shuffled pool of all classes across all domains,
directly testing whether models rely on task-level semantic
shortcuts. The results in Table IV highlight a significant
divergence in robustness across the two settings, revealing
important characteristics of different algorithmic strategies.
1) Analysis of the cross-domain setting: In cross-domain
setting, a clear performance difference emerges between different kinds of methods (Table IV). Methods leveraging either


explicit data rehearsal or powerful pre-trained models prove
most effective at adapting to drastic domain shifts.
Replay-based methods (e.g., ERACE, 85.85% last acc.)
and PTM-based approaches (e.g., RAPF, 87.88%; RanPAC,
87.10%) are the top performers. Their success stems from
rehearsing past data and adapting pretrained features, respectively. In contrast, regularization-based methods like EWC
(26.24%) and LwF (39.79%) fail, as their parameter- or
function-space constraints are insufficient to bridge the large
statistical gaps between domains.
Optimization-based methods like GPM and TRGP yield
intermediate results. GPM, for example, achieves a last accuracy of 69.87%, suggesting that gradient projection can
prevent some interference but may overly restrict the model’s
plasticity, hindering its ability to fully adapt to a new domain.
Finally, the performance of PEFT methods is nuanced. Simpler prompt-based methods like DualPrompt and CodaPrompt
deliver strong but not state-of-the-art results. However, more
sophisticated PEFT techniques like InfLoRA and RAPF are
among the top performers. This demonstrates that the specific
adaptation mechanism is more critical for cross-domain success than merely using a PTM.
2) Analysis of the category-randomized setting: The
category-randomized setting is designed to test genuine robustness by removing the crutch of intra-task semantic coherence.
Comparing performance against the cross-domain setting (Table IV) reveals three distinct behavioral patterns, particularly
when analyzing the change in Last Accuracy. We visualize
this performance shift in Figure 8 to provide a more intuitive
understanding of how each method is affected.
i. Methods exhibiting severe performance degradation. A
key observation is the sharp performance decline of several
high-performing methods when intra-task semantic coherence
is removed. Notably, RanPAC’s accuracy drops by 29.08
percentage points, and similar drops are observed across
prompt-based methods (DualPrompt: -20.72%; L2P: -17.10%;
CodaPrompt: -16.19%).
This collapse in final task performance suggests these
methods heavily exploit task-level semantic regularities as
an implicit inductive bias. When tasks contain semantically
coherent classes, these methods can learn compact, taskspecific representations that capture shared features. However,
when forced to simultaneously learn disparate concepts within
a single task, their task-level adaptation mechanisms become
counterproductive, attempting to find non-existent commonalities among fundamentally unrelated classes. For example, for
RanPAC, its single, fixed random projection layer struggles
to generate sufficiently distinct feature representations for
semantically diverse classes within the same task; for L2P
and DualPrompt, their task-level prompts are forced to find
a compromised solution for heterogeneous tasks, resulting in
suboptimal representations for the unrelated classes.
ii. Methods demonstrating unexpected improvement.
Counter-intuitively, some methods improved under the more
challenging category-randomized conditions. Regularizationbased methods like EWC (+3.9%) and LwF (+15.07%)
have modest gains. This suggests their constraints become
more beneficial when task-level semantic coherence is

>
<

cross-domain

category-randomized

Fig. 8: Performance change from the cross-domain (❍) to the
category-randomized (✩) setting. The plot is divided into a
red-shaded region for methods with a performance drop (❍
> ✩) and a blue-shaded region for those with a performance
gain (❍ < ✩). Methods are sorted by the magnitude of this
change, with the largest drops at the top. Colors denote the
algorithmic type (e.g., Replay, Representation).
removed, as they prevent the model from over-specializing
to spurious task-level patterns. However, their low absolute
performance indicates regularization alone is insufficient for
such heterogeneous tasks.
The most dramatic improvement is observed in MoEAdapter4CL, which exhibits an extraordinary 23.84 percentage
point increase. This remarkable enhancement reveals a fundamental architectural advantage: the mixture-of-experts framework, originally designed to handle inter-task diversity, inadvertently excels when confronted with intra-task heterogeneity.
In the category-randomized setting, each task contains diverse
classes from different domains, effectively creating multiple
implicit sub-tasks within a single task. The routing mechanism
can leverage this diversity by assigning different experts to
handle distinct semantic clusters, transforming what appears
to be a challenge into an opportunity for specialization.
This explains both its under-performance in the homogeneous
cross-domain setting and its success here.
iii. Methods maintaining relative stability. Several methods
demonstrate robustness, with their performance being largely
agnostic to the semantic task composition. iCaRL remains
remarkably stable, with its last accuracy changing by only
+0.61%. Replay-based methods like ERACE (-3.16%) and
ERAML (-3.99%) also show high resilience. Other methods,
including GPM (-7.36%) and RAPF (-7.48%), show moderate but manageable degradation. This stability suggests their
mechanisms operate at a level of abstraction (e.g., exemplar
replay, gradient projection, or decoupled parameter updates)
that is less dependent on the semantic composition of tasks.
Beyond absolute accuracy drops, the category-randomized
setting reveals algorithmic fragility in two other ways. First,
we observe a significant divergence between Last Accuracy
and Average Accuracy for several methods. For example,


replay methods like OCM see their Average Accuracy improve
(e.g., +9.28%) while Last Accuracy slightly falls, masking a
critical final-task decay. We argue that Last Accuracy remains
the more meaningful indicator for real-world capability, as it
assesses the model’s performance on the entire accumulated
knowledge base. Second, the standard deviation, calculated
over multiple runs with different random seeds (as reported
in Table IV), increases for several methods. For instance,
the variance for BiC (10.34), SD-LoRA (9.60), and InfLoRA
(9.25) is notably higher in the category-randomized setting.
This increased variance suggests that their performance might
be more sensitive to factors like initialization or data ordering
when the task structure is less predictable, highlighting a
potential area for improving their robustness.
In summary, the category-randomized setting serves as
a valuable diagnostic. The divergent performance patterns
suggest that a method’s success can be closely tied to the
semantic structure of the tasks. Strategies that appear highly
effective on traditional, semantically coherent benchmarks
may not generalize to scenarios where data arrives in a more
chaotic, unstructured manner. This underscores the importance
of developing methods that are not only accurate but also
robust to variations in the underlying semantic organization
of the learning curriculum.
## VI. Conclusion
In this paper, we present LibContinual, a unified and reproducible library for continual learning that re-implements
and evaluates the major methods under consistent protocols.
Our investigations show that training-from-scratch methods
collapse under the online learning setting, whereas parameterefficient adaptations of pre-trained models achieve strong
accuracy with modest memory usage. We further highlight
the necessity of resource-aware evaluation, demonstrating
that storage forms and budgets are critical to performance.
Moreover, the category-randomized setting reveals that many
approaches rely heavily on semantic coherence, underscoring
the importance of robust strategies for knowledge management
in realistic environments. By consolidating benchmarks, protocols, and metrics, LibContinual offers a reliable foundation
for future research and encourages the development of continual learning methods that balance efficiency, robustness, and
applicability.
## Acknowledgments
This work is supported in part by the National Natural Science Foundation of China (62576160, 62192783),
the Young Elite Scientists Sponsorship Program by CAST
(2023QNRC001), and the Australian Research Council’s Discovery Project (DP220101784).
## References
[1] M. McCloskey and N. J. Cohen, “Catastrophic interference in connectionist networks: The sequential learning problem,” Psychology of
Learning and Motivation, vol. 24, pp. 109–165, 1989.
[2] R. M. French, “Catastrophic forgetting in connectionist networks,”
Trends in cognitive sciences, vol. 3, no. 4, pp. 128–135, 1999.

[3] M. Mermillod, A. Bugaiska, and P. Bonin, “The stability-plasticity
dilemma: Investigating the continuum from catastrophic forgetting to
age-limited learning effects,” Frontiers in psychology, vol. 4, p. 504,
2013.
[4] L. Wang, X. Zhang, H. Su, and J. Zhu, “A comprehensive survey
of continual learning: Theory, method and application,” IEEE Trans.
Pattern Anal. Mach. Intell., vol. 46, no. 8, pp. 5362–5383, 2024.
[5] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins,
A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska,
D. Hassabis, C. Clopath, D. Kumaran, and R. Hadsell, “Overcoming
catastrophic forgetting in neural networks,” Proceedings of the National
Academy of Sciences, vol. 114, no. 13, pp. 3521–3526, 2017.
[6] Z. Li and D. Hoiem, “Learning without forgetting,” in Computer Vision ECCV 2016 - 14th European Conference, Amsterdam, The Netherlands,
October 11-14, 2016, Proceedings, Part IV, ser. Lecture Notes in
Computer Science, B. Leibe, J. Matas, N. Sebe, and M. Welling, Eds.,
vol. 9908. Springer, 2016, pp. 614–629.
[7] S. Rebuffi, A. Kolesnikov, G. Sperl, and C. H. Lampert, “icarl: Incremental classifier and representation learning,” in 2017 IEEE Conference
on Computer Vision and Pattern Recognition, CVPR 2017, Honolulu,
HI, USA, July 21-26, 2017. IEEE Computer Society, 2017, pp. 5533–
5542.
[8] S. Yan, J. Xie, and X. He, “DER: dynamically expandable representation
for class incremental learning,” in IEEE Conference on Computer
Vision and Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021.
Computer Vision Foundation / IEEE, 2021, pp. 3014–3023.
[9] G. M. Van de Ven, H. T. Siegelmann, and A. S. Tolias, “Brain-inspired
replay for continual learning with artificial neural networks,” Nature
communications, vol. 11, no. 1, p. 4069, 2020.
[10] G. Saha, I. Garg, and K. Roy, “Gradient projection memory for continual
learning,” in 9th International Conference on Learning Representations,
ICLR 2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net,
2021.
[11] Y. Liang and W. Li, “Inflora: Interference-free low-rank adaptation for
continual learning,” in IEEE/CVF Conference on Computer Vision and
Pattern Recognition, CVPR 2024, Seattle, WA, USA, June 16-22, 2024.
IEEE, 2024, pp. 23 638–23 647.
[12] Y. Wu, H. Piao, L. Huang, R. Wang, W. Li, H. Pfister, D. Meng, K. Ma,
and Y. Wei, “Sd-lora: Scalable decoupled low-rank adaptation for class
incremental learning,” in The Thirteenth International Conference on
Learning Representations, ICLR 2025, Singapore, April 24-28, 2025.
OpenReview.net, 2025.
[13] J. Yu, Y. Zhuge, L. Zhang, P. Hu, D. Wang, H. Lu, and Y. He, “Boosting
continual learning of vision-language models via mixture-of-experts
adapters,” in IEEE/CVF Conference on Computer Vision and Pattern
Recognition, CVPR 2024, Seattle, WA, USA, June 16-22, 2024. IEEE,
2024, pp. 23 219–23 230.
[14] Z. Wang, Z. Zhang, C. Lee, H. Zhang, R. Sun, X. Ren, G. Su, V. Perot,
J. G. Dy, and T. Pfister, “Learning to prompt for continual learning,”
in IEEE/CVF Conference on Computer Vision and Pattern Recognition,
CVPR 2022, New Orleans, LA, USA, June 18-24, 2022. IEEE, 2022,
pp. 139–149.
[15] M. D. McDonnell, D. Gong, A. Parvaneh, E. Abbasnejad, and A. van den
Hengel, “Ranpac: Random projections and pre-trained models for continual learning,” in Advances in Neural Information Processing Systems
36: Annual Conference on Neural Information Processing Systems 2023,
NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023, A. Oh,
T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, Eds.,
2023.
[16] L. Huang, X. Cao, H. Lu, and X. Liu, “Class-incremental learning
with CLIP: adaptive representation adjustment and parameter fusion,”
in Computer Vision - ECCV 2024 - 18th European Conference, Milan,
Italy, September 29-October 4, 2024, Proceedings, Part LIV, ser. Lecture
Notes in Computer Science, A. Leonardis, E. Ricci, S. Roth, O. Russakovsky, T. Sattler, and G. Varol, Eds., vol. 15112. Springer, 2024,
pp. 214–231.
[17] V. Lomonaco, L. Pellegrini, A. Cossu, A. Carta, G. Graffieti, T. L.
Hayes, M. D. Lange, M. Masana, J. Pomponi, G. M. van de Ven,
M. Mundt, Q. She, K. W. Cooper, J. Forest, E. Belouadah, S. Calderara,
G. I. Parisi, F. Cuzzolin, A. S. Tolias, S. Scardapane, L. Antiga,
S. Ahmad, A. Popescu, C. Kanan, J. van de Weijer, T. Tuytelaars,
D. Bacciu, and D. Maltoni, “Avalanche: An end-to-end library for
continual learning,” in IEEE Conference on Computer Vision and Pattern
Recognition Workshops, CVPR Workshops 2021, virtual, June 19-25,
2021. Computer Vision Foundation / IEEE, 2021, pp. 3600–3610.
[18] A. Douillard and T. Lesort, “Continuum: Simple management of complex continual learning scenarios,” CoRR, vol. abs/2102.06253, 2021.


[19] D. Zhou, F. Wang, H. Ye, and D. Zhan, “Pycil: A python toolbox for
class-incremental learning,” CoRR, vol. abs/2112.12533, 2021.
[20] M. D. Lange, R. Aljundi, M. Masana, S. Parisot, X. Jia, A. Leonardis,
G. G. Slabaugh, and T. Tuytelaars, “A continual learning survey: Defying
forgetting in classification tasks,” IEEE Trans. Pattern Anal. Mach.
Intell., vol. 44, no. 7, pp. 3366–3385, 2022.
[21] D. Zhou, Q. Wang, Z. Qi, H. Ye, D. Zhan, and Z. Liu, “Class-incremental
learning: A survey,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 46,
no. 12, pp. 9851–9873, 2024.
[22] M. Masana, X. Liu, B. Twardowski, M. Menta, A. D. Bagdanov, and
J. van de Weijer, “Class-incremental learning: Survey and performance
evaluation on image classification,” IEEE Trans. Pattern Anal. Mach.
Intell., vol. 45, no. 5, pp. 5513–5533, 2023.
[23] D. Zhou, H. Sun, J. Ning, H. Ye, and D. Zhan, “Continual learning
with pre-trained models: A survey,” in Proceedings of the Thirty-Third
International Joint Conference on Artificial Intelligence, IJCAI 2024,
Jeju, South Korea, August 3-9, 2024. ijcai.org, 2024, pp. 8363–8371.
[24] Y. Guo, B. Liu, and D. Zhao, “Online continual learning through mutual
information maximization,” in International Conference on Machine
Learning, ICML 2022, 17-23 July 2022, Baltimore, Maryland, USA, ser.
Proceedings of Machine Learning Research, K. Chaudhuri, S. Jegelka,
L. Song, C. Szepesvári, G. Niu, and S. Sabato, Eds., vol. 162. PMLR,
2022, pp. 8109–8126.
[25] L. Caccia, R. Aljundi, N. Asadi, T. Tuytelaars, J. Pineau, and
E. Belilovsky, “New insights on reducing abrupt representation change
in online continual learning,” in The Tenth International Conference on
Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022.
OpenReview.net, 2022.
[26] G. M. van de Ven, T. Tuytelaars, and A. S. Tolias, “Three types of
incremental learning,” Nat. Mac. Intell., vol. 4, no. 12, pp. 1185–1197,
2022.
[27] A. Krizhevsky, G. Hinton et al., “Learning multiple layers of features
from tiny images,” 2009.
[28] L. Deng, “The MNIST database of handwritten digit images for machine
learning research [best of the web],” IEEE Signal Process. Mag., vol. 29,
no. 6, pp. 141–142, 2012.
[29] R. Aljundi, F. Babiloni, M. Elhoseiny, M. Rohrbach, and T. Tuytelaars,
“Memory aware synapses: Learning what (not) to forget,” in Proceedings
of the European Conference on Computer Vision (ECCV), vol. 11207.
Springer, 2018, pp. 144–161.
[30] F. Zenke, B. Poole, and S. Ganguli, “Continual learning through synaptic
intelligence,” in Proceedings of the International Conference on Machine
Learning (ICML), ser. Proceedings of Machine Learning Research,
D. Precup and Y. W. Teh, Eds., vol. 70. PMLR, 2017, pp. 3987–3995.
[31] A. Chaudhry, P. K. Dokania, T. Ajanthan, and P. H. S. Torr, “Riemannian
walk for incremental learning: Understanding forgetting and intransigence,” in Proceedings of the European Conference on Computer Vision
(ECCV), ser. Lecture Notes in Computer Science, V. Ferrari, M. Hebert,
C. Sminchisescu, and Y. Weiss, Eds., vol. 11215. Springer, 2018, pp.
556–572.
[32] A. Iscen, J. Zhang, S. Lazebnik, and C. Schmid, “Memory-efficient
incremental learning through feature adaptation,” in Computer Vision ECCV 2020 - 16th European Conference, Glasgow, UK, August 23-28,
2020, Proceedings, Part XVI, ser. Lecture Notes in Computer Science,
A. Vedaldi, H. Bischof, T. Brox, and J. Frahm, Eds., vol. 12361.
Springer, 2020, pp. 699–715.
[33] F. M. Castro, M. J. Marı́n-Jiménez, N. Guil, C. Schmid, and K. Alahari, “End-to-end incremental learning,” in Computer Vision - ECCV
2018 - 15th European Conference, Munich, Germany, September 8-14,
2018, Proceedings, Part XII, ser. Lecture Notes in Computer Science,
V. Ferrari, M. Hebert, C. Sminchisescu, and Y. Weiss, Eds., vol. 11216.
Springer, 2018, pp. 241–257.
[34] A. R. Triki, R. Aljundi, M. B. Blaschko, and T. Tuytelaars, “Encoder
based lifelong learning,” in IEEE International Conference on Computer
Vision, ICCV 2017, Venice, Italy, October 22-29, 2017. IEEE Computer
Society, 2017, pp. 1329–1337.
[35] A. Lewandowski, M. Bortkiewicz, S. Kumar, A. György, D. Schuurmans, M. Ostaszewski, and M. C. Machado, “Learning continually by
spectral regularization,” in The Thirteenth International Conference on
Learning Representations, ICLR 2025, Singapore, April 24-28, 2025.
OpenReview.net, 2025.
[36] Y. Fan, Y. Wang, P. Zhu, D. Chen, and Q. Hu, “Persistence homology distillation for semi-supervised continual learning,” in Advances
in Neural Information Processing Systems 38: Annual Conference on
Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver,
BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey,

D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang, Eds.,
2024.
[37] J. He, H. Guo, M. Tang, and J. Wang, “Continual instruction tuning for
large multimodal models,” CoRR, vol. abs/2311.16206, 2023.
[38] Z. Zheng, M. Ma, K. Wang, Z. Qin, X. Yue, and Y. You, “Preventing
zero-shot transfer degradation in continual learning of vision-language
models,” in IEEE/CVF International Conference on Computer Vision,
ICCV 2023, Paris, France, October 1-6, 2023. IEEE, 2023, pp. 19 068–
19 079.
[39] A. van den Oord, O. Vinyals, and K. Kavukcuoglu, “Neural discrete
representation learning,” in Advances in Neural Information Processing
Systems 30: Annual Conference on Neural Information Processing
Systems 2017, December 4-9, 2017, Long Beach, CA, USA, I. Guyon,
U. von Luxburg, S. Bengio, H. M. Wallach, R. Fergus, S. V. N.
Vishwanathan, and R. Garnett, Eds., 2017, pp. 6306–6315.
[40] R. Aljundi, M. Lin, B. Goujaud, and Y. Bengio, “Gradient based sample
selection for online continual learning,” Advances in neural information
processing systems, vol. 32, 2019.
[41] J. Bang, H. Kim, Y. Yoo, J.-W. Ha, and J. Choi, “Rainbow memory:
Continual learning with a memory of diverse samples,” in Proceedings
of the IEEE/CVF conference on computer vision and pattern recognition,
2021, pp. 8218–8227.
[42] Y. Liu, Y. Su, A.-A. Liu, B. Schiele, and Q. Sun, “Mnemonics training:
Multi-class incremental learning without forgetting,” in Proceedings of
the IEEE/CVF conference on Computer Vision and Pattern Recognition,
2020, pp. 12 245–12 254.
[43] H. Shin, J. K. Lee, J. Kim, and J. Kim, “Continual learning with deep
generative replay,” Advances in neural information processing systems,
vol. 30, 2017.
[44] O. Ostapenko, M. Puscas, T. Klein, P. Jahnichen, and M. Nabi, “Learning
to remember: A synaptic plasticity driven framework for continual
learning,” in Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, 2019, pp. 11 321–11 329.
[45] Y. Cong, M. Zhao, J. Li, S. Wang, and L. Carin, “Gan memory with no
forgetting,” Advances in neural information processing systems, vol. 33,
pp. 16 481–16 494, 2020.
[46] T. L. Hayes, K. Kafle, R. Shrestha, M. Acharya, and C. Kanan, “Remind
your neural network to prevent catastrophic forgetting,” in European
conference on computer vision. Springer, 2020, pp. 466–483.
[47] K. Zhu, W. Zhai, Y. Cao, J. Luo, and Z.-J. Zha, “Self-sustaining
representation expansion for non-exemplar class-incremental learning,”
in Proceedings of the IEEE/CVF conference on computer vision and
pattern recognition, 2022, pp. 9296–9305.
[48] Y. Wu, Y. Chen, L. Wang, Y. Ye, Z. Liu, Y. Guo, and Y. Fu, “Large
scale incremental learning,” in IEEE Conference on Computer Vision
and Pattern Recognition, CVPR 2019, Long Beach, CA, USA, June 1620, 2019. Computer Vision Foundation / IEEE, 2019, pp. 374–382.
[49] S. Hou, X. Pan, C. C. Loy, Z. Wang, and D. Lin, “Learning a
unified classifier incrementally via rebalancing,” in IEEE Conference
on Computer Vision and Pattern Recognition, CVPR 2019, Long Beach,
CA, USA, June 16-20, 2019. Computer Vision Foundation / IEEE,
2019, pp. 831–839.
[50] B. Zhao, X. Xiao, G. Gan, B. Zhang, and S. Xia, “Maintaining discrimination and fairness in class incremental learning,” in 2020 IEEE/CVF
Conference on Computer Vision and Pattern Recognition, CVPR 2020,
Seattle, WA, USA, June 13-19, 2020. Computer Vision Foundation /
IEEE, 2020, pp. 13 205–13 214.
[51] S. Wang, X. Li, J. Sun, and Z. Xu, “Training networks in null space
of feature covariance for continual learning,” in IEEE Conference on
Computer Vision and Pattern Recognition, CVPR 2021, virtual, June
19-25, 2021. Computer Vision Foundation / IEEE, 2021, pp. 184–193.
[52] S. Lin, L. Yang, D. Fan, and J. Zhang, “TRGP: trust region gradient
projection for continual learning,” in The Tenth International Conference
on Learning Representations, ICLR 2022, Virtual Event, April 25-29,
2022. OpenReview.net, 2022.
[53] D. Cheng, Y. Hu, N. Wang, D. Zhang, and X. Gao, “Achieving plasticitystability trade-off in continual learning through adaptive orthogonal
projection,” IEEE Transactions on Circuits and Systems for Video
Technology, 2025.
[54] J. Qiao, Z. Zhang, X. Tan, C. Chen, Y. Qu, Y. Peng, and Y. Xie, “Prompt
gradient projection for continual learning,” in The Twelfth International
Conference on Learning Representations, ICLR 2024, Vienna, Austria,
May 7-11, 2024. OpenReview.net, 2024.
[55] B. Kang, L. Wang, Z. Wu, T. Feng, Y. Li, Y. Gao, and W. Li, “Dynamic
multi-layer null space projection for vision-language continual learning,”
in Proceedings of the IEEE/CVF International Conference on Computer
Vision, 2025, pp. 2077–2086.


[56] Y. Liang and W. Li, “Adaptive plasticity improvement for continual
learning,” in IEEE/CVF Conference on Computer Vision and Pattern
Recognition, CVPR 2023, Vancouver, BC, Canada, June 17-24, 2023.
IEEE, 2023, pp. 7816–7825.
[57] Z. Wang, Z. Zhang, S. Ebrahimi, R. Sun, H. Zhang, C. Lee, X. Ren,
G. Su, V. Perot, J. G. Dy, and T. Pfister, “Dualprompt: Complementary
prompting for rehearsal-free continual learning,” in Computer Vision ECCV 2022 - 17th European Conference, Tel Aviv, Israel, October 23-27,
2022, Proceedings, Part XXVI, ser. Lecture Notes in Computer Science,
S. Avidan, G. J. Brostow, M. Cissé, G. M. Farinella, and T. Hassner,
Eds., vol. 13686. Springer, 2022, pp. 631–648.
[58] J. S. Smith, L. Karlinsky, V. Gutta, P. Cascante-Bonilla, D. Kim,
A. Arbelle, R. Panda, R. Feris, and Z. Kira, “Coda-prompt: Continual decomposed attention-based prompting for rehearsal-free continual
learning,” in IEEE/CVF Conference on Computer Vision and Pattern
Recognition, CVPR 2023, Vancouver, BC, Canada, June 17-24, 2023.
IEEE, 2023, pp. 11 909–11 919.
[59] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal,
G. Sastry, A. Askell, P. Mishkin, J. Clark, G. Krueger, and I. Sutskever,
“Learning transferable visual models from natural language supervision,” in Proceedings of the 38th International Conference on Machine
Learning, ICML 2021, 18-24 July 2021, Virtual Event, ser. Proceedings
of Machine Learning Research, M. Meila and T. Zhang, Eds., vol. 139.
PMLR, 2021, pp. 8748–8763.
[60] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai,
T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly,
J. Uszkoreit, and N. Houlsby, “An image is worth 16x16 words: Transformers for image recognition at scale,” in 9th International Conference
on Learning Representations, ICLR 2021, Virtual Event, Austria, May
3-7, 2021. OpenReview.net, 2021.
[61] G. Zhang, L. Wang, G. Kang, L. Chen, and Y. Wei, “SLCA: slow learner
with classifier alignment for continual learning on a pre-trained model,”
in IEEE/CVF International Conference on Computer Vision, ICCV 2023,
Paris, France, October 1-6, 2023. IEEE, 2023, pp. 19 091–19 101.
[62] H. Cha, J. Lee, and J. Shin, “Co2 l: Contrastive continual learning,” in
2021 IEEE/CVF International Conference on Computer Vision, ICCV
2021, Montreal, QC, Canada, October 10-17, 2021. IEEE, 2021, pp.
9496–9505.
[63] J. Yoon, E. Yang, J. Lee, and S. J. Hwang, “Lifelong learning with
dynamically expandable networks,” in 6th International Conference on
Learning Representations, ICLR 2018, Vancouver, BC, Canada, April
30 - May 3, 2018, Conference Track Proceedings. OpenReview.net,
2018.
[64] J. Serrà, D. Suris, M. Miron, and A. Karatzoglou, “Overcoming catastrophic forgetting with hard attention to the task,” in Proceedings
of the 35th International Conference on Machine Learning, ICML
2018, Stockholmsmässan, Stockholm, Sweden, July 10-15, 2018, ser.
Proceedings of Machine Learning Research, J. G. Dy and A. Krause,
Eds., vol. 80. PMLR, 2018, pp. 4555–4564.
[65] A. Mallya and S. Lazebnik, “Packnet: Adding multiple tasks to a single
network by iterative pruning,” in 2018 IEEE Conference on Computer
Vision and Pattern Recognition, CVPR 2018, Salt Lake City, UT, USA,
June 18-22, 2018. Computer Vision Foundation / IEEE Computer
Society, 2018, pp. 7765–7773.
[66] J. von Oswald, C. Henning, J. Sacramento, and B. F. Grewe, “Continual
learning with hypernetworks,” in 8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30,
2020. OpenReview.net, 2020.
[67] R. Aljundi, P. Chakravarty, and T. Tuytelaars, “Expert gate: Lifelong
learning with a network of experts,” in 2017 IEEE Conference on
Computer Vision and Pattern Recognition, CVPR 2017, Honolulu, HI,
USA, July 21-26, 2017. IEEE Computer Society, 2017, pp. 7120–7129.
[68] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification
with deep convolutional neural networks,” in Advances in Neural Information Processing Systems 25: 26th Annual Conference on Neural
Information Processing Systems 2012. Proceedings of a meeting held
December 3-6, 2012, Lake Tahoe, Nevada, United States, P. L. Bartlett,
F. C. N. Pereira, C. J. C. Burges, L. Bottou, and K. Q. Weinberger, Eds.,
2012, pp. 1106–1114.
[69] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in 2016 IEEE Conference on Computer Vision and Pattern
Recognition, CVPR 2016, Las Vegas, NV, USA, June 27-30, 2016. IEEE
Computer Society, 2016, pp. 770–778.
[70] N. D. Rodrı́guez, V. Lomonaco, D. Filliat, and D. Maltoni, “Don’t forget,
there is more than forgetting: new metrics for continual learning,” CoRR,
vol. abs/1810.13166, 2018.

[71] H. Zhuang, Y. Liu, R. He, K. Tong, Z. Zeng, C. Chen, Y. Wang,
and L. Chau, “F-OAL: forward-only online analytic learning with
fast training and low memory footprint in class incremental learning,”
in Advances in Neural Information Processing Systems 38: Annual
Conference on Neural Information Processing Systems 2024, NeurIPS
2024, Vancouver, BC, Canada, December 10 - 15, 2024, A. Globersons,
L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and
C. Zhang, Eds., 2024.
[72] I. E. Marouf, S. Roy, E. Tartaglione, and S. Lathuilière, “Weighted
ensemble models are strong continual learners,” in Computer Vision
- ECCV 2024 - 18th European Conference, Milan, Italy, September
29-October 4, 2024, Proceedings, Part LXXI, ser. Lecture Notes in
Computer Science, A. Leonardis, E. Ricci, S. Roth, O. Russakovsky,
T. Sattler, and G. Varol, Eds., vol. 15129. Springer, 2024, pp. 306–
324.
[73] S. Ebrahimi, F. Meier, R. Calandra, T. Darrell, and M. Rohrbach,
“Adversarial continual learning,” in Computer Vision - ECCV 2020 - 16th
European Conference, Glasgow, UK, August 23-28, 2020, Proceedings,
Part XI, ser. Lecture Notes in Computer Science, A. Vedaldi, H. Bischof,
T. Brox, and J. Frahm, Eds., vol. 12356. Springer, 2020, pp. 386–402.
[74] A. Maracani, U. Michieli, M. Toldo, and P. Zanuttigh, “RECALL:
replay-based continual learning in semantic segmentation,” in 2021
IEEE/CVF International Conference on Computer Vision, ICCV 2021,
Montreal, QC, Canada, October 10-17, 2021. IEEE, 2021, pp. 7006–
7015.
[75] Z. Meng, J. Zhang, C. Yang, Z. Zhan, P. Zhao, and Y. Wang, “Diffclass:
Diffusion-based class incremental learning,” in Computer Vision - ECCV
2024 - 18th European Conference, Milan, Italy, September 29-October
4, 2024, Proceedings, Part LXXXVII, ser. Lecture Notes in Computer
Science, A. Leonardis, E. Ricci, S. Roth, O. Russakovsky, T. Sattler,
and G. Varol, Eds., vol. 15145. Springer, 2024, pp. 142–159.
[76] X. Rong, J. Zhang, K. He, and M. Ye, “Can: Leveraging clients as
navigators for generative replay in federated continual learning,” in
Forty-second International Conference on Machine Learning.
[77] G. Bellitto, F. P. Salanitri, M. Pennisi, M. Boschini, L. Bonicelli,
A. Porrello, S. Calderara, S. Palazzo, and C. Spampinato, “Saliencydriven experience replay for continual learning,” in Advances in Neural
Information Processing Systems 38: Annual Conference on Neural
Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC,
Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang, Eds., 2024.
[78] H. Wan, S. Ren, W. Huang, M. Zhang, X. Deng, Y. Bao, and L. Nie,
“Understanding the forgetting of (replay-based) continual learning via
feature learning: Angle matters,” in Forty-second International Conference on Machine Learning.
[79] Y. Mahdaviyeh, J. Lucas, M. Ren, A. S. Tolias, R. S. Zemel, and
T. Pitassi, “Replay can provably increase forgetting,” CoRR, vol.
abs/2506.04377, 2025.
[80] M. Farajtabar, N. Azizan, A. Mott, and A. Li, “Orthogonal gradient
descent for continual learning,” in The 23rd International Conference on
Artificial Intelligence and Statistics, AISTATS 2020, 26-28 August 2020,
Online [Palermo, Sicily, Italy], ser. Proceedings of Machine Learning
Research, S. Chiappa and R. Calandra, Eds., vol. 108. PMLR, 2020,
pp. 3762–3773.
[81] H. Liu and H. Liu, “Continual learning with recursive gradient optimization,” in The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022. OpenReview.net,
2022.
[82] G. Zeng, Y. Chen, B. Cui, and S. Yu, “Continual learning of contextdependent processing in neural networks,” Nat. Mach. Intell., vol. 1,
no. 8, pp. 364–372, 2019.


## Appendix A
D ETAILED V ERSION F OR A C LASSIC TAXONOMY OF
C ONTINUAL L EARNING M ETHODS
This appendix provides an expanded discussion of the
classic taxonomy of continual learning methods introduced in
Section III-A of the main paper. It offers a more in-depth
review of the core principles, representative works, and a
critical analysis for each of the five major categories, thereby
offering a richer context for the methodologies evaluated
within LibContinual.
To address the challenges posed by continual learning, a
wide variety of solutions have emerged from different perspectives in the research community. In this section, we begin by
systematically reviewing and categorizing these approaches.
Drawing upon the taxonomy proposed in a recent comprehensive survey by [4], we broadly classify mainstream continual
learning methods into five major categories: regularizationbased, replay-based, optimization-based, representation-based,
and architecture-based methods.In the subsequent subsections,
we will briefly introduce the core principles and representative
works of these categories. A discussion will be provided for
each category, focusing on their distinctive advantages and
unresolved limitations.
A. Regularization-based methods
Regularization-based methods augment the training objective with a penalty term to mitigate forgetting. When learning
task Tt , the parameters θt are found by optimizing,
θt = arg min E(x,y)∼Dt [L(fθ (x), y) + Ω(θ, θt−1 )].
θ

(11)

The objective balances plasticity, driven by the empirical risk
on the new data Dt , with stability, enforced by the regularizer
Ω(θ, θt−1 ) which penalizes deviations from the previous state.
The innovation within this family of methods lies in the
specific design of the regularizer Ω.
The regularizer Ω can be defined in the parameter space, focusing on the importance of individual weights [5], [29], [30],
[31]. For instance, Elastic Weight Consolidation (EWC) [5]
uses a quadratic penalty,
Ω(θ, θt−1 ) =

X

Fi (θi − θt−1,i )2 ,

(12)

i

where θi is the value of the i-th parameter of the model, and
Fi is the diagonal element of the Fisher Information Matrix
(FIM). The FIM serves as a proxy for parameter importance
by penalizing changes to parameters with a high Fi value.
EWC protects weights critical for past tasks.
Alternatively, Ω can be defined in the functional space,
focusing on preserving the model’s input-output behavior [6],
[32], [33], [34]. Learning without Forgetting (LwF) [6] employs knowledge distillation on new data to preserve the
previous model’s outputs. It enforces functional consistency
by treating the old model’s predictions on new data as soft
targets for the new model, defined as,
Ω(θ, θt−1 ) = Ex∼Dt [LKD (fθt−1 (x), fθ (x))].

(13)

The core idea of penalizing important changes continues to
evolve. For instance, recent work has explored regularization

in the spectral domain [35] and the topological domain [36].
Furthermore, researchers have also begun to adapt and apply
these regularization methods to the continual instruction tuning
of large multimodal models [37], [38].
Discussion: Regularization-based methods are foundational
to continual learning due to their simplicity and effectiveness.
However, in the current landscape dominated by Pre-trained
Model (PTM), directly applying a traditional constraint like
EWC across the entire network is often suboptimal [37]. PTMs
possess powerful, general-purpose representations, and imposing strong global constraints can paradoxically limit their
adaptability to new tasks. We believe the future value of the
regularization approach lies in its flexibility as a strategic component rather than a standalone, global solution. For instance,
regularization can be applied more precisely to lightweight
modules in the PTM (such as Adapters), preserving the core
knowledge of the PTM while enabling targeted adaptation.
B. Replay-based methods
Replay-based methods address catastrophic forgetting by
storing a small subset of past data in a memory buffer and
rehearsing it alongside new task data. This strategy directly
counteracts the challenges posed by the non-stationary data
stream by providing the model with explicit reminders of
previously learned knowledge, thereby approximating training
on the union of all data seen so far.
When learning the t-th task Tt , the optimization objective
for replay-based methods is to minimize a composite loss,
min E(x,y)∼Dt [L(fθ (x), y)] + β · E(xm ,ym )∼M [Lm (fθ (xm ), ym )],
θ

M=

t−1
[

Sk .

k=1

(14)

In this formulation, M represents a memory buffer containing
a limited set of exemplars Sk from past tasks. The content
of this buffer M, fundamentally defines the specific replay
strategy. It may contain raw past examples [39] [40] [41] [42],
pseudo-data synthesized by a generative model [43] [44] [45]
[9], or abstract latent representations [46] [47]. Regardless
of the strategy, the model is regularized by minimizing a
replay loss Lm on samples drawn from this buffer. The
hyperparameter β controls the trade-off between learning the
new task and preserving old knowledge. The central challenge
for these methods lies in how to construct, manage, and utilize
the memory buffer M to best approximate the true data
distribution of past tasks under strict memory constraints.
A seminal work in this area is iCaRL [7], which populates
its memory buffer M with exemplars selected via a herding
process and uses knowledge distillation as the replay loss
(Lm in Eq. 14) to preserve the previous model’s outputs.
However, a critical issue with simple replay is the severe data
imbalance between the large number of new task samples and
the few replayed exemplars. This induces a strong predictive
bias towards new classes. Subsequent research has focused
on mitigating this imbalance [49], [50], [48]. For instance,
methods like LUCIR [49] and BiC [48] introduce various


rebalancing techniques, such as cosine normalization or posthoc bias correction.
These challenges of representation stability and data imbalance are further amplified in the demanding online CL setting.
Here, while simple Experience Replay (ER) serves as a strong
baseline, more advanced techniques have emerged. For example, OCM [24] learns more holistic representations via mutual
information maximization to improve feature robustness, while
ER-ACE [25] uses an asymmetric loss to prevent the abrupt
representation drift common at task boundaries.
A significant recent development is the resurgence of generative replay, a strategy that synthesizes pseudo-data for rehearsal [43] [74]. This trend is catalyzed by powerful diffusion
models, which offer a compelling solution to storage and
privacy constraints [75] [76]. Furthermore, innovations are
emerging that replay more abstract forms of knowledge. For
instance, Saliency-driven Experience Replay (SER) proposes
using a forgetting-free saliency prediction network to modulate
and stabilize the features of the main classification model [77].
Concurrently, a deeper theoretical understanding of replay
is emerging, revealing that naive replay can sometimes be
detrimental and motivating the design of more intelligent, nonrandom sampling strategies [78], [79].
Discussion: Replay-based methods remain at the forefront
of continual learning research. Their primary strength lies in
the direct, data-driven constraint against forgetting, an intuitive
strategy that has proven to be highly effective empirically.
While effective, their performance is intrinsically tied to the
size and quality of the memory buffer, creating a tradeoff between memory overhead, potential privacy risks, and
learning efficacy. We argue that future progress hinges on
two key areas: developing more intelligent sampling strategies
to maximize the utility of a limited memory budget, and
establishing a stronger theoretical foundation to explain why
and when replay is most effective. Answering these questions
is essential for unlocking the full potential of replay and
building truly scalable and robust lifelong learning systems.

Optimization-based methods fundamentally seek to address
the stability-plasticity dilemma in continual learning by formulating the learning process as a constrained optimization
problem. The core idea is to ensure that updates performed
for new tasks do not adversely affect the performance on
previously learned tasks [80] [81]. This principle is elegantly
captured by the following constrained optimization objective:
θ

∇Wl Lt = ∇Wl Lt − Ml (Ml )⊤ ∇Wl Lt ,

(16)

where Ml is the basis matrix of the core subspace of the l-th
layer of the model from past tasks. While GPM prevents interference, its strict orthogonality limits plasticity by restricting
new task adaptation. Adam-NSCL [51] proposes an alternative
null space projection strategy grounded in singular value
decomposition (SVD). For layer l, it constructs the uncentered
1
l
l
l
(X̄t−1
)⊤ X̄t−1
from
feature covariance matrix X̄t−1
= ñt−1
l
previous tasks, where X̄t−1 concatenates input features of all
seen tasks. Through SVD decomposition as below,
l
U l , Λl , (U l )⊤ = SVD(X̄t−1
),

(17)

the method isolates the approximate null space via the singular
vector submatrix U2l corresponding to smallest singular values
(λ ≤ aλlmin ). The gradient projection is then formulated as,
∇Wl Lt = U2l (U2l )⊤ ∇Wl Lt .

(18)

This operation forces the gradient update into the null space of
l
l
l
= 0 and
X̄t−1
, ensuring parameter updates satisfy X̄t−1
∆wt,s
thus strictly avoid interference with previous feature representations. Compared to GPM’s explicit orthogonality constraint,
Adam-NSCL’s covariance null space projection provides a
more geometrically interpretable solution to forgetting prevention. However, both methods face plasticity limitations due to
the constrained update space.
To enhance plasticity, TRGP [52] introduces adaptive trust
regions. For the t-th task and past tasks j, when the gradient
similarity reaches a certain level, the gradient can be projected
onto the trust region to improve the learning capability for the
new task. The trust region is defined as follows:
(
T Rlt =

j<t:

∥ ProjS l (∇Wl Lt )∥2
j

∥∇Wl Lt ∥2

)
≥ϵ

l

.

(19)

Here, Sjl is the subspace for task j at layer l, and ϵl is a
similarity threshold. TRGP modulates updates using learnable
scaling matrices Qlj,t ,

C. Optimization-based methods



θt = arg min E(x,y)∼Dt L(fθ (x), y) .

A foundational approach is GPM [10], which projects
gradients of new tasks orthogonally to subspaces spanned by
past task features

s.t.⟨∇θ Lt , ∇θ Lt−1 ⟩ ≥ 0,
(15)

where Lt is the loss on the current task, and the constraint
enforces that the gradient update for the new task does not
increase the loss on previously seen tasks [82]. This formulation encapsulates the essential motivation behind optimizationbased continual learning: to find an update direction that is
beneficial, or at least non-destructive, to prior knowledge while
accommodating new information.

min

{Wl }l ,{Qlj,t }



l
L {Weff
}l , D t

l,j∈T Rlt

s.t.

l
Weff
= Wl +

X h

i
ProjS l ,Q (Wl ) − ProjS l (Wl ) ,
j

j

j∈T Rlt

(20)

where ProjSjl ,Q denotes scaled projection operator. By performing gradient protection within the trust region and simultaneously utilizing the scaled-projected weights for updates,
this method achieves a balance between the model’s stability
and plasticity. Recent work revisits the optimization landscape
itself. AdaBOP [53] derives a closed-form projection matrix,

−1
Plt−1 = I + λX̄lt−1 (X̄lt−1 )⊤
,

(21)

where X̄lt−1 contains past task features. By explicitly constraining plasticity and stability, this method obtains an explicit
form of the optimal solution; furthermore, it achieves favorable


performance by tuning the hyperparameter λ for each task and
each layer.
Discussion: Optimization-based methods are increasingly
adopted as plug-and-play modules to mitigate catastrophic
forgetting in continual learning systems. However, this trend
has overshadowed fundamental innovation in their core antiforgetting mechanisms—most current implementations rely on
conventional gradient constraints without revisiting the underlying optimization principles [54]. We urge renewed focus
on re-examining optimization-based approaches themselves,
developing novel theories that intrinsically encode forgetting
resistance rather than merely applying constraints. Concurrently, emerging memory-efficient implementations like Adaptive Plasticity Improvement (API) [56] demonstrate the value
of optimizing storage overhead, providing an inspiring direction for practical deployment where resource constraints
demand lightweight solutions.
D. Representation-based methods
Representation-based methods shift the focus of continual
learning from “how to preserve old knowledge” to “how
to learn more essential and universal knowledge”. The core
philosophy of this approach can be elucidated through a twophase process. The overall model, denoted as fθ in Section
2 in the main text, is decomposed into a feature encoder fenc
with parameters θenc and a classifier fcls with parameters θcls .
Phase 1 (Representation Learning).
min Lpretext (θenc ; Dpretrain ).
θenc

(22)

Phase 2 (Continual Learning).
min E(x,y)∼Dt [L(fcls (fenc (x; θenc ); θcls ), y)]

θcls ,[θenc ]

(23)
s.t.

fenc ∈ Fstable .

In the first phase, a powerful encoder fenc is trained on a
large-scale dataset Dpretrain via a pretext task, optimizing a
pretext loss Lpretext . This phase, which typically involves selfsupervised learning or large-scale supervised pre-training [59],
[60], aims to yield a high-quality, universal feature encoder
with parameters θenc . While the pre-training in Phase 1 is
foundational, most contemporary methods concentrate on the
strategies for Phase 2, where the model learns the current task
Tt by minimizing the loss L on Dt . To prevent catastrophic
forgetting, the optimization is constrained such that the encoder fenc remains within a stable function space, Fstable . This
special handling of the encoder’s parameters, denoted by θenc ,
leads to two primary strategies.
The most direct and robust strategy to enforce stability is to
keep the powerful encoder entirely frozen after Phase 1, i.e.,
θenc are fixed. In this case, learning is confined to lightweight
modules that operate on these fixed representations.
A leading frozen-encoder paradigm is prompt-based learning, where small, parameter-efficient “prompts” are learned to
instruct the model. The seminal work, Learning to Prompt
(L2P) [14], introduced a prompt pool and a key-value based
query mechanism to select a subset of prompts for each
input, effectively storing task-specific knowledge outside the
core model. This concept was advanced by DualPrompt [57]

decomposes prompts into “General” and “Expert” types to
better manage task-invariant and task-specific knowledge inspired by Complementary Learning Systems theory. More
recently, CodaPrompt [58] proposed an attention mechanism
over a set of prompt components, enabling the creation of
dynamically composed prompts and, critically, facilitating a
fully end-to-end optimization of the query-prompt system. An
alternative and highly effective approach that also employs
a frozen encoder is RanPAC [15]. This method introduces
a training-free adaptation mechanism by inserting a frozen,
non-linear Random Projection layer after the feature extractor.
This layer projects features into a higher-dimensional space to
improve their linear separability for a subsequent prototypebased classifier.
To allow for greater plasticity, a second strategy involves
cautiously fine-tuning the encoder parameters θenc while learning new tasks. This re-introduces the risk of forgetting, necessitating methods that carefully balance adaptation with the
preservation of the encoder’s powerful representations. For
instance, SLCA [61] fine-tunes the backbone with a very
low learning rate and uses a classifier alignment technique to
handle prediction biases. Other methods, like Co2L [62], pair
fine-tuning with a self-supervised contrastive distillation loss
to explicitly maintain representation stability. More recently,
RAPF [16] leverages the textual features from a visionlanguage model (CLIP) to adaptively adjust representations
for semantically similar classes, followed by a decomposed
parameter fusion strategy on a linear adapter to further mitigate
forgetting during the fine-tuning process.
Discussion: Representation-based methods, especially those
built upon the foundation of large-scale PTMs, currently
represent one of promising frontiers of rehearsal-free continual
learning. Their strength lies in leveraging flexible feature
representation modules to further guide or process pre-trained
features, thereby achieving better feature representations. This
highlights a key insight: for many continual learning problems,
the core challenge is not learning new features from scratch,
but rather learning to effectively access and combine the
rich features already present in PTMs. Therefore, the central
challenges lie in learning more potent feature representations
and developing more fine-grained mechanisms to identify
and preserve the features essential for preventing forgetting.
Furthermore, as the field increasingly moves towards multimodal foundation models, addressing the representation gaps
and discrepancies between different modalities, and how to
continually learn on them without catastrophic interference,
emerges as a vital new frontier.
E. Architecture-based methods
Architecture-based methods tackle catastrophic forgetting
by structurally isolating task-specific knowledge, thereby preventing destructive interference by design. These approaches
modify the model’s architecture, typically by composing a
stable, shared component with expandable, task-specific modules. When learning a new task Tt , the model’s parameters
are formed by combining a shared backbone θ with a set of
task-specific parameters {θ̂k }tk=1 . The optimization problem


for task Tt is formulated to update only the newly introduced
parameters θ̂t .
min E(x,y)∼Dt [L(f (x;θ ⊕ θ̂t ), y)] + λ · R(θ̂t )
θ̂t

(24)
s.t.

R(·) = ||θ̂t ||sparse .

Here, θ represents the parameters of the core model, which
are typically frozen to preserve generalized knowledge and
ensure stability. The term θ̂t denotes the set of parameters
exclusively allocated for learning task Tt , providing plasticity.
The composition operator ⊕ signifies how these parameter sets
are combined, such as through masking, additive decomposition, or modular routing. Finally, the regularization term R(·)
is often used to enforce constraints like sparsity on θ̂t , ensuring
the model’s growth is scalable and parameter-efficient.
Early implementations of this principle focused on parameter isolation within a fixed-capacity model [63] [64]
[65] [66] [67]. Methods like Hard Attention to the Task
(HAT) [64] and PackNet [65] define θ̂t as a binary mask
applied to θ, effectively creating dedicated sub-networks for
each task by freezing important weights from past tasks.
Other approaches dynamically expand the architecture. For
instance, Adaptive Plasticity Improvement (API) [56] evaluates
the model’s plasticity for a new task and adaptively expands
θ̂t by adding new neural units if the current plasticity is
deemed insufficient. These methods, while effective, were
often designed for models trained from scratch.
With the advent of large-scale pre-trained foundation models, θ is now commonly a powerful, frozen backbone like a
Vision Transformer (ViT). Consequently, θ̂t is realized through
various Parameter-Efficient Fine-Tuning (PEFT) techniques. A
prominent strategy is to use Low-Rank Adaptation (LoRA).
For example, Interference-Free LoRA (InfLoRA) [11] designs
the LoRA matrices (a form of θ̂t ) to lie in a subspace
that is orthogonal to the gradients of previous tasks, thereby
explicitly minimizing interference. Building on this, Scalable
Decoupled LoRA (SD-LoRA) [12] decouples the learning
of the magnitude and direction of LoRA components. By
fixing previously learned directions and only learning new
directions alongside all magnitudes, it traces a low-loss path
that converges to a shared solution space for all tasks,
uniquely enabling rehearsal-free and inference-efficient CL
without needing task-specific component selection. Another
sophisticated approach, Mixture-of-Experts Adapters for CL
(MoE-Adapter4CL) [13], implements θ̂t as a set of experts
managed by a task-specific router. This method enhances
scalability and leverages a Distribution Discriminative AutoSelector (DDAS) to automate task identification, preserving
the zero-shot capabilities of the underlying vision-language
model for out-of-distribution inputs.
Discussion: Architecture-based methods, especially those
integrated with PEFT on foundation models, currently represent a highly promising frontier in continual learning. Their
core strength lies in providing a structural solution to the
stability-plasticity dilemma by freezing the general knowledge
base (θ) while allowing targeted, efficient updates via θ̂t .
However, a critical challenge emerges from their reliance on
task identity. While highly effective in TIL where the task

ID is provided, many methods struggle in the more realistic
CIL setting. Without an explicit task oracle, dynamically
selecting or activating the correct task-specific parameters (θ̂t )
for a given input becomes a non-trivial problem, potentially
leading to significant performance degradation. Moreover, as
the number of tasks grows, naively accumulating task-specific
parameters can lead to a linear or super-linear growth in
model size, posing significant memory and computational
burdens. The future of this domain lies in developing more
sophisticated strategies for managing θ̂t . Instead of simple
expansion, the focus is shifting towards intelligent parameter
reuse, composition, and merging.
## Appendix B
L IB C ONTINUAL F RAMEWORK
This appendix details the software architecture and design
principles of the LibContinual framework. It elaborates on the
functionality of each core module—from configuration and
data handling to algorithm implementation and evaluation,
providing a technical blueprint for researchers interested in
utilizing or extending the toolbox for their own work.
LibContinual is a comprehensive framework for continual
learning, with its overall architecture illustrated in Figure 2
in the main text. To accommodate the integration of various
continual learning algorithms within a unified framework,
LibContinual is organized into multiple modules. This modular
design enables flexible composition and significantly simplifies
the development process, making it more manageable and
systematic.
A. Config
The configuration module of LibContinual is implemented
using the YAML file format to specify parameters related to
data, learning methods, and other experimental settings. A
wide range of experimental variables can be defined using
key-value pairs, including the continual learning algorithm
to be employed, the architecture of the backbone network,
dataset paths, among other critical information. To reduce
redundant specification of commonly used parameters such
as optimizers and backbone architectures, a set of default
configuration files is also provided. These default files are
first loaded and their contents used as baseline parameters.
Subsequently, the custom configuration file is read, and its
values are used to update the defaults. The final configuration
for the experiment is thus generated through the merging of
both default and customized settings.
B. Continual Learner
The Continual Learner module serves as the core component of LibContinual, responsible for orchestrating the entire
continual learning process. Logically, the training procedure
can be divided into several key stages along a temporal axis.
Initialization Stage. This stage handles the setup of all
essential components, including logger initialization, configuration file parsing, data loader preparation, algorithm and
optimizer instantiation, backbone network construction, and
GPU allocation.


Training Stage. This stage can be further subdivided into
pre-task processing, task-specific training, and post-training
processing, each allowing for the injection of algorithmspecific logic as needed.
Evaluation Stage. This stage assesses the model’s overall
performance on the test set.
Saving Stage. After the entire training process is completed,
this stage is responsible for saving relevant artifacts, such as
configuration files, checkpoints, and training logs.
This logical decomposition enables the flexible insertion of
different algorithms into appropriate stages of the pipeline.
From a temporal perspective, each task in a continual learning
scenario corresponds to a full cycle from pre-task processing
to evaluation. The entire experiment proceeds by repeating
this cycle for each task following the initial setup. After
initialization, the Trainer module executes the training loop
to iteratively carry out this process.
C. Datasets
Compared to traditional deep learning, where all data are
encapsulated in a single data loader, LibContinual introduces
a specialized data loader tailored to the unique multi-task
setting of continual learning. This data loader is designed
to accommodate various requirements specific to continual
learning, such as task-wise dataset partitioning and merging.
Specifically, LibContinual assumes that all datasets follow a
unified directory structure, consisting of two folders named
“train” and “test”, which contain all training and testing
images, respectively. Within each of these folders, images
belonging to different classes are stored in separate subdirectories. To facilitate rapid and convenient experimentation, LibContinual provides pre-processed dataset archives for several
commonly used benchmarks, including CIFAR-10, CIFAR100, CUB200, ImageNet-R, and Tiny-ImageNet. In the context
of continual learning, dataset partitioning is typically defined
by two parameters: init cls num and inc cls num, which
denote the number of classes in the initial task and in each
subsequent incremental task, respectively. In LibContinual, an
entire dataset is encapsulated using a ContinualDatasets object.
During the initialization phase, this object generates a class
order based on the configuration file, and then partitions the
dataset into multiple sub-datasets according to the specified
init cls num and inc cls num. Furthermore, since evaluation
in continual learning often requires testing across multiple
task-specific test sets, LibContinual also supports generalpurpose operations such as merging and splitting datasets.
D. Backbone
Backbone networks play a pivotal role in the field of deep
learning, and in some cases, the introduction of a new network
architecture can significantly advance an entire research area.
In LibContinual, a variety of widely adopted backbone models
in continual learning are integrated into the Backbone module,
including the classical ResNet family, Vision Transformers,
and CLIP networks. Moreover, since certain methods may
require modifications to the backbone, switching the network
structure can be easily achieved by making simple adjustments

in the configuration file of LibContinual. A complete model
typically consists of two components, a backbone network
and a classifier. In most continual learning approaches, the
classifier is implemented as a simple linear layer. LibContinual
encapsulates these classifiers and provides a set of generalpurpose functional interfaces and parameters, thereby reducing
redundancy during the development process.
E. CL Algorithm
For the implementation of specific method modules, several
core functionalities are required. Before the training of the
current task begins, the before task function is invoked to
perform preliminary operations such as variable initialization,
model structure adjustments, and training parameter configuration. During the training phase, the observe function is
called with a batch of training samples as input. This function returns the predicted results, classification accuracy, and
forward loss. It focuses on how the model processes a batch
of data during training, specifically, how the loss is computed
and how parameters are updated. In the inference phase, the
inference function is invoked with a batch of test samples
and returns classification results along with accuracy. This
function is concerned with how the model performs forward
inference during evaluation. After the training of each task
is completed, the after task function is executed to handle
post-task adjustments, such as modifications to the model
architecture or memory buffer. This step typically requires
user-defined logic tailored to the specific method.
F. Metric
The module implements commonly used performance metrics in continual learning, such as average task accuracy,
backward transfer, forgetting measure, and overall average accuracy. These metrics are used to comprehensively evaluate the
model’s performance across different tasks, the effectiveness
of knowledge transfer, and the extent of forgetting.
## Appendix C
M EMORY C ALCULATION
This appendix outlines the specific protocol used to implement the Unified Memory Budget, a central component of our
investigation into algorithmic efficiency as introduced in Section V-C of the main paper. It details the precise methodology
for quantifying the additional memory costs associated with
diverse continual learning strategies, thereby establishing the
standardized and equitable basis for comparison used in our
storage-centric analysis.
To ensure a fair and standardized comparison across continual learning strategies that rely on qualitatively different
forms of stored knowledge, we established a unified memory
accounting protocol. In our framework, the total memory
footprint of a method is calculated as the sum of the static
memory required by the network backbone and any additional
memory consumed by the specific continual learning algorithm
for storing extra information. For the purpose of creating a
single, standardized metric, we quantify the entire memory


TABLE V
M EMORY U SAGE C ALCULATION E XAMPLES OF C ONTINUAL L EARNING M ETHODS .
Method

Memory Classification

iCaRL

Image-based,
Model-based

Image
32x32x3x1

Feature
-

Model

Parameter

Prompt

Total Memory

472,756 x 4

472,756 x 4

-

9,926,048
(9.93 M)

(482 + 5762 + 5122

Frozen Params
-

GPM

Feature-based

-

+10242 + 20482 )
×4

-

6,704,128 x 4

-

50,172,928
(50.17 M)

-

L2P

Prompt-based

-

-

-

-

46,080 x 4

491,920
(0.49 M)

491,920

MoE-Adapter4CL

Parameter-based

-

-

-

4,104,292 x 4

-

16,417,168
(16.42 M)

16,417,168

footprint in terms of integer (int) units. The additional
storage, which is the dynamic component that varies between
methods, is also meticulously quantified using the same base
unit. This extra storage encompasses all forms of preserved
knowledge as categorized in our storage-centric taxonomy,
including the raw pixel values of buffered exemplars (imagebased), the elements of stored feature vectors (feature-based),
the parameters of saved model snapshots (model-based), the
weights of dynamically added network modules (parameterbased), and the tokens of learnable prompts (prompt-based).
By converting all these disparate data types into a common
integer-based unit of account, this protocol enables an equitable and direct comparison of the true resource efficiency of
each method, moving beyond simple performance metrics to
reveal the underlying cost-benefit trade-offs.
As shown in Table V, our protocol is best illustrated
through a concrete application. For instance, calculating the
memory footprint of a hybrid method like iCaRL involves
quantifying and summing each of its storage components. The
primary memory cost is from its image-based exemplar buffer
(2000 images), with additional allocations for its model-based
component (a stored model for knowledge distillation) and the
trainable parameters of the active backbone. By converting
the storage for each component into our unified integer-based
metric, we arrive at its total memory budget of approximately
9.93 M units. This systematic, component-wise summation is
applied uniformly across all evaluated methods to ensure a fair
and direct comparison of their memory overhead.
