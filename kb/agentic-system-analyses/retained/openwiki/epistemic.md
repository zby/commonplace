---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenWiki epistemic routes: source-version checks, sparse Claim decisions, verification metadata, downstream context and separate benchmark judgment."
run-id: AAS-2026-10-14-openwiki-8f502f680f75-01
reviewed-boundary: "7c469e59584bfac3f97f5c32a67604de46805999"
---

# OpenWiki epistemic report

## Source-and-claim boundary

The question is what licenses reliance on OpenWiki's generated knowledge, and how that license reaches later consumers. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and layers are see the [Source register](boundary.md#source-register). All additional direct reads below are SRC-1 implementation or doctrine/design at the frozen pin. No target execution or causal experiment was supplied or performed.

Repository generation combines semantic source research by a model/host with deterministic evidence resolution, reconciliation and persistence. Personal ingestion, translation and later retrieval have different checks. The public Grounded Claims and verification contract is [EPI-CLM-grounded-claims](#epi-clm-grounded-claims). Its own explicit exclusion of connector-derived facts prevents treating every personal-wiki statement as a Grounded Claim. Durability is see [RT-CLM-page-durability](runtime.md#rt-clm-page-durability), not an answer oracle.

| Entry point or operation | Source path and inspection basis | Covering records or remaining limit |
| --- | --- | --- |
| CLI integration/MCP, ingest, print/TUI, cron, visualize, workspace, link, auth and ngrok dispatch | Direct: SRC-1 `src/cli/cli.tsx` | Dispatch checked against runtime; support-command semantics not all inspected. No system-complete negative about those operations. |
| Native repository init/update and host lifecycle | Supplied runtime plus direct admission reads: `src/agent/index.ts`, `src/generation/repository-run.ts`, `src/integrations/core/protocol.ts`, `src/generation/page-jobs.ts` | [RT-RTE-native-generation](runtime.md#rt-rte-native-generation), [RT-RTE-host-generation](runtime.md#rt-rte-host-generation), [EPI-RTE-claim-decisions](#epi-rte-claim-decisions) |
| Preflight, final evidence recheck, persistence and verification withdrawal | Direct: `src/claims/brains/code/preflight.ts`, `src/claims/brains/code/session.ts`, `src/claims/brains/code/runtime.ts`, `src/okf/claims-verification.ts` | [EPI-RTE-evidence-preflight](#epi-rte-evidence-preflight), [EPI-RTE-claims-persistence](#epi-rte-claims-persistence), [EPI-RTE-verification-projection](#epi-rte-verification-projection) |
| Generic evidence mutations and resolution | Direct portions: `src/claims/core/mutations.ts`, `src/claims/evidence/repository/resolver.ts` | Structural/resolution checks inspected; complete line-relocation algorithm not assessed. No universal relocation-fidelity conclusion. |
| Claim evidence to page provenance | Direct: `src/okf/claim-sources.ts` | [EPI-RTE-source-projection](#epi-rte-source-projection) |
| Personal updates, connector discovery, raw imports, chat | Supplied runtime; direct graph middleware/tool registration: `src/agent/index.ts` | [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion), [RT-RTE-mcp-connector](runtime.md#rt-rte-mcp-connector). Connector-specific transformations and complete chat prompt/consumer path unassessed; prevents a complete truth-check inventory for personal mode. |
| Direct translation hook | Supplied runtime: `src/agent/translation-middleware.ts`; direct graph wiring in `src/agent/index.ts` | [RT-RTE-page-translation](runtime.md#rt-rte-page-translation); semantic fidelity unobserved. |
| Registered retrieval tools and MCP delivery | Direct: `src/integrations/core/protocol.ts`, `src/integrations/mcp/server.ts`, portions of `src/retrieval/wiki.ts`; supplied runtime | [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval), [RT-BAP-retrieved-sections](runtime.md#rt-bap-retrieved-sections); deprecated-page search exclusion inspected. Full explicit-read deprecation behavior not assessed. |
| LEDGER precision judgment and checkpoint consumer | Direct portions: `evals/ledger/evaluator/precision.ts`, `evals/ledger/evaluator/prompts.ts`, `evals/ledger/run/evaluate-checkpoint.ts`, `evals/ledger/run/runner.ts` | [EPI-RTE-ledger-judgment](#epi-rte-ledger-judgment), [EPI-RTE-ledger-reporting](#epi-rte-ledger-reporting). Extraction, evidence retrieval and forgetting implementations not fully assessed; prevents complete evaluator accuracy/coverage conclusions. |
| Scheduled publication and managed host instructions | Supplied runtime | [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance); no actual merge or host-loading evidence. |
| DeepSWE caller, visualizer, other scheduling platforms, bundled skills, shipped generated wiki and tests | Boundary inventory and supplied runtime only | Relevant included material remains unassessed here. No complete-system absence of semantic evaluation, human approval, adaptation or learning is asserted. Generated artifacts without provenance traces establish availability, not observed generation or acceptance. |

Missing provider internals prevent conclusions about latent reasoning, weight updates and immutable model identity; see [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model). Missing execution traces prevent conclusions about exercised semantic rechecking, host reliance and actual withdrawal effects. Missing experiment results and independently varied treatments prevent empirical benefit or causal component attribution. Available but uninspected files are not access gaps.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-page-claims](#epi-obj-page-claims) | Repository propositions plus source resource/version identities | Material source-backed facts | see record | A cited resource can exist without entailing its statement. |
| [EPI-OBJ-wiki-markdown](#epi-obj-wiki-markdown) | Generated repository or personal prose, diagrams and relationships | Retained knowledge/context | see record | Page-to-Claim semantic agreement is requested, not proved by durability. |
| [EPI-OBJ-verification-events](#epi-obj-verification-events) | Producer/time events; truth-apt about recorded verification, not a proof of every page proposition | Page-level trust metadata | see record | Non-OpenWiki events are preserved, not independently checked. |
| [EPI-OBJ-page-sources](#epi-obj-page-sources) | Whole-file source resource identities | Page provenance | see record | Range and proposition joins are not retained in this projection. |
| [EPI-OBJ-ledger-verdicts](#epi-obj-ledger-verdicts) | Extracted assertions, model judgments, rationale/evidence references and metrics | Benchmark assessment | see record | Evaluator evidence is bounded; result files and actual runs not supplied. |
| [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance) | Task purposes/instructions, not necessarily factual assertions | Semantic generation guidance | see record | Delivery does not establish source-correct decisions. |
| [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state) | Lifecycle facts/statuses, not substantive repository theory | Queue authority | see record | Completed status licenses continuation, not semantic truth. |
| [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) | Internal truth-apt content not determinable | Semantic research/generation | see record | Distributed-parametric state and external-host parameters opaque. |

## Authority-route ledger

Rows use compact records. Identity, mechanism, producer and generic route fields are see the cited canonical record; the fields below assess the particular consequential function. All implementation is source-level, with operation unobserved.

Route ID: [RT-RTE-native-generation](runtime.md#rt-rte-native-generation), [RT-RTE-host-generation](runtime.md#rt-rte-host-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-markdown](#epi-obj-wiki-markdown), [EPI-OBJ-page-claims](#epi-obj-page-claims)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Repository evidence to page prose and material propositions.
Evaluator/condition and domain: Model/host research under source-backed proposition and falsifiability guidance; semantic entailment and non-entailment of actual generated propositions unavailable.
Activation and timing: Assigned page work before submission.
Possible or observed result: Candidate assertions, diagrams and sparse decisions; no observed candidate lineage.
Implemented force: Candidate generation and proposal.
Epistemic authority and scope: Repository evidence is acquired; a model's reshaping or synthesis does not by itself preserve its warrant. Semantic preservation, entailed derivation and ampliative conjecture remain possible classifications requiring actual input/output evidence.
Operational authority: Worker can write assigned page and propose Claims; shared core can reject submission.
Behavioral-authority path: Model/host, page assignment and source tools, advisory semantic guidance plus bounded write grants, current job then retained pages.
Evidence source ID and local anchor: see records; SRC-1 `src/claims/guidance.ts`.
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none; requested semantic verification is not observed acceptance.
Gap/limit: No accepted ampliative proposition is established by fluent page generation or persistence.

Route ID: [EPI-RTE-evidence-preflight](#epi-rte-evidence-preflight)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-page-claims](#epi-obj-page-claims)
Content/update relation: no content change
Transition or check target: Persisted source identities and versions, not proposition truth.
Evaluator/condition and domain: see record.
Activation and timing: Update preparation, before no-op selection.
Possible or observed result: Stale or unresolved issue, or no issue.
Implemented force: Evidence debt supplied to planning and mandatory reconciliation.
Epistemic authority and scope: Current resource/version support only; unchanged cited text does not entail an arbitrary Claim.
Operational authority: Owning page requires work despite planner omission; stale content not automatically retracted.
Behavioral-authority path: Core planner augmentation and page model/host, issue list, enforcing work requirement and advisory recheck, update/resume.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none.
Gap/limit: Changes outside cited resources may undermine a proposition without a version issue; complete semantic dependency coverage is a model responsibility.

Route ID: [EPI-RTE-claim-decisions](#epi-rte-claim-decisions)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-page-claims](#epi-obj-page-claims)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Complete page Claim set from sparse additions, updates, confirmations and retractions.
Evaluator/condition and domain: Model/host declares semantic decisions; fixed code checks ownership, explicit issue decisions, nonempty set and resolvable evidence.
Activation and timing: submit_page after page write/frontmatter repair.
Possible or observed result: Updated set or rejection; unchanged issue-free Claims auto-confirmed.
Implemented force: Structural/protocol admission, not independent source-to-statement truth judgment.
Epistemic authority and scope: Intended semantic criterion is accuracy against current source for future repository use. Code consumes resource versions, not an entailment proof; no recorded evidence-consuming semantic acceptance of a produced ampliative claim supplied.
Operational authority: Disposes Claim membership and allows finalization only when protocol conditions hold.
Behavioral-authority path: Claim session and lifecycle, sparse decision payload, enforcing membership/continuation, current update and persisted future runs.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none; auto-confirm is not a new semantic endorsement.
Gap/limit: Retraction removes a structured Claim; corresponding prose correction is instructed, not compared by this function.

Route ID: [EPI-RTE-claims-persistence](#epi-rte-claims-persistence)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-page-claims](#epi-obj-page-claims)
Content/update relation: no content change
Transition or check target: Reconciled session state to durable page sidecar.
Evaluator/condition and domain: Final evidence-version check, issue clearance and page hash/write success; see record.
Activation and timing: Before job completion and whole-run finish.
Possible or observed result: Durable Claims/version/event or warning and strict failure.
Implemented force: Enforcing durability gate.
Epistemic authority and scope: Retains candidate propositions and code-owned lineage, not additional semantic warrant.
Operational authority: Completion can advance only after durability proof.
Behavioral-authority path: Core, sidecar and durability assertions, enforcing, current queue and later update sessions.
Evidence source ID and local anchor: see record and [RT-CLM-page-durability](runtime.md#rt-clm-page-durability).
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none.
Gap/limit: Filesystem protocol is not a whole-run transaction or proof of proposition coverage.

Route ID: [EPI-RTE-verification-projection](#epi-rte-verification-projection)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-verification-events](#epi-obj-verification-events)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Durable Claim verification event to page frontmatter; withdrawal of producer-owned stale events.
Evaluator/condition and domain: Eligibility from persistence, nonempty set, no issues and recorded event; hash refresh guards projection durability.
Activation and timing: Claims finalization.
Possible or observed result: Stamp added/retained, OpenWiki-family stamps removed, unsafe projection rolled back.
Implemented force: Changes metadata visible to consumers; no universal downstream admission rule follows.
Epistemic authority and scope: Records passed Claims protocol, not infallibility or complete page truth.
Operational authority: Strict warnings fail lifecycle finalization; preserved foreign events are not certified.
Behavioral-authority path: Finalizer through Markdown to reader/tool, enforcing persistence failure and otherwise descriptive metadata, future page availability.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none.
Gap/limit: Removal of metadata does not remove prose or prove downstream withdrawal of reliance.

Route ID: [EPI-RTE-source-projection](#epi-rte-source-projection)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-page-sources](#epi-obj-page-sources)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Precise Claim resources to page-level source list.
Evaluator/condition and domain: Canonical whole-file mapping, deduplication, stable resource-derived IDs and preservation of independent entries.
Activation and timing: Artifact finalization.
Possible or observed result: Page source list with line ranges removed.
Implemented force: Provenance presentation and retrieval path hints, not semantic acceptance.
Epistemic authority and scope: Source-file lineage preserved; exact statement/range alignment degraded in this projection, still retained in Claims sidecars.
Operational authority: Changes discoverable provenance; write errors abort projection.
Behavioral-authority path: Page reader and retrieval selector, sources field, descriptive/ranking input, later reads.
Evidence source ID and local anchor: see record; SRC-1 `src/retrieval/wiki.ts`.
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none.
Gap/limit: File-level source list cannot independently warrant all prose.

Route ID: [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-markdown](#epi-obj-wiki-markdown)
Content/update relation: no content change
Transition or check target: Retained prose selected for later host context.
Evaluator/condition and domain: Lexical relevance and path hints; search excludes deprecated status, not a semantic truth judgment.
Activation and timing: Foreground host request followed by explicit section selection.
Possible or observed result: Ranked references then requested sections.
Implemented force: Ranking and context delivery.
Epistemic authority and scope: No new warrant from retrieval; skill requests verification against current source.
Operational authority: Supplies approach-shaping context, not instructions under the shipped skill.
Behavioral-authority path: see [RT-BAP-retrieved-sections](runtime.md#rt-bap-retrieved-sections).
Evidence source ID and local anchor: see record; SRC-1 `src/retrieval/wiki.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: Search status filter is not a demonstrated universal withdrawal gate; explicit read and host reliance require separate assessment.

Route ID: [RT-RTE-personal-ingestion](runtime.md#rt-rte-personal-ingestion)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-markdown](#epi-obj-wiki-markdown)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Connector/raw external evidence entering update context; subsequent model prose transformation is indeterminate.
Evaluator/condition and domain: Configured connector pull and model source-curation guidance; no repository Claim criterion for connector-derived facts.
Activation and timing: Requested source ingestion/update.
Possible or observed result: Raw evidence and model wiki edits.
Implemented force: Filesystem retention and later chat context supply.
Epistemic authority and scope: External source warrant unknown; transport/import establishes acquisition, not production or endorsement.
Operational authority: Personal graph writes local wiki without repository page submission.
Behavioral-authority path: see record; model update and later personal/chat consumers, raw/tool/filesystem channel, interpreted context, subsequent sessions.
Evidence source ID and local anchor: see record.
Claim IDs: [EPI-CLM-grounded-claims](#epi-clm-grounded-claims).
Mismatch marker: none; connector scope explicitly excluded from Grounded Claims.
Gap/limit: Specific personal outputs and downstream chat compliance unobserved.

Route ID: [RT-RTE-page-translation](runtime.md#rt-rte-page-translation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-markdown](#epi-obj-wiki-markdown)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Whole-page language conversion.
Evaluator/condition and domain: Nonempty output and token-limit termination checks; semantic preservation requested only.
Activation and timing: Non-repository-generation update hook; language switch or retry marker.
Possible or observed result: Rewritten prose or deferred marker.
Implemented force: Code permits write/retry based on transport/completion checks.
Epistemic authority and scope: Checks license usable output shape, not faithful translation.
Operational authority: Output written directly through backend outside ordinary tool selection.
Behavioral-authority path: see record; middleware/backend to later readers, retained Markdown, permissive write, future reads.
Evidence source ID and local anchor: see record.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: No independent translation oracle or observed semantic result.

Route ID: [EPI-RTE-ledger-judgment](#epi-rte-ledger-judgment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-ledger-verdicts](#epi-obj-ledger-verdicts)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Artifact assertions against bounded current/historical source excerpts.
Evaluator/condition and domain: Model source-grounding classifier; supplied evidence is reference material, not a predetermined expected verdict.
Activation and timing: Separate benchmark checkpoint after generation/artifact capture.
Possible or observed result: Support/contradiction/not-addressed judgments and downstream precision classifications.
Implemented force: Benchmark assessment, not product page admission.
Epistemic authority and scope: Intended license is evidence-grounding within selected excerpts and tense; implementation does not prove model judgment accuracy or extraction fidelity.
Operational authority: Feeds metrics, diagnostics and verdict caching; does not veto repository submit_page.
Behavioral-authority path: Benchmark consumer, structured verdict channel, reporting/cached reuse, benchmark rounds.
Evidence source ID and local anchor: see record.
Claim IDs: none.
Mismatch marker: none; this is a countercase to an unqualified absence of semantic evaluators.
Gap/limit: Bounded source corpus and extraction may omit necessary evidence or qualifiers; no observed result or empirical calibration.

Route ID: [EPI-RTE-ledger-reporting](#epi-rte-ledger-reporting)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-ledger-verdicts](#epi-obj-ledger-verdicts)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Raw verdicts to checkpoint metrics and diagnostics.
Evaluator/condition and domain: Fixed metric/report consumers; see record.
Activation and timing: After checkpoint evaluation.
Possible or observed result: Counts/rates, raw verdict ledger and continued obsolete watch set.
Implemented force: Reporting and next benchmark evaluation context.
Epistemic authority and scope: Metrics summarize judgments, not independent truth or causal benefit.
Operational authority: Carries watch state and aggregates score; inspected runner does not send verdicts back as product-edit instructions.
Behavioral-authority path: Benchmark runner and operator, result/carry, reporting and evaluation selection, benchmark rounds.
Evidence source ID and local anchor: see record.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: This consumer is consequential without being a production acceptance gate or established behavioral improvement.

No lifecycle-integration route after semantic acceptance is established by these inspected product paths. Source projection and page linking retain/organize admitted artifacts; they do not supply the missing semantic acceptance decision. This is a bounded distinction, not a system-wide absence: evaluator and other included paths remain partially unassessed.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | Versioned evidence identifies facts needing confirmation/revision/retirement; successful nonempty durable reconciliation projects verification | see record; doctrine/design | Shared substantive/falsifiable Claim and sparse reconciliation guidance | [EPI-RTE-evidence-preflight](#epi-rte-evidence-preflight), [EPI-RTE-claim-decisions](#epi-rte-claim-decisions), [EPI-RTE-claims-persistence](#epi-rte-claims-persistence), [EPI-RTE-verification-projection](#epi-rte-verification-projection), [EPI-RTE-source-projection](#epi-rte-source-projection) | None supplied | No causal experiment; cited-evidence completeness and semantic judgment depend on researcher | Version/debt/durability architecture implemented, scoped to repository evidence | “Grounded” does not add a deterministic entailment test; connector-derived facts explicitly excluded. |
| [RT-CLM-page-durability](runtime.md#rt-clm-page-durability) | Completion follows persisted Claims and proof | see record; implementation | Ordered lifecycle protocol | [EPI-RTE-claims-persistence](#epi-rte-claims-persistence) | None supplied | Filesystem/dependency assumptions; no transactional crash-proof claim | Enforcing queue continuation rule | Durability does not establish semantic agreement, exhaustive page coverage or source truth. |

## Bounded conclusion

OpenWiki implements a repository evidence-debt loop, not merely a timestamp refresh. Resource/version comparisons identify stale or unresolved evidence; explicit decisions are required for affected Claims, while issue-free omitted Claims survive automatically. The finalizer rechecks evidence, persists a nonempty reconciled set and projects a producer-owned verification event. Structural rejection, page durability and retry/restore are operative controls over completion. Their criterion is protocol validity and current evidence identity for repository-page use, not deterministic truth of the Claim statement.

Semantic research is delegated to the native model or external host. The guidance demands independently falsifiable material propositions, current-source checking and agreement between prose and Claims. That request is implemented guidance; neither execution nor accurate compliance was observed. Actual semantic transformation remains indeterminate without proposition-level inputs and outputs. No produced accepted ampliative claim is evidenced, and source acquisition is not itself production. This does not exclude entailed or ampliative outputs in real runs.

Source provenance has two granularities. Claims retain precise resources/versions; page-level sources deliberately collapse ranges to whole files. Verification events can be removed or rolled back without removing prose. Search suppresses deprecated pages and ranks sections using relevance, not semantic endorsement. Later host context has advisory force and an instruction to verify against source. No observed downstream reliance, universal withdrawal enforcement or benefit follows.

Personal ingestion acquires externally warranted-or-unwarranted material with warrant unknown; its model edits do not use the repository Claim admission criterion. Translation has nonempty/truncation checks but no evidenced fidelity oracle. Both remain separately assessable from repository Claims.

LEDGER is an implemented semantic evaluator countercase: it judges extracted assertions against bounded source excerpts, records verdicts, computes metrics and carries obsolete targets forward. Its results are consequential in the benchmark but do not act as the inspected product generation acceptance gate. No supplied experiment establishes judgment quality, forgetting effectiveness or causal component benefit.

The inspected paths support retained external state and independent model/host semantic work. They do not establish learning as improved future capacity, content-directed theory criticism with blame and iteration, or exercised self-improvement. These properties remain independently unestablished within the assessed paths, not disproved system-wide. Model/provider internals and named unassessed operations prevent broader negatives.

## Shared records

### Operative objects

#### EPI-OBJ-page-claims
Label: Page Claims

Source-native identity: Claim/PageClaims, statement plus resource/version evidence; natural-language statement consumed by model/host and symbolic IDs/versions consumed by code; substrate: `openwiki/.claims/` JSON sidecars and process-local session state. Distinct from [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state): proposition/evidence ledger rather than queue. SRC-1 `src/generation/page-jobs.ts`, `src/claims/brains/code/session.ts`.

> Material factual proposition asserted by the completed page.
> --- `src/generation/page-jobs.ts`

#### EPI-OBJ-wiki-markdown
Label: Wiki Markdown

Source-native identity: generated Markdown page; natural-language prose and diagrams interpreted by readers/model; substrate: repository or local-wiki files. Distinct from [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance): output knowledge rather than assignment instructions. [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval) supplies retention/read evidence and passages. SRC-1 `src/retrieval/wiki.ts`.

#### EPI-OBJ-verification-events
Label: Claims verification events

Source-native identity: ClaimsVerificationEvent/verified; symbolic producer/time mappings consumed by fixed projection code and potentially interpreted as trust metadata; substrate: sidecar and Markdown frontmatter. Distinct from runtime queue objects; not merely a completed status. SRC-1 `src/okf/claims-verification.ts`, `src/claims/brains/code/session.ts`.

> const retained = current.filter((event) => !isOpenWikiActor(event.by));
>     const active = verificationByPage.get(page);
>     const next = active ? [...retained, { ...active }] : retained;
> --- `src/okf/claims-verification.ts`

#### EPI-OBJ-page-sources
Label: OKF page sources

Source-native identity: sources entries; symbolic resource/ID mappings, Markdown YAML substrate. Distinct from [EPI-OBJ-page-claims](#epi-obj-page-claims): page-level whole-file projection omits statements/versions. No supplied runtime object counterpart. SRC-1 `src/okf/claim-sources.ts`.

> function toWholeFileRepositoryResource(resource: string): string {
>   const parsed = parseRepositoryEvidenceResource(resource);
>   return formatRepositoryEvidenceResource({ path: parsed.path });
> }
> --- `src/okf/claim-sources.ts`

#### EPI-OBJ-ledger-verdicts
Label: LEDGER verdicts

Source-native identity: precisionEvaluations/CheckpointResult; natural-language assertions/rationale plus symbolic verdicts/counts; substrate: benchmark working state/result object, optionally durable benchmark outputs whose full persistence path is not assessed. Distinct from runtime product objects: separate evaluation ledger, not page Claim membership. SRC-1 `evals/ledger/run/evaluate-checkpoint.ts`.

> evaluations: {
>       precisionEvaluations: evaluation.precisionEvaluations,
>       forgettingEvaluations: evaluation.forgettingEvaluations,
>       warnings: evaluation.warnings ?? [],
>     },
> --- `evals/ledger/run/evaluate-checkpoint.ts`

### Routes

#### EPI-RTE-evidence-preflight
Label: Evidence version preflight
Part of: [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

A material subfunction of the native generation container, also used by shared host core. Owner: fixed Claims preflight; persisted pages/resources → resolver → issue list → planning/page assignments. Evaluates resource resolution and version equality, not statements. Source-backed issue guidance leaves stale propositions open to confirmation, not automatic retirement. SRC-1 `src/claims/brains/code/preflight.ts`, `src/generation/page-jobs.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Persisted sets, ordered stale/unresolved issues and orphan inventory.
- Later read-back: Issues derive from previous-run sidecars and reach the next update's planning/page work.
- Delegated visibility: Page worker receives attention-requiring Claims; complete set inspectable on demand.
- Selection predicate: Every discovered page with persisted Claims; unresolved resources take precedence over changed versions.
- Invalidation or expiry: Current resolver result compared with prior evidence version; issue cleared by reconciliation, not elapsed time.
- Activation or effect: Required page augmentation plus explicit decision requirement blocks silently omitting debt.
- Evidence limits: Deterministic freshness/license over selected resources, not entailment or complete dependency coverage.

> } else if (current.evidence.version !== evidence.version) {
>           changedResources.push(evidence.resource);
>         }
> --- `src/claims/brains/code/preflight.ts`

> - Treat a stale or unresolved marker as a requirement to recheck current source, not as an instruction to retract the Claim automatically.
> --- `src/claims/guidance.ts`

#### EPI-RTE-claim-decisions
Label: Sparse Claim decisions
Part of: [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

Subfunction used by both native and host submission. Model/host proposes; fixed reconciliation core decides membership/protocol admissibility and can veto. Open init/update work, no predetermined answer oracle or human per-page approval established. Triggers: page completion proposal or evidence debt. Guidance asks current accuracy and prose agreement; payload can add, update, confirm or retract. Unknown/multiply targeted IDs, unhandled issues and empty final factual set fail; unmentioned issue-free Claims auto-confirm. Retry-safe absent retractions differ from unknown confirmations. Worker snapshot recovery is see [RT-RTE-native-generation](runtime.md#rt-rte-native-generation); host edits require host recovery. SRC-1 `src/generation/page-jobs.ts`, `src/claims/core/mutations.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Complete reconciled session set or exception.
- Later read-back: Admitted set persists through finalization and is inspected in future updates.
- Delegated visibility: Sparse payload; omitted current Claims stay in core, not repeated through every model turn.
- Selection predicate: Pending page ownership and explicit decisions, with automatic confirmation only absent issues.
- Invalidation or expiry: Retraction removes Claim membership; updates replace statement/evidence; current evidence resolved again.
- Activation or effect: Membership changes and eligibility for finalization; actual semantic recheck unobserved.
- Evidence limits: Prose agreement and Claim materiality are guidance; this function does not compare natural-language statement entailment to source.

> if (current.issue) {
>       throw new RepositoryRunError(
>         "invalid_input",
>         `Claim ${current.id} is ${current.issue.kind} and requires an explicit confirm, update, or retract decision.`,
>       );
>     }
>     operations.push({ op: "confirm", id: current.id });
> --- `src/generation/page-jobs.ts`

> if (operation.op === "retract") {
>       working.splice(claimIndex, 1);
>       continue;
>     }
> --- `src/claims/core/mutations.ts`

#### EPI-RTE-claims-persistence
Label: Claims durable persistence
Part of: [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

Core ClaimSession owns dirty set → final evidence recheck/page hash → sidecar write → durable eligibility. Veto: unresolved issues, evidence drift, missing page or persistence warnings. Model/host supplied propositions survive only protocol checks; no new human/semantic acceptance is added here. Open generation mode; no answer oracle. Recovery removes missing/orphan/deleted sidecars and keeps resumable state on fatal finalization; snapshot recovery is separately bounded in runtime. SRC-1 `src/claims/brains/code/session.ts`, `src/claims/brains/code/runtime.ts`. Distinct retention subfunction from decisions; [RT-CLM-page-durability](runtime.md#rt-clm-page-durability) supplies queue consequence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-page verification eligibility and warnings; strict facade throws on warnings.
- Later read-back: Durable Claim statement/evidence/version state reaches future preflight and inspection.
- Delegated visibility: Code persists complete session set, including omitted issue-free Claims.
- Selection predicate: Dirty nondeleted nonexcluded states, followed by persisted/clean/nonempty/no-issues/event eligibility.
- Invalidation or expiry: Missing/deleted/orphan page cleanup removes sidecars; changed evidence blocks clean verification.
- Activation or effect: Writes sidecars before queue completion and enables verification projection.
- Evidence limits: No observed I/O/crash outcome or semantic truth test; process/filesystem assumptions remain.

> await this.assertEvidenceStillCurrent(page, state.claims, resolver);
>         ready.push({ page, state, hash: await store.hashPage(page) });
> --- `src/claims/brains/code/session.ts`

> const nextVerification =
>         state.claims.length > 0 ? { ...verification } : undefined;
> --- `src/claims/brains/code/session.ts`

> const eligible =
>         state.persisted &&
>         !state.dirty &&
>         state.claims.length > 0 &&
>         state.issues.length === 0 &&
>         state.verification !== undefined;
> --- `src/claims/brains/code/session.ts`

#### EPI-RTE-verification-projection
Label: Verification projection withdrawal
Part of: [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

Core projection: durable eligibility map → frontmatter event list → page-version refresh/rollback. Distinct metadata subfunction, not persistence of proposition sets. SRC-1 `src/okf/claims-verification.ts`, `src/claims/brains/code/runtime.ts`. Concrete deduction: current events by `human` and `openwiki/old`, with no active event for the page, yield only the human event. The filter recognizes the OpenWiki actor family; it does not judge the human event's truth or erase body prose. This deduction traces inspected code, not target execution.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Changed-page original Markdown map and refreshed-page warnings.
- Later read-back: Projected verified metadata is retained for later page readers; actual interpretation unobserved.
- Delegated visibility: Reader can see page event rather than whole eligibility calculation.
- Selection predicate: All discovered pages; retain non-OpenWiki events and append active durable event only when supplied.
- Invalidation or expiry: No active event removes producer-family metadata; hash-refresh failure rolls unsafe stamps back to original Markdown.
- Activation or effect: Adds/withdraws descriptive trust metadata; strict wrapper rejects warning-bearing finalization.
- Evidence limits: This is lineage/protocol projection, not a downstream universal reliance gate.

> return /^openwiki\//u.test(actor);
> --- `src/okf/claims-verification.ts`

> if (unsafeStamps.length > 0) {
>     await rollbackClaimsVerification(store, originals, unsafeStamps);
>   }
> --- `src/claims/brains/code/runtime.ts`

#### EPI-RTE-source-projection
Label: Whole-file source projection
Part of: [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

Deterministic finalizer maps Claim resource sets to page sources. Distinct lineage transformation rather than semantic generation; native and host core share it. SRC-1 `src/okf/claim-sources.ts`. Concrete deduction: `repo://src/server.ts#L40-L82` and `repo://src/server.ts#L90-L100` become one `repo://src/server.ts` entry, unless an independent entry already represents that resource. Parser extracts path, formatter drops range, Set deduplicates, sort canonicalizes, retained-resource filter avoids duplication. Warrant degrades only in exposed granularity; original precise evidence stays in Claims.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated frontmatter or no write; write failure throws.
- Later read-back: Page-level sources reach later readers and retrieval path hints.
- Delegated visibility: Page sources expose files, not statement-specific ranges/versions.
- Selection predicate: Current concept paths with page-owned resources in supplied map.
- Invalidation or expiry: Replace/remove deterministic OpenWiki-owned entries; preserve independently authored entries.
- Activation or effect: Metadata reshaped for provenance and search, not accepted semantic content.
- Evidence limits: Concrete transformation follows source code; no executed fixture or verified output artifact.

> const projected = [...new Set(resources.map(toWholeFileRepositoryResource))]
>     .sort((left, right) => left.localeCompare(right))
>     .filter((resource) => !retainedResources.has(resource))
> --- `src/okf/claim-sources.ts`

#### EPI-RTE-ledger-judgment
Label: LEDGER source judgment

Separate evaluator, no supplied runtime counterpart: artifact assertions plus bounded source excerpts → model batch judgment → precision evaluations/cache. Owner: benchmark evaluator, not production generation core. Targets distinguish current assertions and historical narration; current claims use current evidence, historical claims combined bounded corpus. Model proposes judgment under explicit evidence criterion; batch/response code handles failures, with complete validation details uninspected. Benchmark mode, not product init/update approval; reference evidence provided but no expected-answer oracle for each judgment. External evaluator model parameters/version pinning and mutable endpoint resolution remain uninspected; no local parameter update established in these paths. SRC-1 `evals/ledger/evaluator/precision.ts`, `evals/ledger/evaluator/prompts.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured per-target judgments and degraded-result indicators.
- Later read-back: Nondegraded verdicts can be cached for matching subsequent targets; checkpoint evaluations consume them.
- Delegated visibility: Judge receives bounded target/evidence batches, not unrestricted repository access.
- Selection predicate: Extracted targets, current/historical split and configured batching; upstream extraction/retrieval completeness unassessed.
- Invalidation or expiry: Cache conditional on key and nondegraded result; full cache-key validity unassessed.
- Activation or effect: Feeds classifications and reporting, not submit_page acceptance.
- Evidence limits: Model evaluator accuracy, extraction faithfulness, evidence selection and actual activation not observed.

> - "supported": the supplied evidence establishes the assertion. For a current
>   assertion, current evidence must establish it. For a historical assertion, the
>   evidence must establish that it held at the earlier checkpoint it describes.
> - "contradicted": the supplied evidence establishes an incompatible truth.
> - "not-addressed": the evidence neither establishes the assertion nor establishes
>   something incompatible with it.
> --- `evals/ledger/evaluator/prompts.ts`

> const [currentJudgments, historicalClaimJudgments] = await Promise.all([
>     judgeTargets(currentTargets, PRECISION_JUDGMENT_SYSTEM),
>     judgeTargets(historicalClaimTargets, PRECISION_JUDGMENT_SYSTEM),
>   ]);
> --- `evals/ledger/evaluator/precision.ts`

#### EPI-RTE-ledger-reporting
Label: LEDGER checkpoint reporting

Separate benchmark consumer, no supplied runtime counterpart: verdicts → claim counts/completeness/progress/checkpoint result → score/diagnostics and next carry. Owner: fixed checkpoint evaluator/runner. It selects evaluation context, not product successors. No human content admission established by reporting. SRC-1 `evals/ledger/run/evaluate-checkpoint.ts`, `evals/ledger/run/runner.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CheckpointResult, history and nextCarry; final runner result with score and diagnostics.
- Later read-back: Previous artifact/surface and outstanding obsolete targets enter subsequent checkpoint evaluation; raw verdicts remain in result.
- Delegated visibility: Progress callback/operator receives counts and selected stale/invented assertions; complete result retains verdict arrays.
- Selection predicate: Evaluation arrays and obsolete watch-state advancement, not production page queue eligibility.
- Invalidation or expiry: Even judged-forgotten obsolete targets stay under watch until requirement revival removes them.
- Activation or effect: Changes benchmark reporting and later evaluation target state; no inspected corrective write from verdict into product wiki.
- Evidence limits: Reporting does not establish actual performance or successful forgetting; full persistence/forgetting implementations not assessed.

> const nextCarry: CheckpointCarry = {
> --- `evals/ledger/run/evaluate-checkpoint.ts`

> outstandingObsolete: obsoleteFacts,
>     previousArtifact: artifact,
>     previousCheckpointId: checkpoint.id,
>     previousSurface: surface,
> --- `evals/ledger/run/evaluate-checkpoint.ts`

> checkpoints: checkpointResults,
>       score: computeLedgerScore(checkpointResults),
>       diagnostics: computeDiagnostics(history),
> --- `evals/ledger/run/runner.ts`

### Claims

#### EPI-CLM-grounded-claims
Label: Grounded Claims contract

Public source-native claim: repository pages retain versioned evidence for substantive facts, changes identify work, and successful durable nonempty reconciliation projects verification. Distinct from [RT-CLM-page-durability](runtime.md#rt-clm-page-durability): broader warrant/lineage contract containing but not reducible to queue durability. SRC-1 `README.md`, doctrine/design; substantive criteria in `src/claims/guidance.ts`.

> OpenWiki tracks the facts behind each repository page as **Grounded Claims**. Each Claim points to versioned source evidence, such as `repo://src/server.ts#L40-L82`. When that evidence changes or disappears, OpenWiki identifies which facts need to be confirmed, rewritten, or retired.
> --- `README.md`

> Grounded Claims currently apply to repository code wikis and repository evidence. Connector-derived facts, including LangSmith-only observations, are not claimed.
> --- `README.md`

> - Repository pages receive `verified: {by: openwiki/<version>, at: ...}` only after a successful page submission reconciles a non-empty complete Claims set, passes the final evidence recheck, and persists the Claims sidecar. Clean preflight alone never creates or advances verification; human and other process events are preserved.
> --- `README.md`

> - The final page body and reconciled Claim set must agree.
> --- `src/claims/guidance.ts`
