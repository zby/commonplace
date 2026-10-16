---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Virtual Context's source warrant, summary and fact checks, actor-card acceptance and consequential consumers at the frozen revision."
run-id: AAS-2026-10-14-virtual-context-bbd06cc3ac95-01
reviewed-boundary: "74ccc570c40bb551820fcd330c42e0dfc0588f05"
---

# Virtual Context epistemic report

## Source-and-claim boundary

The question is what licenses reliance on conversation-derived memory, and which checks actually change later use. Scope, external exclusions and frozen evidence identity are see [boundary](boundary.md#boundary-and-evidence); sources are see [Source register](boundary.md#source-register). All new evidence below is SRC-1 at the registered pin. Direct source reads establish implementation or attributed design, not observed operation. Supplied runtime findings are used where indicated, not treated as an inspection limit.

Conversation testimony is imported evidence of what a participant said, not automatically evidence that the asserted event occurred. Summaries, fact statements, actor-card bodies, drafts and model answers can carry truth-apt content. Tags, counters, rankings and verdict flags instead control selection or disposition. Their names do not make them truth certificates.

| Entry point or operation | Source path | Coverage and limit |
|---|---|---|
| CLI chat, proxy, transform/retrieve/recall, compact, import | SRC-1 `virtual_context/cli/main.py` | Direct dispatch/function search cross-checked against supplied [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat), [RT-RTE-proxy-request](runtime.md#rt-rte-proxy-request), [RT-RTE-import-history](runtime.md#rt-rte-import-history); detailed provider and adapter semantics supplied only. |
| MCP tools, resources and prompts | SRC-1 `virtual_context/mcp/server.py` | Direct exposed-operation search; recall/compact account see [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools). Expansion, quote, temporal search and resource bodies not directly inspected here; prevents all-tool warrant and audience-safety conclusions. |
| OpenClaw hooks and paging tools | SRC-1 `virtual_context/openclaw/virtual-context.mjs`, `virtual_context/core/tool_loop.py` | Supplied [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop); not independently reread. Host consumption and completion delivery remain external. |
| Summary generation, rejection, structured envelopes, tag revalidation | SRC-1 `virtual_context/core/compactor.py`, `virtual_context/core/structured_summary.py` | Direct selected bodies; see [EPI-RTE-summary-check](#epi-rte-summary-check), [EPI-RTE-summary-admission](#epi-rte-summary-admission), [EPI-RTE-structured-materialization](#epi-rte-structured-materialization). Full tag-rollup write/reader loop not audited. |
| Summary-to-model rendering | SRC-1 `virtual_context/core/summary_identity.py`, `virtual_context/core/assembler.py` | Direct render and audience gate bodies; see [EPI-RTE-summary-rendering](#epi-rte-summary-rendering). Counterexample to private-synopsis claim found. |
| Fact proof, rejection, supersession and downstream filtering | SRC-1 `virtual_context/storage/fact_mutations.py`, `virtual_context/core/fact_lifecycle.py`, `virtual_context/core/retrieval_assembler.py` | Direct trust and source-proof bodies, pure supersession policy and filter search; see [EPI-RTE-fact-proof](#epi-rte-fact-proof), [EPI-RTE-fact-withholding](#epi-rte-fact-withholding). Full comparison-model, SQL mutation and refusal-readback loop remains uninspected. |
| Admin record edits and verify/reject/restore | SRC-1 `virtual_context/core/record_editing.py`, `virtual_context/cli/main.py` | Direct function/dispatch search plus supplied [RT-RTE-record-edits](runtime.md#rt-rte-record-edits); host authorization is not a truth evaluator. |
| Actor-card semantic admission, replacement and consumption | SRC-1 `virtual_context/core/community/actor_card_admission.py`, `virtual_context/core/community/actor_card_rebuild.py`, `virtual_context/core/assembler.py` | Direct admission, application and render bodies; see [EPI-RTE-card-check](#epi-rte-card-check), [EPI-RTE-card-integration](#epi-rte-card-integration). Curator generation and complete store serving predicates not independently audited. |
| Engagement drafting/checking/staging | SRC-1 `virtual_context/core/engagement/fidelity.py`, `virtual_context/core/engagement/select.py`, `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py` | Direct fidelity helper, type-dependent disposition, runner acceptance/posting branch and complete posting function; supplied [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage) covers remaining progression. Source-live verifier supplied only; no universal fidelity-veto or draft-truth license. |
| Model-facing wrapper cleanup | SRC-1 `virtual_context/core/render_escape.py`, `virtual_context/core/assembler.py` | Direct deterministic transformations and egress search; see [EPI-RTE-markup-escape](#epi-rte-markup-escape). Canonical replay lane intentionally exempt. |
| LongMemEval judgment and result consumer | SRC-1 `benchmarks/longmemeval/judge.py`, `benchmarks/longmemeval/run.py` | Direct templates, judge/provider branches and result assignment; see [EPI-RTE-answer-scoring](#epi-rte-answer-scoring). No run reproduced or independently authenticated. |
| Other evaluators, repair and maintenance operations | SRC-1 `benchmarks/jev/`, `benchmarks/context_contracts/`, `benchmarks/locomo/`, `benchmarks/beam/`, `benchmarks/mrcr/`, `benchmarks/amb/`, `scripts/`, `virtual_context/cli/main.py` | Available but uninspected bodies, aside from CLI operation searches. Prevents a system-complete negative about evaluators, repair correctness, learning or acceptance routes. |

No registered observed-run or causal-experiment evidence exists. This prevents claims of realized fidelity, reliable model judgment, activated memory, answer-quality benefit, component effects or exercised self-improvement. External model weights, endpoint internals and exact provider artifacts are not inspectable; their mutability findings are see [RT-CMP-chat-provider](runtime.md#rt-cmp-chat-provider), [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider), [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), [RT-CMP-engagement-models](runtime.md#rt-cmp-engagement-models). No parametric-learning conclusion follows from textual retention.

Consequential claims found are [EPI-CLM-record-warrant](#epi-clm-record-warrant), [EPI-CLM-private-synopsis](#epi-clm-private-synopsis) and [EPI-CLM-answer-benefit](#epi-clm-answer-benefit). The source itself acknowledges wrong cached facts. No new explanatory-theory production claim was established.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-summary](#epi-obj-summary) | Synopsis assertions about earlier conversation | see record | SRC-1 `virtual_context/core/compactor.py` | Generated fidelity indeterminate; source retention is not semantic verification. |
| [EPI-OBJ-structured-summary](#epi-obj-structured-summary) | Exact requester statements plus inferred modality/status metadata | see record | SRC-1 `virtual_context/core/compactor.py` | Distinct from synopsis; metadata classifiers not fully traced, and no checked world-truth derivation. |
| [EPI-OBJ-fact](#epi-obj-fact) | Subject/verb/object, status/date and authorship assertions | see record | SRC-1 `virtual_context/storage/fact_mutations.py` | `verified` certifies specified source structure, not statement entailment. |
| [EPI-OBJ-card-entry](#epi-obj-card-entry) | Person-related durable preference, style, goal or history claim | see record | SRC-1 `virtual_context/core/community/actor_card_admission.py` | Acceptance is model-mediated and scoped to supplied evidence. |
| [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state) | None for checkpoint counters/identities | see record | SRC-1 `virtual_context/engine.py` | Selection and recovery authority, not truth endorsement. |
| [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage) | Member-related assertions inside an outward draft; questions need not assert an answer | see record | SRC-1 `virtual_context/core/engagement/fidelity.py` | Assertion/attribution criterion permits presupposition and bot-voice generalization. |
| [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat) | Foreground answer assertions | see record | SRC-1 `virtual_context/tui/headless.py` | Open-mode answers have no demonstrated answer oracle. |

## Authority-route ledger

Each row links the declaring record that owns progression, timing, results and evidence. `implemented` here means inspected source supports the route, never that it operated. The supplied runtime's staging and chat implementations are independently distinguished from missing execution evidence.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-import-history](runtime.md#rt-rte-import-history) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Source warrant unknown through adapters; evidence of imported assertions, not world truth | see record | see record | see record | [EPI-CLM-record-warrant](#epi-clm-record-warrant) | none | Adapter fidelity uninspected. |
| [EPI-RTE-summary-check](#epi-rte-summary-check) | check/evidence production | implemented | [EPI-OBJ-summary](#epi-obj-summary) | no content change | see record | see record | see record | see record | see record | Usability criterion; optional model grounding only, no general entailment proof | see record | see record | see record | [EPI-CLM-record-warrant](#epi-clm-record-warrant) | legacy-grounding-pass | Disabled/failing JEV can use permissive legacy result. |
| [EPI-RTE-summary-admission](#epi-rte-summary-admission) | disposition/acceptance | implemented | [EPI-OBJ-summary](#epi-obj-summary) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Admission for synopsis use, not acceptance of all assertions as knowledge | see record | see record | see record | [EPI-CLM-private-synopsis](#epi-clm-private-synopsis) | synopsis-reaches-model | Successful generated content can lose qualifiers; fallback can truncate. |
| [EPI-RTE-structured-materialization](#epi-rte-structured-materialization) | content transformation | implemented | [EPI-OBJ-structured-summary](#epi-obj-structured-summary) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Exact copied utterance text; added classifier metadata has narrower, unassessed warrant | see record | see record | see record | [EPI-CLM-private-synopsis](#epi-clm-private-synopsis) | none | Applies to claim text; does not certify every metadata inference. |
| [EPI-RTE-summary-rendering](#epi-rte-summary-rendering) | operational admission/selection/consumption | implemented | [EPI-OBJ-summary](#epi-obj-summary) | no content change | see record | see record | see record | see record | see record | Audience compatibility, not semantic grounding | see record | see record | see record | [EPI-CLM-private-synopsis](#epi-clm-private-synopsis) | synopsis-reaches-model | Missing individual rows do not force refusal. |
| [EPI-RTE-fact-proof](#epi-rte-fact-proof) | check/evidence production | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | see record | see record | see record | see record | see record | Complete lineage and specified author proof, not fact entailment | see record | see record | see record | [EPI-CLM-record-warrant](#epi-clm-record-warrant) | verified-is-lineage | A false extracted triple can pass the inspected structural test. |
| [EPI-RTE-fact-withholding](#epi-rte-fact-withholding) | disposition/acceptance | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | see record | see record | see record | see record | see record | Withdrawal is operative; surviving facts are not thereby endorsed | see record | see record | see record | [EPI-CLM-record-warrant](#epi-clm-record-warrant) | none | Human/caller verdict quality unresolved. |
| [EPI-RTE-card-check](#epi-rte-card-check) | check/evidence production | implemented | [EPI-OBJ-card-entry](#epi-obj-card-entry) | no content change | see record | see record | see record | see record | see record | Evidence-consuming semantic judgment for durable person context | see record | see record | see record | none | none | Evaluator reliability unmeasured. |
| [EPI-RTE-card-integration](#epi-rte-card-integration) | lifecycle integration | implemented | [EPI-OBJ-card-entry](#epi-obj-card-entry) | no content change | see record | see record | see record | see record | see record | Accepted entry/source organization, then scoped influence; not world-truth oracle | see record | see record | see record | none | none | Optional and epoch/build-marker constrained; behavior unobserved. |
| [EPI-RTE-markup-escape](#epi-rte-markup-escape) | content transformation | implemented | [EPI-OBJ-summary](#epi-obj-summary) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | No new factual warrant; narrows forged-attribution markup force | see record | see record | see record | none | none | Natural-language obedience and exempt replay not covered. |
| [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage) | operational admission/selection/consumption | implemented | see record | no content change | Draft assertion about member relative to quote | Model/caller fidelity verdict; code applies its veto only to personal outcomes; independent live-identity and staging guards | see record | see record | Personal outcome becomes skip without a faithful verdict; timed outcome bypasses that veto. Runner admits non-skip, nonempty drafts; poster has no independent verdict gate | Attribution check only; not every presupposition or bot assertion is licensed, and admission need not imply a favorable verdict | A negative-verdict timed draft can reach the staging sender when independent posting preconditions pass; default dry-run remains | Runner consumes outcome kind/text, then poster consumes posting intent, live-source proof and staging/day controls; permissive/enforcing code gates to sender and retained day ledger, not universal fidelity enforcement | SRC-1 `virtual_context/core/engagement/fidelity.py`, `virtual_context/core/engagement/select.py`, `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py`; see record | none | entails-docstring-overstates; timed-fidelity-bypass | Supplied drafter can bypass helper; even a returned negative verdict need not veto timed admission. No actual unfaithful staged message or deployment incidence established. |
| [EPI-RTE-answer-scoring](#epi-rte-answer-scoring) | check/evidence production | implemented | [RT-RTE-headless-chat](runtime.md#rt-rte-headless-chat) | no content change | see record | see record | see record | see record | see record | Dataset-answer equivalence under question-type rubric | see record | see record | see record | [EPI-CLM-answer-benefit](#epi-clm-answer-benefit) | none | Score is not runtime acceptance or component causality. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-record-warrant](#epi-clm-record-warrant) | see record | SRC-1 `README.md`; doctrine/design | Source record and explicit cache-error warning | [EPI-RTE-fact-proof](#epi-rte-fact-proof), [EPI-RTE-fact-withholding](#epi-rte-fact-withholding), [RT-RTE-record-edits](runtime.md#rt-rte-record-edits) | None registered | No semantic comparison in inspected trust proof; imported testimony lacks universal world-truth warrant | Retained source lineage and withdrawal can support audit and correction | `verified` is weaker than entailment or world truth; broader reading unwarranted. |
| [EPI-CLM-private-synopsis](#epi-clm-private-synopsis) | see record | SRC-1 `virtual_context/core/compactor.py`; doctrine/design comment | Deterministic structured envelope is implemented separately | [EPI-RTE-structured-materialization](#epi-rte-structured-materialization), [EPI-RTE-summary-rendering](#epi-rte-summary-rendering) | None registered | Renderer chooses stored `.summary` at summary depth after an audience gate; proof-name predicate checks only nonempty string | Generated synopsis has an implemented model-facing path | Source comment is false for inspected ordinary renderer; no runtime record supersession needed because maintenance container did not promise synopsis exclusion. |
| [EPI-CLM-answer-benefit](#epi-clm-answer-benefit) | see record | SRC-1 `README.md`; doctrine/design and reported operation | Named comparison and numbers, not independent run evidence | [EPI-RTE-answer-scoring](#epi-rte-answer-scoring), [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop) | No independently inspected trace | Judge rubrics and model choice bound validity; same reader alone does not identify retrieval, summary or curation effects | Shipped evaluator can grade dataset answers and retain scores | Claimed benefit not independently established; no universal best-context guarantee. |

## Bounded conclusion

Virtual Context acquires conversation assertions and makes retained derivatives consequential through context assembly, paging and record administration. Imported testimony's source warrant is unknown through uninspected adapters; preserved exact utterance text establishes what was said only under trustworthy source identity. The canonical record and provenance checks make correction possible, not automatic truth.

Summary generation is candidate production. Its relation to source meaning remains indeterminate: the inspected implementation neither proves semantic preservation nor establishes a concrete novel proposition as a produced ampliative conjecture. Usability checks and optional grounding can change admission, while permissive legacy grounding and bounded fallback prevent a general fidelity guarantee. Most importantly, ordinary summary rendering admits generated synopsis text after an audience comparison. Deterministic structured envelopes do not impose a universal exact-source-only model interface. This is a concrete counterexample to the compactor's private-synopsis claim, not merely missing execution evidence.

Fact `verified` state is structural lineage/author proof. A full segment mapping can support a mistaken fact triple. Rejected/retracted filtering is an actual withdrawal mechanism, distinct from acceptance of surviving facts. The inspected supersession policy blocks cross-scope, older-evidence and planned-to-observed replacements, but legacy unattributed and unknown-chronology lanes remain deliberately narrower evidence. Full transaction and comparison routes were not audited here. No semantic or world-truth acceptance should be inferred from an admitted supersession edge.

Actor cards provide a different, positive witness: an evidence-consuming acceptance decision with explicit durability, entailment, role, qualifier and revocation criteria for person-context use. Parsed decisions remove rejected immutable candidates; surviving entries are connected to sources and replace the stored card under freshness guards. Optional request-scoped rendering presents those entries as tone, response-preference and relevance guidance, with newer conversation precedence. This supports an implemented semantic acceptance/integration capacity; it does not demonstrate evaluator correctness, activation or improved capacity. Card generation's entailment/ampliation remains unassessed because curator production was not traced.

Engagement has a type-dependent fidelity veto, not universal verdict-controlled staging. In [RT-RTE-engagement-stage](runtime.md#rt-rte-engagement-stage), a negative verdict changes a personal outcome to skip, but a timed outcome bypasses that veto. The runner admits a non-skip, nonempty draft and records its verdict; the poster neither receives nor independently checks that verdict. A negative-verdict timed draft can therefore reach the staging sender if the independent posting, live-source, destination and day controls pass. Default dry-run and staging limits remain; no actual unfaithful staged message or deployment incidence is established. The inspected fidelity helper permits presupposing questions and licenses no general bot-voice truth claim. LongMemEval instead uses an external dataset answer/rubric as oracle for laboratory scoring; that result enters stored benchmark results, not demonstrated runtime knowledge acceptance or behavioral adaptation.

No independently checked derivation from warranted premises to a novel world claim was established. No exercised self-improvement or parametric learning is established. These are separate limits, not system-wide negatives: optional card acceptance, withdrawal, lineage preservation and trace-fed memory maintenance remain supported architectural contributions. Other evaluator and repair bodies remain available but uninspected, preventing exhaustive negative claims about theory criticism, learning or acceptance.

## Shared records

### Operative objects

#### EPI-OBJ-summary
Label: Retrieval synopsis

Source-native identity: `CompactionResult.summary` / stored `.summary`; natural-language propositions in memory and configured content store. It is a material content part of the maintenance route, not a duplicate route or checkpoint.
Part of: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

SRC-1 `virtual_context/core/compactor.py`; evidence passage and consumer are in [EPI-RTE-summary-admission](#epi-rte-summary-admission) and [EPI-RTE-summary-rendering](#epi-rte-summary-rendering).

#### EPI-OBJ-structured-summary
Label: StructuredSummary

Source-native identity: `StructuredSummary.claims`, source digest and metadata; exact natural-language claim text plus symbolic identity, status and modality, held in segment metadata and configured storage. Distinct from [EPI-OBJ-summary](#epi-obj-summary), which can be provider-written synopsis prose.
Part of: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

SRC-1 `virtual_context/core/compactor.py`; passage see [EPI-RTE-structured-materialization](#epi-rte-structured-materialization). This object does not duplicate [RT-OBJ-engine-state](runtime.md#rt-obj-engine-state)'s counters.

#### EPI-OBJ-fact
Label: Fact

Source-native identity: `Fact` content and `trust_state`; mixed natural-language subject/verb/object and symbolic dates, authorship, verdict and supersession fields in relational storage. Distinct content part, not the whole maintenance or admin route.
Part of: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

SRC-1 `virtual_context/storage/fact_mutations.py`; proof and filtering passages see [EPI-RTE-fact-proof](#epi-rte-fact-proof), [EPI-RTE-fact-withholding](#epi-rte-fact-withholding). Admin operations see [RT-RTE-record-edits](runtime.md#rt-rte-record-edits).

#### EPI-OBJ-card-entry
Label: ActorCardEntry

Source-native identity: immutable candidate body and kind, with source links and confidence; natural-language person context plus symbolic evidence references, persisted through `replace_actor_card` in configured store. No counterpart in supplied runtime objects after comparison: this is neither engine checkpoint nor engagement history.

SRC-1 `virtual_context/core/community/actor_card_admission.py`, `virtual_context/core/community/actor_card_rebuild.py`; passages see [EPI-RTE-card-check](#epi-rte-card-check), [EPI-RTE-card-integration](#epi-rte-card-integration).

### Routes

#### EPI-RTE-summary-check
Label: Summary usability check
Part of: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

SRC-1 `virtual_context/core/compactor.py`, `virtual_context/core/judgment.py`, implementation. `_compact_one` sends generated synopsis/source text to `_judged_summary_reject_reason`; code owns the heuristic veto, optionally a configured JEV model judges grounding. Domain: generated synopsis relative to supplied segment, not source truth. Open maintenance mode has no expected-answer oracle; transcript is evidence. Human per-summary review is not required. Check result changes retry/admission in the linked disposition route.

- Immediate return: reason string or `None`.
- Later read-back: inapplicable — check result itself is current-call control; admitted synopsis is read later through the disposition route.
- Delegated visibility: optional grounding evaluator receives summary and source, not whole provider internals.
- Selection predicate: every parsed summary tested for degeneration/overshoot, then optional grounding.
- Invalidation or expiry: new source or generation causes another check; JEV failure invokes legacy.
- Activation or effect: veto causes retry/fallback or fail-closed error in `_compact_one`; observed correctness uninspected.
- Evidence limits: no judge calibration or execution; polarity preservation is prompt guidance, not current lexical enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> grounded = judge_summary_grounding(
>     summary, source_text, legacy=lambda: True, runtime=self.judgment_runtime,
> )
> return None if grounded else "jev_ungrounded"
> --- `virtual_context/core/compactor.py`

> if not rt.enabled_for(seam):
>     return legacy()
> --- `virtual_context/core/judgment.py`

> if outcome is None or outcome.fallback_reason:
>     reason = outcome.fallback_reason if outcome else "jev_unavailable"
>     logger.warning("JUDGMENT_FALLBACK seam=%s reason=%s", seam, reason)
>     return legacy()
> --- `virtual_context/core/judgment.py`

#### EPI-RTE-summary-admission
Label: Summary retry and admission
Part of: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

SRC-1 `virtual_context/core/compactor.py`, implementation. Code consumes the preceding check, retries once, then either throws in fail-closed mode or substitutes a bounded source slice. Model proposes text; software decides/vetoes. Intended use is retained retrieval synopsis. Retry instruction requests faithful segment-only meaning; no evidence-consuming general acceptance of all synopsis assertions is established. Later replacement/rebuild is recovery, not semantic rollback proof. Persistence endpoints are supplied by the parent maintenance record.

- Immediate return: `CompactionResult` or raised generation error.
- Later read-back: admitted synopsis is stored through maintenance and selected by model-facing renderer.
- Delegated visibility: model sees constructed prompt and retry instruction, not direct write access.
- Selection predicate: generated parsed text passing checks, or fallback under non-fail-closed failure.
- Invalidation or expiry: rebuild/recompaction can replace derivatives; fail-closed mode propagates failure.
- Activation or effect: changes future-consumable text, not demonstrated answer behavior.
- Evidence limits: lossy fallback slicing can drop qualifiers; generated semantic preservation or novelty not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> except Exception as e:
>     if fail_closed:
>         raise
>     logger.warning(f"LLM summarization failed for segment {segment.id}: {e}")
>     parsed = {
>         "summary": conversation_text[:target_tokens * 4],
>         "entities": [],
>         "key_decisions": [],
>         "action_items": [],
>         "date_references": [],
>         "refined_tags": segment.tags,
>     }
> --- `virtual_context/core/compactor.py`

#### EPI-RTE-structured-materialization
Label: Deterministic claim materialization
Part of: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance)

SRC-1 `virtual_context/core/compactor.py`, implementation. `_build_structured_summary` ignores provider `parsed` content and constructs exact requester claims from physical roster lanes with canonical IDs, audience proof and bounds. Code owns membership and order, with optional safety classification. Exact-copy claim text is non-ampliative; inferred temporal/modality labels are a separate uncertainty, not warranted by copying alone. No expected-answer oracle; source is evidentiary input.

- Immediate return: digest-bound `StructuredSummary`, possibly empty.
- Later read-back: envelope persists in derivative metadata; inspected tag-rollup validation compares exact text and provenance; complete renderer consumption of envelope unestablished.
- Delegated visibility: requester lanes and metadata, not unrestricted transcript or model weights.
- Selection predicate: whole exact lane within evidence bound, canonical membership and current audience attribution; overflow/internal identities can empty claims.
- Invalidation or expiry: source digest/provenance revalidation can invalidate tag-rollup inputs.
- Activation or effect: deterministic retained envelope construction, with safety-critical text ordered first; downstream behavioral compliance unobserved.
- Evidence limits: exact-copy warrant is about utterance lineage, not world truth; optional metadata-classifier reliability uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _ = parsed
> requester_lanes = _structured_requester_lanes(roster)
> --- `virtual_context/core/compactor.py`

> claims_by_source_index.append((source_index, SummaryClaim(
>     text=canonical_evidence,
>     claim_type="conversation",
>     temporal_status=infer_temporal_status(canonical_evidence),
>     modality=infer_modality(canonical_evidence),
>     event_time="",
>     sources=(source,),
> )))
> --- `virtual_context/core/compactor.py`

#### EPI-RTE-summary-rendering
Label: Stored summary rendering

Distinct operational consumer spanning maintenance and answer delivery, rather than duplicate of [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance) or [RT-BAP-assembled-context](runtime.md#rt-bap-assembled-context). SRC-1 `virtual_context/core/summary_identity.py`, `virtual_context/core/assembler.py`, implementation. Renderer loads canonical rows and code compares proved row audience against request audience; absent individual rows/unstamped provenance do not set `foreign`. A failed batch read with sourced IDs withholds; an unsourced item can pass. This is not a completeness/semantic validator. At normal summary depth the consumer receives stored synopsis, not automatically the deterministic claims. Code controls delivery; later model interprets it as guidance/evidence during the current invocation.

- Immediate return: stored summary/full text or quarantine marker.
- Later read-back: reads retained derivatives produced by earlier maintenance invocations into later model calls.
- Delegated visibility: selected depth text with wrapper/tag context, not guaranteed complete canonical evidence.
- Selection predicate: audience comparison then nonempty text; assembler invokes `render_summaries_for_model` or consumes rendered candidates.
- Invalidation or expiry: each render can reread source rows; missing individual rows do not force failure; caller result expiry uninspected.
- Activation or effect: implements context admission, not semantic reliance or observed model compliance.
- Evidence limits: ordinary path contradicts private-synopsis doctrine; no proof that all tools use identical gate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> summary = getattr(item, "summary", None)
> return summary if isinstance(summary, str) else ""
> --- `virtual_context/core/summary_identity.py`

> for (item, depth), ok in zip(materialized, admitted, strict=True):
>     text = _text_for_depth(item, depth if depth in _DEPTHS else "summary")
>     rendered.append(text if ok and text.strip() else SUMMARY_ATTRIBUTION_QUARANTINE)
> --- `virtual_context/core/summary_identity.py`

> row = rows.get((conversation_id, source_id))
> if row is None:
>     continue
> --- `virtual_context/core/summary_identity.py`

> return isinstance(text, str) and bool(text.strip()) and text != SUMMARY_ATTRIBUTION_QUARANTINE
> --- `virtual_context/core/summary_identity.py`

#### EPI-RTE-fact-proof
Label: Fact trust refresh
Part of: [RT-RTE-record-edits](runtime.md#rt-rte-record-edits)

SRC-1 `virtual_context/storage/fact_mutations.py`, implementation. `refresh_fact_trust` queries active nonretracted facts and derives trust state from latest rejection verdict or `_fact_sources`. Source check requires complete canonical mapping and rows; where required it reproves human author. No predicate compares subject/verb/object meaning against source text. Evaluator is program over physical lineage and author identity, not a model or world oracle. Code writes operational state; admin verify is an explicit trigger, also used by lifecycle operations. This is a distinct check part, not a duplicate of admin edit/rebuild container.

- Immediate return: counts by verified/unverified/rejected state.
- Later read-back: persisted trust state affects later retrieval and supersession selection.
- Delegated visibility: exact physical rows and segment metadata used internally; no disclosure grant from this check alone.
- Selection predicate: current facts in requested segment refs, excluding superseded and retracted rows.
- Invalidation or expiry: changed source/editor verdict or rebuild can change trust; retracted rows cannot be restored by this refresh alone.
- Activation or effect: stores trust flags; structural `verified` can coexist with semantically mistaken statement.
- Evidence limits: author helper directly inspected, complete backend transaction/consumer coverage not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> human_claim = fact.author_source_role not in ("unattributed", "assistant")
> sources = self._fact_sources(conn, fact, require_author=human_claim)
> state = "verified" if sources else "unverified"
> --- `virtual_context/storage/fact_mutations.py`

> if len(rows) != len(ids):
>     return ()
> from ..core.fact_lifecycle import source_author_matches
>
> if require_author and not source_author_matches(fact, [dict(row) for row in rows]):
>     return ()
> --- `virtual_context/storage/fact_mutations.py`

#### EPI-RTE-fact-withholding
Label: Fact trust withholding
Part of: [RT-RTE-record-edits](runtime.md#rt-rte-record-edits)

SRC-1 `virtual_context/core/fact_lifecycle.py`, `virtual_context/core/retrieval_assembler.py`, implementation. Admin/caller rejection and source retraction change operational eligibility. `servable_facts` withholds forbidden trust states before audience selection in inbound fact assembly. This is disposition, distinct from check producing state. No positive epistemic acceptance is conferred by non-withholding. Host chooses who can edit/reject; supplied [RT-RTE-record-edits](runtime.md#rt-rte-record-edits) records exact change, reason, restore and rebuild. Human identity behind generic caller remains unresolved; no answer oracle.

- Immediate return: filtered fact list.
- Later read-back: later inbound assembly reads retained flags and excludes withdrawn facts.
- Delegated visibility: consumer gets surviving facts after filtering, not merely a warning asking it to ignore rejected facts.
- Selection predicate: trust state not in `WITHHELD_TRUST_STATES` then audience eligibility.
- Invalidation or expiry: restore can lift rejection; rebuild replaces retracted derivatives; no automatic semantic proof results.
- Activation or effect: code-enforced withholding at inspected assembly consumer; no observed answer change.
- Evidence limits: other quote/time/fact tools not independently traced here; docs claim wider coverage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return [fact for fact in facts if getattr(fact, "trust_state", "") not in WITHHELD_TRUST_STATES]
> --- `virtual_context/core/fact_lifecycle.py`

The pure supersession policy is an additional bounded countercase against treating latest-date selection as unconditional authority:

> if new.status == "planned" and old.status != "planned":
>     return reject("plan_is_not_observed_outcome")
> --- `virtual_context/core/fact_lifecycle.py`

> reason = "proved_source_scope" if attributed else "legacy_unattributed"
> if new_date is None or old_date is None:
>     reason += ":unknown_chronology"
> return AdmissionDecision(True, reason)
> --- `virtual_context/core/fact_lifecycle.py`

#### EPI-RTE-card-check
Label: Actor card semantic check

SRC-1 `virtual_context/core/community/actor_card_admission.py`, implementation plus model-directed criteria. No supplied record counterpart: [RT-RTE-memory-maintenance](runtime.md#rt-rte-memory-maintenance) describes ordinary tags/summary writes, not this actor-specific admission service. `admit_entries` checks evidence availability then supplies immutable fresh/existing candidates, source turns/segments and compact facts to an independent admission evaluator. Code parses exact decisions and discards vetoed candidates; provider/JEV proposes judgments, fallback can adjudicate coverage. Criterion is durable, source-entailed, correctly scoped person-context use, retaining material qualifiers and respecting later revocation. No expected-answer oracle; source evidence and policy provide criterion. Trigger is actor-card rebuild, not every user answer. Basic parsing is not semantic truth proof.

- Immediate return: admitted entries, raw response, rejection counts and independently substantive flag.
- Later read-back: accepted entries feed replacement and later card assembly in integration route; raw response retained in rebuild reporting/hash path, not shown as accepted knowledge.
- Delegated visibility: bounded source evidence and candidates; truncated/unavailable required evidence causes exclusion.
- Selection predicate: eligible candidate IDs, exact schema decisions, then `admit` true; non-substantive with admitted entries errors.
- Invalidation or expiry: existing entries are rejudged under current criteria; errors/fallback can stop admission.
- Activation or effect: semantic decision controls candidate membership; reliability not measured.
- Evidence limits: provider roles can share model weights; independence of call role is not independent errors; production activation unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "preference) is omitted. The body must be fully entailed by the "
> "cited actor-authored messages and their supplied paired agent "
> "replies, with each participant's role preserved. "
> --- `virtual_context/core/community/actor_card_admission.py`

> if not decision["admit"]:
>     rejection_counts[f"semantic_{decision['reason']}"] += 1
>     continue
> admitted.append((entry, entry_sources))
> --- `virtual_context/core/community/actor_card_admission.py`

#### EPI-RTE-card-integration
Label: Actor card replacement and use

Distinct downstream organization/consumer of [EPI-RTE-card-check](#epi-rte-card-check), without supplied runtime counterpart. SRC-1 `virtual_context/core/community/actor_card_rebuild.py`, `virtual_context/core/assembler.py`, implementation. Accepted entries stay linked to sources; code calibrates confidence and replaces card under source epochs/build marker. Failure aborts; a valid empty accepted set can clear card state. Store replacement combines retention with source-linked lifecycle integration after semantic acceptance. Later optional assembly requires known requester and a store card scoped to audience. Whole lowest-confidence entries drop under budget. Model receives guidance for preferences, register and relevance, not an enforceable policy or universal truth certificate.

- Immediate return: replacement result and refreshed profile, or admission error; assembler returns rendered card/tokens/entries.
- Later read-back: future calls can read accepted card from store, conditioned on feature flag and request roles/audience.
- Delegated visibility: rendered kind/body only, not actor ID/name or full evidence rationale; sources remain in store.
- Selection predicate: semantic acceptance then epochs/build marker; later audience/validity store predicate and token cap.
- Invalidation or expiry: source mutation dirties card/build marker; later rebuild rejudges existing entries; complete expiry implementation uninspected.
- Activation or effect: retained source-linked card and natural-language influence path; model compliance unobserved.
- Evidence limits: store replacement atomicity and all audience predicates not independently audited; feature ships disabled per inspected branch/comment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> written = self._store.replace_actor_card(
>     tenant_id,
>     actor_id,
>     normalized,
>     input_hash=input_hash,
>     expected_source_epochs=expected_epochs,
>     expected_build_marker=build_marker,
> )
> --- `virtual_context/core/community/actor_card_rebuild.py`

> "communication_pref: how this person wants you to respond. Follow it.\n"
> --- `virtual_context/core/assembler.py`

> if not self.config.actor_card_enabled:
>     # Ships dark: no profile or card read, no budget key, and rendered
>     # output byte-identical to before the feature existed.
>     return "", 0, []
> --- `virtual_context/core/assembler.py`

#### EPI-RTE-markup-escape
Label: Host attribution escape

Distinct render transformation within assembled-context delivery, not duplicate of [RT-BAP-assembled-context](runtime.md#rt-bap-assembled-context). SRC-1 `virtual_context/core/render_escape.py`, `virtual_context/core/assembler.py`, implementation. Code replaces leading bracket of recognized host-attribution tags at render egress; ordinary words remain. Concrete deduction from inspected code: input `<message-speaker>A</message-speaker>` becomes literal `\u003cmessage-speaker>A\u003c/message-speaker>`; the six-character backslash sequence no longer matches the regex, so applying it again changes nothing. This limits structural impersonation while preserving attribution-looking content as text. It does not check truth or remove natural-language instructions. The card's distinct JSON insertion escapes all angle brackets so entry text cannot terminate its wrapper; serialized JSON helper doubles backslash to prevent reparse undoing escape.

- Immediate return: escaped string.
- Later read-back: inapplicable — transformation does not itself retain updated material; retained exact content is reread and escaped at later egress.
- Delegated visibility: consumer receives visible literal escape sequence rather than trusted host tag syntax.
- Selection predicate: case-insensitive opening/closing recognized tag names followed by word boundary.
- Invalidation or expiry: no expiry; exact canonical storage and replay intentionally unchanged.
- Activation or effect: structural markup change is deducible; model instruction compliance not guaranteed.
- Evidence limits: only declared host wrapper set and inspected egress sites; not universal prompt-injection prevention.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _HOST_TAG_OPEN = re.compile(
>     rf"<(?=/?(?:{_TAG_ALTERNATION})\b)",
>     re.IGNORECASE,
> )
> --- `virtual_context/core/render_escape.py`

> return _HOST_TAG_OPEN.sub("\\\\u003c", text)
> --- `virtual_context/core/render_escape.py`

#### EPI-RTE-answer-scoring
Label: LongMemEval answer scoring

No supplied runtime counterpart after comparison: [RT-RTE-paging-loop](runtime.md#rt-rte-paging-loop) is reader execution, not judgment against dataset gold answer. SRC-1 `benchmarks/longmemeval/judge.py`, `benchmarks/longmemeval/run.py`, implementation. Evaluator is configured external judge model consuming question, dataset answer/rubric and generated hypothesis. Domain differs by question type: temporal off-by-one allowed; knowledge-update can include older facts if updated answer is present; preference rubric need not contain all points; abstention checks recognition of incomplete/unanswerable question. Code parses yes/no and vote result into result record. This is laboratory score, not acceptance of retained claim for runtime use; no product update consumer traced.

- Immediate return: correctness boolean, judge explanation and cost; runner adds vote metadata.
- Later read-back: result entries written to report JSON and summarized; live engine-policy consumption unestablished.
- Delegated visibility: judge sees gold answer/rubric and hypothesis; reader oracle visibility not independently audited here.
- Selection predicate: question type chooses rubric; configured judge/vote mode chooses score.
- Invalidation or expiry: rerun/rejudge can change result; no automatic runtime rollback.
- Activation or effect: runner assigns score/explanation to `vc_result` and reports benchmark result; no demonstrated behavioral adaptation.
- Evidence limits: judge reliability, actual datasets/run conditions and causal component contrasts uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "In addition, do not penalize off-by-one errors for the number of days. "
> --- `benchmarks/longmemeval/judge.py`

> vc_result["correct"] = vc_judge["correct"]
> vc_result["judge_explanation"] = vc_judge["explanation"]
> --- `benchmarks/longmemeval/run.py`

### Claims

#### EPI-CLM-record-warrant
Label: Conversation record warrant

SRC-1 `README.md`, doctrine/design. A fact is a cached assertion and source record is priority evidence; this claim is distinct from [RT-CLM-compaction-fence](runtime.md#rt-clm-compaction-fence)'s write-ownership guarantee. Broader reading as semantic/world verification is challenged by structural trust checks and source's own cache-error qualification.

> So a fact is not a final answer. It is a cached copy of something that was said, telling the model what it can assume and where the full discussion lives.
> --- `README.md`

> When a cached fact and the conversation disagree, the conversation wins, and it is always one page-in away.
> --- `README.md`

#### EPI-CLM-private-synopsis
Label: Private retrieval synopsis

SRC-1 `virtual_context/core/compactor.py`, doctrine/design comment. Distinct from supplied fence claim; semantic consumer exclusion is its load-bearing promise. Counterexample see [EPI-RTE-summary-rendering](#epi-rte-summary-rendering).

> # ``summary`` is deliberately retained as a lossy retrieval synopsis,
> # including for multi-human groups. It is never admitted to an answer
> # prompt directly. Claim-local source validation, not segment-wide
> # roster cardinality, controls model-visible summary presentation.
> --- `virtual_context/core/compactor.py`

#### EPI-CLM-answer-benefit
Label: Focused context benefit

SRC-1 `README.md`, doctrine/design plus attributed reported benchmark operation, not observed-run evidence. Distinct from supplied write-fence claim.

> - **Better answers from less context.** A focused window of relevant summaries and facts beats a raw window of everything, where the one fact you need is buried.
> --- `README.md`

> On 100 questions from [LongMemEval-500](https://github.com/xiaowu0162/LongMemEval), with the same reader model (Claude Sonnet 4.5):
> --- `README.md`

### Behavioral-authority paths

#### EPI-BAP-card-influence
Label: Actor card influence

Consumer: answer model. Channel: actor-card wrapper inside assembled model context. Force: advisory preference/register/relevance instructions, not code-enforced truth or compliance. Horizon: current invocation and future invocations reading accepted card. SRC-1 `virtual_context/core/assembler.py`; passage see [EPI-RTE-card-integration](#epi-rte-card-integration). This specializes [RT-BAP-assembled-context](runtime.md#rt-bap-assembled-context)'s delivery channel with a distinct optional retained part; it does not replace that container.

Additional evidence for assessing supplied engagement route (not a duplicate declaration):

> It deliberately does NOT judge entailment.
> --- `virtual_context/core/engagement/fidelity.py`

> if "asserts" in raw:
>     asserts = raw.get("asserts")
>     if not isinstance(asserts, bool):
>         return FidelityVerdict(False, "unreadable_verdict")
>     return FidelityVerdict(not asserts, reason if asserts else "")
> --- `virtual_context/core/engagement/fidelity.py`

> if not post or outcome.kind == "skip":
>     return RunResult(report=report, rejections=rejections,
>                      refused="" if post else "dry_run")
> --- `virtual_context/core/engagement/runner.py`
