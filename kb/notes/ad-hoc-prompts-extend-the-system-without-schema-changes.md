---
description: Any system with an LLM agent layer can absorb new requirements through natural language prompts without changing the deterministic base
type: note
traits: []
tags: [learning-theory]
status: seedling
---

# Ad hoc prompts extend the system without schema changes

Any system with an LLM agent layer has two strata: a deterministic base (files, schemas, scripts, APIs) and a prompt layer on top. The prompt layer is where new requirements get absorbed without changing the base.

The mechanism: when a requirement doesn't fit existing code or configuration, you write a natural language prompt — a markdown file, a comment, a task description — that tells the agent what to do. No code change, no schema migration, no deployment. The system's vocabulary grows at the speed of writing, not the speed of coding.

This applies everywhere agents operate. A CI pipeline gains a new check by adding a prompt to the agent's instructions, not by writing a new GitHub Action. A codebase gains a new review criterion by describing it in CLAUDE.md, not by writing a linter rule. A deployment process gains a new safety check by telling the agent "also verify X before pushing," not by adding a pre-deploy hook.

We first noticed this in the KB, where it shows up cleanly.

## The KB example: collections

We needed "read multiple documents through one goal." Three formal options presented themselves:

1. A new `collection` type with a schema for listing document paths
2. A file-listing format (one path per line)
3. A directory glob pattern

Each would require defining structure, adding validation, updating the type taxonomy. Instead: write an instructions note that lists the documents, says what to look for in each, and explains why they're together. The "collection" is a paragraph. It's also *better* than a formal type because it carries context a schema couldn't — why these documents are grouped, what's relevant in each one, what the goal is.

The formal system didn't grow. A prompt absorbed the requirement.

## The constraining spectrum

Ad hoc prompts sit at the loosest end of the [enforcement gradient](./methodology-enforcement-is-constraining.md): instructions → skills → hooks → scripts. Maximally flexible, zero infrastructure cost, but also zero validation and zero reuse. [Typed callables](./instructions-are-typed-callables.md) sit at the other end — declared signatures, validated inputs, composable skills. Both are correct for different moments. Typed callables are right for operations that recur (`/connect`, `/validate`, `/ingest`). Ad hoc prompts are right for operations that might happen once, or whose shape isn't clear yet.

The maturation trajectory is: write ad hoc prompts first, notice when you're writing the same kind repeatedly, extract a skill. The prompt equivalent of "write the code three times, then extract a function." This is [lowest-friction capture, then progressive refinement](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) applied to the skill layer. The extraction step itself is [distillation](./skills-derive-from-methodology-through-distillation.md) — the ad hoc prompt carries reasoning about what to do and why; the extracted skill keeps the procedure and drops the justification.

## Prompts carry what types can't

Prompts carry judgment that type signatures can't express. A prompt can say "focus on sections 3.1-3.3" or "the key tension is between X and Y." A type signature says `source → report`. The prompt carries the caller's judgment, not just the caller's data. This is why ad hoc prompts resist premature formalisation — not convenience, but expressiveness.

This matters most for sub-agent handoff. An ad hoc prompt is a clean context boundary: the caller does the judgment-heavy work (gathering, selecting, deciding what matters) and writes it down. The sub-agent executes with clean context — no conversation history, no search, no decisions about what's relevant. The prompt defines what's visible in the sub-agent's [lexically scoped frame](./llm-context-is-composed-without-scoping.md), and the sub-agent inherits nothing beyond what the caller explicitly passed.

## Why this works: homoiconicity

Ad hoc extension without schema changes is possible because the [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — instructions and content share the same representation (natural language tokens). A markdown file is both content you can read/link/analyze and instructions you can hand to a sub-agent for execution. A CLAUDE.md rule is both documentation for humans and a behavioral constraint for agents. No registration, no type system gatekeeping, no compilation step. This is the same property that makes Lisp, Emacs, and Smalltalk extensible from within — and carries the same discoverability costs.

## Open Questions

- When does an ad hoc prompt become expensive enough to justify extracting a skill or writing code? Is "wrote the same kind three times" the right threshold, or does it depend on how costly a mistake is?
- Can ad hoc prompts reference skills ("follow the directed reading procedure, but also..."), or does that create confusing layering?
- How do you discover useful past ad hoc prompts? They're ephemeral by design, but some patterns are worth finding again.
- Outside KBs, what are the best examples of this pattern? CLAUDE.md rules, PR description templates, agent system prompts — are these all instances of the same technique?

---

Relevant Notes:

- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — the typed end of the spectrum: skills should declare signatures. This note argues for the untyped end — ad hoc instructions that absorb requirements without schema changes. Both are correct for different moments.
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — foundation: the gradient from instructions to scripts. Ad hoc instructions notes are the loosest point on this gradient.
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — extends: this note adds a practice that goes the other direction — sometimes staying at the prompt level is the right choice, not a failure to compile
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: unified calling conventions make it possible to start with a prompt and later extract to a skill without changing call sites
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: the workshop layer is where ad hoc instructions live; the library is where they constrain into skills
- [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — grounds: ad hoc instructions are the wikiwiki principle applied to the skill layer — lowest-friction capture first, progressive refinement into skills as patterns emerge
- [skills-derive-from-methodology-through-distillation](./skills-derive-from-methodology-through-distillation.md) — enables: the extraction from ad hoc instructions to skills is distillation — keeping procedures, factoring out the discursive reasoning that produced them
- [llm-context-is-composed-without-scoping](./llm-context-is-composed-without-scoping.md) — grounds: ad hoc instructions notes are effective sub-agent interfaces because they provide lexically scoped frames — the sub-agent sees only what the caller explicitly passed
