# Vocabulary Redesign

Workshop for redesigning the KB's vocabulary: the terms that appear in always-loaded context, definition notes, collection conventions, link labels, type names, and review/survey prose.

## Question

What vocabulary should commonplace ask every agent and maintainer to learn, and what should stay local to a note, collection, or workshop?

The current vocabulary is useful but has grown through local problem solving. Some terms are central and stable (`context engineering`, `distillation`, `constraining`, `codification`, `register`, `workshop`). The artifact-analysis redesign has now landed a second cluster: `retained artifact`, `operative part`, `storage substrate`, `representational form`, `lineage`, `behavioral authority`, `knowledge artifact`, and `system-definition artifact`. The remaining redesign work is no longer choosing between the paper vocabulary and the KB vocabulary; it is propagating the landed terms, retiring stale shorthand, and deciding which vocabulary rules belong in global, collection, and type-specific authoring paths.

## Scope

In scope:

- Terms in the `AGENTS.md` Vocabulary section.
- Definition notes under `kb/notes/definitions/`.
- Link labels and relationship vocabulary in `kb/reference/link-vocabulary.md`.
- Artifact-analysis words used across notes, references, instructions, reviews, and source ingests.
- Naming conventions for collections, types, traits, statuses, registers, and workshop/library boundaries.

Out of scope unless needed for a vocabulary decision:

- Rewriting all notes to match the new vocabulary.
- Changing validators, schemas, or generated indexes.
- Adding a new type system or ontology.

## Working Principles

- Prefer fewer terms with sharper boundaries over a larger taxonomy.
- A term earns always-loaded status only when misuse causes repeated bad decisions.
- Definition notes should explain operational consequences, not only prose meanings.
- Vocabulary changes should include migration notes: old term, new term, when to use each, and what existing artifacts need updates.
- Keep external-theory borrowings subordinate to local workflow needs.

## Initial Questions

- Which current terms are foundational enough to remain in `AGENTS.md`?
- Which terms should move from always-loaded vocabulary into on-demand definition notes?
- Are `distillation`, `constraining`, and `codification` still the right operator set, or do we need a clearer hierarchy?
- Does `register` still belong as a primary term, or should collection-level roles be named differently?
- Are link labels organized around writer needs, reader needs, register boundaries, or artifact-analysis fields?
- Where do `memory`, `context`, `knowledge`, `retained artifact`, `system-definition artifact`, `instruction`, `skill`, and `source` still blur?

## Current Landing

The redesign has adopted the artifact-analysis vocabulary in durable notes and always-loaded context:

| Adopted term | Replaces or sharpens |
|---|---|
| `retained artifact` | persistent adaptive artifact / adaptive artifact |
| `operative part` | whole-object classification when only part of a stored object shapes behavior |
| `storage substrate` | backend / storage class |
| `representational form` | artifact class / prose-symbolic-opaque shorthand |
| `lineage` | source relation / provenance needed for invalidation and regeneration |
| `behavioral authority` | role / control path / future system use |
| `knowledge artifact` | knowledge role or low-authority knowledge use |
| `system-definition artifact` | system-definition role or high-authority system use |

Important non-landings:

- `artifact-use pairing` was the transitional bridge; it is now mostly decomposed into retained artifact, operative part, and behavioral authority.
- `future system use` was folded into behavioral authority and consumption path language.
- `eligibility` remains useful local lifecycle vocabulary, but it is not one of the four core artifact-analysis fields.
- `persistent adaptive artifact` remains paper-facing vocabulary, not the internal hot-path term.

## Outputs

Candidate durable outputs:

- Revised `AGENTS.md` Vocabulary section.
- Updated definition notes or new definition notes.
- A vocabulary migration note under `kb/reference/` or `kb/notes/`.
- Revisions to `kb/reference/link-vocabulary.md`.
- Review gates or validation warnings if a term boundary can be checked.

## Working Files

- [persistent-adaptive-artifacts-focused-draft.md](./persistent-adaptive-artifacts-focused-draft.md) — copied paper draft whose vocabulary revises several KB terms.
- [inventory.md](./inventory.md) — current KB vocabulary inventory and audit questions.
- [paper-vocabulary-deltas.md](./paper-vocabulary-deltas.md) — historical comparison between the paper's vocabulary and the now-landed KB terms.
- [revision-plan.md](./revision-plan.md) — updated propagation plan for the landed vocabulary.

## Closure

Close this workshop when there is a concrete vocabulary proposal with:

- keep / revise / demote / remove decisions for the always-loaded terms, including the artifact-analysis cluster;
- a propagation plan for affected notes, reference docs, instructions, and review type specs;
- explicit open questions left for later rather than hidden in the vocabulary.

## Grounding

- [AGENTS.md](../../../AGENTS.md) — current always-loaded vocabulary and operating contract.
- [Control-plane goals](../../reference/control-plane-goals.md) — explains why vocabulary can live in always-loaded context.
- [Link vocabulary](../../reference/link-vocabulary.md) — current catalogue for relationship labels.
- [Register](../../notes/definitions/register.md) — current definition of theoretical/descriptive/prescriptive content modes.
- [Context engineering](../../notes/definitions/context-engineering.md) — current definition of the central domain term.
- [Distillation](../../notes/definitions/distillation.md) — current definition of directed context compression.
- [Constraining](../../notes/definitions/constraining.md) — current definition of narrowing interpretation space.
- [Codification](../../notes/definitions/codification.md) — current definition of the far end of constraining.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) — landed vocabulary for retained artifacts, operative parts, storage substrate, representational form, lineage, and behavioral authority.
- [Memory design adds operational axes to artifact analysis](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — companion note separating artifact fields from memory operational policies.
- [Retained artifact](../../notes/definitions/retained-artifact.md) — current definition of retained behavior-shaping state.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — current replacement for loose role/control-path shorthand.
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — current workshop/library boundary.
