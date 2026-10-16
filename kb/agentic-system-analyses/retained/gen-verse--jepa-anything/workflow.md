---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "JEPA-Anything workflow: host-led rollout-task conversion, deterministic design rejection, scaffold generation and inspectable delivery."
run-id: AAS-2026-10-15-jepa-anything-434b01ab7774-01
reviewed-boundary: c6e6c88f3ef75a4ce7acd660d6fa5779d995512c
---

# JEPA-Anything workflow report

## Workflow account

### Selected path and evidence boundary

This account selects conversion of a user's multi-step rollout task into a validated design and code skeleton. Rollout is an explicitly supported task, and selecting it connects the original consumer intent to a generated interface that contract tests exercise. This is one branch of the shipped conversion workflow, not a reconstructed host execution. No concrete user request, generated package from a host run, test result or trained model is supplied. The evidence establishes instructions and deterministic implementation at the [boundary](boundary.md), not successful delivery in practice. SRC-1: `jepa-anything-skill/SKILL.md`, `jepa-anything-skill/references/world-model-conversion.md`, `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`.

The main sequence is already identified by [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation) and [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission). This member adds workflow-specific handoff and completion details through annotations rather than duplicating their records.

### 1. User task to host proposal

The user authorizes creating or adapting a world-model task. The enclosing host agent receives the request and any supplied project. The Skill asks that agent to inspect available task facts, read the conversion/design/configuration references, and establish system-instance identity, prediction-time information, target/horizon and intended consumer. The host interprets these facts; the repository does not implement a separate planner or worker scheduler. Tool execution and model inference remain host responsibilities. SRC-1: `jepa-anything-skill/SKILL.md`; [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).

Missing causal facts create a user-question branch, not an invitation to invent the task. Missing architectural choices instead remain the host's proposal responsibility:

> Ask a short question only when one of these cannot be recovered and a guess could create target leakage or change the task. Do not ask the user to choose OPF, losses, baseline structure, canonical coordinate IDs, or JEPA-specific schema fields.
> --- `jepa-anything-skill/references/world-model-conversion.md`

For rollout, the conversion reference maps rollout/model-predictive control to `repeated_transition`. The host must distinguish historical actions from future inputs actually known at the relevant step. It records proposed choices and a source-task summary under `task.metadata.compiler_assumptions`; these are part of the deliverable, not measured findings. SRC-1: `jepa-anything-skill/references/world-model-conversion.md`.

### 2. Proposal to deterministic criticism and repair

The next handoff is a configuration file, not a delegated natural-language work order. The host supplies a causal boundary, adapter/encoder proposal, dimensions, losses, baselines, audits, use mode and planned evidence contracts. The validator consumes that mapping and returns validity plus structured diagnostics. The host is instructed to correct every error and validate again. It owns the revisions; the validator can reject declared inconsistencies but does not decide which scientific design will work. No mandatory per-field human approval, retry budget or automatic model-repair controller is established by this workflow. SRC-1: `jepa-anything-skill/SKILL.md`; [RT-OBJ-design-config](runtime.md#rt-obj-design-config), [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation).

The source's repair instruction and the validator's limits are retained in those runtime records. A passing report is not an oracle for learned performance. It admits declared completeness on covered paths, not truth of task facts or empirical claim support. SRC-1: `jepa-anything-skill/scripts/validate_design.py`; [RT-CLM-validation-scope](runtime.md#rt-clm-validation-scope).

### 3. Valid design to generated package

The host invokes the generator CLI with the configuration and destination. The CLI repeats validation independently: invalid input prints the diagnostic report and returns 1 without calling the renderer. Thus skipping the earlier standalone validator does not skip the CLI gate. The direct Python renderer is a material exception: it accepts a supplied report without independently checking validity. This distinction is established in [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission), not a system-wide guarantee of unbypassable admission. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`.

After admission, the renderer specializes fixed templates with configuration values. It persists the selected-format configuration, validation report, generated interfaces/tests and a manifest identifying files and `contains_training_loop: False`. The package is assembled in a temporary sibling directory and promoted to the destination. Files and a success JSON response constitute renderer completion; neither establishes that the host tested or delivered them. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`; [RT-OBJ-scaffold-manifest](runtime.md#rt-obj-scaffold-manifest).

### 4. Generated package to contract checks and user handoff

The Skill next instructs the host to run generated unittest contract tests. These inspect declarations and exercise positive and negative cases with fabricated inputs: shared identity, undeclared context fields, rank/geometry, capacity/activity and planned claim coverage. For the rollout branch, the test supplies an incrementing callback and, where required, synthetic exogenous inputs:

> result = consume_state(0, extras=extras)
> self.assertEqual(result, {horizon: horizon for horizon in horizons})
> --- `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`

This checks the selected consumer's interface behavior, not a real encoder, prediction quality or action policy. The eventual caller must supply actual callbacks and domain implementation; generated state dispatch is separately characterized by [RT-RTE-state-consumption](runtime.md#rt-rte-state-consumption). SRC-1: `jepa-anything-skill/assets/scaffold/tests/test_contract.py.tmpl`.

The source defines final reporting, not merely a successful tool exit:

> Report the mapping from the original world-model task to JEPA Anything, the generated paths, validator result, selected use mode, proposed adapter/encoder and dimensions, and unresolved data-owner assumptions.
> --- `jepa-anything-skill/SKILL.md`

Delivery therefore means the host returns the inspectable design handoff and its limits after the requested generation/check steps. The Skill requires running tests but does not provide an implemented delivery gate on their result or a specific failed-test recovery procedure. Test execution and successful host delivery remain unobserved. Training requests are explicitly assigned to a separate execution workflow after validated design completion; no such downstream execution is established here. SRC-1: `jepa-anything-skill/SKILL.md`.

### Rejection and recovery boundaries

Two source-supported rejection cases distinguish responsibilities. An invalid design is rejected by the generator CLI with diagnostics/exit 1; the host must revise the configuration and retry. A valid design aimed at a non-empty destination is rejected by the renderer, and the CLI handles the scaffold error with stderr/exit 2:

> raise ScaffoldError(f"Refusing to overwrite non-empty destination: {destination}")
> --- `jepa-anything-skill/scripts/generate_scaffold.py`

The tool does not choose a replacement destination or authorize deleting existing work. That next action remains with its caller. During rendering, exceptions remove the temporary tree and propagate; there is no versioned rollback of an already promoted package. This cleanup is narrower than general transaction recovery and does not promise concurrent-writer safety. SRC-1: `jepa-anything-skill/scripts/generate_scaffold.py`; [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission).

### Inspection coverage

Additional direct inspection for this member covered the complete Skill, conversion reference, generator and generated contract-test template. These are SRC-1 doctrine/design and implementation, respectively. They support the handoffs, rejection branches and bounded checks above. No target program, example or test was executed; no observed activation, autonomous completion or reliability conclusion follows.

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

#### On [RT-RTE-task-compilation](runtime.md#rt-rte-task-compilation)

Workflow handoffs: user/project facts enter the host's causal-boundary proposal; only unrecoverable causal blockers return to the user. Configuration and diagnostics cross the deterministic-tool boundary. The host is instructed to revise the proposal, invoke generation, run contract tests, and report a task-to-design map plus generated paths and assumptions. The inspected Skill does not specify a worker delegation protocol: these are host/tool and host/user handoffs, not evidence of cooperating model workers. Verification supplies contract criticism, not empirical acceptance. The final narrative and inspectable files are the requested delivery; actual host compliance remains unobserved. Evidence is the Skill and conversion-reference passages in the Workflow account, together with this supplied route's repair instruction.

#### On [RT-RTE-scaffold-admission](runtime.md#rt-rte-scaffold-admission)

Workflow rejection/recovery: the CLI validity check runs even if the caller skipped standalone validation. Invalid designs return diagnostics before rendering; non-empty destinations reject without selecting recovery actions. The caller must revise the input or choose a permissible destination. Temporary-tree cleanup handles rendering exceptions, not post-delivery rollback. Generation success is an intermediate handoff to the host's requested contract-test step, not proof of completed user delivery. Evidence is the generator implementation and retained rejection passage in the Workflow account, together with this supplied route's admission quote.
