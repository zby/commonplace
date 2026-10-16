---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Tracecraft workflow account: shipped agent task claiming, progress exchange and completion handoff, with dependency rejection and delivery limits."
run-id: AAS-2026-10-14-tracecraft-9c4af961e8e2-01
reviewed-boundary: "97c6b7447f8e696f0116357d9f86bb0ece25e5b1"
---

# Tracecraft workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is the shipped agent coordination procedure: check peers and mail, claim a task, do work outside Tracecraft, share progress, and leave completion context for another agent. It was selected because the Claude Code example supplies an ordered procedure and the Hermes skill supplies corresponding read-back and file-sharing commands. This is a prescribed workflow backed by inspectable coordination code, not an observed agent run or a demonstration of a particular coding task. The request's origin, task decomposition and actual work execution are outside the established procedure; no source-supported enclosing scheduler can be inferred from it.

Evidence is SRC-1 implementation and doctrine/design within the [boundary](boundary.md). This member directly inspected `examples/claude-code/CLAUDE.md`, `examples/hermes-agent/SKILL.md`, `sdk/tracecraft/cli/steps.py` and `sdk/tracecraft/cli/artifacts.py` at the frozen revision. The added detail is handoff construction, read-back verification and blocked/review recovery. No target code or evaluator was executed. The runtime records remain the baseline for configuration, storage effects and backend limitations.

### Request, ownership and progress

1. **A host agent receives work and checks coordination state.** The example assumes an agent already has work; it does not allocate a task or launch that agent. The agent checks registered peers and inbox before starting. Configuration determines project, bucket and caller-supplied agent identity through [RT-RTE-init-config](runtime.md#rt-rte-init-config). Loading and following the shipped prompt remains the external host's responsibility through [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt), not a storage invariant.
2. **The agent chooses and claims a step.** [RT-RTE-step-control](runtime.md#rt-rte-step-control) normalizes the requested identifier, conditionally writes a claim, then writes in-progress status. A conflict rejects the claim with the stored owner's name; the procedure does not automatically choose another task. Conditional arbitration depends on the S3 service contract; Hermes's example HF setup uses the backend for which the CLI explicitly warns claims are racy. The claim is cooperative ownership state, not an authenticated worker assignment or a lease.
3. **The agent works outside Tracecraft and shares progress.** The prompt requests shared memory writes through [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) and periodic inbox checks through [RT-RTE-mail-exchange](runtime.md#rt-rte-mail-exchange). The agent, not Tracecraft, chooses the next action and interprets returned text. These commands preserve progress and messages across invocations; they do not substantively verify the work or inject it into another model's context. File upload/download through [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share) is a shipped optional exchange in the same skill, not a mandatory step of every task.

The ordered procedure is explicit (SRC-1 doctrine/design, `examples/claude-code/CLAUDE.md`):

> 1. Check `tracecraft agents` to see who else is working
> 2. Check `tracecraft inbox` for messages before starting
> 3. Run `tracecraft claim <your-step>` before starting work
> 4. Share progress via `tracecraft memory set`
> 5. When done, run `tracecraft complete <step> --note "context for next agent"`
> 6. Check `tracecraft inbox` periodically for messages from other agents
> --- `examples/claude-code/CLAUDE.md`

### Verification, handoff and delivery

The Hermes skill asks the acting agent to verify writes by reading state back, and to ask a message recipient to check inbox. This checks storage visibility or recipient retrieval, not task correctness. It does not define an expected substantive answer, invoke an independent reviewer, or establish that any agent obeyed the request (SRC-1 doctrine/design, `examples/hermes-agent/SKILL.md`):

> After any action, verify with the corresponding read command:
> - After `memory set` → `memory get`
> - After `send` → ask the recipient to check `inbox`
> - After `claim` → `step-status`
> --- `examples/hermes-agent/SKILL.md`

When the agent decides work is done, completion checks claim ownership unless forced, writes status, and writes [WF-OBJ-handoff](#wf-obj-handoff). Optional recipient, next-action text and note supply context; optional changed files come from a fixed Git diff subprocess. The latter identifies tracked staged/unstaged changes relative to HEAD, not all produced files or the correctness of their contents. Subprocess failure becomes an empty list rather than a completion rejection (SRC-1 implementation, `sdk/tracecraft/cli/steps.py`).

Delegation here is a **recorded handoff**, not dispatched execution. A named next agent receives no automatic message merely because `--to` is set. The completion command stores that name and prints it. The next host agent must be independently running and choose to read relevant state, messages or files. `step-status` prints state/owner and `wait-for` tests completion; neither displays the handoff's note or next action. The handoff is separately addressable through bucket/store access, but these inspected step commands provide no handoff-fetch-and-execute operation (SRC-1 implementation, `sdk/tracecraft/cli/steps.py`; [RT-RTE-step-control](runtime.md#rt-rte-step-control)).

Delivery therefore has several bounded endpoints. The producer receives a completion receipt after the status and handoff writes return. A dependency waiter returns when every selected status equals complete through [RT-BAP-step-polling](runtime.md#rt-bap-step-polling). An optional artifact is locally delivered when download succeeds; a missing object rejects download. These endpoints establish command effects, not receipt of all handoff context by a model or an accepted external work product. Status is written before handoff, so a waiter can return before that context exists. The protocol has no atomic bundle of completed state, note and files (SRC-1 implementation, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/cli/artifacts.py`; [RT-RTE-artifact-share](runtime.md#rt-rte-artifact-share)).

### Failure and rejection path

The same completion path supports blocked and needs-review outcomes. The producer selects the outcome; code rejects using both flags together. A blocked dependency makes the waiter fail immediately and asks the caller to resolve it and rerun. Needs-review prevents successful return and is reported during polling, but does not launch a reviewer. Timeout rejects the wait when statuses have not all become complete. These are state gates, not judgments about the contents of the work (SRC-1 implementation, `sdk/tracecraft/cli/steps.py`; [RT-RTE-step-control](runtime.md#rt-rte-step-control)).

Recovery belongs to an external agent or operator. They must resolve the substantive issue and call completion again; the same owner can overwrite blocked/review status with complete. A different agent's completion is rejected unless `--force` bypasses ownership. The original claim remains, so recovery is not automatic lease reclamation. No mandatory distinct reviewer or review evidence is checked before clearing needs-review. This preserves a cooperative escape path after a crash, while limiting what a complete state proves.

## Shared records

### Components

none declared in this member

### Operative objects

#### WF-OBJ-handoff
Label: Completion handoff document

Source-native identity: `steps/<sid>/handoff.json`, written by `complete`. Substrate: JSON in the configured project bucket. Its schema, sender, source step, recipient, state and timestamp are symbolic fields; note and next-action values carry natural-language instructions for a later human or agent. Optional changed-files is a symbolic list derived from Git. Interpretation of the prose remains external; the inspected status consumers do not execute it.

This is distinct from [RT-OBJ-step-state](runtime.md#rt-obj-step-state), whose claim/status documents determine ownership and polling. It is the output context of [RT-RTE-step-control](runtime.md#rt-rte-step-control), not a second declaration of that route. All handoff fields share one overwrite and storage horizon; a later completion replaces the document. Recipient attribution does not authenticate or dispatch a recipient. Evidence: SRC-1 implementation, `sdk/tracecraft/cli/steps.py`:

> handoff = {
>     "schema": 2,
>     "from_agent": agent,
>     "from_step": step_id,
>     "next_agent": next_agent,
>     "state": state,
>     "next_action": next_action,
>     "note": note,
>     "created_at": now,
> }
> --- `sdk/tracecraft/cli/steps.py`

> store.put_json(f"steps/{sid}/handoff.json", handoff)
> --- `sdk/tracecraft/cli/steps.py`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-step-control](runtime.md#rt-rte-step-control)

Workflow-specific rejection and recovery: the waiting caller receives a failure on blocked state, not an automatically scheduled repair. Review state is reported and remains nonterminal for the waiter; clearing it requires another caller-driven state write, not a reviewer identity check. The producer's [WF-OBJ-handoff](#wf-obj-handoff) records context, but successful dependency polling does not ensure that document was delivered. SRC-1 implementation, `sdk/tracecraft/cli/steps.py`:

> raise click.ClickException(
>     f"Step {step_id} is blocked (agent: {agent}) — it will not "
>     f"complete without intervention. Resolve it and re-run wait-for."
> )
> --- `sdk/tracecraft/cli/steps.py`

> if status == "needs_review":
>     needs_review.append(step_id)
> if status != "complete":
>     all_done = False
> --- `sdk/tracecraft/cli/steps.py`

#### On [RT-BAP-agent-prompt](runtime.md#rt-bap-agent-prompt)

Workflow verification is a requested agent action. The Hermes read-back checklist above supplies a concrete verification procedure, but its reference outcome is a readable stored value/status or recipient inbox retrieval, not an oracle for a correct task result. Delivery of the skill, compliance and successful multi-agent execution remain unobserved.
