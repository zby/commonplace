# Remaining migration plan

This workshop no longer tracks the implemented type-system design. For the accepted design, see:

- [ADR-012: types for structure, traits for review](../../notes/adr/012-types-for-structure-traits-for-review.md)
- [ADR-015: standardize authored type definitions on JSON Schema](../../notes/adr/015-standardize-authored-type-definitions-on-json-schema.md)

What remains here is the deferred review-side follow-up.

## Deferred work

### 1. Expand review sweep scope when the DB is stable

`review_target_selector.py` still discovers only top-level `kb/notes/*.md` files.

Recursive sweep expansion under `kb/notes/**` is deferred for now because broadening the review base while the DB and review tooling are still in motion would create unnecessary churn.

### 2. Verify parity after sweep expansion lands

Once recursive discovery is enabled, verify that:

- trait-gated gates are skipped for notes that do not carry the required trait
- direct note-local bundle runs and sweeps resolve the same applicable gates for the same note
- definitions and related-system reviews behave as expected once they are inside sweep scope

### 3. Revisit implied traits only if explicit traits become costly

The current system intentionally keeps trait computation simple: read `traits:` from frontmatter.

If explicit trait maintenance becomes burdensome, revisit whether some types should imply traits. Until then, keep the mechanism explicit.

### 4. Add more trait-gated review only when there is a real need

The current review integration is deliberately narrow. `title-as-claim` is the only trait with review-time routing effects today.

Future candidates:

- `definition` for term-precision or boundary-coverage review
- `has-comparison` for comparison-quality review
- `has-implementation` for implementation-specific review

Do this only when the review system reveals a concrete need.
