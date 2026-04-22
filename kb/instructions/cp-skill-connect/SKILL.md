---
name: cp-skill-connect
description: Discover connections for a single note. Writes a connect-report under kb/reports/connect/<collection>/ without mutating library notes or indexes. Use with a note path or note name.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
---

# Connect — Discovery Only

Find connections for a single note. Output is a connection report saved to `kb/reports/connect/<collection>/<note-name>.connect.md`. Library notes and indexes are not edited. Connect reports are gitignored; they are immediate downstream context and can be regenerated from the source artifact plus current KB state.

## Input

Target: `$ARGUMENTS` — one note path or note name. If none provided, ask which note to connect. Determine the source **collection** from the note's path (`kb/notes/` → notes, `kb/reference/` → reference, etc.).

## Setup

1. Read the target note fully. Identify its claim, mechanism, implications, scope, and tensions. If the target has no frontmatter (`text` file), continue discovery from its title/body and mark the report as provisional.
2. Read `kb/<source-collection>/COLLECTION.md`. Enumerate the **outbound destination blocks** under "Outbound linking conventions" — one block per destination collection the source may link to. For each block, capture:
   - **Search guidance** — when to prospect this destination from the current source.
   - **Authorised labels** — labels the writer may use for links to this destination, with the reader-need each label serves.

   This is the only linking-rules surface. There is no compiled topology and no separate vocabulary doc to consult.
3. Use repo-local discovery only: generated indexes, tag indexes, `rg`, and link following. Do not call external semantic-search tools or MCP search services; connect must work in Codex without external search state.

## Discovery — per destination

Connect is the skill that pays the cost of active search. The write skill is bounded to dir-index + already-loaded context + user-named targets; connect runs the full prospecting procedure on every destination block declared in the source's `COLLECTION.md`.

Active depth: **standard** (quick: index-only single pass; deep: full discovery, multiple passes, synthesis detection).

Capture discovery trace throughout — indexes read, actual query strings, candidate evaluations, and links followed. A trace with only keywords is insufficient.

For **each** destination block in the source's `COLLECTION.md`:

### 1. Apply the destination's search guidance

The block's search guidance names the trigger for searching this destination from the current source — concrete cues like "when the claim describes behaviour the commonplace system exhibits" or latitude cues like "let the agent filter; prefer slight over-retrieval." Use the guidance to decide breadth: scan liberally when the destination is small or the guidance signals breadth; tighten when the trigger is narrow. If the source has no plausible match for the trigger, note that in the trace and move on without prospecting that destination.

### 2. Prospect using repo-local tools

In order of cost:

- **Destination `dir-index.md`.** Read the destination's full `dir-index.md`; titles + descriptions are the cheapest candidate surface. Collections without a `dir-index.md` (rare) can be scanned with `ls` or by reading the collection's `README.md` for curated entry points.
- **Tag indexes.** When the source carries `tags:`, check the corresponding tag indexes in the destination collection (e.g. `tags: [learning-theory]` → `learning-theory-index.md`). Only curated sections above the `<!-- generated -->` marker add value — they capture editorial groupings the flat index scan misses.
- **`rg` body search.** Run focused queries for terms and adjacent concepts the destination block names or that the source's claim foregrounds. Multiple queries; capture the actual query strings.

  ```bash
  rg -n "term" kb/<destination>/ --glob "*.md"
  ```

- **Link following.** From promising candidates, follow their existing links one hop, then re-filter. Look for clusters and chains the source should join.

### 3. Articulation test

Every candidate must complete *"[source] connects to [target] because [specific reason]."* Reject candidates that are merely "related", keyword-only matches, too obvious to help traversal, or likely to confuse an agent following the link. Ask what an agent gains by following the link.

### 4. Label from the destination's authorised set

Each authorised label carries a reader-need; pick the one whose reader-need matches the connection's purpose. The destination block in `COLLECTION.md` is the authoritative list — do not propose labels outside it.

If a candidate passes the articulation test but **no authorised label fits**, it is either off-scope or a signal that the collection author should extend the authorisation. Move it to **Off-authorisation candidates** in the report (see below). Do not invent a label or downgrade to `see-also` to make it fit.

### Instructions sources: respect the frontloading posture

When the source is in `kb/instructions/`, honour `kb/instructions/COLLECTION.md`'s strict outbound rules. Authorised labels are narrow — `rationale` (→ `kb/notes/`, meta-reader audience) and `operates-on` (→ `kb/reference/`). Do not propose `see-also` sprays or `defined-in` links from instructions; terms an executing agent needs must be frontloaded into the instruction body, not deferred to a link. Annotate proposed `rationale` links as meta-reader edges so the author can decide whether to keep them.

## Reverse-edge candidates

Not every useful link is authored from the source side. For the current target, scan for notes **elsewhere** that should link **to** this target under their own collection's outbound rules.

Concrete case: `kb/agent-memory-systems/` is a frequent *target* for theoretical notes via `evidence` / `derived-from`, but its own outbound to `kb/notes/` is narrow. When connecting a review in agent-memory-systems, look for notes in `kb/notes/` whose claims this review could corroborate; surface those as Reverse-edge candidates. Similar asymmetries exist elsewhere — any time the target is in a collection whose outbound rules don't match the inbound flow it actually receives.

The skill does **not** edit those source notes or write draft links from them. It names the candidate reverse edges so the author of the source note (or a future connect run on the source) can decide whether to author the link.

## Output

Save the report to `kb/reports/connect/<source-collection>/<note-name>.connect.md`. Read `kb/reports/types/connect-report.md` for the report structure. Use file-relative markdown links in the body. Tell the user: `Report saved: <full path>`.

Sections:

- **Discovery Trace** — per-destination: indexes read, queries run, candidates evaluated, why kept or rejected.
- **Connections Found** — typed candidates, one per line, with the authorised label and the specific reason.
- **Bidirectional Candidates** — return links from existing notes that are also worth adding (under those notes' own outbound rules).
- **Reverse-edge candidates** — notes in other collections that should link **to** this target under their own COLLECTION.md rules.
- **Off-authorisation candidates** — candidates that passed the articulation test but have no authorised label for the source→destination pair. Suggests either extending the destination's authorised set or rejecting as off-scope. Not draft links.
- **Raw Text Candidates** — targets without frontmatter.
- **Rejected Candidates** — notable non-matches, with the reason.
- **Index Membership** — indexes the source might join.
- **Synthesis Opportunities** — higher-order claims implied by multiple notes (do not create the synthesis note here).
- **Flags** — split candidates, tensions, no-connections findings, follow-up work.

Write `None` for empty sections.

**Quality gates**: verify every candidate path exists. Flag load-bearing relationships (`grounds`, `mechanism`, `derived-from`) to `seedling` or `speculative` notes.

## Constraints

**Never** edit the target note, other notes, or indexes. **Never** add "related" connections without specific reasoning. **Never** force connections — if no genuine connections exist, say so honestly. **Never** propose a label outside the destination's authorised set; route those to Off-authorisation candidates.

**Always** capture discovery trace per destination. **Always** verify candidate paths exist before including them. **Always** read the source `COLLECTION.md` before prospecting — it is the only authoritative linking-rules surface.

## Reflection

If you noticed anything worth flagging during traversal — errors in notes, stale links, clear contradictions — append to `kb/log.md`. Format: `- path/to/note.md: what needs fixing`

Abstraction opportunities (multiple notes sharing an unnamed mechanism) are worth logging only when the pattern is strong and specific. Skip reflection entirely if nothing stood out.
