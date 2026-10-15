---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Prime Agent's bundled builder workflow: scope inspection, parallel section drafting, collector delivery and failure escalation."
run-id: AAS-2026-10-14-prime-agent-8ec59ae12476-01
reviewed-boundary: "33da15a2c15c4e903c372f69ae8e1156d77d53da"
---

# Prime Agent workflow report

## Workflow account

The bundled **builder** machine is selected because one shipped specification connects a working-tree request, parallel writers and a final report collector. This is not a workflow constructed by combining unrelated capabilities. Its implementation is a concrete part of [RT-RTE-factory-run](runtime.md#rt-rte-factory-run), traced below as [WF-RTE-builder-report](#wf-rte-builder-report). SRC-1 supplies implementation and doctrine/design, not an observed execution. No target code or tests were run. The account establishes orchestration and result-access paths, not a correct status report or successful recovery.

### Request and admission

The caller asks the foreground agent to build a status report, or directly calls the documented `await rlm.factory.run("builder")`. Factory use requires opt-in; the bundled skill tells the user to enable `/factory on`. Starting the workflow is not approval of each child's content. The public run function prefers a stored factory entry with that ID, otherwise resolves a library machine. This trace assumes the bundled builder file is selected, rather than a stored or alternate library definition with the same name. Library specs pass canonicalization and subagent resolution before launch; malformed specs or unresolved references are rejected before that launch. The run returns an ID and started/pending states while a background kernel task continues. [RT-RTE-factory-run](runtime.md#rt-rte-factory-run); [SRC-1: `skills/factory/SKILL.md`, `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`]

### Consequential handoffs

1. **Controller to scope child.** The machine supplies an inline prompt and name `builder-scope`. The prompt asks the child to inspect the working tree, count changes using `git status --porcelain`, read latest CI artifacts if present and return an `outline` JSON list with at most five lines. These are model instructions, not evidence that inspection happened or the counts are right. Each spawned child uses the independent loop described by [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn); shell/file effects follow [RT-RTE-python-effects](runtime.md#rt-rte-python-effects).
2. **Scope result to section writers.** The executor collects a settled child answer, prefers full `answer_text` over its preview, and caps each instance's binding text at 8,192 characters. The declared JSON port extracts `outline` from an object in the answer. Required binding waits for a settle and rejects missing or unparseable values. `foreach` additionally requires a list, takes at most eight items, and renders one writer prompt per item. The prompt substitutes the item for `{outline}`; it does not send the entire source child's working transcript. The run allows eight concurrent children. The five-line outline bound is requested by prose; the eight-item expansion bound is executable code. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`]
3. **Writer results to collector.** A writer entry completes after all its instances are done. The executor joins nonempty successful answers with two newlines in instance order and captures that string as `section`. The collector's required `sections` input binds from `notes.section`. Although its template does not contain `{sections}`, the renderer appends unused bound inputs under `## Inputs`; the collector therefore receives the joined drafts, not merely an instruction referring to absent text. It is asked to add `## Status`, preserve paragraph order and add `## Follow-ups`, returning final Markdown only. The controller does not independently verify these instructions were followed. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`]
4. **Collector to caller.** The collector's answer is captured as the text port `merged`. Controller completion is quiescence followed by finalization: no pending evaluations or ordinary pending/running work; entries with errors cause `failed`, otherwise the run becomes `done`. That verdict is workflow completion, not semantic acceptance. `status(run_id)` exposes the collector's latest answer only as a 200-character preview, despite the machine documentation calling it the merged text. Full result access requires collecting the collector child, whose ID appears in status instance rows. `rlm.collect` returns host-bounded `answer_text`; it preserves completed results until deletion and does not automatically steer the parent. Thus machine output capture, parent result inspection and delivery of a report to the user are separate steps. This inspected path does not establish automatic full-report delivery to the user. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/__init__.py`, `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`]

### Verification and rejection

The executor verifies spec/reference admissibility, child terminal status, state budget and port binding. It does not provide a reference answer for working-tree counts, CI interpretation, draft quality or report truth. The scope and collector instructions shape the proposed content; software checks its usable representation and progress, not its factual warrant. JSON extraction alone does not enforce the requested five-line limit or the truth of outline items. Empty outlines produce no writer instances, so this account does not infer a useful report from every valid JSON result. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`]

A supported rejection path starts when the scope child's answer has no usable `outline`. Capture re-collects settled children once to recover an answer-capture race. If the port still fails, the executor records `output_capture_failed`. The dependent writer's required input then fails deterministically instead of spawning on missing data; binding errors do not retry. Builder uses `failure_policy: escalate`, so the failed entry is marked error and the run pauses. Its unspecified child retries canonicalize to zero. A child error/cancellation similarly reaches the entry failure policy; a provisional exit answer remains marked `needs_verify`, not silently accepted as completed work. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`]

Recovery belongs to the caller supervising the run. Status supplies the last error and a remedy. `resume` restarts progression with a new loop generation, but does not redo a failed state; status explicitly directs the caller to fix the subagent and start a fresh run for that. Resuming the malformed-outline case does not create the missing outline or undo downstream errors. `stop` halts nonterminal work and cancels children; neither action promises rollback of shell/file effects. Kernel loss also loses the live factory registry, although daemon-owned children can survive, as bounded in [RT-RTE-factory-run](runtime.md#rt-rte-factory-run). These are recovery controls, not durable replay or demonstrated repair. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`]

Added coverage under SRC-1: full `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md` and `skills/factory/SKILL.md` (doctrine/design plus embedded symbolic spec); selected implementation ranges in `prime-agent-runtime/src/rlm/factory.py` covering rendering, library launch, status, binding, spawn, settlement, capture, failure policy and finalization; and `prime-agent-runtime/src/rlm/__init__.py` covering typed child results and collection. Other machines and every host-specific child-recovery branch were not inspected here; their omission prevents generalizing builder's delivery and failure behavior to all workflows.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-builder-report
Label: Builder status report

Part of: [RT-RTE-factory-run](runtime.md#rt-rte-factory-run)

This route is the bundled builder specialization, not a duplicate of the general factory controller. Endpoints: caller's library run request to scope child, foreach section writers, collector child and caller-side result inspection. Owner: FactoryExecutor decides readiness, binding and completion; child models produce content; caller decides whether to resume, stop, restart or present the result. Operating mode: bounded orchestration for an open status-report request, not an improvement experiment. The user enables the capability; software can reject admission or binding, while a caller can stop or decline the report. No independent expected-answer oracle is established. The proposed product is a Markdown report, not a retained change to Prime Agent's instructions or machinery.

- Immediate return: run handle with started/pending states; report production continues in a background kernel task, with status and child collection as separate calls.
- Later read-back: completed child results can be re-collected until deleted; factory status reads the live kernel registry. Cross-restart workflow replay is not established.
- Delegated visibility: scope gets its inspection prompt; each writer gets one outline item; collector gets the joined sections. Child working transcripts are not the machine's transfer payload.
- Selection predicate: builder resolves only after stored-entry lookup misses; canonical spec and references admit the run, required source ports gate dependents, foreach selects at most eight outline items.
- Invalidation or expiry: stop/deletion and parent/session lifecycle limit child results; kernel loss removes factory-run control state. Failed entries stay error on resume; redo requires a fresh run.
- Activation or effect: executable controller spawns children, binds selected answers and captures collector text; status delivers only a preview. User-visible full report delivery and report correctness remain unobserved.
- Evidence limits: SRC-1 code and shipped instructions only; no supplied run shows actual working-tree inspection, sound CI interpretation, successful merge or exercised recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

[SRC-1: `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`, `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/__init__.py`]

The shipped end-to-end contract is explicit:

> Builds a documented status report from parallel section writers. One source
> child inspects the working tree and produces a short outline, one writer
> child drafts a section per outline line (up to eight in parallel), and a
> collector child assembles the sections into a single markdown report.
> --- `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`

Bound inputs without template placeholders still reach the child:

> unplaced = [(name, value) for name, value in values.items() if name not in used]
> if unplaced:
>     rendered += "\n\n## Inputs\n" + "".join(f"- {name}: {value}\n" for name, value in unplaced)
> return rendered
> --- `prime-agent-runtime/src/rlm/factory.py`

The fan-out cap and ordered fan-in are code operations:

> for item in items[: foreach["max"]]:
> --- `prime-agent-runtime/src/rlm/factory.py`

> answers = [instance.answer for instance in entry.instances if instance.status == "done" and instance.answer]
> if not answers:
>     return None
> return "\n\n".join(answers)
> --- `prime-agent-runtime/src/rlm/factory.py`

Required binding distinguishes upstream failure from a value:

> elif src_output not in outputs:
>     failure = f"input {name!r} from state {src_id!r} has no captured output {src_output!r}"
> --- `prime-agent-runtime/src/rlm/factory.py`

Capture retries address delivery races, not factual correction:

> refreshed = await self._refresh_entry_answers(run, state, entry)
> if refreshed:
>     self._capture_ports(state, entry)
> --- `prime-agent-runtime/src/rlm/factory.py`

Escalation retains the error and pauses progression:

> else:  # escalate (default)
>     run.state = "paused"
>     run.pause_reason = reason
> --- `prime-agent-runtime/src/rlm/factory.py`

The remedy separates continuation from redo:

> "remaining states; the failed state stays error - fix its subagent and "
> "start a fresh run to redo it"
> --- `prime-agent-runtime/src/rlm/factory.py`

Completion does not validate report truth:

> run.state = "done"
> residents = [
> --- `prime-agent-runtime/src/rlm/factory.py`

Status previews do not deliver the whole binding result:

> # The report previews the settle answer compactly; the
> # full binding text stays on the entry.
> report["answer_preview"] = latest.answer[:ANSWER_CAPTURE_CAP]
> --- `prime-agent-runtime/src/rlm/factory.py`

Full child result access is distinct from that preview:

> `answer_text` is the child's full final answer (the settle-binding
> lane, host-bounded); `answer_preview` is the compact roster preview.
> --- `prime-agent-runtime/src/rlm/__init__.py`

> a timeout returns current snapshots, never an error, and the parent
> session is never steered. Completed children keep their result until
> deleted, so a later ``collect`` re-reads them without waiting.
> --- `prime-agent-runtime/src/rlm/__init__.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-factory-run](runtime.md#rt-rte-factory-run)

Workflow-specific delivery limit: the bundled builder's documentation directs callers to status, but that surface provides only an answer preview. Completion, complete output retrieval and user delivery are separate events. The builder-specific transfer and failure account is [WF-RTE-builder-report](#wf-rte-builder-report); it establishes no general semantic acceptance oracle for factory machines.
