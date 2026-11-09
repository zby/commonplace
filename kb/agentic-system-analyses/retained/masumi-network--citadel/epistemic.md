---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Citadel epistemic routes: untrusted source memory, optional text generation, bounded evaluators and operational admission."
run-id: AAS-2026-11-09-citadel-de4383eefa4e-01
reviewed-boundary: "749a24014a6cef59499dbe13b6fb4c348f8044a4"
---

# Citadel epistemic report

## Source-and-claim boundary

Question: which Citadel routes acquire or produce truth-apt engineering material, what checks license reliance, and which consumers actually receive their results? The frozen whole-system scope, exclusions and SRC-1 identity are those of the [boundary and Source register](boundary.md#source-register). All direct source reads below are at that revision (checkout HEAD checked). No target execution occurred. No observed-run or causal-experiment evidence was supplied.

The assessment distinguishes source capture, operational admission, searchable projection, shared-scope promotion and semantic acceptance. The first four can operate without the fifth. The target's own untrusted-context contract is a countercase to treating every use of “knowledge,” “learning” or “verify” as a factual warranty. Public/design claims are [EPI-CLM-context-links](#epi-clm-context-links), [EPI-CLM-promotion-gate](#epi-clm-promotion-gate), [EPI-CLM-preserve-source](#epi-clm-preserve-source), [EPI-CLM-benchmark-score](#epi-clm-benchmark-score) and [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval).

### Coverage

“Supplied” means the runtime's inspected findings, not an independent read here. “Direct” means source inspected for this member. Available but uninspected operations remain limits; no system-complete negative follows.

| Entry point or operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| Python CLI dispatch: ingest/search/local, capture, promotion, feedback, verify, bench, improve/cognify/reindex/learn/sync | `kb/cli.py` | Direct dispatch inventory, verify and maintenance handlers; supplied [RT-RTE-local-access](runtime.md#rt-rte-local-access), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission). User improve/cognify and applying reindex are scheduled-only refusals, not hidden user model evaluators. |
| Registered MCP tools and prompts | `kb/mcp_server.py` | Direct registry/handler inventory, improve refusal and promotion review; supplied [RT-RTE-task-search](runtime.md#rt-rte-task-search), [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review). Share-session/contribute, reconciliation, backup and connector internals not fully traced here; prevents an exhaustive admission/warrant conclusion for all tools. |
| UserPromptSubmit / SessionEnd | `kb/hooks/search_inject.py`, `kb/hooks/sync_session.py`, `kb/session_trace_distill.py` | Supplied [RT-RTE-task-search](runtime.md#rt-rte-task-search), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture); direct [EPI-RTE-note-distill](#epi-rte-note-distill). Full shared trace refinement and git pre-push path not independently inspected; prevents a universal capture-fidelity judgment. |
| HTTP ingest / service / scheduled projection | `kb/server.py`, `kb/service.py`, `kb/learning.py`, `kb/lifecycle_worker.py` | Supplied [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [RT-RTE-source-projection](runtime.md#rt-rte-source-projection); direct enrichment, feedback, improvement, tombstone/filter, conflict call sites and cleanup. Provider graph extraction not inspectable as repository implementation. |
| Optional enrichment and optimization | `kb/llm_enrichment.py`, `kb/self_improve.py` | Direct [EPI-RTE-source-enrichment](#epi-rte-source-enrichment); supplied [RT-RTE-index-curation](runtime.md#rt-rte-index-curation). Source preservation is requested but not parser-enforced. |
| Promotion classification, approve/reject | `kb/promotion.py`, `kb/mcp_server.py` | Supplied [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review); direct MCP approve/reject contracts. Review can veto pending items but does not cover all automatic promotions. |
| Feedback and automated improvement | `kb/service.py`, `kb/improvement_policy.py` | Direct [EPI-RTE-feedback-record](#epi-rte-feedback-record), [EPI-RTE-automation-receipt](#epi-rte-automation-receipt); receipt fields inspected, issuer measurements uninspected. |
| LearningAgent organization updates | `kb/learning_agent.py`, `kb/organization_digest.py` | Direct [EPI-RTE-digest-build](#epi-rte-digest-build); source-sync result and vault-context inputs, preview and gateway post. External source truth and delivered notifications unobserved. |
| Verify / prepare-pr-context | `kb/agent_workflows.py`, `kb/cli.py` | Direct verify shaping [EPI-RTE-verify-report](#epi-rte-verify-report); prepare-pr-context handler inventoried but shaping not fully assessed. Prevents a complete assertion about every source-ranking rule. |
| Conflict warning/resolution | `kb/conflicts.py`, `kb/learning.py` | Direct [EPI-RTE-conflict-record](#epi-rte-conflict-record); title/hash differences and status-only resolution, not semantic contradiction adjudication. Other UI conflict consumers unassessed. |
| Cleanup, source withdrawal and corpus repair | `kb/service.py`, `kb/server.py` | Direct [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup), [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal); repair previews/guards inventoried, full repair transactions uninspected. Prevents universal rollback/erasure guarantee. |
| Retrieval benchmark run/score/enforce | `kb/retrieval_eval.py` | Direct scoring, comparison, release gate and command exit excerpts: [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate). No supplied benchmark run; no independently authenticated result. |
| Browser, Obsidian, connector imports, skills | `web/src/pages/app/search.tsx`, `plugins/obsidian-citadel/src/sync/syncEngine.ts`, `skills/citadel/SKILL.md` | Boundary/supplied coverage only. Detailed client transformations and all sync reconciliation not independently checked here; prevents whole-system fidelity and host-compliance claims. |

Missing private corpus and paired source/output instances prevent testing factual fidelity of generated notes and digests. Missing provider internals prevent classifying graph extraction/improve semantics and parameter changes beyond the supplied component bounds. Missing receipt-issuer evidence prevents treating its five Boolean assertions as verified measurements. Missing consumer traces prevent establishing activation; missing interventions prevent benefit or component-effect attribution. These are different gaps, not one negative verdict.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-node-note](#epi-obj-node-note) | see record | see record | SRC-1 `kb/session_trace_distill.py` | selected transcript assertions, not confirmed outcomes |
| [EPI-OBJ-enriched-chunk](#epi-obj-enriched-chunk) | see record | see record | SRC-1 `kb/llm_enrichment.py` | semantic preservation unknown |
| [EPI-OBJ-organization-digest](#epi-obj-organization-digest) | see record | see record | SRC-1 `kb/organization_digest.py` | source-linked intent does not validate generated interpretation |
| [EPI-OBJ-conflict-record](#epi-obj-conflict-record) | see record | see record | SRC-1 `kb/conflicts.py` | hash difference is not contradiction |
| [EPI-OBJ-evaluation-gate](#epi-obj-evaluation-gate) | see record | see record | SRC-1 `kb/improvement_policy.py` | issuer's proof not loaded |
| [EPI-OBJ-benchmark-run](#epi-obj-benchmark-run) | see record | see record | SRC-1 `kb/retrieval_eval.py` | expected body spans are an oracle for return, not world truth |
| [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result) | none beyond operational receipt assertions; see record | see record | SRC-1 `kb/service.py` | admission/searchability is not truth acceptance |
| [RT-OBJ-optimize-prompt](runtime.md#rt-obj-optimize-prompt) | policy input, not output evidence; see record | see record | SRC-1 `kb/self_improve.py` | requests no invention; output fidelity unobserved |

Other material parts are located by routes rather than given duplicate objects: imported source bytes and projections ([RT-RTE-source-projection](runtime.md#rt-rte-source-projection)), classified promotion candidate ([RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review)), optimization notes ([RT-RTE-index-curation](runtime.md#rt-rte-index-curation)), retrieval page ([RT-RTE-task-search](runtime.md#rt-rte-task-search)) and ratings ([EPI-RTE-feedback-record](#epi-rte-feedback-record)). Chat, decision, embedding and Cognee numerical model state stay separate: see [RT-CMP-openrouter-chat](runtime.md#rt-cmp-openrouter-chat), [RT-CMP-promotion-decision](runtime.md#rt-cmp-promotion-decision), [RT-CMP-embedding-profile](runtime.md#rt-cmp-embedding-profile), [RT-CMP-cognee-models](runtime.md#rt-cmp-cognee-models). No weight-training conclusion follows from retained note updates.

## Authority-route ledger

Each row is one function; repeated citations split checks from disposition or retention. Architectural status is implementation status, not evidence of exercise. Other canonical fields are in the cited records. No supplied record requires supersession: new declarations name distinct routes or explicit parts.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority | behavioral-authority path | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | content transformation | implemented | caller source | truth-apt transformation: acquisition/import | source enters store | authenticated routing/content guards | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | permissive | source warrant unknown; no truth attestation | capture permitted | learning/store; request; permissive; later searches | SRC-1 `kb/service.py` | none | none | receipt means operational admission |
| [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | disposition/acceptance | implemented | [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result) | no content change | write eligibility | scope, scanner, chunk guards | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | see [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | enforcing | not evidence-consuming semantic acceptance | reject or retain source | server to store; enforcing; this write | SRC-1 `kb/learning.py` | [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval) | approval policy not universal | direct/local and automatic routes differ |
| [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) | retention | implemented | source bytes/projections | no content change | retain/reload accepted source | store/worker | see [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) | see [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) | enforcing | retention not endorsement | source available later | store to worker/search; later requests | SRC-1 `kb/lifecycle_worker.py` | none | none | graph semantic transformation is separately opaque |
| [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) | check/evidence production | implemented | projection receipts | no content change | backend visibility/chunk presence | worker read checks in backend domain | see [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) | see [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) | enforcing | projection availability only | mark/search current binding | worker receipt to retrieval filter; enforcing; revision lifetime | SRC-1 `kb/lifecycle_worker.py` | none | none | not factual or complete-recall test |
| [RT-RTE-task-search](runtime.md#rt-rte-task-search) | operational admission/selection/consumption | implemented | retrieval page | no content change | selected source context | scope/ranking/current binding and caps | see [RT-RTE-task-search](runtime.md#rt-rte-task-search) | see [RT-RTE-task-search](runtime.md#rt-rte-task-search) | ranking | untrusted/reference context | deliver bounded descriptions | see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) | SRC-1 `kb/hooks/search_inject.py` | [EPI-CLM-context-links](#epi-clm-context-links) | none | delivery not compliance |
| [EPI-RTE-note-distill](#epi-rte-note-distill) | content transformation | implemented | [EPI-OBJ-node-note](#epi-obj-node-note) | truth-apt transformation: indeterminate | transcript to Outcome/Files changed | deterministic selection, no result-success validation | see [EPI-RTE-note-distill](#epi-rte-note-distill) | see [EPI-RTE-note-distill](#epi-rte-note-distill) | permissive | retains attributed assertions with weakened context | note offered for automatic capture | hook note to ingest; permissive; later personal search | SRC-1 `kb/session_trace_distill.py` | none | outcome/effect labels exceed checked evidence | could reshape or strengthen claims; concrete deduction below |
| [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | content transformation | implemented | [EPI-OBJ-enriched-chunk](#epi-obj-enriched-chunk) | truth-apt transformation: indeterminate | source to generated chunks/summary | model prompt, optional path | see [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | see [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | permissive | preservation requested, not established | generated text can replace ingest input | model → learning chunks → source store; later search | SRC-1 `kb/llm_enrichment.py` | [EPI-CLM-preserve-source](#epi-clm-preserve-source) | semantic-fidelity gap | passthrough/paragraph fallback are non-ampliative reshaping |
| [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | check/evidence production | implemented | [EPI-OBJ-enriched-chunk](#epi-obj-enriched-chunk) | no content change | model JSON shape | parser types, nonempty text and caps | see [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | see [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | enforcing | syntax/shape only | malformed entries skipped; empty result falls back | parser → learning; enforcing; one call | SRC-1 `kb/llm_enrichment.py` | [EPI-CLM-preserve-source](#epi-clm-preserve-source) | no preservation comparison | valid JSON may omit/rewrite source |
| [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | check/evidence production | implemented | seat candidate | no content change | org relevance/sensitivity | typed model or chat plus org reference | see [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | see [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | advisory | bounded classifier judgment, no truth oracle | supply score/reason to engine | model → threshold code; one candidate | SRC-1 `kb/promotion.py` | [EPI-CLM-promotion-gate](#epi-clm-promotion-gate) | none | accuracy unobserved |
| [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | disposition/acceptance | implemented | seat candidate | no content change | shared-scope eligibility | fixed score/rules or pending reviewer | see [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | see [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | enforcing | intended org sharing eligibility, not factual acceptance | known-work auto-share; new-project queue/reject | engine/reviewer → Central writes; permissive; future shared reads | SRC-1 `kb/promotion.py` | [EPI-CLM-promotion-gate](#epi-clm-promotion-gate) | universal explicit-step reading too strong | rejected hash veto is bounded to candidate |
| [RT-RTE-index-curation](runtime.md#rt-rte-index-curation) | content transformation | implemented | optimization note | truth-apt transformation: indeterminate | labels/tags to summaries/tags | chat proposer and known-label parser | see [RT-RTE-index-curation](runtime.md#rt-rte-index-curation) | see [RT-RTE-index-curation](runtime.md#rt-rte-index-curation) | permissive | no checked source-body entailment | admit notes after guards, not semantic acceptance | see [RT-BAP-curation-guidance](runtime.md#rt-bap-curation-guidance) | SRC-1 `kb/self_improve.py` | none | name does not establish improvement | improve dependency separate and opaque |
| [EPI-RTE-feedback-record](#epi-rte-feedback-record) | retention | implemented | rating/event/note | truth-apt transformation: acquisition/import | caller rating | caller judgment, cache/fallback | see [EPI-RTE-feedback-record](#epi-rte-feedback-record) | see [EPI-RTE-feedback-record](#epi-rte-feedback-record) | permissive | attributed judgment only; source warrant unknown | retain searchable rating; optional gated improve | caller → feedback store/cache/note; later consumers | SRC-1 `kb/service.py` | none | none | no raw feedback-to-optimization-prompt link established |
| [EPI-RTE-automation-receipt](#epi-rte-automation-receipt) | check/evidence production | implemented | [EPI-OBJ-evaluation-gate](#epi-obj-evaluation-gate) | no content change | receipt completeness/currency | JSON/timestamps/five booleans | see [EPI-RTE-automation-receipt](#epi-rte-automation-receipt) | see [EPI-RTE-automation-receipt](#epi-rte-automation-receipt) | enforcing | asserted measurement status only | gate computes allow/deny | receipt reader → require function; current call | SRC-1 `kb/improvement_policy.py` | none | measurement vs attestation gap | issuer evidence uninspected |
| [EPI-RTE-automation-receipt](#epi-rte-automation-receipt) | operational admission/selection/consumption | implemented | [EPI-OBJ-evaluation-gate](#epi-obj-evaluation-gate) | no content change | automated improve permission | require + Central scope | see [EPI-RTE-automation-receipt](#epi-rte-automation-receipt) | see [EPI-RTE-automation-receipt](#epi-rte-automation-receipt) | enforcing | no claim-level license | exception blocks or permits Cognee call | service → gateway; enforcing; until receipt expires | SRC-1 `kb/improvement_policy.py` | none | none | direct nonautomation service call differs |
| [EPI-RTE-digest-build](#epi-rte-digest-build) | content transformation | implemented | [EPI-OBJ-organization-digest](#epi-obj-organization-digest) | truth-apt transformation: indeterminate | source packet to interpretation | optional model or deterministic rules | see [EPI-RTE-digest-build](#epi-rte-digest-build) | see [EPI-RTE-digest-build](#epi-rte-digest-build) | advisory | not accepted factual analysis | produce preview text | builder → LearningAgent; advisory; one report | SRC-1 `kb/organization_digest.py` | none | none | need paired output to resolve entailment or conjecture |
| [EPI-RTE-digest-build](#epi-rte-digest-build) | operational admission/selection/consumption | implemented | [EPI-OBJ-organization-digest](#epi-obj-organization-digest) | no content change | notification eligibility | post flag, dry_run, enabled/meaningful predicates | see [EPI-RTE-digest-build](#epi-rte-digest-build) | see [EPI-RTE-digest-build](#epi-rte-digest-build) | permissive | notification not acceptance | post formatted text or preview only | LearningAgent → gateway/recipient; advisory; notification | SRC-1 `kb/learning_agent.py` | none | none | no recipient reliance trace |
| [EPI-RTE-conflict-record](#epi-rte-conflict-record) | check/evidence production | implemented | [EPI-OBJ-conflict-record](#epi-obj-conflict-record) | no content change | same title/path, different hash | two local caches; deterministic | see [EPI-RTE-conflict-record](#epi-rte-conflict-record) | see [EPI-RTE-conflict-record](#epi-rte-conflict-record) | advisory | content difference only | warn after source accepted | detector → store/mesh; advisory; later review | SRC-1 `kb/conflicts.py` | none | disagreement language stronger than hash test | cannot locate proposition contradiction |
| [EPI-RTE-conflict-record](#epi-rte-conflict-record) | retention | implemented | [EPI-OBJ-conflict-record](#epi-obj-conflict-record) | no content change | warning/status record | store record/resolve/prune | see [EPI-RTE-conflict-record](#epi-rte-conflict-record) | see [EPI-RTE-conflict-record](#epi-rte-conflict-record) | permissive | retains allegation, no truth settlement | open or resolved warning state | JSON → list/get; advisory; across invocations | SRC-1 `kb/conflicts.py` | none | none | resolve does not revise source here |
| [EPI-RTE-verify-report](#epi-rte-verify-report) | check/evidence production | implemented | local file and hits | no content change | lexical overlap/doc shape | cue matching and doc_type rules | see [EPI-RTE-verify-report](#epi-rte-verify-report) | see [EPI-RTE-verify-report](#epi-rte-verify-report) | advisory | pointers only | emit report, including incomplete searches | CLI → stdout human/agent; advisory; current task | SRC-1 `kb/agent_workflows.py` | none | verify is not truth validation | ok/exit zero can coexist with timeout |
| [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | check/evidence production | implemented | [EPI-OBJ-benchmark-run](#epi-obj-benchmark-run) | truth-apt transformation: entailed derivation | served body spans/identity | fixed matching/scoring over supplied inputs | see [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | see [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | advisory | conditional on artifact/oracle fidelity; retrieval domain | produce bounded metrics | scorer → run artifact/comparator; one benchmark | SRC-1 `kb/retrieval_eval.py` | [EPI-CLM-benchmark-score](#epi-clm-benchmark-score) | none | not correctness of matched assertions |
| [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | disposition/acceptance | implemented | [EPI-OBJ-benchmark-run](#epi-obj-benchmark-run) | no content change | candidate benchmark comparison | fingerprints, required evidence, nonregression; release extras | see [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | see [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | enforcing | bounded evidence-consuming benchmark decision | exit pass/fail; no automatic vault deployment shown | comparator → CLI exit → invoking shell; enforcing for command only | SRC-1 `kb/retrieval_eval.py` | [EPI-CLM-benchmark-score](#epi-clm-benchmark-score) | none | no authenticated supplied run or causal design |
| [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup) | check/evidence production | implemented | legacy candidate IDs | no content change | known scaffolds/fossils | deterministic classifier and bounded probes | see [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup) | see [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup) | advisory | shape-class membership, not falsity | preview candidate IDs/counts | service → admin preview; advisory; maintenance request | SRC-1 `kb/service.py` | none | none | probe coverage and false positives not measured |
| [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup) | disposition/acceptance | implemented | legacy candidate IDs | no content change | deletion eligibility | admin sources:sync and non-dry-run | see [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup) | see [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup) | enforcing | no semantic rejection claim | invoke gateway delete | admin/code → gateway; enforcing; later availability | SRC-1 `kb/server.py` | none | none | physical purge/rollback unestablished |
| [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal) | lineage/freshness/recovery | implemented | source revision/binding | no content change | current-head eligibility | tombstone admission/filter | see [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal) | see [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal) | enforcing | withdrawn not necessarily false | exclude old/tombstone lifecycle-bound hits | store → retrieval filter; enforcing; future lifecycle reads | SRC-1 `kb/service.py` | none | none | does not retract already emitted context or cover all branches |

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-context-links](#epi-clm-context-links) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-task-search](runtime.md#rt-rte-task-search), [EPI-RTE-verify-report](#epi-rte-verify-report) | none supplied | no recipient trace or intervention | source pointers and explicit untrusted-use policy, not source attestation | complete client/provenance fidelity not audited |
| [EPI-CLM-promotion-gate](#epi-clm-promotion-gate) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | none supplied | no classifier accuracy or reviewer trace | deliberate eligibility gate implemented | not every Central write waits for human explicit step |
| [EPI-CLM-preserve-source](#epi-clm-preserve-source) | see record | SRC-1 `kb/llm_enrichment.py`; doctrine/design prompt | see record | [EPI-RTE-source-enrichment](#epi-rte-source-enrichment) | none supplied | no source/output pair | shape validated; complete source preservation only requested | cap/nonempty parsing does not compare source text |
| [EPI-CLM-benchmark-score](#epi-clm-benchmark-score) | see record | SRC-1 `README.md`; reported operation | bounded metric and explicit corpus limitations | [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate) | attributed README only, not inspectable run | no intervention or component variation | implemented metric is meaningful for body-span return within declared corpus/question scope | reported value not reproduced or authenticated |
| [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval) | see record | SRC-1 `kb/mcp_server.py`; doctrine/design | see record | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review) | none supplied | no host compliance evidence | policy for named tool invocation | automatic writes refute universal approval invariant |

## Bounded conclusion

Citadel acquires engineering source content and caller ratings, retains them, projects selected content and returns bounded context. Operational admission and backend receipt checks authorize storage/searchability, not belief in the content. Source warrant remains unknown: commit/document pointers help a recipient check a source but do not attest source truth. Lifecycle binding can exclude obsolete content; it is not endorsement. See [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [RT-RTE-source-projection](runtime.md#rt-rte-source-projection), [RT-RTE-task-search](runtime.md#rt-rte-task-search), [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal).

The deterministic session note needs special care. A source-supported counterexample to “it simply preserves known outcomes” is an assistant block saying “Deployment succeeded” followed by a Write tool_use for `config.py` whose tool_result reports an error. Inspected code keeps last assistant text as “Outcome” and collects the file path from tool_use without inspecting tool_result in distill_node_note. Thus it can emit “Outcome: Deployment succeeded” and list `config.py` under “Files changed” even with a failed tool result. This is a deduction from implementation, not an executed fixture. It establishes neither deployment nor file mutation. More generally the note is an indeterminate transformation: some inputs merely lose detail; others strengthen an action attempt into an apparent effect. This countercase does not show all notes are false. See [EPI-RTE-note-distill](#epi-rte-note-distill).

Optional generated chunks, summaries, optimization notes and digest interpretations are candidates, not established accepted ampliative claims. The parsers check output shape, count or known labels, not semantic entailment. “Never invent” is model guidance. Without input/output instances, non-entailment is not established either, so these routes remain indeterminate rather than automatically “ampliative.” Passthrough/paragraph fallback is non-ampliative reshaping within its text domain. The digest notification path is distinct from retained optimization notes: it can publish interpretation without any claim-level acceptance step in the inspected driver. See [EPI-RTE-source-enrichment](#epi-rte-source-enrichment), [RT-RTE-index-curation](runtime.md#rt-rte-index-curation), [EPI-RTE-digest-build](#epi-rte-digest-build).

There are real bounded evaluators. Promotion judges organizational relevance/sensitivity for sharing; the engine threshold or authorized pending-item reviewer can admit/reject shared copies. Conflict detection finds title/hash differences after admission; a resolved conflict record does not revise the content. CLI verify provides lexical/source-shape pointers and explicitly delegates live-source confirmation. Garbage cleanup classifies known scaffolds and permits deletion, not epistemic refutation. Each has a different target, intended use and authority horizon. None licenses arbitrary factual reliance. See [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review), [EPI-RTE-conflict-record](#epi-rte-conflict-record), [EPI-RTE-verify-report](#epi-rte-verify-report), [EPI-RTE-garbage-cleanup](#epi-rte-garbage-cleanup).

The benchmark is an evidence-producing retrieval evaluator with a separate evidence-consuming acceptance command. Its formal derivations warrant only what follows from the supplied hits, expected spans/identities and comparison artifacts under those algorithms. A body-span match does not establish that the span is true; an unexpected document can quote it. Enforcement can fail the invoking command, including for missing/noncomparable artifacts and regressions, but a downstream release/deployment gate was not established by this inspection. The automation receipt reader is a different enforcement path: it licenses an automated Central improve call until expiry on asserted check fields, without replaying those checks. Neither is a per-proposition factual acceptance gate. See [EPI-RTE-benchmark-gate](#epi-rte-benchmark-gate), [EPI-RTE-automation-receipt](#epi-rte-automation-receipt).

No inspected route establishes lifecycle integration *after semantic acceptance* of a produced ampliative claim. This is not a system-complete absence: the coverage table's unassessed paths and opaque Cognee processing limit it. Retention, promotion and use can occur before any such acceptance. Feedback and optimization notes can affect later material, but learning as improved capacity, formulated content-directed theory criticism, reflection, autonomy and self-improvement require independent evidence. Here actual later exercise and benefit are unobserved; raw feedback retention does not by itself establish any of them. The direct opaque improve call is not evidence of absent learning, nor does its name establish it. Distributed model mutability remains exactly as bounded by the four supplied component records. There is no single epistemic score or whole-system verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-node-note
Label: Dev session note

Natural-language Markdown string, assembled in Python and subsequently stored as source content after capture admission. Candidate propositions concern task, claimed outcome, decisions and files. Distinct from the symbolic receipt [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result); no supplied object counterpart. Route: [EPI-RTE-note-distill](#epi-rte-note-distill). SRC-1 `kb/session_trace_distill.py`.

> lines: list[str] = ["# Dev session note"]
> --- `kb/session_trace_distill.py`

#### EPI-OBJ-enriched-chunk
Label: EnrichedChunk

Natural-language text/summary and symbolic tag tuple, first in Python/model JSON then source ingestion input. Distinct from [RT-OBJ-optimize-prompt](runtime.md#rt-obj-optimize-prompt): source enrichment output rather than static curation guidance. Truth-apt content includes source assertions and generated summary. Route: [EPI-RTE-source-enrichment](#epi-rte-source-enrichment). SRC-1 `kb/llm_enrichment.py`.

> summary=_clean_summary(entry.get("summary")),
> tags=_clean_tags(entry.get("tags")),
> --- `kb/llm_enrichment.py`

#### EPI-OBJ-organization-digest
Label: Organization update digest

Natural-language formatted text plus symbolic summary/source-label fields in Python return payload, optionally notification transport. Contains source update assertions and interpretation. Distinct from optimization note in [RT-RTE-index-curation](runtime.md#rt-rte-index-curation); no supplied object counterpart. SRC-1 `kb/organization_digest.py`.

> payload["_text"] = text
> --- `kb/organization_digest.py`

#### EPI-OBJ-conflict-record
Label: KnowledgeConflictStore record

Mixed natural-language summary/excerpts and symbolic IDs/status/hash-derived deduplication keys in persistent JSON. Candidate disagreement allegation and preferred-source instruction must be distinguished from measured hash difference. No supplied counterpart after comparison with [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result). SRC-1 `kb/conflicts.py`.

> "status": RESOLVED,
> "resolution_note": clip_excerpt(resolution_note),
> --- `kb/conflicts.py`

#### EPI-OBJ-evaluation-gate
Label: Central evaluation receipt

Symbolic local JSON fields interpreted by fixed code; natural-language run_id is an identifier, not proof. Status/check assertions are truth-apt about a purported evaluation, while their operative role is permission. Distinct from projection acceptance receipt [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result). SRC-1 `kb/improvement_policy.py`.

> path = Path(getattr(config, "evaluation_gate_path", ".citadel/evaluation_gate.json"))
> --- `kb/improvement_policy.py`

#### EPI-OBJ-benchmark-run
Label: Retrieval benchmark artifact

Symbolic question/hit/score/run/fingerprint JSON consumed by Python comparator, with natural-language answer spans and source text. Metrics assert bounded retrieval outcomes. No counterpart after comparison with projection receipt [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result); this is a saved benchmark-run object, not a captured observed run supplied to this analysis. SRC-1 `kb/retrieval_eval.py`.

> baseline = json.loads(Path(args.run_a).read_text(encoding="utf-8"))
> candidate = json.loads(Path(args.run_b).read_text(encoding="utf-8"))
> --- `kb/retrieval_eval.py`

### Routes

#### EPI-RTE-note-distill
Label: Node note extraction

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)
This is its deterministic content-producing subroute, not the transport/admission container.

Endpoints/progression: transcript entries → distill_node_note → note string → SessionEnd capture. Owner/proposer/decider: deterministic code chooses assistant text, tool paths and decision-marker matches. Context: transcript only; effect: creates a candidate recap. No human or model check is performed here. SRC-1 `kb/session_trace_distill.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: note text or empty string
- Later read-back: admitted note can be retrieved in later sessions through the parent route
- Delegated visibility: capture server sees selected note, not complete transcript
- Selection predicate: first prompt, last assistant text, assistant decision-marker matches and edit/write tool paths, with count/length caps
- Invalidation or expiry: inapplicable — extraction has no retained state; retained note follows downstream revision rules
- Activation or effect: labels assistant text as Outcome and tool-use paths as Files changed; these are not checked against successful results
- Evidence limits: deduced from implementation, no supplied transcript instance or successful file-effect trace

> recap_bits.append(f"Outcome: {_truncate(last_assistant_text, 280)}")
> --- `kb/session_trace_distill.py`

#### EPI-RTE-source-enrichment
Label: Optional source enrichment

Distinct from [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission): this is the optional direct-learning generative transformation, which the inspected HTTP admission suppresses.

Endpoints/progression: enrich_source_material → chat with source text → parse_enriched_chunks → LearningProcess._chunk_inputs → ingest. Owner: learning code; model proposes text, summary and tags; parser rejects malformed entries, ingestion guards can veto individual writes. Mode: optional source processing, not an answer-key experiment. Oracle: none. Guidance requests unchanged wording and complete coverage; implementation validates shape, not those semantic properties. Proposed change: searchable chunk text and metadata, not model weights. Failure selects passthrough or paragraph fallback; no semantic rollback after valid but inaccurate JSON is established. SRC-1 `kb/llm_enrichment.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: EnrichmentOutcome with chunks, used_llm and reason
- Later read-back: accepted generated chunk text and summaries can reach later searches
- Delegated visibility: remote chat receives source text when enabled, above threshold, unflagged and keyed; HTTP/light/shared paths suppress this
- Selection predicate: enrichment enablement, size threshold, scanner, API key; parser accepts nonempty text entries up to MAX_CHUNKS
- Invalidation or expiry: uninspected — no semantic expiry of accepted chunks established; source-key revision rules apply
- Activation or effect: model text becomes ingestion input; no equality or source-coverage check in inspected parser
- Evidence limits: indeterminate semantic relation without concrete input/output; dependency graph extraction remains opaque

> text = entry.get("text")
> if not isinstance(text, str) or not text.strip():
>     continue
> --- `kb/llm_enrichment.py`

#### EPI-RTE-digest-build
Label: Organization digest read

No counterpart after comparison with [RT-RTE-index-curation](runtime.md#rt-rte-index-curation): digest output is a separate notification product, not the optimization-note write. Uses the same provider family as [RT-CMP-openrouter-chat](runtime.md#rt-cmp-openrouter-chat), with its own request helper and route configuration.

Endpoints/progression: LearningAgent source-sync results plus recent vault context → capped source packet → optional llm_agent_read or deterministic_agent_read → formatted digest → preview/notification routing. Owner: LearningAgent and digest code. Model proposes up to three interpretation lines; code accepts nonempty lines, with no source-entailment validator. Mode: source-update report. Oracle: none. Private-source policy can block model use; disabled/unusable model falls back. Output is not shown ingested as an accepted knowledge claim by this driver. SRC-1 `kb/organization_digest.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: digest preview, source label, summary and internal formatted text
- Later read-back: inapplicable — inspected driver returns/posts this digest rather than storing it for Citadel read-back
- Delegated visibility: model receives selected source packet; gateway receives formatted digest, not whole source corpus
- Selection predicate: enabled digest, meaningful change predicate; allow_llm, private metadata policy and key; response capped at three lines
- Invalidation or expiry: inapplicable — no persisted digest lifecycle in this inspected driver
- Activation or effect: preview delivery and optional gateway post are wired; actual notification and reliance unobserved
- Evidence limits: no model response or recipient trace; deterministic and generative interpretation cannot be given one entailment classification

> for raw_line in message.splitlines():
>     line = raw_line.strip().lstrip("-* ").strip()
>     if line:
>         lines.append(line)
> return lines[:3] or None
> --- `kb/organization_digest.py`

#### EPI-RTE-conflict-record
Label: Contribution conflict detection

Distinct post-admission check adjacent to [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission); it neither replaces that gate nor evaluates proposition truth.

Endpoints/progression: accepted contribution → title extraction/hash comparison against local GitHub digest or Obsidian sync state → ConflictCandidate → KnowledgeConflictStore JSON → optional mesh record. Owner: code; no human judgment in detection. Target/domain: title/path correspondence and byte-hash difference in those two caches. Mode: automatic after accepted_any when detect_conflicts is set. No answer oracle. Store resolve changes conflict status/note, not source content in inspected implementation. Guidance prefers newer repository material in one generated message, although hash difference alone cannot warrant that preference. SRC-1 `kb/learning.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: conflict record or None in LearningOutcome
- Later read-back: JSON conflict list/get and mesh record expose retained warning; bounded max_records pruning prefers retaining open records
- Delegated visibility: stored excerpts, hashes and summary, not necessarily full compared sources
- Selection predicate: nontrivial first-line title; case-folded title/path match and different hashes in two local sync caches
- Invalidation or expiry: resolved conflicts pruned before open ones; resolve records note and actor without retracting either source here
- Activation or effect: warning is recorded after admission; no ingestion veto or automatic source-truth correction in inspected sequence
- Evidence limits: hash inequality is not contradiction; full consumer/UI conflict resolution outside inspected methods remains unassessed

> conflict = None
> if detect_conflicts and accepted_any:
>     conflict = self._detect_conflict(data)
>     if conflict and self.mesh:
>         await self.mesh.record_conflict(self.config, conflict=conflict)
> --- `kb/learning.py`

#### EPI-RTE-verify-report
Label: CLI verify pointers

No counterpart after comparison with [RT-RTE-task-search](runtime.md#rt-rte-task-search): this consumer adds a local file cue comparison and advisory verification report, rather than hook context.

Endpoints/progression: CLI verify local file → supplied or built query → HTTP search → shape_verify_report → doc-shaped source list, lexical overlaps and warnings → JSON stdout. Owner: CLI and shaping code. Target/domain: token overlap and documentation shape, not correctness of local API claims. Proposer: local caller file; code selects pointers; human/host must perform any substantive external confirmation. Mode: explicit operator command. Oracle: none. Timeout can return ok-shaped report with timed_out flag and zero exit; not a semantic pass. SRC-1 `kb/agent_workflows.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON report, including timeout/truncation/warnings
- Later read-back: inapplicable — report is current-command output, not a retained verification verdict
- Delegated visibility: search sees generated query, report consumer sees selected snippets/URLs and overlaps
- Selection predicate: query/top_k and doc_type; shared lexical cues capped per hit
- Invalidation or expiry: inapplicable — no acceptance or retained attestation created
- Activation or effect: advisory pointers and live-source confirmation instruction; no write admission blocked by this report
- Evidence limits: search_format internals not independently audited here; no observed user confirmation

> "note": "lexical overlap only — open canonical URL / live OpenAPI to confirm",
> --- `kb/agent_workflows.py`

#### EPI-RTE-benchmark-gate
Label: Retrieval benchmark scoring and enforcement

No counterpart after comparison with [RT-RTE-source-projection](runtime.md#rt-rte-source-projection): offline benchmark artifacts and their comparator assess served retrieval, not worker projection receipts.

Endpoints/progression: question answer_spans/expect_any and served hits → score_question → run artifacts → enforce_acceptance baseline/candidate → cmd_enforce stdout/stderr and exit status. Owner/evaluator: deterministic scorer/comparator. Target/domain: retrieval body-span return, document identity, corpus/chunk and run-comparability criteria, with optional release attempt/latency checks. Oracle: question-authored spans and expected paths, optionally cached-body shingles; their factual correctness is not adjudicated. Proposer: candidate run supplier; decider/veto: comparator refuses missing/noncomparable or regressing evidence. Intended use: bounded benchmark/release comparison, not claim truth or mechanism attribution. Mode: paired benchmark, not online per-content acceptance. Command writes no vault change; shell exit consumer can gate continuation, but no deployment caller is established here. SRC-1 `kb/retrieval_eval.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: metrics, comparator verdicts/failures, command exit
- Later read-back: saved run JSON can be read for later comparison/report; source does not establish a passing actual run
- Delegated visibility: comparator receives saved artifacts, no new node contact
- Selection predicate: valid JSON run objects; fingerprint and evidence validation; default or release criteria
- Invalidation or expiry: comparability and ground-truth fingerprints can invalidate comparison; no live truth attestation
- Activation or effect: failure returns exit 1; unreadable input returns 2; pass returns 0, without changing vault
- Evidence limits: span can occur in an unexpected document; metric checks do not establish semantic correctness, causal improvement, or whole-corpus coverage

> if failures:
>     print("ENFORCE FAILED:", file=sys.stderr)
>     for failure in failures:
>         print(f"  {failure}", file=sys.stderr)
>     return 1
> --- `kb/retrieval_eval.py`

#### EPI-RTE-automation-receipt
Label: Automated improvement receipt gate

Part of: [RT-RTE-index-curation](runtime.md#rt-rte-index-curation)
This is the local receipt/scope prerequisite to its automated Cognee-improve call, not the opaque improvement implementation.

Endpoints/progression: service improve(automation=True) / learning automation → require_automation_evaluation → local JSON receipt validation → raise ImprovementEvaluationError or permit Central-only improve. Owner/decider/veto: code; receipt supplier's measurement procedure is uninspected. Target/domain: receipt status/scope, run ID, timezone-aware timestamps and five named Boolean checks. Mode: automated Central maintenance. Oracle: asserted receipt fields, not independently replayed outcomes. Intended use: permission to call improvement until expiry, not acceptance of any generated proposition. Rejection precedes improvement; no content rollback follows merely from gate expiry. SRC-1 `kb/improvement_policy.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean internally or exception from require_automation_evaluation
- Later read-back: local receipt is re-read for later automation decisions until expiry/replacement
- Delegated visibility: improvement caller receives exception or permission; source measurement evidence is not loaded by this gate
- Selection predicate: status passed, scope central, nonempty run_id, all five required checks true, nonfuture evaluated_at and future expires_at
- Invalidation or expiry: expires_at makes receipt unusable; invalid or missing JSON fails closed
- Activation or effect: enforcing precondition on automated improvement call; not proof that the five measurements occurred
- Evidence limits: no supplied receipt, issuer execution, authenticated measurement lineage or intervention comparison

> if not isinstance(checks, dict) or any(
>     checks.get(name) is not True for name in _REQUIRED_AUTOMATION_CHECKS
> ):
>     return False
> --- `kb/improvement_policy.py`

#### EPI-RTE-garbage-cleanup
Label: Legacy garbage cleanup

Distinct from [RT-RTE-source-projection](runtime.md#rt-rte-source-projection): admin-requested classifier/deletion route, not successful projection receipt production.

Endpoints/progression: admin sources:sync /api/admin/graph/cleanup → graph scan plus bounded search probes → _legacy_garbage_kind candidates → dry-run preview or gateway delete_graph_nodes → counts/audit. Owner: operator chooses request and dry_run; deterministic classifier selects candidates; gateway performs deletion. Target/domain: canary/scaffold/cache and timestamped fossil shapes, not truth of ordinary notes. Mode: explicit maintenance; no answer oracle. Admission: admin and dry_run=false permit delete; preview offers human inspection but no bound per-candidate approval evidence. Recovery/rollback of mistaken deletion not established in this method. SRC-1 `kb/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: dry_run, counts_by_kind, candidates and deleted
- Later read-back: inapplicable — candidate list is a request result; deletion changes later retrieval availability rather than supplying retained evidence
- Delegated visibility: operator sees candidate IDs/previews and counts; gateway receives IDs
- Selection predicate: matched graph nodes and hits from five bounded probes; failed probe skipped
- Invalidation or expiry: inapplicable — no acceptance expiry; gateway deletion durability unobserved
- Activation or effect: non-dry-run candidates are passed to delete_graph_nodes; complete physical purge is not established at this call site
- Evidence limits: bounded searches can miss orphaned vectors; classifier safety claim is stronger than absence of real-world false matches established here

> deleted = 0
> if not dry_run and candidates:
>     deleted = await self.cognee.delete_graph_nodes([c["id"] for c in candidates])
> --- `kb/service.py`

#### EPI-RTE-source-withdrawal
Label: Lifecycle source withdrawal

Distinct from [RT-RTE-source-projection](runtime.md#rt-rte-source-projection): source-revision tombstone admission and retrieval exclusion, whereas that record describes worker receipt progression.

Endpoints/progression: source key deletion/replacement → tombstone_source → current exact/chunk revision selection → accept_tombstone with replacement identity → current-head retrieval filtering. Owner: service/store code; initiating sync/operator decides deletion, not an epistemic evaluator. Context/effect: changes source lineage and eligibility. Current revision binding rejects obsolete or tombstoned provider hits. It does not erase already-emitted host context. Proposed change: withdraw source from subsequent lifecycle retrieval; no semantic verdict or human truth oracle. Guard is deliberately independent of model-route drift. SRC-1 `kb/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tuple of acceptance receipts; unsupported without lifecycle store
- Later read-back: later lifecycle retrieval consumes revised current-head/tombstone state; previous source may remain retained for lineage
- Delegated visibility: retrieval filter consumes binding/receipt metadata, not a justification for source falsity
- Selection predicate: dataset/source_key and include_chunks; only non-tombstone current revisions create tombstones
- Invalidation or expiry: obsolete/tombstoned hits are excluded in lifecycle filter; legacy mode is outside this guarantee
- Activation or effect: operational withdrawal, not epistemic refutation; provider physical deletion and every alternate search branch not proven
- Evidence limits: no observed deletion; exact/lexical fallback branches and provider internals prevent a universal erasure claim

> if not binding.current or binding.source_revision.tombstone or receipt is None:
>     continue
> --- `kb/service.py`

#### EPI-RTE-feedback-record
Label: Explicit feedback retention

No counterpart after comparison with [RT-RTE-index-curation](runtime.md#rt-rte-index-curation): rating storage and optional improvement trigger are distinct from optimization proposals.

Endpoints/progression: MCP/CLI /feedback or local service → durable explicit event attempt → Cognee QA cache → on cache miss feedback note ingest → optional allow_llm and auto_improve Central automation. Owner: caller provides rating/text, code selects retention/fallback. Target/domain: caller's usefulness judgment, not an independently known answer. No answer oracle. Mode: explicit rating, not controlled experiment. Fixed guards admit note; receipt gate may veto optional improvement. Default user path is LLM-free. Retained feedback is not evidence that the rated claim was checked against the world. SRC-1 `kb/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: FeedbackResult recorded, improved, ok, reason
- Later read-back: QA cache or searchable feedback note; telemetry event stores text presence rather than full free text
- Delegated visibility: provider cache can receive QA rating and text; fallback note enters configured dataset
- Selection predicate: request identity and rating; cache success vs miss; recorded and allow_llm and auto_improve for improvement
- Invalidation or expiry: uninspected — no feedback semantic expiry in this method
- Activation or effect: recorded/improved flags and retained rating; downstream Cognee improvement effect opaque
- Evidence limits: self-improve proposal prompt does not consume raw rating text in supplied runtime; no demonstrated benefit or weight update

> if recorded and allow_llm and self.config.auto_improve:
> --- `kb/service.py`

### Claims

#### EPI-CLM-context-links
Label: Linked untrusted context

Claimed operation: answers carry source pointers and retrieved text is marked untrusted. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval), which governs write consent rather than read warrant.

> You ask from wherever you already are: the CLI, the web interface, or MCP. Answers carry a link back to the commit, issue, or document behind them, and retrieved text is marked as untrusted context worth checking before you act on it.
> --- `README.md`


#### EPI-CLM-promotion-gate
Label: Deliberate promotion gate

Claimed operation: own-space capture crosses a deliberate explicit step into shared memory, keeping it worth reading. SRC-1 `README.md`, doctrine/design. Related but not identical to [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval): a public shared-layer quality claim, not only the ingest tool's consent instruction. The runtime's automatic known-work promotion is a countercase to a universal per-item-human reading.

> Promotion is the deliberate part. Captured work lands in your own space, and reaching shared org memory takes an explicit step. That gate is what keeps the shared layer worth reading instead of turning it into everyone's scratch notes.
> --- `README.md`


#### EPI-CLM-preserve-source
Label: Preserve source wording

Claimed operation: enrichment keeps original wording and all source content and does not invent. SRC-1 `kb/llm_enrichment.py`, doctrine/design prompt; this is a request to the model, not a guaranteed implementation property. Distinct from [RT-OBJ-optimize-prompt](runtime.md#rt-obj-optimize-prompt), which instructs a different curation operation; no supplied claim counterpart.

> "Each chunk keeps the original wording (no rewriting), carries a one-line "
> "summary, and 3-6 short lowercase tags. Preserve all of the source text "
> "across the chunks. Never invent content and never include secrets."
> --- `kb/llm_enrichment.py`


#### EPI-CLM-benchmark-score
Label: Reported body-span recall

Claimed operation: bounded 69-question harness body-span retrieval result, explicitly not whole-corpus recall. SRC-1 `README.md`, reported operation. No counterpart after comparison with [RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval); it is a performance claim, not a consent rule. No supplied execution artifact independently establishes this number.

> A 2026-08-03 69-question golden harness scored `answer_recall@5` at 0.8974 over the 39 questions carrying validated answer spans.
> --- `README.md`


### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
