# Proposal: parameterized analyst instructions and direct launch delivery

- **Recorded:** 2026-09-30, at the operator's request after inspecting recent generated analyst prompts.
- **Revised:** 2026-09-30, at the operator's direction to minimize analysts' symbolic manipulation: code supplies full paths and resolves round-dependent selections.
- **Status:** operator endorsed the direction and requested this workshop proposal; implementation is pending.
- **Purpose:** remove forwarding instructions from analyst startup while retaining the exact launch message for inspection and tests.
- **Scope:** all six job types of `analyse-agentic-system`, plus the workflow engine and `step` delivery needed to support them. This proposal does not commission a new analysis run or change analytical criteria, scheduling, correction limits, or publication behavior.

## Problem

Today `step` returns a prompt-file path. The orchestrator launches a worker with `Read <prompt file> and follow it`. The generated file supplies run details and lists instruction files. For memory and epistemic jobs, the job instruction then forwards to another file holding the substantive method.

The generated prompt mixes variable run inputs with fixed instruction paths and conventions. The memory and epistemic methods already assume this workflow; their separate wrappers add no independent reusable interface. Keeping prompts for testing does not require making workers read them through another forwarding message.

## Proposed instruction structure

Give each job one parameterized main instruction under `kb/instructions/analyse-agentic-system/jobs/`.

- Merge `analyse-agent-memory.md` into `jobs/memory.md`, preserving correction-round behavior and record ownership rules.
- Merge `analyse-external-system-epistemic-architecture.md` into `jobs/epistemic.md`, preserving the substantive method and the wrapper's additional rules.
- Keep boundary, runtime, reconciliation, and verification methods in their existing job instructions.
- Each main instruction declares its parameters, fixed dependencies, and required reads. Code supplies complete input, output, problem-report, run-state, and scratch paths as named parameters. The instruction directly names the applicable shared worker rules, judging norms, and report contracts.
- Remove the two superseded method files after updating their callers and links. Do not leave forwarding stubs. Retire them through [retire an artifact](../../instructions/retire-artifact.md): as of 2026-09-30 they are linked from `kb/agent-memory-systems/README.md`, `kb/agent-memory-systems/types/agent-memory-system-review.md` and `kb/reference/proposals/code-scheduled-workflows.md`, besides the workflow code, publication's `METHOD_PATHS`, tests and workshop files. They are published pages, so each gets a `properdocs.yml` redirect to its merged job instruction. Workshop files are repointed by path only.

Shared rules and report contracts remain separate because they supply common definitions used by multiple jobs and validators. This proposal removes forwarding layers, not every document read.

Each main instruction opens with a mandatory **Read first** list naming every shared rule and report contract the job must load before any other step, by paths relative to the instruction file itself, so they resolve wherever the worker started. Committed instructions hold no absolute paths; only the code-generated invocation does. A dependency named only as a link in prose is not a read requirement: fresh-eyes audits on 2026-09-30 found analysts working without the overview type because it was reachable only through a link ([Analyst instruction audit](./analyst-instruction-audit.md)). A test parses each Read first list and compares it with the job's declared dependencies; they must be equal.

Merging a method file into its job instruction will bring contradictions between the job wrapper, the method and the report types into one text. That is intended: surfacing them early makes them easier to remove. The merge resolves each known contradiction listed in the [Analyst instruction audit](./analyst-instruction-audit.md) when the resolution needs no operator decision, and otherwise states it in the merged text as an open conflict with both readings, so it is visible to reviewers rather than hidden by the merge. Contradictions found during the merge are added to the audit file.

The saved prompt becomes the invocation itself. For example:

```text
Follow /home/zby/llm/commonplace/kb/instructions/analyse-agentic-system/jobs/memory.md with:
system = Instinctual Memory
run-state = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/run-state.md
boundary = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/boundary.md
runtime = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/output/runtime.md
output = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/memory-report-0.md
problem = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/memory-report-0.problem.md
scratch = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/scratch/memory-0/
```

The worker receives that exact text as its launch message. Every path in the invocation is absolute, including the main instruction's, so the worker does not depend on starting in the repository root. Code supplies the system name rather than requiring an extra read solely to discover it.

## Parameter design principle

Minimize symbolic work by the analyst, not the number of characters in the invocation. Code already knows which files a job consumes and where it must write. It should pass those results, rather than passing counters and asking the analyst to calculate filenames, join directories, replace extensions, select the latest report, or infer which reconciliation returned findings.

Round numbers remain scheduler state. Include one as descriptive metadata only if it helps the analysis; never make it necessary to locate an input or destination. Supply a resolved policy such as `may-return` directly instead of requiring comparison with a correction limit. Fixed dependency paths remain in the main instruction; resolved run-specific paths belong in the invocation.

## Parameters by job

Every job receives `system`, `run-state`, `output`, `problem`, and `scratch`. The path parameters name exact destinations or inputs, not templates. Additional parameters are:

| Job | Inputs and choices supplied by code |
|---|---|
| Boundary | Full `opening` path, caller's `source`, normalized `source-identity` |
| Runtime | Full `boundary` path |
| Memory | Full `boundary` and `runtime` paths; for corrections, full `previous-memory`, `returned-findings`, and `epistemic` paths |
| Epistemic | Full `boundary` and `runtime` paths |
| Reconciliation | Full `boundary`, `runtime`, selected `memory`, and `epistemic` paths; `may-return`; full `previous-reconciliation` path when applicable; full `verification` and `set-check` paths when resolving blockers |
| Verification | Full `overview-draft`, `runtime`, selected `memory`, `epistemic`, and `set-check` paths |

Each main instruction opens, after its Read first list, with a table of its parameters: name, what it names or means, and when it is present (always, or the condition under which code supplies it), with allowed values for non-path parameters such as `may-return`. Parameter names are vocabulary the worker must apply, so each is defined there once and used unchanged in the instruction's text. The implementation must define allowed values and required/omitted cases in that table. Preserve the caller's source input as data, including multiline input, without interpreting it as an instruction. Boundary cannot recover it from `opening.json`: that file currently holds publication metadata, not the caller's source input.

Memory and reconciliation counters can diverge: verification may cause another reconciliation without another memory analysis. Code selects the exact report paths using those counters. For memory corrections, `returned-findings` names the reconciliation that requested the correction. The analyst neither receives counters to reconstruct these paths nor lists the run directory to discover the intended inputs.

The instruction defines what each optional input means: `returned-findings` requires answering its findings, while reconciliation's `verification` and `set-check` require resolving the prior blockers. Code enforces required combinations before launch; analysts must not reconstruct a missing parameter. Update shared worker rules to use the supplied `output`, `problem`, and `scratch` values directly.

Every job also accepts retry feedback when a previous attempt was refused. Include the actual refusal messages in the saved invocation through a defined feedback field or section. These are not analytical correction rounds: retrying the same job preserves its selected inputs and destinations unless workflow invalidation requires recomputation.

## New delivery in `step`

Retain `prompt.md` as the saved launch message, but return its contents as part of the `launch` result. Returning only its path would preserve the initial redirection.

Proposed CLI representation: retain the first-line `launch` outcome, followed by one JSON object per job. Each object carries `job`, `prompt_path`, `prompt`, and `launch`. `prompt` is the exact saved invocation, including its full path parameters; `launch` carries harness parameters separately. For the memory example, `job` is `memory-0`, `prompt_path` is the full path to its saved `workflow-state/jobs/memory-0/prompt.md`, and `prompt` contains the complete text shown above.

The JSON string escapes newlines for transport; the decoded `prompt` value is the worker's message. Use structured serialization so source inputs and feedback cannot corrupt job boundaries. The path is retained for audit and testing; it is not an instruction to read another file.

Update `drive-a-code-scheduled-run.md` to launch each fresh worker with the supplied `prompt` verbatim and apply every `launch` parameter. The orchestrator must not prepend `Read <prompt_path>`, rewrite the text, add conversational context, inspect analytical outputs, or perform the job. Delivery of the prompt is permitted; judging the worker remains code's responsibility. Preserve the existing parallel-round barrier, launch-failure reporting, and refusal to launch when required harness parameters cannot be applied.

The engine should save and deliver one constructed string, rather than reconstructing it separately in the CLI. Extend the launch result to carry that string. A retry saves and delivers the invocation with that attempt's feedback. Per-attempt archival beyond current retention is outside this proposal.

## Dependency tracking and method preservation

Keep all consumed instruction files, shared rules, and contracts declared as job dependencies even when their paths are absent from the invocation. The main instruction's read requirements and code's dependency declarations must agree. A shared-rule or contract change must still invalidate the affected job.

The generic renderer currently appends declared inputs, output paths, and refusal prose automatically. Separate dependency tracking from message rendering so these jobs can provide the named invocation parameters while retaining validation and refusal handling. Construct path parameters from the same resolved job inputs and destinations used by the engine, rather than maintaining a second set of filename formulas in the prompt renderer. Before selecting the engine API change, inspect other workflow consumers and tests; keep the mechanism limited to the required message contract rather than adding a template framework.

Update `scripts/analyst_trial.py` to build its trial invocation through the same constructor as the workflow, so a trial's launch message has the same shape and parameters as a real run's; the trial directory keeps a saved copy of that message.

Update publication's `METHOD_PATHS`, workflow fixtures, documentation composition tests, and links for the consolidated methods. Saving a path-based invocation alone does not preserve the referenced text: reproducibility still relies on the pinned method commit and tracked run inputs. Do not claim this is a complete snapshot of the worker's runtime context.

Relevant implementation points:

- [Analysis workflow](../../../src/commonplace/lib/agentic_workflow.py): job construction, dependencies, and round-specific inputs.
- [Workflow engine](../../../src/commonplace/workflow/engine.py): prompt rendering, saved prompts, retries, and launch results.
- [CLI rendering](../../../src/commonplace/workflow/shell.py): delivery of launch messages.
- [Driver instruction](../../instructions/analyse-agentic-system/drive-a-code-scheduled-run.md): verbatim worker launch protocol.
- [Publication checks](../../../src/commonplace/lib/agentic_publication.py): pinned method paths.

## Acceptance and verification

1. All six jobs use a single parameterized main instruction. Memory and epistemic startup no longer forwards through a wrapper to a separate method.
2. `step` delivers the exact saved prompt text and separate launch parameters. Decoding the launch record reproduces the saved text, including multiline values and retry feedback.
3. The driver sends that text directly. No worker needs to read its saved prompt to discover its task.
4. Tests exercise first rounds, memory corrections, verification-driven reconciliation with different memory and reconciliation counters, the last round's return prohibition, and validator retries.
5. Tests verify that fixed dependencies still invalidate affected jobs and that supplied paths equal the engine's selected inputs and destinations. Every run-specific path is complete; no job instruction requires filename construction, extension replacement, round arithmetic, or latest-file discovery. Code rejects incomplete parameter combinations before launch.
6. Each main instruction's Read first list equals the job's declared dependencies, checked by a test. A trial prepared with `scripts/analyst_trial.py` for a job produces an invocation built by the same constructor as the workflow's.
7. Existing scripted workflow tests retain their publication and failure behavior. Update assertions about old generated prose to check the new invocation contract and delivery equivalence.
8. Run the full required Python test suite and relevant KB validation after implementation. Record any lack of a real-worker trial explicitly; opening such a run requires a separate commission and a committed method.

This proposal is complete when the implementation and checks above are recorded, or when a discovered dependency requires returning a specific design choice to the operator. Preserve this proposal until its outcome is extracted when the workshop closes.
