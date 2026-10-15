---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Incremental self-improvement's in-life work storage, policy retention, restoration history and documented later consumers."
run-id: AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01
source-identity: "https://people.idsia.ch/~juergen/fki198-94.pdf"
reviewed-boundary: fki198-94-revised-1995-01-31-captured-2026-10-14-text
---

# Incremental self-improvement memory report

## Boundary and evidence

The memory boundary is the documented probabilistic interpreter's single system life: work cells, sampled program cells, live distributions, probability-change stack, and task-mediated external state. The frozen capture and evidence layers are declared in [boundary.md](boundary.md). SRC-1 supplies doctrine/design in §3.2, Table 1 and §4, and reported operation in §5. Direct inspection here covered captured text lines 186–890, including the primitive table, retention algorithm, all twenty comments, both experiments and §5.3. Runtime findings were supplied separately; this report rechecked their consequential memory mechanisms in the capture rather than treating them as implementation evidence.

No executable dispatch, CLI, hooks, registered tool implementation or library/service operations are supplied. The documentary alternatives below are therefore not a complete inventory of shipped paths. No cross-process serialization, deployment wiring or raw execution trace can be established. The source permits an account of documented consumers, not independent observation of their activation.

All source anchors below refer to SRC-1, `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`.

| Memory operation or part | Source scope and inspection basis | Records / limit |
|---|---|---|
| Birth initialization; persistent work writes and reads across runs | Direct: §3.2, Table 1; supplied runtime | [RT-OBJ-work-area](runtime.md#rt-obj-work-area), [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle); cell meanings and actual event representations uninspected |
| Program-cell sampling and overwriting | Direct: §3.2; supplied runtime | [RT-OBJ-program-area](runtime.md#rt-obj-program-area), [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection); sampled code is not an executable archive of successful programs |
| IncP/DecP admission and live policy updates | Direct: Table 1, §3.2; supplied runtime | [RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-CMP-probability-distributions](runtime.md#rt-cmp-probability-distributions) |
| GetP introspective read into work storage | Direct: §3.2, Table 1 | [MEM-RTE-getp-read](#mem-rte-getp-read); exercise and later use of particular outputs uninspected |
| Stack saving, grouping, evaluation and reverse restoration | Direct: §3.2, §4 comments 5–7, 17–19; supplied runtime | [RT-OBJ-stack](runtime.md#rt-obj-stack), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment); no rationale archive or raw action trace established |
| Environment as retained state; variable Write/Read and resets | Direct: §3.2, §4 comment 8, §5.1, Table 2 | [MEM-OBJ-variable-array](#mem-obj-variable-array), [MEM-RTE-variable-readback](#mem-rte-variable-readback); exact Read destination is inconsistent in the source |
| Navigation input replacement, position and goal reset | Direct: §5.2 | [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment), [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle); current observations are not themselves a demonstrated memory encoding of past position |
| Reuse of prior sampled instructions | Direct: §4 comment 11 | [RT-OBJ-program-area](runtime.md#rt-obj-program-area); proposed alternative within-run reuse, not the experimental base route |
| Teacher inputs/reward; direct teacher forcing | Direct: §4 comments 15–16 | [RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant); external teaching is discussed, direct protection is proposed, activation unestablished |
| Circular history overwrite; stack introspection | Direct: §4 comment 19, §5.3 | [RT-OBJ-stack](runtime.md#rt-obj-stack); overwrite proposed, stack-reading primitives explicitly not yet implemented; cannot infer agent access to evaluation history |

## Core ideas

1. **Persistence does not mean replay.** Work cells survive run halts and can hold event representations. Program cells also hold sampled integers, but the base interpreter samples again at each visit. The enduring behavioral bias is the distribution table, not a stored script selected because it previously succeeded ([RT-OBJ-work-area](runtime.md#rt-obj-work-area), [RT-OBJ-program-area](runtime.md#rt-obj-program-area), [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection)).
2. **The restoration record and the live policy have different consumers.** The sampler consumes live probabilities. The fixed evaluator consumes historical times/payoff and old distributions. GetP exposes current probabilities to program computation, not the stack's saved history ([RT-OBJ-stack](runtime.md#rt-obj-stack), [MEM-RTE-getp-read](#mem-rte-getp-read)).
3. **Experience filters changes without retaining explanations.** The source's single-experience inference uses reward/time measurements to keep or restore policy changes. It need not transform a raw event log into a summary or retain a criticism of a claim. Stack metadata supports reassessment and recovery; it is not evidence of a causal explanation for success ([RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment), [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant)).
4. **Admission and withdrawal have narrow reach.** Software checks modifier operands and MinP, then changes policy immediately. Evaluation is postponed until EndSelfMod. Rejection restores probabilities, not work cells or environmental consequences. Human choices shape primitives and reward, but do not approve each ordinary update ([RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)).

There is no documented model-visible text window to budget or compact. The finite cell array, integer ranges, finite stack and lifetime computation are the relevant budgets. IP and indirect addresses select operands; Pi selects instruction/argument values. No source-trust ranking is specified: task inputs have the force of integer data under primitive semantics, and task payoff has the force of the fixed evaluator's reference outcome. The corrupted-input experiment specifically prevents assuming that observations are reliable (§5.2.2). These are classical addressable machine-state paths, not text retrieval or host-window isolation.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-variable-array
Label: External variable array

Source-native identity: V0 through V29, with integer contents Ci. Representational form: symbolic integer values. Storage substrate: the documented task environment's array; actual implementation and disk persistence are uninspected. Lineage: zero initialization at birth and after each payoff event; intervening values come from agent Write actions. The task evaluator counts exact address/value matches; Read affords retrieval into work storage. The values are task output and potentially an external memory medium, not a natural-language knowledge base. They remain until overwritten or the next 1,000-step reset (SRC-1, §5.1, Table 2).

Distinct identity: not the internal [RT-OBJ-work-area](runtime.md#rt-obj-work-area); Write/Read cross the boundary between them. The closest supplied route, [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle), includes the action capability but does not declare this external array. No supplied object counterpart after comparison.

> The external environment consists of an array of 30 variables V0 ; V1; : : :; V29.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> Then, all variables are re-initialized with zeros.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Routes

#### MEM-RTE-getp-read
Label: GetP policy read

Part of: [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)

Endpoints and progression: sampled GetP and indirect operands → current addressed probability → scaled integer in an addressed work cell → available for later instruction reads. Owner: fixed GetP semantics, selected by the interpreter. This is the introspective subroute of the supplied instruction cycle, not a duplicate of the modifier route. Context is current registers, addresses and Pi; its action effect is a work-cell write. It exposes a rounded/scaled value, not the complete distribution table, a stored explanation or stack history (SRC-1, Table 1, §3.2).

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: Write a scaled current probability into a permitted work-area destination, conditional on valid addressing/syntax.
- Later read-back: The work-cell result persists across run halts until overwritten and is available to later instructions. Consumption of a particular GetP result in a later run is uninspected.
- Delegated visibility: inapplicable — no delegated worker is described.
- Selection predicate: GetP operands address a current policy cell/value and work destination through the documented addressing scheme; no relevance search or context ranking occurs.
- Invalidation or expiry: The snapshot can become stale after a policy update; the work cell changes only on another write, with no automatic synchronization specified.
- Activation or effect: The design affords subsequent arithmetic/branch/modifier use of the result; no supplied trace demonstrates that this pathway caused reported improvement.
- Evidence limits: Captured design establishes the operation; source calls introspection potentially useful, not demonstrated or essential to the experimental gains.

> The primitive GetP can be used to write scaled versions of current probability values into work cells.
> GetP is potentially useful for purposes of introspection.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### MEM-RTE-variable-readback
Label: Variable write readback

Part of: [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)

Endpoints and progression: sampled Write plus work/address operands → external Ci → later sampled Read → work-cell value available to computation. Owner: interpreter selects actions; fixed task primitives enforce valid ranges. This subroute differs from [MEM-RTE-getp-read](#mem-rte-getp-read) by its retained input and task-owned reset. It connects [MEM-OBJ-variable-array](#mem-obj-variable-array) and [RT-OBJ-work-area](runtime.md#rt-obj-work-area). Source: SRC-1, §5.1 and Table 2.

Write admission is software range/syntax checking, not per-value human approval. The agent computes values through sampled instructions; the programmer supplies the task and the driver controls resets. This is ordinary output/storage admission, not successor-policy selection. Operating mode: the bounded variable experiment. No correctness oracle approves each write: the periodic match-count payoff supplies a later outcome signal to the policy evaluator. Rollback of a probability update does not undo these external writes.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: Write copies an addressed work value into an addressed external variable; Read copies an external value back to work storage. Invalid ranges halt the run.
- Later read-back: Later Read calls can receive agent-written values before the periodic reset, including across run halts; the report does not trace an exercised Write-to-later-Read memory chain.
- Delegated visibility: inapplicable — the same agent interpreter uses both primitives.
- Selection predicate: Double-indexed operands select a variable, not a relevance score; the exact Read destination operand cannot be settled because Table 2 and prose disagree.
- Invalidation or expiry: A subsequent Write can replace a value; every 1,000 time steps the task zeros the external array after scoring. Internal work-cell copies are not automatically zeroed by this reset.
- Activation or effect: Fixed Read semantics can return previously written values for subsequent computation. The task evaluator also uses current variable values to calculate payoff; a beneficial memory use is not independently established.
- Evidence limits: Documentary storage/read capability with a specified consumer role; no raw trace of later reads, and the Read operand inconsistency prevents an exact destination formula.

> Write and read operations outside the valid ranges halt the current run.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> Read(a1; a2) writes the contents of the variable indirectly addressed
> by the second argument into the work cell indirectly addressed by the second argument. See Table 2.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-work-area](runtime.md#rt-obj-work-area)

The representational form and substrate are symbolic integers in an addressable in-life array. Its lineage is birth initialization followed by instruction and environmental writes. Distinguish input cells (task/state observations), registers (indirect addressing) and arbitrary work cells (program-computed values); they share the array but not guaranteed meanings or trust. A value survives a run halt, but a task observation may be replaced whenever the environment writes again. Work-cell persistence is architectural; event-memory encoding and its beneficial later use are only afforded, not observed in this capture. Later instructions receive only the addresses they actually read, not an automatic summary of the whole array (SRC-1, §3.2, §4 comment 8, §5.1–5.2).

> Likewise, the program area may use the work area
> to store representations of previous events.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### On [RT-OBJ-program-area](runtime.md#rt-obj-program-area)

Sampled integer instructions are transiently realized code, not the retained learning product. The base selector consumes Pi each visit, so a previous sampled value does not have automatic replay authority. Comment 11's alternate reuse proposal instead would select an earlier sampled instruction on a repeated address within the current run; it also needs runtime bounds because programs can fail to halt. It is not a checkpoint or cross-run replay mechanism established for the experiments (SRC-1, §3.2, §4 comment 11).

> Otherwise use the instruction executed
> during the most recent visit of the program cell.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### On [RT-CMP-probability-distributions](runtime.md#rt-cmp-probability-distributions)

The lasting product is a localized numerical policy table. Its lineage is maximum-entropy initialization, multiplicative/normalized updates from sampled modifiers, and possible restoration from oldP. The sampler gives retained parameters direct probabilistic authority over future code selection; GetP gives selected current entries data authority in work-cell computations. These are distinct consumers. No text summary or opaque embedding mediates either path. Positive MinP keeps alternatives possible; a retained update does not mandate a single action or guarantee success (SRC-1, §3.2; [RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection), [MEM-RTE-getp-read](#mem-rte-getp-read)).

#### On [RT-OBJ-stack](runtime.md#rt-obj-stack)

Separate oldP's distribution payload from its access/evaluation metadata: address targets restoration; first groups entries by a self-modification program; t and R supply historical comparison baselines. The fixed evaluator reads these structured values. They are neither a raw instruction/observation log nor a stored runnable self-modification program. They retain a recoverable previous policy and enough timing/payoff evidence for reassessment, not why the update was proposed or a causal explanation for payoff. The schema's complete field list in §3.2 supports this scoped distinction; it does not exclude representations elsewhere in arbitrary work cells.

Finite StackSize limits recoverable history. Proposed circular overwrite removes the oldest recovery records, not necessarily the corresponding live policy effects. The source explicitly distinguishes intended agent-facing stack introspection from existing GetP access (SRC-1, §4 comment 19):

> It is intended to introduce additional introspective primitives for addressing and examining stack
> entries (in the style of GetP ). This is not yet implemented, however.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

The experimental input of sp exposes stack size/top position, not this full history. The author's reported inspection of stack entries is an external analytical read, not evidence that the agent examined them (§5.1–5.2).

#### On [RT-RTE-self-modification](runtime.md#rt-rte-self-modification)

Write agency is sampled program computation; software supplies operand/MinP checks and physical saving/updating. The retained product is changed Pi plus oldP and metadata, without a required retained reason. Subsequent samples consume live Pi even before evaluation. The modifier itself need not be reward-derived: operands may come from work/input state, including GetP, but the particular lineage of proposals in the experiments is uninspected. Teacher-provided observations or reward shaping are environmental guidance; comment 16's direct protection would instead make a human decision affect retention of selected changes. That alternate override is proposed, not a base admission step (SRC-1, §3.2, §4 comments 15–16).

#### On [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)

The trace-fed transformation uses numerical time/payoff history and live outcomes, not a retained raw transcript. Its chain is historical t/R at modification → compare current reward/time → retain live Pi or restore oldP → later interpreter samples. Surviving stack entries feed further evaluations. This is experience-responsive policy retention; it does not establish independent causal learning or content-directed criticism. The published disabled/enabled comparisons are attributed benefit evidence, not update-specific attribution ([RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison)).

Withdrawal removes restoration entries and reverses direct policy effects, while work storage, action consequences and later copies can survive. There is no all-state checkpoint alternative in the documented evaluator. Circular-stack history loss would further limit rollback; self-generated corrective modifiers are not deterministic restoration of erased history (SRC-1, §3.2, §4 comments 5, 19).

## Write side

At birth, fixed initialization supplies zero storage and uniform Pi; the programmer chooses primitive semantics, reward and sizes. Later work-cell authoring is agent computation or task input writing, admitted by software syntax/address constraints. No per-content human gate is specified. GetP is an automatic derived snapshot into work storage, but its source is current policy, not an experience log. Sampled program-cell writes are interpreter realization of code, not deliberate library adoption.

For policy changes, [RT-RTE-self-modification](runtime.md#rt-rte-self-modification) separates proposal, physical save and live update from subsequent retention. Invalid factors or below-MinP outcomes veto a change before it takes effect. The fixed evaluator subsequently decides keep/restore using historical payoff, with EndSelfMod controlling when checking resumes. The resulting behavior-shaping material is Pi, while S preserves old versions and measurement baselines. Neither the table nor S requires an explanation; the later sampler receives only parameters, and the evaluator receives numerical evidence rather than reasons.

Maintenance is ongoing reevaluation, not periodic compaction. [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment) can withdraw a formerly accepted change as later rates deteriorate. Restoration cost itself can invalidate older entries. StackSize is a resource ceiling, not a context-window token budget; circular eviction is a proposal with recovery loss. Work cells are not cleaned by this policy rejection. The experimental external array has its own periodic reset, and the maze its own goal-to-start transfer; neither erases internal work storage. These cases falsify a broader claim that all state is permanently retained or all state is rolled back.

No trace-summary checkpoint, model-based curation, text editing or explanation-adoption surface is established within this capture. Universality allows programs to encode arbitrary computations and event representations; it does not show what representations were actually authored. The author reports messy nonzero work cells, not a decoded event archive (§5.1.2).

## Read-back

- **Later interpreter invocations:** a new run resets IP to ProgramStart but leaves work storage and policy available. Pi supplies probabilities by program address; explicit primitives read selected integer cells. Persistent state is not wholesale pushed into a language-model window ([RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle)).
- **Later policy selection:** retained/restored Pi reaches the sampler at each visit. Fixed sampling semantics supply probabilistic behavioral authority, while syntax and task constraints still bound execution ([RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection)).
- **Later evaluation:** after an instruction outside an incomplete modifier, the fixed top-level automatically selects the newest surviving program and its predecessor/birth baselines. It receives t/R/first and oldP/address when restoration is needed, not all previous actions. Its budget includes the cost of handling whole distribution vectors ([RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)).
- **Program introspection:** sampled GetP requests one addressed current policy value and delivers a scaled snapshot to work storage. It does not independently push past history. Persistence of the result is distinct from evidence that a later instruction used it ([MEM-RTE-getp-read](#mem-rte-getp-read)).
- **External read-back:** sampled Read affords retrieval of an earlier Write value before the task reset. Driver payoff computation independently reads array contents for scoring. Only the latter is part of the author's reported task outcomes; an exercised memory chain through Read remains uninspected ([MEM-RTE-variable-readback](#mem-rte-variable-readback)).

Observation replacement is task-driven working-state control, not eviction from a model window. The maze's immediate inputs do not uniquely identify location; persistent work cells could support history-sensitive computation, but the report does not decode that mechanism. There are no described sub-agent frames, return summaries, or host compaction/reload paths in the inspected design. This is a boundary limit rather than an implementation-wide absence claim.

## Integration issues

- **No corrections to supplied facts.** Direct inspection supports the supplied distinction between live policy, sampled code, persistent work cells and restoration-only rollback. No replacement records are proposed.
- **Part decomposition, not duplicates:** [MEM-RTE-getp-read](#mem-rte-getp-read) and [MEM-RTE-variable-readback](#mem-rte-variable-readback) are explicitly subroutes of [RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle). [MEM-OBJ-variable-array](#mem-obj-variable-array) is distinct external task state, not a duplicate of [RT-OBJ-work-area](runtime.md#rt-obj-work-area).
- **Read operand ambiguity:** Table 2 and §5.1 prose give inconsistent Read destinations. This already limits the supplied runtime; [MEM-RTE-variable-readback](#mem-rte-variable-readback) retains it. The existence of task-to-work transfer is supported; exact operand fidelity is not.
- **History access:** [RT-OBJ-stack](runtime.md#rt-obj-stack) is evaluator-readable, while agent-facing stack introspection is explicitly not yet implemented (§4 comment 19). GetP and sp input do not close this gap. This prevents attributing retention decisions to an agent's interpretation of saved evaluation history.
- **Alternative coverage:** instruction reuse, direct teacher protection and circular overwrite remain proposals, not established activated routes. [RT-OBJ-program-area](runtime.md#rt-obj-program-area), [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant) and [RT-OBJ-stack](runtime.md#rt-obj-stack) preserve their consequences without attributing implementation.
- **Exercise and rationale limits:** actual event encodings, GetP-to-update use, external Write-to-Read use and arbitrary work-cell rationales are uninspected. No raw traces resolve them. This prevents an exercised memory-benefit claim, not the documented retention/consumer account. Learning and self-improvement attribution remain bounded as in [RT-RTE-self-modification](runtime.md#rt-rte-self-modification) and [RT-CLM-experimental-comparison](runtime.md#rt-clm-experimental-comparison).

## Limitations and checks

The evidence remains doc-grounded. Runtime source code, raw stack traces and independent interventions are unavailable within the frozen capture. Extraction damage and the Read inconsistency prevent exact reconstruction of some formulas. The inspected table/schema can distinguish the documented payloads; it cannot establish absent arbitrary representations in the work area or complete shipped implementation coverage. Reported successful lifetimes do not prove that any particular stored representation caused improvement.

Source identity recheck: the registered text SHA-256 was recomputed and equals `c6fb513ff17ded4cd5cc3efaa3c3267ce6683d69895219674571a3be26987b5b`. Capture label, source identity and run ID equal the supplied boundary/invocation. Method checkout HEAD was inspected as `d72d0ff43659e0cad5527969e41f79ffa7ab04e5`; the supplied job, member types, worker rules and record contract govern this output.

Validation: passed with the invocation-specific validate-output command; this establishes deterministic form and quotation occurrence, not semantic acceptance or observed operation.
