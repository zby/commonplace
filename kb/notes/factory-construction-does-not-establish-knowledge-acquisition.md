---
description: "Recursive software-factory construction is prior art, but the demonstrated constructors receive the family definitions, metamodels, mappings, and expertise that determine the produced factory"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, self-improving-systems]
---

# A software factory can produce another without acquiring family-specific production knowledge

Producing a software factory is not by itself evidence that a system acquired the family-specific production knowledge embodied in that factory. The software-factory literature already contains recursive factory construction and tooling bootstraps. In the retained examples, computation realizes production machinery from supplied family definitions, metamodels, mappings, frameworks, or expertise. The semantically decisive family knowledge still originates with people.

This separates two problems:

```text
factory construction
  supplied description or family-specific production knowledge
  -> executable production machinery

production-knowledge acquisition
  task or production evidence
  -> adequate family-specific production knowledge
```

A constructor can be highly expressive on the first problem while doing nothing on the second.

## Greenfield's factory-building factory

Greenfield and Short's [2003 software-factory account](../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) explicitly describes software factories being used to produce other software factories. An IDE is used to build languages, frameworks, and tools for factory construction; those assets form a template that configures another IDE as a factory-building factory.

The recursive product type is real: one configured production environment helps build another configured production environment. But product-line developers still choose the target family, define its domain models and variation, and construct the family-specific template and assets. The example automates parts of factory construction; it does not infer the required family production knowledge from experience.

## Tool Factory bootstraps production tooling from a supplied language family

Cook and Kent's [Tool Factory](../sources/cook-kent-tool-factory-2003.ingest.md) makes the mechanism more concrete. A language designer combines supplied family fragments and patterns into a domain-specific-language definition. A generator then produces a designer and related tools on top of a shared framework. The language designer itself can be represented as another generated designer, allowing one version of the tool factory to bootstrap the next.

Again, the recursive construction is substantive. What remains supplied are the language-family definition, fragments, patterns, framework, and mappings into implementation languages and technologies. Regenerating the production tooling can propagate or re-express that family knowledge without acquiring it.

## MDSoFa computes factories from supplied metamodels and expertise

Langlois and Exertier's [MDSoFa](../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md) goes further by implementing a model-driven producer whose outputs can include metamodels, expertise, tools, frameworks, and another model-driven factory. The paper explicitly names the recursive case a `software factory factory`.

Its computation combines supplied metamodels, mappings, aspects, generic expertise, target-platform choices, rule selection, and templates to produce specific expertise and tool environments. Human metamodel designers and architects supply the decomposition and strategic choices that make the generated factory appropriate to its target. The system demonstrates computational factory construction from supplied family-specific production knowledge, not evidence-driven acquisition of that knowledge.

## Construction and acquisition answer different questions

| Question | Construction from supplied production knowledge | Acquisition of production knowledge |
|---|---|---|
| Primary input | Family schema, metamodel, language definition, mappings, expertise, templates, or complete factory description | Requirements, repositories, examples, failures, tests, user interaction, telemetry, and other task or production evidence |
| Computational job | Realize, transform, package, install, regenerate, or compose production machinery | Determine what family scope, representations, workflows, tools, tests, variation knowledge, and other machinery the evidence requires |
| Main uncertainty | Whether the description can be realized correctly and economically | Which description or production organization is adequate |
| Prior-art status in the retained sources | Explicit and sometimes implemented | Not established as a system-determined process in the retained sources |

The distinction is not a judgment that construction is trivial. Tool generation, metamodel transformation, packaging, bootstrapping, compatibility, and installation are real technical achievements. The point is that they start after much of the target-specific production knowledge has been selected and represented.

Nor must acquisition produce every detail from nothing. General models, languages, search procedures, runtimes, trusted kernels, and reusable cross-domain machinery can remain fixed. The relevant question is whether the target-specific production knowledge claimed as newly handled was already supplied or was determined from permitted evidence by the system.

## What would turn the feedback path into learning

Greenfield's [2007 account](../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) already routes defects, requests, and unanticipated variation from solution developers to factory developers. Human factory developers then revise reusable assets or perform factory specialization.

A computational learning extension would require a stronger causal path:

```text
production under current family machinery
  -> evidence about its limits
  -> system-determined change to reusable family machinery
  -> retention and later use of that change
```

That path concerns [factory development](./definitions/factory-development.md), not merely product repair. It can be driven by theory mediation, program search, trajectory reuse, learned policies, direct optimization, trial and error, or mixtures. Recursive factory output does not select among those mechanisms and does not make the transition learning by itself.

## Consequences for the research program

The novelty claim should not be that software factories can build software factories. That is established prior art. The open problem is whether an agentic system can use task and production evidence to acquire, revise, and retain the family-specific production knowledge that existing factory constructors receive from people.

This also blocks a common shortcut. A generic interpreter or generator may be able to realize any factory when given a complete enough description. That constructional expressivity does not establish that the correct description can be found from the evidence available for a previously unanticipated demand.

## Scope

- The negative acquisition claim is bounded to the retained sources; it is not a claim about every system ever described under synthesis, meta-learning, or self-modification terminology.
- Producing another producer is compatible with learning, but does not imply it.
- Regenerating a newer tool or factory can be useful bootstrapping even when all semantically decisive changes are supplied by people.
- A later agentic system may combine construction and acquisition in one process. The distinction remains useful because the evidence burdens differ.

---

Relevant Notes:

- [A software factory is family-scoped lifecycle production machinery](./a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: supplies the inherited factory, family, asset, member, and development-process boundaries
- [Software factory](./definitions/software-factory.md) — defined-in: names the configured family-specific producer constructed in the prior-art examples
- [Factory development](./definitions/factory-development.md) — defined-in: names the acquisition or revision target when reusable family machinery changes
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — extends: explains why computation inside a supplied factory structure does not test whether that structure should change
