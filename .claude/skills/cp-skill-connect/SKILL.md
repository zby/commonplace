---
name: cp-skill-connect
description: Discover connections for a single note. Writes a connect-report under kb/reports/connect/ without mutating library notes or indexes. Use with a note path or note name.
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
---

# Connect — Discovery Only

Find connections for a single note. Output is a connection report saved under `kb/reports/connect/`. Library notes and indexes are not edited.

The connection report is an artifact that can be reviewed, debugged, and used as input to directed reading for actual file mutations.

## Input

Target: `$ARGUMENTS` — exactly one note path or note name. If no target is provided, ask which note to connect.

## Output

Write a `connect-report` artifact under `kb/reports/connect/`. Before writing the report, read:

- `kb/reports/types/connect-report.instructions.md`
- `kb/reports/types/connect-report.template.md`

Derive the report filename from the target note:

```bash
kb/reports/connect/<note-name>.connect.md
```

For example: `kb/reports/connect/frontloading-spares-execution-context.connect.md`.

Because this skill writes reports under `kb/reports/connect/`, body links to KB notes use paths like `[note-title](../../notes/note-title.md)` and body links to KB sources use paths like `[source-title](../../sources/source-title.md)`.

After saving, tell the user: `Report saved: <full path>`.

## Depth

Active depth: standard.

| Depth | Discovery Behavior |
|-------|-------------------|
| deep | Full discovery (all steps). Evaluate every candidate. Multiple passes. Synthesis opportunity detection. |
| standard | Full discovery with top 5-10 candidates. Standard evaluation. |
| quick | Single pass — index scan only. Accept obvious connections only. Skip synthesis detection. |

## Workflow

1. Ensure `kb/reports/connect/` exists.
2. Read the target note fully — understand its claim and context.
3. Check note type. If the target has no frontmatter (a `text` file), continue discovery from its title/body and mark the report as provisional. Do not run convert as part of connect.
4. Throughout discovery, capture actual query strings, scores, and which candidates you evaluated or rejected. This becomes the Discovery Trace.
5. Run Phase 0 (sync search index).
6. Run discovery: index scan → topic indexes → semantic search → keyword search → link following.
7. Evaluate candidates using the connection standards in `kb/reports/types/connect-report.instructions.md`.
8. Save the `connect-report` artifact to `kb/reports/connect/`.

## Search Scope

Discovery scans three collections under `kb/`:

| Directory | Contains |
|-----------|----------|
| `kb/notes/` | Main KB — claims, design notes, research |
| `kb/sources/` | Snapshotted external sources |
| `kb/instructions/` | Reusable procedures and skills |

---

# ═══ PHASE 0: SYNC SEARCH INDEX ═══

**Prerequisite check:** Before running qmd, verify it exists:
```bash
command -v qmd
```
If qmd is not found, log "qmd unavailable — skipping index sync, using grep-only fallback for semantic search" and skip directly to Phase 1. **Never attempt to install qmd or any other software.**

If qmd is available:
```bash
qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed
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
qmd --index "$COMMONPLACE_QMD_INDEX" query "[note's core concepts]" --collection notes -n 15
qmd --index "$COMMONPLACE_QMD_INDEX" query "[note's core concepts]" --collection sources -n 10
qmd --index "$COMMONPLACE_QMD_INDEX" query "[note's core concepts]" --collection instructions -n 5
```

Record the actual query string and top results with scores in the discovery trace.

**Tier 2 — grep only:** If qmd was unavailable or errors, log "qmd unavailable" and rely on index + keyword search only. **Never attempt to install qmd.**

## Step 4: Keyword Search

For specific terms and exact matches — search notes and sources:
```bash
rg "term" kb/notes/ kb/sources/ kb/instructions/ --glob "*.md"
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

Evaluate candidates and synthesis opportunities using `kb/reports/types/connect-report.instructions.md`. Do not create synthesis notes or mutate library artifacts during connect.

---

# ═══ PHASE 4: SAVE CONNECTION REPORT ═══

Write the report to `kb/reports/connect/` using the `connect-report` type template and instructions:

- `kb/reports/types/connect-report.instructions.md`
- `kb/reports/types/connect-report.template.md`

Derive the filename from the target note as `kb/reports/connect/<note-name>.connect.md`. After saving, tell the user: `Report saved: <full path>`.

---

# ═══ CONSTRAINTS ═══

**Never:**
- Edit the target note or any other note
- Edit indexes
- Add "related" connections without specific reasoning
- Force connections that are not there
- Install software — if a tool (e.g. qmd) is missing, fall back or bail with an error

**Always:**
- Save the report to `kb/reports/connect/`
- Apply `kb/reports/types/connect-report.instructions.md`
- Capture discovery trace as you work
- Run the reflection step (Phase 5) and append observations to kb/log.md

---

# ═══ PHASE 5: REFLECTION ═══

After saving the connection report, review what you noticed during traversal and append observations to `kb/log.md`.

During Phases 1-3 you read the index, topic indexes, and many individual notes. You may have noticed improvement opportunities that are outside the scope of the current connect task. **Do not fix them — just log them.**

## What to log

Append one line per observation using the format: `- path/to/note.md: what needs improving`

Anything you noticed that could improve the KB is worth logging — structural issues, content quality, logical problems, redundancies. Examples include weak descriptions, topic-as-title, missing index membership, stale links, missing connections, orphan notes, errors in reasoning, style problems, duplication across notes, area gaps.

**Abstraction opportunities** are especially worth logging: if you noticed multiple notes sharing structure that isn't yet named by any existing note, log it. The signal is link annotations that use similar language across different connections (e.g., three notes all linked as "analogous spectrum" to different targets) or the same mechanism described in different vocabulary across notes. The highest-value act in a knowledge system is creating a note that names a shared mechanism — logging the opportunity here is the capture step. Format: `- ABSTRACTION: [which notes] share [what unnamed structure]`

Use your judgment — if it caught your attention during traversal, log it.

## Rules

- Only log things you actually noticed during THIS traversal — don't re-read notes to look for problems
- Skip if you genuinely noticed nothing — an empty reflection is fine, don't fabricate observations
- Each entry is one line. No explanations, no fixes, no follow-up actions
- This is the lowest-friction capture in the system — keep it that way
