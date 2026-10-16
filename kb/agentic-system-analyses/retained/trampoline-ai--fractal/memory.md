---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Fractal memory: deterministic session projections, bounded exact history, explicit resume and workspace instruction reload."
run-id: AAS-2026-10-14-fractal-ee03010af4c2-01
source-identity: "https://github.com/trampoline-ai/fractal"
reviewed-boundary: "6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385"
---

# Fractal memory report

## Boundary and evidence

This report covers Fractal's retained session material and its later consumers, workspace instruction reload, and the context controls Fractal configures for PredictRLM. SRC-1 is the frozen repository declared in boundary.md. Direct inspection confirmed HEAD at the reviewed commit. Evidence is implementation and doctrine/design; neither the target nor its tests were executed. No observed-run or causal evidence establishes recall, compliance or benefit.

The memory boundary includes both shipped drivers, the public Python adapter, session save/load/listing, runtime finalization, hook reduction, prompt construction, and the context estimator. Direct reads covered all of `src/fractal/session.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`, and `src/fractal/context_meter.py`; the hook targets/reducer/registration in `src/fractal/events.py`; CLI headless construction; TUI resume/new/list/usage and retained-turn rendering; the round-trip test in `tests/test_session.py`; and `docs/session-management.md`. Remaining CLI/configuration and filesystem-skill coverage comes from the supplied runtime report, not an independent full reread. Source searches covered session/history/summary/cleanup occurrences across `src`, session tests, docs and bundled caller instructions.

External PredictRLM compaction, recursive context isolation, document-skill bodies, provider state and SBX reuse internals are outside the frozen artifact. User workspaces are inputs, not supplied evidence. Thus Fractal's visible handoff does not establish exact internal prompts, subordinate-frame retention, model-selected recall, retained container contents or isolation. No new source is declared.

| Entry point or operation | Source path (SRC-1) | Coverage and prevented conclusion |
| --- | --- | --- |
| Submit, pending checkpoint, success/failure/budget/interruption | `src/fractal/runtime.py`, `src/fractal/session.py` | Direct reads; [MEM-RTE-checkpoint-update](#mem-rte-checkpoint-update); supplied [RT-RTE-interactive-interrupt](runtime.md#rt-rte-interactive-interrupt) and [RT-RTE-budget-exhaustion](runtime.md#rt-rte-budget-exhaustion). |
| Summary projection, rendering and history eviction | `src/fractal/session.py`, `src/fractal/agent/signature.py` | Direct reads; [MEM-OBJ-session-summary](#mem-obj-session-summary), [MEM-OBJ-session-history](#mem-obj-session-history), [MEM-RTE-session-context](#mem-rte-session-context). |
| Explicit headless/TUI resume, new session, listing | `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/tui/app.py`, `src/fractal/session.py` | Direct bounded driver reads and full session/runtime reads; [MEM-RTE-session-reload](#mem-rte-session-reload). Remaining CLI dispatch supported by supplied [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn). |
| Hook and trace-derived accounting | `src/fractal/events.py`, `src/fractal/runtime.py`, `src/fractal/session.py` | Direct reducer/registration and consumer reads; [MEM-OBJ-turn-usage](#mem-obj-turn-usage), [MEM-RTE-checkpoint-update](#mem-rte-checkpoint-update); supplied [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting). |
| Root guidance and editable workspace | `src/fractal/agent/service.py`, `src/fractal/agent/signature.py` | Direct reads; annotation on [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance). Arbitrary nested instruction discovery remains model-directed workspace inspection, not a Fractal automatic loader established here. |
| Direct library call | `src/fractal/agent/service.py` | Direct read; annotation on [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent). No invented later caller or automatic persistence. |
| Context estimate and usage display | `src/fractal/context_meter.py`, `src/fractal/tui/app.py` | Direct estimator and usage-handler reads; [MEM-OBJ-turn-usage](#mem-obj-turn-usage). Display estimates do not enforce a context cap. |
| Config/default replacement | `src/fractal/config.py`, `src/fractal/config_commands.py`, `src/fractal/runtime_lms.py` | Supplied [RT-RTE-config-change](runtime.md#rt-rte-config-change); annotation only. Not conversation-derived knowledge. |
| Reused/removed sandbox, mounted files, static/document skills | `src/fractal/agent/service.py`, `src/fractal/agent/skills.py` | Direct service read, supplied runtime skill account; [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn). External backend/skill implementations prevent conclusions about container-memory contents and frame compaction. |
| Source evaluators | `tests/test_session.py` | Direct round-trip test read; asserts counts versus detailed lists and global storage. No execution result or semantic recall evaluation supplied. |

## Core ideas

Fractal separates a persistently accumulating trajectory projection from a recent detailed tail. The projection preserves entire user messages and returned response strings; it compresses activity lists into counts and omits detailed traces. This is deterministic field selection, not a Fractal model-written abstractive summary. Structured JSON is mixed symbolic metadata and natural-language content; the name “structured” does not make interpreted message content symbolic. See [MEM-OBJ-session-summary](#mem-obj-session-summary).

The projection is automatically embedded in the next signature. Detailed history is passed as structured predictor input with a request to inspect it from Python for exact recall. These are separate authority and access paths. A 20-turn detailed-history cap does not bound the projection's message or response lengths, its number of turns, or external inner-loop context. See [MEM-RTE-session-context](#mem-rte-session-context).

Failures and recognized interruptions are retained, not filtered out as rejected experience. The runtime distinguishes returned budget exhaustion from ordinary return but does not grade task correctness before memory admission. Hook observations and trace accounting are provenance-distinct from model output, yet they are not an independent answer oracle or complete execution audit. See [MEM-RTE-checkpoint-update](#mem-rte-checkpoint-update) and supplied [RT-CLM-result-contract](runtime.md#rt-clm-result-contract).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-session-summary
Label: SessionSummary trajectory projection

Part of: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Source-native identity: `SessionSummary.turns` of `SummaryTurn`, each with `UserTurn` and optional `AgentTurn`. Storage substrate: in-memory Pydantic objects and the summary portion of the workspace-keyed session JSON. Representational form: symbolic IDs, statuses and numeric counters plus natural-language user messages, response and error strings. Lineage: caller message copied verbatim; returned response copied without semantic summarization; list lengths and usage derived by host code; status/error supplied by runtime branches. Initial user-message provenance is the generic caller, not established human authorship.

Its model-facing display includes all summary turns, user messages, pending/final status, complete nonempty response, activity counts and nonempty error. It does not render `usage`. The summary preserves neither detailed operation identities nor a separately extracted account of reasons. A response can contain reasons, but Fractal does not require or validate them. Later consumers: signature builder and model-facing instruction text; TUI conversation rendering; cumulative usage reducer. Authority differs by consumer: interpreted context in the model, deterministic rendering/aggregation in host code. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/agent/signature.py`, `src/fractal/tui/app.py`. This is a material part, not a duplicate checkpoint container.

> summary_turn.agent = AgentTurn(
>     status=status,
>     response=response,
>     files_read_count=len(files_read_list),
>     files_changed_count=len(files_modified_list),
>     commands_run_count=len(commands_run_list),
>     error=error,
>     usage=turn_usage_from_trace(trace),
> )
> --- `src/fractal/session.py`

> for index, turn in enumerate(summary.turns, start=1):
>     lines.append("")
>     lines.append(f"Turn {index} ({turn.turn_id})")
>     lines.append(f"User: {turn.user.message}")
> --- `src/fractal/session.py`

#### MEM-OBJ-session-history
Label: SessionHistoryTurn detailed tail

Part of: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Source-native identity: `SessionState.history`, a list of `SessionHistoryTurn`. Storage substrate: same JSON checkpoint and Pydantic state. Representational form: symbolic identifiers, status, timestamps and operation lists, natural-language messages/errors, and an externally defined `RunTrace` payload. Full trace encoding and original production are dependency-owned; Fractal accepts typed traces and validates compatible exception payloads rather than proving completeness. This is retained execution material, not an independently curated knowledge base.

Lineage: user-message copy, hook-derived file-read and command lists, result-provided changed-file list, and result/exception trace. In particular, the runtime does not persist `RuntimeEventTracker.files_modified` as the authoritative changed-file list. Failed/interrupted branches omit `changed_files`, producing an empty stored modification list even when execution may already have edited files. Detailed history does not have its own assistant-response field; the response lives in the summary and may also be represented inside the opaque trace.

Later consumer: predictor input and afforded Python inspection by the delegated model; session loader also reconstructs it. Tail selection is by turn recency, not relevance, path, error class or similarity. The current pending turn is appended before selection, so the 20-slot tail on submission includes it and at most 19 earlier entries. Save and payload construction both enforce the cap. No inspected loader restores evicted traces from the summary. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`; container relation as above, distinct from the summary part.

> history_turn.files_read = files_read_list
> history_turn.files_modified = files_modified_list
> history_turn.commands_run = commands_run_list
> history_turn.trace = trace
> --- `src/fractal/session.py`

> def _enforce_history_limit(self) -> None:
>     self.state.history = self.state.history[-MAX_HISTORY_TURNS:]
> --- `src/fractal/session.py`

#### MEM-OBJ-turn-usage
Label: TurnUsage accounting projection

Part of: [MEM-OBJ-session-summary](#mem-obj-session-summary)

Source-native identity: optional `AgentTurn.usage: TurnUsage`. Representational form: symbolic numeric counters. Storage substrate: summary JSON and in-memory models. Lineage: main plus sub trace usage, duration and iterations; context size taken from the latest trace step with a positive integer main input-token count, not from the response. Unknown when no trace exists. Later consumers: session aggregate `/usage`, headless envelope conversion, and UI accounting. Numeric accounting is not inserted by `render_session_summary` into the model-facing summary, though detailed trace usage is available through history. No learned policy or semantic conclusion is derived here.

Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/tui/app.py`, `src/fractal/context_meter.py`. Closest supplied accounting record is [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting), which concerns hook activity rather than this trace-derived numerical part. The context estimator instead constructs prospective messages through private PredictRLM methods and token-counting fallbacks. Its cache uses session digest, model/budget/path metadata and root instruction stat metadata; it is display support, not an admission or trimming mechanism.

> for step in reversed(trace.steps):
>     prompt_tokens = step.usage.main.input_tokens
>     if isinstance(prompt_tokens, int) and prompt_tokens > 0:
>         context_tokens = prompt_tokens
>         break
> --- `src/fractal/session.py`

### Routes

#### MEM-RTE-checkpoint-update
Label: Automatic checkpoint projection

Endpoints and progression: caller request → pending summary/history append and save → delegated result or caught exception plus hook observations → final summary/history updates → same JSON save. Owner: Fractal runtime/session code. Context and state effects are the retained parts above; workspace effects are independent and not rolled back. This describes the memory transformation across [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-RTE-budget-exhaustion](runtime.md#rt-rte-budget-exhaustion) and [RT-RTE-interactive-interrupt](runtime.md#rt-rte-interactive-interrupt), not another full invocation route. Evidence: SRC-1, `src/fractal/runtime.py`, `src/fractal/session.py`, `src/fractal/events.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: turn ID on append; finalization mutates state, saves and either returns the live result or reraises the error/cancellation.
- Later read-back: summary text and bounded history reach later submit; explicit resume reconstructs them across processes; usage reaches later display.
- Delegated visibility: subsequent model receives response/error/status/count projection as instruction context and detailed tail as predictor input, not all raw hook-event objects.
- Selection predicate: current turn UUID selects the records to update; result trace status selects budget versus succeeded; exception and interruption predicate select failure/interrupted paths.
- Invalidation or expiry: matched final agent data replaces pending state; detailed tail is capped at 20; summary is retained without an inspected turn cap; save overwrites the checkpoint rather than appending a revision archive.
- Activation or effect: deterministic retention and projection are implemented; subsequent model behavior and improved capacity are not observed.
- Evidence limits: malformed/missing trace can yield no trace; hooks are best effort; unrecognized cancellation can leave pending state; writes are not atomic transactions and effects are not rolled back.

Admission: generic caller supplies message; delegated computation supplies response and changed-file proposal; host code computes counts/status/usage and performs I/O. There is no per-content human approval. Type/schema checks can reject malformed structure, but the ordinary success branch is not an answer oracle. Operating mode is recording an open request, not candidate comparison. Error/budget/interruption statuses label incomplete work rather than withdrawing already applied edits or deleting its memory. Guidance shaping delegated work is [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace). Recovery is saved failure context and subsequent caller action; pending/on_pending failures can precede the guarded call.

Trace-fed update is narrow: trace usage/status and hook lists feed durable context and accounting; there is no separate host synthesis of lessons from trace reasoning. Reasons survive only if present in response or surviving trace, and Python recall is afforded, not observed. File reads are added after observed operations; commands are added before execution, so `commands_run` alone is not proof of successful completion.

> if phase == "before":
>     _append_unique(self.commands_run, command)
> --- `src/fractal/events.py`

#### MEM-RTE-session-context
Label: Subsequent turn context delivery

Endpoints and progression: later submit in selected session → render all summary turns and take recent history tail → build signature with root instructions → pass history/workspace/request into PredictRLM. Owner: Fractal code selects delivery; model/dependency decide whether to inspect exact details. State/action effect: renewed model-facing context; the next computation may edit mounted files. Distinct from [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn): this isolates retained-material selection shared with interactive submission. Evidence: SRC-1, `src/fractal/runtime.py`, `src/fractal/agent/signature.py`, `src/fractal/agent/service.py`, `src/fractal/session.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: constructed signature and predictor input; no standalone retrieval answer.
- Later read-back: all retained summary content is pushed on each subsequent turn; detailed tail is supplied for optional exact-recall inspection.
- Delegated visibility: summary embedded in signature docstring; `session_history` passed to `predictor.acall`; exact variable previews and Python inspection behavior belong to PredictRLM.
- Selection predicate: submit is the automatic trigger; selected session state is the input; all summary turns and the last 20 history entries are selected, including current pending state.
- Invalidation or expiry: old detailed entries are removed by code recency rule; projection remains; no semantic-relevance selector or summary token budget appears in these inspected functions.
- Activation or effect: context handoff is wired; no trace demonstrates that the model reads details or changes a decision because of remembered content.
- Evidence limits: the signature's exact-recall request is not proof of complete retained traces, especially after eviction; inner-loop compaction and recursive context are outside source scope.

> rendered_session_summary=self.session.summary(),
> session_history=self.session.session_history_payload(),
> --- `src/fractal/runtime.py`

The supporting signature passage is retained in [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace). This is automatic same-session delivery, not a request-directed search over a memory collection. Any Python lookup within delivered history is foreground model-directed and afforded; its actual selector, extracted parts and token budget are unobserved. Detailed tail eviction resembles freeing older retained entries, but there is no reference/liveness tracking: the remaining summary is a lossy by-value projection, not a pointer capable of recovering the dropped trace. Sub-agent stack/frame behavior cannot be inferred from Fractal's `sub_lm` configuration.

#### MEM-RTE-session-reload
Label: Explicit session reload and rejection

Endpoints and progression: session-ID selector → workspace-keyed file lookup → JSON/schema/embedded-ID checks → retained state or empty replacement → TUI rendering and later submit. Owner: caller chooses session; Fractal loader admits structure. `/sessions` separately lists parseable schema-compatible files with ID, mtime ordering, turn count and first message, then lets the caller choose; it is navigation, not model semantic retrieval. This is the cross-process selection branch within [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), with distinct load/rejection policy. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/runtime.py`, `src/fractal/cli.py`, `src/fractal/tui/app.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: loaded FractalSession or empty state with requested ID; runtime rejects nonexistent files before loading; TUI renders retained turns after resume.
- Later read-back: accepted state feeds the next context-delivery route; rejected contents do not feed that session context; a copied bad-file backup is not automatically consumed.
- Delegated visibility: no model call during load/list; accepted projection/history reaches a later submit.
- Selection predicate: resolved workspace path chooses state namespace; exact requested ID chooses file; accepted schema version and matching embedded ID admit it; listing orders by file mtime, not relevance.
- Invalidation or expiry: unreadable/invalid JSON triggers attempted backup and empty replacement; wrong shape/schema/embedded ID gives warnings and empty replacement without that backup branch; later save can overwrite the original requested file.
- Activation or effect: source wiring supports reload or exclusion from future context, not semantic trustworthiness; `/new` changes the active session without deleting stored sessions.
- Evidence limits: structural validation does not authenticate author/source or compare contents against workspace reality; listing does not check filename against embedded ID as load does; no observed resume or recovery result supplied.

Admission is software validation, not manual approval of every retained statement. The caller selects an ID but authorship can include model returns and external file edits. Recovery preserves a copy only in the read/JSON failure branch; backup failure is warned, not repaired. No task-answer oracle participates. The namespace uses FRACTAL_STATE_HOME, else XDG state home plus `fractal`, else `~/.local/state/fractal`; workspace key combines resolved-path slug and hash. Moving a workspace changes its lookup namespace, not the truth of saved contents.

> if not session_path(self.workspace_path, session_id).exists():
>     raise FileNotFoundError(f"No Fractal session found for id {session_id!r}.")
> self.session = FractalSession.load(self.workspace_path, session_id=session_id)
> --- `src/fractal/runtime.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-summary-context
Label: Retained summary as instruction context

Consumer: PredictRLM model-facing signature. Channel: dynamically rendered summary within instruction docstring, not a dedicated neutral data field. Force: model-interpreted trajectory context, with static guidance describing it as prior messages/results; delivery establishes neither compliance nor verified truth. Horizon: later turns and explicit cross-process resume of the same workspace/session. Source trust: host-generated status/counts coexist with caller messages and model responses; no independent content-validation boundary or escaping transforms these strings into a trusted proof. Evidence: SRC-1, `src/fractal/agent/signature.py`, `src/fractal/session.py`; [MEM-RTE-session-context](#mem-rte-session-context). Closest supplied [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace) is the full signature object, not this retained-summary authority path; [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance) carries a different source.

> class EditWorkspaceWithSession(dspy.Signature):
>     __doc__ = instructions
> --- `src/fractal/agent/signature.py`

## Annotations

#### On [RT-OBJ-session-state](runtime.md#rt-obj-session-state)

Storage and consumers are split into the summary, history and usage parts declared above. The checkpoint is not an event-log archive: same-file write replaces the serialized state, and history truncation happens before persistence. Malformed-file backups are recovery copies without an inspected model read-back route. SRC-1, `src/fractal/session.py`.

#### On [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance)

Write agency is open task editing, not a dedicated automatic memory author. Root AGENTS.md is reloaded from disk each call, truncated at 20,000 characters, and delivered as interpreted instructions subordinate to current request. This can carry externally edited or model-edited retained guidance across sessions, but source-only evidence does not establish that a change occurred or was adopted correctly. Other workspace contents remain model-inspectable files rather than automatic instruction inclusion. SRC-1, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`.

#### On [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent)

Caller-provided rendered summary and history have unresolved initialization control and provenance. The adapter still constructs the signature and passes supplied history, but does not apply FractalSession's 20-turn cap itself or automatically save/load state. Supplied API inputs establish a consumption capability, not a separately wired later memory caller. SRC-1, `src/fractal/agent/service.py`.

#### On [RT-RTE-config-change](runtime.md#rt-rte-config-change)

Retained TOML is symbolic capability configuration consumed by launch resolution, not conversational instruction text or trace-derived lessons. Operator choice and schema/catalog checks admit configuration; authorship is not proven human merely by interface. Workspace-specific overrides can supersede global defaults. These fields retain the supplied implementation account without re-declaring a config store. SRC-1, `src/fractal/config.py`, `src/fractal/config_commands.py`, `src/fractal/runtime_lms.py` (supplied runtime evidence).

## Write side

[MEM-RTE-checkpoint-update](#mem-rte-checkpoint-update) acquires raw caller input, delegated responses/traces and normalized operation observations. Host code projects those into summary and history, saves automatically, and trims by recency. This qualifies as trace-fed retained context production only for the actual derived status/accounting/context fields, not an inferred general lesson-learning algorithm. Source claims that the summary preserves modified files or commands must be read as counts in that projection: identities are in the recent tail. Source claims that `commands_run` or succeeded status prove completed/verified work exceed their admission checks.

[MEM-RTE-session-reload](#mem-rte-session-reload) rejects structurally invalid retained state and can preserve a recovery copy, but does not evaluate its conclusions. `/new` withdraws the old session from active context without deleting it. `--fresh` removes a reusable sandbox and `--ephemeral` changes reuse configuration, not session JSON or workspace edits. This distinction follows SRC-1, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`, and supplied [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn). No claim is made about residual data inside externally implemented containers.

## Read-back

[MEM-RTE-session-context](#mem-rte-session-context) is automatic push of the selected session's entire projection plus recent detail, not semantic memory search. [MEM-RTE-session-reload](#mem-rte-session-reload) is caller-directed identifier selection before that push. The later model is the actual afforded exact-detail consumer; a request to inspect history is not an observed inspection. Root instruction reload is a separate persistent-file authority path. `/sessions`, resumed-turn rendering and `/usage` are human/calling-agent navigation or accounting consumers, not model retrieval or admission gates. Headless JSON is an immediate single-turn return contract, not another durable memory store. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/tui/app.py`, `src/fractal/agent/service.py`; supplied [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn).

The only visible fixed context selections are detailed-tail eviction and root-instruction truncation; summary length is not capped by the inspected renderer. The context meter estimates rather than trims. Dependency context compaction, isolated recursive frames and what crosses those frame boundaries remain uninspected. This preserves the implemented Fractal controls without attributing external loop behavior to them.

## Integration issues

1. No supplied runtime finding requires correction. The summary/history container is retained, with material parts declared rather than duplicated: [MEM-OBJ-session-summary](#mem-obj-session-summary), [MEM-OBJ-session-history](#mem-obj-session-history), [MEM-OBJ-turn-usage](#mem-obj-turn-usage). The memory routes specialize mechanisms shared with the supplied runtime routes; they do not replace those invocations. The summary authority path is distinct from the root-guidance path. There are no proposed duplicate referents after this comparison.
2. Documentation's “compressed” summary and file/command preservation language needs qualification: the host copies whole messages/responses and retains only activity counts in the projection. Reasoning and operation identities remain in bounded detail where available, not a validated enduring lesson store. Evidence: SRC-1, `docs/session-management.md`, `src/fractal/session.py`; [MEM-OBJ-session-summary](#mem-obj-session-summary), [MEM-OBJ-session-history](#mem-obj-session-history). Consequence: no assertion of semantic abstraction, complete exact recall or fixed summary budget.
3. Actual trace structure/completeness, inner-loop summarization, recursive isolation, provider state and sandbox retention are unresolved outside source scope. Evidence: SRC-1, `src/fractal/agent/service.py`, `src/fractal/context_meter.py`; [MEM-RTE-session-context](#mem-rte-session-context), [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent). Consequence: do not infer absence of dependency mechanisms, exact model-visible context or reliable recall from Fractal's labels.
4. Failure/interruption can coexist with already changed workspace files but empty stored modification lists; command lists can include attempts. Evidence: SRC-1, `src/fractal/runtime.py`, `src/fractal/events.py`; [MEM-RTE-checkpoint-update](#mem-rte-checkpoint-update), [MEM-OBJ-session-history](#mem-obj-session-history). Consequence: retained metadata is not an exhaustive audit or rollback record.
5. The listing admits structurally valid entries without the loader's filename/embedded-ID consistency check. Evidence: SRC-1, `src/fractal/session.py`; [MEM-RTE-session-reload](#mem-rte-session-reload). Consequence: a displayed ID is a navigation affordance, not proof the matching selector will load that listed file. No exercised inconsistency is claimed.

## Limitations and checks

Frozen Git identity was rechecked at the exact supplied revision. No new source, external lookup, target execution, dependency install or test execution was used. Authoring followed the supplied memory type, worker rules and record contract; supplied runtime evidence is distinguished from direct reads. Actual operation, memory activation, semantic trust, recall quality and causal benefit remain unestablished. Opaque dependency processing is a local limit, not evidence of absent learning or context management. Retaining experience and supplying it later alone establishes neither improved capacity nor exercised self-improvement.

Validation: invocation-specific `commonplace-run validate-output` passed the member content check. The command states that invocation residue is not checked and that this is neither job acceptance nor claim support.
