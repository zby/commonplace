# Type system design

This is the current workshop position after reviewing the existing type notes, the implemented validator, the move-stability problem with bare type names, and the type-vs-trait boundary.

## Decision

Two orthogonal systems serve two independent concerns:

- **Types** define required structure — sections, fields, templates. Checked by deterministic validation.
- **Traits** route semantic review — which gates fire, what expectations apply. Checked by the review system.

Validation is purely structural. All semantic checks live in the review system, routed by traits.

### Type names stay bare

Types use unqualified bare names: `note`, `structured-claim`, `adr`, `related-system`, `source-review`. Each name is currently unambiguous — no two collections define a type with the same name. Qualified canonical ids (e.g. `notes.related-system`) were considered but deferred: the readability cost is real, and the problem they solve (type identity instability under file moves) doesn't exist in practice yet. If ambiguity arises, qualification can be added to just the conflicting names.

### Type examples

- `text`
- `note`
- `structured-claim`
- `adr`
- `index`
- `related-system`
- `source-review`

### Trait examples

- `title-as-claim` — triggers claim-strength, title-body-alignment gates
- `has-comparison` — triggers comparison-quality gate
- `has-external-sources` — triggers grounding-alignment gate
- `has-implementation` — (existing, not yet gate-routed)
- `definition` — triggers term-precision, boundary-coverage gates

### Why `core.claim` was dropped

An earlier workshop draft proposed `core.claim` as a type structurally identical to `core.note` but semantically distinct. The type/trait split eliminates this: the semantic expectations that `core.claim` was meant to carry belong to the `title-as-claim` trait. A `core.note` with `title-as-claim` gets the same review scrutiny without thickening the global type layer. See [decision-criteria.md](./decision-criteria.md) for the full test.

## Core model

### 1. Frontmatter `type` is authoritative for library artifact kind

For frontmatter-bearing library documents, frontmatter `type` should be the main signal for what kind of artifact a document is.

Directories do not replace the type system. They scope lookup and storage policy.

So the intended model is:

- frontmatter says `type: related-system`
- tooling resolves that bare type name through scoped lookup
- that definition tells validation and review what rules apply
- storage location is checked separately

This separates three things that are currently entangled:

1. **artifact identity** — the frontmatter type value
2. **definition lookup** — where the type contract lives
3. **storage placement** — where this artifact should normally reside

Path should not silently become the type system for ordinary library artifacts.

### 2. Directories scope lookup, not identity

Directory-local `types/` folders are still important, but their role is:

- **resolution scope**
- **local extension point**
- **authoritative local definition source**

not "a separate competing classification system."

In other words:

- `type` answers: "what kind of artifact is this?"
- directory/module answers: "where should I look up the definition of this type?"

This is still analogous to programming-language modules in one limited sense: the definition lives in a known scope, and values can move around without changing what type they are. The difference is that, for now, the type name itself stays bare rather than namespace-qualified.

### 3. Type definitions are two files

Each type has two files in its `types/` directory:

- **`{type}.md`** — prose template, read by agents when writing. Unchanged from current templates.
- **`{type}.yaml`** — machine-readable definition, read by the validator. Contains structural requirements.

Example `kb/notes/types/adr.yaml`:

```yaml
base: note
required_headings:
  - "## Context"
  - "## Decision"
  - "## Consequences"
allowed_status: [proposed, accepted, superseded, deprecated]
```

Example `types/note.yaml`:

```yaml
required_fields:
  - description
allowed_status: [seedling, current, speculative, outdated]
```

The separation avoids agents misinterpreting machine-readable fields as authoring instructions. The validator reads YAML files; agents read prose templates. Neither needs to parse the other.

The root `types/` directory holds `note.yaml` and `text.yaml` (base types). Collection-local `types/` directories hold their own YAML files alongside existing templates.

### 4. Validation is purely structural

The validator is a deterministic script. It checks:

- frontmatter shape
- required fields
- required headings (per type)
- link existence
- type-specific field vocabularies (e.g. ADR status values)
- simple collection-specific required markers

It does **not** make semantic judgments. Questions like "is this description discriminative?" or "does this comparison honestly represent alternatives?" belong to the review system.

### 4. Semantic review is routed by traits

Traits are independently checkable properties that route semantic review gates. A document's full review profile is the union of:

- generic gates that apply to all notes
- trait-specific gates derived from the document's traits

Longer-term, some types may imply traits — `notes.related-system` could imply `has-comparison` and `has-external-sources`, `notes.structured-claim` could imply `title-as-claim`. But that is deferred from the initial migration. The first implementation keeps review routing simple: traits are read explicitly from frontmatter, and the migration bulk-adds the needed traits to the existing corpus.

Examples:

- `title-as-claim` triggers claim-strength and title-body-alignment gates
- `has-comparison` triggers comparison-quality gate
- `has-external-sources` triggers grounding-alignment gate
- `definition` triggers term-precision and boundary-coverage gates
- `notes.index` (as a type) can still disable generic claim-title expectations — type-level review overrides remain possible for structural types that need them

### 5. Types are structural; traits are semantic

This is a clean separation:

- **Types** answer: "what sections and fields must this document have?" → validator
- **Traits** answer: "what semantic expectations should review apply?" → review system

The earlier workshop draft proposed "semantically rich types" (types structurally identical to their parent but semantically distinct). The type/trait split eliminates this category entirely. Every type must introduce structural requirements beyond its parent. Semantic-only distinctions are traits.

## Proposed namespace and ladder

### Current naming

The current migration keeps the global vocabulary thin and bare:

- `text`
- `note`
- `structured-claim`
- `adr`
- `index`
- `related-system`
- `source-review`

These names are treated as stable type identities for now because they are currently unambiguous. If collisions appear later, qualification can be introduced for the conflicting names.

### Ordinary note ladder

For ordinary library notes:

- `note` — generic structured note
- `note` + `title-as-claim` trait — a note whose title and framing are expected to function as a claim; gets semantic review scrutiny on claim strength and title-body alignment
- `structured-claim` — a claim with explicit argument scaffold (`Evidence`, `Reasoning`, optional `Caveats`); during the initial migration these notes also carry explicit `traits: [title-as-claim]`

A claim-shaped note that doesn't need the Toulmin scaffold uses `note` with the `title-as-claim` trait. This replaces the earlier `core.claim` proposal.

## Proposed interpretation of current ambiguous cases

### `related-system`

This should become a real first-class type.

Why:

- it has stable required sections
- it has collection-specific metadata like `last-checked`
- it has review-specific expectations
- it clearly changes authoring and review behavior

So the current `kb/notes/types/related-system.md` template saying `type: note` should be treated as drift, not as the target design.

The frontmatter type should be:

- `related-system`

### `adr`

`adr` is already a real first-class type.

But the current template reveals another design issue: ADRs have their own decision-status vocabulary (`proposed`, `accepted`, `superseded`, `deprecated`) which is not the same thing as generic note `status`.

So the fix here is not to collapse ADR back into `core.note`. It is to acknowledge that some types need type-specific metadata fields in addition to inheriting the note base.

### `index`

`index` should stay a real type. It has:

- navigational affordance
- structural expectations
- different review expectations from ordinary notes

### `source-review`

`source-review` also fits the first-class type model better than a pure collection convention. It is not just "a note stored in `kb/sources/`."

## What this contradicts

This design contradicts or revises parts of several existing notes.

### 1. It strengthens "types must be verifiable" by making types purely structural

[document-types-should-be-verifiable](../../notes/document-types-should-be-verifiable.md) argues that a type is only useful if it asserts a verifiable structural property. The earlier workshop draft weakened this by proposing "semantically rich types." The type/trait split restores the original principle in a stronger form: types ARE structural, full stop. Semantic distinctions that don't change required structure are traits, not types.

### 2. It rejects the strongest version of "directories replace types"

[directory-scoped-types-are-cheaper-than-global-types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) pushes toward directories carrying most of the real type semantics.

This workshop design keeps the useful part:

- local definitions should remain cheap and locally extensible

but rejects the stronger claim:

- directories should replace frontmatter artifact typing for library documents

The problem with directory-first typing is that it makes frontmatter type values documentary or redundant, makes cross-system tooling less coherent, and lets file moves silently change practical type meaning.

### 3. It clarifies "local extensibility"

[why-notes-have-types](../../notes/why-notes-have-types.md) is right that the system needs local extensibility. But the clean version of that is:

- local type definitions
- globally consistent resolution model
- stable canonical ids

not:

- whichever layer happens to be easiest for the current exception

## What this design preserves from the existing notes

The design is still compatible with several current commitments:

- the global base should stay thin
- local extension should be cheap
- deterministic validation should stay narrow and fast
- type systems should tolerate misclassification
- review and writing should become more type-aware over time

So this is not a rejection of the existing type work. It is mostly a sharpening of where each kind of semantics should live.

## Important nuance: not every collection has to use frontmatter type the same way

One thing the current notes blur is that not every subsystem is a library-note collection.

### Library artifacts

Frontmatter-bearing knowledge artifacts should use the frontmatter-`type` resolver model:

- `kb/notes/`
- `kb/sources/`
- probably some future stable library-like collections

### Temporal/workshop/task subsystems

Task files are different:

- they do not use frontmatter
- their status is encoded by directory
- they already behave more like local state-machine templates than note types

So the design should not force every collection into one frontmatter-type mechanism.

The correct boundary is:

- **library artifact typing** — frontmatter type + scoped resolution
- **temporal subsystem schemas** — local subsystem rules, possibly with separate validators

That keeps us from overfitting a note-type model onto tasks.

## Resolver consequence

The earlier workshop direction assumed either directory-hierarchy walking from the file path or a move to qualified canonical ids. The current migration keeps bare type names and uses scoped lookup instead.

The resolver should now primarily do:

1. parse the frontmatter type value
2. derive lookup scopes from the file path
3. resolve the definition file for that type through scoped fallback
4. return the structural validation profile for that type
5. separately check whether the file's storage location is compatible with the type if we ever add that check

That is cleaner than hard-coding a small set of type names, while still avoiding the machinery of namespace-qualified ids.

## Open edges

### 1. Resolver output needs to be richer than just "type name"

The resolver likely needs to return something like:

- declared type
- resolved definition path
- parent/base type
- structural validation profile
- optionally, later: implied traits
- storage-compatibility expectations

If it only returns a string, we will immediately re-fragment the logic.

### 2. Type-specific metadata needs a story

The ADR status mismatch is the clearest current example.

If specialized types are real, some of them will need:

- type-specific fields
- type-specific status vocabularies
- or both

The system should support that explicitly instead of pretending generic note metadata is always enough.

### 3. Implied-trait inheritance needs design

If a future version of the system adds type-implied traits, and `notes.structured-claim` implies `title-as-claim`, then a future type extending `notes.structured-claim` would probably inherit that implied trait. But this propagation question is postponed until after the explicit-traits migration works.

### 4. Migration needs to be staged

The design is coherent, but the current repo is not there yet.

The likely order is:

1. define YAML type definitions
2. build scoped bare-name resolution
3. make validator consume it (structural profiles per type)
4. migrate explicit traits into frontmatter
5. make review system consume traits for gate selection
6. migrate one pilot type (`related-system`)
7. clean up conflicting notes/docs after the implementation proves out

## Current recommendation

The working design direction for this workshop is:

- **Types** are structural — bare names, required sections/fields, checked by deterministic validation
- **Traits** are semantic — route review gates, checked by the review system
- Types can imply traits (e.g. `structured-claim` implies `title-as-claim`) — deferred, not needed for initial migration; first pass uses explicit frontmatter traits
- The global base stays thin: just `text` and `note`
- Directories scope type-definition lookup, not identity
- Qualified type ids deferred — bare names are unambiguous today

See [decision-criteria.md](./decision-criteria.md) for the test that determines whether a distinction is a type or a trait.
