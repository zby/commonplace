---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Swamp runtime baseline: external-agent launch, typed behavior and workflow execution, approval, extension admission and repository review at the frozen commit."
run-id: AAS-2026-10-15-swamp-440d19cc0bcc-01
reviewed-boundary: "380e3c307164501c7d705f7707a864f4612b2785"
---

# Swamp runtime report

## Runtime account

### Work and evidence boundary

Swamp launches external agents and supplies instructions for creating and operating typed automation. Its behavior methods and workflow scheduler are executable machinery, not an enclosing inference loop. In Swamp terminology a behavior's implementation still uses `ModelDefinition`, `modelName` and model repositories; these are not necessarily language models. The distributed-parametric components are the external agents' inference models, separately recorded below. The claimed work is in [RT-CLM-agent-workflows](#rt-clm-agent-workflows).

The evidence is SRC-1 at the revision in [boundary](boundary.md#boundary-and-evidence). Everything traced below is inspected implementation or explicitly labelled doctrine/design. No target executable, test, provider or evaluator was run. No supplied trace establishes activation, operational success, compliance, reliability, performance or benefit. Added inspection within SRC-1 covers `src/domain/models/method_execution_service.ts`, `src/domain/models/in_process_executor.ts`, `src/domain/models/command/shell/shell_model.ts`, `src/domain/extensions/local_model_refresh.ts`, `src/domain/extensions/extension_loader.ts`, `src/domain/extensions/extension_auto_resolver.ts`, `src/libswamp/workflows/approve.ts`, `scripts/compile.ts`, `scripts/check_review_verdict.ts`, and the additional ranges of launch, workflow, review and issue-lifecycle files cited below. No source identity or scope is added.

### Ordinary invocation: goal to retained automation result

1. A user supplies a task and selects an installed harness. `startLaunch` loads the task session, checks launchability and the brief's ownership, enrolls the selected tools, writes a task brief and opens a terminal with a harness launch specification. The session records the launch outcome. The launch prompt names one task brief, rather than embedding arbitrary task text in a command line. [RT-RTE-agent-launch](#rt-rte-agent-launch) separates this checked handoff from the external agent's uninspected inference and permissions.
2. The getting-started skill tells that agent to read only the named brief, confirm its goal, find an installed or registry behavior type, create a behavior and edit its YAML. It asks for validation, confirmation of a real-system target, a read-oriented first method, and output inspection. This is natural-language policy, not a code-level state machine constraining the agent. The behavioral-authority channel is [RT-BAP-agent-instructions](#rt-bap-agent-instructions).
3. On a behavior-run command, libswamp resolves and evaluates the definition, constructs the method context and calls the method execution service. The context carries definition identity, data repositories, vault services, runtime tags, signal and event callbacks. The service merges global/per-method arguments and validates them with the method schema before calling its body. Writers persist typed data handles; output records and method events reach CLI consumers. [RT-RTE-behavior-run](#rt-rte-behavior-run) describes this returning deterministic computation. The external agent, not Swamp, decides what to do with the result next.
4. A workflow replaces conversational next-step selection with symbolic YAML jobs, dependencies, conditions, expressions and tasks. The run generator validates inputs, constructs an execution service and maps its events. The domain service evaluates a plan, records run identity and provenance, saves before yielding `started`, and schedules dependency levels with bounded concurrency. Method tasks reach the same execution machinery. Step outcomes and handles populate downstream expression context and run history. The terminal stream distinguishes completion, cancellation, suspension and errors. [RT-RTE-workflow-run](#rt-rte-workflow-run) covers this route and its recovery boundary.

The procedure offers reviewability through authored definitions, evaluated plans, fingerprints, output provenance and persisted run transitions. It does not turn schema validation into semantic correctness of a cloud or shell action. Nor does a completed event prove that the external agent followed the onboarding gates. SRC-1: `.claude/skills/swamp-getting-started/SKILL.md`, `src/libswamp/models/run.ts`, `src/domain/models/method_execution_service.ts`, `src/domain/workflows/execution_service.ts`.

### Four forcing cases and guarantee boundaries

**1. A typed step can run arbitrary host code.** The default executor runs methods in the host Deno process, while `command/shell` launches a shell with a chosen command, directory and environment. Extension import and method execution are materially different control points: loading validates export shape, and executing validates arguments, but neither is an isolation boundary. The compiled executable requests broad read/write/environment/process/network/system/FFI permissions. That is a capability surface, not evidence of a particular user's current credentials, external OS confinement or deployed grants. A local extension or shell subprocess is therefore a counterexample to treating workflow-vault restrictions, missing approval callbacks, or typed schemas as a universal sandbox. [RT-RTE-behavior-run](#rt-rte-behavior-run), [RT-RTE-extension-load](#rt-rte-extension-load).

**2. Manual approval gates only the configured continuation.** A manual-approval task suspends its run, but the scheduler drains parallel siblings rather than undoing them. Approval stores a decision under a run claim; resumption refuses a still-waiting gate. The server handler authorizes an `approve` action on the resolved workflow and uses the authenticated principal when present. The local libswamp operation instead accepts a caller-supplied decision identity or falls back to environment identity. Consequently “manual” does not establish per-content human authorization on every path. The onboarding target-confirmation request and issue-lifecycle “never auto-approve” rule are separate natural-language policies. [RT-RTE-gate-resume](#rt-rte-gate-resume), [RT-RTE-issue-admission](#rt-rte-issue-admission).

**3. Remote placement changes executor and checks.** Remote methods execute in a worker child runner loaded by bundle fingerprint; the orchestrator retains the surrounding output pipeline. The remote branch skips checks requiring worker-local state and explicitly rejects `rollbackOnFailure`. The runner reconstructs a definition, builds a remote context, validates arguments and calls the method. Remote cancellation crosses an RPC channel. Conversely remote-only mode rejects non-internal methods without placement. These are materially distinct routes, not evidence that host-local guarantees automatically transfer to a worker deployment. [RT-RTE-worker-dispatch](#rt-rte-worker-dispatch).

**4. Agent review is a verdict protocol, not an answer oracle.** The shipped review workflow creates a fresh worktree, computes a merge-base diff, invokes Claude with selected read tools and parses the review output. Provider-error patterns take precedence; otherwise the first line-initial matching pass/fail marker determines the result. A missing marker fails. This narrows the comment's intended “begin your response” instruction: the regex does not require the marker to be on the first response line. It checks an output convention, not whether the review found the right defects. The model alias and external harness remain outside frozen implementation evidence. [RT-RTE-review-verdict](#rt-rte-review-verdict).

### Load-bearing guarantees

| Guarantee and owner | Enforcement and strength | Covered paths and material limits | Conclusion statuses |
| --- | --- | --- | --- |
| Argument shape, method execution service | `safeParse` precedes `method.execute`; invariant within that entry | Default local executor and inspected worker runner call this service. Direct extension import has earlier top-level effects; semantic action safety and arbitrary host code are not covered. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Run exists when `started` is delivered, workflow execution service | Awaited repository save before event; protocol | Inspected workflow-service fresh-run path. Requires successful repository/file/datastore contract; does not imply remote replication or exactly-once external effects. | implementation conclusion status: wired; operation conclusion status: uninspected |
| A waiting approval gate blocks ordinary resumption, workflow execution service | Resume checks stored gate before mutation; protocol | Inspected resume path, claim/repository state and configured collaborators. Siblings may already act; a caller able to approve is not necessarily a human. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Review must produce a usable pass marker, verdict script | Provider-error test then marker parse; protocol | Shipped workflow invokes this script and propagates its exit. Does not cover arbitrary manual review, semantic correctness, or repository merge/release authorization. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Human plan approval, issue-lifecycle skill | Instruction to stop and ask; policy | External agent reading that skill. Extension method itself takes empty approval arguments and cannot establish the conversation contained consent. | instruction conclusion status: claimed; operation conclusion status: uninspected |

Evidence for each guarantee and its disconfirming alternate is retained in the corresponding route, not inferred from this table. Recovery is selective: failed workflow steps and dependents may be reset, suspended work is continued after decisions, and unknown outcomes need recovery handling. Nothing inspected establishes a transaction over all external side effects. Cancellation and local data rollback cannot undo an arbitrary shell command or remote API effect. SRC-1: `src/domain/workflows/execution_service.ts`, `src/domain/models/method_execution_service.ts`, `src/domain/models/command/shell/shell_model.ts`.

## Shared records

### Components

#### RT-CMP-agent-models
Label: External agent inference models

Distributed-parametric components reached through external harness executables. Parameters and provider storage are outside SRC-1. Launch adapters select harness binaries, not exact model weights; the review workflow requests the symbolic alias `claude-opus-5-5`. Exact model version is not pinned by an immutable provider revision in the inspected source. Whether parameters change during operation is uninspected; no weight-update mechanism is established here. Whether an alias or mutable provider endpoint can resolve to different weights is also uninspected, so the alias does not establish fixity. Context assembly, host compaction and provider-native tools belong to those external runtimes and cannot be attributed to Swamp.

SRC-1 implementation: `src/domain/start/harness.ts`, `verification/workflow-verify-reviews.yaml`.

> args: (_ws, _os, prompt) => [prompt],
> --- `src/domain/start/harness.ts:106-127`

> --model claude-opus-5-5 \
> --- `verification/workflow-verify-reviews.yaml:135-135`

#### RT-CMP-in-process-executor
Label: In-process method executor

Symbolic TypeScript code, shipped in source/compiled runtime storage. Injects resource/file writers and context services before delegating validation and execution. Its source-native “model” methods can be shell actions, extension code or remote-service adapters, not just inference. SRC-1 implementation: `src/domain/models/in_process_executor.ts`.

> In-process executor — runs model methods directly in the host Deno process.
> --- `src/domain/models/in_process_executor.ts`

### Operative objects

#### RT-OBJ-task-brief
Label: Task brief

Natural-language goal and agent-facing framing in a workspace-relative Markdown file under `tasks/`; task session identity separately selects it. The launch prompt points to this file. The getting-started skill uses its marker and `# Task` section; it requests exclusion of other tasks, not enforced model-context isolation. SRC-1 implementation/design: `src/libswamp/start/start.ts`, `src/domain/start/harness.ts`, `.claude/skills/swamp-getting-started/SKILL.md`.

> return `Read ${briefFile} and use the swamp-getting-started skill.`;
> --- `src/domain/start/harness.ts`

#### RT-OBJ-workflow-run
Label: WorkflowRun and evaluated run plan

Symbolic run state: workflow/run identifiers, jobs, steps, inputs/provenance, tags, status, timing and captured plan fingerprints. The scheduler uses it for execution and continuation. Evaluated plan snapshots and run records have distinct repositories; local run records are serialized YAML with a relative log path and atomically written, then staged as typed datastore changes. Logs are another output, not proof of changed future policy. This object is declared for execution/recovery; memory selection and revision findings remain for the memory analyst. SRC-1 implementation: `src/domain/workflows/execution_service.ts`, `src/infrastructure/persistence/yaml_workflow_run_repository.ts`.

> const content = stringifyYaml(cleanData as Record<string, unknown>);
> await atomicWriteTextFile(path, content);
> --- `src/infrastructure/persistence/yaml_workflow_run_repository.ts`

### Routes

#### RT-RTE-agent-launch
Label: Task launch and harness continuation

User/task selection → stored task session → enrolled harness and brief → terminal launch → recorded outcome. `startLaunch` owns setup; the external harness takes next-step ownership after launch. The task ID and brief path are distinct from an external conversation identity. `startResume` selects the most recent conversation in the workspace for supporting harnesses; other harnesses open fresh. Resume fallback opens a fresh session if continuation fails immediately. SRC-1 implementation: `src/libswamp/start/start.ts`, `src/domain/start/harness.ts`.

- Immediate return: Launch-progress events and completed task status, including whether a window opened; not the automation's answer.
- Later read-back: Stored task session is loaded on resume; the brief remains unchanged. Conversation read-back is delegated to the harness, not implemented by Swamp.
- Delegated visibility: Initial agent gets a prompt naming one brief and one onboarding skill. Resume does not resend the task; resulting conversation visibility depends on the external harness.
- Selection predicate: Explicit workspace/task and chosen supported harness; continuation uses harness-specific most-recent-in-folder arguments, not a task-to-conversation binding proven by Swamp.
- Invalidation or expiry: Launch checks brief ownership and task launchability; resume requires a launched task and folder trust. No task/conversation expiry established in inspected ranges.
- Activation or effect: Writes brief, enrolls tools, asks terminal launcher to open agent and saves launch outcome. Agent compliance and downstream task completion are unobserved.
- Evidence limits: External inference, actual installed skills, credentials, terminal behavior and conversation restoration were not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision policy is symbolic launch planning; the brief and skill are natural-language guidance. Trust mode varies by harness/platform: Claude has its dialog; non-Windows Codex receives a per-folder trust override; Cursor gets `--trust`; several harnesses have unknown trust mode. These are launch settings, not a single common tool-permission envelope. SRC-1: `src/domain/start/harness.ts`.

> resumeArgs: () => ["--continue"],
> --- `src/domain/start/harness.ts:106-127`

> * the folder do so, the rest open a fresh session there. The brief is left
> * as it is.
> --- `src/libswamp/start/start.ts:1578-1589`

#### RT-RTE-behavior-run
Label: Behavior method execution and shell effects

CLI/libswamp behavior run → evaluated definition and method context → method execution service → local in-process method → typed handles/output and events. The caller chooses method and inputs; code owns argument coercion, schema validation and execution progression. No answer oracle: validation checks declared shape, not the desired real-world outcome. Operating mode is open user automation, with optional checks/report filters rather than a training curriculum. SRC-1 implementation: `src/libswamp/models/run.ts`, `src/domain/models/method_execution_service.ts`, `src/domain/models/in_process_executor.ts`.

- Immediate return: Method result/data handles, progress/output events, and a completed view or error; libswamp exposes output/report information to consumers.
- Later read-back: Output provenance and persisted resource/file data can be consumed by later behavior/workflow/data queries; detailed retention revisions are not assessed here.
- Delegated visibility: Method receives evaluated arguments, definition identity and injected data/vault/context services. Nested `runModel` service can invoke other behavior methods; it is not itself an LLM delegation primitive.
- Selection predicate: Resolved behavior identity, registered type, named method, merged global/per-method arguments; per-method keys take precedence.
- Invalidation or expiry: Unresolved Swamp expressions in accessed global arguments fail; schema mismatch rejects invocation. Output retention depends on declared data policy, not fully audited here.
- Activation or effect: Calls method body after validation; writers persist handles. `command/shell` executes the authored command in the requested directory with environment, timeout and abort signal.
- Evidence limits: No execution traces. Method schemas do not constrain arbitrary extension side effects or prove semantic correctness. Current grants and OS isolation are unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const argsResult = method.arguments.safeParse(methodArgs);
> --- `src/domain/models/method_execution_service.ts`

> const result = await method.execute(argsResult.data, enrichedContext);
> --- `src/domain/models/method_execution_service.ts`

Shell environment construction filters inherited variables, includes lock/trace metadata and explicit user environment, and sets `clearEnv: true`. Vault sentinel handling tries to keep secret contents out of command syntax, but the authored command itself remains executable shell text. Timeout and process-tree cancellation do not establish rollback. The shell persists captured output before judging a nonzero exit. SRC-1 implementation: `src/domain/models/command/shell/shell_model.ts`.

> command: invocation.command,
> args: invocation.args,
> cwd: args.workingDir,
> env: processEnv,
> clearEnv: true,
> timeoutMs: args.timeout,
> signal: context.signal,
> --- `src/domain/models/command/shell/shell_model.ts`

The packaged permission surface includes unrestricted category flags, not per-extension grants. SRC-1 implementation: `scripts/compile.ts`.

> "--allow-read",
> "--allow-write",
> "--allow-env",
> "--allow-run",
> "--allow-sys",
> "--allow-net",
> --- `scripts/compile.ts`

#### RT-RTE-workflow-run
Label: Workflow scheduling and durable continuation

CLI/libswamp workflow-run input → resolved workflow → input/default validation and evaluation → saved run → topological concurrent jobs/steps → persisted outcomes and terminal events. Code and the authored symbolic workflow own next-step selection. CEL assertions can call behavior methods, so expression evaluation is not necessarily effect-free. Reports/check filters are caller controls; an authored assertion is not an independent truth oracle. SRC-1 implementation: `src/libswamp/workflows/run.ts`, `src/domain/workflows/execution_service.ts`.

- Immediate return: Event stream with run identity, job/step progress, method events, reports and completed/cancelled/suspended/error outcomes.
- Later read-back: Run record and captured plan support history, resume and recovery; this is execution continuation, not evidence of policy learning.
- Delegated visibility: Step executor gets expression context, workflow/run identity, inputs, signals and output handles; nested workflows receive parent links and selected inputs. External agents see only what their command/client returns.
- Selection predicate: Workflow identity/name, dependency levels, conditions/guards, step inputs and configured concurrency. `byId` plus expected name supports callers authorizing a resolved target.
- Invalidation or expiry: Failed runs can reset failed steps and dependents; suspended runs require settled waits; resume validates override inputs and stored state. Captured plan fingerprints support recovery, not external exactly-once effects.
- Activation or effect: Scheduler invokes selected methods and persists transitions. It saves before exposing `started`, on material step outcomes and after each job level.
- Evidence limits: Datastore durability, replica convergence, client disconnection semantics and arbitrary external side-effect idempotence are not established by source wiring.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await this.saveRun(workflow.id, run);
>
> yield {
>   kind: "started",
> --- `src/domain/workflows/execution_service.ts:3905-3929`

> // Sort jobs topologically
> const jobNodes: GraphNode[] = workflow.jobs.map((job) => ({
> --- `src/domain/workflows/execution_service.ts`

The outer generator creates an ephemeral scratch store after early input checks and disposes it on exit; this limits working data lifetime, not external-agent conversation context. `lastEvaluated` has a separate cache/replay route and skips the ordinary input-validation branch in this generator. No claim is made that every invocation freshly evaluates authored source. SRC-1: `src/libswamp/workflows/run.ts`.

> } else if (workflow.inputs) {
>   // lastEvaluated: still coerce types but skip validation
> --- `src/libswamp/workflows/run.ts`

#### RT-RTE-gate-resume
Label: Approval decision and resume

Configured manual-approval step → waiting step and suspended run → CLI or server approval/rejection → stored decision → explicit or server continuation. The workflow author places the gate. The caller supplies the decision; code checks run/step status, timeout and ownership claims. Server authorization and local caller authority are separate. SRC-1 implementation: `src/domain/workflows/execution_service.ts`, `src/libswamp/workflows/approve.ts`, `src/serve/handlers/workflow_handlers.ts`.

- Immediate return: Approval request/suspension prompt; decision command returns approved identity/reason and whether all gates are settled, or refusal.
- Later read-back: Saved gate decision and captured inputs are read during continuation; timeout and still-pending gates affect admissibility.
- Delegated visibility: Server uses authenticated principal when present; the approval prompt and stored run reach the deciding client. No demonstrated human attention or consent is available.
- Selection predicate: Resolved workflow, run and waiting non-nested step, under a claim; server additionally checks `approve` on the resolved workflow.
- Invalidation or expiry: Expired gates reject approval. Resume refuses waiting gates and live owners still draining siblings when configured liveness/tracker collaborators are available.
- Activation or effect: Records decision and succeeds approved step; continuation is a separate operation. Parallel sibling effects may complete before the suspension settles.
- Evidence limits: Local decision identity is not authenticated human consent; authorization logic outside inspected handler seams is not exhaustively audited. Claims require storage collaborators' contracts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: workflow author requests a pause. Decider/veto: caller can approve/reject within its path's authority; code rejects invalid/expired decisions. Answer oracle: inapplicable — approval is an authorization decision, not a known reference outcome. Operating mode: configured automation with an optional gate, not universally human-in-the-loop execution. Rollback/recovery: resumption/retry can proceed after an admissible decision; the gate does not rewind already executed siblings.

> // Return instead of throwing WorkflowSuspendedError so that merge()
> // continues draining parallel sibling generators to completion. The
> // post-level save in run()/resume() captures the consistent state.
> --- `src/domain/workflows/execution_service.ts`

> const decidedBy = input.decidedBy ?? Deno.env.get("USER") ??
>   Deno.env.get("USERNAME") ?? "unknown";
> --- `src/libswamp/workflows/approve.ts`

> principal,
> "approve",
> target,
> --- `src/serve/handlers/workflow_handlers.ts:1542-1544`

> // Gate service intentionally not wired here — approving/rejecting
> // workflow gates from model code bypasses authorization. Use the
> // CLI (swamp workflow approve/reject) or WebSocket API instead.
> --- `src/libswamp/workflows/run.ts`

That missing callback is a covered API restriction, not containment of host code: the shell route remains available. The same no-gate-service choice exists in behavior-run setup. SRC-1: `src/libswamp/models/run.ts`.

#### RT-RTE-worker-dispatch
Label: Remote behavior dispatch

Placement-selected orchestrator request → worker child dispatch runner → fingerprint-selected bundle/method → reconstructed definition and remote context → default method executor → output identities/logs to orchestrator. Symbolic RPC frames and code determine progression; worker code is not a delegated language-model reasoner merely because it executes a “model.” SRC-1 implementation: `src/domain/models/method_execution_service.ts`, `src/worker/exec_dispatch.ts`.

- Immediate return: Dispatch success/error, output identities and scrubbed logs; orchestrator reconstructs full handles from persisted data-plane metadata.
- Later read-back: Data-plane persisted outputs and orchestrator output records can be consumed later. Worker-provider durability is not independently established.
- Delegated visibility: Execution envelope, bundle fingerprint, method arguments and remote context cross to worker; runner gets a session credential and data-plane URL from bootstrap.
- Selection predicate: Remote placement and available worker matching; method selected from loaded bundle by execution method name. Full worker scheduling/authorization was not audited.
- Invalidation or expiry: Abort is forwarded through `runner.cancel` and stdin close aborts the runner's controller. Remote rollback-on-failure is rejected; local preflight checks cannot inspect worker-local state.
- Activation or effect: Worker calls method body through the default validator; data-plane writers and method code can produce remote effects.
- Evidence limits: No dispatch observed; worker OS isolation, current credentials, network enforcement and remote service internals remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Remote placement: the method body runs on a matching worker; the
> // surrounding pipeline (output records below)
> // stays at the orchestrator. Pre-flight checks are skipped (they
> // cannot access worker-local state). See design/enablers/remote-execution.md.
> --- `src/domain/models/method_execution_service.ts`

> const executor = new DefaultMethodExecutionService();
> const methodResult = await withConsoleGuard(
>   () => executor.execute(definition, method, remote.context),
> --- `src/worker/exec_dispatch.ts`

#### RT-RTE-extension-load
Label: Capability admission through extensions

Local source or trusted-collective auto-resolution → bundle/import → export and namespace validation → type registration/lazy resolution → later method execution. TypeScript behavior implementations are symbolic code; exported descriptions can separately instruct users/agents. Code files, bundle cache/catalog and registry hold distinct representations. SRC-1 implementation: `src/domain/extensions/extension_loader.ts`, `src/domain/extensions/local_model_refresh.ts`, `src/domain/extensions/extension_auto_resolver.ts`.

- Immediate return: Loaded/failed extension records and registered types, or an auto-resolution refusal/hint.
- Later read-back: Registry/catalog and cached bundles supply later type resolution; a local edit can replace a type used by the next resolve.
- Delegated visibility: Imported module and validated exports enter the host runtime. No separate model context is implied by extension loading.
- Selection predicate: Local source discovery or unresolved type's collective allowlist; export schema, namespace and duplicate-type checks determine registration in the inspected load branch.
- Invalidation or expiry: Local refresh invalidates affected non-built-in types and re-registers loadable catalog rows. Import/validation failure can leave a type unavailable; bundle failure can keep the previous bundle with a warning.
- Activation or effect: Import executes code before export validation; successful registration makes new methods available to later execution.
- Evidence limits: Registry trust is not proof that code is safe; dependency/push/pull review gates and all installation alternatives were not exhaustively audited. No local edit/load cycle was observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal: caller installs a capability or source author edits local extension code. Computational admission: bundling/import, export validation, namespace and registration rules; unknown-type auto-resolution additionally checks allowed collectives. Human approval: not established per-content by these code paths. Rejection ability: these checks can fail; built-ins are not replaced by local refresh. Rollback/recovery: fix source and reload; stale-bundle fallback differs from failed validation and is not universal rollback. Guidance shaping an authored extension is outside these inspected paths; source, bundle and catalog state persist. Operating mode: open capability addition, not a bounded learning experiment. Answer oracle: inapplicable — structural type admission has no expected task answer.

> const module = await this.importBundle(bundled.js, file, baseDir);
> --- `src/domain/extensions/extension_loader.ts:622-622`

> const parsed = this.adapter.validatePrimaryExport(exported);
> --- `src/domain/extensions/extension_loader.ts:652-652`

> if (!this.config.allowedCollectives.includes(collective)) {
> --- `src/domain/extensions/extension_auto_resolver.ts`

> // A local source never replaces a built-in of the same type.
> --- `src/domain/extensions/local_model_refresh.ts`

#### RT-RTE-review-verdict
Label: Repository code-review verdict gate

Commit/branch input → fresh Git worktree → merge-base diff and changed-file selection → parallel external-agent reviews → script verdict → workflow status/logs. Deterministic workflow and shell code own scheduling; an external model judges the proposed code. The request supplies review instructions and a diff-file pointer, with repository instructions/file reads available in the fresh worktree. SRC-1 implementation/design: `verification/workflow-verify-reviews.yaml`, `scripts/check_review_verdict.ts`.

- Immediate return: Reviewer prose streamed through shell output, parsed gate verdict and step exit result.
- Later read-back: Shell/run outputs retain the review account; immediate temporary prompt/diff/result files are removed. Later attestation consumers are outside this route's inspected detail.
- Delegated visibility: A new `claude -p` invocation receives a review prompt and diff path; selected tools are Read, Glob and Grep. Worktree separates review files from caller checkout, not an established security sandbox.
- Selection predicate: Code review runs; other review types have changed-path guards against the selected worktree diff. Workflow concurrency is four.
- Invalidation or expiry: Each workflow run builds a run-keyed fresh worktree. Missing markers and recognized provider errors fail instead of silently passing; semantic review error remains possible.
- Activation or effect: Verdict script exits nonzero on non-pass outcomes, failing the review step. No repository merge, release or actual code improvement is established.
- Evidence limits: No reviewer run or verdict artifact supplied. External tool enforcement, model fixity and review accuracy unobserved; parser checks marker syntax, not truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposed change: user-supplied commit to verify. Proposer: code author, not identified as human or model by the workflow. Decider: model emits a verdict; script decides the gate result. Veto: failed/missing/provider-error verdict blocks this step, not necessarily every route to a merge. Human admission authority beyond the workflow is uninspected. Guidance: review prompt file plus appended output-format request and repository material. Persistence: logs/results, not a model-weight update. Recovery: repair code/provider invocation and rerun; no automatic source rollback. Mode: open review of a proposed commit, not curriculum. Answer oracle: none established — reviewer judgment is not a reference answer.

> --allowedTools "Read,Glob,Grep" < "$PROMPT_FILE" | tee "$RESULT_FILE"
> --- `verification/workflow-verify-reviews.yaml:136-136`

> const VERDICT_MARKER_PATTERN = /^[ \t*]*VERDICT[ \t*]*:[ \t*]*(pass|fail)/im;
> --- `scripts/check_review_verdict.ts`

> if (PROVIDER_ERROR_PATTERN.test(withoutQuotedCode(output))) {
>   return { kind: "provider-error" };
> }
> --- `scripts/check_review_verdict.ts`

This route changes model-visible working context by launching a separate process with selected review inputs, rather than appending the full review conversation to the caller's context. The persisted shell output is the return channel. Internal context trimming, reasoning, provider state and reload are external and uninspected. It resembles a separate task frame with an output crossing back, but there is no inspectable Swamp-managed token window or liveness rule. The alias is described in [RT-CMP-agent-models](#rt-cmp-agent-models).

#### RT-RTE-issue-admission
Label: Issue plan approval to implementation

Repository-local issue skill → agent presents plan and requests feedback → caller invokes extension `approve` → local phase becomes approved and upstream lifecycle work is attempted. This is separate from workflow manual-approval tasks. Natural-language guidance asks for human consent; the extension consumes an empty argument object and records state. SRC-1 implementation/design: `.claude/skills/issue-lifecycle/SKILL.md`, `extensions/models/issue_lifecycle.ts`.

- Immediate return: Method handles/logs and approved lifecycle state, or error. Successful remote posting is not demonstrated here.
- Later read-back: `state-main` and `plan-main` are later-session lifecycle inputs; detailed plan/feedback revision belongs to the memory/epistemic analyses.
- Delegated visibility: External agent is told to show a plan to the human and wait. The approval method reads the retained plan and global issue identity, not the conversation proving consent.
- Selection predicate: Named issue behavior and current retained plan; issue-lifecycle skill routes by phase. The approve method itself has empty arguments.
- Invalidation or expiry: Method declares rollback-on-failure; general local execution supports deferred writes, whereas remote placement rejects that mode. Detailed upstream transaction/recovery behavior is not fully audited.
- Activation or effect: Writes `phase: approved`; the skill routes approved work toward implementation. Actual code change from a retained plan remains unobserved.
- Evidence limits: Policy cannot establish human consent or criticism quality; no lifecycle episode, source improvement or deployed change is demonstrated.
- implementation conclusion status: wired
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Trigger/proposal: issue planning requested by user, with agent-produced plan and feedback. Intended decider/veto: human according to skill; computational method does not validate that consent. Guidance: issue skill and routed repository conventions. Admission: explicit `approve` invocation records phase; rejection/iteration is an instructed conversational alternative. Rollback/recovery: declared local failure rollback and retry, with external posting limits left local to this route. Mode: interactive open issue work. Answer oracle: none established for plan quality. This record assesses admission, not whether plan content meets theory-builder conditions or constitutes learning/self-improvement.

> **Never auto-approve.** Always stop and show the plan to the human. Always ask
> for feedback. Only call `approve` when the human explicitly says to proceed.
> --- `.claude/skills/issue-lifecycle/SKILL.md`

> approve: {
>   rollbackOnFailure: true,
>   description: "Approve the current plan",
>   arguments: z.object({}),
> --- `extensions/models/issue_lifecycle.ts`

### Claims

#### RT-CLM-agent-workflows
Label: Agent-facing reviewable automation claim

Claimed operation: Swamp supplies agents with a CLI for creating operational workflows that are reviewable, shareable and accurate. Reviewability has inspected mechanisms; accuracy remains a product claim rather than an observed outcome. SRC-1 doctrine/design: `README.md`.

> Swamp is a CLI that supercharges AI agents to create operational workflows that
> are reviewable, shareable, and accurate.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-instructions
Label: Brief and installed skill authority

Consumer: external agent harness/model. Channel: launch prompt points to task Markdown and getting-started skill; repository-local issue skill separately routes issue work. Force: natural-language requests to interpret goals, choose types, validate, confirm targets and ask human approval. Horizon: launch invocation and later sessions that read installed instructions/brief/state; actual compliance is unobserved. Symbolic launch checking constrains the brief path, not obedience to brief contents. SRC-1: `src/domain/start/harness.ts`, `.claude/skills/swamp-getting-started/SKILL.md`, `.claude/skills/issue-lifecycle/SKILL.md`.

> **Action:** If the method touches a real system (a cloud account, cluster,
> project or repository), confirm the target with the user before running it —
> which account, cluster, project or repository.
> --- `.claude/skills/swamp-getting-started/SKILL.md`

#### RT-BAP-workflow-execution
Label: Authored workflow and registered method authority

Consumer: workflow scheduler/expression evaluator and method executor. Channel: symbolic workflow definition/evaluated run plan plus registered TypeScript method. Force: code selects ready work and calls methods, which can affect host or remote systems; declarations/validation constrain shape and selected APIs, not all host effects. Horizon: current execution and later continuation; extension reload can change the next type resolution. SRC-1: `src/domain/workflows/execution_service.ts`, `src/domain/models/method_execution_service.ts`, `src/domain/extensions/local_model_refresh.ts`. Supporting execution passage is retained in [RT-RTE-behavior-run](#rt-rte-behavior-run), and code-reload evidence in [RT-RTE-extension-load](#rt-rte-extension-load).

## Annotations

none
