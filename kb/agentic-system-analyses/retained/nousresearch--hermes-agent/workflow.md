---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Hermes Agent workflow: finite one-shot delegated work, bounded output correction, result reduction and terminal delivery."
run-id: AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01
reviewed-boundary: "0e427d788d253630d38a3a51cd76849e73cd6925"
---

# Hermes Agent workflow report

## Workflow account

The selected workflow is a finite `hermes -z` request in which the foreground model delegates one or several subtasks and then produces its final answer. It is representative because it connects a shipped caller to child execution, an optional machine check, return to the foreground model and terminal delivery. It is a conditional implementation trace, not a supplied successful run: a request need not cause delegation or specify an output schema. The frozen [boundary](boundary.md) remains partial-loop inspection. No target execution or causal evidence is supplied.

### Request and handoff

[RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn) supplies the request-to-agent and final-answer-to-stdout endpoints. [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) supplies model-proposed call admission, conditional pre-effect transcript persistence and tool-result return. The foreground model chooses task goals and context; Hermes code schedules and bounds their execution. [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation) establishes child construction, separate identities and finite-session synchronous fallback. A top-level request for background work cannot detach results from this finite caller; the tool waits and returns the combined results with a fallback note (SRC-1 `tools/delegate_tool_dispatch.py`). This report does not extend that conclusion to background-capable clients.

The spawn handler can reject new work on operator pause, depth limit, malformed inputs, explicit routing failure or the one-shot cumulative child budget. Configuration, not a model-supplied iteration argument, owns the child cap. The inspected budget rejection directs the foreground model to continue inline; that direction is model guidance, not proof of recovery (SRC-1 `tools/delegate_tool.py`):

> f"Delegation budget for this one-shot run is exhausted ({spent}/{cap} subagents used; "
> f"delegation.oneshot_max_children). Do the remaining work yourself in this session — reviewing "
> f"your own diff and running the tests inline is expected here, not a delegated review."
> --- `tools/delegate_tool.py`

Each child receives selected goal/context and an optional output contract, resolved tools and model route, rather than the parent's live conversation. Construction skips context files and memory, can inherit prefill messages, links a separate child session to the parent and gives it a fresh iteration budget. Depth/configuration determine whether it may delegate further. These are context and scheduling boundaries, not filesystem confinement; inherited tools can produce consequential effects (SRC-1 `tools/delegate_tool.py`; [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)). The handoff does not establish human authorship or review of the proposed task/context.

### Child execution and verification

The child runs its own conversation/tool loop. Single children run through the child runner; multiple children use daemon-worker futures, with results sorted back into input task order. The attached parallel path polls for parent interruption, fabricates interrupted entries for unfinished children and shuts down without waiting on those workers. That prevents waiting for every pending worker at this join; it does not roll back already executed tools or prove that an uninterruptible external action stopped (SRC-1 `tools/delegate_tool_dispatch.py`).

Optional verification is [WF-RTE-output-contract](#wf-rte-output-contract). It checks an extracted JSON value against a supplied schema and can send one correction turn to the same child. It does not check factual truth or task success. If the second answer still violates the schema, the parent receives raw text with an explicit failed-contract verdict. In particular, `status=completed` does not imply schema validity, budget-complete execution or a correct answer. Provider/runtime failure fields take precedence over mere presence of final text; a budget-exhausted child can still have `status=completed` but `exit_reason=max_iterations` and `truncated=true` (SRC-1 `tools/delegate_tool_child_run.py`).

### Join, recovery and delivery

The child runner packages summary, status, exit reason, token/cost metadata and a reduced tool trace, then performs cleanup in a `finally` path. The aggregate finalizer budgets summaries, notifies the memory manager, fires stop hooks and rolls up cost. The synchronous aggregator then finalizes live transcripts, updates manifest statuses and returns JSON results. Those additional notifications are inspected calls, not established retained-content updates; their downstream persistence/consumption is outside this workflow trace (SRC-1 `tools/delegate_tool.py`, `tools/delegate_tool_dispatch.py`, `tools/delegate_tool_results.py`).

[WF-RTE-summary-return](#wf-rte-summary-return) is the consequential return transformation: an oversized answer becomes head and tail plus a file pointer when spill succeeds. The foreground does not automatically receive the full child transcript or full over-budget answer. It must elect to read omitted content. The structure resembles a context frame: selected inputs enter a separate window and a reduced result escapes. The analogy fails at durable sessions, spill files and external effects, which outlive that window.

There is no deterministic requirement at this join to reject an invalid schema result, rerun failed subtasks or independently test the child product. Recovery after reported failure or unvalidated output remains a foreground-model decision within its remaining budget; the one bounded schema correction is the explicit automatic repair here. The parent can call more tools or finalize. Finalization and the one-shot caller then return/print the final response as described by [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn). Terminal delivery means the selected caller prints the agent's final text, not that a child product passed a semantic acceptance gate. Successful printing, tool effects, cleanup and the benefit of delegation remain unobserved.

Added SRC-1 implementation coverage: child building/admission and runner sequence in `tools/delegate_tool.py`; schema retry and result-entry construction in `tools/delegate_tool_child_run.py`; JSON extraction/checking in `tools/delegation_output_schema.py`; synchronous join, interrupt handling, aggregation and fallback in `tools/delegate_tool_dispatch.py`; summary budgeting/spill and finalizer calls in `tools/delegate_tool_results.py`. Inspection remains selective: full timeout diagnostics, worktree setup, live-log retention, async completion consumers and downstream memory writes are not established by this trace. Source comments about previous runs are not used as observed execution evidence.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-output-contract
Label: Child output contract checking

Part of: [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

This is the optional schema-check/correction portion of the supplied delegation route, not another child scheduler. SRC-1 `tools/delegate_tool.py` appends the contract to selected context and attaches the schema to the child. SRC-1 `tools/delegation_output_schema.py` and `tools/delegate_tool_child_run.py` implement checking, one retry and result annotation. Natural-language contract/retry instructions guide the child model; symbolic JSON/schema validation determines the structural verdict. State is the child schema and result dictionary in process, with ordinary child session persistence conditional on its store.

The foreground caller proposes the schema; code can refuse a malformed schema before spawn. Schema-check code decides the output verdict; the child model proposes a repair. No per-output human approval is wired in this checker. This is open task execution with a structural reference, not a factual answer oracle or an improvement experiment. Parsing strips fences and can extract outer object/array spans, so validation does not enforce the prose instruction's literal JSON-only presentation. If `jsonschema` is unavailable, parsed JSON is accepted without schema validation. Rejection changes the verdict and prompts repair, but does not veto delivery after retry. No external tool-effect rollback is provided by this checker.

- Immediate return: Schema-valid flag and errors, retry count when used, and a note identifying usable but unvalidated final text.
- Later read-back: uninspected — later session reuse of these particular verdicts is not traced; current aggregation receives them immediately.
- Delegated visibility: The child receives the initial schema contract and up to one retry prompt containing validation errors; the parent receives verdict metadata and final text, not the validator's full internal state.
- Selection predicate: An attached dictionary schema; nonempty, noninterrupted invalid first output triggers correction. No schema takes no correction branch.
- Invalidation or expiry: At most one retry per checked result; retry exceptions are logged, preserving the original result and failed verdict. Further repair is left to the foreground.
- Activation or effect: Wired structural checking and possible additional child inference/tool turn; model compliance and successful correction are unobserved.
- Evidence limits: Optional dependency degradation, permissive extraction and schema expressiveness bound the verdict. Even schema-valid output is not evidence of task correctness; post-check summary trimming can alter the text returned to the parent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> except ImportError:
>     logger.debug("jsonschema unavailable; accepting parsed JSON without validation")
>     return True, []
> --- `tools/delegation_output_schema.py`

> if _schema_valid or not _first_text.strip() or result.get("interrupted", False):
>     return _SchemaOutcome(_output_schema, _schema_valid, _schema_errors, 0)
> --- `tools/delegate_tool_child_run.py`

> "Final answer does not satisfy the declared output_schema"
> + (" (after 1 retry)" if schema.retries else "")
> + "; `summary` is the child's raw, UNVALIDATED final text — extract what you need from it "
> "yourself (see schema_errors) rather than re-running the task."
> --- `tools/delegate_tool_child_run.py`

#### WF-RTE-summary-return
Label: Child summary return reduction

Part of: [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

This is the return-side summary transformation inside the supplied delegation route. It is distinct from its optional checker above: schema validation happens before host-owned summary reduction. SRC-1 `tools/delegate_tool_results.py` computes a per-summary cap from the smaller available positive static ceiling and dynamic headroom budget. The default static ceiling is 24,000 characters; dynamic budget uses half remaining token headroom divided across nonempty summaries, approximately four characters per token, with a 2,000-character floor. Unknown usage falls back to the static ceiling. Both disabled/unknown leaves summaries untouched. This is a sizing heuristic, not a proven overflow-prevention invariant.

Code owns selection and trimming. The child supplies natural-language or JSON-text final output; fixed slicing/spill rules produce a model-visible head/tail/footer and optional pointer. Process dictionaries hold the reduced result; cache files hold full spilled text when writing succeeds. The parent model decides whether to page omitted content. The route does not admit a revised product or certify its meaning; it changes delivery representation. Read-back may restore omitted material for a later model request, but is not automatic.

- Immediate return: A replaced summary, summary_truncated flag and optional summary_full_path, subsequently serialized into the combined tool result.
- Later read-back: On successful spill, the full answer remains in a cache file and the footer instructs the parent to page it with read_file; actual reload and cache expiry are not established here.
- Delegated visibility: Parent receives approximately 75 percent head and 25 percent tail of the cap, snapped to line boundaries, plus a footer; the middle remains outside its model window unless requested.
- Selection predicate: Nonempty string summaries longer than the computed cap; static configuration and parent prompt/headroom measurements select size, not semantic relevance.
- Invalidation or expiry: Spill failure still returns the trimmed answer, explicitly warning that full output could not be stored. Cache retention/pruning lifecycle is uninspected.
- Activation or effect: Wired text reduction and best-effort full-text file creation; actual parent reads, interpretation and downstream behavior are unobserved.
- Evidence limits: Returned text can cease to be valid JSON after a successful schema check, and the retained schema flag is not recomputed here. Spill availability depends on storage/backend path access; reduced output is not a complete child-work record.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> model_text, spill_path = _trim_summary_with_footer(summary, cap, entry.get("task_index", -1))
> entry["summary"] = model_text
> entry["summary_truncated"] = True
> if spill_path:
>     entry["summary_full_path"] = spill_path
> --- `tools/delegate_tool_results.py`

> footer_lines.append("Full output could not be stored to disk; the head+tail above is all that was preserved.")
> --- `tools/delegate_tool_results.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

Workflow role: the finite caller's delegation is a joined subtask stage, not delivery of the operator's final answer. The foreground retains the decision to act on failures, use returned unvalidated material or reload spilled text before answering. Optional checking and return reduction are sequential but have different acceptance meanings; a pre-reduction structural verdict is not a certificate for the eventual model-visible summary. Successful operator delivery and semantic acceptance remain separate, unobserved conclusions.
