---
description: When a new requirement doesn't fit existing types or skills, writing an ad hoc instructions note absorbs it without any schema change — the collections problem is a concrete example
type: note
traits: []
areas: [claw-design, learning-theory]
status: seedling
---

# Ad hoc prompts extend the system without schema changes

A claw has a deterministic base — files, directories, types, frontmatter schemas, validation scripts — and a prompt layer on top. The prompt layer is where new requirements get absorbed without changing the base.

The mechanism: when a requirement doesn't fit existing types or skills, you write an instructions note — a markdown file that tells an agent what to do. No code, no schema change, no registration. The system's vocabulary grows at the speed of writing, not the speed of coding.

## The collections example

We needed "read multiple documents through one goal." Three formal options presented themselves:

1. A new `collection` type with a schema for listing document paths
2. A file-listing format (one path per line)
3. A directory glob pattern

Each would require defining structure, adding validation, updating the type taxonomy. Instead: write an instructions note that lists the documents, says what to look for in each, and explains why they're together. The "collection" is a paragraph. It's also *better* than a formal type because it carries context a schema couldn't — why these documents are grouped, what's relevant in each one, what the goal is.

The formal system didn't grow. A prompt absorbed the requirement.

## Where this sits on the stabilisation spectrum

[Methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) describes a gradient: instructions → skills → hooks → scripts. Each step trades flexibility for reliability. Ad hoc instructions notes sit at the loosest end — maximally flexible, zero infrastructure cost, but also zero validation and zero reuse.

[Instructions are typed callables](./instructions-are-typed-callables.md) argues for the other end: declare type signatures, validate inputs, make skills composable. Both are correct for different moments. The typed-callable view is right for operations that recur — `/connect`, `/validate`, `/ingest`. The ad hoc view is right for operations that might happen once, or whose shape isn't clear yet.

The stabilisation direction is: write ad hoc instructions first, notice when you're writing the same kind of instructions repeatedly, extract a skill. This is the prompt equivalent of "write the code three times, then extract a function." The instructions note is the prototype; the skill is the extraction.

## Why prompts carry what types can't

The reason ad hoc instructions resist premature formalisation isn't just convenience — it's that prompts carry judgment that type signatures can't express. A prompt can say "focus on sections 3.1-3.3" or "the key tension is between X and Y." A type signature says `source → report`. The prompt carries the caller's judgment, not just the caller's data.

This matters most for sub-agent handoff. An instructions note is a clean context boundary: the caller does the judgment-heavy work (gathering, selecting, deciding what matters) and writes it all down. The sub-agent executes with clean context — no conversation history, no search, no decisions about what's relevant. The instructions note is the interface, and it's richer than any type signature could be.

## Precedents: Lisp, Emacs, Smalltalk

This pattern has deep roots in systems designed for user-level extension.

**Lisp's homoiconicity.** In Lisp, code and data share the same representation — lists. A list is both a data structure you can inspect and a program you can evaluate. In the claw, a markdown file is both content you can read/link/analyze and instructions you can hand to a sub-agent for execution. The power comes from *not* having a rigid boundary between the language and what it operates on. Lisp macros — code that writes code — map to instructions that produce reports containing further instructions. Quote/eval — toggling between treating something as data vs executing it — maps to reading an instructions note vs handing it off.

**Emacs as ad hoc extension culture.** Emacs is written in Elisp — the system and its extension language are the same thing, so there's literally no boundary between built-in functionality and user extensions. Every user is potentially a programmer. The init file mixes configuration and ad hoc programs — inline `defun`, one-off lambdas bound to keys — and the line between "configuring Emacs" and "programming Emacs" doesn't exist. The stabilisation trajectory is the same: inline snippet in init.el → extracted function → published package. The claw's equivalent: ad hoc instructions note → extracted skill → registered tool.

**Smalltalk's live image.** Smalltalk completes the picture: the image is both the program and the development environment, and you modify the running system from inside itself using the same language. Lisp, Emacs, and Smalltalk all share the property that the system is written in its own extension language. The claw has the same property — its methodology is written in the same markdown it operates on.

The common thread: systems that blur the boundary between using and extending are more adaptable than systems with rigid extension points. The cost is discoverability — Emacs's `.emacs` files are notoriously personal and opaque, Lisp macros can make code unreadable, and ad hoc instructions notes are invisible unless you know they exist.

## Open Questions

- When does an ad hoc instructions note become expensive enough to justify extracting a skill? Is "wrote the same kind three times" the right threshold?
- Can instructions notes reference skills ("follow the directed reading procedure, but also..."), or does that create confusing layering?
- How do you discover useful past instructions notes? They're ephemeral by design, but some patterns are worth finding again.

---

Relevant Notes:
- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — the typed end of the spectrum: skills should declare signatures. This note argues for the untyped end — ad hoc instructions that absorb requirements without schema changes. Both are correct for different moments.
- [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) — foundation: the gradient from instructions to scripts. Ad hoc instructions notes are the loosest point on this gradient.
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — extends: this note adds a practice that goes the other direction — sometimes staying at the prompt level is the right choice, not a failure to compile
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: unified calling conventions make it possible to start with a prompt and later extract to a skill without changing call sites
- [a-functioning-claw-needs-a-workshop-layer-not-just-a-library](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — extends: the workshop layer is where ad hoc instructions live; the library is where they stabilise into skills

Topics:
- [claw-design](./claw-design.md)
- [learning-theory](./learning-theory.md)
