# Type system design

This is the current workshop position after reviewing the existing type notes, the implemented validator, and the move-stability problem with bare type names.

## Decision

We should treat `type` as an **artifact-class signal**, not as "whatever the deterministic validator can prove."

More specifically, we should move to **qualified canonical type ids** so type identity survives file moves.

Examples:

- `core.note`
- `core.claim`
- `notes.structured-claim`
- `notes.adr`
- `notes.index`
- `notes.related-system`
- `sources.source-review`

A coherent type can carry three kinds of meaning:

1. **Structural meaning** — enforced by symbolic validation
2. **Review meaning** — enforced by semantic review gates
3. **Authoring meaning** — used by templates, routing, and writing guidance

Under this design, a type is real if it changes at least one system behavior. It does **not** need to introduce additional symbolic structure to count as a real type.

That means a type like `core.claim` is valid even if it is structurally identical to `core.note`, as long as:

- it changes review expectations
- it changes how writers are instructed to shape the document

## Core model

### 1. Qualified `type` is authoritative for library artifact kind

For frontmatter-bearing library documents, frontmatter `type` should be the main signal for what kind of artifact a document is.

Directories do not replace the type system. They scope lookup and storage policy.

So the intended model is:

- frontmatter says `type: notes.related-system`
- tooling resolves that canonical id to a local type-definition module
- that definition tells validation and review what rules apply
- storage location is checked separately

This separates three things that are currently entangled:

1. **artifact identity** — the canonical type id
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

This is the direct analogue of programming-language modules:

- type names are qualified by module/namespace
- the definition lives in that module
- values can move around without changing what type they are

### 3. Symbolic validation stays symbolic

The deterministic validator should remain hard-oracle only.

It should check things like:

- frontmatter shape
- required fields
- required headings
- link existence
- simple collection-specific required markers

It should **not** try to decide soft questions like:

- whether a title is a good claim
- whether a description is truly discriminative
- whether a comparison is honest
- whether an index provides enough context in prose

Those belong to review gates.

### 4. Review gates must also be type-aware

Semantic review should depend on resolved types too.

Examples:

- `core.claim` should trigger stricter title-as-claim and title/body alignment review
- `notes.related-system` should disable generic claim-title expectations and instead enable review-specific grounding/comparison expectations
- `notes.index` should review navigational context quality, not claim strength
- `notes.adr` should review decision clarity and consequence honesty, not generic note composability

So the architecture should be:

- one shared type resolver
- symbolic validator consumes it for hard checks
- semantic review selector consumes it for gate selection / overrides

### 5. Some types are structurally rich; some are semantically rich

The system should allow both.

#### Structurally rich types

Examples:

- `notes.structured-claim`
- `notes.adr`
- `notes.index`
- `notes.related-system`

These have distinctive symbolic expectations.

#### Semantically rich types

Example:

- `core.claim`

This type can be structurally the same as `core.note` while still being a real type, because it changes review and authoring behavior.

This is the key departure from the strongest current formulation in [document-types-should-be-verifiable](../../notes/document-types-should-be-verifiable.md): a type does not have to be *purely* structural to be legitimate. It has to be actionable somewhere in the system.

## Proposed namespace and ladder

### Core namespace

The global root should stay thin:

- `core.text`
- `core.note`
- `core.claim`

These are the cross-collection library primitives.

### Collection namespaces

Collection-specific library types then live in collection namespaces:

- `notes.structured-claim`
- `notes.adr`
- `notes.index`
- `notes.related-system`
- `sources.source-review`

Tasks are different enough that they likely belong to a separate subsystem design rather than this library-note hierarchy, but if we eventually normalize them into the same namespace family, the natural forms would be things like:

- `tasks.active`
- `tasks.backlog`
- `tasks.recurring`

The important point is that these are canonical ids, not inferences from directory placement.

### Ordinary note ladder

For ordinary library notes, the clean ladder is:

- `core.note` — generic structured note
- `core.claim` — a note whose title and framing are expected to function as a claim; mainly semantic/review distinction
- `notes.structured-claim` — a claim with explicit argument scaffold (`Evidence`, `Reasoning`, optional `Caveats`)

This is cleaner than forcing all claim-shaped notes into either:

- `core.note` with an informal convention
- or `notes.structured-claim` before the argument is ready

## Proposed interpretation of current ambiguous cases

### `related-system`

This should become a real first-class type.

Why:

- it has stable required sections
- it has collection-specific metadata like `last-checked`
- it has review-specific expectations
- it clearly changes authoring and review behavior

So the current `kb/notes/types/related-system.md` template saying `type: note` should be treated as drift, not as the target design.

The canonical type id should be:

- `notes.related-system`

### `adr`

`notes.adr` is already a real first-class type.

But the current template reveals another design issue: ADRs have their own decision-status vocabulary (`proposed`, `accepted`, `superseded`, `deprecated`) which is not the same thing as generic note `status`.

So the fix here is not to collapse ADR back into `core.note`. It is to acknowledge that some types need type-specific metadata fields in addition to inheriting the note base.

### `index`

`notes.index` should stay a real type. It has:

- navigational affordance
- structural expectations
- different review expectations from ordinary notes

### `source-review`

`sources.source-review` also fits the first-class type model better than a pure collection convention. It is not just "a note stored in `kb/sources/`."

## What this contradicts

This design contradicts or revises parts of several existing notes.

### 1. It weakens the strongest version of "types must be verifiable"

[document-types-should-be-verifiable](../../notes/document-types-should-be-verifiable.md) argues that a type is only useful if it asserts a verifiable structural property.

The revised position is:

- types must be **actionable**
- structural verifiability is one strong form of actionability
- review-routing and authoring consequences are also legitimate forms of actionability

So "verifiable" is too narrow if it means "deterministically structurally checkable."

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

Frontmatter-bearing knowledge artifacts should use the canonical `type` resolver model:

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

- **library artifact typing** — frontmatter type + canonical resolution
- **temporal subsystem schemas** — local subsystem rules, possibly with separate validators

That keeps us from overfitting a note-type model onto tasks.

## Resolver consequence

The earlier workshop direction assumed directory-hierarchy walking from the file path. Qualified canonical ids change that.

The resolver should now primarily do:

1. parse canonical type id
2. map namespace prefix to definition module/root
3. resolve definition path for that canonical id
4. return validation and review profiles for that type
5. separately check whether the file's storage location is compatible with the type

That is cleaner than "start from the file's directory and guess what `related-system` means here."

## What you might be missing

These are the main edge cases or follow-up decisions this design still needs to handle.

### 1. Resolver output needs to be richer than just "type name"

The shared resolver likely needs to return something like:

- declared type
- canonical type id
- resolved definition path
- parent/base type
- symbolic validation profile
- semantic review profile
- storage-compatibility expectations

If it only returns a string, we will immediately re-fragment the logic.

### 2. Type-specific metadata needs a story

The ADR status mismatch is the clearest current example.

If specialized types are real, some of them will need:

- type-specific fields
- type-specific status vocabularies
- or both

The system should support that explicitly instead of pretending generic note metadata is always enough.

### 3. Traits need a boundary too

The current notes treat traits as additive, independently checkable properties.

This workshop has not yet decided whether review-only distinctions should ever be traits instead of types. For now, `core.claim` seems more like a type than a trait because it changes authoring expectations for the whole document.

But we should state the decision rule later.

### 4. Review-gate inheritance needs design

If `notes.structured-claim` is a subtype of `core.claim`, should it inherit all `core.claim` review expectations plus extra ones?

Probably yes, but the mechanism needs to be explicit rather than improvised gate-by-gate.

### 5. Migration needs to be staged

The design is coherent, but the current repo is not there yet.

The likely order is:

1. define canonical qualified ids
2. build canonical-id resolution
3. make validator consume it
4. make review selection consume it
5. migrate one pilot type (`notes.related-system`)
6. add `core.claim`
7. clean up conflicting notes/docs after the implementation proves out

## Current recommendation

The working design direction for this workshop is:

- `type` should become a qualified canonical artifact id for library artifacts
- directories/modules should scope lookup of local type definitions
- symbolic validation remains deterministic and structural
- semantic review gates also depend on resolved type
- some types can be structurally identical to `core.note` but semantically distinct
- `core.claim` is the clearest example of such a type
- storage location should be checked separately from type identity

This is the design we should assume in the next workshop artifact unless a better objection appears.
