---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Cortex epistemic routes: citation evidence, memory admission, maintenance, behavioral ranking and bounded evaluation."
run-id: AAS-2026-11-07-cortex-6101286707a0-01
reviewed-boundary: "65d449a3275eee51efd6ce0c275572806ee9d553"
---

# Cortex epistemic report

## Source-and-claim boundary

This report asks what Cortex licenses callers to rely on, and which checks actually control that reliance. Scope, exclusions and SRC-1 identity are those of [boundary](boundary.md#boundary-and-evidence); see its [Source register](boundary.md#source-register). All additional reads below use SRC-1 at that same commit. Implementation deductions are not target executions. No production corpus, provider trace, external labels, deployed database or causal comparison is supplied.

The material boundary includes note acquisition and rewriting, reader generation, citation checking and stamping, answer reuse, proposal admission, host maintenance, graph-based selection, watch diagnostics and evaluators. It excludes external assistants' independent reasoning and provider internals, not shipped dashboard callers. [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification) is an explicitly limited warrant claim. [EPI-CLM-drift-check](#epi-clm-drift-check), [EPI-CLM-prediction-gate](#epi-clm-prediction-gate) and [EPI-CLM-correction-chain](#epi-clm-correction-chain) retain other consequential design claims.

| Entry point or operation | SRC-1 source path | Coverage / records | Remaining limit and conclusion prevented |
| --- | --- | --- | --- |
| MCP registration, trusted and guest Ask | `lib/tools.ts`, `lib/ask.ts`, `lib/verify.ts` | Direct registration search, direct Ask/verifier reads and cache branch; [RT-RTE-guest-mediation](runtime.md#rt-rte-guest-mediation), [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer), [EPI-RTE-quote-check](#epi-rte-quote-check), [EPI-RTE-answer-stamp](#epi-rte-answer-stamp), [EPI-RTE-answer-cache](#epi-rte-answer-cache) | No actual answers; no measured correctness |
| Direct read/corpus/context/handoff; working state | `lib/tools.ts`, `lib/brain.ts`, `lib/handoff.ts` | Supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write); direct neighbor ranker read | Detailed note/bubble derivation not independently retraced; prevents complete transformation classification |
| Trusted writes, capture and proposals; console counterparts | `lib/brain.ts`, `lib/proposals.ts`, `lib/proposal-git.ts` | Supplied [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission) | Trusted admission is not a recorded evidence-consuming truth decision |
| Nightly host maintenance | `ops/groundskeeper/SKILL.md` | Direct complete prompt read; [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance), [EPI-CLM-drift-check](#epi-clm-drift-check) | Host configuration, live-state evidence and resulting writes absent; actual checking/acceptance unknown |
| CLI note import and description backfill | `package.json`, `scripts/ingest.mjs`, `scripts/backfill-descriptions.ts` | Direct complete reads; [EPI-RTE-note-import](#epi-rte-note-import), [EPI-RTE-description-backfill](#epi-rte-description-backfill) | Caller input provenance unresolved; no semantic certification |
| Graph derivation and consumer | `lib/edges.ts`, `lib/handoff.ts`, `supabase/migrations/20260909032252_structural_edge_identity.sql` | Direct correction-edge, rebuild/scheduler, SQL v3 and ranker reads; [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild) | Other structural derivers and score-view inputs not fully read; no complete ranking-effect account |
| Watch queue and learning knobs | `lib/inbox.ts`, `lib/learning.ts`, `app/s/[secret]/console/loaders.ts` | Direct check bodies, setting resolver and loader; [EPI-RTE-watch-checks](#epi-rte-watch-checks) | Detailed downstream remediation UI uninspected; diagnostics do not establish corrective execution |
| Retirement CLI | `scripts/lifecycle-sweep.ts`, `lib/lifecycle.ts` | Direct complete reads; [EPI-RTE-retirement-nomination](#epi-rte-retirement-nomination) | RPC body/current schema not fully assessed; candidate eligibility and actual removal cannot be concluded |
| Reader evaluator | `scripts/eval.ts` | Supplied [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation) | Labels/results absent; not independently reread here |
| Prediction evaluator | `scripts/eval-prediction.ts`, `lib/prediction.ts` | Direct complete reads; [EPI-RTE-prediction-evaluation](#epi-rte-prediction-evaluation) | No access history/results; no demonstrated improvement |
| Retrieval evaluator | `scripts/eval-retrieval.ts` | Direct scoring and final gate reads; [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation) | Setup/label filtering and every arm not fully inspected; no system-complete evaluation verdict |
| Split CLI and edge-building driver | `scripts/split-project-page.ts`, `scripts/build-edges.ts` | Split function/write/assertion search only; edge driver uninspected | Byte-preservation claim and all driver paths not assessed; blocks system-complete negative about checked transformations |
| Operations, configuration, update and deployment | `lib/sweep.ts`, `scripts/update.mjs`, `lib/console-job-providers.ts` | Direct sweep read; supplied [RT-RTE-production-jobs](runtime.md#rt-rte-production-jobs), [RT-RTE-capability-configuration](runtime.md#rt-rte-capability-configuration), [RT-RTE-local-update](runtime.md#rt-rte-local-update) | Receipts/provider statuses concern execution, not note truth; no installed outcomes supplied |
| Other setup, health, operational reports, fixtures and historical design | Boundary coverage table paths | Supplied boundary/runtime only, otherwise uninspected | Prevents exhaustive claims about all material source paths; no global absence of acceptance, learning or theory criticism is asserted |

Missing private content prevents identifying the actual propositions stored, not identifying implemented admission and verification rules. Missing traces prevent claims that maintenance, acceptance, ranking adaptation or evaluation operated. Missing comparisons prevent benefit and causal attribution. Missing immutable provider artifacts prevents claims about exact parameter fixity beyond the serving code's lack of parameter-update operations; see [RT-CMP-reader](runtime.md#rt-cmp-reader).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-note](#epi-obj-note) | Caller-authored claims in Markdown | Durable memory | SRC-1 `scripts/ingest.mjs`; see record | Private claims not supplied; no truth inferred from storage |
| [EPI-OBJ-reader-reply](#epi-obj-reader-reply) | Answer propositions, citation and absence assertion | Corpus-based response | SRC-1 `lib/ask.ts`; see record | Semantic relation to inputs indeterminate without actual pair |
| [RT-OBJ-answer-contract](runtime.md#rt-obj-answer-contract) | Policy, not a factual answer | see record | SRC-1 `lib/ask.ts` | Model compliance not established |
| [RT-CMP-reader](runtime.md#rt-cmp-reader) | Opaque distributed-parametric state | see record | SRC-1 `lib/reader.ts` | Exact weights and internals uninspected |
| [EPI-OBJ-note-edges](#epi-obj-note-edges) | Co-read counts and marker/reference relations; ranking weights | Related-note selection | SRC-1 `lib/edges.ts`; see record | Statistical/structural relations do not establish semantic relevance or contradiction |
| [EPI-OBJ-watch-items](#epi-obj-watch-items) | Diagnostic assertions and recommended edits | Advisory maintenance | SRC-1 `lib/inbox.ts`; see record | Symbolic predicates are narrower than some explanatory prose |
| [EPI-OBJ-eval-results](#epi-obj-eval-results) | Conditional recall, judge and floor results | Measurement for maintainers | SRC-1 `scripts/eval-prediction.ts`, `scripts/eval-retrieval.ts`; see record | No measured result supplied |
| [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) | Working-state text, capture and durable-note subparts: see route | see record | SRC-1 `lib/working-state.ts`, `lib/brain.ts` | Container route reference, not an additional object declaration; actual content and transformations unassessed |

## Authority-route ledger

Ledger fields owned by a cited record say “see”; classifications and architectural status below are this report's overlay. A linked route can appear twice when checking, disposition and retention have different functions. “Implemented” denotes inspected source, including explicitly identified supplied implementation findings, never observed use.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer) | content transformation | implemented | [EPI-OBJ-reader-reply](#epi-obj-reader-reply) | truth-apt transformation: indeterminate | Selected notes and question → answer | Provider reader; semantic fidelity requested, not proven | Cache miss, nonempty pack and sufficient deadline | Candidate prose, abstention or malformed reply | Generative | Candidate only; no entailment license | Return answer subject to separate stamps | Calling assistant; tool reply; advisory; current invocation | SRC-1 `lib/ask.ts` | none | none | An answer may merely restate notes or introduce unwarranted content; actual inputs/outputs needed |
| [EPI-RTE-quote-check](#epi-rte-quote-check) | check/evidence production | implemented | [EPI-OBJ-reader-reply](#epi-obj-reader-reply) | no content change | Issued-tag quote against one loaded note block | Deterministic normalization, length and occurrence; authentic loaded snapshot assumed | After structured positive response | Verified boolean, source block, retraction flags | Enforcing evidence classification | Normalized textual occurrence, not source truth or answer entailment | Supplies stamp decision, not permission to write | Ask renderer; structured citation; enforcing; one response | SRC-1 `lib/verify.ts` | [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification) | none | Markup/retraction conventions are not semantic contradiction detection |
| [EPI-RTE-answer-stamp](#epi-rte-answer-stamp) | disposition/acceptance | implemented | [EPI-OBJ-reader-reply](#epi-obj-reader-reply) | no content change | Citation/protocol/coverage classification for display | Code predicates; lexical completeness versus semantic completeness distinguished | After checking or empty/timeout branch | UNVERIFIED, NOT IN BRAIN, VERIFIED, CORRECTED, SUPERSEDED, PARTIALLY VERIFIED | Enforcing label; prose remains visible | Limited textual warrant, or lexical-search-conditioned absence | Changes displayed warning and cache eligibility, not universal suppression | Caller; verdict-first reply; advisory for caller, enforcing for cache; per answer | SRC-1 `lib/ask.ts` | [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification) | none | Not evidence-consuming acceptance of the answer as true |
| [EPI-RTE-answer-cache](#epi-rte-answer-cache) | retention | implemented | [EPI-OBJ-reader-reply](#epi-obj-reader-reply) | no content change | Rendered response → reusable KV answer | stampOf(reply) not UNVERIFIED; optional cache setting | After fresh Ask | Stored reply, including superseded or corrected verdict | Permissive reuse | No additional semantic warrant | Later request may bypass provider and verification | Ask tool; keyed KV reply; enforcing reuse selection; TTL/SHA horizon | SRC-1 `lib/tools.ts` | none | none | NOT IN BRAIN can be retained without semantic completeness proof |
| [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) | disposition/acceptance | implemented | [EPI-OBJ-note](#epi-obj-note) | truth-apt transformation: acquisition/import | Credentialed candidate → writable content | Caller decides; code shape/path/mode/size checks | Trusted write/capture invocation | Commit or error/warning; see route | Enforcing syntactic admission | Imported source warrant unknown; commit is not epistemic acceptance | Candidate becomes later reader/context input | Corpus/context; Git note; permissive admission; future invocations | SRC-1 `lib/brain.ts` | none | none | Capture/edit derivation semantics not independently classified here |
| [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) | retention | implemented | [EPI-OBJ-note](#epi-obj-note) | no content change | Admitted note or working-state item → storage | Git/database mechanics; see route | After successful write | Durable note or separately backed working state | Enforcing persistence boundary | No new truth license | Retained content becomes eligible for later selection | Ask/boot/handoff; stored text; advisory when delivered; across sessions | SRC-1 `lib/brain.ts` | none | none | Index failure can leave committed note; database is separate recovery boundary |
| [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission) | disposition/acceptance | implemented | [EPI-OBJ-note](#epi-obj-note) | truth-apt transformation: acquisition/import | Guest proposal → trusted accept/reject/cancel | Trusted reviewer decides; server publishes receipt protocol | Explicit accept; competing terminal cancellation | Pending, committed, canceled or uncertain | Enforcing authorized publication | Review criteria and evidence use not mandated by protocol | Permits durable import, not automatic truth certification | Later corpus; accepted note/receipt; permissive; future invocations | SRC-1 `lib/proposals.ts` | none | none | Human-only rule belongs to maintenance prompt, not every trusted tool caller |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-note](#epi-obj-note) | truth-apt transformation: non-ampliative reshaping | Stored notes/working items → bounded bundle | Deterministic routing, budgets, pins/scores; see route | Boot/read/corpus/handoff request | Text, excerpts and pointers | Selection and delivery | Source warrant unchanged or unknown; omission disclosed only within route limits | Shapes host input, not host compliance | External assistant; returned context; advisory; invocation plus later reload | SRC-1 `lib/handoff.ts` | none | none | This classification concerns assembly/selection, not every upstream write |
| [EPI-RTE-note-import](#epi-rte-note-import) | content transformation | implemented | [EPI-OBJ-note](#epi-obj-note) | truth-apt transformation: acquisition/import | Local text → Git Markdown plus provenance warning | Operator commit flag, extension/size/collision checks | CLI --commit | Imported file or individual failure | Enforcing structural checks | Source warrant explicitly unknown | New note can enter future corpus | Corpus reader; Git file; permissive; until edited | SRC-1 `scripts/ingest.mjs` | none | none | Not verification history; separate source files are not authenticated |
| [EPI-RTE-description-backfill](#epi-rte-description-backfill) | content transformation | implemented | [EPI-OBJ-note](#epi-obj-note) | truth-apt transformation: acquisition/import | Supplied description/tags → new frontmatter | Caller supplies metadata; code checks roundtrip and original suffix | CLI --apply; missing existing description | Local file written or abort | Enforcing serialization/preservation checks | Imported metadata warrant unknown; note text preserved | New metadata can shape router selection after publication | Router; note frontmatter; ranking/selection; future reads | SRC-1 `scripts/backfill-descriptions.ts` | none | none | No code-level semantic agreement test between description and body |
| [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance) | check/evidence production | doctrine only | [EPI-OBJ-note](#epi-obj-note) | no content change | Live-state-dependent note claims versus PR/branch/URL/deployment evidence | Host agent directed to re-verify; tools/evidence externally supplied | Health success; bounded recurring review | Requested corrections/unverified annotations/verification dates | Procedural model/human interpretation | Criteria are live-state agreement, intended use is cross-device memory; actual acceptance not supplied | May motivate trusted writes; server does not enforce prerequisite | Host agent; skill; advisory/procedural; nightly if installed | SRC-1 `ops/groundskeeper/SKILL.md` | [EPI-CLM-drift-check](#epi-clm-drift-check) | none | Accessible instructions, not a running evaluator |
| [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance) | lifecycle integration | doctrine only | [EPI-OBJ-note](#epi-obj-note) | truth-apt transformation: indeterminate | Daily logs/live checks → filed pages, markers and digest | Host model requested to preserve history and mark uncertainty | After requested verification/filing | Requested connected corrections and absorption markers | Procedural | Integration after actual acceptance not established | Can change future retained content if executed | Later context/Ask; notes/digest; advisory; future sessions | SRC-1 `ops/groundskeeper/SKILL.md` | [EPI-CLM-drift-check](#epi-clm-drift-check) | none | Requested workflow order does not evidence accepted ampliative claims |
| [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild) | behavior/policy adaptation | implemented | [EPI-OBJ-note-edges](#epi-obj-note-edges) | non-truth-apt policy/content update: trace-derived ranking weights | Eligible access windows → graph weights → neighbor ranking | SQL bounded counts and fixed ranker; no truth oracle | Deferred corpus-triggered refresh or explicit rebuild | Replaced graph or stale/busy/capacity/current outcome | Enforcing graph admission, ranking force downstream | Co-access licenses a count, not importance/truth | Can change tiebreak/fallback neighbor selection | Handoff; note_edges plus scores; ranking; until refresh | SRC-1 `lib/edges.ts` | none | none | No improved future capacity demonstrated; final bundle budget may omit ranked neighbors |
| [EPI-RTE-watch-checks](#epi-rte-watch-checks) | check/evidence production | implemented | [EPI-OBJ-watch-items](#epi-obj-watch-items) | truth-apt transformation: entailed derivation | Markers/references/coaccess thresholds/bytes → diagnostic predicates | Deterministic text and numerical rules; not general semantic evaluator | Enabled checks on console load | Advisory watch items; failure can yield empty list | Advisory | Predicate-level relation only; stronger prose separately assessed | Invites manual correction, linking or splitting; does not execute it | Console badge/queue; TriageItem; advisory; one render | SRC-1 `lib/inbox.ts` | [EPI-CLM-correction-chain](#epi-clm-correction-chain) | heuristic explanation exceeds predicate | No temporal ordering or logical inconsistency follows from mutual references |
| [EPI-RTE-prediction-evaluation](#epi-rte-prediction-evaluation) | check/evidence production | implemented | [EPI-OBJ-eval-results](#epi-obj-eval-results) | truth-apt transformation: entailed derivation | Prior-history rankings versus hidden hour's accessed set | Deterministic recall@5/@10; access is proxy target | Manual CLI with database history | Printed ranker means/wins/ties/losses | Advisory; no ranking promotion | Conditional replay fit on selected windows, not semantic usefulness | Can inform maintainer; no automatic successor installation | Maintainer; stdout; advisory; evaluated history only | SRC-1 `scripts/eval-prediction.ts` | [EPI-CLM-prediction-gate](#epi-clm-prediction-gate) | gate is declared promotion policy, not automatic selection | Current structural graph is anachronistic; baseline historical temperatures unavailable |
| [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation) | check/evidence production | implemented | [EPI-OBJ-eval-results](#epi-obj-eval-results) | truth-apt transformation: entailed derivation | Expected path/phrase versus ranked pack | Code rank-hit and phrase checks; supplied labels are oracle | Manual CLI, optional min-recall floor | Metrics; nonzero exit on floor breach | Enforcing process status only when floor set | Recall over selected labels, not answer correctness | Stops successful command exit, not universal production admission | Invoker; stdout/exit; enforcing local threshold; command horizon | SRC-1 `scripts/eval-retrieval.ts` | none | none | External labels and complete pipeline setup not supplied/fully inspected |
| [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation) | check/evidence production | implemented | [EPI-OBJ-eval-results](#epi-obj-eval-results) | no content change | Answer/source/stamp versus labels and judge panel | see record | Bounded evaluation invocation | Scored JSON, stale labels, null judge or errors | Advisory | Label-relative answer agreement; no causal component effect | No automatic reader installation | Maintainer; output JSON; advisory; corpus/label-hash bound | SRC-1 `scripts/eval.ts` | none | none | Supplied implementation finding; no results |
| [EPI-RTE-retirement-nomination](#epi-rte-retirement-nomination) | disposition/acceptance | implemented | [EPI-OBJ-note](#epi-obj-note) | no content change | Notes → nomination queue, not deletion | RPC request and CLI result-shape checks; substantive predicate unassessed | --propose; otherwise report only | Nominations and undecided-candidate listing | Advisory | Use/age nomination does not withdraw factual warrant | Person may later decide; CLI does not remove note | Maintainer; report/database queue; advisory; until decision | SRC-1 `scripts/lifecycle-sweep.ts` | none | none | No inspected deletion consumer or complete eligibility proof |
| [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild) | content transformation | implemented | [EPI-OBJ-note-edges](#epi-obj-note-edges) | truth-apt transformation: entailed derivation | Eligible recorded access windows → pair count | SQL distinct-hour joins/count; scoped to recorded history, not inferred usefulness | Rebuild after identity and capacity checks | Coaccess count/evidence row | Deterministic derivation | Count of bounded recorded coaccess; input authenticity assumed | Supplies later ranking/watch inputs | Graph consumers; count/weight; ranking and advisory; until rebuild | SRC-1 `supabase/migrations/20260909032252_structural_edge_identity.sql` | none | none | A derived count does not establish a user's need or semantic relation |
| [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild) | retention | implemented | [EPI-OBJ-note-edges](#epi-obj-note-edges) | no content change | Derived rows → replaced Postgres graph | SQL transaction, corpus/usage/structure identity and locks | Successful rebuild publication | Persisted rows and freshness state | Enforcing replacement protocol | No additional factual endorsement | Later handoff/watch can read retained graph | Handoff/watch; database rows; ranking/advisory; across invocations | SRC-1 `supabase/migrations/20260909032252_structural_edge_identity.sql` | none | none | Retention is not lifecycle integration of accepted factual claims |
| [EPI-RTE-answer-cache](#epi-rte-answer-cache) | operational admission/selection/consumption | implemented | [EPI-OBJ-reader-reply](#epi-obj-reader-reply) | no content change | Matching question/policy/snapshot → stored reply | Code cache-key lookup, not renewed truth evaluation | Enabled cache hit before model call | Redacted reply plus cached/no-model-call disclosure | Enforcing selection | Original stamp's limited license only | Bypasses fresh provider/checking on that hit | Requesting caller; tool reply; advisory content; TTL/SHA horizon | SRC-1 `lib/tools.ts` | none | none | Actual reuse and downstream reliance unobserved |

Operational receipts are a separate check domain, not a hidden truth evaluator: see [RT-RTE-production-jobs](runtime.md#rt-rte-production-jobs), [RT-RTE-capability-configuration](runtime.md#rt-rte-capability-configuration) and [RT-RTE-local-update](runtime.md#rt-rte-local-update) for their owners, vetoes, confirmation, recovery and horizons. Directly inspected SRC-1 `lib/sweep.ts` computes monitor transitions and queues/delivers alerts; a provider mail result concerns delivery, not whether a note is true. These paths may change production machinery under operator authority; they do not establish evidence-responsive autonomous improvement.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification) | see record | SRC-1 `lib/ask.ts`, `lib/verify.ts`; implementation and design | Narrow text-presence disclaimer | [EPI-RTE-quote-check](#epi-rte-quote-check), [EPI-RTE-answer-stamp](#epi-rte-answer-stamp) | None supplied | No truth or entailment experiment | Normalized block occurrence is checked and limited stamp rendered | Source truth, semantic currency and answer fidelity remain separate |
| [EPI-CLM-drift-check](#epi-clm-drift-check) | see record | SRC-1 `ops/groundskeeper/SKILL.md`; doctrine/design | Health-first verification/correction procedure | [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance) is a host procedure, not an implemented scheduler | None supplied | No installation, live evidence or outcomes | A procedure requests rechecking, preserves history and records uncertainty | Actual evidence-consuming acceptance and effective drift correction unknown |
| [EPI-CLM-prediction-gate](#epi-clm-prediction-gate) | see record | SRC-1 `scripts/eval-prediction.ts`; doctrine/design versus implementation | Challenger should beat incumbent before promotion | [EPI-RTE-prediction-evaluation](#epi-rte-prediction-evaluation), [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild) | None supplied | Baseline is proxy, present graph used for historical windows, no intervention isolating components | Replay machinery compares two rankers; live ranker uses score then blend | Script does not promote; claim of past winner remains attributed commentary |
| [EPI-CLM-correction-chain](#epi-clm-correction-chain) | see record | SRC-1 `lib/inbox.ts`; implementation-generated explanation | Mutual correction references presented as repeated re-correction | [EPI-RTE-watch-checks](#epi-rte-watch-checks) | None supplied | No date/order or proposition comparison | Detects reciprocal correction-marker path references and suggests review | Does not establish that current truth lives in neither page alone |

## Bounded conclusion

Cortex acquires caller text and makes it available across sessions. Trusted writes and trusted acceptance of guest proposals confer operational admission, not necessarily epistemic acceptance. Their mechanisms can reject malformed or unauthorized input and support receipts/recovery without judging factual truth. Imported files explicitly retain a warning that they lack verification history. Description backfill checks preservation and serialization, not whether a supplied description accurately characterizes its note. See [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), [EPI-RTE-note-import](#epi-rte-note-import) and [EPI-RTE-description-backfill](#epi-rte-description-backfill).

The reader produces candidate answers; actual content relations are indeterminate without input/output pairs. Requested faithful paraphrase is a countercase to classifying all generation as ampliative conjecture. Conversely, a real quote can accompany an answer not entailed by it. The implemented checker licenses textual occurrence at a snapshot, and the renderer consumes that check to distinguish limited warrant, retraction, ambiguity and failure. An UNVERIFIED answer remains visible but is not eligible for answer caching. Other stamps, including SUPERSEDED and lexical-coverage-conditioned NOT IN BRAIN, can be retained and replayed. Caching preserves the verdict and its limitations; it does not supply a second semantic check. See [EPI-RTE-quote-check](#epi-rte-quote-check), [EPI-RTE-answer-stamp](#epi-rte-answer-stamp), [EPI-RTE-answer-cache](#epi-rte-answer-cache) and [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification).

Deterministic predicates can derive narrower claims from inspected representations: a normalized quote occurs in a block; two paths recur in bounded eligible access windows; a labeled target occurs in a top-k list. These derivations depend on authentic input snapshots, correct encoding and the named comparison domain. They do not warrant world facts, explanation or transfer. The watch queue's reciprocal-marker explanation outruns its predicate, so it should be read as a review suggestion, not evidence of contradiction or temporal supersession. See [EPI-RTE-watch-checks](#epi-rte-watch-checks), [EPI-CLM-correction-chain](#epi-clm-correction-chain) and [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild).

The groundskeeper requests the closest thing here to evidence-consuming fact acceptance: compare live-state-dependent claims with live evidence, correct in place, mark unresolved claims unverified, and then retain changes for cross-device use. That is doctrine with a named intended use and scope; neither actual evidence consumption nor accepted ampliative production/integration is demonstrated. Direct-write authority remains broader than this procedure. See [EPI-CLM-drift-check](#epi-clm-drift-check) and [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance).

Trace-derived graph weights have an implemented later ranking consumer even without a new factual claim. This is a bounded behavior-shaping capacity, not demonstrated improved capacity for future action. The replay evaluator measures access-set prediction, not usefulness, and does not install a winner. Reader and retrieval evaluations have separate reference targets and consumers; none supplies production-wide semantic acceptance. See [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild), [EPI-RTE-prediction-evaluation](#epi-rte-prediction-evaluation), [EPI-RTE-retrieval-evaluation](#epi-rte-retrieval-evaluation) and [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation).

Learning benefit remains unestablished for those ranking changes; parameter learning is uninspected at providers and not implemented by inspected serving code. Reflection and formulated-theory criticism are not inferred from correction markers, logs, mutable weights or the name “learning.” Some method instructions are localized and behavior-directing, but evidence that their own content is criticized and revised through retained results is not supplied. Automation of graph rebuilding is independent of autonomous theory building; host maintenance requires external configuration and opaque execution. No exercised self-improvement attribution follows: no subsequent operation trace causally depends on an evidence-shaped organizational update. These are separate bounded limits, not a system-wide negative; coverage gaps above prevent a complete negative about all theory or acceptance routes.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-note
Label: Markdown note

Source-native identity: Markdown files under notes/projects and imported local text. Natural-language propositions are interpreted by readers; frontmatter/path fields have symbolic selection consumers. Substrate: private GitHub notes repository, later loaded corpus snapshot. Distinct from [RT-OBJ-answer-contract](runtime.md#rt-obj-answer-contract): retained user content rather than shipped reader policy. Closest supplied mechanisms are [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); these are routes, not duplicate note objects. SRC-1 `scripts/ingest.mjs`, `lib/brain.ts`; imported-text warning retained under [EPI-RTE-note-import](#epi-rte-note-import). Actual proposition identity and source warrant are unknown without the private corpus.

#### EPI-OBJ-reader-reply
Label: Reader answer and citation

Source-native identity: parsed answer/tag/quote and rendered answer. Natural-language answer/evidence plus symbolic protocol, citation and coverage fields. Substrate: request state; rendered reply optionally in KV. Distinct from [RT-OBJ-answer-contract](runtime.md#rt-obj-answer-contract), which is the instruction that precedes generation; [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer) is its producing route, not an object counterpart. SRC-1 `lib/ask.ts`, `lib/tools.ts`. Split checks/consumers are [EPI-RTE-quote-check](#epi-rte-quote-check), [EPI-RTE-answer-stamp](#epi-rte-answer-stamp) and [EPI-RTE-answer-cache](#epi-rte-answer-cache). No supplied answer instance proves operation.

#### EPI-OBJ-note-edges
Label: Note edges

Source-native identity: `note_edges` rows with src/dst/kind/weight/evidence/built_head. Symbolic tuples and numerical ranking weights, not distributed model parameters; evidence strings are natural language for people. Substrate: Postgres and returned edge rows. Closest supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) consumes neighbors but is not this stored object. SRC-1 `lib/edges.ts`, `supabase/migrations/20260909032252_structural_edge_identity.sql`. Derivation and downstream ranking passages in [EPI-RTE-edge-rebuild](#epi-rte-edge-rebuild) support the distinct identity.

#### EPI-OBJ-watch-items
Label: Watch items

Source-native identity: `TriageItem` arrays derived by watchItems. Symbolic severity/kind/loc and natural-language why/action/evidence interpreted by the console operator. Substrate: per-request derived memory, not a durable accepted-claim ledger. Distinct from supplied proposal queue and reader results: diagnostic suggestions, not candidates awaiting trusted note admission. SRC-1 `lib/inbox.ts`, `app/s/[secret]/console/loaders.ts`; see [EPI-RTE-watch-checks](#epi-rte-watch-checks).

#### EPI-OBJ-eval-results
Label: Evaluation results

Source-native identity: prediction tallies, retrieval ArmResult and reader scored rows. Symbolic metrics/labels/verdicts with natural-language questions/answers. Substrate: evaluator stdout and, for supplied reader route, output JSON. Closest supplied [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation) produces one subset, not this cross-evaluator object; no supplied object counterpart. SRC-1 `scripts/eval-prediction.ts`, `scripts/eval-retrieval.ts`; see their separately declared routes for target-specific checks. No score artifact is supplied.

### Routes

#### EPI-RTE-quote-check
Label: Quote verification

Part of: [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer)

Endpoints: structured positive reply → issued tag resolved to packed path → checkCitation/verifyQuote → citation object. Owner: Ask/verifier code. Context is the scoped corpus snapshot, not external truth. This is the checking part of the supplied reader route, distinct from its disposition and retention. SRC-1 `lib/ask.ts`, `lib/verify.ts`.

Concrete static deduction, not execution: with source block `The oven is lit.` and quote `The oven is lit.`, normalization leaves the sentence unchanged, length exceeds twelve, and one block includes it; verified becomes true. With answer `The oven is cold.` attached to that same quote, the verifier follows exactly the same path because it takes text and quote, not answer. Thus a genuine occurrence does not entail the answer. A quote `lit` fails the normalized length guard. This countercase limits the license even where source truth is warranted.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Citation boolean/reason, source-owned block, heading/line, retraction classification and snapshot identifier.
- Later read-back: inapplicable — this check itself retains nothing; rendered reply retention is a separate part.
- Delegated visibility: Renderer and structured consumers receive the citation; provider supplies no authoritative source path.
- Selection predicate: Issued tag and nonblank quote after parse; normalized length at least MIN_QUOTE and occurrence inside one block.
- Invalidation or expiry: Corpus changes require checking against that snapshot; nearby banner/was markers affect classification, not occurrence boolean.
- Activation or effect: Result directly controls stamp branch; answer truth is not checked.
- Evidence limits: Implementation deduction only; normalization, marker radius and authentic corpus bound the check.

> export function verifyQuote(text: string | undefined, quote: string): Verdict {
> --- `lib/verify.ts`

> if (!normalise(b.text).includes(nq)) continue;
> --- `lib/verify.ts`

#### EPI-RTE-answer-stamp
Label: Answer stamp disposition

Part of: [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer)

Endpoints: protocol/coverage/citation → renderFull or renderBare → caller-visible label and prose. Owner: deterministic Ask renderer. This part is distinct from [EPI-RTE-quote-check](#epi-rte-quote-check), whose result it consumes. SRC-1 `lib/ask.ts`. The model proposes; code decides labels; no human veto is required before response. No answer oracle. Open-question mode. Intended use is communicating limited evidence to a caller, not accepting a factual claim into a truth ledger.

A false-positive-semantic-absence countercase remains possible: an omitted note can paraphrase the answer with no lexical overlap. Hence the code's complete predicate proves its lexical criterion, not semantic exhaustion. The empty-scoped-corpus branch is a genuine narrower absence case; timeout or no fitting note is not conflated with it.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verdict-first rendered answer; source evidence when citations enabled; unproven prose is still returned.
- Later read-back: Rendered verdict may be reused by the separate cache route.
- Delegated visibility: Caller receives limited warrant/warnings; citation suppression removes fields, not every possible prose disclosure.
- Selection predicate: Protocol warning, unresolved tag, notInBrain, verification/outside-pack, correction/retraction and multiplicity branches in order.
- Invalidation or expiry: Snapshot-specific; notInBrain requires valid abstention and coverage.complete, except explicit empty scoped corpus.
- Activation or effect: Label changes display and cache eligibility; retraction warning is advisory to the caller.
- Evidence limits: No semantic entailment evaluator or semantic completeness proof in these branches; calling agent's compliance unobserved.

> complete: omittedNotes === 0 || unreadMatched === 0,
> --- `lib/ask.ts`

> const notInBrain = protocol === "abstention" && coverage.complete;
> --- `lib/ask.ts`

> SUPERSEDED — the supporting passage is marked as retracted.
> --- `lib/ask.ts`

#### EPI-RTE-answer-cache
Label: Answer reuse admission

Part of: [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer)

Endpoints: rendered answer → stamp filter → KV write; matching future call → cached redacted reply. Owner: trusted/guest Ask handlers and cache adapter. A retention/selection part, not an additional semantic check. SRC-1 `lib/tools.ts`; key and TTL contract also supplied by [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer). Software admits all non-UNVERIFIED stamps when enabled; no per-content human approval, model judge or expected-answer oracle. Recovery/withdrawal is key generation, expiry, disabling or clearing, not retraction of prior delivered answers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Fresh rendered answer, or cached answer with cache/no-model-call disclosure.
- Later read-back: Key-matching later request receives retained reply without provider or renewed citation verification.
- Delegated visibility: Requesting client receives reply; cache hit sends no note pack to provider.
- Selection predicate: Enabled cache and matching normalized question/SHA/model/k/door/scope/citations/pipeline identity; non-UNVERIFIED stamp for write.
- Invalidation or expiry: TTL, changed key inputs, disabled cache or clear action; no answer-specific truth withdrawal demonstrated.
- Activation or effect: Can replace an inference with old rendered answer; stores negative/superseded verdicts too.
- Evidence limits: Real reuse and cache integrity unobserved; retention preserves limits of original verdict, not truth.

> if (key && stampOf(reply) !== "UNVERIFIED") {
> --- `lib/tools.ts:303-303`

#### EPI-RTE-note-import
Label: Local folder import

Endpoints: local folder → extension/size/path/collision plan → --commit → GitHub Contents API → later corpus. Owner: operator invokes the CLI; file content comes from disk, not model generation. Distinct from [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write): direct CLI API writes bypass tool-side index regeneration. SRC-1 `scripts/ingest.mjs`. Admission is operator batch permission plus syntactic checks; no semantic oracle. Each file can fail independently and successful files remain; Git history permits external recovery, no automatic all-file rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dry-run plan or per-file success/failure counts.
- Later read-back: Written notes become corpus inputs; index is regenerated by a subsequent server write, not this CLI.
- Delegated visibility: GitHub receives content; no provider invoked by import.
- Selection predicate: Top-level .md/.markdown/.txt, size at most 256 KiB, notes/projects destination, collision-free slug.
- Invalidation or expiry: No automatic semantic expiry; later Git edits or external recovery replace content.
- Activation or effect: Operationally admits imported text without verification history; subsequent use unobserved.
- Evidence limits: Filename/date provenance is not source authentication or fact checking; source warrant remains unknown.

> Review before trusting: ingested text has no verification history.
> --- `scripts/ingest.mjs`

#### EPI-RTE-description-backfill
Label: Description frontmatter backfill

Endpoints: caller JSON descriptions/tags plus local notes → applyDescription → roundtrip/suffix/frontmatter checks → optional local write. Owner: operator and deterministic script. Distinct from [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write): a local metadata-edit driver with its own verification and --apply gate. SRC-1 `scripts/backfill-descriptions.ts`. JSON authorship is unresolved; imported metadata may be truth-apt but is not newly inferred by this script. Checks can veto before a file write; failures abort, not roll back earlier files. No answer oracle or semantic agreement test.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Changed/missing/already counts or thrown assertion.
- Later read-back: After publication/local corpus use, note metadata can affect router selection; publication itself is not performed here.
- Delegated visibility: No model call; local files receive metadata.
- Selection predicate: Input JSON paths whose note lacks an existing description; --apply permits writing.
- Invalidation or expiry: Existing description skipped; subsequent metadata edit needed to revise it.
- Activation or effect: Checks description roundtrip, preserved original suffix, exactly one frontmatter block; does not verify metadata truth.
- Evidence limits: applyDescription internals not independently retraced; asserted input/output properties are visible in caller.

> if (!after.endsWith(before)) {
>     throw new Error(`${item.path}: original note text is not preserved verbatim`);
>   }
> --- `scripts/backfill-descriptions.ts`

#### EPI-RTE-edge-rebuild
Label: Usage graph rebuild and ranking

Endpoints: loaded corpus → deferred refresh/freshness identity → bounded structural derivation and SQL coaccess replacement → note_edges → rankNeighbours → budgeted handoff. Owner: code/SQL, not reader model. Distinct route spanning supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write): graph is a separate retained ranking input, not note text or ordinary write admission. SRC-1 `lib/edges.ts`, `lib/handoff.ts`, `supabase/migrations/20260909032252_structural_edge_identity.sql`.

Software proposes/admits deterministic rows; stale identities, locking and capacity can veto publication. No human per-edge approval or truth oracle. Current corpus observations can schedule another refresh; fixed policy is 90 days of completed UTC hours, excluding boot/handoff/maintenance, at most six distinct paths/hour and at least two shared windows. This filters pushed bundles out of the usage signal; it does not authenticate that recorded access represented usefulness. Replacement is transaction-scoped; failed HTTP can leave outcome unknown until freshness recheck. Guidance is fixed weights/policy, not retained explanatory theory criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rebuild/current/off/missing/stale/busy/capacity/time-budget result; deferred callers do not wait for usefulness evidence.
- Later read-back: Postgres edges reach later handoff neighbor ranking and console watch checks.
- Delegated visibility: Handoff receives ranked excerpts after admission budgets; model weights are not modified.
- Selection predicate: Fresh corpus/usage/structural identity; bounded eligible coaccess; neighbor score descending, blend tiebreak/fallback.
- Invalidation or expiry: Rebuild replaces rows; corpus SHA, cutoff/watermark and structure version determine freshness; stale confirmed graph may remain after failed refresh.
- Activation or effect: Implemented ranking consumer can change later delivered neighbors; actual changed delivery and benefit unobserved.
- Evidence limits: Score-view inputs and all structural derivers not fully inspected; no causal comparison establishes improved capacity.

> if expected_watermark is distinct from identity->>'watermark'
>     or expected_cutoff is distinct from (identity->>'cutoff')::timestamptz then return 'stale-input'; end if;
> --- `supabase/migrations/20260909032252_structural_edge_identity.sql`

> group by a.path,b.path having count(*)>=2;
> --- `supabase/migrations/20260909032252_structural_edge_identity.sql`

> .sort((a, b) => b.score - a.score || b.blend - a.blend || byName(a.path, b.path))
> --- `lib/handoff.ts`

#### EPI-RTE-watch-checks
Label: Mechanical watch diagnostics

Endpoints: corpus plus optional coaccess graph and knobs → watchItems → settled-history filter → shared console loader → badge/queue. Owner: deterministic check code. No counterpart in supplied runtime: different target and advisory consumer from [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer) and [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission). SRC-1 `lib/inbox.ts`, `lib/learning.ts`, `lib/edges.ts`, `app/s/[secret]/console/loaders.ts`.

Targets split by predicate: live references to a frontmatter-SUPERSEDED note; mutually top-three floor-passing co-read pairs with neither link/path/live name mention; reciprocal correction-marker path references; oversized non-log/non-history pages. Software proposes suggestions; the operator determines whether to edit. No reference-answer oracle. Suggestions request linking, chain collapse or splitting; no write follows merely from deriving an item. Correction edges scan marker-bearing blocks for live paths, not compared propositions or timestamps. Thus reciprocal historical bookkeeping is a countercase to assuming current contradictions. Diagnostic text is also redacted/bounded before delivery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: TriageItem list after enabled-check and decays:false filtering; unavailable loader returns empty list.
- Later read-back: inapplicable — items are recomputed, not retained accepted claims; underlying notes/edges persist separately.
- Delegated visibility: Console receives evidence/why/action; no model call in check derivation.
- Selection predicate: Per-check predicates and switches; coaccess floor precedes mutual ranking; either settled endpoint suppresses pair.
- Invalidation or expiry: Resolved predicate, changed metadata, disabled switch or unavailable store can remove suggestion; disappearance is not acceptance.
- Activation or effect: Advisory console output; no automatic claim revision, retirement or contradiction resolution.
- Evidence limits: Output prose may overinterpret markers; complete downstream remediation UI not inspected; no corrective execution supplied.

> if (!isBannerText(b.text) && !WAS_MARK.test(b.text)) continue;
> --- `lib/edges.ts`

> if (!back) continue;
> --- `lib/inbox.ts`

> return items.filter((i) => !onSettledNote(i.loc, files));
> --- `lib/inbox.ts`

> console.error(`[inbox] watch items unavailable — the queue renders without them: ${String(e)}`);
>     return [];
> --- `app/s/[secret]/console/loaders.ts`

#### EPI-RTE-prediction-evaluation
Label: Prediction replay measurement

Endpoints: paginated access history with pinned upper ID + current local corpus → historical window masking → baseline/candidate ranking → recall comparison → stdout. Owner: deterministic CLI. Distinct from supplied [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation): no reader/judge model, different target and oracle. SRC-1 `scripts/eval-prediction.ts`, `lib/prediction.ts`.

Reference outcome is the recorded accessed set of a hidden completed 2–6-note hour; proposer is fixed algorithm code, evaluator is recall arithmetic, operator can choose whether any future code change is adopted. Bounded offline replay mode. No automatic ranking promotion, production veto or rollback is implemented by the CLI. Baseline reconstructs recency/frequency from earlier rows, not historical live temperatures. Candidate coaccess is prior-window-bounded, but links/tags and available endpoints use today's local corpus. A rank improvement would license only measured proxy fit, not semantic relevance, causal component effect or transfer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranker means, wins/ties/losses and methodological disclosure on stdout, or error.
- Later read-back: inapplicable — no retained result writer or automatic promotion consumer in this CLI; maintainers can separately retain output.
- Delegated visibility: No provider calls; database history reaches local process.
- Selection predicate: Non-pushed eligible history, completed 2–6-note windows with prior history; current local corpus for structural data.
- Invalidation or expiry: Different history/corpus/policy requires new evaluation; upper ID bounds appended rows but not concurrent edits.
- Activation or effect: Produces comparative evidence for a human, not a successor installation.
- Evidence limits: No input history/results supplied; hour is a session proxy and present structural graph is not historical.

> No ranking is promoted by this command.
> --- `scripts/eval-prediction.ts`

> const b5 = recallAtK(basePred, w.paths, 5);
>     const b10 = recallAtK(basePred, w.paths, 10);
>     const c5 = recallAtK(candPred, w.paths, 5);
>     const c10 = recallAtK(candPred, w.paths, 10);
> --- `scripts/eval-prediction.ts`

#### EPI-RTE-retrieval-evaluation
Label: Retrieval recall and floor

Endpoints: externally labeled question/expected path/optional phrase → selected retrieval arms → summarise → metrics and optional exit floor. Owner: deterministic harness. Distinct from [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation) and [EPI-RTE-prediction-evaluation](#epi-rte-prediction-evaluation): evaluates candidate-pack membership, not answer quality or future access. SRC-1 `scripts/eval-retrieval.ts`.

External label authorship is uninspected; expected path/phrase is the oracle, not a model judgment. Software compares fixed candidates; operator chooses labels/flags and any resulting revision. Optional floor tests incumbent rank-only recall, not strict phrase hits. Failure exits nonzero; only an external invoker could make that a deployment veto. No automatic candidate promotion or content rollback occurs in inspected final gate.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-arm rank-only/strict recall and pack diagnostics; floor breach exit 1 when requested.
- Later read-back: inapplicable — inspected output/gate emits stdout and process status, not a retained-learning writer.
- Delegated visibility: No judge in inspected scoring; optional remote retrieval adapters not fully assessed here.
- Selection predicate: Arm-returned ranked expected path within k; optional all-phrase check for strict hit; floor uses incumbent rankHits/total.
- Invalidation or expiry: Corpus/label/flag changes alter target; pipeline setup and label filtering not fully inspected.
- Activation or effect: Conditional local process failure can block an external caller's continuation; universal deployment force unestablished.
- Evidence limits: Scoring/final-gate inspection only; no label/results artifact, no complete arm audit or causal attribution.

> const rankHit = rank != null && rank <= k;
> --- `scripts/eval-retrieval.ts`

> const got = incumbent.total ? incumbent.rankHits / incumbent.total : 0;
> --- `scripts/eval-retrieval.ts`

> console.error(
>         "The misses above are the whole list. Either retrieval got worse or the corpus outgrew " +
>           "what the current constants carry; both are real, and neither fixes itself."
>       );
>       process.exit(1);
> --- `scripts/eval-retrieval.ts`

#### EPI-RTE-retirement-nomination
Label: Retirement nomination request

Endpoints: CLI --propose → propose_deletions RPC → database nominations → undecided candidate report. Owner: operator initiates, database proposes; script checks result shapes. No supplied record counterpart; this is not [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)'s guest-content acceptance queue. SRC-1 `scripts/lifecycle-sweep.ts`, `lib/lifecycle.ts`.

Mode is optional nomination/report, not automatic factual withdrawal. No model or answer oracle. Substantive age/use eligibility is stated in comments but current RPC body not fully assessed here. A later person may decide; no deletion operation is implemented in this inspected CLI. This is a consequential cleanup countercase to treating a retirement label as executed forgetting.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Nomination count and temperature/undecided-candidate report, or schema/HTTP error.
- Later read-back: Nomination rows can be read by later CLI reports; script does not turn them into note deletion.
- Delegated visibility: Database receives min_age_days; terminal receives candidate reasons.
- Selection predicate: --propose gates request; report selects decision=is.null; detailed RPC eligibility unassessed.
- Invalidation or expiry: Decision non-null removes a candidate from this report; no factual retraction or automatic expiry proved here.
- Activation or effect: Requests nominations only; no note removal or prevention of reader access in this CLI.
- Evidence limits: Remote function definition/current deployment and later human action not fully assessed; no observed withdrawal.

> "deletion_candidates?select=path,reason&decision=is.null"
> --- `scripts/lifecycle-sweep.ts`

> There is deliberately no flag
>  * here that deletes anything.
> --- `scripts/lifecycle-sweep.ts`

### Claims

#### EPI-CLM-drift-check
Label: Nightly drift checking

Claimed operation: groundskeeper re-verifies live-state-dependent claims, corrects history visibly, marks unverifiable content and dates clean pages. SRC-1 `ops/groundskeeper/SKILL.md`, doctrine/design. Closest supplied [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance) is the procedure route; this claim object is not a second route. No supplied claim counterpart after comparison with [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification), which concerns answer citations rather than external fact checking.

> Re-verify
> claims that depend on live state (PRs, branches, URLs, deployments). Correct
> in place with `(was: … — updated <date>)`; mark what you cannot verify
> `(unverified <date>)`; end clean pages with `_Facts last verified <date>._`
> --- `ops/groundskeeper/SKILL.md`

#### EPI-CLM-prediction-gate
Label: Prediction ranking gate

Claimed operation: challenger ranking ships only after beating the incumbent on prediction replay; module comments attribute incumbent choice to an earlier comparison. SRC-1 `scripts/eval-prediction.ts`, `lib/prediction.ts`, doctrine/design and attributed reported operation, not supplied observed execution. Distinct from [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation): this claim concerns handoff selection promotion rather than answer measurement. No supplied claim counterpart.

> a ranking ships only if it beats the incumbent HERE, the
>  * same rule eval-retrieval enforces for narrowing.
> --- `scripts/eval-prediction.ts`

> THE MEASURED VERDICT: the candidate blend did not beat the recency-and-frequency baseline,
>  * so the incumbent stands.
> --- `lib/prediction.ts`

The code prints results and an adoption rule; it does not perform adoption. This distinction preserves the design claim without turning historical commentary into run evidence.

#### EPI-CLM-correction-chain
Label: Correction chain explanation

Claimed operation/warrant: reciprocal correction references imply the pages have re-corrected each other and current truth lives in neither alone. SRC-1 `lib/inbox.ts`, implementation-generated explanatory prose. Distinct from [RT-CLM-quote-verification](runtime.md#rt-clm-quote-verification): it is a maintenance diagnostic explanation, not citation presence. No supplied claim counterpart.

> why: "Each page's correction names the other, so a reader of either one is reading a correction the other page has since re-corrected — the current truth lives in neither place alone.",
> --- `lib/inbox.ts`

The supporting route is [EPI-RTE-watch-checks](#epi-rte-watch-checks). Its inspected predicate requires reciprocal marker-path edges, not dates or logical incompatibility. A note can retain a correction banner naming another page as historical bookkeeping while both now state the same current fact. Such inputs meet the structural condition without the claimed current disagreement. The justified result is a review candidate, not the stronger semantic conclusion.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
