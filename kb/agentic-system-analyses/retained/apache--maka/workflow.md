---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Apache Maka workflow account: a Host-backed request delegates bounded child work, retrieves its result and optionally publishes a terminal worktree patch."
run-id: AAS-2026-10-15-maka-4a8b73e41579-01
reviewed-boundary: "1751c399239b0f6b717e98e2a5e2b875c3dd11ce"
---

# Apache Maka workflow report

## Workflow account

### Selection and evidence boundary

This account selects the foreground request → bounded child task → child result → foreground answer workflow. It exposes the consequential separation between model-selected delegation, Host admission, independent child execution and delivery to the caller. The optional worktree result branch also distinguishes publishing proposed changes from applying or verifying them. This is one implemented workflow family, not a claim that every request delegates or that a supplied run completed it.

The [boundary](boundary.md) supplies SRC-1 and the frozen revision. The CLI and model/tool baseline comes from [RT-RTE-cli-turn](runtime.md#rt-rte-cli-turn), [RT-RTE-tool-settlement](runtime.md#rt-rte-tool-settlement) and [RT-RTE-child-graph](runtime.md#rt-rte-child-graph). Added SRC-1 implementation inspection covers `packages/runtime/src/subagent-tools.ts` (spawn validation, result projection and selection guidance), `packages/runtime/src/session-manager.ts` (foreground child creation/start, result retrieval and patch finalization), and `packages/runtime-host/src/server/execution-artifacts.ts` (patch publication). Searches located Host wiring in `packages/runtime-host/src/server/execution-composition.ts`. Storage worktree allocation/capture locations were searched but not traced; this account does not certify their Git or containment behavior. No target execution, model call, test or experiment was performed. Source wiring does not establish successful task execution, recovery or semantic correctness.

### 1. Admit the user's request and let the foreground model select work

A user submits task text and a target through the CLI. The Host-backed driver prepares the prompt and requires a Run identity, then observes a Turn rather than owning execution locally. Resume and stop address Host state. These entry and terminal-delivery mechanisms are established by [RT-RTE-cli-turn](runtime.md#rt-rte-cli-turn), SRC-1 `packages/cli/src/runtime-host-run-command.ts`.

Within the admitted turn, the model proposes text or tool calls; code resolves the active tool map and settles calls through the durable tool boundary. The next model request is reconstructed from durable events, not merely the returned JavaScript object. Thus a child result must cross the same settlement/continuation path as other tool results. See [RT-RTE-tool-settlement](runtime.md#rt-rte-tool-settlement), SRC-1 `packages/runtime/src/ai-sdk-turn.ts` and `packages/runtime/src/tool-runtime.ts`.

Delegation is a model decision under guidance, not a fixed decomposition algorithm. The shipped selection tool directs the foreground model to use available catalog choices and an explicit task:

> List a compact page of subagents to select. Copy an available choice's spawn_args into agent_spawn and add task. presets use subagent_id; legacy_profiles use profile, including when presets is empty. agent_id is for Graph only. Use view=catalog only to diagnose unavailable routes. Child execution history is intentionally excluded; use refs returned by agent_spawn or asynchronous graph work with agent_output.
> --- `packages/runtime/src/subagent-tools.ts`

The spawn implementation validates profile/preset selection, supported write-back mode and required isolation. Its child task is a nonempty bounded string. It passes the resolved profile, optional preset/executor and `input.task` to the spawn capability. Invalid selection can be rejected by code; availability does not force the model to delegate. This is open task work, not an experiment curriculum or a reference-answer comparison.

### 2. Supply a separate child with explicit task, authority and lineage

The Host's SessionManager requires durable stores, reads the parent Session/Run/boundary and execution policy, and checks that the parent Run is active. It resolves tools from the definition, or uses an empty local tool list for an executor-backed child. It provisions the workspace and creates durable child metadata containing parent/tool-call lineage, definition version, system prompt, tool names, request fingerprint and initial Turn/Run identities. These are implementation checks, not model promises. SRC-1 `packages/runtime/src/session-manager.ts`; the existing referent is [RT-RTE-child-graph](runtime.md#rt-rte-child-graph).

The child's working context is not the parent transcript. The runtime baseline retains the composer's explicit warning that local Memory and personalization do not implicitly transfer; the parent must put necessary background in the task. This limits both accidental context growth and what the child can infer. Model, prompt and tool choice are distinct controls: the task is interpreted natural language, while tool-name ceilings and durable execution identities are symbolic dispatch inputs. No claim that the child understands all supplied background follows from delivery.

SessionManager starts the linked child with required durability and the task as its input text. Progress is accumulated and can be forwarded to the parent observer, but observer failure is isolated from the child outcome:

> // A presentation observer must not change the child run outcome.
> --- `packages/runtime/src/session-manager.ts`

### 3. Verify admission and result structure, not task truth

There are several rejection gates, but no inspected mandatory independent task-quality verifier. Spawn argument/profile checks reject unsupported contracts. The manager rejects inactive parent Runs, cancellation and missing durable identity. After execution, it reads invocation facts and constructs the child return with status, summary, artifact IDs, timing, event count and optional failure class. The tool's `projectSubagentToolResult` decodes that return through `decodeCanonicalToolResultContent`, rejecting invalid structure. SRC-1 `packages/runtime/src/subagent-tools.ts` and `packages/runtime/src/session-manager.ts`.

These checks establish the shape and execution lineage of a result. They do not decide whether a code change fixes the user's problem or whether a research answer is true. The foreground model can inspect the returned material and choose further tools, but this path does not enforce tests, an external critic or a reference-answer oracle before its final answer. A completed child status is not such an oracle. Child effects remain governed by the selected tools/backend; external-executor guarantees cannot be inferred from local-tool settlement, as [RT-RTE-executor-plugin](runtime.md#rt-rte-executor-plugin) explains.

### 4. Return selected output, with optional patch publication

Foreground spawn awaits linked execution and returns a projected result rather than copying the full child transcript. Later `agent_output` reads can retrieve bounded committed-result or event views using explicit locators. SRC-1 `packages/runtime/src/session-manager.ts` applies event/byte budgets, reports truncation, and separates `view=result` from event collections. The parent can request more evidence, but no automatic complete-transcript handoff is established. This is context isolation with selected results crossing back, not a disposable stack frame: the child and its durable identities remain separately addressable. The existing result/read referent remains [RT-RTE-child-graph](runtime.md#rt-rte-child-graph).

For a configured worktree child, terminal execution can also owe a patch artifact. [WF-RTE-patch-publication](#wf-rte-patch-publication) establishes that narrower branch. Finalization requires a terminal latest inline invocation and a quiescent workspace, captures a patch, and publishes `workspace.patch` with source `subagent_writeback`. An existing such artifact suppresses repeated publication. Publication does not merge the patch into the parent workspace, nor does the inspected method validate its semantic quality. Parent-side application/review is not traced here; delivery of artifact IDs must not be described as accepted integration.

Once the foreground model continues from the settled result, it can produce the terminal answer observed by the CLI. The Host's classified Turn outcome and answer/events make this delivered to the client in the inspected route. Delivery is not independently verified fulfillment of the user's task. This final boundary is [RT-RTE-cli-turn](runtime.md#rt-rte-cli-turn), not patch publication alone.

### 5. Reject cancellation races and recover durable partial progress

SessionManager checks cancellation before creation and again before admitting the initial child run. It rereads the latest parent invocation after looking for an existing spawn, closing the durable-metadata/no-initial-run seam. Its intended handling of the earlier creation race is explicit:

> // Close the create/start race: if the parent settled (or cancellation
> // arrived) while metadata was being written, retain an inspectable aborted
> // child but do not admit new foreground work.
> --- `packages/runtime/src/session-manager.ts`

The implementation can mark the created child aborted and throw, leaving inspectable state rather than pretending successful work. During child execution, abort requests stop of the linked root and the manager waits for that stop. Spawn failures are reported as bounded progress errors and rethrown by the tool. The caller can then choose a different action; automatic successful retry is not guaranteed. SRC-1 `packages/runtime/src/session-manager.ts` and `packages/runtime/src/subagent-tools.ts`.

A previously created spawn is resolved through its durable child identity rather than blindly creating another. For the separate patch seam, `recoverChildWorkspacePatches` reruns finalization, and result listing can attempt missing terminal patch publication. Nonterminal work, live resources, retirement or mismatched publication can reject that handoff. These are recovery responsibilities of runtime/Host code; no observed crash trace establishes their success under real failures.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-patch-publication
Label: Terminal child patch publication

Part of: [RT-RTE-child-graph](runtime.md#rt-rte-child-graph)

This is the worktree-artifact handoff within the supplied child route, not a second declaration of child spawning. Endpoints are terminal child workspace → SessionManager finalizer → Host artifact publisher → returned artifact references. Owner: SessionManager decides eligibility and requests capture; the injected worktree executor captures bytes; Host artifact services publish them. SRC-1 implementation: `packages/runtime/src/session-manager.ts` and `packages/runtime-host/src/server/execution-artifacts.ts`.

> await this.deps.assertChildWorkspaceQuiescent!(sessionId);
> await this.ensureChildWorkspace(header);
> const patch = await this.deps.worktreeChildExecutor!.capturePatch(binding);
> --- `packages/runtime/src/session-manager.ts`

> name: 'workspace.patch',
> kind: 'diff',
> content: patch,
> mimeType: 'text/x-diff; charset=utf-8',
> source: 'subagent_writeback',
> summary: `Workspace changes relative to ${binding.baseCommit}.`,
> --- `packages/runtime-host/src/server/execution-artifacts.ts`

The child proposes changes by modifying its workspace. Code admits the publication, not a human approving each patch. Guidance shaping the actual edits is the child task/definition; their concrete contents vary and are not supplied by an observed run. The persisted result is an artifact with Session/Turn identity, not an adopted parent-workspace change. This is open delegated work; no expected-answer oracle or semantic improvement test is used by these finalization methods. Terminal/quiescence checks can veto capture. Recovery retries finalization; rollback of already performed child effects is not established.

- Immediate return: A published artifact record, then artifact IDs in the child spawn result; publication mismatch or retired Session can throw.
- Later read-back: Child output/artifact listing can return the retained artifact and can attempt missing terminal publication; exact physical artifact-store layout and full download path are uninspected.
- Delegated visibility: Parent receives artifact references and selected child output; the publication method does not copy the full child context or apply the patch to the parent.
- Selection predicate: Configured patch write-back services, bound child workspace, latest inline invocation with a terminal event, no existing subagent_writeback artifact, and successful quiescence/workspace checks.
- Invalidation or expiry: A nonterminal latest Run rejects finalization; existing publication short-circuits it; retirement can reject publication. Artifact retention/expiry policy is uninspected.
- Activation or effect: Publishes proposed file changes as an artifact; subsequent parent application, task correctness and changed behavior are unobserved.
- Evidence limits: Capture backend internals, physical persistence guarantees and parent integration were not traced. Publication and terminal status are not test success or semantic approval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-child-graph](runtime.md#rt-rte-child-graph)

Workflow role: the foreground spawn branch supplies an explicit bounded task to an independently identified child, waits for linked execution and returns a structured status/summary/artifact handoff. Explicit bounded output reads are a follow-up option. Host admission and structural result checks are not task-quality acceptance. The optional patch-publication part is established separately above. Asynchronous Graph supervisor scheduling is not needed for this selected foreground workflow and is not inferred from it.

#### On [RT-RTE-cli-turn](runtime.md#rt-rte-cli-turn)

Workflow delivery criterion: the foreground Turn's terminal answer and classified outcome reach the observing CLI after continuation from settled results. Neither child completion nor artifact publication alone satisfies that client-delivery criterion; client delivery itself does not prove fulfillment.
