---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Voyager's task judgments, model-generated guidance and retained executable skills: evidence, acceptance and later authority at the frozen revision."
run-id: AAS-2026-10-14-voyager-f16a44a0cfe3-01
reviewed-boundary: "55e45a880755d0c8c66ca7fb5fe7962ac8974f89"
---

# Voyager epistemic report

## Source-and-claim boundary

The question is what Voyager can establish from game feedback, what it merely proposes, and how either affects subsequent action. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is [its Source register](boundary.md#source-register), SRC-1. The boundary includes learning, resume, inference, retained libraries, prompts, primitives and the execution bridge. External game and provider implementations remain excluded. No target execution was performed. All new findings below are implementation or doctrine/design findings, not observed operation.

The runtime account is provisional evidence of wiring, not an inspection limit. Direct reads added the complete critic and skill manager, curriculum observation rendering and QA/progress/decomposition methods, action rendering/parser/chest methods, driver step, Node step/cleanup/endpoints, concrete status/inventory/voxel/chest observations, setup metadata, QA/skill/critic prompts, README and the sampled wood-log program. The source tree was checked at the reviewed commit. These are further SRC-1 reads, not new sources.

| Entry point or operation | Source path | Coverage and records, or limit |
|---|---|---|
| Package invocation and configuration | `setup.py`, `README.md`, `voyager/voyager.py` | Direct setup/README read: setup declares no console-script dispatch; shipped invocation is the Python API. Driver wiring supplied by [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop). |
| Learning, reset, step, rollout, resume | `voyager/voyager.py` | Direct step read plus supplied [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission). |
| Decomposition and inference, including caller subgoals | `voyager/agents/curriculum.py`, `voyager/voyager.py` | Direct decomposition method and supplied [RT-RTE-task-inference](runtime.md#rt-rte-task-inference); JSON parsing checks shape, not logical adequacy. |
| Auto/manual task and judgment dispatch | `voyager/agents/critic.py`, `voyager/agents/curriculum.py` | Direct critic and supplied [RT-RTE-task-selection](runtime.md#rt-rte-task-selection), [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment). |
| QA generation/cache/context and filtered delivery | `voyager/agents/curriculum.py` | Direct [EPI-RTE-qa-context](#epi-rte-qa-context). |
| Observation hooks, inventory and biome transformations | `voyager/env/mineflayer/lib/observation/base.js`, `voyager/env/mineflayer/lib/observation/inventory.js`, `voyager/env/mineflayer/lib/observation/status.js`, `voyager/env/mineflayer/lib/observation/voxels.js`, `voyager/agents/curriculum.py` | Direct [EPI-RTE-observation-context](#epi-rte-observation-context). |
| Chest update, invalidation and later judgment supply | `voyager/env/mineflayer/lib/observation/chests.js`, `voyager/agents/action.py` | Direct [EPI-RTE-chest-updates](#epi-rte-chest-updates). |
| Parser, revision feedback and chat-rule extraction | `voyager/agents/action.py`, `voyager/voyager.py` | Direct reads; supplied [RT-OBJ-program-code](runtime.md#rt-obj-program-code), [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance). |
| Skill description, replacement, retrieval and all-skill execution supply | `voyager/agents/skill.py`, `voyager/prompts/skill.txt` | Direct [EPI-RTE-skill-description](#epi-rte-skill-description); supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution). |
| Progress cleanup and failure withdrawal | `voyager/agents/curriculum.py` | Direct [EPI-RTE-progress-cleanup](#epi-rte-progress-cleanup). |
| Direct `/step`, error handling, assistance, `/start`, `/pause`, `/stop` | `voyager/env/mineflayer/index.js`, `voyager/env/bridge.py` | Direct step/cleanup/pause/stop read; supplied start/bridge tracing in [RT-RTE-environment-step](runtime.md#rt-rte-environment-step). No separate registered-tool approval layer appears in that route. |
| Primitive implementation, bundled collection plugin, recorder summaries | `voyager/control_primitives/`, `voyager/env/mineflayer/mineflayer-collectblock/`, `voyager/utils/record_utils.py` | Runtime supplies sampled mining and recorder findings. Other individual algorithms remain unassessed here; no system-complete negative about internal checks, all derivations or all recovery is licensed. |
| Distributed skill libraries | `skill_library/trial1/skill/code/mineWoodLog.js`, `skill_library/` | Direct sampled code, initial coverage in boundary. Other code/description/index contents unassessed; cannot enumerate their truth-apt assertions or establish library-wide quality or provenance. |
| Model/embedding state | `voyager/agents/`, `voyager/voyager.py` | Supplied component records below; external weights and training history inaccessible. No conclusion about provider-internal learning or reasoning. |

Consequential public claims are [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning), [EPI-CLM-self-verification](#epi-clm-self-verification) and [EPI-CLM-skill-transfer](#epi-clm-skill-transfer). Missing execution evidence prevents a finding that these routes actually generated, checked or improved a particular shipped skill. Missing intervention/comparison evidence prevents causal attribution of the README's performance to a component. Missing external dependency and model identities prevent exact reproduction and assessment of provider-internal warrant. No independent reference-answer source is registered.

## Epistemic-object inventory

Fields owned by another record are cited, not reconstructed as competing declarations.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-program-code](runtime.md#rt-obj-program-code) | Executable policy, not by itself an assertion that the program works; comments/embedded assertions require individual inspection | see cited record | SRC-1, `voyager/agents/action.py` | A passed task does not establish general function correctness. Sampled wood-log code conditionally explores/mines and can return without mining; a definition alone is no success trace. |
| [RT-OBJ-control-primitives](runtime.md#rt-obj-control-primitives) | Mostly executable policy; completeness of embedded truth-apt claims not determinable here | see cited record | SRC-1, `voyager/control_primitives/__init__.py` | Sampled implementation is not exhaustive plugin verification. |
| [EPI-OBJ-observation](#epi-obj-observation) | Reported item counts, location, nearby block types, equipment, biome and task-state evidence | see cited record | SRC-1, `voyager/env/mineflayer/lib/observation/inventory.js` | Current-window inventory and heuristic biome labels narrow the apparent observation semantics. |
| [EPI-OBJ-qa-cache](#epi-obj-qa-cache) | Model answers about Minecraft, including possible Unknown answers | see cited record | SRC-1, `voyager/agents/curriculum.py` | No answer-validation branch in inspected QA methods; embeddings do not validate truth. |
| [EPI-OBJ-chest-memory](#epi-obj-chest-memory) | Stored position-to-items/Unknown reports | see cited record | SRC-1, `voyager/agents/action.py` | Historical reports, not continuous inspection or universal freshness. |
| [EPI-OBJ-skill-description](#epi-obj-skill-description) | Model characterization of what a program does | see cited record | SRC-1, `voyager/agents/skill.py` | Generated after task judgment; description is not checked by that earlier judgment. |
| [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment) | Success proposition for a named task, and critique | see cited route for returned values | SRC-1, `voyager/agents/critic.py` | Model/human result, not independent ground truth; reasoning field is not returned by auto implementation. |
| [EPI-RTE-progress-cleanup](#epi-rte-progress-cleanup) | Completed/failed task history | see cited route | SRC-1, `voyager/agents/curriculum.py` | Task strings plus judgments, not a causal history of code achievement. |
| [RT-CMP-action-llm](runtime.md#rt-cmp-action-llm), [RT-CMP-curriculum-llm](runtime.md#rt-cmp-curriculum-llm), [RT-CMP-qa-llm](runtime.md#rt-cmp-qa-llm), [RT-CMP-critic-llm](runtime.md#rt-cmp-critic-llm), [RT-CMP-skill-llm](runtime.md#rt-cmp-skill-llm), [RT-CMP-openai-embeddings](runtime.md#rt-cmp-openai-embeddings) | Individuated propositions in distributed parameters: not determinable | see each cited component | SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py` | Client requests do not expose weight content, immutable versions or provider-internal change. |

## Authority-route ledger

Each compact entry separates a consequential function. Repeated citations denote different functions of one canonical route, not new route identities. All are implementation findings; activation is conditional and unobserved unless a field explicitly says otherwise.

Route ID: [EPI-RTE-observation-context](#epi-rte-observation-context)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-observation](#epi-obj-observation).
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown for actual game state, bounded to external bot/window data.
Transition or check target: external bot/game representations to observation events and model-visible text.
Evaluator/condition and domain: deterministic collection/formatting, not a truth evaluator; see route for exact transformations.
Activation and timing: observations after execution and during context rendering.
Possible or observed result: counts, block-type sets and filtered labels, not observed results here.
Implemented force: supply to model judgment and planning.
Epistemic authority and scope: reports of the exposed interface, not independently authenticated world measurements or causal achievements.
Operational authority: planning and task checking can consume these reports.
Behavioral-authority path: critic/action/curriculum via rendered messages; advisory input until judgment becomes enforcing; current and subsequent attempts.
Evidence source ID and local anchor: SRC-1, `voyager/env/mineflayer/lib/observation/inventory.js`, `voyager/agents/curriculum.py`; see cited record.
Claim IDs or none: [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: potential observation-scope mismatch.
Gap/limit: held-window contents can be called Inventory; absence of selected surface blocks can relabel the biome underground without establishing that physical claim.

Route ID: [RT-OBJ-program-code](runtime.md#rt-obj-program-code), [RT-RTE-environment-step](runtime.md#rt-rte-environment-step)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-program-code](runtime.md#rt-obj-program-code).
Content/update relation: no content change.
Transition or check target: function syntax/shape at parser; execution completion or exception in Node. These are different domains of the same action progression.
Evaluator/condition and domain: see parser and execution records; Babel shape checks and Node execution, not program-purpose validation.
Activation and timing: before execution for parser; during execution for errors.
Possible or observed result: parsed declarations/main call or parse error; execution result/error events.
Implemented force: parser failure withholds ordinary action execution; direct environment invocation bypasses it.
Epistemic authority and scope: syntax/shape and encountered execution outcomes only; no general safety, goal success or reuse license.
Operational authority: accepted functions may execute before task judgment.
Behavioral-authority path: Python parser result to bridge/eval, enforcing on normal action route for that attempt; direct endpoint remains alternate.
Evidence source ID and local anchor: SRC-1, `voyager/agents/action.py`, `voyager/env/mineflayer/index.js`; see cited records.
Claim IDs or none: [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: policy instructions exceed parser enforcement, as runtime records.
Gap/limit: code generation is policy production; explanatory prose is not an admitted knowledge object merely because it accompanies code.

Route ID: [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: success/critique returned by cited record.
Content/update relation: truth-apt transformation: indeterminate; a requested model/human judgment is not an inspected inference trace. Entailed assessment versus ampliative diagnosis requires an actual response and warranted inputs.
Transition or check target: whether selected final-state evidence meets named Minecraft task/context requirements, not whether code caused it or transfers safely.
Evaluator/condition and domain: see cited record; auto critic uses heuristics in prompt; manual human confirms independently of auto veto.
Activation and timing: after an executed parsed action and chest update, before optional failed-placement recovery.
Possible or observed result: success/failure plus critique; automatic error/parse failures produce false.
Implemented force: produces result; disposition is the next ledger entry.
Epistemic authority and scope: fallible task-completion judgment against selected observations.
Operational authority: result is available to retry/admission consumers; no separate enforcement inside the model.
Behavioral-authority path: critic return to Python step; immediate task horizon; see cited route.
Evidence source ID and local anchor: SRC-1, `voyager/agents/critic.py`, `voyager/prompts/critic.txt`.
Claim IDs or none: [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: final-state proxy is not process verification.
Gap/limit: inventory may pre-exist; nearby wheat need not have been planted by this action; server assistance precedes final observations. These are source-supported countercases to causal-success inference, not observed errors.

Route ID: [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment), [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: task success result and [RT-OBJ-program-code](runtime.md#rt-obj-program-code).
Content/update relation: no content change.
Transition or check target: task completion for ending rollout; successful last program for learning admission, except deposit tasks.
Evaluator/condition and domain: critic/human decides task success; Python consumes it. Manager does not independently validate it; see cited records.
Activation and timing: each executed attempt; learning success branch only for skill admission.
Possible or observed result: terminate task and admit code, or retry/stop at limit; direct manager calls bypass success gate.
Implemented force: enforcing at driver branch, permissive for later retention.
Epistemic authority and scope: evidence-consuming task acceptance under the prompt's criteria for task progression; no acceptance of general code correctness, description truth, explanation or transfer.
Operational authority: success permits learning retention; failure does not automatically evict previously retained skills.
Behavioral-authority path: critic result through Python `success` branch to rollout termination/admission; task and later-library horizon; see records.
Evidence source ID and local anchor: SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`.
Claim IDs or none: [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning), [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: task acceptance narrower than reusable-skill warrant.
Gap/limit: manual human can approve after renderer returns None; error veto is not system-wide. Inference does not call skill admission.

Route ID: [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment), [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: critique, last program and new action request.
Content/update relation: non-truth-apt policy/content update: requests revised executable behavior; actual generated revision unobserved.
Transition or check target: failed or incomplete task attempt to next model call.
Evaluator/condition and domain: critique from model/human plus current observations; no independent revision-quality check beyond next execution/judgment.
Activation and timing: next attempt while rollout continues.
Possible or observed result: changed program request; actual compliance not established.
Implemented force: advisory guidance, not enforced repair.
Epistemic authority and scope: diagnosis is candidate guidance, not validated explanation of failure.
Operational authority: next action may execute a newly parsed program.
Behavioral-authority path: two-message replacement to action model, advisory for next attempt; see records.
Evidence source ID and local anchor: SRC-1, `voyager/voyager.py`, `voyager/agents/action.py`.
Claim IDs or none: [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: requested improvement versus demonstrated improvement.
Gap/limit: no observed critique/revision pair; no theory-builder classification inferred from the word critic.

Route ID: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-program-code](runtime.md#rt-obj-program-code), [EPI-OBJ-skill-description](#epi-obj-skill-description).
Content/update relation: no content change.
Transition or check target: current program and new description to active map/files/vector index.
Evaluator/condition and domain: see cited route; task success upstream, count assertions locally.
Activation and timing: successful learning admission, or direct manager call, excluding deposit tasks.
Possible or observed result: new entry or active same-name replacement; versioned text files retained.
Implemented force: persistent admission without separate regression check.
Epistemic authority and scope: retained candidate capability, not a theorem that it works in every future state.
Operational authority: future prompt selection and executable definition supply.
Behavioral-authority path: see [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution); future tasks, resume and imported libraries.
Evidence source ID and local anchor: SRC-1, `voyager/agents/skill.py`.
Claim IDs or none: [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning), [EPI-CLM-skill-transfer](#epi-clm-skill-transfer).
Mismatch marker or none: replacement counters a literal always-growing membership claim.
Gap/limit: writes/index counts do not establish semantic agreement or atomic rollback. No failed-transfer withdrawal branch found in inspected manager/driver.

Route ID: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution), [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: retained skill code, indexed through [EPI-OBJ-skill-description](#epi-obj-skill-description).
Content/update relation: no content change.
Transition or check target: semantic description query to top-k code; entire loaded library to executor.
Evaluator/condition and domain: vector similarity ranks descriptions, not truth or executable fitness; generated calls determine invocation.
Activation and timing: action reset/refresh and every execution.
Possible or observed result: selected examples in prompt and all loaded definitions in eval.
Implemented force: ranking for prompt; executable definitions for Node.
Epistemic authority and scope: relevance ranking only, not endorsement or a new acceptance decision.
Operational authority: retained functions can affect later tasks without a per-skill revalidation gate.
Behavioral-authority path: see cited behavioral-authority records for consumers/channel/horizons.
Evidence source ID and local anchor: SRC-1, `voyager/agents/skill.py`, `voyager/voyager.py`.
Claim IDs or none: [EPI-CLM-skill-transfer](#epi-clm-skill-transfer).
Mismatch marker or none: prompt top-k is not execution admission control.
Gap/limit: distributed library presence proves availability only, not routes that produced it or future benefit.

Route ID: [EPI-RTE-qa-context](#epi-rte-qa-context)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-cache](#epi-obj-qa-cache).
Content/update relation: truth-apt transformation: indeterminate; model request produces candidate answers without an inspectable derivation. Specific answers may be imported model knowledge, reshaping or ampliative conjecture; response/provenance needed to decide.
Transition or check target: task/question to answer and guidance.
Evaluator/condition and domain: model supplies own Minecraft knowledge; prompt requests Unknown for uncertainty, not external verification.
Activation and timing: cache misses and curriculum QA; see route.
Possible or observed result: raw answer text or reused cached answer; no observed answer instance here.
Implemented force: guidance supplied without a truth gate.
Epistemic authority and scope: candidate Minecraft advice; underlying source warrant unknown.
Operational authority: context can influence task selection/actions.
Behavioral-authority path: QA return into curriculum/action messages; advisory; current and future tasks after reload.
Evidence source ID and local anchor: SRC-1, `voyager/agents/curriculum.py`, `voyager/prompts/curriculum_qa_step2_answer_questions.txt`.
Claim IDs or none: none.
Mismatch marker or none: task question can lose semantic specificity.
Gap/limit: static example `Mine iron_ore.` becomes `How to mine iron in Minecraft?`; this is not a guaranteed equivalent question about ore mining.

Route ID: [EPI-RTE-qa-context](#epi-rte-qa-context)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-cache](#epi-obj-qa-cache).
Content/update relation: no content change.
Transition or check target: generated answer to cache/index/files.
Evaluator/condition and domain: cache miss, duplicate assertion and persistence, not a truth criterion.
Activation and timing: immediately after answer generation.
Possible or observed result: durable question/answer and question embedding.
Implemented force: retention, not epistemic acceptance.
Epistemic authority and scope: no additional warrant from persistence.
Operational authority: retained answer can later be delivered without another model answer call.
Behavioral-authority path: cache lookup to task context/curriculum prompts, advisory, cross-task/resume horizon; see record.
Evidence source ID and local anchor: SRC-1, `voyager/agents/curriculum.py`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: similarity reuse can substitute a neighboring question; Unknown/language-model filters apply to curriculum delivery, not cache admission or all task contexts.

Route ID: [EPI-RTE-qa-context](#epi-rte-qa-context)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-cache](#epi-obj-qa-cache).
Content/update relation: no content change.
Transition or check target: exact task-context lookup or nearest-question reuse and filtered curriculum supply.
Evaluator/condition and domain: code key equality, similarity threshold and string filters; see record.
Activation and timing: subsequent task context or curriculum render.
Possible or observed result: reused answer, or excluded curriculum pair; maximum five supplied curriculum pairs.
Implemented force: ranking/filtering of guidance, not answer validation.
Epistemic authority and scope: remembered answer remains a candidate.
Operational authority: action/curriculum models may follow it.
Behavioral-authority path: see record; advisory natural-language supply over current and resumed tasks.
Evidence source ID and local anchor: SRC-1, `voyager/agents/curriculum.py`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: low vector distance does not establish question equivalence or answer transfer.

Route ID: [EPI-RTE-skill-description](#epi-rte-skill-description)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-skill-description](#epi-obj-skill-description).
Content/update relation: truth-apt transformation: indeterminate; requested code summary may preserve, omit or add conditions, and semantic fidelity is not checked.
Transition or check target: program code/main name to description.
Evaluator/condition and domain: description model, not an evaluator of its own summary.
Activation and timing: after successful learning judgment, before persistence.
Possible or observed result: generated function-shaped description text.
Implemented force: embedding input controlling retrieval rank.
Epistemic authority and scope: characterization candidate, not a post-generation accepted claim.
Operational authority: later code-selection influence through description embedding.
Behavioral-authority path: model text to index to top-k retrieval to action model; ranking then advisory, later-task horizon.
Evidence source ID and local anchor: SRC-1, `voyager/agents/skill.py`, `voyager/prompts/skill.txt`.
Claim IDs or none: [EPI-CLM-skill-transfer](#epi-clm-skill-transfer).
Mismatch marker or none: preceding code success does not validate subsequent summary.
Gap/limit: no supplied description-generation trace or summary comparison.

Route ID: [EPI-RTE-chest-updates](#epi-rte-chest-updates)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-chest-memory](#epi-obj-chest-memory).
Content/update relation: truth-apt transformation: acquisition/import; external event warrant unknown, explicit Invalid removes reliance.
Transition or check target: observed position/items/Unknown/Invalid to active chest map.
Evaluator/condition and domain: close/remove events and Python update rules; not a global freshness evaluator.
Activation and timing: event callbacks and post-execution chest update before critic.
Possible or observed result: replace item dict, add unknown chest, remove explicitly invalid position; persist and render.
Implemented force: active-map withdrawal and subsequent evidence supply.
Epistemic authority and scope: last supplied local chest information, with Unknown explicit; not a continuously current world catalog.
Operational authority: critic and planners consume revised chest information.
Behavioral-authority path: event map to JSON/reload/render to critic/action/curriculum; advisory evidence, task and resume horizon.
Evidence source ID and local anchor: SRC-1, `voyager/agents/action.py`, `voyager/env/mineflayer/lib/observation/chests.js`.
Claim IDs or none: [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: no global stale-state exclusion.
Gap/limit: absence from a new nearby scan is not coded as invalidation of all old entries.

Route ID: [EPI-RTE-progress-cleanup](#epi-rte-progress-cleanup)
Route function: lifecycle integration
Architectural status: implemented
Object/candidate ID: accepted task-completion judgments, not generally accepted skill-correctness claims.
Content/update relation: truth-apt transformation: non-ampliative reshaping; deduplicates completed task strings and removes matching failure labels.
Transition or check target: task judgment to organized progress history.
Evaluator/condition and domain: success branch and literal task-string equality.
Activation and timing: progress update after learning/inference rollout; deposit tasks skipped.
Possible or observed result: persisted completed/failed histories with completed taking precedence.
Implemented force: changes later progress/context and inference index.
Epistemic authority and scope: integration of accepted task status only, not resolution of contradictory causal histories or skill regression testing.
Operational authority: subsequent curriculum and inference sequencing change.
Behavioral-authority path: histories to curriculum context/progress; advisory in planning, enforcing index in inference; cross-task/resume horizon.
Evidence source ID and local anchor: SRC-1, `voyager/agents/curriculum.py`.
Claim IDs or none: [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning).
Mismatch marker or none: failure evidence can disappear from active task history without an explanatory comparison.
Gap/limit: removes task-string failure membership, not underlying event logs or retained failing code.

Route ID: [RT-RTE-environment-step](runtime.md#rt-rte-environment-step)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: final observation and failed-attempt state.
Content/update relation: non-truth-apt policy/content update: server assistance and optional placement recovery change the world before later reliance.
Transition or check target: execution to assisted final state; after failure, placement recovery to next action context.
Evaluator/condition and domain: server `returnItems`, unsticking, and driver failure/placement rules; not a causal achievement evaluator.
Activation and timing: server assistance before final observe/critic; optional placement recovery after critic failure.
Possible or observed result: given items/teleport; selected inventory/voxel fields replaced for next context.
Implemented force: direct world effects and modified context, not an atomic rollback.
Epistemic authority and scope: resulting state is not evidence of unaided generated-code achievement.
Operational authority: later behavior proceeds from assisted/recovered state.
Behavioral-authority path: server/game to observations, then critic/action; direct effect then advisory evidence; current/next attempt.
Evidence source ID and local anchor: SRC-1, `voyager/env/mineflayer/index.js`, `voyager/voyager.py`; supplied execution route plus direct reads.
Claim IDs or none: [EPI-CLM-self-verification](#epi-clm-self-verification).
Mismatch marker or none: process attribution would exceed checked evidence.
Gap/limit: real synchronization and actual assistance activation unobserved.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-learning-loop](runtime.md#rt-rte-learning-loop), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | none supplied | No later-use intervention; no immutable provider weights | Implemented task-evidence-conditioned capability retention and later authority, not demonstrated capacity gain | No weight training wired does not negate nonparametric learning capacity. |
| [EPI-CLM-self-verification](#epi-clm-self-verification) | see record | SRC-1, `README.md`; doctrine/design and reported operation | see record | [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment), [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance), [RT-RTE-environment-step](runtime.md#rt-rte-environment-step) | none supplied | Final-state proxy cannot isolate action causality; no component intervention | Feedback, execution errors and fallible model/human task checking are wired into another action request | Reliable self-verification/program improvement unestablished; manual modes qualify no-human scope. |
| [EPI-CLM-skill-transfer](#epi-clm-skill-transfer) | see record | SRC-1, `README.md`; doctrine/design and reported operation | see record | [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-RTE-task-inference](runtime.md#rt-rte-task-inference), [EPI-RTE-skill-description](#epi-rte-skill-description), [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution) | shipped library instances, not production/reuse traces | No benchmark artifacts or intervention; active name replacement and admission bypass qualify literal growth/validation | Executable composition/retrieval and imported-library inference are supported architecture | Generalization, comparative benefit, rapid compounding and forgetting mitigation remain reported, not established here. |

## Bounded conclusion

Voyager has an evidence-consuming **task-acceptance** route, not just retrieval. Its critic compares selected final-state observations with a named task/context; Python consumes the result to stop or retry, and learning success permits retention of the final program. The criterion and intended use are task requirements for task progression, under prompt-specific inventory/equipment/nearby-block heuristics. The result does not warrant that the program caused the state, is generally correct or transfers. Manual approval is a genuine alternate authority path; automatic error rejection is not universal. See [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment) and [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission).

The acquired evidence has local qualifications. Inventory sums item counts from the active window when one is open; curriculum can relabel biome based on missing surface block types. Chest state is revised or withdrawn by explicit events but otherwise persists. External bot/game truth and timing remain unverified. Rendering does not preserve a uniform world-state warrant across every field; see [EPI-RTE-observation-context](#epi-rte-observation-context) and [EPI-RTE-chest-updates](#epi-rte-chest-updates). Deterministic aggregation and deduplication establish bounded reshaping under inspected rules, not a new empirically warranted Minecraft generalization.

QA answers and skill descriptions are distinct truth-apt candidate routes. QA is generated/reused, cached and delivered as guidance without an inspected evidence-consuming truth acceptance decision. Skill descriptions are generated after code admission has already been licensed and determine later retrieval ranking without a fidelity test. Actual content transformations beyond the deterministic wrappers are indeterminate without response evidence. No accepted ampliative claim is demonstrated by those retention operations. See [EPI-RTE-qa-context](#epi-rte-qa-context) and [EPI-RTE-skill-description](#epi-rte-skill-description).

Accepted task judgments are integrated into progress histories, with completed strings overriding prior failure membership. Retained code has a different authority: selected examples influence the action model, while all loaded definitions enter Node execution. Same-name replacement is not regression adjudication, and a later failed task does not by itself withdraw the old skill in inspected manager/driver methods. See [EPI-RTE-progress-cleanup](#epi-rte-progress-cleanup), [RT-BAP-action-guidance](runtime.md#rt-bap-action-guidance) and [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution).

Feedback-conditioned next-action requests and task-conditioned library changes support implemented adaptation independently of provider parameter change. The self-improvement objective is future Minecraft task capability over later tasks/resume. Source wiring supplies a dispositional path from task evidence to retained behavior-determining code and a live execution channel. Subsequent operation causally depending on an admitted change is unestablished, and beneficial learning is not demonstrated. Critique delivery alone establishes neither content-directed explanatory theory criticism nor exercised reflection/autonomy; those properties do not inherit a status from retention. Partial inspection of plugin internals and library contents also blocks a system-wide negative about all truth-apt derivations or all knowledge checks. README empirical and transfer claims remain attributed reports without observed-run or causal evidence in this source set.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-observation
Label: observation

Source-native identity: Node observation event payload and its selected Python renderings. Representational form: symbolic keyed values at deterministic consumers; natural-language reports after prompt rendering. Storage substrate: JS objects/JSON, Python event lists/message strings and recorder files. Distinct from [RT-OBJ-program-code](runtime.md#rt-obj-program-code): this is execution evidence supplied to that program's evaluators and successors, not executable code. No supplied object counterpart after comparison. Evidence: SRC-1, `voyager/env/mineflayer/lib/observation/base.js`, `voyager/env/mineflayer/lib/observation/inventory.js`, `voyager/agents/curriculum.py`.

> const inventory = bot.currentWindow || bot.inventory;
> return inventory.items();
> --- `voyager/env/mineflayer/lib/observation/inventory.js`

> if (acc[cur.name]) {
>     //if the item is already in the dict
>     acc[cur.name] += cur.count;
> } else {
>     //if the item is not in the dict
>     acc[cur.name] = cur.count;
> }
> --- `voyager/env/mineflayer/lib/observation/inventory.js`

#### EPI-OBJ-qa-cache
Label: qa_cache

Source-native identity: `CurriculumAgent.qa_cache` question-to-answer map plus its question index. Representational form: natural-language answers/questions; symbolic key lookup; dense embedding index separately supplies similarity, not answer meaning. Storage substrate: Python dict, JSON and Chroma persistence. Distinct from task-selection output in [RT-RTE-task-selection](runtime.md#rt-rte-task-selection): retained advice backing context, not selected task itself. No supplied object counterpart. Evidence: SRC-1, `voyager/agents/curriculum.py` and the QA route below.

#### EPI-OBJ-chest-memory
Label: chest_memory

Source-native identity: `ActionAgent.chest_memory`. Representational form: symbolic position-keyed dict/Unknown/Invalid update protocol, natural-language rendered chest reports. Storage substrate: Python map, JSON checkpoint and messages. Distinct from current environment events in [RT-RTE-environment-step](runtime.md#rt-rte-environment-step): retained last chest reports surviving calls/resume. No supplied object counterpart. Evidence: SRC-1, `voyager/agents/action.py`, `voyager/env/mineflayer/lib/observation/chests.js`; update passages below.

#### EPI-OBJ-skill-description
Label: skill_description

Source-native identity: manager-generated function-shaped description string. Representational form: natural-language characterization within comment/function wrapper; dense embeddings used for ranking. Storage substrate: skill map/JSON, description text files and Chroma. Distinct from [RT-OBJ-program-code](runtime.md#rt-obj-program-code): generated after the task check, not the admitted executable body. The object belongs to the broader retention mechanism [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), but is not a duplicate of its code object. Evidence: SRC-1, `voyager/agents/skill.py`.

> skill_description = f"    // { self.llm(messages).content}"
> return f"async function {program_name}(bot) {{\n{skill_description}\n}}"
> --- `voyager/agents/skill.py`

### Routes

#### EPI-RTE-observation-context
Label: Observation context transformation

External bot fields/items/block lookups → Node event records → Python selected renderings. Node observation classes and Python renderers own the route. This extends the supplied [RT-RTE-environment-step](runtime.md#rt-rte-environment-step) with evidence semantics, not a duplicate execution route. Inventory aggregation preserves totals for the selected window, not necessarily the player's inventory. Voxels are sets of block names, not counts/positions. Curriculum can override the biome label and filter optional inventory, then probabilistically omit warmed-up fields. Critic uses a different renderer without the biome override. Consequently the route has no uniform claim of complete or unchanged observation meaning. Evidence: SRC-1, `voyager/env/mineflayer/lib/observation/inventory.js`, `voyager/env/mineflayer/lib/observation/voxels.js`, `voyager/agents/curriculum.py`, `voyager/agents/critic.py`.

- Immediate return: event values and rendered messages; no independent truth verdict.
- Later read-back: current final events and last-code/critique frame reach the next call; recorder retains raw events but the driver does not automatically reload them as an accumulating action transcript. BlockRecords retains seen types until reset.
- Delegated visibility: final-state fields selected independently for critic/action/curriculum; most raw event detail and prior turns excluded; rounded positions/health and set-valued nearby blocks reduce detail.
- Selection predicate: observations on events/final observe; curriculum warmup, regex and probability rules choose visible fields; action and critic use fixed renderers.
- Invalidation or expiry: cumulative events cleared on observe; per-action messages replaced; BlockRecords reset method clears its set; no universal world-state freshness guarantee.
- Activation or effect: wired input to judgment/planning; actual influence unobserved.
- Evidence limits: external Mineflayer/game correctness and synchronization uninspected; no observed trace. The deterministic counterexample below is a source deduction, not target execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

A concrete input with `voxels = ["stone"]` and reported biome `plains` becomes `Biome: underground` in curriculum rendering, even though that input does not logically establish underground location. By contrast the critic reads the original status biome. This limits any inference that all consumers receive the same measured biome.

> if not any(
>     "dirt" in block
>     or "log" in block
>     or "grass" in block
>     or "sand" in block
>     or "snow" in block
>     for block in voxels
> ):
>     biome = "underground"
> --- `voyager/agents/curriculum.py`

> const surroundingBlocks = new Set();
> --- `voyager/env/mineflayer/lib/observation/voxels.js`

> if (block && block.type !== 0) {
>     surroundingBlocks.add(block.name);
> }
> --- `voyager/env/mineflayer/lib/observation/voxels.js`

#### EPI-RTE-qa-context
Label: QA context generation and reuse

Part of: [RT-RTE-task-selection](runtime.md#rt-rte-task-selection)

This is the retained-advice subroute supplying context to task selection/action. Curriculum code owns question formation, cache writes, nearest-question reuse and delivery; QA model supplies questions/answers. Proposer is model plus hardcoded biome/task questions; admission is automatic on miss. No human per-answer approval or independent answer oracle is wired in inspected methods. Unknown-answer guidance and delivery string filters are not evidence-consuming validation. Trigger is missing context/QA questions; no truth-directed rollback/expiry branch in these methods. Evidence: SRC-1, `voyager/agents/curriculum.py`, `voyager/prompts/curriculum_qa_step2_answer_questions.txt`.

- Immediate return: generated or cached question/answer strings and formatted task context.
- Later read-back: JSON answers and persisted question index reload on resume; exact task-question key or nearest-question result supplies later invocations.
- Delegated visibility: answer model receives the question, not a game experiment/result oracle. Curriculum gets at most five pairs after filtering `Answer: Unknown` and `language model`; task context returns its answer without those filters.
- Selection predicate: exact task-context cache hit; for run_qa, nearest question reused when score is below 0.05, otherwise answer model called. Curriculum context inclusion also depends on progress.
- Invalidation or expiry: no truth/freshness expiry in inspected QA methods; duplicate-question assertion is structural, not adjudication.
- Activation or effect: wired cached advice to task/context consumers; model compliance, actual answer correctness and benefit unobserved.
- Evidence limits: provider parametric provenance opaque; no actual generated answer trace supplied; semantic equivalence of neighboring questions unproved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> You will answer the question based on the context (only if available and helpful) and your own knowledge of Minecraft.
> 1) Start your answer with "Answer: ".
> 2) Answer "Answer: Unknown" if you don't know the answer.
> --- `voyager/prompts/curriculum_qa_step2_answer_questions.txt`

> question = (
>     f"How to {task.replace('_', ' ').replace(' ore', '').replace(' ores', '').replace('.', '').strip().lower()}"
>     f" in Minecraft?"
> )
> --- `voyager/agents/curriculum.py`

For the concrete input `Mine iron_ore.`, replacements produce `Mine iron ore.`, then `Mine iron.`, then `Mine iron`, then `mine iron`; the resulting question is `How to mine iron in Minecraft?`. The ore qualifier has been removed deliberately, not verified equivalent. This deduction needs only the inspected implementation.

> if question in self.qa_cache:
>     answer = self.qa_cache[question]
> else:
>     answer = self.run_qa_step2_answer_questions(question=question)
>     self.qa_cache[question] = answer
>     self.qa_cache_questions_vectordb.add_texts(
>         texts=[question],
>     )
>     U.dump_json(self.qa_cache, f"{self.ckpt_dir}/curriculum/qa_cache.json")
>     self.qa_cache_questions_vectordb.persist()
> --- `voyager/agents/curriculum.py`

> if docs_and_scores and docs_and_scores[0][1] < 0.05:
>     question_cached = docs_and_scores[0][0].page_content
>     assert question_cached in self.qa_cache
>     answer_cached = self.qa_cache[question_cached]
>     questions.append(question_cached)
>     answers.append(answer_cached)
>     continue
> --- `voyager/agents/curriculum.py`

> if "Answer: Unknown" in answer or "language model" in answer:
>     continue
> --- `voyager/agents/curriculum.py`

#### EPI-RTE-chest-updates
Label: Chest report update and withdrawal

Node close/remove/nearby-scan events → Python chest map → disk and rendered messages. Owners are observation plugin and ActionAgent. Distinct from [RT-RTE-environment-step](runtime.md#rt-rte-environment-step): this is cross-call state maintenance and explicit withdrawal, not code execution. Event reports propose updates; code automatically admits dict/Unknown reports and removes Invalid; no independent reference oracle/human approval. It replaces stored item dicts without preserving a per-update rationale in this map. Evidence: SRC-1, `voyager/env/mineflayer/lib/observation/chests.js`, `voyager/agents/action.py`, `voyager/voyager.py`.

- Immediate return: changed map/persisted JSON; subsequent renderer returns chest description.
- Later read-back: next action/critic/curriculum consumes the map; resume loads JSON.
- Delegated visibility: item dictionaries, Empty or Unknown text and position; not a complete event history or freshness timestamp.
- Selection predicate: closeChest/removeChest events, scanned chest positions within 16 blocks; Python updates from final nearbyChests before critic.
- Invalidation or expiry: explicit Invalid removes position; dict replaces contents; prior map is otherwise retained. Mere lack of a new scan entry does not trigger deletion.
- Activation or effect: wired evidence for chest task judgment and planning; actual use/freshness unobserved.
- Evidence limits: event delivery and live game correspondence uninspected; no globally enforced freshness or atomic world rollback claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> bot.on("closeChest", (chestItems, position) => {
>     this.chestsItems[position] = chestItems;
> });
> bot.on("removeChest", (chestPosition) => {
>     this.chestsItems[chestPosition] = "Invalid";
> });
> --- `voyager/env/mineflayer/lib/observation/chests.js`

> if position in self.chest_memory:
>     if isinstance(chest, dict):
>         self.chest_memory[position] = chest
>     if chest == "Invalid":
>         print(
>             f"\033[32mAction Agent removing chest {position}: {chest}\033[0m"
>         )
>         self.chest_memory.pop(position)
> --- `voyager/agents/action.py`

#### EPI-RTE-skill-description
Label: Skill description generation

Part of: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission)

Manager supplies main name/code → separate description model → function-shaped summary → vector index. Owner is SkillManager. This is a subroute distinct from code judgment because the model generates a new characterization after that judgment. Proposal guidance excludes bot.chat/helpers and requests a main-function summary; nothing checks resulting semantic fidelity. Manager automatically accepts returned text for indexing, without a human decision, reference answer, regression gate or description rollback. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/prompts/skill.txt`.

- Immediate return: description text wrapped as an async function/comment.
- Later read-back: description stored with code and embedded; later query ranking uses the description index to return actual code.
- Delegated visibility: description model sees program code and main name, not original critic evidence/trace; action model receives selected code, not these summary strings from retrieve_skills.
- Selection predicate: every add_new_skill after deposit-task skip, including same-name replacement and direct calls.
- Invalidation or expiry: active description/index replaced on same-name write; versioned text files retained; no description truth-expiry criterion.
- Activation or effect: wired indexing and ranking input; actual ranking effects and summary quality unobserved.
- Evidence limits: prior task success cannot validate a later-generated description; no retained source-to-summary entailment check supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 2) Do not mention anything about `bot.chat` or helper functions.
> 3) There might be some helper functions before the main function, but you only need to describe the main function.
> 4) Try to summarize the function in no more than 6 sentences.
> --- `voyager/prompts/skill.txt`

> self.vectordb.add_texts(
>     texts=[skill_description],
>     ids=[program_name],
>     metadatas=[{"name": program_name}],
> )
> --- `voyager/agents/skill.py`

#### EPI-RTE-progress-cleanup
Label: Progress history cleanup

Part of: [RT-RTE-task-selection](runtime.md#rt-rte-task-selection)

The history-maintenance/read-back part of task selection: task judgment → completed/failed lists → deduplication and failure withdrawal → JSON → progress/context. Curriculum owns it. Distinct from task judgment and skill admission: it organizes their task-status consequence, not code or a new task proposal. Proposer/decider upstream is critic/human; code consumes `success` and literal task strings; no additional reference oracle or causal adjudication. Deposit tasks bypass history. A completed task removes prior failed entries rather than invalidating retained skills. Evidence: SRC-1, `voyager/agents/curriculum.py`; inference consumer is [RT-RTE-task-inference](runtime.md#rt-rte-task-inference).

- Immediate return: updated lists and persisted completed_tasks.json/failed_tasks.json.
- Later read-back: resumed curriculum loads histories; task context and progress-dependent selection/QA visibility consume them; inference progress chooses next subgoal.
- Delegated visibility: task strings marked completed or failed, not code/test provenance or chronological failure evidence.
- Selection predicate: non-deposit progress update after rollout; `info["success"]` determines list.
- Invalidation or expiry: completed list deduplicated in order; every failed occurrence of each completed string removed. No general TTL.
- Activation or effect: wired task-status integration and progression; actual correctness/benefit unobserved.
- Evidence limits: equality cleanup cannot show why failures changed or whether a particular skill now works; raw recorder data is not thereby erased.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # remove completed tasks from failed tasks
> for task in updated_completed_tasks:
>     while task in updated_failed_tasks:
>         updated_failed_tasks.remove(task)
> --- `voyager/agents/curriculum.py`

### Claims

#### EPI-CLM-self-verification
Label: Feedback and self-verification claim

Claimed operation: environment feedback, execution errors and self-verification improve programs, within a system described as making discoveries without human intervention. Source: SRC-1, `README.md`; doctrine/design and reported operation. Distinct from [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning): this names the proposed checking/improvement mechanism, not the learning entry point.

> makes novel discoveries without human intervention. Voyager consists of three
> key components: 1) an automatic curriculum that maximizes exploration, 2) an
> ever-growing skill library of executable code for storing and retrieving complex
> behaviors, and 3) a new iterative prompting mechanism that incorporates environment
> feedback, execution errors, and self-verification for program improvement.
> --- `README.md`

The critic's declared criterion is task requirements, not program proof:

> You are required to evaluate if I have met the task requirements. Exceeding the task requirements is also considered a success while failing to meet them requires you to provide critique to help me improve.
> --- `voyager/prompts/critic.txt`

> Inventory (xx/36): My final inventory. For mining and smelting tasks, you only need to check inventory.
> --- `voyager/prompts/critic.txt`

These criteria admit final-state success without identifying action causality. The server can itself add items before final observation:

> if (bot.inventoryUsed() >= 32) {
>     // if chest is not in bot's inventory
>     if (!bot.inventory.items().find((item) => item.name === "chest")) {
>         bot.chat("/give @s chest");
>     }
> }
> --- `voyager/env/mineflayer/index.js`

Optional failure recovery occurs after the task check and rewrites only selected evidence fields for the next context:

> events[-1][1]["inventory"] = new_events[-1][1]["inventory"]
> events[-1][1]["voxels"] = new_events[-1][1]["voxels"]
> --- `voyager/voyager.py`

#### EPI-CLM-skill-transfer
Label: Skill growth and transfer claim

Claimed operation: reusable/compositional code compounds abilities, mitigates forgetting and solves novel tasks in new worlds. README also reports comparative performance. Evidence: SRC-1, `README.md`; doctrine/design and reported operation, not supplied observed-run or causal evidence. Distinct from [RT-CLM-lifelong-learning](runtime.md#rt-clm-lifelong-learning): this adds transfer/benefit claims beyond entry-point wiring. The literal ever-growing language is retained in [EPI-CLM-self-verification](#epi-clm-self-verification)'s passage; same-name active replacement bounds it.

> The skills developed by Voyager are temporally
> extended, interpretable, and compositional, which compounds the agent’s abilities
> rapidly and alleviates catastrophic forgetting.
> --- `README.md`

> It obtains 3.3× more unique items, travels 2.3× longer
> distances, and unlocks key tech tree milestones up to 15.3× faster than prior SOTA.
> Voyager is able to utilize the learned skill library in a new Minecraft world to
> solve novel tasks from scratch, while other techniques struggle to generalize.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
