---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "llmwiki epistemic routes: transcript grounding, routine and human admission, maintenance checks and later reliance."
run-id: AAS-2026-11-08-llmwiki-7f7e35008c0f-01
reviewed-boundary: "e6be788bdfd969c3695f839a5d6b5752bb233cfc"
---

# llmwiki epistemic report

## Source-and-claim boundary

Question: which shipped routes turn session material into claims, check and admit it, and license later use? The frozen scope, dependencies and exclusions are in [boundary](boundary.md#boundary-and-evidence); source identity and layers are in its [Source register](boundary.md#source-register). All findings use SRC-1 at that revision. The supplied runtime is provisional and supplies the cited passages for its routes. Additional direct reads below are implementation evidence except for skills, comments and README claims, which are doctrine/design. No target execution occurred. No supplied user wiki or trace establishes which route operated, accepted a particular proposition, or improved a task.

| Entry point or operation | Source path | Coverage and limits |
| --- | --- | --- |
| CLI dispatch and hooks | `src/cli.ts`; `hooks/hooks.json`; `src/hook-cli.ts` | Direct handler-table inspection; supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules); no additional registered MCP tool server established by this table. Host loaders remain external. |
| save, capture, update-next/done | `skill/wiki-save.md`; `src/engine/update.ts`; `src/daemon/watch.ts` | Supplied [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture); parser coverage remains as bounded there. |
| autoupdate and ingest | `src/engine/autoupdate.ts`; `src/engine/ingest.ts` | Supplied [RT-RTE-auto-update](runtime.md#rt-rte-auto-update); ingest directly read, reuses updateOne after enqueue, with force reset possible. Not a separate fact verifier. |
| grounding and lint | `src/engine/grounding.ts`; `src/engine/lint.ts` | Direct grounding read and lint citation/excerpt/structural dispatch inspection; [EPI-RTE-mechanical-check](#epi-rte-mechanical-check). Lint is not an exhaustive semantic verifier. |
| consolidate --commit | `src/engine/consolidate.ts` | Direct complete read; [EPI-RTE-topic-merge](#epi-rte-topic-merge). Material alternate writer beyond runtime's deep policy. |
| review and review-input/import | `src/engine/review.ts`; `src/engine/session-review.ts` | Direct complete reads; [EPI-RTE-semantic-review](#epi-rte-semantic-review). Partial excerpts and bounded page scope limit contradiction detection. |
| gaps, distill-verify, overview normalize, digest/spine | `src/engine/gaps.ts`; `src/engine/distill.ts`; `src/engine/overview.ts`; `src/engine/synthesis.ts` | Direct gap refresh (full gaps file reread for correction), complete distill/overview and digest/spine reads; [EPI-RTE-maintenance-view](#epi-rte-maintenance-view) contains separate [EPI-RTE-gap-disposition](#epi-rte-gap-disposition) and [EPI-RTE-navigation-view](#epi-rte-navigation-view), [EPI-RTE-distill-check](#epi-rte-distill-check). Other synthesis topic-view internals not inspected. |
| injected-feedback and recheck | `src/engine/injected-feedback.ts`; `src/engine/reported-wrong.ts`; `src/engine/knowledge-policy.ts` | Direct complete reads and turn/edit consumer ranges; [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck). Caller verification text is not independently adjudicated by hashing. |
| affinity | `src/engine/affinity.ts`; `src/engine/turncontext.ts` | Direct compute/load/rerank and consumer reads; refresh observer internals only partly inspected; [EPI-RTE-affinity-update](#epi-rte-affinity-update). No task-success inference from opens. |
| work-feedback --check | `src/engine/work-feedback.ts` | Direct complete read; [EPI-RTE-feedback-replay](#epi-rte-feedback-replay). Exact excerpt retrieval, not task execution. |
| reflection-receipt and reconcile | `src/engine/reconcile.ts` | Direct complete read; [EPI-RTE-reflection-receipt](#epi-rte-reflection-receipt). Hash continuity is distinct from semantic acceptance. |
| wiki-ask and wiki-quiz | `skill/wiki-ask.md`; `skill/wiki-quiz.md` | Direct complete reads; container [EPI-RTE-ask-quiz](#epi-rte-ask-quiz), existing ask identity [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) and quiz part [EPI-RTE-human-quiz](#epi-rte-human-quiz). Engine quiz scheduler implementation uninspected; scheduling and retention are doctrine here. |
| Human direction review and finding handling | `skill/ref/review-item.md`; `skill/ref/review-findings.md`; `skill/ref/writing.md` | Direct reads; [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance). Instructions, not an enforced signature workflow. |
| diagnostics and measurement | `evals/okf-consumer/README.md`; `src/engine/compare.ts`; `src/engine/longitudinal.ts`; `src/engine/bench.ts` | README directly read; executable diagnostic runners/results and comparison/longitudinal/bench internals not independently assessed here. Prevents a complete evaluation inventory or causal-benefit conclusion. |
| Other exposed maintenance and import surfaces | `src/commands/maintenance.ts`; `src/engine/source-freshness.ts`; `src/engine/hermes-export.ts`; `src/engine/related.ts` | Dispatch identified, detailed cleanup/migration/freshness/export/related internals uninspected. Prevents a system-complete negative about all transformations, deletions or evaluators. |
| Host models and alternate adapters | `adapters/openclaw/llmwiki.ts`; `adapters/opencode/llmwiki.ts`; `src/engine/claude.ts` | Supplied runtime findings, not independently re-audited. Host/provider internals and actual page provenance unavailable; prevents model compliance, immutable model identity and activation conclusions. |

Consequential claims are [EPI-CLM-save-retrieval](#epi-clm-save-retrieval), [EPI-CLM-topic-safety](#epi-clm-topic-safety), [EPI-CLM-distill-loss](#epi-clm-distill-loss), [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify) and [RT-CLM-tool-free](runtime.md#rt-clm-tool-free). The diagnostic README explicitly disclaims general model accuracy/productivity estimates (SRC-1, `evals/okf-consumer/README.md`; see boundary's retained passage). No unqualified system-wide absence follows from this selective inspection. In particular, commit and absence channels named by [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) were not independently inventoried here (`src/engine/commit-context.ts`, `src/engine/absent-subject.ts`, `src/engine/turncontext.ts`). This prevents a complete read-back-source or negative-claim-evaluator inventory; per-turn output must not all be attributed to accepted wiki pages. No full-history absence warrant is established.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Session facts, human decisions/reasons, topic assertions; imperative rules are a separate consumption part | see [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | SRC-1, `skill/wiki-save.md`, `src/engine/consolidate.ts` | No live instance or accepted claim trace |
| [EPI-OBJ-edit-rule](#epi-obj-edit-rule) | Imperative policy, not necessarily a factual proposition | see [EPI-OBJ-edit-rule](#epi-obj-edit-rule) | SRC-1, `src/engine/knowledge-policy.ts` | Shape/currency do not establish human provenance |
| [EPI-OBJ-quiz-record](#epi-obj-quiz-record) | Questions, answer key, human answers and model grades; schedule markers are non-truth-apt control | see [EPI-OBJ-quiz-record](#epi-obj-quiz-record) | SRC-1, `skill/wiki-quiz.md` | Doctrine only; human memory benefit unobserved |
| [EPI-OBJ-tool-facts](#epi-obj-tool-facts) | Event-derived file/command/result cards; source speech remains attributed content | see [EPI-OBJ-tool-facts](#epi-obj-tool-facts) | SRC-1, `src/engine/grounding.ts` | Tool invocation does not establish successful execution |
| [EPI-OBJ-review-report](#epi-obj-review-report) | Advisory report part: alleged contradictions, stale claims, missing concepts, next questions; gap-task part inventoried separately | see [EPI-OBJ-review-report](#epi-obj-review-report) | SRC-1, `src/engine/review.ts`, `src/engine/session-review.ts` | Bounded self/model assessment |
| [EPI-OBJ-gap-task](#epi-obj-gap-task) | Named missing-concept/next-question work items; open/resolved and absence counters are operational state, not proof of repair | see [EPI-OBJ-gap-task](#epi-obj-gap-task) | SRC-1, `src/engine/gaps.ts` | Report omission licenses work closure only, not claim truth |
| [EPI-OBJ-feedback-receipts](#epi-obj-feedback-receipts) | Version-specific usage/wrong judgments and verification statements; numerical affinity and hashes | see [EPI-OBJ-feedback-receipts](#epi-obj-feedback-receipts) | SRC-1, `src/engine/injected-feedback.ts`, `src/engine/work-feedback.ts`, `src/engine/affinity.ts` | Silver assertions and operational statistics, not gold truth |
| [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill) | Authoring and routing policy, not a task claim itself | see [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill) | SRC-1, `skill/wiki-save.md` | Natural-language compliance unobserved |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-CMP-generative-model](runtime.md#rt-cmp-generative-model) | Internal truth-apt representations not determinable | see cited components | SRC-1, `src/engine/models.ts`, `src/engine/claude.ts` | Weights/version/internal adaptation uninspected; no inference from fluency |

## Authority-route ledger

Fields owned by declarations below or supplied records are cited rather than restated. Architectural status here concerns the stated function, not observation. “Implemented” for a model prompt means the call and gate are wired, not that requested judgment is reliable.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture) | retention | implemented | [EPI-OBJ-tool-facts](#epi-obj-tool-facts) | truth-apt transformation: acquisition/import | Session source availability | see [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture) | see [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture) | Source/offset queued | Access retained | Source warrant unknown; no endorsement | Available to writers | Save/deep/autoupdate; queue; permissive; later runs | SRC-1, `src/daemon/watch.ts` | none | see [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture) | No observed activation |
| [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Extract → authored page | Host model; transcript attribution/usefulness | see [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) | Candidate summary | Authoring request | Transcript fidelity requested; not source truth | Creates pages through host tools | Host author; skill/extracts; advisory; close-out | SRC-1, `skill/wiki-save.md` | [EPI-CLM-save-retrieval](#epi-clm-save-retrieval) | see [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) | No input/output pair establishes preservation or non-entailment |
| [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) | disposition/acceptance | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Routine stable vs human direction | Host routine judgment; human Q./A. direction answer | see [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) | Stable routine / draft queue / omission | Policy, not write interception | Useful transcript-grounded handoff; human answer licenses direction only | Routine filing without individual human approval | Host and future reader; Markdown; permissive; sessions | SRC-1, `skill/ref/review-item.md` | [EPI-CLM-save-retrieval](#epi-clm-save-retrieval) | see [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) | Per-claim decision and compliance unobserved |
| [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | check/evidence production | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Candidate vs screened extract | Configured VERIFY model; every claim explicitly supported | see [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | VERIFIED or criticism | Signal consumed by engine | Extract-bounded model assessment, not answer oracle | Enables next gate only for ordinary category | updateOne; verifier text; enforcing token; candidate | SRC-1, `src/engine/autoupdate.ts` | [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify) | see [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | No observed activation |
| [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | disposition/acceptance | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Ordinary publish vs human-review queue | Engine token/optional strict paths/virtual lint; human category differs | see [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | Publish / queue / reject-skip | Enforcing branch | Recorded machine admission for wiki use; not proof; queue not accepted claim | Rejection may mark skipped; direction preserves pending | Future wiki consumers; files; permissive publication; sessions | SRC-1, `src/engine/autoupdate.ts` | [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify) | see [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | Default grounding advisory; dry-run generates without publication |
| [EPI-RTE-mechanical-check](#epi-rte-mechanical-check) | check/evidence production | implemented | [EPI-OBJ-tool-facts](#epi-obj-tool-facts) | truth-apt transformation: entailed derivation | Path presence, excerpt occurrence, structure | Regex/sets/substrings; readable local transcript for excerpt verification | see [EPI-RTE-mechanical-check](#epi-rte-mechanical-check) | Unsupported paths / lint issues | Strict path mode or caller consumes | Only encoded occurrence/structure; not proposition entailment | May block automatic page; host policy repairs lint | Engine/host; report; enforcing or advisory; invocation | SRC-1, `src/engine/grounding.ts` | none | see [EPI-RTE-mechanical-check](#epi-rte-mechanical-check) | Mention is not success evidence; lint unavailable-source silence is not verification |
| [EPI-RTE-topic-merge](#epi-rte-topic-merge) | check/evidence production | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Selected added body lines vs extract | VERIFY; optional strict paths; post-write lint | see [EPI-RTE-topic-merge](#epi-rte-topic-merge) | VERIFIED / rejection / lint errors | Token gate for selected lines | No license for deletions or untested old claims | Permits replacement; not preservation | consolidateOne; calls/reports; enforcing subset; invocation | SRC-1, `src/engine/consolidate.ts` | [EPI-CLM-topic-safety](#epi-clm-topic-safety) | see [EPI-RTE-topic-merge](#epi-rte-topic-merge) | Headings/callouts/short lines and deletions excluded from added claims |
| [EPI-RTE-topic-merge](#epi-rte-topic-merge) | disposition/acceptance | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Full candidate → live topic | WRITE proposes/chooses target; engine gates | see [EPI-RTE-topic-merge](#epi-rte-topic-merge) | Replacement/new page or skip/rejection | Write before lint | No warrant inherited from old text/human stamp | Failed new page removed; failed merge not restored | Future context/maintenance; Markdown; permissive; sessions | SRC-1, `src/engine/consolidate.ts` | [EPI-CLM-topic-safety](#epi-clm-topic-safety) | see [EPI-RTE-topic-merge](#epi-rte-topic-merge) | Rejected merge can remain live; no semantic preservation proof |
| [EPI-RTE-topic-merge](#epi-rte-topic-merge) | lifecycle integration | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Topic into reference/index/log | Engine sequencing | see [EPI-RTE-topic-merge](#epi-rte-topic-merge) | Index/edges; success log and watermark after lint | Organization for later use | Integration is not independent acceptance | Live file may remain indexed even after rejection | Indexer/future model; derived index; selection; sessions | SRC-1, `src/engine/consolidate.ts` | [EPI-CLM-topic-safety](#epi-clm-topic-safety) | see [EPI-RTE-topic-merge](#epi-rte-topic-merge) | Not transactional; rejected merge retention is not lifecycle integration after acceptance |
| [EPI-RTE-semantic-review](#epi-rte-semantic-review) | check/evidence production | implemented | [EPI-OBJ-review-report](#epi-obj-review-report) | truth-apt transformation: indeterminate | Contradictions/stale/citations/gaps | Optional model on briefs or foreground session | see [EPI-RTE-semantic-review](#epi-rte-semantic-review) | Advisory findings | No direct live-page change | Candidate criticism; L0 declared latest authority, not raw proof | Proposes conflicts/downgrades/questions | Reviewer → report; advisory; next deep | SRC-1, `src/engine/review.ts` | none | see [EPI-RTE-semantic-review](#epi-rte-semantic-review) | 500-char briefs/450-char hints; bounded pages; no raw fact check |
| [EPI-RTE-semantic-review](#epi-rte-semantic-review) | retention | implemented | [EPI-OBJ-review-report](#epi-obj-review-report) | no content change | Review output → queued draft | Format/screening or hash/scope/link checks | see [EPI-RTE-semantic-review](#epi-rte-semantic-review) | Draft saved; stale import rejected | Retains advisory artifact | accepted flag means report written, not true findings | Makes findings available to deep/gaps | Human/model; report file; advisory; future deep | SRC-1, `src/engine/session-review.ts` | none | see [EPI-RTE-semantic-review](#epi-rte-semantic-review) | No independent endorsement of findings |
| [EPI-RTE-gap-disposition](#epi-rte-gap-disposition) | disposition/acceptance | implemented | [EPI-OBJ-gap-task](#epi-obj-gap-task) | non-truth-apt policy/content update: close or reopen maintenance task | Gap open/resolved | Parsed findings + distinct complete-scope report hashes | see [EPI-RTE-gap-disposition](#epi-rte-gap-disposition) | Two absences → resolved; recurrence reopens | Tracked work changes | Non-emission heuristic, not proof fixed | Can stop selecting item for work | Deep operator; queue status; selection; later deep | SRC-1, `src/engine/gaps.ts` | none | see [EPI-RTE-gap-disposition](#epi-rte-gap-disposition) | Hash novelty not independence of epistemic judgment |
| [EPI-RTE-navigation-view](#epi-rte-navigation-view) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Overview section and graph view | Heading splice / graph-metadata assembly | see [EPI-RTE-navigation-view](#epi-rte-navigation-view) | Pointer replacing section; links/counts | Overview write or returned view | No new task explanation | Changes cold entry/navigation | Future reader; overview/spine; advisory/ranking; sessions | SRC-1, `src/engine/overview.ts` | none | see [EPI-RTE-navigation-view](#epi-rte-navigation-view) | Preserves outside section, not deleted detail; does not copy history to log |
| [EPI-RTE-distill-check](#epi-rte-distill-check) | check/evidence production | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: entailed derivation | Old/new source-name sets and conflict lines | Set inclusion and exact line equality | see [EPI-RTE-distill-check](#epi-rte-distill-check) | ok or dropped sources/conflicts | CLI failure; deep instructed stop | Mechanical preservation, not all claims | Blocks procedural continuation, not prior write | Host author; exit/report; enforcing CLI plus policy; rewrite | SRC-1, `src/engine/distill.ts` | [EPI-CLM-distill-loss](#epi-clm-distill-loss) | see [EPI-RTE-distill-check](#epi-rte-distill-check) | No semantic fidelity check |
| [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck) | check/evidence production | implemented | [EPI-OBJ-feedback-receipts](#epi-obj-feedback-receipts) | truth-apt transformation: acquisition/import | Emitted page version + caller judgment | Caller evidence statement; code checks emission identity | see [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck) | Immutable self-assessment | Not independent truth oracle | Source warrant unknown, not gold | Wrong queues recheck/removes positive affinity | Feedback recorder; state; permissive; later consumers | SRC-1, `src/engine/injected-feedback.ts` | none | see [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck) | Semantic evidence quality not assessed |
| [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck) | disposition/acceptance | implemented | [EPI-OBJ-feedback-receipts](#epi-obj-feedback-receipts) | no content change | Pending wrong → resolved revision | Caller verification + raw evidence hashes; consistency checks | see [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck) | Resolved receipt/refusal; evidence change reopens | Eligibility/warning state | Evidence-linked decision for current guidance, not entailment proof | Withholds rules, warns prose; can reopen | Rule/turn consumers; aggregate; enforcing withholding/advisory warning; version horizon | SRC-1, `src/engine/reported-wrong.ts` | none | see [EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck) | Changed page may no longer match original wrong hash; no global disputed-text ban |
| [EPI-RTE-affinity-update](#epi-rte-affinity-update) | behavior/policy adaptation | implemented | [EPI-OBJ-feedback-receipts](#epi-obj-feedback-receipts) | non-truth-apt policy/content update: bounded context reranking | Opens/usage → ranking | Smoothing/thresholds/freshness/relevance gates | see [EPI-RTE-affinity-update](#epi-rte-affinity-update) | Near-tie reorder, limited swaps | Ranking, not acceptance | Opens do not establish truth/usefulness | Changes which eligible pages fill slots | Cold/turn assemblers; engine-held JSON; ranking; days/sessions | SRC-1, `src/engine/affinity.ts` | none | see [EPI-RTE-affinity-update](#epi-rte-affinity-update) | Observer refresh partly uninspected; benefit and exercised effect unobserved |
| [EPI-RTE-feedback-replay](#epi-rte-feedback-replay) | check/evidence production | implemented | [EPI-OBJ-feedback-receipts](#epi-obj-feedback-receipts) | truth-apt transformation: entailed derivation | Top5/excerpt vs authored expectations | Deterministic replay with affinity null | see [EPI-RTE-feedback-replay](#epi-rte-feedback-replay) | pass/fail/invalidated/invalid | Diagnostic only | Retrieval/substrings, not correctness of expectations | No task execution or gold promotion | Operator; report; advisory; explicit replay | SRC-1, `src/engine/work-feedback.ts` | none | see [EPI-RTE-feedback-replay](#epi-rte-feedback-replay) | Evidence freshness checked; stored page hash not replay invalidation criterion |
| [EPI-RTE-reflection-receipt](#epi-rte-reflection-receipt) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Source range and non-draft page hashes | Receipt validation plus compare-offset mark | see [EPI-RTE-reflection-receipt](#epi-rte-reflection-receipt) | Advance bounded offset or defer | Queue bookkeeping | Hash continuity not proof of reading/grounding | Suppresses reprocessing for accepted receipt range | Capture consumers; receipt; enforcing offset; later writes | SRC-1, `src/engine/reconcile.ts` | none | see [EPI-RTE-reflection-receipt](#epi-rte-reflection-receipt) | accepted page predicate is non-draft/hash, not independent truth decision |
| [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) | content transformation | doctrine only | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: indeterminate | Wiki/raw → cited answer | Warm model; raw tracing and usefulness criterion | see [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) | Cited answer or file-back | Natural-language procedure | Grounded answer intended; user approval before file-back | Human approves file-back; host may file stable fact resynthesis | Human/model; chat/files; advisory/permissive; session/future review | SRC-1, `skill/wiki-ask.md` | none | see [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) | No source/output pair or observed approved file-back |
| [EPI-RTE-human-quiz](#epi-rte-human-quiz) | check/evidence production | doctrine only | [EPI-OBJ-quiz-record](#epi-obj-quiz-record) | no content change | Human answer vs selected wiki page | Warm model gist-grading; page is answer key | see [EPI-RTE-human-quiz](#epi-rte-human-quiz) | correct / wrong / skip | Natural-language procedure | Recall relative to page; not warrant for page truth | Grade feeds quiz-record and future recall schedule | Human/model; chat/files; advisory/permissive; session/future review | SRC-1, `skill/wiki-quiz.md` | none | see [EPI-RTE-human-quiz](#epi-rte-human-quiz) | No observed grading or scheduler implementation audit |
| [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Pages → model input | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | Pointers/excerpts/L0 | Selection, not validation | Reference data; stale warning not endorsement | May affect later choices; no proven compliance | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1, `src/engine/turncontext.ts` | [EPI-CLM-save-retrieval](#epi-clm-save-retrieval) | see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | Pointer-only/L0 exceptions prevent universal withholding conclusion |
| [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) | operational admission/selection/consumption | implemented | [EPI-OBJ-edit-rule](#epi-obj-edit-rule) | no content change | Eligible rule → reminder/deny | see [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) | see [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) | One deny then retry | Host enforcement if honored | Currency/shape not human provenance | Allows retry without obedience proof | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1, `src/engine/edit-rules.ts` | [EPI-CLM-save-retrieval](#epi-clm-save-retrieval) | see [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) | No observed activation |

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-save-retrieval](#epi-clm-save-retrieval) | see [EPI-CLM-save-retrieval](#epi-clm-save-retrieval) | SRC-1, `README.md`; doctrine/design | Explicit save plus automatic retrieval | [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules), [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | None supplied | No efficacy comparison; optional scheduled writer complicates “only at your explicit request” | Cross-session supply is architecturally wired; facts not thereby warranted | No general accuracy guarantee claimed; opt-in unattended permission differs from per-item request |
| [EPI-CLM-topic-safety](#epi-clm-topic-safety) | see [EPI-CLM-topic-safety](#epi-clm-topic-safety) | SRC-1, `src/engine/consolidate.ts`; doctrine/design comments/prompts vs implementation | Preserve every existing line; independent VERIFY; lint clean | [EPI-RTE-topic-merge](#epi-rte-topic-merge), [EPI-RTE-mechanical-check](#epi-rte-mechanical-check) | None supplied | Separate calls not enforced separate models; subset checking; lint after write | Added selected claims face a gate; old-line preservation and full rollback not enforced | Failed merge can persist; old human verified metadata can survive changed text |
| [EPI-CLM-distill-loss](#epi-clm-distill-loss) | see [EPI-CLM-distill-loss](#epi-clm-distill-loss) | SRC-1, `src/engine/distill.ts`; doctrine/design and implementation | Explicitly mechanical half only | [EPI-RTE-distill-check](#epi-rte-distill-check) | None supplied | No semantic comparison or actual rewrite trace | Deterministic source/conflict preservation check, not full claim no-loss | Broad name must retain narrow domain |
| [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify) | see [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify) | SRC-1, `src/engine/autoupdate.ts`; see cited claim | Separate WRITE/VERIFY contexts | [RT-RTE-auto-update](runtime.md#rt-rte-auto-update), [EPI-RTE-topic-merge](#epi-rte-topic-merge) | None supplied | No independent model/version identity enforcement | Second-call verification wired | Independence of judgment/errors not established |
| [RT-CLM-tool-free](runtime.md#rt-clm-tool-free) | see [RT-CLM-tool-free](runtime.md#rt-clm-tool-free) | SRC-1, `src/engine/claude.ts`; see cited claim | Recommended provider argv | [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) | None supplied | Arbitrary configured wrapper; advisory risk warning | Opt-in external generation, not an invariant sandbox | No claim of universal child tool exclusion supported |

## Bounded conclusion

- **Acquisition and reshaping:** [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture) retains transcript availability, not accepted truth. [RT-RTE-warm-save](runtime.md#rt-rte-warm-save) and [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) request source-grounded summaries of expressed decisions and work. Imported speech/tool text has unknown source warrant. Event identity and verbatim occurrence preserve limited lineage, not the truth of the asserted work outcome ([EPI-RTE-mechanical-check](#epi-rte-mechanical-check)). No observed source/output pair establishes non-ampliative fidelity, entailed task conclusions, or an accepted ampliative proposition. A useful synthesized page can still be a candidate, not a demonstrated new discovery.
- **Checks and admission differ:** routine foreground stability is model policy; human-owned direction review is a separate intended acceptance criterion ([RT-RTE-warm-save](runtime.md#rt-rte-warm-save)). Ordinary autoupdate has an operative verifier token, optional strict path test and lint gate, but direction drafts take another branch ([RT-RTE-auto-update](runtime.md#rt-rte-auto-update)). These license storage/use under named criteria, not infallibility or a known-answer oracle. [EPI-RTE-topic-merge](#epi-rte-topic-merge) further shows why return status and later force must be separated: an unsuccessful merge may leave replacement text live. Retention before successful acceptance is not lifecycle integration after acceptance.
- **Maintenance criticism is real but bounded:** [EPI-RTE-semantic-review](#epi-rte-semantic-review) wires a model check for contradictions and grounding over excerpts and retains draft findings. Host handling can add conflict callouts and re-ground topics; that latter application is doctrine, not observed operation. [EPI-RTE-gap-disposition](#epi-rte-gap-disposition), operating on [EPI-OBJ-gap-task](#epi-obj-gap-task), closes tasks by repeated report omission, not evidence of a repaired proposition. [EPI-RTE-distill-check](#epi-rte-distill-check) cannot license claim preservation merely because source labels and conflict strings survive.
- **Later authority is heterogeneous:** [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) supplies reference context and imperative edit reminders. Retired/cold/stale/source-changed/reported-wrong rules can be withheld while ordinary disputed prose remains available with warnings ([EPI-RTE-feedback-recheck](#epi-rte-feedback-recheck), [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules)). L0 and pointer-only routes differ; no global truth filter follows. Recheck resolution names a current page/evidence revision and verification statement; code consumes identity/freshness, not the statement's entailment.
- **Direct adaptive path:** [EPI-RTE-affinity-update](#epi-rte-affinity-update) changes context ranking from observed opens or explicit usage without first accepting a truth-apt project claim. This is a retained, implemented behavior-selection path, independently of model-weight change. It establishes neither improved future capacity nor exercised self-improvement: actual evidence-responsive update, later activation and causal dependence lack run evidence. Reflection has a bounded architectural witness in the representation of the system's own emissions/usage and its feedback-to-ranking/withholding path, but fidelity of every observer and live activation remain unestablished. Provider-parametric adaptation is separately uninspected; fixed/local files do not decide it.
- **Theory-builder properties remain separate:** localized page rules and method texts are inspectable (condition 1 afforded); delivery to future models is not by itself content-dependent use (condition 2 uninspected at the host). Semantic contradiction prompts and recheck statements afford content-directed criticism, but no trace establishes a challenged theory, result, blame and resulting revision/reliance change together (condition 3 uninspected). Receipts and pages afford persistence across sessions; no theory-specific criticism-to-next-round trace establishes condition 4. Addressability reaches text/page/rule units, not provider reasoning. Method texts are shipped, not shown criticized and revised against their own operation, so reflective theory building is unestablished. Human direction remains internal to those admission routes; computational autonomy of every internal operation is not established. These limits do not negate the independently implemented adaptive ranking or criticism requests.
- **Recall and evaluation are different targets:** [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) requires raw tracing and human-approved file-back for ask; [EPI-RTE-human-quiz](#epi-rte-human-quiz) instead uses a page as answer key for a human and sends grades to a human recall schedule, not to project-claim acceptance. [EPI-RTE-feedback-replay](#epi-rte-feedback-replay) checks self-authored silver retrieval expectations, not gold truth or task success. The diagnostic's published aggregates are scoped synthetic metadata/source-ID evidence, not a general accuracy or causal productivity result. Uninspected comparison/bench/cleanup branches preclude a system-complete negative about additional evaluators or truth-changing routes.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-wiki-pages
Label: Wiki claim pages and rule part

Identity: project Markdown under `docs/wiki/`: session log pages, topic encyclopedia and entry pages; task assertions are natural-language content, YAML/source IDs/links are symbolic metadata. Declared edit rules are natural-language imperative content selected by symbolic globs, distinct from ordinary reference prose. Substrate: repository files, with derived SQLite index/reference edges. Consumers and checks split in the ledger. This object is distinct from [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill), which is shipped authoring policy rather than user-project knowledge. No other supplied object denotes the retained pages. SRC-1, `src/engine/consolidate.ts`, `skill/wiki-save.md`; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) supply consumer evidence.

> //   • the TOPIC ENCYCLOPEDIA (5_topic) — per-concept, create-or-update, MERGED in place —
> //     the living page for a recurring concept, module, or pattern (built here).
> --- `src/engine/consolidate.ts`

#### EPI-OBJ-tool-facts
Label: Transcript tool fact cards

Identity: `GroundedFact` cards and `Evidence.corpus` assembled from transcript JSONL; natural-language detail plus symbolic event kinds, locators and hashes, held in current-call memory; excerpts may later enter page evidence. Source truth is not authenticated by a hash. These are distinct from shipped save policy ([RT-OBJ-save-skill](runtime.md#rt-obj-save-skill)); no supplied tool-fact object counterpart. SRC-1, `src/engine/grounding.ts`.

> kind: "file_touch" | "shell_run" | "check_result" | "vcs_commit";
> --- `src/engine/grounding.ts`

#### EPI-OBJ-review-report
Label: Semantic review report and gap task part

Identity: queued Markdown advisory report and derived gap queue; natural-language alleged defects/questions plus symbolic scope hashes, page hashes and open/resolved/absence markers. Repository files and project-state history retain them. The advisory report part feeds maintenance and gap refresh, not direct truth enforcement. This ID retains its combined report/gap-state referent; the derived work-selection part is separately declared as [EPI-OBJ-gap-task](#epi-obj-gap-task). Report-import format/snapshot checks do not govern that part's later open/resolved disposition. Distinct from [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill); the supplied [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance) is the orchestration policy, not this output object. SRC-1, `src/engine/review.ts`, `src/engine/session-review.ts`, `src/engine/gaps.ts`.

> result.accepted = true; // accepted = report written (not auto-applied to wiki)
> --- `src/engine/review.ts`

#### EPI-OBJ-feedback-receipts
Label: Feedback receipts and affinity aggregates

Identity: project-state JSON stores immutable versioned emission judgments/rechecks, silver replay expectations and bounded affinity statistics. Natural-language evidence/verification and exact expected fragments differ from symbolic page/source hashes, outcomes, counts and numerical scores. The numerical scores are localized symbolic aggregates with fixed consumer rules, not distributed model parameters. Receipts govern later warnings/rules/replay; aggregates govern bounded ranking. No supplied object counterpart after comparison with [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill); distinct from the retained claim pages. SRC-1, `src/engine/injected-feedback.ts`, `src/engine/work-feedback.ts`, `src/engine/affinity.ts`.

> outcome: "used" | "irrelevant" | "wrong" | "unknown";
> --- `src/engine/injected-feedback.ts`

#### EPI-OBJ-edit-rule
Label: Declared edit rule

Part of: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages)

Identity: `x-llmwiki` rule text and applies_to globs in project Markdown; natural-language imperative plus symbolic path eligibility, stored in page YAML and cached declarations/temporary markers. Distinct from the parent ordinary reference prose because it can block an eligible first edit and is withheld under stricter currency criteria. Closest supplied consumer is [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules), not an object duplicate. SRC-1, `src/engine/knowledge-policy.ts`; runtime supplies parsing/consumption passages.

> return !state.retired && !state.cold && !state.stale && !state.sourceChanged && !state.reportedWrong;
> --- `src/engine/knowledge-policy.ts`

#### EPI-OBJ-quiz-record
Label: Human quiz notebook and schedule ledger

Identity: `docs/wiki/6_quiz/` session records and per-person quiz-ledger. Natural-language questions/answers/grounded reveals differ from symbolic verdict/box/date markers. Stored as project Markdown; scheduled recall is the intended later consumer, not model knowledge retrieval. No supplied object counterpart after comparison with [RT-OBJ-save-skill](runtime.md#rt-obj-save-skill). Not part of the ordinary claim-page object: quiz deliberately has a separate audience and exclusion policy. SRC-1, `skill/wiki-quiz.md`, doctrine/design; scheduler implementation uninspected.

> - **One-directional loop**: wiki → human. Quiz artifacts are excluded from indexing/search/cold-start so the LLM never feeds on its own quiz output — the wiki remembers FOR the model; the quiz makes the HUMAN remember.
> --- `skill/wiki-quiz.md`

#### EPI-OBJ-gap-task
Label: Derived gap work-selection state

Part of: [EPI-OBJ-review-report](#epi-obj-review-report)

Identity: the derived gap-task part of the combined report/queue object, not the advisory review report itself. Named missing-concept/next-question text is natural language; hashes, open/resolved status, absence counters and dates are symbolic work-selection state. Substrate: machine-managed gap-queue Markdown plus project-state resolved history and consumed-review hashes. Consumers: gap refresh and the foreground deep operator selecting open work. Report import checks govern a different product. Closest supplied [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance) describes orchestration, not this object. SRC-1, `src/engine/gaps.ts` (implementation).

A resolved marker means repeated qualifying non-emission, not an independently established repaired claim. The container's criticism finding remains supported for its report part; operational disposition belongs to this task part and [EPI-RTE-gap-disposition](#epi-rte-gap-disposition).

> status: "open" | "resolved";
> absent: number; // consecutive reviews this gap was NOT emitted
> --- `src/engine/gaps.ts`

### Routes

#### EPI-RTE-mechanical-check
Label: Mechanical grounding and excerpt checks

Endpoints: source window → tool cards/support corpus; page → path/quantity/overlap report; readable transcript → quote-occurrence lint. Owner: deterministic engine. Context: rendered prose plus tool evidence; no independent source authentication. Distinct checker from [RT-RTE-auto-update](runtime.md#rt-rte-auto-update)'s end-to-end publication route and [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)'s orchestration; shared across consumers, not part of exactly one. SRC-1, `src/engine/grounding.ts`, `src/engine/lint.ts`.

Concrete code deduction, not execution: with support text `src/db.ts failed` and candidate `src/db.ts passed`, PATH_TOKEN finds the same path, so unsupportedPaths is empty; no quantitative token distinguishes these sentences. This licenses only path occurrence, not a passed check. A tool_use for Bash also mints shell_run or vcs_commit from command text without waiting for success. Non-Claude kinds yield empty structured evidence, leaving prose support. Lint checks excerpt text only when its cited transcript is locally readable; inability to check is deliberately silent. Evaluator domain is literal overlap/shape, not truth or entailment. Code selects strict path rejection only when configured; other findings are advisory. Proposal/veto belong to callers ([RT-RTE-auto-update](runtime.md#rt-rte-auto-update)); there is no answer oracle for task truth here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Grounding report, fact cards and lint issues.
- Later read-back: inapplicable — this checker does not itself persist its output; callers can retain excerpts/pages.
- Delegated visibility: inapplicable — no delegated worker in these functions.
- Selection predicate: Path/quant regex matches, metadata stripping, case normalization, path variants including basename; local transcript resolvability gates quote verification.
- Invalidation or expiry: inapplicable — outputs reflect the supplied/current source window; no retained checker state.
- Activation or effect: Consumers can reject on unsupported paths in strict mode; other literal failures may produce lint errors.
- Evidence limits: Source reading only; lexical presence is neither successful tool execution nor factual support.

> if (kind !== "claude-jsonl") return { facts, corpus: "" };
> --- `src/engine/grounding.ts`

> const unsupportedPaths = uniqMatches(PATH_TOKEN, body).filter(
>     (p) => !hay.includes(normalize(p)) && !pathVariants(p).some((v) => supported.has(v)),
>   );
> --- `src/engine/grounding.ts`

> if (tp && verifyExcerpt(ex.text, tp) === false) {
> --- `src/engine/lint.ts`

#### EPI-RTE-topic-merge
Label: Unattended topic selection and merge

Endpoints: pending source bytes → screened WRITE with bounded existing topics → model topic/target/overlap → selected added claims → VERIFY/grounding → full file write → index/refs → lint → log/watermark. Owner: engine, WRITE proposal and VERIFY veto. No per-content human approver. Intended use: durable recurring topic encyclopedia. Operating mode: open session extraction, not curriculum. No expected-answer oracle; raw extract is reference evidence. Distinct concrete --commit route from [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)'s foreground orchestration; closest alternate writer is [RT-RTE-auto-update](runtime.md#rt-rte-auto-update), but destination, own watermark and replacement semantics differ. SRC-1, `src/engine/consolidate.ts`.

The proposal guidance says preserve every old line and ground new claims in extract. addedClaims instead compares trimmed lines, excludes headings, callouts, footnotes and lines shorter than eight characters; it checks additions, not removals. A conceptual old page with bullets A and B and a replacement retaining A plus supported C loses B without B appearing in ADDED. This is a deterministic selector deduction, not a target run. No inspected superset-of-old-lines check blocks that replacement. Old verified metadata is copied as history, not fresh human confirmation. On failed post-write lint only a non-merge file is removed; merge oldContent is not restored. Thus rejected status need not withdraw operational authority. No autonomy, benefit or accepted novel proposition follows from the two model calls.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Topic/merge/overlap/verifier/grounding/lint result, accepted flag after commit.
- Later read-back: Changed topic Markdown is read by index/context and future maintenance; separate consolidated.json suppresses repeat ranges.
- Delegated visibility: WRITE sees up to 24 topics, each body capped at 1200 characters, plus screened extract; VERIFY sees extract and selected added lines, not the full replacement/history.
- Selection predicate: Model durable-concept and overlap judgment; recognized target among shown topics; exact verifier token, optional strict paths and lint.
- Invalidation or expiry: No-topic/no-new-claims and rejected commit advance own watermark. New-page lint failure removes file; merged lint failure leaves replacement. Raw source can be reprocessed manually.
- Activation or effect: Can replace live topic and update discovery even when later lint rejects. Successful continuation logs and advances state.
- Evidence limits: Separate calls, not enforced separate model identity; no full rollback/old-line preservation or observed operation.

> if (/^(---|#|>|\[\^|title:|description:|date:|updated:|tags:|status:|domain:|source:)/.test(l)) continue;
> --- `src/engine/consolidate.ts`

> const oldContent = merging ? (readRepoFile(root, destRel) ?? "") : "";
> --- `src/engine/consolidate.ts`

> writeRepoFile(root, destRel, page.endsWith("\n") ? page : page + "\n");
> --- `src/engine/consolidate.ts`

> if (!merging) removeRepoFile(root, destRel); // roll back through the boundary
> --- `src/engine/consolidate.ts`

#### EPI-RTE-semantic-review
Label: Semantic review and snapshot import

Endpoints: indexed page briefs → optional model report, or current snapshot → foreground session report → queued advisory draft. Owners: reviewer model for interpretation, engine for cadence/cache/format/snapshot controls. Target: cross-page contradiction, staleness, grounding adequacy and missing concepts/links. Prompt grants current-state/overview latest-authority priority. That priority is a policy choice, not independent source verification. Single optional call; session self-assessment is a different producer. Distinct implementation under [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)'s broad policy, not a duplicate of that policy. SRC-1, `src/engine/review.ts`, `src/engine/session-review.ts`.

Ordinary review bounds excerpts to 500 characters per page and selects recent/tag neighbors above page cap. It caches brief content, not every byte of every full page. Session preparation includes at most 40 recent pages, 450-character hints and full-byte hashes. Import checks exact current selected page set, hashes, required headings, screening and resolving local links. These checks admit a report, not certify its criticisms. Findings can later guide host conflict callouts, downgrades or raw-grounded corrections under `skill/ref/review-findings.md`; that application remains doctrine. Human direction has veto under the skill; no task-truth answer oracle or automatic semantic correctness gate.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Report preview or persisted path; imported classification session-self-assessment.
- Later read-back: Queued reports reach later deep/gaps. Review state records completion/cadence, not live-page corrections.
- Delegated visibility: Separate model call gets screened briefs; session reviewer receives snapshot hints and may read pages through host tools.
- Selection predicate: Enough pages, due/force/cache/provider conditions for review; matching unchanged bounded scope and format for import.
- Invalidation or expiry: Changed snapshot/scope rejects import. Cadence/hash cache can skip ordinary calls; incomplete launch marker leaves retry due.
- Activation or effect: Retains advisory criticism; does not directly edit live knowledge. Ordinary accepted flag means report written.
- Evidence limits: No full-page/raw verification from bounded briefs; no observed criticism or successful repair.

> export const EXCERPT_CHARS = 500; // body excerpt per page, bounded — enough to spot claims
> --- `src/engine/review.ts`

> result.accepted = true; // accepted = report written (not auto-applied to wiki)
> --- `src/engine/review.ts`

> throw new Error("review snapshot scope changed; prepare current review-input again");
> --- `src/engine/session-review.ts`

> return { path, duplicate: false, classification: "session-self-assessment" };
> --- `src/engine/session-review.ts`

#### EPI-RTE-maintenance-view
Label: Gap queue and entry views

Container scope: [EPI-RTE-gap-disposition](#epi-rte-gap-disposition) and [EPI-RTE-navigation-view](#epi-rte-navigation-view) now separately own the two route parts. They are not consecutive stages and have no common acceptance criterion or consumer. This combined ID remains a grouping only; the following combined fields summarize alternatives, not one route's pooled authority.

Two consequential parts have separate ledger rows: report findings → gap task selection/disposition, and page/index → overview/digest/spine read shaping. Engine owns deterministic state; host applies repairs. Distinct from [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)'s orchestration and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)'s delivery: this record covers the task-state/view producers. SRC-1, `src/engine/gaps.ts` (refresh range), `src/engine/overview.ts` (complete), `src/engine/synthesis.ts` (digest/spine).

Gap admission: report parser proposes tasks, code adds/reopens; complete-scope, nonduplicate reports with available history can age unmentioned items, closing after two absences. “Independent” is tested by body/scope identity, not independent reviewers or truth checks. Report omission can change work selection without establishing a gap fixed. No answer oracle; explicit maintenance mode. Scope metadata itself is not a semantic proof.

Concrete overview deduction: input `## Recent Updates\n- repaired parser\n## Direction\n- keep local\n` has its Recent Updates body replaced by the canonical log pointer; the Direction section survives. Code does not append removed text to log.md. Thus it is a non-ampliative navigation transformation, not evidence that the removed history is elsewhere. Digest/spine deterministically assemble links, degrees and freshness/open counts; those derived values warrant only their encoded index/metadata domain, not all prose on listed pages.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Gap counts/path/aging status; normalized text/size; bounded graph view.
- Later read-back: Gap queue/history guide future deep work. Overview/spine reach later entry/context readers; digest is regenerable, not independently accepted knowledge.
- Delegated visibility: inapplicable — these inspected deterministic producers launch no worker.
- Selection predicate: Latest review and parsed findings; explicit complete scope for absence aging; overview recognized section; graph degree/date/status/affinity for views.
- Invalidation or expiry: Reappearance reopens gaps; repeated/partial/unknown reports do not age absences. Views regenerate; check mode does not write.
- Activation or effect: Can stop selecting closed gaps and remove entry-page detail; views alter discovery.
- Evidence limits: Gap parser and other synthesis views not exhaustively audited; no proof a closed issue was repaired or log holds removed material.

> const mayAge = complete && !duplicate && historyAvailable;
> --- `src/engine/gaps.ts`

> if (g.absent >= RESOLVE_AFTER) {
>       g.status = "resolved";
>       g.resolvedAt = date;
>     }
> --- `src/engine/gaps.ts`

> const canonical = [lines[start]!, "", recentPointer(lang), ""];
> --- `src/engine/overview.ts`

> const next = [...lines.slice(0, start), ...canonical, ...lines.slice(end)];
> --- `src/engine/overview.ts`

#### EPI-RTE-distill-check
Label: Distill preservation check

Endpoints: old snapshot and replacement text → source/conflict comparison → CLI verdict/exit → host continuation. Owner: deterministic engine; host performs rewrite and obeys stop condition. Part of: represented below as an explicit containment field; this is the mechanical check inside [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)'s larger process, not its full semantic rewrite. SRC-1, `src/engine/distill.ts`; runtime supplies the deep instruction to pass this check.

Part of: [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance)

Target/domain: distinct lowercased source filenames parsed from footnotes and trimmed lines beginning > [conflict]. Example deduction: an old page saying “A” with source s.jsonl and a new page saying “not A” with the same source and no conflict lines produces empty dropped-source/conflict arrays and ok true. The domain is symbol/string preservation, not proposition fidelity. Engine is veto owner at CLI exit; host can already have written replacement. No answer oracle for original claim truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ok, source counts and dropped source/conflict lists.
- Later read-back: inapplicable — check itself retains nothing; snapshots/replacement persist only through host procedure.
- Delegated visibility: inapplicable — deterministic function has no worker.
- Selection predicate: All parsed old footnote source filenames and old conflict lines must remain; order/count duplicates need not.
- Invalidation or expiry: inapplicable — fresh input comparison; no accumulated checker state.
- Activation or effect: CLI can fail and deep policy forbids proceeding; no write interceptor or automatic rollback here.
- Evidence limits: No model judgment or semantic fidelity check inside verifyDistill; actual host compliance unobserved.

> ok: droppedSources.length === 0 && droppedConflicts.length === 0,
> --- `src/engine/distill.ts`

> // Claim-level fidelity still needs the model (diff against the pre-distill snapshot); this
> // gate just makes the checkable part deterministic. Uses the same citation parser as lint,
> // so "source" here means exactly what lint resolves.
> --- `src/engine/distill.ts`
#### EPI-RTE-feedback-recheck
Label: Versioned injection judgments and rechecks

Endpoints: versioned emitted-page list → caller judgment → immutable receipt → wrong queue/usage aggregate → explicit raw-evidence resolution → rule/prose consumers. Owner: caller proposes outcome/verification; code validates identity and records disposition. Operating mode: explicit close-out/recheck, not autonomous fact adjudication. No expected-answer oracle. This is distinct from [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules): they consume its flags; it produces the authority-changing state. SRC-1, `src/engine/injected-feedback.ts`, `src/engine/reported-wrong.ts`, `src/engine/knowledge-policy.ts`, `src/engine/turncontext.ts`, `src/engine/edit-rules.ts`.

Code requires exact session, emitted version/channel and concrete nonempty evidence text; no quality evaluator of that text. Outcomes used/irrelevant can feed affinity; wrong and unknown are excluded, and wrong+used is not rewarded. Wrong versions enter recheck. Resolution requires an existing item, verification text and 1–8 readable raw source/test paths outside wiki, with hashes of current page/evidence. No code judges whether the supplied raw evidence entails the verification. Hash/signature changes can reopen. A changed page no longer matching the originally reported wrong version also stops matching that original marker; this is version-specific, not an irreversible quarantine of a path.

Consumers differ: canInjectRule withholds disputed rules; ordinary turn excerpts may remain with explicit recheck warning. Pointer-only mode returns before excerpt filtering. These distinctions qualify any blanket “wrong knowledge removed” claim. Retaining a resolved record is not by itself accepted new truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Immutable receipt path, recheck items or resolved path/status.
- Later read-back: Receipts/aggregate feed later ranking, reportedWrongPages and rule/turn consumers.
- Delegated visibility: inapplicable — these deterministic recording/resolution functions do not delegate; caller judgment may come from host model.
- Selection predicate: Exact emitted version for feedback; existing wrong id, verification text and safe external-to-wiki raw evidence for resolution.
- Invalidation or expiry: Evidence/page hashes and metadata signatures bind accepted revision; edits may reopen. Feedback per session immutable; malformed/missing state is not proof.
- Activation or effect: Removes positive affinity for wrong versions; withholds rule text; warns ordinary excerpts. Resolution can restore version-specific eligibility.
- Evidence limits: No semantic evidence validation; caller identity/human contribution unresolved by API; consumer compliance and actual correction unobserved.

> if (!seen.some(s => s.page === j.page && s.channel === j.channel && s.sha256 === j.sha256))
>       throw new Error("page version was not emitted in this session");
> --- `src/engine/injected-feedback.ts`

> if (!["used", "irrelevant"].includes(j.outcome) || j.channel === "edit_rules") continue;
> --- `src/engine/injected-feedback.ts`

> return !state.retired && !state.cold && !state.stale && !state.sourceChanged && !state.reportedWrong;
> --- `src/engine/knowledge-policy.ts`

> if (e.rule && !canInjectRule(e.page)) return;
> --- `src/engine/turncontext.ts`

> if (!accepted) out.add(item.page);
> --- `src/engine/reported-wrong.ts`

#### EPI-RTE-affinity-update
Label: Usage and trace feedback to context ranking

Endpoints: emission/read observations or explicit used/irrelevant receipts → bounded aggregate → loadAffinity → adjustedScore/rerankByAffinity → future context slots. Owner: deterministic engine refresh and assemblers. Representational form: localized counts/scores/JSON with fixed rules, not neural training. Distinct adaptive producer behind [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) rather than another declaration of delivery. SRC-1, `src/engine/affinity.ts` (compute/load/rerank, partial refresh), `src/engine/turncontext.ts`, `src/engine/injected-feedback.ts`.

Input domain is observed opens and explicit usage, not correctness. Compute ignores unobserved sessions rather than coding them as unused; counts distinct sessions/days and ignores observations before page mtime. Consumer checks central state, freshness and explicit usage page hashes/mtimes, merges explicit channels, and removes reported-wrong pages from positive evidence. Promotion/demotion require repeated evidence; per-turn shift capped at 0.95 after relevance gates, recent/spine lists have limited displacement. Opens do not certify task benefit. Policy change is ranking, not a produced accepted project claim.

As improvement-directed self-change this is a standing path in context-selection organization, with objective preferentially supplying useful retained context independently specifiable from a particular ranking update. Implementation supports evidence-to-aggregate and aggregate-to-selection capacity. No supplied run establishes a particular update, its later exercise or causal task dependence (self-improvement links 1 and 4 unobserved; links 2–3 architecturally wired). Successful improvement and learning remain unestablished independently of this capacity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Refresh status or ranking values/selected list.
- Later read-back: Engine-held aggregate affects later cold/turn invocation, cached per process.
- Delegated visibility: inapplicable — inspected fold/ranking uses no delegated model worker.
- Selection predicate: Observed sessions/reads in bounded recent window; explicit used/irrelevant for same current version; enough sessions/days; relevance before per-turn rerank.
- Invalidation or expiry: Old/future/corrupt state ignored, observations reset after page changes; explicit usage freshness/hashes required; wrong removes positive evidence.
- Activation or effect: Can alter which eligible pages fill bounded context slots without enlarging context.
- Evidence limits: Observer discovery/refresh implementation only partly read; opened does not mean believed, used or useful; no exercised benefit.

> const seen = recent.filter((e) => observed.has(e.session));
> --- `src/engine/affinity.ts`

> if (aff) for (const page of reportedWrongPages(root)) delete aff.pages[page];
> --- `src/engine/affinity.ts`

> return score + Math.max(-TURN_MAX_SHIFT, Math.min(TURN_MAX_SHIFT, score * (m - 1)));
> --- `src/engine/affinity.ts`

#### EPI-RTE-feedback-replay
Label: Silver retrieval replay

Endpoints: caller query/page/evidence/required/forbidden fragments → immutable silver receipt → later checkFeedback → diagnostic. Owner: caller proposes reference expectations; engine validates and checks retrieval/substring result. No human sign-off required by API; exact computational checks are not independent truth judgment. Distinct from [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)'s production context supply: replay fixes affinity null and consumes its output as a check target. SRC-1, `src/engine/work-feedback.ts`.

1–2 cases per exact session snapshot raw evidence outside wiki and page hash. Replay invalidates changed raw evidence, then requires target in top5 plus an identified target context block containing every required and no forbidden fragment. The saved page hash is not compared as an invalidation test during replay. A changed page can intentionally pass/fail its old expectations. Result is not applied to ranking, task execution or gold labels. Operating mode is bounded self-reported regression; expected fragments are an author-supplied oracle only for exact excerpt behavior.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Receipt path or pass/fail/invalidated/invalid and top5/context booleans.
- Later read-back: Explicit later --check reads stored silver cases; no production ranking reward.
- Delegated visibility: inapplicable — no worker or model call in inspected module.
- Selection predicate: Exact session; bounded cases; readable raw evidence; top5 plus expected excerpt fragments for pass.
- Invalidation or expiry: Raw evidence snapshot changes invalidate; immutable per-session receipt cannot be replaced.
- Activation or effect: Reports retrieval regression only; does not run claimed tests or promote correctness labels.
- Evidence limits: Required/forbidden claims are self-authored; no external verification that they encode true task answers.

> const context = buildTurnContext(root, c.query, "", { affinity: null });
> --- `src/engine/work-feedback.ts`

> const ok = block !== undefined && c.required.every(s => excerpt.includes(s)) && c.forbidden.every(s => !excerpt.includes(s));
> --- `src/engine/work-feedback.ts`

> results.push({ receipt: name, query: c.query, status: top5 && ok ? "pass" : "fail", top5, context: ok });
> --- `src/engine/work-feedback.ts`

#### EPI-RTE-reflection-receipt
Label: Accepted range receipt and reconciliation

Endpoints: caller exact source range/prefix hash/page hash → recordReflection → stored content-addressed receipt → reconcileReflected → compare-offset capture mark. Engine owns consistency; caller claims it actually read and accepted content. Distinct from [RT-RTE-warm-save](runtime.md#rt-rte-warm-save)'s sequential extract receipt and [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture)'s enqueue. SRC-1, `src/engine/reconcile.ts`.

Admission criterion is a known pending transcript, valid bounded contiguous prefix, current non-draft wiki page outside queue/quiz with matching hash. No test of page semantics, evidence sufficiency or actual reading. Caller proposes, engine can veto mismatch, human involvement unresolved. This is explicit bookkeeping mode; source bytes/hash are identity reference, not expected-answer oracle. Citation discovery alone is advisory and cannot advance offset, although uncitedPending's human-facing nag excludes cited files. Reconciliation revalidates immediately before compare-and-mark; history is immutable and content-addressed. Recovery preserves unresolved/deferred pending work.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean receipt stored or reconcile lists plus commit flag.
- Later read-back: Stored receipt is revalidated in later reconcile; marked offsets shape later extraction.
- Delegated visibility: inapplicable — no delegated model in inspected module.
- Selection predicate: Known pending transcript, contiguous eligible range, current non-draft page/hash and prefix hash.
- Invalidation or expiry: Changed page/source invalidates receipt; compare-offset protects against stale queue state.
- Activation or effect: Can advance only recorded end, leaving appended tail pending; mere citation does not do this.
- Evidence limits: Receipt carries caller assertion, not proof it read/accepted a truthful page.

> if (page === null || parseFrontmatter(page).status === "draft" || digest(page) !== receipt.page_sha256) return false;
> --- `src/engine/reconcile.ts`

> const marked = !commit || capture.markIfOffset(row.transcript_path, row.byte_offset, receipt.end,
>         statSync(row.transcript_path).size > receipt.end ? "pending" : "distilled");
> --- `src/engine/reconcile.ts`

#### EPI-RTE-ask-quiz
Label: Warm ask and human recall procedures

Container scope: ask is the same referent as the supplied [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback); quiz is separately declared as [EPI-RTE-human-quiz](#epi-rte-human-quiz), a part of this combined ID. The ask counterpart already owns ask-specific proposal, human veto and file-back fields; it is not redeclared here. This ID retains both procedures as a container, not a route with a pooled oracle, approval rule or later consumer.

Two separate consumers/targets are described, not conflated into a single correctness test. Ask: explicit question → search → raw tracing → cited synthesis → user approval → file-back/checks. Host model proposes, human vetoes filing; judgment pages remain draft, resynthesized facts may be stable. Quiz: selected page → model-authored question → human answer → warm model gist-grade → quiz-record/schedule and human notebook. Here the answer key is the page, not independent evidence of its truth. Ask and quiz are distinct from [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), with stronger file-back approval for ask and a human-only output layer for quiz. SRC-1, `skill/wiki-ask.md`, `skill/wiki-quiz.md`.

These are source-native doctrine/design, not verified execution. They require inline warm work and prohibit delegation, with raw sources for ask, page reading for quiz, no model-memory guessing. Ask generally intends non-ampliative resynthesis, but no output pair establishes that classification; neither non-entailment nor new warranted conjecture is demonstrated. Quiz changes recall scheduling rather than the source page's acceptance. The quiz's localized page/question/answer/verdict notebook and symbolic ledger are separate operative parts from model-facing wiki claim pages (see quiz object below). Operating modes: open question vs bounded scheduled recall; model supplies options/grades, human supplies answers. No universal expected-answer oracle for project truth.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Cited answer and file-back offer; separately quiz questions, grades, grounded reveals and summary.
- Later read-back: Approved ask page can feed future wiki consumers. Quiz notebook/ledger are intended for human recall/scheduling, excluded from model-facing search/index.
- Delegated visibility: Inline only under both skills; host compliance unobserved.
- Selection predicate: Ask reuse value plus user approval; no-basis stop if no evidence. Quiz engine-selected pages then model judgment of core question.
- Invalidation or expiry: Ask corrections follow raw evidence and draft review policy; quiz wrong/skip rescheduled rather than revising page truth.
- Activation or effect: Human-approved ask filing changes later knowledge; quiz-record results change due dates by procedure.
- Evidence limits: Doctrine only for the full routes; quiz scheduler implementation and actual grading/memory benefit uninspected.

> 3. **Read + raw tracing**: Read the top candidate pages. For each page's footnote citation (`[^n]: <transcript/code>`), **directly Read the raw file** it points to and verify the facts (don't assert from the wiki alone).
> --- `skill/wiki-ask.md`

> 5. **Propose file-back (human confirm)**: if the answer has reuse value, ask the user "save this to the wiki?" and on approval:
> --- `skill/wiki-ask.md`

> - **Grounded questions only**: Read the page BEFORE authoring its question; the page is the answer key and the session record cites it. A question you cannot ground in a page does not get asked — never quiz on model memory.
> --- `skill/wiki-quiz.md`

#### EPI-RTE-gap-disposition
Label: Report findings to gap-task disposition

Part of: [EPI-RTE-maintenance-view](#epi-rte-maintenance-view)

Endpoints: latest semantic-review report and prior queue/history → parsed named findings → add/reopen or age missing items → persisted queue/history → later deep work selection. Owner: deterministic engine; model review proposes findings upstream, foreground model performs repairs downstream. Object: [EPI-OBJ-gap-task](#epi-obj-gap-task). Distinct from the sibling [EPI-RTE-navigation-view](#epi-rte-navigation-view); it does not normalize overview or render a graph view. Closest supplied [RT-RTE-deep-maintenance](runtime.md#rt-rte-deep-maintenance) is the broader foreground procedure. SRC-1, `src/engine/gaps.ts`, implementation.

Target/domain: task openness, not truth of a repaired proposition. Code adds or reopens parsed findings, including from partial reviews. Only explicit complete scope, a nonduplicate body/scope hash and available history permit absence aging. Two qualifying absences resolve an open task; recurrence resets it. Distinct hashes do not establish independent epistemic judgment. No human approval is required by this updater, and no answer oracle or task-truth evaluator is present. Mode: explicit maintenance refresh; check mode does not persist. Code can refuse missing/unsafe reports or malformed queues. It records consume history before queue publication to avoid counting a report twice after a crash. Guidance for the downstream foreground worker remains the deep procedure, not an automatically verified repair.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: refreshed/skip, queue path/counts and absence-aging reason.
- Later read-back: queue and resolved/history state reach later refresh; open items guide later deep work.
- Delegated visibility: inapplicable — this deterministic updater launches no worker.
- Selection predicate: latest safe semantic-review report; parsed missing-concept/next-question bullets; complete, nonduplicate scope and available history for absence aging only.
- Invalidation or expiry: recurrence reopens and resets absence; duplicate/partial/unknown/history-unavailable reports cannot age absent work; malformed queue is preserved rather than overwritten.
- Activation or effect: open/resolved state changes which items remain work candidates; it does not validate a repair or alter a project claim directly.
- Evidence limits: implementation inspected, not an observed repair or independent evaluation; downstream host compliance unobserved.

> const mayAge = complete && !duplicate && historyAvailable;
> --- `src/engine/gaps.ts`

> if (g.absent >= RESOLVE_AFTER) {
>       g.status = "resolved";
>       g.resolvedAt = date;
>     }
> --- `src/engine/gaps.ts`

#### EPI-RTE-navigation-view
Label: Overview and graph navigation shaping

Part of: [EPI-RTE-maintenance-view](#epi-rte-maintenance-view)

Endpoints: existing overview → heading-section splice → overview file (unless check); index/metadata → bounded digest or cold-start spine → returned navigation lines. Owner: deterministic engine. Sibling [EPI-RTE-gap-disposition](#epi-rte-gap-disposition) owns task-state updates; this part owns navigation production, with distinct output branches below. Closest supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) delivers the resulting context; it is not this producer. SRC-1, `src/engine/overview.ts`, `src/engine/synthesis.ts`, implementation.

Overview target is a recognized Recent Updates section, not a truth-judged candidate. It replaces that section body with a log pointer, preserving other sections, but does not copy removed history into log. The concrete input deduction in the container remains applicable only to this branch. Digest/spine assemble indexed links, backlink degrees, freshness and open-item counts. Digest uses category/degree/date limits; spine selects non-retired hubs with at least two inbound links, with bounded optional affinity adjustment. Counts are derived within index/metadata scope, not endorsement of page prose. These are reshaping/encoded derivation operations, not semantic acceptance or gap resolution. Normalization admission is caller-controlled via check vs write, without a model or human content-approval check; no project-truth answer oracle. Failure to analyze yields an empty spine rather than breaking cold start.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: overview skip/unchanged/normalized and size data; separately digest Markdown or bounded spine lines.
- Later read-back: written overview reaches later cold-start readers; digest/spine regenerate from the current index and metadata for later readers.
- Delegated visibility: inapplicable — these producers launch no worker.
- Selection predicate: recognized Recent Updates heading for overview; indexed categories, backlinks/date/status and bounded affinity for graph navigation.
- Invalidation or expiry: canonical/no-heading overview is unchanged; check does not write; digest/spine regenerate and can change with index or metadata.
- Activation or effect: removes entry-page detail in favor of a pointer or changes navigation prominence; does not close gap tasks.
- Evidence limits: no semantic no-loss test or proof removed history is elsewhere; graph output and later host use unobserved; other synthesis topic-view internals uninspected.

> const next = [...lines.slice(0, start), ...canonical, ...lines.slice(end)];
> --- `src/engine/overview.ts`

> .filter((x) => x.n >= 2 && !isRetired(parseFrontmatter(String(x.d.content ?? "")).data))
> --- `src/engine/synthesis.ts`

#### EPI-RTE-human-quiz
Label: Page-grounded human recall and schedule recording

Part of: [EPI-RTE-ask-quiz](#epi-rte-ask-quiz)

Endpoints: explicit wiki-quiz → engine-selected page pointers → foreground model reads pages and authors questions → human answers → model gist-grades → quiz-record calls, human notebook and log → later due selection. Owner: foreground model for wording/grades, human for answers, engine for declared schedule math. Object: [EPI-OBJ-quiz-record](#epi-obj-quiz-record); source pages remain [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages). This is not [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback): ask answers a project question and requests approval before file-back; quiz assesses a human against a retained page and updates recall scheduling. The existing ask identity is cited, not duplicated. SRC-1, `skill/wiki-quiz.md`, doctrine/design.

Target/domain: remembered core decision/why relative to a selected page. The page is the answer key supplied to the model, not independently warranted project truth. The model proposes questions and decides correct/wrong/skip after all answers; the human may decline participation but is not asked to approve every grade or stored item. Mode: bounded scheduled human recall, not open synthesis. Every asked item, including skips, should be recorded; wrong/skip leads to earlier re-review under the declared schedule. No approved answer file-back or page-claim revision occurs here. Guidance requires page reads, core concepts and batched questioning, with no delegation. Notebook and per-person ledger persist; concurrency guidance requires sequential record calls because ledger rewriting is not safe for parallel writers. Scheduler internals, rollback and actual grading remain uninspected; this declaration does not upgrade them to implemented behavior.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: questions, then model grades/grounded reveals and one-line recall summary.
- Later read-back: quiz notebook serves the human; per-person ledger serves later due selection, not model-facing claim retrieval.
- Delegated visibility: inline warm authorship and grading required; no subagents under the procedure.
- Selection predicate: engine-selected due/new pages and configured bounded count; model omits questions lacking page-grounded core content.
- Invalidation or expiry: wrong/skip rescheduled by declared engine policy rather than invalidating source page truth; same-day notebook reruns append, not overwrite.
- Activation or effect: grades are instructed inputs to quiz-record and future recall dates; not acceptance of the page or human answer as new project knowledge.
- Evidence limits: full procedure read; engine scheduling implementation and human memory benefit uninspected; no supplied grading trace.

> **Engine schedules, session judges**: box math, due dates, and priority are deterministic engine work; question wording and gist-grading are warm judgment. Neither side crosses over.
> --- `skill/wiki-quiz.md`

> **Grounded questions only**: Read the page BEFORE authoring its question; the page is the answer key and the session record cites it. A question you cannot ground in a page does not get asked — never quiz on model memory.
> --- `skill/wiki-quiz.md`

### Claims

#### EPI-CLM-save-retrieval
Label: Save decisions and use next time

Claimed operation: explicit model-maintained wiki preserves decisions/context and supplies future sessions; automatic hooks retrieve rather than create knowledge. Additional configured generation is opt-in. Scope is project memory, not guaranteed general truth. Distinct public memory/use claim from [RT-CLM-tool-free](runtime.md#rt-clm-tool-free) and [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify). SRC-1, `README.md`, doctrine/design.

> - **Remember the work:** save decisions, insights and project context with `/wiki-save`.
> - **Use it next time:** session-start context and per-prompt excerpts; path-specific rules before edits in Claude Code.
> --- `README.md`

> Wiki knowledge is created, changed or deleted only at your explicit request; a save hint does not authorize a write.
> --- `README.md`

The public request language is consistent with an operator opt-in but does not establish per-content human approval on unattended runs; see [RT-RTE-auto-update](runtime.md#rt-rte-auto-update).

#### EPI-CLM-topic-safety
Label: Preserve old topic lines and gate additions

Claimed operation: raw re-grounded topic merge preserves old lines, independently verifies new additions and requires clean lint. Distinct from [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify), which concerns autoupdate; this claim governs a replacement writer. SRC-1, `src/engine/consolidate.ts`, doctrine/design compared with implementation.

> - High → MERGE: output the FULL updated page — keep EVERY existing line verbatim, ADD new facts as
>   new bullets, each with its own footnote citation. Set MERGE to that page's path.
> --- `src/engine/consolidate.ts`

> // Safety reuses the log's gate: an independent strong-model VERIFY adjudicates only the
> // ADDED claims (so old grounded lines from earlier sessions aren't re-judged), a deterministic
> // grounding check rejects fabricated file paths, and lint must be clean. Default is dry-run.
> --- `src/engine/consolidate.ts`

The old-line premise is not checked by addedClaims; a rejected merge is not restored. The claim is narrower in implementation than preservation/clean-lint language suggests.

#### EPI-CLM-distill-loss
Label: Mechanical no-loss gate

Claimed operation: source citations and conflict lines survive a rewrite; claim fidelity separately needs model comparison. No supplied claim counterpart after comparison with [RT-CLM-independent-verify](runtime.md#rt-clm-independent-verify); this is deterministic preservation, not generative verification. SRC-1, `src/engine/distill.ts`, doctrine/design.

> //   1. citation superset — every footnote SOURCE cited on the old page is still cited on the
> //      new page (set semantics: two old footnotes to one source may merge into one);
> //   2. conflict callouts — every `> [conflict]` line survives verbatim.
> --- `src/engine/distill.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
