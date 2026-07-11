---
description: How Commonplace resolves a note's type contract at authoring and validation time - collection-scoped lookup, collection conventions, and skill-driven on-demand loading
type: kb/types/note.md
tags: []
---

# Type loading

Commonplace stores each explicit artifact type as a path-valued pointer to a type-spec doc. A typed artifact carries frontmatter like:

```yaml
type: ../types/adr.md
```

The path may be repository-relative (`kb/...`) or file-relative (`./...` or `../...`). It must end with `.md`, resolve under `kb/`, and must not be absolute or be a URL. Repository-relative paths must not contain `..`.

## Type Specs

A type-spec doc is a normal markdown file with frontmatter:

```yaml
type: kb/types/type-spec.md
name: adr
description: Architecture decision record for accepted or proposed system decisions
schema: ./adr.schema.yaml
```

The body contains authoring instructions and an optional template block. The validator does not inspect the body; it reads `schema:` and validates artifacts against that schema. `schema:` accepts the same path forms as `type:`, except it must end with `.schema.yaml`. `schema: null` means the type has no structural schema.

`kb/types/type-spec.md` is the root type spec. It points at itself with `type: kb/types/type-spec.md`, which terminates type resolution.

## Resolution

For a file with no frontmatter, validation returns implicit `text` and applies no schema.

For a file with frontmatter, `type:` is required. The validator opens the referenced type-spec doc, verifies that it is itself a type spec, loads the declared schema when present, and validates the parsed markdown document against that schema. Missing type files, bare enum values, absolute paths, URLs, paths escaping `kb/`, and `type: kb/types/text.md` fail validation.

Collection scoping no longer participates in explicit type resolution. Collections offer types by listing readable names and paths in `COLLECTION.md`; artifacts store the chosen path directly.

## Authoring

`cp-skill-write` composes three ordinary files at read time:

- `kb/instructions/cp-skill-write/SKILL.md` for global writing mechanics
- the target collection's `COLLECTION.md` for register and linking conventions
- the selected type-spec doc for artifact shape

There is no resolver CLI, no generated write-context packet, and no legacy old split sidecar lookup.

## Related

- [available-types](./available-types.md) - shipped type inventory
- [collections-and-types](./collections-and-types.md) - how collections offer path-valued types
- [018-types-are-path-references-to-instruction-docs](./adr/018-types-are-path-references-to-instruction-docs.md) - accepted decision
