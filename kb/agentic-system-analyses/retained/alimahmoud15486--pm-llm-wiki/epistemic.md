---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "pm-llm-wiki epistemic routes: source-linked product beliefs, PM admission, contradiction handling and the limits of cited deliverables."
run-id: AAS-2026-11-09-pm-llm-wiki-4c3839e25928-01
reviewed-boundary: "64fb748ac9d187be4c51636aa56bfee1d9e5b116"
---

# pm-llm-wiki epistemic report

## Source-and-claim boundary

This analysis asks how curated product evidence becomes a maintained belief, a permitted decision or a later deliverable, and what warrants those transitions. Scope, exclusions and frozen evidence identity: see [boundary](boundary.md#boundary-and-evidence). Sources and evidence layers: see [Source register](boundary.md#source-register). SRC-1 supplies doctrine/design and reported operation, not inspected executable behavior or authenticated agent traces. The complete shipped prompt-and-state loop is included; the external coding agent, provider, permissions and context-loading machinery are excluded. The pilot is fictional. Its pages establish available candidate instances, not observed production, checking or acceptance by the described agent.

The consequential claims are the citation/unsupported-label policy, see [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control), and the broader defensibility/ground-truth rhetoric, see [EPI-CLM-defensible-claims](#epi-clm-defensible-claims). Candidate generation, source admission, checking, permission, retention and downstream use must be separated: a PM-authorized write is not automatically epistemic acceptance.

### Material operation coverage

“Direct” means source text read for this member at SRC-1's registered revision; “supplied” means the runtime finding was also used. No CLI, hook, registered tool or executable evaluator is shipped in the tracked tree; the entry points are natural-language requests. The tracked-file listing and README's explicit no-code statement bound that packaging conclusion, not the behavior of an external host.

| Entry point or operation | Source path and inspection basis | Covering records or limit |
|---|---|---|
| Setup and instruction loading | Direct: `README.md`, `template/SCHEMA.md`, `pilot/CLAUDE.md`; supplied runtime | See [RT-OBJ-schema](runtime.md#rt-obj-schema), [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent). Actual loading and model compliance remain uninspected. |
| Source placement; digest admission; skip branch | Direct: `template/SCHEMA.md`; supplied runtime | See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [EPI-OBJ-source-files](#epi-obj-source-files). Raw exports and upstream measurement implementations are not supplied. |
| Problem synthesis and confirmation | Direct: `template/SCHEMA.md`, `pilot/wiki/problems/plans-dont-adapt.md`, `pilot/wiki/problems/price-value-gap.md`, `pilot/log.md` | See [EPI-OBJ-problem-pages](#epi-obj-problem-pages), [EPI-RTE-problem-confirmation](#epi-rte-problem-confirmation). |
| Belief checks and PM status admission | Direct: `template/SCHEMA.md`, `pilot/wiki/assumptions.md`, `pilot/sources/2026-06-25_analytics_cohort-retention-readout.md`, `pilot/log.md`; supplied runtime | See [EPI-OBJ-assumptions](#epi-obj-assumptions), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). No raw PM approval conversation. |
| Decision admission, reversal and supersession | Direct: `template/SCHEMA.md`, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`, `pilot/wiki/open-questions.md`, `pilot/sources/2026-07-02_intel_gymjoy-coach-launch.md`; supplied runtime | See [EPI-OBJ-decision-page](#epi-obj-decision-page), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint). No completed product experiment. |
| Index-first query and optional file-back | Direct: `pilot/index.md`, `pilot/wiki/overview.md`, `pilot/wiki/prd-adaptive-plans-v1.md`, `template/SCHEMA.md`, `pilot/log.md`; supplied runtime | See [EPI-OBJ-prd](#epi-obj-prd), [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback). No later trace consuming the filed PRD. |
| Weekly truth check; question closure; discovery planning | Direct: `template/SCHEMA.md`, `pilot/wiki/open-questions.md`, `pilot/log.md`; supplied runtime | See [EPI-OBJ-open-questions](#epi-obj-open-questions), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint). Detection completeness and subsequent research execution are unobserved. |
| Stage change; competitor upkeep | Direct: `pilot/CLAUDE.md`, `pilot/wiki/competitors/gymjoy.md`, `pilot/log.md`, `template/SCHEMA.md`; supplied runtime | See [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade). Schema changes are policy adaptation, not proof of improved epistemic capacity. |
| Repository contribution and fresh-agent check | Direct: `CONTRIBUTING.md`, `README.md`; supplied runtime | See [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade). Manual check requested; no transcript, expected-answer key or comparison supplied. |
| Draft extensions and contextual lineage | Direct: `PM-Wiki-Content-Model.md`; boundary's supplied coverage for `reference/` | Design draft is not the active schema. Reference texts were not independently reread here; they do not establish additional deployed operations. |

Missing host implementation prevents enforcement and provider-state conclusions. Missing raw sessions prevents observed model compliance and role attribution. Missing raw analytics prevents independent checking of imported measurements. Fictional evidence and missing outcomes prevent real-product causal benefit conclusions. Available source material not independently reread here includes the other five raw pilot inputs; therefore this member does not certify every source-to-page paraphrase. Those files' roles and existence are supplied by the boundary, not treated as new independently checked evidence. These limits do not prevent assessing the explicit acceptance and authority design.

## Epistemic-object inventory

The object records own their identity, form, substrate and passages; entries below are a sparse overlay. The model component is separately described in [RT-CMP-llm-agent](runtime.md#rt-cmp-llm-agent): no version is pinned, and parameter change or mutable-endpoint behavior cannot be determined from this repository. No conclusion about online weight learning follows from wiki revision.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-files](#epi-obj-source-files) | Imported testimony, readout findings and competitor reports | Curated evidence | SRC-1, `template/SCHEMA.md` | Immutable by instruction; source truth not authenticated. |
| [EPI-OBJ-problem-pages](#epi-obj-problem-pages) | Pain-point interpretation, occurrence evidence, causal generalizations | Emerging/confirmed/addressed product problems | SRC-1, `pilot/wiki/problems/plans-dont-adapt.md` | Confirmation threshold is not a causal test. |
| [EPI-OBJ-assumptions](#epi-obj-assumptions) | A1–A4 load-bearing beliefs and bounded reliance statuses | Explicit belief register | SRC-1, `pilot/wiki/assumptions.md` | A2 is correlational; A4 remains untested. |
| [EPI-OBJ-decision-page](#epi-obj-decision-page) | Factual premises and rationale; the roadmap commitment itself is policy | Decision record and reversal criteria | SRC-1, `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md` | A permitted bet need not be a proven causal explanation. |
| [EPI-OBJ-open-questions](#epi-obj-open-questions) | Questions are not assertions; proposed explanations/designs and reported answers can be truth-apt | Discovery queue | SRC-1, `pilot/wiki/open-questions.md` | Q1 experiment is proposed, not run. |
| [EPI-OBJ-prd](#epi-obj-prd) | Imported facts, derived totals, interpretive generalizations; feature choices are policy | Filed deliverable/exploration | SRC-1, `pilot/wiki/prd-adaptive-plans-v1.md` | Draft retention is not epistemic acceptance. |
| [RT-OBJ-schema](runtime.md#rt-obj-schema) | Mainly non-truth-apt operating instructions; factual product context is mixed in | Governing guidance | SRC-1, `pilot/CLAUDE.md` | See declaring record; instruction delivery is not compliance. |
| [EPI-OBJ-index](#epi-obj-index) | Selected descriptive page summaries | Catalog and first-read selector | SRC-1, `pilot/index.md` | Summaries can preframe a claim before full-page checking. |
| [EPI-OBJ-overview](#epi-obj-overview) | Current interpreted churn picture and strategy | Living synthesis | SRC-1, `pilot/wiki/overview.md` | Interpretive summaries, not independently verified conclusions. |
| [EPI-OBJ-gymjoy](#epi-obj-gymjoy) | Competitor capability reports and strategic implications | Stage-2 competitor knowledge | SRC-1, `pilot/wiki/competitors/gymjoy.md` | Price/capability restatements and market implications have different inferential warrant. |

## Authority-route ledger

All architectural statuses below are **doctrine only**: readable instructions plus fictional reported operations do not become executable implementation evidence. Repeated route citations identify separate functions of the same supplied route, not new declarations. The ledger owns architectural classification and distinguishes results from their downstream force; record-owned progression and evidence are cited rather than redefined.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-source-files](#epi-obj-source-files)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: curated file or approved digest entering the evidential corpus.
Evaluator/condition and domain: PM selects sources; an agent-drafted high-volume digest requires PM approval as a source. No independent source-truth evaluator is specified.
Activation and timing: PM-selected ingest, before synthesis.
Possible or observed result: source availability; only reported operation in the pilot.
Implemented force: none established; prescribed admission policy.
Epistemic authority and scope: source warrant unknown; read-only lineage preserves an attributed statement, not its truth. Digest compression fidelity is not independently checked here.
Operational authority: behavior permitted, blocked, or changed: ingest a curated source; do not ingest raw dumps; log-only if nothing changes.
Behavioral-authority path: consumer, channel, force, horizon: external agent, source file plus task context, permissive policy, current ingest and later evidence reads.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`; see route and object for passages.
Claim IDs or none: [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control), [EPI-CLM-defensible-claims](#epi-clm-defensible-claims).
Mismatch marker or none: source authority is not independently warranted.
Gap/limit: PM curation establishes selection, not accuracy; no observed digest review supplied.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-problem-pages](#epi-obj-problem-pages), [EPI-OBJ-assumptions](#epi-obj-assumptions)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: source takeaways, problem synthesis and candidate belief revisions.
Evaluator/condition and domain: external agent interpreting evidence; no general entailment checker or answer oracle.
Activation and timing: source read, before proposing statuses and filing freely writable content.
Possible or observed result: new or extended assertions, evidence links and counts.
Implemented force: none established; synthesis and filing are requested.
Epistemic authority and scope: source-cited candidate claims, not universally warranted generalizations. Simple restatement can be non-ampliative; 34% + 29% = 63% is conditionally entailed arithmetic; interpreting that total as adaptivity-caused churn is ampliative. Classification varies by edge.
Operational authority: behavior permitted, blocked, or changed: write problem evidence and overview freely; propose protected changes.
Behavioral-authority path: consumer, channel, force, horizon: later query agent/PM, retained wiki narrative, advisory framing and selection, subsequent tasks.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/wiki/problems/plans-dont-adapt.md`; see object passages.
Claim IDs or none: [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control).
Mismatch marker or none: citation does not settle inference validity.
Gap/limit: no guarantee of semantic preservation; exact interpretations remain edge-specific rather than classifying the whole ingest as conjecture.

Route ID: [EPI-RTE-problem-confirmation](#epi-rte-problem-confirmation)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-problem-pages](#epi-obj-problem-pages)
Content/update relation: no content change
Transition or check target: whether a pain point meets the named evidence-diversity threshold; separately, measured effect for addressed status.
Evaluator/condition and domain: see route; agent assesses source independence/types and measurement evidence under the schema.
Activation and timing: during source ingest or later evidence review.
Possible or observed result: threshold assessment; pilot journal reports confirmation.
Implemented force: none established; no executable count or independence check.
Epistemic authority and scope: qualifies evidence accumulation for PM problem framing, not causal identification or population prevalence.
Operational authority: behavior permitted, blocked, or changed: check informs status admission in the next row; it does not itself authorize a roadmap.
Behavioral-authority path: consumer, channel, force, horizon: agent status-writing decision, evidence assessment in context, advisory criterion, current ingest.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`; see route passage.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: source independence requires interpretation; mention count is not a count of independent people or causal replications.

Route ID: [EPI-RTE-problem-confirmation](#epi-rte-problem-confirmation)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-problem-pages](#epi-obj-problem-pages)
Content/update relation: non-truth-apt policy/content update: assign problem reliance status
Transition or check target: emerging → confirmed, or addressed after measured shipped effect.
Evaluator/condition and domain: see route for agent proposal/decision and PM control boundaries. The criterion concerns a pain point's evidence support for product framing.
Activation and timing: after assessing evidence, before/with freely permitted problem-page write.
Possible or observed result: confirmed status exists in the fictional page; journal attributes it to survey/timing evidence.
Implemented force: none established; model-interpreted status policy.
Epistemic authority and scope: a doctrine-level evidence-consuming acceptance criterion exists for the problem's intended use; it does not license “adaptivity causes retention.”
Operational authority: behavior permitted, blocked, or changed: present the problem as confirmed in later briefs; addressed requires a measurement, not merely shipping.
Behavioral-authority path: consumer, channel, force, horizon: later agent/PM, page status and index summary, advisory reliance/ranking, later product work.
Evidence source ID and local anchor: SRC-1, `pilot/log.md`, `pilot/wiki/problems/plans-dont-adapt.md`; see route.
Claim IDs or none: none.
Mismatch marker or none: no automatic equivalence between confirmed and causally established.
Gap/limit: journal is reported operation, not a trace showing the test was faithfully applied.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-assumptions](#epi-obj-assumptions)
Content/update relation: no content change
Transition or check target: A1 price explanation, A2 adaptivity/retention, A3 annual-plan effect, A4 rules-based sufficiency, each over the pilot's product scope.
Evaluator/condition and domain: agent compares source contents with each belief; correlation must remain distinguished from causation; no causal experiment or expected-answer oracle supplied.
Activation and timing: every ingest, with counter-evidence also sought at lint.
Possible or observed result: proposal to weaken, validate with qualification, invalidate or retain status; example retains uncertainty for A2–A4.
Implemented force: none established; criticism and proposal are instructed.
Epistemic authority and scope: A1 has explicit contrary testimony; A2 has correlational evidence only; A3/A4 remain untested. These are independent findings, not a global truth verdict.
Operational authority: behavior permitted, blocked, or changed: propose a status change; unchanged-status evidence additions have an explicit free-write exception.
Behavioral-authority path: consumer, channel, force, horizon: PM, proposal with source evidence in conversation, advisory, until direct decision.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/wiki/assumptions.md`; see [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).
Claim IDs or none: [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control).
Mismatch marker or none: do not read the final blanket Assumptions prohibition as cancelling the detailed exception.
Gap/limit: no general quantitative validation criterion for assumptions; causal source limitations survive status labels.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-assumptions](#epi-obj-assumptions), [EPI-OBJ-decision-page](#epi-obj-decision-page), [RT-OBJ-schema](runtime.md#rt-obj-schema)
Content/update relation: non-truth-apt policy/content update: grant protected-write permission
Transition or check target: assumption status change, new decision, supersession or schema edit.
Evaluator/condition and domain: direct PM reply to agent proposal in the current conversation; relayed approval is insufficient. PM decides and can veto; agent proposes and executes I/O.
Activation and timing: before protected write; pending until direct reply.
Possible or observed result: approve, correct, withhold; journal reports coordinator relay held pending and direct approval later applied.
Implemented force: none established; no authenticated identity or filesystem check.
Epistemic authority and scope: PM permission licenses the write. Source-linked A1 revision illustrates evidence-responsive reliance, but approval alone is not a general truth test or an evidence-consuming acceptance criterion for every claim.
Operational authority: behavior permitted, blocked, or changed: permit the specific edit or hold it pending; retain existing decision/status on rejection.
Behavioral-authority path: consumer, channel, force, horizon: agent writer, direct conversation reply, permissive policy, proposed edit then durable downstream effect.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/log.md`; see cited route passages.
Claim IDs or none: [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control).
Mismatch marker or none: permission versus epistemic acceptance.
Gap/limit: new assumption registration is not explicitly resolved by the detailed gate; arbitrary manual/host writes are not mediated.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-problem-pages](#epi-obj-problem-pages), [EPI-OBJ-assumptions](#epi-obj-assumptions), [EPI-OBJ-prd](#epi-obj-prd)
Content/update relation: no content change
Transition or check target: keeping written evidence, beliefs and optional explorations in local Markdown.
Evaluator/condition and domain: source relevance/skip rule; optional value judgment for file-back; protected changes still require PM permission.
Activation and timing: after free-write selection or protected approval; query answer may remain only in-message.
Possible or observed result: durable page plus index/log entry; pilot provides a filed PRD candidate.
Implemented force: none established; retained files exist but route execution is not authenticated.
Epistemic authority and scope: retention establishes future availability only; it neither accepts every proposition nor makes a generated answer an independent corroborating source.
Operational authority: behavior permitted, blocked, or changed: expose content to later index-first tasks.
Behavioral-authority path: consumer, channel, force, horizon: later agent/PM, local files and catalog, advisory supply, potentially across sessions.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/log.md`, `pilot/index.md`; see [EPI-OBJ-prd](#epi-obj-prd).
Claim IDs or none: [EPI-CLM-defensible-claims](#epi-clm-defensible-claims).
Mismatch marker or none: retention is not acceptance.
Gap/limit: no independent provenance trace for the PRD's actual generation and no later PRD-use trace.

Route ID: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-problem-pages](#epi-obj-problem-pages), [EPI-OBJ-assumptions](#epi-obj-assumptions)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: accepted status-linked beliefs/problems connected to evidence and related pages for later use.
Evaluator/condition and domain: agent files evidence/history and cross-links following the problem criterion or PM-approved revision. This function is conditional on acceptance, not all ingest writes.
Activation and timing: after the relevant acceptance; index and overview refreshed with the changed picture.
Possible or observed result: source-linked history and related-page organization; fictional A1 history and PRD provide design-consistent examples.
Implemented force: none established; prescribed integration and example state.
Epistemic authority and scope: organizing an accepted item carries its bounded warrant, not additional truth from backlinks. Retention before acceptance stays in the preceding function.
Operational authority: behavior permitted, blocked, or changed: later queries can locate the accepted status and supporting/contrary evidence.
Behavioral-authority path: consumer, channel, force, horizon: later query agent, linked pages/index, advisory framing, subsequent tasks.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/wiki/assumptions.md`; see object and supplied route.
Claim IDs or none: [EPI-CLM-defensible-claims](#epi-clm-defensible-claims).
Mismatch marker or none: all-page “integration” rhetoric is broader than this acceptance-qualified function.
Gap/limit: no observed route trace showing that acceptance preceded each retained page.

Route ID: [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-prd](#epi-obj-prd), [EPI-OBJ-assumptions](#epi-obj-assumptions), [EPI-OBJ-open-questions](#epi-obj-open-questions)
Content/update relation: no content change
Transition or check target: which retained material enters a new answer or discovery plan.
Evaluator/condition and domain: agent interprets PM question, reads index first and only relevant pages. Queue tags route proposed work; no deterministic retrieval/ranking implementation.
Activation and timing: PM query, before synthesis.
Possible or observed result: selected evidence and beliefs in the answer context; PRD reports wiki plus raw-source use.
Implemented force: none established; instruction-mediated selection.
Epistemic authority and scope: source and status qualifications should remain attached; retrieval is not revalidation. The catalog can itself preframe a claim before detailed checking.
Operational authority: behavior permitted, blocked, or changed: A2's uncertainty informs proposed holdout rollout; Q1/Q5 supply discovery work, not executed research.
Behavioral-authority path: consumer, channel, force, horizon: answer agent then PM, index/page text into task and deliverable, advisory/ranking, current query and potential future filed answers.
Evidence source ID and local anchor: SRC-1, `pilot/index.md`, `pilot/wiki/prd-adaptive-plans-v1.md`, `template/SCHEMA.md`; see supplied route and PRD record.
Claim IDs or none: [EPI-CLM-defensible-claims](#epi-clm-defensible-claims).
Mismatch marker or none: delivery is not compliance or benefit.
Gap/limit: host window management, exact selection and actual decision influence are unobserved.

Route ID: [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-prd](#epi-obj-prd)
Content/update relation: truth-apt transformation: ampliative conjecture
Transition or check target: the PRD's categorical generalization that price is the exit justification, not the cause.
Evaluator/condition and domain: agent synthesis from selected pages under citation policy; no source-truth/entailment acceptance gate for each deliverable sentence.
Activation and timing: query synthesis, before optional filing.
Possible or observed result: a categorical assertion exists in the filed draft; generation route remains reported, not observed.
Implemented force: none established; natural-language draft.
Epistemic authority and scope: the conclusion does not follow from two disclaiming interviews plus a survey where 18% report price; Q2 explicitly leaves the interpretation open. This is positive evidence of non-entailment/uncertainty, not classification from failure to prove entailment alone.
Operational authority: behavior permitted, blocked, or changed: pricing excluded from PRD scope; proposal remains draft, not executed roadmap change.
Behavioral-authority path: consumer, channel, force, horizon: intended Dana/Omar/PM readers, retained PRD non-goals, advisory framing, Q3 planning and potential later queries.
Evidence source ID and local anchor: SRC-1, `pilot/wiki/prd-adaptive-plans-v1.md`, `pilot/wiki/open-questions.md`, `pilot/wiki/assumptions.md`; see [EPI-OBJ-prd](#epi-obj-prd).
Claim IDs or none: [EPI-CLM-defensible-claims](#epi-clm-defensible-claims), [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control).
Mismatch marker or none: qualifier loss between open hypothesis and categorical downstream claim.
Gap/limit: a source citation makes the interpretation inspectable but does not warrant its expanded scope; the draft's A1-weakening link partially signals uncertainty without qualifying the categorical sentence.

Route ID: [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-decision-page](#epi-obj-decision-page), [EPI-OBJ-assumptions](#epi-obj-assumptions), [EPI-OBJ-open-questions](#epi-obj-open-questions)
Content/update relation: no content change
Transition or check target: contradictions, counter-evidence, decision-specific reversal conditions, orphan/stale pages and missing research.
Evaluator/condition and domain: agent compares narrative/data and decision predicates; >30-day untouched active page is a review cue, not falsity. GymJoy reversal requires early AND demonstrably strong, not launch alone.
Activation and timing: PM weekly request; reversal also checked during ingest.
Possible or observed result: findings or no triggered condition; pilot reports Q2/Q5 and unchanged decision.
Implemented force: none established; manual model-interpreted checklist.
Epistemic authority and scope: named inconsistency or unmet predicate licenses attention, not automatic contradiction resolution or causal truth.
Operational authority: behavior permitted, blocked, or changed: produce findings for the next disposition function.
Behavioral-authority path: consumer, channel, force, horizon: agent and PM, lint output/proposal, advisory, current review.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/wiki/open-questions.md`; see supplied lint and decision record.
Claim IDs or none: [EPI-CLM-defensible-claims](#epi-clm-defensible-claims).
Mismatch marker or none: freshness is not endorsement.
Gap/limit: no measured contradiction-detection recall; “demonstrably strong” requires judgment, not a fixed test implementation.

Route ID: [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-open-questions](#epi-obj-open-questions), [EPI-OBJ-decision-page](#epi-obj-decision-page)
Content/update relation: non-truth-apt policy/content update: queue questions, hold or supersede reliance
Transition or check target: findings to research queue/status proposal; answered question to filed answer; old decision to superseded record after authorized replacement.
Evaluator/condition and domain: agent routes findings; PM triages research and decides protected edits. Triggered reversal adds a question, never automatically reopens a decision; no universal answer-acceptance criterion for question closure is supplied.
Activation and timing: after finding or new answer evidence; direct approval before supersession.
Possible or observed result: Q4 answered with filed competitor evidence and Q6 follow-up; Q2 stays open; unchanged decision persists.
Implemented force: none established; prescribed containment of unresolved claims and protected edits.
Epistemic authority and scope: question closure asserts a bounded answer, not all related causal questions resolved. Old rationale remains inspectable after changed reliance.
Operational authority: behavior permitted, blocked, or changed: generate future interviews/plans; hold contradictory claims apart; preserve old decision and forward link.
Behavioral-authority path: consumer, channel, force, horizon: PM/later agent, queue tags and decision statuses, advisory research selection plus permissive write policy, subsequent tasks.
Evidence source ID and local anchor: SRC-1, `template/SCHEMA.md`, `pilot/wiki/open-questions.md`; see objects and supplied lint route.
Claim IDs or none: [EPI-CLM-defensible-claims](#epi-clm-defensible-claims).
Mismatch marker or none: questions are not resolutions.
Gap/limit: no automatic deletion/rollback or independent rejection evaluator; a future product experiment is not executed evidence here.

Route ID: [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade), [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: [RT-OBJ-schema](runtime.md#rt-obj-schema)
Content/update relation: non-truth-apt policy/content update: expand entity and upkeep instructions
Transition or check target: Stage-2 competitor addition after second intel ingest; separately, contributor schema changes after manual fresh-agent check.
Evaluator/condition and domain: agent recognizes pressure and proposes; direct PM approval for local schema; contributors inspect fresh-agent behavior for PR changes. No expected-answer oracle, quantitative threshold of improvement or retained check result supplied.
Activation and timing: need trigger then admission, before later instruction use.
Possible or observed result: competitor specification exists in pilot prompt and journal reports approval.
Implemented force: none established; policy-mediated adaptation.
Epistemic authority and scope: grants a filing/maintenance method, not truth to competitor implications. No ampliative belief acceptance follows from entity creation.
Operational authority: behavior permitted, blocked, or changed: later agent maintains competitor snapshot, capabilities, timeline and implications on intel ingest and lint.
Behavioral-authority path: consumer, channel, force, horizon: later external agent, reloaded schema, operating-policy force, subsequent sessions if loaded.
Evidence source ID and local anchor: SRC-1, `pilot/CLAUDE.md`, `CONTRIBUTING.md`; see supplied stage route.
Claim IDs or none: none.
Mismatch marker or none: adaptation is not demonstrated improvement.
Gap/limit: no post-change trace or causal comparison; external model parameters remain outside inspection.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control) | See declaring record | SRC-1, `template/SCHEMA.md`; doctrine/design | Ingest/query/lint prescribe citations, unsupported labels and immutable sources | None established; prescribed paths: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) | None; fictional journal is reported operation | No causal experiment; citation occurrence is not inferential checking | Traceability is explicitly requested and example evidence chains are inspectable | PRD price conclusion drops the queue's hypothesis qualification; not evidence every downstream inference is warranted |
| [EPI-CLM-defensible-claims](#epi-clm-defensible-claims) | See declaring record | SRC-1, `README.md`; doctrine/design | Read-only source layer, explicit belief history, contradiction queue, decision reversal policy, file-back | None established; design paths above plus [EPI-RTE-problem-confirmation](#epi-rte-problem-confirmation) and [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade) | None; persisted candidate pages do not prove who produced or accepted them | No timings, reliability comparison, field outcome or upstream authentication | Source-linked beliefs and inspectable rationale are afforded by the design; local problem criterion and PM authority are named | “Every claim” defensibility, ground truth, forever-access and minutes/week benefits exceed the evidence; archived source mistakes and ampliation can survive citations |

## Bounded conclusion

The design acquires curated testimony, reported measurements and intel as evidence while retaining raw files by policy. Their source warrant is **unknown**, not upgraded by immutability. Digest approval controls admission; it does not independently authenticate the upstream claims. See [EPI-OBJ-source-files](#epi-obj-source-files) and [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

It retains inspectable beliefs, counter-evidence, histories, reversal conditions and research questions, and requests later index-first consumption. There is a specific evidence-consuming problem-status criterion for product framing, separate from PM permission for protected edits. There is no supplied general criterion turning all cited ampliative statements into accepted knowledge. Acceptance-qualified linking can integrate a problem or revised belief; ordinary file-back merely retains an exploration. See [EPI-RTE-problem-confirmation](#epi-rte-problem-confirmation), [EPI-OBJ-assumptions](#epi-obj-assumptions) and [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback).

The arithmetic 34% + 29% = 63% is conditionally warranted within the imported readout's cancellation-reason categories. No independently warranted premises establish that those categories measure adaptivity-caused churn. The design explicitly preserves A2's correlation/causation distinction and proposes a holdout experiment. The PRD uses that limitation in its rollout, a counterexample to any claim that the system uniformly erases uncertainty. Conversely its categorical price statement exceeds A1's weakened status and Q2's still-open hypothesis. Citation preserves inspectability but can coexist with lost qualifiers. See [EPI-OBJ-problem-pages](#epi-obj-problem-pages), [EPI-OBJ-prd](#epi-obj-prd) and [EPI-OBJ-open-questions](#epi-obj-open-questions).

The check-to-consumer paths differ: evidence thresholds can change a problem label; PM replies permit protected writes; reversal checks create questions rather than autonomously reopening decisions; queue tags shape proposed discovery; retained statuses and rationale frame later deliverables. Schema progression separately adapts operating policy. These are natural-language authority paths, not executable invariants. Their activation, reliable observance and benefits are not established by fictional persisted examples. See [RT-BAP-schema-agent](runtime.md#rt-bap-schema-agent), [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) and [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade).

Localized theory content, requested consumption, content-directed A1 criticism and retained history are independently supported at the doctrine/fictional-report layer in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); this is not a system-wide epistemic verdict. Learning lacks improved-capacity evidence. Stage progression supplies a design-level self-representation/feedback path but does not establish reflective theory criticism; direct PM admission also prevents attributing every internal role to computation. Exercised self-improvement lacks later operation causally dependent on the instruction change and objective-responsive improvement evidence. No one of these limits cancels the separately supported source-linked state or policy-adaptation capacities.

## Shared records

### Operative objects

#### EPI-OBJ-source-files
Label: Curated source files

Source-native identity: `sources/` in the schema, instantiated by `pilot/sources/`. Natural-language testimony, digest/readout claims and intel; local Markdown substrate. Distinct from [RT-OBJ-schema](runtime.md#rt-obj-schema), which prescribes their treatment, and input to [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not another declaration of that route. SRC-1, `template/SCHEMA.md` and `pilot/sources/2026-06-25_analytics_cohort-retention-readout.md`, doctrine/design. Read-only is a policy; the analytics artifact is already an analyst readout, not raw measurement. Its actual external warrant is not established by a fictional source.

> sources/             ← immutable raw sources. READ-ONLY. Never edit, never delete.
> --- `template/SCHEMA.md`

> Findings (the readout, not the raw data):
> --- `pilot/sources/2026-06-25_analytics_cohort-retention-readout.md`

> High-volume streams (support tickets, reviews, competitor news): never ingest raw dumps; the PM
> provides a weekly digest file, or you draft one from an export and the PM approves it as a source.
> --- `template/SCHEMA.md`

#### EPI-OBJ-problem-pages
Label: Product problem pages

Source-native identity: `wiki/problems/`, instantiated by `pilot/wiki/problems/plans-dont-adapt.md` and `pilot/wiki/problems/price-value-gap.md`. Natural-language statements/evidence and frontmatter labels/counts on Markdown substrate. There is no shipped parser giving those labels autonomous symbolic force; the agent/PM interprets them. Distinct output objects of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not the governing [RT-OBJ-schema](runtime.md#rt-obj-schema). SRC-1, named paths, doctrine/design.

> - Cancellation survey: "not seeing results" 34% + "got repetitive / boring" 29% = 63% of stated
>   churn reasons map to this problem. (source: 2026-06-25_analytics_cohort-retention-readout.md)
> --- `pilot/wiki/problems/plans-dont-adapt.md`

The addition is entailed arithmetic conditional on the imported category figures; “map to this problem” is an interpretation, not checked causal attribution. The imported readout's 34%, 29% and 18% describe cancellation-survey reasons, not a randomized comparison. No executable text transformation is shipped to trace; this arithmetic distinction is inspection of declarative content, not target execution or a claim of implementation evidence.

> 5. Cancellation-survey top reasons (n=1,204, Jan–May): "not seeing results" 34%, "got repetitive
>    / boring" 29%, "too expensive" 18%, "switched to another app" 9%, other 10%.
> --- `pilot/sources/2026-06-25_analytics_cohort-retention-readout.md`

#### EPI-OBJ-assumptions
Label: Assumption register

Source-native identity: `pilot/wiki/assumptions.md`, prescribed by `template/SCHEMA.md`. Local Markdown natural-language beliefs A1–A4, evidence for/against and dated histories; statuses are interpreted labels, not executable truth values. Distinct retained belief content revised by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); that record supplies A1 history and doctrine-level theory assessment. SRC-1, named paths, doctrine/design. Content can be localized and revised without changing provider weights. A2's status explicitly withholds a causal license; A4 does not become validated from competitor shipping evidence.

> ## A2: Plan adaptivity drives retention
>
> - status: **validated (correlational only)**
> --- `pilot/wiki/assumptions.md`

> - evidence against: none yet; no causal experiment run (see Q1)
> --- `pilot/wiki/assumptions.md`

> - note: contradiction between survey wording and interview depth is Q2 — do not move to
>   `invalidated` until it's resolved.
> --- `pilot/wiki/assumptions.md`

#### EPI-OBJ-decision-page
Label: Q3 retention decision

Source-native identity: `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`. Natural-language options, factual premises, rationale and revision conditions plus interpreted status/date/decider frontmatter, on local Markdown. It is a distinct output/target of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint). SRC-1, named path, doctrine/design. A decision is operational commitment; only its premises/explanations are truth-apt. Reversal predicates constrain when a question is warranted, not permission to rewrite history.

> - GymJoy Coach ships early AND demonstrably strong, making fast-follow pointless and
>   differentiation-elsewhere (e.g. social) more attractive.
> --- `pilot/wiki/decisions/2026-06-30_q3-retention-focus.md`

The “early” conjunct alone is insufficient. The supplied lint record retains the no-delete/supersession passage; it supports recovery through preserved rationale, not an executable rollback.

#### EPI-OBJ-open-questions
Label: Open questions queue

Source-native identity: `pilot/wiki/open-questions.md`, prescribed by `template/SCHEMA.md`. Natural-language questions, candidate explanations and study plans, tagged by resolution path and status on local Markdown. Distinct output of [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint) and input to [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback); no counterpart object is declared in the supplied runtime. SRC-1, named paths, doctrine/design. An imperative interview plan is not a truth-apt assertion; Q2's proposed explanation is a conjecture. Q4's reported answer is bounded to competitor capability, while Q6 continues monitoring. Closure does not answer Q1 causally.

> - status: open — hypothesis to test in next churn interviews: "too expensive" is shorthand for
>   "not worth it anymore". Interview prompt: "You mentioned price — was there a moment the price
>   started feeling different?"
> --- `pilot/wiki/open-questions.md`

> Every contradiction, gap, or triggered reversal condition lands here. When the PM plans discovery,
> generate interview scripts / analysis plans FROM this queue.
> --- `template/SCHEMA.md`

#### EPI-OBJ-prd
Label: Adaptive Plans PRD

Source-native identity: `pilot/wiki/prd-adaptive-plans-v1.md`, status draft-v0.1. Natural-language evidence, generalizations, proposed features/measurement and annotated inferences; local Markdown substrate. Distinct retained output of [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback), which supplies the holdout-rollout passage and reported file-back account. SRC-1, named path, doctrine/design; preamble and journal are reported operation, not an inspectable execution trace. Audience is Dana/Omar; actual decision influence and later read-back of this filed artifact are unobserved.

> *Drafted by the wiki agent on PM request for Q3 kickoff; generated from wiki pages + raw
> sources. Every claim cited; inferences flagged. Filed back per the query workflow.*
> --- `pilot/wiki/prd-adaptive-plans-v1.md`

> **Non-goals:** ML personalization; social features (paused to Q4 per decision); pricing changes
> — price is the exit justification, not the cause (A1 weakening;
> [price-value-gap](problems/price-value-gap.md)), and GymJoy's €5.99 anchor expires Aug 1
> (source: 2026-07-02_intel_gymjoy-coach-launch.md).
> --- `pilot/wiki/prd-adaptive-plans-v1.md`

The parenthetical A1-weakening link supplies partial uncertainty context, but the categorical clause exceeds both the narrower interview evidence and Q2's explicitly open explanation. It is an ampliative claim; no acceptance criterion licenses the general exclusion of price as a cause. Other clauses preserve uncertainty: the rollout passage in the supplied query record explicitly limits A2 to correlation and proposes a holdout experiment. These counterexamples prevent a blanket judgment that all generated claims are either warranted or overconfident.

#### EPI-OBJ-index
Label: Wiki index

Source-native identity: `pilot/index.md`, prescribed by `template/SCHEMA.md`. Natural-language page summaries and Markdown links on a local file substrate. Distinct selector input to [RT-RTE-query-fileback](runtime.md#rt-rte-query-fileback), not the route itself. SRC-1, named paths, doctrine/design. Links provide addresses; their relevance and summaries are model-interpreted rather than deterministic retrieval predicates. The summary below already presents the price interpretation categorically, before the reader opens the problem page or Q2; the catalog is not merely neutral transport.

> - [Price–value gap](wiki/problems/price-value-gap.md) — emerging · medium · 3 mentions · exit justification, not cause (updated 2026-07-02)
> --- `pilot/index.md`

#### EPI-OBJ-overview
Label: Product overview

Source-native identity: `pilot/wiki/overview.md`. Local Markdown natural-language synthesis with an interpreted updated date. Distinct from the index, raw sources, individual problem pages and [RT-OBJ-schema](runtime.md#rt-obj-schema); maintained by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), available to later queries. SRC-1, named path, doctrine/design. It combines attributed reports with interpretations and retains A2's causal qualification. Its current picture is not an independent corroborating source for its own upstream evidence.

> load-bearing assumption — adaptivity drives
> retention (A2) — is validated only correlationally; making it causal is the top open question
> (Q1).
> --- `pilot/wiki/overview.md`

#### EPI-OBJ-gymjoy
Label: GymJoy competitor page

Source-native identity: `pilot/wiki/competitors/gymjoy.md`. Local Markdown natural-language snapshot, capability read, timeline and implications plus interpreted threat/updated labels. Distinct material input/output of [RT-RTE-stage-upgrade](runtime.md#rt-rte-stage-upgrade), not a duplicate of the schema specification it activates. SRC-1, named path and `pilot/CLAUDE.md`, doctrine/design. New intel triggers upkeep; lint checks staleness. No numeric confidence or automatic adjudicator supplies warrant. Competitor asking price is an imported report; inferring market willingness to pay from that asking price is ampliative because an offered price does not establish demand at that price. This page's implications therefore need separate treatment from its capability restatements. Its actual later consumption is unobserved.

> - Prices adaptivity at €9.99 → market-bears-our-price evidence for
>   [price-value-gap](../problems/price-value-gap.md); the €5.99 churn anchor expires 2026-08-01.
> --- `pilot/wiki/competitors/gymjoy.md`

### Routes

#### EPI-RTE-problem-confirmation
Label: Problem status assessment
Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Material subroute: agent assesses source evidence then changes an interpreted problem status. This separates a named evidential criterion and status disposition from the supplied ingest container's broader takeaways and write gates; it does not supersede that valid container. Endpoints: source evidence → threshold assessment → problem status → later index/PRD reliance. Owner: external agent; PM directs work and can correct it. Proposer/decision-maker for freely writable problem pages is the agent; the PM is not assigned per-status approval here. No answer oracle is supplied. Mode: open PM-driven ingest, not a benchmark. Trigger: new problem evidence; addressed status requires shipped measured effect. Guidance persists in the schema and source-linked problem page. Rejection/hold leaves emerging status or lacks addressed status; technical rollback is unspecified. The criterion is limited acceptance for product-problem framing, not an inference that adaptivity causes retention.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: assessment embedded in takeaways/page update; no required independent check artifact.
- Later read-back: interpreted problem status and evidence reach later index-first queries; the PRD presents the problem as confirmed, but a real agent's use is unobserved.
- Delegated visibility: uninspected — no host context-transfer implementation is frozen.
- Selection predicate: first evidence yields emerging; confirmation requires at least three independent sources or at least two source types; addressed requires measured effect of shipped change.
- Invalidation or expiry: inapplicable — no automatic expiry/demotion rule is specified for this subroute; lint may surface counter-evidence or staleness for review.
- Activation or effect: prescribed assignment of a problem reliance status; fictional log reports confirmation from survey/timing evidence, not authenticated computation.
- Evidence limits: SRC-1 doctrine/design and fictional reported operation only; independence, source truth and measurement validity have no executable or observed verification here.

> Status rules: `emerging` on first evidence; `confirmed` at ≥3 independent sources or ≥2 source
> types; `addressed` only when a shipped change shows measured effect (cite the measurement).
> --- `template/SCHEMA.md`

> - `plans-dont-adapt` → confirmed (survey 63% + timing match with months-2–4 cliff).
> --- `pilot/log.md`

### Claims

#### EPI-CLM-defensible-claims
Label: Defensible accumulated claims

Claimed operation: accumulated source-linked evidence makes every claim defensible, supplies immutable “ground truth,” ends decision amnesia and allows rapid deliverables/discovery at low weekly maintenance cost. SRC-1, `README.md`, doctrine/design, with a reported fresh-agent-testing assertion but no retained execution evidence. Distinct from [RT-CLM-evidence-control](runtime.md#rt-clm-evidence-control): that record owns the narrower citation/unsupported-label policy; this record owns broader warrant and payoff rhetoric. The latter cannot be inferred merely from the former. No causal timing/cost evidence, reliability study, perpetual availability guarantee or authentication of source truth is supplied.

> - **Every claim becomes defensible.** "Users need X" links to who said it, when, and in what
>   words — the difference between a PRD that survives a leadership review and one that doesn't.
> --- `README.md`

> - **Sources are read-only.** The agent reads them, never edits them. Your ground truth.
> --- `README.md`

> - **Decision amnesia ends.** "Why did we choose X over Y?" is answered in seconds, forever, with
>   the original options, evidence, and reversal conditions.
> --- `README.md`

> - **The cost is ~30 focused minutes a week.** The agent does the bookkeeping that kills every
>   Confluence wiki; you keep the judgment.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
