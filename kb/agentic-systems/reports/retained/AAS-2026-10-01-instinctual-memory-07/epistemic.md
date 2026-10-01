---
type: types/agentic-system-epistemic-report.md
description: "instinctual-memory epistemic routes: source occurrence, durability judgments, operational admission and bounded retrieval evaluation"
run-id: AAS-2026-10-01-instinctual-memory-07
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# instinctual-memory epistemic report

## Source-and-claim boundary

The question is how `mem` acquires assertions and standing instructions, transforms them into durable facts, checks them, grants reliance and changes later availability. The whole repository product at the reviewed commit is included; enclosing agent hosts, live providers and model internals are excluded. The Source register in the supplied boundary governs SRC-1, SRC-2 and SRC-3. No target code or tests were executed. Supplied runtime findings cover dispatch, host delivery, model configuration and publication; direct source reads below assess semantic checks and additional public library operations.

CLM-1 covers sourced durable memory and delivery. EPI-CLM-1 isolates the stronger durability-selection claim; EPI-CLM-2 covers the evaluation/trust claim. Neither an observed end-to-end trace nor a causal comparison is supplied. This prevents conclusions about truthful extraction, effective cleanup, host activation, improved future capacity or comparative ranking benefit. Source-native `accepted` event numbers record processing outcomes, not necessarily epistemic acceptance of every proposed proposition.

| entry point or operation | source path | covering IDs or scope limit |
|---|---|---|
| CLI dispatch and library exports | `src/cli.rs`, `src/lib.rs` | Directly read dispatch/exports; RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10; EPI-RTE-1, EPI-RTE-2, EPI-RTE-3 |
| MCP, HTTP and shell operations | `src/ops.rs` | Directly read shared dispatch; supplied runtime covers registered interfaces; RTE-1, RTE-2, RTE-3, RTE-8 |
| Ingest and backfill adapters | `src/ingest.rs`, `src/cli.rs` | Directly inspected adapter inventory and Markdown import; EPI-RTE-1. Other parser fidelity is unassessed: no system-complete guarantee of faithful import |
| Rules and LLM extraction, checking, deduplication, publication and old-file retirement | `src/consolidate.rs` | Directly read; RTE-4, EPI-OBJ-1 |
| Explicit remember/correct/forget and domain validation | `src/change.rs`, `src/fact.rs`, `src/validate.rs` | Directly read; RTE-3; runtime supplies publisher/recovery and replay limitation |
| Search, eligibility and reranking | `src/search/mod.rs`, `src/search/rerank.rs` | Direct eligibility/abstraction reads; supplied runtime supplies ranker wiring and fallback; RTE-1, RTE-2 |
| Hook delivery and writeback | `src/hook.rs`, `src/cli.rs` | Direct hook and output reads; supplied runtime supplies writeback selection; RTE-5, RTE-6, BAP-1, BAP-2 |
| Tidy findings and suppression | `src/tidy.rs` | Direct complete read; RTE-9, EPI-OBJ-2 |
| Erase and recovery | `src/erasure.rs`, `src/repo.rs` | Supplied runtime RTE-9 and RTE-3; no independently observed completion, external copies excluded |
| Index regeneration | `src/index.rs` | Direct complete read; EPI-RTE-2 |
| Rubric evaluation and benchmark | `src/evaluation.rs`, `src/cli.rs` | Direct implementation reads; RTE-10, EPI-RTE-3, EPI-OBJ-3 |
| Setup/models/task operations | `src/setup.rs`, `src/search/laya.rs`, `src/ops.rs` | Supplied RTE-7, RTE-8; configuration and task-state admission, no claimed fact-production check |
| Checked-in tests and recorded session attribution | `tests/recorded_search.rs` | Supplied boundary SRC-3; no pass output or intervention trace, therefore no observed or causal conclusion |

## Epistemic-object inventory

OBJ-1 is a heterogeneous store rather than a single evaluated candidate. The rows below assess its material parts separately; reconciliation needs a canonical split for journal assertions, curated assertions/instructions, source references, processing dispositions/checkpoint, and suppression controls. No new declaration here duplicates those retained parts. The gap affects whether a single status or evaluator could be assigned to OBJ-1.

| object ID and operative part | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| OBJ-1: journal events | User/file assertions over personal or project scope; may also contain tasks and non-truth-apt instructions | Source material and raw retrieval | SRC-1 `src/ingest.rs` | Imported assertion truth unknown; role metadata is not authentication |
| EPI-OBJ-1 | Proposed standing assertions, evidence strings and model lasting judgment; imperative rules are non-truth-apt policies | Candidate extraction output | SRC-1 `src/consolidate.rs` | No particular model-produced instance or semantic fidelity trace supplied |
| OBJ-1: curated facts | Assertions about users/projects; separate standing policy instructions under same schema | Later memory reliance | SRC-1 `src/fact.rs` | Active and explicit_assertion labels do not certify truth; parts need canonical split |
| OBJ-1: source references | Proposition that an evidence excerpt occurs in a named event | Provenance support | SRC-1 `src/consolidate.rs` | Occurrence does not establish support for the separate statement |
| OBJ-1: disposition/checkpoint | Processing window, accepted/quarantined event numbers | Batch accounting and future progression | SRC-1 `src/consolidate.rs` | Event acceptance can be recorded after placement drops its proposal |
| OBJ-1: suppression controls | Mostly non-truth-apt read/re-extraction policy; reason may assert duplicate/session-only classification | Withdrawal and deletion control | SRC-1 `src/tidy.rs` | Withdrawal reason is not independent correctness evidence |
| EPI-OBJ-2 | Duplicate and session-only judgments about existing facts | Cleanup candidates | SRC-1 `src/tidy.rs` | Overlap/model judgments lack independent semantic oracle |
| EPI-OBJ-3 | Operator expected IDs and include/exclude predicates | Reference outcome for retrieval checks | SRC-1 `src/evaluation.rs` | Expectation truth and genuine held-outness not established |
| EPI-OBJ-5 | Derived pass/recall comparisons | Computed retrieval evaluation result | SRC-1 `src/evaluation.rs` | No observed score instance or production admission consumer |
| OBJ-1: generated index part | Entity names/types and active-fact counts | Navigation summary | SRC-1 `src/index.rs` | Active count is not currently eligible count or truth count |
| OBJ-2 | None required: task title plus version | Coordination state | SRC-1 `src/ops.rs` | Task text can incidentally assert things; no fact-warrant claim |

## Authority-route ledger

Every implemented row is source-grounded, with operation and downstream activation uninspected. Object identity, endpoint ownership and common route fields refer to the supplied declaration unless a new declaration below is named. Linked rows deliberately separate checking, disposition, retention and consumption. No lifecycle-integration row is credited merely from indexing or operational publication.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPI-RTE-1 | content transformation | implemented | OBJ-1 | truth-apt transformation: acquisition/import | External text into journal | Markdown parser/import; source text | Explicit ingest/backfill | Source-linked event | permissive | Source text retained; source truth/warrant unknown | Eligible source for extraction/raw search | Consolidator and search; journal; permissive; later sessions | SRC-1 `src/ingest.rs` | CLM-1 | none | Other adapter fidelity unassessed |
| RTE-4 | content transformation | implemented | EPI-OBJ-1 | truth-apt transformation: non-ampliative reshaping | Matched first-person name/location and preference into attributed standing statement | Fixed regex/template, user-role events | Rules batch | Deterministic paraphrase | permissive | Preserves attributed assertion under intended literal reading; no truth verification | Proposes fact | Extraction.place; Proposal; permissive; batch | SRC-1 `src/consolidate.rs` | CLM-1 | none | Quoted/fictional matches can defeat literal attribution; no parser of intent |
| RTE-4 | content transformation | implemented | EPI-OBJ-1 | truth-apt transformation: indeterminate | Event/chunk to standing proposition | CMP-1 guided by durable-fact prompt | LLM batch | Candidate assertion/policy | advisory | No semantic warrant from fluency or occurrence | Proposes statement and lasting flag | check_llm_fact; JSON; permissive; batch | SRC-1 `src/consolidate.rs` | EPI-CLM-1 | none | Reshaping, derivation or ampliation remain possible; paired inputs/outputs needed; imperatives are policy proposals |
| RTE-4 | check/evidence production | implemented | EPI-OBJ-1 | no content change | Evidence occurrence, lasting flag, statement length, predicate and placement | Program checks normalized ordered fragments; model supplies lasting judgment | Before place | Error or Proposal | enforcing | Bounded source occurrence and usable shape; no entailment/source truth check | Rejects malformed/unsupported-excerpt candidate | llm_extract; Result; enforcing; batch | SRC-1 `src/consolidate.rs` | EPI-CLM-1 | occurrence versus support | Tiny ellipsis fragments are ignored; original full event is checked |
| RTE-4 | disposition/acceptance | implemented | EPI-OBJ-1 | no content change | Fact placement and event accepted/quarantined classification | Blocked-ID and lexical-restatement checks; model/check outcome | After check | Active fact or dropped proposal; accepted event number | enforcing | Operational durability selection; truth acceptance not established | Admits/drop candidate and advances event accounting | Batch publisher; entity/disposition; enforcing; subsequent batches | SRC-1 `src/consolidate.rs` | EPI-CLM-1 | accepted event is not accepted truth | Negation words removed by duplicate tokenizer; overlap cannot certify equivalence |
| RTE-4 | retention | implemented | OBJ-1 | no content change | Placed facts, source refs, disposition and checkpoint | DomainValidator and CAS; see RTE-4 | Successful batch publication | Versioned sourced facts and accounting | enforcing | Provenance/storage integrity within inspected checks; semantic warrant unchanged | Makes active records available for retrieval | Later search/consolidation; Git; permissive; sessions | SRC-1 `src/consolidate.rs` | CLM-1 | none | Dedup drops can lose additional source support; no learning outcome |
| RTE-3 | content transformation | implemented | OBJ-1 | truth-apt transformation: acquisition/import | Caller-supplied fact/ correction | Human or excluded host proposes; schema checks | Explicit request | Fact payload | permissive | Imported warrant unknown; no truth oracle | Submits new/replacement assertion or policy | change::apply; request; permissive; invocation | SRC-1 `src/change.rs` | CLM-1 | none | Correct is an operation label, not independently verified correction |
| RTE-3 | check/evidence production | implemented | OBJ-1 | no content change | Fact/candidate domain shape and reference existence | Fact.validate and DomainValidator | Before publication | Validation failure or success | enforcing | Structural validity/reference checks only | Blocks invalid shape | GitRepo.publish; validator; enforcing; candidate | SRC-1 `src/validate.rs` | CLM-1 | none | Checkpoint non-regression is documented but not compared; no semantic/evidence occurrence check here |
| RTE-3 | disposition/acceptance | implemented | OBJ-1 | non-truth-apt policy/content update: active, superseded or retracted eligibility | Caller remember/correct/forget | Caller proposes; program applies target/status/controls | Explicit command | Published successor or rejection | enforcing | No epistemic endorsement from user request or publication | Adds new memory, replaces or withholds old memory | Search/read/consolidation; facts/controls; enforcing; later sessions | SRC-1 `src/change.rs` | CLM-1 | none | No independent verification of contradiction; shared replay limitation see RTE-3 |
| RTE-3 | retention | implemented | OBJ-1 | no content change | Fact, controls, index, intent and receipt | Validated publisher; see RTE-3 | Successful request | Versioned change | enforcing | No new truth license | Retains operationally admitted candidate | Later readers; store; permissive; sessions | SRC-1 `src/change.rs` | CLM-1 | none | Soft forget retains Git history; recovery and shared replay bounded by RTE-3 |
| RTE-1 | operational admission/selection/consumption | implemented | OBJ-1 | no content change | Eligible curated statements versus raw journal | Temporal/status/visibility/controls plus lexical/model relevance; see RTE-1 | Open retrieval request | Selected rows or missing | ranking | Relevance/availability only; raw events receive no extraction warrant | Orders/delivers facts and events | Caller; tool result; advisory; current invocation | SRC-1 `src/search/mod.rs` | CLM-1 | none | Ranker judgment is not fact checking; direct history has distinct status labeling |
| RTE-2 | operational admission/selection/consumption | implemented | OBJ-1 | no content change | Selected ID to current/history payload | ID lookup and controls/status; see RTE-2 | Open retrieval request | Current or status-labeled history payload | advisory | Relevance/availability only; raw events receive no extraction warrant | Delivers named record or history | Caller; tool result; advisory; current invocation | SRC-1 `src/search/mod.rs` | CLM-1 | none | No relevance scoring or truth check; host use unobserved |
| RTE-5 | operational admission/selection/consumption | implemented | OBJ-1 | no content change | Selected preferences/facts in hook context | Hook selection; see RTE-5 | Host callback | Context/file statements | advisory | Inherited warrant unchanged; emitted statements need not carry full source evidence | Makes statements usable as instructions/context | See BAP-1 | SRC-1 `src/hook.rs` | CLM-1 | none | Host activation unobserved |
| RTE-6 | operational admission/selection/consumption | implemented | OBJ-1 | no content change | Selected statements in persistent project file | Renderer selection; see RTE-6 | Explicit writeback | Persistent Markdown block | advisory | Inherited warrant unchanged; emitted statements need not carry full source evidence | Makes statements usable as instructions/context | See BAP-2 | SRC-1 `src/cli.rs` | CLM-1 | none | Host activation unobserved; file can outlive corrected store facts |
| RTE-9 | check/evidence production | implemented | EPI-OBJ-2 | truth-apt transformation: indeterminate | Duplicate equivalence and future-lastingness | Word overlap/length or CMP-1; excludes already-flagged rows | Manual tidy | duplicate/session_only IDs | advisory | Heuristic/model candidate judgment, no independent truth/durability oracle | Proposes withdrawal | Tidy apply gate; findings; advisory; maintenance invocation | SRC-1 `src/tidy.rs` | EPI-CLM-1 | none | A longer statement is not necessarily more accurate; lasting classification entailment indeterminate |
| RTE-9 | disposition/acceptance | implemented | OBJ-1 | non-truth-apt policy/content update: suppression/retraction | Tidy withdrawal findings | Operator apply/keep gate, validator | Manual apply | Persistent withholding | enforcing | Withholding of reliance for stated maintenance reason; no proof remaining facts true | Suppresses retrieval/re-extraction | Readers/extractor; controls/status; enforcing; later sessions | SRC-1 `src/tidy.rs` | CLM-1 | none | Keep veto and history limits see RTE-9; no measured capacity trigger |
| RTE-9 | disposition/acceptance | implemented | OBJ-1 | non-truth-apt policy/content update: erasure | Explicit fact/entity erase target | Operator target/request, validator then I/O | Manual erase | Removal/redaction/history rewrite or partial failure | enforcing | Withdrawal of availability; no adjudication of truth | Removes selected store material and lineage | Store readers; tree/journal/history/intents; enforcing; later sessions | SRC-1 `src/erasure.rs` | CLM-1 | none | Supplied RTE-9 bounds partial failure and external copies |
| RTE-4 | lineage/freshness/recovery | implemented | OBJ-1 | non-truth-apt policy/content update: old-file facts superseded | Facts solely supported by older version of reingested memory file | Source-ID prefix/version comparison | Consolidation after file edit | Superseded status | enforcing | Freshness of support lineage only | Withdraws stale-file facts from normal reads | Search/read; status; enforcing; later sessions | SRC-1 `src/consolidate.rs` | CLM-1 | none | No semantic contradiction comparison; other supporting sources can preserve fact |
| EPI-RTE-2 | content transformation | implemented | OBJ-1 | truth-apt transformation: entailed derivation | Entity active-status counts | Program count/sort/render in formal record domain | Writer/index rebuild | Index rows/counts | permissive | Counts follow parsed statuses, not truth/temporal eligibility | Publishes navigation data | File readers; INDEX.md; advisory; stored revision | SRC-1 `src/index.rs` | CLM-1 | none | Budget summarizes unlisted remainder; schema correctness premises required |
| RTE-10 | check/evidence production | implemented | EPI-OBJ-3 | truth-apt transformation: entailed derivation | Retrieved top-k IDs/text against expected sets | Program exact ID and case-insensitive substring predicates; human rubric oracle | Explicit evaluate | Pass/recall report EPI-OBJ-5 | advisory | Retrieval fit to supplied criteria only | Reports scores; no production admission | Operator; report; advisory; evaluation invocation | SRC-1 `src/evaluation.rs` | EPI-CLM-2 | none | Expectations may be wrong; no observed report, causal isolation or automatic ranker choice |
| EPI-RTE-3 | check/evidence production | implemented | EPI-OBJ-4 | truth-apt transformation: entailed derivation | Elapsed search timings and empirical quantiles | Monotonic clock then sort/index arithmetic | Explicit bench | min/median/p95 report | advisory | Timing observations of invoked workload only | Reports latency; no successor selection | Operator; stdout; advisory; benchmark invocation | SRC-1 `src/cli.rs` | none | none | No timing runs supplied; search/content correctness and causal components not established |
| RTE-8 | operational admission/selection/consumption | implemented | OBJ-2 | non-truth-apt policy/content update: versioned task append | Expected task version | Caller proposes; program lock/version comparison | Explicit requests | Task append or conflict | enforcing | Compatibility/concurrency only; no epistemic fact license | Changes task state | Task callers; task JSON; permissive; later invocations | SRC-1 `src/ops.rs` | none | none | No autonomous task action; incidental title assertions unchecked |
| RTE-7 | operational admission/selection/consumption | implemented | CMP-3 | non-truth-apt policy/content update: host/model selection | Configuration/load compatibility | Caller command; configuration write/model load | Explicit requests | Configuration/model selection or failure | enforcing | Compatibility/concurrency only; no epistemic fact license | Changes accessible capability or selected model | Host/ranker; config/cache; permissive; later invocations | SRC-1 `src/search/laya.rs` | none | none | Setup part see RTE-7; model loading licenses compatibility only |

> entity_type: "person".into(),
>                 title: name.clone(),
>                 predicate: "name".into(),
>                 statement: format!("User's name is {name}."),
>                 evidence: cap[0].to_string(),
>             });
> --- `src/consolidate.rs:300-305` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The extraction prompt requests character-for-character evidence, while the implementation accepts normalized, ordered ellipsis fragments. README documentation already explains that relaxation. The important remaining boundary is semantic: `check_llm_fact` checks the evidence string and the statement separately, without checking their entailment. Its source-occurrence result can license attribution of an excerpt, not the separate standing assertion. Compare RTE-4 below.

> if !fact.lasting {
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
> --- `src/consolidate.rs:916-927` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> fn quote_found(source: &str, evidence: &str) -> bool {
>     let haystack = normalise(source);
>     let fragments: Vec<String> = evidence
>         .replace('…', "...")
>         .split("...")
>         .map(normalise)
>         .filter(|f| f.chars().count() >= 8)
>         .collect();
>     if fragments.is_empty() {
>         return false;
>     }
>     let mut from = 0usize;
> --- `src/consolidate.rs:981-992` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> jaccard(&words, &other) >= NEAR_DUPLICATE || contained(&words, &other)
>             })
>     }
> }
>
> /// Word-overlap ratio at which two statements count as the same fact.
> pub(crate) const NEAR_DUPLICATE: f64 = 0.6;
>
> const STOPWORDS: &[&str] = &[
>     "a", "an", "the", "is", "are", "be", "to", "of", "in", "on", "for", "and", "or", "with",
>     "that", "this", "it", "its", "as", "by", "at", "from", "has", "have", "uses", "use",
>     "project", "user", "includes", "include", "consists", "assistant", "agent", "must", "always",
>     "should", "only", "when", "not", "no", "never", "do", "does", "wants", "want", "prefers",
> --- `src/consolidate.rs:443-455` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`


The overlap classifier removes `not`, `no` and `never`. Thus opposed assertions can share its content-word set. This is an inspected possibility of semantic loss in proposal dropping and tidy withdrawal, not a recorded failure case. A normalized match and an active status must not be interpreted as proof of equivalent meaning.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| CLM-1 | See CLM-1 | SRC-2 `README.md`, doctrine/design | Source-linked curated facts, delivery and validated change | EPI-RTE-1, RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6 | None supplied | None; host/provider behavior excluded | Storage, grounding checks and later delivery are wired | Curated/validated does not confer factual warrant or benefit |
| EPI-CLM-1 | Lasting facts pass new-teammate-next-month test | SRC-2 `README.md`, doctrine/design | Fixed prompt, model lasting flag and tidy judge | RTE-4, RTE-9 | None supplied | None; no future-session outcome comparison | Model-assisted selection of prospective durability is implemented | Durability/usefulness not independently established; rules extractor uses patterns without lasting judgment |
| EPI-CLM-2 | Rubric comparison lets reranker be trusted where it helps | SRC-2 `src/evaluation.rs`, doctrine/design | Compare lexical/reranked reports against operator expectations | RTE-10 | None supplied | None; no run contrast, immutable model or snapshot control across both searches established | Fit to explicit retrieval predicates can be measured and reported | Human trust decision outside implementation; held-out rubric quality not established |

## Bounded conclusion

`mem` acquires source assertions and policies, then stores candidate standing statements with source references. The imported source truth is unknown. Rules extraction reshapes narrow literal assertions; model extraction has an indeterminate content relation without paired output evidence. The decisive gate checks source-text occurrence, structure and a model-supplied durability flag. It does not check that the source warrants the statement, so publication and the native `accepted` label do not establish accepted ampliative knowledge (EPI-RTE-1, RTE-4; SRC-1 `src/consolidate.rs`).

Explicit changes grant operational reliance on caller-proposed content after structural checks. Corrections, forgetting, old-file retirement and tidy withdraw availability through statuses and controls. Tidy can criticize the lastingness of a particular stored claim and retain a withdrawal reason, but its model returns IDs rather than a formulated account locating blame in a theory, test or auxiliary assumption. Lexical duplication is an especially weak semantic criterion because its vocabulary discards negation. None of these routes establishes that surviving statements are true (RTE-3, RTE-4, RTE-9; SRC-1 `src/change.rs`, `src/tidy.rs`).

Retrieval, hooks and writeback turn availability into advisory use through tool results, additional context and persistent instructions. BAP-1 and BAP-2 bound consumer, channel, force and horizon; actual activation remains uninspected. These are operational use before evidenced epistemic acceptance, rather than demonstrated lifecycle integration of accepted claims (RTE-1, RTE-2, RTE-5, RTE-6; SRC-1 `src/hook.rs`).

The defensible derived propositions are narrower: active-status counts and evaluation pass/recall formulas within their parsed-record domains. Rubric criteria name a scope and use for retrieval evaluation, but the result is a report with no implemented admission consumer. Benchmark timings similarly report a workload, without adapting production policy. No supplied run supports successful transfer, improved future capacity or a causal ranker effect (EPI-RTE-2, RTE-10, EPI-RTE-3; SRC-1 `src/index.rs`, `src/evaluation.rs`, `src/cli.rs`).

For the shipped extraction and tidy guidance, the supplied RTE-4 and RTE-9 theory-builder conditions 1–4 and separate learning, reflection and autonomy findings apply. Source-localized rules are consumed but method criticism/iteration is absent in those inspected routes. Particular retained statements may contain design rationale or theory; no actual retained store is supplied to classify those instances. Opaque model processing and distributed parameters cannot be individuated as truth-apt content from this boundary. This prevents a broader theory-builder or self-improvement conclusion, without treating opacity as absence.

## Shared records

### Operative objects

#### EPI-OBJ-1 — Extraction proposals

Source-native identity: `Proposal` and `LlmFact`, ephemeral candidate before `Extraction.place`. Representational form: natural-language statement/evidence and structured fields, including lasting judgment; substrate: process memory/model JSON, not yet durable memory. Closest supplied OBJ-1 is the enclosing retained store; distinct identity: this object is a pre-admission candidate, not a retained store part. Evidence: SRC-1 `src/consolidate.rs`. Producer is rules or CMP-1; consumers are check/place. No supplied candidate instance establishes which semantic transformation actually occurred.

> A fact is worth keeping only if it will still be true and useful in a session weeks from now, in a different task: the user's identity and role, standing preferences and working rules, project facts (what it is, stack, architecture, conventions, commands, decisions and why), and named people or organisations with a stated relationship.
>
> The test for every candidate: would a new teammate, starting fresh next month, need to know this? If it only describes what was happening in that session, it is not a fact.
> --- `src/consolidate.rs:578-580` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> id: fact_id,
>             predicate: p.predicate,
>             statement: p.statement,
>             kind: FactKind::ExplicitAssertion,
>             status: FactStatus::Active,
>             observed_at: event.occurred_at,
>             valid_from: None,
>             valid_from_precision: None,
>             valid_to: None,
>             expires_at: None,
>             review_after: None,
>             supersedes: vec![],
>             sources: vec![SourceRef {
>                 event_id: event.event_id.clone(),
>                 role: fact_role(event.role),
>                 evidence: p.evidence,
>             }],
>             visibility: Visibility::Private,
>         };
> --- `src/consolidate.rs:377-395` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-OBJ-2 — Tidy findings

Source-native identity: `Finding`/`TidyReport.findings`. Representational form: structured fact/entity IDs, statement, duplicate/session_only kind and optional duplicate target; substrate: process-memory result, reasons retained only on apply. Closest OBJ-1 includes affected facts and later controls, but findings are distinct transient judgments. No counterpart object after comparing OBJ-1 and OBJ-2. Evidence: SRC-1 `src/tidy.rs`; RTE-9 owns method and decisions.

> let mut report = TidyReport {
>         facts_checked: live.len(),
>         findings,
>         checked_session_only: cfg.is_some(),
>         applied_at: None,
>     };
>     if apply && !report.findings.is_empty() {
>         report.applied_at = Some(forget_all(repo, &head, entities, controls, &report.findings)?);
>     }
>     Ok(report)
> }
> --- `src/tidy.rs:152-162` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-OBJ-3 — Retrieval rubric

Source-native identity: `Rubric`. Representational form: JSON question, expected IDs and required/forbidden text predicates; substrate: operator rubric file and process memory. Producer: caller; consumer: evaluation implementation. Closest supplied OBJ-1 stores evaluated material, not its expectation/result; RTE-10 describes this route without declaring an operative evaluation object. Evidence: SRC-1 `src/evaluation.rs`.

> let recall = case.expected_fact_ids.iter().all(|id| ids.contains(&id.as_str()));
>         let first_expected_rank = ids
>             .iter()
>             .position(|id| case.expected_fact_ids.iter().any(|e| e == id))
>             .map(|i| i + 1);
>         let includes_ok = case.must_include.iter().all(|s| text.contains(&s.to_lowercase()));
>         let excludes_ok = case.must_not_include.iter().all(|s| !text.contains(&s.to_lowercase()));
>         cases.push(CaseScore {
>             id: case.id.clone(),
>             category: case.category.clone(),
> --- `src/evaluation.rs:130-139` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-OBJ-5 — Retrieval score report

Source-native identity: `CaseScore`, `RunReport`, `EvaluationReport`. Representational form: computed boolean, rank and aggregate recall fields; substrate: process memory/stdout or optional CLI serialization. Producer: evaluation implementation; consumer: operator. Closest supplied RTE-10 names this computation but declares no output object; distinct from OBJ-1/OBJ-2 and from the caller-produced rubric EPI-OBJ-3. Evidence: SRC-1 `src/evaluation.rs`; the retained rubric-comparison passage above supports the derived result. No computed result instance supplied.

#### EPI-OBJ-4 — Benchmark timing report

Source-native identity: `cmd_bench` samples and `print_bench_row` aggregates. Representational form: numeric elapsed milliseconds and sorted quantiles; substrate: process memory/stdout. No counterpart after comparing OBJ-1, OBJ-2 and RTE-10: this measures latency rather than rubric fit. Evidence: SRC-1 `src/cli.rs`.

> let start = Instant::now();
>             let found = crate::ops::combined_search(
>                 &cli.root,
>                 &crate::ops::SearchParams { query, limit, rerank, project, ..Default::default() },
>             )?;
>             ms.push(start.elapsed().as_secs_f64() * 1000.0);
>             ranker = found.ranker;
>             hits = found.hits.len();
> --- `src/cli.rs:2513-2520` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Routes

#### EPI-RTE-1 — Source import into journal

Closest supplied RTE-4 consumes already accumulated events and RTE-5 can trigger backfill; distinct identity is the preceding import operation. Endpoints: external file/transcript through adapter into journal event and append; owner: adapters/CLI. Immediate return: event/import counts or parse failure. Later read-back: journal is consumed by RTE-4 and RTE-1/RTE-2 across sessions. Delegated visibility: enclosing caller/store users; host propagation uninspected. Selection predicate: selected file/adapter and parser role/source filters; invalidation/expiry: redaction/erasure, source update becomes a separate event. Effects: import and attribution, without truth check. Implementation conclusion status: wired. Operation conclusion status: uninspected. Activation conclusion status: uninspected. Evidence limits: only Markdown semantic preservation directly assessed; other adapter parsing not exhaustively inspected. Evidence: SRC-1 `src/ingest.rs`, `src/cli.rs`.

> let mut event = JournalEvent::new(
>             scope_id.to_string(),
>             session_id.to_string(),
>             Role::Note,
>             Source::IdeHistory {
>                 source_id,
>                 position: 0,
>                 occurred_at: None,
>             },
>             trimmed,
>             Redaction::None,
> --- `src/ingest.rs:575-585` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-RTE-2 — Index count derivation and regeneration

Closest supplied RTE-3/RTE-4 publish an index alongside writes; distinct identity is exposed `index::rebuild` and its shared count renderer. Endpoints: parsed current entities into sorted bounded rows then validated index commit; owner: index module. Immediate return: new or unchanged revision. Later read-back: stored index consumed by navigation/file readers across sessions; no observed reader supplied. Delegated visibility: store readers. Selection predicate: eligible entity files, active statuses and byte budget; invalidation/expiry: regenerated on subsequent writes or index command, no semantic expiry. Effect: canonical navigation/count data, not fact endorsement. Implementation conclusion status: wired. Operation conclusion status: uninspected. Activation conclusion status: uninspected. Trigger/proposed change: explicit index command or caller writer renders current records. Proposer/decider: deterministic renderer/publisher; veto: validation/CAS/errors. Human chooses invocation, no per-count approval. Answer oracle: formal record statuses, not world truth. Operating mode: open requests. Guidance: fixed renderer/count rule. Retained: index text/Git revision. Rollback/recovery: prior Git revision available; no automatic semantic rollback. Evidence: SRC-1 `src/index.rs`.

> for entity in &rows {
>         let active = entity.facts.iter().filter(|f| f.status == FactStatus::Active).count();
>         let row = format!(
>             "- `{}` ({}) {} — {active} active fact{}\n",
>             entity.id,
>             entity.entity_type,
>             entity.title,
>             if active == 1 { "" } else { "s" }
>         );
>         if body.len() + row.len() > INDEX_MD_BUDGET {
> --- `src/index.rs:30-39` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-RTE-3 — Search latency measurement

Closest supplied RTE-10 computes retrieval correctness criteria; distinct identity is CLI `bench` measuring elapsed wall time. Endpoints: configured queries/iterations through RTE-1, clock samples into aggregate stdout; owner: CLI. Immediate return: timing table or error. Later read-back: inapplicable for result because this route does not retain samples as future controls. Delegated visibility: caller stdout; later sharing uninspected. Selection predicate: supplied queries/project/limit and separate lexical/reranked iteration counts. Invalidation/expiry: inapplicable for transient report. Effect: latency measurement without production policy adaptation. Implementation conclusion status: wired. Operation conclusion status: uninspected. Activation conclusion status: uninspected. Human chooses workload/interprets results; computation measures/aggregates. Answer oracle: none for correctness. Operating mode: bounded operator benchmark; no improvement trigger or successor admission. Evidence: SRC-1 `src/cli.rs`; EPI-OBJ-4.

### Claims

#### EPI-CLM-1 — Future-session durability test

Claimed operation: retain only facts that pass prospective future truth/usefulness selection, with evidence appearing in the cited event. Claim conclusion status: claimed. Closest supplied CLM-1 concerns storage/delivery; this narrower claim concerns the warrant of selection. Evidence: SRC-2 `README.md`, `src/consolidate.rs`. Implemented model lasting flag is an admission condition; its quality is unobserved. Rules mode does not apply that model criterion.

> A fact is worth keeping only if it will still be true and useful in a session weeks from now, in a different task: the user's identity and role, standing preferences and working rules, project facts (what it is, stack, architecture, conventions, commands, decisions and why), and named people or organisations with a stated relationship.
>
> The test for every candidate: would a new teammate, starting fresh next month, need to know this? If it only describes what was happening in that session, it is not a fact.
> --- `src/consolidate.rs:578-580` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-CLM-2 — Evaluation supports bounded reranker trust

Claimed operation: report rubric results side by side so a reranker is trusted where it helps. Claim conclusion status: claimed. No counterpart after comparing CLM-1: this concerns retrieval comparison and operator trust rather than memory persistence. Evidence: SRC-2 `src/evaluation.rs`. The implementation returns reports; admission of a production successor or automatic reliance change is not wired in RTE-10.


> //! Runs every case in a rubric through the real search (curated facts and
> //! the journal, the same code as `mem search` and MCP `memory_search`) twice:
> //! once in lexical order and once reranked. A case passes when every
> //! expected id is in the top `limit` hits, every `must_include` string
> //! appears in them, and no `must_not_include` string does. The two runs are
> //! reported side by side so a reranker is only trusted where it helps.
> --- `src/evaluation.rs:3-8` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`
