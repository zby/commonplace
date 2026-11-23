---
type: types/type-spec.md
name: tag-readme
description: A selective introduction to a tag, with an inclusion condition and editorial picks; use the membership collector for exact enumeration.
schema: ./tag-readme.schema.yaml
---

# Tag README

## Authoring Instructions

A tag-README is the tag's curated head: a short orientation paragraph plus selective editorial picks with context phrases. It lives at `kb/tags/<tag>-README.md`, and the filename is its identity: the file names the tag, and nothing else does ([ADR 089](../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)). It mirrors the directory convention — a directory's curated head is `README.md`, a tag's is `<tag>-README.md`.

Every tag in use has a head. The validator reports a tag on an artifact in a participating collection whose head does not exist; the remedy is to write the head or drop the tag. A head may be minimal: what qualifies for the tag, and a few picks.

A tag-README is understood standalone — the field names are self-describing and the body is ordinary curated prose. This spec is **maintenance-path only**: load it when writing a head, fixing a validator warning, or executing a lifecycle exit.

- Open with what the tag gathers, in the words a reader would search for, and name the defining note if the tag has one. State what makes an artifact qualify for the tag: the subject, question, or mechanism it must substantively address. Mentioning the topic or using it as background is insufficient. A writer must be able to justify or challenge an assignment from this opening without inferring the rule from the picks.
- Where neighboring tags could be confused, state the boundary: what belongs here and what belongs under the neighbor. Tags may overlap when an artifact meets both inclusion conditions; a boundary is not a demand to choose only one tag. Ordinary prose is sufficient; no fixed heading or formal predicate is required.
- Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- A head is selective. Recommend useful starting points; do not promise exhaustive coverage. A small head may happen to link every member.

Assignment fit is judged during authoring and semantic review. The deterministic validator checks head existence, structure, links, and weight; it does not establish that an artifact fits the tag's meaning.

## Scope

Membership ranges over the collections that `kb/tags/COLLECTION.md` declares in its `participating:` list, and over nothing else. The generated tail on the published site, and the head requirement read that one declaration. Artifacts outside it may carry `tags:` lines; membership consumers do not read them. Explicit source-scoped searches may read tags on tracked source analyses under the source collection contract. These search results are outside the member listing, even when they reuse its topic vocabulary.

### Checking exact membership

On the published site, the curated links and generated listing together cover the members. In a Commonplace checkout, run this from the repository root, replacing `evaluation` with the tag name:

```bash
uv run python - evaluation <<'PY'
import sys
from pathlib import Path
from commonplace.lib.index_generated import collect_tag_space

root = Path.cwd()
space = collect_tag_space(root)
if space.declaration_error:
    sys.exit(space.declaration_error)
for path, _, description in space.notes_by_tag.get(sys.argv[1], []):
    print(f"{path.relative_to(root)}: {description}")
PY
```

The site build uses this collector. To check a tag assignment, validation reads the participation declaration and head filenames, not the member listing. A text search finds candidates, not exact membership: it can match ignored captures or miss multiline YAML tags.

## The weight contract

Every tag-README is small by type contract: validation warns past **8 KB** and fails past **16 KB** (bytes; entry count is reported as diagnosis). No exemptions. Remedies past threshold: curate harder, split the tag, or narrow it.

## Splitting a tag

Split only when the groupings are useful topics in their own right. Keep the parent tag on child-tagged members; never split so that only some members keep the parent tag. Relate the heads with a phrase explaining the connection. Retiring the parent tag is a decision about the concept, not a size remedy. For the audit procedure, see [maintain curated indexes](../instructions/maintain-curated-indexes.md).

## Template

```markdown
---
description: "Curated head for the {tag-name} tag — what it gathers, in a reader's words, plus selective picks"
type: types/tag-readme.md
---

# {tag-name}

{Opening: what an artifact must substantively address to qualify, the defining note if there is one, the boundary with confusing neighbors, and how to use this page.}

## {Grouping}

- [note](../theory/note.md) — why it matters here

## Related Tags

- [other-tag](./other-tag-README.md) — how it connects
```
