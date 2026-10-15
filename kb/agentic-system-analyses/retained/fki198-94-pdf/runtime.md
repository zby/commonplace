---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Incremental self-improvement's documented probabilistic interpreter, self-modification and reward-rate retention loop in the revised FKI-198-94 capture."
run-id: AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01
reviewed-boundary: fki198-94-revised-1995-01-31-captured-2026-10-14-text
---

# Incremental self-improvement runtime report

## Runtime account

### Boundary and consequential work

The report describes a lifelong reinforcement-learning runtime that samples integer instructions and arguments, executes task actions, and alters the distributions governing later instruction selection. Its objective is cumulative environmental payoff at death. Its fixed evaluator retains probability changes only while their measured reward rate satisfies a recursive comparison. This is a documented design and attributed implementation, not inspected executable code. No shipped command, callable entry point, packaging, execution trace or deployment envelope can be established from this capture. The evidence boundary is [boundary.md](boundary.md); all source findings below use SRC-1, the registered captured text, §§2–5.

The source-native distinction is between normal instructions, probability-modifying instructions, and an unmodifiable top-level evaluator. There are no explicit learning/meta-learning tiers in the interpreter. The main decision policy is an address-indexed table of probabilities, not a language model. Its numerical entries have localized identities and fixed sampling/update rules; this account classifies the table as symbolic numerical state rather than distributed-parametric content. The runtime has no inspected distributed-parametric component. Neural-network primitives and alternative hardware are proposals, not components of the described experiment (SRC-1, §§3.1–3.2, §5.3).

The main loops are [RT-RTE-instruction-cycle](#rt-rte-instruction-cycle), [RT-RTE-self-modification](#rt-rte-self-modification), and [RT-RTE-credit-assignment](#rt-rte-credit-assignment). Their force on later behavior is recorded in [RT-BAP-probability-selection](#rt-bap-probability-selection).

### Ordinary documented invocation

At birth the runtime initializes integer storage to zero and every program-cell distribution to maximum entropy. A run starts with IP at ProgramStart. The interpreter samples a primitive and up to three arguments from the corresponding consecutive program-cell distributions, writes the sampled integers there, and checks syntax. Valid instructions execute through fixed primitive semantics. An explicit jump changes IP; otherwise IP advances past the arguments. Stop or a syntax failure ends the run. The enclosing lifetime loop starts another run without resetting storage or the environment, until death at T. There is no per-request answer: the ordinary return is a halt to the lifetime loop; terminal outcomes are cumulative payoff and final state (SRC-1, §3.2; [RT-RTE-instruction-cycle](#rt-rte-instruction-cycle)).

The experimental variable-writing driver supplies a concrete end-to-end environment. Its 30 variables begin at zero. Write and Read connect indirect work-cell addresses to that array; out-of-range accesses halt the current run. Every 1,000 measured steps the driver counts variables whose values equal their addresses, delivers that count as payoff/input, and resets the external variables. Thus an experimental task reset coexists with persistent internal storage; “life is one-way” is not a claim that the documented driver never resets any environmental part. IP, stack pointer and a time-derived value also reach input cells. The top-level reward computation, not the agent, owns the expected relation between variable address and value. Table 2 and the surrounding Read description are inconsistent about the destination argument; extraction also damages equations. This report therefore establishes the work-area/environment read route but does not assert the exact Read operand formula (SRC-1, §5.1, Table 2).

Time here is a computational-cost proxy: each operation considering all nops probabilities of a cell costs one step, including sampling and pushing/popping distributions. Other operations are charged zero. This supports the stated order-of-CPU-time accounting, not a guarantee that every instruction has measured wall-clock cost (SRC-1, §5.1).

### Change admission and evaluation

The first effective IncP or DecP after birth or EndSelfMod begins a self-modification program. Each change saves the old distribution and bookkeeping on S, then changes the live policy. EndSelfMod closes the program and resumes top-level checking. Admission therefore is not a pre-install approval gate: changes affect sampling while evaluation is suspended. The computation proposes its own changes through sampled instructions, while fixed primitive constraints veto invalid factors or changes below MinP. The top-level later decides retention from cumulative payoff and elapsed time. No human approves each change in the base design; the programmer chooses the primitive set, reward function and initial parameters (SRC-1, §§3.2, 4 comments 1, 10, 13; §5.3).

Once no self-modification program is running, each completed instruction cycle triggers the evaluator. It compares the reward rate since the newest retained program's beginning to that since the preceding retained program, or birth when there is no predecessor. If the newer rate does not exceed the earlier one, the evaluator pops and restores saved distributions. Restoration itself takes time, so the loop can also invalidate older changes. Work cells and environmental effects are not restored. Subsequent policy sampling is the downstream consumer; the stack records previous distributions, not a retained executable copy of each successful program (SRC-1, §§3.2, 4 comments 5, 17).

### Guarantees and forcing cases

The load-bearing guarantee is the source's recursive “usefulness” invariant, [RT-CLM-usefulness-invariant](#rt-clm-usefulness-invariant). Its owner and enforcement point are the fixed top-level strategy after completed instructions outside an unfinished self-modification program. Guarantee strength: invariant, as a documented algorithmic assertion. Design conclusion status: claimed. Implementation conclusion status: uninspected. Operation conclusion status: uninspected. It compares historical rates; it does not prove causation or future improvement. It requires correctly delivered payoff, correct time/stack accounting, and availability of saved distributions. The capture's experiments are reported operation, not independently observed enforcement.

Four documentary forcing cases qualify this guarantee and its apparent rollback surface:

1. **An unfinished self-modification program.** EndSelfMod lets the system delay evaluation arbitrarily while live probability changes are in force. Positive MinP supports the source's finite expected delay, not a hard deadline. A run halt and a self-modification ending are different events in the description; only EndSelfMod is specified to close the latter. Exact implementation handling of a run halt during an unfinished self-modification program is uninspected (SRC-1, §§3.2, 4 comment 1).
2. **Indirect effects survive rejection.** IncP/DecP changes may already have changed actions, work cells and the external world. Popping restores probabilities only. A harmful effect or coincidental payoff can therefore survive a rejected update, and historical reward acceleration does not identify its true cause (SRC-1, §4 comments 5–7).
3. **Finite restoration history.** The proposed circular stack overwrites oldest history and permits direct restoration only of recent entries. Further self-modification could restore a distribution indirectly, but that is not deterministic rollback. The reported experiments say overflow did not threaten; the circular-stack extension is not established as their active implementation (SRC-1, §4 comment 19).
4. **Alternate programmer/teacher paths.** Direct teacher forcing is proposed to prevent the top-level from countermanding selected changes. That path would deliberately weaken the base invariant's enforcement. Reusing a program cell's earlier sampled instruction is another proposed variant; it can create non-halting programs and needs runtime bounds. Neither belongs to the ordinary per-visit resampling route or is established as active in these experiments (SRC-1, §4 comments 11, 16).

The material documented normal action paths include arithmetic, branching, work-cell writes, observation reads and task-specific output. They share the interpreter's syntax boundary, but only probability writes enter its restoration stack. Normal writes cannot write program-area cells; the interpreter itself writes sampled code there. GetP reads policy values into work storage. An arbitrary Output primitive needs its own task contract: the demonstrated maze primitives enforce grid/obstacle restrictions, while the variable driver enforces address ranges. General primitive universality does not grant unrestricted OS access or establish an isolation envelope. Shell execution, provider-native tools, host callbacks, extension loaders, subprocess/remote workers and durable process restart are not inspectable routes in this capture; their exclusion prevents implementation-wide coverage, not an asserted absence (SRC-1, Table 1, §§3.2, 5.1–5.2).

Coordination is the documented serial interpreter and stack management, not delegated workers. Inputs are task-owned writes to designated cells. No separate context window is described: selected code can read existing addressable cells, and state accumulates across run halts. This is ordinary machine-state persistence, not evidence of model-window compaction or isolation. Memory-specific revisions and additional record decomposition are left to the memory analyst.

### Outcome evidence and interpretation

[RT-CLM-experimental-comparison](#rt-clm-experimental-comparison) records the author's enabled/disabled self-modification comparisons. These support attributed improvement over the described lifetimes. They do not independently authenticate execution, isolate the effect of a particular update, or demonstrate a generally superior learning algorithm. The source itself warns that usefulness is not true causality and that the experiments illustrate operation rather than evaluate initial bias statistically (SRC-1, §4 comment 6, §5 introduction).

## Shared records

### Components

#### RT-CMP-probability-distributions
Label: Program-cell probability distributions

Source-native identity: Pi and Pij, distributions over primitive/argument integer values at each program address. Representational form: symbolic numerical table, with individually addressed entries and fixed rules for sampling, normalization and minimum probability. Storage substrate: runtime numerical arrays associated with program cells; no disk serialization is described. The exact numeric precision and C layout are uninspected. Parameters change during documented operation through IncP/DecP and restoration. The capture pins the design, not an executable model version; no mutable provider endpoint is part of this documented component (SRC-1, §3.2).

> For each cell ai in the program area, there is a discrete
> probability distribution Pi over the set of possible cell contents.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### RT-CMP-top-level
Label: Unmodifiable top-level credit assignment strategy

Source-native identity: the fixed strategy that compares reward rates and pops S. Representational form: symbolic algorithm with fixed control flow, outside the sampled instruction language. Storage substrate: implementation machinery described in the report, with executable code unavailable. It consumes S, R(t), time and whether a self-modification program is incomplete; only distributions are restored. No admitted self-revision of this component is described in the base algorithm (SRC-1, §3.2).

> (1) If there currently is an incomplete self-modi cation program (not yet ended
> by an EndSelfMod action), do nothing.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Operative objects

#### RT-OBJ-work-area
Label: Work area

Source-native identity: integer cells ai with Min ≤ i < ProgramStart, including registers and input cells. Representational form: symbolic integer state, whose current meanings depend on executing instructions; universality affords event representations without establishing what particular cells represent. Storage substrate: addressable array, initially zero, preserved across runs in one life. Environment writes selected inputs; normal primitives write permitted work addresses. Restart durability is uninspected (SRC-1, §3.2).

> Instructions executed in the
> program area may read from and write to the work area. Both register area and input area are subsets
> of the work area.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### RT-OBJ-program-area
Label: Sampled program area

Source-native identity: program cells at ProgramStart through the upper program range, addressed by IP. Representational form: symbolic integer code and arguments. Storage substrate: the same addressable cell array; interpreter sampling overwrites cells with chosen values. Existing contents are not the main base-design selection policy: each visit samples from Pi. The proposal to reuse prior contents within a run is a separate variant. Normal instruction writes are restricted to work cells (SRC-1, §3.2, Table 1, §4 comment 11).

> They are sequentially written onto the program area, starting from
> ai . Syntax checks are performed.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### RT-OBJ-stack
Label: Probability-change stack S

Source-native identity: S(k), with time, cumulative payoff, modified address, first-entry pointer and oldP; sp identifies its top. Representational form: symbolic structured records plus localized numeric distribution vectors. Storage substrate: finite runtime stack; experimental StackSize is 10,000. It saves old distributions per change, supports grouped self-modification comparison and reverse restoration, and persists during the life unless entries are popped. Circular overwrite is proposed; actual restart persistence is uninspected (SRC-1, §3.2, §4 comment 19, §5.1).

> S(k)
> consists of the following variables: S(k):t, S(k):R, S(k):address, S(k):first, and S(k):oldP (a vector
> of nops variables).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Routes

#### RT-RTE-instruction-cycle
Label: Sample and execute an instruction

Endpoints and progression: current IP and Pi → sampled primitive/arguments → syntax check → primitive executor → changed IP, work state or environment → top-level check when enabled → next instruction or run halt. The interpreter owns next-step selection; fixed primitive semantics own execution. Its context consists of current cells, IP, task inputs and policy, not natural-language interpretation. Trigger/principal: the enclosing system-life loop, begun at birth. No delegated principal participates (SRC-1, §3.2, Table 1).

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: A primitive completes with state/action effects, or Stop/syntax failure halts the run; the lifetime driver restarts IP at ProgramStart.
- Later read-back: Work-cell writes can reach later instructions and later runs in the same life; later visits consume changed Pi, not merely the last sampled program-cell contents.
- Delegated visibility: inapplicable — no worker delegation is described in this interpreter route.
- Selection predicate: IP selects the program address; Pi samples integer instruction/argument values, and indirect addressing selects work/environment operands.
- Invalidation or expiry: Sampled program contents can be overwritten on a later visit; work cells persist until a later write, and birth initialization is not repeated per run.
- Activation or effect: Fixed primitive semantics turn valid sampled integers into control, storage or environmental effects; supplied traces demonstrating particular sampled sequences are unavailable.
- Evidence limits: SRC-1 supplies algorithm design and attributed experiments, not executable instruction dispatch or raw traces; exact damaged Table 1 arithmetic is not reconstructed here.

> If
> syntactically correct, the instruction gets executed. Otherwise, the current \run" (see next paragraph)
> is halted.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### RT-RTE-self-modification
Label: Compute and delimit probability changes

Endpoints and progression: sampled IncP/DecP → addressed Pi and modification factor → validity/MinP check → save old Pi on S → change live Pi → further sampled instructions → EndSelfMod. The first effective probability change after birth or EndSelfMod starts the program. The runtime computes proposals; fixed primitive rules veto illegal changes; the later top-level can reject retained effects. There is no per-change human approval in the base loop. GetP makes scaled current probabilities available to work-cell computations (SRC-1, §3.2).

Operating mode: open lifelong interaction, illustrated by bounded-duration toy experiments. Improvement trigger: effective probability-changing instructions, not a user improvement request. Answer oracle: none at the primitive admission step; task payoff supplies the later evaluator's outcome signal. Guidance: programmer-chosen primitive semantics and reward objective, current probability bias, work/input state and any GetP reads. What persists is policy parameters and their restoration history, not a required explanation of the proposal. Rollback is later probability restoration only; environmental and work-cell effects remain.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: A valid modifier changes a distribution immediately and saves its previous value; EndSelfMod marks completion and enables top-level evaluation.
- Later read-back: Later primitive and argument samples consume changed distributions, including probabilities of further self-modification instructions.
- Delegated visibility: inapplicable — the same interpreter computes and consumes the changes without delegated workers.
- Selection predicate: Modifier operands indirectly identify a program cell, a value and a factor; factors must be 1–99 and no resulting probability may fall below MinP.
- Invalidation or expiry: The top-level can restore previous distributions after completion; no fixed expiry exists, and evaluation is suspended while the program is incomplete.
- Activation or effect: Live policy changes alter selection probabilities by design, including selection of future modifier programs; reported stack findings attribute such activity to the experiments, without inspectable sample traces.
- Evidence limits: Source descriptions establish the intended causal path, and §5 attributes exercised changes; no code or update-specific intervention closes independent causal attribution.

> DecP and IncP have no e ect
> if the indirectly addressed cell contents cc 3 (see Table 1) are not an integer between 1 and 99, or if the
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> The self-modi cation program ends itself by executing the EndSelfMod action.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

Learning: the pathway targets improved future action through changed policy; §5 reports enabled/disabled benefit within one system life. General improvement and any particular update's benefit remain unestablished. Reflection: GetP supplies a documented self-representation of current policy, while changes to Pi change that representation and instruction computations can use it to change later Pi. This is a design affordance for bidirectional policy introspection, not evidence that reported gains depend on exercised GetP use. Autonomous proposal/admission: computation performs these roles in the base algorithm; task/reward design is human-supplied and reliability is not implied.

Self-improvement assessment: boundary is the probabilistic instruction runtime; horizon is one life; objective is externally specified cumulative payoff, with historical payoff/time as the admission criterion. Link 1 is documented at the retention stage: measured payoff shapes the keep/restore decision, though a proposed modifier need not itself use reward. Link 2 changes the runtime's own instruction policy. Link 3 reaches live sampling through [RT-BAP-probability-selection](#rt-bap-probability-selection). Link 4 is attributed in §5, not independently observed or causally isolated. This supports documented improvement-directed self-change and reported exercise, not an independently verified successful self-improvement claim. A formulated-theory route is not established: sampled programs and numerical policy shifts alone do not demonstrate content-directed criticism, a reflective theory builder or an autonomous theory builder.

#### RT-RTE-credit-assignment
Label: Retain or restore completed probability changes

Endpoints and progression: completed instruction with no unfinished self-modification → current R(t), t and newest stack program start → comparison with preceding program/birth → keep or successively pop oldP → resumed interpreter. Owner: [RT-CMP-top-level](#rt-cmp-top-level). It computes selection and veto; the self-modification program supplies candidates, not the decision rule. The software admits continuation of live changes; no human per-content approval is required. Guarantee and limits are [RT-CLM-usefulness-invariant](#rt-clm-usefulness-invariant) (SRC-1, §3.2).

Operating mode: ongoing single-life sequential experience, with bounded lifetimes in §5. Improvement trigger: each completed cycle while evaluation is enabled. Answer oracle: measured environmental payoff, not a model's judgment. The variable task's driver counts exact address/value matches; the maze driver pays 100 on reaching the goal and transfers the agent to the start. These expected outcomes are supplied by programmer-defined task code as documented in §§5.1–5.2. The evaluator compares historical rates, not an expected correct program or a causal reference intervention. Guidance is the fixed recursive usefulness rule. What persists is the accepted live distributions plus stack history; what is rejected is only direct probability change.

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed
- Immediate return: Retain qualifying distributions, or pop and restore until the remaining newest program's measured rate exceeds its predecessor's, or the stack becomes empty.
- Later read-back: Later interpreter selections use retained/restored Pi; future evaluations reuse surviving stack start times, payoff totals and oldP records.
- Delegated visibility: inapplicable — the evaluator is internal fixed machinery, not a delegated judge.
- Selection predicate: Evaluate the newest surviving self-modification program against its predecessor or birth; non-exceeding reward/time causes reverse-order restoration.
- Invalidation or expiry: Utility is reevaluated after later instructions and can decline; restoration cost can invalidate earlier programs too. A program may remain accepted for the remaining life.
- Activation or effect: Restoration replaces live policy distributions and therefore changes later sampling probabilities; it cannot erase prior work/environment effects or prove which update caused reward.
- Evidence limits: The formal guarantee is source doctrine; experimental restoration counts are reported operation. No raw stack trace, executable evaluator or overflow case establishes deployed enforcement.

> The reason
> is that popping and restoring probability distributions takes time (t increases during execution of the
> while loop), possibly causing utility values to drop.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> Note that only direct e ects of self-modi cation programs on primitive proba-
> bility distributions can be countermanded by the top-level strategy.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Claims

#### RT-CLM-usefulness-invariant
Label: Completed retained programs satisfy historical usefulness

Claimed operation: after checking outside an incomplete self-modification program, all currently valid probability changes are associated with programs recursively considered useful. Enforcement owner: fixed top-level; enforcement point: the comparison/restoration loop, not the modifier itself. Guarantee strength: invariant. Covered paths: documented IncP/DecP changes with stack history and enabled checking. Alternate paths: ongoing unfinished programs postpone enforcement; proposed teacher forcing bypasses restoration; proposed circular overwrite limits available direct restoration. Required external contract: accurate reward/time bookkeeping, saved distributions and correct primitive/evaluator execution. This is not an environmental safety or future-performance guarantee (SRC-1, §3.2 FACT 3; §4 comments 1, 6, 16, 19).

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> All currently valid probability
> modi cations were computed by currently useful self-modi cation programs.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> However, the system will never have a
> proof that a particular self-modi cation program was the \true" reason for more payo .
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

#### RT-CLM-experimental-comparison
Label: Author-reported benefit with self-modification enabled

Claimed operation: §5 compares system lives with IncP/DecP enabled versus disabled. The variable task reports cumulative payoff about 18.7 million versus 1.41 million. The maze task reports cumulative payoff about 957 million versus 79 million, and a final current average trial length of 79.7 steps for the enabled system; the disabled life has average trial length 12,637. These differently scoped averages are not a like-for-like final-time statistic. A corrupted-input maze experiment is also reported, without the same disabled comparison. The treatment bundles the two modifier capabilities and their interactions with evolving state: it does not isolate GetP, any specific modifier, or meta-learning as a separate cause (SRC-1, §§5.1.1–5.2.2).

- operation conclusion status: claimed
- causal conclusion status: uninspected

> Performance was measured with and without self-modi cation capabilities. In the latter case, the
> primitives IncP and DecP had no e ect.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

> The purpose of this section, however, is not to perform a statistically signi cant
> experimental evaluation of the system's initial bias, or to study e ects of introducing di erent kinds
> of initial bias, or to compare the system to other learning systems with di erent initial bias.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-probability-selection
Label: Live distributions govern later primitive selection

Consumer: interpreter at the program address selected by IP. Channel: Pi values used for sampling primitive and argument integers. Force: fixed probabilistic sampling semantics, conditional on syntax and task primitive constraints; delivery to the sampler changes probabilities, not a guarantee of any specific successful action. Horizon: subsequent instructions and runs in the same system life, until further modification or top-level restoration. Persistence across process restarts is uninspected. Source: SRC-1, §3.2; update and retention routes are [RT-RTE-self-modification](#rt-rte-self-modification) and [RT-RTE-credit-assignment](#rt-rte-credit-assignment).

> a primitive and the corresponding arguments are chosen randomly according to the current probability
> distributions, as already described.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/incremental-self-improvement-90fb0a2a9508/kb/agentic-system-analyses/state/AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01/sources/fki198-94.txt`

## Annotations

none
