---
description: "Experience-responsive retention: production experience determines a retained change to reusable family machinery that later production depends on; factory-level learning is retention that improves the factory relative to a declared objective"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, learning-theory, self-improving-systems]
---

# Factory learning is experience-responsive retention that improves the factory

A [software factory](./definitions/software-factory.md) undergoes **experience-responsive retention** when experience from production causally determines a retained change to its reusable family-level production machinery and later production depends on that change. It undergoes **factory-level learning** when such a retained change also improves the factory. Improvement is relative to a declared objective, so the learning claim carries that index in addition to the boundary index below.

The minimal retention path is:

```text
production under current factory machinery
  -> experience bearing on that machinery
  -> change to reusable family-level production machinery
  -> retention
  -> changed later production
```

Each link excludes a nearby but weaker event.

- Experience without a factory change is observation or feedback.
- Product repair without a reusable change is solution development.
- A generated but rejected or discarded asset is a candidate, not retention.
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

The same production event can have both product-level and factory-level effects. A failed test may trigger a patch to the current product and also reveal that a reusable test generator or release gate should change. Only the latter change is factory-level retention relative to the producing factory.

## Retention is boundary-relative, and learning inherits it

The causal determination must occur inside the learner boundary being claimed. At a human-inclusive boundary, a person and computational tools may jointly interpret experience and revise the factory. At a boundary that excludes the operator, a human-selected schema, promotion decision, or recovery step remains an external intervention rather than retention by the technical subsystem.

This distinction is about causal responsibility, not who typed the final bytes. An LLM can author a file while a person supplies the decisive change. Conversely, a person can provide an observation or acceptance response while the system determines how reusable machinery should change.

The permitted evidence and interaction protocol should therefore be declared separately from the update decisions assigned to the learner.

## Retention means later behavioral dependence

Retention is stronger than storage. The changed machinery must enter a path through which it can affect later production. Depending on the factory, this may mean that a revised schema is loaded, a workflow is selected by default, a validator gates later changes, a tool becomes available, or a natural-language rule is retrieved into later model calls.

Permanent installation is not required. A change can be operative for a declared horizon and later be rolled back. What matters is that later production actually depended on it during the interval for which retention is claimed.

Later use can occur on another family member or on a later lifecycle episode for the same member, provided the changed item is genuinely reusable family machinery rather than a disguised product-local patch. Evidence from a distinct admitted variation is stronger because it tests the reuse claim directly.

## Learning is retention that improves

A retained factory change can degrade later production. The causal sequence then establishes retention — experience changed future capacity or behavior — but not learning: the factory degenerates rather than learns. Learning additionally requires that the change improved the factory relative to a declared objective. Whether it did can be a fact of the trajectory before anyone verifies it; the definition needs the objective it is indexed to, not an oracle. Establishing the claim is a separate measurement problem, disciplined by [an antecedent better-factory comparison](./a-better-factory-claim-compares-operative-states.md).

Neither retention nor learning requires:

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

Some retention paths expose proposals, reject candidates, select one, and install it. Others directly update a retained rule, policy, model, or schema in response to evidence. Both can satisfy the minimal path when the causal and later-use relations are established.

The [proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) remains important for architectures that expose rejectable candidates. It should not be imported as the definition of the retention path itself.

Likewise, [continual-learning governance](./continual-learning-requires-governing-behaviour-changing-writes.md) adds selection, validation, authorization, coordination, and regression control for safe deployment. Those requirements govern retention well; they are stronger than the minimal occurrence condition.

## Evidence

A persuasive record should identify:

1. the factory machinery before the episode;
2. the production experience that bore on it;
3. the update decision and the declared learner boundary;
4. the retained change;
5. the later production path that consumed it; and
6. the behavioral difference attributable to the retained change.

Withholding, reverting, or replacing the change strengthens causal attribution. A mere chronology—experience occurred, a file changed, later work improved—does not establish that the same retention path connects the events. Establishing learning rather than retention alone further requires the improvement evidence a declared comparison supplies.

## Scope

- The definition is relative to a declared factory and product-family boundary.
- Accumulating product facts or traces can be retention at the deployed-system level without touching reusable factory machinery.
- Human maintenance can improve a factory without demonstrating learning by a narrower technical subsystem.
- Factory-level learning can occur in natural-language, symbolic, parametric, or mixed representational forms.
- One occurrence does not establish indefinite learning capacity or recursive self-improvement.

---

Relevant Notes:

- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: places all behavior-determining factory machinery inside the candidate learning surface
- [A better-factory claim compares operative states under an antecedent assessment relation](./a-better-factory-claim-compares-operative-states.md) — extends: disciplines the improvement half of the learning claim with its relata and antecedent relation
- [Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) — extends: adds governance requirements for safe and coordinated deployment
- [Operative change](./definitions/operative-change.md) — extends: supplies the stronger persistence and behavioral-authority account for retained system changes
- [Task families and product families classify different things](./task-families-and-product-families-classify-different-things.md) — grounds: clarifies what later transfer establishes at task and family levels
