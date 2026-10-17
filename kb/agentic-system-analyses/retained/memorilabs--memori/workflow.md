---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Memori workflow account of a Claude Code turn: ambient recall, foreground task completion, capture and partial-failure delivery."
run-id: AAS-2026-10-17-memori-fd4a0418c09b-01
reviewed-boundary: 574b1ea3e876f100ef82c37817d603eb7e258e59
---

# Memori workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is one non-trivial Claude Code user turn under the shipped Memori skill: recall before work, foreground task completion, then submission of the drafted response and optional tool trace. It is selected because the source supplies an ordered agent-facing procedure and its executable subprocess handoffs together, including a consequential partial-failure branch. It does not establish a Memori-owned autonomous task scheduler. The enclosing agent remains responsible for the user's work and final delivery.

The account develops [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill), [RT-CLM-ambient-lifecycle](runtime.md#rt-clm-ambient-lifecycle) and [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance), rather than declaring duplicate records. Inspection covers the complete `integrations/claude-code/SKILL.md` and `integrations/claude-code/index.ts` in SRC-1. The skill supplies doctrine/design; the CLI supplies implementation. No execution trace or experiment was supplied or performed. Host obedience, successful service operation, final-answer quality and later memory benefit remain unobserved. Hosted derivation and persistence internals retain the limits in [boundary](boundary.md#boundary-and-evidence).

### Request, recall and return to the foreground agent

The user supplies the task to Claude Code, not to a Memori task-execution loop. If the shipped skill is loaded and followed, the foreground agent classifies the turn under its non-trivial-turn policy and invokes the Bun CLI through Bash. Trivial turns, purely self-contained turns and explicit user storage opt-out are instructed exceptions, not CLI-enforced exceptions. The skill also requires recall before external lookup. This sequencing is a behavioral policy, not a runtime barrier preventing an early answer or tool call (SRC-1: `integrations/claude-code/SKILL.md`; see [RT-CLM-ambient-lifecycle](runtime.md#rt-clm-ambient-lifecycle)).

The Bash handoff supplies command flags and the host's subprocess environment. The CLI resolves API credentials and entity, derives project from configuration or the workspace basename, and permits explicit overrides. For recall it intentionally does not apply the default write-session identity. Consequently the request is project-scoped across sessions unless the foreground agent supplies `--sessionId`; this is a request selector, not proof of server authorization (SRC-1: `integrations/claude-code/index.ts`).

The CLI delegates retrieval by GET to `/agent/recall`, supplying entity, project and optional explicit session/date/source/signal filters. It does not pass the user's topic as a query. It rejects `--query`, incomplete source/signal pairs and pairs outside its fixed mapping before fetching. These checks accept or reject request shape, not the relevance or truth of returned memory. The HTTP helper rejects non-OK status, returns an empty object for 204, and otherwise parses JSON. The dispatcher prints that result to stdout and exits successfully; the foreground agent then owns interpretation. No inspected step checks returned memory against the user's request before that return (SRC-1: `integrations/claude-code/index.ts`; [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill)).

### Foreground work and capture handoff

The next step is the user's actual work, not a delegated Memori worker task. The skill makes that division explicit:

> 5. Answer or complete the user's actual request. Memory should improve
>    context, not replace the answer.
> 6. After drafting the final response for a non-trivial turn, run
>    `advanced-augmentation` with that final response. This is mandatory
>    ambient bookkeeping and must be the last memory step of the turn.
> --- `integrations/claude-code/SKILL.md`

The foreground agent chooses how to use the recalled material, executes whatever task tools its host permits, and drafts the answer. Task-specific checking, rejection of a faulty answer, sub-agent coordination and acceptance by the user are not specified by this Memori procedure. Their absence from this selected procedure does not establish that the enclosing host lacks them. Memori is not shown verifying that the submitted assistant text matches the subsequently delivered answer.

For capture the agent supplies user and assistant text plus optional model, summary and trace. Trace entries must have a string name, object args and a result key; omission produces an empty tools array. The skill asks not to include secrets or large raw logs, but these shape checks do not enforce redaction, faithful trace coverage or successful task execution. The CLI also prints parsed flags to stderr, so submitted content is not confined to outbound HTTP payloads (SRC-1: `integrations/claude-code/SKILL.md`, `integrations/claude-code/index.ts`).

The CLI requires credentials, entity, project, session and nonempty user/assistant flags. It constructs two text messages: the user message has null trace and the assistant message carries the supplied trace. It first awaits `/agent/conversation/turn` with attribution, messages, project and session. Only after that request succeeds does it submit `/agent/augmentation` to the collector with conversation messages, metadata, optional session summary and trace. The service, not the foreground agent or a local critic, owns inaccessible derivation and downstream admission. There is no per-content human confirmation in this CLI; explicit opt-out remains skill guidance. These are open user turns, with no expected-answer oracle or bounded improvement experiment established (SRC-1: `integrations/claude-code/index.ts`; [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill)).

### Rejection, recovery and what counts as delivered

Malformed trace or missing required input rejects capture before the first POST. A failed conversation-turn request propagates to the top-level error handler, prints an error and exits 1; collector submission is not reached. In contrast, collector failure after the turn request is caught locally:

>   try {
>     await post(`${COLLECTOR_URL}/agent/augmentation`, augPayload);
>   } catch (e) {
>     console.error(`[memori] collector augmentation failed (non-fatal): ${(e as Error).message}`);
>   }
>
>   return { success: true, augmentation: true };
> --- `integrations/claude-code/index.ts`

This branch does not roll back the accepted turn request or retry collector submission in the inspected CLI. It still yields success JSON and exit 0. Thus an `augmentation: true` result is not a receipt proving derived memory exists, and a successful first POST is only client-visible HTTP acceptance, not inspected durable storage. The recovery owner for continuing the user's task is the foreground agent under this instruction:

> On success, commands print JSON to stdout and exit 0. On failure, errors print
> to stderr and exit 1. If memory fails, briefly report the memory issue when
> relevant and continue with the user's actual request using current context.
> --- `integrations/claude-code/SKILL.md`

There are therefore separate delivery boundaries. CLI delivery is JSON/error and exit status to the invoking host. User-facing delivery is the enclosing agent's answer or completed work; this source does not supply its transport acknowledgment or task-success test. Memory delivery to a later turn requires a later retrieval, successful server selection and foreground use. Default cross-session recall makes that route possible but proves none of those events occurred. The source supports a policy-coordinated multi-step workflow with local request validation and graceful degradation, not verified end-to-end task or memory success.

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

#### On [RT-RTE-claude-skill](runtime.md#rt-rte-claude-skill)

Workflow selection: the inspected procedure joins pre-work recall, foreground task completion and post-draft capture in one shipped lifecycle. The foreground agent owns sequencing and user delivery; Bash/CLI handles bounded memory requests, not task delegation to another agent.

Verification boundary: request prerequisites, filter pairing, trace shape, HTTP status and JSON decoding can reject a subprocess operation. They do not accept the user's work product or establish memory truth. No task-answer oracle is established by these checks.

Recovery/delivery boundary: failure before conversation-turn acceptance stops the command; later collector failure returns success after logging. Host continuation is instructed, not observed. The final user answer and the two remote write requests have no inspected common transaction or end-to-end success acknowledgment.
