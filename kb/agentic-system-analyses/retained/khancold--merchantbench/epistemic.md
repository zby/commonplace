---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MerchantBench epistemic routes: simulated feedback, report import, model proposals, scratchpad reliance and terminal wealth evaluation."
run-id: AAS-2026-10-15-merchantbench-d2f4d78dbe37-01
reviewed-boundary: d9e5bd7519ab100193c21778aecfb59e30f24651
---

# MerchantBench epistemic report

## Source-and-claim boundary

The question is what the shipped store benchmark lets an agent know, propose, retain and act upon, and what its checks actually license. The functional boundary and external exclusions are those of the [boundary](boundary.md#boundary-and-evidence); the sole source is SRC-1 in its [Source register](boundary.md#source-register). All added inspection below is implementation or attributed doctrine/design at that revision. There is no observed-run or causal-experiment evidence. Source inspection did not execute MerchantBench, its tests, models or examples.

The material routes include scenario guidance, current simulated evidence, private-report import interfaces, model proposals, action admission, scratchpad retention and recall, context removal, outcome measurement and alternate consumers. Imported reports differ from simulator-derived facts: a publication-date filename does not authenticate a report's claims. Likewise, passing a write-size check is not accepting a strategy as true. The consequential public evaluation claim is [EPI-CLM-horizon-evaluation](#epi-clm-horizon-evaluation). No separate claim that the scratchpad contains accepted knowledge is established by its tool description.

### Coverage and unresolved evidence

Direct inspection means source read in this job; supplied means the runtime's source account, not independent execution. Registry coverage inventories exposed operations, not a claim to have audited every handler equation.

| Entry point or operation | Source path at SRC-1 | Coverage and records, or limit and conclusion prevented |
| --- | --- | --- |
| Server, worker, model CLI, batch and evaluation entry points | `env/run.py`, `env/web/run_worker.py`, `env/web/routes_agent.py`, `agent/baselines/react_160k_compact_30k.py`, `scripts/run_batch.py`, `eval/run_eval.py` | Direct entry-point/dispatch searches agree with supplied [RT-RTE-react-loop](runtime.md#rt-rte-react-loop), [RT-RTE-act-gate](runtime.md#rt-rte-act-gate) and [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval). Hook/recovery internals otherwise supplied; not an independent crash-consistency audit. |
| Registered tool surface, grants and dispatch | `env/tools/registry.py`, `env/tools/dispatch.py`, `env/tools/observation.py` | Direct registry entries, lookup/filter helpers, schema validator, dispatch and two appended observation/self-discovery tools. [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), [RT-BAP-handler-binding](runtime.md#rt-bap-handler-binding). No extra model-facing semantic acceptance operation found in this inspected registry. |
| Brief, observation, get_store_snapshot, get_observation, list_tools, query_platform_rules | `env/tools/observation.py`, `env/tools/tools.py` | Direct snapshot/text and appended tools; brief delivery supplied by [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief), [RT-BAP-brief-guidance](runtime.md#rt-bap-brief-guidance). Added [EPI-RTE-observation-render](#epi-rte-observation-render). Individual rating/event equations not all inspected; prevents certifying every reported fact. |
| get_daily_report and notice suppression | `env/data/daily_reports.py`, `env/tools/tools.py` | Direct reader, date selection, result and persisted read cursor: [EPI-RTE-report-import](#epi-rte-report-import). Actual private Markdown unavailable; truth and production of its opportunity signals not determinable. |
| query_cash_pipeline | `env/tools/tools.py` | Direct full handler: [EPI-RTE-cash-pipeline](#epi-rte-cash-pipeline). Distinguishes observed receivables from predicted proceeds. |
| market_brief, hot_search_terms; search_products, get_product_detail, get_supplier_profile, list_supplier_products | `env/tools/registry.py`, `env/tools/tools.py` | Direct schema/handler binding inventory, not full handler/data-loader inspection. Public-field and historical-window restrictions are registry design here. Hidden-signal exclusion and every ranking/market calculation remain unverified in this member; no system-complete negative about information leakage. |
| review_my_listings, query_my_listings, query_balance, query_my_orders, query_open_orders, query_order_updates, query_order_detail, query_supply_chain_anomalies, query_store_performance, query_product_sales_stats | `env/tools/registry.py`, `env/tools/tools.py`, `env/tools/observation.py` | Direct registry inventory; anomaly wrapper inspected. Remaining handler equations not fully inspected. They expose additional symbolic diagnostics, not evidence of an expected-action oracle; their correctness and completeness remain unassessed. |
| list_product, delist_product, adjust_price, end_of_step | `env/tools/registry.py`, `env/tools/dispatch.py`, `env/tools/tools.py` | Direct bindings/dispatch/EOS; handler business checks and hook timing supplied by [RT-RTE-act-gate](runtime.md#rt-rte-act-gate). Partial success and later corrective actions are not semantic acceptance or universal rollback. |
| write_memory_doc, read_memory_doc, context trimming and argument repair | `env/tools/tools.py`, `agent/baselines/react_160k_compact_30k.py` | Direct memory handlers/history, request sanitizer and suffix trimmer; [EPI-RTE-memory-document](#epi-rte-memory-document), [RT-RTE-context-trim](runtime.md#rt-rte-context-trim). No actual saved candidate or subsequent model reliance supplied. |
| Hosted scoring, result return and cleanup | `eval/scoring.py`, `eval/run_eval.py` | Direct full metric function and result/cleanup consumer: [EPI-RTE-wealth-metric](#epi-rte-wealth-metric). No benchmark results or varied-component comparisons available. |
| Rule-based, auto-seed, human and manual drivers | `agent/baselines/rule_based.py`, `agent/baselines/auto_seed.py`, `env/web/templates/_human_playground_script.html`, `env/web/runner.py` | Supplied [RT-RTE-other-clients](runtime.md#rt-rte-other-clients). Their policy details not independently assessed; no comparative skill inference. |
| Hermes launch, copied skills, provider parameters and arbitrary submitted images | `env/web/runner.py`, `agent/baselines/react_160k_compact_30k.py`, `eval/run_eval.py` | Supplied [RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch), [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model), [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval). External implementations uninspected/outside frozen source; internal learning, criticism and skill acceptance cannot be inferred. |

These gaps limit completeness, not the positive findings below. No supplied fact requires supersession. The supplied runtime already distinguishes source wiring from operation and notes the default memory-denial documentation discrepancy; nothing here reinstates that denial. Independent route conclusions do not imply a system-wide epistemic status.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief) | Platform-rule descriptions are truth-apt relative to scenario; merchant goals are prescriptions | see record | see record | Delivery is not compliance; all text-rule fidelity not independently audited. |
| [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry) | Schema descriptions assert available behavior; callable bindings are symbolic authority | see record | see record | Operational permission differs from evidence that an action is wise. |
| [EPI-OBJ-store-snapshot](#epi-obj-store-snapshot) | Current cash, order totals, event counts, rating and report availability within one run/window | see record | see record | Truth scope is simulation state, not external commerce. |
| [EPI-OBJ-daily-report](#epi-obj-daily-report) | Report-specific market claims cannot be individuated without private content | see record | see record | Acquisition interface is inspectable; source warrant unknown. |
| [EPI-OBJ-memory-doc](#epi-obj-memory-doc) | Possible notes or claims mixed with plans; no concrete content supplied | see record | see record | Content preservation on file I/O does not establish semantic warrant. |
| [EPI-OBJ-eval-metrics](#epi-obj-eval-metrics) | Terminal wealth, profit, survival and rating in a seeded simulated run | see record | see record | No actual outcome artifact supplied; component effectiveness not entailed. |
| [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model) | Parametric content inaccessible; returned assistant claims, if any, not individuated | see record | see record | No local weight update wired; version is not immutably pinned; provider changes uninspected. |

Model tool choices and deterministic/human store actions can be non-truth-apt policy decisions. They must not be recast automatically as theories. Cash-pipeline and other diagnostic results are transient symbolic responses, not necessarily retained knowledge; [EPI-RTE-cash-pipeline](#epi-rte-cash-pipeline) owns that finer transformation.

## Authority-route ledger

Fields owned by declaring records are referenced rather than re-declared. Each route remains independent of any later evidence of benefit.

Route ID: [EPI-RTE-observation-render](#epi-rte-observation-render)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-store-snapshot](#epi-obj-store-snapshot)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: see record
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: [EPI-CLM-horizon-evaluation](#epi-clm-horizon-evaluation)
Mismatch marker or none: none
Gap/limit: see record

Route ID: [EPI-RTE-report-import](#epi-rte-report-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-daily-report](#epi-obj-daily-report)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: see record
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: source warrant unknown; see record

Route ID: [EPI-RTE-cash-pipeline](#epi-rte-cash-pipeline)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-store-snapshot](#epi-obj-store-snapshot)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: see record
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see record

Route ID: [RT-RTE-react-loop](runtime.md#rt-rte-react-loop)
Route function: other — model proposal and operational feedback
Architectural status: implemented
Object/candidate ID: [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: No recorded claim acceptance follows from proposal generation; other fields see record.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: [EPI-CLM-horizon-evaluation](#epi-clm-horizon-evaluation)
Mismatch marker or none: none
Gap/limit: No concrete assistant proposition supplied. Import, reshaping, derivation and non-entailed conjecture remain distinguishable only with actual input/output content. Pure action choices need not be truth-apt at all.

Route ID: [RT-RTE-act-gate](runtime.md#rt-rte-act-gate)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry)
Content/update relation: non-truth-apt policy/content update: permitted store operations
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: Protocol/business validity, not strategy truth or optimality; see record.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: [RT-CLM-http-controls](runtime.md#rt-clm-http-controls)
Mismatch marker or none: none
Gap/limit: This ledger row is the execution consequence, not a merged semantic check/acceptance phase. Validator implementation inspected directly at SRC-1, `env/tools/dispatch.py`; gate details see record.

Route ID: [EPI-RTE-memory-document](#epi-rte-memory-document)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-doc](#epi-obj-memory-doc)
Content/update relation: no content change
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: Admission of bytes only, not evidence-consuming acceptance of a truth-apt claim; see record.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see record

Route ID: [EPI-RTE-memory-document](#epi-rte-memory-document)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-doc](#epi-obj-memory-doc)
Content/update relation: no content change
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: see record
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: File retention and requested recall are distinct from lifecycle integration after acceptance. No such acceptance is established in this handler.

Route ID: [RT-RTE-context-trim](runtime.md#rt-rte-context-trim)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-doc](#epi-obj-memory-doc)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: Suffix selection grants no new warrant; see record.
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: This classification covers code deletion of old turns, not the model's optional memory rewrite. That rewrite's semantic relation is indeterminate without content. Argument sanitization can replace invalid historical call arguments with an error wrapper; it does not repair the original decision's truth.

Route ID: [EPI-RTE-wealth-metric](#epi-rte-wealth-metric)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-eval-metrics](#epi-obj-eval-metrics)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see record
Evaluator/condition and domain: see record
Activation and timing: see record
Possible or observed result: see record
Implemented force: see record
Epistemic authority and scope: see record
Operational authority: behavior permitted, blocked, or changed: see record
Behavioral-authority path: consumer, channel, force, horizon: see record
Evidence source ID and local anchor: see record
Claim IDs or none: [EPI-CLM-horizon-evaluation](#epi-clm-horizon-evaluation)
Mismatch marker or none: Outcome measurement is not a content-directed criticism or successor-selection gate.
Gap/limit: see record

The alternate drivers and external launch profiles remain covered by [RT-RTE-other-clients](runtime.md#rt-rte-other-clients) and [RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch), not a second semantic evaluator. Setup cleanup prevents a failed profile from being installed; hosted container cleanup removes runtime resources, not false claims from an accepted knowledge store. Their external consumers prevent inferring a complete knowledge lifecycle from launch code.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-horizon-evaluation](#epi-clm-horizon-evaluation) | see record | see record | see record | [RT-RTE-react-loop](runtime.md#rt-rte-react-loop), [EPI-RTE-observation-render](#epi-rte-observation-render), [EPI-RTE-wealth-metric](#epi-rte-wealth-metric) | see record | see record | see record | see record |
| [RT-CLM-http-controls](runtime.md#rt-clm-http-controls) | see record | see record | see record | [RT-RTE-act-gate](runtime.md#rt-rte-act-gate) | see record | see record | see record | These are conditional protocol controls; they do not establish factual validation of memory or agent beliefs. |

## Bounded conclusion

MerchantBench implements an evidence/action loop with delayed simulated consequences, not an expected-answer examination. Its observation renderer supplies scoped facts about the current store; its cash pipeline derives summaries of known orders while explicitly withholding guarantees about future receipts. These conclusions are code-grounded in [EPI-RTE-observation-render](#epi-rte-observation-render) and [EPI-RTE-cash-pipeline](#epi-rte-cash-pipeline), conditional on the simulator/database premises. Their truth scope is the simulation, not a validated model of real commerce.

The private daily report route acquires text verbatim and labels it with current publication and preceding data dates. It does not inspect the text to establish those dates or endorse its market claims. The date selector limits which file is exposed; it is not a truth evaluator. Source warrant is unknown, and specific acquired propositions cannot be assessed without the private artifact: [EPI-RTE-report-import](#epi-rte-report-import).

The foreground model can select actions without a human approving each one. Software may reject invalid requests or block execution; operational permission is not epistemic warrant. No supplied candidate/input pair establishes a particular ampliative conjecture or acceptance decision. The model's processing and any provider-side parameter changes remain uninspected, independently of the implemented local loop: [RT-RTE-react-loop](runtime.md#rt-rte-react-loop), [RT-RTE-act-gate](runtime.md#rt-rte-act-gate), [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model).

The scratchpad can retain unreviewed notes and plans and later return them through a requested tool call. Its admission criterion is schema/string and byte size for run-local storage, not evidential adequacy for a named proposition or strategy. The model may rely on recalled content through tool history; actual reliance is unobserved. Compaction removes old context and merely asks for a save. Neither retention nor a reminder establishes successful preservation, accepted knowledge or lifecycle integration: [EPI-RTE-memory-document](#epi-rte-memory-document), [RT-RTE-context-trim](runtime.md#rt-rte-context-trim).

Terminal wealth measurement has a genuine consumer: hosted evaluation includes it in the returned result with run identity and terminal status. Its license is performance measurement in that simulated run, not truth of an explanation, safe replay, cross-scenario transfer, or attribution to memory, reflection or reasoning. No inspected result consumer automatically selects or installs a better agent. No run or comparison establishes improved capacity; model-guided policy adaptation is afforded by repeated feedback, not demonstrated learning. Content-directed criticism and its iterated retention are not established by score extraction. Possible self-representation in arbitrary scratchpad text is not evidence of reflection's two causal directions. Self-improvement would additionally require evidence-responsive changes to live behavior-determining organization and subsequent dependence on those changes; the optional save/recall route alone does not establish those exercised links. These are independent limits, not a bundled negative about the whole system: [EPI-RTE-wealth-metric](#epi-rte-wealth-metric), [EPI-RTE-memory-document](#epi-rte-memory-document).

Uninspected diagnostic handlers and opaque external agents prevent a system-complete negative about other epistemic routes. What is established is narrower: simulated evidence production, constrained action execution, unreviewed text retention, optional recall and bounded outcome measurement, each with its own authority and evidence limits.

## Shared records

### Operative objects

#### EPI-OBJ-store-snapshot
Label: Store snapshot

Distinct from [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief): this is changing run-specific evidence rather than the initial instruction. Symbolic dicts in server memory contain tick, order counters, supply risks, cash and rating. Text rendering is consumed as natural language; structured snapshots remain available to tool clients. It is current-run state, not automatically a retained memory object. SRC-1, `env/tools/observation.py`, `build_store_snapshot` and `render_observation_text`.

> "cash": _new_cash(env, agent_id),
> --- `env/tools/observation.py`

#### EPI-OBJ-daily-report
Label: Daily opportunity report

No counterpart among supplied runtime objects; this is imported private Markdown, not a system brief or callable registry. Files are date-named under the configured/private report directory; the tool returns content in a symbolic envelope. Natural-language market claims, if present, are interpreted by the model. Specific propositions and original evidential provenance are unavailable. SRC-1, `env/data/daily_reports.py`, `env/tools/tools.py`.

> filename = report_date.strftime("%Y%m%d") + ".md"
> --- `env/data/daily_reports.py`

#### EPI-OBJ-memory-doc
Label: Run-local Markdown scratchpad

A material output of [RT-RTE-act-gate](runtime.md#rt-rte-act-gate), not the gate itself; no supplied object denotes this file. The sanitized agent filename resides under run/agent/memory, with a separate version-history Markdown file. Content can mix natural-language claims and plans; structural markers and byte metadata are symbolic. Python/file persistence does not establish factual content, a theory or endorsement. SRC-1, `env/tools/tools.py`, memory path and history functions.

> return os.path.join(env.runs_root, env.run_id, "agent", "memory",
>                         f"{safe_agent_id}.md")
> --- `env/tools/tools.py`

#### EPI-OBJ-eval-metrics
Label: Hosted evaluation metrics

A result object distinct from the enclosing process route [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval); no supplied object denotes it. Symbolic numeric/Boolean fields live in a Python dict and the CLI result JSON. They represent simulated wealth/profit/rating/survival, not statements explaining a policy. SRC-1, `eval/scoring.py`, `eval/run_eval.py`; the latter packages metrics with scenario, seed and terminal status.

> "n_steps": len((series.get("net_assets") or [])),
> --- `eval/scoring.py`

### Routes

#### EPI-RTE-observation-render
Label: Store observation rendering
Part of: [RT-RTE-react-loop](runtime.md#rt-rte-react-loop)

This part owns the evidence-to-text transformation, not model proposal generation. Server observation code builds the snapshot and formats selected fields into the text consumed by the baseline. Target is representational fidelity for displayed current state, not policy quality. Owner is deterministic Python; no independent evaluator accepts claims. SRC-1, `env/tools/observation.py`, `build_store_snapshot`, `render_observation_text`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured snapshot and English observation text with order, supply, cash and shop sections plus a goal instruction.
- Later read-back: Baseline observation text accumulates in later model history until trimming, as in the parent route; snapshot itself is current state, not retained memory.
- Delegated visibility: Model receives the rendered text, not every server field; structured clients can request snapshot data.
- Selection predicate: Observation delivery or get_observation/get_store_snapshot request for an agent and current observation window.
- Invalidation or expiry: New ticks/windows change the snapshot; client history can retain older descriptions until trimmed.
- Activation or effect: Information and the net-assets objective reach the model context, advisory for action selection; no independent permission or demonstrated compliance.
- Evidence limits: Formatting source establishes the selected mapping, not every upstream event/rating equation or real-world truth.

Concrete deduction without execution: a snapshot with active=2, max=5, free_slots=3 renders `Shelf utilization: active 2 / max 5 / free 3`. The formatter prints supplied values; it does not infer a profitable next action. Monetary and rating displays round numeric inputs, so visible precision is reduced. The final imperative is policy guidance, not a derived factual claim.

> f"Shelf utilization: active {listing['active']} / max {listing['max']} / "
>             f"free {listing['free_slots']}",
> --- `env/tools/observation.py`

> sections.append("Continue operating the store. Goal: maximize net_assets.")
> --- `env/tools/observation.py`

#### EPI-RTE-report-import
Label: Current daily report import

A distinct acquisition route not separately declared in supplied runtime; overlaps [RT-RTE-act-gate](runtime.md#rt-rte-act-gate) only as an exposed read handler. Owner is server tool/reader code; current simulation date selects a Markdown file. Target is file availability at the selected date, not report accuracy. A successful read updates the agent/date cursor and suppresses its notice. SRC-1, `env/data/daily_reports.py`, `env/tools/tools.py`, `get_daily_report` and `daily_report_notice_available`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ok/report_date/data_as_of/content, or missing-date/file error.
- Later read-back: Returned text can reach later model calls through tool history; persisted read cursor changes later availability notices, not report content.
- Delegated visibility: Agent receives full file text and computed date labels; underlying source datasets and report-generation procedure are not supplied.
- Selection predicate: Current simulation date and configured report directory; exposed tool accepts no requested future date.
- Invalidation or expiry: Successful read suppresses only this agent's notice for that date; a later date selects another file. There is no semantic withdrawal mechanism in this reader.
- Activation or effect: Tool text is advisory evidence to the foreground model; cursor enforces notice suppression across server restart. It does not require a belief or action.
- Evidence limits: Existence/date selection is not authentication, freshness of actual content or acceptance. Private text unavailable; warrant unknown.

Operational admission of this input is software date/path selection. Caller asks to read; no per-report human approval or truth test occurs in this route. It imports rather than produces the underlying market claims. The `data_as_of` value is calculated from filename date without checking content:

> "data_as_of": (report_date - timedelta(days=1)).isoformat(),
>         "content": content,
> --- `env/tools/tools.py`

> with open(path, "r", encoding="utf-8") as f:
>         return f.read()
> --- `env/data/daily_reports.py`

#### EPI-RTE-cash-pipeline
Label: Known-order cash pipeline

Distinct from the generic execution gate [RT-RTE-act-gate](runtime.md#rt-rte-act-gate): this handler derives a specific diagnostic. Deterministic SQL/Python under the environment lock aggregates current delivered/unsettled orders and active-order purchase costs. It sums current cash components and separates receivables by delivery age. Target/domain is known simulated orders belonging to this run and agent, not prediction of future settlement. SRC-1, `env/tools/tools.py`, `query_cash_pipeline`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current cash, receivable aging, settlement-policy limits and active-order status/cost totals, or guard/window error.
- Later read-back: Diagnostic results can accumulate in the parent's model tool history; no separately persisted summary or policy change in this handler.
- Delegated visibility: Agent sees aggregates, not pre-sampled future anomaly or exact-settlement variables.
- Selection predicate: Live-agent tool request; window_days must be 1, 3, 7 or 14.
- Invalidation or expiry: Changes to current cash/orders/time make a returned snapshot historical; later calls recalculate.
- Activation or effect: Advisory diagnostic to caller/model through the tool-result channel during this run; no automatic action, rejection or strategy acceptance.
- Evidence limits: Arithmetic/SQL entail the output from selected database rows and cash premises; premise correctness and outcome utility are not independently measured.

Concrete deduction: cash balance 10, deposit_pool 20, in_transit 3, receivable 4 yields net_assets 37. The implementation does not deduct cumulative fines again. A delivered/unsettled row contributes its sale price to the reported receivable bucket, not a guarantee it will settle for that amount. This is a counterexample to treating every financial diagnostic as a forecast.

> "net_assets": _round_money(
>                 cash.balance + cash.deposit_pool + cash.in_transit + cash.receivable
>             ),
> --- `env/tools/tools.py`

> "exact_timing_known": False,
>                 "full_sale_proceeds_guaranteed": False,
> --- `env/tools/tools.py`

#### EPI-RTE-memory-document
Label: Scratchpad admission retention and recall
Part of: [RT-RTE-act-gate](runtime.md#rt-rte-act-gate)

The part is the memory-specific handler chain, not a duplicate of general protocol admission. Its separate ledger rows distinguish byte admission from retention. Model, human or deterministic caller proposes full content; dispatch and handler decide whether it can be stored. Server code can veto malformed HTTP arguments and oversized content, not false claims. SRC-1, `env/tools/dispatch.py`, `env/tools/registry.py`, `env/tools/tools.py`, memory read/write/history functions. The foreground guidance to keep concise strategy/product notes and the compaction reminder can shape a proposal, but neither provides an evidential criterion.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Write returns ok/bytes or size error; read returns full content/bytes, empty if absent.
- Later read-back: Explicit read_memory_doc retrieves the current run/agent file; the baseline places results in later model history through the parent loop. Version history is retained but is not automatically fed to the model by these tools.
- Delegated visibility: Handler sees proposed text and server-chosen run/agent identity; model sees returned text if requested. No separate critic or reviewer receives content through this chain.
- Selection predicate: Tool grant, valid request and at most 256 KiB UTF-8 for writes; identity selects the one run-local document for reads.
- Invalidation or expiry: Next write replaces current text; previous versions remain in history. Context trimming does not delete files. No automatic semantic invalidation or history-based rollback in these handlers.
- Activation or effect: Successful write enforces replacement and appends history. Recalled text is advisory model context over later calls in this run, not enforced policy. Actual changed behavior is unobserved.
- Evidence limits: No saved instance/input-output trace supplied. Byte-preserving retention does not decide whether authored content imports, compresses, entails or conjectures a claim, nor establish truth, usefulness or learning.

Admission trigger is a write request; intended use is scratchpad retention. No expected-answer oracle or per-content human approval is required. This is operational storage admission, not evidence-consuming acceptance for a proposition/use/scope. Model-authored revision and subsequent reliance remain possible, not observed. Later overwrite provides correction by replacement; history provides records, not an implemented truth-directed withdrawal process. Filesystem write precedes history append, so the two are not one atomic acceptance transaction.

> if size > _MEMORY_DOC_MAX_BYTES:
>         return {"ok": False,
>                 "error": f"content too large ({size} bytes, max {_MEMORY_DOC_MAX_BYTES})"}
> --- `env/tools/tools.py`

> with open(path, "w", encoding="utf-8") as f:
>         f.write(content)
>     _append_memory_history(env, agent_id, content)
> --- `env/tools/tools.py`

#### EPI-RTE-wealth-metric
Label: Terminal wealth measurement
Part of: [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval)

This part owns the evaluator calculation and its result consumer, not container orchestration. Target is a merchant's outcome in one scenario/seed run. The deterministic evaluator reads the last net_assets series point; if unavailable it sums cash components. It also returns profit, rating, survival and number of metric points. SRC-1, `eval/scoring.py`, `compute`; `eval/run_eval.py`, result packaging and CLI output.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rounded score/final_net_assets and supporting outcome fields in a result dict.
- Later read-back: Hosted CLI writes result JSON for operator consumption; no inspected automatic agent/policy installation or feedback from this result into the next model call.
- Delegated visibility: Evaluator receives merchant-section state; result consumer receives metrics, scenario/seed/agent/image/run identities, terminal status and log tail, not a proof of why performance occurred.
- Selection predicate: Hosted harness finishes polling and fetches merchant state; metric selects final available series values with explicit fallbacks.
- Invalidation or expiry: Metric is a terminal/historical result; resource cleanup does not withdraw or validate it. Early-failure cash fallback may produce a number with zero metric points.
- Activation or effect: Metric is included in returned/serialized evaluation output, reporting force to operators; no enforcing pass threshold, automatic successor ranking or policy update in this inspected consumer.
- Evidence limits: No supplied outcome or intervention. Outcome comparison would require actual runs; component attribution additionally requires independent variation, not just different agents or a high score.

Operator selects candidate image/scenario/seed; software calculates, with no expected correct action sequence and no semantic strategy acceptance. Its reference is simulated terminal state. A concrete code deduction: if net_assets series ends in `[100, 123.456]`, score and final_net_assets are 123.46 regardless of the current cash dict. Without a usable point, cash 10+20+3+4 yields 37.00. Thus numeric scoring can occur without evidence of a full 365-day successful run; terminal_status, survival and n_steps are essential context.

> net = _last(series.get("net_assets") or [])
> --- `eval/scoring.py`

> "score": round(float(net), 2),
>         "final_net_assets": round(float(net), 2),
> --- `eval/scoring.py`

> merchant = _fetch_merchant(env_url, run_id, agent_id,
>                                    headers=admin_headers)
>         result_metrics = scoring.compute(merchant)
> --- `eval/run_eval.py`

> "terminal_status": status,
>             "agent_id": agent_id,
>             **result_metrics,
> --- `eval/run_eval.py`

### Claims

#### EPI-CLM-horizon-evaluation
Label: Long-horizon agent evaluation

Distinct from [RT-CLM-http-controls](runtime.md#rt-clm-http-controls): this is the public benchmark-purpose claim, not an execution guarantee. SRC-1, `README.md`, Key Features, doctrine/design, claims evaluation of sustained/revised goal-directed policy across a 365-day operation and adaptation to delayed evidence.

> MerchantBench evaluates whether an agent
>   can sustain and revise a goal-directed merchant policy throughout a 365-day
>   operation, rather than complete a bounded task.
> --- `README.md`

The supplied loop and newly inspected observation/scoring routes support an implemented opportunity to act repeatedly on delayed simulated feedback and measure wealth. The wording “rather than complete a bounded task” is source rhetoric: the shipped benchmark still has a bounded scenario and horizon. Wealth is a proxy outcome, not direct measurement of coherence, reasoning, learning or truth of a policy explanation. Implemented repeated decision opportunities and outcome extraction support the evaluation workflow; no observed-run evidence establishes any agent's actual adaptation, and no causal experiment establishes which component caused performance. This is a limit on interpretation, not a claim that an operational benchmark must accept theories or contain a semantic reviewer.
