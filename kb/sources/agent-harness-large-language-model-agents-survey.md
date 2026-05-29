---
source: https://www.preprints.org/manuscript/202604.0428
description: "Survey framing the LLM agent harness as a six-component runtime governance layer and primary determinant of deployed agent reliability"
captured: 2026-05-28
capture: web-fetch
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Agent Harness for Large Language Model Agents: A Survey

Author: Qianyu Meng, Yanan Wang, Liyi Chen, Yihang Li, Wei Wu, Wenyuan Jiang, Qimeng Wang, Chengqiang Lu, Yan Gao, Yi Wu, Yao Hu
Source: https://www.preprints.org/manuscript/202604.0428
Date: Posted 2026-04-28; submitted 2026-04-09; version 3

## Snapshot Note

This snapshot captures the main article content visible in the Preprints.org HTML page. The page includes many figures, tables, citations, and math-like component notation that are partly flattened in the HTML text extraction. Use the source page or downloadable PDF for exact table formatting, figure details, and reference metadata.

## Abstract

The paper argues that the reliability of large language model agents in production environments is increasingly determined by the agent harness that wraps the underlying model, rather than by the model alone. It defines the agent harness as a six-component tuple:

- `E` - execution loop
- `T` - tool registry
- `C` - context manager
- `S` - state store
- `L` - lifecycle hooks
- `V` - evaluation interface

The survey claims five main contributions:

1. A formal definition of the agent harness as the six-component tuple above.
2. A historical tracing from software testing and reinforcement learning environments to modern LLM agent systems, unified by the need for controllable, observable, verifiable runtime environments.
3. A taxonomy and completeness matrix for 23 representative systems, showing that production-ready systems tend to implement all six architectural components.
4. A cross-cutting analysis of nine technical challenges, including sandboxing, evaluation, protocol standardization, context management, tool governance, memory architecture, planning governance, multi-agent coordination, and compute economics.
5. A research agenda for harness-layer infrastructure, which the authors argue remains underdeveloped relative to model and component capabilities.

The latest version is also listed at `https://github.com/Gloriaameng/Awesome-Agent-Harness`.

## 1. Introduction

The introduction frames agent reliability as a model-plus-harness property. It argues that recent agent research often focuses on model reasoning, tool use, memory, and planning while assuming that a sufficiently capable model plus prompts and context is enough for robust execution. The paper disputes that assumption by pointing to benchmark and deployment evidence where harness differences alone produce large performance and reliability differences.

Examples used in the introduction include:

- Holistic Agent Leaderboard, where standardizing the evaluation harness eliminated implementation bugs.
- AgencyBench, where models perform differently across execution ecosystems.
- SWE-bench, AgentBench, GAIA, and WebArena, where environment infrastructure is a reproducible bottleneck.
- Practitioner reports from OpenAI Codex, Stripe, Vercel, and LangChain, presented as evidence that underspecified environments and infrastructure design constrain progress.

The introduction states the core thesis: the agent harness is not a passive conduit but a co-determinant of capabilities because it governs tool access, context maintenance, state persistence, execution robustness, and evaluation feedback.

## 2. Related Work

The related work section says prior surveys typically analyze agent capabilities or individual components such as memory, tools, planning, multi-agent coordination, and evaluation. The authors' distinction is that those surveys often treat the execution environment as background, while this survey treats the runtime harness as the primary research object.

The section contrasts the survey with adjacent work on:

- General LLM agents and autonomous-agent architectures.
- Memory mechanisms.
- Tool learning.
- Multi-agent coordination.
- Evaluation methodology.
- Agent self-improvement and adaptive infrastructure.

The paper says its vantage point makes cross-harness performance variation, evaluation infrastructure failure, and emergent reliability properties visible.

## 3. Definition and Conceptual Framework

The paper defines an agent harness as a software system implementing six runtime governance functions:

- `E` - Execution loop: manages observe-think-act sequencing, termination conditions, and error recovery.
- `T` - Tool registry: maintains typed, validated tool interfaces and routes or monitors tool invocations.
- `C` - Context manager: governs what enters the model context across turns, including compaction, retrieval, and prioritization.
- `S` - State store: persists task-relevant state across turns and optionally across sessions.
- `L` - Lifecycle hooks: provide pre- and post-invocation interception points for authentication, logging, policy enforcement, and instrumentation.
- `V` - Evaluation interface: captures action trajectories, intermediate states, and success signals for benchmarking and observability.

The paper distinguishes lifecycle hooks from evaluation interfaces: lifecycle hooks regulate execution events, while evaluation interfaces expose canonical trajectory records for benchmarking and analysis. It maps the six components to recurring production failure modes: execution runaway, tool misuse, context blowout, state loss, unmonitored side effects, and unobservable behavior.

The paper says `E` and `T` are necessary for a minimal harness because a system without multi-step execution or tools is only an inference wrapper or reasoning engine. Implementing all six components with production-grade reliability is treated as sufficient for a full-stack harness.

## 4. Historical Evolution

The survey traces the harness concept through three lineages:

- Software testing harnesses, including JUnit-style governance wrappers.
- Reinforcement learning environments, including interface standardization.
- LLM agent frameworks, which accumulated practical failure modes and orchestration patterns.

It identifies a "harness turn" around 2024 to 2026, where engineering focus shifts from model capability demonstrations toward systematic infrastructure. The paper frames three engineering paradigms:

1. Prompt engineering, asking what text to give the model.
2. Context engineering, asking what structured information to assemble for the model.
3. Harness engineering, asking what governance, constraints, feedback loops, and execution controls are required for reliable agent systems.

The paper uses benchmark infrastructure, MCP, A2A, AgencyBench, SkillsBench, and AIOS as examples of the field recognizing the harness as a separate engineering object.

## 5. Taxonomy of Agent Harness Systems

The taxonomy uses stack position and domain scope as classification axes rather than ranking systems by simple functional completeness. The paper distinguishes:

- Full-stack deployment harnesses.
- Development frameworks.
- Capability modules.

It reports a six-component completeness matrix over 22 or 23 representative systems, depending on the section wording, and argues that full-stack deployment harnesses tend to cover all six governance components. Named examples include Claude Code, OpenClaw/PRISM, Hermes, AIOS, OpenHands, LangChain, LangGraph, AutoGen, CrewAI, Voyager, Reflexion, MemGPT, MCP, A2A, SWE-bench, HAL, AgencyBench, SkillsBench, and other benchmark or module systems.

The taxonomy's main claim is that systems should be selected by stack position and domain scope rather than by a one-dimensional "more features means better" scale.

## 6. Core Technical Challenges

The survey organizes challenges into execution infrastructure, state and knowledge management, and coordination/planning. Its nine main challenge areas are:

1. Sandboxing and security.
2. Evaluation and benchmarking.
3. Protocol and interface standardization.
4. Runtime context management.
5. Knowledge and context engineering.
6. Tool use governance.
7. Memory management architecture.
8. Planning loop governance.
9. Multi-agent coordination.

The paper repeatedly emphasizes cross-component coupling: optimizing one component independently can worsen another.

### 6.2. Sandboxing and Security

The paper says agent harness security differs from both traditional software security and model-output safety because the danger often comes from actions, not text. It names environment prompt injection, capability escalation through tool composition, memory poisoning, and sandbox escape as key threats. It argues that sandboxing is necessary but insufficient, and that protocol enforcement, OS-level isolation, and audit instrumentation must be composed.

The paper also says no current harness provides a formal compositional security specification for the combined effects of protocol enforcement, isolation, and auditing.

### 6.3. Evaluation and Benchmarking

The survey frames agent evaluation as trajectory evaluation rather than string-output evaluation. It identifies three breaks from standard NLP evaluation:

- Partial correctness makes binary success/failure metrics lossy.
- Path dependence means later actions depend on earlier action outcomes.
- Environment coupling means the same agent can perform differently in different harnesses or environment states.

The paper uses AgencyBench, HAL, AgentBench, GAIA, SWE-bench, OSWorld, WebArena, and related benchmark systems to argue that evaluation harnesses can be a source of measurement error as well as observability and security signal.

### 6.4. Protocol and Interface Standardization

The paper treats protocol fragmentation as a structural bottleneck. It discusses MCP, A2A, ACP, and related standards as representing different interoperability layers. It identifies four causes of fragmentation:

- Scope disagreement over whether the central layer is tools, agent delegation, or intent communication.
- Incentive misalignment among major labs and platforms.
- Deployment friction from RPC servers, schema management, and authorization.
- Lack of agreed benchmark scenarios for cross-harness interaction.

It argues that agent interoperability infrastructure lags capability infrastructure by roughly two to three years.

### 6.5. State and Knowledge Management

The paper says the harness creates the model's coherent execution context by managing runtime context, tools, and memory. It treats context management as more than context window length: the core problem is deciding what to retain, compress, retrieve, or evict.

It cites SkillsBench as evidence that curated skills can raise average pass rates, while also noting that skill management can harm performance when the wrong skills are supplied. The paper frames the context manager as an active epistemic filter and a compression mechanism over the execution loop's event/state space.

### 6.6. Tool Use as Core Harness Function

The paper makes the tool registry the primary governance point for agent behavior. It covers:

- Tool schema validation.
- Retry and failure handling.
- Tool permission and composition risk.
- Registry-scale governance.
- MCP as shared protocol infrastructure.
- Agent Skills as workflow-level interoperability beyond tool-level protocols.

It argues that tool governance is not just about adding more tools; removing or constraining tools can improve performance and safety. The registry is compared to a system-call table because it defines capabilities, enforcement boundaries, and audit points.

### 6.7. Memory Management Architecture

The paper reframes memory as harness infrastructure rather than model capability. The harness decides what is eligible for storage, what is written, how it is indexed, how it is retrieved, how long it persists, and who can modify it.

It reports three memory findings:

- Recency bias, scalability, and retrieval latency create a three-way tradeoff.
- Model-written memories require write governance, not only storage and retrieval.
- Memory poisoning can persist across sessions, and write-time security controls are largely absent.

The paper compares memory systems including MemGPT, Generative Agents, Voyager, MemoryOS, A-MEM, Mem0, and AgentSys. It says AgentSys is unusual in offering write isolation, while most systems lack write-time security.

### 6.8. Coordination and Planning

The paper argues that planning quality is a model-harness property because the harness controls observation injection, action validation, abort conditions, branching state, budget allocation, backtracking, and plan commitment. For multi-agent systems, the harness also governs identity, message validation, shared state consistency, delegation, and failure containment.

The paper identifies cross-agent prompt injection as a production security problem: compromised agents can send malicious instructions over legitimate inter-agent channels, and current production harnesses do not provide strong filtering for this trusted-channel threat.

### 6.9. Emerging Topics and Research Directions

The paper identifies cross-component coupling patterns:

- Retention-security coupling between context retention and lifecycle/security enforcement.
- Evaluation-governance coupling between evaluation interfaces and lifecycle hooks.
- Memory-tool composition boundary between state stores and tool registries.

It proposes research directions with estimated effort and success criteria, including:

- Cross-component interaction modeling.
- Agent-native observability and deterministic replay.
- Human-in-the-loop approval policies.
- Cost and compute economics.
- Long-running autonomy and skill library governance.
- Automated harness engineering.
- Natural-language harness specification.
- Formal verification of behavioral guarantees.
- Cross-harness portability.
- Protocol bridging.
- Long-horizon decomposition.
- Security formalization.
- Tool composition and dependency inference.
- Energy-aware infrastructure design.

## 7. Conclusion

The conclusion restates the infrastructure thesis: model capability is necessary but insufficient for reliable deployed agent behavior. The harness translates latent capability into reliability through execution governance, bounded tool access, context control, state persistence, lifecycle policy, and evaluation interfaces.

The paper says the field is building a reliability deficit if model capabilities improve faster than harness infrastructure. It recommends that agent evaluations report harness configuration alongside model and task specifications and endorses HARNESSCARD-style disclosure artifacts. It also recommends that researchers characterize whether findings are harness-specific or harness-general, and that the community invest in shared harness infrastructure such as lifecycle hooks, trajectory schemas, and persistence interfaces.

## Limitations Reported by the Source

The paper states that:

- Its 23-system corpus excludes enterprise-internal deployments and unpublished domain-specific harnesses.
- Completeness ratings for closed-source systems are based on public documentation that may not reflect internal implementations.
- The formal labeled-transition-system treatment of the execution loop is proposed, not established.
- Several quantitative claims come from preprint sources pending peer review.
- The survey reflects the field as of March 2026, and protocol, context, and security work is changing quickly.
- OpenClaw receives unusually detailed treatment because its architecture and PRISM security layer are publicly documented, which may bias the taxonomy toward OpenClaw-style patterns.
