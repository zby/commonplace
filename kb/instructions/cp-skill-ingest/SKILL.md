---
name: cp-skill-ingest
description: Ingest a source into the knowledge base. Accepts a URL (GitHub, X/Twitter, or web page) or a path to an existing snapshot. URLs are snapshotted first, then the snapshot is classified, connected, and analysed. Saves the report as .ingest.md.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[url-or-file] — URL (https://...) or path to .md file in kb/sources/. No argument lists recent snapshots."
---

## EXECUTE NOW

**Target: $ARGUMENTS**

The skill owns execution. The type owns the report contract.
Use this skill for routing, setup, tool use, delegated skill calls, and file writes.
Use the loaded type spec for section meanings, quality standards, and the template.
If the skill and type both mention the same report-content rule, prefer the type.

Interpret "our" through the installed KB's goals and local collection contracts. In this repository, "our" means agent-operated KB methodology. In another installed KB, it means that project's declared system, work, codebase, policy, product, or domain.

Parse the target to determine what to do:

1. **No target** — list `kb/sources/` recent `.md` files (excluding .json, .ingest.md), then ask which to ingest.
2. **URL** (starts with `http://` or `https://`) — invoke the `cp-skill-snapshot-web` skill to capture it. The `cp-skill-snapshot-web` skill handles all URL types (web pages, PDFs, GitHub, X/Twitter). Parse the "Snapshot saved:" line from the output to get the file path. That becomes the input for Step 1.
3. **File path** — proceed to Step 1.

**START NOW.**

---

## Step 1: Run the `cp-skill-connect` skill on the snapshot

Once you have the snapshot file path (from URL resolution or direct input), run discovery-only connection finding with the `cp-skill-connect` skill on that path.

This saves the connection report at `kb/reports/connect/<source-collection>/<snapshot-name>.connect.md`. For source snapshots, read `kb/reports/connect/sources/<snapshot-name>.connect.md`.

The report contains candidate connection context for the ingest analysis. Treat its `Maintenance Observations` section as non-actionable context: you may mention durable signals in the ingest report when relevant, but do not act on or promote them.

Wait for the `cp-skill-connect` skill to complete before proceeding.

## Step 2: Read Connection Report

Read the connection report from `kb/reports/connect/sources/<snapshot-name>.connect.md`. Note:

- Which existing artifacts were identified as connections
- What relationship types were found
- Any synthesis opportunities or tensions flagged

This is your connection context for the analysis below.

## Step 3: Produce the Ingestion Report

Write the analysis as an `ingest-report`, informed by the connections found in Steps 1-2. Before writing the report, read:

- `kb/sources/types/ingest-report.md`

Use the type spec's source-type list, extraction standards, limitations guidance, recommended-action guidance, and template. The report should classify the source, summarize it, explain its connections, extract goal-relative value, state limitations, and recommend one advisory next action.

## Step 4: Save the Report

Save the `ingest-report` next to the snapshot as `.ingest.md`:

- Input:  `kb/sources/some-article.md`
- Output: `kb/sources/some-article.ingest.md`

Ingest's own direct write is only the `.ingest.md` report. Delegated steps may write their own artifacts: snapshot capture may write a snapshot, and connect may write a connect report. Do not directly modify notes, reference docs, instructions, runbooks, policies, ADRs, indexes, collection files, or logs. Promotion belongs to a later explicit step.

## Output Format

Use the template from `kb/sources/types/ingest-report.md`.

Tell the user where the report was saved and what the recommended action is.

## Critical Constraints

**never:**

- Extract atomic claims — this is ingestion, not decomposition
- Write any files directly other than `.ingest.md`
- Modify notes, reference docs, instructions, runbooks, policies, ADRs, indexes, collection files, or logs
- Hallucinate connections — if the source isn't relevant, say so
- Skip running the `cp-skill-connect` skill — the connections are the foundation of the analysis

**always:**

- Run the `cp-skill-connect` skill before doing classification or value extraction
- Base extractable value on what's NEW relative to connections found
- Be specific in the recommended action
- Include effort tags on extractable value items
