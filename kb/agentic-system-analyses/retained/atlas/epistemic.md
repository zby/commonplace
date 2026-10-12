---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ATLAS epistemic routes: record admission, knowledge updates, contradiction flags and the limits of downstream reliance."
run-id: AAS-2026-10-12-atlas-b28ea1ea613f-01
reviewed-boundary: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
---

# ATLAS epistemic report

## Source-and-claim boundary

The question is how ATLAS turns incoming logistics information into retained and later usable content, and what its checks license. Scope, dependencies and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is the [Source register](boundary.md#source-register), SRC-1. The whole shipped system includes its internal chat and maintenance callers, not just returning MCP tools. External hosts' decisions, live service behavior and provider internals remain outside inspection.

All route judgments below use implementation or doctrine/design, not observed operation. No deployment documents, provider responses, retained operational KB, executed tests or intervention comparisons were supplied. These missing items respectively prevent judging source truth/completeness, actual model transformations, historical acceptance, test success and causal benefit. Accessible provider parameters are covered by [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client); hidden provider state is not determinable. No claim of internal model training follows from the non-training client API.

Consequential knowledge claims are [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment) and [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge). The broader scope claim [RT-CLM-data-layer](runtime.md#rt-clm-data-layer) is relevant because it excludes behavior the shipped internal routes permit.

### Coverage

Direct reads below are additions to, or checks against, the supplied runtime account. Search of frozen CLI dispatch, package scripts, MCP registrations and chat switch found explicit evaluators and derived-result tools as well as the ordinary ingestion routes. No hook-based semantic acceptance mechanism was identified in those inspected dispatch surfaces. This is not a negative covering all repository code.

| Entry point or operation | Source path, SRC-1 | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Extraction and record admission | `src/ai/extract.js`, `src/mapper.js` | Direct reads of parsing/filtering and complete mapper; [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [EPI-RTE-field-mapping](#epi-rte-field-mapping) | No source documents or completions; semantic fidelity unobserved. |
| Enrichment, selection, action application and conflict marking | `src/ai/knowledge-engine.js` | Complete direct read; [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [EPI-RTE-contradiction-marking](#epi-rte-contradiction-marking) | No actual KB/model response; no assessed instance of accepted ampliative content. |
| Scheduled metadata enrichment | `src/modules/knowledge-enricher/index.js` | Supplied [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary) | Driver sends metadata, not extracted fact bodies; substantive reconstruction cannot be inferred. |
| Upload, watchers, Drive, connectors, seed | `src/ui-server.js`, `src/modules/file-watch/index.js`, `src/modules/google-drive/index.js`, `src/connector-runner.js`, `bin/atlas.js` | Supplied [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [RT-RTE-record-import](runtime.md#rt-rte-record-import); direct CLI dispatch search | Parser/transport helpers not independently audited here; dataset equivalence cannot be certified. |
| Chat, read/save and browser KB edits | `src/ai/chat.js`, `src/ui/pages/knowledge.js`, `src/ui-server.js` | Direct switch/return search; supplied [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit) | No semantic answer check established; compliance and human acceptance unobserved. |
| MCP registrations and returning queries | `src/index.js`, `src/ui-server.js`, `src/atlas.js` | Direct registration search and query/closure/SLA/idle/anomaly reads; [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query), [EPI-RTE-derived-results](#epi-rte-derived-results) | External host consequences excluded; row caps constrain completeness. |
| Pruning, progress, replacement/deletion | `src/atlas.js` | Direct retention body; supplied [RT-RTE-record-import](runtime.md#rt-rte-record-import), [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit) | Age/hash/cursor is not semantic invalidation; historical validity not established. |
| CLI validate, schema validator, test suite and test-ai | `bin/atlas.js`, `src/validate-models.js`, `src/__tests__/knowledge-engine.test.js`, `src/__tests__/models.test.js`, `src/ui-server.js`, `package.json` | Direct CLI, validator and test-ai reads; conflict-test range and model-test search; [EPI-RTE-evaluator-tools](#epi-rte-evaluator-tools) | Remaining tests not fully audited and none executed; no system-wide performance verdict. |
| Config reload and native modules | `src/ui-server.js`, `src/module-loader.js` | Supplied [RT-RTE-config-reload](runtime.md#rt-rte-config-reload), [RT-RTE-module-lifecycle](runtime.md#rt-rte-module-lifecycle) | External plugin semantics unavailable; arbitrary plugins prevent a universal negative about evaluators/adaptation. |

## Epistemic-object inventory

Fields owned by the cited declarations say see; local truth-apt assessments are not imported claims of observed correctness.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db) | Logistics records: shipment status, carrier identity, rates, document signatures; separately, metadata asserting counts/times/errors | See record | SRC-1, `src/atlas.js` | Symbolic fields and JSON on SQLite; imported assertions not source-verified. Counts/progress are not record-level proof of admission. |
| [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge) | Markdown logistics assertions; exact truth-apt units not determinable without deployed files | See record | SRC-1, `src/atlas.js` | Text on filesystem; one shared store accepts engine, chat and direct edits with different provenance rules. |
| [EPI-OBJ-contradiction](#epi-obj-contradiction) | A reported conflict between current and new values, plus a request to verify | See record | SRC-1, `src/ai/knowledge-engine.js` | Does not decide which assertion is true or deterministically demote either. |
| [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment) | Transient proposed updates, analysis and reasons | See record | SRC-1, `src/ai/knowledge-engine.js` | JSON envelope is symbolic dispatch; content/reason is model-interpreted text. Reasons returned, not an independently checked durable acceptance decision. |
| [EPI-RTE-derived-results](#epi-rte-derived-results) | Conditional database conclusions: readiness, elapsed-time violation, idle threshold and aggregate counts | See record | SRC-1, `src/atlas.js` | Symbolic computed results, current return rather than retained memory. License bounded by inputs, time and selected rows. |
| [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools) | Generated answer and possible saved findings | See record | SRC-1, `src/ai/chat.js` | Answer truth not checked; transient text is not automatically a retained claim. |
| [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) | Not determinable within inaccessible numerical provider state | See record | SRC-1, `src/ai/llm-client.js` | Role-specific parameters, version pinning and endpoint mutability: see record. No accessible localized provider propositions or training evidence. |

## Authority-route ledger

Each compact row separates check, disposition, retention and use, even when it cites the same container. No observed result is asserted. Timing, selectors and immediate/read-back outputs owned by declarations are referenced rather than recopied.

Route ID: [RT-RTE-record-import](runtime.md#rt-rte-record-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: External rows entering the indexed record domain.
Evaluator/condition and domain: See route; source warrant unknown, with mapping interpretation separately assessed below.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Imported fields can become query premises.
Epistemic authority and scope: Acquired assertions, not source endorsement.
Operational authority: behavior permitted, blocked, or changed: Indexed records become available to fixed queries and models.
Behavioral-authority path: consumer, channel, force, horizon: See route; query result delivery is permissive evidence supply across later requests.
Evidence source ID and local anchor: SRC-1, `src/connector-runner.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Live source correctness and synchronization completeness unobserved.

Route ID: [EPI-RTE-field-mapping](#epi-rte-field-mapping)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Configured field and value mappings.
Evaluator/condition and domain: See route. Pure field copies can reshape; arbitrary static/default values can change meaning. No warranted mapping interpretation supplied.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Config rules determine candidate fields before validation.
Epistemic authority and scope: Exact JavaScript transformation is decidable; logistics equivalence is not.
Operational authority: behavior permitted, blocked, or changed: Mapped status/identity values influence subsequent admission and queries.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `src/mapper.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Cannot classify every configured mapping as meaning-preserving or entailed.

Route ID: [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Document text to proposed structured records.
Evaluator/condition and domain: See route; model is generator, not an independently evidenced truth evaluator.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Generated fields can enter database after mechanical checks.
Epistemic authority and scope: Acquisition is intended; actual outputs might copy, normalize, derive or introduce unsupported facts. Source warrant unknown.
Operational authority: behavior permitted, blocked, or changed: Candidate records feed upserts and optional enrichment.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `src/ai/extract.js`.
Claim IDs or none: [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment).
Mismatch marker or none: none.
Gap/limit: No input/output instance proves entailment or non-entailment; 40000-character input bound limits coverage.

Route ID: [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [RT-RTE-record-import](runtime.md#rt-rte-record-import)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: no content change
Transition or check target: Candidate record's minimum required field presence, not real-world accuracy.
Evaluator/condition and domain: See records; validateMapped returns valid/errors using truthiness tests.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Check result is consumed by next admission function.
Epistemic authority and scope: Establishes only the implemented field-presence criterion; no full-schema, factuality or completeness license.
Operational authority: behavior permitted, blocked, or changed: Generates a predicate used to skip invalid rows.
Behavioral-authority path: consumer, channel, force, horizon: See records; enforcing Boolean result within current import.
Evidence source ID and local anchor: SRC-1, `src/mapper.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Native upsert callers need not pass this check.

Route ID: [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [RT-RTE-record-import](runtime.md#rt-rte-record-import)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: no content change
Transition or check target: Admission to import/upsert processing.
Evaluator/condition and domain: See records; software consumes minimum-field result and known type.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Enforcing skip or pass to writer.
Epistemic authority and scope: Operational admission only, not evidence-consuming acceptance of logistics truth for a named use.
Operational authority: behavior permitted, blocked, or changed: Valid rows can be written; per-row errors do not impose whole-batch rejection.
Behavioral-authority path: consumer, channel, force, horizon: See records.
Evidence source ID and local anchor: SRC-1, `src/ai/extract.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: A pass or reported count does not certify durable admission or semantic validity.

Route ID: [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Selected retained files and new text, bounded entity summaries, or extraction metadata to update proposals.
Evaluator/condition and domain: See records; prompt asks model comparison, conflict detection and skip of existing information.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Proposal generation, followed by automatic application if mechanically admitted.
Epistemic authority and scope: Neither fluent analysis nor labeled facts establishes semantic acceptance. Metadata driver supports extraction-occurrence information, not underlying logistics assertions.
Operational authority: behavior permitted, blocked, or changed: Model can propose append, create or mark actions.
Behavioral-authority path: consumer, channel, force, horizon: See records; advisory prompt to provider, symbolic actions to executor, later files to consumers.
Evidence source ID and local anchor: SRC-1, `src/ai/knowledge-engine.js`.
Claim IDs or none: [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment), [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge).
Mismatch marker or none: New-fact and conflict language does not itself establish warranted production.
Gap/limit: No actual output allows classification as ampliative conjecture; absence of entailment proof alone is insufficient.

Route ID: [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)
Content/update relation: no content change
Transition or check target: JSON syntax and action/path envelope; action-specific required values.
Evaluator/condition and domain: See route; JavaScript parses, filters and checks executable arguments, not evidence for proposed assertions.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Produces parse/envelope result for admission.
Epistemic authority and scope: Syntax and minimal executability only.
Operational authority: behavior permitted, blocked, or changed: Parse failure can retry or end; envelope failure removes proposals.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `src/ai/knowledge-engine.js`.
Claim IDs or none: [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment).
Mismatch marker or none: none.
Gap/limit: Retry checks format, not original-source fidelity, and does not resend original newInfo.

Route ID: [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit), [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)
Content/update relation: no content change
Transition or check target: Permission to perform a file action.
Evaluator/condition and domain: See records; engine admits mechanically suitable actions; direct caller or chat save supplies full content without engine review.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Enforcing executable action dispatch/path/I/O conditions.
Epistemic authority and scope: No content-level truth acceptance established by these admission mechanisms.
Operational authority: behavior permitted, blocked, or changed: Immediate append/create/mark or direct replacement/deletion; no human per-proposal approval in engine/chat.
Behavioral-authority path: consumer, channel, force, horizon: See records.
Evidence source ID and local anchor: SRC-1, `src/ai/knowledge-engine.js`.
Claim IDs or none: [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge).
Mismatch marker or none: Existing-path create can overwrite despite add-only instruction.
Gap/limit: Editor saves may express human intent, but evidence-consuming semantic acceptance is not recorded by the generic API.

Route ID: [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit), [RT-RTE-record-import](runtime.md#rt-rte-record-import)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge), [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: no content change
Transition or check target: Admitted payload to file/database persistence.
Evaluator/condition and domain: See records; writer/database success, not truth evaluation.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Later eligibility for read and use.
Epistemic authority and scope: Retention of candidates/acquired assertions; not lifecycle integration after acceptance.
Operational authority: behavior permitted, blocked, or changed: Payloads can outlive request and affect later context.
Behavioral-authority path: consumer, channel, force, horizon: See records.
Evidence source ID and local anchor: SRC-1, `src/atlas.js`.
Claim IDs or none: [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment).
Mismatch marker or none: none.
Gap/limit: Durability depends on actual mounts/database configuration. No revision rollback or evidence graph acceptance established.

Route ID: [EPI-RTE-contradiction-marking](#epi-rte-contradiction-marking)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction](#epi-obj-contradiction)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Supplied current/new value pair to conflict block.
Evaluator/condition and domain: See route; mechanical insertion, not independent conflict adjudication.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Retained warning text; no enforcing invalidation.
Epistemic authority and scope: Preserves supplied pair and adds a verification request, without licensing either value as true.
Operational authority: behavior permitted, blocked, or changed: Consumers can see the warning; ordinary retrieval remains available.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `src/ai/knowledge-engine.js`.
Claim IDs or none: [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment).
Mismatch marker or none: applied:true can describe a missing-file no-op.
Gap/limit: Whether values really conflict and whether warning changes reliance are unobserved.

Route ID: [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query), [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools), [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db), [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)
Content/update relation: no content change
Transition or check target: Selection and delivery of retained data/context to caller or model.
Evaluator/condition and domain: See records; SQL/substring/keyword selectors and model-chosen file read, not factuality checks.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Ranking and context supply. Chat truthfulness instruction is advisory, see [RT-BAP-chat-guidance](runtime.md#rt-bap-chat-guidance).
Epistemic authority and scope: Relevant retained content delivered as evidence, without endorsement or completeness guarantee.
Operational authority: behavior permitted, blocked, or changed: Model may answer, generate updates or save findings; external host may use returning data.
Behavioral-authority path: consumer, channel, force, horizon: See records and [RT-BAP-chat-guidance](runtime.md#rt-bap-chat-guidance).
Evidence source ID and local anchor: SRC-1, `src/ai/chat.js`.
Claim IDs or none: [RT-CLM-data-layer](runtime.md#rt-clm-data-layer).
Mismatch marker or none: Returning MCP scope does not describe internal chat write authority.
Gap/limit: Delivery does not prove reliance or improved behavior; final answer has no independently evidenced truth check.

Route ID: [EPI-RTE-derived-results](#epi-rte-derived-results)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Rule-defined indexed readiness: POD presence, selected signature statuses and shipment delivered status.
Evaluator/condition and domain: See route; required-item conjunction over selected database rows.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Informational checklist only.
Epistemic authority and scope: Conditional readiness under this rule and selected rows, not verified delivery or signatures.
Operational authority: behavior permitted, blocked, or changed: Host receives checklist; no automatic close action.
Behavioral-authority path: consumer, channel, force, horizon: See route; returning MCP result, advisory to external host, current request.
Evidence source ID and local anchor: SRC-1, `src/atlas.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Default document limit 50 can omit a relevant unsigned document.

Route ID: [EPI-RTE-derived-results](#epi-rte-derived-results)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Elapsed hours since earliest indexed tracking event versus selected lane/mode planned_hours.
Evaluator/condition and domain: See route; date arithmetic, clock and threshold comparison over selected shipments.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Informational violation result, not an enforcing replan.
Epistemic authority and scope: Rule-defined threshold exceedance conditional on indexed timestamps and service levels.
Operational authority: behavior permitted, blocked, or changed: Caller/model receives violation details; no automatic shipment update.
Behavioral-authority path: consumer, channel, force, horizon: See route; MCP/chat tool-result evidence, current request.
Evidence source ID and local anchor: SRC-1, `src/atlas.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Missing prerequisites skip records; shipment sampling and result caps prevent complete breach enumeration or contractual warrant.

Route ID: [EPI-RTE-derived-results](#epi-rte-derived-results)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Indexed moving assets with last_movement_at older than requested cutoff.
Evaluator/condition and domain: See route; fixed SQL status/time predicate, enabled assets model and clock.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Informational selection and count.
Epistemic authority and scope: Matching stored status/timestamp, not independently measured asset idleness.
Operational authority: behavior permitted, blocked, or changed: External host receives selected records; no automatic intervention.
Behavioral-authority path: consumer, channel, force, horizon: See route; MCP result, advisory, current request.
Evidence source ID and local anchor: SRC-1, `src/atlas.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Timestamp interpretation/source completeness not verified.

Route ID: [EPI-RTE-derived-results](#epi-rte-derived-results)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)
Content/update relation: no content change
Transition or check target: Selection of stored is_exception tracking events.
Evaluator/condition and domain: See route; SQL field filter, not independent anomaly discovery.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Returning evidence supply.
Epistemic authority and scope: Delivers preexisting exception assertions; no novel anomaly license.
Operational authority: behavior permitted, blocked, or changed: Host/chat model receives stored events.
Behavioral-authority path: consumer, channel, force, horizon: See route; MCP/chat result, advisory, current request.
Evidence source ID and local anchor: SRC-1, `src/atlas.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Returned count is limited result length; source exception classification is not independently checked.

Route ID: [EPI-RTE-evaluator-tools](#epi-rte-evaluator-tools)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: none — parsed configuration.
Content/update relation: no content change
Transition or check target: CLI-selected YAML port/storage/connector field presence.
Evaluator/condition and domain: See route; fixed presence tests after YAML parsing.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: CLI report and failure process exit.
Epistemic authority and scope: Required fields present, not deployment correctness or source truth.
Operational authority: behavior permitted, blocked, or changed: Ends this CLI check with success/failure, without installing configuration.
Behavioral-authority path: consumer, channel, force, horizon: See route; caller sees console/exit status for this invocation.
Evidence source ID and local anchor: SRC-1, `bin/atlas.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: No check execution supplied; no automatic config-admission gate established.

Route ID: [EPI-RTE-evaluator-tools](#epi-rte-evaluator-tools)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: none — model schema files.
Content/update relation: no content change
Transition or check target: JSON schema parsing, required metadata and AJV compilation.
Evaluator/condition and domain: See route; JSON parser, presence checks and AJV2020 compile interface.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Developer report and failure process exit.
Epistemic authority and scope: Schema structural usability, not validation of operational record instances.
Operational authority: behavior permitted, blocked, or changed: Process fails on recorded schema errors; no automatic production write gate.
Behavioral-authority path: consumer, channel, force, horizon: See route; developer console/exit status, current invocation.
Evidence source ID and local anchor: SRC-1, `src/validate-models.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: AJV dependency internals and execution uninspected; declared interface does not establish a passing schema set.

Route ID: [EPI-RTE-evaluator-tools](#epi-rte-evaluator-tools)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: none — fixture behavior and schema properties.
Content/update relation: no content change
Transition or check target: Authored expected mock outputs, string insertion/error behavior and schema-field expectations.
Evaluator/condition and domain: See route; node assertions consume fixture references, not production answer truth.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Test process report/failure.
Epistemic authority and scope: Tested code behavior under fixtures if run; no model conflict-detection accuracy license.
Operational authority: behavior permitted, blocked, or changed: Caller can inspect test result; no automatic runtime KB admission gate.
Behavioral-authority path: consumer, channel, force, horizon: See route; developer/test runner reports, current test invocation.
Evidence source ID and local anchor: SRC-1, `src/__tests__/knowledge-engine.test.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Tests unexecuted and remaining cases not exhaustively inspected; no passing-results claim.

Route ID: [EPI-RTE-evaluator-tools](#epi-rte-evaluator-tools)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: none — transient setup provider response.
Content/update relation: no content change
Transition or check target: Configured client and successful completion return, not literal reply correctness.
Evaluator/condition and domain: See route; isConfigured and exception handling; expected literal requested but not compared.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: Informational REST ok/reply/error to setup caller.
Epistemic authority and scope: Returned provider response only; even unexpected text follows ok:true branch.
Operational authority: behavior permitted, blocked, or changed: Caller receives diagnostic; no result-conditioned routing replacement.
Behavioral-authority path: consumer, channel, force, horizon: See route; REST response, advisory, current setup request.
Evidence source ID and local anchor: SRC-1, `src/ui-server.js`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: No live endpoint execution or response evidence supplied.

Route ID: [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary), [RT-RTE-record-import](runtime.md#rt-rte-record-import), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db), [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)
Content/update relation: no content change
Transition or check target: Replay eligibility, replacement/deletion and retention age, not semantic endorsement.
Evaluator/condition and domain: See records; content hash, timestamp cursor, ID match, age/status predicate or direct caller command.
Activation and timing: See records.
Possible or observed result: See records.
Implemented force: Enforces skips/deletions/replacements, changing future available premises.
Epistemic authority and scope: Freshness and progress only; extraction failure hash can still block replay, metadata cursor can advance after failed enrichment.
Operational authority: behavior permitted, blocked, or changed: Later imports skipped or old rows removed; KB writers can replace/delete retained statements.
Behavioral-authority path: consumer, channel, force, horizon: See records; future ingestion/query/KB selection, executable force across requests.
Evidence source ID and local anchor: SRC-1, `src/atlas.js`.
Claim IDs or none: [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge).
Mismatch marker or none: Store withdrawal is not coordinated semantic withdrawal from dependent knowledge/answers.
Gap/limit: No automatic invalidation of derived Markdown after record pruning is established by these routes; deletion history and rollback unavailable.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-enrichment](#epi-clm-knowledge-enrichment) | See record | SRC-1, `README.md`, doctrine/design | See record | [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary), [EPI-RTE-contradiction-marking](#epi-rte-contradiction-marking) | None supplied | Model comparison and mechanical writes exist; no comparison demonstrates accuracy/benefit | Automatic update capacity, prompt-requested conflict detection and retained flags | New facts are not thereby accepted true; scheduled driver does not deliver underlying facts. |
| [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge) | See record | SRC-1, `src/ai/knowledge-engine.js`, doctrine/design | See record | [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit) | None supplied | Existing-path create and direct writers counter an invariant reading | Add-only policy, not universal preservation guarantee | No existence veto; direct replace/delete bypasses policy. |
| [RT-CLM-data-layer](runtime.md#rt-clm-data-layer) | See record | SRC-1, `src/atlas.js`, doctrine/design | See record | [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query), [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools), [RT-RTE-module-lifecycle](runtime.md#rt-rte-module-lifecycle) | None supplied | Returning MCP callbacks differ from whole shipped system | Narrow read-service interpretation fits | Whole-system absence of decisions/effects/communication does not. |

## Bounded conclusion

ATLAS imports logistics assertions, retains symbolic records and Markdown, selects them for later requests and can automatically write model-proposed knowledge updates. Source warrant is unknown: schemas, minimum fields, filenames, attribution strings and processing timestamps do not independently verify what happened in the world. Enrichment additionally loses input coverage through selected files and first-ten-record summaries; its scheduled metadata driver supplies counts/times rather than fact bodies. See [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment) and [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary).

Checks have distinct licenses. Minimum-field and JSON checks grant immediate operational admission, not semantic acceptance. The fixed derived-result tools support conditional database conclusions, not independently verified delivery/signature/SLA propositions. Developer validators and mock tests target executable/config/schema properties, not production knowledge truth. Their designs are inspectable but none were executed. See [EPI-RTE-derived-results](#epi-rte-derived-results) and [EPI-RTE-evaluator-tools](#epi-rte-evaluator-tools).

Conflict marking retains both supplied values and a request to verify. It neither adjudicates the conflict nor mechanically withholds either statement from selection. Its text can reach later models, but changed reliance is unobserved. Existing-path create can overwrite; direct edit/save/delete permits other revision paths. Persistence is therefore not acceptance, and these writes do not establish lifecycle integration after evidence-consuming acceptance. No observed accepted ampliative claim is established within the available evidence; model production remains semantically indeterminate rather than being classified as conjecture merely because the provider is opaque. See [EPI-RTE-contradiction-marking](#epi-rte-contradiction-marking) and [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge).

The behavioral-authority chain is real at source level: model-chosen actions reach the writer, and later retained text can reach an enrichment or chat model through context/tools. Prompt guidance is advisory; JavaScript action dispatch and file/database mutation are enforcing. This supports autonomous automatic admission on those routes, not correctness, whole-system autonomous theory building or demonstrated learning. Theory formulation and content-directed criticism inside provider processing are not determinable from this source. Retained contradiction warnings alone do not establish theory-builder consumption, blame-directed criticism or iteration. No measured improved future capacity or causally established self-improvement follows. Configuration/module replacement has live operational force but no evidence-responsive improvement selector in the supplied account; provider-side learning remains inaccessible. These are independent limits, not a single system verdict.

## Shared records

### Operative objects

#### EPI-OBJ-contradiction
Label: Knowledge contradiction block

Part of: [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)

Identity: The block emitted by _applyMarkContradiction into a retained knowledge file, not the whole file or model's opaque conflict judgment. Form: natural-language current/new-value warning and verification request. Substrate: Markdown on the shared filesystem. SRC-1, `src/ai/knowledge-engine.js`, implementation. Its advisory consumer is a later file-reading model or human; it has no deterministic truth-selection force. Actual content instances are unavailable. The supplied parent establishes the store, not this warning's license.

> const block = `\n\n> **Суперечність** (джерело: ${src}, ${date}):\n> Поточне значення: ${contradiction.current_value}\n> Нове значення: ${contradiction.new_value}\n> Потребує перевірки.\n`;
> --- `src/ai/knowledge-engine.js`

### Routes

#### EPI-RTE-contradiction-marking
Label: Knowledge contradiction insertion

Part of: [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment)

Endpoints: admitted mark_contradiction → truthy current/new fields → read file → insert block after header or at end → writer. Owner: model proposes values/section/source, engine decides executability, Atlas performs write. Context: existing file and proposed pair. Trigger: admitted model update, open incoming-information mode. Guidance: engine prompt requests conflict marking, not replacement. No answer oracle. A human can supply incoming text but does not approve each block. Veto: missing pair or I/O error; missing target silently returns, after which enclosing applyUpdates reports applied:true. No rollback; other writers may revise/delete the result. SRC-1, `src/ai/knowledge-engine.js`, implementation.

Concrete deduction, without execution: for existing text `## ETA\n5 days\n`, section_header `## ETA`, current_value `5 days`, new_value `3 days`, source `contract`, date `2026-01-01`, code inserts a blank-line-prefixed warning immediately after the six-character header. It retains the original `5 days` text and prints both supplied values plus `Потребує перевірки.`. It never compares their truth or changes a selector. This is a non-ampliative rendering of a supplied conflict candidate, not newly evidenced detection. Countercase: a nonexistent path yields no block but can still return applied:true. The inspected test explicitly expects that behavior; no test execution is asserted.

- Immediate return: Enclosing per-update applied/error result, including applied:true after missing-file no-op.
- Later read-back: Inserted block is eligible for later engine or chat file delivery.
- Delegated visibility: Later selected file content can reach configured providers; human/API readers can see it too.
- Selection predicate: Action name, nonempty current/new fields, target path, first matching section header or end-of-file fallback.
- Invalidation or expiry: No warning TTL or verified-resolution mechanism in this action; store replacement/deletion can remove it.
- Activation or effect: Implemented insertion and future delivery eligibility; changed later reliance unobserved.
- Evidence limits: No actual conflicting inputs/model outputs; warning presence does not authenticate conflict, attribution or either assertion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!contradiction || !contradiction.current_value || !contradiction.new_value) {
>       throw new Error('mark_contradiction requires contradiction.current_value and contradiction.new_value');
>     }
> --- `src/ai/knowledge-engine.js`

> } catch {
>       return; // Can't mark contradiction in non-existent file
>     }
> --- `src/ai/knowledge-engine.js`

> it('silently skips non-existent file', () => {
> --- `src/__tests__/knowledge-engine.test.js`

#### EPI-RTE-field-mapping
Label: Configured field transformation

Part of: [RT-RTE-record-import](runtime.md#rt-rte-record-import)

Endpoints: raw record and mapping → applyMapping/resolveField/getPath → mapped candidate → import validation/upsert. Owner: config author supplies interpretation; JavaScript applies fixed rules. Different from the parent admission container: this part assesses meaning before validation. Form: symbolic object/config rules in process; output can be persisted as database JSON. Open synchronization or seed inputs, not an experiment. Caller/config authorship may be human but no separate per-row human approval is evidenced; no answer oracle. The mapping does not itself veto false values. Guidance consists of source-path, static value and value-map/default rules. Recovery is parent import handling, not semantic rollback. SRC-1, `src/mapper.js`, implementation.

Concrete deduction without execution: source `{tracking_number:'S1',status_code:1}` and mapping `{id:'$.tracking_number',status:{source:'$.status_code',map:{'1':'pending'},default:'unknown'}}` yields `{id:'S1',status:'pending'}`. validateMapped('shipments', result) passes because both values are truthy. This establishes a code-domain transformation and admission predicate, not that source code 1 truthfully means pending. A static `status:'delivered'` also satisfies the same presence test; this countercase prevents a blanket non-ampliative or source-truth license.

- Immediate return: New mapped object, or original source if no object mapping exists.
- Later read-back: Mapped fields can become retained record premises through the parent upsert route.
- Delegated visibility: Subsequent queries/provider context may expose mapped data; no provider call in mapping itself.
- Selection predicate: Configured target keys, dot paths, value-map membership and defaults.
- Invalidation or expiry: New mappings affect later calls; no automatic reinterpretation of prior retained rows is established here.
- Activation or effect: Deterministic candidate-field assignment wired; actual deployed mapping interpretation unobserved.
- Evidence limits: No live mapping/source contract; semantic preservation or warranted derivation not established for arbitrary rules.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const raw = getPath(source, spec.source);
>       const mapped = spec.map[String(raw)];
>       return mapped !== undefined ? mapped : (spec.default ?? raw);
> --- `src/mapper.js`

> if (typeof spec === 'string' && !spec.startsWith('$')) return spec;
> --- `src/mapper.js`

#### EPI-RTE-derived-results
Label: Indexed rule results

Part of: [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query)

Endpoints: registered read request → Atlas fixed rule/SQL → JSON result → calling host. These returning operations are material parts of the supplied query-service container, not replacement for it. Overlap with [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools): chat also exposes SLA/anomaly tools, but not all these operations; the common referent assessed here is the Atlas fixed-rule evaluation, not model selection. Owner: requester selects arguments; code defines predicates and clock evaluation. Context: retained records, enabled model flags, timestamps and current time. Form: symbolic numerical/Boolean results, not model judgment. No product/knowledge revision admission occurs. Mode: open queries; no expected-answer oracle. SRC-1, `src/atlas.js`, implementation.

Distinct targets and licenses: closure checklist tests whether the selected documents include POD, whether their signature_status belongs to fully_signed/n_a, and whether indexed shipment status equals delivered. ready_to_close is their required-item conjunction; optional review presence is not required. It does not verify signatures or close a shipment. SLA tests elapsed hours from the earliest indexed tracking event against a selected lane/mode planned_hours, skipping rows without prerequisites; this licenses that rule-defined threshold, not an independently verified contractual breach. Idle tests stored moving status and last_movement_at against a clock cutoff. Anomaly retrieval filters stored is_exception, so acquisition/filtering rather than a new anomaly theory. Query ranks token occurrences in selected JSON and does not license natural-language answer correctness. SQL counts describe query scope, not external completeness.

Concrete deduction without execution: a returned shipment status delivered, selected documents containing one POD with fully_signed status and no other selected unsigned document produces three required done entries and ready_to_close:true. Change the POD signature_status to sent: pending_docs includes it and readiness becomes false. A omitted unsigned 51st document does not affect that result because listDocuments defaults to 50. This countercase bounds the conclusion to selected rows.

- Immediate return: Rule-defined checklist, violations, idle assets, stored exceptions or counts/ranked query rows.
- Later read-back: inapplicable — these methods do not persist their results or use histories in later invocations.
- Delegated visibility: Requesting MCP host receives JSON; chat receives exposed tool results where registered.
- Selection predicate: SQL filters/limits, required-item predicates, selected SLA/mode match, time threshold or preexisting exception field as described above.
- Invalidation or expiry: Current result can become stale as rows or clock change; no cached-result invalidation protocol is established.
- Activation or effect: Returning deterministic computations wired; no automatic close/replan/write consumer in these methods.
- Evidence limits: Input truth unverified; row limits, timestamp meaning and omitted records constrain completeness; external host action excluded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const allDone = checklist.filter(c => c.required).every(c => c.status === 'done');
>     return { shipment_id: shipmentId, ready_to_close: allDone, checklist };
> --- `src/atlas.js`

> listDocuments({ shipment_id, type, limit = 50 } = {}) {
> --- `src/atlas.js`

> const elapsedHours = (now - startMs) / 3_600_000;
>
>       if (elapsedHours > sla.planned_hours) {
> --- `src/atlas.js`

#### EPI-RTE-evaluator-tools
Label: Developer and setup checks

Identity comparison: No counterpart in the supplied runtime records covers the schema-validator or conflict-test evaluator. [RT-RTE-config-reload](runtime.md#rt-rte-config-reload) mentions test-ai, but its referent is routing/config replacement, not this separate diagnostic response. This record groups inspection of independent developer/setup checks, not a common truth oracle.

Endpoints/owners: CLI validate parses YAML and checks port/storage/connector required fields → prints errors and exits; standalone validate-models parses schema JSON/checks metadata → AJV compile → counts/exit failure; node test runner executes specified assertions → test process results; REST setup test-ai sends literal-response prompt → returns reply/ok or exception. Users/developers initiate them; fixed code judges structure/mocked behavior, while test-ai makes no reply-equality comparison. Context/form: symbolic config/schema/assertions and natural-language provider response. Mode: bounded developer fixtures and open caller-configured connectivity probes. No production candidate acceptance. Proposals/selection/rollback are inapplicable here: these checks do not install revisions. Literal expected fixture values are authored test references, not model-generated answer oracles for production documents. No automatic config admission conditioned on these results was found in supplied config-reload dispatch. SRC-1, `bin/atlas.js`, `src/validate-models.js`, `src/__tests__/knowledge-engine.test.js`, `src/ui-server.js`, implementation.

Checks must be distinguished: schema compilation checks schema usability, not record-instance compliance; conflict mock assertions check string insertion and error paths, not model conflict detection. test-ai requests exactly ok but reports ok:true after a completion returns even without comparing text. Thus a returned unexpected text still follows its success branch. This is a source-supported countercase to treating the ping as a literal-answer correctness evaluator.

- Immediate return: CLI/test process status and reports; REST reply preview/ok/error.
- Later read-back: inapplicable — no diagnostic-result persistence or later result-driven selection in these inspected paths.
- Delegated visibility: Developers/caller receive diagnostics; setup provider receives ping and prompt, not production document evidence.
- Selection predicate: Discovered JSON schemas, test-runner files, chosen config file or caller-selected model endpoint.
- Invalidation or expiry: inapplicable — checks have no retained result store; future checks must be invoked anew.
- Activation or effect: Check implementations exist; none executed. CLI failure exits process, REST response informs caller, not a verified deployment gate.
- Evidence limits: Mock/reference behavior is not production accuracy; no test pass records or quality measurements supplied; remaining tests not exhaustively audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ajv.compile(schema);
> --- `src/validate-models.js`

> if (failed > 0) {
>   process.exit(1);
> }
> --- `src/validate-models.js`

> const result = await client.complete("Reply with exactly: ok", "ping");
>         json({ ok: true, reply: result.text?.slice(0, 100) });
> --- `src/ui-server.js`

### Claims

#### EPI-CLM-knowledge-enrichment
Label: Automatic knowledge enrichment

Claimed operation: AI automatically updates the KB from extracted data, detecting contradictions and appending new facts. SRC-1, `README.md`, doctrine/design. No duplicate of [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge): that claim concerns non-overwrite preservation, while this one concerns source-to-knowledge production and detection. Mechanisms support automatic proposals/application, not demonstrated correct new facts or conflict detection. Source-level conflict insertion has independent bounded force as declared above.

> - **Knowledge enrichment** — AI automatically updates your knowledge base from extracted data, detecting contradictions and appending new facts
> --- `README.md`
