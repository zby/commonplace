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
| deep | Full dual discovery (index + semantic search). Evaluate every candidate. Multiple passes. Synthesis opportunity detection. |
| standard | Dual discovery with top 5-10 candidates. Standard evaluation. |
| quick | Single pass — either index or semantic search. Accept obvious connections only. Skip synthesis detection. |

## EXECUTE NOW

**Target: $ARGUMENTS** (exactly one note path or name — if empty, ask which note)

**Step 0: Check workshop.** Look for an active workshop in the conversation context. If none is set, STOP and tell the user: "No active workshop set. Set one with: workshop is kb/work/<name>/". The connection report needs somewhere to go.

**Execute these steps:**

1. Read the target note fully — understand its claim and context
2. **Check note type.** If the target has no frontmatter (a `text` file), run `/convert` on it first to add frontmatter with `status: seedling`.
3. **Throughout discovery:** Capture which indexes you read, which queries you ran (with scores), which candidates you evaluated. This becomes the Discovery Trace.
4. Run Phase 0 (sync search index)
5. Use dual discovery in parallel:
   - Browse relevant index(s) for related notes
   - Run semantic search for conceptually related notes
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

## Workflow

### Phase 0: Sync Search Index

```bash
qmd --index commonplace update && qmd --index commonplace embed
```

### Phase 1: Understand the Note

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

### Phase 2: Discovery (Find Candidates)

Dual discovery: index exploration AND semantic search in parallel. Three-tier fallback for semantic search (MCP → bash qmd → grep-only). Secondary discovery via keyword search, description scan, and link following.

Read `skills/connect/discovery.md` for full methodology.

### Phase 3: Evaluate Connections

Apply the articulation test to every candidate. Use the relationship type vocabulary (extends, grounds, contradicts, exemplifies, synthesizes, enables). Reject vague "related" connections. Check agent traversal value. Watch for synthesis opportunities.

Read `skills/connect/evaluation.md` for full methodology.

### Phase 4: Save Connection Report

Write the report to the workshop directory. Derive the filename from the target note:

```
<workshop>/connect-report-<note-name>.md
```

For example: `kb/work/connect-refactoring/connect-report-frontloading-spares-execution-context.md`

Read `skills/connect/output-format.md` for the report template.

## Quality Gates

Before saving the report, verify:

1. **Articulation test** — every connection has a specific reason, not just "related"
2. **Candidate verification** — every candidate note path actually exists
3. **No forced connections** — if nothing genuine was found, report that honestly

Read `skills/connect/quality-gates.md` for edge case handling (no connections found, split detection, conflicting notes).

## Critical Constraints

**Never:**
- Edit the target note or any other note
- Edit indexes
- Add "related" connections without specific reasoning
- Force connections that are not there
- Skip the articulation test

**Always:**
- Save the report to the workshop
- Verify candidate note paths exist
- Explain WHY connections exist
- Note bidirectional candidates (both directions worth linking)
- Capture discovery trace as you work
