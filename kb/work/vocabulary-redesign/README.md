# Vocabulary Redesign

Workshop for redesigning the KB's vocabulary: the terms that appear in always-loaded context, definition notes, collection conventions, link labels, type names, and review/survey prose.

## Question

What vocabulary should commonplace ask every agent and maintainer to learn, and what should stay local to a note, collection, or workshop?

The current vocabulary is useful but has grown through local problem solving. Some terms are central and stable (`context engineering`, `distillation`, `constraining`, `codification`, `register`, `workshop`). Others may be overloaded, too abstract for always-loaded context, or split across link labels, type names, artifact roles, and review terminology. The redesign should keep the vocabulary small enough to teach, precise enough to guide writing and review, and operational enough to change agent behavior.

## Scope

In scope:

- Terms in the `AGENTS.md` Vocabulary section.
- Definition notes under `kb/notes/definitions/`.
- Link labels and relationship vocabulary in `kb/reference/link-vocabulary.md`.
- Artifact-role words used across notes, references, instructions, reviews, and source ingests.
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
- Are link labels organized around writer needs, reader needs, register boundaries, or artifact roles?
- Where do `memory`, `context`, `knowledge`, `artifact`, `system-definition`, `instruction`, `skill`, and `source` currently blur?

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
- [paper-vocabulary-deltas.md](./paper-vocabulary-deltas.md) — initial comparison between the paper's vocabulary and the KB's current vocabulary.
- [revision-plan.md](./revision-plan.md) — staged plan for moving from paper vocabulary to durable KB revisions.

## Closure

Close this workshop when there is a concrete vocabulary proposal with:

- keep / revise / demote / remove decisions for the always-loaded terms;
- a migration plan for affected notes and reference docs;
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
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — current workshop/library boundary.
