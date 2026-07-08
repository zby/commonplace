---
type: kb/types/type-spec.md
name: collection
description: Authoring contract for COLLECTION.md files — the per-collection routing and conventions document that also serves as the collection-conformance gate
schema: kb/types/collection.schema.yaml
---

# Collection

A `COLLECTION.md` is the local authoring contract of one [collection](../reference/definitions/collection.md): the conventions and routing rules that bind every artifact in its subtree, whatever the artifact's type. It is contract, not content — collection walks exclude it from note listings, and the collection-conformance lens never pairs it with itself ([ADR 041](../reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)).

The file serves three consumers: an author writing into the collection reads it for the local conventions before writing; the collection-conformance reviewer reads its body as the gate text judging every note in the collection; and the deterministic validator checks its frontmatter against this type's schema. Because the body is gate text, write it as a checkable contract — conventions a reviewer can apply to a finished note — not as narrative about the collection.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `kb/types/collection.md` |
| `description` | Yes | Retrieval description: the collection's role and what its contract governs. |

No `status` or `tags`: a contract is not a note moving through a writing lifecycle. The schema checks frontmatter only; body structure is deliberately unconstrained, because contracts legitimately vary by collection.

## Body contract

A conforming `COLLECTION.md` declares, in whatever structure fits the collection:

- **Purpose and register** — what the artifacts in this subtree do, and the register or content mode governing them.
- **Quality goal** — what makes an artifact worth keeping here, stated so a reviewer can test a note against it.
- **Title and description conventions** — how titles are formed and what frontmatter descriptions must carry.
- **Type guidance** — which type specs artifacts here use, global or collection-local.
- **Outbound-link policy** — which collections this one links into, with which labels.

Clauses must bind the whole subtree. A rule that binds only artifacts of one shape belongs in a type spec; a rule that binds only opted-in artifacts belongs in a trait. Do not restate a type spec's requirements — the type-conformance pair already enforces them, and the collection-conformance wrapper directs reviewers to judge only what the contract asks beyond the type contract.

An authored `## Review` section, when present, is the operative test for the collection-conformance gate; the freshness hash sees it, so sharpening criteria there stales exactly this collection's cohort.

## Template

```markdown
---
type: kb/types/collection.md
description: "{The collection's role and what its contract governs}"
---

# Writing conventions for kb/{collection}/ ({register})

{Purpose, register, quality goal, title and description conventions,
type guidance, outbound-link policy — structured as this collection needs.}
```
