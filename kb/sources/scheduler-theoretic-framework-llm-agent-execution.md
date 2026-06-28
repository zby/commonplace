---
source: https://arxiv.org/html/2604.11378v1
description: Position paper recasting the Agent Loop as a single-ready-unit scheduler and proposing Graph Harness (SGH) — a static-DAG execution model with immutable plan versions, three-layer separation, and bounded three-level recovery.
captured: 2026-06-28
capture: manual-paste
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution

Author: Hu Wei (1990huwei@sina.com)
Source: https://arxiv.org/html/2604.11378v1

## Abstract

The dominant paradigm for building LLM-based agents is the Agent Loop—an iterative cycle where a single language model decides what to do next by reading an ever-growing context window. This paradigm has three structural weaknesses: implicit dependencies between steps, unbounded recovery loops that may retry indefinitely, and mutable execution history that makes debugging difficult. We characterize the Agent Loop as a single-ready-unit scheduler: at any instant, at most one executable unit is active, and the choice of which unit to activate is the output of an opaque LLM inference rather than an inspectable policy. This characterization lets us place Agent Loops and graph-based execution engines on a single semantic continuum.

We propose Graph Harness (Structured Graph Harness), which lifts the control structure from implicit context into an explicit static DAG. Graph Harness makes three design commitments: an execution plan is immutable for the duration of a plan version; planning, execution, and recovery are separated into three independent layers; and recovery follows a strict escalation protocol. These commitments trade some expressiveness for controllability, verifiability, and implementability.

Our contributions are fourfold: a scheduler-unified framework that applies classical scheduling theory to LLM agent execution, identifying the specific challenges introduced by non-deterministic LLM nodes; a trade-off analysis of controllability, expressiveness, and implementability across 70 surveyed systems; a formal specification including a node state machine with proven termination and soundness guarantees; and an attributable experimental framework with a seven-group design for future empirical validation.

This is a position paper and design proposal. We contribute a theoretical framework, a design analysis, and an experimental protocol—not a production implementation or empirical results. The design has been verified for internal consistency and state-machine completeness; engineering details and experimental validation are left to future work.

## 1 Introduction

LLM agents autonomously decompose tasks, invoke tools, and iterate. The dominant paradigm is the Agent Loop: an iterative cycle of reasoning, acting, and observing where a single LLM decides what to do next by reading an ever-growing context window. Despite its simplicity and widespread adoption, this paradigm has three structural weaknesses:

First, dependencies between steps are implicit and unverifiable. The fact that "run tests" depends on "modify code" exists only in the context window; there is no structural guard against out-of-order execution. Second, failure recovery has no bounded semantics — the LLM autonomously decides whether to retry, skip, or replan, with no explicit contract and no bound on attempts. Third, the execution plan can be silently rewritten; after execution it is impossible to reconstruct a faithful audit trail of which plan governed which actions.

Analysis of 70 open-source LLM agent projects reveals that 60% (42 out of 70) adopt the Agent Loop pattern. Recent enhancements (planner-augmented loops, graph-structured orchestration, multi-agent decomposition) improve specific aspects but do not fundamentally address the structural problem: the control flow remains implicit, and execution lacks a stable commitment.

The Agent Loop is, at its core, a single-ready-unit scheduler: at any point at most one executable unit is active, and the choice of next unit is the output of an opaque LLM inference. The key parameter is the ready-set cardinality — how many units are simultaneously eligible for dispatch — and policy explicitness — how deterministic and inspectable the scheduling decision is.

Graph-based executors can dispatch multiple nodes simultaneously, enabling **parallel execution** and **alternative paths**. Two forms of parallelism are distinguished: **constructive parallelism**, where all branches must complete (e.g., reading two files in parallel), and **competitive parallelism**, where only one branch is needed and the rest can be cancelled (e.g., trying two fixes and stopping after one succeeds). SGH supports constructive parallelism but excludes competitive parallelism for controllability reasons.

**Relationship to classical scheduling theory.** The formalization of execution systems as tuples (𝒮, 𝒰, 𝒫, 𝒪, Δ) builds on classical DAG scheduling literature (Topcuoglu et al., 2002; Cormen et al., 2009). What is novel is its application to LLM agent execution and the identification of LLM-specific challenges (non-deterministic node output, semantic validation, reasoning errors) that classical schedulers do not address.

Graph Harness makes three design commitments: (1) an execution plan is an immutable commitment for the duration of a plan version; (2) planning, execution, and recovery are separated into three independent layers with well-defined interfaces; and (3) recovery actions follow a strict escalation protocol that prevents unbounded replanning. These deliberately trade some expressiveness — competitive parallelism, recursive sub-graph expansion, and parent-chain rollback are excluded — for controllability, verifiability, and implementability.

Contributions:
- A scheduler-theoretic framework characterizing LLM agent execution systems as schedulers parameterized by ready-set cardinality (|𝒰|) and policy explicitness, generating testable hypotheses about performance gains.
- A four-principle design methodology derived from 70 surveyed systems, characterizing trade-offs between controllability, expressiveness, and implementability.
- A formal execution model with three-layer separation, immutable plan versioning, and a node state machine with proven termination and soundness guarantees under explicit fairness assumptions.
- A seven-group experimental protocol that isolates the contribution of each design decision (G_plan, G_scaffold, G_graph, G_patch, G_replan).

**Scope.** Theoretical framework, design analysis, and experimental protocol — not a production implementation or empirical results.

**A motivating example.** A bug-fix task: search two modules in parallel, read both, analyze the root cause, try either of two alternative patches, run tests, update documentation, and generate a report (Figure 1). In an Agent Loop, all steps execute serially (11 turns), recovery from a failed patch is ad-hoc, and there is no structural guard ensuring analysis waits for both files. In Graph Harness the same task takes 6 scheduling rounds: the two searches and two reads dispatch in parallel (|𝒰|=2), the two patches and the documentation update proceed concurrently (|𝒰|=3), and the any_of join selects whichever patch succeeds first while skipping the alternative. The parallelism, dependency tracking, and bounded recovery are structural properties of the DAG, not LLM decisions. The example assumes ideal conditions: the planner correctly identifies all parallel structure, dependencies are fully known at planning time, and the LLM executes each node correctly.

## 2 Related Work

**2.1 Agent Loop Paradigm.** The iterative observe–reason–act loop originates in ReAct (Yao et al., 2023). Chain-of-Thought (Wei et al., 2022) and Plan-and-Solve (Wang et al., 2023) extended it. ~60% of 70 surveyed projects use some variant of the iterative tool loop. All Agent Loop systems share |𝒰|=1 at every step; the scheduling policy is the LLM itself — a non-deterministic, non-interpretable black box.

**Graph Harness's novel contributions** vs. prior work: (1) a scheduler-theoretic framework making the expressiveness/controllability trade-off formal; (2) deliberately restricting expressiveness (no first_of, no recursive expansion, no dynamic topology) to maximize controllability and verifiability; (3) systematically addressing LLM-specific challenges (non-deterministic output, reasoning failures as primary error mode, non-idempotent retry).

**2.2 Plan-Then-Execute and Separated Architectures.** Plan-and-Act (Erdogan et al., 2025) trains a dedicated Planner and Executor. Routine (Zeng et al., 2025) introduces structured planning scripts, improving multi-step tool-calling accuracy from 41% to 96% in enterprise settings. Task-Decoupled Planning (TDP) (Li et al., 2026) decomposes tasks into a DAG of sub-goals with scoped contexts, reducing token consumption by up to 82%. In SGH's framework, these remain single-ready-unit schedulers (|𝒰|=1): the plan guides execution but does not create multiple simultaneously dispatchable units.

**TDP in detail** is the closest existing system. Three key differences: (1) Ready-set cardinality — TDP executes one sub-task at a time; SGH dispatches all dependency-satisfied nodes concurrently. (2) Plan stability — TDP allows dynamic sub-task graph modification; SGH enforces plan-version immutability. (3) Recovery — TDP replans at the sub-task level without a formal escalation protocol; SGH requires exhausting lower-level recovery (retry, then local patch) before permitting full replan, preventing the "failure loop" pathology.

**2.3 LLM-Based Workflow Optimization.** AutoGen (Wu et al., 2023) introduces conversational agents with role-based message routing but lacks explicit DAG scheduling and structured recovery. CrewAI (Moura & crewAI Inc., 2024) implements hierarchical task assignment; recovery is ad-hoc. Semantic Kernel (Microsoft, 2023) introduces a planner-executor pattern with composable skills but focuses on skill composition. These remain primarily single-ready-unit schedulers with implicit or semi-deterministic policies.

**2.4 Graph-Based Agent Orchestration.** GPTSwarm (Zhuge et al., 2024) represents agents as computational graphs with optimizable edges. AgentKit (Wu et al., 2024) provides graph-based prompt composition. AFlow (Zhang et al., 2025b) models workflows as graphs using Monte Carlo Tree Search. AGORA (Zhang et al., 2025c) unifies language agent algorithms with a graph-based orchestration engine, showing simpler methods like CoT often perform robustly with lower overhead.

**LangGraph** (Team, 2024) is the most widely adopted graph-based agent framework: parallel node execution (fan-out/fan-in), conditional edges, state channels, and runtime graph modification. In SGH's framework, LangGraph is a multi-ready-unit scheduler with a semi-deterministic 𝒫 — topology constrains parallelism, but conditional-edge routing is determined by LLM output at runtime, making the effective policy non-deterministic. The differences are philosophical rather than structural: LangGraph prioritizes flexibility (dynamic restructuring, LLM-judgment routing); SGH prioritizes controllability (plan-version immutability, escalation protocol). A fairness disclaimer notes LangGraph is mature and production-grade; SGH is unimplemented, and the comparison is structural, not evaluative.

A survey by Liu et al. (2025) categorizes graph-augmented LLM agents by function and identifies open challenges including structural adaptability. Yue et al. (2026) introduce Agentic Computation Graphs (ACGs), distinguishing static templates from dynamic runtime graphs and execution traces.

**2.5 Multi-Agent Task Decomposition and Scheduling.** AOP (Li et al., 2025) proposes agent-oriented planning with solvability, completeness, and non-redundancy. DynTaskMAS (Yu et al., 2025) introduces dynamic task graphs with asynchronous parallel execution, achieving 21–33% reduction in execution time. Graph-of-Agents (Yun et al., 2025) models multi-agent communication as a directed graph. G-Designer (Zhang et al., 2025a) designs task-aware topologies using variational graph auto-encoders. WorfBench (Qiao et al., 2025) reveals a 15% gap between sequence planning and graph planning even in GPT-4. SGH takes the opposite stance to these flexible-topology systems: fixing the topology for the duration of a plan version provides controllability guarantees dynamic systems cannot.

**2.6 Structured Execution for Scientific Agents.** El Agente Gráfico (Bai et al., 2026) embeds LLM decision-making within type-safe execution graphs and knowledge graphs for scientific workflows, supporting the thesis that structured execution infrastructure matters more than agent count.

**2.7 Classical DAG Scheduling.** List scheduling, topological ordering, and critical-path analysis (Topcuoglu et al., 2002; Cormen et al., 2009) are the foundations SGH builds on. The contribution is identifying that the same formal tools apply to LLM agent execution, with specific treatment of non-deterministic LLM nodes. The topological scheduling policy is equivalent to list scheduling with zero communication costs, which achieves a 2−1/m approximation ratio for m identical processors (Graham, 1969).

**2.8 Workflow Engines: Airflow, Luigi, Prefect.** These share static DAG definitions, topological scheduling, and retries with SGH. The fundamental difference: SGH's nodes are non-deterministic — the same node with the same inputs may produce different outputs. SGH adds three mechanisms with no analogue in classical engines: (1) contract-based output validation with explicit pass/fail semantics; (2) a three-level recovery protocol distinguishing transient errors from reasoning failures; (3) execution/diagnostic context separation that prevents failure history from corrupting subsequent reasoning.

**2.9 Systematic Comparison.** SGH is the only LLM agent system that simultaneously enforces all four core constraints: multi-ready-unit scheduling, deterministic policy, bounded recovery, and immutable plan versions. LangGraph achieves multi-ready-unit scheduling but lacks the other three. TDP achieves plan-structure but remains single-ready-unit. Classical workflow engines meet the constraints but their nodes are deterministic and they lack contract validation and LLM-specific recovery. SGH is positioned for engineering tasks with verifiable outcomes.

**2.10 Positioning.** SGH simultaneously enforces three properties as mandatory constraints: (1) multi-ready-unit scheduling with a deterministic policy, (2) immutable plan versions as execution commitments, and (3) a bounded recovery protocol with escalation invariants. Each property exists in isolation in prior work; their combination and the design tensions from enforcing them jointly are the contributions.

## 3 A Scheduler-Unified Framework

**3.1 Execution Systems.** *Definition 3.1.* An execution system is a tuple ℰ = (𝒮, 𝒰, 𝒫, 𝒪, Δ) where:
- 𝒮 = {(v, s_v) | v ∈ V, s_v ∈ Σ} is the set of node states (V = nodes, Σ = node state set);
- 𝒰: 𝒮 → 2^V maps a global state to the ready set: 𝒰(𝒮) = {v ∈ V | s_v = ready ∧ ∀(u,v) ∈ E: s_u = executed}. A node becomes ready when all predecessors have executed;
- 𝒫: 2^V → V is the scheduling policy — a deterministic function selecting a single node from the ready set. In non-deterministic systems, 𝒫 is a relation rather than a function;
- 𝒪 = {success, failure, retry, escalate} is the outcome space;
- Δ: 𝒮 × V × 𝒪 → 𝒮 is the state transition function that updates node state and recomputes 𝒰(𝒮′).

Using a relation rather than a function for 𝒫 lets the framework encompass both deterministic and non-deterministic schedulers. The Agent Loop falls into the latter.

**3.2 Single-Ready-Unit Schedulers.** *Definition 3.2.* ℰ is a single-ready-unit scheduler if at every reachable state |𝒰(s)| ≤ 1. When |𝒰| ≤ 1, 𝒫 becomes vacuous. **Observation: The Agent Loop is a non-deterministic, single-ready-unit scheduler** — at each step the LLM produces exactly one action (|𝒰|=1), but the same context may yield different actions (𝒫 not functional).

*Parallel tool calls* (e.g., OpenAI tool_calls with multiple concurrent functions) correspond to |𝒰|>1 but with non-deterministic 𝒫 — the set is determined by the LLM, not an explicit policy. SGH's advantage is not merely parallelism but **explicit parallelism**: the ready set is computed from DAG topology, and parallel dispatch is guaranteed whenever dependencies allow. *Asynchronous operations* are similarly ad-hoc — the LLM decides what to parallelize.

**3.3 Multi-Ready-Unit Schedulers.** *Definition 3.3.* ℰ is a multi-ready-unit scheduler if there exists a reachable state with |𝒰(s)| > 1. The scheduling relation becomes a genuine design decision; this is the regime of graph-based executors.

**3.4 The Scheduler Continuum.** Execution systems arrange along a continuum with three axes: (1) ready-set cardinality (|𝒰|=1 vs |𝒰|≥1); (2) policy explicitness (implicit / prompt-level / state-machine); (3) policy determinism (non-deterministic relation vs deterministic function). This is a classification framework, not a theorem.

*Theoretical predictions* (untested, to guide future work): (1) G_graph > 0 — moving from single- to multi-ready-unit scheduling yields a measurable benefit independent of planning quality; (2) G_graph increases with task complexity; (3) G_replan > 0 specifically on failure-prone tasks. These are logical consequences of the framework's assumptions, not empirically validated claims.

Figure 2's continuum (left to right): Naive Loop (|𝒰|=1, non-det) → Parallel Loop (|𝒰|≥1, non-det) → Planner Loop (|𝒰|=1, non-det) → Structured Loop (|𝒰|=1, semi-det) → Graph Harness (|𝒰|≥1, det). "Adding a planner to the loop" moves along the policy-explicitness axis but does not change ready-set cardinality. Only a graph-based executor reaches the multi-ready-unit regime.

**3.5 Why Unification Matters.** Three analytical benefits: *Comparability* — the question "is a graph executor better than an Agent Loop?" becomes "does moving from |𝒰|=1 to |𝒰|≥1 with deterministic 𝒫 improve performance, and by how much?" *Expressiveness characterization* — the range of ready-set configurations a system can produce; a single-ready-unit scheduler cannot represent concurrent, conditional, or fallback execution. *Controllability characterization* — the degree to which 𝒫 is functional and 𝒮 is explicit. The framework also provides only a **semantic** classification, not yet complexity-theoretic guarantees (e.g., it does not prove optimal scheduling under budget constraints is NP-hard, though this is likely).

**3.6 Worked Example.** A ten-step bug-fix task (search_auth, search_utils, read_auth, read_utils, analyze, fix_A, fix_B, run_tests, update_docs, report). analyze depends on read_auth AND read_utils (all_of); run_tests depends on fix_A OR fix_B (any_of); report depends on run_tests AND update_docs (all_of).

*Agent Loop execution* (11 turns, all sequential): searches done serially (no parallelism), one fix tried then another after failure (no structured alternatives), recovery unbounded and ad-hoc, dependencies implicit through context, no plan versioning.

*Graph Harness execution* (10 node dispatches across 6 scheduling rounds): Ready-set {search_auth, search_utils} |U|=2 parallel; {read_auth, read_utils} |U|=2 parallel; {analyze} |U|=1; {fix_A, fix_B, update_docs} |U|=3 — fix_A FAILED (transient), fix_B executed, update_docs executed in parallel, fix_A's Level 1 recovery skipped because any_of already satisfied; {run_tests} |U|=1; {report} |U|=1. Five structural differences: parallel execution, structured alternatives, bounded recovery, explicit dependencies, auditability. Wall-clock reduced proportionally to available parallelism.

**3.7 Planning Failures and Their Consequences.** The worked example assumes a perfect DAG. Planning can fail in five ways: *Missing dependencies* — manifests as a contract violation at runtime (caught). *Spurious dependencies* — restricts parallelism, reduces |𝒰|; not detected, costs wasted time not correctness. *Incorrect branch selection* (all_of instead of any_of) — particularly damaging; system retries failing patch through all recovery levels. *Over-decomposition* — too many fine-grained nodes, coordination overhead. *Under-decomposition* — lumps operations, missing parallelism and making error attribution hard. SGH handles failures via structural validation, contract validation, and the recovery protocol, but cannot fix spurious dependencies, incorrect branch selection, or mis-granular decomposition without a new plan version.

## 4 Design Principles and Trade-offs

Three competing goals: **controllability** (predictability, verifiability, auditability), **expressiveness** (range of task structures), and **implementability** (engineering complexity and risk).

**4.1 The Trade-off Space.** Survey of 70 projects classifies by primary execution pattern: Agent Loop (|𝒰|≤1, non-det 𝒫), Event-driven (|𝒰|≤1, externally triggered Δ), State-machine (|𝒰|≤1, semi-explicit 𝒫), Graph/flow (|𝒰|≥1, explicit 𝒫), Hybrid. Systems with the highest expressiveness (graph/flow) consistently exhibit the lowest controllability and highest implementation risk. SGH deliberately targets a point that is *not* at the expressiveness frontier — maximizing controllability while retaining enough expressiveness for verifiable engineering tasks.

**4.2 Principle 1: Controllability First.** In the face of uncertain benefit, prioritize predictability and verifiability. *Rationale from survey:* failure-loop behavior was frequently observed among graph/flow systems (3 of 4) but rarely in state-machine systems (0 of 7) — a qualitative, not formally quantified, observation. *Sacrificed:* competitive parallelism (first_of), recursive sub-graph expansion, parent-chain rollback.

**4.3 Principle 2: Stable Execution Commitment.** Once generated and validated, plan structure must not be modified during execution. *Rationale:* versioned-history systems appeared to support more effective debugging than mutable-history systems (subjective assessment). An immutable plan-version is the minimal unit of accountability. *Sacrificed:* dynamic add/remove of nodes, edge redirection, mid-flight rewrites — any structural change requires a new plan version via controlled replan.

**4.4 Principle 3: Bounded Recovery.** Recovery actions must have explicit triggers, bounded scope, and strict escalation. *Rationale:* Agent Loops commonly lack formal bounds, producing either infinite retry loops or premature abandonment. *Sacrificed:* recovery decisions decoupled from execution loop; cannot skip from transient error directly to full replan.

**4.5 Principle 4: Side-Effect Classification.** Units classified by side-effect profile; scheduling respects classification. A read-only call can be freely retried; a database write cannot. *Sacrificed:* high side-effect operations (writes, deletions, notifications) face stricter scheduling — no speculative parallel dispatch, tighter retry budgets.

**4.6 Summary.** The sum of sacrifices defines SGH's expressiveness boundary — claimed appropriate for verifiable engineering tasks, not universal.

## 5 Execution Commitment and the Static Graph Model

**5.1 The Execution Plan as Commitment.** *Definition 5.1.* An execution plan is Π = (id, version, V, E, σ, κ) where E ⊆ V×V, σ: V → NodeConfig (action, retry policy, side-effect level), and κ is an output contract. *Definition 5.2 (Plan Invariant):* for the lifetime of plan version v, structure (V, E) is immutable; the only mechanism for a different structure is creating version v+1 via the replan protocol. Three consequences: attributability, predictability, verifiability.

**5.2 Why a Static DAG?** A DAG guarantees by construction: no circular dependencies (acyclicity ensures progress), finite execution (fixed node count bounds steps), topological scheduling (a canonical schedule the policy may refine but never violate). Three alternatives (cyclic graph, dynamic graph, tree) were considered and rejected for the target task class.

**5.3 Three-Layer Separation.** *Planner Layer:* receives task intent, produces a validated static DAG Π satisfying the plan invariant (may be LLM, template-based, or hybrid). *Runtime Layer:* executes Π without modifying (V,E); maintains per-node state, computes ready set, applies 𝒫, records observations; reports failures but does not decide how to handle them. *Recovery Layer:* receives failure reports, diagnoses root cause, selects a recovery action based on a diagnostic context invisible to the runtime's execution context.

**5.4 Context Separation.** *Definition 5.3 (Context Partition):* two disjoint contexts — Execution context 𝒞_exec (inputs, visible artifacts, runtime state, budget; accessible to nodes during execution) and Diagnostic context 𝒞_diag (failure history, planner annotations, prior plan versions; accessible only to recovery and planner layers). Constraint: 𝒞_exec ∩ 𝒞_diag = ∅ during node execution. Diagnostic information enters 𝒞_exec only through the planner (as a new plan version). This prevents using failure history as implicit input to subsequent steps.

## 6 Node State Machine and Recovery Protocol

**6.1 Node State Machine.** *Definition 6.1:* Σ = {pending, ready, running, waiting_human, blocked, executed, failed_retryable, failed, cancelled, skipped}. Terminal states Σ_term = {executed, failed, cancelled, skipped}. *Definition 6.2 (Bounded Execution):* each node has timeout τ_v ∈ ℝ⁺ and retry budget b_v ∈ ℕ; waiting_human has finite timeout T_human. Execution transitions running → failed if elapsed time > τ_v OR retries > b_v. running → failed_retryable on transient errors (network timeout, rate limit); running → failed on structural errors (missing dependencies, invalid plan).

*Terminal stability:* terminal states are absorbing — no outgoing transitions — essential for ready-set correctness.

*Proposition 6.1 (Progress Guarantee):* if at least one node is non-terminal, either a transition to ready or a transition to a terminal state is enabled. (Proof via acyclicity + finiteness: there always exists a node whose predecessors are all terminal.)

*Theorem 6.2 (Bounded Termination):* given a valid DAG (finite, acyclic, all nodes reachable) under bounded execution with finite τ_v and b_v, the SGH main loop terminates with probability 1. Total time bound ≤ Σ_v τ_v·(b_v+1) + Σ (waiting_human) T_human(v).

*Contract validation semantics:* running → executed is guarded by contract validation — a node can only enter executed if its output satisfies κ_v; otherwise it transitions to failed_retryable or failed.

*Theorem 6.3 (Conditional Soundness under Validation Reliability):* let p_v ∈ (0,1] be the probability node v's contract validation correctly identifies a passing output. If all nodes reach executed and validation errors are independent, Pr[all outputs correct] ≥ ∏_v p_v. This is the **validation gap**: even when all nodes pass validation, correctness is bounded by validation reliability. Syntactic validation (code) has p_v ≈ 1; semantic validation (especially LLM-based) may be significantly below 1. Mitigations: side-effect classification requires high-impact nodes to use code-based validation; waiting_human allows human review; the recovery protocol catches validation errors at the next dependency boundary. The validation gap is inherent to any LLM-based execution system; SGH makes it observable and controllable but does not eliminate it.

**6.2 Three-Level Recovery Protocol.** *Definition 6.3:* ℛ = {local_retry} (Level 1) ∪ {local_patch} (Level 2) ∪ {request_replan} (Level 3). *Proposition 6.4 (Escalation Invariant):* Level i must be exhausted before Level i+1 may be invoked; skipping levels is prohibited. *Mechanical enforcement:* a per-node counter recovery_state[v] ∈ {pristine, retried, patched}. Three entry points: attempt_retry(v), attempt_patch(v, cfg), request_replan(reason). attempt_patch is rejected unless recovery_state[v] ≥ retried; request_replan is rejected unless all failed nodes have recovery_state ≥ patched. Implementations that bypass the API fall outside SGH's guarantees (analogous to unsafe blocks).

**6.3 Error Classification and Diagnosis.** *Definition 6.4:* a diagnosis is d = (φ, c, r, α): observed failure φ, root-cause hypothesis c, recommended recovery r ∈ ℛ, diagnostic confidence α ∈ [0,1]. The diagnoser operates on 𝒞_diag, not 𝒞_exec, so diagnostic reasoning does not leak into the execution path.

## 7 Join Semantics and Scheduling Constraints

**7.1 Supported Join Modes.** *Definition 7.1 (all_of):* node v enters the ready set iff every predecessor reached executed. *Definition 7.2 (any_of):* candidates dispatched in a deterministic total order; v becomes eligible as soon as any candidate reaches executed; remaining non-terminal candidates transition to skipped (sibling skip); if every candidate reaches terminal failure without success, the join fails and v → failed.

**7.2 Impact on the Ready Set.** all_of is the natural join for dependency-satisfying execution. any_of dispatches all candidates in parallel and takes whichever succeeds first — the natural join for alternative-path execution.

**7.3 The first_of Exclusion.** first_of would enable **speculative execution**: launch competing approaches, take the first success, cancel the rest. Excluded for two reasons: (1) loser cancellation requires compensation protocols for partial results; (2) commit-point ambiguity (if A succeeds first, should B and C still execute? what if B would be higher quality?). These introduce non-determinism. The concerns are not unsolvable in principle (distributed transaction systems use compensation and consensus) but add complexity and their own failure modes. Competitive parallelism remains a viable future extension.

**7.4 Expressiveness Boundary.** The two supported joins plus the static DAG define the boundary. Each excluded capability corresponds to a specific design-principle violation; the boundary can be pushed outward by relaxing principles, with explicit acknowledgment of the controllability trade-off.

## 8 Attributable Experimental Framework

*(Design of a protocol, not completed results.)*

**8.1 Seven-Group Design.** Each group is a distinct point on the scheduler continuum; adjacent comparisons isolate one feature.
- **G0: SOTA Loop** — state-of-the-art prompt-augmented Agent Loop (e.g., Claude Code, OpenAI Codex agent mode) with planning prompts, self-reflection, tool calling; no DAG; inline replan on failure.
- **G1: Naive Loop** — minimal Agent Loop, no planner/graph/recovery, unbounded retry.
- **G2: Planner Loop** — adds a Planner LLM; execution remains a loop (|𝒰|=1).
- **G3: Structured Loop (|𝒰|=1)** — adds a scaffold enforcing plan adherence; recovery unbounded.
- **G4: GH-Core (|𝒰|≥1, no recovery)** — multi-ready-unit, deterministic policy; recovery unbounded.
- **G5: GH+Patch (|𝒰|≥1, level 1-2 recovery)** — adds retry and patch.
- **G6: GH+Replan (|𝒰|≥1, full recovery)** — adds level 3 replan, completing three-level escalation.

*Controlled variables:* same 50 curated tasks (coding, data analysis, operational); same base model, temperature, max tokens; same tool set; same timeout (e.g., 10 min); same token budget (e.g., 100K). *Measured:* success rate, execution time, token cost, node count, recovery actions, plan versions. *Biases & mitigations:* task selection bias (report task-level results), implementation bias (testing), LLM non-determinism (10 runs/task, report mean±std), tool latency (mock then real), order effects (randomize).

Adjacent isolations: G1−G0 (information vs structure), G2−G1 (planning gain), G3−G2 (scaffold gain), G4−G3 (graph gain), G5−G4 (patch gain), G6−G5 (replan gain), G6−G0 (total gain).

**8.2 Gain Decomposition.** *Definition 8.1:* G_plan = Perf(G2)−Perf(G1); G_scaffold = Perf(G3)−Perf(G2); G_graph = Perf(G4)−Perf(G3); G_patch = Perf(G5)−Perf(G4); G_replan = Perf(G6)−Perf(G5). Total structural gain G_total = G_plan + G_scaffold + G_graph + G_patch + G_replan. If G_graph ≫ G_plan, the primary benefit is scheduler structure not planning. *Limitation:* additive decomposition assumes near-additive contributions; plan×structure interaction can be detected by estimating G_graph at different planning-quality levels.

**8.3 Task Set Design.** Stratified into three tiers by dependency complexity (simple, medium, complex). The simple tier stress-tests the fixed-overhead hypothesis (H4): if SGH overhead dominates on simple tasks, the trade-off may need re-evaluation.

**8.4 Evaluation Metrics.** Effectiveness (success rate, contract satisfaction). Efficiency (LLM calls/task, redundant step ratio, wall-clock). Stability (run-to-run variance, failure-loop rate). Observability (trace completeness, failure localization accuracy). Attribution (the five gain components).

## 9 Discussion

**9.1 The Scheduler Continuum as a Design Lens.** The 2025–2026 literature is converging toward graph-structured execution but from different directions: TDP adds DAG structure to reduce context entanglement; DynTaskMAS adds dynamic task graphs for parallelism; GPTSwarm adds optimizable graphs. All reach the multi-ready-unit regime but none provide the execution commitment and bounded recovery SGH guarantees — a consequence of prioritizing expressiveness over controllability.

**9.2 Relationship to Existing Work.** SGH differs in three aspects: prioritizes controllability over expressiveness; static DAG commitment with explicit plan versioning; formal three-layer recovery with escalation invariants. *When is static DAG superior to dynamic graph?* Static DAGs win on auditability (stable execution record), predictable failure semantics (bounded failure modes), and engineering tooling (integrate with CI/CD, monitoring). Dynamic graphs win for emergent structure (exploratory research, debugging unknown failures, creative workflows). The trade-off is task-dependent.

**9.3 When Is Static Structure Sufficient?** Central claim: static DAG structure is sufficient — and preferable — for verifiable engineering tasks whose dependency structure can be articulated before execution and whose success criteria are checkable.
- **9.3.1 The Role of the Planner in Identifying Parallelism.** A critical, non-trivial assumption: the planner must identify independent sub-tasks and express them as parallel branches, via domain knowledge, LLM inference, or explicit user-provided info. If the planner fails, **SGH degenerates to a single-ready-unit scheduler**, and its advantages reduce to three: the three-level recovery protocol, plan-version immutability for auditability, and execution/diagnostic context separation. These are real but not the full structural benefit.
- **9.3.2 Estimating the Prevalence of Parallelism.** From the 70-project survey, ~30–40% of agent tasks exhibit some natural parallelism (multiple file reads, parallel API calls, alternative approaches); the remaining 60–70% are essentially linear chains or have parallelism hard to identify. SGH's multi-ready-unit capability benefits a subset; the rest get recovery + auditability. Hypothesized class includes most software engineering, data analysis, and operational tasks.

**9.4 The Recovery Layer as a First-Class Abstraction.** To the authors' knowledge, the first formal treatment of failure recovery in LLM agent execution as a protocol rather than ad-hoc. Similar escalation patterns exist in classical fault-tolerance (circuit breakers, bulkheads). The recovery layer is a portable design contribution — any LLM agent system struggling with failure loops could adopt a similar escalation protocol, even within a single-ready-unit scheduler.

**9.5 Limitations and Future Directions.**
- *Limitation 1: No experimental validation* — the most significant limitation.
- *Limitation 2: Static DAG assumption* — fails for exploratory tasks, dynamic goal evolution, and creative generation.
- *Limitation 3: LLM error propagation* — a DAG-generation error propagates to multiple parallel executions, wasting time and tokens; recovery mitigates but cost is higher.
- *Limitation 4: Cold start problem* — for new domains the planner must build the DAG from scratch (identify sub-goals, dependencies, joins, contracts); amortized only with reusable templates.
- *Limitation 5: Lack of complexity-theoretic guarantees.*
- *Limitation 6: Implementation complexity* — a minimal SGH needs ~3,300–6,500 lines of production code (DAG validation 1,000–2,000; concurrent scheduler with rate limiting 800–1,500; state persistence/WAL 500–1,000; recovery engine 600–1,200; contract validation 400–800), vs ~300–500 for a simple Agent Loop, but less than Airflow (50,000+) or Prefect (30,000+).

*Future Work Validation Strategy:* (1) implement a prototype SGH runtime; (2) curate a stratified ≥50-task benchmark with ground-truth dependencies; (3) execute the seven-group protocol with ≥10 runs/task/group and paired t-tests.

**9.6 When the Planner Fails: Incorrect DAGs.** Two defenses: structural validation (catches cycles, unreachable nodes, inconsistent joins, missing contracts) and runtime detection (missing dependency → downstream contract violation → recovery). Residual risk: structurally valid but strategically wrong DAGs (suboptimal decomposition missing parallelism) — a planner quality problem, made observable and isolated but not guaranteed correct.

**9.7 The Boundary of Applicability: Exploratory Tasks.** SGH is ill-suited for open-ended exploration, dynamic goal evolution, and creative generation. The static commitment is a liability when task structure is emergent — a direct consequence of Principle 2.

**9.8 SGH as a Degenerate Single-Ready-Unit Scheduler.** If the planner produces a linear chain, |𝒰| ≤ 1 everywhere and SGH degenerates to single-ready-unit. **SGH's value is bounded by planner quality.** Open question: should SGH include a planner-quality validator that falls back to a simpler scheduler for linear chains?

**9.9 The Granularity Trade-off in Static DAGs.** report's all_of join over run_tests and update_docs forces waiting for both, even though analysis is available earlier — unnecessary serialization. Finer-grained decomposition restores parallelism at the cost of a larger DAG. Optimal granularity is a planner design decision SGH does not automate.

**9.10 Implementation Considerations.** *Concurrent scheduling:* incremental ready-set update reduces O(|V|+|E|) to O(|E_new|); token-bucket rate limiting for API quotas. *State persistence:* append-only WAL with periodic snapshots (inspired by Ongaro, 2014) for replayability and time-travel debugging. *Fault-tolerant execution:* heartbeat detection, idempotent nodes (unique request IDs for side-effecting nodes), distributed consensus (Raft/Paxos) for leader election. SGH-specific complexity arises from non-deterministic LLM nodes invalidating classical assumptions (deterministic output, failure = crash).

## 10 Limitations

**10.1 Expressiveness Boundary.** Four deliberately excluded capabilities, each for a principled reason (Table 14). *On the exclusion of first_of:* LLM generation is stateful (mid-generation cancellation needs compensation protocols) and first_of introduces commit-point ambiguity. *Workaround:* approximate "try all, take first" via all_of parallel launch of A, B, C then a downstream D node that selects the best — sacrifices cancellation efficiency but preserves selection. Survey: only 8% of agent tasks require true first_of semantics (mostly "race to solve" benchmarks).

**10.2 Fixed-Overhead Hypothesis (H4).** On simple tasks (1–3 steps), SGH's structural overhead may result in measurably higher cost without proportional success-rate improvement. If confirmed, motivates a dual-path design routing simple tasks to a lightweight loop and complex tasks to the full graph harness.

**10.3 LLM Dependence in Diagnosis and Planning.** SGH removes the LLM from the scheduling policy 𝒫 but the LLM remains central to plan generation and failure diagnosis. SGH makes these failures observable and attributable but does not eliminate them.

**10.4 Relationship to Evolutionary Graph Architecture.** Limitations define the design space for an evolutionary graph architecture (companion work) that selectively relaxes constraints: adding first_of with compensation; recursive sub-graph expansion with bounded depth; parent-chain rollback with plan-version inheritance. Each relaxation trades controllability for expressiveness.

## 11 Conclusion

Graph Harness rests on three ideas: (1) a scheduler-unified framework formalizing agent execution as tuples (𝒮, 𝒰, 𝒫, 𝒪, Δ), with ready-set cardinality |𝒰| as the key parameter (Agent Loops |𝒰|≤1, graph executors |𝒰|≥1); (2) four design principles with explicit trade-offs (controllability first, stable execution commitment, bounded recovery, side-effect classification), derived from 70 systems; (3) an attributable seven-group experimental framework decomposing total gain into planning, scaffold, graph, patch, and replan gains. SGH is not the most expressive architecture — deliberately so — but the most controllable graph-based architecture the authors could design, with an explicit, principled, and relaxable expressiveness boundary.

*Limitations and future work:* the most significant limitation is the absence of empirical validation. A companion paper [work in progress] will report on an SGH prototype and experiments; a second companion paper analyzes the capability boundary and develops an evolutionary graph architecture.

## Selected References

- Bai et al. (2026) El Agente Gráfico: structured execution graphs for scientific agents. arXiv:2602.17902.
- Cormen et al. (2009) Introduction to Algorithms, 3rd ed., MIT Press.
- Erdogan et al. (2025) Plan-and-Act: improving planning of agents for long-horizon tasks. ICML.
- Graham (1969) Bounds on multiprocessing timing anomalies. SIAM J. Applied Math 17(2), 416–429.
- Lamport (2001) Paxos made simple. ACM SIGACT News 32(4), 18–25.
- Li et al. (2025) Agent-oriented planning in multi-agent systems. ICLR.
- Li et al. (2026) Beyond entangled planning: task-decoupled planning for long-horizon agents. arXiv:2601.07577.
- Liu et al. (2025) Graph-augmented large language model agents. arXiv:2507.21407.
- Microsoft (2023) Semantic Kernel: a lightweight SDK for AI orchestration.
- Ongaro (2014) Raft consensus algorithm.
- Team (2024) LangGraph.
- Topcuoglu et al. (2002) Performance-effective and low-complexity task scheduling (HEFT).
- Yue et al. (2026) Agentic Computation Graphs (ACGs).
- Zhuge et al. (2024) GPTSwarm.

*(Snapshot captured by manual paste — the arXiv ID 2604.11378 has a future-dated prefix (2604 → April 2026) relative to capture date; treat provenance accordingly.)*
