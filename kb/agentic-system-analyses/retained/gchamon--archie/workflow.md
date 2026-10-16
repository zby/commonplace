---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Archie workflow account: profile selection, configuration update and external-agent handoff, with end-to-end agent delivery unestablished."
run-id: AAS-2026-10-15-archie-1ab3d8b8ff03-01
reviewed-boundary: 76caf94548cf76f2399d9a7446da15e0daa22685
---

# Archie workflow report

## Workflow account

No multi-step **agent task workflow through delivery** can be established inside the selected subsystem. What can be traced is a multi-step launch preparation sequence: select a profile, update the external runtime's default role, and invoke that runtime with role arguments. This account selects `omp:gpt` because it exposes both the persistent configuration handoff and the foreground launch in one shipped path. It does not join the assistant plan to the launcher to manufacture a documentation-answering workflow. The boundary is the runtime-client subsystem, not the external `omp` agent loop ([boundary](boundary.md)).

The evidence is SRC-1 implementation in `deployment-packages/local/lib/zsh/commands-agents.sh`, and doctrine/design in `docs/epics/assistant.md` and `docs/work-items/assistant-03-agent-backed-documentation-guide.md`, all at the frozen revision. I read these three files completely; this confirms the runtime baseline without adding a source or expanding the functional boundary. No target code was executed and no run trace supplies an actual request, worker result, verification decision or delivered answer.

### Request and consequential handoffs

1. **Make the profile available.** The shipped deployment/loading chain makes shell functions and aliases available, conditional on installation and sourcing. This is preparation, not an agent job. The deployment and loader passages are retained in [RT-RTE-shell-load](runtime.md#rt-rte-shell-load).
2. **Select the profile.** A caller invokes `omp:gpt` with any task arguments. The alias resolves to `omp:openai`; that function supplies a fixed default selector to the helper before launching. This is deterministic shell dispatch, not model-led delegation. The implementation explicitly binds the alias (SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`):

   > alias omp:gpt='omp:openai'
   > --- `deployment-packages/local/lib/zsh/commands-agents.sh`

3. **Prepare retained configuration.** The helper requests the existing `modelRoles`, transforms its symbolic JSON by assigning `.default`, and passes the whole resulting value to `omp config set`. The shell helper owns transformation and ordering; external `omp` owns persistence. The selected default is `openai-codex/gpt-6-luna:medium`. The minimum helper passage and configuration admission account are in [RT-RTE-default-update](runtime.md#rt-rte-default-update). A caller's choice of profile does not establish separate human approval of each transformed field.
4. **Transfer control to the external runtime.** If the helper returns success, the function calls foreground `omp` with `--smol`, `--slow`, `--plan` and `--model` selectors, followed by the caller's unchanged `"$@"`. The complete ordinary launch passage is in [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch). These arguments supply role requests and caller input, not worker assignments, worker-specific evidence packets or acceptance criteria. Role use, interpretation of duplicate caller options, model-visible context, tool execution and subsequent decisions belong to the external runtime and are uninspected. In particular, `--plan` does not establish an executed planning stage, nor do several selectors establish several agents.
5. **Return at the client boundary.** The wrapper does not synthesize a final artifact or test an answer. External process output is not transformed by this function, and its final command ordinarily supplies the function's return status. This establishes the source-level return arrangement, not that a task answer was delivered. No inspected task contract defines completion, reviewer acceptance or successful end-to-end delivery ([RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch)).

### Verification, rejection and recovery

The available gate checks **helper status**, not task quality. A nonzero helper result makes the profile return 1 before the agent launch. The helper itself returns 1 on a failed assignment/pipeline, or propagates the setter's status as its last command. These are executable control-flow checks, not an answer oracle or independent review. They cannot certify correct model selection, provider readiness or valid persisted state. The runtime baseline retains the exact helper and launch passages and the pipeline-status qualification: without an established pipeline-failure option, an upstream getter failure need not cause the whole pipeline to fail ([RT-RTE-default-update](runtime.md#rt-rte-default-update); SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh`).

A second failure point is after successful configuration: the external launch can fail while the changed default remains. Inspection of the complete helper and profile function shows no compensating restore, retry or fallback in that wrapper. The wrapper returns control to its caller; any repair or rerun requires caller or external-runtime action, not an implemented Archie recovery stage. This is a bounded source-level finding about those functions, not a claim that external `omp` lacks recovery. Neither failure case was exercised. Direct `omp` invocation can bypass the profile gate altogether ([RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff)).

### Planned workflow is not implemented delivery evidence

The assistant epic proposes a GUI topic picker, a Kitty-hosted TUI and optional constrained coding-agent support. The work item leaves capability restrictions, context injection, provenance presentation and no-agent fallback to be defined. Its status is Planned. The source explicitly describes decisions still to make (SRC-1, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`):

> - Define the restrictions that keep assistant mode safe, including behavior
>   when an agent wants to edit files, execute commands, or answer beyond the
>   documented Archie scope.
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

These design requirements do not supply a running handoff, rejection mechanism or recovery path for the shipped launcher. [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) retains the planned guide claim. The missing external implementation and execution evidence prevent conclusions about agent delegation, answer verification, failure recovery inside the agent, and completed task delivery. They do not establish those behaviors are absent in the external runtime.

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

#### On [RT-RTE-default-update](runtime.md#rt-rte-default-update)

Workflow role: prerequisite configuration stage. Its reported success permits the next shell command; it is not an acceptance decision on agent work. Failure can stop this profile before launch, but the gate supplies no task-quality verdict. A later launch failure does not trigger wrapper rollback of the earlier update.

#### On [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch)

Workflow role: final inspected handoff, not a demonstrated request-to-answer workflow. The shell supplies selectors and forwarded caller arguments, then yields next-step ownership. No worker-return merge or answer acceptance occurs in the inspected function. Delivery is established only as the wired process handoff/return arrangement; an agent-produced result and its acceptance remain uninspected.
