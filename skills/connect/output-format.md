# Connection Report Format

Save the report to the workshop directory as `connect-report-<note-name>.md`.

```markdown
# Connection Report: [note title]

**Source:** [note-title](kb/notes/note-title.md)
**Date:** YYYY-MM-DD
**Depth:** standard | deep | quick

## Discovery Trace

**Index exploration:**
- Read [index-name](kb/notes/index-name.md) — found candidates: [note A](kb/notes/note-a.md), [note B](kb/notes/note-b.md)
- Followed link from [note A](kb/notes/note-a.md) to [note D](kb/notes/note-d.md)

**Semantic search:** (via MCP | bash fallback | grep-only)
- query "[core concept from note]" — top hits:
  - [note E](kb/notes/note-e.md) (0.74) — strong match, mechanism overlap
  - [note F](kb/notes/note-f.md) (0.61) — weak, only surface vocabulary
  - [note G](kb/notes/note-g.md) (0.58) — skip, different domain

**Keyword search:**
- grep "specific term" — found [note H](kb/notes/note-h.md) (already in index candidates)

## Connections Found

For each accepted connection:

- [target](kb/notes/target.md) — **extends**: [specific reason why this connection exists]
- [another](kb/notes/another.md) — **grounds**: [specific reason]

**Bidirectional candidates** (reverse link also worth adding):
- [target](kb/notes/target.md) ↔ source — **contradicts**: [reason the return path is also useful]

## Rejected Candidates

- [rejected](kb/notes/rejected.md) — surface vocabulary overlap only, no semantic connection
- [another](kb/notes/another.md) — too obvious to be useful

## Index Membership

Which area indexes this note should belong to:
- [index-name](kb/notes/index-name.md) — [what it contributes to this area]
- Already member of: [existing-index](kb/notes/existing-index.md)

## Synthesis Opportunities

[Two or more notes that together imply a higher-order claim not yet captured. Describe what the synthesis would argue and which notes contribute.]

## Flags

- Split candidate: [broad note](kb/notes/broad-note.md) — [why]
- Tension: [X](kb/notes/x.md) vs [Y](kb/notes/y.md) — [what conflicts]
- No connections found — [note this honestly if true]
```
