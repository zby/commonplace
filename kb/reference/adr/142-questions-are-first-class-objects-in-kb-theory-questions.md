---
description: "Decision that recurring theoretical questions are first-class addressable objects in kb/theory/questions/, acting as thinking starting points beside claims while deferring a dedicated question type"
type: reference/types/adr.md
tags: []
status: accepted
---

# 142-Questions are first-class objects in kb/theory/questions

**Status:** accepted
**Date:** 2026-11-27

## Context

Commonplace's Popperian inquiry schema (`P1 → TT → EE → P2`, [tentative theory](../../theory/definitions/tentative-theory.md)) treats problems as the starting point for tentative theories and error elimination, yet `kb/theory/` held first-class files only for claims, definitions, evidence, and unadopted proposals.

The forces that would recur if questions were not first-class objects in `kb/theory/`:

- **No shared root for competing or partial answers.** Claim-first organization hides which recurring problem multiple claims address, makes top-level answering notes look orphaned in `kb/theory/` when no other claim cites them, and leaves tightly linked claim clusters without a root problem anchoring their inquiry.
- **Collection mismatch in `kb/notes/`.** [kb/notes/COLLECTION.md](../../notes/COLLECTION.md) governs short, static replies and examples where no further work is expected. Living standing queries evolve as new theory claims and evidence arrive, and their outbound links from `kb/notes/` do not count as inbound links inside `kb/theory/`.
- **Tags and inline `## Open Questions` solve different jobs.** Tags (`kb/tags/`) group by broad topic rather than a specific problem situation, while inline `## Open Questions` sections record local gaps scoped to a single claim rather than cross-cutting roots that organize multiple tentative answers.

## Decision

**Questions are first-class addressable objects in `kb/theory/questions/`.** A standing question lives as its own Markdown artifact inside `kb/theory/questions/`, an area of the `kb/theory/` collection, serving as a thinking and reading starting point beside claims.

A question artifact frames a recurring theoretical problem, its stakes, the current tentative answers (linking to the claims, evidence, and neighboring notes that bear on it), and what remains unsettled. Unlike a task or backlog item, a core question survives as a durable root when tentative answers improve, narrow, or fail; it narrows or retires when the problem dissolves or a validated mechanism closes the inquiry.

**Placement rules live in `kb/theory/COLLECTION.md`; `kb/theory/questions/README.md` is navigation only** ([ADR 084](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)). Questions are exempt from `kb/theory/`'s claim-title and claim-modality rules while remaining subject to its source-grounding limit, linking rules, and standard tag-assignment rules (so tag pages surface organizing questions alongside the claims that answer them).

**Dedicated `question` type deferred.** Questions remain on `type: types/note.md` until enough examples accumulate to test whether the prototype structure (`Stakes`, `Current answer`, `Unsettled`) warrants its own type spec and schema.

**Boundary with adjacent surfaces:**

- Inline `## Open Questions` on a note stays for local gaps owned by that single claim.
- `kb/notes/` stays for short, static replies, examples, and comparisons usable as written with no expected ongoing revision.
- `kb/work/` stays for active investigations, drafts, and trials.
- `kb/theory/proposals/` stays for finished unadopted theory waiting on an adoption decision.

## Considered alternatives

**Keep standing queries in `kb/notes/`.** Avoids adding a subdirectory to `kb/theory/` and matches `kb/notes/`'s question-title convention. Rejected because `kb/notes/` is contracted for static replies needing no further work, and links from `kb/notes/` stay outside `kb/theory/`'s inbound-link graph so answering theory notes still appear orphaned.

**Create a new top-level `kb/questions/` collection.** Gives questions their own `COLLECTION.md` and top-level navigation entry. Rejected under [why directories despite their costs](../../theory/why-directories-despite-their-costs.md): top-level collections carry registration, navigation, and contract overhead, whereas recurring theoretical questions share `kb/theory/`'s grounding bound, linking vocabulary, and graph neighborhood. Reconsider if non-theory questions need a distinct collection contract.

**Define a dedicated `kb/theory/types/question.md` type spec now.** Enforces section structure and frontmatter immediately through type-conformance review and schema validation. Deferred as a free choice left open: with only two prototypes, locking in required headings risks premature entrenchment ([current-task fit alone does not warrant costly structural entrenchment](../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)).

**Rely on tags and inline `## Open Questions` alone.** Adds no new directory or placement rule. Rejected because tags express topical membership rather than a problem situation with stakes and rival answers, and inline `## Open Questions` cannot anchor multiple claims to one shared root question.

**Free choices left open.** The prototype section layout (`Stakes`, `Current answer`, `Unsettled`) remains an informal convention rather than a schema obligation, and whether validation should distinguish question-sourced inbound links from claim-sourced inbound links is left open until practice shows what helps.

## Consequences

**Easier.** Authors and readers can enter the theory graph from recurring problems as well as from claims. Top-level theory notes cited by a standing question gain inbound links inside `kb/theory/`. `kb/notes/` remains focused on short static replies, and `kb/theory/questions/` keeps question artifacts separate from the root `kb/theory/` claim listing.

**Harder or riskier.** Without a dedicated `question` type spec, structural consistency across question notes is enforced by authoring discipline rather than schema or type-conformance review. If the admission bar weakens, `kb/theory/questions/` could accumulate unframed one-line prompts or duplicate local `## Open Questions` sections.

**Operativity path.** Authors and collection-conformance reviewers consume the placement boundary and claim-title exception through [kb/theory/COLLECTION.md](../../theory/COLLECTION.md) with binding authoring and review-gate force. `commonplace-validate kb/theory` checks frontmatter, links, and `unquoted-source-limit` across `kb/theory/questions/` and counts its links within `kb/theory/`'s inbound-link graph. ProperDocs renders `kb/theory/questions/README.md` and its build-time `dir-index.md` through the existing `index_directory` and `properdocs_hooks` pipeline with no code changes. No type-conformance gate enforces question-specific sections until a `question` type is adopted.

**Limits.** This decision applies to recurring theoretical questions inside Commonplace's `kb/theory/` collection. It does not adopt a `question` type spec or schema, does not scaffold a `questions/` directory via `commonplace-init` for installed host projects, and does not replace single-note `## Open Questions` sections, `kb/log.md` observations, or `kb/work/` workshops.

---

Relevant Notes:

- [Tentative theory](../../theory/definitions/tentative-theory.md) — rests-on: Popper's `P1 → TT → EE → P2` schema placing problems alongside tentative theories and error elimination
- [Why directories despite their costs](../../theory/why-directories-despite-their-costs.md) — rests-on: subdirectories within a collection are cheap when separated by role and metabolic rate, whereas top-level collections carry registration cost
- [ADR 084: kind rules live in type specs and operations in instructions](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) — part-of: keeps binding placement rules in `kb/theory/COLLECTION.md` and keeps `kb/theory/questions/README.md` navigation-only
- [Current-task fit alone does not warrant costly structural entrenchment](../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — rests-on: justifies deferring a dedicated `question` type spec while the section structure is still prototyping
- [How do we value notes?](../../theory/questions/how-do-we-value-notes.md) — see-also: one of the two initial standing queries motivating query-centered root nodes in `kb/theory/`
