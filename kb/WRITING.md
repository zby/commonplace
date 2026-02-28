# Writing Guide for kb/

Read this before creating or editing notes, ADRs, indexes, or source reviews. For searching and routing, see the Knowledge System section in the root `CLAUDE.md`.

## Before You Write

**Text files** skip this checklist entirely. A `text` file is a markdown file with no frontmatter — just create the file and write. See [document-classification](notes/document-classification.md) for the type taxonomy and [note base type](../types/note.md) for field definitions, status, and traits.

For **notes and above** (any type with frontmatter), every note must be findable by a future agent who doesn't know it exists. Before saving, check:

1. **[Title as claim](claw-design/title-as-claim-enables-traversal-as-reasoning.md)** — Does it work as prose when linked? `since [title](./title.md)` reads naturally? (Applies to single-claim documents; multi-claim specs and frameworks get topical titles instead.)
2. **Description** — Is it a retrieval filter, not a summary? The test: if an agent searched for this note's main concept and got 5 results, would this description help pick THIS one? Descriptions that paraphrase the title add zero retrieval value.
3. **Index membership** — Is it linked from at least one area index? (Directory indexes are auto-generated.)
4. **Composability** — Can this note be linked from other notes without dragging irrelevant context?

If any answer is "no," fix it before saving.

## Where It Goes

Where a note goes depends on what triggered it:

- **Human request or established pipeline** → main KB (`notes/`, `adr/`, tasks, etc. — see routing table in `CLAUDE.md`)
- **Agent's own observation during work** → `notes/agent-learnings/` (notes only — no tasks or ADRs without human request)

Agent-learnings are periodically reviewed and either promoted to the main KB / CLAUDE.md, or deleted. The quality checklist above applies to both — but agent-learnings can be briefer since they'll be curated later.

## Templates

The two most common types — `note` and `structured-claim` — are inlined below. The base type specification lives in `../types/note.md` and the creation template in `../types/note.template.md`. Directory-local types live in each collection's `types/` subdirectory:

- `notes/types/` — `structured-claim`, `adr`, `index`, `related-system`
- `sources/types/` — `source-review`
- `tasks/types/` — `task-active`, `task-backlog`, `task-recurring`

### note

Freeform exploration, insights, analysis. The default type for any document with frontmatter.

```markdown
---
description: ""
type: note
traits: []
areas: []
status: current
---

# {prose-as-title — a proposition, not a topic label}

{Your analysis, reasoning, or exploration. Freeform.}

## Open Questions

- {Unresolved points worth tracking — omit section if none}

---

Relevant Notes:
- [related-note](./related-note.md) — how it relates

Topics:
- [relevant-area-index](./relevant-area-index.md)
```

### structured-claim

Developed arguments with Evidence/Reasoning/Caveats sections. Use when a note has matured from exploration into a defensible claim.

```markdown
---
description: ""
type: structured-claim
traits: []
areas: []
status: seedling
---

# {Claim as title — an assertion, not a topic label}

{Opening paragraph — claim stated as a full sentence with context. Why does this matter?}

## Evidence

{Observations, facts, references. Checkable.}
{Toulmin: grounds}

## Reasoning

{The principle connecting evidence to claim. Why does this evidence imply this claim?}
{Toulmin: warrant + backing}

## Caveats

- {Scope limits — when does this not apply?}
- {Assumptions that must hold}
- {Counterarguments and responses}

---

Relevant Notes:
- [related-note](./related-note.md) — how it relates

Topics:
- [relevant-area-index](./relevant-area-index.md)
```

## Frontmatter

Frontmatter makes notes queryable via ripgrep. Its presence determines the note's base type:

- **No frontmatter** → `text` — raw capture, no structural expectations
- **Has frontmatter** → `note` or more specific type — full quality checks apply

| Field | Required | Constraints |
|-------|----------|------------|
| `description` | Yes | Max 200 chars, must discriminate this note from similar ones |
| `type` | No | Base type: `note` (default), `structured-claim`, `spec`, `review`, `index`, `adr`. See [document-classification](notes/document-classification.md) |
| `traits` | No | Independently checkable properties: `has-comparison`, `has-external-sources`, `has-implementation` |
| `areas` | No | Array of area index names this note belongs to (not the auto-generated directory index) |
| `status` | No | current, outdated, speculative |

**`description` is the most important field.** It's a retrieval filter, not a summary — it helps agents decide whether to load the full note. A good description answers "why THIS note?" not "what is this note about?"

Task files do not use frontmatter — their status is encoded by directory (backlog/active/completed). Seedlings also lack frontmatter, but are distinguished by location (they live in `notes/`, not `tasks/`).

## Links

Internal workspace documents connect via standard markdown links. Each link is an edge in the knowledge graph. Use relative paths from the source file's directory.

### How Links Work

- `[note title](./note-title.md)` links to a note in the same directory
- `[note title](../note-title.md)` or `[note title](./subdir/note-title.md)` for cross-directory links
- Links work as prose: "Since [thin adapters reduce coupling between providers and runtime](./thin-adapters-reduce-coupling-between-providers-and-runtime.md), we chose..."
- Link text doesn't have to match the target's title — use whatever text best informs the reader's decision

### Inline vs Footer Links

**Inline links** are woven into prose and carry richer relationship data:
> The insight is that [thin adapters reduce coupling](./thin-adapters-reduce-coupling-between-providers-and-runtime.md), which informed the OAuth gating approach.

**Footer links** appear at the bottom in a structured section:
```markdown
---
Relevant Notes:
- [related note](./related-note.md) — extends this by adding the temporal dimension
Topics:
- [architecture-index](./architecture-index.md)
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

### Dangling Link Policy

Every link must point to a real file. Before creating a link, verify the target exists with `ls`. If it should exist but doesn't, create it, then link.

## Indexes

There are two kinds of indexes:

- **Directory indexes** (`index.md` in each collection) — auto-generated flat listings of all files with title, description, and type. Rebuild with `uv run kb/scripts/generate_notes_index.py <directory>`.
- **Area indexes** (e.g. `approvals-index.md`) — curated navigation hubs with editorial context, grouping, and open questions. Updated by /connect or manually.

The rest of this section covers area indexes.

Area indexes organize notes by topic. They reduce context-switching cost. When you switch to a topic, you need to know: what is known, what is in tension, what is unexplored.

### Index Structure

```markdown
# area-name index

Brief orientation — what this area covers.

## Notes
- [note](./note.md) — context explaining why this matters here

## Decisions
- [NNN-decision](../adr/NNN-decision.md) — brief context

## Open Questions
What is unexplored or unresolved.
```

**Critical rule:** Entries MUST have context phrases. A bare link list without explanation is an address book, not a map.

### Lifecycle

**Create** when 5+ related notes accumulate without navigation structure.
**Split** when an index exceeds 40 notes and distinct sub-communities form.
**Merge** when both indexes are small with significant overlap.

## Helper Functions

### Safe Rename
Never rename a note manually — it breaks links. Use:
```bash
# Find and update all references
rg '\[.*\]\(.*old-title\.md\)' --glob '*.md' -l  # find references first
# Then git mv and update all references
```

### Graph Utilities
```bash
# Orphan detection (notes with no inbound links)
rg -l '.' kb/notes/*.md | while read f; do
  fname=$(basename "$f")
  rg -q "$fname" --glob '*.md' kb/notes/ || echo "Orphan: $f"
done

# Dangling link detection (links to non-existent files)
rg -o '\]\(([^)]+\.md)\)' kb/notes/ -r '$1' --no-filename | sort -u | while read target; do
  [ -f "kb/notes/$target" ] || echo "Dangling: $target"
done

# Find text files (no frontmatter)
rg -L '^---' kb/notes/*.md

# Find notes missing descriptions (has frontmatter but no description — broken, not text)
rg -l '^---' kb/notes/*.md | xargs rg -L '^description:'
```

## Common Pitfalls

### Productivity Porn
Building the knowledge system instead of using it for the library. If you're spending more time on methodology than on design notes, recalibrate. The vault serves the library, not the other way around.

### Temporal Staleness
Design notes become outdated as the library evolves. A note about the runtime architecture from two months ago may reference removed features. Update or archive notes that no longer reflect reality.

### Collector's Fallacy
Accumulating design explorations without distilling them into ADRs or actionable decisions. If your notes grow faster than your decisions, stop capturing and start extracting.
