# Operationalization, executability, automation, and autonomy — revised exploration

**Status:** a workshop investigation, not adopted technical vocabulary, empirical proof, or a system change. **Revision:** 2026-10-31, responding to the operator's objections that the first account confused generalization with operationalization, treated automation and autonomy too similarly, and did not check source ingestability. Repository starting point: main at d19065b3aef33ffca92fa2f72f5203251fcae3b0. Literature access was checked on 2026-10-31. **Second revision:** 2026-10-31, after the merge of the draft, a review of it, and the ingestion of five candidate sources. The review found that the draft restated the operator's directives as findings, misdescribed the existing actionable-methodology relation, and introduced five workshop-local coordinates without saying which are new concepts. Section 6 and the amended disposition answer those points with the ingested sources.

## Central result

**Operationalization is relative to a defined task T (including its application area) and an executor E in an operating setting S.** It is not an intrinsic property of a text. A task definition specifies *what* is to be accomplished and *where* its validity is being claimed; operationalization asks how existing knowledge can guide E in accomplishing that task. What a trained researcher can use immediately may need adaptation for a novice, an LLM agent, or a deterministic interpreter. Every claim that something is operational must state the task, application area, executor, resources/authority, and adequacy criterion.

There are more than two possible transformations of a methodology; moreover, properties of the methodology must not be confused with properties of an executor, its runtime, or a particular execution.

**Generality (outside operationalization):** which additional tasks or application areas a theory or method can adequately guide. This may be researched or expanded, but doing so changes the knowledge's claimed scope or the task specification rather than being a constituent operation of operationalizing a *given* task.

**Constraining:** which readings, choices, or responses the method permits or prefers for a named consumer.

**Methodological coverage (or operational completeness):** which consequential tasks and decisions *in applying* the method have some usable guidance, including how to recognize its applicability, obtain information, choose the next operation, deal with exceptions, and stop. Guidance can specify a decision interface or an approach for obtaining evidence without settling its answer. It is not necessary for every choice to have a fixed answer. Methodological closure, already defined in Commonplace, is stronger: it concerns whether the retained method settles consequential decisions, not merely whether it supplies useful guidance for them. Coverage is therefore closure without the settling condition. Treat it as a diagnostic reading of the existing term, not as a candidate term of its own.

**Operational integration:** whether guidance reaches the relevant executor at the relevant time, with the requisite tools, state, permissions, feedback, invocation and binding authority. Integration changes *the configured system*; it need not alter the methodology's content or range of validity.

**Situated executability:** whether the specified executor and environment can actually perform the required work to an identified standard. This is a relation, not a textual genre and not a single successful trace. It is not a new predicate. It is the existing [actionable](../../theory/definitions/actionable-methodology.md) relation with one addition: the task's success standard over the cases T admits. Section 2 states the correction.

These are diagnostic coordinates rather than scalar scores or a complete axiomatization. **They do not all belong inside operationalization.** Generality belongs to the knowledge's scope (or to changing task definition); automation, autonomy and warranted reliability characterize the configured executor and outcome. Operationalizing for a *fixed* task may constrain local choices, fill in guidance and integrate resources without claiming that the method now applies in more domains. An accidentally discovered wider application is a possible research result, not part of operationalization by definition. Distinguish the task's intended domain, what the source knowledge justifies, and what E actually handles successfully.

**Operationalization** is provisionally the activity of making knowledge K usable for **task T by executor E** under a declared operating setting S. It may produce an artifact or an operating arrangement, and it may leave substantial choices to E. The *task definition* supplies the application area, goal, success/stop conditions and binding boundaries; these are inputs to the operation, not scope to be enlarged by it. There is no requirement that operationalization maximize detail or constrain all choices. Generalization is a separate effort to establish how K or an existing method carries over to other tasks or applications.

There is a potential linguistic double use: a theory can be made action-guiding as a methodology **for T**, and an existing methodology can be made operational as a skill **for the same or a narrower T and E**. Both are instances of the same task-relative operation, not necessarily different definitions of 'operationalization' or mandatory successive transformations. Simply granting tools, delivering an existing instruction, or preserving runtime state can also improve the task-facing operating arrangement without deriving another methodological artifact.

Commonplace already has a **narrow artifact-lineage convention**, `operationalized-from`, in [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md): a methodology-to-procedure pairing where ordering, defaults, or stopping conditions are added. Do not silently broaden that adopted relation to all task-relative operationalization, especially theory-to-method work or deployment of existing artifacts. The conceptual use can be broader while its formal lineage label remains narrow pending a separate decision.

## 0. Task definition fixes application; operationalization makes knowledge usable for the task

**Task definition and operationalization are separate operations.** A task definition T supplies the *application area* (target/problem class), objective, success criterion, and binding scope and authority conditions. It may be a specific case ('assess this empirical claim') or a family ('review the causal claims in this class of papers'). It need not be a complete plan, and an open-ended task can state how its scope may be revised when new evidence appears.

**Operationalization** takes T as a given and asks how knowledge K can guide executor E, with competence and tooling S, to perform T. Its output may be a task-facing methodology, an interpreted checklist/skill, a code component, a hybrid arrangement, or no new artifact when E already knows enough. Success is relative: the arrangement improves or enables E's appropriate task-guided decisions, not merely produces more words. It does not establish generality beyond the application area specified by T or guarantee task success.

A working relation, **not a formal Commonplace definition**, is:

`operationalize(K, T, E, S) → task-facing method or operating arrangement A`

where T fixes the evaluated application, E and S supply actual competence and action possibilities, and A is judged by whether it makes K usable to guide T. Neither the output type nor the number of steps is fixed.

The [operationalism ingest](../../sources/operationalism-sep.ingest.md) adds three conditions to this relation. They come from the discipline that owns the word, so they are transfers by analogy, not established results.

1. **A is partial.** Operationalizing K for T and E selects which operations and indicators count as applying K for this purpose. Part of K stays outside A. That residue is what A can be checked against. An account in which A exhausts K cannot say when operationalization went wrong (Gillies' validity argument).
2. **"Executable by E" names a typed range of operations.** If the range includes open-ended judgment, the relation rules nothing out. If it includes only codified steps, it collapses into [codification](../../theory/definitions/codification.md). This is Margenau's dilemma carried over to executors. The workshop has not yet typed that range; the cases in section 6 are the material for doing so.
3. **A is an indicator hypothesis.** Following Bunge, treat "these operations serve K for T by E" as a fallible claim open to test, not a definition. The [Church–Turing ingest](../../sources/church-turing-thesis-sep.ingest.md) records the same status for the thesis itself: Turing placed it between a theorem and a definition, and Post objected that calling it a definition hides the need for continual verification.

Condition 3 also settles how to read the "central result" above: it is a tentative identification, to be tested against cases, not a stipulation.

**Two examples with the same operation:**

| Starting knowledge K | Fixed task T and executor E | Possible result A |
|---|---|---|
| A Popperian explanatory account of conjecture and criticism | T: critically assess claims in a research article; E: research-experienced human | A methodology explaining how to form criticisms and seek discriminating evidence; perhaps no detailed checklist |
| Existing conjectural-criticism methodology | Same task; E: LLM-based Commonplace agent with bounded context and tools | A selected skill, available source references, authority and stop conditions, and relevant tool access; only the missing pieces need to be supplied |

The first is often described as **theory → methodology**; the second as **methodology → procedure or operating arrangement**. They share the functional test *makes K usable for T by E*. In a different project a methodology might not derive from one articulated theory at all. The [actionable-methodology definition](../../theory/definitions/actionable-methodology.md) classifies methodologies by the guidance they supply, not by their ancestry, and the [two-layer account](../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) explicitly allows methodology-native content.

**Where generalization belongs:** after developing A for T, one can conjecture that K or A works for a broader task T'. Establishing that claim requires new reasoning or evidence about the expanded application area. The act of extending T to T' is a **task-definition or method-scope revision**. Operationalizing for T' is a further task-relative operation. If operationalization for T unexpectedly discovers a general technique, retaining and testing that conjecture is separate from completing T. The same method may be operational for E on T but not on T', even if the theory's principles remain applicable.

**Important boundary case:** operationalizing K for T can reveal that T is infeasible, inconsistent, or under-specified. This is useful feedback to task definition, not license for the operator or agent to silently broaden or replace T. Return the issue to whoever owns task selection, or revise T through an authorized decision. The task can authorize scope discovery as part of its objective; in that case the rules for choosing a new application are part of T rather than an accidental generalization during execution.

**Other boundaries:** constraining choices, supplying a richer method, codifying a local rule and integrating a workflow are *possible means* of operationalizing for T. They are not definitions of operationalization. Automation is subsequently about which task functions the configured system performs, and decision autonomy about what choices E may make. An operationalized arrangement may remain entirely human-executed.

**Provenance versus situated use:** `operationalized-from` in [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) remains the authorized **methodology→procedure** lineage claim, not a generic marker that K has been made operational for T/E. A procedure can satisfy that lineage convention but be unsuitable for E. An unchanged methodology can be directly usable by E without another derivative. No automatic regress follows from the fact that a methodology can itself operationalize a theory.

## 1. From descriptions to situated action

A *description* reports how work occurred; an explanatory theory proposes why. A *methodology* supplies an intervention-relevant mapping: which kind of action, comparison, rejection, or evaluation is favored in represented conditions. An instruction like 'critically assess the causal claim' can be a thin method when a proficient actor reconstructs appropriate tests; it is not an exhaustive plan.

Given a specified task T, inspect the specific barrier to E using K instead of assuming that more detailed steps are the missing ingredient. **Changing the problem domain is a separate task-definition/generalization decision**, not a default operationalization move:

| Potential gap | Candidate intervention | Property principally affected |
|---|---|---|
| The method does not cover T's application area | Return a gap to task/method choice; separately propose revising T or researching generalization | **Outside** operationalization for the fixed T |
| Multiple plausible interpretations cause wrong choices | Add purpose, disambiguation, exclusions or examples | Constraining |
| The methodology does not address how to handle missing evidence or exceptions | Add decision criteria, evidence-gathering, fallback or stop rules | Methodological coverage |
| The model knows the method but does not select it | Select/routinely activate a coherent method, perhaps via a short cue | Activation, not necessarily more content |
| The operator cannot access the target or tools | Provide resources, permissions or a different execution channel | Situated executability, not theory generality |
| Work loses its position across context windows | Retain state, recover checkpoints, arrange subsequent calls | Operational integration and horizon |
| A deterministic check is cheap and stable | Commit the local predicate to code | Codification, local reliability |
| The evaluator cannot tell when the work is wrong | Improve evidence, testing, oracle discrimination and recovery | Warrant of outcomes |
| A person still performs an internal function | Transfer the specific function to computation | Automation coverage |
| The agent has no authority to choose a method or initiate a branch | Deliberately delegate authority and specify bounds | Decision autonomy; perhaps greater unattended scope |

A broadly general methodology might be unavailable at the point of need for T. A well-integrated task procedure may be narrowly applicable by design. A capable executor may perform judgments never prescribed by the method. These cases falsify a one-directional scale of 'more operational'.

**No necessary monotonicity:** additional operational guidance may lower performance by prescribing a method before relevant evidence appears, forcing premature stopping, overloading context, or requiring a model to resolve contradictory constraints. Commonplace's [author–executor determinability rule](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) addresses this precise risk. A stronger artifact may fix governing intent and leave more means open; this combines stronger *appropriate* constraints with more contingent freedom.

## 2. Executability and the actor-relative boundary

For a task definition T (including its application area, objective, success conditions and scope), method M, executor E, supported operations O, target/environment S, delegated authority A, and resource horizon H, the useful question is: can that arrangement execute T using M adequately on the **cases T admits**? There is no reason the answer must be invariant between a trained human, weaker LLM, stronger LLM or code engine.

Three levels of evidence differ:

1. **Can be attempted:** the actor can interpret the method and has a way to act.
2. **Can complete a specified task:** the actor has the necessary operations, state, competence, permission and control to reach an outcome in a declared setting. Commonplace's existing [actionable methodology](../../theory/definitions/actionable-methodology.md) already covers most of this level, not only level 1: its four elements require an operator that can follow the mapping, available operations with the needed access, resources and authority, and a target those operations reach. The first draft of this workshop understated that. What the existing relation does not carry is an explicit task with an objective and a success criterion over admitted cases. That is the only addition this workshop makes at level 2.
3. **Works adequately across a domain/horizon:** observed results satisfy an acceptance standard under representative variation, including exceptions, not just one successful demonstration.

A trace proves an execution occurred. It does not show fidelity to the method (the actor may import its own method), goal success (the method may be wrong), repeatability (inputs and environment may differ), or generally reliable execution. These are separate claims.

**Human algorithm counterexample:** pencil-and-paper long division is an exact effective procedure for a properly trained human. It does not become executable only when translated into a computer program. The classical effective-procedure sense from computability theory is restricted to mechanical steps requiring no ingenuity; it is not the broad sense of a judgment-heavy method *being executable* by a capable LLM.

**Human checklist counterexample:** a checklist can be made operational for a team through prompts, roles and timing while remaining manually performed. Making such a method actionable neither supplies an LLM with sensorimotor competence nor gives it clinical or legal authority.

**Agent research counterexample:** a research skill can be executed by an LLM even while it requires unanticipated judgments, choice of sources and criticism. Computational action can use natural language; there is no necessary crossing to symbolic code.

## 3. Automation is not autonomy

The prior account conflated 'who does the work' with 'who is free to direct it'. Their distinction must be made explicit.

**Automation is an allocation of task functions to machinery/computation.** It asks which operations otherwise performed manually are executed by the system. Its unit can be information acquisition, analysis, decision proposal or execution. An automated function may be highly prescribed and lack discretion. A partially automated end-to-end process can still include manual approval, diagnosis, data entry or recovery.

**Decision autonomy is discretion and authority over consequential choices within delegated limits.** It asks who selects goals/subgoals, methods, alternatives, exceptions, and authorized external actions, and whether the actor can revise its course on newly encountered evidence. Autonomy need not mean permission to do anything; meaningful bounded delegation is still autonomy. Decision autonomy can coexist with a mandatory human authorization gate outside the agent's scope.

**Unattended continuity is another property**, often associated with autonomy in ordinary speech: can the workflow run through the declared functions and horizon without requiring a fresh human production decision? Commonplace's existing [computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md) addresses this property cleanly. A script can be computationally closed for invoice calculation but have almost no discretion to reconsider its procedure. Neither computational closure nor discretion establishes warranted outcome quality.

| Example | Automation of scoped functions | Decision autonomy | Unattended continuity |
|---|---|---|---|
| Fixed batch script calculates payroll | Full for specified arithmetic | Very low; policy and means fixed | Yes, for the bounded batch when inputs are supplied |
| Agent independently proposes and revises a research strategy; human gathers sources and approves publication | Partial (planning/analysis) | Substantial in planning, limited in external action | No, for the whole task |
| Agent drafts code and runs tests; human must decide merge | High for production steps | Substantial within assigned design scope, no merge authority | No, if merge is required for completion |
| Agent chooses methods, fetches sources, evaluates, commits within standing authorization, including recovery | Potentially full for its declared task | High but bounded | Potentially yes if all required functions are computationally supplied |

These examples do not define a universal numeric measure. A function allocation is not commensurable across arbitrary systems, as [autonomy measurement](../../theory/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) explains. External user requirements at task commissioning are different from a human supplying run-time design or repair decisions. Decide which are outside the evaluated production boundary *before* measuring its closure. A human approval step essential to an in-scope completed artifact cannot be hidden as external 'feedback'.

### Can operationalization make a methodology fully automatable with LLMs?

**Executor-relative operationalization is neither logically sufficient nor always necessary for fully automated LLM task performance.** It can increase the possibility and feasibility of that performance. A methodology may already be directly usable by one LLM but not another; matching its instructions to E does not create missing competence, permissions or outcome verification.

1. The model may already know the method and automatically do the relevant work from a broad objective without any newly retained operationalization. This is automation without explicit method extraction; it remains vulnerable to wrong method selection and opaque model competence.
2. A written methodology could fully guide a competent human but still be impossible or untrustworthy for an LLM in the same setting because it lacks tools, perception, context, substantive skill, or authority. Completeness for the human is not completeness for the model.
3. A model can autonomously supply consequential decisions *not settled by the method* from learned competence and situated evidence. Thus **methodological closure is not necessary for computational closure**. But computationally completing the task once does not imply reliable or warranted completion.
4. A narrow fully automated task can be accomplished with little decision autonomy (a deterministic calculator). A highly autonomous agent can still depend on a person for in-scope execution or admission. These are the opposite counterexamples to treating the two as one dimension.
5. An LLM system may be able to execute a whole task only for an explicitly bounded input domain, authority envelope and horizon. A policy of refusing or escalating exceptions is an appropriate safety behavior but **does not count as independently completing** the escalated cases. The full automation claim must either exclude those cases in advance, or admit that coverage is partial.

A task is 'fully automated' only relative to a fixed task boundary and completion criterion, when every production function necessary to complete its admitted cases is computational, including selection and evaluation if they are internal to the task. Its goals, authorization envelope and model may be human supplied initially. If autonomous *task choice* or revision of the operating rules is in scope, that is a larger task and demands a larger test.

This separates three propositions: **the method is operable by this system; the system can complete the whole task unattended; the results are adequately trustworthy**. They require different evidence.

## 4. Revised architectural account: several independent changes, not one progression

The earlier chain 'knowledge → selection → execution → evaluation → retention' confused logical functions with a developmental trajectory. A fixed task definition T gives the application area and evaluation boundary; operationalization concerns making K usable for T by E; generalizing to T' is another project. All those functions may exist even for a human paper-and-pencil system; the architecture can change any one of them, in different directions.

A better analytical map is:

| Layer of question | Variable | Example of progress without codifying more |
|---|---|---|
| Knowledge and task design, **outside operationalization for fixed T** | Generality/domain of applicability | Research whether criticism principles also work for adversarial evidence; define and test T' |
| Method itself | Semantic commitments/constraints | Preserve binding provenance but leave evidence-gathering tactics open |
| Method itself | How much application logic is addressed/settled | Add a way to seek discriminating evidence, without preselecting its outcome |
| Task-relative operationalization | Derive prescriptions from knowledge K for T and E | Work an epistemic principle into a strategy for criticizing claims of the class specified by T |
| Task-relative operationalization | Make an existing method usable for T and E | Derive an LLM skill only if E needs it; otherwise supply missing resources or use the method directly |
| Method use | Selection, activation and authority | Route an existing method and verify that it governs the relevant decision |
| Operational environment | Tools, state, checkpoints, feedback | Enable an unchanged method to be used over longer tasks |
| Actor capability | What E can infer and decide when the method falls silent | A stronger model handles new cases through its learned knowledge |
| Labor allocation | What work computation performs | Transfer source synthesis or experiment design from human to LLM |
| Delegated control | How much discretion/initiative/authority computation has | Let the model select next probes inside an approved envelope |
| Continuity | Which required functions can run without new human intervention | Replace recurring human troubleshooting with bounded recovery |
| Evaluation | Scope of justified trust | Better independent checks, not merely stronger confidence claims |

Important pairwise counterexamples:

- **Generality without operational integration:** a principled method applies in theory to more domains but is never retrieved or routed.
- **Integration without generality:** the exact same research method can act on an existing case after the agent receives source access.
- **Constraining plus generality:** adding a clear applicability test excludes wrong uses while improving successful use across new classes of cases.
- **Operational completeness without methodological closure:** a method says to choose tests by their expected discriminatory value; it prescribes a *procedure for choosing* without predetermining every test.
- **High automation, low discretion:** fixed rule calculates and files a result under preapproved conditions.
- **High discretion, low task automation:** an agent chooses a research plan while people collect samples and approve final action.
- **Full continuity, poor warrant:** unattended agent incorrectly accepts unsupported claims.
- **More detail, less success:** fixed source order blocks following an unexpected disconfirming lead.

The [bounded-context orchestration model](../../theory/bounded-context-orchestration-model.md) provides a computational account only for closed-world workflows with explicit transition-relevant state and suitable barriers. Other environments need richer execution models; none of the conceptual dimensions above implies every workflow should use a deterministic scheduler.

**Architectural diagnosis:** first identify the failure mechanism—lack of applicability, wrong interpretation, missing method decision, failed activation, unavailable operation, context drift, weak competence, inadequate feedback, inappropriate human handoff, or poor warrant—then select a targeted intervention. Codification is one intervention in that space, not the destination of a universal pipeline. A method's supported domain and a system's *actually completed* task domain must be measured separately. Improving activation or tools may move the latter without modifying the former.

## 5. Literature, status of ingestion, and limits of transfer

'Available for ingestion' below means a publicly accessible primary text or full, usable scholarly/web source was found, not that a snapshot was downloaded, a license permits republishing, or the mandatory source-ingest workflow was run. Commonplace keeps reading snapshots local/ignored and tracks analyses separately; see [source collection contract](../../sources/COLLECTION.md) and the cp-skill-ingest workflow. Under copyright restrictions do not distribute primary texts through the tracked repository.

| Source | What it can test | Existing ingest? | Source access checked 2026-10-31 | Disposition |
|---|---|---|---|---|
| Wielinga, Akkermans & Schreiber (1998), [competence theory](https://www.cs.vu.nl/~guus/papers/Wielinga98a.pdf) | Method competence → conceptual refinement → operational choices; possible competence loss | [Yes](../../sources/competence-theory-problem-solving-method-construction.ingest.md) | Full author/institutional PDF surfaced | Reuse existing ingest; do not duplicate |
| Parasuraman, Sheridan & Wickens (2000), [automation levels](https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf) | Function allocation distinct from full-task automation and human performance | [Yes](../../sources/model-types-levels-human-interaction-automation.ingest.md) | Full PDF accessible | Reuse existing ingest |
| Bainbridge (1983), [Ironies of Automation](https://doi.org/10.1016/0005-1098(83)90046-8) | Human exception burden, automation failure and deskilling | [Yes](../../sources/ironies-of-automation.ingest.md) | Existing ingest has full user-supplied PDF capture; publisher paywall | Reuse existing ingest |
| Norman (1989), [NASA-hosted original report](https://ntrs.nasa.gov/api/citations/19900004678/downloads/19900004678.pdf) | Automation feedback/exception boundary; delegated function versus full role | [Yes, this run](../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) | Full 14-page ICS Report 8904 captured; scanned two-column layout, so extracted text is noisy | Ingested; the journal reprint is a different publication and was not captured |
| Suchman (1987), [Plans and Situated Actions](https://course.khoury.northeastern.edu/cs5100f12/resources/reading/suchman-situatedactions.pdf) | Plan ≠ full determination of situated activity | No | Course URL now returns 404. A Wayback capture from 2024-04-22 exists but is a 14-page image-only scan with no text layer, and no OCR tool is installed | Blocked. Needs OCR tooling, a text-layer copy, or a user-supplied edition; do not substitute the 2007 revised edition silently |
| Church–Turing thesis, [SEP entry](https://plato.stanford.edu/entries/church-turing/) | Effective methods as the no-insight limiting case; level-relativity of "the method" | [Yes, this run](../../sources/church-turing-thesis-sep.ingest.md) | Public full HTML article | Ingested; secondary scholarship with Copeland's interpretive position, not Turing's text |
| Operationalism, [SEP entry](https://plato.stanford.edu/entries/operationalism/) | The discipline's own sense of operationalization and its known failure modes | [Yes, this run](../../sources/operationalism-sep.ingest.md) | Public full HTML article | Ingested; supplies the three conditions in section 0 and the Margenau dilemma |
| Plotkin (2004), [origins of SOS](https://homepages.inf.ed.ac.uk/gdp/publications/Origins_SOS.pdf) | Operational semantics is a rule-specified transition relation, distinct from execution by an implementation | [Yes, this run](../../sources/plotkin-origins-of-sos.ingest.md) | The CiteSeerX copy is no longer served; captured from the author's homepage | Ingested; contrast case that keeps "operational" from collapsing into "executed" |
| OMG, [CMMN 1.1 specification](https://www.omg.org/spec/CMMN/1.1/) | A deployed standard that keeps model execution, performer type, activation and discretionary planning as separate controls | [Yes, this run](../../sources/cmmn-1-1-specification.ingest.md) | Normative 144-page PDF captured; figures and lifecycle diagrams lost in text conversion | Ingested; a design standard, not evidence that the design works |
| Haynes et al. (2009), [surgical checklist](https://www.nejm.org/doi/full/10.1056/NEJMsa0810119) | Human operationalization without task automation | No | Publisher returns HTTP 403 to automated capture despite marking the article free | Blocked. Needs a user-supplied copy or another open full-text URL; an abstract would be a weaker, different source |

The sources' meanings do not transfer unchanged: *operational semantics* fixes rules in programming-language theory; *operationalism* addresses measurement and scientific concept meaning; *operational method construction* in knowledge engineering moves toward a task-specific executable control strategy; *automation levels* in human factors classify allocations and interaction. None licenses a universal equation 'operationalize = formalize = automate'.

**Ingest status after the second revision:** five of the seven candidates are ingested and committed (Norman, both SEP entries, Plotkin, CMMN). Suchman and Haynes are blocked for the reasons in the table. Suchman remains the highest-value missing source, because none of the ingested sources addresses situated action against a fixed plan directly. The three earlier reports are reused. Public retrieval does **not** establish a copyright license for committing a full source; the snapshots stay ignored and checksummed.

## 6. Worked cases from the ingested sources

Each case below is read from one ingest. The ingests record their own limits; every transfer to LLM executors is by analogy unless the mechanism is shared.

### 6.1 The effective method: the limiting case where operationalization and automatability coincide

Copeland's four conditions define an effective method: finitely many exact instructions, a result in finitely many steps, performable by an unaided human with paper and pencil, and demanding no insight, intuition or ingenuity ([Church–Turing ingest](../../sources/church-turing-thesis-sep.ingest.md)). The thesis and its easy converse say that a method operationalized to this level is exactly one a Turing machine can carry out. Human computers executing such methods were later replaced by machines doing the same work. That is function-level automation following operationalization with decision autonomy held at zero on both sides: neither executor decided anything.

Two consequences for the workshop:

- **Operationalization entails automatability only for no-insight executors.** Beyond condition 4 it does not. This is the baseline against which the LLM case differs, and it explains why the first draft's "neither sufficient nor necessary" claim in section 3 holds: the claim is about executors that are permitted insight.
- **"The method" is level-relative.** At the level of weights and inference code, an LLM run is mechanical in the technical sense. At the level of the retained task instructions, the same run supplies decisions no method settled. So any claim that K is operationalized for E must name which artifact counts as the method. Without that, "computationally closed but methodologically open" in the [closure note](../../theory/methodological-and-computational-closure-track-different-changes.md) looks like a contradiction with classical computability. It is not; the two readings name different artifacts.

The ingest warns against the equivalence fallacy: the thesis bounds what a human following an effective method can do, not what machines can generate. Do not argue from it to a ceiling on machine judgment, and do not read "mechanical" as "without judgment-like output".

### 6.2 Norman's handover: automating a function versus automating a role

Norman holds the captain's delegation fixed and swaps the delegate: the autopilot or the first officer ([Norman ingest](../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md)). Both "automate" control from the captain's view. Only the human delegate would say "I seem to be correcting this thing more and more." In two incidents the autopilot compensated silently for a growing fault, and the crew learned of it only when the compensator reached its limit and the least recovery time remained.

The mechanism Norman names is the one this workshop needs. The designer's task "is completed when the device functions as requested", and reporting is secondary because "the automation itself doesn't need it." Read in this workshop's terms: **a task definition T written for executor E drops the functions E does not consume.** Anomaly reporting served the surrounding crew, not the control loop, so it fell outside T. This is a mechanism for section 0's claim that T owns the application area and success criteria. It adds a requirement: T must name the functions the previous executor supplied to its surroundings, or operationalizing for the new executor silently removes them.

The case also separates two things the first draft ran together under "automation coverage":

- **automating a delegated function:** the autopilot holds heading and altitude;
- **automating the full role of the previous executor:** everything the first officer did in that seat, including status and anomaly talk.

Norman adds that specific monitors are easy to operationalize (any competent programmer could write one for yoke compensation) while the general case, the next slightly different anomaly, needs "a monitoring of its own monitoring" and a system model nobody knows how to build. That is the escalation boundary in section 3.5 again: escalation is warrantable within a defined anomaly class and unsolved beyond it.

Limits: three incident narratives and one informal simulator run. The "first officer would have said something" premise is untested, and Norman's own fuel-leak replication shows crews missing exactly that cue. The analogy to agents rests on compensation with a saturation limit, which an agent's hidden repairs may not share.

### 6.3 CMMN: four separate controls in a deployed standard

The OMG case-management standard models work that "cannot be orchestrated by a predefined sequence of Tasks" ([CMMN ingest](../../sources/cmmn-1-1-specification.ingest.md)). It keeps four controls apart that the workshop's dimensions also keep apart:

| CMMN control | What it decides | Workshop dimension |
|---|---|---|
| Engine executes the case model's state semantics (sentries, lifecycles) | Whether the model is executed at all | Execution of an operationalized arrangement |
| Task performer type: HumanTask, ProcessTask, DecisionTask | Who or what does each unit of work | Function-level automation |
| ManualActivationRule | Whether enabled work starts by itself or waits for a person | Unattended continuity |
| Discretionary items in PlanningTables, gated by Roles and ApplicabilityRules | Who may select and order work at run time, within a declared catalogue | Decision autonomy |

The mapping gives a non-LLM instance of an operationalized, engine-executed case model with no function-level automation and no decision autonomy for the engine. Executable, automated and autonomous are three predicates here, and the standard sets each independently.

The same knowledge also appears in different forms for different consumers: engine-evaluated rules over the case file, planning tables and filters for the human planner, and tacit knowledge that stays with participants. That is executor-relative operationalization in the standard's own structure.

Where the mapping fails: the standard's executors are human case workers, and its discretion is a declared catalogue, not open judgment. It records no outcome data, so it shows that a two-phase discretion boundary was institutionalized, not that it works. The engine's "execution" is of a state model, not of the knowledge work; the work itself stays with the performers. Transfer to LLM executors holds only for the engine-enforced-state versus judgment split.

### 6.4 Three senses of "operational"

The ingests fix three senses that the KB now uses or touches:

1. **Operationalism** (Bridgman, then Feest and Chang): a concept's meaning given by operations that apply it; in its surviving form, a partial and provisional specification of indicators for a purpose ([operationalism ingest](../../sources/operationalism-sep.ingest.md)).
2. **Operational semantics** (Plotkin): a rule-specified transition relation that gives a language its meaning. It is distinct from an implementation that executes it, and executable rules such as TYPOL's Prolog reading are a further step with their own efficiency problem ([Plotkin ingest](../../sources/plotkin-origins-of-sos.ingest.md)).
3. **`operationalized-from`** (ADR 054): a methodology-to-procedure lineage edge.

None of these is "executed" or "automated". Plotkin keeps specification and execution apart even when the rules run; the operationalism sense names indicators, not steps. The workshop's provisional sense, making K usable for T by E, is a fourth use. If it is ever adopted, the [vocabulary collision ledger](../../reference/vocabulary-collision-ledger.md) must record which sense governs new text. Two further questions fall out and are left open here: which sense the [codification](../../theory/definitions/codification.md) criterion's "unique operational semantics" uses, and whether four surfaces that describe codification as requiring formal semantics overstate a definition that calls formal semantics sufficient but not necessary. A third: the [constraining](../../theory/definitions/constraining.md) definition counts operational definitions as constraining without qualification, while the operationalism source holds that they are partial and cannot show their own validity. All three belong to a separate consistency pass, not to this workshop.

### 6.5 What the cases say about the executor's range of operations

Condition 2 in section 0 asks for a typed range of operations between open judgment and codified steps. The cases bracket it:

- The effective method sits at one end: operations are rule applications with no insight.
- CMMN's engine sits near it: evaluating sentries and rules over a case file.
- CMMN's human planner and Norman's first officer sit at the other end: selecting work from a catalogue, noticing trends and reporting them.
- The LLM executor in the second example table of section 0 sits between: it follows a retained method where one exists and supplies decisions where it does not.

No test here types that middle range. Doing so is the next concrete step for the definition, and it is what the candidate experiment in section 7 would have to log per decision.

## 7. Architectural predictions and proposed discriminating experiments

**P1 — task-relative operationalization does not entail generalization.** With T and its application area fixed, giving E better activation, source access and state can improve successful execution without altering K's domain of applicability. Separately test extending K or redefining the task as T' while preserving E/S. Better T performance is not by itself evidence that K works on T'.

**P2 — method detail can help or harm.** In tasks with late-arriving information, a step-fixed script may do worse than purpose- and bound-guided execution using the same evidence and executor, especially if the pre-fixed path excludes discovery. Compare outcomes and actual evidence encountered, not prompt length alone.

**P3 — methodological incompleteness can coexist with complete computational execution.** An LLM may provide unarticulated method decisions and complete a full bounded task unattended. Log which decisions came from retained method, which from model judgment, and which from symbolic tools; judge quality independently. The test must not quietly exclude human recovery, authorization or approval that was required for completion.

**P4 — automation and decision autonomy diverge.** Replace a human operator with a fixed code path to increase task automation while leaving choice latitude unchanged, and separately delegate method selection to an LLM without automating physical implementation. A metric claiming both interventions are the same progress is defective.

**P5 — autonomy and warrant diverge.** Removing an approval gate can raise computational closure but leave discrimination worse; improving an independent oracle can expand the domain of *warranted* unattended execution. Measure false acceptances and missed exceptions as well as throughput.

**Candidate Commonplace experiment:** define T explicitly, including the application area, acceptance criteria and authority boundaries; select one existing research method and keep the model pinned. Run (a) bare task, (b) relevant methodology cue, (c) cue plus the same method with improved access/state/recovery, and (d) the same support with stronger step constraints. In a **separate generalization experiment**, propose T' with a wider application area and independently check whether K still applies. A second contrast transfers one approval or method-choice function from human to LLM while holding T and evaluation fixed. Log source activation, intervention responsibility, revision fidelity, final correctness, fallback cases, cost and horizon. None of these comparisons has been run here.

## 8. Disposition

1. **Define the application area in task T, not inside operationalization.** Operationalization is the task- and executor-relative transformation that makes K usable for T by E in setting S. Theory → methodology and methodology → skill are possible realizations of this same *task-relative* operation, not two mandatory meanings. Generalizing K or extending T is separate, and any newly discovered T' needs a separately warranted scope claim.
2. **Preserve current Commonplace definitions** of [actionable methodology](../../theory/definitions/actionable-methodology.md), [constraining](../../theory/definitions/constraining.md), [codification](../../theory/definitions/codification.md), and [methodological/computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md); do not create competing 'executability' or 'operationalization' definitions on purely conceptual grounds. Of the five coordinates in the central result, only generality and operational integration name something the existing definitions do not. Situated executability is the actionable relation plus a task success standard; methodological coverage is closure without the settling condition; constraining is already defined.
3. **Treat automation and autonomy separately in future comparisons**: allocate actual task functions to human/computation; separately record discretionary and authorization boundaries, plus which human interventions remain required over the declared horizon. Computational closure is useful for absence of required human decisions, but not a complete proxy for discretionary authority.
4. **Retain the narrower lineage meaning of 'operationalized-from'** as the methodology-to-procedure artifact relation. It is compatible with, but not equivalent to, the proposed task-relative sense. When provenance matters specify the source artifact and kind of transformation; when efficacy matters specify T, E and setting. No ADR change without separate evidence.
5. **Do not infer fully automated LLM work from operationalization alone.** Demonstrate executor capability and function closure under explicit constraints, then separately demonstrate warrant and adequate outcome quality. Lack of a deterministic procedure is not by itself a blocker.
6. **No new machinery or extracted theory definition yet.** This workshop's distinctions are useful for architectural decisions, but causal superiority and the need for additional vocabulary await the scoped tests above.
7. **One extraction is ready without a test.** The claim that a task definition fixes the application area and success criterion, and that operationalization is relative to task, executor and setting, is conceptual and now has a mechanism from Norman (a task written for one executor drops the functions that executor does not consume) and a limiting case from the Church–Turing material. It can go into the library as a short note or as an amendment to the actionable-methodology definition. The rest of this workshop stays here until a test discriminates.
8. **Source status.** Five of seven candidates are ingested. Suchman needs OCR tooling or a text-layer copy. Haynes needs a user-supplied copy. Neither blocks item 7.
