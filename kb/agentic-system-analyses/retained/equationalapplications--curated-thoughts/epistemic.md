---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Curated Thoughts truth-apt content, structural evidence gates, human vouching and consequential recall at the frozen revision."
run-id: AAS-2026-11-08-curated-thoughts-00ab3a770403-01
reviewed-boundary: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
---

# Curated Thoughts epistemic report

## Source-and-claim boundary

The question is how imported files become facts licensed for later reliance, and what the checks actually warrant. Scope and external exclusions: see [boundary](boundary.md#boundary-and-evidence); source identity and layers: see [Source register](boundary.md#source-register). All new source reads below are SRC-1 implementation unless marked doctrine/design. No target execution was performed. Supplied runtime records are provisional source-grounded findings, not observed runs.

The consequential warrant claim is [EPI-CLM-trustworthy-facts](#epi-clm-trustworthy-facts). The external-agent protocol is [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow). Imported text has unknown source warrant. Live evidence anchors preserve traceability, not entailment or truth. Explicit human vouching is a counterexample to treating every admission as mere automatic retention; conversely automatic approval is a counterexample to universal per-fact human acceptance.

| Entry point or operation | Source path (SRC-1) | Coverage and records or prevented conclusion |
| --- | --- | --- |
| Deposit, watcher/desktop ingest, librarian and manual review | `src-tauri/src/pipeline/mod.rs`; `tools/src/bin/ct.rs` | Supplied [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick), [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission); CLI command declarations directly read. |
| JSON/evidence validation and fact commit | `src-tauri/src/librarian/synthesis.rs`; `src-tauri/src/db/commit.rs` | Direct reads: [EPI-RTE-evidence-filter](#epi-rte-evidence-filter), [EPI-RTE-anchor-check](#epi-rte-anchor-check), [EPI-RTE-fact-retention](#epi-rte-fact-retention). |
| Full MCP, legacy wiki and separate tools MCP | `src-tauri/src/tool_dispatch.rs`; `tools/src/bin/curated_thoughts_mcp.rs` | Dispatcher arm search directly checked against supplied [RT-RTE-context-recall](runtime.md#rt-rte-context-recall). Legacy wiki/graph/vault arms remain distinct; their full transformations unassessed here, preventing a system-complete negative about alternate routes. |
| Wisdom match / activity and corrections | `src-tauri/src/wisdom_match.rs` | Direct branch reads and symbol search: [EPI-RTE-match-selection](#epi-rte-match-selection); correction functions found but not traced end to end, so no complete correction-delivery guarantee. |
| Queue confirm, deny, undeny | `src-tauri/src/queue_api.rs`; `src-tauri/src/db/queue.rs` | API symbol search; direct backend reads: [EPI-RTE-fact-confirmation](#epi-rte-fact-confirmation), [EPI-RTE-fact-denial](#epi-rte-fact-denial). |
| Scheduled heal and source grounding | `src-tauri/src/db/heal.rs`; `src-tauri/src/db/commit.rs` | Direct reads: [EPI-RTE-source-healing](#epi-rte-source-healing). GUI button is explicitly a different backend; not assumed equivalent. |
| Forget, prune, evidence repair, ontology sweep/merge and reindex | `tools/src/bin/ct.rs`; `src-tauri/src/db/wiki_forget.rs` | CLI declarations directly read; forget backend read: [EPI-RTE-source-forgetting](#epi-rte-source-forgetting). Prune/repair/merge internals unassessed; prevents universal claims about withdrawal, semantic preservation or organization changes. |
| Supersession | `src-tauri/src/wisdom_deposit.rs` | Direct status branch and symbol search: [EPI-RTE-supersession-pending](#epi-rte-supersession-pending). File creation is not automatic application. |
| Prompt-drop confirmation solicitation | `src-tauri/src/prompt_drop.rs` | Direct emitter read: [EPI-RTE-vouch-solicitation](#epi-rte-vouch-solicitation); actual UI response unobserved. |
| External wiki engine and native timers | `src/lib/wiki.ts` | Supplied [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). External package unavailable; semantic transformation, evaluation and admission inside it not determinable. |
| Retrieval evaluator | `src-tauri/tests/wisdom_gate_bench.rs` | Direct partial reads: [EPI-RTE-gate-regression](#epi-rte-gate-regression); no execution or causal outcome claimed. Calibration artifacts not inspected; no reproduction or population-wide validity conclusion. |

No user vault, human-review trace or external-agent use trace was supplied. That prevents claims of exercised acceptance, reliably true generated propositions, improved future capacity or behavioral benefit. External provider weights and the external wiki engine are uninspected; see [RT-CMP-generation-provider](runtime.md#rt-cmp-generation-provider) and [RT-CMP-embed-profile](runtime.md#rt-cmp-embed-profile). The inspected requests do not update parameters; model-name strings do not pin exact weights. No single parametric-learning conclusion applies to opaque providers.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-source-chunks](#epi-obj-source-chunks) | Imported source assertions over the document's domain | see record | SRC-1 `src-tauri/src/librarian/synthesis.rs` | Attribution does not certify the source. |
| [EPI-OBJ-proposal-items](#epi-obj-proposal-items) | Fact/summary assertions; tasks also include non-truth-apt requests | see record | SRC-1 `src-tauri/src/librarian/synthesis.rs` | Semantic preservation/non-entailment unresolved without instances. |
| [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | Retained title/body assertions | see record | SRC-1 `src-tauri/src/db/commit.rs` | Confidence/provenance are metadata, not truth measurements. |
| [EPI-OBJ-fact-evidence](#epi-obj-fact-evidence) | Source quotations plus symbolic lineage | see record | SRC-1 `src-tauri/src/db/commit.rs` | Surviving anchor does not show quote supports proposition. |
| [RT-OBJ-synthesis-prompt](runtime.md#rt-obj-synthesis-prompt) | Guidance including contradiction handling | see record | SRC-1 `src-tauri/src/librarian/synthesis.rs` | Requested criticism is not demonstrated criticism. |
| [RT-OBJ-folder-rules](runtime.md#rt-obj-folder-rules) | None: symbolic admission policy | see record | SRC-1 `src-tauri/src/librarian/mod.rs` | Can permit automatic admission without human judgment. |
| [RT-CMP-generation-provider](runtime.md#rt-cmp-generation-provider), [RT-CMP-embed-profile](runtime.md#rt-cmp-embed-profile) | Not determinable at weight level | see records | SRC-1 `src-tauri/src/librarian/synthesis.rs`; `src-tauri/src/embedder/mod.rs` | Numerical state/endpoint internals not inspectable as individuated propositions. |

## Authority-route ledger

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick) | content transformation | implemented | [EPI-OBJ-source-chunks](#epi-obj-source-chunks) | truth-apt transformation: acquisition/import | External text enters vault/index | Path/shape checks; no source-truth evaluator | Caller deposit and ingest | File/chunks or refusal | enforcing | Unknown external warrant | New source admitted | Writer → filesystem → later librarian; permissive, across invocations | SRC-1 `src-tauri/src/wisdom_deposit.rs` | none | none | See route; source truth unchecked |
| [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis) | content transformation | implemented | [EPI-OBJ-proposal-items](#epi-obj-proposal-items) | truth-apt transformation: indeterminate | Source plus retained candidates → proposals | Model interprets shipped prompt; document domain is open | Dirty/forced document after extraction gates | Proposals, retry, empty output or logged failure | permissive | Candidate assertions only | Queues possible updates | Model messages → parser → proposal store; permissive, later review | SRC-1 `src-tauri/src/librarian/synthesis.rs` | [EPI-CLM-trustworthy-facts](#epi-clm-trustworthy-facts) | none | Reshaping, derivation and conjecture remain possible; no instance proves entailment or non-entailment |
| [EPI-RTE-evidence-filter](#epi-rte-evidence-filter) | check/evidence production | implemented | [EPI-OBJ-proposal-items](#epi-obj-proposal-items) | no content change | Identifiers and evidence-label membership, not truth | Rust collections; finite identifier domain | After JSON parse | Items kept/dropped; unknown evidence labels omitted | enforcing | Reference membership only | Candidate can reach proposal insertion | Parser → validator → store; enforcing, same invocation | SRC-1 `src-tauri/src/librarian/synthesis.rs` | none | none | Full collections may exceed model-visible truncated context |
| [EPI-RTE-anchor-check](#epi-rte-anchor-check) | check/evidence production | implemented | [EPI-OBJ-fact-evidence](#epi-obj-fact-evidence) | no content change | Does fact_add evidence anchor a surviving chunk? | evidence_has_live_chunk; database lineage domain | Inside commit_fact_add | Anchored boolean or error | enforcing | Existence of a live source anchor, not semantic support | Unanchored fact_add cannot be written | Boolean → skip branch → transaction; enforcing, each add | SRC-1 `src-tauri/src/db/commit.rs` | none | none | Separate from model-output validation and human vouch |
| [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission) | disposition/acceptance | implemented | [EPI-OBJ-proposal-items](#epi-obj-proposal-items) | no content change | Per-item accept/edit/reject or auto accept | GUI operator, CLI caller or folder auto-policy; no answer oracle | Pending proposal resolution | Accepted/rejected/skipped items or refusal | enforcing | Operational admission; no universal evidence-consuming truth criterion | Permits committed changes, subject to structural vetoes | Decisions → shared resolver → transaction; enforcing, retained result | SRC-1 `src-tauri/src/db/commit.rs` | none | none | Manual review may consume evidence; actual criterion and exercise unobserved |
| [EPI-RTE-fact-retention](#epi-rte-fact-retention) | retention | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Admitted fact/evidence persistence | SQLite transaction after anchor/dedupe gates | Successful fact_add | Entry, lineage and outbox insertion | enforcing | Retention preserves candidate plus lineage, not acceptance warrant | Later candidates/recall may select it | Commit → SQLite → future consumers; permissive, across calls | SRC-1 `src-tauri/src/db/commit.rs` | none | none | No evidence-consuming semantic acceptance established by auto commit |
| [EPI-RTE-fact-confirmation](#epi-rte-fact-confirmation) | disposition/acceptance | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Human vouch for exact title/body | Desktop caller requests confirmation; backend stamps metadata, not truth | Queue confirmation of live fact | user_confirmed / confirmed and ledger stamp | enforcing | Declared personal endorsement of that content; correctness unmeasured | Human-tier delivery eligibility changes | Confirmation → metadata/ledger → recall activity provenance filter; permissive, future calls | SRC-1 `src-tauri/src/db/queue.rs` | none | none | Criterion is personal vouch, intended use later recall; evidence consumption by person unobserved |
| [EPI-RTE-fact-denial](#epi-rte-fact-denial) | disposition/acceptance | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Deny keyed document/chunk/fact or undo denial | Desktop caller decides; backend validates key and archives | Queue deny/undeny | Archive plus suppression; undo can restore matching text | enforcing | Changed reliance, not proof of falsity | Remove from live recall; reversible suppression | Deny → archive/queue_denials/ledger → later selectors; enforcing, across calls | SRC-1 `src-tauri/src/db/queue.rs` | none | none | Cannot deny keyless fact; undo searches archived matching fact-text hash broadly |
| [EPI-RTE-source-healing](#epi-rte-source-healing) | disposition/acceptance | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Source reference demonstrably ungrounded | DB grounding predicate plus batch breaker | Scheduled/headless heal; only live librarian_inferred with ref | Soft-delete/edge purge or leave/refuse | enforcing | Withdrawal of lineage-based reliance, not refutation | Selected entries cease live recall eligibility | Grounding predicate → transaction → deleted_at filter; enforcing, future calls | SRC-1 `src-tauri/src/db/heal.rs` | none | none | Missing/invalid/error evidence may conservatively retain; GUI button differs |
| [EPI-RTE-source-forgetting](#epi-rte-source-forgetting) | disposition/acceptance | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Exact source_ref selection | Caller-selected refs; equality, not truth evaluator | Explicit forget invocation | Hard deletion + evidence/edge deletion and outbox | enforcing | Intentional erasure, not epistemic refutation | Local entries removed; replica delete requested | Ref list → shared hard-delete → local selectors/outbox; enforcing locally, durable | SRC-1 `src-tauri/src/db/wiki_forget.rs` | none | none | No guarantee remote consumer processed outbox; no undo established here |
| [EPI-RTE-match-selection](#epi-rte-match-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | truth-apt transformation: non-ampliative reshaping | Select facts relevant to query/activity | Cosine floor, lineage membership, temporal filters and provenance | Match invocation with floor/scheme/coverage | Ranked entries, fallback, corrections or abstention | ranking | Relevance heuristic only; no truth acceptance | Controls delivery, not external compliance | Rust selection → CLI JSON → caller; ranking/permissive, current call | SRC-1 `src-tauri/src/wisdom_match.rs` | none | none | Chunk-hop can admit facts below fact cosine floor; activity limits provenance |
| [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | truth-apt transformation: non-ampliative reshaping | Deliver lexical wiki and semantic code matches | See route; lexical overlap/confidence/time and cosine | Explicit recall | JSON or error | ranking | Retrieved assertions with existing warrant unchanged | Makes selected content available externally | JSON → caller model/human; advisory, current task or opaque host retention | SRC-1 `src-tauri/src/tool_dispatch.rs` | [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow) | none | No supplied consumer-use trace; distinct from wisdom match |
| [EPI-RTE-vouch-solicitation](#epi-rte-vouch-solicitation) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Solicit confirmation of non-human-tier hits | Source-type test; no factual evaluator | Recall/search emitter and later drain | Prompt-drop JSONL or best-effort skip | advisory | Unverified marker, not rejection or confirmation | Can request review without blocking recall | Hits → prompt file → later drain/UI; advisory, until handled | SRC-1 `src-tauri/src/prompt_drop.rs` | none | none | Emission is not actual human review |
| [EPI-RTE-supersession-pending](#epi-rte-supersession-pending) | lineage/freshness/recovery | implemented | [EPI-OBJ-proposal-items](#epi-obj-proposal-items) | no content change | Report supersession application state | Status code overrides completed kick when no live facts | Supersession status lookup | pending despite ingested kick | advisory | No license to treat proposal as applied replacement | Caller sees pending rather than completed revision | Ledger/live evidence → status JSON → caller; advisory, lookup | SRC-1 `src-tauri/src/wisdom_deposit.rs` | none | none | Does not establish automatic old/new adjudication |
| [EPI-RTE-gate-regression](#epi-rte-gate-regression) | check/evidence production | implemented | [EPI-OBJ-wiki-facts](#epi-obj-wiki-facts) | no content change | Recall hit/false-positive behavior on frozen probes | Test harness vs fixture expect lists; finite frozen-vector domain | Explicit test execution, not performed | Assertion pass/fail | enforcing | Code-path regression evidence if run; not truth or model quality | Test failure can block its test process, deployment gate uninspected | Fixture vectors → production matcher → asserts; enforcing, test run only | SRC-1 `src-tauri/tests/wisdom_gate_bench.rs` | none | none | Expected answers fixture-provided; no causal attribution or observed pass here |
| [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | content transformation | implemented | [EPI-OBJ-proposal-items](#epi-obj-proposal-items) | truth-apt transformation: indeterminate | Frontend delegates document synthesis to external engine | Configured model callbacks; internal evaluator uninspected | Frontend ingest and timers | Engine result/error | permissive | Not determinable inside external engine | See route; not necessarily librarian gate | Callback → external engine → retained wiki; force internal uninspected, later use | SRC-1 `src/lib/wiki.ts` | none | none | Implementation supports adapter, not hidden engine semantics |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-trustworthy-facts](#epi-clm-trustworthy-facts) | see record | SRC-1 `INTENT.md`, doctrine/design | Explicit purpose; file lineage and personal vouch described | [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [EPI-RTE-anchor-check](#epi-rte-anchor-check), [EPI-RTE-fact-confirmation](#epi-rte-fact-confirmation), [EPI-RTE-match-selection](#epi-rte-match-selection) | None supplied | No comparative downstream-agent experiment inspected; live anchors do not entail facts | Model-generated candidates can become live, traceable entries, and people can vouch for them | Trustworthy factual content and weak-agent benefit not established by structural gates |
| [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow) | see record | SRC-1 `.skills/curated-thoughts/skill.md`, doctrine/design | Shipped recall/deposit protocol | [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick) | None supplied | Host compliance/CTI excluded | Tools afford the protocol | Availability is not activation or successful use |

## Bounded conclusion

Curated Thoughts acquires assertions from external files with unknown source warrant, uses a model to propose facts and summaries, stores admitted content with lineage, and supplies selected facts to later callers. See [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick), [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [EPI-RTE-fact-retention](#epi-rte-fact-retention). No inspected instance establishes which generated propositions merely reshape source claims, are entailed by warranted premises, or go beyond their inputs. The proper transformation classification is indeterminate, not automatically conjecture or deduction.

The checks have distinct targets. Identifier filtering licenses referential membership; the commit gate licenses live-chunk anchoring; retrieval floors license a bounded relevance heuristic. They do not certify proposition truth. The commit gate is consequential: unlike proposal filtering, it skips an added fact with no live anchor. See [EPI-RTE-evidence-filter](#epi-rte-evidence-filter), [EPI-RTE-anchor-check](#epi-rte-anchor-check), [EPI-RTE-match-selection](#epi-rte-match-selection). This qualifies any reading of the runtime's permissive evidence filtering as permitting unanchored fact_add all the way into live storage; the runtime statement about proposal validation itself needs no supersession.

Operational admission and epistemic acceptance differ. Automatic accept-all follows folder policy. Manual proposal decisions can edit/reject, but their actual evidence-consuming criterion is not supplied. Confirmation explicitly records a personal vouch for exact title/body content, intended for human-tier later recall, and its stamp affects activity delivery. That supports a human-endorsement architecture, not an observed evidence-consuming acceptance event or infallible truth. See [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), [EPI-RTE-fact-confirmation](#epi-rte-fact-confirmation). Entry/evidence/outbox linkage after an operational commit is retention and organization; without established epistemic acceptance it is not established lifecycle integration in this report's technical sense.

Withdrawal is real but heterogeneous. Denial archives and persists a keyed suppression; undo removes suppression and restores matching archived text. Heal withdraws entries on demonstrably broken lineage with conservative fallbacks and a breaker; forget intentionally hard-deletes selected source references. None is itself a truth refutation. Supersession files can remain pending rather than enact a replacement. See [EPI-RTE-fact-denial](#epi-rte-fact-denial), [EPI-RTE-source-healing](#epi-rte-source-healing), [EPI-RTE-source-forgetting](#epi-rte-source-forgetting), [EPI-RTE-supersession-pending](#epi-rte-supersession-pending).

Candidate facts can reenter later synthesis through [RT-BAP-librarian-guidance](runtime.md#rt-bap-librarian-guidance), and external agents receive selected results through [RT-RTE-context-recall](runtime.md#rt-rte-context-recall). These are permissive/advisory behavioral-authority paths across invocations, not evidence that users obeyed them. Symbolic policy and metadata updates alter selection directly without new truth-apt propositions. No improved capacity for future action is established merely by that persistence. The frozen-vector evaluator concerns retrieval regression, not factual warrant or component-level causal benefit: [EPI-RTE-gate-regression](#epi-rte-gate-regression).

Prompt instructions to criticize contradictions afford content-directed revision requests; no observed criticism naming fault and shaping an iterated revision was supplied. Thus localized guidance is inspectable and delivery is wired, while theory-content-dependent decision success, exercised criticism, and criticism-driven iteration remain independently unestablished. There is no basis here for a reflective/autonomous theory-builder or exercised self-improvement verdict. External wiki-engine evaluation, provider internals and listed unassessed native maintenance operations prevent a system-complete negative about all acceptance, derivation or learning routes. No system-wide epistemic score follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-chunks
Label: Numbered source chunks

Natural-language source text plus symbolic labels/IDs, read from indexed chunks and assembled into the current synthesis context. This object is the input material of [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), not a duplicate of its prompt or provider. Its lineage is external document → indexed chunk; source warrant unknown. SRC-1, `src-tauri/src/librarian/synthesis.rs`; passage under [EPI-RTE-evidence-filter](#epi-rte-evidence-filter) shows the carried text/hash/line data.

#### EPI-OBJ-proposal-items
Label: Proposal items

Natural-language bodies, summaries and reasoning plus symbolic operation, target and evidence arrays. Rust constructs proposal items and persists them for later decisions. Distinct from [RT-OBJ-synthesis-prompt](runtime.md#rt-obj-synthesis-prompt), which guides production rather than holding outputs. SRC-1, `src-tauri/src/librarian/synthesis.rs`; passage under [EPI-RTE-evidence-filter](#epi-rte-evidence-filter).

#### EPI-OBJ-wiki-facts
Label: Wiki facts

Natural-language title/body assertions with symbolic provenance, confidence, lifecycle and IDs stored in SQLite `llm_wiki_entries`. Different consumption paths interpret prose and filter metadata separately. These are outputs of [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), not the admission route itself. SRC-1, `src-tauri/src/db/commit.rs`; insertion passage under [EPI-RTE-fact-retention](#epi-rte-fact-retention). Exact source truth and original model training provenance remain unresolved.

#### EPI-OBJ-fact-evidence
Label: Librarian evidence

Symbolic proposal/chunk/hash lineage plus natural-language quotes in SQLite `librarian_evidence`. Distinct from the fact assertion: a source quote can exist while failing to support its associated body. `source_ref` stores a token, not the quote itself. SRC-1, `src-tauri/src/db/commit.rs`; gate and retention passages below. Closest supplied record is [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), a consumer/producer route, not this object.

### Routes

#### EPI-RTE-evidence-filter
Label: Evidence label filtering

Part of: [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis)

Parsed model JSON → validate_llm_output → stored proposal items. Rust owns filtering; model proposes content in open document-processing mode, no answer oracle. Candidate identifiers can veto existing-target operations; nonempty add bodies can survive loss of every unknown evidence label. This is the validation part of the supplied synthesis route, not its model-generation part. SRC-1, `src-tauri/src/librarian/synthesis.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Validated proposal items, not a truth verdict.
- Later read-back: Proposals persist for later resolver decisions.
- Delegated visibility: inapplicable — validator is ordinary Rust, not delegated inference.
- Selection predicate: Known candidate/fact IDs, valid operation and nonempty bodies; only known evidence labels retained.
- Invalidation or expiry: Unknown labels omitted; invalid target operations skipped.
- Activation or effect: Filters the candidate set before insertion; no semantic truth check established.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> let normalized = label.trim().trim_start_matches('[').trim_end_matches(']');
>         if let Some(chunk) = chunk_by_label.get(normalized) {
>             out.push(StoredEvidenceChunk {
>                 chunk_id: Some(chunk.chunk_id),
>                 content_hash: chunk.content_hash.clone(),
>                 quote: chunk.text.clone(),
>                 start_line: Some(chunk.start_line as i32),
>                 end_line: Some(chunk.end_line as i32),
>                 source_kind: None,
>             });
> --- `src-tauri/src/librarian/synthesis.rs`

Concrete code deduction, not execution: with a map containing only C1, refs `["[C1]", "C99"]` normalize to C1 and C99. Only C1 produces stored evidence, carrying that chunk's text/hash/lines. With refs `["C99"]`, the array is empty. The add branch does not test that array before constructing the item:

> let evidence = resolve_evidence(&fact.evidence, &chunk_by_label);
>                 match fact.op.as_str() {
>                     "add" => {
>                         let Some(body) = fact.body.as_ref().filter(|b| !b.trim().is_empty()) else {
>                             continue;
>                         };
> --- `src-tauri/src/librarian/synthesis.rs`

The later commit gate below is a counterexample to extending this permissiveness to live storage.

#### EPI-RTE-anchor-check
Label: Live anchor gate

Part of: [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)

Proposal fact_add evidence → evidence_has_live_chunk → skip/write decision in commit_fact_add. Software owns the evidence-existence check, independently of who approved the proposal. Target/domain: lineage resolving into current chunks, not whether a quote entails the body. SRC-1, `src-tauri/src/db/commit.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean gate or error; skipped_unanchored counter on rejection.
- Later read-back: inapplicable — check itself writes no retained content; its disposition controls the following insertion.
- Delegated visibility: inapplicable — local database check.
- Selection predicate: An add reaching shared commit, after duplicate detection.
- Invalidation or expiry: Recomputed at commit; errors propagate and unanchored adds skip.
- Activation or effect: Blocks fact insertion with no surviving anchor; this is a structural veto, no factual answer oracle.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> let unanchored = !evidence_has_live_chunk(conn, &evidence_json)?;
>     if unanchored {
>         warn_unanchored_fact_skipped(&ctx.proposal_id, &title);
>         ctx.skipped_unanchored += 1;
>         return Ok(FactAddOutcome::SkippedUnanchored);
>     }
> --- `src-tauri/src/db/commit.rs`

#### EPI-RTE-fact-retention
Label: Fact and evidence insertion

Part of: [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)

Approved fact_add → exact normalized-body dedupe/anchor gate → SQLite entry, evidence and outbox in resolver transaction. Software physically writes; approval can originate from GUI, CLI or automatic policy (see parent). Caller/model proposes, resolver can reject/skip and transaction failures roll back. This is persistence, not a second epistemic acceptance decision. SRC-1, `src-tauri/src/db/commit.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Committed entry reference or duplicate/unanchored outcome.
- Later read-back: Live entries can reach later recall and candidate context through the supplied runtime routes.
- Delegated visibility: Embedding precomputation is a separate provider path; insertion itself is local.
- Selection predicate: Nonduplicate normalized body in entity redirect cluster and surviving evidence anchor.
- Invalidation or expiry: Later archive/heal/forget routes can withdraw; transaction failure rolls back.
- Activation or effect: Persists facts plus source evidence and replication request for later consumers.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> "INSERT INTO llm_wiki_entries (
>             id, entity_id, title, body, tags, confidence, source_type,
>             source_hash, source_ref, created_at, updated_at, last_accessed_at,
>             access_count, deleted_at, embedding_blob, embed_scheme, embedding, tier
>          ) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, NULL, ?8, ?9, ?9, NULL, 0, NULL, ?10, ?11, NULL, ?12)",
> --- `src-tauri/src/db/commit.rs`

> insert_librarian_evidence(
>         conn,
>         &fact_id,
>         &ctx.proposal_id,
>         &evidence_json,
>         unanchored,
>         ctx.now_ms,
>     )?;
> --- `src-tauri/src/db/commit.rs`

#### EPI-RTE-fact-confirmation
Label: Fact confirmation

Desktop confirmation request → confirm_fact_at → content-hash ledger → stamp_user_confirmed transaction/outbox/event. No supplied runtime counterpart after comparison with proposal admission: this endorses an already live fact rather than deciding a pending proposal. Human-surface caller chooses vouch; code supplies fixed confirmer metadata. No expected-answer oracle or mandatory external evidence test. Intended use/scope: personal endorsement of exact title/body for future human-tier reliance; actual human judgment and evidence consumption unobserved. Failure can leave ledger before full stamp; retry is idempotent. SRC-1, `src-tauri/src/db/queue.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unit success/error; already fully stamped is a no-op.
- Later read-back: Content-hash ledger supports rebuild; stamped metadata affects later provenance-based selection.
- Delegated visibility: inapplicable — local backend operation.
- Selection predicate: Live fact ID not already fully user_confirmed/confirmed.
- Invalidation or expiry: Content hash keys confirmation; ledger retry avoids duplicate lines; later withdrawal is separate.
- Activation or effect: Promotes provenance/confidence and records verification; activity matching accepts user_confirmed.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> "UPDATE llm_wiki_entries
>             SET source_type = 'user_confirmed',
>                 confidence = 'confirmed',
> --- `src-tauri/src/db/queue.rs`

> stamp_user_confirmed(&tx, fact_id, &entity_id, HUMAN_CONFIRMER, now_ms, &at_iso)?;
> --- `src-tauri/src/db/queue.rs`

#### EPI-RTE-fact-denial
Label: Fact denial and undo

Queue choice → deny_fact_at → durable denial ledger → archive and suppression transaction. Undo removes ledger key and queue row then unarchives text-hash matches. No counterpart in supplied runtime proposal admission: this acts on live/archived facts. User-surface decision proposes and admits withdrawal; software vetoes a missing evidence key. Open human-directed operation, no oracle. The material result is changed reliance, not a newly proven negative proposition. SRC-1, `src-tauri/src/db/queue.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unit success/error.
- Later read-back: Denial ledger/queue key persist across calls/rebuild; archive controls live selection.
- Delegated visibility: inapplicable — no model delegation.
- Selection predicate: Deny requires document path, first evidence chunk hash and fact text hash; undo uses stored denial key.
- Invalidation or expiry: Undo can restore archived text matches; transaction failure rolls back DB but durable ledger precedes it.
- Activation or effect: Archives and suppresses; undo scans all archived facts matching fact_text_hash, not only one document.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> let (Some(document_path), Some(chunk_hash)) = (doc_path, chunk_hash) else {
>         anyhow::bail!(
>             "cannot deny {fact_id}: no evidence source document/chunk to key \
>              the denial (spec §3.3)"
>         );
>     };
> --- `src-tauri/src/db/queue.rs`

> crate::db::wisdom::archive_wisdom_in_tx(&tx, &entity_id, fact_id)?;
>     tx.execute(
>         "INSERT OR REPLACE INTO queue_denials
>             (document_path, chunk_hash, fact_text_hash, denied_by, denied_at)
>          VALUES (?1, ?2, ?3, ?4, ?5)",
> --- `src-tauri/src/db/queue.rs`

> if fact_text_hash(&title, &body) != key.fact_text_hash {
>             continue;
>         }
>         tx.execute(
>             "UPDATE llm_wiki_entries SET deleted_at = NULL WHERE id = ?1",
> --- `src-tauri/src/db/queue.rs`

#### EPI-RTE-source-healing
Label: Source lineage withdrawal

Scheduler/headless caller → selected live inferred rows → grounding predicate/breaker → per-row transaction soft-delete, edge purge and events. Closest supplied route is wiki maintenance: its scheduling is the caller, while this is the native withdrawal backend, not external engine synthesis. No same-referent runtime backend record was supplied. The code decides; bulk-breaker policy can veto a batch, explicit allow_bulk bypasses that veto. No truth oracle; stale lineage is the criterion. SRC-1, `src-tauri/src/db/heal.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Evaluated/deleted/edge counts, including zero deletion on breaker refusal.
- Later read-back: deleted_at changes subsequent live-entry eligibility; events persist.
- Delegated visibility: inapplicable — local Rust/SQLite, not delegated agents.
- Selection predicate: Live librarian_inferred rows with non-null source_ref; only demonstrably ungrounded references deleted.
- Invalidation or expiry: Conservative retain on missing evidence or grounding errors; flagged evidence retained while recovery pending.
- Activation or effect: Withdraws selected rows and touching edges, with breaker budget; does not authenticate source truth.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. The GUI button has a different backend; do not extend this policy to every heal surface.

> if !crate::db::commit::source_ref_is_still_grounded(&tx, &source_ref) {
>             let changed = tx.execute(
>                 "UPDATE llm_wiki_entries
>                  SET deleted_at = ?1
>                  WHERE rowid = ?2
>                    AND deleted_at IS NULL
>                    AND source_ref = ?3",
> --- `src-tauri/src/db/heal.rs`

> None => {
>                 warn_source_ref_missing_evidence(trimmed, "no librarian_evidence row");
>                 true
>             }
> --- `src-tauri/src/db/commit.rs`

#### EPI-RTE-source-forgetting
Label: Source reference erasure

Caller-selected exact source_ref list → SQLite selection → shared hard_delete_entries transaction. This differs from supplied proposal admission and from healing: intentional hard erasure rather than proposal acceptance or source-grounding judgment. CLI declares a write confirmation and dry-run surface. Caller decides; software equality predicate selects. No answer oracle or epistemic truth criterion; rollback is transaction failure, not an undo protocol. SRC-1, `src-tauri/src/db/wiki_forget.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Number of deleted entries or error.
- Later read-back: Erasure removes local entry/evidence and requests outbox deletion for replicas.
- Delegated visibility: inapplicable — database helper is local.
- Selection predicate: Exact source_ref membership; empty list no-op.
- Invalidation or expiry: Hard deletion; no undo established by inspected backend.
- Activation or effect: Erases selected rows/lineage/edges with replication request.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> crate::db::commit::hard_delete_entries(&tx, &doomed, now_ms)?;
> 
>     tx.commit()?;
>     Ok(doomed.len())
> --- `src-tauri/src/db/wiki_forget.rs`

#### EPI-RTE-match-selection
Label: Wisdom gate selection

Query vectors plus retained entries → match floor/scheme/temporal selection → ranked results. Distinct from supplied context-recall route: this uses wisdom gate and two-stage logic, not keyword wiki ranking. Rust owns selection; caller supplies query/exclusions/max. Activity mode restricts provenance to user_stated and user_confirmed; message mode need not. No factual answer oracle: cosine evaluates relevance, not truth. Retrieval does not approve or revise fact content. Exact model validity and calibration generalization unestablished. SRC-1, `src-tauri/src/wisdom_match.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked entries/gate outcome; no floor can abstain.
- Later read-back: Reads retained facts; selection itself does not create new truth-apt content.
- Delegated visibility: Embedding provider sees query via callers; final caller receives selected entries, not full store.
- Selection predicate: Temporal/scheme-valid rows; vector dimensions; floor and two-stage coverage/membership; activity provenance.
- Invalidation or expiry: Selection recalculated; deleted rows excluded; supersession corrections have distinct lookup path not fully assessed here.
- Activation or effect: Floor gates delivery; tier-weighted score ranks; chunk-hop admits opened-document facts without their own cosine floor.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> if let Some(floor) = floor {
>             if raw < floor {
>                 continue; // the gate compares RAW cosine — never the weighted score
>             }
>         }
>         let weighted = raw * tier_weight(&entity_id);
> --- `src-tauri/src/wisdom_match.rs`

> QueryKind::Activity => Some(&["user_stated", "user_confirmed"][..]),
> --- `src-tauri/src/wisdom_match.rs`

> None, // r26 m2: NO fact-level floor under rule (ii)
> --- `src-tauri/src/wisdom_match.rs`

The inspected chunk-hop branch joins evidence hashes into chunks of the opened document, so a fact can be delivered even below a fact-level floor. That counters the stronger reading that every delivered fact independently cleared a cosine threshold.

#### EPI-RTE-vouch-solicitation
Label: Unverified match prompt emission

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Recall/search hits → non-human-tier test → best-effort JSONL prompt drop → separate drain/UI channel. This is the solicitation side effect of the supplied recall route, not its returned JSON result. No evaluator of proposition truth occurs; code classifies source-type metadata. A human may later vouch through fact confirmation, but emission does not constitute vouching or block retrieval. SRC-1, `src-tauri/src/prompt_drop.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Emitter returns unit and can skip failed queries/rows.
- Later read-back: Prompt-drop JSONL can be drained later; actual review/compliance unobserved.
- Delegated visibility: inapplicable — local emitter, external UI is a later consumer.
- Selection predicate: Nonempty hits and vault root; selected live payload; non-human source type.
- Invalidation or expiry: Missing/deleted payload skipped; drain/dedup behavior not fully traced here.
- Activation or effect: Records fact/title/body/query/surface for later review solicitation without making recall contingent on approval.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> if is_human_tier(hit.source_type) {
>             continue;
>         }
>         emit_unverified_match(
> --- `src-tauri/src/prompt_drop.rs`

#### EPI-RTE-supersession-pending
Label: Supersession pending status

Supersession file/kick/live evidence → status response. No supplied same-referent record: deposit-kick covers ordinary deposits, while this override concerns the special supersession lane. The inspected override intentionally does not grant completed-application status from a kick alone. Source intent calls for human-vs-agent adjudication, but this branch is not that implementation. SRC-1, `src-tauri/src/wisdom_deposit.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Status pending when a supersession has an ingested kick but no live facts.
- Later read-back: File/kick persist for later processing; automatic replacement not established by this route.
- Delegated visibility: inapplicable — local status computation.
- Selection predicate: Supersession prefix and no live facts; live evidence otherwise outranks ledger.
- Invalidation or expiry: Status recomputed; no expiry or automatic application shown here.
- Activation or effect: Prevents misleading completed status for unapplied supersession; advisory to callers.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> (Some((s, _, _)), _, _) if s == "ingested" && supersession_lane => "pending".to_string(),
> --- `src-tauri/src/wisdom_deposit.rs`

#### EPI-RTE-gate-regression
Label: Frozen-vector gate regression

Frozen vectors and fixture expect lists → real matcher → hit/false-positive assertions. No counterpart in supplied runtime route records; this is a developer evaluator, not live recall. Target: code-path behavior on finite fixture probes, not generated-fact truth or model quality. Fixture labels supply reference outcomes; their independent correctness is uninspected. Explicit test mode, no target test execution here. No production installation/rejection path for test results inspected. SRC-1, `src-tauri/tests/wisdom_gate_bench.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Assertion success or panic if executed; no observed result in this analysis.
- Later read-back: inapplicable — test result does not implement retained runtime knowledge read-back.
- Delegated visibility: inapplicable — frozen-vector replay need not call provider.
- Selection predicate: Feature-gated tests use frozen snapshots and expect lists.
- Invalidation or expiry: Fixture/version changes alter domain; no live evidence refresh demonstrated.
- Activation or effect: Executable regression oracle in test process, not live semantic acceptance or causal benefit evidence.
- Evidence limits: Implementation deductions only; no exercised human judgment, model compliance, external use or causal benefit established. 

> //! Recomputes hit@2 / FP through `wisdom_match_with_floor` from the vectors
> //! the calibration runs froze. Guards the CODE PATH, not the model.
> --- `src-tauri/tests/wisdom_gate_bench.rs`

> let expect: Vec<&str> = p["expect"]
>             .as_array()
>             .unwrap()
>             .iter()
>             .map(|x| x.as_str().unwrap())
>             .collect();
> --- `src-tauri/tests/wisdom_gate_bench.rs:304-309`

### Claims

#### EPI-CLM-trustworthy-facts
Label: Trustworthy facts for weak agents

Consequential doctrine/design claim, not a measured result: librarian converts files into trustworthy short facts so structure reduces demands on the consuming agent. Distinct from [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow), which prescribes recall/deposit ordering rather than warrant or agent capability. SRC-1, `INTENT.md`.

> You put raw material in as ordinary files. A component called the **Active
> Librarian** reads those files and turns them into short, trustworthy facts
> (the "wisdom layer"). Any agent, even a weak one, can then recall those
> facts. The goal is that good structure does the work, so agents don't need
> to be clever.
> --- `INTENT.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
