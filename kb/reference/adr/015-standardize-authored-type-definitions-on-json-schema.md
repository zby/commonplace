---
description: Accepted decision to replace the custom type-profile DSL with authored JSON Schema over a parsed note document model
type: ../types/adr.md
tags: []
status: accepted
---

# 015-standardize-authored-type-definitions-on-json-schema

**Status:** accepted
**Date:** 2026-04-09
**Supersedes:** the former custom type-profile DSL (global and collection-local `types/*.yaml` profiles).

## Context

Commonplace previously defined note types through a custom YAML mini-language in global and collection-local `types/*.yaml` files, parsed and resolved by package-local type-resolution code.

This approach worked while the type layer was very small, but it left Commonplace owning:

- the schema vocabulary (`required_headings`, `required_fields`, `allowed_status`, `min_links`, and similar fields)
- parser behavior and error handling
- inheritance and merge semantics
- every future increase in expressiveness

One fallback was considered: keep the current mini-language and validate only its outer shape with JSON Schema. That was rejected because it does not standardize the actual constraint language. It only wraps the existing DSL in a stricter envelope while leaving Commonplace responsible for the semantics and future growth of the DSL.

## Decision

Commonplace uses **authored JSON Schema Draft 2020-12**, written in **YAML syntax**, for machine-readable type definitions.

The schema target is a **parsed note document model**, not raw markdown text. The stable validation object includes:

- `frontmatter`
- `body`
- `headings`

Additional parsed fields such as extracted links or dates may exist when needed by runtime checks, but markdown parsing remains local to Commonplace rather than embedded in schemas.

Type definitions therefore stop being custom profiles (`base`, `required_headings`, `required_fields`, and the like) and become direct schemas over parsed note objects.

To manage context costs, **templates remain the agent's writing interface** and **schemas are the verification interface**. Agents read templates on the happy path. Schemas are read by validation tooling, and only loaded into agent context on failure when debugging a concrete validation problem.

Commonplace still owns local logic for:

- parsing markdown into the document model
- scoped schema lookup by directory
- selecting which schema applies to which note
- non-schema checks such as link resolution and repository-specific placement rules
- translating schema validation errors into actionable guidance

## Consequences

**Easier:**
- Commonplace stops inventing and maintaining its own authored schema language.
- External schema tooling and standard JSON Schema features (`allOf`, `$ref`, conditional rules, `$defs`) become available directly.
- Richer type constraints no longer require adding new bespoke DSL fields first.
- The boundary between parsing and validation becomes clearer: parse markdown once, validate structured data.

**Harder:**
- Authored type definitions are more verbose and indirect than the old profiles.
- Maintainers must review and debug schemas rather than a very small declarative DSL.

---

Relevant Notes:

- [ADR-012: types for structure, traits for review](./012-types-for-structure-traits-for-review.md) — refined: keeps the structural role of types, but changes how type definitions are authored
