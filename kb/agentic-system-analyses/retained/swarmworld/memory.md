---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SwarmWorld's bounded private evidence, research-state reuse, public and spatial communication, program inheritance and recorded reconstruction."
run-id: AAS-2026-10-15-swarmworld-e39fbc17e3fb-01
source-identity: https://github.com/lamm-mit/SwarmWorld
reviewed-boundary: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
---

# SwarmWorld memory report

## Boundary and evidence

This report covers memory inside the enclosing society simulator at the frozen boundary in [boundary](boundary.md#boundary-and-evidence). Retained experience enters later model decisions through private retrieval, latest research state, empirical summaries, experiment history, public publications, spatial insights, program knowledge and pending requests. Recorded state also reaches replay and researcher-facing playback. These are different consumers and authority paths, not one knowledge store.

All direct findings below use SRC-1 at commit `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`. HEAD was rechecked against that value. Direct reads cover `src/biofoundry/memory.py`, `src/biofoundry/knowledge.py`, `src/biofoundry/program_library.py`, and bounded implementation passages in `src/biofoundry/simulation.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/science.py`, `src/biofoundry/events.py`, `src/biofoundry/counterfactuals.py` and `src/biofoundry/playback.py`. CLI dispatch was searched for trace/replay/evaluation consumers. These supply implementation evidence, not observed runs. Supplied runtime findings establish the installed entrypoint, driver protocols, provider boundary, artifact installation and static scenario guidance; those findings are cited rather than treated as independent direct inspections.

Excluded from use-generated memory: static scenario instructions and catalogs, ordinary physical world arrays, action queues before execution, and external provider internals. Their context or execution effects remain relevant through supplied records. No source access gap was encountered. Available details not audited below are named explicitly; no exhaustive semantic or security audit is claimed. No target code, tests, model calls, or examples were executed. External paper data and successful model behavior remain outside the evidence.

| Entry point or operation | Inspected source and basis | Coverage or remaining limit |
|---|---|---|
| CLI/live/human model planning; direct environment/controller actions | Supplied `src/biofoundry/cli.py`, `src/biofoundry/server.py`, `game/session.py`, `src/biofoundry/env.py`; direct policy reads | [RT-RTE-model-planning](runtime.md#rt-rte-model-planning), [RT-RTE-direct-control](runtime.md#rt-rte-direct-control); different controllers can author the same social writes. |
| Initial private/empirical stores and passive sensing | Direct `src/biofoundry/simulation.py`, `src/biofoundry/knowledge.py` | [MEM-RTE-evidence-retention](#mem-rte-evidence-retention); initialized by software from configured population/world, not by per-record human approval. |
| INSPECT, recipe proposal/combination, TEST, action feedback | Direct `src/biofoundry/simulation.py`, `src/biofoundry/science.py` | [MEM-OBJ-research-mission](#mem-obj-research-mission), [MEM-RTE-evidence-retention](#mem-rte-evidence-retention). OPERATE's full fabrication internals and lab physics not audited; no independent measurement-validity claim. |
| Model research-state writing and failure rollback | Direct `src/biofoundry/policies/llm.py` | Annotation on [RT-RTE-model-planning](runtime.md#rt-rte-model-planning); [MEM-OBJ-research-state](#mem-obj-research-state). |
| Private/public retrieval, program view, evidence summaries and context trimming | Direct `src/biofoundry/memory.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/simulation.py`, `src/biofoundry/program_library.py` | [MEM-RTE-context-selection](#mem-rte-context-selection); exact delivered evidence is bounded, not the full stores. |
| COMMUNICATE, TEACH, PUBLISH, insight deposit and request receipts | Direct `src/biofoundry/simulation.py` | [MEM-RTE-social-retention](#mem-rte-social-retention), [MEM-OBJ-message-records](#mem-obj-message-records); spatial radius and receipt rules differ from public archive access. |
| Citation/action-outcome feedback | Direct `src/biofoundry/memory.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/simulation.py` | [MEM-RTE-retrieval-feedback](#mem-rte-retrieval-feedback); changes ranking metadata, not scientific truth or record prose. |
| BUILD/WRITE_PROGRAM/FORK_PROGRAM; local observation, measurement and teaching | Supplied installation route plus direct library/simulation reads | [RT-RTE-program-install](runtime.md#rt-rte-program-install), [MEM-OBJ-program-library](#mem-obj-program-library), [MEM-OBJ-program-skills](#mem-obj-program-skills). Full VM semantics supplied by runtime, not re-audited. |
| Mortality/respawn and cultural inheritance | Direct `src/biofoundry/simulation.py`, `src/biofoundry/program_library.py` | [MEM-RTE-cultural-inheritance](#mem-rte-cultural-inheritance); private evidence resets while selected skill indices may survive. |
| Event recording, prompt deduplication, committed-state replay and observer playback | Direct `src/biofoundry/events.py`, `src/biofoundry/counterfactuals.py`, `src/biofoundry/playback.py`; CLI search and supplied route | [MEM-OBJ-event-trace](#mem-obj-event-trace), annotation on [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay). Offline analysis/dossier internals not inspected; no claim that their prose becomes agent memory. |
| Frozen-society evaluation, scenario editing and provider retention | Supplied records only | [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay), [RT-RTE-scenario-admission](runtime.md#rt-rte-scenario-admission), [RT-CMP-configured-model](runtime.md#rt-cmp-configured-model). No demonstrated assay-to-agent update or provider-internal memory conclusion. |

## Core ideas

1. **Research state is a replaceable model-authored continuity surface.** The newest retained state is explicitly sent back in addition to ranked memory. Its hypothesis and progress fields are not software-certified conclusions. Evidence-ID filtering checks availability, not whether a citation supports the prose ([MEM-OBJ-research-state](#mem-obj-research-state)).
2. **Experience changes both content and access.** Simulator observations, tests and outcomes create records. Citation and action-success counters separately change optional retrieval ranking. The latter is a trace-fed update to selection metadata, not automatic rewriting of a scientific claim ([MEM-RTE-retrieval-feedback](#mem-rte-retrieval-feedback)).
3. **Public, local and private retention are separate.** A published insight is private notebook content, a spatial deposit and an archive entry. Teaching can copy retained evidence into another notebook without publication. Request fulfillment can push result records back to a sender. Each channel has its own visibility and admission rules ([MEM-RTE-social-retention](#mem-rte-social-retention)).
4. **“Verified” program knowledge means measured exposure.** It is not a pass/fail assessment. Content-addressed instructions, per-agent evidence indices and the installed executable have distinct consumers. Selected measured skills can survive agent replacement even when private evidence is reset ([MEM-OBJ-program-skills](#mem-obj-program-skills), [MEM-RTE-cultural-inheritance](#mem-rte-cultural-inheritance)).
5. **Context is rebuilt by value.** Each macroturn receives a fresh pair of messages. Ranking, excerpting and list trimming omit evidence without deleting its authoritative store. The character budget can remain exceeded after removable material is exhausted; omitted evidence may return on a later macroturn ([MEM-RTE-context-selection](#mem-rte-context-selection)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-agent-memory
Label: AgentMemory evidence records

Identity: each population slot's `AgentMemory` working, episodic and notebook deques, excluding the separately assessed research-state payload and retrieval metadata. Storage: in-process bounded deques of `MemoryRecord`; serialization can retain records in authoritative state and traces. Representational form: symbolic IDs, ticks, kinds, salience and causal-parent edges surround natural-language messages/results or JSON evidence with fixed fields. Structured measurements are symbolic evidence; their textual display is not a learned dense representation. No embeddings are used by the inspected lexical selector. SRC-1, `src/biofoundry/memory.py`, `src/biofoundry/simulation.py`.

> self.working: deque[MemoryRecord] = deque(maxlen=max(4, min(capacity, 16)))
> self.episodic: deque[MemoryRecord] = deque(maxlen=capacity)
> self.notebook: deque[MemoryRecord] = deque(maxlen=max(capacity, 32))
> --- `src/biofoundry/memory.py`

`remember` always appends to working and episodic and optionally to notebook. Notebook therefore extends retention, but does not make records permanent. Retrieval deduplicates episodic plus notebook by record ID; `get` also searches working. Record bodies come from observations, action outcomes, admitted controller prose, teaching and result receipts. Later consumers are the context builder, ID resolvers and social transfer. Unlike [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues), these are retained evidence, not pending executable actions. No equivalent object is declared in the supplied runtime; its planning route consumes this store.

#### MEM-OBJ-research-state
Label: Self-authored research state

Identity: `MemoryRecord(kind="research_state")` written after local model-output validation, with goal, hypothesis, progress, next checkpoint, collaboration need and evidence IDs. Storage: the same private deques, with `notebook=True`; latest retained tick selected at every macroturn. Form: model-interpreted natural-language fields inside symbolic JSON; evidence-ID lists and causal-parent links are symbolic availability/provenance metadata. This is a distinct payload part of private memory, not another action queue or a static scenario prompt. Closest supplied record: [RT-RTE-model-planning](runtime.md#rt-rte-model-planning), whose write/read endpoints are annotated below, not re-declared. SRC-1, `src/biofoundry/policies/llm.py`.

> prior_state_record = simulation.memories[index].latest("research_state")
> prior_state = (
>     prior_state_record.content if prior_state_record is not None else "none yet"
> )
> --- `src/biofoundry/policies/llm.py`

A successful response writes a new record rather than editing the old hypothesis in place. Evidence IDs survive only if privately retained, in the public archive, or known as programs. The filter does not check entailment or require that the cited item survived prompt trimming. The record may retain the model's rationale in its prose fields, but no separate criticism or reasoning transcript is required. Latest-state delivery establishes continuity, not reliance, truth, learning or content-directed criticism; the runtime's independent theory-builder limits remain applicable.

#### MEM-OBJ-retrieval-stats
Label: Retrieval feedback metadata

Identity: `AgentMemory.retrieval_stats` and `last_retrieval`. Storage: in-process dictionaries indexed by retained record ID; diagnostics can be serialized into model traces. Form: symbolic counts, scores, IDs and query terms, not edited evidence content. Lineage: selector selections, cited selected IDs and reported action success. Consumer: optional adaptive ranking. Distinct from the evidence payload and from [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues); closest route is [RT-RTE-model-planning](runtime.md#rt-rte-model-planning). SRC-1, `src/biofoundry/memory.py`.

> feedback = 0.5 * citation_rate + 0.5 * (
>     causal_success_rate if outcome_attempts else 0.0
> )
> --- `src/biofoundry/memory.py`

Counters can outlast the corresponding deque entry; ranking candidates still come from retained records. Selection is counted before excerpt trimming, so `selected` need not mean actually delivered. The source's `used` counter means cited by the accepted response/action, not demonstrated causal reliance. See [MEM-RTE-retrieval-feedback](#mem-rte-retrieval-feedback).

#### MEM-OBJ-empirical-knowledge
Label: Sparse empirical knowledge

Identity: per-agent `EmpiricalKnowledge.cells`, extraction attempts and successes. Storage: in-process cell-index dictionary and counters, serialized by `authoritative_state`. Form: symbolic spatial coordinates, categories, scalar measurements and counts. Latest observation overwrites a cell's earlier evidence rather than preserving its full time series. Consumer: nearest-observed-site summaries for the model, and `grounded_resources` for recipe admission; those are interpretive and fixed-rule consumers respectively. SRC-1, `src/biofoundry/knowledge.py`, `src/biofoundry/simulation.py`.

> self.cells[y * self.width + x] = CellEvidence(
> --- `src/biofoundry/knowledge.py`

> "scope_note": "Unlisted materials are unobserved, not proven absent.",
> --- `src/biofoundry/knowledge.py`

Direct sensing, inventory and optionally shared-depot possession ground resource IDs. Grounding does not establish that an agent's hypothesis is correct or that an old site still contains its observed mass. No supplied runtime object covers this evidence store; it is not the global world state in [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping).

#### MEM-OBJ-cultural-archive
Label: Public cultural archive

Identity: `CulturalArchive.records` and its `by_id` index. Storage: append-only in-process list plus dictionary, with trace/state serialization. Form: `MemoryRecord` wrappers and authored text, not an authoritative database of scientific truths. `publish` deduplicates IDs; it does not validate assertions. Consumers: recent/lexical model context, teaching resolution, research-state citation filtering and publication-parent checks. SRC-1, `src/biofoundry/memory.py`, `src/biofoundry/simulation.py`.

> def publish(self, record: MemoryRecord) -> None:
>     if record.record_id in self.by_id:
>         return
>     self.records.append(record)
>     self.by_id[record.record_id] = record
> --- `src/biofoundry/memory.py`

This is a distinct retained object downstream of [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping), not a duplicate route. Research publication provenance is separately assessed in [MEM-OBJ-research-mission](#mem-obj-research-mission). No retraction operation was inspected in the archive implementation; append-only storage alone does not establish that every publication remains displayed or scientifically accepted.

#### MEM-OBJ-deposited-insights
Label: Spatial insight deposits

Identity: `simulation.deposited_insights`, including published and unpublished entries. Storage: in-process list of record dictionaries with author, position and publication flag, retained in authoritative state. Form: natural-language insight content plus symbolic location and provenance. Same record can also inhabit private memory and archive, but the spatial index is a separate access surface. Consumer: nearby-insight observation; software examines only the last 128 deposits, newest first, filters Manhattan distance by communication radius, and returns at most four compact or eight ordinary entries. SRC-1, `src/biofoundry/simulation.py`.

> for insight in reversed(self.deposited_insights[-128:]):
> --- `src/biofoundry/simulation.py`

This differs from globally available archive retrieval; old or distant deposits can remain stored without being eligible for this view. Closest supplied record is the executor [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping), not an equivalent object.

#### MEM-OBJ-message-records
Label: Delivered message and request ledger

Identity: `simulation.message_records`, separate from copies in private memory. Storage: in-process dictionary with sender, recipients, reply edge, response list and fulfillment list, included in authoritative state. Form: authored natural-language content and symbolic delivery/response/result edges. Consumer: `_validate_reply_to`, `_pending_requests` and fulfillment routing. Pending requests are selected by recipient and lack of that agent's fulfillment, newest first, at most six, with content truncated to 500 characters. A response alone does not remove the request. SRC-1, `src/biofoundry/simulation.py`.

> """Expose unresolved addressed work as state, without interpreting its prose."""
> --- `src/biofoundry/simulation.py`

The selector actually tests recipients, not the `addressed` flag: it can expose an unresolved delivered message even if broadcast. Fulfillment associates a successful action with an agent-selected request edge; it does not assess whether the action satisfied the prose. Distinct from the direct-control route [RT-RTE-direct-control](runtime.md#rt-rte-direct-control) and from transient action queues.

#### MEM-OBJ-research-mission
Label: Research mission retained evidence

Identity: `ResearchMission` inspections, proposals, staged batches, tests, publications, claims and contribution records. Storage: in-process structured collections, exported by `authoritative_state`. Form: symbolic recipes, measured properties, test flags and provenance; task claims are separately model/human-interpreted prose keyed by author. The public model view supplies task claims and publication metadata, not all internal evaluator state. Private experiment views filter by agent and distinguish untested sample identity/recipe from measured properties. SRC-1, `src/biofoundry/science.py`, `src/biofoundry/simulation.py`.

> if self.config.experience_reuse:
>     # This is the agent-authored input that produced the measured coupon,
>     # not evaluator state. Retaining it closes the experience-reuse loop.
>     result["source_recipe"] = json.loads(json.dumps(batch.source_recipe))
> --- `src/biofoundry/science.py`

> if key != "passes_material_target"
> --- `src/biofoundry/science.py:435-466`

The private result view and TEST's notebook record omit `passes_material_target`, although internal tests and event payloads retain it. With experience reuse enabled, source recipe is carried alongside measured outcomes, supplying input-to-outcome continuity rather than a rewritten theory. Publication provenance can license additional grounded resources in COMBINE_DESIGN, subject to published IDs, structured provenance and minimum distinct grounded contributors. “Validated” proposal records mean mechanical recipe/provenance acceptance, not experimental success. This store is distinct from the evaluator route [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay); shared data does not establish assay-result feedback.

#### MEM-OBJ-program-library
Label: Program registry and lineage

Identity: `ProgramLibrary.programs` and `lineage_edges`: canonical instructions, names, author lists, installation history and instruction differences. Storage: in-process global dictionaries/list and trace serialization. Form: symbolic executable DSL plus symbolic provenance; program names are descriptive text, not execution. Distinct from per-agent knowledge indices below. The installed executable is already [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program); this record is its registry/history access surface, not a new declaration of that program. SRC-1, `src/biofoundry/program_library.py`.

> "instructions": [dict(item) for item in program.instructions],
> --- `src/biofoundry/program_library.py`

`register` merges by content ID, adds authors/installations and records parent-child diffs. `resolve` reconstructs an `ArtifactProgram` from retained instructions. The executable consumer and force remain [RT-BAP-program-execution](runtime.md#rt-bap-program-execution); the model can also receive instructions in a skill view. No requirement to retain a causal explanation for each instruction change is enforced here.

#### MEM-OBJ-program-skills
Label: Per-agent program knowledge indices

Identity: `ProgramLibrary.skills[agent_id][program_id]`. Storage: in-process dictionaries with bounded evidence-ID and measurement tails plus cumulative counts; serialized authoritative state. Form: symbolic membership, verification/inheritance flags, source labels, ticks and measurement evidence, separate from registry instructions. Consumers: known-parent admission for forks, ranked model views, teaching and cultural inheritance. SRC-1, `src/biofoundry/program_library.py`, `src/biofoundry/simulation.py`.

> A library entry grants knowledge of a program, never material access or a physics
> advantage. ``verified`` means the agent obtained a measured artifact observation;
> it is deliberately not an evaluator pass/fail label.
> --- `src/biofoundry/program_library.py`

Authorship and local observation admit unverified indices; INSPECT admits measured entries; teaching copies the sender's verification flag and latest measurement, so a recipient's verified entry need not mean its own direct measurement. Compact views keep full instructions but bounded recent evidence and measurement tails; ordinary views expose retained entry fields. Views prioritize focus IDs extracted from prior-state text, then verified status, recency and ID, at six compact or twelve ordinary entries. Distinct from [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program): knowledge can remain after installation replacement and does not itself execute.

#### MEM-OBJ-event-trace
Label: Recorded events, decisions and snapshots

Identity: recorder JSONL or gzip stream, including model messages/response, accepted research state, actions, events, snapshots and optional prompt templates. Storage: filesystem, unlike live in-process stores. Form: symbolic records, with raw natural-language request/response payloads and structured evidence. Raw model traces are not themselves a compacted scientific memory; research-state records and replay/observer summaries are distinct derived uses. SRC-1, `src/biofoundry/events.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/playback.py`.

> replacements.append((value, f"{{{{trace_template:{template_id}}}}}"))
> --- `src/biofoundry/events.py`

Deduplication stores hash-identified prompt templates and substitutes markers; `read_records` expands markers from earlier templates. This is reversible string factoring, not semantic summarization. Snapshots have a display digest and may have a separate authoritative state digest; neither should be mistaken for a complete restorable memory checkpoint. Closest supplied record is [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay), annotated below. Source code supplies capability and consumers, not an actual trace or demonstrated replay agreement.

### Routes

#### MEM-RTE-evidence-retention
Label: Simulator evidence retention

Endpoints and progression: initial/passive sensing, INSPECT, recipe proposal, TEST and action execution → simulator-authored evidence records and mission state → later observation/retrieval or fixed recipe grounding. Owner: simulator and research mission. Controllers choose optional actions; software produces measurements, validates recipe/provenance admission and can reject actions. No routine human content approval. Mode: bounded simulated research; authoritative simulator outcomes supply evidence, not an independent physical-world oracle. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/knowledge.py`, `src/biofoundry/science.py`.

- Immediate return: updated state plus step events, or rejection feedback; passive initialization directly populates sparse evidence.
- Later read-back: observations, tests, recipe proposals and action-result records enter private context; sparse cells/counters become empirical summaries and grounding sets; mission state yields public metadata and agent-private experiment views.
- Delegated visibility: passive cells concern the agent's sensed neighborhood; private experiments filter by owner; shared publication metadata and depot state follow treatment flags.
- Selection predicate: visible current/cardinal cells for passive sensing; local INSPECT artifact distance at most one; TEST selects newest untested batch; recipe and multi-author publication checks gate proposals.
- Invalidation or expiry: cell observations overwrite per position, private deques evict, and respawn resets private/empirical stores; mission history has distinct retention. A later observation is not proof that every old record is removed.
- Activation or effect: retained resource evidence affects fixed-rule recipe admission; model delivery of observations does not demonstrate their influence on a particular hypothesis.
- Evidence limits: simulated measurements and mechanical checks are inspectable; physical validity, executed decisions, content-directed criticism and scientific benefit are unobserved. Full lab internals were not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.memories[index].remember(record, notebook=True)
> if self.research is not None:
>     self.research.record_inspection(observation)
> --- `src/biofoundry/simulation.py`

Part versus supplied routes: this groups evidence producers inside [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping) and initialization, rather than replacing that executor. It spans initialization as well as stepping, so is not wholly part of exactly one supplied route. The durable changes and consumers are [MEM-OBJ-empirical-knowledge](#mem-obj-empirical-knowledge), [MEM-OBJ-agent-memory](#mem-obj-agent-memory) and [MEM-OBJ-research-mission](#mem-obj-research-mission). Rejected actions can retain failure descriptions rather than becoming proposed recipe records. Recovery is later corrected action; no scientific rollback is implied. Fixed summaries/counts transform traces automatically, but do not formulate a new explanatory theory.

#### MEM-RTE-context-selection
Label: Macroturn context selection

Part of: [RT-RTE-model-planning](runtime.md#rt-rte-model-planning)

Endpoints and progression: scheduled agent and latest private state → semantic observation and lexical private retrieval → bounded excerpts and optional prompt trimming → fresh system/user message pair. Owner: LLM policy and deterministic store selectors; model-authored prior state supplies focus but does not execute retrieval as a separate tool call. SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/memory.py`, `src/biofoundry/simulation.py`, `src/biofoundry/program_library.py`.

- Immediate return: rendered messages plus context/retrieval diagnostics, subsequently passed to the provider.
- Later read-back: selected retained private records, latest research state, empirical summaries, public/spatial content, skill instructions, action feedback and experiment/request history reach the next model invocation by value.
- Delegated visibility: one agent's private packet; shared sources are visible only through selected communication/treatment views. No sub-agent frame or cross-agent hidden reasoning return is implemented in this route.
- Selection predicate: private query concatenates prior state, pending requests and local observation; candidates are episodic plus notebook records, scored by salience, lexical relevance, tiny recency term and optional feedback/exploration. Ordinary private limit is six; attention mode uses configured limit with default four. Public compact retrieval queries prior state; ordinary public view takes recent eight. Spatial, empirical and skill selectors retain their different targeting rules.
- Invalidation or expiry: omissions/excerpts affect the message, not stored content; new macroturns rebuild context and can retrieve omitted records again. No reload of an arbitrary full record through a provider tool is established here.
- Activation or effect: delivery supplies model-interpreted evidence and instructions; particular reliance or improved action is unobserved. Trimming cannot be equated with deleting learned knowledge or changing provider weights.
- Evidence limits: character counts are not token guarantees; minimum causal-core content may exceed the budget. Retrieval diagnostics may list candidates subsequently omitted from delivery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> """Render bounded evidence without changing the authoritative stored record."""
> --- `src/biofoundry/memory.py`

Private records default to 2,000-character excerpts. For long observation JSON, artifact measurements first become artifact/program/performance triples; remaining overlength content is truncated and may no longer be complete JSON. Attention trimming removes retrieved-memory entries from the end before shrinking skill, artifact, archive, insight, experiment, public-evidence and action-result lists according to `_shrink_observation`. Some lists preserve minima initially but skill/archive/insight/catalog lists can later be cleared entirely. Latest research state, local/core observation and static guidance remain outside these list-removal operations. See the supplied prompt-budget passage in [RT-RTE-model-planning](runtime.md#rt-rte-model-planning).

The stack-frame analogy fits only the isolated fresh request and selected input packet: there is no accumulating provider conversation to compact or pop. The heap analogy fails because excerpts are values, not followable references in the model window. IDs remain useful to future simulator actions and selectors, but do not establish automatic dereferencing by the model.

#### MEM-RTE-retrieval-feedback
Label: Retrieval citation and outcome feedback

Endpoints and progression: private ranking selection → accepted response/action citations → action outcome counters → optional future adaptive score. Owner: `AgentMemory`, invoked by policy and simulator. Model/controller proposes evidence and causal-parent IDs; software intersects cited IDs with last selection for `used`, and ignores outcome credit for IDs without statistics. This is software admission of access metadata, not per-content human approval or scientific adjudication. Mode: ongoing macroturn/tick adaptation; simulator action success is the feedback signal, not an expected scientific answer. SRC-1, `src/biofoundry/memory.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/simulation.py`.

- Immediate return: mutated selection/use/outcome statistics and retrieval diagnostics; no new claim text.
- Later read-back: future `retrieve(adaptive=True)` reads citation rate, causal-success rate and exploration counts to score retained candidates.
- Delegated visibility: statistics are private to the slot; optional diagnostics expose numeric reasons to recorded traces. Citations are controller assertions, not observed cognition.
- Selection predicate: selected IDs intersect accepted cited evidence or action parents for use; outcome parents with existing statistics receive success/attempt increments. Feedback is half citation rate and half causal-success rate, plus a separate exploration bonus in the score.
- Invalidation or expiry: store reset clears the metadata; outage freeze restores the entire scheduled memory snapshot. Record eviction removes candidate content but the inspected feedback implementation does not automatically delete its statistics.
- Activation or effect: fixed-rule ranking depends on retained counters when adaptive mode is enabled. This can alter later evidence selection without changing evidence bodies; model reliance and beneficial learning are not established.
- Evidence limits: action success can reflect simulator acceptance or a local consequence, not truth of cited explanations. Selection counts precede trimming; not all selected items were delivered.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.memories[index].mark_causal_outcome(
>     set(map(str, action.causal_parents)), success=success
> )
> --- `src/biofoundry/simulation.py`

This spans policy citation processing and later simulator consequences, overlapping [RT-RTE-model-planning](runtime.md#rt-rte-model-planning) and [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping), not duplicating either. Raw source traces are same-system selection/citation/action outcomes; derived result is [MEM-OBJ-retrieval-stats](#mem-obj-retrieval-stats), whose update reasons remain as numeric diagnostics, not a narrative justification. No improvement-triggered successor selection or theory revision is implemented by these counters. Learning: changed access capacity is inspectable, but improved future capacity and attribution remain uninspected.

#### MEM-RTE-social-retention
Label: Social evidence retention and transfer

Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints and progression: controller-authored message/insight, cited retained evidence/program or successful reply-linked action → simulator checks → recipient memories, public/spatial stores, program indices or sender receipts → later context and ID-based actions. Owner: simulator; model, human or scripted controller proposes content and target, software decides admissibility, no recipient approval or routine human review is required. Mode: simulated collaboration, with no prose-truth oracle. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/program_library.py`, `src/biofoundry/memory.py`.

- Immediate return: communication/publication/teaching/fulfillment events and retained records, or action rejection.
- Later read-back: private retrieval, public archive/research catalog, spatial observations, pending requests and program views expose channel-specific retained parts; successful request receipts may copy resolved result records back to the original sender.
- Delegated visibility: COMMUNICATE/TEACH use nearby recipients and optional known local target; reply IDs require prior participant visibility. PUBLISH has global archive visibility subject to treatment/context selection; deposits remain spatially selected. Fulfillment receipts route to the original sender without repeating local-recipient selection.
- Selection predicate: messages/insights require nonempty content; TEACH resolves private/archive parent IDs or known program IDs, or admits fallback prose. Program transfer requires sender knowledge. PUBLISH additionally registers structured resource provenance when a mission exists. Reply tracking attaches a successful action to a selected delivered request, not to a semantic fulfillment test.
- Invalidation or expiry: recipient deques evict; archive and spatial/ledger records have separate lifetimes; fulfilled requests stop appearing for that recipient, but records are not thereby deleted. No inspected publication withdrawal or belief-revision operation is supplied by these channel implementations.
- Activation or effect: recipient input can change later decisions; publication provenance can mechanically license combined-design resource use. Text truth and actual downstream model reliance are unobserved.
- Evidence limits: source-ID/participant/resource checks are not assertion verification. Message receipt, program verification transfer and fulfillment labels do not prove understanding, successful science or satisfaction of a natural-language request.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for recipient in recipients:
>     for record in records:
>         self.memories[recipient].remember(record, notebook=True)
> --- `src/biofoundry/simulation.py`

> self.memories[sender_index].remember(receipt, notebook=True)
> --- `src/biofoundry/simulation.py`

TEACH preserves copied record IDs and content; it can inject them into another notebook rather than derive a fresh summary. Insight content is author-prefixed and truncated to 1,000 characters, kind to 40, salience clipped to [0,1], then privately retained and spatially deposited; PUBLISH additionally admits the same record to the archive. Publication provenance is distinct from archive prose. Replacement/recovery means later communication, teaching or action; storage has no automatic scientific correction/rollback. Objects: [MEM-OBJ-cultural-archive](#mem-obj-cultural-archive), [MEM-OBJ-deposited-insights](#mem-obj-deposited-insights), [MEM-OBJ-message-records](#mem-obj-message-records) and [MEM-OBJ-program-skills](#mem-obj-program-skills).

#### MEM-RTE-cultural-inheritance
Label: Program knowledge across replacement

Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints and progression: configured mortality/respawn → verified skill ranking or clearing → fresh private/empirical stores and selected inherited program indices → later skill view/known-parent use. Owner: simulator and program library. Software decides selection under configured flags; starting the episode is not per-content human approval. Mode: bounded replacement treatment; no independent expected-answer or performance-improvement oracle. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/program_library.py`.

- Immediate return: respawn event naming inherited IDs, restored active population slot and replacement memory objects.
- Later read-back: inherited indices expose retained instructions and measurement evidence in subsequent model views; they also support known-program checks.
- Delegated visibility: same stable agent ID now has incremented generation; inherited subset is local knowledge while global registry/history persists independently.
- Selection predicate: enabled cultural inheritance plus skill library; only verified entries ranked by retained measurement count, last observation tick and ID, capped by configured inherited skill limit.
- Invalidation or expiry: otherwise all agent skill entries clear; private memory, empirical knowledge and action feedback reset even when skills survive. Later observations/teaching can extend the new indices.
- Activation or effect: software retains selected knowledge and changes later eligibility/context. Inheritance does not copy an installed artifact into inventory or establish a physics advantage.
- Evidence limits: measured exposure is not demonstrated utility; retained measurement count is a heuristic, not a validated cultural-fitness objective. No executed multi-generation benefit is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.memories[index] = AgentMemory(self.config.population.memory_capacity)
> self.empirical_knowledge[index] = EmpiricalKnowledge(self.world.width)
> self.action_feedback[index].clear()
> --- `src/biofoundry/simulation.py`

> entry["sources"] = ["cultural_inheritance"]
> --- `src/biofoundry/program_library.py`

This is not a duplicate of [RT-RTE-program-install](runtime.md#rt-rte-program-install): no executable installation is proposed or selected. Registry instructions and bounded evidence survive indirectly; original source labels are replaced by the inheritance label while evidence/measurements remain. No content-directed criticism or per-content rollback is implied by ranking.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-evidence-admission
Label: Retained evidence in recipe and fork admission

Consumer: simulator grounding/proposal and fork validators. Channel: retained resource cells/possession, public publication provenance and per-agent program membership. Force: symbolic acceptance/rejection, not advice to the model. Horizon: later proposed actions while corresponding evidence/provenance/knowledge remains available. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/knowledge.py`, `src/biofoundry/program_library.py`. See [MEM-RTE-evidence-retention](#mem-rte-evidence-retention), [MEM-RTE-social-retention](#mem-rte-social-retention) and supplied [RT-RTE-program-install](runtime.md#rt-rte-program-install). This is distinct from general action dispatch because it identifies the retained evidence used at admission.

> "COMBINE_DESIGN references records without structured publication "
> f"provenance: {missing_provenance}"
> --- `src/biofoundry/simulation.py`

## Annotations

#### On [RT-RTE-model-planning](runtime.md#rt-rte-model-planning)

Memory write agency: provider/model authors research-state prose; local validation admits its shape, then the policy filters evidence IDs against private retained records, public archive or known programs. No per-content human approval. `mark_retrieval_use` receives those IDs and action causal parents. A new notebook record retains state and evidence IDs; `latest("research_state")` supplies the newest record verbatim as prior state, independently of private retrieval ranking. SRC-1, `src/biofoundry/policies/llm.py`; objects [MEM-OBJ-research-state](#mem-obj-research-state), [MEM-OBJ-retrieval-stats](#mem-obj-retrieval-stats).

> research_state["evidence_ids"] = sorted(retained_evidence)
> --- `src/biofoundry/policies/llm.py`

The source prompts for goal/hypothesis/progress/checkpoint/collaboration, not an independent evaluator-certified explanation. Prior state can carry reasons and altered reliance if the model writes them, but no mandatory blame/criticism schema or executed instance establishes that. Physical state writing is Python; authorship is the model; admission is software. Invalid output does not enter the successful write block. In optional outage freeze, deep-copied scheduled `AgentMemory` instances restore both records and selector statistics, including writes from otherwise successful decisions. This gives a bounded batch rollback, not general world-state rollback.

#### On [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance)

Retained-content authority is model-interpreted evidence/advice, separate from mechanical checks on its IDs. Selected private excerpts, archive prose, spatial deposits, research state, task claims and measurements enter the same fresh prompt but carry different origins. No source-trust ranking authenticates the scientific truth of an agent's prose merely because it is published or highly salient. Rank inputs are inspected in [MEM-RTE-context-selection](#mem-rte-context-selection) and [MEM-RTE-retrieval-feedback](#mem-rte-retrieval-feedback); SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/memory.py`.

#### On [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay)

Storage and lineage: model traces retain accepted research-state dictionaries separately from raw responses/messages. `apply_recorded_model_trace` restores those dictionaries as notebook records before recorded-action stepping, without reinterpreting the raw response or issuing a new model call. False `planning_committed` records are skipped. SRC-1, `src/biofoundry/counterfactuals.py`; [MEM-OBJ-event-trace](#mem-obj-event-trace).

> """Replay authoritative private-memory writes made by the LLM policy."""
> --- `src/biofoundry/counterfactuals.py`

The replay helper does not replay private retrieval scoring, citation-use increments or retrieval diagnostics. The inspected authoritative-state serialization includes record deques but not `retrieval_stats` or `last_retrieval`. Therefore digest agreement cannot establish equality of all later adaptive-selection state. Playback reconstructs from initial configuration and recorded actions, using snapshots/digests for reference and building observer keyframes and dynamics history; it is not a resumed adaptive model society. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/playback.py`.

> "memories": [
>     {
>         "working": [record.as_dict() for record in memory.working],
>         "episodic": [record.as_dict() for record in memory.episodic],
>         "notebook": [record.as_dict() for record in memory.notebook],
>     }
>     for memory in self.memories
> ],
> --- `src/biofoundry/simulation.py`

Observer keyframes/dynamics are derived trace products delivered to playback viewers, not installed private agent conclusions. Scenario/revision/tick/digest checks are compatibility/integrity admission, not a truth test of research-state prose.

## Write side

The write mechanisms differ in admission control, not just storage location:

| Mechanism | Authorship and admission | Retained transformation and later consumer |
|---|---|---|
| Passive sensing, inspection, tests and outcomes | Software generates evidence; optional controller action can trigger it; simulator decides action acceptance. No per-record human approval. | Latest cell overwrite, extraction counts, notebook evidence, recent action/behavior summaries and mission history; later model packet and recipe grounding. [MEM-RTE-evidence-retention](#mem-rte-evidence-retention). |
| Research-state update | Model authors fields, schema and ID availability admit them; invalid output rejected; optional transient-outage batch rollback. | New private JSON record, not in-place semantic correction; later `latest` read plus retrieval. Annotation on [RT-RTE-model-planning](runtime.md#rt-rte-model-planning). |
| Message, teaching, publication and receipts | Selected controller authors or chooses source IDs; simulator checks content, reachability, prior participation and source availability. | Copies, bounded authored insights, public/spatial metadata, result receipts and transferred skills; recipients need not approve. [MEM-RTE-social-retention](#mem-rte-social-retention). |
| Retrieval feedback | Model/controller supplies citations, software records selections/use and action-success credit. | Numeric access metadata influences adaptive selector, not record truth. [MEM-RTE-retrieval-feedback](#mem-rte-retrieval-feedback). |
| Program registry/index maintenance and inheritance | Existing installation validation, observation and measurement writers, sender knowledge for transfer, configured respawn selector. | Canonical instructions/history remain distinct from bounded evidence indices and replacement selection. [MEM-OBJ-program-library](#mem-obj-program-library), [MEM-OBJ-program-skills](#mem-obj-program-skills), [MEM-RTE-cultural-inheritance](#mem-rte-cultural-inheritance). |
| Recording/reconstruction | Driver writes events/decision fields; reader restores committed state and validates compatibility. | Reversible template factoring, fresh replay state, observer keyframes/dynamics; not automatic scientific claim revision. [MEM-OBJ-event-trace](#mem-obj-event-trace), annotation on [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay). |

These rows are grounded by their records. Automatic trace-fed changes include cell/counter updates, action summaries, retained test input/outcome pairing, retrieval feedback and measurement-driven skill indices. Raw messages/events also remain as traces; storing them alone is not an additional learned theory. Where behavior-shaping derived metadata retains reasons, they are IDs, measurements, counts or score components. A later selector/view reads some of them; no required narrative rationale or demonstrated model use follows. Program instruction diffs likewise do not establish formulated criticism. Static authoring and scenario edits remain the supplied [RT-RTE-scenario-admission](runtime.md#rt-rte-scenario-admission), not in-episode autonomous memory curation.

Maintenance includes deque eviction, latest-cell replacement, bounded skill evidence tails, generation reset, request-view withdrawal after fulfillment, context-only omission and explicit outage snapshot restoration. These are not interchangeable with semantic rejection or public retraction. The archive implementation provides publish/recent/retrieve, not a scientific withdrawal workflow; channel and private-store limits remain beside the relevant records rather than a system-wide absence claim.

## Read-back

The later consumer is decisive. Model-context construction automatically selects retained material at a scheduled macroturn; it is not a model-issued memory tool request. Authored prior-state focus targets lexical retrieval and program IDs, while code determines limits and delivery. Private query inputs combine prior state, pending requests and local state; public compact retrieval uses only focus text. Empirical summaries aggregate nearest remembered sites and possession; spatial and public views are not identical. These independent admission paths can deliver related evidence even after a private record falls out of a deque ([MEM-RTE-context-selection](#mem-rte-context-selection)).

COMMUNICATE/TEACH and request fulfillment push evidence into recipient storage when actions execute. A later prompt still selects/excerpts it; unsolicited storage is not guaranteed delivery in full. Program views carry full retained instructions with bounded evidence summaries. Fixed consumers use retained IDs/provenance at recipe and fork admission, whereas the VM consumes installed instructions through the existing [RT-BAP-program-execution](runtime.md#rt-bap-program-execution). The same instructions therefore have descriptive model-input authority and executable authority at different consumers.

Recorded replay is a different read-back horizon: committed research state is restored and actions re-executed without a model decision. Playback derives keyframes and dynamics for viewers. Neither the replay helper nor the provided evaluation route establishes an automatic report-to-model scientific revision loop. See the annotations and [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay). Persistence is wired within an episode, selected program indices can cross replacement generations, and files support offline reconstruction; cross-session adaptive continuation of every private selector state is not established.

## Integration issues

- **Replay completeness qualification, not a contradictory runtime fact.** [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay) restores research records and checks specified state, but does not restore retrieval-statistics evolution. Direct reads of SRC-1, `src/biofoundry/counterfactuals.py` and `src/biofoundry/simulation.py` support the annotation and [MEM-OBJ-retrieval-stats](#mem-obj-retrieval-stats). Consequence: deterministic world/state-digest agreement must not be described as complete adaptive-memory checkpoint equivalence. Full adaptive continuation would require more evidence; it is not needed for fixed-action reconstruction.
- **Verification-label qualification.** [MEM-OBJ-program-skills](#mem-obj-program-skills) separates measured exposure from evaluator success, and transfer can propagate the flag without recipient measurement. SRC-1, `src/biofoundry/program_library.py`. Consequence: reconcile `verified_skill_library` as evidence-index vocabulary, not validated competence or improved performance. No supplied runtime fact requires correction.
- **Selected versus delivered qualification.** [MEM-RTE-context-selection](#mem-rte-context-selection) and [MEM-RTE-retrieval-feedback](#mem-rte-retrieval-feedback) show that retrieval diagnostics/counters precede trimming. SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/memory.py`. Consequence: citation-rate denominators and retained diagnostics cannot alone prove exposure to every selected item.
- **Possible overlaps, not duplicate referents.** [MEM-OBJ-program-library](#mem-obj-program-library) and [MEM-OBJ-program-skills](#mem-obj-program-skills) concern registry/history and knowledge indices around [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program), not another declaration of its executable. [MEM-OBJ-event-trace](#mem-obj-event-trace) is the retained input to [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay), not that route. Context/social/inheritance subroutes carry explicit part relations. Evidence retention spans initialization and stepping; retrieval feedback spans planning and stepping, as declared. No identity supersession is proposed.
- **Remaining inspection limits.** Full lab internals, all offline analysis/dossier consumers and UI presentation details remain available but uninspected. Their absence from direct coverage prevents claims of complete measurement validation, exhaustive offline transformation enumeration or exact viewer display fidelity. This does not suppress the inspected private, public, spatial, program, request and reconstruction routes. No actual model response/episode or empirical dataset is supplied, preventing exercised theory-building, learning, reliance and benefit conclusions. Relevant records retain those limits; no additional source is requested or introduced.

## Limitations and checks

The report describes implemented state and consumer wiring, not successful scientific operation. No particular retained hypothesis, content-directed criticism or improved later decision was observed. Model-weight mutability and opaque provider retention remain those of [RT-CMP-configured-model](runtime.md#rt-cmp-configured-model). Static prompt instructions do not become empirical evidence, and archive/verification/fulfillment labels do not certify prose truth.

The registered Git identity and frozen HEAD were rechecked. Supplied member/type/records/worker inputs were read completely, with bounded recovery where the tool reported a remainder. Only assigned outputs, identity and scratch files were written. No target execution or additional agents were used. Deterministic output validation is recorded below; it establishes format and quotation occurrence, not semantic acceptance.

Validation: passed using the invocation's `commonplace-run validate-output` command.
