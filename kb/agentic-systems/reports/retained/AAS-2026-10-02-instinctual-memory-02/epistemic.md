---
type: agentic-systems/types/agentic-system-epistemic-report.md
description: "Instinctual-memory epistemic routes: source-backed candidate selection, semantic limits, cleanup judgments and retrieval evaluation"
run-id: AAS-2026-10-02-instinctual-memory-02
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual-memory epistemic report

## Source-and-claim boundary

The question is how `mem` acquires or produces truth-apt memory, checks it, admits reliance and changes later behavior. The frozen whole-system boundary and Source register are supplied in boundary.md. SRC-1 is implementation; SRC-2 is doctrine/design. External coding-agent loops, provider internals, model weights and dependency implementations are excluded. The analysis uses source and supplied runtime records, with no observed run or causal experiment.

EPI-CLM-1 claims curated sourced facts; EPI-CLM-2 claims lasting selection, cited evidence and restatement removal; EPI-CLM-3 claims validated concurrent publication. These are operational claims with epistemic consequences, rather than a promise of universally true memory. Their scopes remain separate.

| Entry point or operation | Source path | Coverage and reading basis | Exclusion/uninspected limit and conclusion prevented |
|---|---|---|---|
| CLI dispatch and exported library | SRC-1: `src/cli.rs` | Direct command-variant search, benchmark/evaluation bodies, direct `src/lib.rs` exports; supplied RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11 individually referenced below | Other CLI formatting/adapter internals are not fully reread; prevents a system-complete semantic absence claim |
| MCP, HTTP and shell operations | SRC-1: `src/mcp.rs` | Direct MCP dispatch/tool opening; supplied RTE-1, RTE-2, RTE-7 for shared operation semantics; supplied runtime account for HTTP/shell dispatch | Host tool selection and real transport activation unobserved |
| Ingest/backfill and journal | SRC-1: `src/ingest.rs` | Supplied RTE-10 and OBJ-2 | Adapter-level source fidelity is not independently established; imported warrant remains unknown |
| Rules/LLM extraction, checks, placement and old-file retirement | SRC-1: `src/consolidate.rs` | Direct rules, prompt, batching/admission, placement, overlap, evidence check and retirement bodies; RTE-3, EPI-OBJ-1 | No input/output trace establishes semantic preservation or improved future action |
| Request change / correction / forget | SRC-1: `src/change.rs` | Direct validation/correction source search; supplied RTE-2 publication and replay passages; direct `src/fact.rs`, `src/validate.rs` | External proposer's reasons and source truth uninspected |
| Tidy diagnosis and application | SRC-1: `src/tidy.rs` | Direct full diagnosis and opening retraction body; RTE-4, EPI-OBJ-2 | Actual model judgments and cleanup utility unobserved |
| Eligibility / rank / read / history | SRC-1: `src/fact.rs` | Direct eligibility; supplied RTE-1 and CMP-2, CMP-3 | Relevance scores and status do not establish truth or host uptake |
| Erasure / recovery / index | SRC-1: `src/erasure.rs` | Supplied RTE-6 and RTE-2, RTE-3 publication; direct domain validator | Complete deletion across excluded host/provider copies unassessed; prevents global withdrawal guarantee |
| Hooks / writeback / setup | SRC-1: `src/hook.rs` | Supplied RTE-5, RTE-8, OBJ-3, BAP-1 | Actual host reliance and compliance outside boundary |
| Rubric evaluation | SRC-1: `src/evaluation.rs` | Direct evaluator through scoring; supplied RTE-11; EPI-OBJ-3 | No rubric execution, independence evidence or measured improvement |
| Timing benchmark | SRC-1: `src/cli.rs` | Direct `cmd_bench`; EPI-RTE-1, EPI-OBJ-4 | No timing observations or controlled component comparisons |
| Tasks and model administration | SRC-1: `src/ops.rs` | Supplied RTE-7, RTE-9 | Administrative updates included as operational adaptation; task completion and model quality unassessed |
| Design claims | SRC-2: `README.md` | Direct scoped claim search and retained passages; EPI-CLM-1, EPI-CLM-2, EPI-CLM-3 | Referenced PRD absent according to boundary; conformance not determinable |

This coverage combines direct reads with supplied findings rather than treating all paths as independently read in full. No relevant entry-point family identified here is silently omitted. Supplied records support transport/export and administration accounts; narrower source reads support the semantic assessments. Unassessed adapter branches and opaque model processing prevent a whole-system negative about all possible informal checking.

## Epistemic-object inventory

| Object ID and assessed part | Candidate truth-apt content or none | Claimed role | Evidence | Gap/limit |
|---|---|---|---|---|
| OBJ-2 — source-event content | User assertions, project-file assertions, transcript text; attribution itself can be truth-apt | Imported source for extraction and raw retrieval; see OBJ-2 | SRC-1: `src/ingest.rs` | Acquisition preserves recorded content/provenance, not established source warrant or universal adapter fidelity |
| EPI-OBJ-1 — proposed fact | Standing statement, cited fragment and `lasting` judgment | Candidate before placement/publication; see EPI-OBJ-1 | SRC-1: `src/consolidate.rs` | Statement and quote are different objects of checking; occurrence need not support the statement |
| OBJ-1 — published statements | Structured `Fact.statement`, including rules/preferences and assertions | Persistent later-retrievable memory; see OBJ-1 | SRC-1: `src/fact.rs` | OBJ-1 combines statements, sources and controls; needs a canonical split when their checks/authority differ |
| OBJ-1 — fact provenance | Event ID, role and evidence string | Source link for retained statement; see OBJ-1 | SRC-1: `src/consolidate.rs` | Checked occurrence only on model extraction path; immediate changes do not share that gate |
| OBJ-1 — statuses and controls | Status records say which content is active/superseded/retracted; suppression is an operational policy | Eligibility and prevention of reinsertion; see OBJ-1 | SRC-1: `src/fact.rs` | Status labels are not independent endorsements; distinguish administrative action from falsification |
| OBJ-1 — checkpoints/dispositions/receipts | Operational claims about processed windows and publication | Recovery and future batching; see OBJ-1 | SRC-1: `src/consolidate.rs` | `accepted` event may contain a proposal dropped by placement; count is not semantic acceptance or fact count |
| EPI-OBJ-2 — tidy finding | Claims that fact is duplicate or session-only | Proposed withdrawal; see EPI-OBJ-2 | SRC-1: `src/tidy.rs` | Different evaluators and evidence domains require separate ledger rows |
| EPI-OBJ-3 — rubric/report | Expected answer membership and string criteria; scores relative to those criteria | Retrieval assessment; see EPI-OBJ-3 | SRC-1: `src/evaluation.rs` | Oracle correctness and independence uninspected |
| EPI-OBJ-4 — timing/report | Invocation duration summaries and last returned hit count/ranker | Operational measurement; see EPI-OBJ-4 | SRC-1: `src/cli.rs` | Timing does not warrant retrieved propositions |
| OBJ-3 — exported fact/guidance content | Fact statements may be truth-apt; standing instructions are policy | External host context; see OBJ-3, BAP-1 | SRC-1: `src/hook.rs` | Export adds potential behavioral force without another semantic check |
| OBJ-4 — task titles | Intended actions, not necessarily propositions | Caller-managed tasks; see OBJ-4 | SRC-1: `src/ops.rs` | Version validity licenses append, not task feasibility or completion |
| CMP-1, CMP-2, CMP-3 — model state | Not determinable as individuated propositions from accessible source | Extractor or relevance judgment; see those components | SRC-1: `src/consolidate.rs` | Provider/dependency internals inaccessible; no inference that opaque computation lacks informal reasoning |

## Authority-route ledger

Every ledger entry is architecturally implemented, with operation uninspected because the boundary supplies no execution evidence. Repeated supplied IDs denote separate functions or material parts of the same route; reconciliation would need to split RTE-3 and RTE-4 to give these functions distinct canonical IDs. New object records are distinct intermediate artifacts, not replacements for supplied objects.

Route ID: RTE-10
Route function: content transformation
Architectural status: implemented
Object/candidate ID: OBJ-2
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Local transcript or memory-file record
Evaluator/condition and domain: Adapter parsing and journal identity checks; see RTE-10
Activation and timing: Explicit ingest/backfill or hook sync; no observed operation
Possible or observed result: Serialized source event or parse/write failure
Implemented force: Import and identity admission; see RTE-10
Epistemic authority and scope: Source warrant unknown; recording an assertion does not verify it
Operational authority: Makes recorded text available to raw search and consolidation
Behavioral-authority path: Journal reader, persisted source events, permissive input, later invocations
Evidence source ID and local anchor: SRC-1: `src/ingest.rs`
Claim IDs or none: EPI-CLM-1
Mismatch marker or none: none
Gap/limit: Adapter internals not fully reread; no observed source-fidelity trace

Route ID: RTE-3
Route function: content transformation
Architectural status: implemented
Object/candidate ID: OBJ-2, EPI-OBJ-1
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Rules-generated name, home-city or preference statement
Evaluator/condition and domain: Fixed regex/template extraction from user-role events
Activation and timing: Rules mode within selected batch; no observed operation
Possible or observed result: Proposal or quarantine
Implemented force: Candidate creation, not verified truth
Epistemic authority and scope: Some templating can reshape attributed content; actor and temporal interpretation are not independently checked
Operational authority: Creates a candidate for placement without LLM occurrence/lasting gate
Behavioral-authority path: Placement, Proposal structure, permissive candidate, current batch
Evidence source ID and local anchor: SRC-1: `src/consolidate.rs`
Claim IDs or none: EPI-CLM-1, EPI-CLM-2
Mismatch marker or none: none
Gap/limit: Remaining reshaping/entailed/conjectural classifications need concrete source-output pairs and checked interpretation; source truth unknown

Route ID: RTE-3
Route function: content transformation
Architectural status: implemented
Object/candidate ID: EPI-OBJ-1
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: LLM standing-fact statement and evidence selection
Evaluator/condition and domain: CMP-1, static durability prompt and selected event/known-entity context
Activation and timing: LLM mode; bounded parallel batches; no observed operation
Possible or observed result: Model JSON facts or request/parse error
Implemented force: Candidate generation only
Epistemic authority and scope: Not accepted ampliative knowledge; model reformulation may preserve, derive or extend input, but no observed pair decides which
Operational authority: Feeds proposed statements to deterministic admission
Behavioral-authority path: Checker, LlmFact JSON, advisory proposal, current batch
Evidence source ID and local anchor: SRC-1: `src/consolidate.rs`
Claim IDs or none: EPI-CLM-1, EPI-CLM-2
Mismatch marker or none: none
Gap/limit: No semantic comparison establishes preservation or non-entailment; no model answer oracle

Route ID: RTE-3
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-1
Content/update relation: no content change
Transition or check target: Cited quote occurrence, statement shape and model lasting flag
Evaluator/condition and domain: check_llm_fact and quote_found; ordered normalized fragments, statement bounds, field checks
Activation and timing: After response before placement; no observed operation
Possible or observed result: Proposal or rejection reason
Implemented force: Rejects malformed/unmatched candidates before placement
Epistemic authority and scope: Licenses occurrence of retained fragments in named event and usable structure only; lasting is model assertion, not measured future validity
Operational authority: Allows checked candidate to proceed; no statement entailment test
Behavioral-authority path: Placement, check Result, enforcing gate, current batch
Evidence source ID and local anchor: SRC-1: `src/consolidate.rs`
Claim IDs or none: EPI-CLM-2
Mismatch marker or none: EPI-M1: verbatim scope narrower than character-for-character prompt
Gap/limit: Runtime RTE-3 retained quote supports helper; sub-eight-character fragments discarded and formatting/case normalized

Route ID: RTE-3
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: EPI-OBJ-1, OBJ-1
Content/update relation: non-truth-apt policy/content update: assign eligibility and disposition
Transition or check target: Checked proposal, suppression ID and lexical overlap with existing statements
Evaluator/condition and domain: Code applies blocked set and restates_existing; accepted event marker set after check
Activation and timing: After shape/occurrence check, before publication; no observed operation
Possible or observed result: Drop, upsert active fact, or event marked accepted
Implemented force: Rejects placement by IDs/overlap; marks selected statement Active
Epistemic authority and scope: Operational selection for durable memory; no evidence-consuming criterion checks statement truth or semantic entailment
Operational authority: Dropped candidates do not enter fact store; accepted-event count can include dropped proposal
Behavioral-authority path: Fact store/batch accounting, flags and IDs, enforcing placement, later invocations after publication
Evidence source ID and local anchor: SRC-1: `src/consolidate.rs`
Claim IDs or none: EPI-CLM-1, EPI-CLM-2
Mismatch marker or none: EPI-M2: restatement heuristic not semantic equivalence
Gap/limit: No accepted ampliative-claim route established by these structural/provenance checks

Route ID: RTE-3
Route function: retention
Architectural status: implemented
Object/candidate ID: OBJ-1
Content/update relation: no content change
Transition or check target: Selected fact, source link, index, checkpoint and dispositions
Evaluator/condition and domain: DomainValidator then publication CAS; see RTE-3
Activation and timing: Completed batch candidate; no observed operation
Possible or observed result: Published snapshot or validation/conflict/error
Implemented force: Snapshot publication; see RTE-3
Epistemic authority and scope: Retains statement and provenance as selected memory, without upgrading imported warrant
Operational authority: Allows subsequent readers to retrieve active facts and next batch to resume
Behavioral-authority path: Search/consolidation, Git snapshot, permissive later input, across invocations
Evidence source ID and local anchor: SRC-1: `src/consolidate.rs`
Claim IDs or none: EPI-CLM-1, EPI-CLM-3
Mismatch marker or none: none
Gap/limit: Not lifecycle integration of an epistemically accepted novel claim; operation unobserved

Route ID: RTE-2, RTE-3
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: OBJ-1
Content/update relation: no content change
Transition or check target: Candidate fact/entity/control structure and reference identity
Evaluator/condition and domain: Fact.validate and DomainValidator; repository structure, dates, known references
Activation and timing: Before branch publication on normal callers; no observed operation
Possible or observed result: Validation success or error
Implemented force: Candidate rejection; see RTE-2, RTE-3
Epistemic authority and scope: Structural consistency for named checked fields, not source truth, supersession rationale or semantic support
Operational authority: Allows valid candidate to reach branch CAS
Behavioral-authority path: Publisher, validator Result, enforcing gate, candidate publication
Evidence source ID and local anchor: SRC-1: `src/validate.rs`
Claim IDs or none: EPI-CLM-3
Mismatch marker or none: none
Gap/limit: Public library caller supplies Validator; default validator comment lists more guarantees than inspected body establishes

Route ID: RTE-2
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: OBJ-1
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller remember/correct statement
Evaluator/condition and domain: ChangeRequest, structural validation and target identity; caller supplies semantic decision
Activation and timing: Explicit CLI/tool change; no observed operation
Possible or observed result: New fact, supersession or error; see RTE-2
Implemented force: Enforces request/store constraints without internal human gate
Epistemic authority and scope: Unknown source warrant; correction records chosen replacement, not demonstrated falsity or truth
Operational authority: Updates future eligibility and can withhold old content
Behavioral-authority path: Search/read/consolidation, persisted statuses and controls, enforcing eligibility, across invocations
Evidence source ID and local anchor: SRC-1: `src/change.rs`
Claim IDs or none: EPI-CLM-1, EPI-CLM-3
Mismatch marker or none: none
Gap/limit: Incoming statement does not share model evidence check; source support supplied by caller is not internally semantically verified

Route ID: RTE-2
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: OBJ-1
Content/update relation: non-truth-apt policy/content update: retract and suppress caller-targeted fact
Transition or check target: Caller-selected target fact
Evaluator/condition and domain: Request shape, target existence and publication validation; caller chooses withdrawal
Activation and timing: Explicit forget before publication; no observed operation
Possible or observed result: Retraction and suppression or error; see RTE-2
Implemented force: Enforces future eligibility and blocks reinsertion by ID
Epistemic authority and scope: None for falsity; records caller's withdrawal policy
Operational authority: Withholds target from subsequent current reads and extraction
Behavioral-authority path: Search/read/consolidation, status and controls, enforcing eligibility, across invocations
Evidence source ID and local anchor: SRC-1: `src/change.rs`
Claim IDs or none: EPI-CLM-1
Mismatch marker or none: none
Gap/limit: Does not erase raw source/history; see RTE-6 for distinct erasure protocol

Route ID: RTE-2
Route function: retention
Architectural status: implemented
Object/candidate ID: OBJ-1
Content/update relation: no content change
Transition or check target: Admitted fact/control change and receipt
Evaluator/condition and domain: Publication/recovery logic; see RTE-2
Activation and timing: After validated request; replay shortcut may return earlier; no observed operation
Possible or observed result: Snapshot or replay response
Implemented force: Git publication/replay acknowledgment; see RTE-2
Epistemic authority and scope: CAS licenses base identity, not factual warrant or universal payload-checked replay
Operational authority: Makes selected change durable for later consumers
Behavioral-authority path: Same-root readers, Git branch/receipt, permissive read, across invocations
Evidence source ID and local anchor: SRC-1: `src/repo.rs`
Claim IDs or none: EPI-CLM-3
Mismatch marker or none: EPI-M3: alternate operation replay does not compare digest
Gap/limit: Runtime RTE-2 retained passages delimit shortcut; journal/export/task mutations use other protocols

Route ID: RTE-3
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: OBJ-1
Content/update relation: non-truth-apt policy/content update: supersede outdated file-only facts
Transition or check target: Active facts sourced exclusively from prior versions of newly seen memory files
Evaluator/condition and domain: Source-event path/hash lineage; retire_outdated_file_facts
Activation and timing: On consolidation of new file version; no observed operation
Possible or observed result: Old source-only facts become Superseded unless refreshed by extraction
Implemented force: Future eligibility removal
Epistemic authority and scope: Licenses outdated source lineage, not independent falsity or endorsement of replacement
Operational authority: Blocks old fact in later current-context retrieval
Behavioral-authority path: Eligibility readers, Fact.status, enforcing filter, later invocations
Evidence source ID and local anchor: SRC-1: `src/consolidate.rs`
Claim IDs or none: EPI-CLM-2
Mismatch marker or none: none
Gap/limit: Failure to re-extract can withdraw still-true content; no observed recall/freshness result

Route ID: RTE-4
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-2, OBJ-1
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Whether active facts restate each other
Evaluator/condition and domain: Code sorts longer statements first, compares content-word Jaccard/containment within entity/preference family
Activation and timing: Explicit tidy, before optional apply; no observed operation
Possible or observed result: Duplicate Finding with kept ID
Implemented force: Advisory finding until apply
Epistemic authority and scope: Overlap judgment only; removed negation/modality prevents an equivalence guarantee
Operational authority: Proposes withdrawal of shorter matched fact
Behavioral-authority path: Operator/apply branch, Finding, advisory diagnosis, current invocation
Evidence source ID and local anchor: SRC-1: `src/tidy.rs`
Claim IDs or none: EPI-CLM-2
Mismatch marker or none: EPI-M2: lexical similarity can disregard negation
Gap/limit: Diagnostic proposition may be valid or ampliative; no observed pair establishes semantics

Route ID: RTE-4
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-2, OBJ-1
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Whether unflagged active fact is only session-specific
Evaluator/condition and domain: CMP-1 configuration through chat_json plus JUDGE_PROMPT, not deterministic patterns
Activation and timing: When LlmConfig exists; batches of up to 60, otherwise skipped; no observed operation
Possible or observed result: session_only IDs mapped back to live facts
Implemented force: Advisory finding until apply
Epistemic authority and scope: Model judgment under durability prompt; no source quote, ground truth or external answer oracle supplied
Operational authority: Proposes withdrawal while leaving uncertain facts out by prompt policy
Behavioral-authority path: Operator/apply branch, returned IDs/Finding, advisory diagnosis, current invocation
Evidence source ID and local anchor: SRC-1: `src/tidy.rs`
Claim IDs or none: EPI-CLM-2
Mismatch marker or none: EPI-M4: supplied RTE-4 describes this branch as deterministic
Gap/limit: Runtime record needs correction/split; provider reasoning and classification quality uninspected

Route ID: RTE-4
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: EPI-OBJ-2, OBJ-1
Content/update relation: non-truth-apt policy/content update: retract/suppress flagged facts
Transition or check target: Tidy findings after keep exclusions
Evaluator/condition and domain: Operator apply/keep choice, code forget_all and validator/CAS
Activation and timing: Only --apply and nonempty remaining findings; no observed operation
Possible or observed result: Retraction, soft suppression and reasons in Git or failure
Implemented force: Enforcing withdrawal after operator opt-in
Epistemic authority and scope: Acceptance for operational cleanup under duplicate/durability criteria; not evidence that removed statements were false
Operational authority: Suppresses later retrieval/re-extraction; retained history remains
Behavioral-authority path: Search/consolidation, status/control records, enforcing eligibility, across invocations
Evidence source ID and local anchor: SRC-1: `src/tidy.rs`
Claim IDs or none: EPI-CLM-2
Mismatch marker or none: none
Gap/limit: No utility measurement, automatic method revision or semantic undo; see RTE-4 for recovery

Route ID: RTE-1
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: OBJ-1, OBJ-2
Content/update relation: no content change
Transition or check target: Which curated/raw statements enter query result
Evaluator/condition and domain: Eligibility, lexical ranking, optional CMP-2/CMP-3 relevance scoring/fallback; see RTE-1
Activation and timing: Explicit query; reranker conditional on configuration/availability; no observed operation
Possible or observed result: Ordered bounded hits with ranker/judged flags
Implemented force: Ranking rather than truth verification
Epistemic authority and scope: Relevance to query within scoring domain; raw and curated channels have different admission histories
Operational authority: Permits returned content to reach host; no target-enforced obedience
Behavioral-authority path: Host, tool/search result, ranking and advisory content, current query; see BAP-1
Evidence source ID and local anchor: SRC-1: `src/search/rerank.rs`
Claim IDs or none: EPI-CLM-1
Mismatch marker or none: none
Gap/limit: Relevant nonempty hits need not be model judged; host activation and benefit unobserved

Route ID: RTE-5, RTE-8
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: OBJ-3, OBJ-1
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Selected statements rendered into context/project block
Evaluator/condition and domain: Hook/writeback selection and rendering; see RTE-5, RTE-8
Activation and timing: Host hook or operator writeback; no observed operation
Possible or observed result: Context output or persistent managed block
Implemented force: Advisory content and standing guidance; see BAP-1
Epistemic authority and scope: No additional truth license; source/status history is not a new check
Operational authority: Can guide future host behavior; stale prior export lacks automatic retraction
Behavioral-authority path: External host, additionalContext/project file, advisory instruction, prompt or later sessions; see BAP-1
Evidence source ID and local anchor: SRC-1: `src/hook.rs`
Claim IDs or none: EPI-CLM-1
Mismatch marker or none: none
Gap/limit: No actual host consumption or enforcement observed; static setup skill is not accumulated memory

Route ID: RTE-6
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: OBJ-1, OBJ-2
Content/update relation: non-truth-apt policy/content update: erase retained source-linked content
Transition or check target: Caller-targeted fact/entity and linked journal/history
Evaluator/condition and domain: ID/control checks and staged erasure; see RTE-6
Activation and timing: Explicit erase request; no observed operation
Possible or observed result: Current deletion followed by journal/history/intents scrub, or partial error
Implemented force: Removal within target-controlled stores
Epistemic authority and scope: Administrative withdrawal; does not establish original falsity
Operational authority: Prevents future in-boundary access when stages complete
Behavioral-authority path: Store readers, deletions/controls/redaction, enforcing local removal, future invocations
Evidence source ID and local anchor: SRC-1: `src/erasure.rs`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No all-substrate transaction; prior exports, host originals and provider copies outside scope

Route ID: RTE-11
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-3
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Returned hit IDs and strings against caller rubric
Evaluator/condition and domain: Deterministic membership/substrings, reference outcomes supplied externally; see RTE-11
Activation and timing: Explicit evaluation, lexical versus available judged reranking; no observed operation
Possible or observed result: Passed/recall/rank measures per rubric case
Implemented force: Report only, no production selection gate
Epistemic authority and scope: Derives pass under rubric predicates and given hits; does not establish source truth, general retrieval quality or component effect
Operational authority: Permits operator interpretation; no automatic policy/model admission
Behavioral-authority path: Operator, printed report, advisory measurement, current invocation
Evidence source ID and local anchor: SRC-1: `src/evaluation.rs`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Oracle correctness/independence uninspected; no observed scores or controlled causal comparison

Route ID: EPI-RTE-1
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-4
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Measured search invocation durations and printed duration summaries
Evaluator/condition and domain: Instant timer and deterministic min/median/p95 calculations; see EPI-RTE-1
Activation and timing: Explicit bench repetitions with optional reranking repetitions; no observed operation
Possible or observed result: Timing/hit-count/ranker report
Implemented force: Report only
Epistemic authority and scope: Licenses measured invocation duration under local workload if operated; no factual/semantic retrieval warrant
Operational authority: No automatic production change; operator may inspect
Behavioral-authority path: Operator, stdout measurement, advisory, current invocation
Evidence source ID and local anchor: SRC-1: `src/cli.rs`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No execution evidence, standardized environment or controlled experiment; Summary uses rounded sample-index quantiles, not interpolation; no timing observations or causal isolation

Route ID: RTE-7
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: OBJ-4
Content/update relation: non-truth-apt policy/content update: caller task append
Transition or check target: Task version and append fields
Evaluator/condition and domain: Version comparison under lock; see RTE-7
Activation and timing: Explicit task-update request; no observed operation
Possible or observed result: Task append or version-conflict response
Implemented force: Administrative mutation; see RTE-7
Epistemic authority and scope: Structure/version validity; no task-completion license
Operational authority: Changes later task reads
Behavioral-authority path: Task reader, task file/version, permissive available work, later invocations
Evidence source ID and local anchor: SRC-1: `src/ops.rs`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Task feasibility and task execution are outside the version check

Route ID: RTE-9
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: CMP-3
Content/update relation: non-truth-apt policy/content update: model-family selection
Transition or check target: Supported model-family availability
Evaluator/condition and domain: Supported-name parse and successful asset load; see RTE-9
Activation and timing: Explicit administrative request/environment override; no observed operation
Possible or observed result: Later model selection or load failure
Implemented force: Administrative mutation; see RTE-9
Epistemic authority and scope: Load validity; no improved-ranking license
Operational authority: Changes later ranker routing without evaluation-based successor admission
Behavioral-authority path: Local ranker, selected marker/environment, enforcing routing, later invocations
Evidence source ID and local anchor: SRC-1: `src/search/laya.rs`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No automatic performance-driven adaptation or quality gate

Supporting passages below supplement the supplied retained quotations in RTE-2, RTE-3 and RTE-11. They delimit the occurrence/shape gate, overlap disposition, and event-accounting result; they establish wired branches, not observed operation.

> let evidence = fact.evidence.trim();
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
> --- `src/consolidate.rs:914-927` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> fn place(&mut self, p: Proposal, event: &JournalEvent) {
>         let digest = hex(&Sha256::digest(
>             format!("{}|{}|{}", p.entity_id, p.predicate, p.statement.to_lowercase()).as_bytes(),
>         ));
>         let fact_id = format!("fact_{}", &digest[..12]);
>         if self.blocked.contains(&fact_id) || self.restates_existing(&p, &fact_id) {
>             if std::env::var("MEM_CONSOLIDATE_VERBOSE").is_ok_and(|v| v == "1") {
>                 eprintln!("[consolidate] dropped (forgotten, erased, or restates an existing fact): {}", p.statement);
>             }
>             return;
>         }
>         let fact = Fact {
>             id: fact_id,
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
> --- `src/consolidate.rs:365-392` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> .filter(|f| f.status == FactStatus::Active && f.id != fact_id)
>             .any(|f| {
>                 let other = content_words(&f.statement);
>                 jaccard(&words, &other) >= NEAR_DUPLICATE || contained(&words, &other)
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
> ];
> --- `src/consolidate.rs:440-456` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> }
>             let event = by_seq[&fact.event_ref];
>             match check_llm_fact(&fact, event, &ex.entities) {
>                 Ok(proposal) => {
>                     ex.place(proposal, event);
>                     ex.accepted.insert(event.seq);
>                 }
> --- `src/consolidate.rs:684-690` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> pub fn validate(&self) -> Result<()> {
>         if self.id.is_empty() {
>             return Err(Error::InvalidFact("fact id required".into()));
>         }
>         if self.predicate.is_empty() {
>             return Err(Error::InvalidFact(format!("{}: predicate required", self.id)));
>         }
>         if self.statement.is_empty() {
>             return Err(Error::InvalidFact(format!(
>                 "{}: statement required",
>                 self.id
>             )));
>         }
>         if let (Some(from), Some(to)) = (self.valid_from, self.valid_to) {
>             if from > to {
>                 return Err(Error::InvalidFact(format!(
>                     "{}: valid_from after valid_to",
>                     self.id
>                 )));
>             }
>         }
>         Ok(())
>     }
>
>     /// True if the fact is eligible for current-context retrieval at `now`.
> --- `src/fact.rs:39-63` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> // Session-only: ask the model about everything not already flagged.
>     let cfg = LlmConfig::from_env();
>     if let Some(cfg) = &cfg {
>         let remaining: Vec<&(String, String, String)> =
>             live.iter().filter(|(_, id, _)| !flagged.contains(id)).collect();
>         for batch in remaining.chunks(JUDGE_BATCH) {
>             let facts: Vec<serde_json::Value> = batch
>                 .iter()
>                 .map(|(_, id, s)| serde_json::json!({"id": id, "statement": s}))
>                 .collect();
>             let judged: Judgement = chat_json(cfg, JUDGE_PROMPT, &serde_json::json!({"facts": facts}).to_string())?;
>             let ids: BTreeSet<&str> = judged.session_only.iter().map(String::as_str).collect();
>             for (entity_id, fact_id, statement) in batch {
>                 if ids.contains(fact_id.as_str()) && flagged.insert(fact_id.clone()) {
>                     findings.push(Finding {
>                         fact_id: fact_id.clone(),
>                         entity_id: entity_id.clone(),
>                         statement: statement.clone(),
>                         kind: "session_only",
>                         duplicate_of: None,
>                     });
>                 }
>             }
>         }
>     }
>
>     findings.retain(|f| !keep.contains(&f.fact_id));
>     let mut report = TidyReport {
>         facts_checked: live.len(),
>         findings,
>         checked_session_only: cfg.is_some(),
>         applied_at: None,
>     };
>     if apply && !report.findings.is_empty() {
> --- `src/tidy.rs:125-158` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| EPI-CLM-1 | Curated sourced facts and later agent access; see EPI-CLM-1 | SRC-2: `README.md`, doctrine/design | Declared | RTE-10, RTE-3, RTE-1, RTE-5, RTE-8 | None supplied | None; excluded host loop | Candidate curation, source links, persistence and delivery are wired | Imported source warrant, extraction fidelity and host benefit unknown; curation is not truth verification |
| EPI-CLM-2 | Lasting selection, verbatim evidence, duplicate removal and file supersession; see EPI-CLM-2 | SRC-2: `README.md`, doctrine/design | Prompt/README specify selection | RTE-3, RTE-4 | None supplied | None; static criteria and opaque model judgments | Model flag and normalized quote occurrence gate, heuristic deduplication and lineage retirement wired | EPI-M1: weaker than character-for-character prompt; EPI-M2: lexical restatement lacks semantic guarantee; future truth unmeasured |
| EPI-CLM-3 | Validated changes and CAS publication; see EPI-CLM-3 | SRC-2: `README.md`, doctrine/design | Publication promise explicit | RTE-2, RTE-3 | None supplied | None; depends on Git and selected validator | Validator-before-CAS branch update supported on normal publisher paths | EPI-M3: operation replay can bypass digest comparison; semantic truth and other storage stages outside guarantee |

EPI-M4 is a supplied-record discrepancy rather than a target public-claim mismatch: RTE-4 calls session-only findings deterministic, while direct `src/tidy.rs` inspection wires `chat_json` using LlmConfig. The same model configuration represented by CMP-1 is reused, under a distinct judge prompt. This member flags the affected check and leaves the canonical record unchanged.

## Bounded conclusion

`mem` acquires local source assertions into OBJ-2 and produces selected standing statements through RTE-3. Imported warrant is unknown. Rules and model outputs lack a demonstrated semantic preservation check; occurrence proves only a quoted fragment's relationship to the event. No accepted ampliative claim is established by these checks. RTE-2 likewise admits caller-supplied corrections through structural checks, without an internal truth evaluator.

RTE-3 and RTE-2 retain statements, source links and state in OBJ-1 for later retrieval. `Active`, a successful publication and an event's `accepted` marker license operational availability under different criteria; none independently warrants truth. Because placement can drop a proposal before the event is marked accepted, the event count is not a count of epistemically accepted or even inserted statements. Connecting a selected candidate to a source and an index is retention/organization before epistemic acceptance, not lifecycle integration of accepted novel knowledge.

RTE-3 occurrence/shape checks have an enforcing pre-placement effect. RTE-2 and RTE-3 structural checks and CAS have an enforcing publication effect. RTE-4 duplicate and model-durability judgments are advisory until the operator chooses apply; keep exclusions veto individual withdrawals. The applied result changes status and controls, suppressing future retrieval and re-extraction. This is acceptance for operational cleanup under named heuristics, not verification that a proposition is false. Negation removal bounds duplicate equivalence; unobserved model judgments bound the durability assessment.

RTE-3 source-lineage supersession and RTE-6 erasure withdraw availability without establishing falsity. RTE-1 ranks material for queries; RTE-5 and RTE-8 deliver rendered memory through BAP-1 to excluded hosts. Their force is advisory to those hosts, and no host activation or benefit is demonstrated. Previously exported text has no automatic cross-host retraction guarantee.

RTE-11 can derive rubric satisfaction from explicit reference IDs/strings and retrieved hits. It neither checks every statement's truth nor gates production successor selection. EPI-RTE-1 can measure invocation time, with no implemented retention/adaptation loop. RTE-7 and RTE-9 change administrative state directly, without a truth-apt learning route or quality gate. No supplied observations or experiments establish improved future action, model accuracy, transfer, reliable cleanup, or causal retrieval benefit. These limits concern the named routes and evidence boundary; opaque provider computation and uninspected branches do not support universal absence conclusions.

## Shared records

### Operative objects

#### EPI-OBJ-1 — Model/rules proposed standing fact

Source-native identity: `Proposal` and `LlmFact` before `Extraction::place`. Representational form: Rust structs/model JSON holding statement, predicate/entity, evidence, event reference and model lasting flag. Storage substrate: invocation memory/model response, not a durable candidate archive. Evidence: SRC-1: `src/consolidate.rs`. Closest supplied IDs: OBJ-1 stored snapshot and OBJ-2 source event; distinct identity is the transient statement awaiting checks/placement. RTE-3 carries its processing, so no duplicate route is declared. Minimum support: the occurrence/shape and placement quotations in the ledger show candidate-to-fact transition.

#### EPI-OBJ-2 — Tidy findings

Source-native identity: `Finding`, `Judgement.session_only`, `TidyReport`. Representational form: typed duplicate/session-only diagnosis, fact IDs and optional kept counterpart. Storage substrate: invocation memory/returned report; applied suppression reason persists separately in OBJ-1. Evidence: SRC-1: `src/tidy.rs`. Closest supplied IDs: OBJ-1 assessed facts and RTE-4 processing; distinct identity is the intermediate withdrawal proposal/report, not fact content or its control record. Minimum support: tidy_judge passage in ledger. Code and model contributions are separate there; operator apply/keep choices determine operational force.

#### EPI-OBJ-3 — Retrieval rubric and evaluation result

Source-native identity: `Rubric`, `RubricCase`, `CaseScore`, `RunReport`, `EvaluationReport`. Representational form: JSON reference IDs/string conditions and structured pass/recall/rank results. Storage substrate: operator-provided rubric file and current-invocation report/stdout. Evidence: SRC-1: `src/evaluation.rs`. Closest supplied IDs: RTE-11 evaluator and OBJ-1 searched facts; distinct identity is reference criteria and report, not stored memory. Minimum support: supplied RTE-11 retained evaluation passage. Reference outcomes are supplied by rubric author; neither source truth nor held-out independence is established.

#### EPI-OBJ-4 — Benchmark timing result

Source-native identity: `cmd_bench` duration vectors and printed min/median/p95/ranker/hits rows. Representational form: numerical measurement report. Storage substrate: invocation vectors and stdout. Evidence: SRC-1: `src/cli.rs`. Closest supplied ID: RTE-11 retrieval evaluation; distinct target is elapsed time rather than expected-content correctness. No supplied object declares this report. Minimum support: EPI-RTE-1 retained passage.

### Routes

#### EPI-RTE-1 — Measure retrieval invocation time

Endpoints/progression: explicit `bench` query/options → repeated `combined_search` with lexical or rerank option → `Instant` elapsed samples → printed duration summaries. Owner: operator chooses queries/repetitions; Rust times and renders. Context/state/action effects: temporary measurements, ordinary search/model calls; no production memory or policy update. Implementation conclusion status: wired. Operation conclusion status: uninspected, no supplied benchmark result. Guarantee strength: no claimed guarantee.

Immediate return: printed duration rows, last ranker/hit count or search error. Later read-back: inapplicable, benchmark retains no managed result for a later consumer. Delegated visibility: configured ranker receives ordinary candidate text through RTE-1; no delegated agents. Selection predicate: explicit queries/project/limit and repetition counts. Invalidation/expiry: inapplicable for unretained report. Activation/effect: measurements/report wired; no implemented consumer changes production from them. Evidence limits: no executed timing, controlled environment or causal attribution. Roles: operator defines workload; program produces measurements; no automatic successor selection or vetoed candidate admission. Answer oracle: no reference answer; monotonic timer measures elapsed interval. Operating mode: explicit bounded benchmark. Improvement trigger: operator request, with no automatic improvement loop. Admission/recovery fields: inapplicable, report-producing route does not admit system changes. Closest supplied ID: RTE-11, which assesses retrieved content using a rubric; this route has a different target/evaluator and no content oracle. Evidence: SRC-1: `src/cli.rs`.

> let time = |query: &str, rerank: bool, runs: usize| -> Result<(Vec<f64>, &'static str, usize)> {
>         let mut ms = Vec::with_capacity(runs);
>         let mut ranker = "lexical";
>         let mut hits = 0;
>         for _ in 0..runs.max(1) {
>             let start = Instant::now();
>             let found = crate::ops::combined_search(
>                 &cli.root,
>                 &crate::ops::SearchParams { query, limit, rerank, project, ..Default::default() },
>             )?;
>             ms.push(start.elapsed().as_secs_f64() * 1000.0);
>             ranker = found.ranker;
>             hits = found.hits.len();
>         }
>         Ok((ms, ranker, hits))
>     };
>
>     println!("memory_root: {}", cli.root.display());
>     println!("{:<40} {:>9} {:>9} {:>9}  {:<8} hits", "query", "min ms", "median", "p95", "ranker");
> --- `src/cli.rs:2508-2526` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> fn print_bench_row(label: &str, ms: &[f64], ranker: &str, hits: usize) {
>     let mut sorted = ms.to_vec();
>     sorted.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
>     let pick = |q: f64| sorted[((sorted.len() as f64 - 1.0) * q).round() as usize];
>     let label: String = label.chars().take(40).collect();
>     if sorted.is_empty() {
>         return;
>     }
>     println!(
>         "{:<40} {:>9.1} {:>9.1} {:>9.1}  {:<8} {}",
>         label,
>         sorted[0],
>         pick(0.5),
>         pick(0.95),
>         ranker,
>         if ranker.is_empty() { String::new() } else { hits.to_string() }
>     );
> }
> --- `src/cli.rs:2546-2563` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Claims

#### EPI-CLM-1 — Curated sourced memory for coding agents

Claimed operation: read earlier conversations/project memory files, turn them into curated sourced Git facts, expose search/read/change and project writeback. Source: SRC-2: `README.md`, doctrine/design. Conclusion status: claimed. Closest supplied IDs: RTE-10, RTE-3, RTE-1, RTE-8 implement portions; runtime Claims contains none, so no supplied claim counterpart. Neither curation nor source attribution is itself a truth guarantee.

> `mem` reads the conversations you have already had with Claude Code, Codex, and OpenCode, plus your `AGENTS.md`/`CLAUDE.md`/`README.md` files, and turns them into a small set of curated, sourced facts stored in a plain Git repository. Agents search that memory (facts and raw sessions together), read it over MCP, change it through a validated path, and get it written back into each project's `AGENTS.md`.
> --- `README.md:5-5` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-CLM-2 — Durable selection and source-backed consolidation

Claimed operation: keep lasting facts with in-event quoted evidence, remove restatements, supersede old file-only facts and publish batch state together. Source: SRC-2: `README.md`, doctrine/design. Conclusion status: claimed. Closest supplied IDs: RTE-3 and RTE-4 implement parts; no supplied claim counterpart. Assess quoted-fragment occurrence, lasting classification, semantic equivalence and lineage separately. The prompt's character-for-character demand is stronger than the implemented normalization/fragment gate; the README itself already qualifies ignored Markdown and ellipses.

> - **Consolidation** reads events after its checkpoint in batches. The LLM extractor sees only the user's own words and memory files (it skips assistant turns, subagent transcripts, conversation-compaction summaries, and text the tools inject, such as `<system-reminder>` blocks carrying CLAUDE.md). It keeps only facts that pass a "still true for a new teammate next month" test (requests like "move the button 4px" and "User is running X" are tasks and session activity, not facts), and keeps a fact only if its evidence quote appears verbatim in the cited event (quoted fragments joined by an ellipsis must each appear, in order; Markdown marks are ignored). Memory files are read whole, in chunks. Facts that restate an existing one (in the same project or the user's preferences) are dropped. When AGENTS.md or CLAUDE.md changes, facts that came only from its old version and were not extracted again are marked superseded. Each batch is published as one Git commit with the changed entities, `INDEX.md`, the checkpoint, and a disposition file listing what happened to each event.
> --- `README.md:57-57` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### EPI-CLM-3 — Validated publication with concurrency protection

Claimed operation: models do not write memory directly; request/consolidation changes are validated and published by branch compare-and-swap, preventing concurrent overwrite. Source: SRC-2: `README.md`, doctrine/design. Conclusion status: claimed. Closest supplied IDs: RTE-2, RTE-3; no supplied claim counterpart. Supported scope is normal candidate branch publication under Git's contract, not universal semantic validation, all-substrate atomicity or alternate-path digest-checked replay.

> - The model never writes memory directly: changes go through `memory_request_change` or consolidation, are validated, and publish with compare-and-swap on the `memory` branch, so a concurrent writer can never overwrite another's commit.
> --- `README.md:182-182` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`
