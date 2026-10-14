---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Agno's sequential stock-research workflow: configured agent handoffs, failure policy and delivery at the frozen revision."
run-id: AAS-2026-10-13-agno-60e6e09dd4a6-01
reviewed-boundary: "00497422d4a386d93ab3b45c1a11faf42fcc932f"
---

# Agno workflow report

## Workflow account

### Selection and evidence

The representative workflow is the shipped three-agent stock-research pipeline: Data Gathering → Analysis → Report Writing. It was selected because one caller supplies the complete topology, specialized prompts and a concrete request. There is no need to construct a workflow from unrelated capabilities. The main trace follows its returning SDK execution path; the example's executable driver instead requests streaming. The stream dispatch and terminal-output seam were inspected separately, not assumed equivalent in every branch. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/workflow.py`.

The evidence boundary is [boundary](boundary.md). All added source inspection uses SRC-1 at the frozen revision. Added coverage includes the full sequential cookbook example, bounded Step construction, execution, input transformation and output wrapping in `libs/agno/agno/workflow/step.py`; HumanReview defaults in `libs/agno/agno/workflow/types.py`; and Workflow dispatch, sequential execution, failure handling, terminal output and persistence seams in `libs/agno/agno/workflow/workflow.py`. These supply implementation evidence; the example's prompts and comments also supply doctrine/design. No execution, tests, provider calls or outcome traces were supplied or performed. A wired sequence is not evidence that a market brief was successfully delivered or correct.

### Request, delegation and consequential handoffs

The caller fixes the order rather than asking a leader model to choose delegates. The concrete request is “Analyze NVIDIA (NVDA) for investment.” Workflow.run initializes execution input, run/session/user identities and RunContext, prepares configured steps and selects the stream or returning branch. In the returning branch the host iterates the step list, creates StepInput from the original execution input and accumulated outputs, and calls each configured Step. The outer progression is [WF-RTE-sequential-delivery](#wf-rte-sequential-delivery); the per-executor handoff is the existing [RT-RTE-workflow-step](runtime.md#rt-rte-workflow-step). SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/workflow.py`.

> steps=[
>     data_step,  # Step 1: Gather data
>     analysis_step,  # Step 2: Analyze data
>     report_step,  # Step 3: Write report
> ],
> --- `cookbook/00_quickstart/sequential_workflow.py`

1. **Data Gathering.** The Data Gatherer uses Gemini and grants YFinance stock-fundamentals, key-financial-ratios and historical-prices tools. Its instructions request current price/change, capitalization/volume, ratios, annual range and trends, then require organized raw data without analysis. With no prior output, the step receives the original request. The agent owns its internal model/tool decisions through [RT-RTE-agent-run](runtime.md#rt-rte-agent-run), not the next workflow-stage decision. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/step.py`.
2. **Analysis.** The Analyst receives the last step's deepest content as its primary message, not automatically the whole original request and every tool response. Its own prompt asks for strengths, weaknesses, red flags and limits on unsupported comparisons, and disallows recommendations. No tools are explicitly granted to this Agent in the example. The host does not check that gathered data are comprehensive before dispatching it. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/step.py`.
3. **Report Writing.** The Report Writer's primary message is the Analyst's content. Its prompt requests a one-line summary, a bullish/neutral/bearish research outlook with rationale, no more than 200 words and a small metrics table. These are natural-language requests to the model, not measured acceptance conditions. In particular, the writer is not automatically given the raw market-data/tool record; metric fidelity depends on what survives the Analyst's output. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/step.py`; instruction force is described by [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions).

Each Step supplies its executor a fresh child run ID linked to the workflow, the session ID, user identity, media and configured context controls. With RunContext present, session state is intentionally shared between steps, although the context object itself is shallow-copied. Separate agent messages therefore do not establish full state isolation. Workflow history can optionally be prefixed, but the Workflow default is not to add it and this example does not enable it. Original inputs and prior outputs remain host-side even when omitted from the next primary message. No automatic reload of omitted raw evidence is established for these downstream agents. SRC-1: `libs/agno/agno/workflow/step.py`, `libs/agno/agno/workflow/workflow.py`.

> # Create session_state copy once to avoid duplication.
> # run_context.session_state is shared intentionally across steps in the same workflow,
> # so we use a direct reference. The session_state parameter (used for nested workflows)
> # is deepcopied to prevent cross-workflow mutation.
> --- `libs/agno/agno/workflow/step.py:1119-1122`

### Verification, failure and recovery

This selected caller configures neither a reference answer nor a dedicated reviewer, output schema, confirmation requirement or output-review requirement. HumanReview defaults leave confirmation and output review off. The prompts demand careful work, but do not implement a factual-answer oracle or verify the 200-word limit. Software acceptance checks execution state and configured control policies, rather than whether the investment analysis is true. No claim of system-wide absence of review follows: the same Workflow implementation checks configured pre-execution pauses, executor tool pauses and post-execution review. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/types.py`, `libs/agno/agno/workflow/workflow.py`.

The failure path is materially more permissive than “every stage must succeed.” Step defaults allow three retries after the first attempt for raised ordinary exceptions. Cancellation and an unresolved callable bypass that retry loop. After exhaustion, Step's default skip_on_failure=False rethrows; **Workflow's separate default HumanReview.on_error is skip**, so its enclosing handler can turn that exception into a failed/skipped output and continue to the next agent. A returned Agent error/cancelled status becomes StepOutput.success=False; the fail-policy guard only raises under explicit fail policy without skip_on_failure. These are inspected source paths, not injected failures. SRC-1: `libs/agno/agno/workflow/step.py`, `libs/agno/agno/workflow/types.py`, `libs/agno/agno/workflow/workflow.py`.

> # Shared behavior
> on_reject: Union[OnReject, str] = OnReject.skip
> on_error: Union[OnError, str] = OnError.skip
> max_retries: int = 3
> --- `libs/agno/agno/workflow/types.py`

> elif step_on_error == "skip":
>     # Skip the failed step and continue
>     log_debug(f"Step '{step_name}' failed with on_error='skip' - skipping step")
>     step_output = _create_skipped_step_output(
>         step_name, getattr(step, "step_id", str(uuid4())), step_error
>     )
> --- `libs/agno/agno/workflow/workflow.py:2980-3239`

Consequently a later agent can receive failure/skipped text in place of the expected research product. A completed workflow can include failed steps: completion records lifecycle termination under configured policy, not successful financial research. Operators must inspect step_results as well as final content/status. Explicit fail policy instead records failure and propagates an exception; explicit pause policy stores the failing index, prior outputs and an error requirement and returns paused. Those alternate policies are available, not selected in this cookbook caller; continuation and reviewer decisions were not fully traced here. Host code owns retries, skip, pause and abort. Starting the request establishes neither human authorship of each output nor per-content human approval. Tool effects already performed are not shown to be undone by these policies. SRC-1: `libs/agno/agno/workflow/workflow.py`, `libs/agno/agno/workflow/step.py`; the local tool gate and its limits are [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation).

### What counts as delivered

For the returning path, the host collects StepOutputs, retains metrics/media and sets WorkflowRunOutput.content from the last output (or deepest nested last output). It marks completed, attempts session/run persistence in finally, cleans run/member tracking and returns the output. Persistence exceptions in that finalizer are logged, so a returning result is not proof of a successful durable write. The persistence helper performs separate session and run writes; no atomic commitment of those writes and external tool effects is established. The cookbook configures no database, so durable cross-run storage is not established for this example. SRC-1: `libs/agno/agno/workflow/workflow.py`, `cookbook/00_quickstart/sequential_workflow.py`.

> else:
>     workflow_run_response.content = last_output.content
> --- `libs/agno/agno/workflow/workflow.py:2980-3239`

The shipped script calls print_response with stream=True. The inspected successful-stream terminal seam yields WorkflowCompletedEvent carrying content, step_results, executor runs and run_output, then persists the session/run. Event emission precedes those writes. Moreover cancellation also emits WorkflowCompletedEvent as a stream-end sentinel while the enclosed run remains cancelled. Neither a completed-event name nor an early streamed chunk proves successful work or durable delivery. This report establishes the output boundary, not an observed terminal rendering or network/client receipt. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/workflow.py`.

> # Emit terminal completed event so clients have a single stream-end sentinel
> # (mirrors agent/team _build_cancel_terminal_events pattern).
> --- `libs/agno/agno/workflow/workflow.py:3792-3793`

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-sequential-delivery
Label: Sequential workflow progression and delivery

Distinct identity: this is the outer Workflow coordinator from request to final delivery, not the Step executor handoff in [RT-RTE-workflow-step](runtime.md#rt-rte-workflow-step). It invokes that route repeatedly and contains the workflow-level acceptance, error policy, aggregate return and persistence seam. The agent's internal execution remains [RT-RTE-agent-run](runtime.md#rt-rte-agent-run). No supplied runtime record separately declares this outer coordinator.

Endpoints/progression/owner: caller input → Workflow.run identity/context and execution-input preparation → ordered steps and accumulated StepOutputs → configured pause/error/failure policy → last output as final content → storage attempt and return. Host Workflow code owns ordering and termination; configured agent models generate products inside the steps. The selected caller fixes three specialized Agents. Session/user/run IDs bind context and records, fresh executor run IDs link child work, and shared state/media can carry effects across steps. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/workflow.py`, `libs/agno/agno/workflow/step.py`, `libs/agno/agno/workflow/types.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Returning execution produces WorkflowRunOutput with final content, step_results, metrics/media and lifecycle status; the script selects streaming, whose terminal event contains the run output. Exceptions can propagate instead of delivering a brief.
- Later read-back: Configured persistence writes session/run records; optional workflow history can prefix later step invocations. The selected example supplies no database or history enablement, so durable read-back for this caller is not established; detailed resume selection is uninspected.
- Delegated visibility: StepInput holds original execution input and accumulated outputs; agent primary messages normally receive only the last output's deepest content. Optional history and feedback can add text. User/session identities, shared state and media travel separately; this is not transmission of all raw evidence.
- Selection predicate: Caller topology and stream flag select ordered execution and return mode. Error/review configuration controls pause, skip or failure; deepest last content selects final content.
- Invalidation or expiry: Run/member cancellation tracking is cleaned after returning execution. Persisted workflow checkpoint deletion/expiry is uninspected — backend lifecycle and resume invalidation were not traced.
- Activation or effect: Code dispatches configured executors, advances outputs/state/media and emits or returns aggregate output. Actual execution, factual correctness and downstream dependence on delivered text remain unobserved.
- Evidence limits: Main trace is synchronous returning sequential execution, with bounded inspection of streaming dispatch/terminal behavior. No full stream/async/graph equivalence audit, provider outcome, correctness oracle, atomic durable delivery or rollback of tool effects is established.

Decision roles and verification: caller specifies stages and policies; host checks pause/failure state; each agent model produces its stage's content. No human decision is required by this example's defaults. The operating mode is an open financial request in a configured pipeline. No expected/reference answer is supplied. Acceptance is a lifecycle/control decision, not independent task validation. Guidance is the specialized natural-language prompts; what can persist is run/session output under a configured backend, not an admitted revision to Agno's own machinery. Recovery permits Step retries, default Workflow skipping, or configured failure/pause. No theory-building or self-improvement conclusion is inferred from improving an external report.

Minimum passages for topology and default failure policy are retained in the Workflow account. The final status assignment is explicit:

> workflow_run_response.files = output_files
> workflow_run_response.status = RunStatus.completed
> --- `libs/agno/agno/workflow/workflow.py:2980-3239`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-workflow-step](runtime.md#rt-rte-workflow-step)

Workflow-specific handoff finding: the selected pipeline's caller fixes all three delegates; there is no model-controlled member selection at this boundary. Data → Analyst → Writer transforms model-visible context twice. The writer's metrics table is requested from the Analyst's content, without automatic access to raw gathering output. This is stage isolation by selected messages, not a clean stack-frame pop: shared RunContext.session_state and retained step results escape the frame. Source coverage and passages are in the Workflow account and SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/step.py`.

Verification annotation: _process_step_output sets success from returned executor status, not answer truth. A failed flag alone does not enforce abort; the outer coordinator applies HumanReview.on_error and skip_on_failure. The selected caller inherits on_error=skip. This additional outer policy is declared in [WF-RTE-sequential-delivery](#wf-rte-sequential-delivery), without changing the existing Step route's identity or its nested-pause limitation. SRC-1: `libs/agno/agno/workflow/step.py`, `libs/agno/agno/workflow/types.py`, `libs/agno/agno/workflow/workflow.py`.

> # Propagate cancelled / error status from the executor's RunOutput
> response_status = getattr(response, "status", None)
> success = response_status not in (RunStatus.cancelled, RunStatus.error)
> error = response.content if not success else None
> --- `libs/agno/agno/workflow/step.py`
