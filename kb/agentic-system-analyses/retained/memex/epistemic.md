---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Memex's source-to-wiki, maintenance and answer routes: provenance, model judgment and consequential reliance at the frozen revision."
run-id: AAS-2026-10-14-memex-42ecde52cc05-01
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
---

# Memex epistemic report

## Source-and-claim boundary

The question is whether Memex's persistent wiki machinery establishes warranted knowledge, rather than merely retaining and reusing model-written content. Scope, exclusions and evidence identity are see [boundary](boundary.md#boundary-and-evidence); sources are see [Source register](boundary.md#source-register). This member uses SRC-1 implementation and doctrine/design only. There are no supplied runs, populated wikis, expected-answer results or causal comparisons. These omissions prevent conclusions about actual extraction fidelity, grounding, accepted novel insight, improvement and successful maintenance. External Claude internals and optional MCP services remain uninspected; they prevent complete input-lineage and evaluator-reliability conclusions. No execution was performed.

The following is direct source inspection, except where explicitly marked supplied. All paths are in SRC-1 at the reviewed commit. Available operations were checked against CLI registration, the complete route table, all three runner dispatch branches and the exposed tool/MCP grant. No separate shipped epistemic hook or verifier branch appears in that dispatch. This is coverage of the inspected Memex surface, not enumeration of opaque Claude/MCP operations.

| Entry point or operation | Source path | Coverage or exclusion and conclusion prevented |
|---|---|---|
| CLI dispatch; exported client | `src/index.ts`; `src/cli/client.ts` | Direct: registered commands, uploads, job polling and file browsing; see [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [EPI-RTE-file-browse](#epi-rte-file-browse). |
| Source upload; create; destroy | `src/daemon/routes.ts`; `src/daemon/scaffold.ts` | Direct: archive admission, initial schema/index, removal/keepData; see [EPI-OBJ-raw](#epi-obj-raw), [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job). |
| Ingest and contradictions | `src/lib/prompts/ingest.ts`; `src/lib/prompts/wiki.ts` | Direct, complete: source extraction, updating, linking, schema reflection; see [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job). |
| Query and API history | `src/lib/prompts/query.ts`; `src/cli/commands/query.ts` | Direct, complete: search/grounding instructions, optional caller history, result print; see [RT-RTE-query-job](runtime.md#rt-rte-query-job), [EPI-RTE-result-display](#epi-rte-result-display). |
| Manual/automatic lint | `src/lib/prompts/lint.ts`; `src/daemon/queue.ts` | Direct, complete: eight diagnostic targets, confident edits/report-only partition and success counter; see [RT-RTE-lint-job](runtime.md#rt-rte-lint-job). |
| Registered tools, MCP, model and output envelope | `src/daemon/runner.ts`; `src/daemon/namespace.ts` | Direct, complete: shared process/tool path, current config, output extraction and path mismatch; see [RT-RTE-config-change](runtime.md#rt-rte-config-change), [EPI-RTE-result-display](#epi-rte-result-display). MCP implementation unavailable; prevents determining its truth-apt routes. |
| Config/auth/ownership/status/log endpoints | `src/daemon/routes.ts`; `src/cli/client.ts` | Direct route table and handlers; config changes affect later delegation, other gates establish access/status rather than proposition truth; see [RT-RTE-config-change](runtime.md#rt-rte-config-change), [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs). CLI config/auth details rely on supplied runtime. |
| Terminal persistence/restart | `src/daemon/db.ts`; `src/daemon/queue.ts` | Direct result/requeue methods and queue; startup wiring supplied by [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery). No semantic rollback; partial file effects may survive. |
| Product and prompt evaluation claims | `README.md`; `docs/prompts.md` | Direct, complete: see [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki), [EPI-CLM-grounded-query](#epi-clm-grounded-query), [EPI-CLM-audit-reasons](#epi-clm-audit-reasons). Proposed evaluation, not results. |
| External parametric state | `src/daemon/runner.ts` | Delegation inspected; internals excluded as in boundary; see [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model). No exact model/parameter-update evidence. |

Countercases qualify the strongest negatives. Source references and contradiction checks are explicitly requested, so this is not an architecture without provenance or criticism opportunities. Lint explicitly withholds some edits, so not every detected issue is intended to be auto-fixed. Conversely, these are model policies on pre-approved file tools, not daemon-enforced truth gates. The runtime's relative-path mismatch remains a material activation limit, not a defective supplied fact requiring supersession.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw](#epi-obj-raw) | Imported source statements, if truth-apt; arbitrary binary inputs may not be | Source archive | see record | Byte retention does not validate source truth. |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Extracted facts, summaries, relationships, contradiction flags, potential synthesis | Persistent knowledge | see record | No generated page available to classify particular content edges. |
| [EPI-OBJ-schema](#epi-obj-schema) | Filing policies; descriptive claims about vocabulary/patterns may be truth-apt | Institutional memory | see record | Normative policy differs from factual pattern description. |
| [EPI-OBJ-index](#epi-obj-index) | Descriptions of page contents and connections | Discovery/ranking map | see record | No deterministic semantic index verifier. |
| [EPI-OBJ-log](#epi-obj-log) | Descriptions of completed actions | Activity history | see record | Model-written history is not a tool trace or acceptance record. |
| [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs) | Embedded answers/reports may be truth-apt; status/control columns are operational | Durable job results | see record | Completion means process success, not epistemic acceptance. |
| [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts) | Primarily policies, plus illustrative statements | Curator guidance | see record | Static prompts are not acquired knowledge. |
| [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model) | Not determinable as individuated claims from accessible weights | Semantic producer/evaluator | see record | Distributed-parametric content/version and internal update behavior opaque. |

## Authority-route ledger

These compact entries split functions even when a supplied route implements several. Repeated route citations identify the same container, not duplicate declarations. Fields owned by those records remain there. All outcomes below are possible or requested, not observed operation.

Route ID: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown.
Transition or check target: caller-selected source bytes enter the raw archive.
Evaluator/condition and domain: caller selects files; daemon checks request shape and ownership, not factual content.
Activation and timing: upload before job submission; see route for return/read-back.
Possible or observed result: stored source filename and bytes.
Implemented force: direct host-side write.
Epistemic authority and scope: acquired source content only; no endorsement of its claims.
Operational authority: source is made available for later model extraction.
Behavioral-authority path: Claude, requested raw-file reads in later ingest tasks, advisory evidence input, surviving-file horizon.
Evidence source ID and local anchor: SRC-1, `src/cli/client.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`; see [EPI-OBJ-raw](#epi-obj-raw).
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: immutability is path-conditional, not unconditional provenance authentication.
Gap/limit: read-only namespace alias does not protect every host alias; actual reads and source credibility unobserved.

Route ID: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index)
Content/update relation: truth-apt transformation: indeterminate. Requested extraction and summary could preserve meaning; synthesis could derive or conjecture. No concrete produced proposition establishes entailment or non-entailment.
Transition or check target: raw statements and existing pages become revised prose, relationships and index summaries.
Evaluator/condition and domain: Claude interprets sources and selects pages; no expected-answer oracle.
Activation and timing: during ingest after requested source/schema/index reads.
Possible or observed result: direct page/index edits and an operations report.
Implemented force: pre-approved file tools; model-directed semantic edits, not a staged patch gate.
Epistemic authority and scope: candidate extracted/synthesized claims; no independently established source truth or accepted novel claim.
Operational authority: written content becomes available to future queries and ingests without separate semantic approval.
Behavioral-authority path: later Claude jobs, requested file search/read, advisory factual context, across sessions while files survive.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/ingest.ts`, `src/lib/prompts/wiki.ts`; see supplied route and page/index records.
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: retention/reuse is not evidence of compounding correctness.
Gap/limit: no output instance; source references are requested at page level, not a checked per-claim derivation graph.

Route ID: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages)
Content/update relation: no content change.
Transition or check target: new source statements versus existing pages about the same subjects.
Evaluator/condition and domain: Claude performs requested contradiction comparison; domain is textual consistency, not external truth verification.
Activation and timing: source integration.
Possible or observed result: perceived contradiction, confirmation or extension.
Implemented force: model judgment can feed the next disposition; no separate check artifact required.
Epistemic authority and scope: at most proposed inconsistency within compared texts; consistency does not establish truth.
Operational authority: judgment informs which existing pages are revised or flagged.
Behavioral-authority path: same Claude invocation, prompt-interpreted comparison, advisory to its edit selection, current ingest.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/ingest.ts`, `src/lib/prompts/wiki.ts`; see page record.
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: none.
Gap/limit: unseen model reasoning and no run make realized checking unobserved.

Route ID: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages)
Content/update relation: truth-apt transformation: indeterminate; resolution may change meaning, flagging need not resolve truth.
Transition or check target: conflicting new/existing claims.
Evaluator/condition and domain: Claude decides to resolve or flag under the prompt; caller supplies sources, not per-claim approval.
Activation and timing: during integration before returning operations.
Possible or observed result: existing page updated with resolution or conflict notice.
Implemented force: direct file edits; no daemon semantic veto or content rollback.
Epistemic authority and scope: disposition opportunity, not established evidence-consuming acceptance of a claim against a named truth criterion/use/scope.
Operational authority: replacement text may be relied on at the next query regardless of warrant.
Behavioral-authority path: later reader/model, retained page text, advisory factual input, until overwritten/deleted.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/ingest.ts`; see [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job).
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: operational disposition must not be promoted to epistemic acceptance.
Gap/limit: no explicit criterion for choosing which conflicting source is true; no observed accepted claim.

Route ID: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index), [EPI-OBJ-schema](#epi-obj-schema), [EPI-OBJ-log](#epi-obj-log)
Content/update relation: no content change.
Transition or check target: file effects survive the delegated process.
Evaluator/condition and domain: filesystem retention, not a proposition evaluator.
Activation and timing: writes during jobs, independent of terminal success.
Possible or observed result: later invocations can access surviving files.
Implemented force: durable filesystem effects; no accept-before-persist boundary.
Epistemic authority and scope: retention alone licenses no factual reliance.
Operational authority: material is eligible for later search, reading and filing guidance.
Behavioral-authority path: later Claude jobs, filesystem tools under task instructions, advisory or policy guidance according to object, cross-session horizon.
Evidence source ID and local anchor: SRC-1, `src/daemon/runner.ts`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/query.ts`; see supplied routes.
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: no lifecycle integration after demonstrated acceptance established by this retention path.
Gap/limit: named page linking/indexing is not, by itself, acceptance or post-acceptance lifecycle integration; replay can reuse partial edits.

Route ID: [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index), [EPI-OBJ-schema](#epi-obj-schema)
Content/update relation: truth-apt transformation: indeterminate; reports make new diagnostic claims whose fidelity is unobserved.
Transition or check target: contradictions/staleness in page claims; inbound links, duplicates, missing references; index-content and schema-pattern agreement.
Evaluator/condition and domain: Claude judges markdown and conventions. Date/age flags possible staleness, not present falsity; textual comparison is not independent external corroboration.
Activation and timing: manual lint or success-counter scheduling; see supplied route.
Possible or observed result: diagnostic report, confidence judgments, proposed structural fixes.
Implemented force: findings feed model edit selection and are returned to clients.
Epistemic authority and scope: candidate diagnostics within the inspected wiki; no verified source truth, coverage or contradiction-resolution warrant.
Operational authority: confidence partitions intended immediate edits from report-only issues.
Behavioral-authority path: Claude in current job through lint prompt, advisory diagnosis; caller through stored markdown report, advisory review, current job and later retrieval.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/lint.ts`, `src/daemon/queue.ts`; see supplied route.
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: none.
Gap/limit: eight criteria do not constitute eight independently verified evaluators; no external oracle or measured diagnostic accuracy.

Route ID: [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index), [EPI-OBJ-schema](#epi-obj-schema)
Content/update relation: truth-apt transformation: indeterminate; relationship/index/schema edits may change descriptive assertions.
Transition or check target: model-diagnosed issues.
Evaluator/condition and domain: Claude confidence for enumerated structural fixes; contradictions/merges/stale facts intended for human judgment, but no human approval endpoint.
Activation and timing: same lint after diagnostic comparison.
Possible or observed result: direct confident fixes; remaining issues reported without intended edits.
Implemented force: natural-language edit/withhold policy over equally available Write/Edit tools, not an enforcing issue-type guard.
Epistemic authority and scope: operational confidence selection, not observed acceptance of factual claims.
Operational authority: model may change links/index/schema immediately; human-review flags have advisory force only.
Behavioral-authority path: Claude file tools, policy-mediated edit selection, permissive, current job; later models read resulting files across sessions.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/lint.ts`, `src/daemon/runner.ts`; see supplied route.
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: report-only is requested, not enforced.
Gap/limit: no persistent pending-review/withdrawal state or rollback based on semantic rejection.

Route ID: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-schema](#epi-obj-schema)
Content/update relation: non-truth-apt policy/content update: filing heuristics and conventions; factual pattern descriptions remain indeterminate truth-apt transformations.
Transition or check target: schema versus encountered filing behavior and page patterns.
Evaluator/condition and domain: Claude compares behavior/patterns to conventions and decides revisions under static prompts.
Activation and timing: ingest reflection; lint schema drift; future ingest explicitly requests schema read.
Possible or observed result: retained revised filing guidance.
Implemented force: model can edit schema directly; later behavior change requested, not observed.
Epistemic authority and scope: policies guide filing; adapting to observed practice does not validate factual theories or improve decisions by itself.
Operational authority: categories/templates/ignore rules can influence later page selection and layout.
Behavioral-authority path: future Claude, `_schema.md` requested read, advisory natural-language policy, cross-session survival.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/ingest.ts`, `src/lib/prompts/wiki.ts`, `src/lib/prompts/lint.ts`; see supplied theory accounts and schema record.
Claim IDs or none: [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki).
Mismatch marker or none: evolution is not demonstrated improvement.
Gap/limit: realized consumption, content-directed criticism, iteration and learning remain separately unobserved; see bounded conclusion.

Route ID: [RT-RTE-query-job](runtime.md#rt-rte-query-job)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-index](#epi-obj-index)
Content/update relation: truth-apt transformation: indeterminate; grounded synthesis may reshape, derive or conjecture, but no concrete answer settles which.
Transition or check target: caller question plus relevant retained page content.
Evaluator/condition and domain: Claude selects via requested index/grep/glob/reads, then synthesizes. Requested wiki-only facts, citations and thin-coverage/conflict warnings are not a separate evaluator.
Activation and timing: query job; optional API history appended verbatim, not prior-job automatic recall.
Possible or observed result: answer or explicit no-information response; optional suggestion to save insight.
Implemented force: output returned on process completion; no evidence/citation gate.
Epistemic authority and scope: claimed wiki grounding, not independently warranted world truth or accepted ampliative knowledge.
Operational authority: caller receives prose for potential reliance; queries also retain file-write capabilities.
Behavioral-authority path: user/API client through printed/stored answer, advisory, current answer and later result retrieval; pages remain accessible to subsequent jobs.
Evidence source ID and local anchor: SRC-1, `src/lib/prompts/query.ts`, `src/cli/commands/query.ts`; see supplied route.
Claim IDs or none: [EPI-CLM-grounded-query](#epi-clm-grounded-query).
Mismatch marker or none: answer saving is suggested, not a separate implemented acceptance/save workflow.
Gap/limit: external model compliance and accessible web/MCP inputs prevent guaranteeing wiki-only content.

Route ID: [EPI-RTE-result-display](#epi-rte-result-display)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs)
Content/update relation: truth-apt transformation: non-ampliative reshaping for the concrete plain-answer case in the record; general envelope metadata is omitted.
Transition or check target: Claude stdout envelope to caller-visible output.
Evaluator/condition and domain: JSON parsing and exit code; syntax/process state, not truth.
Activation and timing: child close, terminal result persistence, CLI poll.
Possible or observed result: extracted answer printed; malformed JSON can still be successful raw output.
Implemented force: fixed extraction and completion rules.
Epistemic authority and scope: no new warrant; process completion is not answer validation.
Operational authority: completed output is presented; successful ingests advance automatic-lint counter.
Behavioral-authority path: queue and CLI, success flag/result field, enforcing status/printing selection, current job; later stored result retrievable.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-audit-reasons](#epi-clm-audit-reasons).
Mismatch marker or none: envelope metadata and operation reasons are not parsed into semantic audit records.
Gap/limit: unknown external envelope fields cannot be assumed to reach the user.

Route ID: [EPI-RTE-file-browse](#epi-rte-file-browse)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: no content change.
Transition or check target: client-selected file path to returned UTF-8 content.
Evaluator/condition and domain: ownership and path/existence checks, not content truth.
Activation and timing: exported client's list/read endpoints, outside model jobs.
Possible or observed result: directory entries or file content returned without semantic checking.
Implemented force: daemon host-side read.
Epistemic authority and scope: exposes stored text, not validated knowledge.
Operational authority: clients may inspect retained content independently of model selection.
Behavioral-authority path: API caller, response content, advisory, request/later client-controlled use.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: subsequent client interpretation outside this implementation; arbitrary binary raw files need not be intelligible UTF-8.

Route ID: [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages)
Content/update relation: no content change at requeue; replay may generate further indeterminate edits.
Transition or check target: running job status after restart, not validity of prior edits.
Evaluator/condition and domain: fixed SQL running-status predicate.
Activation and timing: daemon restart before draining pending jobs.
Possible or observed result: replay with same payload, current files/config and increased retry count.
Implemented force: pending eligibility restored; no semantic rejection or file rollback.
Epistemic authority and scope: recovery confers no endorsement or freshness of retained claims.
Operational authority: surviving partial content may influence replay and later jobs.
Behavioral-authority path: scheduler consumes pending state, enforcing continuation, next drain; Claude sees surviving files in later invocation.
Evidence source ID and local anchor: SRC-1, `src/daemon/db.ts`; see supplied route.
Claim IDs or none: none.
Mismatch marker or none: no exactly-once content warrant.
Gap/limit: no supplied crash trace or deduplicated edit transaction.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-compounding-wiki](#epi-clm-compounding-wiki) | see record | see record | Source integration, maintenance and schema evolution requested | [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job) | None supplied | No intervention/comparison; no output fidelity evidence | Persistent update/reuse opportunity implemented | Richer/more correct on every source not established; path mismatch limits literal operation. |
| [EPI-CLM-grounded-query](#epi-clm-grounded-query) | see record | see record | Wiki-only facts, file citations, uncertainty notices, possible save | [RT-RTE-query-job](runtime.md#rt-rte-query-job), [EPI-RTE-result-display](#epi-rte-result-display) | None supplied | No expected answers or independent citation checker | Requested wiki-backed synthesis returned to caller | Actual grounding and automatic filing of good answers unestablished. |
| [EPI-CLM-audit-reasons](#epi-clm-audit-reasons) | see record | see record | Insightful operation reasons requested | [EPI-RTE-result-display](#epi-rte-result-display) | None supplied | Queue records coarse action/job/timing, not parsed reasons | Reasons can survive in job result, not semantic audit entries | Documentation overstates audit narrative wiring. |

## Bounded conclusion

Memex implements persistent source admission, direct model-driven wiki edits, later model-directed reads, returned answers and maintenance opportunities. It acquires sources without checking their truth. Raw byte retention and requested source links offer provenance support, but no run demonstrates preservation of source warrant through extraction, compression, contradiction resolution and later synthesis. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).

The inspected deterministic output transformation preserves the concrete answer proposition while discarding the surrounding envelope; it establishes no new proposition or warrant. Model-generated content edges remain indeterminate without concrete inputs/outputs. No warranted-premise derivation, non-entailed conjecture, evidence-consuming acceptance of produced ampliative content, or post-acceptance lifecycle integration is established. This does not deny such model behavior could occur. Persisting a page, linking it, returning it or exiting successfully does not establish those stronger phases. See [EPI-RTE-result-display](#epi-rte-result-display), [RT-RTE-query-job](runtime.md#rt-rte-query-job).

The material evaluation criteria are distinct. Ingest asks for source/existing-page conflict comparison and resolve-or-flag disposition. Lint asks for internal consistency, possible staleness, relationship/index/schema agreement and model confidence. Confident structural changes are intended to be applied immediately; semantic judgment calls are intended to be report-only. Their scope is wiki text and filing organization. Their force is prompt-mediated model selection, followed by direct file effects or an advisory report, not independently verified truth or an enforcing human review gate. No named truth criterion and intended-use acceptance decision is evidenced for novel facts. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job).

Schema evolution is a separate policy-adaptation opportunity. Generated filing rules are requested to persist and be read by later ingests; facts about recurring patterns can coexist with normative instructions. The supplied theory account separately leaves realized localization, consumption, content-directed criticism and next-round dependence unobserved. Addressability of generated conventions cannot be assessed without them. Cross-session persistence is afforded; improved future capacity is not demonstrated. Self-comparison is requested, but the two realized causal directions needed for reflection are unobserved. Model-owned edit selection does not establish every operation of autonomous theory building. For the bounded wiki-agent filing organization, schema updates offer a possible self-change pathway, but exercised self-improvement cannot be attributed: evidence-responsive determination, installation of a particular change and later causal dependence are not supplied. No improvement outcome or component attribution follows. These are independent limits, not one system-wide negative. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [EPI-OBJ-schema](#epi-obj-schema).

Configuration can alter future model/tool/instruction context without being a truth-apt claim acceptance route. Parameter changes inside Claude remain uninspected; Memex exposes model selection, not inspected weight training. Static prompt revision has proposed sequential evaluation criteria in documentation, not recorded results or a release gate. Recovery requeues work without withdrawing potentially incorrect partial content. Thus retained-use capacity, requested criticism, policy adaptation, opaque model capacity and unestablished benefit must remain separate conclusions. See [RT-RTE-config-change](runtime.md#rt-rte-config-change), [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model), [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery); SRC-1, `docs/prompts.md`.

## Shared records

### Operative objects

#### EPI-OBJ-raw
Label: Raw source archive

Source-native identity: `wiki/raw/` files. Representational form: input-dependent natural-language text, symbolic data or opaque binary/media. Storage substrate: host files. Distinct from [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs), whose payload contains filenames rather than archive bytes; no supplied object counterpart. SRC-1, `src/daemon/scaffold.ts`, `src/daemon/routes.ts`, `src/cli/client.ts`: client bytes are base64-encoded, decoded by daemon and written with a timestamp/sanitized basename. This imports content, not source credibility. Namespace raw-path remount is read-only but original host aliases are not removed; see [RT-CLM-workspace-isolation](runtime.md#rt-clm-workspace-isolation).

> const buffer = Buffer.from(content, 'base64');
> const stored = this.scaffold.writeRawFile(wikiId, filename, buffer);
> --- `src/daemon/routes.ts`

> writeFileSync(join(rawDir, stored), content);
> --- `src/daemon/scaffold.ts`

#### EPI-OBJ-wiki-pages
Label: Wiki pages

Source-native identity: generated entity/topic markdown in `wiki/`, excluding special schema/index/log and raw files. Representational form: natural-language claims, summaries and labeled relationships interpreted by models/readers. Storage substrate: host files. Distinct from [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts), which prescribe their production; no supplied retained-page object counterpart. SRC-1, `src/lib/prompts/wiki.ts`, `src/lib/prompts/ingest.ts`: source links and contradiction handling are requested, not verified per-claim provenance or truth. Direct file admission precedes any separate acceptance decision.

> Each wiki page should reference its raw sources: \`*Source: [raw/filename.md](raw/filename.md)*\`
> --- `src/lib/prompts/wiki.ts`

> - If a source contradicts existing wiki content, UPDATE the existing page — resolve or flag the contradiction
> --- `src/lib/prompts/ingest.ts`

#### EPI-OBJ-schema
Label: Schema conventions

Source-native identity: `_schema.md`. Representational form: natural-language filing policies and potentially descriptive domain/pattern assertions. Storage substrate: scaffolded `wiki/_schema.md`, then model-editable files. Distinct from static [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts); schema is use-changeable retained guidance, not the shipped instruction to change it. Closest route is [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), not a duplicate object. SRC-1, `src/daemon/scaffold.ts`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/wiki.ts`: later requested reads can influence filing; no generated schema or actual activation evidence. Runtime's mount-root mismatch qualifies literal access.

> 2. Read _schema.md for current conventions (create it if it doesn't exist — this is a new knowledge base).
> --- `src/lib/prompts/ingest.ts`

> - Has my filing behavior drifted from what the schema says? Update the schema to match reality.
> --- `src/lib/prompts/ingest.ts`

#### EPI-OBJ-index
Label: Wiki index

Source-native identity: `_index.md`. Representational form: natural-language semantic page summaries and count assertions with path pointers; model-interpreted selection material, not a fixed relevance algorithm. Storage substrate: scaffolded `wiki/_index.md` and later edits. Distinct from [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts); no supplied retained-index counterpart. SRC-1, `src/lib/prompts/wiki.ts`, `src/lib/prompts/query.ts`: index supplies the initial discovery map but does not enforce selection, completeness or correct counts.

> ALWAYS keep _index.md current. Every wiki page gets a one-line summary: what it contains, how many connections, what matters most. Organize by category. A reader should understand the shape of the entire knowledge base by reading only the index.
> --- `src/lib/prompts/wiki.ts`

#### EPI-OBJ-log
Label: Activity log

Source-native identity: `_log.md`. Representational form: model-written natural-language event descriptions, not independently authenticated tool events. Storage substrate: scaffolded `wiki/_log.md` and later appends. Distinct from audit and job rows in [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs); no supplied object counterpart. SRC-1, `src/lib/prompts/wiki.ts`: every operation requests append, but no later task explicitly reads log to evaluate truth or accept claims. Mere availability does not establish trace-fed learning.

> After completing any operation, append an entry to _log.md:
> --- `src/lib/prompts/wiki.ts`

### Routes

#### EPI-RTE-result-display
Label: Result extraction and display

Part of: [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)

This is the terminal-result subroute, not restart replay. Endpoints/progression: Claude stdout → runner JSON extraction → `JobResult.output` → SQLite JSON result → query CLI parse/print. Owner: fixed runner/database/CLI code. Context/state/effects: direct wiki effects already occurred; code packages returned text, not verified edits. SRC-1, `src/daemon/runner.ts`, `src/daemon/db.ts`, `src/cli/commands/query.ts`. The supplied parent includes terminal result recording; this part owns the transformation and final consumer, not the whole job loop.

Concrete implementation deduction, not execution: for stdout `{"result":"The price is 10."}` and exit code zero, outer JSON parses; inner parse of `The price is 10.` fails; `text.trim()` becomes output `The price is 10.`. Runner sets success true, queue calls completion, database serializes the result, CLI parses that object and prints its `output`. This is non-ampliative reshaping of this proposition. No truth check is performed. For plain non-JSON stdout the outer parse fails and raw stdout survives, still successful at exit zero. Other envelope metadata is not carried into `JobResult`; it cannot be assumed available to the caller.

> const envelope = JSON.parse(rawOut);
> const text = envelope.result ?? '';
> --- `src/daemon/runner.ts`

> output = text.trim() || rawOut;
> --- `src/daemon/runner.ts`

> console.log(parsed?.output ?? result.result ?? '(no output)');
> --- `src/cli/commands/query.ts`

> this.db.completeJob(job.id, result);
> this.db.logAudit(wikiId, `job.${job.type}.completed`, `job #${job.id} (${result.duration_ms}ms)`);
> --- `src/daemon/queue.ts`

- Immediate return: stored/printed extracted text on completion; failed execution returns an error path.
- Later read-back: retained result available via job endpoints; not automatically injected into later model queries.
- Delegated visibility: inapplicable — this subroute consumes model stdout, not a new model invocation.
- Selection predicate: envelope.result when outer JSON parses, normalized inner JSON or trimmed text; otherwise raw stdout; CLI selects output.
- Invalidation or expiry: wiki/job deletion or external database maintenance; no truth-based expiry.
- Activation or effect: fixed transformation, completion/printing and success-counter effects wired; actual operation unobserved.
- Evidence limits: external stdout contract and real outputs absent; concrete example is code deduction only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Conditional admission account: process exit proposes no epistemic judgment; fixed code decides operational completion and has no semantic veto. Caller may disregard the output but no per-answer acceptance API is present in this path. Operating mode is ordinary job result processing, not an experiment; answer oracle none. Rejection on nonzero exit does not roll back file writes. Guidance is static runner logic and the task's requested output format; the retained artifact is the result envelope.

#### EPI-RTE-file-browse
Label: Direct file browsing

Distinct identity: [RT-RTE-query-job](runtime.md#rt-rte-query-job) is a model job with search/synthesis; these exported API operations read host files directly without queue/model involvement. No supplied route counterpart after comparison. Endpoints/progression: client `listFiles`/`readFile` → ownership-checked route → scaffold directory listing or UTF-8 read → response. Owner: caller chooses path/prefix; daemon performs read. Effects: no content update or acceptance. SRC-1, `src/cli/client.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`.

> const content = this.scaffold.readWikiFile(wikiId, filePath);
> return { status: 200, body: { ok: true, data: { path: filePath, content } } };
> --- `src/daemon/routes.ts`

- Immediate return: path/content or directory entries; errors on missing/invalid paths.
- Later read-back: client reads surviving use-accumulated wiki files on demand; no automatic model injection by this route.
- Delegated visibility: inapplicable — no delegated model invocation.
- Selection predicate: caller-selected file path or directory prefix, not semantic relevance.
- Invalidation or expiry: file overwrite/removal or wiki destruction changes later reads.
- Activation or effect: host read/response wired; subsequent caller reliance uninspected.
- Evidence limits: no API execution supplied; UTF-8 decoding is not semantic validation and host path checks are not a full security proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### EPI-CLM-compounding-wiki
Label: Compounding maintained knowledge

Claimed operation: each source enriches persistent synthesis, with cross-references and contradictions maintained. SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-workspace-isolation](runtime.md#rt-clm-workspace-isolation), which concerns confinement, not knowledge quality. Supplied ingest/lint routes supply implementation opportunity, not output correctness or monotonic improvement.

> The cross-references are already there. The contradictions have been flagged. The synthesis reflects everything you've ingested. Every source makes the whole richer.
> --- `README.md`

#### EPI-CLM-grounded-query
Label: Grounded answers and filing

Claimed operation: questions yield wiki-grounded synthesis and good answers are filed as pages. SRC-1, `README.md`, doctrine/design. No supplied claim counterpart; closest [RT-RTE-query-job](runtime.md#rt-rte-query-job) correctly limits saving to a suggestion rather than a dedicated workflow.

> - **Query** — ask a question, the LLM searches the wiki and synthesizes an answer grounded in your accumulated knowledge. Good answers get filed back as new pages.
> --- `README.md`

> 6. If your answer synthesizes multiple pages into new insight, mention it could be saved to the wiki as a new page.
> --- `src/lib/prompts/query.ts`

#### EPI-CLM-audit-reasons
Label: Reasons become audit narrative

Claimed operation: ingest operation reasons flow into the audit log and explain evolution. SRC-1, `docs/prompts.md`, doctrine/design. No supplied claim counterpart; closest [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs) distinguishes coarse audit from returned output. Inspected queue completion writes only job/timing details, not operation reasons. Reasons can survive in the job output; the model-maintained activity log is a different object, not this SQLite audit wiring.

> These reasons flow into the audit log and become a narrative of how the knowledge base evolved.
> --- `docs/prompts.md`
