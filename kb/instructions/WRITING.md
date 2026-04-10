# Writing Guide for kb/

Read this when you write or edit a note: any document in this knowledge base that has frontmatter. This file defines the general writing conventions, quality checks, and default `note` template for those documents. Text documents without frontmatter are exempt from these rules.

## Before You Write

For any note in this sense, make sure it will be findable by a future agent who doesn't already know it exists. Before saving, check:

1. **Title**
   - **Title as claim is a useful convention** — When a title is a claim rather than a topic, links to it can read like reasoning: `since [title](./title.md)` or `because [title](./title.md)`. This makes the file tree scannable as arguments rather than topics, and it improves progressive disclosure because the title tells the reader or agent what the note argues before opening it. Ask whether the title states something that could be true or false. Topic labels, category names, and bare artifact names fail this test. If you use a claim title, add the `title-as-claim` trait so review gates can check that the title actually fulfills that promise. This is a useful convention, not a mandatory rule: don't force a claim title when it feels strained. Common exceptions are multi-claim specs and frameworks, definitional notes, indexes, and exploratory/seedling notes that are not ready to assert a clear claim.
   - **If you use a claim title, check composability** — It should work as prose when linked: `since [title](./title.md)` or `because [title](./title.md)` should read naturally. If it forces awkward grammar and is not a concrete artifact name, it is not composable enough.
   - **If you use a claim title, check claim strength** — Make it a contestable one. "Continuous learning is substrate-independent" passes the prose test but fails the contestability test: nobody would push back on it. "Continuous learning can happen outside of weights" names the thing people actually doubt. If the non-obvious claim is not clear yet, or the document is acting as a reference rather than a premise, use a topical title instead.
   - **Title-body alignment** — Read the title, then the body. The body should actually support the title's claim or scope. Watch for claim drift (title says X, body establishes related claim Y) and scope drift (title is narrower or broader than the body).
   - **Length** — Keep note titles at or below 100 characters.
2. **Description** — Is it a retrieval filter, not a summary? The test: if an agent searched for this note's main concept and got 5 results, would this description help pick THIS one? Descriptions that paraphrase the title add zero retrieval value. Keep it under 200 characters; around 50-200 is the intended range.
3. **Tags** — Is it tagged with relevant keywords that help future readers find it? Use as many as genuinely useful.
4. **Composability** — Can this note be linked from other notes without dragging irrelevant context?
5. **KB vocabulary on first mention** — Terms like distillation, constraining, codification, and context engineering have definitions in `kb/notes/definitions/`. Authors know them from CLAUDE.md, but external readers (humans on GitHub Pages) do not. On first mention, provide an inline gloss and a link: `[distillation](./definitions/distillation.md) (directed context compression)`. The gloss lets the reader keep reading; the link lets them go deep.
6. **[Explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md)** — Aim for notes to explain *why*, not just record *what works*. A note with reach captures mechanism rather than a successful pattern, so it transfers beyond the original case and helps the reader predict where the conclusion will change or fail when the assumptions change. Quick tests: if you changed one premise, could you predict what changes in the conclusion? Would the insight still apply in a different domain, or is it tightly fitted to one case? Could someone say exactly how the explanation is wrong, not just that it is incomplete? Notes that only record "X works" are adaptive — useful but brittle. Notes that explain why X works have reach. Reach is a goal to move toward, not a gate that every note must already clear.

If any answer is "no," fix it before saving.

## Templates

This file only inlines the generic `note` template. If the current collection defines specialized types under its local `types/` directory, read both `{type}.template.md` and `{type}.instructions.md` for the type you are using, along with this guide.

### note

Use this as the default template for any note with frontmatter.

```markdown
---
description: ""
type: note
traits: []
tags: []
status: current
---

# {Title}

{Body}

## Open Questions

- {Question}

---

Relevant Notes:

- [related-note](./related-note.md) — {relationship}
```

## Frontmatter

Frontmatter makes notes queryable via ripgrep. Its presence determines the note's base type:

- **No frontmatter** → `text` — raw capture, no structural expectations
- **Has frontmatter** → `note` or more specific type — full quality checks apply

| Field | Required | Constraints |
|-------|----------|------------|
| `description` | Yes | Must discriminate this note from similar ones |
| `type` | No | Base type: `note` (default) or another specialized document type. See [document-classification](../notes/document-classification.md) |
| `traits` | No | Review-routing properties: `title-as-claim`, `definition`, `has-comparison`, `has-external-sources`, `has-implementation` |
| `tags` | No | Freeform tags for navigation |
| `status` | No | `seedling`, `current`, `speculative`, `outdated`; some specialized types override this vocabulary |

**`description` is the most important field.** It's a retrieval filter, not a summary — it helps agents decide whether to load the full note. A good description answers "why THIS note?" not "what is this note about?"

Tags are freeform navigation aids. Use as many as genuinely useful for helping future readers find the note. There is no parent/child restriction — a note can be tagged both `constraining` and `learning-theory` if both help navigation.

## Links

Internal workspace documents connect via standard markdown links. Each link is an edge in the knowledge graph. Use relative paths from the source file's directory.

### How Links Work

- `[note title](./note-title.md)` links to a note in the same directory
- `[note title](../note-title.md)` or `[note title](./subdir/note-title.md)` for cross-directory links
- Links work as prose: "Since [structure enables navigation without reading everything](./structure-enables-navigation-without-reading-everything.md), we chose..."
- Link text doesn't have to match the target's title — use whatever text best informs the reader's decision

## Filenames

Use lowercase, hyphens for spaces, and the `.md` extension. Derive the filename from the `# Title` heading unless there is a strong reason to preserve an established filename.

Filename slugs are capped at 100 characters. If a title would produce a longer slug, shorten the title rather than relying on truncation.

### Inline vs Footer Links

**Inline links** are woven into prose and carry richer relationship data:
> The insight is that [structure enables navigation without reading everything](./structure-enables-navigation-without-reading-everything.md), which informed the index design.

**Footer links** appear at the bottom in a structured section:
```markdown
---
Relevant Notes:

- [related note](./related-note.md) — extends this by adding the temporal dimension
```

Prefer inline links — they carry more information. Footer links are for connections that don't fit naturally into prose.

### Link Semantics

Every connection must articulate the relationship:
- **extends** — builds on an idea by adding a new dimension
- **foundation** — provides the evidence or reasoning this depends on
- **contradicts** — conflicts with this claim
- **enables** — makes this possible or practical
- **example** — illustrates this concept in practice

Bad: `[note](./note.md) — related`
Good: `[note](./note.md) — extends this by adding the runtime perspective`

### Target Maturity

The relationship type determines how much the linking note depends on the target's stability. **Foundation/grounds** links are load-bearing — if the target changes, the linking note's argument weakens. **Extends/exemplifies** links are additive — the linking note stands on its own regardless.

When using foundation/grounds relationships to `status: seedling` or `status: speculative` notes, acknowledge the instability: either use a weaker relationship that doesn't create a dependency, or note the provisional nature in the link text (e.g., "grounds (provisional — target is speculative)").

### Dangling Link Policy

Every link must point to a real file. Before creating a link, verify the target exists with `ls`. If it should exist but doesn't, create it, then link.

### Distillation Tracking

When you distill content from notes into a focused artifact (instruction, skill body, WRITING.md section), add a "Distilled into:" entry in each source note's footer:

```markdown
Distilled into:

- [WRITING.md](../instructions/WRITING.md) — the area assignment checklist
```

A distillation typically draws from multiple source notes. Each source gets its own "Distilled into:" link so that when any source changes, the maintainer sees the downstream artifact that may need review.

The distilled artifact itself should NOT link back to its sources — it's optimized for the executing agent, not the maintainer.

## Indexes

There are two kinds of indexes:

- **Directory indexes** (`index.md` in each collection) — auto-generated flat listings of all files with title, description, and type. Rebuild with `commonplace-generate-notes-index <directory>`.
- **Tag indexes** (e.g. `learning-theory-index.md`) — navigation hubs for a tag, with optional curated section and auto-generated listing.

### Tag Index Structure

Each tag index has two sections:

**Curated section** (optional, hand-written): Editorial groupings with context phrases, tensions, related indexes. A selective "essential reading" list — not every tagged note, just the ones that tell the story. Should stay small.

**Generated section** (automatic): Complete listing of all notes carrying that tag. Rebuilt by `commonplace-sync-generated-index`. Everything below the `<!-- generated -->` marker is replaced on each run.

```markdown
# tag-name

Brief orientation — what this tag covers.

## Notes
- [note](./note.md) — context explaining why this matters here

## Open Questions
What is unexplored or unresolved.

## All notes <!-- generated -->
- [note-a](./note-a.md) — description
- [note-b](./note-b.md) — description
```

**Critical rule:** Curated entries MUST have context phrases. A bare link list without explanation is an address book, not a map.

### Lifecycle

**Create** when 5+ related notes accumulate under a tag without navigation structure.
**Curate** when the generated listing alone isn't enough — add editorial groupings above the marker.
**Merge** when both indexes are small with significant overlap.

## Useful Commands

### Safe Rename
Never rename a note manually — it breaks links. Use `commonplace-relocate-note`, which renames or moves the note and updates backlinks across the KB.

```bash
commonplace-relocate-note old-note "New note title" --apply
commonplace-relocate-note old-note --to kb/notes/definitions --apply
commonplace-relocate-note old-note --to kb/notes/new-path.md --apply
```

## Common Pitfalls

### Productivity Porn
Building the knowledge system instead of using it for the library. If you're spending more time on methodology than on design notes, recalibrate. The vault serves the library, not the other way around.

### Temporal Staleness
Design notes become outdated as the library evolves. A note about the runtime architecture from two months ago may reference removed features. Update or archive notes that no longer reflect reality.

### Collector's Fallacy
Accumulating design explorations without distilling them into ADRs or actionable decisions. If your notes grow faster than your decisions, stop capturing and start extracting.
