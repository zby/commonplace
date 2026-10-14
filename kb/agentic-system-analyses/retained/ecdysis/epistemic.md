---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Ecdysis epistemic routes: failure evidence, collaborative diagnoses, score-based harness admission and separately retained skills."
run-id: AAS-2026-10-13-ecdysis-bb4c64dbdf60-01
reviewed-boundary: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
---

# Ecdysis epistemic report

## Source-and-claim boundary

The question is what Ecdysis's harness-improvement plane acquires, infers, checks and licenses for later reliance. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). SRC-1 is the sole source. This report directly inspected the implementation paths below at the frozen commit; supplied runtime records remain provisional source-supported findings, not execution evidence. No target code was executed.

The material routes include scored-result import, deterministic failure signatures, model diagnosis and criticism, editor-mediated policy changes, aggregate-score comparison and admission, checkpoint reuse, skill checks and persistence, and inference outcome reporting. They do not include inaccessible provider internals or externally supplied production task/editor/evaluator implementations. There is no supplied observed run or causal experiment. Consequently actual criticism, task correctness, semantic editor responsiveness, improved future capacity, transfer and numerical gains remain unestablished. The opaque real harness cannot be individuated as truth-apt content; a dictionary revision in the example is policy state, not a theory of task success.

Public warrant claims are [RT-CLM-harness-training](runtime.md#rt-clm-harness-training) and the separately assessed reusable-behavior claim [EPI-CLM-learned-behavior](#epi-clm-learned-behavior).

| Entry point or operation | Source path, SRC-1 | Coverage and evidence basis | Limit / conclusion prevented |
|---|---|---|---|
| Installed dispatch and exports | `pyproject.toml`; `src/ecdysis/__init__.py`; `src/ecdysis/fdcr/__init__.py` | Direct reads; supplied runtime account distinguishes both CLIs and APIs. | No additional registered task tools or hook dispatch found in these declarations; arbitrary SDK overrides/callback effects remain external. |
| `ecdysis` result analysis | `src/ecdysis/__main__.py`; `src/ecdysis/evolution.py` | Direct reads; [EPI-RTE-failure-shaping](#epi-rte-failure-shaping). | Counts are properties of supplied records, not validated harness-deficiency explanations. |
| Extraction, grouping, mean score; FDCR API | `src/ecdysis/evolution.py`; `src/ecdysis/fdcr/review.py`; `src/ecdysis/fdcr/roles.py` | Direct reads; [EPI-RTE-failure-shaping](#epi-rte-failure-shaping), [EPI-RTE-score-check](#epi-rte-score-check), [RT-RTE-failure-review](runtime.md#rt-rte-failure-review). | Imported labels and omitted messages bound model diagnosis. |
| Training and retained inference | `src/ecdysis/training.py` | Direct read; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference). | External isolation and comparable evaluations are not enforced. |
| Checkpoint, transcript save, instruction renderer | `src/ecdysis/fdcr/review.py` | Direct read; [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), [EPI-RTE-spec-render](#epi-rte-spec-render). Transcript save is explicit JSON retention, with no built-in reload consumer beyond checkpoint's distinct format. | Saving a transcript is not acceptance; formatted imperative text does not independently license changes. |
| Plateau and regression helpers | `src/ecdysis/evolution.py` | Direct read and scoped caller search; [EPI-RTE-stability-checks](#epi-rte-stability-checks). | Runtime omitted these exposed helpers. No shipped consumer makes their booleans stop training or withdraw a harness. |
| Skill build/save/load/merge | `src/ecdysis/artifacts.py`; `src/ecdysis/evolution.py` | Direct reads; [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities), [EPI-OBJ-evolved-skill](#epi-obj-evolved-skill). | Structure, scope and ID checks do not evaluate the skill's rationale or benefit. |
| Provider content/JSON parsing and retries | `src/ecdysis/llm_client.py` | Direct read; [RT-CMP-review-model](runtime.md#rt-cmp-review-model), [RT-RTE-failure-review](runtime.md#rt-rte-failure-review). | No weight update request or exact model-version pin; provider state and semantics are uninspected. |
| Runner, benchmark API and `ecdysis-run` | `src/ecdysis/inference.py`; `src/ecdysis/benchmark.py` | Direct reads; [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference), [EPI-RTE-outcome-check](#epi-rte-outcome-check). | Exception-free execution does not establish a correct answer. Dynamic factories bypass training admission. |
| Synthetic complete driver | `examples/quickstart.py` | Direct read; supplied runtime admission and behavioral-authority records. | Editor ignores the specification; reward depends only on revision. Not an FDCR component-effect experiment. |
| Tests and package prose | `tests/`; `src/ecdysis/README.md`; `README.md` | Test/package-prose coverage supplied by boundary/runtime; README directly read for claims. | Tests are source assertions, not supplied successful runs. No additional test-origin observation is inferred. |

The new helper coverage supplements rather than supersedes the runtime's selected routes. No defective runtime identity needs replacement. Read access was available for the registered source; unavailable evidence is external implementations, model internals, paper methodology and authentic execution/comparison records, not an unavailable tracked file.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-failure-context](#epi-obj-failure-context) | Claims about rewards, termination signatures, counts and task recurrence in input records | Structured failure evidence | SRC-1, `src/ecdysis/evolution.py` | See record; provenance and correctness of upstream scoring unknown. |
| [EPI-OBJ-review-transcript](#epi-obj-review-transcript) | Possible diagnoses, objections and agreements in model replies | Collaborative review and resumable evidence | SRC-1, `src/ecdysis/fdcr/review.py` | See record; persisted text alone does not establish criticism or acceptance. |
| [EPI-OBJ-round-record](#epi-obj-round-record) | Baseline/candidate scores and reference-retention decisions | Auditable training outcome | SRC-1, `src/ecdysis/training.py` | See record; no full evidence-to-patch lineage in the round record. |
| [EPI-OBJ-proposed-changes](#epi-obj-proposed-changes) | Possible descriptions and rationales explaining harness deficiencies; actual truth-apt propositions not determinable without replies | Diagnosis and repair proposal | SRC-1, `src/ecdysis/fdcr/roles.py` | See record; policy instructions are not automatically assertions. |
| [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec) | Mixed candidate claims and instructions, including skills and implementation notes | Moderator specification | SRC-1, `src/ecdysis/fdcr/review.py` | See record; dictionary normalization establishes no semantic acceptance. |
| [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness) | Not determinable for external harness; none identified in synthetic revision state | Retained execution policy | SRC-1, `src/ecdysis/training.py` | See record; opaque payload and external interpretation. |
| [EPI-OBJ-evolved-skill](#epi-obj-evolved-skill) | Pattern can assert a general condition; tip is behavior guidance, possibly containing claims | Reusable learned behavior | SRC-1, `src/ecdysis/artifacts.py` | See record; no automatic link to accepted harness or trace provenance. |
| [RT-CMP-review-model](runtime.md#rt-cmp-review-model) | Internal representations not determinable from the client | Review evaluator/generator | SRC-1, `src/ecdysis/llm_client.py` | See record; inaccessible distributed-parametric state, mutable model resolution. |

## Authority-route ledger

Each row is a separate consequential function. `See` assigns record-owned fields to their canonical declarations rather than redeclaring them. Architectural status and transformation classification are this report's assessment. All results below are possible implemented results, not observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-failure-shaping](#epi-rte-failure-shaping) | content transformation | implemented | See record | truth-apt transformation: acquisition/import | See record | See record | See record | See record | See record | Imported score warrant unknown | See record | See record | SRC-1, `src/ecdysis/evolution.py` | none | none | See record |
| [EPI-RTE-failure-shaping](#epi-rte-failure-shaping) | content transformation | implemented | See record | truth-apt transformation: non-ampliative reshaping | See record | See record | See record | See record | See record | Conditional on supplied records; text preservation degraded by clipping/omission | See record | See record | SRC-1, `src/ecdysis/fdcr/review.py` | none | none | See record |
| [EPI-RTE-score-check](#epi-rte-score-check) | check/evidence production | implemented | See record | truth-apt transformation: entailed derivation | See record | See record | See record | See record | See record | Arithmetic over supplied finite scores; not evaluator validity | See record | See record | SRC-1, `src/ecdysis/evolution.py` | none | none | See record |
| [RT-RTE-failure-review](runtime.md#rt-rte-failure-review) | content transformation | implemented | See record | truth-apt transformation: indeterminate | See record | See record | See record | See record | See record | Candidate generation only; non-entailment depends on actual propositions | See record | See record | SRC-1, `src/ecdysis/fdcr/review.py` | [RT-CLM-harness-training](runtime.md#rt-clm-harness-training) | none | See record |
| [RT-RTE-failure-review](runtime.md#rt-rte-failure-review) | check/evidence production | implemented | See record | truth-apt transformation: indeterminate | Proposed repairs: cross-task applicability, false triggers, valid-action blocking, contract violations | Model Critic; prompt-bounded review, not an external answer oracle | See record | See record | See record | Requested criticism; no warranted diagnosis established by delivery | See record | See record | SRC-1, `src/ecdysis/fdcr/roles.py` | [RT-CLM-harness-training](runtime.md#rt-clm-harness-training) | none | See record |
| [RT-RTE-failure-review](runtime.md#rt-rte-failure-review) | disposition/acceptance | implemented | See record | truth-apt transformation: indeterminate | Moderator selection of specification | Model under conservative dispute-resolution prompt; parser only normalizes fields | See record | See record | See record | Operational proposal disposition, not evidenced acceptance of explanatory claims | See record | See record | SRC-1, `src/ecdysis/fdcr/review.py` | none | none | See record |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | behavior/policy adaptation | implemented | See record | non-truth-apt policy/content update: editor-mediated harness replacement; truth-apt internals uninspected | See record | See record | See record | See record | See record | Score does not certify editor rationale | See record | See record | SRC-1, `src/ecdysis/training.py` | [RT-CLM-harness-training](runtime.md#rt-clm-harness-training) | none | See record |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | disposition/acceptance | implemented | See record | no content change | See record | See record | See record | See record | See record | Strictly higher measured training score, assuming fixed comparable evaluation; not explanatory or transfer acceptance | See record | See record | SRC-1, `src/ecdysis/training.py` | [RT-CLM-harness-training](runtime.md#rt-clm-harness-training) | none | See record |
| [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) | retention | implemented | See record | no content change | See record | See record | See record | See record | See record | Retained policy and decision ledger, not an integrated accepted claim | See record | See record | SRC-1, `src/ecdysis/training.py` | none | none | See record |
| [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery) | lineage/freshness/recovery | implemented | See record | no content change | See record | See record | See record | See record | See record | Formatted-input/model-string compatibility, not renewed endorsement | See record | See record | SRC-1, `src/ecdysis/fdcr/review.py` | none | none | See record |
| [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery) | retention | implemented | See record | no content change | See record | See record | See record | See record | See record | Retains candidate transcript/spec before epistemic acceptance | See record | See record | SRC-1, `src/ecdysis/fdcr/review.py` | none | none | See record |
| [EPI-RTE-spec-render](#epi-rte-spec-render) | content transformation | implemented | See record | truth-apt transformation: non-ampliative reshaping | See record | See record | See record | See record | See record | Preserves displayed claims as instructions; does not establish agreement | See record | See record | SRC-1, `src/ecdysis/fdcr/review.py` | none | none | See record |
| [EPI-RTE-stability-checks](#epi-rte-stability-checks) | check/evidence production | implemented | See record | truth-apt transformation: entailed derivation | Recent score deltas below threshold | Deterministic arithmetic; signed deltas, not absolute plateau test | See record | See record | See record | Selected-window predicate only | See record | See record | SRC-1, `src/ecdysis/evolution.py` | none | none | See record |
| [EPI-RTE-stability-checks](#epi-rte-stability-checks) | check/evidence production | implemented | See record | truth-apt transformation: entailed derivation | Before-minus-after exceeds tolerance | Deterministic scalar subtraction/comparison | See record | See record | See record | Supplied-score drop only | See record | See record | SRC-1, `src/ecdysis/evolution.py` | none | none | See record |
| [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities) | check/evidence production | implemented | See record | no content change | Required dictionary fields, scope equality and identifier uniqueness | Code tests structure/metadata, not truth or efficacy | See record | See record | See record | Structural compatibility only; first ID wins, not best evidence | See record | See record | SRC-1, `src/ecdysis/artifacts.py` | [EPI-CLM-learned-behavior](#epi-clm-learned-behavior) | none | See record |
| [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities) | retention | implemented | See record | no content change | See record | See record | See record | See record | See record | Caller-supplied skills retained without epistemic acceptance | See record | See record | SRC-1, `src/ecdysis/artifacts.py` | [EPI-CLM-learned-behavior](#epi-clm-learned-behavior) | none | See record |
| [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities) | operational admission/selection/consumption | implemented | See record | truth-apt transformation: non-ampliative reshaping | See record | See record | See record | See record | See record | Scope/ID selection neither endorsement nor relevance proof | See record | See record | SRC-1, `src/ecdysis/artifacts.py` | none | none | See record |
| [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference) | operational admission/selection/consumption | implemented | See record | no content change | See record | See record | See record | See record | See record | None beyond external evaluator warrant | See record | See record | SRC-1, `src/ecdysis/inference.py` | none | none | See record |
| [EPI-RTE-outcome-check](#epi-rte-outcome-check) | check/evidence production | implemented | See record | truth-apt transformation: entailed derivation | See record | See record | See record | See record | See record | No caught executor exception; not answer correctness | See record | See record | SRC-1, `src/ecdysis/inference.py` | none | none | See record |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-harness-training](runtime.md#rt-clm-harness-training) | See record | SRC-1, `README.md`; doctrine/design and reported operation | See record | [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [EPI-RTE-failure-shaping](#epi-rte-failure-shaping) | See record: uninspected | See record; synthetic editor ignores review content, no independent FDCR variation | Recurrence-prioritized evidence and review requests are wired; strict measured-score reference admission is implemented | Recurrence does not identify harness versus model causation. Singleton repairs are not forbidden by code. Generalization, numerical gains and reduced costs remain reported, not established. |
| [EPI-CLM-learned-behavior](#epi-clm-learned-behavior) | See record | SRC-1, `src/ecdysis/artifacts.py`; doctrine/design | See record | [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities) | See record: none supplied | See record; skill construction can be manual and disconnected from scored training | Structured reusable behavior guidance can be retained and reloaded | Neither origin from failures nor learned efficacy is required; no shipped inference injection. |

The README's induction claim is doctrine/design, not an inspected causal comparison (SRC-1, `README.md`):

> Our key insight is that failures recurring across distinct tasks provide stronger inductive evidence for systematic harness deficiencies than isolated failures.
> --- `README.md`

The grouped input can also arise from a recurring model limitation: grouping observes task identity, reward components and termination labels, not an intervention separating model from harness effects. Recurrence therefore supplies a candidate-selection heuristic without identifying the causal locus. This bounds the claim; it does not refute the paper's uninspected experiments.

## Bounded conclusion

Ecdysis acquires scored trajectory assertions; it does not originate their source warrant. The evidence consumer sees signature counts and a small metadata sample, not raw trajectory messages, task descriptions or harness code. These deterministic reshaping routes license statements about the supplied records, not explanations of why an agent failed. The concrete counterexample and arithmetic boundary are retained in [EPI-RTE-failure-shaping](#epi-rte-failure-shaping) and [EPI-RTE-score-check](#epi-rte-score-check).

The FDCR schedule implements requests for diagnoses, objections and conservative revision. It affords localized explanatory candidates in [EPI-OBJ-proposed-changes](#epi-obj-proposed-changes); actual conjecture, formulated criticism and its semantic effect are unobserved. Without a concrete reply, the content edge is indeterminate rather than automatically ampliative. Moderator normalization and delivery to an editor grant operational proposal authority through [RT-BAP-review-editor](runtime.md#rt-bap-review-editor), not acceptance of an explanatory proposition against evidence.

The trainer's material admission criterion is strictly higher aggregate training score. Intended use is subsequent harness collection and inference; scope is this supplied evaluator's scored task set, contingent on fixed tasks/model/environment and nonmutating isolated callbacks. It rejects equal/lower scores by keeping a reference, not by restoring mutated payloads. Accepted reference retention reaches later execution through [RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness). This is policy selection and potential behavior adaptation, not acceptance or lifecycle integration of a claim that the proposed mechanism is true or transfers. No separate implemented route here connects accepted explanatory claims to warranted evidence; the searched operations above support that bounded finding, not a universal negative about external editors.

Checkpoint equality permits reuse and may suppress further model checks; it does not refresh semantic warrant. Skills can be saved before any acceptance, then scope/ID-selected for callers. Required-field checks and dictionary labels do not establish that a skill was learned. The renderer's instruction to implement agreed changes adds no agreement check. The exposed stability helpers return arithmetic predicates without a shipped stopping, withdrawal or rollback consumer. Inference success summaries judge exception handling, not task correctness. These remain independent route-level conclusions.

No inspected client route changes review-model parameters, and no exact provider version is pinned; inaccessible provider internals remain uninspected rather than declared incapable of learning. Learning, reflection, autonomy and self-improvement do not follow from retention or score selection alone. The runtime's independently bounded theory conditions and adapter-mediated reflection assessment remain in [RT-RTE-failure-review](runtime.md#rt-rte-failure-review); its improvement pathway limits remain in [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission). The source's synthetic revision reward and specification-ignoring editor are a countercase to FDCR-content attribution. The absent run/comparison evidence prevents demonstrated benefit, not the implemented existence of the review and selection paths.

## Shared records

### Operative objects

#### EPI-OBJ-review-transcript
Label: Review transcript

Source-native identity: `transcript`, a list of symbolic role/content dictionaries carrying natural-language model replies in process memory and optional checkpoint JSON. Closest supplied record is [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), which owns its production and reuse route, not a separately declared transcript object. Unlike [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec), the transcript includes intermediate Analyst/Critic/Engineer turns and appended normalized Moderator output. It can carry localized hypotheses, criticism and agreement, but no supplied instance establishes their truth-apt content. Model consumers receive the last twelve turns, while checkpoint persistence retains the full list; this distinction prevents treating retained history as complete model-visible evidence. SRC-1, `src/ecdysis/fdcr/review.py`, implementation; the supplied parent route retains the load-bearing history-slicing passage.

> transcript.append({"role": role, "content": content.strip()})
> --- `src/ecdysis/fdcr/review.py`

#### EPI-OBJ-round-record
Label: Round record

Source-native identity: `RoundRecord` instances in `TrainingResult.rounds`, symbolic scalar/boolean/string fields in immutable dataclasses and an in-memory tuple. This decision-evidence object is distinct from [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness), whose identity includes the retained harness payload; the parent [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission) describes construction. Scores and acceptance fields assert what the collector/scorer and reference decision returned; they do not retain the trajectory evidence, review transcript or actual patch. No automatic durable round-record reload is implemented. SRC-1, `src/ecdysis/training.py`, implementation.

> accepted=accepted,
> status="accepted" if accepted else "rejected",
> --- `src/ecdysis/training.py`

#### EPI-OBJ-failure-context
Label: Failure context

Source-native identity: `_format_failure_context` output and the structured records it renders. Symbolic rewards, task IDs and signature keys are stored in Python dictionaries; the formatted context is text in memory and supplies model-visible evidence through interpretation. This is a distinct input object within [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), not the moderator's [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec). Its claims concern supplied records: recurrence counts can be checked internally but evaluator truth and distinct real task identity are not authenticated. SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/review.py`, implementation.

> evidence_role = "recurring" if len(task_ids) >= 2 else "auxiliary"
> --- `src/ecdysis/fdcr/review.py`

> for f in failures[:12]:
> --- `src/ecdysis/fdcr/review.py`

#### EPI-OBJ-proposed-changes
Label: Proposed changes

Part of: [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec)

Source-native identity: `spec["proposed_changes"]`, a list in memory and optional checkpoint JSON. Symbolic field structure carries natural-language component descriptions and rationales for an external editor. The Moderator prompt requests a unit capable of stating a causal hypothesis, but the parser permits arbitrary list contents; actual proposition, scope and assumptions are not determinable without replies. Other spec parts carry patterns, skills and notes with different roles. SRC-1, `src/ecdysis/fdcr/roles.py`, doctrine/design; `src/ecdysis/fdcr/review.py`, implementation.

> "  proposed_changes: list of {component, description, rationale}\n"
> --- `src/ecdysis/fdcr/roles.py`

> "proposed_changes": list(parsed.get("proposed_changes") or []),
> --- `src/ecdysis/fdcr/review.py`

#### EPI-OBJ-evolved-skill
Label: Evolved skill

Source-native identity: `EvolvedSkill` fields `id`, `title`, `pattern`, `tip` and optional provenance/metadata. Symbolic identifiers and task-ID metadata accompany natural-language patterns and tips in Python dataclasses and JSON artifacts. This is a stored utility object inside the scope of [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities), not necessarily the optional skill dictionary inside [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec); no conversion between those specific instances is automatically performed. Provenance fields can be empty; pattern/tip correctness and actual learned origin are not checked. SRC-1, `src/ecdysis/artifacts.py`, implementation.

> source: str = "evolution"
> source_task_ids: list[str] = field(default_factory=list)
> --- `src/ecdysis/artifacts.py`

### Routes

#### EPI-RTE-failure-shaping
Label: Failure evidence shaping

Part of: [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)

Endpoints/progression/owner: evolution code imports collector dictionary/file records, selects below-threshold rewards, compacts messages, groups signatures and review code formats model context. [EPI-OBJ-failure-context](#epi-obj-failure-context) owns the input representation. Import preserves available labels but source warrant is unknown. Message clipping, dropping nonselected fields and metadata-only model delivery degrade evidence completeness, even when structured labels are preserved. Summary counts derive from records rather than diagnosing causes. The editor receives fuller extracted failures than the model. Proposers/deciders are the upstream collector and deterministic code; no human per-record approval or internal correctness oracle is wired.

- Immediate return: Extracted records, grouped records and formatted evidence text; CLI prints group counts.
- Later read-back: Formatted context selects compatible checkpoint reentry; retained transcript/spec can reenter later review calls through the parent route.
- Delegated visibility: Model sees counts, up to eight task IDs per group and first twelve metadata samples; editor additionally sees compacted messages and task data.
- Selection predicate: Available reward below configured threshold; failure grouping uses termination and components below 1.0; all groups, including singleton auxiliary groups, reach review.
- Invalidation or expiry: Parent checkpoint context hash mismatch rejects reuse; no independent upstream-score validation or expiry.
- Activation or effect: Code selects review input and nonempty-failure trigger; actual diagnosis from its meaning is unobserved.
- Evidence limits: Counts establish record recurrence, not independent trials or systematic harness causation; raw provider/task behavior uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete implementation deduction, not execution: with task ID `a`, reward 0, termination `stopped`, breakdown `{execution: 0}`, and message content `ABCD`, extraction with `max_content_chars=2` produces content `AB`. Grouping produces `stopped:execution`. Review displays reward/signature/task identity but neither `AB` nor the task text. Changing the message to `WXYZ` changes the editor's compact message to `WX`, yet leaves model context and its checkpoint hash unchanged if metadata is unchanged. Thus neither review access to the actions nor hash coverage of full evidence follows. SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/review.py`, implementation.

> compact["content"] = str(content)[:max_content_chars]
> --- `src/ecdysis/evolution.py`

> sample.append(
>     f"  task={f.get('task_id')} trial={f.get('trial')} "
>     f"reward={f.get('reward')} term={f.get('termination_reason')} "
>     f"breakdown={f.get('reward_breakdown')}"
> )
> --- `src/ecdysis/fdcr/review.py`

#### EPI-RTE-score-check
Label: Aggregate score check

Part of: [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)

Endpoints/progression/owner: collector results enter caller scorer; the default `mean_trajectory_score` converts available rewards to floats and returns their arithmetic mean, consumed by trainer comparison. This isolates evidence production from the parent disposition. Target/domain: aggregate of available scored simulations, not task-answer truth. For finite numeric inputs, `[0, 1]` entails mean `0.5`; missing rewards are excluded, not scored zero. Nonfinite rewards are not rejected here. External custom scorer semantics, reference outcomes and sample comparability are uninspected; the synthetic oracle is revision >= 1. Collector/scorer supply evidence, trainer decides and vetoes reference replacement, caller chooses adapters/configuration.

- Immediate return: Float score or exception if no scored trajectories.
- Later read-back: Score values enter parent RoundRecords; retained harness is recollected in the next round rather than blindly reusing this score.
- Delegated visibility: Scorer sees results; trainer consumes scalar; diagnostic review sees selected reward metadata, not a correctness oracle.
- Selection predicate: All dict simulations with a non-None reward; custom scorers are caller-selected.
- Invalidation or expiry: Recomputed per collection; no evidence-validity expiry or finite-reward guard in default scorer.
- Activation or effect: Comparison consumes scalar to accept/reject reference replacement; no claim-level warrant gate.
- Evidence limits: Arithmetic check is conditional on inputs; real benchmark truth, fixed sampling and held-out validity uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/training.py`, implementation. Acceptance/rejection and retained consumer are owned by the parent; they are not conflated with this score production.

> if not scores:
>     raise ValueError("results contain no scored trajectories")
> return sum(scores) / len(scores)
> --- `src/ecdysis/evolution.py`

#### EPI-RTE-spec-render
Label: Update specification rendering

Distinct identity: closest supplied route is [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), which generates a dictionary. `format_update_spec` is a separately exported formatter accepting caller-supplied dictionaries, not a required trainer step. Code maps supplied descriptions/rationales to text and appends implementation instructions; it does not check truth or determine whether parties agreed. This is non-ampliative display of supplied claims plus non-truth-apt imperative scaffolding. Target domain is spec formatting. Generic caller owns later use; no per-content human approval is established.

- Immediate return: Markdown-like implementation instruction string.
- Later read-back: inapplicable — function does not persist output or provide a reload path.
- Delegated visibility: Caller sees rendered patterns, component descriptions/rationales, JSON skills and notes.
- Selection predicate: Nonempty named fields are displayed; caller explicitly invokes formatter.
- Invalidation or expiry: inapplicable — no store, version or expiry check.
- Activation or effect: Advisory imperative delivered to caller; no shipped consumer executes its contents.
- Evidence limits: Rendering does not establish agreed status or compliance by any external coding agent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `src/ecdysis/fdcr/review.py`, implementation.

> lines.append(
>     f"- [{ch.get('component', '?')}] {ch.get('description', '')}: "
>     f"{ch.get('rationale', '')}"
> )
> --- `src/ecdysis/fdcr/review.py`

> "\nImplement only the agreed changes. Keep edits minimal and test-safe."
> --- `src/ecdysis/fdcr/review.py`

#### EPI-RTE-stability-checks
Label: Score stability checks

Distinct identity: these exposed `check_convergence` and `check_regression` helpers have no counterpart in supplied records; closest score-selection mechanism is [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), whose trainer never calls them. Each helper has its own target: recent-window signed score deltas versus threshold, or before/after scalar drop versus tolerance. Code is evaluator and returns a boolean; callers may decide its use but no shipped consequential consumer is wired. Operating mode is explicit helper invocation, not automatic curriculum termination. No internal answer oracle, human approval, proposal generation or revision occurs.

- Immediate return: Boolean predicate; convergence additionally rejects window < 2 and returns false for insufficient records.
- Later read-back: inapplicable — helpers store neither inputs nor results.
- Delegated visibility: Caller supplies scalar scores/score dictionaries and receives the boolean.
- Selection predicate: Convergence uses final window records, default missing score zero; regression uses both supplied scalars.
- Invalidation or expiry: inapplicable — stateless calculations, with no persisted version or expiry.
- Activation or effect: No shipped stop, rejection, withdrawal or rollback consumer; potential external boolean use is uninspected.
- Evidence limits: Neither helper establishes correct answers, mechanism truth, stable generalization or improvement; signed negative deltas can count as convergence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `src/ecdysis/evolution.py`, implementation. Caller search for both names covered `src`, `tests`, `examples`, `README.md` and `pyproject.toml` at the frozen revision; only definitions were found. Concrete deduction: scores `[1.0, 0.5, 0.0]` give deltas `[-0.5, -0.5]`, whose maximum is below default 0.005, so convergence returns true despite a sustained decline. Regression separately returns true for `before=1`, `after=0`, default tolerance 0.05. No inference that convergence implies non-regression is warranted.

> return max(deltas) < threshold
> --- `src/ecdysis/evolution.py`

> return (before_score - after_score) > tolerance
> --- `src/ecdysis/evolution.py`

#### EPI-RTE-outcome-check
Label: Inference outcome check

Part of: [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference)

Endpoints/progression/owner: inference code catches executor exceptions, records output/error and counts `succeeded` records; benchmark wraps these records and emits metadata/JSONL. Target/domain is caught-exception status, not answer quality. Code decides continuation under caller's fail_fast option; executor supplies output. No reference answer is consulted. The outcome/error object is a material reporting part of the broader execution route rather than an independent evaluator of task correctness.

- Immediate return: Per-task record, aggregate success/failure counts, optional exception propagation under fail_fast.
- Later read-back: JSONL may be explicitly retained by caller; no automatic package reload or training feedback is wired.
- Delegated visibility: Caller/encoder receives task, identifier, output/error and timing; benchmark adds name/version/split.
- Selection predicate: Task iteration order; succeeded means error is None; exceptions govern failed records.
- Invalidation or expiry: inapplicable — immutable result wrapper has no truth/freshness invalidation policy.
- Activation or effect: With fail_fast false, caught executor failure records allow later tasks; fail_fast true raises. Counts are reporting, not answer acceptance.
- Evidence limits: Wrong but exception-free output counts as succeeded; external output evaluation and task/factory effects are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, implementation. Countercase: executor returning an incorrect string without raising creates a record with `error=None` and therefore success; no domain oracle distinguishes it.

> @property
> def succeeded(self) -> bool:
>     return self.error is None
> --- `src/ecdysis/inference.py`

### Claims

#### EPI-CLM-learned-behavior
Label: Reusable learned behavior

Claimed operation: `EvolvedSkill` describes its content as reusable behavior learned from failure evidence; README maps `SkillArtifact` to reusable learned behavior. Closest supplied claim is [RT-CLM-harness-training](runtime.md#rt-clm-harness-training), about generalization/efficiency of harness training, not the provenance and warrant of stored skills. SRC-1, `src/ecdysis/artifacts.py`, `README.md`, doctrine/design. Implementation supports serialization and explicit load/merge, not automatic learned origin, efficacy validation or downstream inference use. No observed or causal support is supplied.

> """A reusable behavior learned from failure evidence."""
> --- `src/ecdysis/artifacts.py`

> required = ("id", "title", "pattern", "tip")
> missing = [key for key in required if not data.get(key)]
> --- `src/ecdysis/artifacts.py`
