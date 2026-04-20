---
source: https://arxiv.org/html/2604.04503v2
description: MIA paper on converting deep-research search trajectories into workflow memory and Planner test-time training
captured: 2026-04-11
capture: lynx-html
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Memory Intelligence Agent

Author: Jingyang Qiao, Weicheng Meng, Yu Cheng, Zhihang Lin, Zhizhong Zhang, Xin Tan, Jingyu Gong, Kun Shao, Yuan Xie
Source: https://arxiv.org/html/2604.04503v2
Date: 2026-04-07

Abstract

   Deep research agents (DRAs) integrate LLM reasoning with external
   tools. Memory systems enable DRAs to leverage historical experiences,
   which are essential for efficient reasoning and autonomous evolution.
   Existing methods rely on retrieving similar trajectories from memory to
   aid reasoning, while suffering from key limitations of ineffective
   memory evolution and increasing storage and retrieval costs. To address
   these problems, we propose a novel Memory Intelligence Agent (MIA)
   framework, consisting of a Manager-Planner-Executor architecture.
   Memory Manager is a non-parametric memory system that can store
   compressed historical search trajectories. Planner is a parametric
   memory agent that can produce search plans for questions. Executor is
   another agent that can search and analyze information guided by the
   search plan. To build the MIA framework, we first adopt an alternating
   reinforcement learning paradigm to enhance cooperation between the
   Planner and the Executor. Furthermore, we enable the Planner to
   continuously evolve during test-time learning, with updates performed
   on-the-fly alongside inference without interrupting the reasoning
   process. Additionally, we establish a bidirectional conversion loop
   between parametric and non-parametric memories to achieve efficient
   memory evolution. Finally, we incorporate a reflection and an
   unsupervised judgment mechanisms to boost reasoning and self-evolution
   in the open world. Extensive experiments across eleven benchmarks
   demonstrate the superiority of MIA. First, MIA significantly enhances
   the current SOTA LLMs’ performance in deep research tasks. For
   instance, MIA further boosts GPT-5.4 performance by up to 9% and 6% on
   LiveVQA and HotpotQA, respectively. Furthermore, with the lightweight
   Executor, like Qwen2.5-VL-7B, MIA can also achieve an average
   improvement of 31% across evaluated datasets, outperforming the much
   larger Qwen2.5-VL-32B by a margin of 18%, highlighting its remarkable
   performance. Additionally, training analysis reveals that reinforcement
   learning enables the Planner and Executor to synergistically optimize
   their strategies, effectively capturing dataset-specific
   characteristics and enhancing cross-domain reasoning and memory
   capabilities. Tool analysis reveals that long-context memory methods
   struggle with multi-turn tool interaction, while our proposed MIA
   significantly outperforms previous methods. Under unsupervised
   settings, MIA achieves performance comparable to its supervised
   counterpart, meanwhile exhibiting the progressive self-evolution
   performance across multiple training iterations.
   \gtechdata

   [Code]https://github.com/ECNU-SII/MIA
   \gtechdata[Model]https://huggingface.co/LightningCreeper/MIA
   \gtechdata[Dataset]https://huggingface.co/datasets/LightningCreeper/MIA
   Refer to caption Figure 1: (a). Comparisons between frontier LLMs and
   their MIA-enhanced counterparts on the LiveVQA (multimodal) dataset.
   (b). Comparisons between frontier LLMs and their MIA-enhanced
   counterparts on the HotpotQA (text-only) dataset. (c). Comparisons
   between MIA based on Qwen2.5-VL-7B Executor with larger LLMs (in
   non-tool-calling settings) across seven diverse datasets. (d).
   Comparisons between MIA and SOTA memory frameworks based on
   Qwen-2.5-VL-7B Executor across seven diverse datasets.

   "Never memorize something that you can look up."

   —Albert Einstein

1 Introduction

   Deep Research Agents (DRAs) (Xu and Peng, 2025; Zhang et al., 2025c;
   Huang et al., 2025) can combine the reasoning capabilities of LLMs with
   external tools, such as search engines, thereby empowering LLMs to
   complete complex, open-ended tasks. Based on tool-augmented LLMs
   (Schmidgall et al., 2025; Parisi et al., 2022; Li et al., 2023; Ma et
   al., 2024), DRAs follow a multi-round paradigm with repeatedly
   interleaved reasoning and external searching (Li et al., 2025; Du et
   al., 2025; Huang et al., 2023). As agents evolve toward long-horizon,
   multi-turn interactions, memory systems become a critical component
   (Wang et al., 2025b; Lerman and Galstyan, 2003; Wang and Chen, 2025).
   They determine whether the agent can accumulate experience, refine
   search strategies, and improve during each research process rather than
   repeatedly solving each task from scratch (Li et al., 2024b; Gandon et
   al., 2002). Existing research on agent memory has mainly focused on
   long context scenarios (Zhang et al., 2025a; Rasmussen et al., 2025),
   where information is stored based on the traces of search experience.
   Although such approaches have shown promising performance in many
   agentic applications (Xiao et al., 2024), long-context memory exhibits
   fundamental limitations when applied to deep research agents (Li et
   al., 2024a; Shi et al., 2025; Wu et al., 2024). First, long contexts
   may dilute attention, hindering the model’s understanding of the
   current problem. Second, irrelevant or weakly related content in memory
   introduces noise, leading to degraded reasoning ability. Third,
   maintaining ever-growing context histories poses substantial storage
   challenges, particularly for agents operating continuously over
   extended periods. Finally, retrieval over massive memory incurs
   increasing computational costs, resulting in time inefficiency.

   Furthermore, long-context memory primarily captures knowledge-oriented
   or factual-oriented memory describing what the result is (e.g., user
   attributes, historical facts, and retrieved documents) (Wang et al.,
   2023; Yu et al., 2025; Kang et al., 2025). In contrast, deep research
   relies heavily on process-oriented memory (Fang et al., 2025) and
   conceptual knowledge describing how a result is obtained (e.g., search
   trajectories, failed attempts, and successful reasoning strategies).
   The objective of adopting memory is not merely to store retrieved
   knowledge, but to leverage historical experiences to guide future
   planning and exploration (Hu et al., 2025; Cao et al., 2025).
   Therefore, deep research agents require memory mechanisms that assist
   in search path planning and strategy reuse, rather than simply
   expanding the amount of stored textual context.

   To address the limitations of long-context memory applied in deep
   research agents, existing memory systems typically utilize pre-trained
   models as planners to generate chain-of-thought (CoT) prompting for
   search path planning with few-shot cases (Zhou et al., 2025). While
   such methods have improved the deep research performance, they still
   suffer from several key challenges: (1) The Planner operates without
   task-specific training, resulting in suboptimal planning. (2) Previous
   CoT-based prompting methods select few-shot examples only based on
   relevance, while neglecting quality, frequency, and other significant
   dimensions. (3) The Executor fails to adequately interpret and follow
   planning instructions without task-specific training. In summary, the
   essence of prior works can be characterized as an incompetent Planner
   retrieving memories from bloated memory and using non-comprehensive
   in-context prompts to guide an unprepared Executor in conducting deep
   research. Consequently, introducing memory systems yields limited
   performance improvements.

   To address these challenges, we propose the Memory Intelligence Agent
   (MIA), a novel framework that integrates brain-inspired memory
   mechanisms into a Manager-Planner-Executor architecture. Specifically,
   MIA employs a hippocampus-like episodic memory to extract insights from
   historical trajectories. Meanwhile, it consolidates historical
   trajectories into parametric memory via Planner training, reducing
   storage overhead. Then, it trains the Executor to follow and execute
   the generated plan, enabling synergistic co-evolution between the two
   agents. Finally, it introduces a reflection mechanism to develop the
   autonomous re-planning ability, paving the way for self-evolution under
   sparse annotations or unsupervised conditions. Extensive experiments
   demonstrate that (1) MIA significantly elevates the performance of
   state-of-the-art (SOTA) Executors. Specifically, it yields a 9%
   improvement on the LiveVQA benchmark and a 6% gain on HotpotQA when
   integrated with GPT-5.4, showcasing its ability to further enhance even
   the most powerful models. (2) MIA exhibits remarkable improvements for
   smaller Executors. Using Qwen2.5-VL-7B as the Executor, our framework
   achieves an average gain of 31% across seven diverse datasets, notably
   outperforming its much larger counterpart, Qwen2.5-VL-32B, by 18%. (3)
   Under unsupervised settings, MIA empowers the trained Executor to
   achieve a 7% performance boost. Furthermore, we observe consistent
   performance growth over multiple training iterations, validating the
   effectiveness of our autonomous evolution mechanism. (4) MIA sets a new
   state-of-the-art. Building on the Qwen2.5-VL-7B Executor, our approach
   consistently outperforms previous SOTA memory baselines by an average
   margin of 5% across all seven evaluated benchmarks.

   Our contributions are as follows:

   • We introduce a Manager-Planner-Executor architecture that addresses
   the storage bottlenecks and reasoning inefficiencies of conventional
   deep research agents by decoupling of historic memory, parametric
   planning and dynamic execution.

   • We propose an alternating RL paradigm to optimize the interplay
   between the Planner and Executor. This ensures that high-level planning
   and low-level retrieval are mutually aligned.

   • We develop a continual test-time learning mechanism, allowing the
   Planner to update its parametric knowledge during inference. This
   enables the agent to adapt to new information without interrupting the
   reasoning workflow.

   • We integrate reflection and unsupervised judgment mechanisms,
   endowing the agent with self-assessment and correction capabilities in
   open-ended tasks. This not only enhances reasoning robustness but also
   ensures continual evolution when facing unknown tasks.

   • MIA surpasses existing memory baselines and exhibits strong
   scalability, significantly enhancing the performance of both frontier
   and small-scale LLMs in deep research tasks.

2 Related Work

   Refer to caption Figure 2: A deep research process of MIA to tackle a
   complex and multi-hop question.

   Deep Research Agents: handle complex and dynamic tasks by iteratively
   prompting LLMs to perform external search and reason over retrieved
   results. However, without parameter optimization through the training
   process, LLMs fail to grasp effective tool calling and adapt to
   real-world environments. Recent methods, such as DeepResearcher (Zheng
   et al., 2025) and Search-R1 (Jin et al., 2025) have used reinforcement
   learning (RL) to enhance multi-turn search and retrieval-augmented
   generation, while they are confined to text-only tasks. Based on these
   foundations, MMSearch-R1 (Wu et al., 2025), and DeepMMSearch-R1
   (Narayan et al., 2025) further integrate multimodal search tools and
   significantly improves reasoning in multimodal search. Despite progress
   having been made in the integration of external retrieval and internal
   reasoning, challenges such as low efficiency in utilizing historical
   search information and past experiences still exist.

   Agent Memory Systems: ReasoningBank (Ouyang et al., 2025) and
   MemoryBank (Zhong et al., 2024) enhance the agent’s reasoning ability
   through the scalable expansion of memory. The ExpeL (Zhao et al., 2024)
   framework optimizes decision-making by learning from successful and
   failed experiences. Mem-
   [MATH: <semantics><mi>α</mi><annotation
   encoding="application/x-tex">\alpha</annotation></semantics> :MATH]
   (Wang et al., 2025a) and Memory-r1 (Yan et al., 2025) incorporate RL to
   model memory as a Markov decision process and guide agents to learn
   optimal memory storage strategies through reward signals. In memory
   management, Agentic Memory (Yu et al., 2026) and A-Mem (Xu et al.,
   2025) propose long-term and short-term memory and graph-based memory
   management paradigms, respectively, significantly improving the agent’s
   contextual scheduling capabilities in complex tasks. Memento (Zhou et
   al., 2025) proposes a different approach by exploring performance gains
   through memory fine-tuning while freezing the LLMs. In memory
   evolution, MemEvolve (Zhang et al., 2025b) drives dynamic adjustments
   of memory systems through higher-order meta-feedback, while Evo-Memory
   (Wei et al., 2025) constructs benchmarks to evaluate the autonomous
   evolution capability of memory systems during inference. Despite
   progress having been made in the construction and management of memory
   systems, challenges such as low memory efficiency, instability of
   results, and poor interpretability still exist. Additionally,
   autonomous evolution for memory systems in unsupervised environments is
   unexplored.
   Refer to caption Figure 3: Reasoning process of MIA consists of three
   parts: Inputs & Retrieval is for retrieving memory context similar to
   the inputs; Research Process is for driving Planner-Executor
   collaboration via a planning-execution-reflection loop; Outputs &
   Storage is for compressing search trajectories into structured memory.

3 Method

3.1 Overview

   Figure 3 illustrates the architecture and reasoning process of the
   proposed MIA. In the architecture, the Planner is an agent for
   generating a search plan for questions. The Executor is responsible for
   implementing the plan step by step until obtaining the final result.
   These two agents are initialized from pre-trained LLM (e.g., Qwen3-8B
   (Yang et al., 2025)) and LMM (e.g., Qwen2.5-VL-7B (Bai et al., 2025)).
   The Memory Manager is a system composed of a memory buffer and a
   pre-trained LLM (e.g., Qwen3-32B (Yang et al., 2025)). The memory
   buffer is responsible for saving high-value historical trajectories
   which serve as CoT cases. The pre-trained LLM is frozen and served to
   manage the buffer with context prompts. In the reasoning process, the
   Planner first analyzes historical cases to formulate a search plan for
   the current question. After that, the Executor interprets this plan,
   performing task reasoning in conjunction with tool usage, and provides
   feedback to the Planner to trigger reflection and determine the
   necessity of re-planning. Finally, the reasoning results and execution
   processes are submitted to the Memory Manager for further memory
   compression and structured organization.

   Figure 5 depicts the memory framework of MIA, which enables the agent’s
   lifelong learning through two complementary mechanisms: non-parametric
   memory for contrastive experience and parametric memory for long-term
   self-consolidation. Specifically, the non-parametric memory retrieves
   similar and high-value historical records to provide an explicit
   reference for the Planner. Meanwhile, the parametric memory distills
   latent knowledge representations from trajectories, internalizing them
   into the agent’s intrinsic capabilities to achieve evolution.

3.2 MIA Agent Loop

   MIA is equipped with a planning-execution-memory loop for the agent’s
   lifelong learning. As shown in Figure 3, the agent loop comprises three
   main stages: memory retrieval, collaborative reasoning, and experience
   consolidation. In summary, our objective is to enable the frozen agent
   to achieve lifelong evolution in a continuous data stream by leveraging
   MIA.

3.2.1 Memory Retrieval

   The deep research process initiates with the parsing of a multimodal
   query. At the beginning, the Memory Manager is empty, and memory
   retrieval is not employed. Once a sufficient amount of historical
   experiences (trajectories) have been accumulated, we retrieve similar
   past experience based on the current input. Specifically, the Memory
   Manager converts visual inputs into textual captions, aligning them
   with the storage format of the units in the Memory Manager. A hybrid
   retrieval strategy then scores each memory across the following three
   dimensions:
     * •
       Semantic Similarity: Measures the semantic distance between the
       current input and the historical questions and image captions
       stored in the memory units to ensure contextual relevance.
     * •
       Value Reward: Prioritizes memory units with high success rates to
       provide high-quality context.
     * •
       Frequency Reward: Rewards low-frequency memory units to encourage
       the exploration of long-tail, potentially relevant knowledge,
       thereby maintaining a balance in memory utilization.

   Based on these scores, MIA overcomes the limitations of conventional
   single-dimensional memory retrieval. The framework retrieves both
   successful trajectories (positive paradigms) and failed trajectories
   (negative constraints) to construct a rich contextual prior for
   planning. More details are provided in Appendix 10.

3.2.2 Collaborative Reasoning

   The core reasoning process is driven by the dynamic synergy between two
   trainable LLMs:
     * •
       Planner (Cognitive Hub): With the retrieved trajectories, it adopts
       a few-shot CoT strategy to decompose complex tasks into executable
       step-by-step sub-goals and generates a plan.
     * •
       Executor (Operational Terminal): After planning, it interacts with
       the environment via a ReAct loop according to the plan. By using
       external search tools and reasoning on the search results, it
       gathers and analyzes information to derive the final answer.

   Additionally, we design a dynamic feedback loop to connect the two
   agents: 1) The Executor reports execution status to the Planner after
   obtaining the final answer. 2) The Planner triggers Reflect-Replan
   mechanism to dynamically adjust the search plan conditioned on the
   execution feedback. For example, if the Executor encounters an impasse
   or unexpected environmental feedback, the Planner will generate a new
   plan, and the Executor will then proceed with the revised plan. To
   reduce reasoning time, the Reflect-Replan mechanism is triggered only
   once.
   Refer to caption Figure 4: Prompt for Memory Manager to extract image
   caption and workflow.

3.2.3 Experience Consolidation

   An LLM Judger is utilized to evaluate the final result. The Manager
   then compresses the current trajectories and updates the memory units.
   First, to reduce storage and retrieval burdens, images are compressed
   into captions, and verbose trajectories are abstracted into structured
   workflow summaries to form the new memory, as shown in Figure 4. A
   Qwen3-32B LLM is utilized to complete this compression task. After
   that, we calculate the semantic similarity between the new memory and
   existing memory units to conduct a high semantic similarity knowledge
   replacement. If no similar memory unit is found, the new memory is
   stored as a new memory unit. Concurrently, the value rewards and
   frequency counts of relevant units are also updated. Finally, we
   propose a real-time exploration and update strategy to retrain the
   Planner with the current batch of questions, trajectories, and results,
   thereby internalizing episodic memory into parametric memory. This
   strategy enables further memory compression and efficient memory
   extraction. After training, the memory units will be selectively
   cleared. This prevents memory explosion while retaining critical
   information.

3.3 Two-Stage Alternating RL Training

   Aiming to enhance the collaborative reasoning and promote the
   connection between the Planner and the Executor, we propose a two-stage
   alternating RL training strategy based on Group Relative Policy
   Optimization (GRPO) (Shao et al., 2024) in the training process. In
   stage 1, we focus on training the Executor to understand and follow the
   plan generated by the Planner, further improving the reasoning
   capability of the Executor. The Planner is frozen as a server to
   provide plans. After training in stage 1, we utilize the Planner and
   the trained Executor to collect training data containing memory
   contexts. In stage 2, we freeze the Executor and deploy it as a server.
   Based on the collected contexts, we conduct RL on the Planner to
   enhance its plan generation and reflection capabilities.

3.3.1 Executor RL Training

   To endow the Executor with the capabilities of deep reasoning, tool
   calling under the ReAct (Yao et al., 2023) paradigm, as well as to
   enable it to accurately parse the Plan and Replan instructions
   generated by the Planner, we extend the GRPO objective function based
   on the interaction between tools and the Planner:
   [MATH: <semantics><mrow><mrow><msubsup><mi
   class="ltx_font_mathcaligraphic">𝒥</mi><mrow><mi>G</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>R</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>P</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>O</mi></mrow><msub><mi>M</mi><mi>E</mi></msub></
   msubsup><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>θ</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo
   rspace="0.448em">=</mo><mi></mi></mrow><annotation
   encoding="application/x-tex">\displaystyle\mathcal{J}_{GRPO}^{M_{E}}(\t
   heta)=\,</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><msub><mi>𝔼</mi><mrow><mi>x</mi><mo>∼</mo><mi
   class="ltx_font_mathcaligraphic">𝒟</mi><mo>,</mo><msubsup><mrow><mo
   stretchy="false">{</mo><msub><mi>y</mi><mi>i</mi></msub><mo
   stretchy="false">}</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mro
   w><mi>G</mi></msubsup><mo>∼</mo><msub><mi>π</mi><mtext>old</mtext></msu
   b><mrow><mo stretchy="false">(</mo><mo lspace="0em"
   rspace="0em">⋅</mo><mo fence="false" rspace="0.167em"
   stretchy="false">|</mo><mi>x</mi><mo>;</mo><msub><mi>s</mi><mi>e</mi></
   msub><mo>,</mo><msub><mi>M</mi><mi>P</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow></msub><mrow><mo maxsize="2.600em"
   minsize="2.600em">[</mo><mstyle
   displaystyle="true"><mfrac><mn>1</mn><mi>G</mi></mfrac></mstyle><mstyle
   displaystyle="true"><munderover><mo
   movablelimits="false">∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow>
   <mi>G</mi></munderover></mstyle><mstyle
   displaystyle="true"><mfrac><mn>1</mn><mrow><msubsup><mo>∑</mo><mrow><mi
   >t</mi><mo>=</mo><mn>1</mn></mrow><mrow><mo
   stretchy="false">|</mo><msub><mi>y</mi><mi>i</mi></msub><mo
   stretchy="false">|</mo></mrow></msubsup><mrow><mi>I</mi><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mi>t<
   /mi></mrow></msub><mo
   stretchy="false">)</mo></mrow></mrow></mrow></mfrac></mstyle><mstyle
   displaystyle="true"><munderover><mo
   movablelimits="false">∑</mo><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow>
   <mrow><mo stretchy="false">|</mo><msub><mi>y</mi><mi>i</mi></msub><mo
   stretchy="false">|</mo></mrow></munderover></mstyle><mi>min</mi><mrow><
   mo maxsize="2.600em" minsize="2.600em">(</mo><mstyle
   displaystyle="true"><mfrac><mrow><msub><mi>π</mi><mi>θ</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>x</mi><mo>,</mo><msub><mi>y</mi><mrow><mi
   >i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi></mrow></mrow></msu
   b><mo>;</mo><msub><mi>s</mi><mi>e</mi></msub><mo>,</mo><msub><mi>M</mi>
   <mi>P</mi></msub></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mrow><msub><mi>π</mi><mtext>old</
   mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>x</mi><mo>,</mo><msub><mi>y</mi><mrow><mi
   >i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi></mrow></mrow></msu
   b><mo>;</mo><msub><mi>s</mi><mi>e</mi></msub><mo>,</mo><msub><mi>M</mi>
   <mi>P</mi></msub></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mfrac></mstyle></mrow></mrow></m
   row><annotation
   encoding="application/x-tex">\displaystyle\mathbb{E}_{x\sim\mathcal{D},
   \{y_{i}\}_{i=1}^{G}\sim\pi_{\text{old}}(\cdot|x;s_{e},M_{P})}\Bigg[\fra
   c{1}{G}\sum_{i=1}^{G}\frac{1}{\sum_{t=1}^{|y_{i}|}I(y_{i,t})}\sum_{t=1}
   ^{|y_{i}|}\min\Bigg(\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t};s_{e},M_{P})}
   {\pi_{\text{old}}(y_{i,t}|x,y_{i,<t};s_{e},M_{P})}</annotation></semant
   ics> :MATH]
   [MATH: <semantics><mrow><mrow><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mrow><mi>i</mi><mo>,</mo><mi
   >t</mi></mrow></msub><mo>,</mo><mtext>clip</mtext><mrow><mo
   maxsize="2.600em" minsize="2.600em">(</mo><mstyle
   displaystyle="true"><mfrac><mrow><msub><mi>π</mi><mi>θ</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>x</mi><mo>,</mo><msub><mi>y</mi><mrow><mi
   >i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi></mrow></mrow></msu
   b><mo>;</mo><msub><mi>s</mi><mi>e</mi></msub><mo>,</mo><msub><mi>M</mi>
   <mi>P</mi></msub></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mrow><msub><mi>π</mi><mtext>old</
   mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>x</mi><mo>,</mo><msub><mi>y</mi><mrow><mi
   >i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi></mrow></mrow></msu
   b><mo>;</mo><msub><mi>s</mi><mi>e</mi></msub><mo>,</mo><msub><mi>M</mi>
   <mi>P</mi></msub></mrow></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mfrac></mstyle><mo>,</mo><mn>1</
   mn><mo>−</mo><mi>ϵ</mi><mo>,</mo><mn>1</mn><mo>+</mo><mi>ϵ</mi><mo
   maxsize="2.600em" minsize="2.600em">)</mo></mrow><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mrow><mi>i</mi><mo>,</mo><mi
   >t</mi></mrow></msub><mo maxsize="2.600em"
   minsize="2.600em">)</mo></mrow><mo>−</mo><mi>β</mi><msub><mi>𝔻</mi><mro
   w><mi>K</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>L</mi></mrow></msub><mrow><mo>[</mo><msub><mi>π<
   /mi><mi>θ</mi></msub><mo fence="false" rspace="0.167em"
   stretchy="false">|</mo><mo fence="false" rspace="0.167em"
   stretchy="false">|</mo><msub><mi>π</mi><mtext>ref</mtext></msub><mo>]</
   mo></mrow><mo maxsize="2.600em"
   minsize="2.600em">]</mo><mo>,</mo></mrow><annotation
   encoding="application/x-tex">\displaystyle\hat{A}_{i,t},\text{clip}\Big
   g(\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t};s_{e},M_{P})}{\pi_{\text{old}}(
   y_{i,t}|x,y_{i,<t};s_{e},M_{P})},1-\epsilon,1+\epsilon\Bigg)\hat{A}_{i,
   t}\Bigg)-\beta\mathbb{D}_{KL}\left[\pi_{\theta}||\pi_{\text{ref}}\right
   ]\Bigg],</annotation></semantics> :MATH]
   (1)

   where
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   and
   [MATH: <semantics><msub><mi>π</mi><mtext>old</mtext></msub><annotation
   encoding="application/x-tex">\pi_{\text{old}}</annotation></semantics>
   :MATH]
   represent the current and previous policy models,
   [MATH: <semantics><msub><mi>π</mi><mtext>ref</mtext></msub><annotation
   encoding="application/x-tex">\pi_{\text{ref}}</annotation></semantics>
   :MATH]
   is the reference model.
   [MATH: <semantics><msub><mi>𝔻</mi><mrow><mi>K</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>L</mi></mrow></msub><annotation
   encoding="application/x-tex">\mathbb{D}_{KL}</annotation></semantics>
   :MATH]
   refers to the KL-divergence.
   [MATH: <semantics><mi>x</mi><annotation
   encoding="application/x-tex">x</annotation></semantics> :MATH]
   denotes input samples drawn from the dataset
   [MATH: <semantics><mi>D</mi><annotation
   encoding="application/x-tex">D</annotation></semantics> :MATH]
   , including <question> and <image>.
   [MATH: <semantics><mi>ϵ</mi><annotation
   encoding="application/x-tex">\epsilon</annotation></semantics> :MATH]
   and
   [MATH: <semantics><mi>β</mi><annotation
   encoding="application/x-tex">\beta</annotation></semantics> :MATH]
   are hyperparameters.
   [MATH: <semantics><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mrow><mi>i</mi><mo>,</mo><mi
   >t</mi></mrow></msub><annotation
   encoding="application/x-tex">\hat{A}_{i,t}</annotation></semantics>
   :MATH]
   indicates the advantage, computed based on the relative rewards of
   outputs within each group.
   [MATH: <semantics><msub><mi>S</mi><mi>e</mi></msub><annotation
   encoding="application/x-tex">S_{e}</annotation></semantics> :MATH]
   refers to historical trajectories.
   [MATH: <semantics><msub><mi>M</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">M_{P}</annotation></semantics> :MATH]
   is the Planner.
   [MATH: <semantics><mi>y</mi><annotation
   encoding="application/x-tex">y</annotation></semantics> :MATH]
   expresses the interleaved trajectory generated by the interaction among
   the policy model, toolset, and Planner.
   [MATH: <semantics><mrow><mi>I</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mi>t<
   /mi></mrow></msub><mo stretchy="false">)</mo></mrow></mrow><annotation
   encoding="application/x-tex">I(y_{i,t})</annotation></semantics> :MATH]
   is a token loss masking operation:
   [MATH: <semantics><mrow><mrow><mi>I</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mi>t<
   /mi></mrow></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>1</mn></mrow><annota
   tion encoding="application/x-tex">I(y_{i,t})=1</annotation></semantics>
   :MATH]
   if
   [MATH:
   <semantics><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mi>t</mi></mrow><
   /msub><annotation
   encoding="application/x-tex">y_{i,t}</annotation></semantics> :MATH]
   is generated by
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   , and
   [MATH: <mn>0</mn> :MATH]
   if it is generated by tools or the Planner. The rollout process is
   shown in Table 1.
   Table 1: Executor Training Rollout Process.
   Step Action / Description
   Step 1 Provide <question> to Planner to obtain the initial plan.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 2.
   Step 2 Input <question>, <image>, and initial plan to the policy model.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 3.
   Step 3 Generate thought(<think>) and action(<tool_call> or <answer>)
   based on current state. If a tool call is needed
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 4; otherwise, generate candidate answer
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 5.
   Step 4 Execute the corresponding tool and append the returned
   observation.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 3.
   Step 5 LLM Judger evaluates the candidate answer. If correct
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 7; otherwise
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 6.
   Step 6 Provide interaction history to Planner to get a revised plan.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 3. (Note: This action triggers at most once; if already triggered
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 7).
   Step 7 Output the final response.

   The reward function serves as the primary signal guiding the RL
   optimization. To train the Executor, we design a rule-based composite
   reward function:
   [MATH:
   <semantics><mrow><mrow><mrow><msub><mi>r</mi><msub><mi>M</mi><mi>E</mi>
   </msub></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mrow><mrow><mn>0.
   7</mn><mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>1</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>a</mi><mtext>pred</mtext></msub><mo>,<
   /mo><msub><mi>a</mi><mtext>gold</mtext></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mrow><mn>0.2</mn>
   <mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>2</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>y</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mrow><mn>0.1</mn>
   <mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>3</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>y</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow></mrow><mo>,</mo></mrow><an
   notation encoding="application/x-tex">\displaystyle
   r_{M_{E}}(x,y)=0.7*r_{1}(a_{\text{pred}},a_{\text{gold}})+0.2*r_{2}(y)+
   0.1*r_{3}(y),</annotation></semantics> :MATH]
   (2)

   where
   [MATH: <semantics><msub><mi>a</mi><mtext>pred</mtext></msub><annotation
   encoding="application/x-tex">a_{\text{pred}}</annotation></semantics>
   :MATH]
   is the final answer extracted from the response
   [MATH: <semantics><mi>y</mi><annotation
   encoding="application/x-tex">y</annotation></semantics> :MATH]
   , and
   [MATH: <semantics><msub><mi>a</mi><mtext>gold</mtext></msub><annotation
   encoding="application/x-tex">a_{\text{gold}}</annotation></semantics>
   :MATH]
   is the ground truth.
   [MATH: <semantics><msub><mi>r</mi><mn>3</mn></msub><annotation
   encoding="application/x-tex">r_{3}</annotation></semantics> :MATH]
   represents the format reward, which is
   [MATH: <semantics><mn>1</mn><annotation
   encoding="application/x-tex">1</annotation></semantics> :MATH]
   if the output format complies with the specifications, and
   [MATH: <mn>0</mn> :MATH]
   otherwise.
   [MATH: <semantics><msub><mi>r</mi><mn>2</mn></msub><annotation
   encoding="application/x-tex">r_{2}</annotation></semantics> :MATH]
   denotes the tool reward, which is
   [MATH: <semantics><mn>1</mn><annotation
   encoding="application/x-tex">1</annotation></semantics> :MATH]
   if there is a successful and standardized tool call, and
   [MATH: <mn>0</mn> :MATH]
   otherwise.
   [MATH: <semantics><msub><mi>r</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">r_{1}</annotation></semantics> :MATH]
   indicates the correctness reward evaluated by the LLM Judger, which is
   [MATH: <semantics><mn>1</mn><annotation
   encoding="application/x-tex">1</annotation></semantics> :MATH]
   if the predicted answer
   [MATH: <semantics><msub><mi>a</mi><mtext>pred</mtext></msub><annotation
   encoding="application/x-tex">a_{\text{pred}}</annotation></semantics>
   :MATH]
   matches the ground truth
   [MATH: <semantics><msub><mi>a</mi><mtext>gold</mtext></msub><annotation
   encoding="application/x-tex">a_{\text{gold}}</annotation></semantics>
   :MATH]
   , and
   [MATH: <mn>0</mn> :MATH]
   otherwise.

3.3.2 Planner RL Training

   Based on the trained Executor, which possesses instruction parsing and
   reasoning capabilities, stage 2 aims to optimize the Planner by
   incorporating memory contexts. The objective is to enhance the
   Planner’s ability to absorb memory, plan for complex questions, and
   reflect on the feedback from the Executor. We extend the GRPO objective
   function based on the memory context and the Executor:
   [MATH: <semantics><mrow><mrow><msubsup><mi
   class="ltx_font_mathcaligraphic">𝒥</mi><mrow><mi>G</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>R</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>P</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>O</mi></mrow><msub><mi>M</mi><mi>P</mi></msub></
   msubsup><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>θ</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo
   rspace="0.448em">=</mo><mi></mi></mrow><annotation
   encoding="application/x-tex">\displaystyle\mathcal{J}_{GRPO}^{M_{P}}(\t
   heta)=\,</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><msub><mi>𝔼</mi><mrow><mi>x</mi><mo>∼</mo><mi
   class="ltx_font_mathcaligraphic">𝒟</mi><mo>,</mo><msubsup><mrow><mo
   stretchy="false">{</mo><msub><mi>y</mi><mi>i</mi></msub><mo
   stretchy="false">}</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mro
   w><mi>G</mi></msubsup><mo>∼</mo><msub><mi>π</mi><mtext>old</mtext></msu
   b><mrow><mo stretchy="false">(</mo><mo lspace="0em"
   rspace="0em">⋅</mo><mo fence="false" rspace="0.167em"
   stretchy="false">|</mo><mi>m</mi><mo>,</mo><mi>x</mi><mo>;</mo><msub><m
   i>M</mi><mi>E</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow></msub><mrow><mo maxsize="2.600em"
   minsize="2.600em">[</mo><mstyle
   displaystyle="true"><mfrac><mn>1</mn><mi>G</mi></mfrac></mstyle><mstyle
   displaystyle="true"><munderover><mo
   movablelimits="false">∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow>
   <mi>G</mi></munderover></mstyle><mstyle
   displaystyle="true"><mfrac><mn>1</mn><mrow><msubsup><mo>∑</mo><mrow><mi
   >t</mi><mo>=</mo><mn>1</mn></mrow><mrow><mo
   stretchy="false">|</mo><msub><mi>y</mi><mi>i</mi></msub><mo
   stretchy="false">|</mo></mrow></msubsup><mrow><mi>I</mi><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mi>t<
   /mi></mrow></msub><mo
   stretchy="false">)</mo></mrow></mrow></mrow></mfrac></mstyle><mstyle
   displaystyle="true"><munderover><mo
   movablelimits="false">∑</mo><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow>
   <mrow><mo stretchy="false">|</mo><msub><mi>y</mi><mi>i</mi></msub><mo
   stretchy="false">|</mo></mrow></munderover></mstyle><mi>min</mi><mrow><
   mo maxsize="2.600em" minsize="2.600em">(</mo><mstyle
   displaystyle="true"><mfrac><mrow><msub><mi>π</mi><mi>θ</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>m</mi><mo>,</mo><mi>x</mi><mo>,</mo><msub
   ><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi
   ></mrow></mrow></msub><mo>;</mo><msub><mi>M</mi><mi>E</mi></msub></mrow
   ></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mrow><msub><mi>π</mi><mtext>old</
   mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>m</mi><mo>,</mo><mi>x</mi><mo>,</mo><msub
   ><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi
   ></mrow></mrow></msub><mo>;</mo><msub><mi>M</mi><mi>E</mi></msub></mrow
   ></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mfrac></mstyle></mrow></mrow></m
   row><annotation
   encoding="application/x-tex">\displaystyle\mathbb{E}_{x\sim\mathcal{D},
   \{y_{i}\}_{i=1}^{G}\sim\pi_{\text{old}}(\cdot|m,x;M_{E})}\Bigg[\frac{1}
   {G}\sum_{i=1}^{G}\frac{1}{\sum_{t=1}^{|y_{i}|}I(y_{i,t})}\sum_{t=1}^{|y
   _{i}|}\min\Bigg(\frac{\pi_{\theta}(y_{i,t}|m,x,y_{i,<t};M_{E})}{\pi_{\t
   ext{old}}(y_{i,t}|m,x,y_{i,<t};M_{E})}</annotation></semantics> :MATH]
   [MATH: <semantics><mrow><mrow><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mrow><mi>i</mi><mo>,</mo><mi
   >t</mi></mrow></msub><mo>,</mo><mtext>clip</mtext><mrow><mo
   maxsize="2.600em" minsize="2.600em">(</mo><mstyle
   displaystyle="true"><mfrac><mrow><msub><mi>π</mi><mi>θ</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>m</mi><mo>,</mo><mi>x</mi><mo>,</mo><msub
   ><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi
   ></mrow></mrow></msub><mo>;</mo><msub><mi>M</mi><mi>E</mi></msub></mrow
   ></mrow><mo
   stretchy="false">)</mo></mrow></mrow><mrow><msub><mi>π</mi><mtext>old</
   mtext></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mrow><msub><mi>y</mi><mrow><mi>i</mi><mo>,</mo>
   <mi>t</mi></mrow></msub><mo
   fence="false">|</mo><mrow><mi>m</mi><mo>,</mo><mi>x</mi><mo>,</mo><msub
   ><mi>y</mi><mrow><mi>i</mi><mo>,</mo><mrow><mi></mi><mo><</mo><mi>t</mi
   ></mrow></mrow></msub><mo>;</mo><msub><mi>M</mi><mi>E</mi></msub></mrow
   ></mrow><mo
   stretchy="false">)</mo></mrow></mrow></mfrac></mstyle><mo>,</mo><mn>1</
   mn><mo>−</mo><mi>ϵ</mi><mo>,</mo><mn>1</mn><mo>+</mo><mi>ϵ</mi><mo
   maxsize="2.600em" minsize="2.600em">)</mo></mrow><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mrow><mi>i</mi><mo>,</mo><mi
   >t</mi></mrow></msub><mo maxsize="2.600em"
   minsize="2.600em">)</mo></mrow><mo>−</mo><mi>β</mi><msub><mi>𝔻</mi><mro
   w><mi>K</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>L</mi></mrow></msub><mrow><mo>[</mo><msub><mi>π<
   /mi><mi>θ</mi></msub><mo fence="false" rspace="0.167em"
   stretchy="false">|</mo><mo fence="false" rspace="0.167em"
   stretchy="false">|</mo><msub><mi>π</mi><mtext>ref</mtext></msub><mo>]</
   mo></mrow><mo maxsize="2.600em"
   minsize="2.600em">]</mo><mo>,</mo></mrow><annotation
   encoding="application/x-tex">\displaystyle\hat{A}_{i,t},\text{clip}\Big
   g(\frac{\pi_{\theta}(y_{i,t}|m,x,y_{i,<t};M_{E})}{\pi_{\text{old}}(y_{i
   ,t}|m,x,y_{i,<t};M_{E})},1-\epsilon,1+\epsilon\Bigg)\hat{A}_{i,t}\Bigg)
   -\beta\mathbb{D}_{KL}\left[\pi_{\theta}||\pi_{\text{ref}}\right]\Bigg],
   </annotation></semantics> :MATH]
   (3)

   where
   [MATH: <semantics><mi>m</mi><annotation
   encoding="application/x-tex">m</annotation></semantics> :MATH]
   denotes the retrieved memory context.
   [MATH: <semantics><msub><mi>M</mi><mi>E</mi></msub><annotation
   encoding="application/x-tex">M_{E}</annotation></semantics> :MATH]
   represents the Executor trained in stage 1.
   [MATH: <semantics><mi>y</mi><annotation
   encoding="application/x-tex">y</annotation></semantics> :MATH]
   denotes the interleaved response trajectory generated by the
   interaction between the Planner and the Executor. The rollout process
   during the Planner training is shown in Table 2.
   Table 2: Planner Training Rollout Process.
   Step Action / Description
   Step 1 Input the memory context, <question>, and prompt template to the
   policy model.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 2.
   Step 2 Perform rollout to generate initial plan through CoT.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 3.
   Step 3 Executor interacts with the environment using <question>,
   <image>, tools, and initial plan, yielding the candidate trajectory and
   result.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 4.
   Step 4 Analyze candidate trajectory. If interaction should terminate
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 7; otherwise
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 5.
   Step 5 Perform rollout to generate CoT reflection and revised plan.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 6.
   Step 6 Executor continues interaction based on candidate trajectory and
   revised plan, yielding final trajectory and result.
   [MATH: <semantics><mo mathsize="0.900em">⊳</mo><annotation
   encoding="application/x-tex">\triangleright</annotation></semantics>
   :MATH]
   Step 7.
   Step 7 Output the final response.

   The reward function for the Planner training comprises the following
   four dimensions:
   [MATH:
   <semantics><mrow><mrow><mrow><msub><mi>r</mi><msub><mi>M</mi><mi>P</mi>
   </msub></msub><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mrow><mrow><mn>0.
   7</mn><mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>1</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msubsup><mi>a</mi><mtext>pred</mtext><mn>2</mn>
   </msubsup><mo>,</mo><msub><mi>a</mi><mtext>gold</mtext></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mrow><mn>0.2</mn>
   <mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>1</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msubsup><mi>a</mi><mtext>pred</mtext><mn>1</mn>
   </msubsup><mo>,</mo><msub><mi>a</mi><mtext>gold</mtext></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mrow><mn>0.05</mn
   ><mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>2</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>y</mi><mo>,</mo><msub><mi>a</mi><mtext>gold<
   /mtext></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mrow><mn>0.05</mn
   ><mo lspace="0.222em"
   rspace="0.222em">∗</mo><msub><mi>r</mi><mn>3</mn></msub></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>y</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow></mrow><mo>,</mo></mrow><an
   notation encoding="application/x-tex">\displaystyle
   r_{M_{P}}(x,y)=0.7*r_{1}(a_{\text{pred}}^{2},a_{\text{gold}})+0.2*r_{1}
   (a_{\text{pred}}^{1},a_{\text{gold}})+0.05*r_{2}(y,a_{\text{gold}})+0.0
   5*r_{3}(y),</annotation></semantics> :MATH]
   (4)

   where
   [MATH:
   <semantics><msubsup><mi>a</mi><mtext>pred</mtext><mn>1</mn></msubsup><a
   nnotation
   encoding="application/x-tex">a_{\text{pred}}^{1}</annotation></semantic
   s> :MATH]
   is the intermediate answer, and
   [MATH:
   <semantics><msubsup><mi>a</mi><mtext>pred</mtext><mn>2</mn></msubsup><a
   nnotation
   encoding="application/x-tex">a_{\text{pred}}^{2}</annotation></semantic
   s> :MATH]
   is the final answer. The two answers are equivalent if no reflection
   occurs.
   [MATH: <semantics><msub><mi>r</mi><mn>3</mn></msub><annotation
   encoding="application/x-tex">r_{3}</annotation></semantics> :MATH]
   represents the format reward.
   [MATH: <semantics><msub><mi>r</mi><mn>2</mn></msub><annotation
   encoding="application/x-tex">r_{2}</annotation></semantics> :MATH]
   indicates the reflection reward, which is designed to encourage an
   effective reflection mechanism (which is 1 if the first interaction is
   correct and reflection is uninitiated, or if the interaction is
   incorrect and reflection is initiated; otherwise, it is 0).
   [MATH: <semantics><msub><mi>r</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">r_{1}</annotation></semantics> :MATH]
   refers to the correctness reward evaluated by the LLM Judger.
   Refer to caption Figure 5: The Executor is activated during the
   first-stage RL training and frozen in the test-time RL process, while
   the Planner is activated during both the second-stage RL training and
   the test-time RL process. The memory framework of MIA during
   exploration: (1) generating multiple plan rollouts; (2) executing the
   inference pipeline, where a router selects the optimal plan based on
   prior experience to interact with the environment, strictly ensuring no
   label leakage; (3) receiving the final feedback from the environment;
   and (4) completing the training pipeline by calculating rewards and
   advantages for all rollouts. These evaluations are then used to update
   both the parametric memory (updating the Planner’s parameters via GRPO)
   and the non-parametric memory (extracting workflows into the Memory
   Manager).

3.4 Test Time Learning

   In the test-time learning (TTL) process, MIA introduces a novel memory
   framework that injects historical experiences via two dimensions:
   context and parameters. Specifically, retrieved workflows serve as
   non-parametric memory for in-context contrastive learning, while
   exploration trajectories continuously update the Planner’s parameters
   as parametric memory to enhance the agent’s reasoning capabilities.
   Unlike offline training, parameters update in the TTL cannot rely on
   pre-collected memory contexts or multi-epoch rollout. As shown in
   Figure 5, MIA adopts an online learning paradigm that performs
   exploration, storage, and learning simultaneously for each batch of
   test data.

3.4.1 Non-parametric Memory

   To continuously enrich the explicit memory base, we design a systematic
   pipeline to extract and store representative interaction workflows as
   non-parametric memory. Input the text query
   [MATH: <semantics><mi>x</mi><annotation
   encoding="application/x-tex">x</annotation></semantics> :MATH]
   and the retrieved memory
   [MATH: <semantics><mi>m</mi><annotation
   encoding="application/x-tex">m</annotation></semantics> :MATH]
   , the Planner
   [MATH: <semantics><msub><mi>π</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">\pi_{P}</annotation></semantics> :MATH]
   generates
   [MATH: <semantics><mi>G</mi><annotation
   encoding="application/x-tex">G</annotation></semantics> :MATH]
   candidate plans:
   [MATH: <semantics><mrow><msubsup><mrow><mo
   stretchy="false">{</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>t</mi><mi>i</mi></msub><mo>,</mo><msub
   ><mi>p</mi><mi>i</mi></msub><mo stretchy="false">)</mo></mrow><mo
   stretchy="false">}</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mro
   w><mi>G</mi></msubsup><mo>∼</mo><msub><mi>π</mi><mi>P</mi></msub><mrow>
   <mo stretchy="false">(</mo><mo lspace="0em" rspace="0em">⋅</mo><mo
   fence="false" rspace="0.167em"
   stretchy="false">|</mo><mi>m</mi><mo>,</mo><mi>x</mi><mo
   stretchy="false">)</mo></mrow><mo>,</mo></mrow><annotation
   encoding="application/x-tex">\{(t_{i},p_{i})\}_{i=1}^{G}\sim\pi_{P}(\cd
   ot|m,x),</annotation></semantics> :MATH]
   where
   [MATH: <semantics><msub><mi>t</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">t_{i}</annotation></semantics> :MATH]
   represents the CoT, and
   [MATH: <semantics><msub><mi>p</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">p_{i}</annotation></semantics> :MATH]
   is the memory enhancement plan. Next, given the text query
   [MATH: <semantics><mi>x</mi><annotation
   encoding="application/x-tex">x</annotation></semantics> :MATH]
   , the image
   [MATH: <semantics><mi
   class="ltx_font_mathcaligraphic">ℐ</mi><annotation
   encoding="application/x-tex">\mathcal{I}</annotation></semantics>
   :MATH]
   , and the plan
   [MATH: <semantics><msub><mi>p</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">p_{i}</annotation></semantics> :MATH]
   , the Executor interacts with the environment to generate
   [MATH: <semantics><mi>G</mi><annotation
   encoding="application/x-tex">G</annotation></semantics> :MATH]
   trajectories:
   [MATH:
   <semantics><mrow><mrow><mrow><msub><mi>τ</mi><mi>i</mi></msub><mo>=</mo
   ><mrow><msub><mi>M</mi><mi>E</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>p</mi><mi>i</mi></msub><mo>,</mo><mi>x
   </mi><mo>,</mo><mi
   class="ltx_font_mathcaligraphic">ℐ</mi><mo>,</mo><mtext>Env</mtext><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo
   rspace="1.167em">,</mo><mrow><mi>i</mi><mo>∈</mo><mrow><mo
   stretchy="false">{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mi
   mathvariant="normal">…</mi><mo>,</mo><mi>G</mi><mo
   stretchy="false">}</mo></mrow></mrow></mrow><mo>,</mo></mrow><annotatio
   n
   encoding="application/x-tex">\tau_{i}=M_{E}(p_{i},x,\mathcal{I},\text{E
   nv}),\quad i\in\{1,2,\dots,G\},</annotation></semantics> :MATH]
   where
   [MATH: <semantics><msub><mi>τ</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">\tau_{i}</annotation></semantics> :MATH]
   encapsulates the entire sequence of tool calls, environmental
   observations, and intermediate reasoning steps. Subsequently, the
   Planner evaluates whether to trigger reflection. If necessary, it
   generates a supplementary plan, which is then fed to the Executor to
   extend the corresponding trajectory
   [MATH: <semantics><msub><mi>τ</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">\tau_{i}</annotation></semantics> :MATH]
   .

   After an LLM Judger evaluates the correctness of the final answer to
   categorize the trajectories into successful (
   [MATH: <semantics><msub><mi
   class="ltx_font_mathcaligraphic">𝒯</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub><annotation
   encoding="application/x-tex">\mathcal{T}_{succ}</annotation></semantics
   > :MATH]
   ) and failed (
   [MATH: <semantics><msub><mi
   class="ltx_font_mathcaligraphic">𝒯</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub><annotation
   encoding="application/x-tex">\mathcal{T}_{fail}</annotation></semantics
   > :MATH]
   ) sets, the Memory Manager selectively extracts and compresses this
   experience to update the non-parametric memory:
     * •
       Positive Paradigm Extraction: If
       [MATH: <semantics><mrow><msub><mi
       class="ltx_font_mathcaligraphic">𝒯</mi><mrow><mi>s</mi><mo
       lspace="0em" rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>c</mi></mrow></msub><mo>≠</mo><mi
       mathvariant="normal">∅</mi></mrow><annotation
       encoding="application/x-tex">\mathcal{T}_{succ}\neq\emptyset</annot
       ation></semantics> :MATH]
       , we select the trajectory with the shortest execution path to
       encourage reasoning efficiency:
       [MATH: <semantics><mrow><msubsup><mi>τ</mi><mrow><mi>s</mi><mo
       lspace="0em" rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>c</mi></mrow><mo>∗</mo></msubsup><mo>=</mo><
       mrow><mrow><mi>arg</mi><mo
       lspace="0.167em">⁡</mo><mrow><msub><mi>min</mi><mrow><mi>τ</mi><mo>
       ∈</mo><msub><mi
       class="ltx_font_mathcaligraphic">𝒯</mi><mrow><mi>s</mi><mo
       lspace="0em" rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>c</mi></mrow></msub></mrow></msub><mo
       lspace="0.167em">⁡</mo><mtext>length</mtext></mrow></mrow><mo
       lspace="0em" rspace="0em">​</mo><mrow><mo
       stretchy="false">(</mo><mi>τ</mi><mo
       stretchy="false">)</mo></mrow></mrow></mrow><annotation
       encoding="application/x-tex">\tau_{succ}^{*}=\arg\min_{\tau\in\math
       cal{T}_{succ}}\text{length}(\tau)</annotation></semantics> :MATH]
       .
     * •
       Negative Paradigm Extraction: If
       [MATH: <semantics><mrow><msub><mi
       class="ltx_font_mathcaligraphic">𝒯</mi><mrow><mi>f</mi><mo
       lspace="0em" rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>l</mi></mrow></msub><mo>≠</mo><mi
       mathvariant="normal">∅</mi></mrow><annotation
       encoding="application/x-tex">\mathcal{T}_{fail}\neq\emptyset</annot
       ation></semantics> :MATH]
       , we randomly sample one failed trajectory
       [MATH: <semantics><mrow><msubsup><mi>τ</mi><mrow><mi>f</mi><mo
       lspace="0em" rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>l</mi></mrow><mo>∗</mo></msubsup><mo>∼</mo><
       msub><mi class="ltx_font_mathcaligraphic">𝒯</mi><mrow><mi>f</mi><mo
       lspace="0em" rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
       rspace="0em">​</mo><mi>l</mi></mrow></msub></mrow><annotation
       encoding="application/x-tex">\tau_{fail}^{*}\sim\mathcal{T}_{fail}<
       /annotation></semantics> :MATH]
       to capture diverse error patterns and prevent future pitfalls.

   The selected trajectories are then compressed into structured workflow
   summaries and stored in the Memory Manager, providing explicit
   contrastive references for future questions.

3.4.2 Parametric Memory

   To maintain execution stability and computational efficiency, parameter
   updates are exclusively applied to the Planner. Serving as the
   cognitive brain of the system, the Planner is driven to achieve
   continuous self-evolution, whereas the Executor is entirely frozen and
   deployed as a stable operational service. The Executor interacts with
   the external environment to gather execution feedback, which
   subsequently serves as the primary training signal to optimize the
   Planner.

   Multiple rollout plans and their corresponding trajectories are
   evaluated for correctness in the non-parametric memory extraction.
   Next, we calculate the reward
   [MATH: <semantics><msub><mi>R</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">R_{i}</annotation></semantics> :MATH]
   for each plan-trajectory pair according to Eq. (4). Then, we calculate
   the advantage
   [MATH: <semantics><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mi>i</mi></msub><annotation
   encoding="application/x-tex">\hat{A}_{i}</annotation></semantics>
   :MATH]
   for each rollout within the group as
   [MATH: <semantics><mrow><mrow><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mi>i</mi></msub><mo>=</mo><m
   frac><mrow><msub><mi>R</mi><mi>i</mi></msub><mo>−</mo><msub><mi>μ</mi><
   mi>R</mi></msub></mrow><mrow><msub><mi>σ</mi><mi>R</mi></msub><mo>+</mo
   ><mi>ϵ</mi></mrow></mfrac></mrow><mo>,</mo></mrow><annotation
   encoding="application/x-tex">\hat{A}_{i}=\frac{R_{i}-\mu_{R}}{\sigma_{R
   }+\epsilon},</annotation></semantics> :MATH]
   where
   [MATH: <semantics><msub><mi>μ</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">\mu_{R}</annotation></semantics> :MATH]
   and
   [MATH: <semantics><msub><mi>σ</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">\sigma_{R}</annotation></semantics> :MATH]
   are the mean and standard deviation of the reward set
   [MATH: <semantics><mrow><mi>𝐑</mi><mo>=</mo><mrow><mo
   stretchy="false">{</mo><msub><mi>R</mi><mn>1</mn></msub><mo>,</mo><mi
   mathvariant="normal">…</mi><mo>,</mo><msub><mi>R</mi><mi>G</mi></msub><
   mo stretchy="false">}</mo></mrow></mrow><annotation
   encoding="application/x-tex">\mathbf{R}=\{R_{1},\dots,R_{G}\}</annotati
   on></semantics> :MATH]
   , and
   [MATH: <semantics><mi>ϵ</mi><annotation
   encoding="application/x-tex">\epsilon</annotation></semantics> :MATH]
   is a small constant to prevent division by zero. Subsequently, the
   parameters of the Planner are updated by the objective function defined
   in Eq. (3.3.2), aiming to effectively reinforce successful reasoning
   strategies while penalizing flawed logic.

   Crucially, parameter updates and non-parametric memory extraction are
   performed simultaneously. By performing policy optimization and
   explicit memory storage simultaneously, MIA achieves a seamless online
   learning paradigm. This allows MIA to continuously internalize
   environmental feedback into its model parameters while enriching its
   external memory base, all without interrupting the ongoing exploration
   process. In conclusion, this online learning paradigm creates a
   positive feedback loop during exploration. As the agent’s reasoning
   capabilities progressively improve, it generates higher-quality
   reference samples, which in turn synchronously amplifies the agent’s
   reasoning proficiency at both the explicit contextual level and its
   internal parametric level.

   During exploration in TTL, we introduce a lightweight Meta Plan Memory
   strategy to conditionally select the optimal trajectory as the final
   output from
   [MATH: <semantics><mi>G</mi><annotation
   encoding="application/x-tex">G</annotation></semantics> :MATH]
   generated rollouts. If both successful and failed trajectories exist
   among the
   [MATH: <semantics><mi>G</mi><annotation
   encoding="application/x-tex">G</annotation></semantics> :MATH]
   rollouts, we store the shortest correct plan and one random incorrect
   plan as a contrastive pair. This provides explicit references to help
   MIA select the highest-quality reasoning. Additionally, after
   generating rollouts, a Router^1^11Router shares the same pre-trained
   LLM with the Memory Manager while distinct context prompts is prompted
   to reference examples in the Meta Plan Memory and select the
   highest-quality plan with its corresponding trajectory from the
   filtered candidates, which is then output as the final response.

3.4.3 Self-Evolution in Unsupervised Environments

   During Test-Time Learning (TTL), MIA strictly follows an online
   self-evolution pipeline of exploration
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\rightarrow</annotation></semantics>
   :MATH]
   environmental feedback acquisition
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\rightarrow</annotation></semantics>
   :MATH]
   non-parametric memory extraction
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\rightarrow</annotation></semantics>
   :MATH]
   parametric memory update, ensuring that each explored trajectory can be
   further transformed into both explicit non-parametric and implicit
   parametric memory. However, this process is effectively implemented
   only when strong supervision signals such as ground-truth answers are
   available. On the one hand, the ground truth enables the Memory Manager
   to assign positive or negative labels to extracted workflows. On the
   other hand, it provides reliable reward signals for training the
   Planner, making the optimization of parametric memory more stable and
   effective. However, such idealized supervision is often unavailable in
   open-world scenarios. For deep research agents, users typically do not
   always provide gold-standard answers or explicit feedback after each
   exploration, making it difficult to directly assess the quality of a
   reasoning trajectory based on answer correctness.
   Refer to caption Figure 6: A novel unsupervised evaluation framework
   that mimics the rigorous peer-review process of scientific venues.

   Traditional LLM-as-a-judge approaches often rely on a single prompt to
   evaluate complex trajectories, which frequently suffer from
   "hallucinated objectivity", where the judge overlooks subtle logical
   fallacies or focuses on stylistic fluency rather than factual
   correctness. To bridge this gap, we propose a novel evaluation
   framework that mimics the rigorous peer-review process of scientific
   venues. Our framework is inspired by the Reviewer-Area Chair (AC)
   decision-making process, as shown in Figure 6. The core idea is to
   decompose the monolithic "judgment" task into specialized, orthogonal
   dimensions, ensuring that the final judgment is not merely a scalar
   score but a synthesis of multi-perspective evidence. This mechanism
   offers three distinct advantages for unsupervised scenarios.
   Dimensional Orthogonality: By isolating Logic, Format, and Factuality,
   we prevent "error bleeding," e.g., a formatting mistake might unfairly
   bias a judge’s perception of logical soundness. Evidence-Based
   Accountability: Each reviewer is required to provide "evidence quotes"
   or "atomic requirements," transforming the evaluation from a black-box
   rating into a verifiable audit trail. Conflict Resolution via
   Meta-Decision: Similar to an academic conference, the AC does not
   simply average the scores but identifies fatal flaws, prioritizing the
   most critical failure modes (e.g., factual hallucinations) over minor
   imperfections. Our motivation is that, for a reasoning trajectory with
   rigorous logic, credible evidence sources, minimal hallucination, and
   proper compliance with task requirements, the reasoning process itself
   can still be regarded as high-quality. Therefore, we treat such process
   as an approximate supervision signal to support both non-parametric
   memory selection and parametric memory updating, enabling MIA to
   maintain continuous self-evolution ability even in unsupervised
   open-world environments.

   In implementation, we utilize a Qwen3-32B model to instantiate three
   specialized reviewers and one AC. Each is governed by a distinct,
   structured prompt designed to minimize heuristic bias (the prompts are
   shown in Appendix 13). Reviewer of Reasoning & Logical Consistency (
   [MATH: <semantics><msub><mi>R</mi><mi>L</mi></msub><annotation
   encoding="application/x-tex">R_{L}</annotation></semantics> :MATH]
   ) focuses on the "reachability" of the conclusion. It evaluates the
   causal chain from premises to results, flagging wrong reasoning or
   unstated assumptions. Reviewer of Information Sourcing & Credibility (
   [MATH: <semantics><msub><mi>R</mi><mi>C</mi></msub><annotation
   encoding="application/x-tex">R_{C}</annotation></semantics> :MATH]
   ) acts as a constraint-checker. It scrutinizes the misunderstandings of
   the retrieved information and factual hallucinations, marking uncertain
   claims for AC judgment. Reviewer of Result Validity (
   [MATH: <semantics><msub><mi>R</mi><mi>V</mi></msub><annotation
   encoding="application/x-tex">R_{V}</annotation></semantics> :MATH]
   ) objectively evaluates the completeness of the multimodal deep
   research agent’s final response and the actual completion status of the
   task. Area Chair Agent performs a meta-analysis of the structured JSON
   outputs from the three reviewers.

4 Experiments

4.1 Experimental Setup

   Training Settings: We build our training framework based on veRL (Sheng
   et al., 2025). We initialize the Executor with Qwen2.5-VL-7B (Bai et
   al., 2025) and the Planner with Qwen3-8B (Yang et al., 2025). The
   Executor is trained using FVQA-train (Wang et al., 2017) to learn tool
   calling and reasoning. For the Planner, we use a mixture of FVQA-train
   (with images discarded) and MATPO (Mo et al., 2025) to enhance its
   planning and reflection capabilities based on memory understanding.
   During the two-stage GRPO training, a Qwen3-32B serves as the LLM
   Judger to provide correctness reward signals. For external tools, we
   employ the local wiki25 (Karpukhin et al., 2020) for text-to-text
   search and a local image cache built by Serper for image-to-image
   search. More details are provided in Appendix 7.

   Test Settings: To comprehensively evaluate the performance of MIA, we
   conduct experiments on both multimodal and text-only benchmarks. For
   multimodal tasks, we evaluate our model on FVQA-test (Wang et al.,
   2017), InfoSeek (Chen et al., 2023), MMSearch (Jiang et al., 2024),
   SimpleVQA (Cheng et al., 2025), LiveVQA (Fu et al., 2025), and two
   In-house datasets (In-house 1 and In-house 2). For text-only tasks, we
   evaluate our model on HotpotQA (Yang et al., 2018), 2WikiMultiHopQA (Ho
   et al., 2020), SimpleQA (Wei et al., 2024), and the text-only subset of
   GAIA (Mialon et al., 2023). For image-to-image search, we utilize
   Serper across all multimodal datasets. For text-to-text search, we use
   wiki25 for HotpotQA, 2WikiMultiHopQA, and SimpleQA, while Serper is
   applied for all other datasets. These datasets are carefully chosen to
   assess the model’s capabilities in handling complex multi-hop
   reasoning, open-domain searching, and visual question answering (VQA)
   in diverse scenarios. More details are provided in Appendix 8. Detailed
   information about the benchmark datasets can be found in Appendix 11.

   Baselines: We evaluate against both closed-source models (GPT-4o (Hurst
   et al., 2024), GPT-5.4 (Singh et al., 2025), Gemini-2.5-Pro (Comanici
   et al., 2025), and Gemini-3-Flash (Google DeepMind, 2026)) and
   open-source models from the Qwen2.5-VL series. All models are tasked
   with solving problems in three different workflows: (1) Direct Answer:
   Models are prompted to generate short and precise answers directly
   without accessing external information. (2) Search Agent: In this
   workflow, models perform multi-turn tool calling under the ReAct (Yao
   et al., 2023) paradigm. Specifically, Qwen2.5-VL-7B+ReACT,
   Qwen2.5-VL-32B+ReACT, and MMSearch-R1 (Wu et al., 2025) are evaluated
   using our tool environment, while the results for DeepMMSearch-R1
   (Narayan et al., 2025), WebWatcher (Geng et al., 2025), and Deepeyes2
   (Zheng et al., 2026) are directly cited from their respective technical
   reports. The base models for MMSearch-R1, DeepMMSearch-R1, WebWatcher,
   and Deepeyes2 all adopt Qwen2.5-VL-7B. (3) Memory-based Search Agent:
   To ensure a fair comparison, the Executors for all memory-based models
   share the exact same training settings. The Executor is trained under
   three modes: no extra prompt, workflow memory prompt, and plan prompt.
   The No Memory baseline utilizes the no extra prompt mode, which is
   trained with the search tools we provided based on the MMSearch-R1
   codebase. Contextual memory methods, including RAG (Lewis et al.,
   2020), Mem0 (Chhikara et al., 2025), and A-Mem (Xu et al., 2025),
   employ the workflow memory prompt. Methods that abstract memory into
   high-level guidance, such as ReasoningBank (Ouyang et al., 2025), ExpeL
   (Zhao et al., 2024), Memento (Zhou et al., 2025), and our MIA, utilize
   the plan prompt. More details about baseline methods are provided in
   Appendix 9.

   Metric: We employ the Qwen3-32B model as an LLM Judger to determine
   whether the models’ final outputs are correct. The specific prompt used
   for the LLM Judger can be found in Appendix 13.
   Table 3: Overall evaluation results on multimodal datasets for Deep
   Research Agent. Bold denotes the highest score in each column.
   Underline indicates the second-highest score in each column.
   Model In-Domain Out-of-Domain
   FVQA-test InfoSeek SimpleVQA LiveVQA MMSearch In-house 1 In-house 2
   Direct Answer
   GPT-5.4 50.8 43.6 55.5 21.5 44.4 45.1 23.0
   Gemini-3-Flash 69.3 69.0 73.7 26.0 69.0 52.5 25.5
   GPT-4o 41.7 42.7 46.6 26.9 22.2 25.6 17.2
   Gemini-2.5-Pro 37.2 37.0 53.4 27.7 26.9 30.8 19.6
   Qwen2.5-VL-7B 20.9 23.9 30.4 8.3 7.2 9.5 5.0
   Qwen2.5-VL-32B 24.7 25.8 40.1 18.7 15.7 18.6 6.7
   Search Agent
   Qwen2.5-VL-7B+ReACT 34.2 28.3 35.8 10.7 21.1 9.5 17.8
   Qwen2.5-VL-32B+ReACT 51.3 38.0 48.5 24.8 27.3 28.8 26.5
   MMSearch-R1 58.0 49.0 55.3 28.3 43.9 13.6 21.8
   DeepMMSearch-R1 - 47.5 55.9 - - - -
   WebWatcher - - 54.3 - 55.3 - -
   Deepeyes2 60.6 51.1 59.4 - 63.7 - -
   Memory-based Search Agent
   No Memory 61.4 56.8 63.0 33.0 55.6 15.9 26.9
   RAG 60.5 55.9 60.5 31.7 54.4 12.5 25.5
   Mem0 55.6 48.2 56.7 24.5 43.3 12.5 23.2
   A-Mem 38.5 36.0 51.6 22.6 40.9 12.5 24.2
   ReasoningBank 64.7 59.5 60.4 34.2 57.3 18.6 29.3
   ExpeL 64.2 58.6 62.5 34.1 61.4 19.7 28.3
   Memento 66.3 57.3 61.9 36.7 61.4 22.7 30.7
   Unsupervised MIA(Ours) 65.1 64.3 63.3 40.1 60.2 29.8 31.1
   MIA(Ours) 69.6 65.5 64.9 43.1 62.6 31.8 37.7
   Table 4: Overall evaluation results on text-only datasets for Deep
   Research Agent. Bold denotes the highest score in each column.
   Underline indicates the second-highest score in each column.
     Model                    Out-of-Domain
                              SimpleQA   2Wiki   HotpotQA   GAIA
     No Memory                40.7       61.2    51.0       11.7
     RAG                      38.3       56.3    47.5       14.6
     Mem0                     38.1       54.9    49.0       16.5
     A-Mem                    38.8       56.2    47.5       12.6
     ReasoningBank            42.4       61.0    52.7       14.6
     ExpeL                    43.0       63.4    55.5       20.4
     Memento                  42.4       64.2    55.2       22.3
     Unsupervised MIA(Ours)   46.6       71.6    61.7       30.1
     MIA(Ours)                47.7       71.8    63.5       31.1

4.2 Main Result

   As shown in Table 3, we find that our proposed MIA achieves the highest
   overall performance among open-source models, reaching an average
   accuracy of 53.6. Compared to the previous best memory-based method,
   MIA improves the average accuracy by 5.5, including specific increases
   of 3.3 on FVQA-test, 6.4 on the multi-hop task LiveVQA, and an
   impressive 9.1 on the highly challenging custom task In-house 1.
   Additionally, we observe a critical phenomenon: traditional contextual
   memory methods (e.g., RAG, Mem0, and A-Mem) generally underperform the
   "No Memory" baseline. This validates that long memory contexts
   introduce noise, leading to performance degradation. Although recent
   advanced memory methods (e.g., ReasoningBank, ExpeL, and Memento)
   abstract memory into high-level guidance to mitigate this issue, they
   still struggle to fully internalize historical experiences. Notably,
   MIA effectively bridges this gap through its dual-memory mechanism and
   online parameter updating, achieving an optimal balance and the highest
   accuracy among all memory-based approaches.

   Furthermore, MIA significantly outperforms most closed-source general
   models (GPT-4o, Gemini-2.5-Pro, and GPT-5.4), achieving performance
   close to that of Gemini-3-Flash. It is noteworthy that MIA, with its 7B
   Executor, has approached or even surpassed giant closed-source LLMs,
   which highlights its excellent performance. Even when compared to
   state-of-the-art specialized search agents like Deepeyes2, MIA
   maintains highly competitive and superior performance. Remarkably, MIA
   is equipped with a simple toolset consisting exclusively of basic text
   and image search tools, yet it surpasses more complex agentic systems.
   This compellingly demonstrates that MIA’s superior performance stems
   directly from its exceptional ability to leverage memory and
   internalize historical experiences, rather than relying on
   sophisticated external tools.

   To validate MIA’s stability and scalability in text-only deep research
   scenarios, we conduct evaluations on the SimpleQA, 2Wiki, HotpotQA, and
   GAIA datasets. As shown in Table 4, MIA consistently outperforms the
   best alternative methods across all text-only datasets, achieving an
   impressive average accuracy of 53.5. Specifically, compared to the
   strongest baseline Memento, MIA improves the average accuracy by 7.5,
   with notable gains of 7.6 on 2Wiki and 8.8 on the highly challenging
   GAIA benchmark. This demonstrates that MIA’s Manager-Planner-Executor
   architecture and continuous evolution mechanism are modality-agnostic,
   sustaining exceptional performance in complex text-only multi-hop
   reasoning tasks.

4.3 Training Analysis

   Refer to caption Figure 7: Left: Reward curves in each batch of Planner
   and Executor during the training stage. Middle: Response length in each
   batch of Planner and Executor during the training stage. Right:
   Response length in each batch of Planner during the TTL stage.

   In Figure 7, we present the reward function curves of the Planner and
   the Executor during the training stage. As the number of training steps
   increases, the rewards of both the Planner and the Executor show an
   overall upward trend, although they exhibit distinct patterns. Because
   the reward function can provide relatively direct and stable feedback
   based on the action of the Executor, the reward curve of the Executor
   shows a clear increase as training progresses. In contrast, the
   Planner’s actions are indirect through the results produced by the
   Executor. Consequently, the feedback provided by the reward function is
   also indirect and unstable, which can reduce the quality of the
   feedback. As a result, the reward curve of the Planner increases more
   slowly as training grows.

   A similar phenomenon can also be observed in the response length. The
   response length of the Planner converges more slowly, indicating that
   its reward signals are relatively unstable and exhibit larger
   fluctuations. In comparison, the response length of the Executor
   converges more quickly, suggesting that its reward signals are
   relatively stable and fluctuate less. Additionally, in the TTL stage,
   as the training steps increase on the 2Wiki dataset, the response
   length gradually shifts toward the pattern of the 2Wiki dataset,
   becoming progressively shorter. In contrast, with increasing training
   steps on the LiveVQA dataset, the response length shows a tendency to
   shift toward the pattern of the LiveVQA dataset, which is characterized
   by progressively longer responses. These experimental results
   demonstrate that the introduction of reinforcement learning enables MIA
   to effectively capture the characteristics of different datasets,
   thereby improving its reasoning capabilities.

4.4 Generalization to Closed-Source Executors

   To evaluate the generalizability of MIA, we replace the open-source
   Executor with the most powerful closed-source models (GPT-5.4 (Singh et
   al., 2025), Gemini-3-Flash (Google DeepMind, 2026), and
   Claude-Sonnet-4.6 (Anthropic, 2025) while removing TTL. As shown in
   Figure 8, MIA achieves consistent improvements across all three models
   on both LiveVQA (multimodal) and HotpotQA (text-only) benchmarks.
   Furthermore, the improvement margin is inversely correlated with the
   base capability of the Executor: GPT-5.4 benefits the most (
   [MATH: <semantics><mrow><mo>+</mo><mn>8.9</mn></mrow><annotation
   encoding="application/x-tex">+8.9</annotation></semantics> :MATH]
   on LiveVQA,
   [MATH: <semantics><mrow><mo>+</mo><mn>6.4</mn></mrow><annotation
   encoding="application/x-tex">+6.4</annotation></semantics> :MATH]
   on HotpotQA), followed by Gemini-3-Flash (
   [MATH: <semantics><mrow><mo>+</mo><mn>3.1</mn></mrow><annotation
   encoding="application/x-tex">+3.1</annotation></semantics> :MATH]
   on LiveVQA,
   [MATH: <semantics><mrow><mo>+</mo><mn>2.6</mn></mrow><annotation
   encoding="application/x-tex">+2.6</annotation></semantics> :MATH]
   on HotpotQA) and Claude-Sonnet-4-6 (
   [MATH: <semantics><mrow><mo>+</mo><mn>1.8</mn></mrow><annotation
   encoding="application/x-tex">+1.8</annotation></semantics> :MATH]
   on LiveVQA,
   [MATH: <semantics><mrow><mo>+</mo><mn>1.7</mn></mrow><annotation
   encoding="application/x-tex">+1.7</annotation></semantics> :MATH]
   on HotpotQA).
   Refer to caption Figure 8: Comparisons between SOTA LLMs with MIA (the
   green area: MIA) and without MIA (the blue area: ReAct).

   These results demonstrate that MIA possesses exceptional
   generalization. The method consistently enhances performance across
   both open-source and closed-source models of varying scales.
   Additionally, our approach achieves state-of-the-art gains. It notably
   yields significant improvements on GPT-5.4 and delivers higher
   improvements on other SOTA LLMs, including Gemini-3-Flash and
   Claude-Sonnet-4.6.

4.5 Tool Call Analysis

   Refer to caption Figure 9: Tool call distribution analysis. Each dot
   represents an individual task execution (gray indicates failures;
   colored indicates successful runs). The scatter and half-violin plots
   illustrate the frequency of tool calls among successful executions.

   Figure 9 presents the distribution of tool calls across tasks sampled
   from TTL, where colored points denote successful executions. From the
   figure, we can draw the following conclusions: (1) Memory is essential:
   Models lacking a memory mechanism and exhibiting very low tool usage
   (e.g., No-Memory) achieve the poorest accuracy. This is because models
   are used to conduct reasoning within limited tool calls. Without
   memory, they cannot effectively recall previous tool interactions
   during multi-turn reasoning processes, leading to the worst
   performance. (2) Planning for the current query is more effective than
   relying solely on historical experiences: Methods based on long-context
   memory (e.g., RAG, Mem0 and A-Mem) or meta-guidance memory (e.g.,
   ReasoningBank and Expel) show weaker performance compared to approaches
   such as Memento and MIA, which incorporate an explicit planner on top
   of meta-guidance memory. (3) Combining heterogeneous memory with
   continual learning during test time yields the best results: By
   integrating multiple memory components with test-time learning, MIA
   achieves the strongest performance among all memory-based systems.

4.6 Ablation Study

   Table 5: Ablation study results on multimodal datasets. Bold denotes
   the highest score in each column.
   Model In-Domain Out-of-Domain
   FVQA-test InfoSeek SimpleVQA LiveVQA MMSearch In-house 1 In-house 2
   Base 61.4 56.8 63.0 33.0 55.6 15.9 26.9
   Only Memory 62.8 56.8 61.2 37.8 56.1 12.2 28.5
   Only Plan 64.9 58.6 62.6 35.4 56.7 21.0 31.3
   Memory for Planner 67.9 60.7 61.8 36.0 59.0 17.0 34.7
   + Reflect 66.2 60.1 63.0 37.9 58.5 23.1 31.3
   Trained Planner 67.6 63.8 63.8 40.1 60.8 26.1 34.5
   + TTL (Ours) 69.6 65.5 64.9 43.1 62.6 31.8 37.7
   Table 6: Ablation study results on text-only datasets. Bold denotes the
   highest score in each column.
     Model                Out-of-Domain
                          SimpleQA   2Wiki   HotpotQA   GAIA
     Base                 40.7       61.2    51.0       11.7
     Only Memory          37.7       61.3    50.3       12.6
     Only Plan            42.1       62.8    54.9       18.5
     Memory for Planner   42.4       64.6    54.8       19.4
     + Reflect            43.9       66.6    57.6       26.2
     Trained Planner      44.6       69.1    59.3       28.2
     + TTL (Ours)         47.7       71.8    63.5       31.1

   To evaluate the contribution of each component in the MIA framework, we
   start from the fundamental baseline (Base) with incrementally adding
   components, and compare the overall performance. The results are shown
   in Table 5 and Table 6. The experimental results demonstrate that each
   proposed module is effective in enhancing the reasoning accuracy of the
   agent across both modalities.

   To validate the superiority of the Manager-Planner-Executor
   architecture, we first compare the Base with the Only Memory and Only
   Plan settings. We observe that simply introducing non-parametric memory
   (Only Memory) leads to a performance drop in the average accuracy of
   multimodal tasks (-0.4). However, when we integrate memory specifically
   to guide the planning process (Memory for Planner), the performance
   significantly improves. Compared to the Base, this architecture
   increases the average accuracy by 3.5 (multimodal) and 4.15
   (text-only). This validates the effectiveness of using memory as a
   contextual prior for the Planner rather than directly feeding it to the
   Executor.

   In addition, we retain the Memory for Planner architecture and
   introduce the reflection mechanism (+ Reflect) to validate its
   effectiveness. The results show that the integration of reflection
   yields positive gains on complex multi-hop reasoning, increasing the
   average accuracy by 0.43 (multimodal) and 3.28 (text-only). Notably,
   while all the aforementioned configurations rely on the Qwen3-32B as
   the Planner, our Trained Planner achieves substantial performance gains
   using a much smaller Qwen3-8B model through the alternating RL
   training. Specifically, we observe that the introduction of the
   alternating RL training process (Trained Planner) further boosts the
   overall performance, increasing the average accuracy by 2.37
   (multimodal) and 1.72 (text-only). Finally, we introduce the online TTL
   mechanism. This dynamic evolution process provides a substantial final
   push, further increasing the average accuracy by 3.23 (multimodal) and
   2.64 (text-only).

   In summary, compared with the initial baseline, our MIA framework
   significantly increases the overall average accuracy by 8.94 on
   multimodal benchmarks and 12.38 on text-only benchmarks. By
   incrementally integrating these components, MIA achieves significant
   performance improvements.

4.7 Unsupervised Self-Evolution

   As shown in Table 3, the unsupervised MIA achieves a comparable
   performance to supervised baselines on multimodal benchmarks. In Table
   4, the unsupervised MIA even surpasses almost all supervised baselines
   on text-only benchmarks and is only inferior to the supervised MIA.
   These results demonstrate our unsupervised evaluation framework is
   effective and MIA retains strong generalization ability even in the
   absence of explicit supervision signals. Furthermore, we conduct
   self-evolution experiments under the unsupervised setting, as shown in
   Table 7. By progressively introducing Plan and Reflect, Unsupervised
   Memory, and Test-Time Learning, we find that relying solely on
   unsupervised non-parametric memory leads to unstable performance,
   whereas incorporating TTL on it yields substantial improvements. We
   further examine the effect of continual evolution across multiple
   epochs during TTL. The results show that, in the unsupervised setting,
   when the model encounters the same dataset for the second and third
   time, its performance improves steadily (e.g., 59.6
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\rightarrow</annotation></semantics>
   :MATH]
   61.1
   [MATH: <semantics><mo stretchy="false">→</mo><annotation
   encoding="application/x-tex">\rightarrow</annotation></semantics>
   :MATH]
   61.7). This indicates that, through continual exploration, MIA is able
   to accumulate useful experience and gradually solve problems that it
   previously failed to answer.
   Table 7: MIA’s self-evolution results in an unsupervised setting. The
   Planner consistently uses Qwen3-8B.
     Model                             Multimodal            Text-only
                                       FVQA-test   LiveVQA   2Wiki   HotpotQA
     Base                              61.4        33.0      61.2    51.0
     Plan and Reflect (no memory)      59.6        36.5      64.2    56.4
     Unsupervised Memory for Planner   57.6        28.5      66.9    56.4
     Unsupervised MIA (epoch-1)        65.1        40.1      71.6    61.7
     Unsupervised MIA (epoch-2)        66.4        41.4      73.4    63.1
     Unsupervised MIA (epoch-3)        67.1        41.8      74.7    63.2

5 Conclusion

   In this paper, we propose MIA, a memory framework to enhance the
   reasoning performance and self-evolution ability of Deep Research
   Agents. Based on the Executor agent, we design a novel
   Manager-Planner-Executor architecture. By compressing bloated
   historical trajectories into structured workflows via the Manager
   agent, MIA effectively mitigates the noise interference in long-context
   memory and improves the precision and quality of memory retrieval. By
   introducing the Planner agent, we transform the non-parametric memory
   into parametric memory, which reduces the storage burden and improves
   the planning performance. Furthermore, to bridge the gap between the
   Planner and Executor agents, we introduce a two-stage alternating RL
   paradigm. This training strategy not only improves the Planner’s
   ability to generate precise plans and conduct autonomous reflection,
   but also significantly enhances the plan understanding and following
   capabilities of the Executor. Additionally, we propose an online
   test-time learning mechanism, enabling the Planner to absorb historical
   experiences during the exploration process. At the contextual level, it
   extracts high-quality positive and negative paradigms as non-parametric
   memory for explicit in-context contrastive learning. At the parametric
   level, MIA synchronously updates the Planner to capture latent
   knowledge representations and internalize planning ability. Extensive
   experiments demonstrate that MIA achieves state-of-the-art performance
   on both multimodal and text-only deep research benchmarks. Currently,
   our framework primarily focuses on deep research tasks. In the future,
   we plan to extend MIA to more complex and dynamic environments.

6 Contribution

   Jingyang Qiao proposed the core methodology, designed the experimental
   protocols, and took the lead in writing and revising the manuscript.
   Weicheng Meng, as a co-first author, implemented the algorithms,
   executed the experiments, and contributed to the manuscript writing. Yu
   Cheng and Zhihang Lin implemented trustworthy and efficiency versions
   of MIA OpenClaw skills, respectively. Zhizhong Zhang, as the
   corresponding author, supervised the research and provided critical
   revisions to the manuscript. Xin Tan, Jingyu Gong and Kun Shao proposed
   insightful suggestions and advice for the methodology. Yuan Xie, as the
   project leader, provided overall direction and strategic guidance for
   the research project.

References

     * Anthropic (2025) Anthropic. System card: Claude opus 4 & claude
       sonnet 4.
       https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2f
       f47.pdf, May 2025. System card, accessed 2026-03-28.
     * Bai et al. (2025) Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang,
       Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang,
       Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan,
       Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo Ye, Xi Zhang,
       Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and
       Junyang Lin. Qwen2.5-vl technical report, 2025.
       https://arxiv.org/abs/2502.13923.
     * Cao et al. (2025) Zouying Cao, Jiaji Deng, Li Yu, Weikang Zhou,
       Zhaoyang Liu, Bolin Ding, and Hai Zhao. Remember me, refine me: A
       dynamic procedural memory framework for experience-driven agent
       evolution. arXiv preprint arXiv:2512.10696, 2025.
     * Chen et al. (2023) Yang Chen, Hexiang Hu, Yi Luan, Haitian Sun,
       Soravit Changpinyo, Alan Ritter, and Ming-Wei Chang. Can
       pre-trained vision and language models answer visual
       information-seeking questions? In Proceedings of the 2023
       Conference on Empirical Methods in Natural Language Processing,
       pages 14948–14968, 2023.
     * Cheng et al. (2025) Xianfu Cheng, Wei Zhang, Shiwei Zhang, Jian
       Yang, Xiangyuan Guan, Xianjie Wu, Xiang Li, Ge Zhang, Jiaheng Liu,
       Yuying Mai, et al. Simplevqa: Multimodal factuality evaluation for
       multimodal large language models. In Proceedings of the IEEE/CVF
       International Conference on Computer Vision, pages 4637–4646, 2025.
     * Chhikara et al. (2025) Prateek Chhikara, Dev Khant, Saket Aryan,
       Taranjeet Singh, and Deshraj Yadav. Mem0: Building production-ready
       ai agents with scalable long-term memory. arXiv preprint
       arXiv:2504.19413, 2025.
     * Comanici et al. (2025) Gheorghe Comanici, Eric Bieber, Mike
       Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon,
       Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5:
       Pushing the frontier with advanced reasoning, multimodality, long
       context, and next generation agentic capabilities. arXiv preprint
       arXiv:2507.06261, 2025.
     * Devlin et al. (2019) Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
       Kristina Toutanova. Bert: Pre-training of deep bidirectional
       transformers for language understanding. In Proceedings of the 2019
       conference of the North American chapter of the association for
       computational linguistics: human language technologies, volume 1
       (long and short papers), pages 4171–4186, 2019.
     * Douze et al. (2025) Matthijs Douze, Alexandr Guzhva, Chengqi Deng,
       Jeff Johnson, Gergely Szilvasy, Pierre-Emmanuel Mazaré, Maria
       Lomeli, Lucas Hosseini, and Hervé Jégou. The faiss library. IEEE
       Transactions on Big Data, 2025.
     * Du et al. (2025) Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang,
       and Zhendong Mao. Deepresearch bench: A comprehensive benchmark for
       deep research agents. arXiv preprint arXiv:2506.11763, 2025.
     * Fang et al. (2025) Runnan Fang, Yuan Liang, Xiaobin Wang, Jialong
       Wu, Shuofei Qiao, Pengjun Xie, Fei Huang, Huajun Chen, and Ningyu
       Zhang. Memp: Exploring agent procedural memory. arXiv preprint
       arXiv:2508.06433, 2025.
     * Fu et al. (2025) Mingyang Fu, Yuyang Peng, Benlin Liu, Yao Wan, and
       Dongping Chen. Livevqa: Live visual knowledge seeking. arXiv
       e-prints, pages arXiv–2504, 2025.
     * Gandon et al. (2002) Fabien Gandon, Agostino Poggi, Giovanni
       Rimassa, and Paola Turci. Multi-agent corporate memory management
       system. Applied Artificial Intelligence, 16(9-10):699–720, 2002.
     * Geng et al. (2025) Xinyu Geng, Peng Xia, Zhen Zhang, Xinyu Wang,
       Qiuchen Wang, Ruixue Ding, Chenxi Wang, Jialong Wu, Yida Zhao, Kuan
       Li, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou.
       Webwatcher: Breaking new frontier of vision-language deep research
       agent, 2025. https://arxiv.org/abs/2508.05748.
     * Google DeepMind (2026) Google DeepMind. Gemini 3.
       https://deepmind.google/models/gemini/, 2026. Official model family
       page, accessed 2026-03-28.
     * Ho et al. (2020) Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and
       Akiko Aizawa. Constructing a multi-hop qa dataset for comprehensive
       evaluation of reasoning steps. In Proceedings of the 28th
       International Conference on Computational Linguistics, pages
       6609–6625, 2020.
     * Hu et al. (2025) Mengkang Hu, Tianxing Chen, Qiguang Chen, Yao Mu,
       Wenqi Shao, and Ping Luo. Hiagent: Hierarchical working memory
       management for solving long-horizon agent tasks with large language
       model. In Proceedings of the 63rd Annual Meeting of the Association
       for Computational Linguistics (Volume 1: Long Papers), pages
       32779–32798, 2025.
     * Huang et al. (2023) Qian Huang, Jian Vora, Percy Liang, and Jure
       Leskovec. Benchmarking large language models as ai research agents.
       In NeurIPS 2023 foundation models for decision making workshop,
       2023.
     * Huang et al. (2025) Yuxuan Huang, Yihang Chen, Haozheng Zhang, Kang
       Li, Huichi Zhou, Meng Fang, Linyi Yang, Xiaoguang Li, Lifeng Shang,
       Songcen Xu, et al. Deep research agents: A systematic examination
       and roadmap. arXiv preprint arXiv:2506.18096, 2025.
     * Hurst et al. (2024) Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
       Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda,
       Alan Hayes, Alec Radford, et al. Gpt-4o system card. arXiv preprint
       arXiv:2410.21276, 2024.
     * Jiang et al. (2024) Dongzhi Jiang, Renrui Zhang, Ziyu Guo, Yanmin
       Wu, Jiayi Lei, Pengshuo Qiu, Pan Lu, Zehui Chen, Chaoyou Fu,
       Guanglu Song, Peng Gao, Yu Liu, Chunyuan Li, and Hongsheng Li.
       Mmsearch: Benchmarking the potential of large models as multi-modal
       search engines, 2024. https://arxiv.org/abs/2409.12959.
     * Jin et al. (2025) Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon,
       Sercan Arik, Dong Wang, Hamed Zamani, and Jiawei Han. Search-r1:
       Training llms to reason and leverage search engines with
       reinforcement learning. Second Conference on Language Modeling,
       2025.
     * Kang et al. (2025) Jikun Kang, Wenqi Wu, Filippos Christianos, Alex
       James Chan, Fraser David Greenlee, George Thomas, Marvin Purtorab,
       and Andrew Toulis. Lm2: Large memory models for long context
       reasoning. In Workshop on Reasoning and Planning for Large Language
       Models, 2025.
     * Karpukhin et al. (2020) Vladimir Karpukhin, Barlas Oguz, Sewon Min,
       Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau
       Yih. Dense passage retrieval for open-domain question answering. In
       Proceedings of the 2020 conference on empirical methods in natural
       language processing (EMNLP), pages 6769–6781, 2020.
     * Lerman and Galstyan (2003) Kristina Lerman and Aram Galstyan. Agent
       memory and adaptation in multi-agent systems. In Proceedings of the
       second international joint conference on Autonomous agents and
       multiagent systems, pages 797–803, 2003.
     * Lewis et al. (2020) Patrick Lewis, Ethan Perez, Aleksandra Piktus,
       Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler,
       Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al.
       Retrieval-augmented generation for knowledge-intensive nlp tasks.
       Advances in neural information processing systems, 33:9459–9474,
       2020.
     * Li et al. (2023) Minghao Li, Yingxiu Zhao, Bowen Yu, Feifan Song,
       Hangyu Li, Haiyang Yu, Zhoujun Li, Fei Huang, and Yongbin Li.
       Api-bank: A comprehensive benchmark for tool-augmented llms. In
       Proceedings of the 2023 conference on empirical methods in natural
       language processing, pages 3102–3116, 2023.
     * Li et al. (2024a) Tianle Li, Ge Zhang, Quy Duc Do, Xiang Yue, and
       Wenhu Chen. Long-context llms struggle with long in-context
       learning. arXiv preprint arXiv:2404.02060, 2024a.
     * Li et al. (2025) Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin
       Qian, Yongkang Wu, Ji-Rong Wen, Yutao Zhu, and Zhicheng Dou.
       Webthinker: Empowering large reasoning models with deep research
       capability. The Thirty-ninth Annual Conference on Neural
       Information Processing Systems, 2025.
     * Li et al. (2024b) Xinyi Li, Sai Wang, Siqi Zeng, Yu Wu, and Yi
       Yang. A survey on llm-based multi-agent systems: workflow,
       infrastructure, and challenges. Vicinagearth, 1(1):9, 2024b.
     * Ma et al. (2024) Yubo Ma, Zhibin Gou, Junheng Hao, Ruochen Xu,
       Shuohang Wang, Liangming Pan, Yujiu Yang, Yixin Cao, and Aixin Sun.
       Sciagent: Tool-augmented language models for scientific reasoning.
       In Proceedings of the 2024 conference on empirical methods in
       natural language processing, pages 15701–15736, 2024.
     * Mialon et al. (2023) Grégoire Mialon, Clémentine Fourrier, Craig
       Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. Gaia: a
       benchmark for general ai assistants, 2023.
     * Mo et al. (2025) Zhanfeng Mo, Xingxuan Li, Yuntao Chen, and Lidong
       Bing. Multi-agent tool-integrated policy optimization, 2025.
       https://arxiv.org/abs/2510.04678.
     * Narayan et al. (2025) Kartik Narayan, Yang Xu, Tian Cao, Kavya
       Nerella, Vishal M. Patel, Navid Shiee, Peter Grasch, Chao Jia,
       Yinfei Yang, and Zhe Gan. Deepmmsearch-r1: Empowering multimodal
       llms in multimodal web search, 2025.
       https://arxiv.org/abs/2510.12801.
     * Ouyang et al. (2025) Siru Ouyang, Jun Yan, I Hsu, Yanfei Chen, Ke
       Jiang, Zifeng Wang, Rujun Han, Long T Le, Samira Daruki, Xiangru
       Tang, et al. Reasoningbank: Scaling agent self-evolving with
       reasoning memory. arXiv preprint arXiv:2509.25140, 2025.
     * Parisi et al. (2022) Aaron Parisi, Yao Zhao, and Noah Fiedel. Talm:
       Tool augmented language models. arXiv preprint arXiv:2205.12255,
       2022.
     * Rasmussen et al. (2025) Preston Rasmussen, Pavlo Paliychuk, Travis
       Beauvais, Jack Ryan, and Daniel Chalef. Zep: a temporal knowledge
       graph architecture for agent memory. arXiv preprint
       arXiv:2501.13956, 2025.
     * Schmidgall et al. (2025) Samuel Schmidgall, Yusheng Su, Ze Wang,
       Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor,
       Zicheng Liu, and Emad Barsoum. Agent laboratory: Using llm agents
       as research assistants. Findings of the Association for
       Computational Linguistics: EMNLP 2025, pages 5977–6043, 2025.
     * Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
       Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y.
       Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical
       reasoning in open language models, 2024.
       https://arxiv.org/abs/2402.03300.
     * Sheng et al. (2025) Guangming Sheng, Chi Zhang, Zilingfeng Ye,
       Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan
       Wu. Hybridflow: A flexible and efficient rlhf framework. In
       Proceedings of the Twentieth European Conference on Computer
       Systems, pages 1279–1297, 2025.
     * Shi et al. (2025) Yaorui Shi, Yuxin Chen, Siyuan Wang, Sihang Li,
       Hengxing Cai, Qi Gu, Xiang Wang, and An Zhang. Look back to reason
       forward: Revisitable memory for long-context llm agents. arXiv
       preprint arXiv:2509.23040, 2025.
     * Singh et al. (2025) Aaditya Singh, Adam Fry, Adam Perelman, Adam
       Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ
       Ostrow, Akhila Ananthram, et al. Openai gpt-5 system card. arXiv
       preprint arXiv:2601.03267, 2025.
     * Wang et al. (2022) Liang Wang, Nan Yang, Xiaolong Huang, Binxing
       Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder, and Furu Wei. Text
       embeddings by weakly-supervised contrastive pre-training. arXiv
       preprint arXiv:2212.03533, 2022.
     * Wang et al. (2017) Peng Wang, Qi Wu, Chunhua Shen, Anthony Dick,
       and Anton Van Den Hengel. Fvqa: Fact-based visual question
       answering. IEEE transactions on pattern analysis and machine
       intelligence, 40(10):2413–2427, 2017.
     * Wang et al. (2023) Weizhi Wang, Li Dong, Hao Cheng, Xiaodong Liu,
       Xifeng Yan, Jianfeng Gao, and Furu Wei. Augmenting language models
       with long-term memory. Advances in Neural Information Processing
       Systems, 36:74530–74543, 2023.
     * Wang and Chen (2025) Yu Wang and Xi Chen. Mirix: Multi-agent memory
       system for llm-based agents. arXiv preprint arXiv:2507.07957, 2025.
     * Wang et al. (2025a) Yu Wang, Ryuichi Takanobu, Zhiqi Liang, Yuzhen
       Mao, Yuanzhe Hu, Julian McAuley, and Xiaojian Wu. Mem-
       [MATH: <semantics><mo stretchy="false">{</mo><annotation
       encoding="application/x-tex">\{</annotation></semantics> :MATH]
       [MATH: <semantics><mo>\</mo><annotation
       encoding="application/x-tex">\backslash</annotation></semantics>
       :MATH]
       alpha
       [MATH: <semantics><mo stretchy="false">}</mo><annotation
       encoding="application/x-tex">\}</annotation></semantics> :MATH]
       : Learning memory construction via reinforcement learning. arXiv
       preprint arXiv:2509.25911, 2025a.
     * Wang et al. (2025b) Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried,
       and Graham Neubig. Agent workflow memory. In International
       Conference on Machine Learning, pages 63897–63911. PMLR, 2025b.
     * Wei et al. (2024) Jason Wei, Nguyen Karina, Hyung Won Chung, Yunxin
       Joy Jiao, Spencer Papay, Amelia Glaese, John Schulman, and William
       Fedus. Measuring short-form factuality in large language models.
       arXiv preprint arXiv:2411.04368, 2024.
     * Wei et al. (2025) Tianxin Wei, Noveen Sachdeva, Benjamin Coleman,
       Zhankui He, Yuanchen Bei, Xuying Ning, Mengting Ai, Yunzhe Li,
       Jingrui He, Ed H Chi, et al. Evo-memory: Benchmarking llm agent
       test-time learning with self-evolving memory. arXiv preprint
       arXiv:2511.20857, 2025.
     * Wu et al. (2024) Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang,
       Kai-Wei Chang, and Dong Yu. Longmemeval: Benchmarking chat
       assistants on long-term interactive memory. Adaptive Foundation
       Models: Evolving AI for Personalized and Efficient Learning, 2024.
     * Wu et al. (2025) Jinming Wu, Zihao Deng, Wei Li, Yiding Liu, Bo
       You, Bo Li, Zejun Ma, and Ziwei Liu. Mmsearch-r1: Incentivizing
       lmms to search. arXiv preprint arXiv:2506.20670, 2025.
     * Xiao et al. (2024) Chaojun Xiao, Pengle Zhang, Xu Han, Guangxuan
       Xiao, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, and Maosong Sun.
       Infllm: Training-free long-context extrapolation for llms with an
       efficient context memory. Advances in neural information processing
       systems, 37:119638–119661, 2024.
     * Xu and Peng (2025) Renjun Xu and Jingwen Peng. A comprehensive
       survey of deep research: Systems, methodologies, and applications.
       arXiv preprint arXiv:2506.12594, 2025.
     * Xu et al. (2025) Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao
       Tan, and Yongfeng Zhang. A-mem: Agentic memory for llm agents. The
       Thirty-ninth Annual Conference on Neural Information Processing
       Systems, 2025.
     * Yan et al. (2025) Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong
       Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe Bi, Kristian
       Kersting, Jeff Z Pan, et al. Memory-r1: Enhancing large language
       model agents to manage and utilize memories via reinforcement
       learning. arXiv preprint arXiv:2508.19828, 2025.
     * Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
       Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu
       Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
       Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu,
       Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou,
       Junyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng,
       Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui
       Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang,
       Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren,
       Yang Fan, Yang Su, Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong
       Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan
       Qiu. Qwen3 technical report, 2025.
       https://arxiv.org/abs/2505.09388.
     * Yang et al. (2018) Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua
       Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D
       Manning. Hotpotqa: A dataset for diverse, explainable multi-hop
       question answering. In Proceedings of the 2018 conference on
       empirical methods in natural language processing, pages 2369–2380,
       2018.
     * Yao et al. (2023) Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
       Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing
       reasoning and acting in language models, 2023.
     * Yu et al. (2025) Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie
       Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-Ying Ma, Jingjing
       Liu, Mingxuan Wang, et al. Memagent: Reshaping long-context llm
       with multi-conv rl-based memory agent. arXiv preprint
       arXiv:2507.02259, 2025.
     * Yu et al. (2026) Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan,
       Jiaqi Feng, Yaliang Li, and Libing Wu. Agentic memory: Learning
       unified long-term and short-term memory management for large
       language model agents. arXiv preprint arXiv:2601.01885, 2026.
     * Zhang et al. (2025a) Guibin Zhang, Muxin Fu, Guancheng Wan, Miao
       Yu, Kun Wang, and Shuicheng Yan. G-memory: Tracing hierarchical
       memory for multi-agent systems. arXiv preprint arXiv:2506.07398,
       2025a.
     * Zhang et al. (2025b) Guibin Zhang, Haotian Ren, Chong Zhan,
       Zhenhong Zhou, Junhao Wang, He Zhu, Wangchunshu Zhou, and Shuicheng
       Yan. Memevolve: Meta-evolution of agent memory systems. arXiv
       preprint arXiv:2512.18746, 2025b.
     * Zhang et al. (2025c) Wenlin Zhang, Xiaopeng Li, Yingyi Zhang,
       Pengyue Jia, Yichao Wang, Huifeng Guo, Yong Liu, and Xiangyu Zhao.
       Deep research: A survey of autonomous research agents. arXiv
       preprint arXiv:2508.12752, 2025c.
     * Zhao et al. (2024) Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu
       Lin, Yong-Jin Liu, and Gao Huang. Expel: Llm agents are
       experiential learners. In Proceedings of the AAAI Conference on
       Artificial Intelligence, volume 38, pages 19632–19642, 2024.
     * Zheng et al. (2025) Yuxiang Zheng, Dayuan Fu, Xiangkun Hu, Xiaojie
       Cai, Lyumanshan Ye, Pengrui Lu, and Pengfei Liu. Deepresearcher:
       Scaling deep research via reinforcement learning in real-world
       environments. In Proceedings of the 2025 Conference on Empirical
       Methods in Natural Language Processing, pages 414–431, 2025.
     * Zheng et al. (2026) Ziwei Zheng, Michael Yang, Jack Hong, Chenxiao
       Zhao, Guohai Xu, Le Yang, Chao Shen, and Xing Yu. Deepeyes:
       Incentivizing "thinking with images" via reinforcement learning,
       2026. https://arxiv.org/abs/2505.14362.
     * Zhong et al. (2024) Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye,
       and Yanlin Wang. Memorybank: Enhancing large language models with
       long-term memory. In Proceedings of the AAAI conference on
       artificial intelligence, volume 38, pages 19724–19731, 2024.
     * Zhou et al. (2025) Huichi Zhou, Yihang Chen, Siyuan Guo, Xue Yan,
       Kin Hei Lee, Zihan Wang, Ka Yiu Lee, Guchun Zhang, Kun Shao, Linyi
       Yang, et al. Memento: Fine-tuning llm agents without fine-tuning
       llms. arXiv preprint arXiv:2508.16153, 2025.

   \beginappendix

7 Training Details

   For the external tools used during training, we employ an offline
   text-to-text retriever built on a local wiki25 (Karpukhin et al., 2020)
   corpus and an offline image-to-image retriever based on cached search
   results. Specifically, the text retriever uses the E5-base-v2 (Wang et
   al., 2022) embedding model with a FAISS (Douze et al., 2025) index and
   returns the top-3 most relevant passages for each query. For image
   retrieval, we first upload each image to obtain a public URL via ImgBB,
   then use the Serper image search API to perform image-to-image
   retrieval based on the URL, and finally cache the returned results
   locally for offline use during training; the tool returns the top-3
   most relevant retrieved images.

   We implement our reinforcement learning training with veRL on 8 GPUs.
   For Executor training, the policy is initialized from
   Qwen2.5-VL-7B-Instruct, using FVQA-train for training and FVQA-test for
   validation. We adopt GRPO with a learning rate of
   [MATH: <semantics><mrow><mn>1</mn><mo lspace="0.222em"
   rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>6</mn></mro
   w></msup></mrow><annotation encoding="application/x-tex">1\times
   10^{-6}</annotation></semantics> :MATH]
   , a batch size of 128, and a micro-batch size of 4 per GPU. The maximum
   prompt and response lengths are both set to 16384 tokens. We use SGLang
   asynchronous rollout with 8 samples per query, and enable multi-turn
   tool interaction with up to 10 assistant turns, 10 user turns, and a
   maximum tool response length of 4096 tokens. The KL coefficient is set
   to 0.0, and the model is trained for 8 epochs with checkpoint saving
   every 10 steps.

   For Planner training, we adopt a tool-free setting and initialize the
   policy model from Qwen3-8B. The Planner is trained on a mixture of
   FVQA-train with images removed and MATPO, which is designed to
   alleviate planning discrepancies caused by the differences between
   text-only and multimodal tool environments, and FVQA-test for
   validation. We also use GRPO with a learning rate of
   [MATH: <semantics><mrow><mn>1</mn><mo lspace="0.222em"
   rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>6</mn></mro
   w></msup></mrow><annotation encoding="application/x-tex">1\times
   10^{-6}</annotation></semantics> :MATH]
   and a batch size of 128, while setting the maximum prompt length to
   24576 and the maximum response length to 8192. Rollout is performed
   asynchronously with 8 samples per query, and the Planner is trained for
   4 epochs on 4 GPUs with the KL coefficient set to 0.0.

8 Test Details

   During evaluation, we extend the tool configuration used in training by
   additionally introducing an online text-to-text search tool based on
   Serper, which returns the top-5 most relevant retrieved results. Thus,
   for multimodal evaluation, image-to-image search is conducted with
   Serper, while text-to-text search is performed using either the local
   wiki25 retriever or online Serper, depending on the benchmark setting.

   For inference, we use the vLLM engine with temperature set to 0.

   For TTL, we set the number of epochs to 1, the learning rate to
   [MATH: <semantics><mrow><mn>1</mn><mo lspace="0.222em"
   rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>6</mn></mro
   w></msup></mrow><annotation encoding="application/x-tex">1\times
   10^{-6}</annotation></semantics> :MATH]
   , and the number of rollouts per sample to 4. In the supervised
   setting, the Planner is initialized from our trained Planner model,
   while in the unsupervised setting, it is initialized from Qwen3-8B.

9 Memory-Based Baseline Details

   To ensure a fair comparison among memory-based search agents, we train
   three Executor variants with different extra prompt formats, while
   keeping all other training settings identical. These three variants
   correspond to three different ways of incorporating memory into the
   Executor: no extra prompt, workflow memory prompt, and guideline
   prompt.

   For the no extra prompt setting, the Executor is trained exactly
   following the default configuration, without any additional memory
   input. This variant is used for the No Memory baseline.

   For the long-context memory prompt setting, which is designed for
   methods that directly inject long-context memory into the Executor, we
   prepend the following extra prompt template:
   [MATH: <semantics><mrow><mrow><mtext
   class="ltx_mathvariant_monospace">Here are some memories for your
   reference:</mtext><mrow><mtext style="--ltx-fg-color:#00FFFF;"
   class="ltx_mathvariant_monospace" mathcolor="#00FFFF">\n</mtext><mtext
   style="--ltx-fg-color:#BF0040;" class="ltx_mathvariant_monospace"
   mathcolor="#BF0040">{memory context}</mtext><mtext
   style="--ltx-fg-color:#00FFFF;" class="ltx_mathvariant_monospace"
   mathcolor="#00FFFF">\n</mtext></mrow></mrow><mo>,</mo></mrow><annotatio
   n encoding="application/x-tex">\texttt{Here\ are\ some\ memories\ for\
   your\
   reference:{\color[rgb]{0,1,1}\definecolor[named]{pgfstrokecolor}{rgb}{0
   ,1,1}\pgfsys@color@cmyk@stroke{1}{0}{0}{0}\pgfsys@color@cmyk@fill{1}{0}
   {0}{0}\textbackslash
   n}{\color[rgb]{.75,0,.25}\definecolor[named]{pgfstrokecolor}{rgb}{.75,0
   ,.25}\{memory\
   context\}}{\color[rgb]{0,1,1}\definecolor[named]{pgfstrokecolor}{rgb}{0
   ,1,1}\pgfsys@color@cmyk@stroke{1}{0}{0}{0}\pgfsys@color@cmyk@fill{1}{0}
   {0}{0}\textbackslash n}},</annotation></semantics> :MATH]

   where
   [MATH: <semantics><mrow><mo stretchy="false">{</mo><mtext
   class="ltx_mathvariant_monospace">memory context</mtext><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{\texttt{memory\
   context}\}</annotation></semantics> :MATH]
   is filled with the retrieved relevant memory context. This setting is
   used for contextual memory methods such as RAG, Mem0, and A-Mem.

   For the guideline prompt setting, which is designed for methods that
   abstract memory into high-level guidance, we prepend the following
   extra prompt template:
   [MATH: <semantics><mrow><mrow><mtext
   class="ltx_mathvariant_monospace">Here is a guide for your
   reference:</mtext><mrow><mtext style="--ltx-fg-color:#00FFFF;"
   class="ltx_mathvariant_monospace" mathcolor="#00FFFF">\n</mtext><mtext
   style="--ltx-fg-color:#BF0040;" class="ltx_mathvariant_monospace"
   mathcolor="#BF0040">{plan}</mtext><mtext
   style="--ltx-fg-color:#00FFFF;" class="ltx_mathvariant_monospace"
   mathcolor="#00FFFF">\n</mtext></mrow><mtext
   class="ltx_mathvariant_monospace">Begin your answer:</mtext><mtext
   style="--ltx-fg-color:#00FFFF;" class="ltx_mathvariant_monospace"
   mathcolor="#00FFFF">\n</mtext></mrow><mo>,</mo></mrow><annotation
   encoding="application/x-tex">\texttt{Here\ is\ a\ guide\ for\ your\
   reference:{\color[rgb]{0,1,1}\definecolor[named]{pgfstrokecolor}{rgb}{0
   ,1,1}\pgfsys@color@cmyk@stroke{1}{0}{0}{0}\pgfsys@color@cmyk@fill{1}{0}
   {0}{0}\textbackslash
   n}{\color[rgb]{.75,0,.25}\definecolor[named]{pgfstrokecolor}{rgb}{.75,0
   ,.25}\{plan\}}{\color[rgb]{0,1,1}\definecolor[named]{pgfstrokecolor}{rg
   b}{0,1,1}\pgfsys@color@cmyk@stroke{1}{0}{0}{0}\pgfsys@color@cmyk@fill{1
   }{0}{0}{0}\textbackslash n}Begin\ your\
   answer:{\color[rgb]{0,1,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,1,
   1}\pgfsys@color@cmyk@stroke{1}{0}{0}{0}\pgfsys@color@cmyk@fill{1}{0}{0}
   {0}\textbackslash n}},</annotation></semantics> :MATH]

   where
   [MATH: <semantics><mrow><mo stretchy="false">{</mo><mtext
   class="ltx_mathvariant_monospace">plan</mtext><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{\texttt{plan}\}</annotation></semantics>
   :MATH]
   is filled with the abstracted high-level guidance generated from
   memory. This setting is used for methods such as ReasoningBank, ExpeL,
   Memento, and our MIA.

   Due to the involvement of multimodal inputs, we find the parametric
   retrieval optimization method provided by the Memento project difficult
   to apply. Consequently, we employed only their non-parametric version.

   During evaluation, each method uses its corresponding prompt template
   together with the matched Executor checkpoint trained under the same
   setting.

10 Memory Retrieval

   In this section, we provide the detailed implementation of the memory
   retrieval mechanism used in MIA. Given a current query, the system
   retrieves relevant historical trajectories from the Memory Manager to
   provide contextual support for planning. The retrieval score is
   computed by jointly considering semantic similarity, value reward, and
   frequency reward.

   The Memory Manager is organized by modality and question category. Each
   memory entry
   [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
   stores a historical trajectory together with its associated metadata,
   including the input question, the image caption, a judgment label, and
   several statistics for retrieval:
     * •
       [MATH: <semantics><msub><mi>u</mi><mi>i</mi></msub><annotation
       encoding="application/x-tex">u_{i}</annotation></semantics> :MATH]
       : the usage count of memory
       [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
       encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
       ,
     * •
       [MATH: <semantics><msub><mi>s</mi><mi>i</mi></msub><annotation
       encoding="application/x-tex">s_{i}</annotation></semantics> :MATH]
       : the success count of memory
       [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
       encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
       ,
     * •
       [MATH: <semantics><msub><mi>y</mi><mi>i</mi></msub><annotation
       encoding="application/x-tex">y_{i}</annotation></semantics> :MATH]
       : the judgment label of memory
       [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
       encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
       , where
       [MATH:
       <semantics><mrow><msub><mi>y</mi><mi>i</mi></msub><mo>∈</mo><mrow><
       mo stretchy="false">{</mo><mtext
       class="ltx_mathvariant_monospace">correct</mtext><mo>,</mo><mtext
       class="ltx_mathvariant_monospace">incorrect</mtext><mo
       stretchy="false">}</mo></mrow></mrow><annotation
       encoding="application/x-tex">y_{i}\in\{\texttt{correct},\texttt{inc
       orrect}\}</annotation></semantics> :MATH]
       .

   When a new memory is inserted, the counts are initialized to 0.

   To represent both textual questions and image captions in a unified
   embedding space, we use the sup-simcse-bert-base-uncased (Devlin et
   al., 2019) encoder. Given an input text
   [MATH: <semantics><mi>x</mi><annotation
   encoding="application/x-tex">x</annotation></semantics> :MATH]
   , we compute its embedding by mean-pooling the last hidden states of
   the encoder and then applying
   [MATH: <semantics><msub><mi>L</mi><mn>2</mn></msub><annotation
   encoding="application/x-tex">L_{2}</annotation></semantics> :MATH]
   normalization:
   [MATH: <semantics><mrow><mrow><mrow><mi>𝐞</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>N</mi><mo
   lspace="0em" rspace="0em">​</mo><mi>o</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mpadded style="width:0.708em;"
   width="0.708em"><mi>m</mi></mpadded><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo>(</mo><mrow><mi>M</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>n</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>P</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>o</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>o</mi><mo lspace="0em"
   rspace="0em">​</mo><mpadded style="width:0.148em;"
   width="0.148em"><mi>l</mi></mpadded><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo>(</mo><mrow><mi>E</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>n</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>o</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>d</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>x</mi><mo
   stretchy="false">)</mo></mrow></mrow><mo>)</mo></mrow></mrow><mo>)</mo>
   </mrow></mrow></mrow><mo lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">\mathbf{e}(x)={Norm}\!\left({MeanPool}\!\l
   eft({Encoder}(x)\right)\right).</annotation></semantics> :MATH]

   For a query consisting of a question
   [MATH: <semantics><mi>q</mi><annotation
   encoding="application/x-tex">q</annotation></semantics> :MATH]
   and an image caption
   [MATH: <semantics><mi>c</mi><annotation
   encoding="application/x-tex">c</annotation></semantics> :MATH]
   , we compute their embeddings:
   [MATH:
   <semantics><mrow><mrow><mrow><msub><mi>𝐞</mi><mi>q</mi></msub><mo>=</mo
   ><mrow><mi>𝐞</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>q</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow><mo>,</mo><mrow><msub><mi>𝐞
   </mi><mi>c</mi></msub><mo>=</mo><mrow><mi>𝐞</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo stretchy="false">(</mo><mi>c</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow></mrow><mo
   lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">\mathbf{e}_{q}=\mathbf{e}(q),\mathbf{e}_{c
   }=\mathbf{e}(c).</annotation></semantics> :MATH]

   For each memory entry
   [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
   , let
   [MATH:
   <semantics><msub><mi>𝐞</mi><msub><mi>q</mi><mi>i</mi></msub></msub><ann
   otation
   encoding="application/x-tex">\mathbf{e}_{q_{i}}</annotation></semantics
   > :MATH]
   and
   [MATH:
   <semantics><msub><mi>𝐞</mi><msub><mi>c</mi><mi>i</mi></msub></msub><ann
   otation
   encoding="application/x-tex">\mathbf{e}_{c_{i}}</annotation></semantics
   > :MATH]
   denote the stored embeddings of its question and caption. We first
   compute the question-level similarity:
   [MATH: <semantics><mrow><mrow><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msubsup><mi>m</mi><mi>i</mi><mrow><mo
   stretchy="false">(</mo><mi>q</mi><mo
   stretchy="false">)</mo></mrow></msubsup></mrow><mo>=</mo><mrow><mpadded
   style="width:1.216em;"
   width="1.216em"><mi>cos</mi></mpadded><mo>⁡</mo><mrow><mo>(</mo><msub><
   mi>𝐞</mi><mi>q</mi></msub><mo>,</mo><msub><mi>𝐞</mi><msub><mi>q</mi><mi
   >i</mi></msub></msub><mo>)</mo></mrow></mrow></mrow><mo>,</mo></mrow><a
   nnotation
   encoding="application/x-tex">{sim}_{i}^{(q)}={\cos}\!\left(\mathbf{e}_{
   q},\mathbf{e}_{q_{i}}\right),</annotation></semantics> :MATH]

   and the caption-level similarity:
   [MATH: <semantics><mrow><mrow><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msubsup><mi>m</mi><mi>i</mi><mrow><mo
   stretchy="false">(</mo><mi>c</mi><mo
   stretchy="false">)</mo></mrow></msubsup></mrow><mo>=</mo><mrow><mpadded
   style="width:1.216em;"
   width="1.216em"><mi>cos</mi></mpadded><mo>⁡</mo><mrow><mo>(</mo><msub><
   mi>𝐞</mi><mi>c</mi></msub><mo>,</mo><msub><mi>𝐞</mi><msub><mi>c</mi><mi
   >i</mi></msub></msub><mo>)</mo></mrow></mrow></mrow><mo
   lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">{sim}_{i}^{(c)}={\cos}\!\left(\mathbf{e}_{
   c},\mathbf{e}_{c_{i}}\right).</annotation></semantics> :MATH]

   If an image caption is available, the semantic similarity score is
   defined as
   [MATH: <semantics><mrow><mrow><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>m</mi><mi>i</mi></msub></mrow><mo>=</mo><m
   row><mrow><msub><mi>α</mi><mi>q</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msubsup><mi>m</mi><mi>i</mi><mrow><mo
   stretchy="false">(</mo><mi>q</mi><mo
   stretchy="false">)</mo></mrow></msubsup></mrow><mo>+</mo><mrow><msub><m
   i>α</mi><mi>c</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msubsup><mi>m</mi><mi>i</mi><mrow><mo
   stretchy="false">(</mo><mi>c</mi><mo
   stretchy="false">)</mo></mrow></msubsup></mrow></mrow></mrow><mo>,</mo>
   </mrow><annotation
   encoding="application/x-tex">{Sim}_{i}=\alpha_{q}{sim}_{i}^{(q)}+\alpha
   _{c}{sim}_{i}^{(c)},</annotation></semantics> :MATH]

   where
   [MATH: <semantics><msub><mi>α</mi><mi>q</mi></msub><annotation
   encoding="application/x-tex">\alpha_{q}</annotation></semantics> :MATH]
   and
   [MATH: <semantics><msub><mi>α</mi><mi>c</mi></msub><annotation
   encoding="application/x-tex">\alpha_{c}</annotation></semantics> :MATH]
   are the relative weights of question and caption similarity. In our
   implementation, we use
   [MATH:
   <semantics><mrow><mrow><mrow><msub><mi>α</mi><mi>q</mi></msub><mo>=</mo
   ><mn>0.8</mn></mrow><mo>,</mo><mrow><msub><mi>α</mi><mi>c</mi></msub><m
   o>=</mo><mn>0.2</mn></mrow></mrow><mo
   lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">\alpha_{q}=0.8,\alpha_{c}=0.2.</annotation
   ></semantics> :MATH]
   If no image caption is available, we use only the question similarity:
   [MATH: <semantics><mrow><mrow><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>m</mi><mi>i</mi></msub></mrow><mo>=</mo><m
   row><mi>s</mi><mo lspace="0em" rspace="0em">​</mo><mi>i</mi><mo
   lspace="0em" rspace="0em">​</mo><msubsup><mi>m</mi><mi>i</mi><mrow><mo
   stretchy="false">(</mo><mi>q</mi><mo
   stretchy="false">)</mo></mrow></msubsup></mrow></mrow><mo
   lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">{Sim}_{i}={sim}_{i}^{(q)}.</annotation></s
   emantics> :MATH]
   We then normalize the semantic similarity scores within the current
   memory bucket using min-max normalization:
   [MATH: <semantics><mrow><mrow><msub><mover
   accent="true"><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>m</mi></mrow><mo>^</mo></mover><mi>i</mi></msub>
   <mo>=</mo><mfrac><mrow><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>m</mi><mi>i</mi></msub></mrow><mo>−</mo><m
   row><msub><mi>min</mi><mi>j</mi></msub><mo
   lspace="0.167em">⁡</mo><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>m</mi><mi>j</mi></msub></mrow></mrow></mro
   w><mrow><mrow><mrow><msub><mi>max</mi><mi>j</mi></msub><mo
   lspace="0.167em">⁡</mo><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>m</mi><mi>j</mi></msub></mrow></mrow><mo>−
   </mo><mrow><msub><mi>min</mi><mi>j</mi></msub><mo
   lspace="0.167em">⁡</mo><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>m</mi><mi>j</mi></msub></mrow></mrow></mro
   w><mo>+</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>8</mn></mrow></msup></
   mrow></mfrac></mrow><mo lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">\widehat{Sim}_{i}=\frac{{Sim}_{i}-\min_{j}
   {Sim}_{j}}{\max_{j}{Sim}_{j}-\min_{j}{Sim}_{j}+10^{-8}}.</annotation></
   semantics> :MATH]

   In addition to semantic similarity, retrieval also considers the
   historical quality of each memory. We define the value reward of memory
   [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
   as its empirical success ratio:
   [MATH: <semantics><mrow><mrow><mrow><mi>V</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>l</mi><mi>i</mi></msub></mrow><mo>=</mo><m
   frac><msub><mi>s</mi><mi>i</mi></msub><mrow><msub><mi>u</mi><mi>i</mi><
   /msub><mo>+</mo><mn>1</mn></mrow></mfrac></mrow><mo>,</mo></mrow><annot
   ation
   encoding="application/x-tex">{Val}_{i}=\frac{s_{i}}{u_{i}+1},</annotati
   on></semantics> :MATH]
   where
   [MATH: <semantics><msub><mi>s</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">s_{i}</annotation></semantics> :MATH]
   is the success count and
   [MATH: <semantics><msub><mi>u</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">u_{i}</annotation></semantics> :MATH]
   is the usage count of memory
   [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
   . This term favors memories that have demonstrated stronger historical
   usefulness.

   To additionally account for memory usage frequency and stabilize
   retrieval for rarely used memories, we introduce a frequency reward:
   [MATH: <semantics><mrow><mrow><mrow><mi>F</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>q</mi><mi>i</mi></msub></mrow><mo>=</mo><m
   frac><mn>1</mn><mrow><msub><mi>u</mi><mi>i</mi></msub><mo>+</mo><mn>1</
   mn></mrow></mfrac></mrow><mo lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">{Freq}_{i}=\frac{1}{u_{i}+1}.</annotation>
   </semantics> :MATH]

   The final retrieval score for memory
   [MATH: <semantics><msub><mi>m</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">m_{i}</annotation></semantics> :MATH]
   is computed by combining semantic similarity, value reward, and
   frequency reward:
   [MATH: <semantics><mrow><mrow><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>o</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>m</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mrow><msub><mi>λ<
   /mi><mi>s</mi></msub><mo lspace="0em" rspace="0em">​</mo><msub><mover
   accent="true"><mrow><mi>S</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>m</mi></mrow><mo>^</mo></mover><mi>i</mi></msub>
   </mrow><mo>+</mo><mrow><msub><mi>λ</mi><mi>v</mi></msub><mo
   lspace="0em" rspace="0em">​</mo><mi>V</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>l</mi><mi>i</mi></msub></mrow><mo>+</mo><m
   row><msub><mi>λ</mi><mi>f</mi></msub><mo lspace="0em"
   rspace="0em">​</mo><mi>F</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><msub><mi>q</mi><mi>i</mi></msub></mrow></mrow></mro
   w><mo>,</mo></mrow><annotation
   encoding="application/x-tex">{Score}(m_{i})=\lambda_{s}\widehat{Sim}_{i
   }+\lambda_{v}{Val}_{i}+\lambda_{f}{Freq}_{i},</annotation></semantics>
   :MATH]

   where
   [MATH: <semantics><msub><mi>λ</mi><mi>s</mi></msub><annotation
   encoding="application/x-tex">\lambda_{s}</annotation></semantics>
   :MATH]
   ,
   [MATH: <semantics><msub><mi>λ</mi><mi>v</mi></msub><annotation
   encoding="application/x-tex">\lambda_{v}</annotation></semantics>
   :MATH]
   , and
   [MATH: <semantics><msub><mi>λ</mi><mi>f</mi></msub><annotation
   encoding="application/x-tex">\lambda_{f}</annotation></semantics>
   :MATH]
   denote the weights of semantic similarity, value reward, and frequency
   reward, respectively. In this work, we set
   [MATH:
   <semantics><mrow><mrow><mrow><msub><mi>λ</mi><mi>s</mi></msub><mo>=</mo
   ><mn>0.7</mn></mrow><mo>,</mo><mrow><msub><mi>λ</mi><mi>v</mi></msub><m
   o>=</mo><msub><mi>λ</mi><mi>f</mi></msub><mo>=</mo><mn>0.3</mn></mrow><
   /mrow><mo lspace="0em">.</mo></mrow><annotation
   encoding="application/x-tex">\lambda_{s}=0.7,\lambda_{v}=\lambda_{f}=0.
   3.</annotation></semantics> :MATH]

11 Dataset Settings

   Table 8: Dataset settings used in this work.
   Dataset    Modality   # Examples Setting          Usage
   FVQA-train Image-text 4,856      From MMSearch-R1 Training
   FVQA-test  Image-text 1,800      From MMSearch-R1 Evaluation
   InfoSeek   Image-text 2,000      From MMSearch-R1 Evaluation
   LiveVQA    Image-text 2,384      Public Version   Evaluation
   SimpleVQA  Image-text 1,013      From MMSearch-R1 Evaluation
   MMSearch   Image-text 171        From MMSearch-R1 Evaluation
   In-house 1 Image-text 295        In-house         Evaluation
   In-house 2 Image-text 505        In-house         Evaluation
   MATPO      Text-only  6,175      From MATPO       Planner Training
   2Wiki      Text-only  12,576     Public Version   Evaluation
   HotpotQA   Text-only  7,405      Public Version   Evaluation
   SimpleQA   Text-only  4,327      Public Version   Evaluation
   GAIA-Text  Text-only  103        From MATPO       Evaluation

   We evaluate our framework on both multimodal and text-only datasets.
   This section summarizes the dataset settings used in our experiments.
   Table 8 summarizes all datasets used in this work.

   FVQA-train: FVQA-train is a multimodal training set containing 4,856
   image-question-answer examples. We adopt this split from the
   MMSearch-R1 setting. The dataset focuses on factual visual question
   answering, where answering requires combining visual content with
   external knowledge. In our experiments, it is used to train both the
   Executor and the Planner.

   FVQA-test: FVQA-test is a multimodal evaluation set containing 1,800
   image-question-answer examples, also adopted from the MMSearch-R1
   setting. Like the training split, it targets factual visual question
   answering grounded in both images and associated knowledge, and is used
   as a held-out evaluation benchmark.

   InfoSeek: We use a 2,000-example evaluation subset of InfoSeek from the
   MMSearch-R1 setting. InfoSeek is a multimodal information-seeking
   benchmark in which each example is built around an image and a
   knowledge-intensive question whose answer depends on factual
   information beyond direct visual perception. We use this subset for
   multimodal evaluation.

   LiveVQA: We use the currently accessible public version of LiveVQA,
   which contains 2,384 multimodal examples. LiveVQA is a real-world
   visual question answering benchmark emphasizing information-rich
   questions that often require both image understanding and external
   factual knowledge. Although MMSearch-R1 reports results on a
   3,602-example version, that version appears to be deprecated or no
   longer publicly accessible; therefore, all experiments in this work are
   conducted on the public 2,384-example version.

   SimpleVQA: We use the English subset of SimpleVQA containing 1,013
   multimodal examples, following the MMSearch-R1 setting. SimpleVQA is a
   factual visual question answering benchmark designed to test whether
   models can answer short, objective questions about real-world entities,
   attributes, and properties based on visual input and factual knowledge.

   MMSearch: We use the visual-question subset of MMSearch containing 171
   examples, adopted from MMSearch-R1. MMSearch is a benchmark for
   multimodal search and knowledge-intensive reasoning. The subset used in
   our experiments consists of image-based question answering instances
   and is used for multimodal evaluation.

   In-house 1: We develop a systematic pipeline to construct multimodal QA
   instances in scientific domains such as Physics, Chemistry, and
   Biology. Starting from an initial website, we crawl relevant textual
   content and extract informative statements, then employ an LLM to
   iteratively generate related concepts or keywords for further search
   and webpage collection. After gathering sufficient cross-source
   evidence, we synthesize question-answer pairs grounded in the collected
   texts. We then identify QA instances with visually representable
   entities, extract the corresponding entity names, and retrieve matched
   images through web search to form multimodal examples. In total, we
   collect 295 image-question-answer examples in this way.

   In-house 2: We develop a systematic pipeline to construct complex
   multi-hop VQA instances. Initially, raw image-text corpora are
   harvested from real-time news sources such as CNN to ensure the
   timeliness and authenticity of entities. We then employ
   Qwen2.5-VL-72B-Instruct to analyze the images and anchor key visual
   entities (e.g., pivotal events or persons) as reasoning pivots. Based
   on these anchors, we construct a triple dependency chain within the
   corpora to generate complex questions, ensuring that all questions and
   answers are grounded in authentic textual evidence. The resulting
   dataset primarily covers dynamic domains such as Sports, Entertainment,
   and other multifaceted social events, ensuring a diverse distribution
   of visual-semantic challenges. We collect 505 image-question-answer
   examples in this way.

   MATPO: We use 6,175 text-only examples from MATPO as part of the
   Planner training data, following the MATPO setting. This dataset
   contains text-based tasks centered on question answering, information
   seeking, and reasoning, and is used to improve the planning ability of
   the model in textual environments.

   2Wiki: The dataset includes 12,576 text-only samples. 2WikiMultihopQA
   (2Wiki) is a multi-hop question answering benchmark in which answering
   a question requires combining evidence from multiple pieces of textual
   information, typically across different documents or entities.

   HotpotQA: The dataset includes 7,405 text-only samples. HotpotQA is a
   widely used multi-hop question answering benchmark that tests retrieval
   and reasoning over multiple supporting documents, with an emphasis on
   compositional and explainable QA.

   SimpleQA: The dataset includes 4,327 text-only samples. SimpleQA is a
   factual question answering benchmark composed of short and direct
   questions with concise fact-based answers, and is used to assess basic
   factual QA ability in the text-only setting.

   GAIA-Text: We use GAIA-Text, a text-only evaluation subset containing
   103 examples, adopted from the MATPO setting. This subset is derived
   from GAIA and consists of general text-based tasks requiring
   information seeking, reasoning, and problem-solving, and is used as an
   additional text-only evaluation benchmark.

12 Algorithm

   Algorithm 1 Executor Training Rollout Process
   1:Question
   [MATH: <semantics><mi>Q</mi><annotation
   encoding="application/x-tex">Q</annotation></semantics> :MATH]
   , Image
   [MATH: <semantics><mi>I</mi><annotation
   encoding="application/x-tex">I</annotation></semantics> :MATH]
   , Pre-trained Planner
   [MATH: <semantics><msub><mi>M</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">M_{P}</annotation></semantics> :MATH]
   , Tool Set
   [MATH: <semantics><mi>T</mi><annotation
   encoding="application/x-tex">T</annotation></semantics> :MATH]
   , Policy
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   .
   2:Reward
   [MATH: <semantics><mi>R</mi><annotation
   encoding="application/x-tex">R</annotation></semantics> :MATH]
   .
   3:Provide
   [MATH: <semantics><mi>Q</mi><annotation
   encoding="application/x-tex">Q</annotation></semantics> :MATH]
   to
   [MATH: <semantics><msub><mi>M</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">M_{P}</annotation></semantics> :MATH]
   to generate initial Plan
   [MATH: <semantics><msub><mi>P</mi><mrow><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>n</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>t</mi></mrow></msub><annotation
   encoding="application/x-tex">P_{init}</annotation></semantics> :MATH]
   .
   4:Construct input context
   [MATH: <semantics><mrow><mi>C</mi><mo stretchy="false">←</mo><mrow><mo
   stretchy="false">{</mo><mi>Q</mi><mo>,</mo><mi>I</mi><mo>,</mo><msub><m
   i>P</mi><mrow><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>n</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>t</mi></mrow></msub><mo>,</mo><mtext>Prompt
   Template</mtext><mo stretchy="false">}</mo></mrow></mrow><annotation
   encoding="application/x-tex">C\leftarrow\{Q,I,P_{init},\text{Prompt
   Template}\}</annotation></semantics> :MATH]
   .
   5:Input
   [MATH: <semantics><mi>C</mi><annotation
   encoding="application/x-tex">C</annotation></semantics> :MATH]
   to Policy
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   .
   6:loop
   7:  
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   performs rollout to generate thought process
   [MATH: <semantics><msub><mi>t</mi><mi>h</mi></msub><annotation
   encoding="application/x-tex">t_{h}</annotation></semantics> :MATH]
   based on current state.
   8:  if
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   decides to call a tool then
   9:   Execute tool
   [MATH:
   <semantics><mrow><mi>t</mi><mo>∈</mo><mi>T</mi></mrow><annotation
   encoding="application/x-tex">t\in T</annotation></semantics> :MATH]
   , obtain result
   [MATH: <semantics><msub><mi>O</mi><mi>t</mi></msub><annotation
   encoding="application/x-tex">O_{t}</annotation></semantics> :MATH]
   .
   10:   Update context with
   [MATH: <semantics><msub><mi>O</mi><mi>t</mi></msub><annotation
   encoding="application/x-tex">O_{t}</annotation></semantics> :MATH]
   .
   11:  else
   12:   
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   performs rollout to generate candidate answer
   [MATH: <semantics><mi>A</mi><annotation
   encoding="application/x-tex">A</annotation></semantics> :MATH]
   .
   13:   LLM Judger evaluates correctness of
   [MATH: <semantics><mi>A</mi><annotation
   encoding="application/x-tex">A</annotation></semantics> :MATH]
   .
   14:   if
   [MATH: <semantics><mi>A</mi><annotation
   encoding="application/x-tex">A</annotation></semantics> :MATH]
   is Incorrect
   [MATH: <semantics><mo>∧</mo><annotation
   encoding="application/x-tex">\land</annotation></semantics> :MATH]
   Re-plan has not been triggered then
   15:     Provide interaction history to
   [MATH: <semantics><msub><mi>M</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">M_{P}</annotation></semantics> :MATH]
   to generate revised Plan
   [MATH: <semantics><msub><mi>P</mi><mrow><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>v</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>d</mi></mrow></msub><annotation
   encoding="application/x-tex">P_{revised}</annotation></semantics>
   :MATH]
   .
   16:     Update context with
   [MATH: <semantics><msub><mi>P</mi><mrow><mi>r</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>v</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>e</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>d</mi></mrow></msub><annotation
   encoding="application/x-tex">P_{revised}</annotation></semantics>
   :MATH]
   .
   17:     Mark Re-plan as triggered.
   18:   end if
   19:  end if
   20:end loop
   21:Compute reward
   [MATH: <semantics><mi>R</mi><annotation
   encoding="application/x-tex">R</annotation></semantics> :MATH]
   according to Eq. (2).
   22:return
   [MATH: <semantics><mi>R</mi><annotation
   encoding="application/x-tex">R</annotation></semantics> :MATH]
   .
   Algorithm 2 Planner Training Rollout Process
   1:Question
   [MATH: <semantics><mi>Q</mi><annotation
   encoding="application/x-tex">Q</annotation></semantics> :MATH]
   , Image
   [MATH: <semantics><mi>I</mi><annotation
   encoding="application/x-tex">I</annotation></semantics> :MATH]
   , Memory Context
   [MATH: <semantics><mi>M</mi><annotation
   encoding="application/x-tex">M</annotation></semantics> :MATH]
   , Trained Executor
   [MATH: <semantics><msub><mi>M</mi><mi>E</mi></msub><annotation
   encoding="application/x-tex">M_{E}</annotation></semantics> :MATH]
   , Tool Set
   [MATH: <semantics><mi>T</mi><annotation
   encoding="application/x-tex">T</annotation></semantics> :MATH]
   , Policy
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   .
   2:Reward
   [MATH: <semantics><mi>R</mi><annotation
   encoding="application/x-tex">R</annotation></semantics> :MATH]
   .
   3:Construct input context
   [MATH: <semantics><mrow><mi>C</mi><mo stretchy="false">←</mo><mrow><mo
   stretchy="false">{</mo><mi>M</mi><mo>,</mo><mi>Q</mi><mo>,</mo><mtext>P
   rompt Template</mtext><mo
   stretchy="false">}</mo></mrow></mrow><annotation
   encoding="application/x-tex">C\leftarrow\{M,Q,\text{Prompt
   Template}\}</annotation></semantics> :MATH]
   .
   4:Input
   [MATH: <semantics><mi>C</mi><annotation
   encoding="application/x-tex">C</annotation></semantics> :MATH]
   to Policy
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   .
   5:
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   performs rollout to generate Chain-of-Thought
   [MATH: <semantics><msub><mi>t</mi><mi>h</mi></msub><annotation
   encoding="application/x-tex">t_{h}</annotation></semantics> :MATH]
   and Initial Plan
   [MATH: <semantics><msub><mi>P</mi><mrow><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>n</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>t</mi></mrow></msub><annotation
   encoding="application/x-tex">P_{init}</annotation></semantics> :MATH]
   .
   6:
   [MATH: <semantics><msub><mi>M</mi><mi>E</mi></msub><annotation
   encoding="application/x-tex">M_{E}</annotation></semantics> :MATH]
   interacts with environment using
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mi>Q</mi><mo>,</mo><mi>I</mi><mo>,</mo><mi>T</m
   i><mo>,</mo><msub><mi>P</mi><mrow><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>n</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>t</mi></mrow></msub><mo
   stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{Q,I,T,P_{init}\}</annotation></semantics
   > :MATH]
   to obtain Trajectory
   [MATH: <semantics><msub><mi>τ</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">\tau_{1}</annotation></semantics> :MATH]
   and Result
   [MATH: <semantics><msub><mi>R</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">R_{1}</annotation></semantics> :MATH]
   .
   7:
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   analyzes
   [MATH: <semantics><msub><mi>τ</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">\tau_{1}</annotation></semantics> :MATH]
   and
   [MATH: <semantics><msub><mi>R</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">R_{1}</annotation></semantics> :MATH]
   to decide whether to Reflect & Replan.
   8:if
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   decides to Reflect & Replan then
   9:  
   [MATH: <semantics><msub><mi>π</mi><mi>θ</mi></msub><annotation
   encoding="application/x-tex">\pi_{\theta}</annotation></semantics>
   :MATH]
   performs rollout to generate Reflection and Supplementary Plan
   [MATH: <semantics><msub><mi>P</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>p</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>p</mi></mrow></msub><annotation
   encoding="application/x-tex">P_{supp}</annotation></semantics> :MATH]
   .
   10:  
   [MATH: <semantics><msub><mi>M</mi><mi>E</mi></msub><annotation
   encoding="application/x-tex">M_{E}</annotation></semantics> :MATH]
   continues interaction based on
   [MATH: <semantics><msub><mi>τ</mi><mn>1</mn></msub><annotation
   encoding="application/x-tex">\tau_{1}</annotation></semantics> :MATH]
   and
   [MATH: <semantics><msub><mi>P</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>p</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>p</mi></mrow></msub><annotation
   encoding="application/x-tex">P_{supp}</annotation></semantics> :MATH]
   to obtain Trajectory
   [MATH: <semantics><msub><mi>τ</mi><mn>2</mn></msub><annotation
   encoding="application/x-tex">\tau_{2}</annotation></semantics> :MATH]
   and Result
   [MATH: <semantics><msub><mi>R</mi><mn>2</mn></msub><annotation
   encoding="application/x-tex">R_{2}</annotation></semantics> :MATH]
   .
   11:end if
   12:Compute reward
   [MATH: <semantics><mi>R</mi><annotation
   encoding="application/x-tex">R</annotation></semantics> :MATH]
   according to Eq. (4).
   13:return
   [MATH: <semantics><mi>R</mi><annotation
   encoding="application/x-tex">R</annotation></semantics> :MATH]
   .
   Algorithm 3 Test-Time Learning Process
   1:Question
   [MATH: <semantics><mi>Q</mi><annotation
   encoding="application/x-tex">Q</annotation></semantics> :MATH]
   , Image
   [MATH: <semantics><mi>I</mi><annotation
   encoding="application/x-tex">I</annotation></semantics> :MATH]
   , Planner
   [MATH: <semantics><msub><mi>π</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">\pi_{P}</annotation></semantics> :MATH]
   , frozen Executor
   [MATH: <semantics><msub><mi>M</mi><mi>E</mi></msub><annotation
   encoding="application/x-tex">M_{E}</annotation></semantics> :MATH]
   , Memory Manager & Router
   [MATH: <semantics><msub><mi>M</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">M_{R}</annotation></semantics> :MATH]
   , Tool Set
   [MATH: <semantics><mi>T</mi><annotation
   encoding="application/x-tex">T</annotation></semantics> :MATH]
   , Group Size
   [MATH: <semantics><mi>G</mi><annotation
   encoding="application/x-tex">G</annotation></semantics> :MATH]
   .
   2:Final Response
   [MATH: <semantics><mi>y</mi><annotation
   encoding="application/x-tex">y</annotation></semantics> :MATH]
   .
   3:Planner
   [MATH: <semantics><msub><mi>π</mi><mi>P</mi></msub><annotation
   encoding="application/x-tex">\pi_{P}</annotation></semantics> :MATH]
   performs rollout to generate
   [MATH: <semantics><mi>G</mi><annotation
   encoding="application/x-tex">G</annotation></semantics> :MATH]
   reasoning-plan pairs
   [MATH: <semantics><msubsup><mrow><mo stretchy="false">{</mo><mrow><mo
   stretchy="false">(</mo><msub><mi>t</mi><mi>i</mi></msub><mo>,</mo><msub
   ><mi>p</mi><mi>i</mi></msub><mo stretchy="false">)</mo></mrow><mo
   stretchy="false">}</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mro
   w><mi>G</mi></msubsup><annotation
   encoding="application/x-tex">\{(t_{i},p_{i})\}_{i=1}^{G}</annotation></
   semantics> :MATH]
   .
   4:
   [MATH: <semantics><msub><mi>M</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">M_{R}</annotation></semantics> :MATH]
   retrieves relevant examples
   [MATH: <semantics><mi>e</mi><annotation
   encoding="application/x-tex">e</annotation></semantics> :MATH]
   from the Meta Plan Memory.
   5:
   [MATH: <semantics><msub><mi>M</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">M_{R}</annotation></semantics> :MATH]
   uses
   [MATH: <semantics><mi>e</mi><annotation
   encoding="application/x-tex">e</annotation></semantics> :MATH]
   as in-context references to select the best plan
   [MATH: <semantics><msup><mi>p</mi><mo>∗</mo></msup><annotation
   encoding="application/x-tex">p^{*}</annotation></semantics> :MATH]
   from
   [MATH: <semantics><msubsup><mrow><mo
   stretchy="false">{</mo><msub><mi>p</mi><mi>i</mi></msub><mo
   stretchy="false">}</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mro
   w><mi>G</mi></msubsup><annotation
   encoding="application/x-tex">\{p_{i}\}_{i=1}^{G}</annotation></semantic
   s> :MATH]
   .
   6:Interact with the environment
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mi>Q</mi><mo>,</mo><mi>I</mi><mo>,</mo><msup><m
   i>p</mi><mo>∗</mo></msup><mo>,</mo><mi>T</mi><mo>,</mo><msub><mi>M</mi>
   <mi>E</mi></msub><mo stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{Q,I,p^{*},T,M_{E}\}</annotation></semant
   ics> :MATH]
   .
   7:Obtain trajectory
   [MATH: <semantics><msup><mi>τ</mi><mo>∗</mo></msup><annotation
   encoding="application/x-tex">\tau^{*}</annotation></semantics> :MATH]
   and final response
   [MATH: <semantics><mi>y</mi><annotation
   encoding="application/x-tex">y</annotation></semantics> :MATH]
   .
   8:for each remaining plan
   [MATH:
   <semantics><mrow><msub><mi>p</mi><mi>i</mi></msub><mo>≠</mo><msup><mi>p
   </mi><mo>∗</mo></msup></mrow><annotation
   encoding="application/x-tex">p_{i}\neq p^{*}</annotation></semantics>
   :MATH]
   do
   9:  Interact with the environment
   [MATH: <semantics><mrow><mo
   stretchy="false">{</mo><mi>Q</mi><mo>,</mo><mi>I</mi><mo>,</mo><msub><m
   i>p</mi><mi>i</mi></msub><mo>,</mo><mi>T</mi><mo>,</mo><msub><mi>M</mi>
   <mi>E</mi></msub><mo stretchy="false">}</mo></mrow><annotation
   encoding="application/x-tex">\{Q,I,p_{i},T,M_{E}\}</annotation></semant
   ics> :MATH]
   .
   10:  Obtain trajectory
   [MATH: <semantics><msub><mi>τ</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">\tau_{i}</annotation></semantics> :MATH]
   and corresponding result.
   11:end for
   12:Form the trajectory set
   [MATH: <semantics><mrow><mi class="ltx_font_mathcaligraphic">𝒯</mi><mo
   stretchy="false">←</mo><mrow><mrow><mo
   stretchy="false">{</mo><msup><mi>τ</mi><mo>∗</mo></msup><mo
   stretchy="false">}</mo></mrow><mo>∪</mo><mrow><mo
   stretchy="false">{</mo><msub><mi>τ</mi><mi>i</mi></msub><mo
   stretchy="false">}</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">\mathcal{T}\leftarrow\{\tau^{*}\}\cup\{\ta
   u_{i}\}</annotation></semantics> :MATH]
   .
   13:LLM Judger evaluates the correctness of each rollout outcome.
   14:Partition
   [MATH: <semantics><mi
   class="ltx_font_mathcaligraphic">𝒯</mi><annotation
   encoding="application/x-tex">\mathcal{T}</annotation></semantics>
   :MATH]
   into successful set
   [MATH: <semantics><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub><annotation
   encoding="application/x-tex">\mathcal{S}_{succ}</annotation></semantics
   > :MATH]
   and failed set
   [MATH: <semantics><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub><annotation
   encoding="application/x-tex">\mathcal{S}_{fail}</annotation></semantics
   > :MATH]
   .
   15:for each plan-trajectory pair
   [MATH: <semantics><mrow><mo
   stretchy="false">(</mo><msub><mi>p</mi><mi>i</mi></msub><mo>,</mo><msub
   ><mi>τ</mi><mi>i</mi></msub><mo
   stretchy="false">)</mo></mrow><annotation
   encoding="application/x-tex">(p_{i},\tau_{i})</annotation></semantics>
   :MATH]
   in
   [MATH: <semantics><mi
   class="ltx_font_mathcaligraphic">𝒯</mi><annotation
   encoding="application/x-tex">\mathcal{T}</annotation></semantics>
   :MATH]
   do
   16:  Compute reward
   [MATH: <semantics><msub><mi>R</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">R_{i}</annotation></semantics> :MATH]
   according to Eq. (4).
   17:end for
   18:Compute reward mean
   [MATH: <semantics><msub><mi>μ</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">\mu_{R}</annotation></semantics> :MATH]
   and standard deviation
   [MATH: <semantics><msub><mi>σ</mi><mi>R</mi></msub><annotation
   encoding="application/x-tex">\sigma_{R}</annotation></semantics> :MATH]
   .
   19:for each reward
   [MATH: <semantics><msub><mi>R</mi><mi>i</mi></msub><annotation
   encoding="application/x-tex">R_{i}</annotation></semantics> :MATH]
   do
   20:  Compute grouped advantage
   [MATH: <semantics><mrow><msub><mover
   accent="true"><mi>A</mi><mo>^</mo></mover><mi>i</mi></msub><mo
   stretchy="false">←</mo><mfrac><mrow><msub><mi>R</mi><mi>i</mi></msub><m
   o>−</mo><msub><mi>μ</mi><mi>R</mi></msub></mrow><mrow><msub><mi>σ</mi><
   mi>R</mi></msub><mo>+</mo><mi>ϵ</mi></mrow></mfrac></mrow><annotation
   encoding="application/x-tex">\hat{A}_{i}\leftarrow\frac{R_{i}-\mu_{R}}{
   \sigma_{R}+\epsilon}</annotation></semantics> :MATH]
   .
   21:end for
   22:if
   [MATH: <semantics><mrow><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub><mo>≠</mo><mi
   mathvariant="normal">∅</mi></mrow><annotation
   encoding="application/x-tex">\mathcal{S}_{succ}\neq\emptyset</annotatio
   n></semantics> :MATH]
   then
   23:  Select the shortest successful rollout:
   [MATH: <semantics><mrow><mrow><mo
   stretchy="false">(</mo><msubsup><mi>p</mi><mrow><mi>s</mi><mo
   lspace="0em" rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow><mo>∗</mo></msubsup><mo>,</mo><msub
   sup><mi>τ</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow><mo>∗</mo></msubsup><mo
   stretchy="false">)</mo></mrow><mo
   stretchy="false">←</mo><mrow><mrow><mi>arg</mi><mo
   lspace="0.167em">⁡</mo><mrow><msub><mi>min</mi><mrow><mrow><mo
   stretchy="false">(</mo><mi>p</mi><mo>,</mo><mi>τ</mi><mo
   stretchy="false">)</mo></mrow><mo>∈</mo><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub></mrow></msub><mo
   lspace="0.167em">⁡</mo><mtext>length</mtext></mrow></mrow><mo
   lspace="0em" rspace="0em">​</mo><mrow><mo
   stretchy="false">(</mo><mi>τ</mi><mo
   stretchy="false">)</mo></mrow></mrow></mrow><annotation
   encoding="application/x-tex">(p_{succ}^{*},\tau_{succ}^{*})\leftarrow\a
   rg\min_{(p,\tau)\in\mathcal{S}_{succ}}\text{length}(\tau)</annotation><
   /semantics> :MATH]
   .
   24:  Compress
   [MATH: <semantics><msubsup><mi>τ</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow><mo>∗</mo></msubsup><annotation
   encoding="application/x-tex">\tau_{succ}^{*}</annotation></semantics>
   :MATH]
   into a structured workflow summary
   [MATH: <semantics><msub><mi>m</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub><annotation
   encoding="application/x-tex">m_{succ}</annotation></semantics> :MATH]
   .
   25:  Store
   [MATH: <semantics><msub><mi>m</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub><annotation
   encoding="application/x-tex">m_{succ}</annotation></semantics> :MATH]
   in the non-parametric Workflow Memory.
   26:end if
   27:if
   [MATH: <semantics><mrow><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub><mo>≠</mo><mi
   mathvariant="normal">∅</mi></mrow><annotation
   encoding="application/x-tex">\mathcal{S}_{fail}\neq\emptyset</annotatio
   n></semantics> :MATH]
   then
   28:  Randomly sample one failed rollout
   [MATH: <semantics><mrow><mrow><mo
   stretchy="false">(</mo><msubsup><mi>p</mi><mrow><mi>f</mi><mo
   lspace="0em" rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow><mo>∗</mo></msubsup><mo>,</mo><msub
   sup><mi>τ</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow><mo>∗</mo></msubsup><mo
   stretchy="false">)</mo></mrow><mo>∼</mo><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub></mrow><annotation
   encoding="application/x-tex">(p_{fail}^{*},\tau_{fail}^{*})\sim\mathcal
   {S}_{fail}</annotation></semantics> :MATH]
   .
   29:  Compress
   [MATH: <semantics><msubsup><mi>τ</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow><mo>∗</mo></msubsup><annotation
   encoding="application/x-tex">\tau_{fail}^{*}</annotation></semantics>
   :MATH]
   into a structured workflow summary
   [MATH: <semantics><msub><mi>m</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub><annotation
   encoding="application/x-tex">m_{fail}</annotation></semantics> :MATH]
   .
   30:  Store
   [MATH: <semantics><msub><mi>m</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub><annotation
   encoding="application/x-tex">m_{fail}</annotation></semantics> :MATH]
   in the non-parametric Workflow Memory.
   31:end if
   32:if
   [MATH: <semantics><mrow><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>s</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow></msub><mo>≠</mo><mi
   mathvariant="normal">∅</mi></mrow><annotation
   encoding="application/x-tex">\mathcal{S}_{succ}\neq\emptyset</annotatio
   n></semantics> :MATH]
   and
   [MATH: <semantics><mrow><msub><mi
   class="ltx_font_mathcaligraphic">𝒮</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow></msub><mo>≠</mo><mi
   mathvariant="normal">∅</mi></mrow><annotation
   encoding="application/x-tex">\mathcal{S}_{fail}\neq\emptyset</annotatio
   n></semantics> :MATH]
   then
   33:  Store
   [MATH: <semantics><mrow><mo
   stretchy="false">(</mo><msubsup><mi>p</mi><mrow><mi>s</mi><mo
   lspace="0em" rspace="0em">​</mo><mi>u</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>c</mi></mrow><mo>∗</mo></msubsup><mo>,</mo><msub
   sup><mi>p</mi><mrow><mi>f</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>a</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>i</mi><mo lspace="0em"
   rspace="0em">​</mo><mi>l</mi></mrow><mo>∗</mo></msubsup><mo
   stretchy="false">)</mo></mrow><annotation
   encoding="application/x-tex">(p_{succ}^{*},p_{fail}^{*})</annotation></
   semantics> :MATH]
   as a contrastive pair in the Meta Plan Memory.
   34:end if
   35:Update Planner parameters according to Eq. (3.3.2).
   36:return
   [MATH: <semantics><mi>y</mi><annotation
   encoding="application/x-tex">y</annotation></semantics> :MATH]
   .

13 Prompt Template

   [Uncaptioned image] [Uncaptioned image] [Uncaptioned image]
   [Uncaptioned image]

   Experimental support, please view the build logs for errors. Generated
   by L A T E xml [LOGO] .
