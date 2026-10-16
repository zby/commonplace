---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Pi Posthorse epistemic routes: provenance-sensitive recovery, unchecked task-state retention and operational context admission at the frozen extension boundary."
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
reviewed-boundary: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
---

# Pi Posthorse epistemic report

## Source-and-claim boundary

The question is whether Posthorse's continuation machinery checks truth-apt task state before granting later reliance, and what its actual checks authorize. Scope, exclusions and source identity are see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). This is the complete extension loop, not Pi's enclosing runtime or a task-solving model. The consequential design claim is [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation). No inspected product claim promises accepted scientific knowledge, verified task progress or model learning.

The ledger separates provenance classification, text transformation, capacity/protocol checks, retention and later consumption. A payload may contain factual claims, commands or both. No supplied note, live handoff or provider trace individuates the actual task propositions; their truth and the external model's internal processing are **not determinable** here. The code can still establish what happens to those candidate payloads.

| Entry point or operation | Source path, SRC-1 | Coverage and record | Remaining limit and conclusion prevented |
| --- | --- | --- | --- |
| Extension factory and tool surface | `index.ts`, `src/context-tools.ts`, `src/notes.ts`, `src/history.ts` | Direct reads of factory and all tool dispatches; [EPI-RTE-context-report](#epi-rte-context-report), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) | Host tool activation/grants are not supplied; cannot establish deployed availability. No separate extension CLI dispatcher was found in the factory; package loading is see runtime. |
| Explicit reset callback and settlement | `src/context-tools.ts`, `src/rollover.ts` | Direct callback and `explicitReset`/registration reads; [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset) | Host persistence and later-handler behavior prevent an unconditional reset guarantee. |
| Automatic compaction and threshold fallback | `src/rollover.ts`, `src/recovery.ts`, `src/recovery-results.ts` | Direct automatic-hook/registration and complete recovery reads; [EPI-RTE-recovery-provenance](#epi-rte-recovery-provenance), [EPI-RTE-recovery-reshape](#epi-rte-recovery-reshape); threshold eligibility supplied by [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery) | Manual and unsupported cases leave native summarization available. No observed activation. |
| Projection edits, ancestry and receipts | `src/recovery.ts`, `src/recovery-results.ts`, `src/history-entries.ts`, `src/message-text.ts` | Direct complete reads; [EPI-OBJ-owner-inputs](#epi-obj-owner-inputs), [EPI-OBJ-result-evidence](#epi-obj-result-evidence) | External projection construction is uninspected; exact fidelity to live reality is not established. |
| Notes list/read/search/write/append; alternate editors | `src/notes.ts`, `src/files.ts`, `src/budget.ts` | Direct mutation/search/dispatch reads and supplied publication/storage findings; [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) | External editor changes bypass tool checks; publication is not semantic acceptance. |
| History search/read and page refusal | `src/history.ts`, `src/history-entries.ts`, `src/paging.ts`, `src/history-pages.ts`, `src/history-search.ts`, `src/session-files.ts` | Direct dispatcher/normalization reads; budget/archive selection supplied by [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) | Prefilter/archive completeness not independently audited; no complete-retrieval conclusion. |
| Guidance, reminder filtering and regeneration | `src/rollover.ts`, `src/budget.ts`, `src/reminders.ts` | Direct registration and supplied hook findings; [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance) | Delivery is not compliance; no observed live-state verification. |
| Shipped reset/resume evaluator | `test/official.test.mjs` | Direct bounded scenario read; [EPI-RTE-reset-evaluator](#epi-rte-reset-evaluator) | Other assertion bodies not audited; no suite-pass or exhaustive evaluator conclusion. |
| Development checker/release plane | `package.json` and excluded paths listed in boundary | Deliberately excluded, not added to the functional loop | No checker-correctness or release-admission conclusion. |

All direct reads use SRC-1 at the frozen commit; these extend the supplied runtime's initial inspection, without adding a source. No target code was executed. No observed-run or causal-experiment source was supplied. This prevents observed restoration, measured task continuity, component benefit, learned capacity or cost-improvement conclusions. The remaining included retrieval/evaluator inspection limits also prevent a system-complete negative about every possible semantic evaluation, although the inspected write/reset/recovery dispatches support specific negative findings about their checks.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-owner-inputs](#epi-obj-owner-inputs) | User statements and linked answers may assert task facts; commands themselves are not truth-apt | see record | SRC-1, `src/recovery.ts` | Provenance labels do not establish source truth. |
| [EPI-OBJ-result-evidence](#epi-obj-result-evidence) | Tool output/error claims and invocation metadata, when present | see record | SRC-1, `src/recovery-results.ts` | Receipts do not certify progress; actual propositions unsupplied. |
| [RT-OBJ-reset-requests](runtime.md#rt-obj-reset-requests) | Handoff prose may contain task facts; map IDs are authorization metadata | see record | SRC-1, `src/rollover.ts` | The later model consumes prose, not a checked task-state assertion. |
| [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) | Caller-authored plaintext may contain factual state, decisions and instructions | see record | SRC-1, `src/notes.ts` | Inventory cites the route because supplied runtime declares no standalone note object; no actual note instance supplied. |
| [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) | Notes and historical messages, including earlier assistant thinking and errors | see record | SRC-1, `src/history-entries.ts` | Original and edited versions need not agree; historical delivery does not assert current truth. |
| [EPI-OBJ-context-report](#epi-obj-context-report) | Approximate remaining capacity, usage and rollover state | see record | SRC-1, `src/context-tools.ts` | Arithmetic license depends on native estimates and settings, not actual provider payload. |
| [RT-OBJ-context-guidance](runtime.md#rt-obj-context-guidance) | Mainly normative policy; capacity descriptions can be truth-apt | see record | SRC-1, `src/budget.ts` | Instructions to verify state are not a verification result. |
| [RT-CMP-active-model](runtime.md#rt-cmp-active-model) | Internal truth-apt units not determinable from accessible state | see record | SRC-1, `index.ts` | External distributed-parametric component; no weight, version or learning evidence supplied. |

## Authority-route ledger

Fields owned by a declaring record are marked `see`; the relation and epistemic architectural status here assess the particular ledger function, not an observed run. Separate rows on a container do not change its identity.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-recovery-provenance](#epi-rte-recovery-provenance) | check/evidence production | implemented | [EPI-OBJ-owner-inputs](#epi-obj-owner-inputs) | no content change | Owner/coordination classification and projected call linkage | see record | see record | see record | Symbolic selector input | Recorded provenance only; not truth or present intent validity | Changes recovery eligibility/label | Recovery builder, code predicate, enforcing selection, current boundary | SRC-1, `src/recovery.ts` | none | none | Tool registration/linkage is not human-answer authentication beyond host metadata. |
| [EPI-RTE-recovery-reshape](#epi-rte-recovery-reshape) | content transformation | implemented | [EPI-OBJ-owner-inputs](#epi-obj-owner-inputs), [EPI-OBJ-result-evidence](#epi-obj-result-evidence) | truth-apt transformation: non-ampliative reshaping | Projected inputs/results to bounded excerpts and pointers | see record | see record | see record | Selection and omission | Preserves selected text provenance; full source warrant unknown, completeness degraded | Determines what surviving continuation can inspect without retrieval | Later model, host summary, advisory evidence and instruction, next window | SRC-1, `src/recovery.ts`, `src/message-text.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Reshaping does not entail semantic equivalence of every truncated proposition. |
| [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery) | check/evidence production | implemented | Recovery payload from [EPI-RTE-recovery-reshape](#epi-rte-recovery-reshape) | no content change | Budget support, construction, length and cancellation | see record | see record | see record | Predicate/failure result feeds draft or cancellation | Capacity/route eligibility only | Establishes whether custom payload can be proposed | Automatic hook, symbolic conditions, enforcing within hook, current boundary | SRC-1, `src/rollover.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | No progress evaluator. |
| [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery) | disposition/acceptance | implemented | Same recovery payload | no content change | Custom compaction versus cancel/native pass-through | see record | see record | see record | see [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) | Operational admission, not epistemic acceptance | Permits host boundary or blocks this recovery attempt | see [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) | SRC-1, `src/rollover.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Manual/unsupported native route remains; cancellation is not journal rollback. |
| [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset) | check/evidence production | implemented | [RT-OBJ-reset-requests](runtime.md#rt-obj-reset-requests) | no content change | Originating callback, foreground errors/abort and pending-input-aware capacity | see record | see record | see record | Symbolic predicates | Foreground protocol success, not handoff truth | Determines eligibility for reset draft | Posthorse turn-end handler, code checks, enforcing there, current turn | SRC-1, `src/context-tools.ts`, `src/rollover.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Later-handler abort is a counterexample to unconditional abort prevention. |
| [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset) | disposition/acceptance | implemented | [RT-OBJ-reset-requests](runtime.md#rt-obj-reset-requests) | no content change | Handoff to retain-none draft, or defer without context change | see record | see record | see record | see [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) | No evidence-consuming acceptance of task claims | Permits fresh foreground continuation | see [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) | SRC-1, `src/rollover.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Successful sibling effects are not undone. |
| [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) | retention | implemented | Caller note payload | truth-apt transformation: acquisition/import | Caller prose to plaintext file | see record | see record | see record | Filesystem publication | Source warrant unknown; no semantic criterion | Enables later retrieval; replace/append can alter instructions as well as facts | Filesystem readers then model tool results, permissive publication/advisory text, later windows/sessions | SRC-1, `src/notes.ts`, `src/files.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Physical rejection/rollback is not false-content rejection; external editor bypass exists. |
| [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery), [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset) | retention | implemented | Automatic bounded recovery or caller handoff | no content change | Draft to host-persisted continuation | see records | see records | see records | Host-mediated projection/persistence | No added warrant from persistence | Replaces accumulated active context while retaining journal access | see [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) | SRC-1, `src/rollover.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Extension-side wiring only; host implementation uninspected. |
| [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) | operational admission/selection/consumption | implemented | Selected notes/history | truth-apt transformation: acquisition/import | Existing content into later model input | see record | see record | see record | Matching/ranking and budgeted delivery | Historical attribution, not current-state endorsement; source warrant unknown | Permits caller-requested evidence use, refuses oversized page | Model, tool result, advisory content with enforcing page refusal, current and later requests | SRC-1, `src/history.ts`, `src/history-entries.ts` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Search favors originals before echoes, not verified claims before false ones. |
| [EPI-RTE-context-report](#epi-rte-context-report) | content transformation | implemented | [EPI-OBJ-context-report](#epi-obj-context-report) | truth-apt transformation: entailed derivation | Supplied usage/settings to numeric report | see record | see record | see record | Advisory tool return | Arithmetic under supplied estimates only | Can inform plan change; does not itself reset or constrain execution | see record | SRC-1, `src/context-tools.ts` | none | none | No independently warranted native usage premise. |
| [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance) | behavior/policy adaptation | implemented | [RT-OBJ-context-guidance](runtime.md#rt-obj-context-guidance) | non-truth-apt policy/content update: request-local checkpoint and verification instructions | Request/working-turn guidance selected from usage/policy/reminder state | see record | see record | see record | see [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance) | None from instruction delivery | Requests checkpointing and live-state verification | see [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance) | SRC-1, `src/budget.ts`, `src/rollover.ts` | none | none | Fixed adaptive delivery, not revised method or demonstrated improvement. |
| [EPI-RTE-reset-evaluator](#epi-rte-reset-evaluator) | check/evidence production | implemented | Reset/resume scenario assertions | no content change | Journal/context preservation, notes/history availability and call count | see record | see record | see record | Test assertion failure only | Specific API/context predicates if executed, not task truth | Can fail test invocation; no production payload gate traced | Test runner, assertions, enforcing failure, one fixture | SRC-1, `test/official.test.mjs` | [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | none | Source is evaluator design, not a recorded pass. |

No **lifecycle integration** route for an accepted task claim was found in the inspected note-write, explicit-reset and automatic-recovery dispatches: none consumes evidence to accept a proposition against a criterion for a named intended use before connecting it to later organization. Retention and operational admission above are not silently recast as integration. This is bounded to those dispatches, not to arbitrary model/host activity.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation) | see record | SRC-1, `package.json`, `README.md`; doctrine/design | Package/reference continuation procedure; README also says each rollover lacks a model-generated summary | [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery), [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval), [EPI-RTE-recovery-reshape](#epi-rte-recovery-reshape), [EPI-RTE-reset-evaluator](#epi-rte-reset-evaluator) | None supplied; evaluator source is not operation | No causal comparison; host reachability and native fallback bound the implementation claim | Reached supported automatic handler constructs deterministic recovery without a summary-model call; notes/history and explicit handoffs wire continuation mechanisms | README's opening “Each rollover” requires its later manual/native qualifications. Neither deterministic recovery nor retained transcript warrants correct task continuation. |

The countercase is present in the same public documentation, not inferred from missing code:

> Each rollover uses a handoff or recovery record without a model-generated summary.
> --- `README.md`

> Manual `/compact` uses Pi's normal summarization.
> --- `README.md`

The supplied runtime already preserves this distinction; no supersession is needed. Its unconditional-negative alternatives were checked against manual pass-through, external editors, projected orphan/async receipts and later-handler ordering rather than treating its ordinary route as exhaustive.

## Bounded conclusion

**Posthorse gives operational continuation authority, not semantic acceptance of task facts.** Note writes publish caller text; reset checks license a context transition; automatic recovery checks support and size. Those targets and domains are different from whether a task-state proposition is true. The later model receives a handoff/recovery record and, on request, selected notes/history; its actual reliance and correctness remain unobserved. See [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset), [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery).

**Recovery manages lineage and limited visibility.** It distinguishes direct inputs, linked owner answers and coordination, honors projection omissions/replacements, and preserves bounded receipts with IDs and retrieval pointers. These are useful evidence-selection controls, not truth certification or completed-work evidence. The selected excerpts retain local provenance; omissions degrade completeness, and source warrant remains unknown. The warning that inputs are not current progress is consequential model guidance, not an enforced prohibition on relying on stale prose. See [EPI-RTE-recovery-provenance](#epi-rte-recovery-provenance), [EPI-RTE-recovery-reshape](#epi-rte-recovery-reshape), [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance).

**The one directly inspected factual derivation is capacity reporting.** Its arithmetic follows native usage/settings; it does not independently measure physical provider capacity. The unknown-usage branch withholds a count. This limited entailed derivation does not warrant unrelated task claims. See [EPI-RTE-context-report](#epi-rte-context-report).

**No particular generated task conjecture or accepted ampliative claim is established by these sources.** External models can supply prose, but no actual candidate/evidence/acceptance chain is supplied. This is not evidence that models never conjecture, learn or criticize. Likewise no conclusion about changing weights follows from fixed extension code; mutability/version/endpoint limits remain see [RT-CMP-active-model](runtime.md#rt-cmp-active-model). The inspected dispatches establish unchecked retention/admission, not a theory-builder verdict about the host or model.

**Verification is requested, not completed by the extension.** Guidance adapts delivery to usage and reminder state; this is a direct operational behavior path without a truth-apt acceptance loop. The shipped test scenario checks concrete continuation mechanics, not live task success. No supplied execution establishes compliance, successful learning, reflective criticism, self-improvement or benefit. Those remain separate unestablished properties, not a single system score. See [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance), [EPI-RTE-reset-evaluator](#epi-rte-reset-evaluator).

## Shared records

### Operative objects

#### EPI-OBJ-owner-inputs
Label: Selected owner and coordination inputs

Part of: [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)

This object is the input-record material carried by that route, not a duplicate of the route itself. Source-native identity: `RecoveryRecord` entries created by `recordSource`/`recoveryRecord`. Representational form: natural-language payload with symbolic kind, label, entry ID and timestamp. Storage substrate: transient objects rendered into host-persisted recovery text if admitted. User text and linked successful unnamespaced `ask_question` answers can contain factual claims; displayed custom-message coordination has different authority. SRC-1, `src/recovery.ts`.

> if (entry.type === "message" && entry.message?.role === "user") {
> 		return { kind: "owner", label: "owner input", content: entry.message.content };
> 	}
> --- `src/recovery.ts`

> kind: "coordination",
> 			label: `visible ${(entry.customType ?? "custom").slice(0, 80)} coordination input (not direct owner input)`,
> 			content: entry.content,
> --- `src/recovery.ts`

#### EPI-OBJ-result-evidence
Label: Projected tool result evidence

Part of: [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)

This object is the receipt material carried by that route. Source-native identity: `RecoveryBatch`/`RecoveryBlock` produced by `recoverableToolResults` and `resultBlock`. Representational form: natural-language tool text/error, with symbolic IDs, names and serialized arguments; image content becomes metadata and a retrieval pointer in this payload. Storage substrate: transient strings then potential host summary. It records what projected receipts say, not a certified external outcome. SRC-1, `src/recovery-results.ts`.

> header: `[${message.isError === true ? "error" : "result"} entry ${resultId}]`,
> 		text: `${resultOutput(result)}\n\nTool: ${name}\nCall ID: ${message.toolCallId ?? "unknown"}${callDetails(matching, allLinked)}`,
> --- `src/recovery-results.ts`

> // Only projected provenance is eligible. Orphans never resurrect a raw call.
> 		return index > start || call === undefined || call.block.async === true;
> --- `src/recovery-results.ts`

#### EPI-OBJ-context-report
Label: Context remaining report

Source-native identity: `contextReport` tool-result text and structured display data. Representational form: localized symbolic arithmetic values rendered as natural-language estimates. Storage substrate: tool return, with journal persistence host-owned. No counterpart object is declared in the supplied runtime: unlike [RT-OBJ-context-guidance](runtime.md#rt-obj-context-guidance), this is a caller-requested report, not regenerated instruction. SRC-1, `src/context-tools.ts`.

> const configured = `≈${n(Math.max(0, usage.contextWindow - usage.tokens))} tokens until the configured context limit (${n(usage.tokens)}/${n(usage.contextWindow)} used, ${Math.round(usage.percent ?? 0)}%). Best available native estimate.`;
> --- `src/context-tools.ts`

### Routes

#### EPI-RTE-recovery-provenance
Label: Recovery provenance classification

Part of: [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)

Endpoints/progression: branch/projection metadata → `projectedCurrent` and `ownerRecords` → owner/coordination classification → recovery selector. Owner: Posthorse code; Pi supplies projection/tool metadata. Effects: removes projected-away records, uses replacement content/IDs, and limits owner answers to successful linked registered unnamespaced calls. This is a check of recorded provenance, not an evaluator of source truth. SRC-1, `src/recovery.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Eligible labeled input records to the recovery builder, not a standalone user-visible judgment.
- Later read-back: Selected labels/IDs survive in admitted recovery text for the later model.
- Delegated visibility: uninspected — the host decides independent worker inputs; coordination text here only records visible input.
- Selection predicate: User messages; displayed non-reminder custom messages; owner answers require registered tool, projected call name/namespace and successful matching result.
- Invalidation or expiry: Projected empty messages and null context-edit replacements omit input; replacement IDs/content change lineage.
- Activation or effect: Classification changes selection/labels in deterministic construction; later model obedience to owner/coordination distinction is unobserved.
- Evidence limits: Recorded linkage depends on external host metadata; no independent authentication or semantic approval.

Software proposes/selects these record classes; there is no mandatory human approval or answer oracle. Operating mode is open task continuation. Rejection omits ineligible records, not false claims; history remains the recovery route for omitted raw material under the host contract.

> const call = calls.get(entry.message?.toolCallId);
> 		const record = recoveryRecord(
> 			entry,
> 			ownerQuestionRegistered &&
> 				call?.name === "ask_question" &&
> 				call.namespace === undefined,
> 		);
> --- `src/recovery.ts`

> if (id !== "" && omittedIds.has(id)) {
> 			return [];
> 		}
> 		const edit = edits.get(id);
> 		if (edit?.replacement === null) {
> 			return [];
> 		}
> --- `src/recovery.ts`

#### EPI-RTE-recovery-reshape
Label: Bounded recovery reshaping

Part of: [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)

Endpoints/progression: classified inputs/projected receipts and older checkpoint ancestry → `buildAutoHandoff` → selected headers, excerpts, omission markers and pointers. Owner: deterministic Posthorse code. Effects: a bounded proposal for later model input; admission is separately owned by the parent route. This part neither duplicates the whole admission route nor asserts an observed outcome. SRC-1, `src/recovery.ts`, `src/message-text.ts`, `src/recovery-results.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Constructed recovery text to the enclosing compaction handler.
- Later read-back: If admitted by the host, later model sees selected payload; ancestry can carry owner anchors instead of nesting whole automatic records.
- Delegated visibility: uninspected — nested/delegated input delivery belongs to the host, not this constructor.
- Selection predicate: First owner input, latest owner and latest overall become anchors; other inputs get budgeted index lines; eligible projected receipts get bounded blocks.
- Invalidation or expiry: Current projection and context-edit versions govern selection; prior checkpoints are marked possibly stale, carried inputs possibly handled; older headers/text can be omitted for budget.
- Activation or effect: Determines surviving context evidence and adds fixed provenance/verification guidance; no observed behavioral reliance or improvement.
- Evidence limits: Non-ampliative reshaping classifies quoted/excerpted source material, not every claim implied by interpreting an incomplete fragment. Input truth and semantic completeness are not established.

Concrete deduction from the inspected implementation, without executing it: `excerpt("abcdef", 3)` takes the branch where the limit is smaller than the omission marker and returns `abc`. A factual sentence can therefore lose a qualifier without a visible marker at very small limits. At larger limits the head/tail retain a middle-omission marker. This is selection/compression, not a newly tested proposition; semantic equivalence to the whole source is not licensed. `buildAutoHandoff` also allocates per-record budgets and can keep headers without text. A record label alone is not progress evidence.

> if (text.length <= limit) {
> 		return text;
> 	}
> 	const marker = "\n… middle omitted …\n";
> 	if (limit <= marker.length) {
> 		return text.slice(0, limit);
> 	}
> --- `src/message-text.ts`

> perBlock > 0 ? `${block.header}\n${excerpt(block.text, perBlock)}` : block.header,
> --- `src/recovery.ts`

> const inputHeader =
> 		fixed.length > 0
> 			? "Selected owner and coordination inputs (chronological):"
> 			: "No selected current-window owner or visible coordination inputs were found.";
> --- `src/recovery.ts`

#### EPI-RTE-context-report
Label: Context remaining derivation

Source-native endpoints/progression: caller invokes `get_context_remaining` → native usage and effective policy → arithmetic/report → current model tool result. Owner: Posthorse computation, external host premises. Context effect: delivers an approximate count and rollover state, not a reset or enforced plan. No counterpart route in supplied runtime; this is distinct from [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance), though both use budget data. SRC-1, `src/context-tools.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unknown-usage message or approximate remaining capacity and rollover configuration.
- Later read-back: uninspected — host journal may retain the result, but no later read-back trace is supplied.
- Delegated visibility: uninspected — this tool returns to its caller; independent model contexts are external.
- Selection predicate: Usage unknown/null withholds count; disabled or unsupported policy changes report; supported enabled policy reports rollover line.
- Invalidation or expiry: Subsequent usage/settings/model changes invalidate applicability of an earlier estimate; report is computed afresh on each call.
- Activation or effect: Caller can use the advisory tool-result estimate when planning; no observed plan change.
- Evidence limits: Native usage/settings are premises, not independently measured here; report does not certify provider limits.

For a hypothetical native input of 100,000 context tokens and 20,000 used, the inspected subtraction/max branch entails an 80,000 configured-limit estimate. This is arithmetic over supplied estimates, not independently warranted physical capacity. The model may choose to query; code decides output and can withhold a number. There is no task-answer oracle and no human approval gate. Operating mode: open context self-management. Consumer: foreground model; channel: tool result; force: advisory estimate; horizon: until usage/configuration changes.

> if (usage === undefined || usage.tokens === null) {
> 		return textResult("Context usage is not known until the next model response.", [], {
> 			kind: "context",
> 		});
> 	}
> --- `src/context-tools.ts`

#### EPI-RTE-reset-evaluator
Label: Reset resume evaluator

Endpoints/progression: shipped faux-provider scenario → real SDK session calls → `assert` predicates over context, journal, notes/history and reopening. Owner: test author/Node test runner; faux provider supplies prescribed responses, not independent task reasoning. This evaluator is distinct from [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset): it tests that route and retrieval, not admits production handoffs. SRC-1, `test/official.test.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Assertion pass/failure when the test is executed; no run result supplied.
- Later read-back: inapplicable — inspected scenario does not retain a behavioral policy update for later product operation.
- Delegated visibility: inapplicable — the scenario has a faux foreground provider, not a delegation mechanism.
- Selection predicate: Test fixture prescribes note write/reset then note read/history search, and compares resulting messages and persisted journal.
- Invalidation or expiry: Fixture-specific predicates apply to that host/configuration/scenario, not arbitrary deployments or task outcomes.
- Activation or effect: A failed predicate can fail the test invocation; no production semantic acceptance gate or observed release disposition follows.
- Evidence limits: Source assertions are design evidence; no execution, suite-pass, host universality or component-causal evidence supplied.

Check target/domain: explicit reset context preservation, transcript accessibility and session reopening in this fixture. Evaluator: deterministic assertions; reference outcomes: literal markers, role/tool predicates and serialized context equality. Intended criterion: those API/context properties, not whether `DURABLE_NEXT_STEP` describes true progress. Author specifies test inputs and expected results; code decides assertion outcome; no model judge supplies an oracle. Operating mode: bounded engineering fixture. Its source does not establish deployment admission or rollback.

> assert.doesNotMatch(JSON.stringify(fresh), /RAW_ORIGINAL_OWNER|DURABLE_NEXT_STEP/);
> 	assert.match(textOf(toolResult(h, "notes")), /DURABLE_NEXT_STEP/);
> 	assert.match(textOf(toolResult(h, "history")), /RAW_ORIGINAL_OWNER/);
> --- `test/official.test.mjs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
