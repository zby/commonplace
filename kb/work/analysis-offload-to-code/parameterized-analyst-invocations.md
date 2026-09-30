# Proposal: parameterized analyst instructions and direct launch delivery

- **Recorded:** 2026-09-30, at the operator's request after inspecting recent generated analyst prompts.
- **Revised:** 2026-09-30, at the operator's direction to minimize analysts' symbolic manipulation: code supplies full paths and resolves round-dependent selections.
- **Revised:** 2026-09-30, after a check against the goal of a simpler process and easier analyst work, with the operator's decisions on delivery: code writes the invocation into the prompt file, the orchestrator reads that file and sends its content as the worker's message, and this holds for every code-scheduled workflow. Code also lists the required reads, the merge deletes restated shared rules, and the round kind is a parameter.
- **Revised:** 2026-09-30, after a readiness check against the code: workers keep the repository root as working directory, because `commonplace-validate` takes the root from it; `run-state` is classified; the engine change is one flag; the work is ordered.
- **Status:** operator endorsed the direction and requested this workshop proposal; implementation is pending.
- **Purpose:** give each analyst one instruction to follow, with code-resolved paths for everything it reads and writes, delivered as its launch message.
- **Scope:** all six job types of `analyse-agentic-system`, the engine's prompt rendering, and the generic driver instruction. `step`'s output does not change. This proposal does not commission a new analysis run or change analytical criteria, scheduling, correction limits, or publication behavior.

## Problem

Today `step` writes a prompt file and returns its path. The orchestrator launches a worker with `Read <prompt file> and follow it`. The prompt file supplies run details and one list of inputs. For memory and epistemic jobs, the job instruction then forwards to another file holding the substantive method.

Four things in this give the analyst work that the orchestrator or code could do:

- The worker's first act is to read a file that holds its real task.
- The memory and epistemic wrappers split one job's rules across two texts. The methods already assume this workflow; the wrappers add no independent reusable interface.
- The Inputs list mixes instruction files with work inputs and gives no input a role. The round note names files by bare name (`memory-report-0.md`), which the worker matches against the list.
- The run state and the scratch directory are given relative to "the run directory", which the worker derives from other paths.

For scale: a memory analyst's required instruction and contract text is about 53 KB, of which the three type specs are 41 KB. The prompt file and the wrapper add about 2.5 KB. This proposal removes steps and symbolic work; it does not reduce that reading.

## Proposed instruction structure

Give each job one parameterized main instruction under `kb/instructions/analyse-agentic-system/jobs/`.

- Merge `analyse-agentic-system/jobs/memory.md` into `jobs/memory.md`, preserving correction-round behavior and record ownership rules.
- Merge `analyse-agentic-system/jobs/epistemic.md` into `jobs/epistemic.md`, preserving the substantive method and the wrapper's additional rules.
- Keep boundary, runtime, reconciliation, and verification methods in their existing job instructions.
- Each main instruction declares its parameters. Code supplies complete input, output, problem-report, run-state, and scratch paths as named parameters, and the paths of the shared worker rules, judging norms, and report contracts the job must read.
- Remove the two superseded method files after updating their callers and links. Do not leave forwarding stubs. Retire them through [retire an artifact](../../instructions/retire-artifact.md): as of 2026-09-30 they are linked from `kb/agent-memory-systems/README.md`, `kb/agent-memory-systems/types/agent-memory-system-review.md` and `kb/reference/proposals/code-scheduled-workflows.md`, besides the workflow code, publication's `METHOD_PATHS`, tests and workshop files. They are published pages, so each gets a `properdocs.yml` redirect to its merged job instruction. Workshop files are repointed by path only.

Shared rules and report contracts remain separate because they supply common definitions used by multiple jobs and validators. This proposal removes forwarding layers, not every document read.

### Required reads come from code

The invocation lists, under `read-first`, the absolute path of every shared rule and report contract the job must load. Code generates the list from the job's declared dependencies. Each main instruction opens with one rule: read every file under `read-first` before any other step.

The list has one source, so the instruction and the code cannot disagree, and no test has to parse an instruction and compare two lists. The worker resolves no relative path. Committed instructions hold no absolute paths; links in their prose stay as documentation. A dependency named only as a link in prose is not a read requirement: fresh-eyes audits on 2026-09-30 found analysts working without the overview type because it was reachable only through a link ([Analyst instruction audit](./analyst-instruction-audit.md)).

A job's declared file dependencies are then exactly three groups, each visible in its invocation: the main instruction on the first line, the files under `read-first`, and the run-specific input files supplied as parameters. Output, problem-report, and scratch paths are destinations, and values such as `system` and `may-return` are not files; neither is a dependency. `run-state` is a file the worker passes to `commonplace-quote`, and it is not a dependency either: code rewrites it during the run, so declaring it would reopen accepted jobs.

### The merge

The merge does two things. It folds the wrapper's rules into the method. It deletes the method's restatements of the shared worker rules: `analyse-agentic-system/jobs/memory.md` restates the source-reading, quotation and prior-analysis rules, with a different placeholder (`<sibling-run-state-path>`), and after the merge those rules are in `worker-rules.md` only.

The merge will bring contradictions between the job wrapper, the method and the report types into one text. That is intended: surfacing them early makes them easier to remove. Handle each one as follows:

- Where a report type or a shared rule (`worker-rules.md`, `judging-norms.md`) settles the question, the merged text follows it: the validator enforces the types, and the shared rules are the common text the merge keeps. Record the contradiction and the reading kept in the [Analyst instruction audit](./analyst-instruction-audit.md).
- Except where the job cannot follow that type or rule from its inputs and its position in the run. Then the type or rule is the side in error, as with the epistemic type placing the Source register in the overview, which does not exist when the epistemic analyst runs. Record it in the audit as a correction to the type or rule; an obvious correction lands with the merge, anything else needs an operator decision.
- Where nothing settles it and the resolution needs an operator decision, record both readings and the decision needed in the audit, and keep the affected merged instruction as a workshop draft until the operator settles it. An unresolved conflict blocks promotion of that instruction; independent work may continue.

Do not put unresolved alternative requirements into an active job instruction or leave the analyst to choose between them. Contradictions found during the merge are added to the audit file.

### The invocation

The prompt file becomes the invocation. For example:

```text
Follow /home/zby/llm/commonplace/kb/instructions/analyse-agentic-system/jobs/memory.md with:
system = Instinctual Memory
round = first
run-state = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/run-state.md
boundary = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/boundary.md
runtime = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/output/runtime.md
output = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/memory-report-0.md
problem = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/memory-report-0.problem.md
scratch = /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-09-30-instinctual-memory-03/scratch/memory-0/

read-first:
- /home/zby/llm/commonplace/kb/instructions/analyse-agentic-system/jobs/worker-rules.md
- /home/zby/llm/commonplace/kb/instructions/analyse-agentic-system/jobs/judging-norms.md
- /home/zby/llm/commonplace/kb/types/agentic-system-analysis-overview.md
- /home/zby/llm/commonplace/kb/types/agent-memory-analysis-report.md
- /home/zby/llm/commonplace/kb/types/agentic-system-runtime-report.md
```

The worker receives that exact text as its launch message. Code supplies the system name rather than requiring an extra read solely to discover it.

The form is: the first line, then single-line `name = value` parameters, then the `read-first` block. The boundary job's invocation adds a `source` block holding the caller's input. That text is not code's, so code puts it inside a fence longer than any backtick run in its content; nothing in it can then be read as a parameter or an instruction line. On a retry the engine appends its existing section, `## Why the previous attempt was refused`, with the refusal messages.

### Workers run in the repository root

Every path in the invocation is absolute, including the main instruction's, so no read or write depends on the working directory. Two operations still do. `commonplace-validate`, which the memory analyst runs on its report, takes the repository root from the working directory. The boundary job uses the repository-relative `related-systems/` directory and runs `git check-ignore -q related-systems`.

Keep the working directory as it is today: the orchestrator runs in the repository root and its workers inherit that directory. State this as a precondition in the workflow's skill, which already tells the orchestrator where the run is. Do not make it a launch parameter: the Claude Code sub-agent launch takes no working directory, so a required one could not be applied and every launch would count as failed. Building an invocation must not depend on the directory from which the operator called `step`.

## Parameter design principle

Minimize symbolic work by the analyst, not the number of characters in the invocation. Code already knows which files a job consumes and where it must write. It should pass those results, rather than passing counters and asking the analyst to calculate filenames, join directories, replace extensions, select the latest report, or infer which reconciliation returned findings.

Round numbers remain scheduler state. Include one as descriptive metadata only if it helps the analysis; never make it necessary to locate an input or destination. Supply a resolved policy such as `may-return` directly instead of requiring comparison with a correction limit. State the kind of round as a value, so that the analyst does not infer it from which optional parameters are present. Code resolves every path the worker needs, fixed dependencies included.

## Parameters by job

Every job receives `system`, `run-state`, `output`, `problem`, and `scratch`. The path parameters name exact destinations or inputs, not templates. Additional parameters are:

| Job | Inputs and choices supplied by code |
|---|---|
| Boundary | Full `opening` path, normalized `source-identity`, the caller's input in the `source` block |
| Runtime | Full `boundary` path |
| Memory | `round` (`first` or `correction`); full `boundary` and `runtime` paths; for a correction, full `previous-memory`, `returned-findings`, and `epistemic` paths |
| Epistemic | Full `boundary` and `runtime` paths |
| Reconciliation | `round` (`first`, `after-correction`, or `after-blockers`); `may-return` (`yes` or `no`); full `boundary`, `runtime`, selected `memory`, and `epistemic` paths; full `previous-reconciliation` path in every round but the first; full `verification` and `set-check` paths after blockers |
| Verification | Full `overview-draft`, `runtime`, selected `memory`, `epistemic`, and `set-check` paths |

Each main instruction has, after its read-first rule, a table of its parameters: name, what it names or means, and when it is present (always, or the `round` value under which code supplies it), with allowed values for non-path parameters. Parameter names are vocabulary the worker must apply, so each is defined there once and used unchanged in the instruction's text. Preserve the caller's source input as data, including multiline input, without interpreting it as an instruction. Boundary cannot recover it from `opening.json`: that file currently holds publication metadata, not the caller's source input.

Memory and reconciliation counters can diverge: verification may cause another reconciliation without another memory analysis. Code selects the exact report paths using those counters. For memory corrections, `returned-findings` names the reconciliation that requested the correction. The analyst neither receives counters to reconstruct these paths nor lists the run directory to discover the intended inputs.

The instruction says what each `round` value requires: a memory `correction` answers the findings in `returned-findings`; a reconciliation `after-blockers` resolves the blockers in `verification` and `set-check`. Analysts must not reconstruct a missing parameter. Code builds the parameters itself, so a test on the constructor checks each job's combinations; no separate check runs at launch. Update shared worker rules to use the supplied `run-state`, `output`, `problem`, and `scratch` values directly.

Every job also accepts retry feedback when a previous attempt was refused: the engine appends the refusal messages to the retry's invocation, as it does to a generic prompt today. These are not analytical correction rounds: retrying the same job preserves its selected inputs and destinations unless workflow invalidation requires recomputation.

## Delivery: the orchestrator reads the prompt file

`step` continues to write `workflow-state/jobs/<job>/prompt.md` and print its path with the job's launch parameters. Its output does not change, and no prompt text passes through the command's output.

The orchestrator reads each named prompt file and launches one fresh worker whose whole message is the file's content, unchanged. This is a rule of the library, not of this workflow: update [drive a code-scheduled run](../../instructions/analyse-agentic-system/drive-a-code-scheduled-run.md), which every code-scheduled workflow's orchestrator follows. The generic prompts the engine renders are already complete messages, so other workflows need no other change.

The driver instruction then says:

- Read a prompt file only to deliver it. Do not prepend a read instruction, rewrite the text, add context, or act on what it says, including a retry's feedback.
- The existing rules stay: apply every launch parameter or report a failed launch, launch a round's jobs together, do not read outputs or problem reports, and do not do a job yourself.

In the worker rules, remove the exception that lets a worker read its prompt file; nothing under `workflow-state/` is then a worker's to read.

Accepted cost, by the operator's decision: the orchestrator is a model, and it copies the invocation with its absolute paths. The saved file records what code built; nothing records what the worker received. A miscopied destination leaves no output where code expects one, which the engine already treats as a failed attempt: it hands the job out again, and blocks it after two such attempts. A miscopied input path that names another existing file would not be detected.

## Engine change and dependency tracking

Keep all consumed instruction files, shared rules, and contracts declared as job dependencies. A shared-rule or contract change must still invalidate the affected job. The `read-first` list is generated from those declarations.

The generic renderer currently appends declared inputs, output paths, a reply rule, and refusal prose to the job's text. Add one flag to the job record: a job may declare that its prompt is the complete message. The engine then writes that prompt unchanged and appends only a retry's refusal section. The analysis workflow builds each invocation as its job's prompt and sets the flag; the reply rule the engine no longer appends is already in the worker rules. Construct path parameters from the same resolved job inputs and destinations the engine uses, rather than maintaining a second set of filename formulas in the prompt renderer. Keep the mechanism limited to the required message contract rather than adding a template framework.

The prompt is part of a job's input state, so the invocation's absolute paths enter it. That adds no new dependence on the checkout's location: declared method files are already keyed by absolute path.

As of 2026-09-30 the engine's only consumers are `AnalyseAgenticSystem` and the definitions in `tests/commonplace/workflow/definitions.py`, which keep the generic rendering.

Update `scripts/analyst_trial.py` to build its trial invocation through the same constructor as the workflow, so a trial's prompt file has the same shape and parameters as a real run's. Update the script's launch guidance: whoever launches the trial sends the content of `prompt.md` as the worker's message.

The trial script currently discovers files to hash by extracting input-list lines from rendered prompt text. Replace that extraction with the job's resolved declared file dependencies. Hash every declared file dependency into `trial.json`. A missing or unreadable dependency must fail trial preparation rather than silently disappear from the record; changing prompt formatting must not change dependency discovery.

Update publication's `METHOD_PATHS`, workflow fixtures, documentation composition tests, and links for the consolidated methods. Saving a path-based invocation alone does not preserve the referenced text: reproducibility still relies on the pinned method commit and tracked run inputs. Do not claim this is a complete snapshot of the worker's runtime context.

Relevant implementation points:

- [Analysis workflow](../../../src/commonplace/lib/agentic_workflow.py): job construction, dependencies, and round-specific inputs.
- [Workflow engine](../../../src/commonplace/workflow/engine.py): prompt rendering, saved prompts, and retries.
- [Driver instruction](../../instructions/analyse-agentic-system/drive-a-code-scheduled-run.md): the launch step.
- [Worker rules](../../instructions/analyse-agentic-system/jobs/worker-rules.md): references to the prompt's output, problem, scratch and run-state paths, and the prompt-file exception.
- [Publication checks](../../../src/commonplace/lib/agentic_publication.py): pinned method paths.
- Texts that describe the old launch or prompt: the `prompt` field's description in `src/commonplace/workflow/job.py`, `scripts/README.md`, the loop sketch in [code-scheduled workflows](../../reference/proposals/code-scheduled-workflows.md), and the prompt-prose assertions in `tests/commonplace/lib/test_agentic_workflow.py` and `tests/commonplace/workflow/test_workflow_orchestrator.py`.

## Order of work

Each step leaves a working system, so the work can stop after any of them.

1. **Delivery.** Change the driver instruction and the worker rules' prompt-file exception. The generic prompts are complete messages, so this works before anything else changes.
2. **Invocations.** Add the engine flag, build the invocations, and give the six job instructions their read-first rule and parameter table. Until a method file is merged it stays a declared dependency, so it appears under `read-first` and its wrapper still forwards to it.
3. **Merges.** Merge each method into its job instruction and retire the method file, one analyst per commit. A merge that waits on an operator decision delays only itself.
4. **Trial script.**

## Acceptance and verification

1. All six jobs use a single parameterized main instruction. Memory and epistemic startup no longer forwards through a wrapper to a separate method, and the merged instructions do not restate the shared worker rules.
2. `step`'s output is unchanged. The prompt file holds the invocation: first line, parameters, `read-first`, the `source` block for the boundary job, and the refusal section on a retry.
3. The driver instruction has the orchestrator send each prompt file's content as the worker's whole message. No worker needs to read a prompt file, and the worker rules grant no access to `workflow-state/`.
4. Tests exercise first rounds, memory corrections, verification-driven reconciliation with different memory and reconciliation counters, the last round's return prohibition, and validator retries.
5. Tests verify that fixed dependencies still invalidate affected jobs, that supplied paths equal the engine's selected inputs and destinations, and that each job's parameter combinations match its `round`. For each job and each correction or retry case, the declared file dependencies equal the main instruction, the `read-first` files, and the input-file parameters of its invocation; `run-state` and the destinations are outside that set. Every path in an invocation is absolute; no job instruction requires filename construction, relative-path resolution, extension replacement, round arithmetic, or latest-file discovery.
6. An invocation built from outside the repository root equals one built inside it. Generic workflow definitions, which do not set the flag, render as before.
7. A trial prepared with `scripts/analyst_trial.py` produces an invocation built by the workflow's constructor and records hashes of every declared file dependency without parsing the prompt.
8. Existing scripted workflow tests retain their publication and failure behavior. Update assertions about old generated prose to check the new invocation contract.
9. Before promoting each merged instruction, resolve its known contradictions with shared rules and report types. Operator decisions still needed remain in the audit and block promotion of that instruction; active instructions contain no unresolved alternative requirements.
10. Run the full required Python test suite and relevant KB validation after implementation. Record any lack of a real-worker trial explicitly; opening such a run requires a separate commission and a committed method.

This proposal is complete when the implementation and checks above are recorded, or when a discovered dependency requires returning a specific design choice to the operator. Preserve this proposal until its outcome is extracted when the workshop closes.
