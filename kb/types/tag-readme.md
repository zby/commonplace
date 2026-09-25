---
type: types/type-spec.md
name: tag-readme
description: A tag's curated head at kb/tags/<tag>-README.md — small by type contract (weight-gated), with optional validator-enforced completeness (complete) and coverage (covered_by) marks over the KB's participating collections
schema: ./tag-readme.schema.yaml
---

# Tag README

## Authoring Instructions

A tag-README is the tag's curated head: a short orientation paragraph plus selective editorial picks with context phrases. It lives at `kb/tags/<tag>-README.md`, and the filename is its identity: the file names the tag, and nothing else does ([ADR 089](../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)). It mirrors the directory convention — a directory's curated head is `README.md`, a tag's is `<tag>-README.md`.

Every tag in use has a head. The validator reports a tag on an artifact in a participating collection whose head does not exist; the remedy is to write the head or drop the tag. A head may be minimal: what the tag gathers, and a few picks.

A tag-README is understood standalone — the field names are self-describing and the body is ordinary curated prose. This spec is **maintenance-path only**: load it when writing a head, declaring or dropping a mark, fixing a validator warning, or executing a lifecycle exit.

- Open with what the tag gathers, in the words a reader would search for, and name the defining note if the tag has one. A head that only summarises its picks hides what the tag means.
- Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- Be selective by default. Completeness is the build's job (the published site appends the full generated listing) and the scoped query's job (`rg` recipes in `kb/reference/navigation.md`) — not the author's, unless the `complete` mark is declared.
- Do not hand-write a complete listing without declaring `complete: true`; do not claim in body text that child tags cover the tag without declaring `covered_by` — unenforced versions of either claim decay silently into the stale-index failure.

## Scope

Membership ranges over the collections that `kb/tags/COLLECTION.md` declares in its `participating:` list, and over nothing else. Both marks, the generated tail on the published site, and the head requirement read that one declaration. Artifacts outside it may carry `tags:` lines; no tag consumer reads them.

## Frontmatter

- `complete: true` (optional) — this README links **every** artifact carrying the tag across the participating collections. Validator-enforced; readers may skip the by-tag `rg` sweep.
- `covered_by: [child-a, child-b]` (optional) — every artifact carrying the tag also carries at least one listed child tag, and every child has a head. Validator-enforced; readers may trust the typed routing. This list is the only symbolic tag-to-tag relation; "Related Tags" prose stays editorial.

Both marks are **validated caches** of tag membership, which the scoped `rg` sweep (`kb/reference/navigation.md`) always recovers. Two properties follow, and any future mark must keep both: **recomputable, therefore never load-bearing** — dropping a mark costs one recomputation, never correctness; and **enforced-or-omitted** — a false mark tells exhaustive consumers to stop looking while members are still out there (`kb/notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`). A mark that cannot be made true without a weak child tag or a tag created to hold a few notes is dropped, and the head lists the uncovered members by hand. ADR 026 is the decision record for the marks; the theory is the value half (`kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`) composed with the safety half (`kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`); the PKM grounding is `kb/notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md`.

## The weight contract

Every tag-README is small by type contract: validation warns past **8 KB** and fails past **16 KB** (bytes; entry count is reported as diagnosis). No exemptions. Remedies past threshold: curate harder, split the tag, or narrow it.

## Maintaining the marks

Enforcement is reactive (the two properties above are why): writing a note does not require touching any README; the validator queues the gap when the marked README is next validated, and its message routes here. Because membership spans collections, a clean validation of one collection does not clear a head: validate `kb/tags/` after tagging artifacts anywhere in the participating set.

**`complete` lifecycle.** Declare it only while full membership fits under the weight gates. Each new tagged note then queues a README entry (add the link with a context phrase). A complete README crossing the soft warn is the early signal the tag is outgrowing completeness. Exits, in order of preference:

1. **Drop to selective** (default): remove the mark, trim to the editorial best-of; readers fall back to `rg`.
2. **Split with overlap** (only when the groupings reveal real substructure): mint child tags with their own heads; child-tagged notes **keep the parent tag**; this README goes selective and links the child READMEs. Never split so that only some members keep the parent tag — partial migration makes the structure invisible.
3. Retiring the parent tag is a decision about the concept dissolving, never a size remedy.

**`covered_by` maintenance.** The check is membership(tag) ⊆ union of the children's memberships: a new note tagged with the parent must (eventually) take a listed child tag, or the validator flags the README. Validation also warns past a fan-out of ~7 children — the remedy is recursive (group children under intermediate tags), not a longer list. Watch for the catch-all-child smell: a `<tag>-misc` child satisfies coverage trivially while destroying its routing value.

For the audit workflow (groupings, orphans, splits), read `kb/instructions/maintain-curated-indexes.md`. For the design rationale, read ADR 026 (marks and weight) and ADR 089 (place, identity, scope).

## Template

```markdown
---
description: "Curated head for the {tag-name} tag — what it gathers, in a reader's words, plus selective picks"
type: types/tag-readme.md
---

# {tag-name}

{Orientation: what this tag gathers, the defining note if there is one, and how to use this page.}

## {Grouping}

- [note](../notes/note.md) — why it matters here

## Related Tags

- [other-tag](./other-tag-README.md) — how it connects
```
