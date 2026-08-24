# Draft writing conventions for installed kb/sources/

> Workshop draft. Intended scaffold target:
> `src/commonplace/_data/templates/user-sources-COLLECTION.md`. The
> [installed-source-collection bug fix](./fix-installed-sources-collection.md)
> now owns a generic template and must not adopt the claim-specific clauses
> below. Retain this draft only while moving those clauses into the claim-pull
> type, source-checkout contract, and grounding path; do not promote it
> wholesale.

## Purpose and scope

This collection contains tracked analyses of external sources. Each ingest is a
durable record of one primary source's identity, capture provenance, exact
snapshot checksum, claim grounding, and relevance to this project's goals.

Local reading copies live under the ignored `kb/sources/.snapshots/` directory.
They are immutable capture materializations, not tracked authority or durable
link targets.

## Quality goal

Preserve faithful source identity and bounded claims while making the source's
project-relative value clear. Do not present local interpretation, transfer, or
implementation inference as if the source itself established it.

## Titles, descriptions, and files

- Name an ingest `<snapshot-slug>.ingest.md`.
- Use the primary source's title for the document title.
- Write a retrieval-oriented description that says what the source establishes
  and where it bears on this project.
- Never edit a snapshot after capture or create a durable link into
  `.snapshots/`.

## Grounding and maintenance

The external source is the evidential authority for what it says. The tracked
ingest owns durable local source identity and a `Claims` cache of primary-source
extracts checked against the observation named by `snapshot_sha256`.

A note may cite the ingest as its tracked grounding record. The note must state
which claim it uses and must carry any project-specific transfer argument.
Exact wording is checked from source to ingest when the entry is added or
materially revised. Later quote validation can check a note against the tracked
ingest; that downstream check does not reverify an unavailable snapshot.

Same-checksum re-ingestion preserves the complete `Claims` section exactly.
Changed-checksum re-ingestion with grounded claims stops pending explicit
regrounding or invalidation. Never silently erase the cache or carry it to a
different observation.

V1 grounds primary-source claims only. A claim whose authority is an
implementation repository or another `secondary_sources` entry requires a
resource-aware procedure and must not be checked against the primary snapshot.

## Outbound links

Use links only when they serve a reader of this source analysis. Inline links
carry load-bearing relationships. Footer links use a label plus a context phrase
that states the reader need.

Default labels:

| label | destinations | reader need |
|---|---|---|
| `derived-from` | external | reach the primary source from which this ingest was produced |
| `is-evidence-for` | notes, reference | inspect the local claim or decision this source materially bears on |
| `abstracted-from` | notes | inspect a local claim generalized beyond this source |
| `compares-with` | notes, reference, sources | compare two artifacts on a named shared axis |
| `see-also` | notes, reference, sources, external | inspect a useful adjacent artifact when no stronger relation applies |

Do not link to generated connection reports or machine-local repository
checkouts.

## Type eligibility

Tracked source analyses use `kb/sources/types/ingest-report.md`. Local snapshots
use `kb/sources/types/snapshot.md` under `.snapshots/`. Frontmatter-free Markdown
is implicit `text` only for deliberate unstructured source work.
