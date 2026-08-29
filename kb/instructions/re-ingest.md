---
description: Re-ingest a source whose .ingest.md report is stale — regenerate the analysis against current KB state, then update all notes that reference the old report.
type: kb/types/instruction.md
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
3. Read `source` and `snapshot_sha256` from ingest frontmatter. Reject the
   retired `source_snapshot` and `code_revisions` fields if present.
4. Derive the only eligible snapshot by name: an ingest at
   `kb/sources/<slug>.ingest.md` pairs with
   `kb/sources/.snapshots/<slug>.md`. Do not search for another snapshot by
   checksum. If the named file is missing, invoke `cp-skill-snapshot-web` on
   `source` and continue only if it returns that exact path.
5. Require the snapshot frontmatter `source` to equal the ingest's canonical
   `source`. Hash the exact named snapshot bytes and retain the incumbent and
   observed lowercase SHA-256 values for reporting.

## Step 1: Re-ingest

Invoke `cp-skill-ingest` with this exact request first:

```yaml
re_ingest_request:
  ingest_path: <exact ingest path>
  snapshot_path: <name-paired snapshot path>
```

Add `occasion: <question or job>` only when the user re-ingests for a new
purpose; otherwise the incumbent's `occasion` field carries through unchanged.

If the named snapshot checksum differs, this call stops without changing the
ingest. Disclose the canonical source, both paired paths, and both checksums.
The recorded observation is immutable: capture changed bytes under a distinct
snapshot basename and ingest them to a distinct report instead of changing the
incumbent `snapshot_sha256`. This applies even when Quotes is empty because an
inbound link marked `(snapshot required)` may depend on those exact bytes.

If the incumbent has no Quotes section during the corpus migration, treat it as
the canonical empty section; do not infer quotes from its other sections. A
same-checksum refresh retains the incumbent Quotes section exactly.

The ingest skill runs connection discovery, delegates fresh analysis, and
accepts an overwrite only after exact Quotes preservation, handoff checks, and
full validation. Before any worker sees an existing output, it creates and
verifies an exact-byte backup outside `kb/`. If the primary and single repair
attempt both fail, it restores and verifies the incumbent bytes before
reporting failure.

The new report reflects the current KB — new notes that didn't exist during the original ingest will appear as connections, and stale connections to deleted/renamed notes will be dropped.

## Step 2: Confirm the accepted report

Continue only after `cp-skill-ingest` reports a validated replacement. Read the
accepted `.ingest.md` and audit:

1. **Link health** — every relative link resolves to an existing file.
2. **Section completeness** — Quotes, Classification, Summary, Connections Found, Extractable Value, Recommended Next Action are all present.
3. **Connection quality** — relationship types (validates, extends, grounds, contrasts, exemplifies) are specific, not vague.
4. **No stale project references** — no references to project names, systems, or concepts that no longer exist in this KB.

If any check fails, report the post-success discrepancy. Do not edit the
validated ingest or dispatch a second drafting pass from this procedure.

## Step 3: Audit inbound links

Search the entire KB for markdown links pointing to this `.ingest.md` file:

```bash
rg -n "<ingest-filename>" kb/ --glob "*.md"
```

Exclude:
- The ingest file itself (self-references)

For each hit:

1. **Read the linking note** around the matched line.
2. **Check whether the reference still holds.** The link URL is unchanged (same filename), but the note may quote or paraphrase specific content from the old ingest. Common patterns:
   - Note cites the ingest's analysis rather than using it as source evidence → verify the analytical reference still holds
   - Note references an extractable value item → verify the item still exists or has an equivalent
   - Note uses the ingest as source evidence → verify its claim against retained Quotes, or against the checksum-verified snapshot when the link text contains `(snapshot required)`
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

- Do not delete or edit the old `.ingest.md` manually — `cp-skill-ingest` owns
  overwrite, validation, and handled-failure restoration.
- Do not modify the source snapshot or replace its durable checksum.
- Do not search for a checksum-matching snapshot under another name.
- Do not rewrite the validated ingest during the post-success audit.
- Do not batch multiple re-ingests in one run. Each re-ingest may change the KB state that the next one depends on.
