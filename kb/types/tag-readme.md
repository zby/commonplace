---
type: kb/types/type-spec.md
name: tag-readme
description: A tag's curated head — small by type contract (weight-gated), with optional validator-enforced completeness (complete) and coverage (covered_by) marks
schema: kb/types/tag-readme.schema.yaml
---

# Tag README

## Authoring Instructions

A tag-README (`<tag>-README.md`) is the tag's curated head: a short orientation paragraph plus selective editorial picks with context phrases. It mirrors the directory convention — a directory's curated head is `README.md`, a tag's is `<tag>-README.md`.

A tag-README is understood standalone; this spec is **maintenance-path only**. Readers never need it — the field names are self-describing and the body is ordinary curated prose. Load this spec when *maintaining* a tag-README: declaring or dropping a mark, fixing a validator warning, or executing a lifecycle exit.

- Write a short orientation paragraph explaining what the tag covers and how to use the page.
- Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- Be selective by default. Completeness is the build's job (the published site appends the full generated listing) and the scoped query's job (`rg` recipes in `kb/reference/navigation.md`) — not the author's, unless the `complete` mark is declared.
- Do not hand-write a complete listing without declaring `complete: true`; do not claim child tags cover the tag in prose without declaring `covered_by` — unenforced versions of either claim decay silently into the stale-index failure.

## Frontmatter

- `index_source: tag` with `index_key: <tag>` — a tag's README. `index_source: tag-indexes` — the hub (`tags-README.md`), whose build-time listing enumerates tag pages instead of tagged notes.
- `complete: true` (optional) — this README links **every** note carrying the tag. Validator-enforced; readers may skip the by-tag `rg` sweep.
- `covered_by: [child-a, child-b]` (optional) — every note carrying the tag also carries at least one listed child tag. Validator-enforced; readers may trust the typed routing. This list is the only symbolic tag-to-tag relation; "Related Tags" prose stays editorial.

## What a mark is

A **mark** is a frontmatter field that caches a value recomputable from ground truth recorded elsewhere, is validated by code against that ground truth, and is read by an agent to spare it an expensive in-context recompute. `complete` and `covered_by` are the two marks; both cache tag membership, which the scoped `rg` sweep (`kb/reference/navigation.md`) always recovers.

Two properties define a mark, and any future mark must hold both:

- **Recomputable, therefore never load-bearing.** The ground truth lives elsewhere; the mark only copies it. No consumer's correctness may depend on a mark being present — dropping one costs a single recomputation, never correctness.
- **Code-validated, therefore enforce-or-omit.** A *false* mark (claiming complete/covered while members are missing) tells exhaustive consumers to stop looking while items are still out there — the sharpest form of the failure in `kb/notes/stale-indexes-are-worse-than-no-indexes.md`. The unenforced prose version of a checkable claim ("this list is complete", with no validator behind it) is that catastrophic state with none of the protection, and must never be written.

Marks earn their maintenance cost only because the consumer is an agent, for which the recompute is dear; for code the same field would be premature denormalization. That is the value half (`kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`) composed with the safety half (`kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`). A content-hash anchor is deliberately *not* a mark: it records a non-recomputable past state and is consumed by code, not read by the model, so it fails both properties. ADR 026 is the decision record.

## The weight contract

Every tag-README is small by type contract: validation warns past **8 KB** and fails past **16 KB** (bytes; entry count is reported as diagnosis). No exemptions. Remedies past threshold: curate harder, split the tag, or narrow it.

## Maintaining the marks

Enforcement is reactive (the two properties above are why): writing a note does not require touching any README; the validator queues the gap when the marked README is next validated, and its message routes here.

**`complete` lifecycle.** Declare it only while full membership fits under the weight gates. Each new tagged note then queues a README entry (add the link with a context phrase). A complete README crossing the soft warn is the early signal the tag is outgrowing completeness. Exits, in order of preference:

1. **Drop to selective** (default): remove the mark, trim to the editorial best-of; readers fall back to `rg`.
2. **Split with overlap** (only when the groupings reveal real substructure): mint child tags; child-tagged notes **keep the parent tag**; this README goes selective and links the child READMEs. Never split so that only some members keep the parent tag — partial migration makes the structure invisible.
3. Retiring the parent tag is a decision about the concept dissolving, never a size remedy.

**`covered_by` maintenance.** The check is membership(tag) ⊆ union of the children's memberships: a new note tagged with the parent must (eventually) take a listed child tag, or the validator flags the README. Validation also warns past a fan-out of ~7 children — the remedy is recursive (group children under intermediate tags), not a longer list. Watch for the catch-all-child smell: a `<tag>-misc` child satisfies coverage trivially while destroying its routing value.

For the audit workflow (groupings, orphans, splits), read `kb/instructions/maintain-curated-indexes.md`. For the full design rationale, read ADR 026.

## Template

```markdown
---
description: "Curated head for the {tag-name} tag — orientation plus selective picks"
type: kb/types/tag-readme.md
index_source: tag
index_key: "{tag-name}"
---

# {tag-name}

{Orientation: what this tag covers and how to use this page.}

## {Grouping}

- [note](./note.md) — why it matters here

## Related Tags

- [other-tag-README](./other-tag-README.md) — how it connects
```
