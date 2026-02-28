---
source: https://arxiv.org/abs/2511.09030
captured: 2026-02-26
capture: pdf-read
type: academic-paper
---

# Solving a Million-Step LLM Task with Zero Errors

Author: Elliot Meyerson, Giuseppe Paolo, Roberto Dailey, Hormoz Shahrzad, Olivier Francon, Conor F. Hayes, Xin Qiu, Babak Hodjat, Risto Miikkulainen (Cognizant AI Lab; UT Austin & Cognizant AI Lab)
Source: https://arxiv.org/abs/2511.09030
Date: 12 Nov 2025

## Abstract

LLMs have achieved remarkable breakthroughs in reasoning, insights, and tool use, but chaining these abilities into extended processes at the scale of those routinely executed by humans, organizations, and societies has remained out of reach. The models have a persistent error rate that prevents scale-up: for instance, recent experiments in the Towers of Hanoi benchmark domain showed that the process inevitably becomes derailed after at most a few hundred steps. Thus, although LLM research is often still benchmarked on tasks with relatively few dependent logical steps, there is increasing attention on the ability (or inability) of LLMs to perform long range tasks. This paper describes MAKER, the first system that successfully solves a task with over one million LLM steps with zero errors, and, in principle, scales far beyond this level. The approach relies on an extreme decomposition of a task into subtasks, each of which can be tackled by focused microagents. The high level of modularity resulting from the decomposition allows error correction to be applied at each step through an efficient multi-agent voting scheme. This combination of extreme decomposition and error correction makes scaling possible. Thus, the results suggest that instead of relying on continual improvement of current LLMs, massively decomposed agentic processes (MDAPs) may provide a way to efficiently solve problems at the level of organizations and societies.

## 1 Introduction

Technological achievements of advanced societies are built on the capacity to reliably execute tasks with vast numbers of steps. Whether constructing a skyscraper, airplane, particle accelerator, or iPhone, running a hospital or medical research organization, processing tax returns and delivering social benefits at a national scale, or even something as seemingly simple as producing a loaf of bread, the precise execution of detailed plans and policies is critical to producing high-value outcomes and maintaining societal trust.

Large language models (LLMs) are increasingly inserted into large and complex real-world processes. This paper focuses on the question of how/whether LLMs can execute large tasks with extreme precision, e.g., when a 1% per-step error rate is not acceptable.

This question is investigated by applying LLM-based reasoning to the Towers of Hanoi problem, whose solution requires more than one million LLM steps with zero errors. Most benchmarks evaluate quality using independent examples, each requiring not many more than a few dependent logical execution steps. A benchmark might be considered solved if accuracy is 99%. However, a system with a 1% per-step error rate is expected to fail after only 100 steps of a million-step task. Solving a million-step task with zero errors requires a fundamentally different approach.

Such an approach is proposed: **Massively decomposed agentic processes** (MDAPs). Main contributions:

- A design of the **MDAP framework**, which consists of three core components: (1) decomposition into minimal subtasks; (2) error correction based on subtask-level voting; and (3) red-flagging to reduce correlated errors.
- A formalization of this framework that yields **scaling laws**, e.g., how probability of success and expected cost change with respect to the number of total steps and level of task decomposition. Under this formalization we find effective scaling under extreme decomposition and infeasibility without it.
- The empirical applications of the framework to **successfully solve a task with over one million steps with zero errors**. One main takeaway is that 'state-of-the-art' reasoning models are not required; relatively small non-reasoning models suffice.

This paper provides a first implementation of the MDAP framework: **MAKER** (for **M**aximal **A**gentic decomposition, first-to-ahead-by-**K** **E**rror correction, and **R**ed-flagging), evaluated on the Towers of Hanoi domain. MAKER is a system of *agents* in which each agent is assigned a single subtask to solve. The *role* of each agent is defined by the subtask it is assigned. By avoiding anthropomorphizing agents (i.e., by assigning them human-level roles) and instead assigning them tiny 'micro-roles', it is possible to exploit the inherent machine-like nature of LLMs.

The results demonstrate an instance of **multi-agent advantage** (akin to quantum advantage), that is, a solution to a problem that is not solvable by a monolithic single-agent system. This sets the stage for a new paradigm of scaling AI: instead of relying on continual improvement of simple underlying LLMs, more powerful AI is achieved through massively decomposed agentic processes (MDAPs).

## 2 Background

### 2.1 Large Agentic LLM Tasks

As large language models have improved, increasing consideration has been given towards real world economic tasks that require multi-step, long horizon reasoning. Research in this direction has repeatedly confirmed an inherent property of LLMs: their performance deteriorates significantly (and often exponentially) with the length of the task horizon, regardless of task complexity. This has led to recent focus on the ability (and failure) of LLMs to *execute*, i.e., failing to complete many-step tasks, even when a correct plan to follow is explicitly provided.

Recent theoretical work has claimed that decomposing large tasks into the smallest possible subtasks can have substantial efficiency benefits. The rise of decomposing tasks into subtasks solvable by focused "small language model" (SLM) agents in industry, motivated by both reliability and cost, as well as the burgeoning study of multi-agent LLM systems in academia, provides evidence for the practicality of this idea. This paper continues this line of work.

### 2.2 Error Correction

Error correction is a critical capability across many important areas of computing, including communication, memory storage, and quantum computing. Error correction makes it possible to pretend that digital communication and classical computation are deterministic, when in fact, single bits are getting lost and flipped all the time. Similarly, improved error correction is the single most important ingredient to achieving scalable quantum computing. In biological systems, error correction is critical to large processes growing and persisting over time.

LLMs now serve as the basis of another substrate of computing, *linguistic computing*, whose constituent processes are *language-based algorithms* (LbAs). Error correction is critical to achieving LbAs that scale, mitigating the inherent nondeterminism that results from producing language by pulling from a probability distribution.

Many possible LbA error correction methods can be derived from instances in other fields. One way to reduce errors is for an LLM to reflect on its output and explicitly correct any error it sees. Another approach is to quantify and exploit LLM uncertainty explicitly. This promise of semantic consistency in sampling makes a third, simpler, approach possible: voting, or *ensembling*, which has been a core machine learning technique for decades, and is now commonly used to boost the accuracy of LLM-based systems.

### 2.3 Motivating Challenge Domain: Towers of Hanoi

Towers of Hanoi was recently introduced as a test domain for investigating the capabilities and limitations of state-of-the-art LLM reasoning models. This benchmark is based on the classic game in which there are three pegs and D disks, and the goal is to move all disks from the first to the third peg, moving only one disk at a time, and maintaining the condition that a larger disk never sits atop a smaller one.

Performance of state-of-the-art LLMs degrades catastrophically on this benchmark: they are able to complete the task with a high success rate up until five or six disks, after which the success rate plummets to zero. The reliability of state-of-the-art LLMs is fundamentally limited: if they need to complete every step correctly in order to solve a task, after a certain number of steps they will almost surely fail as a result of an underlying propensity to make errors.

Two critiques of Towers of Hanoi as a benchmark: First, one could argue that it is not an ideal LLM task since one could write code to solve the problem. True, but producing solutions is not the point: the domain provides an ideal testbed for investigating the capacity of LLM-based systems to scale their inherent intelligence to increasingly large numbers of steps. Second, one could argue that this problem is too hard, since large real-world tasks might allow for a handful of errors without catastrophic results. However, focusing on a case where no error can be tolerated forces us to pursue the elimination of any kind of error that is likely to arise on a long timescale, and this focus can lead to insights and practical methods that might otherwise be overlooked.

## 3 Methods

MAKER involves three main ingredients: (1) Decomposing a task into the smallest possible subtasks; (2) exploiting the modularity of such a decomposition to implement efficient error correction; and (3) "red-flagging" LLM outputs, i.e., discarding outputs whose structure suggests increased risk of errors, particularly correlated errors.

### 3.1 Maximal Agentic Decomposition

In a long-horizon agentic task with s steps, the goal of an LLM-based system is to produce a sequence of actions a_1, ..., a_s that yields a target output y given the initial input x. The s-step task can be decomposed into subtasks, with the granularity of the decomposition defined by the number of steps m per subtask. Subtasks can then be solved by separate calls to LLM *agents*, where a templating function maps the input and specification of a subtask to a prompt for an LLM M.

Of particular interest are the two extreme cases:
- **Single-agent** (m = s): a_1, ..., a_s ~ (psi_a o M o phi)(x)
- **Maximal agentic decomposition** (MAD), i.e., m = 1

Because LLMs are auto-regressive, when generating the ith action, a single agent M is increasingly burdened by the context produced in generating previous actions. Therefore, as the context increases, its outputs become increasingly unreliable. However, with MAD, an agent's context is limited to an amount of information sufficient to execute its single assigned step, allowing it to focus on its assigned role and avoid confusion that can creep in from irrelevant context.

One might argue that this decomposition might improve the reliability of any given LLM call, but by decomposing the task into s independent calls, there are now s possible points of failure, instead of just one. The probability of generating a correct action sequence is exponentially decaying as the number of steps increases:

p(a_1*, ..., a_s*) = prod_{i=0}^{s-1} p((psi_a o M o phi)(x_i) = a_{i+1}*)

However, the modularity induced through maximal decomposition allows for a form of effective and efficient error mitigation and unreliability detection ("red-flagging") that is not possible with a single large call.

### 3.2 First-to-ahead-by-k Voting and Scaling Laws

For simplicity, the error correction in this paper uses the statistical power of independent samples from a stochastic process (here an LLM). To determine a winner from these samples, a *first-to-ahead-by-k* voting process is used, motivated by the optimality of such an approach in the sequential probability ratio test (SPRT).

Concretely, given an LLM M, candidate samples are drawn for a subtask until one has been sampled k times more than any other. This process is a generalization of the classic gambler's ruin problem, but with simultaneous dependent races between all pairs of candidates. For the analysis, it is assumed that a correct candidate with probability p races against a single alternative with probability 1-p. If p > 0.5, the probability that the correct candidate gets selected is:

p(a_i = a*) = 1 / (1 + ((1-p)/p)^k)

Now, suppose the task requires s total steps, with an inherent per-step success rate p, a decomposition level given by the number of steps per subtask m, and that a margin of k votes is required to decide an action for each subtask. The probability that the full task is completed successfully is:

p_full = p_sub^(s/m) = (1 + ((1-p)/p)^k)^(-s/m)

**Key scaling result** (Eq. 18): For maximal decomposition (m = 1):

E[cost of solving full task; m = 1] = Theta(p^{-1} * c * s * ln s) = Theta(s ln s)

when p, c, and t are held constant. This shows that cost grows log-linearly with s. The k_min (minimum votes required to achieve target success probability t) grows logarithmically with s no matter the decomposition level:

k_min = ceil(ln(t^{-m/s} - 1) / ln((1-p)/p)) = Theta(ln s)

In contrast, when m > 1, the cost grows exponentially with m.

### 3.3 Red-Flagging: Recognizing Signs of Unreliability

Since p plays such an important role in the cost of the system, it is worth taking practical measures to push it higher. The simple premise is that "bad" behaviors are correlated in LLMs, so if an LLM produces a response that signals pathological behavior, the response should be flagged and simply discarded. Since in MAD each agent is responsible for only a single step, each step is not too expensive, and it can be discarded and a new action resampled.

Two signs of unreliability are used as red flags:
1. **Overly long responses**: once an LLM gets initially confused, it can go off the rails and over-analyze a situation in a cycle of self-destruction. An agent doing too much work to figure out its answer is likely confused and missing the point.
2. **Incorrectly formatted responses**: when an agent produces an answer in an incorrect format, it is more likely to have become confused at some point on the way to that answer.

The expected cost of MAKER with red-flagging (where v is the probability that a valid response is parsed from the LLM's output):

E[cost of MAKER] ≈ cs * k_min / (v(2p-1)) = Theta(cs ln s / (vp))

## 4 Experiments

### 4.1 Setup

The implementation of MAKER for the Towers of Hanoi problem was derived from the single-agent approach introduced in prior work. The single-agent prompts were modified so that each agent knows that it must only perform a single step of the problem, i.e., to move a single disk. For efficiency, and to focus the agents as much as possible, each agent is given the minimal context it needs to perform its single step: the overall strategy and the current state of the problem (the configuration of disks).

Each agent is asked to produce the next move and the resulting next state. This requires producing the state along with the action, since this is critical information to be fed to the next agent. Each agent is asked to format its answers as "move = <move>" and "next_state = <next_state>".

### 4.2 Estimating single-step success rates

Running an LLM-based system at the scale of a million steps is expensive. It is thus desirable to calibrate the parameters of the system and estimate the success rate and cost before any large experiments are run. A straightforward way to estimate the per-step success rate is to run the system on a random subset of steps.

Initial exploratory estimation experiments were run without red-flagging. Agents were given a maximum of 2048 output tokens as an initial conservative upper bound. They also used a "repairing parser" (written by an LLM) that attempted to correct some of the more common formatting issues in order to extract the LLM's intended answer reliably out of its output.

Key finding from Figure 6a: (1) Different LLMs have different base error rates, but those of relatively small non-reasoning models are comparable to more advanced reasoning models, suggesting that non-reasoning models may be a more effective fit for long-range tasks with MAKER. (2) The per-step error rate is remarkably stable as the number of disks increases, a highly encouraging sign that MAKER will enable scaling to a large number of steps.

### 4.3 Projecting the cost of error correction

Based on single-step error rates, Figure 6b shows estimated costs for models with p > 0.5 to successfully solve the full 20-disk task (t = 0.95). The most effective proprietary choice is `gpt-4.1-mini`, and the most effective open-source choice is `gpt-oss-20B`. Key data:

| Model | $/M | tok | 1-p | k_min | E[cost] |
|-------|-----|-----|-----|-------|---------|
| gpt-4.1-nano | 0.4 | 842 | .3571 | 29 | $41.9K |
| gpt-4.1-mini (τ=1.0) | 1.6 | 580 | .0040 | 4 | $4.9K |
| **gpt-4.1-mini (τ=0.1)** | **1.6** | **538** | **.0022** | **3** | **$3.5K** |
| o3-mini (low) | 4.4 | 535 | .0018 | 3 | $9.4K |
| haiku-4.5 | 5.0 | 588 | .1839 | 12 | $71.2K |
| llama-3.2-3B | 0.06 | 434 | 1.0 | - | - |
| gpt-oss-20B | 0.2 | 1104 | .0358 | 6 | $1.7K |
| qwen3 | 0.6 | 449 | .2342 | 15 | $11.5K |
| deepseek-v3.1 | 1.7 | 1004 | .0569 | 6 | $14.6K |
| kimi-k2 | 3.0 | 925 | .0393 | 6 | $22.9K |

### 4.4 Solving the 20-disk problem: Over one million steps with zero errors

With `gpt-4.1-mini` as the base model, the maximum output token threshold was set to 750, and a red-flagging output parser was used to enforce the basic formatting requirements. Since k_min = 3, at least three responses were generated in parallel for each step. The first step was generated with a temperature of 0 to make sure the best possible guess is included in the votes. For all subsequent votes, a temperature of 0.1 was used.

With these calibrations, the full system solved the problem perfectly. Figure 7 shows a snapshot of an animation visualizing the movement of the disks through the million steps. This result constitutes the first successful solution of a task with one million LLM steps with zero errors, establishing that scaling LLM-based systems to large time horizons is possible.

The number of undecided steps decreases exponentially with sampling round, consistent with the theoretical prediction. Due to this exponential decay, the vast majority of LLM calls (and therefore cost) is spent in the first k calls, while the remaining cost is, for practical purposes, a rounding error.

### 4.5 Investigating the impact of red-flagging

Red-flagging was hypothesized to reduce the per-step error rate, but also the impact of correlated errors. The per-step error rate increases precipitously once the response length crosses about 700 tokens. However, since so few of the overall responses are overly long, the overall error rate at higher max token thresholds is not much larger, and in particular, not large enough to induce an increase in k_min.

However, the main benefit of red-flagging becomes clear when focusing on correlated errors: moving from a 'helpful' repairing output parser to one that discards samples with any formatting issues leads to lower collision counts (i.e., number of steps whose first two votes are incorrect). Red-flagging successfully reduces some of these correlated errors and may be critical to the success of the method on many-step tasks.

## 5 Discussion and Future Work

**More General Applications**: LLM behaviors can be divided into two categories: *insights* and *execution*. Insights come from an LLM creatively generating ideas, plans, and strategies, while execution involves following through with them. This paper focused on execution. Extending the framework to handle LLM-based insights is an area of future work, since insights are inherently more open-ended and may come with irreducible step-wise uncertainty.

Preliminary experiments in a more general version of MAKER were created with four agent types: decomposition agents, decomposition discriminator agents, solution discriminator agents, and problem solver agents. The system achieved promising results on large-digit multiplication.

**The Importance of Decorrelated Errors**: Theoretical analysis assumed errors are i.i.d. across steps. There were a few steps that, for no apparent reason, had substantially higher inherent error rates than others. Such strange behaviors for particular inputs are well-known side-effects of LLM training. The independent sampling plus red-flagging method was sufficient to overcome them, but more sophisticated decorrelation methods may be required in real-world cases.

**Parallels with microservices**: Parallels can be drawn between microagents and microservices. The benefits of decomposing a monolithic agent's task into subtasks are similar to those of decomposing a monolithic application into smaller services:

- **Modularity**: Each microagent can be tailored to a specific task and leverage the right tools for the job.
- **Data management**: Each microagent is responsible for managing its data.
- **Independent development**: Microagents can be updated and tested in isolation.
- **Scalability**: Microagents can be scaled independently.
- **Communication**: Natural language is a powerful, well-understood communication protocol.
- **Complexity**: As microservices solve for large-scale systems, microagents solve for complex reasoning tasks.
- **Real-time monitoring**: Microagents can be monitored in real-time.
- **Design for failure**: Microagents are designed to tolerate the failure of any of the agents.
- **Evolutionary design**: Change is easier to manage with microagents than with a monolithic agent.

**Limits of Decomposition**: The application of MAKER assumes a task can be decomposed into small enough and simple enough steps such that each step can be solved by an LLM agent with reasonable probability. There is thus one central question that will dictate how broadly the methods can be applied: Are there important problems where such a decomposition is not possible or is computationally infeasible to discover?

**Safety, Morality, and the Future of Superintelligence**: If large and important real-world problems can be successfully decomposed into microsteps, there could be major benefits with respect to safety. If each step has a clearly defined and limited focus and purpose, the LLM's view of the world and domain of influence can be strictly limited, allowing for more effective sand-boxing, auditing, and general control. Multiple focused agents can be run independently on each step, which also substantially reduces the ability of agents to collude to produce harmful actions.

LLMs today have just about all the raw intelligence needed to scaffold them into the great superintelligent skyscrapers of the coming age. MDaps present an alternative path to realizing the benefits of superintelligence, which, compared to endlessly building bigger and smarter single-agent models, comes with substantially reduced risks to both humans and machines.

## 6 Conclusion

This paper focused on the question of how LLM-based agentic systems can be massively scaled. Decomposing tasks into minimal subtasks makes it possible to apply error-correction techniques effectively and efficiently, supporting scaling to millions of steps and beyond. A new category of AI systems results, i.e. massively decomposed agentic processes, or MDAPs. MAKER is a first implementation of this approach, and the experiments in this paper on Towers of Hanoi a first demonstration of its value. This foundation opens the door to more general-purpose implementations and large-scale, long-running real-world applications. Such MDAPs offer an alternative to building endlessly larger and more intelligent LLMs: By smashing intelligence into a million pieces, it is possible to build AI that is efficient, safe, and reliable.
