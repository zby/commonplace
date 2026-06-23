---
name: cp-skill-ingest
description: Use when asked to ingest a URL or existing kb/sources snapshot into a .ingest.md source analysis.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[url-or-file] — URL (https://...) or path to .md file in kb/sources/. No argument lists recent snapshots."
---

# Ingest source

Ingest one source into a `kb/sources/*.ingest.md` report. The source may be a
URL or an existing Markdown snapshot under `kb/sources/`.

## Contract

**Target:** `$ARGUMENTS`

The direct output is the `.ingest.md` report next to the source snapshot. URL
snapshotting and connection discovery may write their own delegated artifacts.
Do not directly write any other library artifacts.

Interpret "our" through the installed KB's goals and local collection contracts.
In this repository, "our" means agent-operated KB methodology. In another
installed KB, it means that project's declared system, work, codebase, policy,
product, or domain.

Read and follow `kb/sources/types/ingest-report.md` before drafting the report.
If this skill and the type spec conflict about report content, the type spec
wins.

## Steps

1. **Resolve the target.**
   - If `$ARGUMENTS` is empty, list recent `kb/sources/*.md` files excluding
     `.json` and `.ingest.md`, then ask which one to ingest.
   - If the target starts with `http://` or `https://`, invoke
     `cp-skill-snapshot-web` on the URL. Parse the `Snapshot saved:` line from
     its output; that path is the source snapshot for the next step.
   - Otherwise, treat the target as the source snapshot path.

2. **Run connection discovery.**
   Invoke `cp-skill-connect` on the source snapshot path. Wait for it to finish.
   For source snapshots, read
   `kb/reports/connect/sources/<snapshot-name>.connect.md`.

3. **Extract connection context.**
   From the generated connect report, note:
   - Which existing artifacts were identified as connections
   - What relationship types were found
   - Any synthesis opportunities or tensions flagged

   Treat `Maintenance Observations` as non-actionable context: mention durable
   signals in the ingest report only when relevant, and do not act on or promote
   them during ingest.

   The connect report is generated, gitignored working context. Do not cite it,
   link to it, or name its path in the durable ingest report. Summarize its
   findings and link only durable KB artifacts or source snapshots.

4. **Draft the ingest report.**
   Write the analysis as an `ingest-report`, using the source snapshot and the
   connection context. The report must classify the source, summarize it,
   explain how it connects to the current KB, extract goal-relative value, state
   limitations, and recommend one advisory next action.

   If the source is not relevant to this KB, say so in the report. Keep the
   report short, explain the mismatch, and recommend no promotion or source-only
   filing as appropriate.

5. **Save the report next to the snapshot.**
   - Input: `kb/sources/some-article.md`
   - Output: `kb/sources/some-article.ingest.md`

6. **Validate.**
   Run:

   ```bash
   commonplace-validate kb/sources/some-article.ingest.md
   ```

   If this run created or edited the source snapshot, validate that snapshot too.
   Fix validation failures in files this skill is allowed to write before
   stopping.

7. **Report the result.**
   Tell the user where the ingest report was saved and state the recommended
   next action.

## Constraints

- Run `cp-skill-connect` before classification or value extraction.
- Write only the `.ingest.md` report directly.
- Base extractable value on what is new relative to the discovered connection
  context.
- Include effort tags on extractable value items.
- Recommend exactly one advisory next action.
