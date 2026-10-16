---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "deja-vu's historical evidence, lifecycle authority, fix-pair checks and plan warnings at the frozen source boundary."
run-id: AAS-2026-10-14-deja-vu-22137d4d39a5-01
reviewed-boundary: "4c08fb26ad8a8b8e656a120f06ca4175a7078148"
---

# deja-vu epistemic report

## Source-and-claim boundary

The question is how deja-vu turns prior sessions and recorded decisions into later reliance, and what its checks license. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design here. No target execution was performed. The enclosing model's inference, host execution and provider weights remain outside the frozen source. Their absence prevents observations of compliance, successful repair, improved capacity and causal benefit, not reconstruction of available Go routes.

The supplied runtime is provisional. Its recall, note admission, compaction, rules and embedding records supply evidence for those routes. Direct source inspection additionally finds operative fix-pair judgment and plan checks. These prevent treating production as exclusively unchecked retrieval. Conversely, a fix-pair check is not proof of repair causation; a plan warning is not plan acceptance. No supplied runtime field needs supersession: its described APIs have the stated limits, but its coverage did not include these production checks. The comment that candidate fix pairs are never served is contradicted by the current selector; the record below keeps the implementation's explicit fallback rather than that comment's broader negative ([EPI-RTE-fix-selection](#epi-rte-fix-selection)).

Consequential warrant claims are [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit), [EPI-CLM-knows-held](#epi-clm-knows-held), and [EPI-CLM-history-judgement](#epi-clm-history-judgement). These claim priority for historical decisions, not a demonstrated general knowledge oracle. Public claims about avoiding repeated debugging are addressed only to the extent of the inspected evidence routes; no benchmark number or cross-system comparison is adopted.

### Coverage

All paths below belong to SRC-1 at the reviewed revision. Direct reads are additional inspection; supplied findings are not silently represented as direct reads.

| Entry point or operation | Source path | Coverage and records, or inspection limit and prevented conclusion |
|---|---|---|
| Frozen CLI dispatch, including `check`, `fix`, `hook-plan`, `promote`, forgetting and recovery | `cmd/deja/main.go` | Direct: command map and selected forget code. Enumerates material alternatives; not complete command-body inspection. |
| MCP discovery, modes, aliases, prompts/resources | `cmd/deja/mcp.go` | Direct: protocol dispatch and registered mode schema; supplied [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission). Resource and alias body variants not fully inspected; prevents all-surface equivalence. |
| Recall, context, automatic prompt/tool/startup/spawn delivery | `cmd/deja/hook_context.go`, `cmd/deja/hook_prompt.go`, `cmd/deja/hook_tool.go`, `cmd/deja/hook_spawn.go`, `extensions/pi/index.ts` | Supplied [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-spawn-context](runtime.md#rt-rte-spawn-context), [RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference). Other extension/installer bodies and the deferred queue in `cmd/deja/hook_deferred.go` uninspected here; prevents universal host delivery/framing, all-host immediacy, queue withdrawal and end-to-end retry-safety claims. |
| `remember`, `promote`, indexed note reload | `cmd/deja/promote.go`, `internal/sources/notes.go` | Direct distillation, write/provenance, latest-note loading and conflict check; supplied [RT-RTE-note-admission](runtime.md#rt-rte-note-admission). New parts [EPI-RTE-promote-distill](#epi-rte-promote-distill), [EPI-RTE-conflict-check](#epi-rte-conflict-check). |
| Lifecycle withdrawal and standing decisions | `internal/sources/lifecycle.go`, `cmd/deja/lifecycle.go`, `cmd/deja/hook_conventions.go` | Direct lifecycle loading and complete convention renderer; search annotation/demotion located by source search. [EPI-RTE-convention-use](#epi-rte-convention-use). Full lifecycle ranking implementation remains uninspected; prevents exact all-reader order guarantees. |
| Production fix mining, judgment, rebuild/update, requested remedy | `internal/index/fixpair.go`, `cmd/deja/fix.go` | Direct mining, judgment, merge, selector and prose renderer; [EPI-RTE-fix-check](#epi-rte-fix-check), [EPI-RTE-fix-disposition](#epi-rte-fix-disposition), [EPI-RTE-fix-retention](#epi-rte-fix-retention), [EPI-RTE-fix-selection](#epi-rte-fix-selection). Environment-variant and destructive-command helper internals not all read; prevents full safety or false-positive enumeration. |
| Plan evidence and pre-submission warning, human `check -` | `cmd/deja/hook_plan.go`, `cmd/deja/check.go`, `internal/index/plan.go` | Direct hook/selector/renderer and join setup; [EPI-RTE-plan-check](#epi-rte-plan-check), [EPI-RTE-plan-delivery](#epi-rte-plan-delivery). Join body beyond inspected setup uninspected; limits exact term-matching and completeness conclusions. |
| Compaction capture, freshness check, retry delivery | `cmd/deja/hook_compaction.go` | Supplied [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery); additional direct read of `withCommandOutcomes` and friction helper. Repository movement produces warnings, not source-truth acceptance; inferred outcome labels are assessed separately. |
| Rule candidates, user selection and cross-host standing instructions | `cmd/deja/rules_candidates.go`, `cmd/deja/rules.go`, `skills/deja-search/SKILL.md` | Supplied [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync), [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules). Model synthesis/compliance not observed. |
| Index normalization, stripping, redaction, clipping | `internal/index/ingest.go`, `internal/redact/redact.go` | Supplied [RT-OBJ-index-db](runtime.md#rt-obj-index-db). All transcript parser variants uninspected; source fidelity and provenance are not universally established. |
| Embeddings, imported batches, binary and wiring admission | `internal/embed/client.go`, `internal/embed/sidecar.go`, `internal/index/sync.go`, `cmd/deja/update.go`, `cmd/deja/wiring_state.go` | Supplied [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client), [RT-RTE-embedding-records](runtime.md#rt-rte-embedding-records), [RT-RTE-import-records](runtime.md#rt-rte-import-records), [RT-RTE-binary-update](runtime.md#rt-rte-binary-update), [RT-RTE-wiring-refresh](runtime.md#rt-rte-wiring-refresh). Integrity/shape checks have bounded nonsemantic domains. |
| Forget/unforget, note cleanup and surviving copies | `cmd/deja/main.go`, `internal/sources/notes.go` | Direct selector refusals and notes cleanup contract; supplied promotion warning about peer copies. Full deletion/restoration and cache withdrawal not traced; prevents immediate or global revocation claims. |
| `handoff`, `resume --write-back`, `share`, `restore`, `tests`, `recap`, `friction`, `files`, `how`, `view`, `wip`, specialized hooks | `cmd/deja/main.go`, `cmd/deja/handoff.go`, `cmd/deja/resume_writeback.go`, `cmd/deja/tests.go`, `cmd/deja/recap.go`, `cmd/deja/friction.go` | Dispatch located; bodies not assessed here. Relevant historical extraction/action/copy alternatives remain unassessed, preventing a system-complete negative about derivation, checking, acceptance or behavioral effect. |
| LongMemEval, plan census and context fact coverage | `scripts/longmemeval/main.go`, `scripts/planbench/main.go`, `cmd/deja/bench_context.go` | Supplied [RT-RTE-retrieval-evaluation](runtime.md#rt-rte-retrieval-evaluation); direct planbench counting and context substring scorer. [EPI-RTE-offline-scores](#epi-rte-offline-scores). Other benchmark/e2e drivers and retained result artifacts unassessed; prevents aggregate performance or causal conclusions. |
| Target warrant language | `README.md`, `cmd/deja/mcp.go`, `skills/deja-search/SKILL.md` | Direct README highlights and MCP tool description, supplied skill claim. Claims below retain source-native scope. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-index-db](runtime.md#rt-obj-index-db) | Prior session/note claims over their original project/time; recorded tool outcomes | see record | SRC-1, `internal/index/ingest.go` | Acquisition, not deja production of the imported claim. Redaction, clipping and self-recall removal limit source fidelity; original semantic warrant unknown. |
| [EPI-OBJ-promoted-text](#epi-obj-promoted-text) | Quoted ask/outcome, caller's decision statement, optional rationale | see record | SRC-1, `cmd/deja/promote.go` | Storing source ID establishes traceability, not source truth or approval. Directive-only content may have no truth-apt proposition. |
| [EPI-OBJ-lifecycle](#epi-obj-lifecycle) | State marks operationally encode a caller's judgment; no independent truth certificate | see record | SRC-1, `internal/sources/lifecycle.go` | `accepted` is a controlled marker, not evidence-consuming acceptance by itself. |
| [EPI-OBJ-fixraw](#epi-obj-fixraw) | Historical error/remedy sequence and derived check features | see record | SRC-1, `internal/index/fixpair.go` | Fixed-rule signature normalization and output parsing do not prove complete outcome observation. |
| [EPI-OBJ-fixes](#epi-obj-fixes) | Checked/candidate historical associations; model-facing error and command/file receipts | see record | SRC-1, `internal/index/fixpair.go` | Candidate state has selection force; natural-language remedy interpretation is separate from tuple lookup. |
| [RT-OBJ-policy](runtime.md#rt-obj-policy) | none: origin/activation rules | see record | SRC-1, `internal/policy/policy.go` | Selects admissible origins, not true claims or authenticated authors. |
| [RT-OBJ-rules](runtime.md#rt-obj-rules) | Predominantly directives; any factual rationale depends on actual file content | see record | SRC-1, `cmd/deja/rules.go` | No user rules instance supplied; truth-apt theory content not determinable. |
| [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client) | none individuated in provider weights or dense vectors | see record | SRC-1, `internal/embed/client.go`, `internal/embed/sidecar.go` | Mutable unpinned endpoint; training and semantic stability uninspected. |
| [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery) | Extracted goals/conclusions/outcomes and repo fingerprint | see record | SRC-1, `cmd/deja/hook_compaction.go` | Lossy continuation content, not a new validated explanation. Object is the retained packet material within the supplied route. |

## Authority-route ledger

Each compact row cites its declaring record for endpoints, activation, result, force and limitations. `see` means the field is owned there, not restated as another canonical finding. All statuses here concern architecture, not observed operation.

Route ID: [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-promoted-text](#epi-obj-promoted-text), [EPI-OBJ-lifecycle](#epi-obj-lifecycle)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see route; caller supplies note or lifecycle change.
Evaluator/condition and domain: see route; storage/structure, not proposition truth.
Activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: Source warrant unknown; explicit marking licenses caller-designated reliance only, not validated truth.
Operational authority; behavioral-authority path: see route and [RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference).
Evidence source ID and local anchor: SRC-1, `cmd/deja/promote.go`.
Claim IDs: [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit).
Mismatch marker: Do not equate named `accepted` state with epistemic acceptance.
Gap/limit: No particular stored note, evidence criterion or human approval trace supplied.

Route ID: [EPI-RTE-promote-distill](#epi-rte-promote-distill)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-promoted-text](#epi-obj-promoted-text)
Content/update relation: truth-apt transformation: indeterminate
Relation scope: Factual excerpts only. Copying preserves selected words, but selection and truncation do not establish preservation of their proposition's scope. Non-ampliative reshaping remains possible for complete preserved claims; deciding requires the input and delivered claim with all necessary qualifications. Directive-only extraction is a non-truth-apt policy/content update, assessed separately below.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Selected historical receipts only, not an entailed repair explanation. Semantic completeness is not licensed.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `cmd/deja/promote.go`.
Claim IDs: [EPI-CLM-knows-held](#epi-clm-knows-held).
Mismatch marker: `outcome` may be the last assistant text or detected decision, not a verified outcome.
Gap/limit: Truncation and artifact heuristics can omit qualifications.

Route ID: [EPI-RTE-conflict-check](#epi-rte-conflict-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-promoted-text](#epi-obj-promoted-text)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Topic-overlap notification, not proof of contradiction.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/sources/notes.go`.
Claim IDs: [EPI-CLM-knows-held](#epi-clm-knows-held).
Mismatch marker: Warning occurs after write; no automatic rejection or resolution.
Gap/limit: No human resolution observed.

Route ID: [EPI-RTE-convention-use](#epi-rte-convention-use)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-promoted-text](#epi-obj-promoted-text), [EPI-OBJ-lifecycle](#epi-obj-lifecycle)
Content/update relation: truth-apt transformation: indeterminate
Relation scope: Factual reminder content only. The first-sentence countercase establishes scope loss, not semantic preservation. A complete preserved proposition would be non-ampliative reshaping; a broader emitted proposition could be ampliative, but deciding requires its actual semantic reading and original scope. Pure directives are not truth-apt and have a separate row below.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Caller-marked current project decisions, not independently established correctness.
Operational authority; behavioral-authority path: see record and [RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference).
Evidence source ID and local anchor: SRC-1, `cmd/deja/hook_conventions.go`.
Claim IDs: [EPI-CLM-knows-held](#epi-clm-knows-held), [EPI-CLM-history-judgement](#epi-clm-history-judgement).
Mismatch marker: Standing decision instruction and untrusted-history framing have distinct requested forces; model interpretation resolves them, not a strict gate.
Gap/limit: First-sentence selection can materially weaken the premise of reliance; stale caches and peer copies prevent immediate universal withdrawal.

Route ID: [EPI-RTE-fix-check](#epi-rte-fix-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixraw](#epi-obj-fixraw)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Conditional on faithful parsed records and error-signature interpretation, sequence, absence of detected command/output failure and specified absence of repeat are derivable. A recorded successful outcome is not required; an unknown outcome can pass. No premise warrant for actual repair causation follows.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/index/fixpair.go`.
Claim IDs: [EPI-CLM-history-judgement](#epi-clm-history-judgement).
Mismatch marker: Missing error recurrence is not proof of resolution or transfer; edit fallback differs from checked command branch.
Gap/limit: No live outcome reference or controlled comparison.

Route ID: [EPI-RTE-fix-disposition](#epi-rte-fix-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixes](#epi-obj-fixes)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: An evidence-consuming acceptance criterion for historical remedy selection, not acceptance of an ampliative causal claim that the remedy fixed the error.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/index/fixpair.go`.
Claim IDs: [EPI-CLM-history-judgement](#epi-clm-history-judgement).
Mismatch marker: Source's confirmation terminology exceeds its license if read as causation.
Gap/limit: Correlated repeats and term sharing have no guaranteed semantic specificity.

Route ID: [EPI-RTE-fix-retention](#epi-rte-fix-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixraw](#epi-obj-fixraw), [EPI-OBJ-fixes](#epi-obj-fixes)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Retains receipts and dispositions; not evidence-linked integration of an accepted causal theory.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/index/fixpair.go`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Bounded caps and best-effort sidecar writes; durability unobserved.

Route ID: [EPI-RTE-fix-selection](#epi-rte-fix-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fixes](#epi-obj-fixes)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Historical sequence, explicitly unconfirmed for fallback sightings; no replay-safety or repaired-project guarantee.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/index/fixpair.go`, `cmd/deja/fix.go`.
Claim IDs: [EPI-CLM-history-judgement](#epi-clm-history-judgement).
Mismatch marker: Candidates can be served, contrary to the struct comment; confirmed-only plan consumer remains narrower.
Gap/limit: Rendering is not execution; helper filters are bounded and not a permission sandbox.

Route ID: [EPI-RTE-plan-check](#epi-rte-plan-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-index-db](runtime.md#rt-obj-index-db), [EPI-OBJ-fixes](#epi-obj-fixes)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Counts retained eligible carrier sessions for a historical wall; the proposed plan's future failure is not entailed. Join interpretation and exact match coverage remain bounded by inspected code.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `cmd/deja/hook_plan.go`, `internal/index/plan.go`.
Claim IDs: none.
Mismatch marker: Repeated wall evidence is not a plan validity or decision-reversal checker.
Gap/limit: No executed plans or outcomes.

Route ID: [EPI-RTE-plan-delivery](#epi-rte-plan-delivery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-index-db](runtime.md#rt-obj-index-db), [EPI-OBJ-fixes](#epi-obj-fixes)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Warning/reference only, not an approval certificate.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `cmd/deja/hook_plan.go`, `cmd/deja/check.go`.
Claim IDs: none.
Mismatch marker: Silence has several causes and cannot mean safe plan.
Gap/limit: Dedupe and budgeting can omit findings; host reception and action unobserved.

Route ID: [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), [RT-RTE-spawn-context](runtime.md#rt-rte-spawn-context)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)
Content/update relation: truth-apt transformation: indeterminate
Relation scope: Delivered factual excerpts, not ranking alone. Reordering intact claims is non-ampliative reshaping; budgeted extraction across these mixed routes does not establish preservation of every claim's scope. Complete input/output propositions are needed to distinguish preserved reshaping from changed or ampliative claims. Directive-only delivery has no truth-apt transformation.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see each cited route separately.
Epistemic authority and scope: Ranking/relevance does not validate returned propositions.
Operational authority; behavioral-authority path: see each route and [RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference); requested, unsolicited and child-input channels stay distinct.
Evidence source ID and local anchor: SRC-1, `cmd/deja/mcp.go`, `extensions/pi/index.ts`, `cmd/deja/hook_spawn.go`.
Claim IDs: [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit).
Mismatch marker: Delivered rule priority is a request, not enforced obedience.
Gap/limit: Route-specific policy, cache and host contracts differ; grouping asserts only their common warrant limit.

Route ID: [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see record's retained continuation packet.
Content/update relation: truth-apt transformation: indeterminate
Relation scope: Extracted factual goals/conclusions/receipts, excluding the inferred outcome edge below. Intact copies can be non-ampliative reshaping, but lossy extraction does not establish semantic preservation for every delivered claim. The input and output propositions and qualifications are needed to decide. Pure carry instructions remain non-truth-apt.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Repository-freshness warning and transcript receipts; neither warrants source truth nor successful continuation.
Operational authority; behavioral-authority path: see record; output-write success licenses dedupe, not proof of model receipt.
Evidence source ID and local anchor: SRC-1, `cmd/deja/hook_compaction.go`.
Claim IDs: none.
Mismatch marker: Freshness is not acceptance.
Gap/limit: Extraction completeness and actual use unobserved.

Route ID: [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see record's packet command outcomes.
Content/update relation: truth-apt transformation: ampliative conjecture
Transition or check target: A test entry marked `recorded` is assigned `passed` or `failed` by `withCommandOutcomes`.
Evaluator/condition and domain: Go friction recognizer over tool output after a command; not an independent success oracle.
Activation and timing: Capture, before later recovery delivery.
Possible or observed result: No recognized friction in encountered output yields `passed`; recognized friction yields `failed`; absent associated output leaves the entry unchanged.
Implemented force: Replaces the packet outcome label for later model-facing recovery.
Epistemic authority and scope: Recognizer results license detected-failure facts only. A command can fail without a recognized friction line, so the premises do not entail actual passing.
Operational authority; behavioral-authority path: see recovery route; inferred outcome enters advisory continuation text for a later host inference, not a permission grant.
Evidence source ID and local anchor: SRC-1, `cmd/deja/hook_compaction.go`.
Claim IDs: none.
Mismatch marker: `passed` exceeds the no-detected-friction premise if interpreted as actual command success.
Gap/limit: No target execution or success validation; current implementation supports label production, not outcome truth.

> if failed {
> 				outcome[pending] = "failed"
> 			} else {
> 				outcome[pending] = "passed"
> 			}
> --- `cmd/deja/hook_compaction.go`

> if got, ok := outcome[compactionCommandKey(data.Tests[i].Command)]; ok && data.Tests[i].Outcome == "recorded" {
> 			data.Tests[i].Outcome = got
> 		}
> --- `cmd/deja/hook_compaction.go`

Route ID: [EPI-RTE-promote-distill](#epi-rte-promote-distill), [EPI-RTE-convention-use](#epi-rte-convention-use), [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see each record's extracted directive text, distinct from its factual content.
Content/update relation: non-truth-apt policy/content update: selecting and shortening directives for later reminders or continuation
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see each cited route separately; this row covers only pure directives.
Epistemic authority and scope: None from imperative extraction; a directive need not state a proposition.
Operational authority; behavioral-authority path: see each route; copying, standing-decision reminders and carry instructions have route-specific requested force, not verified obedience.
Evidence source ID and local anchor: SRC-1, `cmd/deja/promote.go`, `cmd/deja/hook_conventions.go`, `cmd/deja/hook_compaction.go`.
Claim IDs: [EPI-CLM-knows-held](#epi-clm-knows-held).
Mismatch marker: Extraction does not make a directive truth-apt; removal of a directive's scope can change requested behavior.
Gap/limit: No supplied concrete packet or note instance; mixed factual rationale must be assessed separately.

Route ID: [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-rules](runtime.md#rt-obj-rules)
Content/update relation: non-truth-apt policy/content update: copying standing directives into host rule files
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see route for distribution; model synthesis and user-selection requirement are doctrine, not implemented model behavior.
Epistemic authority and scope: Structural admission does not establish factual accuracy of proposed rules.
Operational authority; behavioral-authority path: see route and [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules).
Evidence source ID and local anchor: SRC-1, `cmd/deja/rules.go`, `skills/deja-search/SKILL.md`.
Claim IDs: [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit).
Mismatch marker: API can copy source text without checking workflow consent.
Gap/limit: No user rule instance or behavioral trace; semantic synthesis, compliance and improvement remain unobserved.

Route ID: [RT-RTE-embedding-records](runtime.md#rt-rte-embedding-records)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client)
Content/update relation: non-truth-apt policy/content update: dense retrieval representation and ranking
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Shape/model-name checks and numerical similarity do not license proposition truth.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/embed/client.go`, `internal/embed/sidecar.go`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Distributed-parametric state does not expose individuated truth-apt content here; exact weights and mutability unresolved.

Route ID: [RT-RTE-import-records](runtime.md#rt-rte-import-records)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: Source warrant unknown; integrity/attribution is not authenticated per-claim truth.
Operational authority; behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `internal/index/sync.go`.
Claim IDs: none.
Mismatch marker: Local withdrawal does not revoke remote copies.
Gap/limit: Full merge/export/SSH protocol uninspected.

Route ID: [RT-RTE-binary-update](runtime.md#rt-rte-binary-update), [RT-RTE-wiring-refresh](runtime.md#rt-rte-wiring-refresh)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see records' binary/configuration objects.
Content/update relation: non-truth-apt policy/content update: product executable and host wiring replacement
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see each record separately.
Epistemic authority and scope: Hash agreement and version/path checks have no product-correctness license.
Operational authority; behavioral-authority path: see each record; replacement and discovery alter later available machinery, not validated experience learning.
Evidence source ID and local anchor: SRC-1, `cmd/deja/update.go`, `cmd/deja/wiring_state.go`.
Claim IDs: none.
Mismatch marker: Integrity is not authenticated release provenance or behavior verification.
Gap/limit: Installed execution and excluded release pipeline not established.

Route ID: [RT-RTE-retrieval-evaluation](runtime.md#rt-rte-retrieval-evaluation), [EPI-RTE-offline-scores](#epi-rte-offline-scores)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see records' dataset and temporary evaluation inputs.
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see each record separately.
Epistemic authority and scope: Gold-session rank, emitted-wall census and literal fact coverage have different target domains; none verifies explanation, repair causation or real-host compliance.
Operational authority; behavioral-authority path: see records; scores are reported, with no inspected automatic production admission consumer.
Evidence source ID and local anchor: SRC-1, `scripts/longmemeval/main.go`, `scripts/planbench/main.go`, `cmd/deja/bench_context.go`.
Claim IDs: none.
Mismatch marker: Printed success measures cannot be generalized to knowledge correctness or component benefit.
Gap/limit: No evaluation executed; artifacts and other drivers unassessed.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit) | see record | SRC-1, `skills/deja-search/SKILL.md`; doctrine/design | see record | [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync) | none supplied | No intervention/compliance evidence; host model controls action | Search and retention interfaces implement the opportunity; skill requests priority and settled facts | Framed untrusted history versus directive priority requires semantic interpretation. |
| [EPI-CLM-knows-held](#epi-clm-knows-held) | see record | SRC-1, `README.md`; doctrine/design | see record | [EPI-RTE-convention-use](#epi-rte-convention-use), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) | none supplied | Caller-controlled state does not verify original decision or rationale | Records caller judgment and can exclude withdrawn decisions from conventions | `Knows` is justified as recorded lifecycle awareness, not independent truth judgment; a rejected mark alone need not say why. |
| [EPI-CLM-history-judgement](#epi-clm-history-judgement) | see record | SRC-1, `cmd/deja/mcp.go`; doctrine/design | see record | [EPI-RTE-fix-check](#epi-rte-fix-check), [EPI-RTE-fix-disposition](#epi-rte-fix-disposition), [EPI-RTE-fix-selection](#epi-rte-fix-selection), [EPI-RTE-convention-use](#epi-rte-convention-use) | none supplied | Historical sequence and bounded heuristic evidence, not repair attribution or verified human authorship | Fix output can say what followed an error; state markers can convey explicit recorded judgment | Generic software/MCP caller is not proven to be the user; unconfirmed fallback and noncausal reading remain necessary. |

## Bounded conclusion

**Historical acquisition and extractive mechanisms are established, but semantic preservation and source warrant are not universal.** Prior prose and recorded outcomes enter a derived index, with redaction, normalization, selection and clipping. Promotion adds a source identity and selected receipts; it does not create a verified explanation. These routes preserve some lineage while degrading completeness ([RT-OBJ-index-db](runtime.md#rt-obj-index-db), [EPI-RTE-promote-distill](#epi-rte-promote-distill)). No particular candidate instance or warranted source premise was supplied. The implementation can derive historical facts from encoded records; it does not establish that those premises accurately represent the real event.

**There are operative production checks, with narrow licenses.** Fix mining rejects command candidates with detected failure and repeated-error command associations. It does not require a recorded nonfailure: missing exit status and missing nearby output can both pass the failure detectors. The entailed result is about the parsed sequence and detector outputs, not actual success. Judgment consumes parsed evidence to mark pairs as confirmed or candidate for the intended use of historical remedy selection. The criterion uses repaired/substitute features, shared error-command terms, or eligible repetition; it is not an experiment proving remedy efficacy. Retention preserves raw sightings so later evidence can change the candidate flag. Selection consumes the flag and privacy/safety predicates, preferring confirmed pairs but exposing explicitly unconfirmed fallback. This is implemented trace-fed adaptation of future suggestions, independent of whether it improves capacity ([EPI-RTE-fix-check](#epi-rte-fix-check), [EPI-RTE-fix-disposition](#epi-rte-fix-disposition), [EPI-RTE-fix-retention](#epi-rte-fix-retention), [EPI-RTE-fix-selection](#epi-rte-fix-selection)). No produced accepted ampliative causal claim is established by this criterion: the intended license is historical association, not “this command caused recovery.”

**Plan checking supplies evidence, not acceptance.** The check concerns recurring indexed error walls related to a plan's terms; it reports carrier-session counts and optional command associations. PreToolUse supplies framed additional context before plan submission without an inspected deny decision. `check -` reports a miss's cause but still does not certify a plan. The model/user remains the consequential decision maker ([EPI-RTE-plan-check](#epi-rte-plan-check), [EPI-RTE-plan-delivery](#epi-rte-plan-delivery)). Neither outcome success nor complete inspection of all plan-join matching is supplied.

**Lifecycle marks grant operational reliance without certifying truth.** Explicit notes and latest caller marks persist, accepted project notes become standing-decision reminders, and nonaccepted notes do not enter that block. The source-native `accepted` value does not require evidence, a named epistemic criterion or per-content human approval. Topic overlap produces only an after-write warning. A concrete text transformation below shows that a conventional first-sentence renderer can remove the scope condition from a decision. Factual reminders therefore have an indeterminate content relation without an input/output semantic check, rather than a settled non-ampliative classification; directive reminders are non-truth-apt updates. Reliance is licensed no more broadly than the original decision, even if the reminder loses that boundary ([EPI-RTE-conflict-check](#epi-rte-conflict-check), [EPI-RTE-convention-use](#epi-rte-convention-use)). Withdrawal can change local selection; exported copies and stale caches prevent inferring immediate global revocation. No evidence-consuming lifecycle integration of an accepted new theory is established on these inspected routes; broader negative conclusions are prevented by the named unassessed operations.

**Instruction copying is a separate behavioral channel.** User-selection-before-write is prescribed for model-produced rule candidates; code sync admits structurally valid source text and installs standing directives for later host sessions. This can change later behavior without a truth-apt update. The request, file distribution, actual host loading, model obedience and improvement are separate claims ([RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync), [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules)). Recall is otherwise historical reference with advisory/ranking force, not an action executor ([RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference)).

**Freshness, retrieval scores and numerical embeddings keep separate domains.** Compaction fingerprints qualify reuse, checksum checks qualify executable agreement, and embedding shape checks admit vectors. None checks source truth. Compaction extraction has no general semantic-preservation license; its additional `passed` inference from output with no detected friction is ampliative, since an undetected failure is compatible with that evidence. Pure continuation directives remain non-truth-apt updates, not factual derivations. The embedding provider is mutable and unpinned; its parameters and internal learning cannot be assessed. Offline checks score rank/membership, warning counts or literal coverage, not explanation validity or transfer ([RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery), [RT-RTE-binary-update](runtime.md#rt-rte-binary-update), [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client), [RT-RTE-retrieval-evaluation](runtime.md#rt-rte-retrieval-evaluation), [EPI-RTE-offline-scores](#epi-rte-offline-scores)).

These positives do not establish observed learning, reflection, autonomous theory building or exercised self-improvement. The record transitions and later consumers are inspectable capacities; actual behavior depending on them and causal improvement are not supplied. The retained state is receipts, caller decisions, heuristic dispositions and instructions, not demonstrated content-directed theory criticism. Rule content and inaccessible model processing remain unresolved rather than declared absent. There is no single system epistemic score or system-complete negative.

## Shared records

### Operative objects

#### EPI-OBJ-promoted-text
Label: Promoted note text

Source-native identity: `note.Text`/`PromotedNote.Text`, plus title, project and session provenance, in notes JSONL. Natural-language content on a local filesystem is interpreted by later models/humans. This is the raw note text, not the derived [RT-OBJ-index-db](runtime.md#rt-obj-index-db), and not [RT-OBJ-rules](runtime.md#rt-obj-rules)'s global directive source. It is content admitted by [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), not a duplicate declaration of that API route. SRC-1, `cmd/deja/promote.go`, `internal/sources/notes.go`.

> if text == "" {
> 		text = distillSession(s)
> 	}
> --- `cmd/deja/promote.go`

> n.Project, n.State, n.Title, n.Text, n.Tags, n.At = project, state, title, text, tags, t
> --- `internal/sources/notes.go`

#### EPI-OBJ-lifecycle
Label: Promoted lifecycle state

Source-native identity: `Lifecycle.State`, `Note`, `At`, keyed by source session in `PromotedLifecycles()`. Symbolic controlled state and key fields govern fixed selection; the accompanying natural-language rationale is separately interpreted in historical output. Notes JSONL and process memoization hold these fields. Distinct from the prose of [EPI-OBJ-promoted-text](#epi-obj-promoted-text) and the configuration grants of [RT-OBJ-policy](runtime.md#rt-obj-policy); closest supplied route is [RT-RTE-note-admission](runtime.md#rt-rte-note-admission). No supplied object declares this raw keyed state separately. SRC-1, `internal/sources/lifecycle.go`.

> type Lifecycle struct {
> 	State string    // accepted, rejected, superseded, stale
> 	Note  string    // why, in the words of whoever recorded it
> 	At    time.Time // when the state was last set
> }
> --- `internal/sources/lifecycle.go`

#### EPI-OBJ-fixraw
Label: Raw fix sightings

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Source-native identity: `fixraw.gob` in the index directory, holding per-session `FixPair` inputs to later judgment. Filesystem/gob storage, symbolic tuple identities, times, signatures and features; error/command/edit strings are recorded natural-language or command receipts that reach interpretation only at a later output consumer. Raw retained associations are distinct from the served disposition-bearing table [EPI-OBJ-fixes](#epi-obj-fixes). SRC-1, `internal/index/fixpair.go`.

> _ = writeGob(fixRawPath(tmp), all)
> --- `internal/index/fixpair.go`

#### EPI-OBJ-fixes
Label: Judged fixes table

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Source-native identity: `fixes.gob`, a bounded judged `FixPair` table including `Candidate`, `Repaired`, `Substitute`, `Failed`, error signatures, project/key and remedy. Symbolic selection fields and string receipts share filesystem/gob storage but have different consumers: code selects by signature/flags, then a model or human interprets the rendered command/error or edited file. This is a material sidecar part, not a duplicate of the index container; there is no supplied fix-sidecar counterpart. SRC-1, `internal/index/fixpair.go`.

> if kept := judgeFixes(all); len(kept) > 0 {
> 		_ = writeGob(fixesPath(tmp), kept)
> 	}
> --- `internal/index/fixpair.go`

### Routes

#### EPI-RTE-promote-distill
Label: Promotion receipt extraction

Part of: [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

This is the default text-production part of CLI promote, not a second admission route. `distillSession` scans retained messages, skipping blanks and agent artifacts; takes the first user ask and last assistant text; prefers a detected decision from `digest.Conclusions`; then trims whitespace and 300-rune excerpts. Owner: fixed Go extraction code. Endpoints: parsed session to note body, then the parent writer/index route. SRC-1, `cmd/deja/promote.go`. It is implemented extraction, not generation of a proposition warranted beyond the excerpt. Copying complete factual claims can be non-ampliative reshaping, but these selections/truncations do not establish that classification for every emitted proposition; their factual content relation remains indeterminate without semantic comparison. Extracted pure directives are non-truth-apt updates. The extracted `outcome` can be a final assistant statement without a measured outcome. `--note` bypasses this extraction and imports caller text.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: An ask/outcome string or a no-text placeholder, passed to the notes writer.
- Later read-back: Persisted promoted text feeds indexing, recall and project conventions through the parent admission route.
- Delegated visibility: Later host consumers may receive the note; no child execution is owned here.
- Selection predicate: Nonblank nonartifact messages, first user/last assistant, optional detected decision, bounded excerpts; caller override takes precedence.
- Invalidation or expiry: Later promotion appends another version; retention and tombstones follow the parent route.
- Activation or effect: Note body selection is implemented; changed agent behavior is unobserved.
- Evidence limits: Artifact/decision helpers and truncation do not certify semantic completeness, correctness or original human assent.

Proposer/decider is caller plus extractor; invocation can be declined, invalid sources refused and text overridden. No answer oracle or semantic veto is present in the inspected function. Mode: open explicit command, with correction by later append. Proposal guidance is to retain receipts; source, state and text persist, not a newly tested theory.

> if ask == "" && m.Role == "user" {
> 			ask = t
> 		}
> 		if m.Role == "assistant" {
> 			answer = t
> 		}
> --- `cmd/deja/promote.go`

> if cs := digest.Conclusions(s, promoteDecisionBudget, 1); len(cs) > 0 {
> 		if d := strings.TrimSpace(cs[0]); d != "" && digest.CarriesDecision(d) {
> 			answer = d
> 		}
> 	}
> --- `cmd/deja/promote.go`

#### EPI-RTE-conflict-check
Label: Accepted note overlap check

Part of: [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

This is an after-write check part of CLI promotion. Target: topic overlap between the newly marked accepted note and other accepted notes in the same project. Evaluator: Go `ConflictingNotes`, with shared normalized tags or at least three informative shared words. Its domain is overlap, not logical incompatibility or truth. A warning names another note; it neither rejects the append nor resolves which claim should stand. SRC-1, `internal/sources/notes.go`, `cmd/deja/promote.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of overlapping notes, rendered as conflict warnings after append/index attempt.
- Later read-back: inapplicable — the check output itself is not retained as a critic result; underlying notes remain available independently.
- Delegated visibility: Warning reaches CLI caller; onward use is caller-controlled.
- Selection predicate: Accepted state, same project, different source session, shared tag or three informative words.
- Invalidation or expiry: Later note/lifecycle changes alter future comparisons; existing warning has no revocation state.
- Activation or effect: Advisory warning is implemented, with no enforcing write gate or observed human resolution.
- Evidence limits: Topic coincidence can occur without contradiction; disjoint wording can miss a contradiction.

Proposer is the caller's note; computational evaluator produces warnings; user/caller may append a superseding mark, but no per-content human decision is enforced. No expected-answer oracle. Mode: open requested promotion. Rollback/recovery belongs to the parent append/lifecycle/forget route, not this check.

> if shareTag || shared >= 3 {
> 			out = append(out, n)
> 		}
> --- `internal/sources/notes.go`

> for _, c := range sources.ConflictingNotes(me, all) {
> 			fmt.Fprintf(stdout, "conflict: another accepted note covers this ground — %q (from %s, %s). If one replaced the other: deja promote <id> --state superseded\n",
> 				firstLine(c.Title+" "+c.Text), c.Session, c.At.Format("2006-01-02"))
> 		}
> --- `cmd/deja/promote.go`

#### EPI-RTE-convention-use
Label: Project convention selection

`projectConventions` consumes current note states and prose and emits a query-independent project block. This is the standing-decision selection/renderer inside the broader [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), but its referent includes local and imported note consumers, not another declaration of the whole event-delivery chain. It overlaps [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) at the retained input; admission is not its endpoint. SRC-1, `cmd/deja/hook_conventions.go`, `internal/sources/notes.go`.

Go code keeps local accepted project notes, adds imported accepted in-scope notes allowed by automatic policy, orders newest first, deduplicates rendered lines and imposes note/byte budgets. The block requests following standing decisions unless the user overrides. Nonaccepted states are excluded from this block, not necessarily erased from general historical recall. The broader cache/framing caveats remain those of [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A bounded standing-decision reminder or empty string for the startup digest builder.
- Later read-back: Persisted local notes and imported metadata supply future project-context invocations; latest states change eligibility.
- Delegated visibility: Startup host delivery is supplied by the runtime route; child visibility is not automatically inherited.
- Selection predicate: Accepted latest local note, project match, or accepted imported metadata with auto grant and project scope; newest-first and rendered-line dedupe.
- Invalidation or expiry: Lifecycle changes remove eligibility at a fresh build; matching stale digest caches and peer copies can retain earlier bytes.
- Activation or effect: Eligibility and rendering enforce selection; directive force on the receiving model is requested and unobserved.
- Evidence limits: Caller state is not independent truth evaluation; first-sentence/200-byte rendering and title fallback do not preserve every scope condition.

Proposer is the note caller/peer; decider is fixed selector code; caller can change state and user can override the resulting instruction. No answer oracle. Mode: automatic context supply from explicitly or externally admitted state, with no new per-reminder human approval. This is operational use before demonstrated epistemic acceptance, not lifecycle integration of a warranted new theory.

A concrete implementation deduction, not an executed probe: for note text `Use pgx. Only in service A.` and accepted state in the selected project, `conventionLine` replaces newlines, finds the first period followed by a space, and returns `Use pgx.`. The consumer receives no `Only in service A.` qualifier. The countercase rules out unqualified semantic-preservation assurance. This directive example demonstrates changed requested scope, not production of a truth-apt proposition. For factual notes the same renderer leaves preservation versus changed proposition scope indeterminate unless the actual input/output claim is assessed; extractive implementation alone cannot settle the relation.

> if n.State != "accepted" || !want[n.Project] {
> 			continue
> 		}
> --- `cmd/deja/hook_conventions.go`

> b.WriteString("standing decisions in this project (promoted and still accepted — follow them unless the user overrides):\n")
> --- `cmd/deja/hook_conventions.go`

> for i, r := range text {
> 		if (r == '.' || r == '!' || r == '?') && (i+1 >= len(text) || text[i+1] == ' ') {
> 			return strings.TrimSpace(text[:i+1])
> 		}
> 	}
> --- `cmd/deja/hook_conventions.go`

#### EPI-RTE-fix-check
Label: Historical remedy evidence checks

No supplied counterpart after comparison with [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall): this production-side `fixPairsIn` route evaluates transcript evidence before later lookup. Endpoints: parsed message stream to raw fix associations. Owner/evaluator: fixed Go rules. Check target: whether a later command in a ten-record window has no detected command/output failure and no later repeat of the normalized error in the supplied session. Recorded exit status and nearby tool output are optional evidence inputs, not an independent expected-answer oracle. `commandFailed` returns false for an unrecorded exit, and `outputFailed` returns false when no nearby output is found (or another command is reached first). Thus a command with unknown outcome can pair if the remaining gates pass; the check does not establish recorded nonfailure. Error signatures and parsing condition the domain. SRC-1, `internal/index/fixpair.go`.

The scanner rejects commands with detected failure, investigation commands except repaired/substituted variants, open-input scripts and ephemeral paths. A repaired/substitute command relation is a fixed feature check, not an executed reproduction. Material countercase: when no command pairs but a suitable file was edited, the edit fallback appends an association without the command branch's nonrepeat/failure gates. Thus command and edit evidence strengths differ; the later repeat criterion for edit admission cannot be treated as proof of successful edit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `FixPair` sightings carrying error, command or edited file, key/time/project and detected relation features.
- Later read-back: Raw associations persist through the retention route and enter later judgment/selection; this evaluator does not itself own disk writes.
- Delegated visibility: No model child; model-facing consequences occur at later fix consumers.
- Selection predicate: Recognized error in assistant/tool output, nearby eligible command with no later matching error and no recognized command/output failure; separate edit fallback when no command pairs.
- Invalidation or expiry: Reparsed/replaced session is remined; changed transcript evidence can remove an earlier association.
- Activation or effect: Check results constrain which command associations reach judgment; benefit and actual fixes remain unobserved.
- Evidence limits: An absent exit and absent nearby output are not positive nonfailure evidence but can pass; unrecognized failures can also pass. Edit fallback has a weaker target domain; sequence does not establish causation or replay safety.

Proposer is trace-derived candidates; computational evaluator can discard associations, without per-content human approval. Mode: index-derived evidence processing, not online experimentation. Improvement objective is useful historical remedies; admitted evidence is receipts/features, not a tested causal explanation. The original host produced the commands/outcomes; deja does not execute them. It cannot claim warranted entailed derivation about the real world without warranted transcript premises.

> if lastSeen[sig] > j {
> 				break
> 			}
> --- `internal/index/fixpair.go`

> func commandFailed(text string) bool {
> 	_, code, recorded := CommandExitOutcome(text)
> 	return recorded && code != 0
> }
> --- `internal/index/fixpair.go`

> func outputFailed(ms []model.Message, cmd int) bool {
> 	for k := cmd + 1; k < len(ms) && k <= cmd+fixOutputWindow; k++ {
> 		if ms[k].Role == roleCommand {
> 			return false
> 		}
> 		if ms[k].Role != roleToolOutput {
> 			continue
> 		}
> 		return outputReadsAsFailure(ms[k].Text)
> 	}
> 	return false
> }
> --- `internal/index/fixpair.go`

> if commandFailed(ms[j].Text) || outputFailed(ms, j) {
> 				continue
> 			}
> --- `internal/index/fixpair.go`

> if !paired && edited != "" && looksLikeEditedPath(edited) {
> 			out = append(out, FixPair{Sig: sig, Error: line, Edit: edited, Key: key, When: m.Time, Project: project, Also: also})
> 		}
> --- `internal/index/fixpair.go`

#### EPI-RTE-fix-disposition
Label: Remedy candidate disposition

No supplied counterpart: [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall) ranks requests, whereas `judgeFixes` consumes raw sightings and assigns `Candidate` before future remedy use. Endpoints: all raw associations to a sorted bounded disposition-bearing table. Owner/evaluator is Go `judgeFixes`. Criterion: `selfEvidentPair` or permitted repetition with at least two same-key sightings. For commands, self-evidence is repaired/substitute feature or term sharing; edits are not self-evident. Repetition eligibility excludes certain cases. Domain/intended use: evidence sufficiency for historical remedy selection, not mechanism truth. SRC-1, `internal/index/fixpair.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Confirmed/candidate flags in a deduplicated bounded table, newest first.
- Later read-back: Persisted flags are consumed by `FixesFor`, plan remedy filtering and future rejudgment after more trace input.
- Delegated visibility: Flags reach model/human readers through selection/rendering, not via an autonomous critic agent.
- Selection predicate: Self-evident features or allowed repeat count; key dedupe and separate candidate/pair caps.
- Invalidation or expiry: New or replaced raw sightings cause rejudgment; caps evict older entries, and later evidence can change disposition.
- Activation or effect: Flags have ranking/admission force at consumers; they do not execute a remedy or guarantee correctness.
- Evidence limits: Repetition is observational and may share confounds; shared terms can be irrelevant; exact eligibility helpers were not fully inspected, so no exhaustive specificity guarantee.

Computational proposer is the miner, decider is judge code, veto is feature/repetition/cap selection. Human per-pair approval not required; no answer oracle. Mode: ongoing trace-fed admission, not controlled experiment. The guidance is the implemented evidence heuristic; what persists is associations and a disposition flag. No formulated content-directed criticism of a causal theory is evidenced by changing the flag.

> p.Candidate = !selfEvidentPair(p) && (!repetitionConfirms(p) || repeats[fixKey(p)] < 2)
> --- `internal/index/fixpair.go`

> if p.Edit != "" {
> 		return false
> 	}
> 	return p.Repaired || p.Substitute || sharesTerm(p.Error, p.Command)
> --- `internal/index/fixpair.go`

#### EPI-RTE-fix-retention
Label: Fix evidence retention

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

The parent is an object: this route is its fix-sidecar maintenance operation, not a duplicate container declaration. Endpoints: mined raw sightings and judged table to `fixraw.gob` and `fixes.gob`; update reads prior raw evidence, removes replaced/nonlive keys, redacts carried text, remines replacement sessions and rewrites tables. Owner is index build/update code. New raw evidence can change a later judgment instead of a candidate being discarded before confirmation arrives. This is retention and recomputation, not evidence-linked integration of an accepted causal claim. SRC-1, `internal/index/fixpair.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Best-effort gob sidecar writes; build errors for these extras are swallowed rather than failing the index.
- Later read-back: Updates read raw sightings; lookup reads judged table and uses flags/keys in later invocations.
- Delegated visibility: Later CLI/MCP/hooks can consume derived receipts subject to their own filters; no network copy is established here.
- Selection predicate: Per-session mining, live/unreplaced key retention, rejudgment and bounded pair/candidate caps.
- Invalidation or expiry: Replaced or nonlive keys are dropped; redaction can alter carried strings; torn/legacy raw storage triggers remine.
- Activation or effect: Stored evidence shapes later dispositions and selection; no observed durability or improved capacity.
- Evidence limits: Best-effort storage and bounded caps are not universal lossless retention or global revocation.

Mode: automatic index maintenance; software proposal/admission with no per-sighting approval or expected-answer oracle. Rollback/recovery is rederivation from available records and replacement-key removal, not reverting a tested theory. The guidance is miner/judge code; persisted raw/judged evidence feeds later selection.

> if replaced[p.Key] || (live != nil && !live[p.Key]) {
> 			changed = true
> 			continue
> 		}
> --- `internal/index/fixpair.go`

> for _, s := range replacements {
> 		fresh := fixPairsIn(s.Messages, s.Harness+":"+s.ID, s.Project)
> 		changed = changed || len(fresh) > 0
> 		kept = append(kept, fresh...)
> 	}
> 	if changed {
> 		writeFixTables(tmp, kept)
> 	}
> --- `internal/index/fixpair.go`

#### EPI-RTE-fix-selection
Label: Historical remedy selection

Distinct from [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall)'s general retrieval route: `FixesFor` selects mined evidence tuples for CLI fix and other specific error consumers. Owner is fixed Go code; the caller/model owns any next action. Endpoints: error signatures plus allowed-origin predicate and table to bounded receipts. It filters remedies equal to the failure and recognized irreversible commands, enforces policy/ignore filters and selects confirmed pairs first. If none remains it returns held candidates. CLI `printFixPairs` labels those unconfirmed; edits render as changed files, not runnable commands. SRC-1, `internal/index/fixpair.go`, `cmd/deja/fix.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Matching confirmed receipts, otherwise eligible candidate receipts; CLI renders error/date and command or edited-file evidence.
- Later read-back: The table was derived from prior sessions; future error queries consume it, but this request does not update semantic truth status.
- Delegated visibility: CLI caller receives prose/JSON; MCP and automatic consumers have their own final framing/rendering paths, not assumed identical.
- Selection predicate: Error signature match, not same-as-failure or recognized irreversible remedy, caller allow predicate and ignored-project exclusion; confirmed-first, candidates only if no confirmed result.
- Invalidation or expiry: Table regeneration and policy/source changes alter future results; no permission or downstream action rollback is owned by this selector.
- Activation or effect: Enforcing output filters plus ranking and advisory historical evidence; caller may decline to execute, actual execution unobserved.
- Evidence limits: Unconfirmed fallback is not repair acceptance; irreversible-command helper coverage is bounded, and CLI presentation is not a tool permission gate.

Proposer is historical miner/table; decider/veto is selector code and then caller. No answer oracle. Mode: open requested error lookup and reuse by automatic consumers. Material countercase to the `Candidate` struct comment's “never served”: the implemented fallback returns candidate tuples, while `planRemedy` independently refuses one. Thus confirmation has consumer-specific force rather than a system-wide admission boundary.

> if len(out) == 0 {
> 		for _, p := range held {
> --- `internal/index/fixpair.go`

> ran = "ran next, unconfirmed"
> --- `cmd/deja/fix.go`

> if len(fixes) == 0 || fixes[0].Candidate {
> 		return ""
> 	}
> --- `cmd/deja/hook_plan.go`

#### EPI-RTE-plan-check
Label: Plan recurrence evidence

No supplied counterpart after comparison with [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall): this checks plan-step terms against recurring error carriers before a plan submission. Target/domain: historical recurring walls in eligible indexed sessions related to the supplied plan's informative terms. Evaluator/owner: Go `planFindings` and `PlanFrictionMatches`; not a model critic. The join starts from wall clusters and indexed plan terms, then hook code rechecks allowed carrier counts, suppresses repeated walls, optionally includes surviving command associations and a confirmed-only remedy. Result states how many sessions carried a wall, not that the plan must fail. SRC-1, `cmd/deja/hook_plan.go`, `internal/index/plan.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bounded wall-count findings, optional command census and confirmed remedy clause, or no finding.
- Later read-back: Earlier index walls/fix evidence reach this later request; evidence is not newly written by this check except delivery dedupe handled at the delivery route.
- Delegated visibility: Findings can reach the submitting host model or human CLI reader; no critic child launched.
- Selection predicate: Usable current undamaged snapshot, extractable plan steps, auto policy, own-session/delivery exclusions, minimum eligible wall carrier count and finding budget.
- Invalidation or expiry: No rebuild on the critical path; requests warmup on unreadable snapshots. Index and dedupe state change later findings.
- Activation or effect: Historical evidence checking is wired; predictive correctness, changed plans and causal benefit unobserved.
- Evidence limits: Exact join body beyond inspected setup remains uninspected; error recurrence is not logical plan validity or an epistemic decision-reversal criterion.

Plan caller proposes; fixed code decides findings, policy/dedupe can veto delivery; model/user decides revisions. No expected-answer oracle. Mode: open plan submission, not a bounded experiment. Empty check output may mean no steps, index unavailable, filters/dedupe or no match, not safe plan.

> wallSessions := filterPlanMetas(match.Wall.Sessions, keep, nil)
> 		if len(wallSessions) < index.FrictionMinSessions {
> 			continue
> 		}
> --- `cmd/deja/hook_plan.go`

> line := fmt.Sprintf("wall hit in %d sessions%s: %s", len(match.Wall.Sessions), since, wall)
> --- `cmd/deja/hook_plan.go`

#### EPI-RTE-plan-delivery
Label: Plan warning delivery

Distinct from [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery)'s selected startup/prompt/tool history: this is the `ExitPlanMode` PreToolUse check and its human-facing CLI counterpart. Owner: binary hook/output code; host owns plan submission and next inference/action. Hook emits framed `AdditionalContext`, not a deny decision. CLI `check -` prints findings or diagnostic miss explanations. SRC-1, `cmd/deja/hook_plan.go`, `cmd/deja/check.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: PreToolUse additional context, human findings/diagnostics, or silent hook miss.
- Later read-back: Delivery IDs are remembered per session and affect later eligible reminders; historical evidence remains independently queryable.
- Delegated visibility: Host receiving the hook controls onward visibility; no sub-agent launch or child authority is granted.
- Selection predicate: Recall not off, recognized ExitPlanMode, nonempty budgeted findings; CLI uses an empty session ID to skip session dedupe.
- Invalidation or expiry: Delivery ledger prevents repeats; ledger expiry details are not traced here. Miss may request warmup without blocking submission.
- Activation or effect: Advisory context is wired, not enforced plan acceptance/rejection; no observed revision or compliance.
- Evidence limits: A formatted warning is not guaranteed host receipt; all-host wiring and delivery-ledger durability remain uninspected.

Proposer is submitted plan; computational checks propose warning text; caller/model can revise or ignore it. No answer oracle and no inspected plan veto. Mode: automatic pre-submission warning or explicit check. Dedupe consumes results operationally even when no plan revision follows.

> resp.HookSpecificOutput.HookEventName = "PreToolUse"
> 	resp.HookSpecificOutput.AdditionalContext = frameRecall(strings.Join(lines, "\n"))
> --- `cmd/deja/hook_plan.go`

> if sessionID != "" {
> 		rememberPlanFindings(dir, sessionID, findings)
> 	}
> --- `cmd/deja/hook_plan.go`

#### EPI-RTE-offline-scores
Label: Offline evidence measures

Distinct from [RT-RTE-retrieval-evaluation](runtime.md#rt-rte-retrieval-evaluation)'s gold-session rank: planbench counts emitted warnings per plan and distinct wall labels; `contextCoverage` counts supplied literal fact strings present in rendered text. These independent evaluator targets are grouped only by reporting force, not semantic equivalence. Owners: offline Go drivers. Endpoints: supplied plans through `check`, or text/fact list through substring scoring, to counts/coverage reports. SRC-1, `scripts/planbench/main.go`, `cmd/deja/bench_context.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Plan fire/finding/wall counts, or fraction of literal fact strings present in output.
- Later read-back: inapplicable — no inspected automatic production consumer adopts these scores; any maintainer interpretation is outside the inspected score path.
- Delegated visibility: inapplicable — inspected scorers launch no model critic or child inference.
- Selection predicate: Plan files/check findings for census; supplied fact strings and text for coverage.
- Invalidation or expiry: New input/rendered output changes counts; no claim that dataset or report versions are independently frozen.
- Activation or effect: Reporting only; no inspected acceptance/rejection gate for product, rules or knowledge.
- Evidence limits: Fire rate is not warning precision, substring presence is not entailment or correctness, and no execution/comparison evidence is used here.

Mode: bounded offline evaluation. Inputs propose test cases; code computes scores; human interpretation/change admission is external. The coverage scorer's reference is the supplied list of literal facts, not a world-truth oracle. Plan census has no correctness oracle. These targets do not establish causal component benefit even if numbers are later reported.

> findings += len(r.findings)
> --- `scripts/planbench/main.go`

> for _, fact := range facts {
> 		if strings.Contains(text, fact) {
> 			covered++
> 		}
> 	}
> --- `cmd/deja/bench_context.go`

### Claims

#### EPI-CLM-knows-held
Label: Recorded decision validity awareness

Claimed operation: public highlight says deja knows what held, using rejected/accepted promotion and later-hit state explanation. This is narrower/different from [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit)'s requested model workflow, not a duplicate claim. Source: SRC-1, `README.md`, doctrine/design. Implementation supports recording current caller state and convention eligibility. Marker alone need not supply why the decision failed, and no independent evaluator proves it held.

> - **Knows what held.** `deja promote <id> --state rejected` marks a reverted decision, and every later hit says it was tried and why it was dropped; `--state accepted` takes the mark back.
> --- `README.md`

#### EPI-CLM-history-judgement
Label: Historical judgment and remedy guidance

Claimed operation: MCP fix describes what this machine ran after the same error; result markers are characterized as the user's later judgment with a request to act on them. Distinct from [RT-CLM-search-before-edit](runtime.md#rt-clm-search-before-edit)'s search/remember prescription. Source: SRC-1, `cmd/deja/mcp.go`, doctrine/design in an implemented tool schema. Historical receipt guidance is supported; human authorship of each mark and causal repair are not established by API caller identity or sequence checks.

> "- fix: you just hit an error — what this machine ran after that same error. Pass the output verbatim.\n" +
> --- `cmd/deja/mcp.go`

> "A bracketed marker on a result is the user's own later judgement; act on what it says. " +
> --- `cmd/deja/mcp.go`
