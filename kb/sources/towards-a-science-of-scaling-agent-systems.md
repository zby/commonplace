---
source: https://arxiv.org/pdf/2512.08296
captured: 2026-03-08
capture: pdf-read
type: academic-paper
---

# Towards a Science of Scaling Agent Systems

Author: Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Yun Liu, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu (Google Research, Google DeepMind, MIT)
Source: https://arxiv.org/pdf/2512.08296
Date: 17 Dec 2025 (arXiv:2512.08296v2)

---

## Abstract

*Agents*, language model (LM)-based systems that are capable of reasoning, planning, and acting are becoming the dominant paradigm for real-world AI applications. Despite this widespread adoption, the principles that determine their performance remain underexplored, leaving practitioners to rely on heuristics rather than principled design choices. We address this gap by deriving quantitative *scaling principles* for agent systems. We first formalize a definition for agentic evaluation and characterize scaling laws as the interplay between agent quantity, coordination structure, model capability, and task properties. We evaluate this across four diverse benchmarks: Finance-Agent, BrowseComp-Plus, PlanCraft, and Workbench, spanning financial reasoning, web navigation, game planning, and workflow execution. Using five canonical agent architectures (Single-Agent System and four Multi-Agent Systems: Independent, Centralized, Decentralized, Hybrid), instantiated across three LLM families, we perform a controlled evaluation spanning 180 configurations, standardizing tools, prompt structures, and token budgets to isolate architectural effects from implementation confounds. We derive a predictive model using empirical coordination metrics, including efficiency, overhead, error amplification, and redundancy, that achieves cross-validated R²=0.524, enabling prediction on unseen task domains by modeling task properties rather than overfitting to a specific dataset. We identify three dominant effects: (1) a *tool-coordination trade-off*: under fixed computational budgets, tool-heavy tasks suffer disproportionately from multi-agent overhead. (2) a *capability saturation*: we observe that coordination yields diminishing or negative returns (β̂=−0.404, p<0.001) once single-agent baselines exceed an empirical threshold of ~45%. (3) *topology-dependent error amplification*: independent agents amplify errors 17.2× through unchecked propagation, while centralized coordination contains this to 4.4×. Crucially, coordination benefits are task-contingent. Centralized coordination improves performance by 80.8% on parallelizable tasks like financial reasoning, while decentralized coordination excels on dynamic web navigation (+9.2% vs. +0.2%). Yet for sequential reasoning tasks, every multi-agent variant we tested degraded performance by 39–70%. The framework predicts the optimal coordination strategy for 87% of held-out configurations. Out-of-sample validation on GPT-5.2, released after our study, achieves MAE=0.071 and confirms four of five scaling principles generalize to unseen frontier models, providing a quantitatively predictive framework for *agentic scaling* based on measurable task properties.

---

## 1. Introduction

*Agents* (Wang et al., 2024a), language model-driven systems that operate through iterative cycles of reasoning, planning, and acting, adapting their behavior based on environmental or tool-generated feedback, have achieved remarkable performance in diverse applications, from code generation (Yang et al., 2024; Zhang et al., 2024), web browsing (Wei et al., 2025; Yao et al., 2022), medical decision-making (Heydari et al., 2025; Kim et al., 2024; McDuff et al., 2025), finance (Yu et al., 2025), sustainability (Zhang et al., 2025b), to scientific discovery (Gottweis et al., 2025; Mitchener et al., 2025). As tasks grow in complexity and require sustained environmental interaction, the field has increasingly turned to multi-agent systems (MAS), relying on the premise that specialized collaboration consistently outperforms single-agent systems (SAS).

Previous work has made positive claims about multi-agent systems: "More agents is all you need" (Li et al., 2024), suggesting that agent collaboration follows collaborative scaling principles (Qian et al., 2025), and that MAS consistently outperforms single-agent systems (SAS) on complex tasks (Chen et al., 2024b; Du et al., 2023). Yet, despite rapid adoption, there remains no principled quantitative framework to predict when adding agents amplifies performance and when it erodes it.

To determine when multi-agent coordination provides benefit, we first establish which task categories require agentic capabilities. A critical prerequisite is distinguishing between *agentic* and *non-agentic* evaluation paradigms. Expanding from the Agentic Benchmark Checklist (ABC) introduced in (Zhu et al., 2025), we characterize *agentic tasks* as those requiring: (i) sustained multi-step interactions with an external environment, (ii) iterative information gathering under partial observability, and (iii) adaptive strategy refinement based on environmental feedback.

These characteristics differentiate tasks like web browsing (Wei et al., 2025), financial trading (Yu et al., 2025), software engineering (Jimenez et al., 2024), and interactive planning (Dagan et al., 2024) from traditional static benchmarks, tasks solvable through single-shot reasoning without environmental feedback, which lack external environments, are fully observed, or require identical solution strategies (Kapoor et al., 2025; Liu et al., 2024).

Multi-agent systems that show monotonic improvement with team size on static benchmarks (reaching 89% on HumanEval with five agents) exhibit fundamentally different scaling behavior when evaluated on tasks requiring sustained environmental interaction, where coordination overhead and error propagation dynamics dominate.

Fundamentally, this distinction reflects a trade-off between context integration and diversity (Du et al., 2023; Hong et al., 2024). Single-agent systems maximize context integration by maintaining a unified memory stream in which all reasoning steps share full access to prior history, enabling effectively constant-time access to global context. In contrast, multi-agent systems impose intrinsic information fragmentation (Tran et al., 2025): while parallel agents enable diverse exploration, they incur an unavoidable *coordination tax* in which the global context must be compressed into inter-agent messages. This lossy communication increases synchronization overhead and cognitive load, fundamentally altering the scaling behavior of collaboration.

Two fundamental challenges hinder progress toward principled multi-agent design. **First**, existing MAS evaluations compare architectures using different prompts, tools, or computational budgets, conflating architectural effects with implementation choices and precluding clean causal attribution. **Second**, evaluations focus exclusively on final accuracy metrics without examining process dynamics such as coordination overhead, error propagation, and information flow that determine whether collaboration succeeds or fails.

To address these challenges, we present a controlled evaluation establishing the principles for agent coordination. Our experimental design isolates architectural effects by controlling for implementation confounds which maintains identical task prompts, tools, and computational budgets across all configurations, while systematically varying only coordination structure and model capability. We evaluate five canonical architectures: Single Agent System (SAS) and four Multi-Agent variants (Independent, Centralized, Decentralized, Hybrid) instantiated across three major LLM families (OpenAI, Google, Anthropic) spanning diverse capability levels, on four representative agentic benchmarks: (1) web browsing (BrowseComp-Plus), (2) financial analysis (Finance-Agent), (3) game planning (PlanCraft), and (4) realistic workplace tasks (Workbench). Across N=180 controlled configurations with matched token budgets, we derive a scaling principle across tested domains quantifying how performance emerges from empirically measured coordination properties.

### Primary Contributions

- **Formalization of Agentic Evaluation rigor:** We redefine rigorous agentic assessment by distinguishing it from static reasoning tasks (e.g., MMLU). We establish that valid agentic evaluation requires three necessary conditions: sustained multi-step environment interaction, iterative information gathering under partial observability, and adaptive strategy refinement based on feedback.
- **Controlled evaluation of agent systems:** We establish a framework for comparing agent architectures, controlling for implementation confounds to isolate the effects of coordination structure. Our framework spans 180 configurations across three LLM families and four diverse benchmarks, enabling the causal attribution of performance differences to architectural choices rather than stochastic variations.
- **Intelligence-Coordination alignment:** We characterize the non-linear relationship between foundational model capabilities and agentic performance. We demonstrate that while higher capability (Intelligence Index) offers accelerating returns, these gains are not automatic; they strictly depend on architectural alignment. Without correct coordination structures, foundational improvements are often negated by coordination overhead.
- **Quantitative scaling principles and architecture alignment:** We derive a mixed-effects model (R²=0.524) using empirical coordination metrics—efficiency (E_c), error amplification (A_e), and redundancy (ρ)—to quantify how performance emerges from the interplay of reasoning capability and task properties. This framework identifies fundamental limits on coordination, specifically a *tool-coordination trade-off* (β=−0.267) where tool-heavy workflows suffer from coordination tax, and safety bounds where centralized verification reduces error amplification from 17.2× to 4.4×. Leveraging these mechanisms, we demonstrate that architecture selection is governed by measurable task features (e.g., decomposability) rather than simple agent scaling, achieving 87% accuracy in predicting optimal architectures on held-out tasks.

---

## 2. Related Work

**Multi-Agent Systems (MAS) versus Single-Agent Systems (SAS)** Following Tran et al. (2025) and Guo et al. (2024), a **Single-Agent System** features a solitary reasoning locus: all perception, planning, and action occur within a single sequential loop controlled by one LLM instance, even when employing tool use (Yao et al., 2023), self-reflection (Shinn et al., 2023), or chain-of-thought (CoT) reasoning (Wei et al., 2022). Critically, self-reflection mechanisms do not constitute multi-agent collaboration, as they operate within a single decision-making locus (Weng, 2023). A **Multi-Agent System** comprises multiple LLM-backed agents communicating through structured message passing, shared memory, or orchestrated protocols (Xi et al., 2025). MAS architectures vary by topology: *Independent* systems aggregate isolated outputs; *Decentralized* enable peer-to-peer exchange (Du et al., 2023); *Centralized* route through orchestrators (Hong et al., 2024); *Hybrid* combine hierarchical control with lateral communication (Dang et al., 2025).

**Scaling Laws and Coordination Mechanisms** Understanding performance scaling in multi-agent systems requires distinguishing collaborative scaling from neural scaling laws. While neural scaling follows power laws requiring million-fold parameter increases for significant trends (Kaplan et al., 2020), collaborative scaling exhibits logistic growth patterns emerging at substantially smaller scales (Qian et al., 2025). Chen et al. (2024a) explore whether increased LLM calls alone drive performance, finding compound inference systems follow distinct scaling behaviors from single-model training. However, Wang et al. (2024a) note collaborative scaling shows no significant universal pattern, suggesting domain-specific rather than general laws. Coordination mechanisms critically determine whether collaboration amplifies or degrades performance. Recent work reveals architecture-task alignment matters more than team size: Zhang et al. (2025a) achieve superior performance at 6-45% cost through query-dependent configurations; Dang et al. (2025) show puppeteer orchestration improvements stem from compact cyclic structures; Du et al. (2023) demonstrate peer-to-peer debate effectiveness depends on task decomposability.

---

## 3. Agent Systems and Tasks

### 3.1. System Definition

An **agent system** S = (A, E, C, Ω) consists of a set of agents A = {a₁, ..., aₙ} (where n ≥ 1), a shared environment E, a communication topology C, and an orchestration policy Ω. When |A| = 1, we refer to this as a Single-Agent System (SAS); when |A| > 1, a Multi-Agent System (MAS). Each agent aᵢ perceives, reasons, and acts within the environment via iterative feedback.

Formally, each agent aᵢ is defined as a tuple Sᵢ = (Φᵢ, Aᵢ, Mᵢ, πᵢ), where:

- Φᵢ is the reasoning policy (typically an LLM)
- Aᵢ = {ToolCall(t, θ) : t ∈ T, θ ∈ Θₜ} is the action space consisting of tool usage
- Mᵢ is the internal memory
- πᵢ : H → Aᵢ is the decision function mapping observation histories to actions

**Single-Agent System (SAS).** A Single-Agent System contains one reasoning locus (|A| = 1). All perception, reasoning, and action occur within a single sequential loop, producing computational complexity O(k) where k is the number of reasoning iterations. SAS has zero communication overhead and minimal memory O(k), but limited capacity for decomposition or verification.

**Multi-Agent System (MAS).** A Multi-Agent System is an agent system S with |A| > 1, where agents interact through communication topology C and orchestration policy Ω.

Communication topology C defines information flow patterns:

- **Independent**: C = {(aᵢ, aagg) : ∀i} (agent-to-aggregator only, no peer communication)
- **Centralized**: C = {(aₒᵣcₕ, aᵢ) : ∀i} (orchestrator-to-agents only)
- **Decentralized**: C = {(aᵢ, aⱼ) : ∀i, j, i ≠ j} (all-to-all topology)
- **Hybrid**: C = C_centralized ∪ C_peer (orchestrator plus limited peer-to-peer)

The orchestrator Ω (when present) determines: (i) how sub-agent outputs are aggregated (e.g., majority voting, weighted synthesis), (ii) whether the orchestrator can override sub-agent decisions, (iii) whether memory persists across coordination rounds, and (iv) termination conditions based on consensus or quality thresholds.

### 3.2. Agentic Tasks and Benchmarks

Following and extending the framework of Zhu et al. (2025), we operationalize a task T as **agentic** when optimal performance substantially benefits from adaptive interaction. We formalize three necessary properties for agentic benchmarks:

- **Sequential Interdependence**: Later actions depend on earlier observations; a one-shot policy cannot achieve high reward.
- **Partial Observability**: Critical state information is hidden and must be acquired through active querying or tool use.
- **Adaptive Strategy Formation**: The policy must update internal beliefs based on new evidence obtained through interaction.

Benchmarks lacking these conditions (e.g., GSM8K, MMLU) evaluate static reasoning rather than agentic capabilities.

---

## 4. Experiments & Results

### 4.1. Setup

**Benchmarks.** We conducted 180 experiments across four representative benchmarks:

| Benchmark | Task | Evaluation Design |
|---|---|---|
| BrowseComp-Plus (2025) | Web Browsing / Information Retrieval | Multi-website Information Location |
| Finance-Agent (2025) | Finance | Entry-level Analyst Task Performance |
| Plancraft (2024) | Agent Planning | Minecraft Environment Planning |
| WorkBench (2024) | Planning / Tool Selection | Common business activities |

**LLMs and intelligence Scaling.** We evaluate three LLM families across multiple model sizes, spanning externally standardized Intelligence Index values from 42 to 71:

- **OpenAI**: GPT-5-nano, GPT-5-mini, GPT-5
- **Google**: Gemini 2.0 Flash, 2.5 Flash, 2.5 Pro
- **Anthropic**: Claude Sonnet 3.7, 4.0, 4.5

**Agent Architectures and Complexity.** We tested five coordination topologies:

| Characteristic | SAS | MAS (Independent) | MAS (Decentralized) | MAS (Centralized) | MAS (Hybrid) |
|---|---|---|---|---|---|
| LLM Calls | O(k) | O(nk) + O(1) | O(dnk) + O(1) | O(rnk) + O(r) | O(rnk) + O(r) + O(p) |
| Sequential Depth | k | k | d·n | r | r |
| Comm. Overhead | 0 | 1 | d·n | r·n | r·n·k + p·n |
| Parallelization Factor | 1 | n | n | n | n |
| Coordination | Sequential | Parallel + Synthesis | Sequential Debate | Hierarchical Orchestrator | Hierarchical + Peer Orchestrator |

**Coordination Metrics:**

- **Coordination overhead** O = (T_MAS − T_SAS)/T_SAS × 100%
- **Message density** c (inter-agent messages per reasoning turn)
- **Redundancy rate** R (mean cosine similarity of agent output embeddings)
- **Coordination efficiency** E_c = S/(T/T_SAS)
- **Error amplification** A_e = E_MAS/E_SAS (relative failure probability)

### 4.2. Main Results

**MAS exhibits domain-dependence with architectural variation.**

- **Finance Agent**: Centralized reaches +80.8% (mean 0.631 vs. SAS 0.349), Decentralized achieves +74.5% (0.609), Hybrid reaches +73.1% (0.604).
- **Workbench**: Decentralized achieves +5.7% (0.664 vs. SAS 0.629), while Centralized and Hybrid underperform at -1.2%.
- **BrowseComp-Plus**: Decentralized achieves +9.2% (0.347 vs. SAS 0.318); Centralized essentially flat at +0.2%.
- **PlanCraft**: Universal degradation — Centralized to −50.3% (0.282 vs. SAS 0.568), Decentralized to −41.5% (0.332), Hybrid to −39.1% (0.346), Independent to −70.1% (0.170).

Aggregating across all benchmarks and architectures, the overall mean MAS improvement is −3.5% (95% CI: [−18.6%, +25.7%]), reflecting substantial performance heterogeneity with high variance (σ = 45.2%).

**Domain Complexity Moderates Coordination Efficacy.** Mixed-effects regression confirms domain complexity as a significant negative moderator of MAS advantage (β̂ = −0.114, 95% CI: [−0.186, −0.042], p = 0.002). A critical complexity threshold exists at D ≈ 0.40. Below this threshold, multi-agent architectures yield net positive returns. Above this threshold, coordination overhead consumes computational resources otherwise allocated to reasoning.

**Architecture-LLM Family Interactions Reveal Vendor-Specific Coordination Mechanisms.** No single architecture dominates across all domains and vendors. Finance Agent benefits most from Centralized (+80.9%) and Decentralized (+74.5%), Workbench from MAS-Decentralized (+5.6%), and BrowseComp-Plus from MAS-Decentralized (+9.2%). In degrading architectures, Anthropic models show maximum -54.5% (MAS-Hybrid 0.31 vs. SAS 0.68).

### 4.3. Scaling Principles

**Mixed-Effects Model Achieves 52.4% Cross-Validated Variance Explanation.** We fit a scaling principle to all 180 configurations relating agentic system performance to four categories of predictors: 1) base model capability (intelligence index I), 2) system configuration (agent count n_a), 3) task properties (tool count T, single-agent baseline P_SA), and 4) empirically measured coordination metrics (efficiency E_c, overhead O%, error amplification A_e, message density c, redundancy R).

The complete functional form is:

```
P = β₀ + β₁(I − Ī) + β₂(I − Ī)² + β₃log(1 + T) + β₄log(1 + n_a)
  + β₅log(1 + O%) + β₆c + β₇R + β₈E_c + β₉log(1 + A_e)
  + β₁₀P_SA + β₁₁(I × E_c) + β₁₂(A_e × P_SA)
  + β₁₃(O% × T) + β₁₄(R × n_a) + β₁₅(c × I)
  + β₁₆(E_c × T) + β₁₇(P_SA × log(1 + n_a))
  + β₁₈(I × log(1 + T)) + β₁₉(A_e × T) + ε
```

Key coefficient table (Table 4):

| Predictor | β̂ | 95% CI | p | Interpretation |
|---|---|---|---|---|
| Intelligence (I − Ī) | 0.171 | [0.070, 0.272] | 0.001 | Linear capability effect |
| log(1 + T) | 0.411 | [0.291, 0.531] | <0.001 | Tool diversity benefit |
| Single-Agent Baseline (P_SA) | 0.315 | [0.185, 0.445] | <0.001 | Task difficulty proxy |
| P_SA × log(1 + n_a) | −0.404 | [−0.557, −0.252] | <0.001 | **Baseline paradox** |
| E_c × T | −0.267 | [−0.355, −0.178] | <0.001 | **Efficiency-tools trade-off** |
| O% × T | −0.162 | [−0.241, −0.083] | <0.001 | **Overhead scales with task complexity** |
| R × n_a | 0.047 | [0.019, 0.075] | 0.001 | Redundancy benefit with scale |

Cross-validated performance: R²_CV = 0.524 (±0.033 SD), MAE = 0.089, RMSE = 0.112.

**Three critical interactions identified:**

1. **Tool-coordination trade-off** (β̂ = −0.267, p < 0.001): tool-heavy tasks suffer disproportionately from multi-agent inefficiency. Single-agent systems achieve E_c = 0.466, while multi-agent architectures range from E_c = 0.074 (hybrid) to E_c = 0.234 (independent), a 2–6× efficiency penalty.

2. **Capability Ceiling** (β̂ = −0.404, p < 0.001): tasks where single-agent performance already exceeds 45% accuracy experience negative returns from additional agents. The decision boundary between SAS and MAS: P*_SA ≈ 0.45 after denormalization. This threshold achieves 87% correct architecture selection on held-out configurations.

3. **Overhead Scales Non-Linearly with Task Complexity** (β̂ = −0.162, p < 0.001): multi-agent architectures incur substantial overhead — independent (58%), centralized (285%), decentralized (263%), and hybrid (515%) — representing 1.6–6.2× token budgets relative to single-agent.

**The Scaling Principle Enables Quantitative Architecture Selection.** Three task archetypes:
1. *Planning tasks* (T = 4, P_SA = 0.57): favor single-agent due to baseline paradox and low tool count
2. *Analysis tasks* (T = 5, P_SA = 0.35): favor centralized multi-agent, balancing error control with manageable overhead
3. *Tool-heavy tasks* (T = 16, P_SA = 0.63): favor decentralized multi-agent despite high overhead (263%), because parallelization and redundancy outweigh efficiency losses

### 4.4. Coordination Efficiency, Error Dynamics, and Information Transfer

**Coordination Metrics Across Architectures** (n = 180 configurations, 15,750 total instance runs):

| Metric | SAS | Independent | Decentralized | Centralized | Hybrid |
|---|---|---|---|---|---|
| Success Rate (S) | 0.466 | 0.370 | 0.477 | 0.463 | 0.452 |
| Turns (T) | 7.2±2.1 | 11.4±3.2 | 26.1±7.5 | 27.7±8.1 | 44.3±12.4 |
| Overhead (O%) | 0 | 58 | 263 | 285 | 515 |
| Error Amp (A_e) | 1.0 | 17.2 | 7.8 | 4.4 | 5.1 |
| Success/1K tokens | 67.7 | 42.4 | 23.9 | 21.5 | 13.6 |

**Turn count follows power-law scaling with number of agents:**
T = 2.72 × (n + 0.5)^1.724, R² = 0.974, p < 0.001

**Message Density Exhibits Logarithmic Saturation with Performance:**
S = 0.73 + 0.28 ln(c), R² = 0.68, p < 0.001

Performance plateaus near c* = 0.39 messages/turn. Beyond this point, additional messages yield diminishing returns.

**Error Absorption Mechanisms.** Architectures with verification (Centralized, Decentralized, Hybrid) achieve 22.7% average error reduction (95% CI: [20.1%, 25.3%]), peaking at 31.4% for Finance Agent. Independent MAS shows no error correction (+4.6% amplification) due to absence of any inter-agent verification mechanism.

**Error Taxonomy — Four categories:**
1. *Logical Contradiction*: Centralized reduces to 9.1% (36.4% reduction); Decentralized achieves 11.5%; Independent unchanged at 16.8%.
2. *Numerical Drift*: Centralized/Decentralized reduce to 18.3% (24% reduction); Hybrid amplifies to 26.4% as rounding errors propagate.
3. *Context Omission*: Centralized reduces to 8.3% (66.8% reduction); Decentralized achieves 11.2%; Independent unchanged at 24.1%.
4. *Coordination Failure*: Only in MAS. Independent: 0%; Centralized: 1.8%; Decentralized: 3.2%; Hybrid: 12.4%.

**Three operational coordination regimes identified:**
- **Under-coordination** (O < 100% overhead): minimal accuracy gain (ΔS ≈ +2–4%)
- **Optimal band** (200% < O < 300% overhead): highest success–cost ratio (E_c ≈ 0.16)
- **Over-coordination** (O > 400% overhead): reduced efficiency (E_c ≈ 0.11), coordination-failure modes

**Agent Heterogeneity Effects.** In centralized architectures, configurations with high-capability sub-agents outperform those with high-capability orchestrators across all model families, suggesting sub-agent capability matters more than orchestrator capability. Anthropic models uniquely benefit from heterogeneous mixing: low-capability orchestrator with high-capability sub-agents (0.42) outperforms homogeneous high-capability (0.32) by 31%.

---

## 5. Limitations and Future Works

(i) Framework compares canonical coordination structures with preliminary exploration of scaling number of agents up to nine. Scaling to larger collectives may face fundamental barriers as communication overhead grows superlinearly.
(ii) All agents share identical base architectures differing only in scale and role prompts; future work should investigate teams combining fundamentally different model architectures.
(iii) Tool-heavy environments represent a primary failure mode; specialized coordination protocols for tool-intensive tasks represent an important direction.
(iv) Controlled prompts were identical across conditions for experimental validity, not optimized per model family.
(v) Analysis spans four agentic benchmarks; novel task structures (embodied agents, multi-user interaction, long-horizon temporal dependencies) would strengthen confidence.
(vi) Economic viability of multi-agent scaling: token consumption and latency grow substantially with agent count, often without proportional performance gains.

---

## 6. Conclusion

This study quantifies scaling principles for agentic systems across 180 controlled experiments spanning three LLM families and four agentic benchmarks. We reveal that multi-agent performance is governed by quantifiable trade-offs: a tool-coordination trade-off where tool-heavy tasks suffer from coordination overhead, capability saturation where coordination yields diminishing returns beyond ~45% single-agent baselines, and architecture-dependent error amplification ranging from 4.4× (centralized) to 17.2× (independent). Performance gains vary dramatically by task structure, from +80.9% on Finance Agent to −70.0% on PlanCraft, demonstrating that coordination benefits depend on task decomposability rather than team size. We derive a predictive model (R²=0.524) that achieves 87% accuracy in selecting optimal architectures for held-out configurations. Out-of-sample validation on GPT-5.2, released after our study, confirms that four of five scaling principles generalize with MAE=0.071. These results provide practitioners with quantitative guidance for architecture selection based on measurable task properties.

---

## Appendix A. Model Intelligence Index

The study adopts the *Artificial Analysis Intelligence Index*, combining performance across reasoning, knowledge, mathematics, coding, instruction following, long-context reasoning, and agentic workflow tasks. Models used (Intelligence Index range 42–71):

| Model | Index |
|---|---|
| GPT-5.2 | 75 |
| GPT-5 | 71 |
| GPT-5 mini | 68 |
| GPT-5 nano | 59 |
| Gemini-2.5 Pro | 65 |
| Gemini-2.5 Flash | 58 |
| Gemini-2.0 Flash | 47 |
| Claude 4.5 Sonnet | 55 |
| Claude 4.0 Sonnet | 47 |
| Claude 3.7 Sonnet | 42 |

## Appendix B. Out-of-Sample Validation

GPT-5.2 (Intelligence Index = 75, released after the study) validation on BrowseComp-Plus:

| Metric | Value | Status |
|---|---|---|
| Mean Absolute Error (MAE) | 0.071 | < 0.10 ✓ |
| MAPE | 15.8% | Acceptable |
| Qualitative Findings Validated | 4/5 | Partial |

Four of five scaling principles generalize: capability ceiling, Independent MAS degradation, Centralized/Decentralized optimal architecture, and Hybrid overhead degradation. The BrowseComp pattern (Decentralized > Centralized) showed partial validation only, with both architectures converging at 0.48 for GPT-5.2.

## Appendix C. Domain Complexity

Domain complexity D ∈ [0, 1] is computed as the arithmetic mean of: Performance Ceiling (1 − p_max), Coefficient of Variation (σ/μ), and Best-Model Baseline (1 − p_best).

| Domain | D | Characteristics |
|---|---|---|
| Workbench | 0.000 | Minimal sequential constraints; well-structured procedural reasoning |
| Finance Agent | 0.407 | Moderate decomposability; structured domains amenable to localised agent reasoning |
| PlanCraft | 0.419 | High sequential dependencies; constraint satisfaction requiring ordered reasoning steps |
| BrowseComp-Plus | 0.839 | Dynamic state evolution; complex visuospatial reasoning with interaction-heavy environments |

Critical threshold at D ≈ 0.40: below this, MAS yield net positive returns through effective task decomposition and parallel reasoning; above this, coordination overhead dominates.

## Appendix E. Implementation Details

- **Infrastructure**: LiteLLM for unified API access; LangChain for agent orchestration and tool integration.
- **APIs**: OpenAI API (GPT models), GenAI API (Gemini models), Anthropic API (Claude models).
- **Tools**: Web search (Tavily), code execution (Python REPL), mathematical operations, task completion markers.
- **Architecture Parameters**: Single agents use maximum 10 iterations per instance. Independent MAS deploy 3 agents with synthesis-only coordination. Centralized systems employ 3 sub-agents with 1 orchestrator across maximum 5 orchestration rounds, with 3 iterations per agent per round. Decentralized systems run 3 agents through 3 debate rounds with 3 iterations per round.
- **Mean token budget**: 4,800 tokens per trial across all configurations.
