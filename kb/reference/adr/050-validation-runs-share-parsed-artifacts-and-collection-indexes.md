---
description: Validation is evaluated by a library-owned run that parses target artifacts once and shares collection indexes across anchored checks
type: ../types/adr.md
tags: []
status: accepted
---

# 050-Validation runs share parsed artifacts and collection indexes

**Status:** accepted
**Date:** 2026-07-13

## Context

Deterministic validation had one per-note pipeline in the library, but the CLI separately expanded impacted tag-READMEs, built the collection inbound-link graph, merged orphan findings, and checked collection structure. A collection sweep consequently parsed target artifacts three times — during impact selection, orphan calculation, and per-note validation — and each marked tag-README rescanned its collection independently.

## Decision

Evaluate each resolved target through one library-owned validation run.

- The run parses each artifact once and caches it by path. Target expansion, collection indexes, orphan calculation, and per-note validation consume those cached values.
- One lazy collection scan supplies both tag membership and tag-index entries. The collector remains shared with generated-index construction; validation injects its cached document loader rather than defining a second membership algorithm.
- Marked tag-README impact selection remains an explicit invalidation selector. No generic dependency keys, inverse graph, old/new-state model, or KB-authored imperative mechanism is introduced.
- The authored-link inbound graph is built once for a collection-scoped run and its orphan information is attached to each applicable artifact's results in the library.
- Collection-structure failures move to the library and carry the offending `COLLECTION.md` path as their anchor while retaining the existing batch presentation.
- The run returns expanded paths, per-artifact results, and anchored collection-structure findings. The CLI retains target resolution and presentation only.
- Per-artifact dispatch remains base checks, canonical-path imperative type rules, then schema validation. Single-note validation uses a one-path run.

## Consequences

Easier:

- Target artifacts are read and parsed once per validation run, including when tag membership and orphan checks need them.
- Multiple marked tag-READMEs share one collection scan rather than rescanning independently.
- Wide checks no longer require a new hand-merged branch in the CLI; their findings enter through the run result.
- CLI target semantics and validation execution have a narrow, explicit boundary.

Harder:

- Imperative type rules now receive the current run rather than only the repository root so referential checks can use shared inputs.
- The validation library owns run orchestration as well as individual check functions.

Not included:

- schema- or referent-change fan-out;
- a general dependency or incremental-build engine;
- a unified schema/imperative check object interface;
- collection- or KB-authored executable checks.

## Links

- [Validation contract](../validation-contract.md) — implemented-by: the deterministic finding sources retain their existing order inside the run
- [Generalized validation invalidation and imperative extension](../proposals/generalized-validation-invalidation-and-imperative-extension.md) — leaves-open: dependency generalization and local imperative extension remain deferred
- [ADR 049 — Validator resolution returns scope and loads types directly](./049-validator-resolution-returns-scope-and-loads-types-directly.md) — extends: the resolved target's paths and optional collection become the run boundary
- [ADR 026 — Tag-README type with completeness and coverage marks](./026-tag-readme-type-with-completeness-and-coverage-marks.md) — preserves: explicit reactive impact selection and deterministic mark enforcement
