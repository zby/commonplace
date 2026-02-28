---
name: ingest
description: Ingest a source into the knowledge base. Accepts a URL (GitHub, X/Twitter, or web page) or a path to an existing snapshot. URLs are snapshotted first, then the snapshot is classified, connected, and analysed. Saves report as .ingest.md. Triggers on "/ingest", "/ingest [url-or-file]".
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[url-or-file] — URL (https://...) or path to .md file in kb/sources/. No argument lists recent snapshots."
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse the target to determine what to do:

1. **No target** — list `kb/sources/` recent `.md` files (excluding .json, .ingest.md, .working.md), then ask which to ingest.

2. **URL** (starts with `http://` or `https://`) — invoke `/snapshot-web <url>` to capture it. `/snapshot-web` handles all URL types (web pages, PDFs, GitHub, X/Twitter).

   Parse the "Snapshot saved:" line from the output to get the file path. That becomes the input for Step 1.

3. **File path** — start Step 1 immediately.

**START NOW.**

---

## Step 1: Create Working Copy

Copy the snapshot file using `cp`. The snapshot already has YAML frontmatter
that's sufficient for /connect to work with. No rewriting needed.

```bash
cp "{input_path}" "{input_path%.md}.working.md"
```

- Input:  `kb/sources/some-article.md`
- Working: `kb/sources/some-article.working.md`

## Step 2: Run /connect on the Working Copy

Invoke the /connect skill on the working copy:

```
/connect {path to .working.md file}
```

This runs full connect-style discovery: index exploration, semantic search,
keyword search, articulation-tested connections. /connect will write links
INTO the working copy pointing at real docs/notes/ files.

**Note:** /connect also adds reverse links FROM KB notes back TO the working
copy (bidirectional linking). These reverse links will point to the
`.working.md` file. Step 5b fixes these before the working copy is deleted.

Wait for /connect to complete before proceeding.

## Step 3: Read Connected Working Copy

Read the working copy after /connect has annotated it. Note:
- Which docs/notes/ files were linked
- What relationship types were identified
- Any synthesis opportunities or tensions flagged
- The discovery trace (what was searched, what matched)

This is your connection context for the analysis below.

## Step 4: Produce the Ingestion Report

Now write the analysis, informed by the connections found in Step 2-3.

### 4.1 Classification

**Source type** — pick one and briefly justify:
- **scientific-paper**: Peer-reviewed or preprint with methodology, data, citations
- **practitioner-report**: Someone built something and describes what worked/failed
- **conceptual-essay**: Argues a framing, analogy, or theoretical position
- **design-proposal**: RFC, API design, architecture proposal for a specific system
- **tool-announcement**: New tool, library, or framework release
- **github-issue**: Bug report, feature request, or PR from a specific repo
- **conversation-thread**: Discussion without a single authorial thesis

**Domain tags**: 2-4 topic areas

**Author signal**: One sentence — who is this person, why attend to their
experience? ("unknown" is fine)

### 4.2 Summary

One paragraph. What is the source about? What is the author's main thesis or
contribution? Write for someone deciding whether to read the full source.

### 4.3 Connections Found

Summarise what /connect discovered. Which existing notes does this source
connect to, and how? Include the relationship types and the key insight about
how this source fits (or doesn't) into our existing knowledge graph.

### 4.4 Extractable Value

Based on the source type AND the connections found, look for the RIGHT kind
of value. The connections tell you what's already captured — focus on what's NEW.

**From scientific papers** — look for:
- Empirical findings that support or challenge our theory
- Methods or experimental designs we could adapt
- Data points worth citing (with caveats about context)

**From practitioner reports** — look for:
- Concrete practices: specific things they built/did, with enough detail to replicate
- Lessons learned: what failed and why (often more valuable than what worked)
- Design patterns: recurring structures that transfer beyond their specific system

**From conceptual essays** — look for:
- Framings: new ways to think about something we already do
- Analogies: connections to other domains that illuminate our work
- Provocations: questions or tensions that push our thinking
- Vocabulary: terms or distinctions that name something we've noticed but haven't articulated

**From design proposals / tools** — look for:
- Impact on our stack: does this change how we build?
- Patterns worth borrowing: API design, architecture choices
- Gaps exposed: does this solve something we struggle with?

**From github issues / conversations** — look for:
- Direct relevance to our codebase
- Signals about upstream direction

List 3-7 items, each as a one-liner with enough context to evaluate.
Mark each with a rough effort tag: [quick-win], [experiment], [deep-dive],
[just-a-reference].

### 4.5 Recommended Next Action

Pick ONE and be specific:

- "Write a note titled 'X' connecting to Y.md and Z.md — it would argue [thesis]"
- "Update existing-note.md: add a section about X because [reason]"
- "Brainstorm session: this source raises questions about [topic] — explore with [specific questions]"
- "File as reference — interesting but doesn't change our thinking or practices"

## Step 5: Save the Report

Save the report next to the snapshot as `.ingest.md`:

- Input:  `kb/sources/some-article.md`
- Output: `kb/sources/some-article.ingest.md`

## Step 5b: Rewrite Reverse Links

/connect may have added reverse links from KB notes pointing to the
`.working.md` file. Before deleting the working copy, rewrite these to
point to the snapshot file (the permanent source artifact).

```bash
# Find all files linking to the .working.md
grep -rl "{basename}.working.md" kb/ --include="*.md"
```

For each file found, replace `.working.md` with `.md` in the link target:
- `some-article.working.md` → `some-article.md`

Use `sed` or edit each file. Verify the snapshot file exists at the
rewritten path.

## Step 6: Clean Up Working Copy

Delete the `.working.md` file — it was a scratch space for /connect and is no longer needed:

```bash
rm "{input_path%.md}.working.md"
```

The connections found are preserved in the `.ingest.md` report. The working copy is disposable.

## Output Format

The saved `.ingest.md` file should contain:

```
---
source_snapshot: {input filename}
ingested: {current UTC date}
type: {source-type}
domains: [{tag1}, {tag2}, {tag3}]
---

# Ingest: {source title}

Source: {filename}
Captured: {date from frontmatter}
From: {source URL from frontmatter}

## Classification
Type: {source-type} — {brief justification}
Domains: {tag1}, {tag2}, {tag3}
Author: {credibility signal}

## Summary
{one paragraph}

## Connections Found
{summary of /connect discovery — which notes, what relationships}

## Extractable Value
{numbered list of 3-7 items with effort tags}

## Recommended Next Action
{one specific action}
```

Tell the user where the report was saved and what the recommended action is.

---

## Design Note: Connection Quality

LLMs are good at finding candidate connections but tend to over-connect —
linking everything to everything with plausible-sounding justifications. This
is fine here because the pipeline is advisory, not autonomous. /connect writes
its findings into the .working.md copy, the report summarises them, and the
human evaluates which connections are genuine. No notes are created or modified
in docs/notes/ without human decision.

## Critical Constraints

**never:**
- Extract atomic claims — this is ingestion, not decomposition
- Write any files other than .working.md and .ingest.md
- Modify any files in docs/notes/ — that happens in later steps if the human decides to proceed
- Hallucinate connections — if the source isn't relevant, say so
- Skip running /connect — the connections are the foundation of the analysis

**always:**
- Run /connect before doing classification or value extraction
- Base extractable value on what's NEW relative to connections found
- Be specific in the recommended action
- Include effort tags on extractable value items
