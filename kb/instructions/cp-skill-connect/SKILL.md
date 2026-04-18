---
name: cp-skill-connect
description: Discover connections for a single note. Writes a connect-report under kb/reports/connect/<collection>/ without mutating library notes or indexes. Use with a note path or note name.
type: instruction
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
---

# Connect — Discovery Only

Find connections for a single note. Output is a connection report saved to `kb/reports/connect/<collection>/<note-name>.connect.md`. Library notes and indexes are not edited.

## Input

Target: `$ARGUMENTS` — one note path or note name. If none provided, ask which note to connect. Determine the source **collection** from the note's path (`kb/notes/` → notes, `kb/reference/` → reference, etc.).

## Setup

1. Read the target note fully. Identify its claim, mechanism, implications, scope, and tensions. If the target has no frontmatter (`text` file), continue discovery from its title/body and mark the report as provisional.
2. Read `kb/reports/collection-topology.md` — the linking matrix tells you which relationship types are appropriate when source and target are in different collections.
3. Sync the search index if qmd is available:

```bash
command -v qmd && qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed
```

If qmd is not found, log "qmd unavailable — grep-only fallback" and skip. Do not attempt to install it.

## Discovery

Active depth: **standard** (quick: index-only single pass; deep: full discovery, multiple passes, synthesis detection).

Capture discovery trace throughout — actual query strings, scores, candidate evaluations. A trace with only keywords is insufficient.

### 1. Index scan (primary discovery)

Read `dir-index.md` in the source collection first, then in other collections that have one. Each lists every note with its description — a complete, cheap candidate scan. Scan every entry; don't filter by vocabulary overlap — cross-domain connections often share no terminology. Flag candidates with a reason. Collections without a `dir-index.md` (like `kb/instructions/`) can be scanned with `ls` or by reading the collection's `README.md` for curated entry points.

### 2. Tag indexes

If the source note has `tags:` in its frontmatter, check the corresponding tag indexes (e.g. `tags: [learning-theory]` → `learning-theory-index.md`). Only curated sections above the `<!-- generated -->` marker add value — they provide editorial groupings and tensions that the flat index scan misses. Skip fully auto-generated indexes.

### 3. Semantic search

Reaches inside note bodies for connections buried in sections, examples, or open questions that descriptions don't capture.

If qmd was available:
```bash
qmd --index "$COMMONPLACE_QMD_INDEX" query "[core concepts]" --collection <collection> -n 15
```
Run against the source collection and others. Record query strings and top results with scores.

If qmd unavailable, rely on index + keyword search only.

### 4. Keyword search

```bash
rg "term" kb/ --glob "*.md"
```

For exact terms and specific phrases. Searches across all collections.

### 5. Link following

From promising candidates, follow their existing links. Look for clusters and chains the source should join.

## Evaluate and save

**Articulation test**: every connection must complete "[A] connects to [B] because [specific reason]." Reject candidates that are merely "related", keyword-only matches, too obvious to help traversal, or likely to confuse an agent following the link. Ask what an agent gains by following the link.

**Relationship labels** — use only when the reason is explicit: `extends` (adds a dimension), `grounds` (provides foundation), `contradicts` (creates tension), `exemplifies` (concrete instance), `synthesizes` (combines insights), `enables` (makes actionable). Use the linking matrix to pick labels appropriate for the source→target collection pair.

**Report sections**: `Connections Found` for typed notes, `Bidirectional Candidates` for return links also worth adding, `Raw Text Candidates` for targets without frontmatter, `Rejected Candidates` for notable non-matches, `Index Membership` for indexes the source might join, `Synthesis Opportunities` for higher-order claims implied by multiple notes, `Flags` for split candidates or tensions. Write `None` for empty sections.

**Quality gates**: verify every candidate path exists. Flag load-bearing relationships (`grounds`, `synthesizes`) to `seedling` or `speculative` notes.

Read `kb/reports/types/connect-report.template.md` for the report structure. Ensure `kb/reports/connect/<collection>/` exists, then save the report. Use file-relative markdown links in the body. Tell the user: `Report saved: <full path>`.

## Constraints

**Never** edit the target note, other notes, or indexes. **Never** add "related" connections without specific reasoning. **Never** force connections — if no genuine connections exist, say so honestly.

**Always** capture discovery trace. **Always** verify candidate paths exist before including them.

## Reflection

If you noticed anything worth flagging during traversal — errors in notes, stale links, clear contradictions — append to `kb/log.md`. Format: `- path/to/note.md: what needs fixing`

Abstraction opportunities (multiple notes sharing an unnamed mechanism) are worth logging only when the pattern is strong and specific. Skip reflection entirely if nothing stood out.
