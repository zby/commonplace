---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "OpenRSI epistemic routes: executable fitness, task-quality judgment, retained experiment summaries and operator-training authority."
run-id: AAS-2026-10-19-openrsi-4f870183cadd-01
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI epistemic report

## Source-and-claim boundary

Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Source identity and evidence layers: see the [Source register](boundary.md#source-register), SRC-1. The question is which shipped mechanisms turn candidate programs, experiment outcomes and descriptions into content licensed for later reliance, and which merely grant execution, ranking or training authority. The target is an improvement plane, not a single continuously self-modifying agent. All implementation judgments below concern the frozen artifact, not observed activation.

The principal distinction is between **scoped execution evidence** and **reusable explanatory experience**. A finite task score can rank a candidate under the selected metric. It does not by itself warrant the model's explanation of why that candidate worked, or transfer to another task. Conversely, descriptive and comparative summaries can enter later prompts without passing an evidence-consuming semantic acceptance decision.

Claims assessed are [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution), [RT-CLM-training-validation](runtime.md#rt-clm-training-validation), and [EPI-CLM-model-harness](#epi-clm-model-harness). No exact weights, complete training corpus, deployed services, target runs or causal experiments are supplied. Missing weights prevent exact parametric lineage; absent traces prevent an observed score-to-update-to-later-behavior chain; missing experimental artifacts prevent independent performance attribution. External RL SLIME is not the vendored SFT implementation. Available but uninspected metadata, training and evaluator branches remain coverage limits, not access failures.

| Entry point or operation | Source path in SRC-1 | Coverage and records | Limit and prevented conclusion |
| --- | --- | --- | --- |
| Gym CLI dispatch | `OpenMLE-Gym/openmle_gym/cli.py` | Direct read of imports and dispatch; build, prepare-input, overview, metric-check, evaluate and leaderboard identified | Not every dispatched implementation inspected; no CLI-wide negative |
| Gym construction and tools | `OpenMLE-Gym/builder_core/utils/nodes.py` | Supplied [RT-RTE-gym-build](runtime.md#rt-rte-gym-build), [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution) | Generated metric compilation does not establish task fidelity |
| Gym metric-check | `OpenMLE-Gym/openmle_gym/metric_validation.py` | Direct complete read; [EPI-RTE-metric-check](#epi-rte-metric-check) | Task-provided reference data and metric are not independently authenticated |
| Gym task-quality evaluation | `OpenMLE-Gym/openmle_gym/local_evaluator.py` | Direct reads of judgment normalization, task branch, failure consumer and CSV export; [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-quality-recommendation](#epi-rte-quality-recommendation) | Deterministic validation internals and full judge prompt not completely inspected; no comprehensive quality-gate audit |
| Gym overview and metadata | `OpenMLE-Gym/openmle_gym/overview.py` | Function/search inventory only; metadata pipeline and prepare-input/leaderboard bodies unassessed | Cannot establish all acquired/generated metadata semantics, source-warrant preservation or downstream use |
| Evo ordinary, async and final test | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | Supplied [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation), [RT-RTE-evo-async](runtime.md#rt-rte-evo-async), [RT-RTE-final-submit](runtime.md#rt-rte-final-submit) | Supplied findings, not independent full reread; no schedule equivalence or reliable outcome claim |
| Evo experience construction and prompt rendering | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | Direct card/board construction, import/family detector and selected rendering reads; [EPI-RTE-experience-derive](#epi-rte-experience-derive), [EPI-RTE-summary-consume](#epi-rte-summary-consume) | Complete parent-utility and sibling selection policies not read; no complete memory inventory |
| Evo rich summaries | `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py` | Complete operator read and direct solver cache/normalization reads; [EPI-RTE-summary-produce](#epi-rte-summary-produce), [EPI-RTE-summary-retain](#epi-rte-summary-retain) | No model response supplied; actual semantic preservation or new claims not determinable |
| Evo improve prompt consumer | `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py` | Direct targeted-memory assembly read; [EPI-RTE-summary-consume](#epi-rte-summary-consume) | Delivery is not compliance or benefit; debug/crossover detail not independently traced here |
| MLE/NatureBench execution | `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py` | Supplied [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution) and MLE findings in [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation) | External oracle truth, complete preflight and service internals unresolved |
| SFT selection and loss consumer | `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py` | Supplied [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters) | Multi-entry pipeline; arbitrary supplied dataset can avoid upstream selectors; no universal corpus warrant |
| RL generation/reward/storage | `OpenMLE-ERL/RL/generate_mle.py` | Supplied [RT-RTE-rl-training](runtime.md#rt-rte-rl-training); direct search confirms categories, pre-sandbox hack check and insertion predicate | All reward combinations, judge implementation and database later-selection rules not independently inspected; no rejection-implies-forgetting claim |
| Shipped skills, static priors, full sandbox/recovery and other rollout variants | `OpenMLE-Evo/skills` | Included by boundary but unassessed here beyond supplied runtime findings | Prevents system-complete negative about knowledge, criticism, acceptance or withdrawal |

No supplied runtime finding needs supersession. Its generation and training routes remain valid containers; the new route records below separate functions that need different epistemic assessments.

## Epistemic-object inventory

Each new object record owns its form, substrate and evidence; fields below defer to it rather than recopy them.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-metric-result](#epi-obj-metric-result) | Sample scored under the selected task metric; execution/finiteness result | see record | SRC-1, `OpenMLE-Gym/openmle_gym/metric_validation.py` | No independently validated reference truth |
| [EPI-OBJ-quality-scores](#epi-obj-quality-scores) | Task-quality judgments, reasons and evidence allegations | see record | SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py` | Evidence strings are requested and structurally checked, not proven true |
| [EPI-OBJ-experience-card](#epi-obj-experience-card) | Recorded fitness, lineage, status; computed family/novelty/delta | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | Heuristic family and operational novelty differ from a scientific explanation |
| [EPI-OBJ-rich-summary](#epi-obj-rich-summary) | Method description and parent-comparison experience | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py` | No actual response individuates a produced claim |
| Candidate program/plan part of [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation) | Program is executable policy; plans may contain claims | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | No specific plan supports classification of its inferential content |
| Imported task and sandbox outcome part of [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation) | Task description, logs, status and selected fitness | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py` | External metric lineage and execution truth unresolved |
| Trajectory/message and reward parts of [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | Stored demonstrations and execution/relative reward; not every token truth-apt | see records | SRC-1, `OpenMLE-ERL/RL/generate_mle.py` | Training use is not endorsement of all sample statements |
| Distributed-parametric components | Truth-apt latent content not determinable from source | see [RT-CMP-openai-llm-provider](runtime.md#rt-cmp-openai-llm-provider), [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm), [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model), [RT-CMP-rl-model](runtime.md#rt-cmp-rl-model) | SRC-1, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh` | Separate inference/training mutability; no exact weights or model-internal claims available |

## Authority-route ledger

These are functions, not phases every candidate must traverse. A repeated container citation separates its functions without replacing its canonical fields. All implemented rows are source-supported capacity, not observed operation. No acceptance/lifecycle-integration row is inferred from retention or use.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | content transformation | implemented | Generated task description/prepare/metric | truth-apt transformation: indeterminate | Raw task to generated package | Model plus code extraction/compile, not semantic proof | see record | see record | Proposal and executable package | No established general task fidelity | Generated preparation can run; compile admits metric source | see [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution) | SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py` | none | none | Build success is not acceptance of all generated claims |
| [EPI-RTE-metric-check](#epi-rte-metric-check) | check/evidence production | implemented | [EPI-OBJ-metric-result](#epi-obj-metric-result) | truth-apt transformation: entailed derivation | Sample submission against task answer under task metric | Task-supplied class; optional validation; finite numeric check | see record | Score or exception | Enforcing result shape | Metric execution/finiteness on these inputs only | Return or fail metric worker/CLI | see record | SRC-1, `OpenMLE-Gym/openmle_gym/metric_validation.py` | none | none | Not a benchmark of model quality or proof of metric fidelity |
| [EPI-RTE-quality-check](#epi-rte-quality-check) | check/evidence production | implemented | [EPI-OBJ-quality-scores](#epi-obj-quality-scores) | truth-apt transformation: indeterminate | Task semantic quality | Model judgment over supplied task evidence; deterministic hard gate separately | see record | Scores/reasons/issues, skipped or failed | Advisory quality evaluation; structural normalization enforcing | Evidence-conditioned opinion, not independently verified ground truth | Enables recommendation/reporting on successful result | see record | SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py` | none | none | Full deterministic validation and prompt not inspected |
| [EPI-RTE-quality-recommendation](#epi-rte-quality-recommendation) | disposition/acceptance | implemented | [EPI-OBJ-quality-scores](#epi-obj-quality-scores) | non-truth-apt policy/content update: recommendation label | Quality scores to recommended/conditional/not_recommended | Arithmetic thresholds and status consumers | see record | Report recommendation; process status | Advisory recommendation; enforcing CLI failure on listed failures | A recommendation under this rubric, not demonstrated semantic acceptance for training or release | CSV output and CLI exit, not automatic task deletion/deployment veto | see record | SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py` | none | none | Disposition function does not establish evidence-consuming acceptance of an ampliative claim |
| [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation) | check/evidence production | implemented | Program and result | truth-apt transformation: acquisition/import | Candidate outcome/fitness | Configured sandbox/task metric; analyzer fallback; optional self-reported score | see record | see record | Score/bug status for search | Conditional on evaluator/protocol, input and split; source warrant unknown | Debug or continue according to parser | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py` | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Finite score does not warrant explanatory mechanism |
| [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation) | operational admission/selection/consumption | implemented | Evaluated candidates | no content change | Population/parent/best-node choice | Software fitness/validity/policy, possibly model-derived metric | see record | see record | Ranking/admission | Best under configured available results, not universal superiority | Selects later parents, debug and final code | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Selection is not acceptance of all plan/analysis content |
| [EPI-RTE-experience-derive](#epi-rte-experience-derive) | content transformation | implemented | [EPI-OBJ-experience-card](#epi-obj-experience-card) | truth-apt transformation: entailed derivation | Code syntax and recorded outcome statistics | Deterministic detector/arithmetic over supplied inputs | see record | Card/board facts under implementation-defined categories | Records available for memory/ranking | Syntactic imports and computed statistics; family label only a heuristic | Supplies structured experiment context | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | none | none | Derived relation is not a causal effect of parent-to-child change |
| [EPI-RTE-summary-produce](#epi-rte-summary-produce) | content transformation | implemented | [EPI-OBJ-rich-summary](#epi-obj-rich-summary) | truth-apt transformation: indeterminate | Experiment/parent evidence to reusable experience text | Summary model; response shape check only | see record | Two nonempty text fields or failure | Candidate generation | No semantic entailment or non-entailment established for actual outputs | Makes summary eligible for storage/use | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py` | none | none | Could reshape, derive or conjecture; needs actual response and source comparison |
| [EPI-RTE-summary-retain](#epi-rte-summary-retain) | retention | implemented | [EPI-OBJ-rich-summary](#epi-obj-rich-summary) | no content change | Candidate text to node/card/cache | Nonempty fields and cache loading; software | see record | Retained/reloaded summary | Availability, not epistemic acceptance | Preserves IDs, not checked explanatory warrant | Reuse rather than recomputation | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | none | none | Node-keyed cache has no shown content-fidelity revalidation |
| [EPI-RTE-summary-consume](#epi-rte-summary-consume) | operational admission/selection/consumption | implemented | [EPI-OBJ-rich-summary](#epi-obj-rich-summary), [EPI-OBJ-experience-card](#epi-obj-experience-card) | truth-apt transformation: non-ampliative reshaping | Selected parent/related memory to improve context | Code selection, field formatting and bounded text prefix | see record | Targeted memory prompt text | Advisory to model | Scoped past-attempt context; truncation may degrade meaning | Can shape next program through model interpretation | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | none | none | No warranted generic lesson follows from supplying it as evidence |
| [RT-RTE-evo-async](runtime.md#rt-rte-evo-async) | operational admission/selection/consumption | implemented | Evaluated async node | no content change | Commit/admit completed work | Lock-protected software policy and stop condition | see record | see record | Enforcing commit ordering/admission | No extra epistemic evaluator | May reject work after stop; admitted nodes feed later workers | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | none | none | No observed race/budget correctness |
| [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution) | check/evidence production | implemented | Candidate and service feedback | truth-apt transformation: acquisition/import | NatureBench outcome | Preflight/executor/evaluation service; task-specific domain | see record | see record | Failure/status and selection score | Service-dependent outcome, source warrant unknown | Supplies shared search parser | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py` | [EPI-CLM-model-harness](#epi-clm-model-harness) | none | Complete oracle internals uninspected |
| [RT-RTE-final-submit](runtime.md#rt-rte-final-submit) | operational admission/selection/consumption | implemented | Best available program | no content change | Export and final test call | Runner Boolean and repeat bounds | see record | see record | Enforcing on this runner branch | Final test when performed adds split-scoped evidence only | False skips test loop while code still exports | see record | SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py` | none | none | Export cannot imply final testing |
| [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) | disposition/acceptance | implemented | Trajectories | no content change | Which demonstrations reach selected dataset | Path-specific score, length, gap/top-k and dedup filters | see record | see record | Filtering for intended supervised use | Demonstration eligibility, not truth of all text or causal method explanation | Selected messages can enter SFT | see record | SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py` | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Launcher can accept separately supplied data |
| [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) | behavior/policy adaptation | implemented | Operator parameters | non-truth-apt policy/content update: supervised numerical training | Stored messages to loss inputs/checkpoints | Tokenization/loss masks/SFT objective, not fresh task oracle | see record | see record | Training input wiring | No warranted claim extracted from weights by this evidence | Intended operator parameter update | see [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters) | SRC-1, `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py` | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | Actual update and later deployment unobserved |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | check/evidence production | implemented | Candidate code and outcome | truth-apt transformation: acquisition/import | Eligible candidate execution outcome | Sandbox/task metric; eligibility model hack judge separate | see record | see record | Reward-bearing evidence | Task/protocol-scoped only; judge classification not expected-answer oracle | Supplies reward metadata | see record | SRC-1, `OpenMLE-ERL/RL/generate_mle.py` | [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | none | All shaping combinations and judge reliability unresolved |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | disposition/acceptance | implemented | Hack/no_verify/valid code categories | non-truth-apt policy/content update: execution eligibility and reward policy | Code eligibility and penalties | Model classification plus software branch | see record | see record | Enforcing on selected sandbox path | Eligibility is not truth certification | Can prevent execution and penalize; categorized failures may still persist | see record | SRC-1, `OpenMLE-ERL/RL/generate_mle.py` | none | none | Rejection is not withdrawal from every store or future use |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | retention | implemented | Programs with categories/outcomes | no content change | Database insertion | HTTP 200 or named invalid categories | see record | see record | Persistence | None from retention alone | Stored programs available for later generation selection | see record | SRC-1, `OpenMLE-ERL/RL/generate_mle.py` | none | none | Full downstream filtering not inspected |
| [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | behavior/policy adaptation | implemented | Reward/sample and operator parameters | non-truth-apt policy/content update: reward-directed training handoff | Execution reward to training inputs | Local hooks and external RL SLIME | see record | see record | Local reward/hook wiring, external optimizer contract | No claim of truth licensed by reward magnitude | Intended parameter change and serving reuse | see [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters) | SRC-1, `OpenMLE-ERL/RL/generate_mle.py` | [RT-CLM-training-validation](runtime.md#rt-clm-training-validation) | none | Exact optimizer and subsequent effects uninspected |

The first applicable transformation classification is used. Imported scores are acquisition with unknown upstream warrant, not newly produced scientific knowledge. The metric/card deductions add propositions entailed by the inspected program under its stipulated inputs and ordinary Python semantics. A family label's truth outside the detector's own operational definition is not established. The natural-language summary cannot be classified as ampliative merely because entailment has not been proven. The render step only formats/selects existing text; this operational non-ampliative classification does not certify preservation of a truncated claim's qualifications.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) | see record | SRC-1, `README.md`; doctrine/design | Bounded executable-domain improver training | [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation), [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | None supplied | Architecture supplies paths, not an exercised chain | Improvement-directed training and search wiring supported separately | No general RSI success claimed; no independent learning benefit established |
| [RT-CLM-training-validation](runtime.md#rt-clm-training-validation) | see record | SRC-1, `OpenMLE-ERL/RL/README.md`; reported operation | Named restore/optimizer/sync/evaluation profile | [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | Author report only | External trainer, weights and run artifacts unavailable | Report can be attributed, not upgraded to observed operation | Complete end-to-end validation remains unverified here |
| [EPI-CLM-model-harness](#epi-clm-model-harness) | see record | SRC-1, `README.md`; reported operation and design qualification | Model-fixed/harness-fixed contrasts and combined Max setting distinguished | [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation), [RT-RTE-evo-async](runtime.md#rt-rte-evo-async), [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution), [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) | None supplied | Reported contrasts do not expose allocation, repetitions, confounds or raw outcomes; Max bundles priors and async search | Claimed model–harness outcomes, not one-shot model scores | Cannot independently attribute gains to training, experience, asynchronous scheduling or their mechanisms |

## Bounded conclusion

**Executable scores have local force.** Gym metric-check establishes a finite numeric result on the task's sample/reference inputs or fails. Evo uses task outcomes, parser validity and configured policies to rank programs, select parents, debug or export. The source-supported countercase to universally independent holdout scoring is the supported analyzer/self-valid/test-score configuration, not an observed error or cheating event. NatureBench supplies a different service-backed oracle. Each license stays bounded by evaluator, task, split, inputs and protocol; none certifies every explanation accompanying the code. See [EPI-RTE-metric-check](#epi-rte-metric-check), [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation), [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution).

**Task-quality judgment is a separate route with a real reporting consumer.** The model's scores and evidence allegations are normalized, averaged and mapped to recommendation labels. Deterministic validation failure can hard-gate quality scores; explicit local/skip mode avoids the model judgment. CLI failure depends on validation/process/evaluation failure, not merely a low recommendation. This is not a discovered automatic prohibition on training with or deploying an unrecommended task. See [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-quality-recommendation](#epi-rte-quality-recommendation).

**Retained experience mixes warranted arithmetic with unaccepted interpretation.** Card/board arithmetic can derive rankings, deltas and counts from recorded observations. The warrant remains conditional on those observations and the code's category definitions. Rich summary production requests reusable descriptions and parent comparisons, but admits nonempty parsed fields without checking their explanatory fidelity. Cache reuse and prompt delivery grant availability and advisory behavioral force before semantic acceptance. A concrete short input is preserved modulo whitespace; longer text is cut at a character boundary. That may remove a scope condition. No actual generated response establishes either a novel explanatory conjecture or an accepted ampliative claim. See [EPI-RTE-experience-derive](#epi-rte-experience-derive), [EPI-RTE-summary-produce](#epi-rte-summary-produce), [EPI-RTE-summary-retain](#epi-rte-summary-retain), [EPI-RTE-summary-consume](#epi-rte-summary-consume).

**Rejection and cleanup are not equivalent to withdrawal of reliance.** A malformed summary can be left unstored; an existing nonempty node/card/cache summary is reused without shown semantic revalidation. Async commit can refuse completed work after a stop. Final-submit false suppresses only the runner's final test loop, not code export. RL rejects some categories from execution and assigns penalties yet permits their database insertion. The supplied implementation does not justify assuming rejected content disappears from all future contexts. Full store selection, eviction and recovery semantics remain unassessed here, so no system-wide withdrawal absence is asserted. See [EPI-RTE-summary-retain](#epi-rte-summary-retain), [RT-RTE-evo-async](runtime.md#rt-rte-evo-async), [RT-RTE-final-submit](runtime.md#rt-rte-final-submit), [RT-RTE-rl-training](runtime.md#rt-rte-rl-training).

**Training authority is distinct from epistemic acceptance.** SFT selection licenses demonstrations for a path-specific training use; the launcher also accepts caller-selected datasets. RL categories, sandbox feedback and configured shaping supply reward to an external training environment. Both routes are intended to change distributed parameters, while Evo inference changes programs/journal rather than operator weights. Exact produced weights, an installed endpoint mapping and later causally dependent behavior are not available. Thus these are independent architectural self-change contributions, not an observed successful self-improvement chain. Program improvement alone remains improvement of the external work product. Retained experience has a live advisory input path but no observed effect or demonstrated capacity gain in this evidence set. See [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters), [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm), [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model), [RT-CMP-rl-model](runtime.md#rt-cmp-rl-model).

No inspected route establishes a produced accepted ampliative explanation and subsequent lifecycle integration. This is a bounded result for the assessed routes, not a system-complete negative: static priors, skills, metadata and other training variants remain unassessed. Learning benefit, reflection, autonomous theory building and self-improvement success are separate questions, not consequences of the word experience, score improvement, persistence or model opacity. No single system-wide epistemic status follows.

## Shared records

### Operative objects

#### EPI-OBJ-metric-result
Label: Metric smoke-test result

Distinct identity: no operative-object counterpart declared in supplied runtime. This is the result of the additional metric-check operation, not the entire construction route [RT-RTE-gym-build](runtime.md#rt-rte-gym-build). Symbolic score, class name and row counts in a Python dictionary returned through worker/CLI JSON; source-native identity `evaluate_sample_submission` result. SRC-1, `OpenMLE-Gym/openmle_gym/metric_validation.py`; evidence in [EPI-RTE-metric-check](#epi-rte-metric-check).

#### EPI-OBJ-quality-scores
Label: Task quality scores

Distinct identity: no supplied object counterpart; a separately dispatched evaluator output, not Gym build completion. Source-native identity `quality_scores`/`quality_evaluation` in SRC-1, `OpenMLE-Gym/openmle_gym/local_evaluator.py`. Natural-language reasons and issue evidence plus symbolic dimension values, statuses and recommendation. Stored in task-result dictionaries and exported JSON/CSV reports. Material parts have different authority: reasons advise readers, numerical fields determine recommendation, failure statuses determine CLI result. Evidence in [EPI-RTE-quality-check](#epi-rte-quality-check) and [EPI-RTE-quality-recommendation](#epi-rte-quality-recommendation).

#### EPI-OBJ-experience-card
Label: Experience card and strategy statistics

Distinct identity: no supplied object counterpart. Source-native `build_experience_card` and `build_strategy_board`, SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`. Symbolic dictionaries containing experiment IDs, scores, status, computed ranks/counts and graph references; natural-language plan/analysis fields are separate from derived numerical warrant. Node/card/journal in-memory structures supply later rendering; full disk lifecycle not established here. Rich-summary text has its own record. Evidence in [EPI-RTE-experience-derive](#epi-rte-experience-derive).

#### EPI-OBJ-rich-summary
Label: Rich memory summary

Distinct identity: no supplied object counterpart. Source-native `method_overview` and `parent_comparison_experience`, natural-language strings carried in symbolic dictionaries attached to nodes/cards and stored in JSON cache. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` and `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`. Schema and consumers in the summary route records distinguish this from raw logs and numerical fitness. Exact latent model content and actual generated summary unavailable.

### Routes

#### EPI-RTE-metric-check
Label: Metric smoke check

Distinct identity: additional CLI operation, not a duplicate of [RT-RTE-gym-build](runtime.md#rt-rte-gym-build). CLI metric-check invokes a process worker that loads a task-local Metrics class, reads sample predictions/private answers, optionally calls submission validation, evaluates and enforces a finite non-Boolean numerical result. Owner: program; caller chooses task/mode, task author supplies reference/metric; no per-result human approval. Oracle is this task's answer file interpreted by its own metric, in smoke-test mode.

- Immediate return: Score/class/row counts, or exception and worker failure.
- Later read-back: inapplicable — this operation returns a result; no accumulated content reload is needed for this finding.
- Delegated visibility: Metric receives both parsed predictions and reference answers; worker receives task path and execution mode.
- Selection predicate: Existing required files, a locally defined class ending in Metrics, optional validate_submission and finite numeric output.
- Invalidation or expiry: Exception rejects current result; later calls reload task files rather than establishing a persistent endorsement.
- Activation or effect: CLI prints a successful result or raises; local evaluation can consume the same check.
- Evidence limits: No execution supplied; correct metric definition and reference truth are not established by successful evaluation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation, `OpenMLE-Gym/openmle_gym/metric_validation.py`:

> if hasattr(metric, "validate_submission"):
>         metric.validate_submission(y_pred, y_true)
>     score = json_safe(metric.evaluate(y_true=y_true, y_pred=y_pred))
>     if (
>         not isinstance(score, (int, float))
>         or isinstance(score, bool)
>         or not math.isfinite(float(score))
>     ):
> --- `OpenMLE-Gym/openmle_gym/metric_validation.py`

#### EPI-RTE-quality-check
Label: Task quality judgment

Distinct identity: additional evaluate CLI operation, not [RT-RTE-gym-build](runtime.md#rt-rte-gym-build). Owner: `_evaluate_task` orchestrates structural analysis, optional model evaluation and result normalization. Target/domain: semantic quality of the supplied task package. The model proposes dimension judgments and issues; software checks finite bounded scores, nonempty reasons and issue evidence structure. Model judgment is not an expected-answer oracle. Deterministic validation supplies a separate hard-gate result; its full checks are not audited here. Caller may skip model evaluation; no per-judgment human veto observed.

- Immediate return: Result dictionary with quality scores and completed, skipped or failed evaluation status.
- Later read-back: uninspected — results export to reports; no later task-building/training consumer is established here.
- Delegated visibility: Model is supplied selected task evidence, not an independent reference rating of task quality.
- Selection predicate: local_only/skip_llm avoids judgment; failed validation hard-gates; otherwise model judgment and schema normalization run.
- Invalidation or expiry: Model exceptions yield failed evaluation and empty scores; no automatic revision of task files is shown by this method.
- Activation or effect: Judgment values enter recommendation/report processing, not direct code repair.
- Evidence limits: Normalization checks structure, ranges and evidence-source labels, not truth of every reason; no model responses or calibration supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation, `OpenMLE-Gym/openmle_gym/local_evaluator.py`:

> elif validation["status"] == "failed":
>         result["quality_scores"] = _hard_gate_quality(validation)
>         result["quality_evaluation"] = {
>             "status": "completed",
>             "source": "deterministic_hard_gate",
>         }
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

> required = ("severity", "category", "message", "evidence_source", "evidence")
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

#### EPI-RTE-quality-recommendation
Label: Quality recommendation disposition

Distinct identity: no supplied route counterpart; distinct from evidence production in [EPI-RTE-quality-check](#epi-rte-quality-check). Software averages dimension scores, assigns a recommendation, exports it and determines batch failure separately. Its intended use is task-quality reporting; admission to training or production is not enforced here. No model or human chooses the numerical thresholds per result. Rejection capability is reporting/CLI failure under listed statuses, not deletion or replacement of task content; recovery requires a later explicit rerun/edit.

- Immediate return: recommended, conditional or not_recommended with average score; report paths and CLI status.
- Later read-back: uninspected — exported reports exist but a consequential later admission consumer was not traced.
- Delegated visibility: Report readers receive recommendation, scores, issues and validation/evaluation statuses; CLI receives failure predicate.
- Selection predicate: Average at least 4 recommends; at least 2.5 is conditional; otherwise not_recommended. Failure predicate independently tests process, validation and quality-evaluation failure.
- Invalidation or expiry: Current report reflects current evaluation; no implemented retraction of all prior report copies established.
- Activation or effect: Recommendation is written to summary CSV; CLI can return nonzero for listed failure statuses, not simply low average.
- Evidence limits: No reader response observed; label alone is not evidence-consuming acceptance of all task claims for all uses.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation, `OpenMLE-Gym/openmle_gym/local_evaluator.py`:

> overall = round(sum(scores) / len(scores), 2)
>     if overall >= 4:
>         recommendation = "recommended"
>     elif overall >= 2.5:
>         recommendation = "conditional"
>     else:
>         recommendation = "not_recommended"
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

> "Recommendation": scores.get("recommendation", ""),
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

> result.get("task_process_failed") is True
>             or result.get("validation", {}).get("status") == "failed"
>             or result.get("quality_evaluation", {}).get("status") == "failed"
> --- `OpenMLE-Gym/openmle_gym/local_evaluator.py`

#### EPI-RTE-experience-derive
Label: Experience card derivation

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Distinct material function inside the search container: code and recorded step/node data become card/strategy-board fields. Owner: deterministic Python, not the summary model. `extract_imports` parses AST import statements or falls back to regex; method family is token/import heuristic. Fitness, parent score direction, status and counts produce deltas, novelty and board aggregates. This is derivation under explicit program definitions, not experiment-based discovery of why a method succeeds.

- Immediate return: Card dictionary and strategy-board dictionary.
- Later read-back: Cards and board fields are inputs to later targeted-memory rendering; full persistence/selection policy not assessed here.
- Delegated visibility: Constructor sees node source, parents, metrics, step stats and prior cards; prompt renderer receives selected fields rather than all evidence.
- Selection predicate: Board valid list requires finite fitness and nonbuggy; method categories depend on inspected import/token rules.
- Invalidation or expiry: Board recomputes from supplied card list; no independent correction of false upstream measurements in this function.
- Activation or effect: Derived fields become available for ranking/context; actual behavioral effect not observed.
- Evidence limits: Deterministic derivation preserves no more source warrant than its inputs. Heuristic family recognition can misclassify program behavior.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`:

> if isinstance(node, ast.Import):
>                 for alias in node.names:
>                     imports.add(alias.name.split(".", 1)[0])
>             elif isinstance(node, ast.ImportFrom) and node.module:
>                 imports.add(node.module.split(".", 1)[0])
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

> family_count_before = _family_count_before(method_family, previous_cards, node_id=node_id)
>     novelty_score = 1.0 / math.sqrt(1.0 + family_count_before)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

Concrete deduction without execution: `import sklearn.model_selection\nfrom sklearn.metrics import accuracy_score` parses into two imports whose roots both equal `sklearn`; set insertion deduplicates, then sorting returns `["sklearn"]`. This entails a syntactic root-import fact, not that the program executed a valid sklearn experiment. For a fixed family with no previous cards, `family_count_before = 0` gives novelty 1; that is novelty relative to this record/category, not a claim of scientific originality.

#### EPI-RTE-summary-produce
Label: Rich summary candidate production

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Distinct material content-producing function, not all search. Solver selects a node and first parent; summary operator supplies task, source/plan, outcome/status, scores/delta/runtime and sanitized logs to the configured summary model. The model is asked for method description and reusable parent-comparison experience. Owner: code schedules, model proposes, software normalizes nonempty parsed fields. Target is the experiment description/interpretation; there is no inspected semantic evaluator certifying that output. No human approval wired. The process proposes retained guidance changes; software can reject malformed output and retry on a later invocation rather than rolling back the experiment.

- Immediate return: Candidate two-field response, or logged error/invalid JSON and no stored summary.
- Later read-back: A normalized result is eligible for node/card/cache retention and later prompt inclusion through separate routes.
- Delegated visibility: Summary model sees selected current/first-parent information, not a controlled ablation or full journal history.
- Selection predicate: No usable existing/node/card/cache summary and a configured summary function; parsed nonempty method_overview and parent_comparison_experience.
- Invalidation or expiry: Exceptions or invalid fields stop this write; no semantic correctness rejection appears in the inspected normalization path.
- Activation or effect: Successful normalization permits retention; the invocation itself does not certify truth or transfer.
- Evidence limits: No response supplied; possible classifications are reshaping, entailed derivation and ampliative conjecture, requiring response/input comparison to decide.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation/schema contract, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`:

> "description": "2-5 concise sentences comparing the current node against its parent and extracting reusable success or failure experience."
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`

> return rich_memory_summary_llm(
>         query_data=query_data,
>         json_schema=rich_memory_summary_schema,
>         function_name="write_rich_memory_summary",
>         function_description="Write reusable memory for one completed ML experiment node.",
>     )
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`

#### EPI-RTE-summary-retain
Label: Rich summary cache retention

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Distinct retention function, not candidate production or lifecycle integration. Solver attaches summary to node and experience card, writes node/parent IDs and summary to JSON cache, and later reuses node/card/cache content before generating again. Owner: software. Admission is presence/shape, not acceptance of explanation for transfer. Source SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

- Immediate return: Attached summary and attempted cache write; write errors warn.
- Later read-back: Existing node, attached card or parsed cache summary is reused by later memory preparation.
- Delegated visibility: Cache stores node_id, parent_node_ids and summary; readers require nonempty text fields, not an evidence-backed acceptance record.
- Selection predicate: Node then card then node-keyed cache precede new summary generation.
- Invalidation or expiry: Missing/unreadable/invalid JSON cache falls through; no content-change or evaluator-based semantic expiry demonstrated in these methods.
- Activation or effect: Summary can survive for future prompt construction; no observed reliance claimed.
- Evidence limits: IDs preserve association, not causal explanation; cache freshness and filesystem persistence are not semantic warrant.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> method_overview = str(parsed.get("method_overview") or "").strip()
>         parent_experience = str(parsed.get("parent_comparison_experience") or "").strip()
>         if not method_overview or not parent_experience:
>             return None
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> cached_summary = self._load_cached_rich_summary(node)
>         if cached_summary is not None:
>             self._store_rich_summary(node, cached_summary)
>             return
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

#### EPI-RTE-summary-consume
Label: Targeted experience prompt consumption

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Distinct read/render function. Solver selects related nodes for summary preparation; `improve_op` builds targeted parent/ancestor/sibling memory and appends it to optional base memory. `_rich_summary_lines` prefers rich summaries and falls back to legacy analysis. The rendered fields, not full cached text or all experiment evidence, reach operator prompt context. Consumer: improve model. Channel: natural-language memory string plus structured score/ID rendering. Force: advisory through interpretation. Horizon: next proposal, potentially later rounds through changed code/journal. No human veto or guaranteed model compliance; software controls inclusion. Task evidence/metrics remain the search oracle, not the memory text itself.

- Immediate return: Formatted targeted memory appended to operator memory.
- Later read-back: Selected earlier summaries/cards reappear in later model invocations; node/related-card selection is code-directed, not model-requested retrieval.
- Delegated visibility: Per-summary 420-character compaction, legacy analysis 360; selected scores, rank, family and parent context accompany text.
- Selection predicate: prompt_memory_enabled and selected related nodes/cards; rich fields preferred to analysis.
- Invalidation or expiry: Omitted nodes and truncated tails remain outside this invocation; retained full summaries can remain reachable through later selection rather than being deleted.
- Activation or effect: Supplies model-visible guidance for later code proposal; no observed changed behavior or improvement.
- Evidence limits: Full selector policy and all operator variants not read; compaction can discard qualifications and carries no semantic preservation proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`:

> text = re.sub(r"\s+", " ", str(value or "")).strip()
>     if len(text) <= max_chars:
>         return text
>     return text[: max_chars - 3].rstrip() + "..."
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

> method_overview = _compact_text(rich_summary.get("method_overview"), max_chars=420)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

> "Use this memory as evidence about the selected parent, its recent evolution path, and nearby sibling attempts. Do not treat it as a complete history.",
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

Concrete deduction without execution: `_compact_text("  Model\n failed  ", 420)` returns `Model failed`. With `max_chars=8`, the whitespace-normalized `Model failed` exceeds the bound, so the first five characters `Model` plus `...` return `Model...`; the failure predicate has disappeared. The implementation establishes formatting/truncation, not faithful preservation of the original proposition. Working-context control is selected by-value supply: a bounded subset crosses into the operator frame, while omitted text stays in the retained source rather than becoming a pointer the model can automatically follow.

### Claims

#### EPI-CLM-model-harness
Label: Reported model–harness gains

Distinct identity: performance/attribution claim, not the bounded initiative claim [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution) or async path validation [RT-CLM-training-validation](runtime.md#rt-clm-training-validation). Claimed operation: model-fixed/framework-fixed benchmark improvements, with combined Max results explicitly not a pure model gain. SRC-1, `README.md`; reported operation, with design qualification. No execution artifacts or causal experiment registered here.

> These are **model–harness results**, not standalone one-shot model scores. The OpenMLE-Evo-Max result changes the search system through benchmark-independent experience priors and asynchronous search, and should not be interpreted as a pure model gain.
> --- `README.md`

### Evidenced absences

none declared in this member
