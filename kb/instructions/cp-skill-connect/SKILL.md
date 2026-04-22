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

Find candidate connections for a single note and write them to a **discovery report** at `kb/reports/connect/<collection>/<note-name>.connect.md`. The skill never edits the source or any other library artifact — every section of the report describes *candidate* edges for a future writer (a human, a downstream skill, the ingest flow) to act on, not edges already encoded anywhere. This is by design: it lets connect run safely on immutable artifacts (snapshots) and on artifacts whose authoring surface is elsewhere (e.g. a snapshot's `.ingest.md`).

Connect reports are gitignored; they are immediate downstream context and can be regenerated from the source artifact plus current KB state.

## Input

Target: `$ARGUMENTS` — one note path or note name. If none provided, ask which note to connect. Determine the source **collection** from the note's path (`kb/notes/` → notes, `kb/reference/` → reference, etc.).

## Setup

1. Determine the source collection from the target note's path (`kb/notes/...` → `notes`, `kb/reports/foo.md` → `reports`, etc.). **Hard fail immediately if `kb/<source-collection>/COLLECTION.md` does not exist** — do not attempt discovery, do not fall back to defaults, do not soldier on. Report the missing file path to the user and stop. The COLLECTION.md is the only linking-rules surface; without it the skill has no authorised destinations or labels and any output would be invented.
2. Read the target note fully. Identify its claim, mechanism, implications, scope, and tensions. If the target has no frontmatter (`text` file), continue discovery from its title/body and mark the report as provisional.
3. Read `kb/<source-collection>/COLLECTION.md` and find its **outbound-linking section** (heading varies — look for the one that names destinations and labels). Read it as authoritative guidance — extract three things, regardless of whether the section is structured as per-destination blocks, a single labels table with a destinations column, prose, or any mix:
   - **Which destination collections to prospect from this source** (and which are excluded).
   - **Which labels are authorised for which source→destination pairs**, with the reader-need each label serves.
   - **Any direction or composition hints** — inverse-edge expectations, rare/common edges, frontloading posture, sub-agent invocation preferences. The skill below leans on these for reverse-edge candidates and for tightening prospecting on rare edges.

   This is the only linking-rules surface. There is no compiled topology and no separate vocabulary doc to consult.
4. Use repo-local discovery only: generated indexes, tag indexes, `rg`, and link following. Do not call external semantic-search tools or MCP search services; connect must work in Codex without external search state.

## Discovery — per destination

Connect is the skill that pays the cost of active search. The write skill is bounded to dir-index + already-loaded context + user-named targets; connect runs the full prospecting procedure on every destination the source's `COLLECTION.md` permits.

Active depth: **standard** (quick: index-only single pass; deep: full discovery, multiple passes, synthesis detection).

Capture discovery trace throughout — indexes read, actual query strings, candidate evaluations, and links followed. A trace with only keywords is insufficient.

For **each** destination collection authorised by the source's outbound section:

### 1. Decide breadth from the source COLLECTION.md's guidance

The outbound section says (or implies) when to prospect each destination — concrete cues like "when the claim describes behaviour the commonplace system exhibits", latitude cues like "let the agent filter; prefer slight over-retrieval", or composition hints like "the usual direction is inverse." Use the guidance to set breadth: scan liberally when the destination is small or the guidance signals breadth; tighten when the trigger is narrow or the edge is flagged as uncommon. If the source has no plausible match for the trigger, note that in the trace and move on without prospecting that destination.

### 2. Prospect using repo-local tools

In order of cost:

- **Destination `dir-index.md`.** Read the destination's full `dir-index.md`; titles + descriptions are the cheapest candidate surface. Collections without a `dir-index.md` (rare) can be scanned with `ls` or by reading the collection's `README.md` for curated entry points.
- **Tag indexes.** When the source carries `tags:`, check the corresponding tag indexes in the destination collection (e.g. `tags: [learning-theory]` → `learning-theory-index.md`). Only curated sections above the `<!-- generated -->` marker add value — they capture editorial groupings the flat index scan misses.
- **`rg` body search.** Run focused queries for terms and adjacent concepts the source's claim foregrounds and the destination's outbound guidance suggests. Multiple queries; capture the actual query strings.

  ```bash
  rg -n "term" kb/<destination>/ --glob "*.md"
  ```

- **Link following.** From promising candidates, follow their existing links one hop, then re-filter. Look for clusters and chains the source should join.

### 3. Articulation test

Every candidate must complete *"[source] connects to [target] because [specific reason]."* Reject candidates that are merely "related", keyword-only matches, too obvious to help traversal, or likely to confuse an agent following the link. Ask what an agent gains by following the link.

### 4. Label the candidate from the destination's authorised set

Each authorised label carries a reader-need; pick the one whose reader-need matches the candidate connection's purpose, and record both label and a one-line context phrase in the report. The labels the source's outbound section authorises **for this specific destination** are the only options — do not propose labels outside that set. (Labels often appear in a single table with a destinations column; filter to rows whose destinations include the current target collection.)

If a candidate passes the articulation test but **no authorised label fits**, it is either off-scope or a signal that the collection author should extend the authorisation. Move it to **Off-authorisation Candidates** in the report (see below). Do not invent a label or downgrade to `see-also` to make it fit.

The label and context phrase are recorded *in the report* — connect does not write them anywhere else.

### Honour collection-specific posture

Some `COLLECTION.md` files declare global postures that constrain prospecting beyond the per-label rules. Examples to respect when present:

- **Frontloading** (e.g. `kb/instructions/COLLECTION.md`) — outbound is exceptional. Don't propose `see-also` sprays from instructions; terms an executing agent needs must be frontloaded, not linked. Annotate proposed `rationale` links as meta-reader edges.
- **Excluded destinations** — a collection may explicitly say "do not link into X" (commonly `kb/work/`). Don't surface candidates from excluded destinations even if they pass the articulation test.

Read these from the outbound section before prospecting, not after.

## Reverse-edge candidates

Not every useful link is authored from the source side. For the current target, scan for notes **elsewhere** that should link **to** this target under their own collection's outbound rules.

The source COLLECTION.md often flags this directly — language like "the usual direction is inverse" or "primary edge is `instruction → note` via `rationale`" tells you to look for reverse edges from the named direction. When such a hint is present, treat reverse-edge prospecting as a first-class pass for that destination, not an afterthought.

Concrete case: `kb/agent-memory-systems/` is a frequent *target* for theoretical notes via `evidence` / `derived-from`, but its own outbound to `kb/notes/` is narrow. When connecting a review in agent-memory-systems, look for notes in `kb/notes/` whose claims this review could corroborate; surface those as Reverse-edge candidates.

The skill does **not** edit those source notes or write draft links from them. It names the candidate reverse edges so the author of the source note (or a future connect run on the source) can decide whether to author the link.

## Output

Save the report to `kb/reports/connect/<source-collection>/<note-name>.connect.md`. Read `kb/reports/types/connect-report.md` for the report structure. Use file-relative markdown links in the body. Tell the user: `Report saved: <full path>`.

Every section below describes **candidate** signal for a future writer to act on. The connect skill does not author any of these edges into any note — the report is the entire deliverable.

- **Discovery Trace** — per-destination: indexes read, queries run, candidates evaluated, why kept or rejected.
- **Connections Found** — candidate outbound edges from the source. For an authored source (e.g. an `.ingest.md`, a note, an ADR) these are the recommended links a future edit should add. For an immutable source (e.g. a snapshot under `kb/sources/`) they are recommended links for whichever artifact carries the source's authored surface (typically the matching `.ingest.md`).
- **Bidirectional Candidates** — when a Connections Found edge is worth following in both directions, surface the return link here so the target-side author sees the suggestion.
- **Reverse-edge Candidates** — notes elsewhere that should link **to** this source under their own COLLECTION.md rules. Especially load-bearing when the source is an immutable artifact whose inbound flow is asymmetric (snapshots in `kb/sources/`, reviews in `kb/agent-memory-systems/`).
- **Off-authorisation Candidates** — candidates that passed the articulation test but have no authorised label for the source→destination pair. Suggests either extending the destination's authorised set or rejecting as off-scope. Not draft links.
- **Raw Text Candidates** — candidate targets without frontmatter.
- **Rejected Candidates** — notable non-matches, with the reason.
- **Index Membership** — indexes the source might join (a future writer would add the entry, not this skill).
- **Synthesis Opportunities** — higher-order claims implied by multiple notes (do not create the synthesis note here).
- **Flags** — split candidates, tensions, no-connections findings, follow-up work.

Write `None` for empty sections.

**Quality gates**: verify every candidate path exists. Flag load-bearing relationships (`grounds`, `mechanism`, `derived-from`) to `seedling` or `speculative` notes.

## Constraints

**Never** edit the target note, other notes, indexes, or any library artifact — the report is the *only* output the skill produces. Every section is a candidate signal for future authoring, not committed state.

**Never** add "related" connections without specific reasoning. **Never** force connections — if no genuine connections exist, say so honestly. **Never** propose a label outside the destination's authorised set; route those to Off-authorisation Candidates.

**Always** capture discovery trace per destination. **Always** verify candidate paths exist before including them. **Always** read the source `COLLECTION.md`'s outbound-linking section before prospecting — it is the only authoritative linking-rules surface, regardless of how that section is internally structured.

## Reflection

If you noticed anything worth flagging during traversal — errors in notes, stale links, clear contradictions — append to `kb/log.md`. Format: `- path/to/note.md: what needs fixing`

Abstraction opportunities (multiple notes sharing an unnamed mechanism) are worth logging only when the pattern is strong and specific. Skip reflection entirely if nothing stood out.
