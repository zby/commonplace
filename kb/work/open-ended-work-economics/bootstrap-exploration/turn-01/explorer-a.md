# Turn 1, Explorer A: useful work before automation yield

## Finding and status

**Increase the range and quality of worthwhile knowledge work the operator can get done with acceptable total burden—not the amount of methodology the system can execute.** Future automation is an investment hypothesis about that outcome. It also deserves exploration when its return cannot yet be estimated; such exploration should remain a declared research expense, not be booked as delivered usefulness.

This is a bounded conceptual exploration, with one borrowed challenge and two repository episodes. It does not demonstrate an improvement to the system or select an objective function. The [commission](../README.md) supplies the bootstrap purpose; [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) already declares more useful and better-warranted knowledge work per unit of human judgment, explicitly not automation. My contribution is to expose choices hidden by that formulation, not replace it. Proposals below await operator decision.

Why this question merits this turn: choosing what counts as progress changes which user problems become attractive development cases. A system can make its automation measure improve simply by choosing easier-to-check work and leaving valuable difficult work untouched.

## What should increase—and what must not be collapsed

I propose reading progress through three questions rather than one new score:

1. **Present service:** which operator purpose can now be served better, with what warranted result and what work still supplied by people?
2. **Future service:** what later task is now plausibly easier, more reliable, or newly feasible because something was learned? What observation would distinguish that from merely retaining more instructions?
3. **Freedom to redirect:** can the operator change the question, reject the method, or resume work after failure without disproportionate reconstruction? This is a proposed aspect of usefulness under changing purposes, not an adopted independent maximand.

These questions keep distinct a completed useful result, a candidate improvement, and a reusable capacity that has actually survived another application. They need not all increase on each task. An urgent one-off answer can be worth producing even if nothing general is retained. Conversely, an informative failed automation attempt can justify research expenditure without having served the immediate user task.

The KB's [separation of usefulness, autonomy, warrant, and power](../../../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) supports this distinction as an argument, not as four independently validated measurements. Its important implication here is that transferring a step to an agent cannot by itself establish increased usefulness. My additional claim is that selecting which steps or tasks to attempt can conceal the same substitution before execution begins.

### Challenge the denominator as well as the numerator

“Per unit of human judgment” expresses a good concern but does not supply an accounting unit. One approval after reading a long report is not equivalent to one quick clarification. Nor is more judgment necessarily undesirable: an operator may want to understand a problem rather than receive a finished answer.

**Conjecture:** for learning, diagnosis, and consequential design work, making some judgment easier to exercise can be more useful than eliminating it. The mechanism is straightforward: the answer is an input to a later human decision; removing the interaction that builds the person's understanding may lower the value of an otherwise correct artifact. This has not been tested here.

Consequences for interpretation, not a proposed replacement metric:

- Compare operator burden on a named task, including setup, reading, correction, and recovery—not just interventions during execution.
- Keep purpose explicit. “Decide for me,” “help me decide,” and “help me learn to decide” can demand different workflows on identical source material.
- Do not infer improvement from a better ratio if valuable work was dropped from its numerator. A system completing only easy jobs can look efficient while serving less of the operator's actual need.
- Do not require monotonic reduction in human effort when the operator deliberately expands the work's scope. Report that scope change rather than treating it as a cost-saving failure or an efficiency success.

## Where present usefulness and future automation conflict

The following are constructed cases, not observations of prevalence.

| Decision | Present-use case | Future-automation case | What would change the choice |
|---|---|---|---|
| Finish a one-off explanation or generalize its method | A timely explanation resolves the operator's uncertainty | Another pass may reveal reusable checks | A second plausible consumer and a failure that the check could catch; absent these, generalization is research, not delivery |
| Let the expert repair a draft or ask the agent to diagnose and retry | Repair can be fastest and safest | Retry may expose a missing criterion or capability | Stakes, reversibility, and whether the retry supplies discriminating information rather than another fluent draft |
| Choose the next development task | An awkward, unique task may matter most to the operator | A repetitive, well-checked task offers cleaner automation feedback | Whether the choice is product work or a declared learning probe; do not relabel the latter as user demand |
| Preserve a rich episode or only its conclusion | Rich capture interrupts work and creates reading costs | The episode may let a later worker challenge the explanation | Which later uncertainty needs the otherwise-lost evidence; storage alone creates no demonstrated capacity |
| Standardize the workflow or leave methods open | Standardization reduces setup and makes execution predictable | Premature standardization may make later cases fit an inherited procedure rather than improve it | Whether a contrasting case requires a different method while preserving the same purpose |
| Increase unattended execution or preserve informative interaction | Unattended execution may free attention | Interaction may reveal tacit acceptance criteria that automation otherwise optimizes around | Whether the lost interaction supplies purpose, evidence, diagnosis, or merely routine permission |

The conflict is not simply “use now versus learn later.” Present use can supply the best correction to a method, while a separate research exercise can overfit a synthetic task. Equally, real work can teach the wrong lesson: a successful expert repair may conceal that the supposed automated method still depends on an expert.

**Candidate addition to the plan:** distinguish the work delivered from the learning opportunity bought by doing it in a particular way. This requires no general ledger or new schema. A sentence identifying the extra effort and what uncertainty it targets can suffice in a bounded trial. The [use-and-outcome records workshop](../../../use-and-outcome-records/README.md) owns any broader recording design.

## Evidence and challenges

### 1. Repository evidence: successful enforcement is narrower than useful work

The retained [tag-readme trace](../../../../theory/evidence/tag-readme-trace-observed-causal-connection.md) describes changes to the type, instructions, schema, validator, and rendering, followed by a validator catching a block-YAML member the search recipe missed. This is a concrete episode of development and use correcting methodology. It is not merely another note endorsing the idea.

Its own calibration matters: the initial detection was human, and the change relocated verification rather than separating the two jobs completely. The record supports a bounded operational consequence. It supplies neither a net operator-cost comparison nor proof of transfer to another kind of knowledge work. I read the retained reconstruction, not the underlying commits afresh.

Decision implication: a successful bootstrap episode should be reported at the level actually observed. “The new check caught this omission” is stronger and more useful than an unsupported “the system became more autonomous and productive.” The missing cost comparison does not erase the local result; it prevents inflating it.

### 2. Repository evidence: an informative trial can rationally end without adoption

The [synthesis-pilot cost case](../../../use-and-outcome-records/synthesis-pilot-cost-case.md) records an operator reducing a proposed 36–48-call pilot to eight calls. A first control attempt exceeded its cumulative-token ceiling; a revised delivery route then completed the eight-call check. The retained case reports failure to preserve the intended distinction and no basis for adopting the combined treatment under its rule. It also separates process completion, resource consumption, method outcome, and still-unobserved production benefit.

This is evidence of a concrete allocation and stopping decision, not evidence that smaller experiments generally dominate. The unrun larger plan has no observed cost or outcome. Nor does this single case measure reliability. It nevertheless makes an important option visible: spend enough to discover that a proposed methodology is not yet worth adopting, then stop without turning the research procedure into the product.

Decision implication: this five-turn trial should be allowed to leave the main plan mostly unchanged. Counting the number of extracted recommendations would reward invention precisely when a bounded negative result is more useful.

### 3. Borrowed challenge: useful execution may survive while adaptation fails

[Naur's *Programming as Theory Building*](../../../../sources/programming-as-theory-building.ingest.md) states that a program may continue producing useful results after its theory-bearing team dissolves, while the loss becomes visible when modification demands cannot be answered intelligently. His retained compiler case reports successors proposing patches despite substantial documentation, while the original team could suggest simpler changes within the existing structure.

These are a conceptual argument and reported human-programmer cases, not a controlled comparison and not evidence of an LLM limitation. I borrow the diagnostic distinction—**continued execution is not demonstrated capacity to accommodate new demands**—without adopting Naur's claim that the relevant understanding is necessarily inexpressible or exclusively human.

Transfer conjecture for this commission: an automated methodology may perform familiar tasks while failing to recognize that a new operator purpose changes what counts as a good result. A nearby but meaningfully changed purpose is therefore a useful challenge to a claimed learned method. Replaying the original task only tests replay. This is an analogy from software maintenance to methodology maintenance, not a demonstrated result across domains.

### 4. Existing investment argument: correct condition, unsettled applicability

The KB's [long-run machinery-investment argument](../../../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) says investment can dominate immediate learning when the benefit persists and its net return exceeds alternatives. That conditional is compatible with this exploration. It does not tell us whether the contemplated improvement will persist, be used, or improve valuable work.

A practical challenge to its opening “paid for once” intuition is recurring interpretation and maintenance. Those costs are acknowledged in its scope. For this task the operational question is not merely how many future runs there might be, but how many future runs still need the same method after the model, purpose, corpus, and acceptance criteria change. This is an unknown, not a reason to prohibit investment.

The [proximate-target argument](../../../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) makes the relevant logical point: checking that a property was achieved does not check that the property serves the objective. More executable methods, retained rationale, or unattended steps are candidates of this kind. Agreement among these KB notes is not independent corroboration.

## Strongest rival: task-first assistance with selective reusable tools

The strongest rival is not a system that never learns. It is a simpler service: handle worthwhile user tasks with a capable model, available tools, and ordinary correction; retain small reusable improvements only when a recurrence or concrete failure makes them worthwhile. Do not make learning to automate methodologies a standing deliverable of every task.

Why it could win:

- A general model already supplies much methodological competence; a growing local instruction corpus can add loading, conflict, and repair costs without adding useful discrimination.
- Real demand selects valuable problems more directly than an internal automation agenda does.
- A short-lived method may never repay its capture and maintenance costs.
- Immediate conversation can recover purpose more cheaply than attempting to encode every contingency.

Its strongest weakness is that task-local success can repeatedly depend on the same unretained correction. It can also lose evidence about why the correction worked. A deliberate bootstrap program could outperform it by turning such failures into reusable, checkable changes and by searching beyond recurrent annoyances. Neither superiority is demonstrated in this exploration.

A bounded comparison worth considering later would hold a real operator purpose and resource allowance fixed, compare task-first assistance against assistance with an explicit methodology-learning investment, and then expose both to a related task with a changed condition. Judge immediate usefulness and later performance separately. Include the learning arm's capture, checking, and maintenance burden. A tiny comparison could reject an obvious failure or justify another probe; it could not establish broad superiority. This is a proposed discriminating shape, not a commissioned protocol or controller build.

## Possible changed decisions

1. **Do not adopt work moved between resource tiers as the objective.** Keep tier movement as a possible means, judged against its operator consequences.
2. **Do not require every useful task to produce a reusable method.** Permit a clean one-off result and separately authorize exploratory investment. Conversely, do not force every exploration to justify immediate applicability.
3. **Require a claimed learning gain to identify what became possible or better on another use.** Until that use occurs, call it a candidate method or expected benefit, not demonstrated automation capacity.
4. **Retain task-first assistance as a live rival.** Compare against the best simple alternative, not an artificially forgetful baseline.
5. **Before choosing a test domain, ask which purpose it represents.** A portfolio of many easy-to-check task names does not by itself establish usefulness across kinds of knowledge work. Which kinds matter remains an operator choice.
6. **Make stopping without adoption a valid result of this trial.** The useful output may be a sharper limit or a deferred decision rather than a new procedure.

These recommendations refine means within the commission. Choosing domains, changing the weight given to operator learning versus delegated completion, or replacing the bootstrap purpose would require operator direction. I have not made those choices.

## Unknowns, evidence limits, and parked ideas

- No agreed task portfolio, recurrence horizon, or unit of human judgment is available here. Thus no numerical objective, amortization estimate, or claim of general productivity gain is warranted.
- It remains unknown how much retained methodology adds beyond the base model, tools, and task-local conversation. It may help particular failure classes without being broadly beneficial.
- It remains unknown when extra interaction teaches the system something reusable versus merely rescues the current run. Proposed changed-condition probes do not settle that by themselves.
- **Evidence limitation:** the inspected Bainbridge and HarnessCompass ingests have no retained Quotes. I did not use their summarized claims as evidence, access their snapshots, or start grounding outside my authority. Their human-oversight and transfer questions are parked; this output is partial with respect to external empirical adjudication.
- Parked: preserving operator understanding as a first-class product outcome; estimating how model changes shorten a method's useful life; selecting domains by diversity of purpose rather than surface task names. None is a new scope commitment.
- Parked: whether a system that learns when *not* to invoke a methodology is a better bootstrap target than one maximizing methodology execution. This may matter because bypassing a method can be the correct adaptation, but no such target is adopted here.

## Execution, isolation, and available costs

- Read the commission, parent framing, `AGENTS.md`, and `kb/work/COLLECTION.md` fully. Used scoped `rg` searches, topic navigation, library arguments, source Quotes, and peer-workshop evidence. Searches covered theory, references, instructions, tracked sources, and external-system analysis descriptions; this was not an exhaustive survey of the KB.
- Did not inspect other turn-01 agent outputs or coordination results. No nested assignments, no delegated sessions, no source ingests, no snapshots, no library/code edits, and no commits.
- Session: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-11-05T16-15-42-053Z_01a1ac7e-9fe4-7782-880c-de1483f0bc6a.jsonl`. Runtime model: `gpt-6-astra`.
- Available cost facts: one explorer session; zero delegated jobs; one authored artifact. Token usage, monetary cost, aggregate model runtime, and operator review time are unknown here. Numbers in the cited pilot belong to that prior episode, not this exploration.
- Validation: `commonplace-validate` succeeded for this file with zero failures and warnings. A separate path check found all nine local Markdown links resolve. Text validation supplies no semantic verification. Broader connection discovery, if wanted after integration, belongs to `cp-skill-connect`; none was delegated or commissioned here.
