---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Kompl epistemic routes: source interpretation, admission, contradiction checks, query feedback and the limits of compounding warrant."
run-id: AAS-2026-10-14-kompl-9cffb1e5eb86-01
reviewed-boundary: "17970c969b0c2576bf722840e0e2db3c6416a7aa"
---

# Kompl epistemic report

## Source-and-claim boundary

This report asks what Kompl acquires, transforms, checks and licenses for later reliance. It adopts the whole-system scope and exclusions in [the boundary](boundary.md#boundary-and-evidence), and cites its [Source register](boundary.md#source-register) rather than reproducing it. All additional reads below are SRC-1 implementation or doctrine/design at the registered commit; checkout HEAD was checked against that commit. No target execution was performed.

The operative distinction is between installing a page and accepting its claims against evidence. The inspected routes implement the former. Prompts request faithful extraction, attribution and grounding; those requests are not results of evidence-consuming acceptance. Public knowledge/compounding claims are [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge), [EPI-CLM-source-attribution](#epi-clm-source-attribution), and [EPI-CLM-wiki-grounding](#epi-clm-wiki-grounding). The operational completion claim remains [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion).

| Entry point or operation | Source path and inspection basis | Covering records or remaining limit |
|---|---|---|
| Staging, finalization, n8n, compile driver; extraction and resolution | Supplied runtime findings at `app/src/app/api/compile/run/route.ts`, `app/src/app/api/compile/extract/route.ts`, `app/src/app/api/compile/resolve/route.ts`; direct extraction prompt/recovery reads at `nlp-service/services/llm_client.py` | [RT-RTE-session-compile](runtime.md#rt-rte-session-compile), [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [EPI-RTE-extraction-recovery](#epi-rte-extraction-recovery). Conversion branches and resolution internals not independently audited here; no complete source-fidelity or identity-correctness verdict. |
| Match and plan | Search of `app/src/app/api/compile/match/route.ts`; direct planning rules and triage implementation at `app/src/app/api/compile/plan/route.ts`, `nlp-service/services/llm_client.py` | [EPI-RTE-triage-disposition](#epi-rte-triage-disposition). |
| Draft and schema | Supplied `app/src/app/api/compile/draft/route.ts`, `app/src/app/api/compile/schema/route.ts`; direct drafting prompts at `nlp-service/services/llm_client.py` | [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [RT-RTE-schema-bootstrap](runtime.md#rt-rte-schema-bootstrap). No generated instance or semantic comparison supplied. |
| Compile crossref; exposed legacy model crossref | Direct complete app handler and injector at `app/src/app/api/compile/crossref/route.ts`, `app/src/lib/wikilink-injector.ts`; direct Python dispatch/generation at `nlp-service/routers/pipeline.py`, `nlp-service/services/llm_client.py` | [EPI-RTE-crossref-transform](#epi-rte-crossref-transform). Legacy result has no inspected app admission consumer. |
| Compile commit, explicit approval/rejection | Direct commit gates and complete `app/src/lib/approve-plan.ts`; other handlers supplied by runtime | [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval). |
| Chat answer and automatic/manual draft creation | Direct synthesis/feedback and `app/src/app/api/chat/save-draft/route.ts`; direct `insertChatDraft` in `app/src/lib/db.ts` | [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback), [EPI-RTE-chat-save](#epi-rte-chat-save). |
| Metadata answers, wiki/MCP delivery | Direct `getWikiStats` in `app/src/lib/db.ts`, complete registered tool handlers in `mcp-server/index.ts`; other readers supplied by runtime | [RT-RTE-mcp-read](runtime.md#rt-rte-mcp-read), [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback). External agent dependence remains outside boundary. |
| Lint and startup hook | Direct complete `app/src/app/api/wiki/lint-pass/route.ts`, `cli/src/startup-tasks.ts`, CLI dispatch in `cli/src/index.ts`; contradiction display in `app/src/components/WikiLintResults.tsx` | [EPI-RTE-wiki-lint](#epi-rte-wiki-lint). CLI dispatch contains lifecycle, backup and update commands, not another claim-admission workflow. |
| Contradiction sidebar | Direct `app/src/app/api/wiki/[page_id]/contradictions/route.ts` and plan activity producer | [EPI-RTE-triage-disposition](#epi-rte-triage-disposition). Advisory challenge, not automatic withdrawal of challenged prose. |
| Source deletion, redraft, source recompile and import | Supplied maintenance/import implementation; direct source recompile handler at `app/src/app/api/sources/[source_id]/recompile/route.ts` | [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance), [RT-RTE-archive-import](runtime.md#rt-rte-archive-import). Recompile queues ordinary session processing, not a new semantic evaluator. |
| Zombie cleanup and pending-draft dependency cleanup | Direct `app/src/app/api/admin/cleanup/zombie-pages/route.ts`, `findZombiePages` and `cleanupChatDraftsForDeletedPage` in `app/src/lib/db.ts` | [EPI-RTE-zombie-cleanup](#epi-rte-zombie-cleanup). |
| Saved Links regeneration/dismissal | Direct complete `app/src/lib/saved-links.ts`, `app/src/app/api/saved-links/[failure_id]/route.ts`; query searched in `app/src/lib/db.ts` | [EPI-RTE-saved-links](#epi-rte-saved-links). |
| Python registered operations | Direct `nlp-service/main.py`, pipeline dispatch and `nlp-service/routers/llm.py`; extraction/resolution/vector/storage routes supplied by runtime | No hidden provider internals assessed; direct storage writes are not evidence of checked claims. Exhaustive metadata/conversion branches unassessed, preventing system-complete negatives. |
| Product evaluators and provider reports | Direct May 5 runner/report; selected assertions searched in `scripts/integration-test.sh`; May 22 pending report supplied by boundary | [EPI-RTE-corpus-evaluation](#epi-rte-corpus-evaluation). Other manual harnesses and unit assertions not read comprehensively; no claim that all shipped tests lack semantic oracles. |

Missing evidence is local to its prevented conclusion: absent current-revision traces prevent observed grounding, evaluator activation and acceptance claims; missing exact historical corpus prevents inspecting the historical claims against their original texts; unavailable provider internals prevent inference about hidden reasoning or parameter learning; no controlled intervention/outcome comparison establishes causal improvement from compounding, citations, schema or any individual model. Available uninspected harnesses and conversion branches are inspection limits, not access gaps. No system-complete absence of semantic checking is asserted.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-extraction-output](#epi-obj-extraction-output) | Source assertions, identity assignments, relationships and summary | see record | SRC-1 `nlp-service/services/llm_client.py` | Structured shape and confidence words do not verify source truth or entailment. |
| [EPI-OBJ-draft-content](#epi-obj-draft-content) | Proposed wiki statements and source reproduction | see record | SRC-1 `nlp-service/services/llm_client.py` | Individual content is unobserved; retained raw original-source content is imported, not model-produced knowledge. |
| [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans) | None in the control portion | see record | SRC-1 `app/src/app/api/compile/commit/route.ts` | A status transition is not a factual acceptance decision. |
| [RT-OBJ-schema](runtime.md#rt-obj-schema) | Primarily instructions, not an established truth-apt theory instance | see record | SRC-1 `nlp-service/services/llm_client.py` | Exact generated rules, premises and assumptions uninspected. |
| [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) | Answer prose; selected page text and previous answers | see record | SRC-1 `app/src/app/api/chat/route.ts` | Counts describe delivered candidates, not actual citation use. |
| [EPI-RTE-triage-disposition](#epi-rte-triage-disposition) | Candidate novelty/contradiction judgment and reason | see record | SRC-1 `app/src/app/api/compile/plan/route.ts` | Comparison is against summary, not a source-truth oracle. |
| [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | Database anomaly predicates; model contradiction reports | see record | SRC-1 `app/src/app/api/wiki/lint-pass/route.ts` | Summary sample is limited; empty result also follows failed scan. |
| [EPI-RTE-saved-links](#epi-rte-saved-links) | Import-failure descriptions and count; cleared-state assertion | see record | SRC-1 `app/src/lib/saved-links.ts` | Dismissal can produce a false imported-all assertion. |
| [EPI-RTE-corpus-evaluation](#epi-rte-corpus-evaluation) | HTTP/shape/count outcomes about extraction | see record | SRC-1 `validation/2026-05-05-multi-provider-corpus/runner.py` | No semantic reference answers in that runner; reported operation is historical. |
| [RT-CMP-gemini](runtime.md#rt-cmp-gemini), [RT-CMP-deepseek](runtime.md#rt-cmp-deepseek), [RT-CMP-spacy](runtime.md#rt-cmp-spacy), [RT-CMP-key-bert](runtime.md#rt-cmp-key-bert), [RT-CMP-mini-lm](runtime.md#rt-cmp-mini-lm) | Not determinable as individuated propositions in accessible parameter state | see records | SRC-1 `nlp-service/services/llm_client.py` | Inference/derived-vector writes do not show training; exact weights and hidden provider state unavailable. |

## Authority-route ledger

The IDs below denote canonical routes or their cited material parts, not new declarations made by table rows. Architectural status refers to inspected wiring; all current-revision operation remains unobserved. Each row separates checking, disposition and retention. “No factual license” means the route supplies no demonstrated factual warrant beyond its named check, not that its content must be false.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-session-compile](runtime.md#rt-rte-session-compile) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | External sources to raw markdown | Conversion dependencies; source domain open | see record | see record | Imports selected material | Source warrant unknown; retained identity is not verification | see record | see record | SRC-1 `app/src/app/api/compile/run/route.ts` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | none | Conversion fidelity not independently established. |
| [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft) | content transformation | implemented | [EPI-OBJ-extraction-output](#epi-obj-extraction-output), [EPI-OBJ-draft-content](#epi-obj-draft-content) | truth-apt transformation: indeterminate | Sources/dossiers to extraction and prose | Models interpret source and prior prose; open subjects | see record | see record | Candidate generation | Requested faithfulness, not checked entailment | see record | see record | SRC-1 `nlp-service/services/llm_client.py` | [EPI-CLM-source-attribution](#epi-clm-source-attribution) | none | Reshaping versus ampliative content requires actual paired inputs/outputs. Non-entailment not established by synthesis alone. |
| [EPI-RTE-extraction-recovery](#epi-rte-extraction-recovery) | check/evidence production | implemented | [EPI-OBJ-extraction-output](#epi-obj-extraction-output) | no content change | Provider output shape | Parsed response/Pydantic schema | After model return | Parsed model or parse error | Gate to return | Shape only | Reject malformed output unless recovery succeeds | Extraction caller; parsed-model channel; enforcing; current call | SRC-1 `nlp-service/services/llm_client.py` | none | none | Does not test assertions against source. |
| [EPI-RTE-extraction-recovery](#epi-rte-extraction-recovery) | content transformation | implemented | [EPI-OBJ-extraction-output](#epi-obj-extraction-output) | truth-apt transformation: indeterminate | Failed response or shortened input | JSON repair; Gemini-specific halved-input fallback | Parse failure | Salvaged extraction or regenerated candidate | Return recovered candidate | No added source-truth license | May continue without complete initial input/output | Extraction caller; return value; permissive; current extraction and later drafts | SRC-1 `nlp-service/services/llm_client.py` | none | none | Recovery can remove coverage; semantic preservation not established. |
| [EPI-RTE-triage-disposition](#epi-rte-triage-disposition) | check/evidence production | implemented | see record | truth-apt transformation: indeterminate | Novelty/conflict of selected source claims against page summary | Generation model, not expected-answer oracle | Ranked candidates then model call | update/contradiction/skip with reason | Result delivered to planner | Candidate comparison only | see record | see record | SRC-1 `nlp-service/services/llm_client.py` | [EPI-CLM-source-attribution](#epi-clm-source-attribution) | none | Similarity is candidate selection, not warrant. |
| [EPI-RTE-triage-disposition](#epi-rte-triage-disposition) | disposition/acceptance | implemented | see record | no content change | Result to update/provenance/challenge | Fixed planner branches | After triage | Update plan; provenance-only plan; contradiction activity | Enforcing branches, advisory challenge | No recorded acceptance of source truth | see record | see record | SRC-1 `app/src/app/api/compile/plan/route.ts` | [EPI-CLM-source-attribution](#epi-clm-source-attribution) | Contradiction does not imply automatic withdrawal | Other rules may still draft related pages. |
| [EPI-RTE-crossref-transform](#epi-rte-crossref-transform) | content transformation | implemented | [EPI-OBJ-draft-content](#epi-obj-draft-content) | truth-apt transformation: indeterminate | Plain titles/aliases to linked prose | Regex and supplied title map; identity assumptions external to transform | Drafted before commit | Linked prose | Stored crossreffed draft | Prose reshaping conditional on correct title/alias mapping; link association not independently warranted | see record | see record | SRC-1 `app/src/lib/wikilink-injector.ts` | [EPI-CLM-source-attribution](#epi-clm-source-attribution) | No contradiction scan in app crossref | Legacy exposed model endpoint is a separate alternative within record. |
| [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval) | check/evidence production | implemented | [EPI-OBJ-draft-content](#epi-obj-draft-content) | no content change | Nonempty prose; compile body length; explicit pending state | Software predicates, not factual oracle | Before write | Pass/thin/failed/not-pending | Enforcing scoped guards | Length/status/nonemptiness only | see record | see record | SRC-1 `app/src/app/api/compile/commit/route.ts` | none | none | Explicit approval omits compile length gate; original-source exempt. |
| [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval) | disposition/acceptance | implemented | [EPI-OBJ-draft-content](#epi-obj-draft-content) | no content change | Install, queue or reject proposal | Auto-approve default; otherwise caller approval/rejection | Before installation | see record | Enforcing operational admission | Human evidence review not established; no named factual acceptance criterion recorded | see record | see record | SRC-1 `app/src/lib/approve-plan.ts` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Installation is not epistemic acceptance | Caller identity unresolved. |
| [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval) | retention | implemented | [EPI-OBJ-draft-content](#epi-obj-draft-content) | no content change | Installed prose/provenance/indexes | SQLite outbox and file flush | Following admission | see record | Persistent availability | Retention of a candidate, not lifecycle integration after factual acceptance | see record | see record | SRC-1 `app/src/lib/approve-plan.ts` | [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion) | none | File-first reads can expose old content after failed flush. |
| [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) | operational admission/selection/consumption | implemented | see record | no content change | Wiki evidence delivered for answering | Model selection or hybrid scoring, clipping/fallback | Each question | see record | Ranking and context selection | Selected snippets have no new warrant | see record | see record | SRC-1 `app/src/app/api/chat/route.ts` | [EPI-CLM-wiki-grounding](#epi-clm-wiki-grounding) | none | Selected pages may be popular fallback, not sufficient evidence. |
| [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) | content transformation | implemented | see record | truth-apt transformation: entailed derivation | Database row counts/timestamps to metadata answer | Fixed query/template; database-defined population | Recognized metadata question before retrieval/synthesis | Counts and latest stored timestamps | Direct answer/history insertion | Counts entailed by database predicates, not evidence that every counted source contributed or every page is true | Bypasses model answering | Chat user; answer text; advisory; current turn and retained history | SRC-1 `app/src/lib/db.ts` | none | Scope of counts narrower than compiled-knowledge quality | Semantic fidelity of each metadata wording not exhaustively assessed. |
| [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Selected prose/history to answer | Model; wiki-only request | After retrieval | see record | Returned and retained answer | Requested grounding, no verified entailment or citation correspondence | see record | see record | SRC-1 `nlp-service/services/llm_client.py` | [EPI-CLM-wiki-grounding](#epi-clm-wiki-grounding) | none | No actual answer pair supplied. |
| [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback), [EPI-RTE-chat-save](#epi-rte-chat-save) | retention | implemented | see records | truth-apt transformation: non-ampliative reshaping | Answer to pending wiki draft | Retrieved count or explicit content-supplying caller | After answer or save request | see records | Pending candidate, not accepted claim | No new factual license from FAQ wrapper | see records | see records | SRC-1 `app/src/app/api/chat/save-draft/route.ts` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Retrieved count is not verified use | Approval writes page IDs into source-provenance slot. |
| [RT-RTE-schema-bootstrap](runtime.md#rt-rte-schema-bootstrap) | behavior/policy adaptation | implemented | [RT-OBJ-schema](runtime.md#rt-obj-schema) | non-truth-apt policy/content update: generated drafting conventions | Page metadata to standing instructions | Model generator, nonempty write/existence checks | Initial bootstrap; later draft delivery | see record | Requested model guidance | None established for any factual premises of generated conventions | see record | [RT-BAP-schema-drafting](runtime.md#rt-bap-schema-drafting) | SRC-1 `nlp-service/services/llm_client.py` | none | none | Compliance, criticism and improvement unobserved. |
| [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | check/evidence production | implemented | see record | truth-apt transformation: indeterminate | Database anomalies and summary conflicts | SQL predicates; model for at most ten same-category pairs | Manual or overdue startup | Findings or empty contradiction list | Return/log/display, advisory | SQL facts within database; model conflicts remain candidate judgments | see record | see record | SRC-1 `app/src/app/api/wiki/lint-pass/route.ts` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Clean scan not certification | Failed model scan collapses to empty list. |
| [EPI-RTE-zombie-cleanup](#epi-rte-zombie-cleanup) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | Existence of joined provenance/source rows | SQL NOT EXISTS, database domain | Dry-run or cleanup | Zombie candidates | List supplied to deletion loop | Exact database dependency predicate, not subject-matter falsity | see record | see record | SRC-1 `app/src/lib/db.ts` | none | none | Depends on lineage identifiers being correctly typed. |
| [EPI-RTE-zombie-cleanup](#epi-rte-zombie-cleanup) | disposition/acceptance | implemented | see record | no content change | Dependency failure to deletion | Code loop; caller chooses POST | Following query | Database removal and best-effort file/vector removal | Enforcing withdrawal from normal database readers | Withdraws operational availability, not a refutation | see record | see record | SRC-1 `app/src/app/api/admin/cleanup/zombie-pages/route.ts` | none | none | Pending chat dependency pruning can leave surviving draft prose unchanged. |
| [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Surviving sources to replacement prose or provenance note | Cascade rules and drafting model | Source deletion | see record | Direct update/deletion | No checked removal of source's semantic contribution | see record | see record | SRC-1 `app/src/lib/recompile.ts` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Bypasses approval/thin gate | Note fallback retains old prose. |
| [RT-RTE-archive-import](runtime.md#rt-rte-archive-import) | disposition/acceptance | implemented | see record | truth-apt transformation: acquisition/import | Archive to restored state | Manifest/safe-ID/empty-wiki guards | Import request | see record | Direct restore | Imported warrant unknown; structural admission only | see record | see record | SRC-1 `app/src/app/api/import/route.ts` | none | none | Bypasses per-page approval and semantic checks. |
| [EPI-RTE-saved-links](#epi-rte-saved-links) | content transformation | implemented | see record | truth-apt transformation: ampliative conjecture | Empty unresolved set to imported-all statement | Fixed template | Failure resolution/dismissal/lint | Cleared-state wiki page | Direct retained assertion | Not entailed: dismissal is counterexample | see record | see record | SRC-1 `app/src/lib/saved-links.ts` | none | Unsupported cleared-state assertion | Nonempty rows mostly reshape recorded failures; this row assesses the distinct empty branch. |
| [EPI-RTE-corpus-evaluation](#epi-rte-corpus-evaluation) | check/evidence production | implemented | see record | no content change | Response key presence/counts and request outcomes | Runner; bounded historical corpus mode | Offline operator invocation | see record | Result file/report; no inspected production gate | Protocol/shape observations only, no source-truth oracle | see record | see record | SRC-1 `validation/2026-05-05-multi-provider-corpus/runner.py` | none | Provider success not semantic superiority | Quota/timeouts and missing corpus bound comparison. |
| [RT-RTE-mcp-read](runtime.md#rt-rte-mcp-read) | operational admission/selection/consumption | implemented | see record | truth-apt transformation: non-ampliative reshaping | Stored page/metadata to tool text | Explicit client requests and formatting | Tool invocation | see record | Advisory/context delivery | Preserves delivered prose, not proof of truth or lineage completeness | see record | see record | SRC-1 `mcp-server/index.ts` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | none | External scheduling/action uninspected. |

The metadata derivation is scoped to the stored database population. Its implementation premise is explicit:

>   const sourceCount = (db.prepare('SELECT COUNT(*) AS n FROM sources WHERE status = ?').get('active') as { n: number }).n;
>   const pageCount = (db.prepare('SELECT COUNT(*) AS n FROM pages').get() as { n: number }).n;
> --- `app/src/lib/db.ts`

There is no established lifecycle integration after factual acceptance in these rows. Linking, indexing and later use are real operations, but the inspected admission paths do not supply the required preceding evidence-consuming factual acceptance decision. This is scoped to the named production paths, not to every possible operator practice or uninspected test.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | see record | SRC-1 `README.md`; doctrine/design | Pipeline/planner/update prompts | [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback), [RT-RTE-schema-bootstrap](runtime.md#rt-rte-schema-bootstrap), [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | No current-revision trace | No intervention/outcome comparison; input caps and manual pending gates restrict coverage | Cross-session accumulation, promotion and update capacity are wired | Seeing patterns across all sources and maintenance-free knowledge improvement not demonstrated; bootstrap is not ongoing criticism. |
| [EPI-CLM-source-attribution](#epi-clm-source-attribution) | see record | SRC-1 `README.md`; doctrine/design | Prompts request attribution and conflicts | [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [EPI-RTE-triage-disposition](#epi-rte-triage-disposition), [EPI-RTE-crossref-transform](#epi-rte-crossref-transform) | No actual claim/citation pair supplied | Three-source relationship threshold is not independent corroboration; extracted mentions may share origin/errors | Provenance retention, comparison planning and advisory challenges implemented | Skip attaches provenance without prose change; conflict can become sidebar activity instead of comparison-page correction. Citation fidelity unverified. |
| [EPI-CLM-wiki-grounding](#epi-clm-wiki-grounding) | see record | SRC-1 `nlp-service/services/llm_client.py`; doctrine/design | Wiki-only and insufficient-information instructions | [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) | No answer trace | No entailment/citation evaluator inspected in synthesis consumer; clipping can omit needed qualification | Grounding requested over delivered snippets | Provider response schema checks shape, not grounding; returned citations are taken from model output. |
| [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion) | see record | SRC-1 `app/src/app/api/compile/run/route.ts`; implementation | see record | [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval) | see record | see record | File-flush policy, not truth acceptance | Explicit approval and import differ; durable prose can still be an unchecked candidate. |

## Bounded conclusion

Kompl acquires source texts with identities and retains generated interpretations alongside them. Source warrant remains unknown: source inclusion, extracted confidence labels, mention frequency and provenance counts do not adjudicate subject-matter truth. Generation requests faithful extraction, reproduction, synthesis and citation. Without paired generated artifacts and their actual inputs, these edges remain semantically indeterminate rather than automatically classified as entailed or ampliative. The extraction recovery route can accept repaired structure or a result generated from shorter input; successful parsing does not restore lost source coverage. See [EPI-RTE-extraction-recovery](#epi-rte-extraction-recovery) and [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft).

The inspected checks license narrower conclusions. SQL can derive database counts and dependency predicates; deterministic title injection can preserve an ordinary proposition's words while adding navigation dependent on a supplied identity map. These have no independent subject-matter warrant beyond their premises. A concrete deterministic counterexample exists in Saved Links: after dismissing the final failure, the empty-set template says all links were imported. The implementation generates a proposition not entailed by its state and demonstrably false for that reachable input history. See [EPI-RTE-crossref-transform](#epi-rte-crossref-transform), [EPI-RTE-zombie-cleanup](#epi-rte-zombie-cleanup), and [EPI-RTE-saved-links](#epi-rte-saved-links).

Operational admission is implemented, but the named routes do not record factual acceptance against evidence for a named intended use. Compile nonemptiness/body-length checks, default auto-approval, explicit caller approval, import structure guards and deletion-redraft rules all permit later wiki/model use without such an acceptance record. A caller may perform meaningful review outside the API; the source does not establish who did so or against which evidence. Candidate retention and use therefore remain distinct from acceptance and subsequent lifecycle integration. Rejection can withhold pending drafts; source/zombie deletion changes availability; neither proves surviving prose has had every removed contribution retracted. See [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval), [RT-RTE-archive-import](runtime.md#rt-rte-archive-import), and [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance).

Contradiction checks have heterogeneous force. Match triage can change planning, while its contradiction branch creates an advisory sidebar event without automatically withdrawing the page. Lint checks a small summary sample and displays/logs candidate conflicts; a failure can also yield an empty conflict list. Dependency cleanup enforces a database criterion, not semantic refutation. Approval of query-generated drafts also has a lineage caveat: cited/retrieved page IDs occupy a source-ID slot and are then passed to source provenance. Thus stored citation/provenance presence is not a uniform end-to-end warrant path. See [EPI-RTE-triage-disposition](#epi-rte-triage-disposition), [EPI-RTE-wiki-lint](#epi-rte-wiki-lint), [EPI-RTE-chat-save](#epi-rte-chat-save), and [EPI-RTE-zombie-cleanup](#epi-rte-zombie-cleanup).

Retained prose can affect later model context through drafting, answering and pending FAQ feedback, while schema prose directly requests later drafting conventions. These implemented pathways coexist with independently unestablished benefit, learning, content-directed theory criticism and exercised self-improvement. For schema, localized formulation is afforded and delivery is wired; actual decisions depending on its content, criticism and criticism-shaped iteration remain unobserved/uninspected as separated in [RT-RTE-schema-bootstrap](runtime.md#rt-rte-schema-bootstrap). There is no basis to infer hidden parameter learning or its absence across opaque providers. The corpus runner supports historical shape/protocol comparisons only; it cannot close a factual-acceptance or causal-improvement gap. No single epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-extraction-output
Label: Structured source extraction
Part of: [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

This is the material output of the extraction segment of the supplied route, not its encompassing process. It mixes natural-language claims, descriptions and summaries with symbolic JSON fields; app extraction persists it in SQLite and mention tables for later planning/dossiers. Closest supplied object [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans) is later control state, not this payload. SRC-1 implementation/doctrine: `nlp-service/services/llm_client.py`; persistence scope supplied by the parent route. Confidence is a model label about source expression, not a calibrated truth probability.

> 4. claims        — specific factual claims
>    - claim: the claim text itself (a string — full sentence)
>    - confidence: "stated" (explicit) | "implied" (strongly suggested) | "speculative"
> --- `nlp-service/services/llm_client.py`

#### EPI-OBJ-draft-content
Label: Wiki draft prose
Part of: [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

Natural-language markdown in SQLite `page_plans.draft_content`, later page files/outbox. This payload is explicitly excluded from the control-state referent of [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans). It is a material output part of the parent process, not a duplicate process. Requested source reproduction and synthesized claims differ from evidence of their production or fidelity. SRC-1 doctrine/design: `nlp-service/services/llm_client.py`; implementation/persistence supplied by parent and [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

> Synthesize across sources. Attribute specific claims to their source.
> --- `nlp-service/services/llm_client.py`

### Routes

#### EPI-RTE-extraction-recovery
Label: Extraction parse and recovery
Part of: [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

Distinct material parsing/recovery segment of the supplied generation route. The Python function returns parsed extraction, attempts JSON repair, then conditionally repeats Gemini extraction with halved text. SRC-1 implementation: `nlp-service/services/llm_client.py`. Shape acceptance is not source-truth acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed/repaired extraction or LLMCompileError.
- Later read-back: Returned output can be persisted by the app and consumed as later dossiers/mentions; no separate recovery memory is claimed.
- Delegated visibility: Initial capped markdown plus NLP hints; fallback sees half the already capped source, with paragraph-boundary trimming.
- Selection predicate: Parsed response first; salvage on parse failure; halved fallback only after unsuccessful salvage with MAX_TOKENS and Gemini model prefix.
- Invalidation or expiry: Errors prevent that return; retry inputs replace the initial candidate for this call, without a semantic completeness test.
- Activation or effect: Return/admission of recovered structure is wired; actual semantic preservation unobserved.
- Evidence limits: Schema and repair validate form, not entailment, and narrowed fallback may lose relevant text.

Proposer: model then repair/fallback code. Decider/veto: parsed-model checks and exception branches. Oracle: response schema for shape, no expected factual answer. Mode: open source extraction; trigger is parse/truncation failure. Guidance remains extraction prompt; repaired/generated output, rather than a proof, persists through the caller. Recovery can fail and surface both errors; no semantic rollback is established.

>     if result.parsed is not None:
>         return result.parsed  # type: ignore[return-value]
> --- `nlp-service/services/llm_client.py:752-753`

>     half_markdown = markdown[: len(markdown) // 2]
> --- `nlp-service/services/llm_client.py`

#### EPI-RTE-triage-disposition
Label: Triage comparison and plan disposition
Part of: [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

This material comparison/disposition segment has separate check and disposition ledger rows. SRC-1 implementation/doctrine: `nlp-service/services/llm_client.py`, `app/src/app/api/compile/plan/route.ts`, `app/src/app/api/wiki/[page_id]/contradictions/route.ts`. Models compare selected claims against a page summary; app rules map the result to a plan or activity event. Comparison-page creation independently requires a supported relationship type, historical count at least three and both entity plans; contradiction triage alone does not guarantee one.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Model decision/reason, then plans and contradiction activity.
- Later read-back: Provenance-only/update plans can affect later pages; persisted challenge events feed contradiction sidebar API.
- Delegated visibility: Selected source claims, existing summary and title; not all underlying sources or page text.
- Selection predicate: Parent route's ranked candidate filter, then update/contradiction/skip; unknown returned decision normalized to skip.
- Invalidation or expiry: A branch can omit a redraft; no automatic challenge resolution or expiry established by inspected plan/reader.
- Activation or effect: Update schedules drafting; skip may attach provenance; contradiction logs a challenge without a plan from this branch.
- Evidence limits: Other planner rules may independently target the page; model conflict does not prove either proposition false.

Proposer/evaluator: triage model; decider: fixed planner; user can cancel/exclude sources but does not necessarily review each result. No reference-answer oracle. Mode: open maintenance. Guidance defines novelty, contradiction and redundancy; reason/activity and plans persist. Operational challenge force is advisory via sidebar API; planner force is enforcing within this branch. No factual acceptance or semantic rollback established.

>     } else if (match.decision === 'contradiction') {
>       // Log a detailed activity row. The getPageContradictions(pageId) helper
>       // in db.ts json_extracts from here — keep the field names stable.
>       const srcMeta = sessionSourceMetaById.get(match.source_id);
>       logActivity('page_contradiction_detected', {
> --- `app/src/app/api/compile/plan/route.ts`

#### EPI-RTE-crossref-transform
Label: Crossref text transformation
Part of: [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

The parent route's crossref segment is deterministic in the app. SRC-1 implementation: `app/src/app/api/compile/crossref/route.ts`, `app/src/lib/wikilink-injector.ts`. Code-derived witness, without execution: input `MiniLM encodes text. MiniLM repeats.` with target title `MiniLM model` and alias `MiniLM` becomes `[[MiniLM model|MiniLM]] encodes text. MiniLM repeats.` Registration admits the six-character alias, matching finds its first word-boundary occurrence, canonical-used tracking blocks the second, and the alias branch preserves displayed surface text. A plain proposition is reshaped, but the added identity/navigation association relies on the supplied alias mapping. Conflicting aliases are first-writer-wins, so no independent identity proof follows.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: App stores linked drafts and returns counts with contradictions_found zero; exposed Python alternative returns model-edited pages/conflict candidates.
- Later read-back: App crossreffed text enters commit and later wiki consumers; no inspected app read-back of the exposed legacy model result.
- Delegated visibility: App receives draft text and targets/aliases; legacy Python generation sees provided pages, prefix-capped prompt and titles.
- Selection predicate: App nonnull drafted content; excludes own title; four-character surfaces, word boundaries and one link per canonical title; skips frontmatter/headings/code/existing links.
- Invalidation or expiry: Session draft state controls ordinary processing; identity map replacement can change future associations; no retroactive link-identity verification here.
- Activation or effect: App deterministic draft update wired; legacy endpoint model transformation wired but not current compile driver admission.
- Evidence limits: Regex cannot adjudicate the subject of a homonymous mention; legacy model request does not establish faithful reshaping or contradiction accuracy.

Proposer: input drafts and title/alias map; decider: fixed app scanner, or model for exposed Python alternative; caller supplies alternative input. No factual oracle. Mode: open compilation/direct API. Guidance in the legacy prompt requests linking/conflict notes; generated results remain returned candidates absent a demonstrated consumer. Normal rollback is through later plan/content handling, not a semantic check in this transformer.

>       if (match.toLowerCase() === canonical.toLowerCase()) {
>         return `[[${canonical}]]`;
>       }
>       return `[[${canonical}|${match}]]`;
> --- `app/src/lib/wikilink-injector.ts`

>         pages_updated: pagesUpdated,
>         wikilinks_added: wikilinksAdded,
>         contradictions_found: 0,
> --- `app/src/app/api/compile/crossref/route.ts`

#### EPI-RTE-chat-save
Label: Manual chat draft and lineage

No counterpart for the explicit content-supplying endpoint after comparison with [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback), which describes automatic retrieved-count FAQ creation. Both converge on [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval). SRC-1 implementation: `app/src/app/api/chat/save-draft/route.ts`, `app/src/lib/db.ts`, `app/src/lib/approve-plan.ts`. The endpoint accepts supplied content/citations, adds frontmatter/source display, and inserts a pending plan. It does not retrieve or authenticate a stored answer.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved true after draft insertion, or missing-session/content error.
- Later read-back: Pending draft is available for review and potential approval into later wiki context.
- Delegated visibility: API receives content, session and supplied citations; no model is called here.
- Selection predicate: Nonempty session/content; cited page IDs become pages_used then page_plans.source_ids.
- Invalidation or expiry: Pending rejection can block installation; page-deletion cleanup strips cited IDs or deletes empty chat drafts under its chat-session filter.
- Activation or effect: Candidate retention wired; shared approval loops over these same IDs as source provenance, without page-to-original-source expansion in the inspected helper.
- Evidence limits: Human content selection is afforded by UI intent, but arbitrary API caller identity and actual review remain unresolved; source-provenance slot is not typed as page lineage.

Proposer: content-supplying caller; decider: required-fields guard for pending insertion, separate approval caller for installation; veto: rejection. Mode: open manual save. No answer oracle or factual acceptance criterion. Guidance is only wrapper formatting in this endpoint; supplied prose/citation list persists. Recovery/installation follow the shared outbox path, not a new semantic evaluator.

>     .run(data.plan_id, data.session_id, data.title, JSON.stringify(data.pages_used ?? []), data.draft_content);
> --- `app/src/lib/db.ts`

>         for (const sid of sourceIds) {
>           insertProvenance({ source_id: sid, page_id, content_hash: contentHash, contribution_type: contribType });
>         }
> --- `app/src/lib/approve-plan.ts`

#### EPI-RTE-wiki-lint
Label: Wiki lint findings

No declared counterpart after comparison with runtime's maintenance account; [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance) changes source/page content, not this evaluator. SRC-1 implementation: `app/src/app/api/wiki/lint-pass/route.ts`, `cli/src/startup-tasks.ts`, `app/src/components/WikiLintResults.tsx`. SQL checks database graph/provenance/time predicates; model checks summary conflict candidates. Results return, persist in activity and display as issue/hint lists. Lint invokes Saved Links regeneration separately; it does not apply conflict-driven prose revisions in this handler.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Findings with duration, or skipped when scheduled lint disabled.
- Later read-back: Activity/results can be displayed later; last-lint timestamp changes next startup scheduling, not factual endorsement.
- Delegated visibility: Model receives flattened summaries from at most ten same-category page pairs, not complete page corpus or source texts.
- Selection predicate: Manual bypass or enabled schedule; overdue startup threshold 36 hours; SQL sample requires nonnull summaries and shared category.
- Invalidation or expiry: New lint replaces displayed latest results; no inspected result-driven automatic withdrawal of challenged prose.
- Activation or effect: Advisory issue lists and scheduling updates wired; model/provider failures can leave contradictions empty.
- Evidence limits: Empty contradictions does not mean a successful complete scan; SQL predicates support database facts, not the factual validity of wiki claims.

Proposer/evaluator: SQL and model; decider: caller/handler for running, result display rather than factual acceptance. No semantic reference oracle. Mode: open maintenance, trigger manual/startup. Guidance requests contradictions, but no truth-directed revision/recovery loop is established here. Consumer: operator; channel issue list; force advisory; horizon until later review/run.

>           WHERE a.summary IS NOT NULL AND b.summary IS NOT NULL
>           LIMIT 10`,
> --- `app/src/app/api/wiki/lint-pass/route.ts`

>   } catch {
>     // Contradiction scan is best-effort; never fail the lint for it
>   }
> --- `app/src/app/api/wiki/lint-pass/route.ts`

>           {result.contradictions.map((c, i) => (
> --- `app/src/components/WikiLintResults.tsx`

#### EPI-RTE-zombie-cleanup
Label: Provenance dependency withdrawal

No declared counterpart for admin cleanup after comparison with [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance). Cleanup reuses deletion helpers but independently selects pages from database lineage. SRC-1 implementation: `app/src/lib/db.ts`, `app/src/app/api/admin/cleanup/zombie-pages/route.ts`. This is a warranted deduction of a database predicate, not falsification of prose. A page with no provenance joined to an existing source is selected except Saved Links. Chat page IDs in source provenance can therefore satisfy the zombie predicate even when cited pages remain: the query joins sources, not pages.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: GET dry-run list; POST deleted count/list.
- Later read-back: Deleted database pages disappear from ordinary selection; pending chat drafts may have IDs pruned or be deleted when empty.
- Delegated visibility: Vector deletion receives page ID; filesystem helper sees matching page filenames; no model evaluator.
- Selection predicate: NOT EXISTS joined provenance/source row, except page_id saved-links; pending chat cleanup applies only to pending_approval sessions matching chat-%.
- Invalidation or expiry: Database deletion is enforcing; filesystem/vector deletion is fire-and-forget best effort. Surviving pending draft prose is not rewritten by the inspected SQL pruning.
- Activation or effect: Dependency-based withdrawal wired, not observed; cleanup removes lookup state independently of semantic truth.
- Evidence limits: Correct typed lineage is an auxiliary premise; dropping a dependency ID does not remove its semantic contribution from a surviving draft.

Trigger: caller POST; proposer/evaluator: dependency query; decider/executor: fixed loop; veto: caller can choose dry-run/not POST. No subject-matter oracle; bounded database predicate is the criterion for cleanup, intended use removing dangling pages. Mode: open maintenance. No automatic full rollback; backups/archives are distinct recovery possibilities, not truth acceptance.

>           AND NOT EXISTS (
>             SELECT 1 FROM provenance pr
>              JOIN sources s ON s.source_id = pr.source_id
>             WHERE pr.page_id = p.page_id
>           )`
> --- `app/src/lib/db.ts`

>       `UPDATE page_plans
>           SET source_ids = (SELECT COALESCE(json_group_array(value), '[]')
>                               FROM json_each(source_ids)
>                              WHERE value != ?)
>         WHERE draft_status = 'pending_approval'
>           AND session_id LIKE 'chat-%'
> --- `app/src/lib/db.ts`

#### EPI-RTE-saved-links
Label: Saved Links status compilation

No counterpart declared after comparison with runtime's lint mention and [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance). SRC-1 implementation: `app/src/lib/saved-links.ts`, `app/src/app/api/saved-links/[failure_id]/route.ts`, `app/src/lib/db.ts`. Natural-language status markdown is compiled from unresolved failure rows and written directly to page outbox/file/FTS. The empty branch makes a consequential claim available in wiki context, so this deterministic status path is material.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Regeneration promise; dismissal returns deleted true after failure-row deletion.
- Later read-back: Saved Links page/index content enters wiki/search and potentially answering context.
- Delegated visibility: Storage receives generated markdown; metadata descriptions/errors contribute to visible prose.
- Selection predicate: Unresolved-link query; empty list versus nonempty rendering; dismissal or lint can request regeneration.
- Invalidation or expiry: Resolution/dismissal changes queried rows; new generation replaces status content; failed flush retains outbox for startup reconciliation.
- Activation or effect: Direct write without draft approval; empty-list assertion is installed just like nonempty failure listing.
- Evidence limits: Empty unresolved set proves no remaining unresolved rows, not that every saved link was imported.

Concrete implementation deduction: start with one unresolved failed link. DELETE removes its row without ingesting it, then requests regeneration. With no unresolved rows, the template emits “All saved links have been imported into your wiki.” The conclusion is not entailed and is false for this reachable history. This requires no target execution. Proposer/decider: deterministic code, caller can dismiss; no factual oracle. Mode: operational status maintenance. Persistence/outbox recovery does not correct the assertion's semantics.

>       'All saved links have been imported into your wiki.',
> --- `app/src/lib/saved-links.ts`

>   const deleted = deleteIngestFailure(failure_id);
> --- `app/src/app/api/saved-links/[failure_id]/route.ts`

>   void regenerateSavedLinksPage().catch(() => {});
> --- `app/src/app/api/saved-links/[failure_id]/route.ts`

#### EPI-RTE-corpus-evaluation
Label: Provider corpus shape evaluation

No counterpart after comparison with runtime's production routes and components. SRC-1 implementation/reported operation: `validation/2026-05-05-multi-provider-corpus/runner.py`, `validation/2026-05-05-multi-provider-corpus/REPORT.md`. The evaluator's target is provider extraction response shape/counts over a selected file corpus, not factual truth. Historical report success is attributed, not current-revision execution. Selected integration assertions in `scripts/integration-test.sh` similarly test endpoint fields/counts/progression; exhaustive test semantics remain uninspected.

- implementation conclusion status: wired
- operation conclusion status: claimed
- Immediate return: Per-source summaries/results.json; report attributes DeepSeek seven-of-seven shape success and partial Gemini success.
- Later read-back: Durable report/results are available to developers; no inspected production decision consumer reads them.
- Delegated visibility: Providers receive source markdown with empty NER and no keyphrase/TF-IDF hints via extraction endpoint.
- Selection predicate: Sorted corpus markdown files, both named providers; reported timeouts have a separate rerun.
- Invalidation or expiry: Report is historical; reruns overwrite runner results; exact original corpus unavailable in tracked source.
- Activation or effect: Evaluator wiring supports recording outcomes, not an implemented factual acceptance gate.
- Evidence limits: Key presence/counts are not source fidelity; quota, filtering and timeout differences confound attribution of semantic capability or component effect.

Proposer: provider extractions; evaluator/decider: runner shape summary, developer interprets report; no expected factual answer oracle. Mode: bounded corpus experiment, not production admission. No semantic rollback/rejection downstream consumer inspected. Criteria measure protocol/shape outcomes; inference of knowledge accuracy exceeds their domain.

>     if "entities" in resp and "concepts" in resp:
>         return {
>             "ok": True,
> --- `validation/2026-05-05-multi-provider-corpus/runner.py`

### Claims

#### EPI-CLM-compiled-knowledge
Label: Compounding compiled knowledge

No counterpart after comparison with runtime's scoped durability/deployment claims. SRC-1 doctrine/design: `README.md`. The public claim combines automatic organization/update, cross-source pattern recognition and compiled knowledge; it does not itself establish observed or accepted ampliative knowledge.

> Kompl is a compounding LLM-wiki, best fit for a personal second brain that
> organizes and updates itself as it grows, without maintenance or upkeep on your
> end.
> --- `README.md`

> pattern across all ten without you having to ask.
> --- `README.md`

#### EPI-CLM-source-attribution
Label: Conflicts and source attribution

Distinct from [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion): this concerns claim-level attribution and disagreement, not file persistence. SRC-1 doctrine/design: `README.md`.

> promoted into their own pages. When sources disagree, the disagreement surfaces
> on a comparison page with provenance. Claims cite where they came from. By the
> time you have a question, the answer is already a page.
> --- `README.md`

#### EPI-CLM-wiki-grounding
Label: Wiki-only answer contract

No counterpart claim after comparison with [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback), which describes the implementation container. SRC-1 doctrine/design: `nlp-service/services/llm_client.py`. This is a requested warrant constraint, not an observed grounded answer.

> You are a wiki-grounded knowledge assistant. Answer the user's question using
> ONLY the wiki pages provided. Do not use general knowledge — your answer must
> be grounded in the provided pages.
> --- `nlp-service/services/llm_client.py`
