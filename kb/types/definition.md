---
type: kb/types/type-spec.md
name: definition
description: Operational vocabulary note that sharpens a term for KB use
schema: kb/types/definition.schema.yaml
---

# Definition

## Authoring Instructions

Use `definition` for KB vocabulary that needs a stable, operational meaning. A definition note is an explication: it replaces a vague, overloaded, or imported term with a sharper term that serves this KB's work.

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
- What does the term include here?
- What nearby meanings are excluded?
- What would count as misuse of the term?
- Which workflows, review gates, or recurring arguments depend on this meaning?

## Writing Constraints

- Do not write a philosophical survey unless the survey changes how agents should use the term.
- Do not define ordinary terms that are already unambiguous in context.
- Prefer short operational contrasts over exhaustive taxonomies.
- Link to related definition notes when the boundary matters.
- Use examples only when they sharpen future usage.

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

{What the term includes in this KB.}

## Exclusions

{Nearby meanings, ordinary uses, or misleading analogies that this term does not cover.}

## Misuse Cases

- {A plausible wrong use of the term and why it is wrong.}

---

Relevant Notes:

- [{related definition or note}](./related-note.md) -- {boundary or dependency}
```
