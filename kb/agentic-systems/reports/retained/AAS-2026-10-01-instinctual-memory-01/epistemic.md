---
type: agentic-systems/types/agentic-system-epistemic-report.md
description: "Epistemic routes for how instinctual-memory creates, checks, retains, and exposes memory claims"
run-id: AAS-2026-10-01-instinctual-memory-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# instinctual-memory epistemic report

## Source-and-claim boundary

The boundary is the inspected Git implementation and design documentation at `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` (Source register: `boundary.md`). The question is how `mem` produces or acquires truth-apt memory content, checks it, grants reliance, and exposes it to later consumers. Enclosing hosts, providers, and actual deployments are excluded. Runtime records RTE-1 through RTE-3 supply the CLI, MCP, and hook/writeback entry paths; this report directly inspects consolidation, validation, change, search, and source-format behavior. No execution traces are supplied, so operation, caller identity, model behavior, downstream agent uptake, and benefit are unobserved.

| Entry point or operation | Source path | Coverage | Limit |
|---|---|---|---|
| CLI and MCP dispatch | `src/main.rs`, `src/mcp.rs`; runtime RTE-1, RTE-2 | Inherited adapter routes | Their presence does not establish invocation or agent use. |
| Journal ingestion and consolidation | `src/cli.rs`, `src/consolidate.rs` | EPI-OBJ-1, EPI-OBJ-2; EPI-RTE-1, EPI-RTE-2, EPI-RTE-3 | Provider internals and actual extraction outcomes unavailable. |
| Candidate validation and publication | `src/validate.rs`, `src/repo.rs`, `src/change.rs` | EPI-RTE-4, EPI-RTE-5 | Validator scope is structural/domain validity, not independent truth checking. |
| Search and readback | `src/search/`, `src/ops.rs`, `src/cli.rs` | EPI-RTE-6; runtime RTE-1, RTE-2 | Returned content's effect on host behavior is unobserved. |
| Direct remember/correct/forget | `src/change.rs`, `src/ops.rs` | EPI-RTE-7 | No answer oracle or evidence-consuming truth criterion is established. |
| Hooks, HTTP, setup and host configuration | `src/hook.rs`, `src/http_serve.rs`, `src/setup.rs` | Adapter coverage from runtime; no separate epistemic operation established here | Host grants, actual exposure, and deployment configuration are unavailable; system-complete claims about deployed checks or activation are prevented. |

The inspected design claim is that consolidation turns journal events into “curated facts” (EPI-CLM-1). The sources establish implemented candidate-generation and admission mechanisms, but no observed use or causal benefit. The word “curated” does not itself establish warranted acceptance.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| EPI-OBJ-1 | User and note journal event statements, which can assert propositions | Source material for later durable facts | SRC-1 `src/journal.rs`; SRC-1 `src/consolidate.rs` | Imported source warrant is not independently checked. |
| EPI-OBJ-2 | Entity facts: natural-language statements with entity, predicate, status, visibility, and source references | Curated durable memory | SRC-1 `src/fact.rs`, `src/entity.rs`; SRC-1 `src/consolidate.rs` | A fact record and source link do not establish its truth. |
| EPI-OBJ-3 | Consolidation prompt/output and extracted candidate facts, including source quote and lasting flag | Candidate production and operational filtering | SRC-1 `src/consolidate.rs` | LLM internals and model version unavailable; semantic entailment and factual correctness are not established by matching a quote. |
| EPI-OBJ-4 | Controls, retractions, suppressions, and tombstones; primarily disposition metadata, not truth-apt claims | Prevent, withdraw, or suppress facts during later extraction and reads | SRC-1 `src/controls.rs`, `src/change.rs`, `src/consolidate.rs` | Operational exclusion is not a finding that a proposition is false. |

## Authority-route ledger

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EPI-RTE-1 | content transformation | implemented | EPI-OBJ-1 → EPI-OBJ-3 | truth-apt transformation: indeterminate; may preserve or reshape source assertions, while generated statements may add assumptions | Journal event to regex proposal | Fixed patterns for name, residence, and preference in user-role events | When rules extractor is selected and batch is run | Matching proposal is placed as a fact; unmatched/non-user events are quarantined | Admission into fact store | No independent warrant; source assertion is retained in normalized form only if interpretation is accurate | Allows matched candidates into durable facts | Later search/read by caller; available across later invocations, downstream effect unobserved | SRC-1 `src/consolidate.rs` | EPI-CLM-1 | none | No evidence establishes semantic equivalence or truth of input assertions. |
| EPI-RTE-2 | content transformation | implemented | EPI-OBJ-1 → EPI-OBJ-3 | truth-apt transformation: indeterminate; source quote is copied as evidence, but generated proposition may or may not follow | Journal/user or note content to LLM proposed fact | Configured external model, prompted for lasting facts; evidence quote must occur in cited event | Only when LLM extractor is selected/configured and consolidation runs | Fact can be placed; candidate is rejected if lasting flag, lengths, predicate, or quote conditions fail | Candidate filter and placement | Exact quote match licenses only that some cited text occurs; not statement truth, entailment, source reliability, or “lasting” status | Allows a passing proposal into fact store | Search/read can expose it later; host activation unobserved | SRC-1 `src/consolidate.rs` | EPI-CLM-1 | none | No provider trace, answer oracle, semantic judge, or observed acceptance record. |
| EPI-RTE-3 | disposition/acceptance | implemented | EPI-OBJ-3 | no content change | Candidate against lastingness, quote occurrence and schema-like predicates | Rules or code checks; no independent evaluator for truth | During consolidation, before publish | Accepted event IDs and quarantined reasons recorded; candidate facts accompany changed entity files | Operational admission | No epistemic acceptance established; quote validation is provenance screening only | Determines which candidate files and checkpoint/disposition changes can publish | Consolidator and later store readers; durable horizon | SRC-1 `src/consolidate.rs` | EPI-CLM-1 | none | Event-level “accepted” is an implementation label, not an evidenced truth judgment. |
| EPI-RTE-4 | check/evidence production | implemented | EPI-OBJ-2 | no content change | Changed snapshot: parseability, fact validity, references, known suppression targets, checkpoint consistency | `DomainValidator`; structural/domain rules across candidate tree | On publication of a candidate change set | Publish succeeds or rejects | Enforcing publication gate | Licenses repository consistency and declared field constraints only; no truth warrant | Blocks malformed or domain-invalid snapshot publication | Git snapshot consumers, later reads; horizon is persisted revision | SRC-1 `src/validate.rs` | none | none | Validity is not factual verification. |
| EPI-RTE-5 | disposition/acceptance | implemented | EPI-OBJ-2 | no content change | Candidate snapshot vs parent revision and domain rules | `DomainValidator` invoked by publish | On consolidation publication | Atomic revision/receipt or error | Permissive for validated candidate publication; rejects failures | No independent epistemic license | Publishes operationally valid changes | Later repository readers; durable until revised | SRC-1 `src/repo.rs`, `src/consolidate.rs` | EPI-CLM-1 | none | No user approval or evidence-consuming intended-use criterion found in this path. |
| EPI-RTE-6 | operational admission/selection/consumption | implemented | EPI-OBJ-2 | no content change (ranking may reorder results) | Search query against fact and journal stores | Lexical/reranking selection configured by caller; no truth evaluator | At CLI/MCP search/read invocation | Matching fact/event results returned | Ranking/serving | Retrieval grants availability, not endorsement or increased warrant | Makes selected content available to caller | CLI/MCP client; host context and later behavior outside boundary | SRC-1 `src/search/`, `src/ops.rs`; runtime RTE-1, RTE-2 | none | none | No traces establish which results were read or used. |
| EPI-RTE-7 | disposition/acceptance | implemented | EPI-OBJ-2, EPI-OBJ-4 | non-truth-apt policy/content update: explicit remember/correct/forget changes; correction replaces/supersedes, forget retracts and suppresses | Caller request targeting entity/fact | Request validation and `DomainValidator`; requester supplies content and target | At explicit change call | Fact written, superseded, or retracted; forget suppression prevents re-extraction | Enforcing mutation and later suppression | Caller assertion or deletion request is not independently warranted; forget is not falsity judgment | Changes future store state and availability | Later CLI/MCP reads and consolidation; durable revision | SRC-1 `src/change.rs`, `src/controls.rs` | none | none | Caller authority, basis, and approval conditions are not evidenced. |

> Turns journal events into curated facts in the Git store.
> --- `src/consolidate.rs:3-3` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> The test for every candidate: would a new teammate, starting fresh next month, need to know this? If it only describes what was happening in that session, it is not a fact.
> --- `src/consolidate.rs:580-580` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> The evidence must be copied character-for-character from the cited event.
> --- `src/consolidate.rs:595-595` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> if !quote_found(&event.content, evidence) {
> --- `src/consolidate.rs:925-925` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> // - entity files must parse cleanly, each fact must validate;
> --- `src/validate.rs:20-20` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| EPI-CLM-1 | Consolidation produces curated durable facts from journal events | SRC-1 `src/consolidate.rs` implementation; SRC-2 `README.md` doctrine/design | Consolidation and fact storage are designed and implemented | EPI-RTE-1, EPI-RTE-2, EPI-RTE-3, EPI-RTE-5 | None supplied | None; no comparison or deployment evidence | System generates candidate memory records, applies operational filters, and publishes them into durable storage | “Curated” is not demonstrated as warranted acceptance; no evidence-consuming decision names truth criteria, intended use, and scope. |

## Bounded conclusion

`instinctual-memory` implements two routes for turning user/session material into durable fact candidates: deterministic patterns and optional model extraction. The rules path maps selected user phrases to normalized statements. The model path proposes lasting facts and must provide a quote found in the cited event. This quote check supports source occurrence, not truth, entailment, or the model's interpretation. The available evidence leaves the content relation indeterminate for generated statements and source warrant unknown.

The system records extraction dispositions and applies structural/domain validation before publishing Git revisions. Neither stage is an evidence-consuming truth acceptance decision. Explicit remember and correct requests can add or replace claims; forget suppresses and retracts targets operationally. These changes do not establish falsity, reliability, or endorsement. Search and read routes select and expose persisted claims but confer no epistemic warrant. Host use and behavior change remain unobserved.

The design claim of producing “curated facts” is supported only in the operational sense of filtering and storing candidates. No run evidence establishes operation or uptake, and no causal evidence establishes improved memory or future action. The analysis does not establish a system-wide absence of other deployment checks beyond the inspected repository boundary.

## Shared records

### Operative objects

#### EPI-OBJ-1 — Journal event statements
- Closest supplied record: OBJ-1 (runtime CLI/service is a different referent); no counterpart for this content object.
- Source-native identity: journal events with role, source identity, and content.
- Representational form: structured records containing text and metadata.
- Storage substrate: local append-oriented journal; see memory analyst's storage account for detail.
- Evidence: SRC-1 `src/journal.rs` and `src/consolidate.rs`.

#### EPI-OBJ-2 — Entity facts
- Closest supplied record: no counterpart; distinct from OBJ-1's executable.
- Source-native identity: facts attached to entity files, with statements, predicates, kinds, source references, and statuses.
- Representational form: structured metadata plus natural-language statements.
- Storage substrate: Git-backed entity files.
- Evidence: SRC-1 `src/fact.rs`, `src/entity.rs`.

#### EPI-OBJ-3 — Extracted fact candidates
- Closest supplied record: EPI-OBJ-2 is the persisted fact object; candidate is a distinct pre-publication object.
- Source-native identity: rules proposals or LLM fact outputs processed by consolidation.
- Representational form: structured fields including statement and evidence text.
- Storage substrate: in-memory during extraction; accepted output is placed in EPI-OBJ-2.
- Evidence: SRC-1 `src/consolidate.rs`.
- Minimum passage: see the retained consolidation and evidence-quote passages above.

#### EPI-OBJ-4 — Controls and suppression records
- Closest supplied record: no counterpart; operational control state differs from factual claims.
- Source-native identity: suppression, retraction, deletion, and related control entries.
- Representational form: structured identifiers and disposition metadata.
- Storage substrate: Git-backed `state/controls.json`.
- Evidence: SRC-1 `src/controls.rs`, `src/change.rs`.

### Routes

#### EPI-RTE-1 — Rules-based extraction
- Closest supplied records: RTE-1 (general CLI) and EPI-RTE-2 (LLM extraction) are broader/different routes; this is a distinct transformer.
- Endpoints: journal events → regex proposals → entity facts.
- Owner: consolidation code.
- Immediate return: candidates and event disposition; later read-back: persisted facts can be read by later CLI/MCP operations; actual readback not observed.
- Delegated visibility: uninspected host configuration.
- Selection predicate: event role is user and one of a small set of patterns matches.
- Invalidation/expiry: correction, forget, suppression, or later consolidation may revise availability; no general expiry established.
- Activation/effect: durable fact availability is implemented; behavior change unobserved.
- Evidence: SRC-1 `src/consolidate.rs`.

#### EPI-RTE-2 — Model extraction
- Closest supplied records: RTE-1 and RTE-2 cover callers, not this content transformation; distinct from EPI-RTE-1.
- Endpoints: user/note event chunks → configured model proposal → local checks → entity facts.
- Owner: consolidation code calls an external configured model; provider internals inaccessible.
- Immediate return: proposed structured facts or error; later read-back: persisted accepted candidates can be retrieved; operation not observed.
- Delegated visibility: provider receives selected event text; deployed provider/configuration unobserved.
- Selection predicate: user words and memory notes are candidates; code filters model results against batch event references and checks fact fields and source quote.
- Invalidation/expiry: later correction, forget, suppression, or consolidation; general expiry unestablished.
- Activation/effect: memory availability wired, downstream effect unobserved.
- Evidence: SRC-1 `src/consolidate.rs`.
- Theory-builder conditions 1–4: condition 1 `afforded` (prompt formulates a rule for lastingness); condition 2 `not determinable` (the evidence does not show decisions depend on its meaning rather than returned fields/checks); condition 3 `absent` within inspected extraction code (no content-directed criticism and revision route found); condition 4 `absent` within inspected extraction code (no retained criticism shaping a next round). These statuses do not establish absence of inaccessible model processing.
- Addressability: prompt criterion is inspectable as a text instruction; model's internal rationale and learned assumptions are not accessible. Assessment boundary is repository prompt and validation path.
- Persistence: prompt persists in source for successive calls; model judgments are not retained as theory or criticism in the inspected path.
- Learning: not established; no capacity-improvement evidence or causal attribution.
- Reflection: not established; no self-representation of operation and no two-way reflective route evidenced.
- Reflective theory builder: not established.
- Autonomous theory builder: not established; model performs proposal generation but repository checks and external caller control remain separate, and full role coverage is absent.

#### EPI-RTE-3 — Consolidation disposition
- Closest supplied record: EPI-RTE-2 proposes content, but disposition is a separate function.
- Endpoints: extractor results → per-event accepted/quarantined disposition, checkpoint, and candidate changes.
- Owner: consolidator.
- Immediate return: report and published revision; later read-back: disposition file persists in repository.
- Delegated visibility: callers with repository access; actual deployment unobserved.
- Selection predicate: at least one proposal marks an event accepted; otherwise event is quarantined with a reason.
- Invalidation/expiry: next batch writes its own disposition; prior records remain in repository history unless changed externally.
- Activation/effect: controls durable candidate admission, not factual warrant.
- Evidence: SRC-1 `src/consolidate.rs`.

#### EPI-RTE-4 — Domain validation
- Closest supplied record: EPI-RTE-5 invokes it for publication; validation is a distinct gate.
- Endpoints: candidate snapshot and changed paths → validator result.
- Owner: `DomainValidator`.
- Immediate return: pass or error; no persistence of a truth judgment.
- Later read-back: inapplicable; validation result is not retained as a separate epistemic assessment.
- Selection predicate: candidate entity and control structure, allowed references, and state constraints.
- Activation/effect: pass permits publication; failure blocks it.
- Evidence: SRC-1 `src/validate.rs`.

#### EPI-RTE-5 — Candidate publication
- Closest supplied record: runtime RTE-1 general CLI operation; this route identifies consolidation's consequential publish step.
- Endpoints: validated change set → Git revision and receipt.
- Owner: repository publish operation.
- Immediate return: revision receipt or failure; later read-back: published snapshot persists.
- Delegated visibility: repository readers; host permissions unobserved.
- Selection predicate: domain validator succeeds and repository publication succeeds.
- Invalidation/expiry: later revisions may supersede state; Git history retains prior revisions.
- Activation/effect: publishes changed memory for subsequent operations.
- Evidence: SRC-1 `src/consolidate.rs`, `src/repo.rs`, `src/change.rs`.

#### EPI-RTE-6 — Search and read
- Closest supplied records: runtime RTE-1 and RTE-2; annotation of their supplied caller routes, not a new record.
- Endpoints: query → selected fact/journal results → caller response.
- Owner: search/operation implementation, invoked by CLI/MCP caller.
- Immediate return: ranked or filtered content; later read-back: inapplicable to retrieval itself.
- Delegated visibility: host-dependent.
- Selection predicate: query, filters, configured reranker, and operation arguments.
- Invalidation/expiry: source-specific mutations can alter subsequent results.
- Activation/effect: availability to caller is wired; behavioral activation unobserved.
- Evidence: SRC-1 `src/search/`, `src/ops.rs`; runtime RTE-1, RTE-2.

#### EPI-RTE-7 — Explicit memory changes
- Closest supplied records: runtime RTE-1 and RTE-2 are caller routes; this is the distinct memory mutation/admission function.
- Endpoints: caller ChangeRequest → entity/control changes → validated Git revision.
- Owner: caller proposes; code validates request shape and domain state; no separate human or answer oracle evidenced.
- Immediate return: ChangeOutcome receipt or error; later read-back: written facts and controls are available to later store operations, not observed.
- Delegated visibility: caller/deployment dependent.
- Selection predicate: request kind, target identifiers, current entity, and validation rules.
- Invalidation/expiry: correction supersedes; forget retracts and suppresses; Git history preserves prior revisions.
- Activation/effect: changes future availability and re-extraction behavior.
- Evidence: SRC-1 `src/change.rs`, `src/controls.rs`.

### Claims

#### EPI-CLM-1 — Consolidation produces curated facts
- Claimed operation: convert journal events to curated durable facts.
- Source: SRC-1 `src/consolidate.rs` (implementation comment); SRC-2 `README.md` (design description).
- Comparison: EPI-RTE-1 through EPI-RTE-5 implement candidate creation, filtering, and publication, but not evidence-consuming truth acceptance.
- Limit: no run evidence or causal evidence; “curated” is supported as operational selection only.
