---
description: Audit and maintain curated tag-index pages — evaluate editorial groupings, check for orphaned notes, and split or merge indexes where needed.
type: types/instruction.md
---

# Maintain curated indexes

Audit curated tag READMEs (`kb/tags/<tag>-README.md`, type `tag-readme`) for editorial quality and coherence. A tag README is the tag's curated head: a hand-written editorial body with groupings and context phrases, small by type contract (weight gates). The complete per-tag listing is not committed — it is generated at ProperDocs build time for the published site (ADR 025); agents reconstruct it with the same membership collector the site uses.

For the head size limits and split rules, see the [tag-readme type spec](../types/tag-readme.md).

## When to use

- During periodic KB hygiene
- After a batch of new notes have been added to a tag
- When navigating an index feels disoriented — too many entries, unclear groupings, missing context

## Steps

### 1. Inventory tags and sizes

In the Commonplace checkout, run this from the repository root. It discovers member artifacts by collection and includes heads that currently have no members:

```bash
uv run python - <<'PY'
from pathlib import Path
from commonplace.lib.index_generated import collect_tag_space

space = collect_tag_space(Path.cwd())
for tag in sorted(space.heads.keys() | space.notes_by_tag.keys()):
    print(len({path for path, _, _ in space.notes_by_tag.get(tag, [])}), tag)
PY
```

A tag on an eligible artifact needs a head. If validation reports a missing head, write the head or drop the tag. Indexes that haven't been updated after significant tag growth may need revision.

### 2. For each curated index, evaluate editorial quality

Load the head. Run the [exact-membership recipe](../types/tag-readme.md#checking-exact-membership) with its tag name. This listing, not a text match on a `tags:` line, is the comparison set for the curated links. For source evidence beyond already tagged ingests, search `kb/sources/` directly.

Ask:

- **Can a writer decide placement from the opening?** It must state what an artifact must substantively address to qualify and distinguish confusing neighboring tags. Mention or background use is insufficient. Check a clear member and a nearby non-member against the wording; when both tags fit, allow both. Curated background links do not themselves assert membership.
- **Do the groupings still make sense?** Sections should reflect natural clusters. If a section has grown to 15+ entries, it may need sub-grouping or splitting into its own index.
- **Are the context phrases still accurate?** A note's role in the topic may have shifted since the phrase was written.
- **Are important notes missing?** Compare the curated entries against the tag's full membership from the listing above. Tagged notes absent from the index are either: (a) not important enough to curate, which is fine, or (b) missing editorial placement, which should be fixed.
- **Are there entries that no longer belong?** A curated entry whose note has drifted away from the topic should be removed (the note stays reachable through the build-time listing and the membership collector).

### 3. Find eligible notes with no tags

Choose the artifact class before treating an absent tag as a gap. This example covers `types/note.md` in `kb/theory/`, including subdirectories. It checks parsed frontmatter, so an absent field and an empty list both qualify. Other types are not implicitly candidates. Before extending the search, read the tag and destination contracts; instructions and ADRs, for example, are intentionally untagged in Commonplace.

```bash
uv run python - <<'PY'
from pathlib import Path
from commonplace.lib import frontmatter
from commonplace.lib.index_generated import collect_tag_catalog
from commonplace.lib.project_paths import list_collection_validation_paths

root = Path.cwd()
catalog = collect_tag_catalog(root)
for path in list_collection_validation_paths(root / 'kb/theory'):
    if path.suffix != '.md' or not catalog.is_member_candidate(path):
        continue
    doc = frontmatter.parse(path.read_text(encoding='utf-8'))
    if doc.ok and doc.data.get('type') == 'types/note.md' and doc.data.get('tags', []) == []:
        print(path.relative_to(root))
PY
```

Treat the output as a reading list, not a tagging backlog. Assign a tag only if the note meets its head’s inclusion condition and the assignment would help a reader find it. Clarify an ambiguous condition before assigning.

### 4. Split or promote

When a tag grows large and internal clusters emerge:

1. Look at the curated groupings — these often reveal natural sub-tags.
2. Create `kb/tags/<tag>-README.md` with a `description` and `type: types/tag-readme.md` (template in the type spec); the filename names the tag.
3. Add the new tag to relevant notes' `tags:` field — keeping the parent tag on every note (never a partial migration; see the split discipline in the [tag-readme type spec](../types/tag-readme.md)).
4. Write the curated body for the new README; the complete listing appears on the published site automatically.

**Split criteria:**
- Would the resulting indexes each have 5+ notes?
- Do the clusters represent genuinely distinct topics, or just editorial convenience?

### 5. Update the tags hub

Add a new head to `kb/tags/README.md`, the hub readers use to browse by tag. It is an ordinary collection landing, so nothing checks that it lists every head.

### 6. Validate the tag collection

Run `commonplace-validate kb/tags`. Check the edited heads for structure, weight and link warnings.

## Principles

- The curated index is editorial, not exhaustive — it's a "best of" selection with context, not a complete listing.
- Completeness is handled elsewhere — the build-time site listing for humans, the membership collector for agents. Don't chase complete coverage in the curated body unless a note is genuinely important for the topic's story.
- Groupings serve readers, not taxonomy — optimize for "does this help someone understand the topic?" not "is this logically clean?"
