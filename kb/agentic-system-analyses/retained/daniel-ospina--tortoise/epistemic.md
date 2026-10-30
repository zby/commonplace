---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Tortoise epistemic routes: extraction, source addressing, belief-based selection and correction review, with partial-loop limits."
run-id: AAS-2026-10-30-tortoise-0c919b4ca77d-01
reviewed-boundary: "54922a800f96858935b58ef250da569a4896df44"
---

# Tortoise epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on Tortoise's extracted and retrieved claims. It retains the complete-artifact, partial-loop scope and external exclusions of [boundary](boundary.md#boundary-and-evidence), using its [Source register](boundary.md#source-register). All source evidence below is SRC-1 at the frozen commit. Direct reads add selected implementation and doctrine/design evidence; they add no observed operation or causal experiment. No target code was executed.

The assessed routes are conversation import/extraction, candidate vetting and source-span checks, belief computation/write-back, correction-conflict review, withdrawal, and graph-to-context selection. The consequential public claims are [EPI-CLM-evidence-authority](#epi-clm-evidence-authority) and [EPI-CLM-belief-propagation](#epi-clm-belief-propagation). These are claims to compare with routes, not premises establishing their success.

| Entry point or operation | Source path, SRC-1 | Coverage and evidence basis | Remaining limit / conclusion prevented |
|---|---|---|---|
| SDK and hosted capture, direct Point, production commit | `tortoise/sdk.py`, `tortoise/hosted_api.py`, `tortoise/mcp_server.py` | Supplied [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-hosted-capture](runtime.md#rt-rte-hosted-capture), [RT-RTE-direct-point](runtime.md#rt-rte-direct-point), [RT-RTE-production-commit](runtime.md#rt-rte-production-commit); direct reads of v2 payload and promotion parts | M2, v1 and complete remote commit consumer uninspected; no universal extraction or admission conclusion |
| v2 source addressing and VET | `tortoise/extractor_v2.py`, `tortoise/vet_gate.py`, `tortoise/value_gate.py` | Direct reads; [EPI-RTE-source-address](#epi-rte-source-address), [EPI-RTE-vet-check](#epi-rte-vet-check), [EPI-RTE-vet-disposition](#epi-rte-vet-disposition) | Semantic arbiter internals and all consolidation branches uninspected; no general factual-validity guarantee |
| Registered maintenance/review tools | `tortoise/tool_registry.py`, `tortoise/mcp_server.py` | Direct registry and handler reads for promotion, confidence, baseline, calibration audit and dream; SDK promotion/retraction reads | Tool registration is not deployment or execution; dream tenant MCP exclusion differs from REST availability |
| Belief evaluation/write-back | `tortoise/ep.py`, `tortoise/dream.py`, `tortoise/sdk.py`, `tortoise/volunteer.py` | Direct selected score, batch write-back and gate reads; [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate), [EPI-RTE-belief-retain](#epi-rte-belief-retain) | Full propagation mathematics and calibration-data provenance uninspected; no empirically calibrated truth-probability conclusion |
| Mining correction review | `tortoise/mining.py`, `tortoise/review_verdicts.py`, `tortoise/sdk.py` | Direct sweep caller, verdict layer and promotion-tail reads; [EPI-RTE-review-disposition](#epi-rte-review-disposition), [EPI-RTE-review-integration](#epi-rte-review-integration) | Mining's separate batch grounding gate only located/read at call site; its complete evaluator is uninspected, preventing a full mining-safety verdict |
| Explicit withdrawal | `tortoise/sdk.py` | Direct retraction entry, mutation and invalidation tail; [EPI-RTE-point-withdrawal](#epi-rte-point-withdrawal) | Not all deletion, supersession, replay and concurrent failure branches inspected |
| Framework, CLI and hook context | `tortoise/framework.py`, `tortoise/volunteer.py`, `tortoise/__main__.py`, `tortoise/claude-hooks/volunteer-turn.sh`, `tortoise/claude-hooks/CLAUDE.tortoise.md` | Supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); direct confidence gate, CLI output and hook emission reads; [EPI-RTE-hook-context](#epi-rte-hook-context) | Other harnesses, session-start and reinjection consumers not fully inspected; no cross-harness parity or host compliance conclusion |
| Evaluation tooling | `tools/longmem_eval/judge.py`, `tools/longmem_eval/run.py` | Direct answer-check prompt/parser read and bounded runner search; reference-answer comparison exists as tooling | Complete scoring/aggregation consumer and committed outcomes uninspected; not used as an operative graph acceptance criterion or measured-benefit result |
| Other maintenance, imports and consumers | Packs, ingest variants, dream scheduler drivers, backups/rebuild, UI/dashboard and other hook/plugins named in boundary | Available but not traced end-to-end | Prevents a system-complete negative about acceptance, knowledge production, learning or self-improvement |

No missing execution evidence is treated as proof that an implemented route never runs. No model-provider internals are accessible in this boundary; distributed-parametric conclusions remain those of [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). No single score follows from the inspected heterogeneous routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-extracted-points](#epi-obj-extracted-points) | see record | see record | SRC-1, `tortoise/extractor_v2.py` | see record |
| [EPI-OBJ-belief-state](#epi-obj-belief-state) | see record | see record | SRC-1, `tortoise/ep.py` | see record |
| [EPI-OBJ-review-verdict](#epi-obj-review-verdict) | see record | see record | SRC-1, `tortoise/review_verdicts.py` | see record |
| [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission) | see record | see record | SRC-1, `tortoise/sdk.py` | see record |
| [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model) | see record | see record | SRC-1, `tortoise/model_adapters.py` | see record |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) | see record | see record | SRC-1, `tortoise/embeddings.py` | see record |

## Authority-route ledger

The compact entries distinguish computation of a result from its disposition, and retention from post-decision integration. “See record” delegates owned factual fields rather than silently treating a live status or confidence number as acceptance.

Route ID: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: conversation to extracted claims; see record.
Evaluator/condition and domain: model extraction, not an external truth oracle; see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: imports conversation assertions with unknown source warrant; the model's restatement, interpretation and reference completion do not establish entailment or acceptance.
Operational authority: see record.
Behavioral-authority path: see record and [RT-BAP-framework-block](runtime.md#rt-bap-framework-block).
Evidence source ID and local anchor: SRC-1, `tortoise/extractor_v2.py`.
Claim IDs: [EPI-CLM-evidence-authority](#epi-clm-evidence-authority).
Mismatch marker: source addressing is conditional, not universal.
Gap/limit: no paired execution establishes which generated claims preserve meaning, derive or conjecture beyond input. Non-entailment is not inferred merely from a model call.

Route ID: [EPI-RTE-source-address](#epi-rte-source-address)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: no content change
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: localized textual occurrence only; not truth or entailment of the Point.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/extractor_v2.py`.
Claim IDs: [EPI-CLM-evidence-authority](#epi-clm-evidence-authority).
Mismatch marker: warnings can accompany admitted, spanless claims.
Gap/limit: see record.

Route ID: [EPI-RTE-vet-check](#epi-rte-vet-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: no content change
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: identifier-shape policy or supplied arbiter opinion; not factual corroboration.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/vet_gate.py`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: see record.

Route ID: [EPI-RTE-vet-disposition](#epi-rte-vet-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: non-truth-apt policy/content update: candidate membership and dependency repair
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: eligibility for payload, not evidence-consuming acceptance of a true claim.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/vet_gate.py`.
Claim IDs: none.
Mismatch marker: a DISCARD result need not remove a referenced entity.
Gap/limit: see record.

Route ID: [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-belief-state](#epi-obj-belief-state)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: score arithmetic from stored parameters, conditional on their values; not derivation of the underlying claim's truth.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/ep.py`.
Claim IDs: [EPI-CLM-belief-propagation](#epi-clm-belief-propagation).
Mismatch marker: a baseline can be operationally sufficient without measurement.
Gap/limit: see record.

Route ID: [EPI-RTE-belief-retain](#epi-rte-belief-retain)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-belief-state](#epi-obj-belief-state)
Content/update relation: no content change
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: persists evaluation state, not an acceptance decision.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/dream.py`.
Claim IDs: [EPI-CLM-belief-propagation](#epi-clm-belief-propagation).
Mismatch marker: freshness/convergence is not factual endorsement.
Gap/limit: see record.

Route ID: [EPI-RTE-review-disposition](#epi-rte-review-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-review-verdict](#epi-obj-review-verdict)
Content/update relation: non-truth-apt policy/content update: correction decision and lifecycle status
Transition or check target: see record.
Evaluator/condition and domain: see record and [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate).
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: opt-in acceptance against EP threshold for graph correction use, not independently corroborated factual acceptance; explicit verdicts need not consume stated evidence.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/review_verdicts.py`.
Claim IDs: none.
Mismatch marker: even an unmeasured neutral value can clear a lowered threshold.
Gap/limit: see record.

Route ID: [EPI-RTE-review-integration](#epi-rte-review-integration)
Route function: lifecycle integration
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: non-truth-apt policy/content update: post-keep graph relations and successor eligibility
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: connects operationally accepted correction to priors; edge labels do not prove implication or contradiction.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/sdk.py`.
Claim IDs: [EPI-CLM-evidence-authority](#epi-clm-evidence-authority).
Mismatch marker: partial promotion can leave supersession unapplied.
Gap/limit: explicit keep without an evidence-consuming criterion establishes operational admission, not epistemic acceptance; integration naming here refers to the threshold-acceptance branch.

Route ID: [EPI-RTE-point-withdrawal](#epi-rte-point-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: non-truth-apt policy/content update: withdraw reliance and invalidate propagation messages
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: records withdrawal; no automatic demonstration of falsity.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/sdk.py`.
Claim IDs: none.
Mismatch marker: journal-first ordering is not confirmed durable append.
Gap/limit: see record.

Route ID: [RT-RTE-direct-point](runtime.md#rt-rte-direct-point)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: external content with unknown source warrant; kind/shape validation is not truth acceptance.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/sdk.py`.
Claim IDs: [EPI-CLM-evidence-authority](#epi-clm-evidence-authority).
Mismatch marker: direct writes need not carry extracted source evidence.
Gap/limit: see record; object reference denotes the Point family, not proof all direct writes came from extraction.

Route ID: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see record.
Evaluator/condition and domain: see record and [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate).
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: selection of stored snippets/pointers, not new factual warrant; claim scope remains source-dependent.
Operational authority: see record.
Behavioral-authority path: [RT-BAP-framework-block](runtime.md#rt-bap-framework-block).
Evidence source ID and local anchor: SRC-1, `tortoise/volunteer.py`.
Claim IDs: none.
Mismatch marker: confidence gate is not a measured-truth gate.
Gap/limit: reshaping classification applies to selection/packaging, not a proof that all graph content or host answers preserve truth.

Route ID: [EPI-RTE-hook-context](#epi-rte-hook-context)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-extracted-points](#epi-obj-extracted-points)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: advisory prior context, not enforced truth.
Operational authority: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `tortoise/claude-hooks/volunteer-turn.sh`.
Claim IDs: none.
Mismatch marker: unknown-harness plain stdout is not established model injection.
Gap/limit: see record.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-evidence-authority](#epi-clm-evidence-authority) | see record | SRC-1, `README.md`, doctrine/design | see record | [EPI-RTE-source-address](#epi-rte-source-address), [RT-RTE-direct-point](runtime.md#rt-rte-direct-point), [EPI-RTE-review-integration](#epi-rte-review-integration) | none established | see records | Addressable evidence is supported conditionally, not for every admitted Point | Source-span failures warn rather than universally reject; quotation presence does not establish claim entailment |
| [EPI-CLM-belief-propagation](#epi-clm-belief-propagation) | see record | SRC-1, `README.md`, doctrine/design | see record | [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate), [EPI-RTE-belief-retain](#epi-rte-belief-retain) | none established | see records | Computed numerical belief state has downstream selection force | Parameter provenance, calibration validity and graph-edge semantics not independently validated |

## Bounded conclusion

Tortoise can retain conversation assertions and model-produced Points, attach evidence addresses, compute and persist belief numbers, change correction status and deliver selected prior text to a later model. These are separate capabilities with separate authorities: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [EPI-RTE-source-address](#epi-rte-source-address), [EPI-RTE-belief-retain](#epi-rte-belief-retain), [EPI-RTE-review-disposition](#epi-rte-review-disposition), [RT-BAP-framework-block](runtime.md#rt-bap-framework-block).

Import preserves access to some source material, not its truth warrant. The extraction-to-Point relation remains indeterminate without paired claim/input assessment. A textual span check establishes occurrence, and only conditionally supplies a value-bearing address. A numeric mean follows from its stored Beta parameters; no derivation of the underlying proposition's truth follows. Identifier filtering curates candidates, not knowledge. These distinctions survive the counterexamples of spanless payload admission, direct live writes, referenced-entity restoration and baseline-only volunteering ([EPI-RTE-source-address](#epi-rte-source-address), [EPI-RTE-vet-disposition](#epi-rte-vet-disposition), [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate), [RT-RTE-direct-point](runtime.md#rt-rte-direct-point)).

There is an implemented, opt-in correction acceptance criterion: EP mean at or above the configured threshold, default 0.75, subject to promotion eligibility. Its intended use is graph correction-conflict admission, not an independent truth certification. Default operation queues instead. An explicit keep/reject/close can resolve a candidate, but caller identity does not establish human review or evidence consumption. A keep can connect priors and alter subsequent graph use; rejection of a live candidate tombstones it and invalidates its propagation messages. These are operative reliance changes with partial-failure limits, not merely unused critic reports ([EPI-RTE-review-disposition](#epi-rte-review-disposition), [EPI-RTE-review-integration](#epi-rte-review-integration), [EPI-RTE-point-withdrawal](#epi-rte-point-withdrawal)).

The later consumer receives selected text, not the whole graph or a proof. Confidence changes can change eligibility; natural-language context can then shape host behavior without another Tortoise truth check. Delivery remains distinct from demonstrated use. The inspected routes do not establish a produced, accepted ampliative claim, demonstrated learning benefit, exercised self-improvement, or a complete theory-builder loop. Those properties are independently unestablished here, not jointly absent: automatic retention and correction do not imply improved capacity, model opacity does not imply no criticism, and uninspected shipped routes prevent a universal negative. No distributed-parametric update or provider-side learning conclusion follows from graph changes ([RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model)).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-extracted-points
Label: Extracted Point payload parts

Source-native identity: `execute_embed` payload Points, including natural-language `content` and `quote`, symbolic kind/status/source-turn/span fields, and initial numerical confidence fields. Substrates are transient payload dictionaries and, through SDK capture, retained graph/journal surfaces. Truth-apt content consists of asserted state, event or decision statements about the transcript's subject matter; a quote can also support the narrower claim that the source said something. Unknown source truth is not repaired by extraction. Metadata and numbers are not interchangeable with the statement text. Closest supplied route is [RT-RTE-session-capture](runtime.md#rt-rte-session-capture); this is its payload object, not a duplicate route or the event-envelope container [RT-OBJ-event-emission](runtime.md#rt-obj-event-emission). SRC-1, `tortoise/extractor_v2.py`, implementation.

> "source_ref": "session.md", "quote": quote, "status": "draft",
>             "search_keys": search_keys,
>             "source_turn_id": turn_idx,
> --- `tortoise/extractor_v2.py`

#### EPI-OBJ-belief-state
Label: EP parameters and confidence

Source-native identity: persisted `posterior_alpha`, `posterior_beta`, fallback `ep_alpha`, `ep_beta`, confidence and measurement/baseline markers. Symbolic field names/markers and numerical graph state are distinct from claim prose and model weights. Stored on graph nodes and emitted through confidence-change events; current-run EP also holds state in memory. The mathematical claim that a returned mean equals a parameter ratio is truth-apt in this implementation domain. A calibrated real-world probability interpretation is not established. Closest supplied record is [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), which consumes rather than identifies this object. No counterpart object declared there. SRC-1, `tortoise/ep.py`, `tortoise/dream.py`, implementation.

> "mean": a / total,
>             "variance": (a * b) / (total * total * (total + 1)),
>             "alpha": a, "beta": b, "effective_n": total,
> --- `tortoise/ep.py`

#### EPI-OBJ-review-verdict
Label: Correction review state

Source-native identity: `reviewDecision`, `reviewVerdict`, threshold/confidence/measurement, actor/reason/source and target metadata on candidate and prior Points. Symbolic lifecycle/decision values and natural-language optional reason are stored as graph properties; receipt dictionaries expose decisions. The verdict is a policy decision, not necessarily a truth-apt proposition; factual reasons are possible but not required. No counterpart after comparison with supplied capture/direct-admission routes: this is the correction layer's explicit decision state. SRC-1, `tortoise/review_verdicts.py`, implementation.

> "n.reviewDecision=$decision, n.reviewVerdict=$verdict, "
>             "n.reviewVerdictAt=$at, n.reviewVerdictBy=$by, "
>             "n.reviewVerdictReason=$reason, n.reviewVerdictSource=$source, "
>             "n.reviewVerdictTargets=$targets",
> --- `tortoise/review_verdicts.py`

### Routes

#### EPI-RTE-source-address
Label: Value-bearing source address check
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

SDK extraction code owns `_value_verbatim_span` → payload span fields. Target/domain: occurrence of a quote in an already resolved source turn and presence of a detectable value in that quoted substring. Code performs case-insensitive whitespace-tolerant matching, not semantic entailment or external factual verification. The payload keeps the Point when this function returns no address. A deterministic deduction from inspected code: turn `Cost is 12 dollars`, quote `12 dollars`, value-bearing content and the correct turn index produce a match at offsets (8,18); the span's text contains a number, so it passes the value detector. A quote `Cost is` can occur but has no value and receives no value span. This is an implementation-layer deduction, not target execution. Source warrant remains unknown; the narrower occurrence warrant is preserved when an address is supplied. SRC-1, `tortoise/extractor_v2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: span offsets or None, with warnings for selected missing-span cases.
- Later read-back: payload carries offsets only when available; complete downstream provenance propagation is uninspected.
- Delegated visibility: inapplicable — this check is deterministic local code, not a separate model invocation.
- Selection predicate: value-shaped content/quote, resolved turn index, verbatim match, value in matched text.
- Invalidation or expiry: offsets refer to that source turn; source-version validity beyond the payload is uninspected.
- Activation or effect: conditional address fields are added; no universal rejection of spanless claims.
- Evidence limits: textual occurrence and value detection establish neither source truth nor claim entailment; all source resolution tiers not traced.

> if not _carries_value(turn_text[span[0]:span[1]]):
> --- `tortoise/extractor_v2.py`

> if _span is not None:
>             pt_entry["span_start"], pt_entry["span_end"] = _span
> --- `tortoise/extractor_v2.py:7592-7595`

#### EPI-RTE-vet-check
Label: VET candidate judgment
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Extractor code owns `_run_vet_pass` → `vet_candidates` → per-item decisions. Target is candidate suitability for the extraction payload; deterministic evaluator domain is identifier-only shape, not whether any proposition is true. A supplied arbiter can override with KEEP/DISCARD/MERGE; missing/unknown opinions fail open. Runtime-model arbiter implementation is not assessed here. Activation: injected arbiter or VET/value/seam flags arm S2 and union passes. Caller/model proposes, code/arbiter judges; no per-item human veto or expected-answer oracle is established. Open capture, not a labelled-answer curriculum. Concrete deterministic trace: `#4118` matches `_REFERENCE`, strips to empty residue and yields `value.identifier_only.reference`; with the value flag on it becomes DISCARD. `#4118 caused failure` leaves content words and is kept by that mechanical rule. No target execution is needed for this deduction. SRC-1, `tortoise/value_gate.py`, `tortoise/vet_gate.py`, `tortoise/extractor_v2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: decision map, rule/reason/counterfactuals, batch/stats and warnings.
- Later read-back: decisions ride extraction result; durable later consumption of the diagnostic artifact is uninspected.
- Delegated visibility: optional arbiter receives candidate list and narrative, not an independently verified answer key.
- Selection predicate: armed VET; mechanical predicate separately requires value flag; explicit arbiter decisions may override except NOOP does not undo standing DISCARD.
- Invalidation or expiry: judgments are per extraction pass; prior removal pool is passed to union stage.
- Activation or effect: decision map reaches apply_vet; judgment alone does not guarantee removal.
- Evidence limits: an arbiter exception preserves existing mechanical decisions, unlike an outer pass failure that keeps the input list; no quality measurement claimed.

> verdict = value_gate.mechanical_verdict(decision["text"])
>                 if verdict:
>                     decision.update(outcome=DISCARD, **verdict)
>                     mechanical[iid] = verdict
> --- `tortoise/vet_gate.py`

> if incoming == NOOP and standing == DISCARD:
>                 continue
> --- `tortoise/vet_gate.py`

> if word.lower() not in _FUNCTION_WORDS:
>             return None  # a content word survives ⇒ KEEP
> --- `tortoise/value_gate.py`

#### EPI-RTE-vet-disposition
Label: VET removal and dependency repair
Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Extractor code applies the check result through `apply_vet`, then passes the survivor list toward S5. This is a distinct function from [EPI-RTE-vet-check](#epi-rte-vet-check). Candidate membership is computationally decided against payload suitability and referential-integrity policy, not an evidence-consuming criterion for true claims. Referenced entities may survive a discard, earlier removals may be restored when S4 references them, and orphan operator pruning prevents S5's mint-before-wire stage from recreating discarded content. MERGE is left for another consumer; it is not applied by this function. Thus neither a discard token nor a merge token alone establishes its named effect. Guidance is the explicit dependency policy; retained output is a changed candidate list, not changed extraction-model parameters. SRC-1, `tortoise/vet_gate.py`, `tortoise/extractor_v2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: survivor/repaired candidate list and warnings.
- Later read-back: survivors may be persisted through capture and later retrieved; exact selection is separate.
- Delegated visibility: inapplicable — disposition is code over already returned decisions.
- Selection predicate: explicit DISCARD, subject to surviving references and prior-pool restoration.
- Invalidation or expiry: pruning prevents immediate resurrection by endpoint materialization; no permanent ban on future re-extraction.
- Activation or effect: changes what reaches S5; dependency repairs can veto a requested drop.
- Evidence limits: not all downstream consolidation/MERGE application inspected; no factual acceptance or observed benefit established.

> discarded_ids = {iid for iid, d in decision_map.items()
>                      if isinstance(d, Mapping)
>                      and str(d.get("outcome") or "").upper() == DISCARD}
> --- `tortoise/vet_gate.py`

> new_list, apply_warnings = _vet_gate.apply_vet(
>             embed_list, out["decisions"], prior=prior)
> --- `tortoise/extractor_v2.py`

> "but is referenced by a surviving candidate — kept "
>                         "(Layer-1 referential integrity)")
>                     kept.append(item)
>                     continue
> --- `tortoise/vet_gate.py`

> if isinstance(out["entities"], list):
>                 out["entities"].append(original)
> --- `tortoise/vet_gate.py`

> if (content_keys & content_gone) or (entity_keys & entity_gone):
>                     pruned += 1
>                     continue
> --- `tortoise/vet_gate.py`

#### EPI-RTE-belief-evaluate
Label: EP score evaluation and consumers

Distinct from supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery): this record identifies the numerical evaluator that its gate uses, not the entire prompt-delivery route. Owner is EP/SDK code; stored parameter pair → mean/variance/effective_n, including a degenerate-total fallback. Dream also calls `ep.run` over seeds with hydrated evidence. The inspected call/wrapping code establishes that computation is wired, not correctness of the entire propagation algorithm. Target/domain: graph-relative belief numbers conditional on stored priors, messages and topology. There is no expected-answer oracle for real-world Point truth in this computation. Declared author priors and computed posterior state are not the same provenance.

Consequential consumers are volunteer `_eligible` and VerdictLayer's `ep_posterior`/sweep. At the volunteer consumer, a mean clears a configurable floor (default 0.7), or a conflict-relevant contested state gets a bounded boost. A declared prior alone can clear that floor; the gate is not “measured only.” At correction sweep, the same class of score supplies a separate, opt-in admission condition. This record does not conflate these two dispositions. SRC-1, `tortoise/ep.py`, `tortoise/dream.py`, `tortoise/volunteer.py`, `tortoise/review_verdicts.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mean, variance, alpha/beta and effective_n; run returns iteration/convergence information.
- Later read-back: stored parameter state can be read by later gate/review invocations; exact history of each prior is uninspected.
- Delegated visibility: inapplicable — inspected EP and gating are local numerical/code operations.
- Selection predicate: requested claim/run set; volunteer and correction admission each apply their own downstream predicate.
- Invalidation or expiry: lifecycle writes can invalidate messages and mark neighborhoods dirty; full freshness enforcement uninspected.
- Activation or effect: numbers control eligibility for snippets or opt-in review; this is permissive/ranking force through code before model interpretation.
- Evidence limits: no independent calibration measurement, source-truth check or complete propagation proof; score arithmetic entails only a numeric proposition from input values.

> a, b = self._read_node(claim_id)
>         total = a + b
> --- `tortoise/ep.py`

> if mean >= min_confidence:
>         return True
>     if conflict_relevant and ep.get("contested"):
>         boost_floor = max(NEUTRAL_CONFIDENCE, min_confidence - 0.1)
>         return mean >= boost_floor
> --- `tortoise/volunteer.py`

#### EPI-RTE-belief-retain
Label: Dream belief write-back

Dreamer owns `ep.run` result → affected-set means → node confidence and optional freshness stamps → journal attempts. This is retention of evaluation state, not the evaluator or post-acceptance integration. Closest supplied route is [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), a later reader; no counterpart retention route was declared there. SRC-1, `tortoise/dream.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: iteration/convergence/affected set from batch helper; stale-run guard skips write-back.
- Later read-back: graph confidence/freshness and journal events persist beyond the call; exact ranking fields depend on reader, including posterior-first reads rather than confidence scalar alone.
- Delegated visibility: inapplicable — local code/database write-back.
- Selection predicate: affected claims from the EP run; nonempty parameter list; freshness stamping additionally requires convergence and stamp request.
- Invalidation or expiry: stale epoch guard skips write-back; failed convergence does not advance lastDreamedAt, but the scalar confidence can still be written.
- Activation or effect: materialized evaluation state becomes available to later readers; no observed host behavior.
- Evidence limits: graph/journal failure and full replay not audited; a stamp is freshness metadata, not proof of factual acceptance.

> stamp_now = stamp and converged
>         params_list = [
>             {"id": cid, "c": ep.compute_confidence(cid)["mean"]}
>             for cid in affected
>         ]
> --- `tortoise/dream.py`

> else:
>                 _set = "SET n.confidence = p.c, n.updatedAt = $now "
> --- `tortoise/dream.py`

#### EPI-RTE-review-disposition
Label: Correction queue and verdict disposition

Mining invokes `VerdictLayer(sdk).sweep(batch_id=...)` after its batch gate; explicit callers can use decide/drain. This is a new correction-conflict route, distinct from [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and [RT-RTE-direct-point](runtime.md#rt-rte-direct-point). Code owns progression over flagged candidates. Candidate proposal is supplied by mining; automatic decision is code over [EPI-RTE-belief-evaluate](#epi-rte-belief-evaluate), not an LLM self-report. Open correction review has no expected-answer oracle. A supplied verdict can veto/keep/close; caller identity does not prove a human or evidence-based decision.

Automatic acceptance is disabled by default. When enabled it permits keep at EP mean ≥ threshold (default 0.75), unless quarantined/refused by promotion. Other candidates are queued, not automatically closed/rejected. Importantly, measurement state is disclosed but not a hard acceptance gate: an unmeasured neutral 0.5 can pass a sufficiently lowered threshold, with a warning. Criterion and intended scope are therefore graph-relative score admission for correction use, not measured factual accuracy. Explicit decisions have no enforced criterion/evidence input. Keep calls approve_merge then promote; reject calls approve_merge(reject) and retracts an already-live candidate; close stamps reviewed without promoting or retracting. Candidate and priors receive verdict provenance. Recovery tries to undo review stamps only for a failed, non-landed promotion; journalled attempt cannot be unjournalled, and cleanup itself can fail. SRC-1, `tortoise/review_verdicts.py`, `tortoise/mining.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: queue/decision receipts, applied mechanics and per-item errors on drain.
- Later read-back: pending/sweep reads review state; decided candidates are skipped; provenance remains on candidates/targets.
- Delegated visibility: inapplicable — caller verdicts or numerical threshold drive code; no model review invocation inspected here.
- Selection predicate: undecided temporal candidates or explicit ID sets, auto flag, threshold and promotability; drain handles only supplied verdicts.
- Invalidation or expiry: different verdict after decided is refused; same verdict is idempotent; failure cleanup is conditional rather than global rollback.
- Activation or effect: enforcing/permissive lifecycle authority through SDK promote/retract; persists to later graph readers, not merely advisory output.
- Evidence limits: complete mining batch evaluator and original EP warrant uninspected; no exercised acceptance, guaranteed rollback or proven truth.

> if (self.auto_accept and not quarantined
>                     and posterior["mean"] >= self.threshold):
> --- `tortoise/review_verdicts.py`

> self.sdk.approve_merge(candidate_id, action="merge")
>             try:
>                 applied = self.sdk.promote_point(candidate_id)
> --- `tortoise/review_verdicts.py`

> if props.get("status") == "live":
>                 applied = {"retracted": True,
>                            "retract": self.sdk.retract_point(candidate_id)}
> --- `tortoise/review_verdicts.py`

#### EPI-RTE-review-integration
Label: Post-keep prior wiring

After [EPI-RTE-review-disposition](#epi-rte-review-disposition) calls promote, SDK code uses recorded merge approval and target state to wire an alreadyDecided IMPL, temporal NAND, or explicit replacement through supersede_point. This is a distinct post-disposition function; it is not another declaration of the whole promotion or capture route. In the threshold-acceptance branch it integrates an operationally accepted correction; without evidence-consuming acceptance in an explicit keep branch, the same mechanics are operational linking only. Target check is existence/live eligibility and duplicate/cross-link avoidance, not semantic proof that the new statement implies or contradicts the prior. Guidance persists as lifecycle/edges; no model update. SRC-1, `tortoise/sdk.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: promoted result with wiring flags and partial-supersession diagnostics.
- Later read-back: retained edges, statuses and incident live operators affect later graph/EP/retrieval consumers.
- Delegated visibility: inapplicable — local code uses prior review stamps and graph state.
- Selection predicate: merged candidate and existing eligible targets; duplicates and incompatible alreadyDecided links can suppress wiring.
- Invalidation or expiry: successor transition can retire prior; racing missing/terminal targets are skipped; full supersession internals uninspected.
- Activation or effect: enforcing graph mutation followed by later selection/propagation; no observed benefit or host compliance.
- Evidence limits: promotion can proceed with unapplied supersession; partial integration is not all-or-nothing acceptance or proof of contradiction.

> if live_targets and point.get("temporal_replacement"):
>             for tgt in live_targets:
>                 try:
>                     self.supersede_point(tgt, point_id)
>                     superseded = True
> --- `tortoise/sdk.py`

> result["supersede_skipped"] = supersede_skipped
>             result["supersede_skipped_count"] = len(supersede_skipped)
> --- `tortoise/sdk.py`

#### EPI-RTE-point-withdrawal
Label: Retraction and influence withdrawal

Caller → SDK `retract_point` → terminal CAS and message invalidation → updated properties. Closest supplied [RT-RTE-direct-point](runtime.md#rt-rte-direct-point) names later lifecycle effects but does not declare this withdrawal mechanism. Verdict rejection is a concrete caller in [EPI-RTE-review-disposition](#epi-rte-review-disposition). Code validates transition/window eligibility, not falsity of content. Caller may supply a valid-to time; generic caller does not establish human adjudication. No expected-answer oracle. Retraction withdraws operational reliance while retaining the tombstoned record. Journal-first ordering does not mean append confirmation gates this write. SRC-1, `tortoise/sdk.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: retracted node properties or validation/failure exception.
- Later read-back: tombstone remains, ordinary readers exclude terminal state, historical inclusion can remain possible.
- Delegated visibility: inapplicable — lifecycle code, not a model delegation.
- Selection predicate: nonmissing nonoperator eligible lifecycle state; optional window must not invert stored start.
- Invalidation or expiry: invalidates own and factor messages before marking neighborhood dirty, preventing intended future propagation of withdrawn influence.
- Activation or effect: status mutation blocks ordinary eligibility; invalidation requests recomputation, not immediate proof all downstream beliefs are repaired.
- Evidence limits: no global rollback or every-reader audit; append return discarded, failures can leave graph/journal disagreement; no factual falsity inference.

> self._get_ep().invalidate_messages([id])
>         self._get_ep().invalidate_factor_messages([id])
>         self._mark_dirty([id])
> --- `tortoise/sdk.py:17825-17827`

#### EPI-RTE-hook-context
Label: Volunteer CLI to hook context

Hook code → CLI volunteer → local SDK or hosted `/v1/context` → nonempty block → harness-shaped JSON. This is a distinct consumer channel from [RT-BAP-framework-block](runtime.md#rt-bap-framework-block), sharing the selection family [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). Code chooses endpoint based on configured API key, then renders only the returned block unless JSON output requested. For claude/codex/devin, hook uses additionalContext; cline uses contextModification. Consumer is the host's future model invocation, channel natural-language context, force advisory/model-interpreted, horizon current prompt and opaque host retention. Unknown harness plain stdout is not established injection. Shipped Claude instructions request starting from relevant prior decisions while also using current context; requested compliance is not observed compliance. SRC-1, `tortoise/__main__.py`, `tortoise/claude-hooks/volunteer-turn.sh`, `tortoise/claude-hooks/CLAUDE.tortoise.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: block/JSON to hook stdout; failures/empty blocks can produce no injection.
- Later read-back: retrieved graph text enters a later host invocation; host persistence after that is uninspected.
- Delegated visibility: reflex receives prompt window; harness receives selected block, not full graph/why metadata.
- Selection predicate: configured route, successful nonempty block and supported harness output shape; confidence selection belongs to canonical pipeline.
- Invalidation or expiry: silence does not delete memory; host-context removal is outside inspected code.
- Activation or effect: supplies additional context, does not enforce accepting any proposition or taking an action.
- Evidence limits: hook installation/input admission and other hook bodies not fully traced; no observed activation or parity claim.

> block = data.get("block") or ""
>     if block.strip():
>         print(block)
> --- `tortoise/__main__.py`

> 'additionalContext': os.environ.get('TORTOISE_VOLUNTEER_BLOCK', '')}}))
> --- `tortoise/claude-hooks/volunteer-turn.sh`

### Claims

#### EPI-CLM-evidence-authority
Label: Quoted evidence remains authoritative

Claimed operation: every Point retains a quoted source span, and the graph indexes unrewritten evidence. SRC-1, `README.md`, doctrine/design. Closest supplied capture/direct-point records describe implementation rather than declare this public claim; distinct referent. Source-address and direct-write cases bound the universal wording. No efficacy or cited external experiment is adopted without inspecting its conditions.

> Evidence stays authoritative: every
> Point keeps its quoted source span, and the graph is an auditable index over
> unrewritten evidence.
> --- `README.md`

#### EPI-CLM-belief-propagation
Label: Evidence propagation computes belief

Claimed operation: belief scores are computed by propagating graph evidence. SRC-1, `README.md`, doctrine/design. Closest supplied context route consumes scores but declares no counterpart claim. Implementation supports numeric evaluation/write-back and selection use; it does not independently validate input truth or calibrated probabilities.

> A graph engine for agent memory: claims are **Points**, relationships are **edges**, and belief scores are computed by propagating evidence through the graph (EP — Evidence Propagation).
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
