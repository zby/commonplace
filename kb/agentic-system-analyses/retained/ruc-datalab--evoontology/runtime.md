---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "EvoOntology runtime baseline: plugin-driven construction, semantic task execution, evaluation and version admission at c94389b764394379086ff25e50d0e0f4396167b4."
run-id: AAS-2026-10-13-evoontology-f2d0c7992c6e-01
reviewed-boundary: c94389b764394379086ff25e50d0e0f4396167b4
---

# EvoOntology runtime report

## Runtime account

### Responsibility and evidence

EvoOntology supplies a deterministic knowledge service and lifecycle machinery. An external host model performs construction, diagnosis, causal attribution and patch design by interpreting shipped skills. It is not the enclosing host's scheduler, permission manager or model trainer. Shipped benchmark agents are separate included callers with their own model/tool loops. This account uses SRC-1 implementation and doctrine/design only; no target execution was performed or supplied. Activation, host compliance, evaluation authenticity and benefit remain unobserved (SRC-1, `evoontology/runtime/mcp_server.py`, `plugins/evoontology-codex/AGENTS.md`, `benchmarks/bird/agent/data_agent.py`).

Added inspection beyond the boundary's initial coverage includes root semantic retrieval, validation and evaluation aggregation; complete lifecycle/session code; both POSIX launchers and Claude reminder implementation; the Codex Build/Evolve texts and evolution data-boundary reference; all three complete adapter implementations; BIRD's ordinary agent loop, message transformation, provider request and per-question scoring/recording; DDR's message transformation and tool executor; and InsightBench's table setup, ToolCallingChat dispatch and PythonREPL execution. These are implementation or doctrine/design, not run evidence. Local benchmark retrieval internals, all provider-specific DDR wrappers, downstream InsightBench metric implementations and all dataset-preparation helpers were not exhaustively inspected. They remain available, not inaccessible. This prevents treating root retrieval details or one executor's isolation as universal across benchmark variants (SRC-1, `evoontology/runtime/runtime.py`, `evoontology/validate.py`, `evoontology/evaluation/evaluation.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/insightbench/insightbench/tceo/tool_chat.py`).

### Shipped entry paths and ordinary invocation

Codex's MCP configuration chooses a local launcher. It selects a configured interpreter, the Codex cached interpreter or PATH Python, then executes the bundled server. Claude's launcher selects either MCP or reminder mode; its SessionStart hook runs reminder mode synchronously. The server speaks newline-delimited JSON-RPC over stdio, exposes tools plus a manifest resource, ignores notifications without an ID and reports malformed requests or dispatch errors. Semantic calls reload a requested workspace/version; lifecycle calls instantiate deterministic helpers with caller arguments. The source implements serialization in one server process, not a distributed coordination or authentication protocol (SRC-1, `plugins/evoontology-codex/.mcp.json`, `plugins/evoontology-codex/scripts/launch_evo_semantic_mcp`, `plugins/claude-code/scripts/launch-evoontology`, `plugins/claude-code/hooks/hooks.json`, `evoontology/runtime/mcp_server.py`).

An ordinary cold-start request proceeds through [RT-RTE-build-publication](#rt-rte-build-publication): the host interprets the Build skill, resolves data/workload authorization, prepares construction questions, probes actual data through native tools, proposes five semantic record families, saves a version, annotates limitations and publishes it. Python validates structure and references, selects the active version, initializes reminder state and attempts presentation. The host, not Python, owns the next analytical probe and semantic meaning judgment. Presentation failure is returned separately and does not undo publication (SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`, `evoontology/runtime/ops.py`).

Later, a requested data task follows [RT-RTE-task-execution](#rt-rte-task-execution). `start_task` obtains the persisted question and concrete ontology version and creates a UUID task file. `resolve_task` loads that pinned version and records the retrieval event. The host chooses the actual query; built-in SQLite replay executes and records it, or the host uses another native tool and explicitly supplies its observation. `finish_task` appends a trajectory and stores the terminal answer/status. Interrupted running tasks remain discoverable via workflow status; event IDs make matching event re-submission idempotent, while conflicting duplicates are refused. Ordinary semantic calls alone do not complete trajectories. Direct MCP semantic calls instead follow [RT-RTE-semantic-retrieval](#rt-rte-semantic-retrieval) and are not automatically pinned to a task or recorded in its trajectory (SRC-1, `evoontology/workflow.py`, `evoontology/runtime/mcp_server.py`, `plugins/evoontology-codex/AGENTS.md`).

The evolution loop [RT-RTE-evolution-admission](#rt-rte-evolution-admission) begins only when a caller starts or resumes it. A reminder computes whether time or trajectory thresholds are reached; Claude injects a reminder into host context, while Codex instructions request an `evolution_status` call. Neither inspected reminder implementation starts the Evolver. The host freezes objectives, batch, evaluation protocol and budget, diagnoses task evidence, records a falsifiable hypothesis and creates a separate candidate. Rejection leaves the run running; acceptance validates and recomputes an aggregation gate from supplied evaluation summaries before publication. Missing data, permissions, interruption, unreliable evaluation or budget exhaustion can lead to incomplete state under reason-specific checks. `finalize` refuses a still-running run, then presentation reports accepted or unchanged-parent state (SRC-1, `evoontology/trigger/trigger.py`, `plugins/claude-code/scripts/check-reminder.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/evolution/session.py`).

### Control envelope and forcing cases

The capability surface includes semantic reads, project/task writes, version save/selection, lifecycle state manipulation, SQLite replay and presentation. `tools/list` returns semantic tools plus lifecycle operations together. A connected client can pass workspaces and explicit versions. This establishes reachable capabilities, not a current grant set: no deployment's host approvals, credentials or OS sandbox were supplied. The service's file and database access inherits its process rights. Host-native tools and benchmark Python execution have different boundaries (SRC-1, `evoontology/runtime/mcp_server.py`, `evoontology/runtime/ops.py`, `evoontology/workflow.py`, `benchmarks/insightbench/insightbench/utils/agent_utils.py`).

Four source forcing cases bound the load-bearing guarantees:

| Claimed protection | Owner/enforcement and strength | Covered path and forcing alternative | External contract and conclusion |
| --- | --- | --- | --- |
| Candidate success requires improvement | EvolutionSession `accept` plus `_publication_gate`; invariant for calls through that method over supplied inputs | Requires candidate validation, current-round candidate gate input, explicit no-regression assertion, known protocol and passing recomputed gate. But `set_active_version` directly selects an existing directory; direct store publication/promotion and filesystem edits do not invoke the gate. | Caller must supply authentic independent paired scores or judge verdicts. Implementation conclusion status: wired. Operation conclusion status: uninspected. Not a system-wide trustworthy-improvement guarantee. See [RT-RTE-version-override](#rt-rte-version-override). |
| A completed data task has native evidence | ProjectWorkflow `finish_task`; invariant over its recorded events | Refuses completion without a non-error native-tool event. `record_event` accepts caller-supplied tool names/results; it does not witness external execution. Built-in `execute_query` does execute before recording. | Host observation integrity is required for manually supplied events. Implementation conclusion status: wired. Operation conclusion status: uninspected. Completion means evidence-shaped records, not authenticated successful analysis. |
| Data access is read-only | ProjectWorkflow SQLite connection/authorizer/progress handler; invariant within that executor | URI read-only mode, restricted SQLite actions, blocked extension loading, bounded progress and 100-row return cover built-in replay. Host-native tools and InsightBench PythonREPL are alternate executors, not covered. | Host/OS must isolate other executors if needed. Implementation conclusion status: wired. Deployment conclusion status: uninspected. No universal read-only or sandbox conclusion. |
| Design never consumes validation/reference answers | Skill/data-boundary instructions; policy, with partial deterministic filtering | Workload preparation enforces registered construction IDs in fixed-split mode and skips validation/test trajectory history. The MCP client can still choose other files/tools; evaluation summaries include cases and artifact references, and Python does not create an inaccessible model context for the Evolver. | Host must obey role/data partition rules and evaluator access restrictions. Policy conclusion status: claimed. Implementation conclusion status: wired for the scoped workload filter. Operation conclusion status: uninspected. |

Evidence: SRC-1, `evoontology/evolution/session.py`, `evoontology/ontology/store.py`, `evoontology/runtime/ops.py`, `evoontology/workflow.py`, `plugins/evoontology-codex/skills/evolve-ontology/references/ontology-layer-data-boundary.md`, `benchmarks/insightbench/insightbench/utils/agent_utils.py`.

Publication is not a single transaction across all durable effects. `accept` publishes/selects the version, advances the checkpoint, then saves accepted run status. `publish` avoids replacing different official content and permits identical-content retry, but the active selector is written separately, and `save_version` can overwrite an existing named version file by file. Thus the session's documentation about atomic acceptance should not be generalized to crash-safe multi-file commits or concurrent-client isolation. Incomplete/reject preserve the active selector within the lifecycle method; they cannot prevent an independent selector operation (SRC-1, `evoontology/evolution/session.py`, `evoontology/ontology/store.py`).

### Included benchmark alternatives and context

[RT-RTE-benchmark-evaluation](#rt-rte-benchmark-evaluation) covers three shipped subprocess adapters, not a separate autonomous core evaluator. BIRD constructs the selected manifest and MCP configuration, runs a fresh per-question agent, executes model-selected tools, extracts terminal SQL and compares its rows with gold SQL. Gold enters the scorer, not the inspected agent constructor. DDR generates logs with the selected version and then invokes its evaluator, unless `skip_generation` asks it to judge existing logs. InsightBench runs ontology-enabled flag tasks, table-bound semantic setup and model/tool stages. These adapters normalize scores and artifact paths but do not themselves return the `gate_input` consumed by session acceptance. A caller must construct and record that formal gate input; an adapter score file alone does not install a candidate (SRC-1, `benchmarks/bird/evolution_adapter.py`, `benchmarks/bird/run_evaluation.py`, `benchmarks/ddr_10k/evolution_adapter.py`, `benchmarks/insightbench/evolution_adapter.py`, `evoontology/evolution/session.py`).

BIRD uses at most the configured ordinary turns, with bounded no-response/no-action retries, per-turn timeouts and a final no-tools SQL request on turn exhaustion. It executes only the first returned tool call in an ordinary response. Timeout retries can repeat provider requests; the code does not establish exactly-once external effects. DDR's inspected executor dispatches through its MCP manager, appends result messages and additionally requests an insight only after evidence tools. Its message builder includes the session history, translating structured tools by provider rather than removing old turns. BIRD likewise translates its full session history; console preview truncation does not truncate model context (SRC-1, `benchmarks/bird/agent/data_agent.py`, `benchmarks/ddr_10k/agent/data_agent.py`).

InsightBench's ToolCallingChat creates a fresh message list per call and keeps that stage's subsequent results until terminal return or safety-round exhaustion. This is a per-call context frame: earlier stage transcripts do not enter unless callers supply their content; the returned text can cross outward. The layer remains reachable for on-demand semantic reload/delivery, not as a reference automatically followed by the model. Its Python call counter blocks call five and later, so at most four calls execute for that object; this count is not an OS isolation boundary. `PythonREPL.run` executes submitted code in-process and changes/restores the working directory under a lock. Neither a stage frame nor its tool budget makes arbitrary Python read-only (SRC-1, `benchmarks/insightbench/insightbench/tceo/tool_chat.py`, `benchmarks/insightbench/insightbench/utils/agent_utils.py`).

The host's skill context loading, compaction, delegation and approval behavior remain external/uninspected. Retrieval bounds delivered catalog items or requested concepts; they do not prove a bound on total serialized payload or cumulative context. The distributed model dependencies are separately recorded below. No inspected lifecycle path trains their weights (SRC-1, `evoontology/runtime/runtime.py`, `plugins/evoontology-codex/AGENTS.md`, `benchmarks/bird/agent/llm_providers.py`).

## Shared records

### Components

#### RT-CMP-host-model
Label: Host Builder/Evolver model

Source-native identity: the Builder Agent/Evolver addressed by shipped Codex skills and host instructions. Representational form: distributed-parametric model, with natural-language skills as inputs; storage substrate: external host/provider weights, inaccessible here. Its next-step decisions include probes, object proposals, causal explanations, patches and evaluation orchestration. Parameter changes during operation: uninspected host internals; deterministic core does not implement model training. Exact version pinned: no model identity is specified by these skills. Mutable endpoint substitution: uninspected host configuration, so exact model continuity is not established. Evidence: SRC-1, `plugins/evoontology-codex/AGENTS.md`, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.

> The Builder Agent discovers and populates semantic content under this
> schema.
> --- `plugins/evoontology-codex/skills/build-ontology/SKILL.md`

#### RT-CMP-bird-provider
Label: BIRD provider model

Source-native identity: OpenAIProvider and its OpenAI-compatible variants. Representational form: distributed-parametric external model; storage substrate: provider service, not local ontology JSON. Parameter changes during operation: none requested by the inspected inference wrapper; service internals uninspected. Exact version pinned: not guaranteed; constructor accepts model strings and base URLs, defaulting to `gpt-4o`. Mutable endpoint can resolve another model: yes, configurable base URL/model string supplies no immutable weight identity. Evidence: SRC-1, `benchmarks/bird/agent/llm_providers.py`.

> response = await self.client.chat.completions.create(
>     model=self.model,
>     messages=messages,
>     tools=openai_tools or None,
>     temperature=self.temperature,
>     timeout=120,
> )
> --- `benchmarks/bird/agent/llm_providers.py`

#### RT-CMP-ddr-provider
Label: DDR provider model

Source-native identity: `create_llm_provider` routing to OpenAI, Gemini, VLLM or MiniMax providers. Representational form: distributed-parametric models; storage substrate: selected external API or configured serving endpoint. Parameter changes during operation: inference use is wired in the inspected agent, but provider-specific implementation and service-side training remain uninspected. Exact version pinned: not guaranteed; caller/configuration supplies aliases and endpoint settings. Mutable endpoint can resolve another model: configurable VLLM base URL/model and external aliases permit substitution; deployed identity remains unobserved. Evidence: SRC-1, `benchmarks/ddr_10k/agent/llm_providers.py`, `benchmarks/ddr_10k/agent/data_agent.py`.

> return VLLMProvider(
>     base_url=base_url,
>     model=kwargs.get("model") or "",
>     api_key=api_key,
>     port=port
> )
> --- `benchmarks/ddr_10k/agent/llm_providers.py`

#### RT-CMP-tool-calling-chat
Label: InsightBench ToolCallingChat model

Source-native identity: ToolCallingChat's `model_name` and OpenAI-compatible client. Representational form: distributed-parametric model; storage substrate: external inference service. Parameter changes during operation: no update is requested by this inspected loop; provider internals uninspected. Exact version pinned: no immutable weight version; model name and injected client are configurable. Mutable endpoint can resolve another model: yes, the client may be replaced and model names do not fix service weights. Evidence: SRC-1, `benchmarks/insightbench/insightbench/tceo/tool_chat.py`.

> kwargs: Dict[str, Any] = {
>     "model": self.model_name,
>     "temperature": self.temperature,
>     "messages": messages,
> }
> --- `benchmarks/insightbench/insightbench/tceo/tool_chat.py`

#### RT-CMP-llm-judge
Label: Designated LLM Judge

Source-native identity: the designated LLM Judge in rolling-trajectory comparison. Representational form: distributed-parametric model interpreting answers; storage substrate: externally selected provider, not implemented by EvaluationGate. Parameters changing during operation, immutable version pin and endpoint mutability: uninspected because the core implements aggregation/anonymization, not the judge call. The instruction to hold models fixed is a policy, not a model artifact pin. Evidence: SRC-1, `evoontology/evaluation/evaluation.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.

> This module owns the aggregation gate and the A/B anonymization helpers; it does
> not implement ``score_fn`` or call the judge model — those belong to the
> benchmark adapter and the Evolver respectively.
> --- `evoontology/evaluation/evaluation.py`

### Operative objects

#### RT-OBJ-evolution-session
Label: EvolutionSession run state

Source-native identity: EvolutionSession's `run.json`, `rounds.jsonl`, trajectory-source references and evaluation summaries under `evolution/run_N/`. Representational form: symbolic lifecycle fields, numeric gate observations and path references consumed by deterministic Python; hypotheses/notes remain natural-language payload for later host interpretation, not executable rules. Storage substrate: workspace JSON/JSONL files. Separate hypothesis text is assessed on the route below; this record identifies the lifecycle container, not semantic record families. Evidence: SRC-1, `evoontology/evolution/session.py`.

> "current_hypothesis": "",
> "current_candidate": "",
> "accepted_version": "",
> "end_reason": "",
> --- `evoontology/evolution/session.py`

### Routes

#### RT-RTE-build-publication
Label: Initial build publication

Endpoints/progression/owner: user request → host Build skill interpretation → configure/prepare/probe → save_version/annotate → publish_ontology_build → active ontology and explorer. The host proposes content, resolves authorization and can withhold publication; deterministic Python vetoes validation failures and an existing active index. A request authorizes starting the workflow, not necessarily human approval of each semantic object. Mode: fixed-split construction or rolling cold start. Answer oracle: none used by the construction path; the skill prohibits Builder access to ground truth. Trigger/proposed change: workload needs become initial semantic records. Admission: host-generated records pass structural validation; semantic correctness/reproducible grounding are host obligations. Recovery: revise unsupported objects before publication; render retry does not rebuild an already published version. Evidence: SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`, `evoontology/runtime/ops.py`, `evoontology/validate.py`.

- Immediate return: publication status, active version and presentation result; preceding tools return persisted paths/annotations.
- Later read-back: active version is loaded by semantic calls and later tasks; annotations reach the explorer.
- Delegated visibility: MCP replies deliver selected operation results to the requesting host; no internal sub-agent launch is implemented here.
- Selection predicate: caller workspace/version and permitted construction workload; fixed-split IDs are checked by prepare.
- Invalidation or expiry: no automatic semantic expiry here; caller can replace/select versions through other operations.
- Activation or effect: wired selector change makes content available to later consumers; actual model use and task benefit unobserved.
- Evidence limits: schema/reference validation does not reproduce evidence or prove analytical correctness; no build run supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (workspace / "active.json").exists():
>     raise ValueError("An active ontology already exists; evolve it instead")
> --- `evoontology/runtime/ops.py`

#### RT-RTE-semantic-retrieval
Label: Manifest and semantic retrieval

Endpoints/progression/owner: MCP resource/tool request → reload SemanticLayer → deterministic browse/resolve → serialized text result to host. Policy/form: symbolic token/name/alias/ID matching and lifecycle filtering; returned definitions and applicability prose need model interpretation. Context: mention list and optional analysis context; state: selected version. Core returns navigation guidance, not native data-query results. Evidence: SRC-1, `evoontology/runtime/mcp_server.py`, `evoontology/runtime/runtime.py`.

- Immediate return: manifest text, ranked browse views, or resolved term/mapping/relation/constraint/evidence views with ambiguity and coverage status.
- Later read-back: persisted version records reach each subsequent reload; retrieval itself writes no retained revision.
- Delegated visibility: the requesting host sees JSON serialized as MCP text; resource reads use server workspace/version, unlike per-tool workspace overrides.
- Selection predicate: active or explicit version; active/validated items; browse requires query and returns at most six items; resolve processes first five nonempty mentions, with name/alias/token matching and context tie-breaking.
- Invalidation or expiry: semantic calls reload selection; explicit version remains requested until caller changes it; missing files produce an uninitialized layer, not proof of an empty valid ontology.
- Activation or effect: wired delivery of selected guidance; compliance and native-query influence unobserved.
- Evidence limits: counts bound items/mentions, not total bytes, all attached evidence or accumulated context; local benchmark variants may transform content differently.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> accepted = raw_mentions[:_MAX_RESOLVE]
> skipped = raw_mentions[_MAX_RESOLVE:]
> --- `evoontology/runtime/runtime.py`

#### RT-RTE-task-execution
Label: Recorded project task execution

Endpoints/progression/owner: prepared question → start_task pins version → resolve_task/native execution → record_event → finish_task/TrajectoryStore. Host owns analytical steps; Python owns built-in SQLite execution, identifier checks, recording and status transitions. State includes question, source, pinned version, events and final answer. Native manual observations are supplied by the host; the built-in executor directly gathers results. Evidence: SRC-1, `evoontology/workflow.py`, `plugins/evoontology-codex/AGENTS.md`.

- Immediate return: task state, semantic results, bounded query results/errors and terminal answer/status.
- Later read-back: running task files support resumption; completed trajectories can become eligible same-source history and later evolution inputs.
- Delegated visibility: tool replies reach host; host-native execution occurs outside the core executor's permissions.
- Selection predicate: workload question ID and matching data source; active selection is resolved to a concrete version at start; resolve_task uses that version.
- Invalidation or expiry: finished tasks reject new events; duplicate matching event IDs are reused, conflicting duplicates fail; no automatic task expiry.
- Activation or effect: SQLite query executes read-only with action/progress limits and returns at most 100 rows; completed record requires a non-error native event; actual external-event authenticity unobserved.
- Evidence limits: event tool names/results are caller-supplied except built-in replay; completion does not prove answer correctness or automatic logging of all host calls.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if status == "completed" and not any(not e.get("error") for e in task["native_tool_calls"]):
>     raise ValueError("A completed data task needs at least one observed native tool result")
> --- `evoontology/workflow.py`

> connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
> --- `evoontology/workflow.py`

#### RT-RTE-evolution-admission
Label: Evidence-directed evolution and gated admission

Endpoints/progression/owner: user request/resume → frozen context → host Diagnose/Attribute/Patch → candidate version and hypothesis → external evaluation → recorded gate → accept or reject/incomplete → finalize. Host computation proposes, interprets evidence and records the decision inputs; session code can veto acceptance, invalid round transitions, budget exhaustion and unsupported stop reasons. Human contribution is problem/scope/budget authorization and interruption, not mandatory approval of each patch. Mode: bounded quick/full rounds, fixed-split validation or rolling reserve; objective and unacceptable regressions are requested before experiments. Answer oracle: fixed-split designated evaluator may use ground truth; rolling LLM comparison judges alternatives without an expected-answer oracle. Core gate consumes the supplied observations, not the oracle directly.

Change scope: the skill permits Content, Tool and Schema interventions, including related prompts/workflows/runtime. The implemented session publishes five version record files; it does not itself install arbitrary tool/schema/runtime code patches or restore such files. Those capability/product changes and their reversibility remain host-managed instructions. `record_round` stores generic notes/refs, not dedicated changed-component or dimension fields, so the skill's demanded detailed report needs host-authored payload/reporting beyond core state. Rejection leaves parent selection/checkpoint unchanged within this route; accepted semantic content is copied and selected. Recovery uses durable state/resume, separate candidates and preserved parent; final presentation failure does not reverse acceptance. Evidence: SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/evolution/session.py`, `evoontology/ontology/store.py`, `evoontology/runtime/ops.py`.

- Immediate return: run/round state, evaluation summary path, rejection summary, accepted version or explicit error; finalizer returns terminal state/presentation.
- Later read-back: hypotheses, rejected rounds, evaluation references and accepted versions persist for resumed/new host work and later semantic/task consumers.
- Delegated visibility: adapters use subprocesses; evaluator/judge separation is instructed, not an internally enforced inaccessible model frame.
- Selection predicate: latest running session; current candidate/current-round evaluation gate input; budget and protocol checks precede publication.
- Invalidation or expiry: terminal runs cannot be resumed as running; exhausted budget stops begin_round; candidate records and prior summaries remain durable unless externally changed.
- Activation or effect: accepted semantic files become active and checkpoint advances; no supplied run establishes exercise, improved capacity or correct independent scoring.
- Evidence limits: supplied assertions/scores are not authenticated; alternate selector/store/filesystem paths bypass this gate; external code-patch installation is not implemented by accept.
- implementation conclusion status: wired
- policy conclusion status: claimed
- operation conclusion status: uninspected

> gate = self._publication_gate(run)
> if not gate["accept"]:
>     raise EvolutionError("Candidate did not pass the recorded evaluation gate")
> --- `evoontology/evolution/session.py`

> supplied = next((s.get("gate_input") for s in summaries if s.get("gate_input")), None)
> if not isinstance(supplied, dict):
>     raise EvolutionError("Record candidate evaluation gate_input before publication")
> --- `evoontology/evolution/session.py`

> When the attributed mechanism involves related prompt, workflow, or runtime
> components, they may be modified as part of the corresponding evolution
> dimension.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

Theory account: source-native causal hypotheses are localized natural-language statements, requested to explain a limitation, causal mechanism and predicted/falsifying effects. Guidance comes from the shipped four-step method; host criticism is requested to revise attribution and retain rejected explanations for subsequent rounds. The core persists hypothesis and notes but does not interpret their claims. Addressability: one whole hypothesis is stored, while component-level scope/change reports are instructed; no enforced decomposition into individually testable premises. Persistence: run files survive rounds/sessions; subsequent reconstruction/consumption is instructed, not observed.

theory-builder conditions 1–4:

- condition 1 conclusion status: wired

A nonempty current hypothesis and rejection history can persist a whole statement; its explanatory content remains host-dependent.

- condition 2 conclusion status: claimed

Skill requires intervention choice to depend on attributed mechanisms; Python only checks nonempty text, and no decision trace demonstrates dependence.

- condition 3 conclusion status: claimed

Skill asks for competing explanations, counterexamples and revised attribution on ineffective interventions; actual content-directed blame/revision is unobserved.

- condition 4 conclusion status: claimed

Skill requires rejection-loop knowledge to shape new candidates; durable rounds afford this without proving actual reuse.

- learning conclusion status: uninspected

Future improved capacity is an objective, not established by revision or gate wiring; no outcome/attribution evidence supplied.

- reflection conclusion status: claimed

The method requests representations of its tools, schema and runtime limitations and interventions back into those aspects; both causal directions in actual operation remain unobserved.

- reflective theory builder conclusion status: uninspected

Method-text criticism against its own operation is not established by a hypothesis string or a general permission to edit prompts.

- autonomous theory builder conclusion status: claimed

The skill requests autonomous internal search within authorized scope, but role-by-role exercised computation/compliance is unobserved.

- self-improvement conclusion status: afforded

Boundary is the ontology layer plus shipped behavior-shaping skills/tools, horizon later tasks/sessions, objective reproducibly better analysis without unacceptable regression. Evidence-to-update and update-to-organization are designed through diagnosis/admission; active semantic guidance supplies a live authority channel. Subsequent exercised behavior causally dependent on that change is unestablished, so this is a dormant improvement-directed self-change pathway, not exercised or successful self-improvement.

> If the intervention is ineffective, redesign the Candidate. If the
> intervention activates but the problem remains, update the attribution.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

#### RT-RTE-version-override
Label: Direct version save and selection

Endpoints/progression/owner: client → save_version/set_active_version or direct SemanticStore API → files/active selector → subsequent load. Caller proposes and decides; Python checks list serialization/path components or directory existence, not per-content human approval or an evolution gate. Operating mode: direct administrative API; answer oracle: inapplicable because no comparison occurs. Trigger: client command; proposed change: new/replaced record files or selected version. Rejection: malformed family list/path or missing target directory; rollback: select preserved parent, provided its files remain intact. Existing version content can be overwritten by save_version; publish avoids different-content official overwrite, while promote removes/replaces a destination. Evidence: SRC-1, `evoontology/runtime/ops.py`, `evoontology/ontology/store.py`.

- Immediate return: saved version/path or selected active version; errors on scoped checks.
- Later read-back: semantic reloads and future tasks consume changed version/selector; an already pinned task still names the same version, not an immutable content digest.
- Delegated visibility: MCP exposes these operations to connected caller; direct package/file access is an alternate process-rights path.
- Selection predicate: explicit workspace and version; set_active requires directory existence, not full validation or recorded improvement.
- Invalidation or expiry: selector can be switched again; saved named version content is mutable; no enforced expiry.
- Activation or effect: wired durable selection/content change, bypassing session acceptance; actual deployed grants uninspected.
- Evidence limits: administrative capability is not evidence of malicious use; no host ACL or isolation policy is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> SemanticStore.set_active(str(_workspace(arguments)), version)
> return {"status": "ok", "active_version": version}
> --- `evoontology/runtime/ops.py`

#### RT-RTE-benchmark-evaluation
Label: Shipped benchmark subprocess evaluations

Endpoints/progression/owner: caller chooses adapter/version/cases → subprocess driver → benchmark model/tools → scored artifacts → normalized metrics/cases/paths. Adapter code owns subprocess invocation/error handling, benchmark code owns model execution/scoring, caller owns formal pairing and gate submission. Mode: bounded benchmark batches, with DDR existing-log alternative. Answer oracles: BIRD uses gold SQL execution result equivalence; DDR dispatches an LLM evaluator; InsightBench adapter consumes flag scores, but metric internals are not established in this inspection. These observations are evaluation input, not independently authenticated gate evidence. Evidence: SRC-1, all three adapter paths below, `benchmarks/bird/run_evaluation.py`, `evoontology/evolution/adapter.py`.

- Immediate return: normalized metric dict, cases and artifact references; nonzero subprocess status raises an error.
- Later read-back: results/log files and optional trajectories can reach evolution diagnosis or recorded evaluation summaries; adapters do not publish versions.
- Delegated visibility: drivers receive selected version and case flags; adapters return reduced observations, not complete model transcripts or proof of fixed execution conditions.
- Selection predicate: BIRD database/case selectors and newest all_results.json by mtime; DDR scenario/target IDs and optional skip_generation logs; InsightBench flag IDs and expected results.json.
- Invalidation or expiry: result files remain until externally replaced; newest-file selection and reused logs do not prove fresh subject-specific runs.
- Activation or effect: subprocess evaluation is wired; all three inspected adapters omit gate_input, so formal admission needs caller pairing/regression assertion and record_evaluation.
- Evidence limits: no benchmark execution/results supplied; invocation configuration, artifact freshness and downstream metrics need independent verification for benefit claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> completed = subprocess.run(cmd, cwd=str(BIRD_DIR), capture_output=True, text=True)
> --- `benchmarks/bird/evolution_adapter.py`

> if not self.skip_generation:
>     gen_cmd = [
> --- `benchmarks/ddr_10k/evolution_adapter.py`

> "--ontology-layer",
> "--semantic-store", self.store_path,
> "--semantic-version", str(subject),
> --- `benchmarks/insightbench/evolution_adapter.py`

#### RT-RTE-benchmark-tool-loop
Label: Model-selected benchmark execution

Endpoints/progression/owner: fresh task/stage context → provider response → tool dispatch/results → next model turn → SQL/answer/artifacts or error. BIRD chooses first tool call, translates full session messages and forces final SQL on ordinary turn exhaustion; DDR translates history and dispatches MCP tools; InsightBench executes local semantic tools/Python and feeds native or text-protocol results back into its per-call frame. Model chooses tool/action arguments; code chooses dispatch and budgets. References to the three agent models above identify separate parameter dependencies. Evidence: SRC-1, `benchmarks/bird/agent/data_agent.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/insightbench/insightbench/tceo/tool_chat.py`, `benchmarks/insightbench/insightbench/utils/agent_utils.py`.

- Immediate return: BIRD terminal session/predicted SQL; DDR tool response to its agent loop; InsightBench terminal stage text or safety-limit exception, with possible file artifacts.
- Later read-back: benchmark driver/optional recorders retain logs, outputs or trajectories; ordinary turn accumulation is current-run state, not itself a revised ontology.
- Delegated visibility: available tool schemas and selected manifest/data context reach provider; resulting observations return to the task/stage loop.
- Selection predicate: configured MCP tools in BIRD/DDR; InsightBench local layer/execution tool list and stage configuration; model chooses actions within these exposed schemas.
- Invalidation or expiry: BIRD task session and InsightBench per-call message frame reset on new invocation; external artifacts may outlive them; tool count/round limits stop further execution without deleting durable files.
- Activation or effect: tool dispatch is wired, including unrestricted-by-this-function Python exec; terminal outputs and causal semantic influence unobserved.
- Evidence limits: budgets/timeouts are not filesystem/network sandboxes; opaque host/service execution and all alternate MCP server permissions are not established by one executor.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = await self.mcp_client.execute_tool(tool_name, arguments)
> result_text = json.dumps(result, ensure_ascii=False, default=str)
> --- `benchmarks/bird/agent/data_agent.py`

> messages: List[Dict[str, Any]] = [{"role": "user", "content": content}]
> --- `benchmarks/insightbench/insightbench/tceo/tool_chat.py`

> exec(command, locals())
> valid = True
> retry_message = ""
> --- `benchmarks/insightbench/insightbench/utils/agent_utils.py`

### Claims

#### RT-CLM-evolution-success
Label: Reproducible evolution success

Claimed operation: evolution should continue until a credibly, reproducibly better version exists without unacceptable regression, or legitimate external conditions stop trustworthy continuation. Source: SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`. This is an improvement objective; [RT-RTE-evolution-admission](#rt-rte-evolution-admission) establishes partial deterministic enforcement over recorded observations, not reproduced success.

> Only declare success when the final version satisfies:
>
> - the accepted version outperforms the starting Parent under the configured
>   evaluation protocol;
> - the result is reproducible and evidence-supported;
> - no unacceptable regression exists;
> - the accepted version can be activated and rerun.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Skill guidance to host decisions

Consumer: host Builder/Evolver model. Channel: natural-language skill and reference text loaded by the host. Force: policy/instruction, not Python-enforced content interpretation. Horizon: build/evolution episode, with persisted run state available across resumptions. SRC-1, `plugins/evoontology-codex/AGENTS.md`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`. [RT-RTE-evolution-admission](#rt-rte-evolution-admission) distinguishes these instructions from mechanical gates.

> following
> Diagnose → Attribute → Patch → Evaluate/Gate.
> --- `plugins/evoontology-codex/AGENTS.md`

#### RT-BAP-semantic-guidance
Label: Semantic delivery to later analysis

Consumer: external host or shipped benchmark agent model. Channel: manifest plus requested semantic tool replies containing selected definitions, mappings, constraints and evidence. Force: interpretive guidance; native query validation remains requested, not compelled by retrieval. Horizon: later tasks/sessions loading selected retained versions. Source: SRC-1, `evoontology/runtime/runtime.py`, `benchmarks/bird/run_evaluation.py`. Actual behavior change is unobserved; [RT-RTE-semantic-retrieval](#rt-rte-semantic-retrieval) establishes delivery structure.

> "- Resolved mappings are guidance, not final answers — always validate "
> "against the actual data with your native query tools.",
> --- `evoontology/runtime/runtime.py`

#### RT-BAP-session-gate
Label: Session state and gate to publication

Consumer: deterministic EvolutionSession code. Channel: symbolic status/round/candidate and gate_input fields. Force: mechanical veto of this API's acceptance/finalization, not authority over direct selector/file operations. Horizon: persisted evolution run through terminal state and later active-version loads. Source: SRC-1, `evoontology/evolution/session.py`. [RT-RTE-version-override](#rt-rte-version-override) bounds its coverage.

> if supplied.get("unacceptable_regressions") is not False:
>     raise EvolutionError("Evaluation must explicitly rule out unacceptable regressions")
> --- `evoontology/evolution/session.py`

## Annotations

none
