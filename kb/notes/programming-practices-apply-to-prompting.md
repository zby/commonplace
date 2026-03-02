---
description: Programming practices — typing, testing, progressive compilation, version control — apply to LLM prompting and knowledge systems, with semantic underspecification and execution indeterminism making some practices harder in distinct ways
type: note
areas: [learning-theory, computational-model]
status: speculative
---

# Programming practices apply to prompting

Much of what we do in llm-do and this knowledge base is applying established programming practices to prompts, documents, and LLM workflows. The transfers are practical and actionable. Two properties of LLM-based systems — [semantic underspecification and execution indeterminism](./agentic-systems-interpret-underspecified-instructions.md) — make some practices harder than their traditional-programming originals, but in distinct ways.

## Practices we apply

**Typing.** We assign types to documents to mark what operations they afford — a `claim` can be verified, a `spec` can be implemented, `instructions` can be followed. This is the same practice as typing values in code: [the type determines valid operations](./instructions-are-typed-callables.md). The [verifiability criterion](../claw-design/document-types-should-be-verifiable.md) ensures types do real work — a type that doesn't enable specific operations is noise.

**Progressive compilation.** We stabilise LLM behaviour into code as patterns emerge — the same move as compiling: freezing a flexible representation into a rigid, efficient one. [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) frames this explicitly. The [verifiability gradient](./deploy-time-learning-the-missing-middle.md) maps the spectrum from prompt tweaks through evals to deterministic modules. Unlike compilation, stabilisation is projection from an underspecified spec — the natural-language specification admits multiple valid implementations, and committing to code means choosing one interpretation and fixing it in a language with precise semantics. Indeterminism adds noise on top (different runs may surface different interpretations), but the deeper operation is resolving the semantic ambiguity. The same pattern applies to [methodology enforcement](../claw-design/methodology-enforcement-is-stabilisation.md) — written instructions compile into skills, then hooks, then scripts — with the added insight that not all methodology should complete the trajectory.

**Testing.** We test prompts and templates the way we test code. But LLM-based systems are harder to test, and the two phenomena create different challenges. Execution indeterminism means the same input produces different outputs across runs — you need statistical testing over distributions, not assertion equality. Semantic underspecification means the spec itself admits multiple valid interpretations — you need to test whether the instructions are sufficiently constraining, not just whether individual outputs look right. The first challenge requires running N times and checking the distribution; the second requires inspecting the spec for ambiguity, consistency, and sufficient constraint. The [text testing pyramid](../claw-design/observations/automated-tests-for-text.md) sketches what this looks like concretely: deterministic checks at the base, LLM rubric grading in the middle, corpus compatibility at the top.

**Version control.** We version prompts, templates, and knowledge artifacts in git, treating them as source code. [Storing a specific LLM output](./storing-llm-outputs-is-stabilization.md) resolves the underspecification to a fixed interpretation — freezing one concrete value from the space the spec admits. Versioning the spec matters because regeneration is a new projection from the same underspecified spec — potentially a different interpretation, not a deterministic rebuild.

**Design for testability.** [Crystallisation chooses repo artifacts](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) as the substrate specifically because they're inspectable — any agent can diff, test, and verify them. Testability as a design property, applied to LLM output.

## The hard cases

Where prompts produce variable outputs, practices get harder, not just different. Testing is the clearest example, and it doubles the testing surface — but the two halves come from different phenomena.

**Indeterminism doubles the test runs.** The same prompt produces different outputs across runs due to sampling, so you can't assert equality — you test the distribution. This requires statistical techniques (run N times, check pass rates, set confidence thresholds) where traditional code needs a single assertion.

**Underspecification doubles the test targets.** In deterministic code there's no gap between what the code says and what it does, so you only test outputs. With natural-language specs, the instructions admit multiple valid interpretations — you need to test the instructions themselves (are they consistent? unambiguous? sufficiently constraining?) as well as the outputs. A prompt that consistently produces unwanted behavior isn't exhibiting noise; it's exhibiting a valid interpretation you didn't intend. The fix is rewriting the spec, not retrying.

The two phenomena compound: you're testing an underspecified specification executed by an indeterministic engine. Each requires different techniques — statistical testing for indeterminism, structural analysis for underspecification — and conflating them leads to misdiagnosis.

## Why the practices transfer

Both domains solve the same problems: making behaviour predictable, making systems composable, making artifacts verifiable. The underlying concepts (type theory, compilation, contracts) explain *why* a practice works in both settings. [Thalo](./related-systems/thalo.md) demonstrates the endpoint: a system that built a full compiler (Tree-Sitter grammar, LSP, 27 validation rules) for knowledge management, taking typing and testing to their logical extreme. [Crystallisation systematises these transfers](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the accumulated prompt adjustments, output post-processing, and workflow changes that every deployed system accumulates are exactly these programming practices applied informally. The motivation is practical — these are things we do, not abstractions we admire.

## Open Questions

- What other programming practices haven't been applied yet but could be? (Code review for prompts? Dependency injection for context? Refactoring patterns?)
- Where do the practices break down — which ones mislead when applied to systems with underspecified instructions?
- Can we develop prompt-native practices that have no programming equivalent?

---
Relevant Notes:
- [programming-language types applied to documents](./instructions-are-typed-callables.md) — typing practice applied to KB documents
- [document types should be verifiable](../claw-design/document-types-should-be-verifiable.md) — quality criterion for document types
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — conceptual foundation: underspecified vs precise semantics, stabilise/soften, spec-to-program projection
- [crystallisation: the missing middle](./deploy-time-learning-the-missing-middle.md) — progressive compilation in practice
- [stabilisation is learning](./agentic-systems-learn-through-three-distinct-mechanisms.md) — synthesizes: the informal programming practices accumulated by every deployed system are what crystallisation systematises
- [storing LLM outputs is stabilization](./storing-llm-outputs-is-stabilization.md) — version control practice applied to LLM outputs
- [inspectable substrate](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — design for testability applied to LLM artifacts
- [automated tests for text](../claw-design/observations/automated-tests-for-text.md) — extends the testing discussion: concrete test pyramid for the doubled testing surface this note identifies
- [methodology enforcement is stabilisation](../claw-design/methodology-enforcement-is-stabilisation.md) — extends: progressive compilation applied specifically to KB methodology, with a concrete gradient (instruction -> skill -> hook -> script) and the insight that judgment-requiring operations stay at skill level permanently

Topics:
- [learning-theory](./learning-theory.md)
- [computational-model](./computational-model.md)
