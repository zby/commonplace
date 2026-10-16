---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Trajectory-informed memory generation workflow: subtask extraction, consolidation, LLM-guided retrieval and reported single-agent AppWorld delivery, bounded to the frozen paper."
run-id: AAS-2026-10-14-2603-10600v1-a956324c9a82-01
reviewed-boundary: "arxiv-2603.10600v1-html-captured-2026-10-14"
---

# Trajectory-informed memory generation workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is **completed AppWorld trajectories → subtask-level tips → consolidated memory → LLM-guided selection for a later request → single-agent execution and evaluation**. This combination is selected because the paper describes its handoffs and reports held-out results for it. It connects production to a later consumer without inventing a multi-agent runtime or an online update after every test task. The frozen capture supplies doctrine/design and reported operation, not executable prompts, code or inspectable execution traces. SRC-1, §§3.1.4–3.3.3, §§4.1–4.2; [boundary](boundary.md#boundary-and-evidence).

The request-to-result portion starts with a new natural-language AppWorld task. Memory generation is its prerequisite, built from earlier train/dev executions. The source does not supply a particular full trajectory through all these phases. This account therefore traces a documented workflow configuration, not a witnessed successful run. Its existing route identities are [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction), [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation), [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection) and [RT-RTE-agent-execution](runtime.md#rt-rte-agent-execution).

### 1. Prepare outcome evidence and delegate focused extraction

A completed trajectory supplies sequential contexts, thoughts, actions and results, with optional evaluation reports. The extraction pipeline constructs reasoning categories, semantic patterns and an outcome classification. It then traces backward from failure, recovery, inefficiency or success indicators to decisions and proposes corrective or reusable guidance. Ground-truth labels are used when available; otherwise outcome is inferred from the agent's self-reflective signals. External verification is consequently not a universal prerequisite for proposing a tip. These are requested semantic judgments, not independently established causal attribution. SRC-1, §§3.1.1–3.1.3; [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction), including its retained passage on optional labels.

For the selected subtask mode, a segmentation LLM receives the full trajectory. Its handoff describes each subtask generically, identifies applications, preserves source step ranges and states the purpose. Separate extraction calls focus on individual logical phases and return 2–4 tips each. The orchestration described is a pipeline allocating model work; it is not an agent autonomously recruiting other agents. The paper gives no concrete scheduler, retries, worker security principals or exact extraction prompt envelope. SRC-1, §3.1.4.

> An LLM analyzes the full agent trajectory and segments it into logical subtasks. For each subtask, the model produces a generalized description (deliberately generic, e.g., “Authenticate with Spotify” rather than “Login as user@gmail.com”), the set of applications involved, the step range in the original trajectory (maintaining traceability), and the subtask’s purpose.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

The source's Spotify recommendation example separates API discovery, authentication, paginated retrieval and analysis. It illustrates how different phases become separately reusable; it is not a supplied execution record. Tips retain advice, explanatory purpose, steps, trigger, category, priority and provenance metadata. What crosses toward management is structured guidance, not merely a transcript or terminal answer. SRC-1, §§3.1.3–3.1.4.

### 2. Consolidate and admit retained guidance

The management pipeline generalizes descriptions, embeds them and clusters similar operations. Associated tips within each cluster are handed to a consolidation LLM for deduplication, conflict resolution and synthesis. The successor consists of consolidated guidance plus a canonical description, vectors and metadata. Later retrieval therefore sees transformed material: original descriptions can be replaced, and complementary tips can become an ordered composite. SRC-1, §§3.2.1–3.2.4; [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation).

This is the workflow's instruction-admission decision. The model decides merged content under requested precedence rules; no separate per-entry human approval or independent test of the merged prescription is established. The retained runtime passage documents preference for successful-trajectory tips over failed-trajectory tips and proven recovery over speculative prevention. That preference can displace conflicting advice; it does not prove the chosen prescription correct. Executable admission checks, failed-merge handling, transactional writes and rollback are uninspected. SRC-1, §3.2.3; [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation).

### 3. Select guidance for the new request and hand it to the consumer

A new task triggers LLM-guided selection before consumer reasoning. The selection model analyzes task context and category, proposes metadata filters and relevant tip categories, and constructs a query. The retrieval system performs similarity search, filtering and priority-weighted ranking; the selected evaluation configuration requests five tips. The cosine alternatives have their own parameter variants, so five is not a system-wide invariant. SRC-1, §§3.3.2–3.3.3, §4.1.4; [RT-RTE-llm-selection](runtime.md#rt-rte-llm-selection), [RT-CLM-reported-results](runtime.md#rt-clm-reported-results).

Selected tips are formatted with priority, category, content, purpose, steps and trigger in a guidelines section after task context and before standard agent instructions. Unselected tips and original trajectories are not described as delivered to this consumer. The model receives advice, not API permissions or a hard execution guard. Delivery here means prompt insertion; activation requires separate evidence that the advice changed behavior. SRC-1, §3.3.3; [RT-BAP-guidelines-channel](runtime.md#rt-bap-guidelines-channel), which retains the insertion passage.

### 4. Execute, verify and terminate

The reported consumer is one GPT-4.1 ReAct-style agent. It reasons, chooses API actions, observes results and continues until self-declared completion or unrecoverable failure. The agent owns action choice; application APIs execute state changes. The memory pipeline does not own those effects. The evaluation protocol states independent tasks with a maximum of 30 reasoning-action steps; enforcement and the exact limit-exhaustion return are not inspectable. SRC-1, §§4.1.2, 4.1.5; [RT-RTE-agent-execution](runtime.md#rt-rte-agent-execution).

AppWorld's final-state tests supply the external result oracle. A task counts as successful only if all its tests pass; a scenario counts only if every task variant passes. Thus agent-declared completion and accepted benchmark success are different boundaries. Verification measures final API/database/end-state requirements, not the truth of each retained tip or the correctness of every intermediate action. The paper does not establish a failed evaluation automatically scheduling a repair attempt. Terminal response format and delivery to a human or application caller remain unspecified. SRC-1, §4.1.1.

> A task is successful only if all unit tests pass.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

### Failure and recovery path

The paper illustrates an agent attempting checkout without a configured payment method, receiving an error, recognizing the missing prerequisite, adding payment information and retrying successfully. The consuming agent performs that correction; the memory system's role is to extract the failure-recognition-correction sequence as future recovery guidance. This is a design example, not evidence that a particular retrieved tip caused a successful retry. SRC-1, §2, “Recovery extraction from failure handling.”

> For example, if an agent attempts checkout without payment configured, receives an error, recognizes the missing payment method, adds payment information, and successfully retries, this entire sequence should be encoded as a recovery tip including the failure pattern, recognition signals, and correction steps.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/trajectory-informed-memory-generation-a956324c9a82/kb/agentic-system-analyses/state/AAS-2026-10-14-2603-10600v1-a956324c9a82-01/sources/2603.10600v1.html`

Unrecoverable failure terminates the described consumer loop. Complete failures can also inform extraction, but there is no supplied evidence of automatic post-test regeneration, recovery from pipeline model errors or restoration of previous memory versions. Reported aggregate improvements do not establish these missing recovery mechanisms or guarantee benefit for an individual request. The runtime's retained counterexamples show that guidance can also interfere with performance. SRC-1, §§3.1.1–3.1.3, §§4.1.2, 4.2–4.4; [RT-CLM-reported-results](runtime.md#rt-clm-reported-results).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-trajectory-extraction](runtime.md#rt-rte-trajectory-extraction)

Workflow handoff: segmentation assigns scoped logical phases to independent extraction calls; source step ranges preserve traceability across that handoff. This is model-call work allocation, not established multi-agent execution delegation. SRC-1, §3.1.4; the retained segmentation passage is in the workflow account. Exact scheduling, caller return schema and extraction-call recovery are uninspected.

#### On [RT-RTE-tip-consolidation](runtime.md#rt-rte-tip-consolidation)

Workflow acceptance boundary: outcome-precedence instructions govern replacement of contradictory advice during merging, not a separately verified acceptance test. No post-merge benchmark gate or version restoration mechanism can be established from the captured design. The later consumer receives selected consolidated guidance rather than all original claims. SRC-1, §§3.2.3–3.3.3; the record's retained conflict-precedence passage supplies the decision evidence.

#### On [RT-RTE-agent-execution](runtime.md#rt-rte-agent-execution)

Workflow delivery boundary: prompt insertion delivers memory to the agent; termination ends execution; final-state tests determine benchmark success. These are separate events. Evaluation rejection is a failed score, not an established trigger for another attempt. Consumer-led correction is illustrated by the checkout example retained above; the source does not provide a run witnessing that correction or attributing it to a retrieved tip. SRC-1, §2 and §§4.1.1–4.1.5.
