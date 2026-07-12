---
source: https://arxiv.org/html/2505.18761v2
description: Introduces GSM-DC, a controlled benchmark using symbolic DAGs to systematically measure how irrelevant context degrades LLM reasoning — quantifies power-law error scaling with distractor count, and shows Hard-IC training plus PRM-guided tree search are the most effective robustness interventions.
captured: 2026-03-26
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark

Author: Minglai Yang, Ethan Huang, Liang Zhang, Mihai Surdeanu, William Wang, Liangming Pan
Source: https://arxiv.org/html/2505.18761v2
Date: 22 Sep 2025

## Abstract

We introduce *Grade School Math with Distracting Context* (GSM-DC), a synthetic benchmark to evaluate Large Language Models' (LLMs) reasoning robustness against systematically controlled irrelevant context (IC). GSM-DC constructs symbolic reasoning graphs with precise distractor injections, enabling rigorous, reproducible evaluation. Our experiments demonstrate that LLMs are significantly sensitive to IC, affecting both reasoning path selection and arithmetic accuracy. Additionally, training models with strong distractors improves performance in both in-distribution and out-of-distribution scenarios. We further propose a stepwise tree search guided by a process reward model, which notably enhances robustness in out-of-distribution conditions.

## 1 Introduction

Recent advances in Large Language Models (LLMs) have demonstrated reasoning capabilities across diverse tasks, notably in solving mathematical problems. Despite these advancements, LLMs are found to be less robust in reasoning. For example, the Flanker Task in cognitive psychology shows that humans' responses become slower and less accurate with increased distractors. Shi et al. (2023a) first revealed that LLMs similarly suffer performance degradation when irrelevant context is introduced, observing notable reductions in accuracy even with just a single distractor sentence added to math problems from the GSM8K dataset.

Prior work has not systematically explored the mechanisms underlying this sensitivity. Shi et al. (2023a) employed only a single distractor, limited experiments to short reasoning chains, and omitted supervised fine-tuning and out-of-distribution (OOD) evaluations. Several important questions thus remain: How does varying the amount of IC affect robustness? Can robust reasoning be enhanced through supervised fine-tuning? How does the intensity of IC during training impact model performance in both in-distribution and OOD scenarios? Additionally, how can the above questions be qualitatively evaluated?

To address these gaps, we introduce *GSM-DC*, a synthetic benchmark designed to enable precise control over both reasoning complexity and distractor structure. Problems in *GSM-DC* are represented as symbolic dependency graphs, where nodes correspond to intermediate quantities and edges represent symbolic operations. This structure facilitates: 1) the explicit injection of irrelevant context via off-path nodes and edges without affecting correct solutions; 2) adjustment of reasoning complexity by varying graph depth and structure; and 3) automatic evaluation of model outputs by aligning predictions with the correct reasoning path.

Our dataset construction pipeline involves generating symbolic dependency graphs, injecting distractors after determining the solution path, and transforming these into human-readable math word problems. We partition our dataset based on different problem complexities and distractor intensities, conduct various controlled experiments, and use automatic stepwise metrics measuring arithmetic correctness and distraction robustness. Our controlled experiments yield three main findings. First, model accuracy steadily decreases as distractor intensity rises. Second, continued pretraining substantially enhances reasoning robustness. Third, incorporating strong IC during training significantly boosts model resilience, showing superior performance across various distractor intensities in out-of-domain testing.

## 2 Related Work

**Reasoning with Irrelevant Context** LLMs often struggle to reason accurately in the presence of irrelevant context (IC). Prior work has explored this vulnerability by introducing distractors into math problems. For example, GSM-IC (Shi et al., 2023a) appends irrelevant sentences to arithmetic questions but lacks control over distractor structure or complexity. GSMIR (Jiang et al., 2024a) and MPN (Song and Tavanapong, 2024) use hand-crafted prompting strategies to mitigate the effects of textual noise. Anantheswaran et al. (2024) generate adversarial math problems by adding irrelevant variables, showing significant performance drops and partial robustness gains through fine-tuning. However, their hand-crafted distractors risk introducing bias and lack structural control. Other studies show that semantically similar but irrelevant documents can impair LLM performance, but RAG can improve robustness. While these works expose LLMs' sensitivity to IC, they provide limited control over distractor properties. In contrast, *GSM-DC* injects distractors into symbolic reasoning graphs, enabling stepwise evaluation. We further show that a reward-guided beam search improves robustness beyond standard fine-tuning.

**Understanding LLM Reasoning** LLM reasoning has received growing attention, leading to diverse efforts to improve performance on complex tasks. Recently, synthetic benchmarks such as GSM-∞ (Zhou et al., 2025) and iGSM (Ye et al., 2025) explored LLM reasoning under long-context and complex distractors. Unlike GSM-∞ and iGSM, our *GSM-DC* explicitly controls irrelevant distractors within symbolic DAGs to systematically quantify the effects of irrelevant context. Recent methods such as ReAct, Tree-of-Thoughts, and self-consistency decoding guide intermediate steps to improve solution quality. Beyond final-answer supervision, Process Reward Models (PRMs) evaluate partial reasoning paths to promote more robust, interpretable, and aligned multi-step reasoning.

## 3 The GSM-DC Dataset

To systematically investigate how LLMs reason under irrelevant context (IC), we require a framework that satisfies three desiderata: 1) fine-grained manipulation of IC, 2) precise control over reasoning difficulty, and 3) automatic evaluation of reasoning robustness. Existing datasets like GSM-IC are manually built and rely on free-form outputs, lacking structural constraints and making stepwise evaluation impractical without manual checks.

We propose the *Grade School Math with Distracting Context* (*GSM-DC*) benchmark — a controlled framework for systematically evaluating LLMs' reasoning under irrelevant context that meets the above criteria. Each math word problem in *GSM-DC* is represented as a directed acyclic graph (DAG), which allows us to 1) explicitly control irrelevant context by injecting distracting nodes and edges, 2) explicitly control reasoning difficulty by adjusting the graph size, and 3) automatically compute stepwise reasoning correctness by comparing model predictions to the ground-truth reasoning path. As illustrated in Figure 1, we construct the *GSM-DC* dataset in three steps:

**1) Dependency Graph Construction:** To represent a math word problem, we build a symbolic dependency graph G to capture the direct, implicit, and instance-level dependencies in the problem. We then identify a single correct reasoning path P from the graph G via topological sort.

**2) Irrelevant Context Injection:** We turn all nodes outside the reasoning path P into distractors, producing an augmented graph G'. This allows us to explicitly control the problem complexity (e.g., number of reasoning steps) and the intensity of irrelevant context (e.g., via the number and connectivity of distractor nodes).

**3) Natural Language Realization:** We then convert the augmented graph G' into a human-understandable math word problem M by mapping each node to a real-world entity and rendering each edge into a statement. The ground-truth solution S is then derived from the original reasoning path P.

As a result, each problem in the *GSM-DC* is represented as (G', M, P, S). This structured representation enables automatic stepwise evaluation of LLMs' reasoning chain via the ground-truth path P.

### 3.1 Dependency Graph Construction

Many grade-school math or logical reasoning problems involve quantities that are interrelated in various ways. These dependencies typically fall into three categories: 1) *Direct dependencies*, where one quantity is computed directly from another (e.g., if R denotes the radius of a circle and T its diameter, then T = 2 × R); 2) *Instance dependencies*, one entity is automatically reliant on another without explicitly stating that reliance. (e.g., "Each shelf holds M books, and there are N shelves") and 3) *Implicit dependencies*, requiring aggregation or inference over multiple quantities (e.g., grouping cats and dogs as animals).

To model these interrelations, we use the directed acyclic graph (DAG), denoted as G, where each *node* denotes a quantity (e.g., Bob's pens) and each *edge* represents the dependency between quantities (e.g., Alice has one more pen than Bob). We name G as the *dependency graph*. We use DAG because the acyclicity ensures that no quantity depends on itself, allowing a valid solution path P to be recovered via topological sort.

This structured graph-based representation forms the foundation for controlling reasoning complexity and enables injection of irrelevant context without affecting the original solution path P. Given inputs — reasoning steps rs, maximum edges E and distractor count m — we generate a DAG by sampling nodes and edges, then extract the solution path P of length rs via topological sort, and finally inject m controllable distractors. All GSM-DC instances are guaranteed to be well-defined and solvable with a unique solution path P.

### 3.2 Irrelevant Context Injection

To create a problem with irrelevant information, we augment the dependency graph by injecting distractor nodes while preserving the original solution path. We start with a clean dependency graph G and its solution path P. Unused nodes, which are not part of P, are selected and connected to existing nodes through forward-only edges, resulting in a new graph G' that remains acyclic.

Problem difficulty is primarily controlled by the number of reasoning steps rs. To limit the problem complexity across instances, we constrain the input DAG G to have at most E edges. Given such a fixed-scale graph and its solution path P, we inject m distractor nodes (none of which lie on P) to produce the augmented graph G'. Importantly, because the total graph scale is bounded by E, longer reasoning steps occupy more of the graph structure, leaving fewer nodes and edges available for distractor injection. We vary m ∈ [m_min, m_max] to define three distractor intensity levels (e.g., for rs = 2, light uses m ∈ [0,2], medium m ∈ [3,4], hard m ≥ 5).

### 3.3 Natural Language Realization

Once the dependency graph G is constructed and augmented as G', we instantiate it into natural language. Each node is mapped to an entity (e.g., "Arts Campus's T&T Supermarket") from the hierarchical entity vocabulary of the GSM8K dataset, and each edge is rendered using a templated relational statement (e.g., "the number of Zion Markets is 1 more than the number of T&T Supermarkets"). These templates capture the underlying dependencies while maintaining simple, readable language.

To form the math problem M, we concatenate natural-language realizations of edges along the solution path, ending with a question about the final node. Distractors are rendered as unrelated sentences and shuffled with relevant content.

Alongside the natural language (NL) problem M, we generate its corresponding NL solution S based on the ground-truth reasoning path P. The solution S sequentially defines variables for each node along the path P and applies the dependencies.

### 3.4 Stepwise Solution Evaluator

After constructing *GSM-DC*, we build a stepwise solution evaluator to automatically evaluate LLM-generated solutions. For each problem and predicted solution, we report three *binary* scores; for each, a value of 1 is awarded only when the stated criterion is fully satisfied.

- **Step Accuracy (SAcc):** Our symbolic parser reads the model's chain-of-thought and executes every intermediate equation in topological order. SAcc = 1 iff *all* equations are arithmetically correct *and* each step references only symbols that have already been defined. We enforce node-level alignment in the parser (not strict sequence matching). This strict all-or-nothing formulation avoids inflating performance with partially correct derivations.

- **Path Accuracy (PAcc):** To quantify *distraction robustness* we check whether the model confines its reasoning to the augmented dependency graph G' after injecting irrelevant context. PAcc = 1 iff (i) every required dependency on P is present, and (ii) no irrelevant node is used in the computation of any step on P. Similar to SAcc, evaluation is performed via *node-level alignment*, not strict sequence matching: valid steps may appear in any order, and redundant or extra steps are permitted, so long as they do not interfere with the correct solution path P. PAcc is a relaxation of SAcc as it only requires stepwise reasoning to be correct, but not the associated values themselves.

- **Extraction Answer Accuracy (EAcc):** To capture final-answer correctness, EAcc = 1 iff the model's extracted answer exactly matches the ground truth. We report EAcc only for prompting, but our focus remains on SAcc and PAcc.

We evaluate these metrics over a large set of problems and report each as the percentage (%) of instances achieving a score of 1.

## 4 Experiments

### 4.1 Impact of Irrelevant Context

To systematically analyze how irrelevant context (IC) affects LLM reasoning, we conduct controlled experiments by injecting varying numbers of irrelevant context (m = 1–15) into math word problems M drawn from *GSM-DC*. We evaluate performance across four levels of reasoning steps, denoted rs ∈ {2, 3, 4, 5}, and sample 100 instances per condition to ensure statistical stability.

We benchmark six instruct models: Grok-3-Beta, GPT-4.1, GPT-4o-mini, LLaMA-3.3-70B, LLaMA-3.1-8B and LLaMA-3.2-1B. We employ a five-shot prompting strategy enhanced with a structured *Background* section that explicitly encodes relevant dependencies to guide reasoning. Model performance is assessed using three metrics using *Stepwise Solution Evaluator*, SAcc, PAcc and EAcc, which together capture reasoning correctness, robustness to distractors, and output correctness.

**Finding I: LLMs' reasoning performance degrades with increasing irrelevant context.**

As shown in Figure 4, all six models exhibit a clear degradation in reasoning accuracy as the number of irrelevant context increases. For instance, at a fixed reasoning depth of rs=5, Grok-3-Beta's step accuracy drops from 43% with one irrelevant context to just 19% under fifteen irrelevant context. GPT-4.1 exhibits an even steeper decline at the same depth, falling from 26% to 2%.

All three evaluation metrics — step accuracy (SAcc), path accuracy (PAcc), and extraction accuracy (EAcc) — exhibit similar downward trends as irrelevant context increases. Extraction accuracy (EAcc) remains relatively high, because our solution parser enforces a strict Chain-of-Thought format that models learn to follow through five-shot prompting. As a result, EAcc is less sensitive to distraction compared to SAcc and PAcc, which more directly assess reasoning fidelity and resistance to irrelevant information.

**Finding II: Irrelevant context degrades accuracy more steeply at greater reasoning depths.**

To analyze how irrelevant context (IC) interacts with reasoning complexity, we study the error rate E(m; rs) as a function of distractor count m and reasoning depth rs. We find it roughly follows a power-law trend: E(m; rs) ∝ m^δ(rs), where δ(rs) reflects a model's IC sensitivity. Error increases with m, and the degradation steepens with deeper reasoning.

For instance, Grok-3-Beta's exponent grows from δ ≈ 0.11 at rs=2 to δ ≈ 0.49 at rs=5, indicating greater vulnerability at deeper depths. GPT-4.1 shows a similar slope but higher baseline error, suggesting that reasoning depth governs δ(rs), while model capacity sets the vertical intercept — i.e., robustness under minimal distraction. These findings highlight the need to jointly consider reasoning complexity and IC sensitivity when designing robust LLMs.

### 4.2 Training with Different Strategies

**Finding III: Continued pretraining enhances robustness even without access to IC samples.**

Building on this controlled training setup, we investigate how different finetuning strategies affect reasoning robustness under irrelevant context. Specifically, we compare continued pretraining (full finetuning) and LoRA finetuning for reasoning robustness using a 30K-sample training set. As shown in Figure 5, continued pretraining confers strong robustness even without IC supervision, substantially outperforming LoRA on clean data. With IC training, the gap narrows, but continued pretraining remains consistently more robust across reasoning depths.

### 4.3 Control of Training Data

**Finding IV: Training with irrelevant context improves robustness most effectively.**

As shown in Table 1, the model trained on IC consistently achieves the highest SAcc and PAcc across all rs. The model trained on Clean+IC data performs slightly worse, while the Clean model lags behind both. These results suggest that training solely on IC leads to stronger robustness, because of increased exposure to IC during learning.

The clean model performs worse on questions with IC, even under in-distribution (ID) settings. To better understand this limitation, we examine the gap Δ(SAcc, PAcc), represented as the ratio between SAcc and PAcc (Figure 6). A lower ratio indicates a larger gap — arithmetic errors occurring even when the reasoning path is correct. The model trained on Clean data consistently shows a higher Δ, suggesting that IC affects not only reasoning path selection, but also arithmetic execution. These findings reveal that IC broadly disrupts reasoning, and that training with IC-injected examples leads to more robust models.

**Finding V: Training with challenging irrelevant context leads to the strongest robustness and generalization across all pretraining settings.**

Having established that exposure to irrelevant context during training improves robustness, we now investigate whether the intensity of such context further influences generalization. In particular, we test whether training on harder, more distracting IC leads to greater robustness on out-of-distribution (OOD) reasoning problems. Hard-IC yields the best SAcc across all in-distribution and OOD settings, regardless of IC presence or difficulty. Mix-IC, despite incorporating distractor diversity, consistently underperformed Hard-IC, suggesting that distractor difficulty, rather than variety, is the primary driver of improvement.

## 5 Improving Model Robustness Against Irrelevant Context

**Finding VI: PRM-guided tree search preserves ID accuracy while consistently boosting OOD robustness across all IC training levels.**

Our Tree of Thoughts (ToT) algorithm addresses complex reasoning problems by combining tree search with the step-by-step inference capabilities of large language models (LLMs). ToT not only uses an LLM to propose candidate reasoning steps, but also integrates a Process Reward Model (PRM) to evaluate and guide the search process. Given a partial reasoning path h_{1:t}, the PRM assigns a reward R(h_{1:t}) indicating the quality of reasoning up to step t. Leveraging a synthetic dataset, we systematically inject irrelevant context (IC) and arithmetic errors into selected reasoning paths. These negative examples are used to train the PRM to distinguish valid reasoning trajectories from those corrupted by irrelevant context (IC) and wrong arithmetic calculations enabling the model to prioritize more accurate and robust solutions during search.

Through our experiments, we found that the measured accuracy, both SAcc and PAcc, for the in-distribution case with and without a PRM were similar. Furthermore, in the OOD case, the accuracy we measured was significantly improved when a PRM was used. The results suggest that using a PRM preserves model performance in ID tasks, while also allowing the model to generalize its responses to OOD tasks. The model trained with hard IC performs the greatest, and supplementing it with a PRM significantly improves its accuracy.

## 6 Conclusion

We present *GSM-DC*, a controlled benchmark for rigorous evaluation and improving the robustness of LLM reasoning in the presence of systematically injected irrelevant context (IC). By framing math problems as symbolic DAGs, *GSM-DC* enables precise control over reasoning complexity and distractor structure, along with automatic stepwise evaluator. Our experiments reveal that: 1) LLM accuracy degrades as distractor count increases, with the error roughly following a power-law trend whose exponent grows with reasoning depth; 2) IC affects not only reasoning path selection, but also arithmetic execution; 3) Training with challenging IC, combined with continued pretraining, yields the strongest robustness across both in-distribution and out-of-distribution settings, consistently outperforming LoRA finetuning under clean and noisy conditions. Finally, we show that reasoning robustness can be further improved at inference time using beam search with PRM, which boosts OOD step accuracy by up to 6.29%. Together, these findings position *GSM-DC* as both a diagnostic tool for analyzing IC sensitivity and a foundation for developing robust training and inference time strategies for language models reasoning.

## Limitations

*GSM-DC* provides a controlled environment for probing LLM reasoning, combining symbolic DAGs with natural-language templates inspired by datasets like iGSM. To enhance linguistic diversity and realism, we designed a hierarchical vocabulary system derived from GSM8K and constructed templated prompts with varied surface forms. While this approach balances control and naturalness, the use of templates still limits full linguistic expressiveness. To address this, we plan to expand the benchmark with more diverse natural-language realizations sampled from real corpora and support more flexible arithmetic reasoning. The current reasoning depth is capped at 22 operations; we are generating new tiers with 30+ steps to explore long-horizon compositionality. While we benchmark six models — Grok-3-Beta, GPT-4.1, GPT-4o-mini, LLaMA-3.3-70B, LLaMA-3.1-8B, and LLaMA-3.2-1B — all training experiments are conducted solely on LLaMA-3.2-1B using a 30K-sample dataset due to computational constraints. Finally, we also aim to include faithfulness and bias diagnostics — such as explanation consistency and demographic sensitivity — to ensure that robustness gains translate into safe and trustworthy reasoning.
