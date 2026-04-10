# Review integration with types and traits

Most of the review-side type-system work is already implemented:

- gates can declare `requires_trait`
- `title-as-claim` review routing exists
- direct note-local runs and the selector both use the shared note-aware applicability helper

What remains here is the deferred follow-up.

## Current deferred boundary

The selector still discovers only top-level `kb/notes/*.md` files.

This means trait-gating behavior for notes below that level, especially definitions and related-system reviews, is not yet part of the sweep base. That is intentional for now: expanding the review base while the DB and review tooling are still in motion would create churn without adding enough immediate value.

## Deferred work

### Recursive sweep expansion

When the review DB is stable enough, update `review_target_selector.py` to discover frontmatter-bearing notes recursively under `kb/notes/**`.

### Parity verification

After recursive discovery lands, verify that:

- trait-gated gates are skipped for notes that do not carry the required trait
- direct note-local bundle runs and sweeps resolve the same applicable gates for the same note
- definitions and related-system reviews behave correctly once they enter sweep scope

### Future trait-gated review

The routing mechanism is general, but the system should stay conservative.

Possible later extensions:

- `definition` gating term-precision or boundary-coverage review
- `has-comparison` gating comparison-quality review
- `has-implementation` gating implementation-specific review

None of these are needed yet.

## Not revisited here

The core design is settled elsewhere:

- [ADR-012: types for structure, traits for review](../../reference/adr/012-types-for-structure-traits-for-review.md)
- [ADR-015: standardize authored type definitions on JSON Schema](../../reference/adr/015-standardize-authored-type-definitions-on-json-schema.md)
