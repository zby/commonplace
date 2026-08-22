# Retire profiles in favour of collection prototypes

## Status

Complete. [ADR 069](../../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md) records the decision and implementation. The scaffolded user-collection prototypes state their purpose directly; an opt-in dialectical/evidential prototype carries an experimental banner; both root routing tables omit `Role`; and the library-wide profile vocabulary has been retired. This remains the **first** step of the vocabulary cleanup and deliberately excludes relocating `text-contract`, which stays where it is and remains open as [its own task](./text-contract-and-profiles.md).

## The move

1. Create a `collection prototype` definition in `kb/reference/` — an optional starting contract copied when creating a collection, not a contract any collection is under. Copying ends the relationship: the destination project owns and maintains its `COLLECTION.md`, and Commonplace does not synchronize it, apply later prototype changes to it, or claim that it still conforms to the prototype.
2. Retire `profile` as registered vocabulary: no longer a named bundle a collection "adopts, extends, or replaces".
3. Remove the profile gloss from the always-loaded `AGENTS.md` vocabulary list, and delete the `Role` column from its collection routing table without replacing it. Apply the same deletion to the scaffolded `AGENTS.md.template` routing table.
4. Edit `kb/notes/definitions/text-contract.md` in place: extract all profile-related content from its frontmatter and body, moving or recasting any material still needed for collection prototypes into the replacement reference artifact(s). Do not move, rename, or delete `text-contract.md`; preserve its text-contract definition at its current path.

## Why this is separable from the text-contract home question

The open task asks which artifact should own the *text contract* vocabulary and where it lives. That question is about placement under the choice-binding notes/reference rule; its backlink inventory is maintained in the dedicated task.

Retiring profiles is a different question with a different answer: the concept is not misplaced, it is misdescribed. It is presented as a contract feature bundle and behaves as a starting template. Fixing the description does not require settling where the neighbouring term lives, and settling the neighbouring term does not fix the description. Doing the cheaper, independently-correct one first also shrinks the second: once profiles are gone, `text-contract.md` loses its largest section and the relocation options change shape.

## Findings that justify it

**Profiles bind nothing at use time.** Every live `COLLECTION.md` restates its contract in full locally. `kb/reference/COLLECTION.md` spells out its own quality goal ("fidelity + economy"), economy tests, fidelity constraint, title conventions, complete label table, and type table. Nothing is inherited. At the moment an agent reads a collection contract to act, the profile name is a family-resemblance label carrying no force — while its definition sits in always-loaded context and in the theoretical collection, both of which advertise it as live vocabulary.

**The abstraction is real but fires once.** `descriptive` has four realizations — `kb/reference/`, `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/sources/` — so it does generalize across collections. It just does its work at collection-creation time and never again. That is prototype semantics: copy a starting point, then own and evolve the local contract independently. A prototype may change for future copies, but those changes never propagate to existing collection contracts.

**The implemented binding paths confirm the boundary.** Collection discovery resolves only the nearest `COLLECTION.md`. Deterministic validation checks collection structure but parses no profile or register declaration. Collection-conformance review embeds the local `COLLECTION.md` itself as the authoritative gate, and the write and connect skills read that file directly with no profile fallback or compiled inheritance. The package's `TypeProfile` name belongs to type-schema resolution and is unrelated. A profile label can affect an agent only as prose inside the local contract; it supplies no rules independently of that text.

**ADR 042 contains the creation-time evidence.** Its worked-case-first promotion rule means a reusable bundle is extracted only after a real collection demonstrates it. Combined with the absence of any use-time binding path, that is evidence for a prototype: a starting contract abstracted from an instance for later copies.

**The always-loaded cost is unearned.** The routing table reads `| Path | Role | Use when |`. Agents route on `Use when`; `Role` repeats the profile name in the most expensive context slot in the repository, and it is the surface that invites reading profiles as binding.

## Execution record

The pre-migration inventory found roughly 23 library files naming a text-contract profile. `TypeProfile` in `type_resolver.py` was confirmed to be unrelated type-resolution vocabulary. The broad `rg` hit count across `kb/` remains dominated by ordinary uses such as system, pathway, error, and execution profiles.

- `AGENTS.md` and `AGENTS.md.template` now route with `Path | Use when`; neither carries a replacement role column. The root glossary defines only text contract.
- `src/commonplace/_data/templates/user-{notes,reference,instructions}-COLLECTION.md` are the concrete scaffolded prototypes. Each requires a complete local contract and disclaims synchronization after installation.
- `src/commonplace/_data/templates/user-dialectical-evidential-COLLECTION.md` is opt-in, marked experimental, and not installed automatically.
- The seven live collection contracts state their purpose and quality goal directly and claim no prototype relationship.
- `kb/reference/text-contract-profiles.md` was relocated to [the collection prototype catalogue](../../../reference/collection-prototypes.md), with a published redirect. Its opening owns the one-time-copy definition.
- `kb/notes/definitions/text-contract.md` stayed at its path and now contains only the binding local text-contract definition.
- ADR 069 partially supersedes ADRs 042 and 057. ADRs 017, 042, 046, and 057 carry current-terminology or supersession annotations; historical titles and deliberation remain historical.
- The former four-axis foundation note was relocated and rewritten as [Artifact classification separates content kind, lineage, and authority](../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md), with a published redirect from its old path.
- Live notes, reference docs, the full-pass instruction, the draft article, and active proposals now read local collection contracts rather than profiles. Frozen proposal archives keep their historical wording.

[ADR 069](../../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md) supersedes ADR 042's open profile set without disturbing its decision to retire the closed `register` taxonomy.

## Resolved choices

- `collection prototype` is defined at the start of the recast catalogue; there is no standalone definition artifact.
- Editorial/expository stays entirely local to `kb/articles/COLLECTION.md`. One realization and no creation-time consumer do not warrant a prototype.

## Completion evidence

`profile` is no longer registered vocabulary. `collection prototype` is defined in reference with one-time-copy semantics. Neither routing table has a `Role` column. Scaffolded and live collection contracts depend only on their complete local text. No existing collection contract claims inheritance, conformance, synchronization, or updates through a prototype. ADR 069 records the supersession, and `kb/notes/definitions/text-contract.md` still exists at its original path with a text-contract-only definition.

Targeted artifact validation, the aggregate `commonplace-validate today` sweep, and redirect-map validation all pass cleanly. The preceding scaffold implementation passed its 18 initialization tests and a package build containing all four prototype templates.
