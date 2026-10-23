---
description: "Distinguishes model interpretation from runtime-assigned execution, including model-generated code and the same code artifact used as prompt context or as an executable operation"
type: types/note.md
brief: code-complements-weight-prompt-with-symbolic-operations.brief.md
traits: [title-as-claim]
tags: [computational-model, learning-theory, constraining, artifact-analysis]
---

# Code complements the weight–prompt pair with independently executed symbolic operations

The model's weights and its prompt jointly produce an LLM's behavior. The
weights supply learned competence; the prompt supplies the current task,
evidence, and constraints. Code complements this pair by defining operations
that a runtime executes independently of model interpretation. A system can
use the model to choose what to do and code to carry out the chosen operation.

The distinction concerns how the operation executes:

| Execution path | What determines the operation |
|---|---|
| Model-mediated | Weights and assembled prompt jointly produce an interpretation and response |
| Symbolic | Code and runtime define permitted transitions for explicit inputs and state |

“Independently” refers to model interpretation at that execution step. The
operation follows the runtime's rules using the supplied inputs and state.

## The same code can be read or executed

Consider a validator. Supplied in a prompt, its code helps the model understand
the checks, find defects, or propose changes. Run against a file, the same code
computes a verdict. The first use depends on the model's interpretation; the
second executes the checks. The workflow can enforce those checks by requiring
a passing verdict before it proceeds.

The code's bytes can be identical in both cases. What changes is the consumer:
a model reads them as context, or a runtime executes them. This is the relevant
[representational-form](./definitions/representational-form.md) distinction:
content is classified by how it is encoded and consumed. A stored instruction
likewise becomes prompt context when it is supplied to a model call.

## A model can author the operation it delegates

A model may generate, select, or revise a program, then ask a runtime to execute
it. The model chooses the computation; the runtime carries it out under its
operational rules. Authorship and execution are separate roles.

This allows a sequence of complementary operations: the model selects a
transformation, code performs it, and the model interprets the result. The
judgment about which transformation suits the task happens upstream of
execution. This is a case of [relocating semantic work](./semantic-work-can-be-relocated-but-not-eliminated.md).
The implementation needs to follow the selected rule, while
[the rule's suitability for the task needs its own assessment](./exact-implementation-does-not-validate-a-requirement.md).

[Bookkeeping makes the practical leverage concrete](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md):
a model can decide what work is needed while code maintains the dependencies
and completion records. That note develops the reliability argument. The same
division of labor also applies to calculations, transformations, and checks
outside scheduling.

## Scope

The weight–prompt pair describes a call with fixed model binding, inference
settings, tool exposure, and protocol. These settings and the external
environment also affect the system's behavior.

Symbolic execution follows assigned rules, which may permit variation,
concurrency, or external effects. A model response can also be repeatable.
The distinction is who applies the operational rules, rather than whether
successive outputs happen to match.

---

Relevant Notes:

- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: develops why bookkeeping is a high-leverage use of independent symbolic execution
- [Semantic work can be relocated but not eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md) — grounds: selecting or generating an operation moves judgment upstream rather than removing it
- [Representational form](./definitions/representational-form.md) — defined-in: distinguishes symbolic content from model-interpreted content by how it gets its consequences
- [Exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md) — grounds: limits what runtime-assigned execution establishes about the intended task
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: addresses when recurrent interpreted behavior warrants a symbolic commitment
- [Natural-language project state may specialize weight-resident search heuristics](./natural-language-project-state-specializes-search-heuristics.md) — grounds: develops how retained project information changes the prompt side of the operation
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](./unified-calling-conventions-enable-bidirectional-refactoring.md) — extends: makes movement between the two execution paths local while preserving an interface
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — extends: places both operation classes inside one behavior-producing system
