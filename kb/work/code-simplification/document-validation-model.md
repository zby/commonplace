# Document Validation Model

## Current position

Commonplace should **not** model note frontmatter as a closed set of Python classes.

Reason:

- notes must support user-defined types
- user-defined types may require user-defined frontmatter fields
- generating Python classes dynamically from authored schemas would be the wrong kind of machinery

So the clean design is:

- markdown is parsed into one stable document object
- note frontmatter stays an open-world dictionary inside that object
- authored type definitions are the closed-world schema surface

This is now the implemented direction.

## Implemented data model

### Text document

The stable runtime model is the parsed document object in [`src/commonplace/lib/note_parser.py`](../../../src/commonplace/lib/note_parser.py):

```python
class ParsedDocument:
    frontmatter: dict[str, Any] | None
    body: str
    headings: tuple[str, ...]
    links: tuple[str, ...]
    body_dates: tuple[str, ...]
    title: str
```

## Why frontmatter should stay a dictionary

### 1. Notes are intentionally extensible

The repo's type system already allows new type names and new required fields to appear through scoped authored schemas such as:

- [`kb/types/note.schema.yaml`](../../types/note.schema.yaml)
- [`kb/notes/types/structured-claim.schema.yaml`](../../../kb/notes/types/structured-claim.schema.yaml)
- workshop-local or collection-local `types/{type}.schema.yaml`

If Python models hard-code frontmatter fields, the code starts fighting that extensibility story.

### 2. A hybrid model is harder to explain

A partial typed model with "known fields plus arbitrary extras" creates an awkward split:

- some fields are typed attributes
- some fields are arbitrary extras
- type-specific validation still lives elsewhere

That is less coherent than simply treating frontmatter as data.

### 3. The real closed schema is the type definition file

The closed-world schema is the authored JSON Schema document, not the note object.

Notes are open-world documents. Schemas are controlled configuration. Those should not be modeled the same way.

## What gets schema validation

### Type definitions

The correct place for machine-readable structural validation is the type-definition files:

- [kb/types/note.schema.yaml](../../types/note.schema.yaml)
- [kb/reference/types/adr.schema.yaml](../../../kb/reference/types/adr.schema.yaml)
- [kb/notes/types/index.schema.yaml](../../../kb/notes/types/index.schema.yaml)
- [kb/notes/types/related-system.schema.yaml](../../../kb/notes/types/related-system.schema.yaml)
- [kb/notes/types/review.schema.yaml](../../../kb/notes/types/review.schema.yaml)
- [kb/notes/types/spec.schema.yaml](../../../kb/notes/types/spec.schema.yaml)
- [kb/notes/types/structured-claim.schema.yaml](../../../kb/notes/types/structured-claim.schema.yaml)
- [kb/sources/types/source-review.schema.yaml](../../../kb/sources/types/source-review.schema.yaml)

These are now ordinary JSON Schema documents authored in YAML syntax.

The runtime parses them with `yaml.safe_load(...)`, resolves `$ref` chains, and validates note instances with `jsonschema`.

## How note validation works in this design

Note validation still happens. It just does not depend on a static Python class per note type.

Validation has three layers:

### 1. Parse layer

- detect and split frontmatter
- parse frontmatter YAML into `dict[str, Any]`
- extract body content, headings, links, dates, and title into `ParsedDocument`

### 2. Universal note validation

Apply stable rules to the frontmatter dictionary.

Examples:

- `description` exists and is a non-empty string
- `type` is a non-empty string if present
- `traits` is a list if present
- `tags` is a list if present
- `status` is a string if present

These are universal note-contract rules, not type-specific schema.

### 3. Type-specific validation

Resolve the note's `type` to a schema-backed `TypeProfile`, then apply the schema to the parsed note object.

Examples:

- `adr` requires `## Context`, `## Decision`, `## Consequences`
- `review` requires `## Findings` and a date
- `related-system` requires `last-checked`
- `index` requires enough links

This is still schema validation. The schema just lives in authored JSON Schema documents instead of a Commonplace-specific mini-language or one Python class per type.

`TypeProfile` still exists, but now mainly as a compatibility layer that extracts useful summary signals from schemas:

- required headings
- any-of headings
- required frontmatter fields
- allowed status values
- date requirements
- minimum link counts

That metadata supports better CLI messages without making the schema language itself bespoke again.

## What not to do

### Do not create one Python class per type

Avoid:

- `AdrDocument`
- `IndexDocument`
- `ReviewDocument`
- `StructuredClaimDocument`

unless a type later acquires genuinely type-specific runtime behavior or fixed metadata fields that justify a dedicated model.

Right now these distinctions are structural profiles, and the authored schema layer already expresses them better.

### Do not dynamically generate Python models from user type definitions

This would add machinery without solving the underlying modeling problem. The system is already designed around authored schemas plus parsed-note validation; the validator should consume those directly.

## Resulting architecture

The clean split is:

- **documents**: stable parsed-note objects
- **frontmatter**: open-world metadata dictionary
- **type definitions**: authored JSON Schema documents in YAML syntax
- **resolver**: scoped schema lookup plus summary metadata extraction
- **validator**: applies universal checks plus schema validation to parsed notes

This preserves user-defined extensibility without giving up structure where the structure is genuinely closed and stable.
