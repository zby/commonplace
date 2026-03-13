---
description: Audit and maintain curated sections of tag index pages — evaluate editorial groupings, check for orphaned notes, and split or merge indexes where needed.
---

# Maintain curated indexes

Audit curated index sections for editorial quality, completeness, and coherence. The generated section (rebuilt by `uv run scripts/sync_generated_index.py`) is always complete — this instruction focuses on the hand-written curated section above the `<!-- generated -->` marker.

## When to use

- During periodic KB hygiene
- After a batch of new notes have been added to a tag
- When navigating an index feels disoriented — too many entries, unclear groupings, missing context

## Steps

### 1. Inventory tags and sizes

```bash
uv run scripts/sync_generated_index.py --dry-run
```

This shows how many notes each tag has. Tags with many notes but no curated section are candidates for curation. Tags with curated sections that haven't been updated after significant growth may need revision.

### 2. For each curated index, evaluate editorial quality

Load the curated section. Ask:

- **Do the groupings still make sense?** Sections should reflect natural clusters. If a section has grown to 15+ entries, it may need sub-grouping or splitting into its own index.
- **Are the context phrases still accurate?** A note's role in the topic may have shifted since the phrase was written.
- **Are important notes missing?** Compare the curated section against the generated section. Notes in the generated list but absent from the curated section are either: (a) not important enough to curate, which is fine, or (b) missing editorial placement, which should be fixed.
- **Are there entries that no longer belong?** A curated entry whose note has drifted away from the topic should be removed from the curated section (it stays in the generated section automatically).

### 3. Check for orphaned notes

```bash
# Notes with no tags or empty tags
rg "^tags: \[\]" kb/notes/ --glob '*.md'
rg -L "^tags:" kb/notes/*.md
```

For each orphan, assign tags that help future readers find it. No minimum — even one tag is better than none.

### 4. Split or promote

When a tag's generated section grows large and internal clusters emerge:

1. Look at the curated section's groupings — these often reveal natural sub-tags.
2. Create a new tag index page (`{tag}-index.md`).
3. Add the new tag to relevant notes' `tags:` field.
4. Run `uv run scripts/sync_generated_index.py` to populate the generated section.
5. Optionally write a curated section for the new index.

**Split criteria:**
- Would the resulting indexes each have 5+ notes?
- Do the clusters represent genuinely distinct topics, or just editorial convenience?

### 5. Update tags-index.md

Ensure `kb/notes/tags-index.md` lists all curated indexes. This is the hub page readers use to browse by tag.

## Principles

- The curated section is editorial, not exhaustive — it's a "best of" selection with context, not a complete listing.
- The generated section handles completeness — don't worry about missing notes in the curated part unless they're genuinely important for the topic's story.
- Groupings serve readers, not taxonomy — optimize for "does this help someone understand the topic?" not "is this logically clean?"
