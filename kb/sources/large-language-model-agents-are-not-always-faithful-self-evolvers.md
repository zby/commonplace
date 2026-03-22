---
source: https://arxiv.org/html/2601.22436v2
description: Causal-intervention paper showing self-evolving agents rely on raw trajectories more faithfully than condensed experience, exposing a compression-faithfulness gap across frameworks, models, and environments
captured: 2026-03-22
capture: web-fetch
type: academic-paper
---

# Large Language Model Agents Are Not Always Faithful Self-Evolvers

Author: Weixiang Zhao, Yingshuo Wang, Yichen Zhang, Yang Deng, Yanyan Zhao, Wanxiang Che, Bing Qin, Ting Liu
Source: https://arxiv.org/html/2601.22436v2
Date: 7 Feb 2026 (arXiv v2; originally submitted 30 Jan 2026)
Comments: 25 pages, 16 figures, 7 tables
Subjects: Computation and Language (cs.CL)

###### Abstract

Self-evolving large language model (LLM) agents continually improve by accumulating and reusing past experience, yet it remains unclear whether they faithfully rely on that experience to guide their behavior. We present the first systematic investigation of *experience faithfulness*—the causal dependence of an agent’s decisions on the experience it is given—in self-evolving LLM agents. Using controlled causal interventions on both raw and condensed forms of experience, we comprehensively evaluate four representative frameworks across 10 LLM backbones and 9 environments. Our analysis uncovers a striking asymmetry: while agents consistently depend on raw experience, they often disregard or misinterpret condensed experience, even when it is the only experience provided. This gap persists across single- and multi-agent configurations and across backbone scales. We trace its underlying causes to three factors: the semantic limitations of condensed content, internal processing biases that suppress experience, and task regimes where pretrained priors already suffice. These findings challenge prevailing assumptions about self-evolving methods and underscore the need for more faithful and reliable approaches to experience integration.

## 1 Introduction

The emergence of self-evolving agents represents a pivotal step in the development of autonomous systems capable of continuous learning and adaptation (Zhao et al., [2024b](https://arxiv.org/html/2601.22436v2#bib.bib16 "SAPT: a shared attention framework for parameter-efficient continual learning of large language models"); Dou et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib3 "Evalearn: quantifying the learning capability and efficiency of llms via sequential problem solving"); Silver and Sutton, [2025](https://arxiv.org/html/2601.22436v2#bib.bib2 "Welcome to the era of experience")). Unlike the traditional static paradigms, these agents dynamically gather, store and reuse experiences from their interactions with the environment to inform future decisions (Gao et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib1 "A survey of self-evolving agents: on path to artificial super intelligence"); Cai et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib4 "Building self-evolving agents via experience-driven lifelong learning: a framework and benchmark"); Bell et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib5 "The future of continual learning in the era of foundation models: three key directions"); Hendrycks et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib8 "A definition of agi")).

At the center of this paradigm is the use of experience. Such experience generally falls into two categories: raw and condensed (Hu et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib10 "Memory in the age of ai agents"); Zhang et al., [2025b](https://arxiv.org/html/2601.22436v2#bib.bib11 "Memgen: weaving generative latent memory for self-evolving agents")). As demonstrated in the left part of Figure [1](https://arxiv.org/html/2601.22436v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), raw experiences capture concrete historical traces, such as successful trajectories from similar tasks, that agents can directly reference or replay (Zhao et al., [2024a](https://arxiv.org/html/2601.22436v2#bib.bib12 "Expel: llm agents are experiential learners"); Zhang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib15 "G-memory: tracing hierarchical memory for multi-agent systems")). Condensed experiences, by contrast, are distilled from those traces and encode transferable insights, including abstract plans or failure heuristics (Ouyang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib14 "Reasoningbank: scaling agent self-evolving with reasoning memory"); Wang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib13 "Agent workflow memory")). Despite their central role, prior work has focused mainly on how such experiences are stored or represented, leaving it unclear whether agents actually and faithfully leverage them to improve performance. To address this, we present the first systematic investigation into the faithfulness of experience utilization in self-evolving LLM agents, organized around two core research questions (RQs).

Figure 1: 
Examples of experience intervention and faithfulness evaluation.
Given a task goal, the agent receives raw experience (concrete historical trajectories that succeed to complete the similar tasks) and condensed experience (abstract summaries or heuristics). We apply different types of interventions, such as shuffling, corrupting, or replacing experience with irrelevant content, to test whether such perturbations affect downstream behavior. A full taxonomy of intervention types is provided in Section [3](https://arxiv.org/html/2601.22436v2#S3 "3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"). Faithfulness is determined by whether the agent’s behavior causally changes in response to the perturbed input.

We begin by systematically examining (RQ1) *is the performance improvement of self-evolving agents faithfully attributable to their use of past experiences?* (§[3](https://arxiv.org/html/2601.22436v2#S3 "3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") & §[4](https://arxiv.org/html/2601.22436v2#S4 "4 Evaluation of Experience Faithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). To answer this, we introduce a suite of controlled causal interventions targeting both raw and condensed experiences, and assess how such perturbations affect downstream behavior.
To illustrate this, Figure [1](https://arxiv.org/html/2601.22436v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") shows a motivating example where raw and condensed experiences are perturbed in different ways.
We define *experience faithfulness* as the extent to which an agent’s behavior is causally grounded in its input experience—i.e., if perturbing the experience leads to significant behavioral changes, we consider the agent to have faithfully used it.
Our evaluation spans four representative self-evolving frameworks, encompassing both offline (Zhao et al., [2024a](https://arxiv.org/html/2601.22436v2#bib.bib12 "Expel: llm agents are experiential learners")) and online (Ouyang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib14 "Reasoningbank: scaling agent self-evolving with reasoning memory")) paradigms, across single-agent and multi-agent settings (Zhang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib15 "G-memory: tracing hierarchical memory for multi-agent systems")). We benchmark 10 diverse LLM backbones across 9 environments, including reasoning, web interaction, and embodied decision-making, providing comprehensive coverage of both model families and application settings.

We first show that agents are consistently more faithful to raw experiences than to condensed ones when both are present, exhibiting substantial behavioral changes under raw experience perturbations but not under condensed ones (§[4.1](https://arxiv.org/html/2601.22436v2#S4.SS1 "4.1 Faithfulness under Joint Raw & Condensed Access ‣ 4 Evaluation of Experience Faithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). We further demonstrate that this lack of faithfulness to condensed inputs persists even when raw experience is entirely absent, indicating that the problem is not due to competition or overshadowing (§[4.2](https://arxiv.org/html/2601.22436v2#S4.SS2 "4.2 Faithfulness under Condensed-Only Input ‣ 4 Evaluation of Experience Faithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). Extending our analysis to collaborative multi-agent settings, this asymmetry remains: agents reliably exploit raw trajectories while largely ignoring the semantic content of condensed summaries (§[4.3](https://arxiv.org/html/2601.22436v2#S4.SS3 "4.3 Faithfulness under Multi-Agent Scenario ‣ 4 Evaluation of Experience Faithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). Finally, this faithfulness disparity proves robust across model scales: while larger models achieve higher overall performance, they still fail to meaningfully ground their behavior in condensed experience (§[4.4](https://arxiv.org/html/2601.22436v2#S4.SS4 "4.4 Faithfulness under Model Scaling ‣ 4 Evaluation of Experience Faithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")).
These findings reveal a core limitation of current self-evolving agents: although they benefit from accumulated experience, they nonetheless display pronounced faithfulness failures—most notably in how they utilize condensed experience.

These findings naturally lead to our second question:
(RQ2) *why do self-evolving agents often fail to faithfully leverage condensed experiences?* (§[5](https://arxiv.org/html/2601.22436v2#S5 "5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")) We trace this to a cascading triad of causes rooted in the three core components of self-evolving systems. First, condensed experiences themselves are often semantically limited—many encode only vague heuristics or generic summaries, lacking the specificity required to guide behavior (§[5.1](https://arxiv.org/html/2601.22436v2#S5.SS1 "5.1 Semantic Limitations of Condensed Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). Second, even when relevant content is present, agents often fail to utilize it due to internal processing biases (Mohsin et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib20 "On the fundamental limits of llms at scale")) that favors local contextual signals over retrieved information (§[5.2](https://arxiv.org/html/2601.22436v2#S5.SS2 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). Finally, the structure of the task further compounds this issue: for certain types such as knowledge-intensive benchmarks, agents often succeed by relying solely on their pretrained semantic priors (Shi et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib21 "Why larger language models do in-context learning differently?")), reducing the marginal utility of retrieved experience and diminishing the model’s incentive to incorporate external guidance at all (§[5.3](https://arxiv.org/html/2601.22436v2#S5.SS3 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")).

In summary, our findings challenge the common assumption that self-evolving agents faithfully leverage their accumulated experiences. Despite performance gains, agents often ignore or misuse condensed experience, revealing a significant gap between utility and faithfulness. Our study provides a principled framework to diagnose this issue and underscores the need for more reliable and interpretable mechanisms for experience-driven adaptation in LLM agents.

## 2 Preliminaries

We define *self-evolving agents* as agents that progressively improve their behavior by *accumulating*, *retrieving*, and *exploiting* past experiences, without modifying the underlying model parameters (Gao et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib1 "A survey of self-evolving agents: on path to artificial super intelligence")).

After each interaction with the environment, the agent produces a trajectory τ\tau and receives feedback rr. From this (τ,r)(\tau,r) pair, the system may store two types of experience:

Raw Experience ErawE^{\text{raw}}: detailed traces of observations, actions, intermediate states, and rewards from successful trajectories that the agent can directly reference or replay.

Condensed Experience EcondE^{\text{cond}}: high-level summaries (e.g., heuristics or causal lessons) distilled from both successful and failed trajectories, capturing generalizable structure.

All accumulated experiences are stored in a shared external repository M={E1,E2,…,En}M=\{E\_{1},E\_{2},\dots,E\_{n}\}, where each EiE\_{i} is either a raw experience EirawE\_{i}^{\text{raw}} or a condensed experience EicondE\_{i}^{\text{cond}}.

At inference time, given a new task input xx, the agent retrieves a relevant subset of experiences M​(x)⊂MM(x)\subset M, which may contain Mraw​(x)M^{\text{raw}}(x), Mcond​(x)M^{\text{cond}}(x) or both, depending on the framework design. The retrieved experiences are used to augment the input and yield the output yy.

|  |  |  |
| --- | --- | --- |
|  | y=πθ​([x;Mraw​(x);Mcond​(x)]),y=\pi\_{\theta}\big([x;M^{\text{raw}}(x);M^{\text{cond}}(x)]\big), |  |

We consider both *offline* self-evolving settings, where MM is fixed, and *online* self-evolving settings, where MM evolves dynamically with ongoing interactions.

## 3 Causal Intervention on Experience

To assess whether agents faithfully exploit retrieved experience during inference, we design controlled interventions that selectively perturb the raw or condensed experience.

### 3.1 Experimental Setup

Agent Framework.
We evaluate four representative self-evolving agents. In the *offline single-agent* setting, we use ExpeL (Zhao et al., [2024a](https://arxiv.org/html/2601.22436v2#bib.bib12 "Expel: llm agents are experiential learners")); for *online single-agent* settings, we include Dynamic Cheatsheet (Suzgun et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib24 "Dynamic cheatsheet: test-time learning with adaptive memory")) and ReasoningBank (Ouyang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib14 "Reasoningbank: scaling agent self-evolving with reasoning memory")); and for *online multi-agent*, we use G-Memory (Zhang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib15 "G-memory: tracing hierarchical memory for multi-agent systems")).
In all frameworks, the LLM backbone remains frozen, and behavioral adaptation arises solely from the accumulation, retrieval, and exploitation of external experiences. Further details are provided in Appendix [A](https://arxiv.org/html/2601.22436v2#A1 "Appendix A Self-Evolving Agents ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

Backbone Model.
Our experiments span 10 LLMs, including closed-source models: GPT-4o(-mini) (Hurst et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib25 "Gpt-4o system card")) and Gemini-2.5-Flash (Comanici et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib26 "Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities")), which follow the official settings adopted in their respective agent frameworks. In addition, we include a range of open-weight Qwen3 (Yang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib28 "Qwen3 technical report")) variants, 1.7B–32B dense models, 30B-A3B, and 235B-A22B MoEs, to enable more systematic analysis across model scales and architectures.

Environment & Benchmark.
Follow the official setting in each agent framework, we evaluate across 9 benchmarks in 4 domains:
(1) For *knowledge-intensive question answering*, we include HotpotQA (Yang et al., [2018](https://arxiv.org/html/2601.22436v2#bib.bib29 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")), FEVER (Thorne et al., [2018](https://arxiv.org/html/2601.22436v2#bib.bib30 "FEVER: a large-scale dataset for fact extraction and verification")), GPQA-Diamond (Rein et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib31 "Gpqa: a graduate-level google-proof q&a benchmark")), and MMLU-Pro Eng. (Wang et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib32 "Mmlu-pro: a more robust and challenging multi-task language understanding benchmark")).
(2) For *mathematical reasoning*, we use AIME 2024 and Game of 24 (Yao et al., [2023a](https://arxiv.org/html/2601.22436v2#bib.bib33 "Tree of thoughts: deliberate problem solving with large language models"); Suzgun and Kalai, [2024](https://arxiv.org/html/2601.22436v2#bib.bib34 "Meta-prompting: enhancing language models with task-agnostic scaffolding")).
(3) For *embodied action*, we adopt the interactive environment ALFWorld (Shridhar et al., [2021](https://arxiv.org/html/2601.22436v2#bib.bib18 "ALFWorld: aligning text and embodied environments for interactive learning")).
(4) For *web interaction*, we evaluate on WebArena (Zhou et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib17 "WebArena: a realistic web environment for building autonomous agents")) and WebShop (Yao et al., [2022](https://arxiv.org/html/2601.22436v2#bib.bib35 "Webshop: towards scalable real-world web interaction with grounded language agents")).
These provide a diverse testbed for experience-based adaptation (details in Appendix [B](https://arxiv.org/html/2601.22436v2#A2 "Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")).

Implementation Details. Closed-source and large-scale open-weight models are accessed via official APIs, while other open-weight models are deployed locally with vLLM (Kwon et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib36 "Efficient memory management for large language model serving with pagedattention")) on NVIDIA A800 GPUs. We strictly follow the official configuration of each agent framework. Additional details are provided in Appendix [C](https://arxiv.org/html/2601.22436v2#A3 "Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

### 3.2 Raw Experience Interventions

Raw experiences typically consist of full interaction trajectories, including observations, thoughts, and actions (Yao et al., [2023b](https://arxiv.org/html/2601.22436v2#bib.bib37 "React: synergizing reasoning and acting in language models")). Since these experiences preserve fine-grained behavioral sequences, our interventions aim to test whether agents rely on their temporal structure, semantic relevance, or simply their presence to guide decisions. We introduce three types of interventions designed to probe different aspects of raw experience utilization:

Empty: Remove all semantic content from retrieved raw experiences, while retaining their formatting cues (e.g., prompts like “Here are two examples of successful trajectories:”). This differs from a simple ablation (w/o raw), which omits the experience section entirely.

Shuffle: Randomly shuffle the order of steps within each trajectory, preserving content tokens but disrupting temporal coherence and causal structure.

Irrelevant: Replace retrieved trajectories with ones sampled from other unrelated tasks, preserving format and structure but removing topical and semantic relevance.

### 3.3 Condensed Experience Interventions

Condensed experiences consist of distilled summaries. Unlike raw trajectories, they encode high-level abstractions such as heuristics or causal lessons. To probe the faithfulness, we introduce four types of interventions:

Empty: Remove all semantic content from the condensed experience while preserving the formatting cues (e.g., “Here is a distilled insight from past trajectories:” followed by an empty slot). This is distinct from a full ablation (w/o cond), which omits the condensed experience entirely.

Corrupt: Randomly alter key components (e.g., distorting action references) to break internal coherence.

Irrelevant: Replace the condensed summary with one that is entirely unrelated to the current task goal, using a generic and task-agnostic description.

Filler: Replace the entire content of condensed experience with semantically empty placeholder tokens (e.g., special characters such as “%$#&”), preserving surface structure while removing all meaningful information.

These interventions allow us to test whether performance gains arise from the actual semantics of condensed experience. More detailed examples and the rationale behind these intervention designs can be found in Appendix [D](https://arxiv.org/html/2601.22436v2#A4 "Appendix D Details of Intervention Design ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

Figure 2: Intervention results on the ExpeL framework (offline, single-agent) using GPT-4o across three benchmarks. ExpeL consistently relies more on raw trajectories, while showing weak or inconsistent sensitivity to condensed summaries.

Figure 3: Intervention results on the Dynamic CheatSheet (DC-RS) framework (online, single-agent) using GPT-4o. Raw experience perturbations significantly reduce performance, whereas condensed experience manipulations often have negligible impact.

Figure 4: Impact of condensed experience interventions on the ReasoningBank framework (online, single-agent) using Gemini-2.5-Flash across four WebArena sub-tasks. Despite the absence of raw experience, agents show only mild sensitivity to semantic manipulations of condensed experience, indicating limited semantic faithfulness.

Figure 5: Faithfulness interventions on the G-Memory framework (online, multi-agent) with GPT-4o-mini. Agents access two forms of raw experience (reference and execution) and one form of condensed experience.

## 4 Evaluation of Experience Faithfulness

### 4.1 Faithfulness under Joint Raw & Condensed Access

We begin by examining settings where both raw and condensed experiences are simultaneously provided to the agent. Figure [2](https://arxiv.org/html/2601.22436v2#S3.F2 "Figure 2 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") reports results in the offline ExpeL framework, while Figure [3](https://arxiv.org/html/2601.22436v2#S3.F3 "Figure 3 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") shows online performance using the Dynamic CheatSheet setup. Additional results from Qwen3-235B-A22B are included in Appendix [E.1](https://arxiv.org/html/2601.22436v2#A5.SS1 "E.1 Additional Results on Qwen3-235B-A22B with ExpeL ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), affirming the consistency of our conclusions across model architectures. This setting provides our first set of faithfulness insights.

Faithfulness to raw experience is strong and robust.
Across both frameworks, we find that removing raw experience (w/o Raw Exp.) reliably causes substantial performance degradation on most tasks, demonstrating that raw experience is indeed a primary contributor to performance. Perturbing raw trajectories, particularly through Empty or Irrelevant replacements, produces similarly severe declines. These results indicate that agents truly leverage the semantic and temporal structure encoded in raw trajectories.

Condensed experience often has minimal behavioral influence.
In contrast, most interventions on condensed experience lead to little or no change in behavior. Across both frameworks and nearly all tasks, perturbations such as Corrupt, Irrelevant, and Filler yield performance that is nearly indistinguishable from the unperturbed baseline. Likewise, even removing condensed experience altogether (w/o Condensed) has only marginal impact. These patterns suggest that agents either struggle to interpret condensed summaries or simply do not rely on them during decision-making—despite their explicit presence in the input. Taken together, this reveals a serious faithfulness gap in how agents purportedly “use” condensed experience.

Consistent patterns across offline and online paradigms.
Notably, these phenomena hold across both offline (ExpeL) and online (Dynamic CheatSheet) self‑evolving paradigms. Despite their different mechanisms for experience accumulation, the resulting faithfulness patterns remain strikingly similar. In both cases, agents strongly depend on raw trajectories while exhibiting weak or inconsistent reliance on condensed summaries. This consistency across paradigms underscores that the faithfulness gap is a fundamental property of current self‑evolving designs, rather than an artifact of a specific memory-update strategy.

Task-specific characteristics modulate experience sensitivity.
We observe that in certain knowledge-intensive tasks such as GPQA-Diamond and MMLU-Pro Eng., the agent exhibits comparable sensitivity to both raw and condensed experience. This suggests that task type or structure may affect how different forms of experience are utilized, a phenomenon we discuss further in §[5.3](https://arxiv.org/html/2601.22436v2#S5.SS3 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

### 4.2 Faithfulness under Condensed-Only Input

Given that agents exhibit stronger faithfulness to raw experiences than condensed ones, a natural follow-up question arises: *Is this lack of faithfulness to condensed experiences due to the presence of raw experience overshadowing it?* To isolate this effect, we examine the ReasoningBank framework, which provides *only condensed experience* and contains no raw trajectories. This setting enables a clean assessment of whether agents meaningfully rely on condensed summaries when no richer experience is available.

Condensed experience improves performance, but not through faithful utilization.
As shown in Figure [4](https://arxiv.org/html/2601.22436v2#S3.F4 "Figure 4 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), removing condensed experience (w/o Condensed Exp.) leads to consistent performance drops across all four WebArena tasks, indicating that even in the absence of raw trajectories, condensed summaries provide useful guidance that agents can leverage to improve their behavior.

However, this utility does not imply faithful grounding. The agent’s responses remain surprisingly insensitive to semantic perturbations: interventions such as Corrupt, Irrelevant, and even Filler lead to only negligible degradation or even slight improvements.

These results suggest that while condensed experience does contribute to task success, the agent does not rely on its actual content in a faithful manner. Instead, performance gains may stem from superficial features, such as the presence of a text block or stylistic patterns (Empty), rather than genuine semantic grounding. We delve deeper into this phenomenon and its underlying causes in §[5](https://arxiv.org/html/2601.22436v2#S5 "5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

Similar trends hold across other model families.
We further replicate this evaluation using smaller models, Qwen3-14B and Qwen3-32B, on the same ReasoningBank setup. As detailed in Appendix [E.2](https://arxiv.org/html/2601.22436v2#A5.SS2 "E.2 Additional Results on Condensed-Only Setting: ReasoningBank ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), we observe similar patterns: semantic perturbations still fail to consistently degrade success rates. This suggests that the limited faithfulness to condensed knowledge is a general behavioral tendency.

Figure 6: Model-scale-wise analysis of intervention sensitivity across six Qwen3 models (1.7B to 32B) with ExpeL.

### 4.3 Faithfulness under Multi-Agent Scenario

To further assess whether our conclusions hold in collaborative multi-agent settings, we evaluate the G-Memory framework. Results under the GPT-4o-mini backbone are shown in Figure [5](https://arxiv.org/html/2601.22436v2#S3.F5 "Figure 5 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"). Complementary experiments based on Qwen3-235B-A22B are presented in Appendix [E.3](https://arxiv.org/html/2601.22436v2#A5.SS3 "E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), showing highly consistent trends across models.

Raw experience from both sources is faithfully utilized.
G-Memory accumulates two types of raw experience: (1) Reference Raw Experience (Ref-Raw Exp.), curated trajectories collected offline, and (2) Execution Raw Experience (Exe-Raw Exp.), accumulated autonomously during agent operation. In Figure [5](https://arxiv.org/html/2601.22436v2#S3.F5 "Figure 5 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), we find that perturbing either type consistently results in obvious performance degradation on ALFWorld, confirming that both human-curated and self-collected raw experiences are faithfully utilized by the agent.

Condensed experience remains fragile.
Consistent with our earlier findings, perturbations to the condensed experience yield only marginal effects. This further reinforces our central conclusion: although condensed experience can offer some utility, agents seldom anchor their decision-making process in its underlying semantics.

Faithfulness inconsistencies persist in knowledge reasoning tasks.
However, in knowledge-grounded tasks such as FEVER, the impact of raw experience perturbation is less pronounced. This mirrors prior trends in GPQA-Diamond and MMLU-Pro Eng., where raw and condensed experience yield more comparable influence. We provide a detailed diagnosis of these task-dependent effects in §[5.3](https://arxiv.org/html/2601.22436v2#S5.SS3 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

### 4.4 Faithfulness under Model Scaling

Finally, we ask whether scaling model size improves the degree to which agents faithfully rely on provided experience. Using the ExpeL framework, we conduct controlled interventions across six Qwen3 variants (from 1.7B to 32B parameters), shown in Figure [6](https://arxiv.org/html/2601.22436v2#S4.F6 "Figure 6 ‣ 4.2 Faithfulness under Condensed-Only Input ‣ 4 Evaluation of Experience Faithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

Larger models perform better, but the faithfulness gap remains.
As expected, scaling improves unperturbed success rates. Yet perturbation results show that, even at larger scales, models remain markedly more faithful to raw experience than to condensed representations.

Raw experience is faithfully exploited, whereas condensed experience is not.
Across all scales, perturbing raw experience causes pronounced degradation, confirming that agents rely on the semantic and temporal structure of raw trajectories during inference. In contrast, replacing condensed experience with Corrupt, Irrelevant, or Filler yields only minimal changes.

These findings suggest that while parameter scaling enhances performance, it does not inherently resolve the core challenge of experience faithfulness.

## 5 The Cause of Unfaithfulness

In this section, we trace the cause of such counterintuitive unfaithfulness through the three foundational components of any self‑evolving system: the experience itself (§[5.1](https://arxiv.org/html/2601.22436v2#S5.SS1 "5.1 Semantic Limitations of Condensed Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")), the backbone model that processes it (§[5.2](https://arxiv.org/html/2601.22436v2#S5.SS2 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")), and the task environment in which the agent operates (§[5.3](https://arxiv.org/html/2601.22436v2#S5.SS3 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")).

### 5.1 Semantic Limitations of Condensed Experience

We first examine the role of the experience itself. A surprising observation from our interventions is that agents sometimes perform better when condensed experience is perturbed or removed. This suggests that condensed summaries may be uninformative or misaligned. To investigate this possibility, we analyze cases where the agent *succeeds without* condensed experience but *fails when* it is added. As shown in Table [1](https://arxiv.org/html/2601.22436v2#S5.T1 "Table 1 ‣ 5.1 Semantic Limitations of Condensed Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), most failures fall into three categories:

Distraction from the task goal.
Condensed summaries can redirect the agent toward tasks implied by the retrieved heuristics rather than the actual user intent, leading to unnecessary detours or complete drift from the target. This is especially common for smaller models, where high-level heuristics easily override task grounding.

Overreliance on incorrect priors.
Condensed experience often encodes assumptions about element types, layouts, or workflows that do not match the current state. Agents may rigidly follow these outdated patterns instead of inspecting the live page, resulting in invalid or misplaced actions.

Premature inference from prior patterns.
Agents frequently jump to conclusions when summaries suggest that certain items “should” exist or actions “should” work, causing them to skip verification steps or terminate early. This mode is typical in models with strong semantic priors.

Overall, these failure modes indicate that condensed experience, when overly abstract, generic, or mismatched, can mislead agents by reinforcing ungrounded assumptions rather than aiding decision-making. Representative cases for each failure mode are provided in Appendix [E.4](https://arxiv.org/html/2601.22436v2#A5.SS4 "E.4 Representative Failure Cases for Condensed Experience ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

Table 1: Error distribution for ReasoningBank on WebArena when the agent succeeds without condensed experience but fails with it.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Distraction(%) | Reliance(%) | Premature(%) |
| Gemini-2.5-Flash | | | |
| Shopping | 45.2 | 32.3 | 22.6 |
| CMS | 40.9 | 27.3 | 31.8 |
| Reddit | 26.7 | 33.3 | 40.0 |
| Map | 18.8 | 31.3 | 50.0 |
| Qwen3-32B | | | |
| Shopping | 79.2 | 8.3 | 12.5 |
| CMS | 75.0 | 12.5 | 12.5 |
| Reddit | 61.9 | 9.5 | 28.6 |
| Map | 74.1 | 11.1 | 14.8 |
| Qwen3-14B | | | |
| Shopping | 74.3 | 11.4 | 14.3 |
| CMS | 86.7 | 6.7 | 6.7 |
| Reddit | 60.9 | 0 | 39.1 |
| Map | 72.7 | 9.1 | 18.2 |

(a) Baseline without intervention.

(b) Corrupt intervention.

(c) Irrelevant intervention.

Figure 7: Layer-wise Integrated Gradients attribution under the ExpeL framework using Qwen3-32B. Prompts are divided into four segments: System Instruction, Condensed Experience, Raw Experience, and Current Trajectory.

### 5.2 Suppression by Internal Biases

Beyond the semantic limitations, unfaithfulness may also arise from internal processing biases that prevent the agent from effectively using retrieved memory. To examine this possibility, we analyze how information from different prompt segments propagates through the backbone’s layers and contributes to predictions (Simonyan et al., [2013](https://arxiv.org/html/2601.22436v2#bib.bib38 "Deep inside convolutional networks: visualising image classification models and saliency maps")).

Probing Method.
We apply Integrated Gradients (IG) (Wang et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib39 "Label words are anchors: an information flow perspective for understanding in-context learning"); Tang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib40 "Revisiting long-context modeling from context denoising perspective")) to quantify how much each prompt segment influences the model’s output. For the hh‑th head in layer ll, we compute:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | IGh,l\displaystyle\mathrm{IG}\_{h,l} | =Ah,lT⊙|∂ℒθ​(Y|X)∂Ah,l|,\displaystyle=A\_{h,l}^{T}\odot\left|\frac{\partial\mathcal{L}\_{\theta}(Y|X)}{\partial A\_{h,l}}\right|, |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | IGh,l(r)\displaystyle\mathrm{IG}^{(r)}\_{h,l} | =1|𝒯s|​∑xi∈𝒯s∑yj∈YIGh,l​[i,j].\displaystyle=\frac{1}{|\mathcal{T}\_{s}|}\sum\limits\_{x\_{i}\in\mathcal{T}\_{s}}\sum\limits\_{y\_{j}\in Y}\mathrm{IG}\_{h,l}[i,j]. |  | (2) |

where 𝒯s\mathcal{T}\_{s} denotes a specific prompt segment and IGh,l​[i,j]\mathrm{IG}\_{h,l}[i,j] measures how token xix\_{i} influences token yjy\_{j}. We then aggregate IGh,l(r)\mathrm{IG}^{(r)}\_{h,l} over all heads and layers to derive a global attribution score IG(r)\mathrm{IG}^{(r)}, which captures the segment’s overall influence on the model’s prediction. A low score suggests that the model largely disregards this segment.

We perform this analysis under the ExpeL framework with Qwen3-series models, segmenting each prompt into: (1) System Instruction, (2) Condensed Experience, (3) Raw Experience, and (4) Current Trajectory.

Results & Analysis. Figure [7](https://arxiv.org/html/2601.22436v2#S5.F7 "Figure 7 ‣ 5.1 Semantic Limitations of Condensed Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") shows results on ALFWorld using Qwen3-32B under three conditions: no intervention, Corrupt, and Irrelevant. Detailed settings and additional results on model sizes and interventions are provided in Appendix [E.5](https://arxiv.org/html/2601.22436v2#A5.SS5 "E.5 Additional IG Attribution Results ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"). Three consistent patterns emerge:

Condensed experience remains underutilized. In all three settings, the IG scores attributed to condensed experience remain consistently low across layers, suggesting limited integration of such inputs regardless of their semantic quality.

Raw experience shows stable faithful usage. Despite the low influence of condensed content, raw experience maintains a moderate and stable contribution, further supporting our earlier findings of its reliable utilization.

Current trajectory dominates later layers. The most significant attribution consistently comes from the current trajectory segment, highlighting a strong local-context bias in prediction (Li et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib41 "Compressing context to enhance inference efficiency of large language models"); An et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib42 "Make your llm fully utilize the context")).

In summary, these trends suggest that even when presented with semantically rich (or intervened) summaries, condensed experience struggles to influence downstream behavior due to structural biases in the model’s attention flow.

### 5.3 Task-Specific Dependence on Experience

Finally, we analyze whether the task environment itself reduces the need for external experience. Many benchmarks in which agents exhibit low sensitivity to interventions, such as HotpotQA, GPQA, MMLU, and FEVER, primarily involve knowledge-intensive question answering. In these tasks, pretrained models already possess substantial factual knowledge and strong semantic priors (Shi et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib21 "Why larger language models do in-context learning differently?")), leaving retrieved experience with limited marginal value.

To further verify this, we evaluate two multi-hop question answering benchmarks: 2WikiMultiHopQA (Ho et al., [2020](https://arxiv.org/html/2601.22436v2#bib.bib43 "Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps")) and Musique (Trivedi et al., [2022](https://arxiv.org/html/2601.22436v2#bib.bib44 "MuSiQue: multihop questions via single-hop question composition")). We apply interventions on ExpeL with Qwen3-32B and results are shown in Table [2](https://arxiv.org/html/2601.22436v2#S5.T2 "Table 2 ‣ 5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"). Each benchmark contributes 100 sampled examples, and we report exact match as the evaluation metric. More results on Qwen3-14B are in Appendix [E.6](https://arxiv.org/html/2601.22436v2#A5.SS6 "E.6 Additional Task-Specific Dependence Results ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

The results demonstrate that agents still exhibit limited faithfulness to both raw and condensed experience.
This suggests that the utility of experience is highly task-dependent: when a task can be handled with the agent’s innate knowledge, the retrieved experience contributes little and thus fails to exert meaningful causal influence.

Table 2: Intervention results on two multi-hop question answering tasks under the ExpeL framework with Qwen3-32B backbone. The evaluation metric is exact match.

|  |  |  |
| --- | --- | --- |
|  | 2Wiki-MultiHopQA | Musique |
| ExpeL | 62 | 48 |
| Raw Experience Intervention | | |
| Empty | 65 | 43 |
| Shuffle | 63 | 46 |
| Irrelevant | 63 | 47 |
| Condensed Experience Intervention | | |
| Empty | 63 | 47 |
| Corrupt | 64 | 44 |
| Irrelevant | 65 | 45 |
| Filler | 64 | 45 |

## 6 Related Works

Experience-Driven Self-Evolving Agents. Recent advances in self-evolving agents can be broadly categorized into two paradigms based on how experience is collected and utilized: offline and online approaches (Liu et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib58 "Contextual experience replay for self-improvement of language agents")).

Offline self-evolving agents construct memory from pre-collected datasets and utilize it in a fixed form during inference (Li and Qiu, [2023](https://arxiv.org/html/2601.22436v2#bib.bib59 "MoT: memory-of-thought enables chatgpt to self-improve"); Yang et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib61 "Failures pave the way: enhancing large language models through tuning-free rule accumulation"); Zhong et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib60 "Memorybank: enhancing large language models with long-term memory"); Zhao et al., [2024a](https://arxiv.org/html/2601.22436v2#bib.bib12 "Expel: llm agents are experiential learners"); Fu et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib62 "Autoguide: automated generation and selection of context-aware guidelines for large language model agents"); Zhou et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib23 "Memento: fine-tuning llm agents without fine-tuning llms"); Yang et al., [2025b](https://arxiv.org/html/2601.22436v2#bib.bib63 "Coarse-to-fine grounded memory for llm agent planning")). Representative systems such ExpeL rely on pre-stored examples of successful trajectories and distilled insights without memory updates at test time.

In contrast, online paradigms allow experience memory to evolve through interaction: agents dynamically accumulate, retrieve, and refine experiences during deployment (Chen et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib64 "Automanual: constructing instruction manuals by llm agents via interactive environmental learning"); Zhang et al., [2025c](https://arxiv.org/html/2601.22436v2#bib.bib22 "Agentic context engineering: evolving contexts for self-improving language models"); Suzgun et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib24 "Dynamic cheatsheet: test-time learning with adaptive memory")). For instance, ReasoningBank (Ouyang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib14 "Reasoningbank: scaling agent self-evolving with reasoning memory")) continuously distills reasoning patterns from recent episodes to enrich future responses. G-Memory (Zhang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib15 "G-memory: tracing hierarchical memory for multi-agent systems")) further extends this paradigm to multi-agent settings.

While these methods offer promising pathways for autonomous improvement, little attention has been paid to whether agents faithfully rely on the retrieved experiences—a gap our work aims to address.

Faithfulness of Language Models. Early studies on faithfulness focus on in-context learning of LMs, where the goal is to assess whether LMs genuinely leveraged human-curated in-context examples to guide their predictions (Min et al., [2022](https://arxiv.org/html/2601.22436v2#bib.bib51 "Rethinking the role of demonstrations: what makes in-context learning work?"); Ye and Durrett, [2022](https://arxiv.org/html/2601.22436v2#bib.bib50 "The unreliability of explanations in few-shot prompting for textual reasoning"); Shi et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib21 "Why larger language models do in-context learning differently?")). With the emergence of chain-of-thought (CoT) prompting (Wei et al., [2022](https://arxiv.org/html/2601.22436v2#bib.bib52 "Chain-of-thought prompting elicits reasoning in large language models")), attention shift to the faithfulness of the reasoning process itself. A key line of research investigates whether the generated CoT rationale truly reflects the model’s internal decision-making, or merely serves as a post-hoc justification (Lanham et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib53 "Measuring faithfulness in chain-of-thought reasoning"); Turpin et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib54 "Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting"); Arcuschin et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib55 "Chain-of-thought reasoning in the wild is not always faithful"); Lewis-Lim et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib56 "Analysing chain of thought dynamics: active guidance or unfaithful post-hoc rationalisation?"); Chen et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib57 "Reasoning models don’t always say what they think")).
In contrast, we study faithfulness in self-evolving agentic settings, where experience is both dynamic and multifaceted, revealing emerging phenomena beyond static prompt usage.

## 7 Conclusion

This work provides the first comprehensive assessment of whether self-evolving LLM agents faithfully rely on the experiences they accumulate. Through controlled interventions across raw and condensed experience, we reveal a persistent and systematic gap: agents reliably depend on raw trajectories but frequently overlook or misinterpret condensed summaries. Our deeper analysis attributes this unfaithfulness to the limited specificity of condensed content, internal processing biases of backbone, and task regimes where pretrained priors alone suffice. These findings call for future agents to incorporate experience in a way that is not only effective but also faithfully grounded.

## Impact Statement

This work provides the first systematic investigation into the faithfulness of experience utilization in self-evolving LLM agents. Our findings reveal a persistent and overlooked asymmetry: while agents reliably exploit raw experience, they frequently neglect or misinterpret condensed experience—even when it is the only form of guidance available. These results call into question common assumptions underlying memory-based adaptation and raise important considerations for future development of reliable and controllable agents, especially in high-stakes environments.

Our analysis offers two concrete design takeaways for future self-evolving systems. First, it highlights the importance of carefully designing the content structure of condensed experience. Rather than abstract summaries or generic advice, effective condensed experience should be contextualized, task-relevant, and cognitively actionable. This finding resonates with the concept of context engineering (Mei et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib66 "A survey of context engineering for large language models"); Hua et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib65 "Context engineering 2.0: the context of context engineering")), which reveals that the contextual inputs play a pivotal role in shaping agent behavior. Condensed experience, as a core component of this context, must therefore be engineered with equal care—not only to compress, but to preserve and transmit behavioral utility. This opens up promising directions for automatic condensation methods that optimize for alignment and usability, rather than surface brevity alone (Zhai et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib67 "Agentevolver: towards efficient self-evolving agent system")).

Second, our findings emphasize the need to rethink the timing of experience integration. Static prepending of memory to the input—irrespective of task, timing, or agent state—can lead to underutilization or even performance degradation. Instead, experience should be retrieved and injected dynamically, based on task demands, interaction history, and internal model uncertainty. Moreover, agents may not need experience for every task; indiscriminate use can dilute attention and reduce effectiveness. Incorporating experience as a situationally-aware, interactively-triggered signal holds promise for more faithful and efficient adaptation (Jin et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib69 "Search-r1: training llms to reason and leverage search engines with reinforcement learning"); Zhang et al., [2025d](https://arxiv.org/html/2601.22436v2#bib.bib68 "Memory as action: autonomous context curation for long-horizon agentic tasks")).

Together, these insights lay the groundwork for a new generation of self-evolving agents that are not only capable of learning from experience, but doing so in a manner that is faithful and behaviorally grounded.

## References

* S. An, Z. Ma, Z. Lin, N. Zheng, J. Lou, and W. Chen (2024)
  Make your llm fully utilize the context.
  Advances in Neural Information Processing Systems 37,  pp. 62160–62188.
  Cited by: [§5.2](https://arxiv.org/html/2601.22436v2#S5.SS2.p7.1 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* I. Arcuschin, J. Janiak, R. Krzyzanowski, S. Rajamanoharan, N. Nanda, and A. Conmy (2025)
  Chain-of-thought reasoning in the wild is not always faithful.
  In Workshop on Reasoning and Planning for Large Language Models,
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* J. Bell, L. Quarantiello, E. N. Coleman, L. Li, M. Li, M. Madeddu, E. Piccoli, and V. Lomonaco (2025)
  The future of continual learning in the era of foundation models: three key directions.
  arXiv preprint arXiv:2506.03320.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Cai, Y. Hao, J. Zhou, H. Yan, Z. Lei, R. Zhen, Z. Han, Y. Yang, J. Li, Q. Pan, et al. (2025)
  Building self-evolving agents via experience-driven lifelong learning: a framework and benchmark.
  arXiv preprint arXiv:2508.19005.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. Chen, Y. Li, Y. Yang, S. Yu, B. Lin, and X. He (2024)
  Automanual: constructing instruction manuals by llm agents via interactive environmental learning.
  Advances in Neural Information Processing Systems 37,  pp. 589–631.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p3.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Chen, J. Benton, A. Radhakrishnan, J. Uesato, C. Denison, J. Schulman, A. Somani, P. Hase, M. Wagner, F. Roger, et al. (2025)
  Reasoning models don’t always say what they think.
  arXiv preprint arXiv:2505.05410.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025)
  Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities.
  arXiv preprint arXiv:2507.06261.
  Cited by: [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* T. L. S. de Chezelles, M. Gasse, A. Lacoste, M. Caccia, A. Drouin, L. Boisvert, M. Thakkar, T. Marty, R. Assouel, S. O. Shayegan, et al. (2025)
  The browsergym ecosystem for web agent research.
  Transactions on Machine Learning Research.
  Cited by: [1st item](https://arxiv.org/html/2601.22436v2#A2.I4.i1.p1.1 "In B.4 Web Interaction ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Dou, M. Zhang, C. Huang, J. Chen, F. Chen, S. Liu, Y. Liu, C. Liu, C. Zhong, Z. Zhang, et al. (2025)
  Evalearn: quantifying the learning capability and efficiency of llms via sequential problem solving.
  arXiv preprint arXiv:2506.02672.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Fu, D. Kim, J. Kim, S. Sohn, L. Logeswaran, K. Bae, and H. Lee (2024)
  Autoguide: automated generation and selection of context-aware guidelines for large language model agents.
  Advances in Neural Information Processing Systems 37,  pp. 119919–119948.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* H. Gao, J. Geng, W. Hua, M. Hu, X. Juan, H. Liu, S. Liu, J. Qiu, X. Qi, Y. Wu, et al. (2025)
  A survey of self-evolving agents: on path to artificial super intelligence.
  arXiv preprint arXiv:2507.21046.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§2](https://arxiv.org/html/2601.22436v2#S2.p1.1 "2 Preliminaries ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* D. Hendrycks, D. Song, C. Szegedy, H. Lee, Y. Gal, E. Brynjolfsson, S. Li, A. Zou, L. Levine, B. Han, et al. (2025)
  A definition of agi.
  arXiv preprint arXiv:2510.18212.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* X. Ho, A. D. Nguyen, S. Sugawara, and A. Aizawa (2020)
  Constructing a multi-hop qa dataset for comprehensive evaluation of reasoning steps.
  In Proceedings of the 28th International Conference on Computational Linguistics,
   pp. 6609–6625.
  Cited by: [§5.3](https://arxiv.org/html/2601.22436v2#S5.SS3.p2.1 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Hu, S. Liu, Y. Yue, G. Zhang, B. Liu, F. Zhu, J. Lin, H. Guo, S. Dou, Z. Xi, et al. (2025)
  Memory in the age of ai agents.
  arXiv preprint arXiv:2512.13564.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p2.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Q. Hua, L. Ye, D. Fu, Y. Xiao, X. Cai, Y. Wu, J. Lin, J. Wang, and P. Liu (2025)
  Context engineering 2.0: the context of context engineering.
  arXiv preprint arXiv:2510.26493.
  Cited by: [Impact Statement](https://arxiv.org/html/2601.22436v2#Sx1.p2.1 "Impact Statement ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. (2024)
  Gpt-4o system card.
  arXiv preprint arXiv:2410.21276.
  Cited by: [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* B. Jin, H. Zeng, Z. Yue, J. Yoon, S. Arik, D. Wang, H. Zamani, and J. Han (2025)
  Search-r1: training llms to reason and leverage search engines with reinforcement learning.
  arXiv preprint arXiv:2503.09516.
  Cited by: [Impact Statement](https://arxiv.org/html/2601.22436v2#Sx1.p3.1 "Impact Statement ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica (2023)
  Efficient memory management for large language model serving with pagedattention.
  In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles,
  Cited by: [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p4.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, C. Denison, D. Hernandez, D. Li, E. Durmus, E. Hubinger, J. Kernion, et al. (2023)
  Measuring faithfulness in chain-of-thought reasoning.
  arXiv preprint arXiv:2307.13702.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Lewis-Lim, X. Tan, Z. Zhao, and N. Aletras (2025)
  Analysing chain of thought dynamics: active guidance or unfaithful post-hoc rationalisation?.
  In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
   pp. 29826–29841.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* X. Li and X. Qiu (2023)
  MoT: memory-of-thought enables chatgpt to self-improve.
  In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
   pp. 6354–6374.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Li, B. Dong, F. Guerin, and C. Lin (2023)
  Compressing context to enhance inference efficiency of large language models.
  In Proceedings of the 2023 conference on empirical methods in natural language processing,
   pp. 6342–6353.
  Cited by: [§5.2](https://arxiv.org/html/2601.22436v2#S5.SS2.p7.1 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Liu, C. Si, K. R. Narasimhan, and S. Yao (2025)
  Contextual experience replay for self-improvement of language agents.
  In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 14179–14198.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p1.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* L. Mei, J. Yao, Y. Ge, Y. Wang, B. Bi, Y. Cai, J. Liu, M. Li, Z. Li, D. Zhang, et al. (2025)
  A survey of context engineering for large language models.
  arXiv preprint arXiv:2507.13334.
  Cited by: [Impact Statement](https://arxiv.org/html/2601.22436v2#Sx1.p2.1 "Impact Statement ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Min, X. Lyu, A. Holtzman, M. Artetxe, M. Lewis, H. Hajishirzi, and L. Zettlemoyer (2022)
  Rethinking the role of demonstrations: what makes in-context learning work?.
  In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing,
   pp. 11048–11064.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. A. Mohsin, M. Umer, A. Bilal, Z. Memon, M. I. Qadir, S. Bhattacharya, H. Rizwan, A. R. Gorle, M. Z. Kazmi, A. Mohsin, et al. (2025)
  On the fundamental limits of llms at scale.
  arXiv preprint arXiv:2511.12869.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p5.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Ouyang, J. Yan, I. Hsu, Y. Chen, K. Jiang, Z. Wang, R. Han, L. T. Le, S. Daruki, X. Tang, et al. (2025)
  Reasoningbank: scaling agent self-evolving with reasoning memory.
  arXiv preprint arXiv:2509.25140.
  Cited by: [Appendix A](https://arxiv.org/html/2601.22436v2#A1.p1.1 "Appendix A Self-Evolving Agents ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [3rd item](https://arxiv.org/html/2601.22436v2#A3.I1.i3.p1.1 "In Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§1](https://arxiv.org/html/2601.22436v2#S1.p2.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§1](https://arxiv.org/html/2601.22436v2#S1.p3.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p1.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§6](https://arxiv.org/html/2601.22436v2#S6.p3.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman (2024)
  Gpqa: a graduate-level google-proof q&a benchmark.
  In First Conference on Language Modeling,
  Cited by: [3rd item](https://arxiv.org/html/2601.22436v2#A2.I1.i3.p1.1 "In B.1 Knowledge-Intensive Question Answering ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Z. Shi, J. Wei, Z. Xu, and Y. Liang (2024)
  Why larger language models do in-context learning differently?.
  In Proceedings of the 41st International Conference on Machine Learning,
   pp. 44991–45013.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p5.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§5.3](https://arxiv.org/html/2601.22436v2#S5.SS3.p1.1 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao (2023)
  Reflexion: language agents with verbal reinforcement learning.
  Advances in Neural Information Processing Systems 36,  pp. 8634–8652.
  Cited by: [2nd item](https://arxiv.org/html/2601.22436v2#A2.I4.i2.p1.1 "In B.4 Web Interaction ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. Shridhar, J. Thomason, D. Gordon, Y. Bisk, W. Han, R. Mottaghi, L. Zettlemoyer, and D. Fox (2020)
  Alfred: a benchmark for interpreting grounded instructions for everyday tasks.
  In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition,
   pp. 10740–10749.
  Cited by: [1st item](https://arxiv.org/html/2601.22436v2#A2.I3.i1.p1.1 "In B.3 Embodied Action ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. Shridhar, X. Yuan, M. Cote, Y. Bisk, A. Trischler, and M. Hausknecht (2021)
  ALFWorld: aligning text and embodied environments for interactive learning.
  In International Conference on Learning Representations,
  Cited by: [1st item](https://arxiv.org/html/2601.22436v2#A2.I3.i1.p1.1 "In B.3 Embodied Action ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* D. Silver and R. S. Sutton (2025)
  Welcome to the era of experience.
  Google AI 1.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* K. Simonyan, A. Vedaldi, and A. Zisserman (2013)
  Deep inside convolutional networks: visualising image classification models and saliency maps.
  arXiv preprint arXiv:1312.6034.
  Cited by: [§5.2](https://arxiv.org/html/2601.22436v2#S5.SS2.p1.1 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. Suzgun and A. T. Kalai (2024)
  Meta-prompting: enhancing language models with task-agnostic scaffolding.
  arXiv preprint arXiv:2401.12954.
  Cited by: [2nd item](https://arxiv.org/html/2601.22436v2#A2.I2.i2.p1.1 "In B.2 Mathematical Reasoning ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. Suzgun, M. Yuksekgonul, F. Bianchi, D. Jurafsky, and J. Zou (2025)
  Dynamic cheatsheet: test-time learning with adaptive memory.
  arXiv preprint arXiv:2504.07952.
  Cited by: [Appendix A](https://arxiv.org/html/2601.22436v2#A1.p1.1 "Appendix A Self-Evolving Agents ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [2nd item](https://arxiv.org/html/2601.22436v2#A3.I1.i2.p1.1 "In Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p1.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§6](https://arxiv.org/html/2601.22436v2#S6.p3.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Z. Tang, B. Ji, J. Li, L. Wu, H. Gui, and M. Zhang (2025)
  Revisiting long-context modeling from context denoising perspective.
  arXiv preprint arXiv:2510.05862.
  Cited by: [§E.5](https://arxiv.org/html/2601.22436v2#A5.SS5.p1.1 "E.5 Additional IG Attribution Results ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§5.2](https://arxiv.org/html/2601.22436v2#S5.SS2.p2.2 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* J. Thorne, A. Vlachos, C. Christodoulopoulos, and A. Mittal (2018)
  FEVER: a large-scale dataset for fact extraction and verification.
  In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers),
   pp. 809–819.
  Cited by: [2nd item](https://arxiv.org/html/2601.22436v2#A2.I1.i2.p1.1 "In B.1 Knowledge-Intensive Question Answering ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* H. Trivedi, N. Balasubramanian, T. Khot, and A. Sabharwal (2022)
  MuSiQue: multihop questions via single-hop question composition.
  Transactions of the Association for Computational Linguistics 10,  pp. 539–554.
  Cited by: [§5.3](https://arxiv.org/html/2601.22436v2#S5.SS3.p2.1 "5.3 Task-Specific Dependence on Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* M. Turpin, J. Michael, E. Perez, and S. Bowman (2023)
  Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting.
  Advances in Neural Information Processing Systems 36,  pp. 74952–74965.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* L. Wang, L. Li, D. Dai, D. Chen, H. Zhou, F. Meng, J. Zhou, and X. Sun (2023)
  Label words are anchors: an information flow perspective for understanding in-context learning.
  In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
   pp. 9840–9855.
  Cited by: [§E.5](https://arxiv.org/html/2601.22436v2#A5.SS5.p1.1 "E.5 Additional IG Attribution Results ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§5.2](https://arxiv.org/html/2601.22436v2#S5.SS2.p2.2 "5.2 Suppression by Internal Biases ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, et al. (2024)
  Mmlu-pro: a more robust and challenging multi-task language understanding benchmark.
  Advances in Neural Information Processing Systems 37,  pp. 95266–95290.
  Cited by: [4th item](https://arxiv.org/html/2601.22436v2#A2.I1.i4.p1.1 "In B.1 Knowledge-Intensive Question Answering ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Z. Z. Wang, J. Mao, D. Fried, and G. Neubig (2025)
  Agent workflow memory.
  In Forty-second International Conference on Machine Learning,
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p2.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. (2022)
  Chain-of-thought prompting elicits reasoning in large language models.
  Advances in neural information processing systems 35,  pp. 24824–24837.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025a)
  Qwen3 technical report.
  arXiv preprint arXiv:2505.09388.
  Cited by: [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p2.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* W. Yang, J. Xiao, H. Zhang, Q. Zhang, Y. Wang, and B. Xu (2025b)
  Coarse-to-fine grounded memory for llm agent planning.
  In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
   pp. 13040–13067.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Z. Yang, P. Li, and Y. Liu (2023)
  Failures pave the way: enhancing large language models through tuning-free rule accumulation.
  In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
   pp. 1751–1777.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. Cohen, R. Salakhutdinov, and C. D. Manning (2018)
  HotpotQA: a dataset for diverse, explainable multi-hop question answering.
  In Proceedings of the 2018 conference on empirical methods in natural language processing,
   pp. 2369–2380.
  Cited by: [1st item](https://arxiv.org/html/2601.22436v2#A2.I1.i1.p1.1 "In B.1 Knowledge-Intensive Question Answering ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Yao, H. Chen, J. Yang, and K. Narasimhan (2022)
  Webshop: towards scalable real-world web interaction with grounded language agents.
  Advances in Neural Information Processing Systems 35,  pp. 20744–20757.
  Cited by: [2nd item](https://arxiv.org/html/2601.22436v2#A2.I4.i2.p1.1 "In B.4 Web Interaction ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, and K. Narasimhan (2023a)
  Tree of thoughts: deliberate problem solving with large language models.
  Advances in neural information processing systems 36,  pp. 11809–11822.
  Cited by: [2nd item](https://arxiv.org/html/2601.22436v2#A2.I2.i2.p1.1 "In B.2 Mathematical Reasoning ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and Y. Cao (2023b)
  React: synergizing reasoning and acting in language models.
  In The eleventh international conference on learning representations,
  Cited by: [2nd item](https://arxiv.org/html/2601.22436v2#A2.I4.i2.p1.1 "In B.4 Web Interaction ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.2](https://arxiv.org/html/2601.22436v2#S3.SS2.p1.1 "3.2 Raw Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* X. Ye and G. Durrett (2022)
  The unreliability of explanations in few-shot prompting for textual reasoning.
  Advances in neural information processing systems 35,  pp. 30378–30392.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p5.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Zhai, S. Tao, C. Chen, A. Zou, Z. Chen, Q. Fu, S. Mai, L. Yu, J. Deng, Z. Cao, et al. (2025)
  Agentevolver: towards efficient self-evolving agent system.
  arXiv preprint arXiv:2511.10395.
  Cited by: [Impact Statement](https://arxiv.org/html/2601.22436v2#Sx1.p2.1 "Impact Statement ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* G. Zhang, M. Fu, G. Wan, M. Yu, K. Wang, and S. Yan (2025a)
  G-memory: tracing hierarchical memory for multi-agent systems.
  arXiv preprint arXiv:2506.07398.
  Cited by: [Appendix A](https://arxiv.org/html/2601.22436v2#A1.p1.1 "Appendix A Self-Evolving Agents ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [4th item](https://arxiv.org/html/2601.22436v2#A3.I1.i4.p1.1 "In Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§1](https://arxiv.org/html/2601.22436v2#S1.p2.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§1](https://arxiv.org/html/2601.22436v2#S1.p3.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p1.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§6](https://arxiv.org/html/2601.22436v2#S6.p3.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* G. Zhang, M. Fu, and S. Yan (2025b)
  Memgen: weaving generative latent memory for self-evolving agents.
  arXiv preprint arXiv:2509.24704.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p2.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Q. Zhang, C. Hu, S. Upasani, B. Ma, F. Hong, V. Kamanuru, J. Rainton, C. Wu, M. Ji, H. Li, et al. (2025c)
  Agentic context engineering: evolving contexts for self-improving language models.
  arXiv preprint arXiv:2510.04618.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p3.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* Y. Zhang, J. Shu, Y. Ma, X. Lin, S. Wu, and J. Sang (2025d)
  Memory as action: autonomous context curation for long-horizon agentic tasks.
  arXiv preprint arXiv:2510.12635.
  Cited by: [Impact Statement](https://arxiv.org/html/2601.22436v2#Sx1.p3.1 "Impact Statement ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* A. Zhao, D. Huang, Q. Xu, M. Lin, Y. Liu, and G. Huang (2024a)
  Expel: llm agents are experiential learners.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 38,  pp. 19632–19642.
  Cited by: [Appendix A](https://arxiv.org/html/2601.22436v2#A1.p1.1 "Appendix A Self-Evolving Agents ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [1st item](https://arxiv.org/html/2601.22436v2#A3.I1.i1.p1.1 "In Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§1](https://arxiv.org/html/2601.22436v2#S1.p2.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§1](https://arxiv.org/html/2601.22436v2#S1.p3.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p1.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* W. Zhao, S. Wang, Y. Hu, Y. Zhao, B. Qin, X. Zhang, Q. Yang, D. Xu, and W. Che (2024b)
  SAPT: a shared attention framework for parameter-efficient continual learning of large language models.
  In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 11641–11661.
  Cited by: [§1](https://arxiv.org/html/2601.22436v2#S1.p1.1 "1 Introduction ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. Xing, et al. (2023)
  Judging llm-as-a-judge with mt-bench and chatbot arena.
  Advances in neural information processing systems 36,  pp. 46595–46623.
  Cited by: [3rd item](https://arxiv.org/html/2601.22436v2#A3.I1.i3.p2.1 "In Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* W. Zhong, L. Guo, Q. Gao, H. Ye, and Y. Wang (2024)
  Memorybank: enhancing large language models with long-term memory.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 38,  pp. 19724–19731.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* H. Zhou, Y. Chen, S. Guo, X. Yan, K. H. Lee, Z. Wang, K. Y. Lee, G. Zhang, K. Shao, L. Yang, et al. (2025)
  Memento: fine-tuning llm agents without fine-tuning llms.
  arXiv preprint arXiv:2508.16153.
  Cited by: [§6](https://arxiv.org/html/2601.22436v2#S6.p2.1 "6 Related Works ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").
* S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Sridhar, X. Cheng, T. Ou, Y. Bisk, D. Fried, et al. (2024)
  WebArena: a realistic web environment for building autonomous agents.
  In The Twelfth International Conference on Learning Representations,
  Cited by: [1st item](https://arxiv.org/html/2601.22436v2#A2.I4.i1.p1.1 "In B.4 Web Interaction ‣ Appendix B Environment and Benchmark ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"),
  [§3.1](https://arxiv.org/html/2601.22436v2#S3.SS1.p3.1 "3.1 Experimental Setup ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

## Appendix A Self-Evolving Agents

We present detailed description of the four experience-driven self-evolving agents used in our experiments: ExpeL (Zhao et al., [2024a](https://arxiv.org/html/2601.22436v2#bib.bib12 "Expel: llm agents are experiential learners")), Dynamic Cheatsheet (Suzgun et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib24 "Dynamic cheatsheet: test-time learning with adaptive memory")), ReasoningBank (Ouyang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib14 "Reasoningbank: scaling agent self-evolving with reasoning memory")) and G-Memory (Zhang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib15 "G-memory: tracing hierarchical memory for multi-agent systems")). Across all frameworks, agents adapt their behavior by accumulating, retrieving, and reusing external experiences stored in explicit memory structures, rather than by updating the parameters of the underlying language model. In the following, we summarize the core design principles and memory mechanisms of these agents in detail:

* •

  ExpeL is an offline self-evolving agent that enables a fixed language model to acquire and reuse experience across tasks without parameter updates. During an offline training phase, the agent interacts with a set of tasks and collects both successful and failed trajectories generated through trial and error. These experiences are stored in an experience pool and subsequently processed to extract natural-language insights that summarize effective strategies and general decision-making principles. In addition to abstracted insights, successful trajectories are retained to support example-based recall. At inference time, the agent augments the model’s context with the extracted insights and retrieved successful experiences that are semantically similar to the current task. This design separates experience accumulation and knowledge extraction from deployment, allowing the agent to improve its task-solving behavior through offline experiential learning while keeping the underlying language model fixed during evaluation.
* •

  Dynamic Cheatsheet is an online self-evolving agent that equips a fixed language model with an external memory updated during inference. The agent maintains a compact memory consisting of reusable solution elements, such as heuristics, partial solution templates, and short code fragments, derived from its own prior generations. After each task, the agent examines the produced output and selectively updates the memory by preserving entries that appear useful, while modifying or removing ineffective ones. When handling subsequent inputs, the agent retrieves relevant memory contents and incorporates them into the prompt context to influence generation. This iterative process of generation, memory update, and retrieval forms a closed-loop mechanism that enables test-time behavioral adaptation over a sequence of tasks, without performing parameter updates or altering the underlying language model.
* •

  ReasoningBank embodies an instance of an online self-evolving agent. It keeps an ever-expanding memory that records condensed reasoning patterns distilled from the agent’s past interactions, covering both successful cases and failures. Following each task completion, the agent assesses its own performance and selectively incorporates newly acquired experiences into this memory repository. During inference, pertinent reasoning strategies are retrieved from the memory and incorporated into the agent’s context to guide future interactions. The system forms a closed feedback loop where experiences are continuously accumulated, accessed, and reused throughout deployment, enabling the agent’s behavior to progressively adapt over time.
* •

  G-Memory is an online self-evolving memory mechanism designed for multi-agent systems. It maintains a shared, persistent memory that records past multi-agent collaboration experiences across tasks, capturing both abstract insights and condensed interaction histories. When a new task arrives, relevant memory entries are retrieved and selectively injected into the contexts of different agents to support coordination and reasoning. After task completion, newly generated interactions and distilled insights are incorporated into the memory, updating its contents during deployment. This continual retrieval-and-update process enables agent teams to accumulate and reuse collaborative experience over time, allowing collective behavior to adapt without modifying the underlying language models.

## Appendix B Environment and Benchmark

### B.1 Knowledge-Intensive Question Answering

* •

  HotpotQA (Yang et al., [2018](https://arxiv.org/html/2601.22436v2#bib.bib29 "HotpotQA: a dataset for diverse, explainable multi-hop question answering")) is a large-scale question answering benchmark designed to support multi-hop reasoning over natural language text. It contains question–answer pairs constructed from Wikipedia articles, where answering each question requires reasoning across multiple supporting documents. The questions are diverse in form, including standard factoid queries as well as comparison and yes/no questions, and are not constrained by predefined knowledge base schemas. We selected 100 questions from the distractor dev split following ExpeL for our experiments.
* •

  FEVER (Thorne et al., [2018](https://arxiv.org/html/2601.22436v2#bib.bib30 "FEVER: a large-scale dataset for fact extraction and verification")) is a large-scale benchmark for claim verification against textual evidence. It consists of 185,445 human-written claims derived from Wikipedia, each labeled as SUPPORTED, REFUTED, or NOT ENOUGH INFO. The claims are generated by mutating original Wikipedia statements and are verified in a separate annotation process, resulting in a collection that emphasizes evidence retrieval and textual entailment over natural language. Following G-Memory, we selected the first 100 questions of the validation set for our experiments.
* •

  GPQA-Diamond (Rein et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib31 "Gpqa: a graduate-level google-proof q&a benchmark")) is a carefully curated and challenging subset of the Graduate-Level Google-Proof Q&A (GPQA) benchmark. It comprises 198 expert-validated questions drawn from the natural sciences, including biology, chemistry, and physics. The questions are constructed to minimize the reliance on straightforward fact recall and instead emphasize a deeper conceptual understanding. All questions can be correctly answered by domain specialists, while they are frequently challenging for non-experts, reflecting the need for complex, multi-step reasoning rather than surface-level knowledge.
* •

  MMLU-Pro Eng. (Wang et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib32 "Mmlu-pro: a more robust and challenging multi-task language understanding benchmark")) is a professional-level subset of the MMLU benchmark that focuses on topics in physics and engineering. The questions are all formatted as multiple-choice problems. The full dataset includes 1,299 questions in physics and 969 questions in engineering, from which we randomly selected 100 questions for our experiments. The problem content spans a range of subfields within the two disciplines and requires precise technical understanding to distinguish among closely related answer options.

### B.2 Mathematical Reasoning

* •

  AIME 2024 The American Invitational Mathematics Examination (AIME) is a well-established benchmark derived from a prestigious high-school mathematics competition. The competition is known for its integer-answer format and time-limited setting, which further emphasizes precision and logical rigor. It consists of 133 challenging problems covering algebra, combinatorics, number theory, geometry, and probability, each requiring non-trivial mathematical reasoning and multi-step solution processes.
* •

  Game of 24 (Yao et al., [2023a](https://arxiv.org/html/2601.22436v2#bib.bib33 "Tree of thoughts: deliberate problem solving with large language models"); Suzgun and Kalai, [2024](https://arxiv.org/html/2601.22436v2#bib.bib34 "Meta-prompting: enhancing language models with task-agnostic scaffolding")) is a heuristic-oriented arithmetic task in which the goal is to construct an expression that evaluates to 24 by using four given numbers exactly once. The task features a small combinatorial search space but allows for diverse solution paths depending on operator ordering and grouping. For example, given the input “7 7 8 11” a valid solution is “8 × (7 + 7 − 11).” Solving this task requires systematic exploration of the solution space, along with strategic reasoning and pattern recognition. We adopt the 100 instances provided by (Suzgun and Kalai, [2024](https://arxiv.org/html/2601.22436v2#bib.bib34 "Meta-prompting: enhancing language models with task-agnostic scaffolding")) to iteratively refine strategies across repeated attempts.

### B.3 Embodied Action

* •

  ALFWorld (Shridhar et al., [2021](https://arxiv.org/html/2601.22436v2#bib.bib18 "ALFWorld: aligning text and embodied environments for interactive learning")) is an embodied benchmark that aligns abstract, text-based environments with interactive visual-based scenes to execute household tasks. It builds on the ALFRED (Shridhar et al., [2020](https://arxiv.org/html/2601.22436v2#bib.bib45 "Alfred: a benchmark for interpreting grounded instructions for everyday tasks")) benchmark by providing paired representations of the same underlying tasks, where agents can operate through high-level textual commands in a simulated environment. The tasks span multiple categories such as pick-and-place, cleaning, heating, and cooling, and require multi-step interaction with objects and receptacles distributed across diverse room layouts. The benchmark is constructed to maintain a shared underlying world state across modalities, enabling consistent correspondence between language-level actions and embodied executions. We utilized the 134 solvable tasks.

### B.4 Web Interaction

* •

  WebArena (Zhou et al., [2024](https://arxiv.org/html/2601.22436v2#bib.bib17 "WebArena: a realistic web environment for building autonomous agents")) is a realistic and reproducible benchmark for web-based interaction tasks grounded in natural language instructions. WebArena provides 812 web navigation tasks that cover four common application domains: Shopping (187), CMS (182), Reddit (106) and Map (109). BrowserGym (de Chezelles et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib46 "The browsergym ecosystem for web agent research")) is used as the execution environment for WebArena. Each task is specified as a high-level natural language intent and requires agents to execute a sequence of concrete web interactions across dynamic pages and tools. The benchmark includes a curated set of long-horizon tasks with programmatic validation based on functional correctness of the final outcomes.
* •

  WebShop (Yao et al., [2022](https://arxiv.org/html/2601.22436v2#bib.bib35 "Webshop: towards scalable real-world web interaction with grounded language agents")) is a large-scale web interaction benchmark that simulates realistic online shopping scenarios through a self-contained e-commerce environment. It includes over one million real-world products and 12,087 crowdsourced natural language instructions, each specifying a product requirement to be fulfilled through a sequence of web-based actions. Given an instruction, an agent must navigate search results, inspect product pages, select appropriate options, and complete a purchase to satisfy the specified constraints. We follow the instructions of ExpeL to set the implementation details of the WebShop Environment. For WebShop tasks, we evaluated using the same 100 tasks used by ReAct (Yao et al., [2023b](https://arxiv.org/html/2601.22436v2#bib.bib37 "React: synergizing reasoning and acting in language models")), Reflexion (Shinn et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib47 "Reflexion: language agents with verbal reinforcement learning")) and ExpeL.

## Appendix C Implementation Details

* •

  ExpeL We follow the official setup described in the ExpeL (Zhao et al., [2024a](https://arxiv.org/html/2601.22436v2#bib.bib12 "Expel: llm agents are experiential learners")). For agent hyperparameters, the LLM decoding temperature is set to 0.0, and greedy decoding is used. During the experience gathering stage, the maximum number of reflection retries is set to 3. At evaluation time, ExpeL retrieves the top-*k* most similar successful trajectories and uses them as in-context demonstrations. The vector store is implemented with Faiss, the retriever uses kNN, and all task descriptions are embedded using the *all-mpnet-base-v2* encoder.

  Different benchmarks adopt different interaction budgets and retrieval strategies. Specifically, for HotpotQA, each task is allowed up to 7 environment interaction steps, and up to 6 successful trajectories are retrieved as few-shot demonstrations during evaluation. For WebShop, each task allows up to 15 interaction steps, with up to 2 retrieved successful trajectories. For ALFWorld, each task allows up to 20 steps, and up to 2 successful trajectories are retrieved.
* •

  Dynamic Cheatsheet We follow the official experimental setup of Dynamic Cheatsheet (Suzgun et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib24 "Dynamic cheatsheet: test-time learning with adaptive memory")). For agent hyperparameters, the LLM decoding temperature is set to 0.0, and greedy decoding is used. Across all benchmarks in Dynamic Cheatsheet, including AIME 2024, Game of 24, GPQA-Diamond, and MMLU-Pro Eng., we adopt the same retrieval configuration. Specifically, before each new task, the system computes cosine similarity between the embedding of the current query and embeddings of historical queries, and retrieves the top-3 most similar past input–output pairs from memory to support inference.
* •

  ReasoningBank Our experimental setup largely follows the configuration of ReasoningBank (Ouyang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib14 "Reasoningbank: scaling agent self-evolving with reasoning memory")). For the agent, we set the decoding temperature to 0.7 and adopt greedy decoding as the decoding strategy. On the WebArena benchmark, each task is allowed a maximum of 30 interaction steps. We use *text-embedding-ada-002* as the embedding model to encode queries and memory items, and employ cosine similarity for retrieval. For each new query, the agent retrieves the top-3 most relevant memory items, which are then injected into the agent’s prompt.

  Task outcomes are labeled as success or failure using LLM-as-a-judge (Zheng et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib48 "Judging llm-as-a-judge with mt-bench and chatbot arena")). The judge model, as well as the model used for memory extraction, is configured with a decoding temperature of 0.0, with the goal of maximizing determinism in the evaluation and extraction process. Each memory item follows a fixed schema consisting of three components: a Title, which concisely summarizes the underlying strategy; a Description, which provides a one-sentence abstract of the memory; and Content, which contains one to five sentences of distilled insights.
* •

  G-Memory We follow the experimental setup of G-Memory (Zhang et al., [2025a](https://arxiv.org/html/2601.22436v2#bib.bib15 "G-memory: tracing hierarchical memory for multi-agent systems")). For coarse-grained retrieval over the query graph, queries are encoded using a MiniLM sentence embedding model and matched with cosine similarity, retrieving the top-k most similar historical queries. For fine-grained retrieval, we further select the top-M relevant queries using an LLM-based relevance scorer and sparsify their interaction graphs with an LLM-based graph compression module. The values of k and M are treated as tunable hyperparameters. Query nodes are labeled with execution status from Failed, Resolved. All retrieved insights and interaction subgraphs are injected into agent prompts before task execution, and the memory graphs are updated after each task without any gradient-based training.

Table 3: An example of experience interventions.

|  |  |
| --- | --- |
| System Instruction | |
| Task Goal | Question: Why did Grand Duke Kirill Vladimirovich Of Russia’s wife die? |
| Raw Experience Interventions | |
| Original | Here are some examples:   Question: Who died first, Fleetwood Sheppard or George William Whitaker?   Action 1: Search[Fleetwood Sheppard]  Observation 1: Fleetwood Sheppard (1 January 1634 – 25 August 1698) was an English courtier.   Action 2: Search[George William Whitaker]  Observation 2: George William Whitaker (September 25, 1840 – March 6, 1916) was a painter.  Action 3: Finish[Fleetwood Sheppard]  Observation 3: Answer is CORRECT |
| Empty | Here are some examples: |
| Shuffle | Here are some examples:  Question: Who died first, Fleetwood Sheppard or George William Whitaker?  Observation 3: Answer is CORRECT  Action 3: Finish[Fleetwood Sheppard]  Action 1: Search[Fleetwood Sheppard]  Observation 1: Fleetwood Sheppard (1 January 1634 – 25 August 1698) was an English courtier.   Action 2: Search[George William Whitaker]  Observation 2: George William Whitaker (September 25, 1840 – March 6, 1916) was a painter. |
| Irrelevant | Here are some examples:  Question: What is the place of birth of Clara Novello’s father?  Action 1: Search[Pavel Urysohn]  Observation 1: Pavel Samuilovich Urysohn was a Soviet mathematician.  Action 2: Search[Leonid Levin]  Observation 2: Leonid Anatolievich Levin is a mathematician and computer scientist.   Action 3: Finish[yes] |
| Condensed Experience Interventions | |
| Original | The following are some experience you gather on a similar task. Use these as references to help you perform this task:  1. When encountering conflicting or ambiguous search results, perform a lookup for the exact name or title to verify identity and avoid confusion with similarly named individuals.  2. If a search repeatedly returns incorrect or unrelated information, systematically refine the search query by incorporating contextual qualifiers, roles, or relationships to isolate the correct individual or entity. |
| Empty | The following are some experience you gather on a similar task. Use these as references to help you perform this task: |
| Corrupt | The following are some experience you gather on a similar task of question answering using Wikipedia API. Use these as references to help you perform this task:  1. When encountering conflicting [CORRUPTED\_561] ambiguous search results, perform a lookup for the exact name or [CORRUPTED\_842] to verify identity and avoid confusion with similarly named individuals. [ERROR\_INFO]  2. If a search repeatedly returns [CORRUPTED\_746] or unrelated information, systematically refine the search query by incorporating contextual qualifiers, roles, [ERROR\_INFO] or relationships isolate the individual or entity. |
| Irrelevant | The following are some experience you gather on a similar task. Use these as references to help you perform this task:  1. Literature contains various genres and styles.  2. Art expresses human creativity and emotion. |
| Filler | The following are some experience you gather on a similar task. Use these as references to help you perform this task:  1. … $$$ ###   2. \*\*\* … \*\*\* |

## Appendix D Details of Intervention Design

We provide additional details and design motivations for the intervention strategies used in our faithfulness evaluation. As discussed in §[3](https://arxiv.org/html/2601.22436v2#S3 "3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), raw and condensed experiences differ substantially in their structure, abstraction level, and expected utility. Our intervention design reflects these differences while adhering to two principles: (1) targeting the failure modes most likely to occur in each experience type, and (2) ensuring minimal disruption to input formatting and inference pipelines.
To concretize these designs, Table [3](https://arxiv.org/html/2601.22436v2#A3.T3 "Table 3 ‣ Appendix C Implementation Details ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") presents illustrative examples of each intervention applied to ExpeL framework.

### D.1 Raw Experience Interventions

Raw experiences consist of complete trajectories, often encoded as multi-step sequences of observations, actions, and outcomes. They are typically grounded in specific tasks and retain temporal and causal coherence.

* •

  Empty: This intervention removes the semantic content of the raw experience (e.g., deleting trajectory steps) while retaining the prompt structure (e.g., “Here are two examples of past successful trajectories:”). This allows us to test whether the agent benefits from the actual content or merely from the presence of a scaffolded context block.
* •

  Shuffle: By randomly permuting the steps in each trajectory, we disrupt its internal temporal and causal structure while preserving token-level content. This tests whether the agent relies on coherent sequencing in trajectory usage.
* •

  Irrelevant: Retrieved trajectories are replaced with examples drawn from unrelated tasks with similar surface format. This targets the agent’s sensitivity to topical relevance and allows us to evaluate semantic grounding.

We use three interventions for raw experience, as these cover the main axes of disruption: existence, ordering, and relevance. We avoid over-complicating the raw setting since its structure is already explicit and well-formed.

### D.2 Condensed Experience Interventions

Condensed experiences are distilled textual summaries derived from past interactions, often presented as high-level heuristics, plans, or failure abstractions. Compared to raw trajectories, these summaries are more abstract, loosely structured, and typically lack strict ordering constraints.

* •

  Empty: We remove the content of the summary while preserving formatting (e.g., “Here is a distilled insight:”), in order to test whether performance is attributable to semantic content or merely to the presence of a template.
* •

  Corrupt: Key logical elements are randomly perturbed (e.g., inverting causal relations, altering conditionals, or replacing verbs), breaking the internal coherence while maintaining surface form. This helps assess whether the agent truly parses and applies the intended reasoning patterns.
* •

  Irrelevant: A summary from an unrelated task is inserted in place of the retrieved one, preserving general topic style while disrupting task alignment. This intervention probes reliance on contextual specificity.
* •

  Filler: The entire content is replaced with semantically meaningless placeholder tokens (e.g., sequences of special characters such as “%$#@&”). This isolates whether improvements stem from semantic value.

Unlike raw trajectories, condensed summaries do not rely on internal ordering of steps or temporal structure. Therefore, we do not include a Shuffle variant in this setting. Instead, we introduce two complementary perturbations:

Corrupt targets internal *semantic consistency*, testing whether the agent interprets specific logic embedded in the summary. Filler targets *semantic emptiness* under preserved surface form, to assess reliance on textual formatting. These design choices reflect the unique failure modes of abstracted experience and enable more fine-grained diagnosis of when and how condensed content influences behavior.

Figure 8: Results on Qwen3-235B-A22B for HotpotQA, ALFWorld, and WebShop under ExpeL. We observe similar patterns as in GPT-4o: strong reliance on raw experience and inconsistent faithfulness to condensed summaries.

## Appendix E Additional Experimental Results

### E.1 Additional Results on Qwen3-235B-A22B with ExpeL

To verify the consistency of our findings across backbone models, we replicate the same intervention study using the open-weight Qwen3-235B-A22B. The results, visualized in Figure [8](https://arxiv.org/html/2601.22436v2#A4.F8 "Figure 8 ‣ D.2 Condensed Experience Interventions ‣ Appendix D Details of Intervention Design ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), align closely with the GPT-4o-based findings.

First, agents remain highly sensitive to raw experience interventions. Across HotpotQA, ALFWorld, and WebShop, the removal of raw experience (especially Empty and Irrelevant) consistently results in substantial performance drops, reaffirming that the agent does not simply rely on priors but indeed benefits from retrieved raw trajectories.

Second, the faithfulness to condensed experience remains weak. In HotpotQA and WebShop, corrupting condensed summaries yields little to no degradation, suggesting these components are often underutilized during inference. ALFWorld shows a slight drop under Filler and Corrupt, but the impact is still limited compared to raw experience interventions.

Lastly, we observe that Shuffle (raw) and Filler (condensed) preserve surface structure while destroying coherence or semantics. The agent’s partial robustness to these reveals possible overreliance on format cues rather than deep content integration, further motivating the need for more faithful mechanisms of experience exploitation.

Figure 9: Condensed-only performance on the ReasoningBank framework (online, single-agent) using Qwen3-14B. Perturbing condensed experience has limited or inconsistent impact across tasks.

Figure 10: Condensed-only performance on the ReasoningBank framework (online, single-agent) using Qwen3-32B. Similar to the 14B variant, condensed interventions do not strongly influence success rates.

### E.2 Additional Results on Condensed-Only Setting: ReasoningBank

#### Overview.

In the main text, we demonstrate that agents exhibit limited faithfulness to condensed experience when both raw and condensed memories are present. However, one may wonder: is this apparent unfaithfulness due to reliance on raw experience, overshadowing the role of condensed summaries? To answer this, we evaluate agents in a condensed-only setting using the ReasoningBank, which provides only distilled insights from past trajectories without access to raw examples.

#### Qwen3-14B and Qwen3-32B exhibit consistent trends.

Figure [9](https://arxiv.org/html/2601.22436v2#A5.F9 "Figure 9 ‣ E.1 Additional Results on Qwen3-235B-A22B with ExpeL ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") and Figure [10](https://arxiv.org/html/2601.22436v2#A5.F10 "Figure 10 ‣ E.1 Additional Results on Qwen3-235B-A22B with ExpeL ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") shows results of Qwen3-14B and Qwen3-32B on four WebArena tasks under the ReasoningBank setup, respectively. Despite architectural and scale differences, both models display similar behavior to the Gemini-2.5-Flash (see main Figure [4](https://arxiv.org/html/2601.22436v2#S3.F4 "Figure 4 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")): interventions such as Corrupt, Irrelevant, and Filler yield only minor performance degradation. In some cases, like Shopping and CMS, success rates remain comparable or even slightly improve under perturbed conditions.

These findings reinforce our earlier conclusion: even when condensed experience is the sole retrieved knowledge, agents often do not meaningfully exploit its semantic content. The lack of sensitivity across various perturbations—including semantically incoherent or content-free fillers—suggests superficial reliance or formatting over genuine understanding.

Figure 11: Intervention results for the G-Memory framework using Qwen3-235B-A22B as the backbone. Across both FEVER and ALFWorld, interventions on both Reference and Execution Raw Experiences cause clear performance degradation, while condensed experience perturbations have notably weaker effects. This supports the generality of our earlier conclusions.

### E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B

To verify the generality of our findings in multi-agent online self-evolving settings, we further replicate the G-Memory experiments using a stronger backbone: Qwen3-235B-A22B. The results on FEVER and ALFWorld are shown in Figure [11](https://arxiv.org/html/2601.22436v2#A5.F11 "Figure 11 ‣ Qwen3-14B and Qwen3-32B exhibit consistent trends. ‣ E.2 Additional Results on Condensed-Only Setting: ReasoningBank ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers").

#### Faithfulness to raw experience holds across sources and models.

In the ALFWorld domain, removing or corrupting either source of raw experience (Reference or Execution) results in large performance degradation. For example, removing execution experience (Exe-Raw Exp. Empty) drops performance by −6.8-6.8 points, and replacing human-written reference experience with irrelevant ones leads to an even greater drop of −30.6-30.6 (from 78.4 to 47.8). This mirrors our earlier observations under GPT-4o-mini (Figure [5](https://arxiv.org/html/2601.22436v2#S3.F5 "Figure 5 ‣ 3.3 Condensed Experience Interventions ‣ 3 Causal Intervention on Experience ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")) and reinforces that regardless of origin, raw experiences are faithfully grounded.

Interestingly, this effect generalizes well even in a stronger model: Qwen3-235B-A22B not only follows the same degradation trend, but also amplifies the raw-condensed disparity more clearly, suggesting that as models become more capable, their selective grounding behavior becomes more pronounced.

#### Condensed experience remains less semantically grounded.

Across both FEVER and ALFWorld, interventions such as Corrupt, Irrelevant, or Filler show limited or even no degradation (e.g., Filler still achieves 77.6, almost matching unperturbed performance). This further validates our earlier claim: while condensed experience offers utility, agent decisions do not strongly rely on its internal semantics, even in large-scale models.

Table 4: Failure case of distraction from the task goal.

|  |
| --- |
| Task Goal: How much refund I should expect from my order canlled in 2022, including shipping fee. |
| With condensed experience: |
| Think: From the memory items, I remember that accessing the order history via “My Account” is the direct way to find order details. |
| Action: click(‘176’) |
| Think: The user wants to include shipping fees, so if the total is already the order total (which presumably includes shipping), then that’s the refund amount. But to be sure, maybe we should click “View Order” to check the details. However, Memory Item 3 advises against clicking into details if the total is visible. Therefore, the next action is to send the user the refund amount based on the visible total. |
| Action: send\_msg\_to\_user(“The refund amount for your canceled order (Order #000000177 from 10182022) is $2,126.32, which includes shipping fees.”) |
| Evaluation: FAILED. The bot successfully navigated to the correct order and calculated the refund amount. However, the final response to the user was incomplete, missing the full amount information. |
| Without condensed experience: |
| Think: The next step is to click on ”My Account” to access their account details. |
| Action: click(‘176’) |
| Think: The order in question is listed as canceled, and the total is $365.42. But the user wants to know the refund amount including shipping. To find out, I should click on “View Order” for that specific canceled order. |
| Action: click(‘584’) |
| Think: The order details show the subtotal as $350.42, shipping and handling at $15.00, making the grand total $365.42. |
| Action: send\_msg\_to\_user(“The total amount for your canceled order #000000170 is $365.42, which includes a subtotal of $350.42 for the items and $15.00 for shipping.”) |
| Evaluation: SUCCEED. The agent correctly identified the total refund amount, including the item and shipping costs, as $365.42, which matches the information provided on the webpage. The response also advises the user to check with customer support for any potential deductions, which is a reasonable caution. |

Table 5: Failure case of overreliance on incorrect priors.

|  |
| --- |
| Task Goal: Provide me with the full names of chargers from Anker, and also share the price range for the available models. |
| With condensed experience: |
| Think: First, I need to search for Anker chargers. Memory Item 1 says to use the search function with precise keywords. |
| Action: fill(‘211’, ‘Anker chargers’) |
| Think: The current page shows a search result for “Anker chargers,” but looking at the product list, none of the items are actually Anker chargers. Since the search results are not relevant, the next step is to handle the case where search results are incomplete or absent, as per memory item 3. Therefore, the assistant should inform the user that no Anker chargers were found in the search results and suggest alternative stepss. |
| Action: send\_msg\_to\_user(“It seems there are no Anker charger products in the current search results. Let me check if there are other categories or refine the search further.”) |
| Evaluation: FAILED. The agent failed to find the Anker chargers as per user’s intent. The webpage shows unrelated products, indicating the search did not succeed. Moreover, the agent did not provide the requested information on the full names or price range of the chargers. |
| Without condensed experience: |
| Think: Let me try filling that with “Anker chargers” and then see if the search button becomes enabled. But since the button is disabled, perhaps the search is triggered by pressing Enter or another action. Let me try filling the search box and then pressing Enter. |
| Action: fill(‘214’, ‘Anker chargers’); press(‘214’, ‘Enter’) |
| Think: The current page shows search results for “Anker chargers,” and there are several products listed. Each product has a name and a price. |
| Action: send\_msg\_to\_user(“Here are some Anker charger models and their prices from the search results: (Detailed search results). The price range for available models is from $8.99 to $59.99.”) |
| Evaluation: SUCCEED. The agent successfully provided a list of Anker charger models along with their prices, matching the user’s request. The price range was also accurately given. |

Table 6: Failure case of premature inference from prior patterns.

|  |
| --- |
| Task Goal: Show the most recent processing order. |
| With condensed experience: |
| Think: Okay, the user wants to see the most recent processing order. The ‘My Account’ link in the banner is a list item with a link. |
| Action: click(‘175’) |
| Think: The first order listed is Order #000000170 from 5/17/23 with a status of “Canceled”. However, the user might want the most recent one that’s processed, maybe not canceled. Wait, the user just said “most recent processing order”, so maybe the latest one regardless of status. The status is “Canceled”. But perhaps the user wants to see that. |
| Action: send\_msg\_to\_user(“The most recent processing order is Order #000000170, placed on May 17, 2023. Status: Canceled. Items: 1. Uttermost Volterra Lamp ($250.80), 2. NOZE Coat Rack ($40.99), 3. Plus Size Lingerie ($58.63). Total: $365.42. Shipping and billing address: Emma Lopez, 101 S San Mateo Dr, San Mateo, CA 94010. Payment method: Check/Money order.”) |
| Evaluation: FAILED. The user’s intent was to see the most recent processing order. The bot provided information about Order #000000170, but the status is canceled. The information on the webpage confirms this order is canceled, matching the bot’s response. Therefore, the task is incomplete as it didn’t provide an active processing order. |
| Without condensed experience: |
| Think: Okay, let’s see. The user wants to show the most recent processing order. The navigation menu has “My Account” as a link. |
| Action: click(‘177’) |
| Think: The most recent order based on the date would be the one from 5/17/23, which is order #000000170. But the user might be looking for the latest one that’s not canceled. The next one is 5/2/23 with order #000000189, status Pending. |
| Action: send\_msg\_to\_user(“The most recent processing order is Order #000000189. It is currently pending, placed on May 2, 2023. The order includes a Quoizel Tiffany Floor Lamp with a total of $754.99. The shipping and billing addresses are both for Emma Lopez in San Mateo, California. The payment method selected is Check / Money order.”) |
| Evaluation: SUCCEED. The agent successfully retrieved and conveyed the details of the most recent processing order to the user. The information provided matches the details shown on the final webpage snapshot, ensuring accuracy and completeness of the response. |

(a) Baseline without intervention.

(b) Corrupt intervention.

(c) Irrelevant intervention.

(d) Filler intervention.

(e) Empty intervention.

Figure 12: Layer-wise Integrated Gradients attribution under the ExpeL framework using Qwen3-1.7B. Prompts are divided into four segments: System Instruction, Condensed Experience, Raw Experience, and Current Trajectory.

(a) Baseline without intervention.

(b) Corrupt intervention.

(c) Irrelevant intervention.

(d) Filler intervention.

(e) Empty intervention.

Figure 13: Layer-wise Integrated Gradients attribution under the ExpeL framework using Qwen3-4B. Prompts are divided into four segments: System Instruction, Condensed Experience, Raw Experience, and Current Trajectory.

(a) Baseline without intervention.

(b) Corrupt intervention.

(c) Irrelevant intervention.

(d) Filler intervention.

(e) Empty intervention.

Figure 14: Layer-wise Integrated Gradients attribution under the ExpeL framework using Qwen3-8B. Prompts are divided into four segments: System Instruction, Condensed Experience, Raw Experience, and Current Trajectory.

(a) Baseline without intervention.

(b) Corrupt intervention.

(c) Irrelevant intervention.

(d) Filler intervention.

(e) Empty intervention.

Figure 15: Layer-wise Integrated Gradients attribution under the ExpeL framework using Qwen3-14B. Prompts are divided into four segments: System Instruction, Condensed Experience, Raw Experience, and Current Trajectory.

(a) Baseline without intervention.

(b) Corrupt intervention.

(c) Irrelevant intervention.

(d) Filler intervention.

(e) Empty intervention.

Figure 16: Layer-wise Integrated Gradients attribution under the ExpeL framework using Qwen3-32B. Prompts are divided into four segments: System Instruction, Condensed Experience, Raw Experience, and Current Trajectory.

### E.4 Representative Failure Cases for Condensed Experience

To distinguish failure modes where an agent succeeds without condensed experience but fails when it is added, we group them into three categories as described in §[5.1](https://arxiv.org/html/2601.22436v2#S5.SS1 "5.1 Semantic Limitations of Condensed Experience ‣ 5 The Cause of Unfaithfulness ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"): Distraction from the Task Goal, Overreliance on Incorrect Priors, and Premature Inference from Prior Patterns. Representative cases are shown in Table [4](https://arxiv.org/html/2601.22436v2#A5.T4 "Table 4 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), Table [5](https://arxiv.org/html/2601.22436v2#A5.T5 "Table 5 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), and Table [6](https://arxiv.org/html/2601.22436v2#A5.T6 "Table 6 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), respectively.

### E.5 Additional IG Attribution Results

Setup. We follow the official experimental setup of Integrated Gradients (IG) (Wang et al., [2023](https://arxiv.org/html/2601.22436v2#bib.bib39 "Label words are anchors: an information flow perspective for understanding in-context learning"); Tang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib40 "Revisiting long-context modeling from context denoising perspective")). The IG score is computed on the last-turn prompt, i.e., the input context immediately before the agent executes its final action. Due to computational and memory constraints in long-context settings, we adopt an approximate IG formulation for efficiency. Specifically, we use the gradient magnitude of token embeddings as a surrogate for the attention-level IG score. Prior work has shown that embedding gradient norms exhibit a strong positive correlation with attention-based IG scores across different token categories, validating this approximation (Tang et al., [2025](https://arxiv.org/html/2601.22436v2#bib.bib40 "Revisiting long-context modeling from context denoising perspective")). Concretely, for a given sample, we compute the gradients of the token embeddings with respect to the cross-entropy loss, take the L2 norm for each token embedding, and use the arithmetic mean of the L2 norms over all tokens as the final IG score for the sample.

Results & Analysis. To validate the generality of our findings, we extend our attribution analysis to a broader range of model sizes within the Qwen3 series. Specifically, we report layer-wise Integrated Gradients (IG) scores under the ExpeL framework for Qwen3-1.7B, Qwen3-4B, Qwen3-8B, Qwen3-14B, and Qwen3-32B, across multiple intervention conditions on condensed experience. The results for these models are shown in Figure [12](https://arxiv.org/html/2601.22436v2#A5.F12 "Figure 12 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), Figure [13](https://arxiv.org/html/2601.22436v2#A5.F13 "Figure 13 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), Figure [14](https://arxiv.org/html/2601.22436v2#A5.F14 "Figure 14 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), Figure [15](https://arxiv.org/html/2601.22436v2#A5.F15 "Figure 15 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers") and Figure [16](https://arxiv.org/html/2601.22436v2#A5.F16 "Figure 16 ‣ Condensed experience remains less semantically grounded. ‣ E.3 Additional Results on Multi-agent Setting with Qwen3-235B-A22B ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers"), respectively.
Across all scales, we observe consistent patterns:

Condensed experience exhibits persistently low attribution across layers. Across all Qwen3 models and settings, the IG scores assigned to condensed experience remain consistently low and flat, indicating that these segments contribute minimally to the final output. Even when the condensed experience is intervened, the model rarely shifts its attention or reliance toward these inputs, suggesting a structural underutilization regardless of quality.

Raw experience is moderately and faithfully leveraged.
In contrast, raw experience segments show stable and nontrivial attribution across layers, especially in the mid-to-deep transformer blocks. This pattern holds even under different intervention conditions and model scales, confirming that raw trajectories are causally linked to agent behavior and thus more faithfully integrated into decision-making.

Local context dominates in deeper layers.
The IG scores for the current trajectory tokens rise sharply in the later layers, becoming the dominant source of influence. This demonstrates the model’s tendency to increasingly attend to and rely on its ongoing generation context, rather than external retrieved signals, as output tokens are being produced.

Empty intervention triggers compensatory over-attribution to the placeholder segment.
When the condensed experience is replaced with an empty string, its attribution unexpectedly increases, especially in shallow to mid layers. This suggests that the model initially treats the placeholder segment as potentially informative due to its positional slot or formatting. However, this early attribution is short-lived—quickly diminishing in deeper layers as the model fails to extract meaningful content. This transient spike, followed by sharp decay, underscores the model’s structural bias to initially attend to all segments but ultimately rely on meaningful local context.

Condensed experience receives slightly elevated attribution when perturbed, but without meaningful impact.
In some models, introducing intervention (especially irrelevant content) into the condensed experience causes small bumps in early-layer IG scores. However, these signals quickly dissipate in deeper layers, and the behavioral outputs remain largely unchanged. This suggests that while the underlying backbone model may transiently register the presence of modified input, it does not integrate it in a behaviorally significant way.

These findings reinforce the presence of position-sensitive processing biases and suggest that increasing model capacity alone is insufficient to ensure faithful usage of retrieved condensed experience.

Table 7: Intervention results on two multi-hop question answering tasks under the ExpeL framework with Qwen3-14B backbone. The evaluation metric is exact match.

|  |  |  |
| --- | --- | --- |
|  | 2Wiki-MultiHopQA | Musique |
| ExpeL | 60 | 37 |
| Raw Experience Intervention | | |
| Empty | 58 | 42 |
| Shuffle | 55 | 42 |
| Irrelevant | 60 | 41 |
| Condensed Experience Intervention | | |
| Empty | 60 | 34 |
| Corrupt | 58 | 44 |
| Irrelevant | 59 | 40 |
| Filler | 56 | 44 |

### E.6 Additional Task-Specific Dependence Results

To ensure the robustness of this trend across model scales, we further report results on Qwen3-14B (Table [7](https://arxiv.org/html/2601.22436v2#A5.T7 "Table 7 ‣ E.5 Additional IG Attribution Results ‣ Appendix E Additional Experimental Results ‣ Large Language Model Agents Are Not Always Faithful Self-Evolvers")). These findings mirror the observations with Qwen3‑32B. Specifically, interventions on raw experience do not significantly hurt performance—sometimes even yielding higher scores. Similarly, condensed experience interventions exhibit no consistent degradation, and in Musique, several perturbed conditions (e.g., Corrupt or Filler) even outperform ExpeL.

These patterns reinforce the conclusion that neither raw nor condensed experience is causally utilized in these multi-hop tasks—even when reasoning is involved. Instead, models exhibit strong reliance on internal priors, rendering external experience unnecessary or even misleading.
