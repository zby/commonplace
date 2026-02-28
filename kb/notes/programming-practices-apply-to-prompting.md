---
description: Programming practices — typing, testing, progressive compilation, version control — apply to LLM prompting and knowledge systems, with probabilistic execution making some practices harder
type: note
areas: [learning-theory]
status: speculative
---

# Programming practices apply to prompting

Much of what we do in llm-do and this knowledge base is applying established programming practices to prompts, documents, and LLM workflows. The transfers are practical and actionable. Probabilistic execution makes some practices harder than their deterministic originals.

## Practices we apply

**Typing.** We assign types to documents to mark what operations they afford — a `claim` can be verified, a `spec` can be implemented, `instructions` can be followed. This is the same practice as typing values in code: [the type determines valid operations](./instructions-are-typed-callables.md). The [verifiability criterion](../claw-design/document-types-should-be-verifiable.md) ensures types do real work — a type that doesn't enable specific operations is noise.

**Progressive compilation.** We stabilise LLM behaviour into code as patterns emerge — the same move as compiling: freezing a flexible representation into a rigid, efficient one. [agentic systems are probabilistic programs](./agentic-systems-are-probabilistic-programs.md) frames this explicitly. The [verifiability gradient](./deploy-time-learning-the-missing-middle.md) maps the spectrum from prompt tweaks through evals to deterministic modules. Unlike compilation, stabilisation is stochastic projection — each run samples a different valid implementation. The same pattern applies to [methodology enforcement](../claw-design/methodology-enforcement-is-stabilisation.md) — written instructions compile into skills, then hooks, then scripts — with the added insight that not all methodology should complete the trajectory.

**Testing.** We test prompts and templates the way we test code. But because prompts are probabilistic, this is harder: you have two testing surfaces instead of one. You test outputs (does the distribution of results meet expectations?) and you test the instructions themselves (are they consistent? unambiguous? sufficiently constraining?). The second surface exists because probabilistic execution creates a gap between what instructions say and what they produce — a gap that doesn't exist in deterministic code. The [text testing pyramid](../claw-design/observations/automated-tests-for-text.md) sketches what this looks like concretely: deterministic checks at the base, LLM rubric grading in the middle, corpus compatibility at the top.

**Version control.** We version prompts, templates, and knowledge artifacts in git, treating them as source code. [Storing a specific LLM output](./storing-llm-outputs-is-stabilization.md) collapses a distribution to a point — freezing a value. Versioning the spec matters because regeneration is a new sample, not a deterministic rebuild.

**Design for testability.** [Crystallisation chooses repo artifacts](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) as the substrate specifically because they're inspectable — any agent can diff, test, and verify them. Testability as a design property, applied to LLM output.

## The hard cases

Where prompts are probabilistic, practices get harder, not just different. Testing is the clearest example: in deterministic code there's no gap between what the code says and what it does, so you only test outputs. With prompts, the instructions define a distribution — you need to test both the distribution (output quality across runs) and the instructions (structural quality of the prompt itself). This doubles the testing surface and requires different techniques for each.

## Why the practices transfer

Both domains solve the same problems: making behaviour predictable, making systems composable, making artifacts verifiable. The underlying concepts (type theory, compilation, contracts) explain *why* a practice works in both settings. [Thalo](./related-systems/thalo.md) demonstrates the endpoint: a system that built a full compiler (Tree-Sitter grammar, LSP, 27 validation rules) for knowledge management, taking typing and testing to their logical extreme. [Crystallisation systematises these transfers](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the accumulated prompt adjustments, output post-processing, and workflow changes that every deployed system accumulates are exactly these programming practices applied informally. The motivation is practical — these are things we do, not abstractions we admire.

## Open Questions

- What other programming practices haven't been applied yet but could be? (Code review for prompts? Dependency injection for context? Refactoring patterns?)
- Where do the practices break down — which ones mislead when applied to probabilistic systems?
- Can we develop prompt-native practices that have no programming equivalent?

---
Relevant Notes:
- [programming-language types applied to documents](./instructions-are-typed-callables.md) — typing practice applied to KB documents
- [document types should be verifiable](../claw-design/document-types-should-be-verifiable.md) — quality criterion for document types
- [agentic systems are probabilistic programs](./agentic-systems-are-probabilistic-programs.md) — conceptual foundation: probabilistic programs, stabilise/soften, program sampling
- [crystallisation: the missing middle](./deploy-time-learning-the-missing-middle.md) — progressive compilation in practice
- [stabilisation is learning](./agentic-systems-learn-through-three-distinct-mechanisms.md) — synthesizes: the informal programming practices accumulated by every deployed system are what crystallisation systematises
- [storing LLM outputs is stabilization](./storing-llm-outputs-is-stabilization.md) — version control practice applied to LLM outputs
- [inspectable substrate](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — design for testability applied to LLM artifacts
- [automated tests for text](../claw-design/observations/automated-tests-for-text.md) — extends the testing discussion: concrete test pyramid for the doubled testing surface this note identifies
- [methodology enforcement is stabilisation](../claw-design/methodology-enforcement-is-stabilisation.md) — extends: progressive compilation applied specifically to KB methodology, with a concrete gradient (instruction -> skill -> hook -> script) and the insight that judgment-requiring operations stay at skill level permanently

Topics:
- [learning-theory](./learning-theory.md)
