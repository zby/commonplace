---
description: Replaces the areas frontmatter field with freeform tags and restructures index pages to have both curated and generated sections, decoupling navigation from comparative reading
type: adr
tags: [kb-design]
status: proposed
---

# 004-Replace areas with tags

**Status:** proposed
**Date:** 2026-03-13

## Context

The `areas:` frontmatter field was designed to serve two operations: **navigation** (finding related notes) and **comparative reading** (loading a bounded set together to detect redundancy, contradiction, and tension). The comparative reading operation imposed constraints on areas — size limits (~40 notes), precision rules ("tag the most precise area"), prohibition on dual-tagging parent and child, and pressure to keep areas flat.

In practice, comparative reading has never been codified into a skill or automated operation. The constraints it justifies actively harm navigation:

- Notes can only belong to a few areas, limiting discoverability.
- "Tag the most precise area" forces artificial choices — a note about constraining during deployment can't tag both `constraining` and `learning-theory` without breaking the parent/child rule.
- Sub-area relationships are awkward — encoded editorially in cross-links rather than expressed naturally through tagging.
- `kb-design` at 44 notes already exceeds the ~40 note threshold, yet splitting it for size alone doesn't improve navigation.

Meanwhile, the curated area index pages (with groupings, context phrases, tensions sections) are genuinely valuable documents. But their value comes from editorial curation, not from being exhaustive listings of area membership.

## Decision

### 1. Rename `areas` to `tags`

The frontmatter field becomes `tags: [constraining, deploy-time, learning-theory]`. Tags are freeform — no limit on how many a note can have (guidance: use as many as genuinely useful for navigation, typically 3-5). No parent/child prohibition — tag whatever helps a reader find the note.

### 2. Index pages have curated and generated sections

Each tag that accumulates enough notes gets an index page. An index page has two parts:

**Curated section** (optional, hand-written): Editorial groupings, context phrases, tensions, related indexes. This is a small, selective "essential reading" list — not every note tagged with the keyword, just the ones that tell the story. Should stay small enough to be editorially manageable.

**Generated section** (automatic, rebuilt by script): Complete listing of all notes carrying that tag. Rebuilt idempotently — everything below a marker is replaced, everything above is preserved.

```markdown
# constraining

Brief orientation prose...

## Notes
### Foundations
- [constraining](./constraining.md) — defines the concept
- [codification](./codification.md) — the far end of constraining
...

### Tensions
...

## Related Indexes
- [learning-theory](./learning-theory-index.md)

## All notes  <!-- generated -->
- [changing-requirements-conflate...](./changing-requirements-conflate....md)
- [codification](./codification.md)
- ...
```

For tags without curation, the page is just the generated section. Adding curation means writing prose above the marker. No sub-type field needed — the presence of curated content is the distinction.

### 3. No size constraint on tags, editorial constraint on curated sections

Tags have no size limit — a tag with 100 notes is fine; the generated section handles it. The curated section should stay small — it's a selective editorial act, not a completeness obligation. The exact limit is left unspecified for now; experience with comparative reading operations will inform it later.

### 4. Remove Topics footer from notes

The `Topics:` footer section at the bottom of each note is removed. It was a markdown-level navigation aid linking to area indexes, but it duplicates information already available in two other places:

- **Frontmatter** `tags:` field — the source of truth, visible to anyone reading the raw markdown.
- **MkDocs hook** — renders clickable tag links in the HTML output.

Removing Topics eliminates `sync_topic_links.py`, the areas-topics consistency check in the validate skill, and a source of staleness. The `001-generate-topic-links-from-frontmatter` ADR is superseded by this decision.

### 5. Index pages use `-index` filename suffix

All tag index pages follow the naming convention `{tag}-index.md` (e.g. `kb-design-index.md`). This distinguishes them from content notes and makes the tag-to-filename mapping mechanical.

### 6. Sub-areas dissolve into the tag graph

A note tagged `[constraining, learning-theory]` is findable from both index pages. The `learning-theory` curated section can group constraining notes and link to the `constraining` index. The relationship is expressed editorially, not enforced by tagging rules. No "Related Areas" convention needed — curated indexes link to whatever other indexes are useful.

## Consequences

### Easier

- **Tagging** — no precision anxiety, no parent/child rules, just tag what's relevant.
- **Navigation** — more entry points to find a note. A note about constraining is findable from `constraining`, `learning-theory`, and `deploy-time`.
- **Index maintenance** — the generated section is always complete and current. Curated sections can lag without hiding notes.
- **Sub-areas** — emerge naturally as tags that accumulate notes and optionally get curated. No explicit hierarchy management.
- **New topics** — a tag exists as soon as a note uses it. The index page can be generated immediately. Curation comes later if the topic warrants it.

### Harder

- **Tag consistency** — freeform tags can diverge (`deploy-time` vs `deploy-time-learning` vs `deployment`). Will need lightweight normalization, possibly a known-tags registry or script.
- **Curated index completeness** — slight redundancy between curated and generated sections. A note appears in both if it's editorially selected. This is acceptable — same pattern as a book with a narrative introduction and a full table of contents.
- **Migration** — every note's `areas:` field needs renaming to `tags:`, Topics footers stripped, index files renamed. Scripts (`mkdocs_hooks.py`), validation, WRITING.md, and CLAUDE.md all reference `areas`.
- **Comparative reading** — when this operation is eventually codified, it will need its own scoping mechanism rather than piggybacking on tags. This is a feature, not a bug — the scoping can be purpose-built rather than constrained by navigation concerns.

---

Relevant Notes:

- [areas exist because useful operations require reading notes together](../areas-exist-because-useful-operations-require-reading-notes-together.md) — the rationale this ADR partially supersedes; orientation and comparative reading operations that justified area constraints
- [stale indexes are worse than no indexes](../stale-indexes-are-worse-than-no-indexes.md) — the generated section eliminates this failure mode for listings
- [001-generate-topic-links-from-frontmatter](../001-generate-topic-links-from-frontmatter.md) — superseded: Topics footers removed entirely rather than migrated to `tags:`
