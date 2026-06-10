---
description: Audit and maintain curated tag-index pages — evaluate editorial groupings, check for orphaned notes, and split or merge indexes where needed.
type: kb/types/instruction.md
---

# Maintain curated indexes

Audit curated tag READMEs (`<tag>-README.md`, type `tag-readme`) for editorial quality, completeness, and coherence. A tag README is the tag's curated head: a hand-written editorial body with groupings and context phrases, small by type contract (weight gates). The complete per-tag listing is not committed — it is generated at mkdocs build time for the published site (ADR 025); agents reconstruct it on demand with the scoped `rg` recipe below.

This instruction is also the route for fixing validator warnings on tag-READMEs (weight gate, `complete` membership, `covered_by` coverage and fan-out). The marks' maintenance rules — when to declare or drop `complete`/`covered_by`, the lifecycle exits, the smells — live in the type spec, `kb/types/tag-readme.md`; read it before changing a mark.

## When to use

- During periodic KB hygiene
- After a batch of new notes have been added to a tag
- When navigating an index feels disoriented — too many entries, unclear groupings, missing context

## Steps

### 1. Inventory tags and sizes

```bash
rg -N --no-heading '^tags:' kb/notes/ --glob '*.md' \
  | grep -o '\[.*\]' | tr -d '[]' | tr ',' '\n' | sed 's/^ *//' \
  | sort | uniq -c | sort -rn
```

This shows how many notes each tag has. Tags with many notes but no curated index are candidates for curation. Indexes that haven't been updated after significant tag growth may need revision.

### 2. For each curated index, evaluate editorial quality

Load the index and list the tag's full membership:

```bash
rg -l '^tags:.*\bTAG\b' kb/notes/ --glob '*.md' \
  | xargs -r rg -N --no-heading '^description:\s*' -r ''
```

Ask:

- **Do the groupings still make sense?** Sections should reflect natural clusters. If a section has grown to 15+ entries, it may need sub-grouping or splitting into its own index.
- **Are the context phrases still accurate?** A note's role in the topic may have shifted since the phrase was written.
- **Are important notes missing?** Compare the curated entries against the tag's full membership from the listing above. Tagged notes absent from the index are either: (a) not important enough to curate, which is fine, or (b) missing editorial placement, which should be fixed.
- **Are there entries that no longer belong?** A curated entry whose note has drifted away from the topic should be removed (the note stays reachable through the build-time listing and the scoped query).

### 3. Check for orphaned notes

```bash
# Notes with no tags field at all
rg -L "^tags:" kb/notes/*.md
```

For each orphan, consider whether adding tags would help future readers find it.

### 4. Split or promote

When a tag grows large and internal clusters emerge:

1. Look at the curated groupings — these often reveal natural sub-tags.
2. Create a new `<tag>-README.md` with `type: kb/types/tag-readme.md`, `index_source: tag`, and `index_key: <tag>` (template in the type spec).
3. Add the new tag to relevant notes' `tags:` field — keeping the parent tag on every note (never a partial migration; see the split discipline in `kb/types/tag-readme.md`).
4. Write the curated body for the new README; the complete listing appears on the published site automatically.

**Split criteria:**
- Would the resulting indexes each have 5+ notes?
- Do the clusters represent genuinely distinct topics, or just editorial convenience?

### 5. Update tags-README.md

Ensure `kb/notes/tags-README.md` lists all tag READMEs. This is the hub page readers use to browse by tag.

## Principles

- The curated index is editorial, not exhaustive — it's a "best of" selection with context, not a complete listing.
- Completeness is handled elsewhere — the build-time site listing for humans, the scoped `rg` query for agents. Don't chase complete coverage in the curated body unless a note is genuinely important for the topic's story.
- Groupings serve readers, not taxonomy — optimize for "does this help someone understand the topic?" not "is this logically clean?"
