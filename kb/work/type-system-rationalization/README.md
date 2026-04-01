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

The current workshop direction is to move toward **qualified canonical type ids**:

- `core.note`
- `core.claim`
- `notes.structured-claim`
- `notes.adr`
- `notes.index`
- `notes.related-system`
- `sources.source-review`

This separates:

- artifact identity
- type-definition lookup
- storage location

so a file can move without silently changing what type it is.

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
If executable, the validator and review tooling need a real resolver. If documentary, the repo should stop implying that new type values become real by adding templates.

2. **What is the identity of a type?**
If types are unqualified bare strings like `related-system`, their meaning still depends on where the file lives. If types are qualified ids like `notes.related-system`, identity can stay stable under file moves and directory changes.

3. **When should a distinction be a type versus a directory?**
`structured-claim`, `adr`, and `index` look like genuine artifact types. Definitions, articles, and related-systems reviews are less settled. We need a rule that prevents "use whatever signal is convenient this week."

4. **What is the inheritance model?**
The repo says every structured document extends `note`, but the implementation only partially reflects this. We need to decide whether specialized types inherit generic checks and selectively override them, or whether each type defines a full independent contract.

5. **How do semantic review gates learn the applicable conventions?**
The frontmatter and semantic review layers currently rely on broad heuristics. If type distinctions are real, review routing should derive from the same resolved type signal instead of ad hoc path exceptions.

6. **What is the migration path from the current mixed state?**
There are already notes and templates that assume one model while scripts implement another. Any design has to explain how to get from here to there without leaving more ambiguity behind.

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
- a qualified naming scheme for canonical type ids
- a decision on `related-system`: true type, note-shaped convention, or directory-routed artifact class
- a resolution algorithm for validation/review rule lookup
- a migration plan for templates, docs, and validator behavior
- one promoted library artifact when the design stabilizes (likely an ADR or a note sharpening the type-system theory)

## Starter artifacts

- `current-state.md` — inventory of how types are described versus enforced today
- `design.md` — current workshop position on what a coherent type system should mean
- `resolution-algorithm.md` — concrete lookup algorithm for type rules
- `decision-criteria.md` — test for type vs directory vs trait
- `migration-plan.md` — ordered implementation plan once the design is chosen

## Open questions

- Should type definitions stay as prose templates, or gain a machine-readable companion file for tooling?
- Is `related-system` actually a missing first-class type, or evidence that review routing sometimes belongs to collection structure instead?
- Should the validator and review system share one resolver, or can they diverge safely?
- Does the current `index` handling have the same problem as `related-system`, just less visible?
- How much of the namespace should mirror filesystem structure? `notes.related-system` seems right; `kb.notes.related-systems.related-system` does not.
