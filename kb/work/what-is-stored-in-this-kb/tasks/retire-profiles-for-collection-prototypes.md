# Retire profiles in favour of collection prototypes

## Status

Decided in direction, partially executed. The scaffolded user-collection prototypes now state their purpose directly, without register/profile selection; an opt-in dialectical/evidential prototype exists with an experimental banner; and the scaffolded `AGENTS.md.template` routing table no longer carries a `Role` column. The library-wide vocabulary migration is not executed. This is the **first** step of the vocabulary cleanup and is deliberately scoped to exclude relocating `text-contract`, which stays where it is and stays open as [its own task](./text-contract-and-profiles.md).

## The move

1. Create a `collection prototype` definition in `kb/reference/` — an optional starting contract copied when creating a collection, not a contract any collection is under. Copying ends the relationship: the destination project owns and maintains its `COLLECTION.md`, and Commonplace does not synchronize it, apply later prototype changes to it, or claim that it still conforms to the prototype.
2. Retire `profile` as registered vocabulary: no longer a named bundle a collection "adopts, extends, or replaces".
3. Remove the profile gloss from the always-loaded `AGENTS.md` vocabulary list, and delete the `Role` column from its collection routing table without replacing it. Apply the same deletion to the scaffolded `AGENTS.md.template` routing table.
4. Edit `kb/notes/definitions/text-contract.md` in place: extract all profile-related content from its frontmatter and body, moving or recasting any material still needed for collection prototypes into the replacement reference artifact(s). Do not move, rename, or delete `text-contract.md`; preserve its text-contract definition at its current path.

## Why this is separable from the text-contract home question

The open task asks which artifact should own the *text contract* vocabulary and where it lives. That question is about placement under the belief/choice rule and carries 30 backlinks across 22 files.

Retiring profiles is a different question with a different answer: the concept is not misplaced, it is misdescribed. It is presented as a contract feature bundle and behaves as a starting template. Fixing the description does not require settling where the neighbouring term lives, and settling the neighbouring term does not fix the description. Doing the cheaper, independently-correct one first also shrinks the second: once profiles are gone, `text-contract.md` loses its largest section and the relocation options change shape.

## Findings that justify it

**Profiles bind nothing at use time.** Every live `COLLECTION.md` restates its contract in full locally. `kb/reference/COLLECTION.md` spells out its own quality goal ("fidelity + economy"), economy tests, fidelity constraint, title conventions, complete label table, and type table. Nothing is inherited. At the moment an agent reads a collection contract to act, the profile name is a family-resemblance label carrying no force — while its definition sits in always-loaded context and in the theoretical collection, both of which advertise it as live vocabulary.

**The abstraction is real but fires once.** `descriptive` has four realizations — `kb/reference/`, `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/sources/` — so it does generalize across collections. It just does its work at collection-creation time and never again. That is prototype semantics: copy a starting point, then own and evolve the local contract independently. A prototype may change for future copies, but those changes never propagate to existing collection contracts.

**The implemented binding paths confirm the boundary.** Collection discovery resolves only the nearest `COLLECTION.md`. Deterministic validation checks collection structure but parses no profile or register declaration. Collection-conformance review embeds the local `COLLECTION.md` itself as the authoritative gate, and the write and connect skills read that file directly with no profile fallback or compiled inheritance. The package's `TypeProfile` name belongs to type-schema resolution and is unrelated. A profile label can affect an agent only as prose inside the local contract; it supplies no rules independently of that text.

**ADR 042 contains the creation-time evidence.** Its worked-case-first promotion rule means a reusable bundle is extracted only after a real collection demonstrates it. Combined with the absence of any use-time binding path, that is evidence for a prototype: a starting contract abstracted from an instance for later copies.

**The always-loaded cost is unearned.** The routing table reads `| Path | Role | Use when |`. Agents route on `Use when`; `Role` repeats the profile name in the most expensive context slot in the repository, and it is the surface that invites reading profiles as binding.

## Migration inventory

Roughly 23 library files name a text-contract profile. `TypeProfile` in `type_resolver.py` is unrelated type-resolution vocabulary, but scaffold package data is affected: the three user-collection contract templates are the concrete creation-time prototypes, and `AGENTS.md.template` repeats the routing table. The broad `rg` hit count across `kb/` is dominated by ordinary-English "profile" in external-system reviews and workshop files.

- `AGENTS.md` — vocabulary entry and routing-table `Role` column; delete the column rather than replacing it.
- `AGENTS.md.template` — scaffold routing-table `Role` column; already deleted.
- `src/commonplace/_data/templates/user-{notes,reference,instructions}-COLLECTION.md` — the concrete scaffolded collection prototypes; already rewritten to state purpose and scope directly, require a complete local contract instead of register/profile selection, and disclaim synchronization after installation.
- `src/commonplace/_data/templates/user-dialectical-evidential-COLLECTION.md` — an opt-in prototype with an experimental banner, not installed automatically; already added. Its worked-case evidence warrants availability as a starting point, while the mark records that it has not been tested across independently maintained collections.
- Seven collection contracts declaring a profile in their heading and opening line: `notes`, `reference`, `instructions`, `agentic-systems`, `agent-memory-systems`, `sources`, `articles`. Six link the theory definition; `articles` links the catalogue.
- `kb/reference/text-contract-profiles.md` — the catalogue, which becomes the prototype catalogue or is folded into the new definition.
- `kb/notes/definitions/text-contract.md` — profile half removed, text-contract half untouched.
- ADRs whose operative or explanatory text uses the retired model include 017, 042, 046, 057, 061, 062, and 063. Record the later change and any partial supersession without rewriting what each originally decided; occurrences confined to historical titles and links may remain.
- `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` — substantive rewrite required because communicative profile is currently one of its four classification axes, not a passing vocabulary use.
- Other notes, reference docs, instructions, and articles using the term in live prose include `linking-theory.md`, `technical-constraints-make-kb-objective-choice-engineering.md`, `a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md`, `a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md`, `run-full-improvement-pass-on-note.md`, `publish-an-article.md`, `kb/reference/design-rationale-management.md`, and one draft article.
- Active proposals using text-contract-profile semantics must be rewritten or explicitly retired so they cannot reintroduce the model. Frozen archive entries keep their historical wording except where link integrity requires maintenance.

A new ADR is required. This supersedes part of ADR 042 — the open profile set with worked-case promotion — without disturbing its decision to retire the closed `register` taxonomy.

## Open points for the executing session

- Whether `collection prototype` needs a standalone `kb/reference/definitions/` artifact or should be a section of the recast catalogue. The definition-typed artifact already in `kb/reference/definitions/collection.md` shows either is available.
- Whether `editorial` survives as a prototype or collapses, given `kb/articles/` is its only realization and ADR 057 introduced it.

## Completion condition

`profile` is no longer registered vocabulary, `collection prototype` is defined in reference with one-time-copy semantics, `AGENTS.md` no longer glosses or tabulates profiles, neither routing table has a `Role` column, the scaffolded user-collection prototypes depend only on their complete local contracts, and no existing collection contract claims inheritance, conformance, synchronization, or updates through a prototype. Every consumer above is retargeted or rewritten, an ADR records the supersession, and validation plus a broken-link sweep pass. `kb/notes/definitions/text-contract.md` still exists and still defines text contract.
