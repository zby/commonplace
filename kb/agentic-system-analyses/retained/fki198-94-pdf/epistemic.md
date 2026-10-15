---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Incremental self-improvement's measurement, historical usefulness and live policy authority in the revised FKI-198-94 capture."
run-id: AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01
reviewed-boundary: fki198-94-revised-1995-01-31-captured-2026-10-14-text
---

# Incremental self-improvement epistemic report

## Source-and-claim boundary

The question is what the documented runtime can know from inputs and reward, what its usefulness test licenses, and how that result changes later behavior. The source identity and evidence layers are those of the [boundary Source register](boundary.md#source-register), SRC-1. This is a complete captured paper, partial execution loop: design and reported operation, not inspected implementation or observed execution. Direct source inspection here covers the abstract and §§1–5.3, including Table 1, Table 2 and the contrary cases in §4. The supplied runtime is provisional supporting evidence, not an implementation witness.

The public warrant claims assessed are [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant), [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison), and the forward-looking assumption in [EPI-CLM-future-usefulness](#epi-clm-future-usefulness). Broad universality is a capacity claim, not evidence that any particular conjecture or explanation was produced. A source-native numerical policy can guide action without being a truth-apt proposition about the world.

| Entry point or operation | Source path/anchor | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Birth, interpreter dispatch, normal arithmetic and branching, Stop and syntax halts | SRC-1, captured text §3.2, Table 1 | Direct read; [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle) | No executable dispatch or concrete sampled trace; cannot individuate semantic content of arbitrary computed cells |
| Input writes, variable Read/Write, maze movement, goal and obstacle inputs | SRC-1, captured text §§3.2, 5.1–5.2, Table 2 | Direct read; [EPI-RTE-input-supply](#epi-rte-input-supply) | Exact Read destination damaged/inconsistent; arbitrary environment encoding and corrupted-input reliability unknown |
| GetP | SRC-1, captured text §3.2, Table 1 | Direct read; [EPI-RTE-getp-read](#epi-rte-getp-read) | No code or GetP-use trace; no independently demonstrated reflection benefit |
| IncP/DecP, validity limits, live sampling, EndSelfMod | SRC-1, captured text §§3.2, 4 comments 1–2 | Direct read; [RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection) | No independently inspected installation or activation; effects precede evaluation |
| Stack snapshots, reward/time comparison, retention and reverse restoration | SRC-1, captured text §§3.2, 4 comments 5–7, 17–19 | Direct read; [EPI-RTE-rate-comparison](#epi-rte-rate-comparison), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment) | No raw stack/reward trace; no causal attribution to an individual modification |
| Teacher input/reward shaping; direct forcing; repeated-code variant; circular history; additional introspection | SRC-1, captured text §4 comments 11, 15–16, 19 | Direct read; qualifications to [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant) | Optional designs, not established active routes; additional stack-inspection primitives explicitly not yet implemented |
| Enabled/disabled experiments, corrupted-input variant | SRC-1, captured text §§5.1–5.3 | Direct read; [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison) | Narrative only; no independently inspectable experiment or component-level intervention |
| CLI, hooks, registered tools, external callbacks, restart, distributed-parametric variants | No implementation supplied; SRC-1 §5.3 discusses richer primitives | Boundary exclusion and supplied runtime limit | Cannot check frozen implementation dispatch or claim a system-complete negative; proposed neural primitives do not establish a distributed-parametric route |
| Historical related systems and references | SRC-1 §§6–7 and bibliography | Supplied boundary coverage only; not directly reassessed here | Not routes of the selected concrete runtime; referenced systems remain outside capture |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-input-cells](#epi-obj-input-cells) | Encoded goal, local obstruction, variable values/counts and runtime state, over the documented tasks | see record | SRC-1 §§3.2, 5.1–5.2 | Acquired observations; corrupted inputs defeat unconditional source warrant |
| [EPI-OBJ-getp-values](#epi-obj-getp-values) | Scaled numerical representation of a current policy probability | see record | SRC-1 §3.2, Table 1 | Quantized, not an exact copy; no exercised introspection trace |
| [EPI-OBJ-rate-comparison](#epi-obj-rate-comparison) | Historical reward-rate ordering at evaluation time | see record | SRC-1 §3.2 | Entailed only given accurate supplied totals, timestamps and comparator; not causation or future prediction |
| [RT-OBJ-stack](runtime.md#rt-obj-stack) | Snapshot time, reward and old distribution have historical referents | see record | SRC-1 §3.2 | Bookkeeping retains inputs to future checks, not a theory or successful program's explanation |
| [RT-CMP-probability-distributions](runtime.md#rt-cmp-probability-distributions) | None identified: selection weights, not probabilities of named propositions | see record | SRC-1 §3.2 | Practical bias may embody experience without individuating truth-apt learned assertions |
| [RT-OBJ-program-area](runtime.md#rt-obj-program-area) | None individuated: sampled instructions/arguments | see record | SRC-1 §3.2 | Executable code may compute truth-apt results, but universality alone does not identify one |
| [RT-OBJ-work-area](runtime.md#rt-obj-work-area) | Other cells: not determinable | see record | SRC-1 §§3.2, 5.1.2 | Inputs and GetP parts split above; arbitrary arithmetic and messy stored integers have no supplied semantic lineage |

## Authority-route ledger

Route ID: [EPI-RTE-input-supply](#epi-rte-input-supply)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-input-cells](#epi-obj-input-cells)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Environment/runtime quantities enter designated integer cells.
Evaluator/condition and domain: No admission evaluator for input truth; task driver specifies encoding.
Activation and timing: At time steps or task-specific events; see record.
Possible or observed result: Available encoded input; reported operation only.
Implemented force: No inspected implementation; design delivers readable state.
Epistemic authority and scope: Source warrant conditional on correct encoding; unknown for arbitrary environments, degraded in reported corrupted-input experiment.
Operational authority: Inputs can influence subsequent branching and updates without a truth check.
Behavioral-authority path: Interpreter; work-cell operands; permissive availability, enforcing primitive semantics if selected; current and subsequent runs until overwrite.
Evidence source ID and local anchor: SRC-1 §§3.2, 5.1–5.2; see record.
Claim IDs: none
Mismatch marker: none
Gap/limit: Partial observation is not a unique maze-position description. Delivery does not prove use or accuracy.

Route ID: [EPI-RTE-getp-read](#epi-rte-getp-read)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-getp-values](#epi-obj-getp-values)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Current addressed probability to scaled work-cell value.
Evaluator/condition and domain: Fixed primitive contract, not a separate semantic judge.
Activation and timing: Selected valid GetP execution; see record.
Possible or observed result: Rounded numerical self-representation.
Implemented force: No inspected implementation; documented write permits later computation.
Epistemic authority and scope: Current policy value to the encoding's resolution, not value of the policy or future reward.
Operational authority: Subsequent instructions may use this representation in modifiers or other computations.
Behavioral-authority path: Interpreter; work-cell arithmetic/operands; permissive availability, enforcing primitive semantics; until overwrite, with no automatic refresh of old copies.
Evidence source ID and local anchor: SRC-1 §3.2, Table 1; see record.
Claim IDs: none
Mismatch marker: none
Gap/limit: No concrete code transformation or trace exists in boundary; architectural introspection is declared, not independently observed.

Route ID: [EPI-RTE-rate-comparison](#epi-rte-rate-comparison)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-rate-comparison](#epi-obj-rate-comparison), [RT-OBJ-stack](runtime.md#rt-obj-stack)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Historical average reward rate since newest surviving program's beginning versus predecessor's beginning or birth.
Evaluator/condition and domain: Fixed top-level arithmetic, over supplied R(t) and elapsed computational-cost time; see record.
Activation and timing: Completed instruction outside incomplete self-modification; repeated during restoration.
Possible or observed result: Strict exceedance or non-exceedance; source-reported tests, no observed values.
Implemented force: No inspected implementation; design result feeds keep/restore decision.
Epistemic authority and scope: Historical ordering under accurate inputs and source-defined timing, not causal effectiveness, transfer or future utility.
Operational authority: Check result supplies the immediate condition to retention/restoration.
Behavioral-authority path: Fixed top-level; comparison predicate; enforcing by design; present evaluation with later reevaluation.
Evidence source ID and local anchor: SRC-1 §3.2, §4 comments 6–7; see record.
Claim IDs: [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant), [EPI-CLM-future-usefulness](#epi-clm-future-usefulness)
Mismatch marker: Causal or future warrant would exceed evaluator domain.
Gap/limit: This is documentary conditional derivation, not verified executable arithmetic or independently validated proof; damaged formulas limit exact reconstruction.

Route ID: [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [RT-CMP-probability-distributions](runtime.md#rt-cmp-probability-distributions)
Content/update relation: no content change
Transition or check target: Continued retention of live probability changes.
Evaluator/condition and domain: see record; historical strict reward-rate comparison.
Activation and timing: see record; checking suspended during incomplete programs.
Possible or observed result: Keep or pop/restore; reported operation, not observed execution.
Implemented force: see record; implementation uninspected.
Epistemic authority and scope: Operational acceptance for continued policy use in this life. No evidence-consuming acceptance of a new explanatory or predictive claim is established.
Operational authority: Continue live changes or revoke their direct effects.
Behavioral-authority path: see [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection); enforcing by design after check, provisional thereafter.
Evidence source ID and local anchor: SRC-1 §§3.2, 4 comments 1, 5–7; see record.
Claim IDs: [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant)
Mismatch marker: Operational usefulness is not causal proof.
Gap/limit: Testing follows installation; indirect effects survive rejection. No supersession of supplied runtime needed.

Route ID: [RT-RTE-self-modification](runtime.md#rt-rte-self-modification)
Route function: retention
Architectural status: doctrine only
Object/candidate ID: [RT-OBJ-stack](runtime.md#rt-obj-stack)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Internal current distribution, time and total reward copied into restoration history before a change.
Evaluator/condition and domain: see record; effective valid modifier, not epistemic approval.
Activation and timing: see record; before modification and before usefulness check.
Possible or observed result: New snapshot; stack activity reported.
Implemented force: see record; no inspected implementation.
Epistemic authority and scope: Historical lineage for restoration and comparison, conditional on correct bookkeeping; retention does not certify a proposal.
Operational authority: Enables later grouping, reward-rate evaluation and rollback of direct policy changes.
Behavioral-authority path: Top-level; S fields/oldP; enforcing restoration semantics by design; subsequent evaluations within life.
Evidence source ID and local anchor: SRC-1 §3.2, §4 comments 17–19; see record.
Claim IDs: [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant)
Mismatch marker: none
Gap/limit: Pre-check history is not lifecycle integration of accepted knowledge; finite/circular history qualifies restoration.

Route ID: [RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)
Route function: behavior/policy adaptation
Architectural status: doctrine only
Object/candidate ID: [RT-CMP-probability-distributions](runtime.md#rt-cmp-probability-distributions)
Content/update relation: non-truth-apt policy/content update: reweight or restore instruction/argument selection probabilities
Transition or check target: Live sampling bias.
Evaluator/condition and domain: Modifier validity at write; historical usefulness at later retention; see records.
Activation and timing: Immediate after effective modifier, then possible restoration after EndSelfMod.
Possible or observed result: Changed action and future modifier probabilities; reported exercise, no independent activation trace.
Implemented force: see records and [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection).
Epistemic authority and scope: No specific learned truth-apt proposition individuated; policy authority does not require one.
Operational authority: Changes later instruction selection, including computation of future self-changes.
Behavioral-authority path: see [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection).
Evidence source ID and local anchor: SRC-1 §§3.2, 5.1.2, 5.2.2; see records.
Claim IDs: [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison), [EPI-CLM-future-usefulness](#epi-clm-future-usefulness)
Mismatch marker: none
Gap/limit: Restoring weights withdraws operational authority, not environmental consequences or a recorded proposition's endorsement.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant) | see record | SRC-1 §3.2 FACT 3, doctrine/design | Recursive historical-rate criterion and restoration | None inspected; documented [EPI-RTE-rate-comparison](#epi-rte-rate-comparison), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment) | None; reported stack activity only | Incomplete programs delay checks; only direct distribution effects restored; accurate accounting required | Conditional design invariant over retained completed modifications | Not a proof of causal or future usefulness |
| [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison) | see record | SRC-1 §§5.1–5.3, reported operation | Live policy adaptation and reward-rate disposition | None inspected; documented [RT-RTE-self-modification](runtime.md#rt-rte-self-modification) | None supplied | Bundled enabled/disabled modifiers; no raw artifact, independent component variation or statistical evaluation | Attributed task-performance benefit over described lives | Does not establish which update, GetP use, mechanism of a breakthrough, or transfer caused benefit |
| [EPI-CLM-future-usefulness](#epi-clm-future-usefulness) | see record | SRC-1 §4 comments 6, 14, doctrine/design | Continue currently qualifying policies and recheck later | None inspected; documented [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment) | None supplied | Single non-repeatable trajectory; future environment unconstrained | Historical experience operationally guides future sampling | Assumption, not accepted predictive knowledge; source explicitly permits harmful flukes |

## Bounded conclusion

The documented system acquires task observations and reward; its warrant is conditional on the driver's encoding and weaker in the corrupted-input variant. GetP reshapes a localized current policy value into a quantized self-representation. Snapshot history preserves reward/time and prior distributions for later comparison and restoration. Neither ordinary storage nor these copies establish acceptance of new claims.

The fixed evaluator derives historical rate orderings from accumulated outcomes and timestamps. Its check target is completed policy-change history, its domain is source-defined computational time and payoff, and its operative consumer is the keep/restore loop. The named acceptance criterion is strict rate exceedance against the predecessor or birth, for continued policy use within one life. This licenses operational continuation under a revisable criterion, not a causal explanation or a future-performance proposition. Retention, checking, disposition and adaptation remain separate even where one stack-based algorithm supplies them.

Policy weights affect later primitive and argument sampling, including future modifiers. New weights are live before a check; EndSelfMod reenables evaluation. Rejection restores only direct policy effects. Source-supported contrary cases—delayed evaluation, flukes, later harmful consequences and teacher-forcing proposals—exclude a stronger safety, causal or universal-future-warrant interpretation.

The boundary does not individuate a produced ampliative truth-apt claim, evidence-consuming acceptance of such a claim, or subsequent lifecycle integration. Arbitrary programs and stored integers remain semantically unresolved, not proven non-truth-apt. The prospective usefulness assumption is stated by the author, not an independently located proposition retained and criticized by the machine. Thus no system-complete negative about knowledge production or theory building follows. Sampling programs and score-based retention alone do not establish content-directed criticism.

Learning benefit is reported for toy tasks, not independently causally established. GetP supports a declared bidirectional introspection affordance; beneficial exercised reflection is separately unestablished. Computational proposal and retention roles coexist with human primitive/reward design. For self-improvement within this runtime and one life, outcome evidence shapes retention, retained changes alter its own policy, and the policy reaches the sampler by design; exercised dependence and component-specific success remain reported rather than independently verified. These independent conclusions warrant no single epistemic score.

## Shared records

### Operative objects

#### EPI-OBJ-input-cells
Label: Task and runtime input cells
Part of: [RT-OBJ-work-area](runtime.md#rt-obj-work-area)

Source-native identity: designated input cells receiving environment values and, in experiments, IP, sp and time-derived values. Representational form: symbolic integer encodings. Storage substrate: work array. This material part is split from the work-area container because its external/runtime producers and defined observation semantics differ from arbitrary computed integers. SRC-1 §§3.2, 5.1–5.2. The maze signal is local, not an encoded full position. Input corruption limits source warrant.

> Another input cell is lled with a 1 whenever
> the agent is on the goal eld, otherwise it is lled with a 0.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> In another experiment, the system was applied to the same
> task, but inputs were corrupted and unreliable.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### EPI-OBJ-getp-values
Label: Scaled current probability values
Part of: [RT-OBJ-work-area](runtime.md#rt-obj-work-area)

Source-native identity: work-cell values written by GetP. Representational form: symbolic scaled/rounded integers, not distributed weights. Storage substrate: work array. This part has a defined policy-value referent and dedicated producer, unlike the remaining work cells; its producer also appears in the broader [RT-RTE-self-modification](runtime.md#rt-rte-self-modification). Values describe the policy at read time and can become stale after modifications. SRC-1 §3.2, Table 1; exact extraction of operand formulas is not used.

> The primitive GetP can be used to write scaled versions of current probability values into work cells.
> GetP is potentially useful for purposes of introspection.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### EPI-OBJ-rate-comparison
Label: Current reward-rate comparison result

Source-native identity: current exceedance/non-exceedance of the two historical payoff/time ratios used by the top-level. Representational form: symbolic arithmetic comparison predicate. Storage substrate: transient evaluator state; no separately persisted result artifact specified. Distinct from the saved inputs in [RT-OBJ-stack](runtime.md#rt-obj-stack) and machinery in [RT-CMP-top-level](runtime.md#rt-cmp-top-level). This is a truth-apt historical ordering conditional on supplied totals/timestamps, not the candidate policy itself. SRC-1 §3.2; source prose below supplies the undamaged comparison contract.

> FACT 1. At a given time, to decide whether the most recent useful self-modi cation pro-
> gram remains useful, one needs to compare its current payo /time ratio only to the current
> payo /time ratio of the most recent previous useful self-modi cation program.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Routes

#### EPI-RTE-input-supply
Label: Supply encoded task and runtime observations
Part of: [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)

Endpoints/progression: environment/driver and runtime quantities → designated work inputs → optional later primitive consumption. Owner: task interface or runtime bookkeeping, not the sampled program. Context/state: current task and machine state; writes overwrite input cells. This material input subroute is split from the instruction-cycle container, whose supplied finding already mentions task inputs. SRC-1 §§3.2, 5.1–5.2.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: Encoded observation in a designated input cell; task reward also contributes to cumulative payoff.
- Later read-back: Inputs may survive a run halt and reach later runs until rewritten; variable Read copies also enter work storage, with exact destination unresolved.
- Delegated visibility: inapplicable — no delegated workers in the documented loop.
- Selection predicate: Driver-specific input assignment; valid addressed Read and selected work operands determine consumption.
- Invalidation or expiry: New environment/runtime writes overwrite input values; no truth or endorsement invalidation rule is specified.
- Activation or effect: Primitive execution can read the cells; no trace demonstrates which observations produced a reported outcome.
- Evidence limits: Doctrine and reported experiment only; corruption and partial observability prevent unconditional world-state warrant.

> Environmental inputs. At every time step, new inputs from the environment may be written into
> the input cells.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> Every 1000 time steps, the
> number of variables whose values equal their addresses is written into a special input cell. This
> number is the current payo . Then, all variables are re-initialized with zeros.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### EPI-RTE-getp-read
Label: Read scaled current policy probability
Part of: [RT-RTE-self-modification](runtime.md#rt-rte-self-modification)

Endpoints/progression: addressed current Pi entry → GetP scaling/rounding → work cell → optional later arithmetic/modifier operand. Owner: fixed primitive semantics, selected by sampled instruction execution. This dedicated self-representation route is a material part of the supplied self-modification account, not a second identity for its probability-write route. SRC-1 §3.2, Table 1; evidence passage is in [EPI-OBJ-getp-values](#epi-obj-getp-values).

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: Scaled probability integer written into a work cell.
- Later read-back: Result can survive run halt and be read by later instructions/runs until overwritten.
- Delegated visibility: inapplicable — same interpreter reads the resulting work state.
- Selection predicate: Selected GetP with valid indirect source and work destination operands.
- Invalidation or expiry: Overwrite changes copy; later policy changes need not refresh existing copied values.
- Activation or effect: Design allows self-representation to enter computations that affect later policy; no supplied exercised-use trace.
- Evidence limits: No inspected code permits concrete deterministic input tracing; numerical quantization and extraction damage bound reconstruction.

Reflection: policy changes affect future GetP representations; representation-mediated computation can affect future policy through modifiers. This is a design affordance, not demonstrated exercised reflection or its causal contribution to benefit. This read alone admits no policy revision and has no separate answer oracle.

#### EPI-RTE-rate-comparison
Label: Compare current historical payoff rates
Part of: [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)

Endpoints/progression: current R(t), t, newest program-start snapshot and preceding start/birth → rate arithmetic → comparison predicate → separate keep/restore disposition. Owner: fixed top-level. State includes stack first pointers and saved reward/time; restoring distributions consumes time and prompts further comparison. This is the checking part of the supplied credit-assignment container, not a replacement of its keep/restore finding. SRC-1 §3.2, §4 comments 6–7. See [EPI-OBJ-rate-comparison](#epi-obj-rate-comparison) and [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment) for load-bearing comparison and restoration passages.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: Comparison predicate consumed immediately by keep/restore control flow.
- Later read-back: inapplicable — no separately retained comparison result specified; subsequent checks recompute from current totals and surviving snapshots.
- Delegated visibility: inapplicable — internal top-level, no delegated evaluator.
- Selection predicate: Most recent surviving self-modification program's start versus predecessor start, or birth if none.
- Invalidation or expiry: New reward, elapsed time and restoration costs can change a previously positive result.
- Activation or effect: Non-exceedance drives restoration by design; reported experiments attribute substantial countermanding, without inspectable check traces.
- Evidence limits: Documentary contract, not executable proof; historical rate ordering does not identify a modification's true cause or future effect.

Candidate computation belongs to sampled programs; the fixed top-level computes this check and can veto continued retention. Human contribution sets task reward, primitives and initial parameters, not per-change approval. Operating mode is lifelong interaction illustrated by bounded toy lives; trigger is a completed instruction while checking enabled. The oracle is task-owned measured payoff (exact address/value matches or goal arrival in the documented environments), not an expected correct learning program. What persists is live policy and surviving snapshots, not the transient check or an explanatory claim. Modifiers use current state/bias; no truth-apt proposal or mandatory rationale is specified. Rollback restores direct probabilities only.

### Claims

#### EPI-CLM-future-usefulness
Label: Past apparent usefulness guides future reliance

Claimed operation: the source describes continued reliance on changes that appeared useful so far and discusses distributions reflecting knowledge useful for multiple tasks. SRC-1 §4 comments 6, 14, doctrine/design. This is distinct from [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant), which concerns historical ordering, and [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison), which concerns reported outcomes. No machine-retained formulated prediction is identified. The source itself limits forward inference and causal attribution.

> What appeared to be \useful" up until now is assumed to remain \useful" in the
> future, though it may have been just a uke that might later turn out actually to have harmful
> consequences
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> until the current probability distributions re ect
> knowledge useful for solving both tasks.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`
