---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ReasoningBank's trajectory checks, advice admission and later reliance, separated from transfer and learning warrant."
run-id: AAS-2026-10-14-reasoning-bank-f0bedcab086c-01
reviewed-boundary: ed80611788292ea739f1effd31f16c53823b8a0d
---

# ReasoningBank epistemic report

## Source-and-claim boundary

The question is whether the shipped trajectory-to-advice-to-task loops establish warrant for the content they subsequently use. Scope, external dependencies and frozen source identity are see [boundary](boundary.md#boundary-and-evidence); sources are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. This member inspects feedback and its consumers independently of the provisional runtime account. It assesses task-evaluation predicates, induction, automatic admission, retention and later selection separately. It does not treat a task verdict as a check of the induced advice.

Consequential design claims are [EPI-CLM-memory-learning](#epi-clm-memory-learning), [EPI-CLM-memory-scaling](#epi-clm-memory-scaling) and [EPI-CLM-advice-transfer](#epi-clm-advice-transfer). The README explicitly scopes the release to demonstration rather than production. No universal knowledge-production claim is inferred from that release.

| Entry point or operation | SRC-1 source path | Coverage and conclusion boundary |
|---|---|---|
| Web task scheduling, agent execution and no-memory mode | `WebArena/pipeline_memory.py`; `WebArena/run.py`; `WebArena/agents/legacy/agent.py` | Supplied [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline), [RT-BAP-system-memory](runtime.md#rt-bap-system-memory). No-memory mode is a counterexample to universal memory use. |
| Web text/vision feedback and status parsing | `WebArena/autoeval/evaluate_trajectory.py`; `WebArena/autoeval/evaluator.py`; `WebArena/autoeval/prompts.py` | Direct reads: [EPI-RTE-web-check](#epi-rte-web-check). Vision dispatch exists but shipped evaluator CLI choices fail its GPT-only assertion; no operation established. |
| Web ordinary induction, gt alternate, awm/synapse | `WebArena/induce_memory.py`; `WebArena/prompts/memory_instruction.py` | Direct reads plus supplied [RT-RTE-web-admission](runtime.md#rt-rte-web-admission). Distinguishes replay from model induction; failures in success-only alternatives do not reject candidates on quality. |
| Web scaling | `WebArena/induce_scaling.py`; `WebArena/pipeline_scaling.py` | Direct induction read plus supplied [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling). No established distinct-trajectory contrast. |
| Vendored outcome evaluators | `third_party/webarena/evaluation_harness/evaluators.py`; `third_party/webarena/evaluation_harness/helper_functions.py` | Direct reads of string, URL, HTML, combination and routing; [EPI-RTE-benchmark-check](#epi-rte-benchmark-check). Installed BrowserGym consumption remains an external contract. |
| Standalone regrading | `WebArena/reeval_memevol_prompt.py`; `WebArena/webarena_patch.py` | Complete direct reads; [EPI-RTE-answer-regrading](#epi-rte-answer-regrading). Missing imported function blocks ordinary launch; no observed new scores. |
| Coding batch CLI and feedback | `third_party/src/minisweagent/run/mini_extra.py`; `third_party/src/minisweagent/run/extra/swebench.py` | Direct dispatch and lifecycle/check reads, supplied [RT-RTE-swe-task](runtime.md#rt-rte-swe-task), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission), new [EPI-RTE-swe-check](#epi-rte-swe-check). |
| Query-cache selection | `WebArena/memory_management.py`; `third_party/src/minisweagent/memory/memory_management.py` | Web selector directly inspected; coding selector located by search, lifecycle supplied by runtime. [EPI-RTE-query-selection](#epi-rte-query-selection) is restricted to web implementation. No all-selector validation claim. |
| Legacy standalone induction and evaluator | `third_party/src/minisweagent/memory/induce_memory.py`; `WebArena/utils/evaluator.py`; `WebArena/utils/evaluate_trajectory.py` | Direct induction imports/main and evaluator methods; evaluator caller searched. [EPI-RTE-legacy-induction](#epi-rte-legacy-induction). Differently rooted imports lack an established launch context; registered mini-extra dispatch does not launch this script. Append body is afforded, not an established end-to-end direct invocation. Older evaluator uses only last caption, unlike ordinary text route. Full legacy extraction and utility prompt contract unassessed; no all-entry-point equivalence conclusion. |
| Statistics utility | `SWE-Bench/compute_stats.py` | Complete direct read: adds API-call counters and prints sum divided by 500; not a task-success or advice-validity evaluator. |
| Other registered commands | `third_party/src/minisweagent/run/mini_extra.py` | Direct dispatch lists config, inspector, github-issue, swebench-single. Implementations not assessed here. Prevents a system-complete negative about alternate feedback or acceptance routes. |
| Provider state, other agents/adapters, benchmark annotations and config generation | `WebArena/agents/`; `WebArena/config_files/generate_config_files.py`; `third_party/src/minisweagent/models/`; `third_party/webarena/test.raw.json` | Provider internals inaccessible; ancillary implementations/annotation correctness unassessed. Prevents claims of pinned latent knowledge, evaluator annotation fidelity or exhaustive route completeness. Supplied model fixity findings remain see [RT-CMP-task-model](runtime.md#rt-cmp-task-model), [RT-CMP-gemini-embedding](runtime.md#rt-cmp-gemini-embedding), [RT-CMP-qwen-embedding](runtime.md#rt-cmp-qwen-embedding). |

Missing generated advice prevents individuating actual propositions and classifying their transformations. Missing traces prevent establishing actual evaluator decisions, advice activation and criticism-shaped iteration. Missing task/reference validation prevents treating benchmark predicates as ground truth about every intent. Missing controlled comparisons prevents attributing improvement, scaling synergy or transfer to memory. These are distinct limits, not evidence that the corresponding behavior never occurs.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-web-trajectory](#epi-obj-web-trajectory) | Task reports, page observations, thoughts, action history and terminal answer; commands themselves are not assertions | see record | SRC-1 `WebArena/autoeval/evaluate_trajectory.py` | Acquisition preserves copied text but loses steps/views; source-world warrant unknown. |
| [EPI-OBJ-autoeval](#epi-obj-autoeval) | Execution succeeded/failed, plus explanatory thoughts | see record | SRC-1 `WebArena/autoeval/evaluate_trajectory.py` | Verdict targets task execution, not advice transfer. |
| [EPI-OBJ-web-memory](#epi-obj-web-memory) | Possible procedural and causal claims in generated text, or policy-only advice | see record | SRC-1 `WebArena/induce_memory.py` | No generated instance; truth-apt content not determinable. |
| [EPI-OBJ-swe-memory](#epi-obj-swe-memory) | Possible coding strategy claims or prescriptions | see record | SRC-1 `third_party/src/minisweagent/run/extra/swebench.py` | Separate producer/evaluator and thinner provenance than web record. |
| [RT-CMP-task-model](runtime.md#rt-cmp-task-model) | Internal truth-apt units not determinable | see record | SRC-1 `third_party/src/minisweagent/run/extra/swebench.py` | Opaque service weights; no parameter-learning conclusion beyond inspected lack of update. |
| [RT-CMP-gemini-embedding](runtime.md#rt-cmp-gemini-embedding), [RT-CMP-qwen-embedding](runtime.md#rt-cmp-qwen-embedding) | None individuated in dense similarity vectors | see records | SRC-1 `WebArena/memory_management.py` | Selection carries ranking force, not truth certification. |

## Authority-route ledger

Each entry below is a function overlay, not a replacement declaration. Repeated functions on one citation separate production, disposition and retention. Owned fields are see the cited record. All operation evidence is uninspected unless expressly described as a static deduction.

Route ID: [EPI-RTE-web-check](#epi-rte-web-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-web-trajectory](#epi-obj-web-trajectory) → [EPI-OBJ-autoeval](#epi-obj-autoeval).
Content/update relation: truth-apt transformation: indeterminate. A model judges execution; generated rationale and its entailment are not supplied.
Transition or check target: Web task execution relative to intent, including completeness, grounding and exact target.
Evaluator/condition and domain: see record; text model over a bounded saved view, not a reference-answer oracle.
Activation and timing: see record; after task, before induction.
Possible or observed result: see record; true, false or null feedback, not an observed result here.
Implemented force: prompt selection and explanatory input, not item rejection.
Epistemic authority and scope: fallible evidence-consuming task judgment under the prompt criteria. It licenses neither the model's causal explanation nor future applicability of advice.
Operational authority: success/failure guidance selected; null follows failure branch.
Behavioral-authority path: induction consumes JSON rm/thoughts, enforcing branch selection for that induction invocation.
Evidence source ID and local anchor: SRC-1 `WebArena/autoeval/evaluate_trajectory.py`.
Claim IDs: [EPI-CLM-memory-learning](#epi-clm-memory-learning).
Mismatch marker: none; checking precedes generation of the advice it does not check.
Gap/limit: prompt-grounding requests are not guarantees; omitted observations limit checks.

Route ID: [EPI-RTE-swe-check](#epi-rte-swe-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: coding transcript → outcome label used for [EPI-OBJ-swe-memory](#epi-obj-swe-memory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: issue completion, not patch correctness against external tests or proposed advice validity.
Evaluator/condition and domain: see record; direct GenAI transcript judge followed by substring parser.
Activation and timing: see record; finally block after agent exit.
Possible or observed result: see record; Boolean label. Static counterexample: `unsuccessful` returns true because it contains `success`.
Implemented force: enforcing prompt switch, not semantic item admission criterion.
Epistemic authority and scope: transcript-based assessment only; parser can reverse the apparent meaning of a verdict. No independent test oracle is used by this judge.
Operational authority: permits success-guided advice generation for any returned string containing the substring.
Behavioral-authority path: batch runner → SUCCESSFUL_SI/FAILED_SI choice → generator for current instance.
Evidence source ID and local anchor: SRC-1 `third_party/src/minisweagent/run/extra/swebench.py`.
Claim IDs: [EPI-CLM-memory-learning](#epi-clm-memory-learning).
Mismatch marker: lexical result may not preserve judge meaning.
Gap/limit: no provider response, actual patch or benchmark grading supplied.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: task answer, page URL or selected HTML versus configured references.
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: final answer versus configured exact-match or inclusion references.
Evaluator/condition and domain: symbolic normalized string equality or token/substring inclusion. These warrant only the string predicates, conditional on the configured reference and extraction.
Activation and timing: evaluator router dispatches configured checks; actual host reward production unobserved.
Possible or observed result: score products; no observed score. Static clean-answer deduction is in record.
Implemented force: benchmark result production; subsequent gt reward consumption is separate.
Epistemic authority and scope: warrants checked predicates conditional on reference, extraction and environment fidelity. Does not establish all intent constraints, mechanism correctness or replay safety.
Operational authority: returns score and records diagnostic log; no advice rejection here.
Behavioral-authority path: evaluator result → host summary contract → gt induction branch, where configured; log alone has no inspected automatic revision consumer.
Evidence source ID and local anchor: SRC-1 `third_party/webarena/evaluation_harness/evaluators.py`.
Claim IDs: none.
Mismatch marker: none for these symbolic string predicates.
Gap/limit: no universal equivalence between benchmark reward and strict text autoevaluation.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: task answer and configured reference pieces or unachievability reason.
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: semantic reference-piece containment or agreement with an unachievable-task reason.
Evaluator/condition and domain: GenAI fuzzy and UA helper calls; distinct from symbolic exact/inclusion predicates.
Activation and timing: string evaluator fuzzy branch; N/A exact mismatch invokes UA. Actual checks unobserved.
Possible or observed result: model verdict parsed to 0 or 1; invalid responses can assert.
Implemented force: component score multiplication; UA branch can reset score.
Epistemic authority and scope: fallible model judgment relative to supplied references, not explanation or future-advice validity.
Operational authority: returns component score for combination; later gt branch depends on host summary contract.
Behavioral-authority path: helper → string evaluator → combined score → external host summary → configured gt induction.
Evidence source ID and local anchor: SRC-1 `third_party/webarena/evaluation_harness/helper_functions.py`; `third_party/webarena/evaluation_harness/evaluators.py`.
Claim IDs: none.
Mismatch marker: fuzzy class docstring says similar, but executable prompt checks reference-piece containment.
Gap/limit: correct reference and reliable model compliance unestablished.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: final page URL and configured reference URLs.
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: reference base-path inclusion and configured query-value inclusion in final URL.
Evaluator/condition and domain: URLEvaluator's deterministic URL parsing and membership predicates, not answer correctness.
Activation and timing: router selects url_match after task; actual check unobserved.
Possible or observed result: base score multiplied by required query scores, or error for unknown rule.
Implemented force: contributes numeric benchmark score.
Epistemic authority and scope: licenses the checked URL predicate, not satisfaction of every task-intent constraint.
Operational authority: feeds score combination; summary/gt consumer is conditional on host integration.
Behavioral-authority path: URL evaluator → combination → external summary contract → gt induction branch.
Evidence source ID and local anchor: SRC-1 `third_party/webarena/evaluation_harness/evaluators.py`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: actual page state and reference fidelity uncaptured.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: selected HTML/API content and configured required contents.
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: configured content in selected page/locator, not the agent's explanation.
Evaluator/condition and domain: HTMLContentEvaluator invokes locators/helpers, unescapes text and uses exact or inclusion tests.
Activation and timing: router selects program_html; navigation may open a temporary page, with wishlist limit adjustment. Actual check unobserved.
Possible or observed result: product of content scores; some locator failures substitute empty text.
Implemented force: benchmark score production; temporary page cleanup restores previous page, not advice rollback.
Epistemic authority and scope: warrants predicates on extracted text conditional on locator and reference fidelity; no mechanism/transfer warrant.
Operational authority: feeds score combination and conditional host reward consumption.
Behavioral-authority path: page/helper → selected text → content predicate → combination → external summary → gt induction.
Evidence source ID and local anchor: SRC-1 `third_party/webarena/evaluation_harness/evaluators.py`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: selected environment text is an acquired input with unknown source warrant; dynamic helpers, live page state and installed host integration not observed.

Route ID: [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-web-memory](#epi-obj-web-memory), [EPI-OBJ-swe-memory](#epi-obj-swe-memory).
Content/update relation: truth-apt transformation: indeterminate. Remaining possibilities: non-ampliative reshaping, entailed derivation, ampliative conjecture, or non-truth-apt policy output. Prompts request generalization and failure explanations; absent output cannot prove which relation a particular item has.
Transition or check target: task-conditioned advice generation, not an advice evaluator.
Evaluator/condition and domain: producer and guidance are see cited records.
Activation and timing: see cited records.
Possible or observed result: requested memory items; no output instance supplied.
Implemented force: model proposal; no semantic validation of claimed lessons.
Epistemic authority and scope: candidate formulation, not warranted novel claims. A one-task outcome does not entail a generally successful strategy or causal explanation.
Operational authority: generated strings enter append processing.
Behavioral-authority path: generator response → host splitter → bank append in current task; later task-model consumption is separate.
Evidence source ID and local anchor: SRC-1 `WebArena/induce_memory.py`; `third_party/src/minisweagent/run/extra/swebench.py`.
Claim IDs: [EPI-CLM-advice-transfer](#epi-clm-advice-transfer).
Mismatch marker: generalizability is requested, not checked.
Gap/limit: no candidate-specific proof of non-entailment or truth.

Route ID: [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see object records above.
Content/update relation: no content change.
Transition or check target: returned text → bank admission; no named semantic item-acceptance criterion.
Evaluator/condition and domain: code admits generated blocks if calls/I/O complete; proposal, veto and recovery are see records.
Activation and timing: see records.
Possible or observed result: append or call/I/O failure.
Implemented force: automatic admission, not evidence-consuming acceptance of an advice claim for a named scope.
Epistemic authority and scope: admission grants availability, not endorsement of truth or transfer.
Operational authority: newly generated text may be selected for later task prompts.
Behavioral-authority path: host append → bank → later selector; human starts workflow but does not approve each item.
Evidence source ID and local anchor: SRC-1 `WebArena/induce_memory.py`; `third_party/src/minisweagent/run/extra/swebench.py`.
Claim IDs: [EPI-CLM-advice-transfer](#epi-clm-advice-transfer).
Mismatch marker: task verdict is not advice acceptance.
Gap/limit: conditional gt is real outcome evidence, but labels the original trajectory before advice exists.

Route ID: [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: see object records above.
Content/update relation: no content change.
Transition or check target: generated blocks and metadata → JSONL.
Evaluator/condition and domain: see records; ordinary write processing, no quality check.
Activation and timing: see records.
Possible or observed result: durable append; no observed bank mutation.
Implemented force: retention.
Epistemic authority and scope: preserves candidates and available metadata, not their warrant.
Operational authority: bank available to subsequent task reload.
Behavioral-authority path: host filesystem bank → subsequent runner; horizon crosses tasks.
Evidence source ID and local anchor: SRC-1 `WebArena/induce_memory.py`; `third_party/src/minisweagent/run/extra/swebench.py`.
Claim IDs: [EPI-CLM-memory-learning](#epi-clm-memory-learning).
Mismatch marker: none.
Gap/limit: append-only inspected paths do not implement claim withdrawal or evidence integration after acceptance.

Route ID: [EPI-RTE-query-selection](#epi-rte-query-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-web-memory](#epi-obj-web-memory).
Content/update relation: no content change.
Transition or check target: cached query similarity and task-ID equality, not item truth or outcome label.
Evaluator/condition and domain: see record.
Activation and timing: see record; prior cache snapshot ranks before current cache append can participate.
Possible or observed result: top-ID bank match or empty selection.
Implemented force: ranking and deterministic selection.
Epistemic authority and scope: similarity supplies a relevance heuristic, no truth license. Failed-task advice remains eligible.
Operational authority: selects text for task context.
Behavioral-authority path: runner → memory text file → system-message channel; see [RT-BAP-system-memory](runtime.md#rt-bap-system-memory) for downstream force.
Evidence source ID and local anchor: SRC-1 `WebArena/memory_management.py`.
Claim IDs: [EPI-CLM-advice-transfer](#epi-clm-advice-transfer).
Mismatch marker: none.
Gap/limit: a top cache ID without bank match has no implemented fallback here.

Route ID: [RT-BAP-system-memory](runtime.md#rt-bap-system-memory)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: selected parts of web/coding memory objects.
Content/update relation: no content change.
Transition or check target: delivery to task model, not correctness certification.
Evaluator/condition and domain: relevance interpretation is delegated to the model; see record.
Activation and timing: see record.
Possible or observed result: delivered advice; no evidence of decision dependence.
Implemented force: see record.
Epistemic authority and scope: model-visible recommendation, without architecture-enforced warrant.
Operational authority: may change action choice, but does not itself authorize browser or shell effects.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `WebArena/agents/legacy/agent.py`; `third_party/src/minisweagent/agents/default.py`.
Claim IDs: [EPI-CLM-memory-learning](#epi-clm-memory-learning), [EPI-CLM-advice-transfer](#epi-clm-advice-transfer).
Mismatch marker: delivery is not compliance.
Gap/limit: executor/parser checks cover actions, not memory claim truth; see [RT-RTE-swe-task](runtime.md#rt-rte-swe-task).

Route ID: [RT-RTE-context-control](runtime.md#rt-rte-context-control)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: model-visible task observations and histories.
Content/update relation: truth-apt transformation: non-ampliative reshaping; code removes text, not semantic summaries.
Transition or check target: context-size heuristics and output length.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: reduced delivered view with potentially lost evidence.
Implemented force: code determines visible content.
Epistemic authority and scope: source-warrant preservation can be degraded by omission; no new warrant.
Operational authority: model receives bounded/altered view rather than complete underlying evidence.
Behavioral-authority path: prompt construction → task model per invocation; see record.
Evidence source ID and local anchor: SRC-1 `WebArena/agents/legacy/dynamic_prompting.py`; `third_party/src/minisweagent/config/extra/swebench.yaml`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: no whole-request fit invariant; sources can remain reachable outside delivered view.

Route ID: [EPI-RTE-legacy-induction](#epi-rte-legacy-induction)
Route function: retention
Architectural status: not determinable
Object/candidate ID: legacy generated memory text with query/trajectory/status metadata.
Content/update relation: no content change at append; model generation relation indeterminate.
Transition or check target: see record; legacy web-artifact feedback drives prompt choice.
Evaluator/condition and domain: reward equality selects prompt, not item endorsement.
Activation and timing: intended direct CLI; launch/import contract not established, see record.
Possible or observed result: intended generated-content append if import, client and input requirements are satisfied; no ordinary return established.
Implemented force: append body defines retention with software admission, but end-to-end invocation is unestablished.
Epistemic authority and scope: no independent advice warrant established by this route.
Operational authority: intended output bank could be available for compatible consumers; neither a completed append nor an automatic later consumer of this standalone output is established.
Behavioral-authority path: intended configurable output file; invocation and horizon beyond it depend on unresolved launch context and caller routing.
Evidence source ID and local anchor: SRC-1 `third_party/src/minisweagent/memory/induce_memory.py`.
Claim IDs: none.
Mismatch marker: directory name does not make this a SWE transcript judge.
Gap/limit: differently rooted memory.memory_management and instruction imports require an unestablished launch context. No standalone-script dispatch exists in the inspected mini-extra registration; source body alone does not establish direct launch.

Route ID: [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: intended combined-trajectory advice.
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: intended self-contrast of successes and failures.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: intended transferable advice; complete production route not established.
Implemented force: trial launches and repeated-directory input construction exist, but not the claimed distinct-trajectory synthesis.
Epistemic authority and scope: no comparative or causal license established.
Operational authority: intended bank update; executable completion unestablished.
Behavioral-authority path: intended generator → bank → ordinary selector; see record.
Evidence source ID and local anchor: SRC-1 `WebArena/induce_scaling.py`.
Claim IDs: [EPI-CLM-memory-scaling](#epi-clm-memory-scaling).
Mismatch marker: repeated directory and client-class call defeat inference from instructions to working comparison.
Gap/limit: the zero-reward success variable is not itself included in the assembled trajectories; it is not evidence that the generator receives an inverted explicit label.

Route ID: [EPI-RTE-answer-regrading](#epi-rte-answer-regrading)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: final answer versus configured reference parts.
Content/update relation: truth-apt transformation: indeterminate for model-backed regrading; normalization is non-ampliative reshaping.
Transition or check target: see record.
Evaluator/condition and domain: see record; intended containment-based grade.
Activation and timing: direct CLI after task, blocked at import in frozen code.
Possible or observed result: intended comparison JSON, no reachable ordinary result established.
Implemented force: implemented score/output code, unavailable ordinary invocation chain.
Epistemic authority and scope: intended predicate comparison, not acceptance of memory lessons or evidence of changed task behavior.
Operational authority: intended diagnostic output only; no bank revision consumer inspected.
Behavioral-authority path: JSON output and console to operator; no implemented automatic advice withdrawal.
Evidence source ID and local anchor: SRC-1 `WebArena/reeval_memevol_prompt.py`; `WebArena/webarena_patch.py`.
Claim IDs: none.
Mismatch marker: obsolete import.
Gap/limit: implementation exists but launch is not established; not an observed check.

No lifecycle-integration route is established for advice in the assessed ordinary append/selection chains: they retain and use it without a claim-specific acceptance step. This is not a system-complete absence across the unassessed registered commands.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-memory-learning](#epi-clm-memory-learning) | see record | SRC-1 `README.md`, doctrine/design | Success/failure prompts | [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission), [RT-BAP-system-memory](runtime.md#rt-bap-system-memory) | None supplied | No later behavioral-dependence trace or comparison | Automatic experience-conditioned retained advice supply is wired | Learning as improved capacity, exercised self-improvement and memory benefit unestablished |
| [EPI-CLM-memory-scaling](#epi-clm-memory-scaling) | see record | SRC-1 `README.md`, doctrine/design | PARALLEL_SI requests compare/contrast | [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling) | None supplied | No independent variation; source wiring does not supply distinct candidate contrast | Scaling intent and parallel trial affordance | Complete synthesis chain and bidirectional synergy unsupported |
| [EPI-CLM-advice-transfer](#epi-clm-advice-transfer) | see record | SRC-1 `WebArena/prompts/memory_instruction.py`; `third_party/src/minisweagent/memory/instruction.py`, doctrine/design | Explicit future-similar-task goal and failure reflection | [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission), [EPI-RTE-query-selection](#epi-rte-query-selection) | None supplied | Task outcome cannot identify causal mechanism or transfer | Candidate generation and relevance-ranked supply | No advice-specific evidence-consuming acceptance for a named use/scope in assessed chains |

## Bounded conclusion

ReasoningBank acquires task/environment reports and retains generated natural-language advice with task identifiers and queries. Web records also retain extracted think/action lists and a status; coding records retain less derivational context. Acquisition warrant is unknown for uncaptured environments; retained derivational context is partial, and selected agents receive advice text rather than its trajectory/evaluation evidence. Retention and use are not lifecycle integration after epistemic acceptance.

The ordinary web text judge has explicit task criteria and evidence-consuming evaluation: completeness, grounding and right target. Its limited view and model fallibility bound this license. The gt alternate provides a materially different configured-reference outcome source. Symbolic checks derive normalized predicate results within string/URL/HTML domains; none establishes source annotation truth or an induced mechanism. The coding judge instead sees a non-system transcript, with a substring parser that can classify `unsuccessful` as success. These are separate evaluator/authority findings, not one system-wide oracle assessment.

Induction requests reusable lessons, explanations and preventative strategies. No generated candidate is supplied, so actual truth-apt propositions and whether they are entailed, ampliative or policy-only are not determinable. The assessed ordinary routes neither test nor accept those propositions against evidence after generation. The task verdict selects a prompt; host code then appends its response. Similarity selection grants relevance-ranking force, and system-message injection grants advisory, model-mediated operational influence over the task horizon and across later tasks. Neither is a truth endorsement. Failure-related advice remains eligible; this is not simply a bank of success-certified facts.

Direct behavior adaptation is afforded through retained instructions even where an output is policy-only. Task evaluators and cache rankings have enforcing branch/selection force; advice interpretation remains model-mediated. No parameter update is inspected, exact provider weights remain unpinned, and opaque distributed-parametric state cannot be assigned proposition-level acceptance. Fixed task-model parameters would not negate retained-advice adaptation.

The supplied theory-builder assessment remains see [RT-RTE-web-admission](runtime.md#rt-rte-web-admission) and [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission): localized formulation is afforded; delivery does not establish content-dependent decisions; requested failure reflection does not establish claim-directed criticism/revision; accumulation does not establish criticism-shaped iteration. Learning, reflection, autonomous theory-building and self-improvement retain independent limits. In particular, evidence-conditioned update and later delivery are wired, but later causal dependence is unobserved, preventing exercised self-improvement attribution. Improved future capacity or successful improvement requires additional evidence independently.

The scaling instructions do not establish implemented distinct-trajectory comparison, standalone regrading has a frozen import defect, and standalone legacy induction affords an append body without an established launch/import contract. Cleanup of predictions/trajectory destinations in runtime routes is recovery plumbing, not withdrawal of warranted advice. The absence of advice acceptance/withdrawal is bounded to the inspected append/selection consumers; unassessed alternate commands prevent a system-complete negative. No single epistemic score or unqualified verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-web-trajectory
Label: Web trajectory evidence view

Part of: [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline)
The parent is a route container; this object is its material saved-trajectory input to feedback. Source-native identity: step pickle artifacts, `think_list`, `action_list`, `obs_list`, terminal `response`. Natural-language observations/thoughts/answers and symbolic action strings are separate operative parts; storage is compressed pickle files and extracted host lists. The evaluator sees page-text captions capped at 40,000 characters, fallback thoughts where observations are empty, at most five captions, and think/action history. It skips corrupt and actionless steps; this is partial imported evidence, not an authenticated complete browser trace. SRC-1 `WebArena/autoeval/evaluate_trajectory.py`; evaluator consumer see [EPI-RTE-web-check](#epi-rte-web-check).

> if not action:  # skip empty action steps
>     continue
> --- `WebArena/autoeval/evaluate_trajectory.py`

> MAX_OBS_CHARS = 40000
> captions_for_eval = [obs[:MAX_OBS_CHARS] if obs else think
>                      for obs, think in zip(obs_list, think_list)]
> --- `WebArena/autoeval/evaluate_trajectory.py`

#### EPI-OBJ-autoeval
Label: Saved task verdict and explanation

Part of: [RT-RTE-web-admission](runtime.md#rt-rte-web-admission)
Source-native identity: model-named autoeval JSON, `rm`, `thoughts`, `gt`. Symbolic Boolean/null rm and saved numeric gt are distinct from natural-language explanation; substrate is JSON file. rm controls prompt selection; thoughts can be copied into induction input. gt is saved separately, not an input reference answer to ordinary text judgment. This object is the parent admission route's feedback input, not another admission declaration. SRC-1 `WebArena/autoeval/evaluate_trajectory.py`; see [EPI-RTE-web-check](#epi-rte-web-check).

> "gt": traj_info["eval"],
> "rm": eval_result,
> "thoughts": out["thoughts"],
> --- `WebArena/autoeval/evaluate_trajectory.py`

#### EPI-OBJ-web-memory
Label: Web memory item text and derivational metadata

Part of: [RT-RTE-web-admission](runtime.md#rt-rte-web-admission)
Source-native identity: `memory_items`, query, task_id, think_list, action_list, status, template_id. Natural-language generated blocks and trajectory thoughts are separate from symbolic record keys/status and action strings; storage is append-only JSONL in the inspected writer. Generated semantic units need not coincide with blank-line blocks. No supplied instance establishes a proposition. The parent record already supplies append quotation; this declaration identifies its output object, not a duplicate route. SRC-1 `WebArena/induce_memory.py`. Induction receives think/action history and optionally model explanation, not the page observations supplied to the evaluator.

> trajectory = format_trajectory(ex["think_list"], ex["action_list"])
> trajectory = f"**Query:** {ex['query']}\n\n**Trajectory:**\n{trajectory}"
> --- `WebArena/induce_memory.py`

> trajectory += f"\n\nThe task {status_label} because: {autoeval_thoughts}"
> --- `WebArena/induce_memory.py`

#### EPI-OBJ-swe-memory
Label: Coding memory item text and outcome metadata

Part of: [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)
Source-native identity: model-named JSONL `memory_items`, task_id, query and status. Form: natural-language advice/query and symbolic identifier/status fields; substrate: JSONL. Parent record supplies append and system-message-omission evidence. This object is its output, not a duplicate route. Saved trajectory and prediction exist separately, but the bank record does not carry their contents or judge rationale. Actual item truth-apt content is not determinable without generated artifacts. SRC-1 `third_party/src/minisweagent/run/extra/swebench.py`.

> "task_id": instance_id,
> "query": task,
> "memory_items": generated_memory_item,
> "status": "success" if status else "fail",
> --- `third_party/src/minisweagent/run/extra/swebench.py`

### Routes

#### EPI-RTE-web-check
Label: Web execution feedback check

Part of: [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline)
Saved task artifacts → bounded evaluator prompt → model thoughts/status → Boolean/null JSON. Owner: autoeval driver and Evaluator. This is a check part of pipeline scheduling, distinct from the supplied admission route and from benchmark grading. Model proposes/decides semantic outcome; code parses and can produce null on evaluator errors; no human per-verdict veto. Target/domain: successful execution of information-seeking, navigation or modification tasks relative to intent and supplied views. Strict text guidance names completeness, grounding and right target and requires failure under uncertainty. No expected-answer oracle is passed to the model prompt. Mode: bounded task feedback; trigger is completed saved task or direct CLI. Vision consumes last image and action history, but CLI model choices do not satisfy its GPT-only assertion.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rm/thoughts/gt JSON, with true for parsed lowercase success, false otherwise, null on caught evaluation errors.
- Later read-back: ordinary induction reads rm and optionally thoughts; gt mode instead reads saved summary reward.
- Delegated visibility: text model sees intent, response, history and last five bounded captions; no reference-answer config or full underlying browser state.
- Selection predicate: line-start Thoughts/Status extraction, quote removal and lowercase equality to success.
- Invalidation or expiry: current model-named feedback file is overwritten; no advice withdrawal consumer is attached.
- Activation or effect: changes success/failure guidance and available explanatory induction input; actual decisions unobserved.
- Evidence limits: no verdict trace; error fallback and observation omission limit licensed judgments.

SRC-1 `WebArena/autoeval/evaluator.py`; `WebArena/autoeval/prompts.py`; `WebArena/autoeval/evaluate_trajectory.py`.

> last_caps = captions[-5:] if len(captions) >= 5 else captions
> --- `WebArena/autoeval/evaluator.py`

> Before calling a task successful, verify all three:
> - Completeness: every constraint in the intent is satisfied, and if the task implies an exhaustive result (a list, a range, an aggregate), the agent inspected the full source, not just the first page.
> - Grounding: every value, name, or URL the agent reports is traceable to a specific observation; values that were inferred, guessed, or summarized without a visible source count as failures.
> - Right target: when the task names a specific entity (a particular order, category, filter, product), confirm the agent acted on that exact entity and not an adjacent one.
> When uncertain on any of these, mark failure. A false success is more harmful than a false failure, because memory induction amplifies it into future behavior.
> --- `WebArena/autoeval/prompts.py`

> if out["status"].lower() == "success": eval_result = True
> else: eval_result = False
> --- `WebArena/autoeval/evaluate_trajectory.py`

> assert client == "gpt-4v" or client == "gpt-4o"
> --- `WebArena/autoeval/evaluator.py`

#### EPI-RTE-swe-check
Label: Coding transcript completion check

Part of: [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)
Non-system transcript/task → direct GenAI → lexical Boolean → induction prompt. Owner: batch `llm_judge_status`; separate check part of combined admission. Model proposes task-completion label, parser decides operative result; human configures run, no per-label approval. Domain: completion inferred from transcript, not independently graded patch. No answer oracle or external test result consumed. Trigger: agent exit inside bounded instance processing. There is no item-admission veto in this check; failure chooses failure generation rather than rejection. Recovery and provenance omission are see parent record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean from substring search after stripping/lowercasing model text.
- Later read-back: chosen outcome persists as bank status; later retrieval loads the record, without filtering on status.
- Delegated visibility: task and non-system transcript, not selected system advice or independent reference patch/test score.
- Selection predicate: any occurrence of success returns true, all other returned text false.
- Invalidation or expiry: inapplicable — check defines no prior-item revision or expiry.
- Activation or effect: selects success/failure generation instruction; observed judge behavior unavailable.
- Evidence limits: static `unsuccessful` and `not a success` both contain success; these deductions do not establish actual provider output.

SRC-1 `third_party/src/minisweagent/run/extra/swebench.py`; parent supplies predicate quotation.

> prompt = f"Task: {task}\n\nTrajectory:\n{trajectory}\n\nDid the agent successfully complete the task? Answer with 'success' or 'fail' only."
> --- `third_party/src/minisweagent/run/extra/swebench.py`

#### EPI-RTE-benchmark-check
Label: Configured WebArena outcome predicates

No counterpart after comparison with [RT-RTE-web-admission](runtime.md#rt-rte-web-admission): that route imports summary reward; this record identifies the vendored evaluator's producing predicates. Owner: evaluator router/combination and subclasses. Configured domain parts: final-answer normalized exact equality or token/substring inclusion; fuzzy containment of each reference piece; N/A equality or model agreement with unachievability reason; final URL base-path inclusion and configured query values; selected HTML/API-derived content exact/inclusion tests. Config supplies expected references; program/model decides scores. Humans supply configuration rather than per-result approval. Operating mode: configured benchmark task, not open-ended claim validation. No proposed memory change or item veto here. Combination multiplies scores; logs are diagnostic evidence, not a gate by themselves. Actual installed harness→summary link remains external and unobserved; gt consumer is see supplied admission record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: component and combined numeric scores plus gt_eval.jsonl diagnostics.
- Later read-back: gt induction consumes summary cumulative reward if host exposes these checks there; this mapping is an external contract, not an observed run.
- Delegated visibility: symbolic predicates see selected answer/URL/HTML and references; GenAI sees question/prediction/reference or actual/reported unachievable reasons.
- Selection predicate: config eval_types selects string_match, url_match or program_html; fuzzy helpers parse correct/incorrect/partially correct or same/different.
- Invalidation or expiry: inapplicable — evaluator returns/logs a score, not an advice update.
- Activation or effect: provides outcome evidence conditional on host wiring; no advice truth/transfer consumer established.
- Evidence limits: reference truth, annotation correctness, host integration and actual environment state not validated.

SRC-1 `third_party/webarena/evaluation_harness/evaluators.py`; `third_party/webarena/evaluation_harness/helper_functions.py`. Concrete deterministic deduction: clean_answer on a string with outer whitespace and a matched single-quote pair around `OK` strips whitespace, removes the pair and lowercases to `ok`; exact_match with reference `ok` returns 1. This warrants equality after normalization only, not truth of the answer. No target execution was used.

> answer = answer.strip()
> if answer.startswith("'") and answer.endswith("'"):
>     answer = answer[1:-1]
> elif answer.startswith('"') and answer.endswith('"'):
>     answer = answer[1:-1]
> return answer.lower()
> --- `third_party/webarena/evaluation_harness/evaluators.py`

> for evaluator in self.evaluators:
>     cur_score = evaluator(trajectory, config_file, page, client)
>     score *= cur_score
> --- `third_party/webarena/evaluation_harness/evaluators.py`

> message += "If the student's answer contains the reference information (possibly with different phrasing or wording), judge it as correct. Do NOT penalize the student for including extra information beyond the reference.\n"
> --- `third_party/webarena/evaluation_harness/helper_functions.py`

> ref_base_path in pred_base_paths
> --- `third_party/webarena/evaluation_harness/evaluators.py`

> possible_ref_value in pred_query.get(k, [])
> --- `third_party/webarena/evaluation_harness/evaluators.py`

> selected_element = html.unescape(selected_element)
> --- `third_party/webarena/evaluation_harness/evaluators.py`

> cur_score = StringEvaluator.exact_match(
>     ref=required_contents, pred=selected_element
> )
> score *= float(cur_score)
> --- `third_party/webarena/evaluation_harness/evaluators.py`

> if "partially correct" in response or "incorrect" in response:
>     return 0.0
> else:
>     assert "correct" in response
>     return 1.0
> --- `third_party/webarena/evaluation_harness/helper_functions.py`

#### EPI-RTE-query-selection
Label: Web query similarity selection

Part of: [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline)
Current query/prior embedding cache → similarity ranking → first bank record matching selected task ID → delivered memory items. Owner: selector and web runner. This is selection within the supplied pipeline, not another whole pipeline record. Model embeddings produce vectors; symbolic ranking and equality decide records. No human item veto, answer oracle, outcome-status filter or advice-semantic evaluator here. Mode: task-driven top-one selection in ordinary caller, not open-ended curation. The cache appends current query before scoring the previously loaded snapshot; selection can yield no corresponding bank record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected bank records or empty list/dict on inspected branches.
- Later read-back: current query embedding is appended for later tasks; selected retained bank text reaches current task agent.
- Delegated visibility: embedding calls see queries/instruction-prefixed current query, not candidate memory propositions.
- Selection predicate: instruction-aware Gemini similarity descending, first n IDs, first bank task_id match.
- Invalidation or expiry: no expiry or status-based withdrawal in inspected selector; append does not replace previous cache entries.
- Activation or effect: determines supplied memory, not observed compliance; cache can outrun bank after downstream admission failure.
- Evidence limits: cached model provenance/dimensional compatibility and actual ranking quality unestablished.

SRC-1 `WebArena/memory_management.py`; downstream consumer see [RT-BAP-system-memory](runtime.md#rt-bap-system-memory).

> for sid in top_ids:
>     # find the corresponding reasoning bank entry, with reasoning_bank["task_id"] == sid
>     for i, item in enumerate(reasoning_bank):
>         if item["task_id"] == sid:
>             out.append(reasoning_bank[i])
>             break
> --- `WebArena/memory_management.py`

#### EPI-RTE-legacy-induction
Label: Standalone legacy artifact induction

Distinct from [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission): this direct script consumes web-style result folders/feedback rather than saved coding messages. Owner: standalone main. Feedback reward selects success/failure instruction, model proposes generated memory, code appends automatically. Humans supply CLI parameters, no item approval. Expected reward can be imported via gt; autoeval supplies a model label. Mode: bounded direct artifact processing. Trigger: direct invocation; proposed change: memory text under unchanged guidance; call/I/O failures can prevent append, but no semantic item veto or rollback. Guidance requests success lessons/failure prevention. Actual theories not supplied. Theory-builder conditions 1–4: 1 afforded by item instructions; 2–4 uninspected because no decision-dependence, generated criticism/revision or iteration trace. Item-level addressability afforded; fine structure, learning, reflection and autonomy uninspected. Persistence is intended output-file availability; later configured consumer not established. Module-level imports use differently rooted namespaces, `memory.memory_management` and `instruction`; the inspected mini-extra dispatch and package script registration supply no launch contract for this standalone script. This establishes the append body, not a working direct invocation or a universal impossibility under caller-supplied import configuration.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: intended appended generated memory with query/trajectory/status/template metadata; unresolved launch/import context prevents asserting an ordinary return.
- Later read-back: uninspected — configurable output path has no established automatic downstream consumer in this direct invocation.
- Delegated visibility: formatted extracted think/action trajectory and query, not the ordinary coding non-system message stream.
- Selection predicate: reward equals 1 selects success instruction; all other values failure instruction.
- Invalidation or expiry: no expiry/replacement in inspected append main.
- Activation or effect: append body would write candidate advice if reached; end-to-end invocation and later behavior are unestablished.
- Evidence limits: differently rooted imports have no established launch context in inspected CLI/package registration; extraction/client compatibility and actual operation remain unassessed. No target execution was performed.

SRC-1 `third_party/src/minisweagent/memory/induce_memory.py`; `third_party/src/minisweagent/run/mini_extra.py`; `third_party/pyproject.toml`. This qualification agrees with the supplied refusal fragment's [MEM-RTE-standalone-induction](memory.md#mem-rte-standalone-induction); it describes the same standalone script rather than a distinct functioning launch route.

> from memory.memory_management import select_memory
> --- `third_party/src/minisweagent/memory/induce_memory.py`

> from instruction import SUCCESSFUL_SI, FAILED_SI
> --- `third_party/src/minisweagent/memory/induce_memory.py`

> mini-extra = "minisweagent.run.mini_extra:main"
> --- `third_party/pyproject.toml`

> for module_path, aliases, _ in subcommands:
>     if args[0] in aliases:
>         return import_module(module_path).app(args[1:], prog_name=f"mini-extra {aliases[0]}")
> --- `third_party/src/minisweagent/run/mini_extra.py`

> if reward == 1:
>     status = "success"
> else:
>     status = "fail"
> --- `third_party/src/minisweagent/memory/induce_memory.py`

> "memory_items": generated_memory_item,
> "template_id": ex["template_id"]
> --- `third_party/src/minisweagent/memory/induce_memory.py`

#### EPI-RTE-answer-regrading
Label: Standalone fuzzy answer regrading

No counterpart after comparison with [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline): separate post hoc CLI, not pipeline feedback/admission. Owner: regrading script. Intended endpoints: experiment.log final response + configured references + prior reward → alternative score → comparison JSON/console. Domain: reference-part containment, plus exact/must-include and N/A handling. Model/program judges, operator consumes diagnostics; no per-answer veto or automatic bank change. Mode: bounded post hoc comparison with dry-run extraction option. Expected answers are config references; no observed comparison or causal experiment. Frozen `webarena_patch.py` is a no-op with no `_memevol_llm_fuzzy_match` binding, while the script imports that binding at module scope. Thus ordinary launch is blocked before main; implemented scoring body is not a working end-to-end invocation. Vendored harness carries the lenient prompt directly, see [EPI-RTE-benchmark-check](#epi-rte-benchmark-check). No runtime correction is required: runtime explicitly left this ancillary path uninspected.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: intended rows of old/new scores, answer and reference; blocked import prevents asserting ordinary return.
- Later read-back: uninspected — comparison output has no inspected automatic downstream consumer.
- Delegated visibility: intended normalized final response/reference/intent, not full trajectories or memory claims.
- Selection predicate: task directories whose references contain fuzzy_match; dry_run skips model calls/output write.
- Invalidation or expiry: inapplicable — no bank mutation or prior advice withdrawal in intended reporting body.
- Activation or effect: intended operator-visible regrading; not observed and ordinary entry chain blocked.
- Evidence limits: source inspection establishes missing import binding, not an observed launch failure or real score change.

SRC-1 `WebArena/reeval_memevol_prompt.py`; `WebArena/webarena_patch.py`.

> from webarena_patch import _memevol_llm_fuzzy_match
> --- `WebArena/reeval_memevol_prompt.py`

> redundant; kept as a no-op only for import compatibility with run.py.
> --- `WebArena/webarena_patch.py`

### Claims

#### EPI-CLM-memory-learning
Label: Learning from successful and failed trajectories

No counterpart after comparison: supplied runtime declares no claims. SRC-1 `README.md`, doctrine/design. Claimed operation is experience-based memory learning, not a published causal result within this source register.

> We introduce ReasoningBank, a memory mechanism for agents that learns from both
> successful and failed trajectories, with reasoning stored as memory content.
> --- `README.md`

#### EPI-CLM-memory-scaling
Label: Memory and test-time scaling synergy

No counterpart after comparison: supplied runtime declares no claims. SRC-1 `README.md`, doctrine/design. Claimed operation: bidirectional memory/scaling synergy; linked paper is not registered evidence.

> Building upon this memory formulation, we propose memory-aware test-time scaling,
> which leverages the bidirectional synergy between memory and test-time scaling,
> establishing experience-driven memory as another scaling dimension for agent
> systems.
> --- `README.md`

#### EPI-CLM-advice-transfer
Label: Generalizable lessons for future similar tasks

No counterpart after comparison: supplied runtime declares no claims. SRC-1 `WebArena/prompts/memory_instruction.py`; `third_party/src/minisweagent/memory/instruction.py`, doctrine/design. Claimed intended role is reusable future guidance. Induction asks for explanatory reflection and preventative strategies, but there is no supplied generated instance or transfer check.

> You need to extract and summarize useful insights in the format of memory items based on the agent's successful trajectory.
> The goal of summarized memory items is to be helpful and generalizable for future similar tasks.
> --- `WebArena/prompts/memory_instruction.py`

> - You must first reflect and think why the trajectory failed, and then summarize what lessons you have learned or strategies to prevent the failure in the future.
> --- `third_party/src/minisweagent/memory/instruction.py`
