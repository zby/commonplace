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
- Do not define ordinary terms that are already unambiguous in context.
- Prefer short operational contrasts over exhaustive taxonomies.
- Link to related definition notes when the boundary matters.
- Use examples only when they sharpen future usage.
- Keep technique guidance subordinate to term guidance. If a section mainly says when or how to perform an operation, move it to an instruction, ADR, workshop, or ordinary note and link it.

## Template

```markdown
---
description: Definition -- {term} means {operational meaning and why it matters}
type: kb/types/definition.md
tags: []
status: seedling
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
