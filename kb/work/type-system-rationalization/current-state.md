# Current state of the type system

This note inventories how the type system is described, where type-like structure actually lives, what the validator really enforces, and where the current design is internally inconsistent.

The aim is descriptive, not prescriptive: capture the mixed state accurately before proposing a cleanup.

## 1. The stated model

The repo's stated model is spread across four main surfaces:

- [document classification](../../notes/document-classification.md)
- [note base type](../../../types/note.md)
- [WRITING.md](../../instructions/WRITING.md)
- the root [AGENTS.md](../../../AGENTS.md)

Taken together, they imply this model:

1. A document has exactly one type.
2. `text` is the only non-frontmatter root type.
3. Every other structured document extends `note`.
4. The `type` field is a free-form string.
5. Directory-scoped `types/` folders document the structural expectations for each type value.
6. New type values can be introduced by adding a template to the relevant `types/` directory.
7. The routing table tells the writer when to load a directory-local type template.

This is a real type-system story, not just a writing-guidance story. In particular, [types/note.md](../../../types/note.md) says:

- the `type` field is a free-form string
- directory-scoped `types/` folders document the structural expectations for each value
- new type values can be introduced by adding a template to the relevant `types/` directory

That reads as if directory-local type templates are meant to be the authoritative definitions for specialized types.

## 2. Where type-like structure actually lives

There are four different places where "what kind of artifact is this?" is currently expressed.

### A. Frontmatter `type`

This is the most explicit machine-readable signal.

Observed values in the documented model:

- `note`
- `structured-claim`
- `spec`
- `review`
- `index`
- `adr`
- `source-review`

The intended behavior seems to be: frontmatter gives the type name; the relevant template and tooling explain what that name means.

### B. Directory-local `types/` templates

Current local type templates:

- `kb/notes/types/adr.md`
- `kb/notes/types/index.md`
- `kb/notes/types/related-system.md`
- `kb/notes/types/structured-claim.md`
- `kb/sources/types/source-review.md`
- `kb/tasks/types/task-active.md`
- `kb/tasks/types/task-backlog.md`
- `kb/tasks/types/task-recurring.md`

These do not all behave the same way:

- `adr.md` uses `type: adr`
- `index.md` uses `type: index`
- `structured-claim.md` uses `type: structured-claim`
- `source-review.md` uses `type: source-review`
- `related-system.md` uses `type: note`
- task templates do not use frontmatter at all

So even inside the local template layer, there are already at least three different meanings:

1. "this template corresponds to a real frontmatter type value"
2. "this template documents a specialized note shape, but the real type is still `note`"
3. "this template is structural and has no frontmatter type signal at all"

### C. Path / collection placement

The routing table and workshop notes already use directory placement as a semantic signal:

- ADRs live in `kb/notes/adr/`
- related-systems reviews live in `kb/notes/related-systems/`
- source reviews live in `kb/sources/`
- tasks live in `kb/tasks/...`
- the [directories-as-types note](../note-types/directories-as-types.md) explicitly argues that some review-routing distinctions should be carried by directory instead of frontmatter

So the repo is already using path as a type-adjacent signal, whether or not it calls it a type.

### D. Bare type names have unstable identity

The current model uses unqualified type strings like:

- `note`
- `adr`
- `index`
- `related-system`
- `source-review`

This means the identity of some types is still partially path-dependent.

Example:

- if a file says `type: related-system`, what exactly does that mean?
- today, the most plausible answer is "the thing described by `kb/notes/types/related-system.md`"
- but that only works because humans already know the intended collection

The current system has no explicit notion of:

- canonical type identity
- namespace
- type-definition module

So moving a file between directories risks changing the *practical* meaning of its type even when the frontmatter string stays the same.

## 3. What the validator actually enforces

The deterministic validator is [`skills/validate/validate_notes.py`](../../../skills/validate/validate_notes.py).

Its actual behavior is much narrower than the stated model.

### A. Scope

The validator is hard-wired to:

- `NOTES_ROOT = REPO_ROOT / "kb" / "notes"`

So it validates `kb/notes/**.md`, not the whole typed document universe.

Implications:

- `kb/sources/types/source-review.md` exists, but `source-review` is not validated by this script in normal use
- `kb/tasks/types/*.md` exist, but task types are outside the validator's scope
- the current implementation of `/validate` is really "validate notes under `kb/notes/`", not "validate all typed collections"

### B. Type handling

The validator has a hard-coded `TYPE_HEADINGS` map:

- `structured-claim` -> `## Evidence`, `## Reasoning`
- `spec` -> `## Design`, `## Implementation`
- `review` -> `## Findings`
- `adr` -> `## Context`, `## Decision`, `## Consequences`

It also has special-case logic for:

- `review` needing a date
- `index` having enough link density

It does **not**:

- resolve local type definitions dynamically
- walk the directory hierarchy in any general way
- know anything specific about `related-system`
- know anything specific about `source-review`
- know anything specific about task types
- separate type identity from storage location

So the implemented type system is currently:

- generic `note` checks
- plus a small hard-coded set of type-name-specific checks

This is a real implementation, but it is not the same as the directory-scoped type model described in the docs.

### C. Generic heuristics that ignore local type context

The validator applies title composability heuristics globally across notes in `kb/notes/`.

That creates false positives for note classes that are intentionally not claim-titled, for example:

- system-name reviews like `LACP`
- some framework notes
- some definitions
- some index-like artifacts

The validator has no mechanism to say "this note is in a class where artifact-name titles are correct."

## 4. Concrete inconsistencies

These are the clearest mismatches between the stated design and current implementation.

### Inconsistency 1: `related-system` is presented as a type template but encodes `type: note`

[`kb/notes/types/related-system.md`](../../notes/types/related-system.md) is clearly the template the routing table points writers to for related-systems reviews.

But its frontmatter says:

```yaml
type: note
```

So the file is named as if it defines a specialized type, but its own template says the frontmatter type should remain the generic base type.

That makes `related-system` ambiguous:

- is it a real type?
- a note-shaped genre?
- a collection-local convention?

Right now the answer is "somewhere in between."

### Inconsistency 2: docs imply local type definitions are authoritative, but tooling does not resolve them

[types/note.md](../../../types/note.md) says new type values can be introduced by adding a template to the relevant `types/` directory.

But the validator does not dynamically discover those definitions. It only knows the handful of type names hard-coded in `TYPE_HEADINGS` plus the `review`/`index` special cases.

So "add a template, get a type" is true at the documentation level, but false at the tooling level.

### Inconsistency 3: local type templates are heterogeneous about whether they are true type values

Examples:

- `kb/notes/types/adr.md` -> `type: adr`
- `kb/notes/types/index.md` -> `type: index`
- `kb/notes/types/structured-claim.md` -> `type: structured-claim`
- `kb/sources/types/source-review.md` -> `type: source-review`
- `kb/notes/types/related-system.md` -> `type: note`
- `kb/tasks/types/*.md` -> no frontmatter type at all

This means the `types/` directories are not currently one coherent abstraction. They mix:

- first-class type definitions
- note-shape templates
- non-frontmatter runbooks

### Inconsistency 4: ADR template status values do not match note-validator status values

[`kb/notes/types/adr.md`](../../notes/types/adr.md) uses:

- `status: accepted`

and its body expects:

- `proposed | accepted | superseded | deprecated`

But the note validator only recognizes the generic note status ladder:

- `seedling`
- `current`
- `speculative`
- `outdated`

So ADRs are already carrying a second status system that the note validator does not understand.

This is another sign that specialized types are semantically real, even where the tooling still treats them as generic notes.

### Inconsistency 5: WRITING/AGENTS describe more typed collections than `/validate` actually covers

The write-path docs say directory-local types live in:

- `notes/types/`
- `sources/types/`
- `tasks/types/`

But the validator only walks `kb/notes/`.

So there is a gap between:

- "the KB has these local type systems"

and

- "the tooling actually validates those collections as typed artifacts"

### Inconsistency 6: path-based exemptions are already being proposed because the type layer is incomplete

[`kb/work/note-types/directories-as-types.md`](../note-types/directories-as-types.md) argues that some structural exemptions should route by directory rather than by frontmatter type.

That proposal exists for a real reason: the current type layer is not expressive enough in tooling to distinguish:

- artifact-name but valid titles
- claim-shaped notes
- multi-claim frameworks
- collection-specific review forms

So the system is already drifting toward path-based semantics as a compensating mechanism.

### Inconsistency 7: type identity is not clearly separated from storage location

Even if the validator did resolve local type definitions dynamically, the current use of bare type names would still leave one ambiguity:

- is `related-system` the same type wherever the file goes?
- or does it mean "whatever the nearest matching local definition says here"?

The current docs do not answer this cleanly. That is a design gap, not just an implementation gap.

## 5. The current mixed model, stated plainly

The most accurate summary of the current system is:

### Conceptually

- The repo wants a thin global base type system (`text`, `note`) with specialized type meanings documented locally
- the frontmatter `type` field is intended to carry real semantic distinctions
- directory-local templates are supposed to explain those distinctions

### Operationally

- some type names are real because the validator recognizes them (`structured-claim`, `adr`, `review`, `spec`, `index`)
- some collection-specific forms are only conventions (`related-system`)
- some collection semantics live in path placement rather than in frontmatter or validator logic (`tasks`, some review-routing exemptions)
- some type meaning still depends on contextual human knowledge about where the file lives

### Result

The current design is not one unified type system. It is a blend of:

- base types
- hard-coded validator types
- local templates
- collection conventions
- path-based semantics
- bare type names whose identity is still partly contextual

That blend mostly works for writing, because humans and agents can follow the prose guidance. It is much less coherent as a foundation for deterministic validation or review routing.

## 6. What this inventory suggests for the next step

The main design decision is not "how do we fix `related-system`?" It is:

**Which signal is supposed to be authoritative when tooling needs to know what kind of artifact it is looking at, and how is that artifact identity kept stable when files move?**

The candidates are:

1. bare frontmatter `type`
2. qualified canonical frontmatter `type`
3. nearest enclosing `types/` definition resolved by path
4. collection path itself
5. some explicit hybrid rule

Until that is decided, every new special case will tend to leak into a different layer.

## Open questions surfaced by the inventory

- Is `related-system` meant to become a true frontmatter type, or remain a note-shaped collection convention?
- Should the validator resolve local type definitions dynamically, or should the docs stop implying that local templates are authoritative for tooling?
- Are ADR statuses evidence that specialized types need their own field vocabularies, rather than inheriting generic note status semantics unchanged?
- Should `sources/` and `tasks/` get their own validators, or should `/validate` become collection-aware across the whole KB?
- Is the right boundary "types for structure, directories for collections," or is path already the more truthful signal for some artifact classes?
