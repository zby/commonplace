---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "JAZ's session-object history, context filtering, saved-response execution and token-native rollout/export surfaces."
run-id: AAS-2026-10-15-jaz-a94bea79c61a-01
source-identity: https://github.com/jaz-lang/JAZ
reviewed-boundary: 0803d4971be785e95b80054b02259664d70fa3da
---

# JAZ memory report

## Boundary and evidence

JAZ retains several different things, not one memory database: session input/result objects, current-invoke messages and REPL history, execution traces, generated workflows, token rollouts and user configuration. Their consumers have different authority. In particular, replayed assistant text can become executable code; a readable trace directory does not have that authority merely because it contains the same text.

This report uses SRC-1 at the exact boundary revision. Direct source inspection and supplied runtime findings are distinguished below. HEAD was rechecked as `0803d4971be785e95b80054b02259664d70fa3da`; the checkout was clean. No target code, tests, examples, providers or services were executed. Source establishes implementation and documented affordances, not successful operation or improved capacity.

The memory scope includes shipped console consumers, hooks, core context controls, trace post-processing and exposed SGLang weight-management transport. Recursion is included as working-context isolation, not automatically cross-invocation memory. Provider weights, KV caches, storage services and an external trainer are opaque/external: their absence from the capture prevents assessing their persistence and update policy. Static prompt templates are context-construction inputs, not experience-derived memory. Arbitrary application file stores and custom hooks are outside this account; the shipped host-tool capability remains covered by [RT-RTE-host-tools](runtime.md#rt-rte-host-tools).

### Coverage inventory

| Entry point / operation | SRC-1 paths and inspection basis | Records / limit |
|---|---|---|
| Library invoke/ainvoke, recursive contexts, namespace/history | Supplied runtime; direct reads of `src/jaz/_agent.py` edit/projection methods and `src/jaz/protocol/code_only.py` opener, observation and history builder | [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop), [RT-RTE-recursive-work](runtime.md#rt-rte-recursive-work), [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state), annotations below |
| Input/output abbreviation and hook context edits | Direct: `src/jaz/protocol/code_only.py`, `src/jaz/hooks/effects.py`, `src/jaz/hooks/builtin/context_window.py`; runtime supplies core loop wiring | [MEM-RTE-context-selection](#mem-rte-context-selection); generic hooks can supply summaries, but no summarizing policy is established by this seam |
| Console prompt-turn history and helper transcripts | Direct: `src/jaz/console.py` history classes/chat binding; helper consumption and execution gate also supplied in runtime | [MEM-OBJ-conversation-history](#mem-obj-conversation-history), [MEM-OBJ-helper-history](#mem-obj-helper-history), [MEM-RTE-session-history](#mem-rte-session-history) |
| Console startup/flags and settings reload | Direct: `src/jaz/console.py` settings loader, flag hook builder, model writer and readline setup; `src/jaz/user_settings.py` loader/policy | [MEM-OBJ-user-settings](#mem-obj-user-settings), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change). Bare console flags do not install ATIF replay or rollout collection; `--log` installs FileLogger and `--trace` JaegerTracing |
| Credentials and command recall | Direct: resolver/writer in `src/jaz/credentials.py`; readline setup in `src/jaz/console.py` | [MEM-OBJ-credentials](#mem-obj-credentials), [MEM-RTE-credential-access](#mem-rte-credential-access); readline reload is human command recall, not agent transcript rehydration |
| ATIF recording, failure retention, setup/teardown and replay loading | Direct: `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py` | [MEM-OBJ-atif-trace](#mem-obj-atif-trace), [MEM-RTE-trace-recording](#mem-rte-trace-recording); [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) annotated and qualified below |
| Workflow emission and standalone entry blocks | Supplied runtime inspection of `src/jaz/hooks/builtin/workflow_replay.py` | [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission); not independently re-audited here; arbitrary-object reconstruction/equivalence remains unresolved |
| Token-native messages, hidden reasoning and rollout alternatives | Direct: `src/jaz/llm/sglang.py` stamp preparation, response finalization and transport; `src/jaz/hooks/builtin/rollout.py` collection/export | [MEM-OBJ-rollout](#mem-obj-rollout), [MEM-RTE-rollout-export](#mem-rte-rollout-export); sidecar representation separated from visible text |
| Weight loading, distributed/tensor update, pause/resume and GPU-memory release | Direct: `src/jaz/llm/sglang.py` exposed methods | [MEM-RTE-weight-transport](#mem-rte-weight-transport); no supplied trainer or parameter artifact links rollouts to updates |
| Live directory, ATIF batch directory and textual-log conversion | Direct: `src/jaz/hooks/builtin/trajectory_directory.py` format contract/helpers, `src/jaz/utils/trace_to_directory.py` dispatch, `src/jaz/hooks/builtin/loggers.py` FileLogger setup, `src/jaz/utils/log_to_markdown.py` converter | [MEM-RTE-trace-display](#mem-rte-trace-display); detailed event formatting and all malformed-input cases not exhaustively audited |
| Remote telemetry | Direct: `src/jaz/hooks/builtin/otel_tracing.py` exporter setup/attribute formatting; symbol search in `src/jaz/hooks/builtin/jaeger_tracing.py` and `src/jaz/hooks/builtin/langfuse_tracing.py` | OTel exporter wiring is inspected; remote retention, query consumers, backend-specific defaults and complete event payloads remain uninspected. Prevents classifying telemetry as a future-agent memory route |
| Git diff extraction utility | Scoped source search: `src/jaz/utils/extract_git_diff.py` extracts a config field and writes a file | Diagnostic conversion only; detailed parser uninspected, no claim of evaluator/adoption consumer |
| Evaluation/rejection/cleanup | Recorder failure branches, rollout stand-down/export checks, replay divergence and loader, settings-policy rejection directly inspected; return validation supplied by runtime | Failed traces can survive. No supplied evaluator, deployment run or training loop establishes quality-based memory promotion; this is an evidence limit, not an absence inferred from missing runs |

## Core ideas

1. **Keep objects outside the prompt and expose a bounded display.** Console history keeps live prior inputs/results, but renders capped reprs as an index. A later agent can inspect those objects through its REPL. The helper instead receives text transcripts, so it cannot recover the opaque live payload through that channel. See [MEM-RTE-session-history](#mem-rte-session-history).
2. **Separate current-window control from durable memory.** Input/observation abbreviation, fresh recursive contexts and transient hook messages shape the current window. Persistent hook edits alter the current loop's carried buffer; this persistence flag alone is not cross-invocation storage. See [MEM-RTE-context-selection](#mem-rte-context-selection).
3. **A trace can later supply actions rather than advice.** ATIF replay selects saved assistant responses by invoke frame/cursor and feeds the normal execution pipeline. It is not restoration of Python objects or proof of environmental equivalence. Optional divergence checks have material blind spots and a sequential-nesting assumption. See the annotation on [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay).
4. **Training material is not a trained successor.** Token sidecars retain full generations even when visible reasoning is stripped. Rollout exports construct masked samples, and separate methods can request server weight updates. No shipped evidence joins those surfaces into an evaluated update loop. See [MEM-RTE-rollout-export](#mem-rte-rollout-export) and [MEM-RTE-weight-transport](#mem-rte-weight-transport).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-conversation-history
Label: ConversationHistory

A session-owned Python list of ConversationTurn objects retains typed prompt text, interpolation-expression-to-live-object bindings, native results or exception objects, target name and error flag. It is not the invocation's message buffer or REPLState: closest supplied records are [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer) and [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state), which end at a different lifetime and consumer boundary. No supplied declaration identifies this separate session container.

The live bindings and structured fields have symbolic access semantics; the prompt/transcript strings have natural-language interpretation semantics. Arbitrary retained results can be opaque host objects: their repr is a lossy display, not a serialization or a fixed representation class for their internals. Original user input and agent result/exception provenance remain separate fields. No summary model or semantic curation is involved. The source caps per-value transcript reprs at 500 characters but retains all turns and pins their objects; protocol input rendering can further abbreviate the entire description. Later agents receive the live history as an ordinary explicit input. SRC-1, `src/jaz/console.py`:

> Once it has a turn, every prompt turn's invoke receives it as the
> ``conversation_history`` input: it renders as a truncated transcript in the prompt and
> binds as this live object in the agent's REPL, so the agent can inspect a previous
> turn's actual inputs/result rather than a repr.
> --- `src/jaz/console.py`

#### MEM-OBJ-helper-history
Label: HelperHistory

A distinct session list of HelperExchange objects holds request, answer/code tag, content and applied flag. Symbolic tags/status support transcript formatting; retained answer/snippet strings are interpreted by the next helper, not automatically executed from history. Each exchange's content display is capped at 4000 characters. The helper receives rendered main and helper transcripts, not main live result objects. Human rejection of a code snippet is remembered as shown/not run, rather than deleting the proposal. This is distinct from [MEM-OBJ-conversation-history](#mem-obj-conversation-history); [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) is its closest supplied consumer, not a duplicate object declaration. SRC-1, `src/jaz/console.py`:

> class HelperExchange:
>     """One ``%`` exchange: the request and how the helper replied.
>
>     ``kind`` mirrors the helper's response tag (``"answer"`` or ``"code"``); ``applied``
>     is ``None`` for an answer, else whether the user confirmed the snippet to run.
> --- `src/jaz/console.py`

#### MEM-OBJ-atif-trace
Label: ATIF trajectory document

This JSON artifact is distinct from [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer) and is the retained input to [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay). It groups raw conversation text with derived event/metric/provenance metadata and display-only namespace summaries. Conversation text includes interpreted instructions/observations and code-bearing assistant responses. Response code has symbolic execution authority only at the replay consumer. Message IDs, indices, iteration, persistence, parent/child structure and accounting fields are symbolic access/lineage metadata, not knowledge content or correctness judgments.

The recorder's in-process state precedes optional filesystem JSON. Scope and committed explicit inputs are shallow binding snapshots; mutable nested objects can change before teardown serialization. Input/scope/result payloads become type names plus at most 10000 leading repr characters, not object checkpoints. ATIF records message-edit additions and drop coordinates, including persistent and transient edits, separately from raw conversation steps. Added message text can be a host-supplied summary, but recording it does not establish a summarizing implementation. Source-dependent trust remains with the producing model/hooks/caller; lineage labels do not authenticate truth. SRC-1, `src/jaz/hooks/builtin/atif_trace.py`:

> Each value becomes ``{"type": <class name>, "repr_prefix_10000": <repr, truncated>}``.
> --- `src/jaz/hooks/builtin/atif_trace.py`

> if state.children:
>     atif["subagent_trajectories"] = [
>         self._build_atif(child) for child in state.children
>     ]
> --- `src/jaz/hooks/builtin/atif_trace.py`

#### MEM-OBJ-rollout
Label: Rollout and token samples

Rollout is an in-process frozen trajectory view over per-turn TurnRecord/TokenStamp data. Symbolic token IDs, sampled spans, masks, logprobs, model label and optional weight-version metadata differ from readable assistant text and from distributed model weights. Logprobs are numerical measurements, not themselves a learned dense memory. The object is distinct from [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer): it retains exact backend token-side data, including hidden reasoning omitted from visible messages. Its conversion methods expose dictionary/sample exports; a trainer is a documented prospective consumer, not supplied deployed wiring.

Lineage is backend-produced sent/sample records from query events, annotated with Agent iteration and invocation outcome by the recorder. The backend's declared model label need not identify the server's actual loaded model. Partial failures remain filterable; a token-less completed query instead discards that invocation's accumulated token log. SRC-1, `src/jaz/hooks/builtin/rollout.py`:

> Invokes whose backend produced no turn records (text backends, replay
> overrides) yield no rollout — a warning is logged once per invoke.
> --- `src/jaz/hooks/builtin/rollout.py`

#### MEM-OBJ-user-settings
Label: User settings JSON

Symbolic configuration in `~/.jaz/settings.json` persists console-selected backend/model and any authored configuration groups. It is distinct from model weights in [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend); its consumer selects/builds Python components and their settings. Closest supplied route is [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), not a duplicate object. Source lineage is manual file authorship or console persistence, not automatic trace learning. Human authorship of arbitrary existing files is not verified; subsequent programmatic model persistence is software I/O after the console action.

The console loader admits parsed JSON after policy and component checks. It rejects persisted `llm.base_url`/`llm.api_key`, warns rather than rejects sandbox-loosening settings, and runs before CLI flag overrides. Library import does not load it. Removal/edit is manual recovery; model persistence preserves other settings, so validation of the newly selected component does not certify all next-startup defaults. SRC-1, `src/jaz/console.py`:

> The persistent settings file is **console-scoped**: it is an ambient baseline for the ``jaz``
> console, NOT for library ``import jaz`` (which stays fully determined by its call site, so code
> written on top of jaz is portable and cannot be broken by a file in someone's home directory).
> --- `src/jaz/console.py`

#### MEM-OBJ-credentials
Label: Credentials JSON

Provider/field-to-string mappings in `~/.jaz/credentials.json` are symbolic access credentials. They authorize provider requests through backend resolution, not model knowledge or task memory. This has no supplied object counterpart; [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) is the consumer machinery. The private writer stores caller-supplied values and preserves unrelated entries; no model-generated provenance is established for keys. It refuses malformed existing JSON and empty provider/value. The documented mode is owner-only storage with atomic per-write replacement, not serialization of concurrent read-modify-write operations. Rotation/deletion is manual file editing. SRC-1, `src/jaz/credentials.py`:

> There is no remove/list counterpart yet: rotate or delete a key by editing the JSON file
> at :func:`credentials_path` directly.
> --- `src/jaz/credentials.py`

### Routes

#### MEM-RTE-session-history
Label: Session history admission and delivery

After each console prompt invocation, chat records its request/interpolated inputs and result or raised BaseException, then returns/re-raises. The next prompt automatically supplies the accumulated main history if nonempty. Helper requests separately render both transcripts and record helper replies including denied snippets. The console owns selection/delivery; model code chooses whether and what to inspect from the live object. This is distinct from the bare invocation in [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop); it extends the cross-call retention described in [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), without duplicating that proposal-execution route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Main result/exception or helper response; histories append independently of task success.
- Later read-back: Next main invoke receives ConversationHistory by explicit input plus rendered description; helper receives strings of main/helper transcripts.
- Delegated visibility: Main agents may explicitly pass reachable retained objects to children; fresh child frames do not inherit the whole transcript automatically. Helper text-only input cannot expose the original object's methods through that channel.
- Selection predicate: Nonempty history at each prompt; transcript covers oldest-first turns with per-value caps, not query relevance or a last-N policy. Helper content has its own cap; protocol rendering may further shorten inputs.
- Invalidation or expiry: New namespace creates new empty histories. Session objects remain referenced while history lives; reassigning the visible history name does not replace the chat closure's retained object. No durable session-object reload is established.
- Activation or effect: Wired prior-turn delivery and optional programmatic object inspection; actual model reliance or better answers unobserved.
- Evidence limits: Live objects can mutate; historical result displays are not immutable snapshots. Caps do not bound turn count or guarantee relevant material reaches the model.

Admission is automatic software append, not per-entry human approval or truth review; user prompt authorship and model result authorship are distinct from the console writer. Operating mode is open conversation, with no expected-answer oracle or quality promotion trigger. Rejection/withdrawal is not built into this append path; a rejected helper action remains historical evidence and acquires no execution authority merely by being remembered. SRC-1, `src/jaz/console.py`:

> except BaseException as exc:
>     # Recorded, THEN re-raised: a failed turn is part of the conversation ("why
>     # did that error?"), and the exception object itself is the inspectable
>     # result. Ctrl-C included — an aborted turn is likewise worth remembering.
>     history.record(prompt, inputs, exc, target=_target, error=True)
>     raise
> --- `src/jaz/console.py`

#### MEM-RTE-context-selection
Label: Window shaping and history access

The protocol abbreviates rendered inputs and Continue observations; hook effects select drops/additions by message position. This adds specific context-control mechanisms to [RT-RTE-hook-control](runtime.md#rt-rte-hook-control), rather than replacing that broader admission route. Runtime owns the fold; hook authors own selection policy. ContextWindowWarning is a concrete automatic addition: it uses last completed prompt-token count divided by effective model input capacity, then emits caller-supplied text transiently when the configured fraction is reached. It neither removes turns nor creates a summary. SRC-1, `src/jaz/hooks/builtin/context_window.py`, `src/jaz/protocol/code_only.py`, `src/jaz/_agent.py`, `src/jaz/hooks/effects.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bounded opener/observation strings and the final selected provider-facing message list.
- Later read-back: inapplicable — these are current-loop controls; cross-call history delivery and trace replay are separate routes. Hook edits may be recorded into ATIF for later inspection/comparison, not automatically replayed as future summaries.
- Delegated visibility: Recursive invocation creates a fresh frame containing selected explicit inputs and ambient scope; parent transcript is kept out. Native results/exceptions return; explicit return of history can expose more. Shared references defeat process-isolation interpretations.
- Selection predicate: Defaults are 50000-character per-input/per-output ceilings with 0.5 head/tail ratio; hooks select event-snapshot indices and insertion slots. Warning threshold uses previous query usage, not a current prompt reservation; unknown capacity/usage yields no warning.
- Invalidation or expiry: Transient edits affect one query; persistent edits alter the carried buffer for later turns of that invoke. Abbreviated middle text stays reachable in full CodeOnlyProtocol history for Continue output, subject to the REPL providing full output. Frames stop advancing on completion; escaped values can remain reachable.
- Activation or effect: Wired message omission/insertion and programmatic history access. Prompt presence is not model compliance; no automatic global context-budget optimizer is established.
- Evidence limits: Input and output limits are character ceilings, not total-window token budgets. Truncation may remove error text. A custom protocol/REPL or host hook can change these semantics; external host compaction remains uninspected.

Proposals/admission here are computational: installed hook code emits edits, and the fold accepts valid coordinates or raises for invalid indices. No per-message human gate is established. Authors can supply instructions or summary text, but the generic edit seam carries no semantic evaluation, summary rationale or rollback archive; restoring removed text requires another holder, such as history or traces, and an explicit delivery operation. Working-context isolation resembles a call frame: selected inputs enter and a native result escapes. The analogy stops at shared host references and accessible history; message text is not automatically a dereferenceable pointer to evicted material.

> persistent: ``False`` (default) applies the drop to this turn's message list only;
>     ``True`` makes the drop survive into later turns.
> --- `src/jaz/hooks/effects.py`

> return [AddMessages([{"role": "user", "content": self.warning_text}])]
> --- `src/jaz/hooks/builtin/context_window.py`

#### MEM-RTE-trace-recording
Label: ATIF trace retention

An installed TrajectoryRecorder maps Invoke/LLM events into per-invoke trajectory state; teardown optionally writes JSON. This is distinct from [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), which reads the artifact, and from [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission), which emits executable programs. SRC-1, `src/jaz/hooks/builtin/atif_trace.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Observer emits no result override; get_trajectories builds documents mid-run or after scope.
- Later read-back: Selected JSON supplies TrajectoryReplay; trace_to_directory consumes JSON for human-readable files. get_trajectories alone is an exposed storage read capability, not a specified future-agent route.
- Delegated visibility: Recorded child trajectories nest under the parent when the hook observes both; local activation and propagating activation differ as described by runtime hook scope.
- Selection predicate: Active hook event stream, committed post-add/drop input bindings, seed/assistant/observation messages, separate hook-edit records and metrics; no task-success filter.
- Invalidation or expiry: No-path activation clears state on next setup, not teardown; path-configured instances forbid reactivation to avoid replacing their own prior output. Files persist until external replacement/deletion; a separately constructed writer is not proved unable to overwrite the same path.
- Activation or effect: Wired trace production; downstream behavior depends on the separate replay consumer. Failure/abort records remain, not automatically approved recipes.
- Evidence limits: Teardown file writing is not a crash-durable checkpoint of a live namespace. Shallow snapshots and capped reprs prevent full input/result reconstruction; remote effects are not restored or rolled back.

Write admission is automatic event serialization after caller hook activation. Caller choice of output path is not per-content human approval. Raw messages and metadata are not semantically curated knowledge; original response text can retain code/comments, but there is no separately required reason-for-edit field. Source policy retains failed/aborted state rather than rejecting it:

> # Non-completed arms (#892 outcome union) carry no terminal result — record the
> # outcome and its exception instead; the per-invoke state is kept, so teardown still
> # writes everything traced up to the failure, now labelled with how it ended.
> --- `src/jaz/hooks/builtin/atif_trace.py`

#### MEM-RTE-rollout-export
Label: Token rollout collection and sample export

SGLang constructs full token records, RolloutRecorder admits query token truth and freezes records on invoke exit, and caller-selected conversion methods build flat, piecewise or per-turn training samples. Closest supplied records are [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) and [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer); this distinct route produces training material rather than model responses or an ordinary prompt buffer. SRC-1, `src/jaz/llm/sglang.py`, `src/jaz/hooks/builtin/rollout.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: In-memory rollouts and exports of token sequences, loss masks, logprobs and terminal metadata; no trained model return.
- Later read-back: Documented trainer role can consume exported samples; shipped trainer invocation and durable sample persistence are uninspected/unavailable in this distribution. This is an afforded external consumer, not a demonstrated learning loop.
- Delegated visibility: Rollouts are demultiplexed by invoke_id and collected separately in completion order. Child token history does not automatically become parent prompt content.
- Selection predicate: Completed query with actual backend token records; no local retokenization substitute. Token-less completed query stands the invoke down and drops its partial log. Failed query preserves earlier usable turns. to_flat rejects nonmonotone histories; to_pieces splits at context breaks; to_turn_samples exposes each actual conditioning/sample pair.
- Invalidation or expiry: Recorder setup clears prior activation state. Exports are caller-held values; no supplied checkpoint/reload/trainer retention policy. Weight-version metadata labels samples when provided; it does not pin or restore weights.
- Activation or effect: Wired trace-to-sample transformation; trainer consumption and resulting capacity changes unobserved.
- Evidence limits: Per-turn masks and token records do not establish rewards, correctness or optimizer behavior. finished is a terminal-outcome marker, not task success certification.

The software decides token admission and export shape, with no per-sample human approval or answer oracle. The documented operating mode is rollout/training support. Nonmonotonicity rejection prevents one misleading export shape, not all exports or the original run. Hidden reasoning is deliberately excluded from visible content but retained in full sampled IDs and content_text; on subsequent sends, content mismatch forces a fresh rendering of stripped text. This supplies a counterexample to treating visible transcripts as all retained model output. No built-in summary replaces the stripped reasoning.

> if stamp is not None and stamp.content_text == content:
>     stamps.append(stamp)
> --- `src/jaz/llm/sglang.py`

> visible = content
> if self._reasoning_closed is not None and self._reasoning_open is not None:
>     visible = self._reasoning_closed.sub("", visible)
>     visible = self._reasoning_open.sub("", visible)
> --- `src/jaz/llm/sglang.py`

> Raises :class:`~jaz.exceptions.NonMonotoneRolloutError` if any turn's context was
> not a pure extension of the previous one — routine for reasoning models under
> ``SGLangLLM``'s hidden-trace interface (multi-turn rollouts are non-monotone by
> design there), or after a transient nudge, compaction, or edit — use
> :meth:`to_pieces` or :meth:`to_turn_samples` then.
> --- `src/jaz/hooks/builtin/rollout.py`

#### MEM-RTE-weight-transport
Label: Server weight-update transport

SGLang exposes HTTP methods for loading weights from disk, tensors or a distributed group, plus pause/continue generation and release/resume GPU occupation. This is a distinct library-operation capability beside [RT-RTE-settings-change](runtime.md#rt-rte-settings-change): changing serving parameters is not changing a symbolic model name. It concerns the backend represented by [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend), not a new local learned component. SRC-1, `src/jaz/llm/sglang.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Server JSON response or None for a non-JSON response, with mapped HTTP/transport errors.
- Later read-back: uninspected — no shipped caller links a produced weight artifact to subsequent generation; server methods afford changing the weights future requests use, but the server and trainer are not frozen evidence.
- Delegated visibility: inapplicable — methods act on the backend's configured server; no child-agent weight namespace or isolation protocol is established.
- Selection predicate: External caller supplies model_path/options or weight payload; these wrappers do not select traces, judge candidates or compute updates.
- Invalidation or expiry: Server-side lifetime, rollback and cache invalidation are uninspected. Pause/resume and GPU release/resume are transport requests, not evidence of durable memory checkpoints.
- Activation or effect: Afforded parameter replacement with external server contract; no observed update, consumption or improvement.
- Evidence limits: Model weights are external distributed-parametric state; exact version is not pinned by JAZ. Model label can misidentify the server policy; sampled weight_version is optional attribution metadata, not artifact identity validation.

Admission at this boundary is caller-chosen request plus HTTP success handling; human approval, optimizer decision, rejection objective and recovery are external/uninspected. The comment names a trainer operating between batches but supplies no implementation of its guidance, reward oracle, update rule or rollback. Thus automatic trace retention/export and weight-loading methods cannot be joined into a claimed autonomous learning route.

> def update_weights_from_disk(self, model_path: str, **options: Any) -> Any:
>     """Load fresh weights from ``model_path`` into the serving engine."""
>     return self._post(
>         "update_weights_from_disk", {"model_path": model_path, **options}
>     )
> --- `src/jaz/llm/sglang.py`

#### MEM-RTE-trace-display
Label: Trace display conversion

This route groups observer/converter writes with human-readable diagnostic consumers, not replay authority. It differs from [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission): fenced code in Markdown is not a generated program entry block. SRC-1, `src/jaz/hooks/builtin/trajectory_directory.py`, `src/jaz/hooks/builtin/loggers.py`, `src/jaz/utils/trace_to_directory.py`, `src/jaz/utils/log_to_markdown.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Live trace/overview directory, textual event log, batch Markdown/directory output or stdout.
- Later read-back: Explicit trace_path/log_file_path request reads retained files into batch converters; human browsing is documented. No inspected automatic agent-memory injection from these displays.
- Delegated visibility: Directory layout separates each agent's conversation and links child nodes; converters do not automatically expose child content to running parent models.
- Selection predicate: Live recorder selects newly seen messages and separate hook-edit events; overview snippets are short displays. ATIF batch converter defaults to the first root, with all_nodes/--all for all roots; log conversion extracts parsed message lines rather than arbitrary full event payloads.
- Invalidation or expiry: Files remain subject to external edits/deletion; detailed live writer collision/reuse behavior uninspected. Conversion cannot recover content already truncated by its producer.
- Activation or effect: Wired diagnostic materialization and requested file consumption; human/model behavioral reliance unobserved.
- Evidence limits: No semantic evaluation or task-correctness admission gate established. Full log/directory event formatting and every conversion variant were not audited; this does not establish a lossless checkpoint.

Event/converter software admits selected trace text automatically after invocation. This is raw-to-display transformation, not meaning-changing synthesis. Reasons survive only insofar as source content includes them; snippets and parsed message subsets can omit them. Human browsing is interpretive authority, not automatic code execution. The batch converter's root selection is explicit:

> nodes = nodes if all_nodes else nodes[:1]
> --- `src/jaz/utils/trace_to_directory.py`

#### MEM-RTE-credential-access
Label: Credential persistence and request resolution

The console's supported credential action passes values to the private JSON writer; opted-in backends resolve a provider field for requests. Distinct from [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), which persists configuration but not API keys. SRC-1, `src/jaz/credentials.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Writer returns a location string; resolver returns a nonempty string or None, or raises for malformed storage.
- Later read-back: Resolver reloads stored credentials; LiteLLM resolution is documented per request, OpenAI/Anthropic construction-time resolution is documented. Adapter details beyond this resolver contract were not independently audited here.
- Delegated visibility: Credential effects follow whichever backend resolves them; not injected as task-history knowledge or automatically inherited message content.
- Selection predicate: Explicit provider and field lookup; non-string/empty value is treated as absent.
- Invalidation or expiry: Manual rotation/deletion of JSON; already constructed adapter caches may not refresh immediately. Concurrent writer serialization is not guaranteed.
- Activation or effect: Wired access-authority storage/lookup, with provider authentication and operational success external/unobserved.
- Evidence limits: Original key source and human approval for every programmatic writer call are unresolved; filesystem policy is not a complete secret-management audit.

Admission rejects empty inputs and malformed prior storage; write agency is software called by the console action, not semantic learning. No task-answer oracle or improvement mode applies. Backends must opt into this store:

> A custom
> backend that never calls it will not read a key stored under its tag.
> --- `src/jaz/credentials.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-message-buffer](runtime.md#rt-obj-message-buffer)

Memory-specific evidence: SRC-1, `src/jaz/_agent.py` directly confirms persistent edits affect only the carried buffer and provider projection strips unconsumed sidecar keys. Natural-language content influences the model through interpretation; provenance/token metadata are not automatically text in its prompt. Persistent does not mean serialized across calls. There is no summary producer inherent in the edit fold; a caller hook must supply content. [MEM-RTE-context-selection](#mem-rte-context-selection) records the context controls.

#### On [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state)

The default history builder retains full response content, full Continue output and raw recoverable exception objects, but terminal Return/Raise entries carry empty output and no exception in that field. Thus “full REPL output” must be scoped to Continue rather than a claim that terminal stdout/value/exception are checkpointed there. SRC-1, `src/jaz/protocol/code_only.py`:

> ``repl_output`` is always a ``str``: the REPL ``output`` for a ``Continue``, and ``""`` for
> a terminal ``Return``/``Raise`` (which carry no ``output`` at all).
> --- `src/jaz/protocol/code_only.py`

History is addressable to agent code even when the observation is abbreviated, but the inspected default observation emits no recovery advice. Model awareness or successful recovery is not established. History can escape explicitly as a returned reference; it is not automatically a next-invocation transcript.

#### On [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay)

The retained input is [MEM-OBJ-atif-trace](#mem-obj-atif-trace). The loader builds per-node response arrays from agent steps and child arrays from stored child order. It retains responses/metrics and expected observation/edit signatures, not arbitrary original Python objects. Observation matching prefers all provenance-tagged observation user steps, falling back to positional first-user only when no tagged observations exist. Replay supplies saved responses; it compares saved edits but does not automatically apply a saved compaction policy to the live buffer. SRC-1, `src/jaz/hooks/builtin/replay.py`.

The supplied route's per-invoke queue account needs a **sequential-nesting qualification**. on_llm_query_send selects the top of one invoke stack, not an event-invoke-ID lookup. Concurrent sibling calls can therefore receive another sibling's response or divergence latch. This is not a hypothetical deployment isolation finding: source explicitly records the implementation limitation:

> # SEQUENTIAL INVOKES ASSUMED. ``_invoke_stack`` is one stack whose TOP is "the active
> # invoke", which holds only while invokes nest strictly in time. ``ainvoke`` advertises
> # concurrent execution via ``asyncio.gather``, and under it the top at any event need not be
> # the invoke that raised it — so a query can be served from a sibling's queue and a
> # difference in one invoke can latch another's ``diverged``.
> --- `src/jaz/hooks/builtin/replay.py`

Source trust is caller-selected file content plus structural parsing, not an authenticity or task-correctness gate. Multi-root input is rejected, including arrays with more than one root. Default divergence detection is false. When enabled it does not compare seed system/task/input rendering; detected response/output divergence does not undo already committed turns/effects. Post-transform saved responses can be transformed again. Source's warning supplies the counterexample to a stronger safe-cache interpretation:

> No comparison looks
> at the *seed* prompt, so re-running a trace under a changed system prompt, task template, or
> inputs rendering reports no divergence.
> --- `src/jaz/hooks/builtin/replay.py`

#### On [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission)

The supplied source passage establishes automatic trace-to-symbolic-program emission, including partial failed runs, not quality-selected procedural knowledge. This is a separate behavior-shaping derivative of execution content: model-authored code/events → generated functions and entry blocks → afforded standalone Python executor. Comments/reasons can survive if present in selected code, but no retained justification requirement or later reason reader is established. Output-directory files persist across sessions; automatic adoption into later Agent invocation is not established. Code-edit-hook mismatch and arbitrary object binding remain limitations from the supplied record; no direct re-audit was performed here. SRC-1, `src/jaz/hooks/builtin/workflow_replay.py`; source passage in the cited record.

#### On [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)

Retained user settings give later console startup symbolic configuration authority, whereas the helper's retained exchanges give its next invocation natural-language context. These are separate consumers with separate human gates. Current/main/helper transcripts do not bypass snippet confirmation by existing in history. Direct inspection adds loader policy: `base_url`/`api_key` blocked; sandbox policy changes warned but permitted; manual repair for malformed settings; flags override startup file. SRC-1, `src/jaz/user_settings.py`, `src/jaz/console.py`; [MEM-OBJ-user-settings](#mem-obj-user-settings).

#### On [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend)

Direct SGLang inspection adds an exposed parameter-change capability, not evidence that parameters actually change during a run. The class has weight-loading methods; model parameter substrate and exact weights remain external/unpinned. Its `model` is a chat-format/record label rather than a server selection request. Optional sampled weight_version cannot close that identity gap. [MEM-RTE-weight-transport](#mem-rte-weight-transport) and [MEM-RTE-rollout-export](#mem-rte-rollout-export) keep loading capability, trace attribution and learning evidence separate. SRC-1, `src/jaz/llm/sglang.py`:

> # The model id is never sent: `/generate` takes `input_ids` and serves whatever the server
> # was launched with. It only picks the default chat format (`HFChatFormat(model)`) and labels
> # the record, so a wrong id is not a request that fails — with `chat_format` set explicitly
> # it is a mislabelled `TurnRecord` and nothing else.
> --- `src/jaz/llm/sglang.py`

## Write side

- **Session acquisition:** console code automatically appends user requests and model/native results, including exceptions. Neither prompt authorship nor physical append establishes human review of each retained result. Main history keeps objects, helper history keeps response strings/status; no claim synthesis occurs. Rejection of a helper snippet affects execution admission, not retention. See [MEM-RTE-session-history](#mem-rte-session-history).
- **Current-context transformations:** protocol abbreviation and hook edits alter what is shown. Persistent drops/additions can implement host compaction, but source text for an edit seam is not a source-grounded summarizing policy. Original text may remain in history/ATIF; its availability does not prove a model knows to reload it. Reasons for edit decisions are not a required effect field. See [MEM-RTE-context-selection](#mem-rte-context-selection).
- **Trace derivatives:** execution → ATIF is raw-text retention with metadata/display conversion; execution → WorkflowReplay is program materialization; query token truth → Rollout exports is sample/mask construction. Only the latter two produce additional machine-consumable structures, and only workflow output has a documented standalone execution affordance. None establishes improvement by itself. Failed/aborted content can survive. See [MEM-RTE-trace-recording](#mem-rte-trace-recording), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission), [MEM-RTE-rollout-export](#mem-rte-rollout-export).
- **Rejection and cleanup:** replay rejects unsupported root/alignment shape or falls live after exhaustion/detected divergence; this is compatibility control, not correctness evaluation. Rollout collection rejects token-less completed data and flat export rejects nonmonotone shape while other forms remain available. In-memory recorder reuse clears prior scope state; filesystem deletion/rollback is external. No-path ATIF state survives teardown for post-scope reads, while a live directory writer is a different partial-failure retention form. These are not interchangeable restart checkpoints.
- **Configuration/access:** console actions or file authors produce settings/credentials; loaders/writers apply structural/policy admission, not semantic task review. Helper code needs human confirmation as recorded in runtime, while a settings file is not per-startup approval. SGLang update wrappers merely transmit external caller-selected updates. Original weight provenance, optimizer and server admission remain unresolved. See [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), [MEM-RTE-credential-access](#mem-rte-credential-access), [MEM-RTE-weight-transport](#mem-rte-weight-transport).

## Read-back

The shipped cross-invocation consumers are explicit:

| Retained part | Trigger, selector and delivery | Consumer authority / limit |
|---|---|---|
| Main session objects and their display | Every subsequent prompt automatically receives nonempty history; all turns with capped reprs; later code can index objects | Model interprets display and chooses inspection; REPL reads native references, not reconstructed repr payloads. [MEM-RTE-session-history](#mem-rte-session-history) |
| Main/helper text transcripts | `%` request builds text snapshots; per-entry caps and helper input budget | Helper interpretation only; prior proposed code is not automatically host-executed. [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) |
| ATIF saved responses | Caller requests trace by path; query trigger chooses stack frame/cursor; no semantic relevance budget | Response supply leads to symbolic code execution under normal hooks/REPL policy. Seed mismatch and concurrency limit safe correspondence. [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) |
| Workflow program | Caller later runs emitted entry blocks; no demonstrated automatic Agent installation | Afforded native program execution; failure content and binding mismatch can persist. [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) |
| Rollout samples | Caller chooses flat/pieces/turn export; documented trainer consumer | Training-use affordance, not evidence of deployed optimization or later model dependence. [MEM-RTE-rollout-export](#mem-rte-rollout-export) |
| Settings JSON | Console startup parses policy-checked file before CLI overrides | Symbolic configuration controls session components, not library import. [MEM-OBJ-user-settings](#mem-obj-user-settings) |
| Credentials JSON | Opted-in provider lookup on request/construction | Authentication input, not prompt knowledge. [MEM-RTE-credential-access](#mem-rte-credential-access) |
| Logs and directories | Explicit batch-conversion request or human browsing; first-root default in ATIF converter | Interpretive diagnostic display; no inspected automatic agent ingestion. [MEM-RTE-trace-display](#mem-rte-trace-display) |

The readline file is another retained input, but its consumer is interactive command recall: `read_history_file`, a 1000-entry history limit and an atexit writer. It is not restoration of ConversationHistory live objects. SRC-1, `src/jaz/console.py`:

> readline.set_history_length(1000)
> atexit.register(readline.write_history_file, history_file)
> --- `src/jaz/console.py`

Current-loop `__history__` access and fresh recursive frames are described separately from read-back. API storage methods without a later specified consumer are not promoted into retrieval routes. No inferred vector search, relevance-ranked long-term store or full namespace checkpoint is needed to explain the inspected routes; this report does not claim a repository-wide absence of every custom implementation.

## Integration issues

1. **Replay concurrency qualification:** [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) says child queues do not consume the parent's/sibling's next response. This holds for the assumed sequential nesting, not concurrent siblings. SRC-1, `src/jaz/hooks/builtin/replay.py`, top-of-stack query selection and explicit limitation quoted above. Reconciliation should retain the implemented replay route while qualifying its queue-isolation claim; unconditional isolation would misstate read-back selection and behavioral authority.
2. **History output scope:** [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state) describes full output/exception history without distinguishing terminal turns. The direct builder passage above establishes Continue-only full output and recoverable exception, with empty terminal fields. This limits checkpoint/reconstruction conclusions; it does not negate live namespace/history access.
3. **Additional model-mutability surface:** [RT-CMP-model-backend](runtime.md#rt-cmp-model-backend) remains a valid broad component; SGLang's inspected weight transport and unverified model label add detail absent from its LiteLLM-centered account. [MEM-RTE-weight-transport](#mem-rte-weight-transport) is a distinct exposed operation, not a duplicate component or proof of online learning.
4. **External trainer/server link unresolved:** [MEM-RTE-rollout-export](#mem-rte-rollout-export) and [MEM-RTE-weight-transport](#mem-rte-weight-transport) have no supplied trainer, persisted parameter artifact, objective/evaluator or observed subsequent operation connecting them. Prevents attribution of learned successors or improved future capacity, while preserving sample construction and weight-loading affordances.
5. **Telemetry and diagnostic scope unresolved:** remote retention/read-back and full event-format coverage remain limited as the inventory states. [MEM-RTE-trace-display](#mem-rte-trace-display) supports local diagnostic conversion, not a complete external service lifecycle or future-agent consumer claim.
6. **Workflow equivalence unresolved:** [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) already retains code-edit-hook/object-binding limits; this report relies on that supplied inspection and cannot certify standalone equivalence or success-based admission.

No new record is proposed as a duplicate of a supplied declaration. Existing message/state/backend/replay/workflow/settings referents are annotated. New declarations identify separate session containers, retained artifacts or specific mechanisms and compare the closest supplied records locally. Context selection overlaps the generic hook-control route but names specific window-shaping operations; trace production is not trace consumption.

## Limitations and checks

This is static implementation/doctrine evidence under SRC-1, not observed operation or causal benefit. Model compliance, external services, trained parameters, workflow equivalence and actual application grants remain unobserved or external. Full telemetry adapters, every utility/parser branch and all diagnostic event formatting were not audited; their inventory limits prevent stronger claims rather than silently excluding shipped paths.

Source identity and clean frozen HEAD were rechecked. The complete supplied invocation, types, boundary, runtime, collection, worker rules and record contract were read; bounded-range reads recovered the supplied runtime tail. The report uses only assigned source/member evidence and does not add source IDs, execute the target or modify peer reports.

Validation result: deterministic validate-output passed for this invocation; this checks content form, citations and quotation occurrence, not semantic acceptance or operational success.
