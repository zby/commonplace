---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "JAZ memory: live console objects, trace replay, generated workflows and token-native rollout export at the frozen release."
run-id: AAS-2026-10-19-jaz-9d991c410bb9-01
source-identity: "https://github.com/jaz-lang/JAZ"
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
---

# JAZ memory report

## Boundary and evidence

The subject is the shipped JAZ package, including its console. The frozen source is SRC-1 at the revision above, as registered in [boundary](boundary.md#source-register). Memory scope follows the runtime's invocation, console, context-control, replay, workflow and settings routes. It also includes the registered token-native rollout recorder and SGLang service operations, which the provisional runtime did not trace. Static prompts and ordinary invocation state are context surfaces, not automatically later-invocation memory. External trainers, provider internals and telemetry collectors remain outside the boundary; their results and retention policies cannot be established here.

All new findings use implementation text or attributed source documentation within SRC-1. No target execution, provider call, run trace or experiment supplies operation or benefit evidence. Direct source reads added the paths below; supplied runtime findings remain explicitly distinguished.

| Entry point or operation | SRC-1 source path | Coverage and limits |
|---|---|---|
| Invocation namespace, recursive isolation and return | `src/jaz/invoke.py`, `src/jaz/_invoke_tool.py`, `src/jaz/repl/python_repl.py` | Supplied [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state), [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke); not independently reread end to end. |
| Observation/history projection | `src/jaz/protocol/code_only.py` | Direct record and observation seam inspection; [MEM-OBJ-repl-history](#mem-obj-repl-history); supplied [RT-RTE-context-control](runtime.md#rt-rte-context-control) covers persistent/transient query edits. |
| Window warning | `src/jaz/hooks/builtin/context_window.py` | Direct full read; annotation on [RT-RTE-context-control](runtime.md#rt-rte-context-control). Warning does not perform compaction. |
| Console dispatch, prior turns and helper | `src/jaz/console.py` | Direct history, recording, helper confirmation, CLI hook builder and readline ranges; [MEM-OBJ-conversation-history](#mem-obj-conversation-history), [MEM-OBJ-helper-history](#mem-obj-helper-history), [MEM-OBJ-readline-history](#mem-obj-readline-history); dispatch progression supplied by [RT-RTE-console-turn](runtime.md#rt-rte-console-turn). |
| Hook inventory and validators | `src/jaz/hooks/builtin/__init__.py`, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/hooks/builtin/repl_code_hooks.py` | Direct registry read; validator control/cleanup supplied by [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission). Rejection is not rollback of already executed work. |
| ATIF write, live inspection and replay load | `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/replay.py` | Direct serializers, edits, lifecycle, loader and serving ranges; [MEM-OBJ-atif-trajectory](#mem-obj-atif-trajectory), annotation on [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay). Full concurrency and historical-schema compatibility remain uninspected, preventing a universal replay-fidelity claim. |
| Incremental trace and offline conversion | `src/jaz/hooks/builtin/trajectory_directory.py`, `src/jaz/utils/trace_to_directory.py` | Direct lifecycle and converter contract/observation-selection ranges; [MEM-OBJ-trajectory-directory](#mem-obj-trajectory-directory). Complete converter internals uninspected; no claim of lossless equivalence. |
| Trace-to-program | `src/jaz/hooks/builtin/workflow_replay.py` | Supplied [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission); annotation adds memory classification without claiming a separately inspected evaluator. |
| Rollout export | `src/jaz/hooks/builtin/rollout.py` | Direct projections, lifecycle and stand-down branches; [MEM-OBJ-rollout](#mem-obj-rollout), [MEM-RTE-rollout-export](#mem-rte-rollout-export). No shipped trainer closure established. |
| Hidden reasoning, token reuse and weight update | `src/jaz/llm/sglang.py` | Direct stamp preparation, response projection and service wrappers; [MEM-OBJ-token-stamp](#mem-obj-token-stamp), [MEM-RTE-weight-update](#mem-rte-weight-update). Server implementation and training judgment excluded. |
| Persistent settings | `src/jaz/user_settings.py`, `src/jaz/console.py` | Direct settings contract/loader, supplied write and startup trace; annotation on [RT-BAP-settings-load](runtime.md#rt-bap-settings-load). Full config compiler uninspected; no claim every possible setting is valid. |
| Credentials | `src/jaz/credentials.py`, `src/jaz/console.py` | Direct credential getter/writer and source-native CLI contract; [MEM-OBJ-credentials](#mem-obj-credentials). Backend-specific environment precedence not exhaustively traced. |
| File/terminal logging | `src/jaz/hooks/builtin/loggers.py`, `src/jaz/utils/log_to_markdown.py`, `src/jaz/utils/extract_git_diff.py` | Direct logger stream/edit rendering; converter/diff internals not inspected. Raw diagnostics and presentation utilities are included, but no downstream agent consumer or complete losslessness established. |
| Optional telemetry | `src/jaz/hooks/builtin/otel_tracing.py`, `src/jaz/hooks/builtin/jaeger_tracing.py`, `src/jaz/hooks/builtin/langfuse_tracing.py` | Registry and CLI activation inspected, exporter internals not inspected. Retained payload, collector retention and later reader remain unresolved; prevents a complete account of remote traces, not the local-memory findings. |
| Other provider state | `src/jaz/llm/_litellm.py`, `src/jaz/llm/` | Supplied [RT-CMP-llm](runtime.md#rt-cmp-llm) and direct SGLang exception to the thin default route; other adapter context/cache transformations uninspected. No global no-learning or no-retention inference. |

## Core ideas

1. Console memory has two materially different consumption paths: later main agents receive live prior input/result objects, while the settings helper receives only rendered transcripts. A short repr is an index, not the retained payload. See [MEM-OBJ-conversation-history](#mem-obj-conversation-history) and [MEM-OBJ-helper-history](#mem-obj-helper-history).
2. Context reduction is not deletion. Observation abbreviation leaves the code-only history's continuing output whole. Query edits can remove messages while recorder edit records preserve their identities. Recursive invocations keep child conversations out of the parent window, but shared/returned Python objects break a strict stack-only interpretation. See [MEM-OBJ-repl-history](#mem-obj-repl-history), [MEM-OBJ-atif-trajectory](#mem-obj-atif-trajectory), and [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke).
3. Saved responses and generated Python have different authority. Replay substitutes a model response into the normal execution loop. Workflow emission produces an external executable artifact, not an automatically adopted agent policy. Neither label certifies success. See [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay) and [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission).
4. Token-native traces retain material omitted from visible code and later prompts, including hidden reasoning. Exported samples afford external training; exposed weight-update transport does not establish a shipped trace-to-trained-policy loop. See [MEM-OBJ-token-stamp](#mem-obj-token-stamp), [MEM-RTE-rollout-export](#mem-rte-rollout-export), and [MEM-RTE-weight-update](#mem-rte-weight-update).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-repl-history
Label: Code-only REPL history

Part of: [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state)

Source-native identity: `__history__`, a list of REPLHistoryEntry objects surfaced by reference in the namespace. Storage substrate: process memory. Representational form: symbolic records containing natural-language/code response text, output text and a live recoverable exception. This is a part of the runtime state container, not another declaration of that container. Lineage: CodeOnlyProtocol projects finalized loop responses/results; response absence becomes an empty string, continuing output remains whole, terminal output becomes empty. Raw response content may contain comments/reasons, but this does not guarantee a complete reasoning record. Consumer: model-written Python can index/print entries; print output then passes observation abbreviation again. Ordinary use is current-run context, not read-back by definition; a returned/shared history object can outlive its frame, without automatic delivery to a new invocation. Admission is automatic runtime append, not per-entry human approval. SRC-1, `src/jaz/protocol/code_only.py`; supplied [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop).

> repl_output=exec_result.output if isinstance(exec_result, Continue) else "",
> repl_exception=repl_exception,
> --- `src/jaz/protocol/code_only.py`

#### MEM-OBJ-conversation-history
Label: Live console conversation history

Source-native identity: ConversationHistory and its ConversationTurn parts. Distinct from the per-invocation namespace in [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state); it is retained by the console chat closure across fresh invocations in [RT-RTE-console-turn](runtime.md#rt-rte-console-turn). Storage: live process objects, not a serialized session checkpoint. Form: symbolic ordered records plus natural-language prompt text and arbitrary opaque Python inputs/results. A failure stores the exception object, including aborted turns. Inputs/results are references, not frozen value snapshots. Lineage: typed/interpolated user input and invoke outcome; admission is automatic recording, regardless of success, with no semantic relevance filter.

Main-agent consumer gets the object and a transcript description, with repr values capped at 500 characters each. All turns are rendered; this is not a total-size budget. The live objects remain inspectable after truncated display. Trust: past user text, tool outputs and model-produced values become input data, not validated facts or higher-priority instructions. They can nevertheless affect generated code through model interpretation and object access. New namespace construction creates new history; no cross-session live-object reload is established. SRC-1, `src/jaz/console.py`.

> if history.turns:
>     extra["conversation_history"] = history
> --- `src/jaz/console.py`

> history.record(prompt, inputs, exc, target=_target, error=True)
> raise
> --- `src/jaz/console.py`

#### MEM-OBJ-helper-history
Label: Settings helper exchange history

Source-native identity: HelperHistory/HelperExchange. Distinct from main ConversationHistory, but both feed [RT-RTE-settings-admission](runtime.md#rt-rte-settings-admission). Storage: process memory. Form: symbolic request/tag/content/applied records, with natural-language answers or symbolic Python snippets. Lineage: helper output and human confirmation state. Admission to history is software-controlled: answers, declined code and non-TTY rejection are recorded; confirmed code is recorded before execution. Thus `applied=True` denotes permission to run, not verified success. Curation is transcript rendering, capped at 4000 content characters per exchange, with no turn-count bound established. Later helper calls receive text transcripts of this history and main history, not the live input/result payloads. This preserves proposals/rejections for interpretation but not complete execution evidence or machine-verified reasons for success. SRC-1, `src/jaz/console.py`.

> remember(applied=True)
> exec(compile(snippet, "<jaz-settings>", "exec"), namespace)
> --- `src/jaz/console.py`

#### MEM-OBJ-readline-history
Label: Console line-editing history

Source-native identity: readline history at `~/.jaz/history`. Storage: disk text loaded into readline, distinct from the live conversation objects of [MEM-OBJ-conversation-history](#mem-obj-conversation-history). Form: source/input lines consumed symbolically by line editing and subsequently by Python if the user resubmits them. Admission: automatic typed-line retention and exit-time write, not semantic curation. Later consumer: interactive user's recall/edit operation; not automatic prompt injection or reconstruction of result objects. The write cap is 1000 history entries. Credential entry through getpass avoids typed secret lines, but a user writing a literal secret in a command can retain it here. SRC-1, `src/jaz/console.py`; no supplied object counterpart.

> readline.set_history_length(1000)
> atexit.register(readline.write_history_file, history_file)
> --- `src/jaz/console.py`

#### MEM-OBJ-atif-trajectory
Label: ATIF invocation trajectory

Source-native identity: TrajectoryRecorder documents. Distinct retained input to [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), not that consumer route. Storage: recorder state in memory; optional JSON file at scope teardown. Form: symbolic invocation tree, messages, metrics, origin/provenance and edit records, carrying natural-language/code strings. Inputs/scope are only type plus repr prefixes of 10000 characters: display summaries do not serialize live objects. Added messages include content; drops reference identity/position/persistence while original content lives in earlier steps. These access coordinates are not assertions about the content's truth.

Lineage: observed hook events, finalized response text and message-buffer state, not a separate reflective synthesis. Source-native documentation permits mid-run document retrieval; a file is only written at teardown, unlike streaming directories. A process crash before teardown can lose the file. In-memory reactivation clears prior state; file-producing instances refuse reactivation, but this is not an exclusive filesystem lease against a different writer. Later replay reads response queues, not restored REPL objects. A model/tool can encounter recorded reasons only if present in retained strings; nothing here establishes reasoning-guided semantic curation. SRC-1, `src/jaz/hooks/builtin/atif_trace.py`.

> k: {"type": type(v).__name__, "repr_prefix_10000": repr(v)[:10000]}
> for k, v in namespace.items()
> --- `src/jaz/hooks/builtin/atif_trace.py`

> data = trajectories[0] if len(trajectories) == 1 else trajectories
> self.output_path.write_text(json.dumps(data, indent=self.indent))
> --- `src/jaz/hooks/builtin/atif_trace.py`

#### MEM-OBJ-trajectory-directory
Label: Browsable trajectory directory

Source-native identity: TrajectoryDirectoryRecorder output and trace_to_directory output. These are alternative diagnostic projections of invocation events or ATIF, not the JSON input consumed by [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay). Storage: directory files, incremental for the hook, post-run for the converter. Form: natural-language/Markdown message display plus symbolic code/text files and provenance/index metadata. Consumers: human inspection explicitly afforded by the source; automatic agent reuse not established. Admission is automatic event rendering after host activation or explicit converter invocation; no human approval of each message. Streaming output retains partial work, while the JSON writer waits for scope end. A fresh recorder instance can still overwrite an existing directory and leave old children mixed in. Source describes sequential-delegation expectations and lack of thread safety. No complete checkpoint or guaranteed current-state reconstruction follows. SRC-1, `src/jaz/hooks/builtin/trajectory_directory.py`, `src/jaz/utils/trace_to_directory.py`; no supplied object counterpart.

> It is written into **as-is**: a trace already at that path is
> overwritten file by file as the new run reaches each one, and any sub-agent directories
> the old run left behind survive and interleave with the new ones. Give each run its own
> directory.
> --- `src/jaz/hooks/builtin/trajectory_directory.py`

#### MEM-OBJ-token-stamp
Label: Token-native response sidecar

Source-native identity: TokenStamp and TurnRecord produced by SGLangLLM. Distinct from the provider component [RT-CMP-llm](runtime.md#rt-cmp-llm) and text-only histories; no supplied object counterpart. Storage: immutable Python sidecar objects in process memory, carried on LLMResponse.tokens. Form: symbolic token-ID sequences, sampled spans, logprobs and optional weight-version metadata. Numerical logprobs are not learned parameter storage. Decoded strings are a readable companion, not an interchangeable replacement for exact token IDs. Lineage: tokenized sent messages and server-returned output IDs/logprobs; the server's actual sampling fidelity remains outside inspected evidence.

With reasoning tags enabled, regex filtering removes reasoning from visible content, while sampled stamp IDs and content_text retain it. Later text context uses filtered content; a stamp/content mismatch triggers re-rendering rather than silently restoring omitted reasoning tokens. Rollout export can still include those sampled tokens. Hence visible REPL history is not a complete token-side reasoning trace, and reason retention in a training sidecar does not imply a later foreground agent sees the reasons. SRC-1, `src/jaz/llm/sglang.py`.

> visible = content
> if self._reasoning_closed is not None and self._reasoning_open is not None:
>     visible = self._reasoning_closed.sub("", visible)
>     visible = self._reasoning_open.sub("", visible)
> --- `src/jaz/llm/sglang.py`

> if stamp is not None and stamp.content_text == content:
>     stamps.append(stamp)
> --- `src/jaz/llm/sglang.py`

#### MEM-OBJ-rollout
Label: Frozen rollout and training sample projections

Source-native identity: Rollout, FlatSample and TurnSample. Storage: in-process immutable records and exported JSON-compatible dictionaries; no automatic disk writer in the inspected recorder. Form: symbolic sequences of token IDs, masks, probabilities, invocation identities and terminal metadata. Lineage: [MEM-OBJ-token-stamp](#mem-obj-token-stamp) records copied with authoritative iteration, then frozen at invocation exit. Distinct from text-only [MEM-OBJ-atif-trajectory](#mem-obj-atif-trajectory); supplied replay uses text, not these samples. No supplied object counterpart.

A token-less completed query makes the recorder discard any partial log for that invocation and stand down. Failed queries without responses instead allow prior token records to survive as an aborted partial rollout. Export does not add reward or verify correctness. Flat export rejects non-monotone contexts; piece and per-turn exports retain alternatives rather than pretending one uninterrupted sequence. Later trainer consumption is documented affordance, not deployed training observed here. SRC-1, `src/jaz/hooks/builtin/rollout.py`.

> self._stood_down.add(event.invoke_id)
> self._log.pop(event.invoke_id, None)
> return []
> --- `src/jaz/hooks/builtin/rollout.py`

#### MEM-OBJ-credentials
Label: Provider credentials

Source-native identity: credentials.json entries addressed by provider and field. Storage: user-scoped disk JSON; symbolic provider/field mapping containing opaque secret strings. Distinct from settings in [RT-BAP-settings-load](runtime.md#rt-bap-settings-load): credentials authorize access, rather than supply learned knowledge or choose an action. Lineage: console user-supplied value; writer preserves other provider entries and atomically replaces a private file. No remove/list helper is provided in this source-native contract; manual edit handles rotation/deletion. Credential lookup supplies a nonempty string only. Backend readers choose whether to use it; all adapter precedence is not established. Admission is software validation plus user's act of supplying content, not a per-request human approval. SRC-1, `src/jaz/credentials.py`; no supplied object counterpart.

> existing = dict(load_credentials())
> entry = dict(existing.get(provider) or {})
> entry[field] = value
> existing[provider] = entry
> --- `src/jaz/credentials.py`

### Routes

#### MEM-RTE-rollout-export
Label: Token rollout export

Endpoints/progression: completed token-native LLMQueryExit → per-invoke accumulator → InvokeExit frozen Rollout → flat/piece/turn projection → documented external trainer role. Owner: host activates the recorder; deterministic projection rules choose samples. Context/action effects: recording emits empty effects and does not itself change policy. Distinct from [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), which supplies saved response text, not training samples. SRC-1, `src/jaz/hooks/builtin/rollout.py`.

- Immediate return: recorder observes without supplying a task result; export APIs return sample records.
- Later read-back: afforded to an external training driver via explicit export; actual persistence, trainer ingestion and later trained-policy use are uninspected.
- Delegated visibility: nested invokes have separately keyed logs and completion-order rollouts, not one flattened parent transcript.
- Selection predicate: Completed response with token sidecar; no sidecar stands down for that invoke; projection selects monotone spans or individual turns.
- Invalidation or expiry: setup replaces recorder buffers; token-less completion drops partial records; external exported objects require external lifecycle management.
- Activation or effect: symbolic sample production is wired; no weight learning or improvement demonstrated.
- Evidence limits: source-native “training-grade” is not an empirical fidelity or benefit result; reward/evaluation and training are external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission of samples is software-controlled, not human labeling. Driver supplies any reward; there is no built-in reference-answer oracle. Operating mode is recording open invocations with optional downstream training, not an established bounded experiment. Reasons may survive in sampled IDs, but later trained behavior and its attribution cannot be inferred from this export.

> for prev, cur in zip(self.turns, self.turns[1:], strict=False):
>     if not _extends(prev, cur):
>         raise NonMonotoneRolloutError(
> --- `src/jaz/hooks/builtin/rollout.py`

#### MEM-RTE-weight-update
Label: SGLang weight update transport

Endpoints/progression: external caller's disk path/distributed payload/tensors → SGLangLLM HTTP wrapper → serving-engine update endpoint → potential later completion from updated policy. Owner: caller chooses candidate and invocation time; server implements acceptance. Distinct from model selection in [RT-RTE-settings-admission](runtime.md#rt-rte-settings-admission); related component is [RT-CMP-llm](runtime.md#rt-cmp-llm). SRC-1, `src/jaz/llm/sglang.py`.

- Immediate return: server response JSON or None for non-JSON success, with HTTP failure propagation.
- Later read-back: documented later serving role consumes loaded policy; no shipped training driver connects this to the recorded rollouts in inspected evidence.
- Delegated visibility: inapplicable — service transport is not recursive agent delegation; shared endpoint can affect several callers.
- Selection predicate: explicit caller choice of update method/path/payload; no task-based candidate selector is established.
- Invalidation or expiry: replacement update and pause/continue or release/resume methods are exposed; semantic rollback and previous-weight retention belong to the external server/caller.
- Activation or effect: update requests are wired; actual accepted weights and subsequent behavior remain unobserved.
- Evidence limits: endpoint implementation, authentication, training objective, provenance of proposed weights and task-quality validation are outside inspected source.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: host/trainer proposes parameters; HTTP success only reports service acceptance, not improvement. The wrappers do not impose per-update human approval or an answer oracle. Human control over the external caller is unresolved. The transport supports training orchestration but is not evidence that the default agent loop trains itself. No rollback guarantee follows from memory release/resume, which concerns GPU allocation, not reverting policy content.

> return self._post(
>     "update_weights_from_disk", {"model_path": model_path, **options}
> )
> --- `src/jaz/llm/sglang.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-console-turn](runtime.md#rt-rte-console-turn)

Memory consumers differ: main turns automatically receive the nonempty live history and its description; helper invocations receive main/helper transcript strings only. The selector is nonemptiness, not retrieval ranking or relevance inference. Description is capped per value but all turns remain included, subject to subsequent protocol input rendering. Model-written Python can request precise live values, so the automatic transcript supply and subsequent on-demand object access are separate operations. Actual use of earlier content is unobserved. SRC-1, `src/jaz/console.py`; [MEM-OBJ-conversation-history](#mem-obj-conversation-history), [MEM-OBJ-helper-history](#mem-obj-helper-history).

#### On [RT-RTE-context-control](runtime.md#rt-rte-context-control)

CodeOnlyProtocol abbreviates observation text; its separate history projection does not abbreviate continuing output. ContextWindowWarning reads last reported prompt_tokens and effective max_input_tokens, then transiently supplies caller-authored text when the fraction threshold is reached. It does not select or persist a summary. Missing size information means no warning. Exit clears its token maps. Persistent hook edits can replace carried messages, while recorder provenance/edit records can retain evidence about removed content; the hooks' existence does not establish an automatic summarizer. SRC-1, `src/jaz/protocol/code_only.py`, `src/jaz/hooks/builtin/context_window.py`, `src/jaz/hooks/builtin/atif_trace.py`.

> return [AddMessages([{"role": "user", "content": self.warning_text}])]
> --- `src/jaz/hooks/builtin/context_window.py`

#### On [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay)

Retained selector input is a host-chosen ATIF file, then invocation-tree position and response cursor. It is not semantic retrieval against the current task. Supplied content and metrics reach LLMQuerySend; recorded initial inputs are not deserialized into restored tool/results objects. Budget is the finite per-node queue, not a relevance/token budget. Exhaustion, optional divergence latch and missing child nodes fall back to live work; no trace deletion follows. Loading refuses arrays other than one root. Caller activation admits reuse without per-response human approval; runtime parse/code validation and execution remain later gates. Trust in the supplied trace matters because source text can become executed code, not merely evidence. SRC-1, `src/jaz/hooks/builtin/replay.py`; [MEM-OBJ-atif-trajectory](#mem-obj-atif-trajectory).

> if len(data) != 1:
>     raise ValueError(
>         f"TrajectoryReplay: expected a single root trajectory, got "
>         f"{len(data)} in {path}. Multi-root ATIF traces are not supported."
>     )
> --- `src/jaz/hooks/builtin/replay.py`

#### On [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission)

The output is derived symbolic Python on disk, with original code, child-call substitutions and exception wrappers. Its later Python executor gives code direct software authority; automatic installation or later execution is not established. Source comments or response reasons survive only insofar as the emitter retains them in code, not as a guaranteed rationale channel to a model. This trace-fed transformation is stronger than raw logging, but terminal failure does not reject its artifact. The supplied Enter-versus-committed-code mismatch prevents unconditional execution equivalence. SRC-1, `src/jaz/hooks/builtin/workflow_replay.py`; supplied record retains the minimum passages.

#### On [RT-BAP-settings-load](runtime.md#rt-bap-settings-load)

Stored configuration is symbolic JSON, not natural-language learned guidance. Console startup compiles/applies it; library import does not. Manual editing and confirmed helper snippets are separate admission paths. File policy rejects persisted llm.api_key/base_url but warns rather than rejects sandbox loosening. Deletion/editing is recovery; invalid nonempty files fail loudly rather than silently selecting defaults. This gives retained choices later console configuration authority, without demonstrating a beneficial choice or policy-weight update. SRC-1, `src/jaz/user_settings.py`, `src/jaz/console.py`.

> _BLOCKED_LLM_LEAVES: tuple[str, ...] = ("base_url", "api_key")
> --- `src/jaz/user_settings.py`

#### On [RT-CMP-llm](runtime.md#rt-cmp-llm)

The supplied default-adapter no-parameter-write finding must stay scoped to that path. SGLang exposes explicit weight replacement and allocation orchestration, including update-from-disk/tensor/distributed calls. Parameters can therefore change through an exposed target adapter, conditional on server acceptance; actual updates are unobserved. Exact weights are not pinned by the Git revision, and optional weight_version metadata is not independent authentication. Model identifier/endpoint may resolve to a changed policy after updates. Retained token samples afford external training, but do not establish that the JAZ agent loop invokes the update wrappers. SRC-1, `src/jaz/llm/sglang.py`; [MEM-RTE-weight-update](#mem-rte-weight-update), [MEM-OBJ-token-stamp](#mem-obj-token-stamp).

## Write side

Acquisition/admission is mostly event-driven, not semantic curation. Host activation of a recorder authorizes automatic capture, not human approval of every entry. Main console history records success, failure and interruption as live references; helper history records the proposal and confirmation before host exec. Thus rejected proposals remain available to later helpers, while confirmation is not a verified outcome. See [MEM-OBJ-conversation-history](#mem-obj-conversation-history) and [MEM-OBJ-helper-history](#mem-obj-helper-history), SRC-1, `src/jaz/console.py`.

The trace chain has several separate products. Runtime messages/results → ATIF and streaming diagnostics retain raw/projection records. Runtime code events → workflow files transform traces into executable material. Token-native responses → frozen rollouts → masks/turn samples transform traces for an external trainer. These paths are not interchangeable checkpoints: repr summaries cannot restore opaque live objects; directory display is not the replay JSON; flat samples cannot always represent edited contexts. Neither trace retention nor the labels “workflow” and “training-grade” establish semantic revision, successful replay or improved capacity. See [MEM-OBJ-atif-trajectory](#mem-obj-atif-trajectory), [MEM-OBJ-trajectory-directory](#mem-obj-trajectory-directory), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission), [MEM-RTE-rollout-export](#mem-rte-rollout-export); SRC-1 paths attached to those records.

Maintenance has route-specific consequences. Query drops remove current-window delivery, not necessarily REPL history or trace records. In-memory recorder reactivation clears prior buffers; file-producing recorder instances refuse reuse, but other instances can overwrite shared destinations. Rollout token-less completion withdraws the whole invoke's token log rather than fabricating IDs; aborted invokes with valid prior tokens retain partial records. Replay divergence withdraws saved-response serving, not the source file. Return rejection supplies feedback/termination but does not undo side effects already performed. Settings deletion/editing and credential rotation are user recovery, not learned forgetting. These controls have different consumers and should not be combined into a universal retention policy. SRC-1, `src/jaz/hooks/builtin/atif_trace.py`, `src/jaz/hooks/builtin/trajectory_directory.py`, `src/jaz/hooks/builtin/rollout.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/user_settings.py`, `src/jaz/credentials.py`; [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission).

## Read-back

The principal wired later-agent route is console session history: new prompt turns automatically receive the existing object; they can then inspect specific payloads in Python. Helper requests automatically receive textual histories only. No evidence here establishes a total context budget, relevance-ranking store or restored cross-session live objects. Readline instead restores lines for a human editing/recall consumer. SRC-1, `src/jaz/console.py`; [RT-RTE-console-turn](runtime.md#rt-rte-console-turn), [MEM-OBJ-readline-history](#mem-obj-readline-history).

Replay is an explicit host-requested read followed by automatic sequential delivery of saved responses. The consumer is the normal protocol/executor path, not a model reasoning over retrieved examples. Generated workflow execution and external trainer consumption are afforded later consumers, not observed deployment. Settings and credentials reload into deterministic configuration/access consumers; they are retained behavioral machinery/access data, not evidence that models learned from past tasks. SRC-1, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`, `src/jaz/hooks/builtin/rollout.py`, `src/jaz/user_settings.py`, `src/jaz/credentials.py`; route records and annotations above.

Working-context isolation remains distinct from read-back. Child invocation frames exclude their working conversation from parent context and return only explicit results by default; shared objects and escaped histories weaken a strict stack analogy. History indexing/printing can bring omitted output back through the observation channel. SGLang reasoning stripping removes selected text preferentially from later model context, but its token sidecar can keep the removed material for external sample export. None of these mechanisms guarantees the foreground model reloads omitted reasons or follows the supplied history guidance. SRC-1, `src/jaz/llm/sglang.py`, `src/jaz/protocol/code_only.py`; [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke), [MEM-OBJ-token-stamp](#mem-obj-token-stamp).

## Integration issues

- Scope qualification, not a contradiction of the default adapter: [RT-CMP-llm](runtime.md#rt-cmp-llm) leaves other adapters uninspected. [MEM-RTE-weight-update](#mem-rte-weight-update) establishes SGLang update transport and prevents extending the default path's no-write finding to all JAZ. Server acceptance and later exercised policy remain unresolved.
- No new declaration intentionally duplicates a supplied referent. [MEM-OBJ-repl-history](#mem-obj-repl-history) is a declared part of [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state). The other memory objects are retained artifacts or parts consumed by supplied routes, not replacement route declarations. Text trajectory, rollout sidecar and directory projection are distinct operative parts with different selection/rejection and consumers.
- The trace-to-training-to-weight-update connection is not established. [MEM-RTE-rollout-export](#mem-rte-rollout-export) affords external training; [MEM-RTE-weight-update](#mem-rte-weight-update) exposes service writes. Without driver wiring, candidate evaluation and later policy evidence, these must not be collapsed into observed learning or self-improvement. SRC-1, `src/jaz/hooks/builtin/rollout.py`, `src/jaz/llm/sglang.py`.
- Remote telemetry, other adapter context transformations, full converter behavior and concurrent replay remain named uninspected parts in the coverage table. They prevent exhaustive remote-retention/context-equivalence claims, not the supported local mechanisms. No source access gap is claimed for these available files.
- The supplied [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission) records Enter-time code capture and abnormal-exit finalization. These remain limits on artifact fidelity/success, not reasons to omit the derived artifact from memory scope. Later execution and rationale use remain unobserved. SRC-1, `src/jaz/hooks/builtin/workflow_replay.py`.

## Limitations and checks

Source identity recheck: checkout HEAD was `0803d4971be785e95b80054b02259664d70fa3da`, matching boundary. Only registered SRC-1 and supplied boundary/runtime members were used. Required job, member types, worker rules, collection contract and records contract were read completely; no authoring skill or prior analysis was used. Direct reads were source text, not target execution. All operation and benefit conclusions remain unobserved; server, trainer and collector internals remain outside the evidence. Available-but-uninspected parts are retained in the coverage table.

Validation: invocation-specific `commonplace-run validate-output` passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Form/quotation success does not establish semantic acceptance or operation.
