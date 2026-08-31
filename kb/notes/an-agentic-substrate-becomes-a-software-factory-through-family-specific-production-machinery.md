---
description: "Maps the bounded-call agentic substrate to Greenfield's software-factory ontology without calling every generic harness or generated program a factory"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# An agentic substrate becomes a software factory through family-specific production machinery

A general agentic substrate is not automatically a software factory. It becomes a Greenfield-style [software factory](./definitions/software-factory.md) for a declared software product or solution family when it is configured with reusable family-specific production knowledge that guides and supports the creation and sustainment of family members.

The mapping can be written schematically as:

\[
F_{\mathcal P}=\operatorname{configure}(G,K_{\mathcal P})
\]

where \(G\) is general agentic machinery, \(\mathcal P\) is a declared product or solution family, and \(K_{\mathcal P}\) is reusable production knowledge for that family. \(F_{\mathcal P}\) is the configured factory.

The general substrate may include bounded LLM calls, persistent state, context assembly, scheduling, tool dispatch, permissions, code execution, aggregation, validation, recovery, and storage. The [bounded-context orchestration model](./bounded-context-orchestration-model.md) supplies one computational form for this substrate, and [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) explains why exact progression and bookkeeping often belong in its software part.

The family-specific production knowledge may include:

- the family scope, commonality, variability, variants, and constraints;
- schemas, viewpoints, and intermediate representations;
- domain-specific decomposition and coordination strategies;
- processes, guidance, prompts, and methods;
- tools, generators, frameworks, libraries, and interfaces;
- tests, evaluators, validation rules, and recovery procedures; and
- reusable lifecycle content for requirements, design, implementation, deployment, operation, maintenance, or migration.

This list extends the historical ontology into current agentic machinery while preserving its boundary: the relevant items are reusable production knowledge for a declared family, not merely any software artifact present in the system.

## The substrate and the factory have different scopes

One substrate can host, select, compose, or help construct several factories. A generic LLM runtime may remain the same while different family schemas, tools, workflows, tests, and guidance configure it for web applications, data pipelines, embedded controllers, or another declared family.

Calling the general substrate one universal software factory would hide this distinction. Its generic capabilities may make many factories realizable, but a configured factory additionally embodies the specialization needed for a particular family. The ability to execute or generate any supplied program does not establish that the appropriate family specialization is already present or can be acquired from task evidence.

## Task-local software is not sufficient

An agent may write a script, parser, orchestrator, or evaluator for one task. That artifact can be real production machinery within the episode, but it is not yet Greenfield-style factory machinery merely because it is software written by the agent.

The additional boundary is reusable family scope. The artifact becomes part of factory machinery when it carries production knowledge intended to govern later work across a declared family or admitted variation space. Retention alone is not enough: a stored tool that is never used, or is used only as copied product-local code, has not been shown to participate in the configured factory.

This separates three cases:

| Case | Classification |
|---|---|
| The agent writes code that is the requested product | Solution or product work |
| The agent writes an episode-local program that helps produce the requested product | Task-local production machinery, not yet established as factory machinery |
| The agent retains a schema, workflow, tool, evaluator, or other asset that governs later production across a declared family | Reusable software-factory machinery |

## The mapping does not fix who develops the factory

Greenfield's accounts primarily assign [factory development](./definitions/factory-development.md) to human factory or product-line developers. The configured factory may then support human solution developers with varying amounts of automation.

An agentic system can occupy either side of that inherited division. It may use an already configured factory to develop family members. It may also participate in constructing or revising the family machinery. The latter is agentic factory development, an additional capability rather than part of the software-factory definition.

Likewise, the mapping does not imply learning. A complete family template can be supplied by people and installed computationally. The resulting agentic arrangement is a software factory even if its production knowledge never changes.

## Scope

- The mapping is functional, not a claim that a modern agent harness is identical to Greenfield's Microsoft IDE architecture.
- The general substrate may contain fixed components that apply across families.
- The configured factory can include human activities; actor allocation and autonomy must be declared separately.
- A family-valued product can itself be another factory, but recursive output does not establish acquisition, learning, reflection, or self-improvement.
- The product-family boundary must be declared independently; it cannot be inferred post hoc from whatever artifacts the system happened to produce.

---

Relevant Notes:

- [A software factory is family-scoped lifecycle production machinery](./a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: supplies the imported family, schema, template, configured-environment, and member boundaries
- [A software factory can produce another factory without learning its specialization](./a-software-factory-can-produce-another-factory-without-learning-its-specialization.md) — contrasts: shows that general construction machinery can realize supplied specialization without acquiring it
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — extends: places the configured model, artifacts, tools, and runtime inside the behavior-producing system boundary
