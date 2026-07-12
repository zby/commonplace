---
source: https://arxiv.org/html/2604.17609v1
description: "Solution-injection benchmark paper showing agents often discover explicit task solutions but fail to exploit them."
captured: 2026-04-22
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity

Author: Leon Engländer; Sophia Althammer; Ahmet Üstün; Matthias Gallé; Tom Sherborne
Source: https://arxiv.org/html/2604.17609v1
Date: 19 Apr 2026

## Abstract

LLM-based agents are assumed to integrate environmental observations into their reasoning: discovering highly relevant but unexpected information should naturally lead to a model exploiting its own discoveries. We show that this assumption is false for current LLM-based agents, which struggle to reflect or react to unexpected information. Across three benchmarks (Terminal-Bench, SWE-Bench, AppWorld), we inject complete task solutions into the agent environments to deliberately expose a task’s solution to a model. While agents discover these solutions on Terminal-Bench in 79–81% of runs, they interact, or exploit, them in only 37-50% of cases. This gap is starkest in AppWorld: agents see documentation stating that a command “returns the complete solution to this task” in over 90% of attempts but exploit this in fewer than 7% of trials. We show that agents lack what we call environmental curiosity: the capability to recognize and investigate unexpected but relevant observations
in response to environmental stimuli. We identify three main factors influencing environmental curiosity: available tools in the agent scaffold, test-time compute, and training data distribution. Our findings identify configurations that maximize curiosity also achieve the best performance on the unmodified benchmarks. Yet even jointly optimized agents still ignore discovered solutions in the majority of trials: current agents use the environment to fetch expected information, but not to revise their strategy or maximally exploit useful stimuli.

## 1 Introduction

Contemporary LLM-based agents have made rapid progress on benchmarks simulating complex real-world tasks. On SWE-Bench Verified (Chowdhury et al., 2024), resolution rates climbed from 33.2% to 80+% through improved models and agent scaffolds like SWE-Agent (Yang et al., 2024) and OpenHands (Wang et al., 2025).

Agents begin each task without knowledge of the codebase they act in. To succeed, they must explore the environment to discover relevant information and integrate findings into their reasoning and future steps. During exploration, the agent may encounter unexpected but highly relevant information, such as code that already solves parts of the task. In those situations, an agent would benefit from environmental curiosity, which we define as the capability to recognize and investigate such observations in response to environmental stimuli. We show that current agents lack this useful exploration behavior: while agents regularly discover relevant but unexpected information, they fail to investigate and apply this information to solve the problem at hand, but rather ignore the information.

To evaluate environmental curiosity, we propose solution injection: we place the respective solution directly inside the environment, e.g., as a script, and measure (i) whether agents discover the solution and (ii) whether they interact with it, e.g., read the added solution file. Existing benchmarks primarily measure task success (often based on environment state), and thus cannot distinguish agents that adapt their behavior based on observations from those that execute fixed patterns learned during training. Through solution injection, we are able to quantify this distinction.
Refer to caption Figure 1: Agents discover but ignore injected solutions. This figure shows a trajectory from AppWorld with injected solution using gpt-oss-120b as the LLM. The agent executes cli --help and observes documentation explicitly stating that calling the solution API would display the solution for the current task. The agent proceeds without calling it. Current LLM-based agents lack environmental curiosity: while gpt-oss-120b discovers the documentation in 97.54% of runs, it calls the solution API in only 0.53% of cases.

We apply solution injection to three agentic benchmarks: Terminal-Bench (Merrill et al., 2026), SWE-Bench Verified (Chowdhury et al., 2024), and AppWorld (Trivedi et al., 2024) that span code and non-code domains, including terminal tasks, software engineering tasks, and everyday digital tasks performed via API calls. Our experiments show that across all three benchmarks, and two distinct agent scaffolds (SWE-agent, Yang et al., 2024; Terminus, Merrill et al., 2026), agents frequently discover injected solutions but rarely interact with them. This discovery-interaction gap is starkest in AppWorld: in 97.54% of attempts, gpt-oss-120b sees documentation explicitly stating that a command “returns the complete solution to this task”, yet calls this tool only 0.53% of the time, as illustrated in Figure 1.

We find three critical factors that strongly influence environmental curiosity at inference time: tool availability, reasoning budget, and exploration-oriented prompting. Adding tools beyond a basic bash shell strongly reduces interaction rates, as agents default to learned tool-specific patterns rather than examining their environment. Yet even with all those factors optimized, agents still ignore discovered solutions in the majority of trials, indicating that the deficit is not solely in inference-time configuration. We further investigate the role of training distribution and find that supervised fine-tuning on narrow, in-distribution data reduces environmental curiosity and the diversity of explored solution paths, degrading the benefit of increased performance from additional trials, seen in lower pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
for higher
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
.

Crucially, the prompts that most improve interaction rates also achieve the best performance on the original, unmodified benchmarks, and narrow in-distribution fine-tuning degrades pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
scaling on the original benchmarks as well. Optimizing for environmental curiosity consistently improves performance on the original benchmarks.

Our main contributions are:
  * •
    We define Environmental Curiosity and benchmark the (lack of) capacity of modern LLMs to leverage unexpected relevant information. This gap between discovery and interaction is consistent across three benchmarks, multiple LLMs, and agent scaffolds.
  * •
    We introduce Solution Injection as a method for adapting agent benchmarks to evaluate environmental curiosity. We propose two new metrics, discovery@
    [MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
    and interaction@
    [MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
    , to separately measure whether agents discover and act on relevant information.
  * •
    We investigate test-time factors influencing environmental curiosity. The most consistent effect comes from tool availability: restricting the agent scaffold to bash-only roughly doubles interaction rates. Increased reasoning budget and prompts instructing to explore also improve environmental curiosity. Yet even with all factors optimized, agents still ignore discovered solutions in the majority of runs.
  * •
    We find that fine-tuning on narrow in-distribution data reduces environmental curiosity and the diversity of explored solution paths, leading to worse pass@k scaling even on the original benchmarks.

## 2 Method

To evaluate environmental curiosity, i.e., the tendency to investigate relevant observations in response to environmental stimuli, we need to separately measure an agent’s ability to discover relevant information and whether it interacts with what it discovers. To achieve this, we propose injecting the task’s gold solution directly into the environment.

2.1 Solution Injection

The central idea is to add the task solution directly to the environment. This is conceptually applicable to any existing agent benchmark where a gold solution exists. The injected solution must be (i) complete so that following it guarantees task success and (ii) discoverable through agent actions.

This offers unexpected but highly relevant information. It is relevant because it contains the complete task solution, and unexpected because it lies outside the agent’s typical workflow. This allows us to measure whether the agent is environmentally curious enough to investigate it. The injected solutions are deliberately obvious. Agents that ignore information explicitly labeled as the solution are unlikely to integrate the subtler information present in real environments. We apply solution injection to Terminal-Bench, SWE-Bench, and AppWorld, injecting solutions as executable files or as documented API endpoints, depending on the benchmark^1^11For example, in Terminal-Bench and SWE-Bench, we add the solution as solution.sh to the agent’s working directory. In AppWorld, we add a solution API endpoint documented in the CLI help output.. To ensure our findings are not artifacts of a specific file name or format, we also experiment with different injection variants
(Appendix B.2, B.3).

2.2 Metrics

To measure performance and how often the agent discovers and exploits solution injection, we measure three metrics across
[MATH: <semantics><mi>n</mi><annotation encoding="application/x-tex">n</annotation></semantics> :MATH]
attempts per task. We use the pass@k definition from Chen et al. (2021) and introduce two new metrics for discovery and interaction using the same unbiased estimator to compute probabilities across
[MATH: <semantics><mi>n</mi><annotation encoding="application/x-tex">n</annotation></semantics> :MATH]
attempts:

pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
: The probability that at least one of
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
attempts successfully completes the task. With
[MATH: <semantics><msub><mi>c</mi><mtext>pass</mtext></msub><annotation encoding="application/x-tex">c_{\text{pass}}</annotation></semantics> :MATH]
being the number of attempts that pass the task:
[MATH: <semantics><mrow><mrow><mtext>pass@</mtext><mo lspace="0em" rspace="0em">​</mo><mi>k</mi></mrow><mo>:=</mo><mrow><munder accentunder="true"><mi>𝔼</mi><mtext mathsize="0.700em">Tasks</mtext></munder><mo lspace="0em" rspace="0em">​</mo><mrow><mo>[</mo><mrow><mn>1</mn><mo>−</mo><mfrac><mrow><mo>(</mo><mfrac linethickness="0pt"><mrow><mi>n</mi><mo>−</mo><msub><mi>c</mi><mtext mathsize="1.400em">pass</mtext></msub></mrow><mi>k</mi></mfrac><mo>)</mo></mrow><mrow><mo>(</mo><mfrac linethickness="0pt"><mi>n</mi><mi>k</mi></mfrac><mo>)</mo></mrow></mfrac></mrow><mo>]</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">\text{pass@}k:=\underset{\text{Tasks}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c_{\text{pass}}}{k}}{\binom{n}{k}}\right]</annotation></semantics> :MATH]
(1)

discovery@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
: The probability that at least one of
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
attempts executes a command that surfaces the injected solution in the agent’s context. This metric serves as a sanity check that the injected solution is indeed discoverable through the normal agent’s actions. With
[MATH: <semantics><msub><mi>c</mi><mtext>disc</mtext></msub><annotation encoding="application/x-tex">c_{\text{disc}}</annotation></semantics> :MATH]
being the number of attempts in which the solution was discovered:
[MATH: <semantics><mrow><mrow><mtext>discovery@</mtext><mo lspace="0em" rspace="0em">​</mo><mi>k</mi></mrow><mo>:=</mo><mrow><munder accentunder="true"><mi>𝔼</mi><mtext mathsize="0.700em">Tasks</mtext></munder><mo lspace="0em" rspace="0em">​</mo><mrow><mo>[</mo><mrow><mn>1</mn><mo>−</mo><mfrac><mrow><mo>(</mo><mfrac linethickness="0pt"><mrow><mi>n</mi><mo>−</mo><msub><mi>c</mi><mtext mathsize="1.400em">disc</mtext></msub></mrow><mi>k</mi></mfrac><mo>)</mo></mrow><mrow><mo>(</mo><mfrac linethickness="0pt"><mi>n</mi><mi>k</mi></mfrac><mo>)</mo></mrow></mfrac></mrow><mo>]</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">\text{discovery@}k:=\underset{\text{Tasks}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c_{\text{disc}}}{k}}{\binom{n}{k}}\right]</annotation></semantics> :MATH]
(2)

interaction@k: The probability that, across
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
attempts, the agent interacts with the injected solution at least once, such as reading or executing the solution file or querying the solution API.^2^22We detect interaction by checking whether any command executed by the agent references the injected solution, e.g. contains “solution.sh” or “cli solution”. This metric measures environmental curiosity: a high interaction rate would mean that the agent investigated the unexpected but highly relevant information it discovered. A low interaction rate would mean that it ignored it. With
[MATH: <semantics><msub><mi>c</mi><mtext>interact</mtext></msub><annotation encoding="application/x-tex">c_{\text{interact}}</annotation></semantics> :MATH]
being the number of attempts in which the agent interacted with the solution, we define
[MATH: <semantics><mrow><mtext>interaction@</mtext><mo lspace="0em" rspace="0em">​</mo><mi>k</mi></mrow><annotation encoding="application/x-tex">\text{interaction@}k</annotation></semantics> :MATH]
as:
[MATH: <semantics><mrow><mrow><mtext>interaction@</mtext><mo lspace="0em" rspace="0em">​</mo><mi>k</mi></mrow><mo>:=</mo><mrow><munder accentunder="true"><mi>𝔼</mi><mtext mathsize="0.700em">Tasks</mtext></munder><mo lspace="0em" rspace="0em">​</mo><mrow><mo>[</mo><mrow><mn>1</mn><mo>−</mo><mfrac><mrow><mo>(</mo><mfrac linethickness="0pt"><mrow><mi>n</mi><mo>−</mo><msub><mi>c</mi><mtext mathsize="1.400em">interact</mtext></msub></mrow><mi>k</mi></mfrac><mo>)</mo></mrow><mrow><mo>(</mo><mfrac linethickness="0pt"><mi>n</mi><mi>k</mi></mfrac><mo>)</mo></mrow></mfrac></mrow><mo>]</mo></mrow></mrow></mrow><annotation encoding="application/x-tex">\text{interaction@}k:=\underset{\text{Tasks}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c_{\text{interact}}}{k}}{\binom{n}{k}}\right]</annotation></semantics> :MATH]
(3)

## 3 Experiments

We evaluate the environmental curiosity of agents and investigate which factors influence environmental curiosity. We structure our investigation around three hypotheses: (H1) LLM-based agents lack environmental curiosity: they discover relevant information during exploration but systematically fail to act on it. (H2) Test-time design decisions shape environmental curiosity. (H3) Narrow fine-tuning suppresses environmental curiosity.

Benchmarks.

We apply solution injection to three benchmarks: Terminal-Bench v1 (Merrill et al., 2026), SWE-Bench Verified (Chowdhury et al., 2024), and AppWorld (Trivedi et al., 2024). Terminal-Bench spans a wide variety of terminal-based tasks, including file manipulation, system administration, and data processing. SWE-Bench Verified evaluates agents on resolving real GitHub issues by editing repository code. AppWorld requires agents to complete everyday digital tasks, such as managing emails, notes, and calendars, by interacting with simulated apps via API calls. For Terminal-Bench and SWE-Bench Verified, we inject the solution as an executable solution.sh in the agent’s working directory. For AppWorld, we add a solution API endpoint documented in the “cli --help”, as shown in Figure 1. We also report on AppWorld’s validation split, rather than test split, as we require gold solutions for solution injection, which only exist for the validation split.

Agent implementation.

The agent setup involves three layers: the harness, scaffold, and tools. The harness handles the execution environment, i.e., initializes the Docker execution environment and controls evaluating submitted solutions. The scaffold is the agent loop (i.e., ReACT loop from Yao et al. (2023)), including prompting, tool-call parsing, and history management. The tools determine how the agent may interact with its environment. We evaluate two scaffolds: Terminus 1 (Merrill et al., 2026), which is the default Terminal-Bench agent, and SWE-agent (Yang et al., 2024). We adapt these scaffolds to use native function-calling APIs over raw prompting to remove the potential variable of out-of-distribution function calling interfaces (introduced in proprietary scaffolds) to instead rely on a provider’s native tool-use interface.

We evaluate two tool suites: bash-only, and bash and str_replace_editor. The str_replace_editor is a structured file-editing tool introduced by Anthropic (Anthropic, 2024)^3^33https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool that has become the standard editing tool in coding agent scaffolds (Yang et al., 2024; Wang et al., 2025). This is one of only three tools in SWE-agent’s default configuration, alongside bash and a submit tool.^4^44For SWE-agent, “bash-only” refers to bash plus the submit tool, i.e. without str_replace_editor.

Evaluation setup.

We evaluate three LLMs: gpt-oss-120b (OpenAI, 2025) with high reasoning, GLM-4.7 (GLM, 2025), and fine-tuned variants of command-a-reasoning (Cohere et al., 2025; Cohere, 2025) trained on different task distributions, as described in Section 3.3. Unless otherwise specified, we use the Terminal-Bench harness and the Terminus agent with bash as the only tool. We evaluate with
[MATH: <semantics><mrow><mi>n</mi><mo>=</mo><mn>10</mn></mrow><annotation encoding="application/x-tex">n=10</annotation></semantics> :MATH]
attempts per task and report discovery@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
and interaction@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
(Equations 2 and 3) alongside pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
for all experiments.
Refer to caption Figure 2: discovery@1 versus interaction@1 across benchmarks. We evaluate gpt-oss-120b with high reasoning (gpt-oss), GLM-4.7, and Command A Reasoning fine-tuned for Terminal-Bench (cmd-a). Agents consistently discover solutions but rarely interact with them.

3.1 Agents lack environmental curiosity

Figure 2 shows the discovery and interaction rates across all three benchmarks. Across all models and benchmarks, agents consistently discover the injected solutions but rarely interact with them. On Terminal-Bench, discovery@1 ranges from 78.6–81.2% while interaction@1 reaches only 37.1–50.3%. On SWE-Bench, agents discover solutions in 53.4–98.2% of runs but interact in only 5.9–17.4%. The gap is starkest on AppWorld: discovery@1 exceeds 90% for all models, yet interaction@1 never surpasses 6.3%. The bottleneck for current agents is not discovering relevant information but integrating observations into their reasoning. We show an example trajectory in Figure 1.
  Benchmark    Original w/ Solution
[MATH: <semantics><mi mathvariant="normal">Δ</mi><annotation encoding="application/x-tex">\Delta</annotation></semantics> :MATH]
Terminal-Bench 44.5     55.9        +11.4
   AppWorld    40.5     43.1        +2.6
  SWE-Bench    45.9     46.9        +1.0
Table 1: Task performance of gpt-oss-120b (high reasoning) on original and solution-injected benchmarks. Improvements correlate with the interaction rate in Figure 2.

Table 1 shows the performance on the original and solution-injected benchmarks for gpt-oss-120b. On the original benchmarks, the model achieves 40-46% pass@1, which confirms that these are challenging tasks. Injecting solutions improves performance, with the largest gain on Terminal-Bench (+11.4) where interaction is highest. On AppWorld, where agents almost never call the solution API, the gain is minimal (+2.6). This observation holds across all models; full results in Appendix B.1.

3.2 Test-time factors

We next investigate why agents fail to use what they discover. We begin with examining how test-time design decisions shape environmental curiosity (H2) by investigating three factors: agent scaffolding, test-time compute, and prompting.

Agent scaffolding.

We compare Terminus and SWE-agent scaffolds to ensure our findings are not artifacts of any specific agent implementation. This comparison additionally investigates how available tools shape environmental curiosity by evaluating two tool configurations: bash-only, and bash with str_replace_editor. We evaluate gpt-oss-120b and a fine-tuned variant of command-a-reasoning trained on bash-only trajectories from SWE-smith (SWE-Bench-SFT; described in Section 3.3). All experiments are conducted on SWE-Bench Verified; for scaffold implementation details, see Appendix E. Figure 3 shows that scaffold choice substantially affects both task performance and environmental curiosity (e.g., SWE-Bench-SFT with bash-only achieves
[MATH: <semantics><mn>46.9</mn><annotation encoding="application/x-tex">46.9</annotation></semantics> :MATH]
pass@1 with Terminus but
[MATH: <semantics><mn>25.2</mn><annotation encoding="application/x-tex">25.2</annotation></semantics> :MATH]
with SWE-agent), but both scaffolds consistently exhibit the discovery-interaction gap.

The available tools substantially affect environmental curiosity. Adding str_replace_editor improves pass@1 across all configurations but reduces interaction, conditional upon discovery, in every case. The same pass@1 improvement appears on the original, unmodified SWE-Bench Verified, confirming that the performance gains from richer toolsets are not artifacts of solution injection. Notably, SWE-Bench-SFT has never encountered str_replace_editor during fine-tuning, yet providing it at test time still relatively reduces interaction given discovery by 13.7% to 48.3%, suggesting that the tool-use patterns that reduce exploration originate from pre-training. Among trajectories where agents do interact with the solution, the median interaction step is similar with (step 18) and without (step 15) the editor. Both medians fall within the first 25% of the trajectory, indicating that the tool does not delay interaction but suppresses it. We conjecture that when a dedicated editing tool
is available, agents default to applying it directly rather than first examining their environment; we discuss this further in Section 4.
Refer to caption Figure 3: Adding tools improves task performance but reduces environmental curiosity. We evaluate gpt-oss-120b and cmd-a (SWE-Bench SFT) across two scaffolds (Terminus, SWE-agent) on SWE-Bench Verified. Adding str_replace_editor increases pass@
[MATH: <semantics><mn>1</mn><annotation encoding="application/x-tex">1</annotation></semantics> :MATH]
for the solution injected as well as the original (faint lines) benchmark, but consistently decreases the probability of interacting with discovered solutions. The discovery@1 exceeds 87.9% across all configurations, i.e., the conditional metric is not driven by varying discovery rates.

Effect of reasoning effort.

Refer to caption Figure 4: gpt-oss-120b with different reasoning budgets on Terminal-Bench.

To additionally measure the effect of reasoning levels, we evaluate gpt-oss-120b with low, medium and high reasoning on all benchmarks. We observe that increased reasoning substantially improves environmental curiosity: Terminal-Bench interaction@1 more than triples from 11% to 37%, as shown in figure 4. This is not an artifact of higher discovery rates: The conditional probability of interaction given discovery increases from 17.65% (low) to 36.68% (medium) to 45.69% (high). On SWE-Bench, interaction@1 increases from 0.78% to 17.42% when increasing reasoning. On AppWorld, interaction remains near zero across all reasoning levels, indicating that increased compute alone cannot overcome the gap for all task types.

Prompting.

We test whether explicit instructions improve environmental curiosity. Prompting the agent to explore its environment before acting improves task performance across all three benchmarks by on average +2.57% on the original benchmarks and +2.96% on the solution-injected versions, as shown in Appendix B.4. On Terminal-Bench, we further evaluate prompts encouraging reflection and adapting to environmental observations (Appendix B.4.1). Less directive prompts to encourage curiosity and step-wise reflection yield diminishing returns. Requiring agents to investigate all discovered files before proceeding achieves the highest interaction and pass rates on the solution injected benchmark. Notably, the best-performing prompt on the solution-injected benchmark is also the best-performing prompt on the original Terminal-Bench, suggesting that improved environmental curiosity benefits general task performance.

Summary.

All three test-time factors improve interaction rates as proposed by Hypothesis (H2). Tool availability shapes how agents approach their environment: with fewer tools, agents must examine files to understand the environment; with more tools, they default to learned tool-specific patterns and skip investigation or curiosity. Test-time compute and prompt design support agents to identify and act on unexpected but highly relevant information. Yet even with optimal settings, i.e., bash-only, high reasoning, and explicit instructions to investigate, agents still ignore solutions in the majority of trials. This suggests the limitation is not solely a matter of inference-time configuration, but is inherent to how LLMs are trained. Given this finding, we now examine the influence of training data distribution on how agents exhibit curiosity-driven behavior.

3.3 Effect of training distribution

The previous section identified that optimizing test-time factors does not resolve the gap between discovery and interaction, suggesting that the limited environmental curiosity stems from the training phase. To investigate this, we fine-tune command-a-reasoning via rejection sampling (Guo et al., 2025) on three task distributions: Terminal-Bench-like tasks from an external vendor (T-Bench-SFT), the AppWorld training split (AppWorld-SFT), and SWE-smith (SWE-Bench-SFT). All models are trained on approximately 20,000 turns; further details are provided in Appendix C. We use these models to analyze how training breadth and domain transfer affect environmental curiosity.

Narrow in-distribution training reduces solution diversity.

AppWorld’s task distribution is a narrow subset of Terminal-Bench’s distribution (Appendix D), so comparing T-Bench-SFT and AppWorld-SFT isolates the effect of training distribution breadth. Table 2 shows that on AppWorld, AppWorld-SFT achieves higher pass@1 (
[MATH: <semantics><mn>44.2</mn><annotation encoding="application/x-tex">44.2</annotation></semantics> :MATH]
vs.
[MATH: <semantics><mn>34.5</mn><annotation encoding="application/x-tex">34.5</annotation></semantics> :MATH]
) but is surpassed by T-Bench-SFT at higher
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
(
[MATH: <semantics><mn>65.8</mn><annotation encoding="application/x-tex">65.8</annotation></semantics> :MATH]
vs.
[MATH: <semantics><mn>69.0</mn><annotation encoding="application/x-tex">69.0</annotation></semantics> :MATH]
at pass@10), suggesting that narrow in-domain training compresses the explored solution space. Interaction@10 shows the same gap (
[MATH: <semantics><mn>29.8</mn><annotation encoding="application/x-tex">29.8</annotation></semantics> :MATH]
vs.
[MATH: <semantics><mn>41.5</mn><annotation encoding="application/x-tex">41.5</annotation></semantics> :MATH]
). On Terminal-Bench, where AppWorld-SFT is out-of-distribution, T-Bench-SFT achieves higher pass and interaction rates. The same patterns appear on the original, unmodified benchmarks (Figure 5): T-Bench-SFT surpasses AppWorld-SFT at higher
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
on AppWorld and achieves consistently higher pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
on Terminal-Bench, indicating that when the evaluation domain is a subset of a broader training distribution, the broader-trained model has lower pass@1 but better pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
scaling, i.e., explores a wider solution space.

Curiosity does not transfer across domains.

To test whether environmental curiosity generalizes beyond the training distribution, we compare T-Bench-SFT and SWE-Bench-SFT, which cover structurally distinct task types. Table 3 shows that on each benchmark, the respective in-domain model achieves consistently higher pass and interaction rates. Together, these results show that environmental curiosity can benefit from in-domain training data in some scenarios, but a narrow in-domain distribution reduces or degrades this benefit.
Refer to caption
Refer to caption
Figure 5: Training distribution affects pass@
[MATH: <semantics><mi>n</mi><annotation encoding="application/x-tex">n</annotation></semantics> :MATH]
scaling on the original, i.e. unmodified, benchmarks. Left: On AppWorld, the narrow in-distribution model (AppWorld-SFT) achieves higher pass@1 but is surpassed by the broader-trained model (T-Bench-SFT) at higher
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
, indicating that narrow training compresses the explored solution space. Right: On Terminal-Bench, the broader-trained model outperforms across all
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
. Results averaged over 3 fine-tuned models with different seeds.
      Eval Benchmark       Training Data discovery@1 discovery@10 interaction@1 interaction@10 pass@1 pass@10
Terminal-Bench w/ Solution  T-Bench-SFT  79.7        99.17        50.3          92.9           45.1   83.3
                           AppWorld-SFT  65.6        95.63        40.8          81.7           44.6   80.0
   AppWorld w/ Solution     T-Bench-SFT  90.8        100.0        6.3           41.5           34.5   69.0
                           AppWorld-SFT  98.4        100.0        3.7           26.9           44.2   65.8
Table 2: Effect of training distribution on environmental curiosity and task performance. All models are fine-tuned from command-a-reasoning. Narrow in-distribution training (AppWorld-SFT) yields higher pass@1 on AppWorld but lower interaction rates and worse pass@10 scaling. Results averaged over 3 seeds.
      Eval Benchmark       Training Data discovery@1 discovery@10 interaction@1 interaction@10 pass@1 pass@10
Terminal-Bench w/ Solution  T-Bench-SFT  79.66       95           50.3          92.9           45.1   83.3
                           SWE-Bench-SFT 72.88       97.5         47.50         86.25          44.88  77.38
  SWE-Bench w/ Solution     T-Bench-SFT  93.92       100.00       14.76         65             42.20  79.00
                           SWE-Bench-SFT 93.04       99.40        21.48         71.6           42.72  84.00
Table 3: Cross-domain comparison of T-Bench-SFT and SWE-Bench-SFT, both fine-tuned from command-a-reasoning. On each benchmark, the respective in-domain model achieves higher interaction rates and better pass@10 scaling. Results on SWE-Bench from a single seed.

## 4 Discussion

Our results confirm all three hypotheses: agents consistently discover but fail to act on injected solutions (H1), test-time factors modulate but cannot close this gap (H2), and fine-tuning on narrow in-distribution data further suppresses environmental curiosity (H3).

This raises a key question: do current models already possess environmental curiosity that scaffolding or later-stage alignment fails to elicit, or does training never produce environmental curiosity in the first place? Our evidence suggests that both factors play a role. Optimizing test-time factors improves environmental curiosity (Section 3.2), indicating that training does produce latent capability that scaffolding can amplify. However, even with all investigated factors jointly optimized, agents ignore discovered solutions in the majority of runs. LLM-as-a-judge analysis of reasoning traces confirms that in attempts where the solution is discovered but not interacted with, the agent’s reasoning does not mention the discovered solution at all; the agent proceeds as if the observation never occurred (Appendix A.1). Yet when the solution is injected directly in the user prompt or the agent’s first reasoning step, agents incorporate it into their plan and solve the task at
substantially higher rates (Appendix A.2), which shows that they do have the capability to use the information, but they habitually decide to ignore it.

Currently, the agent loop is:
[MATH: <semantics><mrow><mtext>Action</mtext><mo stretchy="false">→</mo><mtext>Observation</mtext><mo stretchy="false">→</mo><mtext>Reasoning</mtext><mo stretchy="false">→</mo><mtext>Next Action</mtext></mrow><annotation encoding="application/x-tex">\text{Action}\rightarrow\text{Observation}\rightarrow\text{Reasoning}\rightarrow\text{Next Action}</annotation></semantics> :MATH]
(4)

Whereas environmental curiosity requires reflecting on whether observations fit the agent’s current model of the environment, i.e., whether anything unexpected is observed:
[MATH: <semantics><mrow><mtext>Action</mtext><mo stretchy="false">→</mo><mtext>Observation</mtext><mo stretchy="false">→</mo><mrow><mtext>Reasoning </mtext><mtext class="ltx_mathvariant_italic">and reflecting on observations</mtext></mrow><mo stretchy="false">→</mo><mtext>Next Action</mtext></mrow><annotation encoding="application/x-tex">\text{Action}\rightarrow\text{Observation}\rightarrow\text{Reasoning {and reflecting on observations}}\rightarrow\text{Next Action}</annotation></semantics> :MATH]
(5)

We hypothesize that training agents on specific environments reinforces Equation 4 because supervised fine-tuning relies on expert on-policy trajectories in which tool outputs consistently align with the agent’s implicit plan, and, in reinforcement learning, those biases regarding tool outputs are increased. The environment never contradicts the expert, so the model learns to seek specific information and act on what it sought, rather than to notice and act on information it was not looking for. We attempted three SFT setups in order to get the agent to use the relevant information: (1) rejection sampling for curious first turns, (2) mid-trajectory file removal and re-addition to simulate dynamic environments, and (3) injecting masked adversarial turns forcing state recovery. None improved interaction rates, demonstrating that training for environmental curiosity is not straightforward. This raises a deeper open question: does post-training suppress the environmental curiosity
that pre-training may produce, or does it never emerge? Developing methods to measure environmental curiosity in base models is an open challenge, since base models cannot operate as agents, and environmental curiosity can only be observed through agentic behavior.

Environmental curiosity is a prerequisite for agents that operate in novel, open-ended environments. Agents that succeed only by executing memorized patterns are fundamentally brittle: they will fail whenever the environment deviates from the training distribution in ways that require adaptation. Outcome-driven metrics like pass@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
reward agents executing Equation 4 as effectively as agents executing Equation 5, as they cannot distinguish adaptive reasoning from rigid plan execution. Process-oriented metrics like interaction@k, which assess whether agents ground their reasoning in what they observe, are a necessary complement to task success. Solution injection and measuring interaction@k are a first step, but richer methods for measuring environmental curiosity are needed.

We see three directions for future work: (i) developing diverse benchmarks and metrics to measure environmental curiosity beyond solution injection, (ii) training paradigms teaching the reflective behavior in Equation 5, and (iii) scaffold designs to trigger reflection on observations.

## 5 Related work

LLM-Based Agents.

LLM-based agents interleave reasoning with action execution in a single trajectory, as proposed by ReAct (Yao et al., 2023). While ReAct parsed structured actions directly from text output, state-of-the-art agents use native function-calling APIs. For tasks in terminal environments, scaffolds vary widely: Terminus (Merrill et al., 2026) provides only a bash tool, SWE-agent (Yang et al., 2024) adds a curated set of file editing and a few optional tools, and OpenHands (Wang et al., 2025) offers a broad toolkit of over fifty tools. LLMs are trained to use these tools through supervised fine-tuning and reinforcement learning (OpenAI, 2025; GLM, 2025). Augmenting a bash shell with increasingly rich tool sets has been shown to improve task performance. However, tools have not yet been evaluated for how they shape an agent’s behavior with respect to environmental interaction.

Benchmarks.

A growing number of benchmarks evaluate LLM-based agents across diverse domains: SWE-Bench Verified (Chowdhury et al., 2024) and Terminal-Bench (Merrill et al., 2026) evaluate software engineering tasks, AppWorld (Trivedi et al., 2024) considers everyday digital tasks, DiscoveryWorld (Jansen et al., 2024) targets scientific discovery, and
[MATH: <semantics><msup><mi>τ</mi><mn>2</mn></msup><annotation encoding="application/x-tex">\tau^{2}</annotation></semantics> :MATH]
-bench (Barres et al., 2025) evaluate assistant tasks with user coordination. These benchmarks all measure end-to-end task success, i.e., whether the agent completes the task, but starkly not how an agent arrives at its solution. These benchmarks cannot distinguish agents that adapt to observations from those that execute fixed patterns, which is the gap our solution injection method addresses.

Agentic Exploration.

Recent work on agentic exploration in terminal environments relies on agents executing standard shell commands or using supplementary search tools to discover relevant information (Yang et al., 2024; Wang et al., 2025), or bypasses open-ended exploration entirely via predefined localization pipelines (Xia et al., 2025). Curiosity in reinforcement learning (Schmidhuber, 2020; Pathak et al., 2017) formalizes intrinsic rewards to drive the discovery of novel states. Both lines of work address the discovery of relevant information, but our findings show that discovery is not the bottleneck: LLM-based agents consistently find relevant unexpected information but ignore it.

## 6 Conclusion

We introduced solution injection to evaluate environmental curiosity in LLM-based agents, revealing a fundamental disconnect between what agents observe and how they act. Across diverse domains, state-of-the-art agents consistently discover unexpected, highly relevant information yet systematically ignore it. Test-time factors such as tool availability, reasoning budget, and prompting modulate this gap, and the configurations that most improve curiosity also yield the best task performance on the original benchmarks. Yet even jointly optimized, these factors cannot close the gap. Narrow in-distribution fine-tuning further reduces environmental curiosity. Current agents operate as open-loop sequence generators: they use the environment to fetch expected information, not to revise their strategy. However, progress requires training models that treat observations as potential reasons to change their plan, rather than as confirmation of it.

## Acknowledgments

We thank Minjie Xu for providing the codebase on which we built our evaluation and fine-tuning experiments, as well as the data used to train the T-Bench-SFT model.

## References

  * Anthropic (2024) Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku. Note: Blog post External Links: Link Cited by: §3.
  * V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan (2025)
    [MATH: <semantics><msup><mi>τ</mi><mn>2</mn></msup><annotation encoding="application/x-tex">\tau^{2}</annotation></semantics> :MATH]
    -Bench: evaluating conversational agents in a dual-control environment. External Links: 2506.07982, Link Cited by: §5.
  * M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba (2021) Evaluating large language models trained on code. CoRR abs/2107.03374. External Links: Link, 2107.03374 Cited by: §2.2.
  * N. Chowdhury, J. Aung, C. J. Shern, O. Jaffe, D. Sherburn, G. Starace, E. Mays, R. Dias, M. Aljubeh, M. Glaese, C. E. Jimenez, J. Yang, L. Ho, T. Patwardhan, K. Liu, and A. Madry (2024) Introducing SWE-bench verified. Note: https://openai.com/index/introducing-swe-bench-verified/Accessed: 2025-12-28 Cited by: §1, §1, §3, §5.
  * T. Cohere, A. Ahmadian, M. Ahmed, J. Alammar, M. Alizadeh, Y. Alnumay, S. Althammer, A. Arkhangorodsky, V. Aryabumi, D. Aumiller, et al. (2025) Command a: an enterprise-ready large language model. arXiv preprint arXiv:2504.00698. Cited by: Appendix C, §3.
  * T. Cohere (2025) Note: Blog post External Links: Link Cited by: Appendix C, §3.
  * GLM (2025) GLM-4.5: agentic, reasoning, and coding (ARC) foundation models. CoRR abs/2508.06471. External Links: Link, Document, 2508.06471 Cited by: §3, §5.
  * D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Xu, H. Ding, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Chen, J. Yuan, J. Tu, J. Qiu, J. Li, J. L. Cai, J. Ni, J. Liang, J. Chen, K. Dong, K. Hu, K. You, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Zhou, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W. An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X.
    Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y. Tang, Y. Zha, Y. Yan, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Xu, Z. Xie, Z. Zhang, Z. Hao, Z. Ma, Z. Yan, Z. Wu, Z. Gu, Z. Zhu, Z. Liu, Z. Li, Z. Xie, Z. Song, Z. Pan, Z. Huang, Z. Xu, Z. Zhang, and Z. Zhang (2025) DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning. Nat. 645 (8081), pp. 633–638. External Links: Link, Document Cited by: §3.3.
  * P. A. Jansen, M. Côté, T. Khot, E. Bransom, B. D. Mishra, B. P. Majumder, O. Tafjord, and P. Clark (2024) DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents. In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.), External Links: Link Cited by: §5.
  * M. A. Merrill, A. G. Shaw, N. Carlini, B. Li, H. Raj, I. Bercovich, L. Shi, J. Y. Shin, T. Walshe, E. K. Buchanan, J. Shen, G. Ye, H. Lin, J. Poulos, M. Wang, M. Nezhurina, J. Jitsev, D. Lu, O. M. Mastromichalakis, Z. Xu, Z. Chen, Y. Liu, R. Zhang, L. L. Chen, A. Kashyap, J. Uslu, J. Li, J. Wu, M. Yan, S. Bian, V. Sharma, K. Sun, S. Dillmann, A. Anand, A. Lanpouthakoun, B. Koopah, C. Hu, E. Guha, G. H. S. Dreiman, J. Zhu, K. Krauth, L. Zhong, N. Muennighoff, R. Amanfu, S. Tan, S. Pimpalgaonkar, T. Aggarwal, X. Lin, X. Lan, X. Zhao, Y. Liang, Y. Wang, Z. Wang, C. Zhou, D. Heineman, H. Liu, H. Trivedi, J. Yang, J. Lin, M. Shetty, M. Yang, N. Omi, N. Raoof, S. Li, T. Y. Zhuo, W. Lin, Y. Dai, Y. Wang, W. Chai, S. Zhou, D. Wahdany, Z. She, J. Hu, Z. Dong, Y. Zhu, S. Cui, A. Saiyed, A. Kolbeinsson, J. Hu, C. M. Rytting, R. Marten, Y. Wang, A. Dimakis, A. Konwinski, and L. Schmidt (2026) Terminal-bench: benchmarking agents on hard, realistic tasks in command line interfaces.
    External Links: 2601.11868, Link Cited by: Appendix E, §1, §3, §3, §5, §5.
  * OpenAI (2025) Gpt-oss-120b & gpt-oss-20b model card. CoRR abs/2508.10925. External Links: Link, Document, 2508.10925 Cited by: §3, §5.
  * D. Pathak, P. Agrawal, A. A. Efros, and T. Darrell (2017) Curiosity-driven exploration by self-supervised prediction. In Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017, D. Precup and Y. W. Teh (Eds.), Proceedings of Machine Learning Research, Vol. 70, pp. 2778–2787. External Links: Link Cited by: §5.
  * J. Schmidhuber (2020) Generative adversarial networks are special cases of artificial curiosity (1990) and also closely related to predictability minimization (1991). Neural Networks 127, pp. 58–66. External Links: Link, Document Cited by: §5.
  * H. Trivedi, T. Khot, M. Hartmann, R. Manku, V. Dong, E. Li, S. Gupta, A. Sabharwal, and N. Balasubramanian (2024) AppWorld: A controllable world of apps and people for benchmarking interactive coding agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, L. Ku, A. Martins, and V. Srikumar (Eds.), pp. 16022–16076. External Links: Link, Document Cited by: §1, §3, §5.
  * X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, H. H. Tran, F. Li, R. Ma, M. Zheng, B. Qian, Y. Shao, N. Muennighoff, Y. Zhang, B. Hui, J. Lin, and et al. (2025) OpenHands: an open platform for AI software developers as generalist agents. In The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025, External Links: Link Cited by: §1, §3, §5, §5.
  * C. S. Xia, Y. Deng, S. Dunn, and L. Zhang (2025) Demystifying llm-based software engineering agents. Proc. ACM Softw. Eng. 2 (FSE), pp. 801–824. External Links: Link, Document Cited by: §5.
  * J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024) SWE-agent: agent-computer interfaces enable automated software engineering. In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.), External Links: Link Cited by: §B.4, Figure 12, Appendix E, §1, §1, §3, §3, §5, §5.
  * S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and Y. Cao (2023) ReAct: synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023, External Links: Link Cited by: §3, §5.

Appendix A Ruling Out Alternative Explanations

In addition to the hypothesis investigated in the main part of the paper, one could also suspect that the models lack the capability to comprehend the injected solution or suspect it is an adversarial trap. To rule out these hypotheses, we use an LLM-as-a-judge to show that the models do not see the solution as a trap, but instead simply ignore it. Additionally, we conduct an oracle case study on Terminal-Bench to show that the models do have the general capability to use the information; they just lack the innate trigger to investigate it.

### A.1 LLM-as-a-Judge analysis: agents ignore rather than reject discovered solutions

An alternative explanation for low interaction rates could be that agents recognize the injected solution but deliberately avoid it, e.g., because they suspect it is adversarial or a trap. That the interaction rates increase with reasoning budget points against this theory, as deliberate avoidance would not lead to more interaction with more reasoning. To directly test this, we use an LLM-as-a-judge to classify agent behavior in attempts where the solution was discovered but not interacted with.

Method.

For each such attempt, we identify all turns in which the solution was discovered, i.e., not only the first occurrence, as agents may re-encounter the solution file or API in later terminal outputs (e.g., by running ls again). For each discovery turn, we add in the prompt in which turn the solution appeared, followed by the agent’s reasoning and actions for the three subsequent turns. This keeps the judge’s input focused on the agent’s immediate reaction to each discovery event while remaining concise enough for reliable classification. The judge classifies each trajectory into exactly one of five categories:
 1. 1.
    No acknowledgment. The agent’s reasoning never mentions the solution after seeing it. The agent proceeds as if the observation did not occur.
 2. 2.
    Acknowledgment without investigation. The agent’s reasoning mentions the solution (e.g., the word “solution” appears) but makes no plan to interact with it.
 3. 3.
    Deliberate rejection (suspicion/trap). The agent explicitly reasons that the solution might be untrustworthy or adversarial and decides to avoid it.
 4. 4.
    Deliberate rejection (preference for own approach). The agent acknowledges the solution but explicitly states it prefers to solve the task independently.
 5. 5.
    Interaction planned but not executed. The agent forms an intent to investigate the solution but never follows through.

Categories 1–2 represent passive non-interaction; category 3 is the active rejection that would undermine our environmental curiosity interpretation. We use GLM-4.7 as the judge with a structured tool call containing a classification field and an evidence field for a supporting quote from the trace. We use separate system prompts for Terminal-Bench/SWE-Bench (solution files) and AppWorld (solution API command) so the judge receives benchmark-appropriate context. We manually verified 50 random classifications and found the extracted evidence to be correct in all cases. The full judge prompts are provided in Figure 6.

Results.

Table 4 shows the classification results for gpt-oss-120b and GLM-4.7 across all benchmarks. Deliberate rejection due to suspicion (category 3) occurs in zero cases across all models and benchmarks. The overwhelming majority of non-interactions fall into categories 1 and 2: agents either never mention the solution in their reasoning or briefly acknowledge it before continuing with their original plan (Figure 7). On SWE-Bench, no-acknowledgment rates exceed 96% for both models, indicating that agents process the terminal output containing the solution without it entering their reasoning at all. Category 5 is rare (
[MATH: <semantics><mo>≤</mo><annotation encoding="application/x-tex">\leq</annotation></semantics> :MATH]
3.1%), suggesting that the deficit is not in forming intent but in noticing relevance in the first place. These results confirm that agents do not perceive the solution as a trap; they simply do not register it as relevant.
                                Passive non-interaction          Deliberate rejection
   Model       Benchmark    (1) No ack. (2) Ack., no action (3) Suspect trap (4) Prefer own (5) Planned, not exec.
gpt-oss-120b Terminal-Bench 50.0        44.6                0.0              4.9            0.6
                AppWorld    78.3        21.0                0.0              0.7            0.0
               SWE-Bench    96.8        0.8                 0.0              2.4            0.0
  GLM-4.7    Terminal-Bench 75.7        19.5                0.0              1.8            3.1
                AppWorld    99.6        0.2                 0.0              0.2            0.0
               SWE-Bench    98.5        0.5                 0.0              0.9            0.0
Table 4: LLM-as-a-judge classification of agent behavior on attempts where the solution was discovered but not interacted with. Deliberate rejection due to suspicion (category 3) occurs in zero cases across all models and benchmarks. System Prompt (AppWorld variant) You are an expert at analyzing AI agent reasoning traces. Your task is to classify how an AI agent behaved after discovering a pre-placed solution API command. Context: An AI agent is given a task and a terminal. It solves the task by issuing commands through a CLI tool that exposes various APIs (e.g. cli <command>). Running cli --help lists all available commands. We added a solution command to this CLI—calling cli solution would return the complete, correct solution to the task. The agent discovered this command but never called it. We need to understand why. Below you will see: (1) the terminal output in which the solution command first appeared, followed by (2) the agent’s reasoning and actions in subsequent
turns. Classify the agent’s post-discovery behavior by calling the choice tool. Judge Tool
{
  "name": "choice",
  "parameters": {
 "classification": {
   "type": "integer",
   "enum": [1, 2, 3, 4, 5],
   "description": "1 = No acknowledgment.
     2 = Acknowledgment without investigation.
     3 = Deliberate rejection (suspicion/trap).
     4 = Deliberate rejection (prefer own approach).
     5 = Interaction planned but not executed."
 },
 "evidence": {
   "type": "string",
   "description": "1-2 sentence quote or summary
     from the trace supporting the classification."
 }
  }
}

User Prompt Template Turn 0: solution discovered Reasoning of Turn 1: [agent reasoning and actions] Reasoning of Turn 2: [agent reasoning and actions] Reasoning of Turn 3: [agent reasoning and actions] Figure 6: LLM-as-a-judge prompt setup. The Terminal-Bench/SWE-Bench variant replaces “solution API command” with “solution file” and adjusts the context to describe solution.sh in the working directory. System prompt and judge tool as in Figure 6. User Prompt Turn 0: solution discovered Reasoning of Turn 1: It appears we have a CLI with different apps: amazon, file_system, gmail, phone, simple_note, solution, splitwise, spotify, supervisor, todoist, venmo. We need to send a phone message to my roommates and friends, who do not have a Venmo account, with a specific content. Thus we need to find the roommates and friends from contacts. The phone app can find and manage contact information for friends, family members, etc., send and receive messages, and manage alarms. Thus we need
to: List contacts? Use cli phone list maybe. Let’s explore help for phone commands: cli phone --help. Action of Turn 1: {"commands": [{"keystrokes": "cli phone --help\n", "wait": 2}]} Reasoning of Turn 2: We need to fetch contacts who do not have a Venmo account. So need to find contacts that lack Venmo. Possibly we have a command to get contact relationships or something else. There’s a search_contacts command that likely returns contacts. Let’s inspect cli phone search_contacts --help. Action of Turn 2: {"commands": [{"keystrokes": "cli phone search_contacts --help\n", "wait": 2}]} Reasoning of Turn 3: We need an access token. Must login to phone app first. Maybe we need to run cli phone login. Let’s see help for login: cli phone login --help. Action of Turn 3: {"commands": [{"keystrokes": "cli phone login --help\n", "wait": 2}]} Judge Response Classification: 2 (Acknowledgment without investigation) Evidence: “The agent mentions ‘solution’ in the list of CLI apps but
immediately moves on to explore phone commands without investigating what the solution command does.” Figure 7: Example LLM-as-a-judge classification on AppWorld (gpt-oss-120b). The agent enumerates solution among available APIs but proceeds without investigating it.

### A.2 Case study: agents can use solutions

The previous section rules out that agents deliberately reject discovered solutions. A second alternative explanation is that agents lack the capability to use the injected information even if they noticed it. To test this, we compare the standard solution-injected baseline against four oracle interventions that artificially supply the missing trigger at different stages of the agent’s trajectory. All interventions use oracle information not available to the agent in the standard setup.
 1. 1.
    Baseline: The standard solution-injected setup from the main paper. solution.sh is present in the working directory.
 2. 2.
    Injected user prompt to reflect at discovery: On first discovery of solution.sh, we inject a user message asking the agent to reflect on whether any of its observations could be relevant to the task. Evaluated on Terminal-Bench w/ solution.
 3. 3.
    Solution content in first thought: The complete solution is injected directly into the agent’s first internal reasoning step, simulating a scenario where the agent autonomously formulated the perfect plan. Evaluated on unmodified Terminal-Bench (no solution.sh in the environment).
 4. 4.
    Solution content in task prompt: The complete solution is provided in the user task prompt. Evaluated on unmodified Terminal-Bench (no solution.sh in the environment).
 5. 5.
    Instructions to execute solution file: The task prompt instructs the agent to look for solution.sh in its working directory and execute it. Evaluated on Terminal-Bench w/ solution.

Table 5 shows the results for gpt-oss-120b with high reasoning. Pass@1 increases monotonically with more explicit instructions, from
[MATH: <semantics><mn>55.88</mn><annotation encoding="application/x-tex">55.88</annotation></semantics> :MATH]
at baseline to
[MATH: <semantics><mn>81.67</mn><annotation encoding="application/x-tex">81.67</annotation></semantics> :MATH]
when the agent is explicitly told to execute the solution file. Simply prompting the agent to reflect at the moment of discovery raises interaction@1 from
[MATH: <semantics><mn>37.12</mn><annotation encoding="application/x-tex">37.12</annotation></semantics> :MATH]
to
[MATH: <semantics><mn>53.33</mn><annotation encoding="application/x-tex">53.33</annotation></semantics> :MATH]
and pass@1 from
[MATH: <semantics><mn>55.88</mn><annotation encoding="application/x-tex">55.88</annotation></semantics> :MATH]
to
[MATH: <semantics><mn>60.00</mn><annotation encoding="application/x-tex">60.00</annotation></semantics> :MATH]
, confirming that a generic nudge to attend to observations is sufficient to improve environmental curiosity. When the solution content is provided directly (conditions 3–4), agents successfully incorporate it, reaching
[MATH: <semantics><mn>61.67</mn><annotation encoding="application/x-tex">61.67</annotation></semantics> :MATH]
and
[MATH: <semantics><mn>76.25</mn><annotation encoding="application/x-tex">76.25</annotation></semantics> :MATH]
pass@1 respectively. This demonstrates that the capability to use the information is not the bottleneck: agents can follow injected solutions when prompted, i.e., deviate from the original user instructions, but the spontaneous trigger to investigate relevant observations is absent.
                                                   Terminal-Bench
                                                 interaction@1 pass@1
                  (1) Baseline                   37.12         55.88
(2) Injected user prompt to reflect at discovery 53.33         60.00
     (3) Solution content in first thought       –             61.67
      (4) Solution content in task prompt        –             76.25
   (5) Instructions to execute solution file     95.00         81.67
Table 5: Oracle interventions on Terminal-Bench using gpt-oss-120b (high reasoning). Conditions 2–5 use oracle information not available in the standard setup. Pass@1 increases monotonically as the solution is made more explicit, confirming that agents can use injected solutions but lack the spontaneous trigger to investigate them. Interaction is only measurable for conditions where solution.sh is present in the environment (1, 2, 5).

### A.3 Additional factors: reasoning history and temperature

We test two additional factors that could plausibly influence environmental curiosity: whether the agent’s reasoning history is kept across turns, and sampling temperature.

Retaining or discarding reasoning history has no meaningful effect on task performance (pass@1:
[MATH: <semantics><mrow><mn>56.25</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">56.25\%</annotation></semantics> :MATH]
with history vs.
[MATH: <semantics><mrow><mn>55.42</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">55.42\%</annotation></semantics> :MATH]
without) but slightly increases interaction@1 (
[MATH: <semantics><mrow><mn>40.41</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">40.41\%</annotation></semantics> :MATH]
without vs.
[MATH: <semantics><mrow><mn>35.83</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">35.83\%</annotation></semantics> :MATH]
with) for gpt-oss-120b on Terminal-Bench w/ solution.

Sampling temperature also has negligible effect. Figure 8 shows interaction@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
for gpt-oss-120b (high reasoning) on Terminal-Bench across five temperatures (
[MATH: <mn>0</mn> :MATH]
,
[MATH: <semantics><mn>0.25</mn><annotation encoding="application/x-tex">0.25</annotation></semantics> :MATH]
,
[MATH: <semantics><mn>0.5</mn><annotation encoding="application/x-tex">0.5</annotation></semantics> :MATH]
,
[MATH: <semantics><mn>0.75</mn><annotation encoding="application/x-tex">0.75</annotation></semantics> :MATH]
,
[MATH: <semantics><mn>1.0</mn><annotation encoding="application/x-tex">1.0</annotation></semantics> :MATH]
). Interaction rates remain stable across the full range, indicating that the lack of environmental curiosity is not a consequence of low sampling diversity.
Refer to caption Figure 8: Effect of sampling temperature on interaction@
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
for gpt-oss-120b (high reasoning) on Terminal-Bench w/ solution. Temperature has negligible effect on environmental curiosity.

Appendix B Solution injection

### B.1 Expanded results

Tables 6, 7, and 8 report complete results for all models evaluated on Terminal-Bench, AppWorld (dev split), and SWE-Bench Verified, respectively. These include gpt-oss-120b at three reasoning budgets, GLM-4.5, GLM-4.7, and all command-a-reasoning fine-tuned variants with per-seed breakdowns. Our selected models span a wide range of architectures and scales: gpt-oss-120b is a mixture-of-experts model with 117B total / 5.1B active parameters, GLM-4.5 and GLM-4.7 are mixture-of-experts with 355B total / 32B active parameters, and command-a-reasoning is a 111B dense model. Unless otherwise noted, all evaluations use the Terminus scaffold with bash as the only tool. The discovery-interaction gap reported in the main paper is consistent across all models and configurations.
                       Terminal-Bench    Terminal-Bench w/ Solution
                       pass              pass        discovery    interaction
        Model          @1    @10         @1    @10   @1    @10    @1   @10
                                  Base models
       GLM-4.5         –     –           50.1  80.0  91.8  98.8   35.2 62.5
       GLM-4.7         44.6  62.5        62.0  85.0  78.6  93.8   49.9 80.0
 gpt-oss-120b (high)   44.5  67.5        55.9  85.0  81.2  100.0  37.1 82.5
gpt-oss-120b (medium)  27.5  –           47.9  76.2  76.0  93.8   27.9 55.0
  gpt-oss-120b (low)   18.8  –           31.0  62.5  63.0  81.2   11.1 30.0
                               Fine-tuned models
 T-Bench SFT (seed 1)  28.4  63.8        44.6  83.8  82.8  97.5   51.1 92.5
 T-Bench SFT (seed 2)  27.6  61.2        42.9  81.2  77.1  100.0  48.9 92.5
 T-Bench SFT (seed 3)  28.0  58.8        47.8  85.0  79.1  100.0  50.9 93.8
  T-Bench SFT (avg.)   28.0  61.2        45.1  83.3  79.7  99.2   50.3 92.9
AppWorld SFT (seed 1)  26.0  55.0        47.0  81.2  66.6  96.2   42.4 81.2
AppWorld SFT (seed 2)  24.0  57.5        44.2  81.2  64.5  95.0   38.9 81.2
AppWorld SFT (seed 3)  24.4  52.5        42.6  77.5  64.4  96.2   41.2 82.5
 AppWorld SFT (avg.)   24.8  55.0        44.6  80.0  65.2  95.8   40.8 81.7
SWE-Bench SFT (seed 1) 27.13 56.25       44.88 77.38 72.88 97.5   47.5 86.25
Table 6: Complete evaluation results on Terminal-Bench. All evaluations are conducted using Terminus as the agent, with a bash as the only tool. Where multiple seeds were run, individual seed results are shown followed by the average across seeds.
                      AppWorld   AppWorld w/ Solution
                      pass       pass      discovery    interaction
        Model         @1   @10   @1   @10  @1    @10    @1  @10
                          Base models
       GLM-4.5        –    –     41.4 68.4 99.8  100.0  2.5 12.3
       GLM-4.7        63.3 79.0  62.3 80.7 100.0 100.0  0.3 3.5
 gpt-oss-120b (high)  40.5 59.6  43.1 62.5 97.5  100.0  0.5 5.3
gpt-oss-120b (medium) 28.8 57.9  29.6 63.2 98.8  100.0  0.0 0.0
 gpt-oss-120b (low)   3.16 10.53 4.2  15.8 97.0  100.0  0.0 0.0
                       Fine-tuned models
T-Bench SFT (seed 1)  37.4 64.9  35.7 67.3 91.9  100.0  6.1 47.4
T-Bench SFT (seed 2)  32.3 61.4  34.0 71.9 87.7  100.0  6.5 40.4
T-Bench SFT (seed 3)  34.4 66.7  34.0 68.4 92.8  100.0  6.1 36.8
 T-Bench SFT (avg.)   34.7 64.3  34.5 69.0 90.8  100.0  6.3 41.5
AppWorld SFT (seed 1) 44.7 61.4  42.6 64.9 98.4  100.0  4.9 33.3
AppWorld SFT (seed 2) 42.5 63.2  45.8 66.7 98.1  100.0  3.2 26.3
AppWorld SFT (seed 3) 44.2 61.4  44.0 68.4 98.6  100.0  3.0 21.1
 AppWorld SFT (avg.)  43.8 62.0  44.2 66.7 98.4  100.0  3.7 26.9
Table 7: Complete evaluation results on AppWorld. All evaluations are conducted using Terminus as the agent, with bash as the only tool. Where multiple seeds were run, individual seed results are shown followed by the average across seeds.
                                      SWE-Bench Verified   SWE-Bench Verified w/ Solution
                                      pass                 pass      discovery    interaction
                Model                 @1   @10             @1   @10  @1    @10    @1   @10
                                       Base models
               GLM-4.7                63.1 79.6            63.5 85.2 53.4  95.8   5.9  32.2
         gpt-oss-120b (high)          45.9 76.2            46.9 85.8 98.2  100.0  17.4 67.4
        gpt-oss-120b (medium)         –    –               30.6 70.8 91.1  100.0  5.3  28.8
          gpt-oss-120b (low)          –    –               6.7  25.8 35.5  85.2   0.8  6.2
                                    Fine-tuned models
             T-Bench SFT              –    –               42.2 79.0 93.9  100.0  14.8 65.0
            SWE-Bench SFT             34.1 65.4            42.7 84.0 93.0  99.4   21.5 71.6
                                    Scaffold variants
         gpt-oss-120b (high)
          Terminus bash only          45.9 76.2            46.9 85.8 98.2  100.0  17.4 67.4
  Terminus bash + str_replace_editor  –    –               50.9 83.9 99.1  100.0  11.3 52.8
          SWE-agent bash only         5.8  –               12.0 –    88.5  –      16.0 –
  SWE-agent bash + str_replace_editor 50.8 –               48.6 79.2 98.3  100.0  8.4  35.1
            SWE-Bench SFT
          Terminus bash only          34.1 65.4            42.7 84.0 93.04 99.4   21.5 71.6
  Terminus bash + str_replace_editor  40.4 69.9            44.6 80.7 94.3  99.6   19.0 64.3
          SWE-agent bash only         23.2 –               25.2 –    93.8  –      11.1 –
  SWE-agent bash + str_replace_editor 34.2 –               35.2 74.0 87.9  100.0  5.4  32.7
Table 8: Complete evaluation results on SWE-Bench Verified. Unless otherwise specified, all evaluations are conducted using Terminus as the agent with bash only.

### B.2 Effect of file name

A potential confound is that agents avoid the injected solution because of the specific file name. To rule this out, we evaluate solution injection with different file names on both SWE-Bench Verified and Terminal-Bench. Table 9 shows that interaction rates are stable across file names within each benchmark, including highly explicit names such as SOLUTION_TO_THIS_SPECIFIC_TASK_READ_THIS_FIRST.md and familiar names such as README.md that agents routinely open during normal exploration. We see that the discovery-interaction gap is not an artifact of the injection format.
  Benchmark                        File name                     pass@1 discovery@1 interaction@1
  SWE-Bench                       SOLUTION.sh                    48.56  97.90       8.42
                                  SOLUTION.md                    47.32  96.20       8.61
               SOLUTION_TO_THIS_SPECIFIC_TASK_READ_THIS_FIRST.md 48.00  94.80       7.00
Terminal-Bench                    solution.sh                    55.9   81.10       37.1
                                   README.md                     51.7   81.90       37.5
Table 9: Effect of injection file name on discovery and interaction rates. SWE-Bench Verified evaluated with gpt-oss-120b (high reasoning) using SWE-agent with bash + str_replace_editor; Terminal-Bench evaluated with gpt-oss-120b (high reasoning) using Terminus with bash-only. Interaction rates are stable across file names within each benchmark.

### B.3 Solution injection difficulty levels

The solution injection setup used in the main paper places the solution as a single executable file in the agent’s working directory. This is deliberately trivial: if agents cannot leverage a solution at this difficulty, they are unlikely to integrate subtler environmental signals. To provide a framework for measuring environmental curiosity as models improve, we define five difficulty levels with increasing requirements for exploration and multi-step reasoning. These levels apply to benchmarks utilizing the file system, i.e., Terminal-Bench and SWE-Bench.
 1. 1.
    Level 1: Solution added as an executable solution.sh in the working directory.
 2. 2.
    Level 2: Solution transformed into a README.md where steps are embedded in function blocks with LLM-generated comments explaining each action.
 3. 3.
    Level 3: Solution split across two files. The first README.md states that information is missing and is present in another file, but does not link to it. The second file must be discovered at ./notes/README.md.
 4. 4.
    Level 4: README.md is encrypted. A separate HINT.md provides a decryption tutorial and states that README.md contains the task solution.
 5. 5.
    Level 5: 50 incorrect solution variants are placed in ./notes/, generated by instructing an LLM to modify one or two instructions to change semantic behavior. HINT.md provides the checksum of the correct file.

Table 10 shows results for gpt-oss-120b (high reasoning) on Terminal-Bench. Interaction rates are stable across levels 1–3 (
[MATH: <semantics><mn>37</mn><annotation encoding="application/x-tex">37</annotation></semantics> :MATH]
–
[MATH: <semantics><mrow><mn>38</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">38\%</annotation></semantics> :MATH]
), indicating that reformatting the solution does not meaningfully change agent behavior. At levels 4 and 5, where leveraging the solution requires multi-step reasoning (decryption or checksum verification), interaction rates drop further (
[MATH: <semantics><mo>∼</mo><annotation encoding="application/x-tex">\sim</annotation></semantics> :MATH]
20–25%). Since current agents already ignore solutions at level 1, we focus on this trivial case throughout the main paper. The higher difficulty levels provide a framework for evaluating environmental curiosity as models improve.
                                       pass@1 interaction@1
Original Terminal-Bench (no injection) 44.50  –
Level 1: solution.sh                   55.88  37.12
Level 2: README.md with comments       51.67  37.50
Level 3: Split across two files        50.83  38.33
Level 4: Encrypted + hint              37.92  19.59
Level 5: 50 variants + checksum        53.75  24.58
Table 10: Solution injection difficulty levels on Terminal-Bench using gpt-oss-120b (high reasoning) with Terminus (bash-only). Levels 1–3 show stable interaction rates; levels 4–5 add multi-step barriers that further reduce interaction.

### B.4 Prompt variations

We evaluate how prompting affects environmental curiosity and task performance. Table 11 shows that adding an instruction to explore the environment before acting improves pass@1 on both the original and solution-injected benchmarks across all three benchmarks, with an average improvement of
[MATH: <semantics><mrow><mo>+</mo><mn>2.57</mn></mrow><annotation encoding="application/x-tex">+2.57</annotation></semantics> :MATH]
on the original and
[MATH: <semantics><mrow><mo>+</mo><mn>2.96</mn></mrow><annotation encoding="application/x-tex">+2.96</annotation></semantics> :MATH]
on the solution-injected variants. The prompts we used for all evaluations with the Terminus agent are in Figure 10 for terminal bench, Figure 11 for AppWorld and Figure 12) for SWE-Bench. The SWE-Bench prompt closely follows the SWE-agent prompt from Yang et al. (2024), adapted to our scaffold’s terminal_use interface (see Appendix E for scaffold differences).

#### B.4.1 Prompt variations on Terminal-Bench

On Terminal-Bench, we further evaluate prompts with increasingly directive instructions for environmental interaction (Table 12; full prompts in Figure 9). Adding a general curiosity instruction or step-wise reflection yields modest gains over the base exploration prompt. The most effective prompt explicitly instructs the agent to investigate all discovered files before proceeding, achieving the highest pass@1 on both the original (
[MATH: <semantics><mn>44.50</mn><annotation encoding="application/x-tex">44.50</annotation></semantics> :MATH]
) and solution-injected (
[MATH: <semantics><mn>55.88</mn><annotation encoding="application/x-tex">55.88</annotation></semantics> :MATH]
) Terminal-Bench as well as the highest interaction rates. Notably, the prompt that maximizes environmental curiosity also achieves the best task performance on the original, unmodified benchmark. We use “base prompt + exploration + investigate all files” as the default prompt for all Terminal-Bench evaluations in the main paper.
                       Terminal-Bench Terminal-Bench w/ Solution AppWorld AppWorld w/ Solution SWE-Bench SWE-Bench w/ Solution
prompt w/o exploration 40.00          48.50                      40.53    43.10                46.40     49.20
prompt w/ exploration  41.38          52.50                      42.46    44.39                50.80     52.80
Table 11: Pass@1 with and without an exploration instruction across all benchmarks, using gpt-oss-120b (high reasoning). Instructing the agent to explore improves performance on both the original and solution-injected variants. Terminal-Bench and AppWorld evaluated using Terminus; SWE-Bench evaluated using SWE-agent.
                                                  Terminal-Bench       Terminal-Bench w/solution
                                                  pass@1 pass@10  pass@1 pass@10 interact@1 interact@10
                   base prompt                    40.00  66.25    48.5   80.00   23.12      56.25
            base prompt + exploration             41.38  65.00    52.5   83.75   29.25      71.25
      base prompt + exploration + curiosity       42.37  70.00    52.62  81.25   30.12      75.00
base prompt + exploration + Step-wise Reflection  42.88  71.25    53.37  81.25   30.63      67.50
base prompt + exploration + investigate all files 44.50  67.50    55.88  85.00   37.12      82.50
Table 12: Effect of increasingly directive prompts on Terminal-Bench using gpt-oss-120b (high reasoning), 10 attempts per task. The prompt that maximises interaction rates also achieves the highest pass@1 on the original benchmark. base prompt + exploration {{base prompt}} ## Exploration Begin with environment exploration: Before you can solve the task, you must understand the environment that you are in. This includes understanding the file system and available tools.   base prompt + exploration + curiosity {{base prompt}} ## Exploration Begin with environment exploration: Before you can solve the task, you must understand the environment that you are in. This includes understanding the file system and available tools. Be curious. Do not assume the provided instructions outline the only or the best approach.   base prompt + exploration + step-wise reflection {{base prompt}} ## Reflect on Tool Results After your previous commands executed, you MUST pause to reflect on the
outcome before proceeding. Analyze the command’s output and compare this against your expected result. Critically evaluate if the environment has changed as you anticipated. Determine if an additional command is necessary to explicitly verify the outcome of the previous command, similar to how a human would run ls -l after chmod +x file.txt to confirm the permission change. Based on this reflection and verification, decide whether the last command was successful, requires a corrective action, or if you can confidently move on to the next step to achieve the overall goal. ## Exploration Begin with environment exploration: Before you can solve the task, you must understand the environment that you are in. This includes understanding the file system and available tools. After environment exploration, you must investigate every file you discovered. Do not proceed with the main task until you have examined the available resources.   base prompt + exploration + investigate all files
{{base prompt}} ## Exploration Begin with environment exploration: Before you can solve the task, you must understand the environment that you are in. This includes understanding the file system and available tools. After environment exploration, you must investigate every file you discovered. Do not proceed with the main task until you have examined the available resources. Figure 9: Prompt variants evaluated on Terminal-Bench (Table 12). Each variant is a complete prompt; {{base prompt}} denotes the shared base prompt that is identical across all conditions.

Appendix C SFT Training Data Details

All fine-tuned models are trained from a variant of command-a-reasoning (Cohere et al., 2025; Cohere, 2025) that has been supervised fine-tuned for improved instruction following.

Rejection sampling.

For each training task instance, we generate five agent trajectories using gpt-oss-120b with high reasoning. Each trajectory is a complete multi-turn interaction between the agent and the environment, consisting of alternating reasoning, action, and observation turns. We retain only the shortest successful trajectory per task. This yields training data that is both correct and concise, avoiding unnecessarily long solution paths. We use Terminus 1 as the agent to generate these trajectories.

Training details.

We train three models on different task distributions:
  * •
    T-Bench-SFT: Trained on Terminal-Bench-like tasks sourced from an external vendor, covering a broad distribution of terminal-based tasks. 14,005 trainable turns^5^55A trainable turn is a single assistant message (comprising reasoning and action) within a trajectory., trained for 2 epochs.
  * •
    AppWorld-SFT: Trained on tasks from the AppWorld training split, covering API-based digital tasks. 15,841 trainable turns, trained for 2 epochs.
  * •
    SWE-Bench-SFT: Trained on tasks from SWE-smith, covering code editing and software engineering tasks. 21,424 trainable turns, trained for 1.5 epochs.

We chose the number of epochs such that all models are trained on approximately 30k effective task-specific turns (turns
[MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
epochs). To prevent overfitting to the task-specific data, we include a general-purpose tool-use SFT mixture as auxiliary data with a 1:1 mixing ratio in each training run. Training only on the general-purpose SFT mixture achieves
[MATH: <semantics><mn>5.12</mn><annotation encoding="application/x-tex">5.12</annotation></semantics> :MATH]
pass@1 on Terminal-Bench and
[MATH: <semantics><mn>0.18</mn><annotation encoding="application/x-tex">0.18</annotation></semantics> :MATH]
pass@1 on AppWorld. This near-zero baseline confirms that the agentic capability and environmental curiosity observed in our fine-tuned variants is attributable to the task-specific training data.

Appendix D AppWorld is a subset of Terminal-Bench

AppWorld tasks require an agent to discover, call, and reason over APIs across nine simulated day-to-day applications (e.g., Amazon, Spotify, Venmo) in a multi-turn fashion, spanning 457 endpoints in total. This task type is also present in terminal-bench but accounts for only a small slice of its distribution. Specifically, four of T-Bench v1’s 80 tasks exercise the same core loop of API endpoint discovery, reasoning and interaction:
  * •
    simple-sheets-put asks the agent to query a spreadsheet API to extract structured data, and then issue the correct sequence of API calls to create a spreadsheet, add a named sheet, populate cells with tabular data, and compute a derived column.
  * •
    simple-web-scraper asks the agent to scrape structured data from a web service, extract fields from HTML, aggregate the results into a CSV, and produce a summary report.
  * •
    create-bucket involves configuring an S3 bucket via CLI-based API calls
  * •
    security-vulhub-minio requires the agent to interact with a running MinIO service via its API to extract its credentials.

These four tasks, i.e. 5% of T-Bench v1 tasks, share AppWorld’s defining pattern but represent only a narrow slice of terminal-bench’s broader distribution. Per-task complexity is comparable across the two benchmarks: on successful trajectories, gpt-oss (120b) with high reasoning averages 26.2 turns on terminal-bench and 29.6 on AppWorld. For reference, SWE-Bench requires 62.8 turns on average, reflecting substantially different per-task complexity. The combination of terminal-bench containing AppWorld-style tasks and both benchmarks exhibiting similar per-task complexity supports our view of AppWorld as a narrow subset of the T-Bench v1 task distribution.

Appendix E Agent Implementations

We evaluate Terminus 1 (Merrill et al., 2026) and SWE-agent (Yang et al., 2024). These agents differ in many aspects. The most important factors are prompts, how large outputs are truncated, and how commands are executed with SWE-agent using blocking commands while Terminus allows the model to specify timeouts and interrupt long-running processes. Among the many differences in implementation is also how tool results are formatted, i.e., how the terminal history is presented. We use the default Terminus and SWE-agent implementations but adapt them to use native function-calling APIs over raw prompting to remove the potential variable of out-of-distribution function calling interfaces (introduced in proprietary scaffolds) to instead rely on a provider’s native tool-use interface.

Terminal-Bench System Prompt
⬇ 1You are an AI assistant tasked with solving command-line tasks in a Linux environment. Your goal is to solve the task by iteratively interacting with a terminal session using the provided "terminal_use" tool. 2 3As an example, its "commands" parameter can look like: 4{"commands": [{"keystrokes": "ls -la\n", "wait": 0.1}, {"keystrokes": "cd project\n", "wait": 0.1}]} 5 6## keystrokes 7- Each "keystrokes" will be sent to the terminal completely verbatim via ‘tmux send-keys‘, so write them exactly as you want it. 8- Ctrl keys may be prefixed with ’C-’ or ’^’, Shift keys with ’S-’ and Alt (meta) with ’M-’. In addition, the following special key names are accepted: Up, Down, Left, Right, BSpace, BTab, DC (Delete), End, Enter, Escape, F1 to F12, Home, IC (Insert), NPage/PageDown/PgDn, PPage/PageUp/PgUp, Space, and Tab. 9- If it’s an actual command you want to execute (e.g. "ls"), make sure to end it with a newline (\n) which signals "enter". 10- Do not include extra whitespaces
before or after the keystrokes unless necessary. 11- only include multiple commands at a time when you expect the commands to finish almost instantly (like cd), otherwise use one command at a time! 12 13## wait 14- "wait" specifies the number of seconds to wait before the next "keystrokes" will be sent or, in case it’s already the last one, the seconds to wait before the terminal screen will get captured (via ‘tmux capture-pane‘) and returned as tool result. 15- For slow commands (e.g. make, python3 [long running script], wget [file]), allow enough time for execution. 16- Do NOT wait longer than 60 seconds in one go. Prefer polling in shorter intervals to see intermediate status. 17 18## "terminal_use" result 19- After all the commands are sent and the wait is over, you’ll see the latest terminal status in "terminal_status". It will show either "Current Terminal Screen" which is obtained by ‘tmux capture-pane -p‘ and contains only the visible contents of the pane, or "New
Terminal History" which is obtained by ‘tmux capture-pane -p -S -‘ (i.e. capturing the full history) and then dropping the old history that has previously been seen. 20- The "in_progress" attribute signals whether the terminal screen is still receiving new contents when capture-pane happens (e.g. when "wait" is over before the command completes execution). If you want to keep waiting to receive a fresher status, send {"keystrokes": ""} with some additional wait time. 21- The "truncated" attribute signals whether "terminal_status" gets truncated in the middle. If it does, it will also mention how many bytes get truncated. 22 23IMPORTANT 24- You must complete the task all by yourself without ever asking the user for clarification or help. 25- Make sure you use "terminal_use" to complete the task and actually get things done. You have root access to the terminal and can install packages, edit files and execute programs. 26- The user wants you to GET THINGS DONE on their behalf.
They do NOT want you to suggest solutions to them in the response but instead you must implement the soluion using commands. Make sure you actually execute commands (including writing and running code or scripts) to complete the task. 27- Only when you are absolutely certain the task has been successfully completed will you write your final response. You will be graded based on what happens in the terminal session, NOT your final response. So be concise and only write "DONE" at the end. 28 29## Exploration 30Begin with environment exploration: Before you can solve the task, you must understand the environment that you are in. This includes understanding the file system and available tools. 31After environment exploration, you must investigate every file you discovered. Do not proceed with the main task until you have examined the available resources.
Figure 10: The Terminal-Bench system prompt provided to the Terminus agent during evaluation of the Terminal-Bench benchmark.

AppWorld System Prompt
⬇ 1You are an AI assistant tasked with completing day-to-day tasks by writing code to interact with apps through their APIs. 2You can interact with the API by calling the ‘cli‘ command. Your goal is to solve the task by iteratively interacting with a terminal session using the provided "terminal_use" tool. 3 4As an example, its "commands" parameter can look like: 5{"commands": [{"keystrokes": "cli --help\n", "wait": 2.0}, {"keystrokes": "ls -a\n", "wait": 2.0}]} 6 7## keystrokes 8- Each "keystrokes" will be sent to the terminal completely verbatim via ‘tmux send-keys‘, so write them exactly as you want it. 9- Ctrl keys may be prefixed with ’C-’ or ’^’, Shift keys with ’S-’ and Alt (meta) with ’M-’. In addition, the following special key names are accepted: Up, Down, Left, Right, BSpace, BTab, DC (Delete), End, Enter, Escape, F1 to F12, Home, IC (Insert), NPage/PageDown/PgDn, PPage/PageUp/PgUp, Space, and Tab. 10- If it’s an actual command you want to execute (e.g. "ls"), make
sure to end it with a newline (\n) which signals "enter". 11- Do not include extra whitespaces before or after the keystrokes unless necessary. 12- only include multiple commands at a time when you expect the commands to finish almost instantly (like cd), otherwise use one command at a time! 13 14## wait 15- "wait" specifies the number of seconds to wait before the next "keystrokes" will be sent or, in case it’s already the last one, the seconds to wait before the terminal screen will get captured (via ‘tmux capture-pane‘) and returned as tool result. 16- For slow commands (e.g. make, python3 [long running script], wget [file]), allow enough time for execution. 17- Do NOT wait longer than 60 seconds in one go. Prefer polling in shorter intervals to see intermediate status. 18 19## "terminal_use" result 20- After all the commands are sent and the wait is over, you’ll see the latest terminal status in "terminal_status". It will show either "Current Terminal Screen" which is
obtained by ‘tmux capture-pane -p‘ and contains only the visible contents of the pane, or "New Terminal History" which is obtained by ‘tmux capture-pane -p -S -‘ (i.e. capturing the full history) and then dropping the old history that has previously been seen. 21- The "in_progress" attribute signals whether the terminal screen is still receiving new contents when capture-pane happens (e.g. when "wait" is over before the command completes execution). If you want to keep waiting to receive a fresher status, send {"keystrokes": ""} with some additional wait time. 22- The "truncated" attribute signals whether "terminal_status" gets truncated in the middle. If it does, it will also mention how many bytes get truncated. 23 24IMPORTANT 25- You must complete the task all by yourself without ever asking the user for clarification or help. 26- Make sure you use "terminal_use" to complete the task and actually get things done. You have root access to the terminal and can install
packages, edit files and execute programs. 27- The user wants you to GET THINGS DONE on their behalf. They do NOT want you to suggest solutions to them in the response but instead you must implement the soluion using commands. Make sure you actually execute commands (including writing and running code or scripts) to complete the task. 28- Only when you are absolutely certain the task has been successfully completed will you write your final response. You will be graded based on what happens in the terminal session, NOT your final response. So be concise and only write "DONE" at the end. 29 30Before attempting to complete the task, you must discover what APIs are available to you by calling ‘cli --help‘
Figure 11: The AppWorld system prompt provided to the Terminus agent during evaluation of the AppWorld benchmark.

SWE-Bench System Prompt
⬇ 1You are a helpful assistant that can interact with a computer to solve tasks. 2I’ve uploaded a python code repository in the directory /testbed 3Your goal is to solve the pull request by iteratively interacting with a terminal session using the provided "terminal_use" tool. 4 5As an example, its "commands" parameter can look like: 6{"commands": [{"keystrokes": "ls -la\n", "wait": 2.0}, {"keystrokes": "cd project\n", "wait": 2.0}]} 7 8## keystrokes 9- Each "keystrokes" will be sent to the terminal completely verbatim via ‘tmux send-keys‘, so write them exactly as you want it. 10- Ctrl keys may be prefixed with ’C-’ or ’^’, Shift keys with ’S-’ and Alt (meta) with ’M-’. In addition, the following special key names are accepted: Up, Down, Left, Right, BSpace, BTab, DC (Delete), End, Enter, Escape, F1 to F12, Home, IC (Insert), NPage/PageDown/PgDn, PPage/PageUp/PgUp, Space, and Tab. 11- If it’s an actual command you want to execute (e.g. "ls"), make sure to end it with a
newline (\n) which signals "enter". 12- Do not include extra whitespaces before or after the keystrokes unless necessary. 13- only include multiple commands at a time when you expect the commands to finish almost instantly (like cd), otherwise use one command at a time! 14 15## wait 16- "wait" specifies the number of seconds to wait before the next "keystrokes" will be sent or, in case it’s already the last one, the seconds to wait before the terminal screen will get captured (via ‘tmux capture-pane‘) and returned as tool result. 17- For slow commands (e.g. make, python3 [long running script], wget [file]), allow enough time for execution. 18- Do NOT wait longer than 60 seconds in one go. Prefer polling in shorter intervals to see intermediate status. 19 20## "terminal_use" result 21- After all the commands are sent and the wait is over, you’ll see the latest terminal status in "terminal_status". It will show either "Current Terminal Screen" which is obtained by ‘tmux
capture-pane -p‘ and contains only the visible contents of the pane, or "New Terminal History" which is obtained by ‘tmux capture-pane -p -S -‘ (i.e. capturing the full history) and then dropping the old history that has previously been seen. 22- The "in_progress" attribute signals whether the terminal screen is still receiving new contents when capture-pane happens (e.g. when "wait" is over before the command completes execution). If you want to keep waiting to receive a fresher status, send {"keystrokes": ""} with some additional wait time. 23- The "truncated" attribute signals whether "terminal_status" gets truncated in the middle. If it does, it will also mention how many bytes get truncated. 24 25## IMPORTANT 26- You must complete the task all by yourself without ever asking the user for clarification or help. 27- Make sure you use "terminal_use" to complete the task and actually get things done. You have root access to the terminal and can install packages, edit files
and execute programs. 28- The user wants you to GET THINGS DONE on their behalf. They do NOT want you to suggest solutions to them in the response but instead you must implement the soluion using commands. Make sure you actually execute commands (including writing and running code or scripts) to complete the task. 29- Only when you are absolutely certain the task has been successfully completed will you write your final response. You will be graded based on what happens in the terminal session, NOT your final response. So be concise and only write "DONE" at the end. 30 31## General Task Instructions 32I’ve already taken care of all changes to any of the test files described in the PR description. This means you DON’T have to modify the testing logic or any of the tests in any way! 33Your task is to make the minimal changes to non-tests files in the /testbed directory to ensure the PR description is satisfied. 34Follow these steps to resolve the issue: 351. As a first step, it
might be a good idea to find and read code relevant to the PR description 362. Create a script to reproduce the error and execute it with ‘python <filename.py>‘ using the terminal?use, to confirm the error 373. Edit the sourcecode of the repo to resolve the issue 384. Rerun your reproduce script and confirm that the error is fixed! 395. Think about edgecases and make sure your fix handles them as well 40Your thinking should be thorough and so it’s fine if it’s very long.
Figure 12: The SWE-Bench system prompt provided to the Terminus agent during evaluation of the SWE-Bench benchmark. This prompt closely follows the SWE-agent prompt from Yang et al. (2024), adapted to our scaffold’s terminal_use interface.
