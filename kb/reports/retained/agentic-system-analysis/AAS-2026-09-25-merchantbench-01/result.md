---
type: kb/types/agentic-system-analysis-result.md
description: 'MerchantBench ReAct subsystem: action-feedback loop, optional trace-derived
  scratchpad and guarded protocol with source/default and context-maintenance limits'
run-id: AAS-2026-09-25-merchantbench-01
system: MerchantBench
run-date: '2026-09-25'
result-disposition: complete
target-class: runtime client
boundary-kind: subsystem-only
reviewed-boundary: f44ce969aeccfd65d1eef6afe50f69868e510946
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: known
      basis: afforded
      note: Dialogue and scratchpad advise; maintenance notices instruct; metadata
        enforces replay/admission and routes observation/history selection; optional
        trace-derived notes afford later behavioral guidance.
      records:
      - BAP-1
      - BAP-2
      - RTE-7
      - RTE-8
      values:
      - knowledge
      - instruction
      - enforcement
      - routing
      - learning
    curation_operations:
      assessment: known
      basis: afforded
      note: History removal/redaction and LRU eviction forget retained material; scratchpad
        overwrite affords revising its contents. No semantic deduplication or synthesis
        procedure is established.
      records:
      - RTE-3
      - RTE-4
      - RTE-6
      - RTE-7
      values:
      - decay
      - evolve
    distilled_form:
      assessment: known
      basis: afforded
      note: The qualifying afforded route is concise Markdown notes, strategy, decisions
        and open follow-ups. Protocol wrappers are not the distilled content.
      records:
      - RTE-8
      values:
      - natural-language
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      note: No retained execution evidence was commissioned or supplied. Source/mock-test
        inspection cannot establish dependence on recalled content; no global claim
        about uninspected experiments.
      records:
      - RTE-8
      values: []
    learning_scope:
      assessment: known
      basis: afforded
      note: Continuation of one merchant operating run, including its strategy and
        unfinished decisions; run-local path and unchanged task loop establish horizon.
        No cross-run import.
      records:
      - RTE-8
      values:
      - per-task
    learning_timing:
      assessment: known
      basis: afforded
      note: Optional note generation and retrieval occur during the same action loop.
      records:
      - RTE-8
      values:
      - online
    lineage:
      assessment: known
      basis: afforded
      note: Model-authored messages, imported observations/tool results, deterministic
        notices/metadata, and afforded trace-derived scratchpad content. Last branch
        is conditional.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - RTE-3
      - RTE-8
      values:
      - authored
      - imported
      - other-compiled
      - trace-extracted
    read_back_direction:
      assessment: known
      basis: wired
      note: Harness automatically supplies bounded history; model requests its current
        scratchpad; protocol consumers request cursor/cache records.
      records:
      - RTE-2
      - RTE-6
      - RTE-7
      values:
      - pull
      - push
    read_back_signal:
      assessment: known
      basis: wired
      note: Model history push selects a recent suffix under a budget. No identifier-targeted
        history branch or query-based semantic selector. Requested keyed reads are
        pull.
      records:
      - RTE-2
      - RTE-3
      values:
      - coarse
    representational_form:
      assessment: known
      basis: wired
      note: Readable dialogue/scratchpad plus protocol calls, JSON records and machine-consumed
        control metadata. No scoped weights or opaque learned payload.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-5
      values:
      - natural-language
      - symbolic
    storage_substrate:
      assessment: known
      basis: wired
      note: Python history/control state and run-local Markdown/JSON files; simulator
        databases and provider caches excluded.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-5
      values:
      - files
      - in-memory
    trace_learning:
      assessment: known
      basis: afforded
      note: Enabled memory tools afford automatic trace-context-to-Markdown-to-later-model
        guidance. No mandatory summary/write/read, execution or benefit demonstrated.
        Disabled-tools branch has no qualifying derived route.
      records:
      - RTE-8
      values:
      - 'yes'
    trace_source:
      assessment: known
      basis: afforded
      note: The qualifying optional note route receives in-process conversation and
        tool-result history, not persisted environment trace files.
      records:
      - RTE-8
      values:
      - session-logs
      - tool-traces
    write_agency:
      assessment: known
      basis: wired
      note: Baseline/model/tool and server writes are automatic. No human scratchpad
        editor or approval route is wired in this subsystem.
      records:
      - RTE-2
      - RTE-3
      - RTE-6
      - RTE-7
      values:
      - automatic
  scope: ReAct baseline retained dialogue and control metadata, optional current-run
    scratchpad and history, environment trace/usage records and consumed protocol
    cursors/idempotency; both tool-enabled and tool-denied branches. Excludes simulator
    domain databases and provider internals.
---

# MerchantBench ReAct runtime and environment interface

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-merchantbench-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/merchantbench.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-merchantbench-01/memory-report.md`

**Memory analysis report SHA-256:** 59893535acfe7179e420f3708a4044ee48e33cbad077bfe56e4a3a965e0f77e4

## Boundary and evidence

Target class: runtime client. Boundary kind: subsystem-only. Includes the reference ReAct 160k-to-30k baseline, its public SDK and consumed server admission/observation/memory-document/trace interfaces. Excludes other agents (rule-based, auto-seed, Hermes and third-party submissions), market-demand/pricing/order simulator algorithms, private data, Docker/batch/evaluation orchestration, UI/leaderboard and provider internals. Scoring source supplies only the objective definition, not empirical agent results or a new runtime route.

Evidence: code-grounded, commit f44ce969aeccfd65d1eef6afe50f69868e510946, inspected 2026-09-25. Sole allowlist https://github.com/KhanCold/merchantbench via commit-addressed Git at `/home/zby/llm/commonplace/related-systems/KhanCold--merchantbench`. No worktree, previous review, ingest or retained analysis evidence. No target command, model call, dependency installation or benchmark execution. Simulated observations are implementation interfaces, not real-market evidence.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | https://github.com/KhanCold/merchantbench | f44ce969aeccfd65d1eef6afe50f69868e510946 | implementation | ReAct/SDK and consumed API/control/memory paths; scoring definition | `agent/baselines/react_160k_compact_30k.py`; `agent/sdk/merchantbench_tool_client.py`; `env/web/routes_agent.py`; `env/web/auth.py`; `env/web/app.py`; `env/tools/dispatch.py`; `env/tools/tools.py:2161-2237`; `env/tools/registry.py:501-524`; `env/core/simulator.py:1357-1503`; `eval/scoring.py:20-76`; `env/storage/agent_log.py`; `env/tools/observation.py`; `tests/test_memory_doc_tools.py`; `tests/test_react_160k_compact_30k.py` | model/provider internals, actual deployment, simulator mechanics and benchmark executions excluded |
| SRC-2 | Git | https://github.com/KhanCold/merchantbench | f44ce969aeccfd65d1eef6afe50f69868e510946 | doctrine/design | agent README, scenario defaults, prompts/comments | `agent/README.md:51-147`; `env/scenarios/default.yaml:190-203`; baseline context-maintenance strings | documentation/default conflict retained below; no claims become observed outcomes |

## Shared records

### Components

CMP-1 — Python ReActAgent: symbolically bounded per-step loop, mutable history/context bookkeeping and provider-error recovery. Source-wired. It chooses model requests, passes actions to the environment and consumes results; it does not simulate market physics. SRC-1 `agent/baselines/react_160k_compact_30k.py:332-360,564-796`.

CMP-2 — OpenAI-compatible model resolved through CLI/environment, default qwen3.5-27b. Source-wired model selection; exact weights/provider changes uninspected. Temperature omitted unless configured; timeout120 seconds. Claude name heuristic changes prompt/cache protocol. No parameter-training path occurs in the inspected requests; exact parameter fixity cannot be inferred. SRC-1 `agent/baselines/react_160k_compact_30k.py:188-229,582-607,799-812,842-879`.

CMP-3 — SDK/server admission interface. SDK caches tool schemas and sends bearer token when configured; server filters schema and calls through registered handlers. Effects occur in environment process under its grants; simulator internals and deployment isolation excluded. Source-wired. SRC-1 `agent/sdk/merchantbench_tool_client.py:34-98,153-201`; `env/web/routes_agent.py:643-679,902-1135`; `env/tools/dispatch.py:114-177`.

### Operative objects

OBJ-1 — Baseline Python `history`, raw observation text, assistant content and optional reasoning content, tool-call syntax and returned tool content, plus token/compaction/retry metadata. Storage is in-memory; form is natural-language with symbolic message/call structure. Observations and results are imported, assistant content is model-authored, and notices are deterministically compiled. History is advisory evidence and maintenance notices are user-role instructions; metadata controls selection and recovery. No baseline restart loader is present in initialization or run lifecycle. SRC-1 `agent/baselines/react_160k_compact_30k.py:332-360,393-431,483-562,564-607,759-796`. Implementation conclusion status: wired.

>     def _append_tool_results(self, act_resp: dict) -> None:
>         for tr in act_resp.get("tool_results", []):
>             self.history.append({
>                 "role": "tool",
>                 "tool_call_id": tr["tool_call_id"],
>                 "name": tr["name"],
>                 "content": tr["content"],
>             })
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

>     def _remember_act(self, assistant_msg: dict, act_resp: dict) -> None:
>         if _is_only_end_of_step(assistant_msg):
>             content = assistant_msg.get("content") or ""
>             if content and not content.startswith("[llm-error]"):
>                 history_msg = {"role": "assistant", "content": content}
>                 if assistant_msg.get("reasoning_content"):
>                     history_msg["reasoning_content"] = assistant_msg["reasoning_content"]
>                 self.history.append(history_msg)
>             return
>         self.history.append(assistant_msg)
>         self._append_tool_results(act_resp)
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

OBJ-2 — Current Markdown scratchpad and append-only version-history Markdown files under the run and sanitized agent ID. The model produces the current content; writes replace the complete document and append a new version with step/time/byte metadata. UTF-8 content above 256 KiB is rejected before overwrite. There is no schema for claims, reasons, provenance or confidence inside Markdown. The current document is advisory context, not an executable instruction registry or an enforced policy. All appended versions remain on disk within this boundary; no version restoration, pruning or history-read tool was found in these functions. SRC-1 `env/tools/tools.py:2161-2227`. Implementation conclusion status: wired.

> def read_memory_doc(env: Environment, agent_id: str) -> dict:
>     """Read this agent's Markdown scratchpad for the current run."""
>     path = _memory_doc_path(env, agent_id)
>     if not os.path.exists(path):
>         return {"ok": True, "content": "", "bytes": 0}
>     with open(path, "r", encoding="utf-8") as f:
>         content = f.read()
>     return {"ok": True, "content": content,
>             "bytes": len(content.encode("utf-8"))}
> --- `env/tools/tools.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

> def write_memory_doc(env: Environment, agent_id: str, content: str) -> dict:
>     """Overwrite this agent's Markdown scratchpad for the current run."""
>     if not isinstance(content, str):
>         content = str(content)
>     size = len(content.encode("utf-8"))
>     if size > _MEMORY_DOC_MAX_BYTES:
>         return {"ok": False,
>                 "error": f"content too large ({size} bytes, max {_MEMORY_DOC_MAX_BYTES})"}
> --- `env/tools/tools.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

OBJ-3 — Server trace messages and turn metadata, including reported usage/context counts, are copied to per-step JSON files and runtime-event JSONL. These are raw records and numeric aggregates, not synthesized agent knowledge. They retain more than the client prompt: an end-of-step tool event can remain server-side even when the baseline omits it from local history. SRC-1 `env/web/routes_agent.py:907-925,1090-1123`, `env/core/simulator.py:1357-1441`, `env/storage/agent_log.py:137-157,215-258,303-306`. The commissioned client has no trace retrieval call in its action loop. Implementation conclusion status: wired.

>     path = os.path.join(base, "by_step", f"t_{t:05d}.json")
>     payload = {
>         "t": t, "n_turns": len(turns_meta),
>         "hook_open_wall_ms": hook_open_wall_ms,
>         "hook_close_wall_ms": 0,
>         "messages": messages,
>         "message_agents": message_agents or [None] * len(messages),
>         "turns": turns_meta,
>     }
>     _atomic_write_json(path, payload)
> --- `env/storage/agent_log.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

OBJ-4 — Initial scenario brief and tool schemas are static doctrine/contracts. Their baseline cache and schema hash identify the available interface; they are not trace-derived memory. The first brief is adopted only while `system_prompt` is unset. SRC-1 `agent/baselines/react_160k_compact_30k.py:393-399`, `agent/sdk/merchantbench_tool_client.py:64-77`; SRC-2 `env/scenarios/default.yaml:190-199`. Excluded from accumulated-memory profile except their role in authorizing and directing the documented routes. Implementation conclusion status: wired.



OBJ-5 — consumed protocol-state records, distinct from model narrative memory. This groups per-agent observation cursor/window and current observation cache, latest step, and per-run LRU idempotency entries with fingerprints/cached results. Storage is Python dictionaries/ordered dictionaries plus `observation_state.json` and `idem_cache.json`; not a separate KV service. Content is symbolic selection/enforcement metadata with cached response payloads. It is automatically acquired/updated through protocol use; it does not derive new strategic claims. SRC-1 `env/core/simulator.py:118-149`, `env/tools/observation.py:700-729,1094-1146`, `env/storage/agent_log.py:693-784`.



### Routes

RTE-1 — Construction, registration and observation. Caller chooses run/agent/baseURL/model; SDK obtains schema and optional token, baseline registers runtime metadata then long-polls observation. First received brief sets its system prompt. SDK records raw tick.step when present; baseline computes its stop horizon from day/hour. HTTP410 returns cleanly; max_steps compares elapsed day/hour, not simply count of invocations. SDK retries408/read timeouts; bounded connection errors can propagate. Conclusion status: wired. SRC-1 `agent/sdk/merchantbench_tool_client.py:34-146`; `agent/baselines/react_160k_compact_30k.py:362-399,759-785`; `env/web/routes_agent.py:613-752`.

SDK fetches schema, registers, long-polls observations and stores the latest step. The server supplies the first brief and records observed text; the baseline loops on observations until HTTP 410 or its step ceiling. This defines continuation of one merchant operating task, not cross-task memory. SRC-1 `agent/sdk/merchantbench_tool_client.py:35-146`, `env/web/routes_agent.py:613-752`, `agent/baselines/react_160k_compact_30k.py:759-796`. Implementation conclusion status: wired.



RTE-2 — Ordinary step/hop. Append observation as user text, possibly maintain context, build messages and current tool schema, call model with tool_choice auto. Submit assistant calls through /act, append returned tool results and continue until step_done. A response without tool calls becomes a synthetic end_of_step call; hop-budget exhaustion also forces release. No internal human approval sits between proposed action and submission. Conclusion status: wired. SRC-1 `agent/baselines/react_160k_compact_30k.py:564-734`.

>                 request = {
>                     "model": self.model,
>                     "messages": llm_messages,
>                     "tools": tools,
>                     "tool_choice": "auto",
>                     "extra_headers": {
>                         "x-idealab-session-id": self.run_id,
>                     },
>                 }
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

Model/provider details and usage can be retained, but no local criticism or truth predicate evaluates free-form reasoning before actions. Invalid tool arguments remain structured error material for the next hop; provider output handling is not task-success verification.

Each hop appends or uses the latest observation and retained history, trims the outgoing suffix and supplies it to the model alongside tools. Successful actions append assistant and tool messages. A pure end-of-step action retains only nonempty assistant content, except `[llm-error]` content, and optional reasoning; tool calls/results for that special case are omitted. No-tool responses and exhausted hops force end-of-step. SRC-1 `agent/baselines/react_160k_compact_30k.py:175-185,401-420,564-734`. Producer: baseline and model. Persistence: OBJ-1. Later consumer: the next model invocation. Implementation conclusion status: wired.

> def _build_llm_messages(system_prompt: Optional[str], history: list[dict],
>                         max_history_tokens: int,
>                         *, exclude_system: bool = False) -> list[dict]:
>     messages: list[dict] = []
>     if system_prompt and not exclude_system:
>         messages.append({"role": "system", "content": system_prompt})
>     messages.extend(
>         _sanitize_message_for_llm(msg)
>         for msg in _trim_messages_to_token_budget(history, max_history_tokens)
>     )
>     return messages
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

RTE-3 — Context maintenance. The threshold uses latest provider prompt usage when positive, otherwise a character heuristic. With write_memory_doc exposed, a user-role reminder invites a write before trimming after successful /act. Without the tool, trimming and a notice occur immediately. Successful /act causes pending compaction regardless of whether a memory write happened or succeeded; there is no summary-model call here. Source-wired transformation/selection; full memory classification delegated below. SRC-1 `agent/baselines/react_160k_compact_30k.py:76-120,315-329,483-539`.

>     def _compact_history_if_pending(self) -> None:
>         if not self.compaction_pending:
>             return
>         self.history = _trim_messages_to_token_budget(
>             self.history,
>             self.compact_keep_tokens,
>         )
>         self.last_prompt_tokens = 0
>         self.compaction_pending = False
>         self._pending_pre_assistant_messages = []
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

The trim helper always retains the newest message even if it alone exceeds the budget, then removes leading tool messages. Tool schemas/system material and this heuristic prevent a strict model-context token invariant. Complete tool-call pairing is not verified by the leading-tool removal rule. These are static bounds, not measured overflow or provider errors.

Context maintenance reads positive last-provider prompt usage, falling back to the heuristic only when that value is unavailable/nonpositive. It checks before the next hop, uses schema presence of `write_memory_doc` as its branch selector and marks context maintenance pending. Reminder/notice is also sent with the action for tracing. Trimming clears usage/pending state after a successful action; the metadata flag `compacted` is reported while pending, so it is not evidence of a successful memory write. SRC-1 `agent/baselines/react_160k_compact_30k.py:483-562,620-635,670-718`. Implementation conclusion status: wired.

>     for msg in reversed(messages):
>         cost = _message_token_estimate(msg)
>         if kept_reversed and total + cost > max_tokens:
>             break
>         kept_reversed.append(msg)
>         total += cost
>         if total >= max_tokens:
>             break
>     kept = list(reversed(kept_reversed))
>     while kept and kept[0].get("role") == "tool":
>         kept.pop(0)
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

> def _compaction_reminder(trigger_tokens: int, keep_tokens: int) -> str:
>     return (
>         "[context-maintenance]\n"
>         f"Conversation reached the {trigger_tokens:,}-token limit. "
>         f"After this turn, history will be compacted to the latest ~{keep_tokens:,} estimated tokens. "
>         "Call write_memory_doc now if important details should be kept."
>     )
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

>             self._remember_act(assistant_msg, act_resp)
>             self._compact_history_if_pending()
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

>         last_prompt_tokens = int(getattr(self, "last_prompt_tokens", 0) or 0)
>         trigger_tokens = (
>             last_prompt_tokens
>             if last_prompt_tokens > 0
>             else _history_token_estimate(self.history)
>         )
>         if trigger_tokens < self.compact_trigger_tokens:
>             return
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

RTE-4 — Recovery. Provider errors map to bounded retry schedules; Forbidden gets one special retry after replacing the last contiguous tool-result group with a policy-redaction message. This changes future prompt evidence without establishing that the removed text was false. Retry exhaustion/no-retry class forces end_of_step. A stale425 during normal act truncates local history to the saved pre-observation length; already committed environment effects from earlier hops are not rolled back by slicing this list. Force-end failure resets pending compaction metadata. Source-wired best effort, no exactly-once whole-turn guarantee. SRC-1 `agent/baselines/react_160k_compact_30k.py:58-73,422-481,656-672,702-718,736-757`.

>                 status = getattr(getattr(e, "response", None), "status_code", None)
>                 if status == 425:
>                     # Stale step: env already advanced. Discard this turn's
>                     # messages (observation + any hops) to prevent accumulation
>                     # of duplicate observations on re-observe.
>                     self.history = self.history[:history_len_before]
>                 else:
>                     self._force_end_of_step(
>                         f"[act-error] {type(e).__name__}: {e}"
>                     )
>                 return
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

One Forbidden retry replaces the most recent contiguous group of tool-result contents with a reason/hint placeholder and rebuilds the request. It preserves other messages and identifiers; it does not redact the server trace or scratchpad. Retryable provider failures have bounded delay lists; other/exhausted errors force end-of-step. HTTP 425 slices history to its saved pre-observation length, intended to discard that step; it is a length slice, not an immutable checkpoint, so intervening trimming can weaken that rollback. Pending notices survive ordinary failed actions, and a failed forced end-of-step clears pending state. SRC-1 `agent/baselines/react_160k_compact_30k.py:58-73,422-481,564-570,656-669,702-718,736-757`. Implementation conclusion status: wired.

>     def _redact_last_tool_turn_for_policy_retry(self) -> int:
>         idx = len(self.history) - 1
>         while idx >= 0 and self.history[idx].get("role") != "tool":
>             idx -= 1
>         redacted = 0
>         while idx >= 0 and self.history[idx].get("role") == "tool":
>             self.history[idx]["content"] = _POLICY_REDACTED_TOOL_CONTENT
>             redacted += 1
>             idx -= 1
>         return redacted
> --- `agent/baselines/react_160k_compact_30k.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

RTE-5 — Server action admission/effects. Optional bearer authentication binds configured run/agent endpoints, with admin override; app installs this pre-request function, but require_tokens false bypasses it. Stale-step check only acts when header is present; the supplied SDK sends it after observation. Act enforces known agent/alive state, message/call shape, unique call IDs, end_of_step last, hook availability and quota. Under env.lock it prechecks mutating-call idempotency fingerprints, then executes calls sequentially through schema/denylist/handler checks. Pure end_of_step can bypass closed-hook gate; native/non-env-origin calls are trace-only. Supplied historical tool results can suppress reexecution. Conclusion status: wired, guarantees conditional on this entry and supplied protocol. SRC-1 `env/web/auth.py:55-95`; `env/web/app.py:43`; `env/web/routes_agent.py:208-237,902-1135`; `env/tools/dispatch.py:114-177`.

> def check_stale_step(env) -> Optional[tuple]:
>     """Reject if X-Agent-Step header doesn't match env.t."""
>     declared = request.headers.get("X-Agent-Step")
>     if declared is None:
>         return None
> --- `env/web/routes_agent.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

>             blocked = check_stale_step(env)
>             if blocked is not None:
>                 return blocked
>             if not env.hook_open and not only_eos:
>                 return jsonify({"ok": False, "error": "hook_closed",
>                                  "hint": "wait for GET /observation"}), 425
>             quota_error = _turn_quota_error(env, agent_id)
>             if quota_error is not None:
>                 return jsonify(quota_error), 429
> --- `env/web/routes_agent.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

Mutation idempotency uses agent/step/callID and tool/arguments fingerprint; successful handler results are persisted to cache before return. A different fingerprint conflicts. The handler effect precedes cache persistence, so the inspected ordering does not itself establish a transaction spanning arbitrary tool files/state and ledger writes. Per-call schema failures are tool results and do not roll back earlier batch calls. Record/trace persistence occurs after effects. Direct Python handler callers or omitted step headers are alternate boundaries without the same protocol guarantees. SRC-1 `env/core/simulator.py:1457-1503`; `env/web/routes_agent.py:1042-1127`.

>         result = fn()
>         # Only cache successful results — failures are typically transient and
>         # the agent should be free to retry without the cache returning the error.
>         if isinstance(result, dict) and result.get("ok", True) is not False:
>             self.idem_cache.put(key, {
>                 "__idem_fingerprint": fingerprint,
>                 "__idem_result": result,
>             })
>             self._idem_dirty = True
>             from storage import agent_log
>             agent_log.persist_idem(
>                 self.runs_root, self.run_id, self.idem_cache
>             )
>             self._idem_dirty = False
>         return result
> --- `env/core/simulator.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

Server admission uses step equality when the SDK supplies its latest step, hook/quota guards, scenario denylist and registry argument validation. It executes planned calls sequentially, retaining provenance fields on generated tool results and recording the action. Mutating calls use agent/step/call identity plus argument fingerprint for replay control. A successful HTTP action can contain a tool-level failure, and preflight checks do not make every side effect transactional. SRC-1 `agent/sdk/merchantbench_tool_client.py:185-201`, `env/web/routes_agent.py:219-237,1020-1135`, `env/tools/dispatch.py:114-177`. Optional authentication limits agent tokens to specific paths/agent IDs and excludes trace-reading routes; disabling token enforcement removes that guard. SRC-1 `env/web/auth.py:10-21,55-95`. Implementation conclusion status: wired for action/dispatch; optional authentication enforcement is configuration-dependent.



RTE-6 — Optional run-local scratchpad read/write. Exposed schema asks model to preserve strategy/product notes/open tasks/decisions. Write rejects above256KiB, overwrites current Markdown then appends version/history; read returns current file or empty content. A successful size/schema check is no validation of claims or strategy quality. Caller/model proposes replacement; dispatcher/scenario and size check can veto; no compulsory comparison, reason field or semantic acceptance step. Later consumer must select read tool; archive presence alone is not automatic readback. Source-wired and model use afforded as specified by specialist. SRC-1 `env/tools/registry.py:501-524`; `env/tools/tools.py:2161-2227`.

When schema exposes the tools, the model may request read or write through the same action loop. Server identity selects the run-local file; the model supplies full replacement Markdown, not a file path. A requested read returns full current content and bytes, or empty content if absent. The baseline receives it as a tool result and retains it until ordinary trimming/redaction removes it. Writes are capped at 256 KiB and append version history after current-file overwrite; those writes are not an atomic two-file transaction. SRC-1 `env/tools/registry.py:500-524`, `env/tools/tools.py:2161-2227`, `env/tools/dispatch.py:147-176`, `agent/baselines/react_160k_compact_30k.py:401-420,674-718`. Implementation conclusion status: wired; actual model choice/benefit unobserved.

>     path = _memory_doc_path(env, agent_id)
>     os.makedirs(os.path.dirname(path), exist_ok=True)
>     with open(path, "w", encoding="utf-8") as f:
>         f.write(content)
>     _append_memory_history(env, agent_id, content)
>     return {"ok": True, "bytes": size}
> --- `env/tools/tools.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

RTE-7 — on subsequent observation/action handling, protocol consumers request retained state. Observation composition looks up agent/step cache and prior-observation window; server initialization reloads persisted cursors/windows and idempotency entries. Dispatch reads cached results by exact request identity and checks fingerprints, avoiding repeated successful mutation. Only successful results enter the replay cache; LRU capacity eviction forgets older entries. These are requested protocol reads, not an identifier-targeted push into model history. SRC-1 `env/tools/observation.py:708-729,1114-1141`, `env/core/simulator.py:118-149,1457-1503`, `env/storage/agent_log.py:748-784`. Implementation conclusion status: wired.

>     def put(self, key: str, value: dict) -> None:
>         with self._lock:
>             self._data[key] = value
>             self._data.move_to_end(key)
>             while len(self._data) > self.cap:
>                 self._data.popitem(last=False)
> --- `env/storage/agent_log.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

>     key = (agent_id, int(env.t))
>     cache = _observation_cache(env)
>     if (prefer_cached or mark_observed) and key in cache:
>         out = copy.deepcopy(cache[key])
>     else:
>         window = current_or_cached_change_window(env, agent_id)
>         out = build_store_snapshot(env, agent_id, window=window)
>         out["text"] = render_observation_text(out)
> --- `env/tools/observation.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

RTE-8 — conditional trace-derived continuation notes. The baseline automatically presents recent observation/assistant/tool traces plus the write reminder; the model may derive and write concise strategy, decisions and open tasks to OBJ-2. Later the same model role can request OBJ-2 to recover what left OBJ-1. The durable current file, explicit consumer role and supplied read tool establish an afforded behavioral memory route, rather than a hypothetical storage API. No automatic read immediately after trimming is wired, and no successful note or recall was observed. The complete chain is therefore afforded, although its transport and storage are wired. SRC-1 `agent/baselines/react_160k_compact_30k.py:315-321,483-539,564-607,674-718`, `env/tools/registry.py:500-524`, `env/tools/tools.py:2200-2227`. Rationale retention: unconstrained Markdown may contain reasons, but neither the reminder nor schema requires them. A later read would deliver any included reasons with the full document; there is no independent rationale field or diagnostic reader. Implementation conclusion status: afforded.

>         description="Read this agent's run-local Markdown scratchpad. "
>                     "Use it to recover long-term notes, plans, supplier/product "
>                     "decisions, and open follow-ups that may have fallen out of "
>                     "the context window. Returns empty content if no document exists.",
> --- `env/tools/registry.py` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

### Claims

CLM-1 — Reference baseline is long-context ReAct with optional memory-aware compaction (SRC-2 `agent/README.md:10`). The same README says default scenario denies memory tools (123-127), but pinned default.yaml comments out both memory deny entries, leaving market_brief/hot_search_terms denied. Schema actually follows denylist. Thus memory tools are available under this shipped default unless another configuration changes it; the disabled branch remains implemented. Status: claimed for prose, wired for configuration/schema conflict. No observed benchmark result is supplied.

>   tool_denylist:                 # null = 全部工具可用；例: [search_products] → 禁用 search_products
>     - market_brief
>     - hot_search_terms
>     # - read_memory_doc
>     # - write_memory_doc
> --- `env/scenarios/default.yaml` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

> - **Optional run-local memory tools** — `read_memory_doc` and
>   `write_memory_doc` still exist, but the default benchmark scenario denies
>   them. If a scenario explicitly enables them, they read/write
>   `runs/<run_id>/agent/memory/<agent_id>.md` through the same `/act`
>   trace path.
> --- `agent/README.md` @ `f44ce969aeccfd65d1eef6afe50f69868e510946`

### Evidenced absences

No separate absence record is claimed. Faithfulness testing is not-determinable within the commissioned source/mock-test boundary; unexecuted tests do not establish model dependence.

### Behavioral-authority paths

BAP-1 — Model consumes system brief, user observations/reminders and assistant/tool history. Source-wired delivery; memory-document text arrives as tool content only when requested. Channel priority and semantic activation in provider remain uninspected. Horizon is subsequent hops/steps within retained history; static objective/schema are doctrine, not accumulated learning. Retained dialogue and requested scratchpad content enter the model through ordinary user/assistant/tool message roles. Notes guide choices by their content; there is no parser elevating scratchpad prescriptions to code or validated truth. Maintenance reminders are task instructions at user role. Initial system brief is separately supplied, including the Claude-specific system channel. SRC-1 `agent/baselines/react_160k_compact_30k.py:175-185,393-420,512-520,564-607`. Implementation conclusion status: wired.

BAP-2 — Token/history/step/callID/status metadata controls context selection, stale rejection, replay and continuation. Force is symbolic routing/validation/enforcement at named consumers, not truth endorsement. SDK schema exposure and server enforcement differ from deployed OS/provider grants. Numeric usage, pending flags, current step, retained observation cursors and idempotency fingerprints govern budget, freshness and replay decisions in code. These symbolic controls do not demonstrate learning. SRC-1 `agent/baselines/react_160k_compact_30k.py:483-562`, `agent/sdk/merchantbench_tool_client.py:138-145,195-200`, `env/web/routes_agent.py:208-237,1042-1063`; further consumed protocol state is proposed below. Implementation conclusion status: wired.

## Runtime account

Ordinary invocation: construct/register with run identity and provider credentials; receive observation/brief; choose tool schemas and bounded history; ask model; send assistant action batch; validate and execute in environment; return tool text; repeat within hop/step limits; release hook and obtain a later observation. Termination is HTTP410 or configured day/hour horizon, not proof of good commercial decisions. Context and server logs have separate persistence/readback routes; process restart does not inherently reconstruct local history from trace storage.

Static forcing cases: model emits no calls → synthetic end_of_step; stale header →425 and local step-history removal; denied/invalid tools →error result while earlier independent batch calls remain; provider Forbidden →one redacted retry; memory tool absent →immediate trim, present →reminder then trim independent of write success. No dynamic check planned. Mock branch tests would verify mechanics but not provider behavior, memory truth, simulated policy quality or benchmark validity. No credentials/services were invoked and no packages installed.

Guards are owned by SDK/header and server lock/schema/denylist/idempotency layers; deployment auth is optional. No shell/native execution is implemented by the selected baseline's advertised environment-tool path. Excluded submitted agents may have their own tools and cannot inherit this guarantee. Single baseline model picks actions; server can reject but does not choose better strategies. Coordination is environment hook/quota protocol, not delegated-agent planning.

The operating objective is maximize final net_assets. The inspected score helper returns final net-assets series value, falling back to cash components. It is a simulator outcome metric, not an expected correct action sequence or answer oracle. Agent sees state feedback; no runtime successor/policy-variant adoption follows from scoring. Optional scratchpad edits retain model-authored guidance; any theory, content-directed criticism, resulting revision and improved capacity need separate evidence. Model sampling, history edits and successful simulated actions do not close that chain. SRC-1 `eval/scoring.py:20-76`; `env/tools/observation.py:1083`.


| Route | Return and later consumer | Selection, expiry, visibility and effect limit |
|---|---|---|
| RTE-1 | Observation/schema/register result; next model hop | Run/agent/step and first brief; server cursors reused; no cross-run recall |
| RTE-2 | Tool actions/results; later model history | Coarse recent suffix; trim/redaction; provider sees selected prompt; activation unobserved |
| RTE-3 | Altered history/reminder plus context metadata | Usage/heuristic threshold and schema presence; trim after HTTP success; write is not required |
| RTE-4 | Retry or forced end; later prompt omits/redacts text | Error class and old list length; no rollback of prior external effects |
| RTE-5 | Tool results/turn and replay receipt | Scenario/schema/step/callID; keyed LRU scope; traces do not imply baseline reread |
| RTE-6 | Full current document or write result | Run/sanitized agent path, size cap; overwrite preserves history separately; no automatic historical-version read |
| RTE-7 | Cached protocol data | Agent/step/call key, cursor/window, LRU capacity; state recovery does not restore model history |
| RTE-8 | Optional durable notes then requested recall | Model choice guided by reminder/tool descriptions; current version until overwrite; content effect unobserved |

## Lens scoping

### Memory/context scope

Full lens on cross-invocation history, compaction/redaction, optional current/versioned scratchpad, operational trace/usage/context and later consumers. Include enabled and denied memory-tool branches, source/default documentation discrepancy, retries/stale handling. Exclude whole simulator databases merely accessed as environment state, static schemas/doctrine from accumulated memory and private/model internals.

### Epistemic scope

Full lens on model-guided operational decisions and retained strategy text, simulator feedback, schema admission and score authority. Inspect whether any modeled decision/criticism path licenses knowledge improvement; keep scenario validity and observed outcomes outside this subsystem source boundary.

## Lens outputs

### Memory/context lens


Automatic acquisition retains the observation and successful action transcript in OBJ-1; the server separately retains OBJ-3. Reasoning content returned by the provider may be preserved, but it is not a verified rationale for later scratchpad prescriptions. The baseline does not mine its persisted trace files. The in-process trace is the input to the optional RTE-8 transformation, and the current scratchpad is its potentially derived output. This distinction matters: raw JSON logging alone does not meet trace learning.

RTE-3 is primarily destructive maintenance of existing history. Its enabled branch gives one model turn an opportunity to save information; any HTTP-successful action then advances trimming, including an unrelated tool action, an oversized memory-write rejection carried as a tool result, or a fallback end-of-step. The disabled branch trims immediately and retains a notice. No generated summary checkpoint is mandatory. The scratchpad has no retention-policy timer or semantic conflict resolver. RTE-6 can replace current content with an empty document; old versions still remain in its history file. These facts support decay and afforded evolve, without establishing consolidate, dedup, synthesize, invalidate or promote as built-in semantic operations.

RTE-7 writes control records through normal operation and forgets LRU cache entries by capacity. Its idempotency term denotes operation replay control, not memory deduplication. The observation cursor records which interval has been served; the simulator's underlying business state remains outside the memory profile. No manual approval or human editing workflow is present in the commissioned baseline/tool route. Direct filesystem tampering is not inferred as a supported adoption surface.



RTE-2 is automatic push: each hop triggers a reverse scan of retained messages, keeps a recent suffix under an estimated budget, removes leading orphan tool results, sanitizes tool arguments and supplies the selected messages to the model. Cost is linear in examined retained messages, with no semantic search index. Budget values are approximate, and system prompt/tools/provider overhead can exceed the nominal history budget. Cache breakpoints for Claude alter provider request hints, not local retention policy; provider cache internals are excluded.

RTE-6 is model-requested pull of the entire current scratchpad, scoped by server run/agent identity. Its read tool has no query, semantic ranking, historical-version selector or partial-content budget. A 256 KiB maximum file can still be large relative to the approximate 30k retained history. Once returned, its tool message joins ordinary push history on later invocations. Requested delivery is not counted as a second push merely because the client appends the response.

RTE-7 is pull by the runtime's observation/dispatch roles. It reads keyed state to preserve protocol continuity; it does not feed an independent learned strategy. OBJ-3 is retained operational evidence with trace-reading endpoints, but the inspected baseline does not request them. Their existence does not supply a second baseline memory route. With optional token enforcement enabled, the agent-token allowlist excludes those trace endpoints. No path imports scratchpads or traces from another merchant run. Availability and delivery are implemented; content activation and task benefit remain unobserved.



The profile unions the exposed-tools and denied-tools alternatives at one explicit subsystem boundary. OBJ-1, OBJ-2, OBJ-3 and OBJ-5 support files/in-memory storage and natural-language/symbolic forms. A JSON dictionary is counted under its actual storage, not as evidence of a KV database. Static OBJ-4 and environmental databases do not inflate the profile.

Lineage distinguishes model authorship, imported observations/results, deterministic compilation of notices/control metadata, and the afforded extraction of continuation notes from the current trace. Behavioral authority distinguishes advisory knowledge, maintenance instructions, coded enforcement/routing and the afforded use of derived guidance. The weakest complete-union basis is afforded wherever the optional derived route contributes. The scoped producer roles are automatic; a hypothetical human writing Markdown on disk does not add manual agency.

The qualifying learning route is RTE-8 only. It receives session conversation and tool traces, produces persistent natural-language continuation notes and affords their consumption within the same merchant operating task. Scope, timing and form refer to that same route: per-task, online, natural-language. A run identifier alone would not prove the horizon; here the unchanged operating loop plus explicit strategy/open-follow-up recovery contract establishes continuation of one task. There is no weight-learning inference and no offline trace-mining pipeline.

Trace learning is assessed yes at afforded basis for the enabled-tools branch, not as an observed outcome or as an invariant of compaction. In the denied-tools branch, only raw-history truncation, logging and protocol-state maintenance remain; none supplies qualifying distilled guidance, so that branch alone would be no, with trace source/scope/timing/form inapplicable. Actual default configuration at this commit belongs to the enabled branch despite README wording. Curation and read-back distinctions are retained in RTE-3, RTE-4, RTE-6 and RTE-7. No faithfulness-test result is available in the permitted evidence; the profile explicitly leaves that axis not-determinable.


### Epistemic lens

1. Boundary: named ReAct/interface routes; no live candidate, simulator intervention or run report observed. CLM-1 characterizes context machinery, not measured learning.

2. Objects: observations/tool results assert simulated state; their authority is the chosen simulator contract. Model actions and scratchpad can state predictions or strategies, but source code does not establish the content of any actual theory. History fields are individually inspectable; free text lacks compulsory assumptions/rationale/criticism structure. Token/step/ID state is operational metadata. Static rules/objective direct behavior without being revised through this loop.

3. Authority ledger:

| Function | Architectural status | Content and admission | Warrant limit |
|---|---|---|---|
| RTE-1 observations | implemented | acquire simulator-supplied text, initial brief | true within engine contract not independently validated real-world truth |
| RTE-2 inference | implemented | model chooses actions from history/tools; potentially ampliative judgments | internal criticism/formulation uninspected; no external correct-action oracle |
| RTE-5 check/disposition | implemented | schema/identity/step/denylist admit or reject operation | protocol validity not decision quality |
| RTE-2 feedback | implemented | tool result enters later prompt | availability does not show content-directed criticism or improved policy |
| RTE-3, RTE-4 maintenance | implemented | tail selection/redaction reshapes evidence | budget/provider compatibility is not epistemic refutation |
| RTE-6 retention | implemented | proposed Markdown replacement admitted by size/schema | persistence is no truth acceptance |
| Score helper | implemented external metric definition | final net assets derived from supplied series/cash | no inspected hypothesis test or automatic revision selection |

4. Lifecycle: model output can contain ampliative decisions, but no candidate-linked prediction/consequence test or criticism record is required. Discovery lifecycle architectural candidate generation is implemented via model call; its theory formulation and content-directed test/adoption are uninspected. Observed candidate state: no instance observed at each phase. Successful tools prove only returned operation outcomes within the simulated interface; they do not prove the policy explanation. Memory serialization/trimming has no necessary new truth-apt candidate.

5. Claim comparison: long-context/compaction machinery exists, but retained data can be dropped/redacted and saving is optional even after reminder. Published benchmark rank/benefit cannot be inferred from scoring code. Documentation/config conflict must resolve toward pinned executable configuration for default availability.

6. Bounded conclusion: a feedback-connected operational agent with explicit protocol controls, not a demonstrated theory-learning loop. Formulation, operative use, criticism, changed reliance and attributable improved future capacity each remain uninspected for any particular formulated strategy, even though the tool/retrieval capability affords them.

## Reconciliation

Verified full specialist report, run/source/pin and unchanged input/method SHA; report hash recorded above. Mapped MEM-OBJ-1 → OBJ-5; MEM-RTE-1 → RTE-7; MEM-RTE-2 → RTE-8. Existing seeds retain their identities.

All six issues accepted: pinned default exposes memory tools despite README; include consumed cursor/idempotency metadata without importing simulator domain databases; preserve optional trace-derived note route at afforded basis; compaction follows HTTP success, not successful write; stale rollback is a length slice weakened by intervening trimming; sanitized agent IDs can collide and scratchpad current/history writes are not atomic. Baseline independently found configuration mismatch and mandatory-trim limit; no stronger execution claim follows. No unresolved substantive conflict. Quoted report evidence integrated once; duplicate baseline passages retained at existing canonical record.

## Bounded synthesis

The strongest supported contribution is a reusable model-action-feedback loop with source-visible context maintenance, optional persistent notes and guarded environment admission. It distinguishes tool effects, per-step control and retained trace, but neither locks nor a context window name supply whole-turn transactional or semantic guarantees.

Reflection is wired narrowly where prompt-size/provider-failure state changes later context handling. A reflective theory builder is uninspected. Self-improvement and conjectural learning remain uninspected: environment feedback and writable notes make a process possible, but no candidate-linked criticism and improved future capacity were observed. Per-branch memory findings qualify that partial contribution rather than denying it. Controlled decision/memory interventions, retained critic/revision traces and fault/replay tests would strengthen distinct claims.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| Provider/simulator internals excluded | CMP-2, CMP-3 | requests and returned interface state | fixed weights, market validity or actual decision quality | pinned internals and experiments |
| Static source only | RTE-2, CLM-1 | baseline/control code | benchmark outcome, activation and causal improvement | retained controlled runs |
| Conditional protocol guarantees | RTE-5 | selected SDK/server calls | universal stale rejection/exactly-once batch | alternate-client and failure testing |
| Heuristic context budget | RTE-3 | tail trim/usage | hard token cap or preservation of all tool pairs | provider tokenization and boundary tests |
| Optional note production/recall | RTE-8 | model-selected enabled-tools chain | guaranteed write, recall, faithfulness or gain | observed note/recall behavior and controlled task outcomes |
| Scratchpad/control failure bounds | OBJ-2, RTE-4, RTE-6 | two-file order, name sanitization and list slice | unique raw-ID isolation or exact restoration | collision/crash and context-trim tests |

## Verification and blockers

### Semantic verification

Checked normal and fallback loops, optional auth/header guarantees, per-call versus batch effects, source/default conflict, provider resolution, feedback versus answer oracle, score versus admission, and separate reflection/learning/capacity claims. Integrated all eight routes/five objects. Profile union includes enabled/denied branches, with current default enabled. Only RTE-8 affords trace-derived continuation notes: session conversation/tool traces, per-task online natural-language output, later model pull. Raw tail trimming, trace logs and replay metadata are not substituted as trace learning. Coarse model-history push differs from requested scratchpad and keyed protocol pull. No identifier push inferred from run IDs. Capacity LRU forgetting and history removal qualify decay; overwrite affords evolve without semantic synthesis/guaranteed consolidation. Static OBJ-4/model assets excluded from accumulated memory. Faithfulness remains uncertain, and benefits/criticism-driven capacity are unobserved.

### Deterministic validation

Full result validation and guarded quote/anchor verification follow integration.

### Blockers

none
