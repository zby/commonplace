---
type: types/type-spec.md
name: tag-readme
description: A tag's curated head at kb/tags/<tag>-README.md — small by type contract (weight-gated), with an optional validator-enforced completeness mark (complete) meaning every member is reached in one hop across the KB's participating collections
schema: ./tag-readme.schema.yaml
---

# Tag README

## Authoring Instructions

A tag-README is the tag's curated head: a short orientation paragraph plus selective editorial picks with context phrases. It lives at `kb/tags/<tag>-README.md`, and the filename is its identity: the file names the tag, and nothing else does ([ADR 089](../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)). It mirrors the directory convention — a directory's curated head is `README.md`, a tag's is `<tag>-README.md`.

Every tag in use has a head. The validator reports a tag on an artifact in a participating collection whose head does not exist; the remedy is to write the head or drop the tag. A head may be minimal: what qualifies for the tag, and a few picks.

A tag-README is understood standalone — the field names are self-describing and the body is ordinary curated prose. This spec is **maintenance-path only**: load it when writing a head, declaring or dropping the mark, fixing a validator warning, or executing a lifecycle exit.

- Open with what the tag gathers, in the words a reader would search for, and name the defining note if the tag has one. State what makes an artifact qualify for the tag: the subject, question, or mechanism it must substantively address. Mentioning the topic or using it as background is insufficient. A writer must be able to justify or challenge an assignment from this opening without inferring the rule from the picks.
- Where neighboring tags could be confused, state the boundary: what belongs here and what belongs under the neighbor. Tags may overlap when an artifact meets both inclusion conditions; a boundary is not a demand to choose only one tag. Ordinary prose is sufficient; no fixed heading or formal predicate is required.
- Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- Be selective by default. Completeness is the build's job (the published site appends the full generated listing) and the scoped query's job (`rg` recipes in `kb/reference/navigation.md`) — not the author's, unless the `complete` mark is declared.
- Do not hand-write a complete listing, or claim in body text that the linked child heads cover the tag, without declaring `complete: true` — an unenforced version of that claim decays silently into the stale-index failure.

Assignment fit is judged during authoring and semantic review. The deterministic validator checks head existence, structure, links, weight, and declared completeness; it does not establish that an artifact fits the tag's meaning.

## Scope

Membership ranges over the collections that `kb/tags/COLLECTION.md` declares in its `participating:` list, and over nothing else. The mark, the generated tail on the published site, and the head requirement read that one declaration. Artifacts outside it may carry `tags:` lines; no tag consumer reads them.

## Frontmatter

- `complete: true` (optional) — every artifact carrying the tag, across the participating collections, is linked from this head or carries a tag whose head is linked from this head: the head reaches every member in one hop. Validator-enforced; readers may skip the by-tag `rg` sweep. Children are the heads the body links; no list names them, and a link's context phrase says whether the linked head is a child or a neighbour ([ADR 090](../reference/adr/090-one-completeness-mark-reaches-members-in-one-hop.md)).

The mark is a **validated cache** of tag membership, which the scoped `rg` sweep (`kb/reference/navigation.md`) always recovers. Two properties follow, and any future mark must keep both: **recomputable, therefore never load-bearing** — dropping the mark costs one recomputation, never correctness; and **enforced-or-omitted** — a false mark tells exhaustive consumers to stop looking while members are still out there (`kb/notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`). A mark that cannot be made true without a weak child tag or a tag created to hold a few notes is dropped, or those members are linked by hand, which satisfies it. ADR 026 is the decision record for marks; ADR 090 folded its two marks into this one; the theory is the value half (`kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`) composed with the safety half (`kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`); the PKM grounding is `kb/notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md`.

## The weight contract

Every tag-README is small by type contract: validation warns past **8 KB** and fails past **16 KB** (bytes; entry count is reported as diagnosis). No exemptions. Remedies past threshold: curate harder, split the tag, or narrow it.

## Maintaining the mark

Enforcement is reactive (the two properties above are why): writing a note does not require touching any head; the validator queues the gap when the marked head is next validated, and its message routes here. Because membership spans collections, a clean validation of one collection does not clear a head: validate `kb/tags/` after tagging artifacts anywhere in the participating set.

**Declaring it.** Declare `complete` while the head can reach every member in one hop under the weight gates: link the load-bearing members directly and link the child heads whose tags cover the rest. Each new member then either carries a child tag whose head is linked, or queues a direct entry (add the link with a context phrase). A complete head crossing the soft warn is the early signal to split.

**Exits, in order of preference:**

1. **Drop to selective** (default): remove the mark, trim to the editorial best-of; readers fall back to `rg`.
2. **Split with overlap** (only when the groupings reveal real substructure): mint child tags with their own heads; child-tagged notes **keep the parent tag**; this head links the child heads and keeps the mark if the hop still reaches everyone. Never split so that only some members keep the parent tag — partial migration makes the structure invisible.
3. Retiring the parent tag is a decision about the concept dissolving, never a size remedy.

Watch for the catch-all-child smell: a `<tag>-misc` child satisfies the hop trivially while destroying its routing value; list such members by hand instead.

For the audit workflow (groupings, orphans, splits), read `kb/instructions/maintain-curated-indexes.md`. For the design rationale, read ADR 026 (marks and weight), ADR 089 (place, identity, scope), and ADR 090 (one mark).

## Template

```markdown
---
description: "Curated head for the {tag-name} tag — what it gathers, in a reader's words, plus selective picks"
type: types/tag-readme.md
---

# {tag-name}

{Opening: what an artifact must substantively address to qualify, the defining note if there is one, the boundary with confusing neighbors, and how to use this page.}

## {Grouping}

- [note](../notes/note.md) — why it matters here

## Related Tags

- [other-tag](./other-tag-README.md) — how it connects
```
