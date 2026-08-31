---
description: "Minimal factory-level continual learning requires production experience to causally determine a retained change to reusable family machinery that affects later production"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, learning-theory, self-improving-systems]
---

# A software factory learns when production experience changes reusable machinery used later

A [software factory](./definitions/software-factory.md) undergoes **factory-level continual learning** when experience from producing one product causally determines a retained change to the reusable family-level production machinery of a new factory and later production under that factory depends on the change.

The minimal path is:

```text
production of product A under factory F
  -> experience bearing on reusable machinery
  -> retained change to reusable machinery in new factory F'
  -> later production under F' depends on the change
```

`F'` is the new factory produced by the learning episode. It may be a revised version of the same family-scoped factory; it need not define a new product family.

Each link excludes a nearby but weaker event.

- Experience without a factory change is observation or feedback.
- Product repair without a reusable change is solution development.
- A generated but rejected or discarded asset is a candidate, not retained learning.
- A factory produced from knowledge supplied independently of the experience is construction, not learning.
- Stored machinery that later production does not consume has no demonstrated behavioral effect.
- A later process that differs only because the task differs does not show dependence on earlier experience.

## The learning target is factory development

[Factory development](./definitions/factory-development.md) constructs or revises reusable production machinery for a declared product or solution family. The learning claim therefore concerns changes such as:

- revised family scope, commonality, variability, or configuration knowledge;
- new or changed schemas, viewpoints, and representations;
- decomposition, aggregation, retrieval, or context-management strategies;
- processes, guidance, prompts, and methods;
- tools, generators, libraries, frameworks, and interfaces;
- tests, evaluators, validation rules, monitors, and recovery procedures; or
- reusable lifecycle content for requirements, architecture, deployment, operation, maintenance, or migration.

The same production event can have both product-level and factory-level effects. A failed test may trigger a patch to the current product and also reveal that a reusable test generator or release gate should change. Only the latter change is factory-level learning relative to the producing factory.

## Learning is boundary-relative

The causal determination must occur inside the learner boundary being claimed. At a human-inclusive boundary, a person and computational tools may jointly interpret experience and revise the factory. At a boundary that excludes the operator, a human-selected schema, evaluator, decomposition, promotion decision, or recovery step remains an external intervention rather than learning by the technical subsystem.

This distinction is about causal responsibility, not who typed the final bytes. An LLM can author a file while a person supplies the decisive change. Conversely, a person can provide an observation or acceptance response while the system determines how reusable machinery should change.

The permitted evidence and interaction protocol should therefore be declared separately from the update decisions assigned to the learner.

## Retention means later behavioral dependence

Retention is stronger than storage. The changed machinery must enter a path through which it can affect later production. Depending on the factory, this may mean that a revised schema is loaded, a workflow is selected by default, a validator gates later changes, a tool becomes available, or a natural-language rule is retrieved into later model calls.

For retained theory, this requires activation rather than storage alone: the theory must be selected into a call-specific context, interpreted, and change a later operation. [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) separates these functions.

Permanent installation is not required. A change can be operative for a declared horizon and later be rolled back. What matters is that later production actually depended on it during the interval for which learning is claimed.

Later use can occur on another family member or on a later lifecycle episode for the same member, provided the changed item is genuinely reusable family machinery rather than a disguised product-local patch. Evidence from a distinct admitted variation is stronger because it tests the reuse claim directly.

## Minimal learning does not imply improvement

A retained factory change can degrade later production. The causal sequence still establishes learning in the minimal sense that experience changed future capacity or behavior. Calling it **improvement** additionally requires a declared objective, an assessment relation, and evidence that the change helped relative to an appropriate comparison.

The minimal definition also does not require:

- explicit competing candidates or a proposal-selection loop;
- a complete independent evaluator;
- computational closure;
- reflection or a self-model;
- recursive factory construction;
- broad domain reach;
- repeatability after the change; or
- compounding improvement.

Those are separately testable extensions.

## Direct updates and search both qualify

Some learning paths expose proposals, reject candidates, select one, and install it. Others directly update a retained rule, policy, model, or schema in response to evidence. Both can satisfy the minimal path when the causal and later-use relations are established.

The [proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) remains important for architectures that expose rejectable candidates. It should not be imported as the definition of all factory learning.

Likewise, [continual-learning governance](./continual-learning-requires-governing-behaviour-changing-writes.md) adds selection, validation, authorization, coordination, and regression control for safe deployment. Those requirements govern learning well; they are stronger than the minimal occurrence condition.

## Evidence

A persuasive record should identify:

1. the factory machinery before the episode;
2. the production experience that bore on it;
3. the update decision and the declared learner boundary;
4. the retained change;
5. the new factory containing that change;
6. the later production path that consumed it; and
7. the behavioral difference attributable to the retained change.

Withholding, reverting, or replacing the change strengthens causal attribution. A mere chronology—experience occurred, a file changed, later work improved—does not establish that the same learning path connects the events.

## Scope

- The definition is relative to a declared factory and product-family boundary.
- Accumulating product facts or traces can be continual learning at the deployed-system level without being factory-level learning.
- Human maintenance can improve a factory without demonstrating learning by a narrower technical subsystem.
- Factory-level learning can occur in natural-language, symbolic, parametric, or mixed representational forms.
- One occurrence does not establish indefinite learning capacity or recursive self-improvement.

---

Relevant Notes:

- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: places all behavior-determining factory machinery inside the candidate learning surface
- [Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) — extends: adds governance requirements for safe and coordinated deployment
- [Operative change](./definitions/operative-change.md) — extends: supplies the stronger persistence and behavioral-authority account for retained system changes
- [Task families and product families classify different things](./task-families-and-product-families-classify-different-things.md) — grounds: clarifies what later transfer establishes at task and family levels
