---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SwarmWorld epistemic routes: simulated measurement, candidate admission, public reliance, adaptive retrieval and bounded evaluation."
run-id: AAS-2026-10-15-swarmworld-e39fbc17e3fb-01
reviewed-boundary: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
---

# SwarmWorld epistemic report

## Source-and-claim boundary

The question is how SwarmWorld's simulated science acquires evidence, evaluates candidates and licenses later reliance. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); source identity and layers are in its [Source register](boundary.md#source-register). All direct reads below are SRC-1 at the frozen commit, supplying implementation evidence unless explicitly labelled doctrine/design. No target execution, paper dataset, observed run or causal experiment is supplied. Physical-world validity, actual model compliance, exercised learning and empirical scaling therefore remain unestablished. Provider internals and weights remain outside accessible evidence; see [RT-CMP-configured-model](runtime.md#rt-cmp-configured-model).

The public research-environment claim is [EPI-CLM-research-environment](#epi-clm-research-environment). The model's grounding instruction is [RT-CLM-grounded-science](runtime.md#rt-clm-grounded-science). Neither is read as a claim of infallible scientific knowledge. The strongest inspected checks concern simulator measurements, recipe eligibility, typed plans, DSL validity and replay agreement. These are different targets.

| Entry point or operation | Source path | Coverage and records, or remaining limit |
|---|---|---|
| CLI dispatch and ordinary model planning | `src/biofoundry/cli.py`; `src/biofoundry/policies/llm.py` | Direct reads of parser, main dispatch, prompt construction, evidence-ID filtering and output handling; supplied [RT-RTE-model-planning](runtime.md#rt-rte-model-planning) covers scheduling/schema/freeze. |
| INSPECT, passive evidence and action feedback | `src/biofoundry/simulation.py`; `src/biofoundry/knowledge.py` | Direct reads; [EPI-RTE-sensor-evidence](#epi-rte-sensor-evidence). Skill-library `verified=True` is observed-measurement provenance here, not proof of general utility. Full program-library promotion/ranking lifecycle remains uninspected. |
| OPERATE and TEST | `src/biofoundry/simulation.py`; `src/biofoundry/science.py` | Direct reads; [EPI-RTE-batch-measurement](#epi-rte-batch-measurement). Material-physics implementation is not fully audited; real-material accuracy cannot be concluded. |
| PROPOSE_RECIPE and COMBINE_DESIGN | `src/biofoundry/simulation.py`; `src/biofoundry/science.py` | Direct reads; [EPI-RTE-recipe-admission](#epi-rte-recipe-admission), [EPI-RTE-proposal-evaluation](#epi-rte-proposal-evaluation). These add evaluator and provenance routes not separated in runtime. |
| PUBLISH, DEPOSIT_INSIGHT and TEACH | `src/biofoundry/simulation.py`; `src/biofoundry/memory.py` | Direct reads; [EPI-RTE-insight-circulation](#epi-rte-insight-circulation). Message transport outside these bodies is supplied runtime coverage, not a full communication audit. |
| Retained excerpts and feedback-weighted retrieval | `src/biofoundry/memory.py`; `src/biofoundry/policies/llm.py`; `src/biofoundry/simulation.py` | Direct reads of selection and later executor outcome feedback; [EPI-RTE-memory-selection](#epi-rte-memory-selection). Full public BM25 implementation and all semantic-observation omission paths remain uninspected; no complete-packet fidelity claim. |
| BUILD, WRITE_PROGRAM, FORK_PROGRAM | `src/biofoundry/simulation.py`; `src/biofoundry/programs.py`; `src/biofoundry/artifacts.py` | Supplied [RT-RTE-program-install](runtime.md#rt-rte-program-install) and [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping); not independently audited here. |
| Scripted, human, live and environment actions | `src/biofoundry/server.py`; `game/session.py`; `src/biofoundry/env.py`; `src/biofoundry/policies/scripted.py` | Supplied [RT-RTE-direct-control](runtime.md#rt-rte-direct-control); model-schema conclusions do not extend to these routes. |
| replay, playback and counterfactual-replay | `src/biofoundry/cli.py`; `src/biofoundry/counterfactuals.py`; `src/biofoundry/playback.py` | Parser directly read; implementation account supplied by [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay). Playback presentation not audited; digest agreement is not semantic endorsement. |
| ecosystem-report and checkpoint/held-out evaluation | `src/biofoundry/cli.py`; `src/biofoundry/technology_ecology.py` | Report wrapper directly read; evaluator supplied by [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay). Reports consume results; no live plan-admission feedback established. |
| research-study, analyze-study, analyze-mobility, trace-report, benchmark | `src/biofoundry/cli.py` | Dispatch directly inspected; trace-report wrapper read. Study member selection, statistical inference, mobility and trace attribution internals not assessed. This prevents system-complete conclusions about evaluators or automatic successor selection. |
| technology-dossiers and technology-atlas | `src/biofoundry/cli.py`; `src/biofoundry/technology_visualization.py`; `src/biofoundry/technology_atlas.py` | Dispatch and wrappers directly read: optional image generation, embeddings and ranked shortlists are additional exposed routes. Downstream prompt construction, semantic fidelity, embeddings and image-model versions are uninspected; generated depictions cannot be certified as measured mechanisms. |
| world validate/describe, doctor and external world authoring | `src/biofoundry/cli.py`; `src/biofoundry/scenarios.py`; `.agents/skills/swarmworld-world-builder/SKILL.md` | Dispatch directly read; supplied [RT-RTE-scenario-admission](runtime.md#rt-rte-scenario-admission). Mechanical package acceptance differs from scientific validation or human review. |

This is a bounded epistemic assessment inside the whole-system source boundary, not an exhaustive semantic audit. Available but uninspected operations above preclude a system-wide negative about acceptance, criticism, knowledge production or adaptation. No supplied runtime record needs supersession: most new routes separate material parts of world stepping; memory selection and outcome feedback span planning and world stepping rather than being contained in either.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-empirical-knowledge](#epi-obj-empirical-knowledge) | See record | EmpiricalKnowledge | SRC-1, `src/biofoundry/knowledge.py` | Historical local evidence, not global current truth |
| [EPI-OBJ-experimental-batch](#epi-obj-experimental-batch) | See record | ExperimentalBatch | SRC-1, `src/biofoundry/science.py` | Simulated measurements; hidden target flag is not delivered privately |
| [EPI-OBJ-memory-record](#epi-obj-memory-record) | See record | MemoryRecord | SRC-1, `src/biofoundry/memory.py` | Text may be a claim, intention or policy; instances not supplied |
| [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues) | None necessarily; see record | Agent action queues | SRC-1, `src/biofoundry/policies/llm.py` | Executable action authority is not propositional warrant |
| [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program) | Not determinable for an unspecified program; see record | Artifact behavior program | SRC-1, `src/biofoundry/programs.py` | A controller may encode a theory but no instantiated theory is supplied |
| [RT-OBJ-scenario-prompt](runtime.md#rt-obj-scenario-prompt) | See record | Scenario agent instructions | SRC-1, `src/biofoundry/scenarios.py` | External authored premises and guidance, not episode-produced knowledge |
| [RT-CMP-configured-model](runtime.md#rt-cmp-configured-model) | Not individuated in accessible weights; see record | Configured provider model | SRC-1, `src/biofoundry/providers/openai_compatible.py` | Parametric provenance, exact version and internal updates uninspected |

## Authority-route ledger

Fields owned by a declaring record are incorporated by citation, not duplicated. Content/update relations below classify the indicated edge only. Architectural status refers to implementation, not observed activation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-sensor-evidence](#epi-rte-sensor-evidence) | content transformation | implemented | [EPI-OBJ-empirical-knowledge](#epi-obj-empirical-knowledge) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/knowledge.py` | none | none | Warrant restricted to simulator source and observation time |
| [EPI-RTE-batch-measurement](#epi-rte-batch-measurement) | check/evidence production | implemented | [EPI-OBJ-experimental-batch](#epi-obj-experimental-batch) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/science.py` | none | none | Arithmetic and state readout, conditional on engine premises |
| [EPI-RTE-batch-measurement](#epi-rte-batch-measurement) | retention | implemented | [EPI-OBJ-experimental-batch](#epi-obj-experimental-batch) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/simulation.py` | none | none | Measurement retention is not acceptance of an explanation |
| [EPI-RTE-recipe-admission](#epi-rte-recipe-admission) | disposition/acceptance | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/simulation.py` | none | none | Operational admission only; not truth acceptance |
| [EPI-RTE-proposal-evaluation](#epi-rte-proposal-evaluation) | check/evidence production | implemented | [EPI-OBJ-experimental-batch](#epi-obj-experimental-batch) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/science.py` | none | none | Matched material ablation, not agent/component causal attribution |
| [RT-RTE-model-planning](runtime.md#rt-rte-model-planning) | content transformation | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance) | SRC-1, `src/biofoundry/policies/llm.py` | [RT-CLM-grounded-science](runtime.md#rt-clm-grounded-science) | none | Hypothesis schema permits candidates, but no output proves entailment or non-entailment |
| [RT-RTE-model-planning](runtime.md#rt-rte-model-planning) | disposition/acceptance | implemented | [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues) | no content change | see record | see record | see record | see record | see record | see record | see record | see [RT-BAP-action-dispatch](runtime.md#rt-bap-action-dispatch) | SRC-1, `src/biofoundry/structured_output.py` | none | none | Shape/type admission is not empirical claim checking |
| [EPI-RTE-insight-circulation](#epi-rte-insight-circulation) | retention | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/simulation.py` | none | none | Prefixing/truncation can lose necessary scope; not guaranteed semantic preservation |
| [EPI-RTE-insight-circulation](#epi-rte-insight-circulation) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/simulation.py` | none | none | Public grounded-resource metadata can grant recipe eligibility, not truth of prose |
| [EPI-RTE-memory-selection](#epi-rte-memory-selection) | content transformation | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/memory.py` | none | none | Unstructured truncation can discard a negation or condition |
| [EPI-RTE-memory-selection](#epi-rte-memory-selection) | behavior/policy adaptation | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | non-truth-apt policy/content update: retrieval ranking statistics | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/memory.py` | none | none | Planning citations and later executor success update future ranking; credit is not causal identification |
| [RT-RTE-program-install](runtime.md#rt-rte-program-install) | behavior/policy adaptation | implemented | [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program) | non-truth-apt policy/content update: installed artifact instructions | see record | see record | see record | see record | see record | see record | see record | see [RT-BAP-program-execution](runtime.md#rt-bap-program-execution) | SRC-1, `src/biofoundry/programs.py` | none | none | Useful effect or theory content requires further evidence |
| [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay) | lineage/freshness/recovery | implemented | [EPI-OBJ-memory-record](#epi-obj-memory-record) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/counterfactuals.py` | none | none | Recorded-state warrant only; no new model reasoning |
| [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay) | check/evidence production | implemented | [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/biofoundry/technology_ecology.py` | [EPI-CLM-research-environment](#epi-clm-research-environment) | none | Conditional simulated comparison, no supplied actual trajectory |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-research-environment](#epi-clm-research-environment) | see record | SRC-1, `README.md`; doctrine/design | see record | [EPI-RTE-sensor-evidence](#epi-rte-sensor-evidence), [EPI-RTE-batch-measurement](#epi-rte-batch-measurement), [EPI-RTE-insight-circulation](#epi-rte-insight-circulation), [RT-RTE-program-install](runtime.md#rt-rte-program-install), [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay) | Uninspected; no supplied episodes | No actual intervention comparison; surrogate domain only | Implemented environment for measurement, exchange and persistent simulated control | Scientific discoveries, benefit, transfer and real-world mechanisms remain unestablished |
| [RT-CLM-grounded-science](runtime.md#rt-clm-grounded-science) | see record | SRC-1, `src/biofoundry/policies/llm.py`; doctrine/design | see record | [RT-RTE-model-planning](runtime.md#rt-rte-model-planning), [EPI-RTE-recipe-admission](#epi-rte-recipe-admission), [EPI-RTE-batch-measurement](#epi-rte-batch-measurement) | Uninspected | Resource grounding mechanically restricts recipes; it does not check arbitrary hypotheses | Guidance and bounded evidence access are wired | Do not upgrade a request against invented observations into a guarantee of truthful prose |

## Bounded conclusion

SwarmWorld acquires local simulator evidence and retains it for later model input. Observation-time labels preserve a bounded lineage; current possession and historical observation grant resource eligibility, not knowledge of an unobserved world. TEST reads simulated batch properties and computes a utility threshold; its private consumer receives measurements and utility but not the threshold flag. These are evidence-producing and arithmetic routes, not evidence-consuming acceptance of a newly proposed scientific explanation ([EPI-RTE-sensor-evidence](#epi-rte-sensor-evidence), [EPI-RTE-batch-measurement](#epi-rte-batch-measurement)).

A counterexample to “only TEST evaluates candidates” is proposal-time latent material evaluation, including leave-one-inherited-material-out comparisons. A counterexample to “publication merely stores text” is the way named, personally grounded resources become citation-based recipe eligibility. These routes carry real computational and operational authority, but their license is restricted respectively to the simulator's utility contrast and to provenance/resource admission. Neither establishes acceptance of the publication's prose or the causal explanation named by a model ([EPI-RTE-proposal-evaluation](#epi-rte-proposal-evaluation), [EPI-RTE-recipe-admission](#epi-rte-recipe-admission), [EPI-RTE-insight-circulation](#epi-rte-insight-circulation)).

Model-authored hypotheses and progress can be stored and delivered again. Their content relation is indeterminate without an output instance; a field named hypothesis does not prove an ampliative claim. Evidence IDs are filtered for availability, not for support. Public and taught records also gain later availability without a truth-acceptance gate in the inspected writers. No lifecycle integration *after epistemic acceptance* is established by those writers; retention, citation eligibility and prompt consumption are separate functions. A complete system-wide absence cannot be concluded because study selection, program-library curation and analysis routes remain partly uninspected ([RT-RTE-model-planning](runtime.md#rt-rte-model-planning), [EPI-RTE-insight-circulation](#epi-rte-insight-circulation)).

Retrieval implements evidence-responsive ranking updates even without a formulated theory. Selection and citation processing occur during planning; action-success counters update during subsequent world stepping and feed later retrieval. The full feedback route spans both phases, not just pre-inference planning. Its credit counts cite-and-succeed associations, not independent variation of the record or causal truth. Excerpts can discard semantic conditions, and subsequent context trimming can omit selected records entirely. The stored original survives, so read-back is possible but not guaranteed delivery in a particular invocation. These changes establish an adaptive selection capacity, not improved future performance, exercised reflection or exercised self-improvement ([EPI-RTE-memory-selection](#epi-rte-memory-selection)).

Programs have enforcing actuator authority after installation, while natural-language claims have interpretive force at model/human consumers. DSL validation licenses bounded execution, not usefulness; replay licenses agreement with compatible recorded state, not scientific correctness. Frozen-society assays can measure simulated service persistence and knockout contrasts, but the inspected episode path records their results rather than automatically selecting a successor controller. No inspected actual experiment supports a causal benefit claim ([RT-RTE-program-install](runtime.md#rt-rte-program-install), [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay), [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay)).

Theory-builder conditions, learning, reflection and autonomy remain independent. The model route affords localized hypothesis text and later persistence; content-dependent use, explicit blame-bearing criticism and criticism-led iteration remain uninspected, as recorded in [RT-RTE-model-planning](runtime.md#rt-rte-model-planning). Automatic scheduling is not evidence for those properties. Nothing in this account establishes weight updates: external parameter mutability remains uninspected independently of the implemented simulator-memory adaptation ([RT-CMP-configured-model](runtime.md#rt-cmp-configured-model)).

## Shared records

### Operative objects

#### EPI-OBJ-empirical-knowledge
Label: EmpiricalKnowledge

Identity: each agent's `EmpiricalKnowledge`, containing `CellEvidence` keyed by cell and extraction counters. Representational form: symbolic coordinates, resource/terrain/station enum values, times, masses and counts. Storage substrate: in-process dictionaries/counters, serializable through authoritative state. Candidate truth-apt content is that a cell had the recorded sensor values at the recorded tick, plus extraction-attempt outcomes. This is distinct from [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues): evidence rather than selected actions. No supplied object is its counterpart. SRC-1, `src/biofoundry/knowledge.py` supplies implementation.

> self.cells[y * self.width + x] = CellEvidence(
> --- `src/biofoundry/knowledge.py`

> "scope_note": "Unlisted materials are unobserved, not proven absent.",
> --- `src/biofoundry/knowledge.py`

#### EPI-OBJ-experimental-batch
Label: ExperimentalBatch

Identity: research-ledger microbatch, source recipe and `tests` entries; distinguish pending latent properties from tested readout and hidden `passes_material_target`. Form: symbolic structured recipe/ID/provenance plus numerical material properties and utility. Substrate: `ResearchLedger.batches`, `tests`, `proposals`, private notebook experiment-result JSON and events. Truth-apt candidates concern simulated batch properties and matched utility differences, not real materials. Unlike [RT-OBJ-artifact-program](runtime.md#rt-obj-artifact-program), this is measurement/evaluation state rather than installed behavior. No counterpart after comparison. SRC-1, `src/biofoundry/science.py` supplies implementation.

> Pending samples expose their identity and authored recipe, but not latent
> material properties or utility. Those values enter the view only after TEST.
> --- `src/biofoundry/science.py`

#### EPI-OBJ-memory-record
Label: MemoryRecord

Identity: ID-addressed text records consumed by private retrieval, teaching and public archive, including self-authored research state and insight text. Natural-language form for model interpretation; IDs, timestamps, kind and causal-parent fields are symbolic metadata. Storage substrate: working/episodic/notebook collections and `CulturalArchive.records`/`by_id`, with optional trace serialization. Candidate propositions depend on content; goal and action-intent strings need not be truth-apt. Text is not made warranted by `kind`, salience or citation. Distinct from [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues) and [RT-OBJ-scenario-prompt](runtime.md#rt-obj-scenario-prompt): use-generated retained content rather than executable queue or static instructions. SRC-1, `src/biofoundry/memory.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/simulation.py` supply implementation.

> f"Prior self-authored research state: {prior_state}\n{tail}"
> --- `src/biofoundry/policies/llm.py`

### Routes

#### EPI-RTE-sensor-evidence
Label: Sensor evidence acquisition
Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints: world/local artifact state → observation records and empirical cell evidence → knowledge view, retained notebook and optional measured program evidence. Owner: simulator and `EmpiricalKnowledge`. This is the sensing subroute, not a duplicate of the full step. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/knowledge.py`; implementation.

- Immediate return: INSPECT emits `sample_inspected`; `observe` updates the most recent cell value; `view` returns counts, bases and nearest historically observed sites.
- Later read-back: notebook observations can enter subsequent retrieval; cell evidence enters later knowledge views. Historical sites retain `last_seen_tick` and last-seen mass.
- Delegated visibility: agent-local sensor evidence, not authoritative global arrays; human/analysis events may expose more than private model packets.
- Selection predicate: INSPECT current tile and nearby active programmed artifacts within distance one; empirical view groups observed cells and matter backed by observation or conserved possession.
- Invalidation or expiry: revisiting a cell replaces that cell's latest evidence; historical evidence is not a freshness guarantee about current world mass.
- Activation or effect: implementation writes notebook evidence and may mark observed program knowledge `verified=True`; model reliance unobserved. `grounded_resources` later gates recipe eligibility.
- Evidence limits: simulator source warrant preserved as time/locality-labelled measurements, not independently checked against physical reality; full program-library verification consumers uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evaluator target/domain: local simulator cell and artifact values; program reads and numeric rounding, not model judgment. Force: measurement availability and enforcing resource eligibility through the recipe gate; program verification concerns measured observation. Consumer/channel/horizon: later `knowledge.view`, memory retrieval and the model prompt, advisory over subsequent macroturns; recipe checker consumes resource sets with enforcing force. No explanation accepted or integrated by this route. Recovery is new sensing or ordinary record retrieval; no universal withdrawal of stale claims is established.

> self.program_library.observe(
>     agent_id,
>     program.program_id,
>     tick=self.tick,
>     source="measured_artifact",
>     evidence_id=record_id,
>     verified=True,
>     measurements=measurement,
> )
> --- `src/biofoundry/simulation.py`

#### EPI-RTE-batch-measurement
Label: Batch measurement and retention
Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints: controller-authored OPERATE recipe → fabricated/staged microbatch → TEST newest pending sample → numeric result and private notebook. Owner: simulator and `ResearchLedger`. This part differs from general action execution by its measured target and private information boundary. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/science.py`; implementation.

- Immediate return: OPERATE emits sample identity/recipe/mass; TEST marks a batch tested and emits properties, utility and target-threshold result in the event.
- Later read-back: measured result retained in ledger and notebook, available to later private experiment view/retrieval. Source recipe is added to the test result when `experience_reuse` is enabled.
- Delegated visibility: private experiment view and notebook omit `passes_material_target`; events carry it. Pending samples do not reveal latent properties or utility through this view.
- Selection predicate: OPERATE requires recipe, suitable foundry/station/workspace, validated fabrication and feedstocks; TEST selects latest untested sample for that agent and rejects when none exists.
- Invalidation or expiry: testing consumes pending status, not the underlying result; old results remain historical tests rather than fresh observations.
- Activation or effect: fixed code computes numeric readout and threshold classification; later prompts can receive it, without demonstrated content dependence.
- Evidence limits: no executed sample; physics, encoding and utility adequacy not independently validated. A utility threshold is not acceptance of a causal theory.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target/domain: the particular simulated batch's property dictionary and utility under `ResearchLedger.material_utility`. Evaluator: fixed code and configured `target_material_utility`; comparison result licenses only that utility criterion at the test tick. Model/human/script proposes actions, software vetoes invalid execution; no reference scientific answer or per-content human approval. Mode: bounded simulated experiment. TEST does not install a recipe, approve a publication or automatically revise a hypothesis. Separate retention follows measurement without a named explanatory acceptance decision. Consumer/channel/force/horizon: private notebook/result view → future model prompt, advisory; research event/ledger → researcher reporting, descriptive. Recovery: fabricate/test another sample; no automatic scientific rollback.

> "passes_material_target": (
>     self.material_utility(batch.batch) >= self.config.target_material_utility
> ),
> --- `src/biofoundry/science.py`

> observable_result = {
>     key: value
>     for key, value in result.items()
>     if key != "passes_material_target"
> }
> --- `src/biofoundry/simulation.py`

#### EPI-RTE-recipe-admission
Label: Recipe provenance admission
Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints: PROPOSE_RECIPE/COMBINE_DESIGN → material validation, resource/provenance checks → recorded eligible proposal or rejection. Owner: simulator. This part handles eligibility, separately from [EPI-RTE-proposal-evaluation](#epi-rte-proposal-evaluation)'s utility calculations. SRC-1, `src/biofoundry/simulation.py`; implementation.

- Immediate return: `recipe_proposed`/`design_combined` event and notebook proposal, or validation error.
- Later read-back: retained design record can be retrieved; proposal ledger preserves recipe and parents.
- Delegated visibility: record says recipe validated; that means these admission checks, not empirical confirmation of a mechanism.
- Selection predicate: valid recipe; own observed/possessed resources or allowed cited resources; combined designs require multiple published parents, structured provenance and configured distinct grounded contributors.
- Invalidation or expiry: historical proposal remains; this method implements no empirical-failure withdrawal of its validation label.
- Activation or effect: gate permits/rejects the proposal and records parent-resource inheritance. Later fabrication/build checks are separate.
- Evidence limits: a grounded material name or multiple authors do not prove the parent statement true, independent evidence sources, or a useful composition.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target: recipe executability/provenance eligibility within collective science, not truth of prose. Proposal owner is selected model/human/script; fixed-rule software decides/vetoes, without a reference answer or required human approval. Guidance is the local material/manual constraint; what persists is recipe, IDs and validation result. Force is enforcing on this action. Consumer/channel/horizon: simulator proposal handler via resource sets/parent metadata, immediate action admission; retained labels later have interpretive force at model consumers. Recovery: revise recipe, obtain/observe inputs or cite eligible parents. No evidence-consuming acceptance of an ampliative explanatory claim occurs in this inspected gate.

> "COMBINE_DESIGN requires empirically grounded publications from at "
> f"least {self.config.science.minimum_contributors} distinct agents"
> --- `src/biofoundry/simulation.py`

> ungrounded = sorted(required - grounded, key=int)
> --- `src/biofoundry/simulation.py`

#### EPI-RTE-proposal-evaluation
Label: Proposal material evaluation
Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints: admitted normalized recipe → synthetic inventory execution → full utility and inherited-material ablations → proposal ledger. Owner: `ResearchLedger.propose`. Distinct check/evidence production within world stepping, not the eligibility gate. SRC-1, `src/biofoundry/science.py`; implementation.

- Immediate return: proposal includes `evaluation_utility` and optional `composition_synergy`.
- Later read-back: proposal ledger retains metrics for research-state/report consumers; the complete downstream scorecard/analysis consumer tree is uninspected here.
- Delegated visibility: authoritative evaluation is excluded from agent observation by design comment; private experiment view exposes measurements only after TEST. Proposal events are broader than that private view.
- Selection predicate: every admitted proposal; ablations only for combined proposals with inherited resource slots and a nonempty remaining recipe.
- Invalidation or expiry: historical proposal metrics persist; no automatic rejection or controller rollback based on negative synergy in this function.
- Activation or effect: computes full utility minus the strongest available leave-one-inherited-material-out utility under unchanged processing; writes result, not a live successor choice.
- Evidence limits: simulator derivation conditional on evaluator/recipe encoding. Ablation compares material inclusion, not the independent causal contribution of cited publications, communication or model intelligence. No observed comparison supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target/domain: utility contribution of inherited materials to the proposed recipe in the simulator. Fixed `MaterialLab` execution and `material_utility` form the evaluator; full recipe is the reference outcome, matched ablations are contrasts. Mode: bounded computational assay, not an empirical physical test. Consumer/channel/force/horizon: numeric proposal-ledger fields and events, descriptive to offline research; any further study selection remains uninspected. No criterion here licenses a new explanatory claim for reliance, and no performance-based acceptance is implemented in this function.

> composition_synergy = (
>     round(full_utility - max(ablation_utilities), 6)
>     if ablation_utilities
>     else None
> )
> --- `src/biofoundry/science.py`

> # Authoritative evaluation is never included in the agent observation.
> "evaluation_utility": round(full_utility, 6),
> --- `src/biofoundry/science.py`

#### EPI-RTE-insight-circulation
Label: Insight retention and circulation
Part of: [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Endpoints: controller insight/message → private notebook/spatial deposit → optional public archive and grounded-resource publication metadata; or TEACH retained record/program IDs/message → nearby recipients. Owner: simulator/archive. This is a retained-content subroute; program transfer is noted but its full library curation is not assessed. SRC-1, `src/biofoundry/simulation.py`, `src/biofoundry/memory.py`; implementation.

- Immediate return: deposited insight or knowledge-taught event; record is retained, publication adds archive entry and structured provenance.
- Later read-back: archive retrieval, recipients' notebooks and own memory can supply later model input. Combined design can consume publication resource metadata.
- Delegated visibility: deposited content is author-prefixed and limited to 1000 characters; TEACH copies selected retained records or supplies a fresh message when no records resolve. IDs/provenance remain metadata, not semantic verification.
- Selection predicate: nonempty insight; TEACH requires nearby addressed recipients and retained records/known programs or nonempty message. Public resource metadata attaches only personally grounded resource names found in publication text.
- Invalidation or expiry: archive deduplicates by record ID; inspected writer has no truth-based retraction, semantic supersession or publication expiry. Other uninspected routes prevent a global absence conclusion.
- Activation or effect: archive/notebook availability, optional immediate-replan interrupts, and enforcing cited-resource eligibility in COMBINE_DESIGN. Actual model reliance remains unobserved.
- Evidence limits: lexical mention plus personal resource grounding establishes resource provenance, not support for every assertion in the publication. Teaching does not upgrade warrant.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target/domain of admission: nonempty retained content and transfer/publication eligibility. Model/human/script authors; software decides these conditions, not propositional truth; no answer oracle or per-content human approval required. Guidance originates in action manual and controller intent. Consumer/channel/force/horizon: model via retained text, advisory across macroturns; simulator recipe checker via `grounded_resources`, enforcing for later combined proposals; replanning scheduler via boolean interrupts, permissive for later scheduling. Retention precedes epistemic acceptance; no post-acceptance lifecycle integration established. Recovery is subsequent content/action, not automatic scientific rollback.

> content=f"{agent_id} | {content[:1000]}",
> --- `src/biofoundry/simulation.py`

> normalized = content.casefold().replace("_", " ")
> personal = self.grounded_resources(index, include_shared_depot=False)
> return {
>     resource
>     for resource in personal
>     if self.resource_name(resource).casefold().replace("_", " ") in normalized
> }
> --- `src/biofoundry/simulation.py`

> for recipient in recipients:
>     for record in records:
>         self.memories[recipient].remember(record, notebook=True)
> --- `src/biofoundry/simulation.py`

#### EPI-RTE-memory-selection
Label: Memory excerpt and adaptive selection

Endpoints: prior research state/pending requests/local observation → query → scored retained records → bounded excerpts → optional packet trimming → model input; accepted citations update use statistics during planning, and subsequent world stepping updates action-outcome statistics that feed later rankings. Owner: `AgentMemory`, LLM policy and simulator feedback writer. This route spans [RT-RTE-model-planning](runtime.md#rt-rte-model-planning) and [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping), overlapping their selection/citation and executor-feedback stages respectively. It is not contained in either runtime route and does not duplicate either full route. It also overlaps [MEM-RTE-retrieval-feedback](memory.md#mem-rte-retrieval-feedback) in the selection/use/outcome feedback chain, while additionally tracing excerpt transformation and packet omission; the overlapping feedback mechanism has the same identity, not an independent evaluator. SRC-1, `src/biofoundry/memory.py`, `src/biofoundry/policies/llm.py`, `src/biofoundry/simulation.py`; implementation.

- Immediate return: retrieval returns ranked records and diagnostics and updates selection counts; packet construction renders bounded excerpts; accepted citation processing updates use counts during planning. Later `_record_action_outcome` calls in world stepping separately update outcome counts after planning has committed its queue.
- Later read-back: retained statistics change adaptive retrieval on later invocations; records omitted from a prompt remain in stores and can be retrieved again.
- Delegated visibility: model sees only remaining excerpts after trimming, with record ID/kind/tick; full retained source remains outside the message window. A selected diagnostic is not proof of delivery after trimming.
- Selection predicate: deduplicated notebook/episodic records, lexical score plus salience and tiny recency term; when `experience_attention` enables adaptation, citation/success feedback and exploration bonus modify ranking. Budget trimming drops memory entries from the end first.
- Invalidation or expiry: selection is per invocation; statistics persist in the in-process agent memory. Excerpting leaves source content unchanged; model conversation is rebuilt, not accumulated.
- Activation or effect: selection/use statistics from planning and action-success statistics from subsequent simulator execution feed fixed-rule ranking on later retrievals. Packet trimming then determines which selected excerpts reach the model. Actual dependence of subsequent model behavior and performance is unobserved.
- Evidence limits: cited-parent success is an association, not an intervention; ranking neither certifies truth nor preserves all conditions in truncated text. Full stored record provenance varies by producer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target/domain: retrieval relevance and heuristic past-use feedback, not propositional truth. Software chooses ranking and omissions; controller supplies citations; simulator supplies action success. No expected-answer oracle. Force: ranking at retriever, enforcing omission at packet builder, advisory at model; horizon later decisions within the agent's retained-state lifetime. Direct behavior/policy adaptation is the ranking-state update across planning and subsequent executor feedback, consumed by later retrieval. The inspected CLI commits planning and takes queued actions before `simulation.step(actions)`; `_record_action_outcome` then calls `mark_causal_outcome`, so outcome credit is not a planning-stage result. SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/simulation.py`, `src/biofoundry/memory.py`. No improved capacity or exercised self-improvement established: objective-aligned determination and causal dependence of subsequent live behavior are not demonstrated. Underlying model parameter fixity is separate.

Concrete deterministic transformation (implementation deduction, no execution): a non-JSON record `Yield is high only after heating` at `max_characters=38` has length 32 and is returned intact. The same record at budget 25 takes the non-JSON truncation branch: the retained prefix has one character, so output is `Y...[bounded excerpt]`. The original necessary condition is no longer conveyed. This branch is therefore not guaranteed non-ampliative semantic reshaping; for arbitrary records the truth-apt relation is indeterminate. Structured artifact-measurement excerpts also project out service details, keeping artifact ID, program ID and performance before any final clipping. The remaining classifications require actual input/output propositions and their interpretation, not merely a text label.

> return content[: max(0, max_characters - 24)] + "...[bounded excerpt]"
> --- `src/biofoundry/memory.py`

> feedback = 0.5 * citation_rate + 0.5 * (
>     causal_success_rate if outcome_attempts else 0.0
> )
> --- `src/biofoundry/memory.py`

> self.memories[index].mark_causal_outcome(
>     set(map(str, action.causal_parents)), success=success
> )
> --- `src/biofoundry/simulation.py`

The model-planning container also filters proposed research-state evidence IDs by retained availability before storage. The predicate checks resolvability, not whether a cited item supports the hypothesis; this bounds the lineage license of the retained text.

> retained_evidence = {
>     str(record_id)
>     for record_id in research_state.get("evidence_ids", [])
>     if simulation.memories[index].get(str(record_id)) is not None
>     or str(record_id) in simulation.archive.by_id
>     or simulation.program_library.knows(agent_id, str(record_id))
> }
> --- `src/biofoundry/policies/llm.py`

### Claims

#### EPI-CLM-research-environment
Label: Scientific research environment

Claim: SwarmWorld offers a deterministic environment for studying model societies discovering, testing, exchanging, inheriting and embodying technology. SRC-1, `README.md`; doctrine/design. Distinct from [RT-CLM-grounded-science](runtime.md#rt-clm-grounded-science), which is a model instruction against invented observations; this claim concerns the environment's scope. It does not itself assert accepted explanatory truth or physical-world validity.

> SwarmWorld is a deterministic research environment for studying how societies of
> language-model agents discover, test, exchange, inherit, and physically embody
> technologies in a shared world.
> --- `README.md`

### Behavioral-authority paths

none declared in this member
