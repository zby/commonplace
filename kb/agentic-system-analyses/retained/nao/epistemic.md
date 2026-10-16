---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "nao epistemic routes: analytics evidence, user-memory admission, answer tests and context diagnoses at the frozen commit."
run-id: AAS-2026-10-14-nao-f9d36a4b7276-01
reviewed-boundary: "0085625a8fd22e4f404b6a3971d153f6b6699479"
---

# nao epistemic report

## Source-and-claim boundary

The question is how nao acquires analytics evidence, generates answers and retained guidance, checks candidates and licenses later reliance. Scope and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). All additional direct reads below belong to SRC-1 at the same commit. No target execution, model calls or experiments were performed. Supplied runtime findings are provisional implementation findings, not observations.

Public claims are [EPI-CLM-analytics-answers](#epi-clm-analytics-answers), [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility) and the scoped [RT-CLM-context-readonly](runtime.md#rt-clm-context-readonly). No source passage inspected establishes a system-wide truth guarantee or autonomous accepted-knowledge-production claim. This is not a system-complete negative: the uninspected included operations below remain material.

| Entry point or operation | SRC-1 source path | Coverage and records, or limit |
| --- | --- | --- |
| CLI dispatch | `cli/nao_core/main.py` | Direct complete read: chat, sync, test, migrate, docs, skills, deploy and administrative commands are registered. Sync/chat/deploy supplied account: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-web-chat](runtime.md#rt-rte-web-chat). Migration/docs/provider bodies uninspected here; semantic preservation of their imports cannot be judged. |
| Main model/tool loop and callbacks | `apps/backend/src/services/agent.ts` | Supplied [RT-RTE-web-chat](runtime.md#rt-rte-web-chat), prompt override and compaction account; source search located prepareStep, onFinish, onError and extraction scheduling. A scoped hook search in this file, `apps/backend/src/agents/` and `cli/nao_core/` returned no literal hook match; it is not an absence claim about callbacks or extensions. |
| Built-in tool registration | `apps/backend/src/agents/tools/index.ts` | Direct complete read: SQL, semantic SQL, cached-result reads, file discovery, skills, task, Python/shell, MCP, story/chart/map, write/replace and continuation tools. Python/shell effects use the supplied runtime account; arbitrary program-generated truth claims and external MCP results are not semantically audited. |
| SQL results, presentation, rerun and paging | `apps/backend/src/agents/tools/execute-sql.ts`, `apps/backend/src/components/tool-outputs/execute-sql.tsx`, `apps/backend/src/agents/tools/read-query-result.ts` | Direct reads of execution, update, rendering and paging: [EPI-RTE-query-results](#epi-rte-query-results). Warehouse/internal DuckDB implementation uninspected; actual dataset truth and query correctness remain conditional. |
| Governed metrics | `apps/backend/src/agents/tools/execute-semantic-query.ts` | Direct complete adapter read: compile then executeQuery with compiledBySemanticLayer. Compiler and metric definitions uninspected here; official-definition fidelity is not established. [EPI-RTE-query-results](#epi-rte-query-results). |
| MCP dispatch and direct SQL | `apps/backend/src/mcp/server.ts`, `apps/backend/src/mcp/tools/context-layer.ts` | Direct server and direct-SQL registration/formatResult reads: direct SQL reuses executeQuery and caches data for assets. Read-before-query wording is advisory, not a checked prerequisite. [EPI-RTE-query-results](#epi-rte-query-results). Asset/story bodies not exhaustively inspected; saved visualizations do not independently warrant their claims. |
| MCP background chat and task frame | `apps/backend/src/mcp/tools/sub-agent.ts`, `apps/backend/src/agents/subagents/run.ts` | Supplied [RT-RTE-mcp-chat](runtime.md#rt-rte-mcp-chat), [RT-RTE-explore-task](runtime.md#rt-rte-explore-task). Report delivery/persistence is not independent answer verification. |
| Memory extraction, normalization, supersession, editing/deletion and reload | `apps/backend/src/services/memory.ts`, `apps/backend/src/agents/memory/memory-extractor-llm.ts`, `apps/backend/src/components/ai/memory-system-prompt.tsx`, `apps/backend/src/queries/memory.ts` | Direct complete reads: [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-memory-admission](#epi-rte-memory-admission). UI/authentication route for user edits uninspected; query ownership predicate is inspected. |
| Test run, expected query, extraction and comparison | `apps/backend/src/routes/test.ts`, `apps/backend/src/services/test-agent.service.ts`, `apps/backend/src/services/test-agent-verification.ts`, `cli/nao_core/commands/test/runner.py` | Direct route range, complete service/prompt and comparison/run_test range: [EPI-RTE-test-comparison](#epi-rte-test-comparison), supplied [RT-RTE-test-answer](runtime.md#rt-rte-test-answer). Assertion implementation and numeric normalization helper uninspected; no complete evaluator-correctness claim. |
| Recommendations, structural reconciliation and resolution | `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/services/context-recommendations.reconcile.ts`, `apps/backend/src/agents/tools/record-recommendation.ts`, `apps/backend/src/components/ai/context-recommendations-system-prompt.tsx` | Direct run/commit range, complete reconciler/collector and diagnostic prompt ranges: [EPI-RTE-finding-reconciliation](#epi-rte-finding-reconciliation). Feedback-coverage postprocessor and patch collector internals uninspected; full recommendation population and patch safety unestablished. |
| PR and live context admission | `apps/backend/src/services/context-pr.service.ts`, `apps/backend/src/services/context-explorer-git/live-context.service.ts`, `cli/nao_core/context/git.py` | Supplied [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). PR opening and byte admission are not semantic acceptance. |
| Automations and messaging | `apps/backend/src/handlers/automation.handler.ts`, `apps/backend/src/services/slack.ts` | Supplied [RT-RTE-automation-run](runtime.md#rt-rte-automation-run); remaining channel policies only located in runtime. Required-call presence checks completion, not truth. Channel-specific checks/withdrawal are unassessed. |
| Shipped context and maintenance skills | `example/`, `skills/` | Included but bodies uninspected here except supplied audit-skill boundary finding. Their formulated rules, test expectations and external editing loops cannot support a complete theory-builder or all-routes conclusion. |

Missing observed runs prevent conclusions about actual extraction, acceptance, subsequent dependence, deployed permissions or improvement. Missing provider weights/internals prevent weight-fixity and parameter-learning conclusions beyond the adapter findings. Missing source-data provenance and test-expectation validation prevent treating returned rows or reference SQL as ground truth. No causal comparison establishes diagnostic root causes, component effects or transfer. These limits do not erase the inspected architectural routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-query-results](#epi-obj-query-results) | Rows and columns as answers to a specified SQL query; not automatically propositions about the entire warehouse | see record | SRC-1 `apps/backend/src/agents/tools/execute-sql.ts` | Source truth, filters and intended metric semantics unresolved |
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | Project facts/metric definitions mixed with non-truth-apt instructions | see record | SRC-1 `apps/backend/src/services/agent.ts` | Must not treat all prompt text as factual knowledge; full override changes delivery |
| [EPI-OBJ-personal-fact](#epi-obj-personal-fact) | User identity/background statements | see record | SRC-1 `apps/backend/src/services/memory.ts` | Model extraction and omitted conversation can alter warrant |
| [EPI-OBJ-global-rule](#epi-obj-global-rule) | None for bare imperatives; permanence/intent judgments about the user are truth-apt inputs to selecting them | see record | SRC-1 `apps/backend/src/components/ai/memory-system-prompt.tsx` | Instruction authority is not factual warrant |
| [RT-RTE-web-chat](runtime.md#rt-rte-web-chat) | Generated answer and retained transcript parts | see record | SRC-1 `apps/backend/src/services/agent.ts` | No observed instance; semantic relation to inputs indeterminate |
| [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model) | Generated history summary, including possible factual restatements | see record | SRC-1 `apps/backend/src/services/compaction.ts` | Request to summarize does not prove meaning preservation |
| [RT-RTE-explore-task](runtime.md#rt-rte-explore-task) | Child investigation report | see record | SRC-1 `apps/backend/src/agents/tools/task.ts` | Parent receives report, not full child evidence/trace |
| [RT-RTE-test-answer](runtime.md#rt-rte-test-answer) | Verification SQL and rows plus expected-row reference | see record | SRC-1 `apps/backend/src/services/test-agent-verification.ts` | SQL extractor may not encode the textual answer faithfully |
| [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation) | Symptoms, root-cause explanations, suggested edits and resolution judgments | see record | SRC-1 `apps/backend/src/agents/tools/record-recommendation.ts` | Explicit candidate slots, not observed verified diagnoses |
| [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context) | None for identifiers/grants; carried query values are separately inventoried | see record | SRC-1 `apps/backend/src/services/agent.ts` | Operational permission is not epistemic authority |

## Authority-route ledger

Each compact row below is an assessment of one function, not a redefinition of the cited record. Generic progression, selection, retention and source-native role fields are `see` the cited records. Status is architectural; every implemented row remains operationally unobserved in this run.

Route ID: [EPI-RTE-query-results](#epi-rte-query-results)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-query-results](#epi-obj-query-results).
Content/update relation: truth-apt transformation: acquisition/import for warehouse rows, source warrant unknown; local SQL derivation is separately conditional below.
Transition or check target: requested effective SQL to returned tabular evidence.
Evaluator/condition and domain: database engine executes SQL; nao adapter gates write/passthrough access. Execution success tests executability, not correct business interpretation.
Activation and timing: on selected exposed query call, before subsequent model step.
Possible or observed result: rows, empty result or error; possible only here.
Implemented force: successful return supplies evidence; errors prevent that query's successful output.
Epistemic authority and scope: returned rows under this query/database/data snapshot; no warrant for omitted rows or source truth.
Operational authority: later analysis, charts, local postprocessing and test extraction can use results.
Behavioral-authority path: agent receives rendered tool output, advisory evidence for current conversation; MCP host receives structured/text data and query ID. No automatic agreement with its interpretation is enforced.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/agents/tools/execute-sql.ts`.
Claim IDs: [EPI-CLM-analytics-answers](#epi-clm-analytics-answers).
Mismatch marker: none.
Gap/limit: semantic compilation adapter is wired but compiler fidelity, dataset quality and actual execution are uninspected.

Route ID: [EPI-RTE-query-results](#epi-rte-query-results)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-query-results](#epi-obj-query-results).
Content/update relation: truth-apt transformation: non-ampliative reshaping for row paging/presentation. Local query derivation is truth-apt transformation: indeterminate without a concrete query and checked interpretation; correct SQL can entail aggregates from rows, but not establish external data truth.
Transition or check target: full cached rows to visible subset and cached-result lookup.
Evaluator/condition and domain: fixed slice rules; default SQL rendering maxRows is 40, paging default limit 20.
Activation and timing: rendering after query or explicit read_query_result call.
Possible or observed result: first rows with remaining-row indication; paged rows, or missing-ID error.
Implemented force: selective evidence delivery; limit warning advises not to report row count as warehouse total.
Epistemic authority and scope: preserved selected cell values, explicitly incomplete display.
Operational authority: model can request more cached rows without rerunning SQL.
Behavioral-authority path: tool text to model, advisory, current and later chat turns through cache/retained results.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/components/tool-outputs/execute-sql.tsx`.
Claim IDs: [EPI-CLM-analytics-answers](#epi-clm-analytics-answers).
Mismatch marker: none.
Gap/limit: deterministic illustration: 41 supplied rows under default renderer deliver rows 0–39 and a one-row remainder notice; read_query_result offset 40, limit 20 returns the remaining row. This is a code deduction, not an executed observation or proof of model compliance.

Route ID: [EPI-RTE-query-results](#epi-rte-query-results)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-query-results](#epi-obj-query-results).
Content/update relation: no content change for stale-output suppression; rerun replaces result bytes through the acquisition route.
Transition or check target: same query ID, old versus latest result.
Evaluator/condition and domain: updateExistingQuery/updateSameTurnQuery and superseded renderer; semantic-query IDs cannot be edited as raw SQL.
Activation and timing: rerun with earlier query_id; later transcript rendering.
Possible or observed result: replacement data or rejection; stale result points to latest result.
Implemented force: old output body omitted when superseded; semantic edit blocked.
Epistemic authority and scope: current lineage selection, not endorsement or semantic correction.
Operational authority: subsequent model/asset consumers can use latest values under same ID.
Behavioral-authority path: tool result/transcript to agent, advisory evidence, across chat turns.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/agents/tools/execute-sql.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: downstream asset refresh correctness not audited; replacing data does not prove the replacement better.

Route ID: [RT-RTE-web-chat](runtime.md#rt-rte-web-chat), [RT-RTE-explore-task](runtime.md#rt-rte-explore-task), [RT-RTE-mcp-chat](runtime.md#rt-rte-mcp-chat)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see these records for answers/reports.
Content/update relation: truth-apt transformation: indeterminate for generated factual text. Input-dependent restatement, derivation and non-entailed hypotheses remain possible; no inspected instance discriminates them. Non-truth-apt policy/content update: response formatting and proposed actions where not factual.
Transition or check target: assembled instructions, user question and selected evidence to model text.
Evaluator/condition and domain: selected provider model generates; no ordinary reference-answer oracle in supplied routes.
Activation and timing: model steps; explore report becomes parent's tool text; MCP returns answer or polling handle.
Possible or observed result: fluent answer, investigation report or clarification, unobserved here.
Implemented force: delivery and tool execution, not evidence-consuming epistemic acceptance.
Epistemic authority and scope: candidate assertions only; novelty/fluency and successful tool return do not license their explanations.
Operational authority: exposed tool calls execute within grants; answer can guide users/parent host.
Behavioral-authority path: see cited route records; interpretation is advisory, tool dispatch permissive within code gates, per run with retained chat horizon.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/agent.ts`.
Claim IDs: [EPI-CLM-analytics-answers](#epi-clm-analytics-answers).
Mismatch marker: none.
Gap/limit: actual entailment, evidence citation accuracy and downstream reliance require candidate/run evidence; models' opaque internal processing remains unassessed.

Route ID: [RT-RTE-web-chat](runtime.md#rt-rte-web-chat)
Route function: retention
Architectural status: implemented
Object/candidate ID: see record for settled messages and compaction summary.
Content/update relation: no content change for settled-message retention; truth-apt transformation: indeterminate for model compaction summary, which is not proven non-ampliative.
Transition or check target: settled response to DB; prefix to summary marker and subsequent model history.
Evaluator/condition and domain: finish callback persists regardless of a separate truth decision; compaction threshold governs summarization, not factual acceptance.
Activation and timing: completion; compaction before model steps and later stored-history reconstruction.
Possible or observed result: retained answer, lossy summary plus tail, or compaction failure with continuation.
Implemented force: persistence and model-window replacement.
Epistemic authority and scope: no new warrant from retention or shorter representation.
Operational authority: future turns receive retained content; forgotten details need explicit available reload paths.
Behavioral-authority path: stored message/summary to later agent request, advisory evidence, within and across turns.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/compaction.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: see [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model) for provider fixity. No summary faithfulness evaluator is established by the supplied account.

Route ID: [EPI-RTE-memory-extraction](#epi-rte-memory-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-personal-fact](#epi-obj-personal-fact), [EPI-OBJ-global-rule](#epi-obj-global-rule).
Content/update relation: truth-apt transformation: indeterminate for profile statements and permanence judgments; non-truth-apt policy/content update: English future-conversation directives.
Transition or check target: recent text and active memories to proposed new/superseding memories.
Evaluator/condition and domain: extractor model, prompted to distinguish persistent profile from permanent directives; no external profile oracle.
Activation and timing: background scheduling on user-message path when memory enabled; message minimum and recent/truncated text selection precede generation.
Possible or observed result: null/no change or schema-shaped candidates; no observed instance.
Implemented force: candidate generation followed by software persistence gates below.
Epistemic authority and scope: user-attributed profile candidates; source warrant unknown after extraction, English rewriting and omitted text.
Operational authority: output can reach persisted user guidance without per-item human approval.
Behavioral-authority path: extractor output to memory service, software admission; active records later enter default system instructions, advisory, other chat sessions.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/agents/memory/memory-extractor-llm.ts`.
Claim IDs: none.
Mismatch marker: prompt says full conversation and deletion; implementation supplies recent truncated text and supersedes without deleting old row.
Gap/limit: distinguish the requested full analysis from actual delivered 17-message maximum with per-message character caps; no assumption of semantic preservation or extraction accuracy.

Route ID: [EPI-RTE-memory-admission](#epi-rte-memory-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-personal-fact](#epi-obj-personal-fact), [EPI-OBJ-global-rule](#epi-obj-global-rule).
Content/update relation: truth-apt transformation: non-ampliative reshaping for ordinary prose profile normalization; non-truth-apt policy/content update: directive whitespace/terminal punctuation normalization.
Transition or check target: extracted content to normalized DB text.
Evaluator/condition and domain: deterministic trim, whitespace collapse and punctuation rule.
Activation and timing: before DB conversion/admission.
Possible or observed result: code deduction: input `  The user\nworks at Acme  ` becomes `The user works at Acme.`; all-whitespace input becomes empty and is omitted.
Implemented force: actual stored text differs in formatting; empty text withheld.
Epistemic authority and scope: no added factual warrant; prose normalization only, not a general semantic-preservation guarantee for arbitrary code or quoted spacing.
Operational authority: normalized text can be persisted and later prompted.
Behavioral-authority path: normalization function to memory row to agent instructions, enforcing at write and advisory at later model use.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/memory.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: implementation deduction needs no target execution; model extraction before it remains indeterminate.

Route ID: [EPI-RTE-memory-admission](#epi-rte-memory-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-personal-fact](#epi-obj-personal-fact), [EPI-OBJ-global-rule](#epi-obj-global-rule).
Content/update relation: no content change.
Transition or check target: normalized memory with optional supersedes_id to admissible write.
Evaluator/condition and domain: code rejects empty content and supersession IDs not in loaded existing memories; extractor schema constrains shape. Persistence criteria are structural, not a profile-truth decision.
Activation and timing: immediately after extractor output, before transaction.
Possible or observed result: filtered memory set or no writes.
Implemented force: software gate withholds structurally invalid candidates; valid candidates are written without a content-review gate in this path.
Epistemic authority and scope: no evidence-consuming acceptance criterion for profile truth; directives gain operational guidance status, not epistemic endorsement.
Operational authority: enables future-memory insertion/replacement.
Behavioral-authority path: service filter to transaction, enforcing, then model guidance across chats.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/memory.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: the prompt's permanence conditions are a requested model judgment; this code gate does not independently establish them.

Route ID: [EPI-RTE-memory-admission](#epi-rte-memory-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-personal-fact](#epi-obj-personal-fact), [EPI-OBJ-global-rule](#epi-obj-global-rule).
Content/update relation: no content change for insert/supersession; truth-apt transformation: indeterminate for human replacement text.
Transition or check target: new rows, old supersededBy links, user-owned edit/delete queries.
Evaluator/condition and domain: DB transaction and userId/id predicates; old rows become inactive rather than deleted by extractor supersession.
Activation and timing: after gate; explicit query operations can update or delete later.
Possible or observed result: persisted active/superseded rows; edited/deleted content.
Implemented force: active-set withdrawal or replacement at subsequent query.
Epistemic authority and scope: record existence and selection status only; no truth license.
Operational authority: withdrawn rows cease active-memory supply; edits can change guidance.
Behavioral-authority path: memory DB through active-row query to default agent prompt, advisory, later chats; an already built system string is not proven retroactively updated.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/queries/memory.ts`.
Claim IDs: none.
Mismatch marker: deletion language in extractor prompt is not physical deletion behavior.
Gap/limit: UI/auth route and race behavior uninspected; arbitrary user changes need not be evidence-based.

Route ID: [EPI-RTE-memory-admission](#epi-rte-memory-admission), [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-personal-fact](#epi-obj-personal-fact), [EPI-OBJ-global-rule](#epi-obj-global-rule).
Content/update relation: no content change for selection; metadata projection omits record IDs, chat IDs and timestamps.
Transition or check target: active user memory to category/content in prompt builder.
Evaluator/condition and domain: user/project enabled flags, userId, supersededBy null and current-chat exclusion. User query is not project-keyed despite project-scoped enablement.
Activation and timing: default prompt construction, not full-override route.
Possible or observed result: selected memories or empty list on disabled state/error.
Implemented force: unsolicited prompt supply; not evidence of compliance.
Epistemic authority and scope: claimed facts delivered without original transcript/evidence in this projection; source warrant unknown at consumer.
Operational authority: instructions can influence subsequent responses, but do not authorize bypassing code gates.
Behavioral-authority path: see [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance); cross-chat advisory system text.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/memory.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: excludes current chat's memories; enabled state does not guarantee every manager receives them. No lifecycle integration after factual acceptance is established by these routes.

Route ID: [RT-RTE-test-answer](runtime.md#rt-rte-test-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see record for verification SQL/result.
Content/update relation: truth-apt transformation: indeterminate for SQL extraction from answer; subsequent execution is conditional derivation under SQL semantics, not established faithfulness to the answer.
Transition or check target: prior response messages plus result-table names/row counts/columns to verification SQL.
Evaluator/condition and domain: model requested to apply same analysis, never retype values, and return null if unable; DuckDB judges query executability with one repair opportunity.
Activation and timing: after test agent returns, when expected SQL is supplied.
Possible or observed result: data/sql, null or error; failed query adds error feedback for corrected SQL.
Implemented force: query error prompts one revision, successful execution supplies comparator input.
Epistemic authority and scope: executability over fetched tables; no independent semantic fidelity check between natural-language answer and query.
Operational authority: can change reported test result through extracted rows.
Behavioral-authority path: verification output to CLI comparator, computational evaluation, test-run horizon.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/test-agent.service.ts`.
Claim IDs: [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility).
Mismatch marker: none.
Gap/limit: verifier is not the reference-answer oracle; its reconstruction can conceal an incorrect textual answer or misrepresent a correct one.

Route ID: [EPI-RTE-test-comparison](#epi-rte-test-comparison)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [RT-RTE-test-answer](runtime.md#rt-rte-test-answer).
Content/update relation: no content change to the answer; truth-apt transformation: entailed derivation of match/fail from comparison inputs under the implemented comparison rules, conditional on helper behavior.
Transition or check target: extracted actual rows versus rows produced by author-supplied expected SQL, plus structural tool assertions.
Evaluator/condition and domain: deterministic dataframe comparison: selected columns, equal row counts, numeric normalization/rounding, order-insensitive sorting, equality then approximate numeric comparison. Both empty passes before column checks.
Activation and timing: CLI run_test after API verification response.
Possible or observed result: match, approximate match, missing column/row-count/value failure; assertions-only path distinct from data test.
Implemented force: produces bounded test evidence; no production context update by itself.
Epistemic authority and scope: conformity to reference query under configured comparison, not raw response truth, causal mechanism, deployment reliability or transfer.
Operational authority: input to pass/fail reporting below.
Behavioral-authority path: comparator tuple to run_test, enforcing evaluation result, current test.
Evidence source ID and local anchor: SRC-1 `cli/nao_core/commands/test/runner.py`.
Claim IDs: [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility).
Mismatch marker: none.
Gap/limit: expected SQL can encode a wrong business rule; reference uses the same data/execution adapter, not an independent source-truth oracle. Numeric helper/assertion bodies uninspected here.

Route ID: [EPI-RTE-test-comparison](#epi-rte-test-comparison)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [RT-RTE-test-answer](runtime.md#rt-rte-test-answer).
Content/update relation: no content change.
Transition or check target: assertions_passed and data_passed to test passed flag.
Evaluator/condition and domain: boolean conjunction for data-verification path, consuming comparison evidence against test-defined expected rows.
Activation and timing: after comparisons.
Possible or observed result: TestRunResult passed or failed with response/reference/verification detail.
Implemented force: accepting/rejecting this test case, not product release or factual memory admission.
Epistemic authority and scope: acceptance criterion is conjunction of tool assertions and reference-data match; intended use is bounded analytics-example evaluation under selected model/settings/tolerances.
Operational authority: marks evaluation result for operator; no automatic deployment veto shown.
Behavioral-authority path: CLI status/details to operator/report, advisory beyond the test result, test/report horizon.
Evidence source ID and local anchor: SRC-1 `cli/nao_core/commands/test/runner.py`.
Claim IDs: [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility).
Mismatch marker: none.
Gap/limit: this is evidence-consuming test acceptance, not acceptance and integration of a produced ampliative claim.

Route ID: [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see record for findings/patch proposals.
Content/update relation: truth-apt transformation: indeterminate for model diagnoses/root causes; non-truth-apt policy/content update: suggested edit actions. Explicit causal explanations are requested, but no generated instance establishes non-entailment or truth.
Transition or check target: usage/errors/corrections/downvotes/context files to named symptom, rootCause and suggestedAction.
Evaluator/condition and domain: diagnostic model with read-only usage query and context discovery tools; requested substantiation, not causal experiment or reference patch oracle.
Activation and timing: manual/scheduled analysis window, existing findings and expensive-file flags supplied.
Possible or observed result: recorded findings, proposed edits, resolution fingerprints; unobserved here.
Implemented force: collector acknowledges schema-shaped inputs; suggestions enter reconciliation and possible PR creation.
Epistemic authority and scope: candidate diagnosis and improvement proposal; downvotes/errors do not identify the causal culprit alone.
Operational authority: software can retain recommendation and automatically open PR when configured.
Behavioral-authority path: diagnostic model to collector/DB/PR; permissive proposal creation, project analysis horizon; live guidance consumption requires separate admission.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/components/ai/context-recommendations-system-prompt.tsx`.
Claim IDs: [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility).
Mismatch marker: none.
Gap/limit: doctrine requests content-directed diagnosis and verified resolution; reliable criticism and changed future reliance are not established merely by a named rootCause field.

Route ID: [EPI-RTE-finding-reconciliation](#epi-rte-finding-reconciliation)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation).
Content/update relation: no content change to diagnosis; truth-apt transformation: entailed derivation for canonical trigger chat IDs from database membership/resolution, conditional on lookup results.
Transition or check target: claimed chat/target references against project DB membership.
Evaluator/condition and domain: repairRefs chooses target-resolved chat if present, otherwise valid supplied chat, drops unresolved refs and deduplicates.
Activation and timing: after model run, before impact/reconciliation/persistence.
Possible or observed result: repaired/dropped trigger references.
Implemented force: persisted lineage changes; unsupported replay links disappear.
Epistemic authority and scope: identifier resolution only, not evidence that the linked event caused the symptom.
Operational authority: affects impact score and diagnostic replay links consumed by reconciliation/UI.
Behavioral-authority path: reference repair to scoring/actions, enforcing structural lineage, current and retained analysis rounds.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/context-recommendations.reconcile.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: dropping refs can reduce evidence visibility without withdrawing unsupported diagnosis text.

Route ID: [EPI-RTE-finding-reconciliation](#epi-rte-finding-reconciliation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation).
Content/update relation: no content change for disposition; non-truth-apt policy/content update: impact-based prioritization and recommendation lifecycle status.
Transition or check target: findings/fingerprints/impact versus existing, dismissed and resolved sets.
Evaluator/condition and domain: code last-wins deduplication, dismissed suppression, impact floor for new insertions, update existing even below floor, reopen applied finding, resolve only open/unhandled/non-dismissed fingerprints.
Activation and timing: after repaired references and model recording/resolution.
Possible or observed result: insert/update/reopen/resolve actions, or no action.
Implemented force: transaction changes retained recommendation population/status; model resolution is not independently semantically checked by reconciler.
Epistemic authority and scope: significance/administrative status, not accepted root-cause truth or demonstrated patch benefit.
Operational authority: controls later recommendation supply and eligibility for review-request workflow.
Behavioral-authority path: collector → reconciler → DB → subsequent diagnostic prompt and PR selection; enforcing administrative state, cross-run horizon.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/context-recommendations.reconcile.ts`.
Claim IDs: [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility).
Mismatch marker: none.
Gap/limit: fingerprints and counts are model-provided/grouped; impact is friction share plus affected chats, not correctness confidence. Feedback-coverage postprocessing remains unassessed.

Route ID: [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation)
Route function: retention
Architectural status: implemented
Object/candidate ID: see record for recommendation content, prior states and patches.
Content/update relation: no content change from retaining selected proposals.
Transition or check target: reconciliation actions to DB and future diagnostic input; optional edits to disposable branch/PR.
Evaluator/condition and domain: DB transaction/PR eligibility and configured autoCreatePrs; no correct-patch oracle.
Activation and timing: after analysis; optional automatic PR creation before completion.
Possible or observed result: retained findings and optional PR links. Both a reconciliation resolve action and successful automatic PR opening write status applied; that status alone establishes neither a PR nor deployment.
Implemented force: retained diagnostic evidence and review requests; not lifecycle integration of epistemically accepted new theory.
Epistemic authority and scope: proposal status only.
Operational authority: future diagnostic runs see prior/dismissed recommendations; reviewers can choose external admission.
Behavioral-authority path: see cited record; DB/prompt and PR channel, advisory proposals plus permissive PR creation, across analysis runs.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/context-recommendations.service.ts`.
Claim IDs: [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility).
Mismatch marker: none.
Gap/limit: future consumption is wired, not observed content-dependent iteration or improved capacity.

Route ID: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt).
Content/update relation: truth-apt transformation: acquisition/import for supplied project facts, source warrant unknown; non-truth-apt policy/content update: supplied rules/skills.
Transition or check target: synchronized/local/Git context bytes to later prompt/read-tool inputs.
Evaluator/condition and domain: delivery/Git/configuration gates, not an evidence-consuming semantic acceptance criterion.
Activation and timing: initialization/refresh/sync then future agent construction or context reads.
Possible or observed result: changed guidance or delivery failure.
Implemented force: byte admission and selective model supply; human authorship/review unresolved.
Epistemic authority and scope: no endorsement inferred from freshness, commit identity or successful merge.
Operational authority: later model receives changed instructions; no guarantee of compliance or current-manager rebuild.
Behavioral-authority path: see cited records; filesystem/default prompt or override/read results to agent, advisory, subsequent invocations.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/services/context-explorer-git/live-context.service.ts`.
Claim IDs: [RT-CLM-context-readonly](runtime.md#rt-clm-context-readonly).
Mismatch marker: none; read-only is scoped to ordinary write tool, not all admission paths.
Gap/limit: remote review, deployment and subsequent behavioral dependence unobserved. No inspected lifecycle-integration-after-epistemic-acceptance route is established by byte delivery.

Route ID: [RT-RTE-automation-run](runtime.md#rt-rte-automation-run)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see record for required integration calls.
Content/update relation: no content change.
Transition or check target: recorded tool-call names versus configured required integrations.
Evaluator/condition and domain: deterministic missing-name check.
Activation and timing: after automation stream.
Possible or observed result: complete/fail status based on call presence.
Implemented force: completion bookkeeping, not answer truth or undo of already performed effects.
Epistemic authority and scope: recorded call presence only.
Operational authority: changes run status; cannot establish exactly-once external action.
Behavioral-authority path: see record, status to run consumers, enforcing completion classification, run horizon.
Evidence source ID and local anchor: SRC-1 `apps/backend/src/handlers/automation.handler.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: actual remote delivery, scheduler checks and channel-specific assessment remain uninspected.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-analytics-answers](#epi-clm-analytics-answers) | see record | SRC-1 `apps/backend/src/mcp/server.ts`, doctrine/design | SQL-backed analytics intent | [EPI-RTE-query-results](#epi-rte-query-results), [RT-RTE-mcp-chat](runtime.md#rt-rte-mcp-chat) | None supplied | Successful query does not establish interpretation; model can compose unverified text | Query evidence is available and reusable; answer faithfulness is not guaranteed | Ordinary chat has no reference oracle; governed-metric compiler fidelity unresolved |
| [EPI-CLM-reliability-visibility](#epi-clm-reliability-visibility) | see record | SRC-1 `README.md`, doctrine/design | Example tests, versioned context, feedback-directed improvement | [EPI-RTE-test-comparison](#epi-rte-test-comparison), [RT-RTE-test-answer](runtime.md#rt-rte-test-answer), [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation) | None supplied | Expected-query quality, extractor fidelity and case coverage bound evaluation; feedback diagnoses lack causal intervention | Implemented bounded evaluation and feedback-to-proposal routes | No observed reliability increase, successful patch admission or transfer benefit |
| [RT-CLM-context-readonly](runtime.md#rt-clm-context-readonly) | see record | SRC-1 `apps/backend/src/agents/tools/write.ts`, doctrine/design and supplied implementation | Scoped write-tool contract | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and supplied write gate | None supplied | Separate sync/Git/editor paths admit changes | Ordinary writable-output restriction coexists with project-context replacement | No mismatch under scoped reading; universal context immutability would be false |

## Bounded conclusion

nao acquires query results and project context, exposes cached evidence and generates analytics answers. The query path retains full rows separately from its limited model-visible display, provides paging, warns about query limits and suppresses stale output. These mechanisms preserve selected values and lineage, not the correctness of the original dataset, intended metric, or model explanation. Local SQL affords derivation from inputs under engine/query semantics; no supplied concrete run establishes a warranted new external-world proposition. See [EPI-RTE-query-results](#epi-rte-query-results).

User-memory extraction separates factual profile from behavior directives. It requests persistent-intent judgment, but receives only recent truncated conversation text. Software normalizes candidates, checks emptiness and supersession membership, then stores them. Profile truth is not independently accepted. Supersession/edit/delete can change later reliance by changing the active set; reload projects only category/content, not original evidence. Default system-prompt delivery gives these records advisory behavioral force across chats, while complete overrides and disabled memory can omit them. This is automatic trace-fed guidance revision, not evidence of improved capacity or parametric training. See [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-memory-admission](#epi-rte-memory-admission).

The test path has a real, bounded evidence-consuming acceptance decision: actual extracted rows must match author-supplied expected-query rows under comparison rules, and tool assertions must pass. The intended use is example-level analytics evaluation, not factual endorsement of all generated prose or a universal deployment gate. SQL-error feedback allows a verifier-query repair, but does not independently test whether that query encodes the answer faithfully. No benchmark was run. See [EPI-RTE-test-comparison](#epi-rte-test-comparison).

Context recommendations request explanations naming symptoms, causes and fixes. They inspect representations of nao's own usage and context, and can retain revisions/resolutions across diagnostic runs. Identifier repair and impact reconciliation are operative structural checks; neither establishes the truth of a root cause. Dismissal, resolution, reopening and PR creation change administrative reliance, not demonstrated epistemic acceptance. Status applied has two producers: reconciliation resolution and successful automatic PR opening. It alone establishes neither a PR nor deployment. PR opening is not live guidance admission; subsequent context delivery is a separate software path. Consequently, feedback-to-proposal and context-to-agent paths are wired, but exercised self-improvement would additionally require evidence-responsive live change and subsequent operation causally depending on it. Successful improvement needs outcomes beyond that. See [EPI-RTE-finding-reconciliation](#epi-rte-finding-reconciliation), [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

The diagnosis schema and prompt support localized causal-candidate formulation and requested content-directed criticism. They do not supply an observed formulated theory, content-dependent consumption, blame-correcting revision or retained criticism shaping a next round. These four theory-builder conditions remain independently unestablished for actual theory instances in the inspected path; capacity to collect and resupply diagnoses is established separately. Reflection has a wired usage/context self-representation and a proposal channel capable of eventual guidance change, but exercised two-way dependence is unobserved. Automation of internal analysis and proposal steps does not establish autonomous completion of external review/admission. Learning, reflection, autonomy, theory building and self-improvement are not one verdict.

Provider model components remain opaque distributed-parametric state. The supplied [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model), [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model), [RT-CMP-verification-model](runtime.md#rt-cmp-verification-model) and the additional [EPI-CMP-memory-extractor](#epi-cmp-memory-extractor) establish nao-side calls and configuration, not exact weight pins, provider-side training or stable alias behavior. Uninspected shipped skills, compiler/providers, feedback postprocessing and channel/asset operations prevent a system-complete negative about checking or knowledge production. No single epistemic score follows.

## Shared records

### Components

#### EPI-CMP-memory-extractor
Label: Memory extractor model

Distinct from supplied agent/compaction/verification roles: this component supplies MemoryExtractorLLM and its extraction judgment, even if a configured model ID happens to coincide. Source-native identity: resolved annotation/other model passed to MemoryExtractorLLM. Form: distributed-parametric; substrate: provider-hosted weights. Parameters changing during operation: no update step in inspected extraction/service path; provider internals uninspected. Exact version pinned: not established by configured provider/modelId. Mutable endpoint resolving to another model: shared resolver allows provider/configurable endpoint behavior; actual fixity uninspected. SRC-1 `apps/backend/src/services/memory.ts`, `apps/backend/src/agents/memory/memory-extractor-llm.ts`; shared resolver uncertainty see [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model).

> const pinned = await resolveDefaultModelSelection(opts.projectId, 'other');
> --- `apps/backend/src/services/memory.ts`

> const extractor = new MemoryExtractorLLM(model);
> const extractorResult = await extractor.extract(existingMemories, opts.messages);
> --- `apps/backend/src/services/memory.ts`

### Operative objects

#### EPI-OBJ-query-results
Label: Query results

Part of: [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context)

Source-native identity: ToolContext.queryResults entries and execute_sql outputs, with query ID, columns and data. Form: symbolic structured tabular values with fixed SQL/cache consumers; model-rendered text is an interpreted presentation of this same evidence. Substrate: process map, retained tool results and direct-MCP query-data cache. Different from the container's identities/grants; these values are the material evidence part. SRC-1 `apps/backend/src/agents/tools/execute-sql.ts`, `apps/backend/src/mcp/tools/context-layer.ts`.

> context.queryResults.set(id, { columns, data });
> --- `apps/backend/src/agents/tools/execute-sql.ts`

> await upsertMcpQueryData(queryId, callLogId, ctx.projectId, output.columns, output.data, {
> sourceChatId: validatedSourceChat ?? null,
> });
> --- `apps/backend/src/mcp/tools/context-layer.ts`

#### EPI-OBJ-personal-fact
Label: Personal fact

Source-native identity: memories category personal_fact, from user_profile. Form: natural-language statement about user; substrate: DB row and projected system-prompt text. Distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): stored candidate source, not assembled invocation string; no supplied dedicated memory object. Factual scope is user identity/background, not warehouse facts. SRC-1 `apps/backend/src/services/memory.ts`, `apps/backend/src/components/ai/memory-system-prompt.tsx`.

> ...this._toDbMemories(profile, 'personal_fact', opts.userId, opts.chatId),
> --- `apps/backend/src/services/memory.ts`

> Extract when the user shares identity or background information such as: their name, role, job title,
> company, team, location, timezone, language, domain expertise, or similar personal details.
> --- `apps/backend/src/components/ai/memory-system-prompt.tsx`

#### EPI-OBJ-global-rule
Label: Global rule

Source-native identity: memories category global_rule, from user_instructions. Form: natural-language directive; substrate: DB row and system-prompt projection. Distinct from profile because it requests behavior, not user-fact truth. Distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): retained input, not prompt container; no supplied dedicated memory object. SRC-1 `apps/backend/src/services/memory.ts`, `apps/backend/src/components/ai/memory-system-prompt.tsx`.

> ...this._toDbMemories(instructions, 'global_rule', opts.userId, opts.chatId),
> --- `apps/backend/src/services/memory.ts`

> Without such signals, assume the instruction applies only to the current conversation.
> --- `apps/backend/src/components/ai/memory-system-prompt.tsx`

### Routes

#### EPI-RTE-query-results
Label: Query evidence delivery

Distinct identity: this record spans the SQL evidence function in [RT-RTE-web-chat](runtime.md#rt-rte-web-chat) and direct host-driven MCP, which the supplied [RT-RTE-mcp-chat](runtime.md#rt-rte-mcp-chat) distinguishes from its enclosed chat. It is not wholly contained in either supplied route. Those records remain valid invocation containers; this shared adapter function is not a duplicate whole invocation. Endpoints: execute_sql/execute_semantic_query → executeQuery → local/admin/warehouse adapter → query map → rendered tool result; direct MCP additionally upserts query data. Owner: model or MCP host chooses query; code selects execution/gates; database executes. Context/state/action effects: fills/replaces query cache, can update persisted SQL parts under same ID, then supplies model/host/asset evidence. Semantic compilation is called, not independently audited.

- Immediate return: data/columns/query ID or error, model rendering or MCP structured/text output.
- Later read-back: read_query_result uses cached/current-or-earlier-chat query ID; stored SQL parts can be replaced; asset cache supports subsequent use.
- Delegated visibility: database gets effective SQL/enforcement inputs; foreground model receives at most default 40 displayed rows; MCP receives formatted full output in inspected registration.
- Selection predicate: selected query/database, tool grants, optional query ID and paging offset/limit; semantic adapter sets compiledBySemanticLayer.
- Invalidation or expiry: rerun replaces values under same ID; semantic-query raw editing rejected; superseded outputs suppress old bodies. Cache expiry uninspected.
- Activation or effect: wired query dispatch, cache mutation and selective evidence delivery; no execution supplied.
- Evidence limits: warehouse/DuckDB implementation, complete permissions, semantic compiler and source truth uninspected; adapter success is not answer correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SQL access admission is software: proposer is model/host, code can reject writes/passthroughs, no per-content human approval is required by this adapter; user/project settings and external database permissions bound grants. Mode: open query tool, no expected answer oracle. SRC-1 `apps/backend/src/agents/tools/execute-sql.ts`, `apps/backend/src/agents/tools/execute-semantic-query.ts`, `apps/backend/src/components/tool-outputs/execute-sql.tsx`, `apps/backend/src/agents/tools/read-query-result.ts`, `apps/backend/src/mcp/tools/context-layer.ts`.

> if (!writePermEnabled && !(await isReadOnlySqlQuery(effectiveSql))) {
> --- `apps/backend/src/agents/tools/execute-sql.ts`

> const compiled = await compileSemanticQuery(query, context);
> --- `apps/backend/src/agents/tools/execute-semantic-query.ts`

> const MAX_ROWS = 40;
> --- `apps/backend/src/components/tool-outputs/execute-sql.tsx`

> const visibleRows = isTruncated ? output.data.slice(0, maxRows) : output.data;
> --- `apps/backend/src/components/tool-outputs/execute-sql.tsx`

> const data = stored.data.slice(offset, offset + limit);
> --- `apps/backend/src/agents/tools/read-query-result.ts`

> Stale result: query {output.id} was re-run later in this conversation. Refer to the latest execute_sql
> result with this query id (or call read_query_result) for the current SQL and rows.
> --- `apps/backend/src/components/tool-outputs/execute-sql.tsx`

> Query ${queryId} is a semantic query and cannot be edited as SQL. Call execute_semantic_query again with the adjusted metrics, group_by or where.
> --- `apps/backend/src/agents/tools/execute-sql.ts`

#### EPI-RTE-memory-extraction
Label: Memory extraction

Distinct from [RT-RTE-web-chat](runtime.md#rt-rte-web-chat): asynchronous extraction called on the user-message path, with separate model/output/consumer, not analytics response production or transcript persistence. Endpoint/progression: safeScheduleMemoryExtraction → enabled/model checks → active memories/recent text → extractor model → output to admission. Owner: nao service schedules; extractor model proposes profile/directive candidates. Context/state/action effects: structured candidates, subsequent memory writes; not weight updates.

- Immediate return: scheduling is asynchronous; extraction returns schema-shaped output/usage or undefined.
- Later read-back: persisted candidates can be supplied to future extraction alongside new conversation; admission/prompt supply is a separate function.
- Delegated visibility: latest 17 UI messages, only user/assistant joined text, middle-truncated to 1,250 characters or 2,000 for last user text, plus existing memories.
- Selection predicate: memory enabled, resolved model, nonempty conversation, last user text minimum length 3.
- Invalidation or expiry: null/no candidate or errors end this attempt; supersession output can replace active memories through admission.
- Activation or effect: model generation and automatic admission are wired; factual accuracy and behavioral change unobserved.
- Evidence limits: prompt requests full-conversation analysis but delivery is bounded; no profile truth oracle or observed candidate instance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer/evaluator: extractor model applying permanence/profile/existing-memory guidance; software shapes input/output. Mode: open recent-conversation extraction; no expected-answer reference. Human supplies source conversation, not per-item approval. Guidance persists in shipped extraction prompt; candidates persist only after admission. SRC-1 `apps/backend/src/agents/memory/memory-extractor-llm.ts`, `apps/backend/src/components/ai/memory-system-prompt.tsx`.

> const CONVERSATION_MESSAGE_LIMIT = 17;
> const MESSAGE_CHAR_LIMIT = 1_250;
> const LAST_USER_MESSAGE_CHAR_LIMIT = 2_000;
> --- `apps/backend/src/agents/memory/memory-extractor-llm.ts`

> const recent = uiMessages.slice(-CONVERSATION_MESSAGE_LIMIT);
> --- `apps/backend/src/agents/memory/memory-extractor-llm.ts`

> const text = truncateMiddle(joinAllTextParts(message), maxLength);
> --- `apps/backend/src/agents/memory/memory-extractor-llm.ts`

> output: Output.object({ schema: ExtractorOutputSchema }),
> --- `apps/backend/src/agents/memory/memory-extractor-llm.ts`

> Before extracting anything, carefully read <Bold>all</Bold> previous user and assistant messages. The full
> conversation context determines whether something is a lasting preference or just a one-off request. Most
> conversations will NOT produce any memory changes — that is the expected default.
> --- `apps/backend/src/components/ai/memory-system-prompt.tsx`

#### EPI-RTE-memory-admission
Label: Memory admission and withdrawal

Distinct from supplied chat/prompt records: the normalization/DB active-set/prompt-projection mechanism, not the whole prompt or response retention. Endpoint/progression: extracted fields → normalization/empty and ID filter → upsert/supersede transaction → active query → category/content projection → default prompt builder. Explicit edit/delete queries alter owned rows. Owner: model proposes candidates/supersession; software decides structural admission and reload; user supplies explicit edits when caller invokes edit/delete. Context/state/action effects: persistent guidance, withdrawal and replacement without independent profile-truth review.

- Immediate return: inserted/superseded counts; edit/delete returns affected row or null; reload returns projected memories or empty on failure/disabled state.
- Later read-back: active user memories supplied to extractor and default agent prompt; current chat can be excluded from prompt query.
- Delegated visibility: default prompt receives category/content only, not source chat or provenance fields from DB query.
- Selection predicate: enabled user/project, userId and active supersededBy null; optional excludeChatId; normalized nonempty content and valid supersession membership.
- Invalidation or expiry: supersededBy excludes old row; explicit deletion removes row; edit changes content; no automatic factual expiry established.
- Activation or effect: persistent text and selected prompt supply wired; no observed model compliance, improvement or semantic rollback.
- Evidence limits: UI/API authorization and races uninspected; model permanence request is not independently checked; overrides can omit standard guidance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposed change: extraction result or explicit edit/delete. Software admits qualifying extracted text without per-item human approval. Rejection: empty/invalid supersession candidates dropped; enabled flag can suppress extraction/supply. Recovery: transactional persistence; superseded rows retained but no dedicated restore procedure inspected. Instructions shape proposal as above; resulting English prose persists. Mode: persistent user guidance, no reference-answer oracle. SRC-1 `apps/backend/src/services/memory.ts`, `apps/backend/src/queries/memory.ts`; later default/override authority see [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance).

> const normalized = content.trim().replace(/\s+/g, ' ');
> --- `apps/backend/src/services/memory.ts`

> return /[.!?]$/.test(normalized) ? normalized : `${normalized}.`;
> --- `apps/backend/src/services/memory.ts`

> ].filter(({ supersedesId }) => (supersedesId ? existingIds.has(supersedesId) : true));
> --- `apps/backend/src/services/memory.ts`

> When <Code>supersedes_id</Code> is set, the old memory will be deleted and replaced by the new one. Use this
> when:
> --- `apps/backend/src/components/ai/memory-system-prompt.tsx`

> .set({ supersededBy: newMemoryId })
> --- `apps/backend/src/queries/memory.ts`

> isNull(s.memories.supersededBy),
> --- `apps/backend/src/queries/memory.ts`

> return memories.map((memory) => ({
> category: memory.category,
> content: memory.content,
> }));
> --- `apps/backend/src/services/memory.ts`

> .where(and(eq(s.memories.id, memoryId), eq(s.memories.userId, userId)))
> --- `apps/backend/src/queries/memory.ts:96-103`

#### EPI-RTE-test-comparison
Label: Test data comparison

Part of: [RT-RTE-test-answer](runtime.md#rt-rte-test-answer)

Endpoint/progression: author expected SQL → test API executeQuery expectedData/columns and runVerification actualData → CLI check_dataframe/evaluate_assertions → passed flag/details. Owner: test author chooses problem/reference/assertions; verifier model reconstructs answer SQL; deterministic comparator judges conformity. Context/state/action effects: bounded evaluation evidence and status; no automatic live guidance update.

- Immediate return: comparator tuple and TestRunResult passed/message/details with expected and actual data, reference and verification SQL.
- Later read-back: uninspected — runner contains report saving, but later model consumption of reports was not traced; test-agent path does not persist chat.
- Delegated visibility: verifier sees original question, response messages and table inventory; comparator sees actual and expected rows, columns and configured tolerances.
- Selection predicate: supplied expected SQL activates data path; assertions-only cases can evaluate call structure without data oracle.
- Invalidation or expiry: missing/error verification fails; row/column/value mismatch fails; subsequent reruns create new results, not semantic rollback of production behavior.
- Activation or effect: pass flag is conjunction of assertions/data checks on data path; no execution supplied.
- Evidence limits: expectation quality, numeric helper, assertion bodies, model extraction faithfulness and benchmark coverage unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode: bounded test example. Proposer: analytics agent; oracle provider: test author SQL executed against configured data, not verifier model. Veto: comparison rejects this test result; user may revise reference/settings, but no inspected automatic production-admission gate follows. SRC-1 `apps/backend/src/routes/test.ts`, `apps/backend/src/services/test-agent-verification.ts`, `apps/backend/src/services/test-agent.service.ts`, `cli/nao_core/commands/test/runner.py`.

> const { data: expectedData, columns: expectedColumns } = await executeQuery(
> { sql_query: sql, database_id: databaseId },
> toolContext,
> );
> --- `apps/backend/src/routes/test.ts`

> - Apply the same filters, aggregations and ordering as the answer you gave.
> --- `apps/backend/src/services/test-agent-verification.ts`

> if actual.empty and expected.empty:
> return True, "both empty", None
> --- `cli/nao_core/commands/test/runner.py`

> actual = actual.sort_values(by=sorted_cols).reset_index(drop=True)
> expected = expected.sort_values(by=sorted_cols).reset_index(drop=True)
> --- `cli/nao_core/commands/test/runner.py`

> actual = round_numeric(actual, decimals=decimals)
> expected = round_numeric(expected, decimals=decimals)
> --- `cli/nao_core/commands/test/runner.py`

> if not np.allclose(
> actual_series.to_numpy(),
> expected_series.to_numpy(),
> rtol=rtol,
> atol=atol,
> equal_nan=True,
> ):
> --- `cli/nao_core/commands/test/runner.py`

> passed = assertions_passed and data_passed
> --- `cli/nao_core/commands/test/runner.py`

#### EPI-RTE-finding-reconciliation
Label: Finding reconciliation

Part of: [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation)

Endpoint/progression: recorded findings/resolution fingerprints → project DB trigger lookup/repair → impact and fingerprint reconciliation → transaction actions; later analysis loads retained recommendations/dismissals. Owner: diagnostic model proposes findings/resolutions; code repairs/selects lifecycle actions. Context/state/action effects: lineage, ranking, retention, reopening and administrative withdrawal. Resolve actions write status applied without opening a PR; the container's separate automatic PR path also writes applied after PR creation. The shared status alone establishes neither PR creation nor deployment. Different from container's model diagnosis/PR work: this part checks identifiers/selection, not root-cause truth.

- Immediate return: repaired finding refs and insert/update/resolve actions, committed by run service.
- Later read-back: existing reconcilable recommendations and dismissed fingerprints supplied to subsequent runs.
- Delegated visibility: reconciler gets model content, DB-resolved IDs, totals and prior statuses; model recorder/resolve calls get ok acknowledgement.
- Selection predicate: file/subject fingerprint; last recording wins; dismissed set suppresses; new finding impact floor; existing updates bypass new-insert floor; only open unresolved-by-update findings resolve.
- Invalidation or expiry: invalid refs dropped; dismissed suppressed; applied can reopen; resolve changes open finding status. No semantic automatic retraction criterion established.
- Activation or effect: structural lineage and administrative disposition wired; no observed verified correction or quality change.
- Evidence limits: impact is model-provided insight counts/friction totals and affected chats; no causal proof; feedback-coverage postprocessor can additionally affect population and is uninspected here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode: bounded diagnostic window. Proposer/evaluator: model requested to substantiate diagnosis and verify resolution, with no correct-patch oracle; computational decider: reconciliation. Human dismissal can veto repeat recording through stored fingerprint; per-candidate human review is not required before DB retention. Proposal shaped by dedicated diagnostic guidance treating context as audit subject, not authoritative instructions. RootCause prose and suggested edits persist; same finding can be updated in later runs. Guidance-to-patch admission/recovery is separately supplied by runtime; administrative selection does not prove a formulated theory was criticized and revised correctly. SRC-1 `apps/backend/src/services/context-recommendations.reconcile.ts`, `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/agents/tools/record-recommendation.ts`, `apps/backend/src/components/ai/context-recommendations-system-prompt.tsx`.

> rootCause: z
> .string()
> .describe(
> 'One sentence explaining the exact sequence that led to this finding (what was read/not read, what mistake followed).',
> ),
> --- `apps/backend/src/agents/tools/record-recommendation.ts`

> resolvedFingerprints.push(fingerprint);
> --- `apps/backend/src/agents/tools/record-recommendation.ts`

> const chatId = resolvedChatId ?? (validChatIds.has(ref.chatId) ? ref.chatId : undefined);
> --- `apps/backend/src/services/context-recommendations.reconcile.ts`

> const impactScore = Math.round(failureShare * 100) + affectedChats * 5;
> --- `apps/backend/src/services/context-recommendations.reconcile.ts`

> if (dismissed.has(fingerprint)) {
> continue;
> }
> --- `apps/backend/src/services/context-recommendations.reconcile.ts`

> } else if (impactScore >= impactFloor) {
> --- `apps/backend/src/services/context-recommendations.reconcile.ts`

> if (current && current.status === 'open') {
> actions.push({ kind: 'resolve', id: current.id });
> }
> --- `apps/backend/src/services/context-recommendations.reconcile.ts`

> await applyActions({ projectId, runId: run.id, model, actions, existing, fixCollector }, tx);
> --- `apps/backend/src/services/context-recommendations.service.ts`

> } else if (action.kind === 'resolve') {
> await crQueries.updateRecommendation(
> action.id,
> { status: 'applied', statusChangedAt: new Date() },
> executor,
> );
> }
> --- `apps/backend/src/services/context-recommendations.service.ts`

The separate automatic PR status producer is evidenced in [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation); direct correction reads of SRC-1 `apps/backend/src/services/context-recommendations.service.ts` and `apps/backend/src/services/context-pr.service.ts` confirm both assignments at the frozen revision.

### Claims

#### EPI-CLM-analytics-answers
Label: SQL backed analytics answers

Claimed operation: MCP server instructions describe nao as answering analytics questions backed by SQL on connected sources. Distinct from supplied read-only-context claim; closest supplied route [RT-RTE-mcp-chat](runtime.md#rt-rte-mcp-chat) implements answer delivery, not a truth guarantee. SRC-1 `apps/backend/src/mcp/server.ts`, doctrine/design.

> 'nao answers analytics questions backed by SQL queries on the connected data sources. ' +
> --- `apps/backend/src/mcp/server.ts`

#### EPI-CLM-reliability-visibility
Label: Agent reliability visibility

Claimed operation: README advertises unit-testing performance, versioning context, tracking usage and feedback-directed improvement. Distinct from supplied scoped read-only claim; [RT-RTE-test-answer](runtime.md#rt-rte-test-answer) and [RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation) are corresponding routes, not observed support for successful improvement. SRC-1 `README.md`, doctrine/design.

> - 🕵🏻‍♀️ **Agent Reliability Visibility** — Unit test your agent performance before deploying it to users. Version the context and track the performance of your agent over time. Get users feedbacks to improve the agent and track their usage.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
