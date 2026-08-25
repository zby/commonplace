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

The deterministic validation CLI interpreted one target argument twice: path selection and the decision whether collection-scoped orphan and structure checks applied each resolved the target independently. A new target form could therefore be added to one interpretation but omitted from the other.

Type-spec referential validation had a separate indirect seam. To verify a type-spec's declared schema, its imperative rule went through the note-oriented type resolver, representing the definition as a fictional note referring to itself and reopening frontmatter already parsed by normal validation.

## Decision

Resolve each validation target once. Resolution returns the selected paths together with the selected collection when the target denotes a collection. Collection scope is explicit target semantics: it is not inferred from coincidental membership of `recent`, `types`, or direct-file results. Batch labels, authored-link orphan calculation, and collection-structure validation derive from that stored collection.

Load type definitions directly. One definition-loading contract accepts an identified type-spec path, the repository root, and optional already-parsed frontmatter, validates the definition fields, and loads the declared schema. Note-oriented type resolution validates a note's `type:` reference and delegates to it; the `type-spec` imperative rule delegates with the current artifact and parsed frontmatter, removing synthetic self-resolution and the second frontmatter read.

## Consequences

- Target selection and collection-wide validation behavior cannot drift between two raw-argument interpreters.
- `recent`, `types`, and direct-file targets retain non-collection semantics even when their paths happen to lie in one collection.
- Ordinary note resolution and type-spec referential validation use one definition-loading contract and retain existing error messages and installed-path normalization.

## Links

- [ADR 047 — Type specifications use normal deterministic validation](./047-type-specifications-use-normal-deterministic-validation.md) — implements: simplifies the type-owned referential rule without changing its contract
- [ADR 048 — Imperative type rules dispatch by canonical path](./048-imperative-type-rules-dispatch-by-canonical-path.md) — preserves: direct loading retains canonical path-valued identity
- [Validation contract](../validation-contract.md) — part-of: collection scope and type-owned referential checks remain behaviorally unchanged
- [ADR 050 — Validation runs share parsed artifacts and collection indexes](./050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) — extended-by: resolved paths and collection scope now seed one shared execution context
