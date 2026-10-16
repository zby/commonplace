---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Cludebot's memory-derived claims, contradiction handling, confidence gates and evaluation authority at the frozen revision."
run-id: AAS-2026-10-15-cludebot-cb70d11d215b-01
reviewed-boundary: cecf234f10397b1e21dec2ff65ded864982f3564
---

# Cludebot epistemic report

## Source-and-claim boundary

The question is how Clude's retained experiences become claims or behavioral guidance, what checks license reliance, and which consumers give those results force. Scope and exclusions are those of the supplied [boundary and Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. No target was executed. The supplied runtime is a baseline, not an inspection limit. Memory and workflow members were not supplied.

The cognitive-memory claim is [RT-CLM-cognitive-memory](runtime.md#rt-clm-cognitive-memory). Additional consequential design claims are [EPI-CLM-belief-update](#epi-clm-belief-update), [EPI-CLM-action-learning](#epi-clm-action-learning) and [EPI-CLM-confidence-gate](#epi-clm-confidence-gate). Source-native terms such as “resolved,” “learned,” and “confidence” are not acceptance findings.

Coverage below distinguishes direct reads from supplied findings. All direct reads and searches were within SRC-1 at the frozen commit. Ranges were bounded around named operations; a named path does not imply full-file inspection. Unassessed included operations prevent a system-complete negative about truth checking or acceptance.

| Entry point or operation | Source path | Coverage and records, or limit and conclusion prevented |
|---|---|---|
| Authenticated/guest chat, SDK writes/recall, pack JSON import, dashboard execution, setup | `apps/server/src/routes/chat.routes.ts`; `packages/brain/src/sdk/cortex.ts`; `apps/server/src/routes/memory-packs.routes.ts`; `packages/brain/src/agents/executor.ts`; `packages/brain/src/cli/setup.ts` | Supplied [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-guest-chat](runtime.md#rt-rte-guest-chat), [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), [RT-RTE-pack-import](runtime.md#rt-rte-pack-import), [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task), [RT-RTE-host-setup](runtime.md#rt-rte-host-setup); not independently re-audited here. |
| CLI dispatch | `packages/brain/src/cli/index.ts` | Direct dispatch read: setup/init/register/connect/ship/status/export/import/sync/inject-instructions/doctor/dream/verify/snapshot/MCP/bot. Verify traced below; import/export/sync/ship internals unassessed, preventing universal portability/admission conclusions. |
| MCP exposed operations and prompt | `packages/brain/src/mcp/server.ts` | Direct registry searches and recall read: recall/store/stats/find_clinamen/delete/update/list/batch-store and memory-instructions prompt. Supplied entry record plus [EPI-RTE-confidence-check](#epi-rte-confidence-check), [EPI-RTE-memory-mutation](#epi-rte-memory-mutation). Stats/list/anomaly semantics beyond dispatch not audited; no completeness or truth license inferred. |
| Main dream scheduling/consolidation | `packages/brain/src/memory/dream/cycle.ts` | Supplied [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle). Direct reads add citation parsing, cop-out filter, compaction, reflection, contradiction resolution, learning handoff and emergence context. Deep connection and JEPA remain unassessed; no system-wide maintenance verdict. |
| Compaction, reflection, contradiction resolution | `packages/brain/src/memory/dream/cycle.ts` | Direct [EPI-RTE-memory-compaction](#epi-rte-memory-compaction), [EPI-RTE-self-reflection](#epi-rte-self-reflection), [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution). |
| Hosted dreams | `packages/brain/src/memory/hosted-dreams.ts` | Direct per-owner generation/admission body: [EPI-RTE-hosted-dreams](#epi-rte-hosted-dreams); deployment and scheduler activation not established. |
| SQLite maintenance | `packages/brain/src/storage/dream-engine.ts`; `packages/brain/src/storage/sqlite-store.ts` | Direct queue processing, Ollama call and completion sink: [EPI-RTE-local-dreams](#epi-rte-local-dreams). Queue scheduling/decay found by search; downstream queue-result consumers beyond inspected completion remain unassessed. |
| Social outcome/strategy refinement | `packages/brain/src/memory/action-learning.ts`; `packages/brain/src/services/response.service.ts` | Direct implementation bodies: [EPI-RTE-action-learning](#epi-rte-action-learning), [EPI-RTE-strategy-consumption](#epi-rte-strategy-consumption). Actual action logging at all social callers not audited; no exercised feedback-loop claim. |
| Confidence and cleanup | `packages/brain/src/experimental/confidence-gate.ts`; `packages/brain/src/experimental/enhanced-recall.ts`; `packages/brain/src/services/response.service.ts`; `packages/brain/src/mcp/server.ts` | Direct computation and consumers: [EPI-RTE-confidence-check](#epi-rte-confidence-check), [EPI-RTE-confidence-consumption](#epi-rte-confidence-consumption). IRCoT, reranker and ensemble internals unassessed; prevents full epistemic classification of enhanced recall. |
| MemoryPack verify and revocation | `packages/brain/src/cli/verify.ts`; `packages/memorypack/src/reader.ts` | Direct CLI and signature/revocation ranges: [EPI-RTE-pack-verification](#epi-rte-pack-verification). Crypto primitive internals, chain adapter and all import consumers not audited; no end-to-end security or withdrawal guarantee. |
| LongMemEval judge/revision | `misc/scripts/longmemeval-benchmark.ts` | Direct judge, optional critic/reviser, call sites, score accumulation and rejudge selection: [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks). Generation/retrieval variants not exhaustively traced; tracked scores not independently authenticated. |
| Other social jobs, clients, marketplace/PMP/title/on-chain paths, experimental local memory, other evaluators | Paths inventoried in [boundary](boundary.md#boundary-and-evidence) and [runtime](runtime.md#runtime-account) | Included but unassessed here. Missing inspection prevents whole-system acceptance, cryptographic provenance, behavioral adaptation and evaluator-coverage conclusions. No inaccessible source is alleged. |

Missing execution evidence prevents conclusions about actual generated propositions, actual content-directed criticism, downstream activation and improvement. Missing provider internals prevent identification of provider-held knowledge or training changes; they do not erase the inspected symbolic/text update routes. No source or boundary amendment is needed. The newly inspected specialist routes supplement, rather than supersede, the runtime's expressly limited orchestration account.

## Epistemic-object inventory

Each row's owned fields and evidence are in the cited record; the short labels distinguish operative parts rather than copy those fields.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | see record | Stored content | SRC-1, `packages/brain/src/memory/memory.ts` | see record |
| [EPI-OBJ-dream-products](#epi-obj-dream-products) | see record | Dream products | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | see record |
| [EPI-OBJ-strategy-state](#epi-obj-strategy-state) | see record | Outcome/strategy parts | SRC-1, `packages/brain/src/memory/action-learning.ts` | see record |
| [EPI-OBJ-confidence-result](#epi-obj-confidence-result) | see record | Retrieval confidence | SRC-1, `packages/brain/src/experimental/confidence-gate.ts` | see record |
| [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context) | see record | Rendered context | SRC-1, `packages/shared/src/core/memory-grounding.ts` | see record |
| [RT-CMP-generate-response](runtime.md#rt-cmp-generate-response), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model), [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic), [RT-CMP-embeddings](runtime.md#rt-cmp-embeddings), [RT-CMP-local-embedder](runtime.md#rt-cmp-local-embedder) | see records | Opaque parametric state | SRC-1, `packages/shared/src/core/claude-client.ts` | see records; no individuated provider-held propositions |

## Authority-route ledger

Rows split checks from disposition, retention from use, and different behavioral forces. Repeated route citations refer to different functions of the same implementation. Owned fields say “see” rather than reproducing the declaring record. Architectural status is this overlay's assessment.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), [RT-RTE-pack-import](runtime.md#rt-rte-pack-import) | content transformation | implemented | see records | truth-apt transformation: acquisition/import | see records | see records | see records | see records | see records | see records | see records | see records | SRC-1, `packages/brain/src/memory/memory.ts` | none | none | see records; source warrant unknown |
| [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `apps/server/src/routes/chat.routes.ts` | none | none | see record |
| [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) | operational admission/selection/consumption | implemented | [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context) | truth-apt transformation: non-ampliative reshaping | see records | see records | see records | see records | see records | see records | see records | [RT-BAP-chat-grounding](runtime.md#rt-bap-chat-grounding) | SRC-1, `apps/server/src/lib/memory-prompt.ts` | none | none | Context delivery, not verification; see records |
| [EPI-RTE-memory-compaction](#epi-rte-memory-compaction) | content transformation | implemented | [EPI-OBJ-dream-products](#epi-obj-dream-products) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | [RT-CLM-cognitive-memory](runtime.md#rt-clm-cognitive-memory) | none | see record |
| [EPI-RTE-memory-compaction](#epi-rte-memory-compaction) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | none | none | see record |
| [EPI-RTE-self-reflection](#epi-rte-self-reflection) | content transformation | implemented | [EPI-OBJ-dream-products](#epi-obj-dream-products) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | [RT-CLM-cognitive-memory](runtime.md#rt-clm-cognitive-memory) | none | see record |
| [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | content transformation | implemented | [EPI-OBJ-dream-products](#epi-obj-dream-products) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | [EPI-CLM-belief-update](#epi-clm-belief-update) | resolution not verified truth | see record |
| [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution), [EPI-RTE-self-reflection](#epi-rte-self-reflection) | check/evidence production | implemented | see records | no content change | see records | see records | see records | see records | see records | see records | see records | see records | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | none | surface/citation check only | see records |
| [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution), [EPI-RTE-self-reflection](#epi-rte-self-reflection) | disposition/acceptance | implemented | see records | no content change | see records | see records | see records | see records | see records | see records | see records | see records | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | none | admission is not epistemic acceptance | see records |
| [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | behavior/policy adaptation | implemented | see record | non-truth-apt policy/content update: decay weight | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/dream/cycle.ts` | [EPI-CLM-belief-update](#epi-clm-belief-update) | lower importance is not judged falsity | see record |
| [EPI-RTE-hosted-dreams](#epi-rte-hosted-dreams) | content transformation | implemented | [EPI-OBJ-dream-products](#epi-obj-dream-products) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/hosted-dreams.ts` | none | none | factual branch; policy branch in record |
| [EPI-RTE-hosted-dreams](#epi-rte-hosted-dreams) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/hosted-dreams.ts` | none | JSON/length admission only | see record |
| [EPI-RTE-local-dreams](#epi-rte-local-dreams) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/storage/sqlite-store.ts` | none | queue result is not memory integration | see record |
| [EPI-RTE-action-learning](#epi-rte-action-learning) | check/evidence production | implemented | [EPI-OBJ-strategy-state](#epi-obj-strategy-state) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/action-learning.ts` | [EPI-CLM-action-learning](#epi-clm-action-learning) | measurement proxy not causal attribution | arithmetic only; see record |
| [EPI-RTE-action-learning](#epi-rte-action-learning) | behavior/policy adaptation | implemented | [EPI-OBJ-strategy-state](#epi-obj-strategy-state) | non-truth-apt policy/content update: generated procedural rule and importance | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/action-learning.ts` | [EPI-CLM-action-learning](#epi-clm-action-learning) | no measured future benefit | see record |
| [EPI-RTE-strategy-consumption](#epi-rte-strategy-consumption) | operational admission/selection/consumption | implemented | [EPI-OBJ-strategy-state](#epi-obj-strategy-state) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/services/response.service.ts` | none | none | see record |
| [EPI-RTE-confidence-check](#epi-rte-confidence-check) | check/evidence production | implemented | [EPI-OBJ-confidence-result](#epi-obj-confidence-result) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/experimental/confidence-gate.ts` | [EPI-CLM-confidence-gate](#epi-clm-confidence-gate) | retrieval proxy not truth confidence | see record |
| [EPI-RTE-confidence-consumption](#epi-rte-confidence-consumption) | operational admission/selection/consumption | implemented | [EPI-OBJ-confidence-result](#epi-obj-confidence-result) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/services/response.service.ts` | [EPI-CLM-confidence-gate](#epi-clm-confidence-gate) | advisory not hard abstention | see record |
| [EPI-RTE-memory-mutation](#epi-rte-memory-mutation) | disposition/acceptance | implemented | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/memory/memory.ts` | none | withdrawal is row-local | see record |
| [EPI-RTE-pack-verification](#epi-rte-pack-verification) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/memorypack/src/reader.ts` | none | byte authenticity not proposition truth | see record |
| [EPI-RTE-pack-verification](#epi-rte-pack-verification) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `packages/brain/src/cli/verify.ts` | none | CLI result does not enforce all imports | see record |
| [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `misc/scripts/longmemeval-benchmark.ts` | none | score bounds in record | see record |
| [EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `misc/scripts/longmemeval-benchmark.ts` | none | conditional critic fallback is permissive | see record |

No evidence-consuming epistemic acceptance decision or subsequent lifecycle integration is established by the inspected dream writers. Their retention and operational use remain positive findings. This is not a negative covering the unassessed routes listed above.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-cognitive-memory](runtime.md#rt-clm-cognitive-memory) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), [EPI-RTE-memory-compaction](#epi-rte-memory-compaction), [EPI-RTE-self-reflection](#epi-rte-self-reflection), [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | none inspected | No matched intervention or run | Maintenance exists beyond storage/retrieval | “Cognitive” supplies no independent warrant |
| [EPI-CLM-belief-update](#epi-clm-belief-update) | see record | SRC-1, `packages/brain/src/memory/dream/cycle.ts`, doctrine/design | see record | [EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution) | none inspected | see route | Model proposes resolution; code stores and changes decay | No check of whether the chosen belief is actually more accurate |
| [EPI-CLM-action-learning](#epi-clm-action-learning) | see record | SRC-1, `packages/brain/src/memory/action-learning.ts`, doctrine/design | see record | [EPI-RTE-action-learning](#epi-rte-action-learning), [EPI-RTE-strategy-consumption](#epi-rte-strategy-consumption) | none inspected | see routes | Outcome-responsive policy-writing capacity and later delivery wired | Improved capacity and exercised self-improvement not established |
| [EPI-CLM-confidence-gate](#epi-clm-confidence-gate) | see record | SRC-1, `packages/brain/src/experimental/confidence-gate.ts`, doctrine/design | see record | [EPI-RTE-confidence-check](#epi-rte-confidence-check), [EPI-RTE-confidence-consumption](#epi-rte-confidence-consumption) | none inspected | see routes | Score, low-score filtering and optional hedging wired | Expected hallucination reduction untested here; score is not calibrated semantic support |

## Bounded conclusion

Clude acquires caller and imported text, retains user/model exchanges, and supplies selected text to later models. Source warrant is unknown for arbitrary caller assertions; preserving text or an original ID does not authenticate the assertion. Chat rendering is bounded reshaping of selected material, not acceptance. Its prompt asks for grounded answers; no inspected answer-verification consumer enforces that request ([RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), [RT-RTE-pack-import](runtime.md#rt-rte-pack-import), [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn)). Guest chat is a counterexample to universal memory participation, not to the authenticated route.

Dream outputs can contain truth-apt observations about users or Clude. Their exact semantic relation to inputs remains indeterminate without response instances: prompts may request compression, synthesis or patterns, but implementation alone proves neither semantic preservation nor non-entailment. Citation parsing maps positions to source IDs and strips citation text; the cop-out filter rejects a small prefix class. Neither checks supporting evidence against the asserted proposition. Hosted dream JSON/length checks have a different domain and omit the direct citation map. These mechanisms admit retained candidates, not evidence-consuming acceptance for a stated epistemic use. No accepted ampliative production is established ([EPI-RTE-memory-compaction](#epi-rte-memory-compaction), [EPI-RTE-self-reflection](#epi-rte-self-reflection), [EPI-RTE-hosted-dreams](#epi-rte-hosted-dreams)).

Contradiction resolution does have operational force: successful resolution storage permits links and a decay reduction on the lower-importance original, with age as tiebreaker. Code does not inspect which original the model actually called false. Thus a generated “resolution” and an altered reliance weight coexist without independent verification of the winning belief. Deletion/update and signed revocation offer other withdrawal mechanisms, but no inspected route establishes automatic retraction of all derived statements or already supplied context ([EPI-RTE-contradiction-resolution](#epi-rte-contradiction-resolution), [EPI-RTE-memory-mutation](#epi-rte-memory-mutation), [EPI-RTE-pack-verification](#epi-rte-pack-verification)).

Deterministic calculations warrant only bounded propositions about supplied numbers: weighted engagement, rate comparisons, retrieval counts and score dispersion. They do not entail “this strategy caused success” or “these memories support this answer.” Confidence cleanup can remove low-score evidence before generation; the later hedging instruction remains advisory. MCP confidence is result metadata, not the complete hedging text ([EPI-RTE-confidence-check](#epi-rte-confidence-check), [EPI-RTE-confidence-consumption](#epi-rte-confidence-consumption)).

Social outcomes can automatically shape procedural rules and importance, and the response service reserves additional procedural recall slots. This is a real behavior-shaping pathway without requiring a new accepted factual claim. Reflection also has an inspectable self-representation loop: accumulated behavior descriptions can generate self-model text, and that text enters future reflection/emergence contexts. Delivery, actual compliance and beneficial change remain distinct. No route here demonstrates improved future capacity, exercised self-improvement, or full theory-builder conditions; those are separate questions, not a single system rating ([EPI-RTE-action-learning](#epi-rte-action-learning), [EPI-RTE-strategy-consumption](#epi-rte-strategy-consumption), [EPI-RTE-self-reflection](#epi-rte-self-reflection)).

Evaluation is not universally absent: the benchmark has a reference-answer judge, an optional evidence critic/reviser, and score consumers. Their force is bounded to benchmark answers, revisions and reports. Signatures check bytes against a key, not the truth of signed statements. Neither evaluator transfers a universal warrant to dream products or production answers. No independently observed or causal performance finding follows from this inspection ([EPI-RTE-benchmark-checks](#epi-rte-benchmark-checks), [EPI-RTE-pack-verification](#epi-rte-pack-verification)). Provider-held parametric content remains opaque; the supplied component records establish inference/model selection, not runtime training or individuated internal knowledge. Unassessed included branches prevent a complete-system absence conclusion.

## Shared records

### Operative objects

#### EPI-OBJ-memory-content
Label: Stored memory content

Natural-language `content`/`summary` and symbolic type/tags/importance/IDs reside in memory rows. Imported or caller-authored content can assert events, preferences and facts; exact truth aptitude is instance-dependent. Distinct from the supplied [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context), which is a transient rendering, and the route [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), not a duplicate object. SRC-1 implementation, `packages/brain/src/memory/memory.ts`; write guards and acquisition evidence also supplied by that route. Truth checks and source authentication are not established by type labels.

> if (patches.summary !== undefined) updates['summary'] = patches.summary.slice(0, 500);
>   if (patches.content !== undefined) updates['content'] = patches.content.slice(0, 5000);
> --- `packages/brain/src/memory/memory.ts`

#### EPI-OBJ-dream-products
Label: Dream product parts

This inventory groups, without equating authority, semantic compaction/resolution text, self-model reflection text and hosted procedural rules in memory rows. Natural-language claims may be truth-apt; imperatives alone need not be. Symbolic evidence IDs and graph links are lineage assertions, not textual proofs. Distinct output object from the transient [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context); closest production container is [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle). The separate routes below own differing checks/consumers. SRC-1 implementation, `packages/brain/src/memory/dream/cycle.ts`, `packages/brain/src/memory/hosted-dreams.ts`. No actual generated instance was inspected; classifications remain local to each route, not a claim that all outputs are novel knowledge.

> type: 'self_model',
>     content: `Self-reflection: ${text}`,
> --- `packages/brain/src/memory/dream/cycle.ts`

#### EPI-OBJ-strategy-state
Label: Action outcome and strategy parts

SRC-1 implementation, `packages/brain/src/memory/action-learning.ts`: action/outcome episodic rows contain natural-language reports and symbolic action IDs, tags, scores and methods. Procedural rows contain natural-language rules and symbolic feature/rate metadata. Importance/access counters are numerical selection state, not model parameters. Truth-apt claims concern reported actions/metrics; an imperative strategy itself is policy. Distinct from [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context); these are persisted producer-side parts, later consumed through the separately traced response service. No matching supplied object after comparison.

> content: `[LEARNED STRATEGY] ${lesson}`,
>           summary: `Strategy (${feature}): ${lesson.slice(0, 120)}`,
> --- `packages/brain/src/memory/action-learning.ts`

#### EPI-OBJ-confidence-result
Label: Evidence confidence result

SRC-1 implementation, `packages/brain/src/experimental/confidence-gate.ts`: a transient symbolic/numerical result with score, sufficient flag, component values and optional natural-language hedging instruction. It asserts threshold satisfaction over retrieval signals, not a calibrated probability that a proposition is true. No durable store is shown in this function. Distinct from supplied embedding components and rendered memory context; no supplied counterpart after comparison.

> const sufficient = score >= threshold;
> --- `packages/brain/src/experimental/confidence-gate.ts`

### Routes

#### EPI-RTE-memory-compaction
Label: Memory compaction
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

SRC-1 implementation, `packages/brain/src/memory/dream/cycle.ts`: code selects old faded low-importance episodic rows, groups by first concept, asks the shared generation model to distill summaries, stores semantic text, marks originals compacted and links them. Code owns progression and automatic admission; no per-item human veto or answer oracle is shown. The model sees summaries, not complete episodes. The proposal is intended to preserve important meaning, but no checked semantic equivalence establishes non-ampliative reshaping; remaining possibilities include omission, faithful compression and new generalization. No actual output distinguishes them. A successful write is a retention prerequisite for marking originals, not acceptance. The local `hashId` used for `compacted_into` is generated independently here; do not infer from it a verified identity with the stored summary. No all-or-nothing rollback is shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: phase completion; summary IDs and counts enter the dream log.
- Later read-back: semantic products are eligible for ordinary recall; compacted flag affects later compaction eligibility.
- Delegated visibility: selected summaries and concept label reach shared generation.
- Selection predicate: episodic, not compacted, decay below 0.3, importance below 0.5, older than seven days; at least five candidates and groups of at least three.
- Invalidation or expiry: original rows are marked, not deleted here; phase errors are logged and other groups may continue.
- Activation or effect: generated text retention, original flags and graph writes are wired; downstream use is unobserved.
- Evidence limits: no semantic verifier, run or transaction guarantee established in this body; no accepted lifecycle integration inferred.

> 'Distill these memories into their essential meaning — what was the overall pattern or lesson? ' +
>           'Be concise. One or two sentences max. Preserve the most important information.',
> --- `packages/brain/src/memory/dream/cycle.ts`

> .update({ compacted: true, compacted_into: hashId })
>           .in('id', memoryIds);
> --- `packages/brain/src/memory/dream/cycle.ts`

#### EPI-RTE-self-reflection
Label: Self reflection
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

SRC-1 implementation, `packages/brain/src/memory/dream/cycle.ts`: self-model and recent semantic summaries plus computed statistics feed model-requested self-observations. Citation parsing and cop-out checks precede automatic storage as self-model text, then temporal/support links and dream logs. Model proposes, software can reject cop-out prefixes, no per-observation human approval or reference oracle is shown. Parser validates citation positions, not semantic support; missing valid citations yield an empty ID list rather than rejection. Exact input/output relations remain indeterminate without generated text. Stored text licenses operational availability, not established self-knowledge.

Concrete deterministic trace: with source IDs 17 and 29, input `I prefer tea (because of 1, 2)` matches the first citation pattern, yields IDs 17 and 29, and returns `I prefer tea`. This follows the inspected parser, not target execution. That same syntactic mapping would work for a false assertion; no entailment test occurs. Prefix `I'm not sure` is rejected, but a confident unsupported assertion need not match a cop-out pattern.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: phase completion or discard; dream log records inputs/output and stored IDs.
- Later read-back: self-model rows feed future reflection and emergence; semantic recall/rendering can expose products according to caller selection.
- Delegated visibility: numbered self-model/semantic summaries and aggregate statistics reach generation.
- Selection predicate: current self-model, up to ten semantic memories from 48 hours; cop-out prefix veto after generation.
- Invalidation or expiry: later memory operations can alter rows; prior self-models remain linked, not automatically retracted.
- Activation or effect: stored representation can shape later generation inputs; exercised behavioral dependence is unobserved.
- Evidence limits: no instance establishes accurate self-description or content-directed criticism. Reflection's representation/update and representation-to-context directions are wired, not demonstrated reliable introspection.

> if (evidenceIds.length > 0) {
>       return { text: cleanText.trim(), evidenceIds: [...new Set(evidenceIds)] };
>     }
>   }
>
>   return { text: text.trim(), evidenceIds: [] };
> --- `packages/brain/src/memory/dream/cycle.ts`

> return COPOUT_PATTERNS.some(p => p.test(text.trim()));
> --- `packages/brain/src/memory/dream/cycle.ts`

#### EPI-RTE-contradiction-resolution
Label: Contradiction resolution
Part of: [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle)

SRC-1 implementation, `packages/brain/src/memory/dream/cycle.ts`: unresolved-pair RPC supplies up to three candidate pairs; full content and age/type/importance/concepts are passed to shared generation. The model is asked which is more accurate now or to synthesize; its response is parsed and cop-out filtered, then automatically stored as semantic text. This is model judgment in the domain of the supplied pair, not independent environmental evidence or an answer oracle. Truth-apt transformation is indeterminate: choosing one belief may preserve content; synthesis may add claims, but no response establishes non-entailment. No per-result human approval is shown.

After successful storage, code links both originals and lowers decay on the lower-importance original (older if importance ties). This disposition rule does not parse or enforce the model's attribution of error. It licenses reduced retrieval weight, not epistemic falsification or deletion of that original. `resolves` links record a claimed relation, not acceptance against a truth criterion. Failed RPC skips the phase; partial writes/links are not rolled back as one unit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: phase completion and dream log when outputs exist.
- Later read-back: stored resolution and changed original decay can affect later recall; exact downstream dependence is unobserved.
- Delegated visibility: both originals' content and metadata reach shared generation.
- Selection predicate: unresolved pairs from RPC, available originals, non-cop-out generated text; successful store gates decay/link changes.
- Invalidation or expiry: originals persist; decay is bounded at 0.05; no cascade retraction is implemented in this phase.
- Activation or effect: candidate storage, relation writes and deterministic weight change are wired; accurate resolution is not observed.
- Evidence limits: RPC pair detection internals not assessed here; code does not adjudicate source truth. No full theory-builder cycle is established by a request for resolution.

> const weaker = memA.importance !== memB.importance
>         ? (memA.importance < memB.importance ? memA : memB)
>         : (new Date(memA.created_at).getTime() < new Date(memB.created_at).getTime() ? memA : memB);
>       const newDecay = Math.max(0.05, weaker.decay_factor * 0.8);
> --- `packages/brain/src/memory/dream/cycle.ts`

#### EPI-RTE-hosted-dreams
Label: Hosted dreams

SRC-1 implementation, `packages/brain/src/memory/hosted-dreams.ts`. Distinct from main [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), which explicitly distinguishes the hosted algorithm. Per-owner execution selects recent episodic summaries, asks an OpenRouter model for factual insight strings and separately behavioral rules, then parses JSON and admits bounded-length outputs to semantic/procedural rows. Code decides eligibility and length/format admission; model proposes; no per-item human veto, reference oracle or semantic evidence check is shown. Factual output relation remains indeterminate; imperative rules are non-truth-apt policy updates unless their particular text also asserts facts. Store success gives later availability, not epistemic acceptance.

The named `meta-llama/llama-3.3-70b-instruct` is remote distributed-parametric computation: this route performs inference, not weight updates. An identifier rather than immutable weights is supplied; provider resolution can change and its internals are uninspected. This is an added call site of the shared remote-generation family, not evidence of fixed weights.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: consolidated/procedural counts.
- Later read-back: generated memory rows become eligible for ordinary owner-scoped recall.
- Delegated visibility: up to thirty dated episode summaries reach the model; no citation-to-ID map is stored by these writes.
- Selection predicate: per-owner count gates, at least five recent episodes, OpenRouter enabled; parsed insights limited to five, rules to three; lengths greater than ten and less than 500.
- Invalidation or expiry: parse/provider errors log and skip; completed writes remain; no batch rollback shown.
- Activation or effect: automatic semantic/procedural writes are wired; later model compliance is unobserved.
- Evidence limits: no observed generated proposition, warranted premise set, acceptance or causal gain.

> if (insight && insight.length > 10 && insight.length < 500) {
>               const id = await storeMemory({
> --- `packages/brain/src/memory/hosted-dreams.ts`

#### EPI-RTE-local-dreams
Label: Local dream queue

SRC-1 implementation, `packages/brain/src/storage/dream-engine.ts`, `packages/brain/src/storage/sqlite-store.ts`. Distinct from the main dream route, and a material local-mode mechanism within [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), but not the same entry/dispatch operation. Queue processing fetches referenced memories, constructs an operation prompt, calls local Ollama and persists the returned result in `dream_queue`. The inspected completion sink updates queue status/result only; it does not insert a semantic memory. No broader claim that nothing ever consumes this queue result follows. Exact result truth aptitude and transformation remain indeterminate without an instance.

Ollama is distributed-parametric inference using a selected model string. This body does not update parameters or pin a weight digest; local artifacts/provider resolution are uninspected and mutable. Code owns processing and failure status; the model proposes text, with no independent answer oracle or semantic veto in the inspected sink. Queued task completion is not evidence-consuming acceptance of a belief.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: queue-processing completion; `executeDream` stores success/result or failure metadata.
- Later read-back: result persists in SQLite queue; a later consumer promoting it to memory is uninspected — none is established by the inspected completion method.
- Delegated visibility: fetched source memories become an operation-specific Ollama prompt.
- Selection predicate: at least five pending entries and detected LLM; up to fifty fetched pending entries.
- Invalidation or expiry: request has AbortController timeout; exceptions mark queue entry failed.
- Activation or effect: queue-result persistence is wired; later behavioral use is uninspected.
- Evidence limits: queue retention is not lifecycle integration, and local/main dream parity is not established.

> const result = await this.dreamWithOllama(entry.operation, memories, llm.model);
>       this.store.completeDream(entry.id, { success: true, result });
> --- `packages/brain/src/storage/dream-engine.ts`

> UPDATE dream_queue
>       SET status = 'completed', result = ?, completed_at = ?
>       WHERE id = ?
> --- `packages/brain/src/storage/sqlite-store.ts`

#### EPI-RTE-action-learning
Label: Action learning

SRC-1 implementation, `packages/brain/src/memory/action-learning.ts`. Closest supplied route is [RT-RTE-dream-cycle](runtime.md#rt-rte-dream-cycle), whose learning phase calls this implementation; this route spans action/outcome writes and refinement outside that orchestration, rather than duplicating the cycle. Caller reports become episodic rows; code tracks tweet metrics, classifies outcome, updates action tags/importance, groups recent outcomes by feature, and asks a model for a caution or reinforcement rule. Software automatically stores procedural text and adjusts existing strategy importance; no human per-rule approval or independent correctness oracle is shown.

The engagement evaluator's target is a weighted count over returned X metrics, not the truth of a reply or causal efficacy of a strategy. Concrete deduction: supplied likes=4, retweets=1, replies=2 yield 4+2+6=12, classified positive with score 0.24. That arithmetic is entailed by supplied numbers; source accuracy and the mapping from engagement to “good” remain auxiliary assumptions. Missing reply ID produces neutral/missing-data rather than a fabricated metric.

Refinement requires at least three outcome-tagged recent actions globally and at least two per feature. Negative rate above 0.6 or positive above 0.7 triggers a generated rule. Imperatives are policy updates, not necessarily truth-apt claims. The model sees rates and short action examples; source causal rationale is not established. Reinforcement uses shared feature tags, not actual proof the strategy was recalled or caused the action's outcome. It may raise importance even without content-directed criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: memory IDs, tracked count or lesson strings, with errors logged.
- Later read-back: outcome tags and importance feed future refinements; procedural rows can enter the response service's dedicated strategy recall.
- Delegated visibility: metrics come from X; feature counts and up to three short examples reach generation.
- Selection predicate: pending actions aged six to 48 hours for measurement; last seven days/up to fifty actions for refinement; feature/rate gates above.
- Invalidation or expiry: missing API metrics may leave items pending; later update/delete are separate; repeated refinement can write more rules without versioned rollback.
- Activation or effect: outcome-driven selection-state and procedural writes are wired; realized downstream behavior and improved capacity unobserved.
- Evidence limits: no causal intervention, counterfactual or trace connects a particular strategy to success. Operating mode is ongoing social feedback, not reference-answer testing.

For theory assessment: guidance asks for specific caution/reinforcement rules, and the persisted output is the rule plus feature/rate metadata, not a full causal explanation. Theory-builder conditions 1–4: condition 1 uninspected for actual generated theory content; condition 2 uninspected for decision dependence rather than delivery; condition 3 uninspected for claim-specific blame/revision rather than feature-level rates; condition 4 uninspected for retention/use of actual criticism. None follows from naming this “learning.” Addressability is row-level text/metadata, not demonstrated assumption-level revision. Persistence across invocations is wired. Under learning, future capacity improvement and attribution remain uninspected. A dispositional improvement-directed self-change pathway exists through outcome-responsive rules and later prompt delivery; exercised self-improvement lacks subsequent operation causally depending on the changed rule. This limit is independent of the reflected self-model route.

> const totalEngagement = (metrics.likes || 0) + (metrics.retweets || 0) * 2 + (metrics.replies || 0) * 3;
> --- `packages/brain/src/memory/action-learning.ts`

> if (negRate > 0.6) {
>         // Mostly bad outcomes — generate caution rule
>         lesson = await generateLesson(feature, stats, 'caution');
>       } else if (posRate > 0.7) {
>         // Mostly good outcomes — reinforce strategy
>         lesson = await generateLesson(feature, stats, 'reinforce');
>       }
> --- `packages/brain/src/memory/action-learning.ts`

> const relevantPositive = positiveActions.filter(a =>
>         (a.tags || []).some((t: string) => t === `action:${feature}`)
>       );
> --- `packages/brain/src/memory/action-learning.ts`

#### EPI-RTE-strategy-consumption
Label: Strategy prompt consumption

SRC-1 implementation, `packages/brain/src/services/response.service.ts`. Distinct caller from [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) and [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task), both use other model-input paths. Whenever this service receives memory options, code recalls three procedural memories with importance at least 0.5 in parallel with enhanced recall, deduplicates and formats them into generation options. Textual rules have advisory force through the shared generation model's memory context over that invocation. No accepted-claim requirement precedes delivery. Code controls inclusion; provider compliance remains unobserved.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated string or thread from shared generation.
- Later read-back: retained procedural rows can recur in subsequent service invocations with memory enabled.
- Delegated visibility: deduplicated/formatted memory text and feature instructions reach shared generation; not every stored strategy.
- Selection predicate: `opts.memory` present; top procedural recall limited to three, minimum importance 0.5, access tracking enabled.
- Invalidation or expiry: context rebuilt each invocation; changed/deleted rows affect later recall, not already delivered text.
- Activation or effect: extra procedural delivery is wired; rule obedience and improved responses are unobserved.
- Evidence limits: source-native “guaranteed slots” is an additional query/merge, not guaranteed activation or semantic validity.

> memoryTypes: ['procedural'],
>         limit: 3,
>         minImportance: 0.5,
>         trackAccess: true,
> --- `packages/brain/src/services/response.service.ts`

#### EPI-RTE-confidence-check
Label: Retrieval confidence computation

SRC-1 implementation, `packages/brain/src/experimental/confidence-gate.ts`. Distinct computation from supplied [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry); actual MCP and response-service consumers are split below. The check target is the quality-signal tuple of retrieved memories: count coverage, normalized first score, type diversity and top-three score dispersion. Code computes a weighted scalar and threshold flag; it does not inspect whether individual propositions support an answer. `agreement` names score clustering, not agreement of meanings. Default parameters are threshold 0.4, expected count three and maximum score two.

Concrete deterministic trace with one semantic memory of score 2: coverage=1/3, topScore=1, diversity=1/4, agreement=1; combined result is 0.1+0.35+0.0375+0.2=0.6875, so sufficient is true. The text could be false without changing that result. Zero memories return score zero and no-evidence instruction. These deductions use inspected code, not execution. They license conclusions about computation over supplied scores, not answer truth or calibrated support probability. Model-free computation has no answer oracle and performs no content acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: score, sufficient flag, component breakdown and optional hedging text.
- Later read-back: inapplicable — transient computation; this function does not persist results.
- Delegated visibility: inapplicable — deterministic local computation makes no provider call.
- Selection predicate: supplied memory array and optional numeric parameters; top score assumes first item represents best score.
- Invalidation or expiry: recomputed per call; no continuing endorsement is stored.
- Activation or effect: output can drive separate cleanup/hedging consumers; the function itself does not block generation.
- Evidence limits: no semantic support analysis, calibration evidence or hallucination experiment inspected.

> const score =
>     0.30 * coverage +
>     0.35 * topScore +
>     0.15 * diversity +
>     0.20 * agreement;
> --- `packages/brain/src/experimental/confidence-gate.ts`

#### EPI-RTE-confidence-consumption
Label: Confidence cleanup and delivery

SRC-1 implementation, `packages/brain/src/experimental/enhanced-recall.ts`, `packages/brain/src/services/response.service.ts`, `packages/brain/src/mcp/server.ts`. Distinct downstream consumers of the confidence computation; closest supplied overlap is [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry), whose MCP subpath receives metadata, not the service's hedging policy. Enhanced recall removes memories below score 0.15 when configured, then computes confidence. Response service conditionally appends hedging text to feature instruction. This changes available evidence and advisory response policy, not semantic acceptance. Strategies are merged after the main result's confidence assessment, so that assessment is not a check of the final complete prompt.

MCP self-hosted loading can initialize the evaluator; recall only evaluates when it exists and at least one memory has a numerical score. It returns rounded score and sufficient flag. It does not deliver `hedgingInstruction` in the inspected JSON confidence field. No host reaction is enforced. Code decides flags and filtering, caller config enables them, model/host decides how to respond. No reference oracle, hard abstention gate or per-result human decision appears in these consumers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: filtered memories/confidence upstream; shared generated text downstream; MCP JSON score metadata on its branch.
- Later read-back: inapplicable — these confidence results/instructions are current-call state, not retained experience.
- Delegated visibility: service model gets conditional hedging instructions and formatted memories; MCP host receives score/flag and selected memories.
- Selection predicate: config.confidenceGate gates filtering and service hedging; MCP requires loaded evaluator and scored memories.
- Invalidation or expiry: results rebuilt each call; filter changes only selected array, not deletion of source rows.
- Activation or effect: cleanup is enforcing on selected evidence; service hedging is advisory for current generation; MCP metadata has no implemented host enforcement.
- Evidence limits: no demonstrated obeyed abstention or reduction in hallucinations; code labels do not calibrate epistemic warrant.

> if (config.confidenceGate) {
>     memories = filterLowConfidenceMemories(memories) as (Memory & { _score: number })[];
>   }
> --- `packages/brain/src/experimental/enhanced-recall.ts`

> const instruction = hedgingInstruction
>     ? `${opts.instruction}\n\n${hedgingInstruction}`
>     : opts.instruction;
> --- `packages/brain/src/services/response.service.ts`

> confidence = { score: Math.round(result.score * 1000) / 1000, sufficient: result.sufficient };
> --- `packages/brain/src/mcp/server.ts`

#### EPI-RTE-memory-mutation
Label: Memory update and deletion
Part of: [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry)

SRC-1 implementation, `packages/brain/src/mcp/server.ts`, `packages/brain/src/memory/memory.ts`. This declares the update/delete material subpath rather than duplicating entry dispatch. MCP selects SQLite/local/hosted/self-hosted handlers. In the directly inspected self-hosted functions, caller patches change content/summary/tags/type/importance or delete an owner-scoped ID. Code truncates/clamps fields; no independent truth criterion or answer oracle is consulted. Caller may be an agent or human; generic tool invocation does not establish authorship. These operations grant row-level revision/withdrawal authority, not proof the old claim was false or the replacement true.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: boolean update/delete result or MCP error JSON.
- Later read-back: changed rows can enter later recall; deleted row no longer supplies its own content from that table.
- Delegated visibility: hosted mode sends ID/patches to HTTP service; self-hosted path updates DB directly.
- Selection predicate: mode dispatch, numeric ID and schema, then self-hosted owner scoping; field presence controls patches.
- Invalidation or expiry: delete is destructive in this body; no automatic versioned rollback, re-embedding or derived-claim invalidation is shown in the inspected self-hosted update/delete functions.
- Activation or effect: row mutation/removal wired; already supplied context and retained derivatives are not retracted by these functions.
- Evidence limits: a no-error DB response is not proof that a row matched; no parity guarantee across mode-specific handlers.

> let query = db.from('memories').delete().eq('id', id);
>   query = scopeToOwner(query);
> --- `packages/brain/src/memory/memory.ts`

> let query = db.from('memories').update(updates).eq('id', id);
>   query = scopeToOwner(query);
> --- `packages/brain/src/memory/memory.ts`

#### EPI-RTE-pack-verification
Label: Pack verification and revocation

SRC-1 implementation, `packages/brain/src/cli/verify.ts`, `packages/memorypack/src/reader.ts`. Distinct from [RT-RTE-pack-import](runtime.md#rt-rte-pack-import), which accepts a different JSON upload and does not imply this verifier gates it. Reader hashes record lines and, when signatures exist, requires verified signatures covering those hashes using supplied/manifest public key. Unsigned records are rejected only in strict-signatures mode. Check target is record-byte/signature/key correspondence, not factual truth, real-world authorship beyond key identity, or useful knowledge. Primitive security is delegated to imported verification functions, whose internals are not inspected here.

CLI consumes reader exceptions as rejection/exit 1; optional chain checks have a separate failure flag and rejection. Reader warnings can coexist with final “Pack is valid.” Thus this status is scoped to configured format/integrity checks. Revocations are separately signature-checked, collected as revoked hashes and exposed for application filtering; bad revocation lines become warnings/rejections of those entries rather than throwing out the whole pack. Retaining revoked records with signatures preserves auditability but does not automatically prevent their use by every importer. This is a source-provenance/withdrawal path, not acceptance of signed propositions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reader records, verification sets, revocation hashes and warnings; CLI diagnostics and exit outcome.
- Later read-back: inapplicable — CLI does not install records into memory here; persisted pack/revocation data can be read by other consumers whose enforcement is unassessed.
- Delegated visibility: optional RPC receives chain verification requests; pack verification otherwise reads local material.
- Selection predicate: requested pack, optional public-key override, strict-signatures and optional chain/strict-chain flags.
- Invalidation or expiry: failed signatures throw; valid revocations expose withdrawal metadata; no global derived-content rollback is shown.
- Activation or effect: exceptions and chain failure enforce CLI failure; revocation force is conditional on application filtering, not universal admission blocking.
- Evidence limits: no chain execution, primitive audit, verified deployment or all-importer propagation established; no answer oracle for content truth.

> if (opts.strictSignatures && unsignedRecords.size > 0) {
>     throw new Error(
>       `MemoryPack: strictSignatures=true but ${unsignedRecords.size} records are unsigned`,
>     );
>   }
> --- `packages/memorypack/src/reader.ts`

> // Soft-delete protocol: revoked records remain in records.jsonl with
>   // their signatures intact. Apps decide what to do with revoked content;
>   // we just expose `revokedRecordHashes` for filtering.
> --- `packages/memorypack/src/reader.ts`

> if (chainFailed) {
>     console.log(`${c.red}REJECTED${c.reset}  Chain verification incomplete.`);
>     process.exit(1);
>   }
> --- `packages/brain/src/cli/verify.ts`

#### EPI-RTE-benchmark-checks
Label: Benchmark judge and revision

SRC-1 implementation, `misc/scripts/longmemeval-benchmark.ts`. No supplied evaluator counterpart after comparison; this is separate from production [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn). The bounded experiment judges generated answers against dataset `q.answer` via an Anthropic judge. Model identifier `claude-sonnet-4-5-20250929` names a remote distributed-parametric evaluator, not an immutable weight digest. No parameter update occurs here; mutable provider resolution and internals remain uninspected.

The judge's target is reference-answer match, with preference-specific generosity and general allowances for paraphrase, partial date match and extra detail. It explicitly prioritizes final answer rather than intermediate reasoning. This is a reference-answer oracle route for the benchmark, not a mechanism verifier, truth oracle for arbitrary memories or universal evidence of recall quality. Text beginning with `1` maps to one; the score and F1 enter per-question results and aggregate statistics. The rejudge mode skips already-correct answers and only flips failures to successes; resulting numbers are not a fresh symmetric re-evaluation of the full set.

A separate optional `--verify` multi-session route asks a model critic to check extracted evidence against proposed answer. Only a verdict beginning REVISE triggers a second generation with critique plus original context; exceptions, empty or non-REVISE verdict preserve the answer. The revised answer is not re-verified in that function. Model criticism can change a candidate, but no supplied execution establishes actual content-directed blame and correction. Error fallback permits continuation, not epistemic acceptance. This evaluator does not gate production chat or dream retention.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: judge 0/1; optional critic/reviser returns revised or original answer; runner aggregates/persists result data.
- Later read-back: saved benchmark results are inputs to rejudge mode; no automatic production-memory or parameter update shown by these consumers.
- Delegated visibility: judge receives question/generated/reference answers; critic receives extracted evidence/question/answer; reviser additionally receives critique and original context.
- Selection predicate: dataset question/type and configured run options; multi-session non-abstention answers with verify enabled; rejudge selects prior failures only.
- Invalidation or expiry: verifier/reviser exceptions fall back to original; rejudge writes modified scoring artifacts rather than versioned production rollback.
- Activation or effect: scores change reported accuracy; critique can replace a benchmark answer before final scoring; no causal benefit observed.
- Evidence limits: no independently authenticated run or ablation, complete evaluator audit, component-effect attribution or transfer to production correctness.

> IMPORTANT: Focus on the FINAL conclusion/answer, not intermediate reasoning. If the generated answer contains reasoning steps but arrives at the correct answer at the end, score "1".
> --- `misc/scripts/longmemeval-benchmark.ts`

> if (!verdict || !/^REVISE/i.test(verdict)) return proposedAnswer;
> --- `misc/scripts/longmemeval-benchmark.ts`

> const correct = await judgeAnswer(generated, goldAnswer, q.question, q.question_type);
>         const f1 = tokenF1(generated, goldAnswer);
> --- `misc/scripts/longmemeval-benchmark.ts`

> if (q.correct === 1) { confirmed++; continue; } // only re-judge failures
> --- `misc/scripts/longmemeval-benchmark.ts`

### Claims

#### EPI-CLM-belief-update
Label: Evidence based belief update

SRC-1 doctrine/design, `packages/brain/src/memory/dream/cycle.ts`. A prompt within contradiction resolution claims genuine evidence-based updating. Distinct narrower claim than [RT-CLM-cognitive-memory](runtime.md#rt-clm-cognitive-memory), not a second declaration of its broad maintenance claim. Implementation supports proposal/storage/decay changes, not demonstrated increased accuracy.

> 'This is not performance — you are genuinely updating your beliefs based on evidence. ' +
> --- `packages/brain/src/memory/dream/cycle.ts`

#### EPI-CLM-action-learning
Label: Closed loop self improvement

SRC-1 doctrine/design, `packages/brain/src/memory/action-learning.ts`. Source describes outcome-responsive rule generation as closed-loop feedback for self-improving agents. Distinct from the cognitive-memory claim's maintenance enumeration; this concerns improvement attribution.

> * Action Learning System — Closed-loop feedback for self-improving agents.
> --- `packages/brain/src/memory/action-learning.ts`

#### EPI-CLM-confidence-gate
Label: Confidence hallucination reduction

SRC-1 doctrine/design, `packages/brain/src/experimental/confidence-gate.ts`. The comment expects reduced hallucinations from weak-evidence hedging. This is an expectation, not an observed result or calibrated probability. No matching supplied claim after comparison with [RT-CLM-cognitive-memory](runtime.md#rt-clm-cognitive-memory).

> * Expected improvement: -30-45% hallucination rate on low-evidence queries.
> --- `packages/brain/src/experimental/confidence-gate.ts`
