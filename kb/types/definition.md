---
type: kb/types/type-spec.md
name: definition
description: Operational vocabulary note that sharpens a term for KB use
schema: kb/types/definition.schema.yaml
---

# Definition

## Authoring Instructions

Use `definition` for KB vocabulary that needs a stable, operational meaning. A definition note is an explication: it replaces a vague, overloaded, or imported term with a sharper term that serves this KB's work.

Definition notes are constraining artifacts for language. They narrow future interpretation, state what a term does and does not cover, and give later notes a stable link target instead of forcing each author to redefine the term locally. Their primary question is vocabulary: when should this word apply?

A definition note is not an operating manual for the technique the term names. It may include brief practical context when that context explains the boundary of the term, but detailed advice about when, whether, or how to perform the technique belongs in an instruction, ADR, workshop, or ordinary note linked from the definition.

## When To Create One

Create a definition note when the KB needs a low-cost canonical gloss that also narrows interpretation. The economic test is context cost: if the best existing target is too long, too argumentative, or too multi-purpose to load just to understand the term, split out a definition and link the developed artifact for the argument, mechanism, or procedure.

A separate definition is especially justified when the term appears across multiple workflows or notes, when misuse is plausible, or when nearby concepts need a stable boundary. Do not create one merely because the term is important; ordinary notes can serve as glossary targets while they remain cheap and focused enough for that job.

## Explication Frame

Use Carnap's explication criteria pragmatically:

- Start from the explicandum: the ordinary, overloaded, or borrowed term that needs sharpening.
- State the explicatum: the technical meaning this KB will use.
- Preserve enough similarity that existing usage remains recognizable.
- Increase exactness by naming boundaries, exclusions, and misuse cases.
- Increase fruitfulness by showing what workflows, notes, or decisions the term enables.
- Keep the definition as simple as the operational purpose allows.

## Definition Body

A good definition note should answer:

- What problem does this term solve for the KB?
- When should authors use this term?
- What does the term include here?
- What nearby meanings are excluded?
- What would count as misuse of the term, not merely misuse of the underlying technique?
- Which workflows, review gates, or recurring arguments depend on this meaning?

## Writing Constraints

- Do not write a philosophical survey unless the survey changes how agents should use the term.
- Do not define ordinary terms that are already unambiguous in context or already have a cheap, focused glossary target.
- Prefer short operational contrasts over exhaustive taxonomies.
- Link to related definition notes when the boundary matters.
- Use examples only when they sharpen future usage.
- Keep technique guidance subordinate to term guidance. If a section mainly says when or how to perform an operation, move it to an instruction, ADR, workshop, or ordinary note and link it.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Retrieval description naming the term and the operational meaning this KB assigns it. |
| `type` | Yes | `kb/types/definition.md`. |
| `tags` | No | Navigation tags for the concept area the term belongs to. |
| `user-verified` | No | Optional explicit human attestation; may only be `true` and must be removed after substantive edits. |

## Template

```markdown
---
description: Definition -- {term} means {operational meaning and why it matters}
type: kb/types/definition.md
tags: []
---

# {Term}

{One-paragraph operational definition. Name the sharpened meaning and why this KB needs it.}

## Scope

{When to use this term in this KB; what cases fall inside the term.}

## Exclusions

{Nearby meanings, ordinary uses, or misleading analogies that this term does not cover.}

## Misuse Cases

- {A plausible wrong use of the term and why it is wrong. Do not list merely bad uses of the technique.}

---

Relevant Notes:

- [{related definition or note}](./related-note.md) -- {boundary or dependency}
```
