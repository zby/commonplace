---
description: "Definition — a text contract is the binding local declaration in a collection's COLLECTION.md: purpose, quality goal, writing conventions, maintenance, and link grammar"
type: kb/types/definition.md
tags: [document-system]
---

# Text contract

The binding local declaration in a writable collection's `COLLECTION.md`. It
states the collection's purpose and scope, quality goal, title and description
conventions, any attribution or evidentiality requirements, maintenance
semantics, outbound link grammar, and other text-level rules needed to author
and review artifacts in that subtree.

The containing path selects one `COLLECTION.md`; that file is authoritative for
the collection. Its clauses must be stated locally and completely enough for an
agent to act without inferring conventions from the collection name or from a
different collection's contract.

## Scope

Use **text contract** for the requirements that govern an artifact's intended
contribution and writing quality because of the collection containing it. A
collection's purpose, quality goal, title convention, attribution rule,
maintenance rule, and authorized outbound relationships are text-contract
clauses.

Text contract is collection-facing vocabulary. Different collections may set
different goals and conventions even when their artifacts use the same type.
Moving an artifact across collection boundaries therefore changes the
applicable text contract and requires a fit check.

## Exclusions

A text contract is not an artifact type. A type contract owns frontmatter
semantics and structural requirements; the collection's text contract owns the
local authoring and review rules. Both apply independently to a typed artifact.

A text contract is also not a content kind, production relation, trait,
lifecycle status, or [behavioral authority](./behavioral-authority.md). Those
distinctions answer different questions and may vary within one artifact or
across its consumption paths.

## Misuse cases

- Inferring a collection's conventions from its directory name instead of
  reading its `COLLECTION.md`.
- Treating one collection's quality goal or title convention as a framework
  universal.
- Letting a collection redefine the semantics of a frontmatter field owned by
  the artifact's type contract.
- Assuming collection placement determines an artifact's truth, lineage, or
  behavioral force.

---

Relevant Notes:

- [Artifact classification separates content kind, lineage, and authority](../artifact-classification-separates-content-kind-lineage-and-authority.md) — contrasts: separates proposition-, region-, and path-level questions from the artifact's local writing contract
- [Directory placement is total, frontmatter classification is partial](../directory-placement-is-total-frontmatter-classification-is-partial.md) — grounds: explains why collection placement always selects a local contract while type metadata may be absent
- [Collections and types](../../reference/collections-and-types.md) — evidenced-by: documents how the shipped system composes collection and type contracts
