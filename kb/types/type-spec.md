---
type: kb/types/type-spec.md
name: type-spec
description: Authoring and validation contract for path-valued Commonplace type specifications
schema: kb/types/type-spec.schema.yaml
---

# Type spec

A type-spec doc is the authoring and validation contract for one Commonplace artifact type. Artifact frontmatter stores the repo-relative path to this doc in `type:`; readers load this file, read its frontmatter, and then load the declared schema when one exists.

## Required Frontmatter

- `type`: `kb/types/type-spec.md`. The root type spec is self-referential and uses the same value.
- `name`: short human-facing type name.
- `description`: retrieval description for the type contract.
- `schema`: repo-relative path to the `.schema.yaml` file that validates artifacts of this type, or `null` when the type has no schema.

## Validation Contract

The validator treats this file as the terminator for type resolution. When an artifact points at a type-spec doc, the validator reads the type-spec frontmatter and validates the artifact with the schema named by `schema`.

Schema files remain separate from authoring prose. The body of a type-spec doc may include instructions, examples, and templates, but the deterministic validator only inspects the frontmatter and the declared schema file.
