---
description: "A model-mediated operation is instantiated by weights plus prompt; code complements that pair by defining operations whose consequences a symbolic runtime executes without reinterpreting the prompt"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, learning-theory, constraining]
---

# Code complements the weight–prompt pair with independently executed symbolic operations

A prompt does not define an LLM operation by itself. Relative to fixed call
settings, the operation is instantiated jointly by the model's weights and the
prompt. The weights provide broad learned competence. The prompt supplies the
current task, project state, intent, evidence, and constraints that specialize
that competence.

Code supplies a complementary operation class. Relative to a runtime, code
assigns consequences to inputs and explicit symbolic state. Once selected and
installed, the runtime can execute those consequences without asking the model
to reinterpret the prompt or reconstruct the operation on every use.

```text
model-mediated operation:  weights + prompt  -> interpreted, generally stochastic behavior
symbolic operation:        code + runtime    -> runtime-assigned state transition
```

A model may generate, select, explain, or revise the code. That provenance does
not change how the installed operation executes. "Independently" means
independently of model interpretation at that execution step, not independently
of the runtime, inputs, or environment.

The weight–prompt pair is useful where an operation requires semantic
interpretation, open-ended generation, judgment, or search. Code is useful where
a selected behavior can be assigned precisely enough to benefit from exact state
transitions, reliable bookkeeping, repeatability, or enforceable checks. This is
the mechanism behind the
[scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md):
a model may decide what a scheduler should do or write it, while a symbolic
runtime owns queues, counters, checkpoints, retries, and transitions.

The complement is therefore not natural language versus code. It is between a
model-mediated operation defined by the interaction of weights and a
call-specific prompt, and a symbolic operation defined by code and its runtime.
A deployed agent system composes both.

## One code artifact can enter both operations

When code is loaded into a prompt, it is project evidence for a model-mediated
operation. It can reveal interfaces, dependencies, invariants, current behavior,
and possible modification points.

When a runtime imports, executes, tests, or validates the same code, the artifact
has symbolic force. Its consequences no longer depend on how the model reads it.
The code can therefore be both an object of semantic search and the independent
executor of a result produced by that search.

This dual role follows the
[representational-form](./definitions/representational-form.md) rule that form is
classified by an operative part and consumption path, not by file extension or
storage substrate.

## Scope

- "Weights plus prompt" abstracts over a call with fixed model binding,
  inference settings, tool exposure, and protocol. Changing those can change the
  model-mediated operation too.
- A retained natural-language artifact is not automatically a prompt. It joins
  the pair only when context assembly supplies it as model input.
- Symbolic exactness is relative to the implemented transition. It does not show
  that the code implements the right requirement, because
  [exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md).
- The claim does not rank the two operation classes globally. Judgment-heavy
  work may remain model-mediated, while adequately specified operations may gain
  reliability or efficiency from symbolic execution.

---

Relevant Notes:

- [Natural-language project state may specialize weight-resident search heuristics](./natural-language-project-state-may-specialize-weight-resident-search-heuristics.md) — grounds: isolates how retained project information changes the prompt side of the model-mediated operation
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: explains why exact state transitions and bookkeeping benefit from independent symbolic execution
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — exemplifies: composes explicit symbolic state and transitions with bounded model calls
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — extends: makes movement between the two operation classes local while preserving an interface
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — extends: places both operation classes inside one behavior-producing system
