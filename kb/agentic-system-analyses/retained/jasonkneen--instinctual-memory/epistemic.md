---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Instinctual Memory's content, evidence gates and reliance routes: what sourced facts and retrieval evaluation license at the frozen revision."
run-id: AAS-2026-10-12-instinctual-memory-af48437aa60c-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual Memory epistemic report

## Source-and-claim boundary

The question is whether converting sessions and instruction files into sourced facts, maintaining them, and delivering them to agents establishes warranted knowledge or only operationally usable candidates. Scope and external exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). All source inspection below is SRC-1 at the frozen commit. Implementation is not observed operation. No target execution was performed.

This overlay assesses acquisition, rule and model extraction, quote checks, publication, duplicate and lastingness judgments, corrections, withdrawal, retrieval ranking, host delivery, instruction writeback, retrieval evaluation, index derivation and timing measurement. Supplied runtime findings remain provisional evidence for paths not independently reread here. No memory or workflow member was supplied. Available support files not independently read are not inaccessible evidence.

| Entry point or operation | Source path | Coverage and evidence basis | Limit |
|---|---|---|---|
| CLI dispatch, ingest and backfill | SRC-1 `src/cli.rs` | Direct dispatch read; acquisition mechanics see [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), supplied account | Adapter fidelity and real source truth not measured |
| Consolidate: rules, LLM, filters and publication | SRC-1 `src/consolidate.rs` | Direct reads of batch, rules, prompt, proposal handling, placement and quote normalization; [EPI-RTE-rules-extraction](#epi-rte-rules-extraction), [EPI-RTE-llm-proposal](#epi-rte-llm-proposal), [EPI-RTE-candidate-gate](#epi-rte-candidate-gate); container see [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) | Provider compliance and semantic preservation unresolved |
| Immediate remember, correct, forget | SRC-1 `src/change.rs`, `src/ops.rs`, `src/cli.rs`, `src/repo.rs`, `src/validate.rs` | Direct shared dispatch read; mechanism and alternatives supplied by [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change) | No independent source truth test or observed caller approval |
| Search, read and history, CLI/MCP/HTTP/shell | SRC-1 `src/mcp.rs`, `src/ops.rs`, `src/search/rerank.rs` | Direct registered tools and shared dispatch read; selection/fallback supplied by [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval) | Ranker internals and actual host reliance uninspected |
| Hook start, prompt, end and sync | SRC-1 `src/hook.rs`, `src/setup.rs` | CLI dispatch read; callbacks supplied by [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks) | Host scheduling, callback completion and activation unobserved |
| Writeback | SRC-1 `src/cli.rs` | Dispatch read; formatting, force and source exclusions supplied by [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback) | Actual instruction-file loading unobserved |
| Tidy preview/apply/keep | SRC-1 `src/tidy.rs` | Direct judgment, filtering and apply read; publication see [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) | No source evidence accompanies lastingness judgment |
| Erase | SRC-1 `src/erasure.rs` | Supplied [RT-RTE-erasure-maintenance](runtime.md#rt-rte-erasure-maintenance) | Sequential effects and external copies prevent universal withdrawal guarantee |
| Evaluate and bench | SRC-1 `src/evaluation.rs`, `src/cli.rs` | Direct scoring and timing reads; [RT-RTE-search-evaluation](runtime.md#rt-rte-search-evaluation), [EPI-RTE-search-benchmark](#epi-rte-search-benchmark) | No supplied result, authenticated holdout or controlled causal experiment |
| Index rebuild | SRC-1 `src/index.rs`, `src/cli.rs` | Direct full index implementation; [EPI-RTE-index-rebuild](#epi-rte-index-rebuild) | Counts reflect stored Active statuses, not truth or endorsement |
| Tasks | SRC-1 `src/ops.rs`, `src/mcp.rs` | Direct registered dispatch; supplied [RT-RTE-task-update](runtime.md#rt-rte-task-update) | Titles are operational directives; individual truth-apt assertions not determinable without actual content |
| Setup and model selection | SRC-1 `src/setup.rs`, `src/search/laya.rs` | Supplied [RT-RTE-integration-admission](runtime.md#rt-rte-integration-admission) | No quality test gates component replacement |
| Init, formats, status, transport administration | SRC-1 `src/cli.rs`, `src/ops.rs` | Direct dispatch; store/status account supplied in runtime | No distinct claim acceptance; not an exhaustive audit of metadata accuracy |

Public warrant claims are [EPI-CLM-sourced-facts](#epi-clm-sourced-facts), [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) and see [RT-CLM-validated-publication](runtime.md#rt-clm-validated-publication). Missing real stores, event/proposal traces and provider responses prevent deciding which observed statements were copied, paraphrased, inferred or invented. Missing source authentication prevents asserting source truth. Missing host traces prevent activation claims. Missing rubric provenance and comparative results prevent retrieval-effectiveness or causal-benefit claims. Missing pinned weights and provider implementation prevent distributed-parametric process or training conclusions. These gaps do not erase the implemented candidate checks or wired later consumption.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-proposal](#epi-obj-proposal) | Name, location, preference, project rule or architecture statement; natural-language candidate plus symbolic routing and evidence fields | Durable candidate | SRC-1 `src/consolidate.rs` | Plausible standing statement need not follow from its quote |
| [EPI-OBJ-source-ref](#epi-obj-source-ref) | Quoted source assertion; source ID/role and link are symbolic | Source lineage | SRC-1 `src/consolidate.rs` | Attribution preserved; source truth and semantic entailment unknown |
| [EPI-OBJ-fact](#epi-obj-fact) | Stored assertion; separately, symbolic status/kind/timestamps govern eligibility | Curated fact | SRC-1 `src/consolidate.rs` | ExplicitAssertion/Active is not evidence-consuming truth acceptance |
| [RT-OBJ-mem-skill](runtime.md#rt-obj-mem-skill) | None as a truth evaluator; source-native procedure | Host review/use guidance: see record | SRC-1 `skills/mem/SKILL.md` | Host compliance unresolved |
| [RT-OBJ-tasks](runtime.md#rt-obj-tasks) | Not determinable for actual titles; task directives need not be truth-apt | Versioned tasks: see record | SRC-1 `src/ops.rs` | Version admission does not validate content |
| [RT-CMP-llm-config](runtime.md#rt-cmp-llm-config) | Opaque numerical model state; truth-apt localized content not determinable | Extraction and cleanup: see record | SRC-1 `src/consolidate.rs` | Requested semantic judgments not evidence of reliable execution |
| [RT-CMP-jev-reranker](runtime.md#rt-cmp-jev-reranker) | Opaque state; relevance scores are query/candidate judgments, not source verification | Ranking: see record | SRC-1 `src/jev.rs` | No independent truth license |
| [RT-CMP-laya-reranker](runtime.md#rt-cmp-laya-reranker) | Opaque state; cross-encoder output ranks candidates | Ranking: see record | SRC-1 `src/search/laya.rs` | No pinned weight digest or measured benefit |

Raw journal assertions, cleanup findings, rubric checks and index counts are addressed by their route records rather than creating duplicate container objects. New objects describe proposal, lineage and eligibility parts absent from the supplied object inventory; their identities and forms are in Shared records.

## Authority-route ledger

Each row is a consequential function, not a second declaration of a supplied route. Linked functions sharing a container retain independent epistemic assessments. Activation, timing, possible results and generic ownership are see the cited record; local license and mismatch assessments are this overlay's findings. No observed operation is established.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) | content transformation | implemented | [EPI-OBJ-source-ref](#epi-obj-source-ref) | truth-apt transformation: acquisition/import | Session/file text to journal and extractor input | Adapter/source role selection; not source authentication | see route | see route | Retains attributed text | Source warrant unknown; imported, not newly discovered truths | Makes eligible inputs available | see route | SRC-1 `src/cli.rs` | [EPI-CLM-sourced-facts](#epi-clm-sourced-facts) | none | Fidelity depends on adapters and original origin |
| [EPI-RTE-rules-extraction](#epi-rte-rules-extraction) | content transformation | implemented | [EPI-OBJ-proposal](#epi-obj-proposal) | truth-apt transformation: indeterminate | Regex match to standing assertion | Fixed lexical patterns on User text | see route | see route | Proposes without semantic adjudication | Conditional paraphrase under intended reading; counterexample below | Proposals can become active facts | see route | SRC-1 `src/consolidate.rs` | [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) | Regex matching is not a lastingness test | Quotation, negation and always/never distinction can change meaning |
| [EPI-RTE-llm-proposal](#epi-rte-llm-proposal) | content transformation | implemented | [EPI-OBJ-proposal](#epi-obj-proposal) | truth-apt transformation: indeterminate | Bounded event text to statement/evidence/lasting | Chat model instructed to extract, not guess | see route | see route | Produces candidates and self-assessed lasting flag | No established entailment or independent semantic warrant | Feeds software gate | see route | SRC-1 `src/consolidate.rs` | [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) | Requested judgment is not verified compliance | Copies, reshaping, entailed inference or conjecture require actual linked responses to distinguish |
| [EPI-RTE-candidate-gate](#epi-rte-candidate-gate) | check/evidence production | implemented | [EPI-OBJ-proposal](#epi-obj-proposal), [EPI-OBJ-source-ref](#epi-obj-source-ref) | no content change | Quote occurrence, flag, statement bounds, usable routing | Deterministic normalized ordered-fragment matching; model flag consumed as given | see route | see route | Enforcing eligibility gate | Licenses normalized quote occurrence in cited event, not entailment or source truth | Rejects malformed/unmatched candidates | see route | SRC-1 `src/consolidate.rs` | [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) | Quote and statement are checked differently | Evidence fragments below eight characters are discarded; no statement-to-evidence semantic check |
| [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) | disposition/acceptance | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | Candidate placement and publication | Duplicate/suppression gates, DomainValidator and CAS | see route | see route | Operational admission | No evidence-consuming acceptance of produced ampliative claim against truth criterion | Writes explicit assertions as Active | see route | SRC-1 `src/consolidate.rs` | [RT-CLM-validated-publication](runtime.md#rt-clm-validated-publication) | Structural validation is not semantic acceptance | Accepted event disposition can coexist with placement dropping a proposal |
| [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) | retention | implemented | [EPI-OBJ-fact](#epi-obj-fact), [EPI-OBJ-source-ref](#epi-obj-source-ref) | no content change | Facts, sources, checkpoint and dispositions | Git publication after candidate checks | see route | see route | Durable snapshot/reload | Preserves attribution and status, not added truth warrant | Later retrieval and consolidation can rely operationally on retained state | see route | SRC-1 `src/consolidate.rs` | [EPI-CLM-sourced-facts](#epi-clm-sourced-facts) | Retention is not lifecycle integration after epistemic acceptance | Linked evidence is useful lineage without verified entailment |
| [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) | lineage/freshness/recovery | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | Old file-source versions to superseded status | Source ID version comparison, not independent truth check | see route | see route | Eligibility changes | Freshness relative to imported file version only | Removes old-source facts from active consumption | see route | SRC-1 `src/consolidate.rs` | [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) | Changed file does not prove previous claim false | No semantic equivalence/contradiction test on changed file |
| [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change) | content transformation | implemented | [EPI-OBJ-fact](#epi-obj-fact) | truth-apt transformation: acquisition/import | Caller statement to explicit assertion/correction | Caller chooses content; software checks structure | see route | see route | Operationally admitted assertion | Source warrant unknown; no extraction quote gate | Adds/replaces/suppresses facts | see route | SRC-1 `src/change.rs` | [RT-CLM-validated-publication](runtime.md#rt-clm-validated-publication) | Correction label not a correctness test | Human authorship/approval unresolved; replay shortcut may report new input without applying it |
| [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change) | disposition/acceptance | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | Structural admission and targeted supersession/retraction | Request checks, validator/CAS, caller target | see route | see route | Enforcing current-read eligibility | Operational acceptance only | Remember/correct/forget current fact state | see route | SRC-1 `src/change.rs` | [RT-CLM-validated-publication](runtime.md#rt-clm-validated-publication) | Soft forget does not withdraw raw source assertions | Raw journal search and prior delivered context remain separate |
| [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) | check/evidence production | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | Duplicate statements and session-only usefulness | Word containment/Jaccard; optional LLM over IDs/statements | see route | see route | Findings only without apply | Lexical similarity and requested temporal usefulness judgments, not truth checks | Proposes removals | see route | SRC-1 `src/tidy.rs` | [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) | Longest is not necessarily semantically most complete | Contradictory assertions can share almost all words; sources not given to judge |
| [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) | disposition/acceptance | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | Findings to suppression/retraction | Apply flag, keep exclusions, validator/CAS | see route | see route | Enforcing current fact eligibility | No positive truth acceptance of surviving assertions | Withdraws selected facts from future fact reads | see route | SRC-1 `src/tidy.rs` | none | Skill review is not executable approval; apply recomputes | Survivor status does not certify truth or lastingness |
| [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval) | operational admission/selection/consumption | implemented | [EPI-OBJ-fact](#epi-obj-fact), raw events in see route | no content change | Query-relative hits/ranks | Lexical shortlist and optional JEV/local scorer | see route | see route | Ranking and truncated delivery | Query relevance, not verification; retrieved raw assertions retain unknown warrant | Determines supplied context | see [RT-BAP-host-context](runtime.md#rt-bap-host-context) | SRC-1 `src/ops.rs` | none | Ranking is not endorsement | Shortlisting/filtering/fallback constrain consumer visibility |
| [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks) | operational admission/selection/consumption | implemented | [EPI-OBJ-fact](#epi-obj-fact) | no content change | Preferences/matching facts to host context | Fact status, lexical overlap and delivery caps | see route | see route | Advisory unsolicited context | Hook warns to check against code if changed | Can shape later host action if interpreted | see [RT-BAP-host-context](runtime.md#rt-bap-host-context) | SRC-1 `src/hook.rs` | none | Delivery not activation | Already delivered context has no enforced revocation |
| [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback) | content transformation | implemented | [EPI-OBJ-fact](#epi-obj-fact) | truth-apt transformation: non-ampliative reshaping | Selected statements to managed instruction block | Fixed status/source/project selection and formatting | see route | see route | Persistent context placement | Copies claims, adds no truth warrant | Makes statements available through later instruction loading | see [RT-BAP-instruction-file](runtime.md#rt-bap-instruction-file) | SRC-1 `src/cli.rs` | [EPI-CLM-sourced-facts](#epi-clm-sourced-facts) | Channel may grant practical influence without verification | Host loading external; force and backfill feedback remain bounded by supplied route |
| [RT-RTE-erasure-maintenance](runtime.md#rt-rte-erasure-maintenance) | disposition/acceptance | implemented | [EPI-OBJ-fact](#epi-obj-fact), [EPI-OBJ-source-ref](#epi-obj-source-ref) | no content change | Caller-targeted content withdrawal | Target lookup and sequential store/history scrub | see route | see route | Destructive removal | Does not assess falsehood; removes lineage as well as assertions | Changes future fact/journal/history visibility if stages finish | see route | SRC-1 `src/erasure.rs` | none | Deletion completion flag precedes later effects | Partial failure/external copies prevent universal withdrawal |
| [RT-RTE-search-evaluation](runtime.md#rt-rte-search-evaluation) | check/evidence production | implemented | Returned hits and caller rubric in see route | no content change | Expected IDs and required/forbidden text in top hits | Deterministic caller-supplied oracle, bounded retrieval cases | see route | see route | Report-only comparison | Pass means rubric satisfaction, not true answers, explanation validity or transfer | No automatic model/content promotion | Caller via report; informational, current evaluation | SRC-1 `src/evaluation.rs` | none | Held-out description is not authenticated independence | Empty expected/string lists permit vacuous per-case checks; snapshots/providers may vary between runs |
| [EPI-RTE-index-rebuild](#epi-rte-index-rebuild) | content transformation | implemented | Entity metadata and Active statuses in see route | truth-apt transformation: entailed derivation | Active counts and entity listing | Deterministic filtering/counting within stored-status domain | see route | see route | Published derived metadata | Correct only relative to parsed snapshot and predicate; no truth status implied | Supplies bounded navigation metadata | see route | SRC-1 `src/index.rs` | none | none | Counts are not suppression-aware truth counts; unparseable entities omitted |
| [EPI-RTE-search-benchmark](#epi-rte-search-benchmark) | check/evidence production | implemented | Timing observations in see route | no content change | Duration of selected search calls | Instant elapsed time and repeated call summaries | see route | see route | Report-only measurement | Selected-process latency, not semantic quality or component causality | No implemented promotion/update | Caller via stdout; informational, current benchmark | SRC-1 `src/cli.rs` | none | none | No actual run or environment controls supplied |
| [RT-RTE-task-update](runtime.md#rt-rte-task-update) | operational admission/selection/consumption | implemented | [RT-OBJ-tasks](runtime.md#rt-obj-tasks) | non-truth-apt policy/content update: task directive appended | Version-matched caller task | Lock and expected-version check | see route | see route | Durable task admission | No content truth license; actual titles could additionally carry assertions | Later host sees task title | see route | SRC-1 `src/ops.rs` | none | none | No task execution or improvement established |
| [RT-RTE-integration-admission](runtime.md#rt-rte-integration-admission) | behavior/policy adaptation | implemented | Components and installed skill in see route | non-truth-apt policy/content update: caller configuration | Host integration/model choice | Caller settings, supported names and load checks | see route | see route | Installs configuration | No measured semantic quality admission | Changes future available callbacks/inference machinery | see route | SRC-1 `src/setup.rs` | none | Configuration is not evidence-responsive self-improvement | Parameter updates not performed by inspected client; provider internals uninspected |

No lifecycle-integration-after-truth-acceptance witness is established by these routes. Evidence links, publication, supersession and retrieval implement useful ledger functions without establishing the type's evidence-consuming acceptance of a produced ampliative claim. This is a bounded assessment of inspected/supplied routes, not an assertion about inaccessible model internals or every possible caller assertion.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-sourced-facts](#epi-clm-sourced-facts) | Curated sourced facts with later search/read/writeback | SRC-1 `README.md`; doctrine/design | see claim | [EPI-RTE-rules-extraction](#epi-rte-rules-extraction), [EPI-RTE-llm-proposal](#epi-rte-llm-proposal), [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback) | None supplied | No answer improvement experiment | Durable assertions with source linkage and consumption wiring | Sourced is not source-verified; direct ops assertions have no source refs |
| [EPI-CLM-lasting-facts](#epi-clm-lasting-facts) | Only durable facts with matching evidence survive extraction | SRC-1 `README.md`, `src/consolidate.rs`; doctrine/design | see claim | [EPI-RTE-llm-proposal](#epi-rte-llm-proposal), [EPI-RTE-candidate-gate](#epi-rte-candidate-gate), [EPI-RTE-rules-extraction](#epi-rte-rules-extraction), [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) | None supplied | No independent temporal test or source-entailment adjudication | LLM route requests lastingness and enforces flag/quote checks; cleanup can revise eligibility | Rules have no equivalent lasting flag; word matches can misrepresent source intent |
| [RT-CLM-validated-publication](runtime.md#rt-clm-validated-publication) | Validated changes and no concurrent overwrite | SRC-1 `README.md`; doctrine/design | see claim | [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change) | None supplied | Requires cooperating publisher/Git; custom-validator and other file effects differ | Structural validation/CAS, not truth evaluation | Replay short-circuit and validator limitations see supplied records; not superseded here |

The evaluator's module calls itself held-out evaluation, but its inspected contract authenticates neither authorship nor independence of the caller rubric. A passing expected-ID/string check is evidence about returned hit composition only (SRC-1 `src/evaluation.rs`; see [RT-RTE-search-evaluation](runtime.md#rt-rte-search-evaluation)).

## Bounded conclusion

Instinctual Memory acquires externally supplied assertions, retains their attributed fragments and operational statuses, and later supplies selected content through search, hooks and instruction files. Those are independently supported capacities. Source warrant remains unknown: source linkage is not source authentication, and source occurrence is not semantic support for a rewritten statement. The LLM route requests extraction without guesses, but actual linked outputs are absent, so its content relation remains indeterminate rather than being classified automatically as conjecture or entailment.

The software quote gate licenses ordered normalized fragment presence. The model's lasting flag licenses operational admission under the product's temporal-usefulness policy; no independent temporal or truth oracle checks that flag. Rules are deterministic but can discard distinctions in source meaning. Direct assertions and corrections bypass extraction checks. None of these facts means that every admitted assertion is false or that the model cannot extract correctly; it means structural eligibility does not supply the missing claim warrant.

Tidy separately evaluates lexical duplication and model-judged session-only usefulness, then optionally suppresses candidates. Keep exclusions provide veto, while human review is a host procedure and apply recomputes findings. Surviving claims are not thereby accepted as true. Forget changes current fact eligibility, not raw source assertions; erase attempts broader sequential removal and can leave partially completed effects. Prior host context and external copies lie beyond enforced withdrawal.

Retrieval relevance judgments have ranking force, not verification force. Hook and writeback delivery can influence a host over later sessions, but no host trace demonstrates activation or benefit. Index counts are entailed within the stored Active-status domain, not evidence of factual correctness. Retrieval evaluation checks a caller rubric; timing measures selected searches. Both return information without an automatic consumer that promotes a model, revises knowledge or adapts policy.

Retention and explicit source attachment are established; acceptance and lifecycle integration of produced ampliative claims are not established by the assessed routes. Trace-fed writes and later reads afford behavioral adaptation without proving improved capacity. Static instructions, maintenance and caller configuration do not establish autonomous iterative criticism of the system's own method. Provider learning/reflection remains uninspected; no single conclusion about these independent properties follows from quote checks, curation or parameter opacity.

## Shared records

### Operative objects

#### EPI-OBJ-proposal
Label: Extraction proposal

Source-native identity: `Proposal`, with LLM input represented by `LlmFact`. Natural-language statement/evidence supply claim content; symbolic entity/predicate/ref/lasting fields control placement and admission. Storage substrate: transient Rust values/model JSON, before durable Fact publication. These objects are parts of the supplied consolidation route, not replacements for its full loop; no supplied object counterpart was declared. SRC-1 `src/consolidate.rs`, implementation.

> /// A fact the extractor wants to record, before it becomes a [`Fact`].
> --- `src/consolidate.rs`

#### EPI-OBJ-source-ref
Label: Fact source reference

Source-native identity: `SourceRef` as constructed by `Extraction::place`. Natural-language evidence is retained alongside symbolic event ID and role in entity YAML. Storage substrate: published entity file in bare Git. Distinct from proposal and stored statement: its consumer can identify source text without verifying the statement. Closest supplied route is [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation); no source-reference object counterpart in supplied inventory. SRC-1 `src/consolidate.rs`, implementation.

> sources: vec![SourceRef {
>                 event_id: event.event_id.clone(),
>                 role: fact_role(event.role),
>                 evidence: p.evidence,
>             }],
> --- `src/consolidate.rs`

#### EPI-OBJ-fact
Label: Published explicit assertion

Source-native identity: `Fact` constructed in `Extraction::place`. Natural-language statement is interpreted by a host; symbolic kind/status/timestamps and ID determine software eligibility and references. Storage substrate: entity YAML/Markdown in Git snapshots. Proposal is transient, SourceRef carries lineage, and Fact carries published content and eligibility. Closest supplied record is [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation), not an existing Fact object declaration. SRC-1 `src/consolidate.rs`, implementation.

> statement: p.statement,
>             kind: FactKind::ExplicitAssertion,
>             status: FactStatus::Active,
> --- `src/consolidate.rs`

### Routes

#### EPI-RTE-rules-extraction
Label: Rules extraction
Part of: [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation)

Owner/endpoints: rules_extract takes bounded events and existing/blocked state, proposes name/location/preferences, and passes each Proposal to place. Trigger: batch chooses rules explicitly or Auto without LLM configuration. Software regexes propose and decide; caller selects mode, not per-fact content. No semantic answer oracle; open extraction mode. Guidance is fixed patterns, not requested lastingness model evaluation. Publication/rollback follow the parent route. Placement can veto suppression and near duplicates; ordinary matching cannot distinguish source assertion from reported speech. SRC-1 `src/consolidate.rs`, implementation.

Concrete code deduction: User input `please always use tabs` yields statement `User requested: use tabs` and evidence `please always use tabs`; `please never use tabs` yields the identical statement, predicate and entity, but opposite original directive. The capture omits always/never/don't, and the statement includes only cap[1]. The fixed entity/predicate/statement digest then identifies the same fact, with no sign bit distinguishing polarity. Input `The example says my name is Alice` also matches the name regex despite not asserting the actual user's name. Thus deterministic execution does not imply warranted semantic preservation. Normal literal name/location declarations may be faithful reshaping; across eligible User inputs, remaining alternatives include reshaping, entailed interpretation or unsupported attribution. Without contextual checks, relation is indeterminate. These are deductions from inspected code, not target runs.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Extraction with proposals placed, counts, accepted event sequences or quarantine reasons.
- Later read-back: Published statements and sources reach subsequent consolidation/retrieval/hooks/writeback through the parent route.
- Delegated visibility: No provider called; later readers see admitted statements and sources, not the original regex decision trace.
- Selection predicate: User role and matching name/live/preference pattern, then blocked/duplicate/space checks.
- Invalidation or expiry: Controls and parent supersession/withdrawal alter later eligibility.
- Activation or effect: Candidate generation/placement wired; host behavior and semantic quality unobserved.
- Evidence limits: Contextual interpretation is not checked; source assertions are not authenticated.

> let pref_re = Regex::new(r"(?i)please (?:always|never|don't)\s+([a-z][^.!?]+)").unwrap();
> --- `src/consolidate.rs`

> statement: format!("User requested: {}", cap[1].trim()),
> --- `src/consolidate.rs`

#### EPI-RTE-llm-proposal
Label: LLM extraction proposal
Part of: [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation)

Owner/endpoints: llm_extract selects event text, sends bounded batches and known entity summaries to [RT-CMP-llm-config](runtime.md#rt-cmp-llm-config), receives LlmFact JSON and forwards in-batch refs to candidate gate. Guidance asks for standing facts useful next month, excludes session requests/guesses, and prioritizes distinct standing rules in memory files. Trigger and mode: configured LLM extraction of accumulated events, not held-out experiment. Model proposes statement and lastingness; software can veto; no human content approval or independent truth oracle. Errors abort rather than publish partially ready batch. Parent owns final publication/recovery. SRC-1 `src/consolidate.rs`, implementation and doctrine/design. Relation is indeterminate without linked response evidence: the prompt asks acquisition/reshaping, but neither guarantees output equivalence nor establishes non-entailment required for a conjecture classification.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed candidate facts with event refs, lasting flag, entity, statement and evidence.
- Later read-back: Admitted output persists as facts; later batches receive existing-entity summary and downstream consumers receive statements.
- Delegated visibility: Provider receives selected user/Note text, project and known-entity context; other roles excluded.
- Selection predicate: Note text or filtered User text; bounded/chunked batches; output event ref must belong to batch.
- Invalidation or expiry: Failed gates/drop conditions prevent placement; later controls/freshness affect published facts.
- Activation or effect: Model request and proposal pipeline wired; actual compliant extraction unobserved.
- Evidence limits: Provider processing and weights uninspected; actual output lineage absent.

> The test for every candidate: would a new teammate, starting fresh next month, need to know this? If it only describes what was happening in that session, it is not a fact.
> --- `src/consolidate.rs`

> memory_file events are curated project instructions (AGENTS.md, CLAUDE.md, README.md): record every distinct standing rule, convention, architecture fact, and command in them, one fact each; skip only examples, history, and prose that states nothing."#;
> --- `src/consolidate.rs`

#### EPI-RTE-candidate-gate
Label: LLM candidate eligibility gate
Part of: [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation)

Owner/endpoints: check_llm_fact consumes LlmFact/event/existing entities and returns Proposal or reason; quote_found checks evidence occurrence. It does not itself decide publication. Target/domain: normalized cited-event fragment occurrence, minimum evidence length, statement bounds, lasting flag and usable entity/predicate. Fixed program decides eligibility, model supplies flag/content; no human veto in this substep and no semantic oracle. Trigger: each in-batch LLM candidate; open extraction. Failed checks drop candidates. Parent placement/publication owns retention/recovery. SRC-1 `src/consolidate.rs`, implementation.

Concrete deduction: source `Alpha beta gamma` and evidence `Alpha beta gamma...NO` normalize to one qualifying fragment because `NO` is under eight characters. Matching succeeds despite the unmatched short fragment. The quote gate also lowercases and strips Markdown marks. A statement `User lives in Paris.` paired with a matching quote `User lives in London.` can pass the inspected gate if its other fields satisfy the structural conditions; no statement/quote entailment relation is tested. Neither deduction claims such a model output actually occurred.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Proposal or rejection reason; normalized matching Boolean is internal evidence.
- Later read-back: inapplicable — this gate itself retains no result; downstream published sources/status are owned by consolidation.
- Delegated visibility: No new model call; caller loop receives Proposal/reason, optional verbose errors expose rejection text.
- Selection predicate: Lasting true; evidence at least eight characters; statement 8–600 characters; matching qualifying fragments; usable routing.
- Invalidation or expiry: inapplicable — current candidate check is not a durable grant; future publication is separate.
- Activation or effect: Enforces eligibility before placement; does not license source truth or semantic entailment.
- Evidence limits: Flag is self-assessment; short fragments ignored; no independent semantic or temporal check.

> if !fact.lasting {
>         return Err("not lasting (true for one session only)");
>     }
> --- `src/consolidate.rs`

> if !quote_found(&event.content, evidence) {
>         return Err("evidence not found in the cited event");
>     }
> --- `src/consolidate.rs`

> .map(normalise)
>         .filter(|f| f.chars().count() >= 8)
>         .collect();
> --- `src/consolidate.rs`

#### EPI-RTE-index-rebuild
Label: Index metadata derivation

No supplied counterpart after comparison with runtime's routes: cmd_index dispatch is mentioned there, but standalone index rebuild/count derivation was not declared. This route concerns only metadata publication, not consolidation's full loop.

Owner/endpoints: CLI cmd_index calls index::rebuild; current head's parseable entities produce ID/type/title/Active-count rows, sorted and bounded at 60,000 bytes, with omitted-entity count appended. Program derives counts from stored predicates; no external truth oracle. Trigger: caller command; open maintenance. Caller starts rebuilding, fixed program chooses rows, DomainValidator/CAS can reject publication. It reuses old head when unchanged. Guidance is canonical index schema; Git prior revisions permit external recovery, not semantic rollback. SRC-1 `src/index.rs`, `src/cli.rs`, implementation. Entailed derivation is bounded to parsed entity facts' stored status: it does not mean true, unsuppressed, endorsed or useful facts. Example deduction: an entity with one Active and one Retracted fact renders one active fact; no fact's proposition is tested.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Unchanged head or published index revision; CLI reports which.
- Later read-back: Later snapshot/file readers can read retained INDEX.md metadata.
- Delegated visibility: No model delegation; index readers see bounded rows and omitted-entity count, not all source evidence.
- Selection predicate: Eligible entity files that parse; sort by entity ID; budget stops listing; counts filter Active status.
- Invalidation or expiry: Rebuild replaces derived index from current head; other publishers also refresh it.
- Activation or effect: Metadata publication wired; exercised navigation use unobserved.
- Evidence limits: Does not establish entity/source truth; malformed entities silently omitted from derivation.

> let active = entity.facts.iter().filter(|f| f.status == FactStatus::Active).count();
> --- `src/index.rs`

> if current.as_deref() == Some(body.as_str()) {
>         return Ok(base);
>     }
> --- `src/index.rs`

#### EPI-RTE-search-benchmark
Label: Search timing benchmark

Distinct from [RT-RTE-search-evaluation](runtime.md#rt-rte-search-evaluation): shares combined_search, but evaluates elapsed duration rather than caller expected hits/text. Runtime locates bench without declaring this measurement route.

Owner/endpoints: caller Bench queries/options invoke repeated combined_search calls; Instant measures elapsed milliseconds and print_bench_row summarizes durations/ranker/hits. Target/domain: calls in this process/store/environment, not source truth or answer correctness. Program measures; caller supplies cases and repetition settings. No reference-answer oracle or content veto. Mode: bounded caller-selected timing comparison, not production improvement trigger. It prints lexical and optional reranked summaries, admits no knowledge/model change and supplies no automatic winner consumer. SRC-1 `src/cli.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed timing summaries, ranker and hit counts; errors reject completion.
- Later read-back: inapplicable — route retains no report for production adaptation.
- Delegated visibility: Search rankers receive usual query/candidate inputs; caller sees aggregate timings.
- Selection predicate: Caller queries/project/limit and iteration counts; lexical always, reranked when rerank_iterations exceeds zero.
- Invalidation or expiry: inapplicable — report-only measurements have no retained grant.
- Activation or effect: Timing/report code wired; no observed measurements or policy updates.
- Evidence limits: Sequential comparisons, caching, provider and environment changes can confound attribution; no actual result supplied.

> ms.push(start.elapsed().as_secs_f64() * 1000.0);
> --- `src/cli.rs`

### Claims

#### EPI-CLM-sourced-facts
Label: Curated sourced facts

Claimed operation: imported conversations/instruction files become curated sourced facts with later search/read/change/writeback. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-validated-publication](runtime.md#rt-clm-validated-publication), which claims validation/CAS rather than source-backed content. The source term facts is assessed as a product claim, not assumed epistemic acceptance.

> `mem` reads the conversations you have already had with Claude Code, Codex, and OpenCode, plus your `AGENTS.md`/`CLAUDE.md`/`README.md` files, and turns them into a small set of curated, sourced facts stored in a plain Git repository. Agents search that memory (facts and raw sessions together), read it over MCP, change it through a validated path, and get it written back into each project's `AGENTS.md`.
> --- `README.md`

#### EPI-CLM-lasting-facts
Label: Lasting fact admission

Claimed operation: extraction keeps only content still true/useful next month and evidence appearing in cited source. SRC-1 `README.md`, `src/consolidate.rs`, doctrine/design. Related to [EPI-CLM-sourced-facts](#epi-clm-sourced-facts) but distinct criterion; no supplied lastingness claim counterpart. Prompt and quote gate establish requested model judgment and lexical enforcement, not reliable semantic adjudication.

> A fact is worth keeping only if it will still be true and useful in a session weeks from now, in a different task: the user's identity and role, standing preferences and working rules, project facts (what it is, stack, architecture, conventions, commands, decisions and why), and named people or organisations with a stated relationship.
> --- `src/consolidate.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; supplied [RT-BAP-host-context](runtime.md#rt-bap-host-context) and [RT-BAP-instruction-file](runtime.md#rt-bap-instruction-file) cover the consequential external channels.
