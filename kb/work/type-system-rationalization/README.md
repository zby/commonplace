# Workshop: Type System Rationalization

## Question

What is the coherent design for types in this KB, and how should validation and review resolve type-specific rules without mixing three competing signals:

- global type names in frontmatter
- directory-scoped `types/` templates
- path-based structural exemptions

And if types are real artifact identities, how do we keep that identity stable when a file moves between directories?

## Why this workshop exists

A concrete inconsistency surfaced while writing the LACP related-systems review:

- [`kb/notes/types/related-system.md`](../../notes/types/related-system.md) is clearly presented as the template for a specialized artifact kind
- but the template still says `type: note`
- meanwhile the validator only gives first-class treatment to a few hard-coded type names
- and there is already a competing line of thought in [note-types/directories-as-types.md](../note-types/directories-as-types.md) arguing that some distinctions should route by path rather than by `type`

That leaves the current system in an in-between state:

- conceptually, `type` is free-form and directory-local type templates are supposed to define structural expectations
- operationally, only some type names are executable semantics
- path-based exceptions are starting to appear because the type layer is incomplete

This workshop exists to rationalize that design before more special cases accumulate.

The current workshop direction is:

1. **Types are structural** — bare type names (`note`, `adr`, `related-system`, etc.) define required sections, fields, and templates. Checked by deterministic validation.
2. **Traits are semantic** — route semantic review gates (`title-as-claim`, `has-comparison`, `definition`, etc.). Checked by the review system.
3. **Initial migration uses explicit traits** — the review system reads `traits:` from frontmatter. Potential type-implied traits are deferred until after the corpus and tooling are migrated.

This separates:

- artifact identity (frontmatter type value)
- structural validation (types)
- semantic review routing (traits)
- type-definition lookup (scoped lookup → definition file)
- storage location (checked separately)

`core.claim` was dropped — its semantic expectations belong to the `title-as-claim` trait, not a type. The global base stays thin: just `text` and `note`.

## Current grounding

- [document classification](../../notes/document-classification.md) — current taxonomy statement: one document, one type; `type` is free-form; directory-scoped `types/` folders define expectations
- [note base type](../../../types/note.md) — `note` as the base structured type and the statement that new type values can be introduced by adding a template to the relevant `types/` directory
- [document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — current strongest statement of types as structurally verifiable contracts
- [why notes have types](../../notes/why-notes-have-types.md) — current summary of navigation, enforcement, verification, and extensibility roles
- [directory-scoped types are cheaper than global types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) — economic argument for local type definitions
- [directories can replace type fields for structural exemptions](../note-types/directories-as-types.md) — competing proposal: some review-routing distinctions should be carried by path, not frontmatter
- [writing guide](../../instructions/WRITING.md) — operational write-path guidance for common vs directory-local types
- [validator](../../instructions/validate/validate_notes.py) — current implementation surface that reveals which type distinctions are real versus documentary

## Tensions to resolve

1. **Are directory-local `types/` files documentary or executable?**
If executable, the validator needs a real resolver. If documentary, the repo should stop implying that new type values become real by adding templates.
→ *Workshop position:* executable. The resolver maps frontmatter type names to definition files through scoped lookup.

2. **What is the identity of a type?**
→ *Resolved for now:* bare names are acceptable because current names are unambiguous. If collisions appear later, qualification can be introduced for the conflicting names.

3. **When should a distinction be a type versus a trait?**
→ *Resolved:* see [decision-criteria.md](./decision-criteria.md). Types = structural requirements. Traits = semantic review routing.

4. **What is the inheritance model?**
Every structured type extends `note` and inherits its structural checks. Trait routing is separate and uses explicit frontmatter traits in the initial migration.

5. **How do semantic review gates learn the applicable conventions?**
→ *Resolved:* traits route gates. The review system reads explicit frontmatter traits to determine which gates fire in the initial migration.

6. **What is the migration path from the current mixed state?**
→ *Resolved enough to execute:* see [migration-plan.md](./migration-plan.md).

## Candidate design directions

### 1. Qualified type-first, module-resolved

- `type` is a canonical qualified id
- resolver maps namespace prefix to a type-definition module
- storage directory is checked separately from type identity
- path-based exemptions become rare and explicit

Strongest benefit: a file can move without changing its type.

Main risk: requires real resolver machinery and probably some machine-readable type metadata in addition to prose templates.

### 2. Directory-first, frontmatter-secondary

- some artifact kinds are encoded structurally by location
- `type` remains for broad shape (`note`, `structured-claim`, `adr`, etc.)
- local review/validation behavior is mostly routed by directory

Strongest benefit: cheap and visible.

Main risk: type semantics get split across two unrelated signals and become harder to reason about.

### 3. Hybrid with explicit boundary

- use qualified `type` ids for library artifact distinctions
- use directories for collections and workshop-like routing
- allow directory-level exemptions only when the distinction is not a genuine document type

This currently feels like the most plausible target, but it needs a crisp test for what counts as a "genuine document type."

## Deliverables for this workshop

- a precise statement of the type model
- a decision on the naming scheme for type ids
- a decision on `related-system`: true type, note-shaped convention, or directory-routed artifact class
- a resolution algorithm for validation/review rule lookup
- a migration plan for templates, docs, and validator behavior
- one promoted library artifact when the design stabilizes (likely an ADR or a note sharpening the type-system theory)

## Artifacts

- `current-state.md` — inventory of how types are described versus enforced today
- `design.md` — current workshop position: types for structure, traits for semantic review, bare names now, explicit traits first
- `resolution-algorithm.md` — concrete lookup algorithm for type rules and explicit-trait review routing
- `decision-criteria.md` — test for type vs trait (structural requirement → type; semantic review routing → trait)
- `review-integration.md` — how the review system consumes traits: gate applicability, shared note-aware filtering, recursive sweep scope, new `title-as-claim` gate
- `type-resolver.md` — scoped lookup algorithm, YAML schema, base type definitions, validator integration
- [`../../notes/adr/012-types-for-structure-traits-for-review.md`](../../notes/adr/012-types-for-structure-traits-for-review.md) — accepted ADR produced by this workshop
- `migration-plan.md` — ordered implementation plan

## Open questions

- ~~Should type definitions stay as prose templates, or gain a machine-readable companion file?~~ Resolved: companion `.yaml` files alongside prose `.md` templates. Validator reads YAML; agents read prose.
- Should the validator and review system share one resolver, or can they diverge safely?
- Should implied traits ever be added after the explicit-traits migration lands?

## Resolved questions

- `related-system` is a real first-class type — it has required sections and fields.
- `core.claim` is dropped — its semantic expectations belong to the `title-as-claim` trait.
- Type vs trait boundary: structural requirement → type; semantic review routing → trait. See [decision-criteria.md](./decision-criteria.md).
- Validation is purely structural (deterministic). All semantic checks live in the review system, routed by traits.
- Qualified canonical type ids deferred — bare names are unambiguous today, qualification adds readability cost for a problem that doesn't exist yet.
- Implied traits from types deferred — authors declare traits explicitly in frontmatter for now, including bulk migration of existing `structured-claim` and claim-shaped notes.
