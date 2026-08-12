---
description: "LLMs interpret instructions and content through one token medium, enabling natural-language artifacts to alter behavior without translation while requiring architecture to enforce role, scope, and authority boundaries"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# LLM contexts interpret instructions and content through the same token medium

Chat protocols distinguish system, user, assistant, and tool roles, and delimiters can label quoted material. Those markers affect how the model interprets text, but they do not create an interpreter-enforced program/data boundary. Once instructions and content enter the context, both are token sequences processed by the same learned interpreter. The same Markdown file can be evidence to analyze in one authority path and an instruction to follow in another.

This shared medium cuts both ways. It lets natural-language artifacts change behavior without translation into a separate extension language. It also lets content imitate instructions, so the surrounding architecture must reimpose the role, scope, and authority boundaries that the medium itself does not enforce.

## A bounded homoiconicity analogy

Lisp is useful as a partial analogy. In Lisp, programs and data share the same list structure, while quote, evaluation, and macros define explicit ways to move between those roles. LLM context resembles this arrangement in one limited respect: a Markdown file can be loaded as content or as instruction without changing format.

The analogy is limited. LLM contexts do not provide Lisp's structural syntax or evaluation semantics. The protocol and orchestrator decide which text carries authority, and the model interprets the resulting context. Here, *homoiconic* names only the resemblance created by cheap role change within one representational medium, not a strict programming-language classification.

## Low-friction extension

The shared medium removes a translation and registration boundary. Because an LLM can interpret new free-form instructions, a system can [absorb a requirement in a prompt without changing its schema](./ad-hoc-prompts-extend-the-system-without-schema-changes.md). A Markdown rule can remain readable documentation while also becoming a behavioral specification when an authorized caller loads it.

The benefit is narrower than "natural language is enough." Natural-language competence and permissive orchestration are also required, and a system can accept new natural-language tasks while still keeping instructions and payloads in separate fields. The specific benefit here is lower local extension cost: the same artifact can move between documentation and behavior without format conversion. That does not guarantee validation, reliability, reuse, or broad expressiveness.

## Boundary costs

Role markers remain evidence the model interprets unless architecture makes their consequences binding. That creates three distinct costs:

**Scope contamination.** [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md): text retained from an earlier computation can influence a later task because both remain available to the same attention process. Role tags and delimiters can reduce confusion, but they do not remove the text or make its scope binding.

**Authority confusion and prompt injection.** Content can contain instruction-like text. If the consumption path gives that text behavioral force, data has crossed into instruction without changing representation. The vulnerability therefore depends on both the shared medium and an authority path that fails to preserve the intended role.

**Discoverability.** When behavioral specifications live in ordinary prose files, the operative system is distributed across artifacts that also look like documentation. Without routing, indexing, or registration, it becomes hard to tell which text actually changes behavior.

[Constraining](./methodology-enforcement-is-constraining.md)—narrowing the range of valid interpretations—is the architectural response. Moving recurring requirements from instructions toward schemas and scripts gives symbolic interpreters the authority and scope rules that the natural-language medium itself does not enforce.

---

Relevant Notes:

- [Ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — exemplifies: shared representation lowers the cost of turning a natural-language artifact into behavior
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — exemplifies: one attention process provides no binding boundary against scope contamination
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: learned interpretation makes both natural-language extension and role confusion possible
- [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — applies: one interface can resolve names to neural or symbolic implementations
- [Programming practices apply to prompting](./underspecification-and-indeterminism-complicate-programming-for.md) — context: typing, testing, and compilation compensate for structure the shared natural-language medium lacks
- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — grounds: moving from instruction to script imposes interpreter-enforced boundaries
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — intensified by: instructions and content compete within the same bounded context
