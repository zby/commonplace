# Retire profiles in favour of collection prototypes

## Status

Decided in direction, not executed. This is the **first** step of the vocabulary cleanup and is deliberately scoped to exclude relocating `text-contract`, which stays where it is and stays open as [its own task](./text-contract-and-profiles.md).

## The move

1. Create a `collection prototype` definition in `kb/reference/` — a starting contract a new collection copies, not a contract any collection is under.
2. Retire `profile` as registered vocabulary: no longer a named bundle a collection "adopts, extends, or replaces".
3. Remove the profile gloss from the always-loaded `AGENTS.md` vocabulary list, and drop the `Role` column from its collection routing table.
4. Edit `kb/notes/definitions/text-contract.md` in place: extract all profile-related content from its frontmatter and body, moving or recasting any material still needed for collection prototypes into the replacement reference artifact(s). Do not move, rename, or delete `text-contract.md`; preserve its text-contract definition at its current path.

## Why this is separable from the text-contract home question

The open task asks which artifact should own the *text contract* vocabulary and where it lives. That question is about placement under the belief/choice rule and carries 30 backlinks across 22 files.

Retiring profiles is a different question with a different answer: the concept is not misplaced, it is misdescribed. It is presented as a contract feature bundle and behaves as a starting template. Fixing the description does not require settling where the neighbouring term lives, and settling the neighbouring term does not fix the description. Doing the cheaper, independently-correct one first also shrinks the second: once profiles are gone, `text-contract.md` loses its largest section and the relocation options change shape.

## Findings that justify it

**Profiles bind nothing at use time.** Every live `COLLECTION.md` restates its contract in full locally. `kb/reference/COLLECTION.md` spells out its own quality goal ("fidelity + economy"), economy tests, fidelity constraint, title conventions, complete label table, and type table. Nothing is inherited. At the moment an agent reads a collection contract to act, the profile name is a family-resemblance label carrying no force — while its definition sits in always-loaded context and in the theoretical collection, both of which advertise it as live vocabulary.

**The abstraction is real but fires once.** `descriptive` has four realizations — `kb/reference/`, `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/sources/` — so it does generalize across collections. It just does its work at collection-creation time and never again. That is prototype semantics: delegate to get started, then own your copy.

**ADR 042 already implies it.** Its worked-case-first promotion rule means a profile is named only after a real collection demonstrates it. A bundle extracted from an instance and copied by later instances is a prototype, whatever it is called.

**The always-loaded cost is unearned.** The routing table reads `| Path | Role | Use when |`. Agents route on `Use when`; `Role` repeats the profile name in the most expensive context slot in the repository, and it is the surface that invites reading profiles as binding.

## Migration inventory

Roughly 23 library files name a text-contract profile. `src/` is unaffected — `TypeProfile` in `type_resolver.py` is unrelated type-resolution vocabulary, and the broad `rg` hit count across `kb/` is dominated by ordinary-English "profile" in external-system reviews and workshop files.

- `AGENTS.md` — vocabulary entry and routing-table `Role` column.
- Seven collection contracts declaring a profile in their heading and opening line: `notes`, `reference`, `instructions`, `agentic-systems`, `agent-memory-systems`, `sources`, `articles`. Six link the theory definition; `articles` links the catalogue.
- `kb/reference/text-contract-profiles.md` — the catalogue, which becomes the prototype catalogue or is folded into the new definition.
- `kb/notes/definitions/text-contract.md` — profile half removed, text-contract half untouched.
- ADRs naming a profile: 042, 057, 061, 062, 063. Record the later change; do not rewrite what each originally decided.
- Notes and instructions using the term in prose: `linking-theory.md`, `technical-constraints-make-kb-objective-choice-engineering.md`, `a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md`, `a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md`, `run-full-improvement-pass-on-note.md`, `publish-an-article.md`, `kb/reference/design-rationale-management.md`, and one published article.
- Proposals and archive entries mentioning profiles are lower priority; archived files are frozen except for link integrity.

A new ADR is required. This supersedes part of ADR 042 — the open profile set with worked-case promotion — without disturbing its decision to retire the closed `register` taxonomy.

## Open points for the executing session

- Whether `collection prototype` needs a standalone `kb/reference/definitions/` artifact or should be a section of the recast catalogue. The definition-typed artifact already in `kb/reference/definitions/collection.md` shows either is available.
- Whether collection contracts should cite their prototype at all after the change, or record provenance only in the ADR. Citing a prototype in a heading risks re-creating the impression of inheritance that the retirement is meant to remove.
- Whether `editorial` survives as a prototype or collapses, given `kb/articles/` is its only realization and ADR 057 introduced it.
- Whether the routing table's `Role` column should be deleted or replaced by something that carries operational weight.

## Completion condition

`profile` is no longer registered vocabulary, `collection prototype` is defined in reference, `AGENTS.md` no longer glosses or tabulates profiles, every consumer above is retargeted or rewritten, an ADR records the supersession, and validation plus a broken-link sweep pass. `kb/notes/definitions/text-contract.md` still exists and still defines text contract.
