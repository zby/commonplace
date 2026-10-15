---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Hindsight epistemic routes: source acquisition, observation revision, page refresh, answer generation and bounded evaluation at the frozen commit."
run-id: AAS-2026-10-14-hindsight-34c2ca821edf-01
reviewed-boundary: "610c135b6f2d0d8b972da94146ae635943f36271"
---

# Hindsight epistemic report

## Source-and-claim boundary

The question is how Hindsight turns submitted material into later usable claims, checks those claims, and licenses reliance. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register), SRC-1. The frozen repository is a complete artifact with partial loop inspection, not a whole-system audit. External hosts, serving weights, hosted internals and live benchmarks remain outside the inspected loop.

The public knowledge claims are [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). The principal distinction is between supporting-source bookkeeping and a decision that a claim is true enough for a named use. This report finds both operationally consequential checks and a separate benchmark acceptance procedure; it does not treat every successful write as that procedure.

| Entry point or operation | Source path | Coverage and record | Limit and conclusion prevented |
|---|---|---|---|
| HTTP retain/reflect, worker, Claude Code hooks | `hindsight-api-slim/hindsight_api/engine/memory_engine.py`; `hindsight-integrations/claude-code/hooks/hooks.json` | Supplied findings: [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks) | Actual activation and host benefit unobserved |
| CLI operation inventory | `hindsight-cli/src/main.rs` | Direct dispatch/declaration search: memories retain/recall/reflect, documents delete, mental models, directives, operations retry/cancel | Rust transport branches not fully inspected; no parity claim |
| MCP registered operations | `hindsight-api-slim/hindsight_api/api/mcp.py`; `hindsight-api-slim/hindsight_api/mcp_tools.py` | Direct searches locate enabled-tool filtering, extension registration, retain/sync_retain, recall/reflect callbacks, page CRUD/refresh and directives | Search corroborates material operations beyond HTTP, not complete transport admission inspection; no universal HTTP-only gate |
| Pre-extraction defense | `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`; `hindsight-api-slim/hindsight_api/extensions/builtin/memory_defense_regex.py` | Direct reads: [EPI-RTE-defense-screen](#epi-rte-defense-screen) | Full detector patterns/custom implementations uninspected; no comprehensive privacy guarantee |
| Fact prompt/schema transformation | `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py` | Direct reads/searches: [EPI-RTE-optional-dimensions](#epi-rte-optional-dimensions); supplied extraction/storage account above | Full extraction response repair and strategy alternatives uninspected; no extraction accuracy verdict |
| Observation generation and write | `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`; `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py` | Direct bounded reads: [EPI-RTE-observation-batch](#epi-rte-observation-batch) | Semantic-dedup adjudicator, every retry and alternative store not fully inspected; no exhaustive revision account |
| Source withdrawal/replacement (cold invalidation/revert archive not traced) | `hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py`; `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py` | Direct reads: [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal) | Every caller and mental-model stale-read policy uninspected; no instantaneous all-consumer retraction guarantee |
| Page refresh and preserve-on-failure | `hindsight-api-slim/hindsight_api/engine/memory_engine.py` | Direct bounded reads: [EPI-RTE-page-refresh](#epi-rte-page-refresh) | Delta edit construction and full grounding validation not exhaustively inspected; no semantic completeness claim |
| Directive creation and later interpretation | `hindsight-api-slim/hindsight_api/engine/memory_engine.py` | Direct create read, supplied reflect consumer: [EPI-RTE-directive-write](#epi-rte-directive-write), [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request) | Authorship unresolved; no guaranteed model compliance |
| Final-answer budget fallback/configuration/extensions | `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`; `hindsight-api-slim/hindsight_api/config_resolver.py`; `hindsight-api-slim/hindsight_api/extensions/loader.py` | Supplied findings: [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis), [RT-RTE-config-update](runtime.md#rt-rte-config-update), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | Not reread as complete implementations here; no system-wide safety or answer-warrant guarantee |
| Knowledge-page convergence evaluator | `hindsight-system-evals/hindsight_system_evals/judge.py`; `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py` | Direct reads: [EPI-RTE-page-evaluation](#epi-rte-page-evaluation) | No execution evidence, causal intervention or complete evaluator inventory |
| Other integrations, embedded callers, UI, retrieval/reranking, other evaluators and maintenance instructions | See boundary inspection map | Available but uninspected here | These material alternatives prevent a system-complete negative about acceptance, learning or evaluation |

No supplied trace establishes a produced claim's actual acceptance, later reliance or improved outcome. Missing serving-weight identities prevent assessment of provider-internal learning; missing controlled comparisons prevent attributing benefit to consolidation, reflection or any individual component. Neither gap removes the inspectable architectural findings below.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-units](#epi-obj-memory-units) | Extracted statements about the world or agent experience | see record | SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py` | Input source truth and semantic preservation not independently established |
| [EPI-OBJ-observations](#epi-obj-observations) | Merged claims, historical/current state and recurring patterns | see record | SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py` | Source count is not independent corroboration; meaning can change |
| [EPI-OBJ-mental-models](#epi-obj-mental-models) | Standing answers/pages | see record | SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py` | Full and delta routes differ; no warranted-premise assumption |
| [RT-OBJ-context-history](runtime.md#rt-obj-context-history) | Retrieved claims and generated answers within a request | see record | SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py` | Model compression and optional evidence IDs do not prove fidelity |
| [EPI-OBJ-directives](#epi-obj-directives) | Normally policy rather than truth-apt assertion; arbitrary supplied text may also assert claims | see record | SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py` | Truth-aptness of an actual directive is not determinable without its content |
| [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config) | None for operational settings | see record | SRC-1, `hindsight-api-slim/hindsight_api/config_resolver.py` | Controls machinery rather than certifying truth |

Distributed-parametric producers are see [RT-CMP-retain-llm](runtime.md#rt-cmp-retain-llm), [RT-CMP-reflect-llm](runtime.md#rt-cmp-reflect-llm), [RT-CMP-embeddings](runtime.md#rt-cmp-embeddings). Numerical inference and model names do not establish a localized proposition or training event. Consolidation's configured model and the evaluation judge are separately bounded in their route records.

## Authority-route ledger

Each compact entry refers to fields owned by its declaring record rather than duplicating its implementation account. All architectural findings concern source wiring, not observed execution.

Route ID: [RT-RTE-retain-work](runtime.md#rt-rte-retain-work)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-units](#epi-obj-memory-units)
Content/update relation: truth-apt transformation: acquisition/import for submitted content, source warrant unknown; truth-apt transformation: indeterminate for model extraction (faithful reshaping versus changed/inferred assertions requires input/output comparison).
Transition or check target: submitted content to facts.
Evaluator/condition and domain: see route; extraction is candidate generation, not an independent truth evaluator.
Activation and timing; possible or observed result; implemented force: see route.
Epistemic authority and scope: no additional truth license follows from extraction or storage.
Operational authority and behavioral-authority path: see route and [RT-BAP-hook-context](runtime.md#rt-bap-hook-context); later recall/reflect can select these facts, advisory natural-language input beyond fixed selectors.
Evidence: see route, SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: retention is not acceptance. Gap/limit: no observed source/output pairs.

Route ID: [EPI-RTE-defense-screen](#epi-rte-defense-screen)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-units](#epi-obj-memory-units), before extraction.
Content/update relation: no content change at the screening decision.
Transition or check target: sensitive-data pattern presence in submitted text, not truth of its propositions.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: operative allow/redact/block decision consumed by orchestrator.
Epistemic authority and scope: detection under the configured detector, not factual endorsement.
Operational authority and behavioral-authority path: see record; enforcing before extraction, this retain request.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/extensions/builtin/memory_defense_regex.py`.
Claim IDs: none. Mismatch marker: none. Gap/limit: detector coverage uninspected.

Route ID: [EPI-RTE-defense-screen](#epi-rte-defense-screen)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-units](#epi-obj-memory-units), input stage.
Content/update relation: truth-apt transformation: indeterminate when redaction removes content; no content change for allow/block.
Transition or check target: admission to extraction under sensitive-data policy.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: remove blocked items or replace text, with all-blocked error.
Epistemic authority and scope: operational policy admission only; no truth acceptance.
Operational authority and behavioral-authority path: orchestrator consumes decision, enforcing via content-list mutation before downstream extraction/storage; see record.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`.
Claim IDs: none. Mismatch marker: admission is not truth warrant. Gap/limit: policy may be disabled.

Route ID: [EPI-RTE-observation-batch](#epi-rte-observation-batch)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-observations](#epi-obj-observations)
Content/update relation: truth-apt transformation: indeterminate. Prompted merges aim at non-ampliative consolidation; neither losslessness nor non-entailment is established for arbitrary model outputs. No checked entailed derivation is established.
Transition or check target: new facts plus recalled observations to proposed creates/updates/deletes.
Evaluator/condition and domain: model applies facet matching, state-change and durability rules; see record.
Activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: source-conditioned candidate interpretation, not independently established source truth.
Operational authority and behavioral-authority path: proposal feeds preparation/write code, permissive after local gates; later observation readers receive changed prose.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: evidence-backed belief does not imply accepted truth. Gap/limit: no actual output proves ampliative conjecture.

Route ID: [EPI-RTE-observation-batch](#epi-rte-observation-batch)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-observations](#epi-obj-observations)
Content/update relation: no content change.
Transition or check target: action structure, recalled target membership, resolvable/live sources and sources unchanged since read.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: preparation and transaction consumers can discard actions or whole batch.
Epistemic authority and scope: lineage/target consistency, not proposition verification or independence of evidence.
Operational authority and behavioral-authority path: see record; enforcing at observation update transaction, with retries possible later.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: freshness is not endorsement. Gap/limit: alternate store behavior remains contract-dependent.

Route ID: [EPI-RTE-observation-batch](#epi-rte-observation-batch)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-observations](#epi-obj-observations)
Content/update relation: no content change at admission decision.
Transition or check target: whether prepared model actions may change stored observations.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: reject unresolved/disallowed actions; discard stale-source batch; allow prepared actions.
Epistemic authority and scope: operational admission, not evidenced acceptance of an ampliative claim against a truth criterion.
Operational authority and behavioral-authority path: model proposes, code vetoes, transaction permits mutation; see record.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: none. Gap/limit: semantic-dedup subroute remains partially inspected.

Route ID: [EPI-RTE-observation-batch](#epi-rte-observation-batch)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-observations](#epi-obj-observations)
Content/update relation: no content change at commit beyond prepared proposals.
Transition or check target: prepared actions to stored observations and consolidation markers.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: batch commit/abort with source bookkeeping.
Epistemic authority and scope: retention of candidates; lifecycle integration after epistemic acceptance is not established by this commit.
Operational authority and behavioral-authority path: later retrieval and page/answer models can consume retained statements across requests; see record.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: retention versus acceptance. Gap/limit: successful actual commit unobserved.

Route ID: [EPI-RTE-page-refresh](#epi-rte-page-refresh)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-mental-models](#epi-obj-mental-models)
Content/update relation: truth-apt transformation: indeterminate for synthesis/editing, no content change on preserve branches.
Transition or check target: refresh result is nonempty, delta operations applied when required, and configured structured projection available.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: safe-to-persist structural/procedural status, not a truth certificate.
Operational authority and behavioral-authority path: enforcing preservation on named failures; successful path calls update, later page reads/reflection receive prose; see record.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: settled knowledge versus fallible stored synthesis. Gap/limit: semantic checks inside delta generation not fully traced.

Route ID: [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-observations](#epi-obj-observations)
Content/update relation: no content change to surviving facts; derived observation removal.
Transition or check target: observations referencing outgoing source IDs.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see record.
Epistemic authority and scope: removes reliance on stale derivation, not a finding that the withdrawn proposition is false.
Operational authority and behavioral-authority path: PostgreSQL cleanup deletes observations and requeues surviving facts; enforcing for this transaction, future reconsolidation depends on scheduling.
Evidence: see record, SRC-1, `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: none. Gap/limit: no all-page retraction guarantee.

Route ID: [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-context-history](runtime.md#rt-obj-context-history), [EPI-OBJ-mental-models](#epi-obj-mental-models), [EPI-OBJ-observations](#epi-obj-observations)
Content/update relation: truth-apt transformation: indeterminate for answer generation/compression; retrieval alone makes no content change.
Transition or check target: retrieved material and current query to returned answer, with enabled-tool/budget constraints.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see records.
Epistemic authority and scope: model-grounded answer candidate. Forced retrieval and IDs do not verify answer propositions; final synthesis is a countercase to universal retrieval-completion requirements.
Operational authority and behavioral-authority path: see records and [RT-BAP-hook-context](runtime.md#rt-bap-hook-context); answer/context delivered advisory to later caller/host, compliance unobserved.
Evidence: see records, SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: gathered evidence versus demonstrated warrant. Gap/limit: no expected-answer oracle on supplied request path.

Route ID: [EPI-RTE-directive-write](#epi-rte-directive-write), [EPI-RTE-optional-dimensions](#epi-rte-optional-dimensions), [RT-RTE-config-update](runtime.md#rt-rte-config-update)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-directives](#epi-obj-directives), [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config)
Content/update relation: non-truth-apt policy/content update: caller instructions, symbolic settings and mechanical prompt substitution.
Transition or check target: configured instruction/setting to future operation inputs.
Evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see records.
Epistemic authority and scope: no factual warrant added. The deterministic substitution warrants only its literal output in its string domain.
Operational authority and behavioral-authority path: symbolic settings enforce selection; model-facing wording is interpretive policy influence, not guaranteed obedience; see records and [RT-BAP-config-consumer](runtime.md#rt-bap-config-consumer).
Evidence: see records, SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py`.
Claim IDs: none. Mismatch marker: no inferred improvement. Gap/limit: arbitrary directive assertions require their actual content to assess.

Route ID: [EPI-RTE-page-evaluation](#epi-rte-page-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-mental-models](#epi-obj-mental-models), benchmark instance.
Content/update relation: no content change to graded page.
Transition or check target: page correctness under question-specific answer criteria and forbidden current claims.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: verdict consumed by assertions and reporting.
Epistemic authority and scope: reference-criterion assessment within constructed page-convergence cases, conditional on judge fidelity; not verified general truth or causal mechanism.
Operational authority and behavioral-authority path: test assertion enforces pass/fail, report aggregates; no inspected feedback to production page admission.
Evidence: see record, SRC-1, `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: evaluator existence is not observed superiority. Gap/limit: no runs supplied.

Route ID: [EPI-RTE-page-evaluation](#epi-rte-page-evaluation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-mental-models](#epi-obj-mental-models), tested page candidate.
Content/update relation: no content change.
Transition or check target: acceptance of this test case, for regression-testing use, when correct and not trapped.
Evaluator/condition and domain; activation and timing; possible or observed result: see record.
Implemented force: `_assert_sound` rejects failing cases.
Epistemic authority and scope: recorded evidence-consuming benchmark decision when executed; does not accept all page propositions for unrestricted use.
Operational authority and behavioral-authority path: enforcing test continuation/pass status within evaluator, not a production installation gate in inspected code.
Evidence: see record, SRC-1, `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`.
Claim IDs: [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs). Mismatch marker: no established production lifecycle integration after this acceptance. Gap/limit: actual verdict unavailable.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs) | Evidence-backed beliefs and learned understanding | SRC-1, `README.md`, doctrine/design | see record | [EPI-RTE-observation-batch](#epi-rte-observation-batch), [EPI-RTE-page-refresh](#epi-rte-page-refresh) | none supplied | No comparison isolates learning or accuracy | Source-conditioned revision and persistent candidate reuse implemented | Source links/counts do not establish truth; semantic transformation indeterminate |
| [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs) | Page as settled knowledge | SRC-1, `README.md`, doctrine/design | see record | [EPI-RTE-page-refresh](#epi-rte-page-refresh), [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request) | none supplied | Test documentation reports false stored pages, not supplied traces | Standing answers are reusable; structural preserve-on-failure exists | Settled is not an epistemic certificate |
| [EPI-CLM-memory-beliefs](#epi-clm-memory-beliefs) | Smarter agents learning over time; state-of-the-art long-term-memory performance | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks), [EPI-RTE-page-evaluation](#epi-rte-page-evaluation) | none supplied; attributed reports only | Evaluator checks bounded cases; no controlled comparative result inspected | Behavioral input and test capacity implemented | Improved capacity, component benefit and comparative superiority unestablished |

## Bounded conclusion

Hindsight acquires submitted claims with unknown source warrant, asks models to extract and revise them, and retains candidates for later retrieval, page refresh and answers. Source-conditioned generation is implemented; accurate extraction, non-ampliative semantic preservation and produced accepted ampliative claims are not established by these static paths. No inspected transformation supplies warranted source premises plus a checked interpretation sufficient to certify a new world claim by entailment. These are route-local findings, not a system-complete negative. See [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), [EPI-RTE-observation-batch](#epi-rte-observation-batch), [EPI-RTE-page-refresh](#epi-rte-page-refresh).

The consequential checks have different targets. Defense gates sensitive-data policy; consolidation gates source/target consistency and freshness; page refresh gates structural/procedural persistability; the regression evaluator judges stated answer criteria. Their force ranges from rejecting individual retain items, through aborting writes/preserving prior content, to failing a test. Only the last is an inspected criterion-based correctness acceptance procedure, scoped to benchmark use; its result is not shown to feed production knowledge admission. Retention and later use are therefore not silently classified as post-acceptance lifecycle integration. See [EPI-RTE-defense-screen](#epi-rte-defense-screen), [EPI-RTE-observation-batch](#epi-rte-observation-batch), [EPI-RTE-page-refresh](#epi-rte-page-refresh), [EPI-RTE-page-evaluation](#epi-rte-page-evaluation).

Withdrawal has implemented force: the inspected PostgreSQL cleanup removes observations derived from outgoing facts and resets surviving sources for reconstruction. It prevents that stale observation from remaining on that storage route, not all stale page answers or already delivered host contexts. See [EPI-RTE-source-withdrawal](#epi-rte-source-withdrawal).

Instructions and settings have separate behavioral authority without needing truth-apt claims. Directive writes are permission-gated policy installation; optional-dimension rewriting is a literal, deterministic prompt change. Both can shape later model inputs without establishing improvement. Reflection's evidence gathering is bounded by budget and terminal synthesis; cited IDs and supporting prose do not independently validate answers. See [EPI-RTE-directive-write](#epi-rte-directive-write), [EPI-RTE-optional-dimensions](#epi-rte-optional-dimensions), [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis).

Recurring trace retention and later context injection establish a standing experience-to-behavior path, not exercised self-improvement. For that bounded hook pathway, durable source-derived state and a live advisory channel are wired, but objective-bearing evidence selecting an improvement and subsequent behavior causally depending on it are unestablished. Learning as improved capacity remains unestablished separately. The name reflect establishes neither self-representation of the machinery nor the four theory-builder conditions. Observation prose is localized and revisions can be proposed computationally; consumed criticism with blame placement and iterated retained effect is not established by that fact alone. Provider-internal changes remain uninspected, not absent. See [RT-RTE-claude-hooks](runtime.md#rt-rte-claude-hooks), [RT-BAP-hook-context](runtime.md#rt-bap-hook-context), [EPI-RTE-observation-batch](#epi-rte-observation-batch), [RT-CMP-reflect-llm](runtime.md#rt-cmp-reflect-llm).

## Shared records

### Operative objects

#### EPI-OBJ-memory-units
Label: Extracted memory units

Source-native identity: extracted facts passed to `insert_facts_batch`, with `world`/`experience` classification. Natural-language fact text is the truth-apt part; symbolic IDs, types and source associations govern retrieval/storage. Substrate: retained memory store through the orchestrator. Distinct from supplied [RT-OBJ-context-history](runtime.md#rt-obj-context-history), which is request-local; no supplied operative-object counterpart for persisted facts. SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`; write passage is see [RT-RTE-retain-work](runtime.md#rt-rte-retain-work). Truth of source assertions is not established by the insertion API.

#### EPI-OBJ-observations
Label: Consolidated observations

Source-native identity: observation text plus `source_memory_ids`, source temporal aggregation and consolidation bookkeeping. Natural-language claims are stored through the memory store; symbolic source IDs/counts are lineage metadata with fixed-rule consumers. Distinct from source fact units above and from [RT-OBJ-context-history](runtime.md#rt-obj-context-history); source facts can survive withdrawal of the observation derived from them. SRC-1, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`, `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`; evidence is see [EPI-RTE-observation-batch](#epi-rte-observation-batch). The prompt explicitly describes `proof_count` as the number of merged source facts, not a proof of the prose claim.

> - `proof_count`: how many source facts this observation has already merged
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`

#### EPI-OBJ-mental-models
Label: Mental models and pages

Source-native identity: `mental_models.content`, with source query, trigger, refresh watermark and optional structured views. Natural-language standing answers are the assessed truth-apt part; symbolic trigger/watermark/structure controls update and selection. Substrate: database rows updated by `update_mental_model`. Distinct from supplied [RT-OBJ-context-history](runtime.md#rt-obj-context-history): pages persist and are later read; retrieved copies may enter the working context. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`; evidence is see [EPI-RTE-page-refresh](#epi-rte-page-refresh). Optional structured projections are not assumed semantic equivalents merely because they parse.

#### EPI-OBJ-directives
Label: Bank directives

Source-native identity: directive `content`, `priority`, `is_active`, tags and bank ID. Natural-language policy text is stored in `directives`; symbolic fields govern scope/order/activation. No supplied operative-object counterpart; closest consumer is [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request). Distinct from [RT-OBJ-bank-config](runtime.md#rt-obj-bank-config), which holds configuration overrides. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`; evidence is see [EPI-RTE-directive-write](#epi-rte-directive-write).

### Routes

#### EPI-RTE-defense-screen
Label: Pre-extraction defense screening

Part of: [RT-RTE-retain-work](runtime.md#rt-rte-retain-work)

The orchestrator passes each submitted item's content/tags/bank/document identity to the loaded defense extension. The inspected default checks configured sensitive-data rules via `apply_redaction`, returning allow/redact/block. This is a policy check, not a truth evaluator. Code consumes it before extraction, replacing redacted content in both parsed and raw representations or removing blocked items. All-blocked raises an error; partial blocks preserve submission-position accounting. Model/human approval is not part of this screen; caller policy selects the rule, extension computes the decision. Open ingestion mode; no answer oracle. Custom extensions and disabled policy are countercases to a universal default-screen claim. Rollback of historical content is not this pre-admission route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Decision to orchestrator; all-blocked error or downstream retain result to caller.
- Later read-back: Only surviving/redacted input proceeds to retained facts; blocked slots have no new fact IDs from this pipeline.
- Delegated visibility: Extension receives content and item scope; extraction receives surviving content.
- Selection predicate: Enabled policy, configured detector/rule and matched types.
- Invalidation or expiry: Per-submission decision; no automatic historical purge established.
- Activation or effect: Decision enforces list filtering/text replacement before extraction; deployed execution unobserved.
- Evidence limits: Detector pattern coverage and custom extensions uninspected; allow does not certify truth or absence of all sensitive data.

SRC-1, implementation, `hindsight-api-slim/hindsight_api/extensions/builtin/memory_defense_regex.py`, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`.

> rule = next((r for r in policy.rules if r.on == "sensitive_data"), None)
> if rule is None or rule.action is DefenseAction.ALLOW:
>     return DefenseDecision(action=DefenseAction.ALLOW)
> --- `hindsight-api-slim/hindsight_api/extensions/builtin/memory_defense_regex.py`

> if _decision.action is DefenseAction.REDACT:
>     _redacted = _decision.redacted_content or _content.content
>     _content.content = _redacted
> --- `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`

> _skip_indices = {v.index for v in _blocked_violations}
> surviving_indices = [i for i in range(original_count) if i not in _skip_indices]
> contents = [contents[i] for i in surviving_indices]
> contents_dicts = [contents_dicts[i] for i in surviving_indices]
> --- `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`

#### EPI-RTE-observation-batch
Label: Observation batch revision

This is the consolidation subloop, not a duplicate of [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), which schedules maintenance without tracing this judgment/write implementation. Endpoints: pending source facts and per-fact recalled observations → configured consolidation model → action preparation → transaction/store batch → observation readers. Code pools retrieved observations; model proposes creates/updates/deletes under mission/facet/state/history instructions; code can veto invalid targets, unresolved sources and changed source versions. Source-dependent candidate generation, checking, disposition and retention are separate ledger functions of this implementation. Mode is open maintenance, not a controlled experiment; there is no expected-answer oracle. No per-action human approval appears in this path.

The prompt forbids arithmetic/logical deductions under incomplete evidence, a countercase to classifying every observation as ampliative inference. It requests merge/update, reference resolution and state revision, but reliable semantic preservation is not enforced merely by those instructions. Thus actual output relation remains indeterminate between reshaping, supported inference and unsupported changed meaning until content instances are available. `reason` is required proposal rationale; it is not an independent verification decision.

The model is `memory_engine._consolidation_llm_config.with_config(...)` for optional dedup, and supplied `llm_config` for primary batch calls. Distributed-parametric parameters are external serving state; inspected code calls inference, not parameter training. Exact weights/version and deployed endpoint are unestablished; configurable endpoints may resolve to different weights. Optional semantic-dedup model adjudication is located but not fully assessed here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-memory create/update/merge statistics or propagated failure.
- Later read-back: Retained observation prose and source associations reach future recall, reflection and page synthesis; operation does not require benchmark acceptance first.
- Delegated visibility: Primary model sees batch fact text/temporal fields and pooled observations, with supporting facts potentially partial; preparation/store receive proposed actions and source identities.
- Selection predicate: Pending batch, tag/scope configuration, recalled related observations, capacity, mission and model action; code checks target membership and source resolution/liveness/change.
- Invalidation or expiry: Transaction failure aborts write batch; changed sources discard response and stamps; later deletion/replacement can retract derived observations.
- Activation or effect: Prepared deletes/updates/creates and consolidation markers commit together in inspected SQL transaction/store-batch protocol; actual commit and later reliance unobserved.
- Evidence limits: Alternate stores require their batch contract; complete dedup/retry paths and model fidelity uninspected. Storage consistency is not source truth.

SRC-1, doctrine/design and implementation, `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`, `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`.

> Synthesize and consolidate what was stated, but never do arithmetic or logical deductions.
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`

> - `reason`: REQUIRED on every create/update/delete — one sentence explaining the choice. For a CREATE, state which existing observation(s) you considered and why none matched (a near-identical existing observation means you should UPDATE, not CREATE). This is audited to catch duplicate creates.
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py`

> if not any(str(obs.id) == delete.observation_id for obs in union_observations):
>     logger.debug(
>         f"Batch consolidation: rejected delete — observation {delete.observation_id} not in unioned recall"
>     )
>     continue
> prepared_deletes.append(delete.observation_id)
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`

> source_mems = [mem_by_id[fid] for fid in update.source_fact_ids if fid in mem_by_id]
> if not source_mems:
>     _log_unresolved_action("update", update.source_fact_ids, update.text, perf)
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`

> prepared_deletes, prepared_updates, prepared_creates, stamp_ids = [], [], [], []
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`

> await write_batch.commit()
> except BaseException:
>     await write_batch.abort()
>     raise
> --- `hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py`

#### EPI-RTE-page-refresh
Label: Page refresh disposition

Distinct from [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request): this route owns the subsequent standing-page write or preservation decision, not the ordinary returned answer. Refresh executor selects full versus delta mode, records a run without writing, then persist path checks run outcome and optional structured output before `update_mental_model`. Failed empty candidates, unapplied delta and failed configured projection preserve previous document and watermark and raise. No-new-facts preserves content but marks refresh completion. Successful path installs `run.final_content`; intended use is standing answer reuse. These are operative persistence criteria, not an evidenced per-proposition truth acceptance decision. Delta-window text is explicitly not accepted as a replacement whole page on failed editing, countering a blanket overwrite claim.

Model proposes synthesis/edits; code decides persistability and can veto. Trigger/query/config shape proposal; persisted prose/metadata shapes later reads. Mode is recurring/open refresh; no expected-answer oracle or per-refresh human approval is established. Failure preserves old content for retry rather than choosing a semantically superior candidate by measured outcome.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated page, preserved-page refresh result, missing-row result or explicit refresh error.
- Later read-back: Stored page content and structured view are later readable; reflect can consume pages, see supplied reflect record.
- Delegated visibility: Executor has current content, source query, trigger and scoped retrieval controls; optional projection model receives final content/schema.
- Selection predicate: Trigger mode, baseline content/query, run outcome and response schema determine branches.
- Invalidation or expiry: Failure leaves document/watermark unchanged for retry; successful update replaces/edits standing answer. Full stale-read policy uninspected.
- Activation or effect: Successful result calls update with content and watermark; preserve branches withhold new content. Actual later reliance unobserved.
- Evidence limits: Delta edit validation and all grounding checks not exhaustively inspected; these guards alone establish neither completeness nor truth of successful pages.

SRC-1, implementation, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

> if run.outcome == "refresh_failed_delta_not_applied":
>     # #3112: the reflect candidate only covers the delta window, so it is
>     # not a document — see the guard in _execute_mental_model_refresh.
>     await _preserve_and_fail(
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> return await self.update_mental_model(
>     bank_id,
>     mental_model_id,
>     content=run.final_content,
>     reflect_response=reflect_response_payload,
>     last_refreshed_source_query=run.source_query,
>     refresh_watermark=run.processed_watermark,
>     refresh_completed=True,
>     structured_content=(run.final_structured.model_dump() if run.final_structured is not None else None),
>     request_context=request_context,
> )
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

#### EPI-RTE-source-withdrawal
Label: Source withdrawal cleanup

This PostgreSQL derived-state cleanup is distinct from supplied [RT-RTE-retain-work](runtime.md#rt-rte-retain-work), whose deletion details were uninspected. Fact-storage wrapper delegates to the memory store; PostgreSQL path identifies observations referencing outgoing facts, locks affected rows, deletes observations/history and resets surviving source consolidation markers. The caller supplies outgoing identities; fixed source-ID association, not a model truth verdict, selects affected observations. Mode: administrative/replacement maintenance; no answer oracle or improvement objective. Whole derived-observation withdrawal is conservative lineage repair, not proof that all remaining claims are true. Reconstruction requires future consolidation; no rollback-to-best semantic state is established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Count of removed observations from cleanup helper.
- Later read-back: Deleted observations cease to be available on this storage path; surviving source facts are requeued for future consolidation.
- Delegated visibility: Store receives bank/source identities and transaction connection, not a natural-language criticism of the claim.
- Selection predicate: Association with any outgoing source fact; remaining sources exclude outgoing IDs.
- Invalidation or expiry: Called before source deletion within transaction; caller failure relies on transaction recovery. Already-delivered contexts are not revoked by this helper.
- Activation or effect: SQL deletion and reset change subsequent availability and consolidation eligibility; actual execution unobserved.
- Evidence limits: Inspected PostgreSQL implementation only; other stores, every delete caller and dependent-page read policy remain uninspected.

SRC-1, implementation, `hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py`, `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`.

> await conn.execute(
>     f"DELETE FROM {fq_table('memory_units')} WHERE id = ANY($1::uuid[])",
>     obs_ids,
> )
> --- `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`

> UPDATE {fq_table("memory_units")}
> SET consolidated_at = NULL
> WHERE id = ANY($1::uuid[])
>   AND fact_type IN ('experience', 'world')
> --- `hindsight-api-slim/hindsight_api/engine/memories/pg/writes.py`

#### EPI-RTE-directive-write
Label: Directive policy installation

Distinct from [RT-RTE-config-update](runtime.md#rt-rte-config-update): stored directive text is a separate bank object consumed as instructions by reflection, not a merged config mapping. Endpoints: caller → authenticated/optionally validated bank write → tag-scope refusal → SQL directive insert → later active-directive selection in [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request). Caller proposes text/priority/activation/tags; code and optional validator veto. Human authorship and per-item human review unresolved. Open administrative policy mutation, no expected-answer oracle. Guidance is caller policy, not necessarily an evaluated improvement proposal. Creation exposes no outcome-scored rollback; later update/deletion operations exist but are not exhaustively traced here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created directive mapping or authorization/validation error.
- Later read-back: Active selected directives enter later reflection prompts; supplied reflection record owns selection details.
- Delegated visibility: Validator receives bank-write context; reflection model receives selected natural-language content.
- Selection predicate: Caller request, authentication, optional bank-write validation and writable tags; later active/scope selection.
- Invalidation or expiry: Active flag and later update/delete operations can change availability; full invalidation/caching uninspected.
- Activation or effect: Stored text can steer later model interpretation, advisory/policy force rather than invariant semantic compliance.
- Evidence limits: Default authentication limitations remain as supplied; no actual directive instance or downstream compliance evidence.

SRC-1, implementation, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`.

> # An untagged directive steers everyone's reflect, so a restricted writer cannot make one.
> self._refuse_unwritable(tags, await self._write_tag_scope(bank_id, request_context), "a directive")
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> INSERT INTO {fq_table("directives")}
> (bank_id, name, content, priority, is_active, tags)
> VALUES ($1, $2, $3, $4, $5, $6)
> RETURNING id, bank_id, name, content, priority, is_active, tags, created_at, updated_at
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

#### EPI-RTE-optional-dimensions
Label: Optional dimension prompt rewrite

Part of: [RT-RTE-retain-work](runtime.md#rt-rte-retain-work)

Deterministic input deduction from inspected implementation, not target execution: give `_null_instead_of_na` the string `why: 'N/A'; where: "N/A"; who: Ana`. First replacement yields `why: null; where: "N/A"; who: Ana`; second yields `why: null; where: null; who: Ana`. The output follows exactly in this string domain, with no source-truth premise. It changes instruction placeholders, not a new world proposition. When optional dimensions are configured, caller prompt also gets this rewrite and the optional-dimensions section; schema construction permits null dimensions. A custom instruction's literal quoted placeholder is also replaced, so this is not an assertion of semantic equivalence for arbitrary prompt text.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rewritten string/schema during extraction prompt construction.
- Later read-back: inapplicable — generated instructions are current-operation inputs, not material accumulated through use.
- Delegated visibility: Extraction model receives resulting prompt/schema, not a proof of equivalence.
- Selection predicate: `retain_optional_fact_dimensions` flag, with exact quoted substring matching in helper.
- Invalidation or expiry: Rebuilt from resolved configuration for operation; not a retained learned instruction.
- Activation or effect: Exact byte-level substitution and appended guidance are implemented; model's resulting behavior unobserved.
- Evidence limits: Literal transformation is entailed by code; semantic fidelity and extraction quality do not follow.

SRC-1, implementation, `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py`.

> return text.replace("'N/A'", "null").replace('"N/A"', "null")
> --- `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py`

> prompt = _null_instead_of_na(prompt) + OPTIONAL_DIMENSIONS_SECTION
> --- `hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py`

#### EPI-RTE-page-evaluation
Label: Knowledge page convergence evaluation

Distinct from supplied [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request): this is a regression-evaluation route with explicit criteria, outside production answer admission. The test builds a standing page over fact waves, obtains final content, asks a separately configured judge whether it meets question answer criteria and optionally asserts a forbidden current claim, records verdicts, then asserts correctness and no trap. Target/domain: final pages in question-specific convergence fixtures, including preservation of earlier facts and accumulated counts. Expected answer guidance comes from `question.answer_criteria` and `must_not_claim`, not from the page model's own completion. Human contribution is source-authored criteria; model grades; code decides test pass/fail. No runtime human review required by the inspected test.

Judge is a distributed-parametric Google provider model configured by environment, default `gemini-2.5-flash`; inference calls only, no visible parameter update. Exact weight/version pin is unestablished and provider endpoint may change serving state. Separate configuration is not proof of actual independent weights: module doctrine says fixtures warn if model identities coincide. Initial passes need one call; initial failures get configurable higher-temperature confirmations, majority can overrule. This is asymmetric noise handling, not calibrated confidence. Invalid JSON returns failure; confirmation exceptions are excluded. A majority judgment licenses criterion-relative test acceptance, not source truth or a component causal effect.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verdicts/page outcome; test pass or assertion failure and report record.
- Later read-back: `RECORDED` entries are consumed by evaluation reporting; no inspected route installs verdicts into production page knowledge.
- Delegated visibility: Judge receives final response, explicit criterion and optional question context; not necessarily raw fact-wave provenance.
- Selection predicate: Minimum-acceptance question IDs or full-marked question set; trap check when forbidden claim configured; confirmations on initial failure.
- Invalidation or expiry: Verdict belongs to this test invocation/configuration; rerun can differ. No production rollback consumer established here.
- Activation or effect: Verdicts feed assertions and recorded metrics, enforcing test acceptance; actual run and deployment/release consequences unobserved.
- Evidence limits: No supplied run artifact or controlled intervention; question corpus and all other evaluators not exhaustively assessed. Criterion/model errors remain possible.

SRC-1, implementation and doctrine/design, `hindsight-system-evals/hindsight_system_evals/judge.py`, `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`.

> verdicts = [primary] + [v for v in confirmations if isinstance(v, Verdict)]
> met = sum(1 for v in verdicts if v.meets_criteria)
> if met > len(verdicts) - met:
>     return Verdict(True, f"majority of {len(verdicts)} judges met the criteria (primary overruled as noise)")
> return Verdict(False, f"{len(verdicts) - met}/{len(verdicts)} judges agree: {primary.reasoning}")
> --- `hindsight-system-evals/hindsight_system_evals/judge.py`

> verdict = await evaluate(outcome.final_content, question.answer_criteria, context=context)
> outcome.correct, outcome.correct_reason = verdict.meets_criteria, verdict.reasoning
> --- `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`

> assert not outcome.hit_trap, (
> --- `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`

> assert outcome.correct, (
> --- `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`

### Claims

#### EPI-CLM-memory-beliefs
Label: Evidence-backed memory and learning claims

Public claims: Hindsight produces evidence-backed beliefs, learned world understanding and reusable settled knowledge, with smarter agents/long-term-memory performance claims. SRC-1, `README.md`, doctrine/design. No supplied runtime claim has this referent; [RT-CLM-tenant-check](runtime.md#rt-clm-tenant-check) concerns a separate authentication contract. These are attributable design/product claims, not accepted findings. Evaluation source comments report motivating page falsehoods; they are a useful countercase to inferring infallibility from a stored page, not independently inspected executions.

> - **Observations:** consolidated, evidence-backed beliefs formed from many memories
> - **Mental models:** learned understanding of the agent's world, synthesized from observations and facts
> --- `README.md`

> A **mental model** is a standing answer to a question about a bank ("What are this user's preferences?"). You define the question once; Hindsight writes the answer, stores it, and rewrites it in the background as the bank learns more. Reading one is a database read — no retrieval, no LLM call — so an agent can boot with a page of settled knowledge instead of rediscovering it every session.
> --- `README.md`

> Hindsight™ is an agent memory system built to create smarter agents that learn over time. Most agent memory systems focus on recalling conversation history. Hindsight is focused on making agents that learn, not just remember.
> --- `README.md`

> It eliminates the shortcomings of alternative techniques such as RAG and knowledge graph and delivers state-of-the-art performance on long term memory tasks.
> --- `README.md`

> Both traced to the same cause: the delta step treated the reflect synthesis as
> authoritative, when that synthesis is written from the new batch alone. Its
> totals count only the batch and its absences describe only the batch.
> --- `hindsight-system-evals/evals/test_01_knowledge_page_convergence.py`
