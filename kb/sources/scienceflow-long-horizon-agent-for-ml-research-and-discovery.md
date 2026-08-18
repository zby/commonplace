---
source: https://arxiv.org/abs/2608.14354v1
description: "ScienceFlow couples recoverable executable workspaces, evidence-gated checkpoints, trajectory re-anchoring, and resource control for long-horizon autonomous research"
captured: 2026-08-18
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# ScienceFlow: A Long-horizon Agent for ML Research, Scientific Discovery and Beyond

Author: Mingming Zhao, Jiqian Dong, Kangping Xu, Zadid Hasan, Chengrui Fan, Shan Jiang, Shuai Mao, Ting Lingya, Linyi Zou, Tailin Zhou, Yun Hin Chan, Wenkai Zhang, Zhanhong Zhou, Guowei Huang, Hongliang Li, Wenjing Cun, Zhitang Chen, Mingxuan Yuan, Yanhui Geng
Affiliation: Noah's Ark Lab, Huawei
Source: https://arxiv.org/abs/2608.14354v1
Date: August 14, 2026 (arXiv:2608.14354v1)
Capture note: Text extracted from the versioned arXiv PDF; page breaks, repeated page headers, standalone page numbers, and the table of contents were removed. Figure text and tables retain the PDF extractor's reading order.

## Abstract

Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended
horizons is a central challenge for autonomous machine learning and scientific discovery, as
progress hinges on continuously managing evolving state, exploration decisions, and computational resources. Pioneering autoresearch agents, despite great success, still lack mechanisms
for continuity, recovery from dead ends, and value-driven compute allocation, which inherently
undermines overall search efficiency, wastes computational resources, and lowers the chance of
ultimate success. To bridge this gap, we introduce ScienceFlow, an end-to-end autoresearch
agent framework that organizes long-horizon research work into research segments grounded in
executable workspaces. It represents research progress as recoverable executable states, enabling
efficient exploration, revision, and execution. Transitions between research segments are governed by Executable-State Transition through Re-Anchoring (ESTRA), which selects either the
live state or an archived state as the next anchor and determines whether to continue or redirect the
research trajectory. An evidence-aware execution controller allocates resources to physical jobs
based on resource availability, remaining budget, and validated progress. We evaluate ScienceFlow on tasks spanning machine learning, scientific modeling, and mathematical optimization.
Results on diverse long-horizon benchmarks demonstrate its ability to sustain effective research
processes, highlighted by a SOTA 70.22% Any-Medal score on the full MLE-bench within a
24-hour budget, and outperforming prior reported results by 4.92 percentage points. The efficacy
of ScienceFlow further demonstrates that efficient state management, adaptive exploration, and
objective-aligned execution are critical for scaling autonomous research beyond short-horizon
interactions.
- GitHub: https://huawei-noah.github.io/noah-research/ScienceFlow/website/

Figure 1: Performance overview. (a) End-to-end performance on the full MLE-bench, where
ScienceFlow achieves 70.22 ± 1.18% Any-Medal. (b) Capability analysis across Search, Storage,
Compute, Model Adaptation, and Time dimensions under full and constrained-reference settings.
Each dimension is evaluated independently.

## 1 Introduction

AI autoresearch agents are rapidly evolving beyond isolated reasoning and tool use toward increasingly complete, long-horizon research workflows. Recent systems can formulate hypotheses, modify
executable artifacts, run experiments, interpret intermediate evidence, and revise subsequent decisions across machine learning and scientific discovery (Lu et al., 2024b; Yamada et al., 2025; Tie
et al., 2026; Wei et al., 2025). AlphaEvolve (Novikov et al., 2025), for example, demonstrates that
iterative code modification guided by evaluator feedback can produce meaningful improvements in
algorithms and scientific constructions. As research agents scale to longer, highly automated workflows, the bottleneck shifts from executing discrete research steps to sustaining productive, stable,
and goal-aligned progress over time. This demands that agents preserve state across iterations, synthesize intermediate evidence, navigate competing directions, recover from dead ends, and translate
available time and compute into tangible improvements.
Achieving sustained progress is complicated by the expanding nature of the research state itself. Over
time, the agent’s context grows beyond a simple interaction log into a rich executable workspace
containing source code, datasets, cached artifacts, model checkpoints, solver states, evaluation
outputs, and other artifacts. While textual summaries can compress past interactions, they cannot
faithfully reconstruct the executable state required to reliably resume, reuse, or revisit earlier work—a
limitation that has motivated structured memory and persistent workspace designs (Zhu et al., 2026;
Chen et al., 2026a; Qian et al., 2026). Moreover, promising directions often consume significant time
and compute before revealing their flaws; apparent progress may be an artifact of noisy evaluation
signals, implementation choices, or strategies that have already exhausted their local potential (Toledo
et al., 2025). Decisions to continue, branch, or revert to an earlier state thus directly govern where
additional resources are deployed. Consequently, effective long-horizon research demands that state
persistence, exploration choices, and execution control evolve together as evidence accumulates.
Recent systems have tackled isolated facets of this problem through disparate representations of the
research process. Structured and persistent memories preserve project knowledge and intermediate
artifacts across iterations (Qian et al., 2026; Chen et al., 2026a), while trajectory-centric methods
support branching, recovery, or iterative refinement of research paths (Chen et al., 2026c; Zhang et al.,
2026b). Resource-aware systems operate at yet another layer, using runtime signals to place, monitor,
and reschedule heterogeneous workloads (Wang et al., 2026; Lu & Reda, 2026). While individually
useful, these representations leave research state, trajectory decisions, and physical execution only
loosely connected. Recovery, exploration, evaluation, and resource allocation each often operate over
different views of the research process, making it difficult to maintain a consistent notion of progress
as research evolves. This fragmentation remains a fundamental obstacle to sustaining coherent,
adaptive, and efficient research over long horizons.
To this end, we introduce ScienceFlow, a workspace-grounded autonomous research system that
supports one or more homogeneous research workers. ScienceFlow organizes research around
recoverable executable workspaces, which preserve the concrete state of each research trajectory
and serve as stable boundaries for continuation, branching, and recovery. During forward research,
task-specific result signals produce validated workspace checkpoints, while text-only responses or
context-capacity limits define research-segment boundaries that invoke ESTRA. At each researchsegment boundary, a research worker uses ESTRA to continue or redirect from the live workspace,
or to restore an archived checkpoint and proceed from that state. Multiple homogeneous workers
can operate on independent trajectories in parallel, exchanging only compact progress summaries
at research-segment boundaries to limit interference while sharing useful evidence. Beneath this
research layer, an evidence-aware execution controller manages the physical jobs associated with
each trajectory, using both resource conditions and validated progress to admit, monitor, pause, or
terminate execution. Scientific decisions remain with the research workers, while the controller
provides resource-aware execution and system-level safeguards.
The broader question is whether a common set of long-horizon research abstractions can transfer
across substantially different executable tasks. We evaluate this question across machine learning, scientific modeling, and mathematical optimization. ScienceFlow achieves strong performance across
all three domains, including a 70.22 ± 1.18% Any-Medal rate on the full 75-task MLE-bench (Chan
et al., 2025) under a 24-hour budget, 4.92 percentage points above the strongest reported baseline,
while also attaining the best group-balanced score on SciModelingBench (SciModelingBench, 2026)


and reaching/improving published frontiers on multiple mathematical optimization problems. Our
contributions are summarized as follows:
• We identify that effective long-horizon research depends not simply on extending interaction time
or compute, but on jointly maintaining executable state, adapting research trajectories, and aligning
execution with validated progress.
• ScienceFlow realizes this principle through recoverable executable workspaces, ESTRA-governed
transitions between research segments, and evidence-aware execution control, enabling research
to continue, redirect, or recover without losing useful progress.
• ScienceFlow demonstrates strong and consistent performance across a diverse range of tasks, including machine learning, scientific modeling, and mathematical optimization, with substantial
gains on MLE-bench and SciModelingBench and state-of-the-art results across multiple optimization problems.


## 2 Method


### 2.1 Preliminaries

We formalize executable research tasks whose outcome quality can be quantified by a goal-dependent
utility. A task is defined as T = (G, UG , VG , B, W0 ), where G specifies the research goal and success
criteria, UG (·) denotes the final task utility, VG (·) is the validation signal observable during research,
B specifies the available resource budget, and W0 is the initial executable workspace. Starting from
W0 , the agent explores a growing collection of recoverable executable states. Let AT denote the
archive of checkpointed executable states created over a research horizon T . Each executable state
sv ∈ AT represents a concrete checkpoint of the evolving research process, including the executable
workspace and its associated artifacts, memory, validation evidence, and resource records. The state
archive therefore provides a set of recoverable states from which the agent can continue, revisit, or
redirect its research trajectory. Since UG is often unavailable during execution, the agent uses VG to
guide search and seeks the best validated state within the available budget:
ŝT = arg max VG (sv )

s.t.

sv ∈AT

CT =

T
X

ρt ⪯ B,

(1)

t=1

where ρt denotes the resource-consumption vector at step t, and CT is the cumulative resource
expenditure. The budget vector B = (B1 , . . . , BK ) specifies K component-wise limits, such as
Pt
wall-clock time, compute, and storage. For any t ≤ T , let Ct =
τ =1 ρτ and Bt = B − Ct
denote the cumulative expenditure and remaining resource budget, respectively. The selected state
is ultimately assessed by UG .

### 2.2 System Overview

Long-Horizon Research Process. ScienceFlow extends conventional tool-using inference loops
to long-horizon executable research by organizing the process around recoverable executable states.
Each state binds an executable workspace with compact memory, validation evidence, and resource
records. These states persist across research iterations, providing a common foundation for resuming
execution, adapting trajectories, and coordinating physical resources as new evidence accumulates.
During the long-horizon search, ScienceFlow uses a stage gate to determine when to checkpoint
each research state, including all artifacts of the current workspace and execution results—into
the state archive. This stage gate is triggered automatically by a task-specific result signal. In
addition, Executable-State Transition through Re-Anchoring (ESTRA) governs transitions between
research segments by selecting the next anchor state and an extend-or-redirect direction. More
concretely, ESTRA is triggered by either a text-only response from the worker or an approaching
context-capacity limit. At each trigger, the research worker uses ESTRA to select an execution
anchor and an extend-or-redirect direction based on the available states, accumulated validation
evidence, and remaining resource budget. If an archived anchor is selected, ScienceFlow restores the
corresponding state before the next research segment begins. Together, these mechanisms connect
recoverable executable states, adaptive trajectory transitions, and physical execution within a single
long-horizon research process. Figure 2 provides an overview of the ScienceFlow architecture and
its long-horizon research process.


Autonomous Research

Evidence-Aware Execution
Control

Executable-State Transition through Re-Anchoring (ESTRA)
Favorable

Re-Anchoring

Continue this route
or re-anchor?

0.71

0.85

0.75

S0

S1

S2

S3

Online review

22m

Useful evidence ETA 8m

Decision：Continue

continue
0.63

Remaining budget

Admission & lease

Unfavorable
Non-convergence,
low GPU utilization
Model Limitation,
I/O Bottleneck

0.93

Workspace State

Code

S3‘

High-value
result

Memory

Evidence

Compute Jobs
jobs

Decision：Stop

…
…

time

Stage Gate

CH ANGE Code · Conf ig · Ru n
RE SULT Artifa ct · Metric · Validity

Evidence

VALUE

Artifacts

Fin ding · R oute Lesson

Restored S2 → optimize S3′

Evaluator Summary

GPU/CPU

Storage

Wall time

Figuregating
2: ScienceFlow
system architecture. Research workers operate over recoverable executable
System-side
(agent-unaware)
states and adapt long-horizon trajectories through ESTRA-governed transitions between research
segments, while an evidence-aware execution controller coordinates physical resource allocation and
runtime execution.

Artifacts：数据文件，模型权重，特征分析等

System and Worker Model. ScienceFlow supports one or more homogeneous research workers,
each operating within an isolated executable workspace and maintaining its own state archive.
Multiple workers explore independent research trajectories and exchange only compact validated
progress at research-segment boundaries. They share a physical resource pool governed by a
common execution controller, which manages resource availability and runtime execution without
participating in scientific route selection.

### 2.3 Executable Research Process

Long-horizon research is organized as a sequence of research segments. Within each segment,
the worker follows its local tool-use policy to inspect, modify, and execute the active workspace.
Whenever ScienceFlow detects a task-specific result signal, the stage gate evaluates the result, records
the resulting evidence, collects a compact progress summary, and checkpoints the corresponding
executable state in the archive. Multiple such checkpoint events may occur within one segment. A
text-only response or an approaching context-capacity limit closes the current segment and invokes
ESTRA to initialize the next segment from a selected research state and direction. Each design is
described in detail in the following subsections.

#### 2.3.1 Research State Representation

We begin by defining the research state sv , which captures a specific milestone in a long-running
research process. Each state is indexed by a unique archive identifier v, which denotes its corresponding entry in the archive A and makes the state retrievable. In ScienceFlow, sv maintains four
distinct types of information:
• Workspace snapshot Wv : contains all executable artifacts available at the time of
archival—including source code, data-processing scripts, model checkpoints, cached features,
validation outputs, submissions, environment metadata, and references to large artifacts.
• Structured research memory mv : maintains a compact long-horizon agent memory that persists
across all research segments, which is detailed in section 2.3.4.
• Validation evidence ev : stores the validation results associated with the current research state,
defined as ev = VG (sv ).
• Resource records ℓv : resource records captured from the current resource ledger at the time of
checkpointing.


To make this research state sv actionable, it is represented as a tuple of these four components:
sv = (Wv , mv , ev , ℓv ) ,

(2)

which can be inserted into or retrieved from the archive A as needed.

#### 2.3.2 Forward Research

Each research segment executes a forward research process that may produce multiple checkpointed
research states. During this process, the worker follows a local reasoning–action–observation policy
to interact with the active workspace. For a given segment n, we define:
• Pn : the fixed segment-level base context, recovered from the cross-segment structured memory
mv from the last research segment.
• Wn,j : the active workspace at round j, where Wn,0 is cloned from the workspace snapshot Wv of
the previous research segment.
• hn,j : the segment-local interaction history (agent context) accumulated up to round j. It captures
the reasoning content, tool actions, and observations across rounds and is initialized as hn,0 = ∅.
At each round j the policy generates a reasoning output rn,j and tool action αn,j :
(rn,j , αn,j ) ∼ πLLM (· | Pn , hn,j ) .

(3)

If αn,j ̸= ∅, ScienceFlow executes the action, producing an observation on,j and an updated
workspace:
(on,j , Wn,j+1 ) = Exec (αn,j ; Wn,j ) .

(4)

If αn,j = ∅, the step is text-only; the workspace remains unchanged, (Wn,j+1 = Wn,j ) and no
observation is produced (on,j = ∅). After each round, the local history is updated by appending the
reasoning, action, and observation:
hn,j+1 = hn,j ⊕ (rn,j , αn,j , on,j ) ,

(5)

where ⊕ denotes ordered concatenation.
Independently of the local interaction policy, ScienceFlow monitors the updated workspace for a
task-specific result signal specified by the task adapter. Upon detection, the stage gate collects
the result, invokes the evaluator to obtain validation evidence, and requests a compact progress
summary from the worker. It then snapshots the workspace as Wv = Snapshot(Wn,j+1 ), records
the associated memory mv , validation evidence ev , and resource records ℓv , and inserts the resulting
state sv = (Wv , mv , ev , ℓv ) into the archive An . Temporary stage-gate exchanges are excluded from
the segment-local history hn,j+1 , and the worker resumes forward research within the same segment.
Separately, the current research segment closes and transfers control to ESTRA when either of the
following conditions for a research-segment boundary is met:
1. The policy produces a text-only response αn,j = ∅; or
2. The accumulated context exceeds the configured capacity threshold |Pn ⊕ hn,j+1 | ≥ Lctx
If neither condition holds, the forward loop proceeds to round j + 1. Otherwise, the live workspace
at the trigger defines the current state scur
n , and ScienceFlow initiates the route-level deliberation
described next. When a result signal and the context-capacity condition coincide, ScienceFlow
completes stage-gate processing first, making the newly checkpointed state available to the subsequent
ESTRA decision.

#### 2.3.3 Re-Anchoring and Exact Restoration

At each research-segment boundary, ScienceFlow invokes ESTRA for route-level deliberation by
the research worker. The worker policy πLLM produces an anchor-and-direction decision (an , dn ).
This decision operates on two independent axes: an selects the execution anchor, either the current
trigger state scur
n or a previously archived state sv ∈ An , while dn determines whether to extend the
current trajectory or redirect onto a new branch from that anchor. The worker bases this decision
on the compact memory view, available anchor candidates with their validation evidence, and the


current resource envelope. Formally:
an ∈ {scur
n } ∪ An ,

dn ∈ {extend, redirect}.

(6)

Combining these two choices yields four possible outcomes: extending or redirecting from the
current state, and extending or redirecting from an archived state. After the ESTRA decision, the
next research segment n + 1 is initialized by defining the segment-level base context Pn+1 and
workspace Wn+1,0 as:
(Pn+1 , Wn+1,0 ) = ESTRA (an , dn ; An ) .

(7)

If an selects the current executable state, ESTRA retains the current workspace Wn,j+1 as Wn+1,0 .
If an selects an archived executable state sv ∈ An , ESTRA restores the full state, i.e., workspace Wv ,
memory mv , validation evidence ev , and resource records ℓv , with resource accounting remaining
cumulative across restoration, including resources consumed after archiving. The anchor thus determines the workspace from which research resumes, while dn determines whether research extends
the anchor’s existing route or redirects from it. The resulting Pn+1 carries the anchor’s research
summary, relevant evidence, and selected direction, while Wn+1,0 provides the corresponding executable artifacts. ESTRA preserves the full archive while cleanly setting both the starting state and
research direction for the next segment.

#### 2.3.4 Memory and Context Assembly

ScienceFlow maintains a persistent memory mv that carries the entire research trajectory across
segments. This memory is updated through two core operations: Add appends new progress
summaries, and Fold compresses the memory when it grows too large. To support anchor selection
during ESTRA, Fold retrieves historical records, and Assemble constructs the prompt that guides
the agent’s decision. Together, these operations ensure that the agent always has a compact yet
complete view of its research history.
Add: accumulating progress. At each stage-gate event, the worker summarizes the evaluated
result, relevant artifacts, and current progress into a compact result card qv . This card is added to
the persistent memory via:
mv = Add(mv , qv ).

(8)

This update preserves the new progress information in mv without resetting the segment-local history.
ESTRA later uses the accumulated memory to assemble the context for the next research segment.
Fold: compressing memory. When persistent memory mv exceeds its allocated context space
Bmem , Fold automatically compresses it:
(m
e v , ιv ) = Fold(mv ; Bmem ).

(9)

where m
e v is a compact view that keeps recent, best-validated, and anchor-relevant records in full
while summarizing older ones, and ιv is an index that maps each folded summary to its original
records in the archive. The complete memory mv remains preserved in the archive.
ScienceFlow also applies Fold whenever an ESTRA transition closes a research segment, independently of Bmem . If the selected anchor is the current state (an = scur
n ), Fold summarizes the
research segment just ended. If the anchor is an archived state (an = sv ∈ An ) it summarizes the
exploration performed since last time that state was restored. This summary is carried forward as
historical evidence, while the raw result cards remain addressable via unfold.
Unfold: retrieving history for anchor selection. To select an anchor during ESTRA, the agent
must understand the full trajectory. Unfold retrieves complete records associated with a requested
identifier (zv a folded summary or an indexed result card):
uv = Unfold(mv , ιv , zv ).

(10)

The retrieved records uv temporarily augment the compact memory view for the current deliberation,
while mv remains the persistent source.


Assemble: constructing the anchor-selection context. With the memory view prepared, ScienceFlow constructs an anchor-specific context Panchor (an ) that presents the agent with the information needed to choose the next anchor and direction. For a selected anchor an , let W (an ), m(an ),
e(an ), and ℓ(an ) denote its retrieved state components, and let m(a
e n ) denote its budgeted memory
view (or m(an ) if folding is unnecessary). Let u(an ) denote any records retrieved via Unfold. The
Assemble operation combines these:
Panchor (an ) = Assemble(m(a
e n ) ⊕ u(an ), e(an ), ℓ(an ), View(W (an ))) .

(11)

Where View(W (an )) provides a compact description of the available workspace artifacts and
execution state. The full base context for the next segment is then:
Pn+1 = Pworker ⊕ Pruntime ⊕ Ptools ⊕ Ptask ⊕Panchor (an ) ⊕ Pdir (dn ) ,
|
{z
}

(12)

Pstable

where Pstable contains the worker policy, runtime instructions, tool descriptions, and task specification, and Pdir (dn ) encodes whether the next segment extends or redirects from the selected anchor.
The next segment begins with hn+1,0 = ∅ and accumulates new interactions through the forward
loop. In summary, Add and Fold maintain a complete yet compact persistent memory across the
research trajectory; Unfold retrieves historical records when the agent needs to re-anchor; and
Assemble constructs the context that guides anchor selection and initializes each new segment. This
design preserves the full research record while supplying each segment with a context-bounded,
anchor-specific memory view.

### 2.4 Evidence-Aware Execution Control

A key distinction that separates ScienceFlow from existing autonomous research agents is the explicit
separation of research-route selection from physical execution control. In this design, the research
worker proposes executable jobs, while a dedicated evidence-aware execution controller determines
whether, where, and for how long each job runs. This controller evaluates both pending and
running jobs using current resource availability, remaining budget, validated research progress, and
the recoverable state of execution artifacts. Accordingly, the control process operates in two stages:
admission and allocation before a job is launched, and online review and replanning during execution.

Execution Admission and Allocation

For each proposed executable job b, ScienceFlow constructs a resource request describing its command, requested device class and count, estimated runtime, memory requirements, and any researchvalue hints supplied by the research worker. ScienceFlow complements these hints with estimates
inferred from the command and execution context to establish the job’s admission priority. This priority reflects expected research value, lineage diversity, proximity to a deliverable, worker starvation,
duplication, and runtime risk.
The admission-and-lease module then evaluates the request against the live resource state Rt , which
includes available GPU/CPU capacity, storage constraints, queue state, GPU pressure, and active
leases, while also accounting for the remaining budget Bt . If the preflight check yields a confident
result, it is applied directly; otherwise, the request is passed to an isolated admission LLM for review.
This LLM combines the resource request, research-value information, and preflight result to produce
the admission decision:
δbadm = Admit(b; Rt , Bt ) ∈ {RUN NOW, OBSERVE THEN RUN, PENDING, REPLAN}.

(13)

Each decision corresponds to a specific action:
• Run now: the job is launched immediately after ScienceFlow atomically acquires the required
device lease.
• Observe then run: the job is launched with a short early-review window when its resource
behavior remains uncertain.
• Pending: the job is retained in the priority-aware queue without a device lease.
• Replan: the blocking evidence is returned to the research worker for plan revision.


Device leases coordinate exclusive or controlled shared access to compute resources and are released
when the corresponding job finishes, is stopped, or no longer requires the assigned device.

Online Review and Replan

Admission establishes the initial execution state of a compute job, after which ScienceFlow reviews its
progress at successive observation boundaries. At each boundary, the controller collects timestamped
evidence from process liveness, logs, metric history, artifact updates, resource utilization, checkpoint
availability, and the remaining budget. The controller treats process liveness, log growth, and
sustained resource utilization as evidence that a job remains active. Metric improvement, validated
results, or newly recoverable artifacts provide stronger evidence that the job is making meaningful
research progress.
From the accumulated evidence, ScienceFlow estimates the time until the job produces its next useful
evidence, such as a comparable metric update or a recoverable artifact. When this useful-evidence
ETA falls within the remaining budget and is supported by recent progress, the controller favors
continued execution. Persistent non-convergence, low GPU utilization, model limitations, or I/O
bottlenecks indicate that a job may fail to produce useful evidence within the remaining budget. When
these signals persist across multiple observation windows and the job has produced no recoverable
value, they provide strong evidence for stop-and-replan.
When execution evidence alone leaves the job’s prospective research value uncertain, ScienceFlow
requests a resource advisory from the research worker. The worker reports its preferred action—
continue, timebox continue, safe to stop, replan, or unknown—together with its confidence, a
measurable commitment, and the expected next artifact. The controller incorporates this advisory as
research-value evidence while retaining authority over lease allocation, execution timeboxing, and
process termination. The controller then combines the accumulated execution evidence y0:t , the
optional worker advisory gt , and the remaining budget Bt to produce a control decision:
ct = Review(y0:t , gt ; Bt ) ∈ {CONTINUE, TIMEBOX, STOP AND REPLAN}.

(14)

Each decision corresponds to a specific action:
• continue : keeps the current job running.
• timebox: grants a bounded proof window tied to a measurable progress condition.
• stop and replan: terminates the current job and redirects control to the research worker.
Notably, recent validated progress, a new checkpoint, or a feasible phase-completion ETA favors
continued execution even when the job progresses slowly. Before applying stop and replan,
ScienceFlow preserves recoverable artifacts, releases the assigned leases, and returns the observed
execution facts to the research worker.
Here, REPLAN and STOP AND REPLAN denote execution-control handoffs: the controller returns
blocking or runtime evidence to the research worker, which determines the revised scientific plan.
These outcomes do not themselves select the ESTRA anchor an or direction dn .
Together, admission and online review form a closed execution-control loop: ScienceFlow applies
Admit before launch and repeatedly applies Review at subsequent observation boundaries until the
job completes or control returns to the research worker for replanning. This loop allocates compute
according to research value while coordinating GPU/CPU capacity, storage usage, and wall-clock
time throughout execution.


## 3 Experiment

We evaluate ScienceFlow across three classes of executable research tasks: machine learning engineering, mathematical optimization, and scientific modeling, covering substantially different forms of
long-horizon research. All runs are conducted in isolated environments without cross-run state sharing, and held-out evaluation information is never exposed to the research agent. Task-specific models,
resource budgets, evaluation protocols, tools, and baselines are described in the corresponding subsections. Beyond overall task performance, we examine the research dynamics of ScienceFlow,
including state evolution, trajectory adaptation, and resource utilization over the course of extended
execution.



### 3.1 Machine Learning Engineering
#### Setup

Benchmark and Metric We evaluate ScienceFlow on the full MLE-bench (Chan et al., 2025),
which contains 75 real-world Kaggle competitions spanning tabular, vision, language, audio, and
time-series tasks. Each task requires the agent to construct an executable machine-learning pipeline
and produce a valid submission evaluated on a held-out test set constructed from the original
competition data. Unlike evaluations restricted to the 22-task Lite split, we report results on the
official Lite, Medium, and High tiers and on the aggregate 75-task benchmark. The primary metric
is Any-Medal rate: a task run succeeds when its submission reaches the Bronze, Silver, or Gold
threshold derived from the original Kaggle leaderboard. ScienceFlow results are reported as mean
± SEM over three independent runs, while baseline statistics are retained in the form reported by
their original sources.
Model and Resource Budget For the primary MLE-bench evaluation, ScienceFlow uses
DeepSeek-V4-Flash-Preview, with a 24-hour budget and at most 2 GPUs, 16–32 logical CPU cores,
and 256 GB RAM per run. Because hardware and concurrency vary across systems, comparisons
use wall-clock time rather than normalized accelerator-hours. Budget deviations are documented in
Table A3 in Appendix B.1.
Tools and Baselines ScienceFlow operates in a sandboxed Python environment, with network
access limited to third-party packages and publicly available model checkpoints. Held-out test labels
and test-derived feedback are never exposed to the agent; the test set is used only by the final scorer.
Baselines are drawn from the official MLE-bench leaderboard (OpenAI, 2026b) and publicly reported
studies.

#### Main Results

Table 1 summarizes the main results on MLE-bench. Across the full 75-task benchmark, ScienceFlow
achieves an Any-Medal rate of 70.22 ± 1.18%, exceeding the strongest reported baseline by 4.92
pp. The three independent runs obtain medals on 54, 53, and 51 tasks, respectively, demonstrating
consistent performance across runs. The improvement is particularly strong on the Medium tier,
where ScienceFlow reaches 74.56 ± 0.88%, 10.52 pp above the best reported baseline. It also
achieves 80.30 ± 1.52% on Lite, matching the best reported result, and 44.44 ± 2.22% on High,
within 2.26 pp of the best reported baseline. Overall, ScienceFlow performs consistently across task
complexities, with its largest advantage concentrated on the Medium tier. The complete leaderboard
and protocol annotations are provided in Table A3 in Appendix B.1.

#### Case Study and Ablations

Long-horizon case study We use the Statoil Iceberg Classifier Challenge, a satellite-SAR binary
classification task, as a representative long-horizon case study. The task requires distinguishing
icebergs from ships from satellite SAR imagery under the same 24-hour budget used throughout
MLE-bench. ScienceFlow earns a medal in all three independent runs. Figure 3 traces one run
and illustrates how recoverable workspace states, ESTRA transitions, and evidence-aware execution
control interact over the course of research.
The trajectory exhibits both state restoration and selective artifact reuse. After subsequent CNN-only
exploration fails to improve the incumbent, ScienceFlow restores S59 as an execution anchor and
redirects the search toward tree models over saved CNN features. A later unproductive stacking
branch similarly returns to S112 before exploring a new route. Within these branches, the agent
selectively reuses earlier workspace artifacts: S59 combines fold checkpoints from S02 and S53,
S112 trains a LightGBM model on CNN logits and angle features derived from S53, and S123
combines the wide-64 and wide-96 assets from S53/S55. These operations reduce recomputation
while improving validation loss from 0.1100 at S02 to 0.0597 at S123.
Validation evidence continuously guides these trajectory decisions. The best validated loss decreases
from 0.11 to 0.1025 and finally 0.0597, while exploratory trials that fail to improve the incumbent
remain preserved in the archive for later comparison or reuse. Retrospective test scores shown in


Table 1: Representative results on the full 75-task MLE-bench. Any-Medal rates (%) are reported
as mean ± SEM when three runs are available. Best results in each column are shown in bold.
Agent

LLM(s)

Lite (%)

Medium (%)

High (%)

All (%)

40.00 ± 0.00
44.44 ± 2.22
46.67 ± 0.00
42.22 ± 2.22
44.40 ± 2.20

59.56 ± 0.89
62.67 ± 0.77
63.11 ± 0.44
64.44 ± 1.18
64.90 ± 0.40

42.22 ± 2.22
42.22 ± 2.22
40.00 ± 0.00
46.70 ± 0.00

56.44 ± 2.47
61.33 ± 1.33
61.33 ± 0.77
65.30 ± 0.80

Other reported systems
Famou-Agent
CAIR MARS+
AIBuildAI
Famou-Agent 2.0
Iris

Gemini-2.5-Pro
Gemini-3-Pro-Preview
Claude-Opus-4.6
Gemini-3-Pro-Preview
Claude-Opus-4.6

75.76 ± 1.52
78.79 ± 1.52
77.27 ± 0.00
80.30 ± 1.52
80.30 ± 1.50

57.89 ± 1.52
60.53 ± 1.52
61.40 ± 0.88
64.04 ± 2.32
64.00 ± 0.90

Open-source baselines
ML-Master 2.0
MLEvolve
PiEvolve
MLEvolve

DeepSeek-V3.2-Speciale 75.76 ± 1.51
Gemini-3-Pro-Preview 80.30 ± 1.52
Gemini-3-Pro-Preview 80.30 ± 1.52
Gemini-3.1-Pro-Preview 80.30 ± 1.50

ScienceFlow
(Ours)

DeepSeek-V4-FlashPreview

80.30 ± 1.52 74.56 ± 0.88 44.44 ± 2.22 70.22 ± 1.18

S02
0.10

Research state
Execution control

0.22

S59

S53

0.20

0.09
0.18
0.08
S112

Test log loss

Best validation
Retrospective test

0.11

Validation log loss

50.88 ± 3.51
57.89 ± 1.52
58.77 ± 0.88
64.00 ± 0.90

0.16

0.07
S123

0.14

0.06


Elapsed time (h)

Figure 3: A 24-hour ScienceFlow trajectory on the Statoil Iceberg Classifier Challenge, showing
validation and retrospective test progress together with checkpointed workspace states and resourcecontrol events. Retrospective test scores are shown only for analysis and are never exposed to the
research agent.

Figure 3 are never exposed to the agent. Their improvement alongside validation provides additional
evidence that the validation signal used during search remains informative for the final submission.
Resource control operates concurrently with trajectory search. Two workers share a single-GPU
device pool, and the marked events show three controller decisions: preserving exclusive GPU access
after a sharing review, terminating a CPU-active job that reports 0% GPU utilization, and falling
back from a blocked heavy execution to lightweight inference, which produces a valid submission in
13.91 seconds. Research-route selection remains with the worker, while the controller admits and
monitors the corresponding physical execution under the available resources.
State-matched re-anchoring study To isolate the effect of re-anchoring from differences in accumulated context and workspace artifacts, we replay seven historical ESTRA decisions from their
captured executable states (Figure 4). At each decision point, four alternatives are evaluated by crossing the execution anchor (current or archived state) with the research direction (extend or redirect),
using three replay seeds and matched four-hour resource budgets, for a total of 84 replay branches.
Because all alternatives are launched from the same recorded decision context and resource budget, their differences enable a controlled comparison of the execution-anchor and research-direction
choices. The historical ESTRA action achieves the best mean replay score, including ties, at five of


Figure 4: State-matched counterfactual replay on the Tabular Playground Series May 2022 task.
Seven historical ESTRA decision points are replayed from their captured executable states under
matched budgets. Each point compares four alternatives formed by current or archived anchors
and extend or redirect directions. Bars show the mean change in retrospective private-test AUROC
relative to the source state across three replay seeds, with error bars denoting sample standard
deviation. Red arrows mark the actions selected in the historical run.

the seven decision points. Relative to an oracle that selects the best of the four replayed actions at
each point, the historical policy has zero median regret and a mean regret of 1.725 × 10−3 AUROC,
with the largest regret of 11.572 × 10−3 occurring at P07.
The two deviations provide complementary evidence about how action value depends on execution
reliability and the remaining search horizon. At P04, the historical archived-redirect action underperforms the source state in all three four-hour replays, including one run that exhausts the replay
budget and degrades substantially. The corresponding original trajectory later reaches a stronger
downstream result after 5.26 hours, indicating that the observed regret reflects both short-horizon
execution instability and delayed payoff. At P07, the historical decision extends the current trajectory
near the end of the 24-hour budget, while the counterfactual replay favors restoration from a strong
archived state. These cases illustrate that effective re-anchoring should account jointly for transition
reliability, remaining budget, and archived-state quality.
Mechanism ablation We ablate ESTRA and Evidence-Aware Execution Control on the official
22-task MLE-bench Lite split under a 24-hour evaluation window. Figure 5 shows the cumulative
first-medal rate over time, where a task is counted once it first reaches Bronze, Silver, or Gold. Curves
show the mean across three seeds, with shaded bands denoting the sample standard deviation. At 24
hours, the full system reaches an Any-Medal rate of 80.30 ± 2.62%, compared with 66.67 ± 2.62%
without ESTRA and 69.70 ± 5.25% without execution control. The difference emerges early: by 12
hours, ScienceFlow reaches 77.27 ± 4.55%, while the two ablations remain at 66.67 ± 2.62% and
69.70 ± 5.25%, respectively. The full system therefore improves both final Any-Medal rate and the
speed of medal acquisition.
Task-level trajectories further separate the two effects. On the Jigsaw Toxic Comment Classification
Challenge, the median first-medal time increases from 2.12 hours with ScienceFlow to 5.17 hours
without ESTRA, while the variant without execution control remains close to the full system at 2.41
hours. This comparison more directly associates the delay with the removal of ESTRA.
Execution control becomes more consequential on longer-running tasks. On the APTOS 2019
Blindness Detection competition, removing Evidence-Aware Execution Control increases the median
first-medal time from 5.18 to 8.05 hours, a 2.87-hour delay, while the slowest seed increases from


0.8

Any-Medal rate

0.7
0.6
0.5
0.4
0.3
0.2

ScienceFlow
w/o ESTRA
w/o execution control

0.1
0.0


Elapsed time (h)

Figure 5: MLE-bench Lite mechanism ablation over a 24-hour window. Curves show the cumulative
Any-Medal rate averaged over three seeds, and shaded bands show the sample standard deviation.

6.64 to 10.45 hours. The corresponding median without ESTRA is 5.91 hours, indicating that the
larger delay is specifically associated with execution control. On the Leaf Classification competition,
ScienceFlow succeeds in all three seeds, whereas both ablations fail in all three. Therefore, this
task can be treated as evidence of joint mechanism dependence rather than attributing it to either
mechanism alone.
System-wide mechanism telemetry To complement the controlled ablations, Table 2 summarizes
mechanism-level telemetry for 54 of the 75 MLE-bench tasks (72.0%) with both ESTRA activity
and workspace-state records. We focus on post-ESTRA completions, checkpoint reuse, and snapshot
reuse as operational indicators of recovery and state reuse, since explicit restoration events are only
sparsely logged. These statistics characterize the behavior of ScienceFlow during execution and are
not used for benchmark scoring.

#### Resource Sensitivity and Efficiency

Resource-Constrained Performance We examine ScienceFlow under tighter storage, compute,
and time budgets. We simulate a 32 GiB per-task storage limit and compare full workspace snapshots
with delta-based states. Among the 33 tasks with available footprint measurements, all delta states
remain below the limit, whereas nine medal-producing tasks exceed it when stored as full snapshots.
Applying these observed violations to the three evaluation seeds reduces the Any-Medal rate from
70.22 ± 1.18% with delta states to 59.11 ± 0.44% with full snapshots. Across the measured tasks,
delta states reduce the aggregate footprint from 2204.6 GiB to 189.2 GiB, a 91.4% reduction. Using
the recorded task-level GPU configurations, we estimate each task to at most one GPU. A tighter
compute budget produces a similar reduction in retained performance. Limiting each task to at most
one GPU yields medals on 48, 48, and 47 tasks across the three runs, corresponding to 63.56±0.44%
Any-Medal, compared with 70.22 ± 1.18% under the reported two-GPU ceiling.
Backbone Sensitivity and Efficiency We test ScienceFlow using four backbones: GLM-5.1,
openPangu-2.0-Pro, DeepSeek-V4-Flash-Preview, and DeepSeek-V4-Pro-Preview, under the same
two-worker, 24-hour protocol on the Tabular Playground Series May 2022 task. In addition to
token consumption, model-priced LLM cost is reported to reflect differences in inference pricing
across backbones. Figure 6 compares their 24-hour token trajectories and endpoint performancecost trade-offs over three independent runs. openPangu-2.0-Pro is served from our local deployment
without prefix/KV-cache optimization, resulting in a 0% cache-hit rate. Its cost is estimated using
Huawei Cloud’s official uncached Pro pricing at the corresponding request-length tier.1 We use
the same model-specific pricing procedure for the other backbones so that reported costs reflect
their actual inference tariffs rather than token counts alone. The results reveal distinct quality,

Huawei Cloud ModelArts Studio pricing, accessed August 3, 2026.


Table 2: Operational telemetry for ScienceFlow mechanisms on 54 of 75 MLE-bench tasks (72.0%
coverage), including ESTRA activity, workspace-state reuse, storage efficiency, and resource control.
Mechanism

ESTRA

Workspace state

Sub-metric

Value

Interpretation

ESTRA decisions
Post-ESTRA completions
Comparable improvements

561 total
71 completed points
19 / 70 (27.1%)

469 continue; 92 switch.
Post-ESTRA outcomes.
Selective gains.

Checkpoint reuse
Snapshot object reuse
Storage footprint
Storage saving

436 / 437 (99.8%)
177,234 / 221,925 (79.9%)
2204.6 GiB → 189.2 GiB
91.4%

Near-complete reuse.
Snapshot dedup.
Storage-covered sources.
Delta footprint.

20,075 samples
27.5%
42.7%
202 stops
157 stops

Device samples.
Observed mean.
> 10% util. buckets.
Guarded stops.
Low-value stops.

Device-utilization samples
Mean utilization
Resource control Active device buckets
Guard terminations
Low-value early stops

throughput, and cost trade-offs. GLM-5.1 processes the most input context and achieves the highest
mean test AUROC of 0.9947, but its $8.11 LLM cost is approximately 84× that of DeepSeekV4-Flash-Preview. DeepSeek-V4-Flash-Preview reaches 0.9882 for $0.096, providing the strongest
quality–cost trade-off among the lower-cost backbones. openPangu-2.0-Pro consumes fewer input
tokens than DeepSeek-V4-Flash-Preview but reaches a lower mean AUROC of 0.9867 at a higher
cost of $0.447, and is therefore dominated by DeepSeek-V4-Flash-Preview on this task. DeepSeekV4-Pro-Preview has the lowest cost at $0.074, but also the lowest mean AUROC at 0.9847. The wider
seed variation of openPangu-2.0-Pro and DeepSeek-V4-Pro-Preview further indicates that backbone
choice affects reliability as well as throughput, cost, and endpoint quality. Given only three runs on
one task, these comparisons are descriptive rather than statistically conclusive.

### 3.2 Mathematical and Engineering Optimization

We evaluate ScienceFlow in two complementary optimization settings: mathematical optimization
problems and tournament scheduling optimization. The former includes three auditable mathematical
problems, while the latter considers the easy, medium, and hard tracks of the SpOC4 KTTSP
challenge. Both require iterative construction and executable validation of candidate solutions, but
differ in problem structure, resource budget, and evaluation protocol. Their setups and results are
presented separately below.

#### 3.2.1 Continuous Mathematical Optimization

Tasks The mathematical optimization suite contains three problems. Circle Packing maximizes
the sum of the radii of 26 disjoint circles inside a unit square under boundary and non-overlap
constraints. Ratio Minimization minimizes dmax /dmin for a configuration of 16 planar points, where
dmin and dmax are the minimum and maximum pairwise distances. Uncertainty Inequality searches
over Hermite–Gaussian constructions to tighten a valid upper bound on the Fourier sign-uncertainty
constant C4 ; Appendix C.1 gives the formal definition.
Protocol For each mathematical problem, ScienceFlow runs for a 12-hour wall-clock budget using
two research workers and a single backbone per run. We evaluate DeepSeek-V4-Flash-Preview and
openPangu-2.0-Pro. We rerun OpenEvolve (Sharma, 2025) locally using its 500-iteration configuration with DeepSeek-V4-Flash-Preview, while published baselines retain their reported setups.
Because budgets and worker topologies differ across systems, the comparison is descriptive rather
than compute-normalized. All ScienceFlow scores are re-evaluated from saved solution artifacts
using task-specific feasibility checks; Appendix C.2 provides the complete audit procedure.
Results Table 3 reports the best audited score from each ScienceFlow configuration. On Circle
Packing, ScienceFlow with DeepSeek-V4-Flash-Preview obtains 2.6359830849, approximately 7.5×
10−9 above ThetaEvolve; at this scale, the two results are best interpreted as a numerical near

GLM-5.1
openPangu-2.0-Pro
DS-V4-Preview
DS-V4-Pro-Preview


0.995

Test AUROC

Input tokens (M)


Time (h)


(a) Cumulative input tokens.

0.990
GLM-5.1
openPangu-2.0-Pro
DS-V4-Preview
DS-V4-Pro-Preview

0.985
0.980

0.1


LLM cost (USD, log)

10.0

(b) Mean best test and cost.

Figure 6: Backbone sensitivity and efficiency on the Tabular Playground Series May 2022 task under
the same two-worker, 24-hour protocol, showing cumulative input-token consumption and endpoint
performance-cost trade-offs over three independent runs. “DS” is an abbreviation for “DeepSeek”
in the figure legends.
tie. On Ratio Minimization, ScienceFlow obtains 3.590157365310609, matching MLEvolve at the
table’s 12-decimal precision. On Uncertainty Inequality, ScienceFlow with openPangu-2.0-Pro
reaches 0.343293122432, reducing the strongest published Hermite-based upper bound by 2.5%.
DeepSeek-V4-Flash-Preview gives the better ScienceFlow result on the first two tasks, whereas
openPangu-2.0-Pro performs better on the uncertainty task.

#### 3.2.2 Combinatorial Scheduling Optimization

Task KTTSP is a main challenge in the fourth ESA Space Optimisation Competition (SpOC4),
organized with GECCO 2026 (European Space Agency, Advanced Concepts Team, 2026). It models
a lunar-orbit collection mission in which a spacecraft must visit all targets in the shortest possible
time. A solution jointly determines the target order, departure epochs, and flight durations. Transfers
follow Lambert dynamics and must satisfy a ∆V limit, with at most E higher-budget exceptions.
We evaluate the easy, medium, and hard instances through the official ESA Optimise evaluator.
Protocol ScienceFlow evaluates all three KTTSP tracks through the official SpOC4 evaluator,
which accepts candidate solutions serialized in the prescribed JSON format. KTTSP-hard is assigned
a separate ten-day campaign using DeepSeek-V4-Pro-Preview, DeepSeek-V4-Flash-Preview, and
GLM-5.1, and provides the persisted worker trace used in the subsequent analysis. We report the
public leaderboard outcomes for all three tracks. Because competing teams do not disclose uniform
compute budgets or model configurations, the leaderboard provides an outcome comparison rather
than a compute-normalized evaluation.
Overall results ScienceFlow obtains scores of 116.911, 234.929, and 393.229 on KTTSP-easy,
KTTSP-medium, and KTTSP-hard, ranking 10th, 8th, and 3rd, respectively. Because the three
tracks use different instances, their raw mission times are not directly comparable across difficulty
levels. On KTTSP-hard, ScienceFlow finishes 42.786 mission days ahead of the fourth-place entry,
fcmaes (436.015), and 55.583 days behind the winning entry, TGMA (337.646). The campaign-level
leaderboard score is 393.229; the worker-level trace analyzed below ends at 393.229.
Long-horizon memory folding Figure 7 traces worker W01 during the ten-day KTTSP-hard
campaign. Across 188 persisted snapshots, the result-card ledger in .run results.md, which
serializes the persistent memory mv , grows from 0.65k to 87.9k characters. In contrast, the 114
recorded context packets assembled at research-segment boundaries remain between 4.4k and 13.4k
characters, with a median size of 8.8k and a median paired packet-to-ledger ratio of 13.7%. This
separation reflects the Add, Fold, and Assemble operations in Section 2.3.4: accumulated stage
records remain persistent, while each new research segment receives a bounded, anchor-specific


Table 3: Best-score comparison on three mathematical optimization tasks. Arrows indicate the
optimization direction. Bold entries denote the best compared results, including ties at the reported
precision; underlined entries denote the second-best results. Published baselines retain their reported protocols, while OpenEvolve is rerun locally under the configuration described in the text.
Uncertainty-inequality results compare only Hermite–Gaussian constructions.
Task

Circle
Packing
P
i ri (↑)

Ratio Minimization
dmax /dmin (↓)

Uncertainty
Inequality
C4 bound (↓)

2 Method

Model

Performance

AlphaEvolve (Novikov et al., 2025) Gemini 2.0 Pro + Flash
ShinkaEvolve (Lange et al., 2025) Claude Sonnet 4 + GPT-4.1
family
ThetaEvolve (Wang et al., 2025b) DeepSeek-R1-0528-Qwen3-8B
MLEvolve (Du et al., 2026)
Gemini-3.1-Pro-Preview

2.6358627564
2.6359828390

OpenEvolve (Sharma, 2025)
ScienceFlow (Ours)
ScienceFlow (Ours)

2.6344194866
2.6359830849
2.6359824748

DeepSeek-V4-Flash-Preview
DeepSeek-V4-Flash-Preview
openPangu-2.0-Pro

2.6359830774
2.6359830395

AlphaEvolve (Novikov et al., 2025) Gemini 2.0 Pro + Flash
FM Agent (Li et al., 2025)
Gemini-2.5-Pro
MLEvolve (Du et al., 2026)
Gemini-3.1-Pro-Preview

3.590162407473
3.590157406159
3.590157365311

OpenEvolve (Sharma, 2025)
ScienceFlow (Ours)
ScienceFlow (Ours)

3.658667107456
3.590157365311
3.590157365325

DeepSeek-V4-Flash-Preview
DeepSeek-V4-Flash-Preview
openPangu-2.0-Pro

AlphaEvolve (Novikov et al., 2025) Gemini Pro + Flash
FM Agent (Li et al., 2025)
Gemini-2.5-Pro
MLEvolve (Du et al., 2026)
Gemini-3.1-Pro-Preview

0.352099104423
0.352099104416
0.352099104416

OpenEvolve (Sharma, 2025)
ScienceFlow (Ours)
ScienceFlow (Ours)

0.352581132500
0.348200107555
0.343293122432

DeepSeek-V4-Flash-Preview
DeepSeek-V4-Flash-Preview
openPangu-2.0-Pro

memory view. The reported packet sizes characterize this dynamic memory component rather than
the complete context Pn+1 of the next research segment.
The trace contains 185 valid evaluation stages and 26 incumbent updates. W01 reduces the objective
from 1928.39 mission days at S01 to 393.229 at S112, a 79.6% reduction. Improvement continues
late in the campaign: after the incumbent remains at 1641.42 days on June 25, phase-aware route
construction coincides with the S80 improvement to 573.03 days, and subsequent route and timing
refinement reaches 420.27 at S97, 415.56 at S109, and 393.229 at S112. At this final incumbent,
the most recent paired context packet contains 6.37k characters, compared with an 80.17k-character
result-card ledger (7.9%). Fourteen subsequent valid trials do not improve the incumbent, indicating
late-stage saturation rather than termination at the first strong solution. This single-run trace does
not establish that memory folding causes the score improvements; it instead shows that late-stage
improvement and continued validation can coexist with a persistent result-card history and bounded
anchor-specific context packets.

Peer-guided search The same trace illustrates cross-worker coordination at research-segment
boundaries. At W01’s S25 research-segment boundary, W00 had reached 521.9054 mission days
while W01 remained at 1746.8935; W00’s validated score prompted W01 to redirect from timingonly refinement toward route ordering. After W01 improved to 1321.8824 days, the S79 researchsegment boundary supplied a compact method summary of W00’s search, prompting an operatorlevel redirect toward route swaps and continuous retiming. W01 subsequently reached a validated
score of 420.2742 within 12 hours and 17 minutes of the S79 decision and later improved to 393.229.
The workers exchanged no executable artifacts or workspace state; all subsequent candidates were
generated and validated within W01’s isolated workspace. The trace therefore illustrates how peer
evidence can guide route selection without direct solution reuse, rather than providing a controlled
estimate of the coordination effect. Appendix D.4 provides the underlying records and checkpoint
timeline.


Table 4: Public leaderboard for the KTTSP-hard track. Scores report total mission elapsed time in
days (lower is better), and timestamps identify each team’s best submission in UTC+8. Boldface
marks the winning score and the ScienceFlow entry. In the model column, DS-V4-Preview denotes
DeepSeek-V4-Flash-Preview, and DS-V4-Pro-Preview denotes DeepSeek-V4-Pro-Preview. Team
names link to their public ESA Optimise profiles. Leaderboard snapshot accessed on July 6, 2026.
Team

Model

Score ↓

Submitted (UTC+8)


TGMA
AC TUWien

337.646
337.700

2026-07-01 13:50
2026-07-01 01:05


ScienceFlow (Ours)

393.229

2026-07-01 09:33


fcmaes
Team HRI
SINTEF
$tellaris
J&C SolExp
ScholORs HFUU+Sunway

–
–
DS-V4-Pro-Preview /
DS-V4-Preview + GLM-5.1
–
–
–
–
–
–

436.015
526.078
587.050
613.794
879.511
1965.276

2026-06-30 14:01
2026-06-30 21:17
2026-06-30 20:27
2026-06-30 04:57
2026-07-05 22:52
2026-05-02 18:10


393.23 d (S112)

Result-card ledger
Context packet
Validation best

400
600


1000
1400


1800
Jun 21

Mission duration (days)

Memory size (k characters)

Rank

2200
Jun 23

Jun 25

Jun 27

Jun 29

Jul 1

Date (UTC)

Figure 7: Persistent-memory growth and validation progress for worker W01 during the ten-day
KTTSP-hard campaign. The right axis uses log10 (score/2000) coordinates with raw mission-day
tick labels; lower is better. Invalid evaluation outputs are excluded.

Route and timing refinement A KTTSP candidate contains two coupled decision components:
−1
a discrete visit permutation π = (v1 , . . . , vN ) and a continuous schedule τ = {(ti , tof i )}N
i=1 of
departure epochs and flight durations. Figure 8 compares two validated candidates generated during
W01’s search: an inclination-binned phase ordering and a phase-proximal construction followed by
multiresolution retiming. The procedures below summarize their decision structures while omitting
implementation-specific optimization loops. These strategies are task-specific artifacts produced by
the research worker rather than fixed components of ScienceFlow.
Initial strategy: Inclination-binned phase ordering.
BIN-INCLINATION → SORT-PHASE → CONCATENATE → FIXED-ROUTE RETIME

The worker groups targets by inclination, orders each group by orbital phase, concatenates the groups, and
then retimes the fixed route. This construction provides a feasible starting route but can retain unfavorable
adjacencies at group boundaries.
Refined strategy: Phase-proximal construction and retiming.
PHASE-NEIGHBORS → LAMBERT-FILTER → APPEND-ROUTE → MULTIRESOLUTION-RETIME → FORWARD-PASS

At each construction step, the worker considers phase-proximal successors, filters infeasible candidates
with the Lambert evaluator, and appends a transfer-aware feasible choice. Coarse-to-fine retiming and a
forward feasibility pass then update the schedule under the temporal and transfer constraints.


Between the evaluator-valid S78 and S112 candidates, fewer than 7% of directed consecutive target
pairs are shared, while mission duration decreases from 1321.8824 to 393.229 days, a 70.25%
reduction. This descriptive comparison associates the improvement with joint route reordering and
retiming rather than isolating individual search operators.

0%

15000

50%
100%
Mission progress

0%

15000

50%
100%
Mission progress

High shell

Visit-time inertial y (km)

Visit-time inertial y (km)

High shell
7500

Low shell
Moon


−7500

−15000

7500

Low shell
Moon


−7500

−15000
Route

−15000

Lambert

−7500

Wait


Start

7500

Final

Route

15000

−15000

Visit-time inertial x (km)

Lambert

−7500

Wait


Start

7500

Final

15000

Visit-time inertial x (km)

(a) Initial strategy at S78: inclination-binned phase (b) Refined strategy at S112: phase-proximal construcordering (1321.8824 days).
tion and retiming (393.229 days).

Figure 8: Route and timing refinement within the W01 KTTSP-hard trajectory. Figures (a) and (b)
visualize two evaluator-valid candidates that visit the same target set. Target color progresses from
blue to yellow with scheduled visit order, and thin links connect consecutive targets.

### 3.3 Scientific Modeling
#### Setup

Benchmark and tasks SciModelingBench tests whether agents can use offline observations to find
high-value designs for a hidden scientific or engineering objective. Its 12 tasks cover seven settings
across DNA binding, RNA and protein design, superconducting materials, preclinical toxicology,
and embodied control. Six DrugMatrix tasks use the same study collection but predict different
clinical pathology endpoints.
The suite begins with scientific settings from Design-Bench (Trabucco et al., 2022), but returns to
their original data and rebuilds the tasks. Learned evaluators make validation approximate and risky
under extrapolation (Beckham et al., 2024); oracle architecture and training seed can also change
method rankings (Surana et al., 2024). We instead standardize candidate identity and repeated
measurements, remove split leakage, regenerate simulator labels with repeated rollouts, and keep
only tasks with reproducible evaluators. The full provenance and reconstruction details are provided
in Appendix E.
Protocol Each task provides an objective, a typed manifest, and offline observations; evaluation
candidates are separated by lower-score truncation or a structured holdout. The agent submits a
ranked list of candidates. When trusted scores cover the full domain, it may propose any valid design
for black-box optimization. Otherwise, it ranks a disclosed pool whose labels remain hidden. Both
settings use measurements, exact lookups, or simulator outcomes rather than a fitted proxy. A fixed
query budget allows iterative improvement, but each query returns only the score of the submitted
batch, not individual candidate outcomes.
Performance metrics We use best-K mean to reward a few strong designs, normalized enrichment
for unordered batches, and global NDCG for ranked submissions. For a batch B of size N and
P
reference pool P , normalized enrichment (NE) is defined as NE(B) = s̄Tops̄B −s̄
−s̄P ; random
N (P )
selection has expected score zero and the ideal batch scores one. We set split thresholds and batch


sizes from data audits and preliminary baselines before the agent runs. For the aggregate score,
Random maps to zero and the attainable oracle optimum to 100. The six DrugMatrix endpoints are
averaged as one group, weighted equally with each of the six other tasks.
Table 5: Task-level results under a two-hour budget with DeepSeek-V4-Flash-Preview. BKM, NE,
and NDCG denote best-K mean, normalized enrichment, and global NDCG. Best and second-best
agent scores are bolded and underlined.
Task

Metric

Random

OpenCode

Pi

Codex

Claude Code

ScienceFlow
(Ours)

0.7533
0.2800
-0.0006
0.0000
0.0001
0.1698

0.9764
0.4929
0.6523
0.2467
0.2600
0.3917

0.9730
0.8671
0.7533
0.2473
0.2692
0.3248

0.9718
0.8188
0.7424
0.2024
0.2586
0.3755

0.9648
0.8132
0.7367
0.3197
0.1977
0.3718

0.9769
0.8583
0.7605
0.2543
0.2732
0.3756

0.7344
0.4147
0.6081
0.7619
0.5106
0.4130

0.3720
0.3673
0.7638
0.8283
0.4551
0.4917

0.6178
0.4242
0.5681
0.7696
0.5589
0.3749

0.6503
0.3623
0.8038
0.8498
0.5397
0.3999

0.7220
0.4793
0.6995
0.8488
0.5488
0.5985

Standalone scientific design tasks
TFBind8
Superconductor
UTR MRL
TFBind10 Pho4
GFP
Hopper Controller

BKM
NDCG
NE
NE
NE
NDCG

Rat clinical pathology tasks (DrugMatrix)
MCHC
MCH
Creatinine
Sodium
Chloride
Phosphorus

NDCG
NDCG
NDCG
NDCG
NDCG
NDCG

0.1733
0.2669
0.1955
0.1519
0.1689
0.2040

Table 6: Group-balanced results. Scores map Random to 0 and the attainable optimum to 100. The
DrugMatrix endpoints form one group, weighted equally with each standalone task. Average rank
uses the same seven groups. Best and second-best values are bolded and underlined; lower rank is
better.
Standalone
Design (6)

Rat Clinical
Pathology (6)

Group-balanced
Score ↑

7-group Avg.
Rank ↓

Task Wins

Pi
Claude Code
Codex
OpenCode

52.77
51.65
51.49
43.84

43.12
49.64
43.79
46.44

51.39
51.37
50.39
44.21

2.79
3.69
3.64
3.33

1/12
3/12
1/12
2/12

ScienceFlow (Ours)

54.16

55.91

54.41

1.55

5/12

Agent

Model, compute and evaluation budget All systems use DeepSeek-V4-Flash-Preview with the
same two-hour limit and the same task-level quota of 8–20 batch submissions, fixed before the
runs. We run each system–task pair once and report its best valid submission within these limits.
ScienceFlow splits the quota between two homogeneous workers, which share only short summaries
of their best score and method. Each system–task run uses eight logical CPU cores, no accelerator,
and less than 32 GiB peak RSS.
Tools and baselines Agents receive an isolated workspace with shell, Python, and common data
and machine-learning packages. Hidden labels and evaluator state remain outside the workspace,
and network access is disabled. The model may still use knowledge learned during pretraining. We
compare ScienceFlow with OpenCode, Pi, Codex, and Claude Code (OpenCode Contributors, 2026;
Zechner, 2026; OpenAI, 2026a; Anthropic, 2026).

#### Main Results

We report results at both the task level and after group-balanced aggregation. As a reference,
Random is the mean score of 5,000 uniformly sampled, task-sized batches. Each batch contains
distinct candidates and, for ranking tasks, uses a random order.
Table 5 reports the task-level results. All five systems beat Random on every task. ScienceFlow
ranks first on five tasks and second on six, placing in the top two on 11 of 12. It leads on TFBind8,
UTR MRL, GFP, MCH, and Phosphorus. Its largest margins over the runner-up are 0.0551 on MCH


Table 7: Candidate coverage in the Phosphorus case study. Repeated conditions across batches are
counted once; coverage is relative to the 390-condition candidate pool.
System

Distinct candidates

Pool coverage


16.9%
9.7%
8.2%
6.2%
8.2%

ScienceFlow
Pi
OpenCode
Codex
Claude Code

Group-balanced normalized score


ScienceFlow

Pi

OpenCode

Codex

Claude Code
ScienceFlow lead


ScienceFlow deficit

0%

10%

20%

30%

40%

50%

60%

70%

80%

90%

100%

80%

90%

100%

Evaluator query budget used

(a) Group-balanced best-so-far score.
Δ score

−5
−10
0%

10%

20%

30%

40%

50%

60%

70%

Evaluator query budget used

(b) ScienceFlow’s signed margin over the strongest baseline at each budget fraction.

Figure 9: Cross-task progress under matched query budgets. The DrugMatrix endpoints form one
group, and ScienceFlow’s worker submissions are merged in chronological order.

and 0.1068 on Phosphorus, while TFBind8 is nearly tied at a margin of 0.0005. Creatinine is its only
result outside the top two.
Table 6 summarizes the group-balanced comparison. ScienceFlow scores highest on both groups,
with 54.16 on the standalone tasks and 55.91 on rat clinical pathology. Its overall score is 54.41,
3.02 points above Pi, and its average rank is 1.55 versus Pi’s 2.79. Each of the other agents leads at
least one task, showing that their strengths differ by domain.

#### Analysis

Case study: independent hypothesis coverage We use DrugMatrix Phosphorus as a case study of
exploration under sparse feedback. Each system has eight batch evaluations and ranks 16 of 390 labelhidden five-day treatment conditions by their change in phosphorus relative to matched controls. The
evaluator reports only a batch score, with no candidate-level labels. Table 7 summarizes coverage
across the eight batches.
ScienceFlow evaluates 66 distinct conditions, compared with 24–38 for the baselines. Its two workers
each cover 43 conditions, with only 20 shared. One uses a general molecular and experimentalcontext model; the other models repeated measurements and matches treatment and control across
dose and duration. Their partly non-overlapping coverage reflects complementary, protocol-aware


hypotheses rather than duplicate searches, under the same eight submissions and batch-level feedback
as the baselines.
Query-budget saturation across tasks We next track the aggregate best-so-far score across all 12
tasks to see how quickly each system uses its query quota.
Figure 9 shows that Codex leads from 10% through 20% of the quota, but ScienceFlow jumps from
38.43 to 52.24 at 25% and remains ahead thereafter. Its advantage over the strongest baseline is
about five points at that point and ends at 3.01. By 50%, ScienceFlow, Codex, and Claude Code are
within 2.2 points of their final scores, while Pi has reached 92% of its final score. By 80%, those
four are within 0.36 points; OpenCode improves later. Most systems therefore approach their final
result before exhausting the quota, leaving room for several rounds of refinement rather than making
the last query decisive.


## 4 Related Work


### 4.1 Scientific Agents

Several recent surveys systematize this rapidly fragmenting landscape along complementary axes:
a six-stage methodological pipeline and three-phase historical evolution (Tie et al., 2026); a fivetask taxonomy spanning scientific comprehension, academic survey, discovery, writing, and peer
review (Chen et al., 2025); a decomposition into five foundational agent capabilities (reasoning and
planning, tool integration, memory, multi-agent collaboration, and optimization) measured along
an autonomy scale from “computational oracle” to “generative architect” (Wei et al., 2025); and a
task-and-evaluation lifecycle view that emphasizes benchmarking, trustworthiness, and the risks of
generative misuse (Eger et al., 2026).
Representative end-to-end systems instantiate this paradigm across disciplines. In machine learning,
The AI Scientist (Lu et al., 2024b) unified idea generation, code execution, and paper writing into the
first fully autonomous research loop, and its successor employs agentic tree search to explore parallel
research directions and self-review the resulting manuscripts (Yamada et al., 2025). In the natural
sciences, agents now couple LLM reasoning with wet-lab hardware to autonomously plan, execute,
and interpret experiments, from chemical synthesis (Boiko et al., 2023) to the de-novo design of
experimentally validated nanobodies by multi-agent virtual research teams (Swanson et al., 2025),
while generate–debate–evolve multi-agent systems (Wei et al., 2025) and self-evolving pipelines that
expand their own toolkits (Novikov et al., 2025) push toward long-horizon, cross-domain discovery.
The same agentic primitives—iterative refinement over literature (Baek et al., 2025), case-based
reasoning (Guo et al., 2024), reflection (Shinn et al., 2023), and executable skill libraries for openended embodied learning (Wang et al., 2023)—recur across these systems, and analogous techniques
now extend to software engineering (Antoniades et al., 2025), algorithm and reward design (RomeraParedes et al., 2024; Lu et al., 2024a; Faldor et al., 2025; Hazra et al., 2025), and open-ended scientific
discovery (O’Neill et al., 2025).
Despite this breadth, the field shares persistent limitations that the surveys converge on: brittle
reproducibility and provenance, uncalibrated confidence and weak novelty validation, monolithic
domain-specific architectures that fail to transfer, and long-horizon memories that cannot sustain
causally-linked experiment histories (Tie et al., 2026; Wei et al., 2025; Eger et al., 2026). Machinelearning engineering is the most mature and most heavily benchmarked slice of this paradigm: a
fully simulated discovery loop that exercises experimental preparation, execution, and iterative optimization without a wet lab, with protocols such as MLE-bench (Chan et al., 2025) providing a
standardized, compute-bounded testbed. ScienceFlow is positioned squarely within this slice, advancing the execution, optimization, and memory capabilities that the broader AI-Scientist literature
identifies as the binding bottlenecks to trustworthy autonomy.

### 4.2 MLE Agents

MLE-bench (Chan et al., 2025) has recently emerged as the de facto evaluation protocol for autonomous machine-learning-engineering (MLE) agents. It curates 75 real-world Kaggle competitions spanning tabular, vision, language, audio, and time-series modalities, requiring agents to deliver


end-to-end solutions within a fixed 24-hour budget on a single GPU. Submissions are evaluated directly against original Kaggle medal thresholds and screened for plagiarism via automated detectors.
The reference baseline—the tree-search agent AIDE (Jiang et al., 2025) powered by o1-preview—
attains a mere 16.9% medal rate on the full benchmark. This pronounced gap between AI and human
performance has catalyzed a rapid proliferation of novel agent architectures.
We survey this expanding landscape along three complementary dimensions: search, multi-agent
collaboration, and memory.
Search- and evolution-driven agents A prominent line of work formulates solution generation as
search over a structured code space. Toledo et al. (2025) provide a unifying formalization of these
agents; critically, they demonstrate that under AIDE’s operator set, advanced search policies (e.g.,
Monte Carlo tree search, evolutionary algorithms) yield marginal benefits. Their analysis points
to the operator set as a key bottleneck and further reveals a validation-to-test generalization gap
that can misdirect search trajectories. ML-Master (Liu et al., 2025) expands this search process
with MCTS-inspired exploration and a steerable reasoning engine conditioned on adaptive memory
from parent and sibling trajectories. MARS (Chen et al., 2026b) combines budget-aware MCTS
with an efficiency-guided reward, a modular design-decompose-implement pipeline, and comparative
reflective memory for credit assignment, achieving a 56%-62.7% medal rate. MLEvolve (Du et al.,
2026) further replaces the rigid search tree with Monte Carlo graph search, allowing non-adjacent
solutions to recombine through cross-branch references. Together with an entropy-driven exploration
schedule, it reaches a 65.3% medal rate under half of the standard time budget. Iris (Fu et al.,
2026) shifts from solution-centric search to an inquiry, which builds revision loop over a revisable
information state, using epistemic actions to resolve decision-critical unknowns and reaching a 64.9%
Any-Medal rate under a 12-hour budget.
Hierarchical multi-agent systems Rather than refining a centralized search policy, an alternative
paradigm decomposes the engineering workflow into collaborating specialists. For instance, R&D
Agent (Yang et al., 2025a) implements a dynamic interaction between ”Researcher” and ”Developer”
roles to periodically synthesize superior outcomes, while InternAgent (InternAgent Team, 2025)
proposes a closed-loop framework that tightly integrates idea generation with experimental execution.
To scale such coordination, the FM Agent (Li et al., 2025) employs a multi-population island
evolutionary model, augmented by expert-guided cold starts and diversity-driven sampling on a
distributed asynchronous infrastructure. Addressing cognitive biases, MLE-STAR (Nam et al., 2025)
counteracts the tendency of agents to over-rely on familiar, outdated models through web-searchbased initialization and ablation-guided code refinement, integrating explicit data-leakage checkers
for robustness. More recently, AIBuildAI (Zhang et al., 2026a) introduces a hierarchical Manager–
Designer–Coder–Tuner topology that adaptively orchestrates seven parallel solution repositories,
boosting the full-benchmark medal rate to 63.1%.
Memory, knowledge, and long-horizon control Because long-horizon MLE tasks generate extensive execution histories that quickly saturate context windows, contemporary architectures prioritize
restructuring memory over simply expanding it. ML-Master 2.0 (Zhu et al., 2026) introduces a threetier hierarchical cognitive cache that distills transient execution traces into cross-task insights, lifting
the full-benchmark success rate to 56.4%. KAPSO (Nadafian et al., 2026) grounds code optimization
in a Git-native experimentation engine and a typed knowledge graph extracted from thousands of
repositories, achieving a 50.7% medal rate. Other works target environment reliability and state
persistence: a file-as-bus framework (Chen et al., 2026a) externalizes decision-relevant states for
long-horizon control; Arbor (Jin et al., 2026) maintains a persistent hypothesis tree regulated by
a held-out merge gate; and EurekAgent (Xin et al., 2026) posits that engineering the operational
environment, including permissions, artifacts, and budgets, is more critical than prescribing rigid
workflows. Complementary efforts explore reinforcement learning for strategic ideation (Zhang et al.,
2026c), lightweight ReAct-style memory tiers (Chopde et al., 2025), and alignment risks, demonstrating that agents can be steered to sandbag or backdoor solutions while evading language-model
monitors (Ward et al., 2025).
Closest mechanisms and distinction Several adjacent systems expose individual mechanisms
used by ScienceFlow, but assign them different roles. AutoSci stores typed project artifacts and
lifecycle states in an active research memory (Qian et al., 2026), while MAGE organizes action–


observation histories as an execution-state tree and revises erroneous segments from a restored
boundary (Chen et al., 2026c). PIVOT instead refines planned trajectories through repeated execution
and verification (Zhang et al., 2026b). At the systems layer, recent agentic schedulers combine
admission control with live CPU–GPU telemetry (Wang et al., 2026) or use an LLM and runtime
monitor to select immediate GPU execution, queued GPU execution, or CPU offload (Lu & Reda,
2026). ScienceFlow does not claim that memory, checkpointing, trajectory revision, or resource
scheduling is individually new. Its distinction is to make a recoverable executable research state—
not a dialogue trace, candidate script, workflow variable, or inference session—the common object
of persistence, trajectory adaptation through re-anchoring, and evidence-aware execution control.
Consequently, scientific route selection remains with the research agent, whereas a separate controller
owns resource admission and termination authority using both physical constraints and validated
research progress.

### 4.3 Optimization Agents

Parallel to the MLE-bench paradigm, a distinct class of autonomous agents has emerged to tackle
numerical and combinatorial optimization. Rather than relying on fixed heuristics, these agents
iteratively propose, evaluate, and refine solutions, and are benchmarked on standard black-box suites
(e.g., BBOB (Hansen et al., 2021)) as well as high-stakes engineering tasks. The core challenge is
that an agent must operate within a limited interaction budget, extract actionable knowledge from
a growing trial history, and balance exploration with exploitation. We survey this agent-driven
optimization landscape along three complementary dimensions: prompt-level search, agent-guided
algorithm design, and hierarchical multi-agent end-to-end pipelines.
Agents That Optimize at the Prompt Level The most direct agent architecture converts optimization into a natural-language sequential decision process. Instead of explicitly coding search
operators, the agent relies entirely on prompt-based reasoning over previous trials (Cheng et al.,
2024). The OPRO framework exemplifies this approach: it encapsulates the entire optimization
trajectory within a meta-prompt, enabling the agent to propose improved candidates solely by analyzing score sequences (Yang et al., 2024). This paradigm has achieved state-of-the-art results
in prompt tuning, code generation, and even mathematical reasoning. Nevertheless, pure promptlevel agents often exhibit strong warm-start behavior but stagnate in later iterations, lacking the
rigorous exploration-exploitation trade-off mechanisms inherent to classical solvers. Consequently,
hybrid agents are being developed that couple prompt-based candidate generation with Bayesian
optimization surrogates, combining semantic insight with principled uncertainty management.
Agents That Design Optimization Algorithms A second dimension elevates the role of the agent
from solution proposer to solver architect. Here, agents are embedded within classical optimization
pipelines as intelligent components that design, configure, and evolve the algorithms themselves.
Rather than merely executing a fixed solver, these agents actively shape the optimization process:
they recommend promising candidate solutions informed by domain priors, strategically narrow or
restructure the search space to focus on high-potential regions, and filter or rank evaluated candidates to guide subsequent iterations (Pandit et al., 2025; Yang et al., 2025b). Beyond solution-level
guidance, agents also autonomously synthesize novel crossover and mutation operators by analyzing
historical population statistics (Suwandi et al., 2025), dynamically adjust algorithm hyperparameters
in response to convergence trends, and serve as lightweight surrogate evaluators that predict solution
quality to reduce costly full simulations (Yuan et al., 2026). Works such as EvoLLM (Lange et al.,
2024) demonstrate that an agent can iteratively refine a differential evolution algorithm across generations, effectively endowing the solver with self-evolution capabilities. This shifts the optimization
problem from finding a single solution to continuously improving the algorithm that finds solutions.
Hierarchical Multi-Agent End-to-End Optimization Pipelines A hierarchical multi-agent system can decompose complex optimization workflows into specialized roles when a single agent
cannot effectively manage problem formulation, constraint analysis, code generation, and evaluation.
Typical architectures decompose the workflow into specialized roles such as algorithm selection,
constraint analysis, code generation, and execution evaluation, which collectively form a fully automated pipeline that covers the entire optimization life cycle (Guo et al., 2025; Baumann & Kramer,
2025). These collectives have demonstrated competitive performance on standard benchmarks and


have been extended to adversarial settings where multiple agents cooperatively generate adversarial examples to probe and improve model robustness. Furthermore, experience-driven multi-agent
frameworks allow agents to accumulate and transfer knowledge across tasks, dramatically improving
sample efficiency in repeated black-box attack scenarios. By distributing cognitive load and enabling
inter-agent critique, these hierarchical architectures deliver more robust and high-quality solutions
than their single-agent counterparts.


## 5 Conclusion

We have introduced ScienceFlow, a workspace-grounded autonomous research system for longhorizon executable work. ScienceFlow combines recoverable workspace states, ESTRA-governed
transitions between research segments, and evidence-aware execution control, while supporting configurable homogeneous research workers with isolated workspaces and synchronization at researchsegment boundaries. We evaluated ScienceFlow across machine learning engineering, mathematical and engineering optimization, and scientific modeling and design. ScienceFlow achieves
70.22 ± 1.18% Any-Medal on the full 75-task MLE-bench. Across mathematical and engineering
optimization, ScienceFlow matches the strongest results on circle packing and ratio minimization,
improves the best published Hermite-based uncertainty bound by 2.5%, and ranks third on KTTSPhard. On SciModelingBench, ScienceFlow achieves the best group-balanced score of 54.41 among
the evaluated agents. Overall, ScienceFlow delivers strong and consistent performance across a
diverse range of long-horizon autonomous research tasks.


## Contributions and Acknowledgments
Mingming Zhao, Jiqian Dong, Kangping Xu† , Zadid Hasan, Chengrui Fan, Shan Jiang, Shuai Mao,
Ting Lingya, Linyi Zou, Tailin Zhou, Yun Hin Chan, Wenkai Zhang, Zhanhong Zhou, Guowei
Huang, Hongliang Li, Wenjing Cun, Zhitang Chen* , Mingxuan Yuan* , and Yanhui Geng* .

†
*

Work completed during an internship.
Team leaders.


References
Anthropic. Claude Code. npm software release, 2026. URL https://www.npmjs.com/package/
@anthropic-ai/claude-code/v/2.1.72. Version 2.1.72; accessed August 12, 2026.
Antonis Antoniades, Albert Örwall, Kexun Zhang, Yuxi Xie, Anirudh Goyal, and William Yang
Wang. SWE-search: Enhancing software agents with monte carlo tree search and iterative refinement. In International Conference on Learning Representations, 2025.
Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. Researchagent: Iterative
research idea generation over scientific literature with large language models. In Proceedings of
the 2025 conference of the nations of the Americas chapter of the association for computational
linguistics: human language technologies (volume 1: long papers), pp. 6709–6738, 2025.
Luis A. Barrera, Anastasia Vedenko, Jesse V. Kurland, et al. Survey of variation in human transcription factors reveals prevalent DNA binding changes. Science, 351(6280):1450–1454, 2016. doi:
10.1126/science.aad2257.
Jill Baumann and Oliver Kramer. An llm-based multi-agent framework for evolutionary blackbox optimization. In Proceedings of the Genetic and Evolutionary Computation Conference Companion,
GECCO ’25 Companion, pp. 671–674, New York, NY, USA, 2025. Association for Computing
Machinery. ISBN 9798400714641. doi: 10.1145/3712255.3726575.
Christopher Beckham, Alexandre Piché, David Vázquez, and Christopher Pal. Exploring validation
metrics for offline model-based optimisation with diffusion models. Transactions on Machine
Learning Research, 2024. URL https://openreview.net/forum?id=wC4ZID0H9a.
Daniil A. Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical research
with large language models. Nature, 624(7992):570–578, 2023. ISSN 1476-4687.
Dmitry Bolotin. Local fitness landscape of the green fluorescent protein. figshare dataset, 2016.
URL https://doi.org/10.6084/m9.figshare.3102154.v1. Dataset; CC BY 4.0.
Sai Kiran Botla, Kirubanath Sankar, Abhishek Chopde, and Fardeen Pettiwala. Pi-Evolve:
Long-horizon evolutionary optimization for autonomous scientific discovery. GitHub software,
2025. URL https://github.com/FractalAIResearchLabs/PiEvolve. Accessed August
12, 2026.
Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio
Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, et al. Mle-bench: Evaluating machine
learning agents on machine learning engineering. International Conference on Learning Representations, 2025.
Guoxin Chen, Jie Chen, Lei Chen, Jiale Zhao, Fanzhe Meng, Wayne Xin Zhao, Ruihua Song, Cheng
Chen, Ji-Rong Wen, and Kai Jia. Toward autonomous long-horizon engineering for ml research.
arXiv preprint arXiv:2604.13018, 2026a.
Jiefeng Chen, Bhavana Dalvi Mishra, Jaehyun Nam, Rui Meng, Tomas Pfister, and Jinsung
Yoon. Mars: Modular agent with reflective search for automated ai research. arXiv preprint
arXiv:2602.02660, 2026b.
Qiguang Chen, Mingda Yang, Libo Qin, Jinhao Liu, Zheng Yan, Jiannan Guan, Dengyun Peng,
Yiyan Ji, Hanjing Li, Mengkang Hu, Yimeng Zhang, Yihao Liang, Yuhang Zhou, Jiaqi Wang,
Zhi Chen, and Wanxiang Che. AI4Research: A Survey of Artificial Intelligence for Scientific
Research, 2025. arXiv:2507.01903.
Yaoqi Chen, Haibin Lai, Yuru Feng, Chuyu Han, et al. Beyond semantic organization: Memory as
execution state management for long-horizon agents. arXiv preprint arXiv:2606.06090, 2026c.
Jiale Cheng, Xiao Liu, Kehan Zheng, Pei Ke, Hongning Wang, Yuxiao Dong, Jie Tang, and Minlie
Huang. Black-box prompt optimization: Aligning large language models without model training.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pp. 3201–3219, 2024.


Abhishek Chopde, Fardeen Pettiwala, Sankar Kirubananth, Sai Kiran Botla, and Pachipulusu Ayyappa Kethan. PiML: Automated machine learning workflow optimization using LLM
agents. In Proceedings of the Fourth International Conference on Automated Machine Learning,
volume 293 of Proceedings of Machine Learning Research, pp. 1/1–42. PMLR, 2025. URL
https://proceedings.mlr.press/v293/chopde25a.html.
Shangheng Du, Xiangchao Yan, Jinxin Shi, Zongsheng Cao, Shiyang Feng, Zichen Liang, Boyuan
Sun, Tianshuo Peng, Yifan Zhou, Xin Li, Jie Zhou, Liang He, Bo Zhang, and Lei Bai. Mlevolve:
A self-evolving framework for automated machine learning algorithm discovery. arXiv preprint
arXiv:2606.06473, 2026.
Steffen Eger, Yong Cao, Jennifer D’Souza, Andreas Geiger, Christian Greisinger, Stephanie Gross,
Yufang Hou, Brigitte Krenn, Anne Lauscher, Yizhi Li, Chenghua Lin, Nafise Sadat Moosavi,
Wei Zhao, and Tristan Miller. Transforming Science with Large Language Models: A Survey
on AI-assisted Scientific Discovery, Experimentation, Content Generation, and Evaluation, 2026.
arXiv:2502.05151.
European Space Agency, Advanced Concepts Team. SpOC 4: Space Logistics. European
Space Agency competition webpage, 2026. URL https://www.esa.int/gsp/ACT/news/
spoc-2026/. Accessed August 12, 2026.
Maxence Faldor, Jenny Zhang, Antoine Cully, and Jeff Clune. OMNI-EPIC: Open-endedness
via models of human notions of interestingness with environments programmed in code. In
International Conference on Learning Representations, 2025.
Fordyce Lab. BET-seq Processed Data. figshare dataset, 2018. URL https://doi.org/10.6084/
m9.figshare.5728467.v1. Dataset; CC BY 4.0.
Shaokang Fu, Yulong Tao, Linbo Jin, Jiarong Zhao, Qiming Shi, Tianjun Pan, Haonan Li, Chengyu
Wang, Jia Wu, and Chengfu Huo. Beyond solution-centric search: Adaptive inquiry and knowledge
revision for autonomous ML engineering. arXiv preprint arXiv:2608.02143, 2026.
Felipe Gonçalves, Diogo Oliveira e Silva, and Stefan Steinerberger. Hermite polynomials, linear
flows on the torus, and an uncertainty principle for roots. Journal of Mathematical Analysis and
Applications, 451(2):678–711, 2017. doi: 10.1016/j.jmaa.2017.02.030. URL https://doi.
org/10.1016/j.jmaa.2017.02.030.
Hongshu Guo, Zeyuan Ma, Yining Ma, Xinglin Zhang, Wei-Neng Chen, and Yue-Jiao Gong.
DesignX: Human-competitive algorithm designer for black-box optimization. Advances in Neural
Information Processing Systems, 38:6582–6615, 2025.
Siyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, and Jun Wang. DS-agent:
Automated data science by empowering large language models with case-based reasoning.
In Proceedings of the 41st International Conference on Machine Learning, volume 235 of
Proceedings of Machine Learning Research, pp. 16813–16848. PMLR, 2024. URL https:
//proceedings.mlr.press/v235/guo24b.html.
Kam Hamidieh. A data-driven statistical model for predicting the critical temperature of a superconductor. Computational Materials Science, 154:346–354, 2018a. doi: 10.1016/j.commatsci.2018.
07.052.
Kam Hamidieh. Superconductivty data. UCI Machine Learning Repository, 2018b. URL https:
//doi.org/10.24432/C53P47. Dataset; CC BY 4.0.
Nikolaus Hansen, Anne Auger, Raymond Ros, Olaf Mersmann, Tea Tušar, and Dimo Brockhoff.
Coco: A platform for comparing continuous optimizers in a black-box setting. Optimization
Methods and Software, 36(1):114–144, 2021.
Rishi Hazra, Alkis Sygkounas, Andreas Persson, Amy Loutfi, and Pedro Zuidberg Dos Martires.
REvolve: Reward evolution with large language models using human feedback. In International
Conference on Learning Representations, 2025.
HeyNeo Team. Neo: Next-generation ai agents. https://heyneo.so/blog, 2025.


Maxwell A. Hume, Luis A. Barrera, Stephen S. Gisselbrecht, and Martha L. Bulyk. UniPROBE,
update 2015: New tools and content for the online database of protein-binding microarray data
on protein–DNA interactions. Nucleic Acids Research, 43(D1):D117–D122, 2015. doi: 10.1093/
nar/gku1045.
InternAgent Team. Internagent: When agent becomes the scientist – building closed-loop system
from hypothesis to verification. arXiv preprint arXiv:2505.16938 [cs.AI], 2025.
Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and
Yuxiang Wu. Aide: Ai-driven exploration in the space of code. arXiv preprint arXiv:2502.13138,
2025.
Jiajie Jin, Yuyang Hu, Kai Qiu, Qi Dai, Chong Luo, Guanting Dong, Xiaoxi Li, Tong Zhao, Xiaolong
Ma, Gongrui Zhang, et al. Toward generalist autonomous research via hypothesis-tree refinement.
arXiv preprint arXiv:2606.11926, 2026.
Robert Lange, Yingtao Tian, and Yujin Tang. Large language models as evolution strategies. In
Proceedings of the Genetic and Evolutionary Computation Conference Companion, pp. 579–582,
2024.
Robert Tjarko Lange, Yuki Imajuku, and Edoardo Cetin. Shinkaevolve: Towards open-ended and
sample-efficient program evolution. arXiv preprint arXiv:2509.19349, 2025.
Daniel D. Le, Tyler C. Shimko, Arjun K. Aditham, Allison M. Keys, Scott A. Longwell, Yaron
Orenstein, and Polly M. Fordyce. Comprehensive, high-resolution binding energy landscapes
reveal context dependencies of transcription factor binding. Proceedings of the National Academy
of Sciences, 115(16):E3702–E3711, 2018. doi: 10.1073/pnas.1715888115.
Annan Li, Chufan Wu, Zengle Ge, Yee Hin Chong, Zhinan Hou, Lizhe Cao, Cheng Ju, Jianmin
Wu, Huaiming Li, Haobo Zhang, Shenghao Feng, Mo Zhao, Fengzhi Qiu, Rui Yang, Mengmeng
Zhang, Wenyi Zhu, Yingying Sun, Quan Sun, Shunhao Yan, Danyu Liu, Dawei Yin, and Dou
Shen. The FM agent. CoRR, abs/2510.26144, 2025.
Zexi Liu, Yuzhu Cai, Xinyu Zhu, Yujie Zheng, Runkun Chen, Ying Wen, Yanfeng Wang, Siheng
Chen, et al. Ml-master: Towards ai-for-ai via integration of exploration and reasoning. arXiv
preprint arXiv:2506.16499, 2025.
Chris Lu, Samuel Holt, Claudio Fanconi, Alex James Chan, Jakob Nicolaus Foerster, Mihaela van der
Schaar, and Robert Tjarko Lange. Discovering preference optimization algorithms with and for
large language models. In Advances in Neural Information Processing Systems, 2024a.
Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The AI Scientist:
Towards Fully Automated Open-Ended Scientific Discovery, 2024b. arXiv:2408.06292.
Tianxi Lu and Sherief Reda. Agentic cpu-gpu scheduling for heterogeneous ai workloads. arXiv
preprint arXiv:2607.22242, 2026.
Alireza Nadafian, Alireza Mohammadshahi, and Majid Yazdani. Kapso: A knowledge-grounded
framework for autonomous program synthesis and optimization. arXiv preprint arXiv:2601.21526,
2026.
Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Jinwoo Shin, Sercan Ö Arık, and Tomas Pfister. Mlestar: Machine learning engineering agent via search and targeted refinement. arXiv preprint
arXiv:2506.15692, 2025.
National Toxicology Program (NTP). DrugMatrix. Chemical Effects in Biological Systems (CEBS),
2023. URL https://doi.org/10.22427/NTP-DATA-107-022-001-000-3.
Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt
Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian,
M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian
Nowozin, Pushmeet Kohli, and Matej Balog. Alphaevolve: A coding agent for scientific and
algorithmic discovery, 2025. URL https://arxiv.org/abs/2506.13131.


Charles O’Neill, Tirthankar Ghosal, Roberta Răileanu, Mike Walmsley, Thang Bui, Kevin Schawinski, and Ioana Ciucă. Sparks of science: Hypothesis generation using structured paper data. arXiv
preprint arXiv:2504.12976, 2025.
OpenAI. Codex CLI. npm software release, 2026a. URL https://www.npmjs.com/package/
@openai/codex/v/0.144.5. Version 0.144.5; accessed August 12, 2026.
OpenAI. MLE-bench Leaderboard. GitHub repository, 2026b. URL https://github.com/
openai/mle-bench. Accessed August 12, 2026.
OpenCode Contributors. OpenCode: The open source AI coding agent. npm software release, 2026.
URL https://www.npmjs.com/package/opencode-ai/v/1.18.4. Version 1.18.4; accessed
August 12, 2026.
Sujay Pandit, Akanksha Jain, Rami Cohen, Zhijie Deng, Sagar Karandikar, Sagi Perel, Anand
Raghunathan, and Parthasarathy Ranganathan. LLM-box : An agentic framework for guided
black-box optimization in mapping LLMs onto specialized hardware accelerators. In Machine
Learning for Systems 2025, 2025.
Weitong Qian, Beicheng Xu, Zhongao Xie, Bowen Fan, et al. Autosci: A memory-centric agentic
system for the full scientific research lifecycle. arXiv preprint arXiv:2605.31468, 2026.
Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog,
M. Pawan Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan S. Ellenberg, Pengming Wang,
Omar Fawzi, Pushmeet Kohli, and Alhussein Fawzi. Mathematical discoveries from program
search with large language models. Nature, 625(7995):468–475, 2024. ISSN 1476-4687.
Paul J. Sample, Ban Wang, and Georg Seelig. Human 5’ UTR design and variant effect prediction from a massively parallel translation assay. NCBI Gene Expression Omnibus, 2018. URL
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114002. Dataset; accession GSE114002.
Paul J. Sample, Ban Wang, David W. Reid, Vlad Presnyak, Iain J. McFadyen, David R. Morris,
and Georg Seelig. Human 5’ UTR design and variant effect prediction from a massively parallel
translation assay. Nature Biotechnology, 37(7):803–809, 2019. doi: 10.1038/s41587-019-0164-5.
Karen S. Sarkisyan, Dmitry A. Bolotin, Margarita V. Meer, et al. Local fitness landscape of the green
fluorescent protein. Nature, 533(7603):397–401, 2016. doi: 10.1038/nature17995.
SciModelingBench. SciModelingBench Design-Bench Data. Hugging Face dataset, 2026. Hugging
Face dataset, version 0.10.0.
Asankhaya Sharma. OpenEvolve: An open-source evolutionary coding agent. GitHub software,
2025. URL https://github.com/codelion/openevolve. Accessed August 12, 2026.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion:
language agents with verbal reinforcement learning. In Advances in Neural Information Processing
Systems, volume 36, pp. 8634–8652, 2023.
Shikha Surana, Nathan Grinsztajn, Timothy Atkinson, Paul Duckworth, and Thomas D. Barrett.
Overconfident oracles: Limitations of in silico sequence design benchmarking. In ICML 2024
Workshop on AI for Science, 2024. URL https://openreview.net/forum?id=fPBCnJKXUb.
Richard Cornelius Suwandi, Feng Yin, Juntao Wang, Renjie Li, Tsung-Hui Chang, and Sergios
Theodoridis. Adaptive kernel design for bayesian optimization is a piece of CAKE with LLMs.
In The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025.
Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak, and James Zou. The virtual lab of AI
agents designs new SARS-CoV-2 nanobodies. Nature, 646:716–723, 2025.
Guiyao Tie, Pan Zhou, and Lichao Sun. A Survey of AI Scientists, 2026. arXiv:2510.23045.
Emanuel Todorov, Tom Erez, and Yuval Tassa. MuJoCo: A physics engine for model-based control.
In IEEE/RSJ International Conference on Intelligent Robots and Systems, pp. 5026–5033. IEEE,
2012. doi: 10.1109/IROS.2012.6386109.


Edan Toledo, Karen Hambardzumyan, Martin Josifoski, Rishi Hazra, Nicolas Baldwin, Alexis
Audran-Reiss, Michael Kuchnik, Despoina Magka, Minqi Jiang, Alisia Maria Lupidi, et al. Ai
research agents for machine learning: Search, exploration, and generalization in mle-bench. arXiv
preprint arXiv:2507.02554, 2025.
Brandon Trabucco, Xinyang Geng, Aviral Kumar, and Sergey Levine. Design-Bench: Benchmarks
for data-driven offline model-based optimization. In Proceedings of the 39th International Conference on Machine Learning, volume 162 of Proceedings of Machine Learning Research, pp. 21658–
21676. PMLR, 2022. URL https://proceedings.mlr.press/v162/trabucco22a.html.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and
Anima Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv
preprint arXiv:2305.16291, 2023.
Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan,
Yueqi Song, Bowen Li, Jaskirat Singh, et al. Openhands: An open platform for ai software
developers as generalist agents. International Conference on Learning Representations, 2025a.
Yifei Wang, Hancheng Ye, Yechen Xu, Cong Guo, Chiyue Wei, Qinsi Wang, Dongting Li, Tingjun
Chen, Hai Li, Danyang Zhuo, and Yiran Chen. Mars: Efficient, adaptive co-scheduling for
heterogeneous agentic systems. arXiv preprint arXiv:2604.26963, 2026.
Yiping Wang, Shao-Rong Su, Zhiyuan Zeng, Eva Xu, Liliang Ren, Xinyu Yang, Zeyi Huang,
Xuehai He, Luyao Ma, Baolin Peng, Hao Cheng, Pengcheng He, Weizhu Chen, Shuohang Wang,
Simon Shaolei Du, and Yelong Shen. Thetaevolve: Test-time learning on open problems. arXiv
preprint arXiv:2511.23473, 2025b.
Francis Rhys Ward, Teun van der Weij, Hanna Gábor, Sam Martin, Raja Mehta Moreno, Harel Lidar,
Louis Makower, Thomas Jodrell, and Lauren Robson. CTRL-ALT-DECEIT: Sabotage evaluations
for automated AI R&D. Advances in Neural Information Processing Systems, 2025.
Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou,
Guangshuai Wang, Zhiqiang Gao, Juntai Cao, Zijie Qiu, Ming Hu, Chenglong Ma, Shixiang Tang,
Junjun He, Chunfeng Song, Xuming He, Qiang Zhang, Chenyu You, Shuangjia Zheng, Ning Ding,
Wanli Ouyang, Nanqing Dong, Yu Cheng, Siqi Sun, Lei Bai, and Bowen Zhou. From AI for Science
to Agentic Science: A Survey on Autonomous Scientific Discovery, 2025. arXiv:2508.14111.
Amy Xin, Jiening Siow, Junjie Wang, Zijun Yao, Jian Song, Lei Hou, Juanzi Li, and Fanjin Zhang.
Eurekagent: Agent environment engineering is all you need for autonomous scientific discovery.
arXiv preprint arXiv:2606.13662, 2026.
Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune,
and David Ha. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic
Tree Search, 2025. arXiv:2504.08066.
Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V Le, Denny Zhou, and Xinyun
Chen. Large language models as optimizers. In The Twelfth International Conference on Learning
Representations, 2024.
Xu Yang, Xiao Yang, Shikai Fang, Yifei Zhang, Jian Wang, Bowen Xian, Qizheng Li, Jingyuan Li,
Minrui Xu, Yuante Li, Haoran Pan, Yuge Zhang, Weiqing Liu, Yelong Shen, Weizhu Chen, and
Jiang Bian. R&D-Agent: An LLM-agent framework towards autonomous data science. arXiv
preprint arXiv:2505.14738, 2025a.
Zhuo Yang, Daolang Wang, Lingli Ge, Beilun Wang, Tianfan Fu, and Yuqiang Li. Reasoning
bo: Enhancing bayesian optimization with long-context reasoning power of llms. arXiv preprint
arXiv:2505.12833, 2025b.
Jiaqi Yuan, Jialu Wang, Zihan Wang, Qingyun Sun, Ruijie Wang, and Jianxin Li. Agenticgeo: A
self-evolving agentic system for generative engine optimization. arXiv preprint arXiv:2603.20213,
2026.


Mario Zechner. Pi Coding Agent. npm software release, 2026. URL https://www.npmjs.com/
package/@earendil-works/pi-coding-agent/v/0.81.1. Version 0.81.1; accessed August
12, 2026.
Ruiyi Zhang, Peijia Qin, Qi Cao, Li Zhang, and Pengtao Xie. Aibuildai: An ai agent for automatically
building ai models. arXiv preprint arXiv:2604.14455, 2026a.
Tuo Zhang, Alin-Ionut Popa, Yan Xu, Rui Song, and Dimitrios Dimitriadis. Pivot: Bridging planning
and execution in llm agents via trajectory refinement. arXiv preprint arXiv:2605.11225, 2026b.
Yunxiang Zhang, Kang Zhou, Zhichao Xu, Kiran Ramnath, Yun Zhou, Sangmin Woo, Haibo Ding,
and Lin Lee Cheong. Learning to ideate for machine learning engineering agents. arXiv preprint
arXiv:2601.17596, 2026c.
Xinyu Zhu, Yuzhu Cai, Zexi Liu, Bingyang Zheng, Cheng Wang, Rui Ye, Jiaao Chen, Hanrui Wang,
Wei-Chen Wang, Yuzhi Zhang, Linfeng Zhang, Weinan E, Di Jin, and Siheng Chen. Toward
ultra-long-horizon agentic science: Cognitive accumulation for machine learning engineering.
arXiv preprint arXiv:2601.10402, 2026.


A

## A Implementation Details


### A.1 Context Construction and Interaction Pipeline

Within each research segment, ScienceFlow follows a standard reasoning–action–observation loop.
At the start of the segment, it assembles the model-facing context in a fixed order from a stable
prefix, the selected anchor state, and the ESTRA direction; segment-local interaction history is
then accumulated during tool use. Table A1 details these components and their update scopes,
complementing the context assembly defined in Section 2.3.4.
Table A1: Model-facing context components in assembly order. The first four components form
the cache-friendly prefix; subsequent components vary with the recoverable state or current research
segment.
Component

Contents

Update scope

Pworker
Pruntime
Ptools
Ptask

Generic research-worker and workspace-interaction policy
Runtime behavior, safety, and tool-use policy
Tool names, descriptions, argument schemas, and call policy
Objective, evaluator contract, budget envelope, task adapter,
and initial analysis guidance
Workspace view, folded or unfolded memory, validation evidence, and resource status for the selected anchor
Extend-or-redirect instruction selected by ESTRA
Reasoning outputs, tool calls, and compact observations

Worker lifecycle
Worker lifecycle
Worker lifecycle
Task run

Panchor (an )
Pdir (dn )
hv,j

Research segment
Research segment
Tool-use round

Initial segment. The initial segment combines the stable context Pstable with a compact view of
the initial workspace W0 . The task component specifies the objective, evaluator contract, resource
budget, and required artifact interface. For MLE-bench, the initial guidance prioritizes file and
modality inspection, leakage-safe validation, and a bounded baseline before expensive training. For
optimization tasks, it specifies the objective, constraints, evaluator, and candidate-solution contract.
These instructions define the initial inspection priorities, while subsequent actions remain selected
by the worker’s local policy.
Schematic context views for initial and subsequent segments
[stable prefix: P_stable]
worker: generic research-worker policy
runtime: execution and tool-use policy
tools:
read / search / edit / write / execute / inspect
task:
objective + evaluator + budget + artifact contract
[initial segment]
workspace_view: View(W_0)
instruction: inspect task -> analyze data -> build bounded baseline
[subsequent segment]
anchor:
current_state | archived_state
workspace_view: View(W(a_n))
memory_view:
Fold(m(a_n); B_mem) [+ optional Unfold(...)]
validation:
e(a_n)
resources:
l(a_n) + remaining budget B_t
direction:
extend | redirect
closed_branch: Fold(completed exploration)
[segment-local history: h_n,j]
reasoning -> tool action -> observation -> workspace update -> ...

Stage-gate and research-segment transitions. During forward research, a task-specific result
signal invokes the stage gate. The gate records a result card qv , snapshots the active workspace as
Wv , stores validation evidence ev and resource records ℓv , and inserts the resulting state sv into
the archive. The worker then resumes the current research segment, with the stage-gate exchange
excluded from its segment-local history.


A text-only response or context-capacity limit closes the current segment and invokes ESTRA to
select the next anchor an and direction dn . A current-state anchor retains the live workspace,
whereas an archived-state anchor restores the corresponding workspace exactly and folds the postanchor branch into completed evidence. The underlying result cards remain indexed and can later be
retrieved through Unfold.

Stable-prefix caching. The stable prefixPstable = Pworker ⊕ Pruntime ⊕ Ptools ⊕ Ptask is placed
before all anchor-specific and segment-local content. The worker policy, runtime instructions, and
tool schemas remain fixed over the worker lifecycle, while the task contract remains fixed within a
task run. Workspace views, memory, validation evidence, resource status, and ESTRA directions
are appended afterward and updated at research-segment boundaries. This ordering preserves a
common prefix across tool rounds and research segments. Backend-reported cache telemetry is
recorded when available, while cache availability does not alter the research-state transitions.


### A.2 ESTRA Decision and Re-Anchoring Pipeline

ESTRA, introduced in Section 2.3.3, jointly selects an execution anchor an and a research direction
dn at each research-segment boundary. The anchor determines whether the next research segment
retains the current workspace or restores an archived executable state, while the direction determines
whether research extends the selected route or redirects from it. When an archived anchor is selected,
exploration performed after that anchor is folded into completed evidence before the next research
segment begins.

Table A2: Evidence provided to ESTRA at a research-segment boundary. Optional components are
included only when corresponding records are available.
Component

Contents

Current state
Archived anchors

Active workspace summary, latest result card, and current validation evidence
Recoverable states with workspace summaries and associated validation evidence
Folded research history, recent result cards, and indexed evidence available
through Unfold
Optional validated scores and compact method summaries from other workers
Remaining wall-clock budget and current execution constraints

Memory view
Peer evidence
Resource envelope Bt

Decision prompt ESTRA evaluates candidate anchors using their validation evidence, recoverable
workspace contents, recent progress, failure history, peer evidence, and the remaining resource
budget. The validation metric is treated as one signal rather than the sole decision criterion, allowing
ESTRA to preserve promising but not yet leading routes or redirect from saturated ones. Tool use is
disabled during this deliberation, and the research worker returns one structured decision specifying
the anchor an , direction dn , supporting evidence, and intended search focus.


Schematic ESTRA decision contract
decision axes:
anchor
= current_state | archived_state
direction = extend | redirect
evidence:
current_state
archived_anchor_candidates
memory_view
validation_history
optional_peer_evidence
remaining_resource_budget
requirements:
select exactly one anchor and one direction
identify the current bottleneck
justify the decision using recorded evidence
specify the next search focus
structured output:
anchor, target_state, direction,
bottleneck, supporting_evidence,
decision_reason, next_search_focus

Folding and segment initialization. At a research-segment boundary, Fold summarizes the completed exploration as historical evidence for the next research segment. If ESTRA selects the current
state, ScienceFlow retains the active workspace and folds the research segment that just ended. If
it selects an archived state, ScienceFlow restores the corresponding workspace snapshot and folds
the post-anchor branch that is no longer active. The original result cards and archived states remain preserved and addressable. ScienceFlow then applies Assemble to combine the stable prefix,
selected-anchor context, ESTRA direction, and optional peer evidence into Pn+1 .
Schematic ESTRA folding and segment initialization
[completed exploration]
terminal_state: Syy
selected_anchor: current_state | archived_state Sxx
direction: extend | redirect
folded_evidence:
methods attempted
validated outcomes
observed failures
avoid-repeat guidance
[next segment]
stable_prefix: P_stable
workspace: current workspace | Restore(W(Sxx))
anchor_context:
memory view
validation evidence
resource records
workspace view
direction_context: extend | redirect
optional_context: peer evidence
local_history: empty

The anchor and direction axes yield four ESTRA outcomes: extending or redirecting from either the
current state or an archived state. Exact workspace restoration is required only when an archived
anchor is selected. Appendix D.3 presents a recorded archived-anchor transition and its folded
post-anchor branch, while Appendix D.4 presents a KTTSP research-segment boundary at which
peer evidence is included in the ESTRA context before a subsequent redirect.


B

## B MLE-bench Supplementary Results


### B.1 Evaluation on the Full MLE-bench Set

We report per-task results on all 75 MLE-bench competitions, grouped by the official Lite, Medium,
and High complexity splits. Each Score is the mean task-specific benchmark score over three
independent runs. Because evaluation metrics differ across competitions, these raw scores should
not be compared across tasks.
A checkmark in Any-Medal indicates that at least one of the three runs reached a bronze, silver,
or gold threshold. For each run, Cost($) is the cumulative LLM/API expenditure up to the first
medal-producing result; if no medal is obtained, it is the total expenditure over the complete run.
The reported cost is averaged over the three runs and excludes accelerator infrastructure costs. First
Medal Time (h) is averaged only over medal-producing runs and is reported as “–” when no run
earns a medal. A value of 0 in GPUs denotes CPU-only execution. All runs use DeepSeek-V4Flash-Preview as the research-worker backbone.
The per-task Any-Medal indicator reports the best observed outcome across runs and is therefore
descriptive. It differs from Table 1, which computes the medal rate independently for each run and
reports mean ± SEM across three runs. Collapsing the archive by competition yields 54 of 75 tasks
(72.0%) with at least one medal: 22 gold, 17 silver, and 15 bronze.
Four-hour archival cutoff. The Time dimension in Figure 1b uses archived first-medal timestamps
to characterize continued progress beyond a short horizon. By the four-hour cutoff, 35 of 75 tasks
(46.67%) had a documented medal-producing result; the final archive contains at least one medal
for 54 tasks. The four-hour value is a descriptive best-observed cutoff reconstructed from available
task logs, rather than the mean of three independent four-hour evaluations. It should therefore be
interpreted as trajectory evidence that additional tasks continue to reach medal quality after four
hours, not as a compute-normalized comparison or a causal estimate of any individual ScienceFlow
mechanism. The full-setting endpoint shown in the profile follows the headline three-run 24-hour
result of 70.22 ± 1.18%.
Official-leaderboard entries below follow the public MLE-bench leaderboard (OpenAI, 2026b);
available system papers are cited alongside the corresponding agent names.

### B.2 Operational Telemetry Coverage

All 75 tasks are included in the performance evaluation under the same ScienceFlow protocol. The
operational analysis is retrospective and requires both ESTRA-event records and checkpoint/snapshot
telemetry. Both streams are available for 54 tasks; the remaining 21 tasks retain benchmark outcomes
but lack complete mechanism-level records. The smaller denominator therefore reflects telemetry
availability rather than task selection or a different system configuration. These records support the
mechanism analysis in Table 2.


Table A3: Full-set MLE-bench Any-Medal results. Values are percentages reported as mean ± SEM
over three runs. Baseline results retain their published reporting protocols. Systems are grouped by
source, and the best result in each column is bolded.
Lite
(%)

Medium
(%)

High
(%)

All
(%)

DeepSeek-V4-Flash-Preview

80.30 ± 1.52

74.56 ± 0.88

44.44 ± 2.22

70.22 ± 1.18

Claude-Opus-4.6
Gemini-3.1-Pro-Preview

80.30 ± 1.50
80.30 ± 1.50

64.00 ± 0.90
64.00 ± 0.90

44.40 ± 2.20
46.70 ± 0.00

64.90 ± 0.40
65.30 ± 0.80

Gemini-3-Pro-Preview

80.30 ± 1.52

64.04 ± 2.32

42.22 ± 2.22

64.44 ± 1.18

Claude-Opus-4.6

77.27 ± 0.00

61.40 ± 0.88

46.67 ± 0.00

63.11 ± 0.44

Gemini-3-Pro-Preview

78.79 ± 1.52

60.53 ± 1.52

44.44 ± 2.22

62.67 ± 0.77

Gemini-3-Pro-Preview
Gemini-3-Pro-Preview3
Gemini-2.5-Pro
DeepSeek-V3.2-Speciale

80.30 ± 1.52
80.30 ± 1.522
75.76 ± 1.52
75.76 ± 1.51

57.89 ± 1.52
58.77 ± 0.882
57.89 ± 1.52
50.88 ± 3.51

42.22 ± 2.22
40.00 ± 0.002
40.00 ± 0.00
42.22 ± 2.22

61.33 ± 1.33
61.33 ± 0.772
59.56 ± 0.89
56.44 ± 2.47

Gemini-3-Pro-Preview
Gemini-3-Pro-Preview3
Gemini-3-Pro-Preview3

74.24 ± 1.52
74.24 ± 3.032
68.18 ± 2.622

52.63 ± 3.04
45.61 ± 0.882
44.74 ± 1.522

37.78 ± 2.22
35.55 ± 2.222
40.00 ± 0.002

56.00 ± 1.54
52.00 ± 0.772
50.67 ± 1.332

gpt-5-codex
Gemini-2.5-Pro

65.15 ± 1.52
68.18 ± 2.62

45.61 ± 7.18
34.21 ± 1.52

31.11 ± 2.22
33.33 ± 0.00

48.44 ± 3.64
44.00 ± 1.33

Gemini-2.5-Pro
gpt-5 (low verbosity/effort)1
Gemini-2.5-Pro
DeepSeek-R1

62.12 ± 1.52
63.64 ± 0.00
66.67 ± 1.52
62.12 ± 3.03

36.84 ± 1.52
33.33 ± 0.882
25.44 ± 0.88
26.32 ± 2.63

33.33 ± 0.00
20.00 ± 0.002
31.11 ± 2.22
24.44 ± 2.22

43.56 ± 0.89
39.56 ± 0.442
38.67 ± 0.77
36.44 ± 1.18

gpt-5

68.18 ± 2.62

21.05 ± 1.52

22.22 ± 2.22

35.11 ± 0.44

undisclosed

48.48 ± 1.52

29.82 ± 2.32

24.44 ± 2.22

34.22 ± 0.89

o3

55.00 ± 1.47

21.97 ± 1.17

21.67 ± 1.07

31.60 ± 0.82

o3 + GPT-4.1
DeepSeek-R1

51.52 ± 4.01
48.48 ± 1.52

19.30 ± 3.16
20.18 ± 2.32

26.67 ± 0.00
24.44 ± 2.22

30.22 ± 0.89
29.33 ± 0.77

o1-preview
o1-preview
gpt-4o-2024-08-06
claude-3-5-sonnet
gpt-4o-2024-08-06

48.18 ± 1.11
35.91 ± 1.86
18.55 ± 1.26
19.70 ± 1.52
12.12 ± 1.52

8.95 ± 1.05
8.45 ± 0.43
3.06 ± 0.33
2.63 ± 1.52
1.75 ± 0.88

18.67 ± 1.33
11.67 ± 1.27
8.15 ± 0.84
2.22 ± 2.22
2.22 ± 2.22

22.40 ± 0.50
17.12 ± 0.61
8.63 ± 0.54
7.56 ± 1.60
4.89 ± 0.44

llama-3.1-405b
gpt-4o-2024-08-06

10.23 ± 1.14
4.55 ± 0.86

0.66 ± 0.66
0.00 ± 0.00

0.00 ± 0.00
0.00 ± 0.00

3.33 ± 0.38
1.60 ± 0.27

Agent

LLM(s) used

ScienceFlow (Ours)5
Public study
Iris (Fu et al., 2026)4
MLEvolve (Du et al., 2026)6
Official leaderboard
Famou-Agent 2.0 (Li et al.,
2025)
AIBuildAI (Zhang et al.,
2026a)
CAIR MARS+ (Chen et al.,
2026b)
MLEvolve4
PiEvolve (Botla et al., 2025)
Famou-Agent 2.0
ML-Master 2.0 (Zhu et al.,
2026)
CAIR MARS
PiEvolve4
Leeroo (Nadafian et al.,
2026)
Thesis
CAIR
MLE-STAR-Pro-1.5 (Nam
et al., 2025)
Famou-Agent
Operand ensemble
CAIR MLE-STAR-Pro-1.04
InternAgent (InternAgent
Team, 2025)4
R&D-Agent (Yang et al.,
2025a)4
Neo (HeyNeo Team, 2025)
multi-agent4
AIRA-dojo (Toledo et al.,
2025)
R&D-Agent
ML-Master (Liu et al.,
2025)4
R&D-Agent
AIDE (Jiang et al., 2025)
AIDE
AIDE
OpenHands (Wang et al.,
2025a)
AIDE
MLAB

Uses light assistance from Gemini-2.5-Pro, Grok-4, and Claude 4.1 Opus, distilled by Gemini-2.5-Pro.
For incomplete three-run evaluations, missing runs are counted as Any-Medal failures when computing the reported mean and SEM.
Uses Gemini-3-Pro-Preview primarily, with selected modules using GPT-5 and GPT-5-mini.
Uses a reported 12 h or 36 h per-task budget rather than the standard 24 h budget; the exact setting follows the cited source.
ScienceFlow evaluates tensorflow-speech-recognition-challenge using the corrected setup from MLE-bench issue #63; baseline
aggregates are retained as reported.
MLEvolve with Gemini-3.1-Pro-Preview uses a 12 h per-task budget.


Table A4: Per-task results on the 22-task MLE-bench Lite split. Field definitions follow Section B.1.
Competition Name

Year

Score

Cost($)

GPUs

Any-Medal

First Medal
Time (h)

detecting-insults-in-social-commentary
the-icml-2013-whale-challenge-right-whale-redux
mlsp-2013-birds
random-acts-of-pizza
denoising-dirty-documents
text-normalization-challenge-russian-language
dogs-vs-cats-redux-kernels-edition
spooky-author-identification
text-normalization-challenge-english-language
leaf-classification
jigsaw-toxic-comment-classification-challenge
new-york-city-taxi-fare-prediction
nomad2018-predict-transparent-conductors
dog-breed-identification
aerial-cactus-identification
aptos2019-blindness-detection
histopathologic-cancer-detection
siim-isic-melanoma-classification
plant-pathology-2020-fgvc7
ranzcr-clip-catheter-line-classification
tabular-playground-series-dec-2021
tabular-playground-series-may-2022

2012
2013
2013
2015
2015
2017
2017
2017
2017
2017
2018
2018
2018
2018
2019
2019
2019
2020
2020
2021
2021
2022

0.9588
0.9486
0.9099
0.7713
0.0116
0.9791
0.0150
0.2800
0.9965
0.0121
0.9865
4.8527
0.0550
0.3525
1.0000
0.9204
0.9970
0.9353
0.9928
0.9124
0.9622
0.9882

0.0618
1.4995
0.1483
1.0641
0.0141
0.3177
0.0150
0.2299
0.1472
0.0603
0.1521
0.2986
0.1805
0.5283
0.2885
0.3543
0.0214
1.9233
0.0283
0.2221
0.0106
0.5283


✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
-

2.54
0.12
1.95
0.35
1.08
1.35
0.48
3.66
1.59
5.76
2.93
0.09
2.11
4.84
1.07
11.98
0.46
0.42
-


Table A5: Per-task results on the 38-task MLE-bench Medium split. Field definitions follow
Section B.1.
Competition Name

Year

Score

Cost($)

GPUs

Any-Medal

First Medal
Time (h)

AI4Code
alaska2-image-steganalysis
billion-word-imputation
cassava-leaf-disease-classification
cdiscount-image-classification-challenge
chaii-hindi-and-tamil-question-answering
champs-scalar-coupling
facebook-recruiting-iii-keyword-extraction
freesound-audio-tagging-2019
google-quest-challenge
h-and-m-personalized-fashion-recommendations
herbarium-2020-fgvc7
herbarium-2021-fgvc8
herbarium-2022-fgvc9
hotel-id-2021-fgvc8
hubmap-kidney-segmentation
icecube-neutrinos-in-deep-ice
imet-2020-fgvc7
inaturalist-2019-fgvc6
iwildcam-2020-fgvc7
jigsaw-unintended-bias-in-toxicity-classification
kuzushiji-recognition
learning-agency-lab-automated-essay-scoring-2
lmsys-chatbot-arena
multi-modal-gesture-recognition
osic-pulmonary-fibrosis-progression
petfinder-pawpularity-score
plant-pathology-2021-fgvc8
seti-breakthrough-listen
statoil-iceberg-classifier-challenge
tensorflow-speech-recognition-challenge
tensorflow2-question-answering
tgs-salt-identification-challenge
tweet-sentiment-extraction
us-patent-phrase-to-phrase-matching
uw-madison-gi-tract-image-segmentation
ventilator-pressure-prediction
whale-categorization-playground

2022
2020
2014
2021
2017
2021
2019
2013
2019
2020
2022
2020
2021
2022
2021
2021
2023
2020
2019
2020
2019
2019
2024
2024
2013
2020
2022
2021
2021
2018
2018
2020
2018
2020
2022
2022
2021
2018

0.7911
0.8992
4.4668
0.8995
0.7248
0.7458
0.6758
0.5037
0.7346
0.3806
0.0248
0.4146
0.1656
0.6994
0.1116
0.9681
1.3585
0.6544
0.2972
0.7329
0.8494
0.9527
0.8355
1.0010
0.2177
-6.7620
16.9877
0.9072
0.8002
0.1349
0.9841
0.5691
0.7704
0.7178
0.8707
0.6902
0.3384
0.4783

1.6478
1.6478
0.1794
0.3477
0.4307
0.0056
0.4361
1.6478
0.2054
0.1189
0.0309
0.1594
0.4524
0.2894
0.1905
0.0891
0.2270
0.6925
0.2171
0.1496
0.3405
0.0462
0.6734
0.4159
0.1462
1.5486
0.9553
0.1213
2.1684
3.0067
1.2587
0.1996
1.1963
0.8099
0.4126
2.4634
0.5535
0.8077


✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

22.27
7.87
11.77
23.04
6.11
2.04
1.05
10.20
2.97
4.06
6.88
2.57
0.45
22.33
3.49
2.63
3.01
1.27
9.55
7.96
11.87
12.03
1.42
6.25
23.42
1.52
11.80
4.01
3.70

Table A6: Per-task results on the 15-task MLE-bench High split. Field definitions follow Section B.1.
Competition Name

Year

Score

Cost($)

GPUs

Any-Medal

First Medal
Time (h)

3d-object-detection-for-autonomous-vehicles
bms-molecular-translation
google-research-identify-contrails-reduce-global-warming
hms-harmful-brain-activity-classification
iwildcam-2019-fgvc6
nfl-player-contact-detection
predict-volcanic-eruptions-ingv-oe
rsna-2022-cervical-spine-fracture-detection
rsna-breast-cancer-detection
rsna-miccai-brain-tumor-radiogenomic-classification
siim-covid19-detection
smartphone-decimeter-2022
stanford-covid-vaccine
vesuvius-challenge-ink-detection
vinbigdata-chest-xray-abnormalities-detection

2019
2021
2023
2024
2019
2023
2021
2022
2023
2021
2021
2022
2020
2023
2021

0.0597
4.8469
0.4474
0.8100
0.2107
0.6585
3,068,390.3330
0.5613
0.1225
0.6163
0.4527
4.6753
0.2272
0.1415
0.3344

0.1874
1.0800
4.1043
4.1043
0.1442
4.1043
2.8259
4.1043
4.1043
4.4492
4.1043
4.1043
0.0580
4.1043
0.4418


✓
✓
✓
✓
✓
✓
✓

1.73
0.68
1.63
4.57
0.59
0.07
1.43


C

## C Mathematical Optimization Details


### C.1 Formal Task Definitions

Circle packing. For n = 26, a candidate consists of circle centers pi = (xi , yi ) ∈ [0, 1]2 and radii
ri ≥ 0. The task is
max26

{pi ,ri }i=1

X

ri

subject to

ri ≤ xi , yi ≤ 1 − ri ,

∥pi − pj ∥2 ≥ ri + rj

(i ̸= j).

(A1)

i=1

The first constraint keeps every circle inside the unit square, and the second prevents pairwise overlap.
The reported score is the sum of radii of a feasible configuration, so larger values are better (Novikov
et al., 2025).
Ratio minimization.
Define

A candidate is a set of n = 16 distinct points P = {p1 , . . . , p16 } ⊂ R2 .

dmin (P ) = min∥pi − pj ∥2 ,
i<j

dmax (P ) = max∥pi − pj ∥2 .

(A2)

dmax (P )
.
dmin (P )

(A3)

i<j

The objective is
min

ρ(P ),

ρ(P ) =

P : dmin (P )>0

The objective is invariant to translation, rotation, and uniform scaling. AlphaEvolve defines the
objective as ρ(P ) but follows the source packing tables in reporting ρ(P )2 (Novikov et al., 2025). To
match Table 3, we take the positive square root of such published values and report ρ(P ) for every
method; lower values are better.
Uncertainty inequality. For an integrable real-valued function f : R → R, let
Z
fb(ξ) =
f (x)e−2πixξ dx,
A(f ) = inf{r > 0 : f (x) ≥ 0 for all |x| ≥ r}.

(A4)

R

For nonzero even functions satisfying max{f (0), fb(0)} < 0 and having finite A(f ) and A(fb), the
Fourier sign-uncertainty constant is
C4 = inf A(f )A(fb).
f

(A5)

Our benchmark follows the first, Hermite-polynomial formulation used by Novikov et al. (2025),
which refines the construction of Gonçalves et al. (2017). It searches over
Qc (z) =

m
X

ck H4k (z),

√
fc (x) = Qc ( 2π x)e−πx ,

(A6)

k=0

where Hj is the physicists’ Hermite polynomial. The degrees 4k make fc invariant under the Fourier
transform. As in the official AlphaEvolve verifier, the final coefficient is chosen so that Qc (0) = 0,
and the polynomial is oriented to be positive at infinity. After removing the resulting factor z 2 , let
rmax be the largest positive real root across which Qc (z)/z 2 changes sign. The evaluator returns
rmax
,
C4 ≤ U (c).
(A7)
2π
Thus the reported score is the verified Hermite-construction upper bound on C4 , and lower values are
better. This benchmark does not include the separate Laguerre-polynomial refinement also discussed
by AlphaEvolve.

U (c) =


### C.2 Evaluation and Feasibility Audit

ScienceFlow candidates are re-evaluated from the JSON artifacts stored in immutable workspace
snapshots rather than from rounded stage-ledger metrics. The audit parses the saved decimal literals,


verifies the task-specific structure and feasibility conditions, and recomputes the displayed objective.
Unreadable artifacts, malformed candidates, and candidates that fail the corresponding feasibility
test are excluded from comparison.
Circle packing. The strict audit treats every saved coordinate and radius as an exact decimal rational
and applies the inequalities in Equation A1 with zero numerical tolerance. It records the minimum
boundary slack and the minimum squared pairwise slack. For a candidate with a small negative
slack, we also compute the smallest
common radius reduction δ ≥ 0 that makes its fixed centers
P
feasible; the repaired score is i ri − 26δ. This repair is used only to produce a conservative feasible
score and never to improve a candidate. The artifact underlying the reported value 2.6359830849
requires δ = 9.26 × 10−15 and yields the strictly feasible score 2.63598308491745569, which is
unchanged at the precision shown in Table 3.
Ratio minimization. The audit parses coordinates with 60-digit decimal precision, requires exactly
16 two-dimensional points, recomputes all 120 pairwise Euclidean distances, and rejects a candidate
when dmin = 0. It then evaluates dmax /dmin directly, avoiding the six-decimal inverse-squared
metric stored in the stage ledger. The best audited DeepSeek-V4-Flash-Preview candidate gives
3.590157365310609, while the best openPangu-2.0-Pro candidate gives 3.590157365325370478.
Both values are reported as the unsquared ratio dmax /dmin .
Uncertainty inequality. We reconstruct the public AlphaEvolve B.4 Hermite verifier exactly. The
audit enforces Qc (0) = 0 and a positive limit at infinity, divides out the factor z 2 , computes the
real roots symbolically, and selects the largest positive sign-changing root using 200-digit root
approximations. The resulting bound is evaluated by Equation A7. The reported ScienceFlow
bounds 0.348200107555 and 0.343293122432 both pass this verifier.
Baseline provenance. Published entries in Table 3 are transcribed from their cited papers or
released repositories and retain the construction and precision reported by those sources; they are not
presented as independent reruns. The AlphaEvolve uncertainty entry is independently reproduced
with its public Hermite verifier. OpenEvolve is run locally as described in Section 3.2.1; its retained
scores come from the local task evaluator. In particular, its circle-packing output does not preserve
the final evaluated coordinates for a separate exact-decimal audit. The local paper archive contains
the derived audit summaries used here; some corresponding raw run artifacts remain in the original
experiment storage and are not duplicated in the paper repository.

D

## D SpOC4-KTTSP Supplementary Details


### D.1 Competition, Tracks, and Evaluation Protocol

SpOC4 is the fourth Space Optimisation Competition organized by ESA’s Advanced Concepts Team.
Its Keplerian Tomato Traveling Salesperson Problem asks a spacecraft to collect all targets in lunar
orbit in minimum mission time while respecting orbital-transfer and maneuverability constraints
(European Space Agency, Advanced Concepts Team, 2026). We evaluate the three official instances.
The easy, medium, and hard tracks contain 50, 182, and 1,052 targets, respectively; their minimum
transfer times are 0.001, 0.01, and 1/1440 days, and their maximum mission durations are 200, 500,
and 3,000 days.
For an N -target instance, a submission contains a permutation of all targets, N − 1 departure epochs,
and N − 1 transfer durations. The evaluator checks the permutation, time bounds, and chronological
consistency before solving each transfer with a Lambert solver in both directions and with at most
20 revolutions. A nominal leg may use at most 100 m s−1 of ∆V ; at most five exception legs may
exceed this threshold, and no leg may exceed 600 m s−1 . The score is the arrival time at the final
target in days, so lower is better. Candidates are serialized as an official-format JSON decision vector,
and invalid candidates receive no score.
Trajectory evaluation is CPU-only. The easy and medium results were obtained through staged continuation runs, whereas KTTSP-hard used the separate ten-day campaign described in Section 3.2.2,
with DeepSeek-V4-Pro-Preview, DeepSeek-V4-Flash-Preview, and GLM-5.1. Because resumed


stages and worker counts differed across tracks, we report the public leaderboard outcomes without
treating them as a compute-normalized comparison.

### D.2 Context-Folding Trace on KTTSP-hard

This section instantiates the memory operations in Section 2.3.4 with a recorded W01 checkpoint
from the KTTSP-hard run. At S115, the append-only stage ledger mv contained 115 result cards
and occupied 73,964 characters. When the memory view exceeded Bmem , Fold compressed cards
e v occupied 4,661
S01--S112 into the addressable summary L S01 S112. The resulting view m
characters, a 93.7% reduction relative to the raw ledger. At the same research-segment boundary,
the runtime emitted a 6,773-character memory-bearing state packet for the next research segment.
This telemetry covers the folded view and associated state metadata, rather than the complete context
Pn+1 ; the stable prefix, resource provenance, workspace view, and direction instruction are composed
during final context assembly.
Before context folding: persistent ledger. The memory mv keeps each stage as an independently
addressable result card in .run results.md. The excerpts below reproduce selected fields from
three decision-critical cards; line wrapping is added only for page layout. The validity field
denotes ScienceFlow’s internal evidence tier, not the KTTSP track difficulty or the official feasibility
decision. The initial feasible result, an unverified intermediate attempt, and the best validated result
are all retained rather than keeping improvements alone.
Selected fields from stage cards before context folding
S01 metric=1928.39350319; validity=medium
BRIEF: Bridge strategy achieves 0 infeasible transfers with
4 exceptions and 1928.39d duration.
WHY: First fully feasible candidate.
S18 metric=1761.93330934; validity=low
NOTE: invalid_submission: no submission artifact found.
BRIEF: Finer local-window timing refinement reached 1761.93d.
WHY: Timing resolution helped, but the result was not eligible
as a verified comparable entry.
S112 metric=393.229; validity=high
BRIEF: Forward-pass timing refinement improved 696 legs and
saved 7.70d locally, but yielded only 0.001d net gain.
WHY: Five frozen exception legs absorbed the upstream savings;
further progress requires re-timing or re-routing them.
FILES: code=refine_timing_fast.py

After context folding: budgeted view. In m
e v , the historical portion is replaced by a compact
summary with an addressable identifier, while cards needed for verification and immediate continuation remain raw. The generated summary records the folded range, its best stage, representative
early evidence, the number of omitted intermediate cards, and the last folded stage:
Folded stage-memory view
Historical summary: L_S01_S112 [S01--S112]
best_stage=S112
- S01: metric=1928.39350319; validity=medium; first feasible
- S02: metric=1928.39350319; validity=medium; safe baseline
- S03: metric=1928.39350319; validity=high; validated baseline
- S04: metric=1891.24195011; validity=medium; timing re-opt
... 107 intermediate stages summarized ...
- S112: metric=393.229; validity=high;
frozen exception legs block the timing cascade
key_stage_index: S112=best_valid
available_expand_id: L_S01_S112
verification_raw_cards: S01, S18, S112
current_raw_segment: S113, S114, S115

Active review through unfolding. The runtime field available expand id exposes the identifier
used by the formal Unfold operation. The following view illustrates an active comparison of the


unverified timing attempt and the best validated route. This is an observed Unfold event from the
archived W01 runtime trace, shown using the corresponding indexed cards:
On-demand unfolded memory view
request: Unfold(L_S01_S112, stages={S18, S112})
index:
L_S01_S112 -> .run_results.md [S01--S112]
returned_raw_cards:
- S18: metric=1761.93330934; validity=low
NOTE: invalid_submission: no submission artifact found
BRIEF: Finer local-window timing refinement reached 1761.93d.
WHY: Timing resolution helped, but the result was not eligible
as a verified comparable entry.
- S112: metric=393.229; validity=high
BRIEF: Forward-pass timing refinement improved 696 legs and
saved 7.70d locally, but yielded only 0.001d net gain.
WHY: Five frozen exception legs absorbed the upstream savings;
further progress requires re-timing or re-routing them.
FILES: code=refine_timing_fast.py
context_effect: temporary augmentation of folded view
ledger_effect: none (m_v remains append-only)

The index resolves the request to the original cards in .run results.md. In the implementation,
this runtime-executed Unfold is realized through indexed workspace reads rather than a separate
memory service.

### D.3 ESTRA-Triggered Folding Trace on KTTSP-hard

This section instantiates the ESTRA-triggered fold in Sections 2.3.3 and 2.3.4 with a recorded
W01 transition. At 17:17 UTC on June 21, at a research-segment boundary caused by the context
limit, the worker selected the runtime action switch stage, moving from terminal stage S27 to
the archived anchor at S23. The transition folded the post-anchor branch S24--S27 into an 845character summary and assembled a 3,583-character state packet for the restored trajectory. Unlike
capacity-based folding of the persistent memory view, this fold scope was determined by the selected
archived anchor: it closes the abandoned branch and carries its diagnosis into the next research
segment.
Before ESTRA-triggered folding: abandoned tail. The four cards refer to the same 1746.8935day artifact, and no new route is produced. Their internal evidence tiers vary because the repeated
evaluations provide different amounts of verification evidence; this variation does not indicate
different outcomes under the official KTTSP feasibility checks:
Selected fields from abandoned-tail cards
S24 metric=1746.89350787; validity=medium
BRIEF: Existing artifact re-scored end-to-end with pykep;
1046 feasible, 4 exceptions, 0 infeasible.
S25 metric=1746.89350787; validity=high
BRIEF: Direct pykep recomputation validates the artifact before
route-ordering experiments.
S26 metric=1746.89350787; validity=medium
BRIEF: Baseline survives the transition but remains far behind peer W00.
WHY: Timing-only refinement is exhausted on the sorted route.
S27 metric=1746.89350787; validity=medium
WHY: Route ordering is the dominant bottleneck; the next route
should use proxy-prefiltered construction and bounded checks.

After ESTRA-triggered folding: restored-state evidence. The generated summary preserves
the branch-level conclusion rather than carrying all four cards verbatim into the next segment’s
agent-facing state packet:


ESTRA-folded abandoned-tail view
runtime_action: switch_stage
restore: terminal S27 -> target S23
fold_scope: abandoned tail S24--S27
tail_summary:
- Repeated pykep rescoring only revalidated the existing 1746.89d
artifact; no new candidate was produced.
- Validity fluctuated between medium and high on the same artifact;
treat the repeated rescoring as non-informative.
- Timing-only refinement on the sorted route is saturated.
- The 1746.89d baseline remains far behind W00 at 521.91d;
route-ordering or structural changes are required.
- Avoid redundant validation passes and further timing polish
without a new ordering or construction strategy.
summary_chars: 845
restored_state_packet_chars: 3583
preserved: raw cards, snapshot, logs, terminal archive

After restoration, the worker resumes from the executable workspace snapshot at S23, while the
folded S24--S27 branch is retained as completed negative evidence. The original cards remain
addressable in the archived memory through Unfold. Thus, the ESTRA-triggered fold changes the
active research route and agent-facing context without altering the persistent research record.


### D.4 Peer-Guided Search Trace on KTTSP-hard

The W01 trajectory in Figure 7 contains a concrete cross-worker coordination episode. W00
established an early validated solution of 521.9054 mission days at S60, while W01 remained
at 1746.8935 days. Each worker maintained an isolated executable workspace, and no artifact or
workspace state was transferred between them. Instead, compact peer evidence comprising W00’s
validated score and method summary entered W01’s ESTRA context. The worker used this evidence
to redirect its search from timing-only refinement toward route-ordering strategies.
The archived runtime records preserve both the peer-evidence payload and the resulting direction
instruction. We identify each archived ESTRA decision by its worker and stage as ESTRA-Wxx-Syy.
At W01’s S25 research-segment boundary, compact peer evidence comprising W00’s validated score
and a brief windowed-2-opt summary entered the worker’s ESTRA decision (event ESTRA-W01-S25).
The worker used the performance gap to diagnose route ordering as the bottleneck, but redirected
toward its own proxy-prefiltered nearest-neighbor construction rather than copying W00’s procedure.
PyKEP supplies the Lambert-transfer evaluation.
Selected fields from ESTRA-W01-S25
Route order is the bottleneck not timing; need faster NN using
orbital-element proxy pre-filter then pykep verify only top-3,
not full grid on 30 candidates.
Bottleneck: Route ordering is the dominant factor: 1746d vs peer
521d, but greedy NN with pykep evaluation is too slow to complete
within resource limits.
Exploration summary: Timing refinement on original sorted route
converged at 1746.89d; greedy NN route rewrite attempted but too
slow at 47s/10 legs. Peer at 521.91d via windowed 2-opt.
Redirect: Proxy-pre-filtered NN: rank by orbital distance,
pykep-verify only top 3-5 with coarse grid.

After several route-ordering attempts, W01 reached 1321.8824 days but still trailed W00 by approximately 802 days. At S79, the peer summary provided more explicit method-level evidence,
producing a second redirect at the operator level (event ESTRA-W01-S79).


Selected fields from ESTRA-W01-S79
Worker decision: Adapt the peer-validated 2-opt+SLSQP operators;
inclination-bin sorting appears saturated.
Bottleneck: Static inclination-bin sorting cannot match W00's
route-reordering and timing-optimization strategy (519 days).
Evidence: An approximately 802-day gap remains; finer bins improve
the objective by only 54 days, while greedy variants remain infeasible.
Next action: Apply 2-opt route swaps and SLSQP timing refinement
to W01's 1321.8824-day incumbent.

Table A7: Validated checkpoints and ESTRA decisions in the KTTSP-hard peer-guided overtaking
case. Mission duration is measured in days; lower is better.
Time (UTC)

Worker

Stage

Duration

Search event

Jun 21 16:12
Jun 21 16:20
Jun 25 18:04
Jun 25 19:12
Jun 25 23:01
Jun 26 00:00
Jun 26 07:29
Jun 27 00:06
Jun 28 23:29

W00
W01
W01
W01
W01
W01
W01
W01
W01

S60
S25
S78
S79
S80
S85
S97
S110
S112

521.9054
1746.8935
1321.8824
1321.8824
573.0305
525.9948
420.2742
393.2352
393.229

Early peer best
Structural ESTRA redirect
Fine inclination bins
Operator-level ESTRA redirect
Phase-greedy narrow bins
Near peer best
First validated lead over W00
Ultrafine timing grid
Final refinement

Between the first peer-aware ESTRA decision at S25 and its first validated lead over W00 at S97,
W01 reduced its incumbent from 1746.8935 to 420.2742 days, a 75.9% improvement over 4 days
and 15 hours. More directly, W01 produced the 420.2742-day result within 12 hours and 17 minutes
of the operator-level redirect at S79. It ultimately reached 393.229 days, outperforming W00’s final
validated 519.6255-day result by 24.32%.
The trace supports peer-guided adaptation rather than direct solution reuse. Applying windowed
SLSQP to W01’s existing route at S94 improved the objective by only 0.02 days. W01 established the
subsequent lead after combining a 10-degree inclination-bin route with phase-proximal construction
and finer timing grids. Peer evidence therefore served as search guidance: it revealed the structural
limitations of the current route family and identified promising operators, while W01 independently
instantiated and validated a distinct route and schedule.


E

## E SciModelingBench Provenance and Evaluation Metadata

This appendix records the data sources and hidden evaluation boundary for the 12 SciModelingBench tasks in
Section 3.3. We use the public SciModelingBench 0.10.0 release and its released dataset. In Table A8, N is the
number of candidates in each submission, K is the summary size used by the shared diagnostics, and Q is the
total query limit for one system–task pair. ScienceFlow’s two workers split this limit. The external baselines are
OpenCode 1.18.4 (OpenCode Contributors, 2026), Pi 0.81.1 (Zechner, 2026), Codex 0.144.5 (OpenAI, 2026a),
and Claude Code 2.1.72 (Anthropic, 2026). All four use DeepSeek-V4-Flash-Preview through non-interactive
clients.

Table A8: SciModelingBench task metadata. Visible scale describes the data given to the agent;
evaluation scale describes the exact reference domain or label-hidden pool. Values in parentheses are
canonical candidates represented by row-level observations. DrugMatrix contains six endpoint tasks
from one study collection. BKM, NE, and NDCG denote best-K mean, normalized enrichment, and
global NDCG. Data terms come from the original source, while the Hopper row separately identifies
simulator software licenses.
Task group

Visible

Evaluation

N/K/Q Trusted evaluator

Source / terms

TFBind8
BBO

32,768 sequences

65,536
sequences

32/5/20

PBM/UniPROBE (Barrera et al., 2016;
Hume et al., 2015); source-specific
academic-use terms

410 sequences

128/16/20 Four-replicate affinity posterior; BET-seq (Le et al., 2018; Fordyce Lab,
NE
2018); CC BY 4.0

Normalized PBM E-score
lookup; BKM

TFBind10 Pho4
2,087,323 rows
BBO
(524,300 seq.)
Superconductor
16,795 records
ranking
(12,179 groups)
UTR MRL
76,877 50-mers
ranking

2,985 groups

32/5/20

5,043 50-mers

128/16/10 Two-replicate mean ribosome
load; NE

GEO
GSE114002/mRNABench (Sample
et al., 2018; 2019); terms unknown

GFP
ranking

41,372 proteins

10,343 proteins

128/16/20 Protein-level median log
brightness; NE

Sarkisyan Figshare (Bolotin, 2016;
Sarkisyan et al., 2016); CC BY 4.0

Hopper
Controller
ranking

1,920 policies

1,280 policies

32/5/10

Mean of 500 frozen Hopper-v5 Design-Bench policy assets (terms not
rollouts; NDCG
separately stated); Gymnasium (MIT),
MuJoCo (Apache-2.0) (Trabucco et al.,
2022; Todorov et al., 2012)

390 conditions

16/5/8

Absolute log treatment–control NIEHS CEBS DrugMatrix (National
deviation; NDCG
Toxicology Program (NTP), 2023);
terms unspecified

DrugMatrix (6)
9,442 animal rows
ranking

Median critical temperature by UCI Superconductivity
composition; NDCG
Data (Hamidieh, 2018b;a); CC BY 4.0

Reconstruction principle SciModelingBench takes its scientific settings from Design-Bench (Trabucco
et al., 2022), but does not automatically treat the packaged arrays as ground truth. For every retained setting, we
return to the original experiment or simulator assets. We then define the candidate identity, visible observations,
hidden reference data, and trusted objective separately. Agents may train predictive models to rank candidates,
but those predictions are not used as ground truth outside the training distribution. We omit settings that do not
support reproducible candidates and evaluation, rather than keep them only to match a historical learned oracle.

Transcription-factor binding For TFBind8, the original PBM table stores an 8-mer and its reverse
complement in separate columns that share one E-score. The historical preprocessing joins these columns,
producing 65,792 rows and duplicating the 256 reverse-complement palindromes. We remove only these exact
duplicates, keep non-palindromic reverse complements as distinct valid sequences, and verify that the result
contains all 48 8-mers exactly once. We also retain both the published and normalized E-score scales. The
resulting complete measured landscape supports direct lookup without a learned oracle.
For TFBind10 Pho4, the legacy table contains replicate-level binding estimates. The same 10-mer can therefore
have conflicting values, and using row order as a lookup rule silently selects one replicate. We rebuild the
task from four BET-seq bound/input count replicates. The lower-half observations expose the raw replicate
measurements, while a deterministic affinity posterior covers the complete 410 domain and is oriented so that
higher values are better. This keeps replicate disagreement visible instead of hiding it behind the final row.

Superconducting materials Design-Bench uses a fitted random forest to score arbitrary composition
vectors. Composition alone, however, omits crystal structure, phase, pressure, defects, and processing. The
source data also contain repeated compositions with different measured critical temperatures. We first realign


the two UCI tables and normalize the amounts of the 86 elements. We then group proportional formulas
under one canonical composition while retaining every measurement. The group median is the ranking target,
and the measurement range and dispersion remain visible to the agent. Evaluation is limited to the measured
high-temperature pool, so composition-only extrapolations are not treated as physical ground truth.

UTR and GFP sequence measurements The original UTR setting uses a learned ResNet to score
arbitrary sequences. We instead use the unique 50-nucleotide variable regions measured in the eGFP reporter
assay. We select the unmodified-RNA condition, use the mean ribosome load over two replicates, and hold out
one group defined by (uAUG presence, Kozak quality) as a finite measured pool.
For GFP, translating the legacy nucleotide rows produces 56,086 rows but only 51,715 unique proteins. Among
the 1,202 duplicated protein groups, 1,201 have conflicting labels, and the wild type alone appears 534 times.
We instead use the authors’ protein-level aggregate, verify the unique 237-residue sequences, and split the data
by protein identity before adding nucleotide and barcode observations. This prevents synonymous encodings of
the same protein from appearing on both sides of the split. Both tasks therefore evaluate measured candidates
rather than predictions from historical neural-network oracles.

Hopper controller relabeling We keep Design-Bench’s 3,200 policy vectors as candidates but replace
the historical labels, each of which came from a single return. Every policy is evaluated over 500 stochastic
episodes in Hopper-v5. Policies share the same reset-seed schedule but use separate action-noise seeds. The
released data include raw returns, episode lengths, termination flags, and uncertainty summaries; mean return is
the frozen target. From the offline observations, the agent ranks a held-out pool of higher-performing measured
policies. It cannot access the simulator, train PPO, or request online rollouts during the task.

DrugMatrix reconstruction The legacy ChEMBL arrays represent each condition only by a molecular
token, dropping its dose, duration, route, vehicle, study, sex, and animal-group context. Nearly every molecule
then maps to several endpoint labels, and a row-level split can place the same molecular identity on both sides.
We therefore rebuild the task from the NIEHS CEBS individual-animal clinical-pathology release instead of
reusing these arrays. We preserve the treatment context and controls, map chemical identity by strict name and
CASRN matching, and use ChEMBL only to link structures rather than supply endpoint labels.
Candidates are five-day treatments at the highest observed dose, with complete endpoints and controls matched
by study, duration, route, vehicle, and sex. We hide the treatment-animal rows for these candidates but keep
their matched controls and observations from other doses or times visible. All six tasks use the same candidate
conditions and rank them by the absolute log difference between the endpoint mean and the matched-control
mean. This score measures the size of a biological change, not drug safety or quality.

Protocol and metric audit Before running any agents, we fixed the lower-score thresholds, structured
holdouts, submission sizes, and primary metrics using source-data analyses and task-specific random, simple,
and cross-validated audits. These audits helped us avoid saturated metrics, distinguish strong submissions, and
keep the queried fraction small relative to the hidden domain. The choices were not based on ScienceFlow or
external-agent results. Here, an “exact” evaluator returns the same score whenever it is applied to the same
frozen data. The underlying experimental measurements may still contain noise.

Runtime leakage controls and contamination scope The agent workspace contains only the exported
observations, candidate view, manifest, task contract, and submission directory. Hidden labels, trusted objectives, evaluator caches, full dataset copies, and submission records stay outside the workspace, and external
network access is disabled. The evaluator returns one score for the full batch rather than a score for each
candidate. The harness separately records query use and the best valid artifact. These controls block runtime
answer lookup through the benchmark infrastructure.
They do not show that public papers or upstream data were absent from model pretraining. We therefore
claim runtime leakage controls and audited provenance, not a contamination-free evaluation. General scientific
knowledge is allowed, although in some cases it is difficult to distinguish inference from memorized candidate
labels.

Licensing and availability SciModelingBench and Design-Bench software use the MIT license, but this
does not relicense the underlying experimental data. Table A8 therefore lists the original source-specific, CC
BY 4.0, or unknown data terms. Because these terms differ, the dataset card lists the license as “other” rather
than assigning one license to the full collection. Processing records and task-specific details are available in the
public suite documentation and dataset card.
