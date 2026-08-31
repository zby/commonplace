# Conceptual spine

This is the dependency ledger for the re-foundation. It separates what each
stage assumes, what it concludes, and what would defeat the inference. The
labels are provisional; the causal descriptions are load-bearing.

## Dependency map

| Stage | Additional premise | Derived claim | Not yet established |
|---|---|---|---|
| 1. Agentic system | Work is performed through bounded LLM calls plus persistent software machinery that stores state and mediates effects across calls. | The model call is not the whole behavior-producing system; consequential functions can live in software. | The software need not be generated, mutable, learning, or universal. |
| 2. Extensible production machinery | The task family is broad enough that predefining every useful schema, workflow, decomposition, validator, algorithm, representation, tool, and coordination structure is practically unrealistic; the agent can construct some of this machinery. | The system can function as an extensible software factory for its own work. | This is not true of every agentic system and does not rule out a fixed universal substrate in principle. |
| 3. Continual learning | Experience on earlier tasks persistently changes how later tasks are solved. | The learning surface may include software machinery as well as weights and memories. | The change need not be an improvement, reflective, autonomous, or computationally closed. |
| 4. Learning software factory | Earlier experience changes retained production machinery and later work depends on that change. | The factory itself learns in the cross-task sense; decompositions, evaluators, context strategies, representations, tools, search procedures, and coordination structures become learnable machinery. | One retained change does not establish compounding, broad reach, or repeated self-improvement. |
| 5. Recursive or reflective factory | Constructing the machinery needed for a task is itself a difficult task; retained machinery can affect how later machinery is constructed. A causally connected self-representation is additionally present when reflection is claimed. | A factory-building-factory relation emerges, and some paths may be reflective with respect to represented machinery. | Factory-valued output alone is not recursion in operation; recursion alone is not reflection; reflection alone is not improvement. |
| 6. Learning-mechanism comparison | More than one mechanism can turn experience into operative changes. | Trial and error, trajectory reuse, program search, learned policies, optimization, theory mediation, and mixtures are live candidates. | No ordering, exhaustiveness, or winner follows from the list. |
| 7. Theory-mediation proposal | Natural-language theory can jointly represent task structure, solver limits, failure explanations, interventions, and evidence, and an LLM can interpret it into heterogeneous software changes. | Theory mediation may be a particularly versatile learning mechanism for the factory. | Necessity, sufficiency, universal superiority, and general learning remain unestablished. |

## Stage 1: bounded calls plus persistent software

The minimum claim is architectural, not ontological. A deployed agentic system
uses one or more bounded model calls while software outside those calls carries
some consequential state or effect path. The machinery can include prompt and
context assembly, scheduling, memory access, tool dispatch, permissions,
execution, validation, recovery, and retention.

The [bounded-context orchestration
model](../../notes/bounded-context-orchestration-model.md) is one useful form
when transition state is explicit and inter-call execution is symbolic. The
more general starting claim should not inherit all of that form's closed-world,
barrier, or scheduler conditions. The
[scheduler–LLM separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
supports why exact state transitions often belong in software rather than
accumulated model context. It still leaves the placement boundary empirical and
revisable.

Required supporting-note job: state the minimal system boundary and explain why
software machinery is behavior-producing rather than inert infrastructure.

Counterexamples and limits:

- A single stateless model call still has serving software, but it may not have
  the persistent cross-call machinery relevant to this program.
- An LLM-mediated scheduler keeps some progression in conversation; this weakens
  the clean separation without erasing the surrounding software substrate.
- A perfect fixed substrate would satisfy the starting architecture. The later
  extensibility claim needs an independent practical premise.

## Stage 2: practical generality creates a factory role

The new premise concerns breadth. Across a sufficiently broad family of tasks,
the useful production machinery is not known exhaustively in advance. Different
tasks may reward different decompositions, data representations, checks,
searches, algorithms, tools, context policies, or coordination structures. If
the agent constructs some of these and uses them to perform its work, the
system has taken on a software-factory role.

The claim is deliberately weaker than an impossibility theorem. A fixed
universal substrate could in principle interpret or generate every needed
program. The practical conjecture is that supplying all task-appropriate
machinery extensionally in advance is unrealistic, while constructing it from
task evidence is useful for broad enough demand families.

Required supporting-note job: state the breadth condition and distinguish a
target work product from software that organizes or performs the production
process. Such machinery may be task-local at this stage. Later cross-task use
belongs to the learning-factory inference rather than to the factory premise.

Terminology question: the in-flight Greenfield-style definition of [software
factory](../../notes/definitions/software-factory.md) requires a declared
product family and lifecycle machinery. That may supply useful distinctions,
but the general derivation must be established first. It should not turn a
broad agentic architecture claim into a software-product-line claim merely to
inherit the word *factory*.

Counterexamples and limits:

- A fixed tool loop over a narrow task family is an agentic system without the
  extensible factory role.
- Generating a one-off answer or target program is product work, not evidence
  that production machinery was constructed. A task-local generated
  orchestrator may be production machinery without yet being retained learning.
- Selecting one item from a fully predefined catalog shows configuration reach,
  not construction of unanticipated machinery.
- Model-written code that is discarded after one task may demonstrate factory
  activity within the task, but not a learning factory across tasks.

## Stage 3: continual learning widens the persistent change surface

Use the minimal temporal relation:

```text
experience on task t
  -> persistent change in the system
  -> a different solution process on a later task
```

The persistent change may be parametric, natural-language, symbolic, or mixed.
This is why the [deployed system rather than the model
alone](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
is the relevant boundary: prompts, retrieval, context policies, schedulers,
tools, validators, and runtime rules can all change later behavior.

The existing [continual-learning governance
note](../../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
adds selection, validation, authorization, and coordination. Those are
important for warranted deployment, but the foundation first needs the weaker
cross-task dependence. The supporting work should say exactly when it moves
from minimal continual learning to improvement-directed or self-improving
change.

Counterexamples and limits:

- Saving a trace that later work never consumes is persistence without
  learning effect.
- Loading a memory that is ignored does not establish causal dependence.
- A human maintenance edit can change later work without showing that the agent
  learned the change.
- A later process that changes only because the task differs does not establish
  retained learning from earlier experience.

## Stage 4: retained construction makes the factory learn

Combine stages 2 and 3 only after both stand independently. The relevant event
is not merely that the agent writes code, nor merely that state persists. The
agent constructs or changes production machinery from experience; the result is
retained; and later work uses the changed machinery.

The concrete candidates include:

- task decomposition and aggregation strategies;
- context selection, compression, and retrieval policies;
- representations and schemas;
- evaluators, tests, and validation procedures;
- search, planning, and recovery procedures;
- tool implementations and interfaces; and
- delegation and coordination structures.

The [orchestration persistence
note](../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md)
provides one narrow example: task-specific run state can remain ephemeral while
reusable selection strategies are promoted into tested library code. The
example should support the general possibility without becoming the definition.

Required supporting-note job: derive the learning-factory intersection and
separate four thresholds: constructed machinery, retained machinery, causal
later use, and evidence of improvement.

Counterexamples and limits:

- A retained but unused tool is not operative learning.
- A reused tool written independently of experience is reusable machinery, not
  continual learning from the earlier task.
- Better output on the task that caused the change does not show cross-task
  learning.
- One successful transfer does not establish an indefinitely self-improving or
  compounding system.

## Stage 5: higher-order construction yields recursion; reflection needs more

Some object-level tasks are difficult because they need decomposition,
representation, evaluation, or tool construction. Choosing or constructing the
right decomposition, representation, evaluator, or tool can itself be a
difficult task. The factory may therefore use production machinery to build
machinery that changes how later production machinery will be built.

That is the factory-building-factory structure. It becomes operationally
recursive when the produced machinery participates in another machinery-
construction transition. It becomes reflective only on a path satisfying the
[reflective-system definition](../../notes/definitions/reflective-system.md): a
causally connected representation of selected aspects of the same system is
used in operation and can affect later behavior.

The [fixed-decomposition
argument](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)
explains why some higher-order choices must remain challengeable when they carry
task-specific mistakes. It does not imply that every fixed component is a
defect. General learning machinery, objectives, interfaces, resource controls,
or trusted kernels may remain fixed over the claimed reach.

Required supporting-note job: derive the higher-order structure from nested
task difficulty and state when recurrence, reflection, self-improvement, and
compounding do or do not follow.

Counterexamples and limits:

- A conventional generator can emit another generator from a supplied complete
  specification without learning or reflecting.
- A reflective system can inspect its scheduler without changing it.
- An adaptive system can change its controller without a self-representation
  and therefore learn without reflection.
- A successor can remove the path that produced it; one transition does not
  establish repeatability.

## Stage 6: compare mechanisms on the same causal job

The comparison object is a transition from experience to a persistent change
that affects later production. Candidate mechanisms include:

- trial-and-error retention of successful machinery;
- reuse or transformation of trajectories and episodes;
- enumerative, stochastic, evolutionary, or LLM-guided program search;
- learned policies for selecting or constructing machinery;
- gradient-based or other direct optimization;
- natural-language theory construction and revision; and
- mixtures operating at different times or on different machinery.

Compare them by what evidence they consume, what change space they can reach,
how they assign credit, how a result becomes operative, how they handle
negative transfer and revision, and their total computational and human cost.
Do not equate a readable mechanism with a better one or a parametric mechanism
with a more general one.

Required supporting-note job: produce a neutral comparison frame or show that
existing notes already supply one. A catalog that merely names techniques does
not carry the argument.

## Stage 7: theory mediation is the proposal

Natural-language theory is a candidate coordination medium for the learning
factory because it can place several kinds of state in one interpretable
representation:

- a model of task or domain structure;
- a model of the solver's relevant capacities and limitations;
- explanations of observed successes and failures;
- proposed changes and their intended mechanisms;
- scope conditions and predictions; and
- evidence that should revise or reject the account.

An LLM can interpret this state into different software changes rather than
requiring one fixed update operator per artifact kind. Existing work on
[program theory and delayed
feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md),
[theory-mediated causal
paths](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md),
and [sample efficiency under structured
shifts](../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
supplies the downstream hypothesis and evidence requirements.

The comparative prediction must be sharper than “theory is flexible.” Plausible
tests ask whether theory mediation, at comparable information and total cost:

- transfers one explanation into several different machinery changes;
- predicts where a mechanism will fail or stop applying;
- improves diagnosis and recovery after delayed feedback;
- supports selective revision without replaying all prior experience; or
- performs no better, or worse, than trajectories, rules, program search,
  learned policies, direct optimization, or mixtures.

Required supporting-note job: state versatility as a defeasible comparative
claim. The article may then make theory mediation its research bet without
making it the foundation of the architecture.

## Integration tests for the final article

1. Delete the theory-mediation section. The reader should still understand why
   an agentic system can become a learning software factory.
2. Replace every factory term with its plain causal description. The argument
   should lose brevity, not validity.
3. Hold the software substrate fixed. The starting architecture must remain
   coherent, while the practical-generalization claim becomes an empirical
   question rather than a contradiction.
4. Let the factory learn without a self-representation. Continual learning must
   remain possible, while reflection is correctly withheld.
5. Let the system construct one-off code and discard it. Factory activity may
   occur, but cross-task factory learning must be withheld.
6. Let theory mediation lose to a direct optimizer. The comparative proposal
   must lose or narrow without collapsing the architectural spine.
