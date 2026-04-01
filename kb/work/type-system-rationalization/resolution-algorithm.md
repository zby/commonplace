# Resolution algorithm

This note specifies the current intended resolver for the workshop design with qualified canonical type ids.

## Goal

Resolve a document's declared type into:

- its canonical identity
- the definition file that describes it
- the symbolic validation profile
- the semantic review profile
- storage-location expectations

without making type meaning depend on the file's current directory.

## Inputs

For a given file:

- absolute or repo-relative path
- parsed frontmatter `type` value, if any

## Output shape

The resolver should return a record roughly like:

```json
{
  "declared_type": "notes.related-system",
  "canonical_type": "notes.related-system",
  "base_type": "core.note",
  "definition_path": "kb/notes/types/related-system.md",
  "symbolic_profile": "notes.related-system",
  "review_profile": "notes.related-system",
  "allowed_roots": ["kb/notes/related-systems", "kb/notes"],
  "storage_ok": true
}
```

The exact fields can differ, but the resolver needs to expose all of these concepts somehow.

## Namespace scheme

Current intended canonical namespaces:

- `core.*` — types defined under repo-root `types/`
- `notes.*` — stable library note types defined under `kb/notes/types/`
- `sources.*` — source-layer types defined under `kb/sources/types/`
- `tasks.*` — task/workflow subsystem schemas, if and when we decide to normalize them into the same namespace family

Examples:

- `core.text`
- `core.note`
- `core.claim`
- `notes.structured-claim`
- `notes.adr`
- `notes.index`
- `notes.related-system`
- `sources.source-review`

## Resolution steps

### 1. Parse declared type

If the file has no frontmatter:

- implicit type is `core.text`

If the file has frontmatter but no explicit `type` field:

- implicit type is `core.note`

If it has a `type` field:

- parse as canonical type id if qualified
- during migration, optionally support legacy bare names and map them forward

Examples of migration mappings:

- `note` -> `core.note`
- `claim` -> `core.claim`
- `structured-claim` -> `notes.structured-claim`
- `adr` -> `notes.adr`
- `index` -> `notes.index`
- `related-system` -> `notes.related-system`
- `source-review` -> `sources.source-review`

### 2. Resolve canonical definition path

Map namespace to definition root:

- `core.*` -> `types/`
- `notes.*` -> `kb/notes/types/`
- `sources.*` -> `kb/sources/types/`
- `tasks.*` -> `kb/tasks/types/`

Then map the suffix to a filename.

Examples:

- `notes.related-system` -> `kb/notes/types/related-system.md`
- `notes.adr` -> `kb/notes/types/adr.md`
- `sources.source-review` -> `kb/sources/types/source-review.md`
- `core.note` -> `types/note.md`

The key property is that this lookup depends on the canonical type id, not on where the file currently lives.

### 3. Resolve base type / inheritance

The current intended base chain is:

- `core.text` has no parent
- `core.note` is the base structured type
- `core.claim` extends `core.note`
- `notes.structured-claim` extends `core.claim`
- `notes.adr` extends `core.note`
- `notes.index` extends `core.note`
- `notes.related-system` extends `core.note`
- `sources.source-review` extends `core.note`

The resolver should expose this explicitly so validation/review can inherit rules rather than duplicating them.

### 4. Resolve symbolic validation profile

The symbolic validator should consume a profile derived from the canonical type.

Examples:

- `core.note` -> generic frontmatter, description, links
- `core.claim` -> same symbolic structure as `core.note`
- `notes.structured-claim` -> require `Evidence` and `Reasoning`
- `notes.adr` -> require ADR headings
- `notes.index` -> require index-like navigation markers / density checks
- `notes.related-system` -> require `last-checked`, `Repository:`, and the review sections
- `sources.source-review` -> whatever symbolic checks we define for source reviews

### 5. Resolve semantic review profile

Review routing should also consume a type-derived profile.

Examples:

- `core.note` -> generic note gates
- `core.claim` -> stronger title-as-claim/title-body alignment expectations
- `notes.structured-claim` -> inherit claim gates plus argument-structure gates
- `notes.related-system` -> disable generic claim-title expectations, enable review-specific comparison/grounding expectations
- `notes.index` -> index-specific navigational/contextual review expectations

### 6. Check storage compatibility separately

Type identity should not depend on location, but location still matters.

So after resolving the type, do a separate storage check:

- is a `notes.related-system` file stored somewhere sensible?
- is a `notes.adr` file under `kb/notes/adr/`?
- is a `sources.source-review` file under `kb/sources/`?

This should produce:

- `ok`
- `warn`
- or `error`, depending on how strict we want to be

The important point is that this is **not** part of type resolution itself.

## Why this is better than directory-first resolution

Directory-first resolution makes the meaning of a bare type name depend on where the file currently sits.

Qualified canonical ids avoid that:

- moving a file does not change what type it is
- type lookup is deterministic from the declared id
- storage policy becomes an explicit second check rather than an implicit hidden one

This matches the programming-language analogy the workshop is now leaning on: modules qualify names; values can move without changing their declared type.

## Migration mode

We do not need to flip the whole repo at once.

A practical migration mode would be:

1. parse legacy bare type names
2. map them to canonical ids internally
3. use canonical ids in validator/review internals
4. gradually rewrite templates and files to the qualified form

That lets us introduce the resolver without forcing a one-shot repo-wide rewrite.

## Open questions

- Should `core.claim` live in `types/claim.md` or be modeled only in code at first?
- Do we want a machine-readable companion file for each type definition, or should the resolver use code-side profiles while templates stay prose?
- Should storage compatibility be a warning or an error during migration?
- Do nested note namespaces ever matter, e.g. `notes.definitions.term`, or is one collection-level namespace enough for now?
