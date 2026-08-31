# Conceptual spine

This ledger states what each stage assumes, what it concludes, and what remains unestablished. The causal relations are load-bearing; the labels merely compress them.

## Dependency map

| Stage | Additional premise | Derived claim | Not yet established |
|---|---|---|---|
| 1. Agentic computational substrate | Work is performed through bounded LLM calls embedded in persistent software machinery that stores state and mediates effects across calls. | The model call is not the whole behavior-producing system; consequential functions can live in software. | The software need not be generated, mutable, learning, family-specific, or universal. |
| 2. Configured software factory | The substrate is configured with reusable production knowledge for a declared software product or solution family. | The resulting configured production environment is a Greenfield-style software factory for that family. | A generic harness, task family, or task-local program does not yet satisfy this boundary. |
| 3. Agentic factory development | Current family machinery is inadequate for a covered demand, and the agent constructs or revises reusable family-level production machinery. | The agent participates in factory development rather than only solution development. | This is a practical capability claim, not a theorem that all useful machinery must be learned. |
| 4. Factory-level continual learning | Production experience causally determines a retained factory-development change and later production depends on it. | The factory learns in the minimal cross-episode sense. | The change need not improve outcomes, be warranted, reflective, autonomous, broad, or computationally closed. |
| 5. Learning-mechanism comparison | More than one mechanism can perform the experience-to-retained-factory-change transition. | Trial and error, trajectory reuse, program search, learned policies, direct optimization, theory mediation, and mixtures are live alternatives. | The list is not exhaustive and supplies no ranking. |
| 6. Theory-mediation proposal | Natural-language theory can jointly represent task structure, solver limits, failures, interventions, evidence, and scope, and an LLM can interpret it into heterogeneous factory changes. | Theory mediation may be an unusually versatile mechanism for factory-level continual learning. | Necessity, sufficiency, universal superiority, and general learning remain unestablished. |

## Stage 1: bounded calls participate in a larger software system

The computational foundation already exists in the [computational-model cluster](../../notes/computational-model-README.md). The [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) gives one explicit architecture in which symbolic state and transitions surround bounded model calls. The [scheduler–LLM separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) explains why exact progression, bookkeeping, and cheaply checkable invariants often belong in software rather than accumulated natural-language context.

The minimum premise is broader than either note's full formal conditions. A deployed agentic system uses one or more bounded calls while software outside those calls carries some consequential state or effect path: context assembly, memory access, scheduling, tool dispatch, permissions, execution, validation, recovery, aggregation, or retention.

Counterexamples and limits:

- A single stateless model call may lack the persistent cross-call machinery relevant to this program.
- An LLM-mediated scheduler weakens a clean model/software split but does not erase the surrounding serving and effect machinery.
- A fixed, perfectly general substrate satisfies this stage. Later construction and learning claims need additional premises.

## Stage 2: family-specific production knowledge configures a factory

The historical term now has an imported boundary. A [software factory](../../notes/definitions/software-factory.md) is a configured, family-specific production environment for a declared family of software products or solutions. The reusable production knowledge may be distributed across a schema, packaged assets, processes or guidance, tools, frameworks, generators, tests, and lifecycle support.

The mapping is:

```text
general agentic substrate
  + declared product or solution family
  + reusable family-specific production knowledge
  -> configured agentic software factory
```

The substrate can host or instantiate multiple factories. It should not automatically be called one universal factory. The Greenfield ontology classifies the configured family-specific producer, not every general mechanism on which it depends.

A **task family** groups tasks under some evaluation or solver-relevant relation. A **product family** groups software products or solutions through declared commonality and variability. The same collection may satisfy both descriptions, but neither follows from the other.

Counterexamples and limits:

- A generic coding agent or IDE is not a Greenfield-style factory merely because it produces software.
- A one-off generated script or orchestrator may help perform a task without carrying reusable family production knowledge.
- A schema, template, workflow, generator, or tool can be factory machinery without being the whole configured factory.
- A family member is product state relative to its producer, even when it happens to be another tool or factory.

## Stage 3: broad demands create pressure for agentic factory development

[Factory development](../../notes/definitions/factory-development.md) changes reusable family-level production machinery. Solution development changes one family member under supplied machinery. An agent participates in factory development when it constructs or revises family scope, schemas, variation knowledge, processes, tools, evaluators, representations, workflows, or other reusable machinery for later family production.

The premise is practical rather than logical. A fixed universal interpreter might express every required program. A complete catalog might contain every useful schema and workflow. The claim is that for sufficiently broad software demands, exhaustively pre-supplying task-appropriate family knowledge is unlikely to be economical or adequate. Novel requirements, repositories, environments, and failure modes will often expose missing or mistaken production knowledge.

This stage still does not require learning. An agent can construct a new factory from a complete human-supplied description. The [factory-construction prior-art boundary](../../notes/a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md) shows why construction and acquisition of family-specific production knowledge must stay separate.

Counterexamples and limits:

- Selecting an anticipated variant from a complete catalog is configuration, not acquisition of new production knowledge.
- Repairing one product does not become factory development unless the result changes reusable machinery.
- Constructing machinery from a supplied metamodel or schema demonstrates realization capability, not inference of that structure from production evidence.
- Fixed general machinery can remain. The burden falls on family-specific production knowledge claimed to be newly handled.

## Stage 4: production experience can make the factory learn

Combine agentic factory development with a causal cross-episode learning relation:

```text
production under current factory machinery
  -> experience or evidence about its behavior
  -> system-determined retained change to reusable factory machinery
  -> later production depends on the change
```

All four links matter. Experience that triggers only product repair does not change the factory. A generated candidate that is discarded does not persist. A stored artifact that no later production consumes has no demonstrated learning effect. A later change caused only by a different task rather than retained experience is not continual learning from the earlier episode.

This is deliberately weaker than the existing [continual-learning governance](../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) account. Governed deployment may require candidate selection, validation, authorization, rollback, and coordination across representational forms. Those are important stronger conditions, but not every direct evidence-responsive update exposes a proposal-selection architecture.

The [deployed system, not the model alone](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), is the relevant learning boundary. The retained change may live in weights, natural-language artifacts, symbolic software, retrieved memories, or mixtures. Factory-level learning is the subset that changes reusable production machinery.

Counterexamples and limits:

- A human maintenance edit can improve later production without showing that the agentic system learned the change.
- Better performance on the same product that caused the revision does not by itself show cross-episode reuse.
- A retained change can be harmful; learning is not yet improvement.
- One occurrence does not establish repeatability, compounding, broad reach, or autonomy.

## Stage 5: compare mechanisms on the same causal job

The shared comparison object is the transition from production experience to a retained factory change that affects later production. Candidate mechanisms include:

- trial-and-error retention of successful machinery;
- retrieval, reuse, transformation, or compression of trajectories and episodes;
- enumerative, stochastic, evolutionary, or LLM-guided program search;
- learned policies for selecting, composing, or constructing machinery;
- gradient-based or other direct optimization;
- natural-language theory construction and revision; and
- mixtures operating on different artifacts, timescales, or parts of the factory.

Compare mechanisms by the evidence they consume, the change spaces they reach, how they allocate search and credit, how changes become operative, how they detect negative transfer, their revision costs, and their total computational and human cost.

Readable state is not automatically better state. Parametric learning is not automatically more general. Exact symbolic machinery is not automatically correct. A fair comparison must hold task information, model access, interaction, and budget as comparable as the mechanism permits.

## Stage 6: theory mediation is the research proposal

Natural-language theory is a candidate coordination medium because it can express several kinds of state in one LLM-interpretable representation:

- models of task or domain structure;
- models of relevant solver capacities and limitations;
- explanations of successes and failures;
- proposed interventions and their intended mechanisms;
- scope conditions, predictions, and expected failure modes; and
- evidence that should revise or reject the account.

An LLM can interpret such theory into heterogeneous changes rather than requiring one fixed update operator per artifact kind. Existing notes on [program theory under delayed feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md), [theory-mediated causal paths](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), and [sample efficiency under structured shifts](../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) supply the downstream hypothesis and evidence requirements.

The comparative prediction must be stronger than “theory is flexible.” At comparable information and total cost, theory mediation should sometimes:

- transfer one explanation into several different factory changes;
- expose where a decomposition, representation, or evaluator will stop applying;
- improve diagnosis and recovery when decisive feedback arrives later;
- support selective revision without replaying all prior experience; or
- lose clearly when trajectories, direct search, learned policies, optimization, or mixtures solve the same transition more effectively.

## Optional extensions

These properties classify stronger systems or experiments. They do not sit on the mandatory path to theory mediation.

| Extension | Additional condition | What it establishes |
|---|---|---|
| Higher-order factory development | Factory machinery constructs or revises machinery used for later factory development. | A factory-building-factory relation in operation. |
| Operational recursion | The result of one machinery-construction transition participates in another transition of the same relevant class. | Recurrence of the construction path, not necessarily learning or improvement. |
| Reflection | A causally connected representation of selected aspects of the same system participates in operation or revision. | Aspect-relative reflective organization. |
| Computational closure | Every decision assigned to a declared learning path is computationally supplied, conditional on permitted external evidence and interaction. | Actor allocation for that path, not quality or breadth. |
| Self-improvement | Evidence supports that the system's own retained change improved a declared objective. | Improvement attribution, not compounding. |
| Compounding | A prior change improves the capacity to produce or select later improvements. | Improvement of the improvement process. |
| Domain breadth | The process acquires adequate family-specific production knowledge across a declared class of demands. | Reach, independent of closure. |

A factory can learn without reflection. A reflective factory can fail to learn. A closed path can perform badly. A broad process can remain human-open. A successor implementation can remove the path that produced it.

## Integration tests

1. Delete the theory-mediation stage. The reader should still understand configured software factories, agentic factory development, and factory-level continual learning.
2. Replace every factory term with its causal description. The argument should lose brevity, not validity.
3. Hold the substrate fixed. The architecture remains coherent; only the practical construction premise becomes false for the tested regime.
4. Generate one-off code and discard it. Production software exists, but factory machinery and continual learning are withheld.
5. Generate a factory from a complete supplied schema. Factory construction is established; acquisition of family-specific production knowledge and learning are withheld.
6. Retain a harmful factory change. Learning may have occurred, while improvement is withheld.
7. Let a direct optimizer beat theory mediation. The theory proposal narrows or loses without collapsing the earlier stages.
