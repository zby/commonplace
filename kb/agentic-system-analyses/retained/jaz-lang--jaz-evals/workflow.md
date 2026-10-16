---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "jaz-evals AppWorld JAZ workflow: root-directed batches, solver handoffs, submission recovery and graded artifact delivery."
run-id: AAS-2026-10-15-jaz-evals-17ab95f93794-01
reviewed-boundary: "2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72"
---

# jaz-evals workflow report

## Workflow account

### Selected workflow and evidence

This report follows the AppWorld JAZ arm from configuration through task delegation, feedback-driven prompt/tool revision and final evaluation artifacts. It is representative of the package's model-directed improvement workflow because `configs/appworld_jaz.yaml` explicitly connects the JAZ harness to `prompts/ttsi/jaz.md`. It is not representative of every method: ACE and per-task JAZ use Python-owned sequencing instead. The baseline routes are [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt) and [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue). Evidence is source implementation and shipped guidance under SRC-1, not an executed workflow. External JAZ, benchmark internals and historical run artifacts remain outside the supplied evidence, as the [boundary](boundary.md#boundary-and-evidence) explains.

The request is an operator-selected benchmark experiment, not an arbitrary end-user task. The configuration chooses AppWorld's `test_challenge` split and seed 42, a dated nano delegate model, a stronger dated root model, recursion/iteration hooks and a session cost budget. The CLI/configuration handoff and central runner are already established in [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt). The model does not choose the experiment's initial scope (SRC-1, `configs/appworld_jaz.yaml`).

### From configuration to a task-solving delegate

The central runner creates attempt-scoped environment and harness objects, sets isolation/artifact destinations, sets up the benchmark and calls the harness with an `AgentEnv`. The underlying environment stays with the runner for final grading. JAZ's adapter supplies environment instructions, single-task instructions and improvement guidance as distinct inputs. It scopes shared tools over the invocation tree but passes queue tools only to the root. Root-only configuration overrides select the stronger root model; ordinary descendants receive the tree configuration (SRC-1, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/harnesses/jaz_harness.py`; [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)).

The root is the task coordinator. Its `get_next_task()` opens a fresh AppWorld context and returns the supervisor's identity and task instruction. Calling it again while a task is open raises an error rather than advancing past ungraded work. The root should pass the task and `single_task_instructions` to one solver invocation, initially adding a request to return session history. The solver inherits `apis`, but not `get_next_task`, `complete_task` or `tasks_remaining`. The single-task text does not automatically propagate. Thus the parent must construct a sufficient handoff; having the text in the parent's context is not delivery to the child (SRC-1, `src/jaz_evals/envs/appworld.py`, `src/jaz_evals/harnesses/jaz_harness.py`, `prompts/ttsi/jaz.md`).

> `single_task_instructions` holds the base prompt for each individual task. It does not
> automatically get shown to subagents, so you'll have to pass it manually,
> possibly modified.
> --- `prompts/ttsi/jaz.md`

The intended solver does benchmark work through the live shared API tree, then returns its answer and history to the root. This is a context boundary, not a transaction boundary: host API effects can survive the solver's return, while the history must be explicitly returned for the root's diagnosis. Actual delegation choices, returned histories and external runtime isolation are unobserved. The guidance's requirement that all solving occur in one child call per task is a policy, not a local Python scheduler or independently checked invariant (SRC-1, `prompts/ttsi/jaz.md`; [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)).

### Verification, rejection and the next batch

The root calls `complete_task(answer)` after the solver returns. That environment method submits through a private API tree, invokes the external grader, records the result, closes the world and advances the cursor. Solver return alone does none of these. Its feedback includes success, assertion counts/descriptions and potentially expected-versus-actual details; task IDs/indices are retained on disk but removed from the agent-facing copy. The package interprets the grader output but does not implement the underlying AppWorld correctness oracle in the registered source (SRC-1, `src/jaz_evals/envs/appworld.py`; [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)). Submission-shape rejection and task-grader failure have code-owned continuation paths detailed in [WF-RTE-task-submission](#wf-rte-task-submission).

The intended revision cycle begins with roughly five tasks using a minimal seed. The root reads histories and grading feedback, formulates a diagnosis and changes prompt text or helper tools. Later tasks are validation inputs. The prompt requests general lessons rather than task-specific patches, larger batches and smaller edits after success, and no changes after especially strong results. It also requests removal of unreliable or unused tools. These are model-interpreted decisions, not deterministic success thresholds enforced by the harness (SRC-1, `prompts/ttsi/jaz.md`; [RT-CLM-ttsi-experiment](runtime.md#rt-clm-ttsi-experiment)).

> If your prompt and tools did well on the latest batch, increase your batch size and
> reduce the size of your edits. If your prompt and tools did really well (e.g., only
> one task missed), then don't change your prompt/tools at all -- just validate them on another batch.
> --- `prompts/ttsi/jaz.md`

The root proposes, tests and can discard the change. There is no separate human per-edit approval or software gate requiring demonstrated improvement before later solver input changes. Retained context within the root's attempt can shape subsequent delegates; no actual authored change or subsequent semantic dependence is supplied. The baseline's independent learning, theory and self-improvement limits remain applicable; this trace adds no exercised-improvement claim ([RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue), [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance)).

### Failure ownership and delivery

Recovery has distinct owners. Guidance asks the root to catch child errors and discard unhelpful changes. The environment owns submission recovery and task-level grader-error reporting. The harness catches non-interrupt invocation failures, records a traceback and returns an error-status report with usage; the central runner can still grade completed work. This is partial-result delivery, not restart or resumption. Cleanup or final grading failures can prevent the attempt record, and operator interrupts deliberately propagate (SRC-1, `prompts/ttsi/jaz.md`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/eval_harness.py`; [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt)).

A normal root return is also not proof of queue exhaustion. The harness installs a completion-based return validator, but AppWorld inherits the base environment's `True` completion result. The baseline establishes this forcing case in [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue). Therefore prompt-requested exhaustion is not enforced by that validator in the selected arm. Final grading uses the whole queue as denominator, counting unreached tasks as unearned rather than granting full credit for an early exit (SRC-1, `src/jaz_evals/envs/appworld.py`).

> return Grade(score=_score(self._results, len(self._task_ids)), extra=_aggregate(self._results))
> --- `src/jaz_evals/envs/appworld.py`

Delivered output has two levels: a task has been submitted/graded and its cursor advanced; an evaluation attempt has a `RunReport`, final environment grade and written attempt record. The central run writes aggregate results only after all attempts return. It may also write analysis, while traces and task-result rows support later inspection. Neither a successful root return nor a written results file establishes task correctness or reliable improvement. The return value of the root invocation is not the score (SRC-1, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/harnesses/jaz_harness.py`; [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt)).

### Additional source inspection

All inspection remains within SRC-1 at the reviewed commit. This member checked `configs/appworld_jaz.yaml` and `prompts/ttsi/jaz.md` in full; `src/jaz_evals/harnesses/jaz_harness.py` at the root assembly, invoke and exception handling; `src/jaz_evals/eval_harness.py` at attempt execution and aggregate delivery; and `src/jaz_evals/envs/appworld.py` at grading, queue tools, submission-shape recognition, submission retry and task-grader failure handling. These supply implementation and doctrine/design evidence only. The new task-submission record narrows a material substep of the supplied whole-queue route; other workflow findings annotate or cite existing referents rather than redeclaring them. No target code, examples, services or tests were executed.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-task-submission
Label: AppWorld task submission and rejection recovery

Part of: [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)

This is the contained completion subroute, not another whole-queue method. Endpoints/progression: root's `complete_task(answer)` → private submission → optional shape-error retry → external evaluation → retained row and agent feedback → closed world/advanced cursor. Owner: AppWorldEnv's Python code; the model supplies the initial answer but does not decide retry or task-grader exception handling. State/effects: submission mutates the active benchmark world; results append to in-process state and are streamed to the task-results sink. SRC-1, `src/jaz_evals/envs/appworld.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: feedback dict containing evaluation results, optional submission/grader error and remaining-task/next-step guidance; retained task identity is omitted from the returned copy.
- Later read-back: inapplicable — this subroute records task outcomes, not revised guidance; any root-mediated reuse belongs to the containing batch workflow.
- Delegated visibility: the root receives feedback; children inherit APIs but not this queue method. Forwarding feedback to later children is model-directed.
- Selection predicate: an open task is required; after failed submission, retry once as None only for a non-scalar answer and a message containing the case-insensitive phrase `input should be a valid`.
- Invalidation or expiry: world closes and cursor advances after result recording; repeated completion without another open task raises. Retry replaces the submitted answer rather than undoing prior task API effects.
- Activation or effect: Python wires submission, grading and advancement; no actual recovery or subsequent agent response is observed.
- Evidence limits: external submission/grader semantics are unavailable; text-matched rejection recognition depends on dependency wording, and a streamed-row OSError is swallowed rather than guaranteeing durable diagnostic delivery.

Verification and recovery: software chooses whether to retry, not a human or another model. Value errors do not trigger the shape retry. A successful retry still records the original submission error with an explanatory suffix; a failed retry returns the first error. Grading proceeds despite submission failure. A task-grader exception becomes a failed result with an error field, allowing the queue to advance; failure of the attempt's final grade is a separate propagated failure. These checks preserve measurement/continuation, not semantic acceptance of advice or proof of a correct answer. The answer oracle is the excluded AppWorld grader, used in a finite benchmark curriculum. Source comments about historical failure rates are reported operation, not verified outcomes here (SRC-1, `src/jaz_evals/envs/appworld.py`).

> if answer is None or isinstance(answer, (bool, int, float, str)):
>     return False
> return "input should be a valid" in message.lower()
> --- `src/jaz_evals/envs/appworld.py`

> if not _is_answer_shape_error(answer, first):
>     return first
> second = self._submit_once(None)
> --- `src/jaz_evals/envs/appworld.py`

> except Exception as exc:
>     return {
>         "success": False,
>         "num_passed": 0,
>         "num_failed": 0,
>         "passes": [],
>         "failures": [],
>         "error": f"{type(exc).__name__}: {exc}",
>     }
> --- `src/jaz_evals/envs/appworld.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue)

Workflow handoff criterion: queue ownership stays with the root; each solver should receive the current task, manually forwarded single-task instructions and the current optimized prompt/helpers. Requested return is answer plus history. The parent receives both task effects through the shared world and diagnostic text through the returned history. Prompt policy assigns diagnosis, validation and rollback decisions to this same parent, rather than an independent verifier. Evidence does not establish compliance or successful rollback. Task-level code-owned rejection recovery is separated in [WF-RTE-task-submission](#wf-rte-task-submission).

#### On [RT-RTE-evaluation-attempt](runtime.md#rt-rte-evaluation-attempt)

Workflow delivery criterion: an attempt record can deliver partial graded work with an error status; successful task solving is not a precondition for writing it. Aggregate delivery waits for every attempt. This creates a distinction between task submission, attempt termination and run-level artifact completion; none substitutes for the others.
