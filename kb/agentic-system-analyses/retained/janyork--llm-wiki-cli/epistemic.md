---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of llm-wiki-cli: source-linked Wiki admission, reference consumption, temporal feedback and optional assessed learning."
run-id: AAS-2026-11-08-llm-wiki-cli-135ef8fbe608-01
reviewed-boundary: e1be6ab30e83947e4b0dba97ba910acfe3bd9821
---

# llm-wiki-cli epistemic report

## Source-and-claim boundary

This report asks which content LWC licenses for reliance, which checks have operative consumers, and where storage or procedural verification stops short of semantic acceptance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identities and layers: see [Source register](boundary.md#source-register). All direct reads below are SRC-1 at the reviewed commit; none is a target execution. The analysis includes the shipped agent policies, not just the Rust store. The host's inference and provider parameters remain outside accessible implementation: see [RT-CMP-host-model](runtime.md#rt-cmp-host-model).

The consequential knowledge claim is [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory). Its verified-milestone prescription must be compared with the actual admission paths, not inferred from the word Wiki. Source text and saved answers can carry truth-apt propositions; an arbitrary stored body need not. No concrete host-produced synthesis or source-to-answer trace was supplied. Semantic preservation, entailment, non-entailment and exercised acceptance of such a synthesis therefore remain undetermined. This is not evidence that agents cannot synthesize or verify.

| Entry point or operation | Source path, SRC-1 | Coverage and consequence |
| --- | --- | --- |
| CLI dispatch and exposed operations | `src/cli/dispatch.rs` | Direct operation inventory searched, including ingest, remember/memory, graph relation retraction, weights, lint, plans, discussion, optional runtimes and archive/sync. Detailed paths below distinguish inspection from inventory. |
| Page write/show; draft commit/rollback | `src/store/content_search.rs`, `src/changeset.rs` | Supplied findings: [RT-RTE-page-write](runtime.md#rt-rte-page-write), [RT-RTE-changeset-commit](runtime.md#rt-rte-changeset-commit). Direct-live and override alternatives defeat a universal lint gate. |
| Ingest completion/failure/retry | `src/store/graph_ingest.rs` | Supplied [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete); no semantic acceptance inferred from completion. |
| Lint results | `src/store/materialize.rs`, `src/store/types.rs` | Direct reads of result construction and selected SQL predicates: [EPI-RTE-lint-check](#epi-rte-lint-check). Not a complete audit of all lint rules. |
| Recall, hooks, pi and core MCP writes | `src/mcp.rs`, `src/agent.rs`, `integrations/pi-lwc/extensions/lwc.js` | Supplied [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-core-command](runtime.md#rt-rte-core-command). No new host-parity claim. |
| Milestone verification and retrieval checks | `skills/using-lwc/references/active-memory.md` | Direct full read: [EPI-RTE-milestone-review](#epi-rte-milestone-review). Doctrine, not an observed review trace. |
| Temporal remember/recall/feedback | `src/store/temporal_memory.rs` | Direct remember, recall and feedback bodies: [EPI-RTE-temporal-feedback](#epi-rte-temporal-feedback). Retention helper internals and hint consumers not fully inspected; no complete temporal curation verdict. |
| Retrieval weight mutation | `src/store/graph_ingest.rs` | Direct weight-set read shows caller reason/provenance and symbolic upsert. Other weight feedback and reranking algorithms not traced end to end; prevents complete ranking-authority assessment. |
| Tutor turns and Soul | `src/learning/tutor.rs`, `skills/using-tutor/SKILL.md` | Supplied [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn), [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish). |
| Practice verify, grade, override and mistakes | `src/learning/practice.rs`, `skills/using-practice/SKILL.md` | Direct selected functions and full skill: [EPI-RTE-practice-verify](#epi-rte-practice-verify), [EPI-RTE-practice-grade](#epi-rte-practice-grade). Scheduling entry was read, not the complete scheduler/queue; no learning-benefit conclusion. |
| Team and recovery, work, runtime admission | `src/replica/engine.rs`, `src/team/hub.rs`, `src/work/runner.rs`, `src/learning_runtime.rs` | Supplied [RT-RTE-team-sync](runtime.md#rt-rte-team-sync), [RT-RTE-work-runner](runtime.md#rt-rte-work-runner), [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install). These constrain lineage and operational admission, not source truth. |
| Other material included routes | `src/learning/book.rs`, `src/store/discussion.rs`, `src/store/plan.rs` | Detailed Book transformations, discussion convergence, plan evidence disposition and their downstream consumers remain uninspected here; no system-complete negative about evidence-consuming acceptance, criticism or integration follows. |
| Import/merge, relation retraction, removal, readers and other host adapters | `src/cli/dispatch.rs`, `src/view/mod.rs` | Dispatch inventory and supplied runtime account only. Detailed withdrawal propagation, merge fidelity, browser rendering and other host delivery not established; prevents complete lineage, rejection and consumer coverage. |
| Evaluations | `benchmarks/README.md` | Boundary's reported-operation scope only; no direct benchmark-result assessment. No end-to-end run or causal experiment supplied. |

Missing evidence is local: host traces prevent conclusions about actual semantic checking and later dependence; source-to-candidate pairs prevent classifying generated content as reshaping, entailed derivation or ampliative conjecture; provider internals prevent weight-learning or version-fixity conclusions; uninspected included operations prevent a system-wide absence claim. No supplied record needs supersession for the bounded findings below.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-RTE-page-write](runtime.md#rt-rte-page-write) | Caller-supplied page propositions and citations | see cited record | SRC-1, `src/store/content_search.rs` | Route identifies the object; no new duplicate page declaration. No concrete proposition verified here. |
| [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete) | Imported source content, source summary, integration-page assertions | see cited record | SRC-1, `src/store/graph_ingest.rs` | Citation/kind counts do not establish summary fidelity or integration after acceptance. |
| [EPI-OBJ-memory-events](#epi-obj-memory-events) | Temporal fragments, changes and evidence supplied by caller | see record | SRC-1, `src/store/temporal_memory.rs` | Content warrant unknown; latest-known is not live-verified. |
| [EPI-OBJ-practice-items](#epi-obj-practice-items) | Item prompts, expected answers, rubrics and source refs | see record | SRC-1, `src/learning/practice.rs` | Reference identity checks do not prove expected answers true. |
| [EPI-OBJ-practice-grades](#epi-obj-practice-grades) | Exact-match result or caller judgment of a response | see record | SRC-1, `src/learning/practice.rs` | Numerical score and accepted state have route-specific scope. |
| [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish) | Stable learner descriptions can be truth-apt; teaching preferences can be non-truth-apt | see cited record | SRC-1, `src/learning/tutor.rs` | Distinct content functions retained; no inspected concrete revision. |
| [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) | Selected Wiki propositions in reference envelope; readiness metadata | see cited record | SRC-1, `src/agent.rs` | Budgeted delivery; not a warrant elevation. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Not determinable within inaccessible parameters | see cited record | SRC-1, `README.md` | Host/provider internals uninspected. |

## Authority-route ledger

The ledger is a sparse overlay. For fields owned by cited records, “see” delegates the detailed finding; the architectural status and content relation here are this report's assessment. Several rows cite one container route to separate checking, disposition, retention and consumption. No row equates retention with lifecycle integration.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-page-write](runtime.md#rt-rte-page-write) | retention | implemented | see route | truth-apt transformation: acquisition/import | Supplied page and citation set | see route | see route | see route | see route | Source warrant unknown; stored attribution is not endorsement | see route | see route and [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1, `src/store/content_search.rs` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | no universal semantic gate | Caller text may contain non-truth-apt parts; no novel claim production established by persistence. |
| [EPI-RTE-milestone-review](#epi-rte-milestone-review) | check/evidence production | doctrine only | page candidate | truth-apt transformation: indeterminate | Mutable claims, citations, retrieval fitness | see record | see record | see record | No autonomous enforcement established | Prescribed source-relative verification and top-five retrieval, not proof of truth | see record | see record | SRC-1, `skills/using-lwc/references/active-memory.md` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | requested versus exercised | Host reasoning unavailable; neither non-entailment nor entailment demonstrated. |
| [EPI-RTE-milestone-review](#epi-rte-milestone-review) | disposition/acceptance | doctrine only | reviewed page | no content change | Capture at verified milestone | see record | see record | see record | Policy | Intended reusable decision/runbook or synthesis; evidence-consuming host judgment prescribed, not observed | see record | see record | SRC-1, `skills/using-lwc/references/active-memory.md` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | no observed acceptance | The policy is consequential but is not a Rust semantic evaluator. |
| [EPI-RTE-lint-check](#epi-rte-lint-check) | check/evidence production | implemented | page structure and references | no content change | Structural Wiki issues | see record | see record | see record | Diagnostic outside commit | Presence of citations/provenance and index/link structure within checked predicates only | see record | see record | SRC-1, `src/store/types.rs` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | none | Explicit provenance can satisfy the uncited-page predicate without independently verified evidence. |
| [RT-RTE-changeset-commit](runtime.md#rt-rte-changeset-commit) | disposition/acceptance | implemented | draft | no content change | Publishability under conflicts/lint | see route | see route | see route | see route | Structural admission, not accepted semantic truth | see route | see route | SRC-1, `src/changeset.rs` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | direct-live and override alternatives | Override is not semantic warrant. |
| [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete) | disposition/acceptance | implemented | source-linked pages | no content change | Generating job completeness | see route | see route | see route | see route | Structural completion only | see route | see route | SRC-1, `src/store/graph_ingest.rs` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | integration label versus lifecycle integration | No accepted ampliative claim established by counts; pages already persist. |
| [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) | operational admission/selection/consumption | implemented | saved pages | truth-apt transformation: non-ampliative reshaping | Reference selection and bounded text | see routes | see routes | see routes | Ranking and bounded supply | No new truth license; truncation can remove qualifications | see routes | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1, `src/mcp.rs`, `src/agent.rs` | [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | delivery is not reliance | Reshaping classifies selection/truncation mechanics, not semantic equivalence of shortened propositions. |
| [EPI-RTE-temporal-feedback](#epi-rte-temporal-feedback) | retention | implemented | [EPI-OBJ-memory-events](#epi-obj-memory-events) | truth-apt transformation: acquisition/import | Caller event and lineage relations | see record | see record | see record | Durable record subject to retention | Source warrant unknown | see record | see record | SRC-1, `src/store/temporal_memory.rs` | none | none | Supersedes/contradicts/resolves are submitted relations, not independently adjudicated facts. |
| [EPI-RTE-temporal-feedback](#epi-rte-temporal-feedback) | behavior/policy adaptation | implemented | event feedback | non-truth-apt policy/content update: usefulness signal changes ranking | Event retrieval priority | see record | see record | see record | Ranking | Usefulness is not truth or live verification | see record | see record | SRC-1, `src/store/temporal_memory.rs` | none | none | Improvement unmeasured; conflict flag is descriptive, not a rejection gate. |
| [EPI-RTE-practice-verify](#epi-rte-practice-verify) | check/evidence production | implemented | [EPI-OBJ-practice-items](#epi-obj-practice-items) | no content change | Revision, exact reread fields and source identity | see record | see record | see record | Enforcing prerequisite | Identity consistency; not semantic agreement with source | see record | see record | SRC-1, `src/learning/practice.rs` | none | source truth name exceeds semantic license | Host verification remains policy. |
| [EPI-RTE-practice-verify](#epi-rte-practice-verify) | disposition/acceptance | implemented | item revision | no content change | Draft to verified | see record | see record | see record | Enforcing state transition | Eligible item, not necessarily warranted answer | see record | see record | SRC-1, `src/learning/practice.rs` | none | none | Distinct from Wiki admission. |
| [EPI-RTE-practice-grade](#epi-rte-practice-grade) | check/evidence production | implemented | [EPI-OBJ-practice-grades](#epi-obj-practice-grades) | truth-apt transformation: entailed derivation | JSON equality to frozen objective answer | see record | see record | see record | Deterministic score | Exact match in JSON domain given stored answer/points; no source-truth proof | see record | see record | SRC-1, `src/learning/practice.rs` | none | none | The stored answer is an oracle for matching, not an infallible reference. |
| [EPI-RTE-practice-grade](#epi-rte-practice-grade) | disposition/acceptance | implemented | subjective grade | no content change | Submitted grade, rationale and confidence | see record | see record | see record | State and mistake-set update | Accepted label means confidence threshold after mechanical checks; model rationale is not independent evidence | see record | see record | SRC-1, `src/learning/practice.rs` | none | accepted label bounded | No independent semantic rubric application demonstrated. |
| [EPI-RTE-practice-grade](#epi-rte-practice-grade) | retention | implemented | grade/history and mistake membership | truth-apt transformation: acquisition/import | Caller subjective judgment or override | see record | see record | see record | Durable records | Warrant of imported judgment unknown | see record | see record | SRC-1, `src/learning/practice.rs` | none | none | Override changes current grade and history; does not prove earlier judgment wrong. |
| [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish) | behavior/policy adaptation | implemented | Soul guidance | non-truth-apt policy/content update: caller replaces teaching guidance | Publication checks | see route | see route | see route | see route | Preference license distinct from factual learner diagnosis | see route | see [RT-BAP-soul-guidance](runtime.md#rt-bap-soul-guidance) | SRC-1, `src/learning/tutor.rs` | none | submitted approval is not authenticated consent | Truth-apt descriptions within Soul are imported with unknown warrant; no inspected specific revision. |
| [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) | lineage/freshness/recovery | implemented | replicated candidate state | truth-apt transformation: indeterminate | Publication authorization, head/digest and resolution | see route | see route | see route | see route | Authorized lineage is not truth; merge fidelity unresolved | see route | see route | SRC-1, `src/team/hub.rs`, `src/replica/engine.rs` | none | none | Semantic conflicts delegated to caller; complete transformations uninspected. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) | see record | SRC-1, `README.md`, `skills/using-lwc/SKILL.md`; doctrine/design | see record; [EPI-RTE-milestone-review](#epi-rte-milestone-review) | [RT-RTE-page-write](runtime.md#rt-rte-page-write), [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [EPI-RTE-lint-check](#epi-rte-lint-check) | None supplied for a semantic write/recall loop | No controlled quality or learning comparison; open host tasks, not fixed answer curriculum | Persistence, source association and later delivery are wired; verified capture is a host policy | Useful compounding and semantic correctness not established by storage, lint or retrieval. Direct live writes are a supported counterexample to universal prepublication lint, not to the policy itself. |

## Bounded conclusion

LWC separates agent reasoning from durable storage. For the inspected Wiki loop, the checks license structural conclusions: citations or provenance exist, selected references resolve, draft conflicts/lint permit publication, and ingest completion has required page kinds. They do not independently accept the truth of a synthesis. The active-memory policy prescribes source-relative verification, retrieval checks and live revalidation; the inspected Rust gates cannot establish that the host performed them. See [EPI-RTE-lint-check](#epi-rte-lint-check), [EPI-RTE-milestone-review](#epi-rte-milestone-review), [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete).

Retention and later consumption are positive architectural findings, not merely doctrine. Pages and event content are acquired with source warrant unknown at admission. Budgeted recall reshapes delivery and can omit qualifications. Reference envelopes are intended as data, not higher-priority instructions, even when pi places them in the system-prompt channel. Semantic activation and benefit are unobserved. See [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context). No inspected source-to-generated-claim pair establishes an accepted ampliative conjecture or integration after such acceptance; the uninspected Book, Discussion and Plan routes prevent generalizing this to a whole-system absence.

Practice provides a materially different evaluator. Objective grades are derivations from frozen JSON answers and responses; the limited warrant is exact equality, not mastery or the correctness of the answer key. Item verification checks stable identity and reread fields against live Book/Tutor records, while semantic verification is instructed. Subjective acceptance consumes caller rationale/confidence, with pending review below 0.6 and durable mistake membership; it is not an independent rubric judgment. Learner overrides retain history but authenticate only submitted actor data in this local function. See [EPI-RTE-practice-verify](#epi-rte-practice-verify), [EPI-RTE-practice-grade](#epi-rte-practice-grade).

There are direct behavior-shaping paths without establishing a newly warranted proposition: useful/not-useful feedback changes temporal ranking, and Soul revisions supply later teaching preferences. Their standing capacity coexists with unestablished learning benefit. See [EPI-RTE-temporal-feedback](#epi-rte-temporal-feedback), [RT-BAP-soul-guidance](runtime.md#rt-bap-soul-guidance). Neither persistence, reflective subject matter, automated scoring nor an approval label alone establishes content-directed theory criticism, iteration, autonomy or exercised self-improvement. Provider parameter learning is uninspected separately; fixed or mutable weights cannot be inferred from these text routes. No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-memory-events
Label: Temporal memory events

Source-native identity: `memory_events`, associated fragments, changes, evidence and relations. Natural-language fragments are interpreted by agents; IDs, times, relation types and feedback signals are symbolic. Substrate: SQLite plus FTS. Distinct from the page referent of [RT-RTE-page-write](runtime.md#rt-rte-page-write); no temporal object counterpart in supplied runtime records. SRC-1, `src/store/temporal_memory.rs`.

> insert_memory_fragments(&tx, &event_id, &input)?;
> insert_memory_changes(&tx, &event_id, &input.changes)?;
> insert_memory_evidence(&tx, &event_id, &input.evidence)?;
> insert_memory_relations(&tx, &event_id, &input.relations)?;
> index_memory_event(&tx, &event_id, &input)?;
> --- `src/store/temporal_memory.rs`

#### EPI-OBJ-practice-items
Label: Practice items

Source-native identity: versioned `practice_items`, frozen into `paper_items`. Prompt/rubric text is natural language; answer JSON, state, revisions, source refs and points have symbolic consumer rules. Substrate: private Practice SQLite store. Distinct from Tutor session replies in [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn), though a committed turn can be its evidence. No supplied item counterpart. SRC-1, `src/learning/practice.rs`.

> if current["prompt"] != input.prompt
>     || current["answer"] != input.answer
>     || current["rubric"] != serde_json::to_value(&input.rubric).unwrap()
>     || current["source"] != serde_json::to_value(&input.source).unwrap()
> --- `src/learning/practice.rs`

#### EPI-OBJ-practice-grades
Label: Practice grades

Source-native identity: `grades` and `grade_history`; numeric score/confidence and symbolic method/state, with natural-language rationale. Substrate: private SQLite. Distinct from items and Tutor checkpoints in [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn); no supplied grade counterpart. SRC-1, `src/learning/practice.rs`.

> "INSERT INTO grade_history VALUES(?1,1,?2,?3,?4,?5,?6,?7)",
> params![id, score, rationale, confidence, method, state, at],
> --- `src/learning/practice.rs`

### Routes

#### EPI-RTE-milestone-review
Label: Milestone verification policy

Endpoints: candidate reusable result through instructed source/retrieval review to capture and live revalidation. Owner: external agent under shipped skill. No new counterpart for this semantic review in supplied runtime; [RT-RTE-page-write](runtime.md#rt-rte-page-write) owns physical admission and [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) owns the public claim. SRC-1, `skills/using-lwc/references/active-memory.md`, doctrine/design.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: inapplicable — policy has no independent executable return.
- Later read-back: resulting captured pages can reach later agents through ordinary Wiki reads; actual compliance not observed.
- Delegated visibility: host agent reads policy; no delegated worker established.
- Selection predicate: verified decision, accepted design, runbook, root cause, correction, synthesis or durable preference likely to be reused.
- Invalidation or expiry: policy requests freshness checks and revision of changed claims, not time-based certification.
- Activation or effect: policy directs evidence use, no unverified conclusions, top-five original/paraphrase retrieval and postcommit revalidation.
- Evidence limits: this is requested host behavior, not semantic validation implemented by the cited store gates.

Proposer/decider/veto: agent authors, reviews and can decline capture; software admission remains separate; human per-content approval not required by this rule. Mode: open tasks. Criterion: current immutable sources or explicit provenance, changed pages lint/retrieval fit, and no unverified conclusion. Intended use: durable reusable knowledge; scope: changed claims/pages. No semantic answer oracle supplied. Recovery: changeset discard/rebegin or immediate mistaken-commit rollback is instructed. The policy does not certify produced claims merely by naming them verified.

> - Claims trace to current immutable sources or explicit provenance.
> - Changed pages pass lint and fixed original/paraphrase retrieval checks in the
>   top five.
> - Draft validation is repeated against live state after commit.
> - No secret, transient detail, or unverified conclusion was persisted.
> --- `skills/using-lwc/references/active-memory.md`

#### EPI-RTE-lint-check
Label: Wiki lint diagnostics

Endpoints: selected store through SQL issue predicates and Markdown structure checks to paginated response/counts. Owner: Store. This is the evaluator upstream of, not duplicate publication identity with, [RT-RTE-changeset-commit](runtime.md#rt-rte-changeset-commit). SRC-1, `src/store/materialize.rs`, `src/store/types.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: structured issues, counts, blocking/advisory totals and pagination.
- Later read-back: inapplicable — issue computation reads current store, not accumulated semantic feedback; explicit lint logging is separate operation bookkeeping.
- Delegated visibility: caller receives diagnostics; no model worker invoked.
- Selection predicate: current store and issue predicates, then offset/limit; totals precede pagination.
- Invalidation or expiry: store mutation can change subsequent lint results.
- Activation or effect: ordinary lint diagnoses; changeset commit consumes blocking lint separately, with override and direct-write alternatives.
- Evidence limits: selected SQL and result construction inspected, not every rule; no semantic entailment evaluator established here.

Target/domain: citation/provenance presence, link/index integrity and Markdown structure. Evaluator: deterministic code. For a page with zero source rows but one explicit-provenance row, the inspected `uncited_page` predicate does not emit that issue: its second NOT EXISTS is false. This is a concrete deduction from SQL, not target execution and not a claim that all other lint rules pass. It demonstrates why provenance presence is weaker than verified truth. No human adjudication or answer oracle in this computation.

> WHERE NOT EXISTS (
>     SELECT 1 FROM page_sources ps WHERE ps.page_slug = p.slug
> )
>   AND NOT EXISTS (
>     SELECT 1 FROM page_provenance pp WHERE pp.page_slug = p.slug
> )
> --- `src/store/types.rs`

> let blocking_total = all_issues
>     .iter()
>     .filter(|issue| issue.severity.is_blocking())
>     .count();
> --- `src/store/materialize.rs`

#### EPI-RTE-temporal-feedback
Label: Temporal event retention and ranking

Endpoints: caller event/feedback to retained temporal records and ranked recall. Owner: Store; ordinary recall consumer receives latest-known/superseded states, conflict indicators and explicit lack of live verification. Distinct from page replacement and bounded MCP page retrieval in [RT-RTE-page-write](runtime.md#rt-rte-page-write), [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall); no supplied temporal-route counterpart. SRC-1, `src/store/temporal_memory.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: event/retention/pressure/hints receipt, feedback receipt or ranked recall list.
- Later read-back: later memory recall reads retained event, lineage relations and summed feedback; age/budget retention can remove events.
- Delegated visibility: requesting caller receives event text and metadata; downstream model delivery is host-owned.
- Selection predicate: tokenized query, time limits, age/protected predicate, supersession resolution, candidate limit, feedback adjustment and final result limit.
- Invalidation or expiry: retention runs on writes; current-visible relation traversal can replace old candidate selection; helper internals not fully assessed.
- Activation or effect: useful/not-useful signals affect recall rank; caller contradiction relations produce an unresolved-conflict flag, not an automatic content rejection.
- Evidence limits: no trace of actual feedback/use, truth evaluation or improved future task capacity; hint consumers and eviction internals not fully traced.

Caller proposes events, relations and feedback and can withhold them; software validates existence/nonempty reason and controlled signal. Human contribution is unresolved, mode is open use, no truth answer oracle. Usefulness feedback does not revise event meaning. Feedback is retained independently of its interpretation. With lexical rank -10 and clamped feedback +1, inspected arithmetic yields adjustment 0.5 and resulting rank -10.5, not a claim of greater truth. Negative signals reverse that direction. Rank is the operational channel into future selection, not evidence-consuming semantic acceptance.

> let feedback = memory_feedback_score(&self.conn, &event_id)?;
> let adjustment = candidate.lexical_rank.abs().max(1e-6)
>     * 0.05
>     * feedback.clamp(-3, 3) as f64;
> --- `src/store/temporal_memory.rs`

> live_verified: false,
> unresolved_conflict,
> --- `src/store/temporal_memory.rs`

> if !matches!(signal, "useful" | "not-useful") {
> --- `src/store/temporal_memory.rs`

#### EPI-RTE-practice-verify
Label: Practice item verification

Endpoints: draft item plus repeated prompt/answer/rubric/source to verified successor revision; downstream bank admission and paper selection use verified revisions. Owner: Practice code, semantic reviewer is external agent. Distinct from Tutor turn persistence in [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn); no supplied verification counterpart. SRC-1, `src/learning/practice.rs`, implementation; `skills/using-practice/SKILL.md`, doctrine/design.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: verified successor item or request/revision/state/source error.
- Later read-back: bank and paper-selection paths select verified revisions; skill requires source reread and verification before this transition.
- Delegated visibility: caller receives receipt; source validation internally opens sibling Book or Tutor SQLite read-only, not a model delegate.
- Selection predicate: exact current draft revision and identical repeated fields; source subject and Book block locator/hash or committed Tutor turn revision.
- Invalidation or expiry: current source mismatch rejects verification; paper selector excludes items with newer retired revisions. Continuous postverification semantic freshness not established.
- Activation or effect: admits eligible revision to verified pool; bank addition rejects nonverified items.
- Evidence limits: source identity SQL checks existence/hash/revision, not whether prompt/answer logically follows from source; paper-selection details beyond inspected predicate not audited.

Agent/caller proposes and requests verification; software can veto stale identity or missing evidence; compulsory authenticated human approval not present in this local transition. Mode: durable assessed work. Oracle: Book block or Tutor turn supplies reference identity, not an automatically extracted semantic answer. Guidance: draft until reread/verified. Admission creates a revision; retirement is separate. Rejection leaves repair possible. No automatic source-truth proof follows from function naming.

> validate_source_truth(
>     &store.root,
>     &input.source,
>     current["subject_id"].as_str().unwrap(),
> )?;
> --- `src/learning/practice.rs`

> "SELECT 1 FROM book_blocks block JOIN books book ON book.id=block.book_id WHERE block.id=?1 AND block.book_id=?2 AND block.text_hash=?3 AND book.subject_id=?4",
> --- `src/learning/practice.rs`

> "SELECT 1 FROM tutor_turns turn JOIN tutor_sessions session ON session.id=turn.session_id WHERE turn.id=?1 AND turn.state='committed' AND CAST(turn.revision AS TEXT)=?3 AND session.subject_id=?4",
> --- `src/learning/practice.rs`

> Generated items stay draft until prompt, answer, rubric, and exact source ref are
>    re-read and verified. Formal papers use verified revisions and report shortages
>    without weakening the blueprint.
> --- `skills/using-practice/SKILL.md`

#### EPI-RTE-practice-grade
Label: Practice grading and override

Endpoints: terminal attempt's exact response and frozen paper item to grade/history and mistake membership; learner override updates grade/history. Owner: Practice software for objective scoring and state decisions; caller for subjective judgment. Distinct from Tutor teaching commit [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn) and item eligibility [EPI-RTE-practice-verify](#epi-rte-practice-verify); no supplied grade counterpart. SRC-1, `src/learning/practice.rs`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: grade envelope or stale revision, wrong grading kind, invalid rationale/confidence/score or already-graded error.
- Later read-back: grade reads include history; below-full objective grades or pending/below-full subjective grades activate durable mistake-set membership. Override appends history.
- Delegated visibility: external caller receives result; subjective rationale is supplied, no internal model evaluation established.
- Selection predicate: response ID/revision, non-in-progress attempt and frozen item; subjective item revision/rubric, bounded score/confidence and agent_rubric method; override requires actor string learner and revision/reason.
- Invalidation or expiry: duplicate grade rejected; learner override changes current score/method/state while retaining history. Downstream removal of mistake membership after override not established by inspected function.
- Activation or effect: objective equality yields full points or zero; subjective confidence below 0.6 yields pending_review, otherwise accepted. Mistake set is an implemented consequence beyond the immediate receipt.
- Evidence limits: no observed marking or learner outcome, no independent authentication of submitted learner actor, no evidence all downstream scheduling consumes grades.

Objective target/domain: exact JSON equality between response and frozen answer. The oracle is the author-supplied frozen answer; code supplies only comparison. Concrete input deduction: expected JSON string `"A"`, actual `"A"`, points 2 yields score 2 and accepted; actual `"a"` yields 0, accepted and a mistake record. This follows inspected code without execution; it neither validates answer-key truth nor judges semantic equivalence. Subjective target: exact response under frozen rubric; external agent proposes score/rationale/confidence, software checks bindings and bounds, then admits according to confidence. Confidence alone is not evidence that the rubric was applied correctly. Mode: bounded papers/attempts, not a controlled experiment of learning benefit. The caller may decline or correct through supported override; software vetoes malformed/stale submissions. Generated questions and semantic grading remain host-dependent.

> let score = if correct == actual { row.4 } else { 0.0 };
> --- `src/learning/practice.rs`

> let state = if input.confidence < 0.6 {
>     "pending_review"
> } else {
>     "accepted"
> };
> --- `src/learning/practice.rs`

> if state == "pending_review" || input.score < max {
>     record_mistake(&tx, &row.0, row.1, &input.request_id, "grade needs review")?;
> }
> --- `src/learning/practice.rs`

> if input.actor != "learner" {
> --- `src/learning/practice.rs:2241-2241`

> "INSERT INTO grade_history VALUES(?1,?2,?3,?4,1,'learner_override','overridden',?5)",
> --- `src/learning/practice.rs`
