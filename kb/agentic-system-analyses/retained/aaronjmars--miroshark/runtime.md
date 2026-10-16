---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MiroShark runtime baseline: graph-derived setup, synchronized simulation, interviews, report loops and optional external-tool dispatch."
run-id: AAS-2026-10-15-miroshark-b3df0e053a29-01
reviewed-boundary: e95d3d8c2a2206b8b6695648e8504cf23436d3de
---

# MiroShark runtime report

## Runtime account

### Evidence and claimed work

MiroShark encloses the agent loop: it produces personas/configuration, launches simulation processes, chooses active agents, executes model-selected platform actions, records results and supplies later report/interview consumers. The [boundary](boundary.md) fixes SRC-1 and the whole-system scope. This report inspects implementation, with comments and prompts treated as declared design. No target execution, provider call, test or benchmark was performed; activation, reliability, predictive validity and benefit remain unobserved.

The shipped start API describes graph-memory updating as optional and subsequent analysis as its purpose; its wording is stronger than this report's verified execution conclusions ([RT-CLM-graph-memory](#rt-clm-graph-memory)). A simulation of social or trading behavior is not an oracle for actual public behavior.

Additional SRC-1 implementation coverage beyond the boundary's initial inspection includes bounded reads/searches of `backend/app/services/agent_mcp_tools.py`, `backend/scripts/mcp_agent_bridge.py`, `backend/scripts/director_events.py`, `backend/app/utils/llm_client.py`, `backend/app/utils/claude_code_client.py`, `backend/app/storage/embedding_service.py`, `backend/app/storage/reranker_service.py`, `backend/app/storage/search_service.py`, `backend/wonderwall/social_platform/recsys.py` and `backend/wonderwall/simulations/polymarket/platform.py`. These are the same frozen source, not new evidence sources. Auxiliary publishing/export, every API endpoint, every locale, detailed belief revision and graph contradiction handling are not exhaustively assessed here. Retained-memory revision belongs to the memory account; this report preserves its runtime supply and consumer boundaries.

### Entry, ordinary invocation and termination

The local launcher/server/browser and HTTP CLI are entry paths into the application, not separate principals deciding each simulated action. The CLI constructs ordinary HTTP requests; its inspected `_api` helper adds Accept/Content-Type, not the server's internal-key header. Thus a configured HTTP deployment can reject this client's requests; shared endpoints do not establish working parity across clients (SRC-1, `backend/cli.py`, `backend/app/__init__.py`). The stdio MCP server instead directly dispatches storage operations ([RT-RTE-storage-mcp](#rt-rte-storage-mcp)).

An ordinary prepared, parallel invocation proceeds as follows:

1. The caller supplies documents and a simulation requirement. Graph-building code calls storage ingestion; preparation selects defined graph entities with edges, generates personas and simulation parameters, and writes platform profiles plus `simulation_config.json`. The model proposes content; application code admits it without a separate per-persona approval step in the inspected preparation path ([RT-RTE-prepare-population](#rt-rte-prepare-population)). Upload extraction and ontology are upstream context, not validated facts about the world merely because ingestion succeeded (SRC-1, `backend/app/api/graph.py`, `backend/app/services/graph_builder.py`, `backend/app/storage/neo4j_storage.py`).
2. `/api/simulation/start` resolves a simulation ID, selected platform, optional round cap and resume/force options. `SimulationRunner` requires a prepared config, guards against an already-running state, saves run state, selects a shipped script and launches Python in the simulation directory. It copies the server environment, forwards locale/model slot and observability identifiers, redirects output and starts a monitoring thread (SRC-1, `backend/app/api/simulation.py`, `backend/app/services/simulation_runner.py`). A successful process launch is not a completed simulation.
3. The parallel driver creates model-backed platform agent graphs and environments. Code owns the round clock and active-agent selection; model interpretation owns action choice within each agent invocation. Agent IDs, simulation ID, platform and graph ID have different roles: population membership, run namespace, environment identity and knowledge namespace respectively. The synchronized loop builds previous-round context, injects belief/memory/market/cross-platform/director material, runs platform steps concurrently, then fetches actions and updates downstream state ([RT-RTE-synchronized-rounds](#rt-rte-synchronized-rounds)).
4. Database actions become per-platform action logs, round memory, belief updates and cross-platform state. Background compaction turns older action descriptions into model-readable summaries; the next round receives selected summaries and recent detail, not the full action history. This is a context transformation, not evidence of faithful summarization or better decisions. Optional graph updating is a separate enabled server path, not a prerequisite for simulation (SRC-1, `backend/scripts/run_parallel_simulation.py`, `backend/scripts/round_memory.py`, `backend/app/services/simulation_runner.py`).
5. End-of-round completion saves trajectories and closes optional MCP processes. The driver normally retains live environments waiting for interview commands unless `--no-wait` is selected; `--env-only` can load existing databases/profiles without executing simulation rounds. Report section workers receive separate local contexts and no prior-section drafts on the shipped parallel path; the helper can conditionally include truncated previous sections only when its caller supplies them (SRC-1, `backend/app/services/report_agent.py`). Reports and interviews are separate consumers, not a mandatory final step of each agent action ([RT-RTE-interview-manual](#rt-rte-interview-manual), [RT-RTE-report-sections](#rt-rte-report-sections)). Terminal products include logs, database changes, trajectories, interview responses and saved report Markdown/metadata, rather than one global agent answer.

The runner uses `start_new_session=True` and the simulation directory as the subprocess working directory. This supports process-group management and file organization, not a filesystem or network sandbox. Configured model providers and optional MCP processes lie outside the frozen implementation boundary (SRC-1, `backend/app/services/simulation_runner.py`, `backend/scripts/mcp_agent_bridge.py`).

### Four forcing cases and guarantee coverage

**1. Synchronized versus single-platform scheduling.** The server selects dedicated Twitter/Reddit scripts, while Polymarket and parallel modes select the parallel script. The synchronized loop places an asyncio timeout around gathered platform work, logs failures and continues; it is not an atomic round transaction. Partial platform effects can precede an exception, and its successful-platform-only postprocessing does not prove complete action accounting. The environment itself warns that synchronous recommendation work can block the event loop. Therefore the timeout is best effort, not a wall-clock invariant. Owner: parallel driver; enforcement: `asyncio.wait_for`; external contract: tasks must yield and honor cancellation. Covered path: synchronized platform tasks. Single-platform scripts, external-tool postprocessing, storage operations and synchronous work are not thereby bounded (SRC-1, `backend/scripts/run_parallel_simulation.py`, `backend/wonderwall/environment/env.py`).

> results = await asyncio.wait_for(
>     asyncio.gather(*task_coros, return_exceptions=True),
>     timeout=_ROUND_TIMEOUT_SECONDS,
> )
> --- `backend/scripts/run_parallel_simulation.py`

> # runs synchronous PyTorch/twhin-bert embedding code that blocks the
> # asyncio event loop, preventing asyncio.wait_for from firing its
> # timeout. Rec-table state is irrelevant for interview responses.
> --- `backend/wonderwall/environment/env.py`

Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. This is failure containment/continuation, not rollback of platform effects or proof of a finished run.

**2. LLM action versus direct/manual/interview calls.** `SocialAgent` passes a default iteration cap of three and tool-call pruning into Camel. That is a runtime-client request whose exact enforcement relies on the external Camel version. The selected action tool list constrains the LLM tool surface, but `perform_action_by_data` searches the environment's full function list; manual action admission is not the same filter. Interviews call the model response method directly rather than running `astep`. A claim that all decisions pass the three-iteration tool loop would be false ([RT-RTE-interview-manual](#rt-rte-interview-manual)). Owner: SocialAgent/Camel; enforcement: constructor configuration; guarantee strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `backend/wonderwall/social_agent/agent.py`, `backend/wonderwall/environment/env.py`).

**3. Configured extension versus persona allowlist.** `build_agent_toolset` offers per-profile server allowlists, but the inspected synchronized bridge calls `load_registry`, builds a single list of registered servers and grants eligible agent IDs that catalogue. Its dispatch checks eligible ID and post type, then delegates to the registry-backed bridge; it does not apply that helper's profile-specific allowlist. Thus the helper's narrower grant semantics cannot be asserted for this driver. The bridge is default-off; actual manifest, grants and running servers are unobserved. Registered command execution inherits the process environment, so simulation-platform-only effects are not a system-wide guarantee ([RT-RTE-agent-mcp](#rt-rte-agent-mcp)).

**4. Report completion versus evidence sufficiency.** Normal report-section completion rejects an early final answer until two tool calls. Exhausting eight iterations forces an additional generation and returns its content or an error placeholder without the same minimum. A tool-count gate is not a truth oracle even on its covered path. Owner: ReportAgent; enforcement: normal final-answer branch; guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. Alternative direct Claude Code model calls are subprocess requests, not the Wonderwall action loop ([RT-RTE-report-sections](#rt-rte-report-sections), [RT-CMP-model-clients](#rt-cmp-model-clients)).

### Control, change admission and unobserved envelope

The HTTP internal-key guard protects non-exempt `/api/` routes when a key is configured. Without a key it returns 503 in detected deployment/non-debug conditions, but permits local debug operation. Exempt status/documentation paths and non-HTTP entry paths are explicit scope limits; this is not per-agent capability authorization. Some API operations have an additional admin decorator; the inspected start/director paths are not evidence of universal admin gating. Owner: Flask application; enforcement: `before_request`; guarantee strength: policy; external contract: correct deployment detection/key provisioning and request routing. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `backend/app/__init__.py`, `backend/app/api/simulation.py`).

> if not provided_key or not hmac.compare_digest(provided_key, internal_key):
>     logger.warning(f"Unauthorized API access attempt: {request.method} {request.path}")
>     return {'error': 'Unauthorized - Invalid or missing internal key'}, 401
> --- `backend/app/__init__.py`

Capability surface includes configured platform actions, generic SimulationConfig action/environment classes, direct manual calls and optional manifest-defined external tools. Current grants are selected tool lists plus the enabled-ID/registry path, not an observed deployed grant set. Deployment isolation remains uninspected: cwd, process groups and API authentication are not an isolation envelope. No source-grounded claim here attributes provider-native hidden tools or actual external publication to a simulation run.

The main inspected admission mechanisms are automatic persona/config acceptance, caller-authored director/counterfactual context and operator-controlled external-tool registration. They change a simulation's future inputs or callable effects; they are not demonstrated product self-modification. Settings-forwarded model configuration can change future subprocess routing without pinning model weights. Memory/graph revision semantics and their distinct downstream authority require the specialist account rather than treating every write as a universal improvement loop.

## Shared records

### Components

#### RT-CMP-model-clients
Label: Generative model clients

Source-native identities: `create_model`, `LLMClient`, `ClaudeCodeClient` and default/smart/NER factory slots. Representational form: distributed-parametric models interpreting natural-language prompts and structured tool requests. Substrate: external OpenAI-compatible endpoints, or an external Claude Code process; Camel backend objects and HTTP clients are local adapters, not the weights. SRC-1, `backend/scripts/run_parallel_simulation.py`, `backend/app/utils/llm_client.py`, `backend/app/utils/claude_code_client.py`.

The inspected routes perform inference; these adapters contain no parameter update operation. Provider-side training/state is uninspected. Exact model versions are not pinned by these factories: names and base URLs come from configuration/environment, including Wonderwall overrides and a boost slot. Mutable endpoints can resolve to another model. A Claude Code invocation's model is likewise a configurable argument; its host configuration and permissions are outside inspected evidence. Grouping these clients describes the same generative role, not identical provider behavior.

> cmd = ["claude", "-p", prompt, "--output-format", "json"]
> if self.model:
>     cmd.extend(["--model", self.model])
> if max_tokens:
>     cmd.extend(["--max-turns", "1"])
> --- `backend/app/utils/claude_code_client.py`

Here `max_tokens` controls whether a one-turn flag is appended; it is not forwarded as a token limit. No claim about Claude's actual tool access follows from this command.

#### RT-CMP-embedding-service
Label: Graph embedding service

Identity: `EmbeddingService`; form: distributed-parametric encoder and dense vectors. Substrate: configured Ollama/OpenAI-compatible service, an in-process text/vector cache, and graph vector properties at the storage consumer. Inspected inference does not update encoder parameters; provider internals remain uninspected. Model and endpoint are configurable, not immutable-version pinned; a mutable endpoint may change the resolved model. The properties consult current Config unless explicit overrides exist (SRC-1, `backend/app/storage/embedding_service.py`, `backend/app/storage/neo4j_storage.py`).

> def model(self) -> str:
>     return self._model_override or Config.EMBEDDING_MODEL
> --- `backend/app/storage/embedding_service.py`

#### RT-CMP-reranker-service
Label: Graph search reranker

Identity: `RerankerService`; form: distributed-parametric cross-encoder scoring query/document pairs. Substrate: lazily loaded local `CrossEncoder` weights and transient scores. Inference calls `predict`, not parameter training. Exact weight revision is not pinned in this constructor; configurable model names/download resolution can select different weights, though an already loaded instance is reused. There is no remote scoring endpoint in the inspected class. Load/inference failure falls back to fused retrieval scores (SRC-1, `backend/app/storage/reranker_service.py`, `backend/app/storage/search_service.py`).

> self._model = CrossEncoder(self.model_name, max_length=512, device=device)
> --- `backend/app/storage/reranker_service.py`

#### RT-CMP-twhin-bert
Label: Twitter recommendation encoder

Identity: `Twitter/twhin-bert-base`; form: distributed-parametric encoder for recommendation vectors; substrate: local Transformers model/tokenizer objects, resolved pretrained weights and computed vectors. The inspected recommendation path loads and runs pretrained models, not training updates. No immutable weight revision is passed; mutable model repository resolution may differ across installations. It is not a configured remote inference endpoint. Actual installed weights/cache are unobserved (SRC-1, `backend/wonderwall/social_platform/recsys.py`, `backend/wonderwall/environment/env.py`).

> twhin_model = AutoModel.from_pretrained(
>     pretrained_model_name_or_path="Twitter/twhin-bert-base").to(device)
> --- `backend/wonderwall/social_platform/recsys.py`

#### RT-CMP-paraphrase-minilm
Label: Alternate Twitter recommendation encoder

Identity: `paraphrase-MiniLM-L6-v2`; form: distributed-parametric sentence encoder; substrate: SentenceTransformer object and `./models` cache. It is a selectable alternative in `get_recsys_model`, not established as the synchronized default. Inspected use loads pretrained weights without a training update. Exact revision is unpinned; upstream download/cache resolution can differ, not a remote inference endpoint (SRC-1, `backend/wonderwall/social_platform/recsys.py`).

> return SentenceTransformer(model_name,
>                            device=device,
>                            cache_folder="./models")
> --- `backend/wonderwall/social_platform/recsys.py`

### Operative objects

#### RT-OBJ-simulation-config
Label: Simulation configuration control fields

Identity: `simulation_config.json` control fields: time configuration, platform choices and agent IDs/activity levels. Form: symbolic values interpreted by driver code. Substrate: per-simulation JSON file plus loaded dictionaries. Generated reasoning prose is a different consumption part, not executable control merely because it shares the file. Preparation serializes parameters; later starts reload the file. SRC-1, `backend/app/services/simulation_manager.py`, `backend/app/services/simulation_runner.py`, `backend/scripts/run_parallel_simulation.py`.

> target_count = int(random.uniform(base_min, base_max))
> --- `backend/scripts/run_parallel_simulation.py`

#### RT-OBJ-agent-profiles
Label: Persona content in platform profile files

Identity: generated persona content in `reddit_profiles.json`, `polymarket_profiles.json` and `twitter_profiles.csv`. Form: natural-language persona descriptions interpreted through agents' system messages; IDs, enabled flags and file schemas are separate symbolic routing fields. Substrate: per-simulation JSON/CSV files and agent system-message objects. Admission and persistence are described by [RT-RTE-prepare-population](#rt-rte-prepare-population); this record does not establish persona validity. SRC-1, `backend/app/services/simulation_manager.py`, `backend/wonderwall/social_agent/agent.py`.

### Routes

#### RT-RTE-prepare-population
Label: Graph entities to admitted simulation population

Endpoints: graph entities/document requirement → profile generator/config generator → files consumed at simulation start. Owner: SimulationManager. Caller supplies the problem and chooses LLM profile generation; graph reader selects defined entities with edges; models propose persona/config content; software saves it. Operating mode: open caller-specified scenario, not a controlled curriculum. Answer oracle: none identified in this path; graph material is context, not expected-answer grading. Zero matching entities produce a failed preparation. Generation errors produce failed state; no per-item human veto is required by the inspected save path. Recovery is retry/regeneration or caller replacement; semantic rollback of individual generated personas was not established (SRC-1, `backend/app/services/simulation_manager.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: preparation state/progress and saved profiles/configuration, not a simulated outcome.
- Later read-back: runner reloads simulation_config.json; drivers load platform profiles into agent graphs and prompts.
- Delegated visibility: profile generation receives selected entities, requirement and graph-retrieval access; simulation agents receive constructed personas, not necessarily the original document corpus.
- Selection predicate: defined entity types and nonzero filtered population; enabled platforms determine emitted profile files.
- Invalidation or expiry: regeneration/replacement can overwrite files; no semantic validity expiry established by this path.
- Activation or effect: admitted values control later setup/sampling and supply persona prompts; actual behavioral dependence remains unobserved.
- Evidence limits: generation quality, provider outputs, demographic fidelity and successful file consumption are not observed.

> profiles = generator.generate_profiles_from_entities(
>     entities=filtered.entities,
>     use_llm=use_llm_for_profiles,
>     progress_callback=profile_progress,
>     graph_id=state.graph_id,  # Pass graph_id for graph retrieval
>     parallel_count=parallel_profile_count,  # Parallel generation count
>     realtime_output_path=realtime_output_path,  # Real-time save path
>     output_platform=realtime_platform  # Output format
> )
> --- `backend/app/services/simulation_manager.py`

#### RT-RTE-synchronized-rounds
Label: Synchronized multi-platform action loop

Endpoints: prepared simulation start → sampled agent model invocations → platform actions → post-round state/next round. Owners: server runner for process lifecycle; parallel driver for scheduling; SocialAgent/Camel for model/tool steps; platform for effects. Code samples candidates by configured activity probability and a random target population. The model receives persona plus selected runtime context and environment text; it chooses tools through `astep`. Natural-language interpretation and symbolic action dispatch are distinct policies. Each platform's action implementation owns its database semantics; no global cross-platform transaction was established (SRC-1, `backend/app/services/simulation_runner.py`, `backend/scripts/run_parallel_simulation.py`, `backend/wonderwall/environment/env.py`, `backend/wonderwall/social_agent/agent.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: environment step returns after gathered agent tasks; driver records successful platform results and advances round scheduling.
- Later read-back: fetched actions feed subsequent round context, beliefs and cross-platform digests; detailed revision semantics are left to the memory account.
- Delegated visibility: agents get constructed context and environment observations, not all other agents' private conversations; platforms in a synchronized round receive previous-round shared context.
- Selection predicate: enabled/existing platform populations and stochastic active-agent selection; injection additionally tests available context/agent belief state.
- Invalidation or expiry: run termination removes live objects; context injection replaces marked sections and older rounds are compacted, not guaranteed preserved verbatim.
- Activation or effect: model tools can change simulated social/market databases; wiring establishes capacity, not actual decisions or improvement.
- Evidence limits: timeout continuation can follow partial effects; dependency execution, complete action accounting and hard wall-clock bounds are unobserved.

> super().__init__(
>     system_message=system_message,
>     model=model,
>     scheduling_strategy='random_model',
>     tools=all_tools,
>     max_iteration=max_iteration,
>     prune_tool_calls_from_memory=True,
> )
> --- `backend/wonderwall/social_agent/agent.py`

Working-context controls include per-agent conversation objects, Camel tool-message pruning requested above, and code-selected memory compaction. The compactor targets `current_round - 2`, submits a background model call and uses a fallback when unavailable; `build_context` can supply action counts while compaction is pending. Ancient batches replace individual records in RoundMemory. A later model invocation therefore receives transformed text rather than a pointer into an automatically live heap; raw platform databases are distinct retained sources, not automatically followed references (SRC-1, `backend/scripts/round_memory.py`).

> loop.run_in_executor(self._pool, self._compact_sync, rec, full_text)
> --- `backend/scripts/round_memory.py`

#### RT-RTE-interview-manual
Label: Interview and direct-action alternate paths

Endpoints: IPC interview commands or environment ManualAction → direct agent methods → model response/platform effect. The parallel driver's command handler and environment own dispatch; a caller supplies interview text or a symbolic action. Interview prompt assembly reads existing memory and adds the question to a modified system context, then calls `_aget_model_response` directly. Manual non-interview calls search the full environment function list; they need not pass the constructor's selected LLM tool list. These are alternate execution paths, not additional autonomous agents (SRC-1, `backend/scripts/run_parallel_simulation.py`, `backend/wonderwall/environment/env.py`, `backend/wonderwall/social_agent/agent.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: interview content/prompt/success record or direct action result; IPC carries the result to its caller.
- Later read-back: interview prompt/response are recorded through the platform channel; optional interview_record updates conversation memory; manual actions update agent memory with a textual result.
- Delegated visibility: interviewer can receive a returned answer, not direct access to provider reasoning; env-only recreation uses profiles/existing databases rather than proving restoration of every prior in-memory state.
- Selection predicate: command-specified agent/platform or explicit ManualAction target; interview-only batches skip recommendation updates.
- Invalidation or expiry: live environment closure ends the resident context; durable platform records have separate retention semantics.
- Activation or effect: model answer generation and platform interview recording are wired; manual actions directly invoke matched platform functions.
- Evidence limits: no executed IPC exchange, successful reload or restored-context equivalence supplied.

> response = await self._aget_model_response(
>     openai_messages=openai_messages, num_tokens=num_tokens)
> --- `backend/wonderwall/social_agent/agent.py:580-581`

> function_list = self.env.action.get_openai_function_list()
> for i in range(len(function_list)):
>     if function_list[i].func.__name__ == func_name:
>         func = function_list[i].func
>         result = await func(*args, **kwargs)
> --- `backend/wonderwall/social_agent/agent.py`

#### RT-RTE-agent-mcp
Label: Optional agent external-tool bridge

Endpoints: operator manifest/profile flags → tool catalogue in prompt → model-authored post tags → registered subprocess tools → next-activation prompt results. Owner: synchronized driver and MCPAgentBridge. This is capability admission: operator/environment supplies executable server commands and enables the feature; the driver grants eligible IDs; model-authored calls select tools/arguments; bridge rejects unknown/unavailable registered servers. Operating mode: optional external enrichment/action during an open simulation. No answer oracle is supplied by successful RPC completion. The configuration helper's narrower allowlist is not invoked by this driver path. A profile flag is not evidence that a human approved each generated call. Rollback of remote effects is not implemented by dispatch; shutdown closes processes, not their prior effects (SRC-1, `backend/app/services/agent_mcp_tools.py`, `backend/scripts/run_parallel_simulation.py`, `backend/scripts/mcp_agent_bridge.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-call result/error objects and latencies to driver, not necessarily immediate model delivery.
- Later read-back: pending results indexed by agent ID are popped and injected on later activation.
- Delegated visibility: eligible active agents receive a catalogue over registered servers; only eight listed tools/server are displayed, which is not a dispatch authorization limit.
- Selection predicate: global flag/import/registry success; IDs collected from tools_enabled Reddit/Polymarket profiles; selected post/comment/quote content containing parsed mcp_call tags.
- Invalidation or expiry: pending results are consumed on injection; process shutdown ends sessions; remote persistence/expiry is uninspected.
- Activation or effect: configured server tools may execute outside simulated platforms; actual calls, remote effects and model use of results are unobserved.
- Evidence limits: deployed manifest/grants absent from evidence; per-persona allowed_tools enforcement cannot be inferred from the unused helper; inherited host privileges are not sandboxed by this bridge code.

> mcp_server_names = list(registry.keys())
> --- `backend/scripts/run_parallel_simulation.py`

> results = bridge.dispatch_calls(calls)
> --- `backend/scripts/run_parallel_simulation.py`

> merged_env = dict(os.environ)
> merged_env.update(env or {})
> self._proc = subprocess.Popen(
>     [command, *args],
> --- `backend/scripts/mcp_agent_bridge.py`

The parser caps calls and tolerates malformed argument JSON by substituting `{}`. Bridge failures become result objects, not proof that all remote side effects were prevented. Per-call timeout is best effort at the RPC reader boundary; it neither guarantees cancellation of the remote operation nor bounds the whole simulation.

#### RT-RTE-director-context
Label: Caller-supplied director context admission

Endpoints: HTTP event text → pending-event files → round-boundary consumption → active-agent system text. Owner: API validation and driver injection. Caller proposes the event; code accepts nonempty text of at most 500 characters when simulation exists/runs and count is below ten. This is user-authored scenario change, not automatic criticism of a theory or factual verification. Operating mode: interactive intervention; counterfactual branch text is another injected scenario mode. Answer oracle: none established. Validation can reject input; no semantic approval gate determines whether the fictional event is true. Events/history persist; fresh start clears director-event files. There is no demonstrated undo of actions taken under an injected event (SRC-1, `backend/app/api/simulation.py`, `backend/scripts/director_events.py`, `backend/scripts/run_parallel_simulation.py`, `backend/app/services/simulation_runner.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: accepted event and count, or validation/error response.
- Later read-back: pending events are consumed at round boundaries; event history persists; active agents receive event text through system-message mutation.
- Delegated visibility: the driver injects into currently active agents, not every dormant agent's invocation at once.
- Selection predicate: running simulation, bounded text/count and pending round event; counterfactual text additionally tests its trigger.
- Invalidation or expiry: injection replaces an earlier marked director section when another event is injected; no unconditional clearing on event-free rounds was established in this path.
- Activation or effect: text explicitly requests changed stance/trading/posting; delivery is wired, actual compliance unobserved.
- Evidence limits: API caller identity alone does not prove a human authored the event; no intervention trace establishes a causal behavior change.

> f"React to this information in your next action — "
> f"it may change your stance, trading behavior, or what you post about."
> --- `backend/scripts/director_events.py`

#### RT-RTE-report-sections
Label: Report section retrieval and composition loop

Endpoints: simulation requirement/outline → parallel section workers with empty previous-sections input → bounded section loop → tool observations → section Markdown → retained report. Owner: ReportAgent; model proposes tool calls and text; code parses calls, enforces quotas/conflict retries and admits final content. Operating mode: report composition for an open scenario, not a benchmark with reference answers. Tools supply simulation/graph/interview evidence, not an answer oracle; no correctness grade follows from two calls. Sections get separate messages. The helper conditionally truncates previous-section text when supplied, but the shipped parallel caller passes an empty list: these workers receive no prior-section drafts, only the helper's first-section placeholder in that input slot. Admission includes model output accepted after normal checks or forced completion after iteration exhaustion; errors can yield a placeholder. Caller can regenerate, but inspection does not establish a semantic report rollback gate (SRC-1, `backend/app/services/report_agent.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: section text, including forced-finish/error-placeholder alternatives; report orchestration assembles sections.
- Later read-back: ReportManager saves metadata/outline/Markdown and reloads reports; optional reasoning traces have separate storage consumers.
- Delegated visibility: section-local messages and tool observations, with no prior-section drafts on the shipped parallel path; the helper's truncated prior-section input is a conditional capability unused by this caller, not delivered sibling context.
- Selection predicate: outline section and model-selected parsed tools; only first tool call per response executes; configured quota limits normal dispatch.
- Invalidation or expiry: local section frame ends after return; saved report survives it; no factual-validity expiry established.
- Activation or effect: retrieval/interview tools and Markdown retention are wired; evidential completeness and accurate synthesis remain unobserved.
- Evidence limits: normal minimum-tool gate has a force-finish alternate; no supplied reports or provider outputs demonstrate grounding or successful generation.

> previous_sections=[],  # parallel: sections don't see each other
> --- `backend/app/services/report_agent.py`

The helper's excerpt capability is conditional on caller-supplied content:

> if previous_sections:
>     per_section_budget = max(400, MAX_PREVIOUS_TOTAL // len(previous_sections))
> --- `backend/app/services/report_agent.py`

> max_iterations = 8  # Maximum iteration rounds
> min_tool_calls = 2  # Minimum tool call count
> --- `backend/app/services/report_agent.py`

> # Reached maximum iterations, force content generation
> logger.warning(f"Section {section.title} reached maximum iterations, forcing generation")
> messages.append({"role": "user", "content": REACT_FORCE_FINAL_MSG})
> --- `backend/app/services/report_agent.py`

> # Save complete Markdown report
> if report.markdown_content:
>     with open(cls._get_report_markdown_path(report.report_id), 'w', encoding='utf-8') as f:
>         f.write(report.markdown_content)
> --- `backend/app/services/report_agent.py`

#### RT-RTE-storage-mcp
Label: Direct stdio graph and report consumption

Endpoints: external MCP client request → stdio server → direct Neo4jStorage calls → text/JSON result. Owner: MCP server dispatch, not Flask or the simulation scheduler. It supports graph search, cluster browsing and retained report/trace lookup. Browsing clusters can automatically build communities if none exist, so this consumer is not strictly read-only. Community-content semantics are left to the memory account. Query/identifier selection is symbolic dispatch combined with retrieval model scores ([RT-CMP-embedding-service](#rt-cmp-embedding-service), [RT-CMP-reranker-service](#rt-cmp-reranker-service)). SRC-1, `backend/mcp_server.py`, `backend/app/storage/search_service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: serialized results or an error as MCP TextContent.
- Later read-back: existing retained graph/report objects are read; automatic community construction supplies later cluster consumers.
- Delegated visibility: external MCP client receives selected results with embeddings stripped, not the entire database or model weights.
- Selection predicate: tool name and supplied graph/query/UUID arguments; browse may select query hits or a limited cluster slice.
- Invalidation or expiry: graph search forwards as_of/include_invalidated/kinds options; external client caching is uninspected.
- Activation or effect: direct storage calls and optional community construction are wired; client use or model uptake unobserved.
- Evidence limits: HTTP guard does not cover stdio; host launch permissions and deployed database credentials are external contracts, not assessed isolation.

For automatic community admission, the trigger is missing communities during browse, the proposal/construction is delegated to storage, and this adapter immediately re-reads resulting communities. No human per-community approval or rollback is provided by this adapter; deeper construction/recovery is uninspected here. Operating mode: requested browsing; no answer oracle established.

> existing = s.list_communities(graph_id)
> if not existing:
>     stats = s.build_communities(graph_id)
>     logger.info(f"Auto-built communities: {stats}")
>     existing = s.list_communities(graph_id)
> --- `backend/mcp_server.py`

### Claims

#### RT-CLM-graph-memory
Label: Optional graph memory for subsequent analysis

The shipped start API claims that enabled activity updating lets the graph remember a simulation for later analysis/conversation. Implementation provides optional updater creation and failure handling; not every run enables it and this claim is not an observed retention/completeness result. SRC-1, `backend/app/api/simulation.py`, `backend/app/services/simulation_runner.py`.

> - This allows the graph to "remember" the simulation process, for subsequent analysis or AI conversation
> --- `backend/app/api/simulation.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-context
Label: Injected context to simulated decisions

Consumer: SocialAgent model invocation. Channel: persona/system-message content plus environment observation user message. Force: model-interpreted instructions/evidence, not deterministic truth enforcement. Horizon: current invocation and subsequent rounds while the mutated system content remains. [RT-RTE-synchronized-rounds](#rt-rte-synchronized-rounds) and [RT-RTE-director-context](#rt-rte-director-context) deliver the material; retained memory parts have their own update semantics. Authority here means capacity to shape decisions through model interpretation, not observed compliance (SRC-1, `backend/wonderwall/social_agent/agent.py`, `backend/scripts/director_events.py`).

> response = await self.astep(user_msg)
> --- `backend/wonderwall/social_agent/agent.py`

## Annotations

none
