---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AgeMem's documentary truth-apt routes, evaluator licenses and outcome-responsive policy adaptation."
run-id: AAS-2026-10-12-2601-01885v1-32274e5bddc1-01
reviewed-boundary: "arxiv-2601.01885v1-html-2026-10-12"
---

# AgeMem epistemic report

## Source-and-claim boundary

The question is how AgeMem acquires or generates factual candidates, evaluates them, permits later reliance, and adapts behavior from results. The [boundary](boundary.md#boundary-and-evidence) freezes a complete paper capture but only a partial operational loop. Its [Source register](boundary.md#source-register) owns SRC-1. All architectural routes below are **doctrine only**: pseudocode, formulas, schemas and prompts are design evidence, not inspected implementation. Author-reported results do not constitute observed-run evidence under this boundary.

Direct inspection here covers Appendix A.1's six operation definitions and both prompts, Appendix A.2's reward formulas, Appendix C.2's two evaluation prompts, and §§4.2–4.3's reported comparisons. Algorithms 1–5, tool schemas and illustrative cases are also covered through supplied runtime findings; they are not independently traced executable code. No frozen CLI, hook, dispatcher, registered executable tool or exposed API exists in the supplied capture. This is an evidence limit, not an absence claim about a deployed AgeMem.

| Entry point or operation | Source path/local anchor in SRC-1 | Coverage | Uninspected evidence and conclusion prevented |
|---|---|---|---|
| Context input, answer generation and stage reset | `2601.01885v1.html#alg1`; `2601.01885v1.html#alg3`–`alg5` | Supplied [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout); [EPI-RTE-language-content](#epi-rte-language-content) | Model-visible inputs and raw answers: cannot establish semantic derivation or actual query isolation |
| Add, Update, Delete | `2601.01885v1.html#A1.SS1.SSS0.Px3`; `2601.01885v1.html#A1.SS1.SSS0.Px4` | Direct definitions; supplied [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools); [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance) | Dispatcher and write history: cannot establish validation, rollback or durable revision lineage |
| Explicit Retrieve and unsolicited Stage 1 retrieval | `2601.01885v1.html#A1.SS1.SSS0.Px2`; `2601.01885v1.html#alg3` | Direct definition; supplied [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval); [EPI-RTE-explicit-retrieval](#epi-rte-explicit-retrieval) | Encoder and delivery rendering: cannot reproduce ranking or establish complete-store awareness |
| Summary and Filter | `2601.01885v1.html#A1.SS1.SSS0.Px5`; `2601.01885v1.html#A1.SS1.SSS0.Px6` | Direct definitions/prompts; [RT-RTE-context-summary](runtime.md#rt-rte-context-summary), [RT-RTE-context-filter](runtime.md#rt-rte-context-filter) | No executable transformations or fidelity traces: cannot prove preservation |
| Terminal answer, storage, relevance and preservation scoring | `2601.01885v1.html#A1.SS2` | Direct formulas; [EPI-RTE-answer-reward](#epi-rte-answer-reward), [EPI-RTE-storage-reward](#epi-rte-storage-reward), [EPI-RTE-relevance-reward](#epi-rte-relevance-reward), [EPI-RTE-context-reward](#epi-rte-context-reward) | Judge implementations and score traces: cannot establish calibration or actual feedback |
| Telemetry reward and GRPO | `2601.01885v1.html#A1.SS2`; `2601.01885v1.html#alg2` | Direct reward definitions; supplied [RT-RTE-policy-update](runtime.md#rt-rte-policy-update); [EPI-RTE-telemetry-reward](#epi-rte-telemetry-reward) | Optimizer and checkpoint lineage: cannot establish exercised adaptation or individual-action effects |
| MQ, HotpotQA answer judgment and simulation metrics | `2601.01885v1.html#A3.SS2`; `2601.01885v1.html#S4.SS1` | Direct prompts; supplied [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles); [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | Raw runs and environment evaluators: cannot reproduce results or validate scorer reliability |
| Reported comparisons and case examples | `2601.01885v1.html#S4.SS2`; `2601.01885v1.html#S4.SS3`; `2601.01885v1.html#A2` | Direct comparison text; supplied runtime case limits; [EPI-CLM-memory-quality](#epi-clm-memory-quality), [EPI-CLM-maintenance-quality](#epi-clm-maintenance-quality), [EPI-CLM-reward-benefit](#epi-clm-reward-benefit) | No independently inspectable interventions: cannot establish causal effects beyond author attribution |

External frameworks, model-provider internals, benchmark code and uncaptured images remain outside the accessible evidence. The policy, encoder, summarizer and evaluator have separate opaque distributed-parametric roles; see [RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy), [RT-CMP-text-encoder](runtime.md#rt-cmp-text-encoder), [RT-CMP-summarize-model](runtime.md#rt-cmp-summarize-model), [RT-CMP-qwen-max](runtime.md#rt-cmp-qwen-max). Their opacity leaves internal truth-apt content **not determinable**, not absent. These gaps prevent a system-complete negative about epistemic acceptance or criticism. Consequential warrant claims are the three EPI claims above, the oracle account, and [RT-CLM-tool-protocol](runtime.md#rt-clm-tool-protocol) and [RT-CLM-context-reset](runtime.md#rt-clm-context-reset).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID/local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | Factual statements, user preferences and reusable information; see record | See record | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px3` | Semantic provenance and accepted state unresolved |
| [EPI-OBJ-context-content](#epi-obj-context-content) | Input facts, distractors and generated summaries; see record | See record | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px5` | Summary fidelity and distinction between claim and quoted distractor unresolved |
| [EPI-OBJ-answer-content](#epi-obj-answer-content) | Task answers where propositions are factual; see record | See record | SRC-1, `2601.01885v1.html#A1.SS2` | Plans/action requests need not be truth-apt; no warrant for all generated content |
| [RT-CMP-text-encoder](runtime.md#rt-cmp-text-encoder) | None individuated in dense representations | See record | SRC-1, `2601.01885v1.html#A1.E9` | Similarity is not truth evaluation |
| [RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy) | Internal propositions not determinable | See record | SRC-1, `2601.01885v1.html#S3.SS1` | Updated weights are not localized accepted claims |
| [RT-CMP-summarize-model](runtime.md#rt-cmp-summarize-model) | Internal content not determinable; output is context prose | See record | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px5` | Prompt requests factuality, not proof of compliance |
| [RT-CMP-qwen-max](runtime.md#rt-cmp-qwen-max) | Internal content not determinable; scalar output expresses assessed fit | See record | SRC-1, `2601.01885v1.html#A3.SS2` | Exact checkpoint, calibration and training-judge identity unresolved |

Reference answers and supporting facts are external oracle inputs, not claims produced by AgeMem. Tool envelopes, memory IDs and timestamps are symbolic control/lineage material; see [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools). Their presence licenses requesting effects, not relying on content as true. The static tool prompt's authority is separately owned by [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy).

## Authority-route ledger

Fields owned by cited records are given by `see`; the classification and bounded epistemic license here are the overlay. No observed result is claimed. A route may appear in multiple rows for distinct consequential functions.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID/local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout) | content transformation | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | truth-apt transformation: acquisition/import | See route | See route | See route | See route | Uninspected | External facts acquired; source warrant unknown; distractors deliberately unreliable | See route | See route | SRC-1, `2601.01885v1.html#alg1` | [RT-CLM-context-reset](runtime.md#rt-clm-context-reset) | Query visibility unresolved | No authenticated source-warrant transport |
| [EPI-RTE-language-content](#epi-rte-language-content) | content transformation | doctrine only | [EPI-OBJ-answer-content](#epi-obj-answer-content), [EPI-OBJ-memory-content](#epi-obj-memory-content) | truth-apt transformation: indeterminate | See route | See route | See route | See route | Uninspected | Candidate generation only; preservation, derivation and conjecture unresolved | See route | See route | SRC-1, `2601.01885v1.html#S3.SS1` | none | none | No input/output trace proving entailment or non-entailment |
| [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance) | retention | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route | See route | See route | See route | Uninspected | Storing requested content does not accept it epistemically | See route | See route | SRC-1, `2601.01885v1.html#A1.E11` | [EPI-CLM-memory-quality](#epi-clm-memory-quality) | Retention is not acceptance | Content-generation relation assessed separately |
| [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance) | lineage/freshness/recovery | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | truth-apt transformation: indeterminate | See route: Update | See route | See route | See route | Uninspected | Replacement and modification timestamp do not establish validated supersession | See route | See route | SRC-1, `2601.01885v1.html#A1.E12` | [EPI-CLM-maintenance-quality](#epi-clm-maintenance-quality) | Maintenance count versus quality | Replacement semantics and prior-version recovery unresolved |
| [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance) | lineage/freshness/recovery | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route: Delete | See route | See route | See route | Uninspected | Availability withdrawal does not establish the deleted proposition's falsity | See route | See route | SRC-1, `2601.01885v1.html#A1.E13` | [EPI-CLM-maintenance-quality](#epi-clm-maintenance-quality) | Removal versus epistemic rejection | Confirmation and recovery enforcement uninspected |
| [EPI-RTE-explicit-retrieval](#epi-rte-explicit-retrieval) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route | See route | See route | See route | Uninspected | Similarity grants selection priority only, not truth warrant | See route | See route | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px2` | none | none | No fidelity guarantee for delivered rendering |
| [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route | See route | See route | See route | Uninspected | Driver delivery is neither agent-requested timing nor endorsement | See route | See route | SRC-1, `2601.01885v1.html#alg3` | none | Proactive agent versus driver | Complete-store awareness unsupported |
| [RT-RTE-context-summary](runtime.md#rt-rte-context-summary) | content transformation | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | truth-apt transformation: indeterminate | See route | See route | See route | See route | Uninspected | Requested non-ampliative compression; preservation not established | See route | See route | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px5` | none | No fidelity gate established | Cannot classify actual outputs as faithful reshaping or conjecture |
| [RT-RTE-context-summary](runtime.md#rt-rte-context-summary) | retention | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | no content change | See route | See route | See route | See route | Uninspected | Replacement retained for later use without demonstrated acceptance | See route | See route | SRC-1, `2601.01885v1.html#A1.E14` | none | Retention is not acceptance | Original-span loss and rollback unresolved |
| [RT-RTE-context-filter](runtime.md#rt-rte-context-filter) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | no content change | See route | See route | See route | See route | Uninspected | Similarity-based removal is not evidence of irrelevance or falsity | See route | See route | SRC-1, `2601.01885v1.html#A1.E15` | none | Criterion polarity inconsistency | Retained statements remain unchanged; omissions change available premises |
| [EPI-RTE-answer-reward](#epi-rte-answer-reward) | check/evidence production | doctrine only | [EPI-OBJ-answer-content](#epi-obj-answer-content) | no content change | See route | See route | See route | See route | Uninspected | Reference-relative answer judgment, not mechanism validation | See route | See route | SRC-1, `2601.01885v1.html#A1.E17` | [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) | none | No deployed-answer veto established |
| [EPI-RTE-storage-reward](#epi-rte-storage-reward) | check/evidence production | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route | See route | See route | See route | Uninspected | Task/answer-relative quality labeling, not general reusable truth | See route | See route | SRC-1, `2601.01885v1.html#A1.E23` | [EPI-CLM-memory-quality](#epi-clm-memory-quality) | Quality score versus acceptance | No per-entry acceptance criterion and admission consumer established |
| [EPI-RTE-relevance-reward](#epi-rte-relevance-reward) | check/evidence production | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route | See route | See route | See route | Uninspected | Query relevance only, not truth or warrant | See route | See route | SRC-1, `2601.01885v1.html#A1.E25` | none | Relevance versus correctness | Reward does not directly reject irrelevant retrieval |
| [EPI-RTE-context-reward](#epi-rte-context-reward) | check/evidence production | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | no content change | See route | See route | See route | See route | Uninspected | Presence of query-derived tokens/phrases, not preservation of relationships or source facts | See route | See route | SRC-1, `2601.01885v1.html#A1.E21` | none | Preservation proxy narrower than semantic fidelity | Detector implementation unspecified |
| [EPI-RTE-telemetry-reward](#epi-rte-telemetry-reward) | check/evidence production | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | no content change | See route: compression | See route: token-count formula | See route | See route | Uninspected | Economy within the declared budget, not factual warrant | See route | See route | SRC-1, `2601.01885v1.html#A1.E19` | none | Economy versus preservation | Exact token accounting uninspected |
| [EPI-RTE-telemetry-reward](#epi-rte-telemetry-reward) | check/evidence production | doctrine only | [EPI-OBJ-context-content](#epi-obj-context-content) | no content change | See route: preventive invocation | See route: timing predicate | See route | See route | Uninspected | Early tool-use occurrence, not successful prevention | See route | See route | SRC-1, `2601.01885v1.html#A1.E20` | none | Invocation versus safe compaction | No pre-action safety enforcement |
| [EPI-RTE-telemetry-reward](#epi-rte-telemetry-reward) | check/evidence production | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See route: maintenance occurrence | See route: event predicate | See route | See route | Uninspected | Update/Delete occurrence only | See route | See route | SRC-1, `2601.01885v1.html#A1.E24` | [EPI-CLM-maintenance-quality](#epi-clm-maintenance-quality) | Operation occurrence versus meaningful repair | No correctness or staleness test in this subscore |
| [EPI-RTE-telemetry-reward](#epi-rte-telemetry-reward) | check/evidence production | doctrine only | [RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy) | no content change | See route: round/token violations | See route: limit predicate | See route | See route | Uninspected | Constraint violation measurement, not factual warrant | See route | See route | SRC-1, `2601.01885v1.html#A1.E26` | none | Penalty versus prevention | Negative reward changes optimization, not an established admission gate |
| [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | behavior/policy adaptation | doctrine only | [RT-CMP-agent-policy](runtime.md#rt-cmp-agent-policy) | non-truth-apt policy/content update: parameter optimization | See route | See route | See route | See route | Uninspected | Reward licenses optimization under the objective, not acceptance of each preceding proposition/action | See route | See [RT-BAP-trained-policy](runtime.md#rt-bap-trained-policy) | SRC-1, `2601.01885v1.html#alg2` | [EPI-CLM-reward-benefit](#epi-clm-reward-benefit) | Broadcast credit not individual causal identification | No content-directed criticism or checkpoint acceptance gate established |
| [EPI-RTE-mq-evaluation](#epi-rte-mq-evaluation) | check/evidence production | doctrine only | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | See record: MQ target | See record: MQ evaluator | See record | See record | Uninspected | HotpotQA supporting-fact coverage/relevance under Qwen-Max judgment | See record | See record: reporting consumer | SRC-1, `2601.01885v1.html#A3.SS2` | [EPI-CLM-memory-quality](#epi-clm-memory-quality) | MQ versus general reusability | No target-loop acceptance consumer shown |
| [EPI-RTE-answer-evaluation](#epi-rte-answer-evaluation) | check/evidence production | doctrine only | [EPI-OBJ-answer-content](#epi-obj-answer-content) | no content change | See record: answer target | See record: answer evaluator | See record | See record | Uninspected | HotpotQA answer equivalence to reference; no process or replay warrant | See record | See record: reporting consumer | SRC-1, `2601.01885v1.html#A3.SS2` | [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) | none | Qwen-Max judgment remains fallible |
| [EPI-RTE-environment-evaluation](#epi-rte-environment-evaluation) | check/evidence production | doctrine only | [EPI-OBJ-answer-content](#epi-obj-answer-content) | no content change | See record: environment target | See record: environment evaluator | See record | See record | Uninspected | Benchmark success/progress only; not explanation or transferable mechanism | See record | See record: reporting consumer | SRC-1, `2601.01885v1.html#S4.SS1` | [EPI-CLM-reward-benefit](#epi-clm-reward-benefit) | Outcome versus mechanism | Environment evaluator internals uninspected |

No **disposition/acceptance** or **lifecycle integration** row is asserted. The inspected design contains operational installation and later scoring, but not an evidenced decision accepting a particular ampliative proposition for a named use and scope, followed by integration on that basis. The formulas are a counterexample to a blanket “no checks” claim: real evaluation roles are specified and their results have an optimizer consumer. They are not an epistemic write gate. Conversely, optional source metadata is a counterexample to saying the design has no lineage fields; it does not prove those fields preserve a warranted derivation.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-memory-quality](#epi-clm-memory-quality) | See claim | SRC-1, `2601.01885v1.html#S4.SS2.p2`, reported operation | See [EPI-RTE-storage-reward](#epi-rte-storage-reward), [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | None inspected | None supplied | See claim | Reported reference-relative MQ comparison | General reusable knowledge exceeds evaluated domain |
| [EPI-CLM-maintenance-quality](#epi-clm-maintenance-quality) | See claim | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px4`, doctrine/design | See [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance), [EPI-RTE-telemetry-reward](#epi-rte-telemetry-reward) | None inspected | None supplied | See claim | Replacement/removal capability declared | Event reward does not itself judge correctness or staleness |
| [EPI-CLM-reward-benefit](#epi-clm-reward-benefit) | See claim | SRC-1, `2601.01885v1.html#S4.SS3`, reported operation | See [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | None inspected | None supplied | See claim | Author-reported reward-bundle comparison | Cannot attribute an individual memory action's contribution |
| [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) | See claim | SRC-1, `2601.01885v1.html#A3.SS2`, doctrine/design and reported operation | See [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation) | None inspected | None supplied | See claim | Reference evidence enters an evaluator distinct from agent confidence | No general correctness guarantee |
| [RT-CLM-tool-protocol](runtime.md#rt-clm-tool-protocol) | See claim | SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px7`, doctrine/design | See claim | None inspected | None supplied | See claim | Formatting request supports intended reward/tool parsing | Prompt does not prove enforcement or semantic truth |
| [RT-CLM-context-reset](runtime.md#rt-clm-context-reset) | See claim | SRC-1, `2601.01885v1.html#S3.SS1`, doctrine/design | See [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout) | None inspected | None supplied | See claim | Named context reset intended to promote LTM reliance | Query visibility and other channels unresolved |

## Bounded conclusion

AgeMem specifies acquisition of external contextual information, policy-proposed memory content, replacement and removal of stored entries, selected read-back, and summary replacement of active context. Retention and retrieval make candidates available for later policy interpretation; they do not establish endorsement. Source metadata is optional in the schema and described in the memory tuple, while premise-to-output provenance and actual source warrant remain unknown. Generated factual answers, summaries and replacement memories are truth-apt candidates when their scope is factual, but accessible evidence does not determine preservation, entailment or non-entailment. No warranted entailed derivation or accepted ampliative claim is established by these design descriptions alone.

The training checks have distinct licenses. Answer reward judges answer/reference fit. Storage reward labels entries using the task and expected answer. Relevance reward assesses retrieved content against the query. Preservation reward checks retention of query-derived tokens or phrases. Maintenance reward checks that a modification happened. Resource scores check economy, timing and violations. Their declared consequential consumer is the optimizer, through composite reward and group-relative advantages, not a documented per-content rejection or acceptance gate. The uniform broadcast of terminal advantage does not identify which action or proposition caused success. Summary/Filter removal and Update/Delete withdrawal change available premises without demonstrated truth checks or rollback. See the corresponding ledger routes and [RT-RTE-policy-update](runtime.md#rt-rte-policy-update).

Benchmark Qwen-Max checks support only reference-relative HotpotQA answer and supporting-fact judgments. Simulation scores support their environment objectives. The reported comparisons are evidence of the authors' performance account, not independently inspected outcomes, per-component causal attribution, or general knowledge reusability. No downstream content acceptance or lifecycle integration is established within the searched documentary routes; executable alternatives are uninspected, so this is not a system-wide absence verdict.

Outcome-responsive parameter adaptation is independently specified: rewards are intended to change future policy decisions through [RT-BAP-trained-policy](runtime.md#rt-bap-trained-policy). Reported training comparisons suggest improved future task capacity at the bundled training-treatment level, with independent exercise and finer causal attribution unestablished. Computation chooses actions and computes updates within a researcher-defined curriculum; that local autonomy does not prove reliable knowledge production. Retrieval of the agent's own store can inform maintenance, but supplied delivery and opaque processing do not close both causal directions needed to establish reflection. No formulated method-theory criticism loop is established by reward ranking. Exercised self-improvement is also unestablished: the design supplies an improvement objective and an update-to-later-policy path, but no inspectable subsequent operation causally dependent on the update. Learning, reflection, theory building and exercised self-improvement therefore remain separate findings, not one bundled negative.

## Shared records

### Operative objects

#### EPI-OBJ-memory-content
Label: Memory content

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

A material state part of the parent route, not a second declaration of the rollout. Source-native identity: content string c in a memory entry, including replacement c′. Representational form: natural-language propositions interpreted by the policy. Storage substrate: abstract LTM store; durable backend uninspected. Embeddings and metadata are separate numerical/symbolic parts, not asserted to be propositions. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px1`, `2601.01885v1.html#A1.E10`. The tuple has described source metadata, but the capture does not establish actual content lineage or acceptance.

> contains a content string and optional metadata.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-OBJ-context-content
Label: Context content

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

A material state part of the parent route. Source-native identity: message list C, including task context, retrieved content, distractors and replacement summary. Representational form: natural language interpreted by the policy; IDs and tool envelopes remain symbolic control parts. Storage substrate: abstract active context, replaced/reset within episodes; backend uninspected. Scope overlaps [RT-RTE-context-summary](runtime.md#rt-rte-context-summary) and [RT-RTE-context-filter](runtime.md#rt-rte-context-filter) as their input/output object, not as another declaration of either operation. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px1`, `2601.01885v1.html#A1.E14`; the supplied summary route retains its preservation quote.

#### EPI-OBJ-answer-content
Label: Answer content

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

Terminal content part of the parent route. Source-native identity: predicted answer A_pred. Representational form: natural-language answer interpreted by judges or recipients; answer envelope is a separate symbolic control surface. Storage substrate: output and training experience notation; archival/reload substrate uninspected. Truth-apt scope is factual answers, not every instruction or schedule. Evidence: SRC-1, `2601.01885v1.html#A1.E17`; closest supplied oracle record is [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles), which declares a claim, not this content object.

### Routes

#### EPI-RTE-language-content
Label: Language content generation

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

Endpoints/progression: presented context/store/task state → policy-generated language and memory-call content → proposed memory entries or task answer. Owner: agent policy. Source: SRC-1, `2601.01885v1.html#S3.SS1`, `2601.01885v1.html#A1.SS1.SSS0.Px7`. Distinct from the enclosing rollout's staging; Summary has its separate supplied route. A factual proposition's relation to input is indeterminate without paired semantic evidence: it could preserve facts, derive an answer or add an unsupported claim.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: generated response, possibly containing a final answer or memory content argument.
- Later read-back: memory proposals can enter LTM and later retrieved model input; response text is also appended to context in the parent rollout.
- Delegated visibility: uninspected — no executable provider boundary or delegated worker is captured.
- Selection predicate: policy distribution conditioned on the presented state and prompt.
- Invalidation or expiry: context reset/removal and memory Update/Delete can replace or withdraw generated material; correction history is uninspected.
- Activation or effect: intended input to executor or answer recipient; actual reliance is unobserved.
- Evidence limits: no paired inputs/outputs, deterministic executable transformation or accepted derivation is inspectable.

> The agent’s policy outputs either language tokens (for text generation) or structured tool calls (for memory operations).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-RTE-memory-maintenance
Label: Memory installation and maintenance

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

Endpoints/progression: policy Add/Update/Delete request → specified store insertion, replacement or removal → later retrieval candidates. Owner: model proposes content/identifier; tool function performs the described effect. This subroute owns write/disposal, not whole episode control. Closest interface record: [RT-OBJ-ltm-tools](runtime.md#rt-obj-ltm-tools). Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px3`, `2601.01885v1.html#A1.SS1.SSS0.Px4`, `2601.01885v1.html#A1.F7`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: changed store; executable response envelope uninspected.
- Later read-back: current content and embeddings become candidates for later explicit or driver retrieval within the rollout.
- Delegated visibility: inapplicable — no worker delegation is specified; policy later consumes selected entries.
- Selection predicate: model chooses content and an existing retrieved identifier for Update/Delete; Delete schema requests confirmation.
- Invalidation or expiry: Update replaces content/embedding and modification timestamp; Delete removes the selected entry; empty store initializes independent rollouts.
- Activation or effect: intended retention/revision/withdrawal of later model-input candidates, not demonstrated behavior change.
- Evidence limits: no per-entry truth test, executed identifier validation, deletion recovery, acceptance record or durable backend is inspectable.

Trigger: new information or policy judgment of outdated/incorrect content. Proposed change: add, replace or remove an entry. Admission is described tool execution of computational requests; no per-content human veto is specified. The model supplies confirmation, not an evidenced human approver. Rejection/error handling and rollback are uninspected. Reward and prompt guide selective storage and maintenance; current content, embeddings and metadata persist, not a specified criticism history. Operating mode: task solving and bounded training curriculum. Answer oracle: none specified at each write; the later training quality and answer scores use task references rather than admitting individual entries.

> These operations are particularly important in long-horizon tasks where information may become outdated or where the agent needs to correct earlier mistakes. The reward function encourages meaningful updates and deletions that improve memory quality over time.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-RTE-explicit-retrieval
Label: Explicit memory retrieval

Part of: [RT-RTE-task-rollout](runtime.md#rt-rte-task-rollout)

Endpoints/progression: model query/top-k request and current LTM → cosine ranking → selected entries inserted into context → policy reasoning. Owner: model requests, described retrieval tool ranks/delivers. Distinct from unsolicited pre-action [RT-RTE-stage-retrieval](runtime.md#rt-rte-stage-retrieval); both share the matching function. Evidence: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px2`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: top-k selected memories added to active context.
- Later read-back: accumulated LTM content reaches a later policy invocation through selected context delivery.
- Delegated visibility: inapplicable — same task policy consumes results, not a specified worker.
- Selection predicate: dense-encoding cosine top-k against the requested query, typically 3–5 entries.
- Invalidation or expiry: writes change candidates; reset/filter/summary changes delivered context.
- Activation or effect: intended influence on reasoning; delivery alone does not demonstrate factual reliance or compliance.
- Evidence limits: encoder fixity, rendered IDs/content, ties and actual use are uninspected; similarity does not assess truth.

Computational proposal/selection, with no described human per-read veto. Operating mode: task memory use. Trigger: policy requests relevant content. Answer oracle: inapplicable — selection has no expected truth outcome; a later relevance score is training feedback rather than a retrieval acceptance gate.

> making them available for immediate reasoning.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-RTE-answer-reward
Label: Answer reward judgment

Part of: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Check subroute: answer/reference or no-answer state → LLM judge/no-answer penalty → task reward → composite score and optimizer. Owner: training scorer and driver; computational evaluation within the researcher-defined curriculum. Target/domain: predicted HotpotQA answer against expected A_q, not reasoning mechanism. Model proposes the answer; judge scores it; no per-answer human veto or operational withholding gate is specified. Oracle: expected answer supplied by training data. Trigger: trajectory completion. Scorer identity is not established as Qwen-Max merely from its reported benchmark role. Source: SRC-1, `2601.01885v1.html#A1.E17`; closest supplied account is [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles).

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: score in [0,1], or default −1.0 when no answer.
- Later read-back: score contributes to changed policy parameters consumed in later training/evaluation, not a retained accepted answer.
- Delegated visibility: evaluator receives predicted and expected answers; actual provider data boundary is uninspected.
- Selection predicate: has-answer branch, otherwise penalty; judge compares reference fit.
- Invalidation or expiry: training buffer lifecycle and checkpoint recovery uninspected; no answer withdrawal is specified by this check.
- Activation or effect: declared optimization signal through group normalization; no independent action-effect attribution.
- Evidence limits: judge fidelity and score traces unavailable; answer success cannot warrant the producing process.

Supporting reward passages:

The next four records isolate check targets inside the supplied policy-update route. They do not redeclare optimization or assert a per-content acceptance gate. SRC-1, `2601.01885v1.html#A1.SS2` supplies these load-bearing passages:

> which equals 1 when the model invokes a context-reduction tool before reaching the token limit, and 0 otherwise.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> such as named entities or temporal and spatial expressions.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> indicate whether these items remain present (either directly or via a retained summary) at the time of answer generation. The preservation reward is therefore
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> are identified as high-quality based on an LLM’s analysis of the input query
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> This metric incentivizes the agent to store valuable information while avoiding the accumulation of redundant or low-quality memories.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> to encourage the agent to actively maintain the memory bank, we reward update or delete operations:
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> to quantify the semantic match between retrieved memories and the query, we introduce an LLM-based relevance assessment.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-RTE-storage-reward
Label: Storage quality reward

Part of: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Endpoints/progression: Stage 1 memory entries plus query/expected answer → LLM high-quality labels → high-quality count divided by max(1,total) → composite terminal reward. Owner: scoring procedure and driver, not content admission executor. Target: stored entries' quality for the given training task. Domain: HotpotQA curriculum; general reusable truth is not independently assessed. Oracle: q and A_q. Computational proposer is task policy, evaluator labels; researchers define objective/data. No per-entry human veto or immediate write rejection is specified. Trigger/mode: terminal reward in bounded training. Source: SRC-1, `2601.01885v1.html#A1.E23` and supporting reward passage above.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: fraction of entries labeled high-quality; empty-store denominator bounded by 1.
- Later read-back: composite reward shapes future parameters through the parent route; no retained acceptance label controlling reads is established.
- Delegated visibility: judge uses q/A_q and memory-quality assessment; exact rendered entry set/provider boundary uninspected.
- Selection predicate: LLM task/answer-relative high-quality labeling; definition and calibration uninspected.
- Invalidation or expiry: entry replacement/removal can change assessed content; score retention/recomputation uninspected.
- Activation or effect: optimizer feedback rather than described entry rejection or endorsement.
- Evidence limits: this is not established identical to benchmark MQ, which uses expected supporting facts; no raw labels or admission consumer.

#### EPI-RTE-relevance-reward
Label: Retrieved relevance reward

Part of: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Endpoints/progression: retrieved memory set and query → LLM semantic relevance score → composite reward → optimizer. Owner: training scorer. Target/domain: retrieved set's relevance to current task query, not source truth. Computational policy selects/proposes retrieval; evaluator scores; no human veto or rejection of the delivered set specified. Oracle: inapplicable — a query alone is not an expected correct answer. Trigger/mode: trajectory evaluation in bounded curriculum. Source: SRC-1, `2601.01885v1.html#A1.E25` and supporting passage above. Distinct from storage labeling and benchmark supporting-fact coverage.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: normalized semantic relevance score in [0,1].
- Later read-back: effect intended through updated policy parameters, not persisted warranted memory status.
- Delegated visibility: LLM receives retrieved set and q; actual formatting/provider boundary uninspected.
- Selection predicate: model semantic judgment against q, separate from encoder ranking.
- Invalidation or expiry: future retrieval can change the set; score expiry/storage uninspected.
- Activation or effect: contributes training reward; no direct veto on already supplied memories is described.
- Evidence limits: relevant false content can satisfy relevance; scorer version and calibration uninspected.

#### EPI-RTE-context-reward
Label: Context preservation reward

Part of: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Endpoints/progression: key query-derived tokens/phrases and final context/summary → presence indicator → preservation component → terminal reward. Owner: specified scorer; executable extraction/detection method uninspected. Target/domain: presence of named entities or temporal/spatial phrases from q at answer generation. It does not compare all source facts or their relations. Oracle: query-derived set K_q, not a reference faithful summary. Computational model proposes context changes; indicator scores their terminal result. Researchers choose the proxy; no per-summary human veto or rejection gate specified. Trigger/mode: bounded curriculum terminal scoring. Source: SRC-1, `2601.01885v1.html#A1.E21` and the supporting reward passages above.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: binary preservation indicator.
- Later read-back: composite reward shapes parameters through parent optimization; no corrected summary is specified.
- Delegated visibility: uninspected — the exact extractor/detector and its supplied context are not captured as code.
- Selection predicate: query-derived tokens/phrases remain directly or via summary.
- Invalidation or expiry: later context transformations can change presence; rollback and retained score history uninspected.
- Activation or effect: intended parameter incentive, not pre-install fidelity enforcement.
- Evidence limits: token presence cannot establish relational or propositional preservation; extraction and semantic presence criteria unspecified.

#### EPI-RTE-telemetry-reward
Label: Operational telemetry reward

Part of: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Endpoints/progression: context token count, reduction timing, maintenance events and constraint violations → formula scores/penalties → terminal composite → optimizer. Owner: training bookkeeping/scorer. Targets/domains differ: compression evaluates final token economy (E19); preventive score evaluates pre-overflow tool invocation (E20); maintenance evaluates Update/Delete occurrence (E24); penalties evaluate round/token violations (E26). These produce no factual content acceptance. Policy proposes actions, driver measures; researcher-defined formulas decide, with no per-score human veto. Oracle: event/count thresholds, not an expected factual answer. Trigger/mode: bounded training episode scoring. Source: SRC-1, `2601.01885v1.html#A1.SS2`; supplied [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) already records the maintenance/prose discrepancy and penalties. Supporting event passages are above.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: compression max(0,1−used/budget), binary preventive/maintenance signals, negative constraint penalties.
- Later read-back: parameter updates retain the behavior-shaping effect under the parent route, not telemetry as accepted factual knowledge.
- Delegated visibility: inapplicable — described bookkeeping inside the training loop, not a worker handoff.
- Selection predicate: formula predicates over event history and counts; exact instrumentation uninspected.
- Invalidation or expiry: current episode statistics; buffer/checkpoint recovery uninspected.
- Activation or effect: composite optimization incentive; cannot enforce avoidance before violation.
- Evidence limits: occurrence does not distinguish harmful from corrective maintenance; economy does not establish preservation; top-level weight scale is disputed in supplied runtime.

#### EPI-RTE-benchmark-evaluation
Label: Benchmark evaluation

This is distinct from the training subchecks above and the supplied [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles), which is an oracle claim, not a scored-output route. Endpoints/progression: trained-agent outputs and reference/environment outcomes → benchmark evaluator → reported aggregate comparisons. Owner: experimenter/evaluator. Three operative check parts have separate targets, evaluators and licenses: MQ compares stored supporting facts to HotpotQA expected facts for coverage/relevance using Qwen-Max; HotpotQA J compares generated answer to reference answer using Qwen-Max; SR/PR assess simulation-task success/progress using uninspected benchmark evaluators. Oracle inputs are dataset references for MQ/J, environment outcomes for SR/PR. Computational policy proposes outputs; computational evaluators score; researchers define/run/report comparisons, not per-content admission. Mode: bounded reported experiments. No live answer veto, memory acceptance or optimizer consumption of benchmark MQ is established. Evidence: SRC-1, `2601.01885v1.html#A3.SS2`, `2601.01885v1.html#S4.SS1`. The ledger splits these checks; their common reporting consumer permits one route container.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: MQ/J scores in [0,1] and simulation success/progress metrics, reported in comparisons.
- Later read-back: inapplicable — no retained metric feeding another target-policy invocation is described; publication is not target read-back.
- Delegated visibility: Qwen-Max receives question/reference facts or answer and predicted content; environment evaluators receive benchmark outcomes; implementation boundaries uninspected.
- Selection predicate: prompt criteria for MQ coverage/relevance and J answer equivalence; simulation scoring rules uninspected.
- Invalidation or expiry: inapplicable — reporting measurements rather than a described retained knowledge lifecycle; correction of experimental records uninspected.
- Activation or effect: researchers use scores for comparisons; no implemented ranking/admission gate in target operation is established.
- Evidence limits: aggregate paper results only; no raw judgments, independently inspected runs or causal intervention artifacts.

> The score reflects both the coverage of expected facts and the relevance of predicted facts to the question.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

> For the LLM-as-a-Judge metric on HotpotQA, we use a similar approach, where Qwen-Max evaluates the correctness of the agent’s answer by comparing it with the ground-truth answer. The evaluator uses the following prompt template:
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-RTE-mq-evaluation
Label: Memory quality evaluation

Part of: [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation)

MQ check part: stored predicted supporting facts plus question/answer and expected HotpotQA facts → Qwen-Max coverage/relevance judgment → scalar MQ → researcher reporting comparison. Owner: experimenter and Qwen-Max evaluator. Closest supplied [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) is the oracle contract claim, not this check. Distinct from answer-equivalence evaluation and training storage labeling. Oracle: dataset supporting facts. Computational agent proposes entries, judge assesses, researchers define/report the bounded experiment; no human per-entry veto or target admission consumer shown. Evidence: SRC-1, `2601.01885v1.html#A3.SS2.p2`; the parent retains the minimum coverage/relevance quotation.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: MQ score in [0,1] under prompt coverage/relevance rubric.
- Later read-back: inapplicable — no benchmark MQ feedback into another policy invocation is specified.
- Delegated visibility: judge receives question/answer, expected facts and predicted stored facts; actual formatting and provider boundary uninspected.
- Selection predicate: coverage of expected facts, relevance to answering and irrelevant predicted facts under the prompt rubric.
- Invalidation or expiry: inapplicable — measurement for reporting, not accepted-claim retention; correction lifecycle uninspected.
- Activation or effect: reporting consumer uses score for experimental comparison; no target memory veto or endorsement gate established.
- Evidence limits: no raw judgments/calibration; reference-task fit does not warrant cross-task reuse or general truth.

#### EPI-RTE-answer-evaluation
Label: Benchmark answer evaluation

Part of: [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation)

Answer check part: HotpotQA question, reference answer and generated answer → Qwen-Max equivalence/correctness score → researcher comparison. Owner: experimenter and judge. Closest supplied [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) supplies the oracle claim; distinct from training answer reward because this result feeds reporting rather than specified optimizer feedback. Oracle: dataset answer. Computational policy proposes answer, model scores, researchers define/report bounded evaluation; no live answer withholding or human per-answer veto specified. Evidence: SRC-1, `2601.01885v1.html#A3.SS2.p4`; the parent retains the reference-comparison quotation.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: J score in [0,1], with full credit requested for a perfect match or equivalent correct answer.
- Later read-back: inapplicable — no benchmark answer score feeding later policy execution is specified.
- Delegated visibility: Qwen-Max receives question, expected answer and agent answer; actual provider boundary uninspected.
- Selection predicate: prompt's graded correctness/equivalence criterion.
- Invalidation or expiry: inapplicable — reported measurement, not a specified accepted-answer lifecycle.
- Activation or effect: reporting comparison only; no implemented target-use gate established.
- Evidence limits: fallible judge and no raw outputs; answer fit does not validate reasoning process, mechanism or replay safety.

#### EPI-RTE-environment-evaluation
Label: Environment outcome evaluation

Part of: [EPI-RTE-benchmark-evaluation](#epi-rte-benchmark-evaluation)

Environment check part: benchmark task outcomes → environment success/progress scoring → researcher comparison. Owner: benchmark evaluator and experimenter; code uninspected. Target/domain: ALFWorld, SciWorld and BabyAI task success; PDDL progress. Distinct from the supplied [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) claim and Qwen-Max factual comparisons. Oracle: environment outcome/reference objective, not the policy's own confidence. Computational policy proposes actions, benchmark evaluates outcomes, researchers define/report bounded evaluation; human per-action veto and evaluator internals uninspected. Evidence: SRC-1, `2601.01885v1.html#S4.SS1`.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: SR/PR benchmark metrics.
- Later read-back: inapplicable — no reported metric feeding target policy updates is specified for these evaluations.
- Delegated visibility: uninspected — environment scoring adapters and exact state supplied are not captured.
- Selection predicate: environment success/progress rules, executable details uninspected.
- Invalidation or expiry: inapplicable — reporting outcome measurements, not retained knowledge acceptance.
- Activation or effect: researchers compare aggregate task outcomes; no implemented target admission gate established.
- Evidence limits: no raw runs or evaluator code; task success does not warrant proposed mechanism, explanation or transfer.

> For the primary task completion metrics, we adopt Success Rate (SR) for ALFWorld, SciWorld, and BabyAI, Progress Rate (PR) for PDDL, and LLM-as-a-Judge (J) for HotpotQA.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

### Claims

#### EPI-CLM-memory-quality
Label: Reusable memory quality claim

Claimed operation: high MQ demonstrates storage of high-quality reusable knowledge and selective construction. Source: SRC-1, `2601.01885v1.html#S4.SS2.p2`, reported operation. Closest supplied [RT-CLM-evaluation-oracles](runtime.md#rt-clm-evaluation-oracles) concerns the reference evaluator contract; this record concerns the authors' inference from reported metric results. MQ directly assesses HotpotQA expected-fact coverage and task relevance. It does not independently assess later cross-task reuse, general truth or durable acceptance. Reported backbone scores 0.533/0.605 support the attributed comparison only; no raw judgments or independently inspectable experiment supports stronger inference.

> This indicates that the unified memory management framework not only improves task performance but also promotes the storage of high-quality, reusable knowledge.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`

#### EPI-CLM-maintenance-quality
Label: Meaningful maintenance claim

Claimed operation: reward encourages meaningful corrections that improve memory quality and mitigate staleness. Source: SRC-1, `2601.01885v1.html#A1.SS1.SSS0.Px4`, `2601.01885v1.html#S3.SS5`, doctrine/design. Closest supplied [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) records the reward mechanism and discrepancy; this is its quality claim, not a duplicate update route. The declared E24 indicator rewards any update/delete occurrence. Quality may be indirectly discouraged/rewarded by other terminal components, so the event proxy does not prove harmful updates are globally rewarded; it also does not itself identify stale/incorrect content or meaningful repair. Illustrative preference replacement is a possible corrective case, not an enforced criterion. The maintenance quotation is retained in [EPI-RTE-memory-maintenance](#epi-rte-memory-maintenance).

#### EPI-CLM-reward-benefit
Label: Composite reward benefit claim

Claimed operation: full composite reward improves answer and memory quality relative to answer-only optimization. Source: SRC-1, `2601.01885v1.html#S4.SS3`, `2601.01885v1.html#S4.T4`, reported operation. Distinct from [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), which declares the optimization mechanism rather than this comparative inference. Table 4 reports J 0.509→0.544, MQ 0.479→0.533, tokens 2078→2117 and calls 3.93→4.92. This is a bundled reward contrast, not independent variation of storage/preservation/maintenance/relevance terms or individual actions. Increased token count is a countercase to inferring that all improved metrics imply uniformly lower resource use. The captured account lacks raw runs, evaluator error estimates and independently inspected causal experiments; supports author attribution, not isolated mechanism effects.

> To demonstrate the effectiveness of our multi-component reward function design, we compare the full reward function (All-Returns) against a variant using only
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01/sources/2601.01885v1.html`
