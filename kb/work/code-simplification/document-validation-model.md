# Document Validation Model

## Current position

Commonplace should **not** model note frontmatter as a closed set of `Pydantic` classes.

Reason:

- notes must support user-defined types
- user-defined types may require user-defined frontmatter fields
- generating Python classes dynamically from `types/*.yaml` would be the wrong kind of machinery

So the clean design is:

- document body has a stable Python shape
- note frontmatter stays an open-world dictionary
- type definitions are the closed-world schema surface

## Proposed data model

### Text document

The only stable document-level model we need right now is:

```python
class TextDocument:
    content: str
```

That matches the repo's real root type: [text](../../../types/text.md).

### Structured note

A structured note is a text document plus frontmatter:

```python
class NoteDocument(TextDocument):
    frontmatter: dict[str, Any]
```

The frontmatter should remain a plain dictionary rather than a `Pydantic` model.

## Why frontmatter should stay a dictionary

### 1. Notes are intentionally extensible

The repo's type system already allows new type names and new required fields to appear through `types/*.yaml`.

If Python models hard-code frontmatter fields, the code starts fighting the extensibility story.

### 2. A hybrid model is harder to explain

A partial `Pydantic` model with `extra="allow"` creates an awkward split:

- some fields are typed attributes
- some fields are arbitrary extras
- type-specific validation still lives elsewhere

That is less coherent than simply treating frontmatter as data.

### 3. The real closed schema is the type definition file

`types/*.yaml` files are controlled configuration with a finite shape. Notes are open-world documents. Those should not be modeled the same way.

## What gets schema validation

### Type definitions

The correct place for schema validation is the type-definition files:

- [types/note.yaml](../../../types/note.yaml)
- [types/text.yaml](../../../types/text.yaml)
- [kb/notes/types/adr.yaml](../../../kb/notes/types/adr.yaml)
- [kb/notes/types/index.yaml](../../../kb/notes/types/index.yaml)
- [kb/notes/types/related-system.yaml](../../../kb/notes/types/related-system.yaml)
- [kb/notes/types/review.yaml](../../../kb/notes/types/review.yaml)
- [kb/notes/types/spec.yaml](../../../kb/notes/types/spec.yaml)
- [kb/notes/types/structured-claim.yaml](../../../kb/notes/types/structured-claim.yaml)
- [kb/sources/types/source-review.yaml](../../../kb/sources/types/source-review.yaml)

These files already form a small declarative schema language:

- `base`
- `required_headings`
- `any_headings`
- `required_fields`
- `allowed_status`
- `requires_date`
- `min_links`

That surface is finite, stable, and belongs in a real schema model.

### Possible implementation

Use:

- `yaml.safe_load(...)` for parsing
- `Pydantic` for validating the loaded type-definition data

Example:

```python
class TypeDefinition(BaseModel):
    base: str | None = None
    required_headings: list[str] = Field(default_factory=list)
    any_headings: list[str] = Field(default_factory=list)
    required_fields: list[str] = Field(default_factory=list)
    allowed_status: list[str] = Field(default_factory=list)
    requires_date: bool = False
    min_links: int | None = None
```

Then the resolver loads YAML, validates it against `TypeDefinition`, and converts it into `TypeProfile`.

## How note validation works in this design

Note validation still happens. It just should not depend on a static Python class per note type.

Validation has three layers:

### 1. Parse layer

- detect and split frontmatter
- parse frontmatter YAML into `dict[str, Any]`
- strip body content

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

Resolve the note's `type` to a validated `TypeDefinition` / `TypeProfile`, then apply the profile to the note.

Examples:

- `adr` requires `## Context`, `## Decision`, `## Consequences`
- `review` requires `## Findings` and a date
- `related-system` requires `last-checked`
- `index` requires enough links

This is still schema validation. The schema is just data-driven from `types/*.yaml` instead of encoded as one Python class per note type.

## What not to do

### Do not create one Python class per type

Avoid:

- `AdrDocument`
- `IndexDocument`
- `ReviewDocument`
- `StructuredClaimDocument`

unless a type later acquires genuinely type-specific runtime behavior or fixed metadata fields that justify a dedicated model.

Right now these distinctions are structural profiles, and the YAML type layer already expresses them better.

### Do not dynamically generate `Pydantic` classes from user type definitions

This would add machinery without solving the underlying modeling problem. The system is already designed around declarative type profiles; the validator should consume those directly.

## Resulting architecture

The clean split is:

- **documents**: stable Python objects
- **frontmatter**: open-world metadata dictionary
- **type definitions**: schema-validated YAML configuration
- **validator**: applies core rules plus resolved type profile to notes

This preserves user-defined extensibility without giving up structure where the structure is genuinely closed and stable.
