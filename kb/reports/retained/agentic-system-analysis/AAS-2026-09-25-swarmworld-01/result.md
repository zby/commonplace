---
type: agentic-system-analysis-result
description: "Complete code-grounded analysis of SwarmWorld's simulator, model-policy, episode memory and experimental authority at a frozen source boundary."
run-id: AAS-2026-09-25-swarmworld-01
system: SwarmWorld
run-date: "2026-09-25"
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "SwarmWorld explicit within-episode private records, empirical knowledge, research-state and feedback derivatives, shared publications/messages, recipes and program/skill lineage, adaptive access metadata, queued plans, and files insofar as recorded model/action traces reconstruct these objects. Includes both disabled/default and enabled configuration branches, including optional turnover. Excludes provider internals, model weights, static scenario/configuration doctrine, presentation-only histories and external study datasets."
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values: [in-memory, files]
      records: [OBJ-9, OBJ-10, OBJ-11, OBJ-2, OBJ-12, OBJ-13, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-19, OBJ-7, OBJ-8, RTE-8]
      note: "Python objects retain live memory; JSONL/gzip files carry recorded model/action content into replay. Lineage edges do not imply a graph database."
    representational_form:
      assessment: known
      basis: wired
      values: [natural-language, symbolic]
      records: [OBJ-9, OBJ-10, OBJ-11, OBJ-2, OBJ-12, OBJ-13, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-19, OBJ-8]
      note: "Authored prose and readable summaries coexist with measured numeric records, counters, references, recipes and executable DSL instructions. No scoped parametric memory."
    lineage:
      assessment: known
      basis: wired
      values: [authored, trace-extracted, imported]
      records: [OBJ-9, OBJ-10, OBJ-11, OBJ-12, OBJ-13, OBJ-16, OBJ-17, OBJ-18, OBJ-8, RTE-2, RTE-8]
      note: "Models author hypotheses/plans/programs; simulator consequences feed derived records and ranking statistics; replay imports recorded research-state and actions. Internal peer transfer preserves existing lineage."
    behavioral_authority:
      assessment: known
      basis: wired
      values: [knowledge, instruction, enforcement, validation, ranking]
      records: [OBJ-9, OBJ-10, OBJ-11, OBJ-2, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-19, OBJ-8, RTE-5, RTE-6, RTE-7]
      note: "Memory advises the model; queued plans instruct action execution; installed DSL executes under VM enforcement; grounded resources and known parent records gate actions; retrieval/skill metadata ranks exposure. No claim of authoritative truth for prose."
    write_agency:
      assessment: known
      basis: wired
      values: [automatic]
      records: [RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-8]
      note: "Scoped writes are model-generated or simulator-generated. Calling step/replay from an external interface does not establish a manual memory editing workflow."
    curation_operations:
      assessment: known
      basis: wired
      values: [decay, evolve, promote, synthesize]
      records: [OBJ-9, OBJ-10, OBJ-11, OBJ-2, OBJ-16, OBJ-17, OBJ-18, OBJ-8, RTE-2, RTE-6, RTE-7]
      note: "FIFO forgetting and turnover remove private content; cell/skill/statistical entries update; verified measured skills gain ranking/inheritance eligibility; models synthesize research hypotheses from prior evidence. Exact-ID collision suppression and trace template compression are not near-duplicate memory deduplication."
    read_back_direction:
      assessment: known
      basis: wired
      values: [push, pull]
      records: [RTE-2, RTE-5, RTE-6, RTE-7, RTE-8]
      note: "Scheduled context assembly pushes selected evidence. Explicit action parent IDs drive requested record/program resolution; operator-invoked replay pulls recorded content through the named CLI consumer."
    read_back_signal:
      assessment: known
      basis: wired
      values: [coarse, identifier, inferred-lexical]
      records: [RTE-7, RTE-9]
      note: "Recency, locality, verified status and budgets are coarse selectors; extracted program IDs select focused skills and participant IDs select pending messages; token overlap selects private/archive evidence. Outcome bonuses are numeric ranking, not semantic judgment or embeddings."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-2, RTE-3, RTE-4, RTE-6, RTE-7, RTE-9]
      note: "Automatic writes retain trace-derived research summaries/hypotheses, action results with intent, measurement-linked reusable recipes/skills and adaptive ranking statistics for later model or selector consumption. This is a structural finding, not improvement evidence."
    trace_source:
      assessment: known
      basis: wired
      values: [event-streams]
      records: [RTE-2, RTE-3, RTE-4, RTE-6, RTE-7, RTE-9]
      note: "Qualifying live writes consume simulator action/measurement/observation and retrieval/citation events. Model requests receive derived portions of these events. Disk session transcripts are not the online learning input."
    learning_scope:
      assessment: known
      basis: wired
      values: [per-task]
      records: [RTE-1, RTE-2, RTE-6, RTE-9]
      note: "Task here is one configured discovery episode/mission; reset recreates all stores. Optional inheritance crosses agent generations inside that same episode, not independent episodes or projects."
    learning_timing:
      assessment: known
      basis: wired
      values: [online]
      records: [RTE-2, RTE-3, RTE-4, RTE-6, RTE-7, RTE-9]
      note: "Qualifying transformations run during decisions, actions, inspection and turnover. Offline replay restores prior writes without new policy calls, so is not a second demonstrated learning timing."
    distilled_form:
      assessment: known
      basis: wired
      values: [natural-language, symbolic]
      records: [OBJ-9, OBJ-10, OBJ-11, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-8, RTE-9]
      note: "Prose research/action summaries and symbolic outcome counts, measured recipe/skill evidence and ranking statistics cover the same trace-fed routes. Installed programs can also be model-authored from that context, without weight updates."
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-8]
      note: "No retained execution evidence was admitted. Citation-success counts and fixed-action contributor replays do not establish that a model depended on recalled content."
---

# SwarmWorld agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-swarmworld-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/swarmworld.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-swarmworld-01/memory-report.md`

**Memory analysis report SHA-256:** `2ab83fb3dc8102531224fb06ed9a29efb4c3e3b67ff5c0cbf7175b311ee1be9d`

Frozen specialist input SHA-256: `1ddda63318f04a3cd137fd88cd5a54a6a97b480b8dcae73cd6e2915d5d96d342`. Fresh specialist and coordinator used only primary sources in the declared boundary. This artifact names intended projections; the run state records publication.

## Boundary and evidence

Evidence basis: source code and current architecture doctrine in SwarmWorld at `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`, inspected 2026-09-25. No target execution, external study artifact or live provider request was admitted. Public name SwarmWorld; historical Python package `biofoundry`.

This is an enclosing runtime for bounded simulated research episodes, with a complete artifact, partial loop boundary. Included: deterministic world/material/artifact transitions, macroturn scheduling and model API/schema, private and social memory, executable programs and inheritance, CLI/server/PettingZoo entry paths, trace/replay and evaluation interfaces where they affect authority. The biological mechanism and declarative scenario interface are included; every scenario's physical validity is not.

Excluded: external model/provider internals (prevents hidden-reasoning or exact-weight-fixity claims); separately released 8.4GB dataset and paper experiments (prevents observed or causal learning claims); renderer internals (prevents UI completeness judgments); physical/material surrogate validity (prevents real-world scientific warrant); exhaustive atlas/figure and scenario-package coverage (prevents source-wide empirical or scenario equivalence claims). Python packages, provider service/network and credentials are external execution requirements. The purpose is an independent system characterization, not adoption advice or experimental reproduction.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/lamm-mit/SwarmWorld`; access root `/home/zby/llm/commonplace/related-systems/lamm-mit--SwarmWorld` | `6af7ae9fa36d98b07b0492cf139658e8af1f6eab` | Implementation: runtime and configuration; doctrine/design: README and current architecture. No observed run or causal experiment. | Full material paths and selected entry/evaluation ranges named on records; `src/biofoundry/` runtime, named profile, README/current architecture only | [Pinned simulator](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/simulation.py), [architecture](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/docs/ARCHITECTURE.md); local full-path anchors below | External service internals, study executions, all scenarios and physical validity uninspected |

Evidence reads used commit-addressed Git only. Worktree/HEAD and historical audits are not evidence. All source-dependent local anchors below resolve within SRC-1. A search miss is not used as a global absence.

## Shared records

### Components

CMP-1 — Authoritative BioFoundrySimulation, material/world/artifact arrays and ArtifactVM. Implementation conclusion status: wired. Symbolic Python/NumPy transitions own preconditions, numeric outcomes, measurements and persistent simulated artifacts. Sequential `step` is not a proven all-or-nothing transaction. Source: SRC-1 `src/biofoundry/simulation.py:298-770,1275-1320,1526-1587`; `src/biofoundry/programs.py:14-222`; `src/biofoundry/artifacts.py:25-64,173-260`.

CMP-2 — LLMPolicy scheduler/context/queue/schema. Implementation conclusion status: wired. Symbolic orchestration invokes a model with natural-language instructions, validates output and queues a bounded plan. Source: SRC-1 `src/biofoundry/policies/llm.py:236-598`; `src/biofoundry/structured_output.py:738-785`.

CMP-3 — OpenAI-compatible Responses wrapper and external distributed-parametric model. Interface conclusion status: wired. Model identity resolution conclusion status: wired: named profile uses `gpt-5.6-luna`, a provider identifier rather than immutable weights. Exact model fixity conclusion status: uninspected. Parameter changes during operation conclusion status: uninspected inside the provider; the local request path sends context/schema/sampling parameters, not a weight update. No inference about hidden formulation or criticism follows from this opacity. Source: SRC-1 `src/biofoundry/providers/openai_compatible.py:143-273`; `configs/openai-gpt-5.6-luna-technology-ecology-50.yaml:31-56`.

>             "store": False,
> --- `src/biofoundry/providers/openai_compatible.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

CMP-4 — AgentMemory, EmpiricalKnowledge, CulturalArchive, ResearchMission and ProgramLibrary. Implementation conclusion status: wired. In-memory symbolic collections hold natural-language evidence/claims, numeric records, identities and code. Lexical/numeric selectors do not introduce an embedding or parametric judge in the inspected retrieval route. Source: SRC-1 `src/biofoundry/memory.py:13-279`; `src/biofoundry/knowledge.py:18-236`; `src/biofoundry/program_library.py:53-295`.

CMP-5 — CLI/server/PettingZoo plus trace/replay/evaluation interfaces. Implementation conclusion status: wired. These invoke the simulation, record output or supply external policies; they do not replace scientific transition rules. Source: SRC-1 `src/biofoundry/cli.py:127-148,355-479,1490-1575`; `src/biofoundry/server.py:247-380`; `src/biofoundry/env.py:94-180`; `src/biofoundry/technology_ecology.py:273-370,435-503`.

### Operative objects

OBJ-1 — Superseded combined seed; retained evidence and original referent follow. Operative parts are OBJ-9, OBJ-10, OBJ-11.  Private `MemoryRecord` collections and action feedback. Implementation conclusion status: wired. SRC-1 `src/biofoundry/memory.py:13-233`, `src/biofoundry/simulation.py:1022-1063`, `src/biofoundry/policies/llm.py:342-598`. Python deques retain record ID, tick, kind, content, salience and causal-parent IDs. Working memory is clamped to 4–16 entries, episodic memory uses configured capacity, notebook uses at least 32. Under capacity 64, these are 16/64/64; notebook is bounded, not permanent. Records include observations, experiment results, prose action outcomes, messages, teachings, proposals and JSON research state. Action-feedback deques separately retain structured recent outcomes and optional intent. The model consumes these as evidence/self-guidance; existence checks do not verify prose content.

>         self.notebook: deque[MemoryRecord] = deque(maxlen=max(capacity, 32))
> --- `src/biofoundry/memory.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

OBJ-2 — `EmpiricalKnowledge` sparse local evidence. Implementation conclusion status: wired. SRC-1 `src/biofoundry/knowledge.py:18-236`, `src/biofoundry/simulation.py:1837-1862`. Cell-keyed records keep the latest local observation; extraction attempts/successes accumulate by resource. The rendered view aggregates observations and selects nearest remembered sites, with last-seen ticks/mass. It supplies grounded material evidence to the model and contributes to simulator recipe admissibility. Shared depot mass is deliberately excluded from the personal semantic evidence view. Missing entries mean unobserved, not nonexistent.

>         self.cells[y * self.width + x] = CellEvidence(
> --- `src/biofoundry/knowledge.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             "scope_note": "Unlisted materials are unobserved, not proven absent.",
> --- `src/biofoundry/knowledge.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

OBJ-3 — Superseded combined seed; retained evidence and original referent follow. Operative parts are OBJ-12, OBJ-13.  Public archive, spatial deposits, messages and request/fulfillment records. Implementation conclusion status: wired. SRC-1 `src/biofoundry/memory.py:236-279`, `src/biofoundry/simulation.py:510-560,770-885,1424-1500,1589-1642,1988-2008`. Archive contents append by unique ID. Spatial records include author/location and whether published. Communications retain sender, recipient and reply relations; taught records preserve original content/IDs, while free-message teaching can create a fresh authored record. Request fulfillment sends the original requester a durable receipt plus locally resolvable produced records. No semantic proof that the arbitrary successful action actually satisfies the request is implemented in the inspected fulfillment route.

>         """Attach a successful arbitrary action to an agent-selected request edge."""
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

OBJ-4 — Superseded combined seed; retained evidence and original referent follow. Operative parts are OBJ-14, OBJ-15.  Recipe/experiment memory. Implementation conclusion status: wired. SRC-1 `src/biofoundry/science.py:402-491`, `src/biofoundry/simulation.py:1170-1274,1365-1399,2240-2272`. ResearchMission retains proposed recipes, staged batches and test records; private views select records for the named agent. Pending batches reveal recipe/identity but not latent measured properties. TEST stores properties and material utility; pass/fail target labels are removed from model-facing records. With experience reuse enabled, measured results retain their input recipe, closing a concrete input–measurement–later-plan route. Without it, results retain recipe IDs but omit that direct recipe payload.

>         if self.config.experience_reuse:
>             # This is the agent-authored input that produced the measured coupon,
>             # not evaluator state. Retaining it closes the experience-reuse loop.
>             result["source_recipe"] = json.loads(json.dumps(batch.source_recipe))
> --- `src/biofoundry/science.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

OBJ-5 — Superseded combined seed; retained evidence and original referent follow. Operative parts are OBJ-16, OBJ-17, OBJ-18.  Executable programs, authored artifact claims and program skill records. Implementation conclusion status: wired. SRC-1 `src/biofoundry/programs.py:65-222`, `src/biofoundry/program_library.py:53-295`, `src/biofoundry/simulation.py:1064-1125,1643-1716`. DSL instruction content determines program identity; names, authors and claimed ancestry do not. Program entries retain authors/installations and explicit instruction diffs for forks. Per-agent skill indexes retain sources, up to 16 recent evidence IDs and eight recent measurements, lifetime counts and verification/inheritance status. Model-facing compact skill views retain instructions and a bounded evidence/measurement subset. Installed instructions operate through the VM; library possession only establishes knowledge and fork eligibility. Authored artifact purpose is not inferred to be physically realized.

>         payload = json.dumps(
>             [dict(item) for item in self.instructions],
> --- `src/biofoundry/programs.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

OBJ-6 — Superseded combined seed; retained evidence and original referent follow. Operative parts are OBJ-19, OBJ-20.  Queued AgentAction plans. Implementation conclusion status: wired. SRC-1 `src/biofoundry/policies/llm.py:236-341,489-552`. Validated output replaces the per-agent deque; later ticks pop one action. Queues are short-lived operational instructions, not evidence of useful learning by themselves. A configured transient-provider failure rolls back private-memory mutations from the entire scheduled planning batch and preserves action queues; failed/uncommitted model traces must not be counted as adopted research-state writes. Configuration/schema objects themselves are static control, outside the memory comparison.

>                 simulation.memories[index] = memory_snapshots[agent_id]
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

OBJ-7 — Recorded prompts, responses, actions, events and snapshots. Implementation conclusion status: wired. SRC-1 `src/biofoundry/events.py:39-154`, `src/biofoundry/counterfactuals.py:58-136`, `src/biofoundry/cli.py:1490-1575`, `src/biofoundry/simulation.py:2548-2570`. JSONL/gzip is losslessly read through template expansion. Replay reconstructs committed research-state writes before action execution. It does not rerun the LLM or establish provider continuation. Retrieval statistics/last-retrieval metadata are not included in the inspected authoritative-memory serialization or reconstructed by apply_recorded_model_trace; replay equivalence therefore must not be described as complete future LLM-policy equivalence.

OBJ-8 — Proposed access-metadata object: `retrieval_stats` and `last_retrieval`. Implementation conclusion status: wired. SRC-1 `src/biofoundry/memory.py:30-31,79-158,182-209`. These are numeric counters and diagnostics distinct from content records. Every retrieval increments selection counts even when experience attention is disabled. Model citations credit only IDs among the last selection; action outcomes credit previously tracked IDs. Enabled adaptive retrieval consumes these counts. Unlike content deques, the inspected dictionary has no per-entry eviction; turnover/reset replace it with the memory object. Diagnostics describe initial selection before possible prompt trimming, not necessarily delivery.

>         used = sorted(selected & cited_record_ids)
> --- `src/biofoundry/memory.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`


>         prior_state_record = simulation.memories[index].latest("research_state")
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>                 f"Prior self-authored research state: {prior_state}\n{tail}"
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>     A library entry grants knowledge of a program, never material access or a physics
>     advantage. ``verified`` means the agent obtained a measured artifact observation;
>     it is deliberately not an evaluator pass/fail label.
> --- `src/biofoundry/program_library.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             "progress": {
>                 "type": "string",
>                 "maxLength": 480,
>                 "description": "What the agent believes it has established so far.",
> --- `src/biofoundry/structured_output.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             feedback = 0.5 * citation_rate + 0.5 * (
>                 causal_success_rate if outcome_attempts else 0.0
>             )
> --- `src/biofoundry/memory.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             stats["outcome_attempts"] += 1
>             stats["successful_outcomes"] += int(success)
> --- `src/biofoundry/memory.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>     experience_attention: bool = False
> --- `src/biofoundry/config.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>   experience_attention: true
>   context_budget_characters: 60000
> --- `configs/openai-gpt-5.6-luna-technology-ecology-50.yaml` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`


OBJ-9 — Private MemoryRecord/deque content. Implementation conclusion status: wired. In-memory natural-language observations, outcomes, intent, proposals and received records have symbolic IDs/ticks/salience/parents. Source and evidence: see superseded OBJ-1, SRC-1 `src/biofoundry/memory.py:13-233`. Bounded FIFO and turnover give episode persistence; the notebook is not permanent.

OBJ-10 — Self-authored research state. Implementation conclusion status: wired for generation/storage/delivery; meaningful formulation conclusion status: afforded. JSON retains prose goal, hypothesis, progress, checkpoint and collaboration need, plus evidence IDs. Truth-apt hypothesis/progress and non-truth-apt intention fields remain distinct parts. Latest state is read as context and used in retrieval queries. Evidence-ID existence does not certify entailment. Source: SRC-1 `src/biofoundry/policies/llm.py:342-598`; `src/biofoundry/structured_output.py:1-160`; quotations retained in the combined operative-object records.

OBJ-11 — Structured action feedback/intent. Implementation conclusion status: wired. Simulator-generated numeric/event summaries and optional model message support later recent-outcome views. Intent is an authored explanation of purpose, not a causal diagnosis. Source: SRC-1 `src/biofoundry/simulation.py:1022-1063,2109-2210`.

OBJ-12 — Public CulturalArchive and spatial publications. Implementation conclusion status: wired. Authored prose and symbolic provenance persist in memory; location/recency/lexical selectors expose them later. Grounded resource mentions establish source/material provenance, not truth. Source: SRC-1 `src/biofoundry/memory.py:236-279`; `src/biofoundry/simulation.py:1170-1274,1589-1642`.

OBJ-13 — Messages, taught records and request/fulfillment receipts. Implementation conclusion status: wired. Prose plus symbolic sender/recipient/reply/record IDs is local or addressed. Copied teachings preserve content; free messages can originate claims. Attaching a successful arbitrary action to a chosen request is not semantic satisfaction proof. Source: SRC-1 `src/biofoundry/simulation.py:510-587,770-885,1424-1500`; quotation on OBJ-3.

OBJ-14 — Proposed recipes and pending microbatches. Implementation conclusion status: wired. Symbolic recipe inputs/processes and batch IDs represent an executable experiment choice. Pending views expose input and mass, not latent measured properties; no explicit truth proposition follows from a procedure alone. Source: SRC-1 `src/biofoundry/science.py:410-467`; `src/biofoundry/simulation.py:1170-1364`.

OBJ-15 — Simulator material and artifact measurements. Implementation conclusion status: wired. Numeric properties, utility/services and identities warrant within-simulator observations under the executed inputs. Experience reuse retains the source recipe. Agent views remove target pass/fail, observer records keep it. Source: SRC-1 `src/biofoundry/science.py:435-491`; `src/biofoundry/simulation.py:1064-1125,1365-1399`; quotation on OBJ-4.

OBJ-16 — Artifact specifications, split conceptually into prose claims and numeric geometry. Implementation conclusion status: wired for storage and geometry use. Claimed function/architecture/inspiration/predicted effects are authored natural-language candidates; clipped geometric parameters separately affect physics. Field presence does not test the claim. Source: SRC-1 `src/biofoundry/artifacts.py:25-64,231-260`; `src/biofoundry/simulation.py:1526-1587`. Further canonical parts OBJ-24 and OBJ-25 keep these unlike routes separate.

OBJ-17 — ArtifactProgram instructions and content identity. Implementation conclusion status: wired. Symbolic straight-line code executes under VM checks. Content hash excludes name/authorship/claimed parent; instruction diffs and known-parent constraints preserve lineage, not a reason why the program works. Source: SRC-1 `src/biofoundry/programs.py:14-222`; `src/biofoundry/simulation.py:1643-1716`; quotation on OBJ-5.

OBJ-18 — Skill evidence/index. Implementation conclusion status: wired. In-memory symbolic program sources, evidence IDs, measurement histories and verification/inheritance flags influence sorting and inheritance. Measurement presence sets verified without performance pass; ordinary view can contain unverified entries. Source: SRC-1 `src/biofoundry/program_library.py:53-295`; `src/biofoundry/simulation.py:1064-1125`; quotation on OBJ-8.

OBJ-19 — Queued AgentAction plans. Implementation conclusion status: wired. Symbolic per-agent deques replace the previous plan after committed planning, then pop once per tick or WAIT. Operational state alone is not a learned theory. Source: SRC-1 `src/biofoundry/policies/llm.py:245-340`.

OBJ-20 — Configuration/scenario capability/schema/prompt controls. Implementation conclusion status: wired. Shipped symbolic configuration and natural-language doctrine govern available actions, contexts and experiment settings; they are excluded from accumulated memory. Raw defaults disable LLM, science, experience attention and the optional skill/turnover mechanisms. The named technology-ecology profile enables model/science/attention/skill reuse but disables economy, so inheritance is not active there. Source: SRC-1 `src/biofoundry/config.py:40-196`; `configs/openai-gpt-5.6-luna-technology-ecology-50.yaml:1-99`; `src/biofoundry/policies/llm.py:1-157`.

OBJ-21 — Model/action trace payloads within OBJ-7. Implementation conclusion status: wired. Symbolic files containing authored prose support operator inspection and reconstruction of committed continuation state/actions. This is importing earlier writes, not a new online synthesis or provider continuation. Source: SRC-1 `src/biofoundry/events.py:39-154`; `src/biofoundry/counterfactuals.py:58-136`.

OBJ-22 — Snapshot/state digest within OBJ-7. Implementation conclusion status: wired. Symbolic serialization/digest checks certify only the represented state projection. Retrieval metadata omissions prevent full future-prompt equivalence. Source: SRC-1 `src/biofoundry/simulation.py:2548-2570`; `src/biofoundry/cli.py:1490-1575`.

OBJ-23 — Scorecard and frozen-artifact assay results within OBJ-7. Implementation conclusion status: wired. Numeric/boolean outcome records describe material, program, performance, novelty and provenance criteria. Artifact removal and held-out disturbance schedules concern fixed discovery states. Source: SRC-1 `src/biofoundry/science.py:530-680`; `src/biofoundry/technology_ecology.py:24-98,273-370,435-503`.

OBJ-24 — Prose artifact claims, the truth-apt part of OBJ-16. Implementation conclusion status: wired for authoring/retention. Claimed function and predicted effects are model claims about an artifact; physical success does not semantically check those words. Source: SRC-1 `src/biofoundry/artifacts.py:55-62`.

OBJ-25 — Numeric artifact geometry, the non-truth-apt part of OBJ-16. Implementation conclusion status: wired. Clipped numeric fields are behavioral parameters consumed in physical calculations, not inferred geometry truth. Source: SRC-1 `src/biofoundry/artifacts.py:29-54,231-260`.

OBJ-26 — Research hypothesis/progress claims, the truth-apt part of OBJ-10. Implementation conclusion status: afforded for substantive conjecture; wired for schema/storage/delivery. These fields can state explanations and alleged findings, but no candidate instance was admitted. Source: SRC-1 `src/biofoundry/policies/llm.py:342-598`.

OBJ-27 — Research goal/checkpoint/collaboration need, the policy part of OBJ-10. Implementation conclusion status: wired for generated self-guidance and later query/context use. Goals can shape future selection without constituting a truth proposition. Source: SRC-1 `src/biofoundry/policies/llm.py:342-598`.

### Routes

RTE-1 — Reset and episode horizon. Implementation conclusion status: wired. SRC-1 `src/biofoundry/simulation.py:63-117`, `src/biofoundry/env.py:131-180`. Reset creates a fresh archive, private/empirical stores, research mission and program library. Environment truncation uses configured max ticks. No cross-episode retained-learning import is established beyond replay of an existing episode.

>         self.program_library = ProgramLibrary(self.population.agent_ids)
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             if self.manual_actions:
>                 actions.update(self.manual_actions)
>                 self.manual_actions.clear()
> --- `src/biofoundry/server.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-2 — Model continuation write/read loop. Implementation conclusion status: wired. SRC-1 `src/biofoundry/policies/llm.py:342-598`. Scheduled planning obtains the newest research state, uses it plus local observation and pending requests to retrieve memories, assembles the request, validates output and stores a new notebook state. Evidence IDs are filtered to records actually retained, archive IDs or known programs. This validates references, not evidential entailment. The new state can carry goal, hypothesis, progress, next checkpoint and collaboration need. The next call reads these reasons/expectations as prose, with no explicit diagnosis algorithm or independent semantic audit.

>             research_state["evidence_ids"] = sorted(retained_evidence)
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>         transient_provider_failure = bool(scheduled) and any(
>             trace.get("error_kind") == "provider_transient"
>             for trace in traces.values()
>         )
>         self.provider_outage = bool(transient_provider_failure and freeze_on_outage)
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>     async def actions(
>         self,
>         simulation: BioFoundrySimulation,
>         show_progress: bool = True,
>     ) -> dict[str, AgentAction]:
>         await self.refresh_plans(simulation, show_progress=show_progress)
>         return self.next_actions(simulation)
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-3 — Action consequences to feedback. Implementation conclusion status: wired. SRC-1 `src/biofoundry/simulation.py:1022-1063,2109-2210`. Simulator outcome updates access statistics and feedback history, then emits a readable action-result memory including intent where supplied. Later semantic observations include recent action results and count/streak summaries. Failure may trigger replanning. This route preserves result detail and optional intention, not a guaranteed causal explanation of failure.

>                 f"{detail[:400]}{intent_suffix}"
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-4 — Observation/experiment to reusable evidence. Implementation conclusion status: wired. SRC-1 `src/biofoundry/simulation.py:1064-1125,1365-1399`, `src/biofoundry/science.py:431-491`, `src/biofoundry/knowledge.py:37-67,111-236`. Passive sensing replaces cell evidence and acquisition records extraction outcomes. INSPECT writes a notebook observation and measurement-backed skill evidence. TEST writes an experiment result; enabled source-recipe retention preserves how the measurement was produced. These records can inform future plans; no independent learning benefit is established.

>         if action.artifact == ArtifactType.NONE:
>             raise RecipeValidationError("BUILD requires a nonzero artifact type")
>         if self.research is not None and action.recipe is None:
>             raise RecipeValidationError(
>                 "BUILD requires an explicit tested recipe in collective-science mode"
>             )
>         if self.research is not None and action.artifact_spec is None:
>             raise RecipeValidationError(
>                 "BUILD requires an agent-authored artifact_spec in collective-science mode"
>             )
>         recipe = action.recipe or DEFAULT_RECIPES[action.artifact]
>         agent_id = self.population.agent_ids[index]
>         batch = self._execute_recipe_from_pool(index, recipe, action.causal_parents)
>         program = (
>             ArtifactProgram.from_dict(action.program, author=agent_id)
>             if action.program is not None
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>         for resource, mass in required.items():
>             personal = min(float(inventory[int(resource)]), mass)
>             inventory[int(resource)] -= np.float32(personal)
>             depot_amount = mass - personal
>             if depot_amount > 1e-7 and self.config.science.shared_depot:
>                 contributors.extend(self.research.consume_depot(resource, depot_amount))
>             elif depot_amount > 1e-7:
>                 raise RecipeValidationError("personal inventory is insufficient")
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-5 — Social record transfer and constrained combination. Implementation conclusion status: wired. SRC-1 `src/biofoundry/simulation.py:770-885,1170-1274,1424-1500,1589-1642`. Teach resolves explicitly cited private/archive records and known programs and copies them to nearby/addressed recipients. Publish adds authored content with structured grounding provenance; combined proposals require published records, structured provenance, enough distinct grounded authors and grounded recipe inputs. Provenance gates establish allowed evidence/material paths; they do not test truth of the publication's prose or whether a model derived its design from those words.

>             record = self.memories[index].get(parent) or self.archive.by_id.get(parent)
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-6 — Program observation, verification, transfer and optional inheritance. Implementation conclusion status: wired. SRC-1 `src/biofoundry/program_library.py:110-295`, `src/biofoundry/simulation.py:132-157,963-1021,1064-1125,1643-1716`. Local visibility records unverified program familiarity; measured nearby artifacts mark verified evidence; teach transfers the latest measurement and status. With turnover enabled, replacement clears private/empirical memory and feedback; enabled cultural inheritance selects strongest verified prior skills by measurement count, recency and ID, within a cap. This preserves code/evidence across replacement inside an episode, not weights or a complete personal notebook. Measurements record outcomes, while instruction diffs record edits; neither alone explains why the program works.

>             (entry for entry in existing.values() if entry["verified"]),
> --- `src/biofoundry/program_library.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             self.memories[index] = AgentMemory(self.config.population.memory_capacity)
>             self.empirical_knowledge[index] = EmpiricalKnowledge(self.world.width)
>             self.action_feedback[index].clear()
> --- `src/biofoundry/simulation.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

> 
> MAX_INSTRUCTIONS = 64
> MAX_REGISTERS = 16
> --- `src/biofoundry/programs.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             value = _operand(instruction.get("value", 0.0), registers, sensors)
>             if op == "set_open":
>                 outputs[op] = float(np.clip(value, 0.0, 1.0))
>             else:
>                 outputs[op] = outputs.get(op, 0.0) + float(
>                     np.clip(value, 0.0, MAX_ACTUATION_PER_TICK)
>                 )
>         return outputs
> --- `src/biofoundry/programs.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-7 — Context selection and access feedback. Implementation conclusion status: wired. SRC-1 `src/biofoundry/memory.py:45-209,245-279`, `src/biofoundry/policies/llm.py:193-233,363-478`, `src/biofoundry/simulation.py:1940-2008,2179-2221`. Private retrieval scans retained episodic+notebook content, tokenizes it, computes document-frequency weighting and scores the full candidate set; no vector index is wired. Archive retrieval similarly scans publications. Automatic skill focus extracts exact program IDs from research-state text, then favors matching and verified records. Locality/recency limit spatial evidence. Record excerpts bound delivered content without rewriting authoritative content. Context trimming drops selected memories first, then specified observation-list tails and whole optional fields; it can stop above the nominal budget when nothing removable remains. No hard token limit follows from the character target.

>                 str(entry["program_id"]) not in focus,
>                 not bool(entry["verified"]),
> --- `src/biofoundry/program_library.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>                 elif not _shrink_observation(observation_packet):
>                     break
> --- `src/biofoundry/policies/llm.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-8 — Observer files and deterministic reconstruction. Implementation conclusion status: wired. SRC-1 `src/biofoundry/events.py:64-154`, `src/biofoundry/counterfactuals.py:58-136`, `src/biofoundry/cli.py:1490-1575`. Named CLI replay reads recorded content, checks revision/configuration/scenario compatibility, reconstructs research state and replays actions before comparing state digests. Counterfactual replay removes agents by replacing their recorded actions with passive controls. Neither path replans after altered recall; this is not a recalled-content dependence test. Template deduplication is storage compression, not memory synthesis or learning. The report claims code wiring only.

>     if record.get("planning_committed") is False:
>         return
> --- `src/biofoundry/counterfactuals.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>             apply_recorded_model_trace(simulation, model_trace)
> --- `src/biofoundry/counterfactuals.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>     for source in sources:
>         knockout = copy.deepcopy(assay_source)
>         knockout.artifacts.retired[source] = True
>         knockout.artifacts.health[source] = np.float32(0.0)
>         knockout.artifacts.performance[source] = np.float32(0.0)
>         knockout.artifacts.services[source].fill(np.float32(0.0))
>         knockout.artifacts.programs[source] = None
>         result = _run_agent_free_assay(
>             knockout,
>             assay_horizon,
>             description=f"Knock out artifact {source}",
>             show_progress=False,
>         )
>         target_auc = np.asarray(result["artifact_auc"], dtype=np.float64)
>         system_effect = float(intact["resilience_auc"] - result["resilience_auc"])
> --- `src/biofoundry/technology_ecology.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

>         "evaluation_unit": "held-out disturbance schedule",
>         "discovery_state_frozen": True,
>         "agent_actions_per_schedule": 0,
>         "seeds": evaluator_seeds,
> --- `src/biofoundry/technology_ecology.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-9 — Proposed route for deterministic derived context over retained action/social/empirical state. Implementation conclusion status: wired. SRC-1 `src/biofoundry/simulation.py:795-823,1837-1862,2109-2221,2240-2272`, `src/biofoundry/science.py:794-864`, `src/biofoundry/knowledge.py:111-229`. The model receives aggregate action counts and streaks, closest remembered resource/station sites, public author profiles and pending requests selected by participant/fulfillment state. These are read-time derived views; persistent evidence/counters and receipt records support later reuse. The views themselves are not separately durable learning artifacts. Request fulfillment automatically retains a receipt/result subset for later caller-agent context. No additional model summarizes or judges these projections.


>             "passes_material_target": (
>                 self.material_utility(batch.batch) >= self.config.target_material_utility
>             ),
> --- `src/biofoundry/science.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

RTE-10 — Mission/evaluation measurement and disposition. Implementation conclusion status: wired. The operator invokes scorecard/assay consumers over the simulated state. TEST calculates utility and threshold status; scorecard declares functional outcome from a passing recipe, present authored-spec fields, non-system program history, peak performance and novelty. It can inspect provenance contributions separately. This evaluates concrete outcome criteria, not the truth of every hypothesis/claimed function. The scorecard reports to the operator; no automatic semantic claim acceptance or online promotion from this aggregate was established. Source: SRC-1 `src/biofoundry/science.py:469-491,530-680`; `src/biofoundry/technology_ecology.py:24-98,273-370,435-503`.

>                 and is_invented
>                 and is_programmed
>                 and has_performance
>                 and is_novel
>             )
>             built_from_test |= is_tested
>             causally_composed_artifact |= is_causally_composed
>             collaborative_build |= is_collaborative
> --- `src/biofoundry/science.py` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

The following extensions complete route ownership and admission details. They amend the existing records, not their referents. All route implementation conclusion statuses remain wired; observed activation and benefit remain uninspected because no candidate-linked execution was admitted.

| Route | Trigger, next owner and decision policy | Context, executor/effect, return and terminal output | Persistence, later read-back and delegated visibility | Selection, invalidation, recovery and admission limits |
|---|---|---|---|---|
| See RTE-1 | Operator selects config/seed/CLI policy; server loop or environment caller drives ticks. Reset creates stores. | Symbolic CLI policy factory chooses scripted/scalable/research-oracle/LLM. Server can overlay manually supplied actions; environment caller receives observations/rewards/termination/truncation. | Episode state lives in the simulation; recorders optionally write files. Provider sees only assembled request; external caller sees its configured observation. | Max ticks/end of episode/reset bound lifetime. Human configuration controls grants. Manual or external actions bypass LLM output schema but still reach simulator parsing/preconditions. Reset is fresh state, not cross-task memory import. |
| See RTE-2 | Scheduled macroturn or enabled event replan; LLMPolicy limits scheduled IDs by remaining call budget, dispatches parallel jobs and deterministically orders traces. | Prior state, current local evidence and selected memory guide external model; schema/coercion admits action/state fields; commit replaces queues and records state. Immediate return is success flag and traces, not completed physical work. | New state enters notebook and next query/prompt; plans persist until pop/replacement. Provider requests `store: false`; opaque server persistence is not established. | Any transient failure with freeze enabled restores scheduled agents' memory snapshots and preserves queues; CLI/server retry without world advance. Terminal/invalid output becomes WAIT. Direct `actions()` ignores the false flag and pops a queue, so it does not itself guarantee caller-level freeze. Call accounting distinguishes attempts from committed calls; no finite outage-retry cap was established in the CLI loop. |
| See RTE-3 | Each tick submits actions; simulator parses, checks available actions/resources/energy and selects within action budget. | Symbolic transitions resolve movement/actions, step world/artifacts, update feedback, then return events/rewards/artifact score. Failed actions can trigger early planning under enabled event scheduling. | Outcome/intent records, access counters, empirical state and artifacts affect later observations/plans. Peers see only communication or local/public observations. | Missing/invalid actions become WAIT; action exceptions become rejection events, not proof of rollback. BUILD consumes materials before later program/artifact checks, so earlier effects can survive a downstream rejection. Global state rollback is not supplied by the inspected catch path. |
| See RTE-4 | Agent proposes/combines recipe, OPERATEs, TESTs, BUILDs or INSPECTs; simulator/material lab owns admissibility and measurement. | Grounding/provenance checks gate proposals; inventory/process checks gate execution. TEST exposes latest untested personal batch; INSPECT measures nearby artifacts. Agent obtains numeric record and optional recipe association, observer obtains pass data. | Recipe IDs, batches, measurements and notebooks survive episode; later model views and skill observations consume them. Unmeasured latent properties stay outside private pending view. | Test criterion is simulator utility; no expected prose answer. BUILD's error text mentions tested recipe, but its inspected call path checks supplied recipe/spec and material availability without a prior TEST lookup. Invalid program after material consumption is not atomic rollback. New experiments or reset replace/extend state; old measurements remain historical. |
| See RTE-5 | Model chooses PUBLISH/DEPOSIT/COMMUNICATE/TEACH/COMBINE; simulator checks local/addressed recipients and identity/provenance constraints. | Source record resolution copies content; free messages/publications can author new claims. Combined proposals require multiple published records, structured grounding and configured distinct contributors/resources. Return is delivery/proposal event, not semantic truth judgment. | Private recipients, archive and spatial deposits enable later reads. Receipts connect successful actions to requests; publication IDs can guide plans and eligibility. | Communication/config/locality gates exposure. Publication grounding is resource-name mention tied to evidence, not a test of prose. Append-by-ID and FIFO are not semantic deduplication or withdrawal; no semantic rollback was established in these functions. |
| See RTE-6 | Model writes/forks/installs a program; observation/teaching and optional turnover update skill records. | Simulator validates known parent, changed content and ancestry; VM validates bounded DSL. Measurements mark verified, teaching preserves status, inheritance selects verified records by counts/recency. Returned events/history name installed program and lineage. | Installed code affects future artifact ticks; skills influence later context and fork eligibility; optional replacement inherits bounded skills while resetting notebook/empirical/feedback state. | No pre-install performance improvement gate. Replacement can install worse behavior; lineage preserves history without automatic rollback selection. Instruction-level bounds are not a universal aggregate actuation bound. Optional inheritance inactive when named profile economy is disabled. |
| See RTE-7 | Scheduled model assembly automatically selects retained experience; scoring consumes state/observation/query plus counts. | Lexical overlap/salience/feedback/exploration and program-ID focus select memory/skills; coarse locality/recency/limits apply. Model receives excerpts; diagnostics expose selected records. | Selected/cited/outcome counts persist and change future ranking when enabled. A cited record may be trimmed before delivery; actual content dependence is uninspected. | Named profile targets six private records, six archive records,1800 chars per memory and60000 total characters. Trimming can stop when no removable field remains; target is best effort, not hard token bound. FIFO/reset/turnover forget content; metadata does not necessarily evict with content. |
| See RTE-8 | Recorder writes events/model/actions/snapshots; operator requests replay/counterfactual/held-out assay. | Replay checks engine/scenario/config conditions, restores committed model states, executes recorded actions and compares serialized state digests. Agent removal replaces recorded actions; artifact knockout uses deep-copied discovery state and common future conditions. | Files preserve inspectable outputs. Read-back goes to replay/operator; no live model replanning in these counterfactual routes. State equality omits adaptive access metadata and cannot certify future prompts. | Engine mismatch can skip action replay while checking snapshot integrity; scenario hash mismatch rejects. A missing field is not restored by a digest. Held-out schedule evaluation freezes discovery state. No empirical effect is claimed without executions. |
| See RTE-9 | Observation assembly projects action/social/empirical stores; successful chosen reply generates receipt. | Deterministic summaries expose counts/streaks, nearest sites, author profiles and pending requests. Receipt stores result IDs; projection returns context immediately. | Durable source/counter/receipt state enables later view; rendered aggregate is usually ephemeral. Recipient identity selects the request subset. | No separate summarizing model or semantic fulfillment judge. Limits/locality/participant state choose records; underlying reset/eviction governs expiry. Receipt persistence qualifies as trace-fed context; pure rendering does not. |
| See RTE-10 | TEST/scorecard/operator assay runs configured numeric criteria. | Material threshold creates pass flag; functional scorecard joins measured input/output and field-presence/program/novelty criteria. Returns operator-facing outcome records. | Measurements/scorecards persist in research state or output files; online private measurement excludes target label. Assay outputs inform human analysis; automated online semantic promotion is uninspected. | Configured thresholds are evaluator definitions, not ground-truth explanations. Optional artifact removal/held-out schedules isolate physical artifact behavior under simulator assumptions, not recalled-content dependence or truth of prose. |

Material revision admission is concentrated in RTE-2 (state/plan replacement), RTE-4 (experiment/product construction), RTE-5 (public/social knowledge admission), RTE-6 (executable behavior/skill inheritance) and RTE-7/RTE-9 (access metadata and receipts). Proposals come from the model or deterministic consequence processing; the simulator owns formal/material rejection and the operator chooses static configuration. There is no universal human semantic acceptance stage on these paths. Guidance is the shipped action manual, current local evidence, prior state and retained measurements; each remains either doctrine, input/outcome record, or authored theory candidate. Program/recipe syntax is individually inspectable and editable; code history can preserve changed instructions without preserving an argument for the change. Natural-language rationale may persist in hypothesis, progress, intent or predicted effects, and later context reads it. No route-level claim that criticism occurred follows from its possible storage.

For theory-bearing guidance in OBJ-26, OBJ-12, OBJ-13 and OBJ-24: formulation conclusion status: afforded; delivery/retention conclusion status: wired; operative application of its stated content conclusion status: uninspected; content-directed criticism conclusion status: uninspected; criticism-linked revision or changed reliance conclusion status: uninspected; improved capacity attributable to that process conclusion status: uninspected. The source provides model calls and measurements through which these can happen; opaque model processing and missing candidate traces prevent asserting the links. A program or recipe update is not by itself a formulated explanatory theory or criticism of one. This distinction does not imply that unobserved reasoning is absent.

### Claims

CLM-1 — README characterizes SwarmWorld as a deterministic research environment where agent societies discover, test, exchange, inherit and embody technologies. Claim conclusion status: claimed. Source: SRC-1 `README.md:1-30`. RTE-2, RTE-4, RTE-5 and RTE-6 implement operations fitting that purpose; the commissioned evidence supplies no measured discovery improvement.

> SwarmWorld is a deterministic research environment for studying how societies of
> language-model agents discover, test, exchange, inherit, and physically embody
> technologies in a shared world. Agents perceive locally, act through a bounded action
> contract, and leave persistent artifacts whose material effects and executable
> programs continue on later simulation ticks.
> --- `README.md` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

CLM-2 — Architecture claims a simulator authority boundary, action replay and separation of evidence, authored claims and physical outcomes. Claim conclusion status: claimed. Source: SRC-1 `docs/ARCHITECTURE.md:6-52,66-81,86-109`. The inspected interfaces support bounded authority; tick atomicity, per-tick actuation wording and future-policy equivalence require the limits stated on RTE-3, RTE-6 and RTE-8.

> `BioFoundrySimulation` is the only component allowed to mutate scientific state.
> PettingZoo, policies, model servers, FastAPI, and Godot submit actions or consume
> state; none defines physical outcomes.
> --- `docs/ARCHITECTURE.md` @ `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`

### Evidenced absences

None established as source-wide ABS records. Missing candidate executions, hidden provider reasoning and untested faithfulness are limitations. Specific call-path limits are positive descriptions of inspected code, not claims that no other branch or external study exists.

### Behavioral-authority paths

BAP-1 — Consumer: external policy model. Channel: system/manual plus observation, selected memory and prior research-state user input. Force: instructional for shipped doctrine, advisory/evidential for memories and self-guidance. Horizon: one request, renewed by episode retention. Delivery is wired; content activation is uninspected. Source: SRC-1 `src/biofoundry/policies/llm.py:342-598`.

BAP-2 — Consumer: simulator and ArtifactVM. Channel: AgentAction, recipe, geometry, installed DSL and configuration. Force: schema/precondition validation and deterministic execution/enforcement. Horizon: an action, queued plan, or installed artifact lifetime. This operational authority does not accept an accompanying explanation. Source: SRC-1 `src/biofoundry/simulation.py:298-770,1275-1399,1526-1716`; `src/biofoundry/programs.py:65-222`.

BAP-3 — Consumer: agents/selector/fork resolver. Channel: taught/published records, skill evidence, grounding/parent IDs and access metadata. Force: advisory for model evidence, ranking for context, permissive/enforcing for combined-proposal/fork/inheritance eligibility. Horizon: retained episode state until reset/eviction/turnover. Source: SRC-1 `src/biofoundry/simulation.py:1170-1274,1424-1500,1643-1716`; `src/biofoundry/program_library.py:110-295`; `src/biofoundry/memory.py:79-209`.

BAP-4 — Consumer: operator/replay checker. Channel: traces, digests, scorecards and artifact evaluation results. Force: replay consistency rejection and scoped numeric outcome reporting, not semantic acceptance of model prose. Horizon: recorded episode/evaluation projection. Source: SRC-1 `src/biofoundry/cli.py:1490-1575`; `src/biofoundry/technology_ecology.py:273-370,435-503`.

## Runtime account

The ordinary model episode starts when an operator chooses a seed and configuration, requests LLM policy and supplies provider credentials. The CLI creates simulation/policy and records configuration/engine identity. Agent identities are population slots, not independent service principals. A macroturn scheduler selects active agents by interval/phase and, when configured, event-driven replanning. The policy reads each agent's own observation and retained state, automatically retrieves a bounded subset, calls the external provider with schema and action manual, and validates returned state/actions. Parallel calls finish in arbitrary order but traces are ordered by agent ID before commit. One queued action per agent executes each world tick. The simulator returns consequences; notebook/feedback/measurements then shape the next explicit context. Max ticks or action/call budgets bound the episode's operation; recorder outputs and scorecards are the operator's terminal artifacts. Sources: SRC-1 `src/biofoundry/cli.py:355-479`; `src/biofoundry/policies/llm.py:245-598`; `src/biofoundry/simulation.py:274-410,624-770`.

Alternate interfaces matter to guarantees. CLI scripted/scalable/research-oracle modes bypass model generation. The inspected factory establishes selectable policy routes, but internal oracle-policy privileged knowledge was not inspected; its name is not evidence of an expected-answer oracle. PettingZoo supplies decoded external actions and returns observations, rewards and termination/truncation; its caller's learning loop is external. Server manual actions overwrite planned actions before `step`. Thus LLM output schema is a model-interface gate, while simulator preconditions are the shared action boundary. No broad host sandbox is inferred: the source-installed Python runtime and operator control plane are trusted. Artifact programs use a restricted DSL, not unrestricted Python/shell. Sources: SRC-1 `src/biofoundry/cli.py:127-148`; `src/biofoundry/env.py:94-180`; `src/biofoundry/server.py:247-341`; `src/biofoundry/programs.py:14-222`.

The capability surface includes experiment, communication, teaching and program modification verbs; the current grant set depends on configuration and scenario capabilities. Named profile settings enable many science/memory features but disable economy, so mortality/inheritance is only a source-supported alternative. The deployment isolation envelope beyond simulator/VM checks is uninspected. Model responses are proposals, physical calculations are simulator-owned, and public prose is not interpreted as an executable physics amendment.

Four static forcing cases distinguish the boundaries:

1. **Transient model failure:** `refresh_plans` freezes on any scheduled transient provider failure with the option enabled, despite its docstring saying total outage. It restores private memory and preserves queues. CLI/server honor the false return and retry without stepping; the convenience `actions()` wrapper still consumes an action. Freeze is an entry-loop protocol, not a universal invariant across callers. Required external contract: the provider's retryability classification and eventual service recovery. Sources: SRC-1 `src/biofoundry/policies/llm.py:245-340`; `src/biofoundry/cli.py:393-453`; `src/biofoundry/server.py:283-317`.
2. **Untested or invalid construction:** `_build` requires a supplied recipe/spec in science mode, executes the recipe, then parses the program/adds the artifact. The inspected helper checks material availability, not prior TEST membership. The mission later computes tested-design success separately. Materials can be consumed before a subsequent validation failure; rejection does not prove atomic rollback. This is a call-path account, not a claim that every build succeeds or lacks all validation. Sources: SRC-1 `src/biofoundry/simulation.py:1275-1320,1526-1587`; `src/biofoundry/science.py:530-620`.
3. **Bad but measured skill:** INSPECT supplies a measurement and sets verified independently of threshold. Ordinary skill view ranks verified first but does not exclude unverified; inheritance does exclude unverified, then orders by measurement count/recency. Therefore verification is evidence presence and selection authority, not successful operation. Fork installation checks parent identity/content difference, not improvement. Sources: SRC-1 `src/biofoundry/simulation.py:1064-1125,1643-1716`; `src/biofoundry/program_library.py:110-295`.
4. **Replay or stronger actuation claim:** replay can recover committed research state/actions and serialized physical state, but not adaptive selector statistics omitted by the serializer/restorer. Matching digests do not entail equal later prompts. Separately, VM bounds instructions/registers and clips each actuator contribution, while repeated contributions accumulate; its per-instruction cap does not imply the same cap for an aggregated output. Further physical constraints remain in artifact/world calculations. Sources: SRC-1 `src/biofoundry/counterfactuals.py:58-136`; `src/biofoundry/simulation.py:2548-2570`; `src/biofoundry/programs.py:14-16,141-222`; `src/biofoundry/artifacts.py:173-260`.

No dynamic check planned. Provider outage, construction precondition, inheritance filtering and replay-statistics checks were considered; the selected claims are bounded call-path and dataflow conclusions visible in code, so no provider expense or scientific reproduction was warranted. No test was attempted or counted as an observed execution. Scientific usefulness, causal recall and simulator accuracy require different evidence.

Diagnosis is model-proposed from feedback when it occurs; formal rejection is simulator-owned. Candidate comparison is optional model deliberation plus configured outcome calculations, not a separately guaranteed critic. The operator chooses task, thresholds and treatment; a model can replace its plan/state or installed behavior within allowed actions, and the simulator can veto inadmissible syntax/material/identity conditions. No candidate-linked content-directed criticism was observed. In the ordinary LLM route, measurements supply outcomes rather than expected prose answers. The material pass threshold and outcome scorecard are code/configuration-defined references supplied by the experiment designer; they govern stated measurement criteria. They are not answers validating an explanation. Internal privileged inputs of the separately selectable research-oracle policy remain uninspected and are excluded from the ordinary model-episode conclusion.

## Lens scoping

### Memory/context scope

Depth: full. Trigger evidence: OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-7 and RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8 and RTE-9. Inspected scope: private memory/research state/feedback, empirical knowledge, public/local/social records, experimental input/outcome records, program lineage and skills, adaptive access metadata and reconstructive trace read-back. Canonical parts OBJ-8, OBJ-9, OBJ-10, OBJ-11, OBJ-12, OBJ-13, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-19, OBJ-21, OBJ-22 and OBJ-23 preserve differences. Static OBJ-20, provider weights, presentation-only outputs and external studies are excluded. Explicit memory is central to repeated macroturns, so a brief lens would miss material behavior. Both raw/default and named/enabled branches are covered.

### Epistemic scope

Depth: full. Trigger evidence: CLM-1, CLM-2; authored OBJ-26, OBJ-12, OBJ-13 and OBJ-24; measured OBJ-2, OBJ-15, OBJ-23; checking/admission on RTE-2, RTE-4, RTE-5, RTE-6 and RTE-10. The invoked standalone epistemic procedure is applied locally as a sparse overlay on these records. The question is which claims become measured, accepted or merely usable, and what each check permits. Assessed: model hypothesis/spec/publication generation, empirical acquisition, experiment measurements, formal/provenance admission, skill selection, traces/replay and scoped outcome evaluation. Unassessed: model-internal reasoning, study executions, every surrogate equation/scenario and full research-oracle policy. Those exclusions prevent a general theory-builder or real-world knowledge-production conclusion.

## Lens outputs

### Memory/context lens

The fresh specialist's complete report is integrated, with source evidence retained above. Explicit memory is supplied anew to the stateless request interface. Episode-lived stores include bounded personal records, accumulating public/program records and access metadata. Research-state goals/hypotheses contribute to the next query and prompt. That is wired continuity and self-guidance, not evidence that a useful theory changed a choice. The named profile's experience attention differs from unadapted defaults; optional turnover crosses agent generations inside an episode, not independent tasks.

Automatic trace-fed writes comprise RTE-2 research continuation, RTE-3 outcome/intent and access feedback, RTE-4 measurement/input association, RTE-6 measured skill records, RTE-7 adaptive counters and RTE-9 receipts. These routes feed later context, ranking or admissibility, supporting `trace_learning: yes` at wired strength. Source is event-streams, timing online, scope per-task (the configured episode), and outputs natural-language plus symbolic. Weight changes, raw JSONL recording and pure read-time rendering are not additional learning routes. Stored hypotheses can synthesize claims; curation also evolves entries, promotes measured skills and forgets via FIFO/reset. Exact-ID collision checks, lossless compression and substring grounding do not establish semantic deduplication, consolidation or invalidation.

At a scheduled macroturn, private/archive selection pushes lexical and coarse-selected content; exact program IDs in prior state focus skill views, and participant identities choose requests. TEACH and FORK_PROGRAM explicitly request retained IDs; operator replay requests recorded content. Those are pull operations distinct from later automatic context push. Read-time aggregates expose retained evidence but do not themselves become separate durable theories. Context trimming can exceed its nominal character target; selection diagnostics can include records omitted from delivered context. Citation and successful cited outcomes change counters without proving content activation. Faithfulness remains not-determinable: no recalled-content intervention with replanning and retained outcomes was admitted. Fixed-action contributor replay and artifact knockout ask different causal questions.

### Epistemic lens

#### 1. Source-and-claim boundary

System/revision and evidence boundary: see SRC-1 and Boundary and evidence. Question and assessed/unassessed route families: see Epistemic scope. Consequential knowledge/authority claims: CLM-1 and CLM-2, doctrine/design only as claims. Implementation supports the following routes; no candidate-linked trace or execution supplies an observed phase. Provider opacity prevents judging internal inference; missing experiment artifacts prevent measured benefit; excluded surrogate validation prevents external scientific warrant.

#### 2. Epistemic-object inventory

Generic identity, producer/consumer, form, storage and anchors remain on the canonical records. This overlay names only truth-apt parts and their limits.

| Object/part | Candidate content and transformation | Warrant boundary |
|---|---|---|
| OBJ-26 | Hypothesis/progress can state ampliative explanations and alleged findings; exact generated content unobserved | A schema and delivery route do not certify implication or criticism |
| OBJ-27 | Goal/checkpoint/collaboration intention; non-truth-apt policy content | Can steer query/context without a discovery claim |
| OBJ-12 | Publications may copy evidence or conjecture mechanisms; transformation indeterminate without instances | Grounding supplies resource/source provenance, not prose entailment |
| OBJ-13 | Taught source content is copied; free messages may originate claims; receipts assert action/request links | Copied lineage preserved within retained text; semantic satisfaction unknown |
| OBJ-24 | Claimed function/predicted effects can be ampliative propositions about artifact behavior | Field presence is not measurement of these words |
| OBJ-25 | Clipped geometry settings; non-truth-apt design parameters | Operational influence does not establish an explanation |
| OBJ-14, OBJ-17, OBJ-19 | Experiment recipe, executable program and action plan; no necessary truth proposition | Formal validity or selection licenses execution only |
| OBJ-2, OBJ-15 | Sensor/extraction/test evidence; acquisition and deterministic measurement projection | Domain is the configured simulator and executed input; not real materials |
| OBJ-9, OBJ-11 | Readable outcome summaries and retained intent; non-ampliative rendering for simulator outcomes, authored intention otherwise | Abbreviation preserves a selected outcome subset, not all causal explanation |
| OBJ-18 | Program familiarity/measurement status and history | Verified means measured evidence, not evaluator pass |
| OBJ-8 | Numeric access/citation/success statistics | Direct selector adaptation; not truth-apt criticism |
| OBJ-21, OBJ-22 | Recorded model/action content and state identity checks | Records establish intended replay data, not observed truthful claims or full policy state |
| OBJ-23 | Calculated threshold/scorecard/assay outcomes | Scoped numeric outcome derivation, not acceptance of generating theory |
| OBJ-20 | Shipped doctrine/configuration | Defines task/check domains; no runtime conjecture instance |

Superseded aggregate OBJ-1, OBJ-3, OBJ-4, OBJ-5 and OBJ-6 are disposed through their parts. OBJ-7, OBJ-10 and OBJ-16 remain explicit containers with unlike part dispositions rather than one epistemic label.

#### 3. Authority-route ledger

Every row's architectural status is separate from candidate observation. `implemented` below means inspected wiring only. All effects are possible implemented results, not reported executions. Behavioral-authority paths supply consumer/channel/force/horizon; canonical records carry anchors and complete progression.

| Route/function | Architectural status | Target and content/update relation | Evaluator/condition, activation and result | Epistemic license | Operational/behavioral force | Claim and gap |
|---|---|---|---|---|---|---|
| RTE-2 / content transformation | implemented | OBJ-26, OBJ-27; possible ampliative conjecture and policy update from explicit context | Scheduled provider output creates state/plan; model reasoning uninspected | Candidate generation only | BAP-1 self-guidance; BAP-2 queue proposal | CLM-1; no instance or known entailment |
| RTE-2 / check/evidence production | implemented | OBJ-10, OBJ-19; no content change apart from coercion/reference filtering | Local schema and retained-ID checks yield valid output/WAIT | Structural conformity and existing references | BAP-2 blocks invalid output | CLM-2; no semantic support check |
| RTE-2 / retention | implemented | OBJ-10, OBJ-19; no content change after admission | Committed planning stores state/replaces queue; outage can rollback memory | No additional warrant | BAP-1 later context; BAP-2 actions | CLM-1; storage is not acceptance |
| RTE-3 / content transformation | implemented | OBJ-11 and OBJ-9; non-ampliative reshaping of outcome plus retained authored intent | Deterministic action-result formatter after each action | Outcome subset under simulator semantics | BAP-1 later evidence, replanning and BAP-3 counts | CLM-2; no guaranteed explanation |
| RTE-4 / check/evidence production | implemented | OBJ-2, OBJ-15; truth-apt transformation: acquisition/import | Local sensing, TEST and INSPECT produce measurements | Configured simulator-domain outcome | BAP-1 evidence; BAP-3 measured skill status | CLM-1; external validity uninspected |
| RTE-4 / operational admission/selection/consumption | implemented | OBJ-14, OBJ-25; non-truth-apt design update | Grounding/inventory/process checks admit proposal/execution/build | Allowed input/provenance, not prior experimental success | BAP-2 constructs product; can reject | CLM-2; BUILD does not enforce prior TEST on inspected path |
| RTE-5 / content transformation | implemented | OBJ-12, OBJ-13; copied content non-ampliative, new prose indeterminate | Agent supplies text/IDs; teaching copies or creates content | Preserved source text or authored claim, not new truth | BAP-3 later peer context | CLM-1; semantic content unobserved |
| RTE-5 / operational admission/selection/consumption | implemented | OBJ-12, OBJ-13, OBJ-14; no content change | Locality/recipient IDs, published grounding and contributor constraints | Identity/material provenance only | BAP-3 transfer/proposal eligibility | CLM-2; no proof of derivation or request satisfaction |
| RTE-5 / retention | implemented | OBJ-12, OBJ-13; no content change | Archive append, personal storage, receipt persistence | No added epistemic license | BAP-3 later recall | CLM-1; not post-acceptance integration |
| RTE-6 / check/evidence production | implemented | OBJ-17; no content change | Syntax/register/instruction/parent/difference checks before install | DSL validity and lineage admissibility | BAP-2 permits/rejects executable update | CLM-2; not improvement |
| RTE-6 / disposition/acceptance | implemented | OBJ-18; no content change to program, evidence-presence status update | Measured observation marks verified | Reliance licensed only as a measured-known skill, not true explanatory claim | BAP-3 ranking/inheritance eligibility | CLM-1; no quality threshold |
| RTE-6 / operational admission/selection/consumption | implemented | OBJ-17, OBJ-18; non-truth-apt behavior update | Install code; optional turnover selects verified bounded records | Operationally valid known code/evidence | BAP-2 future VM; BAP-3 recipient context/parent knowledge | CLM-1; can inherit poor performers |
| RTE-7 / behavior/policy adaptation | implemented | OBJ-8; non-truth-apt numeric ranking update | Selection/citation/success counts enter lexical/feedback/exploration score | No truth judgment | BAP-3 ranking; BAP-1 changed exposure | None; actual model content dependence uninspected |
| RTE-7 / operational admission/selection/consumption | implemented | OBJ-9, OBJ-10, OBJ-12, OBJ-18; no content change except excerpts | Scheduled automatic selection and best-effort trimming | No new warrant from retrieval | BAP-1 delivered evidence | None; selected versus delivered distinction |
| RTE-9 / content transformation | implemented | OBJ-2, OBJ-11, OBJ-13; non-ampliative reshaping | Deterministic aggregate/participant views and receipts | Preserves selected record facts, not semantic fulfillment | BAP-1/BAP-3 context | None; rendered summary not separately durable |
| RTE-8 / lineage/freshness/recovery | implemented | OBJ-21, OBJ-22; acquisition/import and no content change | Compatible replay restores states/actions, checks projection digest | Consistency of represented state only | BAP-4 reject/report | CLM-2; adaptive statistics not reconstructed |
| RTE-10 / check/evidence production | implemented | OBJ-23; entailed derivation in configured numeric domain | Thresholds/field presence/physical outcome rules compute criteria | Defined outcome fits, not theory truth | BAP-4 observer result | CLM-1; measurements unexecuted here |
| RTE-10 / disposition/acceptance | implemented | OBJ-23; no content change | Functional outcome flag accepts composite artifact outcome against stated thresholds | Accepted scope would be this simulator outcome criterion | BAP-4 reporting, not model-prose promotion | CLM-1; no observed candidate acceptance |
| RTE-8 / check/evidence production | implemented | OBJ-23; entailed numeric comparison | Frozen-state artifact knockout/shared future, or held-out schedule evaluation | Artifact behavior under simulator intervention design | BAP-4 comparison output | CLM-1; no execution or recall intervention |
| RTE-2 / lifecycle integration | not determinable | OBJ-26; no established post-acceptance transition | No candidate-linked semantic acceptance/reliance chain inspected | No accepted-theory claim | Possible BAP-1 ordinary context use is separately wired | CLM-1; retention cannot fill missing acceptance |
| RTE-5 / lifecycle integration | not determinable | OBJ-12, OBJ-13; no established post-acceptance transition | Provenance-gated publication/transfer does not supply semantic acceptance | No accepted-publication claim | BAP-3 pre-acceptance use remains wired | CLM-1; candidate content absent |
| RTE-6 / lifecycle integration | not determinable | OBJ-24; no semantic acceptance-to-use transition | Measurements concern physical outputs, not explicit claim semantics | No accepted-explanation claim | BAP-2 code use is separately wired | CLM-1; successful artifact and true explanation differ |

#### 4. Per-object lifecycle disposition

For potential ampliative hypothesis OBJ-26: transformation is ampliative conjecture when the field states a non-entailed explanation; no instance observed. Observation/anomaly: RTE-3 and RTE-4, architectural status implemented, observed candidate state no instance observed. Conjecture: RTE-2, architectural status implemented for generation interface, observed candidate state no instance observed. Derived consequence: model-mediated RTE-2, architectural status not determinable, observed candidate state no instance observed. Test/evidence: RTE-4 is implemented for measurements, but candidate-specific test mapping is not determinable; observed candidate state no instance observed. Acceptance: RTE-2, evaluator/criterion for truth of the particular claim uninspected, intended use guidance, architectural status not determinable, observed candidate state no instance observed, accepted scope unestablished. Lifecycle integration: RTE-2 post-acceptance change unestablished, architectural status not determinable, observed candidate state no instance observed. The wired notebook route is retention, not evidence of an accepted theory.

For potential ampliative artifact-function claim OBJ-24: transformation is ampliative conjecture for an unentailed predicted function; no instance observed. Observation/anomaly: RTE-4, architectural status implemented, observed candidate state no instance observed. Conjecture: RTE-2, architectural status implemented for supplied spec, observed candidate state no instance observed. Derived consequence: predicted-effects field affords formulation but no explicit entailment check was inspected, architectural status not determinable, observed candidate state no instance observed. Test/evidence: RTE-4 and RTE-10 measurements implemented, claim-semantic mapping not determinable, observed candidate state no instance observed. Acceptance: RTE-10 accepts configured physical criteria rather than these words; claim evaluator/criterion/accepted scope unestablished, architectural status not determinable, observed candidate state no instance observed. Lifecycle integration: RTE-6 installs code before a semantic acceptance route is established; architectural status not determinable for post-acceptance integration, observed candidate state no instance observed. Retained code/claim coexistence does not close this lifecycle.

OBJ-12 and the free-message portion of OBJ-13: transformation indeterminate. Copying measured content, summarizing it, deriving consequences and making new conjectures remain possible. RTE-5 preserves record provenance and supplies retention/use, while grounding does not decide entailment. Exact candidate text with its inputs and later checks would distinguish these transformations; no instance observed. The copied-teaching portion of OBJ-13 is non-ampliative acquisition/copy through RTE-5; discovery lifecycle not applicable, source warrant no stronger than original content. Request receipts are non-ampliative records of selected action/request links through RTE-9; they do not certify satisfaction.

OBJ-2 and OBJ-15: acquisition/import from simulator sensors/measurements through RTE-4; discovery lifecycle not applicable. Their warrant is domain-limited measured state, with real-world validity excluded. OBJ-9 and OBJ-11 outcome portions: non-ampliative reshaping through RTE-3/RTE-9; discovery lifecycle not applicable; selected abbreviated details do not carry omitted causal explanation. Authored intentions remain policy content. OBJ-18 verification facts: non-ampliative measurement-status update through RTE-6, discovery lifecycle not applicable; no semantic or performance pass follows. OBJ-21 and OBJ-22: acquisition/copy and identity checks through RTE-8, discovery lifecycle not applicable; replay does not newly warrant recorded prose. OBJ-23: numeric derivation through RTE-10/RTE-8, discovery lifecycle not applicable for the arithmetic outputs; validity stays within supplied simulator state and configured criteria, with no observed outcome instance admitted.

No lifecycle record for OBJ-8: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-7.

No lifecycle record for OBJ-14: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-4.

No lifecycle record for OBJ-17: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-6.

No lifecycle record for OBJ-19: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-2, RTE-3.

No lifecycle record for OBJ-20: no runtime candidate truth-apt output for this static control object; relevant direct-adaptation or update routes: RTE-1.

No lifecycle record for OBJ-25: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-4.

No lifecycle record for OBJ-27: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-2, RTE-7.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design support | Implementation | Observed support | Causal support | Supported conclusion and mismatch/unknown |
|---|---|---|---|---|---|
| CLM-1 | README/current architecture describe discovery, evidence exchange and executable inheritance | RTE-2, RTE-4, RTE-5, RTE-6, RTE-8, RTE-10 | None admitted | None admitted; intervention code is not an executed comparison | Operations to generate, measure, exchange and inherit are wired. Useful discovery, criticism-driven improvement and recalled-content dependence are unresolved. |
| CLM-2 | Simulator authority, deterministic tick/replay and separate evidence/prose | RTE-2, RTE-3, RTE-4, RTE-6, RTE-8 | None admitted | None admitted | Numeric/action authority is bounded and wired; entry-path freeze differs, sequential rejection need not rollback, verified is measurement presence, replay omits selector metadata and VM accumulation differs from a simple total actuation cap. |

#### 6. Bounded conclusion

The runtime acquires local simulated evidence, retains authored hypotheses and plans, measures recipes/artifacts, checks formal/material/provenance constraints and uses code/records operationally. Numeric checks warrant their configured simulator outcomes. They do not generally accept the truth of research-state prose, publication explanations or predicted-function wording. Skill status changes later selection with a specifically limited license: measured and known. Adaptive recall statistics and plan/program replacement can change behavior without a truth-apt acceptance transition. Experimental improvement and content-directed criticism remain uninspected at this evidence boundary; these limits are not a claim that model reasoning lacks them.

## Reconciliation

The specialist report's run, source, full revision, complete status, frozen input hash and method hash (`7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675`) were checked before integration. The coordinator read the entire typed report and retained its source evidence. No prior review or ingest supplied characterization. The specialist supplies memory analysis, not independent semantic clearance of this synthesis.

Proposal mapping uses exact tokens: MEM-OBJ-1 → OBJ-8; MEM-RTE-1 → RTE-9; MEM-ABS-1 → limitation on RTE-8, not an ABS record. The last proposal already carried uninspected status; its local prefix did not establish absence. Known profile axes retain the specialist's values, basis and scope, with canonical references expanded when objects were split. Superseded OBJ-1, OBJ-3, OBJ-4, OBJ-5 and OBJ-6 keep their original combined referents and evidence, with new monotonic part IDs OBJ-9, OBJ-10, OBJ-11, OBJ-12, OBJ-13, OBJ-14, OBJ-15, OBJ-16, OBJ-17, OBJ-18, OBJ-19 and OBJ-20. The source's broader containers OBJ-7, OBJ-10 and OBJ-16 retain identity while their unlike operative parts receive OBJ-21, OBJ-22, OBJ-23, OBJ-24, OBJ-25, OBJ-26 and OBJ-27. Lens overlays do not redefine these records.

All material integration issues are disposed: (1) adaptive statistics are OBJ-8 rather than memory content; (2) derived context/receipts are RTE-9, with ephemeral rendering distinguished from durable source records; (3) faithfulness remains an evidence limitation; (4) defaults, enabled profile and optional turnover are separate; (5) verified means measured, view sorting differs from inheritance filtering; (6) citation, successful cited action and fixed-action intervention do not prove recall dependence, and selected diagnostics can exceed delivered content; (7) replay does not reconstruct adaptive statistics or promise future prompt equivalence; (8) all automatic trace-fed continuation/outcome/recipe/skill/counter/receipt routes enter the comparison dependencies, while raw logs/rendering do not; (9) final ownership, checks and publication remain coordinator-owned.

The coordinator sent the worker questions about BUILD's tested-recipe wording, measurement-only verification and VM instruction versus aggregate bounds. Findings on those prompted issues are coordinated checks, not independent convergence. The parent retained the source-supported caveats on RTE-3, RTE-4 and RTE-6. Coordinator normalized three specialist citation endpoints to the full pinned blob bounds: events.py ends at154 and the named profile ends at99. The specialist could not be resumed because the shared thread slots were occupied; parent confirmed this mechanical correction. Quotation bytes, findings/profile, frozen input and method remain unchanged. The final report hash above identifies the corrected report. No unresolved substantive conflict requires choosing a stronger status. Memory generic records belong to the canonical register; the local epistemic lens adds warrant/phase annotations only. RTE-10 and BAP-4 make observer outcome criteria distinct from model/agent authority.

## Bounded synthesis

SwarmWorld wires an episode-level experimental society: models propose local plans and technological artifacts, a deterministic simulator decides physical consequences, and explicit private/shared memory carries experience into later calls. The artifact programs remain executable after the authoring call, and optional inheritance can carry measured skill records across agent replacement. These are concrete persistence and revision mechanisms; their value is not contingent on proving provider weight change.

The strongest supported learning contribution is automatic continuation-state, measurement/input association, action feedback and adaptive retrieval written during an episode and read by later policies or selectors. Trace learning is wired in the comparison's structural sense. Criticism of an operative formulated theory improving capacity for future action has conclusion status uninspected: candidate-linked theory application, content-directed criticism and attributable gain were not supplied by this source-only pass. Stored hypothesis text and success counters cannot fill those links.

Reflection has conclusion status wired in a bounded operational sense. The system represents selected internal agent history/progress/intent and access statistics; action/measurement changes update those representations; subsequent context queries and ranking consume them and can change later behavior. The two-way dataflow on RTE-2, RTE-3 and RTE-7 supports this limited self-representation. Reflection specifically on a theory of the system's theory-building organization has conclusion status uninspected. Useful improvement does not follow from the reflective loop.

Self-improving operation has conclusion status afforded: evidence can guide plan, research-state, recipe and program replacement through RTE-2, RTE-4 and RTE-6; admission does not require better performance, and no retained comparison establishes net improved capacity. Actual self-improvement has conclusion status uninspected. This separates a route for revising behavior from demonstrated benefit and from criticism of a theory.

For simulator-domain experiments, the source usefully separates measurements from prose and retains provenance/input associations. Its gates have deliberately different licenses: syntax permits execution; resource/provenance permits combination; measured status permits priority/inheritance; scorecard criteria describe physical outcomes. None is a general truth gate for explanations. BUILD's tested-recipe wording, the broader verified label and replay's state projection need the concrete limits stated above. A follow-up could change this assessment by retaining candidate-specific hypothesis/consequence/test/revision traces, measured matched learning comparisons, recalled-content interventions with replanning, a tested-construction gate, or replay restoration/checks that include access metadata.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| No candidate-linked operation admitted | SRC-1, RTE-2, RTE-4, RTE-6, RTE-10 | Implementation/doctrine only | Observed learning, criticism, improvement or accepted theory | Frozen episode artifacts linking exact candidates, inputs, outcomes and later use |
| Provider internals and exact weights opaque | CMP-3, RTE-2 | Request/response interface | Hidden reasoning process, weight fixity/update, reliable inference | Inspectable provider/model boundary and applicable probes |
| Recall dependence not tested in admitted evidence | OBJ-8, RTE-7, RTE-8 | Retrieval/citation/replay code | Faithful citation or causal use of recalled content | Retained interventions on recalled content with fresh decisions and controls |
| Physics validity excluded | CMP-1, OBJ-15, OBJ-23, RTE-10 | Configured surrogate outcomes | Real-world scientific validity or explanatory transfer | External validation of equations/measurements and domain transfer evidence |
| Scenario and oracle-policy internals not exhaustive | OBJ-20, RTE-1 | Default biological route/named profile and entry factory | Every scenario equivalence or oracle-policy information symmetry | Frozen scenario-specific and oracle-policy implementation analysis |
| Replay omits access metadata | OBJ-8, OBJ-22, RTE-8 | Current serializer/restorer | Full future model-context equivalence or supported resume | Restoration and equality coverage for selectors/policy state |
| Static checks only | All inspected runtime routes | No target execution | Deployment reliability, outage recovery rate, scaling or empirical effect size | Bounded execution evidence under declared tools/services/configuration |

## Verification and blockers

### Semantic verification

Checked source boundary, full revision and source-only independence; complete specialist identity and unchanged input/report/method hashes; canonical object splits and exact-token proposal mappings; all fourteen comparison axes; quote text occurrence and local anchors; route ownership and status separation; configuration alternatives; all material admissions and authority horizons. Every material route has immediate return, later read-back, visibility, selection/expiry, activation limit and recovery disposition. Dynamic behavior remains unobserved.

Profile checks cover RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8 and RTE-9. Trace-fed union includes continuation, outcomes/intent, recipe-linked measurements, skill observations, adaptive metadata and receipts with event-stream source, per-episode task horizon, online timing and prose/symbolic form. Pure rendering/raw recording and static configuration were excluded explicitly. Push consumer/trigger/input/selected part are recorded for lexical private/archive, coarse locality/recency/limits, exact program focus and participant requests. Requested record resolution and operator replay are pull. Inaccessible provider state is excluded rather than silently represented as a known memory form. Citation and delivery never establish activation; replay/knockout design never substitutes for an executed faithfulness comparison. Epistemic checking, disposition, retention and post-acceptance integration remain separate.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-swarmworld-01/result.md`. `commonplace-validate --full` passed cleanly. Full pinned-blob checks matched all40 quotes and verified citation endpoints; source-quote and anchor checks precede publication. No review-job or receipt is embedded in this result.

### Blockers

None.
