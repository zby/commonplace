---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Gnosis epistemic routes: caller-supplied rationale, advisory review, structural admission, lexical read-back and withdrawal."
run-id: AAS-2026-10-15-gnosis-5bfb42422ce3-01
reviewed-boundary: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
---

# Gnosis epistemic report

## Source-and-claim boundary

The question is how Gnosis obtains repository knowledge, assesses it, licenses reliance and changes later behavior. Scope and frozen evidence identity: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). All source-dependent findings below use SRC-1 at that revision. Implementation reads establish executable routes, not observed operation. The external coding agent supplies semantic judgment; its model, private reasoning and task execution are outside the target. No model parameters, observed session trace, observed test result or causal comparison were supplied.

The assessment covers all dispatched knowledge operations and the shipped instructions that give them semantic purpose. It does not assess release delivery, dependency internals or external shell authorization. Those exclusions prevent conclusions about deployment reliability, provider reasoning or enforcement by the host. No new material responsibility outside the selected boundary was found. No supplied runtime fact needs supersession; the split records below expose distinct functions within its valid container routes.

| Entry point or operation | Source path in SRC-1 | Coverage and records |
|---|---|---|
| Help, plan, review; repository caller | `cmd/gn/main.go`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `internal/doctrine/commands.txt`, `AGENTS.md`, `README.md` | Direct reads; [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery), [EPI-RTE-candidate-filter](#epi-rte-candidate-filter), [EPI-RTE-candidate-choice](#epi-rte-candidate-choice); embed wiring also supplied by runtime. |
| Write, including stdin and explicit author | `internal/commands/write.go`, `internal/commands/author.go`, `internal/commands/topics.go`, `internal/storage/storage.go` | Direct reads; [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-entry-import](#epi-rte-entry-import), [EPI-RTE-entry-retention](#epi-rte-entry-retention). ID-prefix helper details supplied by [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission). |
| Search | `internal/commands/search.go`, `internal/index/index.go` | Direct reads; [EPI-RTE-lexical-selection](#epi-rte-lexical-selection), [EPI-RTE-cache-refresh](#epi-rte-cache-refresh). |
| Show, latest, topics | `internal/commands/show.go`, `internal/commands/latest.go`, `internal/commands/topics.go` | Direct reads; [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), [EPI-RTE-topic-count](#epi-rte-topic-count). |
| Edit: positional, piped, editor | `internal/commands/edit.go`, `internal/storage/storage.go` | Direct reads; [EPI-RTE-entry-replacement](#epi-rte-entry-replacement). |
| Remove; dangling references | `internal/commands/rm.go`, `internal/storage/storage.go` | Direct reads; [EPI-RTE-entry-withdrawal](#epi-rte-entry-withdrawal). |
| Reindex and automatic refresh | `internal/commands/reindex.go`, `internal/index/index.go` | Direct reads; [EPI-RTE-cache-refresh](#epi-rte-cache-refresh). |
| Shipped knowledge instances | `.gnosis/entries.jsonl` | All ten lines directly read; [EPI-OBJ-entry-text](#epi-obj-entry-text). Candidate availability and attributed history, not production or acceptance traces. |
| Tests and CI | `internal/commands/sanitize_query_test.go`, `internal/commands/reindex_test.go`, `internal/index/index_test.go`, `.github/workflows/test.yml` | Full sanitizer test and CI file; reindex tests for search and stale replacement; index tests for changed/unchanged mtime directly read; [EPI-RTE-test-check](#epi-rte-test-check). Other tests inventoried, not exhaustively assessed; prevents test-adequacy or exhaustive defect claims. |
| Hooks, registered tools, other entry points | `cmd/gn/main.go`, `internal/doctrine/doctrine.go`, `internal/commands/edit.go`, `internal/commands/author.go` | Dispatch directly inspected; tracked `cmd/` and `internal/` inventory and search for hook, Register, MCP, provider, embed and exec.Command. Only editor and Git-config subprocesses found in this executable search boundary; no additional registered semantic evaluator found. This is not an audit of external integrations. |
| Root/cache/locking and rendering helpers | `internal/storage/storage.go`, `internal/paths/paths.go`, `internal/termcolor/termcolor.go`, `internal/textwrap/textwrap.go` | Storage directly read; root/cache/lock and rendering account otherwise supplied by [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance) and runtime capability limits. Exact rendering/helper correctness not exhaustively assessed. |

Consequential source claims: [EPI-CLM-knowledge-continuity](#epi-clm-knowledge-continuity), [EPI-CLM-review-filter](#epi-clm-review-filter), and [RT-CLM-agent-compliance](runtime.md#rt-clm-agent-compliance). Missing session provenance prevents tracing any shipped entry to a particular human statement, observation, evaluation or acceptance. Missing later-consumer traces prevent establishing reliance or benefit. Missing interventions prevent causal attribution to review, retrieval or accumulated entries. The target's intentionally mnemonic scope does not require a research-production loop; it also does not warrant treating retained rationale as verified knowledge.

## Epistemic-object inventory

Object identity, form, substrate and evidence passages are owned by the cited records. Candidate content is separated from the control metadata and output selection that can change its apparent authority.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-entry-text](#epi-obj-entry-text) | Historical decisions, reasons, operational constraints and conditional predictions; specific examples: see record | see record | SRC-1 `.gnosis/entries.jsonl` | A decision directive is not itself true/false; its historical attribution or stated causal reason can be. Provenance and acceptance unresolved. |
| [EPI-OBJ-entry-metadata](#epi-obj-entry-metadata) | IDs, labels, author attribution, times and related-ID assertions; not independent evidence for the body | see record | SRC-1 `internal/storage/storage.go` | Attribution is not authenticated origin; related is not a typed supersession judgment. |
| [EPI-OBJ-entries-fts](#epi-obj-entries-fts) | Selected body/topic text and symbolic match/rank data | see record | SRC-1 `internal/index/index.go` | Omits author, related and timestamps from matching; snippets are not complete claims or evidence. |
| [EPI-OBJ-topic-aggregate](#epi-obj-topic-aggregate) | Counts of decoded topic occurrences | see record | SRC-1 `internal/commands/topics.go` | Valid-write topics are deduplicated; manually duplicated memberships are counted repeatedly. |
| [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine) | Policy for recording and consulting entries, plus contestable rationale about reproducibility | see record | SRC-1 `internal/doctrine/review.txt` | Static guidance, not an observed evaluation of any particular entry. |

## Authority-route ledger

Each compact entry separates its function even where the same implementation supplies several functions. The declaring record owns endpoints, targets, evaluators, conditions, results, force, consumer, channel, horizon and limits; the references below deliberately do not copy those fields. No route has observed-run activation evidence.

Route ID: [EPI-RTE-candidate-filter](#epi-rte-candidate-filter)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-candidate-filter](#epi-rte-candidate-filter).
Content/update relation: no content change.
Claim IDs: [EPI-CLM-review-filter](#epi-clm-review-filter). Mismatch marker: semantic filter is instructed, not software-enforced.

Route ID: [EPI-RTE-candidate-choice](#epi-rte-candidate-choice)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-candidate-choice](#epi-rte-candidate-choice).
Content/update relation: no content change.
Claim IDs: [EPI-CLM-review-filter](#epi-clm-review-filter). Mismatch marker: usefulness selection is not evidence-consuming acceptance of a truth claim.

Route ID: [EPI-RTE-structure-check](#epi-rte-structure-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-structure-check](#epi-rte-structure-check).
Content/update relation: no content change.
Claim IDs: none. Mismatch marker: none; structural validity has no semantic license.

Route ID: [EPI-RTE-entry-import](#epi-rte-entry-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-entry-import](#epi-rte-entry-import).
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown. Caller text is trimmed, not assessed against its purported origin.
Claim IDs: [EPI-CLM-knowledge-continuity](#epi-clm-knowledge-continuity). Mismatch marker: retained content is not necessarily endorsed content.

Route ID: [EPI-RTE-entry-retention](#epi-rte-entry-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-entry-retention](#epi-rte-entry-retention).
Content/update relation: no content change.
Claim IDs: [EPI-CLM-knowledge-continuity](#epi-clm-knowledge-continuity). Mismatch marker: persistence is not lifecycle integration after acceptance.

Route ID: [EPI-RTE-lexical-selection](#epi-rte-lexical-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-lexical-selection](#epi-rte-lexical-selection).
Content/update relation: truth-apt transformation: non-ampliative reshaping; selected snippets and ranking reorganize existing content, with omission rather than semantic validation.
Claim IDs: [EPI-CLM-knowledge-continuity](#epi-clm-knowledge-continuity). Mismatch marker: lexical rank is not credibility rank.

Route ID: [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read) and [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance).
Content/update relation: truth-apt transformation: non-ampliative reshaping; show renders bodies, latest selects and truncates; see deterministic counterexample in [EPI-RTE-lexical-selection](#epi-rte-lexical-selection).
Claim IDs: [EPI-CLM-knowledge-continuity](#epi-clm-knowledge-continuity). Mismatch marker: an excerpt can omit the condition under which its visible assertion holds.

Route ID: [EPI-RTE-topic-count](#epi-rte-topic-count)
Route function: content transformation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-topic-count](#epi-rte-topic-count).
Content/update relation: truth-apt transformation: entailed derivation; occurrence counts follow from the decoded array under the inspected loop, not from any truth of entry bodies.
Claim IDs: none. Mismatch marker: none.

Route ID: [EPI-RTE-edit-check](#epi-rte-edit-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-edit-check](#epi-rte-edit-check).
Content/update relation: no content change.
Claim IDs: none. Mismatch marker: edit structural passage does not license a claim of semantic correction.

Route ID: [EPI-RTE-entry-replacement](#epi-rte-entry-replacement)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-entry-replacement](#epi-rte-entry-replacement).
Content/update relation: truth-apt transformation: acquisition/import; replacement body comes from caller/editor, with source warrant unknown. Meaning need not be preserved relative to the old body; whether the external author derived or conjectured it is not determinable.
Claim IDs: [EPI-CLM-review-filter](#epi-clm-review-filter). Mismatch marker: saving an edit is operational permission, not a truth acceptance.

Route ID: [EPI-RTE-entry-withdrawal](#epi-rte-entry-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-entry-withdrawal](#epi-rte-entry-withdrawal).
Content/update relation: no content change; corpus membership changes, without a recorded proposition about why the entry was withdrawn.
Claim IDs: [EPI-CLM-review-filter](#epi-clm-review-filter). Mismatch marker: withdrawal from JSONL does not erase previously delivered context or guarantee immediate cache withdrawal.

Route ID: [EPI-RTE-cache-refresh](#epi-rte-cache-refresh)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-cache-refresh](#epi-rte-cache-refresh).
Content/update relation: truth-apt transformation: non-ampliative reshaping; rebuild copies ID/body/joined topics from a snapshot. Timestamp decisions add no endorsement.
Claim IDs: none. Mismatch marker: file freshness is not semantic currency or reliable evidence of revocation.

Route ID: [EPI-RTE-test-check](#epi-rte-test-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-test-check](#epi-rte-test-check).
Content/update relation: no content change to retained knowledge; assertions evaluate fixture-specific program outputs.
Claim IDs: none. Mismatch marker: fixture success, even if later observed, would not validate the content retrieved.

Route ID: [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery) and [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance).
Content/update relation: non-truth-apt policy/content update: delivery of static instructions requests search, prompt recording and conflict escalation; it does not revise internal model parameters or prove changed caller behavior.
Claim IDs: [RT-CLM-agent-compliance](runtime.md#rt-clm-agent-compliance). Mismatch marker: policy delivery implemented; adaptation of caller behavior unobserved.

Route ID: [EPI-ABS-evidence-acceptance](#epi-abs-evidence-acceptance)
Route function: lifecycle integration
Architectural status: no route found within boundary
Object/candidate ID; transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-ABS-evidence-acceptance](#epi-abs-evidence-acceptance).
Content/update relation: no content change established after evidence-consuming acceptance. Related-ID linking and indexing operate without that prerequisite.
Claim IDs: none. Mismatch marker: none; this negative concerns inspected target mechanisms, not inaccessible external reasoning.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-continuity](#epi-clm-knowledge-continuity) | see record | SRC-1 `README.md`, `docs/PRODUCT_STRATEGY.md`; doctrine/design, attributed self-use | see record | [EPI-RTE-entry-import](#epi-rte-entry-import), [EPI-RTE-entry-retention](#epi-rte-entry-retention), [EPI-RTE-lexical-selection](#epi-rte-lexical-selection) | Shipped candidates only; no traced production/use | No removal comparison or later-task evidence | Implemented capacity to preserve and retrieve caller rationale across sessions | Cumulative verified knowledge or improved decisions not established; missing provenance also prevents classifying every claim's source warrant |
| [EPI-CLM-review-filter](#epi-clm-review-filter) | see record | SRC-1 `README.md`, `docs/PRODUCT_STRATEGY.md`; doctrine/design and reported efficacy | see record | [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-entry-replacement](#epi-rte-entry-replacement), [EPI-RTE-entry-withdrawal](#epi-rte-entry-withdrawal); requested [EPI-RTE-candidate-filter](#epi-rte-candidate-filter) | No supplied review trajectory | No before/after noise measure; no evidence isolating review effect | Explicit semantic-selection guidance with executable maintenance affordances | Claimed noise reduction not demonstrated; semantic enforcement intentionally delegated |
| [RT-CLM-agent-compliance](runtime.md#rt-clm-agent-compliance) | see record | SRC-1 `README.md`; doctrine/design claim | [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine) | [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery) | Uninspected | Direct writes and external task work bypass prescribed workflow | Guidance can reach a shell-using agent | Every-time compliance is not an enforced invariant or observed result |

## Bounded conclusion

Gnosis implements acquisition and persistence of caller-supplied rationale, with unknown source warrant, and request-driven delivery to later callers. The body can contain truth-apt historical and causal claims, rejected alternatives, intentions or pure directives. Retained examples establish availability, not the route that authored, checked or accepted them. Text and metadata remain distinct: a Git-config author string does not prove human origin, and a related ID does not prove supersession. See [EPI-RTE-entry-import](#epi-rte-entry-import), [EPI-OBJ-entry-metadata](#epi-obj-entry-metadata).

Its semantic criteria are non-reconstructability, human/empirical origin, lack of an obvious code-comment anchor, sufficient context and avoiding short-lived status. These are instructed usefulness criteria for later repository work, not a general truth test. Software criteria are nonempty body, normalized sufficiently long topics and resolvable related IDs, scoped to the command paths described in [EPI-RTE-structure-check](#epi-rte-structure-check). A passing check permits retention or replacement. It licenses no inference that the retained reason, prediction or causal account is true. Neither observed evidence-consuming acceptance of an ampliative claim nor post-acceptance lifecycle integration is established within the inspected target; this does not rule out such judgments by external users.

Lexical selection and snippet limits reshape existing material rather than generating warranted explanations. Topic occurrence totals are a separate, narrowly entailed derivation over decoded arrays, not knowledge of the repository's real behavior. The body is not evaluated against code, measurements or an expected answer. Search rank determines which snippets appear, then the external agent interprets their natural language. The behavioral path is advisory stdout across sessions, not a code-edit veto. Missing later-consumer evidence leaves use, learning as improved capacity, and causal benefit unestablished independently of implemented persistence.

Cleanup has real operational force: edit replaces the stored body and rm removes corpus membership. Neither requires a reason, records a semantic verdict or retracts old tool output already in a model window. Mtime refresh and explicit rebuild normally propagate the surviving corpus to lexical search, but equal mtimes and a missing JSONL file can leave stale indexed material. A related replacement alone leaves the old candidate available. Thus retention, withdrawal and downstream reliance must not be collapsed. See [EPI-RTE-entry-replacement](#epi-rte-entry-replacement), [EPI-RTE-entry-withdrawal](#epi-rte-entry-withdrawal), [EPI-RTE-cache-refresh](#epi-rte-cache-refresh).

The target implements policy delivery without a truth-apt intermediary: instructions request searching, early recording and escalation. Delivery is supported; changed behavior is not observed. The inspected dispatch/index/storage routes contain no distributed-parametric component; external model versions, weights, latent processing and mutability are uninspected. Persistence and doctrine alone do not establish reflection, autonomous criticism, iterative theory building or exercised self-improvement. These are independent limits, not a single system-wide score or verdict. Gnosis's bounded contribution is repository-context retention and consultation infrastructure with caller-owned semantic authority.

## Shared records

### Operative objects

#### EPI-OBJ-entry-text
Label: Entry text

Identity: `storage.Entry.Text`, caller-supplied body in `.gnosis/entries.jsonl`. Natural-language representational form; JSON string encoding and JSONL filesystem substrate. Historical assertions, causal explanations and forecasts can be truth-apt over the named repository, release configuration or event history. Instructions and choices are not automatically propositions. No object counterpart is declared in the supplied runtime; closest [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission) is the route, not this object. SRC-1: `internal/storage/storage.go`, `.gnosis/entries.jsonl`.

Concrete candidate: entry `vycczu` predicts rerun conflicts after partial release uploads, names a proposed configuration change, and says the fix is not yet installed. Entry `dmtxyh` reports rejecting Bleve and gives reasons, but its comparative dependency/typo claims have no attached measurement trace. These are retained assertions, not our acceptance of them. The snapshot cannot individuate their originating evaluation or establish whether an external writer imported, entailed or conjectured each assertion. Entries lacking author fields reinforce the provenance limit, not a conclusion of falsehood.

> Known flaw in the release job: if goreleaser fails partway through uploading artifacts, a rerun will hit 422 conflicts on the assets that already uploaded and abort.
> --- `.gnosis/entries.jsonl`

#### EPI-OBJ-entry-metadata
Label: Entry metadata

Identity: Entry ID, Topics, Author, Related, CreatedAt and UpdatedAt alongside the body. Symbolic fields select lookup, grouping, display and references; author attribution is interpreted as natural language by a reader. Substrate: JSONL fields and decoded Go values. No runtime object counterpart; [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission) supplies the closest write route. SRC-1: `internal/storage/storage.go`, `internal/commands/author.go`, `internal/commands/show.go`.

Author is caller flag, Git config or fallback, not authenticated provenance. Created/updated are command-clock values, not evidence timestamps. Related is an untyped ID list rendered by show, not a replacement edge with enforced consequence. Search omits these fields except ID and topics. Full-entry reads can expose them, but cannot restore absent origin evidence.

> Related   []string  `json:"related"`
> --- `internal/storage/storage.go`

> return authorArg, true
> --- `internal/commands/author.go`

#### EPI-OBJ-entries-fts
Label: Entries FTS

Identity: `entries_fts` rows in disposable SQLite cache. Symbolic FTS structure holds ID, body text and joined topic labels; natural-language body/snippets remain interpreted by the external caller. SQLite tables and Go SearchHit values are substrates, not independent epistemic evidence. No supplied runtime object counterpart; closest [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read) consumes this object. SRC-1: `internal/index/index.go`, `internal/commands/search.go`.

> CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts USING fts5(
> entry_id UNINDEXED,
> text,
> topics,
> tokenize = 'porter unicode61',
> prefix = '2 3 4'
> );
> --- `internal/index/index.go`

#### EPI-OBJ-topic-aggregate
Label: Topic aggregate

Identity: `TopicAggregate.Topic` and `Count`, produced from decoded entries for `gn topics`. Symbolic map/struct counters, in-memory then stdout, not an independently retained theory. No supplied runtime object counterpart; [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read) contains the producing browse operation. SRC-1: `internal/commands/topics.go`.

> type TopicAggregate struct {
> Topic string
> Count int
> }
> --- `internal/commands/topics.go`

### Routes

#### EPI-RTE-candidate-filter
Label: Candidate filter
Part of: [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Semantic-check part of the admission workflow: session candidate → external agent interpreting review/plan → usefulness judgment. Target/domain: prospective repository rationale for later sessions, assessed for reproducibility from code/docs, human or unreconstructable empirical origin, code-anchor placement, staleness and context sufficiency. Evaluator: instructed external agent; it may consult the human/session, but no particular evidence consumption is recorded. No expected-answer oracle is prescribed. Open coding work, not a curriculum. Force: advisory at proposal generation, across candidate writes; no executable gate on the text's truth. Epistemic license: none beyond an attributed selection judgment. SRC-1: `internal/doctrine/review.txt`, `internal/doctrine/plan.txt`.

- Immediate return: Instructed judgment to skip, comment in code or consider an entry; no structured result artifact implemented.
- Later read-back: inapplicable — the check result itself is not persisted; a later selected body belongs to the retention route.
- Delegated visibility: inapplicable — no internal reviewer worker; external host reasoning is uninspected.
- Selection predicate: Human/empirical origin not reconstructable from code/docs, no obvious code anchor, durable usefulness and sufficient context.
- Invalidation or expiry: A later session can reassess; no recorded confidence, expiry or check history.
- Activation or effect: Delivery of criteria is wired through help; per-candidate evaluation and effect unobserved.
- Evidence limits: Source gives instructions, not an implemented semantic evaluator or a trace of compliance.
- instruction conclusion status: wired
- operation conclusion status: uninspected

> Before writing an entry, ask: would a competent agent, given the code
> and docs, reach this conclusion on its own? If yes, skip it. Reach
> for gnosis only when the knowledge originated from the human or from
> empirical observation that isn't reconstructable from the codebase.
> --- `internal/doctrine/review.txt`

#### EPI-RTE-candidate-choice
Label: Candidate choice
Part of: [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Disposition part distinct from the preceding check: external agent chooses to withhold a candidate, place it in a code comment, or invoke write after its usefulness judgment. Same open-work scope and guidance; whether any particular proposal/decision is human or computational is unresolved. Caller can veto by not writing; no independent human approval or answer oracle is required. Intended use is future repository work. This is instructed editorial admission, not recorded evidence-consuming acceptance of body claims. Consumer: caller choosing an operation; channel: natural-language doctrine; force: advisory; horizon: this candidate and later sessions. SRC-1: `internal/doctrine/review.txt`, `internal/doctrine/plan.txt`.

- Immediate return: Instructed choice to write, skip or comment elsewhere.
- Later read-back: inapplicable — no separate admission rationale is stored by the selection procedure.
- Delegated visibility: inapplicable — no internal delegation.
- Selection predicate: see [EPI-RTE-candidate-filter](#epi-rte-candidate-filter); software does not require a recorded pass.
- Invalidation or expiry: Caller may later edit/remove; no recorded acceptance state to revoke.
- Activation or effect: A caller's subsequent command can retain a body; no observed choice supplied.
- Evidence limits: Direct writes bypass the check and the prescribed review timing. Starting a session does not prove per-content approval.
- instruction conclusion status: wired
- operation conclusion status: uninspected

> For each candidate, first ask whether it has an obvious code anchor —
> a specific line, function, or file where someone editing the code
> would see it. If yes, it belongs as a comment there, not here.
> --- `internal/doctrine/review.txt`

#### EPI-RTE-structure-check
Label: Structure check
Part of: [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Software-check part: Write arguments/stdin → deterministic parsers and ID resolver → error or passage toward append. Target/domain: command input shape, trimmed nonempty text, topic normalization/minimum seven runes and related-prefix resolution in the current pre-append read. Program owns the check; caller supplies candidate and can withhold/resubmit; no required human semantic approval. No answer oracle about body content. Result consumed by Write error-return branches; enforcing force for that invocation, horizon through append. This gives only structural operational permission, no truth license. Compare edit validation separately in [EPI-RTE-entry-replacement](#epi-rte-entry-replacement). SRC-1: `internal/commands/write.go`, `internal/commands/topics.go`.

- Immediate return: Validation error or continuation toward persistence.
- Later read-back: inapplicable — check results are not retained; successful values may be persisted by another function.
- Delegated visibility: inapplicable — no reviewer subprocess or model check.
- Selection predicate: One text argument or stdin, nonempty trimmed body; normalized/deduplicated nonempty topics of sufficient length; uniquely resolvable related IDs.
- Invalidation or expiry: Related-target resolution precedes append locking; subsequent removal can invalidate a target.
- Activation or effect: Code errors block this append; missing Git identity only warns.
- Evidence limits: Passing says nothing about truth, origin, relevance, current applicability or author authenticity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> text = strings.TrimSpace(text)
> if text == "" {
> return fmt.Errorf("text must not be empty")
> }
> --- `internal/commands/write.go`

> if utf8.RuneCountInString(normalized) < storage.IDLength+1 {
> return nil, fmt.Errorf("topic %q is too short (normalized form %q has %d characters, minimum is 7)", topic, normalized, utf8.RuneCountInString(normalized))
> }
> --- `internal/commands/topics.go`

#### EPI-RTE-entry-import
Label: Entry import
Part of: [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Acquisition part: external caller submits body/topics/related/author → Write trims and assigns metadata → Entry proposed to AppendNew. Object: [EPI-OBJ-entry-text](#epi-obj-entry-text) and [EPI-OBJ-entry-metadata](#epi-obj-entry-metadata). Caller proposes and makes the semantic decision; software decides only structural passage. No expected-answer oracle. Trigger: explicit command, instructed during work when a decision/rejection occurs. Human versus computational composition unresolved. Body import preserves submitted text apart from boundary whitespace, not the warrant of an absent originating conversation/observation. Force is permissive admission to a later-retrievable corpus, not epistemic endorsement. Guidance and downstream advisory path: [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine), [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). SRC-1: `internal/commands/write.go`, `internal/commands/author.go`.

- Immediate return: On success a new ID; warnings/errors as in [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission).
- Later read-back: Body and metadata reach later explicit reads after retention; no original conversation or empirical trace is automatically attached.
- Delegated visibility: inapplicable — no internal agent or acceptance review.
- Selection predicate: Caller selects the content; structural check gates the production command.
- Invalidation or expiry: Explicit edit/rm; no TTL, truth score or automatic contradiction detection.
- Activation or effect: Creates a candidate available for later reliance, not proof of later reliance.
- Evidence limits: Source warrant unknown; attribution and related IDs do not reconstruct evidence. Post-append display failure need not roll back retention.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> newID, err := store.AppendNew(storage.Entry{
> Topics:    topics,
> Text:      text,
> Author:    author,
> Related:   related,
> CreatedAt: now,
> UpdatedAt: now,
> })
> --- `internal/commands/write.go`

#### EPI-RTE-entry-retention
Label: Entry retention
Part of: [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Persistence part: passed Entry → exclusive-lock AppendNew → JSON marshal and JSONL append → later ReadAll. Owner: storage program; context: repository-local store; no evaluation of body propositions. Consuming store admits content according to caller command and structural checks, with no independent truth criterion. The produced file survives process/session boundaries; sharing requires external version control. This function changes availability, not semantic warrant. Intended use: later explicit CLI retrieval; enforcing persistence when append succeeds, advisory guidance only when a caller later reads. Rollback/recovery: explicit edit/rm or caller-managed Git, no semantic automatic rollback. SRC-1: `internal/storage/storage.go`; compare the runtime's broader [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission).

- Immediate return: Assigned ID or I/O error.
- Later read-back: ReadAll decodes retained text and metadata; missing file returns empty array; malformed JSON returns error.
- Delegated visibility: inapplicable — local file operation, no worker result.
- Selection predicate: Append the passed Entry after collision-free ID generation against locked existing IDs.
- Invalidation or expiry: Entry persists until explicit replacement/removal or external file change.
- Activation or effect: Appends serialized content; no observed cross-session consumer supplied.
- Evidence limits: Does not retain provenance/evaluation events or ensure crash durability; external writers need not follow locking.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> assignedID = GenerateID(existingIDs)
> entry.ID = assignedID
>
> line, err := json.Marshal(entry)
> --- `internal/storage/storage.go`

#### EPI-RTE-lexical-selection
Label: Lexical selection
Part of: [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read)

Search part: caller query/limit → sanitizeQuery → EnsureFresh → FTS5 MATCH/rank/LIMIT → snippets plus separately reread metadata → stdout. Target/domain: lexical match to indexed text/topics; evaluator is symbolic query/index processing, not a truth assessor. Code selects delivered excerpts; external agent selects query and decides relevance and later action. No answer oracle. Force: ranking and output exclusion now; advisory interpretation if later acted upon, through [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). Epistemic license: at most an index match under this expression, not correctness/completeness of body claims. SRC-1: `internal/commands/search.go`, `internal/index/index.go`, `internal/commands/latest.go`.

- Immediate return: Ranked limited ID/date/topic/snippet rows or error/empty result; author, related IDs and full body omitted.
- Later read-back: Persisted entries can reach future searches; show explicitly reloads full bodies and metadata.
- Delegated visibility: inapplicable — stdout goes to caller, no internal agent.
- Selection predicate: Sanitized expression, FTS5 match, rank order, positive limit default 20; snippet best column can be topics rather than body.
- Invalidation or expiry: Cache uses mtime/rebuild; semantic applicability has no machine expiry.
- Activation or effect: Enforces which text reaches stdout; no evidence that the caller changed a plan.
- Evidence limits: Rank is lexical, not evidence quality; metadata reread is not the indexed snapshot. Empty output is not proof of no relevant rationale.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Deterministic input trace (implementation deduction, not execution): query `foo OR bar-baz` keeps `foo`, whitespace and uppercase `OR`; the bare `bar-baz` run replaces its hyphen with one space. The resulting query is `foo OR bar baz`. This selects by the resulting lexical expression, not by semantic alternatives in the input's apparent compound concept. Quoted `"bar-baz"` instead passes through unchanged. The implementation therefore contradicts any assumption that all compound-query intent is preserved. The test source asserts this shape of transformation but is not a supplied passing run.

> result.WriteString(nonAlphanumericPattern.ReplaceAllString(word, " "))
> --- `internal/commands/search.go`

> WHERE entries_fts MATCH ?
> ORDER BY rank
> LIMIT ?
> --- `internal/index/index.go`

A second deterministic trace bounds excerpt reliance: for latest, a body consisting of 200 `A` runes followed by ` not approved` has no whitespace change in the prefix; the code takes the first 200 runes and appends `…`. The qualification is absent from stdout while the full body remains available through show. This is lossy non-ampliative reshaping, not evidence that a complete proposition is preserved in each excerpt. Search similarly requests only 12 tokens from the best FTS column; exact SQLite tokenization is an external dependency, not executed here.

> if runes := []rune(snippet); len(runes) > snippetMaxRunes {
> snippet = string(runes[:snippetMaxRunes]) + "…"
> }
> --- `internal/commands/latest.go`

#### EPI-RTE-topic-count
Label: Topic count
Part of: [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read)

Aggregation part: decoded Entry.Topics arrays → AggregateTopics map increments → sort by descending count/name → count/topic stdout. Owner: program; no external judgment or oracle. Object: [EPI-OBJ-topic-aggregate](#epi-obj-topic-aggregate). Domain: occurrences in the decoded input, not real-world topic importance or truth. Consumer: caller browsing topics; channel stdout; force ranking/presentation; horizon this invocation and possible query choice. SRC-1: `internal/commands/topics.go`, `internal/storage/storage.go`.

- Immediate return: Count/topic rows, empty output or read error.
- Later read-back: inapplicable — aggregate is not persisted; later invocations recompute from retained entries.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Every topic occurrence in decoded entries; sorted by count then name.
- Invalidation or expiry: Recomputed on every topics invocation.
- Activation or effect: Generates arithmetic counts and browsing order, not a semantic relevance decision.
- Evidence limits: Count means entries only when topics within each entry are unique. Write deduplicates; arbitrary legacy/manual arrays may not.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete derivation: decoded arrays `[architecture, search-index]` and `[architecture]` produce architecture=2 and search-index=1 by successive increments. This follows within the program's input domain, assuming successful decoding; it needs no warranted premise about body truth. For `[architecture, architecture]`, the single entry contributes 2, a countercase to an unconditional distinct-entry-count claim.

> for _, entry := range entries {
> for _, topic := range entry.Topics {
> counts[topic]++
> }
> }
> --- `internal/commands/topics.go`

#### EPI-RTE-edit-check
Label: Edit check
Part of: [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance)

Checking part distinct from replacement: caller-selected entry plus positional/piped text or parsed editor buffer → deterministic validation → error or permission to save. Target/domain: nonempty body for either path; interactive path additionally requires parseable separator, nonempty normalized topics and related IDs resolving against the locked snapshot excluding the edited entry. The external caller proposes and can withhold the edit; software can veto structural failure. No required human approval, semantic evidence or expected-answer oracle. Open maintenance, not an experiment. Consumer: Edit branches and Update transform; enforcing force for this save; horizon this invocation. Epistemic license: structural passage only, not true or improved body content. SRC-1: `internal/commands/edit.go`.

- Immediate return: Error or continuation to replacement; unchanged inputs return no changes without replacement.
- Later read-back: inapplicable — check result itself is not retained.
- Delegated visibility: Editor returns a buffer, not a separate semantic review result; no internal reviewer agent.
- Selection predicate: Explicit path-dependent checks; non-interactive edits preserve metadata without revalidating its references.
- Invalidation or expiry: Interactive related checks use the locked snapshot; no semantic applicability or version criterion.
- Activation or effect: Errors block changed fields from being installed. The interactive failed transform can rewrite unchanged entries before surfacing its error.
- Evidence limits: No body truth check, source comparison or stale-original version veto; tests or execution of this path not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if len(parsed.Topics) == 0 {
> return nil, fmt.Errorf("topics must not be empty")
> }
> if parsed.Text == "" {
> return nil, fmt.Errorf("text body must not be empty")
> }
> --- `internal/commands/edit.go`

#### EPI-RTE-entry-replacement
Label: Entry replacement
Part of: [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance)

Edit part: prefix selects original → caller positional/piped body or editor buffer → validation → locked Update substitutes fields → later readers. Caller proposes and decides replacement; code can reject structural problems, missing target or I/O failure. Explicit open-ended maintenance; no expected-answer oracle or required human approval. Guidance: review says tidy stale entries, but edit requires no semantic justification. Checking and its path-specific domain: see [EPI-RTE-edit-check](#epi-rte-edit-check); this disposition function consumes its passage result rather than adding a semantic assessment. Force: enforcing replacement at file consumer; downstream advisory natural-language authority through later CLI reads across sessions. Epistemic authority: no license to infer correction or truth from a successful save. SRC-1: `internal/commands/edit.go`, `internal/storage/storage.go`.

- Immediate return: Success, no-changes notice, parse/validation/editor/I/O error.
- Later read-back: Replacement body and UpdatedAt reach later direct reads and rebuilt search index; prior body not versioned internally.
- Delegated visibility: Editor subprocess receives topics/related/body buffer and stdio; no internal review agent or guaranteed human editor.
- Selection predicate: Unique resolved prefix; positional text takes precedence over piped input; otherwise editor path.
- Invalidation or expiry: Replacement overrides selected fields; same-entry stale-buffer overwrite is not version-vetoed.
- Activation or effect: Changes stored candidate; does not ensure previously delivered text is corrected in caller context.
- Evidence limits: A new body is imported from the caller/editor; whether externally entailed or conjectured is unresolved. Temp rewrite/rename protects file replacement, not semantic correctness or history. Recovery requires another edit/removal or external Git restoration.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> updated := entry
> updated.Text = newText
> updated.UpdatedAt = time.Now().UTC()
> entries[index] = updated
> --- `internal/commands/edit.go`

#### EPI-RTE-entry-withdrawal
Label: Entry withdrawal
Part of: [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance)

Removal part: caller-selected prefixes → all prefixes resolve or error → Update excludes selected IDs → warnings for surviving dangling related references. Owner: program for membership change, caller for semantic reason/decision/veto. No required review result, expected answer or human approval; explicit open-ended operation. Review instructs removal or a related new entry when superseded. Force: enforcing membership change for future JSONL readers; later search depends on cache refresh; no retraction channel for existing context. Epistemic authority: removal does not establish the old claim was false, nor a replacement true. SRC-1: `internal/commands/rm.go`, `internal/storage/storage.go`, `internal/doctrine/review.txt`.

- Immediate return: Removed IDs, dangling-reference warnings or error.
- Later read-back: Surviving corpus excludes removed IDs on direct reads; surviving related fields are not automatically rewritten.
- Delegated visibility: inapplicable — no reviewer or delegation.
- Selection predicate: Explicit resolved ID set; failure of any prefix rejects the requested operation before mutation.
- Invalidation or expiry: Explicit removal, not TTL or machine contradiction detection.
- Activation or effect: Rewrites corpus without selected entries; prior model-window contents and potentially stale cache remain outside that immediate effect.
- Evidence limits: No retained withdrawal reason/tombstone; recovery via external version control. Writing a related replacement instead does not remove the old entry or suppress it in retrieval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if !removeSet[entry.ID] {
> surviving = append(surviving, entry)
> }
> --- `internal/commands/rm.go`

> either remove it ("gn rm") or write a new entry that
> references it ("gn write ... --related <old-id>") explaining what
> changed. Don't leave contradictions in the system.
> --- `internal/doctrine/review.txt`

#### EPI-RTE-cache-refresh
Label: Cache refresh

Distinct cross-cutting freshness function spanning automatic search in [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read) and explicit rebuild in [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance), not a second name for either full route. Endpoints: JSONL snapshot plus mtime → shared-lock read/capture → transaction replacing FTS rows and mtime → later search; automatic path first compares timestamps, explicit reindex bypasses comparison. Owner/evaluator: deterministic program. Target/domain: indexed snapshot identity according to file mtime, not proposition currency or endorsement. Force: enforcing rebuild/skip/error at cache consumer, horizon until next rebuild. Epistemic license: no new body warrant. SRC-1: `internal/index/index.go`, `internal/commands/reindex.go`, `internal/commands/search.go`.

- Immediate return: Rebuild success/error; explicit command reports count/path after another read.
- Later read-back: Derived text/topic rows feed subsequent search invocations.
- Delegated visibility: inapplicable — no agent delegation.
- Selection predicate: Automatic rebuild on unequal/missing stored mtime; explicit rebuild unconditionally copies all decoded entries.
- Invalidation or expiry: Equal mtime skips rebuild; absent JSONL returns success without clearing existing index. Explicit reindex can rebuild an empty corpus, provided database opens successfully.
- Activation or effect: Replacement transaction changes searchable corpus; no semantic reevaluation or automatic acceptance.
- Evidence limits: Equal-mtime external changes and disappeared files can leave stale text. Opening/schema errors stop before repair; malformed JSONL prevents rebuild. Snapshot capture does not make search plus metadata rendering one transaction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if os.IsNotExist(err) {
> // No JSONL file means nothing to index; the index is trivially fresh.
> return nil
> }
> --- `internal/index/index.go`

> if storedMtime == currentMtime {
> return nil
> }
> --- `internal/index/index.go`

Countercase to complete withdrawal: with an existing cached hit and then a removed JSONL file, EnsureFresh returns success; the search query can still read the cached row. Search's subsequent empty ReadAll leaves metadata blank but still prints that hit's ID/snippet. This is a source deduction, not an observed incident. It bounds any claim that successful refresh guarantees currently retained content only.

#### EPI-RTE-test-check
Label: Test check

No counterpart in supplied runtime declarations; runtime mentions tests as evidence but does not declare their check route. Endpoints: test fixtures/expected strings or IDs → Go assertions → test pass/failure → CI command result. Owner/evaluator: Go tests and CI runner; target/domain: exact sanitizer strings, controlled rebuild/search behavior and changed/unchanged mtime cases inspected here. Oracle: test-authored expected values, not external truth evidence. CI triggers on push/pull request; no branch-protection or automatic repair policy established. Force: enforcing test-process result, informational CI result; no inspected effect on entry admission or automatic code adaptation. Scope/horizon: tested fixtures at this revision. SRC-1: `internal/commands/sanitize_query_test.go`, `internal/commands/reindex_test.go`, `internal/index/index_test.go`, `.github/workflows/test.yml`.

- Immediate return: Assertion success/failure if executed, aggregated by go test.
- Later read-back: inapplicable — no retained entry update or learned policy implemented by these tests.
- Delegated visibility: inapplicable — no agent delegation; CI runner is external execution infrastructure.
- Selection predicate: Test definitions selected by go test ./...; this report inspects only named fixture families.
- Invalidation or expiry: Tests/expected values can change through ordinary code development; no runtime semantic expiry.
- Activation or effect: Test logic and CI invocation implemented; no supplied test run, merge veto or automatic revision observed.
- Evidence limits: Tests may show retrieval mechanics on fixtures, not accurate real-world claims, broad recall, process explanations or downstream benefit. No causal component comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if hits[0].EntryID != "cccccc" {
> t.Errorf("expected entry ID %q, got %q", "cccccc", hits[0].EntryID)
> }
> --- `internal/commands/reindex_test.go`

> - run: go test ./...
> --- `.github/workflows/test.yml`

### Claims

#### EPI-CLM-knowledge-continuity
Label: Knowledge continuity

Claim: accumulated knowledge makes later sessions build on previous ones rather than start over; the README's Bleve example predicts a future reader finding prior rationale and avoiding redundant reconsideration or challenging it with a new argument. Doctrine/design claim plus reported self-use, not observed later reliance. Distinct from [RT-CLM-agent-compliance](runtime.md#rt-clm-agent-compliance): this concerns retained-content utility, not every-time instruction compliance. SRC-1: `docs/PRODUCT_STRATEGY.md`, `README.md`.

> It gives AI coding agents a way to accumulate knowledge across sessions so that each session builds on the last instead of starting from zero.
> --- `docs/PRODUCT_STRATEGY.md`

> The next agent (or the next person) that thinks "why not Bleve?" will search, find this, and either move on or come back with an argument the entry doesn't cover.
> --- `README.md`

- claim conclusion status: claimed
- operation conclusion status: uninspected

#### EPI-CLM-review-filter
Label: Review filter

Claim: agent judgment limits entry quality, review catches some noise, and sharper human/empirical-origin doctrine should reduce redundant analysis entries. Doctrine/design with reported efficacy; no measured before/after review comparison. No claim counterpart in supplied runtime; closest [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine) is policy text, not this efficacy assertion. SRC-1: `README.md`, `docs/PRODUCT_STRATEGY.md`.

> Entries are only as good as the agent's judgement about what is worth recording, and that judgement is not perfect. The review step catches some of the noise, but you should expect to prune the odd entry that just restates the code.
> --- `README.md`

> *Structural enforcement (entry templates, source-attribution fields, validation).* Rejected as premature.
> --- `docs/PRODUCT_STRATEGY.md`

- claim conclusion status: claimed
- operation conclusion status: uninspected

### Evidenced absences

#### EPI-ABS-evidence-acceptance
Label: Evidence acceptance boundary

Distinct from the runtime's empty absence section; closest [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission) and [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance) provide operational containers. Searched boundary at SRC-1 revision `429528bf98e424b40837d2dbe3631d0fb42da6fd`: complete CLI dispatch, write, edit, rm, search, show, latest, topics, reindex, storage and index bodies; plan/review doctrine; author helper; executable inventory/search for hook, Register, MCP, provider, embed and exec.Command. Query addressed: is there a target-implemented evidence-consuming acceptance decision over a body's truth, named intended use and scope, followed by integration of an accepted claim? No such implemented route found. Structural branches, caller-controlled persistence, untyped related IDs and mtime checks account for the material transitions found. Doctrinal review names usefulness/origin criteria but requires no recorded evidence-linked truth verdict. No evaluator is invented for this absence.

This supports a bounded negative about inspected Gnosis mechanisms, not about private external agent/human judgments. Transition/check target for the absent phase: a body proposition and its evidence; evaluator, result and force: none found inside the target; operational authority and behavioral-authority path: none found for acceptance as distinct from retention/retrieval. No post-acceptance integration mechanism established. The snapshot has candidates, not acceptance histories. Source passages for branches and disposition are supplied by [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-entry-import](#epi-rte-entry-import), [EPI-RTE-entry-withdrawal](#epi-rte-entry-withdrawal) and [EPI-RTE-cache-refresh](#epi-rte-cache-refresh). SRC-1: `cmd/gn/main.go`, `internal/commands/write.go`, `internal/commands/edit.go`, `internal/commands/rm.go`, `internal/storage/storage.go`, `internal/index/index.go`, `internal/doctrine/review.txt`.

- implementation conclusion status: absent
- external judgment conclusion status: uninspected

### Behavioral-authority paths

none declared in this member; downstream advisory path: see [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). Immediate enforcing/ranking consumers are stated separately in each route above.
