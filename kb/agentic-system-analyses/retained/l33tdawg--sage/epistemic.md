---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SAGE epistemic routes: candidate retention, optional lasting/support judgments, reliance, correction and bounded benchmark warrant."
run-id: AAS-2026-10-15-sage-d3843de6d2dd-01
reviewed-boundary: e2e0242a421afbd356ed135d7d754a35b0ad5f14
---

# SAGE epistemic report

## Source-and-claim boundary

The question is what SAGE's memory and evaluation machinery licenses a later consumer to believe or do. The frozen whole-system scope, exclusions and external dependencies are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is its [Source register](boundary.md#source-register). This member inspects selected material routes within that scope, not every included operation. All new passages are SRC-1 implementation unless explicitly labelled doctrine/design or reported operation. No target execution or newly generated model output enters this account.

Public claims assessed are [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn), [EPI-CLM-gate-purpose](#epi-clm-gate-purpose), [EPI-CLM-reflect-fact](#epi-clm-reflect-fact) and [EPI-CLM-feedback-learning](#epi-clm-feedback-learning). A material counterexample to a blanket absence of evidence-based acceptance is the optional support judge. Counterexamples to universal semantic acceptance are ordinary gate-off admission, gate exemptions, operator resolution and co-commit. Neither counterexample erases the other.

| Entry point or operation | Source path, SRC-1 | Coverage and records, or limit |
| --- | --- | --- |
| CLI dispatch, server and MCP | `cmd/sage-gui/main.go`; `internal/mcp/tools.go` | Direct dispatch/tool inventory search; supplied [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle), [RT-RTE-machinery-change](runtime.md#rt-rte-machinery-change). Dispatch exposes hooks, import/export, seed, restore and recovery beyond foreground turn. |
| Ordinary submit, baseline, optional judging, vote and persistence | `internal/voter/decision.go`; `internal/voter/gate.go`; `internal/store/sqlite_gate.go`; `api/rest/memory_handler.go`; `internal/abci/app.go` | Direct baseline/gate/evidence reads; supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission); parts below separate check, disposition and retention. |
| Co-commit | `internal/abci/app.go` | Supplied [RT-RTE-co-commit](runtime.md#rt-rte-co-commit); semantic-gate bypass is material to warrant. |
| Recall, browser and unsolicited hooks | `internal/mcp/tools.go`; `extension/chrome/background.js`; `cmd/sage-gui/hook.go`; `cmd/sage-gui/hook_precompact.go`; `cmd/sage-gui/nevercompact_recall.go` | Supplied [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context); no independent exhaustive host audit. |
| Reflection and correction | `internal/mcp/tools.go` | Direct registered descriptions and handlers: [EPI-RTE-reflect-format](#epi-rte-reflect-format), [EPI-RTE-correction-check](#epi-rte-correction-check), [EPI-RTE-correction-replace](#epi-rte-correction-replace). These materially extend runtime coverage. |
| Corroborate, challenge, reinstate | `internal/abci/app.go`; `internal/mcp/tools.go` | Direct corroboration implementation, selected challenge/reinstate paths and wrappers: [EPI-RTE-corroborate-signal](#epi-rte-corroborate-signal), [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition). Not every historical replay branch assessed. |
| Typed links | `internal/mcp/tools.go` | Direct toolLink/toolGetLinks read; server admission and downstream graph consumers uninspected. A `supports` label is caller-authored, not an inspected proof. No conclusion of accepted-claim integration across this surface. |
| Cleanup and boot policy | `web/cleanup.go`; `web/handler.go`; `internal/mcp/tools.go` | Supplied [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup), [RT-RTE-boot-guidance](runtime.md#rt-rte-boot-guidance). Operational authority, not demonstrated factual correction or improved method. |
| Level Up distillation | `integrations/levelup/sage_bridge.py` | Supplied [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation); generated proposition/entailment cannot be determined without outputs and full inputs. |
| Answer evaluation | `bench/longmemeval/run_with_llm.py` | Direct score, generate_answer, llm_judge, run_question and model configuration: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check). Other benchmark families and retained result artifacts unassessed. |
| Research benefit claim | `papers/README.md`; `internal/mcp/tools.go` | Direct source-native disclosure and claim read: [EPI-CLM-feedback-learning](#epi-clm-feedback-learning). PDFs and underlying experiment not inspected; README says pipeline and run records are excluded. |
| Import/export/seed, restore, federation copy/adoption/withdrawal, local exchange journaling, SDK variants, judge qualification and other evaluators | `cmd/sage-gui/main.go`; `web/import.go`; `internal/federation/`; `sdk/python/`; `bench/judge-qualify/`; `bench/locomo/run.py` | Available included operations, not fully assessed here. Boundary supplies initial LoCoMo/SDK inspection only. Prevents a system-complete negative about acceptance, integration, provenance preservation or evaluator quality; federation revocation force is not inferred from local lifecycle. |

Missing evidence is local to conclusions: no live deployment config or votes means gate activation and actual quorum are unobserved; no provenance-linked candidate/output traces means actual conjecture, acceptance and later changed reliance are unobserved; absent provider weights/complete host implementation prevents model-internal learning and host-compliance conclusions. Uninspected included files above are not access gaps. The research disclosure prevents independent reconstruction of the particular longitudinal study; it does not negate its attributed report.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | Caller assertions, observations, instructions or transcript statements; scope depends on their text | see record | SRC-1 `internal/mcp/tools.go` | No actual candidate instance supplied; not every stored string is truth-apt. |
| [EPI-OBJ-memory-evidence](#epi-obj-memory-evidence) | Uploaded support text, possibly itself an assertion | see record | SRC-1 `internal/store/sqlite_gate.go` | Source authenticity and source truth unknown; local retention is temporary. |
| [EPI-OBJ-semantic-verdict](#epi-obj-semantic-verdict) | Model-estimated lasting/support probabilities and symbolic pass/reject/abstain | see record | SRC-1 `internal/voter/gate.go` | Lastingness and support are separate targets; scores are not calibrated truth certificates. |
| [RT-OBJ-boot-instructions](runtime.md#rt-obj-boot-instructions) | Primarily operating policy, not necessarily truth-apt | see record | SRC-1 `web/handler.go` | Delivery establishes no improved policy or compliance. |
| [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), [RT-CMP-http-reranker](runtime.md#rt-cmp-http-reranker) | Dense relevance representations/scores, no individuated world claim from weights | see records | SRC-1 `internal/embedding/provider.go`; `internal/embedding/reranker.go` | Relevance is not truth assessment; opaque parameters remain bounded as in records. |
| [RT-CMP-hunch-judge](runtime.md#rt-cmp-hunch-judge) | Distributed-parametric machinery estimating lasting/support classifications | see record | SRC-1 `internal/hunch/local.go` | Exact identity/pinning is path-dependent; inference requests are not training. |
| [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model) | Opaque model plus generated advice candidates | see record | SRC-1 `integrations/levelup/sage_bridge.py` | Weights do not expose individuated theories; actual generated content not determinable. |
| [EPI-OBJ-benchmark-answer](#epi-obj-benchmark-answer) | Generated answer, dataset gold answer and support-session IDs | see record | SRC-1 `bench/longmemeval/run_with_llm.py` | Dataset warrant and model accuracy not independently established. |

## Authority-route ledger

Each route citation owns its generic fields: `see` the record rather than treating this overlay as another declaration. Architectural status below is implementation assessment, not evidence of operation. For compactness, common field names retain the ledger contract's meaning.

Route ID: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: truth-apt transformation: acquisition/import; caller assertions enter, source warrant unknown.
Transition or check target: see record; ordinary proposal intake, not epistemic acceptance.
Evaluator/condition and domain: see record.
Activation and timing: see record; before voting.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: authorship/identity attribution, not verified truth.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context); later eligibility depends on lifecycle.
Evidence source ID and local anchor: SRC-1 `api/rest/memory_handler.go`; see record.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: proposal or transaction commitment is not memory acceptance.
Gap/limit: no actual submission trace.

Route ID: [EPI-RTE-baseline-check](#epi-rte-baseline-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: no content change.
Transition or check target: see record; uniqueness, size/noise and confidence/domain consistency, not proposition truth.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: advisory prevalidation or input to local vote; downstream disposition is separate.
Epistemic authority and scope: licenses only these operational checks.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `internal/voter/decision.go`.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: confidence consistency is not fact checking.
Gap/limit: lookup failure passes dedup; factual contradiction comparison is not implemented by these named checks.

Route ID: [EPI-RTE-lasting-check](#epi-rte-lasting-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content), [EPI-OBJ-semantic-verdict](#epi-obj-semantic-verdict).
Content/update relation: no content change.
Transition or check target: lasting knowledge versus remark about originating conversation.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: local cached result; disposition below.
Epistemic authority and scope: durability-of-subject judgment, not independent truth evidence.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `internal/voter/gate.go`.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: lasting fact-like wording does not establish a fact.
Gap/limit: optional configured route; accuracy unestablished here.

Route ID: [EPI-RTE-support-check](#epi-rte-support-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-evidence](#epi-obj-memory-evidence), [EPI-OBJ-semantic-verdict](#epi-obj-semantic-verdict).
Content/update relation: no content change.
Transition or check target: submitted evidence supports assertion as stated, including time and certainty.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: local stored verdict; see separate disposition.
Epistemic authority and scope: conditional support assessment relative to supplied text, not authentication of that text or external truth.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `internal/voter/gate.go`.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: evidence-free route does not perform this check.
Gap/limit: no actual claim/evidence pair or calibration run inspected.

Route ID: [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content), [EPI-OBJ-semantic-verdict](#epi-obj-semantic-verdict).
Content/update relation: no content change.
Transition or check target: see record; local voting admissibility, with evidence-consuming support criterion when enabled and supplied.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: enforcing over this node's vote, not all alternate admissions.
Epistemic authority and scope: conditional acceptance as supported lasting memory for later recall; evidence-consuming only on support path; operator criterion otherwise unresolved.
Operational authority: behavior permitted, blocked, or changed: see record; consensus remains later owner.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission).
Evidence source ID and local anchor: SRC-1 `internal/voter/gate.go`.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: per-node opinion is not a universal truth certificate.
Gap/limit: no observed accepted candidate or global deployment state.

Route ID: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: no content change.
Transition or check target: see record; canonical lifecycle and serving projection persistence.
Evaluator/condition and domain: see record; vote/quorum rule is protocol disposition, not a semantic oracle.
Activation and timing: see record; proposals are retained before semantic acceptance.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: records lifecycle disposition, not independently warranted source propositions.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
Evidence source ID and local anchor: SRC-1 `internal/abci/app.go`.
Claim IDs or none: [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn).
Mismatch marker or none: retention is not lifecycle integration after epistemic acceptance.
Gap/limit: no observed run; not every projection crash state assessed.

Route ID: [EPI-RTE-evidence-retention](#epi-rte-evidence-retention)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-evidence](#epi-obj-memory-evidence).
Content/update relation: no content change.
Transition or check target: see record; attachment lineage and temporary evidence availability, not evidence truth.
Evaluator/condition and domain: see record; uploader/claim/freshness and memory-state predicates.
Activation and timing: see record; upload/claim then periodic pruning while gate worker runs.
Possible or observed result: see record.
Implemented force: evidence ownership binding; deletion or expiry marker can prevent later source replay.
Epistemic authority and scope: preserves local attachment while available; does not warrant submitted source; deletion loses replayable support without retracting every retained verdict.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record; later support check holds on explicit expiry, whereas terminal memory can outlive source text.
Evidence source ID and local anchor: SRC-1 `internal/store/sqlite_gate.go`; `internal/voter/gate.go`.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: retained decision is not permanently retained evidence.
Gap/limit: deployment pruning schedule and actual deletions unobserved.

Route ID: [RT-RTE-boot-guidance](runtime.md#rt-rte-boot-guidance)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-boot-instructions](runtime.md#rt-obj-boot-instructions).
Content/update relation: non-truth-apt policy/content update: operator-authored instructions replace a preference and are appended to later inception guidance.
Transition or check target: see record; operator authorization and valid body/persistence, not semantic improvement.
Evaluator/condition and domain: see record.
Activation and timing: see record; later inception reads saved text.
Possible or observed result: see record.
Implemented force: delivery of requested operating policy; external model compliance not enforced.
Epistemic authority and scope: no factual or improvement license follows from operator authority alone.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-client-guidance](runtime.md#rt-bap-client-guidance).
Evidence source ID and local anchor: SRC-1 `web/handler.go`; `internal/mcp/tools.go`.
Claim IDs or none: none.
Mismatch marker or none: persistence/delivery is not demonstrated behavior adaptation.
Gap/limit: no live model session or semantic quality check established.

Route ID: [RT-RTE-co-commit](runtime.md#rt-rte-co-commit)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: truth-apt transformation: acquisition/import; signed envelope has content hash, not raw proposition for the voter.
Transition or check target: see record.
Evaluator/condition and domain: see record; coauthor ratification and protocol validity.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: attributable coauthor agreement, not inspected evidence-consuming content acceptance.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
Evidence source ID and local anchor: SRC-1 `internal/abci/app.go`.
Claim IDs or none: [EPI-CLM-gate-purpose](#epi-clm-gate-purpose).
Mismatch marker or none: counterexample to universal judging of committed content.
Gap/limit: actual coauthor evidence and later consumption unobserved.

Route ID: [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: truth-apt transformation: non-ampliative reshaping; selects content and metadata, with path-dependent qualification loss.
Transition or check target: see record; relevance and authorized eligibility, not proposition truth.
Evaluator/condition and domain: see record; embedding/lexical relevance and optional reranking, lifecycle and scope predicates.
Activation and timing: see record; caller request.
Possible or observed result: see record.
Implemented force: ranking and requested context supply, not guaranteed model compliance.
Epistemic authority and scope: retrieved attributed experience, including disputed-but-live content.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
Evidence source ID and local anchor: SRC-1 `internal/mcp/tools.go`; `extension/chrome/background.js`.
Claim IDs or none: [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn).
Mismatch marker or none: browser omission of dispute flags degrades delivered qualification relative to MCP.
Gap/limit: downstream interpretation unobserved; retrieval is not completeness or endorsement.

Route ID: [RT-RTE-hook-context](runtime.md#rt-rte-hook-context)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: truth-apt transformation: non-ampliative reshaping; recent-memory excerpts or thread reconstruction, rather than a new claim.
Transition or check target: see record; eligibility by recency/scope or captured thread identity and sequence.
Evaluator/condition and domain: see record; deterministic selector/reconstructor, not a truth evaluator.
Activation and timing: see record; host SessionStart/resume, independent of foreground recall request.
Possible or observed result: see record.
Implemented force: unsolicited host-context supply; host owns injection/window and later interpretation.
Epistemic authority and scope: retained attributed content, bounded by captured eligible units or truncated prefetch.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
Evidence source ID and local anchor: SRC-1 `cmd/sage-gui/hook.go`; `cmd/sage-gui/nevercompact_recall.go`.
Claim IDs or none: none.
Mismatch marker or none: output reconstruction is not complete model visibility or renewed endorsement.
Gap/limit: exact host injection and semantic effects of lost excerpt qualifications unobserved.

Route ID: [EPI-RTE-reflect-format](#epi-rte-reflect-format)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: truth-apt transformation: non-ampliative reshaping; incoming caller text is prefixed and split, not a new explanation.
Transition or check target: see record.
Evaluator/condition and domain: see record; deterministic formatter, not factual evaluator.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: proposes typed memories with assigned confidence.
Epistemic authority and scope: fact typing is operational promotion, not evidence that dos were proven.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
Evidence source ID and local anchor: SRC-1 `internal/mcp/tools.go`.
Claim IDs or none: [EPI-CLM-reflect-fact](#epi-clm-reflect-fact), [EPI-CLM-feedback-learning](#epi-clm-feedback-learning).
Mismatch marker or none: input label/score cannot supply missing outcome evidence.
Gap/limit: actual propositions and criticism not supplied; no ampliative novelty inferred from route name.

Route ID: [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content), [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model).
Content/update relation: truth-apt transformation: indeterminate; possible faithful compression, entailed advice or ampliative conjecture. Full input/output pairs are needed to decide.
Transition or check target: see record.
Evaluator/condition and domain: see record; model requests new outcome-grounded advice but no observed semantic result.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: candidate proposal, ordinary downstream admission.
Epistemic authority and scope: model-produced candidate only; supplied outcome truth is unverified.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context).
Evidence source ID and local anchor: SRC-1 `integrations/levelup/sage_bridge.py`.
Claim IDs or none: [EPI-CLM-feedback-learning](#epi-clm-feedback-learning).
Mismatch marker or none: request for insight/criticism is not produced insight/criticism.
Gap/limit: no claim of accepted ampliative production from this evidence.

Route ID: [EPI-RTE-correction-check](#epi-rte-correction-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: no content change.
Transition or check target: replacement visible as committed before old record challenge.
Evaluator/condition and domain: see record; signed read-back/status predicate, not truth comparison.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: permits or prevents next destructive step.
Epistemic authority and scope: replacement availability only.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `internal/mcp/tools.go`.
Claim IDs or none: none.
Mismatch marker or none: committed replacement does not establish a correct replacement.
Gap/limit: no observed correction.

Route ID: [EPI-RTE-correction-replace](#epi-rte-correction-replace)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: truth-apt transformation: acquisition/import; caller supplies replacement and reason, source warrant unknown.
Transition or check target: old memory reliance, after replacement check.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: challenge request under lifecycle authority.
Epistemic authority and scope: records proposed correction lineage; no independent comparison of old/new truth.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `internal/mcp/tools.go`.
Claim IDs or none: none.
Mismatch marker or none: lifecycle correction is not necessarily epistemic acceptance/integration.
Gap/limit: interruption may leave both live.

Route ID: [EPI-RTE-corroborate-signal](#epi-rte-corroborate-signal)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: no content change.
Transition or check target: identity-qualified corroboration for an existing memory, not evidence entailment.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: countable corroboration; later challenge electorate can depend on it.
Epistemic authority and scope: distinct principal endorsement, not independent investigation or source reliability.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `internal/abci/app.go`.
Claim IDs or none: none.
Mismatch marker or none: signature distinctness is not epistemic independence.
Gap/limit: no later numerical confidence effect claimed without consumer inspection.

Route ID: [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: no content change.
Transition or check target: memory lifecycle/reliance.
Evaluator/condition and domain: see record; authority and versioned electorate/status rules, not semantic adjudication of reasons.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: canonical challenged/deprecated/recommitted state, with later read filtering/qualification.
Epistemic authority and scope: recorded withdrawal or reinstatement of operational reliance, not programmatic resolution of reason/evidence truth.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record and [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall).
Evidence source ID and local anchor: SRC-1 `internal/abci/app.go`.
Claim IDs or none: none.
Mismatch marker or none: challenge need not remove a record from all recall immediately.
Gap/limit: remote copies, every replay branch and live outcomes unassessed.

Route ID: [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-content](#epi-obj-memory-content).
Content/update relation: no content change.
Transition or check target: see record; eligibility for operator-authorized cleanup, not factual falsehood.
Evaluator/condition and domain: see record; code checks current policy, current memory eligibility and signing authority.
Activation and timing: see record; authorized run and background continuation.
Possible or observed result: see record.
Implemented force: permits/blocks next signed challenge and reconciles pending intent; lifecycle disposition is separate.
Epistemic authority and scope: policy-based retirement intent only.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record; worker to consensus through signed challenge until completion/cancellation.
Evidence source ID and local anchor: SRC-1 `web/cleanup.go`.
Claim IDs or none: none.
Mismatch marker or none: stale/low-value classification is not evidence of falsity.
Gap/limit: no observed cleanup run or resulting benefit.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-benchmark-answer](#epi-obj-benchmark-answer).
Content/update relation: no content change.
Transition or check target: retrieved support-session identity and generated answer against gold in LongMemEval.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: reporting/aggregation only on inspected path, not memory admission.
Epistemic authority and scope: benchmark agreement under supplied dataset and judge, not universal truth or causal component attribution.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: SRC-1 `bench/longmemeval/run_with_llm.py`.
Claim IDs or none: [EPI-CLM-feedback-learning](#epi-clm-feedback-learning).
Mismatch marker or none: different benchmark cannot verify the longitudinal claim.
Gap/limit: retained results, judge qualification and dataset authenticity not assessed here.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn) | see record | SRC-1 `sage-memory/SKILL.md`, doctrine/design | see record | [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle), [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall) | none inspected | none inspected | combined sequential API, governed recall | independent phase failure and disputed eligibility defeat literal broad wording |
| [EPI-CLM-gate-purpose](#epi-clm-gate-purpose) | see record | SRC-1 `internal/voter/gate.go`, doctrine/design plus implementation | see record | [EPI-RTE-lasting-check](#epi-rte-lasting-check), [EPI-RTE-support-check](#epi-rte-support-check), [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition) | none inspected | no calibration or intervention assessed; source comments about held-out tests are reported rationale | optional evidence-relative semantic narrowing of local votes | no universal truth certification; co-commit and exemptions differ |
| [EPI-CLM-reflect-fact](#epi-clm-reflect-fact) | see record | SRC-1 `internal/mcp/tools.go`, doctrine/design comment | see record | [EPI-RTE-reflect-format](#epi-rte-reflect-format), ordinary admission | none inspected | no independent task outcome check in formatter | dos become fact-typed proposals at 0.90 | 'proven to work' is not established by caller field or score |
| [EPI-CLM-feedback-learning](#epi-clm-feedback-learning) | see record | SRC-1 `internal/mcp/tools.go`, doctrine/design; `papers/README.md`, reported operation | attributed study and prompt request | [EPI-RTE-reflect-format](#epi-rte-reflect-format), [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation), [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) | no provenance-linked study runs inspected | underlying pipeline/run records excluded per source disclosure; benchmark harness is a different task; no independent variation of consensus identified here | retention and later delivery afford feedback, with reported study results | no measured improvement or component-specific causal conclusion established by this analysis |

## Bounded conclusion

SAGE imports and retains caller content, including experience and consent-gated transcript material, and supplies it to later model invocations through requested recall and unsolicited hooks. Identity, lifecycle state and selector metadata can be preserved; source truth remains unknown. Qualification is path-dependent: disputed content remains eligible on targeted recall, MCP warns, and browser turn omits dispute metadata. These conclusions use [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context), not an inference from storage alone.

The baseline checks operational suitability, not truth. Optional lasting judgment asks a different question from optional evidence support. On the latter path, the implementation does consume evidence against a named criterion—support for the assertion as stated—for intended use as retained, later-recalled memory. It records pass/reject/hold and gates this node's vote. This is a real implemented acceptance route, bounded by supplied evidence, configured scope, operator overrides and later quorum. It does not authenticate premises, prove the assertion, establish actual accepted ampliative production or cover co-commit. See [EPI-RTE-baseline-check](#epi-rte-baseline-check), [EPI-RTE-support-check](#epi-rte-support-check), [EPI-RTE-semantic-disposition](#epi-rte-semantic-disposition), and [RT-RTE-co-commit](runtime.md#rt-rte-co-commit).

Deterministic reflection formatting produces no new explanatory proposition in the traced example; it changes packaging, type and declared confidence. Bridge distillation requests new advice, but without input/output pairs its semantic relation is indeterminate. No warranted-premise entailed derivation or accepted ampliative instance is established here. The optional support route defeats a stronger assertion that SAGE has no evidence-consuming acceptance capacity. See [EPI-RTE-reflect-format](#epi-rte-reflect-format), [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation).

Correction, corroboration, challenge, cleanup and reinstatement have consequential operational consumers. They can change future eligibility or disputed status without proving a claim true or false. Correction's availability check protects the replacement sequence, not its factual content. Candidate retention before acceptance, typed links without an inspected acceptance lineage, and lifecycle flags are not sufficient evidence of post-acceptance lifecycle integration. Such integration is not established on the assessed paths; unassessed graph/federation/import consumers prevent a system-complete absence. See [EPI-RTE-correction-check](#epi-rte-correction-check), [EPI-RTE-correction-replace](#epi-rte-correction-replace), [EPI-RTE-corroborate-signal](#epi-rte-corroborate-signal), [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).

Operator boot preferences directly change delivered operating guidance, without requiring a truth-apt update; model compliance is separate. Model weights and endpoint fixity remain as bounded in the runtime component records. No inference of training follows from retained-memory writes, and fixed weights would not exclude learning through retained advice. For the bridge, theory-builder conditions 1–4, learning, reflection and autonomy remain independently limited as in [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation). Source-reported learning is not dismissed, but this inspection does not independently establish improved capacity or exercised self-improvement: subsequent behavior causally depending on the retained update is not supplied. Benchmark answer agreement is a separate, implemented evaluation path, not a semantic gate over all product memory or a causal test of its components. See [RT-RTE-boot-guidance](runtime.md#rt-rte-boot-guidance), [EPI-CLM-feedback-learning](#epi-clm-feedback-learning), [EPI-RTE-benchmark-check](#epi-rte-benchmark-check).

## Shared records

### Operative objects

#### EPI-OBJ-memory-content
Label: Memory content

Source-native identity: memory `content`, `memory_type`, lineage `parent_hash` and lifecycle metadata. Natural-language assertions/policies are consumed by models; symbolic type/status/parent fields are consumed by code. Storage substrate: canonical hash/metadata in Badger and serving records in SQL, per [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). This is the operative content object crossing several supplied routes, not another name for any one route. No supplied object counterpart after comparison; [RT-OBJ-boot-instructions](runtime.md#rt-obj-boot-instructions) is a different preference and admission mechanism. SRC-1 `internal/mcp/tools.go`, implementation:

> submitBody := map[string]any{
> 		"content":          content,
> 		"memory_type":      memType,
> 		"domain_tag":       domain,
> 		"provider":         s.provider,
> 		"confidence_score": confidence,
> 		"embedding":        embedResp.Embedding,
> 	}
> --- `internal/mcp/tools.go`

#### EPI-OBJ-memory-evidence
Label: Memory evidence

Source-native identity: `memory_evidence` row and `evidence_id`; natural-language supporting text plus symbolic claim/agent/timestamp fields. Storage substrate: local SQLite with strict plaintext/decryption read; no replicated durable proof is inferred. Distinct from the assertion and the model verdict; closest supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) mentions evidence but declares no evidence object. SRC-1 `internal/store/sqlite_gate.go`, implementation. Claiming checks matching uploader, unclaimed state and freshness; pruning deletes evidence attached to non-proposed existing memories, while orphan expiry retains an expired marker. Therefore a retained verdict need not carry indefinitely replayable source evidence.

> `UPDATE memory_evidence SET memory_id = ?, claimed_at = ?
> 		 WHERE evidence_id = ? AND agent_id = ? AND memory_id IS NULL AND created_at >= ?`,
> --- `internal/store/sqlite_gate.go`

> `DELETE FROM memory_evidence
> 		 WHERE (memory_id IS NULL AND created_at < ?)
> 		    OR (memory_id IS NOT NULL AND EXISTS (
> 		          SELECT 1 FROM memories AS m
> 		          WHERE m.memory_id = memory_evidence.memory_id AND m.status != ?))`,
> --- `internal/store/sqlite_gate.go`

#### EPI-OBJ-semantic-verdict
Label: Semantic verdict

Source-native identity: `memory.SemanticVerdict`, version-keyed local result. Symbolic pass/reject/abstain, numeric probability and natural-language reason; storage substrate: GateStore semantic-verdict persistence, inspected SQLite implementation path. Distinct from model weights and submitted memory; closest supplied [RT-CMP-hunch-judge](runtime.md#rt-cmp-hunch-judge) is the inference component, not this cached output. SRC-1 `internal/voter/gate.go`, implementation:

> if err := gs.RecordSemanticVerdict(ctx, memoryID, g.Version, v); err != nil {
> 		fail(err)
> 	}
> --- `internal/voter/gate.go`

#### EPI-OBJ-benchmark-answer
Label: Benchmark answer and reference

Source-native identity: `llm_answer`, `gold_answer`, `answer_session_ids` and `llm_score` per question. Natural-language answers and symbolic reference IDs/metrics; storage substrate: question dictionaries, per-question result dictionaries and benchmark output aggregation. No supplied counterpart after comparison: [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall) supplies product retrieval, not this answer/reference pair. SRC-1 `bench/longmemeval/run_with_llm.py`, implementation:

> gold_answer = str(question.get("answer", "") or "")
> --- `bench/longmemeval/run_with_llm.py`

> llm_score = llm_judge(openai, question["question"], gold_answer, llm_answer) if gold_answer else 0
> --- `bench/longmemeval/run_with_llm.py`

### Routes

#### EPI-RTE-baseline-check
Label: Baseline check

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Named checks and first-failure aggregate accept/reject with reason.
- Later read-back: inapplicable — this deterministic check recomputes against current input/store rather than accumulating guidance.
- Delegated visibility: Advisory preview to caller; actual aggregate to node voter, no model delegation.
- Selection predicate: All supplied ordinary voter inputs; dedup hash lookup, 20-byte content minimum, noise patterns, reflection minimum, confidence floors and nonempty domain.
- Invalidation or expiry: Fresh computation each vote; store lookup and input changes change result.
- Activation or effect: Advisory prevalidation or local vote input; actual quorum disposition belongs to parent.
- Evidence limits: No execution observed; a check named consistency does not compare proposition truth.

Proposer is caller, evaluator/decider is fixed Go code, no per-content human decision or answer oracle. Open admission, no experiment/improvement trigger. SRC-1 `internal/voter/decision.go`, implementation. A false sufficiently long statement with high declared confidence is not rejected for falsity by these predicates. Dedup lookup error is explicitly permissive in parent evidence.

> checks := []CheckResult{
> 		dedupCheck(ctx, dup, m),
> 		qualityCheck(m),
> 		consistencyCheck(m),
> 	}
> --- `internal/voter/decision.go`

> if m.MemType == "fact" && m.Confidence < 0.7 {
> 		return CheckResult{Name: "consistency", Pass: false, Reason: fmt.Sprintf("facts require confidence >= 0.7 (got %.2f)", m.Confidence)}
> 	}
> --- `internal/voter/decision.go`

#### EPI-RTE-evidence-retention
Label: Evidence attachment and expiry

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Evidence upload ID, claim success/unavailable error, or pruning success/error.
- Later read-back: Claimed plaintext feeds background support judging; orphan expiry marker remains to distinguish expired evidence from never submitted evidence.
- Delegated visibility: Local evidence store supplies configured support judges, not canonical replicated source text.
- Selection predicate: Claim binds same agent, unclaimed ID and upload freshness; pruning selects expired unclaimed rows, attached non-proposed memories and old orphan claims.
- Invalidation or expiry: Non-proposed existing memory causes evidence deletion; orphan claim expiry blanks text and marks expired; releasing a claim is allowed only for provably unsent submission.
- Activation or effect: Attachment determines which support text is judged; later availability affects evidence replay and can hold a pending semantic check.
- Evidence limits: No actual uploads/deletions inspected; stored source truth and permanent auditability not established.

This is a material lineage/retention part, not the parent route's semantic judgment. Evidence proposer is uploading caller; SQL predicates can veto claim; code chooses pruning without per-row human review. No expected-answer oracle; routine admission maintenance. Stored guidance is evidence text and attachment metadata; release refreshes unclaimed expiry only where submission provably did not leave the node. SRC-1 `internal/store/sqlite_gate.go`, implementation; minimum passages are retained in [EPI-OBJ-memory-evidence](#epi-obj-memory-evidence). Periodic worker wiring is SRC-1 `internal/voter/gate.go`:

> if err := p.PruneMemoryEvidence(ctx, time.Now()); err != nil && ctx.Err() == nil {
> --- `internal/voter/gate.go`

#### EPI-RTE-lasting-check
Label: Lasting check

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Probability aggregation produces lasting pass/reject/abstain, subsequently combined with support when applicable.
- Later read-back: Versioned verdict feeds later Gate.Apply; version changes can rejudge pending content.
- Delegated visibility: Configured judges receive plaintext content; inference component is [RT-CMP-hunch-judge](runtime.md#rt-cmp-hunch-judge).
- Selection predicate: Gate in-scope baseline-passing candidate; configured judge set and combination policy.
- Invalidation or expiry: Judge version namespaces pending verdicts; unavailable inference yields hold; operator review can outrank model verdict.
- Activation or effect: Background evaluator writes result without blocking voter loop; separate disposition consumes it.
- Evidence limits: Lastingness classification is not a source truth check; no run or measured accuracy inspected.

Target/domain: lasting world fact or standing rule/method versus conversational remark. Evaluator is one or more operator-configured models, default lead-with-veto or all policy, default pass 0.9/reject below 0.5. A lead of at least ActAt with no judge below RejectBelow passes in lead mode; all judges below RejectBelow rejects; middle holds. Model judgment has no supplied reference-answer oracle. Caller proposes; code aggregates; human may later resolve hold. Routine open admission, not a bounded experiment. SRC-1 `internal/voter/gate.go`, implementation:

> pass := lead >= g.ActAt && lo >= g.RejectBelow
> 	p := lead
> 	if g.Policy == PolicyAll {
> 		pass, p = lo >= g.ActAt, lo
> 	}
> --- `internal/voter/gate.go`

#### EPI-RTE-support-check
Label: Support check

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Evidence support pass/reject/abstain merged with lasting verdict; neither single pass alone suffices when both are checked.
- Later read-back: Stored merged verdict reaches later Gate.Apply; source evidence may be pruned after decision.
- Delegated visibility: Configured support judges receive assertion plus submitted plaintext evidence.
- Selection predicate: EvidenceStore available, support judges configured, actual evidence present, candidate in gate scope; evidence-free candidates skip support.
- Invalidation or expiry: Unreadable evidence holds; explicit expired marker holds rather than taking evidence-free branch; future pending judgments use version namespace.
- Activation or effect: Stored result has force only through separate local-vote disposition.
- Evidence limits: Checks support relative to submitted text; no authentication of original source or measured reliability established.

Target/domain: support for what content asserts, as stated, including time frame and certainty. Each support model must reach ActAt to pass; all below RejectBelow rejects; disagreement/intermediate result holds. Caller supplies evidence; models evaluate, code combines, human may resolve. No expected-answer oracle in runtime route; open admission, not experiment. Implementation itself is a counterexample to treating all SAGE admission as content-length checking. SRC-1 `internal/voter/gate.go`:

> if hasEvidence {
> 		v = mergeVerdicts(v, g.combineSupport(sps))
> 	}
> --- `internal/voter/gate.go`

> case lo >= g.ActAt:
> 		return memory.SemanticVerdict{Verdict: memory.VerdictPass, P: lo, Reason: fmt.Sprintf("supported by its evidence p=%.2f", lo)}
> --- `internal/voter/gate.go`

> if errors.Is(err, memory.ErrEvidenceExpired) {
> 			// Keep an explicit expired-evidence hold rather than taking the
> 			// no-evidence path: a human must decide this memory.
> --- `internal/voter/gate.go`

#### EPI-RTE-semantic-disposition
Label: Semantic disposition

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: gateUseBaseline, gateOverride accept/reject, or gateHold with no vote this tick.
- Later read-back: Operator review and versioned verdict are reread during later voter ticks; parent route persists resulting vote/lifecycle.
- Delegated visibility: One node's signed opinion reaches consensus, not a universal deterministic semantic ruling.
- Selection predicate: Fresh failed baseline or out-of-scope candidate uses baseline; otherwise review first, then verdict; missing verdict queues evaluation and holds.
- Invalidation or expiry: Terminal state ends pending voting; review persists across judge versions; baseline always fresh.
- Activation or effect: Enforcing over this node's accept/reject/abstain behavior before global/scoped quorum.
- Evidence limits: No actual decision instance or activated topology supplied; co-commit differs.

Caller proposes memory; code and optional models decide local admissibility, operator review can resolve semantics but cannot rescue baseline failure. The support branch is evidence-consuming acceptance against support-as-stated and lastingness criteria, intended for retained later memory use, within configured domain/node scope. Absent evidence, lastingness alone is narrower than warrant for truth. Review's human rationale is not available. Rollback/recovery is not automatic semantic revision: later challenge/replacement is separate. No answer oracle; routine open requests. SRC-1 `internal/voter/gate.go`, implementation; parent owns final quorum.

> if !baseline.Accept || !g.InScope(mem.DomainTag) {
> 		return gateUseBaseline, baseline
> 	}
> --- `internal/voter/gate.go`

> if decision == memory.VerdictAccept {
> 			return gateOverride, Decision{Accept: true, Reason: baseline.Reason + "; semantic check resolved by operator review"}
> 		}
> 		return gateOverride, Decision{Accept: false, Reason: "rejected by operator review"}
> --- `internal/voter/gate.go`

> case memory.VerdictPass:
> 		return gateOverride, Decision{Accept: true, Reason: baseline.Reason + "; " + v.Reason}
> 	case memory.VerdictReject:
> 		return gateOverride, Decision{Accept: false, Reason: v.Reason}
> 	default:
> 		return gateHold, Decision{}
> --- `internal/voter/gate.go`

#### EPI-RTE-reflect-format
Label: Reflection formatting

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reflected, partially_stored, skip counts, degradation or error; success is a write outcome, not epistemic proof.
- Later read-back: Proposed/admitted components may reach later recall under ordinary lifecycle and selector rules.
- Delegated visibility: Client supplies task_summary/dos/donts; formatter itself calls no critic model.
- Selection predicate: Nonempty summary, optional dos/donts, resolved domain and unlocked vault; ordinary store admission follows.
- Invalidation or expiry: Ordinary lifecycle and retrieval conditions; no automatic in-place replacement of prior lesson.
- Activation or effect: Prefixed observation/fact/observation writes with 0.85/0.90/0.90 confidence; later actual influence unobserved.
- Evidence limits: No task evidence consumed by formatter; model-generated criticism or factual success not established by supplied strings.

Distinct from [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle): this registered operation splits explicit end-task fields and assigns asymmetric types. Overlaps [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation) only in later ordinary admission, not producer/transformation. Client, not SAGE formatter, authors advice; identity leaves human authorship unresolved. Open end-task request, no per-item human approval requirement or answer oracle. Code can reject malformed/unwritable input and reports partial failure; ordinary admission vetoes content. Persisted guidance is the supplied dos/donts, not formatter-derived causal explanation.

Concrete source deduction, not execution: task_summary `Checked server access` and dos `Use TLS for service traffic` yield `[Task Reflection] Checked server access` as observation at 0.85 and `[DO] Use TLS for service traffic` as fact at 0.90. No new factual claim follows merely from prefixing. The authority-changing type/score is automatic; whether the standing rule is true/useful requires independent evidence. SRC-1 `internal/mcp/tools.go`, implementation:

> store(fmt.Sprintf("[Task Reflection] %s", taskSummary), "observation", 0.85)
> 	if dos != "" {
> 		store(fmt.Sprintf("[DO] %s", dos), "fact", 0.90)
> 	}
> 	if donts != "" {
> 		store(fmt.Sprintf("[DON'T] %s", donts), "observation", 0.90)
> 	}
> --- `internal/mcp/tools.go`

This formatter alone establishes no formulated-theory instance. Theory-builder conditions 1–4: independently uninspected for actual submitted texts; deterministic wrapping supplies neither whole theory content evidence nor content-dependent criticism. Addressability is memory-record granularity, finer claim parts uninspected; persistence is later sessions while eligible. Learning remains uninspected without improved-capacity evidence. Reflection and autonomous theory building are not established by an operation named reflect.

#### EPI-RTE-correction-check
Label: Correction availability check

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Last observed replacement status, including committed or still proposed, within bounded signed read retries.
- Later read-back: Reads newly submitted replacement through ordinary disclosure; does not persist separate evidence about its truth.
- Delegated visibility: Signed GET result is consumed by MCP code, no judge delegation.
- Selection predicate: remember with replaces_memory_id, successful replacement submission and returned ID.
- Invalidation or expiry: Caller deadline, up to ten checks and 30-second timeout end the attempt before destructive action.
- Activation or effect: Only committed status permits challenge of original; other states retain original.
- Evidence limits: Availability/lifecycle predicate is not comparison of old and new propositions.

Distinct from [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission): this is a later client-side check after that admission, not its local voter. Caller proposes correction; program decides availability; server can deny disclosure. No human factual review or answer oracle is required. Open correction request. SRC-1 `internal/mcp/tools.go`, implementation:

> replacementStatus := s.waitForCorrectionCommit(ctx, submitResp.MemoryID)
> 	if replacementStatus != "committed" {
> 		result["correction_status"] = "replacement_pending"
> 		result["replacement_status"] = replacementStatus
> 		result["message"] = "Replacement was submitted but is not committed yet; the original memory was left unchanged. Verify the replacement is committed before deprecating the original."
> 		return result, nil
> 	}
> --- `internal/mcp/tools.go`

#### EPI-RTE-correction-replace
Label: Correction replacement disposition

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Replacement ID and correction status; completed, pending, or committed replacement with old retained after challenge failure.
- Later read-back: Replacement content, parent hash and original lifecycle affect later ordinary reads; not an atomic swap.
- Delegated visibility: Client supplies replacement/reason; signed ordinary submit and challenge requests reach server/consensus.
- Selection predicate: Correction source read, same domain, inherited type when omitted, source classification and parent hash; committed replacement check precedes challenge.
- Invalidation or expiry: Failure/interruption leaves old record rather than destroying it first; can leave both. Later lifecycle handles further changes.
- Activation or effect: Operational revision/withdrawal request, not an evidence-consuming decision that replacement is more accurate.
- Evidence limits: No actual correction, semantic comparison or consumed criticism trace supplied.

Distinct from ordinary [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission): this route coordinates two records and destruction ordering. Caller proposes changed guidance; code enforces lineage/domain/classification and server controls can veto submit/challenge. Human authorship/approval unresolved; no intrinsic oracle. Recovery retains availability rather than guaranteeing semantic rollback. SRC-1 `internal/mcp/tools.go`, implementation:

> submitBody["parent_hash"] = correctionSource.ContentHash
> 		submitBody["classification"] = correctionSource.Classification
> --- `internal/mcp/tools.go`

> forgetResult, forgetErr := s.toolForget(ctx, map[string]any{
> 		"memory_id": replacesMemoryID,
> 		"reason":    reason,
> 	})
> --- `internal/mcp/tools.go`

Theory-builder conditions 1–4 remain independently uninspected for actual corrections: parent linkage can connect records but does not individuate a whole theory, show consumption of its content, locate blame, or establish retained criticism shaping another round. Persisted lineage affords inspection across sessions; it does not by itself establish learning, reflection or autonomy.

#### EPI-RTE-corroborate-signal
Label: Corroboration signal

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Consensus accept/reject and buffered corroboration including agent, memory ID, evidence and creation time.
- Later read-back: Canonical corroboration markers are scanned for app-v21 challenge electorate construction; serving corroboration also persists.
- Delegated visibility: Signed endorsing principal is attributable; evidence text is not sent to support judge in this inspected handler.
- Selection predicate: Current identity/clearance/access, existing memory, nonauthor/noncoauthor and once per principal under relevant version gates.
- Invalidation or expiry: Duplicate/self/unknown/unauthorized endorsements reject; challenge electorate snapshots later eligibility, not perpetual eligibility for every endorser.
- Activation or effect: Countable endorsement can alter subsequent challenge resistance under app-v21, not just an unused log result.
- Evidence limits: Distinct agents may share sources/models; no evidence truth/entailment assessment in this handler; historical no-author records have a self-check exception.

No supplied counterpart after comparison with [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission): corroboration is not ordinary validator accept voting. Agent proposes endorsement; code decides protocol admissibility, no per-item human review or expected-answer oracle. Open endorsement, not experiment. Guidance is caller evidence/endorsement; persistence is attribution and markers. No text revision or automatic epistemic rollback. SRC-1 `internal/abci/app.go`, implementation:

> if already {
> 			return &abcitypes.ExecTxResult{Code: 17, Log: fmt.Sprintf("corroborate: agent %s already corroborated memory %s", agentID[:16], corrob.MemoryID)}
> 		}
> --- `internal/abci/app.go`

> corr := &store.Corroboration{
> 		MemoryID:  corrob.MemoryID,
> 		AgentID:   agentCredentialID,
> 		Evidence:  corrob.Evidence,
> 		CreatedAt: blockTime,
> 	}
> --- `internal/abci/app.go`

> corroborators, corroboratorScanTruncated, corroboratorsErr := app.badgerStore.ListCanonicalCorroboratorsV21UpTo(
> 				challenge.MemoryID, challengerID, store.MaxChallengeCorroboratorScanV21,
> 			)
> --- `internal/abci/app.go`

#### EPI-RTE-lifecycle-disposition
Label: Challenge and reinstatement disposition

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Challenge or reinstatement protocol result; status may be challenged rather than immediately deprecated.
- Later read-back: Canonical status/projection and retained challenge reason/evidence affect later recall qualification or exclusion.
- Delegated visibility: Authorized challenger/confirming principals supply reason/evidence; consensus does not invoke semantic judges on those strings in inspected paths.
- Selection predicate: Current identity/clearance/domain authority, existing lifecycle, versioned electorate/quorum; app-v21 freezes electorate and corroboration-derived threshold.
- Invalidation or expiry: Unauthorized, duplicate or inappropriate-state requests reject; reinstatement can resolve open challenge to committed under rules; not a guaranteed undo for every terminal state.
- Activation or effect: Signed decisions update challenged/deprecated/committed status; disputed live recall may continue with warning/penalty.
- Evidence limits: Selected app-v17/app-v21 and reinstatement paths inspected, not every replay branch or remote-copy propagation.

Distinct from [RT-RTE-maintenance-cleanup](runtime.md#rt-rte-maintenance-cleanup): that worker selects/authorizes intent, this is the downstream lifecycle disposition also used by explicit callers. Human or software caller proposes withdrawal; authority/electorate code decides admission, can veto; no expected-answer oracle. Open lifecycle maintenance. Persisted guidance is reason/evidence plus status and prior state, not a generated explanation of falsity. SRC-1 `internal/abci/app.go`, implementation:

> nextStatus := memory.StatusChallenged
> 			if outcome.Resolved {
> 				nextStatus = memory.StatusDeprecated
> 			}
> --- `internal/abci/app.go:7318-7395`

> data:      &statusUpdate{MemoryID: rein.MemoryID, Status: memory.StatusCommitted, At: blockTime},
> --- `internal/abci/app.go:7680-7710`

#### EPI-RTE-benchmark-check
Label: LongMemEval answer evaluation

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall@5/@10, reciprocal rank, generated answer, gold answer and binary model judgment per question.
- Later read-back: Per-question results feed aggregate benchmark output; no inspected feedback of these verdicts into live SAGE memory or model training.
- Delegated visibility: Answer provider receives retrieved text and question/date; judge receives question, gold and generated answer.
- Selection predicate: Dataset question with seeded sessions, top-K retrieval, reference support-session IDs; absent gold sets score zero.
- Invalidation or expiry: Rerun/provider/configuration changes can change outcomes; repeated provider failure or invalid label yields zero rather than a distinct epistemic uncertainty state.
- Activation or effect: Scoring/reporting consumers only on inspected path; not admission, automatic policy revision or causal validation of components.
- Evidence limits: No harness execution/results evaluated here; gold source truth, temporal correctness, judge independence and calibration not established.

No supplied counterpart after comparison with [RT-RTE-targeted-recall](runtime.md#rt-rte-targeted-recall): this shipped evaluator additionally generates answers and compares against gold. Target domains differ: ID coverage in known answer sessions, and correctness of answer relative to dataset gold. Expected-answer oracle is supplied dataset `answer` and `answer_session_ids`; model judge is a fallible evaluator of agreement, not itself the oracle. OpenAI-compatible client defaults answer and judge to `gpt-4o-mini`, environment-overridable; distributed-parametric inference endpoints are not exact weight-pinned, can change behind names, and no parameter training is requested by these calls. Provider internals uninspected. No per-answer human decision coded. Bounded dataset experiment, not production admission. No component-isolation intervention established by these functions. SRC-1 `bench/longmemeval/run_with_llm.py`, implementation:

> r5 = len(top_5 & answer_sids) / len(answer_sids)
> 	r10 = len(top_10 & answer_sids) / len(answer_sids)
> --- `bench/longmemeval/run_with_llm.py`

> label = str(data.get("label", "")).strip().upper()
> 			return 1 if label == "CORRECT" else 0
> --- `bench/longmemeval/run_with_llm.py`

> context = "\n<->\n".join(retrieved_text[:top_k])
> --- `bench/longmemeval/run_with_llm.py`

> summary = aggregate(per_q)
> --- `bench/longmemeval/run_with_llm.py`

> with out.open("w") as f:
> 		json.dump(payload, f, indent=2)
> --- `bench/longmemeval/run_with_llm.py`

### Claims

#### EPI-CLM-gate-purpose
Label: Lasting and supported memory gate

Claimed operation: optional judging distinguishes lasting knowledge from session remarks and, for evidence-bearing submissions, whether evidence supports assertion. Distinct from [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn); closest supplied mechanism is [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission). SRC-1 `internal/voter/gate.go`, doctrine/design:

> // Gate is the optional memory gate: a semantic check, asked of one or more
> // operator-configured judges, of whether a proposed memory is lasting
> // knowledge or a remark about the session it came from — and, for a memory
> // submitted with evidence, whether that evidence supports it.
> --- `internal/voter/gate.go`

The narrower claim is implemented by the check/disposition parts, not demonstrated accuracy or universal admission coverage. The same source warns that self-declared confidence admitted session-specific false authority before this optional check; a broader warranted-knowledge reading would exceed both that warning and alternate paths.

#### EPI-CLM-reflect-fact
Label: Reflection dos as proven fact

Claimed operation/warrant: comment treats dos as high-confidence fact because proven to work. No supplied claim counterpart after comparison with [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn). SRC-1 `internal/mcp/tools.go`, doctrine/design:

> // Task summary as an observation, dos as a fact (high confidence — proven to
> 	// work), don'ts as an observation (prevents repeating mistakes).
> --- `internal/mcp/tools.go`

Implemented formatting assigns this authority without inspecting task outcomes. Downstream optional support can supply a check on other evidence-bearing submissions, so the finding is local to formatter authority, not a system-wide impossibility of checking.

#### EPI-CLM-feedback-learning
Label: Feedback loop learning claim

Claimed operation/warrant: reflection feedback improves later agents, citing longitudinal SAGE/control rank correlations. Distinct from [RT-CLM-atomic-turn](runtime.md#rt-clm-atomic-turn); related [RT-RTE-bridge-distillation](runtime.md#rt-rte-bridge-distillation) affords outcome-fed proposal and later reuse, not experiment verification. SRC-1 `internal/mcp/tools.go`, doctrine/design:

> "This feedback loop is critical — Paper 4 proved that agents with memory achieve Spearman rho=0.716 improvement over time while memoryless agents show rho=0.040 (no learning). " +
> --- `internal/mcp/tools.go`

SRC-1 `papers/README.md`, reported operation and disclosure. It reports a study, but expressly limits independently inspectable experiment materials:

> The pipeline scripts, organizational wiring, agent mesh, generated challenge
> artifacts and run records are excluded from that tree for IP reasons (see the Level Up
> Integration section of `.gitignore`). A fresh clone therefore cannot rerun
> those experiments or independently re-derive their reported statistics.
> --- `papers/README.md`

This report inspected the summary/disclosure, not PDFs or underlying traces. The reported treatment is a memory-backed organization, not an independently isolated consensus/gate component effect. Correlation values quoted in prompts neither show current deployment learning nor prove the mechanism by which a later action improved.
