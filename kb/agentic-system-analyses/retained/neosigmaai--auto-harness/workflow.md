---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "auto-harness workflow: Terminal-Bench candidate revision from prepared baseline through task delegation, rejection, commit-linked recording and operator delivery."
run-id: AAS-2026-10-15-auto-harness-92303e444cb2-01
reviewed-boundary: "52360dbbeb8cea8886d90778e634a145c51da735"
---

# auto-harness workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is one Terminal-Bench improvement iteration inside the prescribed repeated optimization loop. It was selected because the shipped program joins failure diagnosis, whole-file candidate revision, executable benchmark delegation, regression gating and commit-linked recording. This is not a workflow reconstructed by combining unrelated benchmark integrations. Preparation supplies the initial candidate, composed program, baseline and task split under [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline). The account starts from that prepared state and follows an external coding agent's request to improve benchmark performance through to the requested final operator summary.

The evidence is SRC-1 at the boundary revision. Direct inspection for this member covers `program_templates/base.md`, `program_templates/terminal_bench.md`, `agent/templates/terminal_bench.py`, `gating.py`, `record.py` and the Terminal runner in `benchmark.py`. These are already within the boundary's registered coverage. Python supplies implementation evidence; program templates supply doctrine/design. No execution, actual optimized candidate, generated learning log or successful delivery was supplied. The external coding agent and Harbor's internal scheduler, sandbox and verifier are outside the frozen implementation boundary. Thus the account establishes a coordinated procedure and wired local handoffs, not demonstrated autonomous completion or improved performance.

### 1. Outer delegation and train evaluation

The human/operator supplies the benchmark configuration and launches an external coding agent against the generated program; the repository does not implement that agent's scheduler. The program assigns candidate editing and experiment coordination to that agent. Its compact procedure is explicit:

> run benchmark → analyze failures → improve agent → gate → commit → repeat
> --- `program_templates/base.md`

The first handoff is from the coding agent to `python benchmark.py`. In the selected Terminal route, `TerminalBenchRunner` loads the configured split unless explicit task IDs are supplied. It launches Harbor with dataset, selected IDs, model, environment provider, concurrency, timeout multiplier, jobs directory and the import path `agent.agent:HarnessAgent`. It supplies a repository-root Python import path and model environment. Harbor receives executable candidate code and benchmark selection, not the outer agent's entire diagnostic conversation. See [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task) and SRC-1, `benchmark.py`.

Harbor then supplies each candidate invocation with the task instruction, environment and accounting context. The stock candidate constructs a fresh model conversation from its system instruction and that task. The model chooses bash calls; local Python dispatches them through the Harbor environment with a 120-second command timeout. Tool outputs, including nonzero return-code markers, enter subsequent model context after truncation to beginning/end segments. This is a task-local frame, not an outer coding-agent sub-conversation: what escapes into outer diagnosis is a reward/result mapping and optionally copied conversation evidence. No repository mechanism hands the full outer context down or imports the candidate's hidden model processing back (SRC-1, `agent/templates/terminal_bench.py`; [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task)).

Text without tool calls ends the stock candidate loop. It is a declaration of completion, not acceptance. Harbor's external verifier supplies the reward subsequently parsed by the local runner. The frozen source does not establish the verifier's reference answers or validity. The caller receives printed results and persisted CLI result state, not a trustworthy proof that the candidate solved every selected task. Those distinctions are retained in [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task).

### 2. Evidence handback and candidate proposal

For train runs, the runner copies task traces and result files into `workspace/traces/latest/`; it preserves a first per-task baseline separately. The stock trace contains the messages after output truncation, not omitted middle output. The supplement routes diagnosis specifically to the latest train copies:

> **Only read traces in `workspace/traces/latest/`.** Do not look in `workspace/tbench_jobs/` — it contains both train and test data.
> --- `program_templates/terminal_bench.md`

For non-train runs, the runner sets `HARNESS_SAVE_TRACE=0`, which the stock candidate honors. This is partial implementation support for the train-only diagnosis policy, not a filesystem restriction on the coding agent or a guarantee about external logs. Modified candidate Python could also change trace behavior (SRC-1, `benchmark.py`, `agent/templates/terminal_bench.py`; [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task)).

The coding agent is asked to inspect failing train traces, distinguish prompt problems from tool problems, append findings and make one focused change. It owns the entire candidate file: instructions, tool schema, output processing and loop implementation are possible proposal targets. The supplement's suggested techniques guide proposals; its percentage estimates are not measured evidence here. The proposer is the external coding agent, while the following gate is the computational decider. No per-edit human approval appears in the supplied procedure, but actual external-runtime permissions remain uninspected. This diagnosis/revision handoff is [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), not an additional optimizer implemented in Python.

### 3. Gate decision and rejection recovery

The coding agent next calls `python gating.py`. A successful exit requires the local gate's checks, not the coding model's confidence. The guard first checks disallowed paths if enabled. The regression phase reruns stored suite IDs on the train runner, counts missing requested suite results as failures and compares the pass fraction to the suite threshold. It persists `last_results` before deciding final admission. An empty suite skips this check. The test runner then executes the configured gate split even if the suite check failed; its returned mean is compared with the maximum recorded score. Equal score can pass. These mechanisms and their evidence are [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission), SRC-1, `gating.py`.

A concrete rejection branch is suite pass fraction below threshold. The gate returns 1 after test evaluation and before promotion. It does not undo the candidate edit or the saved suite diagnostics. Recovery ownership returns to the external coding agent through the program:

> **Exit 1** (any step failed) → revert and try a different approach:
> --- `program_templates/base.md`

The prescribed command is `git checkout agent/agent.py`; three consecutive failures of one hypothesis require abandoning it. Neither rollback nor hypothesis counting is implemented by `run_gate`. In particular, a file-guard rejection can concern another tracked or untracked path: reverting the candidate alone does not necessarily remove that violation. The guard's diagnostic instead asks the caller to revert/remove the named paths and rerun. Its printed bypass and Git-unavailable fail-open behavior further limit edit confinement. This is a best-effort path check, not sandbox enforcement (SRC-1, `gating.py`; [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission)).

The task-level failure branch is different: unknown tools or malformed JSON produce tool messages and allow another model step; a model-call exception ends the candidate loop. A missing verifier yields `None` on parsed trial paths. If Harbor creates no recent job directory, the runner returns an empty mapping before filling missing selected IDs. Consequently, successful gate arithmetic does not prove complete evaluation: an empty suite and absent/zero prior best can admit a zero empty-result mean. This source-level forcing case is not an observed incident (SRC-1, `benchmark.py`, `agent/templates/terminal_bench.py`; [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission)).

### 4. Acceptance, retained consequences and delivery

Only after suite and test checks pass does the gate rerun formerly failing non-suite tasks from the last CLI result mapping. Newly passing returned IDs enter the persistent suite. This changes what later iterations must preserve; it does not itself install or commit candidate code. The result loader does not enforce the saved mapping's train provenance, so the procedure's requested preceding train evaluation matters (SRC-1, `gating.py`; [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission)).

After exit 0, the coding agent is instructed to commit `agent/agent.py` and call `record.py` with the gate's printed test score and suite counts. The recorder checks paths including the latest commit, obtains a short Git label and appends a TSV row. It does not consume an authenticated gate result or verify that the committed content is precisely what was evaluated. Therefore gate→commit→record is an instructed handoff, not an atomic transaction. Later gates use the maximum recorded score, making trusted caller-supplied accounting consequential (SRC-1, `record.py`, `gating.py`; [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record)).

The program requests learning-log updates after both success and failure, including attempted changes, outcomes, recurring patterns and needs from the human. The next iteration imports the candidate again and reads retained evaluation state through the routes above. Actual reuse of learning prose is not supplied as run evidence. The intended stopping/delivery criterion is:

> **Stop when** val_score has not improved for 5 consecutive iterations — write a summary in `learnings.md` and surface your top findings to the human
> --- `program_templates/base.md`

Accordingly, delivery has two levels: a successful iteration yields an intended candidate commit plus score row and learnings; the outer workflow ends with an intended summary to the operator after stagnation. The repository supplies no automatic final packaging, notification or independently checked stopping counter. Committed code, appended history and an instructed human-facing summary are distinct outputs; none establishes that a supplied run reached delivery. Retained updates, their subsequent authority and their unobserved activation are already separated in [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record) and [RT-BAP-history-gate](runtime.md#rt-bap-history-gate).

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

#### On [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task)

Workflow role: delegated task execution, followed by a restricted diagnostic handback. Candidate completion text is subordinate to verifier-derived rewards; copied messages are subordinate to their truncation and trace-selection limits. The outer coding agent, not the task candidate, owns the next revision decision.

#### On [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission)

Workflow role: computational acceptance/rejection checkpoint between proposal and requested commit. Suite diagnostic state can change on rejection, whereas suite membership promotion requires successful checks. Recovery crosses back into the external coding-agent procedure; a failed gate is not an automatic restored working tree.

#### On [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record)

Workflow role: durable accounting after the requested commit, not a delivery certificate. Its row becomes a future decision input, but the gate-to-record handoff trusts caller-provided numbers and procedural sequencing.
