---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenRSI epistemic routes: executable task checks, score authority, model judgments and training-directed reliance."
run-id: AAS-2026-10-14-openrsi-c72dec9967a3-01
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI epistemic report

## Source-and-claim boundary

The question is what licenses reliance on OpenRSI's task packages, candidate programs, feedback, experience and training signals. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity is [its Source register](boundary.md#source-register). All added source inspection below is SRC-1, at the frozen revision, and supplies implementation evidence unless marked doctrine/design. No target code was executed. No supplied observed-run or causal-experiment source establishes activation or benefit.

The material distinction is between a program's task-relative outcome, a proposed explanation of that outcome, and a training or search decision. The release implements all three interfaces, but one interface does not warrant another. In particular, checking that a metric executes is not checking that it measures the intended task. A generated metric can itself become production evaluation machinery: see [RT-OBJ-metric](runtime.md#rt-obj-metric).

The consequential design claims are [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) and [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution). Neither is treated as an observed result.

### Coverage

| Entry point or operation | Source path in SRC-1 | Coverage and records | Limit and conclusion prevented |
| --- | --- | --- | --- |
| Gym CLI dispatch: prepare-input, build, overview, metric-check, evaluate, leaderboard | `OpenMLE-Gym/openmle_gym/cli.py` | Direct read of parser and dispatch; build supplied by [RT-RTE-gym-build](runtime.md#rt-rte-gym-build); evaluate and metric-check added below | prepare-input, overview internals and leaderboard internals not traced here; no complete assessment of metadata acquisition or source-warrant preservation |
| Gym graph and registered perception tools | `OpenMLE-Gym/builder_core/design.py` | Direct read of tool registration and graph routing; [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | Listing/CSV/text/save tools identified; full implementations and web scraping uninspected; no system-complete negative about import checks or tool-mediated factual changes |
| Code extraction and metric admission | `OpenMLE-Gym/builder_core/utils/nodes.py` | Direct extraction read; admission supplied by [RT-OBJ-metric](runtime.md#rt-obj-metric), [RT-RTE-gym-build](runtime.md#rt-rte-gym-build); [EPI-RTE-code-extraction](#epi-rte-code-extraction) | No semantic equivalence check for omitted explanation; compilation licenses syntax, not metric fidelity |
| Local package structure/metric evaluation | `OpenMLE-Gym/openmle_gym/metric_validation.py`, `OpenMLE-Gym/openmle_gym/local_evaluator.py` | Direct reads of metric loader/check, structure inspection, deterministic validation, model prompt/result normalization, report and failure consumers; [EPI-RTE-package-validation](#epi-rte-package-validation), [EPI-RTE-quality-judgment](#epi-rte-quality-judgment), [EPI-RTE-quality-disposition](#epi-rte-quality-disposition) | Raw-use-accounting helper and overview internals not fully assessed; no universal task-quality certification |
| Evo generation, execution, score parsing and island admission | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | Direct result-parser read supplements [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search), [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation) | External metric truth and deployed execution unverified; outcome cannot identify a change's causal mechanism |
| Evo rich summary creation/cache and preparation | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | Direct read of cache, normalization and preparation; [EPI-RTE-summary-generation](#epi-rte-summary-generation); later prompt supply also [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance) | Exact meaning of any generated summary unobserved; no accepted explanatory experience established |
| Async commits, local/Docker/SCM NatureBench and final-submit alternatives | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py` | Supplied [RT-RTE-async-search](runtime.md#rt-rte-async-search), [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution) | Backend/reference implementations not fully inspected; no common isolation or independent final-test guarantee |
| SFT data selection and numerical training | `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`, `OpenMLE-ERL/SFT/slime/train.py` | Supplied [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-CMP-training-models](runtime.md#rt-cmp-training-models) | Detailed intermediate row transformations not independently inspected here; no full corpus lineage, exact checkpoint warrant or causal training benefit |
| RL generation/reward hooks, anti-hack judge and database admission | `OpenMLE-ERL/RL/generate_mle.py`, `OpenMLE-ERL/RL/reward_func_utils.py` | Direct check and penalty branches; supplied [RT-RTE-rl-training](runtime.md#rt-rte-rl-training); [EPI-RTE-hack-judgment](#epi-rte-hack-judgment), [EPI-RTE-hack-disposition](#epi-rte-hack-disposition) | Score-to-reward shaping and database selector internals not fully inspected; no invariant that later parents exclude flagged programs; upstream RL optimizer unavailable |
| Public warrant statements | `README.md` | Direct stack table read and supplied [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | Reported benchmark comparisons are not registered causal experiments |

External weights, corpora, task releases, reference data and services are absent from this evidence set, as boundary records. Those gaps prevent independent verification of task truth, historical lineage and deployment. Available but uninspected prompts, skills, metadata tools, reward mappings and quality branches remain named coverage limits, not evidenced absences. This report therefore makes route-local conclusions, not a system-complete negative about knowledge production.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-metric](runtime.md#rt-obj-metric) | Executable scoring rule; its fidelity to task intent is truth-apt, whereas source code also carries executable policy | see record | see record | Syntax and execution checks do not establish construct validity |
| [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | Imported task information, generated description and preparation artifacts; operative parts of this route | see record | see record | Import warrant unknown; generated description's semantic relation to source not determinable without candidate instances |
| [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search) | Candidate code, plan and node analysis are distinct from observed metric fields | see record | see record | Program is an executable proposal; claims about its effect need task evidence, not its name or fluent plan |
| [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation) | Scalar task score, validity fields and execution feedback | see record | see record | Protocol can instead use printed score/model fallback; no universal warrant channel |
| [EPI-OBJ-task-evaluation](#epi-obj-task-evaluation) | File/CSV facts, validation findings, quality reasons, issues and recommendation | see record | see record | Deterministic evidence and model opinion have different licenses |
| [EPI-OBJ-hack-verdict](#epi-obj-hack-verdict) | Whether code learns from data/cheats; optionally whether a printed score comes from holdout evaluation | see record | see record | Judgment can be bypassed or fail open; source review is not execution verification |
| [EPI-OBJ-rich-summary](#epi-obj-rich-summary) | Method overview and parent-comparison experience | see record | see record | Nonempty fields suffice for storage; no truth/entailment check identified in normalization |
| [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) | Selected conversation/code examples and score metadata | see record | see record | Dataset admission is acceptance for training use, not acceptance of every explanatory proposition in a trace |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | Programs, categories, outcome/reward metadata | see record | see record | Database membership includes penalized categories |
| [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm), [RT-CMP-openai-provider](runtime.md#rt-cmp-openai-provider), [RT-CMP-training-models](runtime.md#rt-cmp-training-models) | Individual propositions in distributed parameters not determinable from accessible evidence | see records | see records | Training mutability differs from inference; exact weights and their propositional content unavailable |

## Authority-route ledger

Each row below is one consequential function, not a declaration of another referent. Repeated record citations split checking, disposition, retention and use without conflating them. `see` delegates the record-owned endpoint, evidence and consumer details; the content/update classification and architectural status are this overlay's assessment. SRC-1 is the source throughout.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | External task information entering build | see record | see record | see record | see record | Source warrant unknown; no independent authentication established here | see record | see record | see record | [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | none | Scrape/tool internals not assessed |
| [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Description/preparation/metric generated from selected inputs | see record | see record | see record | see record | Candidate construction only; preservation, derivation and conjecture not distinguished for unseen instances | see record | see record | see record | [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | none | Need source/output comparison to settle relation |
| [EPI-RTE-code-extraction](#epi-rte-code-extraction) | content transformation | implemented | [RT-OBJ-metric](runtime.md#rt-obj-metric) | non-truth-apt policy/content update: select executable code from a model response | see record | see record | see record | see record | see record | No new factual warrant; rationale can be omitted | see record | see record | see record | none | none | Not lossless rewriting of the full response |
| [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | disposition/acceptance | implemented | [RT-OBJ-metric](runtime.md#rt-obj-metric) | no content change | Generated metric/preparation admission | see record | see record | see record | see record | Local syntax/file-layout acceptance for executable use, not task-semantic acceptance | see record | see record | see record | [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | none | Metric becomes evaluator before comprehensive semantic validation is established |
| [EPI-RTE-package-validation](#epi-rte-package-validation) | check/evidence production | implemented | [EPI-OBJ-task-evaluation](#epi-obj-task-evaluation) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | File/CSV predicates and finite sample score under loaded metric; conditional on parser and package data | see record | see record | see record | [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | none | Does not establish prediction quality or metric fidelity |
| [EPI-RTE-quality-judgment](#epi-rte-quality-judgment) | check/evidence production | implemented | [EPI-OBJ-task-evaluation](#epi-obj-task-evaluation) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Evidence-conditioned model assessment; not proof of semantic correctness | see record | see record | see record | [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | none | Need actual outputs to distinguish faithful summary, derivation and unsupported novelty |
| [EPI-RTE-quality-disposition](#epi-rte-quality-disposition) | disposition/acceptance | implemented | [EPI-OBJ-task-evaluation](#epi-obj-task-evaluation) | no content change | see record | see record | see record | see record | see record | Accepts report structure and rating domain, not factual validity of every issue | see record | see record | see record | [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | none | Advisory recommendation is not enforced task promotion |
| [EPI-RTE-quality-disposition](#epi-rte-quality-disposition) | retention | implemented | [EPI-OBJ-task-evaluation](#epi-obj-task-evaluation) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | JSON/CSV retention preserves reported status, not endorsement of source truth | see record | see record | see record | none | none | No lifecycle integration of accepted ampliative claims established |
| [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation) | check/evidence production | implemented | see record | truth-apt transformation: acquisition/import | Task result returned from configured backend | see record | see record | see record | see record | Warrant conditional on selected data/metric/protocol; unknown independently | see record | see record | see record | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Model-printed and model-analyzed channels are not independent measurement |
| [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search) | operational admission/selection/consumption | implemented | see record | no content change | Validity/fitness, island admission, Debug and successor selection | see record | see record | see record | see record | Comparative score licenses bounded search choice, not a causal explanation or transferable method | see record | see record | see record | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Island average differs from parent-improvement criterion |
| [RT-RTE-async-search](runtime.md#rt-rte-async-search) | disposition/acceptance | implemented | see record | no content change | Commit after budget check | see record | see record | see record | see record | Budget eligibility only | see record | see record | see record | none | none | Completed evaluation can be rejected without epistemic refutation |
| [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution) | operational admission/selection/consumption | implemented | see record | no content change | Aggregate outcome/final selection | see record | see record | see record | see record | Task-relative aggregate; final score may reuse search evidence | see record | see record | see record | none | none | No universally independent post-search confirmation |
| [EPI-RTE-hack-judgment](#epi-rte-hack-judgment) | check/evidence production | implemented | [EPI-OBJ-hack-verdict](#epi-obj-hack-verdict) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Textual code review against explicit rubric; permissive fallback has no positive evidential warrant | see record | see record | see record | none | none | Genuine holdout behavior cannot be certified by this code review alone |
| [EPI-RTE-hack-disposition](#epi-rte-hack-disposition) | disposition/acceptance | implemented | [EPI-OBJ-hack-verdict](#epi-obj-hack-verdict) | no content change | see record | see record | see record | see record | see record | Acceptance for continuing to sandbox, not theorem that code is legitimate | see record | see record | see record | none | none | Flagged code can still enter database |
| [EPI-RTE-summary-generation](#epi-rte-summary-generation) | content transformation | implemented | [EPI-OBJ-rich-summary](#epi-obj-rich-summary) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Unverified candidate account; no entailment or non-entailment established for unseen output | see record | see record | see record | none | none | Parent comparison does not isolate causal component effects |
| [EPI-RTE-summary-generation](#epi-rte-summary-generation) | retention | implemented | [EPI-OBJ-rich-summary](#epi-obj-rich-summary) | no content change | see record | see record | see record | see record | see record | Presence/nonempty fields, not evidence-consuming truth acceptance | see record | see record | see record | none | none | Persistence and later supply are not lifecycle integration after acceptance |
| [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance) | operational admission/selection/consumption | implemented | see record | no content change | Model-visible feedback/experience | see record | see record | see record | see record | Advisory candidate knowledge; model compliance and causal reliance unobserved | see record | see record | see record | none | none | Delivery is not acceptance |
| [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) | disposition/acceptance | implemented | see record | no content change | Scored traces admitted to training dataset | see record | see record | see record | see record | Explicit proxy criteria license training-example use within selected tasks | see record | see record | see record | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Top score and validation/test gap do not warrant explanatory content |
| [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) | behavior/policy adaptation | implemented | [RT-CMP-training-models](runtime.md#rt-cmp-training-models) | non-truth-apt policy/content update: numerical actor/rollout weight update | see record | see record | see record | see record | see record | Individual accepted propositions in weights not determinable | see record | see record | see record | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | No historical training-to-serving causal chain |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | retention | implemented | see record | no content change | Conditional database insertion | see record | see record | see record | see record | No success/trust license from membership | see record | see record | see record | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Reward and retention are distinct channels |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | behavior/policy adaptation | implemented | [RT-CMP-training-models](runtime.md#rt-cmp-training-models) | non-truth-apt policy/content update: reward returned to external training machinery | see record | see record | see record | see record | see record | Objective-directed training signal, not acceptance of a proposition | see record | see record | see record | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Hook wiring inspected; upstream optimizer and actual update not established |

The direct parser inspection qualifies a tempting universal interpretation of [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation): with experience disabled, Analyze runs for every node, not merely missing deterministic metadata. Deterministic finite fitness then overrides its metric and bug flag. With experience enabled, deterministic fitness and failure metadata precede fallback analysis. The supplied runtime account already mentions the fallback but its route shorthand must not be read as excluding the legacy always-analyze branch. No supersession is needed: the same route supports multiple conditions. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

> if not experience_enabled:
>     # Preserve the inference AIRA-Evo path: call analyze for every node,
>     # then let deterministic validation fitness override the metric.
>     response = run_legacy_analyze()
>     if validation_fitness is not None:
>         response["metric"] = validation_fitness
>         response["is_bug"] = False
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-verifiable-packages](#epi-clm-verifiable-packages) | see record | see record | see record | [RT-RTE-gym-build](runtime.md#rt-rte-gym-build), [EPI-RTE-package-validation](#epi-rte-package-validation), [EPI-RTE-quality-judgment](#epi-rte-quality-judgment), [EPI-RTE-quality-disposition](#epi-rte-quality-disposition) | None supplied | No package execution or calibrated judge comparison; generated metric can be wrong while returning a finite score | Executable, locally inspectable packages with deterministic checks and optional evidence-conditioned semantic review | Broad semantic verifiability exceeds these checks if interpreted as established correctness; no contradiction with the narrower operational claim |
| [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | see record | see record | see record | [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search), [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | None supplied | Missing exact traces, checkpoints, deployment and comparisons; Max changes more than the model according to supplied boundary/runtime limits | Separately runnable search, selection and training-directed update paths | Exercise, causal improvement and general RSI remain unestablished; the source itself disclaims solving general RSI |

## Bounded conclusion

**Task checks have real but narrow authority.** Gym does more than compile generated metrics: the CLI exposes deterministic structure/CSV checks, sample-submission execution and optional semantic model review. Those omitted-from-baseline details matter. They can fail validation, suppress model judging through a hard gate, populate evidence-bearing reports and change CLI success status. The sample score is a smoke test, not model performance evidence. The semantic judge receives code and concrete package evidence, but report-schema acceptance checks strings and rating domains rather than proving every cited issue. Recommendation remains advisory in the inspected consumer chain. See [EPI-RTE-package-validation](#epi-rte-package-validation), [EPI-RTE-quality-judgment](#epi-rte-quality-judgment), [EPI-RTE-quality-disposition](#epi-rte-quality-disposition).

**Search grants operational reliance before explanatory acceptance.** Task outcomes can admit programs, trigger Debug, rank/select parents and select final output. These decisions are conditional on metric/data/protocol and score-source configuration, including model-printed scores, model analysis, test-score override and NatureBench search-score reuse. They license choices within the experiment, not warranted causal explanations or transfer. Async budget rejection is administrative, not falsification. See [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation), [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search), [RT-RTE-async-search](runtime.md#rt-rte-async-search), [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution).

**Judgment, rejection and retention diverge in RL.** A source-review model checks explicit cheating and holdout criteria before execution. Negative categories receive penalties and bypass normal sandbox execution, yet several are still stored. Some judge failures permit continuation, so a `valid` result is not always evidence that a judgment occurred. Missing configuration is a separate exception, not covered by that permissive result. Neither passing nor database membership certifies code truth or future reusable quality. See [EPI-RTE-hack-judgment](#epi-rte-hack-judgment), [EPI-RTE-hack-disposition](#epi-rte-hack-disposition), [RT-RTE-rl-training](runtime.md#rt-rte-rl-training).

**Retained prose is candidate experience.** Rich summaries can describe methods and parent comparisons, survive in cache and be prepared for later model inputs. The inspected admission rule checks two nonempty fields. It does not check semantic preservation or establish a produced accepted ampliative claim. The summaries may contain derivation, reshaping or conjecture; concrete outputs are required to distinguish them. No lifecycle integration after truth-apt acceptance is established by these cache operations. This is a route-local limit, not a system-wide absence. See [EPI-RTE-summary-generation](#epi-rte-summary-generation), [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance).

**Training adaptation is separately supported.** SFT selection admits traces against score, feedback, length, gap and top-k criteria for intended training use; actor/rollout numerical updates are wired. RL returns an outcome-derived signal to externally owned optimizer machinery. Neither creates inspectable accepted propositions in weights by implication. Training improvement, learned capacity, reliable reflection and formulated content-directed theory criticism are independent questions, not consequences of a score or summary. A dispositional improvement-directed parameter-update path exists; exercised self-improvement cannot be attributed without the live deployment and subsequent causal-dependence links named by [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) and [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution). Provider parameters and training corpora remain opaque. No single epistemic score or unqualified system-wide verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-task-evaluation
Label: Task evaluation report

Source-native identity: per-task result dictionaries, `all_results.json` and `evaluation_summary.csv` from `local_evaluator.evaluate_tasks`. Natural-language quality reasons/issues and symbolic file facts, scores/statuses are distinct fields in filesystem JSON/CSV. The deterministic fields state package-relative facts; model reasons are interpretations. Compared with [RT-OBJ-metric](runtime.md#rt-obj-metric), this is a report about packages/metrics, not the executable metric. No counterpart is declared in the supplied runtime. SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py`.

> results = _chunked_map(prepared, worker_count, evaluate_one_safe)
> combined_path = output_path / "all_results.json"
> summary_path = output_path / "evaluation_summary.csv"
> atomic_write_json(combined_path, results)
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

#### EPI-OBJ-hack-verdict
Label: Hack check verdict

Source-native identity: `(is_valid, category, reason)` returned by `hack_check_async` and its completion parser, consumed by reward code. Symbolic bool/category plus natural-language reason, held in Python values and copied into sample/log/database-related metadata. Unlike the score in [RT-RTE-rl-training](runtime.md#rt-rte-rl-training), this is a pre-execution source-review result. It is a material object inside that route, not a duplicate route. SRC-1, `OpenMLE-ERL/RL/reward_func_utils.py`, `OpenMLE-ERL/RL/generate_mle.py`; passages in [EPI-RTE-hack-judgment](#epi-rte-hack-judgment) and [EPI-RTE-hack-disposition](#epi-rte-hack-disposition).

Part of: [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

The cross-kind parent is the containing training workflow, which creates and consumes this value.

#### EPI-OBJ-rich-summary
Label: Rich summary

Source-native identity: `rich_summary` with `method_overview` and `parent_comparison_experience`, attached to nodes/cards and JSON cache. Natural-language content in a symbolic keyed container on filesystem/in-memory nodes. Distinct from the executing program and its scalar score in [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search). SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`; passages in [EPI-RTE-summary-generation](#epi-rte-summary-generation).

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

The cross-kind parent is the search workflow retaining this summary object.

### Routes

#### EPI-RTE-code-extraction
Label: Code output extraction

Part of: [RT-RTE-gym-build](runtime.md#rt-rte-gym-build)

Endpoints: raw model message → `_clean_code_output` → explanation/code tuple → preparation or metric admission. Owner: deterministic Python; state is one response string. This is a proper transformation part of the supplied build route, not another build referent. Form: natural-language response selected into symbolic executable source. SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`.

- Immediate return: stripped explanation and last tagged/fenced code block; missing complete wrapper raises.
- Later read-back: inapplicable — extractor itself does not retain accumulated material; its caller writes code under the containing build route.
- Delegated visibility: downstream compilation/execution receives extracted code, not the whole explanation.
- Selection predicate: last `<code>` opener with closing tag takes precedence; otherwise last recognized code fence.
- Invalidation or expiry: malformed wrappers raise an exception; no truth check or rollback here.
- Activation or effect: changes which text can become executable machinery; no model execution observed.
- Evidence limits: static deduction from string operations, not a target run; says nothing about generated code correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction: input `reason <code>x = 1</code> ignored <code>x = 2</code>` returns explanation `reason <code>x = 1</code> ignored` and code `x = 2`. The earlier program and trailing prose do not reach the code consumer. This is code selection, not warranted entailment or lossless reshaping of the full message.

> message = message.strip()
> if "<code>" in message and "</code>" in message:
>     parts = message.rsplit("<code>", 1)
>     think = parts[0].strip()
>     code = parts[1].split("</code>", 1)[0].strip()
>     return think, code
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

#### EPI-RTE-package-validation
Label: Package validation

Endpoints: `metric-check` or `evaluate` task package → metric loader/CSV inspection → finite sample score and deterministic findings/status. Owner: local validation code; task metric supplies executable scoring, not an independent semantic oracle. Targets are required files, CSV structure/row counts/identifier correspondence, target columns in public test data and metric execution/finiteness. This extends rather than duplicates [RT-RTE-gym-build](runtime.md#rt-rte-gym-build): separately invoked post-build inspection, not the build graph's success flags. SRC-1, `OpenMLE-Gym/openmle_gym/metric_validation.py`, `OpenMLE-Gym/openmle_gym/local_evaluator.py`, `OpenMLE-Gym/openmle_gym/cli.py`.

- Immediate return: metric class/score/row counts, or exception; evaluate collects findings with passed/failed status.
- Later read-back: results persist through [EPI-RTE-quality-disposition](#epi-rte-quality-disposition); independent later reliance is uninspected — no report-consuming later run supplied.
- Delegated visibility: metric receives submission and private-answer frames; model review receives selected evidence/code, not full raw data.
- Selection predicate: program predicates create findings; a finite numeric score is mandatory; any deterministic finding marks validation failed.
- Invalidation or expiry: errors become failure findings or worker failure; no task-package withdrawal or deletion is established by this evaluator.
- Activation or effect: validation selects hard-gate/model-review path and contributes to CLI failure status; no execution observed.
- Evidence limits: these are checked predicates over files under parser/metric assumptions; private labels and metric semantics remain unverified.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Computation decides validation; operator chooses task/mode, without per-finding approval. The bounded package check's reference outcome is expected local structure and the task's own answer/metric pair. This is not a model-quality benchmark. Recovery is rerunning after package correction; automatic semantic repair is not established here.

> if hasattr(metric, "validate_submission"):
>     metric.validate_submission(y_pred, y_true)
> score = json_safe(metric.evaluate(y_true=y_true, y_pred=y_pred))
> --- `OpenMLE-Gym/openmle_gym/metric_validation.py`

> return {
>     "status": "failed" if findings else "passed",
>     "findings": findings,
> }
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

#### EPI-RTE-quality-judgment
Label: Task semantic judgment

Endpoints: successful deterministic validation → `_evaluate_with_ai` evidence payload → configured OpenAI-compatible or Anthropic model → structured scores/reasons/issues. Owner: caller chooses branch; model proposes judgment. Target/domain: semantic validity, data sufficiency, raw use, complexity and quality of the represented constructed package, not the original competition. Distinct from [RT-RTE-gym-build](runtime.md#rt-rte-gym-build): separately exposed evaluation model call, no supplied counterpart. State is task report and selected evidence. SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py`.

- Immediate return: parsed model quality result, then report normalization by [EPI-RTE-quality-disposition](#epi-rte-quality-disposition).
- Later read-back: uninspected — report persistence is wired, but no subsequent model consumption of a retained quality report supplied.
- Delegated visibility: description, preparation and metric code, metric smoke result, processed/raw CSV summaries, raw inventory and accounting; previews are truncated and full data are not supplied.
- Selection predicate: optional model branch only when LLM judging is not skipped and validation has not failed; configured provider selects model.
- Invalidation or expiry: exceptions mark quality evaluation failed; deterministic failure uses zero-valued hard gate instead of invoking model.
- Activation or effect: opinion can populate report/recommendation; semantic compliance with prompt is unobserved.
- Evidence limits: rubric and evidence delivery implemented; model accuracy, calibration and independent causal validity untested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The judging service is distributed-parametric external state, not one of the Gym construction clients merely because it also generates text. No parameter update is requested here; provider internals uninspected. Exact weights are not pinned by model alias; configurable model/provider can change resolution. Human chooses configuration, model judges, report code can reject malformed output. No independently checked expected-answer oracle adjudicates semantic ratings.

> - sample_submission.csv intentionally contains random schema-valid predictions. Its metric score is only an execution and finiteness smoke test, never a model-quality baseline. Do not penalize a low or high sample score.
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

> - State a major issue only when it is supported by a concrete file, code fragment, or deterministic statistic in the supplied evidence.
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

#### EPI-RTE-quality-disposition
Label: Quality report disposition

Endpoints: deterministic status/model result → hard gate or `_validate_ai_quality` → per-task/combined JSON and summary CSV → `evaluation_has_task_failures` → CLI status. Owner: report code. Distinct from [RT-RTE-gym-build](runtime.md#rt-rte-gym-build): report acceptance/retention and CLI outcome, not construction admission. This owns report disposition separately from model checking in [EPI-RTE-quality-judgment](#epi-rte-quality-judgment). SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py`, `OpenMLE-Gym/openmle_gym/cli.py`.

- Immediate return: normalized report with averaged overall score and threshold recommendation, skipped status, hard-gate result, or failed-quality status; output paths returned to CLI.
- Later read-back: combined JSON is read by failure-status helper in the current command; uninspected — no separate later invocation consuming retained recommendations supplied.
- Delegated visibility: CSV renders scores/recommendation, issue messages/evidence and validation/evaluation status; full structured issues remain in JSON.
- Selection predicate: rating numbers finite in 0–5, nonempty reasons; major issues need required strings, allowed severity and evidence-source name. Mean at least 4 recommends, at least 2.5 is conditional, otherwise not recommended.
- Invalidation or expiry: schema failure yields failed evaluation; deterministic failed validation yields hard gate unless skipped; report writes can fail. No automatic package deletion/rollback or deployment veto based solely on recommendation found in inspected chain.
- Activation or effect: reports retained for operator inspection; task-process, validation or quality-execution failure changes command failure result; low semantic score alone is not checked by failure helper.
- Evidence limits: report normalization accepts shape, not evidence-to-claim correspondence. Advisory recommendation differs from enforced success status.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Software accepts/rejects report form for reporting use; operator may judge products outside this path. No per-report human approval. Hard gating and CLI failure enforce local processing requirements; semantic recommendation is advisory over the represented package. Evidence-bearing issues are not automatically accepted knowledge claims. Re-evaluation can replace reports; no historical truth-maintenance mechanism established here.

> overall = round(sum(scores) / len(scores), 2)
> if overall >= 4:
>     recommendation = "recommended"
> elif overall >= 2.5:
>     recommendation = "conditional"
> else:
>     recommendation = "not_recommended"
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

> return any(
>     isinstance(result, dict)
>     and (
>         result.get("task_process_failed") is True
>         or result.get("validation", {}).get("status") == "failed"
>         or result.get("quality_evaluation", {}).get("status") == "failed"
>     )
>     for result in combined
> )
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

#### EPI-RTE-hack-judgment
Label: Hack source judgment

Part of: [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

Endpoints: generated nonempty code with required printed-score marker if enabled → `hack_check_async` → model completion parser → verdict tuple. Owner: reward hook invokes model judge; parser handles return. This proper part expands the containing route's pre-execution checks. Target is whether code genuinely learns from supplied data versus listed guessing/constant/rule/trivial/no-training patterns; with self-validation enabled, whether claimed final validation really uses holdout rather than train/leaked/CV/proxy values. Source review, not proof or runtime attestation. SRC-1, `OpenMLE-ERL/RL/reward_func_utils.py`, `OpenMLE-ERL/RL/generate_mle.py`.

- Immediate return: valid/hack/hack_verify plus reason, or permissive valid fallback; absent key/base URL raises before protected API block.
- Later read-back: verdict metadata enters [EPI-RTE-hack-disposition](#epi-rte-hack-disposition); later use of reasons uninspected — database selection internals not traced here.
- Delegated visibility: judge receives rubric and generated code, not executed traces or full task datasets.
- Selection predicate: model is asked for JSON validity/category/reason; parser defaults missing is_valid to true, normalizes invalid categories and treats malformed JSON/empty response permissively.
- Invalidation or expiry: bounded API retry; absent SDK/runtime and caught API exceptions return valid; missing credentials are a separate raised condition.
- Activation or effect: negative verdict can block normal sandbox evaluation and change training penalty; actual judgment accuracy unobserved.
- Evidence limits: configurable external distributed-parametric judge, default model alias o3-mini, no exact weights; no update requested, mutable endpoint can resolve differently, provider internals uninspected. Model review is not an independent answer oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operator supplies credentials/configuration, model proposes verdict, parser/consumer decides consequences. The rubric supplies concrete holdout criticism criteria but implementation alone does not establish that such criticism occurred or that it reliably detects cheating.

> if content is None:
>     logger.error("Empty response from GPT API in hack_check")
>     return True, "valid", "GPT API returned empty response"
> --- `OpenMLE-ERL/RL/reward_func_utils.py`

> except json.JSONDecodeError as exc:
>     logger.error("Failed to parse GPT response in hack_check: %s", content)
>     return True, "valid", f"Failed to parse GPT response: {str(exc)}"
> --- `OpenMLE-ERL/RL/reward_func_utils.py`

> if not GPT_API_KEY:
>     raise RuntimeError("Missing GPT_API_KEY")
> if not GPT_BASE_URL:
>     raise RuntimeError("Missing GPT_BASE_URL")
> --- `OpenMLE-ERL/RL/reward_func_utils.py:325-336`

#### EPI-RTE-hack-disposition
Label: Hack verdict disposition

Part of: [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

Endpoints: extracted code/marker/verdict → reward category → bypass or sandbox execution → penalty/status metadata and storage decision. Owner: `reward_func` Python branches. This is disposition, distinct from the checking subroute [EPI-RTE-hack-judgment](#epi-rte-hack-judgment). SRC-1, `OpenMLE-ERL/RL/generate_mle.py`.

- Immediate return: empty code gives -1; no_verify, hack and hack_verify branches assign -0.5 and negative statuses; valid branch proceeds to normal sandbox scoring. Final reward returns through containing RL route.
- Later read-back: status-200 programs and hack/no_verify/hack_verify categories can be added to ProgramDatabase for subsequent selection; selection restrictions uninspected — cannot assert every stored category can become a parent.
- Delegated visibility: reward/sample metadata includes category, hack bit, reason/status payload and reward views; trainer hook receives scalar reward.
- Selection predicate: emptiness first, then missing validation marker when enabled, then model verdict; ordinary execution only in remaining branch.
- Invalidation or expiry: rejected normal execution does not imply removal from database; empty-code insertion not granted by the explicit category predicate. Recovery/snapshot belongs to containing RL route.
- Activation or effect: code enforces execution bypass and penalties, while retention can preserve rejected examples. No target run or parameter effect observed.
- Evidence limits: marker is a preliminary syntax/content cue, not evidence that holdout evaluation ran; upstream training consumption remains outside inspected source.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No per-code human approval. Admission for execution is computational and conditional, not truth acceptance. Rollback cannot undo effects that a separately executed valid program already produced. This branch rejects before ordinary execution, rather than executing then withdrawing a claim.

> elif code_category == "hack_verify":
>     hack_reason_detail = hack_reason
>     logger.warning(f"[HACK VERIFY DETECTED] Validation score is not from a real hold-out validation: {hack_reason_detail}")
>     score = None
>     base_reward = -0.5
>     effective_base_reward = -0.5
>     shaped_base_reward = -0.5
>     final_reward = -0.5
> --- `OpenMLE-ERL/RL/generate_mle.py`

Storage's broader predicate is already quoted in [RT-RTE-rl-training](runtime.md#rt-rte-rl-training); it prevents interpreting this rejection as blanket forgetting or trusted-database admission.

#### EPI-RTE-summary-generation
Label: Rich summary generation

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

Endpoints: selected journal node/first parent/task description → rich summary model if no usable existing/card/cache value → normalized summary → node/card/cache → operator-memory preparation. Owner: solver code, with model proposing prose. A proper retained transformation part of search, distinct from the whole search route. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

- Immediate return: node rich_summary attached or unchanged; missing client, exception or malformed result returns without a newly stored summary.
- Later read-back: subsequent ensure calls accept existing/card/cache summary; selected related nodes have summaries ensured before operator calls. Supplied [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance) establishes optional memory delivery, not activation.
- Delegated visibility: summary function receives task description, node and first parent; cache records node and parent IDs with summary. Full prompt semantics not audited here.
- Selection predicate: existing/card/cache with both required fields preferred; model response accepted after JSON parse and nonempty string coercion of both fields.
- Invalidation or expiry: malformed cache ignored; missing fields reject new output; file-write errors warn while node/card can remain updated. No evidence-based semantic withdrawal predicate in inspected methods.
- Activation or effect: retained prose is available to later prompts and checkpoint-related reuse; behavioral dependence or benefit unobserved.
- Evidence limits: generated explanatory/comparative text is not automatically warranted by score differences; no actual generated instance supplied. Full memory selection/rendering is not assessed exhaustively here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Software selects sources and accepts nonempty structure; model proposes content; operator supplies configuration, not per-summary approval. The intended use is prompt experience, with advisory force over future proposals, not verified scientific knowledge. No independent answer oracle checks its explanations. Source identities link parents, but these are not controlled component interventions.

> method_overview = str(parsed.get("method_overview") or "").strip()
> parent_experience = str(parsed.get("parent_comparison_experience") or "").strip()
> if not method_overview or not parent_experience:
>     return None
> return {
>     "method_overview": method_overview,
>     "parent_comparison_experience": parent_experience,
> }
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> summary = self._normalize_rich_summary(response)
> if summary is None:
>     self.logger.warning(f"Rich memory summary returned invalid JSON for node {node.id}")
>     return
> self._store_rich_summary(node, summary)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

### Claims

#### EPI-CLM-verifiable-packages
Label: Verifiable task packages

Claimed operation: Gym builds, describes, executes and quality-checks verifiable MLE task packages. Source: SRC-1, `README.md`, doctrine/design. Compared with [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution), this is the task-package warrant claim, not the training-to-search cycle. Distinct identity; no counterpart in supplied runtime claims.

> | **OpenMLE-Gym** | Build, describe, execute, and quality-check verifiable MLE task packages | [`OpenMLE-Gym/`](OpenMLE-Gym/) |
> --- `README.md`

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
