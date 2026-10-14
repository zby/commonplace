---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "EvoOntology memory: versioned semantic guidance, lossy task traces, workload reuse and evolution-state consumers, including benchmark-specific alternatives."
run-id: AAS-2026-10-13-evoontology-f2d0c7992c6e-01
source-identity: https://github.com/ruc-datalab/EvoOntology
reviewed-boundary: c94389b764394379086ff25e50d0e0f4396167b4
---

# EvoOntology memory report

## Boundary and evidence

The memory boundary includes semantic version files and their selected read views; project/workload/task persistence; normalized benchmark traces; evolution hypotheses, evaluation summaries and source references; reminder checkpoints; and explorer reports. It includes both plugin delivery routes and all three shipped benchmark consumers. External host compaction, model/provider state, user data, evaluator service behavior and deployed host grants remain outside the frozen source. Their exclusion prevents claims about actual compliance, authentic observations, provider-side retention or successful learning. SRC-1 is the sole source, at the exact revision above; source layers are implementation and doctrine/design, not observed operation.

The runtime is a provisional route account. I directly inspected root models/store, the complete semantic runtime, workflow, trajectory module, trigger, evolution session, MCP dispatch and operations, structural validator, and selected explorer ranges. Added benchmark inspection covers BIRD's loader, browse/resolve and recorder/callers; DDR's manifest, retrieval and recorder; InsightBench's layer initialization, selection/dedup, result projection, manifest and optional trajectory recorder. Model loops and plugin launching otherwise rely on the supplied runtime findings. No target code, tests or examples were executed.

| Entry point or memory operation | Source path (SRC-1) | Coverage and limits |
| --- | --- | --- |
| Build authoring/publication and direct saves/selection | `evoontology/runtime/ops.py`, `evoontology/ontology/store.py` | Direct reads; [RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [RT-RTE-version-override](runtime.md#rt-rte-version-override), semantic objects below. Caller identity does not establish per-object human approval. |
| CLI/stdio semantic dispatch, resource and tools | `evoontology/runtime/mcp_server.py`, `evoontology/runtime/runtime.py` | Direct reads; annotation on [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval). Resource and tool workspace/version selection differ. |
| Workload preparation and resumed project tasks | `evoontology/workflow.py` | Direct reads; [MEM-RTE-workload-reuse](#mem-rte-workload-reuse), annotation on [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). |
| Trajectory normalization and storage | `evoontology/trajectory/trajectory.py`, `benchmarks/bird/trajectory_recorder.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/insightbench/insightbench/runner.py` | Direct bounded reads; [MEM-RTE-trace-retention](#mem-rte-trace-retention). Different payloads and version lineage; not one uniform complete trace. |
| Candidate rejection, evaluation, publication, resume | `evoontology/evolution/session.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md` | Direct reads; parts of [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session) and annotation on [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission). No internally enforced semantic diagnosis. |
| Threshold check and SessionStart reminder | `evoontology/trigger/trigger.py`, `plugins/claude-code/scripts/check-reminder.py` | Direct reads; [MEM-RTE-reminder-delivery](#mem-rte-reminder-delivery). Launcher/hook registration supported by supplied runtime; actual injection unobserved. |
| BIRD semantic consumption | `benchmarks/bird/tceo/runtime.py`, `benchmarks/bird/tceo/loader.py`, `benchmarks/bird/run_evaluation.py` | Direct reads; [MEM-RTE-bird-guidance](#mem-rte-bird-guidance). Local loader discards lifecycle state; root withdrawal rules do not generalize. Binder implementation not fully inspected; physical binding correctness unestablished. |
| DDR semantic consumption | `benchmarks/ddr_10k/tceo/runtime.py`, `benchmarks/ddr_10k/agent/data_agent.py` | Direct reads; [MEM-RTE-ddr-guidance](#mem-rte-ddr-guidance). Richer local model parsing/provider transformations not exhaustively inspected. |
| InsightBench semantic consumption and context frames | `benchmarks/insightbench/insightbench/tceo/retriever.py`, `benchmarks/insightbench/insightbench/tceo/session_manifest.py`, `benchmarks/insightbench/insightbench/agents.py`, `benchmarks/insightbench/insightbench/tceo/tool_chat.py` | Direct retrieval/setup reads; loop frames supported by [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop). [MEM-RTE-insight-guidance](#mem-rte-insight-guidance). Binding provenance starts in actual table inventory, but full binder implementation and its accuracy remain uninspected. |
| Benchmark evaluation output and adapter normalization | All three adapters in supplied runtime; `evoontology/evolution/session.py` | Adapter execution account supplied by [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation); direct reads of persisted summary/gate consumption. Raw metric implementations and dataset preparation not independently inspected here; no benefit inference. |
| Annotation and explorer reload | `evoontology/workflow.py`, `evoontology/runtime/ops.py`, `evoontology/visualization/renderer.py` | Direct reads; [MEM-RTE-explorer-projection](#mem-rte-explorer-projection). HTML payload inspected, browser behavior unobserved. |
| Cleanup/withdrawal alternatives | `evoontology/runtime/ops.py`, `evoontology/ontology/store.py`, root and benchmark retrieval files above | Direct registry/store reads: rejection preserves files; promote removes destination before copy; save overwrites; lifecycle filtering only at particular readers. No blanket deletion, retention or expiry guarantee inferred. |
| Static skills, tool schemas, opaque host context | Supplied runtime plugin/agent records | Static instructions are behavior-shaping inputs, not accumulated read-back. Host loading/compaction/delegation is uninspected and cannot be inferred from retrieval budgets. |

## Core ideas

1. Semantic memory is an explicit five-family version store, not an embedding index. IDs and links are symbolic access structure; definitions, joins, filters and cautions shape models through interpretation. Root retrieval returns the selected content plus attached evidence rather than executing its query fragments. See [MEM-OBJ-term](#mem-obj-term) through [MEM-OBJ-evidence](#mem-obj-evidence), and [RT-BAP-semantic-guidance](runtime.md#rt-bap-semantic-guidance).
2. Retention and learning are different. Traces are normalized and sometimes truncated; a foreground Evolver is instructed to diagnose and patch from them. Neither storage nor summary creation automatically installs improved semantic content. The automatic history-to-workload transformation changes later task selection, not the ontology itself ([MEM-RTE-trace-retention](#mem-rte-trace-retention), [MEM-RTE-workload-reuse](#mem-rte-workload-reuse), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).
3. Context selection is consumer-specific. Root retrieval uses active-state filtering and item/mention budgets. BIRD uses a different catalog and drops lifecycle metadata. DDR frontloads an unfiltered financial concept reference extracted from active mappings. Its optional task-ranking API is not invoked by the inspected shipped manifest callers. InsightBench maintains transient dedup history across calls and can return all known bindings for an empty resolve. None supplies a universal byte/token cap ([MEM-RTE-bird-guidance](#mem-rte-bird-guidance), [MEM-RTE-ddr-guidance](#mem-rte-ddr-guidance), [MEM-RTE-insight-guidance](#mem-rte-insight-guidance)).
4. Rejected explanations and evaluation summaries can survive into resumed evolution. Reasons survive only where the host actually fills hypotheses/notes/artifact references. The deterministic gate consumes scores/verdicts and status, not the causal explanation. Later semantic consumers receive object evidence, not automatically the experiment history that justified publication ([MEM-OBJ-hypothesis](#mem-obj-hypothesis), [MEM-OBJ-evaluation](#mem-obj-evaluation), annotation on [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-term
Label: Term records

Source-native identity: Term objects from `versions/<v>/terms.json`. Storage substrate: workspace JSON; parsed into ID-indexed dataclasses. Form: symbolic ID/type/aliases/lifecycle/evidence references, with natural-language name, definition and scope consumed by models; token matching consumes those same strings symbolically. Lineage: Builder/Evolver proposals based on authorized workload and native data evidence, under host instructions; initial correctness is not established by serialization. Write control: host/model authors content, generic MCP caller saves it; user workflow authorization is not per-term approval. Root consumers select active/validated terms and deliver definition/scope and attached objects. No supplied operative-object counterpart: closest is [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval), a route over these objects, not their container. Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/ontology/store.py`, `evoontology/runtime/runtime.py`; authoring responsibility from [RT-RTE-build-publication](runtime.md#rt-rte-build-publication).

> definition=str(data.get("definition", "")),
> scope=str(data.get("scope", "")),
> aliases=list(data.get("aliases", [])),
> --- `evoontology/ontology/models.py`

#### MEM-OBJ-mapping
Label: Mapping records

Source-native identity: Mapping objects from `versions/<v>/mappings.json`. Substrate: JSON, then dataclasses. Form: symbolic term/table/column associations and evidence IDs; semantic_filter, aggregation_semantics, grain and validation prose are interpreted guidance at root delivery, not executed rules. Lineage/control: same host proposal/save/publication mechanisms as [MEM-OBJ-term](#mem-obj-term); evidence references can come from validation.evidence. Root resolve delivers active mappings for the selected term but omits database_source, validation description and confidence. Meaning and trust therefore cannot be inferred from the richer stored record alone. Distinct from [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval); no supplied object counterpart. Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`.

> "semantic_filter": m.semantic_filter,
> "aggregation_semantics": m.aggregation_semantics,
> "grain": m.grain,
> "evidence_refs": list(m.evidence_refs),
> --- `evoontology/runtime/runtime.py`

#### MEM-OBJ-relation
Label: Relation records

Source-native identity: Relation objects from `versions/<v>/relations.json`. Substrate: JSON/dataclasses. Form: symbolic source/target/type/evidence links; natural-language connection condition and description. Host authors/adopts relations through the same save/publication controls as terms. Root resolve selects active incoming or outgoing relations for a term and sends connection_condition but not description; the model decides whether/how to use the join. No independent enforcement of that condition at native execution. Distinct from closest [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval). Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`.

> for r in self.store.relations.values()
> if _is_active(r) and (r.source == term_id or r.target == term_id)
> --- `evoontology/runtime/runtime.py`

#### MEM-OBJ-constraint
Label: Constraint records

Source-native identity: Constraint objects from `versions/<v>/constraints.json`. Substrate: JSON/dataclasses. Form: symbolic target/severity/lifecycle/trigger keywords/evidence IDs plus natural-language description/scope. Host proposal and admission as for terms. Root resolve selects active constraints whose target equals the selected term; it sends severity, description and evidence references. A severity named block is still interpretive guidance at this consumer, not a native-query veto. Structural validation also permits a mapping target, but root resolve does not retrieve a constraint merely because it targets an attached mapping. Distinct object from closest [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval). Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`, `evoontology/validate.py`.

> for c in self.store.constraints.values()
> if _is_active(c) and c.target == term_id
> --- `evoontology/runtime/runtime.py`

#### MEM-OBJ-evidence
Label: Evidence records

Source-native identity: Evidence objects from `versions/<v>/evidence.json`. Substrate: JSON/dataclasses. Form: symbolic IDs/timestamps/references and text source/query/result/validation_method; root loading casts these content fields to strings. They are retained assertions about grounding, not authenticated execution receipts. Host supplies them; validation checks references and loading, not replay. Root resolve collects referenced evidence from the term and all included related objects, deduplicates IDs, and sends all six evidence fields. The apparent compactness is a display description, not an enforced content-length budget. Distinct from [RT-RTE-task-execution](runtime.md#rt-rte-task-execution): task observations are a possible input to authoring, not identical semantic evidence. Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`, `evoontology/validate.py`.

> "source": evidence.source,
> "query": evidence.query,
> "result": evidence.result,
> "validation_method": evidence.validation_method,
> "timestamp": evidence.timestamp,
> --- `evoontology/runtime/runtime.py`

#### MEM-OBJ-trajectory
Label: Task trajectories

Source-native identity: per-task JSON under `trajectories/<task_id>.json`. Substrate: workspace files; supplied raw benchmark logs remain elsewhere. Form: symbolic task/version/split/status/events plus question, tool arguments/results and final answer payloads interpreted by Evolver/Judge. Root workflow preserves an ordered events list as well as classified calls; benchmark message normalization stores separate semantic/native lists, not one complete ordered transcript. Native previews are derived lossy traces, not newly inferred domain knowledge; result_summary reports size, not semantic content. These are distinct from semantic evidence and from the lifecycle container [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session). Closest supplied route is [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). Acquisition, write control and later consumers are in [MEM-RTE-trace-retention](#mem-rte-trace-retention). Evidence: SRC-1, `evoontology/trajectory/trajectory.py`, `evoontology/workflow.py`.

> Agent prose and chain-of-thought are intentionally not persisted. Only
> observable tool inputs/results and the final answer are retained.
> --- `evoontology/trajectory/trajectory.py`

#### MEM-OBJ-workload
Label: Project and workload records

Source-native identity: project.json and workload/questions.json. Substrate: workspace JSON. Form: symbolic data-source/mode/boundary/task identifiers and provenance links, natural-language question text/topics interpreted by host models. Lineage: supplied questions, compatible trajectory history and explicitly supplied grounded generated questions; Python normalizes/deduplicates/orders them but does not invent questions. Later consumer: prepare/start_task and instructed Builder/Evolver. Generic configure/prepare callers control replacement/input; the origin label user alone does not authenticate a human decision. Distinct from closest [RT-RTE-task-execution](runtime.md#rt-rte-task-execution): these are inputs, not execution traces. Evidence: SRC-1, `evoontology/workflow.py`; [MEM-RTE-workload-reuse](#mem-rte-workload-reuse) covers admission and selection.

> # An explicit scope restriction affects this selection, not saved history.
> --- `evoontology/workflow.py`

#### MEM-OBJ-hypothesis
Label: Evolution hypotheses and rejected-round notes

Part of: [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session)

Operative part: current_hypothesis in run.json and hypothesis/notes/artifact_refs in rounds.jsonl. Storage: workspace JSON/JSONL. Form: natural-language explanation/criticism, with symbolic candidate/round links; not a rule interpreted by the gate. Lineage: host Diagnose/Attribute/Patch, supplied trace and exploration evidence. begin_round requires nonempty text; record_round persists rejection with current hypothesis/notes, not mandatory structured causal premises or full edit diff. Later consumer: host resumption and next-round diagnosis, requested by the skill; core reads decision counts rather than hypothesis meaning. Reasons are retained where authored, but reuse is claimed rather than observed. Theory properties remain separately assessed in [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission), not redefined here. Evidence: SRC-1, `evoontology/evolution/session.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.

> "hypothesis": run.get("current_hypothesis", ""),
> "candidate": run.get("current_candidate", ""),
> "metrics": metrics or {},
> "decision": decision,
> "artifact_refs": list(artifact_refs or []),
> "notes": str(notes or ""),
> --- `evoontology/evolution/session.py`

#### MEM-OBJ-evaluation
Label: Evaluation summaries and gate input

Part of: [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session)

Operative part: evaluations/round...json with subject/role/round, metrics, cases, artifact_paths, provenance, gate_input and timestamp. Substrate: workspace JSON. Form: symbolic/numeric scores/verdict fields consumed mechanically, with opaque caller-provided case payloads/path references interpreted by host readers. Numeric metrics are localized symbolic observations, not model weights. Lineage: caller-normalized adapter observations; raw artifacts are referenced, not copied. record_evaluation admits summaries while running; accept selects current-round/current-candidate records with gate_input, recomputes checks and can veto publication. Caller authentication, independent scoring and artifact freshness remain unestablished. Later consumers differ: gate receives full gate_input; explorer receives only terminal aggregate projections; host can access run artifacts by instructed reads. Evidence: SRC-1, `evoontology/evolution/session.py`; closest route [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation).

> Raw artifacts stay at
> their benchmark/user location; only the summary and path references
> are copied into the run.
> --- `evoontology/evolution/session.py`

#### MEM-OBJ-source-references
Label: Confirmed trajectory source references

Part of: [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session)

Operative part: trajectory-sources.json stores path/scope/purpose/confirmed_at, not trajectory content. Substrate: workspace JSON. Form: symbolic filesystem pointers and natural-language scope/purpose. Generic caller supplies entries; Python requires only a nonempty path and stamps time. User confirmation and verifying reused paths are skill obligations, not authenticated by confirmed_at. Later consumers: trajectory_sources and previous_trajectory_sources return current/newest earlier reference lists, and the skill directs the host to locate/read relevant traces. This is not an automatic content loader nor an independently observed later diagnosis route. Evidence: SRC-1, `evoontology/evolution/session.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.

> Only references are stored; trajectory files are never copied. Each
> entry needs a ``path`` and may carry ``scope`` and ``purpose``; core
> stamps ``confirmed_at``.
> --- `evoontology/evolution/session.py`

#### MEM-OBJ-checkpoint
Label: Evolution checkpoint state

Source-native identity: state.json checkpoint_trajectory/checkpoint_time/evolution_due/thresholds, with legacy fields accepted. Storage: workspace JSON. Form: symbolic task pointer/time/Boolean/count thresholds consumed by deterministic code. initialize preserves existing valid time/pointer; check recomputes due; acceptance advances checkpoint to the most recent trajectory when no ID supplied. It stores access/selection metadata, not semantic task experience or a summary. Later consumer: reminder trigger and instructed batch selection. Caller/user control of original threshold values is unresolved; core defaults are 30 tasks or seven days. Distinct from [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session): workspace trigger state outside run directories; closest route [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission). Evidence: SRC-1, `evoontology/trigger/trigger.py`.

> if last_trajectory_id is None:
>     all_trajs = self.trajectories.list_since(None)
>     if all_trajs:
>         last_trajectory_id = str(all_trajs[-1].get("task_id"))
> --- `evoontology/trigger/trigger.py`

#### MEM-OBJ-version-report
Label: Version annotations and explorer payload

Source-native identity: reports/<version>.json and generated visualizations/ontology-layer-explorer.html. Substrate: workspace JSON/HTML. Form: natural-language summary/limitations, symbolic question/object/version links and projected terminal metrics/task answers. Lineage: caller-authored annotation plus deterministic build_experience and graph/tool rendering. annotate verifies linked question/object existence, not the truth of summary; accept_evolution copies the candidate annotation to the official version if it exists. Later consumer: human explorer; no inspected model-context injection of the HTML. Distinct from closest [RT-RTE-build-publication](runtime.md#rt-rte-build-publication) and [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission), which present rather than identify this payload. Evidence: SRC-1, `evoontology/workflow.py`, `evoontology/runtime/ops.py`, `evoontology/visualization/renderer.py`; [MEM-RTE-explorer-projection](#mem-rte-explorer-projection).

### Routes

#### MEM-RTE-workload-reuse
Label: History-to-workload reuse

Endpoints/owner: prepare request → Python reads project/existing questions/eligible local trajectories and caller lists → normalization, provenance merge and selection → persisted catalog/tool reply → Builder or start_task. This is an automatic trace-fed derivation of questions and provenance, not automatic semantic editing. Distinct sub-operation supporting [RT-RTE-build-publication](runtime.md#rt-rte-build-publication) and [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), not a duplicate complete route. Mode: fixed_split disables automatic history/generated input and checks registered construction IDs; rolling mode admits same-source history, excludes validation/heldout/test local traces, requires construction purpose and evidence_refs for generated input. Host supplies generated content; Python does not assess grounding quality. Generic caller chooses flags/inputs, no mandatory per-question human approval. Incorrect inputs can be rejected by checks; selection restrictions do not erase catalog history, and caller can reconfigure/prepare again. No answer oracle. Evidence: SRC-1, `evoontology/workflow.py`.

- Immediate return: selected questions, origin counts, coverage gaps and next-action guidance.
- Later read-back: questions.json catalog is reused by prepare and start_task; traces can seed later construction/evolution work.
- Delegated visibility: selected question objects reach the requesting host via tool reply; no sub-agent dispatch.
- Selection predicate: normalized question text, matching source, allowed split/purpose/provenance; user priority before history before generated; recency then novel topic coverage. All user questions survive, so limit is not a hard total-count bound.
- Invalidation or expiry: explicit restrictions affect current selection, not deletion of saved history; incompatible data sources are filtered on preparation/start.
- Activation or effect: wired catalog transformation/task-input selection; improved analysis and actual host use unobserved.
- Evidence limits: evidence_refs and origin labels do not authenticate evidence; normalization is not semantic near-duplicate detection promised by evolution instructions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Retain all user questions; fill remaining slots with diverse topics first.
> selected = [q for q in ordered if q["origin"] == "user"]
> --- `evoontology/workflow.py`

#### MEM-RTE-trace-retention
Label: Task trace retention

Endpoints/owner: completed workflow task or benchmark recording point → deterministic event/message projection → TrajectoryStore write → later count/history/host diagnosis. This storage/normalization operation overlaps [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) and [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop), but does not duplicate their execution loops. Callers supply observations; built-in SQLite obtains its own bounded result. Python stores them, without semantic adoption. Human review is not a write precondition; external caller integrity remains unresolved. Same task ID overwrites rather than appending an immutable event ledger. Rejection checks task/event identity and completion shape, not all benchmark trace semantics. Recovery: workflow task files allow resume; omitted full outputs need external raw artifacts, not reconstruction from a size summary. Evidence: SRC-1, `evoontology/trajectory/trajectory.py`, `evoontology/workflow.py`, `benchmarks/bird/trajectory_recorder.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/insightbench/insightbench/runner.py`.

- Immediate return: task/record ID, persisted terminal workflow task or benchmark result.
- Later read-back: stored trajectories feed deterministic reminder counts and workload reuse; skill requests Evolver/Judge diagnosis of retained observations. No automatic ontology patch follows append.
- Delegated visibility: recording itself is local; host tools return task state; benchmark driver keeps separate raw outputs/logs that may be referenced later.
- Selection predicate: workflow records submitted events; from_message_trace retains matched tool_call/tool_result pairs and terminal answer, classifies only browse/resolve as semantic. BIRD/DDR keep semantic payloads but truncate native results; workflow truncates all submitted event results. InsightBench keeps semantic event IDs/status and final insights/summary, with an empty native-tool list.
- Invalidation or expiry: append writes one file per task_id; BIRD identified batch questions and InsightBench flag IDs overwrite on repeat. Corrupt/unreadable files are skipped by TrajectoryStore._all; no expiry enforced there.
- Activation or effect: wired retention and later metadata/task-selection use; content-directed diagnosis/adoption is instructed and unobserved.
- Evidence limits: no complete reasoning history, no guaranteed cross-family execution order after benchmark normalization, no authenticated manual events. BIRD recorder reads active version at recording even when execution selected an explicit candidate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> preview = "\n".join(lines[:_RESULT_MAX_LINES])[:_RESULT_MAX_CHARS]
> --- `evoontology/trajectory/trajectory.py`

> ontology_version = SemanticStore.active_version(store_path)
> task_id = make_task_id(db_id, question, question_id)
> --- `benchmarks/bird/trajectory_recorder.py`

#### MEM-RTE-reminder-delivery
Label: Checkpoint reminder delivery

Endpoints/owner: Claude SessionStart hook → initialize/check active workspace and immediate child workspaces → automatic threshold selector → generated context/user message; Codex's status request returns state/check on demand. Distinct reminder sub-route from [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission), which only starts when a caller acts. Evidence: SRC-1, `plugins/claude-code/scripts/check-reminder.py`, `evoontology/trigger/trigger.py`, `evoontology/runtime/ops.py`; registration and Codex policy from supplied runtime.

- Immediate return: hook JSON with systemMessage and additionalContext when due; otherwise silent exit. MCP status returns checkpoint and check numbers.
- Later read-back: prior checkpoint and trajectory timestamps determine future reminders; message contains reason/workspace, not trace content.
- Delegated visibility: hook output is intended for automatic host context injection and visible user message; no Evolver launch.
- Selection predicate: active.json presence and count since checkpoint OR elapsed days; default 30/seven; checkpoint task timestamp gives an exclusive boundary. Missing checkpoint task causes list_since to return all trajectories.
- Invalidation or expiry: acceptance resets checkpoint/evolution_due; elapsed time/count recomputed on check; rejected/incomplete candidates do not advance through their lifecycle paths.
- Activation or effect: wired reminder generation and state update; host injection/action unobserved.
- Evidence limits: no content relevance filter in counting; latest-task checkpoint may cover more than an explicitly frozen evaluation batch; external host behavior is not established by printed JSON.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "hookEventName": "SessionStart",
> "additionalContext": context,
> --- `plugins/claude-code/scripts/check-reminder.py`

#### MEM-RTE-bird-guidance
Label: BIRD semantic guidance

Endpoints/owner: driver selects version → local loader/binder → manifest at fresh agent setup and model-requested browse/resolve → guidance/native verification. Consumer-specific part of the semantic delivery discussed by [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop), distinct from root [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval). Evidence: SRC-1, `benchmarks/bird/tceo/loader.py`, `benchmarks/bird/tceo/runtime.py`, `benchmarks/bird/run_evaluation.py`.

- Immediate return: manifest counts/workflow and local term catalog or definition/mapping/relation/constraint/evidence replies.
- Later read-back: selected persistent versions loaded at later evaluations/tasks; returned record content guides model choices, not automatic query execution.
- Delegated visibility: driver passes semantic_manifest to the agent and version into configured semantic servers; model gets tool replies through the benchmark loop.
- Selection predicate: ID/column binding/name/alias/substring and weighted token/name/alias/definition/table matching; browse default five, configured maximum defaults eight and can be changed; empty query returns first catalog items. Resolve first five mentions; no lifecycle field is loaded into these local records.
- Invalidation or expiry: local loaded layer persists until recreated; direct selector/content edits affect later loads, not necessarily existing in-memory views. Optional workspace manifest.md can override the loader's displayed version string without changing loaded records.
- Activation or effect: wired delivery of guidance; correctness and exercised model influence unobserved.
- Evidence limits: term-linked evidence bodies are attached, mapping/constraint references are not followed into evidence bodies; relation output omits evidence refs. Inactive semantic content can remain reachable because the loader discards lifecycle. BIRD recording can mislabel explicit candidate execution as active-version experience.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "note": f"Showing first {min(limit, len(items))} of {catalog_total} terms. "
>         f"Provide a specific query for targeted results.",
> --- `benchmarks/bird/tceo/runtime.py`

> for ev_ref in term.evidence_refs:
>     if ev_ref in self.loader.evidence:
> --- `benchmarks/bird/tceo/runtime.py`

#### MEM-RTE-ddr-guidance
Label: DDR semantic guidance

Endpoints/owner: local VersionedSemanticStore/layer → manifest without task filtering plus model-requested semantic tools → DDR agent decisions. Distinct consumer-specific route from root retrieval; included in [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop). Code owns context selection; model owns query adoption. Evidence: SRC-1, `benchmarks/ddr_10k/tceo/runtime.py`, `benchmarks/ddr_10k/agent/data_agent.py`.

- Immediate return: manifest with financial concepts and optionally semantic_filter values as fact_names; browse summaries and resolve objects.
- Later read-back: versions reach subsequent task loads; DDR trajectory recorder uses the loaded layer.version rather than rereading the active pointer.
- Delegated visibility: startup generates a manifest with exposed_tools/include_fact_names; start_session regenerates it with exposed_tools only and places it alongside the task in the system prompt. Neither passes task to manifest. The semantic resource caller also omits task. Requested tool results enter session history. Evidence: SRC-1, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/ddr_10k/tool_server/semantic_mcp.py`.
- Selection predicate: shipped manifest callers extract all concept/fact_name entries from active mappings with nonempty semantic_filter, without task ranking or the 15-concept cap. The optional manifest(task=...) API keeps available members of ten named core concepts then token-ranked extras up to 15 concepts, including zero-overlap extras when slots remain; a scoped search of DDR Python manifest callers found no shipped invocation supplying task. This is an optional filtering capability, not ordinary delivered targeting. Browse caps six; resolve first five; active-state filtering; unresolved mention cache short-circuits repeated misses.
- Invalidation or expiry: transient unresolved cache lasts for the layer object; stored version files survive; new load can see revisions.
- Activation or effect: wired semantic delivery; model adherence and benefit unobserved.
- Evidence limits: manifest promises sample_query/SQL-ready output but inspected _build_resolve_result attaches mappings, relations, constraints and evidence IDs, not a sample_query or evidence bodies. Concept/item caps do not bound text or aliases/fact_names per concept.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if task:
>     key_metrics = self._filter_concepts_by_task(task, key_metrics)
> --- `benchmarks/ddr_10k/tceo/runtime.py`

> self.prompt_manager.semantic_manifest = self._semantic_layer.manifest(
>     exposed_tools=self._semantic_tools,
> )
> --- `benchmarks/ddr_10k/agent/data_agent.py`

> # Fill up to MAX_CONCEPTS with best-matching extras
> for term_key, fact_names, score in scored_extras:
>     if len(filtered) >= MAX_CONCEPTS:
>         break
>     filtered[term_key] = fact_names
> --- `benchmarks/ddr_10k/tceo/runtime.py`

#### MEM-RTE-insight-guidance
Label: InsightBench semantic guidance and dedup

Endpoints/owner: set_table → actual-table inventory and loaded version/binder → enriched schema and local layer → stage model requests → scoped/deduplicated objects. Code owns projection/dedup, model owns requests and use. Distinct local consumer from root retrieval and material sub-route of [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop). Evidence: SRC-1, `benchmarks/insightbench/insightbench/agents.py`, `benchmarks/insightbench/insightbench/tceo/retriever.py`, `benchmarks/insightbench/insightbench/tceo/session_manifest.py`; stage framing supported by supplied runtime.

- Immediate return: browse at most four items, resolve definitions/mappings/relations/constraints and current task bindings; empty resolve returns full known column-to-concept table. Manifest generator returns only version/count/tool/use text, not bindings.
- Later read-back: retained semantic version loaded for later tables/tasks; transient dedup is current-session selection metadata, not revised persistent ontology. Semantic event projections may later be retained as trajectories.
- Delegated visibility: model receives selected tool replies in its stage frame; enriched table schema can enter caller-generated stage prompts. Earlier stage transcripts stay outside unless supplied by the caller; stage terminal text crosses back.
- Selection predicate: optional domain and scope, active-state checks on normal term search/attached objects, column shortcut and name/alias/substring search; browse tracks prior IDs, resolve suppresses previously resolved mention/term pairs. Tool schema maxItems five is not enforced by resolve's Python loop, which processes all mentions.
- Invalidation or expiry: reset_session clears resolve/browse history; set_table creates a new layer/events list. No automatic transcript compaction is established by dedup. Stored content remains reachable through later layer creation.
- Activation or effect: wired filtering/binding delivery; no exercised activation or improved capacity established.
- Evidence limits: browse history replaces each normalized query's ID set, so exclusion is not an everlasting all-seen ledger; skipped count also includes ranked items excluded by the per-call limit. Evidence IDs are exposed but not their bodies. Column shortcut does not repeat the normal search's scope/lifecycle checks; binder enforcement remains uninspected. No universal byte budget or blanket withdrawal guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._browse_history[norm_q] = frozenset(item["id"] for item in fresh_items)
> --- `benchmarks/insightbench/insightbench/tceo/retriever.py`

> del inventory, task_bindings
> --- `benchmarks/insightbench/insightbench/tceo/session_manifest.py`

#### MEM-RTE-explorer-projection
Label: Explorer experience projection

Endpoints/owner: caller annotation/render → stored reports plus versions/trajectories/run evaluations → deterministic HTML embedding → later human review. Distinct presentation sub-route supporting both [RT-RTE-build-publication](runtime.md#rt-rte-build-publication) and [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission). Generic caller authors summary/limitations/links; Python checks identifier existence, projects data and copies candidate reports on accept. Human content approval is not enforced. Re-render replaces stable HTML; it does not admit a semantic update. Evidence: SRC-1, `evoontology/workflow.py`, `evoontology/runtime/ops.py`, `evoontology/visualization/renderer.py`.

- Immediate return: annotation/report or HTML path/presentation status.
- Later read-back: renderer reloads all version directories, annotations, public trajectories and related run state each time; the HTML is a snapshot for later human browsing.
- Delegated visibility: presentation URL/file delivered to caller; no direct model prompt injection established.
- Selection predicate: selected initial version but all available versions embedded; public task examples exclude validation/heldout/test; accepted-version view also includes current-candidate trajectories of its accepting run. Only accepted/incomplete run aggregate evaluations are projected; cases, gate_input and raw paths are omitted.
- Invalidation or expiry: annotation overwrites same version report; generated HTML changes on render, not automatically when upstream files change. Old versions and rejected candidates can still appear in all-version embedding.
- Activation or effect: wired derived display; actual browser review/adoption unobserved.
- Evidence limits: public replay filtering is not an isolation boundary over all on-disk artifacts; version matching and stored labels determine visibility. Aggregate display cannot reconstruct missing raw evidence or causal rationale.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Validation remains isolated from candidate design. Only terminal-run
> # aggregate metrics are embedded; task examples come from public replays.
> --- `evoontology/workflow.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval)

Memory selection is request-driven: caller picks workspace/version/query/mentions; code selects object content. Root browse filters active/validated objects, requires query, ranks token overlap plus phrase match, rejects its hard-coded contradictory token pairs, and delivers up to six compact views. Resolve selects first five nonempty mentions, matches active term ID/name/alias/token sets and can break ties using context. Attached active mappings, incoming/outgoing relations, term-target constraints and deduplicated evidence are all delivered without a byte budget. Ambiguous results can include every matching candidate and attachments. Root manifest sends counts/usage, not the entire store. MCP serializes results as text; resource reads reload server workspace/version rather than tool overrides. Persistent five-family objects are described in this member, not re-declared here. Authority is interpretive at the model, not a database execution rule. Evidence: SRC-1, `evoontology/runtime/runtime.py`, `evoontology/runtime/mcp_server.py`.

> if evidence_id in seen:
>     continue
> seen.add(evidence_id)
> view = self._evidence_view(evidence_id)
> --- `evoontology/runtime/runtime.py`

#### On [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Task files store original question/source, concrete version name, ordered events, classified calls, errors and terminal answer. record_event applies truncate_result even to semantic results; resolve_task returns the complete resolution immediately but retains a potentially truncated task event. Oversized payloads become first 20 lines/2000 characters plus a size summary. The full payload is not stored in another checkpoint by this path. The SQLite result already has a separate 100-row cap before event normalization. Version pinning is by mutable name, not content hash. Later host resumption uses task files; completed trajectories reach history/diagnosis. Generic manually supplied events remain unauthenticated; built-in execution has direct lineage. Evidence: SRC-1, `evoontology/workflow.py`, `evoontology/trajectory/trajectory.py`.

> event = {"event_id": event_id, "tool": tool, "input": arguments,
>          **truncate_result(result), "error": error}
> --- `evoontology/workflow.py`

#### On [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session)

The lifecycle container mixes stored explanation, references, evaluation payloads and mechanical status. The three declared parts separate interpretation/consumer differences. Core resume returns durable run state, previous-source reuse returns references; file existence and source validity remain host checks. Rejected notes can survive rounds, but a next begin_round replaces current_hypothesis in run.json; round retention is through the host's record_round calls. The container does not automatically preserve every proposed hypothesis or copy every raw trajectory. Evidence: SRC-1, `evoontology/evolution/session.py`.

#### On [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)

Write/read-back chain: retained task observations and current objects → host-requested diagnosis/attribution → hypothesis, candidate semantic files, notes and evaluation summaries → mechanical accept/reject → selected semantic files → later root/plugin/benchmark consumers. This is a model-mediated trace-fed update opportunity, not an automatic core learning transformation. The skill directs later rounds to read previous evolution records and preserve rejected explanations. The session mechanically counts rejections, selects supplied current-candidate gate_input and publishes five-family files; hypothesis meaning does not enter the gate. Candidate reasons remain in run/round artifacts and semantic evidence where authored; ordinary semantic delivery does not automatically attach experiment history. Accept wrapper copies annotations, not tool/runtime modifications. Rejection/incomplete preserves selector within the session route and leaves candidate/evaluation files retained. Independent saves/selection can bypass this admission. Evidence: SRC-1, `evoontology/evolution/session.py`, `evoontology/runtime/ops.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`; supplied runtime passage supplies gate/bypass support.

> Do not rely only on current conversation context. Reuse persisted project and
> evolution state whenever available.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

#### On [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop)

Working-context control differs from stored memory. Supplied runtime establishes fresh BIRD task sessions, full BIRD/DDR history translation, and InsightBench's fresh ToolCallingChat message list per call. A stage frame keeps other stage transcripts out; caller-selected stage inputs enter and terminal text escapes, while the layer remains separately reachable. This resembles a temporary call frame, but returned semantic content is by value: a retained ID is not a model-window reference with automatic dereference/liveness. Transient dedup may withhold a reply even after a preceding frame's transcript is no longer supplied. reset_session permits re-resolution; there is no demonstrated durable summary replacing those frames. Console truncation, trace retention truncation and per-turn budgets are not model-window trimming. Evidence: supplied runtime record and SRC-1, `benchmarks/insightbench/insightbench/tceo/retriever.py`; actual host compaction remains external.

## Write side

Semantic authorship is host/model work guided by Build/Evolve, not deterministic inference. The save API checks family lists/path components and physically writes JSON; initial publication adds structural/reference/load validation; evolution acceptance adds recorded gate checks. These are different admission mechanisms. User request/scope/budget authorization does not imply human approval of every semantic record. A generic administrative caller can replace named content or choose an existing directory without the evaluation gate ([RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [RT-RTE-version-override](runtime.md#rt-rte-version-override)). Source trust is consequently caller/host-dependent. Evidence: SRC-1, `evoontology/runtime/ops.py`, `evoontology/ontology/store.py`, `evoontology/validate.py`.

Trace acquisition is separate. Root workflow records submitted events and native SQLite results; BIRD/DDR message normalization discards agent prose and truncates native results, while InsightBench retains semantic event projections without native observations. Workload reuse mechanically extracts questions/provenance from eligible history; this automatic trace-fed transformation can change a later build/task input, but does not produce new semantic claims. A model-directed patch is the point where interpreted experience can become behavior-shaping ontology content. Original trace provenance includes human-supplied/generated questions, native results and potentially opaque caller-supplied observations, not one trusted origin ([MEM-RTE-trace-retention](#mem-rte-trace-retention), [MEM-RTE-workload-reuse](#mem-rte-workload-reuse)).

Maintenance/withdrawal has several effects, not one delete operation. Non-active root objects are omitted at retrieval, not removed from stored versions. Rejection retains candidate files and round evidence; incomplete retains parent selection/checkpoint in that route. Later explorer loads every version, including rejected candidates. BIRD's local loader drops lifecycle fields, so marking an object inactive alone does not reliably withdraw it from that reader. Direct save/promote can overwrite/remove destination content; publish refuses different official content but active selection is a separate write. A preserved version name is not an immutable historical artifact. Evidence: SRC-1, `evoontology/ontology/store.py`, `evoontology/runtime/runtime.py`, `benchmarks/bird/tceo/loader.py`, `evoontology/visualization/renderer.py`; [MEM-RTE-bird-guidance](#mem-rte-bird-guidance), [RT-RTE-version-override](runtime.md#rt-rte-version-override).

## Read-back

Root/plugin semantic consumption is pull: manifest/resource or browse/resolve request → code-selected persisted content → text reply → host model. Targeting and budgets are described in the semantic annotation. Ordinary direct semantic calls are not automatically task-recorded. A current task's resolve uses its version name; a fresh root call reloads current selection unless explicit version supplied. Neither storage API nor the ability to fetch source references establishes that a later model actually read them (SRC-1, `evoontology/runtime/mcp_server.py`, `evoontology/workflow.py`).

Included benchmark consumers read selected semantic versions at setup and on tool requests. DDR additionally supplies a financial concept reference during task initialization; this is requested task setup, not an independent unsolicited event. Its shipped manifest callers select by active mapping and nonempty semantic_filter, not task relevance, and do not invoke the optional 15-concept filter. Placing task and manifest in the same prompt does not establish task-conditioned manifest selection. BIRD's and InsightBench's evidence projection differs materially from root's. Transient dedup is selection control, not persisted semantic curation. Selection metadata cannot substitute for the earlier reply if that reply is absent from a later frame ([MEM-RTE-bird-guidance](#mem-rte-bird-guidance), [MEM-RTE-ddr-guidance](#mem-rte-ddr-guidance), [MEM-RTE-insight-guidance](#mem-rte-insight-guidance)).

Claude's SessionStart reminder is the inspected unsolicited supply route: code selects active workspaces and threshold metadata and emits a short reason/action instruction, not accumulated semantic content. Codex obtains the same status by requested call. Evolution skill reads of previous knowledge and reports are an afforded/instructed host route, not automatic injection. Explorer read-back instead serves human review through a derived HTML snapshot; it deliberately reduces evaluation data ([MEM-RTE-reminder-delivery](#mem-rte-reminder-delivery), [MEM-RTE-explorer-projection](#mem-rte-explorer-projection), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)).

## Integration issues

- Correction of this member's previous DDR account: [MEM-RTE-ddr-guidance](#mem-rte-ddr-guidance), Core ideas and Read-back now distinguish optional manifest(task=...) filtering from shipped delivery without task. Startup, session regeneration and the semantic resource caller omit the argument; scoped search `manifest\(` over DDR Python files found no shipped caller passing it. Ordinary manifest delivery therefore has neither task ranking nor that filter's 15-concept cap. Evidence: SRC-1, `benchmarks/ddr_10k/tceo/runtime.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/ddr_10k/tool_server/semantic_mcp.py`; minimum passages are in the route.
- Carried verification limit: InsightBench's semantic route and normalized trajectories are not its complete recovery/history inventory. The supplied refusal identifies RuntimeError fallback to baseline generate_code without a semantic manifest, and checkpoint reload of insights_history/semantic_events used by later question selection or summarization (SRC-1, `benchmarks/insightbench/insightbench/agents.py`). Those answer/history payloads differ from [MEM-OBJ-trajectory](#mem-obj-trajectory). This correction did not independently trace that additional inventory; withhold claims that every execution uses ToolCallingChat, that fallback retains semantic-tool delivery, or that normalized trajectories exhaust retained analytical history. [MEM-RTE-insight-guidance](#mem-rte-insight-guidance) and [MEM-RTE-trace-retention](#mem-rte-trace-retention) remain selective inventories, not successful recovery or exercised checkpoint reuse evidence.
- Refinement, not correction of root retrieval: do not generalize root's lifecycle/query/budget/evidence-body behavior to all benchmark consumers. BIRD accepts empty browse and drops lifecycle; DDR emits evidence IDs but not bodies; InsightBench has four-item browse, transient dedup, uncapped Python mention loop and empty-resolve binding fallback. Relevant records: [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval), [MEM-RTE-bird-guidance](#mem-rte-bird-guidance), [MEM-RTE-ddr-guidance](#mem-rte-ddr-guidance), [MEM-RTE-insight-guidance](#mem-rte-insight-guidance). Paths/quotes are retained in these records.
- BIRD trace lineage correction to any inference that benchmark trajectories necessarily identify the evaluated version: run_evaluation selects config.semantic.version while record_trajectory rereads active_version. Explicit candidate evaluation can thus be recorded under parent selection; loader manifest.md can also relabel the loaded version without changing files. This prevents trustworthy version-conditioned diagnosis from those fields alone. [MEM-RTE-trace-retention](#mem-rte-trace-retention), [MEM-RTE-bird-guidance](#mem-rte-bird-guidance), [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation); SRC-1, `benchmarks/bird/run_evaluation.py`, `benchmarks/bird/trajectory_recorder.py`, `benchmarks/bird/tceo/loader.py`.
- Supplied runtime's general mention of optional benchmark trajectories must not imply complete observable task evidence. InsightBench recorder writes no native calls and semantic IDs/status only; root workflow truncates semantic results too. Completeness, relative order and replayability depend on recorder. [MEM-OBJ-trajectory](#mem-obj-trajectory), [MEM-RTE-trace-retention](#mem-rte-trace-retention), [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop).
- Local DDR source text promises SQL-ready sample_query but the inspected resolve projection does not supply it. InsightBench tool text mentions bindings in manifest, while its manifest discards inventory/task_bindings. Treat these as misleading source labels, not established payload behavior. [MEM-RTE-ddr-guidance](#mem-rte-ddr-guidance), [MEM-RTE-insight-guidance](#mem-rte-insight-guidance); SRC-1 paths/quotes in records.
- Checkpoint acceptance chooses the most recent trajectory, not necessarily the last member of the frozen evaluation batch; missing checkpoint trajectory causes all stored records to be returned by list_since. Exact freeze/chronological split enforcement and source-path validation remain host obligations, not proven by checkpoint persistence. [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [MEM-OBJ-source-references](#mem-obj-source-references), [MEM-RTE-reminder-delivery](#mem-rte-reminder-delivery), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission); SRC-1, `evoontology/trajectory/trajectory.py`, `evoontology/trigger/trigger.py`, `evoontology/evolution/session.py`.
- Root structural validation permits mapping-target constraints but resolve selects term-target constraints only. Stored valid content need not reach the model. Binder behavior and shortcut withdrawal enforcement remain uninspected for local variants; no generalized all-constraints/all-evidence delivery conclusion. [MEM-OBJ-constraint](#mem-obj-constraint), [MEM-RTE-insight-guidance](#mem-rte-insight-guidance); SRC-1, `evoontology/validate.py`, `evoontology/runtime/runtime.py`.
- No possible duplicate declarations after comparison: semantic objects, trajectories, workload/checkpoint and reports have no supplied object counterpart; hypothesis/evaluation/source-reference declarations are explicit parts of [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session). New memory routes describe narrower transformations or different local consumer implementations, not replacements for supplied runtime loops. Reconciliation should retain containment and consumer scope rather than equate them by shared tool names.
- Unresolved operation questions: actual host compliance, human per-content control of generic caller writes, evaluation authenticity, source-reference validity, correct binder grounding, provider context retention and causal benefit are unobserved. They limit conclusions without blocking the implemented account. Relevant records are the new routes above and [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission); external evidence gaps are those declared by boundary.

## Limitations and checks

Source identity was rechecked directly: checkout HEAD equals c94389b764394379086ff25e50d0e0f4396167b4 and git status --short was empty. Required invocation, member types, collection, worker rules and records contract were read completely, including supplied bounded runtime/contract ranges and trailing-read recovery. Citations use SRC-1 commit-relative paths or supplied runtime records, never another run or mutable characterization. This member follows its supplied memory-report contract rather than a general authoring skill.

Correction inspection directly rechecked DDR's manifest condition, startup/session callers and semantic resource caller, and searched DDR Python manifest invocations at the frozen revision. Implementation supports optional filtering but not wired task-targeted manifest delivery. The benchmark/local-binding/provider and external-host inspection limits, including the supplied InsightBench recovery/history limit, are retained in coverage and integration issues. No passing target-test, exercised learning, successful improvement, authenticated evaluation or causally demonstrated semantic influence is claimed. Automatic storage, projection and selection support wiring conclusions only.

Deterministic validation: the invocation-specific validate-output check passed after writing this member. This establishes form, citation resolution and quote occurrence checks, not analytical acceptance or observed target behavior.
