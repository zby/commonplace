---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "RightMemory native-assistant workflow from context delegation through evidence submission, isolated reconciliation and publication receipt."
run-id: AAS-2026-11-08-rightmemory-cbec05309c2b-01
reviewed-boundary: "62534bd82c58718f31c99692fed4c5d159e218ec"
---

# RightMemory workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is the shipped native-assistant lifecycle: retrieve useful context for user work, submit consequential evidence, reconcile a ready batch in an isolated native Update child, then report the program's publication outcome. It is selected because one shipped skill explicitly connects these steps and assigns their owners; the account does not combine unrelated APIs into a hypothetical agent pipeline. RightMemory manages state and admission, while the enclosing host executes the user's coding task and supplies the native model workers. The canonical route is [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant), with policy supplied through [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions). SRC-1: `skills/rightmemory-assistant/SKILL.md`, `rightmemory/assistant.py`.

> The main agent owns submissions and Update delegation. Retrieve and Update run as native subagents with access to the supplied directories; RightMemory tools manage the queue, isolation, validation, and publication.
> --- `skills/rightmemory-assistant/SKILL.md`

This is implementation and doctrine/design evidence at the frozen revision, not a supplied successful run. In particular, neither native delegation nor application of returned guidance is observed. Added inspection within SRC-1 covers `skills/rightmemory-assistant/SKILL.md`, `rightmemory/assistant_context.py`, `rightmemory/assistant.py` (context, submission, claim, preparation and completion methods), `rightmemory/assistant_write.py` (preparation and completion), and `rightmemory/prompts/update.md`. These are within the registered whole-system boundary; no new source is introduced.

### 1. Main agent delegates a context need

The skill directs retrieval when stored context could materially change the work. The main agent supplies the need, bound active root, stable conversation session ID and preparation command to a native Retrieve child. That child calls `context`, reads its instructions and pending submissions, inspects real files, and returns useful context with sources. Prior context may be passed to reduce redundant reading. The main agent must reconcile this return with the conversation, prefer current user instructions over stale memory, and apply relevant guidance. These are requested model behaviors, not code-enforced relevance or compliance guarantees. SRC-1: `skills/rightmemory-assistant/SKILL.md`; [RT-BAP-host-context](runtime.md#rt-bap-host-context).

The service settles proven terminal outcomes and publishes its outbox before preparing retrieval. Preparation refreshes synchronization, inventories the graph and correction source files, checks file-view imports, and materializes pending evidence and role instructions. It returns live source paths, a memory commit identifier, import directories and status metadata. The commit identifier does not freeze later child reads: the active files remain live. The returned pending block is not itself admitted Memory. SRC-1: `rightmemory/assistant.py`, `rightmemory/assistant_context.py`.

> The active root remains live. Only pending submissions and shared role
> instructions are materialized for this invocation; no model, worker, or
> delivery-history state is created.
> --- `rightmemory/assistant_context.py`

Thus this native handoff does not use the internal retrieval selector's source-resolution/output-size gate or its delivery history. The child decides what context escapes to the main agent. Context separation resembles a call frame with selected inputs and a returned result, but host-native delegation and window management remain outside RightMemory's enforcement. Source files stay tool-readable rather than becoming automatically followed references in a model window. See the contrasting [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval).

### 2. Main agent submits evidence, not final wording

While doing the user's work, the main agent selects evidence whose loss would impair future decisions, cause substantial rediscovery, or repeat a reusable failure. It writes a UTF-8 file outside the memory root and submits it with the root, session and stable request ID. The skill asks for circumstances, evidence and uncertainty, leaving stored wording and placement to Update. Routine progress is not a submission requirement, and Pursuit edits are explicitly separate. SRC-1: `skills/rightmemory-assistant/SKILL.md`.

The service hashes session/request identity into a candidate UID, persists submission identity, and passes evidence to the update store. Repeating identical identity/evidence returns duplicate state; reusing that identity for different evidence is rejected. A successful save is delivery to the queue, not delivery into canonical Memory. No routine human approval of Update's final wording is required by this protocol. SRC-1: `rightmemory/assistant.py`; [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant).

> if previous is not None and previous != identity:
>     raise ValueError("request_id already belongs to different update evidence")
> --- `rightmemory/assistant.py`

### 3. Main agent claims and delegates one ready batch

Batch-ready notices return through normal tool calls; a child must relay them rather than independently owning Update scheduling. The main agent calls `update begin`. Code first handles existing/terminal tasks, checks synchronization, then claims a Git-backed batch or reserves a local ready batch. A synchronization problem returns `sync_required` instead of starting Update. A fresh task binds task ID, batch ID, candidates, backend and expiry. Preparation returns the worktree/base commit, instructions file, candidates JSON and exact completion arguments. SRC-1: `rightmemory/assistant.py`.

The main agent delegates only `claimed: true` to one Update child. `claimed: false` denotes existing work, not permission to launch a duplicate. The user task can continue concurrently. Code preserves active task identity even after lease expiry unless explicit replacement is requested, subject to publication fencing; the skill directs status inspection when completion is uncertain. Host adherence to single-worker scheduling remains unobserved. SRC-1: `skills/rightmemory-assistant/SKILL.md`, `rightmemory/assistant.py`.

> # Lease expiry is not permission to abandon native edits.
> --- `rightmemory/assistant.py`

### 4. Update judges evidence; program checks admissibility

The child receives canonical role instructions and batch evidence against an isolated worktree, not authority to publish arbitrary active-root files. Update is asked to inspect both graph roots and relevant existing state, reconcile the batch by meaning rather than session labels, decide keep/merge/skip/edit, then consult `corrections.md` as a late feedback check. It may reject all candidate content. Pursuit is read-only. The prescribed terminal report names changed modules/items, skipped candidates and unresolved ambiguity. SRC-1: `rightmemory/prompts/update.md`; [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update).

> - Form a tentative keep, merge, skip, and edit judgment first.
> - Then read root `corrections.md` when present and use relevant RightMemory Edit Feedback as a late check on the tentative edit.
> --- `rightmemory/prompts/update.md`

These are semantic instructions, not an independent factual answer oracle. The child validates and commits allowed changes, or makes no commit if state is unchanged. Completion verifies task/worktree identity, clean committed state and source-commit ancestry, imports commits through the isolated supervisor, validates the graph even for no-change work, and retains batch evidence. Runtime-established path/intermediate-commit and publication checks apply at admission; they do not establish semantic truth or an OS sandbox around host tools. SRC-1: `rightmemory/assistant_write.py`; [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant), [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update).

### 5. Receipt, rejection and recovery

For local batches, the writer publishes through its supervisor. Git-backed prepared work instead goes through the queue coordinator's finalization and external completion. The service then acknowledges the batch, persists a receipt including landed commit, changed paths, output and sync status, clears the active pointer, and attempts cleanup. Cleanup failure can become a warning rather than falsely turning successful publication into failure. This inspected handoff establishes the receipt boundary, not a full audit of remote transport or observed synchronization. SRC-1: `rightmemory/assistant.py`; [RT-CLM-native-publication](runtime.md#rt-clm-native-publication).

A concrete rejection path is a changed semantic base: import compares current semantic state with the task's base and rejects stale edits before accepting their commits. If rejection occurs before preparation completes, completion resets captured source/output metadata so edits can be corrected in the same native worktree. SRC-1: `rightmemory/assistant_write.py`.

> if changed:
>     raise AssistantStaleVersionError("memory changed since assistant task began: " + ", ".join(changed))
> --- `rightmemory/assistant_write.py`

> # Rejected edits may be corrected in the same native worktree.
> --- `rightmemory/assistant_write.py`

Interruption or failed publication requires status inspection and retrying completion with the same task/worktree; prepared work retries publication without repeating semantic judgment. Explicit `begin --retry` abandons/replaces stale work for the batch and fences old edits. It is not the response to an uncertain completion receipt. Synchronization repair is a separate delegated recovery branch: a child relays the notice, the main agent dispatches one newly claimed repair, and prepared repair work resumes completion. The skill distinguishes local repair from remote push and says failed push does not undo local repair. Those repair instructions are doctrine/design here, not a traced successful repair or universal rollback guarantee. SRC-1: `skills/rightmemory-assistant/SKILL.md`, `rightmemory/assistant.py`.

The workflow's terminal memory result is the program receipt, not the child's summary or prepared candidate. Later native retrieval can consume active files, but neither downstream use nor improved coding decisions follows from publication. The enclosing user's task has its own host-owned delivery; RightMemory's receipt does not certify its completion. See [RT-BAP-host-context](runtime.md#rt-bap-host-context).

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

#### On [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant)

Workflow-specific handoffs: main agent → Retrieve child carries need/root/session/preparation command; Retrieve child → main agent carries selected context and sources; service → main agent carries batch/task identity, claim state, worktree and instruction/evidence paths; main agent → Update child carries the newly claimed task; Update child → service carries committed work and completion request; service → caller carries the publication receipt. Scheduling ownership remains with the main agent, while publication ownership remains with the program. An existing task is not a fresh delegation authorization. Status and same-task completion retries distinguish uncertain delivery from deliberate replacement; the workflow account supplies the inspected implementation and skill evidence without declaring a second identity for this route.
