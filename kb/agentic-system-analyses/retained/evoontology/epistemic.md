---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "EvoOntology's semantic commitment, retrieval, task evidence and evaluation-to-publication authority routes."
run-id: AAS-2026-10-13-evoontology-f2d0c7992c6e-01
reviewed-boundary: c94389b764394379086ff25e50d0e0f4396167b4
---

# EvoOntology epistemic report

## Source-and-claim boundary

The question is whether workload-grounded semantic state and evolution evaluations license later analytical reliance, and which checks actually control that reliance. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is SRC-1 in its [Source register](boundary.md#source-register). This report does not add sources. The frozen checkout supplies implementation and doctrine/design, not an observed build, evolution episode, benchmark run or causal experiment. README results remain attributed reported operation.

The included system is broader than its deterministic library: model-facing Build/Evolve instructions, host plugins, shipped benchmark consumers and evaluators belong to the boundary. External hosts, data, services and provider weights do not. Their absence prevents verification of actual grounding, instruction compliance, evaluator reliability and model continuity. Uninspected included files are not access gaps. In particular, the detailed DDR judge and InsightBench metric implementations remain unassessed; no system-complete negative about semantic checking follows.

Knowledge/warrant claims are [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment), [EPI-CLM-gated-versioning](#epi-clm-gated-versioning), and [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success). They concern data-grounded commitment and reproducibly better task performance, not formal proof of all semantic propositions.

| Entry point or operation | Source path | Coverage and records | Remaining limit |
| --- | --- | --- | --- |
| CLI validation | SRC-1, `pyproject.toml`, `evoontology/validate.py` | Direct reads; [EPI-RTE-version-validation](#epi-rte-version-validation) | Loadability is not meaning verification. |
| MCP semantic tools/resource | SRC-1, `evoontology/runtime/mcp_server.py`, `evoontology/runtime/runtime.py` | Direct complete dispatch/retrieval reads; [EPI-RTE-semantic-projection](#epi-rte-semantic-projection), [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval) | Local benchmark variants not exhaustively inspected; root projection is not universal. |
| Registered lifecycle/workflow operations | SRC-1, `evoontology/runtime/ops.py`, `evoontology/runtime/tools.py` | Direct complete handler map and initial tool schemas; runtime supplies workflow route: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) | Registry schemas after initial semantic/validation/presentation entries not read completely; handler dispatch is inspected. Manual event authenticity unresolved. |
| Build commitment | SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`, `evoontology/runtime/ops.py` | Direct commitment/validation/publication instructions and implementation; [RT-RTE-build-publication](runtime.md#rt-rte-build-publication) | Host probes and semantic judgments unobserved; Claude Build instruction parity not assessed here. |
| Evolve/check/reject/publish | SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `evoontology/evolution/session.py`, `evoontology/evaluation/evaluation.py` | Direct evaluation instructions, round/evaluation persistence, accept/gate/incomplete and complete aggregation module; [EPI-RTE-gate-aggregation](#epi-rte-gate-aggregation), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission) | Supplied runtime covers start/resume/budget and theory instructions; no independent observation authentication or actual revision trace. |
| Save/select/promote/publish | SRC-1, `evoontology/ontology/store.py`, `evoontology/runtime/ops.py` | Direct store save/load/selection/promotion/publication; [RT-RTE-version-override](runtime.md#rt-rte-version-override) | Content remains mutable by administrative writes; selector is not an endorsement ledger. |
| SessionStart reminder | SRC-1, `plugins/claude-code/hooks/hooks.json`, `plugins/claude-code/scripts/check-reminder.py`, `evoontology/trigger/trigger.py` | Direct hook registration; implementation findings supplied by [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission) | Reminder changes opportunity to evolve, not semantic warrant; host reaction unobserved. |
| BIRD evaluation | SRC-1, `benchmarks/bird/run_evaluation.py` | Direct SQL scorer; supplied driver/adapter/agent findings in [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation); [EPI-RTE-sql-comparison](#epi-rte-sql-comparison) | Dataset/reference correctness, execution and causal effect unobserved. |
| DDR evaluation and existing-log alternative | SRC-1, `benchmarks/ddr_10k/evolution_adapter.py`, `benchmarks/ddr_10k/run_evaluation.py` | Supplied adapter route; targeted source search identifies UnifiedEvaluator dispatch; [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation) | Judge prompts, parsing and scoring not inspected here; no detailed evaluator-license conclusion. |
| InsightBench evaluation | SRC-1, `benchmarks/insightbench/insightbench/runner.py`, `benchmarks/insightbench/insightbench/benchmarks.py`, `benchmarks/insightbench/insightbench/metrics.py` | Supplied runner/adapter route; targeted searches identify insight/summary metrics and configurable ROUGE/G-Eval/Llama3 alternatives; [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation) | Detailed metric inputs, model state and reduction semantics unassessed; no truth-verification verdict. |
| Benchmark answer production/tools | SRC-1, `benchmarks/bird/agent/data_agent.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/insightbench/insightbench/tceo/tool_chat.py` | Supplied [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop) | Provider internal processing and local semantic variants uninspected. |
| Explorer/annotations | SRC-1, `evoontology/runtime/ops.py`, `evoontology/visualization/renderer.py` | Direct presentation wrapper; supplied [RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission) | Presentation is not another acceptance check; explorer transformations not independently assessed here. |

## Epistemic-object inventory

Fields owned by each record are available through its citation rather than duplicated here. Truth-apt content is potential content, not an assertion that a real populated object was observed.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-term](#epi-obj-term) | Concept meaning over its declared scope | see record | SRC-1, `evoontology/ontology/models.py` | Meaning/scope may be empty; no observed commitment. |
| [EPI-OBJ-mapping](#epi-obj-mapping) | Concept-to-data correspondence, grain and filter semantics | see record | SRC-1, `evoontology/ontology/models.py` | Runtime omits some validation metadata; confidence is caller content. |
| [EPI-OBJ-relation](#epi-obj-relation) | Relationship and connection conditions | see record | SRC-1, `evoontology/ontology/models.py` | A `derivation` label is not a checked derivation. |
| [EPI-OBJ-constraint](#epi-obj-constraint) | Applicability/value/business-rule proposition; severity itself is policy | see record | SRC-1, `evoontology/ontology/models.py` | Root resolver conveys severity as guidance, not an execution veto. |
| [EPI-OBJ-evidence](#epi-obj-evidence) | Claimed observation from a source/query at a time | see record | SRC-1, `evoontology/ontology/models.py` | Stored query/result is not authenticated execution or reproduced evidence. |
| [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session) | Hypothesis text and recorded performance assertions; lifecycle status itself is policy state | see record | SRC-1, `evoontology/evolution/session.py` | Mixed container: deterministic code consumes status/scores; model interprets hypothesis/notes. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Not determinable within inaccessible weights | see record | SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md` | Exact model/weight provenance and actual internal theories uninspected. |
| [RT-CMP-bird-provider](runtime.md#rt-cmp-bird-provider), [RT-CMP-ddr-provider](runtime.md#rt-cmp-ddr-provider), [RT-CMP-tool-calling-chat](runtime.md#rt-cmp-tool-calling-chat) | Not determinable within provider weights; outputs may contain task claims | see records | SRC-1, `benchmarks/bird/agent/llm_providers.py` | Separate component fixity limits; inference wrappers do not establish training or truth. |
| [RT-CMP-llm-judge](runtime.md#rt-cmp-llm-judge) | Comparative verdicts are assertions about answers; weight content not determinable | see record | SRC-1, `evoontology/evaluation/evaluation.py` | Core does not implement judge call. |

Task native observations/final answers are operative route outputs of [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); benchmark answers and score artifacts are outputs of [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop) and [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation). Their exact proposition content cannot be individuated without a run artifact. This is not an absence of truth-apt task content.

## Authority-route ledger

These compact entries split functions even when one API performs several. `see` delegates fields to declaring records; local scope judgments remain explicit.

Route ID: [RT-RTE-build-publication](runtime.md#rt-rte-build-publication)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-term](#epi-obj-term), [EPI-OBJ-mapping](#epi-obj-mapping), [EPI-OBJ-relation](#epi-obj-relation), [EPI-OBJ-constraint](#epi-obj-constraint)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Proposed workload semantics grounded in external data.
Evaluator/condition and domain: see route; host interprets workload and native observations, rather than deterministic code generating claims.
Activation and timing: see route; Build instruction before save/publication.
Possible or observed result: Candidate semantic objects; no observed instance-to-route provenance.
Implemented force: Model-facing instruction; Python provides writable containers, not this semantic inference.
Epistemic authority and scope: Candidate generation only until meaning, scope, granularity and reproducibility are checked. Import, reshaping, derivation and conjecture cannot be distinguished without actual inputs/proposals.
Operational authority: see route.
Behavioral-authority path: see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`.
Claim IDs: [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment).
Mismatch marker: Semantic production is delegated, not observed.
Gap/limit: Evidence text alone cannot prove source warrant is preserved; actual grounding lineage unknown.

Route ID: [RT-RTE-build-publication](runtime.md#rt-rte-build-publication)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: The four semantic claim families above and [EPI-OBJ-evidence](#epi-obj-evidence).
Content/update relation: no content change
Transition or check target: Each important workload dimension and its proposed data grounding.
Evaluator/condition and domain: see route; Build demands real structures, reproducible Evidence, explicit applicability, schema-only fields and revision of unsupported/ambiguous objects.
Activation and timing: Before initial commitment.
Possible or observed result: Validated semantic knowledge, revised objects, or a documented coverage gap; no observed decision.
Implemented force: Host policy; not reproduced by structural validator.
Epistemic authority and scope: Declared evidence-consuming criterion for reusable semantic guidance on this workload/data environment. No observed accepted ampliative claim established.
Operational authority: Withhold/revise objects under the skill; see route.
Behavioral-authority path: see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`.
Claim IDs: [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment).
Mismatch marker: Meaning verification is stronger than deterministic publication requirements.
Gap/limit: No host judgment trace. Starting Build is not per-object human approval.

Route ID: [EPI-RTE-version-validation](#epi-rte-version-validation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: Five serialized semantic record families.
Content/update relation: no content change
Transition or check target: Version file integrity, references and loadability.
Evaluator/condition and domain: see record.
Activation and timing: CLI/MCP request, initial publish, or session accept.
Possible or observed result: see record; possible passed/errors, no observed target run.
Implemented force: Returns structural evidence; publication consumers veto failure.
Epistemic authority and scope: License that checked representation loads with resolved checked references, not that business semantics or recorded observations are true.
Operational authority: see record.
Behavioral-authority path: Python validator result → build/session publication condition, enforcing at that API call; standalone CLI/MCP result is advisory to caller.
Evidence source ID and local anchor: SRC-1, `evoontology/validate.py`.
Claim IDs: [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment).
Mismatch marker: none; the tool explicitly describes structural checks.
Gap/limit: No Evidence replay, enum validation or schema-only field enforcement in inspected validator.

Route ID: [RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [RT-RTE-version-override](runtime.md#rt-rte-version-override)
Route function: retention
Architectural status: implemented
Object/candidate ID: Five version files.
Content/update relation: no content change
Transition or check target: Caller record lists → durable version directory.
Evaluator/condition and domain: see routes; serialization/list/path checks, not semantic acceptance.
Activation and timing: save_version before selection, including unaccepted candidates.
Possible or observed result: see routes; saved/replaced files or error.
Implemented force: Durable write.
Epistemic authority and scope: Retention confers none; source warrant unknown.
Operational authority: Later reload can consume files after selection; see routes.
Behavioral-authority path: Version files → selected semantic layer → model guidance, permissive/advisory on later requests.
Evidence source ID and local anchor: SRC-1, `evoontology/ontology/store.py`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Retention precedes acceptance; mutable named versions weaken replay identity.

Route ID: [RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [RT-RTE-version-override](runtime.md#rt-rte-version-override)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: Active version and semantic files.
Content/update relation: no content change
Transition or check target: Version directory selected for later service.
Evaluator/condition and domain: see routes; initial publish validates and refuses existing active index, direct selector only checks directory existence.
Activation and timing: Client command; next reload/new task.
Possible or observed result: see routes.
Implemented force: Selector changes available guidance.
Epistemic authority and scope: Neither selector route independently accepts the truth of semantic claims.
Operational authority: Changes later delivered state; can switch back to a preserved version.
Behavioral-authority path: see [RT-BAP-semantic-guidance](runtime.md#rt-bap-semantic-guidance).
Evidence source ID and local anchor: SRC-1, `evoontology/runtime/ops.py`, `evoontology/ontology/store.py`.
Claim IDs: [EPI-CLM-gated-versioning](#epi-clm-gated-versioning).
Mismatch marker: Alternate administrative path bypasses evolution gate.
Gap/limit: Actual client grants uninspected; capability is not misuse evidence.

Route ID: [EPI-RTE-semantic-projection](#epi-rte-semantic-projection)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: Five semantic families.
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Raw stored fields → root models → delivered views.
Evaluator/condition and domain: see record; deterministic extraction/normalization, not truth judgment.
Activation and timing: Semantic load and resolve.
Possible or observed result: see record.
Implemented force: Limits what the receiving model sees.
Epistemic authority and scope: Carries retained propositions/evidence strings without new source warrant. Omitted source/validation/confidence metadata limits contextual fidelity.
Operational authority: Advisory definitions/mappings/relations/constraints, not final answers.
Behavioral-authority path: see [RT-BAP-semantic-guidance](runtime.md#rt-bap-semantic-guidance).
Evidence source ID and local anchor: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`.
Claim IDs: [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment).
Mismatch marker: none; projections are explicitly navigation aids.
Gap/limit: Non-ampliative extraction does not establish semantic preservation of every omitted field or faithful model interpretation.

Route ID: [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: Active/validated terms and attached objects/evidence.
Content/update relation: no content change
Transition or check target: Query/name/alias/ID/context matches and lifecycle state.
Evaluator/condition and domain: see route; lexical relevance/ambiguity, not correctness. `_is_active` admits `active` or `validated`; missing lifecycle defaults active.
Activation and timing: Request and reload; deprecated/non-active semantic objects cease delivery through these filters.
Possible or observed result: Ranked items, resolved/ambiguous/unresolved and coverage markers; see route.
Implemented force: Ranking and filtering delivered context.
Epistemic authority and scope: `coverage_status: supported` means attached mapping/relation/constraint exists, not verified truth. `block` constraint severity is returned text, not a root query-execution prohibition.
Operational authority: Allows model to use guidance or inspect data directly; no compulsory model reliance.
Behavioral-authority path: see [RT-BAP-semantic-guidance](runtime.md#rt-bap-semantic-guidance).
Evidence source ID and local anchor: SRC-1, `evoontology/runtime/runtime.py`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Lifecycle withdrawal is content/caller-controlled, not an automatic evidence-revocation procedure; already delivered content is not recalled.

Route ID: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: Native observations and final answers.
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Data query executed by built-in SQLite, or observation supplied by host.
Evaluator/condition and domain: see route; SQLite establishes results on accessed database within query semantics, not correct question interpretation. Manual events are assertions of execution.
Activation and timing: During pinned-version task.
Possible or observed result: Rows/errors and evidence-shaped trajectory; see route.
Implemented force: Completion guard demands at least one non-error native event, not answer equivalence.
Epistemic authority and scope: Built-in observation provenance reaches executed query; source-data truth and analytical meaning remain unknown. Host-native observation warrant is unauthenticated.
Operational authority: Permit completion, persist answer/trajectory; see route.
Behavioral-authority path: Task event fields → deterministic completion guard, enforcing now; later trajectory → Evolver interpretation, advisory across rounds/sessions.
Evidence source ID and local anchor: SRC-1, `evoontology/workflow.py`.
Claim IDs: [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment).
Mismatch marker: none.
Gap/limit: One successful tool result cannot warrant every final-answer proposition.

Route ID: [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: Hypothesis/candidate in [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session).
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Trajectory diagnosis and causal attribution → hypothesis/patch.
Evaluator/condition and domain: see route and its independent theory-property assessments.
Activation and timing: Host-called evolution; failed mechanisms should change attribution and subsequent candidate.
Possible or observed result: Explanatory hypothesis/candidate, not observed theory-directed reasoning.
Implemented force: Method guidance; Python stores nonempty hypothesis but does not interpret it.
Epistemic authority and scope: Candidate explanation; no entailed derivation or accepted ampliative mechanism established without actual inputs and acceptance evidence.
Operational authority: Host-directed next probes/patches; see route.
Behavioral-authority path: see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.
Claim IDs: [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success).
Mismatch marker: Task score increase does not verify the proposed causal mechanism.
Gap/limit: No component intervention comparison, actual critique/reuse or parametric-state evidence.

Route ID: [EPI-RTE-sql-comparison](#epi-rte-sql-comparison)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: Predicted SQL, reference SQL, execution-score artifact.
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Equality of sorted row tuples on one database instance.
Evaluator/condition and domain: see record; deterministic SQLite comparison with reference SQL as answer oracle.
Activation and timing: BIRD per-question evaluation after generated SQL.
Possible or observed result: Execution match Boolean and timing ratio; see record.
Implemented force: Benchmark metrics/artifacts, not publication by itself.
Epistemic authority and scope: Conditional warrant for extensional row equivalence on the accessed database; reference correctness is an unverified premise.
Operational authority: Contribution to benchmark summary and caller's possible gate input.
Behavioral-authority path: Scorer → driver metrics → adapter result → caller-supplied formal gate, ranking/advisory until session consumes it.
Evidence source ID and local anchor: SRC-1, `benchmarks/bird/run_evaluation.py`.
Claim IDs: [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success).
Mismatch marker: none.
Gap/limit: No proof of query intent, explanation, other databases or ontology component effect. Error and mismatch can share false/zero output.

Route ID: [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: DDR/InsightBench answers/logs and score artifacts.
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: DDR generated/existing logs; InsightBench flag insights/summary.
Evaluator/condition and domain: see route; detailed judge/metric internals uninspected here.
Activation and timing: Selected-version adapter evaluation; DDR can skip generation.
Possible or observed result: Normalized scores/cases/artifact references; see route.
Implemented force: Returned evaluation input, not accepted ontology or mechanism proof.
Epistemic authority and scope: Not determinable beyond benchmark-reported assessment without inspecting downstream evaluator inputs and criteria.
Operational authority: Caller may record/pair results; adapters omit gate_input.
Behavioral-authority path: Benchmark artifacts → adapter summary → Evolver/formal gate; advisory until admission.
Evidence source ID and local anchor: SRC-1, `benchmarks/ddr_10k/evolution_adapter.py`, `benchmarks/insightbench/evolution_adapter.py`.
Claim IDs: [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success).
Mismatch marker: none.
Gap/limit: Freshness/reused artifacts and external evaluator behavior unresolved; no system-complete evaluation verdict.

Route ID: [EPI-RTE-gate-aggregation](#epi-rte-gate-aggregation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: Formal gate inputs in [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session).
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Supplied paired numeric scores or decoded winner/error verdicts.
Evaluator/condition and domain: see record; arithmetic averages or winner counts under input-validity checks.
Activation and timing: accept recomputes current candidate/current round gate.
Possible or observed result: Conditional accept/reject aggregate; see record.
Implemented force: Necessary mechanical condition for session acceptance.
Epistemic authority and scope: Only aggregate ordering over supplied observations, not authenticity, independence, reproducibility or truth of ontology claims.
Operational authority: Permit/block this API's publication, plus explicit regression assertion.
Behavioral-authority path: see [RT-BAP-session-gate](runtime.md#rt-bap-session-gate).
Evidence source ID and local anchor: SRC-1, `evoontology/evaluation/evaluation.py`, `evoontology/evolution/session.py`.
Claim IDs: [EPI-CLM-gated-versioning](#epi-clm-gated-versioning), [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success).
Mismatch marker: Valid aggregate does not establish reproduced improvement.
Gap/limit: Actual premises unwarranted in this evidence set. Counterexample: caller can submit finite improving scores and false regression flag without a trace; inspected gate checks their form, not execution.

Route ID: [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: Whole candidate version, not each contained proposition or hypothesis.
Content/update relation: no content change
Transition or check target: Structurally valid candidate plus passing formal gate.
Evaluator/condition and domain: see route and [EPI-RTE-gate-aggregation](#epi-rte-gate-aggregation).
Activation and timing: Explicit accept; reject record instead keeps running and parent selected within this route.
Possible or observed result: Accepted published version or veto; reject/incomplete records; no observed run.
Implemented force: Enforcement of recorded-input acceptance for intended later analytical use under frozen protocol.
Epistemic authority and scope: Conditional task-performance admission, not evidence-consuming acceptance of every new semantic claim or causal mechanism. Reproducibility/meaning criteria remain host obligations.
Operational authority: see route; publish/select/checkpoint; rejection blocks only this route's successor adoption.
Behavioral-authority path: see [RT-BAP-session-gate](runtime.md#rt-bap-session-gate), [RT-BAP-semantic-guidance](runtime.md#rt-bap-semantic-guidance).
Evidence source ID and local anchor: SRC-1, `evoontology/evolution/session.py`.
Claim IDs: [EPI-CLM-gated-versioning](#epi-clm-gated-versioning), [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success).
Mismatch marker: Direct selection bypass; acceptance of performance is not acceptance of explanation.
Gap/limit: Rejected files/summaries persist. No global deletion/withdrawal or guaranteed inaccessible evaluator context demonstrated.

Route ID: [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: Accepted semantic claims/mechanisms and problem map.
Content/update relation: no content change
Transition or check target: Connect accepted results to solved problems, remaining limits and future causal understanding.
Evaluator/condition and domain: see route; host interprets evidence and updates problem map.
Activation and timing: Post-decision instruction; not inferred from copying a candidate directory.
Possible or observed result: Preserved validated mechanisms/rejected hypotheses and revised problem understanding.
Implemented force: Instruction to host; durable round/run files afford retention.
Epistemic authority and scope: Integration follows declared acceptance, but actual connected accepted theory is unobserved.
Operational authority: Later diagnosis should use revised understanding; no reliable content-directed reuse established.
Behavioral-authority path: see [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).
Evidence source ID and local anchor: SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`.
Claim IDs: [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success).
Mismatch marker: none.
Gap/limit: Selector installation and retention alone are not this epistemic integration.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-grounded-commitment](#epi-clm-grounded-commitment) | see record | SRC-1, `README.md`; doctrine/design | Build requires comparative grounding, reproducible Evidence and revision | [RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [EPI-RTE-version-validation](#epi-rte-version-validation), [EPI-RTE-semantic-projection](#epi-rte-semantic-projection) | None supplied | No reproduced grounding; structure/reference validity cannot verify semantic interpretation | Semantic evidence architecture and host commitment policy are supported | Automated truth verification and observed accepted semantic knowledge unestablished |
| [EPI-CLM-gated-versioning](#epi-clm-gated-versioning) | see record | SRC-1, `README.md`; doctrine/design | Independent controlled comparison and reruns requested | [EPI-RTE-gate-aggregation](#epi-rte-gate-aggregation), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission), [RT-RTE-version-override](runtime.md#rt-rte-version-override) | None supplied | Input authenticity/fixed conditions/repeated trials not enforced by arithmetic; bundled treatment cannot identify component effect | Session accept enforces aggregate improvement over recorded paired scores or verdict counts | Reproducibility and all-path gate coverage are not guaranteed |
| [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success) | see record | SRC-1, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`; doctrine/design | Diagnose/Attribute/Patch/Evaluate and no unacceptable regression | [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission), [EPI-RTE-sql-comparison](#epi-rte-sql-comparison), [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation) | None supplied | Task comparison is not mechanism verification or transfer; no supplied intervention experiment | Improvement-directed candidate evaluation and conditional admission are wired | Successful learning, causal explanation and exercised self-improvement remain unobserved |

## Bounded conclusion

EvoOntology retains five semantic claim/evidence families and delivers selected views as analytical guidance. Evidence IDs survive root loading and can lead to query/result/source strings; that traceability does not authenticate or reproduce the observations. Imported task observations have bounded lineage: built-in SQLite runs a query, whereas manually recorded events depend on host integrity. No frozen data premises warrant an actual semantic proposition here.

The root deterministic transformations reshape records, filter lifecycle states and derive comparison results within formal domains. A concrete mapping projection loses `database_source` and validation/confidence metadata while preserving term/table/column/filter/grain and evidence references. `supported` coverage and `validated` lifecycle are selection labels, not epistemic endorsement. Neither a relation named `derivation` nor a constraint marked `block` installs a proof or a query veto. These findings are local to [EPI-RTE-semantic-projection](#epi-rte-semantic-projection) and [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval), not every benchmark variant.

Build declares meaningful acceptance criteria: real data correspondences, explicit scope/grain, reproducible Evidence and revision rather than fabrication. Python enforces file/reference/loadability checks, not those semantic judgments. Evolution separately accepts a whole candidate for intended later analytical use when recorded paired scores improve, or candidate wins exceed parent wins with zero candidate critical errors, and the caller explicitly rules out unacceptable regressions. That operational acceptance is real implementation, but its license is conditional on supplied evaluation observations. No observed produced accepted ampliative claim or accepted causal mechanism follows.

BIRD's inspected evaluator licenses only reference-row equivalence on its accessed database and conditional timing comparisons. The GT gate licenses only average ordering; the judge gate licenses only supplied winner/error aggregation. Detailed DDR/InsightBench evaluators remain unassessed. None of those bounded checks proves semantics, explanatory mechanism, replay safety, component contribution or general transfer. The model-dependent generation relations remain indeterminate without concrete inputs/outputs: lack of a proof of entailment is not evidence of ampliative conjecture.

Publication and later retrieval give accepted or administratively selected content an advisory model-authority path across tasks/sessions. They do not prove compliance or benefit. Direct version selection/save bypasses session evaluation. Rejection preserves parent selection within the lifecycle route and retains critique/evaluation records; it does not purge candidates globally. Post-acceptance problem-map/mechanism integration is instructed rather than observed. No separate direct learned policy update is demonstrated; selector/status/checkpoint changes are operational state, while behavior-shaping tool/schema edits remain host-managed as recorded in [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission).

The runtime's independent theory-builder, learning, reflection, autonomy and self-improvement fields remain bounded as stated in that route. Localized hypothesis persistence is wired; content-dependent critique/reuse are requested; weight changes are not implemented by the inspected inference/core paths and provider internals remain uninspected. A dormant evidence-to-ontology-to-guidance pathway does not establish exercised or successful self-improvement. No single epistemic score or system-wide truth verdict is warranted.

## Shared records

### Operative objects

#### EPI-OBJ-term
Label: Term

Source-native identity: root `Term` records. Representational form: natural-language definition/scope/name interpreted by model, symbolic ID/evidence/lifecycle selectors interpreted by code. Storage substrate: `versions/<v>/terms.json`, loaded dataclass. Evidence: SRC-1, `evoontology/ontology/models.py`. No counterpart among supplied object declarations: [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session) is the lifecycle container, not this family. Claimed role is workload concept semantics.

> definition=str(data.get("definition", "")),
> scope=str(data.get("scope", "")),
> --- `evoontology/ontology/models.py`

#### EPI-OBJ-mapping
Label: Mapping

Source-native identity: root `Mapping` records. Representational form: natural-language validation/grain/aggregation meaning and symbolic term/data addressing/filter strings; runtime carries these to model interpretation, not automatic query execution. Storage substrate: `versions/<v>/mappings.json`, loaded dataclass. Evidence: SRC-1, `evoontology/ontology/models.py`. Distinct from [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session), with no supplied family counterpart. Claimed role is concept-to-physical-data grounding.

> database_source=str(data.get("database_source", "")),
> table=str(data.get("table", "")),
> column=str(data.get("column", "")),
> semantic_filter=str(data.get("semantic_filter", data.get("filter", ""))),
> aggregation_semantics=str(data.get("aggregation_semantics", "")),
> grain=str(data.get("grain", "")),
> --- `evoontology/ontology/models.py`

#### EPI-OBJ-relation
Label: Relation

Source-native identity: root `Relation` records. Representational form: symbolic endpoint IDs and relation label; natural-language connection/description for model interpretation. Storage substrate: `versions/<v>/relations.json`, loaded dataclass. Evidence: SRC-1, `evoontology/ontology/models.py`. No supplied family counterpart after comparison with [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session). Claimed role is semantic connection, not executable entailment checking.

> relation_type=str(data.get("relation_type", data.get("type", ""))),
> target=str(data.get("target", data.get("to_term", ""))),
> connection_condition=str(data.get("connection_condition", "")),
> description=str(data.get("description", "")),
> --- `evoontology/ontology/models.py`

#### EPI-OBJ-constraint
Label: Constraint

Source-native identity: root `Constraint` records. Representational form: natural-language applicability/description and symbolic target/severity/lifecycle/confidence; severity is delivered guidance in root resolver. Storage substrate: `versions/<v>/constraints.json`, loaded dataclass. Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`. No supplied family counterpart after comparison with [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session). Claimed role is data-grounded applicability/value/business rules.

> "id": c.id,
> "severity": c.severity,
> "description": c.description or "",
> "evidence_refs": list(c.evidence_refs),
> --- `evoontology/runtime/runtime.py`

#### EPI-OBJ-evidence
Label: Evidence

Source-native identity: root `Evidence` records. Representational form: text source/query/result/validation method/timestamp claims carried as strings, with symbolic ID linkage. Storage substrate: `versions/<v>/evidence.json`, loaded dataclass. Evidence: SRC-1, `evoontology/ontology/models.py`. Distinct from evaluation/trajectory references in [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session); no supplied counterpart. Claimed role is reproducible observation supporting semantic claims, not intrinsic certification.

> source=str(data.get("source", "")),
> query=str(data.get("query", "")),
> result=str(data.get("result", "")),
> validation_method=str(data.get("validation_method", "")),
> timestamp=str(data.get("timestamp", "")),
> --- `evoontology/ontology/models.py`

### Routes

#### EPI-RTE-version-validation
Label: Version structural validation

Distinct identity: check function shared by initial publication and evolution acceptance, not a duplicate of either enclosing route [RT-RTE-build-publication](runtime.md#rt-rte-build-publication) or [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission). It is separately invoked by CLI/MCP. Endpoints: named/active raw files → ID indexing/reference checks → runtime load → passed/errors. Owner: deterministic validator. Context/state: workspace/version; no retained write. Domain: required five JSON lists, IDs, selected references and loadability. It permits missing semantic prose, does not replay Evidence, does not enforce the skill's relation enumeration or all schema field prohibitions. Consumers own disposition; it does not propose semantic changes or install a successor.

- Immediate return: passed/errors/root/version dictionary; CLI prints it and returns zero/one.
- Later read-back: inapplicable — check itself does not persist changed material.
- Delegated visibility: MCP JSON text or CLI report reaches caller; build/session read passed/errors directly.
- Selection predicate: explicit version, otherwise active index.
- Invalidation or expiry: Result applies to inspected files at check time; subsequent overwrites are not invalidated automatically.
- Activation or effect: Wired build/session veto on failure; standalone call only reports.
- Evidence limits: No actual check execution supplied; check covers structure rather than source truth or meaning.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `evoontology/validate.py`, `evoontology/runtime/ops.py`, `pyproject.toml`.

> # The runtime must be able to load the store.
> if not errors:
>     try:
>         SemanticStore.load_version(root, selected_version)
>     except Exception as exc:
>         errors.append(f"Store load failed: {exc}")
> --- `evoontology/validate.py`

> if not result.get("passed"):
>     raise ValueError(f"Ontology validation failed: {result}")
> SemanticStore.set_active(workspace, version)
> --- `evoontology/runtime/ops.py`

#### EPI-RTE-semantic-projection
Label: Root semantic projection
Part of: [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval)

Distinct material function: extraction between persistence and delivery, not another copy of the whole retrieval route. Endpoints: raw JSON → `from_dict` dataclasses → root `_build_resolve_result`/`_evidence_view` → MCP serialized result. Owner: deterministic root model/runtime/server code. Context/state: selected version. Existing evidence references are extracted and unique evidence views appended; no evidence reproduction occurs. Mappings omit database_source, validation description and confidence from resolved delivery; relation descriptions and constraint scope/confidence also do not all cross this projection. Lifecycle availability governs selection, not certification.

Concrete implementation deduction, without execution: a mapping with term_id `t`, table `orders`, column `amount`, database_source `warehouse`, validation description `checked sample` and validation.evidence `[e]` loads those fields via Mapping.from_dict. For resolution of term `t`, the mapping comprehension emits table/column plus filter/aggregation/grain/evidence_refs, but not database_source or validation description. Evidence `e`, if present, is emitted with its source/query/result/method/time. If validation contains no evidence key, `_mapping_evidence_refs` returns its default empty list rather than falling back to top-level evidence; `_mapping_evidence` in validation uses the same precedence. Thus preservation is conditional on supported shapes, not every conceivable evidence field combination. No new data proposition is invented by this extraction; loss of qualifying metadata can still limit warrant at the consumer.

- Immediate return: Extracted root browse/resolve/evidence views serialized by MCP.
- Later read-back: Persisted records are loaded again on subsequent semantic invocations; this route does not write a revision.
- Delegated visibility: Host receives projected fields, not full raw version files automatically.
- Selection predicate: Selected version, active/validated attached records, matching term IDs and existing evidence IDs; duplicate evidence IDs suppressed.
- Invalidation or expiry: Reload follows version selector; removed/inactive objects disappear from subsequent filtered delivery, not from prior model context.
- Activation or effect: Wired projection of delivered guidance; actual model behavior change unobserved.
- Evidence limits: Root implementation only; no observed store instance or benchmark-variant parity established here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `evoontology/ontology/models.py`, `evoontology/runtime/runtime.py`, `evoontology/runtime/mcp_server.py`.

> "term_id": m.term_id,
> "table": m.table,
> "column": m.column,
> "semantic_filter": m.semantic_filter,
> "aggregation_semantics": m.aggregation_semantics,
> "grain": m.grain,
> "evidence_refs": list(m.evidence_refs),
> --- `evoontology/runtime/runtime.py`

> val_evidence = validation.get("evidence", [])
> if isinstance(val_evidence, list):
>     return [str(e) for e in val_evidence]
> return _evidence_refs(data)
> --- `evoontology/ontology/models.py`

> for m in self.store.mappings.values()
> if _is_active(m) and m.term_id == term_id
> ]
> if mappings:
>     result["mappings"] = mappings
> --- `evoontology/runtime/runtime.py`

> elif result.get("mappings") or result.get("relations") or result.get("constraints"):
>     result["coverage_status"] = "supported"
> --- `evoontology/runtime/runtime.py`

> return getattr(item, "lifecycle_state", "active") in _ACTIVE_STATES
> --- `evoontology/runtime/runtime.py`

#### EPI-RTE-gate-aggregation
Label: Gate input aggregation
Part of: [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission)

This is the check component, not publication/disposition. Endpoints: current-round candidate evaluation summary → input validity/protocol/regression checks → EvaluationGate aggregate → accept Boolean consumed by session. Owner: deterministic session and EvaluationGate. State: recorded gate_input, frozen optional expected protocol. Domain: finite paired GT numbers with matching unique case IDs, or valid nonempty decoded verdicts. Formal inference: supplied parent scores `[0, 1]`, candidate `[1, 1]` entail averages 0.5 and 1 and a positive delta under inspected arithmetic; these invented illustrative inputs are not run evidence or warranted measurements. Likewise one candidate win/no critical error entails the judge gate's accept under its counting rule. Neither rule checks repeatability or independence.

Proposer: caller supplies observations and regression conclusion; decider: deterministic gate; veto: session rejects malformed/non-improving inputs. Human contribution: unresolved caller identity; scope/budget confirmation does not authenticate observations. Answer oracle: external GT scorer may have one; core arithmetic has none of its own, and model pairwise judging is not an expected-answer oracle. Operating modes: GT paired scores or no-GT winner counts. Improvement trigger/admission guidance and rejection/recovery of whole candidates remain in the enclosing runtime route; this part produces a check result rather than installing changes.

- Immediate return: accept/protocol and mean/delta or winner/tie/error counts; invalid inputs raise error.
- Later read-back: Chosen gate result is stored in accepted run state; evaluation summaries remain available to later host work.
- Delegated visibility: Caller submits result.gate_input through MCP; accept returns publication/error while run state retains gate.
- Selection predicate: Latest recorded current-round/current-candidate summary with gate_input; protocol must match frozen expected protocol when present.
- Invalidation or expiry: Gate is recomputed on accept; input artifacts/claims are not independently authenticated or expired.
- Activation or effect: Wired necessary session publication condition; direct selection is outside this veto.
- Evidence limits: Arithmetic checks conditional supplied assertions only; no observed evaluator execution, reproducibility or causal benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `evoontology/evaluation/evaluation.py`, `evoontology/evolution/session.py`. See enclosing [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission) for full theory-property account; numerical ordering does not establish content-directed theory criticism.

> parent_avg = sum(parent_scores) / len(parent_scores)
> candidate_avg = sum(candidate_scores) / len(candidate_scores)
> return {
>     "accept": candidate_avg > parent_avg,
> --- `evoontology/evaluation/evaluation.py`

> accept = (e_c == 0) and (w_c > w_p)
> --- `evoontology/evaluation/evaluation.py`

> if not parent or len(parent) != len(candidate) or len(cases) != len(parent) or len(set(cases)) != len(cases):
>     raise EvolutionError("Gate needs paired scores with unique matching case_ids")
> --- `evoontology/evolution/session.py`

> if supplied.get("unacceptable_regressions") is not False:
>     raise EvolutionError("Evaluation must explicitly rule out unacceptable regressions")
> --- `evoontology/evolution/session.py`

#### EPI-RTE-sql-comparison
Label: BIRD SQL comparison
Part of: [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation)

Material evaluator part, not a duplicate of adapter subprocess execution. Endpoints: predicted/reference SQL and database path → read-only SQLite executions → sorted tuple equality → optional timing ratio. Owner: `evaluate_sql`; context: one database/question. Target: extensional row equivalence, including duplicates but disregarding row order and column names. Answer oracle: supplied gold SQL execution, whose correctness is not validated by this routine. Proposer: agent supplies predicted SQL; reference comes from benchmark; decider: deterministic scorer; no human per-case approval established. Mode: benchmark per-question comparison. It generates observations, not successor admission; downstream pairing and veto are separate.

- Immediate return: `(False, 0.0)` on empty prediction/error/mismatch, otherwise true and timing ratio or zero.
- Later read-back: Driver score artifacts and normalized adapter results can be recorded in session evaluations; this helper itself does not persist.
- Delegated visibility: Driver/adapter expose metrics/artifacts to caller; gold is scorer input, not an ontology acceptance oracle.
- Selection predicate: Caller database path and predicted/gold SQL strings.
- Invalidation or expiry: Result applies to that database instance and measurement conditions; no automatic expiry proven.
- Activation or effect: Wired score production consumed by benchmark metrics; no direct ontology publication.
- Evidence limits: No executed comparison supplied. Dataset correctness, SQL semantic intent, portability and causality unestablished; exception handling can conflate execution failure with mismatch.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `benchmarks/bird/run_evaluation.py`.

> cursor = conn.execute(gold_sql)
> gold_rows = [tuple(row) for row in cursor.fetchall()]
> --- `benchmarks/bird/run_evaluation.py`

> ex = (sorted(pred_rows) == sorted(gold_rows))
> --- `benchmarks/bird/run_evaluation.py`

> ves = gold_time / pred_time
> return (True, ves)
> --- `benchmarks/bird/run_evaluation.py`

### Claims

#### EPI-CLM-grounded-commitment
Label: Grounded semantic commitment

Claimed operation: commit semantic objects only after verification against underlying data and reuse them as grounded knowledge. Evidence layer: doctrine/design. Source: SRC-1, `README.md`, elaborated by Build instructions. This is distinct from [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success): initial semantic grounding rather than comparative successor performance.

> | **Grounded construction** | Build around the workload and commit semantic objects only after verification against the underlying data. |
> --- `README.md`

> The ontology layer should preserve the workload coverage map while storing
> only validated semantic knowledge.
> --- `plugins/evoontology-codex/skills/build-ontology/SKILL.md`

> - verify the selected grounding's meaning, scope, and granularity;
> - record supporting evidence, including why competing candidates were not
>   selected when the distinction is analytically important.
> --- `plugins/evoontology-codex/skills/build-ontology/SKILL.md`

> - Evidence can be reproduced;
> --- `plugins/evoontology-codex/skills/build-ontology/SKILL.md`

> Revise unsupported, ambiguous, incomplete, or schema-invalid objects.
> --- `plugins/evoontology-codex/skills/build-ontology/SKILL.md`

#### EPI-CLM-gated-versioning
Label: Paired gated versioning

Claimed operation: publication only after paired reproducible improvement. Evidence layer: doctrine/design. Source: SRC-1, `README.md`. Possible overlap with [RT-CLM-evolution-success](runtime.md#rt-clm-evolution-success): this public claim specifies the publication condition; runtime's claim specifies the broader search completion objective. They are not independent corroboration.

> | **Gated versioning** | Publish a Candidate only when paired evaluation shows a reproducible improvement over its Parent. |
> --- `README.md`

> When the validation set is small, re-run the evaluation to confirm the
> improvement is not single-trial luck. Evaluation should also deepen
> understanding of ontology-layer limitations and guide future optimization.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

> 1. Update the problem map and causal understanding.
> 2. Mark solved problems, remaining limitations, newly discovered issues, and disproven explanations.
> 3. Preserve the main validated mechanisms, rejected hypotheses, and unresolved uncertainty needed for later rounds.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; the ledger cites supplied runtime paths.
