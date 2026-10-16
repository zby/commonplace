---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Signet epistemic routes: source matching, semantic maintenance, aggregate-recall admission, withdrawal and benchmark judgment."
run-id: AAS-2026-10-14-signetai-64f703d83203-01
reviewed-boundary: "12dba1ce753babda735f2ba7b6f150c6c0b7f95e"
---

# Signet epistemic report

## Source-and-claim boundary

The question is which Signet routes acquire or transform truth-apt content, check it, authorize later reliance and revoke that authorization. Scope and external exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All new inspection below is SRC-1 implementation unless marked doctrine/design. No execution, model output, verified benchmark result or causal experiment is supplied. Model weights and external hosts remain outside the frozen source. Their truth checks, compliance, learning and exact model versions cannot be inferred from Signet's interfaces; see [RT-CMP-inference-router](runtime.md#rt-cmp-inference-router).

The runtime is provisional, not exhaustive. Direct inspection found a consequential additional route: aggregate recall can synthesize and save semantic memory outside a Dreaming pass. This qualifies any reading of Dreaming as the exclusive semantic writer, but does not invalidate the runtime's explicitly bounded maintenance account. See [EPI-RTE-aggregate-synthesis](#epi-rte-aggregate-synthesis) and [EPI-RTE-aggregate-retention](#epi-rte-aggregate-retention). Public claims assessed are [EPI-CLM-source-connections](#epi-clm-source-connections), [EPI-CLM-benchmark-accuracy](#epi-clm-benchmark-accuracy), and the supplied tool-boundary claim [RT-CLM-tool-boundary](runtime.md#rt-clm-tool-boundary).

### Coverage

Direct source reads and supplied findings are distinct. Available but unread operations below prevent a system-complete negative about acceptance, evaluators or semantic checks.

| Entry point or operation | Source path | Coverage and records, or limit |
| --- | --- | --- |
| CLI dispatch | SRC-1 `surfaces/cli/src/cli.ts` | Direct registration search: memory, knowledge, ontology, hook, source and Dream commands are shipped; command-body equivalence not inspected. |
| Pi lifecycle and hook delivery | SRC-1 `integrations/pi/extension/src/index.ts`, `platform/daemon/src/hooks.ts` | Supplied [RT-RTE-pi-lifecycle](runtime.md#rt-rte-pi-lifecycle), [RT-BAP-host-context](runtime.md#rt-bap-host-context); no independent reinspection of budget selectors. |
| Direct remember and structured input | SRC-1 `platform/daemon/src/routes/memory-routes.ts`, `platform/daemon/src/mcp/tools.ts` | Supplied [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember); direct MCP registration search confirms recall, aggregate options, remember and forget exposure. Full direct-ingest transaction not re-traced. |
| Dreaming proposal and operation checks | SRC-1 `platform/daemon/src/pipeline/dreaming-operations.ts`, `platform/daemon/src/pipeline/dreaming-capabilities.ts` | Direct citation/validation reads and capability-registration searches; supplied [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass). Structural and hygiene exceptions prevent a universal quote requirement. |
| Memory head support and removal | SRC-1 `platform/daemon/src/memory-head-owner.ts` | Direct reads; [EPI-RTE-head-support](#epi-rte-head-support), [EPI-RTE-head-publication](#epi-rte-head-publication). Full file-to-host reload beyond supplied lifecycle remains uninspected. |
| Aggregate recall | SRC-1 `platform/daemon/src/aggregate-recall.ts`, `platform/daemon/src/routes/memory-routes.ts` | Direct synthesis, guard, transaction and final-result reads; [EPI-RTE-aggregate-synthesis](#epi-rte-aggregate-synthesis), [EPI-RTE-aggregate-guard](#epi-rte-aggregate-guard), [EPI-RTE-aggregate-retention](#epi-rte-aggregate-retention), [EPI-RTE-aggregate-delivery](#epi-rte-aggregate-delivery). Query-expansion and cache-refresh internals not fully inspected. |
| Deterministic normalization | SRC-1 `platform/daemon/src/content-normalization.ts` | Complete direct read; [EPI-RTE-content-normalization](#epi-rte-content-normalization). Native fallback selection visible, native implementation uninspected. |
| Supersession | SRC-1 `platform/daemon/src/routes/memory-routes.ts`, `platform/daemon/src/transactions.ts`, `platform/daemon/src/memory-head-owner.ts` | Direct endpoint, transaction and current-source reads; [EPI-RTE-memory-supersession](#epi-rte-memory-supersession). Forget/recover endpoints were located, not traced through their consumers; prevents comprehensive restoration/withdrawal assurance. |
| Recall selection | SRC-1 `platform/daemon/src/memory-search.ts` | Direct selected response and access-tracking read; exhaustive ranking and visibility predicates uninspected. Neither access counters nor selected delivery prove endorsement. |
| MemoryBench evaluator | SRC-1 `memorybench/src/orchestrator/phases/evaluate.ts`, `memorybench/src/judges/base.ts` | Complete direct reads; [EPI-RTE-benchmark-judgment](#epi-rte-benchmark-judgment), [EPI-RTE-benchmark-checkpoint](#epi-rte-benchmark-checkpoint). Dataset/reference validity, actual judge implementations and protocol-specific evaluators remain uninspected. |
| Alternate executor | SRC-1 `platform/daemon/src/inference-router.ts`, `platform/daemon/src/pipeline/acpx-dreaming-mcp.ts` | Supplied [RT-RTE-alternate-executor](runtime.md#rt-rte-alternate-executor); external evaluator/tools opaque. |
| Other material included paths | SRC-1 `platform/daemon/src/transcript-capture.ts`, `scripts/claim-trace-eval.ts`, `scripts/observer-belief-eval.ts`, `platform/daemon/src/mcp/tools.ts` | Capture normalization, feedback, other registered graph tools, evaluation scripts, source imports, ontology review/recovery, history summarization, identity generation and other host adapters not fully inspected. Their presence is not absence of a truth check; no whole-system negative is supported. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-pass-prompt](runtime.md#rt-obj-pass-prompt) | see record | see record | see record | Guidance requests interpretation; not an observed accepted claim. |
| [EPI-OBJ-memory-entries](#epi-obj-memory-entries) | see record | see record | see record | Exact support is not semantic entailment. |
| [EPI-OBJ-aggregate-evidence](#epi-obj-aggregate-evidence) | see record | see record | see record | Retrieved content's original truth warrant unknown. |
| [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer) | see record | see record | see record | No actual output instance supplied; truth-apt scope is intended memory facts. |
| [EPI-OBJ-normalized-content](#epi-obj-normalized-content) | see record | see record | see record | Storage representation differs from dedupe representation. |
| [EPI-OBJ-judge-result](#epi-obj-judge-result) | see record | see record | see record | Evaluation labels concern benchmark answers, not all stored propositions. |

## Authority-route ledger

Fields owned by declaring records are referenced rather than copied. Architectural status describes source support, not observed activation. For every row below, possible results, consumers, timing, license and limits are in the cited route record.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember) | operational admission/selection/consumption | implemented | see route | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | Import warrant unknown; schema validity is not source truth | see route | see route | see route | none | none | Human authorship unresolved; retention does not establish acceptance. |
| [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass) | content transformation | implemented | [RT-OBJ-pass-prompt](runtime.md#rt-obj-pass-prompt) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Requested extraction lacks checked semantic entailment | see route | see route | see route | [EPI-CLM-source-connections](#epi-clm-source-connections) | none | No observed input/output pair distinguishes reshaping, derivation or conjecture. |
| [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass) | check/evidence production | implemented | see route | no content change | see route | see route | see route | see route | see route | Scoped exact-source matching, not truth adjudication | see route | see route | see route | [RT-CLM-tool-boundary](runtime.md#rt-clm-tool-boundary) | none | Direct source reading confirms exceptions for structural and hygiene writes. |
| [RT-RTE-pi-lifecycle](runtime.md#rt-rte-pi-lifecycle) | operational admission/selection/consumption | implemented | see route | no content change | see route | see route | see route | see route | see route | No additional epistemic license from startup delivery | see route | see route | see route | none | none | Host uptake unobserved; see [RT-BAP-host-context](runtime.md#rt-bap-host-context). |
| [EPI-RTE-content-normalization](#epi-rte-content-normalization) | content transformation | implemented | [EPI-OBJ-normalized-content](#epi-obj-normalized-content) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | none | Confined to storage formatting; normalized hash equivalence need not preserve meaning. |
| [EPI-RTE-head-support](#epi-rte-head-support) | check/evidence production | implemented | [EPI-OBJ-memory-entries](#epi-obj-memory-entries) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-source-connections](#epi-clm-source-connections) | none | Provenance check, not acceptance of the entry's truth. |
| [EPI-RTE-head-publication](#epi-rte-head-publication) | retention | implemented | [EPI-OBJ-memory-entries](#epi-obj-memory-entries) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-source-connections](#epi-clm-source-connections) | none | Operational commit acceptance is not evidence-consuming truth acceptance. |
| [EPI-RTE-aggregate-synthesis](#epi-rte-aggregate-synthesis) | content transformation | implemented | [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | additional semantic route | Output semantics not observed; instruction alone does not establish non-ampliative transformation. |
| [EPI-RTE-aggregate-guard](#epi-rte-aggregate-guard) | check/evidence production | implemented | [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | none | Eligibility/style domain only. |
| [EPI-RTE-aggregate-retention](#epi-rte-aggregate-retention) | retention | implemented | [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | additional semantic route | Source links do not establish accepted ampliative knowledge or lifecycle integration after acceptance. |
| [EPI-RTE-aggregate-delivery](#epi-rte-aggregate-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | save rejection need not block use | Final returned text is credential-redacted; source-memory metadata excludes ontology source IDs. |
| [EPI-RTE-memory-supersession](#epi-rte-memory-supersession) | lineage/freshness/recovery | implemented | see route | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | none | none | Supersession changes eligibility, not demonstrated falsity of old content. |
| [EPI-RTE-benchmark-judgment](#epi-rte-benchmark-judgment) | check/evidence production | implemented | [EPI-OBJ-judge-result](#epi-obj-judge-result) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-benchmark-accuracy](#epi-clm-benchmark-accuracy) | none | Model judgment or opaque protocol; no evaluator calibration supplied. |
| [EPI-RTE-benchmark-checkpoint](#epi-rte-benchmark-checkpoint) | retention | implemented | [EPI-OBJ-judge-result](#epi-obj-judge-result) | no content change | see route | see route | see route | see route | see route | see route | see route | see route | see route | [EPI-CLM-benchmark-accuracy](#epi-clm-benchmark-accuracy) | none | Lab result, not product knowledge admission. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-source-connections](#epi-clm-source-connections) | see record | see record | see record | [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass), [EPI-RTE-head-support](#epi-rte-head-support), [EPI-RTE-head-publication](#epi-rte-head-publication) | none supplied | No intervention; structural/hygiene exceptions in inspected operations | Scoped provenance machinery exists for selected semantic/head writes | “Every connection” is not established as a whole-graph invariant; source links do not certify truth. |
| [EPI-CLM-benchmark-accuracy](#epi-clm-benchmark-accuracy) | see record | see record | see record | [EPI-RTE-benchmark-judgment](#epi-rte-benchmark-judgment), [EPI-RTE-benchmark-checkpoint](#epi-rte-benchmark-checkpoint) | Reported score only; no inspected run | No component variation or verified comparison | Shipped evaluation can score answers against references and retain results | 97.6% not verified; answer success would not establish extraction mechanism or transfer. |
| [RT-CLM-tool-boundary](runtime.md#rt-clm-tool-boundary) | see record | see record | see record | [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass), [RT-RTE-alternate-executor](runtime.md#rt-rte-alternate-executor) | see record | see record | Bounded Pi worker configuration and daemon checks | Neither a whole-system write restriction nor an epistemic oracle. |

## Bounded conclusion

Signet has implemented acquisition, model-guided interpretation, scoped provenance checking, retained source-linked projections and advisory host delivery. Direct remember imports caller text with unknown source warrant. The selected Dreaming operation checks and memory-head checks license exact correspondence to eligible source text, not truth or entailment of the model's claim. They can block publication for invalid provenance, scope, pass state or head freshness; they do not establish an accepted ampliative claim under a named truth criterion, intended use and scope. Structural and hygiene exceptions are real counterexamples to a universal episodic-quote rule. See [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember), [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass), [EPI-RTE-head-support](#epi-rte-head-support).

The TypeScript storage-normalization path can be understood without execution: it preserves the chosen sentence while changing newline/edge formatting. Its dedupe representation additionally collapses case and punctuation; equality in that representation is not a truth judgment. See [EPI-RTE-content-normalization](#epi-rte-content-normalization). No new entailed factual proposition from warranted premises is established by that path.

Aggregate recall is an independent model-based semantic-production and optional persistence route. Its prompt requests evidence-only stable facts; no output pair establishes whether a realized answer preserves, derives or adds claims. Its save gate checks eligible evidence classes and surface form, not whether the answer follows from the evidence. A surface-form rejection can still return an unsaved answer to the caller. Source links and embeddings make admitted text available for later reliance without demonstrating epistemic acceptance or post-acceptance lifecycle integration. Immediate delivery has advisory force; retention has durable recall potential. See [EPI-RTE-aggregate-synthesis](#epi-rte-aggregate-synthesis), [EPI-RTE-aggregate-guard](#epi-rte-aggregate-guard), [EPI-RTE-aggregate-retention](#epi-rte-aggregate-retention), [EPI-RTE-aggregate-delivery](#epi-rte-aggregate-delivery).

Supersession is an implemented withdrawal-related route: the transaction records replacement and invalidates derived memories, and a superseded memory cannot pass the head's current-source eligibility check. This is a bounded downstream consequence, not proof of withdrawal from already delivered host context or every recall branch. See [EPI-RTE-memory-supersession](#epi-rte-memory-supersession).

MemoryBench is a separate evidence-consuming evaluator of answer hypotheses against benchmark references or rubrics. Its parser checks response consistency, and its checkpoint consumer records correctness and completion, suppressing repeat evaluation on resume. This does not approve individual product memories or demonstrate that model judgment is reliable. No supplied observation verifies the public accuracy score or supports causal component attribution. See [EPI-RTE-benchmark-judgment](#epi-rte-benchmark-judgment), [EPI-RTE-benchmark-checkpoint](#epi-rte-benchmark-checkpoint).

Missing provider internals, execution traces, actual semantic outputs, dataset validation and unread material routes bound these conclusions separately. They prevent claims of exercised learning, successful self-improvement, theory-directed criticism or a system-complete absence of truth acceptance. Persistence and scheduled maintenance are architectural contributions, not substitutes for independent evidence of those properties. No single epistemic verdict follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memory-entries
Label: Memory head entries

Natural-language `canonical_text` is retained in SQLite `memory_head_entries`; symbolic entry IDs, revision membership and provenance JSON determine publication/support eligibility. Entries are intended truth-apt remembered facts within the agent scope. This is a material output part distinct from the input prompt [RT-OBJ-pass-prompt](runtime.md#rt-obj-pass-prompt); no supplied object denotes this entry set. SRC-1 `platform/daemon/src/memory-head-owner.ts`.

> const support = (parsed as Record<string, unknown>[]).filter(
> (item) => supportError(db, agentId, row.entryId, item, evidence) === null,
> );
> if (support.length > 0) entries.push({ entryId: row.entryId, text: row.text, support });
> --- `platform/daemon/src/memory-head-owner.ts`

#### EPI-OBJ-aggregate-evidence
Label: Aggregate recall evidence

Natural-language `RecallResult.content` with symbolic IDs, types and timestamps is an in-memory selected evidence array. Its intended role is premises for a stable memory note, not a new source of truth. Truth-apt facts are acquired from already retained content; their source warrant is unknown. Distinct from the guidance object [RT-OBJ-pass-prompt](runtime.md#rt-obj-pass-prompt) and from direct admission [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember): this is retrieved input for an additional route. SRC-1 `platform/daemon/src/aggregate-recall.ts`.

> const evidence = uniqueEvidence(recalls.flatMap((result) => result.results));
> const evidenceIds = evidence.map((row) => row.id);
> --- `platform/daemon/src/aggregate-recall.ts`

#### EPI-OBJ-aggregate-answer
Label: Aggregate recall answer

Natural-language model text exists first in memory and may enter SQLite `memories` as a semantic row. Symbolic `sourceType`, source links and visibility govern its retention and later eligibility. Its intended truth-apt domain is stable facts relevant to the recall question; no concrete answer instance is supplied. This is not the maintenance prompt or its pass output: compare [RT-OBJ-pass-prompt](runtime.md#rt-obj-pass-prompt), [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass). SRC-1 `platform/daemon/src/aggregate-recall.ts`.

> why: "aggregate recall",
> project,
> importance: 0.75,
> type: "semantic",
> tags: "aggregate,recall",
> --- `platform/daemon/src/aggregate-recall.ts`

#### EPI-OBJ-normalized-content
Label: Normalized memory content

`NormalizedMemoryContent` carries natural-language `storageContent` and a separate symbolic dedupe/hash representation (`normalizedContent`, `hashBasis`, `contentHash`) in memory. Storage content can carry caller propositions; the hash is not a proposition about their truth. A material normalization part of the supplied direct-admission route, not a duplicate retained-memory object. SRC-1 `platform/daemon/src/content-normalization.ts`.

Part of: [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember)

> readonly storageContent: string;
> readonly normalizedContent: string;
> readonly hashBasis: string;
> readonly contentHash: string;
> --- `platform/daemon/src/content-normalization.ts`

#### EPI-OBJ-judge-result
Label: Benchmark judge result

Symbolic binary score/label/pass and natural-language explanation are held in a result object then a run checkpoint. The truth-apt judgment is whether a benchmark answer meets the reference/rubric for its question, not whether Signet's graph is true. No counterpart exists in supplied runtime records: [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass) expressly has no expected-answer oracle in its maintenance seam. SRC-1 `memorybench/src/judges/base.ts`, `memorybench/src/orchestrator/phases/evaluate.ts`.

> if ((parsed.score === 1) !== (parsed.label === "correct")) {
> throw new Error("Judge response score and label disagree")
> }
> --- `memorybench/src/judges/base.ts`

### Routes

#### EPI-RTE-content-normalization
Label: Content normalization

Part of: [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember)

The caller's text enters the TypeScript normalization functions, producing storage text and a separate hash basis; fixed code owns progression. SRC-1 `platform/daemon/src/content-normalization.ts`. This is the formatting part of admission, not another acquisition route. With native loading unsuccessful, concrete input `"  Alice moved.\r\n  "` becomes storage `"Alice moved."`, normalized text and hash basis `"alice moved"`, and SHA-256 of that basis. This deduction uses implementation, not target execution. The storage edge is non-ampliative reshaping for this input: the same sentence remains. The dedupe edge intentionally discards case and terminal punctuation and therefore cannot certify semantic equivalence for arbitrary propositions (for example quoted case-sensitive identifiers).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: storageContent, normalizedContent, hashBasis and contentHash.
- Later read-back: uninspected — normalization feeds ingestion, but downstream dedupe consumers were not completely traced.
- Delegated visibility: caller text is available to fixed code; no model judgment occurs here.
- Selection predicate: native implementation if loaded; otherwise the inspected TypeScript branch.
- Invalidation or expiry: current-call result; retained hashes depend on ingestion, not an expiry in this function.
- Activation or effect: changes text representation and hash input; does not establish truth or source endorsement.
- Evidence limits: concrete deduction confined to TypeScript branch; native behavior uninspected.

Evaluator/target/domain: deterministic newline, whitespace, case and punctuation rules over strings, not factual verification. Force: returned representation for admission/dedupe code in the current call. Epistemic license: none added. No human approval, oracle, novel proposition or epistemic acceptance is involved.

> function tsNormalizeContentForStorage(content: string): string {
> return content.replace(CRLF, "\n").trim();
> }
> --- `platform/daemon/src/content-normalization.ts`

> const lowered = storageContent.toLowerCase();
> return lowered.replace(COLLAPSE_WHITESPACE, " ").replace(TRAILING_PUNCTUATION, "").trim();
> --- `platform/daemon/src/content-normalization.ts`

#### EPI-RTE-head-support
Label: Memory head support check

Part of: [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass)

Model-selected entry/support pairs → daemon `supportError` → admissible pair or error. The program checks quote occurrence in rendered canonical scoped evidence; source lookup checks current memory eligibility and source completion. This is the checking part of head maintenance, separate from publication. SRC-1 `platform/daemon/src/memory-head-owner.ts`; object [EPI-OBJ-memory-entries](#epi-obj-memory-entries).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: null for valid support or INVALID_PROVENANCE error.
- Later read-back: committedEntries rechecks retained provenance and omits entries with no valid support; unverifiable metadata is separately flagged.
- Delegated visibility: model supplies entry text and support references/quotes; daemon reads complete rendered sources in the agent scope.
- Selection predicate: supported source-ref classes, nonempty quote, eligible current source, exact substring occurrence.
- Invalidation or expiry: deleted, superseded, stale or archived memory sources fail currentSource; incomplete source captures fail completion eligibility.
- Activation or effect: commitEntries rejects failed support; committedEntries uses checks to select carried entries.
- Evidence limits: exact occurrence does not test whether entry text is entailed by the quote, whether the quote is true, or whether conflicting evidence exists.

Target/domain: source identity/eligibility and verbatim correspondence, not the candidate proposition's truth. Evaluator is fixed daemon code before write or carry-forward selection. The model proposes; code vetoes; no per-entry human decision or expected-answer oracle is established. The returned error enforces a provenance condition for the current commit; null permits further processing, not unconditional publication. Epistemic authority is bounded correspondence to eligible source text. Behavioral path: supportError result → commitEntries/committedEntries → enforced publication or carried-entry selection, current pass and later head reads. The source interpretation remains indeterminate between reshaping, entailed derivation and conjecture.

> if (rendered === null || !rendered.includes(quote))
> return { code: "INVALID_PROVENANCE", error: `entry ${entryId} quote is not exact scoped evidence` };
> return null;
> --- `platform/daemon/src/memory-head-owner.ts`

> return source?.completed === true ? source : null;
> --- `platform/daemon/src/memory-head-owner.ts`

#### EPI-RTE-head-publication
Label: Memory head publication

Part of: [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass)

Model entry set → authorized content-pass head commit → revision/entry tables and pending publication. Code owns disposition and persistence after [EPI-RTE-head-support](#epi-rte-head-support); this record concerns retained membership, not a second truth check. SRC-1 `platform/daemon/src/memory-head-owner.ts`, `platform/daemon/src/pipeline/dreaming-capabilities.ts`; object [EPI-OBJ-memory-entries](#epi-obj-memory-entries).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: accepted commit, NOOP, or rejection such as PASS_NOT_AUTHORIZED, STALE_HEAD or INVALID_HEAD.
- Later read-back: committedEntries reconstructs the last published supported entry set for later passes; exact host reload after publication uninspected.
- Delegated visibility: model submits complete entries, not direct SQLite statements; daemon sees pass/head revisions and retained support.
- Selection predicate: running scoped incremental-content pass, matching base revision, input budget and support; unchanged current hash can return NOOP before revalidating supplied support.
- Invalidation or expiry: omitted active entries become removed; an empty replacement is blocked if carried entries still have valid or unverifiable support.
- Activation or effect: commitEntries creates revision/entries; head metadata and pending publication change on success; content-pass finalization governs durability as supplied runtime establishes.
- Evidence limits: code's accepted commit is operational acceptance of a publication request, not acceptance of factual truth against a substantive criterion.

Trigger/change/guidance: scheduled or requested maintenance submits retained memory entries under the tool's complete-set and budget instructions. Model proposes; daemon vetoes for authorization, stale revision, invalid support and clearing rules. No human per-entry approval or answer oracle appears here. Recovery: stale rejection requires a fresh proposal; supplied runtime distinguishes staged head finalization from earlier committed ontology operations. Criterion/intended use/scope: eligible provenance and publication constraints for agent-scoped MEMORY.md, not a truth criterion. Epistemic license adds no warrant beyond eligible source correspondence. Operational path: fixed head writer → revision membership and publication queue → retained memory projection for later reads; enforcing now, potentially advisory at host consumption. This is retention, not established post-epistemic-acceptance integration.

> if (head?.is_current === 1 && currentHash === contentHash)
> return { ok: true, code: "NOOP", revision, hash: contentHash, changed: false, changedIds: [] };
> --- `platform/daemon/src/memory-head-owner.ts`

> if (retained.has(old.entry_id)) continue;
> db.prepare(
> "UPDATE memory_head_entries SET status='removed', last_revision=?, updated_at=? WHERE agent_id=? AND entry_id=?",
> ).run(nextRevision, now, input.agentId, old.entry_id);
> --- `platform/daemon/src/memory-head-owner.ts`

#### EPI-RTE-aggregate-synthesis
Label: Aggregate recall synthesis

Selected recall evidence → rendered prompt → inference-router execute → trimmed answer/null. Model proposes candidate facts and code handles nonempty output. Distinct from [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass): invoked by aggregate recall, no Dreaming pass/tool loop required. Compare shared model-selection machinery [RT-CMP-inference-router](runtime.md#rt-cmp-inference-router); no new distributed-parametric component identity is established. SRC-1 `platform/daemon/src/aggregate-recall.ts`; inputs [EPI-OBJ-aggregate-evidence](#epi-obj-aggregate-evidence), output [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: answer string or null with routed usage; downstream failure falls back to retrieved evidence.
- Later read-back: answer can enter optional aggregate retention and later recall; synthesis alone does not persist it.
- Delegated visibility: model receives query plus selected content, IDs, creation dates and types, not all underlying sources or full graph.
- Selection predicate: evidence exists and router available; prompt asks for evidence-only stable facts; routed execution returns nonempty text.
- Invalidation or expiry: 30-second timeout supplied to router; failed/empty synthesis yields no generated answer.
- Activation or effect: creates a candidate for caller delivery and optional storage, outside Dreaming maintenance.
- Evidence limits: implemented request for grounded synthesis does not establish compliance, entailment or non-entailment of an actual answer.

Relation: truth-apt transformation indeterminate; remaining possibilities are non-ampliative reshaping, entailed derivation and ampliative conjecture. Need actual source/output propositions and checked interpretation to distinguish them. Epistemic license: none newly established by fluency or router success; source warrant unknown. Operational path: model output → aggregateRecall → optional save and immediate API result, advisory to a caller. Operating mode is open recall, no expected-answer oracle or human per-answer approval. Guidance persists as shipped prompt; model result may persist separately. No accepted ampliative knowledge-production result is established.

> "Write one concise atomic memory note from the memory evidence below.",
> "Use only the evidence.",
> --- `platform/daemon/src/aggregate-recall.ts`

> const text = result.value.text.trim();
> return {
> answer: text.length > 0 ? text : null,
> usage: usageStage("synthesis", result.value),
> };
> --- `platform/daemon/src/aggregate-recall.ts`

#### EPI-RTE-aggregate-guard
Label: Aggregate save guard

Generated answer and selected evidence → fixed eligibility/style functions → booleans consumed by aggregate saving. This is a distinct check with no counterpart in the supplied direct remember or maintenance route; compare [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember). SRC-1 `platform/daemon/src/aggregate-recall.ts`; candidate [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: booleans for evidence eligibility and answer saveability.
- Later read-back: inapplicable — checks return current-call booleans rather than retained evaluation artifacts.
- Delegated visibility: fixed code inspects row identity/visibility/scope and output text; no human evaluator.
- Selection predicate: nonempty evidence all ontology claims or global unscoped linkable memories; answer at least 12 trimmed characters, not refusal or conversational framing.
- Invalidation or expiry: recomputed for the current save attempt.
- Activation or effect: false prevents persistence in this branch, not immediate answer delivery.
- Evidence limits: checks do not compare the answer's propositions with the evidence.

Target/domain: storage eligibility of evidence and surface-form suitability of memory text. Program is evaluator; model generates candidate; no truth oracle or human per-candidate gate is present. Epistemic license: none regarding factual correctness. Operational path: booleans → aggregate save conditional → permissive/enforcing retention gate for this call only. Counterexample to a truth-acceptance reading: an invented third-person sentence longer than 12 characters that avoids forbidden framing would pass the answer-text condition; this is a deduction about the guard, not a fabricated execution. Evidence eligibility is an independent condition.

> function aggregateAnswerCanBeSaved(text: string): boolean {
> const trimmed = text.trim();
> return trimmed.length >= 12 && !isInsufficientAggregateAnswer(trimmed) && !isConversationalAggregateAnswer(trimmed);
> }
> --- `platform/daemon/src/aggregate-recall.ts`

> isOntologyClaimRow(row) ||
> (isLinkableSourceMemoryRow(row) && row.visibility === "global" && row.scope === null),
> --- `platform/daemon/src/aggregate-recall.ts`

#### EPI-RTE-aggregate-retention
Label: Aggregate memory retention

Eligible synthesis → optional transaction/dedupe → semantic memory with source links and query hint → optional embedding. Fixed code admits/persists model text; not a maintenance-pass effect. Distinct from [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember) because producer, guard and source linkage differ; distinct from [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass) because no pass required. SRC-1 `platform/daemon/src/aggregate-recall.ts`; object [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored/deduplicated row and saved/deduped flags, or an unsaved result.
- Later read-back: saved semantic rows receive source links, query hints and an attempted embedding for later retrieval; exact complete recall eligibility uninspected.
- Delegated visibility: fixed transaction consumes generated answer, source identities, agent/project and chosen visibility; model does not write SQLite directly.
- Selection predicate: saving defaults on unless either save flag is false; evidence and answer guards must pass; duplicates and unique-constraint races have distinct results.
- Invalidation or expiry: source links support derived-memory invalidation; cache-refresh/dedupe internals not completely inspected.
- Activation or effect: transaction persists text and linkage; unsuccessful embedding does not undo saved memory.
- Evidence limits: saved status certifies retention, not truth acceptance or successful later retrieval/use.

Trigger/proposal: aggregate recall requests a generated stable note; model proposes text, program decides saving, caller can disable it. No per-answer human approval or reference oracle. Rejection/recovery: guard rejection returns unsaved content; unique conflicts resolve duplicates or return unsaved; embedding failure is logged after save. Guidance is the evidence-only synthesis prompt. Intended use/scope: future agent/project memory retrieval; admission criteria are save flag, row eligibility and surface form. Epistemic authority: source-linked retained candidate with unknown warrant, not accepted ampliative knowledge. Behavioral path: ingest/source-link/query-hint writes → memory retrieval machinery → potential later advisory content, durable horizon. Linking before epistemic acceptance remains retention/lineage, not established lifecycle integration after acceptance.

> const saveAggregate = params.saveAggregate !== false && params.save_aggregate !== false;
> --- `platform/daemon/src/aggregate-recall.ts`

> linkAggregateEvidenceSources(db, id, evidenceSources, agentId, now);
> linkAggregateQueryHint(db, id, agentId, params.query, now);
> saved = true;
> return loadAggregateMemory(db, id);
> --- `platform/daemon/src/aggregate-recall.ts`

> log.warn("memory", "Aggregate recall memory saved without embedding", {
> --- `platform/daemon/src/aggregate-recall.ts`

#### EPI-RTE-aggregate-delivery
Label: Aggregate answer delivery

Aggregate result → saved or unsaved row → credential-redacted single-row API response. Program consumes synthesis even where save guards fail. No counterpart after comparison with [RT-RTE-pi-lifecycle](runtime.md#rt-rte-pi-lifecycle): explicit recall return is distinct from unsolicited startup injection. SRC-1 `platform/daemon/src/aggregate-recall.ts`; object [EPI-OBJ-aggregate-answer](#epi-obj-aggregate-answer).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: one redacted content row with aggregate flags, queries and memory-source IDs; absent synthesis instead returns retrieved evidence.
- Later read-back: inapplicable — this delivery itself changes no retained content; saving is the separate retention route.
- Delegated visibility: caller receives rendered answer and metadata, not the full evidence array; metadata filters ontology sources out of sourceMemoryIds.
- Selection predicate: successful nonempty synthesis; a save guard failure does not exclude the answer from delivery.
- Invalidation or expiry: response belongs to the current request; caller persistence/expiry is uninspected.
- Activation or effect: can supply generated text to model/tool callers without truth acceptance or persistence.
- Evidence limits: actual caller use, credential-redaction semantic effects and further host filtering uninspected.

Target/condition: deliver available row, not approve its truth. Force: advisory API/tool content to requesting consumer in the current call. Epistemic license: no increment over the generated candidate. Model caller can decide how to rely on it, but that decision is not established by this source. This is a counterexample to treating failed saveability as rejection from consequential use.

> } else {
> row = unsavedAggregateResult(answer, key, project);
> }
> --- `platform/daemon/src/aggregate-recall.ts`

> results: row ? [{ ...row, content: redactCredentials(row.content) }] : [],
> --- `platform/daemon/src/aggregate-recall.ts`

> sourceMemoryIds: evidenceSources
> .filter((source) => source.sourceKind === "memory")
> .map((source) => source.sourceId),
> --- `platform/daemon/src/aggregate-recall.ts`

#### EPI-RTE-memory-supersession
Label: Memory supersession

Explicit supersede request → permission/scope/freeze checks → transaction records replacement/version/history and invalidates derived memories → head current-source check can exclude old evidence. Caller proposes and fixed code decides structural admissibility; supplied [RT-RTE-direct-remember](runtime.md#rt-rte-direct-remember) names mutation alternatives but does not declare this endpoint/consumer chain. Distinct identity, no supersession of that valid container. SRC-1 `platform/daemon/src/routes/memory-routes.ts`, `platform/daemon/src/transactions.ts`, `platform/daemon/src/memory-head-owner.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: superseded/idempotent status and versions or missing/self/scope/frozen error.
- Later read-back: head support lookup requires superseded_by IS NULL; derived-memory invalidation is invoked transactionally.
- Delegated visibility: caller provides old/new IDs, optional reason and actor; daemon reads both scopes, state and versions.
- Selection predicate: authorized mutation, existing different IDs in matching agent/project/scope/visibility and admissible prior supersession state.
- Invalidation or expiry: old memory receives superseded_by/time/reason and version increment; dependents invalidated; head support eligibility changes.
- Activation or effect: enforces replacement lineage and prevents superseded memory from serving as current head support.
- Evidence limits: not proof of old claim falsity or new claim truth; every recall selector, recovery reversal and already delivered context were not traced.

Operating mode: explicit open mutation; human authorship/approval unresolved from API identity. Oracle: none established. Admission/rejection is structural, not epistemic. Recovery: transaction status and history retained; full reversal mechanics uninspected. Epistemic authority: changed eligibility, no factual verdict. Behavioral path: supersession state → currentSource predicate → enforced rejection of old source for future head support; bounded future publication effect, not retroactive removal from external windows. Source content is not rewritten by this transition. Guidance is endpoint fields and supplied reason.

> invalidateDerivedMemoriesForMemoryInTx(db, input.memoryId, existing.agent_id ?? "default", input.changedAt);
> --- `platform/daemon/src/transactions.ts:688-735`

> "SELECT 1 FROM memories WHERE id=? AND agent_id=? AND is_deleted=0 AND superseded_by IS NULL AND stale_at IS NULL AND visibility != 'archived'",
> --- `platform/daemon/src/memory-head-owner.ts`

#### EPI-RTE-benchmark-judgment
Label: Benchmark answer judgment

Completed answer hypothesis → benchmark protocol.evaluateQuestion or judge.evaluate with question/reference/hypothesis → score/pass/explanation. The orchestrator owns scheduling; model/protocol judges candidate answers. Distinct from maintenance checks in [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass); this is the shipped lab evaluation seam. SRC-1 `memorybench/src/orchestrator/phases/evaluate.ts`, `memorybench/src/judges/base.ts`; object [EPI-OBJ-judge-result](#epi-obj-judge-result).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: score/pass/explanation and optional metrics/usage; parsing can reject malformed score/label/inconsistency.
- Later read-back: scores/explanations feed checkpoint retention, not product memory admission in this inspected phase.
- Delegated visibility: standard judge receives question, question type, ground truth, hypothesis and optional provider prompts; preference questions label reference a rubric; protocol branch is opaque here.
- Selection predicate: targeted question with completed answer, available hypothesis and evaluation not completed; separate derived-only scoring unless reusing product answer.
- Invalidation or expiry: failure recorded; phase throws with instruction to fix and resume; completed entries skipped on resume.
- Activation or effect: result labels answer correct/incorrect and supplies lab status; no graph rewrite or knowledge acceptance is implemented by this phase.
- Evidence limits: judge implementation/model selection, protocol internals, reference correctness, calibration and execution uninspected.

Target/domain: answer fit to benchmark question/reference or preference rubric, not extraction truth, mechanism identification or general future reliability. Oracle: benchmark supplies groundTruth; judge uses it in standard branch. Parser checks output structure/consistency only, not factual accuracy of the judgment. Model-judged truth relation is indeterminate absent actual outputs and evaluator validity; fixed mapping of label to pass is symbolic. Human role in reference creation and review is uninspected. Operational mode is bounded benchmark evaluation, not open maintenance. Epistemic license: attributed reference-relative judgment only. Behavioral path: evaluator → checkpoint consumer → lab completion and report data, current run/resume horizon; no inspected product acceptance consumer. No exact judge component identity/fixity is established; the supplied routed-maintenance model record must not be silently reused as this judge.

> const result = await judge.evaluate({
> question: question.question,
> questionType: question.questionType,
> groundTruth: question.groundTruth,
> hypothesis: candidate,
> providerPrompts: provider?.prompts,
> })
> --- `memorybench/src/orchestrator/phases/evaluate.ts`

> const groundTruthLabel = isPreference ? "Rubric" : "Ground Truth Answer"
> --- `memorybench/src/judges/base.ts`

#### EPI-RTE-benchmark-checkpoint
Label: Benchmark evaluation checkpoint

Evaluation result → checkpointManager.updatePhase → completed score/label/explanation, or failed error → resume selector. Fixed orchestrator owns persistence requests and continuation. Distinct from supplied runtime records after comparison with [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass); lab state is not maintenance history. SRC-1 `memorybench/src/orchestrator/phases/evaluate.ts`; object [EPI-OBJ-judge-result](#epi-obj-judge-result).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-question ID/duration/label after checkpoint update, or an exception on evaluation failure.
- Later read-back: next evaluation invocation reads phase status and skips completed evaluations.
- Delegated visibility: checkpoint receives score/pass/label/explanation and optional metrics/details/usage; logger receives result/progress.
- Selection predicate: successful result records completed regardless of correct/incorrect; errors record failed and interrupt.
- Invalidation or expiry: failed phase can be resumed; checkpoint serialization/revision internals uninspected.
- Activation or effect: completed result changes continuation and prevents repeat scoring; incorrect is a completed evaluation, not a product-memory veto.
- Evidence limits: checkpoint storage internals and later release/autoresearch gates uninspected; no claim of verified durable run artifact or product improvement.

Target/criterion/use/scope: lab phase completion after valid evaluator return for a benchmark question. This is result retention and workflow disposition, not truth acceptance of the underlying Signet memory. Consumer/channel/force/horizon: updatePhase and getPhaseStatus, symbolic status, enforcing resume selection within that run. No semantic content update occurs here. Recovery is failed status plus resume instruction. No separate human approval is shown.

> return status !== "completed" && answerStatus === "completed" && hypothesis
> --- `memorybench/src/orchestrator/phases/evaluate.ts`

> const label = product.passed ? "correct" : "incorrect"
> checkpointManager.updatePhase(checkpoint, question.questionId, "evaluate", {
> status: "completed",
> score: product.score,
> passed: product.passed,
> label,
> explanation: product.explanation,
> --- `memorybench/src/orchestrator/phases/evaluate.ts`

### Claims

#### EPI-CLM-source-connections
Label: Source linked connections

Signet claims automatic memory creation and structured maintenance with every connection linking to source. Doctrine/design, SRC-1 `README.md`. Distinct from [RT-CLM-tool-boundary](runtime.md#rt-clm-tool-boundary): this concerns provenance coverage, not tool restriction. The claim does not by itself assert an independently verified truth criterion. Selected implemented support is the Dreaming provenance seam and head support/publication, but structural/hygiene exceptions and uninspected graph paths prevent a universal invariant conclusion.

> Signet creates memories automatically from your transcripts, imported files, and other sources. In the background, a process called "dreaming" builds and maintains a structured map of the people, projects, facts, and relationships in your history. Every connection links back to its source, so you can see where it came from.
> --- `README.md`

#### EPI-CLM-benchmark-accuracy
Label: Reported benchmark accuracy

Public reported operation, not an observed-run source: Signet reports its latest tracked MemoryBench average. SRC-1 `README.md`. No supplied runtime claim has this referent; closest comparator [RT-CLM-tool-boundary](runtime.md#rt-clm-tool-boundary) concerns worker configuration, not answer performance. The inspected evaluator gives a possible measurement route, not verified score, unbiased judgment or causal component effect.

> Signet's latest tracked MemoryBench run averages **97.6% LongMemEval answer accuracy**. Keeping your memory local shouldn't mean you have to settle for weak recall. See [Benchmarks](https://docs.signetai.sh/benchmarking/#current-longmemeval-score) for the methodology, scoring note, and run workflow.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; each new route states its consumer, channel, force and horizon; supplied host/maintenance paths remain [RT-BAP-host-context](runtime.md#rt-bap-host-context) and [RT-BAP-maintenance-tools](runtime.md#rt-bap-maintenance-tools).
