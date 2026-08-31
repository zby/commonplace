# Workshop: Agentic-system learning re-foundation

**Posed by:** the operator, 2026-08-31.

## Intent

Re-found the theory-mediated system-learning research program on an architectural argument that does not assume theory mediation. Preserve the existing theory-specific claims, experiments, and evidence, but place them downstream of a more general account of agentic software production and continual learning.

The refoundation must remain valid if theory mediation loses to another learning mechanism. It must also remain intelligible without using *software factory* as a metaphor. Historical terminology may compress an already established relation; it must not create the relation by definition.

## Starting point: the agentic computational substrate

The computational starting point is already developed in the [computational-model cluster](../../notes/computational-model-README.md). Agentic work is performed through bounded LLM calls embedded in persistent software machinery that can retain state, assemble context, schedule calls, expose tools, execute exact transitions, aggregate results, and check outcomes.

The [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) gives one explicit form of that architecture, while [scheduler–LLM separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) explains why exact progression and bookkeeping often belong in software rather than accumulated natural-language context.

This starting point does not imply that the software substrate learns, writes itself, or changes at all. A fixed, sufficiently general substrate remains possible in principle.

## Import the software-factory boundary before extending it

Greenfield's software-factory ontology supplies a useful established distinction, but it is narrower than a generic agentic system.

A Greenfield-style [software factory](../../notes/definitions/software-factory.md) is a development and runtime environment configured for a declared family of software products or solutions. Its family-specific production knowledge is distributed across a schema, packaged assets, processes or guidance, tools, frameworks, and lifecycle support. [Factory development](../../notes/definitions/factory-development.md) constructs or revises that reusable machinery; solution development uses it to create and sustain a family member.

The mapping used by this workshop is therefore:

```text
general agentic substrate
  + declared software product family
  + reusable family-specific production knowledge
  -> configured agentic software factory
```

A generated script or task-local orchestrator is not yet a Greenfield-style factory. It may be software used during production. It becomes factory machinery only when it carries reusable production knowledge for a declared family or admitted variation space.

This also means that a task family and a product family must not be silently equated. A benchmark may group tasks because they stress the same solver capability, while a product family groups software products or solutions through declared commonality and variability.

## Research question

For a sufficiently broad class of software demands, can an agentic system use production experience to construct and retain the family-specific machinery needed for later production? Among the mechanisms that could perform that work, does natural-language theory provide unusually versatile coordination across task understanding, solver limitations, failure diagnosis, proposed interventions, and heterogeneous software changes?

The first question concerns agentic factory development and continual learning. The second is the theory-mediation proposal. A negative answer to the second must not undo the first.

## Conceptual spine

```text
agentic computational substrate
  + family-specific production knowledge
  -> configured software factory

configured software factory
  + demands that exceed currently installed family machinery
  + agentic construction or revision of reusable production machinery
  -> agentic factory development

agentic factory development
  + production experience causally determines a retained factory change
  + later production depends on that change
  -> factory-level continual learning

factory-level continual learning
  -> compare learning mechanisms on the same causal job
  -> theory mediation as one particularly versatile candidate
```

Each `+` introduces an additional premise. The [conceptual spine](./conceptual-spine.md) records what follows, what does not follow, and which counterexamples defeat each step.

## What is downstream rather than foundational

Several important ideas remain in the program, but they are not required to derive factory-level continual learning:

- **Higher-order or recursive factory development** begins when production machinery is used to construct or revise machinery for constructing later production machinery.
- **Reflection** additionally requires a causally connected representation of selected aspects of the same system to participate in operation or revision.
- **Computational closure** asks whether all decisions assigned to a declared learning path are computationally supplied, conditional on permitted external evidence and interaction.
- **Self-improvement** adds an objective and evidence that the system's own change improves it relative to that objective.
- **Compounding** requires later evidence that an earlier change improved the capacity to produce further improvements.
- **Breadth or domain extensibility** asks which demands the process can turn into adequate family specialization; it is independent of closure.

Factory-valued output, recursion, reflection, learning, improvement, closure, and compounding must remain separately classifiable.

## Direction fixed by the operator

### Practical generality, not a necessity theorem

Do not claim that every agentic system must construct new production machinery. A fixed universal interpreter or substrate could in principle express every required workflow or program.

The practical conjecture is weaker: across sufficiently broad software demands, useful family-specific schemas, representations, decompositions, evaluators, tools, and workflows will often not be worth or possible to enumerate in advance. A general agentic system should therefore be able to participate in factory development when its installed machinery is inadequate.

### Continual learning is an additional premise

Software production and factory development do not imply learning. Factory-level continual learning requires a causal cross-episode relation:

```text
production experience
  -> system-determined retained change to reusable factory machinery
  -> changed later production
```

The change need not be beneficial. Improvement, warrant, validation, autonomy, and closure add stronger requirements. The existing [continual-learning governance note](../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) remains useful for governed deployment, but it must not be used to build all stronger conditions into the minimal learning relation.

### Compare mechanisms before proposing theory mediation

The relevant comparison is not natural language versus code or weights. It is among mechanisms that turn experience into retained changes affecting later production. Live candidates include trial-and-error retention, trajectory reuse, program search, learned construction or selection policies, direct optimization, theory mediation, and mixtures.

The positive conjecture is that natural-language theory may be unusually versatile because one LLM-interpretable medium can express claims about tasks, solver capacities, failures, interventions, evidence, and scope, then guide changes across schemas, workflows, tools, evaluators, representations, prompts, and code. This is a comparative hypothesis, not a definition of learning.

## Explicit non-goals

- Do not claim that theory mediation is necessary, sufficient, or universally superior.
- Do not call every coding agent, workflow, generated program, or task-local orchestrator a software factory.
- Do not infer a product family from an evaluator's task grouping.
- Do not infer factory learning from product repair, retained bytes, or improved output on the same task.
- Do not infer learning from recursive construction when the target specialization was supplied.
- Do not require universal self-modification; fixed general machinery, objectives, interfaces, resource controls, and trusted kernels may remain.
- Do not make computational closure, reflection, self-improvement, or compounding part of the minimal continual-learning premise.
- Do not discard theory-mediated material merely because its argumentative position changes.

## Implementation sequence

1. **Contain premature article integration.** Remove article-level claims that depend on successor-factory, closure, or domain-extensibility terminology before the ontology is settled.
2. **Import the Greenfield ontology.** Keep compact definitions for software factory and factory development, a versioned reconstruction, and a separate construction-versus-acquisition prior-art note.
3. **Rebase this workshop.** Replace the loose task-local factory usage with the substrate/configured-factory/factory-development distinction and move recursion and closure downstream.
4. **Write the learning bridge.** Add durable notes for the agentic-substrate mapping, task-family/product-family distinction, practical pressure for agentic factory development, minimal factory-level continual learning, and neutral mechanism comparison.
5. **Restructure the research-program article.** Make the architectural dependency order visible, then preserve the strongest existing theory-mediated argument, experiment, and evidence as the downstream proposal.

The [transition map](./transition-map.md) records the current disposition of existing material.

## Relationship to the existing workshop

The [theory-mediated self-improvement series](../theory-mediated-self-improvement-series/README.md) remains active until a separate migration and closure decision. It continues to own its accepted and rejected drafts, ledgers, source controls, evidence records, and theory-specific investigations.

This workshop owns the new dependency order and the mapping between agentic computation, software-factory ontology, factory-level continual learning, alternative mechanisms, and theory mediation. Historical process records must not be rewritten as though the new framing had governed their production.

## Evaluation

The refoundation succeeds only if a skeptical reader can recover these claims without accepting theory mediation:

1. bounded LLM calls participate in a larger behavior-producing software system;
2. adding family-specific reusable production knowledge configures that substrate as a software factory;
3. broad demands can create a practical need for the agent to construct or revise that machinery;
4. production experience can causally change reusable machinery used in later production; and
5. several learning mechanisms could drive such changes.

Theory mediation then earns its place through comparative evidence. Useful tests hold information and total cost as comparable as possible and ask whether retained theory improves transfer, diagnosis, recovery, selective revision, or heterogeneous machinery change relative to credible alternatives.

## What closes this workshop

The workshop closes when:

- durable notes carry every step of the revised spine without circular dependence on theory mediation;
- task families and product families are kept distinct;
- factory-valued construction, specialization acquisition, learning, reflection, closure, self-improvement, and compounding can be classified independently;
- alternative mechanisms are represented fairly;
- the research-program article has been restructured around the derived architecture; and
- every old-workshop artifact has a recorded disposition before the old workshop is closed separately.
