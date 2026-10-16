---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SwarmWorld runtime baseline: model planning, authoritative world stepping, human overrides, artifact programs, scenario admission and recorded replay."
run-id: AAS-2026-10-15-swarmworld-e39fbc17e3fb-01
reviewed-boundary: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
---

# SwarmWorld runtime report

## Runtime account

SwarmWorld encloses a society simulation rather than delegating host-computer work to autonomous shell users. Its historical package and executable name is `biofoundry`. The ordinary model-driven path constructs a world and population, schedules selected agent IDs, asks a configured model for a private research-state update and a bounded action plan, queues the admitted actions, and executes one action per agent per world tick. The Python simulation owns world effects; the model chooses proposed scientific work. Episode completion produces events, snapshots, state digests and summary/evaluation metrics, not a model-certified scientific answer ([RT-RTE-model-planning](#rt-rte-model-planning), [RT-RTE-world-stepping](#rt-rte-world-stepping)). This is implementation evidence from SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/policies/llm.py` and `src/biofoundry/simulation.py`.

The frozen source and exclusions remain those of [the boundary](boundary.md#boundary-and-evidence). All added inspections below are SRC-1 at the same commit. They add implementation coverage of `src/biofoundry/structured_output.py`, `src/biofoundry/capabilities.py`, `src/biofoundry/programs.py`, `src/biofoundry/artifacts.py`, `src/biofoundry/policies/scripted.py`, `game/policy.py`, and deeper portions of the CLI, server, environment adapter, scenario loader, counterfactuals and ecology evaluator. The world-builder skill supplies doctrine/design only. No target code, tests, provider calls or examples were executed. All operation and benefit conclusions remain uninspected; source wiring is not a successful episode.

### Ordinary invocation and ownership

The installed CLI's policy factory selects `scripted`, `scalable`, `research-oracle`, or an `LLMPolicy` with `OpenAICompatibleProvider`. `_simulate_episode` creates the authoritative `BioFoundrySimulation`, opens an `EventRecorder`, writes an initial snapshot, and repeats planning, action recording, world stepping and periodic snapshotting for the requested tick horizon. It then writes a final snapshot/digest and returns aggregate metrics. Evaluation is an optional consumer of the resulting society, not a prerequisite that approves each model plan (SRC-1, `src/biofoundry/cli.py`).

> policy = _policy(policy_name, config)
> --- `src/biofoundry/cli.py`

> result = simulation.step(actions)
> --- `src/biofoundry/cli.py`

The trigger for a model macroturn is a phase-shifted periodic schedule over active agents, augmented by `needs_replan` when collective-science event-driven immediate replanning is enabled. An exhausted action-attempt budget suppresses scheduling. Stable agent IDs select private memories and action queues; tick numbers identify research-state writes and trace records. `_decide` gathers semantic observations, the latest research state, selected private records and the treatment-specific action manual. Concurrent decisions share a world that has not yet stepped. Completion order does not set the order of stored traces: traces are sorted by agent ID. The policy owns queue replacement, while the simulation owns subsequent action effects (SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/policies/llm.py`).

The runtime constructs two provider messages afresh for each decision. There is no accumulating provider conversation in this path. With `experience_attention` enabled, a character-budget rule first drops retrieved-memory entries from the end, then removes lower-priority observation items. Minimum-size lists and the remaining causal core can prevent further shrinkage, so the configured character budget is not an unconditional hard context limit. Static system guidance, the latest research state and the remaining observation survive; the underlying memory records are not deleted by trimming. A later decision can retrieve them again. This is selective by-value context construction, not a pointer-following heap or a sub-agent frame. Independent per-agent requests isolate input packets but share the authoritative simulator through the enclosing driver (SRC-1, `src/biofoundry/policies/llm.py`).

> if memory_entries:
>     memory_entries.pop()
> elif not _shrink_observation(observation_packet):
>     break
> --- `src/biofoundry/policies/llm.py`

The model response is text interpreted as JSON, transport numbers are coerced, a local schema validator checks the plan, and values are converted to `AgentAction`. Successful admission writes research state before queue commitment. Provider or output errors produce a WAIT plan and an error trace. In the optional freeze mode, any scheduled transient-provider error causes the policy to restore scheduled agents' memory snapshots and preserve old queues, then return false. The CLI/live/human drivers honor false by not stepping, waiting and retrying. It is not merely a freeze on a *total* outage despite the method docstring. In non-freeze mode, failed decisions replace their queues with WAIT. The convenience `LLMPolicy.actions()` calls `next_actions()` regardless of `refresh_plans()`'s return, so freeze-on-outage is a driver protocol, not a universal policy invariant (SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/cli.py`, `src/biofoundry/server.py`, `game/session.py`).

### Material alternate and forcing routes

Four forcing families bound the runtime conclusions:

1. **Invalid output and partial provider failure.** Local validation is downstream of both provider `generate_record` and fallback `generate`. Disabling provider structured output does not disable this local check. The configured provider plan length can be smaller than the local validator's `MAX_PLAN_ACTIONS`; consequently the local validator is not independent enforcement of the smaller configured limit. Freeze requires the driver protocol above, and a single transient failure is sufficient to freeze a batch (SRC-1, `src/biofoundry/structured_output.py`, `src/biofoundry/policies/llm.py`).
2. **Bypassing model planning.** Live manual actions overwrite planned actions; human possession additionally excludes a slot from model scheduling and queue consumption. PettingZoo clients and scripted policies can supply actions directly to `simulation.step`. These routes bypass the model-response schema but converge on simulator action conversion and physical/treatment checks. There is no per-model-action human approval requirement on the ordinary path ([RT-RTE-direct-control](#rt-rte-direct-control)).
3. **Admitting executable artifact changes.** WRITE_PROGRAM and FORK_PROGRAM install bounded DSL programs; BUILD can also install a supplied program, and artifact creation otherwise installs a default. Both installation paths reach `ArtifactProgram.validate` and `ArtifactStore.install_program`. Fork lineage rules apply to FORK_PROGRAM, not to every program installation. Programs affect simulated services, not Python runtime machinery ([RT-RTE-program-install](#rt-rte-program-install)).
4. **Durable reconstruction without a model.** Replay restores committed research-state writes and policy scheduling mutations, then steps recorded actions. Revision, scenario hash, tick and snapshot-digest checks can reject incompatible material. Replay tests agreement with recorded state; it does not reproduce model decision-making or prove the science correct ([RT-RTE-recorded-replay](#rt-rte-recorded-replay)).

The `research-oracle` route is materially different from an ordinary model society. It supplies a fixed default recipe, assigned worker/builder roles and direct world-resource inspection through deterministic Python. Its class describes itself as an upper-bound policy. It is not an answer oracle consulted by `LLMPolicy`; it is a separate experimental controller. Scripted/scalable policies likewise choose actions without model calls. Their capacities must not be attributed to the local-information model path (SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/policies/scripted.py`).

> """Transparent upper-bound policy that exercises the complete research lifecycle."""
> --- `src/biofoundry/policies/scripted.py`

### Guarantees, grants and external contracts

| Guarantee and owner | Enforcement, strength and coverage | Alternate paths, dependencies and conclusion |
|---|---|---|
| Structured model plans; LLM policy | Local JSON/schema admission before research-state writing and queue replacement. Strength: invariant for this admission path, not semantic truth. | Direct controllers and replay do not pass through it. Provider constrained decoding is additional help, not the local check's prerequisite. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/structured_output.py`. |
| Treatment action restrictions; simulator | `available_action_types` controls prompts, schema and action-dispatch rejection. Strength: policy enforced in ordinary simulator dispatch. | Direct actions still reach the dispatcher. Movement and some bookkeeping occur before verb rejection, so this is not a general transaction/isolation guarantee. Python callers can manipulate exposed state outside `step`; no deployment sandbox is established. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/capabilities.py`. |
| Bounded artifact execution; program validator and VM | Allowed operations/registers/sensors, 1–64 instructions, straight-line evaluation and bounded per-instruction actuator outputs. Strength: invariant over validated DSL execution. | WRITE/FORK, BUILD, defaults and direct store installation converge on validation. Per-instruction clipping does not establish a single total 0.05 actuation budget across repeated instructions. No claim about arbitrary Python extension safety. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/biofoundry/programs.py`, `src/biofoundry/artifacts.py`. |
| No advancement during configured transient outage; shipped drivers | Memory snapshot restoration plus preserved queues, with callers honoring false. Strength: protocol. | Disabled by default in `LLMConfig`; terminal provider errors/invalid output do not invoke it, and convenience `actions()` does not honor it. Depends on provider error classification and eventual service recovery, not a retry deadline. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/biofoundry/config.py`, `src/biofoundry/policies/llm.py`. |
| Deterministic replay checking; CLI | Engine compatibility, scenario package hash when recorded, tick agreement and snapshot/state-digest comparison. Strength: protocol. | Old/mismatched engine traces may receive snapshot-integrity checks with deterministic replay skipped. Needs complete compatible trace/config/package and matching engine behavior. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/biofoundry/cli.py`. |

The capability surface is the action enum and bounded DSL; the current grant set is derived from experiment configuration, including communication, depot, forking, metabolism, addressing and reply tracking. These are experimental affordances, not operating-system permissions. The inspected provider request supplies messages and output format, not provider-native tools. The interpreter has no shell/network instruction. This does not prove sandboxing of the server, Python host, model service or external authoring agent. The stock WebSocket handler accepts a connected client's dictionary commands and invokes the live controller; the inspected handler establishes no per-command approval barrier. Configuration defaults to loopback hosting, but actual deployment exposure and external authentication are not supplied (SRC-1, `src/biofoundry/capabilities.py`, `src/biofoundry/providers/openai_compatible.py`, `src/biofoundry/programs.py`, `src/biofoundry/server.py`, `src/biofoundry/config.py`).

Outside episodes, scenario authors can change package data and runtime prompts through a separate authoring workflow. Loader checks, hashes and replay compatibility provide mechanical admission; the shipped skill asks authors to validate and test, but is not an automatic production gate. In-world agents are instructed not to mutate packages. That instruction is distinct from deployment isolation ([RT-RTE-scenario-admission](#rt-rte-scenario-admission)). Private/public knowledge writes and their revisions remain the memory analyst's responsibility; the runtime here establishes their entry and downstream effect boundaries, not a full memory inventory.

## Shared records

### Components

#### RT-CMP-configured-model
Label: Configured provider model

Identity: the model selected by `LLMConfig.model` and served through the configured Responses endpoint. Representational form: distributed-parametric computation in external model weights. Storage substrate: external serving infrastructure; the repository stores only configuration and request/response representations. The inspected path issues inference calls, not weight updates. Parameter change inside the service is uninspected. Exact weights/version are not pinned by this source: a model-name string and optional response model metadata are not a weight digest. A mutable base URL/model alias can resolve to different served weights. Provider internals and any server-side learning are outside supplied evidence. SRC-1, `src/biofoundry/config.py`, `src/biofoundry/providers/openai_compatible.py`.

> "model": self.config.model,
> --- `src/biofoundry/providers/openai_compatible.py`

> "store": False,
> --- `src/biofoundry/providers/openai_compatible.py`

The second passage is a request to the provider, not independent evidence of provider retention practices. This component is used by [RT-RTE-model-planning](#rt-rte-model-planning); learning through retained simulator material is independent of model-weight fixity.

### Operative objects

#### RT-OBJ-action-queues
Label: Agent action queues

Identity: `LLMPolicy.action_queues`, keyed by agent ID. Representational form: symbolic `AgentAction` sequences with fixed enum/field consumption. Storage substrate: in-process dictionary of deques; action records in an optional/CLI recorder persist chosen tick inputs, not a restored live deque. Successful refresh replaces a scheduled agent's queue; `next_actions` consumes one action or returns WAIT. Failed transient batches in freeze mode preserve queues. SRC-1, `src/biofoundry/policies/llm.py`.

> self.action_queues[agent_id] = deque(plan)
> --- `src/biofoundry/policies/llm.py`

#### RT-OBJ-artifact-program
Label: Artifact behavior program

Identity: `ArtifactProgram`, with content ID derived from canonical instruction JSON, independent of name, author and claimed parent. Representational form: symbolic bounded instruction sequence. Storage substrate: in-process artifact program slots, program library and provenance/history mappings; trace/snapshot serialization can retain program content. Names and lineage metadata are separate from executable identity. This record concerns executable form, not the full program-knowledge/memory store. SRC-1, `src/biofoundry/programs.py`, `src/biofoundry/artifacts.py`, `src/biofoundry/simulation.py`.

> return f"program_{hashlib.sha256(payload.encode('utf-8')).hexdigest()[:24]}"
> --- `src/biofoundry/programs.py`

#### RT-OBJ-scenario-prompt
Label: Scenario agent instructions

Identity: the scenario manifest's `agent_prompt` file loaded by `ScenarioDefinition.agent_prompt`. Representational form: natural language interpreted by the model. Storage substrate: UTF-8 package file, embedded into the scenario system message at decision time. It is distinct from the symbolic catalogs and geometry loaded from YAML. Path containment checks apply, and its bytes contribute to the package hash. It is static shipped guidance rather than an episode-generated memory. SRC-1, `src/biofoundry/scenarios.py`, `src/biofoundry/policies/llm.py`.

> scenario_instructions=simulation.scenario.agent_prompt,
> --- `src/biofoundry/policies/llm.py`

### Routes

#### RT-RTE-model-planning
Label: Model macroturn planning

Endpoints and progression: active scheduled agent ID → local observation/retrieved context → provider inference → local structured admission → private research-state write and action queue replacement. Owner: policy and enclosing driver; model proposes goals, hypotheses and action sequences; software decides schema acceptance and can veto malformed proposals. No ordinary per-content human approval. The operating mode is open-ended research within a configured world/treatment and finite plan/action/call budgets. No expected-answer oracle is supplied to this model decision; observations and action outcomes are evidence, not a reference answer. SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/structured_output.py`, `src/biofoundry/simulation.py`.

- Immediate return: `_decide` returns agent ID, proposed typed plan and trace; `refresh_plans` returns a commitment boolean and exposes sorted traces.
- Later read-back: accepted private research-state content is loaded as `prior_state` at a later macroturn; retrieval also supplies retained records. Detailed memory revisions are outside this route's assessment.
- Delegated visibility: each model invocation sees that agent's selected observation, prior state and memory excerpts, not another model's hidden reasoning; communication reaches others through simulator channels rather than sub-agent delegation.
- Selection predicate: phase/event schedule intersected with active agents, bounded by remaining call budget; retrieval uses prior state, pending requests and local observation, with optional adaptive controls.
- Invalidation or expiry: successful refresh replaces an old plan; queue entries expire through consumption; provider-outage freeze preserves them. Prompt trimming omits records without deleting their stores.
- Activation or effect: accepted plans become queued actions; later simulator admission determines world effects. Delivery of a hypothesis or retrieved text does not establish model reliance or successful science.
- Evidence limits: implementation inspected only; model compliance, behavioral dependence on particular memory content and useful outcomes are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> decoded = validate_action_plan(
>     coerce_transport_numbers(_extract_json(response)),
> --- `src/biofoundry/policies/llm.py`

> self.provider_outage = bool(transient_provider_failure and freeze_on_outage)
> --- `src/biofoundry/policies/llm.py`

Recovery: provider/output exceptions yield WAIT; freeze mode restores scheduled memories and declines batch commitment on a transient error. Guidance asks for empirical grounding, goals/hypotheses/checkpoints and bounded plans; retained research state is model-authored, not a truth-certified theory. The route can formulate and revise such text but the supplied source contains no executed candidate showing its theory content or criticism. Theory-builder conditions 1–4: condition 1 conclusion status: afforded (a hypothesis field permits localized formulation); condition 2 conclusion status: uninspected (later delivery is wired, content-dependent decisions are not demonstrated); condition 3 conclusion status: uninspected (prompt requests revision but no claim/result/blame/revision instance is supplied); condition 4 conclusion status: uninspected (read-back wiring alone does not show criticism shaping a next round). Addressability: whole research-state fields are exposed and replaceable; actual assumption structure is uninspected. Persistence: notebook write and later macroturn consumption within an episode are wired. Learning: improved future capacity and attribution are uninspected. Reflection: an agent's goal/progress self-description is requested and returned to later context, but both causal directions for a selected aspect are unestablished. Reflective and autonomous theory building are uninspected, independently of automatic scheduling. No exercised self-improvement is attributed.

#### RT-RTE-world-stepping
Label: Authoritative microtick stepping

Endpoints and progression: action mapping → active-ID selection and `AgentAction` conversion → action-budget/energy handling → movement/observation → action dispatcher → artifact/world evolution and recorded outcomes. Owner: `BioFoundrySimulation`, called by episode/live/human/env/replay drivers. Decision policy is symbolic Python control and configured physics, not model judgment. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/capabilities.py`.

- Immediate return: `StepResult` with events, rewards and artifact score; the driver records events/snapshots or returns environment rewards and termination/truncation information.
- Later read-back: private observations/action outcomes and changed world state can enter later semantic observations; terminal snapshots and event traces support replay/analysis.
- Delegated visibility: local observations restrict what each policy receives; the simulation itself owns global arrays and dispatch order. Public records and spatial communication expose selected effects to other agents.
- Selection predicate: known active IDs; unspecified/invalid action values become WAIT; non-WAIT attempts consume the optional budget in tick-rotated fair order; treatment flags govern executable verbs.
- Invalidation or expiry: one tick consumes the supplied actions; blocked budget entries are replaced with WAIT. Artifacts and retained records have separate lifecycles, not action-map lifetime.
- Activation or effect: admitted actions can harvest, communicate, test, construct and program simulated artifacts; material/facility/evidence/target checks can reject individual actions. World and artifact dynamics then advance.
- Evidence limits: these checks do not establish general rollback, semantic truth of prose, OS isolation or successful physical-world prediction; no run was inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if action.verb not in executable_actions:
>     raise ValueError(
>         f"{action.verb.name} is disabled by this experimental treatment"
>     )
> --- `src/biofoundry/simulation.py`

This is an admission route for simulated products as well as a general executor. The policy/human/script proposes; simulator checks decide and can veto; no answer oracle approves correctness. BUILD in collective-science mode requires a recipe and artifact specification, executes resource-pool fabrication, optionally parses a supplied program and registers the installed program. Claimed function/prose is recorded separately from physics. Rejected actions produce error events and configured feedback; already performed sub-effects are not covered by a general transactional rollback. Replacement/repair/dismantling are later actions, not automatic restoration. This route supports bounded research experiments but does not itself optimize hypotheses or certify improvements (SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/artifacts.py`).

#### RT-RTE-direct-control
Label: Direct and human control

Endpoints and progression: scripted/scalable/research-oracle policy, manual WebSocket command, possessed human slot or PettingZoo caller → action mapping → common simulator step. Owners: selected Python controller, live/human driver or environment caller, with final simulation admission. `research-oracle` uses a fixed recipe/roles and privileged world inspection; the ordinary model path does not consult it. SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/policies/scripted.py`, `src/biofoundry/server.py`, `game/session.py`, `game/policy.py`, `src/biofoundry/env.py`.

- Immediate return: live control acknowledgement, human-input acknowledgement or environment observations/rewards/done maps; action effects occur on the next driver step rather than in the control acknowledgement.
- Later read-back: altered world/retained state reaches later observations; recording captures effective actions, and human sessions additionally write intervention sidecar records.
- Delegated visibility: humans receive the selected slot observation; direct Python policies/environment clients can access their exposed simulation API. No uniform local-information restriction applies to all these controllers.
- Selection predicate: selected policy name; known manual target ID; dynamic human possession excludes the corresponding agent from model scheduling and queue consumption; human input takes precedence after manual merges.
- Invalidation or expiry: manual overrides are cleared after merging; human inputs pop from their queue; possession release restores model eligibility while its old queue has been frozen rather than consumed.
- Activation or effect: final merged actions reach the same simulator action dispatcher, bypassing LLM response-schema admission.
- Evidence limits: client possession is not a deployment sandbox or proof of authentication; no interactive or environment session was executed. Human choice and scripted baseline behavior are not model autonomy evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> actions.update(self.manual_actions)
> self.manual_actions.clear()
> --- `src/biofoundry/server.py`

> actions[self.human.agent_id] = action
> --- `game/session.py`

For candidate/admission decisions, the chosen controller proposes and the simulator can veto; a human action is human content selection, not human approval of each remaining model action. Modes include scripted control, privileged research baseline and interactive research. The fixed default recipe is an explicit reference candidate in the research-oracle mode, not a ground-truth answer for all worlds. Recovery remains per-action simulator rejection plus later control inputs; restarting/resetting is caller responsibility.

#### RT-RTE-program-install
Label: Artifact program admission

Endpoints and progression: WRITE_PROGRAM/FORK_PROGRAM action, or BUILD's optional program → `ArtifactProgram.from_dict` → validation → artifact installation → later VM evaluation of sensors and actuator outputs. Owner: simulator and artifact store. Programs are proposed by the active controller; software can veto invalid DSL, unavailable targets and invalid ancestry. No routine human approval or performance-based pre-install selection is required. Mode: bounded research capability changes to simulated artifacts, not changes to the Python agent runtime. No answer oracle verifies usefulness. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/programs.py`, `src/biofoundry/artifacts.py`.

- Immediate return: installed-program event/provenance and the enclosing step result, or action-rejection feedback.
- Later read-back: content-addressed programs, lineage and recorded performance history can later be observed or retrieved through program knowledge; installed instructions are evaluated on subsequent artifact steps.
- Delegated visibility: program knowledge depends on observation/authorship/teaching/inheritance; a fork must name a known resolvable parent. Installation changes a shared simulated artifact, not a private model weight set.
- Selection predicate: WRITE/FORK requires a non-retired artifact at or near the target; FORK requires enabled forking, a known parent, changed instructions and acyclic lineage; BUILD also admits an original program or default.
- Invalidation or expiry: replacement closes the previous program-history interval and resets peak counters; retired/dismantled artifacts cannot be reprogrammed through this route. History is retained, not an automatic rollback trigger.
- Activation or effect: `ArtifactStore.step` supplies sensors to the VM; fixed op semantics produce actuator requests subsequently gated by artifact/environment mechanics. No executed effect or improvement is established here.
- Evidence limits: bounded DSL safety is narrower than host sandboxing; validation checks vocabulary/shape, not scientific merit, global numeric safety or an empirical improvement objective.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.artifacts.install_program(artifact, program, self.tick)
> --- `src/biofoundry/simulation.py`

> program.validate()
> history = self.provenance[index]["program_history"]
> --- `src/biofoundry/artifacts.py`

> """Straight-line interpreter: no jumps, loops, allocation, or external access."""
> --- `src/biofoundry/programs.py`

The proposal guidance explicitly forbids Python/shell/imports/network/loops and supplies the action manual and sensor/actuator vocabulary. Instructions, not prose claims of ancestry or function, persist as the executable artifact. Recovery is another valid installation or artifact intervention; the inspected route has no automatic performance-regression rollback. This is product/capability adaptation inside the simulated world, not sufficient evidence of improvement to the enclosing runtime. A DSL program can encode hypotheses, but no particular installed program/theory is supplied for content-directed theory assessment; ancestry and instruction diffs alone establish no formulated criticism.

#### RT-RTE-recorded-replay
Label: Recorded state reconstruction

Endpoints and progression: recorded header/model traces/actions/snapshots → compatible fresh simulation → committed private-state restoration and macroturn acknowledgement → recorded-action stepping → digest comparison. Owner: replay CLI and replay helpers; symbolic replay rules decide, not a new model call. SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/counterfactuals.py`.

- Immediate return: replay counts, integrity/deterministic verification counts, final digest and any deterministic-skip reason; mismatch can raise an error.
- Later read-back: recorded research state is restored to the simulator notebook before later replay steps; reconstruction itself does not request a new model decision.
- Delegated visibility: offline replay/analysis consumers receive the reconstructed simulation/summary, not access to unrecorded model internals.
- Selection predicate: trace order, known agent IDs and commitment markers; false `planning_committed` records are not restored. Engine revision/config/package checks determine whether deterministic replay proceeds.
- Invalidation or expiry: engine incompatibility skips deterministic reconstruction; scenario hash mismatch, tick disagreement or digest mismatch rejects the corresponding verification claim.
- Activation or effect: authoritative recorded actions, not generated text re-interpretation, drive the reconstructed world. Counterfactual replay can replace selected agents' actions with WAIT without replanning other agents.
- Evidence limits: a deterministic check is only wired here; no supplied run demonstrates it passing. Counterfactual action replay is a fixed-action intervention, not an adaptive alternative society or a correctness oracle for the scientific claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if record.get("planning_committed") is False:
>     return
> --- `src/biofoundry/counterfactuals.py`

> if replayed != record["state_digest"]:
> --- `src/biofoundry/cli.py`

This is reconstruction/admission of recorded state, with mechanical integrity checks and recorded snapshots as reference outcomes. The caller supplies a trace; replay software can reject incompatibility. It does not improve the trace or revise the controller. Recovery is a compatible engine/package/trace rather than silently accepting a new interpretation.

#### RT-RTE-scenario-admission
Label: Scenario package admission

Endpoints and progression: external author edits a scenario package/config → manifest-routed safe YAML and prompt loading → catalog/geometry/field/recipe validation and package hashing → scenario world plus prompt/schema adaptation. Owner: external author for edits, loader for mechanical acceptance. The shipped world-builder skill requests version bumps, isolated paths and verification; human review and compliance with those instructions are not enforced by the loader. SRC-1, `.agents/skills/swarmworld-world-builder/SKILL.md`, `src/biofoundry/scenarios.py`, `src/biofoundry/policies/llm.py`.

- Immediate return: loaded `ScenarioDefinition` or descriptor from validation; invalid format/path/catalog entries can raise an error.
- Later read-back: static package content is reused by simulations and recorded as scenario metadata/hash; this is authored configuration, not a use-generated memory route. `agent_prompt` reads package text when requested.
- Delegated visibility: the model receives scenario instructions, descriptor/catalog observations and scenario enums; researcher guidance is not automatically equivalent to runtime agent instructions.
- Selection predicate: configured `world.scenario_package`; manifest document routes and `agent_prompt`; paths must resolve to files inside the package.
- Invalidation or expiry: hashes expose package differences to compatible replay checks; `load_scenario` caches definitions by resolved root, while `validate_scenario` loads anew. File editing alone does not establish invalidation of an already cached definition.
- Activation or effect: accepted package data parameterizes the simulator and action vocabulary; accepted prompt text shapes model requests through natural-language instruction, without proof of compliance.
- Evidence limits: no authoring run, human review, successful regression suite or production deployment is supplied. Skill requirements are doctrine/design, loader checks are implementation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Package YAML is data only. Never add executable Python, shell commands, imports, network access, or self-modifying behavior to a world package. Do not let in-world agents mutate the active package during an episode.
> --- `.agents/skills/swarmworld-world-builder/SKILL.md`

> manifest = _mapping(yaml.safe_load(manifest_path.read_text(encoding="utf-8")), "scenario")
> --- `src/biofoundry/scenarios.py`

Trigger and proposed change: operator/author request to create, revise, review or debug a declarative world. Proposal guidance is a coherent catalog/geometry/mission/prompt package using format-v1 constraints. The external author can revise or withhold changes; loader errors can veto mechanical admission. Verification instructions request checks, deterministic tests, smoke traces and replay, but neither their execution nor per-content human approval is established. Recovery is author correction and compatible package selection; version/hash metadata is not automatic rollback. This changes environment/product configuration and model guidance, not an in-episode self-modifying machinery path.

#### RT-RTE-ecology-assay
Label: Frozen society evaluation

Endpoints and progression: existing discovery simulation → deep-copied source society → optional held-out disturbance schedule → agent-free intact and artifact-knockout trajectories → ecosystem metrics. Owner: evaluator code; optional CLI checkpoint/final evaluation invokes it. SRC-1, `src/biofoundry/technology_ecology.py`, `src/biofoundry/cli.py`.

- Immediate return: resilience/service/performance comparisons, knockout effects and held-out summary fields.
- Later read-back: reports and summaries can be consumed by offline analysis; the inspected episode driver does not feed assay conclusions back into model-plan admission.
- Delegated visibility: evaluator receives the existing simulation and internal artifact state, not merely local agent observations; output is researcher-facing evidence.
- Selection predicate: evaluation configuration, checkpoint ticks, held-out seeds and selected knockout artifact indices.
- Invalidation or expiry: fresh deep copies isolate evaluation trajectories from discovery state; validity is bounded by source state, disturbance schedule, horizon and surrogate physics.
- Activation or effect: frozen-agent simulated dynamics measure persistence and artifact contributions; this does not establish that a model improved or learned.
- Evidence limits: evaluator implementation is inspected, but no actual intact/knockout trajectories or paper data are supplied; causal findings from unexecuted comparisons cannot be asserted.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> assay_source = copy.deepcopy(simulation)
> --- `src/biofoundry/technology_ecology.py`

> knockout.artifacts.programs[source] = None
> --- `src/biofoundry/technology_ecology.py`

Mode: bounded counterfactual/held-out simulator evaluation. Software supplies the intact reference trajectory and disturbance conditions; no model judge or general expected scientific answer oracle is involved. Evaluation is not automatic successor selection: the inspected caller records results rather than choosing a replacement policy/program based on them.

### Claims

#### RT-CLM-grounded-science
Label: Grounded scientific work request

Claimed operation: homogeneous research agents should invent interacting material systems from local observations and bounded memory without inventing observations or unmeasured effects. This is model guidance, not a guarantee that hypotheses or claims are true. SRC-1, `src/biofoundry/policies/llm.py`.

> candidate mechanisms yourself. Do not invent observations or claim unmeasured effects.
> --- `src/biofoundry/policies/llm.py`

The simulation supplies authoritative action effects; the policy's request alone does not establish compliance, learning, or improvement.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-model-guidance
Label: Model input guidance

Consumer: configured model. Channel: system prompt, scenario instructions and user-context action manual, observations, prior research state and retrieved memory. Force: natural-language instruction/evidence interpreted by the model; delivery is wired, compliance and particular content dependence unobserved. Horizon: one decision message pair, with retained research state/memory eligible for later decisions. SRC-1, `src/biofoundry/policies/llm.py`; see [RT-RTE-model-planning](#rt-rte-model-planning) and [RT-OBJ-scenario-prompt](#rt-obj-scenario-prompt).

#### RT-BAP-action-dispatch
Label: Executable action authority

Consumer: simulator action dispatcher. Channel: typed queued/direct/recorded `AgentAction` values. Force: symbolic fixed-rule admission and execution; model prose cannot override treatment/resource/program checks merely by requesting it. Horizon: selected microtick and persistent world effects. SRC-1, `src/biofoundry/simulation.py`; see [RT-RTE-world-stepping](#rt-rte-world-stepping).

#### RT-BAP-program-execution
Label: Installed artifact behavior

Consumer: `ProgramVM` and artifact dynamics. Channel: installed symbolic instructions plus current sensor values. Force: bounded computation producing actuator outputs interpreted by simulator physics, not prompt advice. Horizon: repeated artifact ticks until replacement/retirement or episode end, with traces retaining content. SRC-1, `src/biofoundry/artifacts.py`, `src/biofoundry/programs.py`; see [RT-RTE-program-install](#rt-rte-program-install).

> outputs = self.vm.execute(program, sensors)
> --- `src/biofoundry/artifacts.py`

## Annotations

none
