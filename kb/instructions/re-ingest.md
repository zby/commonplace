---
description: Re-ingest a source whose .ingest.md report is stale — regenerate the analysis against current KB state, then update all notes that reference the old report.
---

# Re-Ingest

**Target: $ARGUMENTS** — the `.ingest.md` filename (e.g. `simon-willison-karpathy-claws.ingest.md`) or path.

If target is empty, list `.ingest.md` files and ask which to re-ingest.

## When to use

- The KB has evolved since ingestion and the connections/extractable value are stale
- The original ingest has broken links, missing descriptions, or references to old project names
- You want to re-evaluate a source against notes written after the original ingest

## Prerequisites

1. Resolve the target to a full path under `kb/sources/`. If only a filename was given, prepend `kb/sources/`.
2. Verify the `.ingest.md` file exists.
3. Identify the source snapshot: read the `source_snapshot` frontmatter field. Verify the snapshot file exists in `kb/sources/`.

## Step 1: Re-ingest

Run `/ingest <snapshot-file-path>` on the source snapshot.

This will:
- Set up a workshop
- Run `/connect` against current KB state
- Produce a fresh analysis
- Overwrite the `.ingest.md` file

The new report reflects the current KB — new notes that didn't exist during the original ingest will appear as connections, and stale connections to deleted/renamed notes will be dropped.

## Step 2: Review the new report

Read the newly generated `.ingest.md`. Check:

1. **Link health** — every relative link resolves to an existing file.
2. **Section completeness** — Classification, Summary, Connections Found, Extractable Value, Recommended Next Action are all present.
3. **Connection quality** — relationship types (validates, extends, grounds, contrasts, exemplifies) are specific, not vague.
4. **No stale project references** — no references to project names, systems, or concepts that no longer exist in this KB.

If any check fails, fix the report in place before proceeding.

## Step 3: Update inbound links

Search the entire KB for markdown links pointing to this `.ingest.md` file:

```bash
rg -n "<ingest-filename>" kb/ --glob "*.md"
```

Exclude:
- `kb/sources/index.md` (auto-generated, will rebuild)
- The ingest file itself (self-references)

For each hit:

1. **Read the linking note** around the matched line.
2. **Check whether the reference still holds.** The link URL is unchanged (same filename), but the note may quote or paraphrase specific content from the old ingest. Common patterns:
   - Note cites a specific claim from the ingest summary → verify the new summary still supports it
   - Note references an extractable value item → verify the item still exists or has an equivalent
   - Note uses the ingest as evidence for an argument → verify the new ingest still provides that evidence
3. **If the reference holds** — no change needed.
4. **If the reference is broken or misleading** — update the linking note:
   - Rewrite the sentence to match the new ingest content
   - If the ingest no longer supports the claim at all, remove or replace the reference
   - If the new ingest supports the claim differently, update the framing

Report each linking note and what you did (kept / updated / removed reference).

## Step 4: Report

Summarize what changed:

```
=== RE-INGEST: {filename} ===

Inbound links checked: {count}
  Unchanged: {count}
  Updated: {list with one-line explanation each}
  Removed: {count}

Issues fixed: {broken links, missing description, stale references — or "none"}
===
```

## Do NOT

- Do not delete the old `.ingest.md` manually — `/ingest` overwrites it.
- Do not update `kb/sources/index.md` — it auto-generates.
- Do not modify the source snapshot.
- Do not batch multiple re-ingests in one run. Each re-ingest may change the KB state that the next one depends on.
