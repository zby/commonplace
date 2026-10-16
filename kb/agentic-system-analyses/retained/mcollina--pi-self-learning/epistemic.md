---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "pi-self-learning: truth-apt reflection, syntactic admission and historical-memory authority at the frozen extension revision."
run-id: AAS-2026-10-15-pi-self-learning-1a318610d4b1-01
reviewed-boundary: e0d76a93195b11b688ca71da8a8b5700c6541542
---

# pi-self-learning epistemic report

## Source-and-claim boundary

The question is whether session reflection and maintenance produce checked knowledge or instead retain model-generated candidates for later operational reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identities and layers: see its [Source register](boundary.md#source-register). This member directly inspected SRC-1, the complete `extensions/self-learning.ts`, and `README.md`, at the frozen commit. Packaging and absence of supplied evaluations are taken from the boundary and runtime, not new execution. No providers, host internals, user memories, target executions or experiments were inspected.

Coverage below checks dispatch against the provisional runtime. No omitted material operation was found. The documented command forms represent eight command names: the two documented forms of `/learning-model` share one registration; the source has eight `registerCommand` calls. The boundary/runtime's count of nine is a nonconsequential counting defect, not a missing route. No tool registration exists in the inspected extension.

| Entry point or operation | Source path | Coverage and record citations | Basis and limit |
|---|---|---|---|
| `agent_end`, `/learning-now` | `extensions/self-learning.ts` | [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | Direct: bounded transcript, abort filter, operational-signal classification, completion, repair, parser, writes. Host serialization internals excluded. |
| `before_agent_start` | `extensions/self-learning.ts` | [RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) | Direct: notes, file ordering, truncation, returned policy; host compliance unobserved. |
| `/learning-month` | `extensions/self-learning.ts` | [RT-RTE-month-summary](runtime.md#rt-rte-month-summary) | Direct: daily selection, bounded model input, nonempty-output admission, overwrite. |
| `/learning-redistill` | `extensions/self-learning.ts` | [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | Direct: confirmation, repair, missing-ID fallback, prefix enforcement, collision merge, final writes. |
| `/learning-toggle`, `/learning-model`, `/learning-model-global` | `extensions/self-learning.ts` | [RT-RTE-runtime-controls](runtime.md#rt-rte-runtime-controls) | Direct: branch and settings writes; branch model selection remains ineffective for completions. |
| `/learning-daily`, `/learning-status` | `extensions/self-learning.ts` | [RT-RTE-runtime-controls](runtime.md#rt-rte-runtime-controls) | Direct: path/config diagnostics, not semantic evaluation or retained-claim withdrawal. |
| Index load/migration, update, rendering and ranking | `extensions/self-learning.ts` | [EPI-RTE-index-migration](#epi-rte-index-migration), [EPI-RTE-watchout-conversion](#epi-rte-watchout-conversion), [EPI-RTE-core-ranking](#epi-rte-core-ranking) | Direct: additional split of material functions within runtime containers. |
| Git, default-file initialization, timeout/error paths | `extensions/self-learning.ts` | [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | Direct: best-effort history, no automatic rollback, provider cancellation unestablished. |
| Package loading and remaining tracked files | `package.json`, `AGENTS.md`, `docs/example-settings.json`, `.gitignore` | [boundary](boundary.md#boundary-and-evidence) | Supplied findings only; no separate evaluator entry point reported. |

Consequential claims: [EPI-CLM-prevention-scope](#epi-clm-prevention-scope), [EPI-CLM-full-history](#epi-clm-full-history), and [RT-CLM-strict-consultation](runtime.md#rt-clm-strict-consultation). No supplied output individuates an actual truth-apt learned proposition: its correctness, novelty, acceptance and later use are not determinable. No run evidence establishes model faithfulness or activation; no causal comparison establishes improvement or cross-project transfer. Provider parameters/versioning: see [RT-CMP-reflection-model](runtime.md#rt-cmp-reflection-model). Opaque provider state does not justify a claim of either provider learning or provider immutability.

## Epistemic-object inventory

Fields owned by a linked record are given there, not redefined here. Candidate truth-apt content is distinguished from imperative policy even when both occupy the same string array.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-conversation-signals](#epi-obj-conversation-signals) | Claims about past actions, failures and fixes; tool error classifications | see record | SRC-1, `extensions/self-learning.ts` | Host transcript truth and classification precision unchecked. |
| [EPI-OBJ-reflection-items](#epi-obj-reflection-items) | Mistake/fix assertions if generated; imperative prevention advice can have no proposition | see record | SRC-1, `extensions/self-learning.ts` | Actual outputs unavailable; content-level classification not determinable. |
| [EPI-OBJ-index-items](#epi-obj-index-items) | Retained assertion/rule text; numerical recurrence metadata | see record | SRC-1, `extensions/self-learning.ts` | Scores measure occurrence, not verified success. |
| [EPI-OBJ-monthly-text](#epi-obj-monthly-text) | Summary assertions if generated | see record | SRC-1, `extensions/self-learning.ts` | No output or entailment comparison. |
| [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes) | Prefix of a candidate mistake/fix; may be incomplete | see record | SRC-1, `extensions/self-learning.ts` | Truncation can remove scope or negation; not a checked proposition. |
| [RT-CMP-reflection-model](runtime.md#rt-cmp-reflection-model) | Not individually inspectable in parameters | see record | SRC-1, `extensions/self-learning.ts` | External model state; exact version not pinned. |
| [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) | None in the static consultation imperatives themselves | see record | SRC-1, `extensions/self-learning.ts` | They prescribe reliance; they do not authenticate memory. |

## Authority-route ledger

The ledger splits functions even where the runtime record is a valid container for several phases. All rows are implementation deductions, not observed executions. “No semantic license” means the check supplies no new warrant for truth; it does not imply all stored propositions are false. Evidence anchors and gaps apply locally. Retention here is not lifecycle integration after evidence-consuming acceptance.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | content transformation | implemented | [EPI-OBJ-conversation-signals](#epi-obj-conversation-signals) | truth-apt transformation: acquisition/import | Branch messages into completion input | Code filters aborts/takes tail; regex classifies error text | Automatic gate or manual request | Selected transcript and bounded constraint signals | Input selection | Source warrant unknown; errors are reported signals, not authenticated facts | Supplies selected evidence to proposer | Completion model, user message, informational, current request | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | none | Host conversion may alter representation; tail excludes older context. |
| [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | content transformation | implemented | [EPI-OBJ-reflection-items](#epi-obj-reflection-items) | truth-apt transformation: indeterminate | Transcript to mistake/fix candidates | Selected model under project/global prompt; no independent oracle | Enabled reflection, then optional malformed-output repair | Candidate JSON/text | Proposal only before parser | No verified entailment, factuality or generality | Creates candidates eligible for admission | Parser, completion text, proposed content, this invocation | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | none | Acquisition, reshaping and conjecture remain possible; outputs needed. Imperative-only outputs would instead be policy updates. |
| [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | check/evidence production | implemented | [EPI-OBJ-reflection-items](#epi-obj-reflection-items) | no content change | JSON object and at least one nonempty string list | Deterministic parser, structural/string domain | Before writes; extraction/one model repair if needed | Parsed object or undefined | Enforcing structural test | Licenses usable strings only | Result controls write eligibility | `reflectNow`, parsed return, enforcing, current invocation | SRC-1, `extensions/self-learning.ts` | none | none | No truth test or enforced max array count; repair can change content. |
| [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | disposition/acceptance | implemented | [EPI-OBJ-reflection-items](#epi-obj-reflection-items) | no content change | Admit parsed candidate or skip | Code consumes parser outcome; model proposes; no per-item human veto | Immediately after parsing/repair | Return invalid-output reason or proceed | Enforcing admission | Not evidence-consuming epistemic acceptance | Permits persistence of any qualifying strings | Filesystem writer, branch in code, permissive, current update | SRC-1, `extensions/self-learning.ts` | none | none | Structural admission is not acceptance for verified future prevention. |
| [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) | retention | implemented | [EPI-OBJ-reflection-items](#epi-obj-reflection-items), [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes) | truth-apt transformation: non-ampliative reshaping | Parsed strings to dated bullets and short note | Deterministic append/format/prefix selection | After admission | Daily entry and first-item prefix | Durable append; FIFO process note | No additional truth warrant; note completeness degraded by truncation | Makes candidates available to later turns | File bundler and note hook, text, advisory, sessions/process respectively | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-full-history](#epi-clm-full-history) | none | No transcript provenance link retained per item; no transactional rollback. |
| [EPI-RTE-watchout-conversion](#epi-rte-watchout-conversion) | content transformation | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | non-truth-apt policy/content update: prefix mistakes with avoidance advice | Mistake string to watch-out | Code unconditionally adds `Avoid:` | Each admitted mistake | Normalized imperative-like text | Automatic update | A historical error claim alone does not warrant generalized advice | Installs watch-out in candidate index | Index renderer, text, advisory downstream, sessions | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | none | Concrete counterexample in record; no claim of semantic preservation. |
| [EPI-RTE-index-migration](#epi-rte-index-migration) | lineage/freshness/recovery | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | truth-apt transformation: acquisition/import | Missing/invalid index replaced from Markdown bullets | Code parses every bullet and assigns defaults | Index load fallback | New in-memory index, default file creation if missing | Recovery substitution | Imported source warrant unknown; counters do not recover prior evidence | Allows updates/redistill using migrated items | Index consumers, symbolic defaults/text, permissive, later writes | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-full-history](#epi-clm-full-history) | none | Bullet hierarchy and original chronology not recovered. |
| [EPI-RTE-core-ranking](#epi-rte-core-ranking) | retention | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | truth-apt transformation: non-ampliative reshaping | Text-key updates, rendered core and long-term files | Normalized lowercase keys; fixed hit/score arithmetic | Reflection update or final redistill write | Merged index and overwritten views | Automatic file rewrite | Frequency is not corroboration | Retains merged candidates, not all textual versions | Future load/bundle, index/files, permissive, sessions | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-full-history](#epi-clm-full-history) | none | Case-insensitive collision may discard meaningful distinctions. |
| [EPI-RTE-core-ranking](#epi-rte-core-ranking) | operational admission/selection/consumption | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | no content change | Which candidates occupy core | Score minus age penalty; hit/time tie-breaks; kind balance | Core rendering | Selected bounded view | Ranking | No factual or utility license from recurrence/recency | Promotes selected text into default bundled file | Foreground agent via core bundle, text, ranking then advisory, next turns | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | none | Eviction from core is not rejection from index or retraction. |
| [RT-RTE-month-summary](runtime.md#rt-rte-month-summary) | content transformation | implemented | [EPI-OBJ-monthly-text](#epi-obj-monthly-text) | truth-apt transformation: indeterminate | Daily text to monthly summary | Selected model, bounded month input, unchanged summary prompt | Manual month request | Proposed summary | Proposal | Faithfulness unknown | Produces summary eligible for overwrite | Monthly writer, text, proposal, invocation | SRC-1, `extensions/self-learning.ts` | none | none | Reshaping versus novel assertion unresolved without input/output. |
| [RT-RTE-month-summary](runtime.md#rt-rte-month-summary) | check/evidence production | implemented | [EPI-OBJ-monthly-text](#epi-obj-monthly-text) | no content change | Nonempty text | Code trims concatenated text blocks | Before writer | Empty/nonempty | Enforcing minimal test | Only text presence | Determines continuation | Summary command, Boolean branch, enforcing, invocation | SRC-1, `extensions/self-learning.ts` | none | none | No section, source or semantic comparison. |
| [RT-RTE-month-summary](runtime.md#rt-rte-month-summary) | disposition/acceptance | implemented | [EPI-OBJ-monthly-text](#epi-obj-monthly-text) | no content change | Nonempty candidate admitted | Code; human initiates month, not content approval | After minimal test | Skip or admit | Enforcing admission | No epistemic acceptance established | Permits monthly overwrite | Writer, control flow, permissive, invocation | SRC-1, `extensions/self-learning.ts` | none | none | Cannot reject plausible false summary. |
| [RT-RTE-month-summary](runtime.md#rt-rte-month-summary) | retention | implemented | [EPI-OBJ-monthly-text](#epi-obj-monthly-text) | truth-apt transformation: non-ampliative reshaping | Admitted text into dated monthly wrapper | Code filesystem write | After admission | Same-month file replaced | Automatic overwrite | No additional warrant | Enables optional later bundle | File reader, Markdown, advisory, sessions | SRC-1, `extensions/self-learning.ts` | none | none | Later daily edits do not invalidate old summary. |
| [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | content transformation | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | truth-apt transformation: indeterminate | Selected rules into generic rules | Model prompted to preserve meaning/remove specifics; code enforces kind prefix | Manual global request; optional coarse confirmation; per chunk | Rewritten or original text for missing IDs | Proposal and deterministic prefix editing | No demonstrated semantic preservation or scope transfer | Generates replacement candidates | Chunk parser/update code, JSON, proposed content, invocation | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | none | Removing identifiers may change truth conditions; output pairs required. |
| [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | check/evidence production | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | no content change | Parseable items with finite IDs and nonempty text | Code parser, not semantic evaluator; optional model repair | Each chunk before staging | Nonempty map or failed chunk | Enforcing syntax test | Structural usability only | Allows chunk processing | Redistill loop, map/undefined, enforcing, invocation | SRC-1, `extensions/self-learning.ts` | none | none | Does not enforce complete requested ID set. |
| [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | disposition/acceptance | implemented | [EPI-OBJ-index-items](#epi-obj-index-items) | no content change | Stage chunk or abort; commit entire staged transformation unless dry-run | Code consumes parse result; human can cancel coarse start, not approve each rewrite | All chunks must finish before final write block | Abort, preview or admission | Enforcing staging gate | No evidence-consuming acceptance for cross-project use | Permits index/core/long-term replacement | Final write block, staged values, permissive, sessions | SRC-1, `extensions/self-learning.ts` | [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | none | Partial final writes have no automatic rollback; collisions merge histories. |
| [RT-RTE-context-injection](runtime.md#rt-rte-context-injection) | operational admission/selection/consumption | implemented | [EPI-OBJ-index-items](#epi-obj-index-items), [EPI-OBJ-monthly-text](#epi-obj-monthly-text), [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes) | no content change | Selected retained text to foreground model | Code flags/counts/lexical dates/prefix caps; model later interprets | Enabled before-start hook | Hidden message and consultation policy returned | Advisory historical-evidence framing, imperative policy | Requested reliance, not authenticated evidence | Can shape later answers/consultation; no read/answer gate | see [RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy) | SRC-1, `extensions/self-learning.ts` | [RT-CLM-strict-consultation](runtime.md#rt-clm-strict-consultation) | Enforcement wording exceeds gate | Delivery unobserved; long-term supplied by path only; omitted qualifiers can change interpretation. |
| [RT-RTE-runtime-controls](runtime.md#rt-rte-runtime-controls) | behavior/policy adaptation | implemented | None: settings and branch controls | non-truth-apt policy/content update: enabled/model configuration | Which reflection/context routes run and model is selected | Human command; code validates values and persists references | Explicit command, not evaluation feedback | Toggle/global model change; branch model stored but ignored by pickers | Deterministic settings gate | No truth judgment | Changes route eligibility/model resolution; maintenance bypasses enabled toggle | Hook/picker, symbolic settings, enforcing, later invocations | SRC-1, `extensions/self-learning.ts` | none | none | No autonomous policy revision from measured outcomes. |

No lifecycle-integration route after epistemic acceptance was found in the complete inspected extension. The positive functions above include operational use and organization of candidates, not evidence-consuming acceptance under a named truth/prevention criterion. Git snapshots and display statistics add recovery/visibility, not evaluation. The supplied runtime retains their implementation passages; the new split records below retain additional load-bearing passages.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-prevention-scope](#epi-clm-prevention-scope) | see record | SRC-1, `README.md`, `extensions/self-learning.ts`; doctrine/design | Mistake/fix focus and reusable global rules | [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill), [EPI-RTE-watchout-conversion](#epi-rte-watchout-conversion) | None supplied | No intervention/comparison, evaluator of future success, or transfer evidence | Implemented improvement-directed proposal and memory-use pathway | “Reusable” is requested, not warranted; prefix conversion can change function without semantic judgment. |
| [EPI-CLM-full-history](#epi-clm-full-history) | see record | SRC-1, `README.md`, `extensions/self-learning.ts`; doctrine/design | Complete-history wording | [EPI-RTE-core-ranking](#epi-rte-core-ranking), [EPI-RTE-index-migration](#epi-rte-index-migration), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) | None supplied | File history/commits unobserved; no automatic restore | Long-term renders all current merged index items | Not every reflection/version/evidence lineage; daily logs and optional Git are separate. |
| [RT-CLM-strict-consultation](runtime.md#rt-clm-strict-consultation) | see record | SRC-1, `README.md`; doctrine/design | Imperative policy explicitly requests consultation | [RT-RTE-context-injection](runtime.md#rt-rte-context-injection) | None supplied | Host/model compliance not measured | Consultation request is wired | No enforcement gate; does not establish truth of consulted material. |

## Bounded conclusion

The package acquires a selected account of coding activity, not authenticated task outcomes. It can construct and retain mistake/fix candidates and ask a later model to treat rendered memory as historical evidence. The structural evaluator's domain is JSON/string usability; the monthly evaluator checks text presence; redistill checks usable ID/text mappings. Their operative results control rejection, repair, continuation and writes. None supplies a truth, prevention-success or transfer criterion for epistemic acceptance. Starting maintenance or confirming a large batch is not per-content human acceptance ([RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection), [RT-RTE-month-summary](runtime.md#rt-rte-month-summary), [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill)).

Source warrant is unknown at transcript import. Model transformation, truncation and loss of item-to-transcript lineage do not preserve a demonstrated warrant. No inspected premise set plus checked inference establishes a derived substantive claim. Individual model outputs could be imports, compressions, conjectures or policy-only instructions; without outputs their relation remains indeterminate, not automatically ampliative. Deterministic mistake-to-watch-out conversion does establish a policy transformation, including for truth-apt historical inputs ([EPI-RTE-watchout-conversion](#epi-rte-watchout-conversion)).

Frequency and recency select visibility, not corroboration. Text-key merging preserves counters but can erase distinctions and version lineage. Long-term memory represents the current merged index, not the full evidence history. No source-supported semantic rejection/retraction route removes a false belief from every downstream copy: overwriting a core item need not change daily/monthly text or process notes ([EPI-RTE-core-ranking](#epi-rte-core-ranking), [EPI-RTE-index-migration](#epi-rte-index-migration), [EPI-CLM-full-history](#epi-clm-full-history)). This is a bounded implementation finding over the inspected file, not a claim that users cannot manually edit memory.

Operational authority is real but bounded: update code admits retained candidates; rankers determine prominence; returned hidden text and system policy can influence the foreground model on later turns/sessions. No semantic acceptance is needed for these paths. Actual consultation, changed decisions and benefit remain unobserved ([RT-BAP-memory-policy](runtime.md#rt-bap-memory-policy)). No model-weight update is implemented by this package; inaccessible provider behavior stays unresolved ([RT-CMP-reflection-model](runtime.md#rt-cmp-reflection-model)).

Learning, reflection, theory construction and self-improvement remain separate. The theory account in [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) supports localized-rule affordance and wired trace-to-memory-to-context organization, not observed content-directed criticism, iterative theory revision or improved capacity. For extension-owned memory/context organization across sessions, avoiding repeated mistakes is an independently stated objective. Evidence-responsive update and a later behavioral-authority path are wired; causal dependence of subsequent operation on that change (self-improvement link 4) and successful improvement are unestablished. This supports a dispositional improvement-directed pathway, not exercised or successful self-improvement. Manual control changes are policy updates, not learning from an evaluator's result.

## Shared records

### Operative objects

#### EPI-OBJ-conversation-signals
Label: Selected conversation and execution signals

Part of: [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)

This object is a material input part of the runtime route, not a duplicate route. Source-native identity: `conversationText` and `executionSignals`. Form: natural-language serialized assertions plus symbolically selected error classifications; substrate: transient strings. The host supplies branch messages; code excludes recognized cancellations, takes a tail, and classifies error-tool text. Original message truth and conversion fidelity remain unknown. SRC-1, `extensions/self-learning.ts`, implementation.

> const conversationText = serializeConversation(convertToLlm(messages as any));
> --- `extensions/self-learning.ts`

> if (!isError) continue;
>
> if (PERMISSION_DENIED_PATTERN.test(text)) {
>   push(`Tool ${toolName} failed with a permission denial: ${textPreview}`);
>   continue;
> }
> --- `extensions/self-learning.ts`

#### EPI-OBJ-reflection-items
Label: Parsed reflection and daily text

Part of: [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)

Source-native identity: `LearningReflection`, `parsed`, daily Markdown. Form: natural-language string items in symbolic arrays/sections; substrate: completion response, process object and daily files. This is the admitted candidate content part of the runtime route; [RT-OBJ-runtime-notes](runtime.md#rt-obj-runtime-notes) is a distinct shortened derivative. Claimed role is identifying what went wrong/how fixed. Neither array requires a truth-apt sentence or evidence link. SRC-1, `extensions/self-learning.ts`, implementation; parser passages also retained in the parent record.

> lines.push("### What went wrong");
> if (reflection.mistakes.length === 0) lines.push("- (none)");
> for (const item of reflection.mistakes) lines.push(`- ${item}`);
> --- `extensions/self-learning.ts`

#### EPI-OBJ-index-items
Label: Core index items and rendered views

Source-native identity: `CoreIndexRecord`, `core/index.json`, `core/CORE.md`, `long-term-memory.md`. Form: natural-language rules and assertions, symbolic keys/kinds/counters/timestamps; substrate: JSON/Markdown disk files. Material output/input across [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill), therefore not part of exactly one supplied record. No supplied operative-object counterpart; runtime notes are separate process prefixes. Claimed role is durable/ranked learning history. Text is not linked per item to supporting events. SRC-1, `extensions/self-learning.ts`, implementation.

> type CoreIndexRecord = {
>   key: string;
>   text: string;
>   kind: CoreKind;
>   hits: number;
>   score: number;
>   firstSeen: string;
>   lastSeen: string;
> };
> --- `extensions/self-learning.ts`

#### EPI-OBJ-monthly-text
Label: Monthly summary text

Part of: [RT-RTE-month-summary](runtime.md#rt-rte-month-summary)

Source-native identity: `summary`, `monthly/YYYY-MM.md`. Natural-language content in Markdown on disk; generated from selected daily files and optional later context. Distinct from daily candidates and index views in source and admission criterion. No supplied object counterpart. Model truth/faithfulness not inspected. SRC-1, `extensions/self-learning.ts`, implementation and embedded doctrine/design.

> "Return markdown with these sections:",
> "- Wins",
> "- Recurring issues",
> "- Most important learnings",
> --- `extensions/self-learning.ts`

### Routes

#### EPI-RTE-watchout-conversion
Label: Mistake to watch-out conversion

Part of: [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection)

Endpoints: parsed mistakes → `updateCoreFromReflection` → normalized anti-pattern entries → index/rendering. Owner is deterministic extension code, not another model judgment. This splits a material policy conversion from the parent's broader proposal/admission/write route. The model proposes mistakes; code decides conversion without human approval or expected-answer oracle. Mode is open session reflection; admitted mistakes trigger it under unchanged prevention guidance. Recovery is external editing/conditional Git, not automatic semantic rollback.

- Immediate return: Updated file paths from parent update call.
- Later read-back: Watch-outs enter core/long-term and later foreground context or consultation.
- Delegated visibility: No separate delegation; renderers receive resulting text/kind.
- Selection predicate: Every admitted mistake string; whitespace normalized.
- Invalidation or expiry: Exact normalized-key merging/ranking, not semantic falsification or expiry.
- Activation or effect: Conversion and downstream writes wired; model interpretation unobserved.
- Evidence limits: Implementation deduction, no target execution or observed content.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `extensions/self-learning.ts`, implementation:

> ...reflection.mistakes.map((text) => ({ text: `Avoid: ${text}`, kind: "antiPattern" as const })),
> --- `extensions/self-learning.ts`

Concrete symbolic trace: admissible input `{"mistakes":["The command failed yesterday."],"fixes":[]}` survives `parseReflection`; conversion produces `Avoid: The command failed yesterday.` with kind `antiPattern`. Normalization preserves those words, and `learningKey` lowercases the key. The historical proposition does not entail an avoidance policy, and adding a prefix does not turn it into a sound imperative. Rendering strips that prefix under Watch-outs. This deduction disproves a universal meaning-preserving-reshaping account of mistake conversion without claiming this input occurred. It establishes no new checked truth-apt conclusion. Potential localized theories depend on actual prose; the parent theory account's independent limits remain applicable.

#### EPI-RTE-core-ranking
Label: Core index merging and ranking

Source-native endpoints: admitted reflection/rewrite → normalized-key merge → score/hit/time updates → ranked balanced core and all-index long-term render. This spans [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill); it is a shared deterministic maintenance stage, not a duplicate of either full route. Code owns decisions. No human judges particular entries; no answer oracle compares scores to truth or outcome. Trigger is text admission/rewrite, not measured improvement. It changes visibility and retained organization under unchanged selection rules.

- Immediate return: Rendered file paths and updated index; redistill also exposes counts.
- Later read-back: Selected core is bundled by default; all current merged items appear in long-term file referenced by policy.
- Delegated visibility: Renderers see item text/kind and metadata, not original supporting sessions.
- Selection predicate: Normalized lowercase text keys; score/age ordering, hits/time tie-breaks, kind balancing and size limit.
- Invalidation or expiry: Core exclusion does not delete index entries; rewrites replace text/keys and merge collisions. No semantic invalidation.
- Activation or effect: File rewrite/ranking wired; foreground reliance unobserved.
- Evidence limits: Scores show repetition/recency only; no correctness or benefit measurement. Writes are not transactional; optional Git permits only conditional manual recovery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `extensions/self-learning.ts`, implementation:

> function learningKey(text: string): string {
>   return normalizeLearningText(text).toLowerCase();
> }
> --- `extensions/self-learning.ts`

> const recencyPenalty = ageDays * 0.05;
> return item.score - recencyPenalty;
> --- `extensions/self-learning.ts`

> const repetitionBonus = Math.min(1, existing.hits * 0.08);
> existing.score += incrementBase + repetitionBonus;
> --- `extensions/self-learning.ts`

> existing.hits += item.hits;
> existing.score += item.score;
> --- `extensions/self-learning.ts`

A counterexample to corroboration: repeating the same unsupported output raises hits and score by this code; no independent observation need occur. Case-normalized equality also cannot prove equivalence of case-sensitive code identifiers. This is symbolic ranking/merge, not claim-directed criticism; theories that may occur in retained prose are not independently evaluated here.

#### EPI-RTE-index-migration
Label: Core index migration fallback

Source-native endpoints: `loadCoreIndex` → missing/invalid-index fallback → `ensureCoreFile`/`parseCoreItems` → default index records. Extension code owns recovery; local Markdown supplies content without human approval at load time. Overlaps [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill), not contained in exactly one. No supplied standalone counterpart. This imports prior text rather than producing verified claims. There is no answer oracle or semantic evaluation; the trigger is structural load failure/missing index, operating mode deterministic recovery under unchanged defaults.

- Immediate return: In-memory version-1 index; can create missing default core file.
- Later read-back: Subsequent update/redistill can save migrated items and rendered views for future contexts.
- Delegated visibility: Index consumers receive bullets plus invented default counters/current timestamps, not lost index history.
- Selection predicate: Valid index items win; fallback takes every trimmed `- ` bullet except `(none yet)`.
- Invalidation or expiry: A later valid index takes priority; no source-age check or semantic invalidation.
- Activation or effect: Recovery/migration wired; actual migrations unobserved.
- Evidence limits: Earlier source/provenance unavailable; defaults do not prove historical frequency, timing or endorsement. No automatic restoration of corrupted index.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `extensions/self-learning.ts`, implementation:

> const corePath = ensureCoreFile(root);
> const migrated = parseCoreItems(readFileSync(corePath, "utf-8")).map((text) => ({
>   key: learningKey(text),
>   text,
>   kind: text.toLowerCase().startsWith("avoid:") ? ("antiPattern" as const) : ("learning" as const),
>   hits: 1,
>   score: 1,
>   firstSeen: new Date().toISOString(),
>   lastSeen: new Date().toISOString(),
> }));
> --- `extensions/self-learning.ts`

Countercase: rendered Watch-outs omit `Avoid:`; fallback migration classifies them as learning unless the remaining text itself begins with that prefix. Therefore migration does not guarantee preservation of kind or complete index history. It supplies structural recovery, not epistemic acceptance or a theory-criticism cycle.

### Claims

#### EPI-CLM-prevention-scope
Label: Mistake prevention and cross-project reuse

Claimed operation: extract mistakes/fixes and, in global mode, generate reusable rules. No identical supplied claim record; [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) retains the prompt's prevention focus and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill) retains preservation intent. This claim concerns intended prevention/reuse, distinct from [RT-CLM-strict-consultation](runtime.md#rt-clm-strict-consultation). SRC-1, `README.md` and embedded prompt in `extensions/self-learning.ts`, doctrine/design, not measured benefit.

> - `storage.mode: "global"` distills reflections into cross-project, reusable action rules and avoids project-specific identifiers.
> --- `README.md`

> "- Distill each item into a cross-project rule that is reusable in any repository.",
> --- `extensions/self-learning.ts`

#### EPI-CLM-full-history
Label: Full history in long-term memory

Claimed operation: long-term file holds full history. No counterpart among supplied claims; related runtime routes are [RT-RTE-task-reflection](runtime.md#rt-rte-task-reflection) and [RT-RTE-core-redistill](runtime.md#rt-rte-core-redistill). SRC-1, `README.md`, doctrine/design; implementation renders current merged index, not an append-only evidence ledger.

> 4. writes full history to `long-term-memory.md`,
> --- `README.md`

> const sorted = sortedIndexItems(index);
> const learnings = sorted.filter((x) => x.kind === "learning");
> const antiPatterns = sorted.filter((x) => x.kind === "antiPattern");
>
> const content = [
>   "# Long-term Memory",
> --- `extensions/self-learning.ts`
