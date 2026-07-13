---
description: Imperative deterministic type rules dispatch by canonical path-valued type identity, preventing same-named local types from inheriting framework rules
type: ../types/adr.md
tags: []
status: accepted
---

# 048-Imperative type rules dispatch by canonical path

**Status:** accepted
**Date:** 2026-07-13

## Context

Commonplace type identity is path-valued: `kb/types/tag-readme.md` and `kb/notes/types/tag-readme.md` are different types even if both specifications declare `name: tag-readme`. The imperative `_TYPE_RULES` registry instead keyed registrations and dispatch on that bare name. A same-named collection-local type could therefore inherit framework behavior it did not declare.

Installed Commonplace content adds one wrinkle. A framework type shipped at `kb/types/x.md` lives at `kb/commonplace/types/x.md` in a reader project, but schemas already treat those paths as the same portable framework identity.

## Decision

Imperative type rules register and dispatch by canonical path-valued type identity.

- Registrations name complete source identities such as `kb/types/tag-readme.md`.
- Dispatch uses the resolved `TypeProfile`, not its display `name`.
- `canonical_type_identity` is the shared normalization: an installed `kb/commonplace/...` framework path maps to its source `kb/...` identity; ordinary collection-local paths remain unchanged.
- Finding labels continue to show the concise type name. Reporting vocabulary is not identity.

## Consequences

- Collection-local types may reuse a framework type's name without receiving its imperative rules.
- Framework rules behave identically in the author repository and installed reader repositories.
- Registrations are slightly longer but make applicability inspectable without resolving a global name convention.
- This fixes type applicability only. It does not introduce KB-authored imperative rules or unify schema and imperative checks behind one execution model.

## Links

- [Validation contract](../validation-contract.md) — implemented-by: type-owned rules retain their reporting source while selecting by canonical identity
- [ADR 050 — Validation runs share parsed artifacts and collection indexes](./050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) — part-of: run-scoped dispatch preserves canonical type applicability
