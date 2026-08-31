---
description: "Broad software demands make exhaustive predefinition of useful family-specific production machinery practically implausible, motivating agentic factory development without ruling out a fixed universal substrate in principle"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Broad software demands create pressure for agentic factory development

A sufficiently broad class of software demands creates practical pressure for an agentic system to construct or revise reusable production machinery instead of relying only on family-specific production knowledge supplied in advance. This is a claim about engineering adequacy and scaling, not an impossibility theorem.

In principle, a fixed universal substrate could interpret every needed program. A large catalog could contain every useful schema, workflow, evaluator, representation, tool, and decomposition. The premise here is weaker: as the covered demands widen, exhaustively anticipating and maintaining all useful family-specific production knowledge becomes increasingly implausible and expensive.

The relevant response is agentic [factory development](./definitions/factory-development.md): the system participates in constructing or revising reusable machinery that later production can use.

## Why breadth exposes missing production knowledge

Different software demands can require different:

- decompositions and aggregation strategies;
- intermediate representations and schemas;
- retrieval, context-selection, and memory policies;
- algorithms and data structures;
- tests, evaluators, simulators, and acceptance procedures;
- tools, interfaces, libraries, frameworks, and deployment machinery;
- recovery, rollback, monitoring, and maintenance processes; and
- relations among requirements, architecture, code, tests, runtime state, and operational evidence.

These are not all object-level product decisions. When they are retained and reused across a declared product or solution family, they become part of the [software factory](./definitions/software-factory.md) for that family.

A fixed substrate can remain general while the installed family knowledge changes. Write the configured factory schematically as:

\[
F_{\mathcal P,t}=\operatorname{configure}(G,K_{\mathcal P,t})
\]

where \(G\) is general machinery and \(K_{\mathcal P,t}\) is the current family-specific production knowledge. Agentic factory development can update \(K_{\mathcal P,t}\) without requiring every component of \(G\) to be self-modifying.

## Bounded model calls make the pressure visible

The [bounded-context orchestration model](./bounded-context-orchestration-model.md) shows how a larger computation can be organized around bounded LLM calls. Difficult tasks may require decomposition, persistent intermediate state, code execution, map-reduce aggregation, or external verification.

But the right orchestration is not determined by task size alone. It depends on the task's dependency structure, the solver's effective capabilities, what information must survive between calls, which operations need exact execution, and how partial results can be checked and combined.

A generic scheduler can provide recursion or iteration without knowing the useful decomposition for every domain. The family-specific strategy may still need to be constructed. The [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) therefore supports both a fixed software substrate and the possibility that schemas, invariants, and control strategies become later development targets.

## Configuration, construction, and acquisition must stay separate

Three increasingly strong cases are easy to conflate:

1. **Configuration:** select and bind anticipated options inside already supplied family machinery.
2. **Construction:** realize a factory or asset from a supplied schema, metamodel, mapping, or complete description.
3. **Acquisition:** use task or production evidence to determine what reusable family-specific production knowledge is required and construct or revise it.

The first two can cover substantial work. Greenfield, Tool Factory, and MDSoFa already establish recursive construction from supplied family knowledge. The [construction-versus-acquisition note](./a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md) marks the remaining boundary.

The practical generality claim concerns the third case. A system does not meet it by hiding a target-indexed catalog of handcrafted factories inside its supposedly general substrate.

## What would support the claim

The pressure claim earns evidence when a fixed supplied repertoire repeatedly encounters demands for which:

- ordinary product configuration cannot express the needed solution process;
- human experts introduce new schemas, decompositions, tools, evaluators, or workflows;
- those additions become reusable across later products or episodes; and
- systems that can construct such machinery from evidence transfer with less new human construction of family-specific production knowledge.

A stronger test declares the task and product-family frames before outcomes are known, withholds target-specific production machinery, and compares a fixed-repertoire condition against one allowed to construct and retain new machinery. The comparison should count human interventions, failed attempts, total compute, and later reuse rather than only successful product outputs.

## What would weaken or defeat it

The claim should narrow where a small fixed substrate and stable general policies cover the declared demands at comparable or lower total cost. It also weakens when generated machinery is mostly disposable glue, when the same few tools suffice across domains, or when constructing new machinery adds more error and maintenance burden than it removes.

A universal fixed substrate is therefore a live counterhypothesis, not a contradiction. The empirical question is how much task- or family-specific production knowledge can be economically absorbed into fixed general machinery and how much must still be acquired or revised as demands change.

## Scope

- The note does not claim that every task needs new software or that every agentic system is a software factory.
- Broad demand coverage is not itself learning. The system may construct machinery from a complete human-supplied description.
- Fixed objectives, interfaces, runtimes, model providers, resource controls, and trusted kernels may remain.
- The relevant burden is recurring human construction of family-specific production knowledge required by the claimed reach, not the mere existence of handcrafted general components.
- One novel tool does not establish broad extensibility; later reuse and repeated transfer are separate evidence requirements.

---

Relevant Notes:

- [An agentic substrate becomes a software factory through family-specific production machinery](./an-agentic-substrate-becomes-a-software-factory-through-family-specific-production-machinery.md) — grounds: separates fixed general machinery from installed family knowledge
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: shows why learning confined to supplied production structure may preserve its errors
- [Orchestration strategies and run-state have opposite persistence economics](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — exemplifies: reusable control strategy may merit promotion while task-specific state remains ephemeral
- [Machinery persists by warrant, not position, in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — extends: explains why the pressure does not require universal self-modification
