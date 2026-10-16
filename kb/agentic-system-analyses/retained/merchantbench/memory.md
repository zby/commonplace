---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MerchantBench memory: optional run-local Markdown, foreground history eviction, trace inspection and external Hermes context boundary."
run-id: AAS-2026-10-15-merchantbench-d2f4d78dbe37-01
source-identity: https://github.com/khancold/MerchantBench
reviewed-boundary: d9e5bd7519ab100193c21778aecfb59e30f24651
---

# MerchantBench memory report

## Boundary and evidence

This report covers retained agent material and working-context control in the shipped MerchantBench workflow at SRC-1, commit `d9e5bd7519ab100193c21778aecfb59e30f24651`. The [boundary](boundary.md) registers the source. Runtime findings are provisional inputs; the paths below were also read directly except where marked supplied. Evidence is implementation and source-native design, not observed operation. No target code, tests, providers or containers were executed.

The memory boundary includes the optional document tools, their full-version history, ReAct's process-local history and context selection, human editing/read-back, persisted traces and their inspection consumers, and MerchantBench's Hermes profile/configuration and external-trace readers. Simulator snapshots, ratings, idempotency and scoring are accounted for but distinguished from agent knowledge: ordinary current-run domain state and unchanged recovery checkpoints are not themselves derived agent memory. External Hermes algorithms, private/local run artifacts and provider internals are unavailable within SRC-1; this prevents conclusions about their summarization, skill learning and actual consumer behavior.

| Entry point / operation | Inspected SRC-1 paths / evidence basis | Coverage and prevented conclusion |
| --- | --- | --- |
| Schema publication, list-tools registration and HTTP tool admission | `env/tools/registry.py`, `env/tools/dispatch.py`, `env/web/routes_agent.py`; supplied [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), [RT-RTE-act-gate](runtime.md#rt-rte-act-gate) | [MEM-RTE-document-write](#mem-rte-document-write), [MEM-RTE-document-read](#mem-rte-document-read). Registry metadata is not an independently verified REST tool endpoint. Direct Python handler use is a library capability outside HTTP checks. |
| Document overwrite, read and version append | `env/tools/tools.py`; test source `tests/test_memory_doc_tools.py` | [MEM-OBJ-memory-doc](#mem-obj-memory-doc), [MEM-OBJ-memory-history](#mem-obj-memory-history). Tests were read, not run. No automatic history-version restore consumer established. |
| Human document editor and trace viewer | `env/web/templates/_human_playground_script.html`, `env/web/templates/dashboard.html` | Same document routes; [MEM-RTE-trace-inspection](#mem-rte-trace-inspection). Human edits are a real alternate admission path, not inferred from a generic API caller. |
| Foreground request assembly, threshold eviction, Forbidden retry, stale-step discard | `agent/baselines/react_160k_compact_30k.py` | [MEM-OBJ-history](#mem-obj-history); annotations on [RT-RTE-context-trim](runtime.md#rt-rte-context-trim) and [RT-RTE-react-loop](runtime.md#rt-rte-react-loop). No independent summarizer or automatic document reinjection established. |
| Per-step trace writes, historical observation/trace endpoints, usage and health telemetry | `env/storage/agent_log.py`, `env/web/routes_agent.py`, `env/core/simulator.py`, `env/web/leaderboard.py` | [MEM-OBJ-step-traces](#mem-obj-step-traces), [MEM-RTE-trace-inspection](#mem-rte-trace-inspection), [MEM-CLM-telemetry-limits](#mem-clm-telemetry-limits). Raw traces and counters do not establish semantic learning. |
| First brief and observation delivery | Direct `env/web/routes_agent.py`, baseline; supplied `env/tools/observation.py` findings | [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief), [RT-BAP-brief-guidance](runtime.md#rt-bap-brief-guidance). Static scenario guidance is not learned memory. |
| Hermes profile preparation, reuse and context configuration | `env/web/runner.py`, `env/scenarios/agents/hermes.yaml` | Annotation on [RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch). Configuration is visible; external compression, native memory and skill update consumers remain uninspected. |
| Hermes active/compacted trace display | `env/web/routes_agent.py`, dashboard trace-source selection | [MEM-RTE-trace-inspection](#mem-rte-trace-inspection). Read-only SQL adapters expose messages; they do not establish what external Hermes sends to its model. |
| Simulator persistence, replay and rehydration | `env/storage/snapshot.py`, `env/storage/replay.py`, `env/core/simulator.py`, `env/web/runner.py`, `env/web/routes_dashboard.py` | [MEM-CLM-state-boundary](#mem-clm-state-boundary). JSON deltas/gzip product checkpoints reconstruct dashboard state; SQLite rehydration rebuilds runtime state. Neither restores ReAct history. Detailed domain equations are outside this memory account. |
| Run unloading/deletion, terminal evaluation | Direct `env/web/runner.py`; supplied [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval) | [MEM-RTE-run-withdrawal](#mem-rte-run-withdrawal). Evaluation retains operator-facing results, not an inspected successor-policy feedback route. Deterministic/batch/hosted clients are covered by supplied runtime routes, not claims about arbitrary submitted agents' memory. |

## Core ideas

The durable agent-facing memory is one whole Markdown document per run and sanitized agent name, not a searchable collection. The foreground model may write its own selected notes and later request the entire latest document; a human can edit the same surface. Software admits bytes and protocol validity, not truth, usefulness or justification. Version history preserves previous submitted bodies for inspection, but the read tool returns only the latest body ([MEM-OBJ-memory-doc](#mem-obj-memory-doc), [MEM-OBJ-memory-history](#mem-obj-memory-history)).

ReAct's so-called compaction is recency-based deletion. If writing is available, it first asks the same foreground model to save important details; a successful save is not a prerequisite for eviction. The surviving context is a by-value suffix, not a generated summary or a pointer graph. A later document read can supply external text again, but it cannot automatically recover unsaved discarded turns ([RT-RTE-context-trim](runtime.md#rt-rte-context-trim), [MEM-RTE-document-read](#mem-rte-document-read)).

Trace retention, display and health metrics are separate from behavior-shaping memory. A server can preserve a tool result after the client has removed it from its own context. A counter named `skills_evolutions` or `memory_compactions` does not certify the semantic result of an external update ([MEM-CLM-telemetry-limits](#mem-clm-telemetry-limits)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-doc
Label: Latest run-local memory document

Source-native identity: the file returned by `_memory_doc_path`, under `runs_root/run_id/agent/memory/<safe_agent_id>.md`. Storage is UTF-8 filesystem text. Markdown bodies are natural-language notes/plans when interpreted by the model or human; their text is opaque to the persistence handler. The JSON `ok` and `bytes` envelope is symbolic access metadata, not knowledge content. Lineage is supplied full content, potentially derived by a model from observations/tool results or edited by a human. There is no enforced statement/rationale schema. A real run's payload and initial provenance are unobserved. Consumers are the read handler, human editor and, after a requested read, the foreground model. Storage alone gives no executable permission or mandatory policy authority. Source: SRC-1, `env/tools/tools.py`, `env/tools/registry.py`, human editor. Distinct from [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief): mutable run-authored scratchpad rather than scenario-generated initial instruction; [RT-RTE-act-gate](runtime.md#rt-rte-act-gate) mentions the capability, not a separately declared object.

> return os.path.join(env.runs_root, env.run_id, "agent", "memory",
>                         f"{safe_agent_id}.md")
> --- `env/tools/tools.py`

Agent filenames sanitize characters and strip leading/trailing dots and underscores. This is a naming boundary, not proof that arbitrary distinct agent IDs map injectively: unusual names can collide. Run separation follows the parent directory. Test source demonstrates intended round-tripping and separation for `agent_0` and `agent_1`, not universal name isolation (SRC-1, `tests/test_memory_doc_tools.py`, `env/tools/tools.py`).

#### MEM-OBJ-memory-history
Label: Memory document full-version history

Source-native identity: `_memory_history_path`, adjacent `<safe_agent_id>.history.md`. Storage is append-written UTF-8 Markdown, containing full submitted bodies plus symbolic version marker, step, wall-clock milliseconds and byte count. This is an archive of accepted writes, not an automatic semantic summary or a record of why each revision was warranted. It counts current and legacy version markers when numbering. An author can include reasons, but the handler does not require them. The later writer reads the history to count markers; the normal document read does not read it. No shipped history-version selection/restore route was found in the bounded document-tool and repository-reference search. Thus durable older bodies exist without an established agent reload route. Source: SRC-1, `env/tools/tools.py`, `tests/test_memory_doc_tools.py`. Distinct from [MEM-OBJ-memory-doc](#mem-obj-memory-doc); no supplied object counterpart after comparison with runtime records.

> f.write(f"## Memory version {version}\n")
>         f.write(f"- step: {env.t}\n")
>         f.write(f"- wall_ms: {wall_ms}\n")
>         f.write(f"- bytes: {size}\n\n")
>         f.write(content)
> --- `env/tools/tools.py`

#### MEM-OBJ-history
Label: ReAct process-local message history

Part of: [RT-RTE-react-loop](runtime.md#rt-rte-react-loop)

This is a material state part of the supplied route, not another loop declaration. `self.history` is a Python list in the baseline process: symbolic roles, call IDs and JSON arguments carry natural-language observations, assistant content and tool-result strings. Raw accumulated material is selected into later requests; no new summary object is created by the trim helper. `_remember_act` normally retains assistant/tool messages but treats EOS-only calls specially, retaining eligible assistant content without the EOS tool exchange. It can retain `reasoning_content` when supplied; that does not demonstrate a rationale for every document update. History is initialized empty, not reconstructed from the server trace. The separate `system_prompt` survives suffix trimming in that process. Source: SRC-1, `agent/baselines/react_160k_compact_30k.py`; consumer [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model).

> self.history: list[dict] = []
> --- `agent/baselines/react_160k_compact_30k.py`

#### MEM-OBJ-step-traces
Label: Persisted per-step agent traces

Source-native identity: `agent/by_step/t_NNNNN.json`. Storage is JSON on disk, atomically replaced through a temporary file. Mixed representation: symbolic step/agent/turn/cost/context metadata and OpenAI-format message envelopes; natural-language content, tool arguments and results remain raw recorded material rather than adopted advice. Live writes follow actions and final writes add hook-close timing. Lineage includes observations, assistant proposals, executed tool results and accepted historical/native messages; a recorded native call is not proof of server execution. Consumers include scoped trace endpoints, human viewers and telemetry aggregators. This object overlaps the retained outputs of [RT-RTE-act-gate](runtime.md#rt-rte-act-gate) and [RT-RTE-react-loop](runtime.md#rt-rte-react-loop), but is neither a replacement route nor a part of exactly one supplied record. Source: SRC-1, `env/storage/agent_log.py`, `env/core/simulator.py`, `env/web/routes_agent.py`.

> """Atomic write of in-progress step data (called after each /act)."""
> --- `env/storage/agent_log.py`

### Routes

#### MEM-RTE-document-write
Label: Document authoring and overwrite admission

Part of: [RT-RTE-act-gate](runtime.md#rt-rte-act-gate)

This is the document-admission branch of the supplied HTTP action route. A foreground model proposes `write_memory_doc(content)`, or the human editor's save button supplies the textarea value. The server dispatches under its protocol gate; `write_memory_doc` checks UTF-8 length, overwrites the latest file, then appends its full body to history. There is no semantic critic, approval oracle or comparison of candidate strategies. The generic API also affords other callers; their human/software authorship is unresolved rather than assumed autonomous. Source: SRC-1, `env/tools/tools.py`, `env/tools/registry.py`, `env/tools/dispatch.py`, `env/web/templates/_human_playground_script.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `ok` and byte count, or size/schema/protocol rejection; the write response does not return a summary of the content.
- Later read-back: Latest text persists for [MEM-RTE-document-read](#mem-rte-document-read); full versions persist in [MEM-OBJ-memory-history](#mem-obj-memory-history). Caller arguments also enter server traces.
- Delegated visibility: Handler receives server-selected environment/agent and proposed full content; the model does not receive filesystem access through this tool.
- Selection predicate: Caller explicitly chooses a write; protocol grants/schema and the 256 KiB body limit admit it. No content-quality predicate is implemented.
- Invalidation or expiry: Next successful overwrite replaces the latest body; writing empty content can clear it, while history still retains older bodies. Run deletion removes both.
- Activation or effect: Latest file and version history are changed by code; successful later reliance or better decisions is unobserved.
- Evidence limits: Direct Python invocation bypasses HTTP argument typing and coerces non-strings; filesystem overwrite and history append are separate non-transactional operations. A later append error need not restore the old latest file.

Admission roles: model or human supplies content; software can veto validity/size; no mandatory human approval for model writes. Guidance asks for concise structured strategy, product notes, tasks and decisions (`env/tools/registry.py`); the compaction reminder requests preservation of important details. Operating mode is the bounded store task, with no expected-answer oracle. Recovery is another overwrite, not an exposed history rollback. A permitted write can preserve trace-derived experience, but neither content-directed criticism nor improved capacity follows from the tool's existence.

> with open(path, "w", encoding="utf-8") as f:
>         f.write(content)
>     _append_memory_history(env, agent_id, content)
> --- `env/tools/tools.py`

#### MEM-RTE-document-read
Label: Requested latest-document read-back

Part of: [RT-RTE-act-gate](runtime.md#rt-rte-act-gate)

This is the document-read branch of the supplied HTTP action route. The foreground model requests `read_memory_doc`, or a human presses the read button. The handler selects only the current run/agent filename and returns its entire text; there is no keyword, embedding, relevance ranking, section choice or query-dependent selection. ReAct appends the tool response to history and later request assembly selects a recent-message suffix. The human editor instead updates its local textarea/state. Source: SRC-1, `env/tools/tools.py`, `env/tools/registry.py`, `agent/baselines/react_160k_compact_30k.py`, `env/web/templates/_human_playground_script.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON `ok`, full `content` and UTF-8 byte count; missing file returns empty text with zero bytes.
- Later read-back: Stored text reaches a later model invocation through the tool-message history, subject to request trimming; or reaches the human textarea for inspection/editing.
- Delegated visibility: Caller sees content, not the directory or older versions. HTTP supplies agent identity; the tool has no filename argument.
- Selection predicate: Explicit caller request; deterministic run/agent addressing selects the whole latest body, not task relevance.
- Invalidation or expiry: A later write supersedes the latest body; an already delivered tool response remains until client context eviction; run deletion removes future availability.
- Activation or effect: Delivery is wired. Natural-language influence is possible but compliance and improved action are unobserved.
- Evidence limits: The 256 KiB write limit is not a read-token budget. Request assembly can evict an oversized or orphaned tool message, so API return is not proof every returned byte reaches the next model call.

> return {"ok": True, "content": content,
>             "bytes": len(content.encode("utf-8"))}
> --- `env/tools/tools.py`

#### MEM-RTE-trace-inspection
Label: Persisted trace inspection and display

This is historical inspection, distinct from the foreground accumulation and execution in [RT-RTE-react-loop](runtime.md#rt-rte-react-loop) and [RT-RTE-act-gate](runtime.md#rt-rte-act-gate). User-triggered UI loads call trace-index and chosen-step endpoints. Scoped endpoints filter agent messages; run-level endpoints expose broader trace views under the configured authorization boundary. A historical observation request with `t` also returns a stored step record, not a freshly composed observation. No automatic ReAct history reload is wired through these endpoints. Source: SRC-1, `env/web/routes_agent.py`, `env/web/templates/_human_playground_script.html`, `env/web/templates/dashboard.html`, `env/storage/agent_log.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Index entries/counts/context metadata, selected-step messages, all-trace messages, or empty/error responses where unavailable.
- Later read-back: Persisted raw messages reach human UI inspection. Markdown document read results/write arguments can be rendered as readable Markdown beside raw JSON; this is display transformation, not adoption of a new memory payload.
- Delegated visibility: Agent-scoped routes filter to that agent; admin/run-level views differ. Provider delivery is not part of this inspection path.
- Selection predicate: Requested run, agent where scoped, step or all-traces route; UI index initially chooses latest step. No semantic relevance selector or model token budget.
- Invalidation or expiry: Run-directory deletion withdraws source artifacts; missing/corrupt files can yield empty/default results. Live step records are replaced by later/final records.
- Activation or effect: UI renders retained messages for a human; behavior changes or automatic policy updates are not established.
- Evidence limits: Arbitrary external callers could implement their own reload, but unspecified callers establish only an API capability. Hermes active/compacted records are external-format evidence, not proof of external runtime model context.

The Hermes alternative opens run-local `agent/hermes_home/state.db` read-only. It selects root-session lineage (with legacy/source fallbacks), maps role/content/tool/reasoning and active/compacted flags, and groups messages by parsed observation steps. Default selection uses `active = 1`; `include_compacted` removes that filter. Stored system prompt can be reconstructed into the display. These are inspectable reader rules over externally authored SQLite data, not a local implementation of session creation, summaries or learning (SRC-1, `env/web/routes_agent.py`).

> active_filter = "" if include_compacted else "AND active = 1"
> --- `env/web/routes_agent.py:480-480`

> const response = await fetch(`${PLAYGROUND_CONFIG.traceUrl}?t=${encodeURIComponent(step)}`);
> --- `env/web/templates/_human_playground_script.html`

#### MEM-RTE-run-withdrawal
Label: Run artifact withdrawal

Distinct lifecycle route with no supplied record counterpart after comparison. `RunRegistry.delete_run` stops workers, handles busy-worker failure, kills bootstrap, waits for database leases, closes connections and removes the run directory. This removes documents, versions, traces and profiles under that directory together, rather than semantically rejecting individual notes. `unload` is different: its documented responsibility drops in-memory runtime while retaining disk artifacts. Source: SRC-1, `env/web/runner.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deleted/not-found/busy/error result; deletion can be refused or incomplete when stopping/removal fails.
- Later read-back: Successful removal withdraws future disk-backed document/trace/profile reads; existing client/provider copies are not recalled.
- Delegated visibility: Registry controls local filesystem/process lifecycle; it does not delete remote provider state or exported evaluation results.
- Selection predicate: Caller requests deletion of a run directory recognized by database or agent-subdirectory presence; no content-quality selector.
- Invalidation or expiry: Successful directory removal invalidates all retained local artifacts beneath it. Unload alone does not.
- Activation or effect: Destructive local cleanup, not selective memory revision or proof of secure erasure.
- Evidence limits: No executed deletion, race or crash tests; caller intent is not necessarily human, and remote retention is outside the boundary.

> """Stop the worker, drop in-memory state, and remove the run directory.
> --- `env/web/runner.py`

### Claims

#### MEM-CLM-state-boundary
Label: Simulator checkpoints are not agent summaries

Claimed operation: simulator persistence retains symbolic business/runtime state; dashboard replay and rehydration consume different forms. Source: SRC-1, `env/storage/snapshot.py`, `env/storage/replay.py`, `env/web/runner.py`, `env/web/routes_dashboard.py`, `env/core/simulator.py`. This expands the persistence distinction in [RT-RTE-react-loop](runtime.md#rt-rte-react-loop), not a duplicate route. Delta JSON includes changed products, full agent blobs, changed orders/events and survival state. Gzip checkpoints contain product mutable state. Replay chooses a cached prior frame or nearest checkpoint and applies subsequent deltas for dashboard as-of views. SQLite rehydration loads scenario/products/cash/listings and reconstructs ratings; it does not reload baseline Python history. The idempotency cache instead supplies cached successful mutation results for protocol replay, as covered by [RT-CLM-http-controls](runtime.md#rt-clm-http-controls). These are symbolic recovery/domain consumers, not a raw-trace-to-adopted-advice transformation. Terminal metrics in [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval) likewise do not establish successor selection.

> """On-demand replay frame reconstruction for dashboard as-of views."""
> --- `env/storage/replay.py`

#### MEM-CLM-telemetry-limits
Label: Context and evolution telemetry are not learning evidence

Claimed operation: ReAct reports `compacted` when compaction is pending; leaderboard code counts reported compactions and supplied `skills_evolutions` context fields. Auxiliary usage accepts delayed review token/cost metadata after the hook has closed. Sources: SRC-1, `agent/baselines/react_160k_compact_30k.py`, `env/web/leaderboard.py`, `env/web/routes_agent.py`. Distinct from the externally bounded launch in [RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch): this is an interpretation limit on retained telemetry, not a new external memory mechanism. Reported events/accounting establish neither successful summaries nor accepted skill changes, their reasons, future consumption or improved capacity. No automatic local trace-to-successor-policy route was identified in these telemetry/evaluation consumers; this does not establish absence inside external Hermes.

> if self.compaction_pending:
>             context["compacted"] = True
> --- `agent/baselines/react_160k_compact_30k.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-document-guidance
Label: Requested document to foreground guidance

Consumer: [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model), or human editor in the alternate read path. Channel: tool-result content retained in process history and surviving request selection, or textarea content. Force: natural-language information/planning guidance interpreted by the consumer; not system-message precedence, executable code or permission. Horizon: later calls in the same baseline process, and disk availability in that run after process restart if explicitly requested again. Run-local storage provides no cross-run migration. Source: SRC-1, `env/tools/registry.py`, `env/tools/tools.py`, baseline and human editor. Distinct from [RT-BAP-brief-guidance](runtime.md#rt-bap-brief-guidance): dynamic, explicitly requested notes via tool result, not static scenario brief. Model reliance is unobserved.

> "Use it to recover long-term notes, plans, supplier/product "
>                     "decisions, and open follow-ups that may have fallen out of "
>                     "the context window. Returns empty content if no document exists.",
> --- `env/tools/registry.py`

## Annotations

#### On [RT-RTE-context-trim](runtime.md#rt-rte-context-trim)

Memory-specific selection: defaults are a 160,000-token context/trigger and 30,000-token keep target, configurable by the CLI. Trigger uses previous reported prompt tokens where positive, otherwise estimated history size. Every request separately trims by estimated history budget, without subtracting system/tool-schema cost from that parameter. The suffix selector walks newest messages backward, retains at least one message even if over budget, then removes leading tool messages. A tool result can therefore disappear even after a successful document read. There is no guaranteed provider-token ceiling (SRC-1, `agent/baselines/react_160k_compact_30k.py`).

The trace-to-derived chain is conditional: raw observations/actions/results enter foreground history; reminder asks the same model to select important details; only a proposed and admitted document write yields a derived durable body; only a subsequent explicit read and surviving tool message delivers it again. No automatic extract, summary model or compulsory reason retention closes those gaps. With writes unavailable, immediate trim leaves a suffix plus notice. With writes available, pending trim follows a successful `/act` even if that action did not save anything. Older turns are removed by age rather than importance or content category. A failed act and stale-step branch can discard context without rolling back already persisted earlier writes. Existing files/traces remain independently reachable through tools or inspection APIs, not as dereferenceable pointers in the context window.

#### On [RT-RTE-react-loop](runtime.md#rt-rte-react-loop)

Besides threshold maintenance, a one-shot Forbidden retry replaces the last contiguous tool-result group with a symbolic redaction explanation and hint, then rebuilds the request. This is filtering raw context, not preservation of its facts. HTTP 425 truncates local history back to the saved pre-observation length. Per-request sanitation wraps invalid tool-call JSON in an `_invalid_json_arguments` object without installing a new memory artifact. EOS-only exchanges are not accumulated like ordinary tool turns. These are code-decided local context controls; they neither create an isolated sub-agent frame nor undo server-side traces and completed writes. Source: SRC-1, `agent/baselines/react_160k_compact_30k.py`.

> self.history[idx]["content"] = _POLICY_REDACTED_TOOL_CONTENT
> --- `agent/baselines/react_160k_compact_30k.py`

#### On [RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch)

MerchantBench writes symbolic YAML context/compression settings into the run-local home, copies external skills on first initialization and records a manifest/hash. Existing home reuse rewrites configuration without recopying initial skills. This preserves external material without establishing its origins, semantic admission or subsequent update consumers. Setup requests automatic auxiliary compression with the live runtime, but only external Hermes can establish actual raw-message-to-summary-to-model processing. Run-local home/workspace are filesystem substrates; external skill content and native memory representations are uninspected. The shipped Hermes scenario overlay explicitly denies MerchantBench document tools, unlike the default scenario; do not infer that external Hermes lacks its own memory from this denial (SRC-1, `env/web/runner.py`, `env/scenarios/agents/hermes.yaml`).

> compression_config["abort_on_summary_failure"] = False
> --- `env/web/runner.py`

## Write side

The document is whole-replacement authoring, not an automatic update after every step. Registry descriptions request concise strategy, product notes, open tasks and decisions. A compaction-triggered foreground model can derive those notes from its trace, but neither required content nor successful transformation is enforced. Human save is separately evidenced by the UI button. Generic API callers remain origin-unknown. HTTP schema/type checks, scenario grant denial and size rejection are distinct from authorship; direct handler calls coerce types instead of inheriting the HTTP contract. See [MEM-RTE-document-write](#mem-rte-document-write).

The current body is overwritten before the archive append. History retains submitted full versions and metadata, not mandatory criticism, provenance links or reasons. Empty replacement withdraws the latest content but not historical copies or trace arguments. Oversize content is rejected before file overwrite; subsequent filesystem failures have no demonstrated cross-file rollback. There is no exposed selective edit/merge or history restore in the inspected tools. A caller can reconstruct a prior body and submit it again, but no shipped automatic consumer does so ([MEM-OBJ-memory-history](#mem-obj-memory-history)).

Server trace capture is automatic raw retention, not automatic learning. Context eviction and retry redaction are automatic transformations of the local request substrate; they do not write a derived durable summary. Hermes may perform additional trace-fed changes outside the frozen implementation. Usage callbacks for checkpoint review account for tokens/cost, not the review's result or admission. Simulator checkpoints and dashboard replay retain domain state, not criticisms or revised agent strategies ([MEM-CLM-state-boundary](#mem-clm-state-boundary), [MEM-CLM-telemetry-limits](#mem-clm-telemetry-limits)). Successful deletion withdraws local artifacts together; unloading does not ([MEM-RTE-run-withdrawal](#mem-rte-run-withdrawal)).

## Read-back

The model's document route is pull: the foreground agent requests the latest body; the handler selects a run/agent address, returns full text, and the baseline appends it as a tool result. File identity does not imply task-targeted retrieval. There is no independent unsolicited document selector or automatic document injection in the inspected baseline/observation route. The only automatic push in threshold maintenance is a reminder or notice, not stored document content. The separate static brief is outside dynamic read-back ([MEM-RTE-document-read](#mem-rte-document-read), [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief)).

Working-context control is recency eviction, retry filtering and stale-step discard, not a frame popped after delegated work. The suffix survives by value; no dedicated summary survives unless the foreground agent independently saved one. Persisted traces have a wired human inspection consumer, including requested older steps, but no wired baseline reload. History versions have a writer's marker-count consumer and inspectable files, not a known model history-version consumer. External Hermes readers display active or optionally compacted session messages without establishing external runtime selection. Model-visible authority belongs to delivered text and its actual channel, not to filenames, UI labels or telemetry counters ([MEM-BAP-document-guidance](#mem-bap-document-guidance), [MEM-RTE-trace-inspection](#mem-rte-trace-inspection)).

## Integration issues

- No supplied runtime fact requires correction. Document records refine its capability descriptions; document write/read are explicitly parts of [RT-RTE-act-gate](runtime.md#rt-rte-act-gate), and local history is a part of [RT-RTE-react-loop](runtime.md#rt-rte-react-loop). Context maintenance and Hermes launch remain annotations, not duplicate routes. The persisted trace object spans both supplied runtime routes; its distinct storage identity is retained rather than redeclaring those routes.
- Qualification for isolation: [MEM-OBJ-memory-doc](#mem-obj-memory-doc) uses sanitized filenames, so intended per-agent separation for ordinary IDs is not a proof for arbitrary IDs. The inspected function permits aliasing; test examples do not cover all IDs. This limits a universal isolation conclusion without disputing ordinary test-source behavior.
- Unresolved external integration: [RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch) and [MEM-RTE-trace-inspection](#mem-rte-trace-inspection) expose profile setup and external-format retained messages. Actual summary/skill admission, rationale retention, native-memory stores, later selection and behavior remain external and uninspected. Neither setup configuration nor [MEM-CLM-telemetry-limits](#mem-clm-telemetry-limits) closes this gap.
- Unresolved exercised document chain: [MEM-RTE-document-write](#mem-rte-document-write) and [MEM-RTE-document-read](#mem-rte-document-read) are wired; no run proves that a foreground model saved relevant facts before deletion, preserved reasons or relied on the saved body. This prevents claims of semantic retention, exercised learning or benefit, not the architectural finding that notes can persist and return.
- Read-path limit: no shipped older-version restore consumer was established for [MEM-OBJ-memory-history](#mem-obj-memory-history) in the document references searched. Keep this as a bounded route limit, not system-wide absence of arbitrary external file consumers.

## Limitations and checks

Source HEAD was rechecked as `d9e5bd7519ab100193c21778aecfb59e30f24651`; the target checkout was read-only and its status was clean. Supplied member types, worker rules and record contract were read completely, including final bounded ranges. Direct source reads and supplied runtime findings are distinguished above. The source search covered document references throughout `env`, `agent` and `tests`, and trace/checkpoint/replay/rehydration consumers in the named implementation paths; no empirical or whole-repository negative is claimed. An initial search used a nonexistent test filename; the actual `tests/test_memory_doc_tools.py` was subsequently located and read. No model-version pin, private run, external Hermes implementation or causal experiment was added.

Validation: passed. The invocation-specific `commonplace-run validate-output` returned exit status 0: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” An ambiguous Hermes-reader quotation was repaired using the validator-supplied checked range; no finding was narrowed or withdrawn. Validation establishes form and quotation occurrence, not semantic truth, operation or benefit.
