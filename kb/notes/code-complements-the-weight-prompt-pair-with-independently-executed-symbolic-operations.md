---
description: "A model-mediated operation is instantiated by weights plus prompt; code complements that pair by defining operations whose consequences a symbolic runtime executes without reinterpreting the prompt"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, learning-theory, constraining]
---

# Code complements the weight–prompt pair with independently executed symbolic operations

A prompt does not define an LLM operation by itself. Relative to fixed inference
settings and available tools, the operation is instantiated jointly by the
model's weights and the prompt supplied for the call. The weights provide broad
learned competence and general behavioral tendencies. The prompt supplies the
current task, project state, intent, evidence, and constraints that specialize
that competence.

Code supplies a complementary operation class. Relative to a runtime, code
assigns consequences to inputs and explicit symbolic state. Once the code has
been selected and installed, the runtime can execute those consequences without
asking the model to reinterpret the prompt or reconstruct the operation on every
use.

The distinction can be written schematically as:

```text
model-mediated operation:  weights + prompt  -> interpreted, generally stochastic behavior
symbolic operation:        code + runtime    -> runtime-assigned state transition
```

Neither side is independent of its execution environment. The claim is narrower:
a symbolic operation can execute independently of model interpretation even when
a model generated, selected, explained, or later revised the code.

## The forms contribute different capabilities

The weight–prompt pair is useful where the operation requires semantic
interpretation, open-ended generation, judgment, or search over alternatives.
Code is useful where the selected behavior can be assigned precisely enough to
benefit from deterministic execution, explicit state, reliable bookkeeping,
repeatability, or an enforceable check.

This is the mechanism behind the
[scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).
A model may decide what a scheduler should do or write the scheduler, while a
symbolic runtime owns queue state, counters, checkpoints, retries, and exact
transitions. Moving those operations into code removes repeated interpreter
deviation relative to the implemented transition. It does not establish that
the transition implements the right requirement, because
[exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md).

The complement therefore is not natural language versus code. It is between two
ways of producing behavior:

- a **model-mediated operation**, whose behavior is defined by the interaction of
  distributed-parametric weights with a call-specific prompt; and
- a **symbolic operation**, whose behavior is assigned by code and its runtime.

A deployed agent system composes both.

## Code can be both project state and executable state

The same code artifact can participate through two consumption paths.

When code is loaded into a prompt, it is project evidence for a model-mediated
operation. It can reveal interfaces, dependencies, invariants, current behavior,
and possible modification points. In that path, the code helps the weight–prompt
pair choose or interpret a change.

When the runtime imports, executes, tests, or validates the code, the artifact
has symbolic force. Its consequences no longer depend on how the model reads it.
The artifact may therefore be both an object of semantic search and the
independent executor of a result produced by that search.

```text
code read in a prompt
    -> changes model-mediated search
    -> revised code is proposed and selected
    -> runtime executes the revised code
    -> execution evidence enters later prompts
```

This dual role follows the
[representational-form](./definitions/representational-form.md) rule that form is
classified by an operative part and consumption path, not by file extension or
storage substrate.

## The boundary is a learning target

An evidence-responsive system can learn by changing either operation class or
the division of responsibility between them. It may revise a prompt or retained
natural-language theory, revise target or control code, codify a stable
model-mediated pattern into code, or relax brittle code back into semantic
judgment.

[Unified calling conventions](./unified-calling-conventions-enable-bidirectional-refactoring.md)
can make this movement local by preserving one interface while its
implementation changes. Governing the movement still requires coverage of both
forms and their mapping, because
[moving the interpretation–enforcement boundary requires cross-form coverage](./moving-the-interpretation-enforcement-boundary-requires-coverage.md).

The resulting learning surface includes:

1. the prompt and retained artifacts used to specialize the model;
2. the code and symbolic state used to execute selected operations;
3. the evidence produced by both; and
4. the allocation rule deciding which operations remain model-mediated and
   which become symbolic.

Code is therefore not fixed infrastructure outside the learning account. It can
be produced and selected computationally, become operative state, and later be
revised or removed. Its complementarity to the weight–prompt pair concerns how
it executes, not who authored it or whether it must persist.

## Scope

- "Weights plus prompt" is an abstraction over a call with fixed model binding,
  inference settings, tool exposure, and protocol. Changing those can change the
  model-mediated operation too.
- A retained natural-language artifact is not automatically a prompt. It joins
  the pair only when context assembly supplies it as model input.
- "Independently executed" means independently of model reinterpretation at that
  execution step. Symbolic behavior still depends on the runtime, inputs,
  environment, and the correctness of the code.
- Deterministic execution is valuable only where the operation can be specified
  adequately. Judgment-heavy work may remain model-mediated, and a wrongly
  codified proxy can be reliably wrong.
- The claim does not rank the two operation classes globally. Their value depends
  on semantic ambiguity, verification, cost, latency, failure consequences, and
  the available evidence.

---

Relevant Notes:

- [Natural-language project state may specialize weight-resident search heuristics](./natural-language-project-state-may-specialize-weight-resident-search-heuristics.md) — grounds: isolates how retained project information changes the prompt side of the model-mediated operation
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: explains why exact state transitions and bookkeeping benefit from independent symbolic execution
- [Bounded-context orchestration model](./bounded-context-orchestration-model.md) — exemplifies: composes explicit symbolic state and transitions with bounded model calls
- [Exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md) — limits: symbolic exactness does not validate the upstream requirement
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: keeps the interface stable while an operation moves between model-mediated and symbolic implementations
- [Moving the interpretation–enforcement boundary requires cross-form coverage](./moving-the-interpretation-enforcement-boundary-requires-coverage.md) — extends: states what a reflective system must cover to govern that movement
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — extends: places both operation classes inside one behavior-producing and revisable system
