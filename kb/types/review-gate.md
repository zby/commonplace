---
type: kb/types/type-spec.md
name: review-gate
description: A single quality check the Commonplace review system applies to KB artifacts
schema: kb/types/review-gate.schema.yaml
---

# Review gate

## Authoring Instructions

A review gate is one quality check the review system applies to KB artifacts. Each gate is a single markdown file telling a reviewer what failure to look for and how to decide PASS, WARN, or INFO. The review system discovers gates by filesystem location (`kb/instructions/review-gates/{lens}/{name}.md`); this type contract enforces the shape every gate must carry. See `kb/reference/README-REVIEW-SYSTEM.md` for runtime concepts (bundles, freshness, acceptance) and `kb/reference/review-architecture.md` for the code architecture.

## Frontmatter

- `gate_id: {lens}/{name}` — matches the file path under `kb/instructions/review-gates/`.
- `name: {Human-Readable Name}` — used in rendered reviews.
- `lens: {bundle}` — the bundle this gate belongs to (`accessibility`, `semantic`, `structural`, `complexity`, `prose`, `frontmatter`, `sentence`).
- `watches: [body | frontmatter | ...]` — which parts of the target the gate inspects.
- `staleness: changed | always | ...` — when an accepted review becomes stale.
- `description` — the trigger condition: what kind of authoring problem this gate catches.
- `type: kb/types/review-gate.md`.
- Optional `requires_trait` or `requires-type` — narrow the gate to a subset of artifacts that carry the given trait or type.

## Body

- `## Failure mode` — the failure the reviewer is looking for, stated as the concrete pattern that should not appear.
- `## Test` — the procedure for deciding PASS, WARN, or INFO. Name exceptions explicitly so the reviewer does not double-flag adjacent gates.
- Optional `## Example (pass)` and `## Example (fail)` blocks make the test concrete. Most existing gates carry at least one of each — copy their shape rather than reinventing it.
- **The test must be self-contained.** Review freshness hashes only note text and gate text, so a test that leans on prose living elsewhere (a type spec, a collection convention) carries a dependency that never invalidates acceptances. If the test needs contract language, quote it in the gate body — that converts the dependency into hashed gate text, and editing the gate to track a moved contract fires `gate-changed` through the normal path. Conformance to a type's contract as a whole is not a catalog gate's job: that is the type-conformance pair, whose gate side is the type spec itself (ADR 038). A gate scoped by `requires-type` owns a sharper, named failure mode and should state its boundary with the conformance pair.

## Template

```markdown
---
gate_id: {lens}/{name}
name: {Human-Readable Name}
description: '{What kind of authoring problem this gate catches.}'
type: kb/types/review-gate.md
lens: {lens}
watches: [body]
staleness: changed
---

## Failure mode

{Concrete pattern that should not appear.}

## Test

{Procedure for deciding PASS, WARN, or INFO. Name exceptions explicitly.}

## Example (fail)

{Minimal failing example.}

## Example (pass)

{Minimal passing example.}
```
