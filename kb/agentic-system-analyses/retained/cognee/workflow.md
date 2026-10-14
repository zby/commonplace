---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Cognee workflow account: explicit agentic retrieval through skill loading, checked tool dispatch, recovery and answer delivery."
run-id: AAS-2026-10-14-cognee-d8839fe03c5b-01
reviewed-boundary: f154b32a9e544dac73e7ddf2010327cf9988edcd
---

# Cognee workflow report

## Workflow account

The selected workflow is an explicit agentic-completion request over one dataset. It is representative of Cognee's bounded model/tool coordination, not its default ingestion or recall behavior. Unlike a pipeline whose code fixes every task, this route lets a model select successive tools and decide when to answer. Its canonical container is [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools); recall entry and authorization belong to [RT-RTE-recall-dispatch](runtime.md#rt-rte-recall-dispatch). This is a source-supported possible progression, not a supplied execution trace. A request may finish without any tool call.

All findings use SRC-1 at the frozen commit. Added implementation inspection covers `cognee/modules/retrieval/agentic_retriever.py`, the agentic branch of `cognee/modules/search/methods/get_search_type_retriever_instance.py`, `cognee/modules/tools/execute_tool.py`, handler resolution in `cognee/modules/tools/registry.py`, `cognee/modules/tools/builtin/load_skill.py`, prompt assembly in `cognee/modules/retrieval/utils/completion.py`, and the inherited evidence-append method in `cognee/modules/retrieval/graph_completion_retriever.py`. The complete `cognee/infrastructure/llm/prompts/agentic_system.txt` supplies doctrine/design. No target or provider was executed. This does not extend the boundary to whole-system coverage.

### Request and prepared handoff

The caller explicitly selects `AGENTIC_COMPLETION` and can supply skills, a tool whitelist, prompt paths and an iteration bound. The factory does not silently activate this retriever because unrelated search configuration contains skill/tool keys. Construction requires a user and one explicit dataset. These are caller controls and code preconditions, not proof of human approval of subsequent actions (SRC-1, `cognee/modules/search/methods/get_search_type_retriever_instance.py`, `cognee/modules/retrieval/agentic_retriever.py`).

> if query_type is not SearchType.AGENTIC_COMPLETION and (has_skills or has_tools):
>     raise UnsupportedSearchTypeError(
>         "skills/tools are supported only with SearchType.AGENTIC_COMPLETION"
>     )
> --- `cognee/modules/search/methods/get_search_type_retriever_instance.py`

Code resolves skills and tools, obtains memory triplets when graph edges exist, and formats memory, a name/description skill catalog and a tool manifest. Caller filtering intersects ambient tools; with skills present, their declared-tool union further narrows that set, including `load_skill`. The manifest renders argument names, descriptions and required permissions, not the complete input schema. Dispatch passes argument dictionaries to handlers; this trace does not establish a universal schema validator. Memory retrieval details remain the supplied runtime baseline, not an exhaustive reinspection of every graph selector.

The prepared model handoff includes the question and formatted context, plus available session history and active guidance. Prompt assembly places history before rendered question/context and guidance last; the system template remains separate. These inputs are natural-language information/instructions interpreted by the model, while the action fields have fixed symbolic consumers. [RT-CMP-llm-gateway](runtime.md#rt-cmp-llm-gateway) bounds what is known about the external model. SRC-1, `cognee/modules/retrieval/utils/completion.py`:

> user_prompt = "\n\n".join(filter(None, (session.history, rendered, session.guidance)))
> return user_prompt, resolved_system_prompt
> --- `cognee/modules/retrieval/utils/completion.py`

### Model decision, skill loading and execution

At each turn the gateway returns [RT-OBJ-agent-step](runtime.md#rt-obj-agent-step). Code accepts a nonblank final answer first, even if a tool call is also populated. Otherwise it attempts the tool call; a step with neither usable answer nor tool call ends the iterative phase. The schema and this branch are action selection, not correctness verification.

A model can first request a relevant skill body. [WF-RTE-skill-loading](#wf-rte-skill-loading) establishes the precise handoff missing from the runtime's provisional procedure-delivery account. The handler selects only from the current active-skill map and marks the name opened. It returns a heading and procedure text, subject to two consecutive truncation points. Thus the request for a “full procedure” does not guarantee full delivery of a long procedure. Subsequent tool choice remains the model's responsibility; opening a skill does not execute its prose.

For a selected tool, code supplies user, dataset ID, tool name, arguments and the currently exposed tool names. Dispatcher scope rejection precedes lookup; dataset authorization uses the Tool's required permission before resolving and calling its Python handler. The handler receives arguments, authorized dataset, user and Tool. This is delegation to a callable, not launch of a separately isolated agent. The supplied [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools) retains the scope/ACL and in-process import evidence; those checks do not sandbox arbitrary handler effects.

### Rejection and recovery ownership

A name outside the manifest produces a scope rejection. Scope, permission and invocation failures caught by the safe wrapper become `ERROR:` text rather than immediately aborting the loop. That text is appended to model context; the model owns the next approach, while code owns remaining turns. The prompt requests an alternative rather than repetition, but the inspected loop does not enforce identical-call deduplication (SRC-1, `cognee/modules/retrieval/agentic_retriever.py`, `cognee/infrastructure/llm/prompts/agentic_system.txt`).

> except (ToolScopeError, ToolPermissionError, ToolInvocationError) as exc:
>     return f"ERROR: {exc}"
> --- `cognee/modules/retrieval/agentic_retriever.py`

> - A tool result beginning with `ERROR:` is a permission or invocation failure for that tool. Pick another approach; do not retry the same call with the same arguments.
> --- `cognee/infrastructure/llm/prompts/agentic_system.txt`

Other exception classes can escape. The outer completion wrapper then attempts failure-run recording for opened skills and re-raises; its `finally` resets the active/opened skill ContextVars. No blanket retry, effect rollback or answer delivery is established on that path. Storage of SkillRuns and session QA is best effort: helper exceptions are logged. Session-history/guidance lookup can also fall back to empty input. These fallback policies are not proof of successful durable recovery.

### Terminal delivery and retention

A nonblank model answer exits the tool loop. Exhausting the configured turns, or producing no actionable step, instead triggers one additional string-completion call over accumulated context with the inherited graph-completion templates. The bound therefore limits iterative turns, not total model requests, elapsed time or context tokens. A failure of this final call still escapes (SRC-1, `cognee/modules/retrieval/agentic_retriever.py`).

> # Budget exhausted — force a best-effort final answer from the accumulated context.
> forced: str = await generate_completion(
> --- `cognee/modules/retrieval/agentic_retriever.py`

After success, the wrapper resets skill frames, attempts SkillRun recording only for opened skills, attempts session QA storage, then returns the answer list. Ungraded success uses a neutral default score; caught loop failure supplies zero and error information. Those bookkeeping values do not compare the answer with a reference oracle. The QA write receives the original prepared context rather than the progressively extended loop context; retained SkillRun traces separately include tool arguments and at most 1,000 output characters per call, and result summaries retain at most 500 characters. Future session-history loading omits stored context. These are selective read-back channels, not full replay (SRC-1, `cognee/modules/retrieval/agentic_retriever.py`).

> tool_output=tool_result[:1000],
> success=not tool_result.startswith("ERROR:"),
> --- `cognee/modules/retrieval/agentic_retriever.py`

The final inherited `_append_graph_evidence` call is a no-op, despite the agentic call-site comment promising appended answer-grounded evidence. It returns the completions unchanged. This prevents treating that call as final answer validation or citation-based rejection; structured evidence in other search layers is not characterized here (SRC-1, `cognee/modules/retrieval/graph_completion_retriever.py`).

> async def _append_graph_evidence(self, completions: list[Any]) -> list[Any]:
>     """Compatibility no-op; graph evidence is now returned as structured payload data.
> --- `cognee/modules/retrieval/graph_completion_retriever.py`

Delivery at this inspected boundary means returning the answer list to the search caller, not proving host adoption, factual correctness or task success. There is no supplied expected-answer oracle or observed execution. Successful persistence, later use, reliable model adherence and benefit remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-skill-loading
Label: Progressive skill body loading

Part of: [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools)

This is the material handler subroute inside the supplied tool-loop container, not a duplicate of the complete retrieval workflow. It supplies the concrete body transformation underlying [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). Endpoints/progression: model tool request with skill name → dispatcher checks → active-skill lookup → opened-name mark → heading/body result → loop-context append → next completion. Code owns selection enforcement and truncation; the model chooses whether and which name to request. The procedure is natural-language guidance; the name/map/set are symbolic invocation-local state. No procedure update occurs. SRC-1, `cognee/modules/tools/builtin/load_skill.py`, `cognee/modules/retrieval/agentic_retriever.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A heading and procedure string, or invocation rejection for a missing or out-of-scope name; the safe wrapper can convert that rejection to error text.
- Later read-back: No content write in this handler; marking an opened name selects a later SkillRun write by the enclosing wrapper. Pre-existing procedure storage is not itself accumulated through this read.
- Delegated visibility: The next model call receives the returned string after the loop's additional output truncation; it does not necessarily receive the complete procedure.
- Selection predicate: Exact requested name in the current active-skill map, plus dispatcher tool scope and dataset permission checks.
- Invalidation or expiry: Active/opened maps reset when completion exits. Delivered text remains in this loop's accumulated context; no body eviction or summarization is shown in that loop.
- Activation or effect: Procedure text is appended to subsequent model input and the name is marked opened; content-dependent action change is unobserved.
- Evidence limits: This body loader and enclosing truncation inspected, not all skill resolution, stored procedures or executions; instruction delivery is not compliance or evidence of a formulated theory.

> body = skill.procedure or "(this skill has no procedure body)"
> if len(body) > MAX_SKILL_BODY_CHARS:
>     body = body[:MAX_SKILL_BODY_CHARS] + "\n... [truncated]"
> return f"# Skill: {skill.name}\n{body}"
> --- `cognee/modules/tools/builtin/load_skill.py`

> if len(tool_result) > MAX_TOOL_OUTPUT_CHARS:
>     tool_result = tool_result[:MAX_TOOL_OUTPUT_CHARS] + "\n... [truncated]"
> --- `cognee/modules/retrieval/agentic_retriever.py`

The loader's 12,000-character body cap precedes the loop's 8,000-character cap on the entire result, including its heading. Code keeps the truncated prefix; the unmodified procedure remains reachable through the active map, but another identical load still encounters the same caps. This is on-demand context supply, not a separate model frame. ContextVars isolate handler scope, not provider context or tool effects.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-agentic-tools](runtime.md#rt-rte-agentic-tools)

Workflow-specific acceptance and recovery: dispatch can reject an action, but final-answer acceptance is a nonblank-string branch rather than reference-answer comparison. The model selects alternatives after supported error classes become context; code bounds iterations and requests a final fallback. Caller tool filters can veto exposed capabilities, while no per-turn human approval is established. Operating mode is open question answering, not a comparative experiment. No rollback of prior tool effects follows from a later loop error. The workflow account above retains the additional failure, retention and terminal-call witnesses without changing this record's identity or implementation status.

#### On [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance)

Workflow-specific delivery limit: [WF-RTE-skill-loading](#wf-rte-skill-loading) establishes heading/body construction and both caps. Only the surviving text reaches the next model completion. The prompt requests loading relevant skills; neither that request nor opened-name tracking establishes complete procedure reception, obedience or changed actions.
