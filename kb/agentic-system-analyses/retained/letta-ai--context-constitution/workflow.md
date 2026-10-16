---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Context Constitution workflow account: task-triggered progressive disclosure, optional memory maintenance and the limits of delivery evidence."
run-id: AAS-2026-10-15-context-constitution-7a352d7408f6-01
reviewed-boundary: "964f30137ace9eade1aef112992ed6539b61bbb0"
---

# Context Constitution workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is **task-triggered progressive disclosure**: recognize a situation from an in-context cue, inspect a referenced skill's metadata, and load its full contents only if useful. It is selected because the Constitution itself gives this ordered example, rather than requiring the analyst to assemble a workflow from unrelated affordances. The request is bounded to a current task that matches a retained cue; no concrete user request, task artifact or execution transcript is supplied. The trace therefore establishes a prescribed context-acquisition workflow, not a demonstrated request-to-delivery run (SRC-1, `constitution/CONSTITUTION.md`; [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure)).

This report directly inspected the complete `constitution/CONSTITUTION.md` and `constitution/AFFORDANCES.md` at the frozen revision in [boundary](boundary.md). These reads supply doctrine/design evidence, with no additional source or execution evidence. The external Letta harness remains outside the implementation boundary.

### From task situation to usable context

The source gives the consequential decisions explicitly:

> 1. Observe that the current situation matches what's described in an in-context memory, which references a skill
> 2. Read the top-level metadata of the skill to determine if it's useful for the scenario
> 3. If so, read the full skill which may in turn reference other skills or external memory files
> --- `constitution/CONSTITUTION.md`

The foreground agent owns each next step. The first handoff is informational: an in-context memory supplies a cue and skill reference. The metadata read then supplies a usefulness description, not yet the full procedure. The agent judges relevance and either follows the reference or stops that expansion. The conditional “If so” supports declining to load an irrelevant skill; it is not an answer-correctness test. A loaded skill may supply further references, permitting deeper retrieval under the same task-relative selection rule. Exact tool schemas, return payloads and resolution of broken references are not specified (SRC-1, `constitution/CONSTITUTION.md`; [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure)).

The harness declares automatic skill metadata and a memory-filesystem tree in the system prompt, while the agent maintains additional discovery links. External memory contents must be retrieved on demand. Thus a discoverable reference is not equivalent to having its contents in the model-visible window. Environment-owned skills and agent-owned skills can both be available; the workflow does not make environment instructions agent-owned memory (SRC-1, `constitution/AFFORDANCES.md`).

### Delegation and verification boundaries

The selected three-step workflow does not require a subagent. Its consequential retrieval decisions remain with the foreground agent. The separate delegation affordance names Recall for past conversations, Reflection for conversation-based memory modifications, and Defragmentation for memory organization. These are available auxiliary roles, not evidenced mandatory stages of this workflow. No delegation prompt, supplied task packet, result schema, completion notification or foreground acceptance rule is given. It is therefore not possible to trace a particular delegated result back into task delivery (SRC-1, `constitution/AFFORDANCES.md`; [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context)).

If the agent uses those roles, message-thread isolation does not imply return-only effects: memory is shared across the same agent's conversations. The source does not identify who merges concurrent edits or recovers a failed delegate. Keeping intermediate work out of the foreground window is the stated purpose, but actual context savings are unobserved (SRC-1, `constitution/AFFORDANCES.md`; [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context)).

The only verification decision established within the selected retrieval sequence is the agent's usefulness judgment on metadata. No expected-answer provider, independent task evaluator or user sign-off is supplied. Memory updates likewise need not have explicit reward or verification, as quoted in [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). This limits claims of correctness, not the existence of the prescribed relevance check (SRC-1, `constitution/CONSTITUTION.md`).

### Failure, rejection and recovery

There are two source-supported boundaries, neither an observed failure episode. First, metadata can fail the usefulness decision, preventing full loading of that skill. The source gives no retry or alternative-skill search procedure. Second, if subsequent experience warrants a durable memory edit through MemFS, local editing and committing do not by themselves deliver it to underlying memory: successful remote push is the declared propagation gate. Failed or absent push therefore leaves the proposed file change unpropagated under that contract. The external synchronization machinery owns that transition; this repository supplies neither its implementation nor a failed-push recovery algorithm. Bespoke memory tools remain an alternative with unspecified admission semantics (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`; [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)).

For context that has been compacted out of the conversation, persisted history remains searchable under the declared affordances. This is a possible recovery source, not evidence that a missing detail is detected or restored. The host's compaction summary may itself omit information; no summary acceptance or repair check is supplied (SRC-1, `constitution/AFFORDANCES.md`; [RT-RTE-history-compaction](runtime.md#rt-rte-history-compaction)).

### Completion, cleanup and later consumption

The policy expects loaded content to help the current task and then be released. It does not specify what task artifact or response constitutes delivered work, how completion is detected, or a selective-eviction tool that removes the skill. The account therefore ends at requested usable-context supply and prescribed cleanup, not at a verified user-facing result (SRC-1, `constitution/CONSTITUTION.md`; [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure)).

Moving guidance out of always-visible memory is itself conditional, rather than an unconditional token-reduction step:

> Context should only be removed from the in-context memory and placed externally if the Letta agent is confident that it has laid the groundwork (e.g. through updating its index) to retrieve the context reliably when necessary in the future.
> --- `constitution/CONSTITUTION.md`

Optional durable maintenance can prepare the next traversal: corrected assumptions, user preferences or behavioral guidance may change system memory or external memory and its index. This is not required after each retrieval. Successful file propagation and later system-prompt visibility are separate from proving that the next inference follows the retained guidance. No particular update, later traversal or improvement is observed (SRC-1, `constitution/CONSTITUTION.md`, `constitution/AFFORDANCES.md`; [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-BAP-system-prompt](runtime.md#rt-bap-system-prompt)).

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

#### On [RT-RTE-context-disclosure](runtime.md#rt-rte-context-disclosure)

Workflow role: the selected ordered retrieval sequence. The foreground agent owns cue matching, metadata assessment and conditional full loading. Metadata usefulness is an expansion check, not a task-output oracle. Task-result acceptance and delivered-result criteria are unspecified; the prescribed release of completed-task content is not evidence of an implemented cleanup step.

#### On [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Workflow role: optional durable follow-up, not a mandatory stage of the selected retrieval sequence. File-based propagation has a declared success condition distinct from local preparation. No source-supported retry owner or repair sequence closes a failed-push branch, and a successful push alone does not establish later behavioral dependence on the update.

#### On [RT-RTE-subagent-context](runtime.md#rt-rte-subagent-context)

Workflow role: available auxiliary delegation, not an evidenced handoff in the selected sequence. Absent task-packet and return contracts prevent tracing delegated verification or delivery. Shared persistent memory prevents interpreting isolated message threads as a guarantee that only an explicit result returns.
