---
description: Audit and rework area indexes to comply with read-together methodology — check size, precision, tagging, and split where needed.
---

# Rework Areas

Audit area indexes against the conventions in WRITING.md and the principles in [areas-exist-because-useful-operations-require-reading-notes-together](../notes/areas-exist-because-useful-operations-require-reading-notes-together.md). Fix tagging, split oversized areas, and ensure every note is in the most precise area.

## When to use

- After establishing or changing area conventions
- When an area exceeds ~40 notes
- During periodic KB hygiene

## Steps

### 1. Inventory areas and sizes

```bash
# Count notes per area
for area in $(rg -o 'areas: \[.*\]' kb/notes/ --glob '*.md' -r '$1' | grep -oP '[\w-]+' | sort | uniq); do
  count=$(rg -c "areas:.*$area" kb/notes/ --glob '*.md' | wc -l)
  echo "$area: $count"
done
```

Flag any area with 40+ notes for split evaluation.

### 2. For each area, evaluate precision

Load the area index. Ask: if I loaded all these notes together for comparative reading, what fraction would yield useful tensions, redundancies, or connections with each other?

- **High yield** — most note pairs are related. Area is well-scoped. No action needed.
- **Low yield** — many note pairs have nothing to say to each other. The area has internal clusters that should be separate areas.

### 3. Identify split candidates

For low-yield areas, look at the existing section structure in the index. Sections often reveal natural clusters. For each potential split:

- Would the resulting areas each have 5+ notes?
- Would comparative reading within each new area yield more than the current combined area?
- Are there high-tension pairs that must stay together?

### 4. Execute splits

For each split:

1. Create the new area index file in `kb/notes/`.
2. Re-tag notes: change `areas: [old-area]` to `areas: [new-area]` in each migrating note.
3. Update Topics footers to match the new area.
4. Remove migrated notes from the old area index.
5. Add "Related Areas" cross-links in both the old and new area indexes.
6. Add the new area to `kb/notes/areas.md`.

### 5. Check for dual parent-child tagging

```bash
# Find notes tagged with both an area and its sub-area
# Example: notes with both document-system and type-system
rg "areas:.*document-system.*type-system|areas:.*type-system.*document-system" kb/notes/ --glob '*.md'
```

Remove the parent tag. Keep only the most precise area. The parent is reachable via "Related Areas" in the index.

### 6. Check for orphaned notes

```bash
# Notes with no areas tag or empty areas
rg -L "^areas:" kb/notes/*.md
rg "areas: \[\]" kb/notes/ --glob '*.md'
```

For each orphan, assign the most precise area whose index would help a reader find related notes.

### 7. Verify index-tag consistency

For each area, check that notes tagged with that area actually appear in the area index, and vice versa.

```bash
# Notes tagged with area X but not listed in X's index
area="type-system"
rg -l "areas:.*$area" kb/notes/ --glob '*.md' | while read f; do
  fname=$(basename "$f")
  rg -q "$fname" "kb/notes/$area.md" || echo "Tagged but not listed: $fname"
done
```

### 8. Update areas.md

Ensure all areas appear in `kb/notes/areas.md`. All areas listed flat — sub-area relationships expressed in each area's "Related Areas" section only.

## Do NOT

- Don't create areas with fewer than 5 notes — use section grouping in the parent area instead.
- Don't dual-tag parent and child areas on notes.
- Don't optimise splits for taxonomic cleanliness — optimise for comparative reading yield.
- Don't update CLAUDE.md — it routes to WRITING.md which has the conventions.
