# V1 ingest and local source shape

**Status:** accepted P1 contract. This fixes field names, local paths, and the
permitted body diff. It does not add another feature choice.

## Durable ingest fields

V1 moves the durable capture record onto the tracked ingest:

| Field | Cardinality | Meaning |
|---|---:|---|
| `source` | exactly one | Canonical external URL of the primary source. Preserve an immutable version in the URL when the selected source already has one. |
| `captured` | exactly one | Date or datetime of the observation represented by the snapshot. |
| `capture` | exactly one | Capture mechanism, using the current values such as `web-fetch`, `pdf-read`, `xdk`, or `gh-api`. |
| `genre` | exactly one | Genre of the primary source. This moves durable genre authority from the local snapshot to the ingest. |
| `snapshot_sha256` | exactly one | Lowercase SHA-256 of the exact bytes of the primary Markdown snapshot. |
| `secondary_sources` | zero or one list | Additional external sources that have an implemented role in this ingest. Omit the field when empty. |

Capture-adapter metadata also moves to the ingest under its existing flat field
names. Examples include `status_id`, `conversation_id`, `post_count`, and
`api_url`. V1 does not introduce a generic metadata container or a closed
adapter-field vocabulary. A capture-generated field is copied unchanged unless
it collides with an existing ingest field; any collision gets an explicit P3
migration disposition instead of an automatic rename. The ingest's existing
`description` and `domains` remain analysis metadata, not copies of a local
snapshot's optional editorial description or tags.

Each `secondary_sources` item has exactly two fields:

| Field | V1 value |
|---|---|
| `role` | `implementation` |
| `source` | Immutable GitHub commit URL with a 40-character commit SHA. |

`implementation` means that the named revision was inspected as implementation
evidence for the primary source. The field does not by itself prove that the
repository is official, that it faithfully implements the source, or that any
reported result was reproduced. Those judgments remain in `Code Grounding`.

The old `source_snapshot` and `code_revisions` fields are removed rather than
retained as aliases. Existing fields `description`, `ingested`, `type`, and
`domains` keep their current meaning. The local snapshot's `type` value is not
copied because the tracked artifact is an `ingest-report`.

Mechanically, the ingest schema requires:

- `source` to start with `http://` or `https://`;
- `captured` to be a date or datetime;
- `capture` to be a non-empty string;
- `genre` to use the existing open genre vocabulary and warning behavior;
- `snapshot_sha256` to match `[0-9a-f]{64}`;
- `secondary_sources`, when present, to be a non-empty unique array;
- every secondary item to contain only `role` and `source`;
- `role` to equal `implementation` in v1;
- an implementation `source` to match
  `https://github.com/{owner}/{repo}/commit/{40-character-sha}`;
- `Code Grounding` when `secondary_sources` is present;
- `source_snapshot` and `code_revisions` to be rejected.

## Ordinary ingest example

This uses the existing position-bias announcement ingest as the worked case.

### Before

```yaml
---
description: "Lech Mazur's public benchmark announcement compressing the headline position-bias result, the GPT-5.4 callout, and the operational motivation from everyday comparison prompts"
source_snapshot: "kb/sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order.md"
ingested: "2026-04-23"
type: kb/sources/types/ingest-report.md
domains: [evaluation, judge-reliability, position-bias, llm-as-judge]
---
```

### After

```yaml
---
description: "Lech Mazur's public benchmark announcement compressing the headline position-bias result, the GPT-5.4 callout, and the operational motivation from everyday comparison prompts"
source: https://x.com/LechMazur/status/2046661738339430489
captured: "2026-04-23T16:14:07.941709+00:00"
capture: xdk
genre: tool-announcement
snapshot_sha256: 3c94142effca7a513279544e767d68b4ac424acd5b21020250f50e03709b92dd
status_id: 2046661738339430489
conversation_id: 2046661738339430489
post_count: 13
ingested: "2026-04-23"
type: kb/sources/types/ingest-report.md
domains: [evaluation, judge-reliability, position-bias, llm-as-judge]
---
```

There is no empty `secondary_sources` field.

### Permitted body diff

Before:

```markdown
# Ingest: Thread by @LechMazur

Source: kb/sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order.md
Captured: 2026-04-23T16:14:07.941709+00:00
From: https://x.com/LechMazur/status/2046661738339430489

## Classification

Type: tool-announcement -- this is a public launch thread for a new benchmark/repo rather than the benchmark artifact itself; it highlights headline findings, links to the repository, and frames why the failure mode matters.
Domains: evaluation, judge-reliability, position-bias, llm-as-judge
Author: Lech Mazur is the benchmark author.
```

After:

```markdown
# Ingest: Thread by @LechMazur

## Classification

This is a public launch thread for a new benchmark/repo rather than the benchmark artifact itself; it highlights headline findings, links to the repository, and frames why the failure mode matters.
Author: Lech Mazur is the benchmark author.
```

The exact v1 body rules are:

- Remove the pre-heading `Source:` snapshot path because `source` is now the
  durable source identity and the local path is not portable.
- Remove the pre-heading `From:` line because it exactly repeats `source`.
- Remove the pre-heading `Captured:` line because it exactly repeats
  `captured`. `ingested` remains the separate date of the analysis.
- Remove a `Domains:` line that exactly repeats the existing `domains` field.
- In `Classification`, remove the `Genre: {genre}` or `Type: {genre}` display
  prefix. Keep its justification as ordinary prose, as in the example.
- Keep `Author:` and every existing analytical section.
- Do not shorten, reorder, or otherwise rewrite `Summary`, `Connections Found`,
  `Extractable Value`, `Limitations (our opinion)`, or `Recommended Next
  Action` as part of this migration.

These rules apply only to the metadata preamble and classification display
lines. A later source URL, genre, or domain mention remains when it supports an
argument rather than displaying metadata.

## Code-grounded ingest example

This schema fixture shows the required multi-repository shape. The checksum
and two implementation URLs are syntactically valid illustrative values, not
claims about a real paper. Their role is to make cardinality and validation
exact.

### Before

```yaml
---
description: "A code-grounded paper ingest"
source_snapshot: "paper-v1.md"
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [agentic-systems, evaluation]
code_revisions:
  - https://github.com/example/implementation-a/commit/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  - https://github.com/example/implementation-b/commit/bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
---
```

### After

```yaml
---
description: "A code-grounded paper ingest"
source: https://arxiv.org/abs/2608.12345v1
captured: "2026-08-22"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ingested: "2026-08-22"
type: kb/sources/types/ingest-report.md
domains: [agentic-systems, evaluation]
secondary_sources:
  - role: implementation
    source: https://github.com/example/implementation-a/commit/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  - role: implementation
    source: https://github.com/example/implementation-b/commit/bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
---
```

The current `Code Grounding` section remains. Delete a standalone sentence or
list whose only content is the repository revision already present in
`secondary_sources`. Keep:

- why each repository belongs to the primary source;
- which claim-bearing files were inspected;
- implemented, artifact-supported, and primary-source-only distinctions;
- what was executed;
- pinned file and directory citations used as evidence;
- any source association, limitation, or result-reproduction qualification.

For example, this pure inventory sentence is removed:

```markdown
The official repository was reviewed at commit [65421c…](https://github.com/spade-rl/spade/commit/65421ccb15a6d501ad6217bd969816146da15e11).
```

This analytical sentence remains:

```markdown
The repository is the paper's official release, but no inspected result bundle linked that revision to the reported benchmark outcomes.
```

## Local source materialization

Tracked ingest reports remain at:

```text
kb/sources/<slug>.ingest.md
```

Primary source snapshots and their capture companions live under the ignored
directory:

```text
kb/sources/.snapshots/<slug>.md
kb/sources/.snapshots/<slug>.<capture-companion-extension>
```

V1 uses a flat directory and keeps the capture tool's current slug. The whole
`/kb/sources/.snapshots/` directory is ignored. It is not published, packaged,
or linked from tracked KB artifacts.

A local snapshot may keep the capture tool's existing frontmatter so that a
standalone local capture remains self-describing:

```yaml
---
source: https://x.com/LechMazur/status/2046661738339430489
captured: 2026-04-23T16:14:07.941709+00:00
capture: xdk
genre: tool-announcement
type: kb/sources/types/snapshot.md
status_id: 2046661738339430489
conversation_id: 2046661738339430489
post_count: 13
---
```

`genre` is no longer required or read from the local snapshot. Migrated cache
files may still contain it and the other copied values, but these local copies
have no durable authority. The ingest is the durable authority for source,
capture metadata, genre, and the checksum.

`snapshot_sha256` is computed over the exact bytes of the primary `.md` file
after capture completes. It includes YAML frontmatter, newline representation,
and the presence or absence of a final newline. It excludes capture companions
such as JSON, images, or a downloaded PDF. Moving the file into `.snapshots/`
does not change its checksum; editing either its header or body does. V1 does
not add a companion manifest or hashes for secondary implementation checkouts.

Lookup for an existing ingest is by checksum, not basename:

1. Read `snapshot_sha256` and `source` from the ingest.
2. Hash the Markdown files in `kb/sources/.snapshots/` and select an exact
   checksum match.
3. If exactly one file matches, use it. Its local name and duplicated
   frontmatter are not identity.
4. If none matches, run the existing URL-specific capture adapter for `source`
   and hash the result.
5. If the new capture matches, install it in `.snapshots/` and use it. If it
   differs, report that the source was recaptured but the original observation
   was not reconstructed. The new capture may be read as the current source,
   but it must not silently stand in for the snapshot that grounded the ingest
   or update the ingest's checksum.
6. If more than one local file has the expected checksum, stop and report the
   duplicate paths rather than choosing by filename or modification time.

For a new URL with no ingest yet, the capture adapter's current canonical-URL
deduplication remains the pre-ingest lookup. The ingest command then copies the
capture metadata, computes `snapshot_sha256`, and writes the tracked report.
Changing the durable observation later is an explicit re-ingestion: it updates
the capture fields and checksum together after the analysis is reconsidered.

When ingestion starts from a local snapshot path
`kb/sources/.snapshots/<slug>.md`, its tracked output is still
`kb/sources/<slug>.ingest.md`; it is not written beside the snapshot.

Implementation repositories retain the existing ignored checkout convention:

```text
related-systems/<owner>--<repo>/
```

Their durable identity is the commit URL in `secondary_sources`; the checkout
path never enters ingest frontmatter.

## Two irregular current pointers

These are corpus migrations, not new input modes.

### `position-bias.ingest.md`

Use:

```yaml
source: https://github.com/lechmazur/position_bias/tree/483150e8e1938c17331f9e82f86e41a653286651
captured: "2026-04-21"
capture: git-checkout
genre: code-repository
```

The full revision is recoverable from the current short pin, and the pinned
GitHub tree contains the 27-model/193-pair version described by the ingest. The
current source unit has no surviving primary Markdown snapshot, so this block
cannot truthfully include a checksum yet. P3 first materializes the landing
page, computes its 64-character `snapshot_sha256`, and only then marks this
migration row valid; it must not fabricate a value during planning. The
old `source_snapshot: kb/sources/position-bias/` value is discarded. Remove the
body's `Source:`, `Captured:`, `From:`, `Pin:`, and repeated domain/genre
displays; keep the file manifest and all analysis. If a local reading copy is
needed, materialize the pinned GitHub tree landing page as
`kb/sources/.snapshots/position-bias.md`. Deeper repository inspection uses the
public pinned tree; it does not revive directory ingestion.

### `gentle-coding.ingest.md`

Use:

```yaml
source: https://github.com/OttoRenner/Gentle-Coding
captured: "2026-07-17"
capture: web-fetch
genre: code-repository
snapshot_sha256: 5c99601b818bcc5461e7c7c2fe4d8776773cca417aee8775d197d0739b65bb56
```

The repository is the one primary source. Its README, Proof-of-Concept, and
RESEARCH files are members of that source, not secondary sources with invented
roles. Move the three current captures into `.snapshots/` as local material,
but only `gentle-coding.md` is the primary snapshot identified by the ingest's
checksum. Replace durable links to the other two local files with their
existing public GitHub file URLs. Change “three snapshots captured together”
to “three repository documents read together”; preserve the rest of the
analysis. Do not create a directory-primary workflow or admit a non-v1
secondary role to represent the files.

## P1 acceptance record

The user accepted these exact choices on 2026-08-22:

- top-level `source` and `genre`;
- top-level capture metadata and the exact-file `snapshot_sha256`;
- optional `secondary_sources: [{role, source}]` with only
  `implementation` in v1;
- ignored `kb/sources/.snapshots/` materialization with checksum-first lookup;
- the bounded body-dedup rules above;
- the two one-off irregular migrations.
