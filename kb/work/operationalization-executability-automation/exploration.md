# Operationalization, executability, and automation — exploration

**Status:** conceptual account, not adopted vocabulary or tested empirical result. Baseline: Commonplace `main` at `d19065b3aef33ffca92fa2f72f5203251fcae3b0`, read on 2026-10-31.

## Answer in brief

Operationalizing guidance, executing it, and automating its application are not stages that must follow in order.

1. **Methodology** supplies intervention-relevant guidance: conditions related to prescriptions, exclusions, rankings, or evaluation criteria. A narrative *about* work may explain why something happened without yet telling an operator which intervention it favors.
2. **Operationalization**, used here descriptively rather than as a new Commonplace technical definition, means arranging representations, access, skills, triggering, control and feedback so a methodology can guide situated activity. It is a process of changing a method's application arrangements, not necessarily its semantics.
3. **Situated executability** is a relation among method or task, executor, operations and tools, target, environment, authority, resources, objective and required performance. Its minimal sense is stronger than merely understanding the instructions: the arrangement can carry out the relevant actions. An observed successful run is evidence only for the observed conditions.
4. **Execution** is an event or trace: an actor actually carries out work. Executing the *task* successfully does not prove fidelity to a *specified methodology*, and following a methodology faithfully does not prove an adequate outcome.
5. **Automation** assigns one or more formerly manually performed functions to computation in the configured process. It may rely on deterministic code, LLM judgment, or both, and may leave judgments and authorizations to people. State its functional boundary, not just a claim of 'automated'.
6. **Autonomy** concerns required human intervention and delegated decision authority over the assessed boundary and horizon. Commonplace already has the precise narrower measure **computational closure** for absence of run-time human production decisions. Neither it nor autonomy establishes capability or warrant.

The central independence claim: a system can improve its ability to *apply* guidance without making that guidance more formal, more deterministic, or more restrictive. Conversely, it can codify a small step without automating the enclosing work.

## Existing Commonplace concepts that already do the work

- [Actionable methodology](../../theory/definitions/actionable-methodology.md) explicitly defines a relation between methodology, operator, available operations, target, and setting. Actionability concerns intervention selection; completing the work may require additional execution capabilities and feedback.
- [Methodological and computational closure](../../theory/methodological-and-computational-closure-track-different-changes.md) separates decisions settled by retained methodology from decisions supplied computationally. It gives all four combinations, including human execution of a settled checklist and an unsupervised model using judgment unarticulated in the method.
- [Methodology governs its own extension only where it settles decisions](../../theory/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) prevents attributing a capable actor's extra judgments to a complete methodology.
- [Constraining](../../theory/definitions/constraining.md) narrows or ranks a named consumer's permissible readings, including activation and response. [Codification](../../theory/definitions/codification.md) is its symbolic, fixed-operational-semantics region. Neither defines all ways of making a method usable.
- [Methodology enforcement](../../theory/methodology-enforcement-is-constraining.md) separates activation from response; a skill, hook or script has no inherent rank without examining both.
- [Skills derive from methodology](../../theory/skills-derive-from-methodology.md) captures same-medium reworking into an execution-oriented form without claiming symbolic codification.
- [Methodology selection](../../theory/capable-agents-need-methodology-selection.md), [weight-resident activation](../../theory/weight-resident-methodologies-compress-behavior-in-context.md), [behavioral authority](../../theory/definitions/behavioral-authority.md), and [contextual activation](../../theory/knowledge-storage-does-not-imply-contextual-activation.md) show why knowledge availability, discovery, binding force and actual use are separate.
- [Fix what the executor cannot determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) already explains why more step detail can make action worse: the executor often has evidence the author lacked.
- [Bounded-context orchestration](../../theory/bounded-context-orchestration-model.md) separates state/scheduling from individual model calls only under explicit closed-world and barrier conditions. It does not supply a universal execution model for open environments.
- [Warranted autonomy](../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md) and [tool usefulness, autonomy, warrant and power](../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) prevent mistaking unattended activity for a trustworthy or capable system.

**Vocabulary collision:** [ADR 054](../../reference/adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) adopts `operationalized-from` as a particular source-to-procedure lineage relation: a judgment-shaped procedure adds ordering, defaults, or stopping conditions to methodology, without novel substantive claims. This is useful and narrower than 'making a method operative' by, for example, granting access, routing an existing instruction, improving feedback, or training an operator. A broad definition must not overwrite the lineage test.

## 1. Description, methodology, and operational support

A description of past work says what happened. An explanatory theory may say why. A methodology, even an incomplete one, must discriminate between candidate interventions in some represented conditions. 'Consider alternatives whose rejection would change the decision' can guide activity without describing a fixed list of actions. Conversely, 'write a great report' is primarily a goal, not enough by itself to identify an intervention rule, although a capable actor can invent or import one.

A method does not become a method only when it is exhaustively specified. A skilled operator's tacit capabilities can supply operations, diagnosis, ordering and local judgment. To move it into an unfamiliar setting or to a weaker executor, one may need to supply some or all of:

- **Applicability and activation:** which kinds of problems call for this method and how the executor encounters it.
- **Authority and purpose:** the intended objective, binding constraints, who may decide what, and what may not be delegated.
- **State and resources:** inputs, tools, access, permissions, environmental observations and stable work records.
- **Control and adaptation:** selection of next moves, ordering when dependencies matter, exceptions, retries, fallback, stopping, and escalation.
- **Evidence and evaluation:** what would distinguish promising progress, failure, a wrong assumption, or completion.
- **Provenance and revision:** why an instruction exists, when to return to source theory, and how discoveries change later application.

This is a *diagnostic catalogue*, not a necessary checklist for every method. A single cue can be sufficient when the executor already knows the convention. Adding a step may improve one actor's performance and degrade another's. That is why actionability and executability must be actor- and setting-relative.

A rough relational question is: given guidance M, executor E, supported operations O, state/environment S, authority A, objective G and threshold Q, can the configured arrangement carry out relevant actions, with adequate results in the intended domain? Q matters: one feasible instance, reliable performance on a distribution, and indefinite autonomous operation are three different claims. The relation cannot in general be calculated from text alone.

## 2. Formalization, codification, and execution are different

**Pencil-and-paper long division.** A schoolchild follows a mechanical positional algorithm with pencil and paper. Its instructions can be precise and algorithmic without a computer. It is executable by a suitable human and can later be automated by a machine, without changing the underlying algorithm. Turing's classical 'effective procedure' was modeled on human symbol-manipulation; it requires exact finite instructions that do not demand ingenuity, not a digital computer. This is a special mathematical sense of effective procedure, not a definition of all executable knowledge work.

**A human-run checklist.** A clinical team can operationalize a safety practice by timing prompts and assigning roles while people continue doing and deciding. The WHO surgical checklist study reported improved outcomes after its introduction, but the intervention included communication and workflow changes; the result does not isolate prose detail, and it is no example of complete task automation.

**A model following a research skill.** An LLM may choose sources, criticize a hypothesis, and revise a note under natural-language instructions, choosing unanticipated actions. This can be computational execution of a method whose response semantics are not codified. Whether it actually followed that method and produced good research must be assessed separately.

**A script that calculates a statistic.** A program can codify and automate arithmetic while leaving source selection, study design, interpretation and publication to a human. The local success cannot be credited as automation of research.

**A multi-step agent workflow.** A symbolic scheduler may reliably advance checkpoints and invoke LLM calls. Its control logic can be codified while substantive judgments remain interpreted and possibly unwarranted; conversely, a capable model can determine the next research move without a predeclared workflow.

**A human-approved agent.** Drafting and checking are automated functions; approval remains human. The bounded production path is mixed, not computationally closed end-to-end. This does not make 'partially automated' false. A human requirement supplied before the run is a seed, not automatically a run-time human production decision; a human repair decision required after every failure is.

The terms differ by field. In computer science, **operational semantics** gives a programming language meaning by rules describing computation, not the broader process of making any methodology actionable. In philosophy of science, **operationalism** concerns how concepts relate to measurement or operations, not how a workflow is deployed. In business-process modeling, descriptive maps and executable models serve distinct purposes; adaptive case management explicitly accommodates unpredictable ordering and judgment.

## 3. Counterexamples to tempting implications

| Proposed implication | Counterexample | What failed |
|---|---|---|
| 'More detailed guidance → more executable' | A fixed web-research plan forbids an agent from following new evidence; extra instructions use scarce context and exclude the better route. | Detail can freeze bad assumptions, obscure purpose, or exhaust the executor. |
| 'Executability is intrinsic to a document' | An exact validator procedure is usable with repo access, impossible for the same actor without read permissions. | Executor, tools, authority and setting are missing. |
| 'Operationalizing means constraining' | Give the executor access to sources, a checkpoint, and a feedback path, leaving the permitted intellectual approaches unchanged. | Practical capability changes without necessarily narrowing interpretation space. |
| 'Operationalizing means adding a procedure' | A model already knows a standard method; a short cue activates the method when relevant. | Triggering can dominate restating procedural content. |
| 'Codification automates the task' | A deterministic Markdown linter checks headings while a person still judges whether the argument works. | The unit of automation is too narrow. |
| 'Automation requires codification' | An agent produces a research synthesis without human decisions, guided by interpreted natural language. | Computational production is possible without fixed symbolic response semantics. |
| 'Unattended execution implies methodological closure' | A model selects an unanticipated criticism strategy not settled by the retained method. | The model's repertoire supplies consequential decisions. |
| 'An executed method is reliable' | One successful run fails on new source types, or only succeeds with hidden human correction. | No distributional or independence evidence. |
| 'Method fidelity implies success' | The agent follows a bad checklist perfectly and reaches the wrong conclusion. | Spec compliance and objective satisfaction differ. |
| 'Automation implies autonomy of the whole system' | Software generates a patch; a human decides which repair to apply and whether it may merge. | Internal decisions and authorizations remain human. |
| 'More autonomy implies useful capability' | Removing the reviewer makes a bad model run continuously. | Closure is an allocation property, not a quality guarantee. |

There are also converse counterexamples: highly capable human craftsmanship with little retained procedure, and completely specified formal methods lacking the resources to be executed. These indicate that neither a strict progression nor a single scale will classify the space.

## 4. What 'progress' can mean without progressively narrowing the method

The important design variables are not all locations on a constraining ladder. They include:

| Architectural change | Primary effect | Does **not** imply |
|---|---|---|
| Route the right method to a task, possibly via a compact cue | More reliable activation and method selection | More exhaustive method text |
| Supply tools, source access, permissions and an explicit target | Greater situated actionability/executability | Narrower permitted interpretations |
| Externalize checkpoints and relevant state | Longer-horizon continuity and inspectability | A complete symbolic workflow |
| Give a worker intent, authority bounds and situational feedback | Better-founded local adaptation | A fixed choice of means |
| Add examples and exception/fallback paths | Broader recognized coverage, more recoverable failures | Fewer admissible intellectual methods |
| Split mechanical work into deterministic checks | Cheaper, more repeatable local operations | Automation of the encompassing epistemic judgment |
| Transfer a previously human decision to a model | Greater computational closure within the chosen boundary | Competence, reliability or warrant |
| Improve the discriminating oracle and escalation criterion | Potentially wider **warranted** unattended domain | Better generation by itself |

Some of these changes *also* constrain. Routing may settle which method governs; a permission boundary rules out actions; a schema fixes local acceptance. The claim is not 'zero constraints are ever added'. It is that **increasing operational reach does not require monotonically reducing discretion over substantive methods**. Indeed broader competence may make more approaches viable. Constrain where a stable invariant, safety/authority boundary or necessary shared convention justifies it; retain discretion where execution can gather evidence that the author lacked.

A failure-oriented way to decide what to change first:

- Right method unknown or not activated → search, route or cue.
- Method available but cannot be acted on → supply tools, inputs, access and permissions.
- Work drifts across time → retained state, checkpoints, context budgeting and recovery.
- Same local mechanical error recurs → consider symbolic codification.
- Choices made prematurely → expose objective and constraints, defer to live evidence.
- Outputs untrustworthy → independent outcome tests, evaluators and escalation.
- Human still selects or authorizes consequential internal decisions → name that function and test a bounded computational transfer; do not relabel all prior work 'unautomated'.

This diagnosis predicts that Commonplace can grow in capability and reliability through better *activation, support, control and feedback*, even if the volume of step-by-step instructions remains stable or decreases. It also predicts that transferring a human gate without improving its oracle can raise autonomy while reducing usefulness.

## 5. Literature and its limited transfer

1. **Wielinga, Akkermans & Schreiber (1998),** [A competence theory approach to problem solving method construction](https://doi.org/10.1006/ijhc.1998.0209). Their framework distinguishes required competence, conceptual refinement and operational control choices. It demonstrates that making a problem-solving method operational introduces decisions about inference and control; operationalization can sacrifice coverage. Commonplace already [ingested and qualified this source](../../sources/competence-theory-problem-solving-method-construction.ingest.md). Its formal knowledge-engineering setting does not establish a universal scheme for open-ended natural-language agents.
2. **Turing/effective procedures,** [SEP on the Church–Turing thesis](https://plato.stanford.edu/entries/church-turing/) and [Turing](https://plato.stanford.edu/entries/turing/). Classical algorithms are defined through idealized human symbol work. This is the clean control case against identifying execution with electronic automation, but their no-ingenuity premise cannot classify judgment-rich methodologies.
3. **Plotkin (1981) and later historical account,** [Origins of structural operational semantics](https://doi.org/10.1016/j.jlap.2004.03.009). Programming-language operational semantics fixes transition behavior. This gives a sound analogy for Commonplace's *codification* but not a general definition of operationalizing any human procedure.
4. **Bridgman and critics,** [SEP: Operationalism](https://plato.stanford.edu/entries/operationalism/). Measurement-operational definitions must not be equated with a method's operational deployment. The strong thesis that a concept means only its measurement operations is widely contested.
5. **Lucy Suchman,** [Plans and Situated Actions](https://www.cambridge.org/core/books/abs/humanmachine-reconfigurations/situated-actions/F4AA82303887FF0875BD656977661875) and [Plans](https://www.cambridge.org/core/books/abs/humanmachine-reconfigurations/plans/486980BE0B03AE3DF9C2181D74F26E64). Plans support situated action, rather than fully determining it. This explains the importance of executor competence and feedback; it does not prove that procedures never improve reliability.
6. **Parasuraman, Sheridan & Wickens (2000),** [Types and levels of human interaction with automation](https://pubmed.ncbi.nlm.nih.gov/11760769/). They separate acquisition, analysis, decision/action selection and implementation, each automatable to different degrees. Use function-level allocation, not a universal automation score.
7. **Bainbridge (1983),** [Ironies of automation](https://doi.org/10.1016/0005-1098(83)90046-8), and **Norman (1990),** [The problem with automation is inappropriate feedback and interaction](https://pubmed.ncbi.nlm.nih.gov/1970904/). Partial automation can transfer the most difficult exceptions to humans who have less situational awareness. Recovery design, not just normal-path automation, is consequential.
8. **OMG,** [Case Management Model and Notation](https://www.omg.org/cmmn/index.htm). Adaptive case management models knowledge work whose activity order cannot be fully prescribed. It illustrates that representing work and supporting its execution can preserve discretion rather than force a fixed sequence.
9. **Haynes et al. (2009),** [Surgical safety checklist](https://pubmed.ncbi.nlm.nih.gov/19144931/). A checklist can change human-executed practice and correlate with better outcomes without converting the encompassing operation to software. Before/after evidence does not identify which component of implementation caused improvement.

These sources motivate the distinctions by mechanisms and counterexamples, rather than directly validating Commonplace's proposed vocabulary or comparative performance.

## 6. Architectural disposition

**Keep the current technical definitions.** 'Actionable methodology' already covers the operator-relative relation. 'Methodological closure', 'computational closure', 'constraining', 'codification', and 'behavioral authority' resolve different ambiguities without another overlapping term. The adopted `operationalized-from` relation has a valid narrower lineage test and should remain untouched.

**Use 'operationalization' only as an explicitly scoped umbrella in this exploration:** work that makes method-guided action possible or practical for a named executor and situation. Do not list it in the active vocabulary, and do not infer an `operationalized-from` link merely because tools, routing, access or workflow state improved. Ordinary-language 'making a method operative' is less likely to be mistaken for a formal lineage relation.

**Do not add a new definition of 'executability' yet.** It can be discussed as a situated capability relation, partly overlapping actionability but extending from choice to actual performance. A definition earns its place when an architectural or evaluation decision needs to distinguish it from actionability and from computational closure. We have conceptual examples, not such a recurring unresolved decision.

**Preserve and tighten one already-supported rule for future comparisons:** declare the *task and objective, executor, environment and permissions, behavioral consumption path, functional boundary, horizon, human interventions, and outcome evidence*. State method fidelity and task success separately. For a progress claim, name the changed failure mechanism, not 'more operational' as a catch-all metric. This is a synthesis of existing Commonplace doctrine, not a proposed new mandatory schema.

## 7. Predictions and potential falsifiers

- **Routing hypothesis:** for methods a model already knows, explicit task-to-method cues can improve appropriate method application without detailed procedural additions. Falsifier: controlled target-model trials show cue-only routing does not alter relevant decisions, or imports the wrong method more often.
- **Support hypothesis:** adding source access, persistent state or recovery paths can raise completion probability with the same substantive natural-language instruction. Falsifier: ablation trials show no effect after holding difficulty and resource budgets fixed.
- **Over-specification hypothesis:** forcing premature means can reduce performance on tasks whose decisive evidence arrives later. Falsifier: fixed detailed plans outperform flexible intent-framed execution on representative shifted cases under equivalent budgets.
- **Automation attribution hypothesis:** a system that automates source processing but needs human methodological selection will show an unreduced human decision burden on the enclosing research task. Falsifier: allocation traces show method selection was in fact computationally supplied, without concealed intervention.
- **Warrant hypothesis:** moving an acceptance gate to a model can increase unattended throughput without improving warranted acceptance on hard cases. Falsifier: a stronger external or independent oracle discriminates failures in that tested domain.

These are proposed tests, **not outcomes of experiments**. The current investigation supports the conceptual separation and the decision not to multiply definitions. It does not establish that one architecture will outperform another.

## Immediate next research decision

Select one existing Commonplace method (for example source ingestion, claim criticism, or a multi-artifact review) and evaluate four configurations against an independently assessed task set: bare objective; explicit methodology cue; same cue plus access/state/recovery; same support with much more prescribed step detail. Record intervention counts, fidelity, task outcomes, cost, and exception handling separately. A second test should transfer just one human judgment to an LLM while keeping the rest of the boundary fixed. Only repeatable evidence would warrant promoting an architectural claim beyond this workshop.
