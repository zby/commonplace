# Operationalization, executability, automation, and autonomy — revised exploration

**Status:** a workshop investigation, not adopted technical vocabulary, empirical proof, or a system change. **Revision:** 2026-10-31, responding to the operator's objections that the first account confused generalization with operationalization, treated automation and autonomy too similarly, and did not check source ingestability. Repository starting point: main at d19065b3aef33ffca92fa2f72f5203251fcae3b0. Literature access was checked on 2026-10-31.

## Central result

**Operationalization is relative to an executor, task and operating setting.** It is not an intrinsic property of an artifact: what a trained researcher can use immediately may need adaptation for a novice, an LLM agent, or a deterministic interpreter. Every claim that something is operational must say **operational for whom, to do what, with which capabilities, resources and authority, and to what standard**.

There are more than two possible transformations of a methodology; moreover, properties of the methodology must not be confused with properties of an executor, its runtime, or a particular execution.

**Generality:** which cases the method can guide adequately.

**Constraining:** which readings, choices, or responses the method permits or prefers for a named consumer.

**Methodological coverage (or operational completeness):** which consequential tasks and decisions *in applying* the method have some usable guidance, including how to recognize its applicability, obtain information, choose the next operation, deal with exceptions, and stop. Guidance can specify a decision interface or an approach for obtaining evidence without settling its answer. It is not necessary for every choice to have a fixed answer. Methodological closure, already defined in Commonplace, is stronger: it concerns whether the retained method settles consequential decisions, not merely whether it supplies useful guidance for them.

**Operational integration:** whether guidance reaches the relevant executor at the relevant time, with the requisite tools, state, permissions, feedback, invocation and binding authority. Integration changes *the configured system*; it need not alter the methodology's content or range of validity.

**Situated executability:** whether the specified executor and environment can actually perform the required work to an identified standard. This is a relation, not a textual genre and not a single successful trace.

These are diagnostic coordinates rather than scalar scores or a complete axiomatization. Their separation does not assert statistical independence: improving one may alter another. In particular, adding a correct applicability constraint may increase reliable coverage; a bad constraint may destroy generality; and operational integration may extend the system's *practical reach* without extending the method's *principled domain*. Distinguish intended domain, valid applicability, and empirically successful coverage.

**Operationalization** is best kept provisional as a *source-to-use transformation, assessed relative to a target executor*. There is a real double use: a methodology can make a theory prescriptive for a class of practitioners, while an executor-specific procedure may make that methodology usable for a different actor. These are not the same relation or mandatory successive steps. Simply granting tools, delivering instructions, or preserving runtime state improves *operative integration* without necessarily deriving a new methodological artifact. Merely generalizing a theory is likewise not automatically operationalization.

This proposal leaves open a narrower, defensible reading of operationalization as *producing a procedure from broader methodology*. Commonplace already makes that specific lineage commitment in [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md): 'operationalized-from' is a method-to-procedure relation adding ordering, defaults or stopping conditions not fixed by its source. Do not redefine that identifier to mean any improvement in usability or integration.

## 0. What is being operationalized, and for which executor?

The statements **'a methodology operationalizes a theory'** and **'a skill operationalizes a methodology'** can both be meaningful, but conflating them hides their different sources and target consumers.

| Transformation | Source | Result | What is claimed |
|---|---|---|---|
| **Theory → methodology** | Explanatory/general theory | Prescriptive principles, intervention criteria or strategy for an intended class of actors | Theory is worked into guidance for action, without proving usability for every actor |
| **Methodology → procedure for E** | Existing intervention-guiding methodology | A checklist, skill, decision interface or other E-facing procedure | Guidance has been adapted for a particular executor, task and assumed background competence |
| **Method/procedure → integrated runtime use** | Existing guidance | Routing, permissions, tools, context, state and feedback in an operating arrangement | The guidance is actually available for use by E; no source-to-procedure derivation is necessarily involved |
| **Method plus E → execution** | Guidance and configured executor | Observable actions and outcomes | The work happened, not that the method is complete, correct, or reliably followed |

When provenance matters, call the first **prescriptive derivation from theory**, the second **executor-specific procedure adaptation**, and the third **operational integration**. Reserve the broad word 'operationalization' for uses that identify their source, target, executor and application.

**Methodology is not definitionally 'operationalized theory'.** The existing [actionable-methodology definition](../../theory/definitions/actionable-methodology.md) identifies methodology by its intervention-guiding function. A methodology may indeed be worked out from an explanatory theory, but it may also contain practical conventions or organizing principles that are not derived from a single theory. The [two-layer execution account](../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) explicitly distinguishes the theory-derived part of a methodology from methodology-native content. The phrase is a possible provenance claim, not an identity.

The operation is **executor-relative** in both stages, although the first stage may assume a broad practitioner class rather than one named model. A skilled researcher may use a Popperian criticism methodology without a derived checklist. An LLM may need a short method-selection cue and source access; another may need detailed instructions and a persistent context; a weak model may still be unable to perform reliable criticism no matter how explicit the instructions become. An artifact can satisfy a source-to-procedure lineage description but fail to be operational **for its intended E**. Conversely, an unchanged methodology may already be operational for E, so there is no compulsory infinite regress of ever-finer operationalizations.

The adopted [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) uses `operationalized-from` only for a narrow **methodology-to-procedure artifact-lineage relation**, involving added ordering, defaults or stopping conditions. That relation does not by itself demonstrate executor-relative executability. Do not broaden this registered identifier merely because its ordinary-English root also describes theory-to-method derivation or runtime integration.

**Test for any proposed operationalization:** identify the source guidance, resulting representation or operating arrangement, E's already available competence, target task, environment, action possibilities and adequacy criterion. Then ask which decisions E can now make or actions E can carry out that were not feasible before. If the only change is an improved theory, the result may be generalization rather than operationalization. If the only change is tool access, it may be operational integration rather than a new methodology. If E still cannot apply the procedure, calling it operationalized should remain a hypothesis, not a finding.

## 1. From descriptions to situated action

A *description* reports how work occurred; an explanatory theory proposes why. A *methodology* supplies an intervention-relevant mapping: which kind of action, comparison, rejection, or evaluation is favored in represented conditions. An instruction like 'critically assess the causal claim' can be a thin method when a proficient actor reconstructs appropriate tests; it is not an exhaustive plan.

To make guidance usable, inspect the specific gap instead of assuming that more detailed steps are the missing ingredient:

| Potential gap | Candidate intervention | Property principally affected |
|---|---|---|
| The method applies to too few classes of situation | Extend or revise its intervention principles | Generality |
| Multiple plausible interpretations cause wrong choices | Add purpose, disambiguation, exclusions or examples | Constraining |
| The methodology does not address how to handle missing evidence or exceptions | Add decision criteria, evidence-gathering, fallback or stop rules | Methodological coverage |
| The model knows the method but does not select it | Select/routinely activate a coherent method, perhaps via a short cue | Activation, not necessarily more content |
| The operator cannot access the target or tools | Provide resources, permissions or a different execution channel | Situated executability, not theory generality |
| Work loses its position across context windows | Retain state, recover checkpoints, arrange subsequent calls | Operational integration and horizon |
| A deterministic check is cheap and stable | Commit the local predicate to code | Codification, local reliability |
| The evaluator cannot tell when the work is wrong | Improve evidence, testing, oracle discrimination and recovery | Warrant of outcomes |
| A person still performs an internal function | Transfer the specific function to computation | Automation coverage |
| The agent has no authority to choose a method or initiate a branch | Deliberately delegate authority and specify bounds | Decision autonomy; perhaps greater unattended scope |

A methodology with excellent generality might be unavailable at the point of need. An extensively integrated procedure might be narrowly applicable. A capable executor may perform judgments never prescribed by the method. These cases falsify a one-directional scale of 'more operational'.

**No necessary monotonicity:** additional operational guidance may lower performance by prescribing a method before relevant evidence appears, forcing premature stopping, overloading context, or requiring a model to resolve contradictory constraints. Commonplace's [author–executor determinability rule](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) addresses this precise risk. A stronger artifact may fix governing intent and leave more means open; this combines stronger *appropriate* constraints with more contingent freedom.

## 2. Executability and the actor-relative boundary

For a method M, task T, executor E, available operations O, target/environment S, delegated authority A, objective G, time/resource horizon H, and performance criterion Q, the useful question is: can that arrangement execute the task using M adequately over a specified class of cases? There is no reason the answer must be invariant between a trained human, weaker LLM, stronger LLM or code engine.

Three levels of evidence differ:

1. **Can be attempted:** the actor can interpret the method and has a way to act. Commonplace's existing [actionable methodology](../../theory/definitions/actionable-methodology.md) principally captures whether its prescription can affect intervention selection.
2. **Can complete a specified task:** the actor has the necessary operations, state, competence, permission and control to reach an outcome in a declared setting.
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

The earlier chain 'knowledge → selection → execution → evaluation → retention' confused logical functions with a developmental trajectory. All those functions may exist even for a human paper-and-pencil system; the architecture can change any one of them, in different directions.

A better analytical map is:

| Layer of question | Variable | Example of progress without codifying more |
|---|---|---|
| Method itself | Generality/coverage across situations | Extend criticism method to handle adversarial evidence |
| Method itself | Semantic commitments/constraints | Preserve binding provenance but leave evidence-gathering tactics open |
| Method itself | How much application logic is addressed/settled | Add a way to seek discriminating evidence, without preselecting its outcome |
| Source-to-method transformation | Deriving prescriptions from a theory for an intended practitioner class | Turn an epistemic principle into a strategy for criticizing claims |
| Executor-facing adaptation | Working the method into a form E can use for a declared task | Derive an LLM skill, or avoid it where the method is already usable |
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
| Norman (1989/1990), [NASA-hosted original version](https://ntrs.nasa.gov/api/citations/19900004678/downloads/19900004678.pdf) | Automation feedback/exception boundary | No matching ingest in targeted searches | Full NASA report PDF available; journal reprint record has no downloadable PDF | Priority new ingest candidate; identify the NASA version, not silently the journal's different publication |
| Suchman (1987), [Plans and Situated Actions](https://course.khoury.northeastern.edu/cs5100f12/resources/reading/suchman-situatedactions.pdf) | Plan ≠ full determination of situated activity | No matching ingest in targeted searches | Full 1987 book PDF surfaced at university course URL; Cambridge revised edition is access-controlled | Candidate, but check the version and usage rights; avoid equating original and revised editions |
| Church–Turing history, [SEP entry](https://plato.stanford.edu/entries/church-turing/) | Pencil-and-paper effective methods vs broad judgment-laden execution | No matching ingest in targeted searches | Public full HTML article | Ingest only if needed; remember SEP is secondary scholarship rather than Turing's original text |
| Operationalism, [SEP entry](https://plato.stanford.edu/entries/operationalism/) | Operational definitions/measurements differ from making a methodology usable | No matching ingest in targeted searches | Public full HTML article | Optional disambiguation source, not direct authority for Commonplace vocabulary |
| Plotkin (2004), [origins of SOS](https://citeseerx.ist.psu.edu/document?doi=061229419ca3f09567d6bf6c8cd5c6ff3b94a3e6&repid=rep1&type=pdf) | Operational semantics is formal rule-based execution, not general operationalization | No matching ingest in targeted searches | Full paper PDF surfaced from CiteSeerX; publisher page only reliably exposes abstract | Candidate if conceptual distinction proves load-bearing |
| OMG, [CMMN 1.1 specification](https://www.omg.org/spec/CMMN/1.1/) | Model unpredictable knowledge-worker activity with retained discretion | No matching ingest in targeted searches | Official specification page exposes normative PDF | Candidate, but avoid assuming a graphical case model executes itself or automates the work |
| Haynes et al. (2009), [surgical checklist](https://www.nejm.org/doi/full/10.1056/NEJMsa0810119) | Human operationalization without task automation | No matching ingest in targeted searches | Publisher marks free article and exposes full-text HTML | Optional empirical example; before-after outcomes do not isolate checklist wording from implementation |

The sources' meanings do not transfer unchanged: *operational semantics* fixes rules in programming-language theory; *operationalism* addresses measurement and scientific concept meaning; *operational method construction* in knowledge engineering moves toward a task-specific executable control strategy; *automation levels* in human factors classify allocations and interaction. None licenses a universal equation 'operationalize = formalize = automate'.

**Highest-value next ingests**, if separately commissioned: Norman (directly bears on the transition from automatic normal-path work to recovery), Suchman (situated autonomy versus fixed plans), and possibly the OMG specification (formal representation without fixed activity order). Plotkin, the SEP entries, and Haynes are lower-priority contrasts. Existing three reports should be reused. Public retrieval does **not** establish a copyright license for committing a full source; the normal Commonplace ignored-snapshot/checksum discipline still applies.

## 6. Architectural predictions and proposed discriminating experiments

**P1 — generality and integration separate.** For an unchanged methodology, enabling source access, activation and persistent state can increase *situated task success* without expanding the principled set of cases to which the method applies. Test by fixing source-method content while varying the environment; then separately test a revised method on unchanged resources. Failure to separate would be evidence of interaction, not semantic identity.

**P2 — method detail can help or harm.** In tasks with late-arriving information, a step-fixed script may do worse than purpose- and bound-guided execution using the same evidence and executor, especially if the pre-fixed path excludes discovery. Compare outcomes and actual evidence encountered, not prompt length alone.

**P3 — methodological incompleteness can coexist with complete computational execution.** An LLM may provide unarticulated method decisions and complete a full bounded task unattended. Log which decisions came from retained method, which from model judgment, and which from symbolic tools; judge quality independently. The test must not quietly exclude human recovery, authorization or approval that was required for completion.

**P4 — automation and decision autonomy diverge.** Replace a human operator with a fixed code path to increase task automation while leaving choice latitude unchanged, and separately delegate method selection to an LLM without automating physical implementation. A metric claiming both interventions are the same progress is defective.

**P5 — autonomy and warrant diverge.** Removing an approval gate can raise computational closure but leave discrimination worse; improving an independent oracle can expand the domain of *warranted* unattended execution. Measure false acceptances and missed exceptions as well as throughput.

**Candidate Commonplace experiment:** select one existing research skill and keep the task family, acceptance criteria and model pinned. Run (a) bare goal, (b) relevant methodology cue, (c) cue plus identical method with improved access/state/recovery, (d) same support with stronger step constraints, and (e) a modified broader-coverage methodology under fixed support. A second contrast transfers one approval or method-choice function from human to LLM while holding task boundaries and evaluation fixed. Log source activation, intervention responsibility, revision fidelity, final correctness, fallback cases, cost and horizon. None of these comparisons has been run here.

## 7. Disposition

1. **Revise the conceptual account in the workshop** (this note). The earlier two-pole generality-versus-constraint reading was incomplete. Operationalization is **executor- and task-relative**, and its two source transformations (theory → methodology; methodology → executor-specific procedure) are not interchangeable. It is not a third scalar dimension.
2. **Preserve current Commonplace definitions** of [actionable methodology](../../theory/definitions/actionable-methodology.md), [constraining](../../theory/definitions/constraining.md), [codification](../../theory/definitions/codification.md), and [methodological/computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md); do not create competing 'executability' or 'operationalization' definitions on purely conceptual grounds.
3. **Treat automation and autonomy separately in future comparisons**: allocate actual task functions to human/computation; separately record discretionary and authorization boundaries, plus which human interventions remain required over the declared horizon. Computational closure is useful for absence of required human decisions, but not a complete proxy for discretionary authority.
4. **Retain the narrower lineage meaning of 'operationalized-from'**. Do not treat it as proof of operator-relative actionability or as the name for theory-to-method derivation. When ambiguity matters, say 'prescriptive derivation', 'executor-specific procedure adaptation' or 'runtime integration'. Revising ADR 054 needs its own justification.
5. **Do not infer fully automated LLM work from operationalization alone.** Demonstrate executor capability and function closure under explicit constraints, then separately demonstrate warrant and adequate outcome quality. Lack of a deterministic procedure is not by itself a blocker.
6. **No new machinery or extracted theory definition yet.** This workshop's distinctions are useful for architectural decisions, but causal superiority and the need for additional vocabulary await the scoped tests above.
