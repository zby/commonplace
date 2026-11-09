---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "KHMS memory epistemic routes: source-linked proposal, bounded checks, review, withdrawal and later reliance."
run-id: AAS-2026-11-08-khms-memory-c5267e800c56-01
reviewed-boundary: f739eb976dab199fd4cd64e352192cc0b112c047
---

# KHMS memory epistemic report

## Source-and-claim boundary

The question is how KHMS turns work records into retained claims and instructions, checks them, authorizes reliance, and withdraws or changes that reliance. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Source identity and evidence layers: see [Source register](boundary.md#source-register). All SRC-1 anchors below are at that frozen commit. This report distinguishes inspected implementation from model instructions and attributed deployment reports; none establishes a real run in this analysis.

Material routes include journal/transcript/Git acquisition, model proposals, mechanical checks, reviewer admission, graph/status integration, retrieval, validity review and cleanup. Provider internals remain uninspected; distributed-parametric fixity and alternatives: see [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model), [RT-CMP-qwen](runtime.md#rt-cmp-qwen), [RT-CMP-bge](runtime.md#rt-cmp-bge). No claim about local training follows from card updates.

| Entry point or operation | SRC-1 path | Coverage and evidence basis |
|---|---|---|
| Foreground capture, external findings, bootstrap, review | `AGENTS.md` | Direct complete doctrine read; [EPI-OBJ-mark](#epi-obj-mark), [EPI-CLM-grounding-check](#epi-clm-grounding-check) |
| Generator, ledger/carry, per-MARK dispatch | `tools/nightly_distill.sh`, `tools/permark.py`, `tools/prompts/nightly-generate.md`, `tools/generated_marks.py` | Supplied [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals), [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation); direct FormatCheck slice, [EPI-RTE-quote-check](#epi-rte-quote-check); direct generator prompt and generated-line parse/build reads separate model findings from imported packets; [MEM-OBJ-inbox](memory.md#mem-obj-inbox) |
| Quote matching | `tools/verify_quotes.py` | Direct normalization/classification and fixtures; [EPI-RTE-quote-check](#epi-rte-quote-check) |
| Approval, supersession, views | `tools/approve_inbox.py`, `tools/build_views.py` | Supplied [RT-RTE-card-admission](runtime.md#rt-rte-card-admission); direct supersession implementation slice, [EPI-RTE-supersession-link](#epi-rte-supersession-link) |
| Hook event dispatch and registered integration | `tools/khms_hook.py`, `claude-code/settings.hooks.json` | Direct main, status gate, dispatch gate and settings; [EPI-RTE-hook-gates](#epi-rte-hook-gates); supplied recall record |
| Explicit recall, pending channel, precheck and history | `tools/khms_recall_hybrid.py`, `tools/khms_pending.py`, `tools/khms_select.py` | Supplied [RT-RTE-recall-return](runtime.md#rt-rte-recall-return); consumers and exceptions remain as recorded there |
| Weekly synthesis and own-mistake audit | `tools/prompts/weekly-synthesis.md`, `tools/weekly_synthesis.sh` | Complete prompt read; supplied maintenance implementation; [EPI-CLM-synthesis-review](#epi-clm-synthesis-review) |
| Validity, know-how classification, daily proposals | `tools/card_validity.py`, `tools/khms_validity_daily.sh` | Direct checker, retry, aggregation, know-how and proposal functions; daily batch/wait dispatch; [EPI-RTE-validity-check](#epi-rte-validity-check) |
| Triage application | `tools/apply_triage.py` | Direct decide/ops_for; supplied maintenance application record; [EPI-RTE-triage-verdict](#epi-rte-triage-verdict) |
| Erratum, archive, versions, export | `tools/khms_erratum.py`, `tools/khms_archive.py`, `tools/khms_versions.py`, `tools/khms_export.sh` | Erratum doctrine directly read; remaining implementation supplied only through boundary/runtime. No exhaustive correctness or recovery conclusion |
| Retrieval evaluator | `tools/eval/run_eval.py` | Direct complete read; [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval) |
| Injection measurement and historical experiments | `docs/measuring-injection.md`, `tools/khms_experiments/README.md` | Measurement document directly read; experiment tooling otherwise supplied boundary only, internals unassessed; prevents system-complete evaluator inventory |
| Releases, private prompt extensions | `README.md`, `tools/khms_prompt.py` | Supplied [RT-RTE-operational-change](runtime.md#rt-rte-operational-change); private extension content unavailable |

The supplied refusal also identifies legacy lexical ledger repair in SRC-1 `tools/mark_ledger.py`, `cmd_recheck_carded`: a narrow older unquoted already-carded subset can be reopened under explicit apply. This helper remains unassessed here; no complete inventory of coverage-check/repair mechanisms or per-event human decision control is claimed.

Missing deployment base and source transcripts prevent checking imported claims' truth, complete lineage, actual model outputs and review decisions. Missing host/provider evidence prevents establishing tool-policy enforcement and model compliance. Missing raw measurement traces and comparisons prevents validating deployment metrics, component effects, improved capacity or exercised self-improvement. Available but uninspected helper/test internals are not absences; this is not a system-complete negative about knowledge production.

Claims assessed: [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary), [EPI-CLM-grounding-check](#epi-clm-grounding-check), [EPI-CLM-synthesis-review](#epi-clm-synthesis-review), [EPI-CLM-measured-injection](#epi-clm-measured-injection).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-mark](#epi-obj-mark) | Events, outcomes, requirements, source statements | Acquisition inputs | see record; SRC-1 `AGENTS.md` | Report of measurement is not independent measurement |
| [MEM-OBJ-inbox](memory.md#mem-obj-inbox) | Generated one-line findings, distinct from raw source packets and later card proposals | see record | see record; SRC-1 `tools/generated_marks.py` | Source-span occurrence does not check finding equivalence or entailment |
| [EPI-OBJ-candidate](#epi-obj-candidate) | Proposed observations, mechanisms, principles; normative instructions separately | Proposals without approved authority | see record; SRC-1 `tools/prompts/nightly-marks.md` | Actual semantics and entailment unobserved |
| [EPI-OBJ-card](#epi-obj-card) | Approved claim body; descriptive and normative cards separated by doctrine | Persistent reliance target | see record; SRC-1 `AGENTS.md` | Approved label is not proof |
| [EPI-OBJ-verdict](#epi-obj-verdict) | Validity assertions/reasons and symbolic verdict fields | Bounded evidence check and review input | see record; SRC-1 `tools/card_validity.py` | Checker does not verify relevance of command to claim |
| [RT-CMP-qwen](runtime.md#rt-cmp-qwen), [RT-CMP-bge](runtime.md#rt-cmp-bge) | No independently individuated proposition in vector state | Ranking | see records; SRC-1 `tools/embed_index.py` | Truth-apt content not determinable at numerical-component level |

## Authority-route ledger

Fields owned by supplied/shared records are referenced rather than redefined below. Architectural status is this report's assessment. No route is asserted observed.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) | content transformation | implemented | [EPI-OBJ-mark](#epi-obj-mark) | truth-apt transformation: acquisition/import | External records → source packet | Source identity/selection, not truth evaluation | Scheduled/manual capture | Imported source packet only; excludes generator-authored findings | Retention preparation | Source warrant unknown; source labels retained, capture incomplete possible | Offers external records to generator/evaluator | Generator/evaluator; source packet; advisory; next stage | SRC-1 `tools/nightly_distill.sh` | none | none | Source-linked is not source-true |
| [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) | content transformation | implemented | [MEM-OBJ-inbox](memory.md#mem-obj-inbox) | truth-apt transformation: indeterminate | Imported transcript/Git passages → generator-authored one-line findings | Model selects reusable causes, refutations, measured facts and reasons; software checks shape, source-span occurrence and deduplication | Fresh generator session before per-MARK evaluation; see supplied route | Generated lines retained for later evaluation, or rejected by parse/build checks | Proposal/ledger admission only; not approved-card authority | Located span preserves a provenance witness, not semantic equivalence or source truth; finding warrant unknown | Retained generated findings become per-MARK inputs without per-content human approval | Per-MARK evaluator; generated ledger lines; advisory; later evaluation/resume | SRC-1 `tools/prompts/nightly-generate.md`, `tools/generated_marks.py` | none | none | Acquisition, reshaping, derivation or conjecture cannot be distinguished without actual finding/source pairs and semantic assessment; no accepted ampliative instance established |
| [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation) | content transformation | implemented | [EPI-OBJ-candidate](#epi-obj-candidate) | truth-apt transformation: indeterminate | MARK and related cards → proposed claim | Model interpreting selected packet | After packet construction | New, belongs, supersede, contradict, erratum or no-card decision | Candidate production only | Acquisition/reshaping/derivation/conjecture depend on actual output; no semantic trace to decide | Changes proposal document | Later stages/reviewer; file; advisory; nightly/review | SRC-1 `tools/permark.py` | none | none | No entailed or accepted ampliative instance established |
| [EPI-RTE-quote-check](#epi-rte-quote-check) | check/evidence production | implemented | [EPI-OBJ-candidate](#epi-obj-candidate) | no content change | Quoted text and extracted specifics | String normalization, ordered matching; textual occurrence domain | After candidate output; format check is configurable | Match classes and format problems | Quote report is non-gating in inspected nightly postprocess; separate format repair and admission checks | Text occurs in source under defined matching | Supplies review evidence; quote failure itself does not stop this postprocess | Proposal stages; report; permissive/enforcing per gate; this batch | SRC-1 `tools/verify_quotes.py` | [EPI-CLM-grounding-check](#epi-clm-grounding-check) | none | Occurrence does not establish entailment; postprocess ignores checker exit |
| [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) | check/evidence production | implemented | [EPI-OBJ-candidate](#epi-obj-candidate) | no content change | Candidate schema/lint/IDs | Deterministic checks, not a truth oracle | Before allocated card writes | Refusal or structurally usable batch | Import gate | Schema and selected consistency only | Blocks invalid import | Importer; validation result; enforcing; invocation | SRC-1 `tools/approve_inbox.py` | [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary) | none | Reviewer authority not authenticated |
| [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) | disposition/acceptance | implemented | [EPI-OBJ-card](#epi-obj-card) | no content change | Reviewed candidate → admitted card | Human/strong-model review prescribed; invocation decides import | After edit/withholding opportunity | Approved import; no observed evidence-consuming semantic decision | Permits knowledge-directory writes | Intended reusable knowledge; exact per-claim criterion/decision not available | Makes card eligible for later use | Reviewer/importer; reviewed file; permissive; across sessions | SRC-1 `AGENTS.md` | [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary) | none | Operational admission ≠ demonstrated epistemic acceptance |
| [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) | retention | implemented | [EPI-OBJ-card](#epi-obj-card) | no content change | Allocated cards and receipts | See supplied record | On successful checked import | Durable Markdown and review receipts | Persistent availability | No added truth warrant | Later retrieval enabled | Search/view consumers; files; permissive; sessions | SRC-1 `tools/approve_inbox.py` | none | none | Not lifecycle integration merely because stored |
| [EPI-RTE-supersession-link](#epi-rte-supersession-link) | lifecycle integration | implemented | [EPI-OBJ-card](#epi-obj-card) | non-truth-apt policy/content update: status and replacement pointer | Admitted superseding card → old status/link | Existing target/status guard | During admission after review protocol | Old target superseded and linked | Changes default retrieval eligibility | Relationship licensed by reviewer, not proved by pointer | Withdraws default current reliance on old card | Retrieval; status/graph; enforcing default filtering; subsequent calls | SRC-1 `tools/approve_inbox.py` | none | none | Post-admission integration; epistemic acceptance unobserved |
| [RT-RTE-recall-return](runtime.md#rt-rte-recall-return) | operational admission/selection/consumption | implemented | [EPI-OBJ-card](#epi-obj-card) | truth-apt transformation: non-ampliative reshaping | Cards → ranked snippets/pointers | Ranking, status, budgets and history controls | Query/matched hook event | Selected context; pending evidence labelled separately | Ranking/advisory, not answer enforcement | Relevance score licenses selection, not truth | Changes supplied model context | See [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) | SRC-1 `tools/khms_select.py` | none | none | Open full card; snippet may omit qualification |
| [EPI-RTE-validity-check](#epi-rte-validity-check) | check/evidence production | implemented | [EPI-OBJ-verdict](#epi-obj-verdict) | truth-apt transformation: indeterminate | Card subclaims against copied evidence tree | Model interpretation + rerun exit/quote/schema checks | Sampled daily/calibration or explicit run | holds/no-longer-holds/cannot-check-offline/unverified | Accepted checker result feeds ledger and proposals | Command output reproducibility, not complete claim correctness | Retries invalid answers; emits proposed correction, not automatic card change | Daily reviewer; JSON/ledger/proposal parts; advisory; later review | SRC-1 `tools/card_validity.py` | none | none | Know-how-only leg explicitly NOT_JUDGED |
| [EPI-RTE-triage-verdict](#epi-rte-triage-verdict) | disposition/acceptance | implemented | [EPI-OBJ-card](#epi-obj-card) | non-truth-apt policy/content update: reliance status and relations | Reviewer row → allowed mutation | Explicit verdict + live-body quote and conflict guards | Apply invocation, not detection alone | Reject/skip/apply refute/challenge/link/unlink | Enforcing mutation gate | Reviewer accepts classification for base maintenance; semantic adequacy not checked by quote coverage | Can withdraw current status or mark challenged | Apply planner/writer then retrieval; verdict and metadata; enforcing; later calls | SRC-1 `tools/apply_triage.py` | none | none | No verdict rejects; quote-present does not prove contradiction |
| [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | content transformation | implemented | [EPI-OBJ-candidate](#epi-obj-candidate) | truth-apt transformation: indeterminate | Weekly observations → umbrella claims and experiment proposals | Model instructed to compare patterns and mistakes | Weekly staged calls and review | Proposed principles, discriminating tests, measures | Proposal only until separate admission | Novel analogy need not follow from observations; no concrete output to classify | Offers revisions to reviewer | Reviewer; proposal file; advisory; subsequent review | SRC-1 `tools/prompts/weekly-synthesis.md` | [EPI-CLM-synthesis-review](#epi-clm-synthesis-review) | none | Normative measures are policy proposals, not truth proofs |
| [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | behavior/policy adaptation | implemented | [EPI-OBJ-card](#epi-obj-card) | non-truth-apt policy/content update: revised retained guidance | Reviewed policy/summary → future context | Reviewer and separate application | After separate approval | Potential changed guidance | Model-interpreted authority | No improvement guarantee | May change later foreground decisions | See [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) | SRC-1 `tools/prompts/weekly-synthesis.md` | [EPI-CLM-synthesis-review](#epi-clm-synthesis-review) | none | Disposition supported, actual live causal activation unobserved |
| [EPI-RTE-hook-gates](#epi-rte-hook-gates) | operational admission/selection/consumption | implemented | [EPI-OBJ-mark](#epi-obj-mark) | no content change | Journal status MARK additions / dispatch proposal spans | Syntactic kind parser / ranked unseen card predicate | Matched PreToolUse before execution | deny/allow/exempt | Host permission-decision channel; fail-open | Content-selection discipline, no truth license | Blocks status-only capture or first dispatch pending card exposure | Host tool dispatcher; hook JSON; enforcing if honored; current attempt | SRC-1 `tools/khms_hook.py` | none | none | Dispatch gate not wired in shipped settings; report never refused |
| [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval) | check/evidence production | implemented | [EPI-OBJ-card](#epi-obj-card) | no content change | Query → expected card rank in chosen channel | Program against caller-labelled frozen rows | Explicit --prod eval | Recall@k and gated failure exit | Exit 1 for gated miss-source rows only | Selected-row retrieval quality, not card truth or downstream success | Caller can reject regression; no inspected automatic deployment consumer | CLI caller; status/JSON; advisory or caller gate; eval invocation | SRC-1 `tools/eval/run_eval.py` | none | none | No answer-quality oracle or component causal identification |

Generator guidance and implemented generated-line admission support the distinct content edge above (SRC-1, doctrine/design and implementation respectively):

> - `<one-line finding>`: English, self-contained, under 300 characters; every number, identifier or path
>   in it must also be inside the span.
> --- `tools/prompts/nightly-generate.md`

> elif VQ.classify(rec["span"], src)[0] == "ABSENT":
>     why = "ungrounded (span not in its source)"
> elif rec["id"] in seen:
>     why = "duplicate"
> --- `tools/generated_marks.py`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary) | Approval keeps fabricated cards out of remembered facts | see record; SRC-1 `AGENTS.md`; doctrine/design | Explicit separate review duty | [RT-RTE-card-admission](runtime.md#rt-rte-card-admission) | Uninspected | No authenticated reviewer or universal write confinement | Separate checked import supports review protocol | Not a universal truth/security guarantee |
| [EPI-CLM-grounding-check](#epi-clm-grounding-check) | Mechanical grounding checks that the model did not fabricate | see record; SRC-1 `AGENTS.md`; doctrine/design | Quote occurrence and specifics requested | [EPI-RTE-quote-check](#epi-rte-quote-check) | Uninspected | Occurrence cannot validate causal interpretation or source truth | Textual grounding is implemented | Nightly postprocess logs and ignores quote-check failure; no universal suppression |
| [EPI-CLM-synthesis-review](#epi-clm-synthesis-review) | Patterns, discriminating experiments and own-mistake measures produce better future guidance | see record; SRC-1 `tools/prompts/weekly-synthesis.md`; doctrine/design | Detailed proposal instructions | [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | Uninspected | No experiment execution, accepted novel principle or later benefit trace supplied | Reflection-oriented proposal architecture | Proposed experiment is not performed test; analogy is not warranted transfer |
| [EPI-CLM-measured-injection](#epi-clm-measured-injection) | Measurements led to hook wiring changes; replay distinguished slot budget from switch | see record; SRC-1 `docs/measuring-injection.md`; reported operation | Explicit metrics and comparison caveats | [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval), [RT-RTE-recall-return](runtime.md#rt-rte-recall-return) | No inspectable deployment trace | Before/after and single replay narratives cannot establish broad or component-level effect independently | Attributed measurement-guided change, configurable hook architecture | No reproduced outcome or causal improvement established |

## Bounded conclusion

KHMS acquires work records and external findings, then separately generates model-authored findings before per-MARK card evaluation. The acquisition classification ends at the imported packet. Generated findings have an indeterminate truth-apt transformation relation: span checking licenses textual location, not semantic preservation, entailment or novelty. See [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals), [MEM-OBJ-inbox](memory.md#mem-obj-inbox). KHMS retains source-linked candidates, checks textual/structural properties, and offers reviewed cards to later agents. Source labels preserve some provenance, not the source's truth warrant. Model selection, summaries and snippets can omit conditions; access to the full card and links is a prescribed safeguard, not demonstrated consumer behavior. See [EPI-OBJ-mark](#epi-obj-mark), [EPI-OBJ-candidate](#epi-obj-candidate), [EPI-OBJ-card](#epi-obj-card), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery).

The import gate enforces schema/lint constraints and records admission. Semantic acceptance is delegated to review; no supplied per-claim decision identifies evidence, criterion, intended use and scope for an accepted ampliative result. This prevents claiming an observed accepted novel principle, not the architectural capacity to propose one. The weekly prompt explicitly solicits cross-domain principles and tests, but actual outputs are unavailable, so truth-apt transformation remains indeterminate rather than presumed entailed or ampliative. Normative policies are separated from descriptive claims. See [RT-RTE-card-admission](runtime.md#rt-rte-card-admission), [EPI-CLM-synthesis-review](#epi-clm-synthesis-review).

Checks carry different licenses. Quote matching checks occurrence under normalization/elision rules, not source truth or entailment; its nightly postprocess result is logged rather than a rejection gate. Validity checking reruns commands and tests quoted output and verdict aggregation, but leaves the model's decomposition and command relevance unchecked. Know-how-only judging does not test validity. Triage uses explicit review verdicts and guards before withdrawing or challenging reliance. Retrieval evaluation measures expected-card ranking, not answer correctness. See [EPI-RTE-quote-check](#epi-rte-quote-check), [EPI-RTE-validity-check](#epi-rte-validity-check), [EPI-RTE-triage-verdict](#epi-rte-triage-verdict), [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval).

Integration is more than file retention: admitted replacement edges change old-card status and default current retrieval. History and pending-evidence channels intentionally permit labelled material outside current approved knowledge. Erratum and archive routes offer separate correction/withdrawal surfaces, with server-history recovery limits retained in [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). No source of omniscient evaluation or invariant correctness follows.

For formulated method/policy guidance, localized natural-language content and persistence across sessions are afforded by card files. Model-mediated consumption is architecturally available through recall, but delivered content is not evidence of compliant decisions. Content-directed criticism and iteration are requested in weekly own-mistake review; no concrete retained criticism → revision → next decision trace is supplied. Conditions 1–4 of a theory builder therefore are not jointly established as operated. Learning (improved future capacity) is not demonstrated. Reflection is supported as a designed route from own-operation logs to proposed guidance and back through approved context, not observed causal closure. Autonomous end-to-end review is not established by permission to use a strong model. These findings are independent: review machinery and durable guidance remain supported despite missing benefit evidence.

For the proposed own-mistake → retained policy pathway, the objective is avoiding recurrent operational mistakes across later sessions. Update determination is instructed to use failures; card admission and later retrieval provide a dispositional self-change path within KHMS plus its agent consumer. Evidence that a particular update entered live behavior and subsequently caused different operation is unavailable (self-improvement links 1 and 4 are not established for an exercised instance). The deployment narrative is reported operation only. No successful or exercised self-improvement attribution follows. See [EPI-CLM-synthesis-review](#epi-clm-synthesis-review), [EPI-CLM-measured-injection](#epi-clm-measured-injection), [RT-RTE-operational-change](runtime.md#rt-rte-operational-change).

## Shared records

### Operative objects

#### EPI-OBJ-mark
Label: MARK and source records

Natural-language journal event lines, transcript excerpts and Git descriptions, stored as files and staged source packets. These can express truth-apt reports about events, measurements or decisions; normative requests are imported as statements that someone requested them, not automatically endorsed instructions. No runtime object counterpart is declared; closest route is [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals), whose input part this object identifies. SRC-1: `AGENTS.md`, `tools/prompts/nightly-marks.md`. Source authenticity and full selection completeness are not inspected.

> External findings come back as `reported` observations with the URL
> and a locating quote in `source`.
> --- `AGENTS.md`

#### EPI-OBJ-candidate
Label: Candidate card


Natural-language proposed body plus symbolic header/relations/MARK IDs and quote annotations in staged/inbox Markdown. Proposed descriptive claims and normative policy text have separate type/level roles; they do not gain approved authority just by being written. No supplied object counterpart; distinct output object of [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation) and [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). SRC-1: `tools/prompts/nightly-marks.md`.

> You are the MARK stage of the KHMS nightly pipeline. Zero authority: you only produce candidates and
> verdicts; the morning review decides.
> --- `tools/prompts/nightly-marks.md`

#### EPI-OBJ-card
Label: Approved card

Markdown file in memory/know, natural-language body and symbolic YAML ID/type/status/links. Body semantics are interpreted by agent/reviewer; metadata governs deterministic consumers. These parts are distinguished in the ledger, not treated as one truth check. Source and links support tracing, not automatic endorsement. No runtime object counterpart; distinct retained output of [RT-RTE-card-admission](runtime.md#rt-rte-card-admission), consumed through [RT-RTE-recall-return](runtime.md#rt-rte-recall-return). SRC-1: `AGENTS.md`.

> - **Descriptive and normative never share a card.** What happened is an observation; what to
>   do about it is a `derived` card linked by `derived_from`. A recommendation can die without
>   killing the fact under it, and one fact can feed two competing recommendations.
> --- `AGENTS.md`

#### EPI-OBJ-verdict
Label: Validity verdict

JSON answer with natural-language subclaims/reasons and symbolic enums, command/exit/quote evidence; persisted ledger/report/proposal representation. Truth-apt validity judgments and know-how classification use different checks. No supplied object counterpart; material intermediate within [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). SRC-1: `tools/card_validity.py`.

> def _result(verdict, attempts, ans, history, metas, t0):
>     return {"verdict": verdict, "attempts": attempts, "answer": ans, "errors": history,
>             "wall_s": round(time.time() - t0, 1),
>             "cost_usd": round(sum(float(m.get("cost_usd") or 0) for m in metas), 6), "meta": metas}
> --- `tools/card_validity.py`

### Routes

#### EPI-RTE-quote-check
Label: Candidate quote occurrence check

Distinct checker within the supplied proposal stages, overlapping [RT-RTE-nightly-proposals](runtime.md#rt-rte-nightly-proposals) and [RT-RTE-mark-evaluation](runtime.md#rt-rte-mark-evaluation); not a duplicate of their full progression. FormatCheck's schema/relation/lint check is separate from this quote matcher.

Owner: deterministic verify_quotes classifier; endpoints candidate quotes + named source files → classes/report. SRC-1: `tools/verify_quotes.py`, `tools/nightly_distill.sh`. Exact match precedes normalization, then ordered marked segments; this narrows provenance errors but checks no semantic entailment. Concrete deduction without execution: source `the valve failed`, quote `the valve failed` takes the raw-substring branch and returns EXACT even if the surrounding source says someone falsely alleged that sentence. This is a positive textual witness and counterexample to interpreting occurrence as truth acceptance. Normative claims have no automatic truth license. Nightly postprocess runs the matcher but ignores failure; report is retained for review. No answer oracle or human acceptance in matching.

- Immediate return: Classes and grounding report
- Later read-back: Report retained in staging for review; quote classification itself does not load cards
- Delegated visibility: inapplicable — deterministic checker invokes no model
- Selection predicate: Candidate quote and declared source label; exact/normalized/ordered elision tests
- Invalidation or expiry: Missing occurrence yields ABSENT; no truth expiry test
- Activation or effect: Postprocess logs result and continues; semantic rejection not enforced by this call
- Evidence limits: Implementation deduction only; no target execution; source truth and interpretation unverified
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if q in source.raw:
>     return "EXACT", "", q
> --- `tools/verify_quotes.py`

> python3 "$CODE/verify_quotes.py" "$f" --source digest="$dg" --source journal="$jv" \
>     --source gitlog="$gl" > "$qr" 2>&1 || true
> --- `tools/nightly_distill.sh`

#### EPI-RTE-supersession-link
Label: Supersession target integration

Part of: [RT-RTE-card-admission](runtime.md#rt-rte-card-admission)

The supplied route is a valid container; this part isolates post-admission integration from schema checks and retention. Owner: mark_superseded. Endpoint new approved edge → old target metadata; existing active/challenged target becomes superseded with nested superseded_by. SRC-1: `tools/approve_inbox.py`. Reviewer supplies the relation; code checks existence/status rather than truth of replacement. Rejection/skip covers missing/unparseable or non-live targets. Recovery is supplied receipt/server-history protocol, not observed undo. No answer oracle. Ordinary review/import mode.

- Immediate return: Changed target count and notes
- Later read-back: Nested status/pointer consumed by later current-card retrieval; see [RT-RTE-recall-return](runtime.md#rt-rte-recall-return)
- Delegated visibility: inapplicable — function invokes no model
- Selection predicate: New supersedes edges, target existence/parsing and allowed status
- Invalidation or expiry: Non-live target generally left for review; history mode can still show dead cards
- Activation or effect: Withdraws default current reliance on old card, connects replacement
- Evidence limits: Integration follows operational admission; per-claim epistemic acceptance remains unobserved
- implementation conclusion status: wired
- operation conclusion status: uninspected

> meta["status"] = "superseded"
> links["superseded_by"] = new_id
> meta["links"] = links
> _write_card(path, meta, m.group(2))
> --- `tools/approve_inbox.py`

#### EPI-RTE-validity-check
Label: Card validity and know-how checks

Part of: [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission)

This part isolates evaluation from application. Owner: card_validity judge_card/check_answer plus daily driver. Card and copied repository tree → model subclaims and commands → rerun/schema checks → verified-format result or unverified → ledger/proposal parts. Target is card validity within offline tree evidence, not general truth. A separate know-how-only leg asks relevance to future use without truth testing. Human review can veto subsequent application; model proposes and program rejects malformed/unreproduced answers with bounded retries. No known-correct answer oracle: command outputs are evidence, not reference semantic labels. Modes include operational sampled daily checks and calibration adapter comparison. Guidance: fixed decomposition, command, quote and aggregate-verdict rules. Retained material is judgment, command evidence and suggested change, not provider parameters.

The first positive verdict does not establish complete checking: derived_verdict returns holds when one subclaim holds and none is no-longer-holds, even if another cannot-check-offline. This is a rule over supplied labels, not a deduction that all card claims hold. check_answer checks evidence reproduction, not that the model picked a complete decomposition or a discriminating command. proposal_row returns no correction for holds with knowhow yes; cannot-check-offline keeps the card; no-longer-holds yields suggested erratum/supersede commands; knowhow no yields retirement proposal. The daily APPLIED marker waits for review/application, not independent evidence that review was correct. SRC-1: `tools/card_validity.py`, `tools/khms_validity_daily.sh`.

- Immediate return: Verdict, attempts, errors, answer and cost; proposal rows
- Later read-back: Ledger/results inform future sampling and reviewer proposals; live cards only change through separate application
- Delegated visibility: Model gets card and copied-tree context; know-how-only gets card/rule without tools
- Selection predicate: Eligible sampled cards or explicit IDs; schema/command/quote/aggregation checks decide usable answer
- Invalidation or expiry: Bad result retries to unverified; offline unknown does not automatically withdraw card
- Activation or effect: Produces review evidence, not automatic live-card replacement; older unmarked batch blocks a new daily batch
- Evidence limits: No observed results; command relevance and truth interpretation remain model judgments; provider opacity as in [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model)
- implementation conclusion status: wired
- operation conclusion status: uninspected

> def derived_verdict(subs):
>     vs = [s.get("verdict") for s in subs]
>     if "no-longer-holds" in vs:
>         return "no-longer-holds"
>     if "holds" in vs:
>         return "holds"
>     return "cannot-check-offline"
> --- `tools/card_validity.py`

> if v in ("holds", "no-longer-holds") and not evs:
>     errs.append(f"subclaim {k}: verdict {v!r} without evidence -- run a command and quote its output")
> --- `tools/card_validity.py`

> elif not _quote_in(quote, out):
>     errs.append(f"output_quote {quote[:300]!r} not found in the real output; the real output begins: "
>                 f"{_norm(out)[:300]!r}")
> --- `tools/card_validity.py`

> if verdict in ("holds", NOT_JUDGED) and knowhow != "no":
>     return None
> --- `tools/card_validity.py`

> KNOWHOW_PROMPT = """You are sorting ONE knowledge card. Do not check whether it is still true; answer only
> the question below. Use no tools: everything you need is in this message.
> --- `tools/card_validity.py`

#### EPI-RTE-triage-verdict
Label: Reviewed triage disposition

Part of: [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission)

Owner decide/ops_for; endpoints proposed rows + reviewer verdict + current cards → allowed mutation plan. Reviewer can reject, change class or omit verdict (rejected). Code rechecks live-body quote coverage and winner/loser conflicts; unlink uses a different structural guard, not quote matching. Dry-run assume_apply is preview only, not permission to write. refute/retire makes loser refuted and links evidence winner; challenge marks challenged; contradicts adds symmetric relations without resolving truth. Admission criterion is explicit row authorization plus guards, intended use base maintenance. It consumes source quotes/reason but program does not decide semantic contradiction truth. No answer oracle; operational maintenance, no curriculum. Recovery remains supplied file-history protocol. SRC-1: `tools/apply_triage.py`.

- Immediate return: Per-row REJECT/SKIP/APPLY and plan
- Later read-back: Applied statuses/links reach later retrieval
- Delegated visibility: inapplicable — application checker invokes no model
- Selection predicate: Explicit per-row verdict; quote coverage/conflict guards; explicit apply required for writes
- Invalidation or expiry: Missing verdict rejects, missing files skip, conflicting roles reject
- Activation or effect: Permits metadata changes or blocks them; semantic criticism remains review responsibility
- Evidence limits: No observed criticism instance or successful application supplied
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not d:
>     outcomes[n] = ("REJECT", "no verdict line in the REVIEW VERDICT section — "
>                              "silence is not approval")
>     continue
> --- `tools/apply_triage.py`

> if cls in ("refute", "retire"):
>     return [(loser, "status", "refuted"), (loser, "refuted_by", winner),
>             (winner, "contradicts", loser)]
> --- `tools/apply_triage.py`

#### EPI-RTE-hook-gates
Label: Capture and dispatch gates

Distinct operational-admission referent: [RT-RTE-recall-return](runtime.md#rt-rte-recall-return) covers recall/delivery and mentions Agent dispatch, but not the status-MARK exclusion or first-exposure denial predicate. Both share the hook dispatcher; this record does not replace the valid recall container.

Owner: main/run_status_mark_gate/run_dispatch_proposal_gate. Journal Edit/Write/Bash additions are parsed for forbidden status kinds and denied before execution. For Agent/Task calls, proposal_gate selects relevant cards and denies when a detected proposal has unseen/uncited hits; it saves seen state so repeat attempts can pass. This is exposure control, not truth validation or proof that a card was read. Both gates fail open on exception or kill switch. The shipped settings wire status gate tool types, but not Agent/Task or Stop. Report tools call a stamp path that never refuses reports, despite the settings comment calling it a retrieval-claim gate. No authenticated human decision or answer oracle; code classifies proposed operations. SRC-1: `tools/khms_hook.py`, `claude-code/settings.hooks.json`.

- Immediate return: Hook permission deny or ordinary continuation
- Later read-back: Dispatch seen/shown session state influences repeated attempts; blocked status text is not retained by this gate
- Delegated visibility: Agent tool path checks dispatch text before launch, if wired; actual host delivery unobserved
- Selection predicate: Status-kind grammar for journal additions; OPEN unseen-card hits in proposal spans for dispatch
- Invalidation or expiry: Kill switch/experiment controls, errors fail open, repeat fingerprints bypass first exposure denial
- Activation or effect: Host may block this tool attempt; no check that permitted content is true or user approved
- Evidence limits: Not universal filesystem control; dispatch branch unavailable through supplied example matchers; no activation evidence
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return ("DENY" if opened else "ALLOW"), out
> --- `tools/khms_hook.py`

> if event == "PreToolUse" and payload.get("tool_name") in ("Edit", "Write", "Bash"):
>     try:
>         if run_status_mark_gate(payload):
>             return
>     except Exception as exc:                                   # noqa: BLE001
>         log(event, "status-mark-gate", action="ERROR->ALLOW %s: %s" % (type(exc).__name__, exc))
> --- `tools/khms_hook.py`

> def handle_report(payload, event, exp):
>     """PreToolUse on the report tool: never refused (#247 removed the claim, proposal and terminology gates
>     on a report); the reply is stamped for the Stop gate, which cannot count on the transcript showing it yet."""
> --- `tools/khms_hook.py`

#### EPI-RTE-retrieval-eval
Label: Production-path retrieval evaluation

Distinct evaluator with no supplied route counterpart: closest is [RT-RTE-recall-return](runtime.md#rt-rte-recall-return), which supplies ranking, not expected-card comparison or evaluation exit semantics.

Owner cmd_prod; endpoints caller-selected frozen (query,gold) rows + current loaded base/ranking → hit/rank report/status. Expected-card oracle is supplied by dataset author, with fictional shipped rows and caller-owned real misses. Query k can override CLI k per row; optional lexical contrast tests channel rankings, not downstream truth. Only failed source=miss rows marked gate fail the exit code; other misses count but do not reject. JSON rows are optional; no inspected automatic code-update consumer makes failure a universal deployment veto. Human/operator can use results to choose tuning under AGENTS calibration doctrine. No automatic policy update occurs inside evaluator. SRC-1: `tools/eval/run_eval.py`.

- Immediate return: Recall@k, per-miss lines, exit status and optional JSON
- Later read-back: inapplicable — evaluator does not itself reload/update retained guidance; caller may retain output
- Delegated visibility: inapplicable — deterministic evaluator invokes ranking, not a delegated answer model
- Selection predicate: Selected split and gold file; hit if any expected ID in top k; fatal subset requires source=miss and gate
- Invalidation or expiry: Frozen labels can be revised only outside this evaluator; no correctness expiry check
- Activation or effect: Exit 1 on gated failures; tuning/admission depends on external caller decision
- Evidence limits: No target eval run; labelled relevance does not validate card truth, hook selection budgets or answer benefit
- implementation conclusion status: wired
- operation conclusion status: uninspected

> miss_rows = [(r, ok, rank) for r, ok, rank, _c in per_row
>              if r.get("source") == "miss"]
> failed = [(r, rank) for r, ok, rank in miss_rows if not ok]
> gated_fail = [(r, rank) for r, rank in failed if r.get("gate")]
> --- `tools/eval/run_eval.py`

> return 1 if gated_fail else 0
> --- `tools/eval/run_eval.py`

### Claims

#### EPI-CLM-grounding-check
Label: Mechanical anti-fabrication claim

Distinct from [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary): this claims warrant from textual checking, rather than reviewer separation. SRC-1: `AGENTS.md`, doctrine/design. The inspected implementation supports narrower occurrence/format checks. New direct source slice shows a consequential qualification not explicit in supplied runtime: nightly postprocess ignores quote-check exit and logs a report. This is a supplemental finding on grounding, not a supersession of the supplied format-check failure finding.

> This is the difference
> between asking a model not to fabricate and checking that it did not.
> --- `AGENTS.md`

#### EPI-CLM-synthesis-review
Label: Synthesis and own-mistake review

Distinct from reviewer-boundary claim: content-directed synthesis and criticism guidance. SRC-1: `tools/prompts/weekly-synthesis.md`, doctrine/design. Parts of [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) implement staged proposal/application, not guaranteed semantic performance. A concrete principles instance might be imported, reshaped or genuinely conjectural; none supplied to decide. The normative countermeasure route must be distinguished from claim truth.

> **New principles**: ≥3 independent active observations sharing a shape without an umbrella
>    derived card → draft a `principle` candidate with derived_from listing them. Look for
>    cross-domain analogies and symmetries, not just same-tag groups.
> --- `tools/prompts/weekly-synthesis.md`

> If a mistake RECURRED, say so explicitly —
>    a repeat means the previous measure was wrong, so do not restate it. Analyse why that measure
>    failed and propose a different one that rests on a mechanism (a step that is either taken or not
>    and is visible in the record) rather than on intent. "Be more careful" is not a measure.
> --- `tools/prompts/weekly-synthesis.md`

#### EPI-CLM-measured-injection
Label: Measurement-guided hook changes

Distinct from [RT-CLM-review-boundary](runtime.md#rt-clm-review-boundary): attributed deployment changes and replay diagnosis, not admission guarantees. SRC-1: `docs/measuring-injection.md`, reported operation; no acquired raw traces authenticate the figures or comparisons. Narrative describes removing event wiring and widening budgets, with concrete caveats. It supports an attributed reflective adjustment, not independent causal improvement or transfer.

> **Before you copy any of this: those numbers are one deployment's, on a base of ~2400 cards,
> with one operator.** The method transfers. The conclusion does not.
> --- `docs/measuring-injection.md`

> What surfaced the card was widening the budget (`MAX_PRIMARY = 3`).
> --- `docs/measuring-injection.md`
