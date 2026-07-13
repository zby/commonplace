---
description: Validation target resolution now returns paths with explicit collection scope, while type resolution and type-spec checks share direct definition loading
type: ../types/adr.md
tags: []
status: accepted
---

# 049-Validator resolution returns scope and loads types directly

**Status:** accepted
**Date:** 2026-07-13

## Context

The deterministic validation CLI interpreted one target argument twice. `resolve_targets` selected paths, while `batch_scope` repeated directory resolution to decide whether collection-scoped orphan and structure checks applied. A new target form could therefore be added to one interpretation but omitted from the other.

Type-spec referential validation had a separate indirect seam. To verify the schema declared by a type-spec document, its imperative rule fabricated `{"type": <the document's own path>}` and called the note-oriented `resolve_type`. This correctly loaded the declared schema but represented the definition as a fictional note referring to itself and reopened frontmatter already parsed by normal validation.

## Decision

Resolve each validation target once. `resolve_validation_target` returns `ResolvedValidationTarget`, containing an immutable tuple of selected paths and the selected collection path when the original target denotes a collection. Collection scope is explicit target semantics: it is not inferred from coincidental membership of `recent`, `types`, or direct-file results. Batch labels, authored-link orphan calculation, and collection-structure validation derive from that stored collection.

Load type definitions directly. `resolve_type_definition` accepts an identified type-spec path, repository root, and optional already-parsed frontmatter, then validates the definition fields and resolves and loads its declared schema. The note-oriented `resolve_type` validates a note's `type:` reference and delegates to this function. The `type-spec` imperative rule delegates with the current artifact and parsed frontmatter, removing synthetic self-resolution and the second frontmatter read.

## Consequences

- Target selection and collection-wide validation behavior cannot drift between two raw-argument interpreters.
- `recent`, `types`, and direct-file targets retain non-collection semantics even when their paths happen to lie in one collection.
- Ordinary note resolution and type-spec referential validation use one definition-loading contract and retain existing error messages and installed-path normalization.
- The new values and function names replace the former internal APIs; no compatibility wrapper remains.
- At this decision, wide checks retained their existing responsibilities. [ADR 050](./050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) later moved their orchestration behind one library-owned validation run without changing target semantics.

## Links

- [ADR 047 — Type specifications use normal deterministic validation](./047-type-specifications-use-normal-deterministic-validation.md) — implements: simplifies the type-owned referential rule without changing its contract
- [ADR 048 — Imperative type rules dispatch by canonical path](./048-imperative-type-rules-dispatch-by-canonical-path.md) — preserves: direct loading retains canonical path-valued identity
- [Validation contract](../validation-contract.md) — part-of: collection scope and type-owned referential checks remain behaviorally unchanged
- [ADR 050 — Validation runs share parsed artifacts and collection indexes](./050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) — extended-by: resolved paths and collection scope now seed one shared execution context
