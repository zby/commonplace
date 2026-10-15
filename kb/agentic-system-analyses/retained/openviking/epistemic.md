---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenViking epistemic routes: memory proposals, structural checks, recall authority and rollout-driven policy updates at the frozen revision."
run-id: AAS-2026-10-14-openviking-7b5b57541af5-01
reviewed-boundary: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
---

# OpenViking epistemic report

## Source-and-claim boundary

The question is which routes acquire or produce truth-apt content, what their checks license, and how their results reach consequential consumers. Scope and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). This is a complete artifact with partial loop coverage, not a system-complete epistemic audit. All additional reads below concern SRC-1 at the frozen revision. Implementation and doctrine are distinguished; no observed run or causal experiment is supplied. No target execution was performed.

The main public claims are inspectable agent knowledge, reusable experience, and benchmark benefit: [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge), [EPI-CLM-reusable-experience](#epi-clm-reusable-experience), [EPI-CLM-memory-benefit](#epi-clm-memory-benefit). These are not all claims of validated truth. In particular, a context database may usefully retain unverified records without constituting an acceptance procedure for their assertions.

| Entry point or operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| Python command dispatch | `pyproject.toml`; `openviking_cli/rust_cli.py` | Direct reads: ov/openviking forward to a located Rust binary except doctor. No inference that the Python wrapper implements memory admission. Full native dispatch remains uninspected. |
| HTTP session search, find and context mode | `openviking/server/routers/search.py`; `openviking/storage/viking_fs/_semantic.py` | Supplied [RT-RTE-session-search](runtime.md#rt-rte-session-search), [RT-RTE-direct-find](runtime.md#rt-rte-direct-find), [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly); not independently reread here. Establish selection and context assembly, not factual checking. |
| Digest rewrite, checking and host selection | `openviking/retrieve/context_assembler/rewrite.py`; `openviking/prompts/templates/retrieval/recall_rewrite.yaml` | Direct reads: [EPI-RTE-digest-contract](#epi-rte-digest-contract); supplied [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall) supplies consequential delivery. |
| Commit and extraction | `openviking/session/compressor_v3.py`; `openviking/session/memory/extract_loop.py` | Commit/compressor supplied through [RT-RTE-session-commit](runtime.md#rt-rte-session-commit); direct reads of loop resolution/refetch/patch repair and validator: [EPI-RTE-memory-guards](#epi-rte-memory-guards). Protocol equivalence/security is not established. |
| Direct session extract | `openviking/server/routers/sessions.py`; `openviking/service/session_service.py` | Router search and direct service read show /extract invokes compressor on current messages, with manual_extract archive identity. Same downstream submission family, not proof of the commit archive/recovery protocol on this alternate. |
| Upsert, merge, delete, lineage and vectorization handoff | `openviking/session/memory/memory_updater.py`; `openviking/session/memory/merge_op/replace.py` | Direct selected reads: [EPI-RTE-memory-write](#epi-rte-memory-write), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal). Full index cleanup and concurrency semantics remain uninspected. |
| Memory compile/consolidation | `crates/ov_cli/src/main.rs`; `openviking/service/compile_service.py`; `openviking/service/memory_compile.py`; `openviking/session/memory/consolidation_context_provider.py` | CLI/service searches plus direct runner/provider reads: [EPI-RTE-memory-consolidation](#epi-rte-memory-consolidation). General VikingBot skill-driven compile remains uninspected. |
| Registered extraction tools | `openviking/session/memory/tools.py` | Registry search identifies read/search/ls; direct read implementation inspection shows metadata/link hiding and optional line slicing. Together with supplied ExtractLoop account, limits claims that the model sees all provenance or has arbitrary write tools. |
| User preference and experience schemas | `openviking/prompts/templates/memory/preferences.yaml`; `openviking/prompts/templates/memory/experiences.yaml` | Direct reads: factual content and instruction content distinguished in [EPI-OBJ-memory-fields](#epi-obj-memory-fields), [EPI-OBJ-experience-instructions](#epi-obj-experience-instructions). Other schemas and account overrides remain uninspected. |
| Rollout evaluation and training | `openviking/session/train/components/trajectory_analyzer.py`; `openviking/session/train/components/gradient_estimator.py`; `openviking/session/train/components/policy_trainer.py`; `openviking/session/train/engine.py`; `openviking/session/train/pipeline.py` | Direct selected reads: [EPI-RTE-rollout-feedback](#epi-rte-rollout-feedback), [EPI-RTE-policy-training](#epi-rte-policy-training). Concrete evaluator implementations, benchmark harnesses and all streaming/remote variants are not traced. |
| Conditional skill updates and model config | `openviking/session/train/components/skill_policy_updater.py`; `openviking/config/manager.py` | Supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [RT-RTE-config-patch](runtime.md#rt-rte-config-patch). No new execution/rollback evidence. |
| Plugin hooks and bot consumers | `examples/opencode-plugin/index.mjs`; `bot/vikingbot/agent/context.py` | Supplied boundary/runtime findings only. OpenCode injection has a traced consumer; bot persistence, gateway, other hooks and actual host behavior remain unresolved. |
| Resource acquisition, manual skill edits, filesystem/WebDAV writes and watches | `openviking/server/routers/resources.py`; `openviking/server/routers/skills.py`; `openviking/server/routers/filesystem.py`; `openviking/server/routers/webdav.py`; `openviking/server/routers/watches.py` | Router searches identify alternate admission/deletion surfaces, not end-to-end epistemic assessment. Parser/privacy/summary generation, refresh, manual approval and withdrawal propagation remain uninspected. Prevents a universal acceptance/lineage/withdrawal conclusion. |

Unavailable provider internals prevent identifying exact deployed parameters, internal learning or truth-checking by configured models; see [RT-CMP-query-planner](runtime.md#rt-cmp-query-planner), [RT-CMP-account-vlm](runtime.md#rt-cmp-account-vlm), [RT-CMP-account-embedder](runtime.md#rt-cmp-account-embedder), [RT-CMP-rerank-client](runtime.md#rt-cmp-rerank-client). Missing candidate/input/output traces prevent semantic classification of actual extracted memories and digests, and prevent observations of acceptance or changed behavior. Available but uninspected benchmark protocols prevent finer attribution of reported benefit. These are separate limits, not evidence that those routes do not exist.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit) | Message assertions can be truth-apt; archive/task markers are scheduling state | see record | SRC-1, `openviking/session/session.py` | Supplied record; imported assertions are not authenticated facts. |
| [RT-OBJ-query-plan](runtime.md#rt-obj-query-plan) | Query requests have no necessary truth assertion; natural-language reasoning may, but actual content is not determinable | see record | SRC-1, `openviking/retrieve/intent_analyzer.py` | Planning selects investigations; not a fact acceptance certificate. |
| [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | Preferences and other model-proposed assertion fields | see record | SRC-1, `openviking/prompts/templates/memory/preferences.yaml` | Content instances, fidelity and source warrant unknown. |
| [EPI-OBJ-experience-instructions](#epi-obj-experience-instructions) | Imperatives are policy; generality and effectiveness claims about their conditions can be truth-apt | see record | SRC-1, `openviking/prompts/templates/memory/experiences.yaml` | A schema's abstraction instruction does not establish an actual accepted generalization. |
| [EPI-OBJ-recall-digest](#epi-obj-recall-digest) | Model-written factual bullets attributed to retained URIs | see record | SRC-1, `openviking/retrieve/context_assembler/rewrite.py` | Citation membership is checked; entailment by cited text is not thereby checked. |
| [EPI-OBJ-trajectory-evaluation](#epi-obj-trajectory-evaluation) | Pass/score/criterion feedback, or extraction-existence result | see record | SRC-1, `openviking/session/train/components/trajectory_analyzer.py` | Evaluator-dependent target; fallback does not measure task success. |
| [RT-OBJ-config-settings](runtime.md#rt-obj-config-settings) | No necessary truth-apt content: administrative selectors | see record | SRC-1, `openviking/config/manager.py` | Settings validation is not an epistemic acceptance decision. |

## Authority-route ledger

Fields owned by a cited record are given by that record; the overlay below assesses content relation, evaluator license and architectural status. All implementation rows are unobserved in this run. Multiple rows for one record separate its functions; retention is not labeled lifecycle integration.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-session-commit](runtime.md#rt-rte-session-commit) | retention | implemented | [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit) | truth-apt transformation: acquisition/import | Session messages to archive | see record | see record | see record | see record | Preserves a trace of assertions; source truth/warrant unknown | see record | see record | SRC-1, `openviking/session/session.py` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Archive retention is not content acceptance. |
| [RT-RTE-session-commit](runtime.md#rt-rte-session-commit) | content transformation | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | truth-apt transformation: indeterminate | Messages and retrieved memory to proposed fields | Account VLM, schema/provider instructions; semantic fidelity not established | see record | Model-proposed operations | see record | Candidate production only; cannot establish preservation, entailment or novelty for actual unseen outputs | see record | see record | SRC-1, `openviking/session/compressor_v3.py` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Non-ampliative reshaping, derivation and conjecture remain distinguishable only with content evidence. |
| [EPI-RTE-memory-guards](#epi-rte-memory-guards) | check/evidence production | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | no content change | Operation resolvability, prior-read and patch applicability | see record | see record | see record | see record | Mechanical applicability within checked domain, not truth of edited assertions | see record | see record | SRC-1, `openviking/session/memory/extract_loop.py` | none | none | Refetch and repair are not independent factual tests; one repair is not guaranteed validation success. |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | disposition/acceptance | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | no content change | Operation eligible for physical application | see record | see record | see record | see record | Operational admission only; no claim acceptance criterion for a named epistemic use in inspected updater | see record | see record | SRC-1, `openviking/session/memory/memory_updater.py` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Successful writes do not establish truth acceptance. |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | retention | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | truth-apt transformation: indeterminate | Prior fields plus model updates to retained content | Schema merge operations; see record | see record | see record | see record | Unknown semantic warrant; exact replacement can replace a true assertion with a false one | see record | see record | SRC-1, `openviking/session/memory/merge_op/replace.py` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Merge instruction is not an entailment proof. |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | lineage/freshness/recovery | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | no content change | Source/update identifiers and latest stored content | see record | see record | see record | see record | Traceability aids, not verified provenance or endorsement | see record | see record | SRC-1, `openviking/session/memory/memory_updater.py` | none | none | Fallback to prefetched content on read failure; lineage may be partial. |
| [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | no content change | Proposed deletes and replacement dependencies | see record | see record | see record | see record | Withdrawal is a model/software disposal decision, not a demonstrated falsification | see record | see record | SRC-1, `openviking/session/memory/memory_updater.py` | none | none | Full index and already-delivered host-context withdrawal not established. |
| [EPI-RTE-memory-consolidation](#epi-rte-memory-consolidation) | content transformation | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | truth-apt transformation: indeterminate | Existing memories reorganized in place | see record | see record | see record | see record | Non-ampliative reshaping is requested; actual semantic preservation unestablished | see record | see record | SRC-1, `openviking/session/memory/consolidation_context_provider.py` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Upserts/deletes use existing write/withdrawal mechanisms, not a new acceptance gate. |
| [RT-RTE-session-search](runtime.md#rt-rte-session-search), [RT-RTE-direct-find](runtime.md#rt-rte-direct-find) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-fields](#epi-obj-memory-fields) | no content change | Which stored context is returned | see records | see records | see records | see records | Relevance/scope license, not source endorsement or answer correctness | see records | see [RT-BAP-planner-dispatch](runtime.md#rt-bap-planner-dispatch) | SRC-1, `openviking/storage/viking_fs/_semantic.py` | [RT-CLM-scoped-retrieval](runtime.md#rt-clm-scoped-retrieval) | none | Filter-only lookup has no similarity evidence; reranking is optional. |
| [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) | content transformation | implemented | [EPI-OBJ-recall-digest](#epi-obj-recall-digest) | truth-apt transformation: indeterminate | Selected fragments to factual digest | Model relevance compressor, supplied fragments only | see record | Digest, no_relevant or fallback | see record | Compression requested; semantic preservation unestablished | see record | see record | SRC-1, `openviking/prompts/templates/retrieval/recall_rewrite.yaml` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Actual digest instances absent; cannot infer conjecture solely from model use. |
| [EPI-RTE-digest-contract](#epi-rte-digest-contract) | check/evidence production | implemented | [EPI-OBJ-recall-digest](#epi-obj-recall-digest) | no content change | Bullet shape, length, URI membership and empty/no-relevant token | see record | see record | see record | see record | URI-domain and presentation contract only; no text entailment license | see record | see record | SRC-1, `openviking/retrieve/context_assembler/rewrite.py` | none | none | A false assertion with a valid source URI passes the mechanical contract. |
| [EPI-RTE-digest-contract](#epi-rte-digest-contract) | disposition/acceptance | implemented | [EPI-OBJ-recall-digest](#epi-obj-recall-digest) | no content change | Normalized result to ok/no_relevant/failed | see record | see record | see record | see record | Operational digest admission, not epistemic claim acceptance | see record | see [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall) | SRC-1, `openviking/retrieve/context_assembler/rewrite.py` | none | none | no_relevant can suppress host-visible recall despite retained entries. |
| [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall) | operational admission/selection/consumption | implemented | [EPI-OBJ-recall-digest](#epi-obj-recall-digest) | no content change | Digest/rendered selection to host input | see record | see record | see record | see record | Delivered context has advisory content authority, not hard truth/instruction enforcement | see record | see [RT-BAP-recall-context](runtime.md#rt-bap-recall-context) | SRC-1, `examples/opencode-plugin/lib/memory-recall.mjs` | [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | none | Delivery is wired; actual consumption/compliance unobserved. |
| [EPI-RTE-rollout-feedback](#epi-rte-rollout-feedback) | check/evidence production | implemented | [EPI-OBJ-trajectory-evaluation](#epi-obj-trajectory-evaluation) | truth-apt transformation: entailed derivation | Fallback proposition: at least one extracted trajectory exists | Boolean list-existence check, not rollout success | see record | see record | see record | For a supplied nonempty list, existence follows; input authenticity remains unknown | see record | see record | SRC-1, `openviking/session/train/components/trajectory_analyzer.py` | [EPI-CLM-memory-benefit](#epi-clm-memory-benefit) | none | Optional externally supplied/evaluator result has a separate, uninspected target/domain; this derivation classifies only fallback. |
| [EPI-RTE-rollout-feedback](#epi-rte-rollout-feedback) | operational admission/selection/consumption | implemented | [EPI-OBJ-trajectory-evaluation](#epi-obj-trajectory-evaluation) | no content change | Evaluation feedback to extraction and gradient estimation | see record | see record | see record | see record | Evaluator-dependent feedback, not proof of proposed memory's truth or transfer | see record | see record | SRC-1, `openviking/session/train/components/trajectory_analyzer.py` | [EPI-CLM-reusable-experience](#epi-clm-reusable-experience) | none | Fallback is computed after extraction and is not retroactively injected into that same extraction. |
| [EPI-RTE-policy-training](#epi-rte-policy-training) | behavior/policy adaptation | implemented | [EPI-OBJ-experience-instructions](#epi-obj-experience-instructions) | non-truth-apt policy/content update: model-proposed reusable instructions | Analyses to gradients to policy patches and next policy set | see record | see record | see record | see record | Operational policy updating; generality/effectiveness remains candidate-level | see record | see record | SRC-1, `openviking/session/train/engine.py` | [EPI-CLM-reusable-experience](#epi-clm-reusable-experience), [EPI-CLM-memory-benefit](#epi-clm-memory-benefit) | none | Evaluator presence is not universal: extracted-trajectory existence can supply passed. |
| [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | behavior/policy adaptation | implemented | [EPI-OBJ-experience-instructions](#epi-obj-experience-instructions) | non-truth-apt policy/content update: conditional skill instruction patches | Trace-derived skill proposals to applied skill files | see record | see record | see record | see record | Reusable instruction admission, not effectiveness validation | see record | see record | SRC-1, `openviking/session/train/components/skill_policy_updater.py` | [EPI-CLM-reusable-experience](#epi-clm-reusable-experience) | none | Related instruction class, not identity with experiences schema. |
| [RT-RTE-config-patch](runtime.md#rt-rte-config-patch) | behavior/policy adaptation | implemented | [RT-OBJ-config-settings](runtime.md#rt-obj-config-settings) | non-truth-apt policy/content update: model/resource selection | Config patch to later model resolution | see record | see record | see record | see record | No epistemic claim license | see record | see [RT-BAP-config-model](runtime.md#rt-bap-config-model) | SRC-1, `openviking/config/manager.py` | none | none | No numerical training or self-improvement result follows. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-agent-knowledge](#epi-clm-agent-knowledge) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-session-commit](runtime.md#rt-rte-session-commit), [EPI-RTE-memory-write](#epi-rte-memory-write), [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall) | None supplied | No evidence that filesystem inspectability or relevance implies fact correctness | Persistent, editable and recallable context is supported | “Knows” cannot be upgraded to verified assertions. |
| [EPI-CLM-reusable-experience](#epi-clm-reusable-experience) | see record | SRC-1, `openviking/prompts/templates/memory/experiences.yaml`; doctrine/design | see record | [EPI-RTE-rollout-feedback](#epi-rte-rollout-feedback), [EPI-RTE-policy-training](#epi-rte-policy-training), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) | None supplied | No actual candidate/generalization or transfer comparison | Trace-fed reusable-policy proposal and application machinery is supported | Universal applicability and warranted explanation not established. |
| [EPI-CLM-memory-benefit](#epi-clm-memory-benefit) | see record | SRC-1, `README.md`; reported operation | see record | [EPI-RTE-policy-training](#epi-rte-policy-training) provides related machinery, not provenance for reported benchmark | Attributed results only, no registered trace | Benchmark harness uninspected; even memory/no-memory contrast would identify the varied package, not every component or explanatory mechanism | The repository reports benchmark gains | No reproduced benefit, component attribution or safe transfer finding. |

## Bounded conclusion

OpenViking's inspected paths retain imported assertions and model-proposed memory, select it by scope and relevance, optionally reshape it, and wire selected text into a shipped host callback. Archive integrity, operation applicability, citation membership and semantic relevance are different checking domains. None can be substituted for a check of the truth of the recalled assertions. The counterexample in [EPI-RTE-digest-contract](#epi-rte-digest-contract) establishes this separation from implementation alone.

Source warrant for acquired messages/resources is unknown here. Extraction and consolidation ask models to preserve or abstract content, but actual input/output claims are not supplied. Therefore semantic preservation, entailed derivation and ampliative conjecture remain unresolved for those outputs. There is a narrow implemented entailed derivation in the fallback extraction-existence evaluation; it says nothing about task success. No inspected route establishes acceptance of a produced ampliative claim against an evidence-consuming criterion naming intended use and scope. This is a bounded finding about the traced paths, not an absence finding across all included operations.

Memory write guards license operational application. Successful files become retrievable, and replacement/deletion can change future reliance; retained trace/update identifiers and migrated links are lineage aids. These effects occur without demonstrated epistemic acceptance, so they are retention, organization and operational use, not acceptance-followed-by-lifecycle-integration in the report's technical sense. Physical withdrawal is wired with replacement protections; full propagation to indices and already-delivered host context is unresolved. See [EPI-RTE-memory-write](#epi-rte-memory-write), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal).

Rollout training has consequential feedback consumers and successor-policy wiring. It is stronger than an unused evaluator report, but weaker than demonstrated improved capacity or validated knowledge production. External/reference evaluation can be supplied; without it a passed result may mean only that a trajectory was extracted. Reusable instruction updates are a direct behavior-shaping route even when their imperatives are not truth-apt propositions. Evaluation-only passes collect reports; the inspected pipeline does not turn a reported score delta into an automatic accept/rollback criterion. See [EPI-RTE-rollout-feedback](#epi-rte-rollout-feedback), [EPI-RTE-policy-training](#epi-rte-policy-training).

Learning, reflection, autonomy and theory-building remain independent questions. Instruction parts are addressable and persist; that alone establishes neither whole explanatory theories, content-directed criticism with blame allocation, nor criticism-dependent theory revision. Actual learning and exercised self-improvement are unestablished without later operation and attribution evidence. Configurable inference clients also do not resolve provider-side learning or immutable parameter identity. No single system-wide epistemic verdict follows from these route-level findings.

## Shared records

### Operative objects

#### EPI-OBJ-memory-fields
Label: Memory assertion fields

Source-native identity: schema-defined content fields and associated MemoryFile metadata admitted by MemoryUpdater. Representational form: natural-language assertions in content; symbolic identity/version/source identifiers are distinct metadata consumers. Storage substrate: VikingFS files with indexing handoff. SRC-1, `openviking/prompts/templates/memory/preferences.yaml`; `openviking/session/memory/memory_updater.py`. No counterpart after comparison with supplied objects: [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit) is the archive/queue input, not the resulting memory files.

> User preference memory - captures "what the user likes/dislikes or is accustomed to".
> Extract specific preferences the user has expressed across conversations.
> --- `openviking/prompts/templates/memory/preferences.yaml`

The schema identifies potential truth-apt assertions, not their actual truth. Ordinary user testimony, assistant statements and extracted formulations need not share warrant. The source sample supplies no actual memory candidate whose fidelity can be assessed.

#### EPI-OBJ-experience-instructions
Label: Experience content instructions

Source-native identity: experiences schema content field. Representational form: natural-language imperatives interpreted by a future agent; scope/effectiveness implications may be truth-apt but require content-specific assessment. Storage substrate: files under the schema's user-memory directory. SRC-1, `openviking/prompts/templates/memory/experiences.yaml`. Distinct from [RT-OBJ-session-commit](runtime.md#rt-obj-session-commit) and [EPI-OBJ-memory-fields](#epi-obj-memory-fields): policy instructions have a different content contract and downstream authority from preference assertions. Related to, not identical with, the skill files in [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission).

> Structured experience extraction in EXACTLY this 3-section format. This output will be injected directly into an autonomous agent's system prompt, so it MUST be written as strict, executable machine instructions:
> --- `openviking/prompts/templates/memory/experiences.yaml`

> - ABSTRACTION MANDATE: Strip away specific entities, IDs, user names, or raw text from the past trajectory. Use generalized abstract descriptions so the rule applies universally.
> --- `openviking/prompts/templates/memory/experiences.yaml`

These are instructions to produce reusable policy, not evidence that universal scope is warranted or that system-prompt injection actually occurred.

#### EPI-OBJ-recall-digest
Label: Recall digest bullets

Source-native identity: digest string returned by rewrite_context/normalize_digest. Representational form: natural-language bullets with symbolic URI-membership checking. Storage substrate: transient response and possible host text part, not a new retained database object in this route.
Part of: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly)

The parent is a route; this object is its model-written output part, distinct from the input entries. SRC-1, `openviking/retrieve/context_assembler/rewrite.py`; `openviking/prompts/templates/retrieval/recall_rewrite.yaml`.

> Report only facts found in the fragments; never restate the user query as a
> fact. Do not tell the agent what to do with them: no advice, instructions,
> warnings, or next steps of your own.
> --- `openviking/prompts/templates/retrieval/recall_rewrite.yaml`

This supports the intended factual contract, not compliance.

#### EPI-OBJ-trajectory-evaluation
Label: RubricEvaluation results

Source-native identity: RubricEvaluation attached to RolloutAnalysis, including supplied/evaluator-produced results and trajectory_extracted fallback. Representational form: symbolic passed/score/criterion fields plus natural-language feedback and evidence URI strings. Storage substrate: process-local analysis and downstream report/model-input structures; complete durable result retention uninspected. SRC-1, `openviking/session/train/components/trajectory_analyzer.py`. No supplied counterpart: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) mentions trajectory judgment but does not individuate the evaluation object or its fallback target.

> criterion_name="trajectory_extracted",
> --- `openviking/session/train/components/trajectory_analyzer.py`

### Routes

#### EPI-RTE-digest-contract
Label: Digest contract checking and admission
Part of: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly)

Endpoints/progression/owner: rewrite_context obtains model text, normalize_digest filters bullets and URI membership, then rewrite_context selects ok/no_relevant/failed; caller assembly and recall selector consume the result. Code owns mechanical checking/disposition; the model proposes content and relevance. Human per-bullet approval and an expected-answer oracle are not present in this inspected function. Operating mode: query-driven context preparation. SRC-1, `openviking/retrieve/context_assembler/rewrite.py`; consequential consumers supplied by [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall).

- Immediate return: digest, status and optional usage, or timeout/failed fallback status.
- Later read-back: inapplicable — this check does not persist a new database artifact; host-history retention is host-dependent and uninspected.
- Delegated visibility: rewrite sees selected rendered fragments; host can receive normalized bullets instead of those fragments.
- Selection predicate: bullet prefix, truncation to 500 characters, at least one URI, all cited URIs within valid_uris when provided, count limit; whole-output NO_RELEVANT_MEMORY is a separate result.
- Invalidation or expiry: transient result for the current request; later requests regenerate it.
- Activation or effect: ok permits digest preference; no_relevant suppresses rendered recall/cooling and client injection; failed/timeout leaves fallback available through supplied consumers. Wiring, not observed behavior.
- Evidence limits: no comparison of a bullet proposition against its cited source text occurs in normalize_digest; truth/relevance correctness and actual host use remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> cited = URI_PATTERN.findall(cleaned)
> if not cited or (enforce_provenance and any(uri not in allowed for uri in cited)):
>     continue
> bullets.append(cleaned)
> --- `openviking/retrieve/context_assembler/rewrite.py`

> if digest:
>     return digest, "ok", usage
> if response_text.upper() == "NO_RELEVANT_MEMORY":
>     return "", "no_relevant", usage
> return "", "failed", usage
> --- `openviking/retrieve/context_assembler/rewrite.py`

Concrete implementation deduction, not target execution: set valid_uris to {viking://user/alice/memories/preferences/editor.md}. Suppose the source says Alice prefers Vim, but raw text is `- Alice prefers Emacs. source: viking://user/alice/memories/preferences/editor.md`. It begins with a bullet, is shorter than 500 characters, and its sole extracted URI is allowed. It is appended and receives the digest header, hence an ok result. The checker has no source-body argument with which to reject the contradiction. Conversely, an invented URI is rejected; this positive guard prevents the stronger, false claim that provenance is entirely unchecked. URI membership is weaker than proposition support.

#### EPI-RTE-memory-guards
Label: Extraction mechanical guards
Part of: [RT-RTE-session-commit](runtime.md#rt-rte-session-commit)

Endpoints/progression/owner: ExtractLoop model operations → resolution → optional resolution repair → unread-existing-file refetch → patch validation/repair → finalize_operations. This is a material inner part of the supplied commit container, also reused by consolidation. Model proposes; parser/resolution/code can reject, repair or refetch; the model regenerates. No expected-answer oracle is used by the inspected patch validator. Operating mode: open trace-fed extraction with bounded repair opportunities, not a factual experiment. SRC-1, `openviking/session/memory/extract_loop.py`.

- Immediate return: finalized resolved operations and tools_used, or terminal parsing/completion failure.
- Later read-back: inapplicable — these checks do not themselves persist a new artifact; admitted operations reach the separate updater.
- Delegated visibility: selected read/search/ls results enter the extraction model's local messages; tools may hide links/backlinks and slice visible text while retaining the full parsed file in read_file_contents.
- Selection predicate: schema/protocol resolution, existing target reads, patch matching/application and repair counters.
- Invalidation or expiry: current loop only; operations are checked against inspected/prefetched material, not a proven stable global snapshot.
- Activation or effect: errors can request another generation, refetch adds context, unrecoverable parse failures raise; patch errors receive one repair opportunity before loop completion logic proceeds.
- Evidence limits: checking applicability is not checking revised content truth; source does not justify an invariant that every final patch passed after retry. Full Python DSL security and all output protocols uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> patch_errors = await self._validate_patch_operations(final_operations)
> if patch_errors and patch_repair_count == 0:
>     patch_repair_count += 1
> --- `openviking/session/memory/extract_loop.py`

> if applied_content != working_content:
>     working_content = applied_content
>     continue
> --- `openviking/session/memory/extract_loop.py`

The latter is the validator's practical success condition for a block, not semantic fidelity. The read tool independently limits provenance visible to the model:

> llm_result.pop("links", None)
> llm_result.pop("backlinks", None)
> --- `openviking/session/memory/tools.py`

#### EPI-RTE-memory-write
Label: Memory operational admission and retention
Part of: [RT-RTE-session-commit](runtime.md#rt-rte-session-commit)

Endpoints/progression/owner: MemoryUpdater.apply_operations → error/migration/URI checks → per-URI _apply_upsert → latest read or prefetched fallback → schema merge → version/lineage metadata → write_file → vectorization/resource/link maintenance. This is the updater part left unresolved by the supplied commit record, not a replacement for its archive/queue identity. SRC-1, `openviking/session/memory/memory_updater.py`; `openviking/session/memory/merge_op/replace.py`.

- Immediate return: MemoryUpdateResult written/edited/deleted/skipped/error collections; partial per-operation failures can coexist with successful writes.
- Later read-back: memory files become inputs to retrieval, later extraction and policy loading; complete backend read/index consistency is uninspected.
- Delegated visibility: updater receives model fields, schema and RequestContext; later readers can receive selected content rather than original messages or update rationale.
- Selection predicate: resolved URIs, error/migration validation, schema merge operation and filesystem success; malformed/unresolved operations may be rejected or skipped.
- Invalidation or expiry: later upserts replace/patch fields; deletion is a separate route; version/source identifiers aid tracking but no truth expiry is enforced here.
- Activation or effect: writes persist content and invoke index/link maintenance. This admits future operational use, not proof of later model behavior.
- Evidence limits: no inspected claim-truth acceptance criterion; per-URI and per-field recovery is not established all-or-nothing rollback. Full vectorization/concurrency behavior remains uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger is compressor/consolidator operations. Model supplies candidate fields; software decides mechanical admission and performs I/O. Human initiation is not per-content approval. No expected-answer oracle occurs in these inspected updater stages. Guidance is schema merge policy; persisted product is memory text plus metadata. Old values can survive field merge failure; errors are recorded, not a proven global transaction rollback.

> if operations.has_errors():
>     for error in operations.errors:
>         result.add_error("unknown", ValueError(error))
>     return result
> --- `openviking/session/memory/memory_updater.py`

> if source_extraction_id:
>     metadata["source_extraction_id"] = str(source_extraction_id)
> source_trace_id = _operation_trace_id(resolved_op)
> if source_trace_id:
>     metadata["last_update_trace_id"] = source_trace_id
> --- `openviking/session/memory/memory_updater.py`

> if patch_value is None or patch_value == "":
>     return current_value
> return patch_value
> --- `openviking/session/memory/merge_op/replace.py`

Concrete implementation deduction: ReplaceOp with current text `Alice prefers Vim` and nonempty patch `Alice prefers Emacs` returns the latter regardless of source evidence. This proves replacement capability and no truth check inside that merge operation, not that a model actually proposed that change. A fresh disk-read failure can also leave source_content as fallback; freshness is not universally guaranteed.

#### EPI-RTE-memory-withdrawal
Label: Guarded memory withdrawal
Part of: [RT-RTE-session-commit](runtime.md#rt-rte-session-commit)

Endpoints/progression/owner: updater delete list → replacement/link migration checks and same-batch upsert protection → _apply_delete → VikingFS.rm. Different identity from [EPI-RTE-memory-write](#epi-rte-memory-write): deletes remove retained candidates rather than admit revised fields. SRC-1, `openviking/session/memory/memory_updater.py`.

- Immediate return: deleted URI or per-URI error/skip in MemoryUpdateResult.
- Later read-back: future store reads should no longer find successfully removed files; complete index cleanup and caller caches are uninspected.
- Delegated visibility: consumers see deletion results, not a required explanation that the old claim was false.
- Selection predicate: model-proposed resolved deletes, no unresolved upsert hazard, valid replacement/migrated links, no same-batch written URI conflict.
- Invalidation or expiry: successful rm removes the file; missing files are treated idempotently. Already-delivered text is not retracted by this function.
- Activation or effect: blocks unsafe deletes under inspected dependency checks and otherwise calls filesystem removal.
- Evidence limits: physical removal wiring is established; epistemic rejection, index convergence and actual runtime withdrawal are not.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model proposes disposal, software can veto dependent deletes; no per-item human veto or answer oracle is established. Trigger is an extraction/consolidation update, not necessarily a falsifying test. Replacement guidance and link inheritance can retain history while removing a file; rollback after partial writes is unresolved.

> if has_unresolved_upserts:
>     delete_error = ValueError(
>         "Skipped delete because batch contains unresolved upsert URIs"
>     )
> --- `openviking/session/memory/memory_updater.py`

> await viking_fs.rm(uri, recursive=False, ctx=ctx, lease_ref=lease_ref)
> --- `openviking/session/memory/memory_updater.py`

The updater also skips same-batch written URI deletes and suppresses replacement-source deletion if the replacement write failed. Those countercases rule out describing withdrawal as unconditional model authority.

#### EPI-RTE-memory-consolidation
Label: In-place memory consolidation

No supplied counterpart after comparison: [RT-RTE-session-commit](runtime.md#rt-rte-session-commit) starts from session traces, whereas this route starts from existing selected memory directories through compile. It shares ExtractLoop and MemoryUpdater, not the archive protocol. Endpoints/progression/owner: compile memory runner → account schema resolution and target type discovery → ConsolidationExtractContextProvider → ls/search/read model loop → operation lease → MemoryUpdater → add/update/delete/error counts. SRC-1, `openviking/service/memory_compile.py`; `openviking/session/memory/consolidation_context_provider.py`.

- Immediate return: touched URI lists and counts, selected memory types and errors; empty result when nothing selected/proposed.
- Later read-back: changed files feed subsequent recall and consolidation through the same store.
- Delegated visibility: initial recursive inventory gives paths/sizes; model reads selected content rather than receiving the whole store at once.
- Selection predicate: caller target/type/peer/instruction, enabled registry schemas, model's exploration and final operations, shared updater guards.
- Invalidation or expiry: shared update/delete paths replace retained content; no new truth-expiry rule.
- Activation or effect: model proposals are applied under an operation lease; semantic preservation and actual operation unobserved.
- Evidence limits: read-before-write and schema isolation are not proof every atomic fact was preserved; complete CLI dispatch, lease guarantees and general compile execution are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller initiates the operation and may supply instructions; model proposes merges/splits/edits/deletes, software admits through shared guards. No per-item human approval or expected-answer oracle is established. The declared objective is cleanup without invention, not new discovery; physical retention is not epistemic acceptance. Recovery reports per-operation errors; full rollback is unestablished.

> - Deduplicate repeated or paraphrased facts, preserving every distinct atomic fact.
> - Normalize fields to each memory's own schema; do not invent new facts.
> --- `openviking/session/memory/consolidation_context_provider.py`

> apply_result = await updater.apply_operations(
>     operations,
>     ctx,
>     extract_context=extract_context,
>     isolation_handler=isolation_handler,
> )
> --- `openviking/service/memory_compile.py`

#### EPI-RTE-rollout-feedback
Label: Rollout evaluation and feedback consumption

No supplied counterpart after comparison: [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) contains downstream skill admission but leaves evaluation unresolved; this record establishes the upstream evaluator dispatch, fallback target and feedback consumer, not that admission route. Endpoints/progression/owner: TrajectoryRolloutAnalyzer.analyze → supplied rollout.evaluation or optional evaluator → optional feedback message → trajectory/skill extraction → read trajectories → evaluation fallback if needed → RolloutAnalysis; gradient estimation can consume its fields. SRC-1, `openviking/session/train/components/trajectory_analyzer.py`; `openviking/session/train/components/gradient_estimator.py`.

- Immediate return: RolloutAnalysis evaluation, trajectories, gradients and metadata.
- Later read-back: extracted trajectories are read into the analysis; trajectory content can persist, but durable evaluation-report read-back is uninspected.
- Delegated visibility: when enabled and available before extraction, evaluation feedback is appended as a user-role message with criteria/evidence strings. Fallback is later, after extraction.
- Selection predicate: prefer rollout-supplied evaluation, else configured evaluator, else derive passed from bool(trajectories); feedback injection is conditional.
- Invalidation or expiry: current analysis; later evaluation can differ by supplied evaluator/configuration, with no common truth-retraction policy established.
- Activation or effect: available evaluation can shape extraction context; passed and trajectory outcome alter gradient confidence arithmetic. Downstream gradient/plan consumers are wired, not observed.
- Evidence limits: supplied/evaluator result criteria, oracle and authenticity are uninspected. The fallback measures extraction existence, not successful rollout, memory truth or future transfer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Model extraction proposes trajectory content; optional evaluator or caller supplies evaluation, and code selects/falls back. Human versus computational origin of supplied evaluation is unresolved. Operating modes include trace-fed analysis and pipeline training/evaluation; this analyzer alone does not define a controlled experiment. Evaluator target must be read from the configured evaluator; no universal task-success oracle follows.

> if rollout.evaluation is not None:
>     return rollout.evaluation
> if self.evaluator is None:
>     return None
> return await self.evaluator.evaluate(rollout, context.evaluator_context)
> --- `openviking/session/train/components/trajectory_analyzer.py`

> passed = bool(trajectories)
> return RubricEvaluation(
>     passed=passed,
>     score=1.0 if passed else 0.0,
> --- `openviking/session/train/components/trajectory_analyzer.py`

> if analysis.evaluation.passed:
>     confidence += 0.2
> --- `openviking/session/train/components/gradient_estimator.py`

A concrete symbolic deduction: for a list with one Trajectory object, bool(list) is true, so the fallback returns passed=true and score=1.0, irrespective of that trajectory's outcome. The confidence helper separately adds 0.2 for passed and adjusts for outcome. This is deterministic evidence consumption, not a calibrated probability of correctness. The optional evaluator branch is a counterexample to a blanket claim that all rollout evaluation merely checks existence.

#### EPI-RTE-policy-training
Label: Rollout-driven policy training

Distinct from supplied [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission): this record covers generic batch engine/pipeline successor flow, while that record covers conditional session-skill admission and its updater. Their optimizer/updater roles overlap without establishing identical concrete policies. Endpoints/progression/owner: BatchPolicyTrainer → analyze → estimate gradients → policy-set lock/reload → optimizer.plan → updater.apply → updated_policy_set; pipeline supplies that set to subsequent training batches and optional evaluation passes. SRC-1, `openviking/session/train/components/policy_trainer.py`; `openviking/session/train/engine.py`; `openviking/session/train/pipeline.py`.

- Immediate return: analyses, gradients, plan, apply result and score metadata.
- Later read-back: policy set reload obtains current retained policy; successor set reaches the next training batch/rollout. Persisted formats and all executor consumption paths remain uninspected here.
- Delegated visibility: analyzer receives rollouts; estimator receives analyses/policy; optimizer receives gradients and latest policy; updater receives plan; later consumers need not receive the whole criticism or originating trace.
- Selection predicate: configured components determine proposals/admission; generic engine always calls plan/apply under lock, not a score-threshold accept gate. Batch sequencing uses the returned updated set.
- Invalidation or expiry: replacement governed by configured updater; generic engine establishes no universal rollback or retention lifetime.
- Activation or effect: score-bearing feedback and policy update are source-wired; later rollout construction receives successor policy. No exercised changed behavior or benefit observed.
- Evidence limits: no causal comparison or exact candidate theory; all concrete updater/evaluator/remote/streaming variants and executable skill effects are not established by generic interfaces.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Triggers include externally produced rollouts and offline case-driven epochs. Computation proposes gradient/patch plans and software applies them; configured components can reject, but this interface supplies no universal per-content human veto. Guidance includes rollout analyses, schemas and existing policy. Policy content and metadata can persist; numerical weight updates are not shown. Oracle use is evaluator/executor-dependent, not supplied by generic score averaging. The inspected evaluation-only pass requires rollout.evaluation, collects reports, and does not invoke training; optional epoch evaluation likewise reports rather than imposing an accept/rollback threshold.

> latest_policy_set = await policy_set.reload()
> plan = await self.policy_optimizer.plan(
>     gradients,
>     latest_policy_set,
>     ctx.optimization_context,
> )
> --- `openviking/session/train/engine.py`

> current_policy_set = last_apply_result.updated_policy_set
> --- `openviking/session/train/pipeline.py`

Theory account: policies can be addressable text units, but this evidence does not supply an actual whole explanatory theory or criticism naming a challenged proposition, result and blame. The source-native experience schema asks for instructions; not every instruction unit is a theory. Guidance application is wired; derivation of theory, content-directed criticism/replacement and retained rationale are unresolved.

theory-builder conditions 1–4: condition 1 conclusion status: uninspected — no actual whole theory candidate supplied. Condition 2 conclusion status: uninspected — successor-policy flow is not evidence of decisions depending on what a particular theory says. Condition 3 conclusion status: uninspected — evaluation feedback and gradient machinery do not individuate criticism/blame of a formulated theory. Condition 4 conclusion status: uninspected — successor iteration is wired, but a criticism-dependent next theory round is not established. Addressability: schema fields/files are revisable; actual explanatory parts unresolved. Persistence: policy reload and successor-set flow are wired across batches; full later-use horizon unobserved. learning: uninspected — no demonstrated or attributed improved future capacity. Reflection: uninspected — no complete self-representation and both causal directions established. Reflective theory builder: uninspected — method-text criticism against own operation unestablished. Autonomous theory builder: uninspected — role-complete computational theory operation unestablished. No exercised self-improvement attribution: within the shipped training boundary, outcome-improvement objective is declared but actual update-dependent subsequent behavior and objective-responsive causal links lack run evidence.

### Claims

#### EPI-CLM-agent-knowledge
Label: Inspectable agent knowledge

Claimed operation/source: OpenViking organizes an agent's knowledge, memory and skills as an inspectable/editable virtual filesystem. SRC-1, `README.md`, doctrine/design. No supplied claim counterpart: [RT-CLM-scoped-retrieval](runtime.md#rt-clm-scoped-retrieval) concerns query scope, not epistemic warrant or inspectability.

> Agents navigate it like files — `ls`, `tree`, `read`, `write`, `grep` — and you can open any directory to inspect and edit what your agent knows.
> --- `README.md`

The operational reading is supported by storage/recall routes; the wording does not supply a factual verification contract.

#### EPI-CLM-reusable-experience
Label: Generalizable reusable experience

Claimed operation/source: experiences are transferable insights explaining when and how an approach works. SRC-1, `openviking/prompts/templates/memory/experiences.yaml`, doctrine/design. No supplied claim counterpart; [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) is related machinery rather than this claim.

> A generalizable, reusable insight distilled from agent execution — not a process record.
> Captures a transferable pattern: what situation triggers it, what approach works, and why.
> --- `openviking/prompts/templates/memory/experiences.yaml`

Transferability and explanation are requested output qualities. The implementation establishes candidate/policy production, not a tested mechanism or warranted universal rule.

#### EPI-CLM-memory-benefit
Label: Reported experience-memory benefit

Claimed operation/source: improved task success with experience memory versus the same LLM without memory. SRC-1, `README.md`, reported operation; no inspectable run evidence registered. No supplied claim counterpart; the boundary already limits the benchmark evidence, and [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission) does not establish benefit.

> - **Agent experience (tau2-bench)**: experience memory lifts task success by +6.87pp (retail) and +11.87pp (airline) over the same LLM without memory.
> --- `README.md`

This attributed package-level contrast is not an independently checked causal experiment and cannot identify a particular extraction/checking component or establish why a proposed experience transfers.
