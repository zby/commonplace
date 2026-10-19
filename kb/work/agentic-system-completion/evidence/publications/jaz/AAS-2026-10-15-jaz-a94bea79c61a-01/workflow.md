---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "JAZ workflow account: console helper delegation, typed proposal, human admission, retry and host delivery."
run-id: AAS-2026-10-15-jaz-a94bea79c61a-01
reviewed-boundary: 0803d4971be785e95b80054b02259664d70fa3da
---

# JAZ workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is a console `%` request for a JAZ-related action: the console delegates proposal generation to a restricted helper, checks its returned shape, shows the proposal to the operator, and executes only confirmed code in the console namespace. It was selected because one shipped caller connects request, agent work, rejection, recovery and delivery; no hypothetical application is needed. The same caller also delivers read-only answers without execution. This is the existing [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), not a new route. Its execution-authority endpoint is [RT-BAP-helper-proposal](runtime.md#rt-bap-helper-proposal).

All evidence is SRC-1 implementation at the frozen boundary. Additional inspection covered `src/jaz/console.py` (HelperHistory, helper restrictions and inputs, proposal generation, setup/turn-budget recovery and dispatch) and `src/jaz/hooks/builtin/return_hooks.py` (ReturnType completion checks). Inline contracts supply design intent, not observed operation. No target code was executed and no successful request, accepted proposal or recovered run is evidenced.

### Request and delegation

The operator supplies the request. `jaz_settings` obtains main/helper history from the supplied console namespace, accepting only the expected history classes and otherwise substituting no-history text. It passes transcript strings into `_propose_settings_response`; the helper does not receive the console namespace. The helper receives request text, generated API reference, a redacted current-configuration text snapshot, source root/file listing and these transcripts. SRC-1, `src/jaz/console.py`; see [RT-RTE-settings-change](runtime.md#rt-rte-settings-change).

The host delegates only response production. It installs PythonREPL with deny-all imports, package-tree reads, no writes and the configured default attribute policy, independent of the session's component selection. RecursionLimit makes this helper a leaf. The helper uses the ambient model configuration; the host supplies ReturnType and a three-iteration initial limit with a final-turn warning. These controls do not establish process isolation or successful containment under every trusted hook. SRC-1, `src/jaz/console.py`; the runtime's scoped guarantee qualifications remain applicable in [RT-RTE-hook-control](runtime.md#rt-rte-hook-control).

The task asks the model to consult configuration, reference or source as needed and return either `('answer', text)` for questions or `('code', snippet)` for actions. This is guidance, not a deterministic question/action classifier. The model decides which files to inspect and what Python to emit. The ordinary Agent loop schedules query, parse and execution, returning observations until native return/raise; see [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop). The console is the next-step owner after the helper returns. There is no second agent reviewer or task-correctness oracle on this selected path.

### Verification, rejection and recovery

ReturnType checks `tuple[Literal['code', 'answer'], str]`. A mistagged or wrongly typed native return can be converted into Continue feedback, allowing another model turn. The InvokeComplete backstop rejects a terminal mismatched Return not already checked. Neither check evaluates the snippet's meaning, security or adequacy for the requested action. SRC-1, `src/jaz/hooks/builtin/return_hooks.py`:

> result=Continue(
>     output=summarize_exception(error), exception=error
> )
> --- `src/jaz/hooks/builtin/return_hooks.py`

Turn exhaustion is a different failure from a completed but rejected proposal. The console catches IterationLimitExhaustedError and, in a TTY, offers fresh invocations with total caps of 10, 20 and 40 turns. Each retry receives the same request and captured conversation transcripts; it does not resume the failed helper's REPL or messages. Denial, no TTY or exhausted offers produces a rephrase hint and stops without a helper-history reply. A spent session budget stops without a turn offer. Source constants and branches, rather than any demonstrated rescue, establish these limits. SRC-1, `src/jaz/console.py`:

> budget, grant = grant, grant * 2
> grants_offered += 1
> --- `src/jaz/console.py`

An interactive missing-model/key check can offer deterministic setup before delegation. Authentication failure during delegation can offer setup once from its exception handler and then retry against the changed configuration. Other provider/configuration errors are not generally turned into this recovery path. The source's setup offer is not evidence that authentication or the requested action subsequently succeeds. SRC-1, `src/jaz/console.py`.

### Admission and delivery

After typed return, the caller strips fences only from code. An answer is recorded and printed verbatim, including outside a TTY; it is not executed. For code, the caller displays the snippet. Non-TTY input records it as unapplied and raises rather than silently continuing. In a TTY, only explicit `y` or `yes` admits execution; denial records an unapplied proposal and returns. The quoted human gate and host executor are already retained in [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), SRC-1, `src/jaz/console.py`.

Acceptance transfers the snippet from model-produced text to unsandboxed host Python in the live console namespace. This is not execution inside the restricted helper. The console records confirmation before `exec`, then prints a success marker only if `exec` returns. Thus the record's `applied=True` means admitted to execution, not verified completion or semantic success. If execution raises, partial host effects can remain; no automatic rollback is established. SRC-1, `src/jaz/console.py`:

> remember(applied=True)
> exec(compile(snippet, "<jaz-settings>", "exec"), namespace)
> print("✓ applied")
> --- `src/jaz/console.py`

Delivery therefore has distinct endpoints: printed text for an answer, displayed-but-unapplied code for a rejection, or completed host execution plus the success marker for an accepted action. A helper's returned tuple alone does not establish delivery of the requested state change. Whether a change persists beyond the session depends on the admitted snippet; generic confirmation does not imply a settings-file write.

Later helper requests receive rendered history of earlier resolved exchanges, with content abbreviated per entry. HelperHistory stores request, tag, content and admission flag, not a structured execution outcome. Its transcript labels accepted code “confirmed and run” even when the subsequent executor raised; that label cannot certify success. Failed proposal-generation attempts return before recording any reply. SRC-1, `src/jaz/console.py`:

> status = "confirmed and run" if exchange.applied else "shown, not run"
> lines.append(f"    proposed code ({status}): {content}")
> --- `src/jaz/console.py`

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

#### On [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)

Workflow handoffs: operator request → restricted helper with text snapshots and source-read access → tagged native tuple → console display/dispatch → human admission for code → live host executor. Host code owns scheduling and recovery; the model owns proposal content and response tag; the operator can veto execution and further turn spending. Open requests have no expected-answer oracle. Confirmation is an execution decision, not a correctness finding.

Recovery starts a fresh helper rather than continuing a suspended frame. Initial/renewed iteration caps are 3/10/20/40; session-budget exhaustion does not obtain more calls from these grants. Resolved exchanges can inform later helper requests, but their admission flag does not establish completed execution. These are workflow-specific qualifications to the existing route, not separate identities.

#### On [RT-RTE-hook-control](runtime.md#rt-rte-hook-control)

The selected caller uses ReturnType for response-shape admission, with recoverable per-turn mismatch feedback and a terminal completion backstop. It does not install a semantic snippet evaluator here. The runtime's hook-failure qualification continues to apply: a configured check is not an unconditional fail-closed guarantee.
