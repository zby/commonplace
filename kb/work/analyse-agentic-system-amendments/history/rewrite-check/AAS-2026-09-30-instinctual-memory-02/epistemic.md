---
type: types/agentic-system-epistemic-report.md
description: "Epistemic routes of Instinctual Memory at the inspected repository commit"
run-id: AAS-2026-09-30-instinctual-memory-02
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual Memory epistemic report

## Source-and-claim boundary

This lens traces truth-apt content entering the journal and fact store, candidate generation and checks, explicit fact changes, retrieval ranking, and writeback. It assesses the full repository boundary described in `boundary.md`, using `SRC-1` and the runtime baseline records `RT-OBJ-1`–`RT-OBJ-3`, `RT-RTE-1`–`RT-RTE-7`, `RT-CLM-1`–`RT-CLM-2`, and `RT-BAP-1`–`RT-BAP-3`; the Source register in `boundary.md` defines the frozen source scope. The assessed route families are ingestion, extraction/consolidation, direct remember/correct/forget/erase, search and reranking, retention/read-back, and writeback. Actual installed-host calls, agent use of returned material, provider-side model behavior, and production outcomes are uninspected; those gaps prevent observed-use and end-to-end behavioral conclusions. No observed run or causal experiment was supplied (`SRC-1`; `RT-RTE-1`–`RT-RTE-7`).

The inspected design and implementation describe durable facts and their operational handling, but no explicit criterion for accepting a fact as true, or broader knowledge-production/warrant claim, was identified in the inspected claims and routes. `RT-CLM-1` and `RT-CLM-2` concern hook failure behavior and publication protocol, respectively; neither claims factual correctness. This is a boundary-limited finding, not a claim that no such statement exists elsewhere or in uninspected operation.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| `RT-OBJ-1` | Imported session, user, and file content that can express propositions | Journal input for later consolidation and journal search | `SRC-1` `src/journal.rs`; see `RT-OBJ-1` | Ingestion preserves event content as source material, but the truth of a statement and its source warrant are not independently established. No observed event was supplied. |
| `EPI-OBJ-1` | Fact statements proposed by rule or LLM consolidation, including source-event links | Candidate durable facts derived from journal/file inputs; subset of the facts in `RT-OBJ-2` | `SRC-1` `src/consolidate.rs`; `RT-RTE-4` | Part of `RT-OBJ-2`: this record isolates the extraction-produced subset and its evidence checks. No observed candidate artifact or trace was supplied. |
| `EPI-OBJ-2` | A one-sentence fact supplied by a user or agent for remember/correct | Explicitly requested durable fact; subset of facts in `RT-OBJ-2` | `SRC-1` `src/change.rs`; `RT-RTE-5` | Part of `RT-OBJ-2`: this isolates facts whose proposition is supplied directly by a caller. The caller's assertion/reason is not independent truth evidence; no observed request was supplied. |
| `EPI-OBJ-3` | No truth-apt output; query-relative relevance scores/order over retrieved fact statements | Search ranking result used to select or order items for return | `SRC-1` `src/jev.rs`; `RT-RTE-2`, `RT-RTE-3` | External scoring operation was not observed. A relevance judgment is not an assessment of whether the fact is true. |
| `EPI-OBJ-4` | Fact statements rendered in a host instruction-file managed block | Writeback of eligible stored facts for a host to load | `SRC-1` `src/cli.rs`; `RT-RTE-6` | Part of `RT-OBJ-3`'s writeback content: this isolates the generated instruction-file form. Host loading, precedence, and use were not inspected. |

## Authority-route ledger

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `RT-RTE-4` | content transformation | implemented | `RT-OBJ-1` → `EPI-OBJ-1` | `truth-apt transformation: indeterminate`; candidates may be paraphrase/entailed, reshaping, or ampliative; the inspected checks do not decide which. The evidence link may preserve provenance to an event, but proposition warrant is unknown. | Proposed fact statement against cited event content | Rules or configured LLM proposes; `check_llm_fact` checks lasting flag, length, evidence occurrence, and structure; `DomainValidator` applies domain constraints. These do not test proposition truth or entailment. | Manual consolidation or thresholded session-end consolidation; conditional on events after checkpoint, configured extractor, and (for LLM) provider/key | Code can admit a proposal into a batch or quarantine it; no candidate instance observed | Publication makes the fact available to store consumers; no epistemic acceptance force | No truth warrant granted by source-quote matching or domain validation. Source linkage licenses tracing the cited text only. | Batch publication permits later search/read and possible hook/writeback retrieval; failed validation/generation blocks publication | Future search/read caller or hook host, via operation result or `additionalContext`; actual uptake uninspected | `SRC-1` `src/consolidate.rs`; see `EPI-RTE-1` | none | none | No expected factual answer, independent reviewer, or evidence-consuming truth criterion was found. No observed batch or downstream use. |
| `RT-RTE-4` | check/evidence production | implemented | `EPI-OBJ-1` | `no content change` | Whether the proposed evidence text occurs in the cited event, and whether candidate fields meet local constraints | Program checks text occurrence/order and format/domain constraints over the selected event and fact schema | During LLM proposal validation; only on the configured consolidation path | A proposal can pass or fail local checks; no observed result | Passing allows candidate to proceed operationally; it is not accepted as true | Supports evidence-text traceability to that event plus schema admissibility only | Pass permits batch consideration/publication; failure omits/quarantines candidate | Subsequent store consumers only if batch publishes; no use observed | `SRC-1` `src/consolidate.rs`; quote in `EPI-RTE-1` | none | none | It does not establish that the quoted text supports the proposition, that the source is true, or that the candidate is useful. |
| `RT-RTE-4` | disposition/acceptance | implemented | `EPI-OBJ-1` | `no content change` | Candidate admission to published fact tree | Code applies extraction disposition and domain validation; Git CAS admits the batch against current tree. No truth oracle or human per-fact approval is described. | At batch publication after candidate checks | Accepted/quarantined disposition is possible in code; no persisted observed candidate in this evidence set | Operational admission to durable memory; no epistemic acceptance | No criterion for truth-based acceptance identified; persistence is not acceptance | Permits candidate retention and later retrieval if admitted | Later search/read/hook consumers, conditional on eligibility and selection | `SRC-1` `src/consolidate.rs`, `src/repo.rs`; `RT-RTE-4` | `RT-CLM-2` concerns publication only | none | A disposition or successful publication cannot establish factual warrant; operation was not observed. |
| `RT-RTE-5` | content transformation | implemented | caller assertion → `EPI-OBJ-2` | `truth-apt transformation: acquisition/import` (caller-supplied proposition; warrant unknown) for remember; `truth-apt transformation: indeterminate` for correction because the relationship between old and replacement propositions is not specified by validation | Caller-supplied statement and target fact/entity | Caller proposes; code validates request structure, target and domain constraints; no evaluator of truth | Explicit MCP or CLI change request | A validated fact change can be published; no observed request | Durable admission, not epistemic acceptance | Caller is the source; truth and support remain unknown | Permits a new fact or replacement/supersession to be published; stale base can block publication | Calling MCP/CLI client sees receipt; later consumers must retrieve or receive writeback/hook context | `SRC-1` `src/change.rs`, `src/validate.rs`; `RT-RTE-5` | `RT-CLM-2` covers normal publication protocol | none | Reason text and caller identity do not amount to an independent truth check. No request/result was observed. |
| `RT-RTE-5` | disposition/acceptance | implemented | `EPI-OBJ-2` | `no content change` | Admission of caller's requested remember/correct change | Structural/domain validation and Git CAS, not truth evaluation | During explicit request | Publish or conflict/error possible; no result observed | Operational admission only | No fact-level epistemic authority conferred | Valid request can alter retained fact status/content; conflict blocks stale write | Caller gets operation result; any later behavioral path is conditional and uninspected | `SRC-1` `src/change.rs`, `src/validate.rs`, `src/repo.rs`; `RT-RTE-5` | `RT-CLM-2` | none | Successful validation does not establish truth; no independent approver or answer oracle. |
| `RT-RTE-5` | retention | implemented | `EPI-OBJ-2` / `RT-OBJ-2` | `no content change` for forget; erase removes/redacts stored representations and source history | Retrieval eligibility or requested erasure target | Explicit caller target; code controls retrieval suppression or repository/journal rewriting | Explicit forget/erase request | Suppression or erasure is possible; no operation observed | Changes availability/retention, not truth status | No claim about truth follows from forgetting, retraction, or erasure | Forget blocks ordinary later retrieval; erase removes matched material within its rewrite boundary | Future store readers; no later use observed | `SRC-1` `src/change.rs`, `src/erasure.rs`, `src/fact.rs`; `RT-RTE-5` | none | none | Forget preserves ordinary history while suppressing retrieval; erase is a separate history rewrite. Neither is lifecycle integration. |
| `RT-RTE-2` / `RT-RTE-3` | operational admission/selection/consumption | implemented | `RT-OBJ-2` → `EPI-OBJ-3` | `no content change` | Query-to-fact relevance for returned ordering | Lexical match and optional JEV model score relevance to the query; JEV's stated question is answer relevance, not factual accuracy | On explicit search; automatic prompt hook uses facts-only lexical matching without reranking | Ordered result may be returned; no live response observed | Ranking/selection force over which facts are presented | No truth warrant; at most a query relevance ordering | Affects which facts are returned/prominent; does not publish or correct memory | MCP/CLI caller or Claude hook receives results; agent uptake uninspected | `SRC-1` `src/jev.rs`; `RT-RTE-1`–`RT-RTE-3`; quote in `EPI-RTE-2` | none | none | Provider score correctness and effect on host behavior were not observed. |
| `RT-RTE-1` / `RT-RTE-2` / `RT-RTE-3` | operational admission/selection/consumption | implemented | `RT-OBJ-2` → `RT-OBJ-3` | `no content change` | Fact eligibility and selection by status, expiry, scope, prompt/query | Code filters retracted, superseded, expired and (by default) disputed facts and applies route-specific lexical/project selection | Hook prompt/start or explicit read/search; conditional on host setup and request | Eligible text can be emitted; no host session observed | Supplied context or tool result, with host authority treatment uninspected | Applicability and freshness filters do not endorse propositions | Permits contextual availability; does not force model reliance | Claude `additionalContext` or MCP/CLI result; actual consumption uninspected | `SRC-1` `src/fact.rs`, `src/hook.rs`, `src/ops.rs`; `RT-RTE-1`–`RT-RTE-3`; quote in `EPI-RTE-3` | none | none | No evidence that a host loaded or acted on a returned fact. |
| `RT-RTE-6` | truth-apt transformation | implemented | `RT-OBJ-2` → `EPI-OBJ-4` | `truth-apt transformation: non-ampliative reshaping` insofar as it renders selected stored statements into a managed block; no changed proposition is established | Selected active fact statements for a chosen project/file | Code filters eligibility and writes formatted natural-language content; operator chooses invocation and destination | Explicit operator command | File content can be written; no project-file output or host read observed | Makes selected claims available in a host instruction channel | Preserves the source fact's unverified status; rendering does not add warrant | Enables a later host to load the generated block | Host reading selected instruction file; force/horizon depends on host and is uninspected | `SRC-1` `src/cli.rs`; `RT-RTE-6`; `RT-BAP-3` | none | none | Whether formatting preserves every proposition exactly and whether the host loads/follows it were not observed. |
| `RT-RTE-7` | behavior/policy adaptation | implemented | no candidate truth-apt output | `non-truth-apt policy/content update: host configuration registers hooks, MCP, or skill access` | Selected host integration settings | Setup code edits configuration according to operator-selected target and existing state | Explicit `mem setup` or removal | Capability/configuration change is possible; host invocation not observed | Operationally makes access paths available; no direct host behavior is enforced | None | Changes which memory operations the host can invoke | Selected host runtime; actual hook/tool invocation and effect uninspected | `SRC-1` `src/setup.rs`; `RT-RTE-7` | none | none | Configuration capability does not establish retrieval, use, or behavioral effect. |

## Per-object lifecycle disposition

| candidate object ID | relevant route IDs | transformation | discovery lifecycle / applicable warrant | missing evidence/limit |
|---|---|---|---|---|
| `RT-OBJ-1` | `RT-RTE-4` | `truth-apt transformation: acquisition/import` of source content, with source warrant unknown | Discovery lifecycle not applicable to imported source statements. The event text can be retained and traced to its source; no independent verification of its truth is established. | No event instance or source-side verification was supplied. |
| `EPI-OBJ-1` | `RT-RTE-4` | `transformation: indeterminate`; possible non-ampliative reshaping/entailed derivation or ampliative conjecture. The passage check and source-event association preserve a trace link, not semantic entailment. | Candidate instance state: `no instance observed`. No lifecycle phases are upgraded from code alone; no ampliative lifecycle record is warranted because ampliation itself is not established. | Need an observed candidate and source event plus a semantic comparison establishing preservation/entailment or a non-entailed proposition; then candidate-linked evidence of any later phases. |
| `EPI-OBJ-2` | `RT-RTE-5` | Remember is caller-content acquisition/import with warrant unknown; correction is `indeterminate` as to whether replacement entails, contradicts, or otherwise revises the old proposition | Lifecycle not applicable to caller-supplied content as imported. The change protocol does not accept the proposition epistemically. | No observed request; no independent truth evidence or relation criterion for corrections. |
| `EPI-OBJ-3` | `RT-RTE-2`, `RT-RTE-3` | No content change | No lifecycle record for `EPI-OBJ-3`: no candidate truth-apt output for this object; its relevance score has operational selection effect only. | No live score or observed downstream selection effect. |
| `EPI-OBJ-4` | `RT-RTE-6` | Non-ampliative reshaping/rendering, contingent on proposition-preserving output; no new warranted content established | Lifecycle not applicable absent a new truth-apt proposition. | No generated file was supplied to compare against its selected facts; host consumption not observed. |
| `RT-OBJ-3` | `RT-RTE-1`, `RT-RTE-2`, `RT-RTE-6` | No independent candidate truth-apt output; carries or presents existing fact statements | No lifecycle record for `RT-OBJ-3`: no new candidate truth-apt output for this object; relevant direct-adaptation or update routes: `RT-RTE-6`. | Host interpretation and behavioral effect are outside observed evidence. |

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| `RT-CLM-1` | Hook errors are swallowed and hook returns successfully without context/sync output | `SRC-1` `src/hook.rs`; implementation claim represented by `RT-CLM-1` | Runtime account records the same bounded hook guarantee | `RT-RTE-1` | None; no host operation observed | None; no comparison of host response | Fail-open behavior is a wired hook-level protocol; it says nothing about fact truth, successful context delivery, or model consumption | Actual host handling of exit/output uninspected |
| `RT-CLM-2` | Normal memory writes publish validated compare-and-swap Git revisions | `SRC-1` `src/repo.rs`, `src/change.rs`; implementation claim represented by `RT-CLM-2` | Runtime account records bounded protocol purpose | `RT-RTE-4`, `RT-RTE-5` | None; no concurrent write or publication observed | None; no causal comparison | The protocol can reject malformed/stale writes and atomically publish admitted trees; it does not validate proposition truth | Erase, external edits, and embedding callers are outside the covered normal-write claim; factual warrant remains unestablished |

No separate knowledge-production or truth-warrant claim was found within the inspected runtime/design claims. This does not establish absence outside the recorded inspection boundary.

## Bounded conclusion

Instinctual Memory imports source text, proposes durable fact statements from journal inputs, accepts caller-supplied statements into operational storage, filters and ranks stored facts for retrieval, and can render selected facts into host instruction files. The source-event quote check establishes traceability of an evidence string to an event, while the schema and domain checks establish admissibility constraints. These checks do not establish that the source is true or that it supports the candidate proposition (`EPI-RTE-1`). No inspected route provides an evidence-consuming truth-acceptance criterion, so no produced claim is established as accepted knowledge. Consolidated fact transformation remains indeterminate between paraphrase/entailed content and ampliative conjecture; no candidate-linked execution evidence supports lifecycle phase findings.

Explicit remember/correct routes acquire a caller's proposition or replacement into the store without independent truth review. Search reranking assesses query relevance and affects presentation order, not truth warrant (`EPI-RTE-2`). Status and expiry filters affect retrieval applicability without endorsement (`EPI-RTE-3`). Writeback and hook/tool outputs can make stored claims available to a host; whether a host uses them or changes behavior is uninspected. Setup changes access capability, not truth status or enforced behavior. There is no observed acceptance, post-acceptance integration, or causal evidence that any route improves a consumer's factual performance.

## Shared records

### Operative objects

#### EPI-OBJ-1 — Consolidation-proposed fact statements

Part of: RT-OBJ-2

Identity: propositions proposed by rules or the configured LLM from journal events and eligible file content, with candidate evidence references, then represented as structured facts in entity files. Representational form: natural-language statements plus structured Markdown/YAML fields. Storage substrate: the `memory.git` tree, as a subset of runtime `RT-OBJ-2`. This record owns the scoped part. Evidence: `SRC-1` `src/consolidate.rs`, `src/fact.rs`; see `RT-RTE-4`.

#### EPI-OBJ-2 — Caller-supplied fact statements

Part of: RT-OBJ-2

Identity: fact propositions supplied by a user or agent in explicit remember/correct requests. Representational form: natural-language statement plus structured fact fields. Storage substrate: the `memory.git` tree, as a subset of runtime `RT-OBJ-2`. This record owns the scoped part. Evidence: `SRC-1` `src/change.rs`, `src/fact.rs`; see `RT-RTE-5`.

#### EPI-OBJ-3 — Query relevance scores and ordering

Identity: ephemeral relevance decisions/order over retrieved fact statements for one search query. Representational form: structured score/decision data. Storage substrate: transient operation result; no memory-tree publication. It is not truth-apt content. Evidence: `SRC-1` `src/jev.rs`; see `RT-RTE-2` and `RT-RTE-3`.

#### EPI-OBJ-4 — Writeback fact rendering

Part of: RT-OBJ-3

Identity: selected fact statements rendered in a generated managed block of a host instruction file. Representational form: natural-language text. Storage substrate: operator-selected project/host file, outside the memory revision. This record owns the scoped part. Evidence: `SRC-1` `src/cli.rs`; see `RT-RTE-6` and `RT-BAP-3`.

### Routes

#### EPI-RTE-1 — Consolidation evidence trace check

Part of: RT-RTE-4

Source-native identity: `check_llm_fact` checks proposed fact fields and requires evidence text to occur in the cited journal event; successful proposals flow to consolidation disposition/publication. This is a distinct check function within runtime `RT-RTE-4`, not an independent factuality evaluator. Target: proposed fact statement and its cited event, for source-text traceability and schema/domain admissibility. Evaluator: programmatic string/field checks; no expected factual answer. This record owns the scoped part. Evidence: `SRC-1` `src/consolidate.rs`.

> /// Accept a model-proposed fact only if its evidence is really in the event.
> fn check_llm_fact(
>     fact: &LlmFact,
>     event: &JournalEvent,
>     entities: &BTreeMap<String, EntityFile>,
> ) -> std::result::Result<Proposal, &'static str> {
>     let evidence = fact.evidence.trim();
>     let statement = fact.statement.trim();
>     if !fact.lasting {
>         return Err("not lasting (true for one session only)");
>     }
>     if evidence.chars().count() < 8 {
>         return Err("evidence too short");
>     }
>     if !(8..=600).contains(&statement.chars().count()) {
>         return Err("statement empty or over 600 characters");
>     }
>     if !quote_found(&event.content, evidence) {
>         return Err("evidence not found in the cited event");
>     }
> --- `src/consolidate.rs:908-927` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-RTE-2 — JEV relevance ordering

Source-native identity: JEV sends each candidate statement with the query and requests a relevance score based on whether the text answers that query; its output affects ranking. Target: relevance of a retrieved fact statement to a given search query. Evaluator: configured external JEV model/service; no factuality criterion. Distinct grouping across `RT-RTE-2` and `RT-RTE-3`: the reranking operation is shared, and neither runtime route alone contains this whole grouping. Evidence: `SRC-1` `src/jev.rs`.

> "How well does this text answer the search query? Query: {}",
>                     clip(query, 400)
>                 ),
>                 "criteria": [
>                     "Unrelated to the query",
>                     "Shares a topic but does not answer the query",
>                     "Partly answers the query",
>                     "Directly answers the query"
>                 ]
> --- `src/jev.rs:143-151` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-RTE-3 — Fact retrieval eligibility

Source-native identity: `Fact::is_eligible` filters facts by status and temporal validity for current-context retrieval. Target: current retrieval applicability of a stored fact. Evaluator: deterministic status/time conditions; not a truth assessor. Distinct grouping across `RT-RTE-1`, `RT-RTE-2` and `RT-RTE-3`: eligibility filtering participates in each route, so no single-parent relation is asserted. Evidence: `SRC-1` `src/fact.rs`.

> /// True if the fact is eligible for current-context retrieval at `now`.
>     ///
>     /// Excludes superseded, retracted, expired, and (optionally) disputed facts.
>     pub fn is_eligible(&self, now: DateTime<Utc>, include_disputed: bool) -> bool {
>         match self.status {
>             FactStatus::Active => {}
>             FactStatus::Superseded | FactStatus::Retracted | FactStatus::Expired => return false,
>             FactStatus::Disputed if !include_disputed => return false,
>             FactStatus::Disputed => {}
>         }
> --- `src/fact.rs:63-72` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
