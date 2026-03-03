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

1. **No target** — list `kb/sources/` recent `.md` files (excluding .json, .ingest.md), then ask which to ingest.

2. **URL** (starts with `http://` or `https://`) — invoke `/snapshot-web <url>` to capture it. `/snapshot-web` handles all URL types (web pages, PDFs, GitHub, X/Twitter).

   Parse the "Snapshot saved:" line from the output to get the file path. That becomes the input for Step 1.

3. **File path** — start Step 1 immediately.

**START NOW.**

---

## Step 1: Set Up Workshop

Once you have the snapshot file path (from URL resolution or direct input), create a workshop directory derived from the snapshot filename:

```bash
mkdir -p kb/work/ingest-<source-slug>/
```

For example: `kb/sources/some-article.md` → `kb/work/ingest-some-article/`

The workshop holds the connection report and any other artifacts from this ingestion.

## Step 2: Run /connect on the Snapshot

Run discovery-only connection finding directly on the snapshot — no working copy needed:

```
/connect {path to snapshot file}
```

This produces a connection report in the active workshop: `<workshop>/connect-report-<name>.md`

The report contains:
- Discovery trace (what was searched, what matched)
- Connections found with relationship types and reasons
- Rejected candidates
- Index membership recommendations
- Synthesis opportunities and flags

Wait for `/connect` to complete before proceeding.

## Step 3: Read Connection Report

Read the connection report from the workshop. Note:
- Which `kb/notes/` files were identified as connections
- What relationship types were found
- Any synthesis opportunities or tensions flagged

This is your connection context for the analysis below.

## Step 4: Produce the Ingestion Report

Write the analysis, informed by the connections found in Steps 2-3.

### 3.1 Classification

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

### 3.2 Summary

One paragraph. What is the source about? What is the author's main thesis or
contribution? Write for someone deciding whether to read the full source.

### 3.3 Connections Found

Summarise what `/connect` discovered. Which existing notes does this source
connect to, and how? Include the relationship types and the key insight about
how this source fits (or doesn't) into our existing knowledge graph.

### 3.4 Extractable Value

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

### 3.5 Recommended Next Action

Pick ONE and be specific:

- "Write a note titled 'X' connecting to Y.md and Z.md — it would argue [thesis]"
- "Update existing-note.md: add a section about X because [reason]"
- "Brainstorm session: this source raises questions about [topic] — explore with [specific questions]"
- "File as reference — interesting but doesn't change our thinking or practices"

## Step 5: Save the Report

Save the report next to the snapshot as `.ingest.md`:

- Input:  `kb/sources/some-article.md`
- Output: `kb/sources/some-article.ingest.md`

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

## Critical Constraints

**never:**
- Extract atomic claims — this is ingestion, not decomposition
- Write any files other than `.ingest.md`
- Modify any files in kb/notes/ — that happens in later steps if the human decides to proceed
- Hallucinate connections — if the source isn't relevant, say so
- Skip running /connect — the connections are the foundation of the analysis

**always:**
- Run /connect before doing classification or value extraction
- Base extractable value on what's NEW relative to connections found
- Be specific in the recommended action
- Include effort tags on extractable value items
