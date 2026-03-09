---
name: connect
description: Discover connections for a single note. Saves a connection report to the active workshop — no file mutations. Triggers on "/connect [note]".
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
---

## Link Format

All links in the connection report use **standard markdown links** with relative paths from `kb/`:

```markdown
[note-title](kb/notes/note-title.md)
```

Filenames use hyphens, not spaces (e.g., `my-note-title.md`).

**Active depth: standard**

| Depth | Discovery Behavior |
|-------|-------------------|
| deep | Full discovery (all steps). Evaluate every candidate. Multiple passes. Synthesis opportunity detection. |
| standard | Full discovery with top 5-10 candidates. Standard evaluation. |
| quick | Single pass — index scan only. Accept obvious connections only. Skip synthesis detection. |

## EXECUTE NOW

**Target: $ARGUMENTS** (exactly one note path or name — if empty, ask which note)

**Step 0: Set up workshop.** Ensure the workshop directory exists:

```bash
mkdir -p kb/work/connect/
```

**Execute these steps:**

1. Read the target note fully — understand its claim and context
2. **Check note type.** If the target has no frontmatter (a `text` file), run `/convert` on it first to add frontmatter with `status: seedling`.
3. **Throughout discovery:** Capture actual query strings, scores, and which candidates you evaluated or rejected. This becomes the Discovery Trace.
4. Run Phase 0 (sync search index)
5. Run discovery: index scan → topic indexes → semantic search → keyword search → link following
6. Evaluate each candidate: does a genuine connection exist? Can you articulate WHY?
7. Save connection report to workshop directory

**START NOW.** Reference below explains methodology.

---

# Connect — Discovery Only

Find connections for a single note. Output is a connection report saved to the active workshop. No files are edited.

The connection report is an artifact that can be reviewed, debugged, and used as input to directed reading for actual file mutations.

Every connection must pass the articulation test: can you say WHY these notes connect? "Related" is not a relationship. When uncertain, do not include the connection.

## Search Scope

Discovery scans two collections under `kb/`:

| Directory | Contains |
|-----------|----------|
| `kb/notes/` | Main KB — claims, design notes, research |
| `kb/sources/` | Snapshotted external sources |

---

# ═══ PHASE 0: SYNC SEARCH INDEX ═══

**Prerequisite check:** Before running qmd, verify it exists:
```bash
command -v qmd
```
If qmd is not found, log "qmd unavailable — skipping index sync, using grep-only fallback for semantic search" and skip directly to Phase 1. **Never attempt to install qmd or any other software.**

If qmd is available:
```bash
qmd --index commonplace update && qmd --index commonplace embed
```

---

# ═══ PHASE 1: UNDERSTAND THE NOTE ═══

1. Read the full note, not just title and description
2. Identify the core claim and supporting reasoning
3. Note key concepts, mechanisms, implications
4. Ask: what questions does this answer? What questions does it raise?

**What you are looking for:**
- The central argument (what is being claimed?)
- The mechanism (why/how does this work?)
- The implications (what follows from this?)
- The scope (when does this apply? When not?)
- The tensions (what might contradict this?)

---

# ═══ PHASE 2: DISCOVERY ═══

**Capture discovery trace as you go.** Record actual query strings, scores, and which candidates you evaluated or rejected. A trace that only lists keywords without query strings or scores is insufficient.

## Step 1: Read the Directory Index (required first step)

Read `kb/notes/index.md` before any other discovery. It lists every note with its description — a complete, cheap candidate scan that catches cross-domain connections that vocabulary-based search misses.

Scan every entry. For each, ask: does this note's description suggest a genuine connection to the source? Flag candidates with a reason. Don't filter by vocabulary overlap — a note about "legal drafting" connects to a paper about "behavioral contracts" even though they share no domain terminology, because both address specification and enforcement.

This step is the primary discovery mechanism. It costs one file read and surfaces connections that semantic search would miss due to vocabulary mismatch.

## Step 2: Topic Index Exploration (if relevant)

If the source connects to a known area (check candidates from Step 1), read the relevant topic index(es). Topic indexes add curated structure that index.md lacks — groupings, tensions, gaps — which can reveal connections the flat listing misses.

## Step 3: Semantic Search

The index scan sees descriptions only. Semantic search reaches inside note bodies — finding connections buried in sections, examples, or open questions that descriptions don't capture.

**Tier 1 — qmd (primary):** Only if qmd was available in Phase 0.
```bash
qmd --index commonplace query "[note's core concepts]" --collection notes -n 15
qmd --index commonplace query "[note's core concepts]" --collection sources -n 10
```

Record the actual query string and top results with scores in the discovery trace.

**Tier 2 — grep only:** If qmd was unavailable or errors, log "qmd unavailable" and rely on index + keyword search only. **Never attempt to install qmd.**

## Step 4: Keyword Search

For specific terms and exact matches — search notes and sources:
```bash
rg "term" kb/notes/ kb/sources/ --glob "*.md"
```

Use rg when:
- You know the exact words that should appear
- Searching for specific terminology or phrases
- Finding all uses of a named concept

## Step 5: Link Following

From promising candidates, follow their existing links:
- What do THEY connect to?
- Are there clusters of related notes?
- Do chains emerge that your source note should join?

This is graph traversal. You are exploring the neighborhood.

---

# ═══ PHASE 3: EVALUATE CONNECTIONS ═══

For each candidate connection, apply the articulation test.

## The Articulation Test

Complete this sentence:
> [note A](./note-a.md) connects to [note B](./note-b.md) because [specific reason]

If you cannot fill in [specific reason] with something substantive, the connection fails.

## Valid Relationship Types

| Relationship | Signal | Example |
|-------------|--------|---------|
| extends | adds dimension | "extends [X](./x.md) by adding temporal aspect" |
| grounds | provides foundation | "this works because [Y](./y.md) establishes..." |
| contradicts | creates tension | "conflicts with [Z](./z.md) because..." |
| exemplifies | concrete instance | "demonstrates [W](./w.md) in practice" |
| synthesizes | combines insights | "emerges from combining [A](./a.md) and [B](./b.md)" |
| enables | unlocks possibility | "makes [C](./c.md) actionable by providing..." |

## Target Maturity Check

For each proposed connection, check the target note's `status` field. Flag load-bearing relationships (**grounds**, **foundation**, **synthesizes**) to `seedling` or `speculative` notes — the dependency is unstable. Note the flag in the connection report:

```
- [note](kb/notes/note.md) — **grounds** ⚠️ target is seedling: [reason]
```

Additive relationships (**extends**, **exemplifies**, **enables**) to seedling/speculative notes are fine — the source note doesn't depend on the target's stability.

## Reject If

- The connection is "related" without specifics
- You found it through keyword matching alone with no semantic depth
- Linking would confuse more than clarify
- The relationship is too obvious to be useful

## Agent Traversal Check

Ask: **"If an agent follows this link, what do they gain?"**

| Agent Benefit | Keep Link |
|---------------|-----------|
| Provides reasoning foundation (why something works) | YES |
| Offers implementation pattern (how to do it) | YES |
| Surfaces tension to consider (trade-off awareness) | YES |
| Gives concrete example (grounds abstraction) | YES |
| Just "related topic" with no decision value | NO |

## Synthesis Opportunity Detection

While evaluating connections, watch for synthesis opportunities — two or more notes that together imply a higher-order claim not yet captured.

Signs of a synthesis opportunity:
- Two notes make complementary arguments that combine into something neither says alone
- A pattern appears across three or more notes that has not been named
- A tension between two notes suggests a resolution claim

When you detect a synthesis opportunity:
1. Note it in the output report
2. Do NOT create the synthesis note during connect — flag it for future work
3. Describe what the synthesis would argue and which notes contribute

---

# ═══ PHASE 4: SAVE CONNECTION REPORT ═══

Write the report to the workshop directory. Derive the filename from the target note:

```
<workshop>/connect-report-<note-name>.md
```

For example: `kb/work/connect/connect-report-frontloading-spares-execution-context.md`

After saving, tell the user: `Report saved: <full path>`

## Report Template

```markdown
# Connection Report: [note title]

**Source:** [note-title](kb/notes/note-title.md)
**Date:** YYYY-MM-DD
**Depth:** standard | deep | quick

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — flagged candidates: [note A](kb/notes/note-a.md), [note B](kb/notes/note-b.md)

**Topic indexes:**
- Read [index-name](kb/notes/index-name.md) — additional candidates: [note C](kb/notes/note-c.md)

**Semantic search:** (via qmd | grep-only fallback)
- query "[core concept from note]" — top hits:
  - [note E](kb/notes/note-e.md) (0.74) — strong match, mechanism overlap
  - [note F](kb/notes/note-f.md) (0.61) — weak, only surface vocabulary
  - [note G](kb/notes/note-g.md) (0.58) — skip, different domain

**Keyword search:**
- grep "specific term" — found [note H](kb/notes/note-h.md) (already in index candidates)

## Connections Found

- [target](kb/notes/target.md) — **extends**: [specific reason why this connection exists]
- [another](kb/notes/another.md) — **grounds**: [specific reason]

**Bidirectional candidates** (reverse link also worth adding):
- [target](kb/notes/target.md) ↔ source — **contradicts**: [reason the return path is also useful]

## Rejected Candidates

- [rejected](kb/notes/rejected.md) — surface vocabulary overlap only, no semantic connection
- [another](kb/notes/another.md) — too obvious to be useful

## Index Membership

- [index-name](kb/notes/index-name.md) — [what it contributes to this area]
- Already member of: [existing-index](kb/notes/existing-index.md)

## Synthesis Opportunities

[Two or more notes that together imply a higher-order claim not yet captured.]

## Flags

- Split candidate: [broad note](kb/notes/broad-note.md) — [why]
- Tension: [X](kb/notes/x.md) vs [Y](kb/notes/y.md) — [what conflicts]
- No connections found — [note this honestly if true]
```

---

# ═══ QUALITY GATES ═══

Before saving the report, verify:

**Gate 1: Articulation Test** — For every connection, can you complete: "[A] connects to [B] because [specific reason]"? If any connection fails, remove it.

**Gate 2: Candidate Verification** — Verify every candidate note path actually exists. Never include connections to non-existent files.

**Gate 3: No Forced Connections** — If nothing genuine was found, say so. An honest "no connections found" report is better than weak connections.

## Edge Cases

**No connections found:** Report honestly. Note which indexes were checked, which searches returned nothing relevant, whether the note might belong to an area index even without direct note-to-note connections.

**Too many connections (split detection):** If a note connects to 5+ notes across 3+ distinct topic areas and makes more than one independent assertion, flag as a split candidate. Do not act — flag in report.

**Conflicting notes:** Flag the tension, note which index Tensions section it belongs in. Do not resolve — flag for judgment.

**Orphan discovery:** If you encounter unconnected notes during search, flag them. Do not attempt to connect them — that's a separate `/connect` run.

---

# ═══ CONSTRAINTS ═══

**Never:**
- Edit the target note or any other note
- Edit indexes
- Add "related" connections without specific reasoning
- Force connections that are not there
- Skip the articulation test
- Install software — if a tool (e.g. qmd) is missing, fall back or bail with an error

**Always:**
- Save the report to the workshop
- Verify candidate note paths exist
- Explain WHY connections exist
- Note bidirectional candidates (both directions worth linking)
- Capture discovery trace as you work
- Run the reflection step (Phase 5) and append observations to kb/log.md

---

# ═══ PHASE 5: REFLECTION ═══

After saving the connection report, review what you noticed during traversal and append observations to `kb/log.md`.

During Phases 1-3 you read the index, topic indexes, and many individual notes. You may have noticed improvement opportunities that are outside the scope of the current connect task. **Do not fix them — just log them.**

## What to log

Append one line per observation using the format: `- path/to/note.md: what needs improving`

Anything you noticed that could improve the KB is worth logging — structural issues, content quality, logical problems, redundancies. Examples include weak descriptions, topic-as-title, missing index membership, stale links, missing connections, orphan notes, errors in reasoning, style problems, duplication across notes, area gaps. Use your judgment — if it caught your attention during traversal, log it.

## Rules

- Only log things you actually noticed during THIS traversal — don't re-read notes to look for problems
- Skip if you genuinely noticed nothing — an empty reflection is fine, don't fabricate observations
- Each entry is one line. No explanations, no fixes, no follow-up actions
- This is the lowest-friction capture in the system — keep it that way
