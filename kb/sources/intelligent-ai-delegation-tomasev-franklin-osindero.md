---
source: https://arxiv.org/pdf/2602.11865
description: Google DeepMind framework for intelligent AI delegation — proposes adaptive protocols covering task decomposition, multi-objective optimization, trust/reputation, verifiable completion, and security for human-AI and AI-AI delegation networks, with explicit analysis of how MCP, A2A, AP2, and UCP map onto these requirements.
captured: 2026-03-16
capture: pdf-read
type: academic-paper
---

# Intelligent AI Delegation

Author: Nenad Tomašev, Matija Franklin, Simon Osindero (Google DeepMind)
Source: https://arxiv.org/pdf/2602.11865
Date: 12 February 2026

## Abstract

AI agents are able to tackle increasingly complex tasks. To achieve more ambitious goals, AI agents need to be able to meaningfully decompose problems into manageable sub-components, and safely delegate their completion across to other AI agents and humans alike. Yet, existing task decomposition and delegation methods rely on simple heuristics, and are not able to dynamically adapt to environmental changes and robustly handle unexpected failures. Here we propose an adaptive framework for *intelligent AI delegation* — a sequence of decisions involving task allocation, that also incorporates transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries, clarity of intent, and mechanisms for establishing trust between the two (or more) parties. The proposed framework is applicable to both human and AI delegators and delegatees in complex delegation networks, aiming to inform the development of protocols in the emerging agentic web.

*Keywords: AI, agents, LLM, delegation, multi-agent, safety*

## 1. Introduction

As advanced AI agents evolve beyond query-response models, their utility is increasingly defined by how effectively they can decompose complex objectives and delegate sub-tasks. This coordination paradigm underpins applications ranging from personal use, where AI agents can act as personal assistants, to commercial, enterprise deployments where AI agents can provide support and automate workflows. Large language models (LLMs) have already shown promise in robotics, by enabling more interactive and accurate goal specification and feedback.

Delegation is more than just task decomposition into manageable sub-units of action. Beyond the creation of sub-tasks, delegation necessitates the assignment of responsibility and authority and thus implicates outcomes accountability. Delegation thus involves risk assessment, which can be moderated by trust. Delegation further involves capability matching and continuous performance monitoring, incorporating dynamic adjustments based on feedback, and ensuring completion of the distributed task under the specified constraints.

The absence of adaptive and robust deployment frameworks remains one of the key limiting factors for AI applications in high-stakes environments.

Here we introduce an intelligent task delegation framework aimed at addressing these limitations, informed by historical insights from human organizations, and grounded in key agentic safety requirements.

## 2. Foundations of Intelligent Delegation

### 2.1. Definition

We define *intelligent delegation* as a sequence of decisions involving task allocation, that also incorporates transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries, clarity of intent, and mechanisms for establishing trust between the two (or more) parties. Complex tasks may also involve steps pertaining to task decomposition, as well as careful capability lookup and matching to inform allocation decisions.

### 2.2. Aspects of Delegation

Delegation can take different forms, contextualized across several axes:

1. **Delegator.** Human or AI.
2. **Delegatee.** Human or AI.
3. **Task characteristics.**
   - (a) **Complexity.** The degree of difficulty inherent in the task, often correlated with the number of sub-steps and the sophistication of reasoning required.
   - (b) **Criticality.** The measure of the task's importance and the severity of consequences associated with failure or sub-optimal performance.
   - (c) **Uncertainty.** The level of ambiguity regarding the environment, inputs, or the probability of successful outcome achievement.
   - (d) **Duration.** The expected time-frame for task execution, ranging from instantaneous sub-routines to long-running processes spanning days or weeks.
   - (e) **Cost.** The economic or computational expense incurred to execute the task, including token usage, API fees, and energy consumption.
   - (f) **Resource Requirements.** The specific computational assets, tools, data access permissions, or human capabilities necessary to complete the task.
   - (g) **Constraints.** The operational, ethical, or legal boundaries within which the task must be executed, limiting the solution space.
   - (h) **Verifiability.** The relative difficulty and cost associated with validating the task outcome. Tasks with high verifiability (e.g., formal code verification, mathematical proofs) allow for "trust-less" delegation or automated checking. Conversely, tasks with low verifiability (e.g., open-ended research) require high-trust delegatees or expensive, labor-intensive oversight.
   - (i) **Reversibility.** The degree to which the effects of the task execution can be undone. Irreversible tasks that produce side effects in the real world (e.g., executing a financial trade, deleting a database, sending an external email) require stricter *liability firebreaks* and steeper authority gradients than reversible tasks (e.g., drafting an email, flagging a database entry).
   - (j) **Contextuality.** The volume and sensitivity of external state, history, or environmental awareness required to execute the task effectively. High-context tasks introduce larger privacy surface areas, whereas context-free tasks can be more easily compartmentalized and outsourced to lower-trust nodes.
   - (k) **Subjectivity.** The extent to which the success criteria are a matter of preference versus objective fact. Highly subjective tasks (e.g., "design a compelling logo") typically require "Human-as-Value-Specifier" intervention and iterative feedback loops, whereas objective tasks can be governed by stricter, binary contracts.

4. **Granularity.** The request could involve either fine-grained or course-grained objectives.
5. **Autonomy.** Task delegation may involve requests that grant full autonomy in pursuing sub-tasks, or be far more specific and prescriptive.
6. **Monitoring.** For delegated tasks, monitoring could be continuous, periodic, or event-triggered.
7. **Reciprocity.** While delegation is usually a one-way request, there could be cases of mutual delegation in collaborative agent networks.

The three delegation scenarios are: 1) human delegates to an AI agent; 2) AI agent delegates to an AI agent; 3) AI agent delegates to a human.

### 2.3. Delegation in Human Organizations

**The Principal-Agent Problem.** The *principal-agent problem* has been studied at length: a situation that arises when a principal delegates a task to an agent that has motivations that are not in alignment with that of the principal. The agent may thus prioritize their own motivations, withhold information, and act in ways that compromise the original intent. For AI delegation, this dynamic assumes heightened complexity.

**Span of Control.** In human organizations, *span of control* is a concept that denotes the limits of hierarchical authority exercised by a single manager. For human oversight, it is crucial to establish how many AI agents a human expert can reliably oversee without excessive fatigue, and with an acceptably low error rate.

**Authority Gradient.** Another relevant concept is that of an *authority gradient*. Coined in aviation, this term describes scenarios where significant disparities in capability, experience, and authority impede communication, leading to errors. A more capable delegator agent may mistakenly presume a missing level of capability on behalf of a delegatee. A delegatee agent may potentially, due to sycophancy and instruction following bias, be reluctant to challenge, modify, or reject a request.

**Zone of Indifference.** When an authority is accepted, the delegatee develops a *zone of indifference* — a range of instructions that are executed without critical deliberation or moral scrutiny. In current AI systems, this zone is defined by post-training safety filters and system instructions. In the emerging agentic web, this static compliance creates a significant systemic risk. As delegation chains lengthen (A → B → C), a broad zone of indifference allows subtle intent mismatches or context-dependent harms to propagate rapidly downstream. Intelligent delegation therefore requires the engineering of **dynamic cognitive friction**: agents must be capable of recognizing when a request, while technically "safe," is contextually ambiguous enough to warrant stepping *outside* their zone of indifference to challenge the delegator or request human verification.

**Trust Calibration.** An important aspect of ensuring appropriate task delegation is *trust calibration*, where the level of trust placed in a delegatee is aligned with their true underlying capabilities.

**Transaction cost economies.** *Transaction cost economies* justify the existence of firms by contrasting the costs of internal delegation against external contracting, specifically accounting for the overhead of monitoring, negotiation, and uncertainty.

**Contingency theory.** *Contingency theory* posits that there is no universally optimal organizational structure; rather, the most effective approach is contingent upon specific internal and external constraints. Applied to AI delegation, this implies that the requisite level of oversight, delegatee capability, and human involvement must not be static, but dynamically matched to the distinct characteristics of the task at hand.

## 3. Previous Work on Delegation

Constrained forms of delegation feature within historical narrow AI applications. Early expert systems were a nascent attempt to encode a specialized capability into software. Mixture of experts extends this by introducing a set of expert sub-systems with complementary capabilities, and a routing module.

Hierarchical reinforcement learning (HRL) represents a framework in which decision-making is delegated within a single agent. The Feudal Reinforcement Learning framework, notably revisited in FeUdal Networks, constitutes a particularly relevant paradigm. The Manager operates at a lower temporal resolution, setting abstract goals for the Worker to fulfil. Critically, the Manager learns *how* to delegate — identifying sub-goals that maximise long-term value — without requiring mastery of the lower-level primitive actions.

Multi-agent research addresses agent coordination for complex tasks exceeding single-agent capabilities. The Contract Net Protocol exemplifies an explicit auction-based decentralized protocol.

LLMs now constitute a foundational element in the architecture of advanced AI agents and assistants. These systems execute sophisticated control flows integrating memory, planning and reasoning, reflection and self-critique, and tool use.

Multi-agent systems incorporating LLM agents have become a topic of substantial interest, leading to development of agent communication and action protocols such as MCP, A2A, AP2, and others. Human-in-the-loop approaches have been developed where task delegation has defined checkpoints for human oversight.

## 4. Intelligent Delegation: A Framework

Existing delegation protocols rely on static, opaque heuristics that would likely fail in open-ended agentic economies. The proposed framework for *intelligent delegation* is centered on five requirements: *dynamic assessment*, *adaptive execution*, *structural transparency*, *scalable market coordination*, and *systemic resilience*.

**Dynamic Assessment.** Current delegation systems lack robust mechanisms for the dynamic assessment of competence, reliability, and intent within large-scale uncertain environments. Moving beyond reputation scores, a delegator must infer details of a delegatee's current state relative to task execution. Assessment operates as a continuous rather than discrete process, informing Task Decomposition (§4.1) and Task Assignment (§4.2).

**Adaptive Execution.** Delegation decisions should not be static. They should adapt to environmental shifts, resource constraints, and failures in sub-systems. Delegators should retain the capability to switch delegatees mid-execution.

**Structural Transparency.** Current sub-task execution in AI-AI delegation is too opaque to support robust oversight for intelligent task delegation. This opacity obscures the distinction between incompetence and malice, compounding risks of collusion and chained failures.

**Scalable Market Coordination.** Task delegation needs to be efficiently scalable. Protocols need to be implementable at web-scale to support large-scale coordination problems in virtual economies.

**Systemic Resilience.** The absence of safe intelligent task delegation protocols introduces significant societal risks. AI delegation necessitates a framework to operationalise responsibility. Consequently, the definition of strict roles and the enforcement of bounded operational scopes constitutes a core function of Permission Handling (§4.7).

### Framework Pillars (Table 1)

| Framework Pillar | Core Requirement | Technical Implementation |
|---|---|---|
| Dynamic Assessment | Granular inference of agent state | Task Decomposition (§4.1), Task Assignment (§4.2) |
| Adaptive Execution | Handling context shifts | Adaptive Coordination (§4.4) |
| Structural Transparency | Auditability of process and outcome | Monitoring (§4.5), Verifiable Completion (§4.8) |
| Scalable Market | Efficient, trusted coordination | Trust & Reputation (§4.6), Multi-objective Optimization (§4.3) |
| Systemic Resilience | Preventing systemic failures | Security (§4.9), Permission Handling (§4.7) |

### 4.1. Task Decomposition

Task decomposition is a prerequisite for subsequent task assignment. The framework incorporates *"contract-first decomposition"* as a binding constraint, wherein task delegation is contingent upon the outcome having precise verification. If a sub-task's output is too subjective, costly, or complex to verify, the system should recursively decompose it further. The decomposition logic should maximise the probability of reliable task completion by aligning sub-task granularity with available market specialisations.

Decomposition strategies should explicitly account for hybrid human-AI markets. Delegators need to decide if sub-tasks require human intervention, whether due to AI agent unreliability, unavailability, or domain-specific requirements for human-in-the-loop oversight.

### 4.2. Task Assignment

For each final specification of a sub-task, a delegator needs to identify delegatees with matching capabilities, sufficient resources and time, at an acceptable cost. A centralized approach would involve registries of agents, tools, and human participants. Alternatively, decentralized market hubs where delegators advertise tasks and agents (or humans) can offer their services and submit bids. Advanced AI agents that utilize LLMs introduce new opportunities for matching, given that they can engage in an interactive negotiation prior to commitment.

Successful matching should be formalized into a smart contract that ensures that the task execution faithfully follows the request. Crucially, these contracts must be bidirectional: they should protect the delegatee as rigorously as the delegator. Assignment should also involve establishing a delegatee's role, boundaries, and the exact level of autonomy granted.

### 4.3. Multi-objective Optimization

Core to intelligent task delegation is the problem of multi-objective optimization. A delegator rarely seeks to optimize a single metric, often trading off between numerous competing ones. The optimization landscape consists of competing objectives that map directly to the task characteristics defined in §2 — cost, uncertainty, privacy, quality, and efficiency.

The delegator navigates a *trust-efficiency frontier*, seeking to maximise the probability of success while satisfying strict constraints on context leakage and verification budgets.

### 4.4. Adaptive Coordination

For tasks characterized by high uncertainty or high duration, static execution plans are insufficient. The delegation of such tasks in highly dynamic, open, and uncertain environments requires *adaptive coordination*, and a departure from fixed, static execution plans.

External triggers include: the delegator altering the task specification; the task being canceled; availability or cost changes of external resources; a new task entering the queue with higher priority; security systems identifying potentially malicious actions.

Internal triggers include: a particular delegatee experiencing performance degradation; a delegatee consuming resources beyond its allocated budget; an intermediate artifact failing a verification check; a particular delegatee turning unresponsive.

The response orchestration depends on the level of centralization in the delegation network. In the centralised case, a dedicated delegator maintains a global view. In decentralized orchestration through market-based mechanisms, newly derived delegation requests can be pushed onto an auction queue.

### 4.5. Monitoring

Monitoring in the context of task delegation is the systematic process of observing, measuring, and verifying the state, progress, and outcomes of a delegated task. A robust monitoring system would need to incorporate multiple complementary solutions along these axes:

**Target:** Outcome-level monitoring (post-hoc validation) vs. Process-level monitoring (continuous tracking of intermediate states, resource consumption, and methodology).

**Observability:** Indirect (inferring progress via environmental side-effects) vs. Direct (explicit status polling, push notifications, real-time event streaming APIs).

**Transparency:** Black-box (input/output observation only) vs. White-box (full inspection of internal reasoning traces, decision logic, and memory).

**Privacy:** Full Transparency vs. Cryptographic (Zero-Knowledge Proofs — zk-SNARKs — or MPC to verify correctness without revealing data).

**Topology:** Direct (1-to-1 monitoring) vs. Transitive (relying on signed attestations from intermediate agents to verify sub-delegatees).

Smart contracts on blockchain can be used to make the delegatee agent commit to publishing key progress milestones or checkpoints. Monitoring should be negotiated prior to execution.

### 4.6. Trust and Reputation

Trust and reputation mechanisms constitute the foundation of scalable delegation, minimizing transactional friction and promoting safety in open multi-agent environments. Trust is defined as the delegator's degree of belief in a delegatee's capability to execute a task in alignment with explicit constraints and implicit intent.

Reputation serves as a predictive signal, derived from an aggregated and verifiable history of past actions, which act as a proxy for an agent's latent reliability and alignment. Trust informs the dynamic scoping of authority and autonomy. This mechanism of graduated authority results in low-trust agents facing strict constraints, while high-reputation agents operate with minimal intervention.

Reputation implementation approaches:

| Reputation Model | Mechanism | Utility |
|---|---|---|
| Immutable Ledger | Encodes task outcomes, resource consumption, and constraint adherence as verifiable transactions on a tamper-proof blockchain. | Establishes a foundational history of performance that prevents retroactive tampering. |
| Web of Trust | Utilizes Decentralized Identifiers to issue signed, context-specific Verifiable Credentials attesting to specific capabilities. | Moves beyond generic scores to a portfolio model, enabling precise delegation based on domain-specific expertise. |
| Behavioral Metrics | Derives transparency and safety scores by analyzing the execution process, specifically the clarity of reasoning traces and protocol compliance. | Evaluates *how* a task is performed rather than just the result, ensuring high-stakes tasks align with safety standards. |

### 4.7. Permission Handling

Granting autonomy to AI agents introduces a critical vulnerability surface. Permission handling must balance operational efficiency with systemic safety. For routine low-stakes tasks, characterized by low criticality and high reversibility, agents can be granted default standing permissions derived from verifiable attributes — such as organisational membership, active safety certifications, or a reputation score exceeding a trusted threshold. In high-stakes domains, permissions must be risk-adaptive, granted on a just-in-time basis, strictly scoped to the immediate task's duration, and where appropriate, gated by mandatory human-in-the-loop approval.

Permissioning frameworks must account for the recursive nature of task delegation through privilege attenuation. When an agent sub-delegates a task, it cannot transmit its full set of authorities; instead, it must issue a permission that restricts access to the strict subset of resources required for that specific sub-task. This ensures that a compromise at the edge of the network does not escalate into a systemic breach.

Finally, the lifecycle of permissions must be governed by continuous validation and automated revocation. Access rights are not static endowments but dynamic states that persist only as long as the agent maintains the requisite trust metrics. Permissioning rules should be defined via policy-as-code.

### 4.8. Verifiable Task Completion

The delegation lifecycle culminates in verifiable task completion, the mechanism by which provisional outcomes are validated and finalized. Verification serves as the definitive event that transforms a provisional output into a settled fact within the agentic market, establishing the basis for payment release, reputation updates, and the assignment of liability.

Verification mechanisms:
- **Direct outcome inspection** — feasible for tasks with high intrinsic verifiability and low subjectivity (auto-verifiable domains such as code generation with test cases).
- **Trusted third-party auditing** — used when the delegator lacks the expertise or permissions to access artifacts, and tool-based solutions are infeasible.
- **Cryptographic proofs** — represents a further option for trustless, automated verification in open and potentially adversarial environments. A delegatee can prove that a specific program was executed correctly on a given input via techniques like zk-SNARKs.
- **Game-theoretic mechanisms** — several agents may play a verification game, with the reward distributed to those producing the majority result — a Schelling point.

In a delegation chain A → B → C, verification and liability become recursive. Agent A does not have a direct contractual relationship with C; responsibility flows up the chain.

### 4.9. Security

Ensuring safety in task delegation is a hard prerequisite to its viability and adoption. Security threats are categorized by the locus of the attack vector:

**Malicious Delegatee:**
- Data Exfiltration: Delegatee steals sensitive data provided for the task.
- Data Poisoning: Delegatee aims to undermine the delegator's objective by returning subtly corrupted data.
- Verification Subversion: Delegatee utilizes prompt injection or another related method, aiming to jailbreak AI critics used in task completion verification.
- Resource Exhaustion: Delegatee engages in a denial-of-service attack by intentionally consuming excessive computational or physical resources.
- Unauthorized Access: Delegatee utilizes malware, aiming to obtain permissions and privileges within the network.
- Backdoor Implanting: Delegatee successfully completes a task but additionally embeds concealed triggers or vulnerabilities within the generated artifacts.

**Malicious Delegator:**
- Harmful Task Delegation: Delegator delegates tasks that are illegal, unethical, or designed to cause harm.
- Vulnerability Probing: Delegator delegates benign-seeming tasks designed to probe a delegatee agent's capabilities, security controls, and potential weaknesses.
- Prompt Injection and Jailbreaking: Delegator crafts task instructions to bypass an AI agent's safety filters.
- Model Extraction: Delegator issues a sequence of queries specifically designed to distill the delegatee's proprietary system prompt, reasoning capabilities, or underlying fine-tuning data.
- Reputation Sabotage: Delegator submits valid tasks but reports false failures or provides unfair negative feedback.

**Ecosystem-Level Threats:**
- Sybil Attacks: A single adversary creates a multitude of seemingly unrelated agent identities to manipulate reputation systems or subvert auctions.
- Collusion: Agents collude to fix prices, blacklist competitors, or manipulate market outcomes.
- Agent Traps: Agents processing external content encounter adversarial instructions embedded in the environment, designed to hijack the agent's control flow.
- Agentic Viruses: Self-propagating prompts that not only make the delegatee execute malicious actions, but additionally re-generate the prompt and further compromise the environment.
- Protocol Exploitation: Adversaries exploit implementation vulnerabilities in the smart contracts or payment protocols on the agentic web.
- Cognitive Monoculture: Over-dependence on a limited number of underlying foundation models and agents, or on a limited number of safety fine-tuning recipes, risks creating a single point of failure, which opens up a possibility of failure cascades and market crashes.

A *defense-in-depth* strategy is necessitated, integrating multiple technical security layers.

## 5. Ethical Delegation

### 5.1. Meaningful Human Control

One of the core risks in scalable delegation is the erosion of meaningful human control through automation. Humans naturally develop a zone of indifference, where decisions may be accepted without further scrutiny. The framework therefore requires engineering a certain amount of cognitive friction during oversight. Friction must be context-aware: seamless execution for tasks with low criticality or low uncertainty, but dynamically increasing cognitive load when the system encounters higher uncertainty or unanticipated scenarios.

Intelligent Delegation frameworks need to avoid instantiating a *moral crumple zone*, in which human experts lack meaningful control over outcomes, yet are introduced in delegation chains merely to absorb liability.

### 5.2. Accountability in Long Delegation Chains

In long delegation chains (X → A → B → C → … → Y), the increased distance between the original intent (X) and the ultimate execution (Y) may result in an accountability vacuum. The framework may need to implement *liability firebreaks*, as predefined contractual stop-gaps where an agent must either:
1. Assume full, non-transitive liability for all downstream actions, essentially "insuring" the user against sub-agent failure.
2. Halt execution and request an updated transfer of authority from the human principal.

### 5.3. Reliability and Efficiency

Implementing the proposed verification mechanisms (ZKPs or multi-agent consensus games) may introduce latency, and an additional computational cost. This constitutes a reliability premium. There is a risk that if high-assurance delegation is computationally expensive, safety becomes a luxury good. This should be mitigated by ensuring a level of minimum viable reliability, as a baseline that must be guaranteed for all users.

### 5.4. Social Intelligence

As agents integrate into hybrid teams, they function not only as tools but as teammates, and occasionally as managers. This requires a form of *social intelligence* that respects the dignity of human labor. There is a risk that AI agents may fragment human networks, and weaken inter-human relationships, in case more delegation is being mediated through AI nodes.

Agents must be designed to respect human norms of appropriateness, especially around privacy, and also workflow boundaries such as knowing when to interrupt for feedback and when to remain silent.

### 5.5. User Training

To ensure safety, we must equip human participants with the expertise to function effectively as delegators, delegatees, or overseers within agentic systems. Intelligent delegation frameworks should be extended to include some form of a developmental objective. *Curriculum-aware task routing systems* should track the skill progression of junior team members and strategically allocate tasks that sit at the boundary of their expanding skill set, within the zone of proximal development.

### 5.6. Risk of De-skilling

The immediate efficiency gains achieved through delegation may come at the cost of gradual skill degradation, as human participants in hybrid loops lose proficiency due to reduced engagement. This is an instance of the classic *paradox of automation*. As AI agents expand to handle the majority of routine workflows, human operators are increasingly removed from the loop. Unchecked delegation threatens the organizational apprenticeship pipeline.

## 6. Protocols

For intelligent task delegation to be implemented in practice, the paper examines how requirements map onto established protocols: MCP, A2A, AP2, and UCP.

**MCP.** Has been introduced to standardize how AI models connect to external data and tools via a client-host-server architecture. Reduces transaction cost of delegation. However, MCP defines capabilities but lacks the policy layer to govern usage permissions or support deep delegation chains. It lacks the cryptographic slots to enforce verifiable task completion, and is stateless regarding internal reasoning, exposing only results rather than intent or traces. It lacks native mechanisms for reputation or trust.

**A2A.** The A2A protocol serves as the peer-to-peer transport layer on the agentic web. Defines how agents discover peers via *agent cards* and manage task lifecycles via *task objects*. Supports asynchronous event streams. A2A has been primarily designed for coordination, rather than adversarial safety. A task is marked as completed without additional verification.

**AP2.** Provides a standard for mandates, cryptographically signed intents that authorize an agent to spend funds or incur costs on behalf of a principal. Allows AI agents to generate, sign, and settle financial transactions autonomously. May prove valuable for implementing liability firebreaks. However, AP2 lacks mechanisms to verify task execution quality and omits conditional settlement logic.

**UCP.** The Universal Commerce Protocol addresses the specific challenges of delegation within transactional economies. Crucially, UCP aligns well with the requirements for Permission Handling and Security by treating payment as a first-class, verifiable subsystem. However, UCP's architecture is explicitly optimized for commercial intent; its primitives may require significant extension to support the delegation of abstract, non-transactional computational tasks.

### 6.1. Towards Delegation-centered Protocols

The paper provides several examples of how specific points could be integrated into existing protocols, including: verification policy fields in A2A Task objects; monitoring stream extensions for MCP; Request for Quote (RFQ) protocol extensions; and Delegation Capability Tokens (DCTs) based on Macaroons or Biscuits as attenuated authorization tokens.

## 7. Conclusion

Significant components of the future global economy will likely be mediated by millions of specialized AI agents, embedded within firms, supply chains, and public services. The current paradigm of ad-hoc, heuristic-based delegation is insufficient. What is proposed is a paradigm shift from largely unsupervised automation to verifiable, intelligent delegation — that allows us to safely scale towards future autonomous agentic systems, while keeping them closely tethered to human intent and societal norms.
