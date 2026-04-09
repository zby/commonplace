# Workshop: Type System Rationalization

This workshop is now mostly complete. The implemented design has been promoted into ADRs, and the exploratory notes that led to those decisions have been removed from the active workshop.

## Accepted outcomes

- [ADR-012: types for structure, traits for review](../../notes/adr/012-types-for-structure-traits-for-review.md)
- [ADR-015: standardize authored type definitions on JSON Schema](../../notes/adr/015-standardize-authored-type-definitions-on-json-schema.md)

Together these ADRs capture the settled design:

- types are structural
- traits route semantic review
- frontmatter `type` identifies artifact kind
- directory-local `types/` directories scope definition lookup rather than replacing type identity
- bare type names remain acceptable while unambiguous
- machine-readable type definitions are authored JSON Schema in YAML syntax

## What remains in this workshop

Only the parts that are still deferred or intentionally not implemented:

- [review-integration.md](./review-integration.md) — deferred review-system work, especially recursive sweep expansion and parity checks
- [migration-plan.md](./migration-plan.md) — short backlog for the remaining deferred work

## Why these parts remain local

The remaining work is mostly operational sequencing, not unresolved type-system theory.

In particular, recursive sweep expansion under `kb/notes/**` is intentionally deferred because changing the review base while the DB and review tooling are still moving would create unnecessary churn.

## Historical note

This workshop originally reconciled three competing signals:

- frontmatter `type`
- directory-scoped `types/` templates
- path-based conventions and exemptions

That design work is now captured by the ADRs above. The workshop stays only as a holding area for the deferred review-side follow-up.
